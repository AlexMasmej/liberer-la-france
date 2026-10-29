# W03 : décisions du balayage (troisième passe)

Texte lu : la production, en lecture seule (`CITE_PRODUCTION=1 tools/cite.py`, sqlite `mode=ro`). Les preuves sont sous `evidence/cited/production-20261029/`. Deux consultations de Légifrance ont eu lieu le 2026-10-29 (consolidation courante) : la sous-section L932-40 à L932-48-1 du CSS, et l'ordonnance n° 2026-648 (JORFTEXT000054456926), dont l'article 1er, 4°, fait de L. 752-3-1 l'article L. 760-15.

## Bilan

- 54 articles et 65 pistes : 34 faux positifs, 15 déjà réglés, 7 défauts mineurs (m) et 9 défauts grossiers (G).
- 8 corrections, toutes en mode `replace` : L941-3, R931-9-1, L612-1, R653-9, R653-10, R165-46, R165-47 et R165-48. Le contrôle `check_changes.py W03` donne `problems: []`, avec 8 lignes validées.
- 3 points ne sont pas corrigés (`skipped`) : 2 pour pièce manquante, 1 pour arbitrage.

## Corrections

| Article | Piste | Qualification | Correction |
|---|---|---|---|
| L941-3 (LEGIARTI000034387804) | S8 L931-17, L931-20 | G F3 | Les renvois à L931-17 et L931-20 sont retirés : ces deux articles sont abrogés depuis le 1er janvier 2016. Les notes, qui les disaient à tort absents du corpus, sont corrigées. Il n'y a pas de redirection vers L931-18-3, qui reprend l'ancien L931-20 (voir les points pour l'auteur). |
| R931-9-1 (LEGIARTI000036332492) | S8 R931-5-1-7 | G F3 (texte pénal) | Le renvoi pénal au « dernier alinéa de l'article R. 931-5-1-7 » est retiré du 2°. Cet article a été abrogé en 2010 par le décret n° 2010-217, et son dernier alinéa ne contenait aucune obligation. Aucune incrimination n'est ajoutée. |
| L612-1 (LEGIARTI000036391010) | S8 L723-1 | G F3 | « L. 723-1 » devient « L. 652-1 ». L723-1 a été transféré en 2018 par l'ordonnance n° 2018-470, et la concordance LEGI désigne L652-1 (CNBF) comme successeur. Le fond ne change pas. |
| R653-9 (LEGIARTI000038770306, maintenu puis réécrit) | S8 L653-7 | G F3/F5 | L653-7 a été abrogé le 31 décembre 2025 par l'article 102 de la loi n° 2025-1403. L'exception vise désormais L653-7 « dans sa rédaction applicable à leur situation ». La suspension à la réinscription ne s'applique plus aux assurés relevant du nouveau L161-22, que la loi autorise à cumuler. Les périodes anciennes sont conservées. La rédaction suit celle de D643-10-2. |
| R653-10 (LEGIARTI000038770309) | S8 L653-7 | G F3 | Les renvois à L653-7 sont bornés à l'ancien régime. Pour le nouveau régime de L161-22, l'attestation propre à L653-7 et l'ouverture trimestrielle ne s'appliquent plus. La déclaration de reprise est conservée et aucune pièce nouvelle n'est exigée. |
| R165-46 (LEGIARTI000037148907, maintenu puis réécrit) | S8 L165-1-2 | G F3 | L165-1-2 a été abrogé le 25 décembre 2022 par l'article 58 de la loi n° 2022-1616. Le renvoi mort est remplacé par l'objet du contrôle : les spécifications de l'inscription sur la liste de L. 165-1. Les trois voies de déclenchement sont conservées. |
| R165-47 (LEGIARTI000037148897, maintenu puis réécrit) | S8 L165-1-2 | G F1 | La compensation financière, privée de base légale depuis 2022, ne peut plus être exigée pour les saisies futures. Les saisies antérieures restent régies par les règles qui leur étaient applicables. Les renvois du III sont corrigés : le recours à un organisme compétent ne vise plus l'article abrogé, et les destinataires du courrier sont énumérés expressément (ceux de l'ancien II, plus la HAS). La procédure contradictoire est conservée, puisque R165-5 I 2° l'utilise. |
| R165-48 (LEGIARTI000037148888, maintenu puis abrogé) | S8 L165-1-2 | G F2 | La procédure de pénalité du CEPS et la déclaration du chiffre d'affaires sont abrogées : elles reposaient sur l'ancien II de L165-1-2. Les pénalités définitives sont conservées et les procédures en cours bénéficient de la règle des sanctions plus douces. La pénalité de L165-5-1-1 IV (CNAM) n'est pas touchée. Aucune pénalité de remplacement n'est créée. |

Toutes ces lignes ont la classification `coordination_only`. Elles alignent le texte sur le droit officiel ou retirent des renvois morts, et ne revendiquent aucune coupe propre du projet. R165-47 porte `normative_reduction` et R165-48 `full_repeal`.

## Défauts mineurs non corrigés

- **R160-26** (L712-1 et L712-2, abrogés le 1er septembre 2023 par la loi n° 2023-270) : le renvoi est seulement descriptif et la population reste identifiable. Le retirer pourrait exclure les retraités. C'est à l'auteur de décider, et D160-14, hors paquet, a le même défaut.
- **R931-11-1 et A932-6** (L932-43, plus en vigueur depuis le 1er janvier 2023) : aucun successeur n'est identifié dans le corpus. Les notes disent à tort « L932-43 absent du corpus ».
- **D752-6, R752-21 et R752-20-1** (L752-3-1, transféré le 23 juillet 2026 et devenu L. 760-15) : **L760-15 manque au corpus**. C'est une anomalie d'inventaire : l'ordonnance n° 2026-648 relative à Saint-Pierre-et-Miquelon a probablement créé d'autres articles L760-x absents eux aussi. Il faudra rediriger les renvois après inscription. Les notes disent à tort « L752-3-1 absent du corpus ».

## Une ligne par piste

Faux positifs, car le renvoi vise un autre code :
- **code des assurances** : L942-7 (L143-1 et L143-2), L932-24-4, L932-24-1, L932-40, L932-41, L942-1, R932-4-2-4 (L144-x), R942-5 (L143-2), R932-4-4 (R332-3), R931-11-9 (R332-5), R931-11-1 (L143-1 et L143-4) ;
- **code rural** : R133-1 (L723-3), L114-23 (L723-12), L134-4 et L131-6-1-1 (L722-8), D160-15 et R413-21 (L723-2), R413-19 (L723-11) ;
- **CPCE** : R133-9-8 (L211-3) ;
- **CASF** : D523-2 et D582-1 (L262-2) ;
- **CPI** : R382-17 (L131-4) ;
- **code de la mutualité** : R861-21 (L211-5).

Faux positifs, car l'alinéa visé est toujours le bon : D861-4-1 (×2, dernier alinéa de L861-3), D131-7 (dernier alinéa de L131-8), R861-21 (dernier alinéa de L861-5), R613-13 et R613-11 (premier alinéa du I de L613-7), R172-12-1 (second alinéa de L172-2), R652-31 (deuxième alinéa de L652-6, applicable aux seules années anciennes), R652-36 (piste S2 : la « majoration de cotisation » n'est pas une sanction).

Déjà réglés, car la proposition borne déjà le texte ou le neutralise : D643-10-2 (L643-6), R114-10-2, R380-3 et R380-4 (L380-2), R381-80 et R381-83 (L174-4), D169-6 (dernier alinéa du II de D169-5), R155-4 (L133-4-10), R711-16 (×2, R244-4 et R244-5), R216-2 (abrogé avec L216-3), D861-4-1 (R133-7, qui se neutralise lui-même), R862-13-1 (L862-4-1), R652-31 et R652-36 (L652-6, piste S1).

Le détail de chaque piste, avec ses citations, se trouve dans `audit/sweeps/W03.json`.

## Points pour l'auteur

1. **L941-3** : les institutions de gestion de retraite supplémentaire sont-elles soumises à la dévolution de l'excédent prévue à L931-18-3, qui reprend l'ancien L931-20 ? Y renvoyer ajouterait une contrainte ; ce n'est donc pas fait.
2. **R165-46 et R165-47** : l'autre voie serait d'abroger le contrôle de l'ANSM et de coordonner R165-5 I 2°, car le législateur de 2022 a confié ce contrôle à la CNAM (L165-5-1-1). Cette voie supprime une procédure contradictoire et relève d'un arbitrage. La correction faite conserve la procédure.
3. **R653-9 et R653-10** : le texte de l'article 102 de la loi n° 2025-1403 et ses dispositions transitoires ne sont pas au corpus. La frontière entre générations est renvoyée à ces dispositions, sans date inventée.
4. **Anomalie d'inventaire** : il faut inscrire les articles créés par l'ordonnance n° 2026-648, notamment L760-15.
5. **Hors paquet** : L861-3 a une version VIGUEUR_DIFF (LEGIARTI000048702084, borne 2222-02-22) sans proposition. Elle rétablit la majoration de 10 % supprimée par le projet. Elle n'est pas dans mon paquet et n'est pas examinée ici.

Revue IA, qui ne vaut pas validation par un juriste.
