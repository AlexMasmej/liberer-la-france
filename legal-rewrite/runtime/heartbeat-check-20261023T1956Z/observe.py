"""Read-only operational and targeted acceptance evidence; never registers."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import hashlib, json, os, shlex, shutil, sqlite3, subprocess, sys
sys.dont_write_bytecode = True
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
sys.path.insert(0, str(ROOT))
from ingest import source_notes, source_evidence
from worker_execution import verify_execution

def sha(data):
    return hashlib.sha256(data if isinstance(data, bytes) else (data or '').encode()).hexdigest()

def dump(name, value):
    with (OUT / name).open('x') as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write('\n')

stable = {}
def read(path):
    path = Path(path)
    data = path.read_bytes()
    stable[path] = sha(data)
    return json.loads(data)

def values(row):
    return tuple(row.get(k, 'rewrite_draft' if k == 'status' else None)
                 for k in ('source_sha256','status','proposed_xml','reason','review_notes'))

def locate(directory, keys):
    expression = '|'.join(i for c, i in keys)
    result = subprocess.run(['rg', '-l', expression, str(directory), '--glob', '*.json'],
                            capture_output=True, text=True)
    if result.returncode not in (0, 1):
        raise RuntimeError(result.stderr)
    return [Path(x) for x in result.stdout.splitlines()]

now = datetime.now(timezone.utc).isoformat()
rawps = subprocess.run(['ps','-axo','pid=,ppid=,lstart=,command='],
                       capture_output=True, text=True, check=True).stdout
processes = []
for line in rawps.splitlines():
    parts = line.strip().split(None, 7)
    if len(parts) == 8:
        processes.append(dict(pid=int(parts[0]), ppid=int(parts[1]),
                              birth_local=' '.join(parts[2:7]), command=parts[7]))
coordinators = [x for x in processes if 'run_exhaustive.py' in x['command'] and
                x['command'].split()[0].endswith(('/Python','/python3','/python3.14'))]
assert len(coordinators) == 1 and coordinators[0]['pid'] == 78943
coordinators[0]['birth_utc'] = datetime.strptime(coordinators[0]['birth_local'], '%a %b %d %H:%M:%S %Y').replace(tzinfo=ZoneInfo('America/Los_Angeles')).astimezone(timezone.utc).isoformat()
workers = []
for process in processes:
    if process['ppid'] != 78943 or 'codex exec ' not in process['command']:
        continue
    args = shlex.split(process['command'])
    folder = Path(args[args.index('--output-schema') + 1]).parent
    receipt = read(folder / ('process-' + str(process['pid']) + '.json'))
    assert receipt['pid'] == process['pid']
    workers.append(dict(pid=process['pid'], ppid=process['ppid'], job=folder.name,
                        birth_local=process['birth_local'], execution=verify_execution(folder, stderr_path=receipt['stderr_log'])))
sessions = [x['execution']['session_id'] for x in workers if x['execution']['verified']]
assert len(sessions) == len(set(sessions))
launch = subprocess.run(['launchctl','print',f'gui/{os.getuid()}/com.libererfrance.exhaustive-rewrite'], capture_output=True, text=True)
assert launch.returncode == 0
runtime = ROOT / 'runtime/exhaustive'
metrics_bytes = (runtime / 'job-metrics.jsonl').read_bytes()
assert metrics_bytes.endswith(b'\n')
metrics = [json.loads(x) for x in metrics_bytes.splitlines()]
current = [x for x in metrics if x.get('coordinator_pid') == 78943]
reviewed = [x for x in current if x.get('outcome') == 'reviewed']
deferred = [x for x in current if x.get('outcome') != 'reviewed']
status = read(runtime / 'status.json')
control = read(runtime / 'worker-limit.json')
phase = read(runtime / 'continuation-phase.json')
assert control == {'workers':8, 'role_limits':{'new':6,'review':0}, 'review_tail_limit':8}
assert phase['coordinator_pid'] == 78943 and phase['phase'] == 'review_tail'
assert phase['effective_limits'] == {'workers':8, 'role_limits':{'new':0,'review':8}}
admission = read(runtime / 'admission-status.json')
worklist_path = ROOT / 'runtime/radical-review-20261019.json'
worklist_bytes = worklist_path.read_bytes()
worklist = json.loads(worklist_bytes)
prior = {(x['code_id'], x['source_id']):x for x in worklist['prior_articles']}
assert len(prior) == 30314
original = read(ROOT / 'runtime/heartbeat-check-20261023T1348Z/deferred-disposition.json')
original_pending = [x for x in original['rows'] if x['kind'] == 'review' and prior[(x['code_id'],x['source_id'])]['review_status'] == 'pending']
deferred_proofs = []
db = sqlite3.connect((ROOT / 'corpus.sqlite').as_uri() + '?mode=ro', uri=True)
db.execute('PRAGMA query_only=ON')
db.execute('BEGIN')
try:
    for metric in deferred:
        assert metric['outcome'] == 'deferred'
        folder = runtime / 'jobs' / metric['job']
        sources = read(folder / 'source.json')
        failure = read(folder / 'validation-failure.json')
        checked = []
        for source in sources:
            key = source['code_id'], source['source_id']
            assert db.execute('SELECT source_sha256,content_xml,valid_from,valid_until FROM articles WHERE code_id=? AND id=?', key).fetchone() == (source['source_sha256'],source['source_xml'],source['valid_from'],source['valid_until'])
            assert source_notes(db, *key) == source['source_notes_xml']
            assert db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?', key).fetchone() == values(source['previous_draft'])
            assert prior[key]['review_status'] == 'pending'
            checked.append(dict(code_id=key[0],source_id=key[1],source_sha256=source['source_sha256'],whole_source_NOTA_versions_and_five_unchanged_beforeimage_fields_match=True,review_status='pending'))
        files = {x.name:dict(bytes=x.stat().st_size,sha256=sha(x.read_bytes())) for x in folder.iterdir() if x.is_file()}
        deferred_proofs.append(dict(metric=metric,validation_failure=failure,rows=checked,original_files=files,answer_replayed=False,registration_performed=False))
finally:
    db.close()

# Verify one newly accepted review independently. Input hashes refuse a mixed
# observation if a concurrent valid writer changes any selected owner/registry.
metric = max(reviewed, key=lambda x:x['finished_at_unix'])
folder = runtime / 'jobs' / metric['job']
sources = read(folder / 'source.json')
answers = {(x['code_id'],x['source_id']):x for x in read(folder / 'answer.json')}
wanted = {(x['code_id'],x['source_id']) for x in sources}
assert wanted == set(answers) and len(sources) == metric['articles']
owners = {}
owner_paths = {}
for path in locate(ROOT / 'batches', wanted):
    if not (path.stem.isdigit() or path.stem.startswith('batch')):
        continue
    for row in read(path):
        key = row['code_id'], row['source_id']
        if key in wanted:
            assert key not in owners
            owners[key], owner_paths[key] = row, path
assert set(owners) == wanted
archives = {}
for path in locate(ROOT / 'revisions/radical-review', wanted):
    archive = read(path)
    assert path.stem == sha(json.dumps(archive, ensure_ascii=False, sort_keys=True))
    for row in archive:
        key = row['code_id'], row['source_id']
        if key in wanted and row['replacement'] == owners[key]:
            archives.setdefault(key, []).append((path, row))
registry = read(ROOT / 'registered-batches.json')
observed = read(folder / ('execution-observed-' + str(metric['attempts']) + '.json'))
execution = verify_execution(folder, stderr_path=observed['source_log'])
assert execution['verified'] and execution['session_id'] == metric['execution_session_id']
checked = []
db = sqlite3.connect((ROOT / 'corpus.sqlite').as_uri() + '?mode=ro', uri=True)
db.execute('PRAGMA query_only=ON')
db.execute('BEGIN')
try:
    for source in sources:
        key = source['code_id'], source['source_id']
        row = owners[key]
        assert db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?', key).fetchone() == values(row) == values(answers[key])
        assert db.execute('SELECT source_sha256,content_xml,valid_from,valid_until FROM articles WHERE code_id=? AND id=?', key).fetchone() == (source['source_sha256'],source['source_xml'],source['valid_from'],source['valid_until'])
        assert source_notes(db,*key) == source['source_notes_xml']
        assert db.execute('SELECT source_xml,valid_from,valid_until FROM draft_sources WHERE code_id=? AND source_id=?', key).fetchone() == (source_evidence(source['source_xml'],source['source_notes_xml']),source['valid_from'],source['valid_until'])
        assert registry['|'.join(key)] == dict(source_sha256=row['source_sha256'],proposed_sha256=sha(row['proposed_xml']))
        assert len(archives[key]) == 1
        path, archived = archives[key][0]
        assert values(archived) == values(source['previous_draft'])
        assert sha(archived['proposed_xml']) == source['previous_draft']['proposed_sha256'] == row['prior_proposal_sha256']
        assert prior[key]['review_status'] == 'completed'
        checked.append(dict(code_id=key[0],source_id=key[1],owner=str(owner_paths[key]),archive=str(path),whole_source_NOTA_versions_five_fields_registry_full_archive_and_completed_match=True))
finally:
    db.close()
for path, digest in stable.items():
    assert sha(path.read_bytes()) == digest, 'Input changed during read-only collection: ' + str(path)
deferred_keys = {(r['code_id'],r['source_id']) for d in deferred_proofs for r in d['rows']}
original_keys = {(r['code_id'],r['source_id']) for r in original_pending}
wal = ROOT / 'corpus.sqlite-wal'
report = dict(checked_at_utc=now,coordinators=coordinators,launchagent_registered=True,
    native_workers=workers,native_processes=len(workers),native_responding_distinct_sessions=len(sessions),
    limits=control,phase=phase,admission=admission,status=status,
    postlaunch_outcomes=dict(Counter(m['outcome'] for m in current)),postlaunch_reviewed_jobs=len(reviewed),
    postlaunch_reviewed_articles=sum(m['articles'] for m in reviewed),
    audit_additional_treatments_since_222551Z=2073+sum(m['articles'] for m in reviewed),
    metrics_prefix_sha256=sha(metrics_bytes),metrics_prefix_bytes=len(metrics_bytes),
    worklist_sha256=sha(worklist_bytes),completed=worklist['completed_second_pass'],pending=sum(r['review_status']=='pending' for r in prior.values()),
    original_nonaccepted_review_jobs_current_pending=sorted({r['job'] for r in original_pending}),original_nonaccepted_review_articles_current_pending=len(original_pending),
    current_tail_deferred_jobs=len(deferred_proofs),current_tail_deferred_articles=len(deferred_keys),unique_original_and_current_deferred_reviews_pending=len(original_keys|deferred_keys),
    deferred=deferred_proofs,verified_accepted_review=dict(metric=metric,execution=execution,rows=checked),
    free_bytes=shutil.disk_usage(ROOT).free,wal_exists=wal.exists(),wal_bytes=wal.stat().st_size if wal.exists() else 0,
    supervision_pause_exists=(ROOT/'runtime/supervision/disabled').exists(),
    mutations_to_code_policy_controls_canonical_data=0,signals_sent=0,processes_launched=0,
    input_hashes={str(k.relative_to(ROOT)):v for k,v in stable.items()},
    scope='Current operational and one accepted review verification; not a final whole-corpus legal qualification. Deferred answers preserved and never replayed.')
audit_pointer = read(ROOT / 'runtime/global-reference-audit-latest.json')
audit_folder = Path(audit_pointer['folder'])
baseline = read(audit_folder / 'pre-capture-progress.json')
basis = baseline['treatment_count_basis']
assert sha(metrics_bytes[:basis['metrics_prefix_bytes']]) == basis['metrics_prefix_sha256'], 'Audit baseline metrics prefix changed'
later = [json.loads(line) for line in metrics_bytes[basis['metrics_prefix_bytes']:].splitlines()]
assert all(x['finished_at_unix'] >= basis['last_reviewed_finished_at_unix'] for x in later)
additional = sum(x.get('articles', 0) for x in later if x.get('outcome') in ('accepted', 'reviewed'))
assert sha((audit_folder/'artifact-manifest.json').read_bytes()) == '5e97ad0862115a41ee9725e22fca4f93104e6aded55a75b201e85581c9b771e3'
assert audit_pointer['audit_id'] == '384c85d78606cdafab4c33a86b86533004b1ba9ee0a1006779014a07ce0351f6'
assert sha((ROOT/'run_exhaustive.py').read_bytes()) == '91e898776c7619b89461928010c02f8cd49141745473dcdefbdfd5f6f65c3e40'
assert sha((ROOT/'register_batches.py').read_bytes()) == '75287e3267fb8d182a7262cdb747ae90070e20d6bf92b698768684e03c39051f'
report.update(current_validated_audit=str(audit_folder),current_validated_audit_id=audit_pointer['audit_id'],audit_baseline_metrics_prefix_verified=True,audit_additional_treatments_since_current_validated_baseline=additional,new_audit_due=additional>=1000,new_snapshot_created=False)
dump('CONTROL.json', report)
print(json.dumps({k:v for k,v in report.items() if k in {'checked_at_utc','native_processes','native_responding_distinct_sessions','postlaunch_outcomes','postlaunch_reviewed_jobs','postlaunch_reviewed_articles','completed','pending','current_tail_deferred_jobs','current_tail_deferred_articles','unique_original_and_current_deferred_reviews_pending','free_bytes'}},ensure_ascii=False),flush=True)
