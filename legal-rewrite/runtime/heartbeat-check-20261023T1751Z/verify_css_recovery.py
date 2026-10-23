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

runtime = ROOT / 'runtime/exhaustive'
allmetrics = [json.loads(x) for x in (runtime/'job-metrics.jsonl').read_text().splitlines()]
w = json.loads((ROOT/'runtime/radical-review-20261019.json').read_text())
prior = {(x['code_id'],x['source_id']):x for x in w['prior_articles']}
oldfolder = runtime/'jobs/review-securite-sociale-LEGIARTI000037290433-00002'
oldkeys = {(x['code_id'],x['source_id']) for x in read(oldfolder/'source.json')}
proofs = []
recovered = set()
for wanted_job in ['review-securite-sociale-LEGIARTI000029956107-00015','review-securite-sociale-LEGIARTI000053282440-00016']:
    reviewed = [m for m in allmetrics if m.get('coordinator_pid')==78943 and m.get('job')==wanted_job and m.get('outcome')=='reviewed']
    assert len(reviewed)==1
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
    overlap = {(x['code_id'],x['source_id']) for x in checked} & oldkeys
    recovered.update(overlap)
    proofs.append(dict(metric=metric,execution=execution,rows=checked,original_failed_scope_overlap=len(overlap)))
assert recovered == oldkeys and len(recovered)==10
for path,digest in stable.items():
    assert sha(path.read_bytes())==digest,'Input changed: '+str(path)
current = json.loads((ROOT/'runtime/radical-review-20261019.json').read_text())
current_entries = {(x['code_id'],x['source_id']):x for x in current['prior_articles']}
assert all(current_entries[k]==prior[k] and prior[k]['review_status']=='completed' for k in recovered)
dump('original-css-review-recovery.json',dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),original_failed_job=oldfolder.name,original_failed_scope_articles=10,freshly_verified_jobs=proofs,current_completed_original_scope=10,canonical_mutations=0,answers_replayed=False,whole_corpus_second_pass_completion_claimed=False,input_hashes={str(k.relative_to(ROOT)):v for k,v in stable.items()}))
print(json.dumps(dict(original_failed_job=oldfolder.name,verified_fresh_review_jobs=len(proofs),verified_articles=sum(len(x['rows']) for x in proofs),original_scope_recovered=len(recovered))),flush=True)
