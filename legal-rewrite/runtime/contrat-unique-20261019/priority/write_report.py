from pathlib import Path
import json

FOLDER=Path(__file__).resolve().parent
read=lambda name:json.loads((FOLDER/name).read_text())
guards=read('guard-report.json')
operations=read('reopen-operations.proposed.json')
targets=read('priority-targets.proposed.json')['targets']
by={(r['code_id'],r['source_id']):r for r in targets}
counts=guards['counts']
lines=[
'# Priorité contrat unique — proposition isolée',
'',
f"Capture : {guards['created_utc']}. Aucun fichier canonique, lot, base ou manifeste actif modifié par ce travail.",
'',
f"Sélection : **{len(targets)} articles** ; {counts.get('first_draft_priority',0)} premières rédactions, {counts.get('already_pending_guard_current',0)} revues déjà en attente et {len(operations)} réouvertures proposées. {guards['filtered_broad_candidates']} candidats larges écartés. L’inventaire initial contient {guards['initial_inventory_count']} entrées ; le complément approuvé est figé à 48 identités dans `outside-scope48.json`. Il ne constitue pas une nouvelle exploration ouverte.",
'',
f"**{guards['excluded_pack_records']} articles exclus** au titre des paquets explicites (dont {guards['excluded_from_initial_inventory']} Travail). Les paquets 45/70/48/12/47+5, D6222-21-1 et les deux miroirs D5132-10-5 / D5132-43-11 sont réservés quelle que soit leur situation d’enregistrement au moment de la capture. `excluded-packs.json` distingue une réponse identique enregistrée, une réponse réservée non enregistrée et une source réservée en attente de réponse. Exclusion ne signifie donc pas validation juridique ou publication.",
'',
'## Effet proposé sur les files',
'',
'Installer le module proposé à `legal-rewrite/contrat_unique_priority.py`, puis appliquer les deux patches isolés. Le module ne reconnaît que le couple code/article et son empreinte officielle ; les mots vagues et les numéros seuls ne donnent aucune priorité. L’inventaire JSON est lu localement, sans réseau. Une empreinte d’article différente perd la priorité ; un inventaire malformé provoque un arrêt explicite.',
'',
'Les nouvelles rédactions et les revues trient contrat unique avant SRU. Les lots sont coupés au changement de bande pour ne pas promouvoir des articles ordinaires avec un article prioritaire. En mode intercalé, un tri stable après intercalage et avant `max_jobs` place tous les lots du contrat unique avant les autres ; l’ordre relatif rédaction/revue est conservé à l’intérieur de chaque bande. Les limites de 24/12 articles et 45 000 caractères sont maintenues ; un article long reste entier.',
'',
'Les modes explicites `--review-prior-first` / `--review-prior-after` conservent leur ordre entre files ; la priorité contrat unique s’applique dans chacune. Le mode intercalé donne la priorité commune entre nouvelles rédactions et revues. Les travaux déjà en cours ne sont pas interrompus.',
'',
'Les gardes des deux fichiers canoniques figurent dans `pipeline-patch-guards.json`. Les patches ne touchent ni les instructions ni le hook mémoire récemment intégré. Leur application à blanc a réussi sur les bases capturées. Ne pas remplacer le fichier canonique par une copie `.proposed.txt` si un autre changement est intervenu : appliquer le patch ciblé ou régénérer depuis le dernier fichier.',
'',
'## Proposition explicite de reprise du manifeste',
'',
'`review-manifest.proposed.json` est une proposition complète ; aucun remplacement actif n’a eu lieu. `reopen-operations.proposed.json` fournit chaque ancienne entrée intégrale, l’empreinte de source officielle et l’empreinte de la proposition actuellement enregistrée. Les entrées pending compatibles restent telles quelles. Les archives de seconde passe sont conservées ; rouvrir une revue ne compte pas comme une nouvelle réécriture.',
'',
'Avant toute reprise : arrêter proprement le coordinateur, prendre le verrou partagé du registre, relire le manifeste et les sources/propositions canoniques. Appeler `propose_review_manifest` avec les opérations proposées et l’empreinte canonique de `guard-report.json` ; comparer le résultat à la proposition. Toute différence de manifeste, d’ancienne entrée, de source ou de proposition bloque la reprise et impose une nouvelle capture. Sauvegarder durablement le manifeste précédent, puis écrire atomiquement le résultat seulement après acceptation de ces opérations. La fonction est pure et ne fait elle-même aucune écriture.',
'',
f"Empreinte canonique du manifeste capturé : `{guards['manifest_canonical_sha256']}`. Empreinte du fichier : `{guards['manifest_file_sha256']}`. Échecs de garde : {len(guards['guard_failures'])}.",
'',
'## Articles de seconde passe à rouvrir',
'',
'La sélection exige une relecture complète ; elle ne préjuge pas d’une suppression des protections ni d’une modification nécessaire de chaque alinéa.',
'',
'| Article | Motif précis |',
'| --- | --- |',
]
motifs={
'L1221-1':'Socle de formation du contrat : articulation du contrat unique avec le droit commun.',
'L1221-5-1':'Informations essentielles remises au salarié : nature du contrat et modalités de fin à coordonner.',
'L1222-15':'Démission après mobilité volontaire sécurisée : le texte réserve le seul préavis de l’avenant.',
'L1223-5':'Mission à l’exportation et transition vers l’indemnité ordinaire dans la proposition existante.',
'L1223-6':'Mission à l’exportation : indemnité sans condition d’ancienneté dans la proposition existante, à comparer à la franchise d’un an.',
'L1223-7':'Protection sociale du titulaire d’un contrat de mission à l’exportation : statut à coordonner sans perdre les droits.',
'L1223-8':'Contrat de chantier et disposition transitoire d’indemnité dans la proposition existante.',
'L1223-9':'Contrat de chantier : contreparties d’indemnité et modalités de rupture à articuler au régime unique.',
'L1225-1':'Protection de la grossesse pendant l’essai : vérifier la cohérence du nouvel essai et du préavis en maintenant la protection.',
'L1225-6':'Échéance du CDD opposable aux protections : distinguer les seuls anciens contrats conservés en transition.',
'L1225-34':'Départ pendant la grossesse sans préavis ni indemnité : exception explicite à arbitrer/coordonner avec le délai de quinze jours.',
'L1225-38':'Protection en cas d’adoption et échéance du CDD : réserver le terme aux anciens contrats transitoires.',
}
for row in operations:
    lines.append('| '+row['number']+' | '+motifs.get(row['number'],'Clause ou renvoi précis documenté dans l’inventaire JSON.')+' |')
lines += ['',
'## Vérification',
'',
'16 tests ciblés hors réseau : identités et empreintes, inventaire invalide, refus des gardes modifiées, conservation de l’historique, ajout explicite d’une entrée absente, découpage réel des nouvelles rédactions et revues, priorité avant SRU et avant la limite intercalée, absence de doublons et présence des 48 ajouts. Les fonctions de file sont exécutées depuis les copies réellement patchées, sans lancer de modèle.',
'',
'25 tests de régression existants exécutés contre les modules proposés : rédaction/reprise, archivage des avant-images, contrôle de source, conservation des articles longs, contexte SRU et hook mémoire. Les accès de modèle et de mémoire restent simulés ; les écritures de tests restent temporaires.',
'',
'Commandes reproductibles depuis le projet :',
'',
'```sh',
'python3 legal-rewrite/runtime/contrat-unique-20261019/priority/build_patches.py',
'python3 legal-rewrite/runtime/contrat-unique-20261019/priority/build_proposal.py',
'python3 legal-rewrite/runtime/contrat-unique-20261019/priority/test_priority_proposal.py',
'python3 legal-rewrite/runtime/contrat-unique-20261019/priority/run_regressions.py',
'python3 legal-rewrite/runtime/contrat-unique-20261019/priority/verify_frozen_proposal.py',
'python3 legal-rewrite/runtime/contrat-unique-20261019/priority/write_report.py',
'```',
'',
'`build_proposal.py` ouvre SQLite en lecture seule dans une transaction de capture et écrit uniquement ce dossier de propositions. Les tests et ces propositions ne valident pas juridiquement les articles, ne modifient pas les sources et ne déclarent aucun article réécrit.',
]
(FOLDER/'REPORT.md').write_text('\n'.join(lines)+'\n')
print('Report written:',FOLDER/'REPORT.md')
