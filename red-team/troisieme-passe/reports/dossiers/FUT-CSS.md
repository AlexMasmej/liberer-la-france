# FUT-CSS — Versions futures publiées du code de la sécurité sociale, confrontées au projet

Dossier de red-team juridique indépendante (troisième passe). Rédigé le 26 octobre 2026 sur l'instantané `20261026T230545Z`, avec pour date de référence du corpus le **18 octobre 2026**. Revue par IA, **provisoire** : elle ne vaut pas validation par un juriste. La seconde passe se poursuit en production, et les propositions citées peuvent encore changer.

Ce dossier documente, article par article, l'objection transversale **RT-XCUT-01** (XCUT.json) pour le CSS. Le cas L752-1 (version 2028 LEGIARTI000054466934, qui rétablit le renvoi à L281-4) relève de **RT-UNION-05** : il est cité ici sans être recompté.

## 1. Synthèse

- **Périmètre** : 178 lignes, soit 118 couples (version en vigueur au 18 octobre 2026 / version future VIGUEUR_DIFF) et 60 nouveaux numéros. Les 118 couples comprennent 45 rewrite_draft et 73 retained_unchanged. **177 lignes ont été lues en entier**. La seule exception est la version 2030 de L311-3 (LEGIARTI000046902997), établie par différence exhaustive ligne à ligne.
- **Qualification des 45 couples rewrite_draft** : 10 réformes écrasées, 14 conflits de rédaction, 20 sans effet (transposition seule) et 1 déjà traité (L861-3, en substance). Aucune proposition ni aucune note ne traite expressément une version future en l'intégrant.
- **Objections** : 38 au total, dont 17 P1 (15 confirmées, 2 à confirmer) et 21 P2 (14 confirmées, 7 à confirmer). Aucune n'est P0 : aucun effet n'est à la fois grave et certain dès l'entrée en vigueur d'une réforme dont la date n'est pas fixée.
- **Textes à l'origine des versions futures**, d'après les LIENS LEGI :
  - loi n° 2025-199, art. 90, et décrets n° 2026-354 et 2026-355 : réforme AT-MP au 1er novembre 2026 ;
  - ordonnances n° 2025-1247 et 2026-671 : recodification dans le CIBS au 1er janvier 2027 ;
  - LFSS 2024 (loi n° 2023-1250) et LFSS 2026 (loi n° 2025-1403) : 2027 ;
  - **ordonnance n° 2026-647 du 22 juillet 2026** (JORFTEXT000054456323, NOR TRSS2615197R) : extension du code à Mayotte au 1er janvier 2028. Elle est l'origine des 55 nouveaux numéros L751-1-1 à L759-27. Ses art. 8 et 9 créent un chapitre transitoire jusqu'au **31 mars 2036, date normative** ;
  - loi n° 2026-791 : achats de produits de santé ;
  - **ordonnance n° 2025-1091 du 19 novembre 2025** (NOR JUSD2530057R) : recodification du code de procédure pénale au 1er janvier 2029 ;
  - loi n° 2022-1726 : CVAE, 2030 ;
  - décrets n° 2012-477 et 2018-79 : versions bornées au 2222-02-22.
- **Les trois constats les plus importants** :
  1. **Des allègements du projet disparaissent pour le flux nouveau dès le 1er novembre 2026**, avant toute adoption possible (RT-FUTCSS-01, RT-FUTCSS-02, RT-FUTCSS-03). C'est le cas du versement immédiat du capital AT (L434-1), de la suppression de la commission pluridisciplinaire (R351-37 / L351-1-4) et de l'accès au rapport médical sans délai ni formulaire (R434-32).
  2. **Des prélèvements ou formalités supprimés par le projet sont re-publiés à l'identique ou aggravés** par des versions futures : contribution de 15 % sur la publicité des jeux (L137-27, 2027, RT-FUTCSS-05), condition syndicale (L138-13, RT-FUTCSS-07), pénalité de pertinence (L162-23-14-1, RT-FUTCSS-08), avis préalable (L162-23-8, RT-FUTCSS-11), obligation d'adhésion (L531-8, RT-FUTCSS-12), justification annuelle d'existence et biométrie de principe (L161-24 / L161-24-1, 2028, RT-FUTCSS-14).
  3. **Le projet perdrait des faveurs déjà publiées** s'il était voté sur la base actuelle : plafonds APA à 7,93 % puis 8,1 % (L223-9, RT-FUTCSS-13), renouvellement automatique de la complémentaire santé solidaire, applicable au plus tard depuis le 1er juillet 2026 (L861-5, RT-FUTCSS-17), plancher mahorais à 88 % du SMIC (L241-13, RT-FUTCSS-15). Inversement, le taux de CSG à 6,6 % proposé rend incalculable le taux mahorais de 2028 à 2036 (RT-FUTCSS-16).
- **Défaut de méthode transversal** (RT-FUTCSS-38) : dans 55 numéros, les notes lisent la fin de version ABROGE_DIFF comme une abrogation, ou affirment que le successeur « n'est pas fourni » alors qu'il figure dans l'instantané.

## 2. Méthode

- **Lecture.** Chaque couple a été lu par `tools/cite.py`, qui sauvegarde les preuves dans `evidence/cited/20261026T230545Z/`, et par un comparateur en lecture seule. On lit en entier la source courante, la NOTA, la proposition, le motif, les notes de revue, la version future et sa NOTA. Pour les retained_unchanged, on lit la version future, sa différence exacte avec la source, et le motif ou les notes du maintien. Les textes créateurs sont identifiés par les LIENS LEGI du XML (`typelien` CREE ou MODIFIE).
- **Qualification des couples rewrite_draft.** On compare D_fut (ce que la version future change par rapport à la source courante) et D_proj (ce que change la proposition) :
  - *sans effet* : les passages sont disjoints et la modification se transpose telle quelle ;
  - *réforme écrasée* : la version future rétablit ou maintient, dans le passage réformé, ce que le projet supprime. Sont rangés ici aussi les cas où la proposition se confine elle-même à la version expirante ;
  - *conflit de rédaction* : le même passage est modifié des deux côtés, et il faut fusionner ;
  - *déjà traité* : la proposition intègre le contenu de la version future.
- **Deux directions de risque, toujours examinées ensemble.**
  - *Écrasement de la réforme* (RT-XCUT-01) : la réforme est adoptée avant la date d'effet de la version future, et celle-ci la remplace.
  - *Régression involontaire* (étiquette `base-perimee`) : la réforme, rédigée « ainsi rédigé » sur la source courante, est adoptée après la date d'effet. Elle efface alors la réforme publiée, ou rétablit des renvois périmés.
  - Pour les versions du 1er novembre 2026, seule la seconde direction est réaliste, puisque le projet ne peut être adopté avant cette date.
- **Bornes techniques.** Les dates 2222-02-22 et 2999-01-01 ne sont pas traitées comme normatives. Pour chaque borne 2222, la NOTA a été lue afin d'apprécier si la condition d'entrée en vigueur est déjà réalisée.
- **Retained et nouveaux numéros.** On recherche les obligations, cotisations ou formalités contraires aux orientations (`policy-coordinations.json` : cuts_and_reliefs, editorial_direction, preserved_benefits, micro_entrepreneurs, retraite), ainsi que les renvois vers des articles que le projet abroge. Ces renvois ont été repérés par un criblage automatique (`xref`) puis vérifiés par lecture de la proposition cible. Plusieurs faux positifs ont été écartés : L133-1 → L533-1 (code des procédures civiles d'exécution), L136-1-3 → L245-12 (CASF).
- **Organisation du travail.** La lecture a été répartie entre quatre lectures parallèles (vagues 2026-11, 2026-12 à 2030, 2028 existants, 2028 mahorais) et la lecture directe de la vague 2029 / 2222. Elle a été suivie d'une vérification ponctuelle par l'agent principal : L137-27, L759-5 / L136-8, L142-1, L434-16. Les objections ont été dédoublonnées : le renvoi R613-10-1 → R613-9 a été fusionné avec les renvois mahorais et ceux de L861-3 et L241-13.
- **Sources primaires.** Légifrance (JORF) a répondu HTTP 403 le 2026-10-26. Aucun texte modificatif n'a été lu au JORF : la nature des modifications (ciblée ou « ainsi rédigé ») est **déduite des différences LEGI**. C'est la principale limite des qualifications « sans effet ».

## 3. Tableau des 45 couples rewrite_draft (par date d'effet)

| Date d'effet | Article | Version courante → version future | Qualification | Objection |
|---|---|---|---|---|
| 2026-11-01 | L142-1 | LEGIARTI000042683979 → LEGIARTI000051288452 | sans effet | RT-FUTCSS-01 |
| 2026-11-01 | L351-3 | LEGIARTI000053279221 → LEGIARTI000051288449 | conflit de rédaction | RT-FUTCSS-18 |
| 2026-11-01 | L434-1 | LEGIARTI000031688413 → LEGIARTI000051288500 | réforme écrasée | RT-FUTCSS-02 |
| 2026-11-01 | L434-16 | LEGIARTI000031688385 → LEGIARTI000051288487 | réforme écrasée | RT-FUTCSS-01 |
| 2026-11-01 | L443-1 | LEGIARTI000026799850 → LEGIARTI000051288476 | sans effet | RT-FUTCSS-01 |
| 2026-11-01 | L461-1 | LEGIARTI000053281596 → LEGIARTI000053285183 | sans effet | RT-FUTCSS-01 |
| 2026-11-01 | R351-12 | LEGIARTI000054167657 → LEGIARTI000054060166 | sans effet | RT-FUTCSS-01 |
| 2026-11-01 | R351-12 | LEGIARTI000054167657 → LEGIARTI000054425288 | sans effet | RT-FUTCSS-01 |
| 2026-11-01 | R351-37 | LEGIARTI000047633235 → LEGIARTI000054060160 | conflit de rédaction | RT-FUTCSS-03 |
| 2026-11-01 | R434-32 | LEGIARTI000022073148 → LEGIARTI000054060111 | sans effet | RT-FUTCSS-01 |
| 2027-01-01 | L137-26 | LEGIARTI000041466952 → LEGIARTI000053151613 | conflit de rédaction | RT-FUTCSS-04 |
| 2027-01-01 | L137-27 | LEGIARTI000053269267 → LEGIARTI000053151617 | réforme écrasée | RT-FUTCSS-05 |
| 2027-01-01 | L137-30 | LEGIARTI000037054263 → LEGIARTI000053151619 | sans effet | RT-FUTCSS-04 |
| 2027-01-01 | L137-32 | LEGIARTI000037054450 → LEGIARTI000053151640 | sans effet | RT-FUTCSS-04 |
| 2027-01-01 | L138-11 | LEGIARTI000053282737 → LEGIARTI000048688952 | conflit de rédaction | RT-FUTCSS-06 |
| 2027-01-01 | L138-13 | LEGIARTI000048688928 → LEGIARTI000051287306 | réforme écrasée | RT-FUTCSS-07 |
| 2027-01-01 | L138-15 | LEGIARTI000046805500 → LEGIARTI000051287301 | conflit de rédaction | RT-FUTCSS-06 |
| 2027-01-01 | L162-23-14 | LEGIARTI000053271346 → LEGIARTI000053284498 | conflit de rédaction | RT-FUTCSS-08 |
| 2027-01-01 | L162-23-14-1 | LEGIARTI000053271405 → LEGIARTI000053284620 | réforme écrasée | RT-FUTCSS-08 |
| 2027-01-01 | L162-30-3 | LEGIARTI000053283471 → LEGIARTI000053284385 | conflit de rédaction | RT-FUTCSS-09 |
| 2027-01-01 | L223-9 | LEGIARTI000046808945 → LEGIARTI000046808960 | conflit de rédaction | RT-FUTCSS-13 |
| 2027-01-01 | L311-3 | LEGIARTI000051284232 → LEGIARTI000053151645 | conflit de rédaction | RT-FUTCSS-10 |
| 2027-01-01 | L461-1 | LEGIARTI000053281596 → LEGIARTI000053285169 | sans effet | RT-FUTCSS-01 |
| 2027-09-01 | L162-23-8 | LEGIARTI000053283299 → LEGIARTI000048971734 | réforme écrasée | RT-FUTCSS-11 |
| 2027-09-01 | L531-8 | LEGIARTI000036393126 → LEGIARTI000053281724 | réforme écrasée | RT-FUTCSS-12 |
| 2028-01-01 | L161-24 | LEGIARTI000054477759 → LEGIARTI000054478475 | réforme écrasée | RT-FUTCSS-14 |
| 2028-01-01 | L162-16-4 | LEGIARTI000053278915 → LEGIARTI000054703293 | sans effet | RT-FUTCSS-23 |
| 2028-01-01 | L222-2-1 | LEGIARTI000051288889 → LEGIARTI000054466881 | conflit de rédaction | RT-FUTCSS-22 |
| 2028-01-01 | L223-9 | LEGIARTI000046808945 → LEGIARTI000046808972 | conflit de rédaction | RT-FUTCSS-13 |
| 2028-01-01 | L241-13 | LEGIARTI000053280526 → LEGIARTI000054466849 | conflit de rédaction | RT-FUTCSS-15 |
| 2028-01-01 | L245-6 | LEGIARTI000053282660 → LEGIARTI000054703326 | sans effet | RT-FUTCSS-23 |
| 2028-01-01 | L325-1 | LEGIARTI000048702040 → LEGIARTI000054466898 | sans effet | RT-FUTCSS-24 |
| 2028-01-01 | L752-1 | LEGIARTI000042684012 → LEGIARTI000054466934 | réforme écrasée | RT-UNION-05 |
| 2028-01-01 | L752-3-2 | LEGIARTI000053285063 → LEGIARTI000054466922 | sans effet | RT-FUTCSS-15 |
| 2029-01-01 | L114-12-1 | LEGIARTI000054331780 → LEGIARTI000052851016 | sans effet | RT-FUTCSS-35 |
| 2029-01-01 | L114-9 | LEGIARTI000054331835 → LEGIARTI000054786009 | sans effet | RT-FUTCSS-35 |
| 2029-01-01 | L244-1 | LEGIARTI000029961352 → LEGIARTI000052846151 | sans effet | RT-FUTCSS-35 |
| 2029-01-01 | L355-2 | LEGIARTI000006742657 → LEGIARTI000052850993 | sans effet | RT-FUTCSS-35 |
| 2029-01-01 | L412-8 | LEGIARTI000053283575 → LEGIARTI000052850958 | sans effet | RT-FUTCSS-35 |
| 2030-01-01 | L137-33 | LEGIARTI000051287346 → LEGIARTI000046875809 | sans effet | RT-FUTCSS-04 |
| 2030-01-01 | L311-3 | LEGIARTI000051284232 → LEGIARTI000046902997 | conflit de rédaction | RT-FUTCSS-10 |
| 2222-02-22 | L861-3 | LEGIARTI000046812151 → LEGIARTI000048702084 | déjà traité | RT-FUTCSS-17 |
| 2222-02-22 | L861-5 | LEGIARTI000046806509 → LEGIARTI000048702075 | conflit de rédaction | RT-FUTCSS-17 |
| 2222-02-22 | R145-10 | LEGIARTI000052208286 → LEGIARTI000036592776 | réforme écrasée | RT-FUTCSS-36 |
| 2222-02-22 | R382-72 | LEGIARTI000006749777 → LEGIARTI000025690160 | sans effet | RT-FUTCSS-36 |

Les 133 autres lignes (retained_unchanged et nouveaux numéros) figurent dans `reports/p1-work/FUT-CSS-classification.jsonl`, avec leur motif. Elles sont commentées par vague à la section 4.

## 4. Constats par vague

### 4.1 Vague du 1er novembre 2026

#### Périmètre lu

Lus en entier avec `pair.py` ou `cite.py` : source courante, proposition, motif, notes et version future.

- **11 couples rewrite_draft** : L142-1 (000042683979 → 000051288452), L351-3 (000053279221 → 000051288449), L434-1 (000031688413 → 000051288500), L434-16 (000031688385 → 000051288487), L443-1 (000026799850 → 000051288476), L461-1 (000053281596 → 000053285183 et → 000053285169), R351-12 (000054167657 → 000054060166 et → 000054425288), R351-37 (000047633235 → 000054060160), R434-32 (000022073148 → 000054060111).
- **32 couples retained_unchanged** : D242-34, D242-6-19, D242-6-5, D242-6-6, D242-6-7, D351-1-10, D351-1-9, D432-15, D434-1, D434-2, D434-3-1, L431-1, L434-15, L434-17, L434-2, L452-2, L452-3, R173-3-1, R434-1, R434-1-1, R434-1-2, R434-1-3, R434-2, R434-2-1, R434-21, R434-28, R434-3, R434-34, R434-4, R434-5, R443-7, R461-8. Les versions futures ont été lues en entier ; le diff avec la source et le motif ou les notes ont été lus.
- **3 nouveaux numéros** : L434-1 A, R434-1-1-1, R434-1-4.
- **Lus en complément** : L351-1-4 en vigueur (LEGIARTI000053281659), source et proposition, sur les passages relatifs à L434-1 A et à la commission.
- **Criblage** : renvois au mot « alinéa … L. 434-2 » dans les textes en vigueur du CSS.

#### Règle de qualification appliquée

Je compare passage par passage ce que change la version future (D_fut) et ce que change le projet (D_proj).

Une proposition qui se **confine elle-même** à la version expirante n'est pas transposable telle quelle. C'est le cas de L434-1 (« les champs respectifs des versions successives … sont conservés ») et de L434-16 (« ne modifie ni la date d'abrogation … déjà fixée au 1er novembre 2026 »). Ces propositions sont classées `réforme écrasée`, même si les passages sont disjoints.

Point de droit commun à tout le lot : pour les articles législatifs, le V de l'article 90 de la loi 2025-199 réserve la version nouvelle aux « victimes dont l'état est consolidé à compter de cette date ». L'ancienne version, et la proposition qui s'y rattache, garde donc un champ résiduel pour le stock des victimes plus anciennes. Elle ne touche aucune victime nouvelle. Le projet ne pouvant pas être adopté avant le 1er novembre 2026, toute loi de réforme rédigée sur la source courante effacerait aussi, pour l'avenir, la terminologie de la réforme AT-MP (tag `base-perimee`).

#### Constats par couple rewrite_draft

**L142-1 → 000051288452 : sans effet (RT-FUTCSS-01).**
- La version future ne modifie que le 5° (« incapacité permanente, notamment aux taux »).
- Le projet modifie le 2° (« 5° du I de L. 213-1 ») et le 3° (L. 1233-69 limité aux adhésions antérieures), et ajoute un alinéa de sauvegarde.
- Les passages sont disjoints. Les notes affirment à tort qu'« aucune version de remplacement n'a été trouvée sous ce numéro » : la version existe dans le corpus.

**L351-3 → 000051288449 : conflit de rédaction (RT-FUTCSS-18).**
- La même phrase du 1° est modifiée des deux côtés : « professionnelle » est ajouté par la version future, l'occurrence erronée « ou du congé supplémentaire de naissance » est retirée par le projet.
- La fusion est mécanique. Les notes affirment à tort que le corpus ne contient que la version expirante.

**L434-1 → 000051288500 : réforme écrasée (RT-FUTCSS-02, P1).**
- La version future crée deux parts (professionnelle et fonctionnelle) et reprend mot pour mot « Cette indemnité est versée lorsque la décision est devenue définitive ».
- La proposition supprime cette attente, mais se confine à la version expirante.
- L'allègement est perdu pour toutes les victimes consolidées à compter du 1er novembre 2026.

**L434-16 → 000051288487 : réforme écrasée (RT-FUTCSS-01, effet mineur).**
- La correction « au premier alinéa du présent article » porte sur le troisième alinéa, que la version future laisse avec l'erreur « à l'alinéa précédent ».
- La clause « date d'abrogation déjà fixée au 1er novembre 2026 » lit la fin de version comme une abrogation (tag `lecture-abroge-diff`).

**L443-1 → 000051288476 : sans effet (RT-FUTCSS-01).**
- La version future ne change que le renvoi du quatrième alinéa (« II de l'article L. 434-2 »).
- Le projet rend les intervalles minimaux inopposables aux demandes d'aggravation de la victime.
- Sans transposition, les nouvelles victimes y restent soumises. Le renvoi du projet au « troisième alinéa de l'article L. 434-2 » est périmé pour elles.

**L461-1 → 000053285183 (1er novembre 2026 au 1er janvier 2027) et → 000053285169 (1er janvier 2027) : sans effet (RT-FUTCSS-01).**
- Les deux versions futures laissent l'alinéa CRRMP et son renvoi à L. 315-1 intacts. La correction du projet (« au I de l'article L. 315-2 ») se transpose.
- La version de 2027 insère un alinéa (deux médecins conseils lorsque seul le délai de prise en charge manque). Cette procédure est plus légère que le CRRMP et n'impose pas de formalité nouvelle à l'assuré.
- Effet induit : le renvoi de R461-8 au « septième alinéa » devient décalé (RT-FUTCSS-20).

**R351-12 → 000054060166 et 000054425288 : sans effet (RT-FUTCSS-01), avec un doublon LEGI (RT-FUTCSS-19).**
- La version future ne change que le 5° (IPP au moins égale à 66 %).
- Le projet retire la condition de mention au compte (avant-dernier alinéa), que la version future maintient.
- La seconde passe est encore en attente (inventaire « pending »).

**R351-37 → 000054060160 : conflit de rédaction (RT-FUTCSS-03, P1).**
- Le cinquième alinéa est réécrit des deux côtés : renvoi à L434-1 A dans la version future, au I de L351-1-4 dans le projet. Les deux convergent sur le fond.
- La version future maintient la saisine de la commission pluridisciplinaire, que L351-1-4 proposé supprime.
- Après le 1er novembre 2026, le décret imposerait donc une commission que la loi réformée ne prévoit plus.

**R434-32 → 000054060111 : sans effet (RT-FUTCSS-01).**
- La version future réécrit les alinéas 1 à 3 : deux taux, et suppression de l'alinéa qui annexe les barèmes. La réserve figure RESINT RT-DOC-01 n'est pas recomptée.
- Le projet modifie les alinéas 4 et 5 : ni délai de dix jours, ni formulaire, ni quinzaine.
- La proposition sur l'accès au rapport médical **ne survit pas** sans transposition : la version future maintient le délai de dix jours, le formulaire et la quinzaine.

#### Retained_unchanged et nouveaux numéros (35)

- **Sans effet (34)** : les versions futures appliquent la terminologie de la double indemnisation (« incapacité permanente professionnelle », part professionnelle et part fonctionnelle) et mettent à jour les renvois (II et III de L434-2, L434-1 A).
- **Aucune formalité, demande, attestation ou cotisation nouvelle** à la charge des assurés ou des employeurs n'a été trouvée.
- **Changements favorables** : rentes payées par mois (R434-34) et réparation de « l'ensemble des préjudices » non forfaitaires (L452-3).
- **Simple alerte, sans objection** : L434-17 et L452-2 excluent de la revalorisation la part fonctionnelle versée en capital. C'est une restriction de la loi publiée, cohérente avec le versement en capital, et aucune orientation précise ne la vise.
- **Réserve documentaire mineure** : artefact typographique « capital.éqs » dans R434-1-2 futur (consolidation LEGI).
- **R443-7 futur** : il vise « b du I de l'article R. 434-1-1 », alors que R434-1-1 futur n'a pas de I. C'est une imprécision officielle mineure.
- **R461-8 : coordination manquante (RT-FUTCSS-20)**. Le renvoi au « septième alinéa de L. 461-1 » est décalé à compter du 1er janvier 2027.
- **Nouveaux numéros** : L434-1 A (définition des deux taux par barèmes indicatifs fixés par arrêté), R434-1-1-1 (calcul de la part fonctionnelle) et R434-1-4 (déduction du capital déjà versé) ne créent aucune formalité. Le criblage `xref.json` ne trouve aucun renvoi à un article abrogé par le projet.
- **Tags transversaux** (pour l'agent principal) :
  - `lecture-abroge-diff` dans les notes de L434-16 (proposition) et de L434-15, L434-17, R434-1, R434-1-1, R434-1-2, R434-1-3, R434-2, R434-2-1, R434-28, R434-3, R434-4, R434-5, R461-8 (retained, sans effet sur un texte) ;
  - `notes-absence-version-erronee` dans L142-1, L351-3 et L431-1.

Hors périmètre, à signaler à l'agent principal : des articles en vigueur sans version future et non modifiés par le projet gardent des renvois de l'ancienne structure de L434-2. Ce sont R412-6 (« quatrième alinéa »), R413-7 et R844-5 (« troisième alinéa ») et l'annexe I à R434-32 (17) (« premier alinéa »). Il s'agit d'un conflit de source officiel ; les textes ont été lus par criblage seulement, pas en entier. R443-1 (intervalles de deux ans et un an) reste en retained_unchanged, alors que les notes de L443-1 demandent sa coordination.

### 4.2 Vague du 25 décembre 2026 au 1er janvier 2030

Périmètre : 17 couples rewrite_draft, 11 couples retained_unchanged et 2 nouveaux numéros, soit 30 lignes. Lecture par `pair.py` / `cite.py` : source, proposition, motif, notes et version future lus en entier. Seule exception : L311-3 (version 2030, LEGIARTI000046902997), établie par différence ligne à ligne exhaustive avec la source et avec la version 2027. Lectures complémentaires : L162-23 (toutes versions postérieures à 2026), L162-30-2, L162-30-4 et L162-30-4-1 (propositions), L133-5-12 (version et début de proposition), R613-9 (proposition), et dates de fin de CGI 256 B, 261, 287, 302 septies A, 1586 sexies et 1647 B sexies A.

#### Constats par couple rewrite_draft (date d'effet croissante)

**L137-26 (2027-01-01, ord. 2025-1247) — conflit de rédaction (RT-FUTCSS-04).** L'ordonnance remplace la déclaration par annexe TVA (1° à 3°) par la constatation selon CIBS L161-1 et L180-1. Le projet ne corrige que ce passage (« troisième alinéa »). La correction tombe. Votée après 2027 sur la source, la proposition rétablirait un circuit déclaratif adossé à CGI 302 septies A, éteint au 1er janvier 2027. Il faut accepter la version future et retirer la proposition.

**L137-27 (2027-01-01) — réforme écrasée (RT-FUTCSS-05).** Le projet abroge la contribution de 15 % sur la publicité des opérateurs de jeux. La version issue de l'ordonnance la réinstitue au 1er janvier 2027, à l'identique. L'abrogation doit viser aussi cette rédaction et neutraliser l'article 34 de l'ordonnance (rédaction en RT-FUTCSS-05).

**L137-30 et L137-32 (2027-01-01) — sans effet (RT-FUTCSS-04).** L'ordonnance ne change que les renvois TVA (4° bis ; alinéas 2 et 3 de L137-32). Le mécanisme de suppression de la C3S se transpose, mais les propositions reproduisent les renvois CGI 256 B périmés : il faut les reporter sur la rédaction CIBS.

**L138-11 et L138-15 (2027-01-01, LFSS 2024 art. 28) — conflit de rédaction (RT-FUTCSS-06).** Le législateur passe au montant remboursé et à la collecte publique des données, et supprime la majoration de 0,05 %. Les propositions réécrivent les mêmes passages sur l'ancienne base. L138-15 obtient moins que la loi publiée, puisqu'il garde la déclaration de l'entreprise. Il faut accepter les versions 2027 et garder seulement une transition pour les majorations anciennes non définitives.

**L138-13 (2027-01-01) — réforme écrasée (RT-FUTCSS-07).** L'échéance du 31 janvier disparaît dans la loi publiée, mais la condition syndicale que le projet supprime est maintenue. Rédaction fusionnée ci-dessous.

**L162-23-14 (2027-01-01) — conflit de rédaction ; L162-23-14-1 (2027-01-01) — réforme écrasée (RT-FUTCSS-08).** La LFSS 2026, art. 79, ajoute en 2027 une pénalité de 2 % au plus (2° de L162-23-14) et l'applique aux objectifs individuels de L162-23-14-1, que le projet abroge. Les notes prennent la fin de version pour une extinction (« ne fait pas revivre l'article après »).

**L162-30-3 (2027-01-01) — conflit de rédaction (RT-FUTCSS-09).** La loi réduit l'article au plan régional. Le projet maintient référentiels et volet contractuel volontaire « au-delà du 1er janvier 2027 », mais le CAQES (L162-30-2) et L162-30-4 sont abrogés à cette date sans successeur, et L162-22-4 (2027) retire leur financement. Conflit de source annexe : L162-30-4-1 (VIGUEUR) dépend des référentiels que la version 2027 supprime.

**L223-9 (2027 et 2028) — conflit de rédaction (RT-FUTCSS-13).** Les plafonds du concours APA passent à 7,93 % puis 8,1 %. Le projet fige 7,75 %. Les versions futures gardent le renvoi obsolète à la seconde part et à L137-41, abrogé par le projet.

**L311-3 (2027 et 2030) — conflit de rédaction (RT-FUTCSS-10).** L'ordonnance réécrit le 22° (dirigeants d'associations gérées à titre bénévole). Le projet le réécrit autrement (régime des dirigeants rémunérés). En 2030, le 4° passe de la CET à la CFE. Les autres modifications du projet se transposent.

**L162-23-8 (2027-09-01, loi 2023-29) — réforme écrasée (RT-FUTCSS-11).** L'avis préalable supprimé par le projet revient, avec les renvois fautifs. L162-23 n'a de 2° au I dans aucune version : conflit de source.

**L531-8 (2027-09-01, LFSS 2026 art. 101) — réforme écrasée (RT-FUTCSS-12).** L'obligation d'adhérer revient, désormais au dispositif de versement du salaire de L133-5-12, qui exige l'accord écrit du salarié.

**L137-33 (2030-01-01, loi 2022-1726) — sans effet (RT-FUTCSS-04).** Les renvois 1586 sexies deviennent 1647 B sexies A (suppression de la CVAE). Il suffit de transposer et d'articuler avec le calendrier CVAE du projet.

#### Retained_unchanged et nouveaux numéros

- Sans effet, avec des changements favorables ou neutres : L243-7-7 (réduction de vingt points de droit, donneurs d'ordres exonérés de solidarité), L133-1 (flagrance sociale ; signalement xref L533-1 = **faux positif**, il s'agit du code des procédures civiles d'exécution), L138-10 (2027 et 2028), L162-22-3, L174-16 (centres de vaccination), L544-1 (AJPP en résidence alternée).
- Coordination manquante : L138-12 (taux de 90 %, plafond déplacé vers L245-6 E III : le motif du maintien est dépassé, RT-FUTCSS-06) ; L162-22-4 (financement CAQES retiré, RT-FUTCSS-09).
- Simple alerte (RT-FUTCSS-21) : R160-5 (ticket modérateur relevé ; source encore « pending »), L162-5-10 (non-remboursement des prescriptions des médecins non conventionnés), L322-5-3 (nouveau : géolocalisation et facturation électronique obligatoires des transports sanitaires et taxis).
- Renvoi abrogé (RT-FUTCSS-28) : R613-10-1 (nouveau, favorable) renvoie à R613-9, que le projet abroge.
- Effets transversaux (tags, pour l'agent principal) : lecture-abroge-diff sur L137-26, L137-27, L137-32, L162-23-14, L162-23-14-1, L162-23-8, L531-8, L133-1, L162-22-3, L162-22-4, L162-5-10 ; notes-absence-version-erronee sur L243-7-7, L174-16, L544-1.

### 4.3 Vague du 1er janvier 2028 (articles existants)

#### Textes à l'origine des versions futures (liens LEGI)

- **Ordonnance n° 2026-647 du 22 juillet 2026** (JORFTEXT000054456323, NOR TRSS2615197R). Elle étend le code de la sécurité sociale à Mayotte au 1er janvier 2028 : chapitre II, art. 5 à 8, selon la NOTA de l'art. 4. Elle crée aussi un chapitre 9 du titre V du livre VII, « Dispositions particulières applicables à Mayotte entre le 1er janvier 2028 et le 31 mars 2036 » (art. 9 : L759-1 et suivants, qui relèvent du fork des nouveaux numéros). Dans le corpus, 69 versions VIGUEUR_DIFF du CSS portent un lien vers ce texte (53 CREE, 16 MODIFIE), auxquelles s'ajoutent des liens dans le code du travail et le CCH. Mécanisme commun : Mayotte entre dans la liste de L111-2 et de L751-1, les mentions « ou à Mayotte » ou les adaptations « VIII. – applicable à Mayotte » sont retirées des articles, et les régimes transitoires (convergence des taux et des planchers jusqu'en 2036) sont regroupés dans L759-x. Elle succède à l'ordonnance n° 2026-648 du même jour, dont les versions sont entrées en vigueur le 23 juillet 2026 (versions courantes de L161-24 et L111-2).
- **Loi n° 2026-791 du 16 août 2026, art. 41 III** (JORFTEXT000054694832, NOR ARMD2602476L). Elle remplace l'achat national de produits de santé de L1413-4 du CSP, assuré par l'ANSP, par celui de L3133-1, assuré par le ministre chargé de la santé. Entrée en vigueur **à une date fixée par décret, au plus tard le 1er janvier 2028** (XI) : la date LEGI de 2028 est un plafond, pas une date certaine. Aucun décret n'a été trouvé dans le corpus.
- **Loi n° 2026-534 du 25 juin 2026, art. 5** (NOR SFHT2521808L) et loi n° 2025-199, art. 88 II : L161-24-1 en 2028.
- **Décret n° 2026-858 du 11 septembre 2026** (NOR SFHS2624226D) : indexation des plafonds D160-6 et D160-10 en 2028.

#### Couples rewrite_draft (8, tous lus en entier)

**L161-24** (LEGIARTI000054477759 → LEGIARTI000054478475) : **réforme écrasée** (RT-FUTCSS-14). La version de 2028 réécrit la phrase même que le projet modifie (liste territoriale sans Mayotte) et conserve « justifie chaque année de son existence ». Le projet supprime cette justification annuelle. Les notes disent la version de 2028 « pas disponible dans ce lot », alors qu'elle figure au corpus.

**L162-16-4** (LEGIARTI000053278915 → LEGIARTI000054703293) : **sans effet** (RT-FUTCSS-23). Seul change le renvoi L1413-4 → L3133-1 du CSP. Le projet supprime l'opposition conjointe des ministres dans le même alinéa, sur d'autres mots. Il faut transposer et intégrer L3133-1. La date est fixée par décret et peut être antérieure à 2028.

**L222-2-1** (LEGIARTI000051288889 → LEGIARTI000054466881) : **conflit de rédaction** (RT-FUTCSS-22). L'ordonnance abroge le 6° (allocation spéciale de Mayotte) ; le projet le reformule. Les autres apports du projet (renvoi du b) au troisième alinéa de L1233-72, clause du contrat unique) sont à reporter.

**L241-13** (LEGIARTI000053280526 → LEGIARTI000054466849) : **conflit de rédaction** (RT-FUTCSS-15). Le VIII est supprimé et transféré à L759-10, avec un plancher à 88 % du SMIC au lieu de 60 % : c'est plus favorable. Le projet corrige ce VIII. Les allègements du contrat unique (III et IV 2°) et la règle des 40 heures sont disjoints mais perdus en 2028 s'ils ne sont pas transposés. Alerte transmise à l'agent principal : le I vise la contribution de L137-40, que le projet abroge, dans la source, la proposition et la version future. L759-7 adapte de son côté les taux de L137-40 et L137-41 à Mayotte.

**L245-6** (LEGIARTI000053282660 → LEGIARTI000054703326) : **sans effet** (RT-FUTCSS-23). Seul le III A 7° change (ministre / L3133-1). Le projet supprime les trois contributions et garde le 7° pour le calcul du plafond du III E. Sa clause « Les modifications à entrée en vigueur différée [...] ne peuvent en rétablir l'exigibilité » est utile mais n'intègre pas L3133-1. Aucune contribution supprimée n'est rétablie par le texte de 2026-791 lui-même, qui ne modifie que le 7°. Le risque vient de la version consolidée sans proposition.

**L325-1** (LEGIARTI000048702040 → LEGIARTI000054466898) : **sans effet** (RT-FUTCSS-24). L'ordonnance retire seulement « ou à Mayotte » aux 4° à 7°. Faute de transposition, les forclusions supprimées par le projet et le renvoi inconditionnel à L174-4 (forfait journalier, abrogé par le projet) reviennent en 2028.

**L752-3-2** (LEGIARTI000053285063 → LEGIARTI000054466922) : **sans effet** (RT-FUTCSS-15). L'exonération ultramarine est étendue à Mayotte, ce qui est favorable, et le VIII est supprimé. Le IV bis du projet (contrat unique d'intérim) est disjoint et doit être transposé.

**L752-1** (LEGIARTI000042684012 → LEGIARTI000054466934) : **réforme écrasée**, déjà établie par **RT-UNION-05** et non recomptée. Complément sur l'incertitude laissée par UNION : dans la version de 2028, l'alinéa relatif à Mayotte est inséré en deuxième position. La caisse de MSA de Saint-Barthélemy passe au **quatrième** alinéa (le troisième vise Saint-Martin, le cinquième le conseil de suivi). La correction faite en 2020, « au troisième alinéa », doit donc être transposée en « **au quatrième alinéa** ». La version de 2028 retire en outre L211-3 à L211-5 et L211-7 des deux listes, que la proposition de 2020 conserve. La correction de RT-UNION-05, qui part du texte officiel de 2028, absorbe ce point si elle est appliquée telle qu'elle est rédigée.

#### Couples retained_unchanged (14, tous lus en entier)

- **Sans effet, extension à Mayotte sans charge** : L111-2, L162-20-1 (III 1° : affiliation mahoraise), L713-10 et L713-19 (territoires de L111-2 : extension favorable aux familles de militaires), L751-1, L752-2 (caisse de Mayotte ; aucune approbation rétablie), L752-8 (montants mahorais possibles de l'aide à la restauration scolaire).
- **Sans effet, renvoi au CSP (loi 2026-791)** : L162-16-5-4-1, L162-19-2, L162-19-3. Défaut de source dans L162-16-5-4-1 : « par le ministre chargé de la santé » mais « le prix auquel l'agence a acheté ».
- **Sans effet, décret 2026-858** : D160-6 et D160-10 indexent le nombre maximal de participations (35) et le plafond des franchises (70 €). La proposition de L160-13 supprime pour l'avenir la participation du II et la franchise du III : l'indexation porte sur des charges éteintes. Elle aurait un effet de hausse seulement si cette réforme n'était pas adoptée. Le motif de maintien de D160-6 (« la participation législative subsiste ») contredit la proposition de L160-13 : c'est une incohérence de motif, sans effet normatif, signalée à l'agent principal.
- **Charge contraire aux orientations** : **L161-24-1** (RT-FUTCSS-14). En 2028, la biométrie devient le mode de preuve de principe (« est apportée »), ce qui contredit le renvoi du projet à une « faculté » et l'exclusion de toute biométrie imposée.
- **Coordination manquante / réserve documentaire** : **L757-1** (RT-FUTCSS-25). L'article est remplacé intégralement par des adaptations de l'ASPA à Mayotte. La condition d'âge des allocations forfaitaires et L811-14 disparaissent dans les départements d'outre-mer, alors que le projet les maintenait par précaution. Le c) renvoie à un « troisième alinéa de l'article L. 752-9-1 » qui ne désigne aucune caisse.

### 4.4 Vague du 1er janvier 2028 (55 nouveaux numéros mahorais)

#### Périmètre réellement lu

- **55 articles** (et non 52 : le décompte exact de `new_numbers` avec `future_from` = 2028-01-01 donne 55). Tous sont `VIGUEUR_DIFF`, `not_in_inventory` et sans proposition. Chacun a été lu en entier par `cite.py` : source, NOTA et LIENS. Liste et identifiants : `classification.jsonl` de ce dossier.
  - Section 3 bis du chapitre 2 et dispositions des chapitres 1 à 8 du titre V : L751-1-1, L752-9-1 à L752-9-7, L753-1-1 à L753-1-3, L753-4-1 à L753-4-4, L753-7-1 à L753-7-4, L754-0-1, L755-35 à L755-38, L757-4, L757-5, L758-5. Ils sont créés par l'**art. 8** ; leur NOTA précise : « article 4 […] chapitre II », applicables à Mayotte à compter du 1er janvier 2028, sans terme.
  - Chapitre 9 « Dispositions particulières applicables à Mayotte entre le 1er janvier 2028 et le 31 mars 2036 » : L759-1 à L759-27 et L759-22-1, créés par l'**art. 9**. Leur fin de version est fixée au 2036-03-31 : c'est une date normative, et non une borne technique.
  - Texte créateur, d'après les LIENS LEGI : JORFTEXT000054456323, NOR TRSS2615197R. Je n'ai pas consulté le JORF lui-même. L757-4 et L757-5 sont des numéros recyclés (versions de 1990 à 2003 encore en base), et leur XML de 2028 ne porte pas de lien CREE.
- **Articles cibles lus pour vérifier les renvois** : source, proposition, motif et notes. En entier : L174-4, L137-16, L137-40, L137-41, L380-2, L842-5, L842-2, L821-1, L821-6, L842-3, L842-7, L815-7, L755-19, L582-2, L355-3, L581-4. Par comparaison alinéa par alinéa, avec lecture complète des alinéas visés : L512-2, L162-4-1, L162-4-4, L160-13, L911-7, L911-7-1, L241-3 (dont II à VII lus en entier), L241-10, L136-8, L351-1, L351-2, L355-2 (et sa version de 2029), L581-10, L553-2, L161-23-1, L221-3-1, L227-3, L221-1 (6°), L241-13 (II : source, proposition et version de 2028), L861-5 (dernier alinéa). Pour L635-1, L612-1, L612-6, L217-3-1, L217-6, L213-4, L861-1, L122-6, L553-1, L581-3, L582-1, L531-5, L331-8-1, L815-1, L162-16, L165-1, L162-16-5, L162-16-6, L162-26, L165-7, L162-29, L162-30-1, L222-1, L223-1 et L225-1, j'ai lu les alinéas modifiés et le motif. Ces lectures servaient seulement à vérifier qu'aucune n'abroge l'organisme ou la subdivision visée.
- Méthode : lecture intégrale de chaque article mahorais ; criblage automatique (`f4/refs.py`) des renvois vers des articles CSS dont la proposition est une abrogation ou supprime les mots cités ; puis contrôle manuel de chaque renvoi par rang d'alinéa (« dernier », « avant-dernier », « deuxième phrase »…).

#### Constats regroupés

##### Ce qui est sans effet (38 articles)
L'organisation de la CSSM (L752-9-1, -3, -4, -5) s'accorde avec les propositions : contrats pluriannuels facultatifs, nominations sans liste d'aptitude, budgets réputés approuvés. Il en va de même des exclusions et applications d'articles inchangés ou modifiés sans effet sur le renvoi : L753-1-x, L753-4-2, L753-4-4, L753-7-x, L755-35 à -37, L758-5, L759-1, -2, -4, -8, -9, L759-13 à -19, -21, -22, -27. Elles restent opérantes. Faveurs constatées et à conserver : prise en charge intégrale au CHM (L753-4-1 I), majorations de prix (L753-4-2), trimestres supplémentaires (L753-7-2), report des comptes combinés (L759-2), maintien des allocations familiales pour un enfant (L759-23 9°), convergence ascendante de l'ASPA, de l'AAH et de la prime d'activité. Le gel partiel des pensions (L161-23-1 II proposé) ne touche pas les pensions d'invalidité mahoraises (L759-17), puisqu'il est limité aux pensions de vieillesse et de réversion.

##### RT-FUTCSS-26 — 55 articles hors inventaire (P2, anomalie d'inventaire)
C'est le cas particulier, pour Mayotte, de RT-XCUT-01. À partir de 2028, toutes les propositions qui visent les organismes du régime général s'appliquent à la CSSM par L751-1-1. Les défauts concrets suivent.

##### RT-FUTCSS-27 — Adaptations mahoraises privées d'objet ou déplacées (P2, coordination manquante, confirmé)
Les propositions ajoutent un alinéa final de transition et suppriment des locutions. Les substitutions mahoraises visent des mots exacts ou des rangs d'alinéa :
- **L757-5 2° a) → L842-5** : les mots « les conditions mentionnées à l'article L. 512-2 » n'existent plus, et le « dernier alinéa » est la transition. La condition applicable aux enfants des étrangers à Mayotte devient indéterminée. Le 2° b) (règle de la première épouse) se placerait après la transition.
- **L759-20 2° → L355-2** : les mots « tiers du minimum prévu au premier alinéa de l'article L. 351-10 » sont au 4e alinéa de la proposition, alors que le dernier alinéa est la transition. Le quart de l'ASPA ne se substitue plus.
- **L759-24 → L815-7** : à Mayotte, le « dernier alinéa » supprimé serait la transition de la liquidation sans demande (5e alinéa proposé), au lieu de l'alinéa du décret d'organisation.
- **L759-25 5° → L821-1** : mots supprimés et dernier alinéa déplacé. L'effet est neutralisé par L759-1 1°.
- **L753-4-3 → L162-4-1** : la locution exclue n'existe plus, mais « ainsi que sa durée » subsiste. La mention de durée redevient exigée à Mayotte (effet minime).
- **L752-9-6 → L227-3** : l'« avant-dernier alinéa » désigne désormais l'alinéa de signature propre à la branche maladie.
- **L759-26 1° b) → L842-2 3°** : le 3° est abrogé par le projet ; l'adaptation est sans objet, avec un effet favorable.

##### RT-FUTCSS-16 — CSG mahoraise et taux de 6,6 % proposé (P1, coordination manquante, à confirmer)
L759-5 multiplie séparément la part déductible et la part non déductible du taux du 1° du I de L136-8. La proposition crée un taux de 6,6 % pour les salaires du privé sans le décomposer. Le taux mahorais n'est pas calculable de 2028 à 2036 si la baisse entre en vigueur.

##### RT-FUTCSS-28 — Renvois à des prélèvements que le projet abroge (P2, confirmé)
Sont concernés L759-6 (forfait social L137-16), L759-7 (CSA et CASA L137-40 et L137-41), L759-11 (cotisation subsidiaire L380-2) et L753-4-1 (forfait journalier L174-4). Ces renvois deviennent sans objet. Aucune renaissance n'est possible, mais il y a une hausse annuelle mahoraise si l'abrogation est postérieure à 2028.

##### RT-FUTCSS-29 — Convergence des taux réduits mahoraux (P2, simple alerte, à confirmer)
L759-3 et L759-5 : hausse progressive des cotisations jusqu'en 2036, déjà publiée, que le projet ne tranche pas. L759-22-1 : le décret de convergence ne doit pas rétablir une cotisation minimale que L635-1 proposé retire.

##### RT-FUTCSS-30 — Non-cumul AB / AF pour un enfant rétabli à Mayotte (P2, confirmé)
L759-23 11° a) et b) réécrit L755-19 pour Mayotte jusqu'au 31 mars 2030 et y rétablit le non-cumul que la proposition supprime. Pour Mayotte, c'est une réforme écrasée pendant 27 mois.

##### RT-FUTCSS-31 — Conditions d'accès propres à Mayotte (P2, simple alerte)
Il s'agit de la durée de résidence pour l'AAH des étrangers hors UE (L757-4) et de la prise en compte de la seule première épouse (L755-38, L757-5 2° b). Elles vont dans le sens inverse des suppressions de durées que fait le projet. C'est une décision de l'auteur, sans contradiction de texte.

##### RT-FUTCSS-32 — Transfert vers la capitalisation et salariés de la CSSM (P2, à confirmer)
La CSSM est un « organisme local […] du régime général » (L752-9-2). Les salariés mahorais, y compris les salariés agricoles dont la CSSM gère la vieillesse (L752-9-1 3° b), entrent donc dans la première phase de L241-3 II proposé. Pendant ce temps, leurs taux, leur plafond et leur calcul de pension restent propres (L759-3, L759-8, L759-22). Cela heurte l'orientation « pas d'extension automatique aux salariés agricoles ».

##### RT-FUTCSS-33 — Décision immobilière nationale préalable pour la seule CSSM (P2, confirmé)
L752-9-7 confie cette décision aux caisses nationales, alors que L221-1 6° proposé (et L223-1) supprime l'agrément préalable.

##### RT-FUTCSS-34 — Erreurs matérielles probables du texte officiel (P2, conflit de source, à confirmer)
- L759-23 7° est borné « Jusqu'au 31 mars 2026 », dans un texte applicable en 2028.
- Le chapeau de L759-23 porte « jusqu'au 31 décembre 2036 », alors que l'article prend fin au 31 mars 2036.
- L759-12 II 3° porte « ne sont applicables », sans le « pas ».
- L759-10 porte « au titre de l'année 2026 ».
Le JORF n'a pas été vérifié.

### 4.5 Vague du 1er janvier 2029 et bornes techniques 2222-02-22

#### Constats

##### Textes à l'origine des versions futures (liens LEGI)

- **Ordonnance n° 2025-1091 du 19 novembre 2025** (JORFTEXT000052650320, NOR JUSD2530057R, art. 3 et 41, entrée en vigueur au 1er janvier 2029 selon l'art. 57).
  - Elle recodifie le code de procédure pénale (CPP). Dans le CSS, elle remplace les renvois aux anciens articles du CPP par les nouveaux : 28-1 et 28-2 deviennent L. 2242-1 et suivants, 88 et 392-1 deviennent L. 3413-5 et L. 4415-5, 375 devient L. 4326-18, 44-1 devient L. 4222-1 à L. 4222-6, 723 devient L. 5233-1, 77-2 devient L. 3324-1 et suivants, 2 devient L. 1221-1.
  - Elle remplace aussi des dénominations : « tribunal de police » devient « tribunal contraventionnel », « tribunal correctionnel » devient « tribunal délictuel », « action publique » devient « action pénale ».
  - Le JORF n'a pas été lu : Légifrance a répondu HTTP 403 le 2026-10-26. Les modifications sont déduites des différences LEGI. Elles sont toutes ciblées et ne touchent aucun passage modifié par le projet.
- **Loi n° 2023-1250 du 26 décembre 2023, art. 45** (JORFTEXT000048668665) : L861-3 et L861-5. L'entrée en vigueur est fixée par décret, et au plus tard le 1er juillet 2024, 2025 ou 2026 selon les catégories.
- **Décret n° 2018-79 du 9 février 2018** (JORFTEXT000036589802) : R145-10 et R146-1 à R146-8, applicables aux prochains renouvellements des conseils de l'ordre.
- **Décret n° 2012-477 du 12 avril 2012** (JORFTEXT000025687471) : R382-72, applicable au prochain renouvellement général du conseil de la CAVIMAC.
- **Loi n° 2026-555 du 29 juin 2026, art. 3** : L136-1-3, au plus tard le 1er janvier 2029.

##### Couples rewrite_draft (9, lus en entier)

**L114-12-1 (LEGIARTI000054331780 → LEGIARTI000052851016, 2029) : sans effet (RT-FUTCSS-35).**
- Le 6° voit ses renvois au CPP recodifiés.
- Le projet ajoute au deuxième alinéa la règle du réemploi des données, sans nouvelle demande à l'assuré.
- Les passages sont disjoints. Les notes disent le successeur « non fourni ».

**L114-9 (LEGIARTI000054331835 → LEGIARTI000054786009, 2029) : sans effet (RT-FUTCSS-35).**
- Le IV voit ses renvois au CPP recodifiés.
- Le projet supprime la synthèse annuelle au ministre.
- Les passages sont disjoints, mais la version 2029 publiée reproduit « Ils en établissent annuellement une synthèse ». Sans transposition, la formalité réapparaît dans la consolidation officielle.

**L244-1 (LEGIARTI000029961352 → LEGIARTI000052846151, 2029) : sans effet (RT-FUTCSS-35).**
- La version 2029 remplace « tribunal de police » par « tribunal contraventionnel ».
- Le projet ajoute un second alinéa qui interdit les poursuites fondées sur R244-4 à R244-6, abrogés, et réserve la loi pénale plus douce. Cet alinéa se transpose sans changement.
- Notes : « acte d'abrogation et texte successeur non fournis ».

**L355-2 (LEGIARTI000006742657 → LEGIARTI000052850993, 2029) : sans effet (RT-FUTCSS-35).**
- Au quatrième alinéa, « 375 » devient « L. 4326-18 ».
- Le projet supprime la saisie à 90 % des pensions pour frais d'hospitalisation.
- La version 2029 publiée reproduit « dans la limite de 90 % » : la transposition est indispensable.

**L412-8 (LEGIARTI000053283575 → LEGIARTI000052850958, 2029) : sans effet (RT-FUTCSS-35).**
- Au 5°, le renvoi à « 44-1 » est recodifié.
- Le projet actualise les renvois au code du travail (2° c, f, 9° et 12°) et ajoute un alinéa final sur le contrat unique.

**L861-3 (LEGIARTI000046812151 → LEGIARTI000048702084, borne 2222) : déjà traité (RT-FUTCSS-17).**
- La version différée corrige « avant-dernier alinéa » en « sixième alinéa » de L162-5-3. La proposition fait déjà cette correction et la limite aux soins antérieurs à la suppression de la majoration du parcours de soins.
- Le 2° renvoie au forfait journalier L174-4, que le projet abroge (RT-FUTCSS-28).

**L861-5 (LEGIARTI000046806509 → LEGIARTI000048702075, borne 2222) : conflit de rédaction (RT-FUTCSS-17, P1).**
- Le dernier alinéa est réécrit des deux côtés : renouvellement automatique des personnes présumées éligibles (2° à 5° de L861-2) dans la version de 2023, renouvellement sans demande fondé sur les données disponibles dans le projet.
- La version de 2023 cible aussi l'information des bénéficiaires de l'AAH (troisième alinéa).
- La NOTA fixe des dates butoirs déjà passées (1er juillet 2026). L861-2, en vigueur depuis le 1er juillet 2024 (LEGIARTI000048702111), contient les présomptions visées. La borne 2222 est donc technique, et la base de la proposition est probablement déjà dépassée.

**R145-10 (LEGIARTI000052208286 → LEGIARTI000036592776, borne 2222) : réforme écrasée, à confirmer (RT-FUTCSS-36).**
- La version différée date de 2018 ; la version courante, de 2025 (décret n° 2025-905).
- La version différée vise le RSI, supprimé, et « trois régimes ».
- Elle conserve, dans les cinq 2°, l'« avis du médecin-conseil national » que le projet supprime.
- Il s'agit d'un résidu de consolidation probable (conflit de source).

**R382-72 (LEGIARTI000006749777 → LEGIARTI000025690160, borne 2222) : sans effet (RT-FUTCSS-36).**
- La version différée supprime le quota de nationalité, ce que le projet fait aussi, plus largement.
- La suppression de l'exclusion contraventionnelle n'est pas touchée.

##### Retained_unchanged (16, lus en entier)

- **Recodification du CPP, sans effet** : L133-9-5, L243-10, L244-7, L244-8-1, L382-32, L433-4, L931-7-2 (RT-FUTCSS-35, et RT-FUTCSS-38 pour les notes erronées).
- **L136-1-3, sans effet et favorable** : un 7° nouveau soustrait à la CSG l'allocation de réparation de la loi n° 2026-555 (mineurs réunionnais transplantés). Le signal automatique vers L245-12 est un **faux positif** : il vise le CASF.
- **R652-26, renvoi à un article abrogé (RT-FUTCSS-37)** : R652-26 organise l'exigibilité du droit de plaidoirie de L652-6, que le projet abroge. Les notes du maintien disent « Cette abolition n'est pas proposée dans ce lot », ce que contredit la proposition courante de L652-6 (LEGIARTI000037063237).
- **R146-1, R146-2, R146-3, R146-4, R146-6, R146-7, R146-8, sans effet (RT-FUTCSS-36)** : la mention « de première instance » est retirée pour la Nouvelle-Calédonie et la Polynésie française. Aucune charge.

### 4.6 Constat transversal : lecture de ABROGE_DIFF et notes sur l'absence de successeur (RT-FUTCSS-38)

Dans 55 numéros du paquet (29 avec une lecture de la fin de version comme une abrogation, 29 avec une affirmation qu'aucun successeur n'est fourni), la proposition ou ses notes traitent l'état LEGI ABROGE_DIFF comme l'extinction de l'article. Or il s'agit de la fin d'une version, à laquelle succède une version VIGUEUR_DIFF publiée et présente dans l'instantané. Numéros concernés : D160-6, L114-12-1, L114-9, L133-1, L133-9-5, L136-1-3, L137-26, L137-27, L137-32, L142-1, L161-24, L162-16-4, L162-22-3, L162-22-4, L162-23-14, L162-23-14-1, L162-23-8, L162-5-10, L174-16, L243-10, L243-7-7, L244-1, L244-7, L244-8-1, L325-1, L351-3, L355-2, L382-32, L412-8, L431-1, L433-4, L434-15, L434-16, L434-17, L531-8, L544-1, L713-10, L713-19, L751-1, L752-2, L752-3-2, L752-8, L931-7-2, R145-10, R434-1, R434-1-1, R434-1-2, R434-1-3, R434-2, R434-2-1, R434-28, R434-3, R434-4, R434-5, R461-8. Pour les propositions, la conséquence est soit une clause qui confine la réforme à la version expirante (L434-1, L434-16, L531-8, L162-23-8), soit l'absence de transposition. Pour les maintiens, la conséquence est nulle sur le texte mais trompeuse pour la consolidation.

## 5. Liste des objections

| Id | Priorité | Statut | Nature | Objet (correction minimale, extrait) |
|---|---|---|---|---|
| RT-FUTCSS-01 | P1 | confirmé | coordination manquante | L142-1, L434-16, L443-1, L461-1, R351-12, R434-32 — Inscrire à l'inventaire les versions LEGIARTI000051288452, 000051288487, 000051288476, 000053285183, 000053285169, 000054425288 (avec le doublon 000054060166, voir RT-FUTCSS-19) et 000054060111. Donner à chacune une prop… |
| RT-FUTCSS-02 | P1 | confirmé | incohérence du projet | L434-1, L434-1 A — Inscrire LEGIARTI000051288500 à l'inventaire. Lui donner la rédaction fusionnée de section.md (structure en deux parts de la version future, versement des deux parts dès notification, réserve de l'option de R434-4 et tra… |
| RT-FUTCSS-03 | P1 | confirmé | incohérence du projet | L351-1-4, R351-37 — Inscrire LEGIARTI000054060160 à l'inventaire. Lui donner la rédaction fusionnée de section.md : quatrième alinéa (« cinquième alinéa du III ») et cinquième alinéa du projet, ce dernier précisé par la mention de L434-1 A … |
| RT-FUTCSS-04 | P1 | confirmé | coordination manquante | L137-26, L137-30, L137-32, L137-33 — Inscrire les versions LEGIARTI000053151613, 53151619, 53151640 et 46875809 à l'inventaire. Retirer la proposition L137-26, la version future étant acceptée telle quelle. Pour L137-30, L137-32 et L137-33, appliquer à la v… |
| RT-FUTCSS-05 | P1 | confirmé | risque juridique | L137-27 — Rédiger la disposition de réforme ainsi : « L'article L. 137-27 du code de la sécurité sociale est abrogé, y compris dans sa rédaction issue de l'article 34 de l'ordonnance n° 2025-1247 du 17 décembre 2025. Les dispositi… |
| RT-FUTCSS-06 | P1 | confirmé | incohérence du projet | L138-10, L138-11, L138-12, L138-15 — Accepter expressément les versions 2027 de L138-10, L138-11, L138-12 et L138-15. Retirer les corps proposés de L138-11 et L138-15. Ne garder de L138-15 qu'une disposition transitoire : « Aucune majoration forfaitaire pou… |
| RT-FUTCSS-07 | P1 | confirmé | risque juridique | L138-13 — Appliquer à la version 2027 la rédaction fusionnée donnée en section (suppression de « dont le syndicat représentatif est signataire de l'accord mentionné au premier alinéa de l'article L. 162-17-4, »), et adapter la cla… |
| RT-FUTCSS-08 | P1 | confirmé | risque juridique | L162-23-14, L162-23-14-1 — Disposition de réforme : « L'article L. 162-23-14-1 est abrogé dans toutes ses rédactions, y compris celle issue de l'article 79 de la loi n° 2025-1403 du 30 décembre 2025 entrant en vigueur le 1er janvier 2027. Aucune p… |
| RT-FUTCSS-09 | P1 | confirmé | coordination manquante | L162-22-4, L162-30-2, L162-30-3, L162-30-4, L162-30-4-1 — Choisir l'une de deux voies. (a) Maintenir le CAQES volontaire : disposition expresse abrogeant, à l'article 79 de la loi 2025-1403, les dispositions qui abrogent L162-30-2 et L162-30-4 et réécrivent L162-30-3 au 1er jan… |
| RT-FUTCSS-10 | P1 | à confirmer | conflit de source | L311-3 — Transposer sur les versions 2027 et 2030 toutes les modifications disjointes du projet (1°, 2°, 15°, 16°, 37° et alinéa final). Pour le 22°, retenir la rédaction de l'ordonnance. Si l'auteur maintient sa lecture, l'énonc… |
| RT-FUTCSS-11 | P1 | confirmé | risque juridique | L162-23-8 — Appliquer à la version 2027 la rédaction fusionnée donnée en section, et supprimer la phrase « Elle ne proroge pas la durée d'application du présent dispositif ».… |
| RT-FUTCSS-12 | P1 | confirmé | risque juridique | L531-8 — Appliquer à la version 2027 le premier alinéa fusionné donné en section (adhésion de plein droit, sans démarche, au dispositif de L133-5-12, sous réserve de l'accord du salarié que cet article exige) et supprimer la dern… |
| RT-FUTCSS-13 | P1 | confirmé | coordination manquante | L223-9 — Rédaction fusionnée donnée en section, valable pour toutes les versions : I, premier alinéa à taux échelonnés (7,75 % jusqu'au 31 décembre 2026, 7,93 % en 2027, 8,1 % à compter de 2028) ; le reste de la proposition sans … |
| RT-FUTCSS-14 | P1 | confirmé | coordination manquante | L161-24, L161-24-1 — Inscrire LEGIARTI000054478475 et LEGIARTI000054358416 à l'inventaire. Donner à L161-24 (version 2028) la rédaction de la proposition, la liste territoriale devenant « résidant en dehors des territoires mentionnés à l'art… |
| RT-FUTCSS-15 | P1 | confirmé | coordination manquante | L241-13, L752-3-2, L759-10 — Inscrire LEGIARTI000054466849 et LEGIARTI000054466922 à l'inventaire. L241-13, version 2028 : reprendre les I à VII de la proposition courante (proposed_sha256 indiqué) et ne pas reprendre le VIII. L752-3-2, version 2028… |
| RT-FUTCSS-16 | P1 | à confirmer | coordination manquante | L136-8, L759-5 — Compléter le VII de L136-8 proposé : « Pour l'application de l'article L. 759-5, le taux de 6,6 % se décompose en une part déductible et une part non déductible dans les conditions prévues à l'article 154 quinquies du co… |
| RT-FUTCSS-17 | P1 | confirmé | risque juridique | L861-2, L861-3, L861-5 — Rédiger L861-5 sur la base de la version LEGIARTI000048702075. Garder le troisième alinéa et la deuxième phrase du dernier alinéa dans leur rédaction de 2023, et y ajouter les modifications du projet aux deuxième, quatri… |
| RT-FUTCSS-18 | P2 | confirmé | coordination manquante | L351-3 — Proposition pour LEGIARTI000051288449, 1° : « les périodes pendant lesquelles l'assuré a bénéficié des prestations maladie, maternité, invalidité, accident du travail ou du congé supplémentaire de naissance et celles pos… |
| RT-FUTCSS-19 | P2 | confirmé | anomalie d'inventaire | R351-12 — Rattacher la proposition transposée de R351-12 à LEGIARTI000054425288, inscrire LEGIARTI000054060166 comme doublon LEGI sans proposition propre, et vérifier sur Légifrance laquelle subsiste.… |
| RT-FUTCSS-20 | P2 | à confirmer | conflit de source | L461-1, R461-8 — Proposition pour R461-8 (version applicable à compter du 1er janvier 2027) : « Le taux d'incapacité permanente professionnelle mentionné à l'alinéa de l'article L. 461-1 relatif aux maladies caractérisées non désignées d… |
| RT-FUTCSS-21 | P2 | confirmé | simple alerte | L162-5-10, L322-5-3, R160-5 — Faire examiner ces trois versions par la seconde passe et consigner pour chacune une décision expresse (acceptée ou coupée), sans fixer de taux nouveau.… |
| RT-FUTCSS-22 | P2 | confirmé | incohérence du projet | L222-2-1 — Version 2028 : rédaction de la proposition avec « 6° Abrogé ; ». Texte complet en P-RT-FUTCSS-22.… |
| RT-FUTCSS-23 | P2 | confirmé | coordination manquante | L162-16-4, L162-16-5-4-1, L245-6 — Dans les propositions : L162-16-4, I, premier alinéa : remplacer « L. 1413-4 » par « L. 3133-1 ». L245-6, III, A, 7° : écrire « 7° Celles acquises par le ministre chargé de la santé en application de l'article L. 3133-1 … |
| RT-FUTCSS-24 | P2 | confirmé | coordination manquante | L174-4, L325-1 — Version 2028 : rédaction de la proposition courante, en supprimant les mots « , ou à Mayotte » aux 4°, 5°, 6° et 7° (deux occurrences au 7°) du II.… |
| RT-FUTCSS-25 | P2 | à confirmer | réserve documentaire | L757-1 — Inscrire LEGIARTI000054467090 à l'inventaire et l'accepter telle quelle, avec une seule rectification : au c), remplacer « au troisième alinéa de l'article L. 752-9-1 » par « à l'article L. 752-9-1 ». Lever la réserve su… |
| RT-FUTCSS-26 | P2 | confirmé | anomalie d'inventaire | L751-1-1, L752-9-2, L757-4, L757-5, L759-1, L759-23, L759-3 — Inscrire les 55 versions à l'inventaire de la seconde passe. Les 38 articles « sans effet » ou à pur renvoi reçoivent le statut retained_unchanged ; les articles visés par RT-FUTCSS-27 à RT-FUTCSS-30, RT-FUTCSS-32 et RT-… |
| RT-FUTCSS-27 | P2 | confirmé | coordination manquante | L162-4-1, L227-3, L355-2, L752-9-6, L753-4-3, L757-5, L759-20, L759-24, L759-25, L759-26, L815-7, L821-1, L842-2, L842-5 — Option préférée : inscrire les transitions des propositions dans un article ou un paragraphe distinct (numéroté, par exemple « II » ou article de la loi de réforme), plutôt qu'en dernier alinéa des articles L355-2, L815-… |
| RT-FUTCSS-28 | P2 | confirmé | coordination manquante | L137-16, L137-40, L137-41, L174-4, L223-9, L241-13, L380-2, L753-4-1, L759-11, L759-6, L759-7, L861-3, R613-10-1, R613-9 — Dans la loi de réforme : « Les articles L. 759-6, L. 759-7 et L. 759-11 sont abrogés à compter de la date d'effet de l'abrogation, respectivement, des articles L. 137-16, L. 137-40 et L. 137-41, et L. 380-2. Au deuxième … |
| RT-FUTCSS-29 | P2 | à confirmer | simple alerte | L759-22-1, L759-3, L759-5, L759-9 — Ajouter à L759-22-1 : « Ces conditions de convergence ne peuvent instituer une cotisation minimale obligatoire. » Pour L759-3 : décision expresse de l'auteur, maintien des facteurs publiés ou gel au niveau 2028 ; aucun t… |
| RT-FUTCSS-30 | P2 | confirmé | coordination manquante | L755-19, L759-23 — Dans la loi de réforme : « Au a du 11° de l'article L. 759-23, les mots : “ “a) Les allocations familiales au titre d'un seul enfant à charge ; ” ” et la lettre “b)” sont supprimés ; au b du même 11°, la phrase : “L'allo… |
| RT-FUTCSS-31 | P2 | à confirmer | simple alerte | L755-38, L757-4, L757-5, L821-1, L842-2 — Aucune correction imposée ; décision expresse de l'auteur, consignée dans les notes de L821-1 et L842-2.… |
| RT-FUTCSS-32 | P2 | à confirmer | coordination manquante | L241-3, L351-1, L752-9-1, L752-9-2, L759-22, L759-3, L759-8 — Ajouter au II de L241-3 proposé : « Les salariés relevant de la caisse de sécurité sociale de Mayotte, y compris les salariés agricoles mentionnés au b du 3° de l'article L. 752-9-1, ne sont concernés qu'après l'entrée e… |
| RT-FUTCSS-33 | P2 | confirmé | coordination manquante | L221-1, L223-1, L752-9-2, L752-9-7 — Réécrire L752-9-7 : « La caisse de sécurité sociale de Mayotte décide de ses opérations immobilières et de la gestion de son patrimoine. Les caisses nationales mentionnées aux articles L. 221-1, L. 222-1, L. 223-1 et L. … |
| RT-FUTCSS-34 | P2 | à confirmer | conflit de source | L759-10, L759-12, L759-23 — Vérifier le JORF (JORFTEXT000054456323). Si l'erreur s'y trouve, signaler un rectificatif ou corriger dans la loi de ratification ; le projet ne doit pas corriger en silence.… |
| RT-FUTCSS-35 | P2 | confirmé | coordination manquante | L114-12-1, L114-9, L244-1, L355-2, L412-8 — Pour chaque couple, inscrire la version 2029 à l'inventaire. Lui donner la proposition actuelle, en remplaçant les seuls renvois au CPP et termes juridictionnels par ceux de la version 2029. Préférer la technique de l'am… |
| RT-FUTCSS-36 | P2 | à confirmer | conflit de source | R145-10, R146-8, R382-72 — Faire constater les dates (ou l'absence de prise d'effet) de ces versions. Pour R145-10, déclarer expressément la version LEGIARTI000036592776 sans objet. À défaut, rédiger la proposition sur une base unique en abrogeant… |
| RT-FUTCSS-37 | P2 | confirmé | incohérence du projet | L652-6, R652-26 — Proposer pour R652-26 (versions 2020 et 2029) : « Le présent article ne s'applique qu'aux plaidoiries et représentations antérieures au 1er janvier suivant l'entrée en vigueur de la loi abrogeant l'article L. 652-6. » Co… |
| RT-FUTCSS-38 | P2 | confirmé | anomalie d'inventaire | D160-6, L114-12-1, L114-9, L133-1, L133-9-5, L136-1-3, L137-26, L137-27, L137-32, L142-1, L161-24, L162-16-4, L162-22-3, — Corriger le générateur de notes : ABROGE_DIFF signifie « version remplacée à telle date », et non « article abrogé ». Pour chaque numéro listé, citer l'identifiant de la version successeur. Retirer des propositions les c… |

Le détail de chaque objection (passages cités, références, raisonnement, conséquences, options, éléments à préserver, incertitudes, preuves) figure dans `reports/dossiers/FUT-CSS.json`.

## 6. Propositions de correction (présentées séparément)

**Règle commune (correction générique RT-XCUT-01).** Pour chaque couple, inscrire la version future à l'inventaire. Lui appliquer la même modification que la proposition, dans la terminologie et avec les renvois de la version future. De préférence, rédiger la loi de réforme par **amendements ciblés**, qui valent pour toute version, plutôt que par « l'article est ainsi rédigé ». Lorsque la version future rétablit un prélèvement ou une formalité supprimé, abroger expressément la disposition du texte créateur qui la fait naître (par exemple l'art. 34 de l'ordonnance n° 2025-1247 pour L137-27). Retirer des propositions les clauses qui les confinent à la version expirante. Les rédactions ci-dessous sont des textes complets ou des passages complets. Les marques […] renvoient au texte officiel cité, inchangé.

### 6.1 Vague du 1er novembre 2026

#### Propositions de correction (rédactions complètes)

##### P-RT-FUTCSS-02 — L434-1, version applicable à compter du 1er novembre 2026 (LEGIARTI000051288500)

> Une indemnité en capital est attribuée à la victime d'un accident du travail atteinte d'une incapacité permanente professionnelle inférieure à un pourcentage déterminé. Elle est constituée :
>
> 1° D'une part professionnelle correspondant à la perte de gains professionnels et à l'incidence professionnelle de l'incapacité. Son montant est déterminé, en fonction du taux d'incapacité permanente professionnelle de la victime, par un barème forfaitaire fixé par décret et revalorisé au 1er avril de chaque année par application du coefficient mentionné à l'article L. 161-25. Elle est révisée lorsque le taux d'incapacité permanente professionnelle de la victime augmente tout en restant inférieur à un pourcentage déterminé. Cette part est due même si la consolidation intervient alors que la victime est bénéficiaire d'une pension de retraite ;
>
> 2° D'une part fonctionnelle correspondant au déficit fonctionnel permanent de la victime. Son montant est égal au nombre de points d'incapacité permanente fonctionnelle multiplié par un pourcentage d'une valeur de point fixée par un référentiel prenant en compte l'âge de la victime. Ce pourcentage et ce référentiel sont définis par arrêté des ministres chargés du travail et de la santé. Cet arrêté définit également les conditions dans lesquelles ce référentiel est actualisé. Le montant de cette part est révisé lorsque le taux d'incapacité permanente fonctionnelle de la victime augmente.
>
> Cette indemnité, pour chacune de ses deux parts, est versée dès la notification de la décision qui l'attribue, sans attendre que cette décision soit devenue définitive. L'exercice d'un recours ne suspend pas ce versement. Lorsque la victime dispose d'un choix entre une rente et une indemnité en capital, le versement du capital intervient après qu'elle a choisi cette indemnité ou, à défaut de choix, à l'expiration du délai qui lui est ouvert pour exercer cette option ; l'attente du caractère définitif de la décision n'est pas exigée. Elle est incessible et insaisissable.
>
> La suppression de l'attente du caractère définitif de la décision s'applique aux indemnités relevant du présent article qui n'ont pas encore été versées à l'entrée en vigueur de la loi portant la présente modification ainsi qu'aux indemnités attribuées ultérieurement, quelle que soit la date de consolidation de l'état de la victime et quelle que soit la rédaction du présent article qui leur est applicable. Elle ne modifie ni le montant dû, ni la revalorisation ou la révision, ni les règles de prescription, de recours et de récupération des indus applicables. Aucun second versement n'est dû au titre d'une indemnité déjà payée.

**Justification.** La structure de la loi 2025-199 est conservée. L'allègement du projet est étendu au flux des nouvelles victimes. La phrase qui renvoyait aux « champs respectifs des versions successives » est remplacée par une phrase qui couvre les deux rédactions. Dans la proposition attachée à LEGIARTI000031688413, supprimer cette même phrase finale ou la remplacer de la même manière.

**Dépendances.** R434-4 futur (option de deux mois, inchangé) ; R434-1-1, R434-1-3 et R434-1-4 futurs (révisions et déductions de capital).

##### P-RT-FUTCSS-03 — R351-37, version applicable à compter du 1er novembre 2026 (LEGIARTI000054060160)

> I.-Chaque assuré indique la date à compter de laquelle il désire entrer en jouissance de sa pension, cette date étant nécessairement le premier jour d'un mois et ne pouvant être antérieure au dépôt de la demande. Si l'assuré n'indique pas la date d'entrée en jouissance de sa pension, celle-ci prend effet le premier jour du mois suivant la réception de la demande par la caisse chargée de la liquidation des droits à pension de vieillesse.
>
> II.-L'entrée en jouissance de la pension allouée pour inaptitude au travail ne peut être fixée à une date antérieure au premier jour du mois suivant la date à partir de laquelle l'inaptitude a été reconnue.
>
> III.-L'assuré qui demande à bénéficier des dispositions de l'article L. 351-1-4 en fait la demande auprès de la caisse chargée de la liquidation de sa pension de retraite. Il en est accusé réception.
>
> Cette demande est accompagnée de la notification de rente prévue à l'article R. 434-32 et la notification de la date de consolidation prévue à l'article R. 433-17. Elle comporte en outre, s'il y a lieu, les modes de preuve mentionnés au cinquième alinéa du III de l'article L. 351-1-4.
>
> Lorsque la demande de pension de retraite est présentée par un assuré victime d'un accident du travail justifiant d'un taux d'incapacité permanente professionnelle au sens de l'article L. 434-1 A au moins égal au taux requis au I de l'article L. 351-1-4, selon les règles d'application dans le temps prévues par cet article, la caisse saisit l'échelon régional du service médical dont relève l'assuré au moment du dépôt de sa demande de pension de retraite ou, si l'assuré réside à l'étranger, l'échelon régional du service médical du lieu d'implantation de la caisse chargée de la liquidation de la pension de retraite. L'identité des lésions dont souffre l'assuré avec celles figurant sur la liste prévue à l'article R. 351-24-1 est appréciée par un médecin-conseil du service médical au vu notamment des conclusions médicales figurant sur la notification de rente. Si le médecin-conseil ne reconnaît pas l'identité des lésions avec celles figurant sur cette liste, la caisse notifie à l'assuré le rejet de sa demande de pension de retraite.
>
> Lorsque la demande de pension de retraite relève des dispositions du 1° du III de l'article L. 351-1-4, la caisse apprécie les conditions et les modes de preuve prévus au cinquième alinéa du même III, le cas échéant après accomplissement de la procédure prévue à l'alinéa précédent, sans saisine ni avis obligatoire d'une commission pluridisciplinaire. La dispense des conditions prévue au sixième alinéa du III de l'article L. 351-1-4 demeure applicable. L'assuré conserve le droit d'être entendu et de se faire assister par une personne de son choix ; les informations médicales demeurent couvertes par le secret professionnel.
>
> Dans les cas prévus aux deux alinéas précédents, le silence gardé pendant plus de quatre mois par la caisse vaut décision de rejet.
>
> La suppression du circuit de la commission s'applique à compter de l'entrée en vigueur de la modification correspondante de l'article L. 351-1-4, aux demandes n'ayant pas fait l'objet d'une décision définitive, sans nouveau dossier ni reprise du délai d'instruction. Les avis favorables déjà rendus restent opposables à la caisse. Les pensions liquidées, créances acquises et recours relatifs aux décisions antérieures sont préservés.

**Justification.** Le renvoi à L434-1 A de la version future est fusionné avec le renvoi au I de L351-1-4 du projet ; L351-1-4 en vigueur vise déjà L434-1 A. La suppression de la commission et la transition du projet sont reprises.

**Dépendances.** L351-1-4 proposé (LEGIARTI000053281659). Règlements de composition de la commission (hors lot).

##### P-RT-FUTCSS-01 — Transpositions

Pour chaque article ci-dessous, le texte est la version future officielle en entier, avec seulement les remplacements indiqués.

**L142-1 (LEGIARTI000051288452).**
- 2° : « Au recouvrement des contributions, versements et cotisations mentionnés au 5° du I de l'article L. 213-1 ; ».
- 3° : « Au recouvrement des contributions, versements et cotisations mentionnés aux articles L. 1233-66, L. 3253-18, L. 5212-9, L. 5422-6, L. 5422-9, L. 5422-11, L. 5422-12 et L. 5424-20 du code du travail, ainsi qu'aux versements mentionnés à l'article L. 1233-69 du même code qui restent dus au titre des adhésions antérieures à la suppression de ces versements ; ».
- 5° futur conservé : « A l'état d'incapacité permanente, notamment aux taux de cette incapacité, en cas d'accident du travail ou de maladie professionnelle ; ».
- Ajouter l'alinéa final du projet : « Les renvois des 2° et 3° ne rétablissent aucun prélèvement supprimé ni aucune majoration supprimée. Les litiges relatifs aux créances antérieures, aux exonérations, aux minorations, aux restitutions et aux régularisations demeurent compris dans le contentieux défini au présent article, selon les règles de fond et les dispositions transitoires propres à chaque prélèvement. »

**L434-16 (LEGIARTI000051288487).**
> La rente due aux ayants droit de la victime d'un accident mortel ou à la victime d'un accident ayant occasionné une réduction de capacité égale ou supérieure à un taux minimum ne peut être calculée sur un salaire annuel inférieur à un minimum déterminé au 1er avril de chaque année d'après le coefficient mentionné à l'article L. 161-25, compte tenu du III de l'article L. 434-2.
>
> Dans tous les cas où l'article L. 434-2 et les articles L. 434-7 et suivants déterminent en fonction du salaire annuel une rente individuelle ou collective, ou la limite assignée à l'ensemble des rentes dues aux ayants droit de la victime, le salaire annuel est le salaire réduit, le cas échéant, par application de l'alinéa suivant.
>
> Lorsqu'il s'agit de la victime de l'accident, quelle que soit la réduction de capacité subie, si son salaire annuel est supérieur au salaire minimum déterminé au premier alinéa du présent article, le calcul de la rente est effectué selon une formule dégressive dont les modalités sont déterminées par un décret en Conseil d'Etat.

Supprimer de la proposition attachée à 000031688385 la phrase sur la « date d'abrogation ». La rédaction de cette proposition n'a pas à se prononcer sur la fin de version LEGI.

**L443-1 (LEGIARTI000051288476).** Le texte est la version future en entier, avec :
- le deuxième alinéa du projet (phrases « Toutefois, les intervalles minimaux … sauf accord de la victime pour les diminuer ») ;
- l'alinéa transitoire du projet en fin d'article ;
- au quatrième alinéa, le renvoi futur « II de l'article L. 434-2 », conservé.

**L461-1 (LEGIARTI000053285183 et LEGIARTI000053285169).** Dans l'alinéa CRRMP de chacune des deux versions, remplacer « à l'article L. 315-1 » par « au I de l'article L. 315-2 ». Le reste du texte officiel est inchangé, y compris dans la version 2027 l'alinéa des deux médecins conseils et le renvoi « huitième et avant-dernier alinéas ».

**R351-12 (LEGIARTI000054425288 ; doublon 000054060166).** Le texte est la version future en entier, avec :
- l'avant-dernier alinéa remplacé par : « Pour les périodes prévues aux 1°, 2° et 3°, l'absence de mention au compte de l'intéressé ne peut, à elle seule, faire obstacle à leur prise en compte lorsque leur réalité et leur durée sont établies. » ;
- l'alinéa transitoire du projet ajouté en fin d'article ;
- le 5° futur (« incapacité permanente professionnelle au moins égale à 66 % ») conservé.

**R434-32 (LEGIARTI000054060111).**
> Au vu de tous les renseignements recueillis, la caisse primaire se prononce sur l'existence d'une incapacité permanente et, le cas échéant, sur les taux d'incapacité permanente professionnelle et fonctionnelle de celle-ci et sur le montant de la rente due à la victime ou à ses ayants droit.
>
> La décision motivée fixant les deux taux d'incapacité est immédiatement notifiée par la caisse primaire par tout moyen permettant de déterminer la date de réception, avec mention des voies et délais de recours, à la victime ou à ses ayants droit et à l'employeur au service duquel se trouvait la victime au moment où est survenu l'accident. Le double de cette décision est envoyé à la caisse d'assurance retraite et de la santé au travail.
>
> La notification adressée à la victime ou à ses ayants droit invite ceux-ci à faire connaître à la caisse, sans condition de délai ni de formulaire, s'ils demandent l'envoi, soit à eux-mêmes, soit au médecin que désignent à cet effet la victime ou ses ayants droit, d'une copie du rapport médical prévu au cinquième alinéa de l'article R. 434-31.
>
> La caisse procède à cet envoi dès réception de la demande, en indiquant que la victime, ses ayants droit ou le médecin désigné à cet effet peuvent, sans limitation à un délai de quinzaine suivant la réception du rapport, prendre connaissance au service du contrôle médical de la caisse des autres pièces médicales.
>
> Ces dispositions s'appliquent aux demandes d'accès au rapport et aux autres pièces médicales présentées à compter de l'entrée en vigueur du présent décret, y compris pour une décision antérieure. Elles ne rouvrent ni ne prolongent les délais de recours contre la décision. Les demandes déjà présentées restent valables sans renouvellement.

##### P-RT-FUTCSS-18 — L351-3 (LEGIARTI000051288449)

Voir la correction minimale de l'objection RT-FUTCSS-18 : 1° fusionné, alinéa transitoire du projet ajouté.

##### P-RT-FUTCSS-20 — R461-8, à compter du 1er janvier 2027

> Le taux d'incapacité permanente professionnelle mentionné à l'alinéa de l'article L. 461-1 relatif aux maladies caractérisées non désignées dans un tableau de maladies professionnelles est fixé à 25 %.

### 6.2 Vague du 25 décembre 2026 au 1er janvier 2030

#### Rédactions complètes proposées

##### L138-13, applicable à compter du 1er janvier 2027 (RT-FUTCSS-07)

> Les entreprises redevables de la contribution qui, en application des articles L. 162-16-4, L. 162-16-4-1, L. 162-16-5 et L. 162-16-6, ont conclu avec le Comité économique des produits de santé, pour au moins 90 % du montant remboursé par l'assurance maladie au cours de l'année civile au titre des médicaments mentionnés à l'article L. 138-10 qu'elles exploitent, une convention en cours de validité au 31 décembre de l'année civile au titre de laquelle la contribution est due et conforme aux modalités définies par un accord conclu, le cas échéant, en application du premier alinéa de l'article L. 162-17-4 peuvent être exonérées de tout ou partie du montant dû au titre de la contribution. Les entreprises assurant l'exploitation, l'importation parallèle ou la distribution parallèle des médicaments mentionnés à l'article L. 138-10 bénéficiant d'une autorisation ou d'un cadre de prescription compassionnelle mentionnés aux articles L. 5121-12 et L. 5121-12-1 du code de la santé publique et de la prise en charge associée mentionnée aux articles L. 162-16-5-1 et L. 162-16-5-2 du présent code, d'une prise en charge au titre de l'article L. 162-16-5-1-2 ou du dispositif de prise en charge d'accès direct prévu à l'article 62 de la loi n° 2021-1754 du 23 décembre 2021 de financement de la sécurité sociale pour 2022 peuvent également signer avec le comité un accord prévoyant le versement d'une remise.
>
> [deuxième à quatrième alinéas : texte de la version LEGIARTI000051287306, inchangé]
>
> Avant la date prévue au II de l'article L. 138-15, le Comité économique des produits de santé notifie à chaque entreprise le montant de la remise exonératoire dont elle est redevable.
>
> Pour les accords conclus à compter de l'entrée en vigueur de la loi portant ces simplifications, la signature de l'accord prévu à la seconde phrase du premier alinéa n'est pas subordonnée à la signature, par le syndicat représentatif de l'entreprise, de l'accord mentionné au premier alinéa de l'article L. 162-17-4. Pour les contributions régies par la rédaction du présent article antérieure au 1er janvier 2027 dont la liquidation n'est pas définitive, la signature n'est soumise ni à l'échéance du 31 janvier ni à cette condition. La conclusion de l'accord ne proroge pas le délai légal de paiement de la contribution. Les sommes déjà acquittées sont imputées une seule fois ; l'excédent est restitué dans les conditions de droit commun. Les accords et avantages valablement acquis restent applicables.

Justification : la loi de 2027 supprime l'échéance mais garde la condition syndicale ; la rédaction retire seulement cette condition. Dépendance : accord-cadre L162-17-4 non lu.

##### L162-23-8, applicable à compter du 1er septembre 2027 (RT-FUTCSS-11)

> I.-La dotation nationale de financement des missions d'intérêt général et d'aide à la contractualisation des établissements de santé mentionnés aux a, b, c et d de l'article L. 162-22, comprise dans l'objectif défini à l'article L. 162-23, participe notamment au financement des engagements relatifs :
> 1° A la recherche et à la formation des professionnels de santé et du personnel paramédical à l'exception des formations prises en charge par la région en application des articles L. 4244-1 et L. 4383-5 du code de la santé publique ;
> [2° à 5° et alinéas suivants jusqu'au versement aux GCS : texte de LEGIARTI000048971734, inchangé]
> Les ministres chargés de la santé et de la sécurité sociale arrêtent, en fonction du montant de la dotation nationale mentionnée au premier alinéa du présent I et dans le respect de l'objectif défini à l'article L. 162-23, le montant des dotations régionales ainsi que les critères d'attribution aux établissements.
> II.-Le montant annuel de la dotation de chaque établissement de santé est fixé par le directeur général de l'agence régionale de santé en fonction des missions d'intérêt général, des activités de soins dispensés à certaines populations spécifiques et des objectifs et des orientations prévus dans le cadre du contrat pluriannuel d'objectifs et de moyens et de leur état d'avancement ou, à défaut, dans le cadre de l'engagement contractuel spécifique prévu au I du présent article pour les engagements mentionnés aux 1° à 5°.
> Les modalités de versement et de prise en charge de cette dotation sont fixées à l'article L. 162-23-10.
> La fixation des dotations régionales et des critères d'attribution n'est pas subordonnée à l'avis préalable des organisations nationales représentatives des établissements de santé publics et privés. Cette suppression s'applique aux arrêtés pris à compter de l'entrée en vigueur de la loi portant cette suppression, y compris aux procédures en cours, sans nouvelle saisine ni reprise de la procédure. Les arrêtés antérieurs, les engagements valablement conclus et les droits au financement qui en résultent sont préservés.

Réserve : la formule « La part prévue au 2° du I de l'article L. 162-23 » du texte de 2027 vise un 2° qui n'existe pas dans le corpus. Elle est remplacée par un renvoi à l'objectif de L162-23. À vérifier contre la loi 2023-29.

##### L531-8, premier alinéa et clause finale, applicables à compter du 1er septembre 2027 (RT-FUTCSS-12)

> Par dérogation aux formalités de demande et d'adhésion prévues aux articles L. 133-5-6, L. 133-5-8 et L. 133-5-12, l'attribution du complément mentionné à l'article L. 531-5 emporte, sans démarche d'adhésion distincte de l'employeur, adhésion au dispositif simplifié prévu à l'article L. 133-5-12, sous réserve de l'accord du salarié requis par cet article. L'organisme débiteur des prestations familiales et l'organisme mentionné à l'article L. 133-5-10 mettent en œuvre cette adhésion à partir des informations nécessaires à l'attribution et aux déclarations prévues par l'article L. 133-5-8. Les déclarations nécessaires à l'identification du salarié et des rémunérations demeurent celles de l'article L. 133-5-8 ; aucune répétition de l'adhésion n'est exigée à leur occasion.
> [deuxième à sixième alinéas : texte de LEGIARTI000053281724, avec au dernier alinéa « la caisse d'allocations familiales ou la caisse de mutualité sociale agricole dont relève l'allocataire » comme dans la proposition]
> [clause transitoire de la proposition, sans sa dernière phrase « La présente rédaction ne reporte pas l'abrogation… »]

Réserve : sans l'accord du salarié, l'employeur reste rattaché au dispositif déclaratif du 4° de L133-5-6. C'est un choix à confirmer par l'auteur.

##### L223-9, rédaction unique pour 2027 et au-delà (RT-FUTCSS-13)

> I.-Le concours global mentionné au a du 3° de l'article L. 223-8 ne peut dépasser 7,75 % des contributions mentionnées aux 1° et 2° de l'article L. 241-6-2 jusqu'au 31 décembre 2026, 7,93 % de ces contributions au titre de l'année 2027 et 8,1 % de ces contributions à compter du 1er janvier 2028.
> [suite : texte proposé (LEGIARTI000046808945) inchangé — plafond de 61,4 % cantonné aux concours historiques, II à 1,87 %, neutralisation des références à L137-40 et L137-41, clause des exercices antérieurs]

##### L162-23-14-1 — disposition d'abrogation (RT-FUTCSS-08)

> L'article L. 162-23-14-1 du code de la sécurité sociale est abrogé dans toutes ses rédactions, y compris celle issue de l'article 79 de la loi n° 2025-1403 du 30 décembre 2025 de financement de la sécurité sociale pour 2026 dont l'entrée en vigueur est fixée au 1er janvier 2027. Aucun objectif annuel de volume ou d'évolution ne peut être imposé, et aucune pénalité financière infligée, sur son fondement, y compris au titre d'objectifs fixés antérieurement. [puis le second alinéa de la proposition, inchangé]

##### L137-27 — disposition d'abrogation (RT-FUTCSS-05)

> L'article L. 137-27 du code de la sécurité sociale est abrogé, y compris dans sa rédaction issue de l'article 34 de l'ordonnance n° 2025-1247 du 17 décembre 2025. Les dispositions de cet article 34 en tant qu'elles modifient l'article L. 137-27 sont abrogées. [puis les alinéas 2 à 4 de la proposition]

### 6.3 Vague du 1er janvier 2028 (articles existants)

#### Propositions de correction (rédactions complètes)

##### P-RT-FUTCSS-14 — L161-24 et L161-24-1, rédactions applicables à compter du 1er janvier 2028

**L161-24** (à rattacher à LEGIARTI000054478475) :

> Le bénéficiaire d'une pension de vieillesse d'un régime de retraite obligatoire résidant en dehors des territoires mentionnés à l'article L. 111-2 et de la Polynésie française n'est pas tenu de justifier périodiquement de son existence. L'organisme ou le service de l'Etat assurant le service de cette pension ne peut lui demander cette preuve que si des éléments objectifs font naître un doute sérieux sur son existence et si les informations dont il dispose légalement, notamment celles issues de l'échange prévu au 1° du II de l'article L. 161-24-1, ne permettent pas de lever ce doute. La seule résidence dans ces territoires extérieurs ou l'écoulement d'une année ne suffisent pas à justifier cette demande.
>
> Le contrôle est mis en œuvre dans le cadre de la mutualisation prévue à l'article L. 161-24-3. La demande indique les éléments qui la justifient et les moyens de preuve utilisables parmi ceux prévus à l'article L. 161-24-1. La même preuve ne peut être demandée à nouveau par un autre régime pour le même contrôle. Aucune obligation de déclaration périodique ni d'utilisation de données biométriques ne remplace la justification annuelle supprimée. Le délai protecteur prévu à l'article L. 161-24-2 reste applicable.
>
> Ces dispositions s'appliquent aux demandes et aux contrôles en cours à compter de l'entrée en vigueur de la loi qui les institue. Une demande annuelle en cours ne peut être maintenue que si les conditions du premier alinéa sont remplies. Une pension suspendue pour le seul défaut de justification annuelle est remise en paiement pour les échéances à compter de cette entrée en vigueur, sauf si une demande répondant à ces conditions demeure sans réponse après l'expiration du délai applicable. Les créances, restitutions et recours relatifs aux périodes antérieures demeurent régis par les dispositions qui leur étaient applicables.

**L161-24-1** (à rattacher à LEGIARTI000054358416) :

> I. – Lorsqu'elle est demandée dans les conditions prévues à l'article L. 161-24, la preuve d'existence peut être apportée, dans les conditions prévues par la loi n° 78-17 du 6 janvier 1978 relative à l'informatique, aux libertés et aux fichiers, par l'utilisation de dispositifs techniques permettant l'usage de données biométriques adapté à cette preuve. Un décret en Conseil d'Etat, pris après avis de la Commission nationale de l'informatique et des libertés, précise les moyens pouvant être utilisés à cette fin et les garanties apportées aux personnes dans l'utilisation de ces dispositifs et l'exercice de leurs droits. Il prévoit les conditions d'utilisation par les personnes concernées des outils numériques leur permettant d'effectuer cette démarche.
>
> II. – La preuve d'existence peut également être apportée :
> 1° Par un échange automatique de données entre l'organisme ou le service mentionnés à l'article L. 161-24 et un organisme ou un service chargé de l'état civil du pays de résidence du bénéficiaire ;
> 2° Par un contrôle sur place par un organisme tiers de confiance conventionné ;
> 2° bis En fournissant un certificat d'existence authentifié par une autorité locale habilitée figurant sur une liste établie annuellement par le ministère des affaires étrangères ;
> 3° En fournissant un certificat d'existence visé par le service consulaire du pays de résidence du bénéficiaire.
>
> III. – Le bénéficiaire choisit librement entre les modes de preuve prévus aux I et II. Aucune preuve ne lui est demandée lorsque l'échange prévu au 1° du II suffit à établir son existence.

Justification : ces rédactions conservent la suppression décidée par le projet, l'extension à Mayotte et les quatre modes de preuve favorables de la loi 2025-199. Elles retirent seulement le caractère obligatoire de la biométrie, conformément à l'orientation qui interdit toute formalité de remplacement. Dépendances : versions de 2028 de L161-24-2 et L161-24-3 (non lues) ; textes réglementaires du contrôle d'existence. Le III de L161-24-1 est un ajout du projet, à valider.

##### P-RT-FUTCSS-15 — L241-13 et L752-3-2, versions de 2028

- **L241-13** (LEGIARTI000054466849) : texte intégral des I à VII de la proposition courante (proposed_sha256 `fefc051c58f6dcaf25dcbb6f8bfb41e7f4f8acaeab377e8fa9760a8b26d0f6cb`), sans changement, **sans VIII**. Les adaptations mahoraises relèvent de L759-1 (SMIC et plafond mahorais) et de L759-10 (plancher de 88 % du SMIC jusqu'en 2035, puis droit commun), à conserver. Ne pas réintroduire le plancher de 60 %.
- **L752-3-2** (LEGIARTI000054466922) : texte officiel de 2028 (I avec Mayotte, sans VIII), en insérant après le IV le IV bis de la proposition courante, mot pour mot.

##### P-RT-FUTCSS-22 — L222-2-1, rédaction applicable à compter du 1er janvier 2028

> La branche mentionnée au 3° de l'article L. 200-2 prend en charge :
> 1° Le financement des allocations mentionnées au dernier alinéa de l'article L. 643-1, au chapitre V du titre Ier du livre VIII du présent code et à l'article 2 de l'ordonnance n° 2004-605 du 24 juin 2004 simplifiant le minimum vieillesse ;
> 2° Les sommes représentant la prise en compte, dans la durée d'assurance, par le régime des salariés agricoles, le régime des non-salariés agricoles, le régime d'assurance vieillesse des professions libérales et la Caisse nationale des barreaux français :
> a) Des périodes mentionnées aux 1°, 3° et 8° de l'article L. 351-3 du présent code ;
> b) Des périodes pendant lesquelles les assurés ont bénéficié des allocations mentionnées aux articles L. 1233-68, L. 5422-1, L. 5423-1 et L. 5424-25 du code du travail, de l'indemnité horaire mentionnée au II de l'article L. 5122-1 du même code ou de la rémunération mentionnée au troisième alinéa de son article L. 1233-72 ;
> c) Des périodes pendant lesquelles l'assuré, en l'absence complète d'activité, a bénéficié d'un revenu de remplacement versé par son entreprise en application d'un accord professionnel national mentionné à l'article L. 5123-6 du code du travail ;
> 3° Abrogé ;
> 4° Les dépenses mentionnées au I de l'article 49 de la loi n° 2002-73 du 17 janvier 2002 de modernisation sociale ;
> 5° Les sommes représentant la prise en compte, par les régimes d'assurance vieillesse de base, des périodes de volontariat du service national de leurs assurés ;
> 6° Abrogé ;
> 7° Les sommes correspondant à la prise en charge prévue au second alinéa de l'article L. 6243-3 du code du travail ;
> 8° Le remboursement à la caisse de prévoyance sociale de Saint-Pierre-et-Miquelon des dépenses correspondant à l'application au régime d'assurance vieillesse de cette collectivité des avantages non contributifs mentionnés aux 1° à 5° et 7° du présent article. Ce remboursement intervient dans les conditions prévues par la loi n° 87-563 du 17 juillet 1987 portant réforme du régime d'assurance vieillesse applicable à Saint-Pierre-et-Miquelon.
> Les sommes mentionnées aux 2° et 5° sont calculées sur une base forfaitaire, dans des conditions déterminées par décret en Conseil d'État.
> Pour les relations de travail de droit privé conclues à compter de l'entrée en vigueur de la loi instituant le contrat de travail unique, les prises en charge prévues au présent article restent ouvertes aux périodes et situations éligibles. La durée d'un accompagnement ou d'une formation ne fixe pas le terme de l'emploi. Pour l'application du 7° à ces relations, la prise en charge demeure attachée à la période d'apprentissage. Les périodes et créances relevant de contrats antérieurs conservent leur régime.

Dépendance : dispositions transitoires non codifiées de l'ordonnance 2026-647 relatives aux périodes antérieures à 2028 (non lues). La proposition ne doit pas les reproduire de mémoire.

##### P-RT-FUTCSS-23 — L162-16-4 et L245-6

Dans la proposition de L162-16-4, au I, premier alinéa : « L. 1413-4 » → « L. 3133-1 ». Dans la proposition de L245-6, III, A : « 7° Celles acquises par le ministre chargé de la santé en application de l'article L. 3133-1 du code de la santé publique. » Rattacher ces deux propositions aux versions de 2028. Leur date de rattachement est celle du décret d'application de l'art. 41 XI de la loi 2026-791.

##### P-RT-FUTCSS-24 — L325-1

Version de 2028 : proposition courante, en retirant les mots « , ou à Mayotte » aux 4°, 5°, 6° et 7° (deux fois au 7°) du II.

##### P-RT-FUTCSS-25 — L757-1

Accepter la version de 2028, en remplaçant au c) « au troisième alinéa de l'article L. 752-9-1 » par « à l'article L. 752-9-1 ». Lever la réserve sur L811-14 avant de qualifier de neutre la disparition de l'ancien alinéa sur les départements d'outre-mer.

### 6.4 Vague du 1er janvier 2028 (55 nouveaux numéros mahorais)

#### Rédactions complètes proposées (les plus importantes)

##### P-RT-FUTCSS-16 : complément du VII de L136-8 proposé (paragraphe entier)
> VII.-La baisse à 6,6 % prévue au 1° du I s'applique aux rémunérations versées à compter de la date fixée par une loi de financement de la sécurité sociale qui en couvre le coût par des ressources pérennes ou des économies récurrentes identifiées et prévoit la compensation des organismes affectataires. Tant que ces dispositions de financement ne sont pas entrées en vigueur, le taux de 9,2 % demeure applicable à ces rémunérations, sous réserve des exonérations et régimes plus favorables. La baisse ne modifie ni l'assiette, ni ses abattements, ni les exclusions et exonérations applicables, y compris aux situations futures éligibles. Les rémunérations antérieures conservent leur régime et leurs droits à régularisation et à restitution. Pour l'application de l'article L. 759-5, le taux de 6,6 % se décompose en une part déductible et une part non déductible dans les conditions prévues à l'article 154 quinquies du code général des impôts ; chacune de ces parts est multipliée par le facteur de convergence correspondant, sans que le taux applicable à Mayotte puisse excéder celui qui résulterait de l'application du même facteur au taux de 9,2 %.

Justification : rendre le taux déterminable sans inventer de taux ; la dernière clause garantit que la baisse ne peut pas, par un effet de répartition, aboutir à une hausse à Mayotte. Dépendance : article 154 quinquies du CGI (lot fiscal) ; date de la LFSS de financement.

##### P-RT-FUTCSS-30 : 11° de L759-23 (rédaction complète du 11°)
> 11° a) L'article L. 755-19 est applicable, dans la rédaction suivante, selon la période d'application jusqu'au 31 mars 2029 :
> « Art. L. 755-19. - I. - […] (premier alinéa du I au sixième alinéa du II inchangés) […]
> « Plusieurs allocations de base ne peuvent se cumuler que pour les enfants issus de naissances multiples ou en cas d'adoptions multiples simultanées.
> « L'allocation de base n'est pas cumulable avec le complément familial défini à l'article L. 755-16. L'allocation de base est cumulable avec les allocations familiales et leurs majorations pour âge servies au titre d'un seul enfant à charge, lorsque les conditions propres à chacune de ces prestations sont remplies. » ;
> b) A compter du 1er avril 2029 et jusqu'au 31 mars 2030, l'article L. 755-19 est applicable, dans la rédaction suivante :
> « Art. L. 755-19. - La prestation d'accueil du jeune enfant est attribuée dans les collectivités mentionnées à l'article L. 751-1 dans les conditions définies au titre III du livre V du présent code.
> « L'allocation de base est cumulable avec les allocations familiales et leurs majorations pour âge servies au titre d'un seul enfant à charge, lorsque les conditions propres à chacune de ces prestations sont remplies.
> « L'allocation de base et la prestation partagée d'éducation de l'enfant ne sont pas cumulables avec le complément familial défini à l'article L. 755-16. » ;

Transition : celle de L755-19 proposé (périodes courant à compter de la loi de réforme). Les alinéas marqués […] reprennent mot pour mot le 11° a) officiel.

##### P-RT-FUTCSS-33 : L752-9-7 (article entier)
> La caisse de sécurité sociale de Mayotte décide de ses opérations immobilières et de la gestion de son patrimoine, après avis de son conseil. Les caisses nationales mentionnées aux articles L. 221-1, L. 222-1, L. 223-1 et L. 225-1 exercent sur ces opérations un contrôle a posteriori, qui ne peut les subordonner à un agrément ni à une décision préalable. Les opérations engagées avant l'entrée en vigueur de la présente rédaction restent régies par les règles qui leur étaient applicables.

##### P-RT-FUTCSS-27 (extrait le plus lourd) : 2° de L759-20
> 2° Au quatrième alinéa du même article, les mots : « tiers du minimum prévu au premier alinéa de l'article L. 351-10 » sont remplacés par les mots : « quart du montant prévu à l'article L. 815-1 » ;

La même technique (rang exact au lieu de « dernier alinéa ») s'applique à L759-24, deuxième alinéa (« et le troisième alinéa »), et à L752-9-6 (« au premier alinéa de l'article L. 227-3 »). Option préférée : placer les transitions des propositions hors du corps des articles cibles ; les renvois officiels restent alors exacts.

##### P-RT-FUTCSS-32 : ajout au II de L241-3 proposé
> Les salariés relevant de la caisse de sécurité sociale de Mayotte, y compris les salariés employés dans le secteur agricole mentionnés au b du 3° de l'article L. 752-9-1, ne sont concernés qu'après l'entrée en vigueur des dispositions organisant leur raccordement et leur financement.

##### P-RT-FUTCSS-28 : article de coordination de la loi de réforme
> I. - Les articles L. 759-6, L. 759-7 et L. 759-11 du code de la sécurité sociale sont abrogés à compter de la date d'effet de l'abrogation, respectivement, de l'article L. 137-16, des articles L. 137-40 et L. 137-41 et de l'article L. 380-2 du même code. Les faits générateurs, sommes et années d'assujettissement antérieurs restent régis à Mayotte par les facteurs de convergence alors applicables.
> II. - Au deuxième alinéa du I de l'article L. 753-4-1 du même code, les mots : « et l'article L. 174-4 » sont supprimés à compter de la suppression du forfait journalier.

### 6.5 Vague du 1er janvier 2029 et bornes techniques 2222-02-22

#### Propositions de correction

##### P-17 — L861-5, rédaction unique applicable dès l'entrée en vigueur de la réforme (base : LEGIARTI000048702075)

> La demande de protection complémentaire, accompagnée de l'indication du choix opéré par le demandeur en application de l'article L. 861-4, est faite auprès de la caisse assurant la prise en charge des frais de santé du demandeur. Elle est valable au titre de l'ensemble des personnes rattachées au foyer, y compris si elles ne relèvent pas de cet organisme pour la prise en charge de leurs frais de santé et, le cas échéant, pour le bénéfice des prestations mentionnées à l'article L. 861-3.
>
> Les services sociaux et les établissements de santé apportent leur concours aux intéressés dans leur demande de protection complémentaire. Les associations et organismes à but non lucratif qui proposent ce concours peuvent également l'apporter sans agrément particulier. Ces services, établissements, associations et organismes sont habilités, avec l'accord du demandeur, à transmettre la demande et les documents correspondants à l'organisme compétent. Cette transmission est effectuée sans délai. Il en est de même des organismes chargés du service des prestations sociales et familiales.
>
> Les organismes chargés de la prise en charge des frais de santé informent les bénéficiaires de l'allocation mentionnée à l'article L. 815-24 et les bénéficiaires de l'allocation mentionnée aux articles L. 821-1 et L. 821-2 qui ne remplissent pas les conditions prévues aux 2° et 3° de l'article L. 861-2 de leur éligibilité potentielle au bénéfice de la protection complémentaire et leur proposent un accompagnement dans leur démarche d'ouverture et de renouvellement du droit à cette protection.
>
> La décision est notifiée au demandeur par le directeur de l'organisme assurant la prise en charge de ses frais de santé. Cette décision doit être notifiée au demandeur dans un délai maximal fixé par décret et peut faire l'objet d'un recours contentieux en application des articles L. 142-3 et L. 142-4 et du 2° de l'article L. 142-8. En l'absence de notification de la décision au demandeur, la demande est considérée comme acceptée.
>
> [cinquième alinéa (prise d'effet, attribution anticipée, interruption) : texte officiel inchangé]
>
> Les droits reconnus conformément aux articles L. 861-1 à L. 861-4 sont attribués pour une période d'un an renouvelable, à l'exception de situations déterminées par décret visant à garantir la continuité de ces droits en cas d'évolution de la composition du foyer en cours de droit. Une nouvelle admission ou un renouvellement du droit à la protection complémentaire en matière de santé ne peut être refusé au seul motif que l'assuré n'a pas acquitté des participations dues au titre de droits ouverts précédemment. Le recouvrement de ces participations, les remises ou réductions de dette prévues à l'article L. 861-10, les aides accordées par un organisme mentionné à l'article L. 861-4 en raison de la précarité de l'assuré et les délais de paiement accordés par l'organisme gestionnaire demeurent applicables. Le respect d'un échéancier accepté ne peut entraîner la perte d'un avantage antérieurement reconnu au titre de la régularité du paiement.
>
> [septième alinéa (renonciation sans frais) : texte officiel inchangé]
>
> Le droit à la protection complémentaire en matière de santé mentionnée à l'article L. 861-3 est renouvelé automatiquement à l'issue d'une période d'un an pour les bénéficiaires du revenu de solidarité active et les jeunes majeurs mentionnés à la dernière phrase du deuxième alinéa de l'article L. 861-2, les bénéficiaires de l'allocation mentionnée à l'article L. 815-1 ou d'une des allocations mentionnées à l'article 2 de l'ordonnance n° 2004-605 du 24 juin 2004 simplifiant le minimum vieillesse, dès lors qu'ils continuent de bénéficier de l'une de ces allocations. Ce droit est également renouvelé automatiquement à l'expiration de la période d'un an pour les personnes qui, lors de son attribution, ont été réputées satisfaire les conditions du 2° de l'article L. 861-1 en application des 2° à 5° de l'article L. 861-2, sous réserve qu'elles satisfassent, à la date du renouvellement, l'ensemble des conditions prévues aux mêmes 2° à 5°. Le montant de leur participation est déterminé, le cas échéant, à chaque renouvellement. Pour les bénéficiaires qui ne relèvent d'aucun des renouvellements automatiques prévus aux deux phrases précédentes, lorsque les informations exactes, à jour et légalement disponibles établissent que les conditions du droit demeurent remplies, l'organisme assurant la prise en charge des frais de santé renouvelle le droit sans nouvelle demande ni nouveau dépôt des mêmes pièces. Le bénéficiaire est informé de ce renouvellement et, le cas échéant, du montant de sa participation ; son choix de l'organisme gestionnaire et son droit de renoncer sans frais demeurent garantis. Cette procédure n'étend pas les accès aux données et ne dispense pas de fournir les seules informations nécessaires qui ne sont pas légalement disponibles. [suite : transitions de la proposition LEGIARTI000046806509, inchangées, y compris « sans priver les personnes déjà admises au renouvellement automatique de ce bénéfice »]

**Justification.** Cette rédaction conserve les trois apports de la loi de 2023, qui sont des faveurs déjà applicables : ciblage de l'information, renouvellement automatique des présumés éligibles, et maintien sous condition des 2° à 5°. Elle y ajoute les allègements du projet. La seule adaptation est le renvoi « qui ne relèvent d'aucun des renouvellements automatiques », qui évite le chevauchement des deux mécanismes.

**Dépendances.** L861-2 en vigueur (LEGIARTI000048702111, retained_unchanged) ; R861-18 et R861-21 (non lus) ; décret d'application de l'art. 45 de la loi de 2023 (non consulté).

##### P-35 — Transpositions sur les versions 2029 (ordonnance n° 2025-1091)

Pour chaque article, le texte est la version 2029 officielle en entier, à laquelle on applique la même modification que la proposition :
- **L114-9 (LEGIARTI000054786009)** : au I, deuxième alinéa, remplacer les deuxième et troisième phrases par « À compter de l'entrée en vigueur de la loi, aucune synthèse annuelle distincte de ces opérations n'est exigée au titre du présent I, y compris au titre d'une période antérieure. Les synthèses déjà transmises n'ont pas à être refaites. ». Garder au IV « L. 3413-5 » et « L. 4415-5 ».
- **L355-2 (LEGIARTI000052850993)** : supprimer la seconde phrase du premier alinéa, garder « L. 4326-18 » au quatrième alinéa et ajouter l'alinéa transitoire de la proposition.
- **L244-1 (LEGIARTI000052846151)** : garder « tribunal contraventionnel » et ajouter le second alinéa de la proposition.
- **L114-12-1 (LEGIARTI000052851016)** : ajouter au deuxième alinéa les deux phrases de réemploi de la proposition et garder le 6° recodifié.
- **L412-8 (LEGIARTI000052850958)** : reprendre la proposition, avec au 5° « des articles L. 4222-1 à L. 4222-6 du code de procédure pénale ».

Technique préférée : les amendements ciblés valent pour toutes les versions. Exemple : « Au I de l'article L. 114-9, les deuxième et troisième phrases du deuxième alinéa sont remplacées par… ».

##### P-37 — R652-26 (versions LEGIARTI000039348152 et LEGIARTI000052846149)

> [texte officiel de la version en vigueur à la date considérée, inchangé]
> Le présent article ne s'applique qu'aux plaidoiries et représentations intervenant avant le 1er janvier de l'année suivant celle de l'entrée en vigueur de la loi portant abrogation de l'article L. 652-6. Les exemptions qu'il prévoit demeurent applicables à ces plaidoiries et représentations.

Dépendance : R652-27 à R652-35, non lus.

##### P-36 — R145-10

Faire constater que la version LEGIARTI000036592776 (décret n° 2018-79) est sans objet, puisque le décret n° 2025-905 la remplace. À défaut, abroger expressément, pour R145-10, le 5° de l'article 5 du décret n° 2018-79. Rattacher la proposition à la seule version issue du décret de 2025.

## 7. Incertitudes restantes et éléments non examinés

- **Commun.** JORF non consulté (403) : la nature des modifications est déduite des différences LEGI. La seconde passe est en cours : de nombreux articles réglementaires sont encore « pending » (R351-12, R351-37, R434-32, R145-10, R146-x, R382-72, L861-5…). Les dates de décrets d'entrée en vigueur (loi n° 2026-791 art. 41 XI ; loi n° 2023-1250 art. 45 II ; loi n° 2026-555 art. 3 IV) n'ont pas été trouvées dans l'instantané.
- **Hors périmètre, signalés sans être qualifiés.**
  - R412-6, R413-7, R844-5 et l'annexe I à R434-32 gardent des renvois à des alinéas de l'ancien L434-2 (conflit de source probable, criblage seulement).
  - R443-1 reste maintenu alors que les notes de L443-1 demandent sa coordination.
  - Le motif du maintien de D160-6 contredit la proposition de L160-13.
  - L162-16-5-4-1 (2028) vise « l'agence » alors que l'acheteur devient le ministre.
  - La proposition de L245-6 conserve un plafond « prévu au E » visé par L138-12 en 2027 (vu par extrait).
  - Une version de L241-13 LEGIARTI000053284930 apparaît parmi les preuves citées, sans examen ici.

### 7.1 Vague du 1er novembre 2026

#### Non examiné

- Textes JORF primaires (loi 2025-199 art. 90 ; loi 2025-1403 art. 95 et 96 ; décrets 2026-354, 2026-355 et 2026-901) : seuls les NOTA et LIENS LEGI ont été lus.
- R142-17-2, D461-27, R443-1, R412-6, R413-7, R844-5 et l'annexe I à R434-32 : criblage seulement, pas de lecture intégrale.
- Les règlements de la commission pluridisciplinaire et L315-2.

### 7.2 Vague du 25 décembre 2026 au 1er janvier 2030

#### Non lu ou non vérifié

Textes primaires au JORF : ordonnances 2025-1247 et 2026-671, lois 2023-1250, 2023-29, 2025-199, 2025-1403, 2026-534, 2026-492, 2022-1726 et 2025-127, décrets 2026-809 à 812 et 2025-1338. Aucun n'a été consulté : les contenus sont déduits des versions LEGI de l'instantané. Non lus : CIBS L161-1 et L180-1, CSP L6154-1 et L3133-1, accord-cadre L162-17-4. Le texte modificatif des versions futures de L223-9 n'a pas pu être identifié (ni LIENS créateurs, ni NOTA). La proposition L245-6 (plafond E du III, lot F3) n'a été vue que par extrait.

### 7.3 Vague du 1er janvier 2028 (articles existants)

#### Non lu ou non vérifié

- Le texte JORF des ordonnances 2026-647 et 2026-648, de la loi 2026-791 et de la loi 2026-534 n'a pas été lu. Les instructions de modification (ciblées ou « ainsi rédigé ») sont donc déduites de la différence entre versions, ce qui constitue une limite pour la qualification « sans effet ».
- Le décret d'entrée en vigueur de l'art. 41 III de la loi 2026-791 n'est pas dans le corpus.
- L811-14 est absent du corpus actif. Les versions de 2028 de L161-24-2 et L161-24-3, les L759-x (sauf L759-10, L759-7, L759-6 et L759-11, survolés pour localiser le VIII de L241-13) et L752-9-1 (lu seulement pour le renvoi de L757-1) relèvent du fork des nouveaux numéros.
- Aucune consultation Légifrance n'a été faite : toutes les preuves proviennent de l'instantané 20261026T230545Z.

### 7.4 Vague du 1er janvier 2028 (55 nouveaux numéros mahorais)

#### Non lu / limites
- Texte JORF de l'ordonnance 2026-647 (rapport au Président, articles 1 à 7 et 10 et suivants) non consulté. Le régime mahorais antérieur (ordonnances 96-1122 et 2002-411) est absent du corpus.
- Les articles existants que l'ordonnance modifie en 2028 (successeurs : L111-2, L751-1, L752-1, L752-2, L752-8, L757-1, L161-24, L162-20-1, L222-2-1, L241-13, L325-1, L713-10, L713-19, L752-3-2) relèvent d'autres lots. L752-1 est traité par RT-UNION-05 et n'est pas recompté.
- Les articles réglementaires mahorais (R et D) d'application n'ont pas été recherchés.
- L'article 154 quinquies du CGI et les décrets de convergence n'ont pas été lus.
- La constitutionnalité (article 73) des adaptations restrictives n'a pas été examinée.
- Revue IA : elle ne vaut pas validation par un juriste.

### 7.5 Vague du 1er janvier 2029 et bornes techniques 2222-02-22

#### Non lu

- JORF des ordonnances et lois citées (Légifrance : HTTP 403 le 2026-10-26).
- R861-18, R861-21, R652-27 à R652-35 et le décret d'application de l'art. 45 de la loi n° 2023-1250.
- Dates effectives des renouvellements des conseils de l'ordre et de la CAVIMAC.

## 8. Couverture réelle

- 45 couples rewrite_draft sur 45, lus en entier. L311-3 version 2030 a été établi par différence exhaustive.
- 73 couples retained_unchanged sur 73, et 60 nouveaux numéros sur 60, lus en entier par cite.py. Le décompte est de 55 nouveaux numéros pour Mayotte, et non 52.
- Articles cibles lus pour les renvois : L174-4, L137-16, L137-40, L137-41, L380-2, L652-6, L533-1, L245-12, R613-9, L281-4, L861-2, L351-1-4, L136-8, L162-23, L162-30-2, L162-30-4, L162-30-4-1, L133-5-12, ainsi que les cibles des articles mahorais (voir 4.4).
- Non lus : JORF ; L811-14 (absent) ; versions 2028 de L161-24-2 et L161-24-3 ; R861-18, R861-21, R652-27 à R652-35 ; décrets mahorais ; CGI 154 quinquies ; CIBS L161-1 et L180-1 ; CSP L3133-1.

Revue IA : ces constats sont provisoires et ne valent pas validation par un juriste.
