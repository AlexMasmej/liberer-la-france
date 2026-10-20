# Quatre lacunes graphiques du Code du travail

Les lots `batches/complements-travail/001.json` à `004.json` sont des propositions de réécriture complètes, non des règles en vigueur ou des validations juridiques. Ils ont été enregistrés par `register_batches.py --commit` sous verrou partagé le 19 octobre 2026. Aucun fichier public n’a été modifié par cet agent.

| Lot | Entrée | Restitution |
| --- | --- | --- |
| 001 | Annexe I — LEGIARTI000040477365 | Toutes les expressions intégrales et discrètes a à o, tableaux 1.1 à 1.3, 221 pondérations S, pondérations B/R, définitions et ajout français de 2019 sur la source apparente. Huit images vérifiées et une transcription de l’ajout. |
| 002 | Annexe II — LEGIARTI000023018851 | Huit tableaux HTML conservés, tableau 2.3 manquant restitué avec ses quatre notes ; définitions, trois règles cumulatives et sept bandes Tmin. Coquilles du XML corrigées après confrontation visuelle, sans changer volontairement de seuil. |
| 003 | R4453-3 — LEGIARTI000032980606 | Matrice française entière dépliée en dix bandes et sept notes. Pas de substitution par le tableau européen initial erroné. |
| 004 | R4453-4 — LEGIARTI000043948605 | Quatorze bandes d’effets directs et sept notes ; sept bandes d’effets indirects et quatre notes. Renvois des notes (3) et (6) corrigés vers R4453-3 conformément au décret 2021-1091. |

## Sources effectivement contrôlées

- `rayonnements-optiques/directive-2006-25-ce-fr-2014.pdf` : édition française consolidée au 1er janvier 2014 de la directive 2006/25/CE, obtenue auprès de l’Office des publications de l’Union européenne. Pages 14 à 28 examinées, dont toutes les expressions, les tableaux et leurs notes. Les extraits utilisés dans les projets sont enregistrés dans `media/optique-*.png` et leurs empreintes figurent dans les compagnons.
- Décret français 2019-1547, article 3, texte officiel consulté sur Légifrance : `https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000039699711`. Ajout de la définition α / source apparente. La définition est transcrite dans l’annexe I et son compagnon.
- `champs-electromagnetiques/jo-20160806-texte27-copie-nextinpact.pdf` : copie publique du document DILA, JO du 6 août 2016, texte 27, pages 2 et 3 examinées visuellement. Provenance : `https://cdn2.nextinpact.com/medias/joe_20160806_0182_0027.pdf`. Les métadonnées identifient la DILA ; le fichier ne contient aucune signature PDF. Cette provenance documentaire est explicitement distinguée d’un téléchargement officiel authentifié actuel.
- `champs-electromagnetiques/inrs-ed4204.pdf` : INRS ED 4204, octobre 2018, pages 2 à 4 examinées visuellement, source `https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-4204.pdf`. Toutes les valeurs d’action directes et indirectes sont confrontées à ce document postérieur au rectificatif de 2017. Les bornes du tableau français sont conservées lorsque le document INRS présente différemment une fréquence de bord.
- `champs-electromagnetiques/sometrav-paca-propositions-2017.pdf`, page 18 : reproduction documentaire indépendante de toute la matrice française R4453-3 et de ses sept notes. Les bornes françaises retenues restent celles de la copie JO.
- `champs-electromagnetiques/directive-2013-35-ue-fr.pdf` : directive européenne initiale, obtenue auprès de l’Office des publications. **Son tableau A3 comporte les erreurs imprimées corrigées en décembre 2013**. Il n’est pas employé pour remplacer les valeurs françaises correctes : 0,07 constant pour 10 à 25 Hz et 0,0028 f pour 25 à 400 Hz. Rectificatif officiel identifié : CELEX 32013L0035R(01).
- Décret 2021-1091, article 2, texte officiel lu sur Légifrance : `https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000043947126`. Il remplace les renvois R4453-2 par R4453-3 dans les notes directes (3) et (6). Cette correction est appliquée dans le projet.

## Réserves conservées

Les quatre compagnons portent `documentary_recovery_complete=true` et `authenticated_jo_crosscheck_complete=false`. Cette distinction signifie que les tableaux ne sont plus manquants dans la proposition ; elle ne transforme pas les contrôles documentaires en validation juridique.

- Annexes optiques : source normative européenne, mais confrontation aux tableaux du JO français de 2010 et 2019 non effectuée.
- R4453-3 : confrontation à une copie du JO, sans signature vérifiable dans le fichier, et non à un téléchargement officiel authentifié.
- R4453-4 : le rectificatif du JO du 8 avril 2017, texte 22, NOR ETST1611714Z, est identifié. Son fac-similé n’a pas pu être récupéré. Les tableaux sont reconstitués à partir du JO 2016 et confrontés à INRS 2018 ; la concordance graphique exacte avec le rectificatif demeure réservée. La correction textuelle de 2021 a été vérifiée directement.
- Les paramètres complémentaires définis par l’arrêté du 5 décembre 2016 ne sont pas importés dans ces articles : ils ne figurent pas dans les matrices françaises à restituer. Ils restent régis par leurs textes propres.

## Documents écartés et accès non contournés

La reproduction IHF contient, à l’emplacement de R4453-2 et R4453-3, du texte sans rapport avec les champs électromagnétiques : elle est exclue de toute restitution. Le guide de la Commission de 2015 conserve les erreurs du tableau A3 initial : il est également exclu pour ces valeurs. La documentation optique INRS plus récente décrit des recommandations qui ne doivent pas remplacer silencieusement les seuils réglementaires de 2010.

Les refus d’accès aux PDF Légifrance et à certains fichiers ministériels n’ont pas été contournés. Aucun téléchargement CUA n’a été relancé. Un téléchargement ministériel renvoyant une page HTML de protection a été renommé `.blocked.html` ; le fichier vide issu d’une tentative européenne initiale a été supprimé. Aucun de ces fichiers n’est enregistré comme PDF de preuve.

## Contrôles

Les quatre sources canoniques n’ont pas été modifiées. Leur numéro et leur empreinte correspondent à la base. Les quatre projets passent le validateur partagé : balisage permis et équilibré, aucune table, ligne ou cellule source perdue, tous les marqueurs récupérés présents dans le texte, empreintes de tous les documents et médias conformes.

Le bilan local est enregistré dans `recovery-four-articles.json`. La sortie de l’enregistrement partagé est conservée dans `registration-four-tables.json` ; son total global peut être dépassé par les autres rédacteurs après ce contrôle.
