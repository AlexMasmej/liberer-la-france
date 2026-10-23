from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase,main

from initiative_notice import NOTICE,MARKER,annotate,apply_to_sites
from build_downloads import document


class IndependenceNotice(TestCase):
    def test_notice_stays_outside_legal_article_and_preserves_existing_markup(self):
        article='<article><h2>Article 1</h2><p>Texte &amp; renvoi.</p></article>'
        original='<html><body>'+article+'<footer>Source officielle</footer></body></html>'
        result=annotate(original)
        self.assertIn(article,result)
        self.assertLess(result.index('</article>'),result.index(MARKER))
        self.assertLess(result.index('<footer>'),result.index(MARKER))
        self.assertIn('Source officielle',result)

    def test_repeat_build_does_not_duplicate_or_rewrite_the_notice(self):
        once=annotate('<html><body><main>Projet</main></body></html>')
        self.assertEqual(annotate(once),once)
        self.assertEqual(once.count(NOTICE),1)

    def test_legacy_html_without_explicit_body_gets_a_standalone_footer(self):
        original='<html><title>Coordination</title><article>Article entier</article></html>'
        result=annotate(original)
        self.assertIn('<article>Article entier</article>',result)
        self.assertLess(result.index('</article>'),result.index('<footer>'))
        self.assertTrue(result.endswith('</footer></html>'))

    def test_nested_public_pages_are_covered_without_touching_other_files(self):
        with TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'corpus').mkdir();(root/'.vercel').mkdir()
            for path in [root/'index.html',root/'corpus/index.html',root/'.vercel/private.html']:
                path.write_text('<html><body>Page</body></html>')
            untouched=root/'articles.json';untouched.write_text('{"source":"intacte"}')
            self.assertEqual(len(apply_to_sites([root])),2)
            self.assertEqual(apply_to_sites([root]),[])
            self.assertNotIn(NOTICE,(root/'.vercel/private.html').read_text())
            self.assertEqual(untouched.read_text(),'{"source":"intacte"}')

    def test_download_document_keeps_the_source_and_proposal_intact(self):
        source='<p>Source entière &amp; conservée.</p>'
        proposal='<p>Proposition entière.</p>'
        record={'proposed_xml':proposal,'status':'rewrite_draft','path':['Partie législative'],
                'source_id':'SOURCE1','number':'1','source_url':'https://www.legifrance.gouv.fr/',
                'valid_from':'2026-01-01','valid_until':'2999-01-01','source_state':'VIGUEUR',
                'source_xml':source,'source_notes_xml':'','reason':'Réduction documentée','review_notes':''}
        for working,expected in [(False,source),(True,proposal)]:
            result=document({'title':'Code'},[record],working,'2026-10-18')
            self.assertIn(expected,result)
            self.assertLess(result.index('</article>'),result.index(MARKER))
            self.assertEqual(result.count(NOTICE),1)


if __name__=='__main__':main()
