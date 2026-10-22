# Rafraîchissement de l’audit global

Corpus au 18 octobre 2026. Capture cohérente du 2026-10-22T07:58:42.005082+00:00 au 2026-10-22T07:59:09.711380+00:00, en lecture seule, par étapes de 256 pages (1 Mio maximum), avec contrôle SQLite réussi et 0 étape occupée signalée. Le dossier antérieur reste conservé.

- **30,317 entrées** et **135,904 versions historiques**.
- **461,143 occurrences ou liens** ; **84,100 signalements structurels** à qualifier.
- **1,096 occurrences P1**, concernant **663 articles distincts** ; **436 cibles proposées à l’abrogation** avec renvois détectés.
- Snapshot : **11,716 propositions**, **8,203 maintiens sans modification** ; zéro proposition identique au corps source.

La validation complète recalcule les inventaires, les empreintes logiques de toutes les métadonnées d’articles/documents/archives/propositions, les quatre fichiers de politiques, les gardes source/notes/document/proposition des 30 317 entrées, toutes les gardes source/cible des liens et signalements, les candidats historiques, l’identité et l’ordre de la file, les neuf rapports par recueil, les groupes de coordination et les cycles. Elle a réussi sans erreur. La preuve épinglée des 30 tests du parseur est réutilisée pour l’auditeur byte-identique ; aucun test du parseur n’a été répété. Voir `validation.json` et `parser-tests-inheritance.json`.

La revue limitée L1242-2 (8 renvois, 15 articles et dépendances) conserve sa portée : toutes les gardes d’articles et de politiques concordent. Ses limites sont reprises intégralement ; zéro incohérence effective démontrée dans ce seul groupe, zéro signalement marqué résolu.
La revue limitée CVAE (7 renvois, 13 articles et dépendances) conserve sa portée : toutes les gardes d’articles et de politiques concordent. Ses limites sont reprises intégralement ; zéro incohérence effective démontrée dans ce seul groupe, zéro signalement marqué résolu.

Le relevé conservateur pris avant capture est de **11,716 propositions, 8,203 maintiens, 1,339 secondes passes**, soit **1,260 traitements supplémentaires** depuis la baseline précédente. Les compteurs de progression ne sont pas présentés comme transactionnellement synchrones avec SQLite. Le prochain rafraîchissement est dû après 1 000 traitements supplémentaires selon cette base, ou avant clôture.

Aucune priorité de processus actif n’a été modifiée. La sauvegarde a utilisé les lectures bornées prévues. Aucun slot, processus de rédaction, code actif, politique, catalogue, donnée canonique, note, lot ou proposition n’a été modifié par cet audit. La seule publication est le pointeur d’audit, remplacé atomiquement après validation.

Les occurrences et signalements structurels ne constituent pas des fautes juridiques établies. Les ambiguïtés de code, versions historiques, alinéas et transitions restent à qualifier selon les limites du rapport principal. Ces revues limitées ne valent pas revue juridique globale.
