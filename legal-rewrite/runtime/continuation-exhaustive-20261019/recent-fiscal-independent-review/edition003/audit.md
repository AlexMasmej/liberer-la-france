# Revue indépendante finale — édition003

Les deux propositions entières et leurs sources/notes ont été relues : annexeIII382-0Cter et CGI1681quaterA. Les quatre références et les deux entrées382-0Cbis avaient également été lues intégralement ; leurs gardes ont été vérifiées à nouveau en même temps que les deux sources003.

**Le constatFISCAL-C-NOV est résolu dans cette édition003. Aucun autre défaut opératoire concret n'a été détecté sur ce paquet.** Le rapport historique002 est conservé sans changement pour tracer la raison de la coordination législative.

SourceSHA256 :82cc9ccb62f960499fc416f4accf44900e1cdc942c6e4f75a8f55e6b7b0aab57.

RéponseSHA256 :ab6efe471abca2c1baedb73471983e6736a1f5f8be1707c059e086f6d06a7942.

## Articulation vérifiée

LeC législatif prévoit désormais expressément que les seules parts de rattrapage réparties sur les trois premiers prélèvements peuvent être perçues en novembre au-delà d'une mensualitéB. Le solde ordinaire de novembre conserve son plafond. L'exception couvre le choix du contribuable **et** l'étalement par défaut du contribuable non soumis à acompte obligatoire ; aucune option expresse nouvelle ne lui est imposée.

Les parts futures sont réservées pour calculer le solde ordinaire sans en avancer les échéances. Les sommes déjà payées ne sont imputées qu'une fois ; réserver une part future n'est pas constater un paiement encaissé ni créer un remboursement fictif. Le total prélevé reste limité aux taxes dues et leD conserve arrêt et remboursement du trop-perçu réel. Les droits antérieurs à remboursement, exonérations, plafonnements, assiette et taux restent intacts.

La dernière première mensualité ordinaire permise la même année par lesCbis demeure octobre. Le rattrapage commencé alors peut avoir ses deux autres parts en novembre/décembre ; ce ne sont pas deux nouvelles premières mensualités ordinaires. Lorsqu'il n'existe plus d'échéance mensuelle ouverte, le début de janvier suivant reste prévu, avec le regroupement particulier janvier/février des options de fin décembre.

Le choix de rattrapage reste exprimable dans la demande existante ou avant le premier prélèvement, sans nouvelle preuve ni formulaire. Le remboursement d'un acompte excédentaire avant la fin du mois suivant l'option est conservé. Le régime de solde en cas de rôle mis en recouvrement après le31octobre et les règles légales de modulation/sanctions ne sont pas supprimés sous couvert de modalités réglementaires.

## Comparaison intégrale

Le premier paragrapheC est le seul passage modifié de1681quaterA. La comparaison par octets, balises et blancs confirme que tout le reste est identique : A, totalité deB, second paragrapheC, D, E etF. Sont donc conservés notamment les mensualités janvier-octobre, le dégrèvement attendu, le30septembre, le dernier jour du mois précédent, la marge de20%, la majoration de5%, les articles1663/1731/1731A pour le rôle tardif, l'arrêt au montant recouvré et le remboursement au plus tard à la fin du mois suivant le constat du trop-perçu.

L'objet entier382-0Cter de003, métadonnées incluses, est identique à celui002 déjà lu. Il n'y a aucune nouvelle suppression cachée dans cette reprise.

## Cas du plafond de novembre

calendar-cases.json conserve trois illustrations arithmétiques à mensualitéB=100 et rattrapage déjà déterminé=400. Le calcul du montant individuel de rattrapage n'est pas simulé : il reste celui du texte applicable. Ces montants sont des entrées d'exemple, pas des recettes nationales ni un nouveau taux.

Pour une taxe finale de1200 avec500 déjà payés, le calcul illustratif conduit à un versement ordinaire de100 et une part de400/3 en octobre ; le solde ordinaire restant est200 après réservation des deux parts futures. En novembre, le prélèvement ordinaire reste100, auquel s'ajoute la seule part de400/3 expressément autorisée hors plafond. Décembre comporte le reste du solde ordinaire et la dernière part. Total final1200, sans double paiement ni anticipation.

Avec une taxe finale de1000, il n'existe plus de solde ordinaire après réservation, mais les parts de novembre/décembre demeurent payables : réserver n'est pas les traiter comme déjà encaissées. Avec une taxe connue de800, la dernière somme nécessaire est bornée à ce qui reste dû et les prélèvements cessent ; les parts prévues n'autorisent pas à dépasser l'impôt. Les éventuels trop-perçus déjà constitués restent remboursables au titre duD. Ce contrôle ne prétend pas tester le logiciel de recouvrement de l'administration.

## Classement et intégrité

382-0Cter : **payment_timing_relief**, effet **payment_deferred**.1681quaterA : **coordination_only**, même measure_id cfe-monthly-catchup-three-instalments. Une seule facilité de calendrier est donc suivie ; ni deuxième baisse d'impôt ni économie budgétaire nationale n'est comptée.

validate_answer et substantive_impact.validate passent. Les sept gardes uniques corps/document/notes/avant-image concordent ; l'absence de proposition antérieure de1681quaterA est confirmée. Les fichiers du rédacteur sont toujours identiques aux copies gelées. Cette revue ne modifie aucun fichier de l'auteur, source canonique, base, politique, lot, module ou publication et n'est pas une certification par un juriste.
