# Inventaire du contrat unique — lecture seule

Les 11 593 entrées du Code du travail exportées ont été rapprochées de leur source canonique en base : aucune divergence de contenu, d’empreinte ou de notes. Les propositions sont prises dans une transaction de lecture seule de la base, plus récente que certains champs de l’export. L’inventaire cartographie 1 539 entrées, dont 549 possèdent déjà une proposition. Il distingue 242 sources et notes relues intégralement des simples candidats de structure ou de renvoi ; il ne déclare pas ces 1 539 articles juridiquement relus ou réécrits.

## Noyau proposé : quarante-cinq articles, aucun doublon avec le lot CDD

- Création : **L1221-2**.
- Essai : **L1221-19, L1221-20, L1221-21, L1221-22, L1221-23, L1221-24, L1221-25, L1221-26**, avec l’adaptation de **L1524-1** à Mayotte.
- Articulation générale de la rupture : **L1231-1**.
- Préavis, indemnité, ancienneté, force majeure et droit local : **L1234-1 à L1234-18, plus L1234-17-1**.
- Démission, retraites et minimum de rupture conventionnelle : **L1237-1, L1237-6, L1237-7, L1237-10, L1237-13**.
- Calcul : **R1234-1, R1234-2, R1234-4, R1234-5**.
- Information écrite : **R1221-34**.
- Portes CDD spéciales ajoutées au noyau : **L1226-4-3, L1226-20, L1233-68, L1233-72-1, L1237-18-1**.

`source.json` contient l’intégralité des quarante-cinq sources et notes, les identifiants, les empreintes et les propositions présentes. Aucun L/R/D124* n’est inclus dans ce noyau. Les faits normatifs repérés article par article sont dans `inventaire.json`.

La décision d’auteur transmise ensuite fixe quinze jours **calendaires** pour chaque partie, un essai de trois mois sans renouvellement, une franchise d’indemnité ordinaire avant un an, puis 0,20 mois de salaire par année, plafond de six mois, uniquement à initiative employeur. L’ancienneté s’apprécie à la fin effective, préavis inclus, et le calcul utilise toute l’ancienneté reconnue, pas seulement celle postérieure au premier anniversaire. Les droits antérieurs déjà protégés par le projet restent séparés. Le projet de politique dans ce dossier n’est pas la politique active.

## Conflits immédiats

1. **L1221-2** autorise encore le CDD. Le mot « normale » appliqué au CDI ne suffit pas à le rendre unique.
2. **L1221-19 à L1221-26 et L1231-1** : le projet conserve un essai de trois mois et une exclusion du titre rupture. Les prévenances restent de 24 h, 48 h, deux semaines et un mois. Deux semaines valent quatorze jours, pas quinze. Il faut une règle expresse pour la fin d’un préavis qui dépasserait l’essai.
3. **L1234-1, L1234-2, L1234-8, L1237-1** : les délais d’un ou deux mois, les accords et usages subsistent. Les délais locaux de **L1234-15 à L1234-17-1** s’appliquent aussi à la démission. Le doublement de **L5213-9** et les délais **L7112-2/L7313-9** sont hors noyau et nécessitent une décision/coordination explicite.
4. **L1234-9 et R1234-1/2/4** : le projet ouvre toujours le droit à huit mois. Il prévoit déjà une composante antérieure et une composante nouvelle, dont seule la seconde est plafonnée. Ne pas remplacer cela par un plafond global rétroactif. Le salaire de référence est celui de la rupture. Un salarié sous contrat nouveau atteignant un an pendant son préavis doit entrer dans le barème sur la totalité de l’ancienneté reconnue.
5. La franchise ordinaire ne supprime pas les salaires, congés acquis (**L3141-28**), indemnités de préavis, dommages pour illégalité ni créances spécifiques. La faute grave, actuellement exclue de L1234-9, demande une lecture explicite de la décision d’auteur : son exception indemnitaire n’a pas été expressément supprimée par la seule fixation du barème. Pour le préavis nouveau, une exception de faute grave ne doit pas subsister silencieusement.
6. **L1237-13** : quinze jours de rétractation ne valent pas quinze jours de préavis. Homologation et consentement libre ne disparaissent pas avec le contrat unique. L’indemnité spécifique ne doit pas reprendre mécaniquement une condition d’ouverture réservée au licenciement ; le choix de l’auteur porte expressément sur l’indemnité ordinaire.

## Le titre CDD entier : soixante-dix entrées relues

**59 articles législatifs et 11 réglementaires** : L1241-1 ; L1242-1 à L1242-17, y compris les suffixes ; L1243-1 à L1243-13-1 ; L1244-1 à L1244-4-1 ; L1245-1/2 ; L1246-1 ; L1247-1 ; L1248-1 à L1248-11 ; D1242-1/3/4/5/6/8 ; D1243-1 ; R1243-2 ; R1245-1 ; D1247-1/2. Les listes exactes sont dans le JSON, sans créer d’articles manquants dans les intervalles.

Les durées, motifs, renouvellements, carences, écrit, égalité de traitement, requalification, sanctions pénales, contrôle et actions syndicales doivent tous recevoir un sort. La suppression d’une autorisation nouvelle n’efface pas les droits et litiges des contrats antérieurs. **L1243-4** garantit des rémunérations jusqu’au terme en cas de rupture illicite ; **L1243-8/9** portent une prime de précarité de 10 %, ou 6 % sous conditions ; **L1243-11** conserve l’ancienneté et impute le contrat antérieur sur l’essai. La transition doit décider du sort des contrats en cours, sans réinitialiser ancienneté, congés et essai.

**L1241-1 exclut l’apprentissage et l’intérim du titre CDD**. L’abrogation de ces soixante-dix entrées ne supprime donc pas à elle seule les contrats à terme spéciaux.

## Coordinations nécessaires avant de présenter le régime comme universel

| Ensemble | Entrées cartographiées | Points qui empêchent une simple suppression de mots |
| --- | ---: | --- |
| Intérim, L/R/D1251* | 111 | Contrat de mission distinct, terme, essai de deux/trois/cinq jours, rupture anticipée, prime de mission. **L1251-58-1 à L1251-58-8** organisent déjà le CDI intérimaire : le lien avec l’employeur doit être distingué de la mission chez le client et des périodes sans mission. |
| Contrat d’apprentissage | 98 | **L6222-7** permet durée limitée ou CDI ; **L6222-18** prévoit 45 jours de pratique puis une rupture et une médiation propres ; **L6222-16** protège ancienneté et absence d’un nouvel essai ; la durée de formation peut demeurer déterminée dans un CDI. |
| Professionnalisation, L/R/D6325* | 62 | **L6325-5** permet CDD/CDI ; renouvellement de L6325-7, aides et durée d’action de formation à préserver séparément du terme d’emploi. |
| Portage, L/R/D1254* | 36 | **L1254-7** autorise CDD/CDI, **L1254-18** renvoie à une partie du titre CDD, **L1254-8** distingue fin commerciale et fin d’emploi, **L1254-19** organise déjà le CDI. |
| Insertion/aides, L/R/D5132* et 5134* | 346 candidats | **L5132-5, L5132-11-1, L5132-15-1, L5134-24 et L5134-69** contiennent des CDD propres. **L5132-6 exclut expressément la section CDI intérimaire** pour l’intérim d’insertion. Toutes les entrées de ces chapitres ne sont pas à supprimer : aides et accompagnement peuvent survivre au terme du contrat. |
| Reconversion, L/R/D6324* | 16 | **L6324-3**, en vigueur dans le corpus 2026, prévoit un CDD d’au moins six mois et un essai ; régime des actions antérieures dans les notes. |
| Licenciement économique | 172 | Cause, reclassement, procédures collectives, CSP, PSE et calendrier administratif restent distincts du préavis individuel. |

Autres points : **L1223-5/6/7** (export, indemnité sans condition d’ancienneté), **L1223-8/9 et L1236-8/9** (chantier déjà CDI), **L3123-33 à L3123-37** (intermittent déjà CDI), journalistes, VRP, particuliers employeurs, artistes/mannequins. Les **186 candidats de contrats spéciaux** ne sont pas tous des contrats à terme à supprimer.

Effets transversaux immédiats : **L1111-2**, exclusion des remplaçants CDD du décompte d’effectifs ; **L2253-1**, compétences de branche sur CDD/intérim/essai ; **L4154-1 à L4154-3**, protection renforcée des entrants affectés à un risque ; **L5422-1**, privation involontaire et double refus de CDI. Les indemnités d’inaptitude, maternité, accident du travail, mandats, grossesse et départ pour élever l’enfant ne se déduisent pas du seul barème général.

## Contraintes primaires vérifiées

La convention OIT n°158 distingue motif valable, possibilité de défense, recours, préavis raisonnable et protection du revenu. Elle ne transforme pas une rupture notifiée en quinze jours en rupture automatiquement licite. La France figure parmi ses ratifications en vigueur. Les garanties de licenciement collectif ont leur propre calendrier européen : quinze jours de préavis individuel ne suppriment pas notification et consultation. La directive 2019/1152 conserve l’information écrite et encadre l’essai.

- [OIT, convention n°158](https://normlex.ilo.org/dyn/nrmlx_fr/f?p=NORMLEXPUB%3A12100%3A0%3A%3ANO%3A%3AP12100_INSTRUMENT_ID%3A312303), articles 2, 4, 7 à 12.
- [OIT, ratifications de C158](https://normlex.ilo.org/dyn/nrmlx_fr/f?p=NORMLEXPUB%3A11300%3A0%3A%3ANO%3A%3AP11300_INSTRUMENT_ID%3A312303).
- [Directive 2019/1152](https://eur-lex.europa.eu/eli/dir/2019/1152/oj?locale=fr), articles 4 et 8.
- [Directive 98/59, consolidation 2015](https://eur-lex.europa.eu/eli/dir/1998/59/2015-10-09/fra/pdf), articles 2 à 4.

Des contrats à terme existent aussi hors des cinq codes importés : sport professionnel, contrats publics, recherche et contrats agricoles spéciaux. L1242-3 renvoie notamment aux articles L412-3 et L431-5 du Code de la recherche ; D1242-1 inclut le sport professionnel. Ces pistes ne sont ni récupérées intégralement ni déclarées réécrites ici. Aucun contrôle de conventionalité, d’authenticité actuelle ou d’exhaustivité hors corpus n’est revendiqué.

## Première édition opératoire

Préparer d’abord les quarante-cinq textes du noyau et le lot CDD séparé, avec la même date d’entrée en vigueur et la même transition. L’ensemble peut constituer le noyau opératoire du droit commun après contrôle. Il ne doit pas être annoncé comme un contrat réellement universel tant que les portes d’entrée spéciales ci-dessus, les délais protégés et les règles d’inaptitude n’ont pas été coordonnées. Aucune rédaction dans ce dossier ne vaut acceptation en base, modification de la politique active ou publication.


## Paquet de rédaction proposé

`answer.json` contient les 45 articles complets et passe `run_exhaustive.validate_answer`. `source.json` est une liste directement compatible avec `register_pack.py` : 43 propositions antérieures avec `previous_draft.proposed_sha256`, deux premières rédactions (R1221-34 et R1234-5). Toutes les sources et tous les guards correspondaient à la base lors du contrôle final en lecture seule. Chaque réponse possède une analyse spécifique `benefit_review` de plus de 100 caractères. Les 14 réductions de régime portent les métadonnées `normative_reduction` et `editorial_direction_2026_10_19`. Aucun enregistrement n’a été exécuté.

Le barème ordinaire figure à **L1234-9**, puis dans **R1234-1, R1234-2 et R1234-4** pour le calcul : c’est le renvoi à utiliser pour les coordinations CMG, sans importer une condition d’ouverture à une indemnité spéciale distincte. Les points éditoriaux encore à arbitrer sont exposés dans `policy.proposed.json`, notamment faute grave pour la seule indemnité, force majeure externe et minima spécifiques avant un an.
