# Instantané complet du travail — 25 octobre 2026

Cet instantané contient les cinq sites et les fichiers publiables de l’archive de rédaction présents lors de cet export. Le contenu antérieur du dépôt est conservé. Il ne s’agit pas d’une déclaration d’achèvement ni de validation juridique.

Les secrets, fichiers d’environnement, journaux de conversation, caches, états de processus et `jobs-before-policy.tar.gz` sont exclus. Les originaux locaux sont conservés. `manifest.json` énumère les fichiers inclus, leurs empreintes SHA-256, les exclusions et les fichiers différés car récemment modifiés. Les bases SQLite sont des sauvegardes cohérentes.

Pour restaurer dans un répertoire vide :

```sh
cat archive.tar.gz.part* | tar -xz
```

Vérifier préalablement les empreintes des parties dans `manifest.json`. `verification.json` atteste la lecture complète de l’archive, les empreintes de chaque fichier et les contrôles d’intégrité SQLite réalisés avant publication.
