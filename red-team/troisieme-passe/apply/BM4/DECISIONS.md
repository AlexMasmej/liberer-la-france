# BM4 — corrections des défauts grossiers de l'échantillon apparié frais (paquet `audit/baseline/fix-packet-BM4.json`)

Lecture : production, en lecture seule (`CITE_PRODUCTION=1 tools/cite.py`, sqlite `mode=ro`, `query_only`), le 31 octobre 2026. Sources primaires : EUR-Lex, règlement (UE) 2016/425 (CELEX 32016R0425), consulté le 31 octobre 2026 ; la page de la directive (UE) 2020/262 est restée vide. Revue IA, sans validation par un juriste.

Décompte : 5 corrigés (dont 1 partiel), 1 déjà réglé, 1 non corrigé (correction d'ensemble déposée sous `requests`).

Dossiers : `apply/BM4` (2 changements, 2 requests, 2 skipped), `apply/T108cd`, `apply/Z01cd`, `apply/W09cd` (1 changement chacun). Tous validés, `problems` vide.

## Corrections appliquées

1. **Annexe III 111 H quindecies** (LEGIARTI000047114063, groupe T108) → `apply/T108cd`, défaut hérité.
   - Déjà corrigés en production : le renvoi au « III de l'article 302 M » (disparu en 2017) et la phrase finale tronquée.
   - Restait, au II (réception), le deuxième alinéa recopié du I : « Il en est de même lorsque l'expéditeur ne peut se connecter au service… Dans ce cas, il informe également… ». Le premier alinéa du II traite déjà le cas où le service « était indisponible au moment de l'expédition ». L'alinéa est donc rattaché au cas de l'expédition sous document papier du I (« lorsque, dans le cas prévu au I, l'expéditeur n'a pu se connecter au service au moment de l'expédition en raison d'une indisponibilité de son propre système informatique ») ; sa seconde phrase, qui faisait peser sur un « il » sans antécédent une information des motifs déjà exigée de l'expéditeur par le I, est retirée.
   - Aucune formalité nouvelle. Les mouvements en cours gardent leurs documents.
   - Pour l'auteur : la source ne prévoit aucun secours pour le destinataire dont le propre système est indisponible. L'ajouter serait un choix nouveau, non une coordination ; la directive 2020/262 n'a pu être relue.
2. **CSS D712-31** (LEGIARTI000006738841, sans propriétaire) → `apply/BM4`, défaut hérité.
   - La base légale des sections locales, L. 712-6, est abrogée depuis le 1er janvier 2016 (loi n° 2015-1702, art. 59). La délégation de gestion aux mutuelles de fonctionnaires relève depuis du deuxième alinéa de L. 160-17 et de la convention avec la CNAM de R. 160-26, avec reprise par la caisse nationale à défaut de convention (R. 160-26 IV, R. 160-28).
   - Correction : le premier alinéa rattache la création des sections locales à l'exécution des opérations de gestion déléguées en application de L. 160-17 et de la convention de R. 160-26 ; un dernier alinéa constate l'abrogation de L. 712-6, sans délégation distincte ni formalité ajoutée. La suppression du minimum d'adhérents (réforme du projet), le périmètre départemental et la transition sont inchangés.
   - `requests` : **D712-30** (LEGIARTI000006738840, maintenu, sans propriétaire), « doivent confier » rattaché à L. 160-17 et à la convention de R. 160-26, avec renvoi à R. 160-26 et R. 160-28 à défaut de convention. Texte complet, motif, notes et bilan d'impact joints, validés dans un dossier temporaire supprimé. La délégation reste obligatoire : aucun choix nouveau.
   - Pour l'auteur : R160-26 I vise encore L. 712-1 et L. 712-2, abrogés le 1er septembre 2023 (hors paquet).
3. **CSS R731-18** (LEGIARTI000006753042, groupe Z01) → `apply/Z01cd`, défaut vu par les deux audits.
   - L'article maintenu désignait l'autorité « mentionnée au premier alinéa de l'article L. 731-1 » : cet alinéa ne vise plus aucune autorité depuis le 2 janvier 1990 et L. 731-1 est abrogé depuis le 10 août 1994 (loi n° 94-678, art. 16).
   - Correction, alignée sur R731-1, R731-3, R731-3-1 et R731-8 en production : renvoi rattaché à la rédaction antérieure au 2 janvier 1990 ; désignation limitée aux institutions autorisées avant 1994 ; aucune autorisation nouvelle ; aucune formalité de remplacement ; droits des adhérents conservés.
   - Les notes qui disaient L731-1 « absent du corpus local » sont rectifiées (deux versions au corpus).
4. **Travail L6523-2-1** (LEGIARTI000035902685, groupe W09) → `apply/W09cd`, défaut vu par les deux audits.
   - Le a écarte à Mayotte le deuxième alinéa de L. 6331-54, abrogé au 1er janvier 2018 (loi n° 2016-1088, art. 41), date même d'entrée en vigueur de l'article. La proposition le présentait comme applicable « à toute situation relevant de cette disposition ».
   - Correction : renvoi rattaché à la rédaction abrogée et aux contributions des périodes antérieures au 1er janvier 2018, sans remise en vigueur ; le b est inchangé ; aucune contribution nouvelle ni supprimée. Le champ résiduel est vraisemblablement vide et les notes le disent.
   - Pour l'auteur : une adaptation mahoraise de la contribution des micro-entrepreneurs artisans (quatrième alinéa de L. 6331-48) serait un choix nouveau, non une coordination ; aucune cible successeur n'est inventée.
5. **Urbanisme R520-3** (LEGIARTI000035710656, sans propriétaire) → `apply/BM4`, défaut hérité, correction **partielle**.
   - La première phrase déclarait l'article « abrogé » à la date de suppression de la taxe, alors que ses alinéas suivants datent les faits anciens et préservent les droits acquis. Comme pour L520-4 (corrigé en troisième passe), l'article devient la disposition transitoire du fait générateur réglementaire ; ses règles de datation sont rattachées au II de L520-4, qui renvoie déjà aux règles relatives aux constructions sans autorisation. Ligne requalifiée de `full_repeal` en `normative_reduction`, le reste du texte inchangé.
   - Non appliqué (`skipped`, arbitrage) : la divergence héritée loi/décret sur le fait générateur des constructions irrégulières (loi : à défaut d'autorisation, début des travaux ou changement d'usage ; décret : procès-verbal d'achèvement). Elle ne sert plus qu'à classer le stock ancien, mais retenir l'une ou l'autre date étend ou restreint l'imposition. L520-4 (groupe B09) n'est pas touché.

## Déjà réglé

6. **CCH R315-73** (LEGIARTI000006897042, groupe W11).
   - La proposition de R315-69 en production (SWEEP-M03) rattache toutes les références de la sous-section aux articles L. 315-19 à L. 315-32 (dont le 1° de R315-73 à L. 315-21 et le 4° de R315-72 à L. 315-25) à leur rédaction antérieure à l'abrogation par l'article 180 de la loi n° 2011-525 du 17 mai 2011, pour les seuls comptes ouverts jusqu'au 4 février 1959 non encore clos.
   - L'abrogation date de 2011, non de 1983 (borne de modification de l'intitulé) comme l'écrit l'audit officiel.
   - Résidu m, non corrigé faute de modifier l'article : les notes de R315-73, R315-72 et R315-75 disent encore L315-21 et L315-25 « absents du corpus ».

## Non corrigé, correction d'ensemble sous `requests`

7. **Travail R4313-69** (LEGIARTI000019761050, sans propriétaire).
   - Défaut de régime : R4313-57 à R4313-74 (sous-section 4, procédures d'évaluation de la conformité des EPI) transposent la directive 89/686/CEE. EUR-Lex (31 octobre 2026) : règlement (UE) 2016/425, art. 46, directive abrogée au 21 avril 2018 ; art. 47, produits conformes à la directive mis sur le marché jusqu'au 21 avril 2019, attestations et approbations valables au plus tard jusqu'au 21 avril 2023 ; art. 48, application au 21 avril 2018. Le code vise lui-même ce règlement (L4311-6, R4746-3).
   - Une clause dans le seul R4313-69 serait incohérente avec les douze autres articles du paragraphe. `skipped` (hors corpus / section entière).
   - `requests` : **R4313-82** (LEGIARTI000019760989, maintenu, sans propriétaire), article déclencheur des deux paragraphes de la sous-section 4 : dernier alinéa limitant les procédures des articles R. 4313-57 à R. 4313-74 aux EPI mis sur le marché avant le 21 avril 2019 sous la directive et à la validité résiduelle des approbations (21 avril 2023 au plus tard), et renvoyant les EPI mis sur le marché depuis le 21 avril 2018 aux procédures du règlement, sans procédure nationale supplémentaire. Texte complet, motif, notes et bilan d'impact joints, validés dans un dossier temporaire supprimé.
   - Pour l'auteur : R4313-80 (autocertification CE des EPI) et R4313-81 (examen CE de type des EPI) appellent la même limitation ; l'existence d'approbations nationales encore invoquées n'est pas vérifiée.

## Réserve de méthode

Ces sept articles viennent de l'échantillon apparié frais qui mesure le taux de défauts grossiers. Les corriger ne mesure pas une baisse du taux du corpus ; seule une nouvelle mesure sur un échantillon tiré hors de ces articles peut l'établir.

Revue IA : rien de ceci ne vaut validation par un juriste.
