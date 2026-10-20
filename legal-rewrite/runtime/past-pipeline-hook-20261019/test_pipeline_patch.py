"""Offline integration checks against the proposal, without applying the patch."""
from pathlib import Path
import contextlib, io, json, subprocess, sys, tempfile, tomllib, types, unittest
from unittest.mock import patch

FOLDER=Path(__file__).resolve().parent
LEGAL=FOLDER.parents[1]
sys.path.insert(0,str(LEGAL))
import past_memory
from test_past_sync import SyncContracts

def module():
    value=types.ModuleType('proposed_run_exhaustive')
    value.__file__=str(LEGAL/'run_exhaustive.py')
    exec(compile((FOLDER/'run_exhaustive.proposed.py.txt').read_text(),value.__file__,'exec'),value.__dict__)
    return value

class PipelinePatch(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name);self.setup=self.root/'past-setup';self.setup.mkdir()
        self.server=self.root/'past_memory_mcp.py';self.server.write_text('# test fixture\n')
        self.m=module();self.m.HERE=self.root;self.m.RUNTIME=self.root/'runtime'
        self.addCleanup(patch.stopall)
        patch('past_memory.key_from_environment',side_effect=AssertionError('Unexpected credential access')).start()

    def enabled(self):
        (self.setup/'integration.json').write_text(json.dumps({'enabled':True,'recall_mode':'only_when_useful'}))

    @staticmethod
    def config(options):
        result={}
        for i in range(0,len(options),2):
            if options[i]!='-c':raise AssertionError('Missing repeatable config flag')
            key,body=options[i+1].split('=',1)
            result[key]=tomllib.loads('value='+body)['value']
        return result

    def test_absent_setup_is_offline_and_admin_server_is_disabled(self):
        with patch.object(self.m.subprocess,'run',side_effect=AssertionError('Unexpected subprocess')):
            cfg=self.config(self.m.past_before_job())
        self.assertIs(cfg['mcp_servers.past.enabled'],False)
        self.assertIs(cfg['mcp_servers.legal_rewrite_memory.enabled'],False)

    def test_activation_requires_boolean_true_and_exact_on_demand_mode(self):
        values=[[],{}, {'enabled':True}, {'enabled':'true','recall_mode':'only_when_useful'},
                {'enabled':True,'recall_mode':'always'}, {'enabled':False,'recall_mode':'only_when_useful'}]
        with patch.object(self.m.subprocess,'run',side_effect=AssertionError('Unexpected subprocess')):
            for value in values:
                with self.subTest(value=value):
                    (self.setup/'integration.json').write_text(json.dumps(value))
                    self.assertFalse(self.m.past_job_enabled())
                    self.m.past_before_job()

    def test_invalid_or_unreadable_json_is_nonblocking_and_offline(self):
        (self.setup/'integration.json').write_text('{invalid')
        self.assertFalse(self.m.past_job_enabled())
        with patch.object(Path,'read_text',side_effect=PermissionError('unavailable')):
            self.assertFalse(self.m.past_job_enabled())

    def test_enabled_hook_is_changed_updates_only_and_silences_output(self):
        self.enabled()
        with patch.object(self.m.subprocess,'run',return_value=subprocess.CompletedProcess([],0)) as run:
            cfg=self.config(self.m.past_before_job())
        call=run.call_args
        self.assertEqual(call.args[0][:2],[sys.executable,'-c'])
        self.assertIn('Synchronizer as SyncEngine',call.args[0][2])
        self.assertIn('.run("updates")',call.args[0][2])
        self.assertNotIn('recall',call.args[0][2])
        for stream in ['stdin','stdout','stderr']:self.assertEqual(call.kwargs[stream],subprocess.DEVNULL)
        self.assertEqual(call.kwargs['timeout'],30)
        self.assertTrue(call.kwargs['check'])
        local=cfg['mcp_servers.legal_rewrite_memory']
        self.assertEqual(local['command'],sys.executable)
        self.assertEqual(local['args'],[str(self.server)])
        self.assertEqual(local['enabled_tools'],['past_recall'])
        self.assertIs(local['enabled'],True)
        self.assertIs(local['required'],False)
        self.assertFalse(cfg['mcp_servers.past.enabled'])

    def test_sync_failure_and_timeout_leave_optional_recall_and_drafting_available(self):
        self.enabled()
        errors=[RuntimeError('Sensitive exception body must not be printed'),
                subprocess.CalledProcessError(1,['placeholder']),
                subprocess.TimeoutExpired(['placeholder'],30)]
        for error in errors:
            with self.subTest(type=type(error).__name__), contextlib.redirect_stdout(io.StringIO()) as out:
                with patch.object(self.m.subprocess,'run',side_effect=error):
                    cfg=self.config(self.m.past_before_job())
                self.assertTrue(cfg['mcp_servers.legal_rewrite_memory']['enabled'])
                self.assertNotIn('Sensitive exception',out.getvalue())
                self.assertNotIn('placeholder',out.getvalue())
                self.assertIn('continuing with local sources',out.getvalue())

    def test_missing_local_server_does_not_fall_back_to_account_server(self):
        self.enabled();self.server.unlink()
        with patch.object(self.m.subprocess,'run',return_value=subprocess.CompletedProcess([],0)),contextlib.redirect_stdout(io.StringIO()):
            cfg=self.config(self.m.past_before_job())
        self.assertFalse(cfg['mcp_servers.past.enabled'])
        self.assertFalse(cfg['mcp_servers.legal_rewrite_memory.enabled'])
        self.assertNotIn('mcp_servers.legal_rewrite_memory',cfg)

    def fixture(self):
        # Reuse the tested approved-scope fixture. All clients are fakes.
        value=SyncContracts(methodName='test_initial_reuses_completed_ten_ids_and_only_sends_sixteen_changed_bodies')
        value.setUp();self.addCleanup(value.doCleanups);value.finish_initial()
        value.fake.calls=[];value.created=0
        return value

    def test_real_unchanged_engine_does_not_construct_client_or_make_requests(self):
        self.enabled();fixture=self.fixture();results=[]
        def run(*args,**kwargs):
            results.append(fixture.runner().run('updates'))
            return subprocess.CompletedProcess(args[0],0)
        with patch.object(self.m.subprocess,'run',side_effect=run):self.m.past_before_job()
        self.assertEqual(results,[{'status':'unchanged','changed_sources':0}])
        self.assertEqual(fixture.created,0)
        self.assertEqual(fixture.fake.calls,[])

    def test_real_changed_engine_sends_only_changed_approved_source_and_never_recalls(self):
        self.enabled();fixture=self.fixture();fixture.change_policy()
        def run(*args,**kwargs):
            result=fixture.runner().run('updates');self.assertEqual(result['changed_sources'],1)
            return subprocess.CompletedProcess(args[0],0)
        with patch.object(self.m.subprocess,'run',side_effect=run):self.m.past_before_job()
        self.assertEqual(len(fixture.posts()),1)
        self.assertEqual([r['id'] for r in fixture.posts()[0]['items']],['policy-section0'])
        self.assertFalse(any('recall' in path for _,path,_ in fixture.fake.calls))

    def test_every_exec_attempt_gets_overrides_and_sync_runs_once_per_job(self):
        # All three agent invocations fail in a temporary folder: no corpus write.
        expected=[{'code_id':'code','source_id':'id','source_sha256':'sha','number':'L1','source_xml':'<p>Original</p>'}]
        for file in ['site-summaries.json','policy-coordinations.json']:(self.root/file).write_text('{}')
        class DB:
            def execute(self,*args):return []
            def close(self):pass
        options=['-c','mcp_servers.past.enabled=false','-c','mcp_servers.legal_rewrite_memory.enabled=false']
        with patch.object(self.m,'open_db',return_value=DB()),patch.object(self.m,'progress'), \
             patch.object(self.m,'past_before_job',return_value=options) as before, \
             patch.object(self.m.subprocess,'run',return_value=subprocess.CompletedProcess([],1)) as run, \
             contextlib.redirect_stdout(io.StringIO()):
            self.m.run_job(('test',1,expected),'codex',{})
        self.assertEqual(before.call_count,1)
        self.assertEqual(run.call_count,3)
        for call in run.call_args_list:self.assertEqual(call.args[0][0:6],['codex','exec',*options])

    def test_already_completed_job_never_syncs_or_invokes_agent(self):
        expected=[{'code_id':'code','source_id':'id','source_sha256':'sha'}]
        class DB:
            def execute(self,*args):return [('code','id','sha','rewrite_draft','<p>Done</p>')]
            def close(self):pass
        with patch.object(self.m,'open_db',return_value=DB()), \
             patch.object(self.m,'past_before_job',side_effect=AssertionError('Skipped job synced')), \
             patch.object(self.m.subprocess,'run',side_effect=AssertionError('Skipped job invoked')), \
             contextlib.redirect_stdout(io.StringIO()):
            self.m.run_job(('test',1,expected),'codex',{})

if __name__=='__main__':unittest.main()
