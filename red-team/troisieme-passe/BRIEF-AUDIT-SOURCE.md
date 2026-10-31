# Brief — audit de référence : le droit officiel tel qu'il est

À lire **après** `BRIEF-AGENTS.md` et `BRIEF-AUDIT.md`. Leurs règles s'appliquent : lecture seule, interdits absolus, citations exactes, aucune pièce inventée. Ce brief change ce que tu lis.

## Objectif

Les six audits ont mesuré la proportion d'articles **proposés par le projet** où un juriste trouverait un défaut grossier. Cet audit mesure la même chose sur le **droit officiel**, tel qu'il est en vigueur au 18 octobre 2026, sans le projet. Il sert de point de comparaison. La méthode est la même : **les mêmes 1 879 articles**, répartis dans les mêmes paquets, avec le même critère et la même qualification. Seul le texte lu change : le droit officiel au lieu de la proposition.

## Ce que tu lis, et ce que tu ne lis pas

- **Tu lis uniquement le texte officiel**, avec la commande suivante :

  ```sh
  CITE_PRODUCTION=1 CITE_SOURCE_ONLY=1 python3 -I tools/cite.py <code> <numéro|LEGIARTI>
  ```

  Elle affiche la source officielle, les NOTA et toutes les versions, mais **masque** la proposition, le motif et les notes du projet. Ton paquet ne dit pas non plus si l'article a été réécrit : ne cherche pas à le savoir.
- **Tu ne lis rien du projet** :
  - ni les colonnes `proposed_xml`, `reason` et `review_notes` de la table `drafts` ;
  - ni les lots (`batches/`), ni `reports/`, ni `apply/` ;
  - ni les autres fichiers de `audit/`, ni les fichiers sous `evidence/cited/` qui ne finissent pas par `-source-only`.
- Pour une recherche dans la base, interroge seulement la table `articles` (colonnes `content_xml`, `number`, `state`, `valid_from`, `valid_until`) et la table `documents`, en lecture seule.

## Pour chaque article de ton paquet

1. **Lis l'article officiel en entier** : version en vigueur au 18 octobre 2026, NOTA et versions futures publiées.
2. **Lis ses liens directs dans leur version officielle**, au moins les trois plus importants :
   - les articles auxquels il renvoie ;
   - pour un article législatif, les décrets et annexes qui l'appliquent ;
   - pour un article réglementaire, sa base légale.

   Dis ce que tu n'as pas lu.
3. **Qualifie-le** G, m ou 0, avec **le même critère que les six audits** : un juriste qui ouvre l'article, ses renvois et ses textes d'application le jugerait-il anormal ? Donne une citation exacte avec l'identifiant LEGIARTI pour tout G ou m.

## Familles, appliquées au droit officiel

- **F1** : la loi ne prévoit plus une formalité, une obligation ou un dispositif, mais un décret ou une annexe l'organise encore.
- **F2** : une sanction vise une obligation supprimée ou un article abrogé.
- **F3** : renvoi mort (article abrogé, sans transition), décalé (mauvais alinéa) ou erroné.
- **F4** : un article affirme à tort qu'un autre est abrogé, ou s'appuie sur un texte qui a cessé d'exister.
- **F5** : contradiction entre deux dispositions (hors F1).
- **F6** : transition absente ou fautive.
- **F7** : texte défectueux : tronqué, numérotation cassée, phrase incohérente, tableau amputé.
- **F9** : droit supérieur (Constitution, droit de l'Union), toujours « à confirmer » sans source primaire.

Les familles **F8** (contraire aux orientations du projet) et **F10** (notes et motifs du projet) **ne s'appliquent pas**.

**Ne compte pas comme un défaut :**
- une réforme officielle déjà publiée qui entrera en vigueur plus tard (`VIGUEUR_DIFF`, `ABROGE_DIFF`) : c'est le calendrier normal du droit, sauf si elle laisse un renvoi mort ou une contradiction réelle ;
- un renvoi qui vise une rédaction antérieure dans une disposition transitoire ;
- un renvoi à un texte hors corpus, quand rien n'indique que ce texte a disparu.

## Livrable

Écris `audit/baseline/<GROUPE>.json`, avec le même format que les autres audits :

```json
{"group": "...", "read_from": "official-source",
 "articles": [{"sample_id": "O001", "code": "...", "number": "...", "source_id": "...",
   "verdict": "G|m|0", "families": ["F3"], "description": "...",
   "evidence": "citations exactes avec l'identifiant LEGIARTI",
   "links_read": ["..."], "links_not_read": "..."}]}
```

Écris aussi `audit/baseline/<GROUPE>.md`, court et en français : décompte G, m et 0 ; liste des G avec une phrase chacun ; familles observées.

Termine par un résumé court. Revue IA : ce n'est pas une validation par un juriste.
