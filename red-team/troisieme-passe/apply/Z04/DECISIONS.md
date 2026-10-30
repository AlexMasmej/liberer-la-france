# Z04 : balayage S16b / S18 (sixième balayage), code du travail

Paquet : `audit/sweeps/packet-Z04.json`, 43 articles, 55 pistes (22 S16b/F3, 33 S18/F1+F5). Texte lu en production, en lecture seule (`CITE_PRODUCTION=1 python3 -I tools/cite.py`, sqlite `mode=ro`), le 2026-10-30. Chaque article a été lu en entier, ainsi que l'article cité par chaque piste (source, proposition, motif).

## Résultat

- **0 défaut G, 0 défaut m** sur les pistes du paquet ; **aucune correction** (`changes` vide).
- **27 faux positifs** :
  - 21 pistes S16b renvoient à un **autre code**. Le CSS est cité expressément : L231-9, L231-12, L422-3, L412-3, L213-1, L225-1, L411-1 et L411-2 y sont en vigueur et ne sont pas abrogés par le projet. Les autres renvoient au code rural (L723-2), au CESEDA (L422-1, L422-2, L422-5), au code de la route (L213-1) ou au code du tourisme (L411-1). L'outil les a confondus avec les numéros homonymes du code du travail, éteints en 1982, 2004 ou 2008.
  - 6 pistes S18 visent un renvoi qui figure seulement dans un régime transitoire ou historique : L6222-18 (×2), L5213-13-3 et L5132-6. S'y ajoutent une borne de plage toujours utile (L5422-1, « L. 1237-17 à L. 1237-19-14 ») et une exclusion (R3324-16, « à l'exception [...] D. 3325-1 à R. 3326-1 »).
- **28 déjà réglés** : la proposition actuelle a déjà retiré le renvoi opératoire à l'article abrogé. Il ne reste qu'une clause de transition ou de non-rétablissement (« ne rétablit aucun… », « uniquement pour les périodes antérieures », « n'est pas exigée »).
- Pas de dossier de variante : les deux articles qui ont un `previous_owner` sont R5221-20 (B07, renvois au CESEDA) et R6332-25 (A6, déjà réglé). Ils n'appellent aucune correction.
- Aucune `request`. Pistes croisées vérifiées en passant : D6331-70 (LEGIARTI000038023454) vise déjà « R. 6332-30 à R. 6332-32 ». Rien n'a été touché à l'annexe II 371 ni au chapitre R135 du CSS (groupe X8).

## Une ligne par piste

| Article (version) | Famille | Renvoi | Qualification | Correction |
|---|---|---|---|---|
| R4163-37 (LEGIARTI000036404993) | S16b/F3 | L231-9 | faux positif | non |
| R4643-37 (LEGIARTI000036483888) | S16b/F3 | L4612-16 | déjà réglé | non |
| L6111-6-1 (LEGIARTI000037370938) | S18/F1+F5 | D6111-7 | déjà réglé | non |
| L1251-58-5 (LEGIARTI000037379978) | S18/F1+F5 | L1251-35 | déjà réglé | non |
| L6222-18 (LEGIARTI000037386025) | S18/F1+F5 | L1243-4 | faux positif | non |
| L6222-18 (LEGIARTI000037386025) | S18/F1+F5 | L1243-8 | faux positif | non |
| L5422-3 (LEGIARTI000037388297) | S18/F1+F5 | L5422-11 | déjà réglé | non |
| L1233-68 (LEGIARTI000037388640) | S18/F1+F5 | L1243-13 | déjà réglé | non |
| L351-5-1 (LEGIARTI000038314413) | S18/F1+F5 | L321-4-2 | déjà réglé | non |
| R6261-20 (LEGIARTI000039115769) | S18/F1+F5 | R6251-4 | déjà réglé | non |
| R6261-20 (LEGIARTI000039115769) | S18/F1+F5 | R6261-19 | déjà réglé | non |
| L3347-1 (LEGIARTI000042009015) | S18/F1+F5 | L3344-3 | déjà réglé | non |
| R8112-6 (LEGIARTI000043128414) | S16b/F3 | L422-3 | faux positif | non |
| L6331-55 (LEGIARTI000043701729) | S18/F1+F5 | L6331-6 | déjà réglé | non |
| L6131-1 (LEGIARTI000043709709) | S18/F1+F5 | L6331-6 | déjà réglé | non |
| L4624-8-2 (LEGIARTI000043890473) | S18/F1+F5 | L4622-9-3 | déjà réglé | non |
| L4641-2-1 (LEGIARTI000043891901) | S18/F1+F5 | L4622-9-3 | déjà réglé | non |
| L2316-2 (LEGIARTI000043975175) | S18/F1+F5 | L2312-51 | déjà réglé | non |
| L6333-1 (LEGIARTI000044375694) | S18/F1+F5 | L6331-6 | déjà réglé | non |
| L3142-24 (LEGIARTI000044628245) | S18/F1+F5 | L3142-17 | déjà réglé | non |
| R8241-2 (LEGIARTI000045680893) | S16b/F3 | L412-3 | faux positif | non |
| R7343-102 (LEGIARTI000046322268) | S18/F1+F5 | R7343-101 | déjà réglé | non |
| L1271-5 (LEGIARTI000047293375) | S18/F1+F5 | L1242-13 | déjà réglé | non |
| D5212-5 (LEGIARTI000047480910) | S16b/F3 | L213-1 | faux positif | non |
| L5213-13-3 (LEGIARTI000048589910) | S18/F1+F5 | L1251-12-1 | faux positif | non |
| L5132-6 (LEGIARTI000048590314) | S18/F1+F5 | L1251-12-1 | faux positif | non |
| L5422-1 (LEGIARTI000048590547) | S18/F1+F5 | L1237-19-14 | faux positif | non |
| L5422-24 (LEGIARTI000048600595) | S18/F1+F5 | L5422-11 | déjà réglé | non |
| L6332-1-2 (LEGIARTI000048700917) | S18/F1+F5 | L6331-69 | déjà réglé | non |
| R5213-86-4 (LEGIARTI000049123990) | S18/F1+F5 | R5213-72 | déjà réglé | non |
| D5316-11 (LEGIARTI000049776788) | S18/F1+F5 | D5316-9 | déjà réglé | non |
| R3324-16 (LEGIARTI000049905634) | S18/F1+F5 | D3325-1 | faux positif | non |
| R5221-20 (LEGIARTI000049999760) | S16b/F3 | L422-1 | faux positif | non |
| R5221-20 (LEGIARTI000049999760) | S16b/F3 | L422-2 | faux positif | non |
| R5221-20 (LEGIARTI000049999760) | S16b/F3 | L422-5 | faux positif | non |
| R5523-15-43 (LEGIARTI000050742418) | S18/F1+F5 | D5132-18-1 | déjà réglé | non |
| R5523-15-43 (LEGIARTI000050742418) | S18/F1+F5 | D6211-3 | déjà réglé | non |
| R6323-41 (LEGIARTI000050919896) | S16b/F3 | L213-1 | faux positif | non |
| R6323-41 (LEGIARTI000050919896) | S16b/F3 | L225-1 | faux positif | non |
| R6323-41 (LEGIARTI000050919896) | S16b/F3 | L723-2 | faux positif | non |
| R6523-28 (LEGIARTI000050924442) | S16b/F3 | L213-1 | faux positif | non |
| R6523-28 (LEGIARTI000050924442) | S16b/F3 | L225-1 | faux positif | non |
| R6523-28 (LEGIARTI000050924442) | S16b/F3 | L723-2 | faux positif | non |
| D6523-1-1 (LEGIARTI000050971404) | S16b/F3 | L213-1 | faux positif | non |
| D6235-10 (LEGIARTI000051395713) | S18/F1+F5 | R6332-33 | déjà réglé | non |
| R6523-29 (LEGIARTI000051470304) | S16b/F3 | L213-1 | faux positif | non |
| R6523-29 (LEGIARTI000051470304) | S16b/F3 | L225-1 | faux positif | non |
| R6523-29 (LEGIARTI000051470304) | S16b/F3 | L723-2 | faux positif | non |
| R6113-16-8 (LEGIARTI000051704513) | S18/F1+F5 | R6113-15 | déjà réglé | non |
| R6113-16-9 (LEGIARTI000051704718) | S18/F1+F5 | R6113-15 | déjà réglé | non |
| D6123-26-1 (LEGIARTI000051777197) | S16b/F3 | L411-1 | faux positif | non |
| D6123-26-1 (LEGIARTI000051777197) | S16b/F3 | L411-2 | faux positif | non |
| R6332-25 (LEGIARTI000051821081) | S18/F1+F5 | R6332-25-2 | déjà réglé | non |
| R5212-19-2 (LEGIARTI000053484898) | S16b/F3 | L213-1 | faux positif | non |
| D1132-1 (LEGIARTI000054323930) | S16b/F3 | L411-1 | faux positif | non |

Les citations exactes et les identifiants LEGIARTI de chaque piste sont dans `audit/sweeps/Z04.json`.

## Points pour l'auteur

- Le motif de L351-5-1 (LEGIARTI000038314413) relève que L351-3-1 et L351-21, cités dans la source, sont des numéros éteints en 2008. Cet article résiduel de l'ancien code est hors piste. Défaut de source sans effet nouveau : non corrigé.
- Les notes de R6332-33 (LEGIARTI000037934331) disent encore que D6235-10 et D6331-70 doivent être coordonnés, alors que c'est fait en production. C'est un F10, sur un article hors paquet : non corrigé.

Contrôle : `python3 -B apply/check_changes.py Z04`, `problems: []`. Revue IA, sans validation par un juriste.
