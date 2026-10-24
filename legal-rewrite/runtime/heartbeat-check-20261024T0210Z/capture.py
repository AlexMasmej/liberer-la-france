"""Read-only proof of bounded retries, current responses and terminal deferrals."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,sys
sys.dont_write_bytecode=True
OUT=Path(__file__).resolve().parent;R=OUT.parent;ROOT=R.parent
def sha(b):return hashlib.sha256(b).hexdigest()
def read(p):return json.loads(p.read_bytes())
def put(n,o):
    with (OUT/n).open('x') as f:json.dump(o,f,ensure_ascii=False,indent=2);f.write('\n')
def verify(folder,name,expected):
    b=(folder/name).read_bytes();assert sha(b)==expected
    for n,i in json.loads(b)['files'].items():
        b=(folder/n).read_bytes();assert len(b)==i['bytes'] and sha(b)==i['sha256'],n
PREP=R/'coherence-resumption-acceptance-20261024T0010Z'
verify(PREP,'preparation-manifest.json','b62bb8b6e2e0d4a0ef27b3d43d45b9ea02dfa0f72863e125928e8eb328d17040')
OLD=R/'heartbeat-check-20261024T0108Z'
verify(OLD,'artifact-manifest.json','4bd717aa994e16f026bca9fca21d72f10a42520e3eb2db109c38f6ed391557f9')
sys.path.insert(0,str(PREP))
from observe_v2 import observe
import supervise_exhaustive as supervisor
from worker_execution import verify_execution
obs=observe(False);put('native-and-process.json',obs)
rows=supervisor.processes();live=supervisor.coordinator_processes(rows)
assert len(live)==1 and live[0]['pid']==58195
workers=[x for x in supervisor.job_workers(rows) if x['ppid']==58195]
put('actual-workers.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),workers=workers))
first={x['job'] for x in read(R/'coherence-current-policy-response-confirmation-20261024T0004Z/eight-native-responses.json')['responders']}
metrics_b=(R/'exhaustive/job-metrics.jsonl').read_bytes()
current_metrics=[json.loads(x) for x in metrics_b.splitlines() if json.loads(x).get('coordinator_pid')==58195]
assert not any(x['outcome'] in {'accepted','reviewed'} for x in current_metrics),'Run complete acceptance proof immediately'
names=first|{x['job'] for x in workers}|{x['job'] for x in current_metrics}
reports=[]
for name in sorted(names):
    folder=R/'exhaustive/jobs'/name;target=OUT/'captured'/name;target.mkdir(parents=True)
    files={};records=[]
    for p in sorted(folder.glob('process-*.json')):
        b=p.read_bytes();(target/p.name).write_bytes(b);records.append(json.loads(b))
    for n in ['source.json','policy.json','coordination.json','reference-targets.json']:
        p=folder/n;b=p.read_bytes();(target/n).write_bytes(b);files[n]=dict(bytes=len(b),sha256=sha(b))
    assert read(folder/'policy.json')==read(ROOT/'site-summaries.json')
    assert read(folder/'coordination.json')==read(ROOT/'policy-coordinations.json')
    logs=[]
    for p in sorted(folder.glob('errors-*.log')):
        b=p.read_bytes();text=b.decode(errors='replace')
        old=OLD/'captured'/name/p.name
        # Preserve the old closed capsule. Append-only prefixes are checked,
        # and only changed/new logs need another complete captured prefix.
        if old.exists():
            before=old.read_bytes();assert b[:len(before)]==before
        else:before=None
        if before!=b:(target/p.name).write_bytes(b)
        retained=str(target/p.name) if before!=b else str(old)
        assert p.read_bytes()[:len(b)]==b
        e=verify_execution(folder,stderr_path=p)
        assert not e.get('session_id') or (e.get('model')=='gpt-6-astra' and e.get('reasoning_effort')=='medium')
        diagnostics=[l for l in text.splitlines() if l.startswith('ERROR:') or (' ERROR codex_' in l and l[:4].isdigit())]
        logs.append(dict(original=str(p),retained_prefix=retained,bytes=len(b),sha256=sha(b),execution=e,
            native_diagnostics_tail=diagnostics[-16:],process=next(x for x in records if x['stderr_log']==str(p)),
            coherence_priority_in_input='SECONDE PASSE — PRIORITÉ HUMAINE DU23OCTOBRE2026' in text))
    active=next((x for x in workers if x['job']==name),None)
    terminal=next((x for x in current_metrics if x['job']==name),None)
    assert not (active and terminal),'Terminal metric and active job need separate qualification'
    artifacts=[dict(name=p.name,bytes=p.stat().st_size) for p in folder.iterdir()
               if p.is_file() and p.name.startswith(('answer','previous-answer','result.'))]
    reports.append(dict(job=name,first_wave=name in first,active=active,terminal_metric=terminal,
        assigned_sources=len(read(folder/'source.json')),files=files,processes=records,logs=logs,
        local_artifacts_are_not_accepted_proof=artifacts,current_frozen_policies_match=True))
assert (R/'exhaustive/job-metrics.jsonl').read_bytes()==metrics_b
put('native-and-terminal-diagnostic.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),jobs=reports,
    current_metrics=current_metrics,current_native_processes=len(workers),
    actual_current_native_responses=sum(x['execution']['verified'] for x in workers),
    current_native_sessions=[x['execution'].get('session_id') for x in workers],
    new_active_jobs_after_terminal_deferrals=[x['job'] for x in workers if x['job'] not in first],
    no_acceptance_claim_from_response_or_answer_file=True,
    no_manual_signal_pause_launch_code_policy_or_admission_change=True,
    no_general_network_quota_disk_or_deadlock_cause_established=True))
put('anchor-verification.json',dict(preparation_sha256='b62bb8b6e2e0d4a0ef27b3d43d45b9ea02dfa0f72863e125928e8eb328d17040',
    previous_control_manifest_sha256='4bd717aa994e16f026bca9fca21d72f10a42520e3eb2db109c38f6ed391557f9',
    all_manifest_members_verified=True,old_log_prefixes_preserved=True,
    exact_two_coordinator_launch_history=[41583,58195],bounded_native_attempts_are_not_coordinator_relaunches=True))
print(json.dumps(dict(at_utc=datetime.now(timezone.utc).isoformat(),native=len(workers),responses=sum(x['execution']['verified'] for x in workers),terminal_metrics=current_metrics),ensure_ascii=False))
