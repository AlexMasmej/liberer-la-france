# R1 : demandes de correction du palier A (paquet `audit/tier-a/requests-R1.json`)

13 demandes lues. Chaque article visé et ses liens ont été relus en production, en lecture seule, le 30 octobre 2026. Les changements en attente ont été cherchés dans tous les dossiers de `apply/`.

## Appliquées (6)

| Demande | Article | Dossier | Ce qui change |
|---|---|---|---|
| TA-T016-03 (T016) | CGI 197 A (LEGIARTI000037985917) | `apply/T017ra/` | Le b ne commence plus par « Par dérogation à l'article 164 A, ». 164 A proposé admet désormais les charges du revenu global des non-résidents. Le reste du b est inchangé. Le bilan d'impact ne cite pas ce passage. |
| TA-T043-02 (T043) | Annexe IV 50 quaterdecies-0 A (LEGIARTI000026447160) | `apply/R1/` | Le tarif majoré pour défaut de classement ou de calibrage ne vaut plus que pour les faits générateurs antérieurs, comme le prévoit le 2 du V de 302 bis WA proposé. Les trois tableaux sont conservés avec toutes leurs cellules. Ligne : `normative_reduction` et `coordination_only`. |
| TA-T052-01 (T052) | Annexe IV 121 KL ter (LEGIARTI000006301571) | `apply/R1/` | La source est reprise sans changement, puis bornée aux formules délivrées avant l'abrogation de 916 A. Les relevés déjà faits restent conservés et les obligations autonomes sont réservées. |
| TA-T088-01 (T088) | CSS D311-1 (LEGIARTI000054949011) | `apply/Y04ra/` | Le 16° vise les associations et centres qui étaient agréés au moment de l'abrogation de 1649 quater C à O (loi n° 2025-127). Il ne renvoie plus aux articles abrogés. L'affiliation est conservée, sans extension. Les notes erronées sont corrigées. |
| TA-T117-03 (T117) | CGI 1671, version en vigueur (LEGIARTI000041471931) | `apply/A1ra/` | Le représentant fiscal est « désigné » et non plus « accrédité », sans accréditation préalable, ce qui aligne la loi sur 357 H bis proposé. Les accréditations délivrées et les demandes en cours valent désignation. La ligne passe de `retained_unchanged` à `rewrite_draft` (`normative_reduction`, `coordination_only`). |
| TA-T129-01 (T129) | Annexe IV 93 H quater E (LEGIARTI000006301517) | `apply/R1/` | Abrogation (`full_repeal`) : il s'agit de la conservation des registres et états d'un droit de timbre de dimension supprimé depuis 2006. Les obligations du LPF et les droits antérieurs sont réservés. |

## Non appliquées : déjà réglées par un changement en attente (7)

| Demande | Article | Changement en attente |
|---|---|---|
| TA-T008-01 | CGI 71 (LEGIARTI000054373841) | `apply/T007/`, TA-T007-01 : même 1° bis et même `removed_provisions`. La transition générale couvre déjà les exercices antérieurs. La phrase transitoire supplémentaire serait redondante. |
| TA-T013-02 | Annexe III 41 duovicies K (LEGIARTI000038700156) | `apply/T095/`, TA-T095-01 : texte identique à la demande. |
| TA-T029-02 | Annexe III 46 quater-0 ZK (LEGIARTI000045766216) | `apply/Y17tdx/`, TA-T102-01 : renvoi recalé sur le III de 223 A (vérifié) et note remplacée. |
| TA-T041-03 | Annexe IV 50 sexies D (LEGIARTI000006300410) | `apply/T125/`, TA-T041-03 : texte, motif et note identiques à la demande. |
| TIERA-T081-02 | Annexe II 242-0 C (LEGIARTI000030066036) | `apply/Y15tde/`, TIERA-T083-01 : le renvoi au 3 de 287 est daté et rattaché au 8. |
| TIERA-T083-02 | Annexe III 266 bis (LEGIARTI000030829535) | `apply/T109/`, TIERA-T083-02 : le 1° du I renvoie à la déclaration de l'article 287. |
| TA-T108-03 | Annexe II 289 (LEGIARTI000054363092) | `apply/B09tdg/`, RT-T085-289 : le 32° est abrogé pour l'avenir, le 33° est conservé. |

Aucune fusion n'a été nécessaire : les changements en attente contenaient déjà la correction demandée.

## Points laissés à l'auteur

- **197 A :** faut-il admettre aussi, pour le calcul du taux moyen, les autres charges du revenu global ? Ce serait une extension de faveur non décidée.
- **121 KL ter :** si le relevé d'identité est une protection antifraude autonome, c'est 916 A proposé qui doit céder. LPF L. 102 B est hors corpus.
- **D311-1 :** une autre option n'a pas été retenue : limiter le 16° aux fonctions exercées avant la suppression de l'agrément.
- **1671 :** la version 2027 (LEGIARTI000053188936) fait l'objet d'une demande distincte du paquet R2.
- **Dépendances :**
  - 93 H quater E suppose l'abrogation de 93 H quater C et D, en attente dans T129. Elle reste juste même sans elle, puisque le droit est éteint depuis 2006.
  - 121 KL ter renvoie à 121 KL bis, borné dans T130.

## Contrôle

`python3 -B apply/check_changes.py` renvoie `problems: []` pour R1, T017ra, Y04ra et A1ra. Diagnostics : changements de longueur voulus (bornage, abrogation).

Revue IA, sans validation par un juriste.
