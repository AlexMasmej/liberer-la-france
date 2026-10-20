# Revue indépendante CVAE — édition002

**Un correctif opératoire est nécessaire dans l’annexeIV214 ; aucun autre défaut concret bloquant n’a été relevé dans les37 candidats de cette édition.** Le texte entier corrigé est fourni dans `answer.json`, avec source, avant-images et gardes. Aucun fichier de l’auteur ni aucune proposition en base n’a été modifié.

## Édition stable relue

Dossier auteur : `cvae/editions/002/`.

- `answer.json` : SHA256 **277bb35e5ab78c5ec988d8da2eee9590f56e9d9b7b6051047a8e3acd92b12fea**,37 candidats.
- `source.json` et `expected.json` : SHA256 **074b299c6059591cdecb1367796e6de9ca393f6cbe179b04f04511500550b147**,43 sources.

Les35 premiers corps sont **identiques octet pour octet à l’édition001**, déjà relue. Les deux nouveaux articles1679quinquies et annexeIV214 ont été relus intégralement, avec leurs sources, notes et avant-image lorsqu’elle existe. Les sources supplémentaires1382-0,1635quaterE et1640B ont aussi été lues ; leurs renvois1586 concernent des régimes fonciers, la taxe d’aménagement ou une compensation historique2010, et non une CVAE future. La revue du long CGI39 reste explicitement **ciblée sur son renvoiCET/1679quinquies**, sans nouvelle validation de tout cet article. Au total :42 sources entièrement examinées et une source examinée sur le seul renvoi pertinent.

La [revue détaillée de l’édition001](audit-edition001.md) demeure valable pour les35 corps inchangés : date, anciennes années, CFE, définitions de valeur ajoutée, exonérations1600, acomptes, déclarations, sanctions et annexes. Le relevé des37 candidats est dans `article-findings-edition002.json`.

## Correction requise : annexeIV214,I,1°,c

La source et l’avant-image permettent une délégation sans limite de montant pour les demandes de plafonnement présentées par une entreprise dont **tous les établissements se trouvent dans le ressort territorial d’un service des impôts des entreprises**. La condition vise toutes les demandes concernées, avec la règle complémentaire du2° pour les services regroupés sur un site.

Dans le candidat002, la condition est déplacée après l’incise :

> « y compris les demandes relatives aux anciennes années de contribution économique territoriale présentées par une entreprise dont tous les établissements… »

Elle se rattache alors aux seules demandes historiques, et ne conditionne plus clairement les nouvelles demandes de plafonnementCFE. Cela élargit potentiellement la délégation territoriale, alors que les notes disent qu’elle est inchangée. Ce n’est pas une simple préférence de style : le périmètre des décisions pouvant être signées sans plafond est concerné.

**Correction minimale :** placer la condition territoriale commune avant l’incise historique, puis écrire « y compris celles relatives aux anciennes années de contribution économique territoriale ». Tous les autres paragraphes sont conservés. La correction ne crée ni nouvelle restriction territoriale ni plafond de remboursement ; elle maintient le champ antérieur explicitement annoncé.

Pièces :

- `answer.json` : **article214 entier corrigé**, une seule entrée.
- `correction-source.json` : source et note entières, avant-image en base et candidat002 audité.
- `expected.json` : garde pour la proposition actuellement enregistrée en base.
- `candidate-guards.json` : garde du candidat002 en plus de la garde de base.

Empreintes distinctes à ne pas confondre :

| Élément | SHA256 du texte proposé |
|---|---|
| Avant-image actuellement en base | bd07f5dec58cdc5b0caaf234d0805728ddd8ad2ffa39e74ecb3f2913fe4d2ac4 |
| Candidat214 de l’édition002 |14ca5a0dc805814222574b97722a5f90eb1999198ed3a3514f2543a2536550d9|
| Article214 corrigé livré |f0723c4e55cacc93ffd26c33bb8500e36519ed30de78026ceb69a88c78f4e49e|

## Nouveau1679quinquies : cohérent

Seul le dernier alinéa adapte le dégrèvement attendu au plafonnement de1647Bsexies et confirme son utilisation après suppression de la CVAE. Les anciennes années restent soumises à leur plafonnementCET. Les acomptesCFE de50%, le seuil3000euros, le critère de baisse de base25%, les dates et formalités existantes restent identiques. Aucune CVAE future n’est réintroduite.

## Conclusions conservées de001

Les douze exonérations de1600, la moitié de base des artisans, son taux additionnelCFE1,12% et le corps entier deII restent identiques à la source. La taxe additionnelleCVAE disparaît sans transfert vers la CFE. Les définitions1586sexies sont entièrement conservées et deviennent autonomes ; les périodes de1586quinquies restent utiles au plafonnement.

Les baisses programmées du plafonnement sont conservées :1,531% en2026/2027,1,438% en2028,1,344% en2029 et1,25% à partir de2030. Les trois sources futures complètes ont été examinées. La date de suppression reste le1erjanvier de l’année suivant celle de l’entrée en vigueur de la loi, sans date de promulgation inventée.

Les anciens soldes, rappels, exonérations, dégrèvements, restitutions et recours sont sauvegardés. Un acompte versé pour une année supprimée est restituable sans déclaration annuelle de CVAE. L’édition stable ne crée plus de nouveau remboursement sous soixante jours : elle renvoie aux règles de réclamation des indus ; les délais applicables aux anciennes années demeurent.

La **CFE nette** peut varier mécaniquement lorsque le précédent dégrèvementCET imputé sur elle couvrait aussi la CVAE. Aucun taux ou base de CFE ne monte et le totalCET ne croît pas pour cette raison. Il faut éviter d’affirmer qu’elle reste identique dans tous les cas. L’exemple chiffré et son raisonnement figurent dans la revue001 ; aucun montant de financement n’en est déduit.

##2030 et périmètre restant

La source future **annexeII310HC,LEGIARTI000047814988** et sa note ont été lues. C’est un article distinct, applicable en2030, qui renvoie aux4° et7° duI de1647BsexiesA. Son régime territorial de la navigation aérienne et maritime reste intact ; il ne doit pas être confondu avec une nouvelle version de317septiesE. Aucun candidat n’a été inventé pour déplacer ou abroger cet avantage futur.

**La coordination globale n’est pas achevée.** Restent annoncés mais non entièrement rédigés/revus : calendriers des lois2022-1726art55,2023-1322art79 et2025-127art62 ; transfert2030 vers1647BsexiesA et textes d’application ; LPF,CCI/affectations et modèles déclaratifs. Les pistes et limites de l’auteur sont archivées dans `audited-edition002-limits-and-primary-sources.json`. Une liste de sources ne remplace pas les textes opératoires nécessaires.

## Contrôles

`validate_answer` passe pour les37 candidats002 et pour le correctif214. Les35 corps communs concordent exactement avec001 ; les37 empreintes de proposition concordent. Les43 empreintes brutes et de corps sources sont correctes ; les43 gardes d’avant-image correspondent encore à la base. Les copies auditées correspondent à l’édition figée. Ces contrôles d’intégrité ne remplacent pas les conclusions de fond ci-dessus.

Aucune base, source, lot, manifeste actif ou publication n’a été modifié. Les lacunes graphiques fiscales antérieures restent explicites.
