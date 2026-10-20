import json
from pathlib import Path


drafts = {}


def add(number, xml, reason, notes):
    assert number not in drafts
    drafts[number] = (xml.strip(), reason, notes)


add(
    'L114-19-1',
    '''<p>Les entreprises mentionnées à l'article 242 bis du code général des impôts doivent informer les personnes qui réalisent des transactions commerciales par leur intermédiaire des obligations sociales qui en résultent. Elles fournissent cette information dans les conditions fixées par le même article.</p>
<p>L'administration fiscale transmet à l'Agence centrale des organismes de sécurité sociale et à la Caisse nationale des allocations familiales le document mentionné au I de l'article 1649 ter A du code général des impôts ainsi que les informations similaires reçues d'autres États. Elle effectue cette transmission au plus tard le 31 décembre de l'année au cours de laquelle elle a reçu le document ou les informations. Elle y joint les informations permettant de faciliter l'identification de chaque vendeur ou prestataire et les échanges avec eux, selon des modalités définies par un décret en Conseil d'État pris après avis de la Commission nationale de l'informatique et des libertés. Les données ainsi obtenues peuvent être interconnectées avec celles des organismes mentionnés aux articles L. 212-1, L. 213-1 et L. 752-1 du présent code, pour l'accomplissement des missions de contrôle, de vérification et de lutte contre le travail dissimulé de ces organismes.</p>''',
    "Réécriture à droit constant : distinction entre l'information due par les entreprises et la transmission assurée par l'administration fiscale ; décomposition du calendrier, des données d'identification et de la faculté d'interconnexion. Aucune réforme de fond n'est appliquée à ces échanges.",
    "Les renvois aux articles 242 bis et 1649 ter A du CGI ont été rapprochés des sources du corpus. Maintien des deux destinataires, du 31 décembre de l'année de réception, des trois finalités et de l'avis de la CNIL. La note source fixe l'entrée en vigueur au 1er janvier 2024, en application du A du II de l'article 6 de la loi n° 2023-1250 du 26 décembre 2023 ; elle ne date aucune réforme future. Les deux alinéas sont conservés.",
)

add(
    'L114-20',
    '''<p>Le droit de communication défini à l'article L. 114-19 s'exerce dans les conditions prévues à la section 1 du chapitre II du titre II du livre des procédures fiscales et auprès des personnes qui y sont mentionnées. Sont toutefois exclues les personnes mentionnées aux articles L. 82 C, L. 83 A, L. 84, L. 84 A, L. 91, L. 95 et L. 96 B à L. 96 F de ce livre. Les autres dispositions législatives applicables aux échanges d'informations demeurent applicables.</p>''',
    "Réécriture à droit constant : présentation successive du régime applicable, des personnes exclues et du maintien des autres dispositions législatives. Aucune réforme de fond du droit de communication.",
    "Le renvoi à L. 114-19 est maintenu, ainsi que la section du livre des procédures fiscales et chacune des exclusions, notamment la plage L. 96 B à L. 96 F. L'article reste constitué d'un seul alinéa.",
)

add(
    'L114-20-1',
    '''<p>Les organismes mentionnés aux articles L. 213-1 et L. 752-4 du présent code et à l'article L. 725-3 du code rural et de la pêche maritime transmettent à l'organisme unique mentionné au deuxième alinéa de l'article L. 123-33 du code de commerce des informations concernant les personnes qui exercent un travail dissimulé au sens des articles L. 8221-3 et L. 8221-5 du code du travail. Cette transmission s'effectue dans les conditions prévues au 2° de l'article L. 123-50 du code de commerce. Elle porte sur les seules informations strictement nécessaires à l'immatriculation de ces personnes au registre prévu à l'article L. 123-36 du même code ou, lorsqu'elles sont déjà immatriculées, à une inscription modificative relative à l'activité ou à l'établissement concerné.</p>
<p>Un décret en Conseil d'État définit les informations mentionnées au premier alinéa du présent article.</p>''',
    "Réécriture à droit constant : identification explicite des personnes concernées, séparation des conditions de transmission et de la limitation aux informations strictement nécessaires. Aucune réforme de fond ni extension du partage de données.",
    "Conservation des trois catégories d'organismes émetteurs, du guichet unique désigné au deuxième alinéa de L. 123-33, du 2° de L. 123-50 et du registre de L. 123-36 du code de commerce. L'immatriculation et l'inscription modificative restent deux cas distincts ; le renvoi au premier alinéa demeure exact.",
)

add(
    'L114-21',
    '''<p>Lorsqu'un organisme a exercé le droit de communication prévu à l'article L. 114-19 et décide de supprimer le service d'une prestation ou de mettre des sommes en recouvrement, il doit informer la personne physique ou morale concernée de la teneur et de l'origine des informations et documents obtenus auprès de tiers sur lesquels il a fondé sa décision. Si cette personne le demande, l'organisme lui communique une copie de ces documents avant la mise en recouvrement ou la suppression du service de la prestation.</p>''',
    "Réécriture à droit constant : formulation des obligations de l'organisme à partir de la décision prise et désignation explicite du bénéficiaire de l'information et de la copie. Aucune réforme de fond des garanties contradictoires.",
    "Maintien de la distinction entre l'information obligatoire et la copie fournie sur demande. La copie doit toujours précéder le recouvrement ou la suppression du service de la prestation ; la source ne fixe pas ici de délai chiffré supplémentaire. Le renvoi à L. 114-19 et l'alinéa unique sont conservés.",
)

add(
    'L114-22',
    '''<p>Les organismes chargés de la gestion d'un régime obligatoire de sécurité sociale et du recouvrement des cotisations de sécurité sociale ou du service des allocations et prestations mentionnées au présent code, ainsi que l'opérateur France Travail, peuvent échanger des données à caractère personnel, y compris des données relatives aux revenus des personnes, avec les organismes et institutions chargés de gérer un régime équivalent dans un État membre de l'Union européenne, dans un autre État partie à l'accord sur l'Espace économique européen ou dans un État inscrit sur une liste fixée par voie réglementaire. Dans ce dernier cas, cet État doit imposer à ses organismes et institutions des conditions de protection des données à caractère personnel équivalentes à celles qui existent en France. Ces échanges ont les finalités suivantes :</p>
<p>1° Déterminer la législation applicable et prévenir ou sanctionner le cumul indu de prestations ;</p>
<p>2° Déterminer l'éligibilité aux prestations et contrôler le droit au bénéfice de prestations lié à la résidence, à l'appréciation des ressources, à l'exercice ou non d'une activité professionnelle et à la composition de la famille ;</p>
<p>3° Recouvrer les cotisations et contributions dues et contrôler leur assiette.</p>''',
    "Réécriture à droit constant : séparation de la liste des États et de la condition de protection équivalente applicable aux États inscrits sur la liste réglementaire. Les trois finalités numérotées sont conservées. Aucune réforme de fond des échanges internationaux.",
    "Maintien de France Travail, des données de revenus, de la notion de régime équivalent et des quatre critères du 2°. La note source prévoit l'entrée en vigueur au 1er janvier 2024 conformément au V de l'article 6 de la loi n° 2023-1196 du 18 décembre 2023. Aucune date future n'en est déduite. Les 1° à 3° restent dans leur ordre et à leur place.",
)

add(
    'L114-22-1',
    '''<p>Les employeurs qui relèvent d'un régime de protection sociale agricole sont soumis aux dispositions de l'article L. 243-15.</p>''',
    "Réécriture à droit constant : les employeurs agricoles deviennent le sujet explicite de la règle d'application par renvoi. Aucune réforme de fond du régime agricole.",
    "Le contenu de L. 243-15 a été consulté dans le corpus ; le renvoi intégral est conservé, sans en extraire une obligation isolée ni supprimer ses exceptions. Les réformes de cotisations et de retraite du premier champ privé non agricole ne sont pas étendues ici.",
)

add(
    'L114-22-2',
    '''<p>Lorsqu'une personne fait l'objet d'une condamnation pénale définitive à une peine complémentaire la privant de droits ou de prestations prévus par le présent code et par le code de l'action sociale et des familles, le ministère public près la juridiction pénale qui a prononcé cette condamnation en informe sans délai la caisse nationale mentionnée au second alinéa du présent article. Il tient également cette caisse informée de l'actualisation des informations relatives aux modalités d'exécution de la peine.<br/><br/>L'une des caisses nationales mentionnées au livre II met en œuvre un traitement automatisé, selon des modalités précisées par voie réglementaire. Ce traitement assure la réception et la conservation des informations transmises par le ministère public sur les peines mentionnées au premier alinéa du présent article. Il assure aussi leur utilisation par les seuls organismes de sécurité sociale et de retraite complémentaire dont relèvent les personnes concernées.</p>''',
    "Réécriture à droit constant : identification du ministère public comme auteur de l'information et séparation des fonctions du traitement automatisé. Aucune réforme de fond des peines, des destinataires ou de l'accès aux données.",
    "La condamnation doit rester définitive et porter sur une peine complémentaire. L'information sans délai et son actualisation sont conservées. Les deux alinéas textuels, séparés par le double saut de ligne de la source, gardent leur place pour les renvois réciproques au premier et au second alinéa. L'usage des données demeure réservé aux organismes dont relève la personne.",
)

add(
    'L114-22-2-1',
    '''<p>La présente section s'applique également aux sommes soumises à l'impôt sur le revenu en application de l'article 1649 quater-0 B bis du code général des impôts. Ces sommes sont notamment prises en compte dans les ressources du bénéficiaire lorsqu'une prestation ou une allocation est attribuée sous condition de ressources ou lorsque son montant est réduit en fonction de celles-ci.</p>''',
    "Réécriture à droit constant : séparation du champ d'application de la section et de son effet sur les prestations soumises aux ressources. Aucune réforme de fond de l'imposition ou des prestations.",
    "L'article 1649 quater-0 B bis du CGI a été consulté dans le corpus. Le renvoi reste intégral : la rédaction ne crée ni présomption fiscale supplémentaire ni règle nouvelle de montant. Les deux hypothèses, condition de ressources et réduction en fonction des ressources, sont maintenues, ainsi que le caractère non exhaustif de l'exemple introduit par « notamment ».",
)

add(
    'L114-22-3',
    '''<p>I. – Les agents de contrôle mentionnés à l'article L. 114-10 du présent code, à l'article L. 724-7 du code rural et de la pêche maritime et à l'article L. 5312-13-1 du code du travail sont habilités, lorsqu'ils sont commissionnés par le directeur général ou le directeur de l'organisme national dont relève l'organisme qui les emploie, à rechercher et à constater les infractions mentionnées aux articles 313-1, 313-3, 441-1, 441-6 et 441-7 du code pénal lorsqu'elles sont de nature à porter préjudice aux organismes de protection sociale, ainsi que les infractions mentionnées aux articles L. 114-13 et L. 114-18 du présent code. Les agents de contrôle employés par l'organisme mentionné à l'article L. 382-17 du présent code ou par l'un des organismes gestionnaires des régimes spéciaux mentionnés à l'article L. 711-1 ou du régime spécial des clercs et employés de notaires disposent de la même habilitation lorsqu'ils sont commissionnés par le directeur de cet organisme.</p>
<p>Pour accomplir ces missions, ces agents sont compétents sur l'ensemble du territoire national.</p>
<p>Les agents constatent les infractions par des procès-verbaux qui font foi jusqu'à preuve du contraire. Ces procès-verbaux sont transmis directement au procureur de la République.</p>
<p>II. – Lorsque les nécessités de l'enquête le justifient, ces agents peuvent, sans être pénalement responsables, accomplir sous pseudonyme les actes suivants, aux seules fins de constater les infractions mentionnées au I commises par la voie des communications électroniques :</p>
<p>1° Participer à des échanges électroniques, y compris avec les personnes susceptibles d'être les auteurs de ces infractions ;</p>
<p>2° Extraire ou conserver, par ce moyen, les données relatives aux personnes susceptibles d'être les auteurs de ces infractions et tout élément de preuve.</p>
<p>Ces actes ne doivent pas constituer une incitation à commettre une infraction, à peine de nullité.</p>
<p>III. – Ces agents peuvent également recueillir tout renseignement et toute justification nécessaires à l'accomplissement de leur mission. Ils peuvent se faire remettre copie des documents de toute nature nécessaires à cette mission, quel que soit leur support et quelle que soit la personne qui les détient. En cas de support informatisé, ils peuvent accéder aux logiciels et aux données stockées correspondants ainsi qu'à la restitution en clair des informations propres à faciliter l'accomplissement de leur mission. Ils peuvent demander que ces informations soient transcrites, par tout traitement approprié, en documents directement utilisables pour les besoins de leur mission.</p>
<p>IV. – Ces agents peuvent aussi entendre, sur convocation ou sur place, toute personne susceptible d'apporter des éléments utiles à leurs constatations. Ils dressent un procès-verbal de l'audition, qui doit comporter les questions auxquelles il a été répondu. Les personnes entendues lisent elles-mêmes ce procès-verbal, peuvent y faire consigner leurs observations et le signent. Lorsqu'elles déclarent ne pas pouvoir lire, l'agent leur en donne lecture avant la signature. Tout refus de signer est mentionné sur le procès-verbal.</p>
<p>V. – Un décret en Conseil d'État fixe les modalités d'application du présent article.</p>''',
    "Réécriture à droit constant : séparation, dans le premier alinéa, des deux circuits de commissionnement ; formulation distincte des pouvoirs documentaires et des étapes de l'audition. Les habilitations, leurs conditions et les garanties de preuve restent inchangées. Aucune réforme de fond des pouvoirs d'enquête.",
    "Les I à V et les 1° et 2° du II sont conservés sans déplacement d'alinéa. Maintien des cinq infractions du code pénal, de la condition de préjudice, des deux infractions du CSS, des régimes spéciaux et des notaires. L. 382-17 a été consulté dans le corpus. Contrôler ensemble le commissionnement national du premier groupe et celui du directeur employeur du second groupe lors de toute modification ultérieure de L. 114-10. La compétence nationale, la preuve contraire, la transmission directe au procureur, la nécessité de l'enquête, la nullité pour incitation et les garanties de lecture, d'observations et de signature sont toutes reprises.",
)

add(
    'L114-22-4',
    '''<p>L'habilitation à rechercher et à constater les infractions mentionnées aux articles L. 114-13 et L. 114-18 est accordée aux agents chargés du contrôle mentionnés à l'article L. 243-7.</p>''',
    "Réécriture à droit constant : la règle présente directement l'objet de l'habilitation puis les agents qui en bénéficient. Aucune réforme de fond ni assimilation aux autres pouvoirs d'enquête.",
    "Les trois renvois sont conservés. Cet article ne reprend que l'habilitation à rechercher et constater les infractions de L. 114-13 et L. 114-18 ; il n'importe pas automatiquement tous les moyens prévus à L. 114-22-3.",
)

add(
    'L114-22-5',
    '''<p>Dans l'exercice de leur mission de lutte contre la fraude, les agents de contrôle assermentés et agréés mentionnés à l'article L. 114-10 peuvent interroger les services du ministre des affaires étrangères qui tiennent le registre mentionné à l'article L. 12 du code électoral. Cette interrogation a pour seule finalité de contrôler le respect de la condition de résidence en France pour l'attribution et le service des prestations de l'assurance maladie.</p>''',
    "Réécriture à droit constant : distinction entre les agents autorisés, les services interrogés et la finalité exclusive de la consultation. Aucune réforme de fond ni élargissement à d'autres prestations.",
    "L'assermentation et l'agrément demeurent cumulatifs. Maintien des renvois à L. 114-10 et à L. 12 du code électoral, et du champ limité à la résidence en France pour l'attribution et le service des prestations de l'assurance maladie. Les modalités restent celles de L. 114-22-7.",
)

add(
    'L114-22-6',
    '''<p>Les agents de contrôle assermentés et agréés mentionnés à l'article L. 114-10 peuvent traiter les données de connexion et de suivi dont l'organisme d'assurance maladie dispose dans son système d'information et qui sont nécessaires à la recherche ou à la constatation d'un manquement délibéré ou de manœuvres frauduleuses. Cette faculté est subordonnée à l'existence d'indices sérieux d'un tel manquement ou de telles manœuvres visant à obtenir indûment, pour soi-même ou pour autrui, l'attribution ou le versement d'une prestation de l'assurance maladie, ou ayant conduit à un tel versement.</p>''',
    "Réécriture à droit constant : les agents et les données autorisées sont explicités avant la condition d'indices sérieux. Aucune réforme de fond du traitement des données ni du champ de l'assurance maladie.",
    "Maintien des données de connexion et de suivi déjà détenues dans le système d'information, du critère de nécessité, des indices sérieux, du manquement délibéré et des manœuvres frauduleuses. Sont conservés le bénéfice pour soi ou autrui et la distinction entre la tentative d'obtention indue et le versement déjà intervenu. Coordination réglementaire inchangée avec L. 114-22-7.",
)

add(
    'L114-22-7',
    '''<p>Un décret en Conseil d'État détermine les modalités d'application des articles L. 114-22-5 et L. 114-22-6. Ce décret est pris après avis de la Commission nationale de l'informatique et des libertés.</p>''',
    "Réécriture à droit constant : séparation de l'objet du décret et de la consultation préalable de la CNIL. Aucune réforme de fond de la compétence réglementaire ou de la consultation.",
    "Le décret en Conseil d'État reste commun aux deux articles L. 114-22-5 et L. 114-22-6 et soumis à l'avis préalable de la CNIL. Aucun pouvoir autonome de collecte ou de traitement n'est ajouté.",
)

add(
    'L114-22-8',
    '''<p>Le directeur de l'organisme peut suspendre à titre conservatoire tous les paiements d'une aide, d'une prestation ou d'une allocation lorsque les agents chargés du contrôle mentionnés aux articles L. 114-10 et L. 243-7 du présent code ou à l'article L. 724-7 du code rural et de la pêche maritime réunissent plusieurs indices sérieux de manœuvres frauduleuses, de manquement délibéré à ses obligations ou de commission d'infractions de la part du bénéficiaire.</p>
<p>La décision est motivée et immédiatement notifiée à l'intéressé. Elle indique les voies et délais de recours ainsi que la possibilité, pour l'intéressé, de présenter des éléments de nature à permettre le rétablissement du versement de l'allocation lors d'un débat contradictoire tenu à sa demande, dans un délai de deux semaines à compter de cette notification.</p>
<p>La suspension ne peut durer plus de deux mois à compter de sa notification.</p>
<p>Un décret en Conseil d'État fixe les modalités d'application du présent article, notamment les garanties assurant le respect du contradictoire pour le bénéficiaire dont le paiement de l'allocation est suspendu.</p>''',
    "Réécriture à droit constant : le directeur et sa faculté de suspension sont placés en tête du premier alinéa ; les garanties de notification et les deux délais sont formulés directement. Aucune réforme de fond de la suspension conservatoire.",
    "Maintien de l'exigence de plusieurs indices sérieux, des trois catégories de faits et de tous les renvois aux agents de contrôle. Les deux semaines courent à compter de la notification, de même que le plafond de deux mois. La source vise aide, prestation ou allocation au premier alinéa mais seulement l'allocation aux deuxième et quatrième alinéas : cette différence préexistante est conservée ; une harmonisation de sa portée nécessiterait une décision expresse. Les quatre alinéas restent à leur place.",
)

add(
    'L114-23',
    '''<p>I. – L'autorité compétente de l'État conclut avec les organismes nationaux de sécurité sociale une convention-cadre de performance du service public de la sécurité sociale, dans le respect des lois de financement de la sécurité sociale.</p>
<p>Pour chaque organisme national du régime général et pour la Caisse centrale de la mutualité sociale agricole, cette convention est signée par le président du conseil ou du conseil d'administration et par le directeur général ou le directeur. Pour les régimes spéciaux mentionnés à l'article L. 711-1, les conditions de signature sont fixées par décret.</p>
<p>La convention définit les objectifs transversaux aux différents organismes de sécurité sociale afin de fixer des actions communes dans les domaines suivants :</p>
<p>1° La mise en œuvre de mesures de simplification et d'amélioration de la qualité du service aux assurés, aux allocataires et aux cotisants ;</p>
<p>2° La mutualisation entre organismes, notamment pour la gestion immobilière, les achats, les ressources humaines, la communication et les systèmes d'information, en cohérence avec le plan stratégique des systèmes d'information du service public de la sécurité sociale arrêté par le ministre chargé de la sécurité sociale ;</p>
<p>3° La présence, sur le territoire national, des différents régimes et des différentes branches mentionnés à l'article L. 200-2 du présent code et à l'article L. 721-1 du code rural et de la pêche maritime ;</p>
<p>4° L'évaluation de la performance des différents régimes.</p>
<p>La convention prévoit, le cas échéant, les outils de mesure quantitatifs et qualitatifs associés à la définition des objectifs.</p>
<p>Elle détermine également :</p>
<p>a) Les conditions de conclusion de ses avenants ;</p>
<p>b) Le processus d'évaluation contradictoire des résultats obtenus au regard des objectifs fixés.</p>
<p>II. – La convention-cadre de performance du service public de la sécurité sociale est conclue pour au moins quatre ans. Elle est transmise aux commissions permanentes parlementaires mentionnées à l'article LO 111-9, ainsi que, le cas échéant, les avenants qui la modifient.</p>
<p>III. – Les conventions mentionnées à l'article L. 227-1 du présent code, à l'article L. 723-12 du code rural et de la pêche maritime et dans les dispositions réglementaires ayant le même objet sont négociées dans le respect de la convention-cadre mentionnée au I du présent article.</p>''',
    "Réécriture à droit constant : clarification des signataires selon les régimes, formulation homogène des domaines d'action et explicitation de la transmission au Parlement. Aucune réforme de fond de la gouvernance ni du financement.",
    "Les I à III, les 1° à 4°, les a) et b) ainsi que tous les alinéas textuels sont conservés. Maintien de la signature conjointe du président et du dirigeant, des cinq domaines de mutualisation cités, de la durée minimale de quatre ans et de l'évaluation contradictoire. Le dispositif existant peut servir aux simplifications envisagées dans policy.json, mais aucune économie n'est tenue pour acquise ni affectée au financement des réformes.",
)

add(
    'L114-24',
    '''<p>Le fonds de prospective et de performance de la sécurité sociale finance des études et des actions qui concourent à moderniser le service public de la sécurité sociale et à en améliorer la performance, notamment la réalisation d'audits ou de projets. Il contribue également aux dépenses de fonctionnement résultant des missions de contrôle et d'évaluation des organismes de sécurité sociale.</p>
<p>Les dépenses du fonds sont imputées sur les budgets de gestion des caisses nationales du régime général, de l'Agence centrale des organismes de sécurité sociale, de la Caisse centrale de la mutualité sociale agricole et des régimes spéciaux. Un arrêté des ministres chargés de la sécurité sociale et du budget fixe chaque année les conditions de cette imputation.</p>
<p>Un décret détermine les modalités de gestion du fonds.</p>''',
    "Réécriture à droit constant : distinction des dépenses financées et de la contribution aux frais de contrôle, puis séparation de l'imputation budgétaire et de son arrêté annuel. Aucune réforme de fond des ressources ou des missions du fonds.",
    "Les trois alinéas, toutes les catégories de budgets et les deux ministres compétents sont maintenus. Le décret reste un décret simple. Ce fonds de prospective n'est pas transformé en fonds de transition des retraites ; aucune économie, recette ou dotation nouvelle n'est inventée.",
)

add(
    'L114-25',
    '''<p>Pour accomplir leurs missions, les organismes chargés de gérer un régime obligatoire de sécurité sociale peuvent conclure entre eux des conventions de mise à disposition de services, d'équipements et de biens.</p>
<p>Chaque convention fixe les conditions dans lesquelles son bénéficiaire rembourse les frais qui lui incombent.</p>
<p>Lorsque ces conventions portent sur des services, des biens et des équipements assurés ou gérés par l'un des organismes chargés de gérer un régime obligatoire de sécurité sociale, elles ne sont soumises ni aux règles du code des marchés publics ni à celles de l'ordonnance n° 2005-649 du 6 juin 2005 relative aux marchés passés par certaines personnes publiques ou privées non soumises au code des marchés publics.</p>''',
    "Réécriture à droit constant : mise en évidence de la finalité des conventions, de l'obligation de remboursement du bénéficiaire et de la condition de l'exclusion des règles de marchés publics. Aucune réforme de fond de cette exclusion.",
    "Les trois alinéas normatifs sont conservés ; le paragraphe vide final est supprimé. Le troisième alinéa source renvoie encore au code des marchés publics et à l'ordonnance n° 2005-649 du 6 juin 2005. La concordance avec le droit de la commande publique doit être contrôlée dans ces textes hors des cinq codes, notamment avec le code de la commande publique et les dispositions d'abrogation et de transition ; aucun article de substitution ni aucune nouvelle exemption ne sont inventés. La date historique du 6 juin 2005 est maintenue.",
)

add(
    'L115-1',
    '''<p>À la demande du comptable public de l'État chargé du recouvrement des créances hospitalières, les organismes de sécurité sociale chargés de gérer un régime obligatoire lui communiquent les informations qu'ils détiennent sur l'état civil et le domicile des assurés sociaux débiteurs, sur le nom et l'adresse de leur employeur ainsi que sur le nom et l'adresse des établissements ou organismes auprès desquels un compte de dépôt est ouvert au nom de ces assurés. Ils ne peuvent opposer le secret professionnel à cette communication.</p>''',
    "Réécriture à droit constant : la demande du comptable déclenche explicitement l'obligation de communication et les catégories d'informations sont rattachées à leurs titulaires. Aucune réforme de fond du secret professionnel ou du recouvrement.",
    "Maintien du seul comptable chargé des créances hospitalières comme destinataire et de la limitation aux informations détenues. Les renseignements concernent les assurés débiteurs, leur employeur et les établissements ou organismes teneurs d'un compte de dépôt ; la disposition ne demande pas les soldes ou mouvements des comptes. L'alinéa unique est conservé.",
)

add(
    'L115-2',
    '''<p>Les collectivités territoriales, les groupements de collectivités, les établissements publics et les organismes chargés de gérer un service public peuvent recueillir, auprès des organismes de sécurité sociale chargés de gérer un régime obligatoire de sécurité sociale, des informations sur l'un de leurs ressortissants. Ils doivent en informer préalablement la personne concernée. Cette collecte a pour seule finalité d'apprécier sa situation pour l'accès aux prestations et avantages sociaux qu'ils servent.<br/><br/>Un décret en Conseil d'État, pris après avis de la Commission nationale de l'informatique et des libertés, fixe la nature des informations et les conditions de leur communication.</p>''',
    "Réécriture à droit constant : séparation de la faculté de collecte, de l'information préalable du ressortissant et de la finalité exclusive d'accès aux prestations. Aucune réforme de fond ni nouvelle collecte générale.",
    "Toutes les catégories de demandeurs sont maintenues, de même que l'information préalable, qui n'est pas remplacée par un consentement obligatoire. Les deux alinéas textuels restent séparés par le double saut de ligne de la source. Le décret en Conseil d'État et l'avis de la CNIL sont conservés.",
)

add(
    'L115-2-1',
    '''<p>Les organismes chargés de gérer un régime obligatoire de sécurité sociale échangent les informations non médicales qu'ils détiennent. Ces échanges sont limités aux informations nécessaires à l'appréciation de la situation de leurs ressortissants pour l'accès aux prestations et avantages sociaux qu'ils servent, ainsi qu'aux actions qu'ils mettent en œuvre pour prévenir la perte d'autonomie des personnes âgées.</p>
<p>Un décret en Conseil d'État, pris après avis de la Commission nationale de l'informatique et des libertés, précise quelles informations peuvent être transmises, dans quelles conditions elles le sont et quels organismes peuvent en être destinataires.</p>''',
    "Réécriture à droit constant : rattachement explicite de l'exclusion médicale et de la nécessité aux informations échangées, puis présentation directe des trois objets du décret. Aucune réforme de fond du partage de données.",
    "Maintien de l'échange prévu entre organismes, des deux finalités sociales et de l'exclusion des informations médicales. La prévention de la perte d'autonomie concerne toujours les personnes âgées. Les deux alinéas, le décret en Conseil d'État et l'avis préalable de la CNIL sont conservés ; aucun accès général à des données médicales n'est créé.",
)

add(
    'L115-3',
    '''<p>Le titre Ier du livre II du code des relations entre le public et l'administration détermine dans quelles conditions les organismes de sécurité sociale doivent faire connaître les motifs de leurs décisions individuelles.</p>''',
    "Réécriture à droit constant : la disposition qui fixe les conditions de motivation devient le sujet de la phrase. Aucune réforme de fond ni généralisation de la motivation au-delà du code de renvoi.",
    "Le titre Ier du livre II du code des relations entre le public et l'administration demeure le renvoi intégral. Les décisions restent individuelles et aucun délai de motivation n'est ajouté. Les sauts de ligne sans contenu normatif sont supprimés.",
)

add(
    'L115-4',
    '''<p>Un décret en Conseil d'État fixe les conditions dans lesquelles les autorités compétentes de l'État et les organismes d'assurance maladie échangent les informations non nominatives nécessaires à la mise en œuvre des dispositions du titre Ier du livre VII du code de la santé publique. Ces échanges respectent le secret médical.</p>''',
    "Réécriture à droit constant : formulation active de la compétence réglementaire et expression distincte de l'obligation de respecter le secret médical. Aucune réforme de fond des informations échangeables.",
    "Le caractère non nominatif, la nécessité des informations et le secret médical sont maintenus. La source vise le titre Ier du livre VII du code de la santé publique : ce renvoi ancien est conservé et sa concordance doit être vérifiée dans le code de la santé publique, absent du corpus des cinq codes fourni. Aucun numéro actuel de remplacement n'est supposé. Le décret reste pris en Conseil d'État.",
)

add(
    'L115-5',
    '''<p>Les caisses nationales des régimes de base d'assurance maladie peuvent créer un groupement d'intérêt économique pour lui confier des tâches communes de traitement de l'information. Le service des prestations est exclu de ces tâches.</p>
<p>Les autorités compétentes de l'État contrôlent ce groupement dans les conditions fixées par décret en Conseil d'État.</p>''',
    "Réécriture à droit constant : séparation de la faculté de création et de l'exclusion du service des prestations, puis désignation active de l'autorité de contrôle. Aucune réforme de fond de la mutualisation.",
    "Maintien du caractère facultatif du groupement, du champ des caisses nationales des régimes de base d'assurance maladie, des seules tâches communes de traitement de l'information et de l'exclusion du service des prestations. Les deux alinéas et le contrôle de l'État organisé par décret en Conseil d'État sont conservés.",
)

add(
    'L115-6',
    '''<p>Pour être affiliées à un régime obligatoire de sécurité sociale, les personnes de nationalité étrangère doivent remplir la condition de régularité du séjour prévue à l'article L. 111-2-3.</p>
<p>La méconnaissance des dispositions du premier alinéa et des législations qu'il mentionne ne dispense pas du paiement des cotisations, qui restent dues.</p>''',
    "Réécriture à droit constant : formulation directe de la condition d'affiliation et de l'absence d'effet libératoire d'une méconnaissance des règles. Aucune réforme de fond des conditions de séjour ou des cotisations.",
    "L. 111-2-3 a été consulté dans le corpus : il organise par décret l'appréciation de la stabilité de la résidence et de la régularité du séjour. Le présent article conserve son renvoi et sa seule condition de régularité du séjour, sans lui ajouter une condition autonome de stabilité. La formule source relative aux législations mentionnées par le premier alinéa reste conservée ; L. 111-2-3 est le seul article expressément cité dans cet alinéa. Les deux alinéas sont maintenus.",
)


sources = json.loads(Path('source.json').read_text())
assert len(sources) == 24
assert set(drafts) == {source['number'] for source in sources}
answer = []
for source in sources:
    xml, reason, notes = drafts[source['number']]
    answer.append({
        **{key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')},
        'proposed_xml': xml,
        'reason': reason,
        'review_notes': notes,
        'status': 'rewrite_draft',
    })
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
