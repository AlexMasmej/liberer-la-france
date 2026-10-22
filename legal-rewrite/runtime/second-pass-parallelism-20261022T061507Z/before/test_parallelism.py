"""Temporary, model-free checks of task capacity and read/write job leases."""
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest import TestCase, main
from unittest.mock import patch
import copy
import json
import threading
import time

import run_exhaustive as coordinator
import worker_capacity as capacity


def article(identifier):
    return {'code_id':'TEST', 'source_id':identifier, 'number':'L1-'+identifier,
            'source_xml':'<p>Complete temporary test source.</p>', 'source_notes_xml':''}


def job(identifier):
    return ('temporary', identifier, [article(identifier)])


def lease(writes=(), reads=()):
    return {'writes':set(writes), 'reads':set(reads)}


class Parallelism(TestCase):
    def setUp(self):
        temporary=TemporaryDirectory(); self.addCleanup(temporary.cleanup)
        self.runtime=Path(temporary.name)
        self.threads=[]; self.releases=[]; self.errors=[]
        self.error_lock=threading.Lock()
        for name,value in [('HERE',self.runtime),('RUNTIME',self.runtime),
                           ('SLOTS',threading.Condition()),('STOP',threading.Event()),
                           ('ACTIVE',0),('ACTIVE_LEASES',{}),('LEASE_CONTEXT',threading.local())]:
            p=patch.object(coordinator,name,value); p.start(); self.addCleanup(p.stop)
        # Any accidental database access fails instead of reaching the corpus.
        p=patch.object(coordinator,'open_db',side_effect=AssertionError('Real DB forbidden in parallelism tests'))
        p.start(); self.addCleanup(p.stop)

    def tearDown(self):
        coordinator.STOP.set()
        for release in self.releases:release.set()
        with coordinator.SLOTS:coordinator.SLOTS.notify_all()
        for thread in self.threads:thread.join(timeout=2)
        self.assertFalse([t.name for t in self.threads if t.is_alive()], 'A simulated task retained its lease')

    def event(self):
        e=threading.Event(); self.releases.append(e); return e

    def wait_until(self,predicate,message='condition did not become true',timeout=3):
        end=time.monotonic()+timeout
        while time.monotonic()<end:
            if predicate():return
            time.sleep(.005)
        self.fail(message)

    def set_limit(self,value):
        coordinator.atomic(self.runtime/'worker-limit.json',{'workers':value})
        with coordinator.SLOTS:coordinator.SLOTS.notify_all()

    def start(self,identifier,maximum=6):
        done=threading.Event()
        def run():
            try:coordinator.run_in_slot(job(identifier),'NO_MODEL',{},maximum)
            except BaseException as error:
                with self.error_lock:self.errors.append(error)
            finally:done.set()
        thread=threading.Thread(target=run,name='simulated-'+identifier,daemon=True)
        self.threads.append(thread); thread.start(); return done

    def finished(self):
        for thread in self.threads:thread.join(timeout=3)
        self.assertFalse([t.name for t in self.threads if t.is_alive()])
        self.assertEqual(self.errors,[])
        self.assertEqual(coordinator.ACTIVE,0)
        self.assertEqual(coordinator.ACTIVE_LEASES,{})

    def fake_db(self):
        calls=[]; guard=threading.Lock()
        def open_database(_):
            item={'thread':threading.current_thread().name,'statements':[],'closed':False}
            with guard:calls.append(item)
            return SimpleNamespace(execute=lambda statement:item['statements'].append(statement),
                                   close=lambda:item.update(closed=True))
        return calls,open_database

    def test_task_settings_default_three_and_manual_reservations(self):
        self.assertEqual(capacity.settings(self.runtime),{'capacity':3,'current_workers':3})
        self.assertEqual(capacity.drafting_slots(self.runtime),3)
        coordinator.atomic(self.runtime/'parallelism-plan.json',{'capacity':6,'current_workers':4})
        self.assertEqual(capacity.drafting_slots(self.runtime),4)
        self.assertEqual(capacity.drafting_slots(self.runtime,['manual-A']),3)
        self.assertEqual(capacity.drafting_slots(self.runtime,['manual-A','manual-B']),2)
        coordinator.atomic(self.runtime/'parallelism-plan.json',{'capacity':6,'current_workers':6})
        self.assertEqual(capacity.drafting_slots(self.runtime,['manual-A','manual-B']),4)
        self.assertEqual(capacity.MAX_WORKERS,6)

    def test_invalid_task_plan_cannot_exceed_six_or_use_bool(self):
        for plan in [{'capacity':7,'current_workers':6},{'capacity':6,'current_workers':7},
                     {'capacity':4,'current_workers':6},{'capacity':True,'current_workers':1},
                     {'capacity':6,'current_workers':0},{'capacity':6,'current_workers':2.5}]:
            with self.subTest(plan=plan):
                coordinator.atomic(self.runtime/'parallelism-plan.json',plan)
                with self.assertRaises(ValueError):capacity.settings(self.runtime)

    def test_worker_limit_explicit_ceiling_and_hot_file(self):
        # No plan defaults to three; explicit --workers 6 remains authorized
        # when the separate worker-limit file is absent.
        self.assertEqual(coordinator.worker_limit(6),6)
        self.assertEqual(coordinator.worker_limit(3),3)
        self.set_limit(4)
        self.assertEqual(coordinator.worker_limit(6),4)
        self.assertEqual(coordinator.worker_limit(3),3)
        for value in [0,7,True,2.5]:
            with self.subTest(maximum=value),self.assertRaises(ValueError):coordinator.worker_limit(value)
        for value in [0,7,True,2.5]:
            coordinator.atomic(self.runtime/'worker-limit.json',{'workers':value})
            with self.subTest(file_value=value),self.assertRaises(ValueError):coordinator.worker_limit(6)

    def test_job_lease_collects_reads_and_removes_own_writes(self):
        database=SimpleNamespace(close=lambda:closed.append(True))
        closed=[]; a,b=article('A'),article('B')
        def requirements(row,**kwargs):
            self.assertIs(kwargs['db'],database)
            return {'TEST|A','TEST|B','TEST|X' if row is a else 'OTHER_CODE|Y'}
        with patch.object(coordinator,'open_db',return_value=database),\
             patch.object(coordinator.reference_audit,'requirements',side_effect=requirements) as required:
            got=coordinator.job_lease(('temporary',1,[a,b]))
        self.assertEqual(got,lease(['TEST|A','TEST|B'],['TEST|X','OTHER_CODE|Y']))
        self.assertEqual(required.call_count,2); self.assertEqual(closed,[True])

    def test_read_read_allowed_write_read_and_write_write_conflict_symmetrically(self):
        a=lease(['A'],['COMMON']); b=lease(['B'],['COMMON'])
        self.assertFalse(coordinator.leases_conflict(a,b))
        for other in [lease(['COMMON']),lease(['B'],['A']),lease(['A'])]:
            with self.subTest(other=other):
                self.assertTrue(coordinator.leases_conflict(a,other))
                self.assertTrue(coordinator.leases_conflict(other,a))

    def test_six_independent_jobs_with_shared_reads_overlap(self):
        self.set_limit(6); started=set(); lock=threading.Lock(); release=self.event()
        def run(j,*_,**__):
            with lock:started.add(j[1])
            self.assertTrue(release.wait(4),'Simulated tasks were not released')
        with patch.object(coordinator,'job_lease',side_effect=lambda j:lease(['TEST|'+j[1]],['COMMON'])),\
             patch.object(coordinator,'run_job',side_effect=run):
            for i in range(6):self.start(str(i))
            self.wait_until(lambda:len(started)==6,'Six independent jobs should run together')
            self.assertEqual(coordinator.ACTIVE,6); self.assertEqual(len(coordinator.ACTIVE_LEASES),6)
            release.set(); self.finished()

    def test_conflicting_writer_or_reader_waits_while_independent_job_runs(self):
        for kind in ['write-read','write-write']:
            with self.subTest(kind=kind):
                self.set_limit(6); holding=self.event(); entered=threading.Event(); attempted=threading.Event()
                blocked=threading.Event(); independent=threading.Event()
                footprints={'A':lease(['TARGET']),
                            'B':lease(['OTHER'],['TARGET']) if kind=='write-read' else lease(['TARGET']),
                            'C':lease(['INDEPENDENT'])}
                def get_lease(j):
                    if j[1]=='B':attempted.set()
                    return footprints[j[1]]
                def run(j,*_,**__):
                    if j[1]=='A':entered.set();self.assertTrue(holding.wait(4))
                    elif j[1]=='B':blocked.set()
                    else:independent.set()
                with patch.object(coordinator,'job_lease',side_effect=get_lease),\
                     patch.object(coordinator,'run_job',side_effect=run):
                    self.start('A');self.assertTrue(entered.wait(2));self.start('B')
                    self.assertTrue(attempted.wait(2));self.start('C');self.assertTrue(independent.wait(2))
                    self.assertFalse(blocked.wait(.05),'Conflicting job ran before the writer finished')
                    holding.set();self.wait_until(blocked.is_set);self.finished()

    def test_hot_limit_four_to_six_then_reduction_only_drains(self):
        self.set_limit(4); started=[]; lock=threading.Lock(); gates={str(i):self.event() for i in range(8)}
        attempted=set()
        def get_lease(j):
            with lock:attempted.add(j[1])
            return lease(['TEST|'+j[1]])
        def run(j,*_,**__):
            with lock:started.append(j[1])
            self.assertTrue(gates[j[1]].wait(5),'Simulated task was not released')
        with patch.object(coordinator,'job_lease',side_effect=get_lease),patch.object(coordinator,'run_job',side_effect=run):
            for i in range(6):self.start(str(i))
            self.wait_until(lambda:len(attempted)==6 and len(started)==4)
            self.assertEqual(coordinator.ACTIVE,4)
            self.set_limit(6);self.wait_until(lambda:len(started)==6);self.assertEqual(coordinator.ACTIVE,6)
            initial=list(started);self.set_limit(2)
            self.assertEqual(coordinator.ACTIVE,6,'Lowering the cap must not stop current work')
            self.start('6');self.start('7');self.wait_until(lambda:len(attempted)==8)
            for identifier in initial[:4]:gates[identifier].set()
            self.wait_until(lambda:coordinator.ACTIVE==2)
            self.assertEqual(len(started),6,'No replacement may start at the reduced ceiling')
            gates[initial[4]].set();self.wait_until(lambda:len(started)==7)
            self.assertEqual(coordinator.ACTIVE,2)
            gates[initial[5]].set();self.wait_until(lambda:len(started)==8)
            self.assertEqual(coordinator.ACTIVE,2)
            gates['6'].set();gates['7'].set();self.finished()

    def test_stop_before_admission_invokes_nothing(self):
        coordinator.STOP.set()
        with patch.object(coordinator,'job_lease') as get_lease,patch.object(coordinator,'run_job') as run:
            coordinator.run_in_slot(job('A'),'NO_MODEL',{},6)
        get_lease.assert_not_called();run.assert_not_called()
        self.assertEqual(coordinator.ACTIVE,0);self.assertEqual(coordinator.ACTIVE_LEASES,{})

    def test_stop_releases_waiter_and_active_exception_releases_lease(self):
        self.set_limit(1); entered=threading.Event(); waiting=threading.Event(); release=self.event()
        def get_lease(j):
            if j[1]=='B':waiting.set()
            return lease(['TEST|'+j[1]])
        def run(j,*_,**__):
            self.assertEqual(j[1],'A');entered.set();self.assertTrue(release.wait(4))
        with patch.object(coordinator,'job_lease',side_effect=get_lease),patch.object(coordinator,'run_job',side_effect=run):
            self.start('A');self.assertTrue(entered.wait(2));done=self.start('B');self.assertTrue(waiting.wait(2))
            coordinator.STOP.set()
            with coordinator.SLOTS:coordinator.SLOTS.notify_all()
            self.assertTrue(done.wait(2));self.assertEqual(coordinator.ACTIVE,1)
            release.set();self.finished()
        coordinator.STOP.clear()
        with patch.object(coordinator,'job_lease',return_value=lease(['A'])),\
             patch.object(coordinator,'run_job',side_effect=RuntimeError('expected isolated failure')):
            with self.assertRaisesRegex(RuntimeError,'isolated failure'):
                coordinator.run_in_slot(job('A'),'NO_MODEL',{},6)
        self.assertEqual(coordinator.ACTIVE,0);self.assertEqual(coordinator.ACTIVE_LEASES,{})
        self.assertIsNone(coordinator.LEASE_CONTEXT.token)

    def test_capture_without_lease_uses_one_consistent_read_transaction(self):
        calls,open_database=self.fake_db();frozen={'targets':{'TEST|B':{'body':'complete new target'}}}
        with patch.object(coordinator,'open_db',side_effect=open_database),\
             patch.object(coordinator.reference_audit,'capture',return_value=frozen) as capture:
            self.assertIs(coordinator.capture_for_attempt([article('A')],[]),frozen)
        self.assertEqual(capture.call_count,1);self.assertEqual(len(calls),1)
        self.assertEqual(calls[0]['statements'],['BEGIN']);self.assertTrue(calls[0]['closed'])

    def test_retry_expands_read_footprint_waits_and_recaptures_actual_target(self):
        self.set_limit(6); entered=threading.Event(); release=self.event(); expanded=threading.Event()
        result=[];calls,open_database=self.fake_db();captures=[]
        def snapshot(db,expected,provisional):
            self.assertTrue(provisional,'The newly introduced reference comes from the retry answer')
            captures.append(True);expanded.set()
            return {'targets':{'TEST|B':{'body':'fresh-after-wait' if release.is_set() else 'old-before-wait'}}}
        def run(j,*_,**__):
            if j[1]=='B':entered.set();self.assertTrue(release.wait(4))
            else:result.append(coordinator.capture_for_attempt(j[2],[{'proposed_xml':'new reference to B'}]))
        with patch.object(coordinator,'job_lease',side_effect=lambda j:lease(['TEST|'+j[1]])),\
             patch.object(coordinator,'run_job',side_effect=run),\
             patch.object(coordinator,'open_db',side_effect=open_database),\
             patch.object(coordinator.reference_audit,'capture',side_effect=snapshot):
            self.start('B');self.assertTrue(entered.wait(2));self.start('A');self.assertTrue(expanded.wait(2))
            self.wait_until(lambda:len(coordinator.ACTIVE_LEASES)==1,'Waiting expansion must release its old footprint')
            self.assertEqual(result,[]);release.set();self.finished()
        self.assertEqual(result,[{'targets':{'TEST|B':{'body':'fresh-after-wait'}}}])
        self.assertEqual(len(captures),2);self.assertTrue(all(x['closed'] and x['statements']==['BEGIN'] for x in calls))

    def test_opposite_new_references_do_not_hold_partial_leases_and_deadlock(self):
        self.set_limit(6);barrier=threading.Barrier(2);results=[];lock=threading.Lock()
        calls,open_database=self.fake_db()
        def snapshot(db,expected,provisional):
            own=expected[0]['source_id'];other='B' if own=='A' else 'A'
            return {'targets':{'TEST|'+other:{'body':'whole target '+other}}}
        def run(j,*_,**__):
            barrier.wait(timeout=2)
            got=coordinator.capture_for_attempt(j[2],[{'proposed_xml':'new reciprocal reference'}])
            with lock:results.append(got)
        with patch.object(coordinator,'job_lease',side_effect=lambda j:lease(['TEST|'+j[1]])),\
             patch.object(coordinator,'run_job',side_effect=run),\
             patch.object(coordinator,'open_db',side_effect=open_database),\
             patch.object(coordinator.reference_audit,'capture',side_effect=snapshot):
            self.start('A');self.start('B');self.finished()
        self.assertEqual(len(results),2);self.assertTrue(all(x is not None for x in results))
        self.assertEqual(len(calls),4);self.assertTrue(all(x['closed'] for x in calls))

    def test_stop_during_footprint_expansion_returns_none_and_frees_leases(self):
        self.set_limit(6);entered=threading.Event();captured=threading.Event();release=self.event();results=[]
        calls,open_database=self.fake_db()
        def snapshot(*_):captured.set();return {'targets':{'TEST|B':{'body':'complete target'}}}
        def run(j,*_,**__):
            if j[1]=='B':entered.set();self.assertTrue(release.wait(4))
            else:results.append(coordinator.capture_for_attempt(j[2],[{'proposed_xml':'new B reference'}]))
        with patch.object(coordinator,'job_lease',side_effect=lambda j:lease(['TEST|'+j[1]])),\
             patch.object(coordinator,'run_job',side_effect=run),\
             patch.object(coordinator,'open_db',side_effect=open_database),\
             patch.object(coordinator.reference_audit,'capture',side_effect=snapshot):
            self.start('B');self.assertTrue(entered.wait(2));done=self.start('A');self.assertTrue(captured.wait(2))
            self.wait_until(lambda:len(coordinator.ACTIVE_LEASES)==1)
            coordinator.STOP.set()
            with coordinator.SLOTS:coordinator.SLOTS.notify_all()
            self.assertTrue(done.wait(2));self.assertEqual(results,[None])
            release.set();self.finished()
        self.assertTrue(all(x['closed'] for x in calls))

    def test_capture_exception_closes_mock_database_and_releases_active_lease(self):
        calls,open_database=self.fake_db()
        def run(j,*_,**__):coordinator.capture_for_attempt(j[2],[])
        with patch.object(coordinator,'job_lease',return_value=lease(['TEST|A'])),\
             patch.object(coordinator,'run_job',side_effect=run),\
             patch.object(coordinator,'open_db',side_effect=open_database),\
             patch.object(coordinator.reference_audit,'capture',side_effect=ValueError('isolated snapshot error')):
            with self.assertRaisesRegex(ValueError,'snapshot error'):
                coordinator.run_in_slot(job('A'),'NO_MODEL',{},6)
        self.assertEqual(coordinator.ACTIVE,0);self.assertEqual(coordinator.ACTIVE_LEASES,{})
        self.assertEqual(len(calls),1);self.assertTrue(calls[0]['closed'])


if __name__=='__main__':main(verbosity=2)
