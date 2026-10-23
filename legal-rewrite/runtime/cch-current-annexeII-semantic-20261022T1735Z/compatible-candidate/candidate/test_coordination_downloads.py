import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

from coordination_downloads import load, add_to_archive, unique_records, document


class CoordinationIntegrity(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.folder = self.root/'is-distribution'
        self.folder.mkdir()
        source = '<p>La contribution est annuelle.</p>'
        self.item = {'title': 'Coordination législative', 'outside_code_inventory': True,
                     'articles': [{'number': '48', 'title': 'Article 48',
                     'source_url': 'https://www.legifrance.gouv.fr/loi',
                     'source_date': '2026-10-18', 'source_xml': source,
                     'source_sha256': hashlib.sha256(source.encode()).hexdigest(),
                     'proposed_xml': '<p>La contribution ne concerne plus les faits nouveaux.</p>',
                     'reason': 'Suppression prospective.', 'review_notes': 'Droits antérieurs conservés.'}]}

    def read(self):
        (self.folder/'manifest.json').write_text(json.dumps(self.item))
        return load(self.root)

    def test_companion_stays_outside_code_inventory(self):
        self.assertTrue(self.read()[0]['outside_code_inventory'])
        self.item['outside_code_inventory'] = False
        with self.assertRaisesRegex(ValueError, 'outside the code inventory'):
            self.read()

    def test_source_tampering_is_rejected(self):
        self.item['articles'][0]['source_xml'] += '<p>Autre règle.</p>'
        with self.assertRaisesRegex(ValueError, 'fingerprint mismatch'):
            self.read()

    def test_active_content_is_rejected(self):
        self.item['articles'][0]['proposed_xml'] = '<script>alert(1)</script>'
        with self.assertRaisesRegex(ValueError, 'Unexpected HTML tag'):
            self.read()

    def test_copied_source_is_not_a_rewrite(self):
        self.item['articles'][0]['proposed_xml'] = self.item['articles'][0]['source_xml']
        with self.assertRaisesRegex(ValueError, 'distinct proposal'):
            self.read()

    def test_shared_companion_has_one_global_record_and_two_offline_copies(self):
        self.item['groups'] = ['impots', 'urbanisme']
        article = self.item['articles'][0]
        article.update(valid_from='2027-01-01', valid_until='2999-01-01',
                       source_state='VIGUEUR_DIFF', source_notes_xml='<p>Entrée différée.</p>')
        items = self.read()
        records = []
        payloads = []
        for group in ['impots', 'urbanisme']:
            buffer = io.BytesIO()
            with zipfile.ZipFile(buffer, 'w') as archive:
                related = add_to_archive(archive, self.root, group, items)
            with zipfile.ZipFile(buffer) as archive:
                payloads.append(archive.read(related[0]['archive_html']))
            records.extend(related)
        self.assertEqual(payloads[0], payloads[1])
        self.assertIn(b'2027-01-01', payloads[0])
        self.assertIn('Entrée différée.'.encode(), payloads[0])
        self.assertEqual(len(unique_records(records)), 1)
        self.assertEqual(sum(r['articles'] for r in unique_records(records)), 1)
        with self.assertRaisesRegex(ValueError, 'Conflicting coordination'):
            unique_records([records[0], records[1] | {'sha256': 'different'}])

    def test_unsafe_source_notes_are_rejected(self):
        self.item['articles'][0]['source_notes_xml'] = '<script>alert(1)</script>'
        with self.assertRaisesRegex(ValueError, 'Unexpected HTML tag'):
            self.read()

    def test_official_table_source_is_preserved_and_rendered_safely(self):
        article = self.item['articles'][0]
        source = '<table border="1" onclick="alert(1)"><tr><td align="left">Texte complet</td></tr></table>'
        article.update(source_xml=source, source_sha256=hashlib.sha256(source.encode()).hexdigest())
        item = self.read()[0]
        self.assertEqual(item['articles'][0]['source_xml'], source)
        rendered = document(item)
        self.assertIn('<table><tr><td>Texte complet</td></tr></table>', rendered)
        self.assertNotIn('onclick', rendered)

    def test_official_note_line_break_attribute_is_preserved_as_data_only(self):
        notes = '<p>Note officielle.<br clear="none" /></p>'
        self.item['articles'][0]['source_notes_xml'] = notes
        item = self.read()[0]
        self.assertEqual(item['articles'][0]['source_notes_xml'], notes)
        self.assertIn('<p>Note officielle.<br></p>', document(item))
        self.assertNotIn('clear=', document(item))

    def test_future_source_is_visible_without_replacing_or_counting_as_a_proposal(self):
        source = '<p>Ancien barème différé.</p>'
        self.item['supporting_sources'] = [{
            'title': 'Article futur', 'source_date': '2026-10-19',
            'source_url': 'https://www.legifrance.gouv.fr/article-futur',
            'source_xml': source, 'source_sha256': hashlib.sha256(source.encode()).hexdigest(),
            'source_notes_xml': '<p>Ancienne note de calendrier.</p>',
            'valid_from': '2030-01-01', 'valid_until': '2999-01-01',
            'source_state': 'VIGUEUR_DIFF', 'status': 'source_reference_only',
            'proposed_xml': None}]
        item = self.read()[0]
        rendered = document(item)
        self.assertIn(source, rendered)
        self.assertIn('Ancienne note de calendrier.', rendered)
        self.assertIn('2030-01-01', rendered)
        self.assertIn(self.item['articles'][0]['proposed_xml'], rendered)
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, 'w') as archive:
            records = add_to_archive(archive, self.root, 'impots', [item])
        self.assertEqual(records[0]['articles'], 1)
        self.item['supporting_sources'][0]['proposed_xml'] = '<p>Fausse proposition.</p>'
        with self.assertRaisesRegex(ValueError, 'cannot count'):
            self.read()

    def test_future_source_tampering_is_rejected(self):
        self.item['supporting_sources'] = [{
            'title': 'Article futur', 'source_date': '2026-10-19',
            'source_url': 'https://www.legifrance.gouv.fr/article-futur',
            'source_xml': '<p>Source altérée.</p>',
            'source_sha256': hashlib.sha256(b'other source').hexdigest(),
            'status': 'source_reference_only', 'proposed_xml': None}]
        with self.assertRaisesRegex(ValueError, 'Supporting source fingerprint mismatch'):
            self.read()


if __name__ == '__main__':
    unittest.main()
