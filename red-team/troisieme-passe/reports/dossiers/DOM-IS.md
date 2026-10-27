# DOM-IS : revue de fond de l'IS déclenché à la distribution

Red-team juridique indépendante, troisième passe. Instantané `20261026T230545Z`, corpus au 18 octobre 2026. Rapport du 26 octobre 2026.

**Avertissement.** Revue réalisée par une IA. Elle ne vaut pas validation par un juriste. La seconde passe se poursuit en production : les conclusions sont provisoires. 1668, 1668 B, 1668 D, 1655 sexies et L3324-1 sont encore au statut `pending`.

## 1. Orientation et résultat obtenu

### Orientation (citations exactes, `policy-coordinations.json`)

- `fiscalite` : « remplacer l'IS annuel de droit commun par un IS déclenché à la distribution. Les bénéfices conservés dans l'entreprise, même en trésorerie sans investissement immédiat, ne supportent pas cet IS. Taux français proposé de vingt pour cent du bénéfice avant IS distribué, soit vingt quatre-vingtièmes du dividende net d'IS. Préserver le bénéfice du taux réduit des petites entreprises. »
- `is_distribution` : « Déclencheur : dividendes et distributions de bénéfices, monétaires ou en nature, et avantages personnels dissimulés ou prêts simulés aux associés. […] traiter rachats, liquidation et transferts d'actifs sans créer une échappatoire ni taxer indistinctement tout prêt professionnel. »
- « Éviter une seconde imposition à l'IS des bénéfices déjà taxés avant la réforme, ainsi que les cascades entre filiales et sociétés mères sur un même bénéfice. […] ne pas conserver un acompte annuel d'IS ordinaire sur le seul bénéfice conservé. »
- « Le minimum international […] garde son champ légal. […] ne pas affirmer qu'une nouvelle réforme française en 2026 bénéficie automatiquement du même report que l'Estonie. […] Aucune promesse de zéro impôt total pour les groupes soumis au minimum, ni conformité européenne présumée. »
- Contributions additionnelles (235 ter ZC, article 48 de la LF 2025) : ne pas les appliquer aux faits nouveaux, en conservant les dettes anciennes.

### Résultat obtenu

**Pour le cœur du dispositif, la réforme atteint son objectif.** Les propositions suivantes forment un système cohérent :

- 206 12 et 219 V/VI : assujettissement maintenu, exigibilité à la distribution, définition opératoire de la distribution, taux de 20 % avant IS, PME à 15/85, taux réduits conservés.
- 209 XI–XIII : compte protégé des réserves déjà taxées, compartiments par taux, déficits, transition.
- 1668 : paiement au 15 du mois suivant, aucun acompte sur le bénéfice conservé.
- 145/216 : pas de cascade entre sociétés.
- 221/221 bis : continuité ou sortie.
- 223 A et suivants : groupes.
- 235 ter ZC et article 48 : contributions écartées.
- 223 VJ : minimum maintenu.
- Coordinations du travail (L3324-1) et de l'IR (109–112, 158).

L'arithmétique de 219 V 4 est exacte : S = t(qN−D)/(1−tq) découle de S = t·[q(N+S)−D]. La transition protège les réserves anciennes, les déficits, les crédits et les sursis.

**Elle ne l'atteint pas entièrement, pour sept raisons de fond (P1).**

1. Les grands groupes subissent l'impôt complémentaire de 15 % sur les bénéfices conservés, puis l'IS de 20 % sur les mêmes bénéfices distribués, sans articulation (RT-DOMIS-01).
2. Les charges non déductibles décaissées, dont les surcoûts d'emprunt de l'article 212 bis issus de la directive ATAD, ne sont jamais imposées si l'entreprise ne distribue pas (RT-DOMIS-02).
3. Les impositions annuelles correctives maintenues (205 B à D, 209 B) n'ont ni échéance, ni taux, ni imputation des déficits (RT-DOMIS-03).
4. Les lots se contredisent sur la compensation des pertes nouvelles dans les groupes (RT-DOMIS-04).
5. Deux discriminations au regard du droit de l'Union sont créées par la protection sans seuil des dividendes français : sur les dividendes reçus (RT-DOMIS-05) et sur la retenue à la source sortante (RT-DOMIS-06).
6. Une société peut sortir de l'IS sans perte de compétence française et échapper ainsi à l'IS sur ses bénéfices différés (RT-DOMIS-07).

Aucun constat ne justifie un P0 : aucune impossibilité d'appliquer le cœur du régime, aucune perte de droits acquis, aucune double imposition dès le premier jour pour tous. RT-DOMIS-01 s'en approche pour les groupes d'au moins 750 M€.

## 2. Méthode

- Lecture de l'orientation : `policy-coordinations.json` (`fiscalite`, `is_distribution`, `chiffrage_net_is_2026_10_19`, `taxe_sur_les_salaires_removal`) et `site-summaries.json` (entreprise). Lecture du dossier `coordinations/is-distribution/manifest.json` (article 48 de la loi 2025-127 et sa proposition X ; article 12 de la loi 2026-103) et des pièces du lot `batches/is-distribution/` : `200.json`, `201.json`, `202.json`, `controle-fiscalite.md`, `controle-arithmetique.json`, `verification-finale.json`, `fiscal-revisions-preview.json`.
- Périmètre : recherche dans `drafts.proposed_xml` (versions en vigueur au 18 octobre 2026 ou futures) des motifs « V et VI de l'article 219 », « XI de l'article 209 », « régime de distribution », « IS ordinaire » et « impôt sur les sociétés ordinaire ». Résultat : environ 230 articles du CGI, des annexes II à IV, du code du travail et du CSS, liste reproductible avec `scan.py` (outil de lecture seule, hors instantané). Recherches ciblées complémentaires : minimum international et crédit, renvois à 216 II/III, « impôt correspondant ».
- Lecture : tout extrait cité a été exporté par `tools/cite.py`, qui imprime toutes les versions (preuves sous `evidence/cited/20261026T230545Z/`). Seules les versions en vigueur au 18 octobre 2026 et les versions futures ont été analysées.
- Doublons : vérification dans `reports/register.json` des treize objections signalées, plus une recherche par mots-clés (pertes nouvelles, précompte, minimum, 111 bis, 212 bis). Aucun doublon de fond trouvé. `notes-contradictions/INDEX.md` ne contient aucune entrée IS.
- Sources primaires externes : EUR-Lex (CELEX 32022L2523), interrogé deux fois par WebFetch le 26 octobre 2026, a renvoyé une page vide. Aucun contournement n'a été tenté. Les textes européens et la jurisprudence de la CJUE sont donc cités de mémoire, signalés « à vérifier ». Seules les définitions de 223 VK (transposition) ont été lues dans le corpus.
- Aucun fichier de production lu ou écrit ; aucun script de production lancé ; ni `snapshot.py` ni `sealed_evidence.py`.

## 3. Périmètre et statut de seconde passe

Légende : **E** = proposition (et source lorsqu'elle est utile) lue en entier ; **X** = lecture ciblée de subdivisions motivée par le constat ; **M** = métadonnées et motif seulement.

| Code | Article | Version (LEGIARTI) | Bornes | Statut projet | Seconde passe | Lot propriétaire | Lecture |
|---|---|---|---|---|---|---|---|
| cgi | 206 | LEGIARTI000054373514 | 2026-07-01 → 2999-01-01 | rewrite_draft | completed | `batches/is-distribution/200.json` | E |
| cgi | 209 | LEGIARTI000048847486 | 2023-12-31 → 2999-01-01 | rewrite_draft | completed | `batches/is-distribution/200.json` | E |
| cgi | 219 | LEGIARTI000053542939 | 2026-02-21 → 2999-01-01 | rewrite_draft | completed | `batches/radical-review-legacy/00004.json` | E |
| cgi | 1668 | LEGIARTI000033836779 | 2020-01-01 → 2999-01-01 | rewrite_draft | pending | `batches/is-distribution/200.json` | E |
| cgi | 145 | LEGIARTI000051203497 | 2025-02-16 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00018.json` | X |
| cgi | 216 | LEGIARTI000048831340 | 2023-12-31 → 2999-01-01 | rewrite_draft | completed | `batches/is-transition/001.json` | E |
| cgi | 221 | LEGIARTI000051765018 | 2025-06-19 → 2999-01-01 | rewrite_draft | completed | `batches/is-distribution/200.json` | X |
| cgi | 221 bis | LEGIARTI000037987801 | 2019-01-01 → 2999-01-01 | rewrite_draft | completed | `batches/is-distribution/200.json` | E |
| cgi | 111 bis | LEGIARTI000018015459 | 2007-12-29 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00015.json` | E |
| cgi | 109 | LEGIARTI000006302651 | 1979-07-01 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00015.json` | E |
| cgi | 110 | LEGIARTI000006307234 | 1993-08-18 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00015.json` | E |
| cgi | 111 | LEGIARTI000043662702 | 2021-06-12 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00015.json` | E |
| cgi | 112 | LEGIARTI000051203538 | 2025-02-16 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00015.json` | E |
| cgi | 117 | LEGIARTI000006307263 | 2006-01-01 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00015.json` | E |
| cgi | 119 bis | LEGIARTI000051218411 | 2025-02-16 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00015.json` | E |
| cgi | 187 | LEGIARTI000051218440 | 2025-02-16 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00029.json` | E |
| cgi | 119 ter | LEGIARTI000031815505 | 2016-01-01 → 2027-01-01 | rewrite_draft | completed | `batches/automatic-impots/00015.json` | E |
| cgi | 158 | LEGIARTI000054373673 | 2026-07-01 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00026.json` | X |
| cgi | 205 | LEGIARTI000006303408 | 1979-07-01 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00045.json` | X |
| cgi | 205 B | LEGIARTI000044978626 | 2022-01-01 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00046.json` | X |
| cgi | 205 C | LEGIARTI000040339940 | 2022-01-01 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00046.json` | X |
| cgi | 205 D | LEGIARTI000040339962 | 2020-01-01 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00046.json` | X |
| cgi | 209 B | LEGIARTI000029355796 | 2015-01-01 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00047.json` | X |
| cgi | 212 bis | LEGIARTI000049641637 | 2024-06-02 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00049.json` | X |
| cgi | 238 A | LEGIARTI000037526846 | 2020-01-01 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00066.json` | X |
| cgi | 38 | LEGIARTI000051203585 | 2025-02-16 → 2999-01-01 | rewrite_draft | completed | `batches/fiscalite/batch005.json` | X |
| cgi | 39 | LEGIARTI000053542680 | 2026-02-21 → 2027-01-01 | rewrite_draft | completed | `batches/automatic-impots/00002.json` | X |
| cgi | 210 A | LEGIARTI000046196219 | 2022-08-18 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00048.json` | X |
| cgi | 220 | LEGIARTI000028434377 | 2014-01-01 → 2999-01-01 | rewrite_draft | completed | `batches/is-distribution/201.json` | E |
| cgi | 220 quinquies | LEGIARTI000053560738 | 2026-02-21 → 2999-01-01 | rewrite_draft | completed | `batches/is-distribution/201.json` | M |
| cgi | 223 | LEGIARTI000034387974 | 2017-04-08 → 2999-01-01 | rewrite_draft | completed | `batches/is-distribution/202.json` | M |
| cgi | 223 A | LEGIARTI000048834056 | 2023-12-31 → 2999-01-01 | rewrite_draft | completed | `batches/is-transition/001.json` | X |
| cgi | 223 B | LEGIARTI000048831317 | 2023-12-31 → 2999-01-01 | rewrite_draft | completed | `batches/is-transition/001.json` | X |
| cgi | 223 I | LEGIARTI000042909624 | 2020-12-31 → 2999-01-01 | rewrite_draft | completed | `batches/is-transition/001.json` | X |
| cgi | 223 L | LEGIARTI000053543307 | 2026-02-21 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00054.json` | X |
| cgi | 223 Q | LEGIARTI000037987441 | 2019-01-01 → 2999-01-01 | rewrite_draft | completed | `batches/is-transition/001.json` | X |
| cgi | 223 S | LEGIARTI000037987404 | 2019-01-01 → 2999-01-01 | rewrite_draft | completed | `batches/is-transition/001.json` | X |
| cgi | 223 O | LEGIARTI000053543337 | 2026-02-21 → 2999-01-01 | rewrite_draft | completed | `batches/is-transition/001.json` | E |
| cgi | 223 VJ | LEGIARTI000048846056 | 2023-12-31 → 2999-01-01 | rewrite_draft | completed | `batches/is-transition/001.json` | E |
| cgi | 223 VK | LEGIARTI000054373422 | 2026-07-01 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00055.json` | X |
| cgi | 223 VL | LEGIARTI000048803788 | 2023-12-31 → 2999-01-01 | retained_unchanged | completed | `batches/automatic-impots/00055.json` | M |
| cgi | 223 WB | LEGIARTI000048804000 | 2023-12-31 → 2999-01-01 | retained_unchanged | completed | `batches/automatic-impots/00059.json` | E |
| cgi | 223 WC | LEGIARTI000048804010 | 2023-12-31 → 2999-01-01 | retained_unchanged | completed | `batches/automatic-impots/00060.json` | E |
| cgi | 223 WW | LEGIARTI000053545798 | 2026-02-21 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00062.json` | E |
| cgi | 235 ter ZC | LEGIARTI000031011715 | 2015-08-08 → 2999-01-01 | rewrite_draft | completed | `batches/is-distribution/202.json` | M |
| cgi | 1668 B | LEGIARTI000029355581 | 2015-01-01 → 2999-01-01 | rewrite_draft | pending | `batches/is-distribution/202.json` | M |
| cgi | 1668 D | LEGIARTI000022178453 | 2010-05-01 → 2999-01-01 | rewrite_draft | pending | `batches/is-distribution/202.json` | M |
| cgi | 238 | LEGIARTI000048833463 | 2023-12-31 → 2999-01-01 | rewrite_draft | completed | `batches/is-distribution/201.json` | M |
| cgi | 239 | LEGIARTI000037988649 | 2018-12-31 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00070.json` | X |
| cgi | 239 bis AB | LEGIARTI000038586316 | 2019-01-01 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00070.json` | X |
| cgi | 1655 sexies | LEGIARTI000053543064 | 2026-02-21 → 2999-01-01 | rewrite_draft | pending | `batches/automatic-impots/00124.json` | X |
| cgi | 207 | LEGIARTI000054373456 | 2026-07-01 → 2027-01-01 | rewrite_draft | completed | `batches/automatic-impots/00034.json` | M |
| cgi | 200 A | LEGIARTI000053546896 | 2026-02-21 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00044.json` | M |
| cgi | 199 ter B | LEGIARTI000037988080 | 2019-01-01 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00030.json` | M |
| cgi | 244 quater B | LEGIARTI000053544409 | 2026-01-01 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00072.json` | M |
| cgi | 220 B | LEGIARTI000006303545 | 1983-01-01 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00050.json` | M |
| cgi | 117 quater | LEGIARTI000036428175 | 2018-01-01 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00015.json` | M |
| cgi | 108 | LEGIARTI000006302650 | 1979-07-01 → 2999-01-01 | retained_unchanged | completed | `batches/automatic-impots/00015.json` | M |
| cgi | 223 R | LEGIARTI000042909608 | 2020-12-31 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots/00054.json` | M |
| cgi | 1763 C | LEGIARTI000053543723 | 2026-02-21 → 2999-01-01 | rewrite_draft | pending | `batches/automatic-impots/00130.json` | M |
| a3 | 46 quater-0 ZJ bis | LEGIARTI000043264317 | 2021-03-19 → 2999-01-01 | rewrite_draft | completed | `batches/automatic-impots-annexe-3/00018.json` | X |
| travail | L3324-1 | LEGIARTI000053544617 | 2026-01-01 → 2999-01-01 | rewrite_draft | pending | `batches/automatic-travail/00098.json` | E |

Pièce hors code lue en entier : article 48 de la loi n° 2025-127, source et proposition X (`coordinations/is-distribution/manifest.json`). Le X exclut l'IS de distribution de l'assiette et de la moyenne ; les faits anciens restent régis par la loi antérieure. Aucune objection n'est formulée sur ce point.

## 4. Mécanique d'ensemble vérifiée

| Élément | Constat | Renvoi |
|---|---|---|
| Fait générateur | Mise à disposition effective (219 V 1 a, 205, 109) ; vote non suivi d'effet exclu ; avantages personnels (b), prêts simulés (c), rachats et liquidations au-delà des apports (d), prélèvements d'un établissement stable (e). Cohérent avec l'orientation. | RT-DOMIS-09 (établissement stable) |
| Sortie de l'IS sans perte de compétence | Non imposée : 111 bis vise l'IR seul, 221 7 a écarte l'IS, et le critère « taux du deuxième alinéa du I » de 221 2 devient inopérant. | **RT-DOMIS-07** |
| Assiette, fractions | Formule correcte ; fractions taxables q, quote-part de 12 %, déficits plafonnés. Les charges non déductibles ne sont imposées qu'avec une distribution. | **RT-DOMIS-02** |
| Taux | 20 % avant IS (20/80) ; PME à 15/85 dans la limite de 42 500 € ; taux de 10, 15, 19 et 0 % conservés (219 VI 1). Plafond PME ambigu. | RT-DOMIS-10 |
| Réserves antérieures | Compte protégé de 209 XI 1, imputé en premier ; les sursis n'y figurent pas. Conforme. | alerte écartée |
| Cascades entre sociétés | Protection à 100 % des dividendes français justifiés ou relevant de 145 ; quotes-parts de 5 % et 1 % supprimées pour le régime nouveau. Conforme à l'orientation, mais crée deux écarts au regard du droit de l'Union. | **RT-DOMIS-05**, **RT-DOMIS-06** |
| Déficits | Conservés et imputés sur les assiettes distribuées (209 XI 3), report en arrière maintenu (220 quinquies). Lots contradictoires pour les groupes. | **RT-DOMIS-04** |
| Crédits d'impôt | 1668 7, 223 O 3, 220 6 : imputation à la distribution, droits à remboursement (CIR) non subordonnés à une distribution, crédits étrangers suivis avec le compartiment. Conforme. | alerte écartée |
| Paiement et déclarations | 1668 6 à 10 : déclaration mensuelle seulement en cas de distribution, rapprochement annuel. Aucun acompte sur le bénéfice conservé. Les impositions annuelles correctives ne sont pas couvertes. | **RT-DOMIS-03** |
| Contributions additionnelles | 235 ter ZC, 1668 B et D, annexe III 366 L et M, article 48 X : écartées pour les faits nouveaux, dettes anciennes conservées. Conforme. | alerte écartée |
| Minimum international | Maintenu (223 VJ, 223 WB inchangé) ; article 40 de la directive non revendiqué (223 VK 39° c). Aucune articulation avec l'IS de distribution. | **RT-DOMIS-01** |
| Anti-abus européen | Dispositifs hybrides (205 B à D) et SEC (209 B) corrigés chaque année ; limitation des charges financières (212 bis) différée jusqu'à distribution. Directive mère-fille : question réservée. | RT-DOMIS-02, RT-DOMIS-03, RT-DOMIS-11 |
| Sortie et transfert | 221 7 b et c : imposition de sortie des bénéfices différés et des plus-values, paiement fractionné UE/EEE en cinq fractions maintenu. | RT-DOMIS-07 (sortie sans transfert) |
| Autres codes | Travail L3324-1 : participation calculée avec un IS évalué « comme si » le bénéfice était distribué, sans dette. Cohérent (L3324-1 reste au statut `pending`). Aucune incidence CSS, CCH ou urbanisme relevée dans le périmètre lu. | alerte écartée |
| Constitution | Pas de rétroactivité (exercices ouverts après l'entrée en vigueur). Le décret ne peut toucher ni l'assiette ni le taux (1668 9). Égalité : la différence entre IS et IR existait déjà, l'option IS reste ouverte (1655 sexies, 239). Points d'égalité nouveaux liés à RT-DOMIS-01 et RT-DOMIS-07. | — |

## 5. Constats

Les objections détaillées (champs complets, passages exacts, empreintes) figurent dans `DOM-IS.json`. Synthèse :

| ID | P | Nature | Statut | Objet |
|---|---|---|---|---|
| RT-DOMIS-01 | P1 | coordination manquante | confirmé | Pilier 2 : impôt complémentaire annuel, puis IS de distribution sur le même bénéfice, sans articulation |
| RT-DOMIS-02 | P1 | risque juridique | confirmé | Charges non déductibles décaissées (212 bis / ATAD art. 4, 39 4, 238 A) jamais imposées sans distribution |
| RT-DOMIS-03 | P1 | coordination manquante | confirmé | Impositions annuelles correctives (205 B à D, 209 B) sans échéance, à taux incertain (25/20 %), sans imputation des déficits |
| RT-DOMIS-04 | P1 | incohérence du projet | confirmé | Pertes nouvelles des groupes : 223 A IV / 223 B / 223 L / 223 S contre 209 XI 3 / 223 I II / ZJ bis |
| RT-DOMIS-05 | P1 | risque juridique | à confirmer | Dividendes étrangers de portefeuille imposés à la redistribution, dividendes français protégés sans seuil (art. 63 TFUE) |
| RT-DOMIS-06 | P1 | risque juridique | à confirmer | Retenue de 20 % sur les sociétés de l'Union détenant moins de 10 %, contre 0 % pour les résidents (art. 63 TFUE) |
| RT-DOMIS-07 | P1 | coordination manquante | confirmé | Sortie de l'IS sans perte de compétence (transformation, renonciation, exonération) : IS des bénéfices différés évité |
| RT-DOMIS-08 | P2 | incohérence du projet | confirmé | Renvois au « II de l'article 216 » abrogé (209 XI 1, 220 4) |
| RT-DOMIS-09 | P2 | simple alerte | à confirmer | Établissement stable et prêts à une mère étrangère : report indéfini plausible |
| RT-DOMIS-10 | P2 | simple alerte | à confirmer | Tranche PME : cumul possible de deux plafonds pour un même exercice d'origine |
| RT-DOMIS-11 | P2 | risque juridique | à confirmer | Directive mère-fille : qualification de retenue à la source à écarter clairement |
| RT-DOMIS-12 | P2 | simple alerte | à confirmer | Sociétés patrimoniales passives : report de l'impôt sur les revenus du patrimoine, à chiffrer |

## 6. Objections existantes confirmées, précisées ou contredites

- **RT-FUTFISC-01 (P1)** : confirmée et précisée pour ce domaine. Les coordinations IS de 39 (le 14), 207 et 119 ter n'existent que sur des versions qui s'achèvent au 1er janvier 2027 (`ABROGE_DIFF`) ; les versions de 2027 (`VIGUEUR_DIFF`, LEGIARTI000053154402, LEGIARTI000053154521, LEGIARTI000053154449) n'ont aucune proposition. Le 14 de 39 (aucun fait générateur sur le bénéfice conservé) et la précision du 1 de 119 ter (la société du régime de distribution reste « au taux normal ») doivent être reportés sur la rédaction de 2027, faute de quoi ils disparaîtraient à cette date. Ce n'est pas une nouvelle objection.
- **RT-P1-CGI-C-04 (P1)** : non contredite. Le 219 V 1 e (prélèvements d'un établissement stable) remplace bien la retenue de 115 quinquies pour les exercices nouveaux. Le risque de report indéfini des succursales est traité à part (RT-DOMIS-09) ; il ne recoupe pas les dépendants de C-04.
- **RT-P1-CGI-A-08, RT-P1-CGI-B-08, RT-P1-ANNEXES-08, -10, -14, RT-DOC-04, RT-FUTFISC-07, RT-FUTCSS-33, RT-FUTTL-09, RT-P1-TRAVAIL-B-04, RT-P1-CGI-C-06** : sans recoupement de fond avec le mécanisme de l'IS de distribution examiné ici. Aucune confirmation ni contradiction.
- Aucune objection existante ne porte sur les constats RT-DOMIS-01 à 12 (recherche par articles et par mots-clés dans `register.json`).

## 7. Propositions de correction (présentées séparément des constats)

Chaque correction est rédigée pour être insérée dans la proposition courante, non dans le droit en vigueur. Les dépendances sont indiquées.

### RT-DOMIS-01 — Pilier 2 : impôt complémentaire annuel, puis IS de distribution sur le même bénéfice, sans articulation

**Correction proposée.** Ajouter au V de l'article 219 un 6 ainsi rédigé : « 6. Les entités constitutives situées en France d'un groupe entrant dans le champ de l'article 223 VL peuvent opter pour la liquidation annuelle de l'impôt sur les sociétés, au titre de chaque exercice, sur le bénéfice de cet exercice déterminé selon le XI de l'article 209 et aux taux des 2 et 3 du présent V et du VI appliqués à la base avant impôt, sans la majoration prévue pour les montants nets distribués. Pour un groupe mentionné à l'article 223 A, l'option est exercée par la société mère pour l'ensemble des membres. Elle est notifiée au plus tard à la date de dépôt de la déclaration de l'exercice prévue à l'article 223 et vaut jusqu'à sa dénonciation, qui prend effet pour l'exercice suivant. L'impôt ainsi liquidé est déclaré et payé selon les 1 à 5 de l'article 1668. Le montant net des bénéfices ainsi imposés est inscrit au compte prévu au 1 du XI de l'article 209 ; sa distribution ultérieure ne donne lieu à aucun second impôt sur les sociétés. Les déficits, crédits et réductions d'impôt s'imputent sur cet impôt dans leurs conditions propres, sans double emploi. L'option ne modifie ni le champ, ni le calcul de l'imposition minimale prévue aux articles 223 VJ et suivants. » Coordonner le premier alinéa de l'article 1668 : « … ainsi qu'aux régimes annuels distincts expressément maintenus par le 12 de l'article 206 et à l'option prévue au 6 du V de l'article 219. »

**Justification.** Le projet est cohérent sur un point : il maintient le minimum de 15 % et refuse d'affirmer l'éligibilité au report de l'article 40 (223 VK, 39°, c). Mais il ne tire aucune conséquence de ce maintien. Pour une entité française d'un groupe dans le champ de 223 VL, l'IS ordinaire de l'exercice est nul tant qu'il n'y a pas de distribution ; son taux effectif GloBE est donc proche de zéro et l'impôt national complémentaire (223 WB, retenu inchangé) porte le bénéfice à 15 % chaque année. Lorsque ce même bénéfice est distribué ensuite, l'IS de 20 % du V de 219 est dû en entier : rien ne l'impute, ni ne protège le bénéfice déjà soumis au complémentaire. Le 209 XIII renvoie à des « limites expressément prévues » qui n'existent nulle part dans le corpus (recherche dans tous les projets : aucune), et le 223 O 3 exclut l'imputation dans l'autre sens. Le surcroît d'IS payé l'année de la distribution améliore le taux effectif de cette seule année : il ne rembourse pas le complémentaire des années antérieures (règles de rattachement GloBE, à confirmer sur le texte de la directive). La charge cumulée sur un bénéfice conservé puis distribué peut donc atteindre 35 %, contre 25 % avant la réforme. Sur 100 de bénéfice, 15 sont dus au titre du complémentaire, non déductible (223 VJ). Les 85 restants sont ensuite distribués avec une fraction taxable de 100/85, soit 20 d'IS et 65 nets. Les seuls groupes que l'orientation accepte de ne pas favoriser sont ainsi pénalisés au-delà du droit actuel.

**Autres options.** (a) Imputer l'impôt national complémentaire français acquitté sur un exercice sur l'IS de distribution ultérieur du même bénéfice, ou porter ce bénéfice au compte protégé à hauteur du complémentaire. Ce système suit l'orientation de plus près, mais il pourrait passer pour un « avantage lié » au complémentaire et faire perdre à l'impôt national son caractère qualifié : à vérifier sur la directive et les commentaires de l'OCDE avant tout choix. (b) Exclure de plein droit du régime de distribution les entités dans le champ de 223 VL. C'est plus simple, mais cela retire l'option aux groupes qui préfèrent le report. (c) Maintenir le texte et le dire expressément dans l'étude d'impact : la charge peut alors dépasser le droit actuel, ce que l'orientation n'a pas décidé.

**À préserver.** Le régime de distribution pour toutes les autres entreprises ; le taux de 20 % ; le compte protégé ; les taux réduits et exonérations du VI ; le champ, les exclusions, les mesures favorables et le calendrier propres au minimum international ; l'absence d'affirmation d'éligibilité à l'article 40.

### RT-DOMIS-02 — Charges non déductibles décaissées (212 bis / ATAD art. 4, 39 4, 238 A) jamais imposées sans distribution

**Correction proposée.** Ajouter au 1 du V de l'article 219, après le e, un f ainsi rédigé : « f) Le montant des charges financières nettes non admises en déduction au titre d'un exercice en application de l'article 212 bis et de l'article 223 B bis, ainsi que celui des dépenses et charges effectivement payées dont la déduction est exclue par le 4 et le 2 de l'article 39 ou par l'article 238 A, lorsqu'elles ne constituent pas déjà une distribution en application du b. Ce montant est imposé au titre de l'exercice de sa constatation, au taux du 2 appliqué au montant lui-même, sans la majoration prévue pour les montants nets distribués, et l'impôt est acquitté avec le solde prévu au 8 de l'article 1668. La base ainsi imposée est retranchée de la fraction taxable suivie au XI de l'article 209 et ne peut être imposée une seconde fois lors d'une distribution ; le montant net correspondant n'est pas inscrit au compte protégé. Les charges financières reportées et la capacité de déduction inemployée de l'article 212 bis s'imputent, lorsqu'elles deviennent déductibles, d'abord sur les montants imposés en application du présent f au titre des exercices ultérieurs, puis sur les bases suivies. » Corriger en conséquence le X de l'article 212 bis : « Par dérogation, l'impôt afférent aux charges non admises en déduction est établi dans les conditions du f du 1 du V de l'article 219. »

**Justification.** Dans le régime nouveau, une charge non déductible n'est jamais imposée lorsqu'elle est payée. Elle augmente seulement la fraction taxable q du compartiment (209 XI 2 ; 219 V 4) et ne devient imposable qu'au moment où le bénéfice comptable restant est distribué. Deux cas échappent donc à l'impôt. (1) La charge non déductible absorbe tout le bénéfice comptable : montant économique nul, rien à distribuer. (2) L'entreprise ne distribue jamais et rémunère ses associés ou son groupe par des intérêts, redevances ou frais : c'est le cas d'une filiale à capitaux étrangers. Pour les charges financières nettes, 212 bis X le dit expressément : les réintégrations « corrigent les assiettes suivies ». Or l'article 4 de la directive 2016/1164 limite la déduction « au cours de la période d'imposition » des surcoûts d'emprunt. Le projet applique pourtant la logique inverse aux dispositifs hybrides de la même directive (205 B IV, 205 C, 205 D : correction annuelle « non différée ») et à 209 B. Il est donc incohérent avec lui-même. La définition de 223 VK, 39°, a, issue du Pilier 2, montre d'ailleurs que les régimes de distribution de référence imposent aussi, lorsqu'elles sont engagées, les dépenses étrangères à l'exploitation. Le même trou concerne les charges somptuaires et dépenses privées sans bénéficiaire associé (39, 4), les sanctions (39, 2) et les paiements de 238 A. Seuls les avantages consentis à un associé sont rattrapés (219 V 1 b).

**Autres options.** (a) Limiter le f à l'article 212 bis et à l'article 223 B bis, qui relèvent du droit de l'Union, en laissant les autres non-déductibilités dans le mécanisme q. C'est le minimum juridique, mais la fuite des charges somptuaires reste ouverte. (b) Imposer à la liquidation et à la sortie du régime le solde des fractions taxables sans montant économique. C'est plus tardif et moins sûr au regard de la directive.

**À préserver.** La déductibilité des salaires, achats, investissements, intérêts et remboursements professionnels réels ; le seuil de 3 M€, le ratio de 30 % et les clauses de sauvegarde ou de report de 212 bis ; l'absence d'IS sur la seule conservation des bénéfices.

### RT-DOMIS-03 — Impositions annuelles correctives (205 B à D, 209 B) sans échéance, à taux incertain (25/20 %), sans imputation des déficits

**Correction proposée.** 1° Au premier alinéa de l'article 1668, après « par le 12 de l'article 206 », insérer : « ainsi qu'aux impositions établies au titre d'un exercice en application du IV de l'article 205 B, des articles 205 C et 205 D, du V de l'article 209 B et, le cas échéant, du f du 1 du V de l'article 219 ; pour ces impositions, aucun acompte n'est dû et l'impôt est acquitté avec le relevé de solde prévu au 2 ». 2° Au 2 du VI de l'article 219, après « conservent leurs règles propres. », insérer : « Les impositions correctives annuelles prévues au IV de l'article 205 B, aux articles 205 C et 205 D et au V de l'article 209 B sont établies au titre de leur exercice, au taux du 2 ou du 3 du V appliqué à la base avant impôt, sans majoration pour montant net ; les déficits du 3 du XI de l'article 209 peuvent s'y imputer dans les limites du I de l'article 209, sans double emploi. » 3° Compléter le deuxième alinéa du 12 de l'article 206 par la même énumération.

**Justification.** Les projets de 205 B IV, 205 C, 205 D et 209 B V maintiennent, à juste titre, une imposition corrective établie chaque exercice, même sans distribution. Mais le paiement annuel du 1668 (acomptes et solde, 1 à 5) n'est conservé que pour les exercices anciens et les « régimes annuels distincts expressément maintenus par le 12 de l'article 206 ». Or ce 12 ne vise que le tonnage, les revenus patrimoniaux et 219 bis, et la reprise du 5 ter. Les 6 à 9 du 1668 ne visent que les distributions. Aucune échéance n'est donc fixée pour ces impositions annuelles. Le taux est lui aussi incertain : « aux taux légalement applicables » renvoie au I de 219, qui conserve 25 % (« Le taux normal de l'impôt est fixé à 25 % »), alors que le taux normal du régime nouveau est de 20 % et que 221, 7, b applique pour les sorties les taux du VI aux montants avant impôt. Enfin, l'imputation des déficits n'est prévue par 209 XI 3 que sur les assiettes distribuées. Les notes de 205 B, 205 C et 205 D le reconnaissent (« ne règle pas complètement l'imputation sur les assiettes correctives annuelles. Hors lot : compléter »), comme celles de 209 B pour les listes de 206 12 et 219 VI 2. Ces coordinations restent ouvertes.

**Autres options.** Conserver expressément 25 % pour ces impositions correctives, si l'auteur veut une surcharge anti-évasion. Cette solution serait plus sévère que le droit commun du régime nouveau et devrait être justifiée ; elle n'est pas recommandée. Supprimer les acomptes plutôt que les rétablir est conforme à l'orientation (pas d'acompte sur bénéfice conservé).

**À préserver.** Les protections contre la seconde imposition des montants déjà soumis à ces impositions correctives (205 B IV, 205 C, 205 D, 209 B V) ; les exceptions européennes de 209 B ; l'absence d'IS annuel sur les autres bénéfices conservés.

### RT-DOMIS-04 — Pertes nouvelles des groupes : 223 A IV / 223 B / 223 L / 223 S contre 209 XI 3 / 223 I II / ZJ bis

**Correction proposée.** Aligner sur la faveur maintenue par 223 A IV (ne pas supprimer une faveur pour rendre les textes cohérents). 1° Au premier alinéa du 3 du XI de l'article 209, remplacer « ; cette faculté ne s’étend pas aux pertes nouvelles ni à des membres ou activités exclus par cet article. » par : « . Les pertes nouvelles des membres d’un groupe sont compensées dans les conditions du IV de l’article 223 A ; aucune perte ne peut être utilisée deux fois, ni hors des membres et activités admis par les articles 223 A à 223 U. » 2° Au II de l'article 223 I, remplacer la dernière phrase par : « Les pertes nouvelles des membres suivent le IV de l’article 223 A, sans s’ajouter au plafond ni à l’assiette du présent droit transitoire. » 3° Annexe III, 46 quater-0 ZJ bis : remplacer « Aucune mutualisation de pertes nouvelles ni créance remboursable n'est créée. » par « Aucune créance remboursable n'est créée ; la compensation des pertes nouvelles suit le IV de l'article 223 A du code général des impôts. »

**Justification.** Le lot is-transition (223 A IV, 223 B, 223 S) et le lot 223 L posent, « par dérogation » aux articles 209, 223 B et 223 I, que les pertes nouvelles d'un membre compensent les bénéfices des autres membres. Le lot is-distribution (209 XI 3), le projet de 223 I II et l'annexe III (46 quater-0 ZJ bis) réservent au contraire la mutualisation au seul déficit d'ensemble antérieur. Le contrôle fiscal du lot is-distribution le confirme. La clause « par dérogation » ne règle pas le conflit : 209 XI 3 est la règle spéciale du régime de distribution ; 223 A IV est la règle spéciale des groupes ; et la règle réglementaire ZJ bis contredit la loi proposée. Le juge devrait choisir entre deux textes de même rang, adoptés ensemble et contradictoires.

**Autres options.** Retenir au contraire la restriction de 209 XI 3, en supprimant la dérogation de 223 A IV, 223 B, 223 L 7 et 223 S. Cela supprime une faveur de l'intégration : l'auteur doit le décider expressément, ce n'est pas une simple coordination.

**À préserver.** Le plafond unique du déficit d'ensemble antérieur ; son titulaire ; l'interdiction du double emploi ; les agréments et transferts de 223 I, 223 L et 223 R pour les opérations futures.

### RT-DOMIS-05 — Dividendes étrangers de portefeuille imposés à la redistribution, dividendes français protégés sans seuil (art. 63 TFUE)

**Correction proposée.** Au IV de l'article 216, après le deuxième alinéa, insérer : « Le montant net reçu d’une société établie dans un autre État membre de l’Union européenne, dans un autre État partie à l’accord sur l’Espace économique européen ou dans un État ayant conclu avec la France une convention d’assistance administrative en vue de lutter contre la fraude et l’évasion fiscales, qui ne relève pas de l’article 145, est inscrit au compte prévu au 1 du XI de l’article 209 à proportion de l’impôt sur les bénéfices effectivement acquitté par la société distributrice sur les bénéfices distribués, rapporté au taux du 2 du V de l’article 219, sans pouvoir excéder ce montant net. La justification résulte des pièces dont dispose le bénéficiaire ; à défaut de justification, le montant suit le troisième alinéa. Les exclusions du 6 de l’article 145 et des États ou territoires non coopératifs demeurent applicables. »

**Justification.** Selon 145, 10 et 216, IV, un dividende reçu d'une société française du régime de distribution est inscrit au compte protégé quelle que soit la participation : sa redistribution ne supporte jamais d'IS. Un dividende de portefeuille (moins de 5 %, ou hors 145) reçu d'une société de l'Union ou d'un État tiers suit les « bénéfices nouveaux dont l'imposition est différée » et supporte 20 % à sa redistribution. Aucun crédit n'est donné pour l'impôt sur les sociétés acquitté à l'étranger par la distributrice. Le 220, 6 ne vise que les retenues à la source attachées au revenu. C'est la structure jugée contraire au droit de l'Union pour le précompte : redistribution neutre des dividendes d'origine française, imposée pour ceux d'origine étrangère (Accor). Le projet de 145 reconnaît que cette coordination n'est pas faite.

**Autres options.** Étendre purement et simplement la protection à tout dividende étranger soumis à un impôt équivalent, sans prorata : plus simple, mais plus coûteux, et cela récompense un impôt étranger faible. Ou faire de la protection du dividende français de portefeuille un prorata de l'IS effectivement liquidé : cela réduit une faveur du projet et exige une décision de l'auteur.

**À préserver.** La protection intégrale, sans seuil ni durée, des dividendes français ; le régime mère-fille et la suppression des quotes-parts de 5 % et 1 % ; les exclusions anti-abus du 6 de 145.

### RT-DOMIS-06 — Retenue de 20 % sur les sociétés de l'Union détenant moins de 10 %, contre 0 % pour les résidents (art. 63 TFUE)

**Correction proposée.** Ajouter à l'article 119 ter un 6 ainsi rédigé : « 6. Pour les dividendes distribués par une société relevant du régime prévu aux V et VI de l'article 219 au cours des exercices ouverts à compter de l'entrée en vigueur de ce régime, les conditions de détention et de durée prévues au c du 2 ne sont pas exigées lorsque ces dividendes auraient été inscrits au compte prévu au 1 du XI de l'article 209 s'ils avaient été perçus par une société établie en France. Les autres conditions du 2, le 2 bis et le 3 demeurent applicables. »

**Justification.** Avant la réforme, une société résidente détenant moins de 5 % d'une société française était imposée à 25 % sur le dividende reçu. La retenue de 25 % frappant le non-résident se comparait à cette charge. Après la réforme, le résident est entièrement protégé (145, 10 ; 216, IV), sans condition de participation : sa charge propre sur le dividende devient nulle, de façon définitive. Le non-résident de l'Union détenant moins de 10 % (5 % s'il ne peut imputer, 119 ter), ou ne remplissant pas les autres conditions de 119 ter, supporte une retenue de 20 % (187 proposé). Pour un non-résident, cette retenue est un impôt définitif, sauf imputation effective dans son État. La jurisprudence citée juge qu'un tel écart restreint la libre circulation des capitaux lorsque la convention ne le neutralise pas effectivement. La réforme crée elle-même ce nouvel écart. Les notes de 119 bis et 187 n'examinent pas cette comparabilité.

**Autres options.** Étendre la même règle aux sociétés établies dans un État tiers lié à la France par une convention d'assistance administrative, au titre de l'article 63 TFUE. Ou prévoir une restitution sur demande, par analogie avec les mécanismes existants pour les bénéficiaires déficitaires. Plus lourd, mais plus étroit.

**À préserver.** La retenue sur les bénéficiaires personnes physiques (12,8 %) et le taux de 75 % pour les États et territoires non coopératifs ; la clause anti-montages de 119 ter, 3 ; les conventions plus favorables.

### RT-DOMIS-07 — Sortie de l'IS sans perte de compétence (transformation, renonciation, exonération) : IS des bénéfices différés évité

**Correction proposée.** 1° Ajouter au 1 du V de l'article 219, après le e, un alinéa ainsi rédigé : « Sont également imposables comme des distributions, à la date de l'événement, les bénéfices différés non protégés d'une personne morale qui cesse totalement ou partiellement d'être assujettie à l'impôt sur les sociétés dans le régime du présent V, notamment par transformation, renonciation à une option, exonération ou affectation à un régime d'imposition distinct, sous réserve du 7 de l'article 221 et de l'article 221 bis pour les seuls sursis et plus-values latentes. L'impôt est liquidé aux taux du 2, du 3 et du VI appliqués à la base avant impôt, sans la majoration prévue pour les montants nets distribués. Le montant net correspondant est inscrit au compte prévu au 1 du XI de l'article 209 ; sa répartition ultérieure ou sa distribution réputée en application de l'article 111 bis ne donne pas lieu à un second impôt sur les sociétés. » 2° Au deuxième alinéa du 2 de l'article 221, après « au deuxième alinéa du I de l'article 219 », insérer « ou, pour les exercices relevant du régime de distribution, à l'impôt sur les sociétés dans les conditions du V du même article ». 3° Au a du 7 de l'article 221, après « un changement de forme ou d'activité », insérer « n'entraînant pas la cessation d'assujettissement mentionnée au dernier alinéa du 1 du V de l'article 219 ».

**Justification.** Le fait générateur du V de 219 est la mise à disposition effective. La distribution réputée de 111 bis, lorsqu'une société cesse d'être assujettie, n'en est pas une, et 111 bis renvoie l'impôt de la société à 209, 219, 221 et 221 bis. Or 221, 7, a écarte tout IS lors d'un changement de forme ou d'activité « qui conserve le droit de la France d'imposer les bénéfices différés ». Une société qui devient société de personnes, renonce à l'option de 239 ou 1655 sexies (renonciation désormais libre et réitérable) ou devient exonérée reste sous la compétence fiscale française. Elle peut donc soutenir que le 7, a s'applique : aucun IS sur ses bénéfices différés, que l'IS ne pourra plus jamais atteindre. Le 7, b ne vise que la perte du droit d'imposer, notion territoriale. En sens inverse, le deuxième alinéa du 2 de 221, maintenu, déclenche la cessation lorsque la société cesse d'être soumise « au taux prévu au deuxième alinéa du I de l'article 219 » (25 %). Ce taux ne s'applique plus aux sociétés du régime nouveau (taux du 2 du V) : le critère est désormais inopérant ou équivoque. 221 bis subordonne seulement la continuité des sursis et plus-values latentes à la possibilité d'imposer sous le nouveau régime.

**Autres options.** Rendre l'option de 239 et 1655 sexies irrévocable pendant cinq exercices pour les entités qui conservent des bénéfices différés. Cela recrée une contrainte que la réforme a voulu supprimer ; ce n'est pas recommandé.

**À préserver.** La neutralité de l'entrée dans le régime de distribution ; la libre renonciation à l'option de 239 ; la continuité de 221 bis pour les sursis et plus-values ; les exceptions de 208 C et 208, 3° nonies ; l'imposition personnelle de 111 bis.

### RT-DOMIS-08 — Renvois au « II de l'article 216 » abrogé (209 XI 1, 220 4)

**Correction proposée.** Dans 209 XI 1 et dans le 4 de l'article 220, remplacer « II de l’article 216 » et « II de l'article 216 » par « IV de l’article 216 », et, au 4 de 220, « dans les conditions de ce même II » par « dans les conditions de ce même IV ».

**Justification.** Le projet de 216, en sa version courante, a rétabli les subdivisions historiques : le II est « Abrogé » ; l'inscription au compte protégé et sa remise en cause figurent au IV. 209 XI 1 et 220, 4 renvoient encore au « II de l'article 216 ». La note de 223 B relève le premier renvoi ; aucune note ne relève le second.

**Autres options.** Aucune.

**À préserver.** Le contenu de 216 IV.

### RT-DOMIS-09 — Établissement stable et prêts à une mère étrangère : report indéfini plausible

**Correction proposée.** Au XII de l'article 209, après la deuxième phrase, insérer : « Pour l'établissement stable, l'excédent, apprécié à la clôture de chaque exercice, des fonds et valeurs mis à la disposition du siège ou des autres parties de l'entreprise sur les fonds et valeurs reçus d'eux au cours de l'exercice constitue un prélèvement de bénéfices, à concurrence des bénéfices différés non protégés de l'établissement, sauf si cet excédent correspond au paiement de dettes ou de prestations réelles. » Au c du 1 du V de l'article 219, ajouter : « La convention de prêt consentie à un associé ou à une entreprise liée établie hors de France stipule une échéance et un intérêt de pleine concurrence ; à défaut, la mise à disposition est présumée définitive, sauf preuve contraire. »

**Justification.** Pour un établissement stable, le « prélèvement effectif de bénéfices » est la seule distribution possible, puisqu'il n'existe pas de personne distincte. Or le XII de 209 exclut tout transfert de fonds qui « conserve à la France son droit d'imposer les bénéfices différés ». La France conserve ce droit tant que les bénéfices restent attribués à l'établissement : la remontée de trésorerie vers le siège n'est alors jamais une distribution. De même, une filiale peut prêter durablement sa trésorerie à une mère étrangère solvable. Le c du 1 du V de 219 met à la charge de l'administration la preuve d'une absence de capacité ou d'intention de remboursement. Dans les deux cas, l'IS est différé sans terme, alors que l'économie de la mère ou du siège dispose des fonds.

**Autres options.** Ne rien changer et chiffrer le report, en assumant l'option de l'orientation pour les prêts professionnels.

**À préserver.** Les prêts, avances de trésorerie, comptes courants et crédits commerciaux réels ; l'absence de taxation de toutes les relations commerciales liées.

### RT-DOMIS-10 — Tranche PME : cumul possible de deux plafonds pour un même exercice d'origine

**Correction proposée.** Au 3 du V de l'article 219, après « ne consomme pas la tranche de l’exercice de distribution », insérer : « ; la tranche de l’exercice de distribution utilisée sur des bénéfices d’un autre exercice est imputée sur le plafond de l’exercice d’origine de ces bénéfices, de sorte que les bénéfices d’un même exercice ne bénéficient du taux réduit que dans la limite de 42 500 € ajustée à sa durée ».

**Justification.** Le 3 du V de 219 ouvre, chaque période de douze mois, une tranche de 42 500 € de base distribuée au taux de 15 %, sans en préciser l'origine. Il conserve aussi 15 % pour la fraction éligible de chaque exercice d'origine, « diminué des fractions ayant déjà bénéficié de ce taux au titre du même exercice ». Le 209 XI 2 laisse l'entreprise choisir le compartiment débité. Si la tranche de l'exercice N est imputée sur des bénéfices de N-1 relevant du taux normal, la fraction éligible propre à N reste protégée : on ne sait pas si elle a bénéficié du taux « au titre du même exercice ». Le bénéfice de N peut ainsi recevoir deux fois 42 500 € à 15 %. L'orientation exige un plafond explicite.

**Autres options.** Si l'auteur veut au contraire un cumul, l'écrire expressément et le chiffrer.

**À préserver.** La protection de la fraction éligible de l'exercice d'origine (correction favorable de la seconde passe) ; le plafond unique du groupe ; les conditions du b du I.

### RT-DOMIS-11 — Directive mère-fille : qualification de retenue à la source à écarter clairement

**Correction proposée.** Au 2 du V de l'article 219, remplacer « soit 20/80 du montant net attribué au bénéficiaire avant sa fiscalité personnelle » par « l’impôt étant assis sur le bénéfice de la société, avant impôt, affecté à cette distribution ; pour une fraction entièrement taxable, sans déficit imputé, son montant est égal à 20/80 du montant net attribué ». La règle reste la même, mais l'assiette (bénéfice de la société) passe avant la formule de calcul.

**Justification.** L'article 5 de la directive 2011/96/UE exonère de retenue à la source les bénéfices distribués à une mère de l'Union. La Cour retient trois critères pour qualifier une retenue : fait générateur lié à la distribution, montant proportionnel à la distribution, redevable porteur des titres. Les deux premiers sont réunis : l'impôt est liquidé sur le montant net attribué (20/80), au mois de la mise à disposition. Seul le troisième, le redevable étant la société, écarte la qualification (Burda). Le 219 l'affirme, et le contrôle du lot réserve la question. La rédaction « 20/80 du montant net attribué » renforce pourtant le lien avec le dividende.

**Autres options.** Obtenir une analyse juridique dédiée avant adoption, ce que le lot prévoit déjà.

**À préserver.** Le taux, la formule, l'exonération de retenue de 119 ter.

### RT-DOMIS-12 — Sociétés patrimoniales passives : report de l'impôt sur les revenus du patrimoine, à chiffrer

**Correction proposée.** Aucune correction de texte imposée : l'orientation a tranché. Correction documentaire minimale : faire figurer dans l'étude de chiffrage un scénario dédié aux sociétés dont l'actif est principalement composé de titres de portefeuille, de liquidités ou d'immeubles non affectés à l'exploitation.

**Justification.** Une personne physique qui loge dans une société à l'IS des placements passifs (loyers, intérêts, plus-values, dividendes français de portefeuille, protégés sans seuil) ne supporte plus aucun impôt tant qu'il n'y a pas de distribution. Aujourd'hui, ces revenus supportent l'IR et les prélèvements sociaux chaque année s'ils sont détenus en direct, ou 25 % d'IS s'ils sont détenus en société. L'orientation exclut expressément de conditionner le report à l'investissement. Le chiffrage imposé par l'orientation doit cependant isoler ces déplacements d'assiette. Aucun texte ne les distingue, et aucune mesure n'en permet le suivi.

**Autres options.** Si l'auteur le souhaite, une imposition annuelle distincte, au taux de 20 %, des seuls revenus passifs des sociétés à prépondérance patrimoniale contrôlées par des personnes physiques, à la manière d'un régime distinct maintenu au 12 de 206. Cela restreindrait l'orientation et suppose une décision expresse.

**À préserver.** L'absence d'IS sur les bénéfices conservés des entreprises exploitantes ; l'absence de délai de réinvestissement.

### Dépendances entre corrections

- La correction de RT-DOMIS-03 (1668, 219 VI 2, 206 12) doit viser le f du 1 du V de 219 si celle de RT-DOMIS-02 est retenue.
- RT-DOMIS-01 ajoute une option annuelle payée selon 1668 1 à 5 ; le premier alinéa de 1668 doit alors être modifié une seule fois, pour 01 et 03 ensemble.
- RT-DOMIS-07 ajoute un alinéa au 1 du V de 219, après le e, comme RT-DOMIS-02. Il faut les numéroter ensemble : f pour les charges, puis un alinéa non numéroté pour la cessation d'assujettissement, ou g.
- RT-DOMIS-05 et RT-DOMIS-06 dépendent du même choix : maintenir la protection sans seuil des dividendes français. Si l'auteur la restreignait, les deux risques diminueraient, mais une faveur du projet serait supprimée.
- RT-DOMIS-06 vise 119 ter, dont la version courante expire le 1er janvier 2027 (RT-FUTFISC-01).

## 8. Alertes examinées et écartées (non comptées)

- **Rachats au-delà des apports (219 V 1 d)** : l'impôt peut frapper un prix de rachat supérieur aux réserves. C'est voulu : sans cette règle, une société pourrait s'endetter pour racheter ses titres, puis rembourser la dette, ce qui n'est pas une distribution, sur ses bénéfices futurs, et vider ainsi ses bénéfices sans IS. Alerte écartée ; le risque d'imposer une valeur sans bénéfice reste à signaler dans l'étude d'impact.
- **Remontées entre sociétés d'un groupe** : la filiale paie l'IS lorsqu'elle distribue à sa mère, puis la redistribution est protégée. Il n'y a donc qu'un niveau d'impôt, sans cascade : conforme à l'orientation. Les besoins de trésorerie du groupe peuvent passer par des prêts réels (219 V 1 c).
- **Participation des salariés (L3324-1)** : coordonnée par un IS évalué fictivement, sans dette. Écarté.
- **Crédits étrangers non reportables (220)** : suivis avec le compartiment jusqu'à la distribution (220 6). Écarté.
- **CIR et crédits remboursables** : leur remboursement n'est ni subordonné à une distribution ni reporté (223 O 4, 1668 7). Écarté.
- **Contribution exceptionnelle (article 48) et 235 ter ZC** : écartées pour les faits nouveaux, faits anciens conservés. Écarté.
- **Transition des réserves anciennes et des sursis** : 209 XI 1 et XIII, 206 12, 219 VI 3, 221 bis : pas de seconde imposition, sursis suivis jusqu'à leur dénouement. Écarté.
- **Arithmétique** : les douze cas de `controle-arithmetique.json` ont été recontrôlés à la main sur trois cas (normal, PME et dépassement de plafond, plafond de déficit à 1 M€ + 50 %). Exacts.

## 9. Incertitudes restantes et éléments non examinés

- **Textes européens et jurisprudence de la CJUE** : non relus en ligne (EUR-Lex inaccessible par l'outil le 26 octobre 2026). Les numéros d'affaires et les dates sont cités de mémoire et doivent être vérifiés avant tout usage. Cela concerne RT-DOMIS-01, 02, 05, 06 et 11.
- **Mécanique GloBE** : rattachement des impôts couverts aux exercices, ajustements postérieurs, notion d'« avantage lié » à un impôt national complémentaire qualifié. Non vérifiée sur la directive ni sur les commentaires de l'OCDE.
- **Articles lus seulement par extraits ciblés** : 145 (1 à 9), 221 (1 à 6), 223 B, 223 I, 223 L, 223 S, 223 VK (hors 29° à 39°), 209 B, 205 B, 205 C, 205 D, 212 bis (I à IX), 38, 39, 210 A, 158 (au-delà du 5), 239 bis AB, 1655 sexies et annexe III 46 quater-0 ZJ bis.
- **Non lus** : 208 C, 207 (au-delà des métadonnées), 1655 ter, 223 C à H, 223 N, 223 R, 223 T, 223 U, 238 et 220 quinquies (hors notes), 223 Q (hors extraits), 235 ter ZC, 1668 B et 1668 D (hors métadonnées et contrôle du lot), 200 A, 117 quater, 199 ter B, 244 quater B, 220 B, annexe II 40 à 47 et 171 I à O, annexe III 358 à 381 ter et 366 L/M, annexe IV 23 H, et la plupart des quelque 230 articles du périmètre de recherche : régimes sectoriels 44 sexies et suivants, 39 decies, 210 B à F, 217, 238 bis, 239 nonies, etc. Leur cohérence avec le noyau n'est pas attestée.
- **Conventions fiscales** : compatibilité individuelle non examinée (report de l'imputation des crédits étrangers, qualification des prélèvements des établissements stables).
- **Chiffrage** : aucun. Le report d'impôt et les comportements (RT-DOMIS-12) ne sont pas mesurés.
- **Statut `pending`** : 1668, 1668 B, 1668 D, 1655 sexies, 1763 C, L3324-1. Ces propositions peuvent encore changer.

## 10. Couverture réelle

- **Lus en entier (proposition, motif, notes ; source quand utile)** : CGI 206, 209, 219 (proposition entière), 1668, 216, 221 bis, 111 bis, 109, 110, 111, 112, 117, 119 bis, 187, 119 ter, 220 (source et proposition), 223 VJ (source et proposition), 223 WW (source et proposition), 223 WB, 223 WC, 223 O ; travail L3324-1 ; article 48 de la LF 2025 (manifeste) ; pièces du lot is-distribution.
- **Lus par extraits motivés** : voir § 9, ainsi que 223 A (III à V), 239 (option), 205, 39 (14), 38 (12), 210 A (3 d et 7), 212 bis (X), 238 A, 223 VK (29° à 39°) et 145 (10 et 11).
- **Non lus** : voir § 9.
- **Proportion du périmètre de recherche lue de fond** : environ 45 articles sur environ 230, dont tous les articles centraux du domaine désignés par la consigne, sauf 223 VK (lecture partielle), 145 (lecture partielle) et l'annexe II.
- **Preuves** : `evidence/cited/20261026T230545Z/` (fichiers listés par objection dans `DOM-IS.json`).
