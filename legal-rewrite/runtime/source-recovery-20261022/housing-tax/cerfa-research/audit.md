# CERFA 30-0812 et 30-0813 : complément documentaire

Passe achevée le 22 octobre 2026 UTC. **Les deux modèles graphiques restent non récupérés.** La cartographie textuelle a progressé : sept XML originaux, dont six historiques, sont conservés et vérifiés ; deux archives parlementaires officielles ont été téléchargées, extraites, rendues et lues sur les pages pertinentes. Aucune nouvelle notice n’est prête à être activée.

Cette passe écrit uniquement dans `cerfa-research/`. Elle ne modifie aucune source, aucun article, aucune notice activée ni aucun processus de rédaction.

## Preuves canoniques et limites de dates

La lecture a porté sur la copie isolée `runtime/global-reference-audit-20261022/corpus.snapshot.sqlite`, ouverte en lecture seule avec `query_only`. Une requête ciblée sur `(code_id=LEGITEXT000006069576, number=15)` puis sept lectures de documents par `(code_id,id,kind=ARTICLE)` ont fourni les pièces. Les octets XML sauvegardés correspondent tous à `articles.source_sha256` et `documents.sha256`. L’archive d’origine est `Freemium_legi_global_20250713-140000.tar.gz`. Voir `source-guards.json`, les sept fichiers de `preuves/`, `version-history.json` et `version-diffs.json`.

| XML | Bornes telles que conservées | Observation sur les modèles et le contenu |
|---|---|---|
| LEGIARTI000006301207 | 1979-07-01 / 1977-12-31, MODIFIE_MORT_NE | Renvoi aux modèles sans numéros. Bornes inversées : aucune période de validité n’est déduite de cette entrée. |
| LEGIARTI000006301208 | 1982-12-30 / 1985-02-15 | Renvoi sans numéros ; coupons crédités en compte encore décrits au 3° ; abattements de 5 000 F et 3 000 F. |
| LEGIARTI000006301209 | 1985-02-15 / 1994-09-02 | 3° devenu sans objet ; 4° limité aux relevés du 2°. |
| LEGIARTI000006301210 | 1994-09-02 / 2002-01-01 | Abattement exprimé par renvoi à l’article 158 ; aucun numéro CERFA. Appel de note (1) dans le corps, NOTA XML vide. |
| LEGIARTI000006301211 | 2002-03-31 / 2004-12-31 | Première mention explicite des deux numéros dans les XML conservés, avec indication de non-reproduction ; monnaie en euros ; NOTA relative aux revenus de 1996 et suivants. |
| LEGIARTI000006301212 | 2005-01-01 / 2008-09-18 | Deux numéros conservés ; seul crédit d’impôt au 4°d ; suppression du rappel de note. |
| LEGIARTI000019493914 | 2008-09-18 / 2999-01-01 | Deux numéros conservés ; suppression au 4°a des mots relatifs aux seuls frais d’encaissement ; NOTA vide. |

La première mention des numéros en 2002 ne prouve pas leur création cette année-là. Les bornes conservées ne couvrent pas l’intervalle du 1er janvier au 31 mars 2002. Aucun contenu ou intervalle absent n’a été reconstitué. L’absence de numéro dans un XML ancien ne prouve pas que l’imprimé n’était pas déjà numéroté.

## Publications officielles récupérées

1. [Assemblée nationale, 2e séance du 10 mai 1960](https://archives.assemblee-nationale.fr/1/cri/1959-1960-ordinaire2/012.pdf), question 3805, page imprimée 755, page PDF 13 : la réponse renvoie à l’arrêté du 28 janvier 1960, publié au JO du 10 février 1960, page 1357. Elle confirme que la contexture des relevés a été aménagée pour les revenus de 1960.
2. [Assemblée nationale, questions du 3 septembre 1960](https://archives.assemblee-nationale.fr/1/qst/1-qst-1960-09-03.pdf), question 5817, page imprimée 2348, page PDF 30 : la réponse décrit les quatre catégories prévues pour 1960 : dividendes et revenus assimilés ; intérêts et produits d’obligations ; distributions des sociétés d’investissement et assimilées ; revenus exonérés.

Les deux téléchargements ordinaires donnent HTTP 200 et `application/pdf`, avec validation TLS normale, sans cookies ni authentification. Le premier client Python avait échoué sur sa chaîne locale de certificats ; le client système a ensuite réussi sans désactiver les vérifications. Les fichiers complets, les extractions intégrales, les pages pertinentes rendues et leurs empreintes sont recensés dans `official-pdf-evidence.json`. Les deux pages ont été inspectées visuellement ; l’OCR ancien est imparfait et l’image d’origine commande la lecture.

Ces réponses prouvent le renvoi et le contexte de 1960. **Elles ne montrent aucun imprimé, aucun numéro CERFA ni indice de révision.** Elles ne sont pas les annexes graphiques de l’arrêté.

## Modifications normatives vérifiées

Le texte officiel de l’[arrêté du 17 octobre 1994](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000165661), NOR BUDF9400019A, réécrit le 4°a et renvoie à la loi 87-416 du 17 juin 1987, article 28 I. Le lien ancien du XML la qualifie à tort de décret. Le 1° relatif aux modèles n’est pas modifié par cette disposition.

L’[arrêté du 3 septembre 2001](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000591461/2025-03-22), NOR ECOZ0100005A, article 2 II a, remplace la contre-valeur en francs par la contre-valeur en euros ; son article 8 fixe l’entrée en vigueur au 1er janvier 2002. Il ne crée ni ne renumérote les formulaires. Cette portée a été lue dans le texte officiel, indépendamment de la date d’édition de l’article consolidé.

L’arrêté du 30 décembre 2004, NOR BUDF0400065A, article 1 II, supprime la référence à l’avoir fiscal au 4°d. Son identité et sa publication, JO du 31 décembre 2004, texte 106, sont confirmées par le [sommaire officiel](https://www.legifrance.gouv.fr/jorf/jo/2004/12/31/0304). Le texte exact de sa republication figure dans les résultats publics du [BOI 5 I-2-05 du 11 août 2005, annexe 4](https://bofip-archives.impots.gouv.fr/bofip/25904-AIDA.html/identifiant%3D-20050811). **La portée est établie par le XML et ce texte ministériel indexé ; aucun PDF local de cette republication n’a été obtenu.** Le lien JORF a produit une erreur de cache du lecteur web ; le téléchargement public du PDF Minefi a rendu HTTP 503 et 107 octets HTML, conservés comme réponse d’erreur. Ce résultat n’est pas décrit comme une interdiction d’accès.

L’[arrêté du 15 septembre 2008](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000019491882), NOR BCFL0818512A, article 1 a, supprime au 4°a les mots relatifs à la déduction des seuls frais d’encaissement. Il ne change pas le 1° ni ne fournit les modèles.

Pour 1985, la disparition des dispositions sur les coupons crédités en compte est constatée directement par comparaison des XML. La référence au décret **85-201 du 13 février 1985**, article 4, vient du XML original ; le texte de cet acte n’a pas été récupéré dans cette passe. Une date du 19 février issue d’une piste secondaire n’est pas retenue comme preuve.

La [doctrine officielle 4 J 1342 de 1995](https://bofip-archives.impots.gouv.fr/bofip/27494-AIDA.html/identifiant=4J1342-19951101) renvoie les modèles à l’annexe de l’article 15 et signale l’évolution vers la déclaration annuelle unique depuis 1987. Elle ne contient pas leurs images et ne justifie pas de remplacer les deux anciens CERFA par un imprimé IFU moderne.

## Pièces encore manquantes

Pour **chacun** des CERFA 30-0812 et 30-0813, il manque l’imprimé officiel complet identifiable par son numéro et son titre, ses éventuelles faces ou pages supplémentaires, sa notice et ses annexes, son indice ou sa date de révision, et une preuve de correspondance avec la version de l’article applicable depuis 2008.

Le fac-similé de l’arrêté du 28 janvier 1960 et de ses éventuelles pages annexées reste à obtenir, à partir du JO du 10 février 1960, page 1357. Même récupéré, un modèle de 1960 devra être rapproché des changements ultérieurs et des numéros CERFA avant certification. La correspondance supposée entre les deux numéros et les fonctions guichet/correspondance ou crédit en compte **n’est pas établie**. La limite de 21 × 13 cm du texte concerne les fiches mécanographiques admises en remplacement ; elle ne prouve pas les dimensions des modèles CERFA.

Les actes de 1938, 1961, 1964, 1965 et 1977 repérés par une source secondaire restent des pistes, sans concordance graphique démontrée ici. Les recherches officielles supplémentaires n’ont livré aucune image complète identifiable. Un résultat vide ne prouve pas l’indisponibilité publique d’une archive. Les quatre scans protégés suivis séparément par le coordinateur restent sous réserve de son autorisation en cours ; cette passe n’a ouvert aucun scan protégé ni tenté de défi d’accès.

`documentary_recovery_complete=false`, `ready_for_companion_activation=false`. Les deux modèles restent en réserve ; aucun texte de remplacement, formulaire contemporain ou représentation reconstituée n’a été proposé comme récupération.
