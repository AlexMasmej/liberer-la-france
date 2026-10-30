# M06 : cinquième balayage (S1c, S8c, S17), annexe III du CGI, décisions

J'ai lu la production en lecture seule le 29 octobre 2026, avec `CITE_PRODUCTION=1 python3 -I tools/cite.py` et SQLite en `mode=ro` (états, liens LEGI et versions des articles cités). Les exports sont dans `evidence/cited/production-20261029/`. Rien n'a été écrit en production.

Le paquet `audit/sweeps/packet-M06.json` compte 46 articles de l'annexe III et 54 pistes : 39 S1c, 8 S8c et 7 S17. Le détail de chaque piste, avec sa citation et son identifiant LEGIARTI, est dans `audit/sweeps/M06.json`.

## Bilan

| Qualification | S1c | S8c | S17 | Total |
|---|---|---|---|---|
| G | 0 | 6 | 0 | 6 |
| m | 0 | 2 | 7 | 9 |
| déjà réglé | 0 | 0 | 0 | 0 |
| faux positif | 39 | 0 | 0 | 39 |

J'ai fait **6 corrections**, une par défaut G :
- 3 dans `apply/M06` ;
- 2 dans la variante `apply/Y16mf` ;
- 1 dans la variante `apply/Y17mf`.

Je n'ai fait aucune demande à un autre groupe (`requests` vide). Rien n'est écarté (`skipped` vide).

**Contrôle.** `python3 -B apply/check_changes.py` donne `problems` vide pour les trois dossiers :
- M06 : 3 lignes construites et validées ;
- Y16mf : 2 lignes construites et validées ;
- Y17mf : 1 ligne construite et validée.

Les diagnostics sont attendus : `explicit_normative_reduction` sur les six lignes, et `length_change` sur les abrogations et sur 49 septies ZH.

## Pistes S1c (39) : toutes des faux positifs

- **CRL** (375, 377, 378, 380, 381 ; 46 C, 40 A, 38) : textes bornés aux recettes perçues avant la suppression, conformes à 234 nonies proposé. Les notes de 375 à 381 disent encore « hors lot » des coordinations de 234 duodecies, terdecies et quaterdecies qui sont faites : m F10 sur des articles que je ne modifie pas, donc non corrigé.
- **Frais de poursuite 1912** (416, 382, 382 B) : 1912 n'y est cité que pour interdire les frais et fixer la bascule.
- **« 199 »** (46 AI bis, bis A, bis B, ter, quater, quinquies A, quinquies-0 A, sexies, septies) : erreur de lecture de l'outil, qui a pris « 199 » dans « 199 terdecies-0 … ». Une vérification par expression régulière ne trouve aucun renvoi à 199 seul.
- **Autres transitions alignées** :
  - 313-0 BR (990 D) ;
  - 255 (1529, 1605 nonies, « le cas échéant ») ;
  - 344 G nonies (990 I) ;
  - 344 GD (302 bis ZL, ZN) ;
  - 46 quater-0 ZH (39 B : les amortissements différés des exercices anciens restent à suivre) ;
  - 344 I-0 bis (1679 septies) ;
  - 350 quindecies (1018 A, 805, 808) ;
  - 54, 55 et 344 N (235 ter ZG) ;
  - 281 N (650).

## Pistes S8c (8) : base légale éteinte

| Article | Cible éteinte | Qualification | Suite |
|---|---|---|---|
| 46 AZA septies (M06) | 200 quaterdecies, PERIME au 2026-07-01 | G F3 | Abrogation (`full_repeal`). La définition BBC 2005 est conservée pour les crédits afférents aux intérêts payés avant cette date. |
| 178-0 bis B (M06) | 520 A, ABROGE au 2022-01-01 (ordonnance 2021-1843) | G F3 | Abrogation, comme 178-0 bis voisin (AUDIT3-Q196). Les périodes antérieures restent régies par leurs règles, avec la déduction de pertes et sans les déclarations distinctes. |
| 46 quater-0 W (M06) | 220 quater, ABROGE au 2026-02-21 | G F3 | Retrait de l'alinéa sur l'attestation du crédit de rachat. 220 quinquies en vigueur ne cite plus 220 quater. Le substantive_impact est mis à jour. |
| 46 AZA sexies (Y16 → Y16mf) | 200 quaterdecies, PERIME | G F3 | Abrogation. Les crédits antérieurs restent régis par leurs règles, avec la dispense des pièces de chantier déjà décidée. |
| 111-0 D (Y16 → Y16mf) | 407, ABROGE au 2025-07-01 (ordonnance 2023-1210) | G F3 | Renvoi mort retiré (« prévue à l'article 407 du code général des impôts »). La période de calcul ne change pas. Les citations du substantive_impact sont mises à jour. |
| 49 septies ZH (Y17 → Y17mf) | 199 ter L, 220 N, 244 quater M, ABROGE au 2026-02-21 | G F3 | Premier alinéa limitant l'article aux crédits restant légalement ouverts, sans formalité nouvelle ni réouverture du crédit. |
| 406 undecies | 575 C, ABROGE au 2024-01-01 | m F10 | Texte déjà borné aux créances restant dues. Seule la note « non retrouvé » est fausse. Non corrigé. |
| 46 quater-0 ZL | 44 octies, ABROGE au 2022-01-01 | m | Mention résiduelle dans le 8, sans effet : aucune fraction n'est calculée au titre de 44 octies. Non corrigé. |

Dans chaque article corrigé, j'ai aussi rectifié les notes qui disaient la cible « absente du corpus ».

## Pistes S17 (7) : requalification

Avec le critère de l'audit, les sept pistes restent **m**. Aucune n'est corrigée, car je ne modifie pas ces articles :
- **41-0 A bis A, 49 septies ZZG, 46 ter A** : seules les notes sont périmées ; le texte normatif est sans défaut.
- **38 sexdecies JE** : asymétrie de délai d'option et de renonciation, sans contradiction avec 69.
- **344 O** : imprécision sans effet normatif.
- **322 G** : la voie fondée sur les seuls emplois n'est pas expressément prévue par 1465. Mais le « notamment » de 1465 laisse une marge, et sans agrément l'exonération se limite aux bases nées d'immobilisations nouvelles. C'est une faveur décidée par le projet ; l'ajustement de 1465 reste un choix pour l'auteur.
- **46 quater-0 ZK** : dépend de l'architecture de l'IS à la distribution (53 A, 223, 223 A, 223 Q). Cet arbitrage revient à l'auteur.

## Points pour l'auteur

- **Articles hors paquet qui citent encore une base éteinte.** Ils sont déjà dans d'autres paquets du balayage :
  - 178-0 bis A et 49 septies ZC, ZE, ZF et ZG (paquet M05) ;
  - 50 septies de l'annexe IV (paquet M07).

  Je ne les ai pas modifiés.
- **49 septies ZH.** La portée exacte des crédits encore ouverts dépend des dispositions transitoires de la loi n° 2026-103 du 19 février 2026. Cette loi n'est pas au corpus et je ne l'ai pas lue au JORF.
- **Sources de fin de vigueur.** Le décret n° 2026-562 (péremption de 200 quaterdecies) et les ordonnances n° 2021-1843 et n° 2023-1210 ne sont connus que par les états et liens LEGI. Le CIBS est hors corpus : je n'ai pas vérifié l'existence de régimes équivalents (taux réduits des bières, déclaration de récolte).

Revue IA : rien de ceci ne vaut validation par un juriste.
