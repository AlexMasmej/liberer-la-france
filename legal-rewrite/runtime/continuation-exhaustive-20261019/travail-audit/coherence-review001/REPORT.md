# Revue indépendante du moteur de concordance

Deux correctifs séparés sont proposés, sans mutation des modules canoniques, de la base, des lots, de la politique ou des sites. Les fichiers relus ont été copiés avant les tests ; leurs empreintes figurent dans `reviewed-file-hashes.json`. La file `reference_queue.py` fait aussi l’objet de la revue indépendante de l’agent logement ; aucun patch de cette file n’est fourni ici.

## Défauts reproduits

1. **[P1] Plages imbriquées non développées — reference_coherence.py:46–50.** `L1251-58-1 à L1251-58-6` ne produit que les deux bornes. Les garanties d’intermission des articles intermédiaires peuvent donc changer sans périmer le certificat de l’appelant. Ce n’est pas théorique : la proposition de L1251-1 renvoie à cette plage. Le correctif traite la dernière subdivision numérique d’une même famille, les bornes répétées ou abrégées, les espaces et les entités HTML ; il garde la borne de cent intervalles et n’étend pas les familles différentes.

2. **[P1] Notes officielles absentes de la recherche des renvois — reference_coherence.py:55.** Un renvoi propre à une note d’application ou à une transition n’entre pas dans `requirements`. Un certificat peut donc sembler complet alors que ce renvoi n’a été ni fourni ni commenté. Le correctif ajoute `source_notes_xml` aux textes parcourus, sans remplacer le corps source.

3. **[P1] Verrou relâché avant l’inscription des révisions — review_prior.py:92–95.** Les cibles sont vérifiées sous un premier verrou, puis les fichiers sont remplacés, le verrou est relâché et `register()` est appelé dans un second temps. Un autre auteur peut modifier une cible dans cette fenêtre. Le test instrumente le registre et confirme qu’il est appelé hors du verrou ayant protégé la garde. Le correctif appelle l’implémentation déjà verrouillée `_register()` avant de quitter le premier bloc, sur la même connexion. Il évite une réacquisition bloquante du verrou non réentrant. Le contrôle final des certificats reste nécessaire pour les cibles modifiées par les articles du lot lui-même.

4. **[P2] Version officielle de l’appelant non liée au certificat — reference_coherence.py:137–147.** La version initiale lie le corps proposé de l’appelant et ses cibles, mais pas sa propre source officielle. Une nouvelle source contenant une condition différente, avec le même ensemble de renvois et la même proposition conservée, laisse `certificate_current()` vrai. Le correctif ajoute la garde complète de la source de l’appelant ; une réimportation officielle impose aussi de recharger le corpus utilisé par le coordinateur. Ce correctif ne prétend pas réparer automatiquement une importation de sources pendant le chantier.

5. **[P2] Analyses absentes mais certificat encore courant — reference_coherence.py:137–147 / reference_queue.py:11–15.** Après l’acceptation, le certificat initial ne contient ni les commentaires validés ni leur empreinte. Supprimer `reference_checks` du lot sans changer le corps laisse le certificat exploitable comme courant. Le correctif rend le certificat autonome : copie des analyses acceptées, empreinte de cette liste et vérification des clés, empreintes de cibles et longueurs à chaque contrôle. Supprimer la copie extérieure devient sans effet si les analyses subsistent dans le certificat ; perdre aussi celles-ci périme le certificat. Cela ne vérifie pas leur justesse sémantique.

Une sixième reproduction est une **défense supplémentaire**, distincte d’un défaut du flux normal DILA : modifier les notes dans `documents` tout en laissant l’empreinte d’importation de `articles` inchangée échappait aux gardes. Normalement, cette empreinte provient du document XML entier et couvre donc déjà les notes. Le correctif ajoute néanmoins les empreintes explicites du corps officiel et des notes aux gardes ; il détecte ainsi cette incohérence documentaire. Il suppose toujours que les sources assignées proviennent de l’importateur de confiance et ne constitue pas un réparateur de base corrompue.

## Cas contrôlés qui fonctionnent

- Les auto-renvois sont retirés par identité complète : ils ne créent pas un certificat constamment périmé par sa propre inscription.
- Une cible initialement officielle puis réécrite invalide la garde ; la file de concordance relance la revue et converge lorsque le corps de l’appelant reste stable.
- Un autre article réécrit dans le même lot peut rendre le certificat périmé dès l’inscription. Le contrôle final le retrouve bien. La garde préalable ne prétend pas avoir examiné le futur corps de cet autre article.
- Dans le driver réel testé, un changement de cible pendant le worker provoque un nouvel essai avec une capture actualisée. L’ancien `answer.json` sert à repérer les nouveaux renvois puis `answer.json` et `result.json` sont supprimés avant l’invocation suivante. Le second essai ne peut pas accepter le résultat précédent par inadvertance.
- Un renvoi nouvellement introduit dans la réponse exige son texte cible complet et le reçoit au nouvel essai.
- Les nouvelles écritures vérifient leurs cibles sous `writer_lock` et dans la transaction SQLite d’inscription. Les préimages de l’appelant en révision gardent leur contrôle de source et d’empreinte de proposition ; les tests existants refusent l’écrasement d’un auteur concurrent et archivent l’avant-image réelle.
- Les citations DILA sortantes et les bornes de familles simples sont couvertes par les tests existants. Le sens entrant n’est pas traité comme une citation émise par l’article. Les liens de version ancienne peuvent se résoudre par numéro qualifié unique ; cela ne prouve pas que leur champ historique est interchangeable avec celui de la proposition actuelle.
- Les commentaires peuvent expliquer l’inapplicabilité d’un régime extérieur, d’un contrat antérieur ou d’un agent public. Le moteur ne doit pas transformer leur présence en rattachement au contrat privé. Tous les certificats proposés conservent `semantic_review_by_jurist: false` ; le vérificateur proposé refuse un certificat qui prétendrait le contraire.

## Correctifs proposés

`reference_coherence.py.patch` et `review_prior.py.patch` sont des différences ciblées par rapport aux copies relues. Les versions complètes proposées sont les fichiers `.proposed.txt`. **Aucune copie complète de run_exhaustive.py ou reference_queue.py n’est à remplacer** : leurs versions `.baseline.txt` servent seulement aux tests et à la preuve de lecture.

Le certificat passe à la **version 2**. Les certificats version 1 sont délibérément périmés ; ils doivent être réexaminés, pas convertis mécaniquement en version 2. Aucun commentaire n’est inventé et aucune revue juridique n’est déduite d’un contrôle d’intégrité. La copie autonome des analyses évite d’imposer un changement du contrat de retour de `reference_queue.certificates()`.

Le coût supplémentaire correspond aux empreintes du corps officiel et des notes et à leur lecture dans les gardes. L’audit n’a pas mesuré le temps d’une passe sur les 30 317 entrées ; les lectures doivent rester locales. Le cache de catalogue reste celui de l’implémentation relue : si son périmètre change, le processus doit être relancé ou le cache explicitement invalidé.

## Résultats et reproduction

Sur les copies initiales : **13 cas indépendants, 7 comportements corrects et 6 lacunes reproduites**. Les six `expectedFailure` sont des défauts constatés, pas des succès métier. Parmi eux, cinq correspondent aux défauts ci-dessus et un au scénario d’incohérence des notes décrit séparément.

Sur les deux correctifs proposés : **13/13 cas indépendants réussis**, puis **50/50 tests existants réussis** (références, archives de révision, file de rédaction, intégration mémoire simulée et enregistrement de lots temporaires). Les deux patches passent l’application à blanc. Aucun modèle, service réseau ou registre de production n’a été appelé. Les sorties « registered: true » de la suite existante concernent exclusivement ses bases temporaires.

```sh
python3 legal-rewrite/runtime/continuation-exhaustive-20261019/travail-audit/coherence-review001/test_review_regressions.py
python3 legal-rewrite/runtime/continuation-exhaustive-20261019/travail-audit/coherence-review001/test_driver_branches.py
REVIEW_VARIANT=proposed python3 legal-rewrite/runtime/continuation-exhaustive-20261019/travail-audit/coherence-review001/test_review_regressions.py
REVIEW_VARIANT=proposed python3 legal-rewrite/runtime/continuation-exhaustive-20261019/travail-audit/coherence-review001/test_driver_branches.py
python3 legal-rewrite/runtime/continuation-exhaustive-20261019/travail-audit/coherence-review001/run_existing_regressions.py
```

Les tests de la file fournis séparément par logement restent à combiner avec ces patches avant redémarrage. Le parent conserve l’intégration, la dernière vérification des empreintes et le contrôle global. Cette revue du moteur ne valide aucun des textes légaux rédigés et ne certifie pas tous les renvois de l’ensemble des codes.
