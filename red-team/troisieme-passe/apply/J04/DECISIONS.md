# J04 — quatrième balayage (S9x, S12, S15) : décisions

Texte lu : production, en lecture seule (`CITE_PRODUCTION=1 python3 -I tools/cite.py`), le 29 octobre 2026. Pour chaque piste, j'ai lu en entier l'article du paquet (source, proposition, motif, notes) ainsi que la proposition et les `removed_provisions` de la loi qu'il cite. Revue IA, sans validation par un juriste.

## Bilan

- 68 pistes sur 64 articles : 56 déjà réglées, 12 faux positifs, 0 défaut G, 0 défaut m sur la piste elle-même.
- Corrections : aucune. `changes.json` est vide et `python3 -B apply/check_changes.py J04` renvoie `problems: []`.
- R1237-6-1 (propriétaire précédent : B04) n'a pas besoin de correction, donc aucun dossier de variante `apply/B04jd/` n'a été créé.
- Défauts mineurs relevés en passant (notes ou motifs périmés, F10 ; un retour à la ligne manquant, F7) : ils ne sont pas corrigés, parce que la règle n'autorise ces corrections que sur un article déjà modifié. Ils sont listés à la fin et dans `audit/sweeps/J04.json` (`incidental_observations`).

Les pistes S9x sont « déjà réglées » quand la proposition du décret porte déjà, en toutes lettres, la suppression décidée par la loi (le texte source aurait été un défaut). Elles sont des « faux positifs » quand le décret n'a jamais organisé la disposition retirée : article maintenu à renvoi dynamique, fonction utile distincte, ou mots partagés sans rapport.

## Une ligne par piste

| Article | Piste | Loi citée | Qualification | Correction |
|---|---|---|---|---|
| R7413-4 (LEGIARTI000018521017) | S9x/F1+F5 | L1234-1 | déjà réglé | non : aucun défaut |
| D7112-1 (LEGIARTI000018521951) | S9x/F1+F5 | L1234-9 | déjà réglé | non : aucun défaut |
| D7112-1 (LEGIARTI000018521951) | S9x/F1+F5 | L7112-3 | déjà réglé | non : aucun défaut |
| D5424-65 (LEGIARTI000018524796) | S9x/F1+F5 | L5422-16 | déjà réglé | non : aucun défaut |
| D5424-65 (LEGIARTI000018524796) | S9x/F1+F5 | L5424-20 | déjà réglé | non : aucun défaut |
| R5214-22 (LEGIARTI000018525810) | S9x/F1+F5 | L5214-2 | déjà réglé | non : aucun défaut |
| R4152-13 (LEGIARTI000018532779) | S9x/F1+F5 | L1225-33 | déjà réglé | non : aucun défaut |
| R3332-12 (LEGIARTI000018533132) | S9x/F1+F5 | L3315-2 | déjà réglé | non : aucun défaut |
| R3262-13 (LEGIARTI000018533502) | S9x/F1+F5 | L3262-5 | déjà réglé | non : aucun défaut |
| R2523-4 (LEGIARTI000018534830) | S9x/F1+F5 | L2522-1 | faux positif | non : aucun défaut |
| R1263-8 (LEGIARTI000018537078) | S9x/F1+F5 | L1251-43 | déjà réglé | non : aucun défaut |
| R1233-1 (LEGIARTI000018537694) | S9x/F1+F5 | L1233-43 | déjà réglé | non : aucun défaut |
| R1232-1 (LEGIARTI000018537724) | S9x/F1+F5 | L1232-2 | déjà réglé | non : aucun défaut |
| R1227-6 (LEGIARTI000018537738) | S9x/F1+F5 | L1225-33 | déjà réglé | non : aucun défaut |
| R1225-18 (LEGIARTI000018537778) | S9x/F1+F5 | L1225-66 | déjà réglé | non : aucun défaut |
| D1222-1 (LEGIARTI000018537848) | S9x/F1+F5 | L1222-5 | déjà réglé | non : aucun défaut |
| D1251-1 (LEGIARTI000019668669) | S9x/F1+F5 | L1251-6 | déjà réglé | non : aucun défaut |
| D3171-11 (LEGIARTI000019725811) | S9x/F1+F5 | L3171-2 | déjà réglé | non : aucun défaut |
| R3261-8 (LEGIARTI000020080253) | S9x/F1+F5 | L3261-3 | déjà réglé | non : aucun défaut |
| D5424-45 (LEGIARTI000022357299) | S9x/F1+F5 | L5424-19 | déjà réglé | non : aucun défaut |
| R3262-36 (LEGIARTI000023155181) | S9x/F1+F5 | L3262-3 | déjà réglé | non : aucun défaut |
| D6325-29 (LEGIARTI000025049837) | S9x/F1+F5 | L6325-6-2 | déjà réglé | non : aucun défaut |
| R6227-7 (LEGIARTI000025684847) | S9x/F1+F5 | L6222-35 | déjà réglé | non : aucun défaut |
| R5134-56 (LEGIARTI000026566002) | S9x/F1+F5 | L5134-67-2 | déjà réglé | non : aucun défaut |
| R5134-17 (LEGIARTI000026566093) | S9x/F1+F5 | L5134-20 | faux positif | non : aucun défaut |
| R5312-14 (LEGIARTI000028975743) | S9x/F1+F5 | L5312-5 | déjà réglé | non : aucun défaut |
| R3332-21-2 (LEGIARTI000030776884) | S12/F4 | L3332-17-1 | faux positif | non : aucun défaut |
| R7331-10 (LEGIARTI000031394622) | S9x/F1+F5 | L7331-3 | déjà réglé | non : aucun défaut |
| R3124-3 (LEGIARTI000033471459) | S9x/F1+F5 | L3121-27 | déjà réglé | non : aucun défaut |
| D3171-13 (LEGIARTI000033515985) | S9x/F1+F5 | L3171-2 | déjà réglé | non : aucun défaut |
| D3171-12 (LEGIARTI000033515990) | S9x/F1+F5 | L3171-2 | déjà réglé | non : aucun défaut |
| R23-112-11 (LEGIARTI000034524036) | S9x/F1+F5 | L23-112-4 | faux positif | non : aucun défaut |
| R23-112-12 (LEGIARTI000034524038) | S9x/F1+F5 | L23-112-4 | faux positif | non : aucun défaut |
| R2231-1-1 (LEGIARTI000034594332) | S9x/F1+F5 | L2231-5-1 | déjà réglé | non : aucun défaut |
| R1234-1 (LEGIARTI000035644687) | S9x/F1+F5 | L1234-9 | déjà réglé | non : aucun défaut |
| R1234-2 (LEGIARTI000035644692) | S9x/F1+F5 | L1234-9 | déjà réglé | non : aucun défaut |
| D2232-2 (LEGIARTI000036191604) | S9x/F1+F5 | L2232-12 | déjà réglé | non : aucun défaut |
| D2232-3 (LEGIARTI000036195209) | S9x/F1+F5 | L2232-12 | déjà réglé | non : aucun défaut |
| D2241-2 (LEGIARTI000036222784) | S9x/F1+F5 | L2241-11 | déjà réglé | non : aucun défaut |
| D1237-9 (LEGIARTI000036247093) | S9x/F1+F5 | L1237-19-4 | déjà réglé | non : aucun défaut |
| D1237-9 (LEGIARTI000036247093) | S9x/F1+F5 | L1237-19-1 | déjà réglé | non : aucun défaut |
| R4163-34 (LEGIARTI000036404987) | S9x/F1+F5 | L4163-18 | déjà réglé | non : aucun défaut |
| R4163-39 (LEGIARTI000036404997) | S9x/F1+F5 | L4163-18 | déjà réglé | non : aucun défaut |
| R4163-7 (LEGIARTI000036409891) | S9x/F1+F5 | L1251-43 | faux positif | non : aucun défaut |
| R5151-3 (LEGIARTI000036409997) | S9x/F1+F5 | L3243-2 | déjà réglé | non : aucun défaut |
| R2312-43 (LEGIARTI000036413318) | S9x/F1+F5 | L2316-23 | déjà réglé | non : aucun défaut |
| R2312-49 (LEGIARTI000036413334) | S9x/F1+F5 | L2315-61 | faux positif | non : aucun défaut |
| R2312-51 (LEGIARTI000036413338) | S9x/F1+F5 | L2312-84 | déjà réglé | non : aucun défaut |
| R2312-57 (LEGIARTI000036413353) | S9x/F1+F5 | L2315-76 | faux positif | non : aucun défaut |
| D2315-34 (LEGIARTI000036433849) | S9x/F1+F5 | L2315-61 | faux positif | non : aucun défaut |
| D2316-6 (LEGIARTI000036434439) | S9x/F1+F5 | L2315-76 | déjà réglé | non : aucun défaut |
| D2316-7 (LEGIARTI000036434441) | S9x/F1+F5 | L2316-23 | déjà réglé | non : aucun défaut |
| R7524-2 (LEGIARTI000037563343) | S9x/F1+F5 | L7232-8 | déjà réglé | non : aucun défaut |
| D6222-21-1 (LEGIARTI000037876487) | S9x/F1+F5 | L6222-18 | déjà réglé | non : aucun défaut |
| R2271-1 (LEGIARTI000038026691) | S9x/F1+F5 | L2271-1 | déjà réglé | non : aucun défaut |
| D6111-6 (LEGIARTI000038701972) | S9x/F1+F5 | L6111-6 | faux positif | non : aucun défaut |
| R3341-5 (LEGIARTI000038895163) | S15/F5 | — | faux positif | non : aucun défaut |
| R4163-33 (LEGIARTI000039223162) | S9x/F1+F5 | L4163-16 | déjà réglé | non : aucun défaut |
| R4163-45 (LEGIARTI000039344647) | S9x/F1+F5 | L4163-18 | déjà réglé | non : aucun défaut |
| R3326-1 (LEGIARTI000039344704) | S9x/F1+F5 | L3326-1 | déjà réglé | non : aucun défaut |
| R2523-7 (LEGIARTI000039652590) | S9x/F1+F5 | L2523-1 | déjà réglé | non : aucun défaut |
| R1237-6-1 (LEGIARTI000041541504) | S9x/F1+F5 | L1237-19 | déjà réglé | non : aucun défaut |
| R6222-21 (LEGIARTI000041771333) | S9x/F1+F5 | L1234-9 | déjà réglé | non : aucun défaut |
| R6222-21 (LEGIARTI000041771333) | S9x/F1+F5 | L6222-18 | déjà réglé | non : aucun défaut |
| R6226-3 (LEGIARTI000041771529) | S9x/F1+F5 | L1251-16 | déjà réglé | non : aucun défaut |
| D6274-1 (LEGIARTI000041824968) | S9x/F1+F5 | L6222-18 | déjà réglé | non : aucun défaut |
| R6123-27 (LEGIARTI000042907356) | S9x/F1+F5 | L6111-6 | faux positif | non : aucun défaut |
| D5132-10-5-3 (LEGIARTI000043991802) | S9x/F1+F5 | L5132-5 | déjà réglé | non : aucun défaut |

Le détail de chaque qualification (citations exactes avec leurs identifiants LEGIARTI) figure dans `audit/sweeps/J04.json`.

## Pistes S12 et S15

- **R3332-21-2 (S12)** : faux positif. Le mot « abrogation » vise CGI 885 O bis, pas L3332-17-1. La version de 2027 (LEGIARTI000054140237) garde le 3° du I et a déjà sa propre proposition.
- **R3341-5 (S15)** : faux positif. La « disposition législative qui la prévoit » existe en production : L3341-7 (LEGIARTI000043197156) proposé dispose « L'état récapitulatif peut être remis indépendamment du livret d'épargne salariale ».

## Défauts mineurs non corrigés (pour l'auteur)

- **R3332-21-2** (F10, m) : Notes : « La version de L3332-17-1 disponible finit au 1er janvier 2027 ; sa succession n'est pas présente dans le corpus et reste à coordonner. » Or LEGIARTI000054140237 (VIGUEUR_DIFF, 2027-01-01) figure au corpus avec une proposition (batches/third-pass-corrections/00006.json).
- **R2523-4** (F10, m) : Notes : « R2523-7 proposé conserve en revanche « une demande écrite et motivée » : coordination nécessaire hors lot ». R2523-7 (LEGIARTI000039652590) proposé dit désormais « Elle n'est soumise à aucune forme imposée ni à une motivation distincte ».
- **R2312-43** (F10, m) : Notes : « D2316-7 proposé impose toujours « comporte notamment » suivi de six rubriques ». D2316-7 (LEGIARTI000036434441) proposé : « peut comporter, à titre indicatif et sans clause type obligatoire ».
- **D2316-7** (F10, m) : Notes : « R2312-43 exige encore une « convention conforme aux dispositions réglementaires » ». R2312-43 (LEGIARTI000036413318) proposé : « Cette convention n'est soumise à aucune clause type obligatoire ».
- **D2315-34** (F10, m) : Notes : « R2312-49 9° renvoie ordinalement au cinquième alinéa de L2315-61, qui traite de l'inscription et non de la décision de transfert ». Dans L2315-61 (LEGIARTI000036761916), source et proposition, le cinquième alinéa (1° et 2° comptés) est « Le comité social et économique peut décider [...] de transférer » ; le renvoi de R2312-49 est exact.
- **R5151-3** (F7, m) : Proposition : « notamment par le biais de la statistique.Cette coordination s'applique aux bulletins remis à compter de l'entrée en vigueur » : l'alinéa transitoire est collé au 5° (retour à la ligne manquant). Sans effet sur le fond.
- **L7331-3 (hors paquet, cible)** (F10, m) : Motif : R7331-10 « précise les délais et les modalités par lesquels l'entrepreneur salarié devient associé » « reste obligatoire dans sa proposition ». R7331-10 (LEGIARTI000031394622) proposé : « peut préciser les modalités d'une éventuelle accession ».
- **L3262-5 (hors paquet, cible)** (F10, m) : Motif : pour R3262-13 et R3262-14 « aucune proposition n'est fournie pour ces deux articles dans le corpus consulté ». R3262-13 (LEGIARTI000018533502) a une proposition qui interdit le prélèvement pour les nouvelles péremptions.

## Points laissés à l'auteur

- Les notes périmées ci-dessus pourront être rafraîchies lors d'une prochaine modification de ces articles. Aucune ne change le fond.
- Aucun arbitrage politique n'est ouvert par ce paquet.

Revue IA : rien de ceci ne vaut validation par un juriste.
