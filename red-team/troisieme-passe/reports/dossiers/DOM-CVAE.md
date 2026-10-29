# DOM-CVAE — Revue de fond : suppression de la CVAE et de sa taxe additionnelle CCI

**Avertissement.** Cette revue a été faite par une IA. Elle ne vaut pas validation par un juriste. Elle porte sur l'instantané `20261026T230545Z`, dont la date de référence est le 18 octobre 2026. Les articles du noyau CGI sont encore `pending` en seconde passe : les conclusions sont donc provisoires. Lecture seule : aucun script de production n'a été lancé, aucun fichier de l'instantané ni d'un autre agent n'a été modifié.

Livrables : `reports/dossiers/DOM-CVAE.md` (le présent rapport) et `reports/dossiers/DOM-CVAE.json` (6 objections, RT-DOMCVAE-01 à 06).

## 1. Orientation et résultat obtenu

### Orientation (citations exactes)

- `policy-coordinations.json`, `fiscalite` : « CVAE : appliquer cvae_removal en entier. Suppression prospective de la taxe et de sa taxe additionnelleCCI, sans retrait des exonérations/plafonnements CFE ni réintroduction par renvoi, déclaration ou calendrier futur. »
- `cvae_removal[0]` : « Supprimer la CVAE et sa taxe additionnelle CCI pour les années d'imposition commençant le 1er janvier de l'année suivant celle de l'entrée en vigueur de la loi proposée. […] aucun IS ni CFE de remplacement. »
- `cvae_removal[2]` : « Conserver les définitions autonomes de valeur ajoutée et de période de référence de 1586 sexies et quinquies, nécessaires au plafonnement favorable de CFE, ainsi que le mécanisme de 1647 B sexies. Les baisses programmées restent : 1,531 % en 2026 et 2027 ; 1,438 % en 2028 ; 1,344 % en 2029 ; 1,25 % en 2030 et après. »
- `cvae_removal[4]` : « Aucune CVAE fictive à déduire ni double avantage inventé. »
- `cvae_removal[6]` : « Calendriers législatifs 2027–2030 : retirer les substitutions futures qui réintroduiraient un barème ou une CVAE […]. Les coordinations hors corpus sont rédigées dans un paquet séparé ; ne pas les déclarer achevées à partir du seul noyau. »
- `site-summaries.json` : « Supprimer la CVAE et sa taxe additionnelle CCI dès l'année suivant l'entrée en vigueur de la loi. Conserver les exonérations et le plafonnement favorable de CFE, avec ses baisses programmées. »

En résumé : la CVAE et la TA-CVAE sont supprimées pour les années postérieures à l'entrée en vigueur de la loi. Les années anciennes gardent leur droit. Les avantages CFE (plafonnement, taux décroissants, avantages de 1600) sont conservés. Aucune taxe de remplacement, aucune compensation inventée, aucune réintroduction par calendrier, renvoi ou déclaration.

### Résultat obtenu

- **Noyau codifié** (lot `batches/cvae-removal/001.json`, 29 propositions, plus 1681 septies et 1649 quater B quater dans le lot `successions/204`) :
  - Pour les années supprimées, le noyau atteint l'objectif : il supprime l'assujettissement, le barème, les acomptes, le solde, la déclaration 1330-CVAE, les effectifs, le télérèglement, les amendes, les annexes de l'annexe III et la TA-CVAE.
  - Il préserve expressément les années anciennes : dettes, dégrèvements, restitutions, recours, solde du dernier exercice.
  - Il conserve le plafonnement CFE sur une définition de valeur ajoutée qui fonctionne : 1586 sexies réécrit en définition autonome, 1586 quinquies en période autonome, et les taux de 1647 B sexies.
  - Il conserve aussi les douze exonérations, la demi-base et le taux de 1,12 % de 1600. Il ne crée aucune taxe de remplacement.
- **Calendrier** :
  - Seul, le noyau ne neutralise pas les rédactions différées de 2027 à 2030.
  - Un paquet compagnon (`coordinations/cvae-calendar`) le fait de façon substantiellement complète : il réécrit LF 2023 art. 55 (XXVIII), LF 2024 art. 79 (V) et LF 2025 art. 62 (VII).
  - Mais ce paquet porte le statut « proposal_not_adopted » et n'est « pas activé par son auteur ». Il est ignoré par l'objection RT-FUTFISC-13, qui propose une autre disposition transitoire (RT-DOMCVAE-01).
- **2030 et après** : le paquet laisse s'appliquer la réécriture 2030 de 1647 B sexies. La cotisation plafonnée perd alors 1599 quater D et 1609 İ, et deux régimes de période se chevauchent. Le paquet contredit aussi la correction de RT-FUTFISC-14 (RT-DOMCVAE-02).
- **Conclusion** :
  - L'objectif est atteint pour les années supprimées antérieures à 2030, à condition d'activer le paquet cvae-calendar comme véhicule unique.
  - Il n'est pas pleinement atteint à partir de 2030 pour le plafonnement CFE : perte probable d'un élément favorable et texte applicable incertain.
  - Je n'ai trouvé aucun trou d'imposition, aucune double imposition, aucune réintroduction par déclaration et aucune perte de droits sur les années anciennes.

## 2. Périmètre (articles du domaine, statut de seconde passe)

Construit à partir de l'orientation, du lot propriétaire, d'une recherche (expression régulière `1586 ter…nonies | valeur ajoutée des entreprises | CVAE`) dans `articles.content_xml` et `drafts.proposed_xml` (versions en vigueur au 18 octobre 2026 ou futures : 60 couples) et des versions futures du paquet.

| Code | Article | Version (début → fin) | Statut d'inventaire | Lot / statut |
|---|---|---|---|---|
| cgi | 1447-0 | LEGIARTI000021640942 (2010 → 2030) | pending | cvae-removal / rewrite_draft |
| cgi | 1586 ter | LEGIARTI000048847020 (2024 → 2027) | pending | cvae-removal / rewrite_draft |
| cgi | 1586 ter | LEGIARTI000053188762 (2027 → 2030) | not_in_inventory | — (version future) |
| cgi | 1586 quater | LEGIARTI000048860944 (2026 → 2028) | pending | cvae-removal |
| cgi | 1586 quater | LEGIARTI000051242682 (2028), LEGIARTI000051249022 (2029 → 2999) | not_in_inventory | — |
| cgi | 1586 quinquies | LEGIARTI000023380915 (2010 → 2030) | pending | cvae-removal |
| cgi | 1586 sexies | LEGIARTI000043048297 (2022 → 2029) | pending | cvae-removal |
| cgi | 1586 sexies | LEGIARTI000054591243 (2029 → 2030) | not_in_inventory | — |
| cgi | 1586 septies | LEGIARTI000048846991 (2024 → 2030) | pending | cvae-removal |
| cgi | 1586 octies | LEGIARTI000042909509 (2021 → 2030) | pending | cvae-removal |
| cgi | 1586 nonies | LEGIARTI000054374005 (2026 → 2030) | pending | cvae-removal |
| cgi | 1600 | LEGIARTI000053562172 (2026-03 → 2027) | pending | cvae-removal |
| cgi | 1600 | LEGIARTI000049534935 (2027), 051242816 (2028), 051249045 (2029), 051248679 (2030 →) | not_in_inventory | — |
| cgi | 1647 B sexies | LEGIARTI000048860555 (2026 → 2028) | pending | cvae-removal |
| cgi | 1647 B sexies | LEGIARTI000051248428 (2028), 051248495 (2029), 048860644 (2030 →) | not_in_inventory | — |
| cgi | 1647 B sexies A | LEGIARTI000048847068 (2030 →) | not_in_inventory | — |
| cgi | 1679 septies | LEGIARTI000042908204 (2021 → 2030) | pending | cvae-removal |
| cgi | 1679 quinquies | LEGIARTI000033812199 (2019 →) | pending | cvae-removal |
| cgi | 1681 septies | LEGIARTI000051764486 (2025 → 2030) | pending | successions/204 |
| cgi | 1649 quater B quater | LEGIARTI000051764508 (2025 → 2027) | pending | successions/204 |
| cgi | 1731 | LEGIARTI000033812315 (2019 → 2030) | pending | cvae-removal |
| cgi | 1770 decies | LEGIARTI000025092026 (2012 → 2030) | pending | cvae-removal |
| cgi | 1447 | LEGIARTI000053544997 (2026 → 2030) | pending | cfe-micro-exoneration |
| cgi | 238 bis HW | LEGIARTI000047303743 (2023 → 2030) | completed | cvae-removal |
| cgi | 39 | LEGIARTI000053542680 (2026 → 2027) | completed | (lot fiscal) |
| cgi | 1655 septies | LEGIARTI000046868436 | pending | automatic-impots/00124 |
| a2 | 317 septies E | LEGIARTI000023396197 (→ 2030) | completed | — |
| a2 | 310 HC | LEGIARTI000047814988 (2030 →) | not_in_inventory | — |
| a3 | 328 G bis à 328 G nonies D (12 articles, dont 328 G nonies B hors lot CVAE) | 2010–2024 → 2999 | completed | cvae-removal (11), automatic-impots-annexe-3/00039 (1) |
| a3 | 344-0 B, 344 I-0 bis, 406 terdecies | | completed | cvae-removal |
| a3 | 344-0 A, 344-0 C, 344 I ter, 344 quindecies, 38, 39, 40 A, 46 C, 382-0 C ter, 382-0 C sexies | | completed | lots annexe III |
| css | L137-33 | LEGIARTI000051287346 (→ 2030) | completed | securite-sociale/002 |
| css | R133-14 | LEGIARTI000054167679 | pending | simplified-employment-declarations |
| travail | D3324-3 | LEGIARTI000029729147 | pending (retained_unchanged) | faux positif : « valeur ajoutée des entreprises de banque » (participation), sans lien avec la CVAE |
| hors code | LF 2022-1726 art. 55 ; LF 2023-1322 art. 79 ; LF 2025-127 art. 62 | LEGIARTI000053547707, 051215956, 051173263 | hors inventaire | `coordinations/cvae-calendar` (proposal_not_adopted) |

Articles cités dans la consigne mais hors champ actuel : 1647 C quinquies B et 1647 E n'ont aucune version en vigueur ou future (articles abrogés). Les versions courantes de 1639 A ter, 1518 B, 1635 sexies, 1586, 1599 bis et 1647 D ne renvoient pas à la CVAE : lecture par recherche, puis contrôle de leurs passages pertinents.

## 3. Méthode

1. Lecture de l'orientation (citations ci-dessus), du manifeste `coordinations/cvae-calendar/manifest.json`, avec ses trois articles (source et proposition en entier) et ses pièces futures, et du lot `cvae-removal/001.json`.
2. Export par `tools/cite.py` (toutes versions) des articles du périmètre. Fichiers : `evidence/cited/20261026T230545Z/`. Lecture par filtrage sur les versions en vigueur au 18 octobre 2026 ou futures.
3. Recherche en lecture seule dans `corpus.sqlite` (`mode=ro`, `query_only`) des renvois à la CVAE, à 1586 ter–nonies et à la « valeur ajoutée des entreprises », dans tous les codes.
4. Confrontation avec `reports/register.json` (14 objections désignées, plus les objections voisines RT-XCUT-01, RT-FUTCSS-04 et RT-FUTFISC-27), le dossier FUT-FISC (A-redactions n° 1 et 2) et la preuve scellée `evidence/sealed/runtime/cvae-semantic-recheck-20261023T1956Z/`. Cette preuve est une ancienne conclusion, sans contradiction effective établie dans son périmètre, et n'a pas été tenue pour acquise.
5. Une recherche web datée (2026-10-26) sur le décret FNAET : source secondaire seulement.

## 4. Mécanique d'ensemble (vérification)

- **Assiette et fait générateur.**
  - La CVAE est due par le redevable qui exerce l'activité au 1er janvier (1586 octies I). Elle est assise sur la valeur ajoutée de l'année ou de l'exercice clos dans l'année (1586 quinquies).
  - Le critère temporel « années d'imposition commençant à compter du 1er janvier de l'année suivant l'entrée en vigueur » est cohérent avec ce fait générateur. L'année N (année d'entrée en vigueur) reste due ; les années N+1 et suivantes sont supprimées. Les exercices décalés ne créent pas de trou : la valeur ajoutée d'un exercice clos en N+1 n'est simplement plus taxée.
- **Taux et barèmes.** 1586 quater est supprimé pour les années supprimées. Les dégrèvements anciens (188 €, et 125 €/63 € selon les versions) sont maintenus pour les années anciennes. La correction de RT-FUTFISC-13, qui demande de viser « chacune des années antérieures », reste pertinente pour la proposition de 1586 quater.
- **Acomptes et solde de la dernière année.**
  - 1679 septies proposé : « Aucun acompte ni solde de CVAE n'est dû pour une année supprimée, même lorsque la base de calcul aurait été tirée d'une année antérieure ». Les sommes indûment versées sont restituables selon les règles de l'indu, sans liquidation annuelle.
  - Le solde de l'année N (déclaration en mai N+1) reste régi par les règles anciennes, y compris la modulation et la restitution à 60 jours.
  - La date du « deuxième jour ouvré suivant le 1er mai » est fixée dans 1679 septies et 1586 octies eux-mêmes. Le retrait du renvoi à 1679 septies dans l'annexe III 344 I-0 bis ne crée donc pas de trou.
  - La contribution complémentaire 2025 (LF 2025 art. 62 V) est cantonnée par le VII du paquet.
- **Faveurs conservées.**
  - Plafonnement CFE : 1647 B sexies proposé applique le même taux à la seule CFE, avec les taux programmés. 1679 quinquies conserve la modulation du solde ; CGI 39 et l'annexe III 382-0 C sexies sont coordonnés.
  - La valeur ajoutée reste définie par 1586 sexies, réécrit en définition autonome et complète : 80/85 %, secteurs, plus-values de création.
  - 1600 conserve ses douze exonérations, la demi-base et le taux de 1,12 %.
  - Les abattements et exonérations de CFE (1466 A, 1466 F) sont expressément préservés par 1586 nonies proposé.
- **Effet mécanique du plafonnement.** Pour une entreprise plafonnée, le dégrèvement baisse du montant de la CVAE supprimée. Le gain net peut donc être nul, comme `cvae_removal[4]` le reconnaît. Ce n'est pas un défaut. La rédaction du paquet laisse toutefois place à une lecture de « dégrèvement à acquérir » qui équivaudrait à une CVAE fictive (RT-DOMCVAE-03).
- **Déclarations supprimées sans remplacement.** 1586 octies II (1330-CVAE et effectifs), 1649 quater B quater IV, l'annexe III 328 G bis à nonies D, R133-14 CSS 8° et l'annexe II 317 septies E : rien n'est remplacé. 238 bis HW (ratio électro-intensif) se justifie par les données comptables.
- **Affectations et compensations.**
  - Depuis 2023, le produit de la CVAE revient à l'État (LF 2023 art. 55 XXVI), et les collectivités reçoivent des fractions de TVA indépendantes du produit (XXIV, XXV). La suppression n'emporte donc pas de perte directe pour les collectivités, et le paquet conserve ces fractions (E).
  - La TA-CVAE affectée à CCI France disparaît sans compensation, conformément à l'orientation. Les textes de répartition et de plafond (code de commerce L711-16, LF 2012 art. 46) sont hors corpus (RT-DOMCVAE-06).
- **Anti-abus.** Les règles de consolidation de 1586 quater (I bis, III) perdent leur objet. Je n'ai trouvé aucune voie de contournement : la suppression est générale et ne dépend d'aucune condition manipulable.
- **Autres codes.**
  - CSS L137-33 (C3S) renvoie aux définitions de 1586 sexies, qui sont conservées. RT-FUTCSS-04 traite le basculement de 2030, et la C3S fait l'objet d'une autre mesure.
  - CSS R133-14 est coordonné.
  - Le code du travail ne contient aucun renvoi : D3324-3 est un faux positif.
  - Je n'ai trouvé aucun renvoi dans l'urbanisme ni dans le CCH.
- **Constitutionnel et européen.**
  - La mesure est générale et prospective, sans rétroactivité défavorable, et je ne vois pas de problème d'égalité.
  - La seule question constitutionnelle ouverte porte sur les sanctions anciennes (in mitius, RT-DOMCVAE-04).
  - Aides d'État : la mesure est générale. Le maintien du cadre de minimis de 1600 12° est conservé.
  - Pilier 2 : la CVAE n'est pas un impôt sur le bénéfice. Je n'ai pas vu d'effet sur l'ATAD ni sur la directive mère-fille.

## 5. Objections existantes confirmées, précisées ou contredites

| ID | Position |
|---|---|
| RT-FUTFISC-13 | **Précisée / contredite sur la prémisse** (RT-DOMCVAE-01). Le paquet cvae-calendar contient la neutralisation demandée, plus complète sur la contribution 2025, mais il n'est pas activé. L'objection reste valable tant que le paquet n'est pas activé ; il faut ensuite un seul véhicule. Sa correction de 1586 quater (« chacune des années antérieures ») est confirmée. |
| RT-FUTFISC-14 | **Précisée** (RT-DOMCVAE-02). Si le paquet est activé, les points a, b et d sont couverts : maintien de 1586 quinquies et sexies après 2030 et plancher « ne peut augmenter la valeur ajoutée ». Le point c (1599 quater D, 1609 İ, phrase lacunaire) reste ouvert. La correction de RT-FUTFISC-14 et le paquet sont incompatibles. |
| RT-FUTFISC-15 | Confirmée : accélération de la suppression légale de 2030, à compter comme une seule mesure. |
| RT-FUTFISC-16 | Confirmée, sans nouvel élément. 1649 quater E et H ne sont pas visés par le XXVIII B du paquet ; la correction propre de FUT-FISC reste nécessaire. |
| RT-FUTFISC-32 | Confirmée. Deux NOTA discordantes en relèvent également : 1647 B sexies LEGIARTI000051248495 (version 2029 dont la NOTA vise la CFE « due au titre de 2030 ») et 1647 B sexies A (NOTA « à compter du 1er janvier 2027 », version LEGI de 2030). Aucune objection nouvelle n'est créée. |
| RT-FUTCSS-10 | Hors du cœur du domaine (L311-3 4° CSS) : confirmée sans nouvel examen. Avancer « cotisation foncière des entreprises » à la date de suppression reste cohérent avec l'ancre de RT-DOMCVAE-05. |
| RT-P1-CGI-B-07, RT-P1-CGI-C-08, RT-P1-CGI-C-03 | Le modèle de bornage des affectations n'est pas en cause pour la CVAE : depuis 2023, l'affectation de la CVAE passe par l'État (XXVI) et le paquet la borne (E). Les objections restent valables pour les autres impositions (TLV, IFER). |
| RT-DOC-04 | Précisée par la liste propre au domaine (RT-DOMCVAE-06). |
| RT-XCUT-01 | Confirmée : 1586 sexies 2029 (ord. 2026-671 : « contributions douanières » au lieu de « contributions indirectes ») n'est pas reporté dans la proposition, rédigée sur la version 2022-2029. Il s'agit d'une substitution de mots, sans effet de fond. |
| RT-INST-01, RT-INST-02, RT-P1-TRAVAIL-A-03, RT-P1-TRAVAIL-B-12 | Sans lien de fond avec la CVAE (la mention « CVAE » vient du texte des motifs). Aucune position. |

## 6. Constats nouveaux (résumé ; détail dans DOM-CVAE.json)

| ID | Priorité | Statut | Nature | Objet |
|---|---|---|---|---|
| RT-DOMCVAE-01 | P1 | confirmé | anomalie d'inventaire | La neutralisation du calendrier existe (paquet cvae-calendar) mais n'est pas activée ; elle fait doublon avec la correction de RT-FUTFISC-13 ; les notes du noyau la disent « à préparer » |
| RT-DOMCVAE-02 | P1 | confirmé | incohérence du projet | 2030 : le paquet laisse jouer la réécriture de 1647 B sexies (perte de 1599 quater D et 1609 İ, VII évincé, double règle de période) et contredit la correction de RT-FUTFISC-14 |
| RT-DOMCVAE-03 | P2 | à confirmer | risque juridique | « dégrèvement de CFE […] à acquérir » : lecture possible d'une CVAE fictive, contraire à cvae_removal[4] |
| RT-DOMCVAE-04 | P2 | à confirmer | risque juridique | In mitius « réservée » sans être tranchée pour les amendes 1770 decies et les majorations 1731 3 des années anciennes |
| RT-DOMCVAE-05 | P2 | à confirmer | risque juridique | Ancre temporelle : auto-abrogation de 1586 ter, « la présente loi » dans des articles codifiés et réglementaires, ancres hétérogènes |
| RT-DOMCVAE-06 | P2 | à confirmer | réserve documentaire | Textes hors corpus : décret FNAET 2023-1101, code de commerce L711-16, LF 2012 art. 46, code de l'énergie L351-1, code des transports L5334-11, LPF, formulaires |

**Les plus importants.**

**RT-DOMCVAE-01.** RT-FUTFISC-13 conclut que les barèmes CVAE et les taux de TA-CVAE de 2027 à 2029 ne sont pas neutralisés. Le paquet `coordinations/cvae-calendar` contient pourtant cette neutralisation, intégralement rédigée. Le XXVIII B de LF 2023 art. 55 dispose : « Les calendriers de taux de cette cotisation et de sa taxe additionnelle sont sans application à ces années, y compris en 2027, 2028 et 2029. » Ce paquet est toutefois « proposal_not_adopted » et « non activée par son auteur ». Le noyau ne satisfait donc `cvae_removal[6]` que sous condition. FUT-FISC a rédigé une autre disposition transitoire, dont la liste d'articles diffère.

**RT-DOMCVAE-02.** Le paquet conserve le XXVII İ, qui applique la réécriture de 1647 B sexies à la CFE due à compter de 2030. Il déclare cette réécriture « applicable selon son calendrier propre ». La version 2030 limite la cotisation majorée aux taxes « 1607 bis, 1607 ter et 1609 B à 1609 H ainsi que du montant, calculées dans les mêmes conditions ». Elle perd ainsi la TASA d'Île-de-France et la taxe 1609 İ, que la proposition du projet conserve.

## 7. Propositions de correction (présentées séparément)

### C-01 (RT-DOMCVAE-01) — Véhicule unique de neutralisation du calendrier

*Texte.* Aucun texte nouveau. Adopter tels quels le XXVIII de LF 2023 art. 55, le V de LF 2024 art. 79 et le VII de LF 2025 art. 62 du paquet, comme dispositions de la loi de réforme (« L'article 55 de la loi n° 2022-1726 du 30 décembre 2022 de finances pour 2023 est complété par un XXVIII ainsi rédigé : […] » ; même formule pour les deux autres). Ne pas adopter en parallèle la disposition transitoire A-redactions n° 1 de FUT-FISC. Mettre à jour les notes de 1647 B sexies (LEGIARTI000048860555) et des articles 1586 ter à nonies : remplacer « coordination […] à préparer » par un renvoi au paquet.

*Justification.* Le paquet couvre les années 2027 à 2029, la date de 2030, la contribution complémentaire de 2025, les affectations de TVA et les années anciennes, et il exclut à dessein 1586 quinquies et sexies de la neutralisation. Deux textes concurrents créeraient une ambiguïté sur les mêmes années.

*Dépendances.* RT-FUTFISC-13 (à requalifier « résolu sous condition d'activation ») ; RT-FUTFISC-16, que le paquet ne traite pas ; JORF de LF 2023 art. 55 (subdivisions Q, T à Z), non lu.

### C-02 (RT-DOMCVAE-02) — Régime unique du plafonnement CFE à compter de 2030

*Texte de remplacement du 4e alinéa du C du XXVIII (LF 2023 art. 55) :*

> Le Q du I du présent article, en tant qu'il réécrit l'article 1647 B sexies du code général des impôts, n'est pas applicable ; cet article s'applique, à compter des impositions établies au titre de 2030, dans sa rédaction issue de la loi portant suppression de la cotisation sur la valeur ajoutée des entreprises. L'article 1647 B sexies A du même code et l'article 310 HC de l'annexe II à ce code s'appliquent à compter des impositions établies au titre de 2030 pour la détermination de la valeur ajoutée mentionnée au b du I de l'article 1647 B sexies, lorsqu'ils conduisent à une valeur ajoutée inférieure à celle déterminée en application des articles 1586 quinquies et 1586 sexies. Le calcul est établi au moyen des documents nécessaires à la demande de plafonnement, sans déclaration propre à la cotisation sur la valeur ajoutée des entreprises.

*Texte complémentaire dans la proposition de 1647 B sexies (LEGIARTI000048860555), au b du I :*

> b) Pour les autres contribuables, celle définie à l'article 1586 sexies ; à compter des impositions établies au titre de 2030, la valeur ajoutée ainsi définie ne peut excéder celle qui résulte de l'article 1647 B sexies A.

Le II reste inchangé, avec la liste complète « 1599 quater D, 1607 bis, 1607 ter et 1609 B à 1609 H ainsi que du montant de la taxe prévue à l'article 1609 İ ».

*Justification.* Cette rédaction garde, cumulativement, tous les éléments favorables : 80/85 %, règle de création, navigation (310 HC), majoration complète, VII protecteur, taux de 1,25 %. Elle supprime la double règle de période en conservant 1586 quinquies. Elle ne crée aucune formalité. Elle concilie l'objectif de RT-FUTFISC-14 et l'architecture du paquet.

*Dépendances.* Coordination de 1447 (renvoi au 1 du I de 1586 sexies, conservé) ; 238 bis HW (renvoi figé, compatible avec le C du XXVIII, 3e alinéa) ; vérification JORF du Q.

### C-03 (RT-DOMCVAE-03) — Rédaction du dégrèvement

*Texte (XXVIII C, 1er alinéa, dernière phrase) :*

> La suppression de la cotisation sur la valeur ajoutée des entreprises ne permet ni de relever ces taux ni de réduire un dégrèvement accordé ou dû au titre d'une année antérieure à cette suppression. Pour les années supprimées, le dégrèvement est calculé sur la seule cotisation foncière des entreprises, sans prise en compte d'une cotisation sur la valeur ajoutée des entreprises fictive.

*Justification.* Aligne le paquet sur le VII de 1647 B sexies et sur `cvae_removal[4]`. *Dépendances.* Aucune.

### C-04 (RT-DOMCVAE-04) — Sort des sanctions anciennes (choix de l'auteur)

*Option A, conforme à `cvae_removal[1]`* (à insérer dans 1770 decies et 1731 3, à la place de la réserve) :

> La suppression, pour les années supprimées, de l'amende prévue au présent article résulte de la suppression de la cotisation sur la valeur ajoutée des entreprises ; elle est sans incidence sur les sanctions encourues au titre des années antérieures, sous réserve des droits de recours.

*Option B, plus favorable :*

> Les amendes et majorations non définitivement prononcées au titre des années antérieures ne sont plus appliquées.

*Justification.* Le projet ne doit pas laisser au juge un choix de politique répressive. L'option B est une faveur ; elle ne doit pas être écartée sans examen du principe de nécessité des peines, dont la jurisprudence n'a pas été vérifiée ici. *Dépendances.* XXVIII F du paquet, à aligner.

### C-05 (RT-DOMCVAE-05) — Ancre temporelle unique

*Texte (article non codifié de la loi de réforme) :*

> I. – Les dispositions du code général des impôts, de ses annexes et du code de la sécurité sociale relatives à la cotisation sur la valeur ajoutée des entreprises et à sa taxe additionnelle, dans leur rédaction issue de la présente loi, s'appliquent aux impositions établies au titre de [année suivant l'entrée en vigueur] et des années suivantes, dites « années supprimées ».
>
> II. – Les impositions établies au titre des années antérieures demeurent régies par les dispositions qui leur sont applicables.

Dans les textes codifiés, remplacer « la présente loi » et les autres ancres par « à compter des impositions établies au titre de [année] ». Dans l'annexe III, viser « la loi n° … du … ». Mettre la proposition de 1586 ter sous la forme d'une règle maintenue (« La cotisation sur la valeur ajoutée des entreprises n'est pas due au titre des impositions établies à compter de [année]. […] ») plutôt que d'une auto-abrogation.

*Dépendances.* Toutes les propositions du noyau, R133-14 CSS, CGI 39, 1655 septies, le paquet cvae-calendar.

### C-06 (RT-DOMCVAE-06) — Pièces à obtenir

Décret n° 2023-1101 (FNAET) et article 344 quaterdecies de l'annexe III ; code de commerce L711-16 ; LF 2012 art. 46 ; code de l'énergie L351-1 ; code des transports L5334-11 ; LPF L56, L173, L174 et L265 (versions différées) ; formulaires 1330-CVAE, 1329-AC, 1329-DEF et 1327-CET. Ne pas reconstituer ces textes de mémoire. Si le décret FNAET renvoie encore à 1586 octies, prévoir sa modification par décret, sans déclaration de remplacement.

## 8. Incertitudes et éléments non examinés

- Les instructions JORF exactes de LF 2023 art. 55, LF 2024 art. 79 et LF 2025 art. 62 n'ont pas été lues : la version consolidée ne contient que des marqueurs « A modifié ». Cela touche la qualification de la réécriture 2030 de 1647 B sexies (RT-DOMCVAE-02).
- Le paquet cvae-calendar réécrit des articles non codifiés. Son adoption suppose des instructions de modification que la loi de réforme devra rédiger.
- Le décret FNAET n'est connu que par une source secondaire (consultée le 2026-10-26). Selon cette source, les effectifs viennent de la DSN depuis 2025 : la dépendance à 1586 octies est probablement faible, mais elle n'est pas vérifiée.
- Le principe in mitius appliqué aux sanctions fiscales d'un impôt supprimé n'a pas été vérifié en jurisprudence : aucune décision n'est citée.
- Les versions futures de 1600 (2027 à 2030) n'ont été examinées qu'au travers des objections RT-FUTFISC-13 et 32 et des en-têtes : pas de relecture intégrale propre.
- Le LPF, le code de commerce, le CGCT, le code de l'énergie et les formulaires sont hors corpus.
- Le noyau est encore `pending` en seconde passe : une proposition peut changer.

## 9. Couverture réelle

**Lus en entier (source et proposition, versions au 18 octobre 2026 et futures indiquées) :**
- CGI 1586 ter (2024-2027 + proposition ; 2027-2030) ;
- CGI 1586 quater (2026-2028 + proposition ; 2028 ; 2029) ;
- CGI 1586 quinquies (proposition entière ; source, partie I) ;
- CGI 1586 sexies (proposition entière ; source 2022-2029, avec diff mot à mot contre 2029-2030) ;
- CGI 1586 septies, 1586 octies, 1586 nonies, 1600 (2026 + proposition), 1679 septies, 1679 quinquies, 1447-0, 1731, 1770 decies, 1681 septies ;
- CGI 1647 B sexies (2026-2028 + proposition ; 2028 ; 2029 ; 2030) ;
- LF 2023 art. 55 : XXIV à XXVII de la source et XXVIII proposé en entier ; la partie I à XXIII est faite de marqueurs « A modifié/abrogé » ;
- LF 2024 art. 79 et LF 2025 art. 62 : source et proposition en entier.

**Lus sur les passages pertinents (CVAE, valeur ajoutée, plafonnement), pas en entier :** CGI 1447, 1649 quater B quater (I à IV, XV), 238 bis HW, 39, 1655 septies, 1647 B sexies A (7° et NOTA), 1635 sexies II ; CSS L137-33, R133-14 ; annexe II 317 septies E (proposition) ; annexe III 328 G bis à 328 G nonies D, 344-0 A, 344-0 B, 344-0 C, 344 I-0 bis, 344 I ter, 344 quindecies, 406 terdecies, 38, 39, 40 A, 46 C, 382-0 C ter, 382-0 C sexies (début de la source et de la proposition, clause type d'abrogation) ; travail D3324-3 (faux positif).

**Non lus :** versions futures de 1600 (2027 à 2030) en entier ; annexe II 310 HC ; versions 2030 de 1447, 1649 quater B quater, 1681 septies et 1731 ; 1647 B sexies A, au-delà du 7° ; textes hors corpus (§ 8) ; JORF des trois lois de finances.

Exports : `evidence/cited/20261026T230545Z/` (cgi_1586_*, cgi_1600_*, cgi_1647_B_sexies_*, cgi_1679_*, cgi_1731_*, cgi_1770_decies_*, cgi_1447*, cgi_238_bis_HW_*, cgi_39_*, cgi_1655_septies_*, css_L137-33_*, css_R133-14_*, travail_D3324-3_*, a2_317_septies_E_*, a2_310_HC_*, a3_328_G_*, a3_344*, a3_406_terdecies_*, a3_38_*, a3_39_*, a3_40_A_*, a3_46_C_*, a3_382-0_C_*). Le paquet est lu dans l'instantané (`snapshots/20261026T230545Z/coordinations/cvae-calendar/manifest.json`, empreinte 5e24e187…cd7f72 au `manifest.json` de l'instantané). `cite.py` ne couvre pas les articles non codifiés.
