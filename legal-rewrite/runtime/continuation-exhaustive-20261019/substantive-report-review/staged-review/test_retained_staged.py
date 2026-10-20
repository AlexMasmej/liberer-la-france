"""Isolated regressions against captured staged files, never active outputs."""
from pathlib import Path
from copy import deepcopy
import importlib.util
import json
import sqlite3
import sys
import tempfile
import types
import unittest
from unittest.mock import patch

PACK = Path(__file__).resolve().parent
LEGAL = PACK.parents[3]
sys.path.insert(0, str(LEGAL))
import reference_coherence as audit
import substantive_impact as impact

CURRENT = '--current' in sys.argv
if CURRENT:
    sys.argv.remove('--current')


def captured(name):
    module = types.ModuleType('isolated_' + name[:-3])
    path = LEGAL / 'runtime/substantive-priority-20261019/staged' / name if CURRENT else PACK / (name + '.reviewed')
    module.__file__ = str(path)
    exec(compile(path.read_text(), module.__file__, 'exec'), module.__dict__)
    return module


class RetainedStaged(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'batches/test').mkdir(parents=True)
        (self.root / 'policy-coordinations.json').write_text('{}\n')
        self.register = captured('register_batches.py')
        self.register.HERE = self.root
        self.register.load_companions = lambda: {}
        self.register.source_notes = lambda *args: ''
        self.db = sqlite3.connect(':memory:'); self.addCleanup(self.db.close)
        self.db.executescript('''CREATE TABLE articles(code_id,id,number,source_sha256,content_xml,valid_from,valid_until);
            CREATE TABLE drafts(code_id,source_id,source_sha256,status,proposed_xml,reason,review_notes);
            CREATE TABLE documents(code_id,id,kind,xml);''')
        self.row = {'code_id': 'CODE', 'source_id': 'A', 'number': 'L10-1',
                    'source_sha256': 'sha-a', 'status': 'retained_unchanged', 'proposed_xml': None,
                    'reason': 'Maintien de cette garantie nécessaire sans nouvelle variante stylistique.',
                    'review_notes': 'Aucune nouvelle obligation ni dépense n’est créée par ce maintien.',
                    'substantive_impact': {'version': 1, 'classification': 'retained_necessary',
                        'assessment': 'La garantie reste nécessaire et aucune coupe complémentaire justifiée ne ressort de cet examen.',
                        'scope_limitations': 'Ce maintien isolé ne préjuge pas du solde global des charges ou de tous les textes connexes.',
                        'new_burdens_review': 'La source entière demeure identique : aucune obligation nouvelle ne résulte de ce maintien.',
                        'effects': []}}

    def validate_body(self, body):
        self.db.execute('INSERT INTO articles VALUES(?,?,?,?,?,?,?)', ('CODE', 'A', 'L10-1', 'sha-a', body, '2026-01-01', '2999-01-01'))
        (self.root / 'batches/test/001.json').write_text(json.dumps([self.row]))
        return self.register.validate_batches(self.db, self.root / 'batches')

    def test_retained_prose_passes(self):
        self.assertEqual(len(self.validate_body('<p>La garantie du salarié demeure applicable.</p>')[0]), 1)

    def test_retained_table_must_pass_without_a_fabricated_rewrite(self):
        body = '<p>La garantie du salarié demeure applicable.</p><table><tr><th>Plafond</th></tr><tr><td>100</td></tr></table>'
        self.assertEqual(len(self.validate_body(body)[0]), 1)

    def graphic(self):
        return {'documentary_recovery_complete': True, 'expected_markers': 1,
                'documents': [{'path': 'official.pdf'}],
                'transcriptions': [{'marker': 1, 'text': 'Le tableau source prévoit un plafond de cent euros.'}]}

    def test_retained_recovered_graphic_is_preserved_in_companions(self):
        self.register.load_companions = lambda: {('CODE', 'A'): self.graphic()}
        body = '<p>Vous pouvez consulter le tableau dans le Journal officiel.</p>'
        self.assertEqual(len(self.validate_body(body)[0]), 1)

    def test_coordinator_rejects_retained_unrecovered_graphic(self):
        coordinator = captured('run_exhaustive.py'); coordinator.HERE = self.root
        source = {'code_id': 'CODE', 'source_id': 'A', 'number': 'L10-1', 'source_sha256': 'sha-a',
                  'source_xml': '<p>Vous pouvez consulter le tableau dans le Journal officiel.</p>',
                  'source_notes_xml': '', 'impact_check_required': True}
        with self.assertRaisesRegex(ValueError, 'graphic|formula|source|table|Graphic'):
            coordinator.validate_answer([deepcopy(self.row)], [source])
        source['source_companions'] = self.graphic()
        coordinator.validate_answer([deepcopy(self.row)], [source])

    def test_retained_reference_certificate_accepts_null_and_tracks_source(self):
        source = {'code_id': 'CODE', 'source_id': 'A', 'number': 'L10-1',
                  'source_sha256': 'sha-a', 'source_xml': '<p>La garantie de L20-1 demeure applicable.</p>', 'source_notes_xml': ''}
        target = {'code_id': 'CODE', 'source_id': 'B', 'number': 'L20-1',
                  'source_sha256': 'sha-b', 'source_xml': '<p>La garantie du salarié demeure applicable.</p>', 'source_notes_xml': ''}
        for a in (source, target):
            self.db.execute('INSERT INTO articles VALUES(?,?,?,?,?,?,?)', ('CODE', a['source_id'], a['number'], a['source_sha256'], a['source_xml'], '2026-01-01', '2999-01-01'))
        row = deepcopy(self.row)
        catalog = {audit.key(target): target}
        with patch.object(audit, 'HERE', self.root):
            snapshot = audit.capture(self.db, [source], catalog=catalog)
            row['reference_checks'] = [{'target_key': k, 'view_sha256': v['view_sha256'],
                'assessment': 'Le renvoi conserve intégralement la garantie de cet article cible ; aucun montant, délai ou droit du salarié ne disparaît par le maintien de la source.'}
                for k, v in snapshot['targets'].items()]
            audit.accept_checks([row], [source], snapshot, catalog)
            self.assertTrue(audit.certificate_current(self.db, source, None, row['reference_coherence'], catalog))
            self.db.execute('UPDATE articles SET content_xml=? WHERE id="A"', ('<p>La garantie de L20-1 est désormais modifiée.</p>',))
            self.assertFalse(audit.certificate_current(self.db, source, None, row['reference_coherence'], catalog))

    def test_null_substantive_certificate_is_stable_before_and_after_validation(self):
        coordinator = captured('run_exhaustive.py'); coordinator.HERE = self.root
        source = {'code_id': 'CODE', 'source_id': 'A', 'number': 'L10-1', 'source_sha256': 'sha-a',
                  'source_xml': '<p>La garantie du salarié demeure applicable.</p>', 'source_notes_xml': '', 'impact_check_required': True}
        row = deepcopy(self.row)
        coordinator.validate_answer([row], [source])
        self.assertIsNone(row['proposed_xml'])
        self.assertEqual(row['substantive_impact_certificate'], impact.certificate(row, source, audit.digest((self.root / 'policy-coordinations.json').read_text())))

    def test_progress_separates_retained_and_preserves_pending_publication(self):
        coordinator = captured('run_exhaustive.py'); coordinator.HERE = self.root
        coordinator.RUNTIME = self.root / 'runtime/exhaustive'; coordinator.RUNTIME.mkdir(parents=True)
        (coordinator.RUNTIME / 'publication-state.json').write_text('{"publication_pending":true}')
        path = self.root / 'test.sqlite'
        with sqlite3.connect(path) as db:
            db.execute('CREATE TABLE drafts(code_id,source_id,source_sha256,status,proposed_xml)')
            db.execute('INSERT INTO drafts VALUES(?,?,?,?,?)', ('CODE', 'A', 'sha-a', 'retained_unchanged', None))
            db.execute('INSERT INTO drafts VALUES(?,?,?,?,?)', ('CODE', 'B', 'sha-b', 'rewrite_draft', '<p>Une proposition complète nouvelle.</p>'))
        coordinator.open_db = lambda *args: sqlite3.connect(path)
        result = coordinator.progress({'travail': [
            {'code_id': 'CODE', 'source_id': 'A', 'source_sha256': 'sha-a'},
            {'code_id': 'CODE', 'source_id': 'B', 'source_sha256': 'sha-b'}]})
        self.assertEqual(result['drafted_articles'], 1)
        self.assertEqual(result['retained_unchanged'], 1)
        self.assertEqual(result['pending'], 0)
        self.assertTrue(result['publication_pending'])
        self.assertFalse(result['exhaustive_rewriting_complete'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
