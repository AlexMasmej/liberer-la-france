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

## 2 ter. Troisième balayage : contradictions entre propositions

Ce balayage vise la famille passée au premier plan dans la seconde mesure (F5), avec deux pistes mécaniques :
- **S9** : un décret ou une annexe applique une loi réduite par le projet et mentionne encore une formalité du même type que celle retirée de la loi (964 pistes) ;
- **S10** : une proposition déroge à une autre proposition (échantillon de 150 pistes sur 1 134).

Les pistes, réparties sur 916 articles en 18 groupes disjoints (`apply/Y01` à `Y18`), se répartissent ainsi :

| Qualification | Pistes |
|---|---|
| faux positif | 607 |
| déjà réglé | 457 |
| défaut mineur | 20 |
| défaut grossier | 33 |

**33 corrections appliquées**, surtout dans les annexes du CGI. Le Code du travail, le CSS et le CCH n'en comptent presque plus. Les dérogations entre propositions (S10) sont propres : un seul défaut sur 150 pistes. **Le rendement est d'environ 3 % des pistes, contre 14 % au balayage précédent** : la famille « la loi retire, le décret garde » est presque épuisée.

## 2 quater. Troisième mesure, objections P2 et pilote « notes »

| Mesure | Défauts grossiers | Grossiers et mineurs |
|---|---|---|
| Audit 1 (avant balayages) | 12 / 309, **4,0 % ± 2,2** | 21,1 % ± 4,6 |
| Audit 2 (après le deuxième balayage) | 9 / 314, **2,9 % ± 1,9** | 22,1 % ± 4,5 |
| Audit 3 (après le troisième balayage) | 12 / 314, **3,8 % ± 2,1** | 17,7 % ± 4,1 |

- **Le taux de défauts grossiers plafonne autour de 3,5 %** : 33 sur 937 articles tirés au hasard dans les trois mesures. Les défauts mineurs reculent. Les balayages corrigent bien la famille qu'ils visent, mais les défauts restants sont dispersés.
- **Défauts connus mais non corrigés** : environ la moitié des défauts grossiers de l'audit 3 étaient déjà connus. Il s'agissait d'objections P2 du registre, ou de volets de P1 non appliqués. Ces 12 défauts sont corrigés (43 lignes).
- **Objections P2** : les 157 objections P2 retenues ont ensuite été traitées sur le texte de production, avec le même critère d'alignement que les P1. Elles ont donné **201 lignes appliquées**. Une partie était déjà réglée par les corrections antérieures. Les autres n'ont pas été appliquées, chacune avec son motif : arbitrage, texte hors corpus ou point à confirmer (`apply/B01` à `B10`).
- **Pilote « notes »** : 4 333 articles portent des notes de revue qui annoncent une coordination ouverte. Sur 250 d'entre eux, tirés au hasard :
  - 60 % des notes sont périmées (la coordination est faite) ;
  - 21 % visent un texte hors corpus ;
  - 15 % relèvent d'un défaut mineur ;
  - 4,8 % révèlent un défaut grossier, à peine plus que la lecture au hasard.

  Le balayage complet n'a donc pas été lancé. Les 12 défauts du pilote sont corrigés.

## 2 quinquies. Quatrième mesure et quatrième balayage

| Mesure | Défauts grossiers | Grossiers et mineurs |
|---|---|---|
| Audit 4 (après les P2 et le pilote) | 8 / 314, **2,5 % ± 1,7** | 14,6 % ± 3,9 |

Échantillon : `sample-4.json`, graine 20261101, tiré hors des 937 articles déjà lus.

- **Les 8 défauts** (K011, K041, K202, K058, K098, K260, K290, K299) sont corrigés (groupe X4 et une variante, 17 lignes), ainsi que 4 constats incidents d'audits antérieurs restés sans correction.
- **Ce que l'audit a appris sur la méthode** : deux de ces défauts étaient déjà repérés. L'un figurait comme constat incident d'un audit antérieur, l'autre comme piste S9 écartée par un filtre trop étroit (liste fixe de mots de formalité).
- **Quatrième balayage** (`tools/sweeps4.py`, groupes J01 à J16, 854 articles, 918 pistes). Il porte sur cinq familles tirées des défauts de l'audit :
  - S9x : décret qui reprend les mots de ce que la loi a retiré ;
  - S9a : annexes du CGI appliquant un article réduit ;
  - S12 : abrogation affirmée à tort d'un autre article ;
  - S13 : renvoi à un « n° » disparu ;
  - S15 : effet suspendu à une modification législative non faite.

  Résultats : 45 pistes G (4,9 %), 15 m, 395 déjà réglées, 463 faux positifs. Ces pistes ont donné **47 lignes appliquées**, dont 3 demandes croisées (X5).
- **Point faible repéré : les annexes du CGI.** Les pistes S9a y donnent 20 G sur environ 450. Plusieurs décrets d'application y organisent encore des états, des délais ou des justificatifs que l'article du CGI réécrit a supprimés.
- **Total de la quatrième ronde** : 64 lignes appliquées ; 321 tests OK.

## 4. Taux mesuré et ce qu'il signifie

- **Taux mesuré** : environ **3 % des articles** gardent un défaut qu'un juriste remarquerait. Sur quatre mesures indépendantes, on compte 41 défauts grossiers sur 1 251 articles (3,3 %), et la dernière mesure donne 2,5 % ± 1,7. Il s'agit surtout de contradictions entre deux propositions, de renvois et de décrets d'application non alignés. Le reste ne présente pas de défaut grossier.
- **Probabilité pour un juriste** qui lit 20 articles de sa matière de tomber sur au moins un défaut grossier : environ une chance sur deux.
- **Ce qu'il faudrait pour descendre sous 1 %** : une lecture systématique de l'ensemble des articles, ou au moins des articles réécrits les plus importants. Aucun signal mécanique ne concentre plus assez les défauts restants pour qu'un balayage ciblé suffise.
- **Les signalements extérieurs ont le meilleur rendement mesuré** : 9 des 11 issues du premier contributeur visaient un vrai défaut. Voir ci-dessous comment signaler une erreur.

## 5. Signaler une erreur

Ouvrez une issue sur le dépôt avec :
- l'article (code, numéro et identifiant LEGIARTI) ;
- la date de lecture ;
- le passage exact ;
- le problème, en le rattachant si possible à une famille : contradiction loi/décret, renvoi mort ou décalé, sanction orpheline, version future, transition, droit supérieur ;
- la correction proposée.

Chaque issue est triée contre le registre, corrigée si elle relève d'une contradiction ou d'une faille, et close avec un lien vers le commit. Les demandes qui changeraient une orientation du projet sont expliquées et closes comme non retenues.

## 3. Ce qui reste

- Une **cinquième mesure**, pour confirmer que la baisse de l'audit 4 (2,5 %) ne tient pas au hasard de l'échantillon.
- Le **reste des pistes S9 larges** hors annexes (environ 2 000 articles au score faible), non balayé.
- **S3** (numéros introuvables) : l'échantillon de 40 montre surtout des renvois à d'autres codes ; il n'est pas balayé en entier.
- **S6** (désignations de la loi de réforme) : 60 formules différentes, dont « loi portant la présente réforme » (1 452 occurrences), « loi instituant le contrat de travail unique » (394) et « loi instituant le contrat unique » (338). Une désignation unique est un choix de rédaction à arrêter.
- Les défauts mineurs (notes et motifs) ne sont corrigés que sur les articles déjà modifiés.

Revue IA, sans validation par un juriste.
