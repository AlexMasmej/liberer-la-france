# R7 — demandes des groupes BM3 et BM4 pour des articles hors de leur paquet : décisions

Paquet : `audit/baseline/requests-R7.json` (7 demandes). Lecture en production, en lecture seule (`CITE_PRODUCTION=1 tools/cite.py`, sqlite `mode=ro`, `query_only`), le 31 octobre 2026. Aucun des sept articles n'avait de changement en attente dans les dossiers de `audit/baseline/fix-folders-2.json` : aucune fusion. Contrôle : `python3 -B apply/check_changes.py` sur `R7`, `Z04cf` et `B04cf` → `problems: []`. Revue IA, sans validation par un juriste.

## Décompte

- **Appliquées : 7** (5 dans `apply/R7`, 1 dans `apply/Z04cf`, 1 dans `apply/B04cf`).
- **Fusionnées : 0. Non appliquées : 0.**
- Trois demandes ont été appliquées avec une modification minimale de R7 (R441-28, L351-8/L351-14/L351-5-1 : clause de renvoi, R4313-82), expliquée ci-dessous et dans les notes.

## Dossier `apply/R7` (articles sans propriétaire)

### CCH R441-28 (LEGIARTI000026617887, demande BM3, BASELINE-BM3-L441-11)
- Défaut vérifié : la proposition en production faisait encore notifier et prononcer la sanction résiduelle par le préfet, avec recouvrement au profit de l'Etat (décret n° 2012-1246), alors que L441-11 ne fixe plus que le montant depuis 2015 (LEGIARTI000028808505) et que L342-14 I 1° b, L342-12 et L342-16 régissent la sanction (ministre sur proposition de l'ANCOLS, contradictoire, recouvrement au profit de la CGLLS). L342-14 proposé borne déjà le b aux manquements antérieurs.
- Correction : renvoi aux articles L. 342-12 à L. 342-16 pour le seul stock ancien, comme demandé. **Modification R7 :** le délai d'un mois pour présenter ses observations, garantie de la source, est conservé comme plancher (option laissée ouverte par BM3) ; il ne change ni l'autorité ni le recouvrement et n'est pas une formalité à la charge de l'organisme. Motifs, notes et bilan d'impact rectifiés : le décret n° 2012-1246 n'est plus visé.
- R472-1 et R481-4 (renvois à la sous-section SLS) lus : déjà bornés aux périodes anciennes, non touchés.

### Travail L351-8 (LEGIARTI000018124711, demande BM3, BASELINE-BM3-L351-6)
- Défaut vérifié : article de la partie législative ancienne (NOTA de L351-13 : ordonnance n° 2007-329, art. 12), maintenu sans proposition ; son exception « L. 351-5 à L. 351-6 » meurt avec l'abrogation de L351-6 en attente dans `apply/BM3` ; objet régi par L5422-20 à L5422-22, maintenus.
- Correction : abrogation (`full_repeal`), accords et décrets antérieurs conservés. **Ajout R7 :** clause de renvoi vers L. 5422-20 à L. 5422-22 pour les dispositions qui visent encore « l'accord prévu à l'article L. 351-8 » (L321-4-2, abrogé pour l'avenir mais conservant les situations anciennes ; L351-14), limitée aux champs où elles demeurent applicables.

### Travail L351-14 (LEGIARTI000018125034, demande BM3, BASELINE-BM3-L351-6)
- Défaut vérifié : la proposition en production traitait cet article ancien comme du droit vivant et y portait une transition du contrat unique déjà portée par L5424-20 proposé ; les aménagements relèvent de L5422-6, la suppression de la contribution spécifique de L5424-20, L5424-22 et L5422-16.
- Correction : abrogation, sans perte de faveur ni contribution de remplacement. **Ajout R7 :** clause de renvoi vers L. 5422-6 et L. 5424-20 pour L351-5-1, qui vise encore « les contributions prévues aux articles L. 321-4-2, L. 351-3-1 et L. 351-14 ».

### CSS D712-30 (LEGIARTI000006738840, demande BM4, BM4-D712-30)
- Défaut vérifié : article maintenu ; sa base légale L712-6 est à l'état ABROGE depuis le 1er janvier 2016 (loi n° 2015-1702, art. 59) ; la délégation relève de L160-17 (deuxième et troisième alinéas) et de la convention de R160-26, avec reprise à défaut de convention (R160-26 IV, R160-28).
- Correction : texte de BM4 appliqué tel quel ; cohérent avec D712-31 en attente dans `apply/BM4`. Aucune formalité nouvelle, délégation obligatoire conservée.
- Pour l'auteur : R160-26 I vise encore L. 712-1 et L. 712-2 abrogés (signalé par BM4, hors paquet).

### Travail R4313-82 (LEGIARTI000019760989, demande BM4, BM4-R4313-82)
- Défaut vérifié : article maintenu ; les procédures nationales R. 4313-57 à R. 4313-74 transposent la directive 89/686/CEE, abrogée par le règlement (UE) 2016/425 que le code vise lui-même (L4311-6, R4746-3).
- Correction : dernier alinéa de BM4 limitant ces procédures au champ transitoire de la directive. **Modification R7 :** « mis sur le marché à compter du 21 avril 2018 » remplacé par « Les autres équipements de protection individuelle », pour éviter le chevauchement avec les produits conformes à la directive encore mis sur le marché jusqu'au 21 avril 2019 (art. 47 § 1 du règlement) ; motif et bilan d'impact ajustés. R4312-8 6° renvoie à la liste des sept catégories, inchangée.
- Réserve documentaire : R7 n'a pu relire le règlement sur EUR-Lex le 31 octobre 2026 (page tronquée) ; les dates sont celles rapportées par BM4.
- Pour l'auteur : R4313-80 et R4313-81 appellent la même limitation (signalé par BM4).

## Dossiers de variante

### `apply/Z04cf` — Travail L351-5-1 (LEGIARTI000038314413, propriétaire Z04, demande BM3)
- Défaut vérifié : article ancien dont l'objet entier est repris par L5422-16 (LEGIARTI000048600606) ; la proposition en production ne bornait que le renvoi à L321-4-2.
- Correction : abrogation, situations antérieures conservées. **Ajout R7 :** clause de renvoi vers L. 5422-16 pour L143-11-4 et L143-11-6 (articles anciens maintenus qui visent encore L. 351-5-1 pour les cotisations de garantie salariale), afin de ne pas laisser un renvoi mort. Le groupe Z04 est invité à confirmer.

### `apply/B04cf` — CGI 1406 bis (LEGIARTI000053536221, propriétaire B04, demande BM3)
- Défaut vérifié : « ne remet pas en vigueur les dispositions antérieures de l'article 232 » contredit le X ajouté à 232 dans `apply/B04cc`, qui maintient les I, V et VI de 232 ; 1407 ter et le code de l'urbanisme s'appuient sur ce zonage.
- Correction : phrase remplacée comme demandé ; reste de la proposition, motif et quotes du bilan d'impact inchangés ; notes complétées. Coordination neutre, aucune imposition rétablie. Dépend de l'application de `apply/B04cc`.

## Points laissés à l'auteur

1. Partie législative ancienne du code du travail : au-delà de L351-6, L351-8, L351-14 et L351-5-1, L143-11-4 et L143-11-6 (garantie salariale) restent des articles anciens maintenus ; la clause de renvoi de L351-5-1 évite seulement un renvoi mort.
2. R4313-80, R4313-81 et la section « examen CE de type » : même limitation au champ transitoire à décider d'ensemble.
3. R441-28 : le plancher d'un mois peut être retiré si l'auteur préfère s'en tenir au contradictoire de L. 342-12 sans délai.
