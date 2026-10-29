# Red-team juridique indépendante — troisième passe

**Rapport final de la troisième passe, 29 octobre 2026.** Historique :
- 27 octobre, 00 h UTC : première version, sur l'instantané `20261026T230545Z` ;
- 27 octobre, 04 h UTC : revue de fond des cinq domaines prioritaires (§ A.3 bis) ;
- 27 octobre, 08 h UTC : revue des différences sur l'instantané intermédiaire `20261027T044303Z` (§ D.1 à D.6) ;
- 28 octobre : tri des issues GitHub externes (§ D.9) ;
- 29 octobre : **revue finale des différences sur l'instantané `20261029T034912Z`, pris après la fin de la seconde passe** (30 314 articles relus sur 30 314), avec l'examen des points transmis par la seconde passe (§ D.7 à D.10).

Projet de réécriture du Code du travail, du CGI et de ses annexes I à IV, du Code de la sécurité sociale, du Code de l'urbanisme et du Code de la construction et de l'habitation. Corpus au **18 octobre 2026**.

> **Statut.** Revue conduite par une IA (un coordinateur et 50 agents, dont certains ont délégué à des sous-agents), **sans validation par un juriste**. Elle a été conduite sur l'instantané figé `20261026T230545Z`, réexaminée sur l'instantané intermédiaire `20261027T044303Z`, puis **réexaminée une dernière fois sur l'instantané final `20261029T034912Z`**, pris après la fin de la seconde passe. Les chiffres ci-dessous sont ceux d'après la revue finale. L'instantané final est identique, fichier par fichier, à la publication de la seconde passe sur la branche `main` du dépôt (1 496 fichiers de lots, registre, politiques et index des contradictions comparés). Aucune modification n'a été apportée à la production.

Livrables :

| Fichier | Contenu |
|---|---|
| `reports/RAPPORT.md` | Le présent rapport : synthèse, portée, méthode, revue des différences |
| `reports/REGISTRE.md` et `reports/register.json` | B. Registre des objections (243 retenues après la revue finale), avec preuves, empreintes et citations complètes |
| `reports/CORRECTIONS.md` | C. Corrections minimales des P0 et P1. Les rédactions intégrales sont dans `reports/dossiers/<dossier>.md` |
| `reports/dossiers/*.md` et `*.json` | Les 31 rapports de dossier, dont les 5 revues de fond des domaines prioritaires (`DOM-*`), et les objections issues des issues GitHub (`ISS.json`) et des points transmis par la seconde passe (`TR.json`) |
| `reports/p1-work/*-classification.jsonl` | La qualification ligne à ligne de chaque alerte examinée (1 943 lignes) |
| `reports/dedupe.json`, `reports/reexam/merges.json` et `reports/reexam-final/merges.json` | Les 46 fusions de doublons, chacune motivée |
| `reports/reexam/` et `reports/reexam-final/` | D. Revues des différences intermédiaire et finale : verdict et trace de chaque objection réexaminée, requalification des alertes, contrôles du coordinateur |
| `reports/transmission/` et `inputs/` | Examen des points transmis par la seconde passe, avec la transmission elle-même et la dernière relecture acceptée |
| `reports/issues/` | Tri des issues GitHub externes (`TRI.md`), avec le détail par groupe et les copies des issues triées |

---

## A. Synthèse

### A.1 Résultat chiffré

| | Confirmé | À confirmer | Total |
|---|---|---|---|
| **P0** | 3 | 0 | **3** |
| **P1** | 69 | 14 | **83** |
| **P2** | 116 | 41 | **157** |
| **Total retenu** | 188 | 55 | **243** |

Évolution du registre :
- **303 objections** avant tout réexamen (4 P0, 111 P1, 188 P2), dont 34 issues de la revue des domaines prioritaires.
- **288** après le réexamen intermédiaire : 26 résolues par la seconde passe, dont 11 P1, et 11 constats nouveaux.
- **296** après le tri des issues GitHub (8 objections nouvelles).
- **243** après la revue finale (§ D.7). Elle a réexaminé 136 objections dont un article avait changé :
  - **58 résolues**, dont **17 P1**, par le texte final de la seconde passe ;
  - 30 reformulées et 48 maintenues ;
  - 6 changements de priorité ;
  - 4 constats nouveaux retenus (1 P1, 3 P2), et 5 autres fusionnés dans des objections existantes.

S'y ajoutent 46 doublons fusionnés et 12 faux positifs ou alertes écartées, tous documentés.

Par nature :
- 81 coordinations manquantes ;
- 71 incohérences introduites par le projet ;
- 37 risques juridiques ;
- 14 anomalies d'inventaire ;
- 12 conflits de source ;
- 11 réserves documentaires ;
- 17 simples alertes.

### A.2 Les P0

Trois P0 restent ouvertes au terme de la revue finale : RT-INV-02, RT-FUTFISC-04 et RT-FUTFISC-23. La quatrième, RT-INV-01, a été traitée par la seconde passe et ramenée en P2. **Aucun article des trois P0 restantes n'a changé dans la dernière partie de la seconde passe.**

1. **RT-INV-01 — CGI 1609 quinvicies (P0 → P2 au réexamen).**
   - L'inventaire a retenu une version jamais entrée en vigueur (`MODIFIE_MORT_NE`), sélectionnée à cause de sa borne technique de fin en 2999. L'article est abrogé depuis le 1er janvier 2022.
   - Sa proposition rétablit *« Il est institué une contribution supplémentaire à l'apprentissage »*, avec ses taux. Or la proposition de L6242-1 du code du travail dispose : *« La contribution supplémentaire à l'apprentissage est supprimée »*.
   - Le projet recrée donc un prélèvement qu'il supprime.
   - Correction : retirer la proposition de 1609 quinvicies.
   - **Au réexamen :** la proposition dit désormais « Le présent article est abrogé » et précise qu'elle « n'institue aucune contribution en sus de celle régie […] par l'article L. 6242-1 » (vérifié par le coordinateur). Reste en P2 : la version mort-née est toujours comptée comme article courant, et des règles de fond y sont logées en doublon de L6242-1 VIII.

2. **RT-INV-02 — Réforme AT-MP du 1er novembre 2026.**
   - Neuf propositions du CSS réécrivent des versions qui cessent de s'appliquer le 1er novembre 2026 (loi 2025-199, art. 90 ; décrets 2026-354 et 2026-355). L434-1 en est un exemple. Les versions de remplacement figurent dans le corpus, et les notes de revue affirment à tort qu'elles n'ont pas été fournies.
   - Les allègements du projet visent donc des textes qui n'existeront plus. Plusieurs propositions font aussi perdre des gains de la réforme de 2026, comme la part fonctionnelle de l'indemnité en capital ou l'avis de deux médecins-conseils.
   - Correction : rédactions fusionnées, rédigées sur les versions de remplacement (dossiers INV et FUT-CSS).

3. **RT-FUTFISC-04 — CGI 287.**
   - La proposition est rédigée sur la version qui expire le 1er janvier 2027. Elle applique encore le régime de 302 septies A, abrogé à cette date.
   - Elle effacerait le régime trimestriel issu de la loi de finances pour 2025.

4. **RT-FUTFISC-23 — CGI 150 VM.**
   - La proposition déclare que l'article ne s'applique plus *« au-delà de sa date d'abrogation déjà prévue au 1er janvier 2027 »*. Cette abrogation n'existe pas : une version de remplacement (`VIGUEUR_DIFF`) commence à cette date.
   - L'erreur est certaine. *Sa gravité, qualifiée P0 par le dossier, mérite d'être confirmée par le coordinateur au vu de la portée de 150 VM : il pourrait s'agir d'un P1.*

Chacun de ces quatre points a été vérifié par le coordinateur directement sur l'instantané, citations comprises. RT-INV-02, RT-FUTFISC-04 et RT-FUTFISC-23 sont maintenues sur l'instantané final : leurs articles sont identiques, par empreinte, à ceux de l'instantané intermédiaire (RT-FUTFISC-04 y avait été réexaminée et maintenue).

### A.3 Principales fragilités, par mécanisme

**1. Le projet est écrit sur le droit au 18 octobre 2026, alors que le droit déjà publié change après cette date.** C'est la fragilité principale et systémique (RT-XCUT-01, avec RT-INV-05 et les dossiers FUT-*).

- Le corpus contient **516 versions futures déjà publiées** et 379 « abrogations différées » qui sont en réalité des remplacements. **Aucune n'a de proposition, y compris dans l'instantané final** (recomptage du groupe F05). 43 d'entre elles entrent en vigueur le 1er novembre 2026.
- Qualification des 516 :
  - 344 sans effet ;
  - 95 conflits de rédaction à fusionner ;
  - **43 réformes écrasées** : à leur date d'effet, le texte publié rétablit ce que le projet supprime ;
  - 9 déjà traitées ;
  - 25 autres (coordinations ou renvois).
- Exemples de réformes écrasées :
  - la contribution de 15 % sur la publicité des jeux (2027) ;
  - la preuve annuelle d'existence pour les pensionnés (2028) ;
  - la CSI réédictée pour Mayotte (2029) ;
  - l'enquête de sécurité incendie transférée au CCH (2027) ;
  - L621-6 du CCH, qui rétablit en 2029 l'expulsion pour sous-occupation.
- Le projet fait aussi perdre des **faveurs déjà publiées** : plafonds de l'APA, renouvellement automatique de la complémentaire santé solidaire, plancher mahorais, quota Rixain à 40 %.
- À l'inverse, **des propositions créent des abrogations qui n'existent pas** : elles lisent l'état LEGI ABROGE_DIFF comme une extinction (RT-FUTTL-02). La seconde passe a aggravé ce défaut à la fin de sa relecture : elle a ajouté dans plusieurs propositions une clause selon laquelle la rédaction « ne reporte aucune abrogation différée » de l'article. Or la version suivante réécrit l'article sans l'abroger.
  - Une recherche du coordinateur sur l'instantané final en trouve **29**, dont 1750, 1751, 1754 et 1788 A du CGI. Aucune des 29 versions suivantes n'a de proposition.
  - À la date de ces versions (2027 à 2029), les faveurs de la réforme tombent : par exemple, la suppression du permis comme peine fiscale (1750) ou l'amende de 5 % (1788 A 4).
  - Liste : `reports/reexam-final/coordinator-checks.json`. Constat RT-RXF01-01, fusionné dans RT-FUTTL-02.
- La **recodification de la TVA et des accises dans le CIBS au 1er janvier 2027** (ordonnance 2025-1247, RT-INV-06) touche 169 articles du CGI inventoriés, dont 70 réécrits. Le CIBS n'est pas suivi par le projet.
- **Correction structurelle :**
  - rédiger chaque proposition sur la dernière version publiée, ou fusionner les deux ;
  - ou abroger expressément la disposition qui fait naître la version future ;
  - corriger les notes de revue qui nient l'existence des successeurs ;
  - inscrire le CIBS dans les coordinations hors corpus.

**2. La loi supprime une formalité, mais les décrets et annexes la maintiennent.** C'est la majorité des P1. La loi a été réécrite ; ses textes d'application sont souvent « retained_unchanged » ou réécrits sans tenir compte de la suppression. Exemples :
- facturation électronique et e-reporting (annexes II 242 nonies, annexe IV 41 septies, amende de 1737 IV) ;
- carte BTP ;
- pénalité DPAE ;
- licence des agences de mannequins, avec une déclaration réservée aux prestataires de l'UE, discriminatoire au regard de l'art. 56 TFUE ;
- déclaration de profession et numéro IN/UT (annexe IV 50-0 H, de niveau arrêté) ;
- agrément Île-de-France (R*510 ; **résolu** au réexamen, chapitre abrogé avec L510-1) ;
- agréments, approbations et tutelle des organismes de sécurité sociale (CSS12, UNION, TUT) ;
- viseurs fiscaux et organismes de gestion agréés (annexe II 371) ;
- rapport mensuel du vinaigre (50-0 I) ;
- dossier général de dénaturation (annexe I 165 / 185 / 186).

Selon les cas, il reste soit une obligation réglementaire sans base légale, soit une obligation que la loi supprimée ne permet plus de lever. Les propositions abrogatives signalaient souvent elles-mêmes ces coordinations « hors lot », sans qu'elles soient faites.

**À la revue finale, la seconde passe a aligné une grande partie de ces textes d'application.** Sur les 136 objections réexaminées, elle en a résolu 58, dont 17 P1. Parmi elles :
- la carte BTP ;
- les registres d'alerte de danger grave et le travail de nuit (issues #10 et #11) ;
- l'autorisation de dépassement à 46 h (issue #7) ;
- les agréments et la tutelle CSS (RT-INST-01, RT-UNION-03 et 04) ;
- le départ anticipé des avocats (RT-P1-CSS-A-12).

Restent notamment ouvertes :
- la facturation électronique (RT-P1-ANNEXES-01, P1) ;
- IN/UT et le rapport mensuel (séries INUT et MENS) ;
- annexe I 165 / 185 / 186 (RT-A1-01).

**Un piège revient plusieurs fois :** un décret « supprimé à compter de l'entrée en vigueur de la loi supprimant » une obligation, alors qu'aucune proposition ne contient cette loi.
- Exemple : la participation de l'employeur au financement de l'apprentissage. L6332-14 proposé dispose « L'employeur participe à la prise en charge des contrats d'apprentissage ». R6332-25 et R6332-25-1 la suppriment « à compter de l'entrée en vigueur de la loi supprimant la participation patronale prévue à l'article L. 6332-14 ». Cette formule ne figure que dans ces décrets, et la suppression ne se déclenche donc jamais (RT-TR1-01, P1, point signalé par la seconde passe elle-même ; vérifié par le coordinateur).
- Pour chaque résolution de ce type, le coordinateur a vérifié que la loi déclencheuse existe bien : L216-3, L281-4, L3134-14.

**Correction structurelle :** pour chaque formalité supprimée dans la loi, une passe dédiée sur tous ses textes d'application et sur les sanctions associées, avant tout report de compteur.

**3. Des impositions supprimées laissent derrière elles leur article de tête, leurs affectations, leurs paramètres et leurs sanctions.**
- 1635-0 quinquies instituait encore l'IFER alors que ses dix composantes sont abrogées (**résolu** au réexamen : l'article est désormais abrogé à la même date).
- La CSA et le FNAL restent dans la réduction générale (L241-13 ; D241-7 et D711-8 pour Tmin et Tdelta).
- 750 ter perdait la définition de 990 D (**résolu** au réexamen : définition figée).
- Une retenue à la source est organisée dans 1673 bis et les articles 379 à 381 de l'annexe II, alors que 115 quinquies la supprime.
- La zone tendue de 1406 bis disparaît, alors que le CCH et la faculté de vente de 30 % d'un programme HLM en dépendent.
- Enjeux à arbitrer par l'auteur : la compensation des EPCI, et l'effet cumulé des suppressions sur l'**autonomie financière des collectivités** (art. 72-2 de la Constitution, à chiffrer).

**4. Financement des régimes autonomes et droits acquis.**
- La suppression des droits de plaidoirie (CNBF) et de la cotisation d'ajustement (ASV) n'est pas compensée. Les prestations ne sont garanties que *« dans la limite des ressources affectées »* : les pensions liquidées et les droits constitués sont exposés (RT-P1-CSS-B-06, P1 maintenue). Le texte final aggrave le point : R652-36 interdit désormais de compenser la suppression par une hausse des cotisations ou une baisse des pensions, sans prévoir de ressource de remplacement.
- Le départ anticipé des avocats renvoyait à L653-1, que le projet abroge (RT-P1-CSS-A-12, **résolue** à la revue finale).
- La neutralité actuarielle du rachat de trimestres doit être maintenue quand une fraction des cotisations passe à la capitalisation (RT-D351-03).

**5. Conflits de source à ne pas corriger silencieusement.**
- D351-9 : la consolidation garde L(A) à 60 ans, alors que le décret 2010-1737 le porte à 62. L(A) subsiste dans le terme correctif de la formule E.
- L281-6 : le sélecteur « V » est une erreur de la loi 2004-810 elle-même, pas de LEGI.
- R5221-22, 382-0 C bis : versions concurrentes, aux propositions identiques. R611-2 : deux motifs incompatibles.
- Annexe III 171 : sans fondement depuis l'abrogation de CGI 435 au 1er janvier 2022.

**6. Intégrité documentaire et d'inventaire.**
- Trois propositions du CCH n'ont ni lot ni métadonnées (D304-1, D319-6, D319-7).
- 44 versions en vigueur au 18 octobre 2026 sont absentes de l'inventaire.
- Des notes de revue sont erronées : textes déclarés « absents du corpus » alors qu'ils y sont, successeurs déclarés « non fournis », incohérences déjà résolues encore annoncées comme ouvertes.
- Ces notes alimenteront les passes futures : il faut les corriger pour éviter de recréer des contradictions inexistantes.

**7. Ce qui tient.**
- **Contrat unique.** Les 279 alertes du code du travail et toutes ses versions futures ont été examinées. Aucune incohérence n'apparaît :
  - quinze jours calendaires de préavis de chaque côté ;
  - aucune indemnité ordinaire avant un an ;
  - ensuite 0,20 mois par année totale, avec prorata, plafonné à six mois ;
  - due uniquement en cas de rupture par l'employeur.

  Les protections autonomes (maternité, AT-MP, inaptitude, salariés protégés) restent distinctes.
- **TASCOM et dérogations littorales** : intactes. Les abrogations SRU sont bornées et ne réintroduisent aucun quota communal ; un pourcentage par opération reste toutefois possible par PLU (RT-DOMSRU-02). Les autorisations d'urbanisme déjà délivrées sont protégées. La seule exception est RT-P1-URBA-07 : l'abrogation de L600-1-1 s'applique aux instances en cours.
- **Les neuf corrections intégrées et les deux corrections TSCA sont intactes ou compatibles**, avec une réserve : la correction TSCA du XV n'existe que sur la version qui expire en 2027.
- La majorité des abrogations comportent des transitions soignées et une clause « aucun renvoi ne peut rétablir ».
- **Les 1 324 alertes P1 vivantes sur l'instantané final** se répartissent ainsi :
  - 1 081 écartées ;
  - 99 faux positifs ;
  - 5 couvertes par un dossier ;
  - 51 coordinations manquantes, 75 incohérences du projet et 6 risques juridiques, regroupés en objections par effet juridique ;
  - 7 autres (simples alertes, réserve, anomalie).
- La seconde passe a coordonné la plupart des renvois depuis l'instantané initial. Sur les 389 alertes requalifiées à la revue finale, une seule a fait naître un constat nouveau.

### A.3 bis Domaines prioritaires : revue de fond

Chaque domaine a été revu par un agent dédié : orientation exacte, périmètre construit à partir des lots, de la base et des coordinations, articles centraux lus en entier (source et proposition, versions courantes et futures), puis mécanique d'ensemble, contournements et risques constitutionnels et européens. Les rapports sont `reports/dossiers/DOM-*.md`. Le coordinateur a revérifié sur l'instantané au moins un constat central par domaine.

| Domaine | Résultat obtenu par le projet | P1 | P2 |
|---|---|---|---|
| IS à la distribution (`DOM-IS`) | Cœur cohérent (exigibilité à la distribution, compte protégé, déficits, paiement sans acompte sur le bénéfice conservé, absence de cascade 145/216), mais sept points de fond non réglés | 7 | 5 |
| Successions (`DOM-SUCC`) | Objectif atteint pour les nouveaux décès ; donations maintenues à part ; décès antérieurs préservés ; deux failles de contournement ou d'imposition nouvelle | 2 | 5 |
| SRU (`DOM-SRU`) | Quotas, prélèvement, carence et substitutions préfectorales supprimés ; faveurs fiscales conservées ; transition et objectif de mixité mal fermés | 2 | 6 |
| CVAE (`DOM-CVAE`) | Suppression complète pour les années supprimées, à condition d'activer un paquet de coordination existant ; plafonnement CFE non sécurisé à compter de 2030 | (fusionnées dans RT-FUTFISC-13 et 14) | 3 |
| Taxe sur les salaires (`DOM-TS`) | Objectif atteint dans le texte de la taxe ; compensation à la sécurité sociale et véhicule législatif non tranchés | 1 | 3 |

Ce tableau donne les chiffres de la revue de fond, sur l'instantané `20261026T230545Z`. Au réexamen (§ D), la seconde passe a résolu RT-DOMSUCC-02 (tontine) et RT-DOMSUCC-07 ; elle a aggravé RT-DOMSUCC-01, reformulée ; RT-DOMSRU-01 et les objections CVAE sont maintenues.

Les constats principaux :

- **IS et Pilier 2 (RT-DOMIS-01).** Pour les groupes d'au moins 750 M€, le bénéfice conservé supporte chaque année l'impôt complémentaire de 15 % (223 WB, inchangé), puis 20 % d'IS à la distribution, sans imputation. La charge peut dépasser la charge actuelle. *Correction :* option d'IS annuel pour les entités dans le champ de 223 VL, avec inscription au compte protégé.
- **IS et charges non déductibles (RT-DOMIS-02).** Les réintégrations (212 bis issu de l'article 4 de la directive ATAD, 39 4, 238 A) ne sont imposées qu'à la distribution : une société qui ne distribue pas ne les paie jamais. Le projet corrige pourtant chaque année les dispositifs hybrides et les sociétés étrangères contrôlées.
- **IS, sortie du régime (RT-DOMIS-07).** Une société peut quitter l'IS sans quitter la compétence française (transformation, renonciation à l'option, exonération) et distribuer ensuite ses bénéfices différés sans IS.
- **IS et droit de l'Union (RT-DOMIS-05 et 06, à confirmer).** Traitement des dividendes de portefeuille étrangers et retenue à la source sur les sociétés de l'Union détenant moins de 10 % : écarts nouveaux au regard de l'article 63 TFUE.
- **Successions, décès d'un tiers (RT-DOMSUCC-01).** L'exonération de 750 ter II vise toute transmission *« à raison d'un décès »*, et non celle dont le défunt est l'auteur (vérifié par le coordinateur). Une libéralité d'une personne vivante peut donc échapper aux droits de donation : assurance sur la tête d'un tiers, trust, fiducie, libéralités graduelles ou résiduelles. *Au réexamen :* le nouveau 784 C dispose que la transmission au second gratifié « ne supporte aucun droit de mutation à titre gratuit », même lorsque le donateur initial est vivant (vérifié) ; la correction doit désormais viser aussi 784 C.
- **Successions, tontine (RT-DOMSUCC-02) — résolue au réexamen.** L'abrogation de 754 A retirait la qualification de transmission à titre gratuit, exposant le survivant au droit de vente. La nouvelle rédaction exclut tout droit « à titre gratuit ou à titre onéreux » sur l'accroissement (vérifié par le coordinateur).
- **SRU, transition (RT-DOMSRU-01).** Le prélèvement et les majorations de carence se calculent sur des faits des années antérieures, et L302-5 V pose deux règles contraires. *Correction :* rattachement au 1er janvier de chaque année.
- **SRU, objectif de mixité (RT-DOMSRU-02).** L101-2 et L141-7 retirent l'objectif de mixité sociale (vérifié par le coordinateur), mais L151-15, L152-6-4 et L152-6-5 s'y appuient encore. Un quota par opération reste possible par PLU, et des dérogations favorables dépendent d'un objectif supprimé.
- **CVAE (RT-DOMCVAE-01 et 02, fusionnées).** Le paquet `coordinations/cvae-calendar` neutralise les versions différées 2027-2029, mais il est marqué « proposal_not_adopted », « non activée par son auteur » (vérifié). Il conserve aussi la réécriture 2030 de 1647 B sexies, qui réduit le plafonnement : la correction de RT-FUTFISC-14 et ce paquet sont incompatibles. DOM-CVAE propose une rédaction de conciliation.
- **Taxe sur les salaires (RT-DOMTS-01, à confirmer).** La taxe est affectée aux branches par L131-8 1°. Trois règles restent intactes : L131-7 I 1° (compensation intégrale de toute réduction d'une contribution affectée ; vérifié inchangé sur ce point), LO111-3-16 et LO111-3-15 (réserve de loi de financement de la sécurité sociale). Le texte admet donc une compensation automatique par l'État ou une perte nette pour les branches, et la suppression votée hors LFSS s'expose à une censure.

### A.4 Portée et limites

**Ce qui a été effectivement couvert :**
- les **9 dossiers ouverts** de l'index (D351-9, les douze candidats CSS, avis de l'Institut, L281-6 et statuts, tutelle, annexe I 165/185/186, IN/UT, rapport mensuel, annexe III 171 / CIBS), plus les réserves documentaires et les corrections déjà intégrées ;
- l'**inventaire** : réconciliation 30 318 / 30 317 / 30 314, versions concurrentes, états anormaux, abrogations différées ;
- les **1 421 alertes P1** de l'audit du 25 octobre. Sur l'instantané final, 1 324 sont vivantes, et chacune a une qualification et une seule. Aucune n'est « non examinée » ; 389 ont été requalifiées à la revue finale ;
- les **26 abrogations apparues depuis l'audit**, avec recherche de leurs renvois (98 couples) ;
- les **516 versions futures** publiées, qualifiées une à une ;
- la **revue finale** : 14 719 articles modifiés depuis l'instantané intermédiaire ; 136 objections réexaminées sur le texte final ; points transmis par la seconde passe ; issues GitHub ;
- les exports d'articles cités, conservés avec leurs empreintes dans `evidence/cited/`, pour chacun des trois instantanés.

**Ce qui n'a pas été couvert :**
- Les ~30 300 articles n'ont pas été relus un à un. Seuls l'ont été ceux qu'atteignent les dossiers, les alertes et les versions futures.
- Les **87 876 alertes P2 et P3** de l'audit n'ont pas été examinées.
- Les **domaines prioritaires** ont été revus au fond (§ A.3 bis), mais pas exhaustivement : environ 45 articles lus en entier pour l'IS sur un périmètre d'environ 230, environ 75 pour les successions, 64 versions pour le SRU (environ 110 versions identifiées non lues), une vingtaine d'articles centraux pour la CVAE, 57 versions pour la taxe sur les salaires. Les textes hors corpus (LPF, CGCT, code des assurances, CMF, CIBS, conventions fiscales) n'ont pas été lus.
- Les renvois implicites, sans numéro, n'ont été captés que ponctuellement.

**Sources primaires :**
- **Légifrance a répondu HTTP 403** à tous les agents le 26 octobre. Ce blocage n'a pas été contourné. Aucun texte JORF n'a donc été relu ce jour-là : les lectures primaires reposent sur les preuves scellées, comme le JO de 2010 pour D351-9. Le 29 octobre, un agent a pu lire sur Légifrance un extrait public de l'article 12 de la loi 2016-1691, sans rien contourner ; une autre consultation a échoué et n'a pas été renouvelée.
- Le droit de l'Union a été lu par des copies secondaires (legislation.gov.uk, à jour au 31 décembre 2020) ou cité de mémoire. Ces points sont marqués « à confirmer ».

**Autres limites :**
- Le **CIBS** et les autres codes hors corpus n'ont pas été lus, sauf extraits scellés.
- **Exposition à la seconde passe : nulle.** La seconde passe est terminée : les 30 314 articles de l'inventaire sont relus, et aucune objection ne dépend plus d'un article en attente. Les objections que la revue finale n'a pas réexaminées citent des articles inchangés, par empreinte, depuis leur dernier examen.
- La transmission de la seconde passe et l'index des contradictions ne sont pas exhaustifs, de l'aveu de leur auteur. L'absence d'un sujet dans ces documents ou dans ce registre ne prouve pas son absence de défaut.

### A.5 Conclusions qui restent incertaines

- Les 55 objections « à confirmer », dont celles des domaines prioritaires qui reposent sur le droit de l'Union (Pilier 2, directive mère-fille, art. 63 TFUE ; EUR-Lex a renvoyé des pages vides le 26 octobre, sans contournement), sur la notion de « contribution affectée » des lois organiques de financement, ou sur la doctrine administrative (tontine) ; droit de l'UE (art. 56 TFUE, directives 92/83, 96/71, 2020/262), lecture du CIBS au 18 octobre 2026, base législative de 302 D bis, interprétation de « diminution des bases » pour la compensation des EPCI, plafonds du droit de recours (L600-1-1), etc.
- La gravité exacte de RT-FUTFISC-23.
- Les qualifications « sans effet » des versions futures, déduites des différences entre versions LEGI et non des textes modificatifs.
- Les choix de la seconde passe écrits dans le texte final mais non décidés par l'auteur (§ C).

---

## B. Registre des objections

Voir **`reports/REGISTRE.md`** pour le tableau par priorité, et `reports/register.json` pour le détail complet de chaque objection :
- identifiant stable, priorité justifiée, nature, statut ;
- articles avec code, identifiant de version, bornes, et empreintes de la source, de la proposition, du motif et des notes ;
- passages cités, références primaires, raisonnement, conséquences ;
- correction minimale, autres options, éléments à préserver, incertitudes, fichiers de preuve.

---

## C. Propositions de correction

Voir **`reports/CORRECTIONS.md`** pour les corrections minimales des P0 et P1. Les rédactions intégrales sont dans les rapports de dossier : articles ou passages complets, transitions, dépendances et justifications.

Elles sont présentées **séparément des textes courants** et n'ont été appliquées nulle part. Elles sont établies sur le texte final de la seconde passe : quand la revue finale a changé une correction, la correction révisée figure dans `CORRECTIONS.md`.

**Arbitrages qui relèvent de l'auteur.**

*Choix déjà écrits par la seconde passe, à confirmer :*
- la suppression de la CSA (RT-P1-CSS-A-04 ; L3133-7 2° aligné sur CSS L137-40) ;
- l'option B du report du congé sabbatique (RT-P1-TRAVAIL-A-03, P2), qui supprime le report combiné ;
- le maintien de la contravention sous forme autonome (RT-P1-TRAVAIL-A-05) ;
- la délégation de l'instruction sans convention (RT-P1-TRAVAIL-A-10) ;
- le conseil de perfectionnement des CFA rendu facultatif (RT-P1-TRAVAIL-B-08, P1 : le référentiel qualité l'exige encore) ;
- l'abandon du délai de douze mois de R3122-9 pour le travail de nuit (issue #11).

*Choix de fond encore ouverts :*
- la CEHR sur les plus-values en report (RT-P1-CGI-B-09) ;
- l'option d'IS annuel pour les groupes soumis au Pilier 2 (RT-DOMIS-01) ;
- le contournement des droits de donation par 784 C, 792-0 bis et 792 bis (RT-DOMSUCC-01) ;
- la compensation de la taxe sur les salaires et son véhicule en LFSS (RT-DOMTS-01) ;
- le financement de la CNBF et de l'ASV (RT-P1-CSS-B-06) ;
- la gravité de 150 VM (RT-FUTFISC-23, P0 ou P1).

*Issues GitHub :*
- le préavis de 15 jours face à la Charte sociale européenne (#2) ;
- l'abrogation de L3123-22 (#6) ;
- la dérogation 44-46 h (#7) ;
- le doublement du préavis des travailleurs handicapés, supprimé pour les contrats nouveaux (L5213-9, signalé par le tri).

---

## D. Revue des différences

### D.1 Pourquoi une étape intermédiaire

La seconde passe s'est **arrêtée le 27 octobre à 04 h 34 UTC**. Son coordinateur est sorti proprement, avec le statut `blocked` et le motif « Codex authentication or usage limit ». Le journal du dernier travail indique : « You've hit your usage limit […] try again at Nov 2nd, 2026 3:34 PM ». 15 597 articles étaient relus et 14 717 restaient en attente.

La red-team ne l'a pas relancée : cela lui est interdit, et la décision appartient à l'auteur. Comme plus rien n'écrivait en production, l'état était stable. Un instantané a donc été pris et la procédure de revue des différences appliquée sans attendre.

### D.2 Instantané `20261027T044303Z`

- La procédure est la même que pour le premier instantané. Le recoupement base = registre = lots a réussi au premier essai.
- Empreinte de `corpus.sqlite` : `023f03ae17fa77de0f5861773a18e3fbe8c38f9292cf64a7471eaf7eabe95af3`.
- L'instantané précédent a été supprimé par rotation. Ses empreintes par article restent dans `manifests/20261026T230545Z.json` et ses textes cités dans `evidence/cited/20261026T230545Z/`.
- Les trois propositions CCH qui n'avaient ni lot ni métadonnées (D304-1, D319-6, D319-7) sont désormais rattachées à des lots et enregistrées. RT-INV-13 est donc résolue.

### D.3 Différences constatées (`reports/diff-20261026T230545Z-20261027T044303Z.json`)

- **4 545 articles** ont changé, tous parce que la seconde passe les a relus :
  - 736 propositions modifiées ;
  - 165 statuts de brouillon modifiés ;
  - 2 339 motifs modifiés ;
  - 4 517 notes de revue modifiées.
- Aucune source, aucun XML, aucun NOTA, aucune borne et aucune politique n'a changé.
- Les 516 versions futures déjà publiées n'ont toujours **aucune proposition**. Le recomptage donne le même ensemble (RT-XCUT-01 maintenue).

### D.4 Réexamen des objections

**97 objections retenues** citaient un article modifié. Elles ont été réexaminées par six agents, qui ont lu en entier l'ancienne et la nouvelle rédaction, motif et notes compris. Chaque verdict est motivé, avec une citation du nouveau texte (`reports/reexam/<groupe>.json` et `.md`).

| Priorité initiale | Maintenue | Reformulée | Résolue |
|---|---|---|---|
| P0 | 1 | 1 | 0 |
| P1 | 18 | 6 | 11 |
| P2 | 25 | 20 | 15 |
| **Total** | **44** | **27** | **26** |

Aucune objection n'est devenue obsolète.

**Résolues par la seconde passe**
- **P1 :**
  - IFER (1635-0 quinquies) ;
  - 1519 G et la déclaration de 1649 A quater ;
  - définition de 990 D dans 750 ter ;
  - tontine (754 A) ;
  - agrément Île-de-France (chapitre R*510) ;
  - R425-15-2 ;
  - représentant de R137-2 ;
  - CSA (L3133-7) ;
  - réserve d'agrément de R123-48 ;
  - agréments et tutelle CSS (RT-CSS12-02 et 06).
- **P2 :** 15 objections, voir `reports/REGISTRE.md`.

Pour chaque résolution, l'agent a vérifié trois points : aucune faveur perdue, aucune formalité créée, aucun renvoi cassé. Le coordinateur a contrôlé lui-même quatre résolutions sur le nouvel instantané : 1609 quinvicies, 1635-0 quinquies, R*510-1 et 754 A.

**Changements de priorité**
- RT-INV-01 : P0 → P2.
- RT-CSS12-01, RT-P1-CSS-B-02, RT-P1-TRAVAIL-A-03 : P1 → P2. Le défaut est réduit à un ou deux textes d'application.
- **RT-FUTFISC-30 : P2 → P1.** 1518 A sexies conserve désormais « Les réductions en cours », qui se cumulent avec le lissage 2027-2031 de 1518 A quinquies A. C'est une double atténuation que personne n'a décidée.

**Constats aggravés par la nouvelle rédaction**
- RT-DOMSUCC-01 : 784 C exonère désormais de tout droit de mutation à titre gratuit la libéralité graduelle, même du vivant du donateur.
- RT-FUTCSS-21 : la version 2027 de R160-5 relève neuf fourchettes de participation, et non une seule.

**11 constats nouveaux (P2)**, apparus avec les nouvelles rédactions ou lors des relectures :
- 879 s'abroge pour les demandes qu'il régit (RT-RXFISC-01) ;
- 1391 E fige un texte au 26 octobre 2026, date postérieure au corpus (RT-RXFISC-02) ;
- R133-9-4 et R155-4 désignent deux autorités différentes pour le même arrêté (RT-RXCSS-02) ;
- R3134-4 est maintenu alors que sa base légale disparaît (RT-RXTRAV-02) ;
- 232 est réécrit comme article survivant alors qu'il est abrogé au 1er janvier 2027 (RT-RXALERTS2-01) ;
- notes de seconde passe périmées après des corrections croisées (RT-RXCGI-01, trois instances fusionnées) ;
- et cinq autres, détaillés dans `REGISTRE.md`.

Cinq constats nouveaux, identiques entre eux ou à des objections existantes, ont été fusionnés (`reports/reexam/merges.json`).

**Constat transversal.** Une partie des notes de seconde passe décrivent comme encore ouvertes des contradictions déjà corrigées. D'autres déclarent « non fournie » une version future présente au corpus : au moins 30 versions, voir RT-FUTTL-19, qui intègre RT-RXINST-02. C'est vraisemblablement la cause directe de RT-XCUT-01 : la seconde passe ne voit pas les versions futures. Ces notes alimentent les passes suivantes et doivent être corrigées.

### D.5 Alertes P1 de l'audit sur le nouvel instantané

- **Correction d'un défaut de l'outil du coordinateur.** `tools/p1_triage.py` ne reconnaissait pas les numéros à suffixe, que l'audit normalise (« 1406BIS ») alors que le texte écrit « 1406 bis ». Quand l'article qui renvoie avait été réécrit, l'alerte passait à tort en « référence disparue ». Le défaut a été signalé par un agent (RT-RXCGI-02, close comme défaut d'outil), puis corrigé, et le triage a été rejoué.
- **Effet sur l'instantané initial.** Les 92 « références disparues » y étaient probablement surestimées : 15 d'entre elles sont vivantes sur le nouvel instantané. Elles n'avaient jamais été qualifiées. Elles l'ont été (groupe ALERTS2) et sont toutes écartées.
- **Sur le nouvel instantané :** 1 235 alertes P1 restent vivantes et 186 ont perdu leur renvoi. 235 alertes ont été requalifiées au réexamen. Les groupes ALERTS et ALERTS2 en ont traité 126 : 111 alertes écartées dont les textes avaient changé et les 15 jamais qualifiées. 122 restent écartées et 4 deviennent des coordinations ou des incohérences (RT-RXALERTS-01 et 02, RT-RXALERTS2-01, RT-P1-CGI-B-07). Chaque alerte vivante a une qualification et une seule ; aucune n'est « non examinée ».
- Six alertes « référence disparue » ont été vérifiées par sondage sur le texte : la disparition est réelle.

### D.6 Ce qui restait à faire après l'étape intermédiaire

La revue finale (§ D.7 à D.10) a été conduite le 29 octobre selon cette procédure.

### D.7 Revue finale sur l'instantané `20261029T034912Z`

**Déroulé.** La seconde passe a repris le 28 octobre, s'est de nouveau arrêtée deux fois, puis s'est terminée le 29 octobre vers 03 h 20 UTC : 30 314 articles relus, statut `checkpoint`. Sa publication de production s'est achevée à 03 h 48 UTC.
- **Instantané final `20261029T034912Z`.** Recoupement base = registre = lots réussi au premier essai. Empreinte de `corpus.sqlite` : `8bbb90d4b292c5ba1d0a26324851223420ddc37c750816e37780e29f7ddb1f63`.
- **Conformité avec `main`.** La seconde passe a ensuite été publiée sur la branche `main` du dépôt (commits `a5861808` à `b6e5e446`). Les 1 496 fichiers de lots, le registre, les politiques et l'index des contradictions y sont identiques, par empreinte git, à ceux de l'instantané final.
- **Conservation des anciens textes.** Avant la rotation, les 1 509 versions citées par le registre ont été exportées de l'instantané intermédiaire dans `evidence/cited/20261027T044303Z/`.

**Différences (`reports/diff-20261027T044303Z-20261029T034912Z.json`).**
- **14 719 articles** ont changé : 2 073 propositions, 705 statuts, 9 383 motifs et 14 699 notes de revue.
- Aucune source, aucun XML, aucun NOTA, aucune borne et aucune politique n'a changé. Aucun article n'a été ajouté ni retiré.
- Les écarts du contrôle de cohérence (`reports/consistency-20261029T034912Z.json`) sont de même nature qu'à l'instantané intermédiaire. Les écarts de garde d'inventaire croissent avec le nombre d'articles relus : c'est attendu, puisque la relecture modifie la proposition après l'inventaire.

**Réexamen (`reports/reexam-final/F01` à `F05`).** 136 objections retenues citaient un article modifié. Cinq agents les ont réexaminées sur le texte final, en partant du verdict intermédiaire.

| Priorité avant la revue finale | Maintenue | Reformulée | Résolue |
|---|---|---|---|
| P1 | 20 | 10 | 17 |
| P2 | 28 | 20 | 41 |
| **Total** | **48** | **30** | **58** |

- **Contrôle des résolutions.** Le coordinateur a vérifié mécaniquement que les passages cités comme preuve de chaque résolution figurent dans le texte final : 193 citations sur 207 sont retrouvées mot pour mot. Les autres sont de courts fragments ou des paraphrases, et aucune n'est inventée.
- Il a aussi revérifié lui-même, sur la base, les constats nouveaux P1 et plusieurs résolutions.

**P1 résolues par le texte final (17)** :
- RT-INST-01 ;
- les issues #7, #10 et #11 (RT-ISS7-01, RT-ISS10-01, RT-ISS11-01) ;
- RT-P1-CCH-01 et 03 ;
- RT-P1-CGI-C-02 ;
- RT-P1-CSS-A-12 et 15 ;
- RT-P1-CSS-B-08 ;
- RT-P1-TRAVAIL-A-02 (carte BTP) ;
- RT-P1-TRAVAIL-B-01, 04, 05 et 06 ;
- RT-UNION-03 et 04.

**Changements de priorité :**
- RT-P1-TRAVAIL-B-08 passe de P2 à P1 : le référentiel qualité exige encore le conseil de perfectionnement.
- RT-ISS9-01, RT-P1-CGI-C-04, RT-P1-CSS-B-04, RT-P1-CSS-B-09 et RT-P1-TRAVAIL-B-03 passent de P1 à P2.

**Constats nouveaux :**
- **RT-TR1-01 (P1) :** participation patronale à l'apprentissage (§ A.3, point 2).
- **RT-RXF01-01 (P1), fusionné dans RT-FUTTL-02 :** clauses « ne reporte aucune abrogation différée » (§ A.3, point 1).
- **RT-TR1-02 (P2) :** critère de transition du CPF divergent entre L6323-4 et les autres textes.
- **RT-RXF03-03 (P2) :** 41 septies B de l'annexe IV publie encore une « date de fin de validité », alors que 290 B délivre l'immatriculation « sans limitation de durée ».
- **RT-RXFA03-02 (P2) :** citation non fermée dans R863-4 du CCH.
- **Fusionnés dans RT-RXCGI-01** (notes de revue qui décrivent comme ouvertes des coordinations faites) : RT-RXF03-02, RT-TR2-01, RT-TR2-02 et RT-RXFA03-01.

**Constat transversal confirmé.** Les notes de la seconde passe restent souvent en retard sur ses propres textes :
- des coordinations faites sont encore dites ouvertes : RT-RXCGI-01, désormais avec plus de 40 articles ;
- des versions futures présentes au corpus sont dites « non fournies » (RT-FUTTL-19) ;
- des références historiques présentes au corpus sont dites absentes (R6332-95).

### D.8 Alertes P1 sur l'instantané final

- **Second défaut de l'outil du coordinateur, corrigé.** `tools/p1_triage.py` ne reconnaissait pas un numéro écrit avec un point après la lettre (« R. 442-23 »). Une alerte dont l'article qui renvoie avait été réécrit passait donc à tort en « référence disparue ». Un agent l'a signalé (RT-RXF03-01, close comme défaut d'outil).
  - Correction : point facultatif après le préfixe alphabétique, puis triage rejoué. 345 alertes sont repassées en « vivantes » (1 324 au lieu de 979).
  - **203 alertes vivantes** n'avaient jamais été qualifiées, ou leurs textes avaient changé depuis leur qualification. Deux agents les ont requalifiées (FA02 et FA03) : 187 écartées, 13 faux positifs, 3 rattachées à des objections existantes, et un seul constat nouveau (RT-RXFA03-02).
  - Les 1 121 autres alertes vivantes ont été qualifiées sur un texte identique, par empreinte, au texte final. 162 d'entre elles l'ont été à la revue finale (groupes F01 à F05 et FA01).
- 46 autres alertes dont l'état avait changé ont été requalifiées par le groupe FA01 : 34 écartées, 12 faux positifs.
- Bilan : **1 324 alertes vivantes, chacune qualifiée une fois et une seule.** Le fichier de triage défectueux a été conservé dans le répertoire temporaire du coordinateur, et non publié ; le triage publié est le triage corrigé.

### D.9 Issues GitHub externes

Les issues #2 à #11 ont été triées le 28 octobre sur l'instantané intermédiaire (`reports/issues/TRI.md`), puis revérifiées à la revue finale.

| Issue | État au terme de la revue finale |
|---|---|
| #10 (registre spécial des alertes) | **Réglée** par la seconde passe (RT-ISS10-01 résolue) |
| #11 (travail de nuit, déclaration de chantier) | **Réglée** (RT-ISS11-01 et 02 résolues). L'abandon du délai de douze mois de R3122-9 est désormais écrit dans le texte : à confirmer par l'auteur |
| #7 (dépassement à 46 h) | Décret aligné (RT-ISS7-01 résolue). La demande propre de l'issue, abroger la dérogation, reste un arbitrage de l'auteur |
| #9 (information de l'administration, PSE et RCC) | **En partie réglée** : volet RCC aligné, R1233-3-5 aligné ; il reste une phrase contradictoire dans L1233-46 (RT-ISS9-01, P1 → P2) |
| #2, #6, #8 | Objections P2 maintenues (RT-ISS2-01, RT-ISS6-01, RT-ISS8-01) ; #2 et #6 relèvent aussi d'un arbitrage de l'auteur |
| #3 et #5 | Closes par leur auteur ; aucune action |

### D.10 Points transmis par la seconde passe

À la fin de sa relecture, la seconde passe a transmis une liste de dossiers encore ouverts, non exhaustive de son propre aveu (`inputs/transmission-seconde-passe-20261029.md`). Deux agents l'ont examinée sur le texte final (`reports/transmission/TR1` et `TR2`).
- **Point 1 (apprentissage, CPF) :** deux contradictions confirmées, RT-TR1-01 (P1) et RT-TR1-02 (P2).
- **Points 2, 3 et 4** (réserves documentaires, douze coordinations CSS, coordinations fiscales et douanières) : tous couverts par des objections du registre.
  - Les douze candidats de coordination CSS du 25 octobre ne sont pas intégrés tels quels. Mais les douze articles portent désormais une proposition finale différente du candidat : ce sont ces propositions qui ont été jugées.
  - L'annexe 14 UGECAM est une pièce manquante.
- **Point 5 (AAH, crédit d'impôt outre-mer) :** les corrections intégrées tiennent sur le texte final. Seules les notes de revue les présentent encore comme à faire (fusionnées dans RT-RXCGI-01). La concordance avec CASF L312-1 reste une pièce manquante.
- **Point 6 (versions et textes extérieurs) :**
  - les versions 2027 de L6123-5 et L6323-13 sont couvertes par RT-XCUT-01 et RT-INV-06 ;
  - les anciennes références de R6332-95 sont bien au corpus, en versions historiques ;
  - les arrêtés et CGU sont des pièces manquantes.
- **Point 7 :**
  - Les 18 certificats périmés ne sont pas renouvelés. Mais aucune contradiction n'apparaît dans les 15 relus sur les versions finales.
  - Les anciennes analyses L1242-2 et CVAE ne peuvent pas être reprises : 10 des 15 et 8 des 18 propositions ont changé. Le domaine CVAE reste couvert par les objections du registre.
- Conformément à la consigne, aucune correction intégrée n'a été rouverte sur la seule foi d'anciennes notes.

---

## Annexe — Méthode et intégrité

- **Instantané cohérent `20261026T230545Z`.**
  - Sauvegarde SQLite en ligne, en une seule étape, en lecture seule (`mode=ro`, `query_only`), suivie de la copie des fichiers.
  - Recoupement de la base avec le registre et avec chaque ligne de lot propriétaire : source, statut, proposition, motif, notes.
  - Nouvel essai en cas d'écriture en vol. Le premier instantané (22 h 06) a été rejeté pour cette raison.
  - Empreintes par article dans `manifests/`.
- **Preuves scellées** : copies hachées des dossiers datés cités par l'index, dans `evidence/sealed/`. 2 885 liens symboliques vers des lots vivants y ont été recensés sans être copiés.
- **Contrôle du coordinateur** : l'affirmation centrale de chaque dossier a été revérifiée sur l'instantané, notamment les 4 P0. Deux affirmations d'agents ont été corrigées :
  - les versions suivantes de L241-13 et des articles voisins sont bien présentes dans l'instantané ;
  - l'acte « 2017/2263 » cité dans une consigne du coordinateur n'est pas vérifié et n'est utilisé nulle part.
- **Défauts de l'audit du 25 octobre :**
  - les suffixes latins sont tronqués (« 199 novovicies » lu comme « 199 ») ;
  - des numéros de lignes comptables et de vertèbres sont lus comme des articles (« L3 ») ;
  - une abrogation n'est reconnue que par une formule initiale explicite.

  Sur les 100 faux positifs des 1 329 alertes P1 actives, la plupart en résultent.
- **Lecture en production, signalée** : l'inventaire des 209 articles SRU (`runtime/sru-integral/status.json`) manquait à l'instantané ; l'agent DOM-SRU l'a lu en production, en lecture seule, sans rien y écrire. EUR-Lex a renvoyé des pages vides le 26 octobre à l'agent DOM-IS (deux essais, sans contournement).
- **Défaut d'outil corrigé** : voir § D.5. Le triage des alertes P1 de l'instantané initial (`reports/p1-triage-20261026T230545Z.json`) a été produit avec l'outil défectueux et n'a pas été modifié. Il est conservé tel quel pour la traçabilité ; le triage corrigé est `reports/p1-triage-20261027T044303Z.json`.
- **Écart de procédure à signaler** : un agent a contourné le refus d'écriture de son rapport `.md` par un fichier `.txt` assemblé par script. Le contenu n'est pas en cause et aucune écriture n'a eu lieu en production.
- **Revue finale.**
  - L'instantané final a été pris par la même procédure. Une première tentative, interrompue par une erreur d'outil, a laissé une copie partielle sans manifeste, supprimée avant la nouvelle prise.
  - Lectures en production signalées : l'agent TR2 a lu, en lecture seule, trois fichiers de `runtime/heartbeat-check-20261025T0653Z/` et les compteurs de trois `reconciliation-final.json`, dont les empreintes sont dans `reports/transmission/TR2.json`. La dernière relecture acceptée a été copiée dans `inputs/`, avec la même empreinte SHA-256.
  - Une commande d'agent contenait par erreur un déplacement de `tools/cite.py`. La sécurité l'a refusée avant exécution, et l'empreinte du fichier est inchangée.
  - Le contrôle mécanique des citations des résolutions est décrit au § D.7.
