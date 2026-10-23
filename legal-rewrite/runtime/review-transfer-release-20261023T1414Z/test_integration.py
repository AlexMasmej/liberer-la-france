"""Actual tiny SQLite/owner fixtures and interrupted orchestration, offline only."""
from pathlib import Path
import copy,hashlib,json,os,shutil,sqlite3,sys,tempfile,time,unittest
from unittest.mock import patch
import registration_reconciliation as rr
import transfer_controller as t

STAGE=Path(__file__).parent.resolve();PROJECT=STAGE.parents[1]
REBASE=PROJECT/'runtime'/t.REBASE
MODULES=['ingest','source_assets','substantive_impact','register_batches','reference_coherence']

def put(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_bytes(value if isinstance(value,bytes) else (json.dumps(value,ensure_ascii=False)+'\n').encode())

def h(value):return rr.digest(value)

def guards(row):
    return dict(source_sha256=row['source_sha256'],status=row['status'],proposal_sha256=h(row['proposed_xml']),reason_sha256=h(row['reason']),notes_sha256=h(row['review_notes']))

class OfflineBackend(t.NativeBackend):
    def __init__(self,case):
        super().__init__(case.root);self.case=case;self.clock=2000.;self.old=True;self.new=None
        self.launches=0;self.collects=0;self.waits=0;self.forever=False;self.on_wait=None
        self.after_launch=None;self.unattested=False
    def reconciliation_precondition(self):
        if not self.root.is_relative_to(Path(self.case.temp.name).resolve()):raise AssertionError('Test backend escaped its fixture')
    def baseline_pins(self,manifest):return self.case.pins()
    def now(self):return self.clock
    def processes(self):
        if self.new:
            return [dict(pid=self.new,ppid=1,pgid=self.new,started='new fixture',os_started_at_unix=2000,
                args=['python3',str(self.root/'run_exhaustive.py'),'--recover-new-before-reviews']),
                dict(pid=4500,ppid=self.new,pgid=4500,started='worker fixture',os_started_at_unix=2001,
                args=['codex','exec','--output-last-message',str(self.root/'runtime/exhaustive/jobs/review-fixture/result.json')])]
        if self.old:return [dict(pid=3122,ppid=1,pgid=3122,started='old fixture',os_started_at_unix=994,args=['python3',str(self.root/'run_exhaustive.py')])]
        return [dict(pid=999,ppid=1,pgid=999,started='other',os_started_at_unix=990,args=['other'])]
    def wait(self,seconds):
        self.waits+=1;self.clock+=1
        for name in ['draft-writer.lock','runtime/exhaustive/coordinator.lock','runtime/exhaustive/manual-agent-slots.lock']:
            with t.locked(self.root/name):pass
        if self.on_wait:self.on_wait()
        if not self.forever:
            self.old=False
            put(self.root/'runtime/exhaustive/coordinator-exit.json',dict(pid=3122,ended_at_unix=2001,exit_code=0,exit_type=None,stop_requested=False))
            os.utime(self.root/'runtime/exhaustive/coordinator-exit.json',(2001,2001))
    def reconcile(self,pins):
        self.collects+=1
        return super().reconcile(pins)
    def launch(self,folder):
        self.launches+=1;self.new=9123;self.clock=2002
        command=['python3',str(self.root/'run_exhaustive.py'),'--recover-new-before-reviews']
        put(folder/'launch.json',dict(pid=9123,command=command,launched_at_unix=2000))
        put(self.root/'runtime/exhaustive/coordinator-run.json',dict(pid=9123,started_at_unix=2001,requested_execution=dict(model='gpt-6-astra',reasoning_effort='medium')))
        job=self.root/'runtime/exhaustive/jobs/review-fixture';log=job/'errors-1.log'
        text='OpenAI Codex v0.160.1\n--------\nworkdir: '+str(job)+'\nmodel: gpt-6-astra\nprovider: openai\nreasoning effort: medium\nsession id: 01234567-0123-0123-0123-000000000001\n--------\n'
        if not self.unattested:text+='codex\nFixture response.\n'
        put(log,text.encode());put(job/'process-4500.json',dict(pid=4500,started_at_unix=2001,stderr_log=str(log)))
        # Fresh accepted review is independent from the still-live worker.
        rows=json.loads((self.root/'batches/fixture/001.json').read_text());old=copy.deepcopy(rows[1])
        rows[1]['prior_proposal_sha256']=h(old['proposed_xml']);put(self.root/'batches/fixture/001.json',rows)
        archive=[old|dict(replacement=rows[1])]
        put(self.root/'revisions/radical-review'/(h(json.dumps(archive,ensure_ascii=False,sort_keys=True))+'.json'),archive)
        source=json.loads((self.root.parent/'sites/liberer-la-retraite/dist/corpus/s1.json').read_text())[0]
        source['previous_draft']=old|dict(proposed_sha256=h(old['proposed_xml']))
        accepted=self.root/'runtime/exhaustive/jobs/review-accepted';accepted_log=accepted/'errors-1.log'
        accepted_text=text.replace(str(job),str(accepted)).replace('000000000001','000000000002')
        if 'codex\nFixture response.' not in accepted_text:accepted_text+='codex\nFixture response.\n'
        put(accepted_log,accepted_text.encode());put(accepted/'source.json',[source]);put(accepted/'answer.json',[rows[1]])
        put(accepted/'execution-observed-1.json',dict(source_log=str(accepted_log)))
        metric=dict(coordinator_pid=9123,kind='review',outcome='reviewed',job='review-accepted',articles=1,attempts=1,execution_session_id='01234567-0123-0123-0123-000000000002',started_at_unix=2001,finished_at_unix=2002)
        metrics=self.root/'runtime/exhaustive/job-metrics.jsonl'
        metrics.write_bytes(metrics.read_bytes()+(json.dumps(metric)+'\n').encode())
        if self.after_launch:self.after_launch()
        return 9123

class Integration(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='transfer-integration-offline-');self.addCleanup(self.temp.cleanup)
        self.root=(Path(self.temp.name)/'legal-rewrite').resolve();self.root.mkdir()
        self.addCleanup(self.unload)
        for name in t.GATE_CODE:
            shutil.copyfile(PROJECT/name,self.root/name)
        self.unload()
        for f in ['draft-writer.lock','runtime/exhaustive/coordinator.lock','runtime/exhaustive/manual-agent-slots.lock','runtime/supervision/supervisor.lock']:
            put(self.root/f,b'')
        (self.root/'attachments/records').mkdir(parents=True)
        (self.root/'revisions/radical-review').mkdir(parents=True)
        self.sealed=self.root/'runtime'/t.REBASE;shutil.copytree(REBASE,self.sealed,ignore=shutil.ignore_patterns('__pycache__'))
        for name in t.sealed_package(self.sealed)['baseline']:
            shutil.copyfile(self.sealed/'baseline'/name,self.root/name)
        specs=[dict(id='CODE'+str(i),slug='s'+str(i),title='Fixture'+str(i)) for i in range(9)]
        put(self.root/'corpus.json',dict(codes=specs[:5],annexes=specs[5:]))
        for f in ['policy-coordinations.json','site-summaries.json','reference-focus-extra.json']:put(self.root/f,[])
        focus=self.root/'runtime/contrat-unique-20261019/priority'
        put(focus/'excluded-packs.json',[]);put(focus/'priority-targets.proposed.json',dict(schema_version=1,targets=[]))
        base=self.root/'runtime/exhaustive'
        put(base/'manual-agent-slots.json',[]);put(base/'worker-limit.json',dict(workers=7,role_limits=dict(new=6,review=0)))
        put(base/'parallelism-plan.json',dict(capacity=8,current_workers=8,role_limits=dict(new=6,review=2),preserve='fixture'))
        put(base/'model-policy.json',dict(model='gpt-6-astra',reasoning_effort='medium'))
        put(base/'coordinator.pid',b'3122');put(base/'coordinator-run.json',dict(pid=3122,started_at_unix=1000))
        put(base/'admission-status.json',dict(coordinator_pid=3122,updated_at_unix=1100,pending_by_kind=dict(new=0,review=100),reserved_or_running_by_kind=dict(new=0,review=0),admitted_by_kind=dict(new=1,review=0)))
        put(base/'queue-admission-plan.json',dict(coordinator_pid=3122,queue_file='mixed-queue.json',scheduled_by_kind=dict(new=1,review=1)))
        put(base/'mixed-queue.json',[dict(slug='s0',index=1,review=False,source_ids=['A0']),dict(slug='s0',index=1,review=True,source_ids=['A0'])])
        put(base/'job-metrics.jsonl',(json.dumps(dict(coordinator_pid=3122,slug='s0',index=1,kind='new',job='s0-00001',outcome='accepted',articles=1,started_at_unix=1100,finished_at_unix=1200))+'\n').encode())
        db=sqlite3.connect(self.root/'corpus.sqlite')
        db.executescript('CREATE TABLE articles(code_id,id,number,valid_from,valid_until,content_xml,source_sha256);CREATE TABLE documents(code_id,id,kind,xml,sha256);CREATE TABLE drafts(code_id,source_id,source_sha256,status,proposed_xml,reason,review_notes);CREATE TABLE draft_sources(code_id,source_id,source_xml,valid_from,valid_until);')
        rows=[];sources=[];ledger=[];coverage=[]
        for i,spec in enumerate(specs):
            sid='A'+str(i);body='<p>Réservé.</p>';xml=('<ARTICLE><META><META_SPEC><META_ARTICLE><NUM>'+str(i)+'</NUM><DATE_DEBUT>2000-01-01</DATE_DEBUT><DATE_FIN>2999-01-01</DATE_FIN></META_ARTICLE></META_SPEC></META><BLOC_TEXTUEL><CONTENU>'+body+'</CONTENU></BLOC_TEXTUEL></ARTICLE>').encode();sha=h(xml)
            source=dict(code_id=spec['id'],source_id=sid,number=str(i),source_sha256=sha,source_xml=body,source_notes_xml='',valid_from='2000-01-01',valid_until='2999-01-01')
            row=dict(code_id=spec['id'],source_id=sid,number=str(i),source_sha256=sha,status='retained_unchanged',proposed_xml=None,reason='Fixture reason.',review_notes='Fixture notes.')
            rows.append(row);sources.append(source);ledger.append(dict(code_id=spec['id'],source_id=sid,source_sha256=sha,number=str(i),slug=spec['slug'],draft_guards=guards(row)))
            db.execute('INSERT INTO articles VALUES(?,?,?,?,?,?,?)',(spec['id'],sid,str(i),'2000-01-01','2999-01-01',body,sha))
            db.execute('INSERT INTO documents VALUES(?,?,?,?,?)',(spec['id'],sid,'ARTICLE',xml,sha))
            struct=('<TEXTELR><STRUCT><LIEN_ART id="'+sid+'" debut="2000-01-01" fin="2999-01-01"/></STRUCT></TEXTELR>').encode()
            db.execute('INSERT INTO documents VALUES(?,?,?,?,?)',(spec['id'],spec['id'],'TEXTELR',struct,h(struct)))
            db.execute('INSERT INTO drafts VALUES(?,?,?,?,?,?,?)',(spec['id'],sid,sha,row['status'],None,row['reason'],row['review_notes']))
            db.execute('INSERT INTO draft_sources VALUES(?,?,?,?,?)',(spec['id'],sid,body,'2000-01-01','2999-01-01'))
            corpus=self.root.parent/'sites/liberer-la-retraite/dist/corpus';put(corpus/(spec['slug']+'.json'),[source]);coverage.append(dict(slug=spec['slug'],expected_articles=1,imported_versions=1,inventory_reconciled=True))
        outside=[]
        for i in range(4):
            row=dict(code_id='OLD',source_id='O'+str(i),source_sha256='oldhash'+str(i),status='rewrite_draft',proposed_xml='<p>Historical fixture.</p>',reason='Old reason',review_notes='Old notes')
            outside.append(dict(code_id=row['code_id'],source_id=row['source_id'],draft_guards=guards(row)))
            db.execute('INSERT INTO drafts VALUES(?,?,?,?,?,?,?)',(row['code_id'],row['source_id'],*rr.values(row)))
        db.commit();db.close()
        put(corpus/'coverage.json',dict(as_of='2026-10-18',sources_complete=True,missing_archives=[],codes=coverage))
        folder=self.root/'runtime/completion-coverage-inventory-20261023T0254Z'
        put(folder/'current-article-ledger.jsonl',b''.join((json.dumps(x)+'\n').encode() for x in ledger))
        put(folder/'outside-current-inventory.json',outside)
        patcher=patch.multiple(rr,LEDGER_SHA=h((folder/'current-article-ledger.jsonl').read_bytes()),CANONICAL_COUNT=9);patcher.start();self.addCleanup(patcher.stop)
        put(self.root/'batches/fixture/001.json',rows)
        put(self.root/'registered-batches.json',{'|'.join((x['code_id'],x['source_id'])):dict(source_sha256=x['source_sha256'],proposed_sha256=h(x['proposed_xml'])) for x in rows})
        put(base/'jobs/s0-00001/source.json',[sources[0]])
        put(base/'jobs/intent/source.json',sources);put(base/'jobs/intent/reference-targets.json',{})
        put(base/'jobs/intent/registration-intent.json',dict(rows=rows,batch_path=str(self.root/'batches/fixture/001.json'),source_sha256=h((base/'jobs/intent/source.json').read_bytes()),reference_sha256=h((base/'jobs/intent/reference-targets.json').read_bytes())))
        put(base/'jobs/intent/registration-complete.json',dict(batch_path=str(self.root/'batches/fixture/001.json'),accepted_articles=9))
        put(self.root/'runtime/radical-review-20261019.json',dict(prior_articles=[dict(code_id=x['code_id'],source_id=x['source_id'],source_sha256=x['source_sha256'],proposed_sha256=h(x['proposed_xml']),review_status='pending') for x in rows]))
        recapture={}
        for field in ['source','answer','snapshot','proof','receipt','capture','capture_approval','helper']:
            f=self.root/('runtime/legacy/'+field+'.json')
            value=dict(metadata_only=True,sqlite_changed=False,registry_changed=False,normative_bodies_changed=0,impacts_changed=0,workflow_fields_changed=0,owning_files=[],checks=[]) if field=='receipt' else {}
            put(f,value);recapture[field+'_path']=str(f.relative_to(self.root));recapture[field+'_sha256']=h(f.read_bytes())
        put(self.root/'runtime/poursuite-20261020-e/root-adoption-approval.json',dict(approved=True,scope='E52-and-C141-bounded-context',recapture=recapture,approved_refreshed_identifiers=[]))
        for f in ['runtime/sru-integral/registration-003','runtime/sru-urbanisme-fiscalite']:
            put(self.root/f/'sources.json',[]);put(self.root/f/'candidates.json',[])
        self.backend=OfflineBackend(self);self.run_dir=self.root/'runtime'/t.PACKAGE/'runs/case'
        self.real_connect=sqlite3.connect
        def confined(path,*args,**options):
            from urllib.parse import urlsplit,unquote
            target=Path(unquote(urlsplit(str(path)).path)).resolve()
            if not target.is_relative_to(self.root) or not str(path).endswith('?mode=ro') or not options.get('uri'):raise AssertionError('Collection attempted writable or non-fixture DB: '+str(path))
            return self.real_connect(path,*args,**options)
        dbpatch=patch.object(sqlite3,'connect',side_effect=confined);dbpatch.start();self.addCleanup(dbpatch.stop)
    def unload(self):
        for name in MODULES:sys.modules.pop(name,None)
    def pins(self):
        names={p.name for p in self.root.glob('*.py')}|set(t.POLICIES)
        return {n:h((self.root/n).read_bytes()) for n in names}
    def collect(self):return rr.collect(self.root,self.pins())
    def controller(self,kind=t.Transfer):return kind(self.root,self.sealed,self.run_dir,self.backend,timeout=2)
    def alter_db(self,sql,args=()):
        db=self.real_connect(self.root/'corpus.sqlite');db.execute(sql,args);db.commit();db.close()
    def test_full_current_collector_is_read_only_and_keeps_legacy_flag_open(self):
        before={p:p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        report=self.collect();self.assertEqual(report['canonical_identities'],9);self.assertEqual(report['validated_batch_records'],9)
        self.assertEqual(report['required_second_pass_states'],dict(independent_second_pass_required=9))
        self.assertEqual(before,{p:p.read_bytes() for p in self.root.rglob('*') if p.is_file()})
    def test_current_db_or_registry_owner_mismatch_fails(self):
        self.alter_db('UPDATE drafts SET reason=? WHERE source_id=?',('Intervening reason','A0'))
        with self.assertRaises(AssertionError):self.collect()
    def test_source_xml_body_notes_or_version_mismatch_fails(self):
        self.alter_db('UPDATE articles SET valid_from=? WHERE id=?',('2001-01-01','A0'))
        with self.assertRaises(AssertionError):self.collect()
    def test_whole_normative_document_is_rehashed(self):
        self.alter_db('UPDATE documents SET xml=? WHERE id=?',(b'<ARTICLE>Changed</ARTICLE>','A0'))
        with self.assertRaises(AssertionError):self.collect()
    def test_truncated_canonical_inventory_fails(self):
        put(self.root.parent/'sites/liberer-la-retraite/dist/corpus/s0.json',[])
        with self.assertRaises(AssertionError):self.collect()
    def test_forged_completed_intention_or_source_hash_fails(self):
        f=self.root/'runtime/exhaustive/jobs/intent/source.json';put(f,[])
        with self.assertRaises(AssertionError):self.collect()
    def test_unknown_null_prior_marker_does_not_count_as_review(self):
        f=self.root/'batches/fixture/001.json';rows=json.loads(f.read_text());rows[0]['prior_proposal_sha256']=None;put(f,rows)
        with self.assertRaises(AssertionError):self.collect()
    def test_production_backend_refuses_before_os_collection_or_mutation(self):
        backend=t.NativeBackend(self.root)
        with patch.object(backend,'processes',side_effect=AssertionError('No production collector')):
            with self.assertRaisesRegex(t.Blocked,'NOT READY'):t.Transfer(self.root,self.sealed,self.run_dir,backend).run(3122)
        self.assertFalse(self.run_dir.exists())
    def test_complete_transfer_integrates_real_reconciliation_and_native_response(self):
        result=self.controller().run(3122)
        self.assertEqual(result['phase'],'COMPLETE');self.assertEqual(self.backend.launches,1);self.assertGreaterEqual(self.backend.collects,2)
        self.assertFalse((self.root/t.DISABLED).exists());self.assertGreater(self.backend.waits,0)
        self.assertEqual(t.required_json(self.root/t.HOT)['review_tail_limit'],8)
    def test_os_birth_is_explicitly_distinct_from_run_creation(self):
        entry=self.backend.entry(3122);self.assertEqual(entry['identity']['run_start_delay_seconds'],6)
        self.assertEqual(t.utc_birth('Thu Oct 22 20:54:15 2026'),1792702455)
    def test_unfinished_new_queue_never_mutates_controls(self):
        ad=self.root/'runtime/exhaustive/admission-status.json';data=json.loads(ad.read_text());data['reserved_or_running_by_kind']['new']=1;put(ad,data)
        with self.assertRaises(Exception):self.controller().run(3122)
        self.assertFalse(self.run_dir.exists())
    def test_interruption_after_reconciled_recollects_current_database(self):
        class Interrupt(t.Transfer):
            def phase(self,name,**kw):
                super().phase(name,**kw)
                if name=='RECONCILED':raise KeyboardInterrupt()
        with self.assertRaises(KeyboardInterrupt):self.controller(Interrupt).run(3122)
        count=self.backend.collects
        self.alter_db('UPDATE drafts SET review_notes=? WHERE source_id=?',('Changed notes','A0'))
        with self.assertRaises(AssertionError):self.controller().run(3122)
        self.assertGreater(self.backend.collects,count);self.assertEqual(self.backend.launches,0)
    def test_interruption_after_install_or_configuration_recollects(self):
        class Interrupt(t.Transfer):
            def phase(self,name,**kw):
                super().phase(name,**kw)
                if name=='SIX_MODULES_INSTALLED':raise KeyboardInterrupt()
        with self.assertRaises(KeyboardInterrupt):self.controller(Interrupt).run(3122)
        count=self.backend.collects
        result=self.controller().run(3122)
        self.assertEqual(result['phase'],'COMPLETE');self.assertGreater(self.backend.collects,count);self.assertEqual(self.backend.launches,1)
    def test_launch_receipt_after_interruption_adopts_without_second_launch(self):
        self.backend.after_launch=lambda:(_ for _ in ()).throw(KeyboardInterrupt())
        with self.assertRaises(KeyboardInterrupt):self.controller().run(3122)
        self.assertEqual(self.controller().run(3122)['phase'],'COMPLETE');self.assertEqual(self.backend.launches,1)
    def test_late_adoption_rechecks_pins_and_requires_response(self):
        self.backend.unattested=True
        with self.assertRaises(Exception):self.controller().run(3122)
        self.assertEqual(self.backend.launches,1);self.assertTrue((self.root/t.DISABLED).exists())
        with self.assertRaises(Exception):self.controller().run(3122)
        self.assertEqual(self.backend.launches,1)
    def test_preexisting_pause_is_preserved(self):
        put(self.root/t.DISABLED,b'owned by operator')
        with self.assertRaises(t.Blocked):self.controller().run(3122)
        self.assertEqual((self.root/t.DISABLED).read_bytes(),b'owned by operator');self.assertEqual(self.backend.launches,0)

    def test_mid_group_interruption_recollects_and_resumes_only_journalled_files(self):
        class Interrupt(t.Transfer):
            def change(self,name,after):
                super().change(name,after)
                if name=='review_lanes.py':raise KeyboardInterrupt()
        with self.assertRaises(KeyboardInterrupt):self.controller(Interrupt).run(3122)
        count=self.backend.collects
        self.assertEqual(self.controller().run(3122)['phase'],'COMPLETE')
        self.assertGreater(self.backend.collects,count);self.assertEqual(self.backend.launches,1)
    def test_configured_resume_rejects_intervening_database_or_manual_reservation(self):
        class Interrupt(t.Transfer):
            def phase(self,name,**kw):
                super().phase(name,**kw)
                if name=='CONFIGURED':raise KeyboardInterrupt()
        with self.assertRaises(KeyboardInterrupt):self.controller(Interrupt).run(3122)
        put(self.root/'runtime/exhaustive/manual-agent-slots.json',[dict(owner='intervening',kind='review')])
        with self.assertRaisesRegex(t.Blocked,'Manual'):self.controller().run(3122)
        self.assertEqual(self.backend.launches,0);self.assertTrue((self.root/t.DISABLED).exists())
    def test_configured_resume_rechecks_sources(self):
        class Interrupt(t.Transfer):
            def phase(self,name,**kw):
                super().phase(name,**kw)
                if name=='CONFIGURED':raise KeyboardInterrupt()
        with self.assertRaises(KeyboardInterrupt):self.controller(Interrupt).run(3122)
        self.alter_db('UPDATE articles SET valid_until=? WHERE id=?',('2020-01-01','A1'))
        with self.assertRaises(AssertionError):self.controller().run(3122)
        self.assertEqual(self.backend.launches,0)
    def test_unknown_launch_without_receipt_never_launches_again(self):
        def lose_receipt():
            (self.run_dir/'launch/launch.json').unlink();raise KeyboardInterrupt()
        self.backend.after_launch=lose_receipt
        with self.assertRaises(KeyboardInterrupt):self.controller().run(3122)
        with self.assertRaisesRegex(t.Blocked,'ambiguous'):self.controller().run(3122)
        self.assertEqual(self.backend.launches,1)
    def test_late_launch_intervening_policy_is_preserved_and_blocks_adoption(self):
        def change_policy():
            put(self.root/'policy-coordinations.json',b'operator changed policy');raise KeyboardInterrupt()
        self.backend.after_launch=change_policy
        with self.assertRaises(KeyboardInterrupt):self.controller().run(3122)
        with self.assertRaises(t.Conflict):self.controller().run(3122)
        self.assertEqual(self.backend.launches,1);self.assertEqual((self.root/'policy-coordinations.json').read_bytes(),b'operator changed policy')
    def test_timeout_leaves_all_active_jobs_unsignalled_and_restores_owned_controls(self):
        self.backend.forever=True
        with self.assertRaises(TimeoutError):self.controller().run(3122)
        self.assertEqual(self.backend.launches,0);self.assertTrue(self.backend.old)
        self.assertFalse((self.root/t.DISABLED).exists());self.assertEqual(t.required_json(self.root/t.HOT)['workers'],7)
    def test_timeout_preserves_intervening_pause(self):
        self.backend.forever=True
        self.backend.on_wait=lambda:put(self.root/t.DISABLED,b'new operator pause')
        with self.assertRaises(t.Conflict):self.controller().run(3122)
        self.assertEqual((self.root/t.DISABLED).read_bytes(),b'new operator pause');self.assertEqual(self.backend.launches,0)
    def test_actual_os_pid_reuse_or_descendant_survival_blocks_exit(self):
        identity=self.backend.entry(3122)['identity'];self.backend.old=False
        saved=self.backend.processes
        self.backend.processes=lambda:[dict(pid=3122,ppid=1,pgid=3122,args=['different'],started='replacement',os_started_at_unix=1999)]
        with self.assertRaisesRegex(t.Blocked,'PID reuse'):self.backend.idle(identity,set())
        self.backend.processes=lambda:[dict(pid=4501,ppid=1,pgid=3122,args=['export'],started='descendant',os_started_at_unix=1500)]
        with self.assertRaisesRegex(t.Blocked,'descendant'):self.backend.idle(identity,set())
    def test_declared_false_legal_access_failure_is_not_a_natural_exit(self):
        identity=self.backend.entry(3122)['identity'];self.backend.old=False;self.backend.clock=2002
        put(self.root/'runtime/exhaustive/coordinator-exit.json',dict(pid=3122,ended_at_unix=2001,exit_code=0,exit_type=None,stop_requested=True))
        with self.assertRaises(Exception):self.backend.idle(identity,set())
    def test_whole_review_archive_and_historical_intention_are_reconciled(self):
        f=self.root/'batches/fixture/001.json';rows=json.loads(f.read_text());old=copy.deepcopy(rows[0])
        rows[0].update(prior_proposal_sha256=h(None),reason='Reviewed fixture reason')
        put(f,rows);self.alter_db('UPDATE drafts SET reason=? WHERE source_id=?',(rows[0]['reason'],'A0'))
        archive=[old|dict(replacement=rows[0])]
        path=self.root/'revisions/radical-review'/(h(json.dumps(archive,ensure_ascii=False,sort_keys=True))+'.json');put(path,archive)
        report=self.collect()
        self.assertEqual(report['current_review_rows_with_beforeimages'],1)
        self.assertEqual(report['registration_intents']['historical_rows'],1)
        self.assertEqual(report['required_second_pass_states']['whole_row_review_beforeimage_present'],1)
    def test_historical_intent_cannot_be_excused_by_a_different_current_owner(self):
        f=self.root/'batches/fixture/001.json';rows=json.loads(f.read_text());rows[0]['reason']='Changed fixture';put(f,rows)
        self.alter_db('UPDATE drafts SET reason=? WHERE source_id=?',(rows[0]['reason'],'A0'))
        with self.assertRaisesRegex(AssertionError,'Historical intent'):self.collect()
    def test_terminal_queue_cannot_hide_accessible_first_passes_outside_its_ids(self):
        f=self.root/'batches/fixture/001.json';rows=json.loads(f.read_text());rows.pop();put(f,rows)
        self.alter_db('DELETE FROM drafts WHERE source_id=?',('A8',));self.alter_db('DELETE FROM draft_sources WHERE source_id=?',('A8',))
        f=self.root/'registered-batches.json';registry=json.loads(f.read_text());del registry['CODE8|A8'];put(f,registry)
        folder=self.root/'runtime/exhaustive/jobs/intent'
        # This fixture is a not-yet-admitted identity, not a partial committed
        # registration. Adjust its complete intention to its actual eight rows.
        intent=json.loads((folder/'registration-intent.json').read_text());intent['rows']=rows;put(folder/'registration-intent.json',intent)
        receipt=json.loads((folder/'registration-complete.json').read_text());receipt['accepted_articles']=8;put(folder/'registration-complete.json',receipt)
        report=self.collect();self.assertEqual(len(report['accessible_first_pass_pending']),1)
        with self.assertRaisesRegex(t.Blocked,'Accessible'):self.controller().run(3122)
        self.assertFalse((self.root/t.DISABLED).exists());self.assertEqual(self.backend.launches,0)

    def test_launched_without_accepted_new_pid_review_stays_pending_without_relaunch(self):
        def remove_accepted():
            f=self.root/'runtime/exhaustive/job-metrics.jsonl'
            data=[json.loads(x) for x in f.read_text().splitlines()]
            put(f,b''.join((json.dumps(x)+'\n').encode() for x in data if x.get('coordinator_pid')!=9123))
        self.backend.after_launch=remove_accepted
        with self.assertRaisesRegex(Exception,'fresh accepted review'):self.controller().run(3122)
        with self.assertRaisesRegex(Exception,'fresh accepted review'):self.controller().run(3122)
        self.assertEqual(self.backend.launches,1);self.assertTrue((self.root/t.DISABLED).exists())
    def test_late_acceptance_requires_whole_archived_beforeimage(self):
        def tamper_beforeimage():
            f=self.root/'runtime/exhaustive/jobs/review-accepted/source.json'
            rows=json.loads(f.read_text());rows[0]['previous_draft']['review_notes']='Unrelated note';put(f,rows)
        self.backend.after_launch=tamper_beforeimage
        with self.assertRaisesRegex(Exception,'whole beforeimage'):self.controller().run(3122)
        self.assertEqual(self.backend.launches,1);self.assertTrue((self.root/t.DISABLED).exists())
    def test_accepted_native_header_without_response_never_completes_transfer(self):
        def header_only():
            f=self.root/'runtime/exhaustive/jobs/review-accepted/errors-1.log'
            put(f,(f.read_text().split('\ncodex\n')[0]+'\n').encode())
        self.backend.after_launch=header_only
        with self.assertRaisesRegex(Exception,'native execution'):self.controller().run(3122)
        self.assertEqual(self.backend.launches,1)
    def test_late_resume_imports_only_pinned_source_parser_after_interruption(self):
        self.backend.after_launch=lambda:(_ for _ in ()).throw(KeyboardInterrupt())
        with self.assertRaises(KeyboardInterrupt):self.controller().run(3122)
        self.unload()
        result=self.controller().run(3122)
        self.assertEqual(result['phase'],'COMPLETE');self.assertEqual(result['new_coordinator']['accepted_review']['articles'],1)
    def test_exit_temporal_binding_rejects_receipt_before_last_actual_observation(self):
        identity=self.backend.entry(3122)['identity'];self.backend.old=False;self.backend.clock=2100
        put(self.root/'runtime/exhaustive/coordinator-exit.json',dict(pid=3122,ended_at_unix=1900,exit_code=0,exit_type=None,stop_requested=False))
        with self.assertRaises(Exception):self.backend.idle(identity,set())
    def test_os_birth_from_a_different_or_future_lifetime_is_rejected(self):
        row=self.backend.processes()[0]
        for start in (None,True,990,2100,1100):
            with self.subTest(start=start),self.assertRaises(t.Blocked):t.bind_process(row,dict(pid=3122,started_at_unix=start),2000)
        for stamp in ('22/10/2026 20:54:15','Thu Oct 22 20:54:15 PDT 2026',None):
            with self.subTest(stamp=stamp),self.assertRaises(t.Blocked):t.utc_birth(stamp)
    def test_configured_plan_cannot_be_replaced_on_resume(self):
        class Interrupt(t.Transfer):
            def phase(self,name,**kw):
                super().phase(name,**kw)
                if name=='CONFIGURED':raise KeyboardInterrupt()
        with self.assertRaises(KeyboardInterrupt):self.controller(Interrupt).run(3122)
        put(self.root/t.PLAN,dict(capacity=999,current_workers=999,role_limits=dict(new=0,review=999)))
        with self.assertRaises(t.Conflict):self.controller().run(3122)
        self.assertEqual(self.backend.launches,0)

    def test_existing_launcher_imports_installed_dependencies_from_its_own_root(self):
        # A fixture launcher returns without Popen; it tests module resolution.
        put(self.root/'worker_capacity.py',b'MARKER="installed fixture"\n')
        put(self.root/'supervise_exhaustive.py',b'import worker_capacity\ndef launch(folder): return worker_capacity.MARKER\n')
        self.addCleanup(lambda:sys.modules.pop('worker_capacity',None))
        self.assertEqual(t.NativeBackend(self.root).launch(self.run_dir),'installed fixture')

    def test_missing_admission_control_never_becomes_a_known_empty_value_on_resume(self):
        class Interrupt(t.Transfer):
            def phase(self,name,**kw):
                super().phase(name,**kw)
                if name=='RECONCILED':raise KeyboardInterrupt()
        with self.assertRaises(KeyboardInterrupt):self.controller(Interrupt).run(3122)
        (self.root/t.HOT).unlink()
        with self.assertRaises(t.Conflict):self.controller().run(3122)
        self.assertEqual(self.backend.launches,0)
    def test_postlaunch_timeout_never_rolls_back_a_running_installation(self):
        original=self.backend.launched
        self.backend.launched=lambda *a,**kw:(_ for _ in ()).throw(TimeoutError('Fixture OS timeout'))
        with self.assertRaises(TimeoutError):self.controller().run(3122)
        state=t.required_json(self.run_dir/'state.json');self.assertEqual(state['phase'],'LAUNCHED')
        self.assertTrue((self.root/t.DISABLED).exists());self.assertEqual(t.required_json(self.root/t.HOT)['review_tail_limit'],8)
        self.backend.launched=original
        self.assertEqual(self.controller().run(3122)['phase'],'COMPLETE');self.assertEqual(self.backend.launches,1)

    def test_interruption_after_exact_pause_unlink_resumes_adoption_without_relaunch(self):
        class Interrupt(t.Transfer):
            def restore(self,names):
                super().restore(names)
                if names==[t.DISABLED]:raise KeyboardInterrupt()
        with self.assertRaises(KeyboardInterrupt):self.controller(Interrupt).run(3122)
        self.assertFalse((self.root/t.DISABLED).exists())
        self.assertEqual(t.required_json(self.run_dir/'state.json')['phase'],'ADOPTION_VERIFIED')
        self.assertEqual(self.controller().run(3122)['phase'],'COMPLETE');self.assertEqual(self.backend.launches,1)
    def test_intervening_pause_after_release_intent_is_never_cleared(self):
        class Interrupt(t.Transfer):
            def restore(self,names):
                super().restore(names)
                if names==[t.DISABLED]:raise KeyboardInterrupt()
        with self.assertRaises(KeyboardInterrupt):self.controller(Interrupt).run(3122)
        put(self.root/t.DISABLED,b'intervening operator pause')
        with self.assertRaises(t.Conflict):self.controller().run(3122)
        self.assertEqual((self.root/t.DISABLED).read_bytes(),b'intervening operator pause');self.assertEqual(self.backend.launches,1)

    def test_predrain_inventory_allows_a_guarded_review_staging_window(self):
        # Existing first-pass DB rows are complete while a current review is
        # preparing an owner replacement. This permits admission closure only.
        f=self.root/'batches/fixture/001.json';rows=json.loads(f.read_text());rows[0]['reason']='Staged current review';put(f,rows)
        report=self.backend.first_pass_inventory(self.pins())
        self.assertTrue(report['all_accessible_first_passes_registered'])
        self.assertTrue(report['full_registration_reconciliation_still_required_after_exit'])
        with self.assertRaises(AssertionError):self.collect()

    def test_old_worklist_subset_cannot_authorize_all_corpus_review_transfer(self):
        path=self.root/'runtime/radical-review-20261019.json';data=json.loads(path.read_text());data['prior_articles']=data['prior_articles'][:1];put(path,data)
        report=self.collect();self.assertFalse(report['required_second_pass_worklist_ready'])
        self.assertEqual(len(report['required_second_pass_worklist_blockers']),8)
        self.assertFalse(self.backend.reconcile(self.pins())['required_second_pass_worklist_ready'])
    def test_completed_manifest_flag_needs_a_whole_current_archived_beforeimage(self):
        path=self.root/'runtime/radical-review-20261019.json';data=json.loads(path.read_text());data['prior_articles'][0]['review_status']='completed';put(path,data)
        report=self.collect();self.assertEqual(report['required_second_pass_states']['legacy_review_flag_needs_reconciliation'],1)
        self.assertFalse(self.backend.reconcile(self.pins())['required_second_pass_worklist_ready'])

    def independent_fixture(self,reference_only=False):
        self.collect() # Load only this fixture root through the reconciler.
        f=self.root/'batches/fixture/001.json';rows=json.loads(f.read_text());old=copy.deepcopy(rows[0])
        rows[0]['prior_proposal_sha256']=h(old['proposed_xml']);put(f,rows)
        archive=[old|dict(replacement=rows[0])]
        put(self.root/'revisions/radical-review'/(h(json.dumps(archive,ensure_ascii=False,sort_keys=True))+'.json'),archive)
        source=json.loads((self.root.parent/'sites/liberer-la-retraite/dist/corpus/s0.json').read_text())[0]
        source['previous_draft']=old|dict(proposed_sha256=h(old['proposed_xml']))
        if reference_only:source['reference_recheck_only']=True
        folder=self.root/'runtime/exhaustive/jobs/review-current';put(folder/'source.json',[source]);put(folder/'answer.json',[rows[0]])
        put(folder/'coordination.json',[]);put(folder/'policy.json',[])
        put(folder/'policy-fingerprint.json',dict(radical_review=True,coordination_sha256=h((folder/'coordination.json').read_bytes())))
        import reference_coherence as refs
        db=self.real_connect(self.root/'corpus.sqlite')
        try:snapshot=refs.capture(db,[source],[rows[0]],refs.focus())
        finally:db.close()
        put(folder/'reference-targets.json',snapshot)
        log=folder/'errors-1.log';session='01234567-0123-0123-0123-000000000003'
        put(log,('OpenAI Codex v0.160.1\n--------\nworkdir: '+str(folder)+'\nmodel: gpt-6-astra\nprovider: openai\nreasoning effort: medium\nsession id: '+session+'\n--------\ncodex\nCurrent fixture review.\n').encode())
        put(folder/'execution-observed-1.json',dict(source_log=str(log)))
        metric=dict(coordinator_pid=3122,kind='review',outcome='reviewed',job=folder.name,articles=1,attempts=1,execution_session_id=session,started_at_unix=1100,finished_at_unix=1200)
        metrics=self.root/'runtime/exhaustive/job-metrics.jsonl';metrics.write_bytes(metrics.read_bytes()+(json.dumps(metric)+'\n').encode())
        return folder
    def test_worklist_publication_covers_later_first_passes_and_preserves_full_history(self):
        path=self.root/t.WORKLIST;old=json.loads(path.read_text());old['prior_articles']=old['prior_articles'][:1];old['funding']='No invented savings';put(path,old);before=path.read_bytes()
        result=self.controller().run(3122);after=json.loads(path.read_text())
        self.assertEqual(len(after['prior_articles']),9);self.assertEqual(after['funding'],'No invented savings')
        self.assertEqual(t.decoded(result['mutations'][t.WORKLIST]['before']),before)
        self.assertEqual(after['complete_canonical_worklist']['canonical_identities'],9)
        hot=t.required_json(self.root/t.HOT);self.assertEqual(hot['role_limits'],dict(new=6,review=0));self.assertEqual(hot['workers'],8)
    def test_only_native_current_substantive_review_is_completed_in_new_inventory(self):
        from review_worklist import build,matches
        self.independent_fixture();report=self.collect();old=t.required_json(self.root/t.WORKLIST)
        manifest=build(report,old,'fixture-owner')
        self.assertEqual(manifest['completed_second_pass'],1)
        self.assertEqual(sum(x['review_status']=='pending' for x in manifest['prior_articles']),8)
        self.assertTrue(matches(report,manifest))
    def test_reference_only_review_remains_open_in_full_worklist(self):
        from review_worklist import build
        self.independent_fixture(reference_only=True);report=self.collect()
        self.assertEqual(build(report,t.required_json(self.root/t.WORKLIST),'owner')['completed_second_pass'],0)
        self.assertEqual(report['unproven_historical_native_reviews'][0]['reason'],'reference_only_not_substantive_second_pass')
    def test_historical_completed_flag_does_not_certify_current_independent_pass(self):
        from review_worklist import build
        path=self.root/t.WORKLIST;old=t.required_json(path);old['prior_articles'][0]['review_status']='completed';put(path,old)
        result=build(self.collect(),old,'owner');self.assertEqual(result['completed_second_pass'],0)
        self.assertEqual(result['prior_articles'][0]['previous_policy_review_status'],'completed')
    def test_header_without_response_does_not_certify_published_completion(self):
        self.independent_fixture();log=self.root/'runtime/exhaustive/jobs/review-current/errors-1.log';put(log,(log.read_text().split('\ncodex\n')[0]+'\n').encode())
        self.assertEqual(self.collect()['independent_native_review_rows'],0)
    def test_reused_native_session_cannot_certify_two_distinct_jobs(self):
        self.independent_fixture();path=self.root/'runtime/exhaustive/job-metrics.jsonl'
        rows=[json.loads(x) for x in path.read_text().splitlines()];other=rows[-1]|dict(job='other-job',kind='new',outcome='accepted')
        path.write_bytes(path.read_bytes()+(json.dumps(other)+'\n').encode())
        self.assertEqual(self.collect()['independent_native_review_rows'],0)
    def test_native_review_of_older_policy_is_not_inherited(self):
        folder=self.independent_fixture();put(folder/'policy.json',[dict(unrelated='old policy')])
        self.assertEqual(self.collect()['independent_native_review_rows'],0)
    def test_current_impact_metadata_must_equal_the_actual_native_answer(self):
        folder=self.independent_fixture();path=folder/'answer.json';rows=json.loads(path.read_text());rows[0]['benefit_assessment']='Unrelated';put(path,rows)
        self.assertEqual(self.collect()['independent_native_review_rows'],0)
    def test_worklist_binds_current_targets_and_whole_notes(self):
        from review_worklist import build,matches
        proof=self.collect();manifest=build(proof,t.required_json(self.root/t.WORKLIST),'owner')
        for field,value in [('current_reference_target_views',dict(target=dict(proposal='changed'))),('source_notes_sha256','changed')]:
            changed=copy.deepcopy(proof);changed['required_second_pass_dispositions'][0]['current_guard'][field]=value
            self.assertFalse(matches(changed,manifest))
    def test_documentary_holds_stay_explicitly_unverified_and_not_pending_native_work(self):
        from review_worklist import build
        proof=self.collect();row=proof['required_second_pass_dispositions'][-1];row['state']='first_pass_open'
        proof['documentary_holds']=[dict(code_id=row['code_id'],source_id=row['source_id'])]
        result=build(proof,t.required_json(self.root/t.WORKLIST),'owner')
        self.assertEqual(len(result['prior_articles']),8);self.assertEqual(len(result['documentary_holds']),1)
        self.assertFalse(result['documentary_holds'][0]['counts_as_verified'])
    def test_unknown_missing_first_pass_never_becomes_documentary_hold(self):
        from review_worklist import build
        proof=self.collect();proof['required_second_pass_dispositions'][0]['state']='first_pass_open'
        with self.assertRaisesRegex(ValueError,'unclassified'):build(proof,t.required_json(self.root/t.WORKLIST),'owner')
    def test_duplicate_canonical_identity_never_publishes(self):
        from review_worklist import build
        proof=self.collect();proof['required_second_pass_dispositions'][0]=proof['required_second_pass_dispositions'][1]
        with self.assertRaisesRegex(ValueError,'duplicated'):build(proof,t.required_json(self.root/t.WORKLIST),'owner')
    def test_interruption_after_worklist_publication_recollects_and_launches_once(self):
        class Interrupt(t.Transfer):
            def phase(self,name,**kw):
                super().phase(name,**kw)
                if name=='WORKLIST_PUBLISHED':raise KeyboardInterrupt()
        with self.assertRaises(KeyboardInterrupt):self.controller(Interrupt).run(3122)
        before=self.backend.collects
        self.assertEqual(self.controller().run(3122)['phase'],'COMPLETE')
        self.assertGreater(self.backend.collects,before);self.assertEqual(self.backend.launches,1)
    def test_journal_before_worklist_rename_resumes_from_original_bytes(self):
        original=t.durable;done=False
        def interrupt(path,data):
            nonlocal done
            if Path(path)==self.root/t.WORKLIST and not done:done=True;raise KeyboardInterrupt()
            return original(path,data)
        with patch.object(t,'durable',side_effect=interrupt),self.assertRaises(KeyboardInterrupt):self.controller().run(3122)
        self.assertEqual(self.controller().run(3122)['phase'],'COMPLETE');self.assertEqual(self.backend.launches,1)
    def test_interruption_after_worklist_rename_before_receipt_resumes_exact_after_bytes(self):
        original=t.durable;done=False
        def interrupt(path,data):
            nonlocal done
            original(path,data)
            if Path(path)==self.root/t.WORKLIST and not done:done=True;raise KeyboardInterrupt()
        with patch.object(t,'durable',side_effect=interrupt),self.assertRaises(KeyboardInterrupt):self.controller().run(3122)
        self.assertEqual(self.controller().run(3122)['phase'],'COMPLETE');self.assertEqual(self.backend.launches,1)
    def test_intervening_worklist_bytes_are_preserved_and_block_resume(self):
        class Interrupt(t.Transfer):
            def phase(self,name,**kw):
                super().phase(name,**kw)
                if name=='WORKLIST_PUBLISHED':raise KeyboardInterrupt()
        with self.assertRaises(KeyboardInterrupt):self.controller(Interrupt).run(3122)
        path=self.root/t.WORKLIST;data=json.loads(path.read_text());data['instruction']='Intervening instruction';put(path,data);intervening=path.read_bytes()
        with self.assertRaises(t.Conflict):self.controller().run(3122)
        self.assertEqual(path.read_bytes(),intervening);self.assertEqual(self.backend.launches,0)
    def test_changed_whole_db_after_publication_blocks_launch(self):
        class Interrupt(t.Transfer):
            def phase(self,name,**kw):
                super().phase(name,**kw)
                if name=='WORKLIST_PUBLISHED':raise KeyboardInterrupt()
        with self.assertRaises(KeyboardInterrupt):self.controller(Interrupt).run(3122)
        self.alter_db('UPDATE drafts SET review_notes=? WHERE source_id=?',('Changed','A2'))
        with self.assertRaises(AssertionError):self.controller().run(3122)
        self.assertEqual(self.backend.launches,0)
    def test_prepared_entry_requires_current_zero_review_admission_control(self):
        put(self.root/t.HOT,dict(workers=7,role_limits=dict(new=6,review=1)))
        with self.assertRaisesRegex(t.Blocked,'role control'):self.controller().run(3122)
        self.assertEqual(self.backend.launches,0)

    def test_stale_reference_snapshot_does_not_inherit_native_completion(self):
        folder=self.independent_fixture();path=folder/'reference-targets.json';snapshot=json.loads(path.read_text());snapshot['version']=0;put(path,snapshot)
        report=self.collect();self.assertEqual(report['independent_native_review_rows'],0)
        self.assertEqual(report['unproven_historical_native_reviews'][0]['reason'],'historical_reference_guards_or_assessments_not_current')
    def test_historical_outside_rows_are_preserved_without_inflating_canonical_coverage(self):
        from review_worklist import build,matches
        proof=self.collect();manifest=build(proof,t.required_json(self.root/t.WORKLIST),'owner')
        self.assertEqual(len(manifest['historical_outside_current_inventory']),4)
        self.assertEqual(len(manifest['prior_articles']),9)
        manifest['historical_outside_current_inventory']=[];self.assertFalse(matches(proof,manifest))
    def test_publication_cannot_claim_different_policy_or_code_pins(self):
        from review_worklist import build,matches
        proof=self.collect();manifest=build(proof,t.required_json(self.root/t.WORKLIST),'owner')
        manifest['complete_canonical_worklist']['policy_and_code_pins']['policy-coordinations.json']='different'
        self.assertFalse(matches(proof,manifest))

    def test_existing_review_reader_consumes_all_new_canonical_worklist_rows(self):
        self.collect()
        for name in ['sru_context','contrat_unique_priority']:
            shutil.copyfile(PROJECT/(name+'.py'),self.root/(name+'.py'));sys.modules.pop(name,None)
            self.addCleanup(lambda n=name:sys.modules.pop(n,None))
        self.controller().run(3122)
        sys.path.insert(0,str(self.root))
        try:
            import importlib
            sys.modules.pop('review_prior',None);prior=importlib.import_module('review_prior')
            self.addCleanup(lambda:sys.modules.pop('review_prior',None))
            sources={}
            for spec in json.loads((self.root/'corpus.json').read_text())['codes']+json.loads((self.root/'corpus.json').read_text())['annexes']:
                sources[spec['slug']]=json.loads((self.root.parent/('sites/liberer-la-retraite/dist/corpus/'+spec['slug']+'.json')).read_text())
            jobs=prior.build_jobs(sources)
        finally:sys.path.pop(0)
        captured=[a for slug,index,articles in jobs for a in articles]
        self.assertEqual(len(captured),9)
        for row in captured:
            before=row['previous_draft'];self.assertIn('batch_row_sha256',before)
            self.assertEqual(before['reason'],'Fixture reason.');self.assertEqual(before['review_notes'],'Fixture notes.')

    def test_installed_candidate_supports_eight_tail_admissions_and_lowering_to_zero(self):
        self.controller().run(3122)
        import importlib.util
        spec=importlib.util.spec_from_file_location('_capacity_fixture',self.root/'worker_capacity.py');capacity=importlib.util.module_from_spec(spec);spec.loader.exec_module(capacity)
        runtime=self.root/'runtime/exhaustive'
        self.assertEqual(capacity.admission_limits(runtime,8,review_tail=True),dict(workers=8,role_limits=dict(new=0,review=8)))
        hot=t.required_json(runtime/'worker-limit.json');hot['review_tail_limit']=0;put(runtime/'worker-limit.json',hot)
        self.assertEqual(capacity.admission_limits(runtime,8,review_tail=True)['role_limits'],dict(new=0,review=0))
        self.assertEqual(capacity.admission_limits(runtime,8)['role_limits'],dict(new=6,review=0))

    def test_future_dated_metric_cannot_inherit_review_completion(self):
        self.independent_fixture();path=self.root/'runtime/exhaustive/job-metrics.jsonl'
        rows=[json.loads(x) for x in path.read_text().splitlines()];rows[-1]['finished_at_unix']=time.time()+600
        path.write_bytes(b''.join((json.dumps(x)+'\n').encode() for x in rows))
        self.assertEqual(self.collect()['independent_native_review_rows'],0)
    def test_separate_consistent_review_sessions_count_identity_once(self):
        folder=self.independent_fixture();second=folder.parent/'review-current-second';shutil.copytree(folder,second)
        old='01234567-0123-0123-0123-000000000003';new='01234567-0123-0123-0123-000000000004'
        text=(second/'errors-1.log').read_text().replace(str(folder),str(second)).replace(old,new);put(second/'errors-1.log',text.encode())
        put(second/'execution-observed-1.json',dict(source_log=str(second/'errors-1.log')))
        path=self.root/'runtime/exhaustive/job-metrics.jsonl';metrics=[json.loads(x) for x in path.read_text().splitlines()]
        metric=metrics[-1]|dict(job=second.name,execution_session_id=new,finished_at_unix=1201)
        path.write_bytes(path.read_bytes()+(json.dumps(metric)+'\n').encode())
        proof=self.collect();self.assertEqual(proof['independent_native_review_rows'],1)
        found=[x for x in proof['required_second_pass_dispositions'] if x.get('independent_review_evidence')]
        self.assertEqual(len(found),1);self.assertEqual(found[0]['independent_review_evidence']['job'],second.name)
    def test_real_release_gate_uses_pinned_helpers_and_no_external_enable_flag(self):
        import importlib.util
        folder=self.root/'runtime'/t.PACKAGE;folder.mkdir(parents=True)
        for name in ['transfer_controller.py','registration_reconciliation.py','transfer_guards.py','accepted_work.py','review_worklist.py','baseline-policy-pins.json','release-input-pins.json']:
            shutil.copyfile(STAGE/name,folder/name)
        spec=importlib.util.spec_from_file_location('_gate_fixture',folder/'transfer_controller.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        with patch.object(module,'APPROVED_ROOT',self.root):
            backend=module.NativeBackend(self.root)
            with patch.object(backend,'processes',side_effect=AssertionError('No OS collection in sealed gate')):
                result=backend.reconciliation_precondition();self.assertEqual(result['initial_hot_sha256'],t.INITIAL_HOT_SHA)
                self.assertEqual(result['expected_baseline_pins'],json.loads((folder/'baseline-policy-pins.json').read_text()))
                put(folder/'review_worklist.py',b'changed helper')
                with self.assertRaisesRegex(module.Blocked,'helper changed'):backend.reconciliation_precondition()
    def test_release_resume_rejects_forged_state_pins_before_any_launch(self):
        pins=self.pins();gate=dict(expected_baseline_pins=pins,initial_hot_sha256=h((self.root/t.HOT).read_bytes()),controller_sha256='fixture-controller',release_helpers_sha256='fixture-inputs')
        self.backend.reconciliation_precondition=lambda:gate
        class Interrupt(t.Transfer):
            def phase(self,name,**kw):
                super().phase(name,**kw)
                if name=='RECONCILED':raise KeyboardInterrupt()
        with self.assertRaises(KeyboardInterrupt):self.controller(Interrupt).run(3122)
        path=self.run_dir/'state.json';state=json.loads(path.read_text());state['pins']['policy-coordinations.json']='forged';put(path,state)
        with self.assertRaisesRegex(t.Blocked,'sealed release baseline'):self.controller().run(3122)
        self.assertEqual(self.backend.launches,0)
    def test_release_resume_rejects_changed_controller_identity(self):
        pins=self.pins();gate=dict(expected_baseline_pins=pins,initial_hot_sha256=h((self.root/t.HOT).read_bytes()),controller_sha256='fixture-controller',release_helpers_sha256='fixture-inputs')
        self.backend.reconciliation_precondition=lambda:gate
        class Interrupt(t.Transfer):
            def phase(self,name,**kw):
                super().phase(name,**kw)
                if name=='RECONCILED':raise KeyboardInterrupt()
        with self.assertRaises(KeyboardInterrupt):self.controller(Interrupt).run(3122)
        gate=dict(gate,controller_sha256='different-controller')
        with self.assertRaisesRegex(t.Blocked,'controller or release helper'):self.controller().run(3122)
        self.assertEqual(self.backend.launches,0)

    def test_canonical_source_and_public_reader_views_have_exact_separate_guards(self):
        self.collect();import source_assets as assets
        raw="<p>L'emploi &amp; les droits sont préservés.</p><br />";notes="<p>L'application demeure.</p>"
        fields=(raw,'2000-01-01','2999-01-01','12')
        exported=dict(source_xml=assets.safe_html(raw),valid_from=fields[1],valid_until=fields[2],number=fields[3],source_notes_xml=assets.safe_html(notes))
        rr.source_export_matches(fields,exported,notes,assets)
        for field,value in [('source_xml',assets.safe_html(raw.replace('préservés','supprimés'))),('source_notes_xml',''),('valid_from','2001-01-01'),('number','13')]:
            changed=exported|{field:value}
            with self.subTest(field=field),self.assertRaises(AssertionError):rr.source_export_matches(fields,changed,notes,assets)
        # Raw canonical text is not substituted for its escaped public view.
        with self.assertRaises(AssertionError):rr.source_export_matches(fields,exported|dict(source_xml=raw),notes,assets)

    def test_only_exact_known_historical_outside_manifest_rows_are_preserved(self):
        from review_worklist import build
        path=self.root/t.WORKLIST;manifest=t.required_json(path)
        outside=t.required_json(self.root/'runtime/completion-coverage-inventory-20261023T0254Z/outside-current-inventory.json')
        for row in outside:
            manifest['prior_articles'].append(dict(code_id=row['code_id'],source_id=row['source_id'],source_sha256=row['draft_guards']['source_sha256'],proposed_sha256=row['draft_guards']['proposal_sha256'],review_status='outside_current_inventory'))
        put(path,manifest);proof=self.collect();result=build(proof,manifest,'fixture-owner')
        self.assertEqual(len(result['prior_articles']),9);self.assertEqual(len(result['outside_current_inventory']),4)
        self.assertEqual(len(result['historical_outside_current_inventory']),4)
        manifest['prior_articles'][-1]['proposed_sha256']='changed';put(path,manifest)
        with self.assertRaisesRegex(AssertionError,'Historical outside review guard'):self.collect()
    def test_unknown_noncanonical_manifest_status_or_identity_blocks(self):
        path=self.root/t.WORKLIST;manifest=t.required_json(path)
        manifest['prior_articles'].append(dict(code_id='UNKNOWN',source_id='UNKNOWN',source_sha256='x',proposed_sha256='x',review_status='outside_current_inventory'));put(path,manifest)
        with self.assertRaisesRegex(AssertionError,'Unclassified noncanonical'):self.collect()
    def handoff_fixture(self):
        import journal_handoff as h
        old_stage=self.root/'runtime'/t.PACKAGE;old_stage.mkdir(parents=True,exist_ok=True)
        put(old_stage/'transfer_controller.py',b'fixture old controller');put(old_stage/'release-input-pins.json',b'fixture old helper pins')
        manifest=dict(files={n:dict(sha256=h.sha((old_stage/n).read_bytes())) for n in ['transfer_controller.py','release-input-pins.json']})
        put(old_stage/'manifest.json',manifest)
        pins=self.pins();old_gate=dict(expected_baseline_pins=pins,initial_hot_sha256=h.sha((self.root/t.HOT).read_bytes()),controller_sha256=h.sha((old_stage/'transfer_controller.py').read_bytes()),release_helpers_sha256=h.sha((old_stage/'release-input-pins.json').read_bytes()))
        self.backend.reconciliation_precondition=lambda:old_gate
        class Interrupt(t.Transfer):
            def phase(self,name,**kw):
                super().phase(name,**kw)
                if name=='NATURALLY_DRAINED':raise KeyboardInterrupt()
        with self.assertRaises(KeyboardInterrupt):self.controller(Interrupt).run(3122)
        new_gate=old_gate|dict(controller_sha256='fixture new controller',release_helpers_sha256='fixture new pins')
        self.backend.reconciliation_precondition=lambda:new_gate
        for attribute,value in [('APPROVED_ROOT',self.root),('OLD_PACKAGE',t.PACKAGE),('OLD_MANIFEST_SHA',h.sha((old_stage/'manifest.json').read_bytes())),('NativeBackend',lambda root:self.backend)]:
            patcher=patch.object(h,attribute,value);patcher.start();self.addCleanup(patcher.stop)
        return h,self.run_dir,self.root/'runtime'/t.PACKAGE/'runs/continued'
    def test_owned_drained_journal_handoff_preserves_old_proof_and_launches_once(self):
        h,old,new=self.handoff_fixture();before=(old/'state.json').read_bytes();owner=json.loads(before)['owner']
        receipt=h.handoff(self.root,old,new);self.assertEqual(receipt['owner'],owner)
        self.assertEqual((old/'state.json').read_bytes(),before)
        state=t.required_json(new/'state.json');self.assertEqual(state['phase'],'RECONCILIATION_REQUIRED');self.assertEqual(state['owner'],owner)
        self.assertEqual(t.required_json(self.root/t.DISABLED)['state_file'],str(new/'state.json'))
        self.assertEqual(t.Transfer(self.root,self.sealed,new,self.backend,timeout=2).run(3122)['phase'],'COMPLETE');self.assertEqual(self.backend.launches,1)
    def test_handoff_resume_before_new_journal_write_does_not_lose_owned_pause(self):
        h,old,new=self.handoff_fixture();original=h.durable;done=False
        def interrupt(path,data):
            nonlocal done
            if Path(path)==new/'state.json' and not done:done=True;raise KeyboardInterrupt()
            return original(path,data)
        with patch.object(h,'durable',side_effect=interrupt),self.assertRaises(KeyboardInterrupt):h.handoff(self.root,old,new)
        self.assertEqual(t.required_json(self.root/t.DISABLED)['state_file'],str(old/'state.json'))
        h.handoff(self.root,old,new);self.assertEqual(t.required_json(self.root/t.DISABLED)['state_file'],str(new/'state.json'))
    def test_handoff_resume_after_pause_cas_issues_receipt_without_relaunch(self):
        h,old,new=self.handoff_fixture();original=h.durable;done=False
        def interrupt(path,data):
            nonlocal done
            original(path,data)
            if Path(path)==self.root/t.DISABLED and not done:done=True;raise KeyboardInterrupt()
        with patch.object(h,'durable',side_effect=interrupt),self.assertRaises(KeyboardInterrupt):h.handoff(self.root,old,new)
        self.assertEqual(t.required_json(self.root/t.DISABLED)['state_file'],str(new/'state.json'))
        result=h.handoff(self.root,old,new);self.assertEqual(result['launches'],0)
        self.assertEqual(h.handoff(self.root,old,new),result)
    def test_handoff_preserves_foreign_pause_and_refuses_unknown_state(self):
        h,old,new=self.handoff_fixture();put(self.root/t.DISABLED,b'operator intervening pause')
        with self.assertRaises(t.Conflict):h.handoff(self.root,old,new)
        self.assertEqual((self.root/t.DISABLED).read_bytes(),b'operator intervening pause');self.assertFalse((new/'state.json').exists())
    def test_handoff_refuses_any_module_installation_or_changed_predecessor(self):
        h,old,new=self.handoff_fixture();path=old/'state.json';state=json.loads(path.read_text());state['mutations']['run_exhaustive.py']=dict(before=None,after='changed');put(path,state)
        with self.assertRaisesRegex(t.Blocked,'never-installed'):h.handoff(self.root,old,new)
        self.assertEqual(self.backend.launches,0)
    def test_handoff_requires_no_manual_reservations_and_actual_exit(self):
        h,old,new=self.handoff_fixture();put(self.root/'runtime/exhaustive/manual-agent-slots.json',[dict(owner='other')])
        with self.assertRaisesRegex(t.Blocked,'Manual reservations'):h.handoff(self.root,old,new)
        put(self.root/'runtime/exhaustive/manual-agent-slots.json',[]);self.backend.old=True
        with self.assertRaisesRegex(t.Blocked,'descendant remains'):h.handoff(self.root,old,new)

if __name__=='__main__':unittest.main(verbosity=2)
