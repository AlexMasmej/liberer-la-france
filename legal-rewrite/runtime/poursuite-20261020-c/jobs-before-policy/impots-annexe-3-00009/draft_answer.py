import json
from pathlib import Path


drafts = {}


def article(number, proposed_xml, reason, review_notes):
    assert number not in drafts
    drafts[number] = {
        "proposed_xml": proposed_xml.strip(),
        "reason": reason,
        "review_notes": review_notes,
        "status": "rewrite_draft",
    }


article(
    "41 sexdecies F",
    """
<p>Le dépositaire des actifs du fonds doit remplir les obligations suivantes dans les conditions et sous les sanctions prévues aux articles 57 et 75 à 79 de l'annexe II au code général des impôts et aux articles 17 à 17 D de l'annexe IV au même code :</p>
<p>a) Établir, conformément aux articles 41 sexdecies C à 41 sexdecies E, le relevé des sommes payées destiné à l'administration fiscale et les certificats de crédit d'impôt à remettre aux bénéficiaires des répartitions ;</p>
<p>b) Conserver les pièces justificatives de chacun des paiements effectués, en application de l'article R. 87-1 du livre des procédures fiscales.</p>
""",
    "Réécriture à droit constant : les deux obligations du dépositaire sont formulées directement et les destinataires du relevé et des certificats sont distingués. Aucune réforme de fond n'est applicable à ces formalités dans le périmètre de policy.json.",
    "Les subdivisions a) et b), les renvois aux annexes II et IV, aux articles 41 sexdecies C à E et à l'article R. 87-1 du livre des procédures fiscales sont conservés. Les conditions et sanctions demeurent celles des textes cités ; aucun délai de conservation autonome n'est ajouté.",
)

article(
    "41 sexdecies G",
    """
<p>Les obligations définies aux articles 41 sexdecies A à 41 sexdecies F s'imposent au gérant d'un fonds commun de placement à risques, d'un fonds professionnel spécialisé relevant de l'article L. 214-37 du code monétaire et financier dans sa rédaction antérieure à l'ordonnance n° 2013-676 du 25 juillet 2013 modifiant le cadre juridique de la gestion d'actifs, ou d'un fonds professionnel de capital investissement. Elles s'imposent également au dépositaire des actifs du fonds lorsqu'il agit pour le compte du gérant.</p>
""",
    "Réécriture à droit constant : la phrase est scindée pour rendre plus lisible l'assujettissement du gérant et du dépositaire agissant pour son compte, sans changer les catégories de fonds. Aucune réforme de fond n'est introduite.",
    "Le renvoi à l'article L. 214-37 est maintenu dans sa rédaction antérieure à l'ordonnance n° 2013-676 du 25 juillet 2013. Cette référence historique ne doit pas être remplacée par le régime actuel d'autres fonds. L'alinéa unique et la portée du renvoi aux articles 41 sexdecies A à F sont conservés.",
)

article(
    "41 sexdecies H",
    """
<p>1. Pour l'application du sixième alinéa du 4° du 3 de l'article 158 du code général des impôts, les sociétés, organismes ou placements collectifs mentionnés à ce 4° ventilent leurs distributions ou répartitions entre la part éligible à l'abattement de 40 % prévu au 2° du 3 de cet article et la part non éligible. Lorsqu'ils n'ont pas la personnalité morale, cette obligation incombe à leur gérant ou à leur représentant à l'égard des tiers. Cette ventilation s'effectue sans préjudice des autres dispositions fiscales qui leur sont applicables.</p>
<p>Lors de la mise en paiement des distributions ou répartitions, cette ventilation est communiquée à l'établissement payeur soumis aux obligations de l'article 242 ter du code général des impôts. Elle est tenue à la disposition de l'administration fiscale ainsi que des actionnaires, des porteurs de parts et de tout établissement payeur soumis aux obligations de cet article qui en font la demande.</p>
<p>La part éligible à l'abattement de 40 % mentionnée au premier alinéa figure sur les rapports annuels ou semestriels prévus par le règlement général de l'Autorité des marchés financiers pour les sociétés, organismes ou placements collectifs mentionnés au a du 4° du 3 de l'article 158 du code général des impôts. Pour les organismes mentionnés au b du même 4°, elle figure sur les rapports annuels et semestriels mentionnés à l'article 27 de la directive 85/611/CEE du Conseil du 20 décembre 1985 portant coordination des dispositions législatives, réglementaires et administratives concernant certains organismes de placement collectif en valeurs mobilières (OPCVM).</p>
<p>2. Pour l'application du 1, les personnes mentionnées au premier alinéa du 1 prélèvent les revenus distribués ou répartis éligibles à l'abattement de 40 % prévu au 2° du 3 de l'article 158 du code général des impôts sur les revenus identifiés comme éligibles dans les conditions du 3. Elles respectent leurs obligations en matière de distribution de leurs bénéfices ou résultats.</p>
<p>3. Pour l'application du 1, les personnes mentionnées au premier alinéa du 1 identifient les revenus perçus selon qu'ils sont ou non éligibles à l'abattement de 40 % prévu au 2° du 3 de l'article 158 du code général des impôts, dans les conditions suivantes :</p>
<p>1° Elles identifient, sous leur propre responsabilité, la fraction éligible à l'abattement de 40 % prévu au 2° du 3 de l'article 158 du code général des impôts parmi les revenus distribuables ou à répartir qui n'ont pas été distribués ou répartis au 1er janvier 2005. Elles tiennent les justificatifs correspondants à la disposition de l'administration fiscale ;</p>
<p>2° Elles identifient la part éligible à l'abattement de 40 % mentionné au 1° parmi les revenus qu'elles perçoivent à compter du 1er janvier 2005.</p>
<p>4. Pour l'application du 1, les personnes mentionnées au premier alinéa du 1 établissent un état de suivi des revenus perçus et distribués ou répartis, conforme à un modèle établi par l'administration fiscale. Elles le produisent à toute demande de cette administration.</p>
""",
    "Réécriture à droit constant : les responsables de la ventilation, ses destinataires, les obligations de publication et les modalités d'identification et de suivi sont énoncés dans des phrases plus courtes. Les subdivisions et l'ordre des alinéas sont maintenus ; aucune réforme de fond ne modifie l'abattement ou les revenus concernés.",
    "Incohérence préexistante relevée dans le corpus : le premier alinéa vise le sixième alinéa du 4° du 3 de l'article 158, alors que la condition de ventilation figure au septième alinéa de ce 4° dans la version fournie du CGI ; le sixième traite des revenus reçus par intermédiaire. Le renvoi source est conservé et appelle une coordination expresse. Le renvoi historique à l'article 27 de la directive 85/611/CEE du 20 décembre 1985 est également conservé et sa coordination doit être contrôlée. Sont maintenus l'abattement de 40 %, les deux catégories de rapports (annuels ou semestriels pour le a ; annuels et semestriels pour le b), les deux situations au 1er janvier 2005 et les huit alinéas, dont le troisième est visé par l'article 41 sexdecies J.",
)

article(
    "41 sexdecies I",
    """
<p>Le contribuable qui perçoit des revenus distribués, directement ou indirectement par l'intermédiaire de sociétés ou organismes mentionnés au 4° du 3 de l'article 158 du code général des impôts, en déclare le montant dans les conditions prévues au 1 de l'article 170 du même code. Il distingue, parmi ces revenus, la part éligible à l'abattement de 40 % prévu au 2° du 3 de l'article 158.</p>
""",
    "Réécriture à droit constant : l'obligation de déclarer et celle de distinguer la part éligible sont exprimées dans deux phrases au sein du même alinéa. Aucune réforme de fond n'est introduite.",
    "Le champ des revenus distribués perçus directement ou indirectement, le renvoi au 1 de l'article 170 et l'abattement de 40 % prévu au 2° du 3 de l'article 158 sont conservés. La réforme de la CSG salariale ne s'applique pas à ces revenus de capitaux mobiliers.",
)

article(
    "41 sexdecies J",
    """
<p>Les contribuables qui perçoivent des revenus distribués ou répartis directement par des organismes de placement collectif en valeurs mobilières ou par des placements collectifs mentionnés au b du 4° du 3 de l'article 158 du code général des impôts tiennent à la disposition de l'administration fiscale l'état de suivi des distributions ou répartitions prévu au 4 de l'article 41 sexdecies H, ainsi que les rapports mentionnés au troisième alinéa du 1 du même article qui justifient cette ventilation. Les établissements payeurs soumis aux obligations de l'article 242 ter du code général des impôts sont également tenus de mettre ces documents à la disposition de l'administration fiscale.</p>
""",
    "Réécriture à droit constant : l'obligation documentaire des établissements payeurs est formulée expressément, après celle des contribuables. Le champ des organismes et des documents reste identique ; aucune réforme de fond n'est introduite.",
    "Les renvois au 4 et au troisième alinéa du 1 de l'article 41 sexdecies H sont conservés ; l'alinéa relatif aux rapports reste à la même place dans la proposition de cet article. Le renvoi historique à la directive que comporte cet alinéa appelle le contrôle signalé dans les notes de l'article 41 sexdecies H.",
)

article(
    "41 sexdecies K",
    """
<p>I. – La déclaration prévue à l'article 125 D du code général des impôts est souscrite sur un formulaire normalisé. Elle comporte les indications suivantes :</p>
<p>a. La nature et le montant des revenus, produits et gains pour lesquels l'option est exercée ;</p>
<p>b. Le montant du prélèvement dû ;</p>
<p>c. Le montant des contributions et prélèvements sociaux dus.</p>
<p>La déclaration indique également la dénomination et l'adresse de la personne mentionnée au IV de l'article 125 D, mandatée par le contribuable pour accomplir, en son nom et pour son compte, les formalités déclaratives et de paiement du prélèvement. Si la convention prévue au VI du même article est conclue, elle indique aussi le numéro d'identification de cette personne.</p>
<p>II. – La déclaration mentionnée au I est déposée auprès du service des impôts désigné par le ministre chargé du budget, dans les délais prévus au IV de l'article 125 D du code général des impôts. Elle est accompagnée du paiement des impôts dus.</p>
""",
    "Réécriture à droit constant : les mentions du formulaire, l'identification du mandataire et les modalités de dépôt et de paiement sont clarifiées en conservant les subdivisions. Aucune réforme de fond n'est apportée aux prélèvements ou à l'option.",
    "Décalage préexistant relevé : le a ne vise que les revenus, produits et gains pour lesquels une option est exercée, alors que l'article 125 D du CGI fourni dans le corpus prévoit aussi un prélèvement obligatoire au I et le mentionne au IV. Cette rédaction source est conservée ; une coordination du contenu du formulaire avec ces deux branches doit être examinée expressément. Les renvois aux IV et VI de l'article 125 D et au service désigné par le ministre sont maintenus, sans extension de l'option aux contrats ou primes hors de son champ.",
)

article(
    "41 sexdecies L",
    """
<p>La convention prévue au VI de l'article 125 D du code général des impôts organise les modalités de déclaration et de paiement des impôts définies à l'article 41 sexdecies K pour les personnes mentionnées au IV de l'article 125 D. Il s'agit des personnes mandatées par plusieurs contribuables pour accomplir ces formalités en leur nom et pour leur compte.</p>
<p>Cette convention doit être conforme au modèle délivré par l'administration.</p>
""",
    "Réécriture à droit constant : la désignation des mandataires de plusieurs contribuables est isolée dans une phrase explicative, sans changer les formalités couvertes par la convention. Aucune réforme de fond n'est introduite.",
    "Les deux alinéas et les renvois aux IV et VI de l'article 125 D ainsi qu'à l'article 41 sexdecies K sont conservés. Le modèle administratif reste obligatoire. La coordination du contenu déclaratif signalée pour l'article 41 sexdecies K n'est pas réglée implicitement par cette convention.",
)

article(
    "41 sexdecies M",
    """
<p>L'associé d'une société unipersonnelle d'investissement à risque qui bénéficie de l'exonération prévue à l'article 163 quinquies C bis du code général des impôts doit conserver l'état individuel mentionné à l'article 46 ter D. Il le conserve jusqu'à la fin de la troisième année suivant celle au titre de laquelle il a bénéficié de l'exonération.</p>
""",
    "Réécriture à droit constant : l'obligation de conservation est séparée de son échéance, au sein du même alinéa. L'exonération et sa durée documentaire ne font l'objet d'aucune réforme de fond.",
    "Les renvois aux articles 163 quinquies C bis et 46 ter D sont conservés. Le délai reste calculé jusqu'à la fin de la troisième année suivant l'année au titre de laquelle l'associé a bénéficié de l'exonération, et non trois ans à compter d'une date de perception.",
)

article(
    "41 septdecies H",
    """
<p>Pour l'application de l'article 150 ter du code général des impôts, la date de dénouement d'un contrat est celle à laquelle la position ouverte par ce contrat est définitivement clôturée.</p>
""",
    "Réécriture à droit constant : la règle est formulée comme une définition directe de la date de dénouement, sans modifier le fait retenu. Aucune réforme de fond n'est introduite.",
    "Le renvoi à l'article 150 ter et le caractère définitif de la clôture sont conservés. Aucune date de règlement, d'encaissement ou de clôture provisoire n'est substituée à cette date.",
)

article(
    "41 septdecies I",
    """
<p>Pour l'application de l'article 150 ter du code général des impôts, les contribuables déclarent le montant du profit net imposable ou de la perte nette, ainsi que les éléments nécessaires à leur détermination. Ils utilisent une déclaration conforme au modèle établi par l'administration.</p>
<p>Les contribuables qui demandent le report de pertes subies au cours des dix années antérieures indiquent sur cette déclaration le détail des pertes reportées, année par année.</p>
""",
    "Réécriture à droit constant : le contenu de la déclaration et l'emploi du modèle administratif sont énoncés séparément ; le suivi annuel des pertes est exprimé directement. Aucune réforme de fond ne modifie le report.",
    "Les deux alinéas sont conservés, ainsi que le renvoi à l'article 150 ter, le caractère net du profit ou de la perte et la période des dix années antérieures. Le détail par année reste exigé uniquement des contribuables qui demandent le report.",
)

article(
    "41 septdecies K",
    """
<p>Lorsqu'une société mentionnée à l'article 8 du code général des impôts sert d'intermédiaire pour des opérations sur des instruments financiers à terme entrant dans le champ de l'article 150 ter du même code, elle déclare à l'administration la quote-part des profits et des pertes correspondant aux droits de chacun de ses membres dans la société. Elle effectue cette déclaration selon les modalités prévues à l'article 242 ter E du même code.</p>
""",
    "Réécriture à droit constant : le rôle de la société déclarante et la ventilation entre ses membres sont formulés directement, puis les modalités de déclaration sont rappelées dans une seconde phrase. Aucune réforme de fond n'est introduite.",
    "Les renvois aux articles 8, 150 ter et 242 ter E sont conservés. La déclaration porte sur les profits comme sur les pertes et reste répartie selon les droits de chaque membre, sans remplacement par une répartition uniforme.",
)

article(
    "41 duovicies D",
    """
<p>En cas de rachat de parts d'un fonds commun de placement, le gérant du fonds ou le dépositaire de ses actifs agissant pour le compte du gérant tient à la disposition du propriétaire des parts les éléments nécessaires pour déterminer la valeur moyenne pondérée d'acquisition des parts rachetées.</p>
""",
    "Réécriture à droit constant : le fonds et les parts concernés sont identifiés dès le début de l'alinéa et l'obligation de mise à disposition est formulée directement. Aucune réforme de fond ne modifie la valeur d'acquisition.",
    "Le champ reste limité au rachat de parts. La qualité de dépositaire agissant pour le compte du gérant et la méthode de la valeur moyenne pondérée d'acquisition sont conservées ; aucune obligation de transmission automatique n'est ajoutée.",
)

article(
    "41 duovicies E",
    """
<p>Avant le 1er février de chaque année, le gérant du fonds commun de placement ou le dépositaire des actifs du fonds agissant pour le compte du gérant adresse à la direction départementale ou, le cas échéant, régionale des finances publiques désignée au premier alinéa de l'article 41 sexdecies A un document comportant les indications suivantes :</p>
<p>1° Lorsqu'un propriétaire de parts a détenu plus de 10 % des parts pendant une partie de l'année, la période de dépassement de cette limite de 10 %, l'identité et le domicile fiscal de l'intéressé mentionnés au 3° du I de l'article 49 E, ainsi que le nombre de parts qu'il détient ;</p>
<p>2° (Devenu sans objet)</p>
<p>3° Pour chaque propriétaire, le montant global des rachats de parts effectués à son profit au cours de l'année précédente, lorsque ce montant excède 1 500 € ;</p>
<p>4° Dans la même limite que celle fixée au 3°, la valeur globale des apports en nature de valeurs mobilières effectués par chaque propriétaire de parts ;</p>
<p>5° En cas de dissolution du fonds :</p>
<p>La date de dissolution ;</p>
<p>L'identité et l'adresse de chaque propriétaire de parts mentionné au 3° du I de l'article 49 E ;</p>
<p>Le nombre de parts dont il disposait et leur valeur pondérée d'acquisition ;</p>
<p>Le montant des attributions en espèces ou en nature lui revenant à la suite de la liquidation, à l'exclusion de celles qui présentent le caractère de revenus de capitaux mobiliers.</p>
""",
    "Réécriture à droit constant : l'échéance annuelle et le destinataire sont placés en tête ; les informations exigées dans chaque situation sont clarifiées sans changer leur ordre ni les alinéas. Aucune réforme de fond ne modifie les seuils ou les déclarations.",
    "Sont conservés le dépôt avant le 1er février, le dépassement strict de 10 %, le seuil strictement supérieur à 1 500 €, le 2° devenu sans objet et les renvois au premier alinéa de l'article 41 sexdecies A et au 3° du I de l'article 49 E. La formule source du 4° « Dans la même limite » est maintenue et appelle un contrôle de portée avec le seuil du 3°, sans transformation silencieuse en plafond. Au 5°, l'exclusion des revenus de capitaux mobiliers et l'expression source « valeur pondérée d'acquisition » sont maintenues.",
)

article(
    "41 duovicies F",
    """
<p>En cas de rachat ou de cession de parts d'un fonds commun de placement à risques, d'un fonds professionnel spécialisé relevant de l'article L. 214-37 du code monétaire et financier dans sa rédaction antérieure à l'ordonnance n° 2013-676 du 25 juillet 2013 modifiant le cadre juridique de la gestion d'actifs, ou d'un fonds professionnel de capital investissement, le gérant ou le dépositaire des actifs du fonds fournit au propriétaire des parts rachetées ou cédées tous les éléments nécessaires au calcul de la plus-value, notamment :</p>
<p>a. Les éléments permettant de déterminer la valeur moyenne pondérée d'acquisition des parts rachetées ou cédées ;</p>
<p>b. La date et le montant des rachats ou cessions de parts ;</p>
<p>c. (Abrogé)</p>
<p>Lorsque des parts sont cédées sans l'intervention du gérant, le cédant communique au gérant ou au dépositaire le nombre et la catégorie des parts cédées, l'identité et le domicile du cessionnaire, ainsi que la date et le montant de la cession.</p>
""",
    "Réécriture à droit constant : le champ des fonds est rattaché aux parts concernées et les obligations du gérant, du dépositaire et du cédant sont formulées directement. Aucune réforme de fond ne modifie le calcul de la plus-value ou les régimes historiques.",
    "La référence à l'article L. 214-37 dans sa rédaction antérieure à l'ordonnance n° 2013-676 du 25 juillet 2013 est conservée, de même que les subdivisions a, b et c abrogé. La liste des éléments de calcul demeure non exhaustive. L'information par le cédant reste liée à l'absence d'intervention du gérant et porte sur le domicile du cessionnaire, sans ajout de la qualification fiscale.",
)

article(
    "41 duovicies G",
    """
<p>Avant le 16 février de chaque année, le gérant ou le dépositaire des actifs d'un fonds commun de placement à risques, d'un fonds professionnel spécialisé relevant de l'article L. 214-37 du code monétaire et financier dans sa rédaction antérieure à l'ordonnance n° 2013-676 du 25 juillet 2013 modifiant le cadre juridique de la gestion d'actifs, ou d'un fonds professionnel de capital investissement, adresse un relevé des opérations de l'année précédente à la direction départementale ou, le cas échéant, régionale des finances publiques auprès de laquelle il souscrit sa déclaration de résultats. Ce relevé mentionne :</p>
<p>1° Pour chaque propriétaire, le montant global des cessions de parts qu'il a effectuées et des rachats opérés par le fonds ;</p>
<p>2° La valeur globale des apports en nature de titres effectués par chaque propriétaire de parts ;</p>
<p>3° Lorsqu'un propriétaire de parts a détenu plus de 10 % des parts pendant une partie de l'année, la période de dépassement de cette limite de 10 %, les renseignements le concernant mentionnés au 3° du I de l'article 49 E, ainsi que le nombre de parts qu'il détient ;</p>
<p>4° En cas de dissolution du fonds ou de distribution d'une partie de ses avoirs entraînant l'annulation d'une fraction des parts du fonds :</p>
<p>a. La date de dissolution ou de distribution des avoirs ;</p>
<p>b. Les renseignements mentionnés au 3° du I de l'article 49 E concernant chaque propriétaire de parts, ainsi que, en cas de dissolution, le nombre et la catégorie des parts dont il disposait avant celle-ci ou, en cas de distribution d'avoirs, le nombre de ses parts annulées, leur catégorie et leur valeur moyenne pondérée d'acquisition ;</p>
<p>c. Le montant des attributions en nature ou en espèces revenant à chaque propriétaire, à l'exclusion de celles qui présentent le caractère de revenus de capitaux mobiliers.</p>
<p>5° En cas de distribution d'une partie des avoirs du fonds sans annulation de parts :</p>
<p>a. La date de distribution ;</p>
<p>b. Les renseignements mentionnés au 3° du I de l'article 49 E concernant chaque propriétaire de parts, ainsi que le nombre et la catégorie des parts détenues ouvrant droit à la distribution et leur valeur moyenne pondérée d'acquisition ;</p>
<p>c. Le montant de la distribution en nature ou en espèces revenant à chaque propriétaire.</p>
<p>d. (Abrogé).</p>
""",
    "Réécriture à droit constant : l'échéance et le destinataire du relevé sont explicités ; les informations à fournir sont présentées en conservant l'ensemble des subdivisions et la distinction entre dissolution et distributions avec ou sans annulation de parts. Aucune réforme de fond n'est introduite.",
    "Le dépôt demeure antérieur au 16 février pour les opérations de l'année précédente ; le seuil est strictement supérieur à 10 %. La référence historique à l'article L. 214-37 antérieur à l'ordonnance n° 2013-676 du 25 juillet 2013 et les renvois au 3° du I de l'article 49 E sont conservés. Le 4° b maintient la distinction de la source entre parts détenues avant dissolution et parts annulées lors d'une distribution, sans étendre silencieusement les indications de valeur à la première branche. L'exclusion des revenus de capitaux mobiliers au 4° c n'est pas étendue au 5° c ; le 5° d abrogé et les treize alinéas sont maintenus.",
)

article(
    "41 duovicies-0 H",
    """
<p>I. – Pour l'application du 1° bis du II de l'article 150 U du code général des impôts, lorsqu'une exonération est demandée au titre de la cession à titre onéreux d'un logement, l'acte constatant cette cession comporte les mentions suivantes :</p>
<p>1° L'identité du bénéficiaire de l'exonération ;</p>
<p>2° Les droits de ce bénéficiaire sur le prix de cession ;</p>
<p>3° La fraction du prix de cession correspondant à ses droits qu'il destine au remploi pour l'acquisition ou la construction d'un logement affecté à sa résidence principale ;</p>
<p>4° Le montant de la plus-value exonérée.</p>
<p>II. – Les mentions prévues au I sont indiquées séparément pour chaque bénéficiaire de l'exonération.</p>
""",
    "Réécriture à droit constant : la condition de demande d'exonération est formulée directement et la fraction destinée au remploi est rattachée explicitement au bénéficiaire. Aucune réforme de fond ne modifie l'exonération.",
    "Le renvoi au 1° bis du II de l'article 150 U, les quatre mentions de l'acte et leur individualisation par bénéficiaire sont conservés. Aucun délai, montant ou nouveau cas d'exonération n'est ajouté. La réforme envisagée des droits de mutation ne modifie pas cette exonération de plus-value.",
)

article(
    "41 duovicies-0 H bis",
    """
<p>I. – Pour l'application du 7° du II de l'article 150 U du code général des impôts, constituent une réhabilitation lourde les travaux qui permettent aux bâtiments d'habitation collectifs, à leur issue, de satisfaire aux deux conditions suivantes :</p>
<p>1° Atteindre le niveau de performance énergétique et environnementale mentionné au 5° du I de l'article 1384 C bis du code général des impôts ;</p>
<p>2° Respecter les critères de sécurité d'usage, de qualité sanitaire et d'accessibilité définis au III de l'article 315 ter A de l'annexe III du même code.</p>
<p>II. – À l'issue des travaux, le respect des exigences et critères mentionnés au I est justifié, sur demande de l'administration, par la production des documents mentionnés au 2° du IV de l'article 315 ter A de l'annexe III au code général des impôts.</p>
""",
    "Réécriture à droit constant : la définition de la réhabilitation lourde fait apparaître le cumul des deux conditions et le moment de leur justification. Aucune réforme de fond ne modifie les exigences techniques ou le champ des bâtiments collectifs.",
    "Les I et II et les quatre alinéas sont maintenus. Les renvois au 7° du II de l'article 150 U, au 5° du I de l'article 1384 C bis et aux III et 2° du IV de l'article 315 ter A sont conservés. Le III de ce dernier article comporte aussi des cas dans lesquels certains critères ne sont pas exigés : le renvoi intégral est maintenu sans les supprimer. La justification reste demandée à l'issue des travaux, sans dépôt systématique nouveau ni assimilation à la voie de rénovation locative de vingt-quatre mois envisagée par policy.json.",
)

article(
    "41 duovicies H",
    """
<p>Pour l'application du III de l'article 150 VA du code général des impôts, seuls les frais suivants, supportés par le vendeur à l'occasion de la cession, peuvent être admis en diminution du prix de cession, sous réserve que leur montant soit justifié :</p>
<p>1° Les frais versés à un intermédiaire ou à un mandataire ;</p>
<p>2° Les frais liés aux certifications et diagnostics rendus obligatoires par la législation en vigueur au jour de la cession ;</p>
<p>3° Les indemnités d'éviction versées au preneur par le propriétaire qui vend le bien loué libre d'occupation ;</p>
<p>4° Les honoraires versés à un architecte pour des travaux permettant d'obtenir un accord préalable à un permis de construire ;</p>
<p>5° Les frais exposés par le vendeur d'un immeuble pour obtenir d'un créancier la mainlevée de l'hypothèque grevant cet immeuble.</p>
""",
    "Réécriture à droit constant : l'alinéa introductif rattache directement la liste limitative des cinq catégories de frais à leur déduction et à la justification de leur montant. Aucune réforme de fond ne modifie le prix de cession ou les dépenses admises.",
    "Le renvoi au III de l'article 150 VA et les cinq catégories sont conservés. Le caractère obligatoire des certifications et diagnostics reste apprécié au jour de la cession ; les qualifications relatives à l'éviction, à l'accord préalable au permis et à la mainlevée de l'hypothèque sont maintenues.",
)

article(
    "41 duovicies I",
    """
<p>I. – Pour l'application du II de l'article 150 VB du code général des impôts, seuls les frais suivants, supportés par le vendeur lors de l'acquisition du bien cédé, peuvent être admis en majoration du prix d'acquisition, sous réserve que leur montant soit justifié :</p>
<p>1° Lorsque le bien ou le droit cédé a été acquis à titre gratuit, les droits de mutation payés et les frais d'acte et de déclaration afférents à ce bien ou droit, ainsi que, le cas échéant, les frais de timbre et de publicité foncière. Les droits de mutation sont pris en compte à proportion de la fraction de leur valeur représentative des biens ou droits ;</p>
<p>2° Lorsque le bien ou le droit cédé a été acquis à titre onéreux, les frais et coûts du contrat prévus à l'article 1699 du code civil et les droits d'enregistrement ou la TVA effectivement supportés par le contribuable.</p>
<p>II. – En cas de cession d'une partie d'un bien ou d'un droit immobilier, les frais d'acquisition sont retenus dans la même proportion que le prix d'acquisition lui-même.</p>
""",
    "Réécriture à droit constant : la condition de justification et la liste limitative sont rendues plus directes ; les acquisitions à titre gratuit et à titre onéreux ainsi que la règle proportionnelle restent distinctes. Aucune réforme de fond ne modifie les droits de mutation ou la TVA.",
    "Les I, 1°, 2° et II ainsi que les renvois au II de l'article 150 VB et à l'article 1699 du code civil sont conservés. La formulation source de la proportion des droits de mutation au 1° reste inchangée sur le fond et appelle un contrôle de son application à l'ensemble transmis ; aucune assiette nouvelle n'est fixée. La règle du II relative à une partie de bien ou à un droit immobilier est maintenue, sans taux ni calendrier de baisse des droits de mutation inventé.",
)

article(
    "41 duovicies J",
    """
<p>I. – Pour l'application de l'article 150 VH bis du code général des impôts, le redevable porte sur l'annexe prévue au V de cet article les informations suivantes, pour chaque cession à titre onéreux de crypto-actifs imposable en vertu des I et II du même article :</p>
<p>1° Le prix de cession défini au A du III de l'article 150 VH bis, en précisant :</p>
<p>a) Le cas échéant, les frais qu'il a supportés à l'occasion de cette cession ;</p>
<p>b) Le cas échéant, la soulte qu'il a reçue ou versée lors de cette cession ;</p>
<p>2° Le prix total d'acquisition du portefeuille de crypto-actifs défini au B du III de l'article 150 VH bis du code général des impôts, en précisant :</p>
<p>a) La somme des prix et valeurs d'acquisition à retenir ;</p>
<p>b) Le cas échéant, la somme des fractions de capital initial contenues dans la valeur ou le prix de chacune des cessions de crypto-actifs ou de droits s'y rapportant réalisées antérieurement, à titre gratuit ou onéreux, à l'exclusion des échanges non imposés en application du A du II de l'article 150 VH bis ;</p>
<p>c) Le cas échéant, le montant de chaque soulte reçue par le cédant lors d'échanges réalisés avant la cession imposable ;</p>
<p>3° La valeur globale du portefeuille de crypto-actifs définie au C du III de l'article 150 VH bis, évaluée au moment de cette cession ;</p>
<p>4° Le montant de la plus-value ou de la moins-value réalisée au titre de cette cession.</p>
<p>II. – Le redevable indique sur la même annexe la somme de l'ensemble des plus-values et moins-values réalisées au cours de l'année d'imposition au titre des cessions imposables.</p>
<p>III. – Pour les cessions exonérées en application du B du II de l'article 150 VH bis du code général des impôts, le contribuable porte sur l'annexe mentionnée au I uniquement les informations prévues au 1° de ce I.</p>
<p>IV. – Lorsque la cession mentionnée au I est réalisée par l'intermédiaire d'une personne interposée, le redevable porte sur l'annexe mentionnée au I uniquement la quote-part de la plus-value ou de la moins-value correspondant à ses droits, telle que la personne interposée l'a déclarée en application de l'article 41 duovicies K.</p>
<p>V. – Sur demande de l'administration, le contribuable fournit, dans les trente jours suivant cette demande, les pièces justifiant les informations mentionnées aux I à IV. Ces pièces justifient notamment les dates et les prix ou valeurs d'acquisition retenus pour calculer la somme mentionnée au b du 2° du I.</p>
""",
    "Réécriture à droit constant : les composantes déclaratives du prix de cession et du prix total d'acquisition, les deux modalités déclaratives particulières et la communication des justificatifs sont formulées plus directement. Toutes les subdivisions sont conservées ; aucune réforme de fond ne modifie l'imposition des crypto-actifs.",
    "Les I à V, les 1° à 4°, les lettres et les quatorze alinéas sont maintenus. Sont conservés les soultes reçues ou versées, les cessions antérieures gratuites ou onéreuses, l'exclusion des échanges non imposés, l'évaluation du portefeuille au moment de la cession, la déclaration limitée des cessions exonérées, la seule quote-part en cas de personne interposée et le délai de trente jours. Les renvois aux A, B et C du III, aux A et B du II et au V de l'article 150 VH bis sont maintenus et cohérents avec l'article du corpus. La note source attribue la modification à l'article 26-2° de l'ordonnance n° 2024-936 du 15 octobre 2024 ; cette donnée historique n'est pas transformée en date d'une réforme future. La coordination avec l'article 41 duovicies K est conservée.",
)

article(
    "41 duovicies K",
    """
<p>I. – Les sociétés ou groupements qui réalisent, en qualité de personnes interposées, des opérations mentionnées à l'article 150 VH bis du code général des impôts indiquent, sur une annexe conforme au modèle établi par l'administration, les informations prévues à l'article 41 duovicies J, dans les conditions fixées par cet article. Ils indiquent également la répartition entre chacun de leurs associés ou membres de l'assiette imposable au titre de l'article 150 VH bis.</p>
<p>II. – Sur demande de l'administration, ces sociétés ou groupements produisent, dans les trente jours suivant cette demande, tout élément permettant de justifier les informations mentionnées au I.</p>
""",
    "Réécriture à droit constant : la déclaration des personnes interposées, la répartition de l'assiette entre associés ou membres et la communication des justificatifs font l'objet de phrases distinctes. Les I et II restent séparés ; aucune réforme de fond n'est introduite.",
    "Les renvois aux articles 150 VH bis et 41 duovicies J, le modèle administratif et le délai de trente jours suivant la demande sont conservés. Le renvoi source « au titre de cet article » est explicité par l'article 150 VH bis, qui définit l'assiette, l'article 41 duovicies J définissant ses informations déclaratives. La déclaration par l'interposé reste coordonnée avec la seule quote-part exigée du redevable au IV de l'article 41 duovicies J.",
)

article(
    "41 tervicies",
    """
<p>Sur la déclaration prévue au 1 de l'article 170 du code général des impôts, établie l'année suivant celle du transfert de son domicile fiscal hors de France, le contribuable indique le montant total des plus-values latentes, des créances issues d'une clause de complément de prix et des plus-values en report, imposables en application des premier et deuxième alinéas du 1 du I et du II de l'article 167 bis du même code.</p>
<p>Sur un formulaire distinct, il précise la date du transfert de son domicile fiscal hors de France, l'adresse de son nouveau domicile fiscal, le montant des plus-values latentes, des créances issues d'une clause de complément de prix et des plus-values en report, ainsi que les éléments nécessaires à leur détermination.</p>
<p>Le contribuable dépose le formulaire mentionné au deuxième alinéa à l'appui de la déclaration mentionnée au premier alinéa, auprès du service des impôts des particuliers dont dépendait son domicile fiscal en France avant le transfert.</p>
""",
    "Réécriture à droit constant : le contribuable est désigné comme sujet des trois obligations et la déclaration annuelle est distinguée du formulaire détaillé qui l'accompagne. Aucune réforme de fond ne modifie l'imposition liée au transfert du domicile fiscal.",
    "Les trois alinéas sont maintenus dans leur ordre, notamment le deuxième, visé par l'article 41 tervicies A. Sont conservés l'année suivant le transfert, les trois catégories de sommes, les renvois au 1 de l'article 170 et aux premier et deuxième alinéas du 1 du I et au II de l'article 167 bis, ainsi que la compétence du service de l'ancien domicile fiscal français.",
)

article(
    "41 tervicies A",
    """
<p>Le contribuable qui souhaite bénéficier du sursis de paiement prévu au V de l'article 167 bis du code général des impôts le demande sur le formulaire mentionné au deuxième alinéa de l'article 41 tervicies.</p>
<p>Il dépose ce formulaire auprès du service des impôts des particuliers non résidents, au plus tard quatre-vingt-dix jours avant le transfert de son domicile fiscal hors de France.</p>
<p>Il y indique le nom ou la dénomination sociale et l'adresse de son représentant fiscal. Sur ce même document, le représentant s'engage à représenter le contribuable dans les conditions prévues au quatrième alinéa du V de l'article 167 bis du code général des impôts.</p>
""",
    "Réécriture à droit constant : les démarches du contribuable et l'engagement du représentant sont exprimés avec des sujets explicites, en conservant les trois alinéas. Aucune réforme de fond ne modifie le sursis ou son anticipation.",
    "Le champ reste celui du sursis demandé au titre du V de l'article 167 bis, sans extension au sursis du IV. Le délai d'au plus tard quatre-vingt-dix jours avant le transfert, le service des non-résidents, l'engagement sur le même formulaire et les renvois au deuxième alinéa de l'article 41 tervicies et au quatrième alinéa du V de l'article 167 bis sont maintenus.",
)

article(
    "41 tervicies B",
    """
<p>Lorsque le contribuable bénéficie du sursis de paiement prévu au IV ou au V de l'article 167 bis du code général des impôts, l'impôt afférent aux plus-values latentes, aux créances issues d'une clause de complément de prix et aux plus-values en report fait l'objet d'une mise en recouvrement spécifique. Le service des impôts des particuliers non résidents prend en charge les rôles correspondants.</p>
""",
    "Réécriture à droit constant : la mise en recouvrement spécifique et la prise en charge des rôles sont énoncées dans deux phrases au sein du même alinéa, avec désignation explicite du service responsable. Aucune réforme de fond n'est introduite.",
    "Les deux fondements du sursis, IV et V de l'article 167 bis, et les trois catégories de sommes concernées sont conservés. La prise en charge demeure attribuée au service des impôts des particuliers non résidents, sans fusion avec le service de dépôt prévu à l'article 41 tervicies.",
)


if __name__ == "__main__":
    sources = json.loads(Path("source.json").read_text())
    assert len(sources) == 24
    assert set(drafts) == {s["number"] for s in sources}
    result = []
    for source in sources:
        item = {key: source[key] for key in ("code_id", "source_id", "source_sha256", "number")}
        item.update(drafts[source["number"]])
        result.append(item)
    Path("answer.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"answer.json : {len(result)} articles")
