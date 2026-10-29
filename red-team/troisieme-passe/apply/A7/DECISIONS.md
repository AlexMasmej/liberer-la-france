# Groupe A7 : décisions de la troisième passe

Textes lus dans l'instantané `20261029T034912Z` (cite.py) ; contrôle `python3 -B apply/check_changes.py A7` : 22 changements construits et validés, `problems` vide. Les diagnostics restants (longueur de 1668, 205 C, 205 D, 216 ; renvois de 212 bis et L302-1) existaient avant les corrections. Revue IA : rien de ceci ne vaut validation par un juriste.

Critère appliqué : une correction qui ferait payer chaque année un IS que le projet reporte à la distribution n'est retenue que si une norme supérieure l'impose de façon certaine et que l'objection est « confirmé ». L'article 4 de la directive 2016/1164 a été relu le 28 octobre 2026 sur la copie de legislation.gov.uk (EUR-Lex renvoie une page vide) : « Exceeding borrowing costs shall be deductible in the tax period in which they are incurred only up to 30 percent » ; l'article 1 vise « all taxpayers that are subject to corporate tax ».

| Objection | Décision | Articles touchés | Ce qui change |
|---|---|---|---|
| RT-DOMIS-01 (confirmé) | Appliquée | CGI 219 (V, 6), 1668 (premier alinéa) | Les entités dans le champ du minimum international peuvent opter pour une liquidation annuelle de l'IS à 20 % ; le bénéfice ainsi taxé va au compte protégé et sa distribution ne paie plus de second IS. |
| RT-DOMIS-02 (confirmé) | Appliquée en partie (option a) | CGI 219 (V, 1 bis a), 212 bis (X), 1668 | Les charges financières nettes non déductibles de 212 bis et 223 B bis sont taxées l'année où elles sont constatées, à 20 % du montant, dans la limite du résultat de référence positif, avec imputation facultative des déficits et des reports ultérieurs. |
| RT-DOMIS-03 (confirmé) | Appliquée | CGI 219 (VI, 2), 206 (12), 1668 ; notes de 205 B, 205 C, 205 D, 209 B | Les impositions correctives annuelles (anti-hybrides, sociétés étrangères contrôlées) reçoivent un taux (20 %, ou 15 % dans la tranche PME, au lieu de 25 %), l'imputation des déficits et une échéance (relevé de solde, sans acompte). |
| RT-DOMIS-04 (confirmé) | Appliquée | CGI 209 (XI, 3), 223 I (II), annexe III 46 quater-0 ZJ bis ; notes de 223 L | La contradiction entre lots est levée dans le sens favorable : les pertes nouvelles des membres d'un groupe se compensent selon 223 A IV. |
| RT-DOMIS-05 (à confirmer) | Appliquée | CGI 216 (IV) | Les dividendes de portefeuille venant de l'UE, de l'EEE ou d'un État conventionné sont protégés à proportion de l'impôt effectivement payé par la société distributrice. |
| RT-DOMIS-06 (à confirmer) | Demande à A1 | CGI 119 ter (LEGIARTI000031815505 et version 2027 LEGIARTI000053154449) | Les sociétés de l'Union détenant moins de 10 % sont exonérées de retenue lorsqu'un résident aurait été protégé. Texte exact donné dans `requests`. |
| RT-DOMIS-07 (confirmé) | Appliquée, `loophole_closure` | CGI 219 (V, 1 bis b), 221 (2 et 7 a) | Les bénéfices différés d'une société qui quitte l'IS (transformation, renonciation à l'option, exonération personnelle) sont taxés comme une distribution ; le montant net est ensuite protégé. |
| RT-DOMSUCC-01 (confirmé) | Appliquée en partie, `loophole_closure` | CGI 784 C, 792 bis, 792-0 bis | Une libéralité graduelle, une fiducie ou un trust dont l'auteur est vivant n'échappe plus aux droits de donation parce qu'elle s'exécute au décès d'un tiers. |
| RT-DOMTS-01 (à confirmer) | Non appliquée (arbitrage) | — | — |
| RT-P1-CGI-B-01 (confirmé) | Appliquée | CCH L433-2, L302-1 | La zone de l'ancien 1406 bis est figée à la liste de la veille de l'abrogation (L433-2 y ajoute les critères antérieurs) ; aucune obligation n'est créée s'il n'existe pas de liste. |
| RT-P1-CGI-C-03 (à confirmer) | Non appliquée (arbitrage) | — | — |
| RT-P1-CGI-C-06 (confirmé) | Appliquée | Annexe IV 50 sexies B ; notes de 290 quater ; demande pour 50 sexies C (article non attribué) | Le nouveau V supprime toute la billetterie fiscale pour les spectacles futurs. Les I à IV sont conservés pour les spectacles antérieurs et pour que le renvoi de 50 sexies C reste exact. |
| RT-P1-CGI-C-07 (confirmé) | Appliquée | Annexe III 38 quindecies A (`full_repeal`) | L'article est abrogé à la même date que 54 octies, avec la même transition. |

## Détail et points laissés à l'auteur

- **RT-DOMIS-01.** L'option est facultative et favorable. Deux écarts par rapport au texte de l'objection, tous deux dans le sens de l'allègement :
  - l'option s'exerce par une mention portée sur la déclaration existante, et non par une notification distincte ;
  - l'impôt se paie avec le relevé de solde, sans acompte, conformément à l'orientation (pas d'acompte sur bénéfice conservé).

  Reste à vérifier sur la directive 2022/2523 : la mécanique GloBE, c'est-à-dire le rattachement des impôts couverts à l'exercice.
- **RT-DOMIS-02.**
  - Appliqué : seule l'imposition annuelle des surcoûts d'emprunt est retenue, parce que l'article 4 de l'ATAD l'impose de façon certaine.
  - Non appliqué, faute de norme supérieure : l'imposition annuelle des charges somptuaires (39, 4), des sanctions (39, 2) et des paiements de 238 A. Ces charges restent suivies dans les compartiments et ne sont taxées qu'à la distribution.
  - Le texte retenu ne taxe pas plus que le droit actuel : 20 % au lieu de 25 %, rien pour un exercice déficitaire, déficits imputables au choix de l'entreprise.
  - 223 B bis n'est attribué à aucun groupe. Il est couvert par renvoi depuis 219, sans modification.
- **RT-DOMIS-03.** Le taux de 25 % aurait pu être maintenu pour ces impositions. Cette option, plus sévère, n'est pas retenue.
- **RT-DOMIS-05 et 06.** Ces deux objections sont « à confirmer » (article 63 TFUE ; jurisprudence citée de mémoire). Elles sont appliquées parce qu'elles ne font que réduire l'impôt et ne créent aucune formalité, quel que soit le point de droit restant à confirmer. Reste ouverte : la comparabilité exacte, sur le taux effectif ou le taux nominal.
- **RT-DOMIS-07.** Ce n'est pas une imposition annuelle : l'impôt naît d'un événement de sortie, comme pour une liquidation. La correction ne fait que rétablir ce que le droit actuel taxe déjà lors d'une cessation. Elle ferme la sortie sans IS, contraire à l'orientation `is_distribution` (« traiter rachats, liquidation et transferts d'actifs sans créer une échappatoire »). Restent intacts :
  - la libre renonciation à l'option de 239 ;
  - les exonérations temporaires ou partielles de bénéfices ;
  - 221 bis, 208 C et 207 (1, 4°).

  Elle est marquée pour revue de l'auteur.
- **RT-DOMSUCC-01.**
  - Appliqué : volets a (784 C) et b (792-0 bis, 792 bis) de la correction révisée.
  - Non appliqué : le volet c (assurance-vie dont le souscripteur est distinct de l'assuré, 750 ter, 757 B, 990 I). L'orientation « successions » inclut expressément les prélèvements sur les capitaux d'assurance-vie dénoués par décès. C'est à l'auteur de trancher.
  - L'exonération des transmissions dont l'auteur est décédé reste totale.
- **RT-DOMTS-01.** Ajouter un 3° au II de L131-7 (pas de compensation par l'État) ou inscrire la compensation en loi de finances est un choix budgétaire. L'orientation le réserve : « examiner séparément les obligations de compensation et les lois financières nécessaires ». La qualification de « contribution affectée » n'est pas établie, et le véhicule (LFSS) relève d'une disposition non codifiée.
- **RT-P1-CGI-C-03.** L'objection laisse expressément le choix à l'auteur : réduire les attributions de compensation, ou faire supporter la perte d'IFER et de taxe additionnelle par l'EPCI.
- **RT-P1-CGI-C-06.** Ne sont pas réécrits : le cahier des charges de 1993, le deuxième alinéa de 242 octies de l'annexe II et la reprise CIBS L. 216-48 (hors corpus).

## Demandes à d'autres groupes

- **A1, CGI 119 ter.** Les deux versions (jusqu'au 1er janvier 2027 et à partir de cette date) reçoivent un 6 (RT-DOMIS-06). La version 2027 est à reporter avec RT-FUTFISC-01.
- **Non attribué, annexe IV 50 sexies C.** Ajouter un alinéa qui le limite aux spectacles antérieurs. Le V de 50 sexies B produit déjà cet effet ; cette demande est une coordination de sécurité.
