"""Independent offline regressions against immutable reviewed file copies.

Expected failures expose baseline defects. All writes are in memory or temp.
"""
from pathlib import Path
from unittest import TestCase,main,expectedFailure
from unittest.mock import patch
from tempfile import TemporaryDirectory
from types import ModuleType,SimpleNamespace
import contextlib,copy,json,os,sqlite3,sys,threading

P=Path(__file__).resolve().parent
LEGAL=P.parents[3]
VARIANT=os.environ.get('REVIEW_VARIANT','baseline')
sys.path.insert(0,str(LEGAL))
audit=ModuleType('reviewed_reference_coherence')
audit.__file__=str(LEGAL/'reference_coherence.py')
exec(compile((P/('reference_coherence.py.'+VARIANT+'.txt')).read_text(),audit.__file__,'exec'),audit.__dict__)
queue=ModuleType('reviewed_reference_queue')
queue.__file__=str(LEGAL/'reference_queue.py')
with patch.dict(sys.modules,{'reference_coherence':audit}):
    exec(compile((P/'reference_queue.py.baseline.txt').read_text(),queue.__file__,'exec'),queue.__dict__)

class Cases(TestCase):
    def setUp(self):
        self.tmp=TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        (self.root/'batches').mkdir()
        (self.root/'runtime').mkdir()
        self.db=sqlite3.connect(self.root/'corpus.sqlite',check_same_thread=False);self.addCleanup(self.db.close)
        self.db.executescript('CREATE TABLE articles(code_id,id,number,source_sha256,content_xml); CREATE TABLE drafts(code_id,source_id,source_sha256,status,proposed_xml,reason,review_notes); CREATE TABLE documents(code_id,id,kind,xml);')
        self.catalog={}
        for identifier,number in [('A','L10-1'),('B','L20-1'),('C','L20-2')]:
            r={'code_id':'CODE','source_id':identifier,'number':number,'source_sha256':'s'+identifier}
            self.catalog[audit.key(r)]=r
            self.db.execute('INSERT INTO articles VALUES(?,?,?,?,?)',('CODE',identifier,number,'s'+identifier,'<p>Source '+identifier+'.</p>'))
        self.article=self.catalog['CODE|A']|{'source_xml':'<p>Règle renvoyant à L20-1.</p>','source_notes_xml':''}
        self.body='<p>Le renvoi à L20-1 conserve les garanties applicables.</p>'
        self.known={}

    def accepted(self,article=None,body=None):
        article=article or self.article;body=body or self.body
        snap=audit.capture(self.db,[article],catalog=self.catalog)
        row=article|{'proposed_xml':body,'reference_checks':[
            {'target_key':k,'view_sha256':v['view_sha256'],
             'assessment':'Pour la cible '+k+', le champ de la garantie et sa transition sont conservés, sans en retirer les droits aux nouveaux contrats remplissant les conditions.'}
            for k,v in snap['targets'].items()]}
        audit.accept_checks([row],[article],snap,self.catalog)
        return row,snap

    def draft(self,identifier,body):
        self.db.execute('INSERT OR REPLACE INTO drafts VALUES(?,?,?,?,?,?,?)',('CODE',identifier,'s'+identifier,'rewrite_draft',body,'Motif spécifique.','Réserves spécifiques.'))
        self.db.commit()

    @expectedFailure
    def test_nested_intterim_range_requires_all_intermediate_articles(self):
        self.assertEqual(audit.token_refs('L1251-58-1 à L1251-58-6'),{f'L1251-58-{n}' for n in range(1,7)})

    @expectedFailure
    def test_application_note_reference_is_required(self):
        article=self.article|{'source_xml':'<p>Disposition autonome.</p>','source_notes_xml':'<p>La garantie de L20-2 demeure applicable aux contrats antérieurs.</p>'}
        self.assertIn('CODE|C',audit.requirements(article,catalog=self.catalog))

    @expectedFailure
    def test_changed_referrer_source_invalidates_unchanged_proposal_certificate(self):
        row,snap=self.accepted()
        self.db.execute("UPDATE articles SET source_sha256='new-source', content_xml='<p>Nouvelle condition de L20-1.</p>' WHERE id='A'")
        newer=self.article|{'source_sha256':'new-source','source_xml':'<p>Nouvelle condition de L20-1.</p>'}
        self.assertFalse(audit.certificate_current(self.db,newer,self.body,row['reference_coherence'],self.catalog))

    @expectedFailure
    def test_target_application_note_change_is_guarded_even_if_importer_hash_is_stale(self):
        self.db.execute('INSERT INTO documents VALUES(?,?,?,?)',('CODE','B','ARTICLE','<ARTICLE><NOTA><CONTENU><p>Ancien champ.</p></CONTENU></NOTA></ARTICLE>'))
        snap=audit.capture(self.db,[self.article],catalog=self.catalog)
        self.db.execute('UPDATE documents SET xml=? WHERE id=?',('<ARTICLE><NOTA><CONTENU><p>Nouveau champ transitoire.</p></CONTENU></NOTA></ARTICLE>','B'))
        with self.assertRaises(ValueError):audit.check_guards(self.db,snap)

    @expectedFailure
    def test_removed_reference_assessments_cannot_leave_a_current_certificate(self):
        row,snap=self.accepted();self.draft('A',self.body)
        row.pop('reference_checks')
        # Version 2 may keep an autonomous copy inside the certificate. Only
        # losing both copies means the required assessments are actually gone.
        row['reference_coherence'].pop('assessments',None)
        (self.root/'batches/x').mkdir();(self.root/'batches/x/001.json').write_text(json.dumps([row]))
        with patch.object(queue,'HERE',self.root),patch.object(audit,'focus',return_value=self.catalog):
            known=queue.certificates();self.known=known
            with patch.object(queue,'certificates',return_value=known):
                selected,report=queue.pending({'travail':[self.article]},save=False)
        self.assertEqual(len(selected['travail']),1)

    def test_self_reference_never_requires_its_own_old_version(self):
        article=self.article|{'source_xml':'<p>Le présent article L10-1 s’applique.</p>'}
        self.assertNotIn('CODE|A',audit.requirements(article,catalog=self.catalog))

    def test_same_batch_target_change_is_detected_by_final_queue(self):
        row,snap=self.accepted();self.draft('A',self.body);self.draft('B','<p>Cible B réécrite dans le même lot.</p>')
        self.known['CODE|A']=(audit.digest(self.body),row['reference_coherence'])
        with patch.object(queue,'HERE',self.root),patch.object(queue,'certificates',return_value=self.known),patch.object(audit,'focus',return_value=self.catalog):
            selected,report=queue.pending({'travail':[self.article]},save=False)
        self.assertEqual(len(selected['travail']),1)
        self.assertEqual(report['current_reference_certificates'],0)

    def test_target_first_draft_reexecutes_reference_review_and_converges(self):
        row,snap=self.accepted();self.draft('A',self.body)
        self.known['CODE|A']=(audit.digest(self.body),row['reference_coherence'])
        with patch.object(queue,'HERE',self.root),patch.object(queue,'REPORT',self.root/'runtime/report.json'),patch.object(queue,'certificates',side_effect=lambda:self.known),patch.object(queue,'priority',return_value=0),patch.object(audit,'focus',return_value=self.catalog):
            self.assertEqual(queue.pending({'travail':[self.article]},save=False)[1]['current_reference_certificates'],1)
            self.draft('B','<p>La garantie B change lors de sa première réécriture.</p>')
            calls=[]
            def recheck(job,*args):
                calls.append(job)
                refreshed,_=self.accepted(job[2][0],self.body)
                self.known['CODE|A']=(audit.digest(self.body),refreshed['reference_coherence'])
            coordinator=SimpleNamespace(STOP=threading.Event(),run_in_slot=recheck)
            report=queue.run(coordinator,{'travail':[self.article]},'NO_MODEL',1)
        self.assertEqual(len(calls),1)
        self.assertEqual(report['pending_reference_reviews'],0)
        self.assertTrue(report['all_detected_contract_reference_checks_current'])
        self.assertFalse(report['semantic_review_by_jurist'])

    def test_missing_assessment_is_rejected_at_acceptance(self):
        row,snap=self.accepted();row['reference_checks']=[]
        with self.assertRaisesRegex(ValueError,'no explicit assessment'):
            audit.accept_checks([row],[self.article],snap,self.catalog)

    @expectedFailure
    def test_review_registration_keeps_the_reference_guard_lock(self):
        row,snap=self.accepted();self.draft('A',self.body)
        previous={'source_sha256':'sA','status':'rewrite_draft','proposed_xml':self.body,
                  'reason':'Motif spécifique.','review_notes':'Réserves spécifiques.',
                  'proposed_sha256':audit.digest(self.body)}
        expected=self.article|{'previous_draft':previous}
        row.update(reason='Relecture de concordance.',review_notes='Conserver les garanties de B.')
        folder=self.root/'batches/x';folder.mkdir()
        (folder/'001.json').write_text(json.dumps([row]))
        (self.root/'registered-batches.json').write_text('{}')
        (self.root/'runtime/radical-review-20261019.json').write_text(json.dumps({'prior_articles':[]}))
        module=ModuleType('reviewed_prior');module.__file__=str(LEGAL/'review_prior.py')
        exec(compile((P/('review_prior.py.'+VARIANT+'.txt')).read_text(),module.__file__,'exec'),module.__dict__)
        held=[];registered=[]
        @contextlib.contextmanager
        def lock():
            self.assertFalse(held,'The file lock is deliberately non-reentrant')
            held.append(True)
            try:yield
            finally:held.clear()
        def register(db,*args):
            registered.append(True)
            self.assertTrue(held,'Reference guard lock was released before database registration')
        register_name='register_locked' if hasattr(module,'register_locked') else 'register'
        with patch.object(module,'HERE',self.root),patch.object(module,'writer_lock',lock),patch.object(module,'open_db',side_effect=lambda path:sqlite3.connect(path)),patch.object(module,register_name,side_effect=register),patch.dict(sys.modules,{'reference_coherence':audit}):
            module.commit([row],[expected],reference_snapshot=snap)
        self.assertEqual(registered,[True])

    def test_explicit_external_scope_can_be_assessed_as_inapplicable(self):
        article=self.article|{'source_xml':'<p>Renvoi historique à L20-1 dans un régime distinct.</p>'}
        row,snap=self.accepted(article)
        row['reference_checks'][0]['assessment']='Le numéro de la cible appartient ici à un régime extérieur ; ce renvoi historique ne substitue pas le contrat privé aux agents publics concernés. Les garanties autonomes restent applicables.'
        audit.accept_checks([row],[article],snap,self.catalog)
        self.assertFalse(row['reference_coherence']['semantic_review_by_jurist'])

if VARIANT=='proposed':
    for name in dir(Cases):
        method=getattr(Cases,name)
        if getattr(method,'__unittest_expecting_failure__',False):method.__unittest_expecting_failure__=False

if __name__=='__main__':main(verbosity=2)
