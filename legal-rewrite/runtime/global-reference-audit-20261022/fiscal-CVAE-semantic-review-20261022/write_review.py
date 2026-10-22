"""Guarded semantic overlay for seven CVAE links; no active state mutation."""
from collections import Counter
from datetime import datetime, timezone
import hashlib
import html
import json
from pathlib import Path
import re
import sqlite3
import xml.etree.ElementTree as ET

OUT = Path(__file__).resolve().parent
AUDIT = OUT.parent
PROJECT = AUDIT.parent.parent
TARGET = 'LEGITEXT000006069577|LEGIARTI000048847020'
FIELDS = ('source_sha256', 'source_body_sha256', 'source_notes_sha256',
          'article_document_sha256', 'article_document_stored_sha256',
          'proposal_sha256', 'draft_source_sha256', 'draft_status')


def sha(value):
    return hashlib.sha256(value.encode() if isinstance(value, str) else value or b'').hexdigest()


def write(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


packet = json.loads((OUT / 'review-packet.json').read_text())
dependencies = json.loads((OUT / 'review-dependencies.json').read_text())
articles = {row['key']: row for row in packet['articles'] + dependencies['articles']}
by_number = {row['number']: row for row in articles.values()}
guards = {}
for line in (AUDIT / 'article-manifest.jsonl').open():
    row = json.loads(line)
    if row['key'] in articles:
        guards[row['key']] = {field: row[field] for field in FIELDS}
assert len(articles) == len(guards) == 13

policies, policy_before = {}, {}
for name in ('corpus.json', 'policy-coordinations.json', 'site-summaries.json', 'reference-focus-extra.json'):
    value = (PROJECT / name).read_bytes()
    (OUT / (name + '.current.frozen')).write_bytes(value)
    policy_before[name] = sha(value)
    policies[name] = {'source_path': str(PROJECT / name), 'snapshot_sha256': sha((AUDIT / name).read_bytes()),
                      'current_sha256': sha(value), 'matches_snapshot': sha(value) == sha((AUDIT / name).read_bytes())}
query = '''SELECT a.source_sha256,a.content_xml,a.valid_from,a.valid_until,a.state,
    p.proposed_xml,p.source_sha256 AS draft_source_sha256,p.status AS draft_status,
    d.xml AS document_xml,d.sha256 AS document_stored_sha256
    FROM articles a LEFT JOIN drafts p ON p.code_id=a.code_id AND p.source_id=a.id
    LEFT JOIN documents d ON d.code_id=a.code_id AND d.id=a.id AND d.kind='ARTICLE'
    WHERE a.code_id=? AND a.id=?'''
db = sqlite3.connect((PROJECT / 'corpus.sqlite').as_uri() + '?mode=ro', uri=True, timeout=2)
db.execute('PRAGMA query_only=ON')
db.row_factory = sqlite3.Row
current = {}
for key, expected in guards.items():
    row = db.execute(query, key.split('|')).fetchone()
    root = ET.fromstring(row['document_xml'])
    node = root.find('NOTA/CONTENU')
    notes = ((node.text or '') + ''.join(ET.tostring(child, encoding='unicode') for child in node)).strip() if node is not None else ''
    observed = {'source_sha256': row['source_sha256'], 'source_body_sha256': sha(row['content_xml']),
        'source_notes_sha256': sha(notes), 'article_document_sha256': sha(row['document_xml']),
        'article_document_stored_sha256': row['document_stored_sha256'],
        'proposal_sha256': sha(row['proposed_xml']) if row['proposed_xml'] is not None else None,
        'draft_source_sha256': row['draft_source_sha256'], 'draft_status': row['draft_status']}
    current[key] = {'number': articles[key]['number'], 'snapshot_guard': expected, 'current_guard': observed,
                    'matches_snapshot': expected == observed,
                    'validity_and_state_match': all(row[field] == articles[key][field] for field in ('valid_from', 'valid_until', 'state'))}
query_plan = [list(row) for row in db.execute('EXPLAIN QUERY PLAN ' + query, TARGET.split('|'))]
db.close()
for name, item in policies.items():
    item['stable_during_check'] = sha((PROJECT / name).read_bytes()) == policy_before[name]
checked_at = datetime.now(timezone.utc).isoformat()
all_current = all(row['matches_snapshot'] and row['validity_and_state_match'] for row in current.values())
all_policy = all(row['matches_snapshot'] and row['stable_during_check'] for row in policies.values())
assert all_current and all_policy
write('final-state-check.json', {'checked_at_utc': checked_at, 'query_mode': 'mode=ro; query_only=ON; indexed lookup per(code_id,id)',
    'article_queries': 13, 'query_plan': query_plan, 'direct_live_database_scan_performed': False,
    'new_snapshot_created': False, 'articles': current, 'policies': policies,
    'all_article_guards_match': all_current, 'all_policy_guards_match': all_policy})


def paras(row, view):
    body = row['content_xml'] if view == 'source' else row['proposed_xml']
    root = ET.fromstring('<audit-root>' + body + '</audit-root>')
    return [(index, ET.tostring(node, encoding='unicode'), ''.join(node.itertext()))
            for index, node in enumerate(root.findall('p'))]


def evidence(row, view, predicate):
    for index, markup, plain in paras(row, view):
        if predicate(plain):
            return {'article_key': row['key'], 'number': row['number'], 'view': view,
                    'paragraph_index_zero_based': index, 'exact_paragraph_xml': markup,
                    'paragraph_xml_sha256': sha(markup), 'text': plain,
                    'whole_view_sha256': guards[row['key']]['source_body_sha256' if view == 'source' else 'proposal_sha256']}
    raise ValueError('Evidence not found: ' + row['number'] + ' ' + view)


policy = json.loads((OUT / 'policy-coordinations.json.current.frozen').read_text())
review_id = sha(packet['latest_pointer']['audit_id'] + '|CVAE-seven-target-1586-ter-v1|' +
                json.dumps(guards, sort_keys=True) + json.dumps(policies, sort_keys=True))
target_proofs = [evidence(articles[TARGET], 'proposal', lambda s: s.startswith('Le présent article est abrogé')),
                 evidence(articles[TARGET], 'proposal', lambda s: s.startswith('Les cotisations afférentes')),
                 evidence(articles[TARGET], 'proposal', lambda s: s.startswith('La suppression de la CVAE'))]
reviewed = []
for finding in packet['findings']:
    row = articles[finding['source_key']]
    number = row['number']
    proof, secondary, benefit, analysis = [], [], [], ''
    if number in {'38', '39', '46 C'}:
        classification = 'coordination_des_annees_supprimees_avec_transition_ancienne'
        proof.append(evidence(row, 'proposal', lambda s: 'Pour les années d’imposition visées au premier alinéa' in s))
        if number == '39':
            proof.append(evidence(row, 'proposal', lambda s: s.startswith('l) Pour les années')))
            secondary.append(evidence(by_number['1586 octies'], 'proposal', lambda s: s.startswith('Pour une année supprimée')))
            old = 'Localisation, effectifs et période de référence exclusivement destinés à la CVAE'
        else:
            secondary.append(evidence(by_number['1586 octies'], 'source', lambda s: s.startswith('II.')))
            old = 'Tableau de calcul de la valeur ajoutée exigé lorsque l’obligation du II de 1586 octies s’applique'
        analysis = (old + ": le renvoi vise maintenant la frontière des années supprimées définie au premier alinéa de la proposition 1586 ter. Il ne demande pas d'appliquer un article abrogé pour imposer ou déclarer la CVAE; il retire ces données pour le nouveau champ et conserve explicitement le régime des années antérieures. La proposition 1586 octies supprime les mêmes obligations pour la même date. Les autres rubriques demeurent dans le texte et ne sont pas supprimées par la coordination CVAE.")
        benefit = ['Droits, exonérations, restitutions et recours des années anciennes conservés par la cible.',
                   'Aucune obligation CVAE d’une année supprimée imposée pour traiter une dette ancienne.',
                   'Les obligations IR, IS, sociales ou relatives aux autres impositions ne sont pas déclarées supprimées par ce renvoi.']
    elif number in {'1586 quinquies', '1586 sexies'}:
        classification = 'definition_autonome_favorable_maintenue_avec_transition'
        if number == '1586 quinquies':
            proof.extend([evidence(row, 'proposal', lambda s: s.startswith('I.')),
                          evidence(row, 'proposal', lambda s: s.startswith('II.')),
                          evidence(row, 'proposal', lambda s: s.startswith('III.'))])
            analysis = ("La période de référence est maintenue expressément pour 1647 B sexies et les autres impositions conservées. Le renvoi à 1586 ter ne rétablit aucune cotisation: il date la disparition de l'annualisation propre au champ/barème de CVAE et le passage aux définitions autonomes. L'annualisation favorable ou nécessaire de la valeur ajoutée reste régie séparément par 1647 B sexies. Les cinq configurations d'exercice et l'absence de double prise en compte sont conservées; les années anciennes gardent leurs règles et droits.")
        else:
            proof.extend([evidence(row, 'proposal', lambda s: s.startswith('Les définitions')),
                          evidence(row, 'proposal', lambda s: s.startswith('La présente rédaction'))])
            analysis = ("Le texte source entier de 1586 sexies, I à VII avec toutes les subdivisions sectorielles, est reproduit exactement entre un préambule et une transition. Le préambule maintient les définitions pour les avantages et impôts autonomes et exclut expressément une assiette, cotisation ou déclaration CVAE nouvelle. Le renvoi à 1586 ter n'est que le sélecteur temporel de ce changement de champ. Retirer ces définitions à cause de l'abrogation de la taxe priverait le plafonnement favorable de CFE de sa base.")
            assert row['content_xml'].strip() in row['proposed_xml']
        secondary.extend([evidence(by_number['1647 B sexies'], 'proposal', lambda s: s.startswith('b)')),
                          evidence(by_number['1647 B sexies'], 'proposal', lambda s: s.startswith('La valeur ajoutée prise')),
                          evidence(by_number['1647 B sexies'], 'proposal', lambda s: s.startswith('Le taux de plafonnement'))])
        benefit = ['Définitions de valeur ajoutée et de période nécessaires au plafonnement CFE maintenues.',
                   'Taux programmés confirmés par la politique repris dans la proposition: 1,531 % en2026–2027, 1,438 % en2028, 1,344 % en2029, 1,25 % dès2030. La confrontation de tous les textes différés reste ouverte.',
                   'Pas de CVAE fictive ajoutée au calcul ni d’économie nette de CFE promise à chaque contribuable.']
    elif number == '344 quindecies':
        classification = 'avantage_annuel_historique_preserve_et_coordonne'
        proof.extend([evidence(row, 'source', lambda s: 'l’année 2025' in s or "l'année 2025" in s),
                      evidence(row, 'proposal', lambda s: s.startswith('Pour l’année 2025')),
                      evidence(row, 'proposal', lambda s: s.startswith('a.')),
                      evidence(row, 'proposal', lambda s: s.startswith('b.')),
                      evidence(row, 'proposal', lambda s: s.startswith('Ces taux'))])
        secondary.extend([evidence(by_number['1635 sexies'], 'proposal', lambda s: s.startswith('3°')),
                          evidence(by_number['1635 sexies'], 'proposal', lambda s: s.startswith('Chaque année'))])
        analysis = ("La source fixe exclusivement deux abattements de 99 % pour 2025. La proposition conserve ces deux taux, les rectifications et restitutions de cette année et le fondement propre des autres années. Le renvoi CVAE dans le b reste utile pour le stock ancien; une clause interdit qu'il établisse une nouvelle CVAE ou additionnelle pour les années supprimées. Le 3° du II de 1635 sexies conserve la fixation annuelle dans la limite de99 %. Rien dans cet article annuel ne ferme l'avantage CFE/foncier futur ou n'étend son taux2025 à toutes les années.")
        benefit = ['Deux taux d’abattement de99 % pour2025 conservés, sans retrait rétroactif.',
                   'Fondement annuel de 1635 sexies maintenu pour les autres années.',
                   'Pas d’extrapolation du décret2025 à2026, ni de CFE de remplacement.']
    elif number == '238 bis HW':
        classification = 'regime_favorable_autonome_a_definition_historique_figee'
        proof.extend([evidence(row, 'source', lambda s: s.startswith('Les actions de la société agréée')),
                      evidence(row, 'proposal', lambda s: s.startswith('Les actions de la société agréée')),
                      evidence(row, 'proposal', lambda s: s.startswith('Pour les années supprimées'))])
        secondary.append(evidence(by_number['238 bis HV'], 'source', lambda s: s.startswith("Pour l'établissement")))
        analysis = ("Le dispositif d'approvisionnement électrique et l'avantage de souscription ont un fondement autonome dans 238 bis HV/HW. La proposition fige la définition du ratio de consommation/valeur ajoutée à la rédaction antérieure à la réforme, sans condition d'assujettissement ou paiement de CVAE. Son dernier alinéa interdit une déclaration CVAE pour les années supprimées et permet de justifier le ratio avec les données comptables de l'exercice de référence. Le renvoi ancien est donc matériel pour des bénéficiaires futurs, pas seulement un rappel d'une taxe ancienne. Les seuils et limites sources restent inchangés.")
        benefit = ['Ratio strictement supérieur à2,5kWh/€, durée d’au moins15ans, 55 % en heures creuses, 8 000heures et capital agréé600 000€ conservés.',
                   'Conditions de producteurs/activités et exceptions des arrêts et entretiens conservées.',
                   'Pas d’assujettissement, paiement ou déclaration CVAE nouveau pour obtenir l’avantage autonome.',
                   'La fenêtre2023–2028 de 238 bis HV reste explicite; l’IS à la distribution n’est pas réputé audité en entier ici.']
    else:
        raise AssertionError(number)
    reviewed.append({'review_id': review_id, 'global_audit_id': packet['latest_pointer']['audit_id'],
        'original_finding_id': finding['finding_id'], 'source_key': row['key'], 'number': number,
        'original_priority': finding['priority'], 'classification': classification,
        'effective_inconsistency_established': False, 'resolved': False,
        'status': 'reviewed_contextual_reference_no_error_established',
        'source_guard': guards[row['key']], 'target_key': TARGET, 'target_guard': guards[TARGET],
        'dependency_guards': {item['article_key']: guards[item['article_key']] for item in secondary},
        'policy_guards': {name: item['current_sha256'] for name, item in policies.items()},
        'current_guards_match_at_check': all_current and all_policy, 'analysis': analysis,
        'evidence': proof, 'dependency_evidence': secondary, 'preserved_benefits_and_limits': benefit,
        'recommended_action': 'Joindre cette qualification au signal; ne pas supprimer le renvoi ou un avantage et ne pas réécrire sans incohérence démontrée.',
        'automatic_change': False, 'semantic_review_by_jurist': False})

pending = [
    {'topic': 'Calendriers différés2027–2030 et recodification2030', 'status': 'pending_outside_this_targeted_group',
     'detail': 'Les notes et politiques citent des rédactions différées et un transfert vers1647BsexiesA. Les compagnons et lois de calendrier ne sont pas confrontés exhaustivement dans cette revue; aucune suppression globale irréversible de toute future CVAE n’est certifiée.'},
    {'topic': 'QPC2014-413 et note de1647Bsexies', 'status': 'pending_primary_decision_and_historical_version_review',
     'detail': 'La note mentionne l’inconstitutionnalité du dernier alinéa du II et le considérant8. Cette seule note ne permet pas de déduire le sort d’une rédaction ultérieure; aucune suppression ou validation de cet alinéa n’est inventée.'},
    {'topic': 'Modèles originaux CERFA et téléprocédures', 'status': 'still_missing_not_marked_recovered',
     'detail': 'La revue des articles textuels38/39/46C et1586octies ne récupère pas les modèles originaux, notices, cases ou schémas de transmission. Leur coordination et la couverture des formulaires restent à établir.'},
    {'topic': 'Modalités extérieures2023 de l’approvisionnement électrique', 'status': 'pending_outside_primary_text',
     'detail': 'Les notes de238bisHV/HW renvoient au VI de l’article86 de la loi2023-175. Le texte externe complet et ses modalités européennes ne sont pas confrontés dans cette revue.'},
    {'topic': 'Autres réformes intégrées aux articles lus', 'status': 'not_certified_by_CVAE_reference_review',
     'detail': 'L’annexeIII39 contient TSA/CPF-CDD et238bisHV contient une coordination IS à la distribution. Ces corps ont été lus pour leur contexte; leur ensemble normatif et les cibles209/217quindecies ne sont pas réputés audités par cette qualification CVAE.'},
]
summary = {'review_id': review_id, 'global_audit_id': packet['latest_pointer']['audit_id'],
    'reviewed_at_utc': checked_at, 'scope': 'Sept alertes P1 vers1586ter dans CGI et annexeIII',
    'findings_reviewed': len(reviewed), 'articles_read_in_full': len(articles),
    'classification_counts': Counter(item['classification'] for item in reviewed),
    'effective_inconsistencies_established': 0, 'resolved_findings': 0,
    'all_current_guards_match': all_current and all_policy, 'new_snapshot_created': False,
    'target_evidence': target_proofs, 'policy_evidence': {'cvae_removal': policy['cvae_removal']},
    'full_read_inventory': [{'key': key, 'number': row['number'], 'source_characters': len(row['content_xml']),
        'proposal_characters': len(row['proposed_xml'] or ''), 'official_notes_characters': len(row['source_notes_xml']),
        'guard': guards[key]} for key, row in articles.items()],
    'findings': reviewed, 'still_in_analysis': pending,
    'limits': ['Revue de cohérence interne du projet local, pas une consultation de droit positif ni validation par un juriste.',
               'T reste la date inconnue d’entrée en vigueur; la suppression couvre les années commençant au1erjanvier de l’année suivant T.',
               'ABROGE_DIFF indique une transition différée dans la source, pas une abrogation déjà applicable.',
               'Ne pas confondre mention historique et effet historique seulement: 238bisHW réemploie une définition ancienne pour un avantage futur.',
               'Aucune baisse supplémentaire, économie nationale ou solde net de complexité compté dans cette revue.',
               'Les gardes doivent être revérifiées après tout changement de source, proposition, note, calendrier ou politique.'],
    'semantic_review_by_jurist': False, 'automatic_change': False}
assert len(reviewed) == 7 and len({item['source_key'] for item in reviewed}) == 7
write('findings-reviewed.json', summary)
write('corrections.proposed.json', {'review_id': review_id, 'corrections': [],
    'reason': 'Aucune incohérence effective démontrée dans les sept renvois; aucune proposition de remplacement n’est fabriquée.',
    'guard_set': {'articles': guards, 'policies': {name: item['current_sha256'] for name, item in policies.items()},
                  'must_recheck_before_any_future_mutation': True, 'checked_at_utc': checked_at},
    'pending_reviews': pending, 'database_changed': False, 'batches_changed': False,
    'policy_changed': False, 'original_global_queue_changed': False, 'resolved_findings': 0})
write('queue-reviewed-overlay.json', {'review_id': review_id,
    'global_audit_id': packet['latest_pointer']['audit_id'], 'original_queue_unchanged': True,
    'items': [{field: item[field] for field in ('original_finding_id', 'source_key', 'number', 'classification',
        'effective_inconsistency_established', 'resolved', 'source_guard', 'target_guard', 'policy_guards')}
        for item in reviewed]})
lines = ['# Revue ciblée CVAE — sept renvois vers 1586 ter', '',
    'Aucune incohérence effective n’est démontrée dans ce groupe. Les sept alertes structurelles restent traçables; aucune n’est supprimée ou marquée résolue.', '',
    f'Les 13 articles entiers, notes et propositions ont été examinés. Les empreintes courantes correspondent au snapshot à {checked_at}. Les lectures directes utilisent les clés (code_id, id); aucun scan direct, nouveau snapshot ou rédacteur ajouté.', '',
    '| Article | Qualification |', '|---|---|']
lines.extend('| ' + item['number'] + ' | ' + item['classification'] + ' |' for item in reviewed)
lines.extend(['', 'Les renvois 38/39/46 C identifient les années pour lesquelles les formalités CVAE disparaissent. Les définitions 1586 quinquies/sexies restent nécessaires au plafonnement CFE. 344 quindecies conserve les deux abattements de 99 % de La Poste pour 2025. 238 bis HW fige une définition afin que la suppression de CVAE ne ferme pas un avantage électrique autonome.', '',
    'Le calendrier CFE proposé reprend les taux de la politique : 1,531 % en 2026–2027, 1,438 % en 2028, 1,344 % en 2029 et 1,25 % dès 2030. Les textes différés restent à confronter. Cette constatation ne démontre ni un gain net individuel égal à la CVAE brute ni une économie nationale.', '',
    '## Vérifications encore ouvertes', ''])
lines.extend('- ' + item['topic'] + ': ' + item['detail'] for item in pending)
lines.extend(['', 'Aucune correction de texte préparée faute d’erreur effective démontrée. Sources, propositions actives, batches, politique, file globale et certificats restent inchangés. Aucun statut de revue par un juriste.', ''])
(OUT / 'REPORT.md').write_text('\n'.join(lines))
write('artifact-manifest.json', {'review_id': review_id, 'global_audit_id': packet['latest_pointer']['audit_id'],
    'snapshot_sha256': packet['latest_pointer']['snapshot_sha256'],
    'files': {path.name: {'sha256': sha(path.read_bytes()), 'bytes': path.stat().st_size}
              for path in sorted(OUT.iterdir()) if path.is_file() and path.name != 'artifact-manifest.json'},
    'no_active_mutations': True})
print(json.dumps({'review_id': review_id, 'findings_reviewed': len(reviewed), 'articles_read': len(articles),
    'current_guards_match': all_current and all_policy, 'effective_errors_established': 0,
    'proposed_corrections': 0, 'resolved_findings': 0, 'new_snapshot_created': False}, ensure_ascii=False))
