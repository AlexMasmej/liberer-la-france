# Transmission à une IA pour une troisième passe

## Dossier à ouvrir

`/Users/alexandremasmejean/.codex/.chatgpt-projects/g-p-6ad59c015c308191aa21cba63c71a6dc/legal-rewrite`

Le corpus comprend cinq codes et les quatre annexes du CGI, avec une date de référence au **18 octobre 2026**. La troisième passe n'est pas lancée par ce guide. À la demande de l'auteur du 26 octobre, le travail de ce suivi s'arrête après la fin vérifiée de la seconde passe ; les dossiers encore ouverts seront transmis tels quels.

## Entrées à lire en premier

| Fichier ou dossier | Contenu |
|---|---|
| `README.md` | Historique et fonctionnement du projet. Certaines indications opérationnelles sont historiques : ne pas exécuter les commandes sans confronter les consignes courantes. |
| `policy-coordinations.json` et `site-summaries.json` | Orientations de réforme à respecter, avantages et droits à conserver. |
| `corpus.sqlite` | Sources officielles et versions, documents XML/NOTA, propositions, motifs et notes. Identité complète : code + identifiant de version ; ne pas se fonder sur le numéro seul. |
| `batches/` et `registered-batches.json` | Lots propriétaires des propositions et leur registre. Les nouvelles propositions remplacent les anciennes selon un protocole gardé ; une ancienne copie de lot ne fait pas foi pour la version courante. |
| `runtime/radical-review-20261019.json` | Inventaire de seconde passe et preuves de traitement. |
| `runtime/exhaustive/status.json` | Compteurs opérationnels, sans assimilation à une validation juridique. |
| `notes-contradictions/INDEX.md` | Index des problèmes connus, réserves, corrections historiques et alertes à qualifier. |
| `runtime/global-reference-audit-latest.json` | Pointeur vers l'audit de références courant. Lire sa date, son résumé, ses gardes et ses limites avant d'utiliser ses résultats. |

## Mission de troisième passe suggérée

Lire chaque source, proposition, justification, note d'application et contrepartie pertinente en entier. Examiner les contradictions entre recueils, les champs et conditions, seuils, droits acquis, dates, transitions et renvois explicites ou implicites. Séparer : conflit de consolidation de la source, incohérence introduite par le projet, coordination manquante, pièce documentaire non obtenue et simple alerte automatique.

Préserver les orientations de fond et avantages déjà décidés, notamment TASCOM, dérogations littorales et contrat unique. Pour ce dernier : préavis de quinze jours calendaires de chaque côté ; aucune indemnité ordinaire avant un an ; ensuite 0,20 mois par année totale avec fractions proratisées, plafond de six mois, rupture à l'initiative de l'employeur seulement. Les protections autonomes et droits antérieurs restent distincts.

Pour chaque constat, fournir les identifiants et versions, passages entiers pertinents, preuves datées, conséquence, proposition de coordination et statut. Ne pas supprimer une faveur pour rendre des textes artificiellement cohérents. Ne pas déclarer une équivalence CIBS/UE sur une ressemblance de mots ou un lien de concordance.

## Conditions de lecture et de livraison

- Attendre la fin vérifiée de la seconde passe pour une revue d'ensemble stable. Avant cette date, toute lecture porte sur un état encore évolutif.
- Accès **en lecture seule** aux sources, à la base et aux lots. Avec SQLite, utiliser `mode=ro` et `query_only`. Une copie du seul fichier principal pendant des écritures/WAL n'est pas un instantané cohérent : demander un export ou une sauvegarde cohérente du workflow existant.
- Les fichiers du projet synchronisés sous `sources/` sont des références intouchables. Conserver XML, NOTA, tableaux, figures, bornes et vrais SQL NULL.
- Aucun lancement, import de module à effets de bord, intégrateur, reprise, publication, changement de politique ou ancien script d'activation pour simplement examiner les textes.
- Livrer un rapport séparé et des corrections proposées avec leurs gardes de version ; ne rien intégrer directement dans la production depuis une troisième passe externe.
- Les dossiers `runtime/` scellés sont des preuves datées. Ne pas rejouer leurs stades ou traiter leurs anciens compteurs comme actuels. Les candidats CSS non intégrés restent séparés des corrections déjà installées.
- La livraison doit distinguer couverture des articles, cohérence juridique, réserves documentaires et éventuelle validation de juriste. Une troisième lecture IA ne constitue pas à elle seule cette dernière validation.

Le dossier complet n'est pas un paquet d'export minimal. Pour une IA distante sans accès local, utiliser un export cohérent du corpus et des propositions, accompagné de cet index et des dossiers de preuve utiles ; ne pas téléverser indistinctement tous les journaux de fonctionnement.
