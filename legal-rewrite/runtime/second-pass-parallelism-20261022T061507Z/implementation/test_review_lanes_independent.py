"""Independent, model-free safety checks of the prepared review lanes.

Run this file directly. Imports resolve the prepared coordinator/capacity module
first; every runtime, DB accessor and authoring operation is replaced before a
coordinator function is invoked. These tests never start a CLI or reserve an
actual task slot. Threads represent only in-memory synthetic jobs.
"""
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import ast
import importlib
import json
import sys
import threading
import time
import unittest
from unittest.mock import patch

STAGING = Path(__file__).resolve().parent
BEFORE = STAGING.parent / 'before'
PROJECT = STAGING.parents[2]
sys.path.insert(0, str(PROJECT))
sys.path.insert(0, str(STAGING))
import run_exhaustive as prepared
import worker_capacity as capacity
import review_lane_observation as observation


def article(identifier):
    return {'code_id': 'SYNTHETIC', 'source_id': identifier,
            'source_sha256': 'isolated-source-sha', 'number': 'L1-' + identifier,
            'source_xml': '<p>Entire synthetic source, never a corpus article.</p>',
            'source_notes_xml': ''}


def job(identifier):
    return ('synthetic', identifier, [article(identifier)])


def footprint(writes=(), reads=()):
    return {'writes': set(writes), 'reads': set(reads)}


class IndependentLanes(unittest.TestCase):
    def setUp(self):
        global prepared
        prepared = importlib.reload(prepared)
        self.assertEqual(Path(prepared.__file__).resolve(), STAGING / 'run_exhaustive.py')
        self.assertEqual(Path(capacity.__file__).resolve(), STAGING / 'worker_capacity.py')
        self.temporary = TemporaryDirectory(prefix='independent-lanes-', dir=STAGING)
        self.addCleanup(self.temporary.cleanup)
        self.runtime = Path(self.temporary.name)
        self.threads, self.gates, self.errors = [], [], []
        self.mutex = threading.Lock()
        for name, value in [('HERE', self.runtime), ('RUNTIME', self.runtime),
                            ('STOP', threading.Event()), ('SLOTS', threading.Condition()),
                            ('ACTIVE', 0), ('ACTIVE_LEASES', {}),
                            ('LEASE_CONTEXT', threading.local())]:
            stub = patch.object(prepared, name, value)
            stub.start()
            self.addCleanup(stub.stop)
        for name in ['open_db', 'invoke_agent', 'writer_lock', 'register', 'publish_checkpoint']:
            stub = patch.object(prepared, name, side_effect=AssertionError('Active I/O forbidden in independent lane tests: ' + name))
            stub.start()
            self.addCleanup(stub.stop)
        self.configure()

    def tearDown(self):
        prepared.STOP.set()
        for gate in self.gates:
            gate.set()
        with prepared.SLOTS:
            prepared.SLOTS.notify_all()
        for thread in self.threads:
            thread.join(timeout=2)
        self.assertFalse([t.name for t in self.threads if t.is_alive()], 'Synthetic job did not drain')

    def configure(self, new=6, review=2, total=None):
        prepared.atomic(self.runtime / 'parallelism-plan.json',
                        {'capacity': 8, 'current_workers': 8, 'role_limits': {'new': 6, 'review': 2}})
        prepared.atomic(self.runtime / 'worker-limit.json',
                        {'workers': new + review if total is None else total,
                         'role_limits': {'new': new, 'review': review}})
        with prepared.SLOTS:
            prepared.SLOTS.notify_all()

    def gate(self):
        value = threading.Event()
        self.gates.append(value)
        return value

    def until(self, predicate, message='Synthetic scheduling condition did not become true', timeout=2):
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            if predicate():
                return
            time.sleep(.005)
        self.fail(message)

    def start(self, identifier, review=False):
        done = threading.Event()

        def invoke():
            try:
                prepared.run_in_slot(job(identifier), 'NEVER_EXECUTED', {}, 8, review)
            except BaseException as error:
                with self.mutex:
                    self.errors.append(error)
            finally:
                done.set()

        thread = threading.Thread(target=invoke, name='synthetic-' + identifier, daemon=True)
        self.threads.append(thread)
        thread.start()
        return done

    def drained(self):
        for thread in self.threads:
            thread.join(timeout=3)
        self.assertFalse([t.name for t in self.threads if t.is_alive()])
        self.assertEqual(self.errors, [])
        self.assertEqual(prepared.ACTIVE, 0)
        self.assertEqual(prepared.ACTIVE_LEASES, {})

    def fake_database(self):
        records = []

        def open_database(_):
            record = {'statements': [], 'closed': False}
            with self.mutex:
                records.append(record)
            return SimpleNamespace(execute=lambda sql: record['statements'].append(sql),
                                   close=lambda: record.update(closed=True))

        return records, open_database

    def test_eight_requires_explicit_role_authorization_and_never_means_eight_new(self):
        limits = capacity.admission_limits(self.runtime, 8)
        self.assertEqual(limits, {'workers': 8, 'role_limits': {'new': 6, 'review': 2}})
        prepared.atomic(self.runtime / 'parallelism-plan.json', {'capacity': 8, 'current_workers': 8})
        with self.assertRaises(ValueError):
            capacity.admission_limits(self.runtime, 8)
        invalid = [
            {'workers': 9, 'role_limits': {'new': 6, 'review': 2}},
            {'workers': 8, 'role_limits': {'new': 7, 'review': 1}},
            {'workers': 8, 'role_limits': {'new': 6, 'review': 3}},
            {'workers': 8, 'role_limits': {'new': True, 'review': 2}},
            {'workers': 7, 'role_limits': {'new': 6, 'review': 2}},
        ]
        for document in invalid:
            with self.subTest(document=document):
                self.configure()
                prepared.atomic(self.runtime / 'worker-limit.json', document)
                with self.assertRaises(ValueError):
                    capacity.admission_limits(self.runtime, 8)

    def test_six_new_and_two_reviews_overlap_without_borrowing_review_capacity(self):
        release = self.gate()
        started = []
        running = {'new': 0, 'review': 0}
        peaks = {'new': 0, 'review': 0, 'total': 0}

        def run(assigned, *_args, review=False, **_kwargs):
            kind = 'review' if review else 'new'
            with self.mutex:
                running[kind] += 1
                peaks[kind] = max(peaks[kind], running[kind])
                peaks['total'] = max(peaks['total'], sum(running.values()))
                started.append((assigned[1], kind))
            try:
                if not release.wait(5):
                    raise AssertionError('Synthetic jobs were not released')
            finally:
                with self.mutex:
                    running[kind] -= 1

        with patch.object(prepared, 'job_lease', side_effect=lambda j: footprint(['SYNTHETIC|' + j[1]], ['SHARED_READ'])), \
             patch.object(prepared, 'run_job', side_effect=run):
            for index in range(9):
                self.start('N' + str(index))
            for index in range(4):
                self.start('R' + str(index), True)
            self.until(lambda: len(started) == 8)
            self.assertEqual(running, {'new': 6, 'review': 2})
            self.assertEqual(prepared.ACTIVE, 8)
            release.set()
            self.drained()
        self.assertLessEqual(peaks['new'], 6)
        self.assertLessEqual(peaks['review'], 2)
        self.assertLessEqual(peaks['total'], 8)
        self.assertEqual(len(started), 13)

    def test_real_pool_dispatch_reaches_two_reviews_behind_a_large_new_backlog(self):
        new_release, review_release = self.gate(), self.gate()
        entered, completed = [], []
        finished = threading.Event()
        scheduled = [(job('N' + str(i)), False) for i in range(14)] + [(job('R' + str(i)), True) for i in range(2)]

        def run(assigned, *_args, review=False, **_kwargs):
            with self.mutex:
                entered.append((assigned[1], review))
            if not (review_release if review else new_release).wait(5):
                raise AssertionError('Synthetic pool task was not released')

        def dispatch():
            try:
                for future in prepared.scheduled_futures(scheduled, 'NEVER_EXECUTED', {}, 8):
                    future.result()
                    with self.mutex:
                        completed.append(True)
            except BaseException as error:
                self.errors.append(error)
            finally:
                finished.set()

        with patch.object(prepared, 'job_lease', side_effect=lambda j: footprint([j[1]])), patch.object(prepared, 'run_job', side_effect=run):
            thread = threading.Thread(target=dispatch, name='synthetic-real-pools', daemon=True)
            self.threads.append(thread)
            thread.start()
            self.until(lambda: sum(review for _, review in entered) == 2,
                       'New backlog starved dedicated review executors')
            self.assertEqual(sum(not review for _, review in entered), 6)
            self.assertEqual(prepared.ACTIVE, 8)
            review_release.set()
            self.until(lambda: len(completed) == 2)
            self.assertFalse(finished.is_set(), 'Held new tasks unexpectedly finished')
            new_release.set()
            self.drained()
        self.assertEqual(len(completed), 16)

    def test_real_pool_dispatch_skips_conflicts_instead_of_occupying_all_new_threads(self):
        owner_release = self.gate()
        owner_entered, independent_entered = threading.Event(), threading.Event()
        entered = []
        scheduled = [(job('blocked-' + str(i)), False) for i in range(8)] + [(job('independent'), False)]

        def acquire(assigned):
            identifier = assigned[1]
            if identifier == 'R-owner':
                return footprint(['SHARED_TARGET'])
            if identifier.startswith('blocked-'):
                return footprint([identifier], ['SHARED_TARGET'])
            return footprint([identifier])

        def run(assigned, *_args, **_kwargs):
            identifier = assigned[1]
            with self.mutex:
                entered.append(identifier)
            if identifier == 'R-owner':
                owner_entered.set()
                if not owner_release.wait(5):
                    raise AssertionError('Synthetic review owner was not released')
            elif identifier == 'independent':
                independent_entered.set()

        def dispatch():
            try:
                for future in prepared.scheduled_futures(scheduled, 'NEVER_EXECUTED', {}, 8):
                    future.result()
            except BaseException as error:
                self.errors.append(error)

        with patch.object(prepared, 'job_lease', side_effect=acquire), patch.object(prepared, 'run_job', side_effect=run):
            # Establish the conflicting owner first. Global queue position does
            # not promise ordering between dedicated role executors.
            self.start('R-owner', True)
            self.assertTrue(owner_entered.wait(2))
            thread = threading.Thread(target=dispatch, name='synthetic-pool-conflicts', daemon=True)
            self.threads.append(thread)
            thread.start()
            self.assertTrue(independent_entered.wait(2), 'Conflicting admissions exhausted all executor threads')
            self.assertFalse(any(x.startswith('blocked-') for x in entered))
            owner_release.set()
            self.drained()
        self.assertEqual(len(entered), 10)

    def test_real_pool_dispatch_with_review_zero_finishes_without_running_paused_reviews(self):
        self.configure(new=6, review=0)
        entered, completed = [], []
        scheduled = [(job('R' + str(i)), True) for i in range(4)] + [(job('N' + str(i)), False) for i in range(3)]

        def run(assigned, *_args, review=False, **_kwargs):
            if review:
                raise AssertionError('Zero-quota review reached a worker')
            entered.append(assigned[1])

        def dispatch():
            try:
                for future in prepared.scheduled_futures(scheduled, 'NEVER_EXECUTED', {}, 8):
                    future.result()
                    completed.append(True)
            except BaseException as error:
                self.errors.append(error)

        with patch.object(prepared, 'job_lease', side_effect=lambda j: footprint([j[1]])), patch.object(prepared, 'run_job', side_effect=run):
            thread = threading.Thread(target=dispatch, name='synthetic-paused-review-pool', daemon=True)
            self.threads.append(thread)
            thread.start()
            self.drained()
        self.assertEqual(set(entered), {'N0', 'N1', 'N2'})
        self.assertEqual(len(completed), 3)
        self.assertFalse(prepared.STOP.is_set(), 'Pausing reviews must not stop new drafting')

    def test_slow_completed_future_consumer_does_not_pause_new_or_review_admissions(self):
        consumer_resume = self.gate()
        first_delivered = threading.Event()
        entered, completed = [], []
        running = {'new': 0, 'review': 0}
        peaks = {'new': 0, 'review': 0, 'total': 0}
        scheduled = [(job('N' + str(i)), False) for i in range(18)] + [(job('R' + str(i)), True) for i in range(6)]
        releases = {assigned[1]: self.gate() for assigned, _ in scheduled}
        threads_before = {t.ident for t in threading.enumerate()}

        def run(assigned, *_args, review=False, **_kwargs):
            role = 'review' if review else 'new'
            with self.mutex:
                running[role] += 1
                peaks[role] = max(peaks[role], running[role])
                peaks['total'] = max(peaks['total'], sum(running.values()))
                entered.append(assigned[1])
            try:
                if not releases[assigned[1]].wait(5):
                    raise AssertionError('Synthetic worker release was not signalled')
            finally:
                with self.mutex:
                    running[role] -= 1

        def consume_slowly():
            try:
                iterator = prepared.scheduled_futures(scheduled, 'NEVER_EXECUTED', {}, 8)
                first = next(iterator)
                first.result()
                completed.append(True)
                first_delivered.set()
                if not consumer_resume.wait(5):
                    raise AssertionError('Synthetic slow consumer was not resumed')
                for future in iterator:
                    future.result()
                    completed.append(True)
            except BaseException as error:
                self.errors.append(error)

        with patch.object(prepared, 'job_lease', side_effect=lambda j: footprint([j[1]])), patch.object(prepared, 'run_job', side_effect=run):
            thread = threading.Thread(target=consume_slowly, name='synthetic-slow-completed-consumer', daemon=True)
            self.threads.append(thread)
            thread.start()
            self.until(lambda: len(entered) == 8)
            releases['N0'].set()
            self.assertTrue(first_delivered.wait(2))
            self.assertFalse(consumer_resume.is_set())
            for release in releases.values():
                release.set()
            self.until(lambda: len(entered) == 24,
                       'Admissions stopped while the main consumer was handling a completed future')
            self.assertEqual(len(completed), 1, 'The synthetic consumer was meant to remain paused')
            self.assertLessEqual(peaks['new'], 6)
            self.assertLessEqual(peaks['review'], 2)
            self.assertLessEqual(peaks['total'], 8)
            consumer_resume.set()
            self.drained()
        self.assertEqual(len(completed), 24)
        self.until(lambda: not [t for t in threading.enumerate() if t.ident not in threads_before],
                   'Dispatcher or executor thread survived normal queue exhaustion')

    def test_dispatcher_delivers_worker_error_then_stop_drains_without_thread_leak(self):
        release, failure_release, error_delivered = self.gate(), self.gate(), threading.Event()
        entered, failures = [], []
        scheduled = [(job('N' + str(i)), False) for i in range(18)] + [(job('R' + str(i)), True) for i in range(5)]
        threads_before = {t.ident for t in threading.enumerate()}

        def run(assigned, *_args, **_kwargs):
            with self.mutex:
                entered.append(assigned[1])
            if assigned[1] == 'N0':
                if not failure_release.wait(5):
                    raise AssertionError('Synthetic failure trigger was not released')
                raise RuntimeError('Synthetic failing article')
            if not release.wait(5):
                raise AssertionError('Synthetic active article was not released')

        def consume():
            try:
                for future in prepared.scheduled_futures(scheduled, 'NEVER_EXECUTED', {}, 8):
                    try:
                        future.result()
                    except RuntimeError as error:
                        failures.append(str(error))
                        prepared.STOP.set()
                        with prepared.SLOTS:
                            prepared.SLOTS.notify_all()
                        error_delivered.set()
            except BaseException as error:
                self.errors.append(error)

        with patch.object(prepared, 'job_lease', side_effect=lambda j: footprint([j[1]])), patch.object(prepared, 'run_job', side_effect=run):
            thread = threading.Thread(target=consume, name='synthetic-error-stop-consumer', daemon=True)
            self.threads.append(thread)
            thread.start()
            self.until(lambda: len(entered) == 8)
            failure_release.set()
            self.assertTrue(error_delivered.wait(2))
            release.set()
            self.drained()
        self.assertEqual(failures, ['Synthetic failing article'])
        self.assertLess(len(entered), len(scheduled), 'STOP failed to leave unadmitted work pending')
        self.assertEqual(prepared.ACTIVE_BY_KIND, {'new': 0, 'review': 0})
        self.until(lambda: not [t for t in threading.enumerate() if t.ident not in threads_before],
                   'Dispatcher or executor thread survived error/STOP drainage')

    def test_fatal_worker_stops_refill_even_while_completed_future_consumer_is_paused(self):
        success_release, fatal_release, active_release, consumer_resume = [self.gate() for _ in range(4)]
        first_delivered = threading.Event()
        entered, failures, submissions = [], [], []
        scheduled = [(job('N' + str(i)), False) for i in range(18)] + [(job('R' + str(i)), True) for i in range(6)]
        threads_before = {t.ident for t in threading.enumerate()}
        real_executor = prepared.review_lanes.concurrent.futures.ThreadPoolExecutor

        class RecordingExecutor:
            def __init__(self, **kwargs):
                self.delegate = real_executor(**kwargs)

            def __enter__(self):
                self.delegate.__enter__()
                return self

            def __exit__(self, *args):
                return self.delegate.__exit__(*args)

            def submit(self, function, *args, **kwargs):
                with self_outer.mutex:
                    submissions.append(args[0][1])
                return self.delegate.submit(function, *args, **kwargs)

        self_outer = self

        def run(assigned, *_args, **_kwargs):
            identifier = assigned[1]
            with self.mutex:
                entered.append(identifier)
            if identifier == 'N0':
                if not success_release.wait(5):
                    raise AssertionError('Initial synthetic result was not released')
            elif identifier == 'N1':
                if not fatal_release.wait(5):
                    raise AssertionError('Synthetic fatal failure was not triggered')
                raise RuntimeError('Synthetic fatal while consumer paused')
            elif not active_release.wait(5):
                raise AssertionError('Synthetic active job was not drained')

        def consume_slowly():
            try:
                iterator = prepared.scheduled_futures(scheduled, 'NEVER_EXECUTED', {}, 8)
                next(iterator).result()
                first_delivered.set()
                if not consumer_resume.wait(5):
                    raise AssertionError('Synthetic slow consumer was not resumed')
                for future in iterator:
                    try:
                        future.result()
                    except RuntimeError as error:
                        failures.append(str(error))
            except BaseException as error:
                self.errors.append(error)

        with patch.object(prepared, 'job_lease', side_effect=lambda j: footprint([j[1]])), \
             patch.object(prepared, 'run_job', side_effect=run), \
             patch.object(prepared.review_lanes.concurrent.futures, 'ThreadPoolExecutor', RecordingExecutor):
            thread = threading.Thread(target=consume_slowly, name='synthetic-paused-consumer-fatal-worker', daemon=True)
            self.threads.append(thread)
            thread.start()
            self.until(lambda: len(entered) == 8)
            success_release.set()
            self.assertTrue(first_delivered.wait(2))
            self.until(lambda: 'N6' in entered, 'Normal refill was not independent of the paused consumer')
            fatal_release.set()
            self.until(prepared.STOP.is_set,
                       'Dispatcher left future admissions open until the paused main consumer observed a fatal error')
            self.assertFalse(consumer_resume.is_set())
            self.assertNotIn('N7', entered, 'A replacement new job started after the fatal future')
            self.assertNotIn('N7', submissions, 'A replacement future was submitted after the fatal worker')
            self.assertEqual(failures, [], 'Fatal result should still be queued for the paused consumer')
            active_release.set()
            self.until(lambda: prepared.ACTIVE == 0, 'Active jobs did not drain independently of the paused consumer')
            self.assertNotIn('N7', entered)
            self.assertNotIn('N7', submissions)
            consumer_resume.set()
            self.drained()
        self.assertEqual(failures, ['Synthetic fatal while consumer paused'])
        self.assertEqual(prepared.ACTIVE_BY_KIND, {'new': 0, 'review': 0})
        self.until(lambda: not [t for t in threading.enumerate() if t.ident not in threads_before],
                   'Dispatcher or executor thread survived fatal/paused-consumer drainage')

    def test_cancelled_future_that_never_started_releases_its_reserved_role_and_lease(self):
        class CancelBeforeStartingExecutor:
            def __init__(self, **_kwargs):
                pass

            def __enter__(self):
                return self

            def __exit__(self, *_args):
                return False

            def submit(self, *_args, **_kwargs):
                future = prepared.concurrent.futures.Future()
                future.cancel()
                # Executor protocol notifies waiters even when cancel wins.
                future.set_running_or_notify_cancel()
                return future

        threads_before = {t.ident for t in threading.enumerate()}
        with patch.object(prepared, 'job_lease', return_value=footprint(['SYNTHETIC|A'])), \
             patch.object(prepared, 'run_job') as run, \
             patch.object(prepared.review_lanes.concurrent.futures, 'ThreadPoolExecutor', CancelBeforeStartingExecutor):
            futures = list(prepared.scheduled_futures([(job('A'), True)], 'NEVER_EXECUTED', {}, 8))
        self.assertEqual(len(futures), 1)
        self.assertTrue(futures[0].cancelled())
        run.assert_not_called()
        self.assertTrue(prepared.STOP.is_set())
        self.assertEqual(prepared.ACTIVE, 0, 'Cancelled future never entered run_in_slot.finally')
        self.assertEqual(prepared.ACTIVE_BY_KIND, {'new': 0, 'review': 0})
        self.assertEqual(prepared.ACTIVE_LEASES, {})
        self.until(lambda: not [t for t in threading.enumerate() if t.ident not in threads_before],
                   'Dispatcher survived cancelled-future drainage')

    def test_closing_completed_iterator_cancels_future_admissions_and_joins_dispatcher(self):
        close_requested, closing, closed = self.gate(), threading.Event(), threading.Event()
        scheduled = [(job('N' + str(i)), False) for i in range(24)] + [(job('R' + str(i)), True) for i in range(8)]
        releases = {assigned[1]: self.gate() for assigned, _ in scheduled}
        entered = []
        threads_before = {t.ident for t in threading.enumerate()}

        def run(assigned, *_args, **_kwargs):
            with self.mutex:
                entered.append(assigned[1])
            if not releases[assigned[1]].wait(5):
                raise AssertionError('Synthetic active job not released during close')

        def consume_then_close():
            try:
                iterator = prepared.scheduled_futures(scheduled, 'NEVER_EXECUTED', {}, 8)
                next(iterator).result()
                if not close_requested.wait(5):
                    raise AssertionError('Synthetic iterator close was not requested')
                closing.set()
                iterator.close()
            except BaseException as error:
                self.errors.append(error)
            finally:
                closed.set()

        with patch.object(prepared, 'job_lease', side_effect=lambda j: footprint([j[1]])), patch.object(prepared, 'run_job', side_effect=run):
            thread = threading.Thread(target=consume_then_close, name='synthetic-closing-consumer', daemon=True)
            self.threads.append(thread)
            thread.start()
            self.until(lambda: len(entered) == 8)
            releases['N0'].set()
            close_requested.set()
            self.assertTrue(closing.wait(2))
            # The closer must first signal its local admission stop and may
            # then wait for real active work to finish, without cancelling it.
            self.until(lambda: bool(prepared.STOP.is_set()) or
                       json.loads((self.runtime / 'admission-status.json').read_text()).get('action') in {'draining', 'stopped'},
                       'Closing iterator did not stop local admissions')
            for release in releases.values():
                release.set()
            self.assertTrue(closed.wait(2), 'Closing iterator did not join its dispatcher')
            self.drained()
        self.assertLess(len(entered), len(scheduled))
        self.assertEqual(prepared.ACTIVE_BY_KIND, {'new': 0, 'review': 0})
        self.until(lambda: not [t for t in threading.enumerate() if t.ident not in threads_before],
                   'Dispatcher or executor thread survived iterator close')

    def test_pool_submission_failure_releases_the_preacquired_role_and_lease(self):
        class RejectingExecutor:
            def __init__(self, **_kwargs):
                pass

            def __enter__(self):
                return self

            def __exit__(self, *_args):
                return False

            def submit(self, *_args, **_kwargs):
                raise RuntimeError('Synthetic executor rejected submission')

        with patch.object(prepared, 'job_lease', return_value=footprint(['SYNTHETIC|A'])), \
             patch.object(prepared, 'run_job') as run, \
             patch.object(prepared.review_lanes.concurrent.futures, 'ThreadPoolExecutor', RejectingExecutor):
            futures = list(prepared.scheduled_futures([(job('A'), True)], 'NEVER_EXECUTED', {}, 8))
        self.assertEqual(len(futures), 1)
        with self.assertRaisesRegex(RuntimeError, 'executor rejected'):
            futures[0].result()
        run.assert_not_called()
        self.assertEqual(prepared.ACTIVE, 0)
        self.assertEqual(prepared.ACTIVE_LEASES, {})
        self.assertEqual(prepared.ACTIVE_BY_KIND, {'new': 0, 'review': 0})

    def test_conflicts_serialize_across_lanes_but_independent_review_can_start(self):
        for new_first in [True, False]:
            with self.subTest(new_first=new_first):
                held, entered, attempted, blocked, independent = self.gate(), threading.Event(), threading.Event(), threading.Event(), threading.Event()
                leases = {'owner': footprint(['SHARED_TARGET']),
                          'reader': footprint(['OTHER_ARTICLE'], ['SHARED_TARGET']),
                          'independent': footprint(['INDEPENDENT'])}

                def acquire(assigned):
                    if assigned[1] == 'reader':
                        attempted.set()
                    return leases[assigned[1]]

                def run(assigned, *_args, **_kwargs):
                    if assigned[1] == 'owner':
                        entered.set()
                        if not held.wait(5):
                            raise AssertionError('Synthetic owner not released')
                    elif assigned[1] == 'reader':
                        blocked.set()
                    else:
                        independent.set()

                with patch.object(prepared, 'job_lease', side_effect=acquire), patch.object(prepared, 'run_job', side_effect=run):
                    self.start('owner', not new_first)
                    self.assertTrue(entered.wait(2))
                    self.start('reader', new_first)
                    self.assertTrue(attempted.wait(2))
                    self.start('independent', True)
                    self.assertTrue(independent.wait(2))
                    self.assertFalse(blocked.wait(.05), 'Cross-lane reader bypassed writer lease')
                    held.set()
                    self.until(blocked.is_set)
                    self.drained()

    def test_hot_zero_review_limit_drains_active_reviews_and_keeps_six_new_slots(self):
        gates = {identifier: self.gate() for identifier in ['N' + str(i) for i in range(8)] + ['R0', 'R1']}
        entered = set()

        def run(assigned, *_args, **_kwargs):
            identifier = assigned[1]
            with self.mutex:
                entered.add(identifier)
            if identifier not in gates:
                raise AssertionError('Paused review was newly admitted')
            if not gates[identifier].wait(5):
                raise AssertionError('Synthetic active job not released')

        with patch.object(prepared, 'job_lease', side_effect=lambda j: footprint([j[1]])), patch.object(prepared, 'run_job', side_effect=run):
            for index in range(6):
                self.start('N' + str(index))
            self.start('R0', True)
            self.start('R1', True)
            self.until(lambda: len(entered) == 8)
            waiting_review = self.start('R2', True)
            self.configure(new=6, review=0)
            self.assertEqual(prepared.ACTIVE, 8, 'Lower limit must not kill active jobs')
            self.assertTrue(waiting_review.wait(2), 'Paused reviews must return for later resumption, not hang the pool')
            self.assertNotIn('R2', entered)
            gates['R0'].set()
            gates['R1'].set()
            self.until(lambda: prepared.ACTIVE == 6)
            self.start('N6')
            self.start('N7')
            self.assertFalse(gates['N0'].is_set())
            self.assertEqual(len([x for x in entered if x.startswith('N')]), 6)
            gates['N0'].set()
            gates['N1'].set()
            self.until(lambda: {'N6', 'N7'} <= entered)
            self.assertEqual(prepared.ACTIVE, 6)
            for gate in gates.values():
                gate.set()
            self.drained()

    def test_stop_cancels_waiters_in_both_lanes_and_drains_existing_jobs(self):
        self.configure(new=1, review=1)
        release, entered = self.gate(), set()

        def run(assigned, *_args, **_kwargs):
            with self.mutex:
                entered.add(assigned[1])
            if not release.wait(5):
                raise AssertionError('Synthetic active job not released')

        with patch.object(prepared, 'job_lease', side_effect=lambda j: footprint([j[1]])), patch.object(prepared, 'run_job', side_effect=run):
            self.start('new-active')
            self.start('review-active', True)
            self.until(lambda: len(entered) == 2)
            new_waiter = self.start('new-waiting')
            review_waiter = self.start('review-waiting', True)
            prepared.STOP.set()
            with prepared.SLOTS:
                prepared.SLOTS.notify_all()
            self.assertTrue(new_waiter.wait(2))
            self.assertTrue(review_waiter.wait(2))
            self.assertEqual(entered, {'new-active', 'review-active'})
            self.assertEqual(prepared.ACTIVE, 2)
            release.set()
            self.drained()

    def test_expanded_review_footprint_releases_partial_lease_and_recaptures_after_writers(self):
        writer_release, intervening_release = self.gate(), self.gate()
        writer_entered, captured, intervening_entered = threading.Event(), threading.Event(), threading.Event()
        records, fake_db = self.fake_database()
        results, captures = [], []

        def snapshot(*_args):
            captures.append(True)
            captured.set()
            return {'targets': {'SYNTHETIC|B': {'body': 'fresh' if writer_release.is_set() else 'old'}}}

        def run(assigned, *_args, **_kwargs):
            identifier = assigned[1]
            if identifier == 'B':
                writer_entered.set()
                if not writer_release.wait(5):
                    raise AssertionError('Writer not released')
            elif identifier == 'A':
                results.append(prepared.capture_for_attempt(assigned[2], [{'proposed_xml': 'New reference to B'}]))
            else:
                intervening_entered.set()
                if not intervening_release.wait(5):
                    raise AssertionError('Intervening writer not released')

        def acquire(assigned):
            return footprint(['SYNTHETIC|' + ('A' if assigned[1] == 'C' else assigned[1])])

        with patch.object(prepared, 'job_lease', side_effect=acquire), patch.object(prepared, 'run_job', side_effect=run), \
             patch.object(prepared, 'open_db', side_effect=fake_db), patch.object(prepared.reference_audit, 'capture', side_effect=snapshot):
            self.start('B')
            self.assertTrue(writer_entered.wait(2))
            self.start('A', True)
            self.assertTrue(captured.wait(2))
            self.until(lambda: len(prepared.ACTIVE_LEASES) == 1)
            self.start('C')
            self.assertTrue(intervening_entered.wait(2), 'Waiting review retained its partial write lease')
            writer_release.set()
            self.assertEqual(results, [])
            intervening_release.set()
            self.drained()
        self.assertEqual(results, [{'targets': {'SYNTHETIC|B': {'body': 'fresh'}}}])
        self.assertEqual(len(captures), 2)
        self.assertTrue(all(r['closed'] and r['statements'] == ['BEGIN'] for r in records))

    def test_stop_during_expanded_review_footprint_returns_no_snapshot(self):
        release, writer_entered, captured = self.gate(), threading.Event(), threading.Event()
        records, fake_db = self.fake_database()
        results = []

        def run(assigned, *_args, **_kwargs):
            if assigned[1] == 'B':
                writer_entered.set()
                if not release.wait(5):
                    raise AssertionError('Writer not released')
            else:
                results.append(prepared.capture_for_attempt(assigned[2], []))

        def snapshot(*_args):
            captured.set()
            return {'targets': {'SYNTHETIC|B': {}}}

        with patch.object(prepared, 'job_lease', side_effect=lambda j: footprint(['SYNTHETIC|' + j[1]])), \
             patch.object(prepared, 'run_job', side_effect=run), patch.object(prepared, 'open_db', side_effect=fake_db), \
             patch.object(prepared.reference_audit, 'capture', side_effect=snapshot):
            self.start('B')
            self.assertTrue(writer_entered.wait(2))
            review_done = self.start('A', True)
            self.assertTrue(captured.wait(2))
            self.until(lambda: len(prepared.ACTIVE_LEASES) == 1)
            prepared.STOP.set()
            with prepared.SLOTS:
                prepared.SLOTS.notify_all()
            self.assertTrue(review_done.wait(2))
            self.assertEqual(results, [None])
            release.set()
            self.drained()
        self.assertTrue(all(r['closed'] for r in records))

    def test_real_pool_transfers_the_reserved_lease_context_to_review_threads(self):
        release, writer_entered, captured = self.gate(), threading.Event(), threading.Event()
        results, tokens = [], []
        records, fake_db = self.fake_database()

        def snapshot(*_args):
            captured.set()
            return {'targets': {'SYNTHETIC|B': {'body': 'fresh' if release.is_set() else 'old'}}}

        def run(assigned, *_args, review=False, **_kwargs):
            if assigned[1] == 'B':
                writer_entered.set()
                if not release.wait(5):
                    raise AssertionError('Synthetic writer not released')
            else:
                tokens.append(getattr(prepared.LEASE_CONTEXT, 'token', None))
                results.append(prepared.capture_for_attempt(assigned[2], []))

        def dispatch():
            try:
                for future in prepared.scheduled_futures([(job('B'), False), (job('A'), True)], 'NEVER_EXECUTED', {}, 8):
                    future.result()
            except BaseException as error:
                self.errors.append(error)

        with patch.object(prepared, 'job_lease', side_effect=lambda j: footprint(['SYNTHETIC|' + j[1]])), \
             patch.object(prepared, 'run_job', side_effect=run), patch.object(prepared, 'open_db', side_effect=fake_db), \
             patch.object(prepared.reference_audit, 'capture', side_effect=snapshot):
            thread = threading.Thread(target=dispatch, name='synthetic-reserved-review-context', daemon=True)
            self.threads.append(thread)
            thread.start()
            self.assertTrue(writer_entered.wait(2))
            self.assertTrue(captured.wait(2))
            self.until(lambda: len(prepared.ACTIVE_LEASES) == 1)
            self.assertEqual(results, [], 'Review bypassed shared lease after pool submission')
            release.set()
            self.drained()
        self.assertEqual(len(tokens), 1)
        self.assertIsNotNone(tokens[0])
        self.assertEqual(results, [{'targets': {'SYNTHETIC|B': {'body': 'fresh'}}}])
        self.assertEqual(len(records), 2)
        self.assertTrue(all(r['closed'] for r in records))

    def test_exceptions_in_either_lane_release_global_count_and_dependency_lease(self):
        for review in [False, True]:
            with self.subTest(review=review), patch.object(prepared, 'job_lease', return_value=footprint(['SYNTHETIC|A'])), \
                 patch.object(prepared, 'run_job', side_effect=RuntimeError('Synthetic isolated failure')):
                with self.assertRaisesRegex(RuntimeError, 'isolated failure'):
                    prepared.run_in_slot(job('A'), 'NEVER_EXECUTED', {}, 8, review)
                self.assertEqual(prepared.ACTIVE, 0)
                self.assertEqual(prepared.ACTIVE_LEASES, {})
                self.assertIsNone(prepared.LEASE_CONTEXT.token)

    def test_native_execution_evidence_is_required_before_validation_in_both_lanes(self):
        for review in [False, True]:
            for header_kind in ['wrong_model', 'missing_response']:
                with self.subTest(review=review, header_kind=header_kind):
                    prepared.STOP.clear()
                    (self.runtime / 'site-summaries.json').write_text('{}')
                    (self.runtime / 'policy-coordinations.json').write_text('{}')
                    database = SimpleNamespace(execute=lambda *_args: [], close=lambda: None)
                    measurement = {}

                    def fake_cli(_command, **kwargs):
                        folder = Path(kwargs['cwd'])
                        model = 'gpt-6-sol' if header_kind == 'wrong_model' else 'gpt-6-astra'
                        response = '\nthinking\n' if header_kind == 'wrong_model' else '\n'
                        kwargs['stderr'].write('OpenAI Codex v0.0\n--------\n'
                                               f'workdir: {folder}\nmodel: {model}\nprovider: openai\n'
                                               'reasoning effort: medium\nsession id: 12345678-1234-1234-1234-123456789abc\n--------\n' + response)
                        kwargs['stderr'].flush()
                        return SimpleNamespace(returncode=0)

                    with patch.object(prepared, 'open_db', return_value=database), \
                         patch.object(prepared, 'past_before_job', return_value=[]), \
                         patch.object(prepared, 'capture_for_attempt', return_value={'targets': {}}), \
                         patch.object(prepared, 'invoke_agent', side_effect=fake_cli) as fake_invoke, \
                         patch.object(prepared, 'progress', return_value={}), \
                         patch.object(prepared, 'validate_answer') as validate, \
                         patch.object(prepared.reference_audit, 'accept_checks') as accept:
                        prepared._run_job(('synthetic', 1, [article('A')]), 'NEVER_EXECUTED', {}, review, measurement)
                    self.assertEqual(fake_invoke.call_count, 1)
                    validate.assert_not_called()
                    accept.assert_not_called()
                    self.assertTrue(prepared.STOP.is_set())
                    self.assertEqual(measurement['outcome'], 'blocked_execution_evidence')

    def observed_workers(self):
        return [{'pid': 1000 + index, 'ppid': 123,
                 'kind': 'new' if index < 6 else 'review',
                 'execution': {'verified': True, 'model': 'gpt-6-astra',
                               'reasoning_effort': 'medium',
                               'session_id': '00000000-0000-0000-0000-' + str(index).zfill(12)}}
                for index in range(8)]

    def test_native_eight_proof_rejects_an_additional_unverified_active_worker(self):
        prepared.atomic(self.runtime / 'coordinator-run.json',
                        {'pid': 123, 'capacity': 8, 'role_limits': {'new': 6, 'review': 2}, 'started_at_unix': 0})
        workers = self.observed_workers()
        workers.append({'pid': 9999, 'ppid': 123, 'kind': 'review',
                        'execution': {'verified': False, 'status': 'awaiting_model_response'}})
        result = observation.observe(self.runtime, [{'pid': 123}], workers, 100)
        self.assertFalse(result['simultaneous_six_new_plus_two_review_verified'],
                         'Filtering an extra worker cannot establish the eight-worker capacity invariant')

    def test_native_eight_positive_control_uses_all_eight_distinct_sessions_and_roles(self):
        prepared.atomic(self.runtime / 'coordinator-run.json',
                        {'pid': 123, 'capacity': 8, 'role_limits': {'new': 6, 'review': 2}, 'started_at_unix': 0})
        result = observation.observe(self.runtime, [{'pid': 123}], self.observed_workers(), 100)
        self.assertTrue(result['simultaneous_six_new_plus_two_review_verified'])
        self.assertTrue((self.runtime / 'review-lanes-execution.json').is_file())

    def test_native_eight_proof_requires_authorized_coordinator_capacity(self):
        prepared.atomic(self.runtime / 'coordinator-run.json',
                        {'pid': 123, 'capacity': 6, 'started_at_unix': 0})
        result = observation.observe(self.runtime, [{'pid': 123}], self.observed_workers(), 100)
        self.assertFalse(result['simultaneous_six_new_plus_two_review_verified'],
                         'Native response evidence cannot authorize extra workers')

    def test_normative_validation_and_commit_pipeline_are_unchanged_from_baseline(self):
        before = ast.parse((BEFORE / 'run_exhaustive.py').read_text())
        current = ast.parse((STAGING / 'run_exhaustive.py').read_text())
        functions = lambda tree: {n.name: ast.dump(n, include_attributes=False) for n in tree.body if isinstance(n, ast.FunctionDef)}
        old, new = functions(before), functions(current)
        for name in ['validate_answer', 'policy_is_current', 'invoke_agent', '_run_job', 'job_lease', 'leases_conflict', 'capture_for_attempt']:
            with self.subTest(function=name):
                self.assertEqual(new[name], old[name], 'Lane change altered an existing validation or lease contract')
        before_review = functions(ast.parse((BEFORE / 'review_prior.py').read_text()))
        current_review = functions(ast.parse((STAGING / 'review_prior.py').read_text()))
        self.assertEqual(before_review['commit'], current_review['commit'],
                         'Lane change altered the exact source/proposal/batch before-image guards')


if __name__ == '__main__':
    unittest.main(verbosity=2)
