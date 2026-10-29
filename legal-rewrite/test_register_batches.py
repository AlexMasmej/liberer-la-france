import hashlib,json,tempfile,unittest
from unittest.mock import patch
from pathlib import Path
import register_batches as mod
from ingest import open_db

class BatchRegistrationTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name);self.old_here=mod.HERE;mod.HERE=self.root
        self.db=open_db(self.root/'test.sqlite');self.folder=self.root/'batches/worker';self.folder.mkdir(parents=True)
        self.body='<p>Le délai est de trois mois.</p>';self.sha=hashlib.sha256(self.body.encode()).hexdigest()
        self.db.execute('INSERT INTO articles VALUES(?,?,?,?,?,?,?,?,?,?)',('CODE','ARTICLE','L1','2020-01-01','2999-01-01','VIGUEUR',self.body,'Le délai est de trois mois.',self.sha,'archive.tar.gz'));self.db.commit()
        self.row={'code_id':'CODE','source_id':'ARTICLE','source_sha256':self.sha,'number':'L1','proposed_xml':'<p>Le délai applicable est fixé à trois mois.</p>','reason':'Clarifie le délai sans changer sa durée.','review_notes':'Contrôler le point de départ dans les articles liés.'}
    def tearDown(self):
        self.db.close();mod.HERE=self.old_here;self.tmp.cleanup()
    def write(self,row=None):
        (self.folder/'001.json').write_text(json.dumps([row or self.row]))
    def test_registers_exact_source_and_is_idempotent(self):
        self.write();mod.register(self.db,self.root/'batches',True);mod.register(self.db,self.root/'batches',True)
        self.assertEqual(self.db.execute('SELECT count(*) FROM drafts').fetchone()[0],1)
        self.assertEqual(self.db.execute('SELECT source_xml FROM draft_sources').fetchone()[0],self.body)
    def test_rejects_unchanged_source(self):
        self.write(self.row|{'proposed_xml':self.body})
        with self.assertRaisesRegex(ValueError,'Unchanged'):mod.validate_batches(self.db,self.root/'batches')
    def test_rejects_wrong_source_version(self):
        self.write(self.row|{'source_sha256':'0'*64})
        with self.assertRaisesRegex(ValueError,'mismatch'):mod.validate_batches(self.db,self.root/'batches')
    def test_rejects_companion_manifest_changed_during_validation(self):
        self.write()
        with patch.object(mod,'load_companions',side_effect=[{}, {('CODE','ARTICLE'):{'media':[]}}]):
            with self.assertRaisesRegex(ValueError,'companions changed'):
                mod.validate_batches(self.db,self.root/'batches')
    def test_rechecks_companion_hashes_before_returning_success(self):
        self.write()
        with patch.object(mod,'load_companions',side_effect=[{}, ValueError('Companion hash mismatch')]):
            with self.assertRaisesRegex(ValueError,'hash mismatch'):
                mod.validate_batches(self.db,self.root/'batches')
    def test_preverified_media_cannot_escape_media_directory(self):
        parser=mod.Markup(verified_media={'other/image.png'})
        with self.assertRaisesRegex(ValueError,'Only registered local'):
            parser.feed('<img src="other/image.png" alt="Formula">')
    def test_preverified_media_still_checks_file_presence(self):
        parser=mod.Markup(verified_media={'media/not-present.png'})
        with self.assertRaisesRegex(ValueError,'Missing or unsafe'):
            parser.feed('<img src="media/not-present.png" alt="Formula">')
    def test_rejects_duplicate_article(self):
        self.write();(self.folder/'002.json').write_text(json.dumps([self.row]))
        with self.assertRaisesRegex(ValueError,'Duplicate'):mod.validate_batches(self.db,self.root/'batches')
    def test_rejects_lost_source_table(self):
        self.db.execute('UPDATE articles SET content_xml=?',('<table><tr><td>Un montant</td></tr></table>',));self.db.commit();self.write()
        with self.assertRaisesRegex(ValueError,'table missing'):mod.validate_batches(self.db,self.root/'batches')
    def repeal(self):
        (self.root/'policy-coordinations.json').write_text(json.dumps({'editorial_direction_2026_10_19':['Suppression expressément demandée.']}))
        return self.row|{'proposed_xml':"<p>Le présent article est abrogé à compter de l'entrée en vigueur de la présente loi. Il reste applicable aux faits générateurs antérieurs.</p>",'change_type':'full_repeal','repeal_policy_id':'editorial_direction_2026_10_19','repeal_scope':'Supprime entièrement le barème et les obligations déclaratives de cet article pour les faits futurs.'}
    def test_authorized_repeal_keeps_source_evidence_without_reprinting_table(self):
        original='<p>Barème imposé.</p><table><tr><td>10 %</td></tr></table>'
        self.db.execute('UPDATE articles SET content_xml=?',(original,));self.db.commit();self.write(self.repeal())
        mod.register(self.db,self.root/'batches',True)
        self.assertEqual(self.db.execute('SELECT source_xml FROM draft_sources').fetchone()[0],original)
        self.assertNotIn('<table>',self.db.execute('SELECT proposed_xml FROM drafts').fetchone()[0])
    def test_repeal_metadata_cannot_hide_an_incomplete_retained_rule(self):
        row=self.repeal()|{'proposed_xml':'<p>Le barème sera simplifié ultérieurement.</p>'};self.write(row)
        with self.assertRaisesRegex(ValueError,'operative'):mod.validate_batches(self.db,self.root/'batches')
    def test_repeal_requires_authorized_policy(self):
        row=self.repeal()|{'repeal_policy_id':'invented'};self.write(row)
        with self.assertRaisesRegex(ValueError,'explicit author policy'):mod.validate_batches(self.db,self.root/'batches')
    def test_partial_reduction_requires_explicit_inventory_of_removed_rules(self):
        row=self.repeal()|{'change_type':'normative_reduction','reform_policy_id':'editorial_direction_2026_10_19','proposed_xml':'<p>Une déclaration unique remplace les formalités précédentes.</p>'}
        self.write(row)
        with self.assertRaisesRegex(ValueError,'identify the removed'):mod.validate_batches(self.db,self.root/'batches')
        self.db.execute('UPDATE articles SET content_xml=?',('<p>Déclaration obligatoire.</p><table><tr><td>Tableau de seuils supprimé</td></tr></table>',));self.db.commit()
        self.write(row|{'removed_provisions':['Supprime entièrement le barème conditionnant la seconde déclaration devenue redondante.']})
        records,diagnostics,_=mod.validate_batches(self.db,self.root/'batches')
        self.assertEqual(len(records),1)
        self.assertTrue(any(d['check']=='explicit_normative_reduction' for d in diagnostics))
    def test_rejects_unsafe_or_incomplete_markup(self):
        for body in ['<p>Texte<script>alert(1)</script></p>','<p onclick="x()">Texte</p>','<p>Texte','<p>[à compléter]</p>']:
            with self.subTest(body=body):
                self.write(self.row|{'proposed_xml':body})
                with self.assertRaises(ValueError):mod.validate_batches(self.db,self.root/'batches')
    def test_protects_existing_independent_draft(self):
        self.db.execute('INSERT INTO drafts VALUES(?,?,?,?,?,?,?)',('CODE','ARTICLE',self.sha,'rewrite_draft','<p>Un brouillon antérieur.</p>','raison','notes'));self.db.commit();self.write()
        with self.assertRaisesRegex(ValueError,'overwrite'):mod.validate_batches(self.db,self.root/'batches')
    def test_allows_traceable_revision_of_own_registered_batch(self):
        self.write();mod.register(self.db,self.root/'batches',True)
        updated=self.row|{'proposed_xml':'<p>Le délai est fixé à trois mois, sans autre modification.</p>'};self.write(updated)
        mod.register(self.db,self.root/'batches',True)
        self.assertEqual(self.db.execute('SELECT proposed_xml FROM drafts').fetchone()[0],updated['proposed_xml'])

if __name__=='__main__':unittest.main()
