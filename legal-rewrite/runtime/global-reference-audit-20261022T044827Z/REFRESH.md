# Rafraîchissement de l'audit global

Analyse au 18 octobre 2026. Capture cohérente effectuée du 2026-10-22T04:48:27.938963+00:00 au 2026-10-22T04:48:52.454765+00:00, en lecture seule, par étapes de 256 pages (1 Mio maximum). Aucun blocage signalé par la sauvegarde ; contrôle SQLite réussi. L'ancien audit est conservé.

- **30 317 entrées** et **135 904 versions historiques** indexées.
- **459 023 occurrences ou liens** inventoriés ; **82 802 signalements structurels** à qualifier.
- **1 032 occurrences prioritaires P1**, touchant **631 articles distincts** ; **399 cibles proposées à l'abrogation** avec renvois détectés.
- Snapshot : **11 200 propositions** et **6 376 maintiens sans modification** dans l'inventaire canonique. Aucune proposition identique au corps source n'est comptée parmi les propositions.

La validation couvre l'inventaire complet, les empreintes de tous les articles/documents/archives/propositions, les quatre politiques figées, les gardes des 30 317 articles, toutes les gardes source/cible des liens et signalements, les 4 000 candidats historiques, l'identité et l'ordre de la file, les neuf rapports par recueil, les groupes de coordination et les cycles. Les 30 tests du parseur passent. Voir `validation.json` pour les compteurs exacts.

Les revues limitées L1242-2 (8 renvois, 15 articles lus) et CVAE (7 renvois, 13 articles lus) restent accessibles dans l'ancien dossier. Toutes leurs gardes source/proposition et leurs quatre politiques concordent avec ce snapshot. Leurs limites sont reprises intégralement dans `semantic-review-inheritance.json` ; zéro incohérence effective démontrée dans ces seuls groupes, zéro signalement marqué résolu. Elles ne valent pas revue juridique globale.

Pour le prochain seuil de rafraîchissement, le relevé conservateur pris **avant** la capture est conservé : **11 183 propositions, 6 345 maintiens, 897 secondes passes**, soit **1 144 traitements supplémentaires** depuis la baseline précédente. Le compteur de secondes passes n'est pas présenté comme un compteur transactionnel SQLite. Un nouveau snapshot sera dû après 1 000 traitements supplémentaires selon cette base, ou avant clôture.

Les signalements structurels ne sont pas des erreurs juridiques établies. Les ambiguïtés de code, versions historiques, alinéas et transitions restent à qualifier selon les limites du rapport principal. Aucune source, politique, base active, lot, proposition ou processus de rédaction n'a été modifié par ce rafraîchissement.
