"""Bounded synthetic checks. Never invokes a model or opens the real corpus."""
import ast
import fcntl
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import sys
import tempfile
import threading
import time
from types import SimpleNamespace
import unittest
from unittest.mock import patch

STAGE=Path(__file__).resolve().parent
PROJECT=STAGE.parents[1]
sys.path.insert(0,str(PROJECT))
sys.path.insert(0,str(STAGE/'candidate'))
import continuation_tail as tail
import run_exhaustive as c
import worker_capacity as capacity
import review_lanes
import review_prior
import review_lane_observation as observation
import supervise_exhaustive as supervisor
REAL_VERIFY_COMPLETE=tail.verify_complete_inventory


def article(identifier,**extra):
    return {'code_id':'SYNTHETIC','source_id':identifier,'source_sha256':'sha-'+identifier,
            'number':'L-'+identifier,'source_xml':'<p>Whole synthetic normative text.</p>',
            'source_notes_xml':'',**extra}


def job(identifier):return ('temporary',identifier,[article(identifier)])


class Preflight(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='review-reallocation-test-')
        self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name);self.runtime=self.root/'runtime';self.runtime.mkdir()
        self.threads=[];self.releases=[];self.errors=[]
        for name,value in [('HERE',self.root),('RUNTIME',self.runtime),('STOP',threading.Event()),
                           ('SLOTS',threading.Condition()),('ACTIVE',0),('ACTIVE_BY_KIND',{'new':0,'review':0}),
                           ('ACTIVE_LEASES',{}),('LEASE_CONTEXT',threading.local()),('REVIEW_TAIL',False)]:
            stub=patch.object(c,name,value);stub.start();self.addCleanup(stub.stop)
        for name in ['open_db','invoke_agent','register','publish_checkpoint']:
            stub=patch.object(c,name,side_effect=AssertionError('Real I/O forbidden: '+name));stub.start();self.addCleanup(stub.stop)
        self.plan(8)
        (self.runtime/'manual-agent-slots.lock').touch()
        (self.runtime/'manual-agent-slots.json').write_text('[]')
        stub=patch.object(tail,'verify_complete_inventory',return_value={'complete':True,'source_records':1})
        stub.start();self.addCleanup(stub.stop)

    def tearDown(self):
        c.STOP.set()
        for event in self.releases:event.set()
        with c.SLOTS:c.SLOTS.notify_all()
        for thread in self.threads:thread.join(3)
        self.assertFalse([t.name for t in self.threads if t.is_alive()])
        tail.exit_review_tail(c)

    def plan(self,total=8,**extra):
        roles={'new':6,'review':total-6}
        c.atomic(self.runtime/'parallelism-plan.json',{'capacity':8,'current_workers':total,
                 'role_limits':roles,'review_tail_capacity':8,**extra})
        c.atomic(self.runtime/'worker-limit.json',{'workers':total,'role_limits':roles,'review_tail_limit':total})

    def until(self,predicate,timeout=3):
        end=time.monotonic()+timeout
        while time.monotonic()<end:
            if predicate():return
            time.sleep(.003)
        self.fail('Synthetic progress did not occur')

    def gate(self):
        e=threading.Event();self.releases.append(e);return e

    def dispatch(self,scheduled,consume=None):
        def go():
            try:
                for future in c.scheduled_futures(scheduled,'NEVER_A_MODEL',{},8):
                    future.result()
                    if consume:consume()
            except BaseException as error:self.errors.append(error)
        thread=threading.Thread(target=go,name='synthetic-dispatch',daemon=True)
        self.threads.append(thread);thread.start();return thread

    def drained(self,thread):
        thread.join(3);self.assertFalse(thread.is_alive());self.assertEqual(self.errors,[])
        self.assertEqual(c.ACTIVE,0);self.assertEqual(c.ACTIVE_BY_KIND,{'new':0,'review':0});self.assertEqual(c.ACTIVE_LEASES,{})

    def test_candidate_modules_resolve_only_to_candidate(self):
        for module in [c,capacity,review_lanes,tail,supervisor,observation]:
            self.assertEqual(Path(module.__file__).resolve().parent,STAGE/'candidate')

    def test_default_mixed_roles_still_6_and_2_and_seven_is_not_eight(self):
        self.assertEqual(capacity.admission_limits(self.runtime,8)['role_limits'],{'new':6,'review':2})
        self.plan(7)
        self.assertEqual(capacity.admission_limits(self.runtime,8,review_tail=True),
                         {'workers':7,'role_limits':{'new':0,'review':7}})

    def test_tail_needs_authorization_and_does_not_erase_pause_or_manual_slots(self):
        for mutation in ['missing','bool','nine','paused','manual','unexplained']:
            with self.subTest(mutation=mutation):
                self.plan()
                plan=json.loads((self.runtime/'parallelism-plan.json').read_text())
                hot=json.loads((self.runtime/'worker-limit.json').read_text())
                if mutation=='missing':plan.pop('review_tail_capacity')
                elif mutation=='bool':plan['review_tail_capacity']=True
                elif mutation=='nine':plan['review_tail_capacity']=9
                elif mutation=='paused':hot={'workers':6,'role_limits':{'new':6,'review':0}}
                elif mutation=='manual':hot={'workers':6,'role_limits':{'new':4,'review':2}}
                else:hot={'workers':8,'role_limits':{'new':6,'review':1}}
                c.atomic(self.runtime/'parallelism-plan.json',plan);c.atomic(self.runtime/'worker-limit.json',hot)
                with self.assertRaises(ValueError):capacity.admission_limits(self.runtime,8,review_tail=True)

    def test_tail_entry_requires_no_new_no_active_no_leases_and_no_stop(self):
        with self.assertRaises(ValueError):tail.enter_review_tail(c,8,[job('open')])
        for key,value in [('ACTIVE',1),('ACTIVE_BY_KIND',{'new':0,'review':1}),('ACTIVE_LEASES',{'lease':{}})]:
            with self.subTest(key=key),patch.object(c,key,value),self.assertRaises(ValueError):tail.enter_review_tail(c,8,[])
        c.STOP.set()
        with self.assertRaises(ValueError):tail.enter_review_tail(c,8,[])
        c.STOP.clear()
        self.assertEqual(tail.enter_review_tail(c,8,[])['role_limits'],{'new':0,'review':8})
        receipt=json.loads((self.runtime/'continuation-phase.json').read_text())
        self.assertFalse(receipt['execution_verified']);self.assertFalse(receipt['legal_completion_claimed'])

    def test_tail_requires_known_empty_real_manual_inventory_and_marker_blocks_new_reservations(self):
        for value in [None,'invalid-json','{}','["manual-agent"]']:
            path=self.runtime/'manual-agent-slots.json'
            if value is None:path.unlink(missing_ok=True)
            else:path.write_text(value)
            with self.subTest(value=value),self.assertRaises(ValueError):tail.enter_review_tail(c,8,[])
            self.assertFalse(c.REVIEW_TAIL)
        path.write_text('[]')
        with (self.runtime/'manual-agent-slots.lock').open('r+') as other:
            fcntl.flock(other,fcntl.LOCK_EX|fcntl.LOCK_NB)
            with self.assertRaises(BlockingIOError):tail.enter_review_tail(c,8,[])
        tail.enter_review_tail(c,8,[])
        with (self.runtime/'manual-agent-slots.lock').open('r+') as other:
            fcntl.flock(other,fcntl.LOCK_EX|fcntl.LOCK_NB)
            with self.assertRaisesRegex(ValueError,'fully drained review tail'):capacity.slot_document(self.runtime,['new-manual'])
            self.assertEqual(capacity.slot_document(self.runtime,[])['review_tail_limit'],8)
        with patch.object(c,'ACTIVE',1),self.assertRaisesRegex(ValueError,'full review-tail drain'):tail.exit_review_tail(c)
        tail.exit_review_tail(c)
        with (self.runtime/'manual-agent-slots.lock').open('r+') as other:fcntl.flock(other,fcntl.LOCK_EX|fcntl.LOCK_NB)

    def test_uncoordinated_manual_document_change_closes_tail_admissions(self):
        tail.enter_review_tail(c,8,[])
        (self.runtime/'manual-agent-slots.json').write_text('["unexpected-new-reservation"]')
        with self.assertRaisesRegex(ValueError,'explicitly empty'):c.current_limits(8)

    def test_explicit_tail_budget_supports_one_two_four_zero_and_rejects_invalid_values(self):
        tail.enter_review_tail(c,8,[])
        original=json.loads((self.runtime/'worker-limit.json').read_text())
        for limit in [1,2,4,0,8]:
            c.atomic(self.runtime/'worker-limit.json',original|{'review_tail_limit':limit})
            self.assertEqual(c.current_limits(8)['role_limits'],{'new':0,'review':limit})
        for limit in [None,True,-1,9,'4']:
            c.atomic(self.runtime/'worker-limit.json',original|{'review_tail_limit':limit})
            with self.subTest(limit=limit),self.assertRaises(ValueError):c.current_limits(8)
        c.atomic(self.runtime/'worker-limit.json',original)

    def test_zero_tail_budget_defers_following_jobs_and_drains_valid_active_jobs(self):
        tail.enter_review_tail(c,8,[])
        release=self.gate();started=[]
        def run(j,*_,**__):started.append(j[1]);self.assertTrue(release.wait(4))
        with patch.object(c,'job_lease',side_effect=lambda j:{'writes':{j[1]},'reads':set()}),patch.object(c,'run_job',side_effect=run):
            thread=self.dispatch([(job(str(i)),True) for i in range(12)])
            self.until(lambda:len(started)==8)
            document=json.loads((self.runtime/'worker-limit.json').read_text())
            with (self.runtime/'manual-agent-slots.lock').open('r+') as operator:
                fcntl.flock(operator,fcntl.LOCK_EX|fcntl.LOCK_NB)
                c.atomic(self.runtime/'worker-limit.json',document|{'review_tail_limit':0})
            self.until(lambda:json.loads((self.runtime/'admission-deferred.json').read_text())['jobs'])
            self.assertEqual(c.ACTIVE,8);self.assertFalse(c.STOP.is_set())
            release.set();self.drained(thread)
        self.assertEqual(len(started),8)
        deferred=json.loads((self.runtime/'admission-deferred.json').read_text())['jobs']
        self.assertEqual(len(deferred),4);self.assertTrue(all(not j['accepted'] and not j['attempted'] for j in deferred))
        self.assertFalse(c.STOP.is_set())

    def test_supervisor_holds_explicit_zero_tail_budget_without_restarting(self):
        self.plan(8,continuation_mode='recover_new_before_reviews')
        document=json.loads((self.runtime/'worker-limit.json').read_text())
        c.atomic(self.runtime/'worker-limit.json',document|{'review_tail_limit':0})
        c.atomic(self.runtime/'status.json',{'status':'checkpoint','pending':5,'prior_drafts_awaiting_review':50})
        c.atomic(self.runtime/'coordinator-run.json',{'pid':42})
        c.atomic(self.runtime/'continuation-phase.json',{'coordinator_pid':42,'phase':'review_tail_drained',
                 'complete_inventory':{'complete':True,'identity_sha256':'CURRENT'}})
        fresh={'open_accessible_new':0,'held':[],'inventory':{'complete':True,'identity_sha256':'CURRENT'}}
        with patch.object(supervisor,'HERE',self.root),patch.object(supervisor,'RUNTIME',self.runtime),patch.object(supervisor,'SUPERVISION',self.root/'health'),\
             patch.object(supervisor,'processes',return_value=[]),patch.object(supervisor,'coordinator_locked',return_value=False),\
             patch.object(tail,'fresh_recovery_state',return_value=fresh),\
             patch.object(supervisor,'launch') as launch:
            result=supervisor.check()
        self.assertEqual(result['state'],'review_tail_paused');launch.assert_not_called()
        self.assertEqual(supervisor.action({'status':'checkpoint','pending':2},[],[],False,{},[],100,tail_paused=True)[0],'restart')
        with patch.object(supervisor,'HERE',self.root),patch.object(supervisor,'RUNTIME',self.runtime),patch.object(supervisor,'SUPERVISION',self.root/'health'),\
             patch.object(supervisor,'processes',return_value=[]),patch.object(supervisor,'coordinator_locked',return_value=False),\
             patch.object(tail,'fresh_recovery_state',return_value=fresh|{'open_accessible_new':2}),\
             patch.object(supervisor,'launch',return_value=111) as launch:
            result=supervisor.check()
        self.assertEqual(result['state'],'starting');launch.assert_called_once()

    def test_actual_tail_pool_reaches_eight_under_common_ledger_and_never_admits_ninth(self):
        tail.enter_review_tail(c,8,[])
        release=self.gate();started=[];lock=threading.Lock();peaks=[]
        def run(assigned,*_,**__):
            with lock:started.append(assigned[1]);peaks.append(c.ACTIVE)
            if not release.wait(4):raise AssertionError('Unreleased synthetic job')
        with patch.object(c,'job_lease',side_effect=lambda j:{'writes':{j[1]},'reads':set()}),patch.object(c,'run_job',side_effect=run):
            thread=self.dispatch([(job(str(i)),True) for i in range(12)])
            self.until(lambda:len(started)==8)
            time.sleep(.04);self.assertEqual(len(started),8);self.assertEqual(c.ACTIVE,8)
            self.assertEqual(c.ACTIVE_BY_KIND,{'new':0,'review':8})
            self.assertIsNone(c.try_reserve_slot(job('illegal-new'),8,False,lease={'writes':{'X'},'reads':set()}))
            release.set();self.drained(thread)
        self.assertEqual(len(started),12);self.assertLessEqual(max(peaks),8)

    def test_tail_footprints_block_conflict_and_allow_independent_reviews(self):
        tail.enter_review_tail(c,8,[])
        release=self.gate();owner=threading.Event();independent=threading.Event();blocked=threading.Event()
        def footprint(j):return {'writes':{'T'} if j[1]=='owner' else {j[1]},'reads':{'T'} if j[1]=='blocked' else set()}
        def run(j,*_,**__):
            if j[1]=='owner':owner.set();self.assertTrue(release.wait(4))
            elif j[1]=='blocked':blocked.set()
            else:independent.set()
        with patch.object(c,'job_lease',side_effect=footprint),patch.object(c,'run_job',side_effect=run):
            thread=self.dispatch([(job('owner'),True)])
            self.assertTrue(owner.wait(2))
            other=self.dispatch([(job('blocked'),True),(job('independent'),True)])
            self.assertTrue(independent.wait(2));self.assertFalse(blocked.is_set())
            release.set();self.drained(thread);self.drained(other);self.assertTrue(blocked.is_set())

    def test_lowering_tail_limit_drains_without_cancelling_running_work(self):
        tail.enter_review_tail(c,8,[])
        releases={str(i):self.gate() for i in range(10)};started=[]
        def run(j,*_,**__):
            started.append(j[1]);self.assertTrue(releases[j[1]].wait(4))
        with patch.object(c,'job_lease',side_effect=lambda j:{'writes':{j[1]},'reads':set()}),patch.object(c,'run_job',side_effect=run):
            thread=self.dispatch([(job(str(i)),True) for i in range(10)])
            self.until(lambda:len(started)==8)
            self.plan(7)
            self.assertEqual(c.ACTIVE,8)
            releases['0'].set();self.until(lambda:c.ACTIVE==7)
            time.sleep(.04);self.assertEqual(len(started),8)
            for event in releases.values():event.set()
            self.drained(thread)

    def test_tail_submission_failure_releases_shared_reservations(self):
        tail.enter_review_tail(c,8,[])
        class Reject:
            def __init__(self,**kwargs):pass
            def __enter__(self):return self
            def __exit__(self,*args):return False
            def submit(self,*args,**kwargs):raise RuntimeError('Synthetic submit rejection')
        with patch.object(c,'job_lease',return_value={'writes':{'A'},'reads':set()}),\
             patch.object(c.review_lanes.concurrent.futures,'ThreadPoolExecutor',Reject):
            futures=list(c.scheduled_futures([(job('A'),True)],'NEVER_A_MODEL',{},8))
        self.assertEqual(len(futures),1)
        with self.assertRaisesRegex(RuntimeError,'submit rejection'):futures[0].result()
        self.assertEqual(c.ACTIVE,0);self.assertEqual(c.ACTIVE_LEASES,{})

    def small_database(self,articles,states=()):
        db=sqlite3.connect(self.root/'corpus.sqlite')
        db.execute('CREATE TABLE articles(code_id TEXT,id TEXT,source_sha256 TEXT,number TEXT)')
        db.execute('CREATE TABLE drafts(code_id TEXT,source_id TEXT,source_sha256 TEXT,status TEXT,proposed_xml TEXT)')
        db.executemany('INSERT INTO articles VALUES(?,?,?,?)',[(a['code_id'],a['source_id'],a['source_sha256'],a['number']) for a in articles])
        db.executemany('INSERT INTO drafts VALUES(?,?,?,?,?)',states);db.commit();db.close()

    def test_fresh_queue_recovers_deferred_absent_ids_and_skips_registered_retained_sources(self):
        absent=article('deferred');done=article('done');retained=article('retained');graphic=article('graphic')
        self.small_database([absent,done,retained,graphic],[('SYNTHETIC','done','sha-done','rewrite_draft','<p>Accepted.</p>'),('SYNTHETIC','retained','sha-retained','retained_unchanged',None)])
        batch=self.root/'batches/automatic-temporary';batch.mkdir(parents=True);(batch/'00009.json').write_text('[]')
        evidence=self.runtime/'jobs/temporary-00010';evidence.mkdir(parents=True);(evidence/'answer.json').write_text('NEVER REPLAY ME')
        with patch.object(c,'needs_graphic_source',side_effect=lambda a:a['source_id']=='graphic'):
            jobs,held=tail.fresh_new_jobs(c,{'temporary':[absent,done,retained,graphic]},['temporary'])
        self.assertEqual([(s,i,[a['source_id'] for a in rows]) for s,i,rows in jobs],[('temporary',10,['deferred'])])
        self.assertEqual(held[0]['source_id'],'graphic');self.assertFalse(held[0]['accepted'])
        self.assertEqual((evidence/'answer.json').read_text(),'NEVER REPLAY ME')
        self.assertEqual(tail.identities(jobs),(('SYNTHETIC','deferred','sha-deferred'),))

    def test_fresh_queue_rejects_stale_canonical_or_incomplete_existing_draft(self):
        a=article('A');self.small_database([a],[('SYNTHETIC','A','stale','rewrite_draft','<p>Different.</p>')])
        with self.assertRaisesRegex(ValueError,'reconciliation'):tail.fresh_new_jobs(c,{'temporary':[a]},['temporary'])
        db=sqlite3.connect(self.root/'corpus.sqlite');db.execute('DELETE FROM drafts');db.execute('UPDATE articles SET source_sha256="changed"');db.commit();db.close()
        with self.assertRaisesRegex(ValueError,'Canonical source changed'):tail.fresh_new_jobs(c,{'temporary':[a]},['temporary'])

    def test_unknown_empty_duplicate_or_incomplete_inventory_is_never_treated_as_zero(self):
        for sources,slugs in [(None,['temporary']),({},['temporary']),({'temporary':[]},['temporary']),
                              ({'temporary':[{}]},['temporary']),({'temporary':[article('A'),article('A')]},['temporary']),
                              ({'temporary':[article('A')]},[])]:
            with self.subTest(sources=sources,slugs=slugs),self.assertRaises(ValueError):
                tail.fresh_new_jobs(c,sources,slugs)

    def test_pure_drain_decision_requires_fresh_owners_queues_guards_and_exact_zero_counts(self):
        self.assertFalse(tail.drain_decision({})['may_close_review_admissions'])
        evidence={name:True for name in ['coordinator_identity_verified','fresh_queue_identity_verified',
              'fresh_inventory_verified','active_batch_owners_verified','registration_guards_clear',
              'source_guards_clear','benefit_guards_clear','impact_guards_clear','reference_guards_clear',
              'no_orphan_or_manual_workers']}
        evidence.update(coordinator_pid=3122,pending_new_jobs=0,reserved_or_running_new_jobs=0)
        self.assertTrue(tail.drain_decision(evidence)['may_close_review_admissions'])
        for name,value in [('pending_new_jobs',None),('pending_new_jobs',False),('reserved_or_running_new_jobs',1),
                           ('active_batch_owners_verified',False),('reference_guards_clear',None),
                           ('fresh_queue_identity_verified',False)]:
            with self.subTest(name=name,value=value):
                self.assertFalse(tail.drain_decision(evidence|{name:value})['may_close_review_admissions'])

    def test_supervisor_actually_selects_new_mode_only_with_explicit_plan(self):
        self.plan(7,continuation_mode='recover_new_before_reviews')
        with patch.object(supervisor,'RUNTIME',self.runtime),patch.object(supervisor.subprocess,'Popen',return_value=SimpleNamespace(pid=999)) as launch:
            supervisor.launch(self.root)
        command=launch.call_args.args[0]
        self.assertIn('--recover-new-before-reviews',command);self.assertNotIn('--interleave-review',command)
        self.plan(7)
        with patch.object(supervisor,'RUNTIME',self.runtime),patch.object(supervisor.subprocess,'Popen',return_value=SimpleNamespace(pid=999)) as launch:
            supervisor.launch(self.root)
        self.assertIn('--interleave-review',launch.call_args.args[0]);self.assertNotIn('--recover-new-before-reviews',launch.call_args.args[0])

    def tail_observation_setup(self,count=8):
        self.plan(count,continuation_mode='recover_new_before_reviews')
        c.atomic(self.runtime/'coordinator-run.json',{'pid':55,'capacity':8,'role_limits':{'new':6,'review':count-6},
                 'started_at_unix':10,'continuation_mode':'recover_new_before_reviews'})
        c.atomic(self.runtime/'continuation-phase.json',{'coordinator_pid':55,'phase':'review_tail',
                 'open_accessible_new_sources':0,'shared_ledger_drained':True,
                 'complete_inventory':{'complete':True},'manual_reservations_verified_empty':True})
        return [{'pid':100+i,'ppid':55,'kind':'review','execution':{'verified':True,'model':'gpt-6-astra',
                 'reasoning_effort':'medium','session_id':'distinct-synthetic-session-'+str(i)}} for i in range(count)]

    def test_tail_observation_accepts_authorized_reviews_and_requires_all_native_distinct_sessions(self):
        workers=self.tail_observation_setup(8)
        result=observation.observe(self.runtime,[{'pid':55}],workers,100)
        self.assertTrue(result['configuration_matches_authorized_roles'])
        self.assertTrue(result['review_tail_distinct_native_sessions_verified'])
        self.assertFalse(result['simultaneous_six_new_plus_two_review_verified'])
        self.assertEqual(json.loads((self.runtime/'review-tail-execution.json').read_text())['verified_review_workers'],8)
        workers[1]['execution']['session_id']=workers[0]['execution']['session_id']
        self.assertFalse(observation.observe(self.runtime,[{'pid':55}],workers,100)['review_tail_distinct_native_sessions_verified'])
        workers=self.tail_observation_setup(8);workers[1]['execution']['session_id']=''
        self.assertFalse(observation.observe(self.runtime,[{'pid':55}],workers,100)['review_tail_distinct_native_sessions_verified'])
        workers=self.tail_observation_setup(8);workers.append({'pid':999,'ppid':55,'kind':'review','execution':{'verified':False}})
        self.assertFalse(observation.observe(self.runtime,[{'pid':55}],workers,100)['review_tail_distinct_native_sessions_verified'])

    def test_tail_configuration_alone_or_one_missing_response_never_proves_eight_sessions(self):
        workers=self.tail_observation_setup(8)
        configured=observation.observe(self.runtime,[{'pid':55}],[],100)
        self.assertTrue(configured['configuration_matches_authorized_roles'])
        self.assertFalse(configured['review_tail_distinct_native_sessions_verified'])
        self.assertFalse((self.runtime/'review-tail-execution.json').exists())
        document=json.loads((self.runtime/'worker-limit.json').read_text())
        c.atomic(self.runtime/'worker-limit.json',document|{'review_tail_limit':0})
        self.assertFalse(observation.observe(self.runtime,[{'pid':55}],[],100)['review_tail_distinct_native_sessions_verified'])
        self.assertFalse((self.runtime/'review-tail-execution.json').exists())
        c.atomic(self.runtime/'worker-limit.json',document)
        workers[0]['execution']['verified']=False
        self.assertFalse(observation.observe(self.runtime,[{'pid':55}],workers,100)['review_tail_distinct_native_sessions_verified'])
        workers=self.tail_observation_setup(7)
        measured=observation.observe(self.runtime,[{'pid':55}],workers,100)
        self.assertEqual(measured['effective_review_tail_limits']['workers'],7)
        self.assertTrue(measured['review_tail_distinct_native_sessions_verified'])

    def driver_fixture(self):
        self.plan(8,continuation_mode='recover_new_before_reviews')
        args=SimpleNamespace(workers=8,slugs='temporary',export_every=0,publish_at_end=False,deploy_on_export=False)
        manifest=self.root/'review-manifest.json'
        manifest.write_text(json.dumps({'prior_articles':[],'completed_second_pass':0}))
        state={'drafted_articles':0,'retained_unchanged':0,'prior_drafts_reviewed':0}
        source={'temporary':[article('A')]}
        return args,manifest,state,source

    def test_driver_recovers_current_new_then_captures_fresh_reviews_then_runs_reference_convergence(self):
        args,manifest,state,sources=self.driver_fixture();events=[]
        review=article('R',previous_draft={'proposed_sha256':'fresh-body','batch_row_sha256':'fresh-whole-row'})
        def scheduled(items,*_):
            items=list(items);events.append(('review' if items[0][1] else 'new',items[0][0][2][0]))
            future=concurrent.futures.Future();future.set_result(None);yield future
        with patch.object(c,'SLUGS',['temporary']),patch.object(c,'load_sources',return_value=sources),\
             patch.object(c,'progress',return_value=state),patch.object(c,'scheduled_futures',side_effect=scheduled),\
             patch.object(tail,'fresh_new_jobs',side_effect=[([('temporary',1,[article('A')])],[]),([],[]),([],[])]),\
             patch.object(review_prior,'build_jobs',side_effect=[[('temporary',1,[review])],[]]),\
             patch.object(review_prior,'revisions_manifest',return_value=manifest),\
             patch.object(c,'run_reference_review_phase',side_effect=lambda *_:events.append(('references',None))):
            tail.run(c,'NEVER_A_MODEL',args)
        self.assertEqual([x[0] for x in events],['new','review','references'])
        self.assertEqual(events[1][1]['previous_draft']['batch_row_sha256'],'fresh-whole-row')
        self.assertFalse(c.REVIEW_TAIL)

    def test_driver_repeated_unresolved_new_fingerprint_blocks_instead_of_blind_replay(self):
        args,manifest,state,sources=self.driver_fixture()
        future=concurrent.futures.Future();future.set_result(None)
        with patch.object(c,'SLUGS',['temporary']),patch.object(c,'load_sources',return_value=sources),\
             patch.object(c,'progress',return_value=state) as progress,\
             patch.object(c,'scheduled_futures',return_value=iter([future])) as schedule,\
             patch.object(tail,'fresh_new_jobs',return_value=([('temporary',1,[article('A')])],[])),\
             patch.object(review_prior,'build_jobs') as reviews:
            with self.assertRaisesRegex(ValueError,'no progress'):tail.run(c,'NEVER_A_MODEL',args)
        self.assertEqual(schedule.call_count,1);reviews.assert_not_called()
        self.assertTrue(c.STOP.is_set());self.assertFalse(c.REVIEW_TAIL)
        self.assertEqual(progress.call_args.args[1],'blocked')

    def test_driver_pending_reviews_with_unknown_or_changed_beforeimages_block_before_reference_phase(self):
        args,manifest,state,sources=self.driver_fixture()
        manifest.write_text(json.dumps({'prior_articles':[{'review_status':'pending'}]}))
        with patch.object(c,'SLUGS',['temporary']),patch.object(c,'load_sources',return_value=sources),\
             patch.object(c,'progress',return_value=state),patch.object(tail,'fresh_new_jobs',return_value=([],[])),\
             patch.object(review_prior,'build_jobs',return_value=[]),patch.object(review_prior,'revisions_manifest',return_value=manifest),\
             patch.object(c,'run_reference_review_phase') as references:
            with self.assertRaisesRegex(ValueError,'before-images'):tail.run(c,'NEVER_A_MODEL',args)
        references.assert_not_called();self.assertTrue(c.STOP.is_set())

    def test_driver_repeated_review_beforeimage_blocks_after_one_unsuccessful_wave(self):
        args,manifest,state,sources=self.driver_fixture()
        review=article('R',previous_draft={'proposed_sha256':'unchanged-body','batch_row_sha256':'unchanged-whole-row'})
        manifest.write_text(json.dumps({'prior_articles':[{'review_status':'pending'}]}))
        future=concurrent.futures.Future();future.set_result(None)
        with patch.object(c,'SLUGS',['temporary']),patch.object(c,'load_sources',return_value=sources),\
             patch.object(c,'progress',return_value=state),patch.object(tail,'fresh_new_jobs',return_value=([],[])),\
             patch.object(c,'scheduled_futures',return_value=iter([future])) as schedule,\
             patch.object(review_prior,'build_jobs',return_value=[('temporary',1,[review])]),\
             patch.object(review_prior,'revisions_manifest',return_value=manifest),\
             patch.object(c,'run_reference_review_phase') as references:
            with self.assertRaisesRegex(ValueError,'no progress'):tail.run(c,'NEVER_A_MODEL',args)
        self.assertEqual(schedule.call_count,1);references.assert_not_called();self.assertTrue(c.STOP.is_set())

    def test_full_inventory_matches_config_coverage_pinned_counts_and_official_ids(self):
        a,b=article('A'),article('B');self.small_database([a,b])
        db=sqlite3.connect(self.root/'corpus.sqlite')
        db.execute('CREATE TABLE documents(code_id TEXT,id TEXT,kind TEXT,xml TEXT)')
        db.execute('INSERT INTO documents VALUES(?,?,?,?)',('SYNTHETIC','SYNTHETIC','TEXTELR','<TEXTELR><STRUCT><LIEN_ART id="A"/><LIEN_ART id="B"/></STRUCT></TEXTELR>'))
        db.commit();db.close()
        (self.root/'corpus.json').write_text(json.dumps({'codes':[{'id':'SYNTHETIC','slug':'temporary'}],'annexes':[]}))
        coverage={'sources_complete':True,'missing_archives':[],'as_of':'2026-10-18','codes':[{'slug':'temporary','expected_articles':2,'imported_versions':2,'inventory_reconciled':True}]}
        (self.root/'coverage.json').write_text(json.dumps(coverage))
        plan=json.loads((self.runtime/'parallelism-plan.json').read_text())
        plan['current_stage_initial_status']={'source_records':2,'codes':[{'slug':'temporary','source_records':2}]}
        c.atomic(self.runtime/'parallelism-plan.json',plan)
        with patch.object(c,'SLUGS',['temporary']),patch.object(c,'CORPUS',self.root):
            self.assertEqual(REAL_VERIFY_COMPLETE(c,{'temporary':[a,b]})['source_records'],2)
            with self.assertRaisesRegex(ValueError,'truncated'):REAL_VERIFY_COMPLETE(c,{'temporary':[a]})
            with self.assertRaisesRegex(ValueError,'identities differ'):REAL_VERIFY_COMPLETE(c,{'temporary':[a,article('C')]})
            plan['current_stage_initial_status']['source_records']=3
            c.atomic(self.runtime/'parallelism-plan.json',plan)
            with self.assertRaisesRegex(ValueError,'full canonical inventory'):REAL_VERIFY_COMPLETE(c,{'temporary':[a,b]})

    def test_tail_queue_rejects_drafting_job_before_any_executor(self):
        with patch.object(review_lanes.concurrent.futures,'ThreadPoolExecutor') as pool:
            with self.assertRaisesRegex(ValueError,'cannot contain'):
                list(review_lanes.completed_futures([(job('N'),False)],limits=lambda:{},submit=None,
                     stopped=lambda:False,wait_for_change=None,describe=None,state_changed=None,deferred_changed=None,review_tail=True))
            pool.assert_not_called()

    def test_validation_execution_reference_and_commit_functions_are_unchanged(self):
        functions=lambda p:{x.name:ast.dump(x,include_attributes=False) for x in ast.parse(p.read_text()).body if isinstance(x,ast.FunctionDef)}
        before=functions(STAGE/'baseline/run_exhaustive.py');after=functions(STAGE/'candidate/run_exhaustive.py')
        for name in ['validate_answer','policy_is_current','invoke_agent','_run_job','run_job','job_directory','job_lease','leases_conflict','capture_for_attempt','run_in_slot','release_slot']:
            with self.subTest(name=name):self.assertEqual(before[name],after[name])
        self.assertEqual((STAGE/'baseline/review_prior.py').read_bytes(),(PROJECT/'review_prior.py').read_bytes())


if __name__=='__main__':unittest.main(verbosity=2)
