"""Pure checks only: AST-selected functions, no module main/import/DB/ledger."""
import ast
import copy
import hashlib
import json
from pathlib import Path
import unittest

FILE = Path(__file__).with_name('adopt_reviewed.py')
TREE = ast.parse(FILE.read_text())
PURE = {'sha_bytes', 'digest', 'canonical_digest', 'key', 'pin', 'dependency_matches', 'prior_reasons', 'hashes_in', 'prior_allowlist', 'require'}
NS = dict(hashlib=hashlib, json=json)
exec(compile(ast.Module(body=[n for n in TREE.body if isinstance(n, ast.FunctionDef) and n.name in PURE], type_ignores=[]), str(FILE), 'exec'), NS)


class PriorAuditGuards(unittest.TestCase):
    def setUp(self):
        self.s = dict(code_id='A', source_id='1', number='N', source_sha256='official', source_xml='<p>source</p>', source_notes_xml='<p>note</p>')
        self.r = dict(code_id='A', source_id='1', number='N', proposed_xml='<p>draft</p>')
        self.assessment = dict(version=1, classification='coordination_only')
        self.dep = NS['pin'](dict(self.s, code_id='B', source_id='2'), dict(self.r, code_id='B', source_id='2'))
        self.audit = dict(reviewed_by='Independent reader', approved_at='old-date', assessment=self.assessment,
                          dependency_guards=[copy.deepcopy(self.dep)], certificate=dict(version=1,
                          source_sha256='official', source_notes_sha256=NS['digest'](self.s['source_notes_xml']),
                          proposed_sha256=NS['digest'](self.r['proposed_xml']),
                          assessment_sha256=NS['canonical_digest'](self.assessment), policy_sha256='OLD'))
        self.actual = {'B|2': copy.deepcopy(self.dep)}

    def reasons(self):
        return NS['prior_reasons'](self.audit, self.s, self.r, self.actual)

    def test_exact_all_dependencies_and_policy_only_refresh_allowed(self):
        self.assertEqual(self.reasons(), [])

    def test_source_header_changed(self):
        self.s['source_sha256'] = 'changed'
        self.assertIn('source_sha256', self.reasons())

    def test_own_notes_changed(self):
        self.s['source_notes_xml'] += ' changed'
        self.assertIn('source_notes_sha256', self.reasons())

    def test_own_body_pin_changed(self):
        self.audit['source_body_sha256'] = 'changed'
        self.assertIn('source_body_sha256', self.reasons())

    def test_own_proposal_changed(self):
        self.r['proposed_xml'] += ' changed'
        self.assertIn('proposed_sha256', self.reasons())

    def test_own_assessment_changed(self):
        self.audit['assessment']['classification'] = 'material_reduction'
        self.assertIn('assessment_sha256', self.reasons())

    def test_every_dependency_field_required_and_exact(self):
        for field in ('source_sha256', 'source_body_sha256', 'source_notes_sha256', 'proposed_sha256'):
            with self.subTest(field=field):
                self.actual['B|2'] = dict(self.dep, **{field: 'changed'})
                self.assertIn('changed_dependency:B|2', self.reasons())

    def test_missing_dependency_not_silently_skipped(self):
        self.actual = {}
        self.assertIn('changed_dependency:B|2', self.reasons())

    def test_missing_guard_hash_not_replaced_with_current(self):
        del self.audit['dependency_guards'][0]['source_body_sha256']
        self.assertIn('changed_dependency:B|2', self.reasons())

    def test_duplicate_dependency_rejected(self):
        self.audit['dependency_guards'].append(copy.deepcopy(self.dep))
        self.assertIn('duplicate_dependency:B|2', self.reasons())

    def test_null_proposal_not_confused_with_copied_source(self):
        self.actual['B|2']['proposed_sha256'] = NS['digest'](None)
        self.assertIn('changed_dependency:B|2', self.reasons())

    def test_review_identity_required(self):
        self.audit['reviewed_by'] = ''
        self.assertIn('missing_independent_reading_identity', self.reasons())

    def test_hash_evidence_nested_supported(self):
        self.assertIn('HASH', NS['hashes_in']({'variants': [{'answer.json': 'HASH'}]}))


class PriorAllowlist(unittest.TestCase):
    def fixture(self):
        entries = {'C|' + str(i): dict(code_id='C', source_id=str(i)) for i in range(284)}
        adopted = {'adopted': [dict(source_id=str(i)) for i in range(204)]}
        return entries, adopted

    def test_exact_204_only_excludes_80_even_with_empty_dependency_lists(self):
        entries, adopted = self.fixture()
        allowed = NS['prior_allowlist'](entries, adopted)
        self.assertEqual(len(allowed), 204)
        self.assertNotIn('C|204', allowed)
        self.assertNotIn('C|283', allowed)

    def test_duplicate_allowlist_rejected(self):
        entries, adopted = self.fixture()
        adopted['adopted'][-1] = adopted['adopted'][0]
        with self.assertRaises(ValueError):
            NS['prior_allowlist'](entries, adopted)

    def test_ambiguous_source_id_is_never_assigned_a_code_silently(self):
        entries, adopted = self.fixture()
        entries['OTHER|0'] = dict(code_id='OTHER', source_id='0')
        with self.assertRaises(ValueError):
            NS['prior_allowlist'](entries, adopted)

    def test_missing_allowlist_identity_rejected(self):
        entries, adopted = self.fixture()
        del entries['C|0']
        with self.assertRaises(ValueError):
            NS['prior_allowlist'](entries, adopted)


if __name__ == '__main__':
    unittest.main()
