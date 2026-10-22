# Revue indépendante des deux groupes de traitement

État : **23 tests indépendants réussis en 0,363 seconde**, sur des fichiers identiques avant et après l'exécution du 22 octobre 2026 à 06:40:22 UTC. Aucun défaut bloquant restant dans la portée testée. Ce document ne déclenche aucune bascule.

## Contrat contrôlé

La capacité locale autorisée est de huit traitements au total : au plus six nouvelles rédactions et deux secondes passes. Les deux groupes partagent le même compteur global, le verrou d'admission, les empreintes de lecture/écriture et l'arrêt STOP. Aucune capacité inutilisée par les secondes passes ne devient une septième place de nouvelle rédaction.

La réservation complète précède la soumission à un groupe. Un travail bloqué sur un renvoi ne consomme ainsi aucun thread d'exécution. Les six places des nouveaux articles restent disponibles pour des travaux compatibles. L'élargissement des lectures abandonne d'abord l'empreinte partielle, attend les conflits, puis relit les cibles entières ; le token de réservation est transféré au thread exécutant.

Le quota de seconde passe peut descendre à zéro : les actifs finissent, les travaux non admis restent en attente pour une reprise, les nouveaux articles continuent. STOP et les erreurs fatales ferment les admissions sans tuer les modèles déjà actifs. Une soumission refusée ou une future annulée avant exécution doit libérer la réservation une seule fois.

## Régressions éprouvées

Le premier test adversarial a reproduit le gel des admissions lorsque le consommateur de futures s'occupait d'un résultat. Le correctif sépare le dispatcher du consommateur et garde les deux plafonds de rôles. Le test libère les tâches actives pendant que le consommateur reste suspendu : les nouveaux travaux et secondes passes doivent continuer.

Le second test a reproduit le délai d'arrêt après une erreur fatale pendant que le consommateur était suspendu. Le correctif doit détecter l'exception dès la future, poser STOP, empêcher toute nouvelle soumission, drainer les actifs et livrer ensuite l'erreur originale. Le test compte directement les soumissions, puis vérifie l'absence de threads résiduels.

La preuve opérationnelle de huit agents a également été durcie : huit sessions vérifiées et distinctes, configuration explicite 8/6+2, un seul coordinateur attendu et aucun travail actif supplémentaire ou non attesté. Des tests positif et adversariaux couvrent cette distinction entre configuration et exécution observée.

## Couverture et limites

Les tests sont indépendants de ceux de l'auteur. Ils utilisent de véritables threads et les groupes préparés, avec travaux, bases et en-têtes CLI synthétiques. Les accès à la base active, appels de modèle, publications, verrous d'écriture réels et réservations de places réelles sont interdits par le banc de test. Aucun compte, crédit ou réglage global n'est modifié.

La comparaison des arbres syntaxiques vérifie que les fonctions de validation normative, bénéfices/impact, contrôle de politique, preuve native, invocation et engagement des propositions sont inchangées. Le contrôle d'avant-image complet de seconde passe dans review_prior.commit est également conservé. Les tests ne remplacent pas les validations de corpus et ne constituent pas une revue juridique.

La priorité d'admission des nouveaux articles est conservée selon la décision du coordinateur. Une seconde passe écrivant une cible commune peut attendre que ses lecteurs terminent dans la file finie ; les autres secondes passes indépendantes peuvent passer. Aucun verrou d'intention global n'est ajouté pour suspendre les six rédacteurs. Les conflits de renvois peuvent réduire la simultanéité effective.

Ces simulations ne prouvent ni huit réponses de modèles réelles ni un gain de débit. La bascule sûre, l'identité du nouveau coordinateur et les huit preuves natives après bascule relèvent du coordinateur principal. Le débit doit être observé sur sa fenêtre propre ; aucune non-régression réelle n'est déduite du seul plafond.

## Pièces

- implementation/test_review_lanes_independent.py : contrôles indépendants.
- independent-tests.log et independent-test-evidence.json : résultat final et empreintes avant/après.
- independent-slow-consumer-initial.log : reproduction de la première régression.
- independent-fatal-consumer-initial.log : reproduction de la seconde régression.

## Gel vérifié

- run_exhaustive.py : `1c66699d0b54334c099460546c8bd1cfced0a831336a544caf17b7b928538f7e`.
- review_lanes.py : `5a0fbfc04e9e2e4d6e6b315308425e6a807e5b2134a4dddd09ac65cfae22a1c5`.
- Les empreintes des six fichiers contrôlés, dont capacité, observation et tests, figurent dans independent-test-evidence.json.

L'annulation avant démarrage est également éprouvée : elle ne passe jamais dans run_in_slot.finally, mais libère sa réservation globale, son rôle et sa lease par le callback idempotent. Les contrôles d'erreur, STOP et fermeture anticipée ne laissent aucun thread résiduel. Les tests représentent des interleavings ciblés et ne constituent pas une preuve formelle couvrant tous les ordonnancements possibles.
