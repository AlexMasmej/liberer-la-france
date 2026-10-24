"""Read-only native retry evidence; output is confined to this new capsule."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, sys
sys.dont_write_bytecode = True
OUT = Path(__file__).resolve().parent
R = OUT.parent
ROOT = R.parent

def sha(b): return hashlib.sha256(b).hexdigest()
def read(p): return json.loads(p.read_bytes())
def put(name, value):
    with (OUT / name).open('x') as f:
        json.dump(value, f, ensure_ascii=False, indent=2)
        f.write('\n')
def verify(folder, name, expected):
    b = (folder / name).read_bytes()
    if sha(b) != expected: raise ValueError('Manifest differs: ' + str(folder))
    for n, item in json.loads(b)['files'].items():
        b = (folder / n).read_bytes()
        if len(b) != item['bytes'] or sha(b) != item['sha256']:
            raise ValueError('Evidence differs: ' + n)

PREP = R / 'coherence-resumption-acceptance-20261024T0010Z'
verify(PREP, 'preparation-manifest.json', 'b62bb8b6e2e0d4a0ef27b3d43d45b9ea02dfa0f72863e125928e8eb328d17040')
WAVE = R / 'coherence-current-policy-response-confirmation-20261024T0004Z'
verify(WAVE, 'artifact-manifest.json', '7d74d53f8295a51bbc9d36fbb554a852e2ce55a1f4f496dc16e4b46be0f40266')
sys.path.insert(0, str(PREP))
from observe_v2 import observe
from worker_execution import verify_execution
import supervise_exhaustive as supervisor

observation = observe(False)
put('native-and-process.json', observation)
rows = supervisor.processes()
live = supervisor.coordinator_processes(rows)
if len(live) != 1 or live[0]['pid'] != 58195:
    raise ValueError('Coordinator changed during collection')
workers = [x for x in supervisor.job_workers(rows) if x['ppid'] == 58195]
put('actual-workers.json', dict(at_utc=datetime.now(timezone.utc).isoformat(), workers=workers))
wave = read(WAVE / 'eight-native-responses.json')
names = {x['job'] for x in wave['responders']}
if {x['job'] for x in workers} != names:
    raise ValueError('First wave changed: qualify actual job history separately')
reports = []
for name in sorted(names):
    folder = R / 'exhaustive/jobs' / name
    target = OUT / 'captured' / name
    target.mkdir(parents=True)
    records = []
    captured = []
    for p in sorted(folder.glob('process-*.json')):
        b = p.read_bytes()
        (target / p.name).write_bytes(b)
        records.append(json.loads(b))
    current = next(x for x in workers if x['job'] == name)
    current_record = next(x for x in records if x['pid'] == current['pid'])
    if 'ended_at_unix' in current_record:
        raise ValueError('Current native already ended: refresh inventory')
    for p in sorted(folder.glob('errors-*.log')):
        b = p.read_bytes()
        text = b.decode(errors='replace')
        (target / p.name).write_bytes(b)
        # Appending is allowed; replacement of the captured prefix is not.
        if p.read_bytes()[:len(b)] != b:
            raise ValueError('Native log prefix changed')
        evidence = verify_execution(folder, stderr_path=p)
        rec = next(x for x in records if x['stderr_log'] == str(p))
        diagnostics = [line for line in text.splitlines()
                       if line.startswith('ERROR:') or re.match(r'^\d{4}-\d\d-\d\dT.* ERROR codex_', line)]
        captured.append(dict(original_path=str(p), captured=str((target/p.name).relative_to(OUT)),
            bytes=len(b), sha256=sha(b), process=rec,
            execution=evidence, native_diagnostics=diagnostics,
            pipeline_retry_timeout_message='Le précédent contrôle a échoué : Agent timed out; no article accepted' in text,
            pipeline_retry_invocation_message='Le précédent contrôle a échoué : Agent invocation failed; inspect local job logs' in text,
            routing_discovery_timeout='ERROR: workspace routing discovery timed out' in text,
            model_manager_timeout='failed to refresh available models: request timed out' in text,
            system_skills_directory_error='failed to install system skills:' in text,
            certificate_unknown_issuer='invalid peer certificate: UnknownIssuer' in text))
    for n in ['source.json','policy.json','coordination.json','reference-targets.json']:
        p=folder/n; b=p.read_bytes(); (target/n).write_bytes(b)
    artifacts = [dict(name=p.name, bytes=p.stat().st_size) for p in folder.iterdir()
                 if p.is_file() and p.name.startswith(('answer','previous-answer','result.'))]
    reports.append(dict(job=name, current_native_pid=current['pid'],
        current_execution=current['execution'], logs=captured, artifacts=artifacts,
        current_frozen_policies_match=read(folder/'policy.json') == read(ROOT/'site-summaries.json')
            and read(folder/'coordination.json') == read(ROOT/'policy-coordinations.json')))

metrics = [json.loads(x) for x in (R/'exhaustive/job-metrics.jsonl').read_bytes().splitlines()]
current_metrics = [x for x in metrics if x.get('coordinator_pid') == 58195]
if any(x['outcome'] in {'accepted','reviewed'} for x in current_metrics):
    raise ValueError('Run complete accepted verification now')
put('native-retry-diagnostic.json', dict(at_utc=datetime.now(timezone.utc).isoformat(), jobs=reports,
    current_native_processes=len(workers), current_verified_model_responses=sum(x['execution']['verified'] for x in workers),
    current_header_sessions=sum(bool(x['execution'].get('session_id')) for x in workers),
    current_no_header=sum(not bool(x['execution'].get('header_sha256')) for x in workers),
    first_wave_actual_responses_remain_historical=True,
    first_wave_final_process_records=[log['process'] for x in reports for log in x['logs'] if log['process'].get('ended_at_unix')],
    current_coordinator_metrics=current_metrics,
    no_401_403_429_or_auth_usage_cause_claimed=True,
    no_general_network_disk_quota_or_deadlock_cause_established=True,
    no_manual_signal_retry_reset_pause_launch_or_policy_change=True,
    native_retries_are_existing_pipeline_attempts_not_supervisor_relaunches=True))
put('pipeline-bounded-retry-code-evidence.json', dict(runner_sha256=sha((ROOT/'run_exhaustive.py').read_bytes()),
    attempt_bound=3, per_attempt_timeout_seconds=3600,
    note='The pinned runner contains invoke_agent group cleanup on timeout and ordinary bounded retries. Six first-attempt receipts ended with returncode -15 and two with returncode 1. Available retry inputs distinguish timeout from invocation failure; this control sent no signal.',
    exact_two_coordinator_launches=[41583,58195],
    no_bounded_retry_count_or_native_access_detector_change=True))
print(json.dumps(dict(at_utc=datetime.now(timezone.utc).isoformat(), native=len(workers),
    actual_current_responses=sum(x['execution']['verified'] for x in workers),
    current_metrics=current_metrics),ensure_ascii=False))
