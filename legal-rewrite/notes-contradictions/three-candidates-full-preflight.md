# Trois candidats — validation globale isolée réussie

R821-8, 49 septies ZZX et 49 septies ZZX bis ont passé le contrôle ordinaire global sur les 30 312 articles présents dans les lots figés : 1 448 fichiers, validation de 20,35 secondes. Les réponses, sources, NOTA, avantages, impacts et vérifications de références prévues par le moteur ont été contrôlés. Le catalogue automatique n’impose aucune cible contractuelle à ces trois articles ; les six sources et propositions couplées ont été gardées séparément. Ceci n’est ni un audit exhaustif de tous les renvois externes ni une validation juridique indépendante.

La capture est cohérente avec une transaction SQLite en lecture seule. Les lots testés sont des copies isolées. Le processus de contrôle est à priorité réduite ; aucun verrou d’écriture de production, aucune réservation manuelle et aucune interruption du coordinateur. Cette observation ne prouve pas à elle seule une absence de variation de débit.

**État historique avant intégration du 27 octobre au soir : les corrections n’étaient pas encore enregistrées ni publiables.** Le traitement actif reste dans une phase qui interdit les réservations manuelles. Leur intégration doit attendre un point naturellement drainé, puis refaire les gardes et les contrôles complets sous les verrous existants. Aucun résultat natif intervenu ne doit être écrasé. Les corrections parentales ne comptent pas comme lectures natives indépendantes.

[Résultat détaillé](../runtime/coordination-followups-20261026/three-full-preflight/ordinary-global-validation.json) · [Étapes d’intégration](../runtime/coordination-followups-20261026/safe-integration-plan.json). Les réserves demeurent ouvertes jusqu’à l’intégration acceptée et aux vérifications finales.


## Recontrôle du 27 octobre 2026

Les trois propositions R821-8 et annexe III 49 septies ZZX / ZZX bis conservent leurs propriétaires entiers et les propositions couplées de la préparation initiale. La validation complète actuelle a réussi sur 30 314 articles et 1 449 fichiers ; les gardes de sources, NOTA, bornes et politique ont été revérifiées. Le rapprochement intégral des neuf collections ne signale aucune divergence bloquante du registre ou de la liste de travail. Il conserve explicitement les certificats de références périmés et les preuves historiques à réexaminer ; il ne constitue pas une validation juridique finale.

L’arrêt sur limite d’usage du coordinateur 17229 avait été qualifié, mais la reprise ordinaire 82144 est intervenue avant l’acquisition des verrous d’intégration. Le verrou exclusif a refusé l’opération avant toute modification de production. Les trois correctifs restent **non intégrés** et les réserves restent **ouvertes**. Aucune relecture indépendante n’est ajoutée au compteur. Le script préparé pour l’ancien arrêt ne doit pas être rejoué sur la nouvelle reprise.

Preuves : `runtime/coordination-three-safe-point-20261027/fresh-preflight/ordinary-global-validation.json`, `reconciliation-before.json`, `tests.json` et `deferred-by-new-coordinator.json`. Au prochain point sûr naturel, recapturer les gardes et les propriétaires, refaire les contrôles courants et conserver les corrections parentales en attente d’une relecture native indépendante.

## Intégration contrôlée du 27 octobre au soir

Les trois correctifs ont désormais été enregistrés au point naturellement arrêté du coordinateur 82144, après gardes fraîches sur sources, NOTA, bornes, politique, propriétaires et textes couplés. La validation complète actuelle porte sur 30 314 articles et 1 449 fichiers. Les rapprochements des neuf collections avant, après enregistrement et après actualisation de la liste de travail ont réussi. La pause propre à cette intégration a été libérée.

Une première tentative avait été refusée au rapprochement pour un lien de révision antérieure manquant : ses avant-images ont été restaurées, sa validation et son archive conservées, puis le lien a été corrigé et tous les contrôles rejoués dans une nouvelle transaction. Aucune source canonique n’a été modifiée.

**Trois corrections parentales enregistrées ; zéro relecture native indépendante ajoutée.** Les deux lignes fiscales précédemment terminées sont remises en attente ; R821-8 y était déjà. Les trois réserves demeurent ouvertes jusqu’à leur lecture indépendante et la qualification finale des textes couplés. Les validations techniques ne valent pas approbation juridique.

Preuves courantes : [installation](../runtime/coordination-three-safe-point-20261027T2115Z-v2/installed.json), [rapprochement final](../runtime/coordination-three-safe-point-20261027T2115Z-v2/reconciliation-final.json), [validation globale isolée](../runtime/coordination-three-safe-point-20261027T2115Z-v2/fresh-preflight/ordinary-global-validation.json), [tests](../runtime/coordination-three-safe-point-20261027T2115Z-v2/tests.json). Les contrôleurs historiques ne doivent pas être rejoués.

## Suivi natif du 27 octobre, 22 h 03 UTC

Les deux correctifs fiscaux ont désormais fait l’objet d’un lot natif indépendant accepté par le coordinateur 2181 (deux articles, session attestée gpt-6-astra/medium, fin à 1793137509). R821-8 reste en attente. Cette acceptation ne clôt pas automatiquement les dossiers de cohérence couplée ni les contrôles finaux des références. Preuve : `runtime/coordination-followups-20261026/two-fiscal-native-acceptances-20261027T2203.json`.
