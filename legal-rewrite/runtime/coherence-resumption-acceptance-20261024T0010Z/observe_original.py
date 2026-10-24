"""Read-only continuation evidence attached to the actual stale-policy exit."""
from pathlib import Path
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import hashlib,json,os,shutil,sqlite3,subprocess,sys,time
sys.dont_write_bytecode=True
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1];R=ROOT/'runtime'
WORK=R/'coherence-rollout-20261023T2042Z'
sys.path.insert(0,str(ROOT));sys.path.insert(0,str(WORK))
import supervise_exhaustive as supervisor
from worker_execution import verify_execution
from ingest import source_notes

def sha(b):return hashlib.sha256(b).hexdigest()
def read(p):return json.loads(p.read_bytes())
def fsha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()
def put(p,o):
    with p.open('x') as f:json.dump(o,f,ensure_ascii=False,indent=2);f.write('\n')

def validate_chain(old_pid,pid,receipt,last_alive,launches,release,run,birth):
    if pid==old_pid or run['pid']!=pid:raise ValueError('Fresh current PID required')
    if receipt['pid']!=old_pid or receipt['exit_code']!=0 or receipt['stop_requested'] is not True:
        raise ValueError('Actual stale-policy natural exit receipt required')
    ordered=sorted(launches,key=lambda a:a['launched_at_unix'])
    if len(ordered)!=2 or [a['pid'] for a in ordered]!=[old_pid,pid]:
        raise ValueError('Exact two-launch history required; no arbitrary counter override')
    if not release<ordered[0]['launched_at_unix']<=last_alive<=receipt['ended_at_unix']<ordered[1]['launched_at_unix']:
        raise ValueError('Exit not attached to actual preceding live observation and next launch')
    if not ordered[1]['launched_at_unix']<=birth<=run['started_at_unix']<=birth+15:
        raise ValueError('OS birth and run are inconsistent with the actual next launch')

def observe(accept=False):
    rows=supervisor.processes();live=supervisor.coordinator_processes(rows)
    if len(live)!=1:raise ValueError('Exactly one real coordinator required')
    pid=live[0]['pid']
    if pid!=58195:raise ValueError('Unexpected new coordinator: re-evaluate this chain')
    run=read(R/'exhaustive/coordinator-run.json');resume=read(R/'resume-latest.json')
    launch=read(Path(resume['archive'])/'launch.json');receipt=read(R/'exhaustive/coordinator-exit.json')
    if resume['pid']!=pid or launch['pid']!=pid:raise ValueError('Registered supervisor binding differs')
    last=read(R/'coherence-policy-refusal-final-20261023T2222Z/native-and-process.json')
    if last['new_coordinator_pid']!=41583:raise ValueError('Previous live origin differs')
    last_alive=datetime.fromisoformat(last['checked_at_utc']).timestamp()
    release=read(WORK/'run/pause-released.json')['at_unix']
    launches=[read(p) for p in (R/'supervision/restarts').glob('*/launch.json') if read(p)['launched_at_unix']>release]
    birth_text=subprocess.check_output(['/bin/ps','-p',str(pid),'-o','lstart='],text=True,timeout=15).strip()
    birth=datetime.strptime(birth_text,'%a %b %d %H:%M:%S %Y').replace(tzinfo=ZoneInfo('America/Los_Angeles')).astimezone(timezone.utc)
    validate_chain(41583,pid,receipt,last_alive,launches,release,run,birth.timestamp())
    if any(p['pid']==41583 or p['ppid']==41583 for p in rows):raise ValueError('Old coordinator/children still exist')
    old_observation=read(R/'coherence-response-confirmation-20261023T220040Z/eight-native-responses.json')
    old_names={x['job'] for x in old_observation['responders']}
    groups=set()
    for name in old_names:
        for p in (R/'exhaustive/jobs'/name).glob('process-*.json'):groups.add(read(p)['process_group'])
    pg=subprocess.check_output(['/bin/ps','-axo','pid=,ppid=,pgid='],text=True,timeout=15)
    group_survivors=[line for line in pg.splitlines() if len(line.split())==3 and int(line.split()[2]) in groups]
    if group_survivors:raise ValueError('Known old native process group still present')
    exporters=[p for p in rows if any(str(ROOT/n) in p['args'] for n in ['publish_snapshot.py','build_reader.py','build_compact_sites.py'])]
    if exporters:raise ValueError('Project exporters still active: no exit finality claimed')
    if (R/'supervision/disabled').exists():raise ValueError('Unexpected supervision pause')
    expected={'workers':8,'role_limits':{'new':6,'review':0},'review_tail_limit':8}
    if read(R/'exhaustive/worker-limit.json')!=expected:raise ValueError('Worker controls changed')
    pins=read(WORK/'resumption-observation-pins-v4.json')|{'run_exhaustive.py':'d826aac7dbd43e5e07538d07a9bbf770bbb732842352424456ffd19067898802'}
    for name,h in pins.items():
        if fsha(ROOT/name)!=h:raise ValueError('Current pin differs: '+name)
    origin_folder=R/'review-transfer-adoption-20261023T1426Z'
    if fsha(origin_folder/'manifest.json')!='1246653fc7f94585affe9d6a40d52c8b33d92bd810db6c5839447bda07b0e13d':raise ValueError('Interpreter origin manifest changed')
    origin=read(origin_folder/'adoption-verified.json')['interpreter_binding']
    requested=Path(launch['command'][0]).resolve();image=Path(live[0]['args'][0]).resolve()
    if requested!=Path(origin['requested_launcher']).resolve() or image!=Path(origin['observed_loaded_image']).resolve() or live[0]['args'][1:]!=launch['command'][1:]:
        raise ValueError('Physical launch arguments differ')
    if fsha(requested)!=origin['launcher_sha256'] or fsha(image)!=origin['image_sha256']:raise ValueError('Physical interpreter hashes differ')
    ls=subprocess.run(['/usr/sbin/lsof','-p',str(pid)],capture_output=True,text=True,timeout=20)
    if ls.returncode or str(image) not in ls.stdout:raise ValueError('Loaded image not confirmed')
    registered=subprocess.run(['/bin/launchctl','print',f'gui/{os.getuid()}/com.libererfrance.exhaustive-rewrite'],capture_output=True,text=True,timeout=20)
    if registered.returncode:raise ValueError('LaunchAgent not registered')
    phase=read(R/'exhaustive/continuation-phase.json')
    ready=phase.get('coordinator_pid')==pid and phase.get('phase')=='review_tail' and phase.get('effective_limits')=={'workers':8,'role_limits':{'new':0,'review':8}}
    natives=[x for x in supervisor.job_workers(rows) if x['ppid']==pid]
    responders=[]
    for item in natives:
        d=R/'exhaustive/jobs'/item['job'];e=item['execution']
        if not e.get('verified'):continue
        if e['model']!='gpt-6-astra' or e['reasoning_effort']!='medium':raise ValueError('Native model/effort differs')
        if read(d/'policy.json')!=read(ROOT/'site-summaries.json') or read(d/'coordination.json')!=read(ROOT/'policy-coordinations.json'):
            raise ValueError('Fresh native job frozen policy is stale')
        b=Path(e['source_log']).read_bytes()
        if 'SECONDE PASSE — PRIORITÉ HUMAINE DU23OCTOBRE2026' not in b.decode(errors='replace'):raise ValueError('New priority absent')
        responders.append(dict(job=item['job'],pid=item['pid'],execution=e,current_frozen_policies_match=True,priority_present=True,log_prefix_bytes=len(b),log_prefix_sha256=sha(b)))
    if len({x['execution']['session_id'] for x in responders})!=len(responders):raise ValueError('Native sessions not distinct')
    metrics_b=(R/'exhaustive/job-metrics.jsonl').read_bytes();metrics=[json.loads(x) for x in metrics_b.splitlines()]
    old=[m for m in metrics if m.get('coordinator_pid')==41583]
    if len(old)!=8 or {m['job'] for m in old}!=old_names or any(m['outcome']!='stale_policy' for m in old):raise ValueError('Old queue terminal partition is not exact')
    work_b=(R/'radical-review-20261019.json').read_bytes()
    work={(a['code_id'],a['source_id']):a for a in json.loads(work_b)['prior_articles']}
    db=sqlite3.connect((ROOT/'corpus.sqlite').as_uri()+'?mode=ro',uri=True,timeout=15);db.execute('BEGIN')
    preserved=[]
    try:
        for metric in old:
            sources=read(R/'exhaustive/jobs'/metric['job']/'source.json')
            if len(sources)!=metric['articles']:raise ValueError('Old metric assignment mismatch')
            for source in sources:
                key=source['code_id'],source['source_id'];prior=source['previous_draft']
                if db.execute('SELECT source_sha256,content_xml,valid_from,valid_until FROM articles WHERE code_id=? AND id=?',key).fetchone()!=(source['source_sha256'],source['source_xml'],source['valid_from'],source['valid_until']):raise ValueError('Old rejected source guard changed')
                if source_notes(db,*key)!=source['source_notes_xml']:raise ValueError('Old rejected NOTA changed')
                values=tuple(prior[k] for k in ['source_sha256','status','proposed_xml','reason','review_notes'])
                if db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?',key).fetchone()!=values:raise ValueError('Rejected beforeimage changed; requalify actual current disposition')
                if work[key]['review_status']!='pending':raise ValueError('Rejected article no longer pending: verify fresh recovery')
                preserved.append(dict(code_id=key[0],source_id=key[1],source_NOTA_versions_five_field_beforeimage_and_pending_match=True))
    finally:db.close()
    if (R/'radical-review-20261019.json').read_bytes()!=work_b:raise ValueError('Worklist changed during old-source proof')
    current=[m for m in metrics if m.get('coordinator_pid')==pid]
    result=dict(at_utc=datetime.now(timezone.utc).isoformat(),state='NEW_SUPERVISED_STARTUP' if not ready else 'NEW_GUARDED_PHASE_NATIVE_AND_ACCEPTANCE_TO_VERIFY',
        previous_pid=41583,new_pid=pid,old_exit_receipt=receipt,last_old_real_live_observation=last['checked_at_utc'],
        exact_two_launch_history=sorted(launches,key=lambda a:a['launched_at_unix']),old_native_groups_absent=sorted(groups),old_exporters_absent=True,
        current_process=live[0],birth_utc=birth.isoformat(),run=run,physical_interpreter_hashes_verified=True,
        lsof_sha256=sha(ls.stdout.encode()),registered_launchagent=True,all77_current_pins_match=True,
        guarded_phase_matches_current_pid=ready,observed_phase_marker=phase,native_process_count=len(natives),responders=responders,
        actual_current_distinct_native_responses=len(responders),old_refused_jobs=old,old_refused_articles=sum(m['articles'] for m in old),
        old_rejected_beforeimages_preserved=preserved,
        current_metrics=current,current_successful_articles=sum(m['articles'] for m in current if m['outcome'] in ['accepted','reviewed']),
        free_gib=shutil.disk_usage(ROOT).free/2**30,no_manual_signal_pause_launch_code_policy_or_admission_change=True,
        no_old_response_replay=True,accepted_review_verification_complete=False,global_legal_completion=False)
    if accept:
        if not ready:raise ValueError('Fresh guarded phase required before acceptance proof')
        from accepted_work import accepted_review
        accepted=accepted_review(ROOT,pid,pins,time.time())
        d=R/'exhaustive/jobs'/accepted['job']
        if read(d/'policy.json')!=read(ROOT/'site-summaries.json') or read(d/'coordination.json')!=read(ROOT/'policy-coordinations.json'):
            raise ValueError('Accepted frozen policy changed')
        log=Path(accepted['native_execution']['source_log']).read_bytes()
        if 'SECONDE PASSE — PRIORITÉ HUMAINE DU23OCTOBRE2026' not in log.decode(errors='replace'):raise ValueError('Accepted native priority absent')
        work_b=(R/'radical-review-20261019.json').read_bytes();work={(x['code_id'],x['source_id']):x for x in json.loads(work_b)['prior_articles']}
        if not all(work[a['code_id'],a['source_id']]['review_status']=='completed' for a in accepted['rows']):raise ValueError('Accepted entries not completed')
        if (R/'radical-review-20261019.json').read_bytes()!=work_b:raise ValueError('Worklist changed during proof')
        result.update(accepted_review=accepted,accepted_review_verification_complete=True)
    folder=OUT/'observations';folder.mkdir(exist_ok=True)
    put(folder/('observation-'+str(time.time_ns())+'.json'),result)
    return result

if __name__=='__main__':
    result=observe(accept=len(sys.argv)>1 and sys.argv[1]=='accepted')
    print(json.dumps({k:v for k,v in result.items() if k in ['at_utc','state','new_pid','birth_utc','guarded_phase_matches_current_pid','native_process_count','actual_current_distinct_native_responses','old_refused_articles','current_successful_articles','accepted_review_verification_complete']},ensure_ascii=False))
