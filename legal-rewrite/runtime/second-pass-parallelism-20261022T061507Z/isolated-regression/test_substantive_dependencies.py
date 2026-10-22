"""Published claims expire when a separately read dependency changes."""
from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase
import json
from build_substantive_report import build, _sha
from substantive_impact import certificate


class PublishedDependencies(TestCase):
    def setUp(self):
        self.tmp = TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.export = self.root / 'runtime/export-source'; self.export.mkdir(parents=True)
        self.batches = self.root / 'batches'; self.batches.mkdir()
        self.policy = self.root / 'policy-coordinations.json'; self.policy.write_text('{}')
        self.record = dict(code_id='CODE', source_id='A', number='L10-1',
                           source_sha256='source-a', source_xml='<p>Un avis séparé est obligatoire.</p>',
                           source_notes_xml='', proposed_xml='<p>Aucun avis séparé ne peut être exigé.</p>', status='rewrite_draft')
        self.target = dict(code_id='CODE', source_id='B', number='L20-1',
                           source_sha256='source-b', source_xml='<p>Le droit du demandeur est protégé.</p>',
                           source_notes_xml='', proposed_xml=None, status='source_imported')
        impact = dict(version=1, classification='material_reduction',
                      assessment='L’avis séparé est supprimé au profit de la procédure déjà ouverte dans cette disposition.',
                      scope_limitations='Le coût et le gain de temps individuels demeurent inconnus ; aucune extrapolation nationale.',
                      new_burdens_review='Aucune formalité supplémentaire n’est créée dans ce texte ; les autres droits restent protégés.',
                      effects=[dict(kind='obligation_removed', measure_id='separate-opinion-removed',
                                    description='Suppression de l’avis séparé.', before='Avis distinct obligatoire', after='Avis distinct supprimé',
                                    unit='legal_duty', affected_population='Demandeurs visés par le texte.',
                                    conditions_and_transition='Demandes nouvelles uniquement.',
                                    replacement_or_new_burdens='Aucune pièce ou demande de remplacement.',
                                    source_quote='Un avis séparé est obligatoire.', proposed_quote='Aucun avis séparé ne peut être exigé.')])
        row = self.record | {'substantive_impact': impact}
        self.approval = dict(code_id='CODE', source_id='A', assessment=impact,
                             certificate=certificate(row, self.record, _sha(self.policy.read_bytes())),
                             reviewed_by='Contrelecture IA distincte', approved_at='2026-10-20',
                             dependency_guards=[dict(code_id='CODE', source_id='B', source_sha256='source-b',
                                                     source_body_sha256=_sha(self.target['source_xml']), source_notes_sha256=_sha(''), proposed_sha256=_sha(''))])

    def render(self):
        (self.export / 'travail.json').write_text(json.dumps([self.record, self.target]))
        (self.root / 'runtime/substantive-audits.json').write_text(json.dumps({'version': 1, 'audits': [self.approval]}))
        return build(self.root / 'site/corpus', self.export, self.root / 'corpus.sqlite', self.batches)

    def test_dependency_source_change_retires_claim_without_changing_referrer(self):
        self.assertEqual(self.render()['coverage']['current_approved_independent_reviews'], 1)
        self.target['source_xml'] += '<p>Une condition différente est introduite.</p>'
        report = self.render()
        self.assertEqual(report['coverage']['current_approved_independent_reviews'], 0)
        self.assertEqual(report['measures'], [])

    def test_dependency_first_proposal_retires_old_official_only_analysis(self):
        self.assertTrue(self.render()['measures'])
        self.target.update(proposed_xml='<p>Une nouvelle garantie complète est proposée.</p>', status='rewrite_draft')
        self.assertEqual(self.render()['measures'], [])

    def test_dependency_missing_from_current_edition_is_not_silently_certified(self):
        self.approval['dependency_guards'][0]['source_id'] = 'MISSING'
        report = self.render()
        self.assertEqual(report['coverage']['unassessed_proposals'], 1)
        self.assertFalse(report['aggregation']['article_counts_are_savings'])
