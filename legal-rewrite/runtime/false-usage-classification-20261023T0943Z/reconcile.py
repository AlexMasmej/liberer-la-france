"""Small read-only, current disposition; never a transfer activation proof."""
from pathlib import Path
import collections
import datetime
import hashlib
import json
import re
import shutil
import sqlite3
import sys
import time

PROOF = Path(__file__).resolve().parent
ROOT = PROOF.parents[1]
OUTPUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else PROOF/'current-reconciliation.json'
if OUTPUT.exists() or not OUTPUT.parent.resolve().is_relative_to(ROOT/'runtime'):
    raise RuntimeError('Use a fresh evidence file inside this project runtime')
sys.path.insert(0, str(ROOT))
from ingest import source_notes, source_evidence

stable = {}


def read(path):
    path = Path(path)
    if path.is_symlink() or not path.is_file():
        raise RuntimeError('Unknown regular evidence: '+str(path))
    data = path.read_bytes(); stable[path] = data
    return json.loads(data)


def sha(data):
    return hashlib.sha256(data).hexdigest()


runtime = ROOT/'runtime/exhaustive'
run = read(runtime/'coordinator-run.json')
assert run['pid'] == 3122
metrics_data = (runtime/'job-metrics.jsonl').read_bytes()
assert metrics_data.endswith(b'\n')
metrics = [json.loads(x) for x in metrics_data.splitlines()]
metrics = [x for x in metrics if x['coordinator_pid'] == 3122]
names = [x['job'] for x in metrics]
assert len(names) == len(set(names))
admission = read(runtime/'admission-deferred.json')
assert admission['coordinator_pid'] == 3122
held = read(runtime/'held-graphic-sources.json')
resolution = read(runtime/'failed-job-resolutions.json')
reviews = read(ROOT/'runtime/radical-review-20261019.json')
pending_reviews = {(x['code_id'], x['source_id']) for x in reviews['prior_articles']
                   if x['review_status'] == 'pending'}
ledger_path = ROOT/'runtime/completion-coverage-inventory-20261023T0254Z/current-article-ledger.jsonl'
ledger_data = ledger_path.read_bytes()
ledger = [json.loads(x) for x in ledger_data.splitlines()]
assert len(ledger) == 30317
canonical = {(x['code_id'], x['source_id']): x for x in ledger}
assert len(canonical) == 30317
db = sqlite3.connect('file:'+str(ROOT/'corpus.sqlite')+'?mode=ro', uri=True)
db.execute('BEGIN')
drafts = {(c, i): (s, status, body) for c, i, s, status, body in db.execute(
    'SELECT code_id,source_id,source_sha256,status,proposed_xml FROM drafts')}
missing = {k for k, x in canonical.items() if k not in drafts or
           drafts[k][0] != x['source_sha256'] or
           not (drafts[k][2] or drafts[k][1] == 'retained_unchanged')}
rows = []; jobs = []; unsuccessful_new = set(); stopped_reviews = set()
for metric in metrics:
    if metric['outcome'] in {'accepted', 'reviewed', 'skipped_existing', 'skipped'}:
        continue
    folder = runtime/'jobs'/metric['job']
    sources = read(folder/'source.json')
    assert len(sources) == metric['articles']
    jobs.append({k: metric[k] for k in ['job', 'kind', 'outcome', 'attempts']})
    for source in sources:
        key = source['code_id'], source['source_id']
        assert key in canonical
        actual = db.execute('SELECT source_sha256,content_xml,valid_from,valid_until '
                            'FROM articles WHERE code_id=? AND id=?', key).fetchone()
        assert actual == (source['source_sha256'], source['source_xml'],
                          source['valid_from'], source['valid_until']), key
        assert source_notes(db, *key) == source['source_notes_xml'], key
        assert canonical[key]['source_sha256'] == source['source_sha256'], key
        is_new = metric['kind'] == 'new'
        if is_new and key in missing: unsuccessful_new.add(key)
        if not is_new and key in pending_reviews: stopped_reviews.add(key)
        rows.append(dict(job=metric['job'], kind=metric['kind'],
                         outcome=metric['outcome'], code_id=key[0], source_id=key[1],
                         whole_sources_notes_versions_match=True,
                         first_pass_absent=key in missing,
                         prior_review_pending=key in pending_reviews))
unattempted = set()
unattempted_jobs = []
for job in admission['jobs']:
    assert job['attempted'] is False and job['accepted'] is False
    if job['kind'] != 'new': continue
    ids = job['source_ids']; assert len(ids) == len(set(ids))
    keys = {k for k, x in canonical.items()
            if x['slug'] == job['slug'] and k[1] in ids}
    assert len(keys) == len(ids)
    for key in keys:
        actual = db.execute('SELECT source_sha256 FROM articles WHERE code_id=? AND id=?', key).fetchone()
        assert actual and actual[0] == canonical[key]['source_sha256']
        assert key in missing
    unattempted.update(keys)
    unattempted_jobs.append(dict(slug=job['slug'], index=job['index'], articles=len(keys)))
held_keys = {k for x in held for k, entry in canonical.items()
             if entry['slug'] == x['slug'] and k[1] == x['source_id']}
assert len(held_keys) == len(held)
assert held_keys <= missing
assert not unsuccessful_new & unattempted
assert not (unsuccessful_new | unattempted) & held_keys
assert missing == unsuccessful_new | unattempted | held_keys, 'Unclassified first-pass identities'

# The single naturally finishing new job was accepted under the existing code.
folder = runtime/'jobs/travail-00474'
answer = read(folder/'answer.json'); sources = read(folder/'source.json')
complete = read(folder/'registration-complete.json')
intent = read(folder/'registration-intent.json')
batch = read(Path(complete['batch_path']))
registry = read(ROOT/'registered-batches.json')
source_map = {(x['code_id'], x['source_id']): x for x in sources}
answer_map = {(x['code_id'], x['source_id']): x for x in answer}
assert len(answer) == len(batch) == len(source_map) == complete['accepted_articles'] == 24
assert len(answer_map) == 24
assert batch == intent['rows']
for row in batch:
    key = row['code_id'], row['source_id']; source = source_map[key]
    actual_source = db.execute('SELECT source_sha256,content_xml,valid_from,valid_until '
                              'FROM articles WHERE code_id=? AND id=?', key).fetchone()
    assert actual_source == (source['source_sha256'], source['source_xml'],
                             source['valid_from'], source['valid_until'])
    assert source_notes(db, *key) == source['source_notes_xml']
    assert canonical[key]['source_sha256'] == source['source_sha256']
    original_answer = answer_map[key]
    for field in ['source_sha256','proposed_xml','reason','review_notes']:
        assert original_answer.get(field) == row.get(field), (key, field)
    assert original_answer.get('status','rewrite_draft') == row.get('status','rewrite_draft')
    actual = db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes '
                        'FROM drafts WHERE code_id=? AND source_id=?', key).fetchone()
    assert actual == (row['source_sha256'], row.get('status', 'rewrite_draft'),
                      row['proposed_xml'], row['reason'], row['review_notes'])
    evidence = db.execute('SELECT source_xml,valid_from,valid_until FROM draft_sources '
                          'WHERE code_id=? AND source_id=?', key).fetchone()
    assert evidence == (source_evidence(source['source_xml'], source['source_notes_xml']),
                        source['valid_from'], source['valid_until'])
    assert registry['|'.join(key)] == dict(
        source_sha256=row['source_sha256'], proposed_sha256=sha((row['proposed_xml'] or '').encode()))
db.rollback(); db.close()
for path, data in stable.items():
    assert path.read_bytes() == data, 'Evidence changed: '+str(path)
assert (runtime/'job-metrics.jsonl').read_bytes() == metrics_data
log = runtime/'jobs/travail-00472/errors-3.log'
raw = log.read_bytes(); text = raw.decode()
old_tail = text[-4000:]
matches = [m.group() for m in re.finditer(
    r'rate.limit|usage.limit|quota|unauthori[sz]ed|authentication|sign.in|insufficient', old_tail, re.I)]
assert matches and set(x.lower() for x in matches) == {'quota'}
report = dict(
    checked_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    coordinator_pid=3122, current_first_pass_covered=30317-len(missing),
    current_first_pass_open=len(missing),
    unsuccessful_jobs=len(jobs), unsuccessful_by_outcome=dict(collections.Counter(x['outcome'] for x in jobs)),
    unsuccessful_new_absent=len(unsuccessful_new), prior_review_pending=len(stopped_reviews),
    unattempted_new_absent=len(unattempted), unattempted_new_jobs=unattempted_jobs,
    held_documentary_sources=len(held_keys), all_missing_first_pass_ids_accounted=True,
    old_review_completed=reviews['completed_second_pass'], old_review_pending=len(pending_reviews),
    naturally_finished_474_accepted=24, accepted_db_batch_registry_intent_source_evidence_equal=True,
    classification_trigger=dict(job='travail-00472', original_log_bytes=len(raw), original_log_sha256=sha(raw),
                                old_detector_matches=matches, terminal_error='workspace routing discovery timed out',
                                actual_authentication_or_usage_denial_established=False),
    unresolved_failed_registry_resolutions_read=len(resolution),
    source_records_checked=len(rows), rows=rows, jobs=jobs,
    guarded_input_hashes={str(p.relative_to(ROOT)): sha(data) for p, data in stable.items()},
    metrics_sha256=sha(metrics_data), canonical_ledger_sha256=sha(ledger_data),
    free_gib=shutil.disk_usage(ROOT).free/2**30,
    wal_bytes=(ROOT/'corpus.sqlite-wal').stat().st_size if (ROOT/'corpus.sqlite-wal').exists() else None,
    no_snapshot_no_canonical_mutation=True, no_general_transport_recovery_certified=True,
    not_a_full_registration_or_legal_transfer_certificate=True)
with OUTPUT.open('x') as stream:
    stream.write(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['rows','jobs','guarded_input_hashes']},ensure_ascii=False))
