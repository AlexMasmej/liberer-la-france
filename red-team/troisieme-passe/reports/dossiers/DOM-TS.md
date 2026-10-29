# DOM-TS : suppression de la taxe sur les salaires (revue de fond)

Instantané : `snapshots/20261026T230545Z` (corpus au 18 octobre 2026). Revue réalisée le 26 octobre 2026 par un agent d'IA de la troisième passe. Elle ne vaut pas validation par un juriste. Les conclusions restent provisoires : la seconde passe continue, et plusieurs articles du périmètre sont encore `pending`.

Objections nouvelles : 4 (RT-DOMTS-01 à 04), soit 1 P1 à confirmer et 3 P2 confirmés. Fichier : `reports/dossiers/DOM-TS.json`.

## 1. Orientation et résultat obtenu

### Orientation (citations exactes)

- `policy-coordinations.json`, fiscalité : « Supprimer prospectivement la taxe sur les salaires selon taxe_sur_les_salaires_removal, avec droits anciens, affectations résiduelles et prélèvements autonomes préservés ; une seule mesure dédupliquée. »
- Mesure `taxe_sur_les_salaires_removal` (`measure_id` : `taxe-sur-les-salaires-suppression`) :
  - champ : « Toutes rémunérations versées dès entrée en vigueur de la loi de suppression, quelle que soit leur période de travail ; taux normal, majorations et taux DOM supprimés pour ces versements. Aucun nouvel impôt de remplacement. » ;
  - périodes anciennes : « Année mixte : rémunérations nouvelles hors assiette et tranches, seuils annuels non proratisés. Modalités annuelles déjà allégées369/374 conservées. » ;
  - recettes sociales : « L131-8 : affectations aux branches […] conservées uniquement sur recettes anciennes réellement recouvrées et leurs régularisations. Aucun produit fictif, pourcentage redistribué ou compensation créée. » ;
  - budget : « Examiner séparément les obligations de compensation et les lois financières nécessaires, sans inventer une recette ni conditionner silencieusement l'abolition à un financement non décidé. » ;
  - régimes autonomes : « Ne pas abolir les cotisations, IR/PAS, PEEC, contribution formation, amendes logement ou leur procédure par simple suppression du renvoiTSA. »
- `site-summaries.json` [2], ideas[2] : « Supprimer cette taxe employeur, distincte des cotisations sociales, pour les rémunérations versées après l'entrée en vigueur. Elle concerne surtout les employeurs peu ou pas soumis à la TVA. Retirer les déclarations et acomptes exclusivement liés à cette taxe. Garder les exonérations et allègements pour les rémunérations anciennes. » La rubrique finance du même bloc ajoute : « distinguer la perte brute de recettes sociales et le solde public consolidé […] aucun autofinancement n'est présumé. »
- Il n'existe pas de dossier `coordinations/` propre à ce domaine. La mesure n'est citée que dans `policy-coordinations.json` et dans un lot (`automatic-impots-annexe-2/00008.json`). Les propositions centrales sont réparties dans `poursuite-20261020-b-reviewed`, `automatic-impots`, `automatic-impots-annexe-2/-3`, `automatic-securite-sociale`, `automatic-construction-habitation`, `automatic-travail`, `successions` et `cvae-removal`.

### Résultat

**Pour la taxe elle-même, l'objectif est atteint dans le texte.** La proposition de CGI 231 (LEGIARTI000054370158) :
- fixe la bascule à la date du versement, quelle que soit la période de travail ;
- supprime taux normal, majorations et taux DOM ;
- interdit tout rétablissement par renvoi et toute formalité exclusivement destinée à la taxe ;
- protège les rémunérations anciennes : liquidation, exonérations, franchise, décote, abattement, restitutions, recours, conditions européennes, loi répressive plus douce ;
- règle l'année mixte sans prorata des seuils ;
- conserve de façon autonome les champs et les procédures des prélèvements distincts (III).

Les articles d'exécution sont bornés de façon cohérente : exonérations 231 A à 231 bis V, 1679, 1679 A, 1679 bis, 1681 septies, 1929 quater, 1649 quater B quater, annexes II 142 à 144 et 383, annexes III 39, 39 B, 51, 53 à 53 ter, 344-0 B, 369 et 374. Il en va de même des prélèvements autonomes : PEEC (CCH L313-1 et L371-4), contribution formation des non-salariés (R6331-47), amendes logement (L302-16-2) et exonérations sportives (1655 septies). La déduplication est respectée : seul 231 est classé `material_reduction`, les autres articles TS sont `coordination_only`.

**Restent ouverts :**
1. Le traitement financier de la perte d'une recette entièrement affectée à la sécurité sociale (RT-DOMTS-01, P1 à confirmer) : compensation de L131-7 et compétence exclusive de la LFSS (LO111-3-15 et LO111-3-16). Ni le véhicule ni la compensation ne sont tranchés. L'orientation exige pourtant cet examen séparé.
2. Une contradiction rédactionnelle sur la liquidation de l'année mixte, à l'annexe II 143 (RT-DOMTS-02).
3. Une date indéterminée (« la présente loi ») pour le passage au versement annuel, aux annexes III 369 et 374 (RT-DOMTS-03).
4. Les versions futures déjà publiées (2027, 2029, 2030) de 231, 231 A, 231 bis L, 1649 quater B quater, 1681 septies, 1929 quater et L302-16-2, qui n'ont pas de proposition. Elles sont déjà couvertes par RT-XCUT-01, RT-FUTFISC-01/07/15/33 et RT-INTEG-03 (voir § 6). Pour la taxe elle-même, la clause « Aucun renvoi […] ne peut rétablir ce prélèvement » neutralise leur effet.
5. Les textes hors corpus : LPF, code rural (L716-2, R716-28), LOLF, formulaires 2501/2502/2460.

Il n'a été trouvé ni double imposition, ni perte de droits acquis, ni réintroduction effective de la taxe.

## 2. Périmètre (liste et statut de seconde passe)

Construction : orientation ; recherche dans `articles.plain_text` et `drafts.proposed_xml` (versions dont la fin de validité est postérieure au 18 octobre 2026) des motifs « taxe sur les salaires », « article 231 » (hors ter, quater, bis et A), « 231 du code général », « 1679 A », « taxes assises sur les salaires » et « rapport d'assujettissement » ; puis ajout des articles financiers liés (L131-7, LO111-3-15/16/18, L241-2).

| code | numéro | version | validité | brouillon | seconde passe |
|---|---|---|---|---|---|
| cgi | 231 | LEGIARTI000054370158 | 2026-07-01 → 2027-01-01 | rewrite_draft | completed |
| cgi | 231 | LEGIARTI000054567303 | 2027-01-01 → 2999-01-01 | — | not_in_inventory |
| cgi | 231 A | LEGIARTI000051203013 | 2025-02-16 → 2027-01-01 | rewrite_draft | completed |
| cgi | 231 A | LEGIARTI000054567345 | 2027-01-01 → 2999-01-01 | — | not_in_inventory |
| cgi | 231 bis D | LEGIARTI000027565898 | 2013-06-17 → | rewrite_draft | completed |
| cgi | 231 bis I | LEGIARTI000006303786 | 1997-04-11 → | rewrite_draft | completed |
| cgi | 231 bis L | LEGIARTI000006303790 | 1983-07-10 → 2027-01-01 | rewrite_draft | completed |
| cgi | 231 bis L | LEGIARTI000053154609 | 2027-01-01 → | — | not_in_inventory |
| cgi | 231 bis N, P, Q, R, S, U, V | 032701654, 018619609, 033805452, 006303803, 018619606, 030701106, 031768756 | en vigueur | rewrite_draft | completed |
| cgi | 1679 | LEGIARTI000026950015 | 2014-01-01 → | rewrite_draft | pending |
| cgi | 1679 A | LEGIARTI000054373070 | 2026-07-01 → | rewrite_draft | pending |
| cgi | 1679 bis | LEGIARTI000006313545 | 2005-01-01 → | rewrite_draft | pending |
| cgi | 1679 bis B | LEGIARTI000037387236 | 2019-01-01 → | retained_unchanged | pending |
| cgi | 1655 septies | LEGIARTI000046868436 | 2023-01-01 → | rewrite_draft | pending |
| cgi | 1681 septies | LEGIARTI000051764486 / 049473827 | → 2030 / 2030 → | rewrite_draft / — | pending / not_in_inventory |
| cgi | 1649 quater B quater | LEGIARTI000051764508 / 053188914 / 049473689 | → 2027 / 2027–2030 / 2030 → | rewrite_draft / — / — | pending / not_in_inventory |
| cgi | 1929 quater | LEGIARTI000044072896 / 053189078 / 054591306 | → 2027 / 2027–2029 / 2029 → | rewrite_draft / — / — | pending / not_in_inventory |
| cgi | 90 | LEGIARTI000006314115 | 1987-08-10 → | rewrite_draft | completed |
| cgi | 231 ter | LEGIARTI000054713030 | 2026-08-20 → | rewrite_draft | completed |
| cgi | 1599 quater C | LEGIARTI000054373125 | 2026-07-01 → | rewrite_draft | pending |
| a2 | 142, 143, 144, 383 | 037094692, 054363256, 054363249, 022179520 | en vigueur | rewrite_draft | completed |
| a3 | 39, 39 B, 51, 53, 53 bis, 53 ter | 053218832, 034737239, 006296889, 006298625, 022343100, 006298626 | en vigueur | rewrite_draft | completed |
| a3 | 53 quater | LEGIARTI000006298627 | 1979-07-01 → | retained_unchanged | completed |
| a3 | 344-0 B | LEGIARTI000053732969 / 053189893 | 2026-03-31 → (doublon DILA) | rewrite_draft / — | completed / not_in_inventory |
| a3 | 369, 374 | LEGIARTI000026848794, 025624827 | en vigueur | rewrite_draft | completed |
| css | L131-8 | LEGIARTI000053538201 | 2026-02-01 → | rewrite_draft | completed |
| css | L131-7 | LEGIARTI000051285503 / 053278888 | 2026-01-01 → / 2025-12-31 → (doublon, RT-INV-14) | rewrite_draft / — | completed / not_in_inventory |
| css | L241-2 | LEGIARTI000046805562 | 2023-01-01 → | rewrite_draft | completed |
| css | LO111-3-15, -16, -18 | 045354445, 045354454, 045354464 | 2022-09-01 → | retained_unchanged | completed |
| cch | L313-1 | LEGIARTI000038610274 | 2020-01-01 → | rewrite_draft | completed |
| cch | L371-4 | LEGIARTI000052093580 | 2026-01-01 → | rewrite_draft | completed |
| cch | L302-16-2 | LEGIARTI000042857903 / 054567273 | → 2027 / 2027 → | rewrite_draft / — | completed / not_in_inventory |
| cch | L302-6 | LEGIARTI000037670601 | 2018-11-25 → | rewrite_draft | completed |
| travail | L3332-22, L5123-5, L5428-1 | 006903066, 037075030, 054334605 | en vigueur | retained_unchanged | pending |
| travail | L5134-31, L6332-17, R6331-47 | 053278893, 037387500, 045987495 | en vigueur | rewrite_draft | pending |
| travail | L3242-1 | LEGIARTI000006902858 | 2008-05-01 → | retained_unchanged | pending |

Il n'existe plus en vigueur, dans les cinq codes, d'article CSS (L241-2, L241-6, etc.) qui vise nommément la taxe sur les salaires, hors L131-8. Les ressources des branches y renvoient de façon générique.

## 3. Méthode

- Lecture de tous les articles centraux avec `tools/cite.py`, source et proposition, NOTA, motif et notes. Les sorties sont dans `evidence/cited/20261026T230545Z/`.
- Requêtes en lecture seule (`mode=ro`, `query_only`) sur `corpus.sqlite` pour le périmètre.
- Recherche dans `reports/register.json` des objections existantes sur les mêmes articles, avant toute création.
- Contrôle de la mécanique : fait générateur, assiette et tranches, année mixte, franchise, décote et abattement, formalités, recouvrement et privilèges, affectations, renvois autonomes, versions futures, compétence financière.
- Aucun script de production, `snapshot.py` ou `sealed_evidence.py` n'a été lancé. Aucune source extérieure n'a été consultée en ligne.

## 4. Mécanique d'ensemble (constats sans objection, sauf renvoi)

- **Fait générateur et champ.** La date du versement est le seul critère (231 I). Les exonérations 231 A à 231 bis V reproduisent ce critère mot pour mot, avec la même transition. 231 bis I, L et N gardent en outre les coordinations du contrat unique. Rien ne s'écarte de la bascule.
- **Année mixte.** 231 II, 1679 A, 143 et 144 de l'annexe II, ainsi que 51, 53 bis et 53 ter de l'annexe III, excluent les rémunérations nouvelles et ne proratisent ni les seuils, ni la franchise (1 200 €), ni la décote (jusqu'à 2 040 €), ni l'abattement (24 256 €). Seul l'ancien mécanisme de prorata de 143 n'est pas neutralisé : voir **RT-DOMTS-02**. 374 de l'annexe III ventile les crédits budgétaires communs de l'État sans prorata mensuel : la règle est cohérente.
- **Formalités.** Aucune donnée ni déclaration propre à la taxe n'est demandée pour les rémunérations nouvelles : 231 I, 90, annexe III 39 (1° c et 2° e et g), 39 B, 344-0 B 5°, 1649 quater B quater XIV et 1681 septies 1 et 5. Les formalités communes (IR, DSN, PEEC) subsistent, conformément à l'orientation. Aucune formalité de remplacement n'est créée.
- **Recouvrement et procédure.** 1679, 1679 bis, 1929 quater et annexe II 383 sont bornés à l'ancien portefeuille. Les renvois procéduraux d'autres régimes sont figés « à la veille de la suppression » par 231 III, ce qui couvre les amendes de L302-16-2. Le renvoi de 231 ter VIII et de 1599 quater C VIII aux « règles applicables en matière de taxe sur les salaires jusqu'au 31 décembre 2003 » est statique : il n'est pas touché.
- **Prélèvements autonomes.** PEEC (L313-1) : le champ est défini de façon autonome par la qualité d'employeur et la territorialité de 231 « à la veille de la suppression », et les exonérations liées à la TVA ne dispensent pas de la participation. Cette rédaction est conforme au droit actuel tel que la note le décrit. L'exclusion agricole est figée sur le a du 3 de 231 ancien. Mayotte (L371-4) : l'adaptation transitoire ne renaît pas. R6331-47 fige la notion de « salaires » du 1 de 231. L6332-17 (OPCO) ne prend plus en charge que la taxe ancienne. 1655 septies V borne le a du 2° du I.
- **Affectations.** L131-8 1° ne répartit que les recettes anciennes et leurs régularisations, sans recette fictive. Les fractions de 58,35, 10,74, 24,77 et 6,14 % totalisent 100 %. L241-2 IV pose la règle générale de non-rétablissement. La compensation et le véhicule financier ne sont pas traités : **RT-DOMTS-01**.
- **Contournement.** Puisque le critère est la date de versement, un employeur peut différer après la bascule le versement de primes dont la date est libre. L'orientation l'accepte (« quelle que soit leur période de travail »). Le salaire lui-même reste payé une fois par mois (travail L3242-1, maintenu sans changement), ce qui borne l'effet à la seule période de transition. Ce point n'appelle pas d'objection. Le texte n'offre aucun autre contournement : la taxe disparaît pour tous.
- **Constitution et droit européen.** La suppression est générale : pas de sélectivité au sens des aides d'État, et aucune rupture d'égalité. L'exigence de l'article 15 du RGEC pour les taux DOM est conservée pour les rémunérations anciennes (231 II). Seul risque identifié : la compétence de la loi de financement (RT-DOMTS-01).
- **Renvois aux subdivisions supprimées.** L'annexe II 383 (« 1 et 2 bis de l'article 231 ») et 142 (« seuils […] figurant à l'article 231 ») renvoient à des subdivisions qui disparaissent du nouveau 231. Leurs propositions ne s'appliquent qu'aux rémunérations anciennes, régies par l'ancien texte (231 II). Simple remarque, sans objection.

## 5. Constats (objections nouvelles)

### RT-DOMTS-01 — P1, risque juridique, à confirmer : compensation et véhicule financier de la suppression non tranchés

- **Articles** : CGI 231 (LEGIARTI000054370158) ; CSS L131-8 (LEGIARTI000053538201), L131-7 (LEGIARTI000051285503), LO111-3-15, LO111-3-16, LO111-3-18.
- **Constat.** La taxe sur les salaires est entièrement affectée aux branches par L131-8 1°. Le projet la supprime et borne l'affectation aux recettes anciennes, conformément à l'orientation. Mais il laisse intactes trois règles :
  - L131-7 I 1° : « toute mesure de réduction ou d'exonération de contribution affectée aux régimes » donne lieu à compensation intégrale par l'État. Les notes de L131-7 précisent seulement que le III « n'étend pas sa condition préalable à la suppression de la taxe sur les salaires ». Le II n'exclut pas cette suppression.
  - LO111-3-16 II 1° : seules les lois de financement peuvent créer des réductions non compensées de « contributions affectées ».
  - LO111-3-15 : la répartition entre branches d'une ressource de l'État qui leur est affectée relève de la seule LFSS. La réécriture de L131-8 1° touche cet article.
- **Conséquence.** Le texte admet deux lectures : compensation automatique par l'État, ou perte nette pour les branches. S'y ajoute un risque de censure si la suppression non compensée ou L131-8 figure hors LFSS. Les notes de 231 renvoient les lois financières « hors lot ».
- **Incertitude.** La qualification d'un impôt d'État affecté au regard de ces notions de « contribution » n'est pas vérifiée (jurisprudence non consultée).

### RT-DOMTS-02 — P2, incohérence du projet, confirmé : l'ancien prorata de l'annexe II 143 n'est pas neutralisé pour l'année mixte

- **Article** : annexe II 143 (LEGIARTI000054363256), avec 142 et CGI 231.
- **Constat.** 143 ancien calcule la majoration sur la rémunération de toute l'année, puis applique un prorata selon la « période d'application de la majoration ». Il plafonne aussi les droits « ajustée à l'année ». La proposition conserve ces « règles de régularisation annuelle des majorations, les plafonnements » pour les rémunérations anciennes, puis pose la règle contraire pour l'année mixte.
- **Exemple.** Salaire de 3 000 € par mois, bascule au 1er juillet : la majoration due est de 372,77 € selon 231 II, et d'environ 1 017 € selon l'ancien 143.
- **Effet.** La loi (231 II) devrait prévaloir, mais le règlement reste contradictoire.

### RT-DOMTS-03 — P2, incohérence du projet, confirmé : « la présente loi » dans les annexes III 369 et 374

- **Constat.** Le passage au versement annuel et la fin des relevés s'appliquent aux échéances postérieures à « l'entrée en vigueur de la présente loi ». Cette date se distingue de celle de la « loi portant suppression ». Dans une annexe réglementaire, ce texte n'est pas identifiable. S'il s'agit de la loi de suppression, l'allègement « déjà décidé » est presque sans objet.

### RT-DOMTS-04 — P2, simple alerte, confirmé : exonérations sans terme dans le code du travail

- **Constat.** L3332-22, L5123-5 et L5428-1 (retained_unchanged, pending) gardent une exonération de taxe sur les salaires sans terme. Les mêmes exonérations sont bornées dans le CGI (231 bis D et S) et dans L5134-31. L'effet juridique est nul, car 231 I interdit tout rétablissement par renvoi. Seules la lisibilité et l'unité de méthode sont en cause.

## 6. Objections existantes confirmées, précisées ou contredites

- **RT-P1-ANNEXES-13** (CGI 90, note « Annexe III, art. 369 à 374 ») : **confirmée**. La note figure inchangée dans la proposition de 90, qui y ajoute une phrase sur les formalités de la taxe sur les salaires.
- **RT-P1-CSS-A-19** (L131-8 3° ter non borné) : **confirmée**. L131-8 1° est correctement borné, le 3° ter ne l'est pas. Pas de doublon avec RT-DOMTS-01, qui porte sur la compensation et la compétence.
- **RT-FUTFISC-07** (231, version 2027) : **confirmée et précisée**. La version 2027 (LEGIARTI000054567303) ne diffère de la version actuelle que par le renvoi aux plafonds de franchise TVA du CIBS : L. 233-9 et L. 233-10, alors qu'une version mort-née LEGIARTI000053154595 portait L. 223-9 et L. 223-10. La proposition supprime ce passage pour l'avenir et 231 II couvre les versements anciens. Il n'y a pas de réintroduction si la loi de réforme réécrit « l'article 231 » après le 1er janvier 2027. La réserve d'une entrée en vigueur au même jour (LFI 2027) demeure.
- **RT-FUTFISC-33** : **confirmée**. Les notes de 231 lisent ABROGE_DIFF comme une abrogation dont « la note ne donne pas le texte de reprise ». La version successeur, de même numéro, est pourtant dans l'instantané. Même lecture dans les notes de 231 A et 231 bis L.
- **RT-FUTFISC-01** (231 A et 231 bis L : renvois aux articles 256 C, 271 et 261, recodifiés au CIBS en 2027) : **confirmée** pour le domaine.
- **RT-FUTFISC-15, RT-FUTFISC-32, RT-INTEG-03, RT-XCUT-01** : **confirmées**. Les versions 2027 et 2030 de 1649 quater B quater (XIV) et 1681 septies (5), et les versions 2027 et 2029 de 1929 quater, gardent des mentions non bornées de la taxe sur les salaires et n'ont pas de proposition. Pour la taxe elle-même, l'effet est neutralisé par 231 I. Les bornes doivent néanmoins être reportées sur ces versions.
- **RT-FUTTL-02** (L302-16-2 : abrogation supposée au 1er janvier 2027) : **confirmée**. Le renvoi au recouvrement de la taxe sur les salaires « à la veille de sa suppression » est, lui, cohérent avec 231 III.
- **RT-P1-CGI-C-10** (231 ter et 1599 quater C) : **confirmée sans changement**. Aucun lien avec la taxe sur les salaires au-delà du renvoi statique de 2003.
- **RT-INV-14** (doublon DILA de L131-7) : constaté à nouveau. La proposition porte sur LEGIARTI000051285503.

**Alertes écartées** (aucune objection créée) :
- 1679 bis B : le 3 renvoie à L6362-12 du code du travail, soit les règles des taxes sur le chiffre d'affaires, non à la taxe sur les salaires. Le maintien est correct.
- L302-6 : l'amende « recouvrée comme en matière de taxe sur les salaires » est abrogée avec l'article. Les sanctions définitives restent régies par leurs règles.

## 7. Propositions de correction (présentées séparément)

### C-01 (RT-DOMTS-01) — Trancher la compensation dans une loi de financement, sans conditionner la suppression

**Option A**, conforme à l'orientation « aucune compensation créée ».

CSS L131-7, II : ajouter un 3° :

> « 3° À la suppression de la taxe sur les salaires prévue à l'article 231 du code général des impôts pour les rémunérations versées à compter de l'entrée en vigueur de la loi qui la prévoit. »

Article non codifié de la LFSS :

> « La suppression de la taxe sur les salaires prévue à l'article 231 du code général des impôts n'est pas compensée aux branches mentionnées au 1° de l'article L. 131-8 du code de la sécurité sociale. Ses effets sur leurs recettes sont retracés dans les prévisions de recettes et les tableaux d'équilibre de la présente loi. »

**Option B** : laisser L131-7 I s'appliquer et inscrire la compensation en loi de finances.

**Justification.** L'orientation impose d'examiner séparément compensation et lois financières, sans inventer de recette. Les options A et B rendent le choix explicite. Dans les deux cas, la réécriture de L131-8 1° est votée en LFSS (LO111-3-15). La suppression elle-même peut y figurer (LO111-3-7 1°).

**Dépendances** : L131-7 III (CSG, C3S, retraites) n'est pas modifié. LO111-3-18 s'applique.

### C-02 (RT-DOMTS-02) — Annexe II 143, troisième alinéa de la proposition

Ajouter à la fin :

> « Pour cette année, la période antérieure à cette entrée en vigueur n'est pas une période d'application partielle de la majoration au sens des deuxième à quatrième alinéas de la rédaction antérieure du présent article. Les droits dus au titre de la majoration sont déterminés en appliquant les taux de 4,25 % et de 9,35 % aux fractions de la seule rémunération versée à chaque salarié avant cette date qui sont comprises entre les limites applicables pour l'année en vertu du 2 bis de l'article 231 du code général des impôts dans sa rédaction antérieure, ou qui excèdent la limite supérieure, sans rapport de rémunérations ni ajustement à l'année. »

**Justification** : aligner le règlement sur 231 II. **Dépendances** : 142 (calcul mensuel provisoire), 144 et 383, sans changement.

### C-03 (RT-DOMTS-03) — Annexe III 369 et 374

Remplacer « de la présente loi » par la désignation du texte qui introduit le versement annuel, avec sa date. Si ce texte est la loi de suppression, l'écrire expressément. Variante : fixer une date propre au versement annuel, antérieure à la suppression, sans restitution des échéances déjà payées.

### C-04 (RT-DOMTS-04) — Code du travail L3332-22, L5123-5 et L5428-1

Lors de leur seconde passe, borner la seule mention de la taxe sur les salaires sur le modèle de L5134-31 (rédaction type dans le JSON). Les exonérations d'impôt sur le revenu et de cotisations restent inchangées.

## 8. Couverture réelle

**Lus en entier (source, NOTA, proposition, motif, notes) — 57 versions :**
- CGI : 231 (LEGIARTI000054370158, 054567303 ; versions historiques imprimées et parcourues seulement), 231 A (2 versions), 231 bis D, I, L (2 versions), N, P, Q, R, S, U et V, 1679, 1679 A, 1679 bis, 1679 bis B, 1655 septies, 1681 septies (2 versions), 1929 quater (version courante), 90.
- Annexe II : 142, 143, 144, 383.
- Annexe III : 39, 39 B, 51, 53, 53 bis, 53 ter, 53 quater, 344-0 B (2 versions), 369, 374.
- CSS : L131-8, L131-7 (2 versions), L241-2, LO111-3-15, LO111-3-16, LO111-3-18.
- CCH : L313-1, L371-4, L302-16-2 (2 versions), L302-6.
- Code du travail : L3332-22, L5123-5, L5134-31, L5428-1, L6332-17, R6331-47, L3242-1.

**Lus partiellement** (passages pertinents seulement) :
- CGI : 1649 quater B quater (3 versions, XIV et motif), 1929 quater (versions 2027 et 2029, 1), 231 ter (structure, VII à X, motif et notes), 1599 quater C (VIII et notes), 1647 (III à V), 235 ter C (sans lien avec le domaine).
- CSS : LO111-3 à LO111-3-14 et LO111-3-17 (par requête).

**Non lus** : LPF (droit de reprise, procédure) ; code rural (L716-2, R716-28) ; CGCT ; LOLF (art. 2 et 36) ; CIBS (L. 233-9, L. 233-10, L. 234-2) ; doctrine BOI ; formulaires 2501, 2502 et 2460 ; CSS L136-1, L130-1 et L242-1 ; travail L6331-48 et L6331-53 ; CGI 1384 F, 1764, 406 terdecies et 235 bis ; jurisprudence du Conseil constitutionnel sur LO111-3-16.

## 9. Incertitudes restantes

- Qualification de la taxe sur les salaires au regard de L131-7 I 1° et LO111-3-16 : RT-DOMTS-01 reste « à confirmer ».
- Territorialité du champ autonome de la PEEC : elle est d'origine jurisprudentielle et doctrinale, alors que le renvoi figé vise « l'article 231 et ses textes d'application ». La portée de ce renvoi à la doctrine n'est pas vérifiée.
- Seize versions du périmètre sont `pending` en seconde passe : 9 au CGI (1679, 1679 A, 1679 bis, 1679 bis B, 1655 septies, 1681 septies, 1649 quater B quater, 1929 quater, 1599 quater C) et 7 au code du travail. Les versions futures n'ont pas de proposition. Toute conclusion peut changer.
- Aucune consultation de Légifrance, d'EUR-Lex ni du Conseil constitutionnel n'a été faite. Les références hors corpus restent des réserves documentaires.
