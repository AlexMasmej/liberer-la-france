# Dossier CIBS — annexe III 171, ancien CGI 435 et CIBS L313-6 : base juridique, concordance et transitions

Red-team juridique indépendante, troisième passe. Instantané : `snapshots/20261026T230545Z`. Date de référence du corpus : **18 octobre 2026**. Rapport établi le 26 octobre 2026 (lectures locales et consultations publiques entre 23:00Z et 23:25Z environ). Cette revue est faite par une IA : elle ne vaut pas validation par un juriste. La seconde passe continue : les propositions citées peuvent encore changer.

## 1. Résumé

- **Base juridique au 18 octobre 2026.** L'annexe III 171 (LEGIARTI000006298919, état VIGUEUR depuis le 2006-01-01) est un texte d'application des 2° des I et II de CGI 435. Dans sa version 2002-03-31 → 2022-01-01 (LEGIARTI000006309896), CGI 435 renvoyait expressément « à un seuil fixé par décret » et à des « conditions également fixées par décret ». Ce CGI 435 a été abrogé par l'ordonnance n° 2021-1843, art. 10 (lien ABROGE du XML ; borne LEGI 2022-01-01). Le CIBS L313-6 (LEGIARTI000044603571), créé par la même ordonnance, pose lui-même les deux critères dans la loi. La version lue est celle du 18 mars 2026 ; il ne renvoie à aucun décret. Conséquence : depuis le 1er janvier 2022, 171 n'a plus de disposition législative à appliquer pour les impositions nées sous le CIBS. Il garde seulement une fonction pour les droits régis par l'ancien droit (anciens CGI 435/438). LEGI le présente toujours comme « VIGUEUR » : c'est une survivance formelle, pas un fondement actuel. Je n'ai pas obtenu la version du 18 octobre 2026 de L313-6, ce qui forme une réserve documentaire (RT-CIBS-05).
- **Proposition courante pour 171** (proposition `31619282…`, identique à celle des preuves scellées de 17h07). Elle conserve intégralement les deux critères, le seuil inclusif de 3 bar et l'anhydride carbonique en solution. Elle retire le renvoi à CGI 435 du corps et ne renvoie à aucun texte abrogé comme fondement actuel. En revanche, elle transforme 171 en **définition réglementaire autonome**, sans champ déterminé (« les catégories fiscales auxquelles elle est applicable ») et sans fondement législatif actuel. Cette définition coexisterait avec la définition législative de L313-6 et ne s'articule pas avec le CIBS (RT-CIBS-01, P1). Sa clause transitoire est imprécise (RT-CIBS-02, P2). Sa dernière phrase qualifie à tort de « directement applicables » des définitions qui, en matière d'accise sur le vin, résultent d'une directive (RT-CIBS-03, P2).
- **Anomalie.** Les notes de revue de 171 (et de 178) affirment que CGI 435 (et 438) sont absents du corpus. Ils sont présents dans l'instantané : six versions de 435, dont celle de 2002-2022 abrogée par l'ordonnance (RT-CIBS-04, P2).
- **Aucune équivalence CIBS/UE n'est déclarée.** La convergence des deux critères matériels est constatée sur des textes lus en entier. Les introductions, les champs (« présente section » / « 2° des I et II de 435 » / NC et titres de la directive), les versions et les transitions ne sont pas réputés équivalents. Les liens CONCORDANCE (171→L313-6 ; 435→L313-2, L313-6, L313-15) restent des pistes.

Objections : **1 P1** (confirmé), **4 P2** (2 confirmés, 2 à confirmer), **1 faux positif** écarté.

## 2. Périmètre réellement lu

### 2.1 Instantané, par `tools/cite.py`, en entier

Pour chaque article : source, NOTA, bornes, état, proposition, motif, notes, lot et statut d'inventaire. Les fichiers sont sauvegardés sous `evidence/cited/20261026T230545Z/`.

| Code | Numéro | Version | Bornes | État | Proposition | Inventaire |
|---|---|---|---|---|---|---|
| a3 | 171 | LEGIARTI000006298919 | 2006-01-01 → 2999-01-01 | VIGUEUR | rewrite_draft (lot `automatic-impots-annexe-3/00033.json`, index 2) | completed |
| a3 | 170 | LEGIARTI000006300055 | 2005-07-06 → 2006-01-01 | TRANSFERE | aucune | not_in_inventory |
| cgi | 435 | LEGIARTI000048274309, 049423340, 049582304, 006309894, 006309895, **006309896** | 1950 → 2022-01-01 (dernière : 2002-03-31 → 2022-01-01, ABROGE) | historique | aucune | not_in_inventory |
| cgi | 438 | LEGIARTI000043662369 | 2021-06-12 → 2022-01-01 | ABROGE | aucune | not_in_inventory |
| cgi | 1613 bis | LEGIARTI000053282843 | 2025-12-31 → 2999-01-01 | VIGUEUR | retained_unchanged | pending |
| a3 | 178 | LEGIARTI000006298930 | 1979-07-01 → 2999-01-01 | VIGUEUR | rewrite_draft (même lot 00033) | completed |
| a3 | 111-0 A | LEGIARTI000006299038 et 006299039 | — | — | retained_unchanged | completed |

J'ai aussi lu le XML LEGI complet de 171, 170 et 435 (2002-2022) : contexte, versions, NOTA vide et liens. La proposition, le motif et les notes de 171 ont des empreintes identiques à l'objet capturé dans `evidence/sealed/runtime/cibs-alcohol-public-followup-20261026T1707Z/whole-current-and-historical-inputs-two-RO.json` (`31619282…`). La ligne du lot propriétaire de l'instantané porte `prior_proposal_sha256 = 921a3704…`.

### 2.2 Recherche des renvois (base en lecture seule, `mode=ro`, `query_only`)

- Liens XML de tous les documents ARTICLE vers les identifiants des versions de CGI 435, vers 171 et vers 170, ou portant les mentions « CGI 435 » ou « CGIAN3 171 ». Liens trouvés uniquement dans : les versions de 435 elles-mêmes (CITATION vers 171) ; CGI 438 (toutes versions, jusqu'au 2022-01-01) ; CGI 443 (2000-2003) ; CGI 1613 bis (liens de citation hérités jusqu'à la version 2022-2024, dont le texte ne cite plus 435) ; a3 171 et a3 170.
- Recherche textuelle de « 435 » et de « 171 » dans toutes les versions des sources du CGI et des annexes I à IV, après filtrage du bruit numérique. Résultat : **aucun texte en vigueur au 18 octobre 2026 ne renvoie à l'annexe III 171 ni à CGI 435**. Les mentions de « l'article 435 » dans a3 437, 438 et 444 visent l'ancien article 435 de l'annexe III (commission), abrogé en 2012. C'est un autre texte (numéro recyclé).
- Recherche dans toutes les propositions, motifs et notes (`drafts`) de « 435 », « 171 de l'annexe III », « mousseu » et « 313-6 ». Seule 171 traite de cette définition. 178 reprend le même constat erroné d'absence de 435/438. Les autres occurrences de « vins mousseux » (a3 111-0 A, 111 I ; a4 50 octies, 50-0 E, 50-0 L, 50-0 M, 54-0 D, 54-0 L, 54-0 M, 54-0 AB, 54-0 BW) emploient la catégorie sans renvoyer à 171 : ce ne sont pas des renvois exprès. Les occurrences « L313-6 » concernent d'autres codes (urbanisme, CCH, travail).

### 2.3 Preuves scellées lues

- `evidence/sealed/runtime/alcohol-2006-normative-followup-20261026T1600Z/` : REPORT, CONTROL, documentary-intent, qualification and limits, coverage, remaining requirements, reçus de refus (JO index 403, recherche 403, PDF cache miss), différence de source, journal de capture, reconstruction entière F/170/171. J'ai aussi lu dans le texte affiché du décret n° 2006-356 : le préambule (« Vu … l'article 11 de la loi n° 51-247 »), les articles 1 à 4 et le passage de l'article 3 relatif à 170 (lignes L1303–L1305). Les grandes captures de la base (`whole-current-and-historical-inputs-two-RO.json`, `whole-file-input-stability.json`) n'ont été utilisées que pour le contrôle d'empreinte de 171. Je les ai relues sur l'instantané par `cite.py`.
- `evidence/sealed/runtime/cibs-alcohol-public-followup-20261026T1707Z/` : REPORT, CONTROL, limites, qualification, exigences restantes, liaison de concordance, et reçus intégraux (section L313-6 à L313-18 au 18 mars 2026, recherche d'index, contexte L111-3 et refus).
- `evidence/sealed/runtime/cibs-2021-primary-pistes-followup-20261026T1808Z/` : tous les fichiers, dont les deux reçus de recherche (art. 1, 10, 22, 30, 40, 41 indexés de l'ordonnance 2021-1843, 302 D bis, L111-3, L111-5).

### 2.4 Consultations publiques (26 octobre 2026, sans contournement)

| Heure (UTC, approx.) | URL | Résultat |
|---|---|---|
| 23:14Z | `https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044603571/2026-10-18` | HTTP 403 |
| 23:15Z | `https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000044598647/2026-10-18/` | HTTP 403 |
| 23:14–23:16Z | EUR-Lex `CELEX:01992L0083-20220101` (TXT et TXT/HTML), `eli/dir/1992/83/oj/fra`, `LexUriServ … 31992L0083:FR:HTML`, `CELEX:32020L1151` | pages vides pour l'outil (aucun contenu), sans tentative de contournement |
| 23:16Z | recherche web (directive 92/83/CEE art. 8 et 12) | pistes seulement : réponse ministérielle AN QE 9011 (16e lég.), pages EUR-Lex non lues |
| 23:17Z | `https://www.legislation.gov.uk/eudr/1992/83/section/II` et `/section/III` | **résumés** (l'outil a refusé la reproduction intégrale) du texte de l'UE tel qu'en vigueur au 31 décembre 2020, version britannique « retained », pas EUR-Lex |

D'après la source britannique, l'article 8 (vin mousseux) combine trois éléments : des codes NC 2204 10, 2204 21 10, 2204 29 10 et 2205 ; le bouchon champignon maintenu par attaches ou liens **ou** une surpression de CO2 en solution de trois bar ou plus ; un titre supérieur à 1,2 % et au plus 15 % vol, avec un alcool entièrement d'origine fermentaire. L'article 9 prévoit une assiette à l'hectolitre de produit fini, un taux uniforme par catégorie avec faculté d'un même taux tranquille/mousseux, et des taux réduits jusqu'à 8,5 % vol. L'article 12, point 2 (autres boissons fermentées mousseuses), combine NC 2206 00 91 et certaines positions 2204/2205 non couvertes par l'article 8, le même critère alternatif bouchon/3 bar, et un titre de 1,2 à 13 % vol, ou de 13 à 15 % vol si l'alcool est entièrement fermentaire. Ces lectures ne certifient **pas** le texte de l'UE en vigueur au 18 octobre 2026 : je n'ai pas vérifié l'effet de la directive (UE) 2020/1151, applicable à partir de 2022.

## 3. Méthode

1. Lecture entière, par `cite.py`, des sources, propositions, motifs et notes. Lecture du XML LEGI complet des articles pivots.
2. Recherche des renvois exprès par les liens XML, puis recherche textuelle filtrée dans toutes les versions et dans toutes les propositions. Les numéros recyclés sont écartés par code et identifiant.
3. Reconstitution de la chaîne normative : CGI 435 (2002) → décret → a3 170 (décret n° 2005-758, art. 3) → transfert à 171 (décret n° 2006-356, art. 3) → abrogation de 435 (ordonnance n° 2021-1843, art. 10) → CIBS L313-6.
4. Comparaison des champs : celui de 171 source, celui de 171 proposé, celui de L313-6 (version du 18 mars 2026) et celui des articles 8 et 12 de la directive (source secondaire au 31 décembre 2020). Aucune équivalence n'est déduite de la ressemblance des mots.
5. Qualification d'un seul constat par contradiction, sans double comptage entre 171 et ses renvois.

## 4. Constats

### RT-CIBS-01 — P1 — risque juridique (base légale, compétence, coordination avec le CIBS) — confirmé

**Faits.**
- 171 source : « Pour l'application du 2° des I et II de l'article 435 du code général des impôts, les vins, les boissons ou les produits fermentés mousseux sont ceux qui… ». C'est l'exécution d'une habilitation : CGI 435 (LEGIARTI000006309896) I 2° vise une « surpression dépassant un seuil fixé par décret » et des bouteilles « fermées dans des conditions également fixées par décret ». Le II 2° est identique pour les produits ou boissons fermentés mousseux.
- 435 a été abrogé par l'ordonnance n° 2021-1843, art. 10 (lien `ABROGE`, borne 2022-01-01). L'article 40 indexé de l'ordonnance fixe l'entrée en vigueur au 1er janvier 2022. L'article 41 indexé précise que, pour le régime général d'accises, l'ordonnance s'applique aux impositions dont « l'exigibilité intervient à compter de cette même date ».
- CIBS L313-6 (version du 18 mars 2026) : « Par dérogation à l'article L. 111-3, pour l'application de la présente section, une boisson mousseuse s'entend d'une boisson qui répond à l'une des deux conditions suivantes : 1° … bouchon champignon maintenu à l'aide d'attaches ou de liens ; 2° … surpression … égale ou supérieur à 3 bars. » Le critère est dans la loi, sans renvoi à un décret.
- 171 proposé : « Les vins, boissons ou produits fermentés mousseux sont ceux qui… » puis « À compter de l'entrée en vigueur de la loi portant la présente réforme, cette définition ne vaut que pour le classement des produits dans les catégories fiscales auxquelles elle est applicable. »

**Raisonnement.**
- Depuis le 1er janvier 2022, plus aucune disposition législative ne charge un décret de fixer le seuil de pression ou les conditions de fermeture. Pour l'accise sur les alcools, la notion est définie par L313-6 lui-même. L'annexe III 171 n'est donc pas un texte d'application du CIBS. Pour les impositions exigibles depuis 2022, elle est privée d'objet et de base légale, même si LEGI la laisse en « VIGUEUR ».
- La proposition supprime l'ancrage à 435 mais garde une définition réglementaire générale. Son champ (« les catégories fiscales auxquelles elle est applicable ») est circulaire et ne peut viser que l'une de deux choses :
  - les catégories fiscales de L313-15 du CIBS : un décret redéfinirait alors une notion de l'assiette déjà définie par la loi, sans habilitation (compétence législative pour l'assiette des impositions) ;
  - aucune catégorie : la phrase est vide.
- Dans les deux cas, la proposition crée une seconde définition parallèle, sans hiérarchie expresse avec L313-6.
- Les champs diffèrent, même si les deux critères matériels convergent :
  - 171 vise « les vins, les boissons ou les produits fermentés » ;
  - L313-6 vise toute « boisson » pour la seule section 3 du chapitre III, par dérogation à L111-3 (nomenclature combinée) ; il sert aussi aux seuils de L313-17 (8,5 % vol pour les boissons mousseuses) ;
  - les articles 8 et 12 de la directive combinent NC, titre et critère alternatif.
- Je ne conclus à aucune équivalence. Je constate seulement que la proposition ne choisit pas entre ces champs.

**Conséquences.** Insécurité sur le texte qui gouverne le classement mousseux/tranquille, dont dépendent des tarifs distincts : sous l'ancien droit, CGI 438 1° fixait 9,68 €/hl pour les vins mousseux contre 3,91 €/hl pour les autres vins. Une exception d'illégalité est possible contre 171 s'il est invoqué pour une imposition CIBS. Le motif « Retirer un critère modifierait le classement fiscal » ne justifie pas le maintien d'une définition réglementaire générale : le classement CIBS ne dépend pas de 171 depuis 2022.

**Ce qui n'est pas en cause.** Les deux critères, le seuil inclusif de 3 bar et le CO2 en solution sont repris. Aucun renvoi à un texte abrogé n'est présenté comme fondement actuel. Aucune charge nouvelle n'est créée. La décision de ne pas réduire le critère est saine.

### RT-CIBS-02 — P2 — risque juridique (transition) — à confirmer

**Faits.**
- La proposition indique : « Elle ne crée aucun prélèvement, n'étend aucune assiette et ne remet pas en vigueur le droit auquel renvoyait le 2° des I et II de l'article 435 », puis « Pour les périodes antérieures relevant de ces dispositions, elle conserve sa portée antérieure. »
- Le 2° des I et II de 435 ne renvoie à aucun « droit ». Il définit des catégories de produits et renvoie au décret. Le droit concerné était le droit de circulation de CGI 438 (LEGIARTI000043662369, abrogé au 2022-01-01).
- La bascule d'application est fixée au 1er janvier 2022, sur le critère de l'exigibilité pour les accises (art. 41 indexé). La proposition, elle, ne parle que de « l'entrée en vigueur de la loi portant la présente réforme ».

**Raisonnement.** La clause sauve bien la portée ancienne, et le corps conserve les critères. Elle laisse pourtant trois ambiguïtés :
- le texte abrégé (sans « pour l'application du 2° des I et II de 435 ») reste-t-il porteur des conditions de NC et de titre que la loi ancienne y attachait ?
- la limite des « périodes antérieures » est-elle la date de la réforme ou le 1er janvier 2022 ?
- elle mentionne un « droit » auquel 435 ne renvoyait pas.

Une lecture pourrait laisser croire que 171 a gouverné des impositions entre 2022 et la réforme. Effet limité : les critères sont matériellement repris et L313-6 s'applique par sa propre force.

**À préserver.** Les droits et contentieux des droits de circulation exigibles avant le 1er janvier 2022, les réclamations et restitutions encore ouvertes, et les décisions définitives.

### RT-CIBS-03 — P2 — risque juridique (européen) — à confirmer

**Faits.** La dernière phrase proposée : « Les définitions directement applicables du droit de l'Union européenne demeurent applicables dans leur champ propre. » Les définitions du vin mousseux et des autres boissons fermentées mousseuses figurent aux articles 8 et 12 de la directive 92/83/CEE. Une directive lie l'État quant au résultat et se transpose ; elle n'est pas « directement applicable ». La nomenclature combinée (règlement (CEE) n° 2658/87), elle, est directement applicable : L111-3 y renvoie, et L313-6 y déroge expressément.

**Raisonnement.** La phrase peut être lue comme une substitution des articles 8/12 à la définition, ce qui est inexact. Elle peut aussi être lue comme un renvoi au règlement NC, contraire à la dérogation de L313-6. Isolée de ses conditions de NC et de titre, la définition proposée pourrait, si elle était appliquée de façon autonome, qualifier de « mousseux » des produits que les articles 8 et 12 excluent (titre supérieur à 15 % vol, alcool non entièrement fermentaire). Le risque est faible tant que L313-15 et L313-17 encadrent le classement CIBS. Je n'ai pas obtenu le texte de l'UE consolidé au 18 octobre 2026 : cette phrase ne doit pas être conservée, ni une concordance CIBS/UE affirmée, sur cette seule base.

### RT-CIBS-04 — P2 — anomalie d'inventaire — confirmé

**Faits.**
- Les notes de revue de 171 (`c034d61b…`) et le champ `scope_limitations` de la ligne propriétaire disent : « CGI 435 absent du corpus public fourni, constat renouvelé ».
- Les notes de 178 (`b70f9712…`) disent : « l'absence de CGI 435/438 dans le corpus ».
- L'instantané contient six versions de CGI 435 (dont LEGIARTI000006309896, 2002-03-31 → 2022-01-01, ABROGE, avec ses liens ABROGE et CONCORDANCE) et toutes les versions de CGI 438 jusqu'à LEGIARTI000043662369 (ABROGE au 2022-01-01).

**Conséquence.** La prémisse documentaire de deux propositions est fausse au regard de l'instantané. Elle a conduit à traiter la concordance comme impossible à instruire, alors que le texte de l'habilitation abrogée est lisible. Cela ne change pas le corps des propositions. Les motifs et certificats d'impact doivent être corrigés pour ne pas propager le constat.

### RT-CIBS-05 — P2 — réserve documentaire — confirmé

Pièces non obtenues :
1. **Versions au 18 octobre 2026** de L313-6, de son contexte (L313-5, L313-15 à L313-17) et de L111-3 : 403 et inaccessibilité, déjà constatées dans les preuves scellées et à nouveau le 26 octobre à 23:14–23:15Z. Seule la version affichée au 18 mars 2026 a été lue.
2. **Évolutions 2025-2027.** Plusieurs articles de la sous-section (L313-7, L313-8, L313-12, L313-16, L313-17) et L111-3 portent une fin au 01/01/2027. Légifrance signale une ordonnance n° 2026-671 du 27 juillet 2026 et des tables « ancienne/nouvelle numérotation » au JO n° 0174 du 28/07/2026. La base locale montre aussi un titre III du CGI rebaptisé au 2027-01-01. Une vue indexée « au 01/01/2027 », explorée il y a environ quatre mois (donc probablement avant le 27 juillet 2026), affiche L313-6 sans borne de fin : ce n'est pas une preuve de son état après cette ordonnance.
3. **Texte entier de l'ordonnance n° 2021-1843** (JORFTEXT000044590225) : opérations de l'art. 10, art. 38 à 43, et existence ou non d'une clause générale de substitution des références. Seuls des extraits indexés sont disponibles.
4. **Texte français de la directive 92/83/CEE** consolidé au 18 octobre 2026 (EUR-Lex vide pour l'outil) et effet de la directive (UE) 2020/1151 sur les articles 8, 9, 12 et 13.

Toute correction qui citerait « L. 313-6 » doit attendre ces vérifications. C'est pourquoi la correction proposée ci-dessous ne cite pas le numéro.

### RT-CIBS-06 — alerte écartée (faux positif)

Les liens XML de CGI 1613 bis (versions 2010-2024) vers CGI 435 sont des liens de citation hérités. Le texte de 1613 bis en vigueur (LEGIARTI000053282843) renvoie aux catégories de L313-15 du CIBS et non à 435 ni à 171. Les mentions de « l'article 435 » dans a3 437, 438 et 444 visent un autre texte, l'article 435 de l'annexe III, abrogé en 2012. CGI 443 (abrogé en 2008) relève de l'historique. Il n'y a donc aucun renvoi entrant vivant vers 171 ou vers CGI 435 à coordonner. Le seul article dépendant est 171.

## 5. Propositions de correction (présentées séparément, non appliquées)

### C1 — Réécriture de l'annexe III 171 (corrige RT-CIBS-01, -02 et -03)

Garde de version : a3 171, LEGIARTI000006298919, source `6f0eb127…`. Elle remplace la proposition `31619282…`.

> Pour l'application du 2° des I et II de l'article 435 du code général des impôts, dans sa rédaction antérieure au 1er janvier 2022, les vins, les boissons ou les produits fermentés mousseux sont ceux qui sont présentés dans des bouteilles fermées par un bouchon « champignon » maintenu à l'aide d'attaches ou de liens ou ceux qui ont une surpression due à l'anhydride carbonique en solution égale ou supérieure à 3 bar.
>
> À compter de l'entrée en vigueur de la loi portant la présente réforme, le présent article ne s'applique qu'aux droits régis par les articles 435 et 438 du code général des impôts dans leur rédaction antérieure au 1er janvier 2022 dont l'exigibilité est intervenue avant cette date, y compris pour leur contrôle, leur recouvrement, leur contentieux et leur restitution. Il ne définit pas la notion de boisson mousseuse pour l'application du code des impositions sur les biens et services, qui relève des dispositions législatives de ce code. Il ne crée, ne rétablit ni n'étend aucune imposition.

**Justification.**
- Le corps source est conservé mot pour mot, à une seule précision temporelle près. Les deux critères, le seuil inclusif de 3 bar et le CO2 en solution sont préservés pour l'ancien droit.
- La définition réglementaire concurrente et la formule circulaire disparaissent. L'ancrage historique exact (435 et 438) est conservé.
- La formule « directement applicables » est supprimée. Aucune équivalence CIBS/UE n'est affirmée.
- Le texte ne cite pas de numéro du CIBS, ce qui le rend robuste à une renumérotation en 2027.
- La rédaction est prospective : elle ne prétend pas régir rétroactivement la période 2022-réforme.

**Dépendances.**
- Confirmer, sur le texte entier de l'ordonnance n° 2021-1843, la règle d'exigibilité de l'art. 41 et l'absence de disposition transitoire contraire (par exemple pour des stocks ou des régularisations).
- Confirmer que L313-6 ou son successeur est en vigueur et inchangé au 18 octobre 2026 et à la date d'entrée en vigueur de la réforme.
- Corriger en conséquence le motif et le `substantive_impact` de la ligne propriétaire.

### C2 — Variante : abrogation avec clause de survie

> L'article 171 est abrogé à compter de l'entrée en vigueur de la loi portant la présente réforme. Il demeure applicable, dans sa rédaction antérieure, aux droits régis par les articles 435 et 438 du code général des impôts dans leur rédaction antérieure au 1er janvier 2022 dont l'exigibilité est intervenue avant cette date.

Cette variante est plus nette sur la hiérarchie des normes, mais elle dépend d'une clause de survie bien placée dans l'acte de réforme. C1 garde le texte lisible à sa place, ce qui me paraît préférable pour la sécurité des anciens dossiers.

### C3 — Notes et motifs (corrige RT-CIBS-04)

- 171, notes de revue et `scope_limitations`. Remplacer « CGI 435 absent du corpus public fourni, constat renouvelé. » par : « CGI 435 est présent dans le corpus (six versions). La version 2002-03-31 → 2022-01-01 (LEGIARTI000006309896), abrogée par l'ordonnance n° 2021-1843, art. 10, renvoyait au décret en ses I 2° et II 2°. Depuis le 1er janvier 2022, la notion de boisson mousseuse de l'accise sur les alcools est fixée par la loi (CIBS), sans renvoi à ce décret ; aucune équivalence de champ n'est affirmée. »
- 178, notes de revue. Remplacer « l'absence de CGI 435/438 dans le corpus » par « CGI 435 et 438, présents dans le corpus dans leurs versions abrogées au 1er janvier 2022 ». Le reste de la note de 178 (décharge, droit de circulation, coordination hors lot) est inchangé et n'est pas examiné au fond ici.

## 6. À préserver

- Les deux critères alternatifs, le seuil inclusif « égale ou supérieure à 3 bar » et le CO2 « en solution ».
- La portée de 171 pour les droits de circulation et les définitions des anciens CGI 435 et 438 exigibles avant le 1er janvier 2022, y compris les réclamations, restitutions et contentieux ouverts, les délais de reprise et les décisions définitives.
- L'absence de renaissance du droit de circulation et l'absence de toute formalité ou condition de conditionnement nouvelle pour les producteurs.
- Les catégories et tarifs du CIBS, qui ne sont pas modifiés par l'annexe.
- Les acquis des propositions voisines : 178 (décharge des pertes, preuve ouverte), 1613 bis (conservé intact), 111-0 A (niveaux).

## 7. Incertitudes restantes et éléments non examinés

- Les versions du 18 octobre 2026 (CIBS L313-6 et contexte, L111-3) n'ont pas été obtenues (403). L'effet de l'ordonnance n° 2026-671 et de l'ordonnance n° 2025-1247 sur la sous-section au 1er janvier 2027 est inconnu.
- La directive 92/83/CEE a été lue seulement à travers des résumés d'une source britannique au 31 décembre 2020. Je n'ai lu ni le texte français EUR-Lex, ni la directive 2020/1151.
- L'ordonnance n° 2021-1843 n'a été lue que par extraits indexés (art. 1, 10, 22, 30, 40, 41). Une clause générale de substitution de références, si elle existe, pourrait rattacher 171 à L313-6 « par correspondance ». Elle ne rendrait pas pour autant nécessaire une définition réglementaire doublant la loi.
- Le principe d'abrogation des actes réglementaires dépourvus d'objet ou devenus illégaux par changement de droit (CRPA L243-2) est invoqué de mémoire. Le CRPA n'est pas dans le corpus et n'a pas été consulté.
- Non examinés au fond : la note de 178 sur le droit de circulation ; les textes de l'annexe IV qui emploient « vins mousseux » (capsules, couleurs, entrepôts), qui ne renvoient pas à 171 mais dont le raccordement aux catégories CIBS reste à vérifier ; les tableaux externalisés et l'arrêté du 24 mars 2006 (réserves des preuves scellées) ; les coordinations alcool déjà ouvertes à l'index (165/185/186, 302 D bis/E/F/50-0 G/H, 111-0 H/50-0 I).

Cette revue IA ne vaut pas validation par un juriste.
