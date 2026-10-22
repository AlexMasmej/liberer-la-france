"""Emit a read-only, guarded review overlay; never register or certify drafts."""
import hashlib
import html
import json
from pathlib import Path
import re
import sqlite3
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

OUT = Path(__file__).resolve().parent
PROJECT = OUT.parent.parent
TARGET = 'LEGITEXT000006072050|LEGIARTI000037312980'
FIELDS = ('source_sha256', 'source_body_sha256', 'source_notes_sha256',
          'article_document_sha256', 'article_document_stored_sha256',
          'proposal_sha256', 'draft_source_sha256', 'draft_status')


def sha(value):
    return hashlib.sha256(value.encode() if isinstance(value, str) else value or b'').hexdigest()


def write(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def text(value):
    return ' '.join(html.unescape(re.sub('<[^>]*>', ' ', value or '')).split())


packet = json.loads((OUT / 'L1242-2-review-packet.json').read_text())
dependencies = json.loads((OUT / 'L1242-2-review-dependencies.json').read_text())
articles = {row['key']: row for row in packet['articles'] + dependencies['articles']}
by_number = {row['number']: row for row in articles.values()}
manifest = {}
for line in (OUT / 'article-manifest.jsonl').open():
    row = json.loads(line)
    if row['key'] in articles:
        manifest[row['key']] = {field: row[field] for field in FIELDS}
audit_id = packet['findings'][0]['audit_id']
policy_names = ('corpus.json', 'policy-coordinations.json', 'site-summaries.json', 'reference-focus-extra.json')
policies_before = {name: sha((PROJECT / name).read_bytes()) for name in policy_names}
db = sqlite3.connect((PROJECT / 'corpus.sqlite').as_uri() + '?mode=ro', uri=True, timeout=2)
db.execute('PRAGMA query_only=ON')
db.row_factory = sqlite3.Row
identifiers = [row['id'] for row in articles.values()]
rows = db.execute('''SELECT a.code_id,a.id,a.source_sha256,a.content_xml,
    d.proposed_xml,d.source_sha256 AS draft_source_sha256,d.status AS draft_status,
    doc.xml AS document_xml,doc.sha256 AS document_stored_sha256
    FROM articles a LEFT JOIN drafts d ON d.code_id=a.code_id AND d.source_id=a.id
    LEFT JOIN documents doc ON doc.code_id=a.code_id AND doc.id=a.id AND doc.kind='ARTICLE'
    WHERE a.code_id=? AND a.id IN (''' + ','.join('?' for _ in identifiers) + ')',
    ['LEGITEXT000006072050', *identifiers]).fetchall()
db.close()
current = {}
for row in rows:
    root = ET.fromstring(row['document_xml'])
    node = root.find('NOTA/CONTENU')
    notes = ((node.text or '') + ''.join(ET.tostring(child, encoding='unicode') for child in node)).strip() if node is not None else ''
    guard = {'source_sha256': row['source_sha256'], 'source_body_sha256': sha(row['content_xml']),
             'source_notes_sha256': sha(notes), 'article_document_sha256': sha(row['document_xml']),
             'article_document_stored_sha256': row['document_stored_sha256'],
             'proposal_sha256': sha(row['proposed_xml']) if row['proposed_xml'] is not None else None,
             'draft_source_sha256': row['draft_source_sha256'], 'draft_status': row['draft_status']}
    key = row['code_id'] + '|' + row['id']
    current[key] = {'number': articles[key]['number'], 'snapshot_guard': manifest[key],
                    'current_guard': guard, 'matches_snapshot': guard == manifest[key]}
policies_after = {name: sha((PROJECT / name).read_bytes()) for name in policy_names}
policies = {name: {'snapshot_sha256': sha((OUT / name).read_bytes()),
                  'current_sha256': policies_after[name],
                  'matches_snapshot': sha((OUT / name).read_bytes()) == policies_after[name],
                  'stable_during_check': policies_before[name] == policies_after[name]}
            for name in policy_names}
checked_at = datetime.now(timezone.utc).isoformat()
current_ok = set(current) == set(articles) and all(item['matches_snapshot'] for item in current.values())
policy_ok = all(item['matches_snapshot'] and item['stable_during_check'] for item in policies.values())
write('L1242-2-final-state-check.json', {'checked_at_utc': checked_at,
    'source_connection': 'mode=ro; query_only=ON; one bounded SELECT for all 15 article states',
    'all_article_guards_match_snapshot': current_ok, 'all_policy_guards_match_snapshot': policy_ok,
    'articles': current, 'policies': policies})


def paragraphs(row, view):
    body = row['content_xml'] if view == 'official_source' else row['proposed_xml']
    root = ET.fromstring('<audit-root>' + body + '</audit-root>')
    return [(index, ET.tostring(node, encoding='unicode'), ''.join(node.itertext()))
            for index, node in enumerate(root.findall('p'))]


def evidence(row, view, predicate):
    for index, markup, value in paragraphs(row, view):
        if predicate(value):
            return {'article_key': row['key'], 'number': row['number'], 'view': view,
                    'paragraph_index_zero_based': index, 'exact_paragraph_xml': markup,
                    'paragraph_xml_sha256': sha(markup), 'text': value,
                    'whole_view_sha256': manifest[row['key']]['source_body_sha256' if view == 'official_source' else 'proposal_sha256']}
    raise ValueError('Required evidence paragraph missing: ' + row['number'] + ' ' + view)


target = articles[TARGET]
target_evidence = [
    evidence(target, 'official_source', lambda s: s.startswith('3°')),
    evidence(target, 'proposal', lambda s: s.startswith('Le présent article est abrogé')),
    evidence(target, 'proposal', lambda s: s.startswith('Les qualifications et droits')),
    evidence(target, 'proposal', lambda s: s.startswith('Les effets antérieurs')),
]
transition = by_number['L1241-1']
transition_evidence = [evidence(transition, 'proposal', lambda s: s.startswith('II.')),
                       evidence(transition, 'proposal', lambda s: s.startswith('La réalisation après')),
                       evidence(transition, 'proposal', lambda s: s.startswith('V.'))]
policy = json.loads((OUT / 'policy-coordinations.json').read_text())
policy_evidence = {'travail': [value for value in policy['travail'] if any(term in value for term in ('Rupture individuelle', 'CDD :', 'Intérim, portage'))],
    'favourable_rules': policy['cuts_and_reliefs_2026_10_19']['favourable_rules'],
    'warning': "Les quinze jours et le barème d'indemnité ordinaires ne sont pas réévalués par cet audit; la politique les distingue expressément des autorisations et protections spéciales."}
review_id = sha(audit_id + '|L1242-2-3-targeted-review-v1|' + json.dumps(manifest, sort_keys=True) + json.dumps(policies, sort_keys=True))
reviewed = []
for finding in packet['findings']:
    row = articles[finding['source_key']]
    is_mission = row['number'] == 'L1251-37-1'
    proofs = [evidence(row, 'proposal', lambda s: 'Pour les contrats conclus avant' in s or s.startswith('Les dispositions du présent article demeurent')),
              evidence(row, 'proposal', lambda s: '3°' in s and 'L. 1242-2' in s)]
    if is_mission:
        proofs.append(evidence(row, 'proposal', lambda s: s.startswith('Pour les contrats uniques')))
        proofs.append(evidence(row, 'proposal', lambda s: s.startswith("Les contrats conclus avant l'entrée")))
        classification = 'renvoi_historique_transitoire'
        analysis = ("Le renvoi au 3° de L1242-2 figure dans le bloc introduit expressément par « Pour les contrats conclus avant cette entrée en vigueur ». Le premier alinéa dispense déjà les nouvelles lettres de mission de carence légale et ne dépend pas de l'ouverture de nouveaux CDD. Le dernier alinéa maintient le régime applicable et les droits acquis des contrats antérieurs. La cible L1242-2 proposée conserve elle-même les qualifications et effets antérieurs. La note officielle de 2017 conserve son champ propre: elle ne date pas la réforme du contrat unique.")
        independent = None
        residual = ["Rendre, si nécessaire, le renvoi historique explicitement statique; le 3° dans sa rédaction applicable aux contrats concernés doit rester consultable.",
                    "Conserver la frontière de la note du 22 septembre 2017 pour les contrats anciens; ne pas appliquer rétroactivement son régime à tous les contrats conclus avant la future réforme."]
    else:
        proofs.extend([
            evidence(row, 'proposal', lambda s: s.startswith('Les renvois aux anciens articles')),
            evidence(row, 'proposal', lambda s: s.startswith('Les nouveaux contrats uniques')),
            evidence(row, 'proposal', lambda s: s.startswith('Pour les futurs salariés')),
        ])
        classification = 'protection_speciale_independante_avec_composante_transitoire'
        analysis = ("Le renvoi signalé est dans le bloc CDD source conservé intégralement et précédé d'une réserve expresse aux CDD antérieurs via L1241-1. Une clause supplémentaire interdit d'en tirer une nouvelle autorisation de CDD ou un renouvellement à terme. Le dernier alinéa vise expressément les futurs contrats uniques: il reprend seulement le champ matériel des activités saisonnières ou d'usage de l'ancien 3°, afin de maintenir la prolongation de protection pendant l'interruption habituelle d'activité. Cette protection nouvelle ne dépend pas d'une faculté actuelle de conclure un CDD; l'interruption ne termine pas le contrat et n'exonère pas de l'autorisation requise. Elle correspond à la conservation des protections et avantages favorables demandée par la politique.")
        independent = {'future_beneficiaries_expressly_covered': True,
                       'material_scope': 'Activités saisonnières OU d’usage par nature temporaire relevant du même champ matériel que le 3° ancien',
                       'preserved_benefit': "Prolongation des délais de protection égale à la période habituelle d'interruption de l'activité",
                       'new_CDD_authorization': False,
                       'automatic_contract_termination': False,
                       'special_termination_authorization_preserved': True,
                       'source_body_retained_as_exact_substring': row['content_xml'].strip() in row['proposed_xml']}
        assert independent['source_body_retained_as_exact_substring']
        residual = ["Clarification facultative: limiter l'alinéa d'ouverture aux dispositions relatives aux anciens CDD, afin qu'il ne paraisse pas exclure l'alinéa final expressément applicable aux futurs contrats uniques.",
                    "Clarification facultative: préciser que le renvoi matériel au 3° ancien vise une rédaction antérieure déterminée, sans retirer les activités d'usage ni les garanties des anciens représentants/candidats.",
                    "Les durées et conditions détaillées des articles L2411 cités ne sont pas revues intégralement ici; aucune conformité globale du statut protecteur n'est certifiée."]
    reviewed.append({'review_id': review_id, 'original_finding_id': finding['finding_id'],
        'global_audit_id': audit_id, 'source_key': row['key'], 'number': row['number'],
        'original_priority': finding['priority'], 'classification': classification,
        'effective_inconsistency_established': False,
        'review_status': 'reviewed_context_with_evidence_not_marked_resolved',
        'resolved': False, 'automatic_change': False, 'semantic_review_by_jurist': False,
        'source_guard': manifest[row['key']], 'target_key': TARGET, 'target_guard': manifest[TARGET],
        'policy_guards': {name: data['snapshot_sha256'] for name, data in policies.items()},
        'current_guards_match_snapshot_at_check': current[row['key']]['matches_snapshot'] and current[TARGET]['matches_snapshot'] and policy_ok,
        'analysis': analysis, 'reference_components': {
            'legacy_contract_reference': 'CDD ou contrats de mission antérieurs, avec régime conservé',
            'future_reference': independent},
        'evidence': proofs, 'target_and_transition_evidence_ids': ['target_evidence', 'transition_evidence'],
        'residual_review_points': residual,
        'queue_overlay_recommendation': 'Conserver le signal original et y joindre cette analyse; aucun remplacement automatique de la proposition.'})

unknowns = [
    "La date d'entrée en vigueur de la réforme reste une variable T: aucun texte de promulgation n'est supposé exister.",
    "La lecture est celle de textes de projet dans le snapshot local daté du 18 octobre 2026, pas une consultation de droit positif ni une validation par un juriste.",
    "Les conventions de branche, décrets sectoriels, conditions détaillées de tous les articles L2411 et procédures contentieuses externes ne sont pas revus dans ce contrôle ciblé.",
    "La présence du mot ancien ne permet pas de neutraliser le renvoi: les sept L2412 utilisent aussi l'ancienne définition pour une protection future autonome.",
    "Aucune réduction de charge, nouvelle simplification ou économie n'est comptée au titre de cette revue ou des clarifications facultatives.",
    "Toute modification ultérieure d'une source, proposition ou politique invalide les gardes et exige une nouvelle lecture du cas affecté.",
]
report = {'review_id': review_id, 'global_audit_id': audit_id, 'reviewed_at_utc': checked_at,
    'scope': 'Les huit propositions signalées vers le 3° de L1242-2, avec cible entière, notes et six dépendances entières',
    'target_key': TARGET, 'findings_reviewed': len(reviewed),
    'classification_counts': {'incoherence_effective_etablie': 0,
                             'renvoi_historique_transitoire': 1,
                             'protection_speciale_independante_avec_composante_transitoire': 7},
    'all_article_guards_match_current_state': current_ok,
    'all_policy_guards_match_current_state': policy_ok,
    'full_articles_read': [{'key': key, 'number': row['number'], 'source_characters': len(row['content_xml']),
                           'proposal_characters': len(row['proposed_xml'] or ''),
                           'official_note_nonempty': bool(row['source_notes'].strip()),
                           'guard': manifest[key]} for key, row in articles.items()],
    'target_evidence': target_evidence, 'transition_evidence': transition_evidence,
    'policy_evidence': policy_evidence, 'findings': reviewed, 'limits_and_unknowns': unknowns,
    'semantic_review_by_jurist': False, 'resolved_findings': 0, 'automatic_change': False}
write('findings-reviewed.json', report)

all_guards = {'articles': manifest, 'policies': {name: data['snapshot_sha256'] for name, data in policies.items()},
              'must_recheck_before_any_future_mutation': True,
              'current_matches_at_utc': checked_at, 'current_matches': current_ok and policy_ok}
seven_keys = [row['source_key'] for row in reviewed if row['classification'].startswith('protection_speciale')]
mission_key = by_number['L1251-37-1']['key']
actions = [
    {'action_id': 'document_review_context', 'priority': 2, 'type': 'review_overlay_only',
     'article_keys': [row['source_key'] for row in reviewed], 'guards': all_guards,
     'action': "Joindre la qualification documentée aux huit alertes. Ne pas remplacer automatiquement les renvois ni supprimer les protections au motif de l'abrogation prospective de L1242-2.",
     'mandatory_text_change_demonstrated': False,
     'acceptance': ['Les huit finding_id restent traçables.', 'Aucune alerte n’est marquée résolue automatiquement.', 'Les gardes correspondent encore aux corps source et proposés.']},
    {'action_id': 'clarify_legacy_opening_without_excluding_future_benefit', 'priority': 3,
     'type': 'optional_drafting_clarification_for_existing_writers', 'article_keys': seven_keys,
     'guards': all_guards,
     'action': "Si une reprise rédactionnelle est décidée, restreindre la phrase initiale aux dispositions relatives aux CDD antérieurs. Conserver expressément la protection des futurs contrats uniques dans l'alinéa final, les mêmes catégories protégées, l'interruption habituelle et l'autorisation de rupture. Ne pas supprimer l'alinéa final pour aligner artificiellement l'ensemble sur les anciens contrats.",
     'mandatory_text_change_demonstrated': False,
     'acceptance': ['Les sept blocs source restent protégés pour les CDD antérieurs.', 'Les futurs salariés saisonniers ET d’usage conservent la prolongation.', 'Ni fin automatique du contrat ni nouveau CDD.', 'Aucune protection de mandat retirée.']},
    {'action_id': 'make_historical_definition_version_explicit', 'priority': 3,
     'type': 'optional_static_reference_clarification',
     'article_keys': [row['source_key'] for row in reviewed] + [TARGET], 'guards': all_guards,
     'action': "Rendre la rédaction historique du 3° identifiable dans le lecteur et, si nécessaire, dans le texte: rédaction applicable aux contrats anciens concernés ou rédaction en vigueur immédiatement avant T pour la définition matérielle conservée. Pointer vers la source officielle figée, jamais vers le seul paragraphe d'abrogation proposé. Une copie de la définition doit préserver à la fois saison et usage temporaire et ne pas recréer un CDD.",
     'mandatory_text_change_demonstrated': False,
     'acceptance': ['Numéro, identifiant/version et empreinte de la définition sont consultables.', 'La définition matérielle reste distincte du droit de conclure un CDD.', 'Aucune date future de réforme inventée.']},
    {'action_id': 'retain_2017_note_boundary_for_legacy_missions', 'priority': 3,
     'type': 'transition_boundary_verification', 'article_keys': [mission_key], 'guards': all_guards,
     'action': "Conserver la portée de la note officielle de l'ordonnance du 22 septembre 2017 pour les contrats anciens, distinctement de T. Lors d'une reprise, préciser si besoin que la liste de dispense s'applique aux contrats antérieurs dans la mesure où ce régime leur était applicable, sans recommencer un délai ancien.",
     'mandatory_text_change_demonstrated': False,
     'acceptance': ['Le nouveau contrat unique reste dispensé de carence légale.', 'Les six exceptions anciennes restent ouvertes dans leur champ.', 'La note 2017 ne devient pas la date T.']},
]
scenarios = [
    {'case': 'CDD saisonnier protégé conclu avant T', 'expected': 'Régime ancien, clause de reconduction et prolongation de protection conservés, sous les conditions anciennes; aucune nouvelle autorisation de CDD.'},
    {'case': 'Contrat unique saisonnier protégé conclu après T', 'expected': 'Protection de mandat et prolongation pour interruption habituelle; interruption sans fin automatique de l’emploi.'},
    {'case': 'Contrat unique d’usage par nature temporaire protégé après T', 'expected': 'Même contrôle de conservation de la prolongation, sans réduire silencieusement la catégorie à la seule saison.'},
    {'case': 'Droit de réemploi saisonnier acquis avant T exécuté après T', 'expected': 'Réalisation sous contrat unique sans terme, ancienneté et garanties conservées; pas de nouveau CDD.'},
    {'case': 'Nouvelle lettre de mission après T', 'expected': 'Pas de carence légale entre lettres de mission, mais sécurité et conditions licites conservées; aucun besoin de rouvrir L1242-2.'},
    {'case': 'Contrat de mission antérieur au régime de la note de 2017', 'expected': 'Vérifier le régime réellement applicable au contrat; ne pas lui étendre rétroactivement la note de 2017 par la seule formule avant T.'},
]
write('correction-plan.json', {'review_id': review_id, 'global_audit_id': audit_id,
    'plan_status': 'review_proposals_only_no_batch_or_database_change',
    'guard_set': all_guards, 'effective_inconsistency_established': 0,
    'mandatory_article_rewrites_identified': 0, 'actions': actions,
    'acceptance_scenarios_for_any_future_edit': scenarios,
    'writer_capacity': 'Réservé aux six rédacteurs existants si une reprise est décidée; aucun nouveau travail de rédaction actif démarré.',
    'certificate_issued': False, 'database_changed': False, 'batch_changed': False,
    'global_queue_changed': False, 'resolved_findings': 0, 'limits': unknowns})
write('queue-reviewed-overlay.json', {'review_id': review_id, 'global_audit_id': audit_id,
    'original_queue_unchanged': True,
    'items': [{key: row[key] for key in ('original_finding_id', 'source_key', 'number', 'classification',
        'effective_inconsistency_established', 'resolved', 'source_guard', 'target_guard', 'policy_guards')}
        for row in reviewed]})
summary_lines = [
    '# Lecture ciblée des huit renvois au 3° de L1242-2', '',
    "Aucune incohérence effective n'est établie par ces huit renvois. Un renvoi est transitoire; sept utilisent aussi une définition ancienne pour maintenir une protection future autonome. Aucune alerte n'est supprimée ni marquée résolue.", '',
    f"Contrôle courant à {checked_at}: les 15 articles lus et les quatre fichiers de contexte correspondent au snapshot.", '',
    '| Article | Qualification |', '|---|---|',
] + [f"| {row['number']} | {row['classification']} |" for row in reviewed] + [
    '',
    "L1251-37-1 place la citation dans son bloc de contrats antérieurs; les nouvelles missions sont déjà dispensées de carence légale. Les sept L2412 conservent exactement leur corps source, le réservent aux anciens CDD, puis étendent explicitement la prolongation saisonnière ou d'usage aux futurs contrats uniques. L1242-2 et L1241-1 proposés conservent les qualifications et droits anciens et interdisent les nouveaux CDD.", '',
    "Le plan propose seulement des clarifications facultatives: portée de la phrase d'ouverture, version statique de la définition et frontière de la note de 2017. Retirer les renvois ou limiter les garanties aux contrats anciens supprimerait des protections que la politique demande de préserver.", '',
    'La portée complète des durées L2411, des accords et décrets sectoriels et des procédures externes reste à vérifier. Aucune revue juridique, aucun texte actif ni certificat modifié.', '',
]
(OUT / 'L1242-2-REVIEW.md').write_text('\n'.join(summary_lines))
names = ('L1242-2-review-packet.json', 'L1242-2-review-dependencies.json',
         'L1242-2-current-state-check.json', 'L1242-2-final-state-check.json',
         'findings-reviewed.json', 'correction-plan.json', 'queue-reviewed-overlay.json',
         'L1242-2-REVIEW.md', 'write_L1242_semantic_review.py')
write('semantic-review-manifest.json', {'review_id': review_id, 'global_audit_id': audit_id,
    'files': {name: {'sha256': sha((OUT / name).read_bytes()), 'bytes': (OUT / name).stat().st_size} for name in names},
    'snapshot_sha256': json.loads((OUT / 'capture.json').read_text())['snapshot_sha256'],
    'current_guards_matched': current_ok and policy_ok})
print(json.dumps({'review_id': review_id, 'reviewed': len(reviewed), 'current_guards_match': current_ok,
                  'policy_guards_match': policy_ok, 'classifications': report['classification_counts'],
                  'resolved_findings': 0, 'automatic_change': False}, ensure_ascii=False))
