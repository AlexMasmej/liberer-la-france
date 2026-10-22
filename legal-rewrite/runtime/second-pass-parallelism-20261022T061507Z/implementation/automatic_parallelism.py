"""Bounded, task-local promotion at the existing minute-by-minute health check.

Never launches an agent, accepts an article, changes a global setting, or
weakens a drafting validator. A durable intent permits safe file reconciliation.
"""
from pathlib import Path
from datetime import datetime,timezone
import fcntl,hashlib,json,sqlite3,statistics,tempfile

MAIN_CODES={'travail','impots','securite-sociale','urbanisme','construction-habitation'}
EXECUTION={'model':'gpt-6-astra','reasoning_effort':'medium'}


def read(path,default=None):
    return json.loads(path.read_text()) if path.exists() else default


def atomic(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.NamedTemporaryFile(mode='w',encoding='utf-8',dir=path.parent,delete=False) as stream:
        temporary=Path(stream.name);json.dump(value,stream,ensure_ascii=False,indent=2)
    try:temporary.replace(path)
    finally:temporary.unlink(missing_ok=True)


def cohort(runtime,pid,start):
    selected=[]
    for line in (runtime/'job-metrics.jsonl').read_text().splitlines(keepends=True):
        if not line.endswith('\n'):raise ValueError('Incomplete metrics write; defer this check')
        item=json.loads(line)
        # Exclude initialization and boundary jobs, as well as other models/PIDs.
        if item.get('coordinator_pid')==pid and item['started_at_unix']>=start:
            selected.append(item)
    return selected


def evaluate(runtime,plan,live,workers,locked,status,now):
    reasons=[];rules=plan['promotion'];pid=plan['stage_coordinator_pid']
    start=datetime.fromisoformat(plan['stage_started_at_utc']).timestamp()
    elapsed=(now-start)/3600
    metrics=cohort(runtime,pid,start)
    success=[m for m in metrics if m['outcome'] in {'accepted','reviewed'}]
    retry_fraction=sum(m['attempts']>1 for m in success)/len(success) if success else 1
    rate=len(success)/elapsed if elapsed>0 else 0
    run=read(runtime/'coordinator-run.json',{})
    if not plan.get('explicit_promotion_authorization',{}).get('approved'):reasons.append('missing_user_authorization')
    if len(live)!=1 or live[0]['pid']!=pid or not locked:reasons.append('coordinator_identity_or_lock')
    if run.get('pid')!=pid or run.get('capacity',0)<6 or run.get('requested_execution')!=EXECUTION:reasons.append('coordinator_execution_or_capacity')
    if status.get('status')!='running' or status.get('failure'):reasons.append('coordinator_not_healthy')
    if not workers or any(w['ppid']!=pid or not w['execution'].get('verified') or
        any(w['execution'].get(k)!=v for k,v in EXECUTION.items()) for w in workers):
        reasons.append('active_execution_not_yet_verified')
    if elapsed<rules['minimum_hours_at_four_workers']:reasons.append('minimum_observation_window')
    if len(success)<rules['minimum_successful_jobs']:reasons.append('minimum_successful_jobs')
    if retry_fraction>rules['maximum_retry_job_fraction']:reasons.append('retry_fraction')
    if rate<rules['baseline_successful_jobs_per_hour']*(1+rules['minimum_job_throughput_gain_over_baseline']):reasons.append('throughput_gain')
    if any(m['outcome'] not in {'accepted','reviewed','skipped'} for m in metrics):reasons.append('new_deferred_or_blocked_outcome')
    if any(not m.get('execution_verified') or any(m.get(k)!=v for k,v in EXECUTION.items()) for m in success):reasons.append('completed_execution_evidence')
    if not MAIN_CODES<={m['slug'] for m in success}:reasons.append('five_code_sample')
    if {m['kind'] for m in success}!={'new','review'}:reasons.append('new_and_review_sample')
    proof=Path(plan['model_migration_proof_directory']).resolve()
    if not proof.is_relative_to(runtime.parent.resolve()):raise ValueError('Unexpected proof directory')
    before=read(proof/'cohort-start-failed-jobs.json')
    if before is None:raise ValueError('Missing deferred-job baseline')
    canonical=lambda value:json.dumps(value,sort_keys=True,ensure_ascii=False)
    baseline={canonical(m) for m in before}
    new_deferred=[m for m in read(runtime/'failed-jobs.json',[]) if canonical(m) not in baseline]
    if new_deferred:reasons.append('new_deferred_registry_entries')
    report={'checked_at_utc':datetime.fromtimestamp(now,timezone.utc).isoformat(),
            'coordinator_pid':pid,'hours_since_verified_four_worker_start':elapsed,
            'successful_jobs':len(success),'successful_jobs_per_hour':rate,
            'retry_job_fraction':retry_fraction,'new_deferred_entries':len(new_deferred),
            'successful_by_code':{s:sum(m['slug']==s for m in success) for s in sorted(MAIN_CODES)},
            'active_workers_execution_verified':sum(w['execution'].get('verified',False) for w in workers),
            'decision':'hold_at_four' if reasons else 'eligible_for_validation_audit',
            'reasons':reasons,'promotion_validated':False,'confirmation_required':False,
            'measurement_note':'Post-start Astra/medium jobs only; historical baseline is not a matched-model benchmark.'}
    return report,success


def audit_jobs(runtime,metrics):
    """Re-run the existing source/benefit/impact/reference checks, in memory."""
    import run_exhaustive as runner
    from worker_execution import verify_execution
    root=runtime.parent.parent
    db=sqlite3.connect('file:'+str(root/'corpus.sqlite')+'?mode=ro',uri=True)
    characters={'new':[],'review':[]};articles=0
    try:
        db.execute('BEGIN')
        for metric in metrics:
            folder=(runtime/'jobs'/metric['job']).resolve()
            if not folder.is_relative_to((runtime/'jobs').resolve()):raise ValueError('Unexpected job directory')
            attempt=metric['attempts'];execution=verify_execution(folder,EXECUTION,folder/f'errors-{attempt}.log')
            if not execution['verified'] or execution.get('session_id')!=metric.get('execution_session_id'):
                raise ValueError('Native execution evidence differs: '+metric['job'])
            if not runner.policy_is_current(folder):raise ValueError('Policy changed since sample: '+metric['job'])
            source_text=(folder/'source.json').read_text();source=json.loads(source_text)
            if len(source)!=metric['articles']:raise ValueError('Source count differs: '+metric['job'])
            target_text=(folder/'reference-targets.json').read_text();targets=json.loads(target_text)
            for article in source:
                row=db.execute('SELECT content_xml,source_sha256,number FROM articles WHERE code_id=? AND id=?',
                               (article['code_id'],article['source_id'])).fetchone()
                if row!=(article['source_xml'],article['source_sha256'],article['number']):
                    raise ValueError('Whole canonical source differs: '+metric['job'])
                if runner.source_notes(db,article['code_id'],article['source_id'])!=article.get('source_notes_xml',''):
                    raise ValueError('Canonical source notes differ: '+metric['job'])
            answer=runner.validate_answer(read(folder/'answer.json'),source)
            runner.reference_audit.accept_checks(answer,source,targets)
            if metric['kind']=='new':
                intent=read(folder/'registration-intent.json',{});complete=read(folder/'registration-complete.json',{})
                if (intent.get('source_sha256')!=hashlib.sha256(source_text.encode()).hexdigest() or
                    intent.get('reference_sha256')!=hashlib.sha256(target_text.encode()).hexdigest() or
                    not 0<complete.get('accepted_articles',0)<=len(source)):
                    raise ValueError('Missing completed registration evidence: '+metric['job'])
            characters[metric['kind']].append(sum(len(a['source_xml'])+len(a.get('source_notes_xml','')) for a in source))
            articles+=len(source)
    finally:db.close()
    return {'jobs':len(metrics),'articles':articles,'source_benefit_impact_reference_checks_passed':True,
            'source_characters_by_kind':{kind:{'minimum':min(sizes),'median':statistics.median(sizes),'maximum':max(sizes)}
                                         for kind,sizes in characters.items() if sizes},
            'reference_scope':'Existing dependency catalogue; this is not the final exhaustive reference audit.'}


def snapshot_inputs(runtime,refresh):
    live,workers,locked,status=refresh()
    return live,workers,locked,status


def promote_if_ready(runtime,refresh,now,*,audit=audit_jobs):
    runtime=Path(runtime);path=runtime/'parallelism-plan.json';plan=read(path,{})
    if not plan.get('promotion',{}).get('automatic_minute_check'):return None
    if plan.get('capacity')!=6 or plan.get('target_workers')!=6:return None
    intent_path=runtime/'promotion-intent.json';intent=read(intent_path,{})
    # A successful plan write followed by a failed limit write is recoverable.
    if plan.get('current_workers')==6 and intent.get('state')=='prepared':
        with (runtime/'manual-agent-slots.lock').open('a') as lock:
            fcntl.flock(lock,fcntl.LOCK_EX);current=read(path)
            if current.get('promotion_event_id')!=intent.get('event_id'):return None
            reservations=read(runtime/'manual-agent-slots.json',[])
            if len(reservations)>=6:return {'decision':'hold_reconciliation','reason':'manual_slots'}
            atomic(runtime/'worker-limit.json',{'workers':6-len(reservations)})
            intent['state']='complete';atomic(intent_path,intent)
            return {'decision':'promoted_to_six','reconciled':True,'workers':6-len(reservations)}
    if plan.get('current_workers')==6:
        if plan.get('effective_six_verified_at_utc'):return None
        live,workers,locked,status=snapshot_inputs(runtime,refresh)
        pid=plan['stage_coordinator_pid']
        if (len(live)!=1 or live[0]['pid']!=pid or not locked or status.get('status')!='running'
                or len(workers)!=6 or len({w.get('pid') for w in workers})!=6
                or len({w['execution'].get('session_id') for w in workers})!=6
                or any(w['ppid']!=pid or not w['execution'].get('verified') or
                    any(w['execution'].get(k)!=v for k,v in EXECUTION.items()) for w in workers)):
            return None
        observed={'decision':'six_agents_effectively_verified','coordinator_pid':pid,
                  'verified_at_utc':datetime.fromtimestamp(now,timezone.utc).isoformat(),
                  'active_workers':workers,'model':EXECUTION['model'],
                  'reasoning_effort':EXECUTION['reasoning_effort']}
        with (runtime/'manual-agent-slots.lock').open('a') as lock:
            fcntl.flock(lock,fcntl.LOCK_EX);current=read(path)
            if current.get('promotion_event_id')!=plan.get('promotion_event_id') or current.get('current_workers')!=6:return None
            if current.get('effective_six_verified_at_utc'):return None
            atomic(runtime/'promotion-execution.json',observed)
            current['effective_six_verified_at_utc']=observed['verified_at_utc'];atomic(path,current)
        return observed
    if plan.get('current_workers')!=4:return None
    inputs=snapshot_inputs(runtime,refresh)
    try:report,success=evaluate(runtime,plan,*inputs,now)
    except (OSError,ValueError,TypeError,KeyError) as error:
        report={'decision':'hold_at_four','reasons':['promotion_telemetry_unavailable'],
                'error_type':type(error).__name__,'confirmation_required':False}
        success=[]
    if not report['reasons']:
        try:
            report['validation_audit']=audit(runtime,success)
            if (report['validation_audit'].get('source_benefit_impact_reference_checks_passed') is not True
                    or report['validation_audit'].get('jobs')!=len(success)):
                raise ValueError('Validation audit did not confirm the complete sample')
            # A newly finished job must be included in the audit, not waved through.
            fresh=snapshot_inputs(runtime,refresh)
            checked,latest=evaluate(runtime,plan,*fresh,now)
            if checked['reasons']:report=checked
            elif {m['job'] for m in latest}!={m['job'] for m in success}:
                report.update(decision='hold_at_four',reasons=['sample_changed_during_audit'])
        except Exception as error:
            report.update(decision='hold_at_four',reasons=['validation_audit_failed'],
                          audit_error_type=type(error).__name__,audit_error=str(error)[:300])
    with (runtime/'manual-agent-slots.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX);current=read(path)
        if ((current.get('current_workers'),current.get('stage_coordinator_pid'),current.get('stage_started_at_utc'))!=(4,plan.get('stage_coordinator_pid'),plan.get('stage_started_at_utc'))
                or current.get('promotion')!=plan.get('promotion')
                or current.get('explicit_promotion_authorization')!=plan.get('explicit_promotion_authorization')):
            return {'decision':'hold_at_four','reasons':['plan_changed_during_check']}
        reservations=read(runtime/'manual-agent-slots.json',[])
        if len(reservations)>=6:report.update(decision='hold_at_four',reasons=['manual_slots'])
        if report['reasons']:
            current['latest_evaluation']=report;atomic(path,current);return report
        event_id=report['checked_at_utc']+'-'+str(plan['stage_coordinator_pid'])
        report.update(decision='promoted_to_six',promotion_validated=True,workers=6-len(reservations))
        atomic(runtime/'promotion-evidence.json',report)
        intent={'event_id':event_id,'state':'prepared','coordinator_pid':plan['stage_coordinator_pid'],
                'evidence':'promotion-evidence.json','target_workers':6}
        atomic(intent_path,intent)
        current.update(current_workers=6,stage='six_worker_run_astra_medium',promotion_event_id=event_id,
                       promoted_at_utc=report['checked_at_utc'],latest_evaluation=report)
        atomic(path,current)
        atomic(runtime/'worker-limit.json',{'workers':6-len(reservations)})
        intent['state']='complete';atomic(intent_path,intent)
        return report
