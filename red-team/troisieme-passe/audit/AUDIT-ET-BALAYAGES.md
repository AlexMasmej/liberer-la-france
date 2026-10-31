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

## 2 sexies. Cinquième mesure et cinquième balayage

| Mesure | Défauts grossiers | Grossiers et mineurs |
|---|---|---|
| Audit 5 (après la quatrième ronde) | 10 / 314, **3,2 % ± 1,9** | 22,6 % ± 4,6 |

Échantillon : `sample-5.json`, graine 20261102, tiré hors des 1 251 articles déjà lus.

- **Pas de baisse confirmée.** La baisse de l'audit 4 (2,5 %) tenait au hasard de l'échantillon. Sur cinq mesures, on compte 51 défauts grossiers sur 1 565 articles, soit **3,3 %**.
- **Les 10 défauts sont corrigés** (groupe X6 et cinq variantes, 23 lignes). Exemples :
  - taux « réduit » de 24 % des organismes sans but lucratif, devenu supérieur au taux normal de 20 % (CGI 219 bis) ;
  - chapeau de CGI 200 qui, lu à la lettre, ouvrait la réduction de 66 % à tout don ;
  - régimes réécrits sans base légale (emplois-jeunes, conventions de 1649 quater N, rescrit Agefiph).
- **Lacune de méthode trouvée.** Les pistes S1, S2 et S8 ne lisaient que les numéros L, R, D et A. Elles n'avaient donc rien produit dans le CGI et ses annexes. `tools/sweeps5.py` lit les numéros du CGI.
- **Cinquième balayage** (groupes M01 à M09, 365 articles, 548 pistes) : S1c, S2c, S8c (CGI), S16 (base légale éteinte, autres codes) et S17. S17 réexamine les 166 pistes de balayages antérieurs qualifiées « m » sans correction.
  - Résultats : 114 pistes G (21 %), 135 m, 104 déjà réglées, 195 faux positifs. Ces pistes ont donné **74 lignes appliquées**, dont 13 abrogations pour l'avenir des régimes emplois-jeunes et prime de retour à l'emploi (X7).
  - **S17 donne 56 G** : les premiers balayages avaient classé « m » des renvois morts qu'un juriste juge grossiers. Le seuil de qualification a été resserré pour ce balayage.
- **Total de la cinquième ronde** : 97 lignes appliquées ; 321 tests OK.

## 2 septies. Sixième mesure et sixième balayage

| Mesure | Défauts grossiers | Grossiers et mineurs |
|---|---|---|
| Audit 6 (après la cinquième ronde) | 13 / 314, **4,1 % ± 2,2** | 15,3 % ± 4,0 |

Échantillon : `sample-6.json`, graine 20261103, tiré hors des 1 565 articles déjà lus.

- **Pas de baisse.** Sur six mesures, on compte 64 défauts grossiers sur 1 879 articles, soit **3,4 % ± 0,8**. D'un audit à l'autre, le taux oscille entre 2,5 % et 4,1 %, dans la marge d'un échantillon de 314.
- **Une ronde peut créer des défauts.** Trois des 13 défauts viennent de l'annexe II, articles 371 (organismes agréés). La cinquième ronde y avait abrogé une partie des articles sans base légale, mais les articles voisins organisaient encore l'agrément. Le groupe X8 traite désormais les chapitres en entier : annexe II 371 et CSS R135 (Fonds de solidarité vieillesse, supprimé en 2026). Il a appliqué 81 lignes.
- **Sixième balayage** (`tools/sweeps6.py`, groupes Z01 à Z07, 292 articles, 365 pistes) :
  - S16b : base légale éteinte, filtre de transition resserré ;
  - S18 : article qui s'appuie sur un voisin abrogé ;
  - S19a : alinéa décalé par une version future publiée ;
  - S19b : adaptation locale future sans proposition, par exemple à Mayotte.

  Résultats : 25 pistes G, 28 m, 151 déjà réglées, 161 faux positifs. Ces pistes ont donné 23 lignes, plus 6 lignes de fermeture (X9, X10 et variantes).
- **Contrôle de régression.** Après application, on cherche les articles non abrogés qui citent l'un des 115 articles abrogés par les rondes 5 et 6. Le contrôle a donné 5 pistes : 2 défauts, corrigés, et 3 faux positifs.
- **Total de la sixième ronde** : 110 lignes appliquées ; 321 tests OK.

## 2 octies. Lecture systématique, palier A : articles réécrits du CGI et de ses annexes

Les six audits donnaient aux articles réécrits du CGI et de ses annexes le taux le plus haut : 9 % pour le CGI et 12 % pour les annexes. Ces taux reposent sur de petits échantillons (76 et 128 articles), donc à ± 5 points près. Ce palier lit donc chacun de ces articles.

- **Périmètre** : 2 740 articles réécrits en vigueur, soit 1 310 du CGI et 1 430 des annexes I à IV. Les articles déjà lus par les audits sont exclus.
  - `tools/tier_a.py` les répartit en 132 paquets, groupes T001 à T132, suivant l'ordre des sections, pour que chaque lecteur voie une section entière.
  - Le brief des lecteurs est `BRIEF-LECTURE.md`. Le résultat de chaque paquet est dans `audit/tier-a/T*.json`.
- **Résultat** : 96 défauts grossiers (**3,5 %**), 383 mineurs et 2 261 articles sans défaut. Avec les mineurs, on arrive à 17,5 %, comme dans les audits.
  - Le taux de défauts grossiers est bien plus bas que les 9 à 12 % attendus. Deux raisons, dont on ne peut pas séparer le poids :
    - les rondes 4 à 6 ont surtout corrigé le CGI et ses annexes, avant cette lecture ;
    - un lecteur qui parcourt une section entière classe peut-être moins souvent en défaut grossier qu'un auditeur qui tire des articles au hasard.
- **Corrections** : 81 lignes appliquées (53 dossiers), dont 16 corrections que les lecteurs ont demandées sur des articles hors de leur paquet. Les groupes R1 à R3 les ont traitées.
  - Les 21 autres demandes étaient déjà couvertes par une correction en attente ailleurs, sauf une, écartée comme défaut mineur.
- **Restent ouverts** (10) :
  - **TVA recodifiée au CIBS (environ 9 cas : 289 A, 293 A, 293 D, 296 ter, 298, 298 nonies, 298 sexdecies D et I…)**. Le projet écrit sa réforme dans des subdivisions du CGI que l'ordonnance n° 2025-1247 abroge au 1er janvier 2027, pour les reprendre dans le code des impositions sur les biens et services (CIBS). La loi de réforme ne pouvant entrer en vigueur avant cette date, ces réformes resteraient sans effet. Le CIBS n'est pas au corpus. La correction suppose de l'y ajouter, ou d'écrire la réforme dans une disposition non codifiée.
  - **1518 A sexies** : arbitrage déjà laissé à l'auteur (RT-FUTFISC-30).
- **Contrôle d'alignement** : les corrections qui ajoutent des mots de formalité ou d'impôt ont été relues. Toutes retirent une formalité, gardent une transition ou reportent la réforme sur une version future.

## 4. Taux mesuré et ce qu'il signifie

- **Taux mesuré** : environ **3 % des articles** gardent un défaut qu'un juriste remarquerait. Sur six mesures indépendantes, on compte 64 défauts grossiers sur 1 879 articles (3,4 % ± 0,8). Aucune tendance à la baisse n'est mesurable d'une ronde à l'autre. Il s'agit surtout de contradictions entre deux propositions, de renvois et de décrets d'application non alignés. Le reste ne présente pas de défaut grossier.
- **Probabilité pour un juriste** qui lit 20 articles de sa matière de tomber sur au moins un défaut grossier : environ une chance sur deux.
- **Pourquoi les rondes ne font pas baisser le taux mesuré** : environ 1 000 articles sur 30 000 gardent un défaut grossier. Une ronde en corrige 50 à 110, soit une baisse attendue d'environ 0,3 point. C'est en dessous de ce qu'un audit de 314 articles peut détecter (± 2 points).
- **Ce qu'il faudrait pour descendre nettement sous 3 %** : une lecture systématique, article par article. Aucun signal mécanique ne concentre plus assez les défauts restants pour qu'un balayage ciblé suffise.
  - Elle a commencé par les articles réécrits du CGI et de ses annexes (palier A, § 2 octies) : 2 740 articles lus, 96 défauts grossiers trouvés, et tous corrigés sauf 10.
  - Restent les articles réécrits des autres codes, environ 11 400.
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

- La **lecture systématique** des autres articles réécrits.
  - **Palier A**, CGI et annexes : fait, voir § 2 octies.
  - **Palier B**, construction-habitation et sécurité sociale : environ 5 500 articles, à faire.
  - **Palier C**, travail et urbanisme : environ 5 900 articles, à faire.
- Le **CIBS** n'est pas au corpus. Les réformes de TVA écrites dans des subdivisions du CGI abrogées au 1er janvier 2027 restent sans effet (§ 2 octies).
- Le **reste des pistes S9 larges** hors annexes (environ 2 000 articles au score faible), non balayé.
- **S3** (numéros introuvables) : l'échantillon de 40 montre surtout des renvois à d'autres codes ; il n'est pas balayé en entier.
- **S6** (désignations de la loi de réforme) : 60 formules différentes, dont « loi portant la présente réforme » (1 452 occurrences), « loi instituant le contrat de travail unique » (394) et « loi instituant le contrat unique » (338). Une désignation unique est un choix de rédaction à arrêter.
- Les défauts mineurs (notes et motifs) ne sont corrigés que sur les articles déjà modifiés.

Revue IA, sans validation par un juriste.
