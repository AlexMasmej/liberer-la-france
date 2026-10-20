import json
from pathlib import Path


drafts = {}


def article(number, paragraphs, reason, review_notes):
    drafts[number] = {
        "proposed_xml": "\n".join(f"<p>{p}</p>" for p in paragraphs),
        "reason": reason,
        "review_notes": review_notes,
    }


article("L181-1", [
    "Les fonctionnaires et agents publics assermentés qui sont habilités ou commissionnés par l'autorité administrative de l'État compétente, par l'autorité compétente mentionnée aux articles L. 422-1 à L. 422-3 du code de l'urbanisme ou par leurs délégués peuvent visiter les bâtiments soumis au présent code pour contrôler le respect de ses dispositions. Dans les conditions fixées par décret en Conseil d'État, ils peuvent obtenir communication de tous les documents techniques relatifs à la construction, à la rénovation ou à la démolition des bâtiments et en prendre copie.",
    "Le droit de visite et de communication peut être exercé pendant les travaux de construction ou de rénovation des bâtiments et jusqu'à six ans après leur achèvement. Il s'exerce de 6 heures à 21 heures et, en dehors de cette plage horaire, lorsque les lieux sont ouverts au public.",
], "Réécriture à droit constant : les qualités requises des agents, les autorités qui les habilitent et leurs pouvoirs sont explicités ; la période de contrôle et les horaires restent dans le deuxième alinéa. Aucune réforme de fond n'est introduite.",
    "Maintien des six ans, des horaires de 6 heures à 21 heures et de l'exception liée à l'ouverture au public. La source vise la démolition pour les documents, mais seulement la construction et la rénovation pour la période d'exercice du droit : cette différence de champ est conservée. Le dossier coordonné prévu par la politique de réforme ne dispense pas des contrôles du présent article.")

article("L181-1-1", [
    "L'autorité administrative compétente ou les fonctionnaires et agents publics mentionnés à l'article L. 181-1 peuvent confier la visite des bâtiments prévue à cet article à un contrôleur technique agréé et assermenté. Ce contrôleur ne doit exercer aucune activité de nature à compromettre son impartialité ou son indépendance à l'égard du projet. Sans l'assentiment de leur occupant, les domiciles et les locaux comprenant des parties à usage d'habitation sont exclus de cette visite.",
    "Les conditions d'application du présent article sont fixées par décret en Conseil d'État.",
], "Réécriture à droit constant : la désignation du contrôleur, les garanties d'impartialité et d'indépendance et l'exclusion des locaux habités sans assentiment sont présentées en phrases distinctes dans le même alinéa. Aucune réforme de fond.",
    "L'agrément et l'assermentation restent cumulatifs. La faculté de désignation n'est pas étendue à une visite forcée d'un domicile par le contrôleur technique ; l'articulation avec les articles L. 181-4 à L. 181-10 est conservée.")

article("L181-2", [
    "Pour les bâtiments relevant du ministre de la défense, des agents habilités du ministère de la défense contrôlent les mesures prises en application du titre VI relatif à l'accessibilité du cadre bâti. Les conditions de ce contrôle sont définies par un décret en Conseil d'État pris après avis du conseil mentionné à l'article L. 146-1 du code de l'action sociale et des familles.",
], "Réécriture à droit constant : les agents responsables du contrôle sont placés comme sujet de la phrase ; les modalités réglementaires et la consultation préalable sont distinguées dans le même alinéa. Aucune réforme de fond.",
    "Le régime particulier reste limité aux bâtiments relevant du ministre de la défense et aux mesures du titre VI sur l'accessibilité. Le renvoi au conseil prévu par l'article L. 146-1 du code de l'action sociale et des familles est maintenu.")

article("L181-3", [
    "Pour les besoins des contrôles qu'ils conduisent, les fonctionnaires et agents publics mentionnés à l'article L. 181-1 peuvent se transmettre spontanément les informations et les documents qu'ils détiennent ou recueillent dans l'exercice de leurs missions de police administrative. Le secret professionnel auquel ils sont éventuellement tenus ne peut être opposé à ces communications.",
], "Réécriture à droit constant : la finalité des échanges et leur périmètre sont explicités, puis la dérogation au secret professionnel est formulée dans une phrase distincte. Aucune réforme de fond.",
    "La dérogation au secret demeure limitée aux échanges entre les agents désignés, nécessaires à leurs contrôles et portant sur les éléments détenus ou recueillis au titre de la police administrative. Elle n'est pas transformée en autorisation générale de partage pour le dossier coordonné.")

article("L181-4", [
    "La visite des domiciles et des locaux comportant des parties à usage d'habitation exige la présence de leur occupant et son assentiment.",
    "Si l'accès à un domicile ou à un local comprenant des parties à usage d'habitation est refusé, ou si la personne ayant qualité pour l'autoriser ne peut être jointe, le juge des libertés et de la détention peut autoriser la visite par ordonnance. Le juge compétent est celui du tribunal judiciaire dans le ressort duquel se trouvent les lieux ou locaux à visiter.",
    "L'ordonnance indique l'adresse des lieux à visiter, le nom et la qualité des agents habilités à réaliser la visite, ainsi que les heures auxquelles ils sont autorisés à se présenter.",
    "L'ordonnance est exécutoire à titre provisoire.",
], "Réécriture à droit constant : les conditions de la visite consentie, les cas de saisine du juge et sa compétence territoriale sont rendus explicites, sans modifier les quatre alinéas. Aucune réforme de fond.",
    "Les deux exigences du premier alinéa demeurent cumulatives. Le deuxième alinéa conserve l'autorisation judiciaire en cas de refus ou d'impossibilité de joindre la personne compétente ; les mentions de l'ordonnance et son caractère provisoirement exécutoire sont maintenus. La source de L. 181-8 mentionne encore un tribunal de grande instance, contrairement au tribunal judiciaire ici désigné : divergence signalée sans correction implicite.")

article("L181-5", [
    "Lors de la visite, l'ordonnance est notifiée sur place à l'occupant des lieux ou à son représentant. L'occupant ou son représentant en reçoit une copie intégrale contre récépissé ou émargement au procès-verbal de visite. Si l'occupant et son représentant sont absents, la notification intervient après la visite par lettre recommandée avec demande d'avis de réception. Elle est réputée faite à la date de réception inscrite sur l'avis. À défaut de réception, l'ordonnance est signifiée par acte d'huissier de justice.",
    "L'acte de notification indique les voies et les délais de recours contre l'ordonnance autorisant la visite et contre le déroulement des opérations. Il précise aussi que le juge ayant autorisé la visite peut être saisi d'une demande de suspension ou d'arrêt de celle-ci.",
], "Réécriture à droit constant : les étapes de notification, leurs destinataires et la date retenue sont présentés dans leur ordre d'exécution ; les informations sur les recours restent au deuxième alinéa. Aucune réforme de fond.",
    "La copie intégrale, le récépissé ou l'émargement, la lettre recommandée avec avis de réception et la signification subsidiaire sont conservés. La source emploie encore « huissier de justice » : cette désignation ancienne est maintenue et appelle un contrôle de coordination terminologique avec la profession de commissaire de justice.")

article("L181-6", [
    "La visite se déroule sous l'autorité et le contrôle du juge des libertés et de la détention qui l'a autorisée. S'il l'estime utile, il peut se rendre dans les locaux pendant l'intervention. Il peut, à tout moment, suspendre la visite ou y mettre fin. Une demande de suspension ou d'arrêt des opérations adressée à ce juge ne suspend pas leur déroulement.",
], "Réécriture à droit constant : les pouvoirs du juge sont exprimés par des verbes directs et l'absence d'effet suspensif de sa saisine est formulée explicitement. Aucune réforme de fond.",
    "Le contrôle reste confié au juge ayant autorisé la visite. Son pouvoir de présence, de suspension ou d'arrêt à tout moment et l'absence d'effet suspensif de la seule demande sont conservés, en coordination avec L. 181-5.")

article("L181-7", [
    "Les agents effectuent la visite en présence de l'occupant des lieux ou de son représentant. L'occupant ou son représentant peut se faire assister par un conseil de son choix. En l'absence de l'occupant, les agents chargés de la visite ne peuvent l'effectuer qu'en présence de deux témoins qui ne sont pas placés sous leur autorité.",
    "Les agents ayant effectué la visite dressent immédiatement un procès-verbal qui décrit les modalités et le déroulement de l'opération et consigne leurs constatations. Ce procès-verbal est signé par les agents et par l'occupant des lieux ou, le cas échéant, son représentant et les témoins. Tout refus de signature y est mentionné.",
    "Dès l'établissement du procès-verbal, son original est adressé au juge ayant autorisé la visite. Une copie est remise à l'occupant des lieux ou à son représentant, ou lui est adressée par lettre recommandée avec demande d'avis de réception.",
    "Le procès-verbal indique les voies et le délai de recours.",
], "Réécriture à droit constant : les personnes présentes, les obligations de rédaction et de signature, puis la transmission du procès-verbal sont exprimées en phrases directes. Les quatre alinéas sont conservés ; aucune réforme de fond.",
    "Maintien du conseil librement choisi, des deux témoins indépendants de l'autorité des agents, de la rédaction immédiate et des modalités de remise. La condition des témoins reste rattachée à l'absence de l'occupant, comme dans la source, sans la remplacer par l'absence de tout représentant. Le délai de recours reste déterminé par L. 181-9.")

article("L181-8", [
    "Un appel contre l'ordonnance autorisant la visite peut être formé devant le premier président de la cour d'appel, selon les règles du code de procédure civile. Les parties peuvent agir sans constituer avocat.",
    "L'appel est formé par une déclaration remise ou adressée par pli recommandé au greffe de la cour, dans un délai de quinze jours à compter de la notification de l'ordonnance. Il n'a pas d'effet suspensif.",
    "Le greffe du tribunal de grande instance transmet sans délai le dossier au greffe de la cour d'appel. Les parties peuvent y consulter ce dossier.",
    "Un pourvoi en cassation peut être formé contre l'ordonnance du premier président de la cour d'appel, selon les règles du code de procédure civile. Le délai de ce pourvoi est de quinze jours.",
], "Réécriture à droit constant : les modalités de l'appel, la consultation du dossier et le pourvoi sont exposés en phrases plus courtes, sans déplacer les quatre alinéas. Aucune réforme de fond.",
    "Les deux délais de quinze jours et le point de départ propre à l'appel sont conservés ; aucun point de départ nouveau du pourvoi n'est ajouté. Incohérence préexistante : le troisième alinéa désigne encore le tribunal de grande instance alors que L. 181-4 vise le tribunal judiciaire. Cette mention est conservée pour une coordination expresse.")

article("L181-9", [
    "Les recours portant sur le déroulement des visites autorisées par le juge des libertés et de la détention relèvent du premier président de la cour d'appel, selon les règles du code de procédure civile. Les parties peuvent agir sans constituer avocat.",
    "Le recours est formé par une déclaration remise ou adressée par pli recommandé au greffe de la cour, dans un délai de quinze jours à compter de la remise ou de la réception du procès-verbal de visite. Il n'a pas d'effet suspensif.",
    "Un pourvoi en cassation peut être formé contre l'ordonnance du premier président de la cour d'appel, selon les règles du code de procédure civile. Le délai de ce pourvoi est de quinze jours.",
], "Réécriture à droit constant : la compétence et les formalités du recours contre les opérations sont formulées directement ; l'absence d'effet suspensif est isolée dans une phrase. Aucune réforme de fond.",
    "Le délai de quinze jours court de la remise ou de la réception du procès-verbal, et non de la notification de l'ordonnance prévue à L. 181-8. Le pourvoi conserve son délai distinct de quinze jours ; l'absence de représentation obligatoire est maintenue.")

article("L181-10", [
    "L'acte notifiant l'ordonnance par laquelle le juge des libertés et de la détention autorise la visite reproduit les articles L. 181-3 à L. 181-8.",
], "Réécriture à droit constant : l'acte de notification devient le sujet de l'obligation de reproduction, sans modifier les textes à reproduire. Aucune réforme de fond.",
    "La plage L. 181-3 à L. 181-8 est conservée exactement. Elle comprend L. 181-3 mais n'inclut pas L. 181-9 relatif au recours contre les opérations, alors que L. 181-5 impose d'informer sur ce recours : ce périmètre préexistant appelle un contrôle et n'est pas étendu silencieusement.")

article("L181-11", [
    "Lors du contrôle prévu à l'article L. 181-1, le fonctionnaire ou l'agent public chargé du contrôle en application de l'article L. 181-1 adresse un rapport à l'autorité administrative compétente s'il constate que les utilisateurs du sol, les bénéficiaires des travaux, y compris les propriétaires et les copropriétaires d'immeubles collectifs à usage d'habitation, les architectes, les entrepreneurs, les personnes et organismes mentionnés à l'article L. 122-12 ou toute autre personne responsable de l'exécution de travaux ont manqué aux obligations imposées par les articles L. 112-1, L. 112-9, L. 112-10, L. 113-10, L. 113-11, L. 113-12, L. 113-13, L. 113-18, L. 113-19, L. 113-20, L. 122-3, L. 122-7, L. 122-8, L. 122-8-1, L. 122-9, L. 122-10, L. 122-11, L. 126-27, L. 126-34, L. 131-1, L. 131-2, L. 132-1, L. 132-2, L. 132-3, L. 132-5 et L. 132-6, L. 132-7, L. 133-1, L. 133-2, L. 134-6, L. 134-8, L. 134-10, L. 134-11, L. 134-12, L. 141-1, L. 141-2, L. 145-1, L. 146-1, L. 151-1, L. 152-1, L. 152-2, L. 152-3, L. 153-1 à L. 153-4, L. 154-1, L. 154-2, L. 155-1, L. 156-1, L. 157-1, L. 161-1, L. 162-1, L. 163-1, L. 163-2 à l'exception de son dernier alinéa, L. 164-1, L. 164-2, L. 164-3, L. 171-1, L. 171-3, L. 171-4, L. 172-1 et L. 173-1. Il remet une copie du rapport à l'intéressé. Celui-ci peut présenter ses observations à l'autorité administrative dans le délai qu'elle fixe, qui ne peut être inférieur à un mois.",
], "Réécriture à droit constant : l'agent chargé du contrôle devient le sujet de l'obligation de rapport ; les destinataires, les personnes concernées et la procédure contradictoire sont explicités. La liste intégrale des obligations reste dans l'unique alinéa. Aucune réforme de fond.",
    "Tous les renvois et l'exclusion du dernier alinéa de L. 163-2 sont maintenus, ainsi que le minimum d'un mois. Le champ administratif, notamment L. 112-1 et L. 134-10, n'est pas aligné sur la liste pénale distincte de L. 183-4. La source est marquée ABROGE_DIFF avec une fin de validité indiquée au 1er janvier 2028 : la proposition porte sur cette version, sans en prolonger l'application.")

article("L181-12", [
    "L'autorité administrative compétente met l'intéressé en demeure de régulariser sa situation dans le délai qu'elle fixe, indépendamment des poursuites pénales susceptibles d'être exercées en application de l'article L. 183-4.",
    "Sauf si des motifs d'intérêt général s'y opposent, elle peut, dans la mise en demeure ou dans un acte distinct, ordonner la suspension des travaux de construction, de rénovation ou de démolition jusqu'à la régularisation de la situation de l'intéressé.",
], "Réécriture à droit constant : l'obligation de mise en demeure et la faculté de suspension sont distinguées ; la réserve d'intérêt général est placée au début du deuxième alinéa. Aucune réforme de fond.",
    "Le cumul possible avec les poursuites pénales, les trois catégories de travaux et la réserve d'intérêt général sont conservés. La rénovation locative de vingt-quatre mois prévue par la politique de réforme nécessite des dispositions expresses dans la loi n° 89-462 du 6 juillet 1989, notamment sur la décence et les travaux, avec contrôle des travaux, compensation des surcoûts énergétiques et transition des baux ; elle ne constitue ici ni délai de régularisation automatique ni dérogation aux protections contre l'habitat indigne.")

article("L181-13", [
    "Lorsque la personne mise en demeure n'a pas exécuté cette mise en demeure à l'expiration du délai fixé en application de l'article L. 181-12, l'autorité administrative compétente peut prononcer une ou plusieurs des sanctions administratives suivantes :",
    "1° Obliger la personne mise en demeure à consigner entre les mains d'un comptable public, avant la date fixée par l'autorité administrative, une somme égale au montant des travaux ou opérations à réaliser.",
    "La somme consignée bénéficie d'un privilège de même rang que celui prévu à l'article 1920 du code général des impôts. Son recouvrement suit les règles applicables aux créances de l'État étrangères à l'impôt et au domaine.",
    "L'opposition formée devant le juge administratif contre l'état exécutoire pris pour une mesure de consignation ordonnée par l'autorité administrative n'a pas d'effet suspensif ;",
    "2° Faire exécuter d'office les mesures prescrites, à la place de la personne mise en demeure et à ses frais. Les sommes consignées au titre du 1° servent à payer les dépenses ainsi engagées ;",
    "3° Suspendre les travaux de construction, de rénovation ou de démolition jusqu'à la régularisation de la situation de l'intéressé et prendre les mesures conservatoires nécessaires, aux frais de la personne mise en demeure ;",
    "4° Imposer le paiement d'une amende administrative d'un montant maximal de 20 000 € pour une personne physique et de 100 000 € pour une personne morale, ainsi que d'une astreinte journalière d'un montant maximal de 300 € pour une personne physique et de 1 500 € pour une personne morale. L'amende est recouvrée selon les règles applicables aux créances de l'État étrangères à l'impôt et au domaine. L'astreinte s'applique à compter de la notification de la décision qui la fixe et jusqu'à ce que la mise en demeure ou la mesure ordonnée soit satisfaite. Les deuxième et troisième alinéas du 1° s'appliquent à l'astreinte ;",
    "5° Suspendre l'agrément des personnes ou organismes mentionnés à l'article L. 122-12, ou le leur retirer.",
    "Le montant des amendes et des astreintes est proportionné à la gravité des manquements constatés.",
    "L'amende ne peut être prononcée plus de trois ans après la constatation des manquements.",
    "Les mesures prévues aux 1° à 5° ne peuvent être prises qu'après communication à l'intéressé des éléments susceptibles de les fonder et après l'avoir informé de la possibilité de présenter ses observations dans un délai fixé à cet effet, qui ne peut être inférieur à un mois.",
    "L'autorité administrative compétente peut publier l'acte prononçant ces sanctions sur le site internet des services de l'État dans le département, pour une durée comprise entre deux mois et cinq ans. Elle informe au préalable la personne sanctionnée de la publication envisagée, au cours de la procédure contradictoire prévue à l'avant-dernier alinéa du présent article.",
], "Réécriture à droit constant : les cinq sanctions, leurs modalités de recouvrement, leurs plafonds et les garanties contradictoires sont présentés avec des sujets explicites et des phrases plus courtes. Les douze alinéas, les numéros et leurs renvois internes sont conservés. Aucune réforme de fond.",
    "Contrôle des plafonds : amende de 20 000 €/100 000 €, astreinte journalière de 300 €/1 500 €, selon la nature physique/morale ; délai de trois ans, observations pendant au moins un mois et publication entre deux mois et cinq ans maintenus. Les deuxième et troisième alinéas du 1° restent aux mêmes positions pour leur application à l'astreinte ; la procédure contradictoire demeure à l'avant-dernier alinéa. Aucun délai de rénovation locative n'est substitué à cette procédure de sanction.")

article("L181-14", [
    "Un décret en Conseil d'État fixe les conditions d'application du présent chapitre. Il précise notamment l'autorité administrative de l'État compétente, les catégories de fonctionnaires autorisés à effectuer le contrôle administratif et leur champ territorial d'intervention.",
], "Réécriture à droit constant : l'habilitation réglementaire est formulée activement, puis ses précisions obligatoires sont énoncées dans une seconde phrase du même alinéa. Aucune réforme de fond.",
    "Le décret en Conseil d'État, l'énumération non exhaustive introduite par « notamment » et les trois précisions demandées sont conservés. La mention des catégories de fonctionnaires n'est pas étendue à d'autres catégories par la réécriture.")

article("L183-1", [
    "I. – Tous les officiers ou agents de police judiciaire peuvent constater les infractions prévues à l'article L. 183-4, de même que les fonctionnaires et agents de l'État et des collectivités publiques commissionnés à cette fin par le maire ou par l'autorité administrative dont ils relèvent et assermentés. Les fonctionnaires et agents ainsi commissionnés et assermentés recherchent et constatent ces infractions, quel que soit le lieu où elles sont commises, dans les conditions définies aux articles L. 181-1 à L. 181-10.",
    "Avant leur accès aux bâtiments et parties de bâtiment à usage professionnel, ces fonctionnaires et agents informent le procureur de la République. Celui-ci peut s'opposer à cet accès.",
    "Les procès-verbaux établis par ces agents font foi jusqu'à preuve du contraire.",
    "II. – Les agents de contrôle de l'inspection du travail mentionnés à l'article L. 8112-1 du code du travail recherchent et constatent également les infractions prévues à l'article L. 183-5, dans les conditions fixées aux articles L. 8113-1 et suivants du même code.",
    "III. – Après l'achèvement des travaux de bâtiments neufs ou de parties nouvelles de bâtiment soumis à permis de construire, les agents prévus au présent article, commissionnés à cette fin et assermentés, peuvent également constater les infractions à l'article L. 171-1 au vu d'une attestation. Celle-ci est établie par un contrôleur technique mentionné à l'article L. 125-1, par une personne répondant aux conditions de l'article L. 271-6 ou par un architecte.",
], "Réécriture à droit constant : les compétences de constatation, l'information du procureur et le recours à une attestation sont rendus plus lisibles, en conservant les I, II et III et leurs cinq alinéas. L'accord fautif « commissionnée » est corrigé en « commissionnés ». Aucune réforme de fond.",
    "Maintien de l'assermentation, des autorités de commissionnement, de l'opposition possible du procureur et de la force probante jusqu'à preuve contraire. Les missions de l'inspection du travail demeurent limitées ici au renvoi à L. 183-5. Au III, les trois catégories d'auteurs d'attestation restent alternatives ; ni les attestations ni les solutions techniques équivalentes envisagées par la réforme ne créent d'immunité pénale.")

article("L183-2", [
    "L'interruption des travaux peut être ordonnée sur réquisition du ministère public agissant à la demande du maire ou du fonctionnaire compétent. Elle peut aussi être ordonnée, même d'office, par le juge d'instruction saisi des poursuites ou par le tribunal correctionnel.",
    "L'autorité judiciaire statue après avoir entendu le bénéficiaire des travaux ou l'avoir dûment convoqué à comparaître dans les quarante-huit heures. Sa décision est exécutoire sur minute, nonobstant toute voie de recours.",
    "Si l'autorité judiciaire ne s'est pas encore prononcée, le maire peut également ordonner l'interruption des travaux par arrêté motivé dès qu'un procès-verbal constatant une infraction prévue à l'article L. 183-4 a été dressé. Une copie de l'arrêté est transmise sans délai au ministère public.",
    "L'autorité judiciaire peut, à tout moment, décider de lever ou de maintenir les mesures prises pour interrompre les travaux, d'office ou à la demande du maire, du fonctionnaire compétent ou du bénéficiaire des travaux. En tout état de cause, l'arrêté du maire cesse de produire effet en cas de non-lieu ou de relaxe.",
    "Le maire est informé de la décision judiciaire et en assure l'exécution lorsqu'il y a lieu.",
    "Si aucune poursuite n'a été engagée, le procureur de la République en informe le maire. Celui-ci met fin aux mesures qu'il a prises, d'office ou à la demande de l'intéressé.",
    "Pour assurer l'application immédiate de la décision judiciaire ou de son arrêté, le maire peut prendre toutes les mesures de coercition nécessaires, notamment saisir les matériaux approvisionnés et le matériel de chantier.",
    "L'un des agents mentionnés à l'article L. 183-1 procède à la saisie et, s'il y a lieu, à l'apposition des scellés. Il en dresse procès-verbal.",
    "Dans tous les cas où le maire n'a pas pris les mesures prévues au présent article, le représentant de l'État dans le département peut prendre toutes ces mesures après une mise en demeure restée sans résultat à l'expiration d'un délai de vingt-quatre heures. Il reçoit alors, à la place du maire, les avis et notifications prévus aux cinquième et sixième alinéas.",
], "Réécriture à droit constant : les décisions judiciaires, l'intervention subsidiaire du maire, l'exécution et la substitution préfectorale sont exprimées en phrases plus courtes. Les neuf alinéas et la place des avis auxquels renvoie le dernier alinéa sont préservés. Aucune réforme de fond.",
    "Les quarante-huit heures de convocation et les vingt-quatre heures de mise en demeure sont conservées ; les pouvoirs du juge, le non-lieu, la relaxe et l'absence de poursuites gardent leurs effets distincts. Le renvoi aux cinquième et sixième alinéas conserve ses cibles. La source est marquée ABROGE_DIFF avec une fin de validité indiquée au 1er janvier 2029 : cette version n'est pas prolongée par la proposition.")

article("L183-3", [
    "Si les travaux se poursuivent malgré la décision judiciaire ou l'arrêté qui en ordonne l'interruption, les personnes mentionnées au premier alinéa de l'article L. 183-4 encourent trois mois d'emprisonnement et 45 000 € d'amende.",
], "Réécriture à droit constant : la poursuite des travaux est formulée comme condition explicite de la peine ; les personnes concernées restent définies par renvoi. Aucune réforme de fond.",
    "Maintien du cumul de trois mois d'emprisonnement et de 45 000 € d'amende et du renvoi au premier alinéa de L. 183-4. L'infraction reste liée au non-respect d'une décision judiciaire ou d'un arrêté d'interruption des travaux, sans extension à un autre régime.")

article("L183-4", [
    "Les utilisateurs du sol, les bénéficiaires des travaux, les architectes, les entrepreneurs ou toute autre personne responsable de l'exécution de travaux sont punis de 45 000 € d'amende s'ils commettent une infraction aux obligations imposées par les articles L. 112-9, L. 112-10, L. 113-10, L. 113-11, L. 113-12, L. 113-13, L. 113-18, L. 113-19, L. 113-20, L. 122-3, L. 122-7, L. 122-8, L. 122-8-1, L. 122-9, L. 122-10, L. 122-11, L. 126-27, L. 126-34, L. 131-1, L. 131-2, L. 132-1, L. 132-2, L. 132-3, L. 132-5 et L. 132-6, L. 132-7, L. 133-1, L. 133-2, L. 134-6, L. 134-8, L. 134-11, L. 134-12, L. 141-1, L. 141-2, L. 145-1, L. 146-1, L. 151-1, L. 152-1, L. 152-2, L. 152-3, L. 153-1 à L. 153-4, L. 154-1, L. 154-2, L. 155-1, L. 156-1, L. 157-1, L. 161-1, L. 162-1, L. 163-1, L. 163-2 à l'exception de son dernier alinéa, L. 164-1, L. 164-2, L. 164-3, L. 171-1, L. 171-3, L. 171-4, L. 172-1, L. 173-1, par les dispositions réglementaires prises pour leur application ou par les autorisations délivrées conformément à ces dispositions. En cas de récidive, une peine de six mois d'emprisonnement peut en outre être prononcée.",
    "Les peines prévues à l'alinéa précédent s'appliquent également :",
    "1° Si les travaux accessoires d'aménagement ou de démolition imposés par les autorisations mentionnées au premier alinéa ne sont pas tous exécutés dans les délais prescrits ;",
    "2° Lorsque les bénéficiaires d'autorisations accordées pour une durée limitée ou à titre précaire ne respectent pas les délais fixés pour rétablir les lieux dans leur état antérieur ou réaffecter le sol à son ancien usage.",
    "Le propriétaire ou l'exploitant responsable de la mise en accessibilité d'un établissement recevant du public encourt les peines prévues au premier alinéa s'il n'a pas rempli les obligations des articles L. 164-1 à L. 164-3.",
    "Les personnes physiques coupables de l'un des délits du présent article encourent aussi la peine complémentaire prévue à l'article 131-35 du code pénal.",
    "Les personnes morales coupables de l'un des délits du présent article encourent les peines complémentaires ci-après :",
    "a) La peine mentionnée au 9° de l'article 131-39 du code pénal ;",
    "b) L'interdiction d'exercer, directement ou indirectement, une ou plusieurs activités professionnelles ou sociales, à titre définitif ou pour une durée de cinq ans au plus, selon les modalités de l'article 131-48 du code pénal.",
], "Réécriture à droit constant : les personnes pénalement concernées deviennent le sujet de la disposition ; les deux cas assimilés et les peines complémentaires sont formulés plus directement. La liste exhaustive des obligations, les neuf alinéas et les subdivisions 1°, 2°, a) et b) sont conservés. Aucune réforme de fond.",
    "Maintien de 45 000 €, des six mois en récidive, de l'exception du dernier alinéa de L. 163-2, des autorisations précaires et de l'interdiction définitive ou de cinq ans au plus. La liste pénale distincte n'est pas étendue aux références supplémentaires de L. 181-11. La source est marquée ABROGE_DIFF avec une fin de validité indiquée au 1er janvier 2028 ; aucune prolongation n'est proposée. Les garanties de sécurité, d'accessibilité et de salubrité voulues par la politique de réforme ne sont pas écartées.")

article("L183-5", [
    "Les conditions de sanction des infractions aux articles L. 112-2, L. 134-13 et L. 155-2, ainsi qu'aux dispositions réglementaires prises pour leur application, sont celles fixées à l'article L. 4744-1 du code du travail.",
], "Réécriture à droit constant : la règle de rattachement au régime de sanction du code du travail est formulée directement, sans modifier les obligations concernées. Aucune réforme de fond.",
    "Les trois références du CCH, leurs textes réglementaires d'application et le renvoi à L. 4744-1 du code du travail sont conservés. Ce régime distinct n'est pas remplacé par les sanctions de L. 183-4 ni par des paramètres de la réforme des contrats de travail.")

article("L183-6", [
    "En cas de condamnation pour une infraction prévue à l'article L. 183-4, le tribunal statue au vu des observations écrites du fonctionnaire compétent ou après l'avoir entendu. Il se prononce soit sur la mise en conformité des lieux ou des ouvrages avec les règlements, l'autorisation administrative ou le permis de construire, soit sur la démolition des ouvrages ou la réaffectation du sol afin de rétablir les lieux dans leur état antérieur.",
], "Réécriture à droit constant : la consultation du fonctionnaire et les deux catégories de mesures sur lesquelles statue le tribunal sont distinguées en deux phrases du même alinéa. Aucune réforme de fond.",
    "Le tribunal conserve l'ensemble des mesures de conformité, de démolition et de réaffectation ; les observations écrites et l'audition restent alternatives. Ces mesures de construction ne sont pas une procédure d'expulsion locative. L'accélération du traitement judiciaire des impayés appelle des dispositions propres dans la loi n° 89-462 du 6 juillet 1989 et les textes de procédure applicables, avec maintien des garanties contre les expulsions privées ; aucun renvoi nouveau n'est créé ici.")

article("L183-7", [
    "Lorsque le décès du prévenu ou l'amnistie éteint l'action publique, les dispositions de l'article L. 183-6 restent applicables.",
    "Si le tribunal correctionnel n'est pas saisi à la date de cette extinction, l'affaire est portée devant le tribunal judiciaire du lieu où se trouve l'immeuble. Celui-ci statue comme en matière civile.",
    "À la demande du maire ou du fonctionnaire compétent, le ministère public saisit le tribunal. Dans les deux cas, le tribunal statue au vu des observations écrites de ce fonctionnaire ou après l'avoir entendu, l'intéressé ou ses ayants droit ayant été mis en cause dans l'instance.",
    "Cette demande reste recevable jusqu'au jour où l'action publique aurait été prescrite.",
], "Réécriture à droit constant : les effets de l'extinction de l'action publique, la juridiction compétente et la saisine sont exposés en phrases directes, en conservant les quatre alinéas. Aucune réforme de fond.",
    "Seuls le décès et l'amnistie visés par la source sont repris ; le texte n'est pas étendu à toute extinction de l'action publique. La mise en cause de l'intéressé ou des ayants droit, la consultation du fonctionnaire et la limite liée à la prescription sont maintenues. La source est marquée ABROGE_DIFF avec une fin de validité indiquée au 1er janvier 2029 : aucune prolongation de cette version n'est introduite.")

article("L183-8", [
    "Le tribunal fixe au bénéficiaire des travaux irréguliers ou de l'utilisation irrégulière du sol le délai dans lequel il doit exécuter l'ordre de démolition, de mise en conformité ou de réaffectation. Il peut assortir sa décision d'une astreinte de 3 à 75 € par jour de retard.",
    "Si ce délai n'est pas respecté, l'astreinte court dès son expiration et jusqu'à l'exécution complète de l'ordre. Elle ne peut être révisée que dans le cas prévu au troisième alinéa du présent article.",
    "À défaut d'exécution dans l'année suivant l'expiration du délai, le tribunal peut, sur réquisition du ministère public, augmenter une ou plusieurs fois le montant de l'astreinte, même au-delà du maximum prévu ci-dessus.",
    "Lorsque la remise en état ordonnée a été régularisée, le tribunal peut autoriser le reversement d'une partie des astreintes si le redevable établit qu'une circonstance indépendante de sa volonté l'a empêché de respecter le délai imparti.",
], "Réécriture à droit constant : le délai d'exécution, le cours de l'astreinte, sa majoration et le reversement partiel sont exprimés en conditions distinctes. Les quatre alinéas et le renvoi au troisième sont conservés. Aucune réforme de fond.",
    "Maintien de la fourchette de 3 à 75 € par jour, de la condition d'un an et de la réquisition du ministère public pour une augmentation même au-delà du plafond. Le reversement reste partiel, facultatif et subordonné à la remise en état régularisée et à la preuve d'un empêchement indépendant de la volonté du redevable. Ce régime n'est pas aligné sur l'astreinte administrative de L. 181-13.")

article("L183-9", [
    "Les astreintes sont recouvrées selon les règles applicables au recouvrement des produits communaux. Leur produit revient à la commune sur le territoire de laquelle l'infraction a été commise. Si, dans le mois suivant l'invitation que lui adresse le représentant de l'État dans le département, le maire n'a pas liquidé le produit de l'astreinte, dressé l'état nécessaire au recouvrement et transmis cet état à ce représentant, la créance est liquidée et l'état est établi et recouvré au profit de l'État.",
], "Réécriture à droit constant : les règles de recouvrement, le bénéficiaire communal et le mécanisme subsidiaire au profit de l'État sont présentés en trois phrases dans l'unique alinéa. Aucune réforme de fond.",
    "Le délai reste d'un mois à compter de l'invitation du représentant de l'État. Les trois diligences du maire et le transfert au profit de l'État en cas de défaut sont conservés. Aucun produit supplémentaire ni financement de la réforme du logement n'est présumé.")


def main():
    sources = json.loads(Path("source.json").read_text())
    assert len(sources) == 24
    assert len(drafts) == len(sources)
    answer = []
    for source in sources:
        draft = drafts[source["number"]]
        notes = draft["review_notes"]
        if "2022-1076" in source["source_notes_xml"]:
            notes += " Note historique lue : second alinéa de l'article 8 de l'ordonnance n° 2022-1076 du 29 juillet 2022, entrée en vigueur fixée par décret en Conseil d'État et au plus tard le 1er janvier 2024 ; cette note ne fixe pas la date de la réforme proposée."
        else:
            assert "2020-71" in source["source_notes_xml"]
            notes += " Note historique lue : article 8 de l'ordonnance n° 2020-71 du 29 janvier 2020, entrée en vigueur fixée par décret en Conseil d'État et au plus tard le 1er juillet 2021 ; cette note ne fixe pas la date de la réforme proposée."
        answer.append({
            **{key: source[key] for key in ("code_id", "source_id", "source_sha256", "number")},
            "proposed_xml": draft["proposed_xml"],
            "reason": draft["reason"],
            "review_notes": notes,
            "status": "rewrite_draft",
        })
    Path("answer.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
