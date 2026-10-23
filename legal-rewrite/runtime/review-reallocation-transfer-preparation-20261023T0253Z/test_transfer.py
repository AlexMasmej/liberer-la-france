"""Synthetic transfer tests. No production collector, model, CLI or process runs."""
from contextlib import contextmanager
from pathlib import Path
import copy,fcntl,hashlib,json,shutil,sqlite3,tempfile,unittest
from unittest.mock import patch
import transfer_controller as t

HERE=Path(__file__).resolve().parent
PROJECT=HERE.parents[1]
SEALED=PROJECT/'runtime/review-reallocation-preflight-20261022T223009Z'

class FixtureBackend(t.NativeBackend):
    def __init__(self,root):
        super().__init__(root);self.clock=1000.;self.old=True;self.new=None
        self.launches=0;self.waits=0;self.forever=False;self.on_wait=None;self.after_launch=None
        self.new_lock=None;self.collects=0
    def reconciliation_precondition(self):
        # This is a test-only backend, never a production certificate adapter.
        if not str(self.root).startswith(tempfile.gettempdir()):raise AssertionError('Fixture root escaped temporary directory')
        with sqlite3.connect(self.root/'fixture.sqlite') as db:
            assert db.execute('PRAGMA quick_check').fetchone()==('ok',)
    def now(self):return self.clock
    def processes(self):
        if self.new is not None:
            return [{'pid':self.new,'ppid':1,'pgid':self.new,'started':'new synthetic',
                     'args':['python3',str(self.root/'run_exhaustive.py'),'--recover-new-before-reviews']}]
        if self.old:
            return [{'pid':3122,'ppid':1,'pgid':3122,'started':'old synthetic',
                     'args':['python3',str(self.root/'run_exhaustive.py'),'--interleave-review']}]
        return [{'pid':999,'ppid':1,'pgid':999,'started':'unrelated synthetic','args':['unrelated']}]
    def baseline_pins(self,manifest):
        names=set(manifest['baseline'])|{t.POLICIES[-1]}
        return {n:t.sha((self.root/n).read_bytes()) for n in names}
    def wait(self,seconds):
        self.waits+=1;self.clock+=seconds
        # These three locks must remain free throughout the drain wait.
        for name in ['draft-writer.lock','runtime/exhaustive/coordinator.lock','runtime/exhaustive/manual-agent-slots.lock']:
            with t.locked(self.root/name):pass
        if self.on_wait:self.on_wait()
        if not self.forever:
            self.old=False
            t.durable(self.root/'runtime/exhaustive/coordinator-exit.json',t.packed({
                'pid':3122,'ended_at_unix':1001,'exit_code':0,'exit_type':None,'stop_requested':False}))
    def reconcile(self,pins):
        self.collects+=1
        # Actual tiny DB/owner/registry equality, not a supplied JSON approval.
        with sqlite3.connect((self.root/'fixture.sqlite').as_uri()+'?mode=ro',uri=True) as db:
            rows=db.execute('SELECT source_id,body FROM articles ORDER BY source_id').fetchall()
        batch=t.required_json(self.root/'fixture-batch.json')
        registry=t.required_json(self.root/'fixture-registry.json')
        if rows!=[(r['source_id'],r['body']) for r in batch] or registry!={r['source_id']:t.sha(r['body'].encode()) for r in batch}:
            return {'integrity_status':'contradictory','ambiguities':['fixture_owner_db_or_registry_mismatch']}
        return {'integrity_status':'reconciled','ambiguities':[],
                'fixture_digest':t.sha(t.packed(rows)),
                'pending_reference_work':[{'source_id':'A','status':'pending_not_claimed_current'}]}
    def launch(self,folder):
        self.launches+=1;self.new=9123
        self.new_lock=(self.root/'runtime/exhaustive/coordinator.lock').open('r+')
        fcntl.flock(self.new_lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        receipt={'pid':self.new,'command':['python3',str(self.root/'run_exhaustive.py'),'--recover-new-before-reviews'],'launched_at_unix':self.clock}
        t.durable(folder/'launch.json',t.packed(receipt))
        if self.after_launch:self.after_launch()
        return self.new

class TransferTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='transfer-isolated-');self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)/'legal-rewrite';self.root.mkdir()
        self.sealed=self.root/'runtime/review-reallocation-preflight-20261022T223009Z'
        self.sealed.mkdir(parents=True)
        shutil.copy2(SEALED/'manifest.json',self.sealed/'manifest.json')
        shutil.copytree(SEALED/'candidate',self.sealed/'candidate')
        for name in t.sealed_package(self.sealed)['baseline']:
            shutil.copy2(SEALED/'baseline'/name,self.root/name)
        self.prep=self.root/'runtime/review-reallocation-transfer-preparation-20261023T0253Z'
        self.prep.mkdir();self.run_dir=self.prep/'runs/case'
        for name in ['runtime/exhaustive/coordinator.lock','runtime/exhaustive/manual-agent-slots.lock','runtime/supervision/supervisor.lock','draft-writer.lock']:
            path=self.root/name;path.parent.mkdir(parents=True,exist_ok=True);path.touch()
        self.base=self.root/'runtime/exhaustive'
        t.durable(self.base/'coordinator.pid',b'3122')
        t.durable(self.base/'coordinator-run.json',t.packed({'pid':3122}))
        t.durable(self.base/'admission-status.json',t.packed({'coordinator_pid':3122,'updated_at_unix':1000,
            'pending_by_kind':{'new':0,'review':100},'reserved_or_running_by_kind':{'new':0,'review':0},
            'admitted_by_kind':{'new':1,'review':0}}))
        t.durable(self.base/'queue-admission-plan.json',t.packed({'coordinator_pid':3122,'queue_file':'mixed-queue.json'}))
        t.durable(self.base/'mixed-queue.json',t.packed([{'slug':'synthetic','index':1,'review':False,'source_ids':['A']}]))
        t.durable(self.base/'manual-agent-slots.json',b'[]\n')
        self.hot=b'{"workers":7,"role_limits":{"new":6,"review":1},"preserve":"exact bytes"}\n'
        t.durable(self.root/t.HOT,self.hot)
        t.durable(self.root/t.PLAN,t.packed({'capacity':8,'current_workers':8,'role_limits':{'new':6,'review':2},'model':'UNCHANGED'}))
        t.durable(self.base/'model-policy.json',t.packed({'model':'gpt-6-astra','reasoning_effort':'medium'}))
        db=sqlite3.connect(self.root/'fixture.sqlite');db.execute('CREATE TABLE articles(source_id TEXT,body TEXT)')
        db.execute('INSERT INTO articles VALUES(?,?)',('A','Complete synthetic text.'));db.commit();db.close()
        t.durable(self.root/'fixture-batch.json',t.packed([{'source_id':'A','body':'Complete synthetic text.'}]))
        t.durable(self.root/'fixture-registry.json',t.packed({'A':t.sha(b'Complete synthetic text.')}))
        self.backend=FixtureBackend(self.root)
        self.original={name:t.raw(self.root/name) for name in set(t.SIX)|{t.HOT,t.PLAN,t.DISABLED}}
    def tearDown(self):
        if self.backend.new_lock:self.backend.new_lock.close()
    def controller(self,kind=t.Transfer,timeout=2):return kind(self.root,self.sealed,self.run_dir,self.backend,timeout)
    def state(self):return t.required_json(self.run_dir/'state.json')
    def same_original(self,names):
        for name in names:self.assertEqual(t.raw(self.root/name),self.original[name],name)

    def test_native_backend_hard_blocks_before_any_production_collector_or_mutation(self):
        native=t.NativeBackend(self.root)
        with patch.object(native,'processes',side_effect=AssertionError('No production preflight allowed')):
            with self.assertRaisesRegex(t.Blocked,'NOT READY'):t.Transfer(self.root,self.sealed,self.run_dir,native).run(3122)
        self.assertFalse(self.run_dir.exists());self.same_original(t.SIX+(t.HOT,t.PLAN,t.DISABLED))

    def test_real_entry_collector_refuses_new_queue_reserved_stale_unknown_and_pid(self):
        original=t.required_json(self.base/'admission-status.json')
        variants=[original|{'pending_by_kind':{'new':43,'review':100}},
                  original|{'reserved_or_running_by_kind':{'new':6,'review':0}},
                  original|{'updated_at_unix':1},original|{'updated_at_unix':None},
                  original|{'coordinator_pid':999},original|{'pending_by_kind':{}}]
        for value in variants:
            t.durable(self.base/'admission-status.json',t.packed(value))
            with self.subTest(value=value),self.assertRaises(t.Blocked):self.controller().run(3122)
            self.assertFalse(self.run_dir.exists());self.same_original([t.HOT,t.DISABLED])
        t.durable(self.base/'admission-status.json',t.packed(original))
        self.assertEqual(self.backend.entry(3122)['identity']['pid'],3122)
        with self.assertRaises(t.Blocked):self.backend.entry(999)
        with self.assertRaises(t.Blocked):t.parse_processes('')

    def test_preexisting_pause_and_foreign_pause_are_never_overwritten(self):
        t.durable(self.root/t.DISABLED,b'operator pause\n')
        with self.assertRaisesRegex(t.Blocked,'pre-existing'):self.controller().run(3122)
        self.assertEqual(t.raw(self.root/t.DISABLED),b'operator pause\n');self.assertEqual(t.raw(self.root/t.HOT),self.hot)

    def test_run_directory_and_lock_symlinks_are_rejected(self):
        with self.assertRaises(t.Blocked):t.Transfer(self.root,self.sealed,self.root/'arbitrary',self.backend)
        target=self.root/'runtime/exhaustive/manual-agent-slots.lock';target.unlink();target.symlink_to(self.root/'draft-writer.lock')
        with self.assertRaisesRegex(t.Blocked,'non-symlink'):self.controller().run(3122)

    def test_success_drains_without_writer_lock_installs_exact_six_and_launches_once(self):
        result=self.controller().run(3122)
        self.assertEqual(result['phase'],'COMPLETE');self.assertGreater(self.backend.waits,0)
        self.assertEqual(self.backend.launches,1);self.assertFalse((self.root/t.DISABLED).exists())
        for name in t.SIX:self.assertEqual((self.root/name).read_bytes(),(self.sealed/'candidate'/name).read_bytes())
        hot=t.required_json(self.root/t.HOT)
        self.assertEqual(hot['role_limits'],{'new':6,'review':1});self.assertEqual(hot['workers'],7);self.assertEqual(hot['review_tail_limit'],7)
        plan=t.required_json(self.root/t.PLAN);self.assertEqual(plan['role_limits'],{'new':6,'review':2});self.assertEqual(plan['model'],'UNCHANGED')
        self.assertEqual(self.controller().run(3122)['phase'],'COMPLETE');self.assertEqual(self.backend.launches,1)

    def test_timeout_restores_only_owned_exact_bytes_and_never_signals(self):
        self.backend.forever=True
        with self.assertRaises(TimeoutError):self.controller(timeout=.3).run(3122)
        self.assertEqual(self.state()['phase'],'ABORTED');self.assertEqual(self.backend.launches,0)
        self.same_original(t.SIX+(t.HOT,t.PLAN,t.DISABLED))

    def test_timeout_does_not_remove_pause_if_worker_control_was_changed(self):
        self.backend.forever=True
        intervening=b'{"workers":1,"operator":"intervened"}'
        self.backend.on_wait=lambda:t.durable(self.root/t.HOT,intervening)
        with self.assertRaises(t.Conflict):self.controller(timeout=.3).run(3122)
        self.assertEqual(t.raw(self.root/t.HOT),intervening);self.assertTrue((self.root/t.DISABLED).exists())
        self.assertEqual(self.state()['phase'],'ROLLBACK_CONFLICT');self.assertEqual(self.backend.launches,0)

    def test_contradictory_fixture_reconciliation_keeps_pause_and_does_not_install(self):
        t.durable(self.root/'fixture-registry.json',b'{}')
        with self.assertRaisesRegex(t.Blocked,'reconciliation'):self.controller().run(3122)
        self.assertEqual(self.state()['phase'],'RECONCILIATION_REQUIRED');self.assertTrue((self.root/t.DISABLED).exists())
        self.same_original(t.SIX);self.assertEqual(self.backend.launches,0)

    def test_interruption_mid_group_resumes_owned_before_after_without_loading_modules(self):
        class InterruptGroup(t.Transfer):
            def change(self,name,after):
                super().change(name,after)
                if name=='review_lanes.py':raise KeyboardInterrupt('Synthetic mid-install interruption')
        with self.assertRaises(KeyboardInterrupt):self.controller(InterruptGroup).run(3122)
        self.assertEqual(self.state()['phase'],'RECONCILED');self.assertTrue((self.root/t.DISABLED).exists())
        self.assertEqual(self.controller().run(3122)['phase'],'COMPLETE');self.assertEqual(self.backend.launches,1)

    def test_group_failure_rolls_back_exact_group_and_does_not_launch(self):
        class FailGroup(t.Transfer):
            def change(self,name,after):
                super().change(name,after)
                if name=='review_lanes.py':raise OSError('Synthetic replace failure')
        with self.assertRaises(OSError):self.controller(FailGroup).run(3122)
        self.same_original(t.SIX);self.assertTrue((self.root/t.DISABLED).exists());self.assertEqual(self.backend.launches,0)

    def test_interruption_after_hot_configuration_intent_resumes_paused_or_configured(self):
        class InterruptConfigure(t.Transfer):
            def save(self):
                super().save()
                item=self.state.get('mutations',{}).get(t.HOT,{})
                if 'configured_after' in item and t.raw(self.root/t.HOT)==t.decoded(item['after']):
                    raise KeyboardInterrupt('Synthetic journal-before-hot-write interruption')
        with self.assertRaises(KeyboardInterrupt):self.controller(InterruptConfigure).run(3122)
        self.assertEqual(self.state()['phase'],'SIX_MODULES_INSTALLED')
        self.assertEqual(t.required_json(self.root/t.HOT)['workers'],6)
        self.assertEqual(self.controller().run(3122)['phase'],'COMPLETE');self.assertEqual(self.backend.launches,1)

    def test_resume_launched_adopts_unique_pid_without_taking_new_coordinator_lock(self):
        class InterruptLaunched(t.Transfer):
            def phase(self,name,**evidence):
                super().phase(name,**evidence)
                if name=='LAUNCHED':raise KeyboardInterrupt('Synthetic post-launch interruption')
        with self.assertRaises(KeyboardInterrupt):self.controller(InterruptLaunched).run(3122)
        self.assertEqual(self.state()['phase'],'LAUNCHED');self.assertIsNotNone(self.backend.new_lock)
        self.assertEqual(self.controller().run(3122)['phase'],'COMPLETE');self.assertEqual(self.backend.launches,1)

    def test_resume_launch_intent_with_receipt_adopts_without_relaunch(self):
        self.backend.after_launch=lambda:(_ for _ in ()).throw(KeyboardInterrupt('Synthetic Popen/receipt boundary'))
        with self.assertRaises(KeyboardInterrupt):self.controller().run(3122)
        self.assertEqual(self.state()['phase'],'LAUNCH_INTENT')
        self.assertEqual(self.controller().run(3122)['phase'],'COMPLETE');self.assertEqual(self.backend.launches,1)

    def test_ambiguous_launch_without_receipt_never_starts_second_coordinator(self):
        def missing_receipt():
            (self.run_dir/'launch/launch.json').unlink();raise KeyboardInterrupt('Synthetic unknown launch outcome')
        self.backend.after_launch=missing_receipt
        with self.assertRaises(KeyboardInterrupt):self.controller().run(3122)
        with self.assertRaisesRegex(t.Blocked,'ambiguous'):self.controller().run(3122)
        self.assertEqual(self.backend.launches,1);self.assertTrue((self.root/t.DISABLED).exists())

    def test_intervening_code_policy_or_pause_blocks_resume_without_overwrite(self):
        class InterruptGroup(t.Transfer):
            def change(self,name,after):
                super().change(name,after)
                if name=='review_lanes.py':raise KeyboardInterrupt('Synthetic interruption')
        with self.assertRaises(KeyboardInterrupt):self.controller(InterruptGroup).run(3122)
        t.durable(self.root/'review_lanes.py',b'operator changed code')
        with self.assertRaises(t.Conflict):self.controller().run(3122)
        self.assertEqual(t.raw(self.root/'review_lanes.py'),b'operator changed code');self.assertEqual(self.backend.launches,0)
        t.durable(self.root/t.DISABLED,b'operator now owns pause')
        with self.assertRaisesRegex(t.Conflict,'pause'):self.controller().run(3122)
        self.assertEqual(t.raw(self.root/t.DISABLED),b'operator now owns pause')

if __name__=='__main__':unittest.main(verbosity=2)
