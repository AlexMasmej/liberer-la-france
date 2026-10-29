import contextlib,hashlib,io,json,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
import register_batches as batches
import review_prior as review
from ingest import open_db

class PriorReviewTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
        self.old_batch_here=batches.HERE;self.old_review_here=review.HERE
        batches.HERE=self.root;review.HERE=self.root
        self.db=open_db(self.root/'corpus.sqlite')
        self.source='<p>Une déclaration mensuelle est obligatoire.</p>'
        self.sha=hashlib.sha256(self.source.encode()).hexdigest()
        self.db.execute('INSERT INTO articles VALUES(?,?,?,?,?,?,?,?,?,?)',('CODE','ARTICLE','L1','2020-01-01','2999-01-01','VIGUEUR',self.source,'Une déclaration mensuelle est obligatoire.',self.sha,'official.tar.gz'));self.db.commit()
        self.row={'code_id':'CODE','source_id':'ARTICLE','source_sha256':self.sha,'number':'L1','proposed_xml':'<p>La déclaration est déposée chaque mois.</p>','reason':'Clarifie la périodicité.','review_notes':'Relecture à effectuer.','status':'rewrite_draft'}
        self.folder=self.root/'batches/worker';self.folder.mkdir(parents=True)
        self.path=self.folder/'001.json';self.path.write_text(json.dumps([self.row]))
        with contextlib.redirect_stdout(io.StringIO()):batches.register(self.db,self.root/'batches',True)
        self.prior=self.row|{'proposed_sha256':review.digest(self.row['proposed_xml'])}
        (self.root/'runtime').mkdir()
        review.revisions_manifest().write_text(json.dumps({'prior_articles':[{'code_id':'CODE','source_id':'ARTICLE','source_sha256':self.sha,'proposed_sha256':self.prior['proposed_sha256'],'review_status':'pending'}]}))
        self.expected=[self.row|{'previous_draft':self.prior}]
        self.new=self.row|{'proposed_xml':'<p>La déclaration est déposée une fois par an.</p>','reason':'Remplace douze déclarations par une déclaration annuelle.','review_notes':'Coordonner les contrôles et le calendrier des autres articles.'}
    def tearDown(self):
        self.db.close();batches.HERE=self.old_batch_here;review.HERE=self.old_review_here;self.tmp.cleanup()
    def captured_expected(self):
        return review.pending_sources({'sample':[self.row|{'source_xml':self.source}]})['sample']
    def assert_refused_without_writes(self,expected,message):
        before=self.path.read_bytes() if self.path.exists() else None
        registry=(self.root/'registered-batches.json').read_bytes()
        manifest=review.revisions_manifest().read_bytes()
        with self.assertRaisesRegex(ValueError,message):review.commit([self.new.copy()],expected)
        self.assertEqual(self.path.read_bytes() if self.path.exists() else None,before)
        self.assertEqual((self.root/'registered-batches.json').read_bytes(),registry)
        self.assertEqual(review.revisions_manifest().read_bytes(),manifest)
        self.assertFalse((self.root/'revisions/radical-review').exists())
    def test_preserves_before_image_and_canonical_source(self):
        with contextlib.redirect_stdout(io.StringIO()):review.commit([self.new],self.expected)
        self.assertEqual(self.db.execute('SELECT content_xml FROM articles').fetchone()[0],self.source)
        self.assertEqual(self.db.execute('SELECT proposed_xml FROM drafts').fetchone()[0],self.new['proposed_xml'])
        archive=list((self.root/'revisions/radical-review').glob('*.json'))
        self.assertEqual(len(archive),1)
        self.assertEqual(json.loads(archive[0].read_text())[0]['proposed_xml'],self.prior['proposed_xml'])
        self.assertEqual(json.loads(review.revisions_manifest().read_text())['completed_second_pass'],1)
        self.assertEqual(len(list((self.root/'batches').glob('*/*.json'))),1)
    def test_owner_lookup_never_reuses_mutated_returned_rows(self):
        keys={('CODE','ARTICLE')}
        _,files=review.batch_owners(keys)
        files[self.path][0]['reason']='Only changed in caller memory'
        _,fresh=review.batch_owners(keys)
        self.assertEqual(fresh[self.path][0]['reason'],self.row['reason'])
    def test_owner_lookup_invalidates_index_when_rows_move(self):
        keys={('CODE','ARTICLE')}
        review.batch_owners(keys)
        other=self.row|{'source_id':'OTHER'}
        self.path.write_text(json.dumps([other,self.row]))
        owners,_=review.batch_owners(keys)
        self.assertEqual(owners[('CODE','ARTICLE')],(self.path,1))
        self.path.write_text(json.dumps([self.row,self.row]))
        with self.assertRaisesRegex(ValueError,'Duplicate active batch owner'):
            review.batch_owners(keys)
    def test_refuses_to_overwrite_an_intervening_author(self):
        before=self.path.read_text()
        self.db.execute('UPDATE drafts SET proposed_xml=?',('<p>Une autre décision de l’auteur.</p>',));self.db.commit()
        with self.assertRaisesRegex(ValueError,'changed draft'):review.commit([self.new],self.expected)
        self.assertEqual(self.path.read_text(),before)
        self.assertFalse((self.root/'revisions/radical-review').exists())
    def test_acceptance_is_finalized_before_unlocking(self):
        @contextlib.contextmanager
        def lock():
            yield
            report=json.loads(review.revisions_manifest().read_text())
            self.assertEqual(report['completed_second_pass'],1)
        with patch.object(review,'writer_lock',lock),contextlib.redirect_stdout(io.StringIO()):
            review.commit([self.new],self.expected)
    def test_failed_full_validation_never_marks_review_complete(self):
        before=review.revisions_manifest().read_bytes()
        with patch.object(review,'register_locked',side_effect=ValueError('full validation rejected')):
            with self.assertRaisesRegex(ValueError,'full validation rejected'):
                review.commit([self.new],self.expected)
        self.assertEqual(review.revisions_manifest().read_bytes(),before)
    def test_failed_global_validation_restores_mirrors_and_allows_safe_retry(self):
        batch=self.path.read_bytes();registry=(self.root/'registered-batches.json').read_bytes()
        with patch.object(review,'register_locked',side_effect=ValueError('full validation rejected')):
            with self.assertRaisesRegex(ValueError,'full validation rejected'):review.commit([self.new.copy()],self.expected)
        self.assertEqual(self.path.read_bytes(),batch)
        self.assertEqual((self.root/'registered-batches.json').read_bytes(),registry)
        self.assertEqual(self.db.execute('SELECT proposed_xml FROM drafts').fetchone()[0],self.prior['proposed_xml'])
        with contextlib.redirect_stdout(io.StringIO()):review.commit([self.new.copy()],self.expected)
        self.assertEqual(json.loads(review.revisions_manifest().read_text())['completed_second_pass'],1)
    def test_post_commit_failure_does_not_restore_old_files_over_new_database(self):
        def committed_then_failed(db,*args):
            db.execute('UPDATE drafts SET proposed_xml=?',(self.new['proposed_xml'],));db.commit()
            raise OSError('receipt failed after database commit')
        with patch.object(review,'register_locked',side_effect=committed_then_failed):
            with self.assertRaisesRegex(OSError,'receipt failed'):review.commit([self.new.copy()],self.expected)
        self.assertEqual(json.loads(self.path.read_text())[0]['proposed_xml'],self.new['proposed_xml'])
        self.assertEqual(json.loads(review.revisions_manifest().read_text())['prior_articles'][0]['review_status'],'pending')
    def test_refuses_a_changed_official_source_before_editing_batches(self):
        before=self.path.read_text()
        self.db.execute('UPDATE articles SET source_sha256=?',('0'*64,));self.db.commit()
        with self.assertRaisesRegex(ValueError,'canonical source'):review.commit([self.new],self.expected)
        self.assertEqual(self.path.read_text(),before)
    def test_historical_jobs_check_each_database_field_without_a_batch_hash(self):
        self.assertNotIn('batch_row_sha256',self.expected[0]['previous_draft'])
        for field,value in [('status','retained_unchanged'),('reason','Motif récent.'),('review_notes','Réserve récente.')]:
            with self.subTest(field=field):
                self.db.execute('UPDATE drafts SET '+field+'=?',(value,));self.db.commit()
                self.assert_refused_without_writes(self.expected,'changed draft')
                self.db.execute('UPDATE drafts SET '+field+'=?',(self.prior[field],));self.db.commit()
    def test_capture_pins_complete_metadata_in_one_locked_read_transaction(self):
        batch=self.row|{'substantive_impact':{'effects':[{'kind':'obligation_removed'}]},'reference_coherence':{'targets':['other']}}
        self.path.write_text(json.dumps([batch]))
        held=[];observed=[];connect=review.sqlite3.connect;owners=review.batch_owners
        @contextlib.contextmanager
        def lock():
            self.assertFalse(held)
            held.append(True)
            try:yield
            finally:held.clear()
        def connect_locked(path,**kwargs):
            self.assertTrue(held)
            self.assertTrue(path.endswith('?mode=ro'))
            self.assertTrue(kwargs['uri'])
            db=connect(path,**kwargs)
            def trace(statement):
                observed.append((statement,bool(held)))
            db.set_trace_callback(trace)
            return db
        def owners_locked(keys):
            self.assertTrue(held)
            return owners(keys)
        with patch.object(review,'writer_lock',lock),patch.object(review.sqlite3,'connect',side_effect=connect_locked),patch.object(review,'batch_owners',side_effect=owners_locked):
            expected=self.captured_expected()
        previous=expected[0]['previous_draft']
        self.assertEqual(previous['batch_row_sha256'],review.batch_row_sha256(batch))
        self.assertEqual(review.draft_values(previous),review.draft_values(self.prior))
        self.assertEqual(previous['proposed_sha256'],self.prior['proposed_sha256'])
        self.assertEqual(observed[0],('BEGIN',True))
        self.assertTrue(any(sql.startswith('SELECT ') for sql,_ in observed))
        self.assertTrue(all(locked for _,locked in observed))
    def test_build_does_not_capture_divergent_batch_and_database_fields(self):
        self.path.write_text(json.dumps([self.row|{'reason':'Motif non encore enregistré.'}]))
        self.assertEqual(self.captured_expected(),[])
        changed=json.loads(review.revisions_manifest().read_text())['changed_since_inventory']
        self.assertEqual(len(changed),1)
        self.assertIn('before-images differ',changed[0]['reason'])
    def test_metadata_only_batch_changes_are_refused(self):
        base=self.row|{'substantive_impact':{'effects':[{'kind':'obligation_removed'}]},'substantive_impact_certificate':{'sha':'old'},'reference_coherence':{'targets':['old']}}
        self.path.write_text(json.dumps([base]))
        expected=self.captured_expected()
        for field,value in [('substantive_impact',{'effects':[{'kind':'coordination'}]}),('substantive_impact_certificate',{'sha':'new'}),('reference_coherence',{'targets':['new']}),('new_metadata',{'reviewer':'another'})]:
            with self.subTest(field=field):
                self.path.write_text(json.dumps([base|{field:value}]))
                self.assert_refused_without_writes(expected,'changed active batch row')
                self.assertEqual(self.db.execute('SELECT proposed_xml,reason FROM drafts').fetchone(),(self.row['proposed_xml'],self.row['reason']))
    def test_batch_hash_ignores_layout_and_key_order_and_other_rows(self):
        expected=self.captured_expected()
        unrelated=self.row|{'source_id':'UNRELATED','reason':'Une justification indépendante.'}
        self.path.write_text(json.dumps([dict(reversed(list(self.row.items()))),unrelated],indent=4))
        with patch.object(review,'register_locked') as registered,contextlib.redirect_stdout(io.StringIO()):
            review.commit([self.new],expected)
        registered.assert_called_once()
        self.assertEqual(json.loads(self.path.read_text())[1],unrelated)
    def test_captured_batch_owner_disappearance_is_refused(self):
        expected=self.captured_expected()
        self.path.unlink()
        self.assert_refused_without_writes(expected,'changed active batch row')
    def test_captured_legacy_absence_cannot_adopt_a_new_batch_owner(self):
        self.path.unlink()
        expected=self.captured_expected()
        self.assertIn('batch_row_sha256',expected[0]['previous_draft'])
        self.assertIsNone(expected[0]['previous_draft']['batch_row_sha256'])
        self.path.write_text(json.dumps([self.row]))
        self.assert_refused_without_writes(expected,'changed active batch row')
    def test_duplicate_active_batch_owners_are_rejected(self):
        (self.folder/'002.json').write_text(json.dumps([self.row]))
        with self.assertRaisesRegex(ValueError,'Duplicate active batch owner'):self.captured_expected()
        self.assert_refused_without_writes(self.expected,'Duplicate active batch owner')
    def test_fresh_batch_guard_is_held_through_registration(self):
        expected=self.captured_expected();held=[]
        @contextlib.contextmanager
        def lock():
            self.assertFalse(held)
            held.append(True)
            try:yield
            finally:held.clear()
        def register(*args):self.assertTrue(held)
        with patch.object(review,'writer_lock',lock),patch.object(review,'register_locked',side_effect=register) as registered,contextlib.redirect_stdout(io.StringIO()):
            review.commit([self.new],expected)
        registered.assert_called_once()
    def test_second_built_job_cannot_overwrite_a_metadata_only_registration(self):
        first=self.captured_expected();second=self.captured_expected()
        # All five DB values stay identical, but a newer audit is now canonical.
        updated=self.row|{'review_provenance':{'reviewer':'newer independent reviewer'}}
        with contextlib.redirect_stdout(io.StringIO()):review.commit([updated],first)
        self.assertEqual(self.db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts').fetchone(),review.draft_values(self.row))
        before=self.path.read_bytes()
        registry=(self.root/'registered-batches.json').read_bytes()
        archive={p.name:p.read_bytes() for p in (self.root/'revisions/radical-review').glob('*.json')}
        with self.assertRaisesRegex(ValueError,'changed active batch row'):review.commit([self.new],second)
        self.assertEqual(self.path.read_bytes(),before)
        self.assertEqual((self.root/'registered-batches.json').read_bytes(),registry)
        self.assertEqual({p.name:p.read_bytes() for p in (self.root/'revisions/radical-review').glob('*.json')},archive)

if __name__=='__main__':unittest.main()
