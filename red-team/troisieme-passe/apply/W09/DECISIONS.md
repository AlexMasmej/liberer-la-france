# W09 : décisions du balayage (troisième passe)

J'ai lu la production en lecture seule (`CITE_PRODUCTION=1 tools/cite.py`, sqlite `mode=ro`). Les preuves sont sous `evidence/cited/production-20261029/`. Le détail de chaque piste, avec ses citations, est dans `audit/sweeps/W09.json`.

## Bilan

- **Volume :** 50 articles, 61 pistes, toutes dans le code du travail.
- **Qualification :**
  - 35 déjà réglées ;
  - 16 faux positifs ;
  - 1 défaut mineur (m) ;
  - 9 défauts grossiers (G), tous corrigés.
- **Corrections :** 9 lignes dans `apply/W09/changes.json`, soit 6 `replace` et 3 `new`.
- **Contrôle :** `python3 -B apply/check_changes.py W09` donne `problems: []`, 9 lignes construites et 9 validées.
- **Diagnostics :** ils sont tous voulus. Ce sont les renvois retirés (R2145-7, L6331-54, L8112-5), le renvoi D1142-2 remplacé par D1142-2-1 et les réductions déclarées de D1142-14 et D1142-6-1.
- **Sur les corrections :** aucune ne crée de formalité, de sanction, d'impôt ou de condition. Aucune ne touche à une orientation politique.

## Corrections faites (G)

| Article (version) | Piste | Famille | Correction |
|---|---|---|---|
| R23-113-3 (LEGIARTI000034524060) | S8 | F3 | **Défaut :** le texte renvoie aux limites « du I de l'article R. 2145-7 ». Cet article est abrogé depuis le 29 octobre 2018 (LEGIARTI000033442168) et aucun article ne reprend son barème. C'est un conflit de source hérité.<br>**Correction :** les trois limites sont reprises mot pour mot : 50 € par mois jusqu'à 300 €, six fractions jusqu'à 1 200 €, douze au-delà.<br>**Mises à jour :** motif, notes, `substantive_impact` (un effet ajouté) et `benefit_review`. |
| R6313-1 (LEGIARTI000038014099), maintenu | S8 | F3 | **Défaut :** le texte renvoie à « L. 6331-48 et L. 6331-54 ». L6331-54 est abrogé depuis le 1er janvier 2018, et L6331-48 couvre déjà les artisans.<br>**Correction :** le renvoi mort est retiré. L'article passe à `coordination_only`. |
| R1263-11-1 (LEGIARTI000042168312), maintenu | S8 | F3 | **Défaut :** le texte renvoie à « L. 8112-1 ou L. 8112-5 ». L8112-5, sur les contrôleurs, est abrogé depuis le 1er juillet 2016, et L8112-1 vise inspecteurs et contrôleurs.<br>**Correction :** le renvoi mort est retiré. |
| R6251-1 (LEGIARTI000037872712), maintenu | S7 | F3 | **Défaut :** le texte vise le « dernier alinéa de l'article L. 6211-2 ». La proposition de L6211-2 ajoute un dernier alinéa transitoire.<br>**Correction :** le renvoi vise le « sixième alinéa », c'est-à-dire le contrôle pédagogique. C'est le même décompte que R6222-23-1 officiel, qui place les 25 % au cinquième alinéa. Le renvoi est exact avant et après la réforme. |
| L5135-2 (LEGIARTI000042674215), maintenu | S7 | F3 | **Défaut :** le 4° ter vise le « dernier alinéa de l'article L. 6313-6 ». La proposition de L6313-6 ajoute un dernier alinéa sur le contrat unique, qui ne désigne aucun organisme.<br>**Correction :** le renvoi vise le « sixième alinéa », sur la préparation à l'apprentissage. La numérotation « 4° ter », visée par CSS L412-8, ne change pas. |
| L1237-18-3 (LEGIARTI000042683521), maintenu | S7 | F3 | **Défaut :** le texte vise le « dernier alinéa de l'article L. 1233-72 ». La proposition de L1233-72 ajoute deux alinéas, alors que le régime de L5122-4 reste au troisième.<br>**Correction :** le renvoi vise le « troisième alinéa », comme la proposition de CSS L222-2-1. |
| D1142-7, version du 1er mars 2029 (LEGIARTI000047548327), `new` | S5 | F4 | **Défaut :** la version suivante, de texte identique, n'avait pas de proposition. Elle rétablissait le renvoi erroné à D1142-2.<br>**Correction :** la proposition est reprise mot pour mot, avec ses `substantive_impact` et contrôles. |
| D1142-14, version du 1er mars 2029 (LEGIARTI000047548269), `new` | S5 | F4 | **Défaut :** sans proposition, le forfait de deux PMSS par salarié et par mois serait rétabli au 1er mars 2029.<br>**Correction :** la réduction est reportée (`normative_reduction`, même `removed_provisions`). |
| D1142-6-1, version du 1er mars 2029 (LEGIARTI000047548343), `new` | S5 | F4 | **Défaut :** sans proposition, les objectifs par indicateur sous 85 points seraient rétablis.<br>**Correction :** l'abrogation est reportée (`full_repeal`, même `repeal_scope`). |

Les quatre corrections de R6313-1, R1263-11-1, R6251-1 et L5135-2 suivent le précédent de W04 (CSS R644-3) : l'article passe de maintenu à coordonné, sans autre changement. Pour ces cinq articles maintenus (avec L1237-18-3), les notes qui disaient la cible « absente du corpus » ou citaient l'ancien ordinal sont corrigées.

## Une ligne par piste

**Déjà réglées (35)**
- R3124-2 et R3124-1 (S1 et S2, L3121-40) : la plage s'arrête à L3121-39, avec loi pénale plus douce.
- R7213-12 (L3141-29).
- L1255-7 (S2, L1251-12-1) : champ temporel et plafonds abrogés non sanctionnables.
- L6523-2-1 (S8, L6331-54) : renvoi neutralisé, « lorsqu'il est applicable ».
- D2261-4-5 (L2261-27-1).
- D1233-44, D1233-43, D1233-40 et D1233-37 (L1237-19-9, -10 et -11) : volet RCC limité aux accords antérieurs.
- R2312-60 (S8, R6322-66) : références bornées aux situations résiduelles.
- R4741-4 (S1 et S2, L4532-12) : 1° abrogé et loi plus douce.
- R1524-4 (L1221-11).
- R1323-1 (S2, R1321-2).
- D1151-1 (L1153-5-1) : 4° abrogé à la même date.
- D1272-4 (L1242-13).
- Annexe du référentiel qualité (L6231-3) : conseil facultatif.
- R6232-1 et R6233-1 (L6231-3, -5 et -7) : renvoi ramené à L6231-2 et L6231-4.
- R1263-7 (L1251-46).
- R5221-45 (L5221-9).
- R4641-8 et R4641-4 (L4622-9-3) : missions des 3° et 5°.
- L6355-24 (S2, L6331-69 et L6331-6) : renvois bornés aux périodes antérieures.

**Faux positifs (16)**
- Renvois ordinaux toujours exacts. L'alinéa ajouté est une transition finale, ou l'ordinal visé est inchangé :
  - D3123-3 et D4163-25 (L3123-26, troisième alinéa) ;
  - L4131-2 (L4132-2, premier alinéa) ;
  - D4154-3 (L4154-1, second alinéa) ;
  - L1232-6 (L1332-2, dernier alinéa) ;
  - R8272-9 (L8272-2, cinquième alinéa, visé dans sa rédaction antérieure) ;
  - D1142-4 et D1142-8 (D1142-5, troisième alinéa).
- Renvois à un autre code :
  - L4163-13 (CSS L351-6-1) ;
  - R6227-2 (code rural L713-2) ;
  - L7342-2 et D7342-2 (CSS L743-1).
- Bornes de plage abrogées, la plage gardant des articles en vigueur : L1225-71 (L1225-69) et R6261-1 (R6261-14).
- Versions suivantes sans reprise de la réforme :
  - R4451-61 (2027) : le texte ne nomme plus l'IRSN ;
  - L5524-2 (2028) : l'adaptation du 3° a disparu.

**Défaut mineur non corrigé (1)**
- L3422-5, version 2028 (LEGIARTI000054468615), F3 hérité.
  - **Défaut :** cette version garde « b) Le a du 2° », alors que le a et le b de L3152-4 forment un alinéa commun aux 1° et 2°. Le sens reste univoque.
  - **Pourquoi non corrigé :** son a) est tronqué (RT-FUTTL-20), et le report a déjà été écarté pour pièce manquante (RT-FUTTL-09).

## Points pour l'auteur

1. **R23-113-3.** Le barème de l'ancien R2145-7 I est écrit en clair. Une autre lecture tiendrait le renvoi pour figé à sa version de 2017 : le résultat est le même. Les stipulations conventionnelles de l'ancien R2145-7, liées à la convention de L2145-6, ne sont pas reprises : elles ne concernaient pas les CPRI. Aucune retenue passée n'est remise en cause.
2. **Hors paquet, signalés sans être touchés :**
   - D1142-16, version de 2029 (LEGIARTI000047548234). Elle n'a pas de proposition, alors que la version en vigueur (LEGIARTI000045669624, paquet W10) en a une. Elle est à reporter de la même façon si elle n'est pas traitée par W10.
   - CSS L222-2-1, version suivante (LEGIARTI000054466881). Elle n'a ni proposition ni groupe attribué, et garde « au dernier alinéa de l'article L. 1233-72 », que la proposition en vigueur (W06) corrige en « troisième alinéa ». Ce renvoi décalé reviendrait à son entrée en vigueur.
   - R6261-1. La plage officielle « R. 6261-2 à R. 6261-14 » ne couvre pas R6261-15 à R6261-20, en vigueur depuis 2019. C'est le texte officiel ; je ne l'ai pas modifié.
3. **Notes périmées (F10, m), non corrigées car les articles ne sont pas modifiés :**
   - L3121-40 dit que R3124-1 et R3124-2 « conservent la plage ».
   - L4131-2 dit que D4132-1 et D4132-2 ne sont pas coordonnés.
   - D1233-37 et D1233-40 disent que D1233-43 n'est pas limité.
   - Le motif de L1232-6 dit que L1332-2 n'a « pas encore cette exception ».
   - Chacune des notes de R4641-4 et R4641-8 dit l'autre non coordonné.
   - R2312-60 et L6523-2-1 disent leurs cibles « absentes du corpus », alors qu'elles y figurent comme ABROGE.
4. **Méthode.** Pour constituer les lignes de base, j'ai lu une fois les lignes de lot de production avec la fonction de lecture `review_prior.batch_owners`, celle qu'utilise `check_changes.py`, sans aucune écriture. Les lots ont aussi été lus directement en JSON.

Revue IA : ce n'est pas une validation par un juriste.
