import json
from pathlib import Path


drafts = {}


def add(number, paragraphs, reason, review_notes):
    drafts[number] = {
        "proposed_xml": "".join(f"<p>{p}</p>" for p in paragraphs),
        "reason": reason,
        "review_notes": review_notes,
    }


add(
    "L2142-1-1",
    [
        "Dans une entreprise ou un établissement d'au moins cinquante salariés, un syndicat qui constitue une section syndicale conformément à l'article L. 2142-1 peut désigner un représentant de cette section s'il n'est pas représentatif dans cette entreprise ou cet établissement. Ce représentant y représente le syndicat.",
        "Le représentant de la section syndicale exerce ses fonctions conformément aux dispositions du présent chapitre. Il dispose des mêmes prérogatives que le délégué syndical, sauf du pouvoir de négocier des accords collectifs.",
        "À l'issue des premières élections professionnelles suivant sa désignation, le mandat du représentant de la section syndicale prend fin si le syndicat qui l'a désigné n'est pas reconnu représentatif dans l'entreprise. Le salarié qui perd ainsi son mandat ne peut de nouveau être désigné représentant syndical au titre d'une section avant le début de la période de six mois qui précède la date des élections professionnelles suivantes dans l'entreprise.",
    ],
    "Réécriture à droit constant : le seuil d'effectif et les conditions de désignation sont regroupés en tête du premier alinéa ; la mission du représentant est isolée dans une phrase. La fin du mandat et la période interdisant une nouvelle désignation sont formulées dans l'ordre chronologique. Aucune réforme de fond n'est appliquée.",
    "Trois alinéas conservés. Maintien du seuil de cinquante salariés, du renvoi à L. 2142-1, de l'exclusion du pouvoir de négocier des accords collectifs et du délai de six mois avant les élections suivantes. La source vise l'entreprise ou l'établissement pour la désignation, mais seulement l'entreprise pour la représentativité à l'issue des élections et la nouvelle désignation : cette différence de périmètre est conservée et appelle un contrôle de coordination, sans harmonisation implicite.",
)

add(
    "L2142-1-2",
    [
        "Les règles suivantes s'appliquent au représentant de la section syndicale : les dispositions des articles L. 2143-1 et L. 2143-2 relatives aux conditions de désignation du délégué syndical ; les dispositions des articles L. 2143-7 à L. 2143-10 et des deuxième et troisième alinéas de l'article L. 2143-11 relatives à la publicité, à la contestation, à l'exercice et à la suppression de son mandat ; les dispositions du livre IV de la présente partie relatives à la protection des délégués syndicaux.",
    ],
    "Réécriture à droit constant : le représentant auquel les règles s'appliquent est nommé au début de l'alinéa et les trois groupes de dispositions sont séparés par des points-virgules. Aucune réforme de fond n'est appliquée.",
    "Alinéa unique conservé. Renvois maintenus à L. 2143-1, L. 2143-2, L. 2143-7 à L. 2143-10, aux seuls deuxième et troisième alinéas de L. 2143-11 et au livre IV de la deuxième partie. Vérification locale de L. 2143-11 : les deuxième et troisième alinéas concernent bien la suppression du mandat en cas de baisse d'effectif ; le premier alinéa n'est pas rendu applicable par ce renvoi.",
)

add(
    "L2142-1-3",
    [
        "Chaque représentant de la section syndicale dispose du temps nécessaire à l'exercice de ses fonctions, avec un minimum de quatre heures par mois. Les heures de délégation constituent de plein droit du temps de travail et sont payées à l'échéance normale.",
        "Pour contester l'utilisation des heures de délégation, l'employeur saisit le juge judiciaire.",
        "Sauf accord collectif contraire, lorsque le représentant du personnel élu ou désigné est un salarié mentionné à l'article L. 3121-58, son crédit d'heures est regroupé en demi-journées. Ces demi-journées sont déduites du nombre annuel de jours travaillés fixé par sa convention individuelle. Une demi-journée correspond à quatre heures de mandat. Si le crédit d'heures ou la fraction de crédit restant est inférieur à quatre heures, le représentant du personnel en bénéficie dans les conditions définies par un décret en Conseil d'État.",
    ],
    "Réécriture à droit constant : le temps nécessaire et son minimum sont énoncés ensemble ; la règle de conversion en demi-journées est séparée de son imputation sur le forfait annuel, au sein du même alinéa. Aucune réforme de fond n'est appliquée.",
    "Trois alinéas conservés. Maintien du minimum de quatre heures par mois, du paiement à l'échéance normale, de la saisine du juge judiciaire, de la réserve d'accord collectif contraire, de l'équivalence d'une demi-journée pour quatre heures et du traitement réglementaire du reliquat inférieur à quatre heures. L. 3121-58 a été vérifié dans le corpus local ; le régime des forfaits en jours n'est pas modifié par les orientations relatives au seuil hebdomadaire des heures supplémentaires. Le troisième alinéa conserve la désignation générale du représentant du personnel élu ou désigné employée par la source.",
)

add(
    "L2142-1-4",
    [
        "Dans les entreprises de moins de cinquante salariés, un syndicat non représentatif dans l'entreprise qui constitue une section syndicale peut désigner un membre de la délégation du personnel au comité social et économique comme représentant de cette section, pour la durée du mandat de ce membre. Une disposition conventionnelle peut accorder un crédit d'heures au titre du mandat de représentant de la section syndicale. Le membre de la délégation du personnel au comité social et économique peut utiliser, dans les mêmes conditions, le temps dont il dispose au titre de son mandat pour exercer ses fonctions de représentant de la section syndicale.",
    ],
    "Réécriture à droit constant : la durée de la désignation est rattachée explicitement au mandat du membre du comité social et économique ; la possibilité conventionnelle d'un crédit d'heures est distinguée de l'utilisation du temps de son mandat existant. Aucune réforme de fond n'est appliquée.",
    "Alinéa unique conservé, hors sauts de ligne de présentation. Maintien du champ des entreprises de moins de cinquante salariés, de la non-représentativité dans l'entreprise, de la constitution d'une section et de la qualité de membre de la délégation du personnel. Aucun crédit d'heures légal autonome n'est créé ; articulation conservée avec L. 2142-1-3 et, pour le régime distinct des syndicats représentatifs, avec L. 2143-6.",
)

add(
    "L2142-2",
    ["Les cotisations syndicales peuvent être collectées à l'intérieur de l'entreprise."],
    "Réécriture à droit constant : la locution « peut être réalisée » est remplacée par le verbe « collecter », en plaçant les cotisations en sujet. La faculté et son champ sont conservés ; aucune réforme de fond n'est appliquée.",
    "Disposition unique conservée et présentée dans un paragraphe. Aucune restriction de lieu supplémentaire ni condition d'autorisation de l'employeur n'est ajoutée.",
)

add(
    "L2142-3",
    [
        "Les communications syndicales peuvent être affichées librement sur les panneaux réservés à cet usage. Ces panneaux sont distincts de ceux destinés aux communications du comité social et économique.",
        "Un exemplaire de chaque communication syndicale est transmis à l'employeur au moment de son affichage.",
        "Un accord avec l'employeur fixe les modalités de mise à disposition des panneaux pour chaque section syndicale.",
    ],
    "Réécriture à droit constant : la liberté d'affichage et la séparation des panneaux sont énoncées dans deux phrases du premier alinéa ; le dernier alinéa donne directement à l'accord sa fonction de fixation des modalités. Aucune réforme de fond n'est appliquée.",
    "Trois alinéas conservés. Maintien des panneaux réservés, de leur distinction avec ceux du comité social et économique, de la transmission simultanée à l'employeur et de l'accord fixant les modalités pour chaque section. La transmission ne devient pas une autorisation préalable.",
)

add(
    "L2142-4",
    ["La diffusion des publications et tracts de nature syndicale aux travailleurs de l'entreprise est libre dans l'enceinte de l'entreprise, aux heures d'entrée et de sortie du travail."],
    "Réécriture à droit constant : la liberté de diffusion est énoncée comme règle principale, puis ses destinataires, son lieu et ses horaires sont précisés dans la même phrase. Aucune réforme de fond n'est appliquée.",
    "Disposition unique conservée. Le terme « travailleurs », le caractère syndical des documents, l'enceinte de l'entreprise et les heures d'entrée et de sortie sont maintenus. La règle n'est pas étendue à tout moment de la journée.",
)

add(
    "L2142-5",
    ["L'organisation syndicale détermine librement le contenu des affiches, publications et tracts, sous réserve de l'application des dispositions relatives à la presse."],
    "Réécriture à droit constant : l'organisation syndicale devient le sujet du verbe afin d'identifier directement le titulaire de la liberté de contenu. Aucune réforme de fond n'est appliquée.",
    "Disposition unique conservée. Les trois supports et la réserve relative aux dispositions sur la presse sont intégralement maintenus.",
)

add(
    "L2142-6",
    [
        "Un accord d'entreprise peut fixer les conditions et les modalités de diffusion des informations syndicales par les outils numériques disponibles dans l'entreprise.",
        "En l'absence d'accord, les organisations syndicales présentes dans l'entreprise peuvent mettre à disposition des publications et des tracts sur un site syndical accessible depuis l'intranet de l'entreprise, s'il existe. Elles doivent satisfaire aux critères de respect des valeurs républicaines et d'indépendance et être légalement constituées depuis au moins deux ans.",
        "Lorsqu'elles utilisent les outils numériques mis à leur disposition, les organisations syndicales doivent respecter toutes les conditions suivantes :",
        "1° Cette utilisation doit être compatible avec les exigences de bon fonctionnement et de sécurité du réseau informatique de l'entreprise ;",
        "2° Elle ne doit pas avoir de conséquences préjudiciables à la bonne marche de l'entreprise ;",
        "3° Elle doit préserver la liberté des salariés d'accepter ou de refuser un message.",
    ],
    "Réécriture à droit constant : le régime applicable sans accord est réparti entre la faculté de diffusion et les critères cumulatifs d'éligibilité, dans le même alinéa. Chacune des trois conditions d'utilisation est formulée comme une obligation explicite. Aucune réforme de fond n'est appliquée.",
    "Six alinéas et numérotation 1° à 3° conservés, hors sauts de ligne de présentation. Maintien de la priorité de l'accord d'entreprise, de l'existence éventuelle de l'intranet, de la présence dans l'entreprise, des valeurs républicaines, de l'indépendance et des deux ans de constitution légale. Les trois conditions techniques, de fonctionnement et de liberté de réception restent cumulatives ; aucune faculté générale d'envoi direct de courriels n'est ajoutée.",
)

add(
    "L2142-7",
    ["Dans les entreprises de travail temporaire, les communications syndicales figurant sur le panneau d'affichage doivent être remises aux salariés temporaires en mission ou leur être adressées par voie postale, au moins une fois par mois. Les frais sont à la charge de l'entrepreneur de travail temporaire."],
    "Réécriture à droit constant : l'obligation de remise ou d'envoi et sa périodicité sont énoncées dans une première phrase ; la prise en charge des frais est isolée dans une seconde, au sein du même alinéa. Aucune réforme de fond n'est appliquée.",
    "Alinéa unique conservé. Maintien des seuls salariés temporaires en mission, des communications portées sur le panneau, de la fréquence minimale mensuelle, de la remise ou de l'envoi postal et des frais à la charge de l'entrepreneur de travail temporaire. Aucun mode numérique de substitution n'est introduit.",
)

add(
    "L2142-8",
    [
        "Dans une entreprise ou un établissement d'au moins deux cents salariés, l'employeur doit fournir aux sections syndicales un local commun adapté à l'exercice de la mission de leurs délégués.",
        "Dans une entreprise ou un établissement d'au moins mille salariés, l'employeur doit également fournir à chaque section syndicale constituée par une organisation syndicale représentative dans l'entreprise ou l'établissement un local convenable, aménagé et équipé du matériel nécessaire à son fonctionnement.",
    ],
    "Réécriture à droit constant : l'obligation de l'employeur est explicite dans chacun des deux alinéas ; le caractère supplémentaire des locaux à partir de mille salariés est maintenu. Aucune réforme de fond n'est appliquée.",
    "Deux alinéas conservés. Seuils inclusifs de deux cents et de mille salariés maintenus, dans l'entreprise ou l'établissement. Le local commun reste destiné aux sections syndicales ; le local supplémentaire est propre à chaque section constituée par une organisation représentative dans le périmètre concerné. Aménagement et matériel conservés.",
)

add(
    "L2142-9",
    ["Un accord avec l'employeur fixe les modalités d'aménagement des locaux mis à la disposition des sections syndicales et les modalités de leur utilisation par ces sections."],
    "Réécriture à droit constant : l'accord est placé en sujet et les deux objets de cet accord, aménagement et utilisation, sont explicités. Aucune réforme de fond n'est appliquée.",
    "Disposition unique conservée. L'accord reste conclu avec l'employeur et porte sur les locaux mis à la disposition des sections syndicales, en articulation avec L. 2142-8.",
)

add(
    "L2142-10",
    [
        "Les adhérents de chaque section syndicale peuvent tenir une réunion par mois dans l'enceinte de l'entreprise, en dehors des locaux de travail. Un accord avec l'employeur en fixe les modalités.",
        "Les sections syndicales peuvent inviter des personnalités syndicales extérieures à l'entreprise à leurs réunions dans les locaux syndicaux mis à leur disposition en application de l'article L. 2142-8. Elles peuvent aussi les inviter à leurs réunions dans d'autres locaux mis à leur disposition, avec l'accord du chef d'entreprise.",
        "Les sections syndicales peuvent inviter à une réunion des personnalités extérieures autres que syndicales, avec l'accord de l'employeur.",
    ],
    "Réécriture à droit constant : chaque alinéa distingue la catégorie de participants et les conditions applicables ; les deux lieux possibles pour l'accueil de personnalités syndicales sont présentés dans des phrases séparées du deuxième alinéa. Aucune réforme de fond n'est appliquée.",
    "Trois alinéas substantiels conservés à partir des séparations par br de la source. Maintien de la réunion mensuelle, de l'enceinte de l'entreprise hors locaux de travail et de l'accord sur les modalités. Renvoi à L. 2142-8 maintenu. L'accord du chef d'entreprise reste nécessaire pour les autres locaux accueillant des personnalités syndicales ; l'accord de l'employeur reste requis pour les personnalités extérieures non syndicales.",
)

add(
    "L2142-11",
    ["Les participants aux réunions syndicales y assistent en dehors de leur temps de travail. Toutefois, les représentants du personnel peuvent participer à ces réunions sur leur temps de délégation."],
    "Réécriture à droit constant : le principe relatif au temps de participation et l'exception réservée aux représentants du personnel sont séparés en deux phrases dans le même alinéa. Aucune réforme de fond n'est appliquée.",
    "Alinéa unique conservé. L'exception porte exclusivement sur le temps de délégation des représentants du personnel ; aucun droit général de réunion pendant le temps de travail n'est créé.",
)

add(
    "L2143-1",
    [
        "Pour être délégué syndical, le salarié doit avoir dix-huit ans révolus, travailler dans l'entreprise depuis au moins un an et n'avoir fait l'objet d'aucune interdiction, déchéance ou incapacité relative à ses droits civiques.",
        "En cas de création d'entreprise ou d'ouverture d'établissement, l'ancienneté requise dans l'entreprise est réduite à quatre mois.",
    ],
    "Réécriture à droit constant : les conditions sont présentées comme des exigences cumulatives pour accéder à la fonction ; le second alinéa désigne explicitement l'ancienneté à laquelle s'applique la réduction. Aucune réforme de fond n'est appliquée.",
    "Deux alinéas substantiels conservés. Maintien des dix-huit ans révolus, d'un an de travail dans l'entreprise, des trois catégories d'atteintes aux droits civiques et de la réduction à quatre mois dans les deux cas prévus. Application au représentant de la section syndicale par L. 2142-1-2 conservée ; régime particulier du travail temporaire traité à L. 2143-2.",
)

add(
    "L2143-2",
    ["Dans les entreprises de travail temporaire, les salariés temporaires doivent justifier de six mois d'ancienneté pour être désignés délégués syndicaux. Cette ancienneté est calculée en additionnant les périodes pendant lesquelles ils ont été liés à ces entreprises par des contrats de mission au cours des dix-huit mois précédant la désignation. En cas de création d'entreprise ou d'ouverture d'établissement, cette période de référence est réduite à six mois."],
    "Réécriture à droit constant : la durée d'ancienneté exigée est distinguée de la période sur laquelle les contrats de mission sont totalisés ; la dernière phrase rattache expressément la réduction à cette période de référence. Aucune réforme de fond n'est appliquée.",
    "Alinéa unique conservé. Maintien des six mois d'ancienneté, de la totalisation des contrats de mission, de la référence aux dix-huit mois précédant la désignation et de sa réduction à six mois en cas de création d'entreprise ou d'ouverture d'établissement. La source emploie « Ce délai » à la fin : la proposition explicite son rattachement aux dix-huit mois de la phrase précédente, sans réduire l'ancienneté de six mois ; ce rattachement est un point à contrôler. Application au représentant de la section syndicale par L. 2142-1-2 conservée.",
)

add(
    "L2143-3",
    [
        "Dans une entreprise ou un établissement d'au moins cinquante salariés, chaque organisation syndicale qui y est représentative et qui constitue une section syndicale désigne un ou plusieurs délégués syndicaux pour la représenter auprès de l'employeur, dans les limites fixées à l'article L. 2143-12. Elle les choisit parmi les candidats aux élections professionnelles ayant recueilli, à titre personnel et dans leur collège, au moins 10 % des suffrages exprimés au premier tour des dernières élections au comité social et économique, quel que soit le nombre de votants.",
        "Une organisation syndicale représentative peut désigner un délégué syndical parmi les autres candidats ou, à défaut, parmi ses adhérents au sein de l'entreprise ou de l'établissement ou parmi ses anciens élus dans l'un des cas suivants : aucun des candidats qu'elle a présentés aux élections professionnelles ne remplit les conditions du premier alinéa du présent article ; il ne reste, dans l'entreprise ou l'établissement, aucun candidat aux élections professionnelles remplissant ces conditions ; tous les élus remplissant ces conditions renoncent par écrit à leur droit d'être désignés délégués syndicaux.",
        "Un délégué syndical peut être désigné lorsque l'effectif a atteint au moins cinquante salariés pendant douze mois consécutifs.",
        "La désignation peut intervenir dans un établissement qui regroupe des salariés placés sous la direction d'un représentant de l'employeur et formant une communauté de travail ayant des intérêts propres, susceptibles de générer des revendications communes et spécifiques.",
    ],
    "Réécriture à droit constant : le premier alinéa sépare la désignation du délégué des conditions électorales de son choix. Le deuxième alinéa énonce la désignation subsidiaire puis ses trois cas alternatifs, sans créer de nouveaux alinéas. Aucune réforme de fond n'est appliquée.",
    "Quatre alinéas conservés. Maintien du seuil de cinquante salariés pendant douze mois consécutifs, des 10 % personnels dans le collège au premier tour quel que soit le nombre de votants et du renvoi à L. 2143-12, vérifié localement. Les trois cas du deuxième alinéa restent alternatifs ; le défaut d'autres candidats conditionne le recours aux adhérents ou aux anciens élus. La renonciation écrite concerne tous les élus remplissant les conditions, et non tous les candidats. Les anciens élus restent une catégorie propre sans condition supplémentaire ajoutée. Le périmètre fonctionnel de l'établissement et les intérêts propres générant des revendications communes et spécifiques sont conservés.",
)

add(
    "L2143-4",
    [
        "Dans une entreprise d'au moins cinq cents salariés, un syndicat représentatif dans l'entreprise peut désigner un délégué syndical supplémentaire s'il remplit les deux conditions suivantes : avoir obtenu un ou plusieurs élus dans le collège des ouvriers et employés lors de l'élection du comité social et économique ; compter au moins un élu dans l'un des deux autres collèges.",
        "Le syndicat choisit ce délégué supplémentaire parmi les candidats aux élections professionnelles ayant recueilli au moins 10 % des suffrages exprimés au premier tour des dernières élections au comité social et économique, quel que soit le nombre de votants.",
    ],
    "Réécriture à droit constant : les deux conditions de représentation dans les collèges sont identifiées comme cumulatives au premier alinéa ; le second nomme le syndicat comme auteur du choix du délégué. Aucune réforme de fond n'est appliquée.",
    "Deux alinéas conservés, hors br de présentation. Maintien des cinq cents salariés, de la représentativité dans l'entreprise, du ou des élus ouvriers et employés et d'au moins un élu dans l'un des deux autres collèges. Le seuil de 10 % au premier tour reste indépendant du nombre de votants. Ne pas ajouter à cet article des précisions absentes de sa source sur le collège de calcul ; coordination avec les limites de L. 2143-12, qui vise ce délégué supplémentaire.",
)

add(
    "L2143-5",
    [
        "Dans une entreprise d'au moins deux mille salariés comprenant au moins deux établissements d'au moins cinquante salariés chacun, chaque syndicat représentatif dans l'entreprise peut désigner un délégué syndical central d'entreprise distinct des délégués syndicaux d'établissement.",
        "Pour désigner ce délégué syndical central, le syndicat doit avoir recueilli au moins 10 % des suffrages exprimés au premier tour des dernières élections des titulaires au comité social et économique, quel que soit le nombre de votants. Ce résultat est calculé en additionnant les suffrages de l'ensemble des établissements compris dans l'entreprise.",
        "Toutes les dispositions relatives au délégué syndical d'entreprise s'appliquent au délégué syndical central.",
        "Dans une entreprise de moins de deux mille salariés comprenant au moins deux établissements d'au moins cinquante salariés chacun, chaque syndicat représentatif peut confier également les fonctions de délégué syndical central d'entreprise à l'un de ses délégués syndicaux d'établissement.",
    ],
    "Réécriture à droit constant : les critères électoraux et leur agrégation sont distingués dans deux phrases du deuxième alinéa ; le dernier alinéa formule directement le cumul des fonctions pour les entreprises de moins de deux mille salariés. Aucune réforme de fond n'est appliquée.",
    "Quatre alinéas conservés. Maintien de la frontière de deux mille salariés et d'au moins deux établissements de cinquante salariés chacun, des 10 % recueillis par le syndicat au premier tour des élections des titulaires et de l'addition sur l'ensemble des établissements. Ce résultat est celui du syndicat, sans seuil personnel ajouté au délégué central. À partir de deux mille salariés, le central est distinct des délégués d'établissement ; en dessous, il est choisi parmi eux et cumule les fonctions. Renvoi du deuxième alinéa de L. 2143-12 au premier alinéa du présent article préservé par le maintien de la structure.",
)

add(
    "L2143-6",
    [
        "Dans un établissement de moins de cinquante salariés, un syndicat représentatif dans cet établissement peut désigner comme délégué syndical un membre de la délégation du personnel au comité social et économique, pour la durée du mandat de ce membre.",
        "Ce mandat de délégué syndical ne donne pas droit à un crédit d'heures, sauf disposition conventionnelle. Le membre de la délégation du personnel au comité social et économique peut utiliser, dans les mêmes conditions, le temps dont il dispose au titre de son mandat pour exercer ses fonctions de délégué syndical.",
    ],
    "Réécriture à droit constant : la durée de la désignation est rattachée explicitement au mandat du membre de la délégation du personnel ; le second alinéa distingue le crédit d'heures conventionnel de l'utilisation du temps de ce mandat. Aucune réforme de fond n'est appliquée.",
    "Deux alinéas conservés. Maintien du périmètre de l'établissement de moins de cinquante salariés et de la représentativité à ce niveau. Le mandat syndical ne bénéficie pas d'un crédit d'heures légal propre ; la réserve conventionnelle et l'utilisation du temps du mandat de membre du comité social et économique sont conservées. Ne pas confondre avec L. 2142-1-4, qui vise les syndicats non représentatifs et le périmètre de l'entreprise.",
)

add(
    "L2143-7",
    [
        "Le nom de chaque délégué syndical est communiqué à l'employeur dans les conditions fixées par décret. Les noms des délégués sont également affichés sur les panneaux réservés aux communications syndicales.",
        "Une copie de la communication à l'employeur est transmise simultanément à l'agent de contrôle de l'inspection du travail mentionné à l'article L. 8112-1.",
        "Cette procédure s'applique également au remplacement d'un délégué syndical ou à la cessation de ses fonctions.",
    ],
    "Réécriture à droit constant : les trois formalités sont formulées avec des verbes directs ; le dernier alinéa précise les deux événements auxquels la même procédure s'applique. Aucune réforme de fond n'est appliquée.",
    "Trois alinéas conservés. Maintien de la communication réglementée à l'employeur et de l'affichage au premier alinéa, visé par L. 2143-8. Copie simultanée à l'agent de contrôle de L. 8112-1, vérifié localement ; aucun délai nouveau n'est ajouté. Le même régime couvre remplacement et cessation de fonctions et s'applique au représentant de section par L. 2142-1-2.",
)

add(
    "L2143-8",
    [
        "Le juge judiciaire est seul compétent pour statuer sur les contestations relatives aux conditions de désignation des délégués syndicaux légaux ou conventionnels. Le recours doit, pour être recevable, être introduit dans les quinze jours suivant l'accomplissement des formalités prévues au premier alinéa de l'article L. 2143-7.",
        "À l'expiration de ce délai, la désignation est purgée de tout vice. L'employeur ne peut plus invoquer une irrégularité pour priver le délégué désigné du bénéfice des dispositions du présent chapitre.",
        "Si une contestation rend indispensable une mesure d'instruction, l'État prend en charge les dépenses afférentes à cette mesure.",
    ],
    "Réécriture à droit constant : la compétence exclusive et la condition de recevabilité sont énoncées directement ; les effets de l'expiration du délai sont séparés dans deux phrases du deuxième alinéa. Le dernier alinéa identifie l'État comme débiteur des frais. Aucune réforme de fond n'est appliquée.",
    "Trois alinéas substantiels conservés. Maintien du délai de quinze jours, de son point de départ lié aux formalités du seul premier alinéa de L. 2143-7, de la compétence judiciaire exclusive pour les délégués légaux ou conventionnels, de la purge de tout vice et de la prise en charge par l'État des seules mesures d'instruction rendues indispensables. Correction grammaticale de « jours suivants l'accomplissement » en « jours suivant l'accomplissement », sans modification du délai. Application au représentant de section par L. 2142-1-2 conservée.",
)

add(
    "L2143-9",
    ["Un délégué syndical peut également exercer les fonctions de membre de la délégation du personnel au comité social et économique ou de représentant syndical à ce comité."],
    "Réécriture à droit constant : la compatibilité des fonctions est exprimée par une faculté directe de les exercer également. Aucune réforme de fond n'est appliquée.",
    "Disposition unique conservée. Les deux fonctions compatibles avec celle de délégué syndical sont maintenues sans créer, par cette disposition, de règle de compatibilité entre elles. Application au représentant de section par L. 2142-1-2 conservée.",
)

add(
    "L2143-10",
    [
        "Lorsqu'une modification de la situation juridique de l'employeur mentionnée à l'article L. 1224-1 concerne une entreprise qui conserve son autonomie juridique, le mandat du délégué syndical ou du délégué syndical central se poursuit.",
        "La même règle s'applique lorsque la modification porte sur un établissement au sens de l'article L. 2143-3.",
    ],
    "Réécriture à droit constant : la modification et la condition d'autonomie juridique précèdent l'énoncé du maintien du mandat ; le second alinéa conserve l'application de cette même règle aux établissements. Aucune réforme de fond n'est appliquée.",
    "Deux alinéas substantiels conservés. Renvois à L. 1224-1, vérifié dans le corpus local, et à L. 2143-3 maintenus. Le premier alinéa conserve la condition d'autonomie juridique de l'entreprise. La portée du rattachement du second alinéa au premier, exprimée dans la source par « Il en est de même », est conservée par « La même règle s'applique » ; son articulation avec les conditions de maintien des mandats dans un établissement reste à contrôler sans ajouter ni retrancher ici de condition. Le délégué central et l'application au représentant de section par L. 2142-1-2 sont préservés.",
)


sources = json.loads(Path("source.json").read_text())
assert len(sources) == 24
assert len(drafts) == 24
assert {a["number"] for a in sources} == set(drafts)
answer = []
for source in sources:
    item = {key: source[key] for key in ("code_id", "source_id", "source_sha256", "number")}
    item.update(drafts[source["number"]])
    item["status"] = "rewrite_draft"
    answer.append(item)
Path("answer.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")
print(f"answer.json : {len(answer)} articles")
