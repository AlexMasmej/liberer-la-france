# Brief — vérifier les défauts vus d'un seul côté

À lire **après** `BRIEF-AGENTS.md` et `BRIEF-AUDIT.md`. Leurs règles s'appliquent : lecture seule, citations exactes, aucune pièce inventée.

## Contexte

Les mêmes 1 879 articles ont été audités deux fois, avec le même critère :
- une fois sur le **texte proposé** par le projet (six audits) ;
- une fois sur le **texte officiel** au 18 octobre 2026 (audit de référence).

Certains défauts grossiers (G) n'ont été vus que d'un côté. Ton paquet les liste (`flagged_in` dit de quel côté, `description` et `evidence` décrivent le défaut). Il faut savoir si chaque défaut existe **dans les deux textes, dans un seul, ou dans aucun**.

## Pour chaque élément

1. Lis l'article avec `CITE_PRODUCTION=1 python3 -I tools/cite.py <code> <LEGIARTI>` : la source officielle **et** la proposition du projet. Lis aussi les articles visés par le défaut, dans leurs deux versions (officielle et proposée).
2. Réponds à deux questions, avec une citation exacte pour chaque réponse :
   - `present_official` : le défaut décrit est-il présent dans le **texte officiel** ? (`oui`, `non`, `incertain`)
   - `present_project` : est-il présent dans le **texte proposé** par le projet, en tenant compte des propositions des articles liés ? (`oui`, `non`, `incertain`)
3. Dis si le défaut est réellement **grossier** (un juriste le jugerait anormal) : `gross` = `oui` ou `non`.

Ne qualifie pas d'autres défauts. Ne propose pas de correction.

## Livrable

`audit/baseline/<GROUPE>.json` :

```json
{"group": "...", "items": [{"source_id": "...", "number": "...", "flagged_in": "official|project",
  "present_official": "oui|non|incertain", "present_project": "oui|non|incertain", "gross": "oui|non",
  "evidence_official": "...", "evidence_project": "...", "note": "..."}]}
```

Termine par un résumé court : décompte des réponses. Revue IA : ce n'est pas une validation par un juriste.
