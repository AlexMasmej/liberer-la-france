"""Read-only proof of actual new instructions, native responses and acceptance."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess,sys,time
sys.dont_write_bytecode=True
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1];RUN=OUT/'run'
sys.path.insert(0,str(ROOT))
import supervise_exhaustive as supervisor
from worker_execution import verify_execution
sys.path.insert(0,str(OUT))
from controller import BASELINE,CANDIDATE,CONTROL,digest,raw,read,encoded,durable,stream_sha

def observed():
    if not (RUN/'pause-released.json').exists():raise ValueError('Owned pause has not been released')
    before=read(RUN/'drain-context.json');release=read(RUN/'pause-released.json');installed=read(RUN/'installed.json')
    rows=supervisor.processes();live=supervisor.coordinator_processes(rows)
    if len(live)!=1 or live[0]['pid']==before['pid']:raise ValueError('Exactly one new coordinator required')
    pid=live[0]['pid'];run=read(ROOT/'runtime/exhaustive/coordinator-run.json')
    resume=read(ROOT/'runtime/resume-latest.json');launch=read(Path(resume['archive'])/'launch.json')
    if run['pid']!=pid or resume['pid']!=pid or launch['pid']!=pid or launch['launched_at_unix']+1<=release['at_unix']:raise ValueError('New process not tied to registered supervisor launch')
    launches=[read(p) for p in (ROOT/'runtime/supervision/restarts').glob('*/launch.json') if read(p)['launched_at_unix']+1>release['at_unix']]
    if len(launches)!=1 or launches[0]['pid']!=pid:raise ValueError('More than one supervised continuation since release')
    if raw(ROOT/'runtime/exhaustive/worker-limit.json')!=__import__('base64').b64decode(before['control_before_b64']):raise ValueError('Restored control changed')
    if (ROOT/'runtime/supervision/disabled').exists():raise ValueError('Unexpected supervision pause')
    original=read(OUT/'baseline-pins.json')
    reviewed=read(OUT/'concurrent-presentation-change-review-v3.json')
    if original['build_compact_sites.py']!=reviewed['original_pinned_sha256'] or not reviewed['reverse_substitution_byte_identical'] or reviewed['exact_occurrences']!=3:raise ValueError('Concurrent presentation change not reviewed')
    pins=read(OUT/'resumption-observation-pins-v4.json')
    grammar=read(OUT/'concurrent-site-summaries-grammar-review.json')
    if original['site-summaries.json']!=grammar['baseline_sha256'] or not grammar['whole_json_exactly_reconstructed_by_three_grammar_edits']:raise ValueError('Unreviewed grammar change')
    if {n for n in original if original[n]!=pins[n]}!={'build_compact_sites.py','site-summaries.json'} or pins['build_compact_sites.py']!=reviewed['current_sha256'] or pins['site-summaries.json']!=grammar['current_sha256']:raise ValueError('Unreviewed pin update')
    pins=pins|{'run_exhaustive.py':CANDIDATE}
    for n,h in pins.items():
        if digest(raw(ROOT/n))!=h:raise ValueError('Current installed code/policy pin changed: '+n)
    old=ROOT/'runtime/review-transfer-adoption-20261023T1426Z'
    if digest(raw(old/'manifest.json'))!='1246653fc7f94585affe9d6a40d52c8b33d92bd810db6c5839447bda07b0e13d':raise ValueError('Interpreter origin manifest changed')
    origin=read(old/'adoption-verified.json')['interpreter_binding']
    requested=Path(launch['command'][0]).resolve();image=Path(live[0]['args'][0]).resolve()
    if requested!=Path(origin['requested_launcher']).resolve() or image!=Path(origin['observed_loaded_image']).resolve() or live[0]['args'][1:]!=launch['command'][1:]:raise ValueError('Physical interpreter argument binding differs')
    if stream_sha(requested)!=origin['launcher_sha256'] or stream_sha(image)!=origin['image_sha256']:raise ValueError('Physical interpreter hash differs')
    lsof=subprocess.run(['/usr/sbin/lsof','-p',str(pid)],capture_output=True,text=True,timeout=20)
    if lsof.returncode or str(image) not in lsof.stdout:raise ValueError('Loaded image not confirmed')
    birth_text=subprocess.check_output(['/bin/ps','-p',str(pid),'-o','lstart='],text=True,timeout=15).strip()
    birth=datetime.strptime(birth_text,'%a %b %d %H:%M:%S %Y').replace(tzinfo=__import__('zoneinfo').ZoneInfo('America/Los_Angeles')).astimezone(timezone.utc)
    if not birth.timestamp()<=run['started_at_unix']<=birth.timestamp()+15:raise ValueError('New birth/run timestamps differ')
    phase=read(ROOT/'runtime/exhaustive/continuation-phase.json')
    if phase['coordinator_pid']!=pid or phase['phase']!='review_tail' or phase['effective_limits']!={'workers':8,'role_limits':{'new':0,'review':8}}:raise ValueError('New guarded review-tail not active')
    native=[x for x in supervisor.job_workers(rows) if x['ppid']==pid]
    responders=[]
    marker='SECONDE PASSE — PRIORITÉ HUMAINE DU23OCTOBRE2026'
    for worker in native:
        e=worker['execution']
        if not e['verified']:continue
        if e['model']!='gpt-6-astra' or e['reasoning_effort']!='medium':raise ValueError('Native model/effort differs')
        log=Path(e['source_log']);b=raw(log)
        if marker not in b.decode(errors='replace'):raise ValueError('Native session did not receive the new priority')
        responders.append(dict(pid=worker['pid'],job=worker['job'],execution=e,new_priority_present_in_native_input=True,log_prefix_bytes=len(b),log_prefix_sha256=digest(b)))
    if len({x['execution']['session_id'] for x in responders})!=len(responders):raise ValueError('Native sessions not distinct')
    proof=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),new_coordinator_pid=pid,previous_coordinator_pid=before['pid'],birth_utc=birth.isoformat(),run=run,registered_supervisor_launch=launch,physical_interpreter=dict(requested_launcher=str(requested),loaded_image=str(image),launcher_sha256=stream_sha(requested),image_sha256=stream_sha(image),lsof_sha256=digest(lsof.stdout.encode()),arguments_identical=True),native_workers=len(native),native_responding_distinct=len(responders),responders=responders,installed_runner_sha256=CANDIDATE,all77pins_match=True,legal_policy_coordinations_or_global_model_changed=False,concurrent_presentation_and_grammar_reviews=[str(OUT/'concurrent-presentation-change-review-v3.json'),str(OUT/'concurrent-site-summaries-grammar-review.json')],new_priority_applies_to_responding_sessions=True,throughput_gain_claimed=False)
    return pid,pins,proof

if __name__=='__main__':
    pid,pins,proof=observed();name='resumption-observation-'+str(time.time_ns())+'.json';durable(RUN/name,encoded(proof))
    prior=[]
    for p in RUN.glob('resumption-observation-*.json'):
        previous=read(p)
        if previous['new_coordinator_pid']==pid:prior.extend(previous['responders'])
    sessions={x['execution']['session_id']:x for x in prior}
    if len(sys.argv)>1 and sys.argv[1]=='accepted':
        from accepted_work import accepted_review
        accepted=accepted_review(ROOT,pid,pins,time.time())
        data=raw(ROOT/'runtime/radical-review-20261019.json');manifest=json.loads(data);mapped={(x['code_id'],x['source_id']):x for x in manifest['prior_articles']}
        if not all(mapped[x['code_id'],x['source_id']]['review_status']=='completed' for x in accepted['rows']):raise ValueError('Accepted manifest rows not completed')
        if raw(ROOT/'runtime/radical-review-20261019.json')!=data:raise ValueError('Completed manifest changed during verification')
        e=accepted['native_execution'];log=Path(e['source_log'])
        if 'SECONDE PASSE — PRIORITÉ HUMAINE DU23OCTOBRE2026' not in raw(log).decode(errors='replace'):raise ValueError('Accepted review did not receive coherence priority')
        accepted.update(completed_manifest_rows=len(accepted['rows']),manifest_sha256=digest(data),new_priority_present_in_native_input=True)
        durable(RUN/('accepted-verification-'+str(time.time_ns())+'.json'),encoded(accepted))
        sessions[e['session_id']]=dict(job=accepted['job'],execution=e,new_priority_present_in_native_input=True)
        proof['accepted_review']=accepted
    proof['distinct_new_native_responses_observed_across_dated_captures']=len(sessions)
    proof['eight_distinct_new_responses_attested']=len(sessions)>=8
    durable(RUN/('resumption-proof-'+str(time.time_ns())+'.json'),encoded(proof))
    print(json.dumps({k:v for k,v in proof.items() if k in ['checked_at_utc','new_coordinator_pid','native_workers','native_responding_distinct','distinct_new_native_responses_observed_across_dated_captures','eight_distinct_new_responses_attested']}|dict(accepted_articles=proof.get('accepted_review',{}).get('articles')),ensure_ascii=False))
