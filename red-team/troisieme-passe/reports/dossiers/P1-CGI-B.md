# Dossier P1-CGI-B — qualification des alertes « renvoi vers une abrogation proposée » (cibles du CGI)

*Rapport rédigé par l'agent P1-CGI-B et enregistré par le coordinateur. L'outil d'écriture de l'agent a refusé le fichier .md ; le JSON et le fichier de classification ont été écrits par l'agent lui-même. Le tableau de périmètre du § 2 est conservé à part, dans `reports/p1-work/P1-CGI-B-perimeter.md` (160 lignes).*

- Instantané : `20261026T230545Z`. Droit de référence : 18 octobre 2026. Audit d'origine : `global-reference-audit-20261025T2341Z`.
- Revue IA indépendante du 26 octobre 2026. Elle est **provisoire**, car la seconde passe continue et plusieurs propositions lues sont encore « pending ». **Elle ne vaut pas validation par un juriste.**
- Livrables : `reports/dossiers/P1-CGI-B.json` (10 objections, avec les champs `proposed_text` et `finding_ids`) et `reports/p1-work/P1-CGI-B-classification.jsonl` (147 lignes).

## 1. Résultat en bref

- **147 alertes** dans 43 clusters, un par cible du CGI proposée à l'abrogation. Toutes ont été lues en entier ; aucune n'est « non examinée ».
- **112 alertes écartées** : le renvoi est borné, ou historique par nature, ou neutralisé par la clause de la cible. **1 faux positif** : R121-11 du CCH vise le décret GBCP n° 2012-1246. **1 alerte couverte par un autre dossier** : annexe II 289, traitée dans le dossier INUT.
- **33 alertes** alimentent **10 objections** : 2 P1 et 8 P2 ; 9 sont confirmées, 1 reste à confirmer. RT-10 est un constat hors alerte.
- **Aucune P0.** Les cibles prévoient presque toutes une transition soignée et une clause « aucun renvoi ne peut rétablir ». Le risque tient donc à des **textes accessoires qui font survivre des formalités**, et à la **disparition d'une définition utilisée hors du champ fiscal** : la zone tendue de 1406 bis.

## 2. Périmètre réellement lu

L'agent a lu en entier les 146 articles distincts, soit 43 cibles et les textes qui y renvoient. Pour chacun : source, NOTA, bornes, état, proposition, motif, et notes de revue pour les cibles. La source a été lue si l'article est retenu inchangé, la proposition s'il est réécrit. Tous ont été exportés par `tools/cite.py`, avec leurs empreintes. Seules les versions visées par les alertes ont été lues, pas les versions historiques des mêmes numéros. Le tableau complet figure dans `reports/p1-work/P1-CGI-B-perimeter.md`.

## 3. Méthode

1. Lecture entière de la proposition d'abrogation de chaque cible : date de bascule, stock ancien conservé, clauses de neutralisation des renvois.
2. Lecture entière du texte qui porte le renvoi, avec vérification de l'identité de la cible.
3. Grille de qualification :
   - **écartée** : renvoi borné, historique, plage d'articles, ou règle accessoire sans effet pour l'avenir ;
   - **coordination manquante** : texte accessoire (affectation, perception, sanction, etc.) qui présente encore comme vivant un prélèvement supprimé ;
   - **incohérence du projet** : texte réécrit ou retenu qui fait encore vivre, pour l'avenir, une formalité supprimée ;
   - **risque juridique** : champ temporel ambigu, avec un effet possible sur une créance.
4. Priorités : une formalité entière maintenue, ou la perte d'une faveur, donne P1. Une donnée superflue ou un renvoi neutralisé donne P2.
5. Une objection par effet juridique.

## 4. Qualification cluster par cluster

| Cluster | Cible | Alertes | Écartées | Autres qualifications |
|---|---|---|---|---|
| c00 | CGI 234 nonies | 18 | 17 | 1 incohérence → RT-03 |
| c01 | CGI 1406 bis | 11 | 6 | 3 coordinations → RT-07 ; 2 incohérences → RT-01 |
| c02 | CGI 39 B | 8 | 8 | — |
| c03 | CGI 1912 | 8 | 8 | — |
| c04 | CGI 1519 E | 8 | 2 | 1 incohérence → RT-06 ; 5 coordinations → RT-07 |
| c05 | CGI 1599 quater A | 8 | 7 | 1 incohérence → RT-06 |
| c06 | CGI 568 | 7 | 2 | 1 couverte par dossier (302 D bis / 289) ; 2 incohérences → RT-04 ; 2 coordinations → RT-07 |
| c07 | CGI 235 ter ZD | 7 | 4 | 3 coordinations → RT-08 |
| c08 | CGI 235 ter ZG | 6 | 6 | — |
| c09 | CGI 289 E | 5 | 2 | 3 incohérences → RT-02 |
| c10 | CGI 1519 | 4 | 3 | 1 incohérence → RT-05 |
| c11 | CGI 1519 HB | 4 | 2 | 1 incohérence → RT-06 ; 1 coordination → RT-07 |
| c12–c16 | 1607 ter, 1529, 302 bis ZL, 1518 B, 1599 quater D | 3–4 | toutes | — |
| c17 | CGI 223 sexies | 3 | 0 | 3 risques juridiques → RT-09 |
| c18–c22, c24, c25, c27–c35, c37–c40 | divers | 1–2 | toutes | — |
| c23 | CGI 209-0 A | 2 | 1 | 1 coordination → RT-08 |
| c26 | CGI 1635 bis AH | 2 | 1 | 1 coordination → RT-07 |
| c36 | CGI 222 bis | 1 | 0 | 1 coordination → RT-08 |
| c41 | CGI 1609 sexdecies C | 1 | 0 | 1 coordination → RT-07 |
| c42 | CGI 222 | 1 | 0 | 1 faux positif |

Les motifs détaillés de chaque alerte figurent dans le fichier de classification.

## 5. Objections

- **RT-P1-CGI-B-01 (P1, incohérence du projet, confirmée).**
  - L'abrogation de 1406 bis fait disparaître la définition de la zone tendue (1° du B du I, liste fixée par décret).
  - Les textes d'urbanisme (L151-22, L151-36-1, L151-14-1) figent cette liste. CCH L433-2 et L302-1 y renvoient au contraire comme à une norme vivante.
  - Enjeu : une faveur que le projet veut conserver, la vente de 30 % d'un programme HLM à des personnes privées.
- **RT-P1-CGI-B-02 (P1, incohérence du projet, confirmée).**
  - Le flux de facturation électronique supprimé par 289 E survit dans trois textes :
    - 242 nonies E 7° et 8° de l'annexe II, retenu inchangé ;
    - 41 septies H de l'annexe IV, réécrit ;
    - l'amende de 1737 IV (50 € par facture, plafond de 45 000 €).
  - *Fusionnée par le coordinateur* avec P1-ANNEXES et P1-CGI-A (groupe E-INVOICING, `reports/dedupe.json`).
- **RT-03 (P2).** Annexe III 40 A h : la donnée CRL est maintenue pour l'avenir.
- **RT-04 (P2).** Annexe IV 56 AJ : la déclaration du droit de licence, pourtant supprimé, est reconstituée.
- **RT-05 (P2).** Annexe IV 121 sexies : le relevé nominatif minier est maintenu, avec une collecte de données personnelles sans finalité.
- **RT-06 (P2).** 1635-0 quinquies institue encore l'IFER alors que ses composantes sont supprimées. *Fusionnée avec RT-P1-CGI-C-01, qui est P1.*
- **RT-07 (P2).** Accessoires non bornés : 1379, 1639 A quater, 1640, 1379-0 bis, 1586 4°, 1609 nonies C, 1649 quater B quater VII, CSS L131-8 6°, 1647 III bis et IX.
- **RT-08 (P2).** Sanctions qui visent des obligations supprimées : 1788 C, 1729 B, 1763 C.
- **RT-09 (P2, risque juridique, à confirmer).** La CEHR reste-t-elle due sur les plus-values en report qui expirent après sa suppression (200 A 2 ter b) ? C'est à l'auteur de choisir.
- **RT-10 (P2, constat hors alerte).** 234 duodecies maintient un acompte CRL limité, alors que 234 terdecies et les articles 376, 379 et 381 bis de l'annexe III le suppriment. La loi contredit son décret.

## 6. Propositions de correction

Les textes complets sont dans le champ `proposed_text` du JSON. En résumé :
- **6.1 CCH L433-2 et L302-1** : figer la zone, comme l'urbanisme, sans rétablir la taxe.
- **6.2 Facturation électronique** :
  - abrogation des 7° et 8° de 242 nonies E, avec un alinéa interdisant de conditionner l'immatriculation à ces services ;
  - abrogation de 41 septies H ;
  - 1737 IV borné, avec application de la loi répressive plus douce.
- **6.3 à 6.5** : bornes temporelles pour 40 A h, 56 AJ et 121 sexies.
- **6.6** : clause de non-rétablissement dans 1635-0 quinquies, ou abrogation de l'article si toutes les composantes disparaissent.
- **6.7** : clause type pour les accessoires, et bornage des délibérations de 1406 bis.
- **6.8** : bornage des sanctions.
- **6.9** : option A (maintien assumé) ou option B (extinction).
- **6.10** : alignement de 234 duodecies sur 234 terdecies.

## 7. Incertitudes et éléments non examinés

- **Réserves documentaires** : plusieurs sources sont en ABROGE_DIFF au 1er janvier 2027, 2028 ou 2029, avec une reprise possible dans le CIBS. *Le coordinateur précise que ces versions futures existent dans l'instantané et sont traitées par RT-XCUT-01 / RT-INV-05 et par le paquet FUT-FISC.*
- **Sources non consultées** : Légifrance et EUR-Lex. Les principes DDHC 8, CRPA L243-2 et RGPD art. 5 ont été cités de mémoire.
- **Occurrences voisines non signalées par l'audit** : 1379 I 6°, 1736 V et VI, 39 1 2°, 242 nonies E 6° c, 289 bis I et VI.
- **Non examinés** : l'autonomie financière des collectivités (art. 72-2), les formulaires, le LPF.
- **Seconde passe** : plusieurs cibles sont encore « pending ». Il faut confronter les empreintes du JSON à l'état courant avant toute intégration.
