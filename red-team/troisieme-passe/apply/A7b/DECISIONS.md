# Groupe A7, variante A7b : corrections sans hausse d'impôt par rapport au projet

Cette variante a été demandée par le coordinateur. Elle reprend toutes les corrections du groupe A7, sauf les trois mises en attente d'une décision expresse de l'auteur. La version complète reste intacte dans `apply/A7/`.

- Textes lus dans l'instantané `20261029T034912Z`.
- Contrôle : `python3 -B apply/check_changes.py A7b` construit et valide 17 changements ; `problems` est vide.
- Les seuls diagnostics (changement de longueur de 1668, 205 C, 205 D et 216 ; renvois modifiés de L302-1) existaient avant les corrections.
- Revue IA : rien de ceci ne vaut validation par un juriste.

## Corrections reprises

Les articles 219, 1668 et 206 sont réécrits en entier sans les ajouts propres aux corrections en attente :
- pas de 1 bis au V de 219 ;
- aucun renvoi à ce 1 bis dans 1668 et 206 ;
- motifs et notes expurgés.

| Objection | Décision | Articles touchés | Ce qui change |
|---|---|---|---|
| RT-DOMIS-01 (confirmé) | Appliquée | CGI 219 (V, 6), 1668 (premier alinéa) | Option facultative de liquidation annuelle de l'IS à 20 % pour les entités dans le champ du minimum international. L'option s'exerce par une mention sur la déclaration existante et l'impôt se paie sans acompte. Le bénéfice ainsi taxé va au compte protégé et ne supporte pas de second IS à la distribution. |
| RT-DOMIS-03 (confirmé) | Appliquée | CGI 219 (VI, 2), 206 (12), 1668 ; notes de 205 B, 205 C, 205 D et 209 B | Les impositions correctives annuelles (205 B IV, 205 C, 205 D, 209 B V) reçoivent : un taux de 20 %, ou 15 % dans la tranche PME, au lieu de 25 % ; l'imputation des déficits ; une échéance au relevé de solde, sans acompte. |
| RT-DOMIS-04 (confirmé) | Appliquée | CGI 209 (XI, 3), 223 I (II), annexe III 46 quater-0 ZJ bis ; notes de 209 et de 223 L | Les pertes nouvelles des membres d'un groupe se compensent selon le IV de 223 A. C'est la faveur que le projet maintient ; la contradiction entre lots disparaît. |
| RT-DOMIS-05 (à confirmer) | Appliquée | CGI 216 (IV) | Les dividendes de portefeuille de source UE, EEE ou d'un État conventionné sont protégés à proportion de l'impôt payé par la société distributrice. La correction ne fait que réduire l'impôt et ne crée aucune formalité. |
| RT-DOMIS-06 (à confirmer) | Demande à A1 | CGI 119 ter, versions LEGIARTI000031815505 et LEGIARTI000053154449 (2027) | Un 6 dispense de la condition de 10 % les sociétés de l'Union lorsqu'un résident aurait été protégé. Le texte exact figure dans `requests`. |
| RT-P1-CGI-B-01 (confirmé) | Appliquée | CCH L433-2, L302-1 | La zone de l'ancien 1406 bis est figée à la liste en vigueur la veille de son abrogation. Pour L433-2, s'y ajoutent les communes qui remplissent les critères antérieurs. Pour L302-1, aucune obligation n'est créée faute de liste. |
| RT-P1-CGI-C-06 (confirmé) | Appliquée | Annexe IV 50 sexies B ; notes de 290 quater ; demande pour 50 sexies C (non attribué) | Le nouveau V supprime la billetterie fiscale pour les spectacles futurs. Les I à IV sont conservés, ce qui garde exact le renvoi de 50 sexies C. |
| RT-P1-CGI-C-07 (confirmé) | Appliquée | Annexe III 38 quindecies A (`full_repeal`) | L'article est abrogé à la même date que 54 octies, avec la même transition. |
| RT-DOMTS-01 (à confirmer) | Non appliquée (arbitrage) | — | La question de la compensation budgétaire et de la loi de financement est réservée par l'orientation `taxe_sur_les_salaires_removal`. |
| RT-P1-CGI-C-03 (à confirmer) | Non appliquée (arbitrage) | — | L'objection laisse elle-même le choix à l'auteur. |

## Corrections en attente

Trois corrections sont en attente d'une décision de l'auteur. Elles sont absentes de `changes.json` et figurent dans `apply/A7/` :
- RT-DOMIS-02, partie annuelle ;
- RT-DOMIS-07 ;
- RT-DOMSUCC-01.

Les articles qui ne portaient que ces corrections ne figurent pas dans A7b : 212 bis, 221, 784 C, 792 bis et 792-0 bis.
