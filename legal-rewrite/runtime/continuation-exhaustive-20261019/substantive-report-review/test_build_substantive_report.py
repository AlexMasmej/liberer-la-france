from copy import deepcopy
from pathlib import Path
import hashlib
import json
import sys
import tempfile
import unittest
from unittest.mock import patch

LEGAL = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(LEGAL))
import build_substantive_report as report
import substantive_impact as impact


class SubstantiveReport(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.legal = self.root / 'legal'
        self.export = self.legal / 'runtime/export-source'
        self.batches = self.legal / 'batches'
        self.out = self.root / 'site/corpus'
        self.export.mkdir(parents=True)
        (self.batches / 'test').mkdir(parents=True)
        self.policy = self.legal / 'policy-coordinations.json'
        self.policy.write_text('{"orientation":"alléger"}\n')
        self.record = {
            'code_id': 'CODE', 'source_id': 'ARTICLE-A', 'number': 'L10-1',
            'source_sha256': hashlib.sha256(b'original complete official document').hexdigest(),
            'source_xml': '<p>Le taux applicable aux salaires est de 9,2 %.</p>',
            'source_notes_xml': '<p>Disposition applicable aux nouveaux revenus.</p>',
            'proposed_xml': '<p>Le taux applicable aux salaires est de 6,6 %.</p>',
            'status': 'rewrite_draft',
        }
        self.row = {key: self.record[key] for key in ('code_id', 'source_id', 'number', 'source_sha256', 'proposed_xml', 'status')}
        self.row['substantive_impact'] = {
            'version': 1, 'classification': 'material_reduction',
            'assessment': 'Le taux salarial diminue à assiette identique dans le seul champ indiqué par cet article.',
            'scope_limitations': 'Aucun gain national ni effet sur les aides et impôts du foyer ne peut être déduit de cet article seul.',
            'new_burdens_review': 'Aucune déclaration ni condition nouvelle dans le texte proposé, qui modifie uniquement ce taux.',
            'effects': [{
                'kind': 'tax_reduced', 'measure_id': 'csg-salaires-prives',
                'description': 'Réduction du taux de CSG salariale.',
                'before': '9,2 % de la même assiette salariale',
                'after': '6,6 % de la même assiette salariale',
                'unit': 'percent', 'affected_population': 'Salariés visés par cet article.',
                'conditions_and_transition': 'Opérations nouvelles uniquement.',
                'replacement_or_new_burdens': 'Aucun remplacement identifié dans cet article.',
                'source_quote': 'Le taux applicable aux salaires est de 9,2 %.',
                'proposed_quote': 'Le taux applicable aux salaires est de 6,6 %.',
            }],
        }
        self.certify(self.row, self.record)

    def certify(self, row, record):
        row['substantive_impact_certificate'] = impact.certificate(row, record, report._sha(self.policy.read_bytes()))

    def write(self, records=None, rows=None):
        (self.export / 'travail.json').write_text(json.dumps([self.record] if records is None else records))
        (self.batches / 'test/001.json').write_text(json.dumps([self.row] if rows is None else rows))

    def build(self):
        return report.build(self.out, self.export, self.legal / 'corpus.sqlite', self.batches)

    def test_legacy_without_metadata_remains_unassessed(self):
        row = deepcopy(self.row)
        del row['substantive_impact']; del row['substantive_impact_certificate']
        self.write(rows=[row]); result = self.build()
        self.assertEqual(result['coverage']['unassessed_proposals'], 1)
        self.assertEqual(result['measures'], [])

    def test_current_worker_declaration_is_never_an_independent_audit(self):
        self.write(); result = self.build()
        self.assertEqual(result['coverage']['current_worker_declarations'], 1)
        self.assertEqual(result['coverage']['current_approved_independent_reviews'], 0)
        self.assertFalse(result['semantic_review_by_jurist'])
        self.assertIsNone(result['national_savings']['value'])
        self.assertEqual(result['net_global_reduction']['status'], 'not_established')

    def test_each_of_the_five_stale_guards_excludes_the_claim(self):
        for key in ('source_sha256', 'source_notes_sha256', 'proposed_sha256', 'assessment_sha256', 'policy_sha256'):
            with self.subTest(guard=key):
                row = deepcopy(self.row); row['substantive_impact_certificate'][key] = 'changed'
                self.write(rows=[row]); result = self.build()
                self.assertEqual(result['measures'], [])
                self.assertEqual(result['coverage']['unassessed_proposals'], 1)

    def test_anchor_validation_still_applies_even_with_recomputed_certificate(self):
        row = deepcopy(self.row)
        row['substantive_impact']['effects'][0]['source_quote'] = 'Un passage inventé qui ne figure pas dans la source.'
        self.certify(row, self.record); self.write(rows=[row])
        self.assertEqual(self.build()['measures'], [])

    def test_same_measure_across_articles_and_coordination_is_not_counted_twice(self):
        second = deepcopy(self.record); second.update(source_id='ARTICLE-B', number='L10-2')
        other = deepcopy(self.row); other.update(source_id='ARTICLE-B', number='L10-2')
        other['substantive_impact']['classification'] = 'coordination_only'
        other['substantive_impact']['effects'][0]['kind'] = 'coordination'
        self.certify(other, second); self.write(records=[self.record, second], rows=[self.row, other])
        result = self.build()
        self.assertEqual(len(result['measures']), 1)
        self.assertEqual(result['measures'][0]['kinds'], ['coordination', 'tax_reduced'])
        self.assertFalse(result['aggregation']['amounts_summed'])
        self.assertNotIn('total_savings', result)

    def test_mixed_additions_and_replacements_are_published(self):
        row = deepcopy(self.row)
        row['substantive_impact']['classification'] = 'mixed'
        addition = deepcopy(row['substantive_impact']['effects'][0])
        addition.update(kind='obligation_added', measure_id='new-declaration-burden',
                        description='Nouvelle déclaration', before='Aucune nouvelle déclaration',
                        after='Déclaration annuelle', replacement_or_new_burdens='Une démarche annuelle supplémentaire est créée.')
        row['substantive_impact']['effects'].append(addition)
        self.certify(row, self.record); self.write(rows=[row]); result = self.build()
        self.assertEqual(len(result['measures']), 2)
        page = (self.out.parent / 'bilan-allegements.html').read_text()
        self.assertIn('Obligation ajoutée', page)
        self.assertIn('démarche annuelle supplémentaire', page)

    def test_retained_source_uses_empty_proposal_hash_and_is_not_a_rewrite(self):
        record = deepcopy(self.record); record.update(status='retained_unchanged', proposed_xml=None)
        row = deepcopy(self.row); row.update(status='retained_unchanged', proposed_xml=None)
        row['substantive_impact'].update(classification='retained_necessary', effects=[])
        self.certify(row, record); self.write(records=[record], rows=[row]); result = self.build()
        self.assertEqual(result['coverage']['exported_proposals'], 0)
        self.assertEqual(result['coverage']['retained_sources'], 1)
        self.assertEqual(result['coverage']['current_worker_declarations'], 1)
        self.assertEqual(row['substantive_impact_certificate']['proposed_sha256'], hashlib.sha256(b'').hexdigest())
        self.assertEqual(result['measures'], [])

    def test_missing_certificate_is_unassessed(self):
        row = deepcopy(self.row); del row['substantive_impact_certificate']
        self.write(rows=[row]); self.assertEqual(self.build()['measures'], [])

    def test_page_escapes_metadata_and_never_uses_an_unsupported_economy(self):
        row = deepcopy(self.row)
        row['substantive_impact']['effects'][0]['description'] = '<script>alert(1)</script>'
        row['substantive_impact']['claimed_national_savings'] = 999999999
        self.certify(row, self.record); self.write(rows=[row]); result = self.build()
        page = (self.out.parent / 'bilan-allegements.html').read_text()
        self.assertNotIn('<script>', page)
        self.assertIn('&lt;script&gt;', page)
        self.assertIsNone(result['national_savings']['value'])
        self.assertNotIn('999999999', page)

    def test_current_approved_review_can_override_worker_but_stale_one_cannot(self):
        approved = {
            'code_id': self.record['code_id'], 'source_id': self.record['source_id'],
            'assessment': deepcopy(self.row['substantive_impact']),
            'certificate': deepcopy(self.row['substantive_impact_certificate']),
            'reviewed_by': 'Relecteur indépendant', 'approved_at': '2026-10-20T05:00:00Z',
        }
        path = self.legal / 'runtime/substantive-audits.json'
        path.write_text(json.dumps({'version': 1, 'audits': [approved]}))
        self.write(); result = self.build()
        self.assertEqual(result['coverage']['current_approved_independent_reviews'], 1)
        self.assertEqual(result['coverage']['current_worker_declarations'], 0)
        approved['certificate']['policy_sha256'] = 'old'
        path.write_text(json.dumps({'version': 1, 'audits': [approved]}))
        self.assertEqual(self.build()['coverage']['current_approved_independent_reviews'], 0)

    def test_coherent_export_does_not_require_database_to_have_same_current_draft(self):
        # A newer DB is irrelevant to the already exported edition; it is never opened.
        (self.legal / 'corpus.sqlite').write_bytes(b'not even a SQLite file')
        self.write(); self.assertEqual(self.build()['coverage']['current_worker_declarations'], 1)

    def test_conflicting_duplicate_assessments_do_not_silently_select_one(self):
        row = deepcopy(self.row)
        row['substantive_impact']['assessment'] += ' Une conclusion indépendante supplémentaire.'
        self.certify(row, self.record); self.write(rows=[self.row, row]); result = self.build()
        self.assertEqual(result['measures'], [])
        self.assertEqual(result['coverage']['unassessed_proposals'], 1)

    def test_policy_change_during_build_downgrades_all_claims(self):
        self.write(); original = report._batches
        def changed(folder):
            data = original(folder); self.policy.write_text('{"orientation":"nouvelle"}\n'); return data
        with patch.object(report, '_batches', side_effect=changed):
            result = self.build()
        self.assertEqual(result['measures'], [])
        self.assertEqual(result['articles'][0]['unassessed_reason'], 'policy_changed_during_build')

    def test_missing_proposal_is_coverage_only_not_a_material_assessment(self):
        record = deepcopy(self.record); record.update(proposed_xml=None, status='source_imported')
        self.write(records=[record], rows=[]); result = self.build()
        self.assertEqual(result['coverage']['exported_articles'], 1)
        self.assertEqual(result['articles'], [])
        self.assertEqual(result['measures'], [])

    def test_payment_deferral_is_distinct_from_a_permanent_tax_cut(self):
        row = deepcopy(self.row)
        row['substantive_impact']['classification'] = 'payment_timing_relief'
        row['substantive_impact']['effects'][0]['kind'] = 'payment_deferred'
        self.certify(row, self.record); self.write(rows=[row]); result = self.build()
        self.assertEqual(result['classification_counts']['payment_timing_relief'], 1)
        self.assertIn('sans baisse permanente', (self.out.parent / 'bilan-allegements.html').read_text())

    def test_extended_relief_and_deadline_units_are_preserved_without_sum(self):
        row = deepcopy(self.row)
        effect = row['substantive_impact']['effects'][0]
        effect.update(kind='relief_extended', unit='calendar_days', before='30 jours calendaires', after='60 jours calendaires')
        self.certify(row, self.record); self.write(rows=[row]); result = self.build()
        self.assertEqual(result['measures'][0]['effects'][0]['unit'], 'calendar_days')
        self.assertIn('Avantage ou exonération étendus', (self.out.parent / 'bilan-allegements.html').read_text())

    def test_build_does_not_modify_inputs(self):
        self.write()
        before = {p: p.read_bytes() for root in (self.export, self.batches) for p in root.rglob('*.json')}
        self.build()
        self.assertEqual(before, {p: p.read_bytes() for p in before})


if __name__ == '__main__':
    unittest.main(verbosity=2)
