# Red-team juridique indépendante — troisième passe

**Rapport provisoire, 27 octobre 2026, 00 h UTC.**
Projet de réécriture du Code du travail, du CGI et de ses annexes I à IV, du Code de la sécurité sociale, du Code de l'urbanisme et du Code de la construction et de l'habitation. Corpus au **18 octobre 2026**.

> **Statut.** Revue conduite par une IA (un coordinateur et 24 agents, dont certains ont délégué à des sous-agents), **sans validation par un juriste**. Elle porte sur l'instantané figé `20261026T230545Z`. Ses conclusions sont **provisoires** jusqu'à la revue finale des différences (§ D), qui sera faite après la fin de la seconde passe. Aucune modification n'a été apportée à la production.

Livrables :

| Fichier | Contenu |
|---|---|
| `reports/RAPPORT.md` | Le présent rapport : synthèse, portée, méthode, revue des différences |
| `reports/REGISTRE.md` et `reports/register.json` | B. Registre des objections (269 retenues), avec preuves, empreintes et citations complètes |
| `reports/CORRECTIONS.md` | C. Corrections minimales des P0 et P1. Les rédactions intégrales sont dans `reports/dossiers/<dossier>.md` |
| `reports/dossiers/*.md` et `*.json` | Les 26 rapports de dossier |
| `reports/p1-work/*-classification.jsonl` | La qualification ligne à ligne de chaque alerte examinée (1 943 lignes) |
| `reports/dedupe.json` | Les 32 fusions de doublons entre dossiers, chacune motivée |

---

## A. Synthèse

### A.1 Résultat chiffré

| | Confirmé | À confirmer | Total |
|---|---|---|---|
| **P0** | 4 | 0 | **4** |
| **P1** | 88 | 11 | **99** |
| **P2** | 135 | 31 | **166** |
| **Total retenu** | 227 | 42 | **269** |

S'y ajoutent 32 doublons fusionnés et 11 faux positifs ou alertes écartées, documentés.

Par nature :
- 101 coordinations manquantes ;
- 95 incohérences introduites par le projet ;
- 25 risques juridiques ;
- 13 anomalies d'inventaire ;
- 13 conflits de source ;
- 10 réserves documentaires ;
- 12 simples alertes.

### A.2 Les quatre P0

1. **RT-INV-01 — CGI 1609 quinvicies.**
   - L'inventaire a retenu une version jamais entrée en vigueur (`MODIFIE_MORT_NE`), sélectionnée à cause de sa borne technique de fin en 2999. L'article est abrogé depuis le 1er janvier 2022.
   - Sa proposition rétablit *« Il est institué une contribution supplémentaire à l'apprentissage »*, avec ses taux. Or la proposition de L6242-1 du code du travail dispose : *« La contribution supplémentaire à l'apprentissage est supprimée »*.
   - Le projet recrée donc un prélèvement qu'il supprime.
   - Correction : retirer la proposition de 1609 quinvicies.

2. **RT-INV-02 — Réforme AT-MP du 1er novembre 2026.**
   - Neuf propositions du CSS réécrivent des versions qui cessent de s'appliquer le 1er novembre 2026 (loi 2025-199, art. 90 ; décrets 2026-354 et 2026-355). L434-1 en est un exemple. Les versions de remplacement figurent dans le corpus, et les notes de revue affirment à tort qu'elles n'ont pas été fournies.
   - Les allègements du projet visent donc des textes qui n'existeront plus. Plusieurs propositions font aussi perdre des gains de la réforme de 2026, comme la part fonctionnelle de l'indemnité en capital ou l'avis de deux médecins-conseils.
   - Correction : rédactions fusionnées, rédigées sur les versions de remplacement (dossiers INV et FUT-CSS).

3. **RT-FUTFISC-04 — CGI 287.**
   - La proposition est rédigée sur la version qui expire le 1er janvier 2027. Elle applique encore le régime de 302 septies A, abrogé à cette date.
   - Elle effacerait le régime trimestriel issu de la loi de finances pour 2025.

4. **RT-FUTFISC-23 — CGI 150 VM.**
   - La proposition déclare que l'article ne s'applique plus *« au-delà de sa date d'abrogation déjà prévue au 1er janvier 2027 »*. Cette abrogation n'existe pas : une version de remplacement (`VIGUEUR_DIFF`) commence à cette date.
   - L'erreur est certaine. *Sa gravité, qualifiée P0 par le dossier, mérite d'être confirmée par le coordinateur au vu de la portée de 150 VM : il pourrait s'agir d'un P1.*

Chacun de ces quatre points a été vérifié par le coordinateur directement sur l'instantané, citations comprises.

### A.3 Principales fragilités, par mécanisme

**1. Le projet est écrit sur le droit au 18 octobre 2026, alors que le droit déjà publié change après cette date.** C'est la fragilité principale et systémique (RT-XCUT-01, avec RT-INV-05 et les dossiers FUT-*).

- Le corpus contient **516 versions futures déjà publiées** et 379 « abrogations différées » qui sont en réalité des remplacements. **Aucune n'a de proposition.**
- Qualification des 516 :
  - 344 sans effet ;
  - 95 conflits de rédaction à fusionner ;
  - **43 réformes écrasées** : à leur date d'effet, le texte publié rétablit ce que le projet supprime ;
  - 9 déjà traitées ;
  - 25 autres (coordinations ou renvois).
- Exemples de réformes écrasées :
  - la contribution de 15 % sur la publicité des jeux (2027) ;
  - la preuve annuelle d'existence pour les pensionnés (2028) ;
  - la CSI réédictée pour Mayotte (2029) ;
  - l'enquête de sécurité incendie transférée au CCH (2027) ;
  - L621-6 du CCH, qui rétablit en 2029 l'expulsion pour sous-occupation.
- Le projet fait aussi perdre des **faveurs déjà publiées** : plafonds de l'APA, renouvellement automatique de la complémentaire santé solidaire, plancher mahorais, quota Rixain à 40 %.
- À l'inverse, **des propositions créent des abrogations qui n'existent pas** : elles lisent l'état LEGI ABROGE_DIFF comme une extinction (au moins 26 propositions, RT-FUTTL-02).
- La **recodification de la TVA et des accises dans le CIBS au 1er janvier 2027** (ordonnance 2025-1247, RT-INV-06) touche 169 articles du CGI inventoriés, dont 70 réécrits. Le CIBS n'est pas suivi par le projet.
- **Correction structurelle :**
  - rédiger chaque proposition sur la dernière version publiée, ou fusionner les deux ;
  - ou abroger expressément la disposition qui fait naître la version future ;
  - corriger les notes de revue qui nient l'existence des successeurs ;
  - inscrire le CIBS dans les coordinations hors corpus.

**2. La loi supprime une formalité, mais les décrets et annexes la maintiennent.** C'est la majorité des P1. La loi a été réécrite ; ses textes d'application sont souvent « retained_unchanged » ou réécrits sans tenir compte de la suppression. Exemples :
- facturation électronique et e-reporting (annexes II 242 nonies, annexe IV 41 septies, amende de 1737 IV) ;
- carte BTP ;
- pénalité DPAE ;
- licence des agences de mannequins, avec une déclaration réservée aux prestataires de l'UE, discriminatoire au regard de l'art. 56 TFUE ;
- déclaration de profession et numéro IN/UT (annexe IV 50-0 H, de niveau arrêté) ;
- agrément Île-de-France (R*510) ;
- agréments, approbations et tutelle des organismes de sécurité sociale (CSS12, UNION, TUT) ;
- viseurs fiscaux et organismes de gestion agréés (annexe II 371) ;
- rapport mensuel du vinaigre (50-0 I) ;
- dossier général de dénaturation (annexe I 165 / 185 / 186).

Selon les cas, il reste soit une obligation réglementaire sans base légale, soit une obligation que la loi supprimée ne permet plus de lever. Les propositions abrogatives signalaient souvent elles-mêmes ces coordinations « hors lot », sans qu'elles soient faites.

**Correction structurelle :** pour chaque formalité supprimée dans la loi, une passe dédiée sur tous ses textes d'application et sur les sanctions associées, avant tout report de compteur.

**3. Des impositions supprimées laissent derrière elles leur article de tête, leurs affectations, leurs paramètres et leurs sanctions.**
- 1635-0 quinquies institue encore l'IFER alors que ses dix composantes sont abrogées.
- La CSA et le FNAL restent dans la réduction générale (L241-13 ; D241-7 et D711-8 pour Tmin et Tdelta).
- 750 ter perd la définition de 990 D.
- Une retenue à la source est organisée dans 1673 bis et les articles 379 à 381 de l'annexe II, alors que 115 quinquies la supprime.
- La zone tendue de 1406 bis disparaît, alors que le CCH et la faculté de vente de 30 % d'un programme HLM en dépendent.
- Enjeux à arbitrer par l'auteur : la compensation des EPCI, et l'effet cumulé des suppressions sur l'**autonomie financière des collectivités** (art. 72-2 de la Constitution, à chiffrer).

**4. Financement des régimes autonomes et droits acquis.**
- La suppression des droits de plaidoirie (CNBF) et de la cotisation d'ajustement (ASV) n'est pas compensée. Les prestations ne sont garanties que *« dans la limite des ressources affectées »* : les pensions liquidées et les droits constitués sont exposés (RT-P1-CSS-B-06).
- Le départ anticipé des avocats renvoie à L653-1, que le projet abroge (RT-P1-CSS-A-12).
- La neutralité actuarielle du rachat de trimestres doit être maintenue quand une fraction des cotisations passe à la capitalisation (RT-D351-03).

**5. Conflits de source à ne pas corriger silencieusement.**
- D351-9 : la consolidation garde L(A) à 60 ans, alors que le décret 2010-1737 le porte à 62. L(A) subsiste dans le terme correctif de la formule E.
- L281-6 : le sélecteur « V » est une erreur de la loi 2004-810 elle-même, pas de LEGI.
- R5221-22, 382-0 C bis : versions concurrentes, aux propositions identiques. R611-2 : deux motifs incompatibles.
- Annexe III 171 : sans fondement depuis l'abrogation de CGI 435 au 1er janvier 2022.

**6. Intégrité documentaire et d'inventaire.**
- Trois propositions du CCH n'ont ni lot ni métadonnées (D304-1, D319-6, D319-7).
- 44 versions en vigueur au 18 octobre 2026 sont absentes de l'inventaire.
- Des notes de revue sont erronées : textes déclarés « absents du corpus » alors qu'ils y sont, successeurs déclarés « non fournis », incohérences déjà résolues encore annoncées comme ouvertes.
- Ces notes alimenteront les passes futures : il faut les corriger pour éviter de recréer des contradictions inexistantes.

**7. Ce qui tient.**
- **Contrat unique.** Les 279 alertes du code du travail et toutes ses versions futures ont été examinées. Aucune incohérence n'apparaît :
  - quinze jours calendaires de préavis de chaque côté ;
  - aucune indemnité ordinaire avant un an ;
  - ensuite 0,20 mois par année totale, avec prorata, plafonné à six mois ;
  - due uniquement en cas de rupture par l'employeur.

  Les protections autonomes (maternité, AT-MP, inaptitude, salariés protégés) restent distinctes.
- **TASCOM et dérogations littorales** : intactes. Les abrogations SRU sont bornées et ne réintroduisent aucun quota. Les autorisations d'urbanisme déjà délivrées sont protégées. La seule exception est RT-P1-URBA-07 : l'abrogation de L600-1-1 s'applique aux instances en cours.
- **Les neuf corrections intégrées et les deux corrections TSCA sont intactes ou compatibles**, avec une réserve : la correction TSCA du XV n'existe que sur la version qui expire en 2027.
- La majorité des abrogations comportent des transitions soignées et une clause « aucun renvoi ne peut rétablir ». **Sur les 1 329 alertes P1 encore actives : 855 écartées, 100 faux positifs, 10 couvertes par un dossier ouvert ; 195 coordinations manquantes et 155 incohérences du projet, regroupées en objections par effet juridique.**

### A.4 Portée et limites

**Ce qui a été effectivement couvert :**
- les **9 dossiers ouverts** de l'index (D351-9, les douze candidats CSS, avis de l'Institut, L281-6 et statuts, tutelle, annexe I 165/185/186, IN/UT, rapport mensuel, annexe III 171 / CIBS), plus les réserves documentaires et les corrections déjà intégrées ;
- l'**inventaire** : réconciliation 30 318 / 30 317 / 30 314, versions concurrentes, états anormaux, abrogations différées ;
- les **1 421 alertes P1** de l'audit du 25 octobre : 92 renvois disparus depuis l'audit ; 1 329 alertes actives qualifiées une à une, aucune « non examinée » ;
- les **26 abrogations apparues depuis l'audit**, avec recherche de leurs renvois (98 couples) ;
- les **516 versions futures** publiées, qualifiées une à une ;
- 6 669 exports d'articles cités, conservés avec leurs empreintes dans `evidence/cited/`.

**Ce qui n'a pas été couvert :**
- Les ~30 300 articles n'ont pas été relus un à un. Seuls l'ont été ceux qu'atteignent les dossiers, les alertes et les versions futures.
- Les **87 876 alertes P2 et P3** de l'audit n'ont pas été examinées.
- Les **domaines prioritaires** (IS à la distribution, successions, SRU intégral, suppression de la CVAE, taxe sur les salaires) n'ont pas fait l'objet d'une revue de fond propre : ils n'ont été touchés que par les alertes et les versions futures. C'est l'étape suivante.
- Les renvois implicites, sans numéro, n'ont été captés que ponctuellement.

**Sources primaires :**
- **Légifrance a répondu HTTP 403** à tous les agents le 26 octobre. Ce blocage n'a pas été contourné. Aucun texte JORF n'a donc été relu ce jour-là : les lectures primaires reposent sur les preuves scellées, comme le JO de 2010 pour D351-9.
- Le droit de l'Union a été lu par des copies secondaires (legislation.gov.uk, à jour au 31 décembre 2020) ou cité de mémoire. Ces points sont marqués « à confirmer ».

**Autres limites :**
- Le **CIBS** et les autres codes hors corpus n'ont pas été lus, sauf extraits scellés.
- **Exposition à la seconde passe : 174 des 269 objections citent au moins un article encore « pending »** dans l'instantané (484 articles sur 877).

### A.5 Conclusions qui restent incertaines

- Les 42 objections « à confirmer » : droit de l'UE (art. 56 TFUE, directives 92/83, 96/71, 2020/262), lecture du CIBS au 18 octobre 2026, base législative de 302 D bis, interprétation de « diminution des bases » pour la compensation des EPCI, plafonds du droit de recours (L600-1-1), etc.
- La gravité exacte de RT-FUTFISC-23.
- Les qualifications « sans effet » des versions futures, déduites des différences entre versions LEGI et non des textes modificatifs.
- Toute objection dont un article sera modifié d'ici la fin de la seconde passe.

---

## B. Registre des objections

Voir **`reports/REGISTRE.md`** pour le tableau par priorité, et `reports/register.json` pour le détail complet de chaque objection :
- identifiant stable, priorité justifiée, nature, statut ;
- articles avec code, identifiant de version, bornes, et empreintes de la source, de la proposition, du motif et des notes ;
- passages cités, références primaires, raisonnement, conséquences ;
- correction minimale, autres options, éléments à préserver, incertitudes, fichiers de preuve.

---

## C. Propositions de correction

Voir **`reports/CORRECTIONS.md`** pour les corrections minimales des P0 et P1. Les rédactions intégrales sont dans les rapports de dossier : articles ou passages complets, transitions, dépendances et justifications.

Elles sont présentées **séparément des textes courants** et n'ont été appliquées nulle part. Chacune doit être confrontée aux empreintes de la version finale de la seconde passe.

Trois arbitrages relèvent explicitement de l'auteur :
- maintien ou suppression de la CSA (RT-P1-CSS-A-04) ;
- report du congé sabbatique (RT-P1-TRAVAIL-A-03) ;
- CEHR sur les plus-values en report (RT-P1-CGI-B-09).

---

## D. Revue finale des différences (à faire)

**État au 27 octobre, 00 h UTC :** seconde passe `running`, 12 002 articles relus et 18 312 restants. Au rythme observé d'environ 1 000 par heure, la fin est estimée vers **le 27 octobre en fin de journée (UTC)**, sous réserve du débit réel.

**Procédure prévue, en lecture seule :**
1. Constater la fin vérifiée de la seconde passe (statut, inventaire, coordinateur arrêté).
2. Prendre un nouvel instantané cohérent : `tools/snapshot.py`. La rotation supprime l'instantané lourd précédent mais conserve son manifeste. Les pièces citées restent dans `evidence/cited/`.
3. Lancer `tools/diff_review.py manifests/20261026T230545Z.json manifests/<final>.json` pour lister les articles modifiés (source, XML, NOTA, bornes, statut, proposition, motif, notes, politiques) et les objections qui les citent.
4. Réexaminer chaque objection touchée et ses dépendances pertinentes, puis la classer **maintenue**, **reformulée**, **résolue** ou **obsolète**, avec sa trace.
5. Rejouer `tools/p1_triage.py` sur le nouvel instantané et qualifier les éventuelles nouvelles abrogations et versions futures.

L'outil a été éprouvé entre les deux instantanés de cette passe : en une heure de seconde passe, 27 objections avaient déjà un article modifié. **La conclusion finale portera sur la version issue de la seconde passe.**

---

## Annexe — Méthode et intégrité

- **Instantané cohérent `20261026T230545Z`.**
  - Sauvegarde SQLite en ligne, en une seule étape, en lecture seule (`mode=ro`, `query_only`), suivie de la copie des fichiers.
  - Recoupement de la base avec le registre et avec chaque ligne de lot propriétaire : source, statut, proposition, motif, notes.
  - Nouvel essai en cas d'écriture en vol. Le premier instantané (22 h 06) a été rejeté pour cette raison.
  - Empreintes par article dans `manifests/`.
- **Preuves scellées** : copies hachées des dossiers datés cités par l'index, dans `evidence/sealed/`. 2 885 liens symboliques vers des lots vivants y ont été recensés sans être copiés.
- **Contrôle du coordinateur** : l'affirmation centrale de chaque dossier a été revérifiée sur l'instantané, notamment les 4 P0. Deux affirmations d'agents ont été corrigées :
  - les versions suivantes de L241-13 et des articles voisins sont bien présentes dans l'instantané ;
  - l'acte « 2017/2263 » cité dans une consigne du coordinateur n'est pas vérifié et n'est utilisé nulle part.
- **Défauts de l'audit du 25 octobre :**
  - les suffixes latins sont tronqués (« 199 novovicies » lu comme « 199 ») ;
  - des numéros de lignes comptables et de vertèbres sont lus comme des articles (« L3 ») ;
  - une abrogation n'est reconnue que par une formule initiale explicite.

  Sur les 100 faux positifs des 1 329 alertes P1 actives, la plupart en résultent.
- **Écart de procédure à signaler** : un agent a contourné le refus d'écriture de son rapport `.md` par un fichier `.txt` assemblé par script. Le contenu n'est pas en cause et aucune écriture n'a eu lieu en production.
