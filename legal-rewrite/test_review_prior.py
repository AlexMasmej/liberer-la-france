import contextlib,hashlib,io,json,tempfile,unittest
from pathlib import Path
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
    def test_preserves_before_image_and_canonical_source(self):
        with contextlib.redirect_stdout(io.StringIO()):review.commit([self.new],self.expected)
        self.assertEqual(self.db.execute('SELECT content_xml FROM articles').fetchone()[0],self.source)
        self.assertEqual(self.db.execute('SELECT proposed_xml FROM drafts').fetchone()[0],self.new['proposed_xml'])
        archive=list((self.root/'revisions/radical-review').glob('*.json'))
        self.assertEqual(len(archive),1)
        self.assertEqual(json.loads(archive[0].read_text())[0]['proposed_xml'],self.prior['proposed_xml'])
        self.assertEqual(json.loads(review.revisions_manifest().read_text())['completed_second_pass'],1)
        self.assertEqual(len(list((self.root/'batches').glob('*/*.json'))),1)
    def test_refuses_to_overwrite_an_intervening_author(self):
        before=self.path.read_text()
        self.db.execute('UPDATE drafts SET proposed_xml=?',('<p>Une autre décision de l’auteur.</p>',));self.db.commit()
        with self.assertRaisesRegex(ValueError,'changed draft'):review.commit([self.new],self.expected)
        self.assertEqual(self.path.read_text(),before)
        self.assertFalse((self.root/'revisions/radical-review').exists())
    def test_refuses_a_changed_official_source_before_editing_batches(self):
        before=self.path.read_text()
        self.db.execute('UPDATE articles SET source_sha256=?',('0'*64,));self.db.commit()
        with self.assertRaisesRegex(ValueError,'canonical source'):review.commit([self.new],self.expected)
        self.assertEqual(self.path.read_text(),before)

if __name__=='__main__':unittest.main()
