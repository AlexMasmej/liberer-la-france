"""One guarded handover. SIGTERM uses the existing drain handler, never a worker kill."""
from pathlib import Path
import argparse,datetime,fcntl,hashlib,json,os,shlex,shutil,signal,subprocess,sys,time

FOLDER=Path(__file__).resolve().parent
HERE=FOLDER.parents[1]
RUNTIME=HERE/'runtime/exhaustive'
SUPERVISION=HERE/'runtime/supervision'

def read(path):return json.loads(path.read_text())
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def atomic(path,value):
    temporary=path.with_name('.'+path.name+'.activation.tmp')
    temporary.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
    temporary.replace(path)

def inventory():
    rows=[]
    for line in subprocess.check_output(['/bin/ps','-axo','pid=,ppid=,command='],text=True,timeout=15).splitlines():
        values=line.strip().split(None,2)
        if len(values)!=3:continue
        try:args=shlex.split(values[2])
        except ValueError:continue
        pid,ppid=map(int,values[:2])
        if str(HERE/'run_exhaustive.py') in args[1:3]:rows.append({'kind':'coordinator','pid':pid,'ppid':ppid})
        elif args and Path(args[0]).name=='codex' and '--output-last-message' in args:
            target=Path(args[args.index('--output-last-message')+1])
            if target.is_relative_to(RUNTIME/'jobs'):
                rows.append({'kind':'worker','pid':pid,'ppid':ppid,'job':target.parent.name})
    return rows

def coordinator_unlocked():
    with (RUNTIME/'coordinator.lock').open('a') as stream:
        try:fcntl.flock(stream,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError:return False
        fcntl.flock(stream,fcntl.LOCK_UN);return True

def receipt(state,**fields):
    data={'state':state,'recorded_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),**fields}
    atomic(FOLDER/'activation-state.json',data)
    print(json.dumps(data,ensure_ascii=False),flush=True)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--apply',action='store_true');args=parser.parse_args()
    baseline=read(FOLDER/'baseline.json');checks=read(FOLDER/'checks.json')
    if checks.get('all_passed') is not True:raise ValueError('Staged checks are not complete')
    if checks.get('activation_sha256')!=sha(Path(__file__)):
        raise ValueError('Handover helper differs from the tested artifact')
    for name,expected in checks['implementation_sha256'].items():
        if sha(FOLDER/'implementation'/name)!=expected:raise ValueError('Validated implementation changed: '+name)
    changed=checks['activate_files']
    for name in changed:
        path=HERE/name
        if name in baseline['files']:
            if sha(path)!=baseline['files'][name]:raise ValueError('Active file changed since staging: '+name)
        elif path.exists():raise ValueError('New module already exists: '+name)
    rows=inventory();live=[x for x in rows if x['kind']=='coordinator'];old=baseline['coordinator_pid']
    if len(live)!=1 or live[0]['pid']!=old:raise ValueError('The original single coordinator is not the owner')
    if read(RUNTIME/'coordinator-run.json')['pid']!=old:raise ValueError('Coordinator identity receipt changed')
    if read(RUNTIME/'status.json').get('status')=='blocked':raise ValueError('Resolve existing blockage before handover')
    if not args.apply:
        receipt('dry_run_passed',old_pid=old,active_workers=[x for x in rows if x['kind']=='worker'],activate_files=changed)
        return
    with (SUPERVISION/'supervisor.lock').open('a') as supervisor_lock:
        fcntl.flock(supervisor_lock,fcntl.LOCK_EX)
        # This lock prevents automatic restart while the old PID drains. It
        # does not interfere with any drafting, validation or corpus lock.
        rows=inventory()
        if [x['pid'] for x in rows if x['kind']=='coordinator']!=[old]:raise ValueError('Coordinator changed before handover')
        atomic(FOLDER/'before/active-jobs-at-drain.json',rows)
        receipt('draining_current_jobs',old_pid=old,active_workers=[x for x in rows if x['kind']=='worker'])
        os.kill(old,signal.SIGTERM)
        started=time.monotonic();last=None
        while True:
            rows=inventory();pids=[x['pid'] for x in rows if x['kind']=='coordinator']
            if any(pid!=old for pid in pids):raise ValueError('Unexpected second coordinator; handover stopped')
            workers=[x for x in rows if x['kind']=='worker']
            state=(tuple(pids),tuple(x['pid'] for x in workers))
            if state!=last:
                receipt('draining_current_jobs',old_pid=old,active_workers=workers,elapsed_seconds=round(time.monotonic()-started));last=state
            if not pids and not workers and coordinator_unlocked():break
            if time.monotonic()-started>1800:raise TimeoutError('Old work remains active; no forced termination performed')
            time.sleep(2)
        exit_record=read(RUNTIME/'coordinator-exit.json')
        if exit_record.get('pid')!=old or exit_record.get('exit_code')!=0 or exit_record.get('stop_requested') is not True:
            raise ValueError('Old coordinator did not confirm a successful drained exit')
        status=read(RUNTIME/'status.json')
        if status.get('status')=='blocked' or status.get('failure'):raise ValueError('A validation or access blockage remains binding')
        shutil.copy2(RUNTIME/'status.json',FOLDER/'before/drained-status.json')
        shutil.copy2(RUNTIME/'coordinator-exit.json',FOLDER/'before/drained-exit.json')
        receipt('safe_handover_point',old_pid=old,old_exit=exit_record)
        correction=HERE/'runtime/css-impact-metadata-review-20261022/integrate_guarded.py'
        if correction.exists():
            with (FOLDER/'css-correction.log').open('w') as stream:
                result=subprocess.run([sys.executable,str(correction),'--apply'],cwd=HERE,stdout=stream,stderr=subprocess.STDOUT)
            atomic(FOLDER/'css-correction-result.json',{'returncode':result.returncode,'original_gates_remain_binding':True,'log':'css-correction.log'})
            # A stale guarded candidate is left pending; it cannot block an
            # independent scheduling improvement or be silently refreshed.
        for name in changed:
            path=HERE/name
            if name in baseline['files']:
                if sha(path)!=baseline['files'][name]:raise ValueError('Active code changed during draining: '+name)
            elif path.exists():raise ValueError('New module appeared during draining: '+name)
        for name in changed:shutil.copy2(FOLDER/'implementation'/name,HERE/name)
        atomic(FOLDER/'installed-code.json',{'sha256':{n:sha(HERE/n) for n in changed},'old_process_not_reloaded':True})
        policy=read(RUNTIME/'model-policy.json')
        if (policy.get('model'),policy.get('reasoning_effort'))!=('gpt-6-astra','medium'):
            raise ValueError('Execution policy changed')
        with (RUNTIME/'manual-agent-slots.lock').open('a') as manual_lock:
            fcntl.flock(manual_lock,fcntl.LOCK_EX)
            manual=read(RUNTIME/'manual-agent-slots.json')
            if manual:raise ValueError('Manual drafting reservations require explicit capacity reconciliation')
            plan=read(RUNTIME/'parallelism-plan.json')
            plan.setdefault('role_transition_history',[]).append({'previous_capacity':plan['capacity'],'previous_workers':plan['current_workers'],'coordinator_pid':old,'proof_folder':str(FOLDER)})
            plan.update(capacity=8,current_workers=8,target_workers=8,role_limits={'new':6,'review':2},
                        stage='six_drafting_plus_two_review_astra_medium',
                        additional_review_authorization={'approved':True,'new_confirmation_required':False,'instruction':'Accélérer aussi les secondes passes en parallèle, sans réduire les six places de rédaction ni les vérifications.'},
                        review_lane_proof_directory=str(FOLDER))
            atomic(RUNTIME/'parallelism-plan.json',plan)
            atomic(RUNTIME/'worker-limit.json',{'workers':8,'role_limits':{'new':6,'review':2}})
        command=[sys.executable,'-u',str(HERE/'run_exhaustive.py'),'--workers','8','--interleave-review','--export-every','1000','--deploy-on-export','--publish-at-end']
        with (FOLDER/'continuation.log').open('ab',buffering=0) as output:
            child=subprocess.Popen(command,cwd=HERE,stdin=subprocess.DEVNULL,stdout=output,stderr=subprocess.STDOUT,start_new_session=True)
        atomic(FOLDER/'launch.json',{'pid':child.pid,'command':command,'launched_at_unix':int(time.time())})
        atomic(HERE/'runtime/second-pass-parallelism-latest.json',{'folder':str(FOLDER),'state':'activated_awaiting_native_evidence','old_pid':old,'pid':child.pid,'capacity':8,'role_limits':{'new':6,'review':2},'activated':True})
        receipt('new_coordinator_launched',old_pid=old,pid=child.pid,capacity=8,role_limits={'new':6,'review':2})

if __name__=='__main__':
    try:main()
    except BaseException as error:
        receipt('handover_stopped',error_type=type(error).__name__,reason=str(error))
        raise
