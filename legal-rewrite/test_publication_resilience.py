from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase,main
from unittest.mock import patch
from types import ModuleType,SimpleNamespace
from contextlib import redirect_stdout,redirect_stderr
import io,json,subprocess,sys,threading

P=Path(__file__).resolve().parent;LEGAL=P
sys.path.insert(0,str(LEGAL))

def module(name):
    result=ModuleType('proposed_'+name);result.__file__=str(LEGAL/(name+'.py'))
    exec(compile((LEGAL/(name+'.py')).read_text(),result.__file__,'exec'),result.__dict__)
    return result

class Publication(TestCase):
    def setUp(self):
        self.tmp=TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name);self.legal=self.root/'legal-rewrite';self.legal.mkdir()
        self.runtime=self.legal/'runtime';self.runtime.mkdir()
        self.m=module('publish_snapshot');self.calls=[];self.build_failure=None;self.mode='success'
        self.first=next(iter(self.m.PROJECTS))
        for slug,project in self.m.PROJECTS.items():
            folder=self.root/'sites'/slug/'dist';(folder/'.vercel').mkdir(parents=True)
            (folder/'.vercel/project.json').write_text(json.dumps({'projectId':project,'orgId':'team_m7zLS15LnoyaB6RyJ0zKsHYj'}))
        folder=self.root/'sites/liberer-la-retraite/dist/downloads';folder.mkdir()
        (folder/'manifest.json').write_text(json.dumps({'drafted_articles':6934,'source_records':30317}))
        self.marker='FAKE_PRIVATE_VALUE_MUST_NOT_BE_PRINTED'

    def worker(self,command,**kwargs):
        if command[0]!='vercel':
            if self.build_failure==Path(command[1]).name:raise subprocess.CalledProcessError(1,command)
            return SimpleNamespace(returncode=0)
        slug=kwargs['cwd'].parent.name;attempt=1+sum(x==slug for x in self.calls)
        self.assertEqual('--archive=tgz' in command,slug=='liberer-la-retraite')
        self.calls.append(slug)
        self.assertEqual(kwargs['timeout'],900)
        initial=json.loads((self.runtime/'publication.json').read_text())
        self.assertTrue(initial['local_checks_passed'])
        self.assertFalse(initial['all_sites_published'])
        if slug==self.first and self.mode=='timeout_exception' and attempt==1:
            raise subprocess.TimeoutExpired(command,900)
        if slug==self.first and self.mode=='invalid_server_json' and attempt==1:
            kwargs['stdout'].write('Error: FetchError: invalid json response body at https://api.vercel.com/v2/files reason: Unexpected token, "Internal S"... is not valid JSON\n')
            return SimpleNamespace(returncode=1)
        if slug==self.first and (self.mode=='persistent' or self.mode=='timeout_then_success' and attempt==1):
            kwargs['stdout'].write('Error: read ETIMEDOUT '+self.marker+'\n')
            return SimpleNamespace(returncode=1)
        if slug==self.first and self.mode=='auth_failure':
            kwargs['stdout'].write('Authentication failed '+self.marker+'\n')
            return SimpleNamespace(returncode=1)
        kwargs['stdout'].write('Deployment ready\n');return SimpleNamespace(returncode=0)

    def invoke(self,deploy=True):
        output=io.StringIO();db=SimpleNamespace(close=lambda:None)
        with patch.object(self.m,'HERE',self.legal),patch.object(self.m,'open_db',return_value=db),patch.object(self.m,'register'),patch.object(self.m.subprocess,'run',side_effect=self.worker),patch.object(self.m.time,'sleep') as sleep,redirect_stdout(output):
            report=self.m.publish(deploy)
        self.assertNotIn(self.marker,output.getvalue())
        self.assertNotIn(self.marker,json.dumps(report))
        return report,sleep.call_count

    def test_first_timeout_then_success_confirms_all_five(self):
        self.mode='timeout_then_success';report,sleeps=self.invoke()
        self.assertEqual(self.calls.count(self.first),2);self.assertEqual(sleeps,1)
        self.assertTrue(report['all_sites_published']);self.assertFalse(report['publication_pending'])
        self.assertEqual(len(report['deployments']),5)
        self.assertTrue(all(x['published'] for x in report['deployments'].values()))
        self.assertTrue((self.runtime/'last-published.json').exists())

    def test_process_timeout_is_retried_with_the_same_bound(self):
        self.mode='timeout_exception';report,_=self.invoke()
        self.assertTrue(report['all_sites_published'])
        self.assertEqual(report['deployments'][self.first]['attempts'][0]['failure_type'],'TimeoutExpired')

    def test_internal_server_response_retries_without_loosening_validation(self):
        self.mode='invalid_server_json';report,sleeps=self.invoke()
        self.assertTrue(report['all_sites_published'])
        self.assertEqual(self.calls.count(self.first),2);self.assertEqual(sleeps,1)
        self.assertFalse(self.m.NETWORK_ERROR.search('FetchError: invalid json response body at https://api.vercel.com/v2/files: Authentication failed'))
        self.assertTrue(self.m.NETWORK_ERROR.search('FetchError: request failed, reason: write EPIPE'))

    def test_persistent_first_failure_does_not_hide_other_results(self):
        self.mode='persistent';(self.runtime/'last-published.json').write_text('{"edition":"previous"}')
        report,sleeps=self.invoke()
        self.assertEqual(self.calls.count(self.first),3);self.assertEqual(sleeps,2)
        self.assertEqual(len(self.calls),7)
        self.assertTrue(report['publication_pending']);self.assertFalse(report['all_sites_published'])
        self.assertEqual(sum(x['published'] for x in report['deployments'].values()),4)
        self.assertEqual(json.loads((self.runtime/'last-published.json').read_text()),{'edition':'previous'})
        with patch.object(self.m,'publish',return_value=report),patch.object(sys,'argv',['publish_snapshot.py','--deploy']):self.assertEqual(self.m.main(),20)

    def test_non_network_failure_is_not_retried(self):
        self.mode='auth_failure';report,sleeps=self.invoke()
        self.assertEqual(self.calls.count(self.first),1);self.assertEqual(sleeps,0)
        self.assertTrue(report['publication_pending'])

    def test_local_build_validation_is_still_fatal_and_prevents_all_deploys(self):
        self.build_failure='check_downloads.py'
        with self.assertRaises(subprocess.CalledProcessError):self.invoke()
        report=json.loads((self.runtime/'publication.json').read_text())
        self.assertFalse(report['local_checks_passed']);self.assertEqual(report['failure_stage'],'check_downloads.py')
        self.assertEqual(self.calls,[])

    def test_corpus_validation_failure_records_a_report_and_returns_one(self):
        db=SimpleNamespace(close=lambda:None);out=io.StringIO()
        with patch.object(self.m,'HERE',self.legal),patch.object(self.m,'open_db',return_value=db),patch.object(self.m,'register',side_effect=ValueError('Invalid corpus')),patch.object(self.m.subprocess,'run') as worker,patch.object(sys,'argv',['publish_snapshot.py','--deploy']),redirect_stderr(out):
            self.assertEqual(self.m.main(),1)
        worker.assert_not_called()
        report=json.loads((self.runtime/'publication.json').read_text())
        self.assertEqual(report['status'],'local_validation_failed');self.assertEqual(report['failure_stage'],'corpus_validation')

    def test_destination_validation_remains_fatal(self):
        linked=self.root/'sites'/self.first/'dist/.vercel/project.json'
        linked.write_text('{"projectId":"wrong"}')
        with self.assertRaisesRegex(ValueError,'project mismatch'):self.invoke()
        self.assertEqual(self.calls,[])
        self.assertEqual(json.loads((self.runtime/'publication.json').read_text())['failure_stage'],'destination_validation')

    def test_local_only_build_does_not_claim_an_earlier_failed_deploy_was_fixed(self):
        (self.runtime/'publication.json').write_text('{"publication_pending":true}')
        report,_=self.invoke(False)
        self.assertTrue(report['publication_pending']);self.assertFalse(report['all_sites_published'])
        self.assertFalse(report['deployment_requested']);self.assertEqual(self.calls,[])

class Coordinator(TestCase):
    def setUp(self):
        self.tmp=TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name);self.runtime=self.root/'runtime/exhaustive';self.runtime.mkdir(parents=True)
        self.m=module('run_exhaustive')
        self.m.HERE=self.root;self.m.ROOT=self.root;self.m.RUNTIME=self.runtime;self.m.STOP=threading.Event()
        (self.runtime/'status.json').write_text('{"status":"running","drafted_articles":6934}')
        self.report={'local_checks_passed':True,'deployment_requested':True,'publication_pending':True,'all_sites_published':False,
                     'drafted_articles':6934,'deployments':{'failed':{'published':False},'ok':{'published':True}}}

    def call(self,code,deploy=True):
        (self.root/'runtime/publication.json').write_text(json.dumps(self.report))
        with patch.object(self.m.subprocess,'run',return_value=SimpleNamespace(returncode=code)),redirect_stdout(io.StringIO()):return self.m.publish_checkpoint(deploy)

    def test_deployment_only_failure_does_not_stop_drafting_and_is_durable(self):
        self.assertFalse(self.call(20));self.assertFalse(self.m.STOP.is_set())
        state=json.loads((self.runtime/'publication-state.json').read_text())
        self.assertTrue(state['publication_pending']);self.assertEqual(state['failed_sites'],['failed'])
        self.assertEqual(json.loads((self.runtime/'status.json').read_text())['status'],'running')
        fake=SimpleNamespace(execute=lambda *args:[],close=lambda:None)
        with patch.object(self.m,'open_db',return_value=fake):status=self.m.progress({},'running')
        self.assertTrue(status['publication_pending'])

    def test_busy_publisher_defers_without_claiming_validation_or_rewriting_report(self):
        self.report={'status':'validating_local','local_checks_passed':False}
        self.assertFalse(self.call(21))
        self.assertFalse(self.m.STOP.is_set())
        self.assertEqual(json.loads((self.root/'runtime/publication.json').read_text()),self.report)
        self.assertFalse((self.runtime/'publication-state.json').exists())

    def test_local_failure_remains_an_exception_for_the_coordinator(self):
        self.report['local_checks_passed']=False
        with self.assertRaises(subprocess.CalledProcessError):self.call(1)
        self.assertFalse((self.runtime/'publication-state.json').exists())

    def test_unconfirmed_pending_result_cannot_bypass_local_validation(self):
        self.report['local_checks_passed']=False
        with self.assertRaisesRegex(ValueError,'Unconfirmed'):self.call(20)

    def test_confirmed_deployment_clears_pending_without_changing_drafting_status(self):
        self.call(20);self.report.update(publication_pending=False,all_sites_published=True)
        self.assertTrue(self.call(0))
        self.assertFalse(json.loads((self.runtime/'publication-state.json').read_text())['publication_pending'])
        self.assertEqual(json.loads((self.runtime/'status.json').read_text())['status'],'running')

    def test_local_only_export_does_not_clear_pending(self):
        self.call(20);self.assertTrue(self.call(0,False))
        self.assertTrue(json.loads((self.runtime/'publication-state.json').read_text())['publication_pending'])

if __name__=='__main__':main(verbosity=2)
