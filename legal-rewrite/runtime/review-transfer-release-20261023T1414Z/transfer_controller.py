"""Prepared transfer controller. Never run against production during preparation.

No model or article-registration path exists here. A durable, owned supervisor
pause survives interruption. Six direct module files use a journalled group
transaction under exclusion; this is not an atomic six-file POSIX rename.
"""
from contextlib import contextmanager, ExitStack
from pathlib import Path
import argparse, base64, copy, fcntl, hashlib, importlib.util, json, os
import shlex, sqlite3, stat, subprocess, sys, tempfile, time, uuid

SEAL='e5c236715c130c46f57108d96d39f8e9cdf6e72a672d54448d31a5e91f079229'
PACKAGE='review-transfer-release-20261023T1414Z'
REBASE='review-reallocation-rebase-20261023T1058Z'
APPROVED_ROOT=Path('/Users/alexandremasmejean/.codex/.chatgpt-projects/g-p-6ad59c015c308191aa21cba63c71a6dc/legal-rewrite')
RELEASE_INPUT_PINS_SHA='be1b0a9b15080e3fe781f9b9070a7f9493d63bc6aa08dc61f1adc490afcd49e5'
INITIAL_HOT_SHA='3b42181e618137d37e78d1a37216c8f1cb64ebb6d2f32f7aa935d99d52cdfc4e'
BASELINE_PINS_SHA='01acd90d5f8410f1381b5995a26450628533cead3c2b0b6921fc7184f903fb2c'
from transfer_guards import terminal_new_queue, successful_exit, native_launch_attestation
from registration_reconciliation import collect as collect_registration,first_pass_inventory
from accepted_work import accepted_review
from review_worklist import WORKLIST,build as build_worklist,matches as worklist_matches
import datetime
SIX=('continuation_tail.py','review_lane_observation.py','review_lanes.py',
     'run_exhaustive.py','supervise_exhaustive.py','worker_capacity.py')
POLICIES=('corpus.json','policy-coordinations.json','site-summaries.json',
          'reference-focus-extra.json','runtime/exhaustive/model-policy.json')
GATE_CODE=('register_batches.py','review_prior.py','reference_coherence.py',
           'reference_queue.py','ingest.py','source_assets.py','substantive_impact.py','worker_execution.py')
HOT='runtime/exhaustive/worker-limit.json'
PLAN='runtime/exhaustive/parallelism-plan.json'
DISABLED='runtime/supervision/disabled'

class Blocked(RuntimeError):pass
class Conflict(Blocked):pass
def sha(data):return hashlib.sha256(data).hexdigest()
def encoded(data):return None if data is None else base64.b64encode(data).decode()
def decoded(value):return None if value is None else base64.b64decode(value)
def packed(value):return (json.dumps(value,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
def raw(path):
    path=Path(path)
    if path.exists() and not stat.S_ISREG(path.stat().st_mode):raise Blocked('Non-regular evidence: '+str(path))
    if path.is_symlink():raise Blocked('Symlink is not an owned regular file: '+str(path))
    return path.read_bytes() if path.exists() else None
def required_json(path):
    value=raw(path)
    if value is None:raise Blocked('Required evidence is absent: '+str(path))
    try:return json.loads(value)
    except (ValueError,UnicodeError) as error:raise Blocked('Invalid JSON: '+str(path)) from error

def durable(path,data):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    if data is None:path.unlink()
    else:
        mode=stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o600
        fd,name=tempfile.mkstemp(prefix='.'+path.name+'.transfer-',dir=path.parent)
        try:
            os.fchmod(fd,mode)
            with os.fdopen(fd,'wb') as stream:stream.write(data);stream.flush();os.fsync(stream.fileno())
            os.replace(name,path)
        finally:
            if os.path.exists(name):os.unlink(name)
    fd=os.open(path.parent,os.O_RDONLY)
    try:os.fsync(fd)
    finally:os.close(fd)

@contextmanager
def locked(path,*,must_exist=True):
    path=Path(path)
    if path.is_symlink() or (path.exists() and not stat.S_ISREG(path.stat().st_mode)):
        raise Blocked('Lock must be a regular non-symlink file: '+str(path))
    if must_exist and not path.is_file():raise Blocked('Required lock is unknown: '+str(path))
    with path.open('r+' if must_exist else 'a+') as stream:
        try:fcntl.flock(stream,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError as error:raise Blocked('Required lock is busy: '+str(path)) from error
        yield stream

def sealed_package(folder):
    folder=Path(folder);data=raw(folder/'manifest.json')
    if data is None or sha(data)!=SEAL:raise Blocked('Sealed candidate manifest changed')
    manifest=json.loads(data)
    if set(manifest['candidate'])!=set(SIX):raise Blocked('Candidate module set is not the exact six')
    for name in SIX:
        if sha((folder/'candidate'/name).read_bytes())!=manifest['candidate'][name]['sha256']:
            raise Blocked('Sealed candidate module changed: '+name)
    return manifest

def parse_processes(output):
    if not isinstance(output,str) or not output.strip():raise Blocked('Process inventory is unknown')
    rows=[]
    for line in output.splitlines():
        parts=line.split(None,8)
        if len(parts)!=9:raise Blocked('Unparseable process identity')
        try:
            row={'pid':int(parts[0]),'ppid':int(parts[1]),'pgid':int(parts[2]),
                 'started':' '.join(parts[3:8]),'args':shlex.split(parts[8])}
        except ValueError as error:raise Blocked('Ambiguous process record') from error
        if not row['args']:raise Blocked('Empty process command')
        row['os_started_at_unix']=utc_birth(row['started'])
        rows.append(row)
    if len({r['pid'] for r in rows})!=len(rows):raise Blocked('Duplicate process PID')
    return rows

def utc_birth(lstart):
    try:
        return int(datetime.datetime.strptime(lstart,'%a %b %d %H:%M:%S %Y').replace(tzinfo=datetime.timezone.utc).timestamp())
    except (TypeError,ValueError) as error:raise Blocked('OS process birth cannot be converted explicitly to UTC') from error

def bind_process(row,run,now):
    birth=row.get('os_started_at_unix');start=run.get('started_at_unix')
    if (type(birth) is not int or type(start) is not int or row['pid']!=run.get('pid')
            or not birth<=start<=now or not 0<=start-birth<=60):
        raise Blocked('Actual OS birth and run creation do not bind to one lifetime')
    return row|{'started_at_unix':start,'run_start_delay_seconds':start-birth}

def descendant_groups(rows,pid):
    known={pid};changed=True
    while changed:
        new={r['pid'] for r in rows if r['ppid'] in known};changed=not new<=known;known|=new
    return sorted({r['pgid'] for r in rows if r['pid'] in known})

def classify(root,rows):
    root=Path(root);runner=str(root/'run_exhaustive.py');jobs=(root/'runtime/exhaustive/jobs').resolve()
    coordinators=[];workers=[]
    for row in rows:
        args=row['args']
        if runner in args[1:3] and Path(args[0]).name.lower().startswith('python'):coordinators.append(row)
        if Path(args[0]).name=='codex' and 'exec' in args:
            try:target=Path(args[args.index('--output-last-message')+1]).resolve()
            except (ValueError,IndexError):raise Blocked('Native worker output identity is ambiguous')
            if target.is_relative_to(jobs):
                if target.name!='result.json':raise Blocked('Unexpected worker output target')
                workers.append(row|{'job':target.parent.name,'folder':str(target.parent),
                                   'kind':'review' if target.parent.name.startswith(('review-','reference-review-')) else 'new'})
    return coordinators,workers

class NativeBackend:
    """All actual collectors. None is called when this module is imported."""
    def __init__(self,root):self.root=Path(root)
    def reconciliation_precondition(self):
        # This new release copy is bound to one reviewed local project and its
        # sealed helper sources. No external boolean/configuration enables it.
        # Transfer.run still proves the real unique PID, whole nine-collection
        # first-pass coverage and terminal new queue BEFORE controlling pause
        # or admissions; after natural exit it recollects every registration
        # guard under exclusion on EVERY prelaunch resume.
        folder=Path(__file__).resolve().parent
        if self.root.resolve()!=APPROVED_ROOT or folder!=APPROVED_ROOT/'runtime'/PACKAGE:
            raise Blocked('NOT READY: release is bound to the exact approved project and reviewed runtime folder')
        data=raw(folder/'release-input-pins.json')
        if data is None or sha(data)!=RELEASE_INPUT_PINS_SHA:raise Blocked('NOT READY: release input pins differ')
        helper_pins=json.loads(data)
        if set(helper_pins)!={'registration_reconciliation.py','transfer_guards.py','accepted_work.py','review_worklist.py','baseline-policy-pins.json'}:
            raise Blocked('NOT READY: release helper set differs')
        for name,h in helper_pins.items():
            value=raw(folder/name)
            if value is None or sha(value)!=h:raise Blocked('NOT READY: release helper changed: '+name)
        baseline=raw(folder/'baseline-policy-pins.json')
        if baseline is None or sha(baseline)!=BASELINE_PINS_SHA:raise Blocked('NOT READY: immutable release baseline differs')
        return dict(expected_baseline_pins=json.loads(baseline),initial_hot_sha256=INITIAL_HOT_SHA,
                    release_helpers_sha256=RELEASE_INPUT_PINS_SHA,
                    controller_sha256=sha(raw(Path(__file__))),source='reviewed_bounded_production_release')
    def processes(self):
        output=subprocess.check_output(['/bin/ps','-axo','pid=,ppid=,pgid=,lstart=,command='],
              text=True,timeout=15,env=os.environ|{'LC_ALL':'C','TZ':'UTC'})
        return parse_processes(output)
    def now(self):return time.time()
    def wait(self,seconds):time.sleep(min(seconds,1))
    def baseline_pins(self,manifest):
        path=Path(__file__).parent/'baseline-policy-pins.json'
        data=raw(path)
        if data is None or sha(data)!=BASELINE_PINS_SHA:raise Blocked('Prepared gate/policy pins changed')
        pins=json.loads(data)
        for name,entry in manifest['baseline'].items():
            if pins.get(name)!=entry['sha256']:raise Blocked('Rebased baseline differs: '+name)
        if raw(self.root/'continuation_tail.py') is not None:raise Blocked('Unowned continuation module exists')
        self.check_pins(pins)
        return pins
    def check_pins(self,pins):
        for name,expected in pins.items():
            target=self.root/name
            if (Path(name).is_absolute() or '..' in Path(name).parts or target.is_symlink()
                    or not target.resolve().is_relative_to(self.root) or raw(target) is None or sha(raw(target))!=expected):
                raise Conflict('Pinned dependency changed: '+name)
        actual={str(p.relative_to(self.root)) for p in (self.root/'attachments/records').glob('*.json')}
        if actual!={n for n in pins if n.startswith('attachments/records/')}:raise Conflict('Companion membership changed')
    def entry(self,expected_pid,max_age=None):
        rows=self.processes();live,workers=classify(self.root,rows)
        if len(live)!=1 or live[0]['pid']!=expected_pid:raise Blocked('Exact unique old coordinator is unknown')
        run=required_json(self.root/'runtime/exhaustive/coordinator-run.json')
        identity=bind_process(live[0],run,self.now())
        identity['last_seen_alive_at_unix']=self.now()
        identity['descendant_groups']=descendant_groups(rows,expected_pid)
        accounting=terminal_new_queue(self.root,identity,workers,self.now())
        if any(x['current_disposition']=='deferred_still_pending' for x in accounting['dispositions']):
            raise Blocked('Deferred first passes still require fresh ordinary recovery before transfer')
        return {'identity':identity,'workers':workers,'observed_at_unix':self.now(),'terminal_queue':accounting}
    def idle(self,identity,groups):
        rows=self.processes();live,workers=classify(self.root,rows)
        same_pid=[x for x in rows if x['pid']==identity['pid']]
        if live:
            if len(live)!=1 or any(live[0][k]!=identity[k] for k in ['pid','started','args','pgid','os_started_at_unix']):
                raise Blocked('Coordinator identity changed during drain')
            if any(w['ppid']!=identity['pid'] for w in workers):raise Blocked('Orphan or foreign native worker')
            bind_process(live[0],required_json(self.root/'runtime/exhaustive/coordinator-run.json'),self.now())
            identity['last_seen_alive_at_unix']=self.now()
            identity['descendant_groups']=sorted(set(identity.get('descendant_groups',[]))|set(descendant_groups(rows,identity['pid'])))
            return False,workers
        if same_pid:raise Blocked('PID reuse or command replacement prevents exact exit binding')
        all_groups=set(groups)|set(identity.get('descendant_groups',[]))|{identity['pgid']}
        if workers or any(x['pgid'] in all_groups for x in rows):raise Blocked('A descendant or native worker survived the coordinator')
        proof=successful_exit(self.root,identity,identity['last_seen_alive_at_unix'],self.now())
        # Preserve both independent clock readings and their explicit offset.
        proof.update(os_started_at_unix=identity['os_started_at_unix'],run_start_delay_seconds=identity['run_start_delay_seconds'])
        identity['exit_binding']=proof
        return True,[]
    def first_pass_inventory(self,pins):
        self.check_pins(pins)
        report=first_pass_inventory(self.root,pins)
        self.check_pins(pins)
        if not report['all_accessible_first_passes_registered']:raise Blocked('Accessible first passes remain outside the terminal queue')
        return report
    def reconcile(self,pins):
        self.check_pins(pins)
        result=collect_registration(self.root,pins)
        self.check_pins(pins)
        if not result['all_accessible_first_passes_registered']:
            raise Blocked('Accessible first passes remain open in the full nine-collection reconciliation')
        return result
    def launch(self,folder):
        # Reuse exactly the installed supervisor launcher, after evicting old
        # versions of the six modules from this controller's single interpreter.
        # Their origin must still be this root; never import an unrelated tree.
        for name in SIX:
            key=Path(name).stem;previous=sys.modules.get(key)
            if previous is not None:
                if Path(previous.__file__).resolve().parent!=self.root:raise Blocked('Foreign cached launch dependency: '+key)
                del sys.modules[key]
        sys.path.insert(0,str(self.root))
        try:
            spec=importlib.util.spec_from_file_location('_transfer_supervisor',self.root/'supervise_exhaustive.py')
            module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
            return module.launch(folder)
        finally:sys.path.pop(0)
    def launched(self,folder,pins):
        rows=self.processes();live,workers=classify(self.root,rows)
        if len(live)!=1:raise Blocked('New coordinator is not unique')
        run=required_json(self.root/'runtime/exhaustive/coordinator-run.json')
        live[0]=bind_process(live[0],run,self.now())
        self.check_pins(pins)
        result=native_launch_attestation(self.root,folder,live,workers,pins,self.now())
        # A valid startup header alone never establishes a response; the guard
        # checks every live native session, its own log and actual OS lifetime.
        result['accepted_review']=accepted_review(self.root,result['pid'],pins,self.now())
        self.check_pins(pins)
        return result

class Transfer:
    def __init__(self,root,sealed,run_dir,backend=None,timeout=7200):
        self.root=Path(root).resolve();self.sealed=Path(sealed).resolve();self.folder=Path(run_dir).resolve()
        allowed=self.root/('runtime/'+PACKAGE+'/runs')
        if self.root.name!='legal-rewrite' or not self.folder.is_relative_to(allowed) or self.folder==allowed:
            raise Blocked('Transfer run directory is outside the bounded preparation runtime')
        if self.sealed!=self.root/('runtime/'+REBASE):
            raise Blocked('Sealed package path differs from the reviewed package')
        self.backend=backend or NativeBackend(self.root);self.timeout=timeout
        self.manifest=sealed_package(self.sealed);self.path=self.folder/'state.json';self.state=None
    def save(self):durable(self.path,packed(self.state))
    def phase(self,name,**evidence):
        self.state['phase']=name;self.state.setdefault('events',[]).append({'phase':name,'at':self.backend.now(),**evidence});self.save()
    def assert_pins(self,installed=False,installing=False):
        for name,digest in self.state['pins'].items():
            expected=self.manifest['candidate'][name]['sha256'] if installed and name in SIX else digest
            data=raw(self.root/name)
            valid=data is not None and sha(data)==expected
            if name==PLAN and PLAN in self.state.get('mutations',{}):
                item=self.state['mutations'][PLAN]
                choices={decoded(item['after'])} if self.state['phase'] in {'CONFIGURED','WORKLIST_PUBLISHED','LAUNCH_INTENT','LAUNCHED','ADOPTION_VERIFIED','COMPLETE'} else {decoded(item['before']),decoded(item['after'])}
                valid=data in choices
            if installing and name in SIX and name in self.state.get('mutations',{}):
                item=self.state['mutations'][name]
                valid=data in {decoded(item['before']),decoded(item['after'])}
            if not valid:raise Conflict('Pinned code/policy/catalogue changed: '+name)
        if installed:
            for name in SIX:
                if sha((self.root/name).read_bytes())!=self.manifest['candidate'][name]['sha256']:raise Conflict('Incomplete six-module group')
    def effective_pins(self):
        pins=copy.deepcopy(self.state['pins'])
        for name,item in self.state.get('mutations',{}).items():
            if name not in set(SIX)|{PLAN}:continue
            current=raw(self.root/name)
            allowed={decoded(item['before']),decoded(item['after'])}
            if current not in allowed:raise Conflict('Journalled module/control differs: '+name)
            if current is not None:pins[name]=sha(current)
            else:pins.pop(name,None)
        return pins
    def fresh_reconciliation(self,require_worklist=False):
        if required_json(self.root/'runtime/exhaustive/manual-agent-slots.json')!=[]:raise Blocked('Manual reservations are unknown or nonempty')
        hot=self.state.get('mutations',{}).get(HOT)
        if hot is not None:
            allowed={decoded(hot['after'])}
            if 'configured_after' in hot:allowed.add(decoded(hot['configured_after']))
            if raw(self.root/HOT) not in allowed:raise Conflict('Owned admission control changed')
        idle,_=self.backend.idle(self.state['entry']['identity'],set(self.state.get('worker_groups',[])))
        if not idle:raise Blocked('Full drain no longer confirmed')
        pins=self.effective_pins()
        proof=self.backend.reconcile(pins)
        if (proof.get('integrity_status')!='reconciled' or proof.get('ambiguities')!=[]
                or proof.get('all_accessible_first_passes_registered') is not True):
            raise Blocked('Full current reconciliation is incomplete or ambiguous')
        if require_worklist and proof.get('required_second_pass_worklist_ready') is not True:raise Blocked('Published complete current second-pass worklist is not reconciled')
        self.reconciled_proof=proof
        number=1+self.state.get('reconciliation_generation',0)
        target=self.folder/('reconciliation-'+str(number)+'.json')
        if target.exists():raise Conflict('Reconciliation generation already exists')
        durable(target,packed(proof));self.state['reconciliation_generation']=number
        self.state['reconciliation_sha256']=sha(packed(proof));self.save()
    def change(self,name,after):
        if name not in set(SIX)|{HOT,PLAN,DISABLED,WORKLIST}:raise Blocked('Mutation target is outside the exact transfer allowlist')
        path=self.root/name;mutations=self.state.setdefault('mutations',{})
        if not path.resolve().is_relative_to(self.root):raise Blocked('Mutation path escapes the project root')
        if name not in mutations:
            mutations[name]={'before':encoded(raw(path)),'after':encoded(after)};self.save()
        item=mutations[name]
        if decoded(item['after'])!=after:raise Conflict('Mutation intent differs: '+name)
        current=raw(path)
        if current==after:return
        if current!=decoded(item['before']):raise Conflict('Intervening control/code write: '+name)
        durable(path,after)
    def restore(self,names):
        for name in reversed(list(names)):
            item=self.state.get('mutations',{}).get(name)
            if item is None:continue
            current=raw(self.root/name);before=decoded(item['before']);after=decoded(item['after'])
            if current==before:continue
            if current!=after:raise Conflict('Rollback refuses intervening bytes: '+name)
            durable(self.root/name,before)
    def owned_pause(self):
        marker=packed({'transfer_owner':self.state['owner'],'state_file':str(self.path),'candidate_manifest_sha256':SEAL})
        if DISABLED not in self.state.get('mutations',{}) and raw(self.root/DISABLED) is not None:
            raise Blocked('A pre-existing supervisor pause is never replaced')
        self.change(DISABLED,marker)
    def close_reviews(self):
        with locked(self.root/'runtime/exhaustive/manual-agent-slots.lock'):
            manual=required_json(self.root/'runtime/exhaustive/manual-agent-slots.json')
            if manual!=[]:raise Blocked('Manual reservations must be known and empty')
            prior=self.state.get('mutations',{}).get(HOT)
            if prior is not None and raw(self.root/HOT)==decoded(prior['after']):return
            current=required_json(self.root/HOT)
            if current.get('workers')!=7 or current.get('role_limits')!={'new':6,'review':0}:raise Blocked('Expected effective seven-worker role control differs')
            paused=copy.deepcopy(current);paused.update(workers=7,role_limits={'new':6,'review':0})
            self.change(HOT,packed(paused))
    def drain(self):
        deadline=self.backend.now()+self.timeout;identity=self.state['entry']['identity']
        groups=set(self.state.get('worker_groups',[]))
        while True:
            self.assert_pins();idle,workers=self.backend.idle(identity,groups)
            groups.update(w['pgid'] for w in workers)
            if sorted(groups)!=self.state.get('worker_groups',[]):self.state['worker_groups']=sorted(groups);self.save()
            self.save()
            if idle:return
            if self.backend.now()>=deadline:raise TimeoutError('Natural drain timed out; no process signalled')
            self.backend.wait(.2)
    def group_install(self):
        self.assert_pins(installing=True)
        try:
            for name in SIX:self.change(name,(self.sealed/'candidate'/name).read_bytes())
            self.assert_pins(installed=True)
        except Exception:
            self.restore(SIX)
            raise
    def configure(self):
        plan=required_json(self.root/PLAN)
        if plan.get('capacity')!=8 or plan.get('current_workers')!=8 or plan.get('role_limits')!={'new':6,'review':2}:raise Blocked('Authorized eight-worker ceiling differs')
        updated=copy.deepcopy(plan);updated.update(continuation_mode='recover_new_before_reviews',review_tail_capacity=8)
        self.change(PLAN,packed(updated))
        original=required_json(self.folder/'original-worker-control.json')
        original.update(workers=8,role_limits={'new':6,'review':0},review_tail_limit=8)
        # A second intended write to the hot control must own the paused bytes.
        item=self.state['mutations'][HOT];desired=packed(original)
        if 'configured_after' not in item:
            item['configured_after']=encoded(desired);self.save()
        if decoded(item['configured_after'])!=desired:raise Conflict('Configured hot-control intent differs')
        current=raw(self.root/HOT)
        if current not in {decoded(item['after']),desired}:raise Conflict('Paused/configured worker control changed')
        if current!=desired:durable(self.root/HOT,desired)
    def publish_worklist(self):
        proof=self.reconciled_proof
        old=raw(self.root/WORKLIST)
        if old is None or sha(old)!=proof['review_manifest_sha256']:raise Conflict('Review manifest changed after current reconciliation')
        mutation=self.state.get('mutations',{}).get(WORKLIST)
        if mutation is not None:
            planned=decoded(mutation['after'])
            if old not in {decoded(mutation['before']),planned}:raise Conflict('Published review worklist has intervening bytes')
            if not worklist_matches(proof,json.loads(planned)):raise Blocked('Journalled worklist no longer matches fresh corpus evidence')
            self.change(WORKLIST,planned)
            before=decoded(mutation['before']);document=json.loads(planned)
        else:
            document=build_worklist(proof,json.loads(old),self.state['owner']);before=old
            # Save full original and intended bytes before the atomic rename.
            self.change(WORKLIST,packed(document))
        self.state['worklist_publication']=dict(owner=self.state['owner'],before_sha256=sha(before),
            after_sha256=sha(packed(document)),reconciliation_sha256=self.state['reconciliation_sha256'])
        self.save()
    def assert_worklist_bytes(self):
        item=self.state.get('mutations',{}).get(WORKLIST)
        if item is None or raw(self.root/WORKLIST)!=decoded(item['after']):raise Conflict('Published review worklist changed before launch')
    def finish_adoption(self,receipt):
        self.state['new_coordinator']=receipt
        marker=self.state['mutations'][DISABLED]
        self.state['pause_release_intent']={'owner':self.state['owner'],'owned_marker_sha256':sha(decoded(marker['after'])),'restore':marker['before']}
        self.phase('ADOPTION_VERIFIED')
        self.restore([DISABLED]);self.phase('COMPLETE')
    def run(self,expected_pid):
        release=self.backend.reconciliation_precondition()
        if self.path.exists():
            self.state=required_json(self.path)
            if self.state.get('root')!=str(self.root) or self.state.get('seal')!=SEAL:raise Blocked('Resume identity differs')
            if release is not None:
                if self.state.get('pins')!=release['expected_baseline_pins']:raise Blocked('Resume baseline is not the sealed release baseline')
                if self.state.get('production_release')!=release:raise Blocked('Resume controller or release helper identity differs')
        else:
            if release is not None and (raw(self.root/HOT) is None or sha(raw(self.root/HOT))!=release['initial_hot_sha256']):raise Blocked('Initial owned admission control differs from the reviewed current state')
            # Refuse before any production lock/control/file change.
            entry=self.backend.entry(expected_pid)
            pins=self.backend.baseline_pins(self.manifest)
            self.folder.mkdir(parents=True,exist_ok=True)
            self.state={'owner':str(uuid.uuid4()),'root':str(self.root),'seal':SEAL,'phase':'ELIGIBLE',
                        'entry':entry,'pins':pins,'production_release':release,'mutations':{},'events':[],
                        'worker_groups':sorted({w['pgid'] for w in entry['workers']})}
            durable(self.folder/'original-worker-control.json',raw(self.root/HOT));self.save()
        with locked(self.folder/'controller.lock',must_exist=False),locked(self.root/'runtime/supervision/supervisor.lock'):
            phase=self.state['phase']
            if phase=='COMPLETE':return self.state
            if phase in {'ABORTED','ROLLBACK_CONFLICT'}:raise Blocked('Terminal transfer needs a new parent review')
            marker=self.state.get('mutations',{}).get(DISABLED)
            released_intent=self.state.get('pause_release_intent')
            release_boundary=(phase=='ADOPTION_VERIFIED' and marker is not None and marker['before'] is None
                and released_intent=={'owner':self.state['owner'],'owned_marker_sha256':sha(decoded(marker['after'])),'restore':None}
                and raw(self.root/DISABLED) is None)
            if marker is not None and not release_boundary and (marker['before'] is not None or raw(self.root/DISABLED)!=decoded(marker['after'])):
                raise Conflict('Owned durable supervisor pause is missing or was replaced')
            try:
                if phase in {'LAUNCH_INTENT','LAUNCHED','ADOPTION_VERIFIED'}:
                    if not (self.folder/'launch/launch.json').exists():raise Blocked('Launch outcome is ambiguous; no second launch is allowed')
                    self.assert_pins(installed=True)
                    receipt=self.backend.launched(self.folder/'launch',self.effective_pins())
                    self.finish_adoption(receipt)
                    return self.state
                if phase=='ELIGIBLE':
                    hot=self.state.get('mutations',{}).get(HOT)
                    if hot is None or raw(self.root/HOT)!=decoded(hot['after']):
                        again=self.backend.entry(expected_pid)
                        if any(again['identity'][k]!=self.state['entry']['identity'][k] for k in ['pid','started','args','pgid','os_started_at_unix','started_at_unix']):raise Blocked('Old process changed before exclusion')
                    self.assert_pins()
                    entry_inventory=self.backend.first_pass_inventory(self.state['pins'])
                    durable(self.folder/'entry-inventory.json',packed(entry_inventory))
                    self.owned_pause();self.close_reviews();self.phase('REVIEW_ADMISSIONS_CLOSED')
                if self.state['phase']=='REVIEW_ADMISSIONS_CLOSED':
                    self.drain();self.phase('NATURALLY_DRAINED')
                with ExitStack() as stack:
                    # No writer/coordinator/manual lock is held while waiting.
                    for name in ['runtime/exhaustive/coordinator.lock','draft-writer.lock','runtime/exhaustive/manual-agent-slots.lock']:
                        stack.enter_context(locked(self.root/name))
                    # Every resume of any prelaunch phase recollects the live
                    # DB/owners/intentions/source/notes/reference/beforeimages.
                    # A saved reconciliation hash never authorizes continuation.
                    if self.state['phase'] in {'NATURALLY_DRAINED','RECONCILIATION_REQUIRED','RECONCILED','SIX_MODULES_INSTALLED','CONFIGURED','WORKLIST_PUBLISHED'}:
                        self.assert_pins(installing=self.state['phase']=='RECONCILED',installed=self.state['phase'] in {'SIX_MODULES_INSTALLED','CONFIGURED','WORKLIST_PUBLISHED'})
                        self.fresh_reconciliation()
                        if self.state['phase'] in {'NATURALLY_DRAINED','RECONCILIATION_REQUIRED'}:self.phase('RECONCILED')
                    if self.state['phase']=='RECONCILED':
                        self.group_install();self.phase('SIX_MODULES_INSTALLED')
                    if self.state['phase']=='SIX_MODULES_INSTALLED':
                        self.configure();self.phase('CONFIGURED')
                    self.assert_pins(installed=True)
                    self.fresh_reconciliation()
                    if self.state['phase']=='CONFIGURED':
                        self.publish_worklist();self.phase('WORKLIST_PUBLISHED')
                    self.assert_worklist_bytes()
                    self.fresh_reconciliation(require_worklist=True)
                    idle,_=self.backend.idle(self.state['entry']['identity'],set(self.state.get('worker_groups',[])))
                    if not idle:raise Blocked('Process appeared before launch')
                # Release the coordinator lock before the existing launcher,
                # while the supervisor exclusion and durable owned pause remain.
                if self.state['phase']=='WORKLIST_PUBLISHED':
                    self.assert_worklist_bytes()
                    self.phase('LAUNCH_INTENT')
                    launch_dir=self.folder/'launch';launch_dir.mkdir(exist_ok=True)
                    pid=self.backend.launch(launch_dir)
                    self.phase('LAUNCHED',pid=pid)
                elif self.state['phase']=='LAUNCH_INTENT':
                    # Unknown outcome can never become a second launch.
                    if not (self.folder/'launch/launch.json').exists():raise Blocked('Launch outcome is ambiguous; no second launch is allowed')
                    self.phase('LAUNCHED')
                if self.state['phase']=='LAUNCHED':
                    self.assert_pins(installed=True)
                    receipt=self.backend.launched(self.folder/'launch',self.effective_pins())
                    self.finish_adoption(receipt)
                return self.state
            except TimeoutError:
                if self.state['phase']!='REVIEW_ADMISSIONS_CLOSED':
                    self.save();raise
                try:self.restore([DISABLED,HOT]);self.phase('ABORTED',reason='natural_drain_timeout')
                except Conflict:self.phase('ROLLBACK_CONFLICT');raise
                raise
            except BaseException:
                # Interruptions retain a durable pause and journal for resume.
                # Do not restore files/controls over an intervening write and do
                # not reactivate a supervisor over an incomplete installation.
                self.save();raise

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--activate',action='store_true')
    parser.add_argument('--root',type=Path,required=True)
    parser.add_argument('--sealed',type=Path,required=True)
    parser.add_argument('--run-dir',type=Path,required=True)
    parser.add_argument('--expected-pid',type=int,required=True)
    args=parser.parse_args()
    if not args.activate:raise SystemExit('Offline preparation only. No production collector, preflight or activation was called.')
    Transfer(args.root,args.sealed,args.run_dir).run(args.expected_pid)

if __name__=='__main__':main()
