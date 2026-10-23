# Décompte de clôture — portée et limites des secondes passes

Lecture opérationnelle du 23 octobre 2026, vers 02h54 UTC, sur une transaction SQLite en lecture seule et les neuf inventaires canoniques exportés. Aucun modèle, enregistrement d’article, changement de file, verrou rédacteur ou nouveau snapshot d’audit. Le manifeste de relecture était identique avant et après la lecture ; il n’est toutefois pas une ressource transactionnelle commune avec SQLite. Les preuves ne deviennent pas automatiquement actuelles après cette capture.

## Inventaire observé

Les neuf recueils contiennent 30 317 identités courantes. L’export, la configuration, les nombres de couverture et les empreintes/nombres des lignes canoniques concordent. Les propositions ou maintiens couvrent 28 610 identités ; 1 707 premières passes restent ouvertes au relevé. Quatre propositions historiques supplémentaires ne figurent pas dans cet inventaire courant : elles sont conservées séparément et ne sont pas ajoutées au pourcentage de couverture courante.

Le manifeste de relecture initial comporte 7 563 anciennes propositions du corpus courant : 2 472 portent le marqueur `completed`, et 5 091 restent `pending`. Quatre autres entrées sont explicitement hors inventaire courant. Sa directive porte sur les propositions antérieures à réexaminer sous les orientations de fond, pas sur toute entrée créée ensuite.

| Catégorie courante | Marqueur du manifeste initial | Nombre |
|---|---|---:|
| Proposition réécrite | Seconde passe marquée achevée | 1 396 |
| Source maintenue nécessaire | Seconde passe marquée achevée | 1 076 |
| Proposition réécrite | Seconde passe en attente | 5 091 |
| Proposition réécrite | Absente de cette liste initiale | 7 153 |
| Source maintenue nécessaire | Absente de cette liste initiale | 13 894 |
| Première passe encore ouverte | Absente de cette liste initiale | 1 707 |

Le fichier `current-article-ledger.jsonl` donne la correspondance par identité avec ses empreintes de proposition, motifs et notes. Il ne contient pas de nouveau texte juridique. `outside-current-inventory.json` garde les quatre identités historiques supplémentaires sans les supprimer ni les compter comme travaux courants.

## Ce que ces nombres ne prouvent pas

Les entrées hors de la liste initiale ne sont pas, par cette seule absence, dépourvues des validations ordinaires de première passe. Inversement, leurs contrôles de première passe ne constituent pas automatiquement une seconde lecture indépendante. Le seul marqueur `completed` d’une ancienne relecture ne prouve pas non plus que toutes les propositions, sources, politiques et cibles de renvois sont restées identiques depuis cette relecture.

Ce diagnostic n’établit aucune erreur juridique, n’ajoute aucune obligation de réécrire une ligne déjà acceptée et ne résout administrativement aucun signalement de renvoi. Il ne remplace ni l’audit global sur snapshot cohérent, ni la lecture sémantique des textes et cibles entiers, ni une validation humaine par juriste.

## Garde de clôture à conserver

Avant d’annoncer 100 %, rapprocher toutes les passes requises pour les textes du périmètre courant d’un registre d’évidence par article. Les preuves doivent désigner leur source, proposition entière, raisons, notes, politique, propriétaires, avant-images et cibles de renvois sous empreintes actuelles. Les marqueurs hérités ne se transfèrent que si les gardes pertinentes concordent. Toute lecture requise non attestée reste ouverte ; ne pas l’inférer de la file vide, d’un statut de première passe ou du nombre initial de 7 563.

Si une nouvelle liste de relecture doit être construite pour des textes non couverts par la liste initiale, la préparer à partir d’un état courant réconcilié, au point coordonné, en conservant intégralement les anciens registres et preuves. Utiliser les mêmes réservations, captures de before-image et validations ; ne pas modifier le manifeste actif pendant un lot. Ne pas convertir ce diagnostic en nouveaux travaux déclarés achevés.

Le contrôleur de réaffectation en préparation conserve sa portée bornée : finir les nouvelles entrées accessibles, reconstruire les différés réellement ouverts, puis exécuter les relectures et renvois gardés. Il ne décide pas à lui seul de l’exhaustivité de toutes les secondes passes. Les trois entrées retenues pour sources normatives, les limites sémantiques conservées et les coordinations extérieures restent ouvertes selon leurs suivis respectifs. Le corpus source est arrêté au 18 octobre 2026.
