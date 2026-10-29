# Dossier MENS — CGI annexe III 111-0 H 2° / annexe IV 50-0 I II : déclaration (« rapport ») mensuelle des fabricants de vinaigre

Red-team juridique indépendante, troisième passe. Rapport établi le 26 octobre 2026 sur l'instantané `20261026T230545Z` (corpus au 18 octobre 2026). Revue produite par une IA : elle ne vaut pas validation par un juriste. La seconde passe continue : ces conclusions sont provisoires.

## 1. Synthèse

- **RT-MENS-01 (P1, incohérence du projet, confirmé).** Sur les propositions courantes, 111-0 H 2° supprime pour les nouveaux mois la déclaration mensuelle récapitulative des fabricants de vinaigre. Or 50-0 I II proposé continue de régler le contenu de cette même déclaration et affirme que la dispense « néant » « ne modifie pas […] les déclarations des mois comportant une opération de fabrication ». Les opérateurs, les mois, l'objet et la finalité sont les mêmes. Il ne s'agit pas de deux obligations distinctes : 50-0 I II ne fait que mettre en œuvre le 2° de 111-0 H. On peut tirer argument de la hiérarchie des normes (arrêté d'application contre décret), mais le texte reste contradictoire et l'effet probable.
- **RT-MENS-02 (P2, risque juridique de transition, confirmé).** Les deux transitions ne retiennent pas le même fait générateur. 111-0 H vise les « mois commençant à compter de » l'entrée en vigueur, avec les mois antérieurs dus « selon les règles antérieures ». 50-0 I vise les « formalités accomplies à compter de » l'entrée en vigueur, « y compris dans les procédures en cours ». Les deux règles se heurtent pour le mois à cheval, pour les déclarations « néant » des mois antérieurs déposées après l'entrée en vigueur et pour les déclarations dues mais non déposées. Rien n'est dit des rectifications ni des sanctions. Enfin, l'ancre « réforme » n'est pas synchronisée entre un décret et un arrêté.
- **RT-MENS-03 (P2, alerte écartée, faux positif).** Il n'y a pas d'incompatibilité générale entre 50-00 D (annexe IV) et les corrections traçables de 111-0 G/H. L'exception spéciale est déjà écrite dans G 3° et H 3°. Elle ne doit pas être étendue à tous les registres vitivinicoles.
- **RT-MENS-04 (P2, réserve documentaire, à confirmer).** Plusieurs pièces manquent : la base légale de 302 D bis (état `ABROGE_DIFF`, abrogé par l'ordonnance n° 2021-1843, art. 10, borne technique `2222-02-22`), la concordance avec le CIBS, l'arrêté du 4 juillet 2005 et ses modèles (aucun modèle de déclaration mensuelle du vinaigre n'est identifié), ainsi que les obligations européennes vitivinicoles autonomes. Aucune confusion entre une borne technique et une date normative ne figure dans les propositions courantes. Le risque est signalé pour l'avenir.
- **RT-MENS-05 (P2, anomalie d'inventaire, confirmé).** La fiche d'impact de 50-0 I décrit l'état « après » comme « Déclaration seulement pour les mois actifs ». Elle étend la population à tous les « utilisateurs soumis à comptabilité matières » et peut compter, pour les nouveaux mois, un gain déjà inclus dans la mesure `vinaigre-fin-declaration-mensuelle` de 111-0 H.

La dépendance au numéro UT (rubrique c de 50-0 I II) est constatée mais non comptée à part. Pour les nouveaux mois, elle disparaît avec la correction RT-MENS-01. Pour les anciens mois, la correction RT-MENS-02 la neutralise par « le cas échéant ». La suppression du numéro lui-même relève de **RT-INUT** (302 D bis III, 111-0 E/F, 50-0 G/H, annexe II 289 15°) et n'est pas doublée ici.

## 2. Périmètre réellement lu

### 2.1 Articles lus en entier par `tools/cite.py`

Chaque article a été lu en entier : source, NOTA, bornes, état, proposition, motif, notes de revue, ligne propriétaire et statut d'inventaire. Les fichiers sont dans `evidence/cited/20261026T230545Z/`.

| Code | Numéro | Version | Bornes | État | Statut du projet | Seconde passe |
|---|---|---|---|---|---|---|
| a3 | 111-0 G | LEGIARTI000006298857 | 2005-07-06 → 2999-01-01 | VIGUEUR | rewrite_draft | completed |
| a3 | 111-0 H | LEGIARTI000006298858 | 2005-07-06 → 2999-01-01 | VIGUEUR | rewrite_draft | completed |
| a3 | 111-0 E | LEGIARTI000006298854 | 2005-07-06 → 2999-01-01 | VIGUEUR | rewrite_draft | completed |
| a3 | 111-0 F | LEGIARTI000006298855 (historique) | 2005-07-06 → 2006-01-01 | MODIFIE | — | hors manifeste |
| a3 | 111-0 F | LEGIARTI000006298856 | 2006-01-01 → 2999-01-01 | VIGUEUR | rewrite_draft | completed |
| a4 | 50-0 I | LEGIARTI000006300444 | 2005-07-06 → 2999-01-01 | VIGUEUR | rewrite_draft | completed |
| a4 | 50-00 D | LEGIARTI000006300435 | 2001-03-31 → 2999-01-01 | VIGUEUR | rewrite_draft | completed |
| a4 | 50-0 H | LEGIARTI000006300443 | 2005-07-06 → 2999-01-01 | VIGUEUR | rewrite_draft | completed |
| a4 | 50-0 G | LEGIARTI000006300441 (historique) | 2005-07-06 → 2006-01-01 | MODIFIE | — | hors manifeste |
| a4 | 50-0 G | LEGIARTI000006300442 | 2006-01-01 → 2999-01-01 | VIGUEUR | retained_unchanged (proposed_xml NULL) | completed |
| cgi | 302 D bis | 9 versions, de LEGIARTI000006304984 à LEGIARTI000041535168, dont 2 MODIFIE_MORT_NE | 2001-09-01 → 2222-02-22 | dernière : ABROGE_DIFF (LEGIARTI000041472187) | rewrite_draft | **pending** |
| a2 | 289 | LEGIARTI000054363092 (version courante lue ; 21 autres versions exportées) | 2026-07-01 → 2999-01-01 | VIGUEUR | rewrite_draft | completed |

Le XML LEGI complet a aussi été examiné (métadonnées, `VERSIONS` et `LIENS`) pour 111-0 G, 111-0 H, 50-0 I et 302 D bis. Il fournit les liens de création suivants : décret n° 2005-758, art. 1, pour G/H, et arrêté du 4 juillet 2005, art. 1, pour 50-0 I. Il fournit aussi le lien `ABROGE` de l'ordonnance n° 2021-1843, art. 10, et les liens `CONCORDANCE` vers le CIBS (L313-7 à L313-14, L314-9 à L314-12) pour 302 D bis.

### 2.2 Recherche ciblée dans la base, en lecture seule

La recherche a porté sur toutes les sources et propositions des neuf corpus. Motifs recherchés : `111-0 H`, `50-0 I`, `111-0 G`, `50-00 D`, `vinaigr`, `UT`, puis, sur les textes en vigueur des annexes II, III et IV et du CGI, « déclaration récapitulative », « récapitul », « dixième jour », « déclaration mensuelle » et « comptabilité matières ».

Résultat. Aucun autre texte courant ne renvoie à 111-0 H ou à 50-0 I, et aucun ne prescrit une déclaration mensuelle du vinaigre. Les autres mentions de « vinaigre » sont soit historiques, soit sans rapport : par exemple, 50 duodecies de l'annexe IV est une liste tarifaire DOM. Les déclarations récapitulatives des entrepositaires agréés (annexe II 286 I/J, annexe IV 50-00 C/G) visent d'autres assujettis et n'ont pas été lues en entier (voir § 7).

### 2.3 Preuves scellées

- `evidence/sealed/runtime/alcohol-denaturation-coherence-readonly-20261026T1305Z/`. Lus en entier : REPORT.md, CONTROL.json, remaining-semantic-and-operational-requirements.json, unchanged-canonical-controls.json, capture-source-anchor.json, exact-corpus-code-title-catalogue.json, exploratory-read-limit.json, post-review-tool-launch-refusal.json, whole-official-displayed-source-body-comparison.json, ainsi que les sept constats de fresh-cross-corpus-semantic-qualification.json. Ses vingt-six gardes à cinq champs ont été confrontées automatiquement à l'instantané.
- `evidence/sealed/runtime/alcohol-2005-scoped-readonly-20261026T1505Z/`. Lus en entier : REPORT.md, CONTROL.json, fresh-2005-documentary-and-cross-level-qualification.json, remaining-requirements.json, new-copy-source-review.json, post-review-whole-scoped-input-stability.json, artifact-manifest.json, capture-current.log et source-diff-from-refused-copy.txt. Les cinq champs de whole-current-and-historical-inputs-two-RO.json ont été confrontés automatiquement à l'instantané.
- **Limite.** Les grosses copies de données d'entrée n'ont pas été lues ligne à ligne : `whole-*-inputs-two-RO.json` (575 Ko et 998 Ko), `whole-file-input-stability.json` et `whole-owner-files/`. Ce sont des copies des pièces du corpus, lues ici directement dans l'instantané.
- **Confrontation.** Pour les neuf identités courantes communes, les cinq champs (source_sha256, status, proposed_xml, reason, review_notes) sont **strictement égaux** entre l'instantané et les deux dossiers scellés. Les conclusions scellées portent donc sur les mêmes propositions, mais elles n'ont pas été reprises sans être revérifiées.
- Lus en complément : les REPORT.md de `cibs-alcohol-public-followup-20261026T1707Z`, `cibs-2021-primary-pistes-followup-20261026T1808Z` et `alcohol-2006-normative-followup-20261026T1600Z`.

### 2.4 Orientations

- `policy-coordinations.json` › `formalites_accises_et_cidre` (quatre consignes lues). Aucune ne vise expressément 111-0 H ou 50-0 I. On en retient l'esprit : supprimer les formalités demandées, ne prévoir aucune formalité de remplacement, conserver les droits, contrôles, preuves et pièces anciennes.
- `notes-contradictions/INDEX.md` (ligne MENS, et point « à ne pas transformer » sur 50-00 D / G/H).
- Les lignes propriétaires (`batches/automatic-impots-annexe-3/00031.json`, lignes 18 et 19 ; `batches/automatic-impots-annexe-4/00013.json`, ligne 9 ; `…/00012.json`, ligne 11) ont été lues dans leurs champs hors texte, y compris `substantive_impact`.

## 3. Méthode

1. Lecture entière des versions de chaque numéro, identifiées par code et identifiant LEGIARTI.
2. Reconstruction, sur les **propositions courantes**, du régime prospectif (nouveaux mois) et transitoire (mois antérieurs et mois à cheval). Pour chaque texte, on a établi : les assujettis, l'objet, le fait générateur, l'échéance, la dépendance au numéro UT, et le rang (décret pour l'annexe III, arrêté pour l'annexe IV, d'après les liens `CREATION`).
3. Contrôle d'éventuelles obligations autonomes portant sur le même objet, par recherche dans l'ensemble du corpus.
4. Contrôle des points écartés par l'index (50-00 D / G/H) sur les textes entiers.
5. Contrôle des bornes : dates techniques LEGI (`2999-01-01`, `2222-02-22`) contre dates normatives.
6. Confrontation des conclusions scellées aux empreintes courantes.

Aucune consultation web n'a été faite. Les pistes publiques déjà épuisées (Légifrance 403 sur l'ordonnance n° 2021-1843 et sur l'arrêté du 4 juillet 2005) n'ont pas été rejouées, conformément aux consignes des dossiers scellés.

## 4. Constats

### 4.1 RT-MENS-01 — Le corps de 50-0 I II proposé contredit 111-0 H 2° proposé (P1, incohérence du projet)

**Texte de 111-0 H 2° proposé** (LEGIARTI000006298858) :
> « Au titre du présent article, aucune déclaration récapitulative mensuelle distincte ni transmission au plus tard le dixième jour du mois n'est exigée. »

et

> « La suppression de la transmission mensuelle s'applique aux mois commençant à compter de l'entrée en vigueur de la présente réforme. »

Les données a à c restent tenues dans la comptabilité matières. Elles ne sont communiquées que sur demande, « pour les périodes nécessaires au contrôle ». Le texte précise : « Des demandes systématiques ne peuvent rétablir la transmission mensuelle supprimée. »

**Texte de 50-0 I II proposé** (LEGIARTI000006300444) :
> « II. – Pour l'application des dispositions du 2° de l'article 111-0 H […], la déclaration mensuelle récapitulant les quantités de produits vitivinicoles comporte les renseignements suivants : […] c. Le numéro d'identification attribué […] dans les conditions fixées à l'article 50-0 H ; […] »

puis

> « Cette dispense ne modifie pas les obligations de comptabilité matières ni les déclarations des mois comportant une opération de fabrication. »

Le motif est dans le même sens : « La comptabilité matières et les déclarations des mois actifs conservent la preuve […] ».

**Qualification.**
- *Mêmes opérateurs.* Le II de 50-0 I n'a pas de champ propre : il vise les assujettis du 2° de 111-0 H, c'est-à-dire les fabricants de vinaigre qui reçoivent et utilisent des produits vitivinicoles. Les utilisateurs relevant de 111-0 G n'ont jamais été soumis à une déclaration mensuelle.
- *Mêmes mois.* La transition de 50-0 I proposé (« formalités accomplies à compter de l'entrée en vigueur ») ne limite pas le II aux mois antérieurs. Il continue donc à décrire, pour les nouveaux mois actifs, une déclaration que 111-0 H supprime.
- *Même objet et même finalité.* La « déclaration mensuelle récapitulant les quantités » est celle du 2° de 111-0 H. Le II n'en fixe que le contenu. Le I de 50-0 I (renseignements de la comptabilité matières) est, lui, une obligation distincte, et il est conservé.
- *Ce n'est donc pas deux obligations distinctes.* Ce n'est pas non plus une simple coordination manquante, car 50-0 I a bien été réécrit. Sa proposition **réaffirme** le maintien des déclarations des mois actifs, sur une prémisse antérieure à la version courante de 111-0 H. Ses notes renvoient d'ailleurs à « Coordonner H 2° pour la dispense des mois sans fabrication ». À l'inverse, les notes de 111-0 H relèvent déjà que le brouillon de 50-0 I « ne suffit donc pas à cette coordination ». C'est une **incohérence introduite par le projet**.

**Effet.** Rang : 111-0 H vient du décret n° 2005-758 ; 50-0 I vient de l'arrêté du 4 juillet 2005 « pour l'application » du 2°. Le juge devrait donc faire prévaloir la suppression. Mais après l'entrée en vigueur, un arrêté publié décrirait encore une déclaration mensuelle des mois actifs, avec un numéro UT et un contenu signé. Cela crée une ambiguïté probable pour les opérateurs et les services : maintien des formulaires, demandes systématiques ou contestation de pénalités. L'effet n'est pas certain : le texte ne subordonne pas l'exonération du 302 D bis II a à cette déclaration. D'où la priorité P1 et non P0. Si le projet devait être adopté par un acte unique de même rang, l'argument hiérarchique s'affaiblirait (voir § 6).

**À préserver.** Le I de 50-0 I, la comptabilité matières quotidienne (enregistrement au plus tard le jour ouvrable suivant), les calculs a à c disponibles au contrôle, la clause sur les déclarations directement exigées par le droit de l'Union, et l'exonération elle-même.

### 4.2 RT-MENS-02 — Transitions désynchronisées (P2, risque juridique)

| Situation (exemple : entrée en vigueur au 1er ou au 15 du mois M) | 111-0 H proposé | 50-0 I proposé | Résultat |
|---|---|---|---|
| Nouveaux mois (à partir de M+1, ou de M si l'entrée en vigueur tombe le 1er) | aucune déclaration | déclaration des mois actifs maintenue | contradiction (RT-MENS-01) |
| Mois à cheval (entrée en vigueur le 15 du mois M) | M a commencé avant : déclaration due le 10 de M+1 « selon les règles antérieures » | formalité accomplie après l'entrée en vigueur : pas de cachet, pas de « néant » | règles antérieures et règles simplifiées se superposent |
| Mois antérieur sans fabrication, échéance après l'entrée en vigueur (M-1 si l'entrée en vigueur tombe le 1er de M) | « néant » dû (règles antérieures) | « néant » non exigé (formalité postérieure) | contradiction |
| Déclaration d'un mois antérieur due avant l'entrée en vigueur et non déposée | reste due | « y compris dans les procédures en cours » : la dispense du néant joue | issue incertaine, sanctions non traitées |
| Contrôle ou rectification d'un mois antérieur | données et conservation maintenues ; rien sur la rectification | droits, créances et recours conservés ; rien sur la rectification | silence |
| Rubrique c (UT) pour un mois antérieur déclaré après l'entrée en vigueur | — | numéro exigé, alors que 111-0 F proposé n'attribue plus de numéro, même aux « demandes en cours » | dépendance UT (renvoi RT-INUT) |

Deux autres points s'ajoutent.
- L'ancre « entrée en vigueur de la (présente) réforme » n'a pas de date. Elle relève d'instruments de rang différent (décret pour l'annexe III, arrêté pour l'annexe IV), alors que 302 D bis proposé vise « la loi qui les prévoit ». Un décalage d'entrée en vigueur entre ces instruments ouvrirait une période intermédiaire.
- Ni 111-0 H ni 50-0 I ne réservent l'application immédiate des dispositions répressives plus douces. D'autres propositions du même ensemble le font, par exemple annexe I 165.

**À préserver.** Les échéances des anciens mois et les déclarations dues. L'absence de renouvellement des dépôts déjà faits. La faveur déjà accordée par 50-0 I : pas de cachet ni de « néant » pour les formalités accomplies après l'entrée en vigueur, y compris pour d'anciens mois. Les contrôles, les rectifications et les créances des périodes antérieures.

### 4.3 RT-MENS-03 — 50-00 D et G/H : point écarté (P2, faux positif)

- 50-00 D proposé conserve un compteur inaccessible et non réinitialisable, ainsi que la règle suivante : « Dès que l'utilisateur valide la saisie […], ces informations ne peuvent plus être annulées ni modifiées ».
- 111-0 G 3° et 111-0 H 3° proposés prévoient : « Pour une tenue informatisée, les conditions de l'article 50-00 D […] s'appliquent sous réserve du présent 3°, qui permet la réutilisation des enregistrements et les corrections traçables », et « Les corrections laissent subsister l'inscription d'origine ainsi que la date et l'identification de leur auteur ».

L'exception est expresse et spéciale, limitée aux comptes de G/H. Une correction traçable conserve l'inscription d'origine : elle se concilie avec l'immutabilité de l'inscription validée. Il n'y a pas d'incompatibilité générale, et l'exception ne doit pas être étendue aux registres vitivinicoles des entrepositaires agréés. Ce constat rejoint, après relecture entière, la qualification scellée de 15 h 05. Reste une question d'interprétation résiduelle : la réutilisation d'un logiciel de gestion sans compteur conforme est-elle couverte par la réserve ? Elle est notée au § 6 sans être érigée en contradiction.

### 4.4 RT-MENS-04 — Réserves documentaires et bornes techniques (P2, réserve documentaire)

- **302 D bis**, base légale des 111-0 E à H. Sa version courante (LEGIARTI000041472187) est en état `ABROGE_DIFF`, avec la borne `2222-02-22`. Le XML porte un lien `ABROGE` vers l'ordonnance n° 2021-1843 du 22 décembre 2021, art. 10 (JORFTEXT000044590225, LEGIARTI000044595100), et des liens `CONCORDANCE` vers le CIBS. La date d'effet de cette abrogation, et donc le maintien au 18 octobre 2026 de la base légale sur laquelle reposent 111-0 H 2° et 50-0 I, **n'est pas établie** dans l'instantané. 302 D bis est par ailleurs `pending` en seconde passe.
- **Bornes.** `2222-02-22` (302 D bis et son chapitre) et `2999-01-01` (G, H, 50-0 I, 50-00 D et dates de signature des liens CODE) sont des bornes techniques de la base LEGI, non des dates normatives. Les bornes `2005-07-06` et `2006-01-01` sont des bornes de version : décret n° 2005-758 et arrêté du 4 juillet 2005 (JO du 6 juillet 2005) ; décret n° 2006-356 et arrêté du 24 mars 2006 (JO du 26 mars 2006, début de version au 1er janvier 2006). Elles ne fondent aucune rétroactivité déduite. **Aucune confusion de cette nature n'apparaît dans les propositions ou motifs courants du périmètre**, et les notes de 302 D bis l'écartent expressément. Le risque est signalé pour la rédaction de la transition : aucune de ces bornes ne doit servir de date d'entrée en vigueur ni de date de fin d'un mois déclaratif.
- **Arrêté du 4 juillet 2005 et modèles** (JORFTEXT000000632265, non obtenu). Seuls les modèles I à III de 50-0 H sont identifiés. Aucun modèle de déclaration mensuelle du vinaigre n'est certifié. Si un tel modèle existe, il doit tomber avec le II pour les nouveaux mois.
- **Droit de l'Union.** Le règlement (CE) n° 1493/1999 cité est ancien. Les règlements (UE) n° 1308/2013, 2018/273 et 2018/274 n'ont pas été consultés. La clause de sauvegarde de 111-0 H 2° (« ne dispense pas d'une déclaration directement exigée par le droit de l'Union ») suffit à ne rien abroger par assimilation.

### 4.5 RT-MENS-05 — Fiche d'impact de 50-0 I (P2, anomalie d'inventaire)

La ligne propriétaire de 50-0 I (`batches/automatic-impots-annexe-4/00013.json`, ligne 9) contient l'effet `vinaigre-declaration-neant-cachet`. Il porte « after » : « Déclaration seulement pour les mois actifs, signature suffisante », et « affected_population » : « Fabricants de vinaigre et utilisateurs soumis à comptabilité matières. »

1. L'état « après » contredit la mesure `vinaigre-fin-declaration-mensuelle` de 111-0 H.
2. Pour les nouveaux mois, la suppression du « néant » et du cachet est absorbée par la suppression de toute la déclaration. La compter à part reviendrait à compter deux fois la même mesure.
3. La population est trop large : le II ne concerne que les fabricants de vinaigre visés au 2° de 111-0 H.

Le gain propre de 50-0 I ne subsiste que pour les déclarations d'anciens mois établies après l'entrée en vigueur.

## 5. Propositions de correction (présentées séparément)

Aucune de ces propositions n'est intégrée ni enregistrée. Elles ne créent aucune formalité de remplacement et conservent la comptabilité quotidienne.

### 5.1 Correction C1 (RT-MENS-01 et RT-MENS-02) : texte complet proposé de l'annexe IV, article 50-0 I

> I. – Pour l'application des dispositions du 2° de l'article 111-0 G et du 1° de l'article 111-0 H de l'annexe III au code général des impôts, la comptabilité matières doit reprendre notamment les renseignements suivants :
>
> a. La nature, le numéro et la date de réception du document d'accompagnement mentionné à l'article 302 M dudit code, du document économique ou des pièces justificatives des entrées ou des fabrications ;
>
> b. La nature et la date de toute autre opération constituant une " entrée " ou une " sortie " selon le 2° de l'article 111-0 G de la même annexe ;
>
> c. L'espèce, la qualité et la nature des produits mentionnés à l'article 302 D bis du code général des impôts et des produits issus de la fabrication.
>
> II. – Pour les mois commençant à compter de la date à laquelle s'applique la suppression de la transmission mensuelle prévue au 2° de l'article 111-0 H de l'annexe III au code général des impôts, aucune déclaration mensuelle récapitulant les quantités de produits vitivinicoles n'est établie ni transmise, que le mois comporte ou non une opération de fabrication. Aucun modèle de cette déclaration ni aucune déclaration portant la mention « néant » n'est exigé pour ces mois. Les renseignements du I continuent d'être portés dans la comptabilité matières ; les données prévues au 2° de l'article 111-0 H ne sont communiquées que dans les conditions qu'il prévoit.
>
> III. – Pour le mois en cours à la date mentionnée au II et pour les mois antérieurs, la déclaration mensuelle prévue au 2° de l'article 111-0 H de l'annexe III au code général des impôts dans sa rédaction antérieure reste due et comporte les renseignements suivants :
>
> a. La campagne vitivinicole au cours de laquelle sont mis en oeuvre les produits vitivinicoles ;
>
> b. Le nom ou la raison sociale du fabricant de vinaigre ;
>
> c. Le cas échéant, le numéro d'identification attribué par le service des douanes et droits indirects avant cette date ;
>
> d. L'adresse du lieu d'utilisation des produits vitivinicoles ;
>
> e. Le mois au titre duquel la déclaration est établie ;
>
> f. Les date et lieu d'établissement de la déclaration ;
>
> g. La qualité et la signature du déclarant.
>
> Lorsque la déclaration relative à l'un de ces mois est établie à compter de la date mentionnée au II, aucun cachet de l'entreprise n'est exigé et, à défaut d'opération de fabrication au cours de ce mois, aucune déclaration portant la mention « néant » n'est exigée. Les déclarations déjà déposées ne sont pas renouvelées. Les déclarations des mois comportant une opération de fabrication qui étaient dues et n'ont pas été déposées restent dues. Le contrôle et la rectification des déclarations de ces mois, ainsi que les droits, exonérations, créances et recours qui s'y rapportent, demeurent régis par les règles applicables à ces mois, sous réserve de l'application immédiate des dispositions répressives plus douces.

**Justification.**
- Le I est repris à l'identique de la proposition et de la source.
- Le II est rattaché au **même déclencheur** que 111-0 H 2°, et non à une date propre de l'arrêté. Le décalage d'entrée en vigueur entre décret et arrêté est ainsi neutralisé.
- Le III conserve les échéances anciennes et toutes les faveurs du brouillon courant : pas de cachet, pas de « néant » pour les formalités postérieures, pas de nouveau dépôt.
- La rubrique c devient « le cas échéant ». La correction ne présuppose donc ni le maintien ni la suppression du numéro, et ne double pas RT-INUT.
- Aucune nouvelle déclaration, aucun registre, aucune attestation.

**Dépendances.**
- Correction C2 ci-dessous, qui fixe l'ancre et le mois à cheval.
- RT-INUT : le traitement de 50-0 H et des modèles de l'arrêté du 4 juillet 2005 pour le numéro UT ; le c du III devient sans objet si l'on retient que les numéros attribués valent pour les anciennes périodes.
- Concordance CIBS des renvois 302 M et 302 D bis du I, non tranchée.

### 5.2 Correction C2 (RT-MENS-02) : passage complet proposé, dernier alinéa de l'annexe III, article 111-0 H

Le 1°, le 2° (y compris a à c) et le 3° de la proposition courante restent inchangés. Le dernier alinéa est remplacé par :

> La suppression de la transmission mensuelle prévue au 2° s'applique aux mois commençant à compter de l'entrée en vigueur de la présente réforme. Le mois en cours à cette date et les mois antérieurs restent soumis aux règles antérieures : leurs déclarations, y compris celles qui étaient dues et n'ont pas été déposées, restent dues dans les conditions prévues au III de l'article 50-0 I de l'annexe IV au code général des impôts, et leur contrôle comme leur rectification demeurent régis par ces règles, sous réserve de l'application immédiate des dispositions répressives plus douces. Les modalités simplifiées de tenue des comptes s'appliquent à compter de cette entrée en vigueur, sans suppression des données antérieures ni de leurs obligations de conservation.

**Justification.** Le choix du projet est conservé : seuls les mois commençant après l'entrée en vigueur échappent à la déclaration, et le mois à cheval reste déclaré. Le texte traite expressément les déclarations dues et non déposées, les rectifications et la loi répressive plus douce. Il renvoie aux modalités allégées de 50-0 I III, sans en créer de nouvelles.

**Dépendance.** La date d'entrée en vigueur de la réforme et le rang de l'instrument (§ 6). C2 doit être adoptée avec C1 et ne doit pas l'être seule.

### 5.3 Correction C3 (RT-MENS-05) : métadonnées d'impact de 50-0 I (hors texte normatif)

Les champs de l'effet `vinaigre-declaration-neant-cachet` seraient réécrits ainsi :
- « after » : « Nouveaux mois : aucune déclaration mensuelle (mesure de 111-0 H). Mois antérieurs déclarés après l'entrée en vigueur : signature sans cachet, pas de déclaration néant. »
- « affected_population » : « Fabricants de vinaigre visés au 2° de l'article 111-0 H. »
- « conditions_and_transition » : un renvoi au III.

Aucun gain distinct ne doit être compté pour les nouveaux mois.

### 5.4 Autres options écartées ou subsidiaires

- *Abroger tout le II de 50-0 I sans III.* Plus simple, mais cela priverait de contenu réglementaire les déclarations des anciens mois que 111-0 H maintient. Option écartée.
- *Supprimer aussi la déclaration du mois à cheval* (déclarations dont l'échéance tombe après l'entrée en vigueur). Plus libérale, elle reste compatible avec l'objectif. Elle suppose de modifier aussi 111-0 H, d'accepter une période sans agrégat déclaré, et de vérifier les éventuelles exigences européennes. C'est une option politique à arbitrer.
- *Laisser jouer la hiérarchie des normes sans corriger.* C'est insuffisant : le texte contradictoire et les formulaires subsisteraient.

## 6. Incertitudes restantes

- Date et instrument d'entrée en vigueur de la « réforme ». La répartition entre loi, décret et arrêté conditionne l'argument hiérarchique de RT-MENS-01 et la synchronisation de RT-MENS-02. Elle pose aussi une question de compétence : un arrêté d'application modifié par un autre véhicule que celui du décret.
- Base légale résiduelle de 302 D bis (abrogation différée par l'ordonnance n° 2021-1843, art. 10) et transfert éventuel vers le CIBS du régime d'exonération du vinaigre et de ses modalités : non établis.
- Existence d'un modèle de déclaration mensuelle du vinaigre dans l'arrêté du 4 juillet 2005 ou dans un autre acte : non vérifiée.
- Obligations européennes vitivinicoles autonomes, déclarations ou registres, pesant sur les vinaigreries : non vérifiées.
- Régime des sanctions des contributions indirectes applicables au défaut de déclaration, et portée exacte de la rétroactivité in mitius pour une obligation déclarative technique : non lus ni tranchés.
- Interprétation de la réserve de G/H 3° : la réutilisation d'un système de gestion dispense-t-elle des exigences de compteur de 50-00 D, ou seulement de l'interdiction de corriger ? Interprétation ouverte, non qualifiée de contradiction.
- La seconde passe continue, et 302 D bis y est `pending`. Toute modification future de 111-0 H, de 50-0 I ou de 302 D bis rend ces conclusions caduques.

## 7. Éléments non examinés

- Les déclarations récapitulatives et comptabilités des entrepositaires agréés (annexe II 286 I/J ; annexe IV 50-00 A, B, C, E, F, G ; 50-0 J à O). Elles portent sur d'autres assujettis ; seules leur existence et leur indépendance apparente ont été constatées par recherche.
- Les articles de sanctions du CGI (contributions indirectes), les textes européens, le CIBS et les arrêtés de 2005 et 2006 dans leur intégralité.
- Les grosses copies d'entrée scellées n'ont pas été lues ligne à ligne. Seule leur égalité de champs avec l'instantané a été vérifiée.
- Le circuit IN/UT lui-même (302 D bis III, 111-0 E/F, 50-0 G/H, 289 15°) relève de RT-INUT.

Une revue IA ne vaut pas validation par un juriste.
