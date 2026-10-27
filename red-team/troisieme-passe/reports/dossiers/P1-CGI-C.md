# Paquet P1-CGI-C — qualification des alertes « renvoi vers une abrogation proposée » (CGI)

Red-team juridique indépendante, troisième passe. Revue IA, pas une validation par un juriste.
Instantané : `snapshots/20261026T230545Z` (date de référence du corpus : 18 octobre 2026). Audit d'origine : `global-reference-audit-20261025T2341Z`. Revue effectuée le 26 octobre 2026.
La seconde passe continue : plusieurs cibles et dépendants sont encore « pending » à l'inventaire. Les conclusions ci-dessous sont donc provisoires.

## 1. Résultat en bref

- **147 alertes** réparties en **43 clusters** (43 cibles abrogées, 72 articles qui y renvoient). Toutes sont classées dans `reports/p1-work/P1-CGI-C-classification.jsonl`.
- Classement : **86 alertes écartées**, **37 coordinations manquantes**, **22 incohérences du projet**, **1 simple alerte**, **1 faux positif**. Aucune n'est « non examinée ». Aucune ne relève d'un dossier ouvert d'un autre agent.
- **13 objections** (`reports/dossiers/P1-CGI-C.json`) : **7 P1** (6 confirmées, 1 à confirmer) et **6 P2** (4 confirmées, 2 à confirmer). Aucune P0.
- La plupart des cibles sont des abrogations prospectives bien construites : elles maintiennent les années antérieures et contiennent une clause du type « Aucun renvoi au présent article ne peut rétablir… ». Beaucoup de renvois sont donc neutralisés. Les vrais problèmes viennent surtout de dépendants **réécrits sur une version antérieure de la cible**, qui appliquent encore activement la règle supprimée.

## 2. Périmètre réellement lu

Chaque pièce a été exportée par `tools/cite.py` (fichiers `evidence/cited/20261026T230545Z/<code>_<numéro>_<LEGIARTI>.json`). Pour chaque cible, la proposition d'abrogation a été lue en entier, avec son motif et ses notes. Pour chaque dépendant, le texte courant qui porte le renvoi a été lu, avec son motif et ses notes : la proposition s'il est `rewrite_draft`, la source s'il est `retained_unchanged`.

**Cibles (43, CGI)** : 1519 F (LEGIARTI000054356142), 1519 D (…54373218), 1519 G (…54373204), 990 I (…47288653), 1605 nonies (…48848701), 1519 H (…54373185), 990 D (…18014411), 1519 HA (…54373172), 290 quater (…18619290), 115 quinquies (…42159010), 1599 quater A bis (…54373143), 1599 quater B (…54373136), 1609 H (…54373107), 1519 I (…41470807), 1586 ter (…48847020), 881 M (…22335723), 1601-0 A (…51217366), 299 quinquies (…53189791), 54 octies (…6302462), 302 bis WD (…28447771), 235 ter X (…30059687), 238 bis HZ (…6304035), 1018 A (…51877580), 1609 G (…51219412), 641 (…6305176), 1635 bis AF (…37064931), 1599 quater C (…54373125), 1635 bis P (…33815210), 1595 bis (…37100546), 234 duodecies (…20013533), 1679 septies (…42908204), 650 (…6305188), 1644 (…6306858), 302 bis MB (…48826666), 796-0 bis (…6305480), 751 (…27517865), 1789 (…24041681), 1601 (…51217384), 235 ter ZE bis (…31779544), 641 bis (…28417046), 1519 C (…51220099), 1600 A (…53562186), 224 (…53561826). Les identifiants abrégés commencent par LEGIARTI0000.

**Dépendants (72)**, lus en entier sauf mention contraire :
- CGI : 1635-0 quinquies, 1379, 1379-0 bis, 1586, 1609 nonies C, 1609 quinquies C, 1599 bis, 1649 A quater, 1649 quater B quater (seuls les passages 990 I et les notes ont été lus), 1681 septies, 990 I bis, 750 ter, 990 E, 990 FA, 990 G, 1791 bis, 1673 bis, 1396, 1647 B sexies, 220 Z septies, 1586 quinquies, 1586 sexies (en-tête de coordination et une partie du corps), 881 L, 881 N, 1601, 1601-0 A, 299 septies, 302 bis WF, 39 (seuls le 1, 4°, et les notes ont été lus), 238 bis HZ bis, 1018 A bis, 1920, 1656 quater, 1728, 792-0 bis, 1647, 231 ter, 1693 bis, 968, 1753 ;
- annexe II : 242 octies, 306-0 F, 326 ter, 379, 380, 381 ;
- annexe III : 328 K, 328 O, 328 P, 255, 331 K bis, 331 K ter, 344 G nonies, 96 B, 96 C, 96 D, 38 quindecies A, 111 quater U, 344-0 B (seuls le 8° et les notes ont été lus), 344 quindecies, 267, 375, 344 I-0 bis, 281 N ;
- annexe IV : 121 K ter, 50 sexies B, 155-0 ter, 155-00 ter, 155 bis A ;
- CSS : L241-2, D133-4 ;
- CCH : R121-11.

Pièces de contrôle hors alertes, également lues : les sources et propositions de 1519 E, 1519 HB, 1599 quater A et 1736 (LEGIARTI000054373979 et la version future LEGIARTI000047006062) ; la source de 990 D ; les versions futures VIGUEUR_DIFF de 1586 ter, 881 M, 302 bis WD, 235 ter X, 1018 A, 302 bis MB, 1789, 235 ter ZE bis et 1519 B ; `reports/future-versions-20261026T230545Z.json` ; `coordinations/cvae-calendar/manifest.json` (passage pertinent seulement) ; `notes-contradictions/INDEX.md` ; les orientations de `policy-coordinations.json` (fiscalité, successions, CVAE, coupes et avantages, IS à la distribution, CSI, droits fixes, taxe sur les salaires) et `site-summaries.json`.

## 3. Méthode

1. Pour chaque cible : clauses de transition, de neutralisation des renvois et de préservation.
2. Pour chaque dépendant : vérification que le numéro cité vise bien la cible (même code, même article). Un faux positif a été trouvé : R121-11 du CCH vise le décret n° 2012-1246, pas le CGI.
3. Qualification selon l'addendum :
   - **écartée** : renvoi transitoire, borné, neutralisé par la cible ou utile aux seules années anciennes ;
   - **coordination manquante** : texte maintenu non borné, quand la cible elle-même demande la coordination ;
   - **incohérence du projet** : proposition réécrite qui organise activement la règle supprimée.
4. Une objection par effet juridique : les alertes répétées sur un même mécanisme sont regroupées.
5. Vérification annexe des versions futures des cibles. Les cas trouvés sont déjà couverts par RT-XCUT-01 (voir § 6) et ne sont pas comptés une seconde fois.

## 4. Constats (objections)

### P1

**RT-P1-CGI-C-01 — 1635-0 quinquies maintient l'IFER alors que ses dix composantes sont abrogées** (incohérence du projet, confirmé ; 7 alertes)
L'article de tête dit encore « Il est institué […] une imposition forfaitaire sur les entreprises de réseaux », déterminée par les articles 1519 D à 1599 quater B. Son motif porte : « Conservation de l'imposition et de ses composantes ». Or 1519 D, E, F, G, H, HA, HB et 1599 quater A, A bis et B sont tous proposés à l'abrogation pour les années commençant après l'entrée en vigueur. La désindexation proposée au II ne s'appliquerait alors à aucune année si les deux réformes entrent en vigueur ensemble. Les clauses anti-renvoi des composantes empêchent la perception, mais la loi se contredit sur l'existence même de l'impôt.

**RT-P1-CGI-C-02 — 1649 A quater et 1736 VI maintiennent la déclaration sanctionnée des transformateurs** (incohérence du projet, confirmé ; 1 alerte)
1649 A quater a été réécrit pour alléger la répétition annuelle, avec le motif « Ce n'est ni une suppression ni une baisse de l'IFER ». Il conserve donc, sans borne, une déclaration assortie de l'amende de 1736 VI (1 000 € par transformateur, plafond 10 000 €). Or 1519 G supprime la composante et toute formalité qui lui est exclusivement liée, et 328 P de l'annexe III abroge les modalités réglementaires. Les notes de 328 P relèvent elles-mêmes que cette coordination reste à faire.

**RT-P1-CGI-C-03 — attribution de compensation des EPCI à fiscalité professionnelle unique (1609 nonies C V)** (coordination manquante, à confirmer ; effet distinct des alertes)
L'attribution de compensation est figée sur les produits de l'année précédant la première application, y compris l'IFER et la taxe additionnelle de 1519 I (I bis 1 et 2). Elle n'est pas indexable et constitue une dépense obligatoire. Une fois ces impôts supprimés, l'EPCI continue de la verser. La réduction unilatérale n'est ouverte qu'en cas de « diminution des bases imposables » : il est incertain qu'une suppression d'impôt entre dans ce cas. Le projet refuse à juste titre d'inventer une compensation, mais il ne dit pas qui supporte la perte. C'est un choix à écrire.

**RT-P1-CGI-C-04 — 1673 bis, 379, 380 et 381 de l'annexe II organisent une retenue que 115 quinquies supprime** (incohérence du projet, confirmé ; 5 alertes)
Les dépendants ont été coordonnés avec une version antérieure de 115 quinquies qui conservait une retenue au désinvestissement. Ils prévoient un dépôt au 15 du mois suivant, un « régime de désinvestissement institué à l'article 115 quinquies » et une restitution « pour les distributions futures ». La proposition courante de 115 quinquies supprime la retenue pour les exercices nouveaux, « qu'ils demeurent en France ou soient désinvestis hors de France ». Ses notes demandent elles-mêmes de retirer le dépôt mensuel de 379.

**RT-P1-CGI-C-05 — 750 ter (donations maintenues) renvoie à la définition de 990 D, supprimée** (incohérence du projet, confirmé ; 1 alerte)
« La détention peut être directe ou résulter d'une chaîne de participations au sens de l'article 990 D ». La proposition de 990 D remplace tout le texte par une abrogation, ce qui fait disparaître la définition et ses exclusions renvoyant à 990 E. Les droits de donation, préservés par les orientations, perdent ainsi une règle d'assiette pour les non-résidents. Le projet a déjà résolu un cas identique en 968 par un renvoi figé à la rédaction de la veille.

**RT-P1-CGI-C-06 — 50 sexies B de l'annexe IV maintient toute la billetterie fiscale** (incohérence du projet, confirmé ; 1 alerte)
Le texte prévoit toujours que « Toute entrée […] doit être constatée par la remise d'un billet » et impose le cahier des charges de 1993. La proposition n'a retiré que le nom du fabricant. 290 quater supprime pourtant les obligations « prises pour l'application du présent article ». Les notes de 290 quater relèvent cette contradiction.

**RT-P1-CGI-C-07 — 38 quindecies A de l'annexe III maintient la déclaration abrogée de 54 octies** (incohérence du projet, confirmé ; 2 alertes)
Le règlement conserve la déclaration par bien et le tableau de résultat prévisionnel. Il affirme même que la dispense « ne supprime pas la déclaration légalement due ». Or 54 octies est abrogé, « y compris lorsque l'amortissement a commencé avant cette date ».

### P2

**RT-P1-CGI-C-08 — affectations et substitutions IFER, 1519 B et 1519 I non bornées** (coordination manquante, confirmé ; 36 alertes)
Sont concernés 1379 (retenu inchangé, 8°–15°), 1379-0 bis (I, V et V bis), 1586 (3° à 5° bis), 1609 nonies C (I bis 1, 1 bis à 1 quater et 2) et 1609 quinquies C (II 2 et III 4, retenu inchangé). Ces textes ne peuvent pas rétablir les impôts, car les cibles réservent les affectations anciennes et interdisent tout rétablissement par renvoi. Mais ils ne sont pas bornés, leurs motifs supposent l'impôt maintenu, et ils laissent ouvertes des délibérations sans objet. Le projet sait pourtant faire : 1599 bis et le 2° de 1586 sont bornés. Les notes de 1519 G et 1519 H demandent cette coordination.

**RT-P1-CGI-C-09 — 990 E réforme pour l'avenir les déclarations d'une taxe abolie** (incohérence du projet, confirmé ; 3 alertes)
Le motif porte « La taxe de 990 D reste une incitation… ». L'effet est neutralisé, car 990 D cite expressément 990 E et 990 F parmi les obligations qui ne sont plus exigibles. Le motif de 990 G est lui aussi périmé, mais son texte reste nécessaire aux années anciennes : cette alerte est écartée.

**RT-P1-CGI-C-10 — 231 ter VII conserve la procédure de la taxe de stationnement (1599 quater C), abolie** (incohérence du projet, confirmé ; 2 alertes)
231 ter prévoit encore une déclaration accompagnée du paiement « avant le 1er mars de chaque année ». Les deux taxes n'ont pas non plus la même date de bascule. Si la loi entre en vigueur un 1er janvier, la taxe de stationnement reste due un an de plus.

**RT-P1-CGI-C-11 — 281 N de l'annexe III réserve le 1 de 650, abrogé** (coordination manquante, confirmé ; 1 alerte)
Les notes de 650 demandent de viser 654 à la place.

**RT-P1-CGI-C-12 — 1753 : exclusion des commissions fondée sur 1789 abrogé** (simple alerte, à confirmer ; 1 alerte)
L'exclusion fondée sur 1747, second alinéa, est neutralisée, mais celle fondée sur 1789 ne l'est pas, sans motif.

**RT-P1-CGI-C-13 — autonomie financière des collectivités (art. 72-2 C.)** (risque juridique, à confirmer ; sans alerte propre)
L'effet cumulé des suppressions de l'IFER, de 1519 I, de 1519 B/C, de 1599 quater C, des TSE (1609 G et 1609 H) et de 1595 bis n'est pas chiffré au regard du plancher organique. Il faut chiffrer, pas renoncer.

## 5. Alertes écartées (86) et faux positif (1)

- **Abrogations coordonnées des textes d'application** : 328 K, 328 O et 328 P (annexe III) ; 121 K ter (annexe IV) ; 306-0 F et 326 ter (annexe II) ; 331 K bis et 331 K ter ; 96 B, 96 C et 96 D ; 111 quater U ; 302 bis WF ; 990 FA ; 1018 A bis ; 1601 et 1601-0 A ; 238 bis HZ bis.
- **Renvois expressément bornés aux faits anciens** : 1599 bis, 344 G nonies, 990 I bis, 1681 septies, 1649 quater B quater, 1728, 792-0 bis, 881 L, 881 N, 1586 quinquies, 1586 sexies, 344 quindecies, 344-0 B, 344 I-0 bis, 375, L241-2 CSS, 968 (renvoi figé).
- **Renvois neutres utiles aux années anciennes, neutralisés par la cible** : 255, 242 octies (suppression rédactionnelle recommandée), 1791 bis, 990 G, 1396, 1647 B sexies, 220 Z septies, 1656 quater, 1920, 1647 III bis, 1693 bis, 267, 155 bis A, D133-4 CSS, 299 septies (coordination formelle recommandée par 299 quinquies), 39 (1, 4°).
- **Définitions dont le champ suit la cible** : 155-0 ter et 155-00 ter de l'annexe IV (motifs périmés).
- **Faux positif** : R121-11 du CCH (décret n° 2012-1246, articles 220 à 228).

## 6. Points couverts ailleurs (non comptés)

Pour sept cibles de ce paquet, une version future déjà publiée (VIGUEUR_DIFF) n'a ni proposition ni place à l'inventaire. Elle peut donc remplacer l'abrogation proposée à sa date d'effet :
- 881 M (2029, LEGIARTI000053545728) ;
- 302 bis WD (2027, …53187726) ;
- 235 ter X (2027, …51191113 et …53154614) ;
- 1018 A (2029, …52846070) ;
- 302 bis MB (2027, …54567330) ;
- 1789 (2029, …52845684) ;
- 235 ter ZE bis (2027, …53154681).

Même situation pour 1519 B (2027, …53188734), voisin de la cible 1519 C, et pour 1736 VI (2030). Ces cas figurent dans `reports/future-versions-20261026T230545Z.json` et relèvent de **RT-XCUT-01** (`dedupe.json`). Ils sont cités ici comme preuves, sans nouvelle objection. Pour 1586 ter (version 2027–2030, …53188762), une coordination de calendrier existe (`coordinations/cvae-calendar`) ; elle n'a pas été relue en entier ici.

## 7. Propositions de correction (présentées séparément)

Les textes ci-dessous sont des propositions de red-team. Ils restent à confronter à la version courante des lots au moment de l'intégration.

**C-01 — CGI 1635-0 quinquies (texte complet proposé)**
> I. – Il est institué au profit des collectivités territoriales ou de leurs établissements publics de coopération intercommunale une imposition forfaitaire sur les entreprises de réseaux. Cette imposition est déterminée dans les conditions prévues aux articles 1519 D, 1519 E, 1519 F, 1519 G, 1519 H, 1519 HA, 1519 HB, 1599 quater A, 1599 quater A bis et 1599 quater B.
> Le présent I ne s'applique qu'aux impositions établies au titre des années pour lesquelles ces articles demeurent applicables. Aucune imposition forfaitaire sur les entreprises de réseaux n'est établie, sur le fondement du présent article, au titre d'une année pour laquelle la composante concernée est supprimée.
> II. – À compter du 1er janvier de l'année suivant celle de l'entrée en vigueur de la loi supprimant leur revalorisation à la hausse, les montants et tarifs de l'imposition forfaitaire sur les entreprises de réseaux ne sont plus augmentés au titre de l'indexation annuelle. Lorsque le taux prévisionnel, associé au projet de loi de finances de l'année, d'évolution des prix à la consommation des ménages, hors tabac, pour la même année est négatif, les montants et tarifs de l'année précédente sont diminués selon ce taux. Les exonérations, réductions et tarifs plus favorables demeurent applicables. Le présent II ne s'applique qu'aux composantes encore dues au titre de l'année concernée ; il ne peut ni rétablir ni revaloriser une composante supprimée.
> III. – Les impositions des années antérieures restent régies par les dispositions qui leur étaient applicables, y compris leurs tarifs, exonérations, réductions, affectations, restitutions, prescriptions et recours. Le présent article n'institue aucune compensation ni aucun prélèvement de remplacement.

Justification : aligne la tête sur les dix abrogations et conserve la désindexation favorable si elle précède la suppression. Dépendances : les dix composantes et C-08.

**C-02 — CGI 1649 A quater (texte complet proposé) et 1736 VI**
> Le présent article est abrogé pour les années d'imposition commençant à compter du 1er janvier suivant l'entrée en vigueur de la loi supprimant la composante de l'imposition forfaitaire sur les entreprises de réseaux prévue à l'article 1519 G. Aucune déclaration ni confirmation n'est exigée au titre de ces années, et l'amende prévue au VI de l'article 1736 ne peut être appliquée à raison de ces années.
> Pour les années antérieures, le propriétaire de transformateurs électriques mentionnés à l'article 1519 G qui font l'objet d'un contrat de concession déclare à l'administration des finances publiques l'identité du concessionnaire, le nombre de transformateurs électriques par commune qui font l'objet d'un contrat de concession et, pour chacun d'eux, la tension en amont. Après la première déclaration, cette déclaration n'est renouvelée que pour les années au titre desquelles l'un de ces éléments a été modifié. Aucune confirmation de l'absence de modification n'est exigée. La déclaration s'effectue dans les conditions et délais fixés par décret et sous peine des sanctions prévues au VI de l'article 1736.
> La dispense de renouvellement s'applique aux échéances déclaratives intervenant à compter de l'entrée en vigueur de la loi. Les déclarations déjà souscrites valent première déclaration. Les obligations dont l'échéance est antérieure demeurent régies par les dispositions antérieures, sous réserve de l'application de la loi répressive plus douce aux sanctions non définitives.

Ajouter à la fin du VI de 1736 : « Le présent VI ne s'applique qu'aux déclarations dues au titre des années d'imposition antérieures à la suppression de la composante prévue à l'article 1519 G. » Dépendances : 328 P (déjà concordant) et la version 2030 de 1736 (RT-XCUT-01). Vérifier le même point pour 1649 A ter et 1736 V (composante 1599 quater A).

**C-03 — CGI 1609 nonies C, V 1° (alinéa à insérer après le sixième alinéa ; option à valider par l'auteur)**
> Pour l'application des cinquième et sixième alinéas du présent 1°, la suppression, pour les années d'imposition mentionnées aux articles 1519 D à 1519 HB et 1519 I, des composantes de l'imposition forfaitaire sur les entreprises de réseaux et de la taxe additionnelle à la taxe foncière sur les propriétés non bâties est assimilée à une diminution des bases imposables réduisant le produit global disponible. La réduction des attributions de compensation qui en résulte ne peut excéder, pour chaque commune, le produit de ces impositions retenu lors du calcul de son attribution de compensation, ni la perte de produit effectivement constatée. Elle ne crée aucune ressource ni aucun prélèvement nouveau.

Justification : ne rétablit aucun impôt et ouvre une base claire à la répartition de la perte ; elle reste encadrée par les plafonds existants (5 % des recettes réelles de fonctionnement). Autre option : statu quo écrit (l'EPCI supporte la perte), ou compensation budgétaire non présumée. Dépendances : 1609 quinquies C, 1379-0 bis.

**C-04 — 115 quinquies et ses textes d'application**
- 1673 bis (texte complet proposé) :
  > Pour les exercices ouverts avant l'entrée en vigueur de la loi abrogeant l'article 115 quinquies, la retenue à la source exigible en vertu des dispositions de cet article est déclarée et versée au Trésor par la société au plus tard le quinzième jour du quatrième mois qui suit la clôture de l'exercice. Si l'exercice est clos le 31 décembre ou si aucun exercice n'est clos en cours d'année, le versement est effectué au plus tard le 15 mai.
  > Pour les exercices ouverts à compter de cette entrée en vigueur, aucune retenue, aucune déclaration ni aucun versement n'est exigé sur le fondement du présent article, y compris à raison d'un désinvestissement. Les exonérations et droits à restitution afférents aux exercices antérieurs demeurent applicables.
- 379 de l'annexe II (texte complet proposé) :
  > 1. Pour les exercices ouverts avant l'entrée en vigueur de la loi abrogeant l'article 115 quinquies du code général des impôts, la société étrangère qui réalise des bénéfices en France sans y avoir son siège produit une déclaration en vue de la liquidation de la retenue à la source exigible en vertu de cet article. Elle l'adresse au service dont relève l'établissement de l'impôt sur les sociétés, dans le délai prévu pour la déclaration des résultats de l'exercice concerné, et y fait apparaître le montant en euros des bénéfices et plus-values à retenir pour l'assiette de l'impôt sur les sociétés, de l'impôt correspondant et des bénéfices et plus-values réalisés en France et exonérés de cet impôt. Elle est accompagnée du versement de la retenue exigible.
  > 2. Aucune déclaration ni aucun versement n'est exigé sur le fondement du présent article au titre des exercices ouverts à compter de cette entrée en vigueur, ni à raison d'un désinvestissement ou d'une distribution qui s'y rapporte.
  > 3. Les rectifications et restitutions relatives aux exercices antérieurs suivent les articles 380 à 382.
- 380 de l'annexe II : supprimer la dernière phrase du deuxième alinéa du I (« Pour les retenues relevant du régime de désinvestissement… ») et le IV. Conserver les I à III et le V.
- 381 de l'annexe II : remplacer la dernière phrase par : « La restitution demeure ouverte pour les retenues afférentes aux exercices ouverts avant l'abrogation de l'article 115 quinquies du code général des impôts, y compris lorsque la demande est présentée ultérieurement dans les délais, sans double restitution. »

**C-05 — CGI 750 ter, I 2°, deuxième alinéa (phrase à remplacer)**
> La détention peut être directe ou résulter d'une chaîne de participations au sens de l'article 990 D dans sa rédaction en vigueur la veille de l'entrée en vigueur de la loi supprimant la taxe prévue à cet article, sans limite du nombre d'intermédiaires.

**C-06 — CGI annexe IV 50 sexies B (texte complet proposé)**
> I. – Pour les spectacles organisés à compter de l'entrée en vigueur de la loi abrogeant l'article 290 quater du code général des impôts, aucune remise de billet, aucun enregistrement ni aucune conservation de données individuelles d'entrée, aucun contrôle d'entrée, aucune mention sur les billets ou les souches et aucune conformité au cahier des charges annexé à l'arrêté du 8 mars 1993 ne sont exigés sur le fondement du présent article. La délivrance volontaire de billets reste possible. Aucun billet, registre, équipement ou relevé de remplacement n'est exigé.
> II. – Pour les spectacles organisés avant cette date, les règles du présent article dans sa rédaction antérieure demeurent applicables. Les billets, souches, données et systèmes constitués avant cette date restent soumis aux règles de conservation et de contrôle qui leur étaient applicables, sans réfection ni mise en conformité. Les créances, restitutions, prescriptions et recours relatifs aux opérations antérieures demeurent régis par les règles qui leur sont applicables ; les sanctions des seuls manquements supprimés relèvent de la loi répressive plus douce.
> III. – Les obligations concernant les mentions à porter sur les billets d'entrée dans les établissements de spectacles cinématographiques, la fourniture et l'utilisation de ces billets sont fixées par la réglementation de l'industrie cinématographique.

Dépendances : 50 sexies C (renvoi aux alinéas de l'ancien III), cahier des charges de 1993, reprise CIBS. Il est recommandé de supprimer le deuxième alinéa de 242 octies de l'annexe II.

**C-07 — CGI annexe III 38 quindecies A (texte complet proposé)**
> Le présent article est abrogé à compter de l'entrée en vigueur de la loi abrogeant l'article 54 octies du code général des impôts. Aucune déclaration, aucun tableau de résultat prévisionnel ni aucun modèle n'est exigé sur son fondement, y compris pour un bien dont l'amortissement a commencé avant cette date ou dont le délai de dépôt est déjà expiré. Les déclarations déjà déposées ne sont pas à refaire.
> Les manquements antérieurs demeurent régis par les règles applicables à leur date, sous réserve de l'application de la loi répressive plus douce aux sanctions non définitives. Les déductions d'amortissement et leurs conditions de fond, notamment celles de l'article 39 C du code général des impôts, ne sont pas modifiées.

**C-08 — clause de bornage des affectations (modèle 1599 bis)**
- À la fin du I de 1379 :
  > Les 8° à 15° ne s'appliquent, pour les impositions prévues aux articles 1519 B, 1519 D à 1519 HB et 1519 I, qu'aux produits afférents aux années d'imposition antérieures à leur suppression, y compris lorsqu'ils sont recouvrés, régularisés ou restitués ultérieurement. Ils ne constituent pas un fondement d'imposition et ne peuvent rétablir une imposition supprimée.
- Clause équivalente :
  - à la fin du I de 1586, pour les 3° à 5° bis ;
  - à la fin du V bis de 1379-0 bis, visant les I, V et V bis ;
  - à la fin du I bis de 1609 nonies C, visant les 1, 1 bis, 1 ter, 1 quater et 2 ;
  - à la fin du II de 1609 quinquies C, visant le 2 du II et le 4 du III.
- Statut : 1379 et 1609 quinquies C passent à `rewrite_draft`.

**C-09 — CGI 990 E (alinéa à insérer en tête)**
> Le présent article ne s'applique qu'à la taxe due au titre des années d'imposition antérieures à celles pour lesquelles l'article 990 D la supprime. Pour les années suivantes, aucune déclaration prévue aux d et e du 3° n'est exigée et l'absence de ces déclarations ne peut fonder aucune imposition.

Corriger aussi les motifs de 990 E et de 990 G, qui supposent la taxe maintenue.

**C-10 — CGI 231 ter**
- VII, phrases 2 et 3 :
  > Pour la taxe distincte prévue à l'article 1599 quater C, due au titre des seules années antérieures à sa suppression, les modalités auxquelles renvoie le VII de cet article demeurent le dépôt d'une déclaration accompagnée du paiement de cette seule taxe, avant le 1er mars de l'année d'imposition, auprès du comptable public compétent du lieu de situation des surfaces imposables. Ce dépôt ne comprend aucune déclaration ni aucun paiement au titre de la taxe supprimée par le présent article. Aucune déclaration ni aucun paiement n'est exigé au titre de la taxe prévue à l'article 1599 quater C pour les années pour lesquelles celle-ci est supprimée.
- X, dernière phrase :
  > Les exclusions propres à l'article 1599 quater C demeurent applicables dans leur champ exact pour les années où cette taxe reste due.
- Aligner ou motiver les deux dates de bascule.

**C-11 — CGI annexe III 281 N, I (début à remplacer)**
> I. – Sous réserve, pour les actes présentés à la formalité, des règles de compétence prévues à l'article 654 du code général des impôts et, pour les présentations antérieures à l'abrogation de l'article 650 du même code, du 1 de cet article, la déclaration prévue à l'article 790 G du même code est déposée en un seul exemplaire…

**RT-P1-CGI-C-12 et -13** : pas de texte imposé. L'auteur doit faire un choix (neutralisation symétrique pour 1789 dans 1753) et la réforme doit être chiffrée (ratio d'autonomie financière par catégorie de collectivités).

Ces corrections préservent :
- toutes les années antérieures ;
- les exonérations et avantages (désindexation, plafonnement CFE, exonération de 790 G, révision favorable des retenues, 1384 F, TASCOM) ;
- l'absence de toute taxe ou formalité de remplacement.

## 8. Incertitudes et éléments non examinés

- La seconde passe continue. Sont « pending » notamment 1635-0 quinquies, 1519 F, 115 quinquies et 990 D, ainsi que d'autres pièces : chaque proposition peut changer.
- Lectures partielles : 39 (seuls le 1, 4°, et les notes), 344-0 B (seuls le 8° et les notes), 1649 quater B quater (seuls les passages 990 I) et 1586 sexies (en-tête et une partie du corps). Ces alertes sont écartées sur la base de leur passage pertinent, et `read_in_full` vaut `false`.
- Non examinés : 1649 A ter et 1736 V (composante 1599 quater A, hors paquet) ; 990 F et le formulaire 2746 ; 382 et 1668 en entier ; 654 proposé ; 50 sexies C ; le cahier des charges de 1993 ; les textes du CGCT et du CIBS ; les formulaires.
- Aucune source primaire en ligne n'a été consultée. Les références constitutionnelles et organiques de RT-P1-CGI-C-13 sont à vérifier sur Légifrance. L'interprétation de « diminution des bases imposables » (RT-P1-CGI-C-03) n'a pas été confrontée à la jurisprudence.
- Aucun chiffrage n'a été établi ni présumé.
- Cette revue IA ne vaut pas validation par un juriste.
