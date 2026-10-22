from copy import deepcopy
from unittest import TestCase
from substantive_impact import validate


class SubstantiveImpact(TestCase):
    def setUp(self):
        self.source = {'source_xml': '<p>Le taux applicable aux salaires est de 9,2 %.</p>'}
        self.row = {
            'status': 'rewrite_draft',
            'proposed_xml': '<p>Le taux applicable aux salaires est de 6,6 %.</p>',
            'substantive_impact': {
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
                    'proposed_quote': 'Le taux applicable aux salaires est de 6,6 %.'
                }]
            }
        }

    def test_anchored_before_after_survives(self):
        self.assertEqual(validate(self.row, self.source, required=True), self.row['substantive_impact'])

    def test_legacy_is_unassessed_but_new_job_requires_evidence(self):
        row = deepcopy(self.row); del row['substantive_impact']
        self.assertIsNone(validate(row, self.source))
        with self.assertRaisesRegex(ValueError, 'assessment is required'):
            validate(row, self.source, required=True)

    def test_paraphrased_or_fabricated_quote_is_rejected(self):
        self.row['substantive_impact']['effects'][0]['source_quote'] = 'Les salaires sont imposés à 25 %.'
        with self.assertRaisesRegex(ValueError, 'exact passage'):
            validate(self.row, self.source, True)

    def test_equal_value_is_not_a_cut(self):
        effect = self.row['substantive_impact']['effects'][0]
        effect['after'] = effect['before']
        with self.assertRaisesRegex(ValueError, 'unchanged value'):
            validate(self.row, self.source, True)

    def test_capitalisation_is_not_a_contribution_cut(self):
        self.row['substantive_impact']['classification'] = 'financing_transfer'
        with self.assertRaisesRegex(ValueError, 'financing transfer'):
            validate(self.row, self.source, True)
        self.row['substantive_impact']['effects'][0]['kind'] = 'financing_transfer'
        self.assertIsNotNone(validate(self.row, self.source, True))

    def test_new_burden_requires_mixed_classification(self):
        effect = deepcopy(self.row['substantive_impact']['effects'][0])
        effect.update(kind='obligation_added', measure_id='declaration-csg-nouvelle')
        self.row['substantive_impact']['effects'].append(effect)
        with self.assertRaisesRegex(ValueError, 'disclose additions'):
            validate(self.row, self.source, True)
        self.row['substantive_impact']['classification'] = 'mixed'
        self.assertIsNotNone(validate(self.row, self.source, True))

    def test_coordination_is_not_a_second_cut(self):
        self.row['substantive_impact']['classification'] = 'coordination_only'
        with self.assertRaisesRegex(ValueError, 'separate substantive cut'):
            validate(self.row, self.source, True)

    def test_deferred_tax_is_distinct_from_a_permanent_cut(self):
        self.row['substantive_impact']['classification'] = 'payment_timing_relief'
        with self.assertRaisesRegex(ValueError, 'permanent tax cut'):
            validate(self.row, self.source, True)
        self.row['substantive_impact']['effects'][0]['kind'] = 'payment_deferred'
        self.assertIsNotNone(validate(self.row, self.source, True))

    def test_a_real_norm_cannot_be_misclassified_as_reserved(self):
        self.row.update(status='retained_unchanged', proposed_xml=None)
        self.row['substantive_impact'].update(classification='reserved', effects=[])
        with self.assertRaisesRegex(ValueError, 'explicit reserved source'):
            validate(self.row, self.source, True)

    def test_necessary_rule_can_remain_without_inventing_a_rewrite(self):
        self.row.update(status='retained_unchanged', proposed_xml=None)
        impact = self.row['substantive_impact']
        impact.update(classification='retained_necessary', effects=[])
        self.assertIsNotNone(validate(self.row, self.source, True))
        self.row['proposed_xml'] = '<p>Une autre norme serait dissimulée ici.</p>'
        with self.assertRaisesRegex(ValueError, 'hide an altered'):
            validate(self.row, self.source, True)

    def test_no_new_cosmetic_version_even_during_review(self):
        self.row['substantive_impact'].update(classification='editorial_only', effects=[])
        with self.assertRaisesRegex(ValueError, 'stylistic rewrite'):
            validate(self.row, self.source, True)
        self.source['previous_draft'] = {'proposed_xml': self.row['proposed_xml']}
        self.assertIsNotNone(validate(self.row, self.source, True))
        self.row['proposed_xml'] = '<p>Une nouvelle variante simplement stylistique serait rédigée.</p>'
        with self.assertRaisesRegex(ValueError, 'another stylistic version'):
            validate(self.row, self.source, True)
