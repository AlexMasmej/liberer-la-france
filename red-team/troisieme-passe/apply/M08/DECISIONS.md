# M08 : décisions (cinquième balayage, pistes S2c et S8c du CGI)

J'ai lu le texte en production avec `CITE_PRODUCTION=1 python3 -I tools/cite.py` (exports sous `evidence/cited/production-20261029/`) et la base en `mode=ro`, sans rien écrire. J'ai consulté une source primaire : Légifrance, JORF, loi n° 2025-127, art. 48 (JORFARTI000051168626), le 29 octobre 2026. Revue IA, sans validation par un juriste.

**Décompte.** 46 articles et 67 pistes :
- 34 faux positifs ;
- 20 déjà réglées ;
- 11 m ;
- 2 G, qui se rapportent à un seul défaut.

Deux articles sont corrigés dans `apply/M08/` : 1668 B et 1731 A bis. J'ai créé les variantes A1mh, A3mh, B03mh, B04mh, B05mh et B07mh pour les articles qui ont un `previous_owner`. Aucune ne contient de correction. Toutes sont validées et `problems` est vide partout. Le détail par piste, avec les citations, figure dans `audit/sweeps/M08.json`.

## Correction appliquée : SWEEP-M08-1668B (G, F3 + F5)

| Piste | Article | Qualification | Correction |
|---|---|---|---|
| S8c vers 235 ter ZAA | 1668 B, LEGIARTI000029355581 | **G** | Oui : abrogation pour l'avenir (`full_repeal`) |
| S2c vers 1668 B | 1731 A bis, LEGIARTI000029355548 | **G** | Oui : abrogation pour l'avenir (`full_repeal`) |

- **Le constat.** 1668 B et 1731 A bis n'organisent que le paiement, le versement anticipé et la sanction de la sous-estimation de la contribution exceptionnelle de 235 ter ZAA.
  - Cette contribution ne valait que pour les « exercices clos à compter du 31 décembre 2011 et jusqu'au 30 décembre 2016 ».
  - 235 ter ZAA (LEGIARTI000029355234) est **PERIME** depuis le 1er juillet 2026, par l'article 2 du décret n° 2026-562.
  - Les propositions ajoutaient pourtant des clauses sur les « exercices ouverts à compter de l'entrée en vigueur » du régime de l'impôt sur les sociétés à la distribution. C'est un régime éteint réécrit pour l'avenir.
  - Les notes disaient aussi 235 ter ZAA « absent du corpus », ce qui est inexact.
- **La correction.** J'ai suivi la règle S8c : les deux articles cessent d'organiser le régime pour l'avenir. Ce qui est conservé :
  - les exercices clos de 2011 à 2016 restent régis par l'ancienne rédaction ;
  - pour 1668 B, la restitution de l'excédent sous trente jours, les réclamations et les recours ;
  - pour 1731 A bis, les seuils (20 %, 100 000 et 400 000 euros) et la dispense fondée sur le compte de résultat prévisionnel, sous réserve de la loi répressive plus douce ;
  - les articles 1727 et 1731 gardent leur champ.

  Cette correction ne supprime ni ne crée aucune taxe et n'institue aucune formalité de remplacement. Les deux bilans d'impact sont classés `coordination_only` et reprennent les `measure_id` existants.
- **Les vérifications.** Aucun autre article du corpus ne renvoie à 1668 B ou à 1731 A bis. La proposition de 219 parle déjà de « l'ancien article 235 ter ZAA ». La contribution de 2025 (loi n° 2025-127, art. 48, hors corpus) renvoie directement aux articles 1668, 1727 et 1731, jamais à 1668 B ni à 1731 A bis : elle n'est pas touchée.
- **Les diagnostics.** Pour 1731 A bis, le renvoi au code de commerce L. 232-2 est retiré. C'est voulu : la dispense subsiste pour les anciens exercices, par renvoi à l'ancienne rédaction.
- **Point laissé à l'auteur.** J'ai choisi l'abrogation plutôt qu'une simple limitation aux anciens exercices, qui serait l'autre option S8c.

## Pistes non corrigées (m)

| Piste | Article | Qualification | Motif |
|---|---|---|---|
| S8c vers 302 L | 302 H quater, LEGIARTI000021664269 | m (F3, F10) | Article lui-même abrogé à date différée (ordonnance n° 2021-1843, art. 10). La règle de reprise est au CIBS, hors corpus : `skipped`. Les notes disent à tort 302 L absent du corpus. |
| S8c vers 302 F bis et 302 D | 302 F ter, LEGIARTI000043829226 | m (F3, F10) | Même situation (302 F bis abrogé en 2022, 302 D en 2024). CIBS hors corpus. Notes inexactes. |
| S8c (×4) vers 564 undecies, 438, 402 bis, 520 A | 302 B, LEGIARTI000041535200 (B07, variante B07mh) | m | Version sans brouillon, dans une section close : anomalie d'inventaire déjà signalée (RT-INV-14). Décision du coordinateur. |
| S8c vers 302 L | 302 M, LEGIARTI000042623631 | m | Sans brouillon, hors inventaire (RT-INV-14). Conflit de la source. |
| S8c vers 327 | 302 M bis, LEGIARTI000036365498 | m | Sans brouillon, hors inventaire (RT-INV-14). |
| S8c vers 302 M ter | 441, LEGIARTI000031781361 | m | Sans brouillon, section close au 1er juillet 2025 (RT-INV-14). |
| S8c vers 244 quater Q | 217 duodecies, LEGIARTI000042912650 | m | Clause d'adaptation qui cite des mots que 199 undecies B formule désormais par renvoi au code de la consommation. Elle reste intelligible et sans effet opératoire. |

## Pistes déjà réglées (20)

Dans chacun de ces cas, la proposition actuelle limite déjà la sanction ou le renvoi aux obligations qui subsistent, ou aux périodes anciennes :
- 1693 bis → 302 bis MB ;
- 1649 A quater → 1519 G ;
- 1788 C → 235 ter ZD (B05, variante B05mh) ;
- 1740-0 B → 242 quater ;
- 1731 → 1679 septies (B03, variante B03mh) ;
- 1766 → 1649 AA ;
- 1759 → 240 ;
- 150-0 C → 39 quinquies H ;
- 1738 → 1649 quater B quinquies ;
- 1731 A → 219 et 1668 ;
- 1740-00 AB → 242 septies ;
- 1740 A → 200 ;
- 1649 A ter → 1599 quater A ;
- 1729 B → 238 bis, 244 quater B et 222 bis (B04, variante B04mh) ;
- 1731 ter → 242 bis ;
- 1743 → 1741 et 199 undecies A.

## Faux positifs (34)

Ce sont :
- des renvois à des subdivisions conservées par la cible réduite (157 7°, 792 bis, 1378 octies III 2 et 3, 187, 1672 2, 1731 1, 1679 quinquies, 243 bis, 158, 204 J, 197 A, 199 unvicies, 150-0 A, 200 quater, 1650, 1406, 204 I, 50-0, 69, 1737, 223 A) ;
- des renvois à un autre code ou à une annexe (code civil 274, code de procédure civile 485, annexe IV 50 quaterdecies-0 A bis, piste « 199 » pour 199 terdecies-0 A) ;
- des renvois historiques nécessaires (1640 B → 1599 quinquies pour l'année 2010, 75-0 C → 72 D pour les sommes anciennes) ;
- une mention de transfert (1681 quater A → 1762 A, deux pistes) ;
- une condition qui cesse d'elle-même (1740 → 199 undecies A).

## Points pour l'auteur

- La concordance CIBS des articles d'accise abrogés à date différée (302 H quater, 302 F ter) est hors corpus. Les notes de ces articles sont à rectifier lors de leur prochaine modification.
- L'inscription ou l'exclusion de 302 B, 302 M, 302 M bis et 441 de l'inventaire reste à décider (RT-INV-14).
