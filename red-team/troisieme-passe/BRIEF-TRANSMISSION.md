# Brief — points transmis par la seconde passe

À lire **après** `BRIEF-AGENTS.md`. Toutes ses règles s'appliquent : lecture seule, `cite.py` obligatoire, interdits absolus, orientations de réforme à préserver, discipline de qualification.

## Contexte

La seconde passe est terminée : 30 314 articles relus. Son auteur a transmis à la troisième passe une liste de points encore ouverts : `inputs/transmission-seconde-passe-20261029.md`. Lis ce fichier en entier. C'est une **information à vérifier**, pas une conclusion : la seconde passe se relit elle-même, et la troisième passe est indépendante.

La liste **n'est pas exhaustive**, de l'aveu même de son auteur. L'absence d'un point dans la liste ne prouve pas qu'il est réglé.

Documents d'entrée :
- l'index `snapshots/20261029T034912Z/notes-contradictions/INDEX.md` et le guide `snapshots/20261029T034912Z/GUIDE-TROISIEME-PASSE.md` ;
- pour les points CPF et apprentissage, la dernière relecture acceptée, copiée dans `inputs/review-travail-LEGIARTI000018522505-00001.answer.json`. C'est un gros fichier JSON : lis-en les passages pertinents.

L'instantané courant est l'instantané final `snapshots/20261029T034912Z/` ; `cite.py` le lit.

Consignes de la transmission que tu appliques, parce qu'elles rejoignent les règles de `BRIEF-AGENTS.md` :
- lire en entier les sources, NOTA, propositions, motifs, contreparties et transitions ;
- distinguer quatre cas : contradiction confirmée, coordination nécessaire, différence de champ, pièce manquante ;
- ne pas rouvrir une correction déjà intégrée sur la seule foi d'anciennes notes. Une objection fondée sur une note supersédée doit être vérifiée sur le texte final.

## Ta tâche

Pour chaque point de ton paquet :
1. Lis en entier, avec `cite.py`, chaque article cité par le point, source et proposition finales, ainsi que les articles qui en dépendent directement.
2. Qualifie le point :
   - `contradiction confirmée` ;
   - `coordination nécessaire` ;
   - `différence de champ` ;
   - `pièce manquante` ;
   - `non confirmé` ;
   - `résolu dans le texte final`.

   Appuie chaque qualification sur une courte citation exacte et l'identifiant LEGIARTI.
3. Cherche dans `reports/register.json` les objections existantes sur les mêmes articles. Remonte les fusions (`_merged_into`) jusqu'à l'objection vivante.
   - Si une objection couvre le point, cite-la : ne crée pas de doublon. Son réexamen sur le texte final est fait par un autre groupe ; ne rends pas de verdict sur elle.
   - Si aucune ne le couvre et que le défaut est confirmé, rédige une objection au format de `BRIEF-AGENTS.md`, avec l'identifiant `RT-TR<GROUPE>-NN`, `origin: "transmission seconde passe, point <n>"` et `relates_to` si utile.
4. Propose une correction minimale qui préserve les réformes, les exonérations, les avantages futurs et les droits acquis, et qui ne rétablit aucune formalité supprimée.
5. N'invente jamais le contenu d'un arrêté, d'un modèle CERFA, d'une figure ou d'un texte extérieur absent du corpus. Marque le point `pièce manquante` ou `à confirmer`.

## Livrable

Écris `reports/transmission/<GROUPE>.json` :

```json
{"group": "...", "snapshot": "20261029T034912Z",
 "points": [{"point": "1a", "summary": "...",
   "qualification": "...", "evidence": "citations courtes exactes, avec l'identifiant LEGIARTI",
   "articles": [{"code": "...", "number": "...", "source_id": "...", "proposed_sha256": "..."}],
   "register_ids": [], "minimal_correction": "...", "new_objections": []}]}
```

Ajoute un court `reports/transmission/<GROUPE>.md` en français : un paragraphe par point, avec la couverture réelle. Si ton outil refuse un fichier, ne contourne pas le refus : renvoie le contenu dans ta réponse. Termine par un résumé court.
