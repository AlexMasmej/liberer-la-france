from pathlib import Path
import copy,json,sqlite3,tempfile,unittest
from unittest.mock import patch
import reference_coherence as audit

class ReferenceChecks(unittest.TestCase):
    def setUp(self):
        self.db=sqlite3.connect(':memory:');self.addCleanup(self.db.close)
        self.db.executescript('CREATE TABLE articles(code_id,id,number,source_sha256,content_xml); CREATE TABLE drafts(code_id,source_id,source_sha256,proposed_xml); CREATE TABLE documents(code_id,id,kind,xml);')
        self.catalog={}
        for identifier,number in [('A','L10-1'),('B','L20-1'),('C','L20-2'),('D','L20-3')]:
            row={'code_id':'CODE','source_id':identifier,'number':number,'source_sha256':'s'+identifier};self.catalog[audit.key(row)]=row
            self.db.execute('INSERT INTO articles VALUES(?,?,?,?,?)',('CODE',identifier,number,'s'+identifier,'<p>Règle officielle '+identifier+'</p>'))
        self.article={'code_id':'CODE','source_id':'A','number':'L10-1','source_xml':'<p>Le renvoi à L20-1 conserve la garantie.</p>'}
        self.body='<p>La règle de L20-1 demeure applicable, sous sa transition.</p>'
    def snapshot(self,article=None):return audit.capture(self.db,[article or self.article],catalog=self.catalog)
    def row(self,snapshot=None):
        snap=snapshot or self.snapshot();row=self.article|{'proposed_xml':self.body}
        row['reference_checks']=[{'target_key':k,'view_sha256':v['view_sha256'],'assessment':'Le renvoi vise la garantie intégrale de la cible et conserve sa période transitoire ; aucune condition nouvelle de rupture ni perte de droit ne résulte de cette coordination.'} for k,v in snap['targets'].items()]
        return row
    def test_full_target_body_and_notes_are_frozen(self):
        self.db.execute('INSERT INTO documents VALUES(?,?,?,?)',('CODE','B','ARTICLE','<ARTICLE><NOTA><CONTENU><p>Note intégrale.</p></CONTENU></NOTA></ARTICLE>'))
        snap=self.snapshot();self.assertEqual(snap['targets']['CODE|B']['source_xml'],'<p>Règle officielle B</p>');self.assertIn('Note intégrale',snap['targets']['CODE|B']['source_notes_xml'])
    def test_official_target_is_invalidated_when_rewritten(self):
        snap=self.snapshot();self.db.execute('INSERT INTO drafts VALUES(?,?,?,?)',('CODE','B','sB','<p>Nouvelle règle B.</p>'))
        with self.assertRaisesRegex(ValueError,'changed'):audit.check_guards(self.db,snap)
    def test_proposed_target_is_invalidated_when_changed(self):
        self.db.execute('INSERT INTO drafts VALUES(?,?,?,?)',('CODE','B','sB','<p>Proposition B.</p>'));snap=self.snapshot();self.db.execute("UPDATE drafts SET proposed_xml='<p>Autre règle.</p>'")
        with self.assertRaisesRegex(ValueError,'changed'):audit.check_guards(self.db,snap)
    def test_canonical_target_version_change_is_rejected(self):
        snap=self.snapshot();self.db.execute("UPDATE articles SET source_sha256='new' WHERE id='B'")
        with self.assertRaisesRegex(ValueError,'changed'):audit.check_guards(self.db,snap)
    def test_mismatched_source_and_target_proposal_is_rejected(self):
        self.db.execute('INSERT INTO drafts VALUES(?,?,?,?)',('CODE','B','wrong','<p>B.</p>'))
        with self.assertRaisesRegex(ValueError,'different canonical'):self.snapshot()
    def test_all_references_require_specific_assessments(self):
        snap=self.snapshot();row=self.row(snap);audit.accept_checks([row],[self.article],snap,self.catalog);self.assertFalse(row['reference_coherence']['semantic_review_by_jurist'])
        for invalid in [[],[row['reference_checks'][0]|{'assessment':'Vérifié.'}],[row['reference_checks'][0]|{'view_sha256':'stale'}]]:
            with self.subTest(invalid=invalid),self.assertRaises(ValueError):audit.accept_checks([self.row(snap)|{'reference_checks':invalid}],[self.article],snap,self.catalog)
    def test_duplicate_assessments_are_rejected(self):
        snap=self.snapshot();row=self.row(snap);row['reference_checks']*=2
        with self.assertRaisesRegex(ValueError,'Duplicate'):audit.accept_checks([row],[self.article],snap,self.catalog)
    def test_new_reference_requires_its_full_target(self):
        snap=self.snapshot();row=self.row(snap);row['proposed_xml']='<p>Les articles L20-1 et L20-2 s’appliquent.</p>'
        with self.assertRaisesRegex(ValueError,'complete target'):audit.accept_checks([row],[self.article],snap,self.catalog)
    def test_new_reference_can_be_supplied_on_retry(self):
        row=self.row();row['proposed_xml']='<p>Les articles L20-1 et L20-2 s’appliquent.</p>';snap=audit.capture(self.db,[self.article],[row],self.catalog);row=self.row(snap)|{'proposed_xml':row['proposed_xml']};audit.accept_checks([row],[self.article],snap,self.catalog)
        self.assertEqual(set(row['reference_coherence']['targets']),{'CODE|B','CODE|C'})
    def test_referrer_body_change_invalidates_certificate(self):
        snap=self.snapshot();row=self.row(snap);audit.accept_checks([row],[self.article],snap,self.catalog);cert=row['reference_coherence'];self.assertTrue(audit.certificate_current(self.db,self.article,self.body,cert,self.catalog));self.assertFalse(audit.certificate_current(self.db,self.article,self.body+'<p>Changement.</p>',cert,self.catalog))
    def test_self_reference_does_not_create_a_permanently_stale_certificate(self):
        article=self.article|{'source_xml':'<p>Le présent article L10-1 s’applique.</p>'};self.assertEqual(audit.requirements(article,catalog=self.catalog),set())
    def test_only_same_family_ranges_are_expanded(self):
        self.assertEqual(audit.token_refs('articles L20-1 à L20-3'),{'L20-1','L20-2','L20-3'});self.assertNotIn('L20-2',audit.token_refs('articles L20-1 à L30-3'))
    def test_removed_reference_still_requires_review_of_its_transition(self):
        snap=self.snapshot();row=self.row(snap)|{'proposed_xml':'<p>Le renvoi est remplacé par une règle autonome complète.</p>'};audit.accept_checks([row],[self.article],snap,self.catalog);self.assertIn('CODE|B',row['reference_coherence']['targets'])
    def test_other_rows_in_batch_can_invalidate_certificate_after_commit(self):
        snap=self.snapshot();row=self.row(snap);audit.accept_checks([row],[self.article],snap,self.catalog);self.db.execute('INSERT INTO drafts VALUES(?,?,?,?)',('CODE','B','sB','<p>B également réécrit dans le lot.</p>'));self.assertFalse(audit.certificate_current(self.db,self.article,self.body,row['reference_coherence'],self.catalog))
    def test_dila_outgoing_numeric_link_is_included_but_incoming_is_not(self):
        article=self.article|{'code_id':'LEGITEXT000006069577','source_id':'T','source_xml':'<p>Texte sans numéro littéral.</p>'};self.db.execute('INSERT INTO documents VALUES(?,?,?,?)',(article['code_id'],'T','ARTICLE','<ARTICLE><LIENS><LIEN sens="source" typelien="CITATION" cidtexte="CODE" id="B" num="L20-1"/><LIEN sens="cible" typelien="CITATION" cidtexte="CODE" id="C" num="L20-2"/></LIENS></ARTICLE>'));self.assertEqual(audit.requirements(article,catalog=self.catalog,db=self.db),{'CODE|B'})
    def test_new_source_cannot_disappear_from_guard_set(self):
        snap=self.snapshot();row=self.row(snap);audit.accept_checks([row],[self.article],snap,self.catalog);self.db.execute("DELETE FROM articles WHERE id='B'")
        with self.assertRaisesRegex(ValueError,'Missing canonical'):audit.certificate_current(self.db,self.article,self.body,row['reference_coherence'],self.catalog)

if __name__=='__main__':unittest.main()
