"""Isolated guard tests; no production database, coordinator, model or API."""
from pathlib import Path
import copy,fcntl,json,tempfile,unittest
import controller as c

class Guards(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
    def tearDown(self):self.temp.cleanup()
    def test_atomic_beforeimage_and_mode(self):
        p=self.root/'code.py';p.write_bytes(b'before');p.chmod(0o640)
        c.replace_exact(p,b'before',b'after');self.assertEqual(p.read_bytes(),b'after');self.assertEqual(p.stat().st_mode&0o777,0o640)
    def test_intervening_write_blocks(self):
        p=self.root/'code.py';p.write_bytes(b'foreign')
        with self.assertRaises(ValueError):c.replace_exact(p,b'before',b'after')
        self.assertEqual(p.read_bytes(),b'foreign')
    def test_foreign_pause_blocks(self):
        p=self.root/'pause';b=c.encoded({'owner':'foreign'});p.write_bytes(b)
        with self.assertRaises(ValueError):c.check_pause(p,b,'ours')
        self.assertEqual(p.read_bytes(),b)
    def test_changed_owned_pause_blocks(self):
        p=self.root/'pause';p.write_bytes(c.encoded({'owner':'ours','changed':1}))
        with self.assertRaises(ValueError):c.check_pause(p,c.encoded({'owner':'ours'}),'ours')
    def test_symlink_is_not_regular_evidence(self):
        p=self.root/'real';p.write_text('x');link=self.root/'link';link.symlink_to(p)
        with self.assertRaises(ValueError):c.raw(link)
    def test_real_locks_prevent_second_owner(self):
        p=self.root/'lock';p.touch()
        with c.hold_locks(self.root,['lock']):
            with self.assertRaises(BlockingIOError):
                with c.hold_locks(self.root,['lock']):pass
        with c.hold_locks(self.root,['lock']):pass
    def test_missing_lock_never_created(self):
        with self.assertRaises(ValueError):
            with c.hold_locks(self.root,['absent']):pass
        self.assertFalse((self.root/'absent').exists())
    def test_exit_identity_birth_and_granularity(self):
        c.bind_exit({'pid':7,'started_at_unix':100},{'pid':7,'exit_code':0,'exit_type':None,'stop_requested':False,'ended_at_unix':104},{'pid':7,'observed_at_unix':104.9},99,True)
    def test_unknown_inventory_never_zero(self):
        with self.assertRaises(ValueError):c.bind_exit({'pid':7,'started_at_unix':100},{'pid':7,'exit_code':0,'exit_type':None,'stop_requested':False,'ended_at_unix':104},{'pid':7,'observed_at_unix':103},99,None)
    def test_old_or_abnormal_exit_blocks(self):
        run={'pid':7,'started_at_unix':100};exit={'pid':7,'exit_code':0,'exit_type':None,'stop_requested':False,'ended_at_unix':104};alive={'pid':7,'observed_at_unix':103}
        for changes in [{'pid':6},{'ended_at_unix':99},{'exit_code':1},{'stop_requested':True}]:
            with self.assertRaises(ValueError):c.bind_exit(run,exit|changes,alive,99,True)
        with self.assertRaises(ValueError):c.bind_exit(run,exit,alive,30,True)
    def test_prompt_change_only(self):
        before='PROMPT="\\nSECONDE PASSE : old"\ndef guard():return 7\n'
        after='PROMPT="\\nSECONDE PASSE — PRIORITÉ HUMAINE new"\ndef guard():return 7\n'
        c.prompt_only(before,after)
        with self.assertRaises(ValueError):c.prompt_only(before,after.replace('return 7','return 0'))
        with self.assertRaises(ValueError):c.prompt_only(before,before)
    def setup_queue(self):
        self.plan={'coordinator_pid':7,'scheduled_by_kind':{'new':0,'review':3}}
        self.admission={'coordinator_pid':7,'action':'review_admissions_paused','reserved_or_running_by_kind':{'new':0,'review':0},'admitted_by_kind':{'new':0,'review':2},'deferred_by_kind':{'new':0,'review':1}}
        self.unattempted={'coordinator_pid':7,'jobs':[{'kind':'review','slug':'x','index':3,'reason':'role_admissions_paused','attempted':False,'accepted':False}]}
        self.metrics=[{'coordinator_pid':7,'kind':'review','slug':'x','index':1,'outcome':'reviewed'},{'coordinator_pid':7,'kind':'review','slug':'x','index':2,'outcome':'deferred'}]
        self.pending={('C','2'),('C','3')}
        self.resolve=lambda m:{('C',str(m['index']))}
    def run_queue(self):return c.partition(self.plan,self.admission,self.unattempted,self.metrics,self.pending,self.resolve)
    def test_exact_queue_partition_and_deferred_preservation(self):
        self.setup_queue();r=self.run_queue();self.assertEqual(r['pending_identities'],2);self.assertEqual(r['failed_identities'],1);self.assertEqual(r['unknown_jobs'],0)
    def test_pending_identity_not_in_queue_blocks(self):
        self.setup_queue();self.pending.add(('C','forgotten'))
        with self.assertRaises(ValueError):self.run_queue()
    def test_replayed_or_duplicate_terminal_blocks(self):
        self.setup_queue();self.metrics.append(copy.deepcopy(self.metrics[0]))
        with self.assertRaises(ValueError):self.run_queue()
    def test_foreign_pid_or_unfinished_queue_blocks(self):
        self.setup_queue();self.admission['coordinator_pid']=6
        with self.assertRaises(ValueError):self.run_queue()
        self.setup_queue();self.admission['reserved_or_running_by_kind']['review']=1
        with self.assertRaises(ValueError):self.run_queue()
    def test_unknown_outcome_or_unattempted_reason_blocks(self):
        self.setup_queue();self.metrics[0]['outcome']='unknown'
        with self.assertRaises(ValueError):self.run_queue()
        self.setup_queue();self.unattempted['jobs'][0]['reason']='unexpected'
        with self.assertRaises(ValueError):self.run_queue()
    def test_count_only_is_not_sufficient(self):
        self.setup_queue();self.resolve=lambda m:{('C','2')}
        with self.assertRaises(ValueError):self.run_queue()
    def test_durable_intention_cannot_be_overwritten(self):
        p=self.root/'intent';c.durable(p,b'first')
        with self.assertRaises(FileExistsError):c.durable(p,b'overwritten')
        self.assertEqual(p.read_bytes(),b'first')

if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Guards)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    out={'tests_run':result.testsRun,'success':result.wasSuccessful(),'failures':len(result.failures),'errors':len(result.errors),'production_database_or_model_used':False,'models_launched':0,'test_root':'isolated temporary directories only'}
    c.durable(Path(__file__).resolve().parent/'tests.json',c.encoded(out))
    raise SystemExit(0 if result.wasSuccessful() else 1)
