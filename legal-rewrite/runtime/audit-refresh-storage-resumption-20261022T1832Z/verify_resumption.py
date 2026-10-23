"""Read-only recovery evidence; never registers work or launches a process."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import hashlib, json, shutil, sqlite3, sys

OUT = Path(__file__).resolve().parent
HERE = OUT.parents[1]
RUNTIME = HERE / 'runtime/exhaustive'
sys.path.insert(0, str(HERE))
sys.dont_write_bytecode = True
import supervise_exhaustive as supervision
from ingest import source_notes

def read(path):
    return json.loads(path.read_text())

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write(name, value):
    path = OUT / name
    tmp = path.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    tmp.replace(path)

def main():
    run = read(RUNTIME / 'coordinator-run.json')
    pid = run['pid']
    processes = supervision.processes()
    coordinators = supervision.coordinator_processes(processes)
    assert [x['pid'] for x in coordinators] == [pid]
    assert run['requested_execution'] == {'model':'gpt-6-astra','reasoning_effort':'medium'}
    assert sha(HERE / 'register_batches.py') == '75287e3267fb8d182a7262cdb747ae90070e20d6bf92b698768684e03c39051f'
    limits = read(RUNTIME / 'worker-limit.json')
    assert limits == {'workers':7,'role_limits':{'new':6,'review':1}}
    admission = read(RUNTIME / 'queue-admission-plan.json')
    assert admission['coordinator_pid'] == pid
    assert (RUNTIME / 'queue.json').stat().st_mtime >= run['started_at_unix']
    workers = supervision.job_workers(processes)
    assert all(x['ppid'] == pid for x in workers)
    responding = [x for x in workers if x.get('execution',{}).get('verified')]
    sessions = {x['execution']['session_id'] for x in responding}
    assert len(sessions) == len(responding)
    kinds = Counter(x['kind'] for x in responding)
    native_proof = OUT / 'seven-native-response-proof.json'
    if kinds == {'new':6,'review':1}:
        write(native_proof.name, {'at_utc':datetime.now(timezone.utc).isoformat(),
              'coordinator_pid':pid,'workers':workers,'all_seven_distinct_responses_verified':True})
    native_verified = native_proof.exists() and read(native_proof)['coordinator_pid'] == pid
    metrics = [json.loads(line) for line in (RUNTIME/'job-metrics.jsonl').read_text().splitlines() if line.strip()]
    cohort = [x for x in metrics if x.get('coordinator_pid') == pid]
    accepted = [x for x in cohort if x['outcome'] in {'accepted','reviewed'}]
    assert all(x.get('execution_verified') and x.get('model') == 'gpt-6-astra'
               and x.get('reasoning_effort') == 'medium' for x in accepted)
    queued = {identifier for item in read(RUNTIME/'queue.json') for identifier in item['source_ids']}
    dispositions = []
    db = sqlite3.connect((HERE/'corpus.sqlite').as_uri()+'?mode=ro', uri=True, timeout=5)
    db.execute('PRAGMA query_only=ON')
    db.execute('BEGIN')
    try:
        for name in ['travail-00344','travail-00345','travail-00349']:
            folder = RUNTIME/'jobs'/name
            for article in read(folder/'source.json'):
                key = (article['code_id'],article['source_id'])
                source = db.execute('SELECT source_sha256,content_xml,valid_from,valid_until,state,archive FROM articles WHERE code_id=? AND id=?', key).fetchone()
                assert source and source[0] == article['source_sha256'] and source[1] == article['source_xml']
                assert source_notes(db,*key) == article.get('source_notes_xml','')
                assert list(source[2:]) == [article[k] for k in ['valid_from','valid_until','source_state','source_archive']]
                draft = db.execute('SELECT source_sha256,status,proposed_xml FROM drafts WHERE code_id=? AND source_id=?',key).fetchone()
                present = bool(draft and draft[0] == article['source_sha256'] and (draft[2] or draft[1] == 'retained_unchanged'))
                state = 'present_guarded' if present else 'requeued' if article['source_id'] in queued else 'unaccounted'
                assert state != 'unaccounted', key
                dispositions.append({'old_job':name,'key':list(key),'state':state,'source_body_notes_version_archive_guards_match':True})
        for item in accepted:
            if item['kind'] != 'new':
                continue
            folder = RUNTIME/'jobs'/item['job']
            completion = read(folder/'registration-complete.json')
            intent = read(folder/'registration-intent.json')
            assert completion['accepted_articles'] == item['articles']
            assert sha(folder/'source.json') == intent['source_sha256']
            assert sha(folder/'reference-targets.json') == intent['reference_sha256']
            assert read(Path(completion['batch_path'])) == intent['rows']
            for row in intent['rows']:
                current = db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?',(row['code_id'],row['source_id'])).fetchone()
                assert current and current[0] == row['source_sha256']
                assert current[1] == row.get('status','rewrite_draft')
                assert tuple(current[2:]) == (row['proposed_xml'],row['reason'],row['review_notes'])
    finally:
        db.close()
    new_accepted = [x for x in accepted if x['kind'] == 'new' and x['articles'] > 0]
    report = {'at_utc':datetime.now(timezone.utc).isoformat(),'coordinator_pid':pid,
              'single_coordinator_verified':True,'optimizer_hash_verified':True,'effective_limits':limits,
              'native_seven_response_proof':str(native_proof) if native_verified else None,
              'current_responding_by_kind':dict(kinds),'accepted_jobs':accepted,
              'accepted_articles_by_kind':{kind:sum(x.get('articles',0) for x in accepted if x['kind']==kind) for kind in ['new','review']},
              'interrupted72':dispositions,'disposition_counts':dict(Counter(x['state'] for x in dispositions)),
              'sqlite_quick_check_evidence':str(OUT/'live-db-quick-check.json'),
              'free_bytes':shutil.disk_usage(HERE).free,'state':'resumption_verified' if native_verified and new_accepted else 'awaiting_accepted_new_articles',
              'performance_gain_measured':False,'legal_completion_claimed':False,'live_or_canonical_data_modified':False}
    write('resumption-verification.json',report)
    print(json.dumps({k:report[k] for k in ['state','coordinator_pid','current_responding_by_kind','accepted_articles_by_kind','disposition_counts','free_bytes']}))

if __name__ == '__main__':
    main()
