"""Second pass requested by the author, preserving every earlier draft.

Called under the coordinator lock, either separately or between new drafts.
No old draft is overwritten unless its full database before-image matches.
New jobs also pin the complete active batch row, including audit metadata.
"""
from pathlib import Path
import json,hashlib,re,sqlite3,time,os
import concurrent.futures,subprocess,sys,itertools
from register_batches import writer_lock,register,_register as register_locked
from ingest import HERE,open_db
from sru_context import priority as sru_priority
from contrat_unique_priority import article_priority as cu_article_priority, priority as cu_priority

def digest(value):return hashlib.sha256((value or '').encode()).hexdigest()

def revisions_manifest():return HERE/'runtime/radical-review-20261019.json'

def batch_row_sha256(row):
    """Hash one whole JSON row, independent of file layout or key order."""
    return digest(json.dumps(row,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False))

_OWNER_INDEX_CACHE={}

def batch_owners(keys,root=None):
    """Caller holds writer_lock from this scan through capture or revision."""
    owners={};files={}
    for path in sorted(((HERE if root is None else root)/'batches').glob('*/*.json')):
        if not re.fullmatch(r'(?:batch)?\d+\.json',path.name):continue
        payload=path.read_bytes();sha=hashlib.sha256(payload).hexdigest()
        cached=_OWNER_INDEX_CACHE.get(path)
        items=None
        if cached is not None and cached[0]==sha:
            index_rows=cached[1]
        else:
            items=json.loads(payload.decode('utf-8'))
            index_rows=tuple((index,(item['code_id'],item['source_id'])) for index,item in enumerate(items))
            if len(_OWNER_INDEX_CACHE)>=2048:_OWNER_INDEX_CACHE.clear()
            _OWNER_INDEX_CACHE[path]=(sha,index_rows)
        # Only the location index is reused, after hashing the complete current
        # file. Selected rows are decoded afresh, never shared mutable objects.
        selected=[(index,key) for index,key in index_rows if key in keys]
        if selected and items is None:items=json.loads(payload.decode('utf-8'))
        for index,key in selected:
            if key in owners:raise ValueError('Duplicate active batch owner: '+str(key))
            owners[key]=(path,index);files[path]=items
    return owners,files

def draft_values(row):
    return (row['source_sha256'],row.get('status','rewrite_draft'),row['proposed_xml'],row['reason'],row['review_notes'])

def pending_sources(sources):
    result={};changed=[];seen=set()
    with writer_lock():
        report=json.loads(revisions_manifest().read_text())
        wanted={(a['code_id'],a['source_id']):a for a in report['prior_articles'] if a['review_status']=='pending'}
        owners,files=batch_owners(wanted)
        # The writer lock keeps batch metadata and DB fields from different
        # registrations out of the same job. BEGIN pins all DB reads as well.
        db=sqlite3.connect((HERE/'corpus.sqlite').resolve().as_uri()+'?mode=ro',uri=True,timeout=600)
        db.execute('BEGIN')
        try:
            for slug,articles in sources.items():
                rows=[]
                for source in articles:
                    key=(source['code_id'],source['source_id']);prior=wanted.get(key)
                    if not prior:continue
                    seen.add(key)
                    old=db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?',key).fetchone()
                    if not old or old[0]!=source['source_sha256'] or digest(old[2])!=prior['proposed_sha256']:
                        changed.append({'code_id':key[0],'source_id':key[1],'reason':'Source or proposal changed; manual comparison required'});continue
                    batch=None
                    if key in owners:
                        path,index=owners[key];batch=files[path][index]
                        if draft_values(batch)!=old:
                            changed.append({'code_id':key[0],'source_id':key[1],'reason':'Active batch and database before-images differ; manual comparison required'});continue
                    # Present with null means a captured legacy absence; an
                    # absent key identifies historical jobs without this guard.
                    rows.append(source|{'previous_draft':{'source_sha256':old[0],'status':old[1],'proposed_xml':old[2],'reason':old[3],'review_notes':old[4],'proposed_sha256':digest(old[2]),'batch_row_sha256':batch_row_sha256(batch) if batch is not None else None}})
                result[slug]=rows
        finally:db.close()
        report['changed_since_inventory']=changed
        outside=set(wanted)-seen
        report['outside_current_inventory']=[{'code_id':c,'source_id':i,'reason':'Historical draft not included in the current official article inventory; preserved separately'} for c,i in sorted(outside)]
        for article in report['prior_articles']:
            if (article['code_id'],article['source_id']) in outside and article['review_status']=='pending':article['review_status']='outside_current_inventory'
        temporary=revisions_manifest().with_suffix('.tmp');temporary.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');temporary.replace(revisions_manifest())
    return result

def commit(rows,expected,reference_snapshot=None):
    started=time.perf_counter()
    prior={(a['code_id'],a['source_id']):a['previous_draft'] for a in expected}
    with writer_lock():
        acquired=time.perf_counter()
        owners,files=batch_owners(prior)
        file_before={path:path.read_bytes() for path in files}
        legacy_path=None
        archive=[];legacy=[]
        db=open_db(HERE/'corpus.sqlite')
        try:
            if reference_snapshot is not None:
                from reference_coherence import check_guards
                check_guards(db,reference_snapshot)
            for row in rows:
                key=(row['code_id'],row['source_id']);old=prior[key]
                current=db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?',key).fetchone()
                if not current or current!=draft_values(old) or digest(current[2])!=old['proposed_sha256']:
                    raise ValueError('Refusing to replace a changed draft during radical review: '+str(key))
                if 'batch_row_sha256' in old:
                    batch=None
                    if key in owners:
                        path,index=owners[key];batch=files[path][index]
                    actual=batch_row_sha256(batch) if batch is not None else None
                    if actual!=old['batch_row_sha256']:
                        raise ValueError('Refusing to replace a changed active batch row during radical review: '+str(key))
                canonical=db.execute('SELECT source_sha256 FROM articles WHERE code_id=? AND id=?',key).fetchone()
                if not canonical or canonical[0]!=row['source_sha256']:
                    raise ValueError('Refusing to revise a changed canonical source: '+str(key))
                archive.append({'code_id':key[0],'source_id':key[1],'source_sha256':current[0],'status':current[1],'proposed_xml':current[2],'reason':current[3],'review_notes':current[4],'replacement':row})
                row['policy_review_id']='substantive_outcomes_2026_10_19' if row.get('substantive_impact') else 'editorial_direction_2026_10_19'
                row['prior_proposal_sha256']=old['proposed_sha256']
                if key in owners:
                    path,index=owners[key];files[path][index]=row
                else:legacy.append(row)
            # Durable before-image, written before any existing batch is revised.
            audit=HERE/'revisions/radical-review';audit.mkdir(parents=True,exist_ok=True)
            identifier=digest(json.dumps(archive,ensure_ascii=False,sort_keys=True))
            (audit/(identifier+'.json')).write_text(json.dumps(archive,ensure_ascii=False,indent=2)+'\n')
            registry_path=HERE/'registered-batches.json';registry_before=registry_path.read_bytes();registry=json.loads(registry_before)
            # Legacy first drafts may precede the batch registry: adopt only the
            # exact, archived before-image, never a different independent draft.
            for row in rows:
                key=(row['code_id'],row['source_id']);old=prior[key]
                registry['|'.join(key)]={'source_sha256':old['source_sha256'],'proposed_sha256':old['proposed_sha256']}
            registry_path.write_text(json.dumps(registry,ensure_ascii=False,indent=2)+'\n')
            for path,items in files.items():
                temporary=path.with_suffix('.tmp');temporary.write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n');temporary.replace(path)
            if legacy:
                folder=HERE/'batches/radical-review-legacy';folder.mkdir(exist_ok=True)
                index=1+max((int(p.stem) for p in folder.glob('*.json')),default=0)
                legacy_path=folder/f'{index:05d}.json'
                legacy_path.write_text(json.dumps(legacy,ensure_ascii=False,indent=2)+'\n')
            # Keep the same non-reentrant writer lock from target checks through
            # canonical registration. The public register() wrapper would lock
            # again; use its already-locked implementation here.
            validation_started=time.perf_counter()
            try:
                register_locked(db,HERE/'batches',True)
            except Exception:
                db.rollback()
                unchanged=all(db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?',key).fetchone()==draft_values(old) for key,old in prior.items())
                # A validation/transaction failure must not leak staged batch
                # writes into a later worker's full-corpus registration. Once
                # SQLite committed, retain evidence for manual reconciliation.
                if unchanged:
                    for path,payload in file_before.items():
                        temporary=path.with_suffix('.rollback.tmp');temporary.write_bytes(payload);temporary.replace(path)
                    if legacy_path is not None:legacy_path.unlink()
                    temporary=registry_path.with_suffix('.rollback.tmp');temporary.write_bytes(registry_before);temporary.replace(registry_path)
                raise
            validation_finished=time.perf_counter()
        finally:db.close()
        # Finalize successful acceptance before releasing the writer lock.
        # Reacquiring it here lets other full-corpus registrations indefinitely
        # delay completion bookkeeping and keep all review slots occupied.
        report=json.loads(revisions_manifest().read_text());done={(a['code_id'],a['source_id']) for a in rows}
        for article in report['prior_articles']:
            if (article['code_id'],article['source_id']) in done:article['review_status']='completed'
        report['completed_second_pass']=sum(a['review_status']=='completed' for a in report['prior_articles'])
        temporary=revisions_manifest().with_suffix('.tmp');temporary.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');temporary.replace(revisions_manifest())
    # Operational timing only: never let a telemetry write undo acceptance.
    finished=time.perf_counter()
    measurement={'pid':os.getpid(),'accepted_at_unix':time.time(),'articles':len(rows),
                 'writer_wait_seconds':acquired-started,
                 'full_registration_seconds':validation_finished-validation_started,
                 'writer_section_seconds':finished-acquired,'total_seconds':finished-started}
    try:
        with (HERE/'runtime/registration-timings.jsonl').open('a') as log:
            log.write(json.dumps(measurement)+'\n')
    except OSError:pass

def build_jobs(sources):
    pending=pending_sources(sources);per_code=[]
    for slug,articles in pending.items():
        articles.sort(key=lambda a:(cu_article_priority(a),not bool(a.get('sru_context'))))
        chunk=[];size=0;index=0;jobs=[]
        for article in articles:
            amount=len(article['source_xml'])+len(article['previous_draft']['proposed_xml'] or '')+len(json.dumps(article.get('sru_context',[]),ensure_ascii=False))
            if chunk and (cu_article_priority(chunk[0])!=cu_article_priority(article) or size+amount>45000 or len(chunk)>=12):
                index+=1;jobs.append((slug,index,chunk));chunk=[];size=0
            chunk.append(article);size+=amount
        if chunk:
            index+=1;jobs.append((slug,index,chunk))
        per_code.append(jobs)
    # Review every code while new drafting also progresses.
    return sorted([job for group in itertools.zip_longest(*per_code) for job in group if job is not None],key=lambda job:(cu_priority(job),sru_priority(job)))

def run(coordinator,sources,codex,maximum=3):
    jobs=build_jobs(sources)
    print('RADICAL REVIEW START',len(jobs),'jobs;',sum(len(rows) for _,_,rows in jobs),'previous articles',flush=True)
    report=json.loads(revisions_manifest().read_text());exported=report.get('completed_second_pass',0)
    with concurrent.futures.ThreadPoolExecutor(max_workers=maximum) as pool:
        futures=[pool.submit(coordinator.run_in_slot,job,codex,sources,maximum,True) for job in jobs]
        for future in concurrent.futures.as_completed(futures):
            try:future.result()
            except Exception as error:
                coordinator.STOP.set();coordinator.progress(sources,'blocked',str(error));raise
            report=json.loads(revisions_manifest().read_text())
            if report.get('completed_second_pass',0)-exported>=200:
                subprocess.run([sys.executable,str(HERE/'publish_snapshot.py')],check=True,cwd=HERE.parent)
                exported=report['completed_second_pass']
    print('RADICAL REVIEW CHECKPOINT',json.loads(revisions_manifest().read_text()).get('completed_second_pass',0),'articles',flush=True)
