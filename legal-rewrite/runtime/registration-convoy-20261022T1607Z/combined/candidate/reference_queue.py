"""A final, repeatable dependency review, separate from article rewriting counts."""
from pathlib import Path
import concurrent.futures,json,re,sqlite3,time
from ingest import HERE
from reference_coherence import requirements,certificate_current,digest,key,state
from contrat_unique_priority import priority
from register_batches import writer_lock
from review_prior import batch_owners,batch_row_sha256

REPORT=HERE/'runtime/reference-coherence.json'

def certificates():
    result={}
    for path in sorted((HERE/'batches').glob('*/*.json')):
        if not re.fullmatch(r'(?:batch)?\d+\.json',path.name):continue
        for row in json.loads(path.read_text()):
            if row.get('reference_coherence'):
                result[key(row)]=(digest(row.get('proposed_xml')),row['reference_coherence'])
    return result

def pending(sources,save=True):
    with writer_lock(HERE):return _pending(sources,save)

def _pending(sources,save=True):
    known=certificates();result={};reviewed=0;relevant=0;drafted=0;retained=0;unwritten=0;details=[]
    db=sqlite3.connect('file:'+str(HERE/'corpus.sqlite')+'?mode=ro',uri=True);db.execute('BEGIN')
    try:
        for slug,rows in sources.items():
            selected=[]
            for a in rows:
                old=db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?',(a['code_id'],a['source_id'])).fetchone()
                if not old or (not old[2] and old[1]!='retained_unchanged') or old[0]!=a['source_sha256']:
                    if requirements(a,db=db):unwritten+=1
                    continue
                if old[1]=='retained_unchanged':retained+=1
                else:drafted+=1
                if not requirements(a,old[2],db=db):continue
                relevant+=1;entry=known.get(key(a));certificate=entry[1] if entry and entry[0]==digest(old[2]) else None
                if certificate_current(db,a,old[2],certificate):reviewed+=1;continue
                previous=dict(zip(['source_sha256','status','proposed_xml','reason','review_notes'],old));previous['proposed_sha256']=digest(old[2])
                selected.append(a|{'previous_draft':previous,'reference_recheck_only':True})
                details.append({'slug':slug,'code_id':a['code_id'],'source_id':a['source_id'],'number':a['number'],'proposed_sha256':digest(old[2]),'dependency_fingerprint':digest(json.dumps([state(db,k) for k in sorted(requirements(a,old[2],db=db))],sort_keys=True)),'reason':'Contract-law reference certificate missing or dependencies changed'})
            result[slug]=selected
    finally:db.close()
    selected=[a for rows in result.values() for a in rows]
    owners,files=batch_owners({(a['code_id'],a['source_id']) for a in selected},root=HERE)
    for article in selected:
        owner=owners.get((article['code_id'],article['source_id']))
        article['previous_draft']['batch_row_sha256']=batch_row_sha256(files[owner[0]][owner[1]]) if owner else None
    report={'updated_at_unix':int(time.time()),'scope':'all five codes and CGI annexes; contract-unique dependencies only','drafted_articles_scanned':drafted,'retained_sources_scanned':retained,'relevant_drafted_articles':relevant,'current_reference_certificates':reviewed,'pending_reference_reviews':len(details),'relevant_sources_not_yet_rewritten':unwritten,'pending':details,'semantic_review_by_jurist':False,'all_detected_contract_reference_checks_current':not details and not unwritten}
    if save:
        temporary=REPORT.with_suffix('.tmp');temporary.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');temporary.replace(REPORT)
    return result,report

def jobs(sources):
    rows,report=pending(sources);result=[]
    for slug,articles in rows.items():
        chunk=[];size=0;index=1
        for article in articles:
            amount=len(article['source_xml'])+len(article['source_notes_xml'])+len(article['previous_draft']['proposed_xml'] or '')
            if chunk and (size+amount>45000 or len(chunk)>=12):
                result.append((slug,index,chunk));index+=1;chunk=[];size=0
            chunk.append(article);size+=amount
        if chunk:result.append((slug,index,chunk))
    return sorted(result,key=priority),report

def run(coordinator,sources,codex,workers):
    seen=set()
    while not coordinator.STOP.is_set():
        queue,report=jobs(sources)
        if not queue:return report
        fingerprint=tuple((a['code_id'],a['source_id'],a['proposed_sha256'],a['dependency_fingerprint']) for a in report['pending'])
        if fingerprint in seen:raise ValueError('Reference review did not converge; unresolved full-article checks preserved in runtime/reference-coherence.json')
        seen.add(fingerprint)
        print('REFERENCE REVIEW',len(queue),'jobs;',len(report['pending']),'articles requiring current target checks',flush=True)
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
            futures=[pool.submit(coordinator.run_in_slot,j,codex,sources,workers,True) for j in queue]
            try:
                for future in concurrent.futures.as_completed(futures):future.result()
            except BaseException:
                # Stop waiting slot holders before the pool drains queued work.
                coordinator.STOP.set()
                for future in futures:future.cancel()
                raise
    return pending(sources)[1]
