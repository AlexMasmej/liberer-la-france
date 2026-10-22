import json
from pathlib import Path
import tempfile
import unittest

from sru_context import contexts, priority


class SRUContext(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)/'sru-integral'
        self.root.mkdir()
        self.original = [{'number': '14', 'source_url': 'https://www.legifrance.gouv.fr/jorf/test',
                          'text': 'Tout le texte initial, avec sa fin et ses exceptions.'}]
        (self.root/'original-articles.json').write_text(json.dumps(self.original))

    def write(self, name, value):
        p = self.root/name
        p.parent.mkdir(exist_ok=True)
        p.write_text(json.dumps(value))

    def test_unverified_or_missing_id_does_not_match_by_number(self):
        self.write('habitat-inventory.json', {'articles': [{'sru_article': '14', 'current_review_targets': [
            {'number': 'L115-4', 'code_id': 'CODE', 'source_id': 'UNKNOWN', 'current_slot_verified': False},
            {'number': 'L115-4', 'code_id': 'CODE', 'current_slot_verified': True}]}]})
        self.assertEqual(contexts(self.root), {})

    def test_two_documentary_routes_keep_one_complete_origin_and_warn(self):
        self.write('habitat-inventory.json', {'articles': [{'sru_article': '14', 'current_review_targets': [
            {'code_id': 'CODE', 'source_id': 'CURRENT', 'current_slot_verified': True}]}]})
        self.write('urbanisme-evidence/canonical-lineage.json', {'records': [{'original_article': '14',
            'canonical_targets': [{'version_id': 'HISTORICAL', 'original_target_number': 'L111-5-3',
                'current_descendants': [{'code_id': 'CODE', 'source_id': 'CURRENT'}]}]}]})
        origins = contexts(self.root)[('CODE', 'CURRENT')]
        self.assertEqual(len(origins), 1)
        self.assertEqual(origins[0]['initial_text'], self.original[0]['text'])
        self.assertEqual(len(origins[0]['documentary_evidence']), 2)
        self.assertTrue(all(e['warning'] for e in origins[0]['documentary_evidence']))
        self.assertNotIn(('CODE', 'L115-4'), contexts(self.root))

    def test_priority_does_not_mark_a_job_complete(self):
        ordinary = ('code', 1, [{'source_id': 'A'}])
        related = ('code', 2, [{'source_id': 'B', 'sru_context': [{'original_article': '14'}]}])
        self.assertEqual(sorted([ordinary, related], key=priority), [related, ordinary])
        self.assertNotIn('status', related[2][0])


if __name__ == '__main__':
    unittest.main()
