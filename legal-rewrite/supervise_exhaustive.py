"""One bounded health check, launched every minute by the user's launch agent.

Adopts a running coordinator, restarts a disappeared one, and never accepts
drafts or declares the legal corpus complete. All legal checks stay in the
existing coordinator. No credentials or account configuration are read.
"""
from pathlib import Path
import datetime,fcntl,json,os,shlex,shutil,sqlite3,subprocess,sys,tempfile,time
from worker_capacity import settings as worker_settings
from worker_execution import requested_execution,verify_execution
from automatic_parallelism import promote_if_ready

HERE=Path(__file__).resolve().parent
RUNTIME=HERE/'runtime/exhaustive'
SUPERVISION=HERE/'runtime/supervision'
RUNNER=HERE/'run_exhaustive.py'
SCOPE=['travail','impots','securite-sociale','urbanisme','construction-habitation',
       *[f'impots-annexe-{i}' for i in range(1,5)]]


def read_json(path,default=None):
    if not path.exists():return default
    return json.loads(path.read_text())


def atomic(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary=None
    try:
        with tempfile.NamedTemporaryFile(mode='w',encoding='utf-8',dir=path.parent,
                                         prefix='.'+path.name,delete=False) as stream:
            temporary=Path(stream.name)
            json.dump(value,stream,ensure_ascii=False,indent=2)
        temporary.replace(path)
    finally:
        if temporary is not None:temporary.unlink(missing_ok=True)


def processes():
    result=[]
    output=subprocess.check_output(['/bin/ps','-axo','pid=,ppid=,command='],text=True,timeout=15)
    for line in output.splitlines():
        parts=line.strip().split(None,2)
        if len(parts)!=3:continue
        try:args=shlex.split(parts[2])
        except ValueError:continue
        result.append({'pid':int(parts[0]),'ppid':int(parts[1]),'args':args})
    return result


def coordinator_processes(rows):
    # Match a complete script argument, never a substring or a stale PID alone.
    return [p for p in rows if len(p['args'])>1
            and Path(p['args'][0]).name.lower().startswith('python')
            and str(RUNNER) in p['args'][1:3]]


def job_workers(rows):
    result=[]
    for row in rows:
        args=row['args']
        if not args or Path(args[0]).name!='codex' or 'exec' not in args:continue
        try:target=Path(args[args.index('--output-last-message')+1]).resolve()
        except (ValueError,IndexError,OSError):continue
        if target.name!='result.json' or not target.is_relative_to((RUNTIME/'jobs').resolve()):continue
        job=target.parent
        # Native text mode writes progress to stderr; stdout may stay empty
        # until the final answer. Keep both old JSON and new native logs.
        logs=[p for p in job.glob('events-*.*') if p.suffix in {'.jsonl','.log'}]
        logs.extend(job.glob('errors-*.log'))
        modified=max((p.stat().st_mtime for p in logs),default=0)
        process_file=job/f'process-{row["pid"]}.json'
        process=read_json(process_file,{})
        evidence=verify_execution(job,requested_execution(RUNTIME,kind='review' if job.name.startswith(('review-','reference-review-')) else 'new'),process.get('stderr_log') or None)
        result.append({'pid':row['pid'],'ppid':row['ppid'],'job':job.name,
                       'kind':'review' if job.name.startswith(('review-','reference-review-')) else 'new',
                       'last_event_unix':int(modified),'execution':evidence})
    return result


def coordinator_locked():
    RUNTIME.mkdir(parents=True,exist_ok=True)
    with (RUNTIME/'coordinator.lock').open('a') as stream:
        try:fcntl.flock(stream,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError:return True
        fcntl.flock(stream,fcntl.LOCK_UN)
        return False


def fresh_tail():
    """Recheck remaining identities, companions and reference certificates."""
    from run_exhaustive import load_sources,needs_graphic_source
    from reference_queue import pending
    sources=load_sources(SCOPE)
    db=sqlite3.connect('file:'+str(HERE/'corpus.sqlite')+'?mode=ro',uri=True)
    try:
        states={(c,i):(sha,status,body) for c,i,sha,status,body in
                db.execute('SELECT code_id,source_id,source_sha256,status,proposed_xml FROM drafts')}
    finally:db.close()
    remaining=[];held=[]
    for articles in sources.values():
        for article in articles:
            state=states.get((article['code_id'],article['source_id']))
            if state and state[0]==article['source_sha256'] and (state[2] or state[1]=='retained_unchanged'):continue
            key={'code_id':article['code_id'],'source_id':article['source_id']}
            remaining.append(key)
            if needs_graphic_source(article):held.append(key)
    _,report=pending(sources)
    return len(remaining),held,report['pending_reference_reviews']


def action(status,live,workers,locked,previous,held,now,reference_pending=None,tail_paused=False):
    """Decide without mutating corpus, files or processes; easy to regression-test."""
    if live:
        if len(live)>1:return 'needs_attention','Multiple coordinators detected; no new process launched'
        return 'monitoring','Existing coordinator adopted without interruption'
    if locked:return 'waiting_for_lock','Coordinator lock is held; no duplicate launched'
    if workers:return 'orphan_workers','Worker evidence preserved; no concurrent replacement launched'
    failure=str(status.get('failure') or '')
    if status.get('status')=='blocked':
        if any(s in failure.lower() for s in ['authentication','usage limit','quota','sign-in']):
            # Existing errors conflate authentication and quota. Do not invent a
            # reset time or make an unbounded series of authenticated requests.
            return 'needs_attention','Authentication or usage limit requires resolution'
        return 'needs_attention','Validation blocked the coordinator; checks remain binding'
    if tail_paused and type(status.get('pending')) is int and status['pending']<=len(held):
        return 'review_tail_paused','Explicit review-tail limit is zero and current canonical inventory has no accessible new work'
    if status.get('pending')==0 and status.get('prior_drafts_awaiting_review')==0 and reference_pending==0:
        return 'awaiting_final_audit','Coverage is not a complete legal or reference audit'
    if status.get('pending') is not None and held and status['pending']<=len(held) and status.get('prior_drafts_awaiting_review')==0 and reference_pending==0:
        return 'needs_source_recovery','Only unresolved normative source companions remain'
    if int(previous.get('consecutive_unexpected_exits',0))>=5:
        return 'needs_attention','Repeated exits without progress require diagnosis'
    if now<int(previous.get('next_start_after_unix',0)):
        return 'restart_backoff','Waiting before retrying an interrupted coordinator'
    return 'restart','Coordinator disappeared before completion'


def save_state(state,previous):
    atomic(SUPERVISION/'status.json',state)
    signature=lambda s:(s.get('state'),s.get('reason'),tuple(s.get('coordinator_pids',[])),s.get('launch_pid'),
                        s.get('worker_configuration',{}).get('current_workers'),
                        bool(s.get('worker_configuration',{}).get('effective_six_verified_at_utc')))
    if signature(state)!=signature(previous):
        # Events contain identifiers and operational facts, no agent output.
        with (SUPERVISION/'events.jsonl').open('a') as stream:
            stream.write(json.dumps(state,ensure_ascii=False)+'\n')


def checkpoint_metadata(folder):
    folder.mkdir(parents=True)
    for name in ['status.json','queue.json','mixed-queue.json','held-graphic-sources.json',
                 'failed-jobs.json','coordinator.pid','publication-state.json']:
        p=RUNTIME/name
        if p.exists():shutil.copy2(p,folder/name)
    # Existing job folders are immutable across future resumptions. Preserve
    # their inventory here without repeatedly copying hundreds of megabytes.
    atomic(folder/'preserved-job-folders.json',sorted(p.name for p in (RUNTIME/'jobs').iterdir() if p.is_dir())
           if (RUNTIME/'jobs').exists() else [])


def launch(folder):
    plan=worker_settings(RUNTIME)
    mode='--recover-new-before-reviews' if plan.get('continuation_mode')=='recover_new_before_reviews' else '--interleave-review'
    command=[sys.executable,'-u',str(RUNNER),'--workers',str(plan['capacity']),mode,
             '--export-every','1000','--deploy-on-export','--publish-at-end']
    with (folder/'continuation.log').open('ab',buffering=0) as output:
        child=subprocess.Popen(command,cwd=HERE,stdin=subprocess.DEVNULL,
                               stdout=output,stderr=subprocess.STDOUT,start_new_session=True)
    atomic(folder/'launch.json',{'pid':child.pid,'command':command,'launched_at_unix':int(time.time())})
    return child.pid


def check():
    SUPERVISION.mkdir(parents=True,exist_ok=True)
    with (SUPERVISION/'supervisor.lock').open('a') as lock:
        try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError:return {'state':'already_checking'}
        now=int(time.time());previous=read_json(SUPERVISION/'status.json',{})
        if (SUPERVISION/'disabled').exists():
            state={'state':'disabled','checked_at_unix':now,'reason':'Explicit local pause marker exists'}
            save_state(state,previous);return state
        rows=processes();live=coordinator_processes(rows);workers=job_workers(rows)
        status=read_json(RUNTIME/'status.json',{})
        held=read_json(RUNTIME/'held-graphic-sources.json',[])
        counters={k:status.get(k) for k in ['source_records','drafted_articles','retained_unchanged',
                                            'pending','prior_drafts_reviewed','prior_drafts_awaiting_review']}
        signature=[counters.get(k) for k in ['drafted_articles','retained_unchanged','prior_drafts_reviewed']]
        failures=0 if signature!=previous.get('progress_signature') else int(previous.get('consecutive_unexpected_exits',0))
        previous=previous|{'consecutive_unexpected_exits':failures}
        locked=coordinator_locked();reference_pending=None
        # Only at the end of a stopped queue: inspect current canonical targets,
        # not a stale report left before the coordinator's disappearance.
        if not live and not workers and not locked and status.get('pending') is not None and status['pending']<=len(held) and status.get('prior_drafts_awaiting_review')==0:
            remaining,held,reference_pending=fresh_tail()
            status=status|{'pending':remaining}
        control=read_json(RUNTIME/'worker-limit.json',{})
        plan=worker_settings(RUNTIME)
        tail_paused=False;recovery_state=None
        if (not live and not workers and not locked and plan.get('continuation_mode')=='recover_new_before_reviews' and
                type(control.get('review_tail_limit')) is int and control['review_tail_limit']==0):
            import run_exhaustive
            from continuation_tail import fresh_recovery_state
            recovery_state=fresh_recovery_state(run_exhaustive)
            held=recovery_state['held']
            status=status|{'pending':recovery_state['open_accessible_new']+len(held)}
            phase=read_json(RUNTIME/'continuation-phase.json',{})
            run=read_json(RUNTIME/'coordinator-run.json',{})
            tail_paused=(recovery_state['open_accessible_new']==0 and phase.get('phase') in {'review_tail','review_tail_drained'} and
                         type(run.get('pid')) is int and phase.get('coordinator_pid')==run['pid'] and
                         phase.get('complete_inventory',{}).get('complete') is True and
                         phase['complete_inventory'].get('identity_sha256')==recovery_state['inventory'].get('identity_sha256'))
        decision,reason=action(status,live,workers,locked,previous,held,now,reference_pending,tail_paused)
        promotion=None
        if decision=='monitoring':
            def refresh_promotion_inputs():
                current_rows=processes()
                return (coordinator_processes(current_rows),job_workers(current_rows),
                        coordinator_locked(),read_json(RUNTIME/'status.json',{}))
            promotion=promote_if_ready(RUNTIME,refresh_promotion_inputs,now)
        state={'state':decision,'reason':reason,'checked_at_unix':now,
               'coordinator_pids':[p['pid'] for p in live],'active_agents':workers,
               'scope':SCOPE,'counters':counters,'progress_signature':signature,
               'consecutive_unexpected_exits':failures,
               'next_start_after_unix':previous.get('next_start_after_unix',0),
               'fresh_pending_reference_reviews':reference_pending,
               'fresh_recovery_state':recovery_state,
               'worker_configuration':worker_settings(RUNTIME),
               'exhaustive_rewriting_complete':False,'semantic_review_by_jurist':False}
        if promotion is not None:state['parallelism_evaluation']=promotion
        role_plan=state['worker_configuration'].get('role_limits')
        if role_plan is not None:
            from review_lane_observation import observe
            observation=observe(RUNTIME,live,workers,now)
            state['review_lane_observation']=observation
        if decision=='restart':
            stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
            folder=SUPERVISION/'restarts'/stamp
            failures+=1
            state.update(consecutive_unexpected_exits=failures,
                         next_start_after_unix=now+min(900,60*2**(failures-1)))
            try:
                checkpoint_metadata(folder)
                pid=launch(folder)
                state.update(state='starting',launch_pid=pid,launch_log=str(folder/'continuation.log'))
                # Persist identity before any optional secondary receipt fails.
                save_state(state,previous)
                atomic(HERE/'runtime/resume-latest.json',{'archive':str(folder),'state':'launched',
                       'pid':pid,'log':str(folder/'continuation.log'),'launched_at_unix':now,'supervised':True})
            except Exception as error:
                state.update(state='restart_failed' if not state.get('launch_pid') else 'starting',
                             reason='Restart metadata or launch failed; evidence retained',failure_type=type(error).__name__)
        save_state(state,previous)
        return state


def main():
    try:
        result=check()
        print(json.dumps({k:result.get(k) for k in ['state','reason','coordinator_pids','launch_pid']},ensure_ascii=False))
        return 0
    except Exception as error:
        # Do not print raw command output, process arguments or credentials.
        SUPERVISION.mkdir(parents=True,exist_ok=True)
        atomic(SUPERVISION/'check-error.json',{'checked_at_unix':int(time.time()),'type':type(error).__name__})
        print('Supervisor check failed; next launch-agent interval will retry.',file=sys.stderr)
        return 1


if __name__=='__main__':raise SystemExit(main())
