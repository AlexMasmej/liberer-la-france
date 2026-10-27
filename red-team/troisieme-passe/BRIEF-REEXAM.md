# Brief — réexamen des objections après l'instantané intermédiaire (revue des différences, § D)

À lire **après** `BRIEF-AGENTS.md`. Toutes ses règles s'appliquent : lecture seule, interdits absolus, discipline de qualification. Trois points de ce brief les remplacent.

## Ce qui change

- **L'instantané courant est maintenant `snapshots/20261027T044303Z/`.** L'ancien instantané `20261026T230545Z` a été supprimé par rotation et n'existe plus.
  - La seconde passe est **arrêtée** : statut `blocked`, limite d'usage du compte, reprise possible le 2 novembre. Elle a relu 15 597 articles sur 30 314.
  - L'instantané est cohérent : base = registre = lots, sans écriture en vol.
- **Les anciens textes** restent disponibles dans `evidence/cited/20261026T230545Z/` : une export JSON par numéro, avec toutes ses versions et leurs empreintes. Les empreintes par article des deux instantanés sont dans `manifests/20261026T230545Z.json` et `manifests/20261027T044303Z.json`.
- **Les nouveaux textes** se lisent avec `python3 -I tools/cite.py <code> <numéro|LEGIARTI>`. L'outil lit désormais le nouvel instantané et écrit dans `evidence/cited/20261027T044303Z/`.

## Ta tâche

Tu reçois un paquet (`reports/reexam/packets.json`, filtré sur tes identifiants). Pour chaque objection, il contient :
- les articles modifiés depuis l'ancien instantané, avec les champs modifiés : proposition, statut, motif, notes, statut de seconde passe ;
- les alertes P1 liées dont l'état a changé : `before` et `after`, avec `bucket`, `reference_gone`, etc.

Pour chaque objection :
1. Relis l'objection complète dans `reports/register.json`.
2. Lis **en entier** l'ancienne version (export `20261026T230545Z`) et la nouvelle version (`cite.py`) de chaque article modifié : proposition, motif, notes de revue. Vérifie aussi les autres articles de l'objection, qui peuvent avoir été touchés indirectement.
3. Classe l'objection :
   - `maintenue` : le défaut subsiste, inchangé ;
   - `reformulée` : il subsiste, mais sa forme, sa portée, sa priorité ou sa correction change ;
   - `résolue` : la nouvelle rédaction règle le défaut. Cite le passage qui le règle et vérifie qu'il ne crée pas d'effet nouveau, notamment la perte d'une faveur, une formalité ou un renvoi cassé ;
   - `obsolète` : la prémisse ne tient plus pour une autre raison.
4. Si la nouvelle rédaction introduit un **défaut nouveau** dans le périmètre lu, signale-le sous `new_findings`, au format d'objection de `BRIEF-AGENTS.md`, avec des identifiants `RT-RX<groupe>-NN`.
5. Une modification des seules notes ou du seul motif peut suffire à résoudre une objection qui portait sur une note erronée. Elle ne résout jamais un défaut du texte proposé.

**Alertes écartées dont les textes ont changé** (groupe ALERTS seulement) : requalifie chaque alerte selon la méthode de `BRIEF-P1.md`. La question est de savoir si le renvoi vers une disposition abrogée par le projet pose désormais un problème réel.

## Livrable

Écris `reports/reexam/<GROUPE>.json` :

```json
{"group": "...", "snapshot_old": "20261026T230545Z", "snapshot_new": "20261027T044303Z",
 "objections": [{"id": "...", "verdict": "maintenue|reformulée|résolue|obsolète",
   "new_priority": "P0|P1|P2|null", "new_status": "confirmé|à confirmer|résolu|obsolète",
   "trace": "ce qui a changé, ce que dit le nouveau texte (citation courte exacte), pourquoi ce verdict",
   "articles_read": [{"code": "...", "number": "...", "source_id": "...", "proposed_sha256_new": "..."}],
   "revised_minimal_correction": "si reformulée, sinon null"}],
 "alerts": [{"finding_id": "...", "classification": "...", "objection_id": null, "motif": "...", "read_in_full": true}],
 "new_findings": []}
```

Ajoute un court `reports/reexam/<GROUPE>.md` en français : synthèse, verdicts et couverture réelle. Si ton outil refuse un fichier, ne contourne pas le refus : renvoie le contenu dans ta réponse. Termine par un résumé court des verdicts.
