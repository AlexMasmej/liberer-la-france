"""Owned natural drain and one prompt-only installation. Never launches/signals."""
from contextlib import ExitStack,contextmanager
from datetime import datetime,timezone
from pathlib import Path
from zoneinfo import ZoneInfo
import ast,base64,fcntl,hashlib,json,os,stat,subprocess,sys,tempfile,time,uuid
sys.dont_write_bytecode=True
EVIDENCE=Path(__file__).resolve().parent
ROOT=EVIDENCE.parents[1]
PREP=ROOT/'runtime/coherence-prompt-preparation-20261023T1956Z'
BASELINE='91e898776c7619b89461928010c02f8cd49141745473dcdefbdfd5f6f65c3e40'
CANDIDATE='d826aac7dbd43e5e07538d07a9bbf770bbb732842352424456ffd19067898802'
CONTROL={'workers':8,'role_limits':{'new':6,'review':0},'review_tail_limit':8}
LOCKS=['runtime/supervision/supervisor.lock','runtime/exhaustive/coordinator.lock','draft-writer.lock','runtime/exhaustive/manual-agent-slots.lock']

def digest(b):return hashlib.sha256(b).hexdigest()
def encoded(d):return (json.dumps(d,ensure_ascii=False,indent=2)+'\n').encode()
def raw(p):
    p=Path(p)
    if p.is_symlink() or not p.is_file() or not stat.S_ISREG(p.stat().st_mode):raise ValueError('Regular file required: '+str(p))
    return p.read_bytes()
def read(p):return json.loads(raw(p))
def sync(p):
    fd=os.open(p,os.O_RDONLY)
    try:os.fsync(fd)
    finally:os.close(fd)
def durable(p,b):
    with Path(p).open('xb') as f:f.write(b);f.flush();os.fsync(f.fileno())
    sync(Path(p).parent)
def stream_sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()
@contextmanager
def hold_locks(root,names):
    with ExitStack() as s:
        for n in names:
            p=Path(root)/n
            if p.is_symlink() or not p.is_file():raise ValueError('Unknown lock')
            f=s.enter_context(p.open('r+'));fcntl.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB)
        yield
def compare(p,h):
    if digest(raw(p))!=h:raise ValueError('Intervening file: '+str(p))
def replace_exact(p,before,after):
    p=Path(p)
    if raw(p)!=before:raise ValueError('Compare-and-swap beforeimage differs')
    with tempfile.NamedTemporaryFile(dir=p.parent,prefix='.'+p.name+'.coherence-',delete=False) as f:
        temp=Path(f.name);f.write(after);f.flush();os.fsync(f.fileno())
    os.chmod(temp,stat.S_IMODE(p.stat().st_mode))
    if raw(p)!=before:
        temp.unlink();raise ValueError('Intervening write before replace')
    os.replace(temp,p);sync(p.parent)
    if raw(p)!=after:raise ValueError('Installed bytes differ')
def check_pause(p,expected,owner):
    b=raw(p)
    if b!=expected or json.loads(b).get('owner')!=owner:raise ValueError('Pause owner/bytes differ')
    return b
def prompt_only(before,after):
    a=ast.parse(before);b=ast.parse(after)
    old=[x for x in ast.walk(a) if isinstance(x,ast.Constant) and isinstance(x.value,str) and x.value.startswith('\nSECONDE PASSE :')]
    new=[x for x in ast.walk(b) if isinstance(x,ast.Constant) and isinstance(x.value,str) and x.value.startswith('\nSECONDE PASSE — PRIORITÉ HUMAINE')]
    if len(old)!=1 or len(new)!=1:raise ValueError('Exactly one review literal required')
    new[0].value=old[0].value
    if ast.dump(a,include_attributes=False)!=ast.dump(b,include_attributes=False):raise ValueError('Change beyond one prompt literal')
    compile(after,'review-prompt-candidate','exec')
def bind_exit(run,receipt,last_alive,birth,known_absent):
    if known_absent is not True:raise ValueError('OS inventory unknown or not drained')
    if run['pid']!=receipt['pid'] or receipt['pid']!=last_alive['pid']:raise ValueError('Exit PID mismatch')
    if receipt.get('exit_code')!=0 or receipt.get('exit_type') is not None or receipt.get('stop_requested') is not False:raise ValueError('Natural successful exit required')
    if not birth<=run['started_at_unix']<=birth+15:raise ValueError('Run/birth differ')
    # The exit receipt records whole seconds; preserve its one-second precision.
    if not run['started_at_unix']<=last_alive['observed_at_unix']<receipt['ended_at_unix']+1:raise ValueError('Exit is not attached to last live process')
def partition(plan,admission,unattempted,metrics,pending,resolve_sources):
    pid=plan['coordinator_pid']
    if admission['coordinator_pid']!=pid or unattempted['coordinator_pid']!=pid:raise ValueError('Queue belongs to another PID')
    if admission['action']!='review_admissions_paused' or admission['reserved_or_running_by_kind']!={'new':0,'review':0}:raise ValueError('Queue has not drained')
    terminal=[m for m in metrics if m.get('coordinator_pid')==pid]
    keys=lambda x:(x['kind'],x['slug'],x['index'])
    terminals={keys(x):x for x in terminal};deferred={keys(x):x for x in unattempted['jobs']}
    if len(terminals)!=len(terminal) or len(deferred)!=len(unattempted['jobs']) or set(terminals)&set(deferred):raise ValueError('Duplicate/overlapping queue jobs')
    if any(x['kind']!='review' or x['outcome'] not in {'reviewed','deferred'} for x in terminal):raise ValueError('Unknown current terminal outcome')
    if any(x['kind']!='review' or x['reason']!='role_admissions_paused' or x['attempted'] is not False or x['accepted'] is not False for x in unattempted['jobs']):raise ValueError('Unknown unattempted disposition')
    if plan['scheduled_by_kind']!={'new':0,'review':len(terminal)+len(deferred)}:raise ValueError('Queue count mismatch')
    if admission['admitted_by_kind']!={'new':0,'review':len(terminal)} or admission['deferred_by_kind']!={'new':0,'review':len(deferred)}:raise ValueError('Admission count mismatch')
    failed=set();successful=set();queued=set()
    for m in terminal:
        assigned=resolve_sources(m)
        dest=successful if m['outcome']=='reviewed' else failed
        if dest&assigned:raise ValueError('Overlapping current terminal identities')
        dest.update(assigned)
    for m in unattempted['jobs']:
        assigned=resolve_sources(m)
        if queued&assigned:raise ValueError('Overlapping unattempted identities')
        queued.update(assigned)
    if successful&failed or successful&queued or failed&queued:raise ValueError('Overlapping identity dispositions')
    if queued|failed!=pending or successful&pending:raise ValueError('Persistent pending identities do not match failed and unattempted queue')
    return dict(terminal_jobs=len(terminal),unattempted_jobs=len(deferred),successful_identities=len(successful),failed_identities=len(failed),unattempted_identities=len(queued),pending_identities=len(pending),unknown_jobs=0)

class Production:
    def __init__(self):
        if ROOT.name!='legal-rewrite' or ROOT.resolve()!=ROOT:raise ValueError('Unexpected production root')
        self.out=EVIDENCE/'run';self.out.mkdir(exist_ok=True)
        self.pins=read(EVIDENCE/'baseline-pins.json')
        sys.path.insert(0,str(ROOT))
        import supervise_exhaustive
        self.supervisor=supervise_exhaustive
    def record(self,n,d):durable(self.out/n,encoded(d))
    def fresh_record(self,n,d):
        p=Path(n);index=0;name=n
        while (self.out/name).exists():
            index+=1;name=p.stem+'-'+str(index)+p.suffix
        self.record(name,d);return name
    def pins_match(self,installed=False):
        for n,h in self.pins.items():compare(ROOT/n,CANDIDATE if installed and n=='run_exhaustive.py' else h)
    def sealed(self):
        m=read(EVIDENCE/'preparation-manifest.json')
        for n,e in m['files'].items():
            b=raw(EVIDENCE/n)
            if digest(b)!=e['sha256'] or len(b)!=e['bytes']:raise ValueError('Preparation changed')
        tests=read(EVIDENCE/'tests.json')
        if tests['success'] is not True or tests['production_database_or_model_used'] is not False:raise ValueError('Tests required')
        compare(PREP/'artifact-manifest.json','1f5c1180bb7d9df01a89f51a8d2a2dc4f4cfe0a1af6fe3384b41b34ce9876ef2')
        compare(PREP/'run_exhaustive.py',CANDIDATE)
        prompt_only(raw(PREP/'baseline-run_exhaustive.py').decode(),raw(PREP/'run_exhaustive.py').decode())
    @contextmanager
    def locks(self,all_locks=False):
        with hold_locks(ROOT,LOCKS if all_locks else [LOCKS[0],LOCKS[3]]):yield
    def inventory(self):
        rows=self.supervisor.processes()
        live=self.supervisor.coordinator_processes(rows);workers=self.supervisor.job_workers(rows)
        exporters=[x for x in rows if any(str(ROOT/n) in x['args'][1:3] for n in ['publish_snapshot.py','build_reader.py','build_downloads.py','build_compact_sites.py','prepare_existing_sites.py'])]
        descendants=set(p['pid'] for p in live)
        while True:
            more={p['pid'] for p in rows if p['ppid'] in descendants}-descendants
            if not more:break
            descendants.update(more)
        descendants-={p['pid'] for p in live}
        return dict(known=True,observed_at_unix=time.time(),coordinators=live,workers=workers,exporters=exporters,all_pids={p['pid'] for p in rows},descendant_pids=sorted(descendants))
    def birth(self,pid):
        text=subprocess.check_output(['/bin/ps','-p',str(pid),'-o','lstart='],text=True,timeout=15).strip()
        if not text:raise ValueError('Birth unknown')
        return datetime.strptime(text,'%a %b %d %H:%M:%S %Y').replace(tzinfo=ZoneInfo('America/Los_Angeles')).astimezone(timezone.utc).timestamp()
    def capture_alive(self,context):
        inv=self.inventory();live=inv['coordinators']
        if len(live)==1 and live[0]['pid']==context['pid']:
            if self.birth(context['pid'])!=context['birth_unix']:raise ValueError('PID birth changed')
            observed=dict(pid=context['pid'],birth_unix=context['birth_unix'],observed_at_unix=inv['observed_at_unix'],native_workers=len(inv['workers']),descendant_pids=inv['descendant_pids'])
            with (self.out/'alive-observations.jsonl').open('ab') as f:f.write((json.dumps(observed)+'\n').encode());f.flush();os.fsync(f.fileno())
        elif live:raise ValueError('Unexpected coordinator')
        return inv
    def context(self):return read(self.out/'drain-context.json')
    def pause(self,c):return base64.b64decode(c['pause_b64'])
    def poll(self):
        c=self.context();inv=self.capture_alive(c)
        result=dict(observed_at_unix=inv['observed_at_unix'],known_inventory=True,coordinator_pids=[x['pid'] for x in inv['coordinators']],native_workers=len(inv['workers']),exporters=len(inv['exporters']),admission=read(ROOT/'runtime/exhaustive/admission-status.json'),exit_receipt=read(ROOT/'runtime/exhaustive/coordinator-exit.json'))
        path=self.out/('poll-'+str(time.time_ns())+'.json');durable(path,encoded(result))
        return {k:result[k] for k in ['coordinator_pids','native_workers','exporters']}|dict(admission_action=result['admission']['action'],exit_pid=result['exit_receipt']['pid'])
    def drain(self):
        self.sealed();self.pins_match()
        if (self.out/'drain-context.json').exists():raise ValueError('Drain already journalled; inspect/poll rather than replay')
        # Coverage is read before taking admission locks and is not a mirror certificate.
        sys.path.insert(0,str(EVIDENCE))
        from registration_reconciliation import first_pass_inventory
        proof=first_pass_inventory(ROOT,self.pins)
        if not proof['all_accessible_first_passes_registered'] or len(proof['documentary_holds'])!=3:raise ValueError('Accessible first passes or unknown documentary holds')
        self.record('first-pass-inventory.json',proof)
        with self.locks():
            self.pins_match();inv=self.inventory();run=read(ROOT/'runtime/exhaustive/coordinator-run.json')
            if len(inv['coordinators'])!=1 or inv['coordinators'][0]['pid']!=run['pid'] or run['pid']!=78943:raise ValueError('Fresh unique coordinator required')
            phase=read(ROOT/'runtime/exhaustive/continuation-phase.json')
            if phase['coordinator_pid']!=run['pid'] or phase['phase']!='review_tail':raise ValueError('Review-tail phase differs')
            if read(ROOT/'runtime/exhaustive/manual-agent-slots.json')!=[]:raise ValueError('Manual reservations present/unknown')
            controlpath=ROOT/'runtime/exhaustive/worker-limit.json';before=raw(controlpath)
            if json.loads(before)!=CONTROL:raise ValueError('Current control differs')
            paused=CONTROL|{'review_tail_limit':0};after=encoded(paused)
            pausepath=ROOT/'runtime/supervision/disabled'
            if pausepath.exists() or pausepath.is_symlink():raise ValueError('Preexisting pause; never overwrite')
            launch=subprocess.run(['launchctl','print',f'gui/{os.getuid()}/com.libererfrance.exhaustive-rewrite'],capture_output=True,text=True,timeout=15)
            if launch.returncode:raise ValueError('LaunchAgent not registered')
            owner='coherence-rollout-'+str(uuid.uuid4());birth=self.birth(run['pid'])
            pause=encoded(dict(owner=owner,pid=run['pid'],created_at_unix=time.time(),reason='Natural drain before reviewed prompt-only coherence update; no active job interrupted.'))
            c=dict(owner=owner,pid=run['pid'],birth_unix=birth,run=run,control_before_b64=base64.b64encode(before).decode(),control_paused_b64=base64.b64encode(after).decode(),pause_b64=base64.b64encode(pause).decode(),pause_sha256=digest(pause),launchagent_registered=True)
            self.record('drain-context.json',c);self.record('drain-intent.json',dict(prepared_at_unix=time.time(),owner=owner,control_before_sha256=digest(before),control_after_sha256=digest(after),pause_sha256=digest(pause),signals=0,only_new_review_admissions_close=True))
            durable(pausepath,pause);replace_exact(controlpath,before,after)
            self.record('drain-applied.json',dict(at_unix=time.time(),owned_pause_created=True,control=paused,signals_sent=0,active_jobs_interrupted=0))
            self.capture_alive(c)
        return dict(draining=True,pid=c['pid'],owner=c['owner'],signals_sent=0)
    def install(self):
        self.sealed();c=self.context()
        if (self.out/'installed.json').exists():raise ValueError('Installation already completed; use release, which rechecks all saved input/code/DB hashes')
        with self.locks(all_locks=True):
            inv=self.inventory()
            alive_records=[json.loads(x) for x in (self.out/'alive-observations.jsonl').read_bytes().splitlines()]
            tracked={pid for x in alive_records for pid in x['descendant_pids']}
            absent=not inv['coordinators'] and not inv['workers'] and not inv['exporters'] and not tracked&inv['all_pids']
            receipt=read(ROOT/'runtime/exhaustive/coordinator-exit.json')
            last=alive_records[-1];bind_exit(c['run'],receipt,last,c['birth_unix'],absent)
            if read(ROOT/'runtime/exhaustive/coordinator-run.json')!=c['run']:raise ValueError('Run changed')
            target=ROOT/'run_exhaustive.py';actual_code=digest(raw(target));recovering=(self.out/'installation-intent.json').exists()
            if recovering:
                intent=read(self.out/'installation-intent.json')
                if intent['owner']!=c['owner'] or intent['baseline_sha256']!=BASELINE or intent['candidate_sha256']!=CANDIDATE or actual_code not in {BASELINE,CANDIDATE}:raise ValueError('Unknown interrupted installation')
                compare(self.out/'runner-before.py',BASELINE)
            elif actual_code!=BASELINE:raise ValueError('Runner changed without this installation intent')
            self.pins_match(installed=actual_code==CANDIDATE);pausepath=ROOT/'runtime/supervision/disabled';check_pause(pausepath,self.pause(c),c['owner'])
            cp=ROOT/'runtime/exhaustive/worker-limit.json'
            allowed=[base64.b64decode(c['control_paused_b64'])]
            if recovering and actual_code==CANDIDATE:allowed.append(base64.b64decode(c['control_before_b64']))
            if raw(cp) not in allowed or read(ROOT/'runtime/exhaustive/manual-agent-slots.json')!=[]:raise ValueError('Control/manual guards changed')
            phase=read(ROOT/'runtime/exhaustive/continuation-phase.json')
            if phase['coordinator_pid']!=c['pid'] or phase['phase']!='review_tail_drained':raise ValueError('Phase not actually retired')
            sys.path.insert(0,str(EVIDENCE))
            from registration_reconciliation import collect
            active_pins=self.pins|({'run_exhaustive.py':CANDIDATE} if actual_code==CANDIDATE else {})
            proof=collect(ROOT,active_pins);reconciliation_name=self.fresh_record('reconciliation.json',proof)
            if proof['integrity_status']!='reconciled' or proof['ambiguities'] or not proof['all_accessible_first_passes_registered'] or proof['canonical_identities']!=30317 or len(proof['collections'])!=9 or len(proof['documentary_holds'])!=3 or proof['required_second_pass_worklist_blockers']:raise ValueError('Full reconciliation blocks installation')
            # This is a prompt change, not publication of a newly retargeted worklist.
            # Current native beforeimages are verified above; stale certificates remain pending.
            self.fresh_record('worklist-scope.json',dict(existing_worklist_preserved=True,full_retargeted_worklist_ready=proof['required_second_pass_worklist_ready'],current_identity_beforeimage_blockers=proof['required_second_pass_worklist_blockers'],reference_convergence_claimed=False))
            wl=read(ROOT/'runtime/radical-review-20261019.json');pending={(x['code_id'],x['source_id']) for x in wl['prior_articles'] if x['review_status']=='pending'}
            canonical={(x['code_id'],x['source_id']):x for x in proof['required_second_pass_dispositions']}
            config=read(ROOT/'corpus.json');slug_to_code={x['slug']:x['id'] for x in config['codes']+config['annexes']}
            import sqlite3
            from ingest import source_notes
            db=sqlite3.connect((ROOT/'corpus.sqlite').as_uri()+'?mode=ro',uri=True);db.execute('PRAGMA query_only=ON');db.execute('BEGIN')
            def resolve(m):
                if 'job' in m:
                    sources=read(ROOT/'runtime/exhaustive/jobs'/m['job']/'source.json')
                    keys=set()
                    for x in sources:
                        key=(x['code_id'],x['source_id']);actual=db.execute('SELECT source_sha256,content_xml,valid_from,valid_until FROM articles WHERE code_id=? AND id=?',key).fetchone()
                        if actual!=(x['source_sha256'],x['source_xml'],x['valid_from'],x['valid_until']) or source_notes(db,*key)!=x['source_notes_xml']:raise ValueError('Assigned whole source/NOTA/boundaries differ')
                        keys.add(key)
                    if len(keys)!=m['articles'] or len(keys)!=len(sources):raise ValueError('Assigned article count differs')
                    return keys
                keys={(slug_to_code[m['slug']],sid) for sid in m['source_ids']}
                if len(keys)!=len(m['source_ids']) or not keys<=set(canonical):raise ValueError('Unknown unattempted identity')
                return keys
            try:
                metricsbytes=raw(ROOT/'runtime/exhaustive/job-metrics.jsonl')
                if not metricsbytes.endswith(b'\n'):raise ValueError('Incomplete metric suffix')
                partitioned=partition(read(ROOT/'runtime/exhaustive/queue-admission-plan.json'),read(ROOT/'runtime/exhaustive/admission-status.json'),read(ROOT/'runtime/exhaustive/admission-deferred.json'),[json.loads(x) for x in metricsbytes.splitlines()],pending,resolve)
            finally:db.close()
            self.fresh_record('queue-disposition.json',partitioned)
            for rel,h in proof['input_hashes'].items():compare(ROOT.parent/rel,h)
            self.pins_match(installed=actual_code==CANDIDATE);check_pause(pausepath,self.pause(c),c['owner'])
            before=raw(target);candidate=raw(PREP/'run_exhaustive.py')
            if digest(candidate)!=CANDIDATE:raise ValueError('Candidate changed')
            if not recovering:
                prompt_only(before.decode(),candidate.decode());durable(self.out/'runner-before.py',before)
                self.record('installation-intent.json',dict(at_unix=time.time(),owner=c['owner'],baseline_sha256=BASELINE,candidate_sha256=CANDIDATE,only_file='run_exhaustive.py',exit_receipt=receipt,last_alive=last,full_reconciliation_sha256=digest(raw(self.out/reconciliation_name)),queue_disposition=partitioned,reference_certificate_convergence_pending=proof['reference_certificates']))
            else:self.fresh_record('installation-recovery.json',dict(at_unix=time.time(),code_before=actual_code,fresh_reconciliation=reconciliation_name,all_current_guards_recollected=True))
            if actual_code==BASELINE:replace_exact(target,before,candidate)
            self.pins_match(installed=True)
            if raw(cp)==base64.b64decode(c['control_paused_b64']):replace_exact(cp,raw(cp),base64.b64decode(c['control_before_b64']))
            self.record('installed.json',dict(at_unix=time.time(),installed_sha256=digest(raw(target)),only_one_prompt_literal_changed=True,worker_control_restored=read(cp),reconciliation_file=reconciliation_name,source_database_sha256=stream_sha(ROOT/'corpus.sqlite'),wal_sha256=stream_sha(ROOT/'corpus.sqlite-wal') if (ROOT/'corpus.sqlite-wal').exists() else None,canonical_mutations=0,signals_sent=0,coordinators_launched=0))
        return dict(installed=True,pause_still_owned=True,new_runner_sha256=CANDIDATE)
    def release(self):
        self.sealed();c=self.context()
        if not (self.out/'installed.json').exists() or (self.out/'pause-released.json').exists():raise ValueError('Release stage differs')
        with self.locks(all_locks=True):
            inv=self.inventory()
            if inv['coordinators'] or inv['workers'] or inv['exporters']:raise ValueError('Unexpected process before supervised resumption')
            self.pins_match(installed=True)
            installed=read(self.out/'installed.json');proof=read(self.out/installed['reconciliation_file'])
            for rel,h in proof['input_hashes'].items():compare(ROOT.parent/rel,h)
            if stream_sha(ROOT/'corpus.sqlite')!=installed['source_database_sha256']:raise ValueError('Database changed after full reconciliation')
            wal=ROOT/'corpus.sqlite-wal'
            if (stream_sha(wal) if wal.exists() else None)!=installed['wal_sha256']:raise ValueError('WAL changed after full reconciliation')
            if raw(ROOT/'runtime/exhaustive/worker-limit.json')!=base64.b64decode(c['control_before_b64']) or read(ROOT/'runtime/exhaustive/manual-agent-slots.json')!=[]:raise ValueError('Resumption controls differ')
            p=ROOT/'runtime/supervision/disabled';check_pause(p,self.pause(c),c['owner'])
            self.record('resumption-intent.json',dict(at_unix=time.time(),owner=c['owner'],pause_sha256=c['pause_sha256'],action='Remove only owned pause; registered existing LaunchAgent performs one continuation',no_direct_launch=True,no_signal=True))
            check_pause(p,self.pause(c),c['owner']);p.unlink();sync(p.parent)
            self.record('pause-released.json',dict(at_unix=time.time(),only_owned_pause_removed=True,waiting_for_supervisor=True,new_native_responses_and_accepted_review_still_required=True))
        return dict(pause_released=True,no_launch_or_signal=True)

if __name__=='__main__':
    if len(sys.argv)!=2 or sys.argv[1] not in {'drain','poll','install','release'}:raise SystemExit('Choose drain, poll, install or release; no test/backend override')
    result=getattr(Production(),sys.argv[1])()
    print(json.dumps(result,ensure_ascii=False),flush=True)
