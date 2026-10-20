# Revue indépendante CVAE — édition001

**Aucune erreur normative concrète bloquante relevée dans les35 candidats de cette édition.** Aucun correctif entier n’est donc proposé : `answer.json=[]`. La suppression n’est toutefois **pas encore intégralement coordonnée** : les deux coordinations annoncées dans l’édition002 et le compagnon des rédactions différées2030 ne sont pas compris dans cet avis.

## Édition exactement auditée

Dossier auteur figé : `cvae/editions/001/`.

- `source.json` : SHA256 **311b6884bcbcf6f906ba18b05b4ccd6a3eddfcc7530ef0e2346c2f2e888b46f9** —37 sources.
- `answer.json` : SHA256 **bd4c9c5c68d9f3d1f77b1e5b4033221ba61c69a24b1da9b64243936b008c0474** —35 candidats.
- `expected.json` : SHA256 **65de1cee700bb99f04aa3a3591d029fc1a00acaf1735bb47fc91b98c760d78ea**.

Une première édition de27 candidats (SHA6bf4c552…) avait été relue. La mutation a été détectée avant conclusion ; les huit ajouts et les quatre modifications ont ensuite été examinés. Les deux éditions exactes sont archivées dans ce dossier, sans modification des fichiers de l’auteur.

Les37 sources et leurs notes ont été examinées, ainsi que les35 textes proposés, motifs et notes. Les trois rédactions futures officielles du plafonnement ont aussi été lues intégralement. Les doublons exacts de transition ont été identifiés par empreinte : les onze articles328G ont le même texte proposé, mais leurs sources propres ont été examinées séparément. Pour les longs textes conservés, le contrôle du corps intégral a été complété par une comparaison exhaustive des modifications.

## Résultats de fond

### Date, anciennes années et paiements

Le critère commun est **le1erjanvier de l’année suivant celle au cours de laquelle la loi entre en vigueur**. Aucune date de promulgation n’est inventée. Le critère porte sur l’année d’imposition, non sur la date du paiement ou du dépôt : un solde, rappel ou contrôle ultérieur concernant une ancienne année ne devient pas une nouvelle CVAE.

1586ter et les textes d’application ferment assujettissement, assiette, taux, acomptes, soldes, déclarations de valeur ajoutée et d’effectifs pour les années supprimées. Les droits anciens à exonération, abattement, dégrèvement, imputation, restitution et recours restent ouverts dans leurs conditions et délais. Le seuil historique de63euros de1586septies et le dégrèvement de188euros de1586quater restent utiles aux anciennes années qui en relèvent ; ils ne limitent pas la suppression générale future.

1679septies exclut un acompte d’une année supprimée même si son calcul aurait utilisé une ancienne base. Toute somme indûment versée au titre de cette année est restituable sans liquidation annuelle de CVAE. **Attention au changement entre éditions :** le premier projet de27 articles prévoyait un nouveau délai de remboursement de soixante jours ; l’édition001 de35 articles l’a remplacé par les procédures, garanties et délais de réclamation de droit commun. Les délais anciens, notamment le remboursement des excédents après liquidation d’une ancienne année, sont conservés. Le présent avis porte sur cette dernière formulation, sans promettre un nouveau remboursement automatique sous soixante jours.

1731 conserve ses1,2 et4 ; son3 neutralise les sanctions d’acomptes inexistants.1770decies ne sanctionne plus une déclaration supprimée. Les réserves de loi répressive plus douce et les recours sont exprimés pour les anciennes périodes.

### Plafonnement de CFE et calendrier de baisse

1647Bsexies conserve le plafonnement, le délai de réclamation, la valeur ajoutée micro égale à80% des recettes moins achats, les règles de période et d’annualisation, les exclusions de taxes additionnelles, le plancher de cotisation minimum, l’imputation sur la CFE, les procédures et l’ordonnancement sous six mois.

Les taux sont ceux des sources officielles conservées :

| Année | Taux du plafonnement |
|---|---:|
|2026–2027|1,531%|
|2028|1,438%|
|2029|1,344%|
|2030 et suivantes|1,25%|

Les versions futures sont identifiées dans `audited-future-cap-sources.json` : LEGIARTI000051248428, LEGIARTI000051248495 et LEGIARTI000048860644. Leur lecture confirme les taux. Leurs notes de report législatif ne sont pas prises pour la date de la nouvelle réforme. Les tentatives d’ouverture de deux de ces pages par le moteur web n’ont pas abouti ; la preuve utilisée est le XML officiel DILA complet fourni dans le paquet.

**Nuance de communication et de calcul :** aucun taux ou base de CFE n’est relevé, mais la CFE nette ne reste pas nécessairement identique, car l’ancien dégrèvement CET était imputé sur la CFE tout en plafonnant la somme CFE+CVAE. Exemple de contrôle, hors taxes exclues et avec minimum non contraignant : valeur ajoutée100000€, CFE3000€, CVAE280€, plafond1531€. Avant : dégrèvement1749€, CFE nette1251€ +CVAE280€. Après : dégrèvement1469€, CFE nette1531€, CVAE0€. Le total reste1531€, sans hausse globale ; la part nette appelée CFE augmente mécaniquement. Cet effet ne justifie ni une CVAE fictive à déduire ni une nouvelle déclaration. Il faut éviter l’affirmation universelle « CFE nette inchangée ». Les dégrèvements acquis des anciennes années sont, eux, protégés.

La clause générale interdisant la réduction des dégrèvements se lit comme conservation de leurs régimes légaux ; la formule de1647Bsexies produit l’effet mécanique ci-dessus. Le texte spécifique ne promet pas de figer chaque montant futur de remboursement.

### Définitions autonomes et avantages maintenus

1586sexies reprend **octet pour octet tout le corps source** entre une clause initiale de champ et une transition finale. Sont ainsi maintenus les secteurs BIC/BNC/foncier, banques, gestion d’instruments financiers, financements et assurances, les exclusions de95%, les plafonds80/85%, le seuil7,6millions, les déductions et la règle des plus-values de création. La conservation des définitions n’institue ni assiette ni déclaration de CVAE future.

1586quinquies conserve les périodes atypiques, l’absence de clôture, les créations, les exercices multiples et la prévention du double compte. L’annualisation supprimée concernait le seuil et le barème CVAE ; l’annualisation propre au plafonnement CFE demeure dans1647Bsexies.1447 continue donc de trouver une définition pour son seuil de chiffre d’affaires de100000euros des locations nues, sans augmentation de ce seuil ni de son champ.

1586nonies supprime les seules exonérations d’une CVAE elle-même supprimée, sans retirer les exonérations de CFE1466A/F ou d’autres impôts maintenus. Les anciennes conditions et plafonds restent applicables à leurs années.238bisHW préserve l’accès au dispositif d’approvisionnement électrique par un renvoi de définition figé, indépendant du paiement de CVAE ; le ratio2,5kWh/€, les quinze ans,55%,8000heures et600000euros demeurent. Les justificatifs comptables remplacent toute demande de déclaration CVAE pour cette seule preuve.

### Article1600 : taxe pour frais de chambres

L’ensemble des **douze exonérations**, la réduction de moitié de la base des artisans et **tout leII relatif à la CFE** sont repris octet pour octet. Le taux de taxe additionnelle CFE reste1,12%. La taxe additionnelle CVAE de9,23% disparaît pour les années supprimées, sans transfert de son montant vers la CFE. Ses anciennes années et leurs exonérations, dégrèvements, restitutions et recours sont conservés.

344quindecies n’a pas de candidat dans001 : la source fixe des abattements de99% **pour2025**. Son caractère historique et les droits de cette année demeurent. Aucune reconduction automatique pour une année future n’est déduite de ce texte annuel ; l’audit ne prétend pas avoir retrouvé un nouveau taux annuel absent de cette source.

### Déclarations et annexes

Les coupes mixtes sont limitées aux champs CVAE : IV de1649quaterBquater,3 de1681septies, II3° de l’annexeIII38, Im de40A, III de46C,1°g/2°l de39,6° de344-0B, référence CVAE de344I-0bis et recouvrement CVAE de406terdecies. Les simplifications antérieures de réemploi des données et les autres rubriques restent présentes. Les champs de salaire, retraite, options/actions, résidents suisses et impatriés de39 ne sont pas retranchés. La suppression des obligations990I pour nouveaux décès n’est pas annulée par ces reprises.

317septiesE et les onze articles328G retirent les déclarations et répartitions territoriales exclusivement CVAE pour les nouvelles années. Ils ne retirent pas une obligation salariale ou fiscale indépendante. Les anciennes règles territoriales restent disponibles pour les anciennes années.

## Contrôles et limites d’intégration

`validate_answer` passe sur les35 candidats. Les35 empreintes des propositions concordent ; les37 empreintes de XML bruts, empreintes de corps et avant-images en base ont été vérifiées sans divergence. Les copies relues concordent exactement avec l’édition001 figée. `article-findings.json` donne une conclusion pour chacun des35 candidats, `current-guards.json` les gardes ; aucune écriture de base ou lot n’a été effectuée.

**Restent hors de cet avis :** l’édition002 annoncée pour1679quinquies et annexeIV214, ainsi que les dispositions de loi différées2028/2029/2030 et le transfert vers1647BsexiesA. Leur articulation doit être effectivement rédigée et relue pour éviter qu’un calendrier antérieur rétablisse un prélèvement ou casse une définition. Une réserve documentaire ne suffit pas à déclarer la coordination achevée. Les modèles et effets budgétaires hors corpus n’ont pas fait ici l’objet d’une certification générale. Aucun financement ou économie nationale n’est inventé.

Les deux lacunes graphiques fiscales antérieures restent explicites. Le présent audit n’active aucune pièce jointe, ne modifie aucune source ni manifeste actif et n’effectue aucune publication.
