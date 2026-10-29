# Dossier FUT-TRAV-LOG : versions futures déjà publiées (code du travail, CCH, urbanisme)

Red-team juridique indépendante, troisième passe. Instantané : `snapshots/20261026T230545Z`. Le corpus est arrêté au **18 octobre 2026** et le rapport est établi le 26 octobre 2026. Il s'agit d'une revue faite par une IA. Elle **ne vaut pas validation par un juriste**. La seconde passe se poursuit en production : les propositions citées peuvent encore changer, et ces conclusions restent provisoires.

Objet : documenter, article par article, l'objection transversale **RT-XCUT-01** pour le paquet `FUT-TRAV-LOG`. Il compte 122 couples (version en vigueur au 18 octobre 2026, version future VIGUEUR_DIFF sans proposition) et 38 nouveaux numéros futurs. Le couple travail R4451-39 (LEGIARTI000047715485, 1er juillet 2027) relève du dossier INV : il est cité ici sans être recompté.

## 1. Résumé

Je dépose **20 objections** : **10 P1** (9 confirmées, 1 à confirmer) et **10 P2** (9 confirmées, 1 à confirmer). Toutes les versions du paquet ont été qualifiées (fichier `reports/p1-work/FUT-TRAV-LOG-classification.jsonl`, 160 lignes).

| Statut | rewrite_draft (66) | retained_unchanged (56) | nouveaux numéros (38) |
|---|---|---|---|
| conflit de rédaction | 51 | — | 1 |
| réforme écrasée | 2 | — | 2 |
| déjà traité | 1 | — | — |
| sans effet | 12 | 56 | 35 |

Pour les retained_unchanged et les nouveaux numéros, « sans effet » signifie qu'aucune proposition n'est écrasée. Cela n'exclut pas une obligation nouvelle non examinée, signalée par l'objection mentionnée dans la ligne.

Constats principaux :

1. **RT-FUTTL-02 (P1).** Le projet prend l'état LEGI ABROGE_DIFF pour une abrogation. Dans 18 propositions, le corps normatif contient une clause qui affirme ou crée une abrogation inexistante. Exemples : « ne reporte pas l'abrogation du présent article prévue au 1er janvier 2029 » pour le délit de L651-3 ; « s'applique jusqu'au 31 décembre 2026 » pour la cotisation PEEC de L313-4 ; « Le présent article est abrogé à compter du 1er janvier 2028 » pour L3422-5 ; « ne proroge pas l'application […] au-delà de son abrogation différée » pour l'index égalité, dont la version de 2029 est pourtant identique. Adoptées, ces clauses mettraient fin à des normes que le droit publié maintient, ou rendraient le texte applicable incertain.
2. **RT-FUTTL-05 (P1).** Au 1er janvier 2027, les dispenses de sécurité incendie passent du code du travail au CCH (R144-18 à R144-20, décret 2025-1100). Ces nouveaux numéros rétablissent l'**enquête obligatoire** et le **délai de quatre mois**, que le projet avait rendus facultatifs ou réduits dans R4216-33 et R4216-34.
3. **RT-FUTTL-03 et RT-FUTTL-04 (P1).** Avec la recodification CIBS (ordonnance 2025-1247, 1er janvier 2027), CGI 261 B, 278 sexies et 284 disparaissent sans successeur dans le CGI. Plusieurs propositions y renvoient encore. Pour les services à la personne, la suppression de la déclaration et de l'exclusivité prévue par le projet pour la TVA perd son support : la TVA relève désormais de CIBS L213-187/188, hors des cinq codes.
4. Autres P1 : Qualiopi (RT-FUTTL-01, en vigueur dans six jours), ESUS (RT-FUTTL-06), loi Rixain 2029 et quota de 40 % (RT-FUTTL-07), registre des copropriétés (RT-FUTTL-08), convergence de Mayotte (RT-FUTTL-09), renvoi de L6353-12 à L6353-11 que le projet abroge (RT-FUTTL-10).

Points expressément vérifiés, avec un résultat négatif :
- **Contrat unique.** Aucune version future du paquet ne touche L1221-x, L1234-x, L1242/L1243 ou R1234-x. Préavis de 15 jours, absence d'indemnité avant un an, 0,20 mois par année, plafond de 6 mois, indemnité due seulement en cas de rupture par l'employeur : rien n'est écrasé. Les coordinations du contrat unique dans L5427-1 e) et L6123-5 (CPF-CDD) survivent, car les versions futures modifient d'autres passages. Pour L5427-1, voir aussi RT-P1-TRAVAIL-B-20, non recompté. La suppression de la condition d'ancienneté du projet de transition professionnelle (L6323-17-2, I) n'est pas touchée.
- **Autorisations d'urbanisme, abrogation SRU, TASCOM, dérogations littorales.** Aucune version future du paquet ne porte sur L421-x à L425-x, sur L302-5 à L302-9-x, sur la franchise TASCOM ni sur L121-28 à 30, R121-7/8/36, L104-2 ou R151-52. Les textes d'urbanisme du paquet concernent le PEB (L112-16), la taxe bureaux d'Île-de-France (L520-7, déjà traité), la terminologie pénale (L480-x) et l'exclusion de préemption liée à l'AGIE (RT-FUTTL-15).

## 2. Périmètre réellement lu

- **Les 66 couples rewrite_draft**, par date d'effet croissante. Pour chacun, j'ai lu en entier par `cite.py` la proposition, son motif, ses notes et la version future, ainsi que deux différences au mot près : source courante/version future et source courante/proposition. Exception pour quatre annexes très longues : Qualiopi (LEGIARTI000038591641/054612711), annexe II à R373-3 CCH (047400423/053470634), annexes I et II de l'index égalité (038137262/047548258, 038137266/047548249). Pour elles, j'ai lu les différences intégrales et les passages concernés, ainsi que la proposition, le motif et les notes. Je n'ai pas relu ligne à ligne les tableaux, d'où la mention « partiel » dans le JSONL.
- **Les 56 couples retained_unchanged.** J'ai lu la différence intégrale entre source courante et version future, ainsi que le motif. J'ai lu en entier le texte futur des R824-x, de L8222-2, de L8271-9 et de R144-1. Pour les autres, le texte futur est reconstitué par la différence intégrale : « partiel » dans le JSONL.
- **Les 38 nouveaux numéros** : texte futur et NOTA lus en entier.
- **Articles connexes** lus par `cite.py` pour vérifier les effets : travail R4216-1 à R4216-34 (motifs ; R4216-33 et R4216-34 en entier), L8222-1, D8222-5, L6353-11, L6111-8, L6113-8 ; CCH L171-4, L641-6, L812-2, L812-3 ; CGI 261 B, 278 sexies, 279, 279-0 bis A, 284, 231, 1384-0 A, 199 sexdecies, 244 quater J (états et bornes).
- **Dossiers voisins consultés** pour ne rien compter deux fois : XCUT.json, CIBS.json/.md (sans recoupement), P1-TRAVAIL-B.json (RT-P1-TRAVAIL-B-19 et 20 sur L5427-1). Aucun dossier INV n'était encore déposé.
- Le tableau article par article (section 7) reprend chaque version lue avec son identifiant.

Je n'ai consulté aucune source en ligne : Légifrance a refusé l'accès lors des passes précédentes (dossier CIBS) et je n'ai pas réessayé. **Aucun texte modificatif n'a été lu au JORF** (ordonnances 2025-1247, 2026-647, 2025-1091, décrets 2025-1100, 2025-831, 2026-84, 2026-728, 2026-806, lois 2026-403, 2026-534, 2026-795, 2025-989, 2021-1774, 2023-175). Leur contenu est déduit de la consolidation LEGI de l'instantané et de ses NOTA.

## 3. Méthode

1. **Lecture des couples.** Pour chaque couple, j'ai fait trois lectures : version future contre source courante (ce que change le droit publié), proposition contre source courante (ce que change le projet), puis comparaison des deux.
2. **Qualification.** Une version consolidée future résulte d'instructions de modification (« les mots … sont remplacés par … »), sauf réécriture intégrale de l'article. J'ai donc retenu :
   - **sans effet** : les modifications futures portent sur des passages que le projet ne change pas. Si la réforme entre en vigueur avant, l'instruction s'applique au texte réformé. Si elle entre en vigueur après, il faut rebaser mécaniquement la rédaction intégrale : c'est l'effet générique de RT-XCUT-01, noté « RT-XCUT-01 » dans le JSONL.
   - **réforme écrasée** : la version future réécrit le passage réformé, ou un nouveau numéro rétablit la contrainte supprimée.
   - **conflit de rédaction** : le même passage est modifié autrement, ou la proposition contient une clause, un renvoi ou une structure incompatible avec la version future.
   - **déjà traité** : la proposition ou ses notes règlent le sort de la version future.
   Cette inférence suppose que l'on connaisse la forme des textes modificatifs. Faute de lecture au JORF, c'est une réserve documentaire générale.
3. **Bornes techniques.** Les bornes 2222-02-22 et 2999-01-01 ne sont pas traitées comme des dates. Pour L213-1, L219-2 et L240-2 (loi 2026-795) et pour R4226-18-1 (décret 2025-1271), la NOTA montre une **entrée en vigueur événementielle**, d'où la borne 2222-02-22.
4. **Nouveaux numéros et retained_unchanged.** J'ai recherché les obligations contraires aux orientations (`policy-coordinations.json` : travail, logement, autorisations_urbanisme, sru_abrogation, preserved_benefits, cuts_and_reliefs, editorial_direction) et les renvois vers des articles que le projet abroge. Les propositions des articles connexes ont été lues à cette fin (L6353-11, R4216-33/34, D8222-5, L171-4).
5. **Contrôle des citations.** Toutes les citations du JSON ont été vérifiées automatiquement contre le texte de l'instantané (source, proposition, motif ou notes), après normalisation des espaces et des apostrophes.

## 4. Constats

Le détail figure dans `FUT-TRAV-LOG.json` (raisonnement, conséquences, empreintes, fichiers de preuve).

| Id | Prio. | Nature | Statut | Objet |
|---|---|---|---|---|
| RT-FUTTL-01 | P1 | coordination manquante | confirmé | Référentiel Qualiopi remplacé le 1er novembre 2026 (décret 2026-728) : la proposition repose sur l'ancienne annexe ; la suppression du renouvellement doit être reportée et les ajouts de 2026 conservés |
| RT-FUTTL-02 | P1 | incohérence du projet | confirmé | 18 propositions affirment ou créent une abrogation inexistante (lecture erronée d'ABROGE_DIFF) |
| RT-FUTTL-03 | P1 | coordination manquante | confirmé | Renvois à CGI 261 B, 278 sexies, 284 et aux règles TCA, abrogés au 1er janvier 2027 (recodification CIBS) |
| RT-FUTTL-04 | P1 | coordination manquante | à confirmer | L7233-2 : l'allègement de TVA des services à la personne part au CIBS, hors des cinq codes |
| RT-FUTTL-05 | P1 | coordination manquante | confirmé | CCH R144-19 et R144-20 (2027) rétablissent l'enquête obligatoire et les quatre mois supprimés dans R4216-33 et R4216-34 |
| RT-FUTTL-06 | P1 | coordination manquante | confirmé | ESUS (loi 2026-403) : nouveau II fondé sur l'agrément, incompatible avec la qualité de plein droit |
| RT-FUTTL-07 | P1 | coordination manquante | confirmé | Loi Rixain 2029 : quota de 40 %, publication d'objectifs, pénalité ; proposition figée à 30 % ; D1142-18 sans support |
| RT-FUTTL-08 | P1 | coordination manquante | confirmé | Registre des copropriétés (décret 2025-831) : inventaires abrogés par le projet mais rétablis et étendus ; vérification nouvelle des syndics |
| RT-FUTTL-09 | P1 | coordination manquante | confirmé | Mayotte (ordonnance 2026-647, loi 2025-797) : huit articles réécrits sur des adaptations abrogées en 2027-2036 |
| RT-FUTTL-10 | P1 | coordination manquante | confirmé | L6353-12 (2027) renvoie à L6353-11, abrogé par le projet, et crée une formalité nouvelle |
| RT-FUTTL-11 | P2 | coordination manquante | confirmé | Impayés d'APL (décret 2026-84) : quatre propositions sur l'ancien régime ; numéros réaffectés en 2027 |
| RT-FUTTL-12 | P2 | coordination manquante | confirmé | Transitions professionnelles (loi 2025-989) : missions 3° et 5° de l'instance paritaire nationale, système d'information |
| RT-FUTTL-13 | P2 | incohérence du projet | confirmé | D2135-7 et D2135-8 : allègements déjà réalisés par le décret 2026-806 ; risque de rétablir la voie DREETS |
| RT-FUTTL-14 | P2 | coordination manquante | confirmé | Renvois et institutions corrigés autrement par le droit publié (D353-145, R5312-34, R4451-61, R711-16) |
| RT-FUTTL-15 | P2 | coordination manquante | confirmé | Exclusion de préemption des cessions de l'État (loi 2026-795, date AGIE) |
| RT-FUTTL-16 | P2 | coordination manquante | confirmé | L8222-1-1 (au plus tard le 26 décembre 2026) : vigilance nouvelle envers les sous-traitants, non examinée |
| RT-FUTTL-17 | P2 | coordination manquante | confirmé | L171-5 (2028) : solarisation ou végétalisation des bâtiments existants, non examinée |
| RT-FUTTL-18 | P2 | simple alerte | confirmé | Fin au 1er janvier 2028 de la dérogation PTZ pour le neuf non collectif (D31-10-9 II bis), non tranchée |
| RT-FUTTL-19 | P2 | anomalie d'inventaire | confirmé | 160 versions futures hors inventaire ; au moins 18 notes affirment à tort que le successeur manque |
| RT-FUTTL-20 | P2 | conflit de source | à confirmer | Défauts rédactionnels des versions futures (L313-4, L3422-5, L5524-6, L112-16, D2135-8, L862-3) |

### 4.1 RT-FUTTL-02 : liste des clauses fautives

Les clauses relevées sont les suivantes : L651-3, L3422-5 (abrogation opérante), L313-4, L452-5, L302-16-1, L302-16-2, L112-16, L861-2 (seconde phrase), L861-5, D2135-7, D2135-8, D1142-4, D1142-5, D1142-6, D1142-6-2, D1142-8, annexes I et II de l'index égalité. Pour les R824-4, -6, -9 et -11, la clause est inexacte, mais le contenu de l'article est réellement remplacé : ce cas relève de RT-FUTTL-11. Trois clauses sont **légitimes**, car elles organisent des abrogations décidées par le projet lui-même : L621-6, D1142-6-1 et L520-7.

### 4.2 Cas sans effet utiles à la réforme

Pour L6123-5, R6123-16, L862-3, L480-4, L480-5, l'annexe II à R373-3 et L5427-1 (renvoi à RT-P1-TRAVAIL-B-20), le droit futur modifie d'autres passages que ceux réformés. La réforme survit, mais une rédaction intégrale adoptée après la date doit reprendre les modifications futures, en application de RT-XCUT-01. Pour D1142-x et les annexes de l'index, la version de 2029 est textuellement identique : c'est un re-versionnement LEGI de la section lié à l'insertion des articles Rixain. Seules les clauses de RT-FUTTL-02 posent problème.

## 5. Propositions de correction

Chaque correction préserve l'objectif de la réforme. Les rédactions complètes figurent dans le champ `minimal_correction` du JSON ; les plus importantes sont reprises ici.

**C1 (RT-FUTTL-02, L651-3 CCH).** Rédaction proposée, à compter de la réforme et compatible avec l'ordonnance 2025-1091 :
> Quiconque a, pour l'une quelconque des déclarations prévues aux titres Ier (chapitre II), II (chapitre Ier), III et IV du présent livre, à l'exclusion des articles L. 612-1, L. 631-1 à L. 631-6, L. 641-12 et L. 641-14, ou par les textes pris pour leur application, sciemment fait de fausses déclarations, quiconque a, à l'aide de manoeuvres frauduleuses, dissimulé ou tenté de dissimuler les locaux soumis à déclaration, est passible d'un emprisonnement d'un an et d'une amende de 80 000 euros ou de l'une de ces deux peines seulement.
> Le présent article n'entraîne, par lui-même, ni résiliation du bail ni expulsion des locataires. Les demandes de résiliation ou d'expulsion reposant sur un fondement distinct restent soumises à leurs conditions propres.
> [Troisième et quatrième alinéas de la proposition actuelle, inchangés.]

Il faut supprimer le cinquième alinéa (« La présente rédaction ne reporte pas l'abrogation […] »). Dans la loi de réforme, en disposition non codifiée : « La modification de l'article L. 651-3 du code de la construction et de l'habitation prévue par l'ordonnance n° 2025-1091 du 19 novembre 2025 est sans objet en tant qu'elle porte sur la phrase supprimée par la présente loi. » Justification : le délit de fausse déclaration est maintenu par le projet, et L641-6 y renvoie ; seule la résiliation automatique est retirée. Dépendance : L621-6 et L641-6.

**C2 (RT-FUTTL-02, L452-5 CCH).** Troisième alinéa :
> La cotisation est recouvrée et contrôlée dans les conditions prévues par les dispositions du livre II du code général des impôts et du livre des procédures fiscales qui sont applicables aux taxes sur les biens et services, sous réserve du deuxième alinéa et des obligations supprimées par le présent article. L'absence d'une déclaration périodique ou de l'utilisation d'un formulaire dont l'obligation est supprimée ne peut justifier une sanction ni une taxation d'office. Les contrôles de l'exactitude des renseignements et les conséquences des manquements aux obligations subsistantes demeurent applicables.

Il faut supprimer le dernier alinéa (« L'abrogation du présent article prévue au 1er janvier 2027 demeure applicable […] »). Les autres alinéas sont conservés. Dépendances : L452-4, L452-4-1, L342-21.

**C3 (RT-FUTTL-02, L313-4 et L3422-5).** Pour L313-4, retirer la proposition, qui est stylistique, et conserver la version officielle 2027 ; seule la correction du verbe manquant est à demander (RT-FUTTL-20). Pour L3422-5, supprimer « Le présent article est abrogé à compter du 1er janvier 2028. » et rebaser le a) sur la version 2028.

**C4 (RT-FUTTL-05, CCH R144-19 et R144-20, nouvelles propositions).**
> R. 144-19. – La dispense est accordée après examen des mesures compensatoires proposées en application de l'article R. 144-18. L'enquête de l'agent de contrôle de l'inspection du travail est facultative ; elle peut être diligentée lorsque l'appréciation de la sécurité équivalente le nécessite. Elle est accordée après avis : 1° Du comité social et économique, s'il existe ; 2° De la commission de sécurité compétente mentionnée à l'article R. 143-25. La suppression du caractère obligatoire de l'enquête s'applique aux demandes en cours et aux demandes présentées à compter de l'entrée en vigueur du décret portant la présente rédaction ; les avis et enquêtes déjà recueillis demeurent utilisables.
>
> R. 144-20. – Le silence gardé pendant plus de deux mois par le ministre compétent saisi d'un recours hiérarchique contre une décision prise en application de l'article R. 144-18 vaut décision de rejet. Ce délai s'applique aux recours reçus à compter de l'entrée en vigueur du décret portant la présente rédaction ; les recours reçus avant cette date restent soumis au délai de quatre mois.

Justification : cela reporte sur le nouveau support les deux allègements déjà décidés, sans toucher aux règles techniques. Dépendances : R4216-33 et R4216-34 sont à borner au 31 décembre 2026.

**C5 (RT-FUTTL-07, loi Rixain).** L1142-11, dernier alinéa :
> Dans chacun des deux ensembles mentionnés au premier alinéa, la proportion de personnes de chaque sexe doit être d'au moins 30 %, et d'au moins 40 % à compter du 1er mars 2029.

L1142-12, deuxième phrase : « L'entreprise transmet, au bout d'un an, aux services du ministre chargé du travail des objectifs de progression et les mesures de correction retenues, qui sont rendus publics dans les conditions prévues au deuxième alinéa de l'article L. 1142-11. » D1142-18 et D1142-19 sont à aligner sur cette transmission unique (voir le JSON).

**C6 (RT-FUTTL-06, L3332-17-1 II).**
> II. - Est réputée satisfaire aux conditions énoncées aux 1° et 2° du I l'entreprise de l'économie sociale et solidaire qui exerce des activités poursuivant une utilité sociale, au sens de l'article 2 de la loi n° 2014-856 du 31 juillet 2014 précitée, et qui appartient à l'une des catégories fixées par décret.

Les I, III, IV et V et la transition de la proposition sont conservés. Si l'auteur veut garder la liste des seize catégories, ce choix doit être motivé.

**C7 (RT-FUTTL-10, L6353-12).**
> Les prestataires de formation mentionnés à l'article L. 6351-1 qui dispensent des actions conduisant à l'obtention des certifications professionnelles, certifications et habilitations mentionnées aux articles L. 6113-5 et L. 6113-6 mettent à la disposition du public sur leur site internet, le cas échéant par un lien vers la publication des services de l'Etat, les données mentionnées aux articles L. 6111-8 et L. 6113-8-1 qui les concernent. Ils les communiquent aux apprentis, élèves et stagiaires avant toute inscription et tout règlement de frais.

**C8 (RT-FUTTL-01, Qualiopi).** Rebaser sur LEGIARTI000054612711. Le premier alinéa du II, 2 et les a) à c) deviennent : « La procédure de certification repose sur un audit initial et sur des audits de surveillance organisés selon des cycles de trois années, selon des modalités précisées par arrêté du ministre chargé de la formation professionnelle. La certification n'est soumise ni à expiration périodique ni à renouvellement. Elle comprend : a) Un audit initial, qui permet de vérifier que les actions de développement des compétences répondent aux exigences requises. En cas de résultats satisfaisants, la certification est délivrée sans limitation de durée ; b) Un audit de surveillance, qui permet de s'assurer de la bonne application du référentiel. » Les indicateurs 1 à 33 de 2026 sont conservés.

**C9 (RT-FUTTL-09, L5524-6).**
> Pour l'application à Mayotte de l'article L. 5428-1, les articles L. 131-2, L. 241-2, L. 242-13 et L. 711-2 du code de la sécurité sociale s'entendent dans leurs versions applicables à Mayotte.

Pour L1521-2-2, L1522-3, L1524-9 et L2122-6-1 : retirer les réécritures stylistiques.

**C10 (RT-FUTTL-03).** Les renvois CIBS et LPF à reprendre article par article sont donnés dans le JSON : L31-10-2 vers L. 231-85, L313-6 vers le LPF, L6323-13 vers L. 180-1 sans la majoration, L7232-1-1 vers le seul « 2° ». Pour L443-15, il faut vérifier au CIBS l'exonération qui remplace CGI 261 B.

## 6. Incertitudes et éléments non examinés

- **Textes modificatifs non lus** (réserve documentaire générale). Je n'ai pas vérifié si chaque version future résulte d'un remplacement de mots ou d'une réécriture intégrale. C'est la forme du texte qui départage, dans certains cas, « sans effet » et « réforme écrasée ».
- **Non lus** : textes hors des cinq codes (CIBS, CPP recodifié, ordonnances mahoraises, code de l'énergie, directives EPBD 2024/1275 et 2022/2381). Les propositions des articles CGI correspondants relèvent du paquet FUT-FISC.
- **Annexes longues** (Qualiopi, R373-3, index égalité) : je n'ai pas relu ligne à ligne les tableaux ; j'ai lu les différences intégrales et les passages concernés.
- **Retained_unchanged** : en dehors des R824-x, de L8222-2, de L8271-9 et de R144-1, la lecture repose sur la différence intégrale et le motif, sans relecture séparée du texte futur.
- **Recoupements** : le dossier INV, non encore déposé, peut traiter R4216-33/34 (ABROGE_DIFF) et R4451-39 ; RT-FUTTL-05 ne compte que l'effet des nouveaux numéros CCH. Le dossier UNION a relevé l'ordonnance 2026-647 pour CSS L752-1 ; RT-FUTTL-09 ne vise que les articles du travail et du CCH. Le dossier P1-TRAVAIL-B (RT-P1-TRAVAIL-B-20) couvre L5427-1.
- Je n'ai pas examiné les autres paquets FUT-* ; l'anomalie de RT-FUTTL-19 y est probable.

## 7. Documentation article par article de RT-XCUT-01

Une ligne par version future du paquet. La colonne « Lecture » vaut « oui » pour une lecture intégrale de la proposition, du motif, des notes et de la version future, et « partiel » pour une lecture par différence intégrale ou des annexes non relues tableau par tableau. Le motif de chaque qualification figure dans `reports/p1-work/FUT-TRAV-LOG-classification.jsonl`. Pour Annexe (travail, 2026-11-01), Annexe I et Annexe II (travail, 2029-03-01), deux versions courantes sont inventoriées sous le même numéro recyclé ; une seule est le vrai prédécesseur, l'autre est un faux appariement sans effet (voir le motif).

| Date d'effet | Code | Numéro | Version(s) courante(s) | Version future | Statut courant | Qualification | Objection | Lecture |
|---|---|---|---|---|---|---|---|---|
| 2026-11-01 | travail | Annexe | LEGIARTI000036483371, LEGIARTI000038591641 | LEGIARTI000054612711 | rewrite_draft | conflit de rédaction | RT-FUTTL-01 | partiel |
| 2026-12-26 | travail | L8222-1-1 | — | LEGIARTI000054335512 | nouveau_numero | sans effet | RT-FUTTL-16 | oui |
| 2026-12-26 | travail | L8222-2 | LEGIARTI000006904824 | LEGIARTI000054335516 | retained_unchanged | sans effet | RT-FUTTL-16 | oui |
| 2026-12-26 | travail | L8271-9 | LEGIARTI000029109289 | LEGIARTI000054335523 | retained_unchanged | sans effet | RT-FUTTL-16 | oui |
| 2027-01-01 | cch | Annexe II à l'article R. 373-3 | LEGIARTI000047400423 | LEGIARTI000053470634 | rewrite_draft | sans effet | RT-XCUT-01 | partiel |
| 2027-01-01 | cch | D353-145 | LEGIARTI000038979316 | LEGIARTI000053470707 | rewrite_draft | conflit de rédaction | RT-FUTTL-14 | oui |
| 2027-01-01 | cch | L302-16-1 | LEGIARTI000042857888 | LEGIARTI000054567276 | rewrite_draft | conflit de rédaction | RT-FUTTL-02 | oui |
| 2027-01-01 | cch | L302-16-2 | LEGIARTI000042857903 | LEGIARTI000054567273 | rewrite_draft | conflit de rédaction | RT-FUTTL-02 | oui |
| 2027-01-01 | cch | L31-10-2 | LEGIARTI000048826443 | LEGIARTI000054567279 | rewrite_draft | conflit de rédaction | RT-FUTTL-03 | oui |
| 2027-01-01 | cch | L313-4 | LEGIARTI000037387268 | LEGIARTI000053151481 | rewrite_draft | conflit de rédaction | RT-FUTTL-02 | oui |
| 2027-01-01 | cch | L313-6 | LEGIARTI000006824846 | LEGIARTI000053151478 | rewrite_draft | conflit de rédaction | RT-FUTTL-03 | oui |
| 2027-01-01 | cch | L443-15 | LEGIARTI000037669097 | LEGIARTI000053151467 | rewrite_draft | conflit de rédaction | RT-FUTTL-03 | oui |
| 2027-01-01 | cch | L452-5 | LEGIARTI000048839976 | LEGIARTI000053151495 | rewrite_draft | conflit de rédaction | RT-FUTTL-02 | oui |
| 2027-01-01 | cch | R144-1 | LEGIARTI000043819051 | LEGIARTI000052645045 | retained_unchanged | sans effet | RT-FUTTL-05 | oui |
| 2027-01-01 | cch | R144-10 | — | LEGIARTI000052645016 | nouveau_numero | sans effet | RT-FUTTL-05 | oui |
| 2027-01-01 | cch | R144-11 | — | LEGIARTI000052645014 | nouveau_numero | sans effet | RT-FUTTL-05 | oui |
| 2027-01-01 | cch | R144-12 | — | LEGIARTI000052645012 | nouveau_numero | sans effet | RT-FUTTL-05 | oui |
| 2027-01-01 | cch | R144-13 | — | LEGIARTI000052645010 | nouveau_numero | sans effet | RT-FUTTL-05 | oui |
| 2027-01-01 | cch | R144-14 | — | LEGIARTI000052645007 | nouveau_numero | sans effet | RT-FUTTL-05 | oui |
| 2027-01-01 | cch | R144-15 | — | LEGIARTI000052645005 | nouveau_numero | sans effet | RT-FUTTL-05 | oui |
| 2027-01-01 | cch | R144-16 | — | LEGIARTI000052645003 | nouveau_numero | sans effet | RT-FUTTL-05 | oui |
| 2027-01-01 | cch | R144-17 | — | LEGIARTI000052645001 | nouveau_numero | sans effet | RT-FUTTL-05 | oui |
| 2027-01-01 | cch | R144-18 | — | LEGIARTI000052644998 | nouveau_numero | sans effet | RT-FUTTL-05 | oui |
| 2027-01-01 | cch | R144-19 | — | LEGIARTI000052644996 | nouveau_numero | réforme écrasée | RT-FUTTL-05 | oui |
| 2027-01-01 | cch | R144-2 | — | LEGIARTI000052645035 | nouveau_numero | sans effet | RT-FUTTL-05 | oui |
| 2027-01-01 | cch | R144-20 | — | LEGIARTI000052644994 | nouveau_numero | réforme écrasée | RT-FUTTL-05 | oui |
| 2027-01-01 | cch | R144-3 | — | LEGIARTI000052645033 | nouveau_numero | sans effet | RT-FUTTL-05 | oui |
| 2027-01-01 | cch | R144-4 | — | LEGIARTI000052645031 | nouveau_numero | sans effet | RT-FUTTL-05 | oui |
| 2027-01-01 | cch | R144-5 | — | LEGIARTI000052645029 | nouveau_numero | sans effet | RT-FUTTL-05 | oui |
| 2027-01-01 | cch | R144-6 | — | LEGIARTI000052645027 | nouveau_numero | sans effet | RT-FUTTL-05 | oui |
| 2027-01-01 | cch | R144-7 | — | LEGIARTI000052645025 | nouveau_numero | sans effet | RT-FUTTL-05 | oui |
| 2027-01-01 | cch | R144-8 | — | LEGIARTI000052645023 | nouveau_numero | sans effet | RT-FUTTL-05 | oui |
| 2027-01-01 | cch | R144-9 | — | LEGIARTI000052645021 | nouveau_numero | sans effet | RT-FUTTL-05 | oui |
| 2027-01-01 | cch | R824-1 | LEGIARTI000038878877 | LEGIARTI000053470474 | retained_unchanged | sans effet | RT-FUTTL-11 | oui |
| 2027-01-01 | cch | R824-10 | LEGIARTI000038878855 | LEGIARTI000053470493 | retained_unchanged | sans effet | RT-FUTTL-11 | oui |
| 2027-01-01 | cch | R824-11 | LEGIARTI000038878851 | LEGIARTI000053470490 | rewrite_draft | conflit de rédaction | RT-FUTTL-11 | oui |
| 2027-01-01 | cch | R824-12 | LEGIARTI000038878849 | LEGIARTI000053470507 | retained_unchanged | sans effet | RT-FUTTL-11 | oui |
| 2027-01-01 | cch | R824-13 | LEGIARTI000038878847 | LEGIARTI000053470503 | retained_unchanged | sans effet | RT-FUTTL-11 | oui |
| 2027-01-01 | cch | R824-14 | LEGIARTI000038878843 | LEGIARTI000053470500 | retained_unchanged | sans effet | RT-FUTTL-11 | oui |
| 2027-01-01 | cch | R824-15 | — | LEGIARTI000054394490 | nouveau_numero | sans effet | RT-FUTTL-11 | oui |
| 2027-01-01 | cch | R824-16 | LEGIARTI000038878839 | LEGIARTI000053470497 | retained_unchanged | sans effet | RT-FUTTL-11 | oui |
| 2027-01-01 | cch | R824-2 | LEGIARTI000038878875 | LEGIARTI000053470471 | retained_unchanged | sans effet | RT-FUTTL-11 | oui |
| 2027-01-01 | cch | R824-3 | LEGIARTI000038878873 | LEGIARTI000053470469 | retained_unchanged | sans effet | RT-FUTTL-11 | oui |
| 2027-01-01 | cch | R824-4 | LEGIARTI000038878867 | LEGIARTI000053470467 | rewrite_draft | conflit de rédaction | RT-FUTTL-11 | oui |
| 2027-01-01 | cch | R824-5 | LEGIARTI000038878865 | LEGIARTI000053470465 | retained_unchanged | sans effet | RT-FUTTL-11 | oui |
| 2027-01-01 | cch | R824-6 | LEGIARTI000038878863 | LEGIARTI000053470485 | rewrite_draft | conflit de rédaction | RT-FUTTL-11 | oui |
| 2027-01-01 | cch | R824-7 | LEGIARTI000038878861 | LEGIARTI000053470483 | retained_unchanged | sans effet | RT-FUTTL-11 | oui |
| 2027-01-01 | cch | R824-8 | LEGIARTI000038878859 | LEGIARTI000053470481 | retained_unchanged | sans effet | RT-FUTTL-11 | oui |
| 2027-01-01 | cch | R824-9 | LEGIARTI000038878857 | LEGIARTI000053470478 | rewrite_draft | conflit de rédaction | RT-FUTTL-11 | oui |
| 2027-01-01 | cch | R862-2 | LEGIARTI000041419269 | LEGIARTI000054394059 | retained_unchanged | sans effet | RT-FUTTL-11 | partiel |
| 2027-01-01 | cch | R862-3 | LEGIARTI000039621265 | LEGIARTI000054394516 | retained_unchanged | sans effet | RT-FUTTL-11 | partiel |
| 2027-01-01 | cch | R863-9 | LEGIARTI000044636793 | LEGIARTI000054394576 | retained_unchanged | sans effet | RT-FUTTL-11 | partiel |
| 2027-01-01 | travail | L3332-17-1 | LEGIARTI000049720096 | LEGIARTI000054140237 | rewrite_draft | conflit de rédaction | RT-FUTTL-06 | oui |
| 2027-01-01 | travail | L6123-5 | LEGIARTI000053549490 | LEGIARTI000052437578 | rewrite_draft | sans effet | RT-XCUT-01 | oui |
| 2027-01-01 | travail | L6323-13 | LEGIARTI000052437094 | LEGIARTI000053151869 | rewrite_draft | conflit de rédaction | RT-FUTTL-03 | oui |
| 2027-01-01 | travail | L6323-17-2 | LEGIARTI000047452262 | LEGIARTI000052437428 | rewrite_draft | conflit de rédaction | RT-FUTTL-12 | oui |
| 2027-01-01 | travail | L6323-17-5-1 | LEGIARTI000052437402 | LEGIARTI000052437649 | rewrite_draft | conflit de rédaction | RT-FUTTL-12 | oui |
| 2027-01-01 | travail | L7232-1-1 | LEGIARTI000048844005 | LEGIARTI000053151864 | rewrite_draft | conflit de rédaction | RT-FUTTL-03 | oui |
| 2027-01-01 | travail | L7233-2 | LEGIARTI000048843938 | LEGIARTI000053151858 | rewrite_draft | réforme écrasée | RT-FUTTL-04 | oui |
| 2027-01-01 | travail | R4211-3 | LEGIARTI000024769357 | LEGIARTI000052645178 | retained_unchanged | sans effet | RT-FUTTL-05 | partiel |
| 2027-01-01 | travail | R4214-28 | — | LEGIARTI000052645192 | nouveau_numero | sans effet | RT-FUTTL-05 | oui |
| 2027-01-01 | travail | R4214-7 | LEGIARTI000018532507 | LEGIARTI000052645184 | retained_unchanged | sans effet | RT-FUTTL-05 | partiel |
| 2027-01-01 | travail | R4214-9 | LEGIARTI000018532501 | LEGIARTI000052645188 | retained_unchanged | sans effet | RT-FUTTL-05 | partiel |
| 2027-01-01 | travail | R4227-2 | LEGIARTI000018532143 | LEGIARTI000052645195 | retained_unchanged | sans effet | RT-FUTTL-05 | partiel |
| 2027-01-01 | travail | R4227-37 | LEGIARTI000024769379 | LEGIARTI000052645197 | retained_unchanged | sans effet | RT-FUTTL-05 | partiel |
| 2027-01-01 | travail | R5312-33 | LEGIARTI000050943121 | LEGIARTI000050947086 | retained_unchanged | sans effet | — | partiel |
| 2027-01-01 | travail | R5312-34 | LEGIARTI000050943127 | LEGIARTI000050947141 | rewrite_draft | conflit de rédaction | RT-FUTTL-14 | oui |
| 2027-01-01 | travail | R6123-16 | LEGIARTI000053428211 | LEGIARTI000054107742 | rewrite_draft | sans effet | RT-XCUT-01 | oui |
| 2027-01-01 | travail | R6323-18-13 | — | LEGIARTI000054106237 | nouveau_numero | sans effet | RT-FUTTL-12 | oui |
| 2027-01-01 | urba | L112-16 | LEGIARTI000031210287 | LEGIARTI000053151885 | rewrite_draft | conflit de rédaction | RT-FUTTL-02 | oui |
| 2027-01-01 | urba | L520-7 | LEGIARTI000045917236 | LEGIARTI000054567160 | rewrite_draft | déjà traité | — | oui |
| 2027-01-15 | travail | D2135-7 | LEGIARTI000030190813 | LEGIARTI000054739438 | rewrite_draft | conflit de rédaction | RT-FUTTL-13 | oui |
| 2027-01-15 | travail | D2135-8 | LEGIARTI000054175074 | LEGIARTI000054739440 | rewrite_draft | conflit de rédaction | RT-FUTTL-13 | oui |
| 2027-02-21 | cch | R711-16 | LEGIARTI000033073023 | LEGIARTI000052123156 | rewrite_draft | conflit de rédaction | RT-FUTTL-14 | oui |
| 2027-02-21 | cch | R711-8 | LEGIARTI000033073005 | LEGIARTI000052123166 | retained_unchanged | sans effet | RT-FUTTL-08 | partiel |
| 2027-02-21 | cch | R711-9 | LEGIARTI000042078909 | LEGIARTI000052123161 | rewrite_draft | réforme écrasée | RT-FUTTL-08 | oui |
| 2027-06-25 | travail | L6113-8-1 | — | LEGIARTI000054337158 | nouveau_numero | sans effet | RT-FUTTL-10 | oui |
| 2027-06-25 | travail | L6353-12 | — | LEGIARTI000054319423 | nouveau_numero | conflit de rédaction | RT-FUTTL-10 | oui |
| 2027-07-01 | travail | R4451-38 | LEGIARTI000037024759 | LEGIARTI000047715489 | retained_unchanged | sans effet | — | partiel |
| 2027-07-01 | travail | R4451-39 | LEGIARTI000037024754 | LEGIARTI000047715485 | retained_unchanged | sans effet | INV (non recompté) | partiel |
| 2027-07-01 | travail | R4451-61 | LEGIARTI000037024582 | LEGIARTI000050927329 | rewrite_draft | conflit de rédaction | RT-FUTTL-14 | oui |
| 2027-07-01 | travail | R4451-62 | LEGIARTI000037024578 | LEGIARTI000047715521 | retained_unchanged | sans effet | — | partiel |
| 2027-07-01 | travail | R4451-63 | LEGIARTI000037024573 | LEGIARTI000050927325 | retained_unchanged | sans effet | — | partiel |
| 2027-12-31 | travail | L1521-2-2 | LEGIARTI000036261425 | LEGIARTI000052085723 | rewrite_draft | conflit de rédaction | RT-FUTTL-09 | oui |
| 2028-01-01 | cch | D31-10-9 | LEGIARTI000051397190 | LEGIARTI000051400385 | retained_unchanged | sans effet | RT-FUTTL-18 | partiel |
| 2028-01-01 | cch | L171-5 | — | LEGIARTI000047298141 | nouveau_numero | sans effet | RT-FUTTL-17 | oui |
| 2028-01-01 | cch | L181-11 | LEGIARTI000046120784 | LEGIARTI000047475243 | retained_unchanged | sans effet | RT-FUTTL-17 | partiel |
| 2028-01-01 | cch | L183-4 | LEGIARTI000046123749 | LEGIARTI000047475406 | retained_unchanged | sans effet | RT-FUTTL-17 | partiel |
| 2028-01-01 | cch | L861-2 | LEGIARTI000038814787 | LEGIARTI000054475016 | rewrite_draft | conflit de rédaction | RT-FUTTL-02 | oui |
| 2028-01-01 | cch | L861-5 | LEGIARTI000044405110 | LEGIARTI000054475019 | rewrite_draft | conflit de rédaction | RT-FUTTL-09 | oui |
| 2028-01-01 | cch | L862-3 | LEGIARTI000038814753 | LEGIARTI000054475023 | rewrite_draft | sans effet | RT-XCUT-01 | oui |
| 2028-01-01 | travail | L1521-2-2 | LEGIARTI000036261425 | LEGIARTI000054468599 | rewrite_draft | conflit de rédaction | RT-FUTTL-09 | oui |
| 2028-01-01 | travail | L1522-3 | LEGIARTI000035902392 | LEGIARTI000054468604 | rewrite_draft | conflit de rédaction | RT-FUTTL-09 | oui |
| 2028-01-01 | travail | L1524-9 | LEGIARTI000035881741 | LEGIARTI000054468608 | rewrite_draft | conflit de rédaction | RT-FUTTL-09 | oui |
| 2028-01-01 | travail | L2122-6-1 | LEGIARTI000035902419 | LEGIARTI000054468611 | rewrite_draft | conflit de rédaction | RT-FUTTL-09 | oui |
| 2028-01-01 | travail | L3142-104 | LEGIARTI000033021890 | LEGIARTI000054703450 | retained_unchanged | sans effet | — | partiel |
| 2028-01-01 | travail | L3422-5 | LEGIARTI000035902495 | LEGIARTI000054468615 | rewrite_draft | conflit de rédaction | RT-FUTTL-02 | oui |
| 2028-01-01 | travail | L5151-11 | LEGIARTI000044375921 | LEGIARTI000054703477 | retained_unchanged | sans effet | — | partiel |
| 2028-01-01 | travail | L5427-1 | LEGIARTI000048600544 | LEGIARTI000054468622 | rewrite_draft | sans effet | RT-P1-TRAVAIL-B-20 | oui |
| 2028-01-01 | travail | L5524-2 | LEGIARTI000037388521 | LEGIARTI000054468635 | rewrite_draft | conflit de rédaction | RT-FUTTL-09 | oui |
| 2028-01-01 | travail | L5524-6 | LEGIARTI000035902588 | LEGIARTI000054468644 | rewrite_draft | conflit de rédaction | RT-FUTTL-09 | oui |
| 2028-01-01 | travail | L6323-17-2 | LEGIARTI000047452262 | LEGIARTI000052437628 | rewrite_draft | conflit de rédaction | RT-FUTTL-12 | oui |
| 2028-01-01 | travail | L6323-17-5-1 | LEGIARTI000052437402 | LEGIARTI000052437674 | rewrite_draft | conflit de rédaction | RT-FUTTL-12 | oui |
| 2028-01-01 | travail | R4451-129 | — | LEGIARTI000050927584 | nouveau_numero | sans effet | — | oui |
| 2028-01-01 | travail | R4451-130 | — | LEGIARTI000050927582 | nouveau_numero | sans effet | — | oui |
| 2028-01-01 | travail | R4451-131 | — | LEGIARTI000050927570 | nouveau_numero | sans effet | — | oui |
| 2028-01-01 | travail | R4451-132 | — | LEGIARTI000050927568 | nouveau_numero | sans effet | — | oui |
| 2028-01-01 | travail | R4451-133 | — | LEGIARTI000050927566 | nouveau_numero | sans effet | — | oui |
| 2028-07-01 | travail | R4451-112 | LEGIARTI000037024246 | LEGIARTI000050927374 | retained_unchanged | sans effet | — | partiel |
| 2028-07-01 | travail | R4451-125 | LEGIARTI000050961292 | LEGIARTI000050927365 | retained_unchanged | sans effet | — | partiel |
| 2028-07-01 | travail | R4451-126 | LEGIARTI000050961324 | LEGIARTI000050927352 | retained_unchanged | sans effet | — | partiel |
| 2029-01-01 | cch | L183-2 | LEGIARTI000041570599 | LEGIARTI000052846032 | retained_unchanged | sans effet | — | partiel |
| 2029-01-01 | cch | L183-7 | LEGIARTI000046123747 | LEGIARTI000052846030 | retained_unchanged | sans effet | — | partiel |
| 2029-01-01 | cch | L621-6 | LEGIARTI000039279909 | LEGIARTI000052846041 | rewrite_draft | sans effet | — | oui |
| 2029-01-01 | cch | L651-3 | LEGIARTI000006825952 | LEGIARTI000052846034 | rewrite_draft | conflit de rédaction | RT-FUTTL-02 | oui |
| 2029-01-01 | travail | L8113-12 | LEGIARTI000054316647 | LEGIARTI000054787411 | retained_unchanged | sans effet | — | partiel |
| 2029-01-01 | travail | L8114-4 | LEGIARTI000032375310 | LEGIARTI000052851302 | retained_unchanged | sans effet | — | partiel |
| 2029-01-01 | travail | L8114-6 | LEGIARTI000032375321 | LEGIARTI000052851300 | retained_unchanged | sans effet | — | partiel |
| 2029-01-01 | travail | L8271-3 | LEGIARTI000033025016 | LEGIARTI000052851296 | retained_unchanged | sans effet | — | partiel |
| 2029-01-01 | travail | L8271-6-1 | LEGIARTI000032655803 | LEGIARTI000052851293 | retained_unchanged | sans effet | — | partiel |
| 2029-01-01 | travail | R3324-22 | LEGIARTI000049905590 | LEGIARTI000052845711 | retained_unchanged | sans effet | — | partiel |
| 2029-01-01 | urba | L480-2 | LEGIARTI000041411292 | LEGIARTI000052845893 | retained_unchanged | sans effet | — | partiel |
| 2029-01-01 | urba | L480-4 | LEGIARTI000049398788 | LEGIARTI000052851316 | rewrite_draft | sans effet | RT-XCUT-01 | oui |
| 2029-01-01 | urba | L480-5 | LEGIARTI000043979205 | LEGIARTI000052851310 | rewrite_draft | sans effet | RT-XCUT-01 | oui |
| 2029-01-01 | urba | L480-6 | LEGIARTI000041411243 | LEGIARTI000052851305 | retained_unchanged | sans effet | — | partiel |
| 2029-03-01 | travail | Annexe I | LEGIARTI000038137262, LEGIARTI000040477365 | LEGIARTI000047548258 | rewrite_draft | conflit de rédaction | RT-FUTTL-02 | partiel |
| 2029-03-01 | travail | Annexe II | LEGIARTI000023018851, LEGIARTI000038137266 | LEGIARTI000047548249 | rewrite_draft | conflit de rédaction | RT-FUTTL-02 | partiel |
| 2029-03-01 | travail | D1142-10 | LEGIARTI000038026047 | LEGIARTI000047548298 | retained_unchanged | sans effet | — | partiel |
| 2029-03-01 | travail | D1142-11 | LEGIARTI000038026051 | LEGIARTI000047548291 | retained_unchanged | sans effet | — | partiel |
| 2029-03-01 | travail | D1142-12 | LEGIARTI000038026055 | LEGIARTI000047548286 | retained_unchanged | sans effet | — | partiel |
| 2029-03-01 | travail | D1142-13 | LEGIARTI000038026059 | LEGIARTI000047548276 | retained_unchanged | sans effet | — | partiel |
| 2029-03-01 | travail | D1142-14 | LEGIARTI000038026063 | LEGIARTI000047548269 | rewrite_draft | sans effet | — | oui |
| 2029-03-01 | travail | D1142-15 | LEGIARTI000045669609 | LEGIARTI000047548240 | retained_unchanged | sans effet | — | partiel |
| 2029-03-01 | travail | D1142-16 | LEGIARTI000045669624 | LEGIARTI000047548234 | rewrite_draft | sans effet | RT-FUTTL-07 | oui |
| 2029-03-01 | travail | D1142-17 | LEGIARTI000045669628 | LEGIARTI000047548230 | retained_unchanged | sans effet | — | partiel |
| 2029-03-01 | travail | D1142-18 | — | LEGIARTI000045669671 | nouveau_numero | sans effet | RT-FUTTL-07 | oui |
| 2029-03-01 | travail | D1142-19 | LEGIARTI000045688527 | LEGIARTI000045688595 | rewrite_draft | conflit de rédaction | RT-FUTTL-07 | oui |
| 2029-03-01 | travail | D1142-2 | LEGIARTI000038026011 | LEGIARTI000047548410 | retained_unchanged | sans effet | — | partiel |
| 2029-03-01 | travail | D1142-2-1 | LEGIARTI000038026015 | LEGIARTI000047548404 | retained_unchanged | sans effet | — | partiel |
| 2029-03-01 | travail | D1142-3 | LEGIARTI000038026019 | LEGIARTI000047548396 | retained_unchanged | sans effet | — | partiel |
| 2029-03-01 | travail | D1142-4 | LEGIARTI000045250060 | LEGIARTI000047548385 | rewrite_draft | conflit de rédaction | RT-FUTTL-02 | oui |
| 2029-03-01 | travail | D1142-5 | LEGIARTI000045250047 | LEGIARTI000047548371 | rewrite_draft | conflit de rédaction | RT-FUTTL-02 | oui |
| 2029-03-01 | travail | D1142-6 | LEGIARTI000045250040 | LEGIARTI000047548361 | rewrite_draft | conflit de rédaction | RT-FUTTL-02 | oui |
| 2029-03-01 | travail | D1142-6-1 | LEGIARTI000045247841 | LEGIARTI000047548343 | rewrite_draft | sans effet | — | oui |
| 2029-03-01 | travail | D1142-6-2 | LEGIARTI000045247901 | LEGIARTI000047548332 | rewrite_draft | conflit de rédaction | RT-FUTTL-02 | oui |
| 2029-03-01 | travail | D1142-7 | LEGIARTI000038026035 | LEGIARTI000047548327 | rewrite_draft | sans effet | — | oui |
| 2029-03-01 | travail | D1142-8 | LEGIARTI000045250066 | LEGIARTI000047548312 | rewrite_draft | conflit de rédaction | RT-FUTTL-02 | oui |
| 2029-03-01 | travail | D1142-9 | LEGIARTI000038026043 | LEGIARTI000047548306 | retained_unchanged | sans effet | — | partiel |
| 2029-03-01 | travail | L1142-11 | LEGIARTI000045951643 | LEGIARTI000044613235 | rewrite_draft | conflit de rédaction | RT-FUTTL-07 | oui |
| 2029-03-01 | travail | L1142-12 | — | LEGIARTI000044566691 | nouveau_numero | sans effet | RT-FUTTL-07 | oui |
| 2029-03-01 | travail | R1142-20 | — | LEGIARTI000047547415 | nouveau_numero | sans effet | RT-FUTTL-07 | oui |
| 2029-03-01 | travail | R1142-21 | — | LEGIARTI000047547418 | nouveau_numero | sans effet | RT-FUTTL-07 | oui |
| 2029-03-01 | travail | R1142-22 | — | LEGIARTI000047547420 | nouveau_numero | sans effet | RT-FUTTL-07 | oui |
| 2029-03-01 | travail | R1142-23 | — | LEGIARTI000047547422 | nouveau_numero | sans effet | RT-FUTTL-07 | oui |
| 2032-01-01 | travail | L1521-2-2 | LEGIARTI000036261425 | LEGIARTI000054481673 | rewrite_draft | conflit de rédaction | RT-FUTTL-09 | oui |
| 2036-01-01 | travail | L1521-2-2 | LEGIARTI000036261425 | LEGIARTI000054481814 | rewrite_draft | conflit de rédaction | RT-FUTTL-09 | oui |
| 2222-02-22 | travail | R4226-18-1 | — | LEGIARTI000053161627 | nouveau_numero | sans effet | — | oui |
| 2222-02-22 | urba | L213-1 | LEGIARTI000048704337 | LEGIARTI000054713084 | rewrite_draft | conflit de rédaction | RT-FUTTL-15 | oui |
| 2222-02-22 | urba | L219-2 | LEGIARTI000045525589 | LEGIARTI000054713068 | rewrite_draft | conflit de rédaction | RT-FUTTL-15 | oui |
| 2222-02-22 | urba | L240-2 | LEGIARTI000048704303 | LEGIARTI000054713050 | rewrite_draft | conflit de rédaction | RT-FUTTL-15 | oui |
