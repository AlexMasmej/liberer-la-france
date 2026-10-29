# A1DOSSIER : annexe I du CGI, articles 165, 185 et 186 (dénaturation des alcools)

Red-team juridique indépendante, troisième passe. Rédigé le 26 octobre 2026 sur l'instantané `snapshots/20261026T230545Z` (corpus LEGI arrêté au 18 octobre 2026). C'est une revue par IA, pas une validation par un juriste. Les conclusions sont provisoires : la seconde passe continue en production et les propositions peuvent encore changer. L'article 302 D bis, en particulier, est encore au statut d'inventaire `pending`.

## 1. Résumé

| ID | Priorité | Nature | Statut | Objet |
|---|---|---|---|---|
| RT-A1-01 | P1 | incohérence du projet | confirmé | 185 et 186 proposés dépendent encore de 165, que le projet abroge (3 occurrences, 2 articles, 1 cible) |
| RT-A1-02 | P2 | incohérence du projet | confirmé | Le corps et le motif de 165 proposé supposent la déclaration du III de 302 D bis, que le projet supprime |
| RT-A1-03 | P2 | coordination manquante | à confirmer | CGI 508 (exigence d'un « établissement désigné à l'administration ») : article hors inventaire et non coordonné avec la suppression du dossier 165 |
| RT-A1-04 | P2 | risque juridique | à confirmer | Article 27 de la directive 92/83/CEE : maintenir l'autorisation du procédé spécial. Le texte en vigueur après la directive 2020/1151 n'a pas été obtenu |
| RT-A1-05 | P2 | réserve documentaire | à confirmer | 302 D bis en ABROGE_DIFF (ordonnance 2021-1843, art. 10) et CIBS L313-7/L313-8 en vigueur : fondement législatif de 165, 186 et 289 2° non stabilisé |
| RT-A1-06 | P2 | simple alerte | confirmé | 192 : le « retrait de l'autorisation administrative » ne vise plus, pour l'avenir, que les autorisations subsistantes |
| RT-A1-07 | P2 | alerte écartée | faux positif | 169, 170, 184, 189 : pas de dépendance au dossier 165 |

Bilan : 1 P1 et 6 P2. Par statut : 3 confirmés, 3 à confirmer, 1 faux positif.

Conclusion principale : l'index a raison. Les trois occurrences P1 visent toujours la version courante. Les empreintes des propositions 165, 185 et 186 sont identiques à celles de la preuve scellée de 13 h 05. Il s'agit d'**une seule** contradiction, et non de trois gains distincts. Je propose une correction couplée des articles 165, 185 et 186 (§ 5) :
- elle supprime le dossier du procédé général pour tous les industriels, y compris ceux de 185 ;
- elle rend autonome, dans 186, la demande d'autorisation du procédé spécial ;
- elle ne crée aucune pièce nouvelle et conserve les autorisations déjà délivrées.

## 2. Périmètre réellement lu

Toutes les lectures ont été faites par `tools/cite.py`, en entier : source, NOTA, bornes, proposition, motif, notes de revue et lot propriétaire. Les sorties sont dans `evidence/cited/20261026T230545Z/`.

**Annexe I (LEGITEXT000006069568), section « Chapitre Ier, Section IV, I : Alcools dénaturés »**, identifiée par les `TITRE_TM` des XML :

- 1° Procédé général. Textes en vigueur avec leur proposition :
  - 165 : LEGIARTI000032881253 (2016-07-10 → 2999-01-01, rewrite_draft) ;
  - 167 : LEGIARTI000032881249 ;
  - 168 : LEGIARTI000006293577 ;
  - 169 : LEGIARTI000006293598 ;
  - 170 : LEGIARTI000032881236 (retained_unchanged) ;
  - 173 : LEGIARTI000006293585 (retained) ;
  - 175 : LEGIARTI000006293588 (retained) ;
  - 179 : LEGIARTI000006293601 (retained) ;
  - 180 : LEGIARTI000032881231 ;
  - 181 : LEGIARTI000006293591 (abrogation proposée) ;
  - 182 : LEGIARTI000006293604 (retained) ;
  - 184 : LEGIARTI000006293594.
- 2° Procédé spécial :
  - 185 : LEGIARTI000006293344 (2001-03-31 → 2999-01-01, rewrite_draft) ;
  - 186 : LEGIARTI000032881225 (2016-07-10 → 2999-01-01, rewrite_draft) ;
  - 188 : LEGIARTI000032881220 ;
  - 189 : LEGIARTI000032881214 (retained).
- 3° Alcool sans dénaturation : 190 (LEGIARTI000032881246, retained) et 191 (LEGIARTI000006293619, retained).
- 4° Dispositions diverses : 192 (LEGIARTI000032881242).
- Versions historiques imprimées par cite.py pour les mêmes numéros :
  - 165 : 1979 et 1993 ;
  - 185 : 1979, 1988 et 1993 ;
  - 186 : 1979, 1989 et 1998 ;
  - 166, 174 et 187, abrogés en 2001 et sans version courante ;
  - versions anciennes de 167 à 192.
- Les corps historiques de 165, 185, 186, 166, 174 et 187 ont été lus en entier. Pour les autres, je me suis limité aux en-têtes, sans en tirer de constat.

**CGI (LEGITEXT000006069577)**, versions vérifiées au 18 octobre 2026 :

- 302 D bis : toutes les versions. La version courante est LEGIARTI000041472187 (2021-01-01 → 2222-02-22, **ABROGE_DIFF**, inventaire `pending`). Il existe aussi deux versions MODIFIE_MORT_NE (2023 et 2026).
- 508 : toutes les versions. La version courante est LEGIARTI000006309958 (ABROGE_DIFF, **hors inventaire, sans proposition**).
- 458 : LEGIARTI000041472229 (ABROGE_DIFF, hors inventaire).
- 302 M : LEGIARTI000042623631 (ABROGE_DIFF).
- 302 B : LEGIARTI000041535200 (VIGUEUR à compter du 2026-01-01).
- Les bornes de 509 à 513, de 401 à 407, de 435 et de 631 ont été listées par requête en lecture seule. Ces articles sont tous abrogés ou transférés au 18 octobre 2026 : il n'y a pas de série « 401 et suivants » en vigueur.

**Annexe II** : 289, LEGIARTI000054363092 (2026-07-01 → 2999-01-01), lu en entier, en particulier ses 2°, 15° et dernier alinéa. Le 15° relève de l'agent INUT.

**Preuves scellées lues** :

- `alcohol-denaturation-coherence-readonly-20261026T1305Z/`, en entier : REPORT, CONTROL, findings P1 et comparaison des gardes, qualification sémantique, comparaison officielle, catalogue, contrôles, refus, manifeste. Les deux gros fichiers d'entrées (`whole-current-and-historical-inputs-two-RO.json`, `whole-file-input-stability.json`) ont seulement été inspectés dans leur structure. Leur contenu a été relu directement depuis l'instantané par cite.py.
- `cibs-alcohol-public-followup-20261026T1707Z/` : REPORT, qualification, lignes affichées de L313-7 et L313-8.
- REPORT de `alcohol-2005-*`, `alcohol-2006-*` et `cibs-2021-primary-pistes-followup-20261026T1808Z`.

**Orientations lues** dans `policy-coordinations.json` :

- `formalites_accises_et_cidre`, en entier. Elle ne vise pas expressément la dénaturation ; elle donne la méthode (pas de visa ni de registre de remplacement, numéro d'accise existant, contraintes européennes propres).
- `editorial_direction_2026_10_19`, `cuts_and_reliefs_2026_10_19`, `preserved_benefits_2026_10_19` et `scope`.
- Lignes 14 à 16 de `notes-contradictions/INDEX.md`.

## 3. Méthode

1. J'ai identifié la section par les XML. J'ai recensé toutes les versions de 160 à 193 dans `articles`, puis lu par cite.py chaque version en vigueur et ses voisines.
2. J'ai confronté les empreintes courantes aux gardes scellées. Les propositions sont identiques :
   - 165 : `6d4be25d…` ;
   - 185 : `5d4a6c19…` ;
   - 186 : `eef280bd…`.
   Les sources sont identiques elles aussi : `04708941…`, `d5c8b040…`, `72ac8ce0…`. Les constats scellés s'appliquent donc à la version courante, mais je les ai requalifiés sur les corps entiers.
3. J'ai recherché les autres renvois à 165, 185 et 186 dans les propositions, motifs et notes des cinq recueils fiscaux. Seuls 170, 185, 186 et 189 (annexe I) et 289 2° (annexe II) sont concernés.
4. J'ai lu les liens LEGI (`LIENS`) de 302 D bis, 165, 185 et 186 : abrogation par l'ordonnance 2021-1843, art. 10, et concordances CIBS.
5. Sources européennes : EUR-Lex a renvoyé un HTTP 202 avec un corps vide (défi d'accès) le 2026-10-26 vers 23 h 19 UTC. Je ne l'ai pas contourné. J'ai lu les copies officielles des Archives nationales britanniques (legislation.gov.uk), figées au 31 décembre 2020, et la page de la Commission. Leurs limites sont exposées au § 6.

## 4. Constats

### RT-A1-01 (P1, incohérence du projet, confirmé) : 185 et 186 dépendent encore du dossier 165 abrogé

**Ce que disent les textes courants**

- Le 165 proposé abroge l'article entier : « Le présent article est abrogé à compter de l'entrée en vigueur de la loi. La demande spéciale de dénaturation, la production du plan en double exemplaire et la déclaration préalable des modifications avec plan rectificatif ne sont plus exigées sur son fondement, y compris pour les demandes en cours. »
- Le 185 proposé maintient « Les dispositions des articles 165 à 170 et 173 à 175 sont applicables aux industriels qui se proposent de dénaturer des alcools par un procédé différent du procédé général » (occurrence 1). Il ajoute « Pour l'application de l'article 165 à ces industriels, le plan joint à la demande est fourni en un seul exemplaire » (occurrence 2). Son motif affirme que « L'autorisation, le contenu du plan, les modifications […] restent applicables ».
- Le 186 proposé maintient « Lesdits industriels mentionnent dans la demande d'autorisation prévue à l'article 165 » (occurrence 3).

**Analyse : trois éléments à distinguer**

1. **Le dossier du procédé général** (165) : demande, destination, plan en double et modifications avec plan rectificatif. Le projet le supprime. Ce choix est conforme aux orientations, qui imposent de supprimer les formalités sans fonction démontrée. Je ne le remets pas en cause.
2. **L'autorisation du procédé spécial** :
   - elle repose sur 302 D bis I b (« autorisé par l'administration ») ;
   - sur CIBS L313-8 2° (« dénaturé conformément à l'un des procédés autorisés, dans des conditions déterminées par décret, pour l'utilisation à laquelle il est employé », version affichée du 01/01/2022 au 01/01/2027) ;
   - sur la décision du directeur interrégional après avis du laboratoire (dernier alinéa de 186) ;
   - et sur la compétence de 289 2°.
   Cette autorisation doit être conservée. Aucune proposition ne la supprime, mais sa **procédure de demande** n'existe plus que par renvoi à 165.
3. **Les titres et règles autonomes** : séparation et dérogations de 167, cuves de 168, prescriptions de 169, conditions des alcools de 170, prélèvements de 173, régénération favorable de 175, dispense de lieu de 188, libre circulation de 189, franchise de 190, et agréments d'accise éventuels. Ils ne dépendent pas du dossier 165.

**Conséquences probables à l'entrée en vigueur**

- Un renvoi de 185 « applicable » à un article abrogé peut se lire de deux façons :
  - comme un renvoi statique, qui maintient pour le procédé spécial la demande, le plan en un exemplaire et la déclaration des modifications ;
  - comme un renvoi devenu sans objet, ce qui ferait disparaître la demande du procédé spécial.
- Les deux lectures sont plausibles et le texte n'en exclut aucune.
- La première crée une asymétrie inexpliquée : le procédé spécial garderait un dossier que le procédé général perd. Elle maintient aussi par renvoi une formalité que le projet déclare supprimée.
- La seconde laisse 186 sans base de demande, alors que l'autorisation reste requise par la loi. Le demandeur ne saurait plus ce qu'il doit déposer, et le directeur ne saurait plus sur quoi statuer.
- La transition du 165 proposé (« y compris pour les demandes en cours ») pourrait aussi faire tomber les demandes de procédé spécial en cours, déposées « en application de 165 » via 185.
- Les métadonnées de 185 (« alcool-denature-plan-exemplaire-unique ») comptent un gain distinct qui est absorbé si le plan disparaît. Il faut éviter un double comptage.

**Priorité**

P1 : la contradiction a un effet probable sur une autorisation qui conditionne une exonération, mais pas d'effet certain dès l'entrée en vigueur. L'autorisation elle-même subsiste par 302 D bis I b, 289 2° et 186, dernier alinéa.

**Correction** : couplée sur 165, 185 et 186 (§ 5.1 à 5.3).

### RT-A1-02 (P2, incohérence du projet, confirmé) : 165 présuppose une déclaration que le projet retire

- Le corps du 165 proposé dit : « La déclaration prévue au III de l'article 302 D bis du code général des impôts demeure distincte ; aucun second dépôt n'est requis au titre du présent article. »
- Son motif dit : « L'article 302 D bis lu dans le corpus impose déjà la déclaration des bénéficiaires de l'exonération ».
- Or le 302 D bis III proposé prévoit : « ne sont subordonnés à aucune déclaration préalable de profession auprès de l'administration ».
- La phrase de 165 renvoie donc à une déclaration qui n'existe plus dans le projet. Une norme réglementaire ne peut pas recréer une déclaration législative supprimée, d'où un effet limité. Mais la formule « demeure distincte » se lit comme un maintien, et le motif perd sa prémisse.

L'abrogation de 165 reste justifiée par elle-même : pas de fonction démontrée, preuve ordinaire de destination. Le circuit de la déclaration de profession et du numéro IN/UT relève de l'agent **INUT**. Je ne corrige ici que la phrase de 165 (§ 5.1), en reprenant les termes du 302 D bis III proposé. Si INUT modifie ce III, la phrase devra suivre.

### RT-A1-03 (P2, coordination manquante, à confirmer) : CGI 508 et l'« établissement désigné à l'administration »

**Le texte**

- Le CGI 508 (LEGIARTI000006309958, ABROGE_DIFF) dispose : « Pour bénéficier de l'exonération prévue aux a et b du I de l'article 302 D bis, les alcools doivent être dénaturés, soit dans l'établissement même où ils ont été produits, soit dans tout autre établissement désigné à l'administration. »
- Sa NOTA rattache la prise d'effet de l'abrogation à « l'intervention du décret mentionné à l'article L. 311-39 du code des impositions sur les biens et services et pris pour l'application de l'article L. 311-40 du même code » (ordonnance 2021-1843, art. 38, 5°).
- 508 est absent de `drafts`, de l'inventaire `radical-review-20261019.json`, de `registered-batches.json` et de `manifest.json`. Une requête montre que 30 articles du CGI en ABROGE_DIFF sur 375 n'ont pas de proposition, dont 508, 458 et 302 M.

**Le risque**

- Le projet supprime la demande de 165 et affirme qu'« aucun second dépôt n'est requis ». Pourtant 508, s'il s'applique encore, maintient une désignation de l'établissement de dénaturation comme **condition de l'exonération**, sans procédure.
- Un opérateur qui se fierait à 165 risquerait de perdre l'exonération pour défaut de désignation.

**Pourquoi « à confirmer »**

L'applicabilité résiduelle de 508 au 18 octobre 2026 dépend de deux points que je n'ai pas établis :
- l'intervention du décret mentionné ;
- l'articulation avec CIBS L313-7 et L313-8, en vigueur depuis le 1er janvier 2022 selon l'affichage historique.

Je signale aussi l'anomalie d'inventaire, sans la compter comme un second constat.

**Correction** : § 5.4, sous réserve.

### RT-A1-04 (P2, risque juridique européen, à confirmer) : ce que le droit de l'Union impose de garder

Texte de l'article 27 de la directive 92/83/CEE dans sa version au 31 décembre 2020 (copie legislation.gov.uk) :

- Le §1 (chapeau) impose d'exonérer « under conditions which they shall lay down for the purpose of ensuring the correct and straightforward application of such exemptions and of preventing any evasion, avoidance or abuse ».
- Le a vise l'alcool « completely denatured in accordance with the requirements of any Member State, such requirements having been duly notified and accepted » selon les §3 et §4.
- Le b vise l'alcool « both denatured in accordance with the requirements of any Member State and used for the manufacture of any product not for human consumption ».
- Le §5 permet de refuser ou de retirer l'exonération en cas d'abus.

Le règlement (CE) 3199/93, dont l'annexe a été substituée par le règlement d'exécution (UE) 2018/1880, fixe pour la France le procédé commun : « 1,0 litre isopropyl alcohol, 1,0 litre methyl ethyl ketone, 1,0 gram denatonium benzoate » par hectolitre d'éthanol absolu.

Conséquences :

- **Rien n'impose** un dossier préalable propre à chaque opérateur pour l'alcool totalement dénaturé : le procédé est fixé au niveau de l'Union. La suppression de 165 est compatible avec ces textes, sous réserve du texte postérieur à 2020.
- En revanche, pour l'alcool partiellement dénaturé (b), l'exonération suppose des « requirements » nationaux. La page de la Commission indique : « Member States authorise national processes for "partial denaturation" ».
- Supprimer l'autorisation du procédé spécial, ou la laisser sans procédure, exposerait l'exonération du b à un défaut de prescriptions nationales. Les conditions anti-abus (167 à 170, 173, 175, 188 à 191) et le pouvoir de retrait (192, autorisation de 186) doivent rester.

Ce constat confirme l'orientation de la correction : garder 186 et ne pas recréer 165.

Réserves :
- Le texte modifié par la directive (UE) 2020/1151 (CELEX 32020L1151), applicable à partir de 2022, n'a pas été obtenu.
- Les éventuels actes d'exécution postérieurs au 31 décembre 2020 sur la reconnaissance des dénaturants n'ont pas été obtenus.
- Le « règlement d'exécution (UE) 2017/2263 » cité dans la commande **n'a pas pu être vérifié** : legislation.gov.uk renvoie une erreur 404 et EUR-Lex n'est pas accessible. Les actes de 2017 effectivement identifiés sont le règlement d'exécution (UE) 2017/1112 (abrogation de 2016/1867) et le règlement d'exécution (UE) 2017/2236 du 5 décembre 2017, qui modifie 3199/93. Je n'affirme aucune équivalence avec la référence citée.

### RT-A1-05 (P2, réserve documentaire, à confirmer) : quel fondement législatif au 18 octobre 2026 ?

- Le 302 D bis (LEGIARTI000041472187) porte l'état ABROGE_DIFF et la borne technique 2222-02-22. Le lien `ABROGE` vise l'ordonnance 2021-1843, art. 10. Ses liens `CONCORDANCE` visent CIBS L313-7 à L313-14 et L314-9 à L314-12.
- CIBS L313-7 et L313-8 sont affichés « en vigueur du 01/01/2022 au 01/01/2027 ». Il s'agit d'une vue historique du 18 mars 2026, et non de la version du 18 octobre 2026. Ma tentative directe du 2026-10-26 sur LEGIARTI000044603563 a reçu un HTTP 403.
- Le 289 2° (version du 2026-07-01) renvoie toujours à « b du I de l'article 302 D bis ».
- Les deux bases coexistent donc dans les textes. La borne 2222 n'est pas une date.
- La correction de 186 proposée ne cite volontairement aucune base législative, comme la source. Elle reste ainsi opérante que l'autorisation relève du 302 D bis I b ou du CIBS L313-8 2°. Aucune équivalence n'est affirmée.
- La concordance d'ensemble relève du dossier CIBS.

### RT-A1-06 (P2, simple alerte, confirmé) : 192 et l'« autorisation administrative »

Le 192 proposé maintient l'expédition du stock « en cas de cessation de leur industrie ou de retrait de l'autorisation administrative ». Après l'abrogation de 165, les dénaturateurs par le procédé général ne détiennent plus d'autorisation nouvelle. Le déclencheur « retrait » ne vise plus que :
- les autorisations du procédé spécial (186) ;
- les franchises de 190 ;
- les autorisations déjà délivrées, qui sont conservées.

Ce n'est pas une contradiction : le déclencheur se réduit, ce qui est favorable, et la cessation reste visée. Aucune correction n'est nécessaire. Option de clarification : « retrait de l'autorisation administrative dont ils sont titulaires ».

### RT-A1-07 (alerte écartée, faux positif) : autres renvois apparents

- **170** (retained) : la détermination des conditions des alcools présentés est une compétence technique, sans dépôt. Sa note précise que « ce maintien ne rétablit pas le dossier supprimé à 165 ».
- **169** : il vise le procédé général par catégorie, sans renvoi à la demande.
- **184** : l'information préalable de l'utilisateur qui reçoit de l'alcool dénaturé et procède à une récupération ou une régénération est un texte autonome, propre à un autre acteur, déjà réduit. Ce n'est pas une dépendance au dossier 165. L'asymétrie avec le dénaturateur qui régénère sous 175 sans informer est seulement notée.
- **189** : sa note vise 188, pas 165.

## 5. Propositions de correction (présentées séparément)

Principes appliqués :
- aucun dossier général rétabli ;
- autorisation spéciale conservée ;
- aucune pièce, déclaration, numéro ni registre de remplacement ;
- preuve ordinaire de destination ;
- autorisations, avantages et dossiers déjà délivrés conservés ;
- aucune date de réforme inventée : la date reste « l'entrée en vigueur de la loi », comme dans les propositions courantes.

### 5.1 Annexe I, article 165 (LEGIARTI000032881253) : texte proposé entier

> Le présent article est abrogé à compter de l'entrée en vigueur de la loi. La demande spéciale de dénaturation, la production du plan en double exemplaire et la déclaration préalable des modifications avec plan rectificatif ne sont plus exigées sur son fondement, ni sur celui de l'article 185 qui le rendait applicable aux industriels mettant en œuvre un procédé spécial, y compris pour les demandes en cours.
>
> Cette abrogation ne supprime ni l'exonération des alcools totalement dénaturés ni les conditions du procédé de dénaturation admis par le droit de l'Union. Elle ne supprime pas l'autorisation du procédé spécial de dénaturation, dont la demande demeure régie par l'article 186. Aucune déclaration, demande ou pièce de remplacement n'est exigée au titre du présent article ; le respect des conditions de l'exonération est établi, lors des contrôles légalement prévus, par les pièces ordinaires d'achat, de fabrication, de circulation ou d'utilisation et par les données légalement disponibles.
>
> Les décisions et avantages antérieurement acquis sont conservés. Les plans déjà fournis n'ont pas à être mis à jour. Les demandes en cours ne sont pas poursuivies en tant qu'elles portent sur le seul dossier supprimé ; celles qui tendent à l'autorisation d'un procédé spécial sont instruites conformément à l'article 186, au vu des pièces déjà fournies et sans nouveau dépôt. Les opérations futures satisfaisant aux conditions de fond de l'exonération continuent d'en bénéficier. Les contrôles des opérations, les règles de sécurité et les droits et recours relatifs aux périodes antérieures demeurent applicables, sous réserve de la loi répressive plus douce.

Justification :
- La phrase sur la « déclaration prévue au III de l'article 302 D bis » est remplacée par la formule de preuve ordinaire du 302 D bis III proposé (RT-A1-02).
- La transition protège les demandes de procédé spécial en cours (RT-A1-01).
- Le motif devrait dire : « Abrogation du dossier spécial : demande, destination détaillée, plan double et mises à jour préalables, sans fonction de contrôle démontrée ; la preuve de destination repose sur les pièces ordinaires. L'autorisation du procédé spécial subsiste (186). »
- Les métadonnées d'effet doivent viser aussi les industriels de 185.

Dépendances : 302 D bis III (agent INUT) ; 185 et 186 ci-dessous.

### 5.2 Annexe I, article 185 (LEGIARTI000006293344) : texte proposé entier

> Les dispositions des articles 167 à 170 et 173 à 175 sont applicables aux industriels qui se proposent de dénaturer des alcools par un procédé différent du procédé général, ou de fabriquer des produits à base d'alcool ainsi dénaturé.
>
> Aucune demande, aucun plan de l'établissement ni aucune déclaration préalable des modifications avec plan rectificatif ne peut être exigé de ces industriels sur le fondement de l'article 165, abrogé, ou du présent article. Leur demande d'autorisation du procédé spécial est régie par l'article 186.
>
> Ces dispositions s'appliquent à compter de l'entrée en vigueur de la loi, y compris aux demandes en cours, sans nouveau dépôt des pièces déjà fournies ni modification des délais applicables. Les plans déjà fournis n'ont pas à être mis à jour sur ce fondement. Les autorisations délivrées avant cette date demeurent valables dans leurs termes ; seules cessent de produire effet leurs prescriptions imposant la production ou la mise à jour d'un plan au titre de l'article 165. Les contrôles, droits et recours relatifs aux opérations antérieures demeurent régis par les dispositions alors applicables.

Justification :
- 165 est retiré de la plage de renvoi. Les renvois favorables et techniques sont conservés en entier : dérogations de 167, cuves de 168, prescriptions de 169, conditions de 170, prélèvements de 173 et régénération de 175. Supprimer tout le bloc fermerait 167 et 175, ce que le motif courant redoute à juste titre.
- La suppression du plan pour le procédé spécial aligne ce régime sur celui du procédé général. Une formalité que le projet juge inutile pour le procédé général n'est pas recréée ici sur un autre fondement.
- Le gain « plan en un exemplaire » est remplacé par « plan supprimé ». Il ne faut pas compter deux mesures.

Autre option (si le propriétaire veut garder un plan pour le procédé spécial) : rédiger dans 185 une obligation autonome de plan en un exemplaire. Cette option n'est pas retenue : elle rétablirait, sur un nouveau fondement, une partie du dossier supprimé, ce qui revient à une formalité de remplacement, et le motif courant ne démontre pas l'utilité propre du plan pour le procédé spécial.

### 5.3 Annexe I, article 186 (LEGIARTI000032881225) : texte proposé entier

> Les industriels mentionnés à l'article 185 adressent au directeur interrégional des douanes et droits indirects une demande d'autorisation du procédé spécial de dénaturation. Cette demande mentionne :
>
> 1° Le procédé de dénaturation proposé et l'utilisation à laquelle l'alcool ainsi dénaturé est destiné ;
>
> 2° Supprimé.
>
> Le directeur interrégional des douanes et droits indirects statue après avis du service commun des laboratoires.
>
> Aucune autre pièce, notamment aucun plan de l'établissement ni aucune estimation de la quantité annuelle d'alcool, ne peut être exigée sur le fondement du présent article.
>
> À compter de l'entrée en vigueur de la loi, ces dispositions s'appliquent aux demandes nouvelles et aux demandes en cours ; ces dernières, y compris lorsqu'elles ont été présentées en application de l'article 165, sont instruites au vu des pièces déjà fournies, sans nouveau dépôt. Les autorisations déjà délivrées demeurent valables dans leurs termes et les données déjà fournies n'ont pas à être renouvelées sur ce fondement.

Justification :
- La demande d'autorisation devient autonome, sans renvoi à 165.
- Le 2° supprimé, le dernier alinéa (décision après avis du laboratoire) et la conservation des autorisations sont repris du projet courant.
- La mention de **l'utilisation** n'est pas une pièce nouvelle. C'est le reliquat réduit de l'indication de la « nature des produits qui seront fabriqués », aujourd'hui exigée via 185 et 165. Elle est nécessaire pour que le laboratoire apprécie un procédé partiel, autorisé « pour l'utilisation à laquelle il est employé » (CIBS L313-8 2°, version historique affichée) et « en vue de la fabrication de produits qui ne sont pas destinés à la consommation humaine » (302 D bis I b).
- Le texte ne cite aucune base législative (RT-A1-05).

Autres options :
- (a) se limiter à « Le procédé de dénaturation proposé », si le propriétaire estime que la description du procédé couvre l'usage ;
- (b) ajouter une mesure favorable : « Lorsque le procédé est déjà autorisé pour l'usage considéré, aucune nouvelle demande n'est exigée de l'industriel qui fabrique des produits à base d'alcool ainsi dénaturé ». C'est une coupe supplémentaire, à vérifier au regard de l'article 27, §1, b de la directive.

Dépendances : 289 2° (compétence, inchangé) et 192 (retrait de l'autorisation).

### 5.4 CGI, article 508 (LEGIARTI000006309958, hors inventaire) : texte proposé entier, sous réserve de RT-A1-03 et RT-A1-05

> Pour bénéficier de l'exonération prévue aux a et b du I de l'article 302 D bis, les alcools doivent être dénaturés, soit dans l'établissement même où ils ont été produits, soit dans tout autre établissement connu de l'administration. Cette dernière condition est remplie lorsque l'établissement de dénaturation ressort des pièces ordinaires de circulation ou de comptabilité, de l'autorisation du procédé spécial ou d'un agrément ou statut en matière d'accise dont l'opérateur est déjà titulaire ; elle n'emporte aucune demande, déclaration, plan ni autorisation préalable propre.
>
> Ces dispositions s'appliquent aux dénaturations effectuées à compter de l'entrée en vigueur de la loi, tant que le présent article demeure applicable. Les désignations déjà effectuées restent valables. Les exonérations, droits et contrôles relatifs aux opérations antérieures demeurent régis par les dispositions alors applicables.

Justification :
- La fonction de localisation est conservée pour le contrôle, sans formalité.
- La condition de l'avantage est sécurisée, pour qu'il ne se perde pas faute d'une démarche que 165 dit supprimée.
- Préalable : inscrire 508 à l'inventaire et vérifier sa portée résiduelle au regard de l'ordonnance 2021-1843 (art. 38, 5°) et du CIBS. Si l'abrogation a pris effet, la correction est sans objet.

## 6. Sources primaires et accès (consultations du 26 octobre 2026)

- **LEGI local** (instantané au 18 octobre 2026) : identifiants LEGIARTI cités ci-dessus. Ordonnance 2021-1843 : JORFTEXT000044590225, art. 10 (lien ABROGE de 302 D bis), art. 38, 5° (NOTA de 508 et 302 M).
- **Directive 92/83/CEE**, CELEX 31992L0083, art. 27 : copie https://www.legislation.gov.uk/eudr/1992/83/article/27, version au 31 décembre 2020, qui **n'est pas** la version au 18 octobre 2026. Le texte EUR-Lex https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:01992L0083-20220101 a renvoyé HTTP 202 sans contenu ; il n'a pas été contourné.
- **Directive (UE) 2020/1151**, CELEX 32020L1151 : non obtenue (même défi EUR-Lex).
- **Règlement (CE) 3199/93**, CELEX 31993R3199, annexe substituée par le règlement d'exécution (UE) 2018/1880 (CELEX 32018R1880) : https://www.legislation.gov.uk/eur/1993/3199, version au 31 décembre 2020.
- **Règlement d'exécution (UE) 2017/2236** : titre vérifié sur https://www.legislation.gov.uk/eur/2017/2236/contents. **2017/2263** : https://www.legislation.gov.uk/eur/2017/2263/contents renvoie une erreur 404 ; non vérifié.
- **Commission européenne**, page non normative : https://taxation-customs.ec.europa.eu/taxation/excise-taxes/excise-duties-alcohol/denatured-alcohol_en.
- **CIBS L313-7 et L313-8** : affichage historique du 18 mars 2026, scellé dans `cibs-alcohol-public-followup-20261026T1707Z`. https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044603563/2026-10-18 a renvoyé HTTP 403 le 2026-10-26.

## 7. Renvois aux autres dossiers (sans doublon)

- **INUT** : déclaration de profession et numéro IN/UT (302 D bis III, 111-0 E et F, 50-0 G et H, 289 15°). Je ne corrige ici que la phrase de 165 qui présupposait la déclaration (RT-A1-02). Le 289 2° est hors du circuit IN/UT et doit être conservé.
- **MENS** : rapport mensuel (111-0 H, 50-0 I). Non traité ici.
- **CIBS** : concordance CGI et CIBS, ordonnance 2021-1843 et bornes 2027.

## 8. Incertitudes restantes et éléments non examinés

- Le droit de l'Union au 18 octobre 2026 (après la directive 2020/1151 et ses actes d'exécution) n'a pas été lu. Les conclusions européennes reposent sur le texte au 31 décembre 2020.
- L'état réel de 302 D bis et de 508 au 18 octobre 2026 (abrogation différée, décret L311-39/L311-40) n'est pas établi, pas plus que la version de CIBS L313-8 à cette date. Ordonnance n° 2026-671 du 27 juillet 2026 : signalée par le dossier CIBS, non lue ; aucun effet n'en est déduit.
- J'ai supposé que la dénaturation au procédé général est pratiquée par des opérateurs déjà identifiés par un statut d'accise (entrepositaire agréé), mais je ne l'ai pas vérifié dans le corpus. La correction de 508 ne dépend pas de cette hypothèse.
- Arrêtés et décisions administratives d'application (modèles de demande, autorisations types) : non obtenus.
- La proposition de 302 D bis n'a pas encore subi la seconde passe (`pending`) : ses termes peuvent changer.
- Versions historiques de 167 à 192 autres que 165, 185, 186, 166, 174 et 187 : non lues au fond.
- Tout cela relève d'une revue par IA. Aucune validation par un juriste n'est revendiquée.
