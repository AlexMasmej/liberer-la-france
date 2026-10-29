# Groupe B03 : décisions (objections P2)

Lecture : production en lecture seule (sqlite `mode=ro`, `query_only`), le 29 octobre 2026. Le registre date d'un instantané ancien : chaque objection a été confrontée au texte actuel.

Contrôle : `python3 -B apply/check_changes.py B03` donne 38 lignes construites et validées, `problems` vide. Les diagnostics restants (changements de longueur, renvois `L410-1`, `L123-221` et `L4163-1`) existaient déjà dans les propositions et ne viennent pas de ces corrections.

Tous les articles touchés appartiennent à B03, ou n'ont aucun groupe attribué : c'est le cas des 27 articles 371 de l'annexe II. Aucune variante n'a été créée et aucune demande n'a été adressée à un autre groupe.

## Appliquées

### RT-P1-ANNEXES-07 : appliquée

- **Article touché :** annexe IV, 50-0 BA.
- **Ce qui change :** l'arrêté qui fixait le formulaire, les rubriques a à g et le signalement des modifications de la déclaration de 286 O est abrogé (`full_repeal`), sans formalité de remplacement.
  - 286 O est déjà abrogé dans le projet.
  - L'abrogation prend effet à la même date que celle de 286 O, c'est-à-dire avec la loi supprimant la déclaration du 2° de 302 F ter.
- **Ce qui est préservé :** l'agrément de l'entrepositaire (302 F ter 1°), les exonérations, les créances et les recours.
- **Laissé à l'auteur :** la concordance avec le CIBS (302 F ter est en état ABROGE_DIFF).

### RT-P1-ANNEXES-08 : appliquée

- **Article touché :** annexe III, 46 quater-0 A.
- **Ce qui change :** les organismes du 5 de 206 ne produisent plus la note, l'attestation culturelle ni la copie du label prévues par 41 J, qui est abrogé. La phrase « La note […] demeure exigée » est retirée.
- **Transition :** la même que celle de 41 J, y compris pour une déclaration ou une réclamation relative à une année antérieure.
- **Ce qui est préservé :** les déductions et leurs proportions, inchangées.
- **Impact :** reclassé en `coordination_only`, sous la mesure de 41 J, pour ne pas compter deux fois la même suppression.

### RT-P1-ANNEXES-10 : appliquée

- **Article touché :** annexe IV, 56 J vicies.
- **Ce qui change :** l'arrêté d'application de 209-0 A, qui est abrogé, est lui-même abrogé. Plus aucun modèle fiscal de fiche ni aucune déclaration de paiement n'est exigé.
- **Ce qui est préservé :** les documents d'essai, de marquage et de restitution, les créances antérieures et les recours.
- **Laissé à l'auteur :** l'éventuel transfert de la garantie des métaux précieux dans un autre code (CGI 527 est abrogé au 1er janvier 2019 dans le corpus).

### RT-P1-ANNEXES-12 : appliquée

- **Article touché :** annexe IV, 50-0 E.
- **Ce qui change :** le bon de commande n'est plus désigné par renvoi à 111 J, qui est abrogé. Il devient « Le bon de commande de marques fiscales ou de capsules établi par l'entrepositaire agréé et transmis au fabricant agréé ».
- **Ce qui ne change pas :** le contenu du bon, l'absence de visa et de double exemplaire, et la traçabilité.

### RT-P1-ANNEXES-13 : appliquée

- **Article touché :** CGI 90.
- **Ce qui change :** la note éditoriale inexacte « (1) Annexe III, art. 369 à 374 » est retirée.
  - 369 et 374 portent sur la taxe sur les salaires ; 370 est abrogé ; 371 à 373 n'existent pas dans l'annexe III.
  - Aucune liste de remplacement n'est inventée : c'est la solution de repli prévue par l'objection.
- **Ce qui ne change pas :** le fond de l'article.

### RT-P1-ANNEXES-14 : partiellement appliquée

Les notes périmées de trois articles sont corrigées, sans changement du corps :

- **49 septies H :** 244 quater B proposé supprime l'agrément, et la liste des pièces se trouve à l'annexe IV 23 L duodecies, déjà abrogé pour les dépenses nouvelles.
- **209-0 A :** CGI 527 figure au corpus, abrogé au 1er janvier 2019. Le motif est corrigé sur le même point.
- **Annexe IV 124 :** CGI 1565 figure au corpus, abrogé au 1er janvier 2025.

La mention qui reprend ces notes dans `substantive_impact` est corrigée de la même façon.

Pour 371 bis H, 371 R, 371 bis B et 242 nonies E, l'objection était déjà réglée (voir plus bas).

### RT-P1-ANNEXES-05 : partiellement appliquée (notes seules)

- **Articles touchés :** les notes de 27 articles de l'annexe II : 371 A, A bis, B, C, E, EA, G, LA, LC, M, M bis, O, Q, QA, X, Y, Z bis, Z quater, Z quindecies, Z sexdecies, bis A, bis D, bis J, ter A, ter C, ter D et ter H.
- **Ce qui change :** ces notes disaient « absents du corpus » les articles 1649 quater C, E, E bis, F, G, H, K ter, L et N. Elles indiquent désormais que ces articles figurent au corpus, à l'état ABROGE depuis le 16 février 2025 (loi n° 2025-127, art. 11).
  - Elles signalent aussi les versions VIGUEUR_DIFF 2030 de 1649 quater E et H.
  - Elles signalent enfin que 164 F vicies et 164 F duovicies de l'annexe IV sont à l'état PERIME depuis 2009.
- **Ce qui ne change pas :** aucun corps n'est modifié.
- **Laissé à l'auteur :** l'abrogation d'ensemble des articles 371 A à 371 bis N, ou leur renvoi vers un nouveau fondement. Ce choix dépend de l'article 11 de la loi n° 2025-127, qui n'a pas été lu (objection « à confirmer »).

### RT-INST-04 et RT-INST-02 : appliquées

Les deux objections portent sur le même article, CSS L228-1, traité en une seule ligne.

- **RT-INST-04 :** au V, le mot « modalités » de la source est rétabli : « les modalités de nomination de son directeur… ».
- **RT-INST-02 :** la note « D224-8 dernier alinéa […] après avis de son comité exécutif : cohérent avec la tutelle du V » est remplacée par la rédaction de l'objection. La condition qu'elle posait est remplie : D224-8 et D227-5 proposés suppriment tous deux l'avis.

### RT-RXALERTS-02 : appliquée

- **Article touché :** annexe II, 317 B.
- **Ce qui change :** le troisième alinéa ne permet plus de refuser un dépôt présenté après la réforme, même pour une cession antérieure, au motif que les mentions du I ou les justificatifs des II et III manquent. Il s'aligne ainsi sur l'alinéa correspondant de 1529 proposé.
- **Ce qui est préservé :** les dettes, les exonérations et les obligations déclaratives des cessions antérieures.
- **Laissé à l'auteur :** 1605 nonies garde ce motif de refus pour les cessions anciennes. Il n'est pas modifié, car la divergence entre les deux taxes reste à confirmer.

### RT-RXTRAV-01 : appliquée

La correction est sûre quelle que soit la date des abrogations.

- **Article touché :** CSS R133-14, IV.
- **Ce qui change :** jusqu'à l'entrée en vigueur des abrogations de L1251-46, L1221-16 et L1221-18, la DSN continue de satisfaire le formulaire et les deux déclarations ; ensuite, plus rien n'est exigé, y compris pour les périodes antérieures.
- **Risque écarté :** aucune formalité séparée ne peut renaître dans l'intervalle.
- **Impact :** les transitions des trois effets correspondants sont mises à jour.

## Déjà réglées

- **RT-P1-ANNEXES-09 :** 23 L duodecies est déjà abrogé pour les dépenses nouvelles (balayage W14) : « Pour ces dépenses, aucune pièce, fiche ou copie n'est exigée au titre d'une demande d'agrément. »
- **RT-P1-ANNEXES-11 :** 146 est déjà abrogé (AUDIT3-Q222) : « Aucune déclaration, aucun engagement des signataires ni aucune autre formalité ne peut être exigé des cercles et maisons de jeux sur le fondement du présent article. »
- **RT-P1-ANNEXES-14 (partie) :** les notes de 371 bis H, 371 R, 371 bis B et 242 nonies E sont déjà corrigées.
- **RT-DOMCVAE-03 :** le texte codifié tranche déjà la question.
  - 1586 ter proposé : « sans prise en compte d'une CVAE fictive pour une année supprimée ».
  - 1647 B sexies VII : « déjà acquis ».
  - La formule « ou à acquérir » ne subsiste que dans le XXVIII C du paquet non codifié cvae-calendar, non adopté et hors corpus. Il n'est pas repris sous `uncodified`, pour éviter un doublon (même choix que le groupe A3).

## Non appliquées

- **RT-DOMCVAE-04 (arbitrage, « à confirmer ») :**
  - L'option A supprimerait une éventuelle application de la loi répressive plus douce, que le principe de nécessité des peines peut imposer de plein droit. Le champ `preserve` de l'objection l'exclut.
  - L'option B étendrait une faveur que le projet n'a pas décidée.
  - Les réserves actuelles de 1731 3 et de 1770 decies ont le même effet.
- **RT-DOMCVAE-05 (« à confirmer ») :**
  - **Déjà réglé :** 1647 B sexies VII est désormais ancré sur la date de la loi, et non plus sur 1586 ter.
  - **Écartée :** la formule unique d'ancrage, et le transfert des règles de survie de 1586 ter vers un article maintenu. Ces deux points relèvent d'une convention de rédaction propre à tout le projet : le validateur impose lui-même la forme « Le présent article est abrogé […] » suivie de règles transitoires.
  - **Écartée :** l'harmonisation des trois ancres de R133-14. Elle n'est pas sûre tant que l'unicité de la loi de réforme n'est pas établie.

## Points laissés à l'auteur

- **Régime des CGA, AGA et OMGA :** lire l'article 11 de la loi n° 2025-127, puis décider de l'abrogation ou du renvoi des articles 371 A et suivants de l'annexe II (RT-P1-ANNEXES-05).
- **CVAE :** choisir entre les options A et B pour les sanctions des années anciennes (RT-DOMCVAE-04), puis fixer la convention d'ancrage de la date de la réforme (RT-DOMCVAE-05).
- **Taxe sur les terrains devenus constructibles :** décider s'il faut aligner le motif de refus de 1605 nonies sur 1529 et 317 B (RT-RXALERTS-02).

## Résumé

| Statut | Nombre | Objections |
|---|---|---|
| Appliquées | 9 | ANNEXES-07, 08, 10, 12 et 13, INST-02, INST-04, RXALERTS-02, RXTRAV-01 |
| Partiellement appliquées | 2 | ANNEXES-05 (notes seules), ANNEXES-14 (trois articles ; les quatre autres déjà réglés) |
| Déjà réglées | 3 | ANNEXES-09, ANNEXES-11, DOMCVAE-03 |
| Non appliquées | 2 | DOMCVAE-04 (arbitrage), DOMCVAE-05 (à confirmer ; partie déjà réglée) |

Au total, 38 lignes `replace` sont prêtes ; aucune n'est une ligne `new` et aucune n'est marquée `loophole_closure`.

Revue IA, sans validation par un juriste.
