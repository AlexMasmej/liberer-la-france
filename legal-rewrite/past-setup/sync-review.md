# Synchronisation past.dev — livrable local à examiner

Le client `legal-rewrite/past_sync.py` est prêt ; aucun import, appel réseau, lecture de clé, rappel automatique ou service permanent n’a été exécuté pendant sa préparation. Aucun branchement du coordinateur n’a été ajouté. La permission humaine visée est « Import et futures mises à jour », réponse à `call_59e7245f52e54c5fba61ab228800962d`.

## Périmètre et contrôles

Le fichier distinct `full-approval.json` doit autoriser explicitement l’import et, pour `updates`, les mises à jour futures. Ses empreintes doivent correspondre exactement aux octets de `full-proposal.json` et `full-records.proposed.json`. L’ancien `approval.json` n’est pas modifié. Le projet est fixé à `default-project`, l’identité à `legal-rewrite`. Chaque document porte obligatoirement l’audience approuvée `orientations` ou `coordinations`.

Les 26 sources sont figées : 19 sections précises de `policy-coordinations.json` et 7 chemins d’audits Markdown. Les sections ou fichiers ajoutés ultérieurement sont ignorés ; une suppression ou un déplacement d’une source approuvée arrête la synchronisation, sans suppression distante automatique. Les liens symboliques sortant de `legal-rewrite` sont refusés. Un document dépassant la borne de taille n’est pas découpé automatiquement sous de nouveaux identifiants.

Les 10 identifiants de test sont réutilisés. Leur journal initial est reconnu seulement avec l’approbation du test, son empreinte, le reçu, le statut `completed` et le rapport de vérification. Sur les fichiers approuvés actuels, 9 corps du test sont inchangés et la section `is_distribution` a changé : l’import initial attendu comporte donc **17 contenus** (16 nouveaux et une révision), et non 26 nouveaux documents.

L’import initial utilise l’instantané expressément approuvé. Il ne remplace pas cet instantané par des fichiers locaux qui auraient changé entre l’approbation et son exécution ; `updates`, après achèvement de l’import initial, prendra en compte ces changements dans les seules sources approuvées.

## Exécution après revue par le parent

Depuis la racine du projet :

```sh
python3 legal-rewrite/past_sync.py initial
python3 legal-rewrite/past_sync.py poll
python3 legal-rewrite/past_sync.py updates
```

`initial` est idempotent ; une fois terminé, le relancer ne rétablit pas un vieil instantané après des mises à jour. `poll` effectue uniquement la consultation d’une ingestion déjà identifiée : il ne réingère jamais un document. `updates` n’envoie que les sources dont le corps a changé. Sans changement et sans ingestion en attente, il ne charge aucune clé, ne crée aucun client réseau et ne change aucun horodatage du journal.

Avant tout envoi nécessaire, le client vérifie à distance le projet et l’accès de l’identité fixe aux deux audiences. Le verrou `sync.lock` exclut les appels concurrents de plusieurs travailleurs ; l’appel perdant retourne `synchronization-already-running` avant tout accès réseau. Le parent peut traiter ce résultat comme une synchronisation déjà prise en charge, puis continuer son travail. Aucun rappel n’est associé à ces commandes : la préférence « seulement lorsque c’est utile » reste indépendante.

## Reprise et états incomplets

`sync-state.json` contient l’intention complète avant le premier POST, avec une clé d’idempotence stable et les horodatages persistés. Après réception, l’identifiant d’ingestion est conservé avant tout prochain passage. Les corps ne sont inscrits comme finalisés qu’au statut **`completed`** ; `queued`, `processing`, `failed` ou le seul état de disponibilité du projet ne valent pas achèvement.

Après une réponse perdue, `poll` retourne `receipt-unknown` sans POST. Relancer `initial` ou `updates` rejoue exactement l’intention enregistrée et la même clé, sans créer une révision artificielle. Une vraie succession de corps A → B → A reçoit en revanche une nouvelle clé, car chaque révision a son propre horodatage persisté.

Une ingestion en attente est rapprochée avant tout nouveau lot ; cela nécessite un appel de consultation, même si les corps locaux sont inchangés. Un échec reste bloquant et journalisé : aucune réingestion aveugle ni suppression du journal n’est effectuée. L’API officielle prévoit `POST /api/v1/ingest/{id}/retry` pour reprendre une ingestion échouée ; ce client ne l’automatise pas. Il faut examiner l’échec et, si approprié, effectuer cette reprise explicitement, puis reprendre `poll`. Ne pas effacer le journal pour contourner l’échec.

Les fichiers d’état et d’événements sont créés en mode `0600`, avec remplacement atomique et synchronisation sur disque. Le journal d’événements ne contient ni les documents ni les en-têtes d’authentification. L’intention persistée contient nécessairement les documents approuvés permettant la reprise exacte.

## Patch proposé au rappel — non appliqué

`past_memory_full_scope.proposed.patch` remplace seulement la liste des identifiants admissibles dans `PastClient.recall`. L’aide locale `past_sync.approved_source_ids` retourne les 26 identifiants si l’approbation complète et ses empreintes sont valides ; sinon elle conserve le périmètre du test approuvé. Une approbation complète active mais altérée échoue sans repli silencieux.

La vérification locale précède la requête de rappel. Les documents sans attribution, appartenant à une autre intégration ou mélangeant une source approuvée et une source étrangère restent exclus. Le lecteur fixe, les bornes de question/budget, le contrôle du projet et le MCP en lecture seule sont conservés. Il n’y a pas d’élargissement aux autres documents du projet ni de rappel systématique.

Le fichier canonique `past_memory.py` n’a pas été modifié. Le patch est établi sur la base SHA-256 `fae94ac9ba068bb09cb36e2d9d93a499b7133a67252af17969b2fd2ac2e8a0c8`. Les copies `.base.py.txt` et `.proposed.py.txt` permettent de relire et tester exactement le patch sans changer le client actif. Si le client canonique a changé, réexaminer ce delta avant de l’appliquer.

## Validation locale

```sh
cd legal-rewrite
python3 -m unittest test_past_sync test_past_memory -v
```

25 tests ont passé hors réseau, dont les 4 tests existants de frontière du rappel. Ils couvrent la persistance avant envoi, l’attente d’achèvement, la reprise après réponse perdue, les changements limités aux sources approuvées, les refus de projet/audiences non conformes, les identifiants réutilisés, le verrou des travailleurs et le patch de rappel chargé dans un module isolé. La fonction de lecture des identifiants de connexion est remplacée par un échec explicite pendant les tests ; les requêtes sont simulées.

Références API officielles consultées dans les copies locales `/private/tmp/past-api-reference.txt`, `/private/tmp/past-sending-data.txt` et `/private/tmp/past-setup.txt`. Les résultats simulés ne démontrent pas l’acceptation réelle du serveur ; celle-ci reste à vérifier lors de l’import approuvé exécuté par le parent.
