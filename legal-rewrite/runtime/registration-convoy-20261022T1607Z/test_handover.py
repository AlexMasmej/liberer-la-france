from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase,main
from unittest.mock import patch,Mock
from contextlib import ExitStack,redirect_stdout
import io,json,hashlib
import activate


class Handover(TestCase):
    def setUp(self):
        self.temp=TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.here=Path(self.temp.name)/'legal-rewrite';self.runtime=self.here/'runtime/exhaustive'
        self.folder=self.here/'runtime/proof';self.supervision=self.here/'runtime/supervision'
        for p in [self.runtime,self.folder/'implementation',self.folder/'before',self.supervision]:p.mkdir(parents=True,exist_ok=True)
        self.write(self.here/'runner.py','old source',raw=True)
        self.write(self.folder/'implementation/runner.py','new source',raw=True)
        self.write(self.folder/'baseline.json',{'files':{'runner.py':activate.sha(self.here/'runner.py')},'coordinator_pid':12})
        self.write(self.folder/'checks.json',{'all_passed':True,'activation_sha256':activate.sha(Path(activate.__file__)),'implementation_sha256':{'runner.py':activate.sha(self.folder/'implementation/runner.py')},'activate_files':['runner.py']})
        self.write(self.runtime/'coordinator-run.json',{'pid':12})
        self.write(self.runtime/'status.json',{'status':'running','failure':None})
        self.write(self.runtime/'model-policy.json',{'model':'gpt-6-astra','reasoning_effort':'medium'})
        self.write(self.runtime/'parallelism-plan.json',{'capacity':8,'current_workers':8,'target_workers':8,'role_limits':{'new':6,'review':2}})
        self.write(self.runtime/'worker-limit.json',{'workers':7,'role_limits':{'new':6,'review':1}})
        self.write(self.runtime/'manual-agent-slots.json',[])
        self.write(self.here/'runtime/second-pass-parallelism-latest.json',{'pid':12,'execution_verified':True})
        self.rows=[{'kind':'coordinator','pid':12,'ppid':1},{'kind':'worker','pid':34,'ppid':12,'job':'valid-job'}]
        self.drained=False
        self.stack=ExitStack();self.addCleanup(self.stack.close)
        for name,value in [('FOLDER',self.folder),('HERE',self.here),('RUNTIME',self.runtime),('SUPERVISION',self.supervision)]:
            self.stack.enter_context(patch.object(activate,name,value))
        self.kill=self.stack.enter_context(patch.object(activate.os,'kill',side_effect=self.signal))
        self.launch=self.stack.enter_context(patch.object(activate.subprocess,'Popen',return_value=Mock(pid=99)))
        self.stack.enter_context(patch.object(activate,'inventory',side_effect=lambda:[] if self.drained else list(self.rows)))
        self.stack.enter_context(patch.object(activate,'coordinator_unlocked',return_value=True))
        self.stack.enter_context(redirect_stdout(io.StringIO()))

    def write(self,path,value,raw=False):path.write_text(value if raw else json.dumps(value))
    def read(self,path):return json.loads(path.read_text())

    def signal(self,pid,signum):
        self.assertEqual(pid,12,'Only the coordinator may receive the existing drain request')
        self.assertEqual((self.here/'runner.py').read_text(),'old source')
        self.assertEqual(self.read(self.runtime/'worker-limit.json'),{'workers':7,'role_limits':{'new':6,'review':1}})
        self.drained=True
        self.write(self.runtime/'coordinator-exit.json',{'pid':12,'exit_code':0,'stop_requested':True})
        self.write(self.runtime/'status.json',{'status':'checkpoint','failure':None})

    def run_handover(self,apply=True):
        with patch.object(activate.sys,'argv',['activate.py']+(['--apply'] if apply else [])):activate.main()

    def test_dry_run_cannot_signal_copy_or_launch(self):
        self.run_handover(False)
        self.kill.assert_not_called();self.launch.assert_not_called()
        self.assertEqual((self.here/'runner.py').read_text(),'old source')

    def test_new_configuration_and_launch_follow_a_successful_drained_exit(self):
        self.run_handover()
        self.assertEqual(self.kill.call_count,1)
        self.assertEqual((self.here/'runner.py').read_text(),'new source')
        self.assertEqual(self.read(self.runtime/'worker-limit.json'),{'workers':7,'role_limits':{'new':6,'review':1}})
        self.assertEqual(self.read(self.runtime/'parallelism-plan.json')['role_limits'],{'new':6,'review':2})
        self.launch.assert_called_once()
        self.assertEqual(self.launch.call_args.args[0][4],'8')
        self.assertTrue((self.folder/'before/drained-exit.json').exists())

    def test_active_work_timeout_never_changes_code_or_capacity_or_kills_workers(self):
        self.kill.side_effect=lambda *_:None
        with patch.object(activate.time,'monotonic',side_effect=[0,5401,5401]):
            with self.assertRaises(TimeoutError):self.run_handover()
        self.launch.assert_not_called()
        self.assertEqual((self.here/'runner.py').read_text(),'old source')
        self.assertEqual(self.read(self.runtime/'worker-limit.json'),{'workers':7,'role_limits':{'new':6,'review':1}})
        self.assertEqual([call.args[0] for call in self.kill.call_args_list],[12])

    def test_code_drift_is_blocking_before_any_process_action(self):
        (self.here/'runner.py').write_text('concurrent change')
        with self.assertRaises(ValueError):self.run_handover()
        self.kill.assert_not_called();self.launch.assert_not_called()

    def test_a_blocked_exit_is_not_relaunched_or_reclassified(self):
        original=self.signal
        def blocked(pid,signum):
            original(pid,signum)
            self.write(self.runtime/'status.json',{'status':'blocked','failure':'usage limit'})
        self.kill.side_effect=blocked
        with self.assertRaises(ValueError):self.run_handover()
        self.launch.assert_not_called()
        self.assertEqual((self.here/'runner.py').read_text(),'old source')


    def test_transient_inventory_timeout_keeps_old_code_until_fresh_empty_inventory(self):
        inv=self.rows.copy();calls=[inv,inv,activate.subprocess.TimeoutExpired('ps',15),[]]
        with patch.object(activate,'inventory',side_effect=calls),patch.object(activate.time,'sleep'):
            self.run_handover()
        self.assertEqual(self.kill.call_count,1)
        self.launch.assert_called_once()
        self.assertEqual((self.here/'runner.py').read_text(),'new source')

    def test_unconfirmed_inventory_deadline_never_installs_or_launches(self):
        inv=self.rows.copy()
        with patch.object(activate,'inventory',side_effect=[inv,inv,activate.subprocess.TimeoutExpired('ps',15)]),patch.object(activate.time,'sleep'),patch.object(activate.time,'monotonic',side_effect=[0,0,1,5401]):
            with self.assertRaises(TimeoutError):self.run_handover()
        self.launch.assert_not_called()
        self.assertEqual((self.here/'runner.py').read_text(),'old source')
        self.assertEqual(self.kill.call_count,1)


if __name__=='__main__':main()
