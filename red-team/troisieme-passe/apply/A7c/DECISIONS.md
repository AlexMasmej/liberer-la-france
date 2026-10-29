# Groupe A7, variante A7c : décision de l'auteur appliquée

L'auteur a délégué la décision au coordinateur : RT-DOMIS-07 et RT-DOMSUCC-01 sont appliquées, mais pas la partie annuelle de RT-DOMIS-02. A7c reprend donc la version complète `apply/A7/` sans aucune trace de cette partie annuelle. Les dossiers `apply/A7/` et `apply/A7b/` sont restés intacts.

Textes lus dans l'instantané `20261029T034912Z`.

Contrôle : `python3 -B apply/check_changes.py A7c` construit et valide 22 changements ; `problems` est vide. Le 22e est une phrase de notes ajoutée à 223 B (voir ci-dessous). Il reste quatre diagnostics de longueur (1668, 205 C, 205 D, 216) et un renvoi modifié (L302-1). Ils existaient avant les corrections.

Revue IA : rien de ceci ne vaut validation par un juriste.

## Changements de la seconde passe après l'instantané

Entre 04 h 03 et 04 h 14 UTC, après l'instantané final de 03 h 49, la seconde passe a modifié 49 articles en production. J'ai lu la production en lecture seule et l'ai comparée à l'instantané.

**Articles de A7c concernés.** Pour CGI 219, 216, 209 B et 223 B, A7c part désormais des textes actuels de la production. Les motifs et notes nouveaux de l'autre IA sont repris en entier ; mes ajouts viennent après.
- 209 B : la proposition ne diffère que par l'encodage des apostrophes (`&#x27;`) ; c'est cette version de production qui est reprise.
- 223 B (attribué à A7) : sa proposition a changé, pour une correction favorable de renvoi (« deuxième ou de la troisième phrase »). Ses nouvelles notes jugent encore « utile » d'harmoniser 209 XI 3 et 223 I. J'ajoute seulement une phrase de notes signalant que cette harmonisation est faite (RT-DOMIS-04) ; son corps de production est repris tel quel.
- Les autres articles de A7c n'ont pas changé depuis l'instantané. Le contrôle confirme que chaque motif et chaque note part du texte actuel de la production. Seules exceptions : les motifs de 784 C et de 38 quindecies A, réécrits volontairement.

**Autres articles modifiés.**
- 212 bis (attribué à A7) n'est pas touché par A7c. Ses nouvelles notes confirment que le IV de 223 A prime sur 209 XI 3 et 223 I, ce qui va dans le sens de RT-DOMIS-04.
- 207 (A1) : sa proposition est inchangée. Ses nouvelles notes rappellent que les dérogations HLM du 4° du 1 de l'article 207 écartent 111 bis et la seconde condition de 221 bis. Pour ne pas retirer cette faveur, le 1 bis du V de 219 (RT-DOMIS-07) précise désormais qu'il « ne peut entraîner une imposition que les dérogations du 4° du 1 de l'article 207 écartent ». La même règle figure déjà au 7 de 221.
- 208, 209-0 B, 210-0 A, 217 octies, 223 D, 44 duodecies à quindecies, 125 A, 125 D, 125 ter, 167 bis, 199 septvicies et 199 undecies F : leurs changements sont des relectures de concordance ou des retouches propres à ces régimes. Aucun ne règle ni ne modifie RT-DOMIS-01, 03, 04, 05 ou 07. Ils ne sont pas touchés ; ceux qui n'appartiennent pas à A7 restent à leurs groupes.
- Les autres articles de la liste relèvent du code du travail et de l'annexe II. Je n'ai examiné que l'indication de quels champs avaient changé (motifs et notes seulement), sans en lire le contenu ; ils sont hors du périmètre de A7.

## Ce qui a été retiré par rapport à A7

- **219** : le a du 1 bis (charges financières nettes non déductibles taxées chaque année) est supprimé. Le 1 bis ne contient plus que la règle de sortie de l'IS : « 1 bis. Par exception au premier alinéa du 1, les bénéfices différés non protégés […] ». Le renvoi interne devient « Le présent 1 bis ».
- **221** : ses renvois sont mis à jour en conséquence (« au 1 bis du V de l'article 219 »).
- **1668 et 206** : les renvois au « a du 1 bis du V de l'article 219 » sont retirés du texte, des motifs et des notes.
- **212 bis** : il n'est plus touché.
- **209** : la mention de la charge financière est retirée des notes.

## Décisions

| Objection | Décision | Articles touchés | Ce qui change |
|---|---|---|---|
| RT-DOMIS-01 (confirmé) | Appliquée | CGI 219 (V, 6), 1668 | Option facultative de liquidation annuelle de l'IS à 20 % pour les groupes dans le champ du minimum international. L'option s'exerce par une mention sur la déclaration et l'impôt se paie sans acompte. Le bénéfice ainsi taxé n'est pas taxé une seconde fois à la distribution. |
| RT-DOMIS-02 (confirmé) | **Non appliquée** | — | Non appliquée : rétablirait un IS annuel ; risque au regard de l'article 4 de la directive 2016/1164 (ATAD) signalé, à confirmer. |
| RT-DOMIS-03 (confirmé) | Appliquée | CGI 219 (VI, 2), 206 (12), 1668 ; notes de 205 B, 205 C, 205 D, 209 B | Les impositions correctives annuelles reçoivent un taux (20 %, ou 15 % dans la tranche PME), l'imputation des déficits et une échéance au relevé de solde, sans acompte. |
| RT-DOMIS-04 (confirmé) | Appliquée | CGI 209 (XI, 3), 223 I (II), annexe III 46 quater-0 ZJ bis ; notes de 223 L et de 223 B | Les pertes nouvelles des membres d'un groupe se compensent selon 223 A IV. |
| RT-DOMIS-05 (à confirmer) | Appliquée | CGI 216 (IV) | Les dividendes de portefeuille de l'UE, de l'EEE ou d'un pays conventionné sont protégés à proportion de l'impôt payé par la société distributrice. |
| RT-DOMIS-06 (à confirmer) | Demande à A1 | CGI 119 ter (deux versions) | Un nouveau 6, dont le texte exact figure dans `requests`. |
| RT-DOMIS-07 (confirmé) | Appliquée, `loophole_closure` (décision de l'auteur) | CGI 219 (V, 1 bis), 221 (2 et 7 a) | Les bénéfices différés d'une société qui quitte l'IS sont taxés comme une distribution ; leur montant net est ensuite protégé. La continuité de 221 bis et les régimes de 208 C et 207 sont conservés. |
| RT-DOMSUCC-01 (confirmé) | Appliquée en partie, `loophole_closure` (décision de l'auteur) | CGI 784 C, 792 bis, 792-0 bis | Une libéralité graduelle, une fiducie ou un trust dont l'auteur est vivant reste soumis aux droits de donation. Le volet assurance-vie (750 ter, 757 B, 990 I) n'est pas appliqué : l'orientation « successions » inclut ces capitaux dans l'abolition. |
| RT-DOMTS-01 (à confirmer) | Non appliquée (arbitrage) | — | La compensation et le choix de la loi de financement sont réservés par l'orientation. |
| RT-P1-CGI-B-01 (confirmé) | Appliquée | CCH L433-2, L302-1 | La zone de l'ancien 1406 bis est figée à la liste de la veille de l'abrogation. |
| RT-P1-CGI-C-03 (à confirmer) | Non appliquée (arbitrage) | — | Le choix est laissé à l'auteur. |
| RT-P1-CGI-C-06 (confirmé) | Appliquée | Annexe IV 50 sexies B ; notes de 290 quater ; demande pour 50 sexies C (non attribué) | La billetterie fiscale est supprimée pour les spectacles futurs. |
| RT-P1-CGI-C-07 (confirmé) | Appliquée | Annexe III 38 quindecies A (`full_repeal`) | Abrogation à la même date que 54 octies. |
