# Réexamen CGI : instantané 20261026T230545Z → 20261027T044303Z

Groupe CGI. 18 objections issues des dossiers P1-CGI-C, P1-CGI-B, RESINT et INUT. Revue par IA, qui ne vaut pas validation par un juriste. Les conclusions restent provisoires : la seconde passe est arrêtée (`blocked`) et peut reprendre le 2 novembre.

## Méthode

- Chaque objection a été relue en entier dans `reports/register.json`.
- Pour chaque article du paquet et de l'objection, j'ai comparé l'ancien export (`evidence/cited/20261026T230545Z/`) et le nouveau (`cite.py`, `evidence/cited/20261027T044303Z/`) sur la proposition, le motif et les notes, en texte intégral.
- J'ai aussi comparé les deux manifestes (`manifests/*.json`) pour repérer les articles touchés indirectement.
- J'ai relu en plus 654, dont la nouvelle rédaction règle en partie RT-P1-CGI-C-11.
- J'ai vérifié ponctuellement en SQL, en lecture seule, 1519 A, 1609 nonies C, 1649 quater B quater et CSS L131-8.
- Aucun script de production n'a été lancé.

## Verdicts

| Objection | Ancienne priorité | Verdict | Nouvelle priorité | Point clé |
|---|---|---|---|---|
| RT-INUT-01 | P1 | maintenue | P1 | Seules les notes de 302 D bis changent ; elles confirment la contradiction avec 50-0 H, qui est inchangé. |
| RT-INUT-04 | P1 | maintenue | P1 (à confirmer) | Le III de 302 D bis garde « sur le seul fondement du présent article » ; l'article reste ABROGE_DIFF. |
| RT-P1-CGI-B-01 | P1 | maintenue | P1 | Les notes de 1406 bis traitent l'urbanisme, mais ni CCH L433-2 ni L302-1, qui sont inchangés. |
| RT-P1-CGI-C-01 | P1 | **résolue** | — | 1635-0 quinquies est désormais abrogé à la même bascule, avec une clause de non-rétablissement et le maintien des années anciennes. |
| RT-P1-CGI-C-02 | P1 | **résolue** | — | 1519 G rend expressément non exigibles la déclaration de 1649 A quater et l'amende du VI de 1736. |
| RT-P1-CGI-C-03 | P1 | maintenue | P1 (à confirmer) | 1609 nonies C est inchangé ; le XI de 1379-0 bis renvoie les attributions de compensation à « leurs règles propres » sans trancher. |
| RT-P1-CGI-C-05 | P1 | **résolue** | — | 750 ter fige la définition de 990 D « dans leur rédaction en vigueur la veille ». |
| RT-DOC-04 | P2 | maintenue | P2 | Aucune pièce extérieure ajoutée (LPF L. 23 C, codes des assurances et de commerce, 1002/1003). |
| RT-INUT-06 | P2 | maintenue | P2 | EUR-Lex toujours vide (nouvel essai le 26/10/2026, non contourné). |
| RT-INUT-07 | P2 | maintenue | P2 | Transitions toujours hétérogènes ; numéros IN/UT et arrêté de 2005 non traités. |
| RT-P1-CGI-B-04 | P2 | maintenue | P2 | 56 AJ est inchangé ; la note de 568 confirme le défaut. |
| RT-P1-CGI-B-05 | P2 | reformulée | P2 | 1519 exclut désormais le relevé nominatif ; il reste à borner ou abroger 121 sexies (annexe IV). |
| RT-P1-CGI-B-07 | P2 | reformulée | P2 | 1379, 1379-0 bis, 1586 et 1647 sont bornés ; restent 1639 A quater et 1640 (article 108 et 1406 bis), 1649 quater B quater VII et CSS L131-8 6°. |
| RT-P1-CGI-C-08 | P2 | reformulée | P2 | 1379, 1379-0 bis, 1586 et 1609 quinquies C sont bornés ; reste le seul 1609 nonies C I bis. |
| RT-P1-CGI-C-09 | P2 | **résolue** | — | 990 E est borné et son motif corrigé ; 990 G est réécrit, avec la non-déductibilité résiduelle. |
| RT-P1-CGI-C-10 | P2 | **résolue** | — | 1599 quater C limite le renvoi au VII de 231 ter aux années où la taxe reste due. |
| RT-P1-CGI-C-11 | P2 | reformulée | P2 | 654 rend inopposables les restrictions réglementaires de lieu ; reste à nettoyer 281 N (et 281 E et 60 A). |
| RT-P1-CGI-C-13 | P2 | maintenue | P2 (à confirmer) | Toujours aucun chiffrage du ratio d'autonomie financière ; le cumul des suppressions apparaît plus large que la liste initiale. |

**Totaux :** 9 maintenues, 4 reformulées, 5 résolues, 0 obsolète.

**Priorités :** aucun changement de niveau. Sur les 7 objections P1, 3 sont résolues (C-01, C-02, C-05) et 4 restent ouvertes (INUT-01, INUT-04, B-01, C-03).

**Doublon :** le volet IFER de 1609 nonies C n'est plus compté que sous C-08, et non plus aussi sous B-07.

## Vérification des résolutions (pas d'effet nouveau)

- **C-01.** Les années anciennes conservent revalorisation, exonérations, affectations et recours. La désindexation abandonnée ne fait perdre aucune faveur, puisqu'elle ne devait s'appliquer qu'à compter de la même bascule. Aucune formalité n'est créée.
- **C-02.** Les dispenses déclaratives des années anciennes sont expressément réservées. Le toilettage de 1649 A quater et de 1736 VI est facultatif.
- **C-05.** Le texte source du 2° est rétabli et le 3° est rectifié (« situés en France ou hors de France »). Aucune faveur n'est perdue.
- **C-09.** La dispense de répétition des années anciennes est préservée, et la non-déductibilité des taxes anciennes est maintenue même en cas de paiement tardif.
- **C-10.** Les définitions utiles à 1384 F sont réservées. Le décalage de bascule avec 231 ter est désormais assumé dans les notes ; le porter au motif relève de la lisibilité.

## Constats nouveaux

- **RT-RXCGI-01 (P2, anomalie d'inventaire).** Les relectures de seconde passe sont asynchrones et ont laissé des notes périmées.
  - Les notes de 1519 D, E, F, H, HA, 1599 quater A et B et 1599 bis décrivent encore un 1635-0 quinquies qui « conserve sa liste et l'indexation ». Il est pourtant abrogé.
  - Les notes de 1379, 1379-0 bis et 1609 quinquies C se renvoient mutuellement des coordinations qui sont déjà faites.
  - Correction : mettre à jour ces notes. La seule coordination restante de cette chaîne est 1609 nonies C.
- **RT-RXCGI-02 (P2, anomalie d'inventaire).** Le triage classe l'alerte 1640 → 1406 bis (cd41f0cf…) en « reference_gone », alors que le renvoi subsiste à l'identique au II 1° b et n'est neutralisé par aucune clause. Le bucket se déduit à tort d'un simple changement du renvoyeur. Cette alerte doit être requalifiée en « live ».

## Alertes liées (63 identifiants uniques)

- **52 alertes écartées.** Les renvois sont désormais bornés ou neutralisés : 1635-0 quinquies, 1649 A quater, 750 ter, 1379, 1379-0 bis, 1586, 1609 quinquies C, 990 E, 1647 et 231 ter.
- **11 coordinations manquantes maintenues :**
  - 1609 nonies C : 9 alertes ;
  - 1640 → 1406 bis : 1 alerte ;
  - 121 sexies → 1519 : 1 alerte.
- **Lecture non intégrale.** Pour 1609 nonies C, 1647 et 231 ter, le classement repose sur la lecture intégrale de la cible et sur des passages ciblés du renvoyeur. `read_in_full` vaut donc `false` pour ces alertes.

## Couverture réelle et limites

**Lu en entier (ancien et nouveau) :**
- 302 D bis, 1406 bis, 1635-0 quinquies, 1519 D, E, F, G, H, HA et HB, 1599 quater A, A bis, B et C, 1379-0 bis, 1519 I, 1649 A quater, a3 328 P ;
- 750 ter, 990 D, 990 E, 990 G, 991, 1586 octies, 1600, 990 I, 755, 806 ;
- 568, a4 56 AJ, 1519, a4 121 sexies, 1379, 1586, 1609 quinquies C, 1639 A quater, 1640 ;
- 1635 bis AH, 1609 sexdecies C, 1599 bis, 1519 C, 650, 654, a3 281 N, 1609 G, 1609 H, 1595 bis.

**Partiellement lus :**
- 1647 : passages relatifs aux III bis, VIII, IX et XIX ;
- 1609 nonies C : texte inchangé ; empreinte vérifiée et passages V, I bis et X relus.

**Contrôlés par empreinte seulement, car inchangés :** a4 50-0 H et 50-0 G, a3 111-0 E et F, a2 289, CCH L433-2 et L302-1, urbanisme L151-*, 1736, 231 ter, 1649 quater B quater, CSS L131-8 et L241-2, et les articles travail, CCH et urbanisme de RT-DOC-04.

**Non lus :**
- 281 E (a3) et 60 A (a4), seulement signalés ;
- textes extérieurs : CIBS, LPF, CGCT, arrêté de 2005, directive 92/83/CEE.

**Observation :** la version future de 1519 A (2027, sans proposition) relève de RT-FUTFISC-07 et 32. Je ne l'ai pas dupliquée.
