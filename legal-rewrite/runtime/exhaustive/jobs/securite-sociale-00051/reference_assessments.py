# Ce fichier est exécuté par build_answer.py après rédaction des corps normatifs.
# Les clés requises et empreintes sont reprises exclusivement du paquet fourni.
contexts = {
    'L330-1': "L330-1 définit les prestations et leur remboursement entre caisses, sans régir la rupture d'une relation de travail.",
    'L331-3': "Les six/dix semaines, les huit semaines de repos minimal et les prolongations de L331-3 sont des périodes de protection maternelle indemnisées.",
    'L331-3-1': "L331-3-1 distingue le travail salarié de l'élue et l'exercice de son mandat local ; ce mandat n'est pas un contrat privé.",
    'L331-4': "L331-4 porte l'indemnisation maternelle à huit/dix-huit semaines selon la charge ou les naissances antérieures ; vingt-six semaines ne désignent pas une durée d'emploi.",
    'L331-4-1': "L331-4-1 permet un report prénatal/postnatal de trois semaines sur prescription ; la demande aménage le repos et ne notifie pas une rupture.",
    'L331-5': "L331-5 prévoit un report après hospitalisation de l'enfant et un supplément médical de deux semaines ; aucune de ces durées ne termine le contrat.",
    'L331-6': "L331-6 indemnise, après décès de la mère, la durée restante du repos, avec dispense de L313-1 et bénéficiaire subsidiaire ; le maintien de traitement peut relever d'un régime public.",
    'L331-7': "L331-7 indemnise l'adoption ou l'accueil pendant seize, dix-huit ou vingt-deux semaines, avec dérogation pour le mandat local ; ce sont des congés et non des emplois à terme.",
    'L331-8': "L331-8 indemnise vingt-cinq ou trente-deux jours de paternité/accueil et l'hospitalisation, avec un repos minimal de quatre jours ; l'annonce du congé n'est pas une notification de rupture.",
    'L331-8-1': "L331-8-1 indemnise le congé supplémentaire de naissance ; la proposition conserve les conditions d'accès et retire la baisse propre au second mois, sans limiter l'emploi à deux mois.",
    'L331-8-2': "L331-8-2 coordonne les non-cumuls de revenus de remplacement ; sa liste ne prononce aucune fin de contrat ni suppression de congé.",
    'L331-9': "L331-9 indemnise le deuil ; ses quinze jours pour les personnes relevant de L161-8/L311-5 sont une durée de prestation, distincte du préavis de rupture.",
    'L333-1': "L333-1 indemnise une suspension protectrice hors congé légal de maternité, faute de reclassement hors travail de nuit ou risque ; la suspension n'est pas une rupture.",
    'L333-2': "L333-2 fait débuter l'allocation à la suspension du contrat et cesser le paiement si ses conditions disparaissent ; il ne met pas fin à l'emploi.",
    'L333-3': "L333-3 vise six non-cumuls de l'allocation de dispense de travail, avec limites favorables pour handicap et PreParE ; il ne définit pas une indemnité de rupture.",
    'L341-3': "L341-3 apprécie l'invalidité selon les capacités et quatre moments médicaux ; la consolidation, l'épuisement des indemnités ou la stabilisation ne terminent pas automatiquement le contrat.",
}

common = {
    'L1234-1': "La vue de L1234-1 est une proposition, distincte de sa source officielle : quinze jours calendaires de préavis patronal individuel sans condition d'ancienneté pour le nouveau contrat unique. Ce délai, lié à la notification de rupture selon la coordination L1234-3, ne réduit pas les durées sociales ici visées. Les anciens contrats conservent leurs préavis antérieurs ; procédures collectives, autorisations de salariés protégés et protections de maternité restent distinctes. Aucun renvoi direct à L1234-1 n'est ajouté.",
    'L1221-2': "La vue proposée de L1221-2 impose une durée indéterminée aux nouvelles relations privées et interdit qu'une mission, une formation ou une date mette fin automatiquement à l'emploi. Les bénéficiaires éligibles du nouveau contrat unique restent couverts par la prestation ici examinée, sans réserver l'avantage aux anciens CDD. Les contrats antérieurs gardent leur transition. Ni mandat électif ni régime d'agent public ne sont artificiellement soumis à ce contrat privé.",
    'L1234-9': "La vue proposée de L1234-9 concerne l'indemnité ordinaire patronale de rupture, avec son exception de faute grave : zéro avant un an mesuré au terme effectif, préavis inclus ; ensuite 0,20 mois par année totale, mois complets au prorata et plafond de six mois, sans retrancher la première année. Ce seuil ne conditionne pas la prestation sociale ici visée. Les services antérieurs gardent leur composante protégée ; salaires, congés, indemnités spéciales et réparation d'illégalité restent distincts. Aucun renvoi à ce barème n'est ajouté.",
}

specific = {
'L330-1': {
    'L331-3': "Le 2° de L330-1 comprend l'indemnité de repos de L331-3 et ses quatre alinéas (maternité ordinaire, multiples, naissance anticipée, grande prématurité hospitalisée). La vue est la source officielle entière, sans proposition : elle reste maintenue dans le lot. Le remboursement de 60 % est fixé par L223-1 6° a), non par les durées de congé et sans condition d'ancienneté de rupture.",
    'L331-5': "L331-5 ajoute report pour hospitalisation et deux semaines médicales au régime de repos inclus dans le 2°. La cible officielle maintenue ne crée ni nouvelle cotisation ni indemnité de licenciement ; son remboursement suit L223-1 6° a). Le report du premier alinéa et la priorité du deuxième restent ouverts, sans déplacer les alinéas.",
    'L333-1': "L333-1, compris dans le 2°, ouvre l'allocation hors congé de maternité pour suspension protectrice. La vue officielle fournie garde deux anciens numéros du code du travail ; le présent lot les coordonne à L1225-10/L1225-14 après lecture du corpus. L330-1 conserve cette allocation et la quote-part de L223-1, sans importer le seuil d'un an de rupture.",
    'L331-6': "L331-6, inclus dans le 2°, est le relais au père puis, faute de demande, au conjoint/PACS/concubin après décès maternel. La dispense totale des conditions de L313-1 et le maintien de traitement public comme borne alternative sont conservés. Le remboursement entre caisses n'instaure aucune condition nouvelle d'ancienneté et ne fiscalise pas le décès.",
    'L331-8': "Le 3° renvoie bien à L331-8, indemnité de paternité/accueil de vingt-cinq ou trente-deux jours, avec prolongation hospitalière et dérogation pour mandat local. Sa vue officielle est maintenue ; les conditions de liquidation renvoyées à L331-3 ne transforment pas cette durée en repos maternel de seize semaines. L223-1 6° b) conserve le remboursement total.",
    'L331-7': "L331-7 appartient au 2° mais son remboursement relève du 6° b), et non de la fraction de 60 % du a), de L223-1, avec réserve d'une prise en charge directe par l'employeur. La nouvelle formule « dans les proportions » corrige l'ambiguïté « en partie », sans modifier seize/dix-huit/vingt-deux semaines, l'accueil régulier ou les avantages du mandat local.",
    'L331-8-1': "La cible officielle L331-8-1 institue effectivement l'indemnité supplémentaire de naissance. Elle remplace donc L331-8-2 dans le 3° de L330-1. Sa fraction de revenu et son plafond subsistent ; le présent lot retire la dégressivité au second mois. Le remboursement de la totalité au 6° d) de L223-1 demeure, sans nouvelle durée d'affiliation cachée.",
    'L331-8-2': "L331-8-2 est une liste de non-cumuls, et non le fondement d'une indemnité à rembourser : le renvoi du 3° de L330-1 à cet article était incohérent. Il est remplacé par L331-8-1 ; les quatre exclusions restent applicables, avec correction séparée de l'intervalle réflexif du 2° dans ce lot. Aucun droit de prestation n'est retiré.",
    'L223-1': "Les 6° a), b) et d) de la source et de la vue proposée fixent respectivement 60 % pour maternité L331-3 à L331-6/allocations L333, totalité pour adoption sous réserve patronale, paternité et deuil, puis totalité pour L331-8-1. Le c) conserve les frais de gestion. L330-1 est rendu concordant ; les 7°/8° publics et spéciaux ne deviennent pas du contrat privé et aucune recette de compensation n'est créée.",
    'L331-9': "Le 3° cite correctement L331-9 pour le deuil, avec remboursement total prévu par L223-1 6° b). La source officielle maintient non-cumuls et subrogation patronale de plein droit. Les quinze jours du dernier alinéa concernent le maintien social L161-8/L311-5, sans lien avec une notification de rupture ou un seuil d'ancienneté d'un an.",
    'L333-3': "Le 2° comprend L333-3 comme règle du régime d'allocation de dispense, non comme créateur d'une prestation supplémentaire. Ses six non-cumuls sont maintenus, notamment la limitation du 2° à la cessation d'activité et du 5° à l'ouverture de la PreParE partielle. Aucun remboursement distinct, supplément d'assiette ou critère de rupture n'est ajouté.",
},
'L331-3-1': {
    'L331-3': "Les deux renvois au premier alinéa de L331-3 portent sur le travail salarié et les conditions du repos indemnisé. L331-3-1 y déroge expressément pour le mandat poursuivi avec indemnités de fonction ; si le mandat est interrompu, le droit à indemnité correspondant reste possible. La vue officielle de L331-3 demeure sans déplacement de son premier alinéa ni condition nouvelle d'ancienneté d'entreprise.",
    'L313-1': "Le renvoi vise les conditions sociales pour l'indemnisation propre au mandat interrompu, non l'indemnité ordinaire de rupture. La source de L313-1 exige rémunérations/heures au I et affiliation au II ; sa vue proposée retire l'affiliation minimale pour les périodes futures, y compris congé commencé. Maintenir le renvoi n'en rétablit pas l'ancienne durée et préserve les dérogations favorables.",
},
'L331-4': {
    'L331-3': "Le renvoi au premier alinéa de L331-3 remplace la durée ordinaire six/dix semaines par huit/dix-huit dans les deux situations de L331-4. La cible officielle est maintenue avec ses autres alinéas : multiples et supplément de grande prématurité ne disparaissent pas. L'avance volontaire de deux semaines et le total de vingt-six semaines ne sont ni délai de rupture ni ancienneté minimale d'emploi.",
},
'L331-4-1': {
    'L331-3': "La dérogation porte sur la répartition avant/après accouchement du repos indemnisé de L331-3, sans en effacer le droit ni les adaptations pour multiples et prématurité. Au maximum trois semaines sont déplacées sur prescription ; l'arrêt de travail ouvre l'indemnité dès son premier jour et réduit le report. La cible officielle maintenue conserve ses alinéas et ses protections sanitaires, sans seuil d'ancienneté patronale.",
},
'L331-5': {
    'L331-3': "Le premier alinéa vise le reliquat indemnisable de L331-3 ; le deuxième vise précisément son dernier alinéa, supplément pour naissance plus de six semaines avant terme avec hospitalisation. La cible officielle maintenue n'est pas déplacée : ce supplément est servi avant l'exercice du report, sans perte du reliquat ni création d'un nouveau préavis. Les huit semaines de repos de L331-3 gardent leur fonction protectrice.",
},
'L331-6': {
    'L331-3': "Le renvoi accorde au bénéficiaire du relais l'indemnité journalière de maternité mentionnée à L331-3 pour la seule durée restant entre décès et fin du droit de la mère. Il ne lui impose pas de reprendre toute la période prénatale ni un minimum d'ancienneté dans l'entreprise. La vue officielle demeure entière ; le maintien de traitement maternel est une borne alternative, y compris de régime public.",
    'L331-5': "Le deuxième alinéa de L331-6 vise exclusivement le premier alinéa de L331-5, report de tout ou partie du reliquat à la fin de l'hospitalisation lorsque l'enfant est resté hospitalisé jusqu'à la sixième semaine. Les autres alinéas ne sont pas importés indistinctement. Le droit au report reste accessible au bénéficiaire du relais, sans nouveau délai de notification de rupture.",
    'L313-1': "L331-6 écarte expressément l'ensemble des conditions de L313-1 pour le bénéficiaire après décès maternel, pas seulement le minimum d'affiliation de son II. La vue proposée de L313-1 supprime ce minimum pour d'autres situations ; elle ne réduit pas la dispense plus large du présent article. Rémunération/heures et ancienneté de rupture ne doivent donc pas être réintroduites par renvoi dans ce relais.",
},
'L331-7': {
    'L313-1': "Le dernier alinéa de L331-7 renvoie à L313-1 pour l'indemnité propre au mandat électif interrompu, alors que le mandat poursuivi et ses indemnités de fonction demeurent autorisés. La vue proposée retire l'affiliation minimale du II et conserve les tests de rémunération/heures applicables : le renvoi dynamique suit cet allègement sans créer une ancienneté d'entreprise ni réserver l'avantage aux anciens contrats.",
},
'L331-8': {
    'L331-3': "Le premier alinéa de L331-8 emprunte l'indemnité et ses conditions d'ouverture, liquidation et service à L331-3 ; il fixe lui-même vingt-cinq/trente-deux jours et le minimum de quatre jours lié à L1225-35. Il n'importe pas seize semaines de congé maternel, huit semaines de repos ou un seuil d'un an de rupture. La vue officielle de L331-3 est maintenue et ses alinéas ne sont pas déplacés.",
    'L313-1': "Le quatrième alinéa autorise une indemnité à raison du mandat interrompu si L313-1 est rempli, tandis que la poursuite du mandat et des indemnités de fonction reste permise. Le renvoi suit la vue proposée de L313-1 : conditions contributives conservées, affiliation minimale du II supprimée pour les périodes futures. Aucun justificatif de cette durée supprimée ni ancienneté patronale d'un an ne doit être réintroduit.",
},
'L331-8-1': {
    'L313-1': "Le premier alinéa vise bien les I et II de L313-1 pour l'indemnité de naissance : dans la vue proposée, le I garde rémunérations/heures et le II écarte expressément la durée minimale d'affiliation. Le renvoi reste cohérent et ne rétablit pas cette durée ; son III conserve la transition favorable aux périodes futures, congés commencés compris. L'absence de dégressivité du second mois ne supprime ni cessation d'activité ni ces conditions contributives.",
},
'L331-8-2': {
    'L331-3': "L331-3 est une indemnité maternelle distincte, correctement comprise dans le 2° du non-cumul. L'intervalle corrigé s'arrête à L331-8 puis vise séparément L331-9, sans retirer L331-3 ni ses allongements. La source officielle maintenue conserve quatre alinéas, et les durées maternelles ne sont pas des délais de rupture ou des conditions d'ancienneté.",
    'L331-5': "L331-5 demeure compris dans le 2° comme prolongation/report de l'indemnité maternelle, non comme une taxe ou un revenu supplémentaire supprimé. Son report après hospitalisation et son supplément de deux semaines restent possibles, pour une période distincte de l'indemnité de naissance. La correction de l'autorenvoi de L331-8-2 ne ferme pas ces avantages futurs.",
    'L331-6': "Le relais après décès de la mère prévu à L331-6 reste une indemnité maternelle distincte soumise au non-cumul de L331-8-2 sur la période commune. La dispense des conditions de L313-1, le report et les bénéficiaires subsidiaires sont maintenus. La liste ne transforme ni ce décès en fait générateur fiscal ni la durée restante en préavis de rupture.",
    'L331-8': "Le 2° corrigé inclut toujours L331-8 : les vingt-cinq/trente-deux jours, l'hospitalisation et les avantages des élus demeurent dans le régime de paternité, sans cumul avec le congé supplémentaire pour une même période. La source officielle ne porte aucune condition d'ancienneté d'un an et le repos minimal de quatre jours ne devient pas un délai de rupture.",
    'L331-7': "L331-7 reste visé par le 2° : indemnités d'adoption de seize, dix-huit ou vingt-deux semaines et indemnisation liée au mandat gardent leur champ propre. La correction de l'intervalle ne retire aucun droit d'adoption ni n'autorise deux revenus de remplacement simultanés. La durée d'accueil ou de congé ne constitue pas le terme d'un nouveau contrat unique.",
    'L331-8-1': "C'est l'indemnité dont L331-8-2 règle les exclusions. Le 2° officiel L331-3 à L331-9 l'incluait à tort dans son propre non-cumul ; la proposition exclut L331-8-1 de cet intervalle sans supprimer l'indemnité ni créer un cumul avec une autre prestation. Sa dégressivité est retirée séparément dans ce lot ; les conditions contributives suivent L313-1 proposé.",
    'L331-9': "Le 2° corrigé vise séparément L331-9 afin de garder le non-cumul avec le deuil, sans inclure L331-8-1 lui-même. Subrogation patronale et durée favorable de quinze jours pour les assurés L161-8/L311-5 restent dans la cible officielle maintenue. Ces quinze jours ne sont pas le préavis individuel du contrat unique et ne changent pas son point de départ par notification.",
    'L433-1': "Le 3° vise les indemnités AT-MP de L433-1, y compris son travail aménagé/partiel et son relais d'inaptitude dans leurs conditions propres ; il n'abolit aucune indemnité spéciale. La vue officielle comporte une note réservant la rédaction issue de l'article 81 de la loi de 2025 aux sinistres depuis le 1er janvier 2027 : le non-cumul n'avance pas cette transition ni ne convertit le délai L1226-11 en préavis de quinze jours.",
    'L321-1': "Le 1° concerne l'indemnité maladie pour incapacité médicalement constatée, dans les compétences respectives médecin/sage-femme/chirurgien-dentiste, avec sa dérogation favorable de cure thermale. La source officielle entière est distincte de l'indemnité supplémentaire de naissance. Aucun critère de rupture, d'un an d'ancienneté ou de durée déterminée d'emploi n'est importé par ce non-cumul.",
},
'L331-9': {
    'L331-3': "Le premier alinéa emprunte à L331-3 l'indemnité, sa liquidation et son service, mais la durée du deuil provient de L3142-1-1 ou du dernier alinéa de L331-9. Il ne transpose pas les six/dix semaines maternelles, le repos de huit semaines ou une grossesse au bénéficiaire. La cible officielle maintenue demeure à sa place ; aucune condition d'ancienneté de rupture n'est ajoutée.",
    'L311-5': "Le dernier alinéa vise les bénéficiaires du maintien de droits de L311-5, notamment chômage indemnisé, activité reprise insuffisante et situations d'indemnités nulles/faibles. La vue proposée précise le deuxième alinéa de L1235-16 sans fermer ces bénéficiaires futurs. Ils conservent quinze jours fractionnables d'indemnisation de deuil ; ce n'est ni une allocation nouvelle pour licenciement ni le préavis du contrat unique.",
    'L161-8': "Le maintien de droits de L161-8 est conditionné à résidence/séjour, absence de réouverture aux mêmes prestations et durée réglementaire, prolongée pour les demandeurs d'emploi ; les situations d'indemnités nulles/faibles demeurent. La vue proposée conserve cette portée. Le renvoi leur ouvre les quinze jours de deuil sans imposer une nouvelle affiliation ou un an d'ancienneté patronale.",
},
'L333-1': {
    'L323-5': "Le dernier alinéa importe la protection de l'indemnité contre saisie/cession au-delà des limites applicables aux rémunérations. La cible officielle entière ne contient aucune condition de durée de contrat ou d'ancienneté : elle doit rester applicable à l'allocation de dispense des nouveaux contrats uniques comme aux anciens, sans restriction par le barème de rupture.",
    'L313-1': "Le premier alinéa de L333-1 vise les conditions du I pour les prestations de son 2°, donc le test rémunérations/heures propre aux indemnités maladie ; il ne renvoie pas à un an d'ancienneté patronale. La vue proposée de L313-1 conserve ce I et retire l'affiliation minimale du II dans son champ. L333-1 n'a pas à réintroduire cette durée ni à supprimer les assimilations de L313-2.",
    'L323-4': "Le dernier alinéa emprunte le calcul fondé sur les dernières payes, fraction de revenus cotisés, plafond et valeur journalière réglementaires. La cible officielle entière et sa note d'application aux arrêts de 2020 sont conservées ; aucune base ni taux intermédiaire nouveau n'est inventé. Ce salaire de référence est celui d'une allocation sociale et non celui de l'indemnité ordinaire de rupture de L1234-9.",
},
'L333-3': {
    'L544-1': "Le 3° vise l'allocation journalière de présence parentale pour un enfant gravement malade, handicapé ou accidenté nécessitant présence et soins. L544-1 ouvre aussi expressément ce droit aux agents publics selon leur congé propre : le non-cumul demeure et ne les rattache pas au contrat privé unique. Les conditions d'ancienneté ou de notification d'une rupture sont sans objet dans cette cible.",
    'L331-8-1': "Le 6° vise l'indemnité supplémentaire de naissance créée par L331-8-1, dont l'accès dépend du congé L1225-46-2 et de L313-1. Le présent lot conserve cette exclusion tout en retirant la dégressivité du second mois dans l'article créateur. Aucun avantage n'est réservé aux anciens contrats et aucune durée de congé de un/deux mois ne devient un terme d'emploi.",
},
'L341-3': {
    'L321-1': "Le 2° situe l'appréciation d'invalidité à la fin de la période d'indemnités maladie de L321-1, tandis que le 3° permet une stabilisation antérieure. La cible officielle exige l'incapacité constatée par un professionnel compétent et préserve la dérogation de cure thermale ; son terme de prestation n'est pas un terme d'emploi. Aucune ancienneté de rupture ou notification de préavis n'est importée, et l'affiliation distincte supprimée dans L341-2 ne réapparaît pas ici.",
},
}

for a in answer:
    source_key = a['code_id']+'|'+a['source_id']
    checks = []
    for target_key in references['requirements'][source_key]:
        target = references['targets'][target_key]
        number = target['number']
        if number in common:
            assessment = contexts[a['number']]+' '+common[number]
        else:
            assessment = specific[a['number']][number]
        assessment = a['number']+' — cible '+number+' : '+assessment
        assert len(assessment) >= 80
        checks.append(dict(target_key=target_key,view_sha256=target['view_sha256'],assessment=assessment))
    a['reference_checks'] = checks
