# Brief — audit par échantillon aléatoire : ce qu'un juriste trouverait

À lire **après** `BRIEF-AGENTS.md`. Ses règles s'appliquent : lecture seule, interdits absolus, citations exactes, aucune pièce inventée. Ce brief change ta mission.

## Objectif

Mesurer la proportion d'articles où **un juriste qui ouvre l'article** trouverait un défaut grossier. Tu ne cherches pas l'exhaustivité juridique. Tu lis comme un praticien qui connaît la matière : il ouvre l'article, ses renvois et ses textes d'application, et il juge.

## Indépendance

- **Ne lis pas** `reports/register.json`, `reports/` ni les dossiers des passes précédentes **avant** d'avoir qualifié un article. Ton jugement doit être indépendant.
- **Après** ta qualification, et seulement alors, cherche dans `reports/register.json` si le défaut était déjà connu (`known_objection`). Une objection close (`résolu`) dont le défaut est encore visible compte comme un défaut présent.

## Texte à lire : la production actuelle

Les corrections du 29 octobre sont appliquées en production. Lis toujours avec :

```sh
CITE_PRODUCTION=1 python3 -I tools/cite.py <code> <numéro|LEGIARTI>
```

L'outil lit la production en lecture seule. Codes : `css`, `cgi`, `travail`, `urba`, `cch`, `a1` à `a4` (annexes I à IV du CGI). Pour chercher les articles qui renvoient à un numéro, interroge la base de production en lecture seule :

```sh
sqlite3 "file:/Users/alexandremasmejean/.codex/.chatgpt-projects/g-p-6ad59c015c308191aa21cba63c71a6dc/legal-rewrite/corpus.sqlite?mode=ro"
```

Tables utiles :
- `articles(code_id, id, number, state, valid_from, valid_until, content_xml)` ;
- `drafts(code_id, source_id, status, proposed_xml, reason, review_notes)`.

## Pour chaque article de ton paquet

1. **Lis l'article en entier** : source en vigueur au 18 octobre 2026, proposition (ou source maintenue si `retained_unchanged`), motif et notes, ainsi que ses versions futures s'il en a (`VIGUEUR_DIFF`). Le texte qui compte est celui que le projet propose. Pour un article maintenu, c'est la source.
2. **Lis ses liens directs** :
   - les articles auxquels il renvoie : leur proposition actuelle ;
   - pour un article législatif, les décrets et annexes qui l'appliquent : cherche son numéro dans `content_xml` et `proposed_xml` du même code ;
   - pour un article réglementaire, sa base légale.

   Lis au moins les trois liens les plus importants. Au-delà, dis ce que tu n'as pas lu.
3. **Qualifie l'article** :
   - `G` (**défaut grossier**) : un juriste le remarquerait et le jugerait anormal. Voir les familles F1 à F9 ci-dessous.
   - `m` (**défaut mineur**) : notes ou motifs erronés, rédaction maladroite sans effet, redondance, doute raisonnable à confirmer.
   - `0` : rien à signaler.

   Donne au moins une citation exacte, avec son identifiant LEGIARTI, pour tout `G` ou `m`.
4. **Famille** du défaut (un ou plusieurs codes) :
   - **F1** : la loi supprime une formalité, une obligation ou un dispositif, mais un décret, une annexe ou un autre article le maintient ou l'organise encore ;
   - **F2** : une sanction (amende, délit, contravention, majoration) survit à l'obligation qu'elle sanctionne, ou vise un dispositif supprimé ;
   - **F3** : renvoi mort, ou renvoi vers un article abrogé par le projet sans neutralisation, ou renvoi décalé (mauvais alinéa) ;
   - **F4** : une version future déjà publiée, sans proposition, rétablit ou écrase la réforme ; ou une proposition affirme à tort une abrogation (lecture d'`ABROGE_DIFF`) ;
   - **F5** : contradiction interne ou entre deux articles, hors F1 ;
   - **F6** : transition absente ou fautive : rétroactivité, perte de droits acquis, instances en cours ;
   - **F7** : texte défectueux : tronqué, numérotation cassée, phrase incohérente, tableau amputé ;
   - **F8** : contraire à une orientation du projet, par exemple un impôt ou une formalité recréés, ou une faveur supprimée sans décision ;
   - **F9** : droit supérieur (Constitution, droit de l'Union), toujours « à confirmer » sans source primaire ;
   - **F10** : notes ou motifs seulement (toujours `m`).
5. **Défaut nouveau.** Si le défaut est `G` et nouveau (`known_objection` vide), rédige une correction minimale alignée sur les orientations : moins de contraintes, aucune formalité de remplacement, droits acquis conservés. Mets-la dans `suggested_correction`. Ne l'applique pas.

## Livrable

Écris `audit/<GROUPE>.json` :

```json
{"group": "...", "read_from": "production",
 "articles": [{"sample_id": "S001", "code": "...", "number": "...", "source_id": "...",
   "verdict": "G|m|0", "families": ["F1"], "description": "...",
   "evidence": "citations exactes avec l'identifiant LEGIARTI",
   "links_read": ["..."], "links_not_read": "...",
   "known_objection": null, "suggested_correction": null}]}
```

Écris aussi `audit/<GROUPE>.md`, court et en français : décompte G, m et 0 ; liste des G avec une phrase chacun ; familles observées. Termine par un résumé court. Revue IA : ce n'est pas une validation par un juriste.
