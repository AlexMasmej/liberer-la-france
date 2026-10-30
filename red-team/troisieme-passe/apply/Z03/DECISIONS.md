# Z03 : sixième balayage, code du travail (pistes S16b et S18), décisions

Texte lu : la production, en lecture seule (`CITE_PRODUCTION=1 python3 -I tools/cite.py` et SQLite `mode=ro`), le 30 octobre 2026. Paquet : `audit/sweeps/packet-Z03.json`, soit 43 articles du code du travail et 54 pistes (42 S18, 12 S16b). Contrôle : `python3 -B apply/check_changes.py Z03` donne 1 ligne construite, 1 validée et `problems` vide. Les diagnostics sont voulus : abrogation déclarée (`full_repeal`) et renvois ajoutés à L8112-1 et R8111-1, tous deux en vigueur et maintenus.

Rien n'a été écrit en production. Cette revue a été faite par une IA. Elle ne vaut pas validation par un juriste.

## Bilan

| Qualification | Pistes |
|---|---|
| G | 1 (R212-12), corrigé |
| m | 2 (L1221-14, R4532-97), non corrigés |
| déjà réglé | 36 |
| faux positif | 15 |

Corrections : 1 ligne en mode `replace` (R212-12). Aucune demande à un autre groupe. Rien d'écarté (`skipped` vide). Aucun dossier de variante : les deux articles qui ont un `previous_owner` (D5427-13 et R1253-43, groupe B05) sont déjà réglés.

Règle appliquée : la plupart des pistes S18 visent un renvoi vers un article abrogé pour l'avenir par le contrat unique ou par une suppression de formalité. Quand le renvoi ne sert plus qu'aux contrats ou aux faits antérieurs, ou que la proposition l'a déjà retiré, la piste est « déjà réglée » ou « faux positif ». Les pistes S16b sur des numéros d'autres codes (CSS, code de l'éducation, CRPA, COJ) sont des faux positifs.

## Défaut confirmé et corrigé

- **R212-12** (LEGIARTI000018513896), article maintenu de l'ancienne partie réglementaire. Piste S16b vers L611-4. Qualification : G (F3).
  - **Défaut.** L'article confie au ministre chargé des transports et aux inspecteurs des transports « les attributions conférées par les dispositions de la présente section », pour les entreprises « énumérées à la fin de l'article L. 611-4 ».
    - L'ancien L611-4 (LEGIARTI000006650429) est abrogé depuis le 1er mai 2008.
    - Tous les autres articles de la section (anciens R212-1 à R212-14) ont pris fin au plus tard à cette date.
    - L'article ne répartit donc plus aucune attribution. Le projet le maintenait pourtant tel quel, au motif d'un risque de « contrôles sans rattachement ».
  - **Correction.**
    - Abrogation pour l'avenir (`full_repeal`, bilan `coordination_only`).
    - Les actes, procédures et recours antérieurs sont maintenus.
    - Aucune formalité de remplacement.
    - Les compétences générales de L8112-1 et R8111-1 sont rappelées.
    - La note fausse sur l'ancien L611-4 (« non documentée ») est corrigée.
  - **Défaut connu.** Non : aucune objection au registre.

## Défauts mineurs (non corrigés)

- **L1221-14** (LEGIARTI000006900853), F5. « Par dérogation à l'article L. 2315-5 » vise un article abrogé pour les supports futurs. La dérogation garde une portée pour les supports déjà en service, restés sous l'ancien régime. Redondance sans effet.
- **R4532-97** (LEGIARTI000018529364), F5 et F10. La phrase sur « le renvoi de l'article R. 4532-39 » est devenue redondante depuis l'abrogation de R4532-39. Les notes citent encore l'ancien brouillon de R4532-39 (« demeurent obligatoires »).
- **Notes erronées (F10), connexes à des pistes classées autrement :**
  - L1221-12 (LEGIARTI000006900851) dit D1221-18 et D1221-19 « encore sans proposition » et R1221-13 contradictoire. Les trois sont désormais coordonnés.
  - D1442-9 (LEGIARTI000034545777) dit que L6322-7 à L6322-9 « ne figurent pas dans le corpus courant ». Ils y figurent, abrogés au 1er janvier 2019.

## Points laissés à l'auteur

- **R212-12.** Le NOTA indique que le décret n° 2008-244 l'a maintenu en vigueur avec R213-11 et R221-18 à R221-26. Ces derniers sont hors paquet et n'ont pas été examinés ; ils peuvent relever du même constat. Les textes d'organisation des services d'inspection des transports ne figurent pas au corpus. La correction ne s'appuie pas sur eux.
- **Choix de fond relevés à la lecture, hors pistes, non qualifiés.** Plusieurs propositions étendent au contrat unique une garantie autrefois propre aux CDD :
  - L1226-4-3 : indemnité spéciale d'inaptitude sans condition d'ancienneté ;
  - L1254-18 : garantie de congés de L1242-16 ;
  - L1233-72-1 et L1251-12-1 : avantages ouverts « aux situations futures ».

  Leurs notes le signalent (« élargit le champ », « coût non chiffré »). L'auteur peut vérifier que ces extensions sont voulues.

## Une ligne par piste

| Article | Piste | Cible | Qualification | Correction |
|---|---|---|---|---|
| L1221-12 (LEGIARTI000006900851) | S18/F1+F5 | L1221-11 | faux positif | non |
| L1221-12 (LEGIARTI000006900851) | S18/F1+F5 | L1221-12-1 | faux positif | non |
| L1221-14 (LEGIARTI000006900853) | S18/F1+F5 | L2315-5 | m | Non corrigé (article non modifié) |
| L1251-48 (LEGIARTI000006901304) | S18/F1+F5 | L1251-46 | déjà réglé | non |
| L2262-7 (LEGIARTI000006901816) | S18/F1+F5 | L2262-6 | déjà réglé | non |
| L3134-10 (LEGIARTI000006902632) | S18/F1+F5 | L3134-9 | déjà réglé | non |
| L3134-15 (LEGIARTI000006902637) | S18/F1+F5 | L3134-11 | déjà réglé | non |
| L5134-70 (LEGIARTI000006903608) | S18/F1+F5 | L1243-2 | déjà réglé | non |
| L7313-17 (LEGIARTI000006904739) | S18/F1+F5 | L7313-14 | faux positif | non |
| R212-12 (LEGIARTI000018513896) | S16b/F3 | L611-4 | G | Corrigé (Z03) |
| R7123-29 (LEGIARTI000018521568) | S18/F1+F5 | R7123-26 | déjà réglé | non |
| R6341-21 (LEGIARTI000018522491) | S18/F1+F5 | R6341-19 | déjà réglé | non |
| R6341-20 (LEGIARTI000018522493) | S18/F1+F5 | R6341-19 | déjà réglé | non |
| R5522-71 (LEGIARTI000018524426) | S18/F1+F5 | R5522-79 | faux positif | non |
| D5427-13 (LEGIARTI000018524668) | S18/F1+F5 | D5427-9 | déjà réglé | non |
| R5422-6 (LEGIARTI000018525121) | S18/F1+F5 | R5422-8 | déjà réglé | non |
| R5123-35 (LEGIARTI000018526954) | S18/F1+F5 | R5123-28 | déjà réglé | non |
| R4532-97 (LEGIARTI000018529364) | S18/F1+F5 | R4532-39 | m | Non corrigé (article non modifié) |
| R1253-44 (LEGIARTI000018537184) | S18/F1+F5 | D1253-4 | déjà réglé | non |
| R1253-44 (LEGIARTI000018537184) | S18/F1+F5 | D1253-6 | déjà réglé | non |
| R1253-43 (LEGIARTI000018537186) | S18/F1+F5 | D1253-7 | déjà réglé | non |
| L1226-4-3 (LEGIARTI000024024758) | S18/F1+F5 | L1243-8 | déjà réglé | non |
| R1221-12 (LEGIARTI000024214305) | S18/F1+F5 | R1221-8 | déjà réglé | non |
| L1221-25 (LEGIARTI000029144958) | S18/F1+F5 | L1242-10 | faux positif | non |
| D4622-37 (LEGIARTI000029236950) | S18/F1+F5 | D4622-36 | déjà réglé | non |
| L1254-18 (LEGIARTI000030436459) | S18/F1+F5 | L1243-10 | déjà réglé | non |
| R6341-30 (LEGIARTI000030520593) | S16b/F3 | L432-9 | faux positif | non |
| L5134-25-1 (LEGIARTI000031087287) | S18/F1+F5 | L5134-23-2 | déjà réglé | non |
| R8113-3-1 (LEGIARTI000031392050) | S16b/F3 | L124-8 | faux positif | non |
| R8113-3-1 (LEGIARTI000031392050) | S16b/F3 | L124-10 | faux positif | non |
| R8113-3-1 (LEGIARTI000031392050) | S16b/F3 | L124-13 | faux positif | non |
| R8113-3-1 (LEGIARTI000031392050) | S16b/F3 | L124-14 | faux positif | non |
| L8252-2 (LEGIARTI000032171278) | S18/F1+F5 | L1243-4 | déjà réglé | non |
| L8252-2 (LEGIARTI000032171278) | S18/F1+F5 | L1243-8 | déjà réglé | non |
| L5132-14 (LEGIARTI000033024468) | S18/F1+F5 | L1255-6 | déjà réglé | non |
| L1254-9 (LEGIARTI000033024484) | S18/F1+F5 | L1254-15 | déjà réglé | non |
| R3142-25 (LEGIARTI000033509603) | S18/F1+F5 | R3142-29 | déjà réglé | non |
| R7232-12 (LEGIARTI000033747445) | S18/F1+F5 | R7232-9 | déjà réglé | non |
| R1262-14 (LEGIARTI000033769259) | S18/F1+F5 | R4624-50 | faux positif | non |
| R8124-21 (LEGIARTI000034423329) | S16b/F3 | L311-1 | faux positif | non |
| D1442-9 (LEGIARTI000034545777) | S16b/F3 | L6322-7 | déjà réglé | non |
| D1442-9 (LEGIARTI000034545777) | S16b/F3 | L6322-9 | déjà réglé | non |
| R1423-50-1 (LEGIARTI000034652024) | S16b/F3 | L123-3 | faux positif | non |
| R5141-12 (LEGIARTI000034728034) | S16b/F3 | L213-1 | faux positif | non |
| D1442-23 (LEGIARTI000035525267) | S16b/F3 | L141-2 | faux positif | non |
| L1243-12 (LEGIARTI000035644025) | S18/F1+F5 | L1242-8 | déjà réglé | non |
| L1243-12 (LEGIARTI000035644025) | S18/F1+F5 | L1242-8-1 | déjà réglé | non |
| L1251-34 (LEGIARTI000035644080) | S18/F1+F5 | L1251-12-1 | déjà réglé | non |
| L1251-30 (LEGIARTI000035644083) | S18/F1+F5 | L1251-12-1 | déjà réglé | non |
| L1233-72-1 (LEGIARTI000036261982) | S18/F1+F5 | L1243-13 | déjà réglé | non |
| L1233-72-1 (LEGIARTI000036261982) | S18/F1+F5 | L1243-13-1 | déjà réglé | non |
| L1251-40 (LEGIARTI000036262126) | S18/F1+F5 | L1251-12-1 | déjà réglé | non |
| L1251-40 (LEGIARTI000036262126) | S18/F1+F5 | L1251-35 | déjà réglé | non |
| L1251-40 (LEGIARTI000036262126) | S18/F1+F5 | L1251-35-1 | déjà réglé | non |

Revue IA : rien de ceci ne vaut validation par un juriste.
