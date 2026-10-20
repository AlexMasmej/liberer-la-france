import json
from pathlib import Path


drafts = {}


def add(number, paragraphs, reason, review_notes):
    drafts[number] = {
        "proposed_xml": "\n".join(f"<p>{p}</p>" for p in paragraphs),
        "reason": reason,
        "review_notes": review_notes,
        "status": "rewrite_draft",
    }


add("73 E", [
    "Les prestations de services effectuées pour les besoins directs de la cargaison des aéronefs désignés au 4° du II de l'article 262 du code général des impôts sont les suivantes :",
    "– l'embarquement et le débarquement des passagers et de leurs bagages ;",
    "– le chargement et le déchargement des aéronefs ;",
    "– la manutention des marchandises accessoire au chargement et au déchargement des aéronefs ;",
    "– les opérations d'assistance aux passagers et les opérations relatives à l'enregistrement des passagers et de leurs bagages ;",
    "– l'émission et la réception de messages de trafic ;",
    "– les opérations de trafic et de transit-correspondance ;",
    "– la location de matériels et d'équipements nécessaires au trafic aérien et utilisés sur l'aire des aéroports ;",
    "– la location de contenants et de matériels de protection des marchandises ;",
    "– le gardiennage des marchandises ;",
    "– le magasinage des marchandises nécessaire au transport par voie aérienne, dans la limite des quinze jours précédant leur embarquement ou suivant leur débarquement ;",
    "– les expertises portant sur l'évaluation des dommages subis par les passagers et les marchandises, ainsi que sur l'évaluation des indemnités d'assurances destinées à réparer le préjudice qui en résulte.",
], "Réécriture à droit constant : l'introduction énonce directement la liste et les postes sont harmonisés ; la période de magasinage et l'objet des expertises sont formulés plus directement. Aucune réforme de fond n'est appliquée à cette exonération de TVA.",
    "Les onze catégories et leur ordre sont conservés, ainsi que le renvoi au 4° du II de l'article 262 du CGI. La limite de quinze jours concerne le magasinage, avant l'embarquement ou après le débarquement ; elle n'est pas étendue aux autres prestations. Le rattachement des prestations à la cargaison, y compris celles relatives aux passagers dans la source, est conservé.")

add("73 F", [
    "Pour bénéficier de l'exonération prévue au 10° du II de l'article 262 et au 2° du III de l'article 291 du code général des impôts, relative aux transports par route, en provenance et à destination de l'étranger, de marchandises et de voyageurs étrangers circulant en groupe d'au moins dix personnes, le transporteur routier doit présenter une feuille de route lorsque le transport comporte un transbordement dans un port ou un aéroport français. Cette feuille indique le numéro d'immatriculation du véhicule, le parcours effectué, ainsi que la nature et la quantité de la marchandise ou le nombre de voyageurs transportés en groupe. Le service des douanes du point d'entrée et celui du point de sortie visent ce document respectivement à l'entrée et à la sortie ; à défaut, le visa est apposé par le service des douanes le plus proche du point concerné.",
], "Réécriture à droit constant : l'obligation conditionnée par un transbordement, le contenu de la feuille de route et ses visas sont exposés dans trois phrases successives. Aucun élargissement de l'exonération n'est proposé.",
    "Seuil d'au moins dix personnes, provenance et destination étrangères, transbordement dans un port ou un aéroport français et double visa conservés. Incohérence préexistante à coordonner : le 10° du II de l'article 262 du CGI du corpus ne vise que les voyageurs étrangers, alors que le présent article mentionne aussi les marchandises ; le 2° du III de l'article 291 concerne les services directement liés au placement sous un régime douanier. Ces champs ne sont pas assimilés ni corrigés silencieusement.")

add("73 G", [
    "L'exonération prévue au I de l'article 262 et au 2° du III de l'article 291 du code général des impôts s'applique aux prestations de services suivantes :",
    "1° Les transports de marchandises à destination ou en provenance d'un Etat ou d'un territoire n'appartenant pas à la Communauté européenne, d'un territoire d'un autre Etat membre de la Communauté européenne mentionné au 1° de l'article 256-0 du même code ou d'un département d'outre-mer, ainsi que les transports en provenance et à destination d'un tel Etat, territoire ou département ; les commissions afférentes à ces transports ;",
    "2° Le chargement et le déchargement des véhicules de transport, ainsi que les manutentions accessoires des marchandises désignées au 1° ;",
    "3° La location de véhicules et de matériels utilisés pour les opérations mentionnées aux 1° et 2°, ainsi que la location de contenants et de matériels destinés à la protection des marchandises ;",
    "4° Le gardiennage et le magasinage des marchandises ; lorsqu'un des régimes douaniers communautaires mentionnés au b du 2 du I de l'article 291 du même code s'applique, ces prestations sont exonérées dans la limite de la durée d'application de ce régime ;",
    "5° L'emballage des marchandises destinées à l'exportation ;",
    "6° Les opérations effectuées par des commissionnaires agréés en douane et inhérentes à l'exportation ou aux régimes douaniers communautaires mentionnés au b du 2 du I de l'article 291 du même code. Dans ce dernier cas, les opérations concomitantes ou postérieures à la mise à la consommation sont exclues ;",
    "7° (Abrogé à compter de la date d'entrée en vigueur de l'article 4 du décret n° 96-672 du 25 juillet 1996, J. O. du 28) ;",
    "8° Les prestations consistant à convoyer un moyen de transport entre deux points, sans transporter à titre onéreux des passagers ou des marchandises.",
], "Réécriture à droit constant : les catégories de prestations sont présentées uniformément ; la limite temporelle du 4° et l'exclusion du 6° sont explicitées sans changer leur portée. Aucune réforme de fond ne concerne ce régime dans les orientations fournies.",
    "Les 1° à 8°, y compris l'emplacement abrogé du 7° et sa mention historique, sont conservés. Sont maintenus les trois schémas de trajet du 1°, les commissions, la durée du régime douanier au 4° et l'exclusion des opérations concomitantes ou postérieures à la mise à la consommation au seul cas douanier du 6°. Les termes Communauté européenne et régimes douaniers communautaires sont ceux de la source ; leur coordination avec la réglementation douanière applicable nécessite un contrôle distinct. Le renvoi au b du 2 du I de l'article 291 existe dans le corpus.")

add("73 H", [
    "I. - Le bénéfice des dispositions de l'article 73 G est soumis aux obligations suivantes :",
    "1° Les entreprises installées à l'étranger doivent remettre aux prestataires de services portant sur des marchandises exportées une attestation certifiant que les opérations commandées portent sur des marchandises destinées à l'exportation ;",
    "2° Les preneurs de services portant sur des marchandises placées, lors de leur entrée sur le territoire, sous l'un des régimes douaniers communautaires mentionnés au b du 2 du I de l'article 291 du code général des impôts doivent remettre aux prestataires une attestation certifiant le placement de ces marchandises sous l'un de ces régimes.",
    "II. - Les prestataires de services doivent :",
    "1° Inscrire chaque jour les services rendus dans leur comptabilité ou, à défaut, sur le livre spécial prévu au 3° du I de l'article 286 du code général des impôts, en indiquant la date de l'inscription ainsi que les noms et adresses des donneurs d'ordre ;",
    "2° Conserver à l'appui de leur comptabilité les attestations remises par les donneurs d'ordre. Pour les services se rapportant à des marchandises exportées, ils doivent également y joindre les copies des factures que leur renvoient les clients étrangers, dûment annotées des références aux déclarations d'exportation de ces marchandises : numéros, dates et points de sortie.",
], "Réécriture à droit constant : les obligations des entreprises ou preneurs et celles des prestataires sont distinguées ; l'exigence supplémentaire relative aux factures d'exportation est isolée dans une phrase. Les justificatifs de tiers ne sont pas supprimés au titre de la réutilisation de données administratives.",
    "Subdivisions I et II et leurs 1° et 2° conservés. L'inscription demeure quotidienne, avec sa date et l'identité et l'adresse des donneurs d'ordre. Les attestations et les factures annotées sont cumulatives pour les services relatifs aux marchandises exportées. Coordination avec l'article 73 G maintenue ; le renvoi douanier historique au b du 2 du I de l'article 291 n'est pas modernisé sans contrôle.")

add("73 I", [
    "Pour l'application du 6° du II de l'article 262 du code général des impôts, et aux seules fins de cette réglementation, relève de la petite pêche côtière la pêche pratiquée au moyen de bateaux réunissant les conditions suivantes : une longueur hors tout inférieure à douze mètres, l'utilisation exclusive d'engins non remorqués et une sortie en mer n'excédant pas 24 heures.",
], "Réécriture à droit constant : les trois caractéristiques du bateau et de la sortie sont énoncées comme des conditions cumulatives dans une phrase plus lisible. Aucune modification de fond de la définition fiscale n'est introduite.",
    "Définition limitée au 6° du II de l'article 262 du CGI ; longueur strictement inférieure à douze mètres, engins uniquement non remorqués et durée au plus égale à 24 heures conservées. Cette définition n'est pas étendue à d'autres réglementations de la pêche.")

add("74", [
    "1. Les livraisons d'objets ou de marchandises exportés réalisées par les assujettis sont exonérées de la taxe sur la valeur ajoutée sous les conditions suivantes :",
    "a. L'assujetti exportateur qui ne tient pas habituellement une comptabilité permettant de déterminer son chiffre d'affaires doit inscrire les envois sur le registre prévu au 3° du I de l'article 286 du code général des impôts ;",
    "b. (abrogé)",
    "c. L'assujetti exportateur doit établir, pour chaque envoi, une déclaration d'exportation conforme au modèle donné par l'administration. Il conserve à l'appui de sa comptabilité ou du registre prévu au a l'exemplaire numéro 3 de cette déclaration, visé par l'autorité douanière compétente conformément au code des douanes communautaires et à ses dispositions d'application. Lorsque la déclaration d'exportation est établie selon la procédure électronique prévue par le règlement (CEE) n° 2913/92 du Conseil du 12 octobre 1992 modifié établissant le code des douanes communautaires et par ses textes d'application, l'assujetti produit la certification de sortie délivrée par le bureau d'exportation. Toutefois, les assujettis exportateurs qui ne figurent pas dans la rubrique exportateur de la déclaration en douane conservent à l'appui de leur comptabilité ou du registre prévu au a un exemplaire de leurs factures visées par la personne habilitée ou autorisée à déclarer en douane et annotées des références permettant d'identifier la déclaration en douane correspondante, dans les cas suivants : la sortie du territoire communautaire à partir de la France est effectuée par l'entremise d'un intermédiaire agissant au nom et pour le compte d'autrui et désigné comme expéditeur des biens sur la déclaration d'exportation ; des opérateurs interviennent dans une livraison commune de marchandises à l'exportation ; ou les marchandises font l'objet d'un groupage.",
    "Lorsque l'intermédiaire est habilité ou autorisé à déclarer en douane et a obtenu de l'administration des douanes et droits indirects un agrément spécifique à la procédure du dédouanement des envois express, l'assujetti exportateur conserve à l'appui de sa comptabilité ou du registre prévu au a le document remis par cet intermédiaire, comportant tous les éléments d'information requis par l'administration.",
    "d. Lorsque l'assujetti exportateur ne produit pas les justificatifs prévus au c, il doit conserver à l'appui de sa comptabilité ou du registre mentionné au a l'un des éléments de preuve alternatifs énumérés ci-après. Cette possibilité est exclue pour les opérations mentionnées aux quatrième à huitième alinéas du I de l'article 262 du code général des impôts. L'élément produit doit justifier la sortie des biens expédiés vers un pays n'appartenant pas à la Communauté européenne, un territoire mentionné au 1° de l'article 256-0 du même code ou un département d'outre-mer :",
    "1° La déclaration en douane authentifiée par l'administration des douanes du pays de destination finale des biens, ou une attestation de cette administration, accompagnée, le cas échéant, d'une traduction officielle ;",
    "2° Tout document de transport des biens vers un pays n'appartenant pas à la Communauté européenne, un territoire mentionné au 1° de l'article 256-0 du code général des impôts ou un département d'outre-mer ; ou tout document relatif au chargement du moyen de transport quittant la Communauté européenne pour rejoindre le pays ou le territoire de destination finale situé hors de la Communauté ;",
    "3° Pour les biens soumis à des contrôles particuliers, tout document douanier visé par le service des douanes compétent et utilisé pour surveiller l'acheminement des biens vers leur destination finale hors de la Communauté ;",
    "4° Les documents mentionnés à l'article 302 M du code général des impôts, émis sur papier ou transmis par voie électronique dans le cadre du système d'informatisation du suivi des mouvements de produits soumis à accises, visés par le bureau des douanes du point de sortie de la Communauté ; ou tout autre élément de preuve alternatif accepté par l'administration chargée de la surveillance des mouvements de produits soumis à accises ;",
    "5° Pour les produits autres que ceux soumis à accises et en cas de livraison effectuée dans les conditions prévues au premier alinéa du 2° du I de l'article 262 du code général des impôts, une déclaration du transporteur ou du transitaire ayant pris en charge les biens. Cette déclaration doit être accompagnée de la preuve du paiement des biens par le client établi dans un pays n'appartenant pas à la Communauté européenne, un territoire mentionné au 1° de l'article 256-0 du même code ou un département d'outre-mer.",
    "2. Pour les envois de marchandises effectués par La Poste, l'assujetti exportateur apporte la preuve de l'exportation au moyen d'un exemplaire de la déclaration en douane CN23. Toutefois, si la valeur de l'envoi postal excède 8 000 €, il peut également conserver à l'appui de sa comptabilité ou du registre prévu au a du 1 le document administratif unique.",
    "3. et 4. (Abrogés à compter de la date d'entrée en vigueur du décret n° 93-991 du 9 août 1993, J.O. des 9 et 10).",
    "4 bis. Le service des douanes effectue toutes vérifications utiles à la sortie des objets ou marchandises. Les agents du service compétent effectuent également toutes vérifications utiles chez les assujettis exportateurs et chez les personnes habilitées ou autorisées à déclarer en douane. Les assujettis exportateurs et les personnes habilitées ou autorisées à déclarer en douane doivent présenter aux agents les registres et factures prescrits par le présent article ainsi que, le cas échéant, toute autre pièce susceptible d'étayer les énonciations de ces documents.",
    "5. Les livraisons de biens d'avitaillement destinés aux besoins des navires visés au 6° du II de l'article 262 du code général des impôts sont exonérées de la taxe sur la valeur ajoutée, qu'elles soient effectuées directement ou en sortie d'un régime suspensif mentionné au I de l'article 277 A du même code. Pour chaque livraison, l'assujetti exportateur doit établir une déclaration en douane conforme au modèle fourni par l'administration ou tout autre document en tenant lieu prévu par la réglementation douanière. Il conserve ces documents à l'appui de sa comptabilité, après avis du service des douanes chargé du contrôle de la mise à bord des biens.",
    "6. (Abrogé)",
], "Réécriture à droit constant : les obligations documentaires sont exprimées avec un sujet explicite ; les cas particuliers du c, les preuves alternatives et les contrôles sont répartis en phrases plus courtes au sein des mêmes alinéas. Toutes les voies de preuve et leurs restrictions sont reprises. Aucune réforme de fond de la TVA n'est appliquée.",
    "Structure 1, a à d, 1° à 5°, 2, 3 et 4, 4 bis, 5 et 6 et ordre des alinéas conservés. Contrôles particuliers : exemplaire numéro 3, seuil strictement supérieur à 8 000 €, déclaration CN23, factures visées, agrément des envois express, exclusion des quatrième à huitième alinéas du I de l'article 262 et conditions cumulatives du 5° du d maintenus. Les mentions historiques des abrogations restent telles quelles et ne fixent aucune date de réforme. Le règlement (CEE) n° 2913/92 et la terminologie douanière historique appellent un contrôle de coordination avec la réglementation applicable ; ils ne sont pas remplacés sans base fournie. L'article 302 M n'a pas été retrouvé dans le fichier impots.json du corpus : son renvoi est conservé et doit être vérifié. Le corpus de l'article 277 A signale une recodification à compter du 1er janvier 2027, avec maintien transitoire de certaines dispositions : coordonner le renvoi du 5 lors de cette opération, sans lui substituer une référence conjecturale.")

add("75", [
    "Pour la procédure prévue aux deuxième à sixième alinéas du 2° du I de l'article 262 du code général des impôts, l'exportation est justifiée par un bordereau de vente à l'exportation. Ce bordereau est numéroté dans une série continue et conforme au modèle établi par la direction générale des douanes et droits indirects. Le vendeur le délivre le jour de la transaction au voyageur éligible à la procédure et muni de son passeport.",
    "Le bordereau de vente à l'exportation est édité par voie informatique au moyen d'un téléservice, sauf recours à la procédure de secours prévue à l'article 75 A, qui constitue la seule exception.",
    "Un arrêté du ministre chargé du budget détermine la forme du titre mentionné au premier alinéa ainsi que les conditions de son établissement et de son apurement.",
], "Réécriture à droit constant : la définition du justificatif, ses caractéristiques et sa remise sont exposées séparément ; le caractère exclusif de la procédure de secours est conservé. Aucune réforme de fond n'est introduite.",
    "Trois alinéas conservés afin de maintenir les renvois de l'article 75 A au second alinéa et celui du présent article à son premier alinéa. Numérotation continue, modèle douanier, remise le jour de la transaction et passeport maintenus. La portée exacte des deuxième à sixième alinéas du 2° du I de l'article 262 doit être vérifiée lors de toute réorganisation de cet article ; aucune renumérotation n'est opérée ici.")

add("75 A", [
    "Le vendeur peut recourir à la procédure de secours dans les cas énumérés ci-dessous, à condition d'être préalablement affilié à un opérateur de détaxe ou habilité au téléservice mentionné au second alinéa de l'article 75 :",
    "1° Le téléservice mentionné au second alinéa de l'article 75 est affecté par une indisponibilité générale ;",
    "2° Les outils informatiques du vendeur permettant d'émettre les bordereaux de vente à l'exportation sont en panne ;",
    "3° La connexion internet du vendeur est interrompue.",
    "Un arrêté du ministre chargé du budget fixe les modalités de recours à cette procédure de secours.",
], "Réécriture à droit constant : la condition préalable d'affiliation ou d'habilitation est distinguée des trois incidents autorisant la procédure de secours ; chaque incident est formulé comme une situation explicite. Aucune extension du champ de la procédure n'est prévue.",
    "Les trois cas sont limitatifs et conservés dans l'ordre 1° à 3°. L'affiliation préalable à un opérateur de détaxe et l'habilitation au téléservice restent alternatives. Le renvoi au second alinéa de l'article 75 est maintenu ; la proposition de cet article conserve cet emplacement.")

add("76", [
    "1. En cas d'échange, le chiffre d'affaires imposable correspond à la valeur des objets reçus en contrepartie des objets livrés, augmentée de la soulte.",
    "2. (Abrogé)",
    "3. Dispositions devenues sans objet.",
], "Réécriture à droit constant du 1 : la base imposable est énoncée directement, en conservant l'ajout de la soulte. Les emplacements 2 et 3 sont maintenus ; aucune réforme de fond ne vise cette règle d'assiette.",
    "Numérotation 1 à 3 conservée. La soulte reste ajoutée à la valeur des objets reçus ; aucune déduction, règle de valorisation ou exception nouvelle n'est introduite. Les mentions d'abrogation et de dispositions sans objet ne sont pas traitées comme des emplacements Réservé.")

add("77", [
    "1. Les redevables dont les opérations sont passibles de la taxe sur la valeur ajoutée lors de l'encaissement du prix ou de la rémunération peuvent opter pour le paiement de cette taxe d'après les débits. Ils doivent déclarer cette option par écrit au service des impôts dont ils relèvent pour le paiement de la taxe.",
    "L'option couvre l'ensemble des opérations réalisées. Elle reste valable tant que le redevable ne demande pas par écrit le retour au paiement d'après les encaissements.",
    "2. L'option prévue au 1 s'applique aux opérations réalisées à compter du premier jour du mois qui suit celui de son exercice.",
    "Lorsque le redevable renonce à l'option, le paiement d'après les encaissements s'applique aux opérations réalisées à compter du premier jour du mois qui suit celui de la déclaration de renonciation.",
], "Réécriture à droit constant : le choix offert au redevable et la déclaration écrite sont distingués ; les effets temporels de l'option et de sa renonciation sont formulés de manière parallèle. Aucun régime nouveau d'exigibilité n'est créé.",
    "Subdivisions 1 et 2 et quatre alinéas conservés. Portée globale de l'option, maintien jusqu'à une demande écrite et effet au premier jour du mois suivant conservés pour l'exercice comme pour la renonciation. Ne pas confondre ce calendrier avec l'effet immédiat de la renonciation propre aux travaux immobiliers à l'article 83.")

add("78", [
    "1. Les entrepreneurs peuvent acquitter la taxe sur la valeur ajoutée au moment de la livraison des travaux immobiliers lorsque ces travaux sont exécutés dans le cadre d'un marché unique comprenant la fourniture de biens meubles et l'installation ou l'incorporation à un ouvrage immobilier des matériels et appareils fournis.",
    "2. L'option mentionnée au 1 n'est admise que si la valeur de vente des matériels ou appareils fournis, indispensables au fonctionnement de l'installation ou incorporés à l'ouvrage immobilier, est supérieure à 50 % du montant total du marché.",
    "3. L'option prévue au 1 est exclue pour les travaux suivants :",
    "a) Les travaux immobiliers concourant :",
    "1° A la construction, à la livraison, à la réparation ou à la réfection des voies et bâtiments de l'Etat et des collectivités locales, ainsi que de leurs établissements publics, à l'exception des établissements publics à caractère industriel ou commercial assujettis à la taxe sur la valeur ajoutée ;",
    "2° A la construction et à la livraison des immeubles destinés à être affectés à l'habitation pour au moins les trois quarts de leur superficie ;",
    "3° A la réparation et à la réfection des locaux d'habitation ainsi que des parties communes des immeubles dont au moins les trois quarts de la superficie sont affectés à l'habitation ;",
    "4° A la construction, à la livraison, à la réparation et à la réfection des immeubles affectés à l'exercice public du culte et des locaux annexes nécessaires à cette activité ;",
    "b) Les travaux immobiliers réalisés par les redevables inscrits au Registre national des entreprises en tant qu'entreprise du secteur des métiers et de l'artisanat et placés, sur option, sous le régime simplifié d'imposition.",
], "Réécriture à droit constant : les critères du marché unique et du seuil de fournitures sont clarifiés ; les exclusions sont énoncées avec leur exception propre pour certains établissements publics. Aucune réforme du logement ou de la TVA n'est étendue à cette option.",
    "Structure 1 à 3, a), 1° à 4° et b) conservée. Valeur strictement supérieure à 50 %, seuils d'au moins trois quarts et double condition tenant au caractère industriel ou commercial et à l'assujettissement à la TVA des établissements publics maintenus. La note source rattache l'entrée en vigueur au 1er janvier 2023 à l'article 18 du décret n° 2022-1015 du 19 juillet 2022 ; cette date historique ne constitue pas une date d'effet de la présente réécriture. Coordination du champ de l'option avec les articles 79 à 84 maintenue.")

add("79", [
    "Pour opter pour le paiement de la taxe lors de la livraison des travaux immobiliers, l'entrepreneur doit déposer une déclaration auprès du service des impôts dont il dépend. Par cette déclaration, il s'engage à acquitter la taxe lors de la livraison des travaux pour tous les marchés conclus à compter de la date de la déclaration et remplissant les conditions de l'article 78.",
    "Les entreprises nouvelles doivent déposer cette déclaration dans les quinze jours de leur installation. Les entreprises qui ont modifié leur activité doivent la déposer dans les quinze jours du commencement de leur nouvelle activité.",
], "Réécriture à droit constant : la formalité d'option et l'engagement global qui en résulte sont séparés ; le point de départ du délai est explicité pour chacune des deux catégories d'entreprises. Aucune transition ou réforme de fond nouvelle n'est introduite.",
    "Deux alinéas conservés. L'engagement couvre tous les marchés remplissant les conditions de l'article 78 et conclus dès la date de la déclaration, sans extension aux marchés antérieurs. Le délai de quinze jours demeure propre aux entreprises nouvelles ou ayant modifié leur activité.")

add("80", [
    "Le bénéfice de l'option est subordonné à une mention expresse, dans les contrats établis pour les marchés concernés, du choix de l'entrepreneur de payer la taxe sur la valeur ajoutée lors de la livraison des travaux immobiliers. L'entrepreneur doit reproduire cette mention sur tous les mémoires afférents à ces marchés.",
], "Réécriture à droit constant : la condition de mention contractuelle et l'obligation de la reproduire sur chaque mémoire sont exposées en deux phrases. Aucun assouplissement ni élargissement de l'option n'est proposé.",
    "Obligations cumulatives concernant les contrats et tous les mémoires conservées. L'article 82 mentionne également les factures dans la sanction du défaut de mention : cette différence préexistante entre les supports énumérés aux articles 80 et 82 est signalée sans ajouter silencieusement un support à l'article 80.")

add("81", [
    "L'entrepreneur qui a exercé l'option doit attendre la livraison des travaux pour facturer la taxe sur la valeur ajoutée. La livraison correspond à la remise des ouvrages en la possession du maître de l'ouvrage. La date retenue pour cette livraison ne peut être postérieure à l'occupation ou à l'utilisation réelle des locaux et installations.",
], "Réécriture à droit constant : l'interdiction de facturer avant la livraison, la définition de celle-ci et sa date limite sont réparties en trois phrases. Aucune nouvelle règle de fait générateur n'est ajoutée.",
    "Remise en possession du maître de l'ouvrage et date au plus tard égale à l'occupation ou à l'utilisation réelle conservées. La facturation anticipée reste interdite ; la sanction de l'article 82 demeure coordonnée.")

add("82", [
    "L'option est annulée si l'entrepreneur facture la taxe sur la valeur ajoutée à l'occasion de l'encaissement d'un seul acompte avant la livraison, ou s'il omet les mentions prévues à l'article 80 sur les contrats, factures ou mémoires. Dans chacun de ces cas, la taxe devient immédiatement exigible sur tous les encaissements reçus au titre des marchés en cours.",
], "Réécriture à droit constant : les deux causes d'annulation sont formulées explicitement comme alternatives et leur conséquence commune figure dans une seconde phrase. Aucun changement de fond n'est apporté à la sanction.",
    "Un seul acompte facturé avec TVA suffit ; la conséquence porte sur tous les encaissements des marchés en cours. Contrats, factures et mémoires sont maintenus comme dans la source. Incohérence de formulation préexistante : l'article 80 n'énumère expressément que les contrats et les mémoires ; cette question nécessite une coordination expresse plutôt qu'une correction implicite.")

add("83", [
    "L'entrepreneur peut renoncer à tout moment à l'option pour le paiement de la taxe lors de la livraison des travaux immobiliers, en déclarant cette renonciation au service des impôts dont il dépend. La renonciation prend effet le jour de cette déclaration. Elle rend immédiatement exigible le paiement de la taxe afférente aux encaissements reçus au titre des marchés en cours.",
], "Réécriture à droit constant : la faculté de renoncer est reliée à sa déclaration obligatoire ; l'effet temporel et l'exigibilité immédiate sont exposés séparément. Aucune modification de fond du régime n'est appliquée.",
    "Effet dès la date de la déclaration et paiement immédiat sur les encaissements des marchés en cours conservés. Coordination avec le délai d'un an avant une nouvelle option prévu à l'article 84. Le délai au mois suivant de l'article 77 ne s'applique pas à cette renonciation.")

add("84", [
    "Après avoir renoncé à l'option, l'entrepreneur doit attendre l'expiration d'un délai d'un an à compter de la date de sa renonciation pour exercer une nouvelle option.",
], "Réécriture à droit constant : la restriction est formulée comme un délai d'attente dont le point de départ est explicite. Aucune réforme de fond ne vise cette condition.",
    "Délai d'un an conservé, calculé depuis la date de renonciation et non depuis la fin d'un exercice ou d'un marché. Coordination avec l'effet de la déclaration de renonciation prévu à l'article 83.")

add("84 A", [
    "Pour l'application du 1° de l'article 273 septies C du code général des impôts, le demandeur doit certifier sur l'honneur que les conditions suivantes sont remplies :",
    "1° Le certificat d'immatriculation du véhicule ou, le cas échéant, son contrat de location est établi au nom d'un exploitant de remontées mécaniques ou de domaines skiables ;",
    "2° Le véhicule est exclusivement affecté à l'exploitation de ces infrastructures ;",
    "3° Le véhicule comporte, d'origine ou à la suite de travaux, au moins trois des équipements techniques suivants :",
    "a. Plateau de chargement ;",
    "b. Arceau de sécurité pour habitacle ;",
    "c. Portique de levage ;",
    "d. Crochet d'attelage ;",
    "e. Treuil frontal ;",
    "f. Bac de benne ;",
    "g. Blocage de différentiel ;",
    "h. Boîte de transfert ;",
    "i. Arceau porte-échelle arrière de cabine ;",
    "j. Plusieurs points d'arrimage sur les côtés des ridelles ;",
    "k. Pneus mixtes.",
], "Réécriture à droit constant : les trois éléments de la certification sur l'honneur sont présentés comme des conditions explicites ; le seuil d'équipements est formulé directement. Les désignations techniques de la liste sont conservées. Aucune réforme de fond n'est introduite.",
    "Subdivisions 1° à 3° et a à k conservées avec les onze équipements. Seuil d'au moins trois équipements, présence d'origine ou après travaux et affectation exclusive maintenus. La note source indique une modification en conséquence de l'article 89 de la loi n° 2023-1322 du 29 décembre 2023 ; elle ne fixe aucune date future de réforme. Le renvoi vérifié au 1° de l'article 273 septies C concerne les véhicules tout terrain des remontées mécaniques et domaines skiables ; aucun ajout du régime des véhicules de transport d'équidés.")

add("84 B", [
    "1° Pour l'application de l'article 273 septies D du code général des impôts, les associations qui reçoivent des dons d'invendus alimentaires et non alimentaires neufs doivent établir, au profit des assujettis donateurs, une attestation en deux exemplaires contenant les informations suivantes :",
    "a) Le nom, l'adresse et l'objet de l'association bénéficiaire ;",
    "b) La date et le numéro du décret de reconnaissance d'utilité publique, tel qu'il figure au Journal officiel ;",
    "c) Le nom et l'adresse du donateur ;",
    "d) Un inventaire détaillé indiquant la date du don, la nature des biens donnés et leur quantité.",
    "Une même attestation peut couvrir plusieurs dons reçus d'un même donateur au cours d'une période n'excédant pas une année civile.",
    "2° Un tiers dûment mandaté, agissant au nom et pour le compte de l'association bénéficiaire, peut émettre et délivrer l'attestation mentionnée au 1°.",
    "3° L'association bénéficiaire et l'assujetti donateur doivent conserver chacun un exemplaire de l'attestation prévue au 1°, dans les conditions du I de l'article L. 102 B du livre des procédures fiscales. Un tiers dûment mandaté, agissant au nom et pour le compte du bénéficiaire ou du donateur, peut assurer cette conservation dans les mêmes conditions.",
], "Réécriture à droit constant : l'obligation d'attestation, son contenu, le regroupement des dons et les possibilités de mandat sont formulés directement. La conservation par chaque partie reste explicite. Les preuves entre donateur et bénéficiaire ne sont pas supprimées au titre de la réutilisation administrative des données.",
    "Structure 1° à 3° et a) à d) conservée. Deux exemplaires, donateur unique pour une attestation regroupée, limite d'une année civile, mandat régulier pour émission ou conservation et renvoi au I de l'article L. 102 B du LPF maintenus. Le renvoi à l'article 273 septies D du CGI conserve le champ des associations reconnues d'utilité publique présentant l'intérêt général défini par cet article, sans l'étendre à toutes les associations recevant des dons.")

add("85", [
    "1. L'assujetti à la taxe sur la valeur ajoutée qui souhaite bénéficier de la suspension de cette taxe prévue au I de l'article 277 A du code général des impôts présente la demande d'autorisation d'ouverture d'un régime mentionné au 2° du même I. Il doit être destinataire des opérations de livraison, d'acquisition intracommunautaire, d'importation ou de prestation de services concernées.",
    "Le demandeur établi dans un autre Etat membre de l'Union européenne doit être identifié à la taxe sur la valeur ajoutée en France. Il doit également y avoir désigné un mandataire chargé d'accomplir, au nom et pour le compte du demandeur, les formalités et obligations afférentes au régime fiscal sollicité.",
    "Sous réserve du III de l'article 289 A du code général des impôts, le demandeur établi en dehors de l'Union européenne doit avoir désigné en France un représentant fiscal dans les conditions du I du même article. Ce représentant accomplit, au nom et pour le compte du demandeur, les formalités et obligations afférentes au régime fiscal sollicité.",
    "2. La demande est déposée dans les conditions suivantes :",
    "a. Pour les régimes mentionnés aux a et d du 2° du I de l'article 277 A du code général des impôts, elle est déposée par l'assujetti qui souhaite bénéficier de la suspension de la taxe prévue au I du même article pour les opérations de livraison, d'acquisition intracommunautaire ou d'importation dont il est destinataire, ou de prestation de services dont il est le preneur.",
    "La personne qui souhaite gérer le régime sollicité peut également déposer la demande pour le compte de l'assujetti. Elle est dénommée gestionnaire ou entreposeur selon le régime sollicité.",
    "b. Pour les régimes mentionnés au e du 2° du I de l'article 277 A du même code, la demande est déposée par l'assujetti qui souhaite effectuer ou faire effectuer les opérations envisagées.",
    "3. La demande comporte les renseignements demandés par l'administration concernant le demandeur, le cas échéant le gestionnaire ou l'entreposeur selon le régime sollicité, et l'objet du régime. Dans le cas du régime fiscal suspensif prévu au a du 2° du I de l'article 277 A du même code, elle précise les fonctions pour les besoins desquelles le régime est demandé. Elle comporte également les renseignements relatifs aux opérations envisagées, à la nature des biens, au ou aux lieux où ils seront situés ou utilisés, aux locaux ou autres installations éventuellement utilisés, ainsi que tout autre renseignement utile aux contrôles de l'administration. Pour instruire la demande, l'administration réutilise les renseignements qu'elle détient déjà légalement et qu'elle peut légalement réutiliser à cette fin, dans le respect des secrets protégés. Elle ne demande pas au demandeur de fournir de nouveau ces renseignements. Le demandeur peut en demander la rectification.",
], "Réécriture à droit constant des personnes habilitées, de leur représentation et des renseignements requis, avec des phrases distinctes pour chaque situation. Réforme de fond au 3 : application de l'orientation Déclarer une fois par la réutilisation des renseignements déjà légalement détenus et réutilisables pour l'instruction, sans demande en double, avec maintien des secrets protégés et du droit de rectification. Cette mesure ne dispense pas de l'autorisation ni de fournir les renseignements manquants.",
    "Subdivisions 1 à 3 et a et b, ainsi que les huit alinéas, conservés ; la règle de réutilisation est ajoutée au 3 sans déplacer les alinéas. Les demandes modificatives de l'article 85 B sont expressément coordonnées dans la proposition de cet article. Adapter les formulaires et modalités administratives d'instruction à cette réutilisation ; aucune nouvelle interconnexion ni dérogation aux secrets n'est créée. Incohérence préexistante vérifiée : le III de l'article 289 A du CGI auquel la source réserve l'obligation de représentation est abrogé dans le corpus, tandis que le I comporte notamment des exceptions ; le renvoi au III est conservé en attente d'une coordination expresse, sans rétablir ni supprimer ces exceptions. Le corpus des articles 277 A et 289 A signale leur recodification à compter du 1er janvier 2027 avec certaines dispositions transitoirement maintenues ; les renvois doivent être coordonnés à cette occasion, sans inventer ici les dispositions de remplacement.")

add("85 A", [
    "1. La décision autorisant l'ouverture d'un régime mentionné au 2° du I de l'article 277 A du code général des impôts fixe les éléments constitutifs du régime ainsi que ses conditions d'octroi et de fonctionnement. L'autorisation est subordonnée au respect, par le demandeur, de ses obligations déclaratives et de paiement liées à son activité professionnelle.",
    "Pour les entreprises créées depuis plus de deux ans, l'autorisation d'ouverture est réputée accordée tacitement à l'expiration d'un délai de 30 jours. Ce délai court à compter de la date de réception de la demande par le service.",
    "Sans préjudice de l'article 1788 A du code général des impôts et des articles L. 80 K et L. 80 L du livre des procédures fiscales, l'autorisation désigne le service chargé de la gestion du régime. Il s'agit, selon le cas, du service des impôts chargé des régimes mentionnés aux a, d et e du 2° du I de l'article 277 A du code général des impôts, ou du service des douanes chargé du régime fiscal suspensif mentionné au a du 2° du I du même article.",
    "2. Lorsque la demande est soumise à autorisation, l'autorisation prend effet à la date fixée par l'administration.",
], "Réécriture à droit constant : le contenu et la condition de l'autorisation sont distingués ; le délai d'accord tacite et la désignation du service compétent sont énoncés directement. Le sujet de la prise d'effet au 2 est explicité. Aucune réforme de fond du délai ou du contrôle n'est introduite.",
    "Quatre alinéas et subdivisions 1 et 2 conservés. Ancienneté strictement supérieure à deux ans et délai de 30 jours courant de la réception maintenus. L'articulation préexistante entre l'accord tacite du 1 et la date fixée par l'administration au 2 mérite un contrôle, notamment en cas d'absence de décision expresse ; aucun mécanisme complémentaire de date d'effet n'est inventé. Compétences fiscales ou douanières et réserves des articles 1788 A du CGI et L. 80 K et L. 80 L du LPF conservées. Le corpus de l'article 277 A annonce une recodification au 1er janvier 2027 avec maintien transitoire de certaines dispositions : prévoir la coordination des renvois.")

add("85 B", [
    "Tout changement affectant les éléments constitutifs d'un régime autorisé, tels qu'ils figurent dans la demande d'ouverture, doit être autorisé.",
    "L'autorisation du changement prend la forme d'une décision modifiant l'autorisation d'ouverture. Cette décision est prise dans les mêmes conditions que l'autorisation d'ouverture et est valable à compter de la date fixée par l'administration. Pour l'instruction de la demande de modification, les règles de réutilisation des renseignements prévues au 3 de l'article 85 s'appliquent.",
], "Réécriture à droit constant de l'obligation d'autorisation, de la forme de la décision et de sa date de validité. Coordination de fond avec la réforme du 3 de l'article 85 : les règles de réutilisation des renseignements sont expressément appliquées aux demandes de modification. Aucune catégorie de changement n'est soustraite à autorisation.",
    "Deux alinéas conservés. Le périmètre reste celui des éléments constitutifs figurant dans la demande d'ouverture ; la date de validité demeure fixée par l'administration. Le renvoi au 3 de l'article 85 vise la règle proposée dans ce même lot : réutilisation légalement possible des renseignements détenus, absence de demande en double, respect des secrets et droit de rectification. Cette coordination ne dispense pas d'indiquer le changement ni d'obtenir la décision modificative.")

add("85 C", [
    "Le titulaire de l'autorisation d'ouverture peut demander la fermeture d'un régime fiscal suspensif mentionné au 2° du I de l'article 277 A du code général des impôts. Sa demande doit être formulée au moins deux mois avant la date d'effet de la fermeture, qui peut être prononcée sur cette demande.",
    "L'administration peut également prononcer la fermeture de sa propre initiative dans les cas suivants :",
    "1. Le régime est resté inactif pendant un an. La fermeture prend alors effet le premier jour du mois suivant celui au cours duquel l'administration a pris sa décision.",
    "2. Les règles de fonctionnement du régime ne sont pas respectées, ou les formalités et obligations qui lui sont liées ne sont pas exécutées. La fermeture prend alors effet dès la notification des constatations effectuées.",
    "3. Les obligations déclaratives et de paiement ne sont pas respectées. La fermeture prend alors effet dès la notification des constatations effectuées.",
], "Réécriture à droit constant : la demande du titulaire et l'initiative de l'administration sont distinguées ; chaque motif administratif est relié à sa date d'effet. Le caractère facultatif du prononcé de fermeture est conservé. Aucune réforme de fond n'est introduite.",
    "Cinq alinéas et motifs 1 à 3 conservés. Préavis d'au moins deux mois pour le titulaire ; un an d'inactivité et effet au premier jour du mois suivant la décision pour le 1 ; effet dès notification des constatations pour les 2 et 3 maintenus. Aucune procédure nouvelle de retrait n'est inventée. Le renvoi à l'article 277 A devra être coordonné avec sa recodification signalée dans le corpus à compter du 1er janvier 2027, sous réserve de ses maintiens transitoires.")

add("85 D", [
    "Le transfert de biens entre les fonctions énoncées à l'article 85 E est autorisé au sein du régime visé au du 2° du I de l'article 277 A du code général des impôts, à condition que l'administration conserve les moyens de contrôler le suivi des biens.",
], "Réécriture à droit constant : l'opération autorisée devient le sujet de la phrase et la condition de contrôle est exprimée directement. Le renvoi incomplet de la source est conservé sans lui attribuer une subdivision absente. Aucune réforme de fond n'est introduite.",
    "Anomalie préexistante : la source porte exactement le renvoi incomplet « au du 2° du I de l'article 277 A ». Il est reproduit dans la proposition ; aucune lettre n'est inventée. Le a du 2° du I de l'article 277 A désigne le régime fiscal suspensif dans le corpus, et l'article 85 E en décrit les fonctions : ce rapprochement doit faire l'objet d'une coordination expresse avant de compléter la référence. Le contrôle du suivi des biens reste une condition du transfert. Tenir également compte de la recodification de l'article 277 A signalée dans le corpus à compter du 1er janvier 2027 et de ses dispositions transitoires.")


def main():
    sources = json.loads(Path("source.json").read_text())
    assert len(sources) == len(drafts) == 24
    assert {s["number"] for s in sources} == set(drafts)
    answers = []
    for source in sources:
        answer = {key: source[key] for key in (
            "code_id", "source_id", "source_sha256", "number"
        )}
        answer.update(drafts[source["number"]])
        answers.append(answer)
    Path("answer.json").write_text(
        json.dumps(answers, ensure_ascii=False, indent=2) + "\n"
    )


if __name__ == "__main__":
    main()
