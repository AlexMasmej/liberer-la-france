# Brief complémentaire — revue de fond d'un domaine prioritaire

À lire **après** `BRIEF-AGENTS.md`, dont toutes les règles s'appliquent : lecture seule, `cite.py` obligatoire, interdits absolus, discipline de qualification, format des livrables.

Les dossiers précédents ont examiné le domaine seulement par des alertes de renvois et par les versions futures. Ta mission est différente : une **revue de fond** de la réforme du domaine. Il faut établir si l'ensemble des propositions, lues avec les articles laissés inchangés, produit le résultat annoncé :
- sans trou ni double imposition ;
- sans réintroduction par renvoi, déclaration ou calendrier ;
- sans contournement facile ;
- sans perte de droits acquis ;
- sans risque constitutionnel ou européen non traité.

## Méthode attendue

1. **Orientation.** Lis l'orientation exacte du domaine :
   - `policy-coordinations.json` et `site-summaries.json` ;
   - le dossier `snapshots/20261026T230545Z/coordinations/<domaine>/` s'il existe ;
   - les mesures nommées (par exemple `cvae_removal`), à retrouver dans l'instantané par `grep -rl`.

   Énonce l'orientation en quelques lignes, avec les citations exactes.
2. **Périmètre.** Construis la liste des articles du domaine à partir de l'orientation, des lots propriétaires et d'une recherche dans `articles.content_xml` et `drafts.proposed_xml` (versions courantes au 18 octobre 2026 et versions futures). Publie cette liste avec le statut de seconde passe de chaque article.
3. **Lecture.** Lis en entier, avec `cite.py`, chaque article central du domaine, source et proposition. Lis aussi, au moins par échantillon motivé, les articles qui y renvoient.
4. **Mécanique.** Vérifie la mécanique d'ensemble : assiette, fait générateur, taux, exonérations et faveurs conservées, obligations déclaratives supprimées sans remplacement, entrée en vigueur et transitions, droits acquis et échéances anciennes, affectations de recettes et compensations, dispositifs anti-abus. Vérifie aussi la cohérence avec les autres codes du corpus (CSS, CCH, urbanisme, travail) et les risques constitutionnels (égalité devant l'impôt, incompétence négative, rétroactivité) et européens (directive mère-fille, ATAD, Pilier 2, libertés de circulation, aides d'État).
5. **Contournement.** Cherche les effets involontaires et les contournements plausibles.

## Ne pas compter deux fois

Avant de créer une objection, cherche dans `reports/register.json` les objections existantes qui portent sur les mêmes articles. Les identifiants déjà repérés pour ton domaine figurent dans la consigne.

Si ton constat est le même, ne crée pas d'objection : cite l'identifiant existant dans le rapport, à la section « Objections existantes confirmées, précisées ou contredites ». Crée une objection seulement pour un constat nouveau, ou pour une contradiction d'une objection existante ; dans ce cas, mets le champ `relates_to` à l'identifiant concerné.

## Livrables

- `reports/dossiers/DOM-<X>.md` et `reports/dossiers/DOM-<X>.json`, avec les identifiants `RT-DOM<X>-NN`.
- Le rapport doit comporter :
  - une section « Orientation et résultat obtenu » qui dit clairement si la réforme du domaine, telle que rédigée dans l'instantané, atteint son objectif ;
  - une section « Couverture réelle » : les articles lus en entier et les articles non lus.

Si ton outil d'écriture refuse un fichier `.md`, **ne contourne pas** le refus. Renvoie le contenu complet dans ta réponse finale ; le coordinateur l'enregistrera.
