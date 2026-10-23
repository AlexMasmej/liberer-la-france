"""Explicit continuation after a prior coordinator has drained.

No independent model invocation or registration path. The coordinator must own
its existing process lock; every job uses its common admission/lease ledger and
unchanged execution, source, policy, benefit, impact, reference and commit guards.
"""
import json
import os
import fcntl
import hashlib
from contextlib import nullcontext
import sqlite3
import time
from pathlib import Path
from register_batches import writer_lock
from contrat_unique_priority import article_priority, priority
from sru_context import priority as sru_priority
from worker_capacity import known_empty_manual_slots


def verify_complete_inventory(coordinator,sources):
    """Reconcile full identities against configuration and official structures.

    Reads the existing coverage/config/plan and canonical structures, with no
    export, backup or second database. The author's already pinned inventory
    totals must agree with every collection and the complete canonical ID set.
    """
    from ingest import inventory
    root=coordinator.HERE
    config_raw=(root/'corpus.json').read_text()
    coverage_raw=(coordinator.CORPUS/'coverage.json').read_text()
    config=json.loads(config_raw);coverage=json.loads(coverage_raw)
    configured=config['codes']+config.get('annexes',[])
    slugs=list(coordinator.SLUGS)
    entries={a['slug']:a for a in configured}
    if len(entries)!=len(configured) or set(entries)!=set(slugs) or not isinstance(sources,dict) or set(sources)!=set(slugs):
        raise ValueError('Complete configured source inventory is unknown or inconsistent')
    covered={a['slug']:a for a in coverage['codes']}
    if len(covered)!=len(coverage['codes']) or set(covered)!=set(slugs) or coverage.get('sources_complete') is not True or coverage.get('missing_archives')!=[] or not coverage.get('as_of'):
        raise ValueError('Complete canonical coverage is unknown or incomplete')
    plan=coordinator.worker_settings(coordinator.RUNTIME)
    pinned=[plan[k] for k in ['baseline_three_worker_status','current_stage_initial_status'] if isinstance(plan.get(k),dict)]
    if not pinned:raise ValueError('Canonical inventory totals are not pinned to the task plan')
    counts={slug:covered[slug]['expected_articles'] for slug in slugs}
    if any(type(n) is not int or n<=0 for n in counts.values()):raise ValueError('Canonical article counts are unknown')
    for receipt in pinned:
        values=receipt.get('codes')
        if not isinstance(values,list):raise ValueError('Pinned collection inventory is unknown')
        expected={r['slug']:r['source_records'] for r in values}
        if len(expected)!=len(values) or expected!=counts or type(receipt.get('source_records')) is not int or receipt['source_records']!=sum(counts.values()):
            raise ValueError('Pinned full canonical inventory changed; review required')
    identities=[]
    db=sqlite3.connect((root/'corpus.sqlite').resolve().as_uri()+'?mode=ro',uri=True,timeout=600)
    try:
        db.execute('BEGIN')
        canonical={(c,i):(sha,number) for c,i,sha,number in db.execute('SELECT code_id,id,source_sha256,number FROM articles')}
        for slug in slugs:
            rows=sources[slug];code=entries[slug]['id'];report=covered[slug]
            if not isinstance(rows,list) or len(rows)!=counts[slug] or report.get('inventory_reconciled') is not True or report.get('imported_versions')!=counts[slug]:
                raise ValueError('Current collection inventory is truncated or incomplete: '+slug)
            tree=inventory(db,code,coverage['as_of'])
            ids=[a['source_id'] for a in rows]
            if tree.get('missing_sections') or tree.get('missing_articles') or len(ids)!=len(set(ids)) or set(ids)!=set(tree['article_ids']) or len(tree['article_ids'])!=counts[slug]:
                raise ValueError('Complete canonical source identities differ: '+slug)
            for a in rows:
                key=(a['code_id'],a['source_id'])
                if a['code_id']!=code or canonical.get(key)!=(a['source_sha256'],a['number']):
                    raise ValueError('Canonical source identity changed: '+str(key))
                identities.append((a['code_id'],a['source_id'],a['source_sha256'],a['number']))
    finally:db.close()
    return {'complete':True,'source_records':sum(counts.values()),'collections':counts,
            'as_of':coverage['as_of'],'identity_sha256':hashlib.sha256(json.dumps(sorted(identities),ensure_ascii=False).encode()).hexdigest(),
            'config_sha256':hashlib.sha256(config_raw.encode()).hexdigest(),
            'coverage_sha256':hashlib.sha256(coverage_raw.encode()).hexdigest()}


def fresh_new_jobs(coordinator,sources,slugs,*,use_writer_lock=True):
    """Reconstruct canonical open identities, never replay saved failed answers.

    Small read transaction only: no DB copy, schema write or snapshot export.
    Already registered retained sources count as completed. A stale, incomplete,
    or nonmatching existing draft is a reconciliation blocker, never an overwrite.
    """
    root=coordinator.HERE
    if not isinstance(sources,dict) or not slugs or len(set(slugs))!=len(slugs):
        raise ValueError('Current source inventory is unknown or invalid')
    seen=set()
    for slug in slugs:
        if slug not in sources or not isinstance(sources[slug],list) or not sources[slug]:
            raise ValueError('Current source inventory is missing or empty for '+slug)
        for source in sources[slug]:
            if not isinstance(source,dict) or any(not source.get(k) for k in ['code_id','source_id','source_sha256','number','source_xml']):
                raise ValueError('Incomplete current source identity in '+slug)
            key=(source['code_id'],source['source_id'])
            if key in seen:raise ValueError('Duplicate current source identity: '+str(key))
            seen.add(key)
    with writer_lock(root) if use_writer_lock else nullcontext():
        db=sqlite3.connect((root/'corpus.sqlite').resolve().as_uri()+'?mode=ro',uri=True,timeout=600)
        try:
            db.execute('BEGIN')
            states={(c,i):(sha,status,body) for c,i,sha,status,body in db.execute(
                'SELECT code_id,source_id,source_sha256,status,proposed_xml FROM drafts')}
            canonical={(c,i):(sha,number) for c,i,sha,number in db.execute(
                'SELECT code_id,id,source_sha256,number FROM articles')}
            jobs=[];held=[]
            for slug in slugs:
                if slug not in sources:raise ValueError('Unknown code '+slug)
                pending=[]
                for source in sources[slug]:
                    key=(source['code_id'],source['source_id'])
                    if canonical.get(key)!=(source['source_sha256'],source['number']):
                        raise ValueError('Canonical source changed before queue reconstruction: '+str(key))
                    existing=states.get(key)
                    if existing:
                        if existing[0]!=source['source_sha256'] or not (existing[2] or existing[1]=='retained_unchanged'):
                            raise ValueError('Existing draft requires reconciliation before continuation: '+str(key))
                        continue
                    if coordinator.needs_graphic_source(source):
                        held.append({'slug':slug,'code_id':key[0],'source_id':key[1],
                                     'number':source['number'],'accepted':False,
                                     'reason':'Normative graphic companion remains unresolved'})
                    else:pending.append(source)
                pending.sort(key=lambda a:(article_priority(a),not bool(a.get('sru_context'))))
                batch_dir=root/'batches'/('automatic-'+slug)
                index=1+max((int(p.stem) for p in batch_dir.glob('*.json') if p.stem.isdigit()),default=0)
                chunk=[];size=0
                for source in pending:
                    amount=len(source['source_xml'])+len(source.get('source_notes_xml',''))+len(json.dumps(source.get('sru_context',[]),ensure_ascii=False))
                    if chunk and (article_priority(chunk[0])!=article_priority(source) or size+amount>45000 or len(chunk)>=24):
                        jobs.append((slug,index,chunk));index+=1;chunk=[];size=0
                    chunk.append(source);size+=amount
                if chunk:jobs.append((slug,index,chunk))
        finally:db.close()
    jobs.sort(key=lambda j:(priority(j),sru_priority(j),j[1],list(sources).index(j[0])))
    return jobs,held


def identities(jobs):
    return tuple(sorted((a['code_id'],a['source_id'],a['source_sha256']) for _,_,rows in jobs for a in rows))


def fresh_recovery_state(coordinator):
    """Supervisor-only fresh read; no model, DB writer, export or process change."""
    from source_assets import load_companions
    companions=load_companions();sources={}
    for slug in coordinator.SLUGS:
        rows=json.loads((coordinator.CORPUS/(slug+'.json')).read_text())
        for row in rows:
            companion=companions.get((row['code_id'],row['source_id']))
            if companion:row['source_companions']=companion
            else:row.pop('source_companions',None)
        sources[slug]=rows
    inventory=verify_complete_inventory(coordinator,sources)
    jobs,held=fresh_new_jobs(coordinator,sources,coordinator.SLUGS,use_writer_lock=False)
    return {'open_accessible_new':sum(len(j[2]) for j in jobs),'held':held,'inventory':inventory}


def drain_decision(evidence):
    """Pure checklist for the parent's future live audit; never an activator.

    Unknown/missing counters are blocking. Recheck this evidence under the
    supervision/manual-slot locks immediately before closing review admissions.
    A second independent process/lock/registration audit is required after exit.
    """
    required=['coordinator_identity_verified','fresh_queue_identity_verified',
              'fresh_inventory_verified','active_batch_owners_verified',
              'registration_guards_clear','source_guards_clear','benefit_guards_clear',
              'impact_guards_clear','reference_guards_clear','no_orphan_or_manual_workers']
    missing=[k for k in required if evidence.get(k) is not True]
    for name in ['pending_new_jobs','reserved_or_running_new_jobs']:
        if type(evidence.get(name)) is not int or evidence[name]!=0:missing.append(name)
    if type(evidence.get('coordinator_pid')) is not int or evidence['coordinator_pid']<=0:
        missing.append('coordinator_pid')
    return {'may_close_review_admissions':not missing,'blocking_or_unknown':missing,
            'must_recheck_under_supervision_lock':True,'activation_performed':False}


def enter_review_tail(coordinator,maximum,new_jobs,sources=None):
    """Only call after the full scheduler/executor context has drained."""
    if new_jobs:raise ValueError('Open accessible drafting sources prevent review-tail reallocation')
    if coordinator.REVIEW_TAIL:raise ValueError('Review tail is already active')
    try:manual=(coordinator.RUNTIME/'manual-agent-slots.lock').open('r+')
    except OSError as error:raise ValueError('Manual reservation lock is unknown') from error
    try:
        fcntl.flock(manual,fcntl.LOCK_EX|fcntl.LOCK_NB)
        with coordinator.SLOTS:
            if coordinator.STOP.is_set():raise ValueError('Stopped coordinator cannot enter review tail')
            if coordinator.ACTIVE or any(coordinator.ACTIVE_BY_KIND.values()) or coordinator.ACTIVE_LEASES:
                raise ValueError('Shared admissions and footprints must be fully drained')
            known_empty_manual_slots(coordinator.RUNTIME)
            inventory_receipt=verify_complete_inventory(coordinator,sources)
            effective=coordinator.admission_limits(coordinator.RUNTIME,maximum,review_tail=True)
            if effective['role_limits'] is None:raise ValueError('Review tail requires an explicit role plan')
            coordinator.REVIEW_TAIL=True
            coordinator.atomic(coordinator.RUNTIME/'continuation-phase.json',{
                'coordinator_pid':os.getpid(),'phase':'review_tail',
                'entered_at_unix':int(time.time()),'effective_limits':effective,
                'open_accessible_new_sources':0,'shared_ledger_drained':True,
                'complete_inventory':inventory_receipt,'manual_reservations_verified_empty':True,
                'manual_reservation_guard':'phase marker rejects new manual reservations; inventory rechecked on every admission',
                'execution_verified':False,'legal_completion_claimed':False})
            coordinator.SLOTS.notify_all()
    except BaseException:
        coordinator.REVIEW_TAIL=False
        raise
    finally:manual.close()
    return effective


def exit_review_tail(coordinator):
    """Retire the phase marker after all tail workers drain; no long-held lock."""
    if not coordinator.REVIEW_TAIL:return
    with (coordinator.RUNTIME/'manual-agent-slots.lock').open('r+') as manual:
        fcntl.flock(manual,fcntl.LOCK_EX)
        with coordinator.SLOTS:
            if coordinator.ACTIVE or any(coordinator.ACTIVE_BY_KIND.values()) or coordinator.ACTIVE_LEASES:
                raise ValueError('Cannot retire phase marker before full review-tail drain')
            phase=json.loads((coordinator.RUNTIME/'continuation-phase.json').read_text())
            coordinator.atomic(coordinator.RUNTIME/'continuation-phase.json',phase|{
                'phase':'review_tail_drained','drained_at_unix':int(time.time())})
            coordinator.REVIEW_TAIL=False


def run(coordinator,codex,args):
    """Fresh new waves, fresh before-images for review waves, reference convergence.

    No-progress is blocking: residual sources/reviews remain explicit and are
    never converted into an acceptance or counted as legally complete.
    """
    import review_prior
    maximum=args.workers
    slugs=args.slugs.split(',')
    plan=coordinator.worker_settings(coordinator.RUNTIME)
    if plan.get('continuation_mode')!='recover_new_before_reviews':
        raise ValueError('Recovery continuation must be explicitly selected in the task plan')
    checkpoint=coordinator.progress(coordinator.load_sources(coordinator.SLUGS))
    exported=checkpoint['drafted_articles']+checkpoint['retained_unchanged']+checkpoint.get('prior_drafts_reviewed',0)

    def consume(scheduled,sources):
        nonlocal exported
        for future in coordinator.scheduled_futures(scheduled,codex,sources,maximum):
            try:
                future.result()
                if args.export_every and not coordinator.STOP.is_set():
                    state=coordinator.progress(sources)
                    count=state['drafted_articles']+state['retained_unchanged']+state.get('prior_drafts_reviewed',0)
                    if count-exported>=args.export_every:
                        coordinator.publish_checkpoint(args.deploy_on_export);exported=count
            except Exception:
                coordinator.STOP.set()
                raise

    sources=None
    try:
        seen_new=set()
        while not coordinator.STOP.is_set():
            sources=coordinator.load_sources(coordinator.SLUGS)
            verify_complete_inventory(coordinator,sources)
            jobs,held=fresh_new_jobs(coordinator,sources,slugs)
            coordinator.atomic(coordinator.RUNTIME/'continuation-open-new.json',{
                'jobs':[{'slug':s,'index':i,'source_ids':[a['source_id'] for a in rows]} for s,i,rows in jobs],
                'held_graphic_sources':held,'accepted':False,'derived_from_current_canonical_state':True})
            coordinator.atomic(coordinator.RUNTIME/'queue-admission-plan.json',{
                'coordinator_pid':os.getpid(),'phase':'recover_current_new',
                'capacity':maximum,'initial_admission_limits':coordinator.current_limits(maximum),
                'scheduled_by_kind':{'new':len(jobs),'review':0},
                'borrowing_enabled':False,'authorized_reallocation':False,
                'queue_file':'continuation-open-new.json','execution_verified':False})
            if not jobs:break
            fingerprint=identities(jobs)
            if fingerprint in seen_new:
                raise ValueError('Drafting recovery made no progress; unresolved identities preserved in continuation-open-new.json')
            seen_new.add(fingerprint)
            consume([(job,False) for job in jobs],sources)
        if coordinator.STOP.is_set():return
        # A scope restriction may not hide unresolved first passes elsewhere.
        all_new,all_held=fresh_new_jobs(coordinator,sources,coordinator.SLUGS)
        enter_review_tail(coordinator,maximum,all_new,sources)
        seen_reviews=set()
        while not coordinator.STOP.is_set():
            if coordinator.role_reviews_paused(maximum):
                coordinator.progress(sources,'checkpoint');return
            # build_jobs captures full DB and active-batch before-images anew.
            jobs=review_prior.build_jobs(sources)
            coordinator.atomic(coordinator.RUNTIME/'queue-admission-plan.json',{
                'coordinator_pid':os.getpid(),'phase':'review_tail','capacity':maximum,
                'effective_limits':coordinator.current_limits(maximum),
                'scheduled_by_kind':{'new':0,'review':len(jobs)},
                'borrowing_enabled':False,'authorized_reallocation':True,
                'queue_source':'fresh current full DB and active-batch before-images',
                'execution_verified':False})
            report=json.loads(review_prior.revisions_manifest().read_text())
            unresolved=[a for a in report['prior_articles'] if a['review_status']=='pending']
            if not jobs:
                if unresolved:raise ValueError('Pending prior reviews have changed before-images; manual reconciliation is required')
                break
            fingerprint=tuple(sorted((a['code_id'],a['source_id'],a['previous_draft']['proposed_sha256'],
                                      a['previous_draft'].get('batch_row_sha256'))
                                     for _,_,rows in jobs for a in rows))
            if fingerprint in seen_reviews:
                raise ValueError('Prior review made no progress; unresolved before-images remain pending')
            seen_reviews.add(fingerprint)
            consume([(job,True) for job in jobs],sources)
        if not coordinator.STOP.is_set():coordinator.run_reference_review_phase(sources,codex,maximum)
        if not coordinator.STOP.is_set():
            coordinator.progress(sources,'checkpoint')
    except Exception as error:
        coordinator.STOP.set()
        if sources is not None:coordinator.progress(sources,'blocked',str(error))
        raise
    finally:
        try:
            if sources is not None and (args.export_every or args.publish_at_end):
                coordinator.publish_checkpoint(args.publish_at_end)
        finally:exit_review_tail(coordinator)
