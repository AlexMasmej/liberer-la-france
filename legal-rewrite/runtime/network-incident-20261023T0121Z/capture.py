"""Bounded read-only incident receipt. No API calls, model or pipeline mutation."""
from pathlib import Path
import collections, datetime, hashlib, json, re, sqlite3, sys

HERE = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from ingest import source_notes
from worker_execution import verify_execution

def digest(data):
    return hashlib.sha256(data).hexdigest()

def write(name, value):
    p = OUT / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

inputs = []
def capture(relative, destination=None):
    path = HERE / relative
    raw = path.read_bytes()
    record = {'path': str(path), 'sha256': digest(raw), 'bytes': len(raw)}
    if destination:
        p = OUT / destination
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(raw)
        record['preserved_copy'] = str(p.relative_to(OUT))
    inputs.append(record)
    return raw

now = datetime.datetime.now(datetime.timezone.utc).isoformat()
run = json.loads(capture('runtime/exhaustive/coordinator-run.json', 'inputs/coordinator-run.json'))
pid = run['pid']
supervision = json.loads(capture('runtime/supervision/status.json', 'inputs/supervision-status.json'))
status = json.loads(capture('runtime/exhaustive/status.json', 'inputs/status.json'))
limit = json.loads(capture('runtime/exhaustive/worker-limit.json', 'inputs/worker-limit.json'))
for rel in ['runtime/exhaustive/admission-status.json', 'runtime/exhaustive/admission-deferred.json',
            'runtime/exhaustive/review-lanes-observation.json', 'runtime/global-reference-audit-latest.json']:
    capture(rel, 'inputs/' + Path(rel).name)
metrics = []
for line in capture('runtime/exhaustive/job-metrics.jsonl').splitlines():
    try:
        item = json.loads(line)
    except ValueError:
        continue
    if item.get('coordinator_pid') == pid:
        metrics.append(item)
write('cohort-metrics.json', metrics)
failed = json.loads(capture('runtime/exhaustive/failed-jobs.json', 'inputs/failed-jobs.json'))
resolutions = json.loads(capture('runtime/exhaustive/failed-job-resolutions.json', 'inputs/failed-job-resolutions.json'))
failmap = {v['job']: v for v in failed}
queue = json.loads(capture('runtime/exhaustive/mixed-queue.json'))
queued = collections.defaultdict(list)
for job in queue:
    for identity in job['source_ids']:
        queued[(identity, bool(job.get('review')))].append({'slug': job['slug'], 'index': job['index']})
prior = json.loads(capture('runtime/radical-review-20261019.json'))
reviews = {(a['code_id'], a['source_id']): a.get('review_status') for a in prior['prior_articles']}

def errors(path, preserved):
    raw = capture(str(path.relative_to(HERE)), preserved)
    text = raw.decode(errors='replace')
    lines = [line for line in text.splitlines() if line.startswith(('ERROR:', 'warning: Falling back'))
             or (re.match(r'^2026-\d\d-\d\dT', line) and ' ERROR ' in line)]
    return {'original': str(path), 'preserved_copy': preserved,
            'sha256': digest(raw), 'bytes': len(raw),
            'transport_lines': [line for line in lines if re.search(r'workspace routing discovery|error sending request|request timed out|Reconnecting', line, re.I)],
            'access_or_quota_lines': [line for line in lines if re.search(r'rate.limit|usage.limit|quota|unauthori[sz]ed|authentication|sign.in|insufficient|\b40[13]\b|\b429\b', line, re.I)],
            'native_execution': verify_execution(path.parent, stderr_path=path)}

workers = []
for worker in supervision.get('active_agents', []):
    path = Path(worker.get('execution', {}).get('source_log', ''))
    if not path.is_file():
        workers.append(worker | {'fresh_log_known': False})
        continue
    proof = errors(path, 'active-logs/' + worker['job'] + '/' + path.name)
    workers.append(worker | {'fresh_log_known': True, 'fresh_native_execution': proof['native_execution'], 'proof': proof})
write('active-workers.json', workers)

db = sqlite3.connect((HERE/'corpus.sqlite').resolve().as_uri() + '?mode=ro', uri=True, timeout=15)
try:
    db.execute('BEGIN')
    jobs = []
    for metric in metrics:
        if metric.get('outcome') != 'deferred':
            continue
        name = metric['job']
        folder = HERE/'runtime/exhaustive/jobs'/name
        sources = json.loads(capture(str((folder/'source.json').relative_to(HERE)), 'deferred/' + name + '/source.json'))
        attempts = [errors(p, 'deferred/' + name + '/' + p.name) for p in sorted(folder.glob('errors-*.log'))]
        dispositions = []
        for source in sources:
            key = (source['code_id'], source['source_id'])
            canonical = db.execute('SELECT source_sha256,content_xml,valid_from,valid_until FROM articles WHERE code_id=? AND id=?', key).fetchone()
            draft = db.execute('SELECT source_sha256,status,proposed_xml FROM drafts WHERE code_id=? AND source_id=?', key).fetchone()
            dispositions.append({'code_id': key[0], 'source_id': key[1], 'number': source['number'],
                'source_sha256_matches': bool(canonical and canonical[0] == source['source_sha256']),
                'source_xml_matches': bool(canonical and canonical[1] == source['source_xml']),
                'notes_match': source_notes(db, *key) == source.get('source_notes_xml', ''),
                'versions_match': bool(canonical and canonical[2:] == (source.get('valid_from'), source.get('valid_until'))),
                'draft_present': draft is not None,
                'draft_source_matches': bool(draft and draft[0] == source['source_sha256']),
                'prior_review_status': reviews.get(key),
                'persistent_startup_queue': queued.get((key[1], metric['kind'] == 'review'), []),
                'failed_job_counted_as_accepted': False})
        jobs.append({'job': name, 'kind': metric['kind'], 'metric': metric,
                     'recorded_failure': failmap.get(name),
                     'explicit_resolutions': [r for r in resolutions if r.get('job') == name],
                     'attempts': attempts, 'articles': dispositions})
finally:
    db.close()
write('deferred-disposition.json', {'captured_at_utc': now, 'coordinator_pid': pid, 'jobs': jobs})
new = [a for j in jobs if j['kind'] == 'new' for a in j['articles']]
old = [a for j in jobs if j['kind'] == 'review' for a in j['articles']]
accepted = [m for m in metrics if m.get('outcome') in {'accepted', 'reviewed'}]
last = max(accepted, key=lambda m: m['finished_at_unix'], default=None)
pointer = json.loads((HERE/'runtime/global-reference-audit-latest.json').read_text())
baseline = pointer['refresh_progress_observed_after_initial_scan']
delta = sum(status[k] - baseline[k] for k in baseline)
receipt = {'captured_at_utc': now, 'state': 'routing_recurrence_unresolved',
           'coordinator_pid': pid, 'configured_limits': limit, 'workers_observed': len(workers),
           'fresh_native_responses_verified': sum(w.get('fresh_native_execution', {}).get('verified') is True for w in workers),
           'deferred_jobs': len(jobs), 'new_deferred_jobs': sum(j['kind']=='new' for j in jobs),
           'review_deferred_jobs': sum(j['kind']=='review' for j in jobs),
           'new_failed_source_identities': len({(a['code_id'],a['source_id']) for a in new}),
           'new_failed_identities_still_absent': sum(not a['draft_present'] for a in new),
           'prior_failed_review_identities': len({(a['code_id'],a['source_id']) for a in old}),
           'prior_failed_reviews_still_pending': sum(a['prior_review_status']=='pending' for a in old),
           'all_failed_source_notes_version_guards_match': all(all(a[k] for k in ['source_sha256_matches','source_xml_matches','notes_match','versions_match']) for a in new+old),
           'all_failed_ids_retained_in_persistent_startup_queue': all(a['persistent_startup_queue'] for a in new+old),
           'persistent_queue_does_not_prove_live_readmission': True,
           'last_accepted_metric': last,
           'last_accepted_at_utc': datetime.datetime.fromtimestamp(last['finished_at_unix'],datetime.timezone.utc).isoformat() if last else None,
           'pending_first_pass': status['pending'], 'pending_prior_reviews': status['prior_drafts_awaiting_review'],
           'additional_treatments_since_current_audit': delta, 'new_snapshot_required_by_threshold': delta>=1000,
           'no_authenticated_probe_or_model_invocation': True, 'no_model_or_quota_reset': True,
           'no_pipeline_code_policy_slot_or_process_change': True,
           'root_cause_beyond_observed_native_routing_transport_failure_established': False,
           'completion_claimed': False}
write('check.json', receipt)
write('inputs-manifest.json', inputs)
manifest = [{'path': str(p.relative_to(OUT)), 'sha256': digest(p.read_bytes()), 'bytes': p.stat().st_size}
            for p in sorted(OUT.rglob('*')) if p.is_file() and p.name != 'artifact-manifest.json']
write('artifact-manifest.json', manifest)
print(json.dumps({k: receipt[k] for k in ['captured_at_utc','coordinator_pid','fresh_native_responses_verified','deferred_jobs','new_failed_identities_still_absent','prior_failed_reviews_still_pending','all_failed_source_notes_version_guards_match','last_accepted_at_utc','additional_treatments_since_current_audit']}, ensure_ascii=False))
