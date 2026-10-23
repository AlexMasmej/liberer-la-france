"""Single-file technical repair under the existing supervisor; no launch API.

The six-module review reallocation package is deliberately never imported.
All checks run before mutation. Any failure leaves the owned pause in place.
"""
from contextlib import ExitStack
from pathlib import Path
import fcntl
import hashlib
import json
import os
import runpy
import stat
import sys
import tempfile
import time

PROOF=Path(__file__).resolve().parent
ROOT=PROOF.parents[1]
PREP=ROOT/'runtime/false-usage-classification-20261023T0943Z'
sys.path.insert(0,str(ROOT))
import supervise_exhaustive as supervisor
from worker_capacity import settings

BASELINE='1c66699d0b54334c099460546c8bd1cfced0a831336a544caf17b7b928538f7e'
CANDIDATE='e950a288939012b1915f180a7cc80987b5e79452e08eab7b9a4cd4a4f7a3a0db'
PAUSE='56afa06903a7e52346f17f5d937844c9d16160f68dce473c8837aa94fc4a009c'
OWNER='false-usage-classification-20261023T0943Z-f7e28488-2bc7-4a9f-8113-ee14df0a6198'


def digest(data):return hashlib.sha256(data).hexdigest()


def raw(path):
    path=Path(path)
    if path.is_symlink() or not path.is_file() or not stat.S_ISREG(path.stat().st_mode):
        raise RuntimeError('Unknown regular evidence: '+str(path))
    return path.read_bytes()


def record(name,value):
    data=(json.dumps(value,ensure_ascii=False,indent=2)+'\n').encode()
    with (PROOF/name).open('xb') as output:
        output.write(data);output.flush();os.fsync(output.fileno())
    fsync(PROOF)


def fsync(path):
    descriptor=os.open(path,os.O_RDONLY)
    try:os.fsync(descriptor)
    finally:os.close(descriptor)


def compare(path,expected):
    if digest(raw(path))!=expected:raise RuntimeError('Intervening evidence: '+str(path))


def no_processes():
    # A failed/unknown ps invocation raises; it never becomes an empty inventory.
    rows=supervisor.processes()
    coordinators=supervisor.coordinator_processes(rows)
    workers=supervisor.job_workers(rows)
    others=[x for x in rows if any(str(ROOT/name) in x['args'][1:3]
        for name in ['publish_snapshot.py','build_reader.py','build_downloads.py','build_compact_sites.py'])]
    assert not coordinators and not workers and not others
    return dict(observed_at_unix=time.time(),known_inventory=True,
                coordinators=coordinators,workers=workers,exporters=others)


with ExitStack() as stack:
    for relative in ['runtime/supervision/supervisor.lock',
                     'runtime/exhaustive/coordinator.lock','draft-writer.lock',
                     'runtime/exhaustive/manual-agent-slots.lock']:
        path=ROOT/relative
        assert path.exists() and not path.is_symlink()
        stream=stack.enter_context(path.open('r+'))
        fcntl.flock(stream,fcntl.LOCK_EX|fcntl.LOCK_NB)
    observed=no_processes()
    pause_path=ROOT/'runtime/supervision/disabled'
    pause=raw(pause_path);assert digest(pause)==PAUSE
    assert json.loads(pause)['owner']==OWNER
    compare(ROOT/'run_exhaustive.py',BASELINE)
    compare(PREP/'run_exhaustive.py',CANDIDATE)
    compare(PREP/'artifact-manifest.json','6a1f915e658a2ac86a34b0e82ee0c30ad3acbade505c7cabf567766450372640')
    manifest=json.loads(raw(PREP/'artifact-manifest.json'))
    for name,metadata in manifest['artifacts'].items():compare(PREP/name,metadata['sha256'])
    tests=json.loads(raw(PREP/'tests.json'))
    assert tests['tests_run']==105 and tests['success'] is True
    assert tests['failures']==tests['errors']==tests['model_invocations']==0
    assert tests['tested_runner_sha256']==CANDIDATE and tests['production_db_forbidden'] is True
    plan=settings(ROOT/'runtime/exhaustive')
    assert plan['capacity']==8 and plan['role_limits']==dict(new=6,review=2)
    assert json.loads(raw(ROOT/'runtime/exhaustive/manual-agent-slots.json'))==[]

    # The locks are held for actual reconciliation, never for an active-job wait.
    previous_argv=sys.argv
    try:
        sys.argv=[str(PROOF/'preflight.py'),str(PROOF/'locked-preflight.json')]
        runpy.run_path(str(PROOF/'preflight.py'),run_name='__guarded_readonly_preflight__')
        sys.argv=[str(PREP/'reconcile.py'),str(PROOF/'locked-disposition.json')]
        runpy.run_path(str(PREP/'reconcile.py'),run_name='__guarded_readonly_disposition__')
    finally:sys.argv=previous_argv
    fresh=json.loads(raw(PROOF/'locked-preflight.json'))
    disposition=json.loads(raw(PROOF/'locked-disposition.json'))
    assert disposition['current_first_pass_open']==795
    assert disposition['unsuccessful_new_absent']==696 and disposition['unattempted_new_absent']==96
    assert disposition['held_documentary_sources']==3
    for name,expected in fresh['pins'].items():compare(ROOT/name,expected)
    for name,expected in fresh['input_hashes'].items():compare(ROOT/name,expected)
    current=no_processes()
    assert raw(ROOT/'runtime/exhaustive/coordinator.pid')==b'3122'
    exit_receipt=json.loads(raw(ROOT/'runtime/exhaustive/coordinator-exit.json'))
    assert exit_receipt['pid']==3122 and exit_receipt['stop_requested'] is True
    assert type(exit_receipt['exit_code']) is int and exit_receipt['exit_code']==0 and exit_receipt['exit_type'] is None
    record('installation-intent.json',dict(prepared_at_unix=time.time(),owner=OWNER,
        file='run_exhaustive.py',baseline_sha256=BASELINE,candidate_sha256=CANDIDATE,
        old_process_exit=exit_receipt,os_inventory=current,pause_sha256=PAUSE,
        preflight_sha256=digest(raw(PROOF/'locked-preflight.json')),
        disposition_sha256=digest(raw(PROOF/'locked-disposition.json')),
        source_policy_guards_unchanged=True,not_a_review_phase_transfer=True))
    with (PROOF/'owned-pause-before.json').open('xb') as output:
        output.write(pause);output.flush();os.fsync(output.fileno())
    before=raw(ROOT/'run_exhaustive.py')
    with (PROOF/'runner-before.py').open('xb') as output:
        output.write(before);output.flush();os.fsync(output.fileno())
    target=ROOT/'run_exhaustive.py'
    with tempfile.NamedTemporaryFile(dir=ROOT,prefix='.run_exhaustive.repair-',delete=False) as output:
        temporary=Path(output.name);output.write(raw(PREP/'run_exhaustive.py'))
        output.flush();os.fsync(output.fileno())
    os.chmod(temporary,stat.S_IMODE(target.stat().st_mode))
    compare(target,BASELINE);compare(pause_path,PAUSE)
    os.replace(temporary,target);fsync(ROOT)
    compare(target,CANDIDATE)
    for name,expected in fresh['pins'].items():
        if name!='run_exhaustive.py':compare(ROOT/name,expected)
    record('installed.json',dict(installed_at_unix=time.time(),file='run_exhaustive.py',
        installed_sha256=CANDIDATE,previous_sha256=BASELINE,other_code_policy_catalogue_pins_unchanged=True,
        effective_limits_unchanged=dict(workers=7,role_limits=dict(new=6,review=1)),
        canonical_mutations=0,signals_sent=0,coordinators_launched=0))
    compare(pause_path,PAUSE)
    assert json.loads(raw(pause_path))['owner']==OWNER
    record('resumption-intent.json',dict(prepared_at_unix=time.time(),owner=OWNER,
        installed_sha256=CANDIDATE,pause_sha256=PAUSE,
        action='Remove only this owned pause; existing registered LaunchAgent performs one guarded continuation',
        no_direct_launch=True,no_signals=True))
    pause_path.unlink();fsync(pause_path.parent)
    record('pause-released.json',dict(released_at_unix=time.time(),owner=OWNER,
        only_owned_pause_removed=True,expect_existing_supervisor_to_resume=True))
print(json.dumps(dict(installed=True,only_file='run_exhaustive.py',installed_sha256=CANDIDATE,
                     owned_pause_released=True,no_launch_or_signal=True)))
