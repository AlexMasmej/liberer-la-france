"""Isolated file/SQLite fixtures; no live DB, OS collector, model or activation."""
from pathlib import Path
import copy
import json
import os
import shutil
import sqlite3
import tempfile
import unittest
from unittest.mock import patch
import transfer_guards as g

HERE = Path(__file__).resolve().parent
PARSER = HERE.parents[1] / 'worker_execution.py'


class Guards(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='transfer-guard-isolated-')
        self.addCleanup(self.temp.cleanup)
        self.root = (Path(self.temp.name) / 'legal-rewrite').resolve()
        self.base = self.root / 'runtime/exhaustive'
        self.base.mkdir(parents=True)
        self.identity = {'pid': 3122, 'started_at_unix': 1000}
        self.now = 3000
        self.put(self.base/'coordinator.pid', b'3122')
        self.put(self.base/'coordinator-run.json', {'pid': 3122, 'started_at_unix': 1000})
        self.ad = {'coordinator_pid': 3122, 'updated_at_unix': 1100,
                   'pending_by_kind': {'new': 0, 'review': 99},
                   'reserved_or_running_by_kind': {'new': 0, 'review': 1},
                   'admitted_by_kind': {'new': 2, 'review': 1}}
        self.put(self.base/'admission-status.json', self.ad)
        self.queue = [{'slug': 'travail', 'index': 1, 'review': False, 'source_ids': ['A']},
                      {'slug': 'travail', 'index': 2, 'review': False, 'source_ids': ['B']},
                      {'slug': 'travail', 'index': 1, 'review': True, 'source_ids': ['C']}]
        self.put(self.base/'mixed-queue.json', self.queue)
        self.put(self.base/'queue-admission-plan.json', {
            'coordinator_pid': 3122, 'queue_file': 'mixed-queue.json',
            'scheduled_by_kind': {'new': 2, 'review': 1}})
        self.config = {'codes': [{'slug': 'travail', 'id': 'CODE'}],
                       'annexes': [{'slug': 'other'+str(i), 'id': 'OTHER'+str(i)} for i in range(8)]}
        self.put(self.root/'corpus.json', self.config)
        db = sqlite3.connect(self.root/'corpus.sqlite')
        db.execute('CREATE TABLE articles(code_id TEXT,id TEXT,source_sha256 TEXT)')
        db.execute('CREATE TABLE drafts(code_id TEXT,source_id TEXT,source_sha256 TEXT,status TEXT,proposed_xml TEXT)')
        db.executemany('INSERT INTO articles VALUES(?,?,?)', [('CODE', 'A', 'source-A'), ('CODE', 'B', 'source-B')])
        db.execute('INSERT INTO drafts VALUES(?,?,?,?,?)', ('CODE', 'A', 'source-A', 'rewrite_draft', '<p>Whole fixture proposal</p>'))
        db.commit(); db.close()
        self.metrics = [self.metric(1, 'accepted'), self.metric(2, 'deferred')]
        for index, identifier in [(1,'A'),(2,'B')]:
            self.put(self.base/'jobs'/('travail-'+str(index).zfill(5))/'source.json',
                     [{'code_id':'CODE','source_id':identifier,'source_sha256':'source-'+identifier}])
        self.metrics_file()

    def put(self, path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(value if isinstance(value, bytes) else (json.dumps(value)+'\n').encode())

    def metric(self, index, outcome):
        return {'coordinator_pid': 3122, 'slug': 'travail', 'index': index,
                'kind': 'new', 'outcome': outcome,
                'job':'travail-'+str(index).zfill(5), 'articles':1,
                'started_at_unix': 1200, 'finished_at_unix': 1500}

    def metrics_file(self):
        self.put(self.base/'job-metrics.jsonl', b''.join((json.dumps(x)+'\n').encode() for x in self.metrics))

    def collect(self, **kwargs):
        original = sqlite3.connect
        def fixture_ro(path, **options):
            self.assertTrue(str(path).startswith(self.root.as_uri()))
            self.assertTrue(str(path).endswith('?mode=ro'))
            self.assertTrue(options.get('uri'))
            return original(path, **options)
        with patch.object(g.sqlite3, 'connect', side_effect=fixture_ro):
            return g.terminal_new_queue(self.root, kwargs.get('identity', self.identity),
                                        kwargs.get('workers', []), self.now)

    def test_stale_admission_can_be_proved_by_complete_actual_terminal_inventory(self):
        before = {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        result = self.collect()
        self.assertEqual(result['terminal_new_jobs'], 2)
        self.assertFalse(result['all_first_passes_complete'])
        self.assertEqual(result['dispositions'][1]['current_disposition'], 'deferred_still_pending')
        self.assertEqual(result['dispositions'][0]['current_disposition'], 'registered_requires_full_reconciliation')
        self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()})

    def test_pending_or_reserved_new_blocks_even_if_processes_are_empty(self):
        for field in ('pending_by_kind', 'reserved_or_running_by_kind'):
            value = copy.deepcopy(self.ad); value[field]['new'] = 1
            self.put(self.base/'admission-status.json', value)
            with self.subTest(field=field), self.assertRaises(g.GuardError): self.collect()
        self.put(self.base/'admission-status.json', self.ad)

    def test_unknown_and_live_new_processes_block(self):
        for workers in (None, [{'ppid':3122,'kind':'new'}], [{'ppid':999,'kind':'review'}]):
            with self.subTest(workers=workers), self.assertRaises(g.GuardError): self.collect(workers=workers)

    def test_review_validation_without_native_process_does_not_prove_idle(self):
        result = self.collect()
        self.assertNotIn('all_workers_idle', result)
        with self.assertRaises(g.GuardError):
            self.collect(workers=[{'ppid':3122,'kind':'review'}, {'ppid':3122,'kind':'review'}])

    def test_unknown_future_or_foreign_admission_cannot_be_freshened(self):
        for value in (self.ad|{'updated_at_unix':None}, self.ad|{'updated_at_unix':4000},
                      self.ad|{'coordinator_pid':999}, self.ad|{'pending_by_kind':{}},
                      self.ad|{'admitted_by_kind':{'new':True,'review':1}}):
            self.put(self.base/'admission-status.json', value)
            with self.subTest(value=value), self.assertRaises(g.GuardError): self.collect()

    def test_truncated_queue_and_incomplete_metrics_are_refused(self):
        self.put(self.base/'mixed-queue.json', self.queue[:1])
        with self.assertRaises(g.GuardError): self.collect()
        self.put(self.base/'mixed-queue.json', self.queue)
        self.put(self.base/'job-metrics.jsonl', b'{"coordinator_pid":3122')
        with self.assertRaises(g.GuardError): self.collect()

    def test_duplicate_assignment_or_terminal_metric_is_refused(self):
        self.put(self.base/'mixed-queue.json', self.queue+[self.queue[0]])
        with self.assertRaises(g.GuardError): self.collect()
        self.put(self.base/'mixed-queue.json', self.queue)
        self.metrics.append(self.metrics[0]); self.metrics_file()
        with self.assertRaises(g.GuardError): self.collect()

    def test_missing_exception_and_foreign_pid_terminal_results_do_not_exhaust_queue(self):
        for metrics in ([self.metrics[0]], [self.metrics[0], self.metric(2,'exception')],
                        [self.metrics[0], self.metric(2,'deferred')|{'coordinator_pid':999}]):
            self.metrics=metrics; self.metrics_file()
            with self.subTest(metrics=metrics), self.assertRaises(g.GuardError): self.collect()

    def test_false_acceptance_or_wrong_source_hash_in_database_is_refused(self):
        self.metrics[1]['outcome']='accepted'; self.metrics_file()
        with self.assertRaises(g.GuardError): self.collect()
        self.metrics[1]['outcome']='deferred'; self.metrics_file()
        db=sqlite3.connect(self.root/'corpus.sqlite');db.execute("UPDATE drafts SET source_sha256='wrong'");db.commit();db.close()
        with self.assertRaises(g.GuardError): self.collect()

    def test_no_unknown_canonical_collection_is_inferred_from_current_queue(self):
        self.config['annexes'].pop(); self.put(self.root/'corpus.json',self.config)
        with self.assertRaises(g.GuardError): self.collect()

    def test_runtime_evidence_changed_during_db_read_is_rejected(self):
        check = g.unchanged
        def intervening(records):
            self.put(self.base/'coordinator-run.json', {'pid':999,'started_at_unix':1000})
            check(records)
        with patch.object(g, 'unchanged', side_effect=intervening):
            with self.assertRaises(g.GuardError):self.collect()

    def test_queue_cannot_substitute_other_registered_ids_for_the_actual_job(self):
        queue=copy.deepcopy(self.queue);queue[0]['source_ids']=['C']
        self.put(self.base/'mixed-queue.json',queue)
        with self.assertRaises(g.GuardError):self.collect()

    def test_deferred_job_source_change_or_invented_source_membership_blocks(self):
        path=self.base/'jobs/travail-00002/source.json'
        for source in ([{'code_id':'CODE','source_id':'B','source_sha256':'stale'}],
                       [{'code_id':'CODE','source_id':'A','source_sha256':'source-A'}]):
            self.put(path,source)
            with self.subTest(source=source),self.assertRaises(g.GuardError):self.collect()

    def test_legitimate_skip_needs_no_job_but_requires_current_registered_identity(self):
        self.metrics[0]['outcome']='skipped';self.metrics[0].pop('job');self.metrics_file()
        shutil.rmtree(self.base/'jobs/travail-00001')
        self.assertEqual(self.collect()['terminal_new_jobs'],2)
        db=sqlite3.connect(self.root/'corpus.sqlite');db.execute('DELETE FROM drafts');db.commit();db.close()
        with self.assertRaises(g.GuardError):self.collect()

    def test_zero_scheduled_count_cannot_be_supplied_as_a_boolean(self):
        self.put(self.base/'mixed-queue.json',self.queue[:2])
        self.put(self.base/'queue-admission-plan.json',{'coordinator_pid':3122,
            'queue_file':'mixed-queue.json','scheduled_by_kind':{'new':2,'review':False}})
        with self.assertRaises(g.GuardError):self.collect()

    def test_pid_reuse_and_symlinked_queue_are_refused(self):
        with self.assertRaises(g.GuardError): self.collect(identity=self.identity|{'started_at_unix':2000})
        p=self.base/'mixed-queue.json'; target=self.base/'other.json';p.rename(target);p.symlink_to(target)
        with self.assertRaises(g.GuardError): self.collect()

    def exit_file(self, **updates):
        value={'pid':3122,'ended_at_unix':2500,'exit_code':0,'exit_type':None,'stop_requested':False}|updates
        self.put(self.base/'coordinator-exit.json',value)
        os.utime(self.base/'coordinator-exit.json',(2500,2500))

    def test_exit_is_bound_to_observed_process_and_real_receipt(self):
        self.exit_file()
        proof=g.successful_exit(self.root,self.identity,2000,self.now)
        self.assertEqual(proof['started_at_unix'],1000)
        self.assertEqual(proof['ended_at_unix'],2500)

    def test_historical_reused_pid_future_signal_or_incomplete_exit_blocks(self):
        for updates in ({'pid':999},{'ended_at_unix':900},{'ended_at_unix':1500},
                        {'ended_at_unix':4000},{'exit_code':1},{'exit_code':False},{'exit_type':'OperationalError'},
                        {'stop_requested':True},{'stop_requested':None}):
            self.exit_file(**updates)
            with self.subTest(updates=updates),self.assertRaises(g.GuardError):
                g.successful_exit(self.root,self.identity,2000,self.now)

    def test_exit_with_changed_run_identity_or_old_file_mtime_blocks(self):
        self.exit_file();os.utime(self.base/'coordinator-exit.json',(1000,1000))
        with self.assertRaises(g.GuardError):g.successful_exit(self.root,self.identity,2000,self.now)
        self.exit_file();self.put(self.base/'coordinator-run.json',{'pid':3122,'started_at_unix':2000})
        with self.assertRaises(g.GuardError):g.successful_exit(self.root,self.identity,2000,self.now)

    def launch_fixture(self):
        for name in g.REQUIRED_PINS:
            if not (self.root/name).exists():self.put(self.root/name,b'# isolated fixture\n')
        shutil.copyfile(PARSER,self.root/'worker_execution.py')
        (self.root/'attachments/records').mkdir(parents=True)
        self.put(self.root/'attachments/records/asset.json',{'fixture':True})
        self.pins={name:g.digest((self.root/name).read_bytes()) for name in g.REQUIRED_PINS}
        self.pins['attachments/records/asset.json']=g.digest((self.root/'attachments/records/asset.json').read_bytes())
        self.launch=self.root/'runtime/preparation/launch';self.command=['/usr/bin/python3','-u',str(self.root/'run_exhaustive.py'),'--recover-new-before-reviews']
        self.put(self.launch/'launch.json',{'pid':9123,'command':self.command,'launched_at_unix':2100})
        self.new={'pid':9123,'args':self.command,'started_at_unix':2100}
        self.put(self.base/'coordinator-run.json',{'pid':9123,'started_at_unix':2100,'requested_execution':{'model':'gpt-6-astra','reasoning_effort':'medium'}})
        self.native=[]
        for i in range(2):
            job='review-fixture-'+str(i);folder=self.base/'jobs'/job;log=folder/'errors-1.log';pid=4500+i
            session=f'01234567-0123-0123-0123-{i:012d}'
            self.put(log,('OpenAI Codex v0.160.1\n--------\nworkdir: '+str(folder)+'\nmodel: gpt-6-astra\nprovider: openai\nreasoning effort: medium\nsession id: '+session+'\n--------\ncodex\nSynthetic fixture response.\n').encode())
            self.put(folder/f'process-{pid}.json',{'pid':pid,'started_at_unix':2200,'stderr_log':str(log)})
            self.native.append({'pid':pid,'ppid':9123,'job':job})

    def attest(self, coordinators=None, workers=None):
        return g.native_launch_attestation(self.root,self.launch,
            [self.new] if coordinators is None else coordinators,
            self.native if workers is None else workers,self.pins,self.now)

    def test_native_launch_requires_actual_distinct_responses_and_is_read_only(self):
        self.launch_fixture();before={p:p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        result=self.attest();self.assertEqual(len(result['native_workers']),2)
        self.assertFalse(result['configured_capacity_or_speed_gain_proven'])
        self.assertEqual(before,{p:p.read_bytes() for p in self.root.rglob('*') if p.is_file()})

    def test_late_launch_rechecks_all_code_policy_and_catalogue_pins(self):
        self.launch_fixture();self.put(self.root/'policy-coordinations.json',b'changed policy')
        with self.assertRaises(g.GuardError):self.attest()
        self.launch_fixture_catalogue_reset()

    def launch_fixture_catalogue_reset(self):
        # Restore the owned fixture policy; introducing a new record must block.
        self.put(self.root/'policy-coordinations.json',b'# isolated fixture\n')
        self.put(self.root/'attachments/records/new.json',{'fixture':'new'})
        with self.assertRaises(g.GuardError):self.attest()

    def test_missing_pin_duplicate_coordinator_or_unknown_workers_block(self):
        self.launch_fixture()
        for coords in ([],[self.new,self.new]):
            with self.subTest(coordinators=coords),self.assertRaises(g.GuardError):self.attest(coordinators=coords)
        with self.assertRaises(g.GuardError):self.attest(workers=[])
        self.pins.pop('reference_coherence.py')
        with self.assertRaises(g.GuardError):self.attest()

    def test_historical_launch_receipt_or_different_process_command_blocks(self):
        self.launch_fixture();self.new['started_at_unix']=2000
        with self.assertRaises(g.GuardError):self.attest()
        self.new['started_at_unix']=2100;self.new['args']=self.command+['--unexpected']
        with self.assertRaises(g.GuardError):self.attest()

    def test_config_and_header_alone_never_count_as_model_response(self):
        self.launch_fixture();p=self.base/'jobs/review-fixture-1/errors-1.log';p.write_text(p.read_text().split('\ncodex\n')[0]+'\n')
        with self.assertRaises(g.GuardError):self.attest()

    def test_foreign_worker_pid_and_wrong_native_workdir_block(self):
        self.launch_fixture();self.native[0]['ppid']=999
        with self.assertRaises(g.GuardError):self.attest()
        self.native[0]['ppid']=9123;p=self.base/'jobs/review-fixture-1/errors-1.log'
        p.write_text(p.read_text().replace(str(p.parent),str(self.base/'jobs/unrelated')))
        with self.assertRaises(g.GuardError):self.attest()

    def test_pinned_source_symlink_or_missing_catalogue_member_blocks(self):
        self.launch_fixture();p=self.root/'reference_coherence.py';target=self.root/'different.py';p.rename(target);p.symlink_to(target)
        with self.assertRaises(g.GuardError):self.attest()
        p.unlink();target.rename(p);(self.root/'attachments/records/asset.json').unlink()
        with self.assertRaises(g.GuardError):self.attest()

    def test_wrong_effort_reused_session_and_old_worker_lifetime_block(self):
        self.launch_fixture();p=self.base/'jobs/review-fixture-1/errors-1.log';text=p.read_text()
        p.write_text(text.replace('reasoning effort: medium','reasoning effort: ultra'))
        with self.assertRaises(g.GuardError):self.attest()
        p.write_text(text.replace('01234567-0123-0123-0123-000000000001','01234567-0123-0123-0123-000000000000'))
        with self.assertRaises(g.GuardError):self.attest()
        p.write_text(text);process=p.parent/'process-4501.json';v=json.loads(process.read_text());v['started_at_unix']=1900;self.put(process,v)
        with self.assertRaises(g.GuardError):self.attest()


if __name__ == '__main__':
    unittest.main(verbosity=2)
