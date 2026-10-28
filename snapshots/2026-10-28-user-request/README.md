# Instantané intermédiaire du 28 octobre 2026

Demandé explicitement par l’auteur avant achèvement. La réécriture reste incomplète ; les contrôles techniques ne constituent pas une validation par un juriste.

Cet instantané est un différentiel par rapport au commit `cac48419271390c9d4f47917ffee30c1bd7f9c2a`. Il préserve le contenu de ce commit. `snapshot.json` donne les fichiers inchangés, ajoutés ou remplacés, leurs empreintes, les exclusions et les fichiers différés. Le dossier contient les parties et le manifeste permettant de reconstruire `payload.tar.gz`. Restaurer les archives de la base puis appliquer cette superposition uniquement dans un nouveau dossier.

La base SQLite active est une sauvegarde transactionnelle cohérente, rapprochée exactement des 30314 lignes de lots capturées sous verrou. Les fichiers des cinq sites sont capturés sous le verrou de publication ; leur état local et l’état du dernier déploiement figurent dans le manifeste. Aucun déploiement n’est déclenché par ce push.

## Restauration vérifiée

La restauration complète exige plusieurs dizaines de Go : prévoir de la place pour le dépôt de base, les parties compressées et les données décompressées. Conserver ce dossier d’instantané et préparer un autre checkout au commit de base indiqué dans `snapshot.json`, puis lancer, avec Python 3.11 ou ultérieur :

```sh
python3 /chemin/vers/instantane/restore-overlay.py --destination /chemin/vers/checkout-de-base
```

L’outil restaure les archives de base depuis leurs manifestes, vérifie les fichiers réutilisés et les empreintes de toutes les parties, puis applique les fichiers capturés. Il ne supprime aucun fichier propre à la base. Les exclusions et fichiers différés du manifeste restent hors de cette nouvelle capture. Les fichiers à la racine du dépôt représentent toujours la publication de base ; la superposition restitue cet instantané demandé.

Les sauvegardes SQLite sont cohérentes individuellement. Seule la base active est aussi rapprochée de l’ensemble des propriétaires de lots au même point de capture. Les archives historiques imbriquées non inspectées sont explicitement différées ou exclues ; elles ne sont pas présentées comme contrôlées.
