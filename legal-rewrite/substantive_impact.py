"""Require anchored before/after claims, without mistaking them for an audit.

Article counts and model declarations never establish a corpus-wide net cut.
Existing batches remain unassessed until their full source and draft are read.
"""
from html.parser import HTMLParser
import hashlib
import json
import re

VERSION = 1
POLICY_ID = 'substantive_outcomes_2026_10_19'
CLASSES = {'material_reduction', 'coordination_only', 'editorial_only',
           'retained_necessary', 'financing_transfer', 'payment_timing_relief', 'mixed', 'reserved'}
CUTS = {'tax_removed', 'tax_reduced', 'obligation_removed', 'obligation_merged',
        'authorization_removed', 'regime_merged', 'deadline_reduced', 'compliance_cost_reduced', 'relief_extended'}
ADDITIONS = {'tax_increased', 'obligation_added', 'deadline_increased', 'complexity_added'}
KINDS = CUTS | ADDITIONS | {'financing_transfer', 'payment_deferred', 'relief_preserved', 'coordination'}
UNITS = {'percent', 'euro', 'legal_duty', 'regime', 'calendar_days',
         'working_days', 'financing', 'other'}


class Plain(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def plain(value):
    parser = Plain()
    parser.feed(value or '')
    return ' '.join(' '.join(parser.parts).split())


def digest(value):
    return hashlib.sha256((value or '').encode()).hexdigest()


def assessment_digest(impact):
    return digest(json.dumps(impact, ensure_ascii=False, sort_keys=True, separators=(',', ':')))


def certificate(row, source, policy_sha256):
    return {'version': VERSION, 'source_sha256': source['source_sha256'],
            'source_notes_sha256': digest(source.get('source_notes_xml')),
            'proposed_sha256': digest(row.get('proposed_xml')),
            'assessment_sha256': assessment_digest(row['substantive_impact']),
            'policy_sha256': policy_sha256,
            'verification': 'exact_passages_and_hashes_only',
            'independent_impact_audit': False, 'semantic_review_by_jurist': False}


def validate(row, source, required=False, enforce_workflow=True):
    impact = row.get('substantive_impact')
    if impact is None and not required:
        return None
    if not isinstance(impact, dict) or impact.get('version') != VERSION:
        raise ValueError('A current substantive_impact assessment is required')
    category = impact.get('classification')
    if category not in CLASSES:
        raise ValueError('Unknown substantive impact classification')
    for field in ['assessment', 'scope_limitations', 'new_burdens_review']:
        if not isinstance(impact.get(field), str) or len(impact[field].strip()) < 40:
            raise ValueError('Specific substantive impact explanation required: ' + field)
    effects = impact.get('effects')
    if not isinstance(effects, list):
        raise ValueError('Substantive effects must be an explicit list')
    before = plain(source['source_xml'])
    after = plain(row['proposed_xml']) if row.get('proposed_xml') else before
    ids = set()
    for effect in effects:
        if not isinstance(effect, dict) or effect.get('kind') not in KINDS:
            raise ValueError('Unknown substantive effect kind')
        measure = effect.get('measure_id')
        if not isinstance(measure, str) or not re.fullmatch(r'[a-z][a-z0-9-]{5,95}', measure):
            raise ValueError('A stable measure_id is required to avoid counting its coordinations twice')
        identifier = (measure, effect['kind'])
        if identifier in ids:
            raise ValueError('Duplicate measure and effect in one article')
        ids.add(identifier)
        if effect.get('unit') not in UNITS:
            raise ValueError('An explicit effect unit is required')
        for field in ['description', 'before', 'after', 'affected_population',
                      'conditions_and_transition', 'replacement_or_new_burdens']:
            if not isinstance(effect.get(field), str) or not effect[field].strip():
                raise ValueError('Missing before/after effect detail: ' + field)
        for field, body in [('source_quote', before), ('proposed_quote', after)]:
            quote = effect.get(field)
            normalized_quote = plain(quote) if isinstance(quote, str) else ''
            if not isinstance(quote, str) or len(normalized_quote) < 12 or normalized_quote not in body:
                raise ValueError('Effect evidence is not an exact passage of the full article: ' + field)
        if effect['kind'] in CUTS and effect['before'].strip() == effect['after'].strip():
            raise ValueError('An unchanged value or duty is not a substantive reduction')
    kinds = {effect['kind'] for effect in effects}
    if category == 'material_reduction' and (not kinds & CUTS or kinds & ADDITIONS):
        raise ValueError('A reduction needs a concrete cut and must disclose additions as mixed')
    if category == 'financing_transfer' and (not kinds & {'financing_transfer'} or kinds & (CUTS | ADDITIONS)):
        raise ValueError('A financing transfer alone is not a tax or contribution cut')
    if category == 'payment_timing_relief' and ('payment_deferred' not in kinds or kinds & (CUTS | ADDITIONS)):
        raise ValueError('Payment timing relief is not a permanent tax cut')
    if category == 'mixed' and not kinds & (CUTS | ADDITIONS):
        raise ValueError('Mixed effects need concrete changes to burdens')
    if category in {'editorial_only', 'retained_necessary', 'reserved'} and effects:
        raise ValueError('Unchanged or editorial text cannot claim substantive effects')
    if category == 'coordination_only' and kinds - {'coordination', 'relief_preserved'}:
        raise ValueError('Coordination alone cannot claim a separate substantive cut')
    retained = row.get('status') == 'retained_unchanged'
    if category == 'reserved' and before not in {'Réservé.', 'Réservé', '(Réservé)'}:
        raise ValueError('Only an explicit reserved source can be classified as reserved')
    if retained and category not in {'retained_necessary', 'reserved'}:
        raise ValueError('A maintained source needs a specific necessity assessment')
    if retained and row.get('proposed_xml') is not None:
        raise ValueError('A maintained norm must not hide an altered proposal')
    if category in {'retained_necessary', 'reserved'} and not retained:
        raise ValueError('Maintain necessary sources without a cosmetic rewrite')
    if enforce_workflow and category == 'editorial_only' and not source.get('previous_draft'):
        raise ValueError('Do not create a stylistic rewrite: maintain a justified necessary source instead')
    if enforce_workflow and category == 'editorial_only' and row.get('proposed_xml') != source['previous_draft'].get('proposed_xml'):
        raise ValueError('An editorial-only review must not generate another stylistic version')
    return impact


PROMPT = '''
PRIORITÉ DE RÉSULTAT — lis substantive_outcomes_2026_10_19 de coordination.json.
Supprimer, fusionner et alléger avant de reformuler. Le nombre d'articles traités
mesure seulement la couverture. Ni une phrase plus courte ni un transfert de
cotisations vers la capitalisation ne prouve une baisse de prélèvement.
Pour chaque article, ajoute substantive_impact, objet version=1 avec :
- classification : material_reduction, coordination_only, retained_necessary,
  financing_transfer, payment_timing_relief, mixed, reserved ou editorial_only ;
- assessment : conclusion spécifique sur le changement réel par rapport à la
  source officielle entière, et pas seulement au précédent brouillon ;
- scope_limitations : ce qui n'est pas démontré, les coordinations manquantes,
  les populations et périodes non couvertes ;
- new_burdens_review : obligations, registres, données, délais et conditions
  nouveaux, y compris ceux créés en remplacement. Dire explicitement si aucune
  charge nouvelle n'est identifiée, avec sa justification, sans prétendre avoir
  chiffré le solde de l'ensemble des codes. Ces trois textes font au moins40caractères ;
- effects : liste, éventuellement vide, de changements normatifs démontrés.
Chaque effet contient kind, measure_id, description, before, after, unit,
affected_population, conditions_and_transition, replacement_or_new_burdens,
source_quote, proposed_quote. Les deux quotes sont des passages EXACTS non
tronqués, au moins12caractères, respectivement de la source et de la proposition
(texte sans balises). Elles ne peuvent être remplacées par une paraphrase.
kind : tax_removed, tax_reduced, obligation_removed, obligation_merged,
authorization_removed, regime_merged, deadline_reduced, compliance_cost_reduced,
tax_increased, obligation_added, deadline_increased, complexity_added,
financing_transfer, payment_deferred, relief_extended, relief_preserved ou coordination. unit : percent, euro,
legal_duty, regime, calendar_days, working_days, financing ou other.
measure_id est une clé descriptive stable en minuscules/tirets, de6à96caractères,
commune aux articles coordonnant UNE MÊME mesure. Ne transforme jamais chaque
renvoi d'une taxe supprimée en une taxe ou une obligation supplémentaire supprimée.
before/after précisent taux ET assiette si une baisse est avancée, les personnes
visées, et les délais/unités ; une taxe écartée dans le temps n'est pas abolie.
Une dépense moindre n'est pas une économie nationale chiffrée sans données.
Un étalement ou report de paiement seul est payment_timing_relief avec
kind=payment_deferred : amélioration de calendrier, sans baisse de taux revendiquée.
Une coordination conserve la même measure_id et kind=coordination ; elle n'est
pas une seconde réduction. Recense aussi les charges nouvelles, en classification
mixed lorsque coupes et ajouts coexistent. Si le solde net n'est pas établi,
écris-le. Un changement de financeur est financing_transfer, sans baisse fictive.
Une disposition essentielle ou une exonération nécessaire peut être MAINTENUE
INTÉGRALEMENT : status=retained_unchanged, proposed_xml=null,
classification=retained_necessary, effects=[], et analyse spécifique de sa
nécessité après examen de ses charges, doublons et renvois. Elle sera reproduite
en entier depuis la source et ne comptera pas comme réécrite ou simplifiée.
Ne maintiens pas ainsi un renvoi rendu incohérent ou un texte nécessitant une
réforme. Ne conserve pas un nouveau texte à droit constant pour changer des mots.
reserved est réservé aux véritables emplacements Réservé. editorial_only ne sert
qu'à conserver SANS nouvelle modification un brouillon antérieur stylistique ;
justifie-le et ne lui attribue aucune réduction. Aucune de ces déclarations ne
constitue un audit indépendant ni une preuve de réduction nette de complexité.
'''
