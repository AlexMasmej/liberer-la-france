# Revue indépendante du cycle reference_queue

Module relu : legal-rewrite/reference_queue.py, SHA256 gelé `9f352613b6c71e81233c577e508f39506d019d04401106aaa333f757c34e66fe`.

Un défaut concret de gestion d'erreur est reproduit. Les douze autres scénarios du cycle passent. Le correctif séparé fait passer les treize tests ; aucun module canonique, corpus, lot ou politique n'a été modifié par le relecteur.

## Q1 — STOP déclenché trop tard après une exception de worker

Dans run(), future.result() peut lever une exception inattendue. Sans traitement à l'intérieur du bloc ThreadPoolExecutor, son gestionnaire de contexte attend les autres futures en sortie. À cet instant le STOP du coordinateur n'est pas encore positionné : la branche main qui le positionne ne reçoit l'exception qu'après la sortie du pool. Les tâches en attente peuvent donc démarrer d'autres invocations, au lieu de conserver immédiatement le reliquat en attente.

La reproduction utilise un pool d'un worker et trois tâches simulées : la première lève RuntimeError ; les deux autres attendent le signal STOP comme le fait run_in_slot avant de lancer le travail. Sur le module gelé le signal reste faux et les tâches suivantes partent avant la remontée de l'erreur. Ce n'est pas un faux marquage de complétude ; c'est un retard d'arrêt pouvant provoquer des traitements supplémentaires après l'échec.

Le correctif proposé entoure as_completed/future.result d'un try/except à l'intérieur du contexte du pool. Il positionne STOP, annule les futures qui n'ont pas commencé et propage la même exception. Les travailleurs déjà en cours restent soumis à l'arrêt gracieux existant ; ceux en attente d'un créneau voient STOP. Il ne tue pas un processus, ne masque pas l'erreur et n'inscrit aucun article.

Fichiers séparés : reference_queue.patch, reference_queue.proposed.py. Le fichier baseline conserve les octets du module relu. L'adoption appartient au parent.

## Scénarios vérifiés

1. Un certificat actuel et lié au corps courant est reconnu.
2. Une modification du corps appelant remet l'article en attente.
3. La première réécriture d'une cible invalide le certificat établi sur sa source officielle.
4. Deux modifications successives d'une cible changent l'empreinte de dépendance, même avec un appelant inchangé.
5. Une source pertinente sans proposition empêche le signal de contrôles complets.
6. Une cible pertinente non réécrite, incluse dans l'inventaire des sources, empêche aussi ce signal, même si l'appelant possède un certificat sur la source officielle de la cible.
7. Une proposition dont l'empreinte source est périmée n'est pas comptée comme réécriture actuelle.
8. Une cible changée après la certification de son appelant dans une même vague provoque une deuxième vague et converge après recertification.
9. Un état en attente inchangé provoque une erreur de non-convergence et conserve un rapport incomplet.
10. STOP avant la vague empêche tout lancement et retourne le reliquat.
11. STOP pendant la vague empêche une deuxième vague et retourne le reliquat.
12. Une file vide, mais des sources pertinentes non réécrites, ne produit pas de signal de complétude.
13. Une exception inattendue d'un worker doit déclencher STOP avant de vider les tâches en attente : seul test en échec sur le module gelé ; il passe sur le correctif.

Résultats enregistrés dans results.json, baseline-tests.log et proposed-tests.log : baseline13 tests,1 échec,0 erreur ; proposé13 tests,0 échec,0 erreur.

## Isolation et limites

Tous les tests utilisent leurs propres bases SQLite et fichiers batches temporaires. Aucune invocation de modèle, inscription d'article ou lecture du corpus réel n'est nécessaire. Le scénario de deuxième vague est déterministe : la cible change après le certificat initial, puis demeure stable. La convergence de cette machine de contrôle ne prouve pas la cohérence juridique des analyses qu'elle reçoit.

Le signal all_detected_contract_reference_checks_current reste celui des dépendances détectées du périmètre fourni, pas un certificat de réécriture exhaustive des cinq codes. Les contrôles des plages d'articles, des notes, du lien entre certificat et source appelante, de la conservation des analyses et du verrou de commit sont confiés au relecteur travail ; ils n'ont pas été dupliqués ici. Sa proposition de certificat autoportant v2 ne nécessite pas de modifier le contrat de certificates() pour le correctif Q1.
