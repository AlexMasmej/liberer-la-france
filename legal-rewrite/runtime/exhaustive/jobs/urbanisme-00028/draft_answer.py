import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
drafts = {}


def add(number, xml, reason, review):
    assert number not in drafts
    drafts[number] = (xml.strip(), reason, review)


add('L324-2-1 C', '''
<p>Lors de la fusion d'établissements publics de coopération intercommunale à fiscalité propre dont au moins un est membre d'un établissement public foncier local, l'établissement public de coopération intercommunale issu de la fusion devient membre de plein droit de cet établissement public foncier local à titre transitoire. Cette adhésion porte uniquement sur la partie de son territoire correspondant à celui de l'établissement ou des établissements publics de coopération intercommunale qui en étaient membres.</p>
<p>Lors de la création d'une commune nouvelle, si au moins une des anciennes communes qui la constituent est membre d'un établissement public foncier local, la commune nouvelle devient membre de plein droit de cet établissement à titre transitoire. Cette adhésion porte uniquement sur la partie de son territoire correspondant à celui de l'ancienne commune ou des anciennes communes qui en étaient membres.</p>
<p>Lorsqu'une commune membre d'un établissement public foncier local adhère à un établissement public de coopération intercommunale à fiscalité propre, ce dernier devient, à titre transitoire, membre de l'établissement public foncier local à la place de la commune. Cette adhésion porte uniquement sur la partie de son territoire correspondant à la commune concernée.</p>
<p>Dans chacun des cas prévus aux trois premiers alinéas, l'organe délibérant de l'établissement public de coopération intercommunale ou le conseil municipal de la commune se prononce sur son adhésion à l'établissement public foncier local dans un délai de six mois.</p>
<p>Au vu de ces délibérations, le représentant de l'État dans la région arrête le nouveau périmètre de l'établissement public foncier local. L'assemblée générale et, le cas échéant, le conseil d'administration de cet établissement restent en fonction jusqu'à la première réunion de l'assemblée générale constituée dans les conditions fixées par cet arrêté.</p>
<p>Par dérogation au cinquième alinéa de l'article L. 324-1, si l'organe délibérant de l'établissement public de coopération intercommunale ou le conseil municipal de la commune adopte une délibération défavorable, l'établissement public foncier local reste compétent uniquement sur les territoires des communes ou des établissements publics de coopération intercommunale qui en étaient membres auparavant. Cette compétence prend fin à la fin du deuxième exercice budgétaire plein suivant la délibération.</p>
''',
    "Réécriture à droit constant : chaque événement territorial est distingué de son effet sur l'adhésion et sur le périmètre transitoire. Le vote dans les six mois, l'arrêté régional, la continuité des organes et la durée de compétence après un refus sont explicités dans leurs alinéas respectifs. Aucune réforme de fond n'est appliquée à ce régime institutionnel.",
    "Six alinéas conservés. Maintien du caractère de plein droit dans les deux premiers cas et de la substitution à la commune dans le troisième, sans étendre l'adhésion au reste du territoire. Le délai de six mois est conservé sans inventer un point de départ absent du texte. Le renvoi au cinquième alinéa de L. 324-1 a été vérifié dans le corpus : il concerne le territoire d'intervention des membres. La fin du deuxième exercice budgétaire plein n'est pas remplacée par un délai de deux ans. La coquille source « cet établissement du public foncier local » est corrigée en « cet établissement public foncier local ». Coordonner le maintien des mandats avec la difficulté signalée à L. 324-3, sans modifier ce dernier renvoi ici.")

add('L324-2-1', '''
<p>Pour modifier les statuts de l'établissement public foncier local, l'assemblée générale se prononce à la majorité des deux tiers des délégués des membres de l'établissement présents ou représentés.</p>
''',
    "Réécriture à droit constant : l'organe qui décide de la modification des statuts est placé en sujet, avec la majorité requise et les délégués pris en compte. Aucune réforme de fond.",
    "La majorité reste celle des deux tiers des délégués des membres présents ou représentés ; elle n'est calculée ni sur les seuls suffrages exprimés ni sur l'ensemble des délégués en exercice. Aucun changement des règles de quorum de L. 324-7.")

add('L324-2-2', '''
<p>I. – L'établissement public foncier établit un programme pluriannuel d'intervention. Ce programme :</p>
<p>1° Définit les actions de l'établissement, leurs modalités et les moyens mis en œuvre ;</p>
<p>2° Précise les conditions de cession du foncier de nature à garantir une utilisation conforme aux missions de l'établissement.</p>
<p>II. – Le programme pluriannuel d'intervention prend en compte les priorités énoncées dans les documents d'urbanisme et les objectifs de réalisation de logements précisés par les programmes locaux de l'habitat.</p>
<p>L'établissement transmet ce programme au préfet de région.</p>
<p>Chaque année, avant le 1er juillet, l'établissement transmet un bilan annuel au comité régional de l'habitat et de l'hébergement compétent pour la région dans laquelle il exerce son activité. Ce bilan porte sur les actions de l'établissement, sur ses modalités d'intervention et sur les moyens mis en œuvre, tels que définis dans le programme pluriannuel d'intervention.</p>
''',
    "Réécriture à droit constant : le contenu du programme et ses références de planification restent distincts des deux obligations de transmission. L'établissement est expressément désigné comme auteur des transmissions, et le contenu du bilan annuel est isolé dans une seconde phrase. Aucune réforme de fond ni nouvel objectif chiffré de logement.",
    "Les I et II, les 1° et 2° et les six alinéas sont maintenus. La transmission annuelle intervient avant le 1er juillet, au comité régional de l'habitat et de l'hébergement compétent ; le programme lui-même est transmis au préfet de région. La note source prévoit, au XIII de l'article 102 de la loi n° 2017-86 du 27 janvier 2017, un décret en Conseil d'État pour l'application de la rédaction issue du XII du même article : cet encadrement réglementaire demeure à prendre en compte. Les mesures de densification de policy.json visent les règles d'urbanisme concernées et ne justifient pas de modifier ici les priorités ou les missions de l'établissement.")

add('L324-3', '''
<p>Une assemblée générale réunit les représentants de chacun des membres de l'établissement public foncier et élit parmi eux un conseil d'administration. La durée du mandat des délégués et de leurs suppléants éventuels au sein de l'établissement suit celle du mandat des organes délibérants qui les ont désignés. Par dérogation, dans les cas prévus à l'article L. 324-2-1 C, les délégués et leurs suppléants éventuels conservent leur mandat jusqu'à ce que l'organe délibérant de l'établissement public de coopération intercommunale issu de la fusion ou le conseil municipal de la commune issue de la fusion désigne ses représentants au sein de l'établissement public foncier.</p>
<p>Si tous les membres de l'établissement sont représentés au conseil d'administration, ce conseil exerce les attributions de l'assemblée générale.</p>
''',
    "Réécriture à droit constant : la représentation des membres, l'élection du conseil et la durée des mandats sont énoncées directement. Le maintien dérogatoire des mandats et le remplacement fonctionnel de l'assemblée générale par le conseil restent dans leurs alinéas d'origine. Aucune réforme de fond.",
    "Deux alinéas conservés. Le renvoi à L. 324-2-1 C demeure entier. Difficulté préexistante : cet article couvre désormais aussi l'adhésion d'une commune à un établissement public de coopération intercommunale, alors que L. 324-3 continue de désigner une personne « issue de la fusion » pour nommer les représentants ; cette discordance n'est pas résolue par une extension implicite. La note de l'article 102-XIV de la loi n° 2017-86 du 27 janvier 2017 prévoit l'application : 1° aux établissements publics de coopération intercommunale à fiscalité propre créés à compter du 1er janvier 2017 en application des I et III de l'article 35 de la loi n° 2015-991 du 7 août 2015, ou dont le périmètre a évolué à compter de cette date en application du II du même article ; 2° aux communes nouvelles créées à compter du 1er janvier 2017 en application de L. 2113-2 du code général des collectivités territoriales. Cette disposition d'application externe est conservée comme telle, sans transformer la date historique en date de réforme future ni l'étendre aux ajouts ultérieurs sans contrôle.")

add('L324-4', '''
<p>Le vote par l'assemblée générale du produit de la taxe spéciale d'équipement à percevoir dans l'année exige une majorité comprenant plus de la moitié des délégués des communes ou des établissements publics de coopération intercommunale présents ou représentés.</p>
''',
    "Réécriture à droit constant : le vote annuel est directement relié à la majorité nécessaire, en rapprochant la qualité des délégués de la condition de présence ou de représentation. Aucune réforme de fond ni modification du produit fiscal.",
    "Le seuil demeure strictement supérieur à la moitié des délégués concernés présents ou représentés. Il ne devient pas une majorité des suffrages exprimés. Le vote porte sur le produit à percevoir dans l'année, sans fixation d'un taux ou d'un montant nouveau. Articulation conservée avec le quorum de L. 324-7 et les recettes de L. 324-8.")

add('L324-5', '''
<p>Le conseil d'administration prend, par délibération, les décisions relatives aux affaires de l'établissement. Il exerce notamment les attributions suivantes :</p>
<p>1° Il fixe les orientations de la politique de l'établissement, approuve le programme pluriannuel d'intervention et ses tranches annuelles, et les révise ;</p>
<p>2° Il vote l'état prévisionnel des recettes et des dépenses et autorise les emprunts. Il approuve les comptes et se prononce sur l'affectation du résultat ;</p>
<p>3° Sur proposition du président, il nomme le directeur et met fin à ses fonctions.</p>
<p>Le conseil d'administration élit parmi ses membres un président et un ou plusieurs vice-présidents.</p>
''',
    "Réécriture à droit constant : les attributions du conseil sont exprimées par des verbes directs et les décisions budgétaires et comptables sont séparées en deux phrases. La proposition du président est explicitement commune à la nomination et à la cessation des fonctions du directeur. Aucune réforme de fond.",
    "Cinq alinéas et numérotation 1° à 3° conservés. La liste reste indicative grâce à « notamment ». Le conseil approuve et révise tant le programme pluriannuel que les tranches annuelles. L'état prévisionnel, les emprunts, les comptes et l'affectation du résultat demeurent des décisions distinctes. La nomination et la fin des fonctions restent soumises à la proposition du président, sans ajout d'un avis préfectoral propre au régime de L. 326-3.")

add('L324-6', '''
<p>Le directeur exerce les fonctions d'ordonnateur des dépenses et des recettes. Il assure la représentation de l'établissement en justice et dans tous les actes de la vie civile. Au nom de l'établissement, il conclut des contrats et signe tous les actes. Il est chargé de préparer et d'exécuter les décisions de l'assemblée générale et du conseil d'administration. Il recrute le personnel et exerce son autorité sur celui-ci. Il peut déléguer sa signature.</p>
''',
    "Réécriture à droit constant : les responsabilités du directeur sont énoncées successivement, avec une référence explicite à l'établissement pour les contrats et les actes. Les compétences et la faculté de déléguer la signature restent identiques. Aucune réforme de fond.",
    "Alinéa unique conservé. Les recettes comme les dépenses relèvent de l'ordonnateur. La préparation et l'exécution concernent les deux organes, assemblée générale et conseil d'administration. La délégation reste une délégation de signature, sans création d'une délégation de compétence ni modification de la fonction du comptable prévue à L. 324-9.")

add('L324-7', '''
<p>Le contrôle de légalité des actes et délibérations de l'établissement public s'exerce dans les conditions prévues aux articles L. 2131-1 à L. 2131-11 du code général des collectivités territoriales.</p>
<p>Pour que l'assemblée générale ou le conseil d'administration puisse délibérer valablement, la majorité des membres de l'organe concerné doit être présente ou représentée. Si ce quorum n'est pas atteint, l'organe concerné est de nouveau convoqué dans un délai de dix jours, avec le même ordre du jour. Lors de cette nouvelle réunion, il délibère valablement quel que soit le nombre de membres présents. Les membres empêchés d'assister à une séance peuvent se faire représenter dans les conditions prévues à l'article L. 2121-20 du code général des collectivités territoriales.</p>
''',
    "Réécriture à droit constant : le quorum est formulé séparément pour chacun des deux organes et la seconde convocation est reliée à son absence. Le délai, le maintien de l'ordre du jour et les règles de représentation sont exprimés sans modifier leurs effets. Aucune réforme de fond.",
    "Deux alinéas conservés. Le quorum initial tient compte des présents et des représentés. Le délai de dix jours porte sur la nouvelle convocation ; aucune nouvelle durée de réunion n'est ajoutée. La seconde réunion reste valable quel que soit le nombre de membres présents, selon la formulation source. Renvois L. 2131-1 à L. 2131-11 et L. 2121-20 maintenus. La dispense de quorum de seconde réunion n'est pas étendue au régime distinct de L. 326-6.")

add('L324-8', '''
<p>Les dispositions du chapitre Ier du titre unique du livre VI de la première partie du code général des collectivités territoriales régissent l'établissement, le vote, le règlement et l'exécution de l'état prévisionnel des recettes et des dépenses.</p>
<p>Les recettes de l'établissement public comprennent notamment :</p>
<p>1° Le produit de la taxe spéciale d'équipement prévue à l'article 1607 bis du code général des impôts ;</p>
<p>2° La contribution prévue à l'article L. 302-7 du code de la construction et de l'habitation ;</p>
<p>3° Les contributions accordées à l'établissement par l'État, les collectivités locales, les établissements publics ou toute autre personne morale publique ou privée intéressée ;</p>
<p>4° Les emprunts ;</p>
<p>5° La rémunération de ses prestations de services, ses produits financiers, les produits de la gestion des biens entrés dans son patrimoine et les produits de la vente de biens et de droits mobiliers et immobiliers ;</p>
<p>6° Le produit des dons et legs.</p>
''',
    "Réécriture à droit constant : le renvoi budgétaire est formulé comme une règle applicable aux quatre étapes de l'état prévisionnel et les catégories de recettes sont présentées en alinéas lisibles. La liste et son caractère non exhaustif sont conservés. Aucune réforme de fond ni recette nouvelle.",
    "Les six rubriques numérotées et leur ordre sont maintenus. Les renvois au code général des collectivités territoriales, à CGI 1607 bis et à CCH L. 302-7 sont conservés. Aucune suppression des obligations de logement social ni exonération de leur contribution n'est déduite de policy.json. Les ventes de biens restent une recette patrimoniale : leur mention ne les érige pas en financement durable de charges permanentes ou de baisses de prélèvements.")

add('L324-9', '''
<p>Le comptable de l'établissement public est un comptable public de l'État. Le préfet le nomme après avis conforme du directeur départemental des finances publiques.</p>
<p>L'établissement public est soumis aux articles L. 1617-2, L. 1617-3 et L. 1617-5 du code général des collectivités territoriales. Il relève également de la première partie du livre II du code des juridictions financières.</p>
''',
    "Réécriture à droit constant : la qualité du comptable est distinguée de sa nomination et le préfet est désigné comme auteur de celle-ci. Les deux séries de règles comptables et financières restent dans le second alinéa. Aucune réforme de fond.",
    "Deux alinéas conservés. L'avis du directeur départemental des finances publiques reste conforme et préalable à la nomination préfectorale. Les trois articles du code général des collectivités territoriales sont repris individuellement, sans transformer l'énumération en intervalle. Le renvoi source à la « première partie du livre II » du code des juridictions financières est conservé ; sa concordance avec la structure de ce code, non fourni dans le corpus, reste à contrôler. Rédaction coordonnée avec L. 326-7, sans confondre comptable et ordonnateur.")

add('L324-10', '''
<p>Les établissements publics fonciers locaux peuvent créer des filiales et acquérir ou céder des participations dans des sociétés, groupements ou organismes dont l'objet contribue à l'accomplissement de leurs missions. Un décret en Conseil d'État fixe les conditions de ces opérations.<br/><br/>Les délibérations de leur conseil d'administration et de leur bureau relatives à ces créations de filiales et à ces acquisitions ou cessions de participations sont soumises à une seule approbation : celle du représentant de l'État dans la région.</p>
''',
    "Réécriture à droit constant : les opérations autorisées et leur encadrement par décret sont distingués en deux phrases, puis l'autorité d'approbation est désignée directement. Le lien de l'objet des organismes avec les missions de l'établissement est conservé. Aucune réforme de fond.",
    "Le paragraphe et sa séparation interne sont conservés. Création de filiales, acquisitions et cessions de participations restent toutes visées. L'approbation exclusive du représentant de l'État dans la région porte tant sur les délibérations du conseil d'administration que sur celles du bureau ; elle n'est pas remplacée par l'approbation du préfet de département prévue dans d'autres régimes. Le décret demeure un décret en Conseil d'État.")

add('L326-1', '''
<p>Les établissements publics locaux de rénovation urbaine créés en application du présent chapitre ont un caractère industriel et commercial. Ils ont compétence pour conduire des opérations et actions de rénovation urbaine et de développement économique au sens de la loi n° 2003-710 du 1er août 2003 d'orientation et de programmation pour la ville et la rénovation urbaine. Ces opérations et actions sont conduites exclusivement pour le compte de leurs membres.</p>
<p>Ils peuvent recevoir délégation de l'instruction et du traitement des demandes d'aides à la réhabilitation de l'habitat privé dans les conditions prévues à l'article L. 321-1-3 du code de la construction et de l'habitation. Ils peuvent également recevoir délégation de la gestion comptable et financière ainsi que de l'instruction et du traitement des demandes d'aides dans les conditions prévues à l'article 10-2 de la loi n° 2003-710 du 1er août 2003 d'orientation pour la ville et la rénovation urbaine.</p>
''',
    "Réécriture à droit constant : le caractère de l'établissement, ses opérations et l'exclusivité du compte des membres sont séparés en phrases. Les deux fondements de délégation d'aides sont distingués pour ne pas confondre leurs champs. Aucune réforme de fond ni transfert nouveau de décision d'attribution des aides.",
    "Deux alinéas conservés. Les missions de rénovation urbaine et de développement économique restent cumulativement mentionnées ; le compte exclusif des membres est maintenu. Le renvoi à CCH L. 321-1-3 a été vérifié : il permet la délégation de l'instruction et du traitement des demandes, distincte de la décision d'attribution. La gestion comptable et financière demeure rattachée au renvoi séparé à l'article 10-2 de la loi de 2003. La source emploie « rénovation urbaine » dans L. 326-1 mais « aménagement » dans le titre du chapitre et L. 326-2 : cette différence préexistante est conservée. Les deux intitulés différents donnés à la même loi n° 2003-710 dans la source sont conservés ; leur harmonisation éditoriale reste à contrôler.")

add('L326-2', '''
<p>Le préfet crée l'établissement public local d'aménagement au vu des délibérations concordantes des organes délibérants des établissements publics de coopération intercommunale et des collectivités territoriales compétents. Lorsque les établissements publics de coopération intercommunale et les communes appartiennent à plusieurs départements, les préfets concernés prennent conjointement l'arrêté de création.</p>
<p>Les délibérations déterminent la liste des membres de l'établissement, ses modalités de fonctionnement, les conditions de modification de ses statuts, sa durée, ses modalités de dissolution, son siège et la composition de son conseil d'administration.</p>
<p>La décision de création comporte l'ensemble des éléments mentionnés à l'alinéa précédent.</p>
''',
    "Réécriture à droit constant : le préfet est placé en sujet de la création et la décision interdépartementale est formulée directement. Les délibérations et la décision de création restent tenues de préciser les mêmes éléments. Aucune réforme de fond.",
    "Trois alinéas conservés. Maintien des délibérations concordantes des organes compétents et de l'arrêté conjoint dans le cas de plusieurs départements. La condition interdépartementale vise toujours les établissements publics de coopération intercommunale et les communes, sans extension à d'autres membres. Les sept éléments statutaires sont tous conservés : membres, fonctionnement, modification des statuts, durée, dissolution, siège, composition du conseil.")

add('L326-3', '''
<p>Le conseil d'administration prend, par délibération, les décisions relatives aux affaires de l'établissement. À cet effet :</p>
<p>– il fixe les orientations de la politique de l'établissement ;</p>
<p>– il vote l'état prévisionnel des recettes et des dépenses et autorise les emprunts ; il approuve les comptes et se prononce sur l'affectation du résultat ;</p>
<p>– il nomme le directeur général sur proposition du président, après avoir recueilli l'avis du préfet.</p>
<p>Le conseil d'administration élit parmi ses membres un président et un ou plusieurs vice-présidents.</p>
''',
    "Réécriture à droit constant : les pouvoirs du conseil sont présentés par décisions et les étapes de nomination sont exprimées dans leur ordre. Les tirets et la place de l'élection du président et des vice-présidents sont conservés. Aucune réforme de fond.",
    "Cinq alinéas conservés, sans transformer les tirets en subdivisions numérotées. L'avis du préfet reste un avis simple ; il n'est pas rendu conforme. La proposition du président et l'avis préfectoral sont tous deux requis pour la nomination. Aucune règle de cessation des fonctions n'est importée de L. 324-5. Difficulté terminologique préexistante : le « directeur général » de cet article est nommé « directeur » à L. 326-5 ; les deux désignations sont maintenues dans leurs articles respectifs.")

add('L326-4', '''
<p>Les dispositions du chapitre Ier du titre unique du livre VI de la première partie du code général des collectivités territoriales régissent l'établissement, le vote, le règlement et l'exécution de l'état prévisionnel des recettes et des dépenses.</p>
<p>Les recettes de l'établissement public comprennent :</p>
<p>– les contributions accordées à l'établissement par l'État, les collectivités territoriales, les établissements publics ou toute autre personne morale publique ou privée intéressée ;</p>
<p>– les emprunts ;</p>
<p>– la rémunération de ses prestations de services, ses produits financiers, les produits de la gestion des biens entrés dans son patrimoine et les produits de la vente de biens et de droits mobiliers et immobiliers ;</p>
<p>– le produit des dons et legs.</p>
''',
    "Réécriture à droit constant : les quatre étapes budgétaires sont rattachées directement aux règles applicables et les ressources sont présentées dans leurs rubriques distinctes. Les catégories de contributeurs et tous les produits patrimoniaux restent énumérés. Aucune réforme de fond.",
    "Les quatre tirets et leur ordre sont conservés. Le mot « notamment », présent au régime distinct de L. 324-8, n'est pas ajouté ici. Aucune taxe spéciale d'équipement ni contribution de CCH L. 302-7 n'est importée de cet autre régime. Le renvoi budgétaire conserve le chapitre Ier, le titre unique, le livre VI et la première partie du code général des collectivités territoriales. Aucun produit de cession n'est présenté comme une économie récurrente finançant la réforme.")

add('L326-5', '''
<p>Le directeur exerce les fonctions d'ordonnateur des dépenses et des recettes. Il assure la représentation de l'établissement en justice et dans tous les actes de la vie civile. Au nom de l'établissement, il conclut des contrats et signe tous les actes. Il est chargé de préparer et d'exécuter les décisions du conseil d'administration. Il recrute le personnel et exerce son autorité sur celui-ci. Il peut déléguer sa signature.</p>
''',
    "Réécriture à droit constant : les fonctions financières, la représentation, les actes, l'exécution des décisions et l'autorité sur le personnel sont exprimées successivement. Le pouvoir de délégation de signature est conservé. Aucune réforme de fond.",
    "Alinéa unique conservé. Seules les décisions du conseil d'administration sont visées, sans ajouter l'assemblée générale du régime distinct de L. 324-6. La délégation de signature ne devient pas une délégation de compétence. La dénomination « directeur » est maintenue malgré la référence au « directeur général » dans L. 326-3 ; une harmonisation éventuelle exige un contrôle explicite, sans modification silencieuse du titulaire des pouvoirs.")

add('L326-6', '''
<p>Le contrôle de légalité des actes et délibérations de l'établissement public s'exerce dans les conditions prévues aux articles L. 2131-1 à L. 2131-11 du code général des collectivités territoriales.</p>
<p>Pour délibérer valablement, le conseil d'administration doit réunir la majorité de ses membres, présents ou représentés. Les membres empêchés d'assister à une séance peuvent se faire représenter dans les conditions prévues à l'article L. 2121-20 du même code.</p>
''',
    "Réécriture à droit constant : la soumission au contrôle de légalité et la condition de quorum sont formulées directement. La représentation des membres empêchés conserve son fondement propre. Aucune réforme de fond.",
    "Deux alinéas conservés. La majorité des membres doit être présente ou représentée. Les renvois L. 2131-1 à L. 2131-11 et L. 2121-20 sont maintenus. Aucune seconde convocation sans quorum ni délai de dix jours n'est ajouté : cette exception relève de L. 324-7 et ne figure pas dans le présent régime.")

add('L326-7', '''
<p>Le comptable de l'établissement public est un comptable public de l'État. Le préfet le nomme après avis conforme du directeur départemental des finances publiques.</p>
<p>L'établissement public est soumis aux articles L. 1617-2, L. 1617-3 et L. 1617-5 du code général des collectivités territoriales. Il relève également de la première partie du livre II du code des juridictions financières.</p>
''',
    "Réécriture à droit constant : la qualité du comptable et les conditions de sa nomination sont distinguées en deux phrases, avec le préfet comme auteur de la décision. L'application des règles comptables et du contrôle financier reste distincte. Aucune réforme de fond.",
    "Deux alinéas conservés. L'avis préalable du directeur départemental des finances publiques demeure conforme. Les renvois L. 1617-2, L. 1617-3 et L. 1617-5 restent une énumération, sans inclusion de L. 1617-4. Comme à L. 324-9, le renvoi source à la « première partie du livre II » du code des juridictions financières est conservé ; sa concordance avec la structure de ce code non fourni dans le corpus reste à contrôler. Aucune confusion avec les fonctions d'ordonnateur de L. 326-5.")

add('L327-1', '''
<p>Les sociétés publiques locales d'aménagement et les sociétés publiques locales d'aménagement d'intérêt national sont des sociétés anonymes auxquelles s'applique le livre II du code de commerce.</p>
<p>Sous réserve des dispositions du présent chapitre, elles relèvent également du titre II du livre V de la première partie du code général des collectivités territoriales.</p>
<p>Elles exercent leurs activités uniquement pour le compte de leurs actionnaires et sur le territoire des collectivités territoriales et des groupements de collectivités territoriales qui en sont membres. La réalisation de leur objet contribue à l'exercice d'au moins une compétence de chaque collectivité territoriale et de chaque groupement de collectivités territoriales actionnaire.</p>
<p>Une société publique locale d'aménagement peut aussi exercer ses activités pour le compte d'une société publique locale d'aménagement d'intérêt national si l'un au moins de ses membres exerce sur cette dernière un contrôle analogue à celui qu'il exerce sur ses propres services.</p>
<p>Outre les opérations prévues au dernier alinéa de l'article L. 327-2 ou aux 1° à 3° de l'article L. 327-3 du présent code, ces deux catégories de sociétés sont compétentes pour réaliser les opérations de requalification de copropriétés dégradées prévues à l'article L. 741-1 du code de la construction et de l'habitation. Elles sont également compétentes pour réaliser des études préalables et procéder à toute acquisition et cession d'immeubles en application des articles L. 221-1 et L. 221-2 du présent code. Elles peuvent procéder à toute opération de construction ou de réhabilitation immobilière en vue de la réalisation des objectifs énoncés à l'article L. 300-1. Elles peuvent aussi procéder à toute acquisition et cession de baux commerciaux, de fonds de commerce ou de fonds artisanaux dans les conditions prévues au chapitre IV du titre Ier du livre II. Elles peuvent exercer, par délégation de leurs titulaires, les droits de préemption et de priorité définis par le présent code et agir par voie d'expropriation dans les conditions fixées par des conventions conclues avec l'un de leurs membres.</p>
''',
    "Réécriture à droit constant : les règles communes sont formulées directement et la longue énumération des compétences est répartie en phrases dans son alinéa d'origine. L'activité pour le compte d'une société d'intérêt national reste une faculté propre aux sociétés locales, soumise au contrôle analogue. Aucune réforme de fond.",
    "Cinq alinéas conservés, notamment le dernier auquel ne sont pas substituées de nouvelles subdivisions. Maintien de l'exclusivité pour les actionnaires, du territoire des membres et de l'exigence d'au moins une compétence pour chacun des actionnaires territoriaux. La faculté du quatrième alinéa ne devient ni réciproque ni ouverte sans contrôle analogue. Les renvois au dernier alinéa de L. 327-2 et aux 1° à 3° de L. 327-3 sont vérifiés dans le lot ; les compétences correspondantes ne sont pas déplacées. Toutes les opérations supplémentaires, les deux droits délégués et l'expropriation conventionnelle restent mentionnés. Les mesures de transformation de bureaux ne créent ici aucune dispense des autorisations ou protections applicables.")

add('L327-2', '''
<p>Dans le cadre des compétences que la loi leur attribue, les collectivités territoriales et leurs groupements peuvent constituer des sociétés publiques locales d'aménagement. Ils en détiennent la totalité du capital.</p>
<p>La majorité au moins des droits de vote doit appartenir à l'une des collectivités territoriales ou à l'un des groupements de collectivités territoriales participant à la société.</p>
<p>Les sociétés publiques locales d'aménagement ont compétence pour réaliser toute opération ou toute action d'aménagement au sens du présent code.</p>
''',
    "Réécriture à droit constant : la création dans le champ des compétences légales et la détention intégralement publique du capital sont distinguées en deux phrases. Le détenteur de la majorité des voix est identifié directement. Aucune réforme de fond.",
    "Trois alinéas conservés. Le capital reste intégralement détenu par les collectivités territoriales et leurs groupements. La majorité des droits de vote doit être détenue par un participant déterminé ; elle n'est pas remplacée par la seule majorité collective des actionnaires publics. Le dernier alinéa, visé par L. 327-1, demeure en troisième position et vise tant les opérations que les actions d'aménagement. Le seuil de 35 % de L. 327-3 n'est pas importé dans ce régime distinct.")

add('L327-3', '''
<p>L'État ou l'un de ses établissements publics mentionnés au chapitre Ier du présent titre ou à l'article L. 5312-1 du code des transports peut constituer une société publique locale d'aménagement d'intérêt national avec au moins une collectivité territoriale ou un groupement de collectivités territoriales. Ces participants en détiennent la totalité du capital.</p>
<p>Pour les établissements publics mentionnés au premier alinéa du présent article, la création d'une telle société ainsi que l'acquisition ou la cession de participations dans celle-ci s'effectuent dans les conditions prévues aux articles L. 321-3, L. 321-16 ou L. 321-30 du présent code ou à l'article L. 5312-3 du code des transports.</p>
<p>L'une des collectivités territoriales ou l'un des groupements de collectivités territoriales participant à la société doit détenir au moins 35 % de son capital et de ses droits de vote.</p>
<p>La société peut organiser, réaliser ou contrôler :</p>
<p>1° Toute action ou opération d'aménagement au sens du présent code qui relève de la compétence de l'État ou de l'un de ses établissements publics mentionnés au premier alinéa du présent article, ou de celle d'une collectivité territoriale ou d'un groupement de collectivités territoriales actionnaire ;</p>
<p>2° Toute action ou opération de construction ou de réhabilitation d'équipements d'intérêt collectif et de services publics relevant de la compétence d'une collectivité territoriale ou d'un groupement de collectivités territoriales actionnaire, ainsi que la maintenance et l'entretien de ces équipements ;</p>
<p>3° Toute intervention foncière ou immobilière qui relève de la compétence de l'État ou de l'un de ses établissements publics mentionnés au premier alinéa du présent article, ou de celle d'une collectivité territoriale ou d'un groupement de collectivités territoriales actionnaire.</p>
<p>L'article L. 1541-3 du code général des collectivités territoriales s'applique aux collectivités territoriales actionnaires de la société publique locale d'aménagement d'intérêt national ou au groupement de collectivités territoriales compétent qui en est actionnaire.</p>
''',
    "Réécriture à droit constant : les conditions de constitution sont distinguées de la détention du capital et le régime des participations des établissements publics est formulé directement. Les trois compétences restent énumérées séparément avec leurs titulaires et leurs champs respectifs. Aucune réforme de fond.",
    "Huit alinéas, les 1° à 3° et les renvois au premier alinéa sont conservés. Un participant territorial doit détenir au moins 35 % à la fois du capital et des droits de vote ; aucune majorité nouvelle n'est exigée. Les établissements des transports restent mentionnés aux côtés de ceux du chapitre Ier. Les renvois L. 321-3, L. 321-16 et L. 321-30 ont été vérifiés dans le corpus pour les filiales et participations ; L. 5312-1 et L. 5312-3 du code des transports sont maintenus sans substitution hors corpus. Le 2° reste limité aux compétences des actionnaires territoriaux et conserve la maintenance et l'entretien des équipements ; les 1° et 3° couvrent aussi l'État et ses établissements visés. La formulation source du dernier alinéa, visant les collectivités ou le groupement compétent actionnaires, et le renvoi à CGCT L. 1541-3 sont maintenus sans élargissement implicite.")

add('L328-1', '''
<p>L'établissement public local « Paris La Défense » a un caractère industriel et commercial.</p>
''',
    "Réécriture à droit constant, limitée à la formulation de cette disposition très courte : la dénomination de l'établissement est intégrée au sujet et son caractère industriel et commercial est énoncé directement. Aucune réforme de fond.",
    "Alinéa unique conservé. La dénomination « Paris La Défense », le statut d'établissement public local et le caractère industriel et commercial sont tous maintenus. Aucun nouveau statut, périmètre ou pouvoir n'est ajouté.")

add('L328-2', '''
<p>Paris La Défense a pour mission principale de conduire toute action destinée à favoriser l'aménagement, le renouvellement et le développement urbains et durables dans un périmètre couvrant une partie des communes de La Garenne-Colombes et de Nanterre. Ce périmètre est compris dans le territoire couvert par l'opération d'intérêt national mentionnée au 6° de l'article R. 102-3. Il est délimité par décret en Conseil d'État, pris après concertation avec ces communes et le département des Hauts-de-Seine et après avis de ceux-ci.</p>
<p>À cet effet, Paris La Défense a compétence pour y réaliser :</p>
<p>1° Toutes les opérations foncières ou immobilières nécessaires à ses opérations ;</p>
<p>2° Toutes les actions ou opérations d'aménagement au sens du présent code, pour son compte ou pour celui de collectivités territoriales, d'établissements publics ou de personnes publiques ou privées ;</p>
<p>3° Tous les ouvrages de bâtiment ou d'infrastructure, en qualité de mandataire au sens de l'article 3 de la loi du 12 juillet 1985 relative à la maîtrise d'ouvrage publique et ses rapports avec la maîtrise d'œuvre privée.</p>
<p>À titre accessoire et sous réserve des compétences dévolues à d'autres personnes publiques, Paris La Défense peut accomplir des missions présentant un caractère complémentaire et un intérêt directement utile à sa mission principale d'aménagement, de renouvellement et de développement urbains, en vue de favoriser le développement durable du territoire mentionné au premier alinéa. Il les accomplit pour son compte ou, dans le cadre d'une convention passée avec l'État, des collectivités territoriales ou leurs groupements, pour le compte de ceux-ci.</p>
''',
    "Réécriture à droit constant : le périmètre et sa délimitation sont séparés de l'objet de la mission dans le premier alinéa. Le bénéficiaire et l'exigence de convention des missions accessoires sont explicités sans changer leur caractère complémentaire ni leur utilité directe. Aucune réforme de fond.",
    "Six alinéas et les 1° à 3° conservés. Le 6° de R. 102-3 a été vérifié dans le corpus : il concerne Nanterre et La Garenne-Colombes, à distinguer du 2° utilisé à L. 328-3. Ni l'ensemble des deux communes ni tout le territoire de l'opération d'intérêt national ne deviennent automatiquement le périmètre d'intervention. Concertation et avis des communes et du département sont tous deux maintenus avant le décret en Conseil d'État. Le renvoi ancien à l'article 3 de la loi du 12 juillet 1985 est conservé et doit faire l'objet d'un contrôle de concordance avec le mandat de maîtrise d'ouvrage publique dans le code de la commande publique, deuxième partie, livre IV, titre II, chapitre II, hors du corpus fourni ; aucun article de remplacement non vérifié n'est inventé. Les missions accessoires pour autrui restent conventionnelles et soumises aux compétences des autres personnes publiques.")

add('L328-3', '''
<p>Paris La Défense exerce à titre exclusif la mission prévue à l'article L. 328-2 sur un périmètre couvrant une partie des communes de Courbevoie et de Puteaux. Ce périmètre est compris dans le territoire couvert par l'opération d'intérêt national mentionnée au 2° de l'article R. 102-3. Il est délimité par décret en Conseil d'État, pris après concertation avec ces communes et le département des Hauts-de-Seine et après avis de ceux-ci. Dans ce même périmètre, Paris La Défense assure également, à titre exclusif, la gestion des ouvrages et espaces publics ainsi que des services d'intérêt général.</p>
<p>Cette mission de gestion comprend :<br/><br/>1° L'exploitation, l'entretien et la maintenance des ouvrages et espaces publics et des services d'intérêt général, y compris leur remise en état ou leur renouvellement ;<br/><br/>2° L'animation et la promotion du site dont le périmètre est mentionné au premier alinéa du présent article, en vue notamment de favoriser son rayonnement international auprès des acteurs économiques ;<br/><br/>3° La préservation de la sécurité des personnes et des biens. Pour assurer cette sécurité, Paris La Défense peut acquérir, installer et entretenir des dispositifs de vidéoprotection dans les conditions fixées au chapitre III du titre II et au titre V du livre II du code de la sécurité intérieure.</p>
<p>Paris La Défense peut gérer les ouvrages, espaces publics et services d'intérêt général mentionnés au premier alinéa lorsqu'ils lui appartiennent. Lorsqu'ils appartiennent à l'État ou aux collectivités territoriales et à leurs groupements mentionnés au premier alinéa du I de l'article L. 328-8 du présent code, il peut les gérer dans le cadre de conventions conclues avec ces propriétaires.</p>
<p>Les ouvrages, espaces publics et services d'intérêt général confiés à Paris La Défense par l'État ou par les collectivités territoriales et leurs groupements sont mis à sa disposition. À leur égard, Paris La Défense assume l'ensemble des obligations du propriétaire et dispose des pouvoirs de gestion définis aux articles L. 1321-2 et L. 1321-3 du code général des collectivités territoriales.</p>
<p>À titre accessoire et sous réserve des compétences dévolues à d'autres personnes publiques, Paris La Défense peut accomplir des missions présentant un caractère complémentaire et un intérêt directement utile à sa mission de gestion. Il les accomplit pour son compte ou, dans le cadre d'une convention passée avec l'État, des collectivités territoriales ou leurs groupements, pour le compte de ceux-ci.</p>
''',
    "Réécriture à droit constant : la mission exclusive, le périmètre et le décret de délimitation sont exprimés dans des phrases distinctes. La gestion des biens propres est séparée de celle des biens confiés par convention, sans modifier leur mise à disposition. Les missions accessoires gardent leurs conditions. Aucune réforme de fond.",
    "Les cinq paragraphes de la source et les 1° à 3° internes au deuxième sont conservés pour ne pas déplacer les alinéas suivants. Le 2° de R. 102-3 a été vérifié : il vise le quartier d'affaires de La Défense ; il n'est pas confondu avec le 6° de L. 328-2. Les deux exclusivités, l'avis et la concertation, les trois catégories de gestion, la remise en état et le renouvellement sont conservés. La vidéoprotection reste soumise aux deux ensembles de dispositions du code de la sécurité intérieure, sans création d'un pouvoir général de police. Le premier alinéa du I de L. 328-8 a été vérifié pour les personnes publiques visées, sans importer les personnalités qualifiées ou représentants du personnel des alinéas suivants. La mise à disposition ne devient pas un transfert de propriété ; l'ensemble des obligations du propriétaire et les deux renvois de gestion L. 1321-2 et L. 1321-3 demeurent. Les missions accessoires ne reçoivent pas l'exclusivité des missions principales.")


assert len(sources) == 24
assert len(drafts) == 24
assert set(drafts) == {a['number'] for a in sources}
result = []
for source in sources:
    xml, reason, review = drafts[source['number']]
    entry = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    entry.update(proposed_xml=xml, reason=reason, review_notes=review, status='rewrite_draft')
    result.append(entry)
Path('answer.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(result)} articles')
