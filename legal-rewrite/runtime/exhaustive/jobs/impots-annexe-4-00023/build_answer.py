import json
from pathlib import Path


SOURCES = json.loads(Path('source.json').read_text())
drafts = {}


def add(number, xml, reason, notes):
    assert number not in drafts
    drafts[number] = (xml.strip(), reason, notes)


APPLICATION_2018 = (
    "La note source réserve l'application de cette rédaction aux déclarations "
    "souscrites au titre des revenus, produits et gains dont le fait générateur "
    "d'imposition intervient à compter du 1er septembre 2018, conformément à "
    "l'article 2 de l'arrêté du 28 août 2018 ; cette portée temporelle est conservée."
)

add('170 octies', """
<p>En Île-de-France, le directeur régional des finances publiques d'Île-de-France et de Paris exerce les compétences que les articles 170 quinquies, 170 sexies et 170 septies H attribuent aux directeurs départementaux ou, le cas échéant, régionaux des finances publiques du département au chef-lieu duquel est localisée une direction de contrôle fiscal. Dans les départements d'outre-mer, ces mêmes compétences sont exercées par le directeur régional des finances publiques territorialement compétent.</p>
""",
    "Réécriture à droit constant : deux phrases, dans le même alinéa, distinguent l'autorité compétente en Île-de-France de celle compétente dans les départements d'outre-mer. Les compétences transférées restent définies par les trois articles cités. Aucune réforme de fond de cette répartition territoriale n'est prévue par policy.json.",
    "Les trois renvois et les deux champs territoriaux sont conservés. Le corpus local maintient à l'article 170 septies H l'ancienne dénomination « directeur des services fiscaux », alors que le présent article emploie les dénominations des finances publiques : discordance préexistante à coordonner sans substitution silencieuse. La note source rattache les modifications à l'article 35-I-2° de la loi n° 2021-1900 du 30 décembre 2021 ; cette mention historique ne fixe aucune entrée en vigueur de la réforme projetée."
)

add('170 decies', """
<p>I. – Hors du secteur du logement, le directeur départemental ou le directeur régional des finances publiques du département dans lequel le programme d'investissement est réalisé délivre l'agrément prévu aux II quater et III de l'article 217 undecies du code général des impôts lorsque le montant total du programme n'excède pas 10 millions d'euros.</p>
<p>Le ministre du budget prend la décision lorsque le montant du programme d'investissement dépasse 10 millions d'euros, lorsque le programme est réalisé dans plus d'un département d'outre-mer, à Saint-Martin, à Saint-Barthélemy, en Polynésie française, aux îles Wallis et Futuna, dans les Terres australes et antarctiques françaises, en Nouvelle-Calédonie ou à Saint-Pierre-et-Miquelon, ou lorsqu'il évoque l'affaire.</p>
<p>I bis. – Dans le secteur du logement, le directeur départemental ou le directeur régional des finances publiques du département dans lequel les logements sont réalisés délivre l'agrément prévu au 4 de l'article 199 undecies A, aux II quater et III de l'article 217 undecies et au VII de l'article 244 quater W du code général des impôts lorsque le montant total du programme immobilier est inférieur ou égal à 20 millions d'euros.</p>
<p>Le ministre du budget délivre l'agrément lorsque ce montant dépasse 20 millions d'euros ou lorsqu'il évoque le programme immobilier.</p>
<p>I ter. – Les montants mentionnés au I et au I bis sont appréciés par programme, toutes taxes, frais et commissions compris.</p>
<p>II. – Les demandes d'agrément mentionnées au premier alinéa du I et au premier alinéa du I bis sont adressées au directeur départemental ou au directeur régional des finances publiques du département dans lequel le programme d'investissement sera réalisé.</p>
<p>Les demandes d'agrément mentionnées au second alinéa du I et au second alinéa du I bis sont adressées à la direction générale des finances publiques.</p>
<p>III. – Pour les programmes d'investissement placés sous le régime de la copropriété ou réalisés par l'une des sociétés ou l'un des groupements visés aux articles 8 ou 239 quater du code général des impôts, un représentant unique présente la demande d'agrément. Ce représentant, promoteur de l'opération, gérant ou associé, doit remettre une copie de la décision obtenue aux investisseurs, copropriétaires ou associés.</p>
<p>IV. – (Dispositions devenues sans objet).</p>
""",
    "Réécriture à droit constant : les autorités chargées de délivrer l'agrément deviennent les sujets des phrases ; les seuils, la compétence ministérielle, l'acheminement des demandes et les obligations du représentant unique sont formulés directement. Les neuf alinéas et les subdivisions I à IV, dont I bis et I ter, sont maintenus. La simplification administrative envisagée par policy.json ne modifie ici ni les conditions de l'agrément ni les compétences.",
    "Seuils de 10 et 20 millions d'euros, égalités incluses dans la compétence locale, calcul par programme toutes taxes, frais et commissions compris, secteurs, territoires et pouvoir d'évocation conservés. Les seuils de compétence ne doivent pas être confondus avec les seuils d'assujettissement à agrément des articles du CGI cités. La note source vise l'article 106-I [2°] de la loi n° 2016-1918 du 29 décembre 2016. Elle maintient, en application du II de l'article 11 de l'arrêté du 13 janvier 2020, les procédures applicables à leur présentation pour les demandes de décisions administratives individuelles présentées avant l'entrée en vigueur de cet arrêté ; cette transition demeure réservée. Les alinéas auxquels renvoie le II restent aux mêmes places."
)

add('170 undecies', """
<p>En application du III de l'article 347 de l'annexe III au code général des impôts, le nombre de suppléants de la commission des impôts directs et des taxes sur le chiffre d'affaires instituée aux articles 1651 et suivants du code général des impôts peut être augmenté dans les limites suivantes, si son président le juge utile :</p>
<p>1. Pour la ville de Paris :</p>
<p>a) Jusqu'à cent cinquante pour les représentants des contribuables désignés par la chambre de commerce et d'industrie territoriale ;</p>
<p>b) Jusqu'à cinquante pour les représentants des contribuables désignés par la chambre des métiers et de l'artisanat et par les organisations ou organismes professionnels regroupant les titulaires de revenus non commerciaux ;</p>
<p>2. Pour les départements de plus de 600 000 habitants dans le ressort du tribunal administratif, le nombre de suppléants peut, dans les mêmes conditions qu'au 1, être porté à soixante pour les représentants mentionnés au a du 1 et à trente pour ceux mentionnés au b du 1.</p>
""",
    "Réécriture à droit constant : la décision du président est rattachée à l'ensemble des plafonds et les deux plafonds départementaux sont explicitement associés aux catégories de représentants déjà définies au 1. Les subdivisions et les cinq alinéas sont conservés. Aucune réforme de fond de la composition des commissions n'est appliquée.",
    "Plafonds de cent cinquante et cinquante pour Paris, de soixante et trente pour les départements de plus de 600 000 habitants, et condition tenant au ressort du tribunal administratif conservés. Le III de l'article 347 de l'annexe III permet bien une modification par arrêté du nombre de suppléants. Le corpus marque l'article 1651 du CGI ABROGE_DIFF avec une fin de version au 1er janvier 2027 : vérifier la coordination de la commission pour les périodes ultérieures, sans anticiper cette évolution dans le présent texte. La note source vise l'article 87-1° du décret n° 2010-1463 du 1er décembre 2010 ; elle n'est pas une date de réforme future."
)

add('188 B', """
<p>Le régime fiscal prévu à l'article 1678 bis du code général des impôts s'applique aux intérêts des bons nominatifs, à ordre ou au porteur qui comportent ou valent engagement de payer et sont délivrés en contrepartie d'un prêt par les entreprises industrielles et commerciales ou par les personnes morales visées à l'article 108 du même code, quel que soit l'objet de ces personnes morales.</p>
<p>Si ces bons sont cotés en bourse ou susceptibles de l'être, ce régime reste applicable lorsque le paiement des intérêts n'a pas lieu sur présentation ou remise de coupons ou d'instruments représentatifs de coupons.</p>
<p>Lorsque le prêt a fait l'objet d'un contrat préalable, les écrits créés à seule fin de faciliter le recouvrement ou la mobilisation de la créance sont exclus du champ du premier alinéa.</p>
""",
    "Réécriture à droit constant : le champ des bons concernés est posé directement, puis la condition relative aux bons cotés et l'exclusion des écrits de recouvrement sont formulées séparément. Les trois alinéas sont maintenus. Les réformes de prélèvements salariaux et de retraite de policy.json ne sont pas étendues à ce régime de revenus mobiliers.",
    "Renvois aux articles 1678 bis et 108 du CGI vérifiés dans le corpus local et conservés. Maintien du prêt en contrepartie de l'émission, de l'indifférence de l'objet des seules personnes morales visées, du critère de présentation ou remise des coupons et de l'exclusion subordonnée à un contrat préalable et à la seule finalité de recouvrement ou de mobilisation. Aucun taux ni régime nouveau n'est introduit."
)

add('188 C', """
<p>Les personnes morales visées à l'article 108 du code général des impôts versent l'impôt afférent aux intérêts des bons de caisse au service des impôts destinataire de leur déclaration de résultat. À défaut d'une telle déclaration, elles le versent au service des impôts dont relève leur siège social.</p>
""",
    "Réécriture à droit constant : une seconde phrase, dans le même alinéa, isole le service compétent en l'absence de déclaration de résultat. Le redevable, l'impôt et la règle de rattachement sont inchangés ; aucune réforme de fond ne vise cette compétence dans policy.json.",
    "L'absence de déclaration de résultat, et non un simple retard de dépôt, demeure le critère subsidiaire de rattachement au siège social. Renvoi à l'article 108 du CGI conservé. " + APPLICATION_2018
)

add('188 D', """
<p>L'impôt sur les intérêts payés au cours d'un mois doit être acquitté dans les quinze premiers jours du mois suivant (1).</p>
<p>(1) Ces dispositions s'appliquent aux intérêts payés à compter de la date d'entrée en vigueur de l'arrêté.</p>
""",
    "Réécriture à droit constant : le mois de paiement des intérêts et le délai d'acquittement sont reliés dans une phrase plus directe. La note d'application déjà intégrée au source_xml est reproduite sous une forme clarifiée. Aucune réforme de fond du délai n'est appliquée.",
    "Délai des quinze premiers jours du mois suivant conservé ; il ne devient pas un délai de quinze jours à compter de chaque paiement. La note (1) reste attachée à la règle. L'arrêté auquel elle renvoie n'est pas identifié ni daté dans cet article : lacune historique conservée et signalée, sans lui substituer la date technique de début de version du corpus."
)

add('188 E', """
<p>Les entreprises qui paient les intérêts des bons de caisse doivent souscrire la déclaration prévue au 1 de l'article 242 ter du code général des impôts.</p>
""",
    "Réécriture à droit constant : l'obligation déclarative est exprimée par « doivent » et rattachée directement aux entreprises qui paient les intérêts. Aucune réforme de fond de cette déclaration de revenus mobiliers n'est prévue par policy.json.",
    "Le renvoi au 1 de l'article 242 ter du CGI, présent dans le corpus local, est conservé sans modifier son contenu, ses exclusions, ses modalités ou ses délais. Le champ reste limité ici aux entreprises assurant le paiement des intérêts des bons de caisse."
)

add('188 F', """
<p>Lors du paiement de l'impôt, les entreprises doivent fournir toutes les précisions nécessaires sur les caractéristiques de chaque catégorie de bons émis, sur le montant de l'intérêt stipulé ainsi que sur les dates et les modalités de paiement de cet intérêt.</p>
""",
    "Réécriture à droit constant : le moment de communication est placé en tête et les trois catégories de renseignements sont séparées par une ponctuation explicite. Aucune réforme de fond de l'obligation d'information n'est appliquée.",
    "Communication au moment du paiement de l'impôt maintenue. Aucune catégorie de renseignements n'est retranchée : caractéristiques de chaque catégorie de bons, montant de l'intérêt stipulé, époques et mode de paiement de l'intérêt. Aucune nouvelle périodicité ni dispense fondée sur la politique générale de réemploi des données n'est inventée."
)

add('188-0 H', """
<p>La retenue à la source prévue au 2 de l'article 119 bis du code général des impôts doit être versée au service des impôts destinataire de la déclaration de résultat du redevable. À défaut d'une telle déclaration, le versement est effectué au service des impôts dont relève le siège social du redevable.</p>
""",
    "Réécriture à droit constant : l'obligation de versement et la compétence subsidiaire sont présentées en deux phrases dans l'alinéa existant ; le titulaire du siège social est explicité. Aucune réforme de fond des dividendes ou de leur retenue n'est appliquée.",
    "Renvoi au seul 2 de l'article 119 bis du CGI et rattachement subsidiaire au siège social conservés. La baisse de CSG salariale privée de policy.json n'est pas transposée à cette retenue. " + APPLICATION_2018
)

add('188 H', """
<p>1. Les retenues opérées par les agences ou succursales des établissements de crédit ou des entreprises sont versées globalement. Pour chaque versement, l'organisme centralisateur établit et conserve un état indiquant le montant versé pour le compte de chaque agence ou succursale. Les liasses visées au 3 de l'article 17 A doivent être conservées soit par l'organisme centralisateur, soit par l'agence ou la succursale.</p>
<p>2. (Abrogé).</p>
""",
    "Réécriture à droit constant : les versements globaux, l'établissement de l'état et la conservation des liasses sont énoncés par des verbes directs dans le 1 existant. Le 2 abrogé est maintenu à sa place. Aucune réforme de fond du recouvrement n'est introduite.",
    "Les deux obligations d'établir et de conserver un état pour chaque versement sont conservées, avec le montant propre à chaque agence ou succursale. Le 3 de l'article 17 A du corpus prévoit bien les deux liasses ; son 4 organise leur conservation avec l'état de l'article 188 H. Le choix du détenteur des liasses n'est pas étendu à la conservation de l'état. " + APPLICATION_2018
)

add('188-0 I', """
<p>I. – Le prélèvement sur les produits de placements à revenu fixe prévu à l'article 125 A du code général des impôts, lorsqu'il est dû à raison des revenus, produits et gains mentionnés aux articles 125-0 A et 125 A du même code, doit être versé au service des impôts destinataire de la déclaration de résultat du redevable. À défaut d'une telle déclaration, le versement est effectué au service des impôts dont relève le redevable.</p>
<p>II. – Lorsque le prélèvement mentionné au I est dû à raison des revenus, produits et gains visés aux I et II de l'article 125 D du code général des impôts, il doit être versé :</p>
<p>1° À la recette des impôts des non-résidents de la direction des impôts des non-résidents, si la personne qui assure le paiement de ces revenus, produits et gains acquitte le prélèvement sur mandat du contribuable ;</p>
<p>2° Au service des impôts du domicile du contribuable, si celui-ci paie lui-même le prélèvement.</p>
""",
    "Réécriture à droit constant : le champ du I est rapproché du prélèvement et les deux destinataires du II sont associés explicitement à la personne qui paie. Les quatre alinéas et les subdivisions sont conservés. Aucune réforme de fond de la fiscalité des placements n'est appliquée.",
    "Renvois aux articles 125 A, 125-0 A et aux I et II de l'article 125 D du CGI conservés. Au I, le rattachement subsidiaire demeure celui du redevable, sans ajout d'un critère de siège social absent de la source. Au II, le mandat du contribuable reste requis au 1° et le domicile reste le critère du 2°. Les conditions propres à l'article 125 D demeurent applicables par renvoi, y compris les règles distinctes des contrats anciens. " + APPLICATION_2018
)

add('188 I', """
<p>Les prélèvements opérés par les agences et succursales des établissements de crédit, par les caisses publiques, par les caisses d'épargne ou par les succursales des entreprises sont versés globalement, dans les conditions prévues à l'article 188 H.</p>
<p>Cette règle ne s'applique pas au prélèvement dû à raison des revenus, produits et gains mentionnés à l'article 125 D du code général des impôts.</p>
""",
    "Réécriture à droit constant : l'énumération des organismes est ponctuée et le versement global est formulé directement ; l'exception demeure dans le second alinéa. Aucune réforme de fond des prélèvements mobiliers n'est introduite.",
    "Renvois aux articles 188 H et 125 D du CGI maintenus. Le champ vise les agences et succursales des établissements de crédit, mais seulement les succursales des entreprises : il n'est pas élargi à toutes les entreprises ni à leurs agences. L'exclusion porte sur les revenus, produits et gains de l'article 125 D dans leur ensemble. " + APPLICATION_2018
)

add('188 J', """
<p>Le recouvrement de l'impôt mentionné à l'article 381 K de l'annexe III au code général des impôts relève du service des impôts destinataire de la déclaration de résultat de la collectivité émettrice. À défaut d'une telle déclaration, il relève du service des impôts dont dépend le siège social de cette collectivité.</p>
""",
    "Réécriture à droit constant : le recouvrement est rattaché au service compétent dans une première phrase et le cas subsidiaire dans une seconde ; la collectivité tenue à la déclaration est explicitée. La construction grammaticale défectueuse de la fin de la phrase source est clarifiée sans changement de compétence. Aucune réforme de fond n'est appliquée.",
    "Renvoi à l'article 381 K de l'annexe III vérifié : celui-ci prévoit bien un service désigné par le ministre chargé du budget. Le service destinataire de la déclaration de résultat et, à défaut, celui du siège social de la collectivité émettrice restent compétents. " + APPLICATION_2018
)

add('188 K', """
<p>Le service auquel doit être versé le prélèvement prévu à l'article 117 quater du code général des impôts est déterminé comme suit :</p>
<p>1° Lorsque la personne mentionnée au b du III de l'article 117 quater du même code opère le prélèvement sur mandat du contribuable, il est versé à la recette des impôts des non-résidents de la direction des impôts des non-résidents ;</p>
<p>2° Lorsque la personne mentionnée au II de l'article 117 quater du même code opère le prélèvement, il est versé au service des impôts destinataire de sa déclaration de résultat ou, à défaut d'une telle déclaration, au service des impôts dont relève son siège social ;</p>
<p>3° Lorsque le contribuable paie lui-même le prélèvement, il le verse au service des impôts de son domicile.</p>
""",
    "Réécriture à droit constant : chaque branche de l'énumération commence par l'identification de la personne qui effectue le paiement, puis indique le service destinataire. Les quatre alinéas et les 1° à 3° sont maintenus. Aucune réforme de fond du prélèvement sur les dividendes n'est appliquée.",
    "Mandat au 1°, rattachement à la déclaration de résultat puis au siège social au 2°, domicile au 3° conservés. Imprécision préexistante : le « b du III » cité au 1° correspond, dans l'article 117 quater du corpus local, au b du 1 du III. Le renvoi source est conservé ; une correction formelle de ce renvoi doit être coordonnée explicitement. Aucun taux de prélèvement ni condition d'assujettissement de l'article 117 quater n'est modifié."
)

add('188 L', """
<p>Les prélèvements prévus à l'article 117 quater du code général des impôts et opérés par les agences et succursales des établissements de crédit, par les caisses publiques, par les caisses d'épargne et par les entreprises sont versés globalement, dans les conditions prévues à l'article 188 H.</p>
<p>Cette règle ne s'applique pas lorsque le prélèvement est acquitté dans les conditions du III de l'article 117 quater du même code.</p>
""",
    "Réécriture à droit constant : le versement global est exprimé directement et l'exception est reprise dans le second alinéa sans déplacement. Aucune réforme de fond du prélèvement sur les dividendes n'est introduite.",
    "Le champ comprend ici les entreprises, contrairement au champ plus étroit de l'article 188 I pour celles-ci ; cette différence est conservée. L'exclusion vise l'ensemble des paiements effectués dans les conditions du III de l'article 117 quater, sans être limitée aux seuls mandataires. Renvoi à l'article 188 H maintenu. " + APPLICATION_2018
)

add('190', """
<p>I. – Pour l'application du II de l'article 283 bis et du II de l'article 293 A ter du code général des impôts, le signalement que l'administration adresse à l'opérateur de plateforme en ligne comprend les informations suivantes :</p>
<p>1° Les éléments d'identification de l'assujetti concerné, définis au II du présent article ;</p>
<p>2° La description des obligations fiscales auxquelles l'administration présume que l'assujetti a manqué ;</p>
<p>3° Les périodes auxquelles se rapporte la défaillance présumée de l'assujetti ;</p>
<p>4° Les mesures que l'opérateur de plateforme en ligne doit mettre en œuvre, définies au III du présent article ;</p>
<p>5° L'indication des conséquences, en matière de responsabilité solidaire, de l'absence de mise en œuvre de ces mesures par l'opérateur de plateforme en ligne.</p>
<p>II. – Les éléments d'identification de l'assujetti prévus au 1° du I sont les suivants, dans la mesure où l'administration les connaît :</p>
<p>1° Sa raison sociale ;</p>
<p>2° Son nom commercial ou son nom d'utilisateur tel qu'il est communiqué sur la plateforme en ligne ;</p>
<p>3° L'identifiant que lui a fourni l'opérateur de plateforme en ligne ;</p>
<p>4° Son lieu d'établissement à la date du signalement ;</p>
<p>5° Son numéro de taxe sur la valeur ajoutée intracommunautaire ou, à défaut, ses numéros d'identification définis à l'article R. 123-221 du code de commerce ou, pour une entreprise non résidente, son numéro d'immatriculation auprès de l'administration fiscale de son pays de résidence.</p>
<p>III. – Les mesures que l'opérateur de plateforme en ligne doit mettre en œuvre en application du 4° du I sont les suivantes :</p>
<p>1° Rappeler à l'assujetti l'information fournie au titre du 1° de l'article 242 bis du code général des impôts ;</p>
<p>2° Demander à l'assujetti de prendre contact avec l'administration afin de régulariser sa situation fiscale ;</p>
<p>3° Le cas échéant, demander à l'assujetti de fournir son numéro de taxe sur la valeur ajoutée intracommunautaire ;</p>
<p>4° Le cas échéant, vérifier la validité du numéro de taxe sur la valeur ajoutée intracommunautaire de l'assujetti et, si ce numéro est invalide, lui demander de régulariser sa situation ;</p>
<p>5° Le cas échéant, demander à l'assujetti de désigner un représentant fiscal en France en application de l'article 289 A du code général des impôts.</p>
<p>En complément de ces mesures, l'opérateur de plateforme en ligne peut prendre toute autre mesure qu'il estime utile.</p>
""",
    "Réécriture à droit constant : le rôle de l'administration est explicité et les mesures obligatoires de l'opérateur sont formulées à l'infinitif dans les subdivisions existantes. Les dix-neuf alinéas, les données conditionnées à leur connaissance et les trois mentions « le cas échéant » sont conservés. La simplification administrative de policy.json ne justifie pas de supprimer les mesures de régularisation fiscale ou de créer une nouvelle collecte de données.",
    "Anomalie préexistante : le 1° du III vise le « 1° de l'article 242 bis », alors que l'article 242 bis du corpus local ne comporte plus de 1° dans sa version applicable depuis le 1er janvier 2023. Le renvoi est conservé et nécessite une coordination expresse. Les articles 283 bis et 293 A ter sont marqués ABROGE_DIFF avec une fin de version au 1er janvier 2027 dans le corpus ; contrôler la portée temporelle de l'arrêté d'application. L'article 289 A est également marqué ABROGE_DIFF ; aucune anticipation n'est faite. Le renvoi au code de commerce, hors des cinq codes, reste à contrôler. La note source vise les articles 3-3° et 45 du décret n° 2022-1014 du 19 juillet 2022. La défaillance demeure présumée ; seules les autres mesures prises en complément au dernier alinéa restent facultatives."
)

add('191', """
<p>L'opérateur de plateforme en ligne doit notifier à l'administration les mesures qu'il a mises en œuvre à la suite du signalement effectué en application du II de l'article 283 bis ou du II de l'article 293 A ter du code général des impôts. Il dispose pour cela d'un délai d'un mois à compter de la réception de ce signalement.</p>
<p>La notification comprend les informations suivantes :</p>
<p>1° Les éléments d'identification de l'assujetti prévus au II de l'article 190 que l'administration ne connaît pas et dont dispose l'opérateur de plateforme ;</p>
<p>2° La nature des mesures mises en œuvre ;</p>
<p>3° La date de mise en œuvre de ces mesures ;</p>
<p>4° Tout élément permettant d'établir la mise en œuvre effective des mesures par l'opérateur de plateforme en ligne ;</p>
<p>5° Le cas échéant, tout élément dont dispose l'opérateur de plateforme en ligne susceptible de permettre à l'administration de vérifier que l'assujetti a régularisé sa situation.</p>
""",
    "Réécriture à droit constant : l'obligation de notification précède le délai, exposé dans une seconde phrase du même alinéa ; la liste des informations est allégée sans perte de ses conditions. Les sept alinéas et les cinq rubriques sont conservés. Aucune réforme de fond du délai ou du contenu de la notification n'est appliquée.",
    "Délai d'un mois courant de la réception du signalement conservé. Le 1° ne vise que les éléments à la fois inconnus de l'administration et détenus par l'opérateur ; aucune obligation nouvelle de recherche n'est créée. La réserve « le cas échéant » et le critère de disponibilité du 5° sont maintenus. Les articles 283 bis et 293 A ter du CGI sont marqués ABROGE_DIFF avec fin de version au 1er janvier 2027 dans le corpus local : coordonner le maintien de cette procédure pour les périodes concernées. Le II de l'article 190 demeure à sa place."
)

add('192', """
<p>I. – Pour l'application du III de l'article 283 bis et du III de l'article 293 A ter du code général des impôts, la mise en demeure que l'administration adresse à l'opérateur de plateforme en ligne comprend les informations suivantes :</p>
<p>1° La date et la référence du signalement effectué en application du II de l'article 283 bis ou du II de l'article 293 A ter du même code ;</p>
<p>2° La description des motifs pour lesquels la présomption de défaillance de l'assujetti persiste ;</p>
<p>3° Les mesures supplémentaires que l'opérateur de plateforme en ligne doit mettre en œuvre ou la demande d'exclusion de l'assujetti ;</p>
<p>4° L'indication des conséquences, en matière de responsabilité solidaire, de l'absence de mise en œuvre de ces mesures supplémentaires ou d'exclusion de l'assujetti par l'opérateur de plateforme en ligne.</p>
<p>II. – Les mesures supplémentaires prévues au 3° du I sont les suivantes :</p>
<p>1° Toute mesure prévue au III de l'article 190 ;</p>
<p>2° Toute mesure permettant de suspendre l'activité de l'assujetti concerné en lien avec des transactions imposables à la taxe sur la valeur ajoutée en France.</p>
""",
    "Réécriture à droit constant : l'administration et l'opérateur sont identifiés comme auteurs des actes et les conséquences de l'inaction sont formulées directement. Les huit alinéas, le I et le II et leurs subdivisions sont conservés. Aucune réforme de fond de la responsabilité solidaire ou du champ des mesures n'est appliquée.",
    "Maintien de la présomption de défaillance, de l'alternative entre mesures supplémentaires et exclusion, du renvoi au III de l'article 190 et de la limitation de la suspension aux activités en lien avec des transactions imposables à la TVA en France. Les conditions permettant la mise en demeure restent celles des textes législatifs cités. Les articles 283 bis et 293 A ter du CGI sont marqués ABROGE_DIFF avec fin de version au 1er janvier 2027 dans le corpus local : coordination temporelle à contrôler sans suppression anticipée des obligations du présent article."
)

add('192 bis', """
<p>L'opérateur de plateforme en ligne doit notifier à l'administration la mise en œuvre des mesures supplémentaires définies au II de l'article 192 ou l'exclusion de l'assujetti. Il dispose pour cela d'un délai d'un mois à compter de la réception de la mise en demeure effectuée par l'administration en application du III de l'article 283 bis ou du III de l'article 293 A ter du code général des impôts.</p>
<p>La notification comprend les informations suivantes :</p>
<p>1° La nature des mesures supplémentaires mises en œuvre ;</p>
<p>2° La date de mise en œuvre de ces mesures supplémentaires ou la date à laquelle l'exclusion est effective ;</p>
<p>3° Tout élément permettant d'établir la mise en œuvre effective des mesures supplémentaires ou de l'exclusion de l'assujetti concerné ;</p>
<p>4° Le cas échéant, tout élément dont dispose l'opérateur de plateforme en ligne susceptible de permettre à l'administration de vérifier que l'assujetti a régularisé sa situation.</p>
""",
    "Réécriture à droit constant : l'obligation de notifier est présentée avant le délai et la liste distingue la nature des mesures, leur date et la preuve de leur exécution. Les six alinéas et les quatre rubriques sont maintenus. Aucune réforme de fond de la procédure de mise en demeure n'est introduite.",
    "Délai d'un mois courant de la réception de la mise en demeure, renvoi au II de l'article 192, alternative entre mesures et exclusion effective, preuve d'exécution et réserve du 4° conservés. Le 1° reste limité à la nature des mesures supplémentaires ; aucune rubrique nouvelle relative à l'exclusion n'y est ajoutée. Les articles 283 bis et 293 A ter du CGI sont marqués ABROGE_DIFF avec fin de version au 1er janvier 2027 dans le corpus local : la coordination temporelle demeure à contrôler."
)

add('193', """
<p>Sauf disposition contraire, le redevable peut payer en numéraire, par chèque bancaire ou postal selon les modalités fixées aux articles 199 à 204, ou par virement au compte de chèques postaux du receveur des impôts compétent.<br/><br/>Il peut aussi payer par mandat compte émis au profit de ce même receveur.</p>
""",
    "Réécriture à droit constant : le verbe « payer » remplace la périphrase « se libérer » et les quatre modes de paiement restent distingués. Le second développement reste dans le même paragraphe avec ses sauts de ligne. Aucune réforme de fond des moyens de paiement n'est appliquée.",
    "Réserve de dispositions contraires, numéraire, chèque bancaire ou postal, virement au compte de chèques postaux et mandat compte conservés ; aucun mode contemporain n'est substitué sans base. Dans la plage 199 à 204, le corpus local ne fournit pas d'article 203 : absence à contrôler sans supprimer le renvoi global. Anciennes appellations postales et comptables conservées. La note source, fondée sur l'article 51 du décret n° 2024-610 du 26 juin 2024, fixe l'entrée en vigueur de cette rédaction au 1er janvier 2025 ; elle ne vaut pas date d'entrée en vigueur d'une réforme projetée."
)

add('196 A', """
<p>Les assureurs doivent accompagner chaque versement mensuel de la taxe sur les conventions d'assurances d'une déclaration établie sur les formules mises à leur disposition par l'administration (1).</p>
<p>(1) Cette obligation s'applique aux versements effectués à compter du 1er décembre 1991.</p>
""",
    "Réécriture à droit constant : le lien entre chaque versement mensuel et la déclaration exigée est formulé directement ; la note intégrée à la source précise toujours le champ temporel de l'obligation. Aucune réforme de fond de la taxe sur les conventions d'assurances n'est appliquée.",
    "Maintien d'une déclaration à l'appui de chacun des versements mensuels et de l'usage des formules fournies par l'administration. La date du 1er décembre 1991 et l'appel (1) sont conservés. Aucune télédéclaration ni dispense de déclaration n'est ajoutée. Cette taxe distincte n'est pas modifiée par les orientations relatives aux cotisations vieillesse ou à l'épargne retraite."
)

add('198 quinquies', """
<p>Le comptable des impôts chargé du bureau dans le ressort duquel se situent les terrains et immeubles recouvre les droits et taxes d'enregistrement, les taxes assimilées ainsi que la taxe hypothécaire ou la taxe de publicité foncière exigibles lorsque devient caduc le régime fiscal de faveur appliqué à des mutations à titre onéreux de terrains à bâtir et d'immeubles assimilés.</p>
""",
    "Réécriture à droit constant : le comptable compétent devient le sujet de la phrase et le fait déclenchant le recouvrement est exprimé par une proposition verbale. L'alinéa et la liste des impositions sont conservés. L'orientation de baisse progressive des droits de mutation ne fixe aucun paramètre permettant de modifier ici ces sommes ou leur recouvrement.",
    "Maintien du critère territorial de situation des terrains et immeubles, des mutations à titre onéreux, de la caducité du régime de faveur et de toutes les catégories d'impositions citées. L'appellation historique « taxe hypothécaire » est conservée ; l'applicabilité de ces régimes anciens et la nomenclature du comptable doivent être contrôlées sans les supprimer silencieusement. La baisse projetée des droits de mutation exige des dispositions d'assiette, de taux, de transition et de compensation des collectivités ; le présent article de recouvrement ne les crée pas."
)

add('198 septies', """
<p>Les receveurs des impôts recouvrent les produits provenant des locations d'immeubles domaniaux bâtis, y compris les charges et taxes correspondantes. Ils recouvrent également les produits, y compris les charges et taxes correspondantes, provenant des cessions d'immeubles réalisées conformément à l'article R. 3211-32 du code général de la propriété des personnes publiques et à l'article 6 du décret n° 2011-1612 du 22 novembre 2011.</p>
""",
    "Réécriture à droit constant : deux phrases, dans le même alinéa, distinguent les produits locatifs des produits de cession et rendent explicite l'inclusion des charges et taxes pour chacun. Aucune réforme de fond du recouvrement domanial n'est appliquée.",
    "Le caractère bâti reste attaché aux immeubles domaniaux loués ; il n'est pas ajouté comme condition nouvelle aux cessions visées. Renvois à l'article R. 3211-32 du code général de la propriété des personnes publiques et à l'article 6 du décret n° 2011-1612 conservés ; ces textes, hors des cinq codes du corpus indiqué, nécessitent un contrôle de coordination. La note source cite également les articles 2 et 3-I [1°] de ce décret. L'ancienne dénomination « receveurs des impôts » est conservée sans réattribution de compétence inventée."
)

add('198 octies', """
<p>L'autorité administrative transmet au trésorier payeur général et au titulaire du permis de construire la fiche de liquidation des impositions dont la délivrance de ce permis constitue le fait générateur.</p>
<p>Elle transmet également une fiche modificative lorsqu'une modification du permis de construire ou de l'autorisation tacite de construire a une incidence sur l'assiette d'une taxe.</p>
""",
    "Réécriture à droit constant : les deux transmissions sont exprimées à la voix active et la condition d'incidence fiscale de la modification est rapprochée de la fiche modificative. Les deux alinéas sont maintenus. La coordination du dossier de permis envisagée par policy.json ne modifie pas ici les faits générateurs fiscaux ni les destinataires des fiches.",
    "Transmission au trésorier payeur général et au titulaire du permis conservée, ainsi que les modifications de permis ou d'autorisation tacite ayant une incidence sur l'assiette d'une taxe. L'ancienne dénomination « trésorier payeur général » et l'articulation avec les régimes fiscaux de construction encore applicables à certaines opérations antérieures nécessitent un contrôle ; aucun remplacement d'autorité ni basculement de fait générateur n'est effectué silencieusement. Ce texte de transmission ne crée ni un nouveau dossier d'autorisation ni un nouveau délai d'instruction."
)


assert len(SOURCES) == len(drafts) == 24
answer = []
for source in SOURCES:
    xml, reason, notes = drafts[source['number']]
    answer.append({
        'code_id': source['code_id'],
        'source_id': source['source_id'],
        'source_sha256': source['source_sha256'],
        'number': source['number'],
        'proposed_xml': xml,
        'reason': reason,
        'review_notes': notes,
        'status': 'rewrite_draft',
    })
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
