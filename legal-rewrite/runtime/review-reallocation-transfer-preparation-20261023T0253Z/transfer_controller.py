"""Prepared transfer controller. Never run against production during preparation.

No model or article-registration path exists here. A durable, owned supervisor
pause survives interruption. Six direct module files use a journalled group
transaction under exclusion; this is not an atomic six-file POSIX rename.
"""
from contextlib import contextmanager, ExitStack
from pathlib import Path
import argparse, base64, copy, fcntl, hashlib, importlib.util, json, os
import shlex, sqlite3, stat, subprocess, sys, tempfile, time, uuid

SEAL='f8cbed8270405812119485da55d2faa15d52bbd6b98b9d7539d2b506e202de68'
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
        rows.append(row)
    if len({r['pid'] for r in rows})!=len(rows):raise Blocked('Duplicate process PID')
    return rows

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
        # Intentionally hard-blocked. A JSON boolean or command-line switch
        # cannot substitute for the absent, parent-reviewed current collector.
        raise Blocked('NOT READY: current guarded parent reconciliation collector/certificate verifier is not implemented')
    def processes(self):
        output=subprocess.check_output(['/bin/ps','-axo','pid=,ppid=,pgid=,lstart=,command='],
              text=True,timeout=15,env=os.environ|{'LC_ALL':'C'})
        return parse_processes(output)
    def now(self):return time.time()
    def wait(self,seconds):time.sleep(min(seconds,1))
    def baseline_pins(self,manifest):
        pins={}
        for name,entry in manifest['baseline'].items():
            data=raw(self.root/name)
            if data is None or sha(data)!=entry['sha256']:raise Blocked('Baseline code changed: '+name)
            pins[name]=sha(data)
        if raw(self.root/'continuation_tail.py') is not None:raise Blocked('Unowned continuation module already exists')
        for name in GATE_CODE+POLICIES:
            data=raw(self.root/name)
            if data is None:raise Blocked('Required gate/policy is unknown: '+name)
            pins[name]=sha(data)
        records=self.root/'attachments/records'
        if not records.is_dir():raise Blocked('Companion catalogue is unknown')
        for path in sorted(records.glob('*.json')):pins[str(path.relative_to(self.root))]=sha(path.read_bytes())
        return pins
    def entry(self,expected_pid,max_age=120):
        rows=self.processes();live,workers=classify(self.root,rows)
        if len(live)!=1 or live[0]['pid']!=expected_pid:raise Blocked('Exact unique old coordinator is unknown')
        base=self.root/'runtime/exhaustive'
        run=required_json(base/'coordinator-run.json');ad=required_json(base/'admission-status.json')
        plan=required_json(base/'queue-admission-plan.json')
        if raw(base/'coordinator.pid')!=str(expected_pid).encode():raise Blocked('Coordinator PID file differs')
        if any(r.get('coordinator_pid',r.get('pid'))!=expected_pid for r in [run,ad,plan]):raise Blocked('Queue/run PID differs')
        stamp=ad.get('updated_at_unix')
        if type(stamp) is not int or not 0<=self.now()-stamp<=max_age:raise Blocked('Admission evidence is stale or unknown')
        for name in ['pending_by_kind','reserved_or_running_by_kind','admitted_by_kind']:
            if not isinstance(ad.get(name),dict) or set(ad[name])!={'new','review'} or any(type(v) is not int or v<0 for v in ad[name].values()):
                raise Blocked('Admission counters are unknown: '+name)
        if ad['pending_by_kind']['new'] or ad['reserved_or_running_by_kind']['new'] or any(w['kind']=='new' for w in workers):
            raise Blocked('New queue or new reservations are not empty')
        if any(w['ppid']!=expected_pid for w in workers):raise Blocked('Orphan or foreign native worker')
        queue_name=plan.get('queue_file')
        if queue_name not in {'queue.json','mixed-queue.json'}:raise Blocked('Unknown current queue file')
        queue=required_json(base/queue_name)
        if not isinstance(queue,list):raise Blocked('Current queue is unknown')
        for item in queue:
            if not isinstance(item,dict) or type(item.get('review',False)) is not bool or not isinstance(item.get('source_ids'),list) or not item['source_ids'] or any(not isinstance(i,str) or not i for i in item['source_ids']):
                raise Blocked('Current queue identity inventory is malformed')
        new=[r for r in queue if r.get('review',False) is False]
        if len(new)!=ad['admitted_by_kind']['new']:raise Blocked('Frozen queue and admissions disagree')
        if ad['reserved_or_running_by_kind']['review']!=len(workers):raise Blocked('Native workers and reserved reviews disagree')
        identity={'pid':live[0]['pid'],'started':live[0]['started'],'args':live[0]['args'],'pgid':live[0]['pgid']}
        return {'identity':identity,'workers':workers,'observed_at_unix':self.now(),
                'raw_evidence':{name:encoded(raw(base/name)) for name in ['coordinator.pid','coordinator-run.json','admission-status.json','queue-admission-plan.json',queue_name]}}
    def idle(self,identity,groups):
        rows=self.processes();live,workers=classify(self.root,rows)
        if live:
            if len(live)!=1 or any(live[0][k]!=identity[k] for k in ['pid','started','args','pgid']):raise Blocked('Coordinator identity changed during drain')
            if any(w['ppid']!=identity['pid'] for w in workers):raise Blocked('Orphan worker during drain')
            return False,workers
        if workers or any(r['pgid'] in groups and r['pid']!=identity['pid'] for r in rows):raise Blocked('Native worker/group survived coordinator exit')
        exit_record=required_json(self.root/'runtime/exhaustive/coordinator-exit.json')
        if exit_record.get('pid')!=identity['pid']:return False,[]
        if exit_record.get('exit_code')!=0 or exit_record.get('exit_type') is not None or exit_record.get('stop_requested') is not False or type(exit_record.get('ended_at_unix')) is not int:
            raise Blocked('Natural successful old coordinator exit is unconfirmed')
        return True,[]
    def reconcile(self,pins):
        """Read-only actual gates; pending guarded legal work stays pending."""
        raise Blocked('NOT READY: guarded current reconciliation implementation is absent; no supplied JSON can bypass it')
    def launch(self,folder):
        # Reuse the installed supervisor launch mechanism; no alternate CLI.
        spec=importlib.util.spec_from_file_location('_transfer_supervisor',self.root/'supervise_exhaustive.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        return module.launch(folder)
    def launched(self,folder):
        receipt=required_json(Path(folder)/'launch.json');rows=self.processes();live,workers=classify(self.root,rows)
        pid=receipt.get('pid')
        if len(live)!=1 or live[0]['pid']!=pid:raise Blocked('Launched coordinator is not uniquely adopted')
        if '--recover-new-before-reviews' not in live[0]['args']:raise Blocked('Wrong continuation mode')
        if any(w['ppid']!=pid for w in workers):raise Blocked('Foreign worker after launch')
        return receipt

class Transfer:
    def __init__(self,root,sealed,run_dir,backend=None,timeout=7200):
        self.root=Path(root).resolve();self.sealed=Path(sealed).resolve();self.folder=Path(run_dir).resolve()
        allowed=self.root/'runtime/review-reallocation-transfer-preparation-20261023T0253Z/runs'
        if self.root.name!='legal-rewrite' or not self.folder.is_relative_to(allowed) or self.folder==allowed:
            raise Blocked('Transfer run directory is outside the bounded preparation runtime')
        if self.sealed!=self.root/'runtime/review-reallocation-preflight-20261022T223009Z':
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
            if installing and name in SIX and name in self.state.get('mutations',{}):
                item=self.state['mutations'][name]
                valid=data in {decoded(item['before']),decoded(item['after'])}
            if not valid:raise Conflict('Pinned code/policy/catalogue changed: '+name)
        if installed:
            for name in SIX:
                if sha((self.root/name).read_bytes())!=self.manifest['candidate'][name]['sha256']:raise Conflict('Incomplete six-module group')
    def change(self,name,after):
        if name not in set(SIX)|{HOT,PLAN,DISABLED}:raise Blocked('Mutation target is outside the exact transfer allowlist')
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
            if current.get('workers')!=7 or current.get('role_limits')!={'new':6,'review':1}:raise Blocked('Expected effective seven-worker role control differs')
            paused=copy.deepcopy(current);paused.update(workers=6,role_limits={'new':6,'review':0})
            self.change(HOT,packed(paused))
    def drain(self):
        deadline=self.backend.now()+self.timeout;identity=self.state['entry']['identity']
        groups=set(self.state.get('worker_groups',[]))
        while True:
            self.assert_pins();idle,workers=self.backend.idle(identity,groups)
            groups.update(w['pgid'] for w in workers)
            if sorted(groups)!=self.state.get('worker_groups',[]):self.state['worker_groups']=sorted(groups);self.save()
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
        original.update(workers=7,role_limits={'new':6,'review':1},review_tail_limit=7)
        # A second intended write to the hot control must own the paused bytes.
        item=self.state['mutations'][HOT];desired=packed(original)
        if 'configured_after' not in item:
            item['configured_after']=encoded(desired);self.save()
        if decoded(item['configured_after'])!=desired:raise Conflict('Configured hot-control intent differs')
        current=raw(self.root/HOT)
        if current not in {decoded(item['after']),desired}:raise Conflict('Paused/configured worker control changed')
        if current!=desired:durable(self.root/HOT,desired)
    def run(self,expected_pid):
        self.backend.reconciliation_precondition()
        if self.path.exists():
            self.state=required_json(self.path)
            if self.state.get('root')!=str(self.root) or self.state.get('seal')!=SEAL:raise Blocked('Resume identity differs')
        else:
            # Refuse before any production lock/control/file change.
            entry=self.backend.entry(expected_pid)
            pins=self.backend.baseline_pins(self.manifest)
            self.folder.mkdir(parents=True,exist_ok=True)
            self.state={'owner':str(uuid.uuid4()),'root':str(self.root),'seal':SEAL,'phase':'ELIGIBLE',
                        'entry':entry,'pins':pins,'mutations':{},'events':[],
                        'worker_groups':sorted({w['pgid'] for w in entry['workers']})}
            durable(self.folder/'original-worker-control.json',raw(self.root/HOT));self.save()
        with locked(self.folder/'controller.lock',must_exist=False),locked(self.root/'runtime/supervision/supervisor.lock'):
            phase=self.state['phase']
            if phase=='COMPLETE':return self.state
            if phase in {'ABORTED','ROLLBACK_CONFLICT'}:raise Blocked('Terminal transfer needs a new parent review')
            marker=self.state.get('mutations',{}).get(DISABLED)
            if marker is not None and (marker['before'] is not None or raw(self.root/DISABLED)!=decoded(marker['after'])):
                raise Conflict('Owned durable supervisor pause is missing or was replaced')
            try:
                if phase in {'LAUNCH_INTENT','LAUNCHED'}:
                    if not (self.folder/'launch/launch.json').exists():raise Blocked('Launch outcome is ambiguous; no second launch is allowed')
                    receipt=self.backend.launched(self.folder/'launch')
                    self.state['new_coordinator']=receipt
                    self.restore([DISABLED]);self.phase('COMPLETE')
                    return self.state
                if phase=='ELIGIBLE':
                    hot=self.state.get('mutations',{}).get(HOT)
                    if hot is None or raw(self.root/HOT)!=decoded(hot['after']):
                        again=self.backend.entry(expected_pid)
                        if again['identity']!=self.state['entry']['identity']:raise Blocked('Old process changed before exclusion')
                    self.assert_pins();self.owned_pause();self.close_reviews();self.phase('REVIEW_ADMISSIONS_CLOSED')
                if self.state['phase']=='REVIEW_ADMISSIONS_CLOSED':
                    self.drain();self.phase('NATURALLY_DRAINED')
                with ExitStack() as stack:
                    # No writer/coordinator/manual lock is held while waiting.
                    for name in ['runtime/exhaustive/coordinator.lock','draft-writer.lock','runtime/exhaustive/manual-agent-slots.lock']:
                        stack.enter_context(locked(self.root/name))
                    if self.state['phase'] in {'NATURALLY_DRAINED','RECONCILIATION_REQUIRED'}:
                        idle,_=self.backend.idle(self.state['entry']['identity'],set(self.state.get('worker_groups',[])))
                        if not idle:raise Blocked('Full drain no longer confirmed')
                        self.assert_pins()
                        proof=self.backend.reconcile(self.state['pins'])
                        durable(self.folder/'reconciliation.json',packed(proof))
                        if proof.get('integrity_status')!='reconciled' or proof.get('ambiguities')!=[]:
                            self.phase('RECONCILIATION_REQUIRED');raise Blocked('Unclassified or contradictory reconciliation evidence remains')
                        self.state['reconciliation_sha256']=sha(packed(proof));self.phase('RECONCILED')
                    if self.state['phase']=='RECONCILED':
                        self.group_install();self.phase('SIX_MODULES_INSTALLED')
                    if self.state['phase']=='SIX_MODULES_INSTALLED':
                        self.configure();self.phase('CONFIGURED')
                    self.assert_pins(installed=True)
                    idle,_=self.backend.idle(self.state['entry']['identity'],set(self.state.get('worker_groups',[])))
                    if not idle:raise Blocked('Process appeared before launch')
                # Release the coordinator lock before the existing launcher,
                # while the supervisor exclusion and durable owned pause remain.
                if self.state['phase']=='CONFIGURED':
                    self.phase('LAUNCH_INTENT')
                    launch_dir=self.folder/'launch';launch_dir.mkdir(exist_ok=True)
                    pid=self.backend.launch(launch_dir)
                    self.phase('LAUNCHED',pid=pid)
                elif self.state['phase']=='LAUNCH_INTENT':
                    # Unknown outcome can never become a second launch.
                    if not (self.folder/'launch/launch.json').exists():raise Blocked('Launch outcome is ambiguous; no second launch is allowed')
                    self.phase('LAUNCHED')
                if self.state['phase']=='LAUNCHED':
                    receipt=self.backend.launched(self.folder/'launch')
                    self.state['new_coordinator']=receipt
                    self.restore([DISABLED]);self.phase('COMPLETE')
                return self.state
            except TimeoutError:
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
