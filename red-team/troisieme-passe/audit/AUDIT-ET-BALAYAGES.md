# Audit aléatoire et balayages par famille — 29 octobre 2026

## 1. Audit par échantillon aléatoire (mesure avant balayages)

- **Échantillon** : 309 articles tirés au hasard parmi les 30 314 de l'inventaire (graine 20261029), stratifiés par code et par niveau (législatif ou réglementaire). Liste : `audit/sample.json`.
- **Lecture** : texte de production après les corrections du 29 octobre, par dix agents indépendants qui ont lu « comme un juriste » l'article, ses renvois et ses textes d'application, sans consulter le registre avant de qualifier. Détail : `audit/U01` à `U10`.
- **Résultat :**
  - **12 défauts grossiers sur 309**, soit **4,0 % ± 2,2 %** des articles (intervalle à 95 %, pondéré par strate) ;
  - 53 défauts mineurs (défauts grossiers et mineurs : 21 %) ;
  - 9 des 12 défauts grossiers étaient inconnus du registre.
- **Familles** : surtout des renvois (F3, 8 cas sur 12) : renvois morts hérités, ou renvois à un alinéa décalé par une proposition. Viennent ensuite les versions futures (F4, 3 cas). Le cas « la loi supprime, le décret maintient » (F1) n'apparaît qu'une fois.
- **Code du travail** : aucun défaut grossier sur 115 articles tirés.

## 2. Balayages par famille

`tools/sweeps.py` produit, sur la production, des pistes mécaniques par famille :
- **S1** : un décret cite une loi abrogée ;
- **S2** : une sanction cite un article abrogé ;
- **S3** : un numéro est introuvable (échantillon de 40) ;
- **S4** : la proposition affirme à tort une abrogation différée ;
- **S5** : la version suivante n'a pas de proposition ;
- **S7** : un renvoi désigne un alinéa décalé ;
- **S8** : un renvoi vise un article abrogé entre 2009 et 2026.

S'y ajoutent les 12 défauts de l'audit. Au total : 803 articles et 1 127 pistes, répartis en 14 groupes disjoints, puis qualifiés un à un sur la production (`audit/sweeps/`, `apply/W01` à `W14`).

| Qualification | Pistes |
|---|---|
| faux positif | 560 |
| déjà réglé | 282 |
| défaut mineur | 131 |
| défaut grossier | 154 |

Défauts grossiers par famille : S5 67, S8 36, S7 15, F3 14, AUDIT 12, S1 4, F4 3, S2 3.

**145 lignes de correction appliquées** avec l'outil gardé du projet, dont les propositions sur versions futures (S5), les renvois rectifiés (S7, S8), les sanctions et formalités alignées (S1, S2) et les 12 défauts de l'audit. 321 tests passent. Aucune réécriture de style, aucune orientation politique modifiée, aucune formalité ni sanction de remplacement.

## 2 bis. Seconde mesure après les balayages

- **Échantillon** : second tirage aléatoire indépendant de 314 articles. Les articles du premier échantillon en sont exclus. La graine est 20261030 et l'allocation est la même. Liste : `audit/sample-2.json`.
- **Lecture** : dix agents à l'aveugle (`audit/V01` à `V10`), sur la production après les balayages.

| | Défauts grossiers | Grossiers et mineurs |
|---|---|---|
| Audit 1 (avant balayages) | 12 / 309, **4,0 % ± 2,2** | 21,1 % ± 4,6 |
| Audit 2 (après balayages) | 9 / 314, **2,9 % ± 1,9** | 22,1 % ± 4,5 |

- **Évolution du taux** : il baisse d'environ un quart, mais les intervalles se recouvrent. La baisse n'est pas établie statistiquement sur des échantillons de cette taille.
- **Évolution des familles** : les renvois morts ou décalés, visés par les balayages, reculent. Les **contradictions entre deux propositions (F5)** passent au premier plan, avec quatre cas sur neuf : par exemple, L200-8 supprime la comptabilité séparée des sociétés d'habitat participatif alors que L202-2 la maintient. Ces contradictions sont plus difficiles à détecter mécaniquement.
- **Défauts inconnus** : 6 des 9 défauts grossiers étaient inconnus.
- **Probabilité pour un juriste** qui lit 20 articles de sa matière de tomber sur au moins un défaut grossier : environ 44 %, contre environ 56 % avant les balayages.

## 3. Ce qui reste

- Une **nouvelle mesure** sur un échantillon aléatoire indépendant, tiré hors du premier, pour vérifier la baisse du taux.
- **S3** (numéros introuvables) : l'échantillon de 40 montre surtout des renvois à d'autres codes ; il n'est pas balayé en entier.
- **S6** (désignations de la loi de réforme) : 60 formules différentes, dont « loi portant la présente réforme » (1 452 occurrences), « loi instituant le contrat de travail unique » (394) et « loi instituant le contrat unique » (338). Une désignation unique est un choix de rédaction à arrêter.
- Les défauts mineurs (notes et motifs) ne sont corrigés que sur les articles déjà modifiés.

Revue IA, sans validation par un juriste.
