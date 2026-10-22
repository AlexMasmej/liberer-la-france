"""Isolated lifecycle tests: only temporary databases and batches are writable."""
from pathlib import Path
import copy
import hashlib
import json
import sqlite3
import sys
import tempfile
import threading
import unittest
from types import SimpleNamespace
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import reference_coherence as audit
import reference_queue as queue


class QueueCycle(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.home = Path(self.temp.name)
        (self.home / 'batches/test').mkdir(parents=True)
        (self.home / 'runtime').mkdir()
        self.db = sqlite3.connect(self.home / 'corpus.sqlite')
        self.addCleanup(self.db.close)
        self.db.executescript('''
            CREATE TABLE articles(code_id,id,number,source_sha256,content_xml);
            CREATE TABLE drafts(code_id,source_id,source_sha256,status,proposed_xml,reason,review_notes);
            CREATE TABLE documents(code_id,id,kind,xml);
        ''')
        self.sources = {}
        self.catalog = {}
        for identifier, number, body in [
            ('A', 'L10-1', '<p>Le renvoi à L20-1 conserve les droits.</p>'),
            ('B', 'L20-1', '<p>La garantie du contrat de travail conserve le renvoi à L10-1.</p>'),
        ]:
            row = dict(code_id='CODE', source_id=identifier, number=number,
                       source_sha256='s' + identifier, source_xml=body,
                       source_notes_xml='')
            self.sources[identifier] = row
            self.catalog[audit.key(row)] = row
            self.db.execute('INSERT INTO articles VALUES(?,?,?,?,?)',
                            ('CODE', identifier, number, 's' + identifier, body))
        self.db.commit()
        for target, value in [(queue, 'HERE'), (audit, 'HERE')]:
            p = patch.object(target, value, self.home)
            p.start(); self.addCleanup(p.stop)
        p = patch.object(queue, 'REPORT', self.home / 'runtime/report.json')
        p.start(); self.addCleanup(p.stop)
        p = patch.object(audit, 'focus', return_value=self.catalog)
        p.start(); self.addCleanup(p.stop)
        p = patch.object(queue, 'priority', side_effect=lambda job: (job[0], job[1]))
        p.start(); self.addCleanup(p.stop)

    def draft(self, identifier, body=None):
        body = body or self.sources[identifier]['source_xml'] + '<p>Droits maintenus.</p>'
        self.db.execute('DELETE FROM drafts WHERE code_id=? AND source_id=?', ('CODE', identifier))
        self.db.execute('INSERT INTO drafts VALUES(?,?,?,?,?,?,?)',
                        ('CODE', identifier, 's' + identifier, 'proposed', body, 'Motif', 'Note'))
        self.db.commit()
        return body

    def certify(self, identifier='A', batch='001.json'):
        article = self.sources[identifier]
        body = self.db.execute('SELECT proposed_xml FROM drafts WHERE source_id=?', (identifier,)).fetchone()[0]
        snap = audit.capture(self.db, [article], catalog=self.catalog)
        row = article | dict(proposed_xml=body, reference_checks=[dict(
            target_key=k, view_sha256=v['view_sha256'],
            assessment='Le texte entier de la cible conserve les droits antérieurs et la transition ; le renvoi ne crée ni terme automatique ni perte de protection.'
        ) for k, v in snap['targets'].items()])
        audit.accept_checks([row], [article], snap, self.catalog)
        (self.home / 'batches/test' / batch).write_text(json.dumps([row]))
        return row

    def pending(self, ids=('A',), save=True):
        return queue.pending({'test': [self.sources[i] for i in ids]}, save=save)

    def test_current_certificate_is_accepted(self):
        self.draft('A'); self.certify()
        rows, report = self.pending()
        self.assertEqual(rows['test'], [])
        self.assertEqual(report['current_reference_certificates'], 1)
        self.assertTrue(report['all_detected_contract_reference_checks_current'])

    def test_reference_recheck_pins_complete_batch_metadata(self):
        self.draft('A');row=self.certify()
        # Changing B makes A's old certificate require a fresh whole-target read.
        self.draft('B')
        rows,_=self.pending()
        from review_prior import batch_row_sha256
        self.assertEqual(rows['test'][0]['previous_draft']['batch_row_sha256'],batch_row_sha256(row))
        changed=row|{'review_notes':'A newer independent assessment was added.'}
        self.assertNotEqual(rows['test'][0]['previous_draft']['batch_row_sha256'],batch_row_sha256(changed))

    def test_changed_referrer_body_requeues_existing_certificate(self):
        self.draft('A'); self.certify(); self.draft('A', '<p>L20-1 : autre règle entière.</p>')
        rows, report = self.pending()
        self.assertEqual(report['pending_reference_reviews'], 1)
        self.assertTrue(rows['test'][0]['reference_recheck_only'])

    def test_target_first_rewrite_invalidates_official_source_certificate(self):
        self.draft('A'); self.certify(); self.draft('B')
        self.assertEqual(self.pending()[1]['pending_reference_reviews'], 1)

    def test_target_rewrite_changes_fingerprint_even_if_referrer_unchanged(self):
        self.draft('A'); self.draft('B'); self.certify()
        self.draft('B', '<p>Première version modifiée.</p>')
        first = self.pending()[1]['pending'][0]
        self.draft('B', '<p>Deuxième version modifiée.</p>')
        second = self.pending()[1]['pending'][0]
        self.assertEqual(first['proposed_sha256'], second['proposed_sha256'])
        self.assertNotEqual(first['dependency_fingerprint'], second['dependency_fingerprint'])

    def test_no_completion_with_unwritten_relevant_referrer(self):
        _, report = self.pending()
        self.assertEqual(report['relevant_sources_not_yet_rewritten'], 1)
        self.assertFalse(report['all_detected_contract_reference_checks_current'])

    def test_no_completion_with_unwritten_target_in_source_inventory(self):
        self.draft('A'); self.certify()
        _, report = self.pending(('A', 'B'))
        self.assertEqual(report['current_reference_certificates'], 1)
        self.assertEqual(report['relevant_sources_not_yet_rewritten'], 1)
        self.assertFalse(report['all_detected_contract_reference_checks_current'])

    def test_stale_source_draft_never_counts_as_rewritten(self):
        self.draft('A'); self.certify()
        self.db.execute("UPDATE drafts SET source_sha256='old' WHERE source_id='A'"); self.db.commit()
        rows, report = self.pending()
        self.assertEqual(rows['test'], [])
        self.assertEqual(report['drafted_articles_scanned'], 0)
        self.assertFalse(report['all_detected_contract_reference_checks_current'])

    def test_run_rechecks_dependency_changed_after_same_wave_certificate(self):
        self.draft('A')
        event = threading.Event(); calls = []
        def worker(job, *_):
            # Callback executes in worker thread: use an independent SQLite handle.
            c = sqlite3.connect(self.home / 'corpus.sqlite')
            old = self.db; self.db = c
            try:
                calls.append(job)
                self.certify()
                if len(calls) == 1: self.draft('B')
            finally:
                self.db = old; c.close()
        coordinator = SimpleNamespace(STOP=event, run_in_slot=worker)
        report = queue.run(coordinator, {'test': [self.sources['A']]}, 'unused', 1)
        self.assertEqual(len(calls), 2)
        self.assertEqual(report['pending_reference_reviews'], 0)
        self.assertTrue(report['all_detected_contract_reference_checks_current'])

    def test_unchanged_pending_state_raises_instead_of_false_completion(self):
        self.draft('A'); calls = []
        coordinator = SimpleNamespace(STOP=threading.Event(), run_in_slot=lambda *args: calls.append(args))
        with self.assertRaisesRegex(ValueError, 'did not converge'):
            queue.run(coordinator, {'test': [self.sources['A']]}, 'unused', 1)
        self.assertEqual(len(calls), 1)
        report = json.loads(queue.REPORT.read_text())
        self.assertFalse(report['all_detected_contract_reference_checks_current'])

    def test_stop_before_wave_does_not_start_worker_or_claim_completion(self):
        self.draft('A'); calls = []; event = threading.Event(); event.set()
        coordinator = SimpleNamespace(STOP=event, run_in_slot=lambda *args: calls.append(args))
        report = queue.run(coordinator, {'test': [self.sources['A']]}, 'unused', 1)
        self.assertEqual(calls, [])
        self.assertEqual(report['pending_reference_reviews'], 1)
        self.assertFalse(report['all_detected_contract_reference_checks_current'])

    def test_stop_during_wave_returns_pending_without_second_wave(self):
        self.draft('A'); event = threading.Event(); calls = []
        def worker(*args): calls.append(args); event.set()
        coordinator = SimpleNamespace(STOP=event, run_in_slot=worker)
        report = queue.run(coordinator, {'test': [self.sources['A']]}, 'unused', 1)
        self.assertEqual(len(calls), 1)
        self.assertEqual(report['pending_reference_reviews'], 1)
        self.assertFalse(report['all_detected_contract_reference_checks_current'])

    def test_no_queue_does_not_mean_unwritten_sources_are_complete(self):
        coordinator = SimpleNamespace(STOP=threading.Event(), run_in_slot=lambda *args: self.fail('Unexpected worker'))
        report = queue.run(coordinator, {'test': [self.sources['A']]}, 'unused', 1)
        self.assertFalse(report['all_detected_contract_reference_checks_current'])
        self.assertEqual(report['relevant_sources_not_yet_rewritten'], 1)

    def test_worker_exception_sets_stop_before_draining_waiting_jobs(self):
        event = threading.Event(); started_after_failure = []
        def worker(job, *_):
            if job[1] == 1:
                raise RuntimeError('Unexpected reference job failure')
            # A job already pulled by the pool can be waiting for a slot/limit.
            # The coordinator observes STOP before starting a model invocation.
            if not event.wait(timeout=0.25):
                started_after_failure.append(job[1])
        coordinator = SimpleNamespace(STOP=event, run_in_slot=worker)
        jobs = [('test', n, []) for n in range(1, 4)]
        report = dict(pending=[dict(code_id='CODE', source_id='A',
                     proposed_sha256='body', dependency_fingerprint='target')])
        with patch.object(queue, 'jobs', return_value=(jobs, report)):
            with self.assertRaisesRegex(RuntimeError, 'Unexpected reference job failure'):
                queue.run(coordinator, {}, 'unused', 1)
        self.assertTrue(event.is_set(), 'Fatal job error must stop queued reference jobs')
        self.assertEqual(started_after_failure, [])


if __name__ == '__main__':
    unittest.main(verbosity=2)
