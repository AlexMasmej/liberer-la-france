# X8 : décisions sur les 13 défauts grossiers du sixième audit (E01 à E10)

Lecture faite en production, en lecture seule, le 30 octobre 2026 (`CITE_PRODUCTION=1 python3 -I tools/cite.py`, sqlite en `mode=ro` et `query_only`). Les pièces citées sont sous `evidence/cited/production-20261030/`. Rien n'a été écrit en production.

Les textes sont produits par `apply/X8/build_x8.py`. Le script relit la production, fait des remplacements exacts (contrôlés à l'occurrence près) et vérifie que chaque citation d'impact (`source_quote`, `proposed_quote`) est un passage exact.

Revue IA, sans validation par un juriste.

## Bilan

- **Défauts traités :** 13 sur 13. Aucun n'était déjà réglé en production.
- **Lignes :** 81 au total.
  - `apply/X8/` : 55 lignes.
  - Variantes, pour les articles attribués à un autre groupe :
    - `A8y/` : 8 lignes (annexe II 371 D, F, K bis, V bis, Z quinquies, Z octies, Z terdecies, bis K) ;
    - `M05y/` : 3 lignes (371 A, notes seules ; 371 A bis ; 371 M bis) ;
    - `J10y/` : 2 lignes (371 QA, 371 Y) ;
    - `B03y/` : 1 ligne (371 R) ;
    - `W05y/` : 6 lignes (CSS R135-15-1, R135-16-1, R135-16-3 à R135-16-6) ;
    - `W06y/` : 1 ligne (R135-16) ;
    - `W07y/` : 1 ligne (R135-16-2) ;
    - `B01y/` : 1 ligne, mode `new` (CSS L759-23, version du 1er janvier 2028) ;
    - `J13y/` : 1 ligne (annexe III 46 quater-0 ZF) ;
    - `Y17y/` : 1 ligne (annexe III 46 quater-0 ZD) ;
    - `J07y/` : 1 ligne (CCH R165-2).
- **Contrôle :** `python3 -B apply/check_changes.py <dossier>` donne `problems: []` pour les 12 dossiers ; toutes les lignes sont construites et validées.
- **Diagnostics, tous voulus :**
  - longueur : corps d'abrogation ou de limitation plus long qu'une source très courte (371 EB, G, H, LC, LD, LE, P, S, T, Z, Z septies à Z sexdecies, bis G, bis N, K bis, V bis, Z quinquies, Z terdecies ; R135-1, 5, 9, 10, 13, 16-1, 16-8 ; D135-1 ; L165-5) ;
  - renvois ajoutés : L. 135-1, L. 135-5, L. 200-2 et L. 222-2-1 dans les articles du FSV ; R. 371-9 dans R371-10 et R371-11 ; renvois retirés : L. 371-12 (R371-9), L. 1235-16 (L311-5) ;
  - renvois déjà modifiés par les propositions antérieures, non touchés : L651-2, L653-2 et L653-8 (244 bis A), L2143-3 (R165-16), L2111-1 (371 A), L160-18 (D160-16), L165-1 (R165-2).
- **Fermetures de faille (`loophole_closure: true`) :** 244 bis et 244 bis A (E191), à revoir par l'auteur.

## Par défaut

1. **E135, E223, E240 : annexe II, section des articles 371 A à 371 bis N (centres, associations, organismes mixtes, professionnels conventionnés). Appliqué : abrogation de toute la section pour l'avenir.**
   - **Constat :** CGI 1649 quater C à O sont abrogés depuis le 16 février 2025 (6° de l'article 11 de la loi n° 2025-127). Les groupes M05, J10me et X6 avaient abrogé 371 A, E, LA, M, Q, X, Z bis, Z quater, bis A et bis J. Le reste de la section organisait encore l'agrément : demande et pièces (371 F, R, Z octies), décision (G, S, Z nonies), acceptation tacite (H, T, Z decies), durée (J, U, Z undecies), retrait (K, V, Z duodecies), conventions (C, O), statuts (EA, EB, QA, Z sexies, Z septies), seuils (Z ter), intégrité des dirigeants (D, P, Z quinquies), information de la clientèle (LB, LC, LD, Z quindecies), recommandations et exclusions (Y, Z, Z sexdecies), contrôle des conventions de viseur (bis G).
   - **Correction :** chacun de ces articles est abrogé dans les termes déjà employés par M05 : base législative citée, « aucun agrément, déclaration ni condition de remplacement », droits et obligations des périodes antérieures régis par les règles alors applicables, loi répressive plus douce, avantages fiscaux autonomes non affectés, rien ne revit pour la période écoulée depuis le 16 février 2025. Garanties ajoutées selon l'article : 1747 réservé (C, O), secret des informations déjà recueillies (EB, QA, Z septies), destruction des documents comptables exhaustifs (Z sexies), dispenses Corse et outre-mer acquises pour le passé (B, N, Z ter), décisions et recours antérieurs conservés (H, K, T, V, Z decies, Z duodecies, LE, Z, Z quindecies, Z sexdecies, bis G).
   - **Articles déjà abrogés mais incohérents, réécrits :**
     - 371 LE (E240) : il déclarait « maintenues » les obligations de 371 LA à LD et « applicables » les garanties de 371 E, tous abrogés ;
     - 371 B, N, K bis, V bis, Z terdecies : ils supposaient encore l'octroi, le maintien ou l'examen de nouvelles demandes d'agrément ;
     - 371 bis K : il faisait produire à la fin d'une suspension « les effets prévus à l'article 371 bis A », abrogé ; phrase remplacée ;
     - 371 bis N : il réservait des obligations « subsistant à l'article 371 bis M », abrogé ; phrase alignée ;
     - 371 A : phrase périmée des notes supprimée (E135, F10).
   - **Faveurs :** 371 A bis et 371 M bis (faculté de services des seuls organismes agréés) sont abrogés avec la précision que la fourniture de ces services « n'est restreinte par aucune disposition de la présente section » : la faculté n'est pas retirée, elle n'a plus d'agrément à suivre. M05 les avait laissés en arbitrage ; la consigne de rendre toute la section cohérente le tranche. Les cotisations réduites deviennent libres (EA, QA, Z septies).
   - **Non touchés, car limités aux périodes passées et cohérents :** 371 L, W, Z quaterdecies, bis B, bis C, bis C bis, bis D, bis E, bis F, bis H, bis I, bis L, bis M.
   - **Pour l'auteur :** les arrêtés, modèles et l'annexe IV (164 F…) ne sont pas au corpus ou hors périmètre. Les mesures de « réforme de fond » antérieures sur ces articles ne sont plus comptées comme des coupes du projet (classement `coordination_only`), puisque la loi avait déjà supprimé le régime.

2. **E069 : CSS, chapitre R135 et D135 (fonds de solidarité vieillesse). Appliqué, même solution que R135-2, R135-6 et R135-14 (variantes W02ma, W04ma).**
   - **Constat :** L. 135-1 à L. 135-5 sont abrogés au 1er janvier 2026 (article 24 de la loi n° 2025-199) ; leurs versions sont au corpus à l'état ABROGE, contrairement aux notes qui les disaient absentes. R135-8 organisait encore pour l'avenir une convention FSV-CNAV, un président et un agent comptable.
   - **Correction, articles d'organisation** (R135-1, 3, 4, 5, 7, 8, 9, 13, D135-1) : un alinéa final constate la suppression, la dévolution des droits et obligations à la CNAV et la prise en charge des dépenses par la branche vieillesse (L. 222-2-1). L'article ne régit plus rien pour l'avenir et ne demeure applicable qu'à la clôture des comptes et à la liquidation, assurées par la CNAV. Pour R135-8, la transition qui appliquait la suppression de l'approbation aux conventions futures est remplacée par cet alinéa, avec réserve des créances, remboursements de frais et droits des tiers.
   - **Correction, articles de financement** (R135-10, 15-1, 16, 16-1, 16-2, 16-3 à 16-6, 16-8) : les formules sont conservées. Les sommes ne restent dues que dans la mesure où la branche les prend en charge en application de L. 222-2-1, et les mentions du fonds et de L. 135-2 s'entendent de la CNAV et de L. 222-2-1. Les transferts à la CNAV sont donc conservés, sans dépense nouvelle. Pour R135-16-8, les données vont à la seule CNAV.
   - **Non touchés :** R135-2, R135-6, R135-14 (déjà réglés), R135-17 et R135-16-7 (sans mention du fonds), D135-3 (déjà abrogé). La section R135-18 et suivantes concerne le fonds de réserve pour les retraites.
   - **Pour l'auteur :** la dévolution à la CNAV (XXII de l'article 24 de la loi n° 2025-199) est citée d'après la lecture de l'audit E09 sur Légifrance, le 29 octobre 2026 ; elle n'a pas été relue par X8. Les autres articles qui nomment le fonds hors du chapitre 135 (R111-1, R115-1, D114-1, D373-4, D815-9, D815-14) ne sont pas traités. Le financement de la prise en compte des indemnités maternité (R135-16-6, ancien 7° de L. 135-2) n'a pas d'équivalent dans L. 222-2-1 : avec la clause, il n'est plus dû que si la loi le prévoit.

3. **E191 : CGI 244 bis et 244 bis A. Appliqué, fermeture de faille (`loophole_closure`).**
   - **Constat :** une société sans établissement en France relève du régime de distribution (206, 12) pour ses profits immobiliers français. Pourtant, le e du 1 du V de 219 et le XII de 209 ne voient de distribution que pour un établissement stable. La suspension du prélèvement à la réalisation rendait l'impôt sur les sociétés de ces profits non recouvrable.
   - **Correction :** pour les profits et plus-values du régime rattachés à un établissement stable, le report à la distribution est maintenu. Pour les autres, le prélèvement est opéré à la réalisation ou à la cession :
     - aux taux du 2 et du 3 du V et du VI de 219, appliqués au profit avant impôt, comme au 1 bis du V de 219 ;
     - à titre libératoire de l'impôt sur les sociétés ;
     - le montant net est inscrit au compte du 1 du XI de 209, sans second impôt à la distribution ;
     - le taux de 75 % des États ou territoires non coopératifs est réservé.

     Aucune formalité nouvelle n'est créée : déclaration et paiement suivent 244 quater A et le IV de 244 bis A, comme dans la source.
   - **Pour l'auteur :** fermeture de faille à valider. Réserve F9 : l'article 63 du TFUE, pour l'écart avec le report accordé aux sociétés résidentes, n'a pas été vérifié sur source primaire.

4. **E261 : CSS L759-23 (Mayotte, du 1er janvier 2028 au 31 mars 2036). Appliqué, proposition `new` (variante B01y).**
   - Le 11° a et b reprend la seule réforme de L755-19 : cumul de l'allocation de base et des allocations familiales pour un seul enfant, « lorsque les conditions propres à chacune de ces prestations sont remplies ».
   - Le non-cumul avec le complément familial et toutes les autres adaptations mahoraises sont conservés. Les périodes antérieures restent régies par leurs règles.
   - L751-1 inclut Mayotte dès 2028 (vérifié : LEGIARTI000054466946).
   - **Pour l'auteur :** B01 avait laissé RT-FUTCSS-30 en arbitrage, parce que la mesure ouvre le cumul à Mayotte dès 2028. La consigne de report le tranche ; le coût n'est pas chiffré. Le « revenu professionnel minimal » de la rédaction mahoraise n'est pas coordonné avec L531-3.

5. **E152 : CSS R371-9 à R371-11. Appliqué.**
   - L371-12 est abrogé depuis le 25 janvier 1990 ; il figure au corpus, contrairement aux notes.
   - R371-10 et R371-11 sont abrogés : aucun règlement ne peut plus être pris sur ce fondement. Les prestations, les dispenses et les créances antérieures sont conservées.
   - R371-9 ne perd que la réserve morte ; l'absence de participation des assurés indigents est conservée.
   - La faculté de remboursement direct ajoutée par la proposition antérieure de R371-11 n'avait pas d'objet.

6. **E302 : CSS L311-5. Appliqué.**
   - Le renvoi à L1235-16 est un vestige de 2008 : il visait alors la contribution de la convention de reclassement personnalisé. Il est retiré au lieu de rattacher l'indemnité après annulation d'un PSE au maintien des droits, ce qui créait un droit nouveau non décidé.
   - Une clause protège les bénéficiaires en cours.

7. **E103 : CGI 163 quinquies C et 80 quindecies. Appliqué.**
   - Le c du 2° du 1 du II est abrogé : 150-0 A proposé supprime déjà le délai de cinq ans pour les mêmes actions de sociétés de capital-risque. C'est la seule façon de lever la contradiction (cession avant cinq ans en plus-values, distribution avant cinq ans en salaire) sans rétablir une contrainte supprimée. Il s'agit d'une cohérence, comptée sous la même mesure que 150-0 A.
   - Transition : distributions perçues à compter de la même loi.
   - Le délai de conservation de l'exonération du 2) est distinct et conservé.
   - Pour 80 quindecies, le motif seul est rectifié ; le texte officiel est maintenu.

8. **E114 : CSS D160-16. Appliqué.** « du même article » devient « de l'article D. 160-15 ».

9. **E136 : annexe III 46 quater-0 ZF (J13y) et ZD (Y17y). Appliqué.**
   - Dans 223 A proposé, le I garde six alinéas, le II un seul, et les notifications sont au III.
   - ZF retrouve les renvois exacts de la source : premier, quatrième ou cinquième alinéas du I ; deuxième alinéa du I ; sixième alinéa du I.
   - Dans ZD, les renvois au IV, au II et aux deuxième et troisième alinéas du I sont corrigés, et les notes inexactes rectifiées.
   - Aucune formalité n'est ajoutée ; la règle 95 % = 100 % et les allègements sont conservés.

10. **E148 : CSS D752-2-3. Appliqué.**
    - Le renvoi « mentionnée au troisième alinéa de L. 752-1 » est rédigé sans numéro d'alinéa, pour valoir aussi après 2028. La note qui disait le successeur de 2028 absent est corrigée.
    - **Non fait :** D752-2-1, 2-2, 2-4, 2-5 et 2-6 ont la même piste S19a dans les paquets en cours de Z01 et Z02. Pour éviter deux réécritures concurrentes, aucune variante Z01y ou Z02y n'est créée. Le coordinateur aligne leur formulation sur celle-ci.

11. **E268 : CCH R165-2 (J07y), L165-5, L165-6 et R165-16. Appliqué.**
    - R165-2 : le I ne renvoie plus à R165-16, abrogé. Le IV écarte tout document de suivi ; l'attestation d'achèvement de R165-17 reste due.
    - L165-5 : la mention « ni le bilan de fin d'agenda » est retirée, pour aligner la loi sur la suppression déjà retenue au décret.
    - L165-6 : la sanction ne peut viser le bilan final lorsque le décret ne le prévoit pas ; aucune sanction nouvelle.
    - R165-16 : notes seules.

## Points laissés à l'auteur

- E191 : la fermeture de faille et la réserve F9.
- E261 : l'ouverture du cumul à Mayotte dès 2028, et son coût.
- 371 A bis et M bis : leur abrogation est faite sans retirer la faculté.
- FSV : la dévolution à la CNAV, lue par l'audit et non relue par X8, et les articles hors chapitre 135.
- D752-2-x : l'alignement des articles de Z01 et Z02.

Revue IA : rien de ceci ne vaut validation par un juriste.
