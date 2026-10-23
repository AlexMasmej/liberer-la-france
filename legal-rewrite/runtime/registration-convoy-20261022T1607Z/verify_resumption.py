"""Read-only operational checks, never accepts a draft or declares legal completion."""
from pathlib import Path
import datetime,hashlib,json,sqlite3,sys
FOLDER=Path(__file__).resolve().parent
HERE=FOLDER.parents[1]
sys.path.insert(0,str(HERE))
import supervise_exhaustive as supervision
from ingest import source_notes

def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def atomic(p,value):
    q=p.with_name('.'+p.name+'.verification.tmp')
    q.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n');q.replace(p)

def main():
    activation=read(FOLDER/'activation-state.json')
    if activation['state']!='new_coordinator_launched':
        print(json.dumps({'handover_state':activation['state'],'installed':False}));return
    pid=activation['pid'];runtime=HERE/'runtime/exhaustive'
    requested=read(FOLDER/'checks.json')['implementation_sha256']
    assert requested=={'register_batches.py':'75287e3267fb8d182a7262cdb747ae90070e20d6bf92b698768684e03c39051f'}
    assert all(sha(HERE/name)==value for name,value in requested.items())
    rows=supervision.processes();live=supervision.coordinator_processes(rows)
    assert [p['pid'] for p in live]==[pid], 'Single new coordinator not established'
    run=read(runtime/'coordinator-run.json');assert run['pid']==pid
    assert run['requested_execution']=={'model':'gpt-6-astra','reasoning_effort':'medium'}
    admission_path=runtime/'queue-admission-plan.json'
    admission=read(admission_path) if admission_path.exists() else {}
    if admission.get('coordinator_pid')!=pid or (runtime/'queue.json').stat().st_mtime<run['started_at_unix']:
        print(json.dumps({'pid':pid,'installed':True,'single_coordinator':True,'state':'startup_validation_queue_not_rebuilt_yet'}));return
    limits=read(runtime/'worker-limit.json')
    assert limits=={'workers':7,'role_limits':{'new':6,'review':1}}
    old_exit=read(FOLDER/'before/drained-exit.json')
    assert old_exit['pid']==75807 and old_exit['exit_code']==0 and old_exit['stop_requested']
    workers=supervision.job_workers(rows)
    assert all(w['ppid']==pid for w in workers)
    keys={w['execution'].get('session_id') for w in workers if w['execution'].get('verified')}
    assert len(keys)==sum(w['execution'].get('verified',False) for w in workers)
    metrics=[json.loads(line) for line in (runtime/'job-metrics.jsonl').read_text().splitlines()]
    cohort=[x for x in metrics if x['coordinator_pid']==pid]
    accepted=[x for x in cohort if x['outcome'] in {'accepted','reviewed'}]
    assert all(x.get('execution_verified') and x.get('model')=='gpt-6-astra' and x.get('reasoning_effort')=='medium' for x in accepted)
    pending_new={i for x in read(runtime/'queue.json') for i in x['source_ids']}
    pending_reviews={i for x in read(runtime/'mixed-queue.json') if x['review'] for i in x['source_ids']}
    review=read(HERE/'runtime/radical-review-20261019.json')
    reviewed={(x['code_id'],x['source_id']) for x in review['prior_articles'] if x['review_status']=='completed'}
    drift={(x['code_id'],x['source_id']) for x in review.get('changed_since_inventory',[])}
    original=read(FOLDER/'network-resumption-and-inflight.json');dispositions=[];errors=[]
    db=sqlite3.connect((HERE/'corpus.sqlite').as_uri()+'?mode=ro',uri=True,timeout=10)
    db.execute('BEGIN')
    try:
        for job in original['jobs']:
            folder=runtime/'jobs'/job['job'];assert sha(folder/'source.json')==job['source_file_sha256']
            for article in read(folder/'source.json'):
                key=(article['code_id'],article['source_id'])
                src=db.execute('SELECT source_sha256,content_xml FROM articles WHERE code_id=? AND id=?',key).fetchone()
                guards=(bool(src) and src[0]==article['source_sha256'] and src[1]==article['source_xml'] and source_notes(db,*key)==article.get('source_notes_xml',''))
                if not guards:errors.append({'key':key,'error':'Canonical source or notes changed'})
                old=db.execute('SELECT source_sha256,status,proposed_xml FROM drafts WHERE code_id=? AND source_id=?',key).fetchone()
                complete=bool(old and old[0]==article['source_sha256'] and (old[2] or old[1]=='retained_unchanged'))
                if job['kind']=='new':state='present_guarded' if complete else 'requeued' if key[1] in pending_new else 'unaccounted'
                else:state='reviewed' if key in reviewed else 'requeued' if key[1] in pending_reviews else 'guard_drift_pending' if key in drift else 'unaccounted'
                dispositions.append({'job':job['job'],'kind':job['kind'],'key':key,'source_guards_passed':guards,'state':state})
                if state=='unaccounted':errors.append({'key':key,'error':'Interrupted work not present or queued'})
    finally:db.close()
    report={'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pid':pid,'old_pid':75807,
            'optimizer_hash_verified':True,'old_drained_exit':old_exit,'single_coordinator_verified':True,
            'configured_roles':limits,'workers':workers,'accepted_jobs':accepted,
            'new_article_acceptance_verified':any(x['kind']=='new' and x['outcome']=='accepted' and x['articles']>0 for x in accepted),
            'review_acceptance_verified':any(x['kind']=='review' and x['outcome']=='reviewed' for x in accepted),
            'inflight_dispositions':dispositions,'errors':errors,'all_inflight_entries_accounted':not errors,
            'performance_gain_claimed':False,'legal_validation_claimed':False,'scope':'Operational resumption only; unchanged full-corpus gates remain, final audit incomplete.'}
    atomic(FOLDER/'resumption-verification.json',report)
    assert not errors, errors
    print(json.dumps({'pid':pid,'accepted_new_jobs':sum(x['kind']=='new' for x in accepted),
        'accepted_review_jobs':sum(x['kind']=='review' for x in accepted),'verified_active_workers':len(keys),
        'inflight_entries_accounted':len(dispositions),'new_acceptance_verified':report['new_article_acceptance_verified']}))
if __name__=='__main__':main()
