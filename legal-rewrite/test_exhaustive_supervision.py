from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase,main
from unittest.mock import patch
import fcntl,json,subprocess,sys,os
import hashlib,io,threading,time
from contextlib import redirect_stdout
from types import SimpleNamespace
from ingest import open_db
import supervise_exhaustive as supervisor
import run_exhaustive as coordinator
from test_execution_fixture import emit_cli_startup


class Decisions(TestCase):
    def decide(self,status=None,live=None,workers=None,locked=False,previous=None,held=None,now=100,reference_pending=0):
        return supervisor.action(status or {'pending':100,'prior_drafts_awaiting_review':10},
                                 live or [],workers or [],locked,previous or {},held or [],now,reference_pending)[0]

    def test_live_coordinator_is_adopted(self):
        self.assertEqual(self.decide(live=[{'pid':92516}]),'monitoring')

    def test_lock_prevents_duplicate_even_without_visible_pid(self):
        self.assertEqual(self.decide(locked=True),'waiting_for_lock')

    def test_orphans_do_not_get_overlapping_replacements(self):
        self.assertEqual(self.decide(workers=[{'pid':8}]),'orphan_workers')

    def test_disappearance_with_unprocessed_articles_restarts(self):
        self.assertEqual(self.decide(),'restart')

    def test_validation_failure_remains_blocking(self):
        self.assertEqual(self.decide(status={'status':'blocked','failure':'Invalid frozen reference','pending':100}),'needs_attention')

    def test_quota_does_not_loop_every_minute(self):
        self.assertEqual(self.decide(status={'status':'blocked','failure':'Codex authentication or usage limit','pending':100}),'needs_attention')

    def test_zero_pending_is_only_awaiting_final_audit(self):
        self.assertEqual(self.decide(status={'pending':0,'prior_drafts_awaiting_review':0}),'awaiting_final_audit')

    def test_zero_pending_does_not_discard_unreviewed_proposals(self):
        self.assertEqual(self.decide(status={'pending':0,'prior_drafts_awaiting_review':12}),'restart')

    def test_empty_drafting_queue_with_stale_references_restarts(self):
        self.assertEqual(self.decide(status={'pending':0,'prior_drafts_awaiting_review':0},reference_pending=3),'restart')
        self.assertEqual(self.decide(status={'pending':0,'prior_drafts_awaiting_review':0},reference_pending=None),'restart')

    def test_graphic_gaps_do_not_hide_pending_reference_work(self):
        self.assertEqual(self.decide(status={'pending':2,'prior_drafts_awaiting_review':0},held=[{},{}],reference_pending=1),'restart')

    def test_graphic_sources_are_not_invented_by_endless_empty_runs(self):
        self.assertEqual(self.decide(status={'pending':2,'prior_drafts_awaiting_review':0},held=[{},{}]),'needs_source_recovery')

    def test_backoff_and_repeated_no_progress_exits(self):
        self.assertEqual(self.decide(previous={'next_start_after_unix':200}),'restart_backoff')
        self.assertEqual(self.decide(previous={'consecutive_unexpected_exits':5}),'needs_attention')

    def test_pid_identity_uses_exact_script_argument(self):
        with patch.object(supervisor,'RUNNER',Path('/project/run_exhaustive.py')):
            rows=[{'pid':1,'args':['/bin/python3','/project/run_exhaustive.py']},
                  {'pid':2,'args':['/bin/python3','/other/run_exhaustive.py']},
                  {'pid':3,'args':['/bin/echo','/project/run_exhaustive.py']},
                  {'pid':4,'args':['/bin/python3','-c','print("/project/run_exhaustive.py")']}]
            self.assertEqual([p['pid'] for p in supervisor.coordinator_processes(rows)],[1])


class FilesAndProcesses(TestCase):
    def setUp(self):
        self.tmp=TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        self.runtime=self.root/'runtime/exhaustive';self.runtime.mkdir(parents=True)
        self.health=self.root/'runtime/supervision'
        self.patches=[patch.object(supervisor,'HERE',self.root),patch.object(supervisor,'RUNTIME',self.runtime),
                      patch.object(supervisor,'SUPERVISION',self.health)]
        for p in self.patches:p.start();self.addCleanup(p.stop)
        (self.runtime/'status.json').write_text(json.dumps({'status':'running','pending':23,'prior_drafts_awaiting_review':3}))

    def test_restart_preserves_metadata_and_does_not_touch_job_answers(self):
        job=self.runtime/'jobs/previous';job.mkdir(parents=True)
        (job/'answer.json').write_text('unaccepted previous evidence')
        with patch.object(supervisor,'processes',return_value=[]),patch.object(supervisor,'launch',return_value=1234) as launch:
            result=supervisor.check()
        self.assertEqual(result['state'],'starting');launch.assert_called_once()
        self.assertEqual((job/'answer.json').read_text(),'unaccepted previous evidence')
        folder=launch.call_args.args[0]
        self.assertTrue((folder/'status.json').exists())
        self.assertEqual(json.loads((folder/'preserved-job-folders.json').read_text()),['previous'])

    def test_two_checks_cannot_both_launch(self):
        self.health.mkdir()
        with (self.health/'supervisor.lock').open('a') as stream:
            fcntl.flock(stream,fcntl.LOCK_EX|fcntl.LOCK_NB)
            with patch.object(supervisor,'launch') as launch:
                self.assertEqual(supervisor.check()['state'],'already_checking')
                launch.assert_not_called()

    def test_launch_failure_persists_backoff_and_counts_failed_attempt(self):
        with patch.object(supervisor,'processes',return_value=[]),patch.object(supervisor,'launch',side_effect=OSError('simulated')):
            result=supervisor.check()
        self.assertEqual(result['state'],'restart_failed')
        self.assertEqual(result['consecutive_unexpected_exits'],1)
        self.assertGreater(result['next_start_after_unix'],result['checked_at_unix'])
        with patch.object(supervisor,'processes',return_value=[]),patch.object(supervisor,'launch') as launch:
            self.assertEqual(supervisor.check()['state'],'restart_backoff');launch.assert_not_called()

    def test_explicit_pause_survives_new_health_check(self):
        self.health.mkdir();(self.health/'disabled').touch()
        with patch.object(supervisor,'launch') as launch:
            self.assertEqual(supervisor.check()['state'],'disabled');launch.assert_not_called()

    def test_existing_worker_is_never_signalled_or_relaunched(self):
        job=self.runtime/'jobs/current';job.mkdir(parents=True)
        rows=[{'pid':7,'ppid':1,'args':['/local/bin/codex','exec','--output-last-message',str(job/'result.json')]}]
        with patch.object(supervisor,'processes',return_value=rows),patch.object(supervisor,'launch') as launch:
            self.assertEqual(supervisor.check()['state'],'orphan_workers');launch.assert_not_called()

    def test_native_stderr_progress_counts_while_stdout_is_empty(self):
        job=self.runtime/'jobs/native';job.mkdir(parents=True)
        stdout=job/'events-1.log';stdout.touch();os.utime(stdout,(100,100))
        stderr=job/'errors-1.log';stderr.write_text('native progress\n');os.utime(stderr,(200,200))
        rows=[{'pid':7,'ppid':1,'args':['/local/bin/codex','exec','--output-last-message',str(job/'result.json')]}]
        worker=supervisor.job_workers(rows)[0]
        self.assertEqual(worker['last_event_unix'],200)
        self.assertFalse(worker['execution']['verified'])

    def test_real_subprocess_death_then_health_check_restarts(self):
        script=self.root/'fake_coordinator.py'
        script.write_text('import time; time.sleep(30)\n')
        child=subprocess.Popen([sys.executable,str(script)])
        replacements=[]
        real_popen=subprocess.Popen
        def spawn(*args,**kwargs):
            result=real_popen(*args,**kwargs);replacements.append(result);return result
        try:
            with patch.object(supervisor,'RUNNER',script):
                self.assertEqual(supervisor.check()['state'],'monitoring')
                child.kill();child.wait(timeout=5)
                with patch.object(supervisor.subprocess,'Popen',side_effect=spawn):
                    result=supervisor.check()
                self.assertEqual(result['state'],'starting')
                replacement=next(p for p in replacements if p.pid==result['launch_pid'])
                self.assertIsNone(replacement.poll())
                self.assertEqual(supervisor.check()['state'],'monitoring')
        finally:
            if child.poll() is None:child.terminate();child.wait(timeout=5)
            for replacement in replacements:
                if replacement.poll() is None:replacement.terminate();replacement.wait(timeout=5)

    def test_repeat_assignment_creates_new_evidence_directory(self):
        with patch.object(coordinator,'RUNTIME',self.runtime):
            first=coordinator.job_directory('travail-00001')
            (first/'answer.json').write_text('preserve me')
            second=coordinator.job_directory('travail-00001')
        self.assertNotEqual(first,second)
        self.assertEqual((first/'answer.json').read_text(),'preserve me')

    def test_agent_timeout_stops_its_grandchild_before_next_attempt(self):
        marker=self.root/'should-not-be-written'
        delayed='import pathlib,time; time.sleep(1.2); pathlib.Path('+repr(str(marker))+').write_text("late")'
        program='import subprocess,sys,time; subprocess.Popen([sys.executable,"-c",'+repr(delayed)+']); time.sleep(20)'
        with self.assertRaises(subprocess.TimeoutExpired):
            coordinator.invoke_agent([sys.executable,'-c',program],input='',text=True,
                                     stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,cwd=self.root,timeout=.5)
        time.sleep(1.3)
        self.assertFalse(marker.exists())
        receipt=json.loads(next(self.root.glob('process-*.json')).read_text())
        self.assertIn('ended_at_unix',receipt)

    def test_post_commit_disk_failure_preserves_rows_and_does_not_reinvoke_model(self):
        for name in ['site-summaries.json','policy-coordinations.json']:(self.root/name).write_text('{}')
        body='<p>Le délai est de trois mois.</p>'
        sha=hashlib.sha256(body.encode()).hexdigest()
        source={'code_id':'CODE','source_id':'ARTICLE','source_sha256':sha,'number':'L1',
                'source_xml':body,'source_notes_xml':''}
        db=open_db(self.root/'corpus.sqlite')
        db.execute('INSERT INTO articles VALUES(?,?,?,?,?,?,?,?,?,?)',('CODE','ARTICLE','L1','2020-01-01','2999-01-01','VIGUEUR',body,body,sha,'archive'))
        db.commit();db.close()
        def child(*args,**kwargs):
            emit_cli_startup(kwargs)
            row={k:source[k] for k in ['code_id','source_id','source_sha256','number']}
            row.update(proposed_xml='<p>Le délai applicable est fixé à trois mois.</p>',reason='Clarifier le délai.',review_notes='Trois mois conservés.')
            folder=kwargs['cwd']
            (folder/'answer.json').write_text(json.dumps([row]))
            (folder/'result.json').write_text(json.dumps({'output_file':'answer.json','article_count':1}))
            return SimpleNamespace(returncode=0)
        real_atomic=coordinator.atomic
        def disk_failure(path,value):
            if 'automatic-travail' in path.parts:raise OSError('simulated disk failure')
            return real_atomic(path,value)
        with patch.object(coordinator,'HERE',self.root),patch.object(coordinator,'RUNTIME',self.runtime),\
             patch.object(coordinator,'STOP',threading.Event()),patch.object(coordinator,'past_before_job',return_value=[]),\
             patch.object(coordinator,'invoke_agent',side_effect=child) as model,\
             patch.object(coordinator,'atomic',side_effect=disk_failure),redirect_stdout(io.StringIO()):
            coordinator.run_job(('travail',1,[source]),'mock',{'travail':[source]})
        self.assertEqual(model.call_count,1)
        intent=json.loads((self.runtime/'jobs/travail-00001/registration-intent.json').read_text())
        self.assertEqual(len(intent['rows']),1)
        db=open_db(self.root/'corpus.sqlite')
        self.assertIsNotNone(db.execute('SELECT proposed_xml FROM drafts WHERE source_id="ARTICLE"').fetchone())
        db.close()
        state=json.loads((self.runtime/'status.json').read_text())
        self.assertEqual(state['status'],'blocked')
        self.assertIn('reconciliation',state['failure'])


if __name__=='__main__':main(verbosity=2)
