# Brief — réexamen final des objections après la fin de la seconde passe (revue des différences, § D)

À lire **après** `BRIEF-AGENTS.md`. Toutes ses règles s'appliquent : lecture seule, interdits absolus, discipline de qualification. Trois points de ce brief les remplacent.

## Ce qui change

- **L'instantané courant est l'instantané final `snapshots/20261029T034912Z/`**, pris après la fin de la seconde passe.
  - L'instantané intermédiaire `20261027T044303Z` a été supprimé par rotation.
  - L'instantané final est cohérent : base = registre = lots, sans écriture en vol.
- **Les anciens textes** (instantané `20261027T044303Z`) restent disponibles dans `evidence/cited/20261027T044303Z/` : une export JSON par version citée par le registre, avec ses empreintes. Les empreintes par article des deux instantanés sont dans `manifests/20261027T044303Z.json` et `manifests/20261029T034912Z.json`.
- **Les nouveaux textes** se lisent avec `python3 -I tools/cite.py <code> <numéro|LEGIARTI>`. L'outil lit le nouvel instantané et écrit dans `evidence/cited/20261029T034912Z/`.
- **Le registre a déjà été réexaminé une fois**, sur l'instantané intermédiaire (`reports/reexam/`).
  - Le champ `previous_reexam` de ton paquet donne ce verdict et sa trace.
  - Le champ `reexam.revised_minimal_correction` de `reports/register.json` donne la correction révisée.
  - Pars de cet état, pas de l'état initial.

## Ta tâche

Tu reçois un paquet `reports/reexam-final/packet-<GROUPE>.json`. Pour chaque objection, il contient :
- les articles modifiés depuis l'instantané intermédiaire, avec les champs modifiés : proposition, statut, motif, notes, statut de seconde passe ;
- les alertes P1 liées dont l'état a changé : `before` et `after`.

Pour chaque objection :
1. Relis l'objection complète dans `reports/register.json`, y compris `reexam` s'il existe.
2. Lis **en entier** l'ancienne version (export `20261027T044303Z`) et la nouvelle version (`cite.py`) de chaque article modifié : proposition, motif, notes de revue. Vérifie aussi les autres articles de l'objection, qui peuvent avoir été touchés indirectement.
3. Classe l'objection :
   - `maintenue` : le défaut subsiste, inchangé ;
   - `reformulée` : il subsiste, mais sa forme, sa portée, sa priorité ou sa correction change ;
   - `résolue` : la nouvelle rédaction règle le défaut. Cite le passage qui le règle et vérifie qu'il ne crée pas d'effet nouveau, notamment la perte d'une faveur, une formalité ou un renvoi cassé ;
   - `obsolète` : la prémisse ne tient plus pour une autre raison.
4. **Objections déjà closes** (statut `résolu` ou `obsolète` au réexamen intermédiaire) dont les articles ont encore changé : vérifie que la résolution tient toujours.
   - Si elle tient, le verdict est `résolue` (ou `obsolète`), avec une trace courte.
   - Si le défaut est revenu, le verdict est `maintenue` ou `reformulée`, avec la priorité et le statut qui conviennent.
5. Si la nouvelle rédaction introduit un **défaut nouveau** dans le périmètre lu, signale-le sous `new_findings`, au format d'objection de `BRIEF-AGENTS.md`, avec des identifiants `RT-RX<GROUPE>-NN` (par exemple `RT-RXF03-01`).
   - Avant de créer un constat, cherche dans `reports/register.json` une objection existante sur les mêmes articles. Ne compte pas deux fois.
6. Une modification des seules notes ou du seul motif peut suffire à résoudre une objection qui portait sur une note erronée. Elle ne résout jamais un défaut du texte proposé.

**Paquets d'alertes** (`FA..`) : requalifie chaque alerte selon la méthode de `BRIEF-P1.md`. Ce sont des alertes P1 vivantes dont le texte a changé, ou qui n'avaient jamais été qualifiées. La question est de savoir si le renvoi vers une disposition abrogée par le projet pose désormais un problème réel.

## Livrable

Écris `reports/reexam-final/<GROUPE>.json` :

```json
{"group": "...", "snapshot_old": "20261027T044303Z", "snapshot_new": "20261029T034912Z",
 "objections": [{"id": "...", "verdict": "maintenue|reformulée|résolue|obsolète",
   "new_priority": "P0|P1|P2|null", "new_status": "confirmé|à confirmer|résolu|obsolète",
   "trace": "ce qui a changé, ce que dit le nouveau texte (citation courte exacte), pourquoi ce verdict",
   "articles_read": [{"code": "...", "number": "...", "source_id": "...", "proposed_sha256_new": "..."}],
   "revised_minimal_correction": "si reformulée, sinon null"}],
 "alerts": [{"finding_id": "...", "classification": "...", "objection_id": null, "motif": "...", "read_in_full": true}],
 "new_findings": []}
```

Ajoute un court `reports/reexam-final/<GROUPE>.md` en français : synthèse, verdicts et couverture réelle. Si ton outil refuse un fichier, ne contourne pas le refus : renvoie le contenu dans ta réponse. Termine par un résumé court des verdicts.
