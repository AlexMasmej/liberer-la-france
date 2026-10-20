import json
from pathlib import Path


DRAFTS = {}


def draft(number, xml, reason, notes):
    if number in DRAFTS:
        raise ValueError(number)
    DRAFTS[number] = (xml.strip(), reason, notes)


draft(
    'L1238-2',
    """<p>Procéder à un licenciement sans avoir accompli les consultations du comité social et économique prévues aux articles L. 1233-29, L. 1233-30, L. 1233-34 et L. 1233-35 est puni d'une amende de 3 750 euros. Cette amende est prononcée pour chaque salarié concerné par l'infraction.</p>""",
    "Réécriture à droit constant : l'infraction et la règle de multiplication de l'amende sont exprimées dans deux phrases au sein du même alinéa. Aucune réforme de fond ; les sanctions des obligations de consultation sont maintenues.",
    "Montant de 3 750 euros par salarié et quatre renvois conservés. Les articles L. 1233-34 et L. 1233-35 du corpus concernent notamment l'expertise et les échanges d'informations : leur inclusion dans la formule générale des consultations est celle de la source et n'est pas remaniée. La réforme du motif économique ne dispense pas de ces obligations."
)

draft(
    'L1238-3',
    """<p>Le non-respect du délai d'envoi des lettres de licenciement fixé à l'article L. 1233-39 est puni d'une amende de 3 750 euros. Cette amende est prononcée pour chaque salarié concerné par l'infraction.</p>""",
    "Réécriture à droit constant : le manquement au délai est désigné directement et le calcul de l'amende fait l'objet d'une phrase distincte. Aucune modification de fond de l'infraction ni du délai auquel elle renvoie.",
    "Renvoi à L. 1233-39 et amende de 3 750 euros par salarié conservés. Les délais et modalités de notification demeurent déterminés par l'article de renvoi ; aucun délai autonome n'est créé ici."
)

draft(
    'L1238-4',
    """<p>Procéder à un licenciement sans l'avoir notifié à l'autorité administrative dans les conditions fixées à l'article L. 1233-46 est puni d'une amende de 3 750 euros. Cette amende est prononcée pour chaque salarié concerné par l'infraction.</p>""",
    "Réécriture à droit constant : la notification préalable et la sanction par salarié sont présentées dans deux phrases. Aucune réforme de fond des obligations envers l'autorité administrative.",
    "Montant de 3 750 euros par salarié et renvoi à L. 1233-46 conservés. La source parle de notification du licenciement alors que L. 1233-46 vise la notification du projet de licenciement économique d'au moins dix salariés dans une même période de trente jours. Ce décalage de formulation préexistant est signalé, sans étendre le champ de la sanction ni substituer un nouveau renvoi."
)

draft(
    'L1238-5',
    """<p>En cas de redressement ou de liquidation judiciaire, l'employeur, l'administrateur ou le liquidateur qui ne respecte pas les dispositions des articles L. 1233-58 et L. 1233-60 encourt une amende de 3 750 euros. Cette amende est prononcée pour chaque salarié concerné par l'infraction.</p>""",
    "Réécriture à droit constant : les personnes susceptibles de commettre l'infraction deviennent les sujets de la phrase et la sanction par salarié est explicitée séparément. Aucune réforme de fond du régime pénal en procédure collective.",
    "Les deux procédures, les trois personnes visées, les renvois à L. 1233-58 et L. 1233-60 et le montant de 3 750 euros par salarié sont conservés. L. 1233-58 contient lui-même, dans le corpus, des références anciennes aux articles L. 2323-31, L. 2325-35 et L. 4614-12-1 : leur éventuelle actualisation relève de cet article et n'est pas opérée indirectement ici."
)

draft(
    'L1241-1',
    """<p>Le contrat d'apprentissage et le contrat de mission conclu avec une entreprise de travail temporaire sont exclus du champ d'application du présent titre.</p>""",
    "Réécriture à droit constant : les deux contrats exclus sont placés en tête de phrase pour rendre le champ d'application immédiatement lisible. Aucune réforme de fond ni extension des règles du CDD à ces régimes distincts.",
    "Les deux exclusions sont intégralement maintenues, y compris la conclusion du contrat de mission avec une entreprise de travail temporaire. Les mesures relatives aux nouveaux CDI n'ont pas vocation à modifier ces exclusions."
)

draft(
    'L1242-1',
    """<p>Quel que soit le motif invoqué, le recours à un contrat de travail à durée déterminée ne doit avoir ni pour objet ni pour effet de pourvoir durablement un emploi relevant de l'activité normale et permanente de l'entreprise.</p>""",
    "Réécriture à droit constant : l'interdiction est formulée à partir du recours au CDD et son application à tous les motifs est placée en tête. Aucune réforme de fond ; l'interdiction de pourvoir durablement un emploi permanent reste entière.",
    "L'interdiction couvre aussi bien l'objet que l'effet du recours au CDD : chacun suffit à faire obstacle à ce recours. Les qualifications d'activité normale et permanente et de pourvoi durable sont conservées. Coordination maintenue avec les cas limitatifs de L. 1242-2 et les cas supplémentaires de L. 1242-3."
)

draft(
    'L1242-2',
    """<p>Sous réserve de l'article L. 1242-3, le recours à un contrat de travail à durée déterminée est autorisé uniquement pour exécuter une tâche précise et temporaire, dans l'un des cas suivants :</p>
<p>1° Remplacement d'un salarié dans l'une des situations suivantes :</p>
<p>a) Son absence ;</p>
<p>b) Son passage provisoire à temps partiel, convenu par avenant à son contrat de travail ou par un échange écrit entre lui et son employeur ;</p>
<p>c) La suspension de son contrat de travail ;</p>
<p>d) Son départ définitif précédant la suppression de son poste de travail, après consultation du comité social et économique, s'il existe ;</p>
<p>e) L'attente de l'entrée en service effective du salarié recruté par contrat à durée indéterminée pour le remplacer ;</p>
<p>2° Accroissement temporaire de l'activité de l'entreprise ;</p>
<p>3° Emplois à caractère saisonnier, dont les tâches ont vocation à se répéter chaque année selon une périodicité à peu près fixe, en fonction du rythme des saisons ou des modes de vie collectifs. Sont également concernés les emplois pour lesquels, dans certains secteurs d'activité définis par décret ou par convention ou accord collectif de travail étendu, il est d'usage constant de ne pas recourir au contrat de travail à durée indéterminée en raison de la nature de l'activité exercée et du caractère par nature temporaire de ces emplois. Si la durée du contrat de travail est inférieure à un mois, l'employeur émet un seul bulletin de paie ;</p>
<p>4° Remplacement d'un chef d'entreprise artisanale, industrielle ou commerciale, d'une personne exerçant une profession libérale, de son conjoint, à condition que celui-ci participe effectivement à l'activité de l'entreprise à titre professionnel et habituel, ou d'un associé non salarié d'une société civile professionnelle, d'une société civile de moyens, d'une société d'exercice libéral ou de toute autre personne morale exerçant une profession libérale ;</p>
<p>5° Remplacement du chef d'une exploitation agricole ou d'une entreprise mentionnée aux 1° à 4° de l'article L. 722-1 du code rural et de la pêche maritime, d'un aide familial, d'un associé d'exploitation ou de leur conjoint mentionné à l'article L. 722-10 du même code, à condition que ce conjoint participe effectivement à l'activité de l'exploitation agricole ou de l'entreprise ;</p>
<p>6° Recrutement d'ingénieurs et de cadres, au sens des conventions collectives, afin de réaliser un objet défini, à condition qu'un accord de branche étendu ou, à défaut, un accord d'entreprise prévoie ce recours et définisse :</p>
<p>a) Les nécessités économiques auxquelles le recours à ces contrats peut apporter une réponse adaptée ;</p>
<p>b) Les conditions dans lesquelles les salariés sous contrat à durée déterminée à objet défini bénéficient de garanties en matière d'aide au reclassement, de validation des acquis de l'expérience, de priorité de réembauche et d'accès à la formation professionnelle continue. Ces conditions doivent aussi leur permettre, au cours du délai de prévenance, de mobiliser les moyens disponibles pour organiser la suite de leur parcours professionnel ;</p>
<p>c) Les conditions de priorité d'accès des salariés sous contrat à durée déterminée à objet défini aux emplois en contrat à durée indéterminée dans l'entreprise.</p>""",
    "Réécriture à droit constant : les situations de remplacement ont un sujet explicite ; le 3° distingue les emplois saisonniers et les emplois d'usage dans des phrases séparées ; les garanties du contrat à objet défini sont rendues plus lisibles. Les six cas, leurs lettres et leur ordre sont conservés. Aucune réforme de fond : la politique maintient les CDD pour des besoins temporaires identifiés.",
    "Conservation des cinq situations du 1°, des catégories de personnes et de sociétés des 4° et 5°, de la condition de participation effective et des renvois ruraux. Au 4°, une virgule sépare les sociétés civiles de moyens des sociétés d'exercice libéral, que la source énumère sans ponctuation intermédiaire ; aucune catégorie n'est ajoutée. Le bulletin unique reste limité aux contrats de moins d'un mois du 3°. Au 6°, l'accord de branche doit être étendu ; l'accord d'entreprise n'intervient qu'à défaut. Les quatre garanties du b), leur mobilisation pendant le délai de prévenance et la priorité du c) sont maintenues. Aucun cas nouveau de recours n'est ajouté au titre de l'adaptation économique."
)

draft(
    'L1242-3',
    """<p>En plus des cas prévus à l'article L. 1242-2, la conclusion d'un contrat de travail à durée déterminée est possible dans les cas suivants :</p>
<p>1° En application de dispositions légales visant à favoriser le recrutement de certaines catégories de personnes sans emploi ;</p>
<p>2° Lorsque l'employeur s'engage à assurer au salarié un complément de formation professionnelle, pour une durée et selon des conditions fixées par décret ;</p>
<p>3° Lorsque l'employeur confie au salarié des activités de recherche et participe à sa formation à la recherche et par la recherche, dans les conditions fixées à l'article L. 412-3 du code de la recherche ;</p>
<p>4° Lorsque l'employeur confie au salarié des activités de recherche pour réaliser un objet défini, dans les conditions fixées à l'article L. 431-5 du code de la recherche, et s'engage à lui fournir une expérience professionnelle complémentaire au diplôme de doctorat prévu à l'article L. 612-7 du code de l'éducation ;</p>
<p>5° Au titre de la période de reconversion mentionnée à l'article L. 6324-1 du présent code, à condition que le contrat soit conclu pour une durée d'au moins six mois.</p>""",
    "Réécriture à droit constant : la liste des cas supplémentaires est introduite directement et les engagements de formation et de recherche sont reformulés avec un sujet explicite. Le minimum de six mois est rattaché au contrat du 5°. Aucune réforme de fond des dispositifs particuliers.",
    "Les cinq cas et les renvois à L. 1242-2, L. 412-3 et L. 431-5 du code de la recherche, L. 612-7 du code de l'éducation et L. 6324-1 sont conservés. La note source fixe l'entrée en vigueur de cette rédaction au 1er janvier 2026, conformément au II de l'article 11 de la loi n° 2025-989 du 24 octobre 2025 ; ce repère historique reste applicable et n'est pas une date de réforme nouvelle. La note de L. 6324-1 du corpus réserve aussi les actions antérieures dont l'avenant a été conclu avant le 1er janvier 2026 ; leur régime n'est pas modifié ici."
)

draft(
    'L1242-4',
    """<p>À l'issue d'un contrat d'apprentissage, un contrat de travail à durée déterminée peut être conclu dans les cas prévus aux articles L. 1242-2 et L. 1242-3. Il peut également être conclu lorsque l'apprenti doit satisfaire aux obligations du service national moins d'un an après l'expiration de son contrat d'apprentissage.</p>""",
    "Réécriture à droit constant : les cas de droit commun et le cas supplémentaire lié au service national sont présentés dans deux phrases du même alinéa. Aucune réforme de fond ni suppression de la disposition historique relative au service national.",
    "Renvois à L. 1242-2 et L. 1242-3 et délai strictement inférieur à un an conservés. La note source attribue à l'article 19 VIII de la loi n° 2014-40 du 20 janvier 2014 une application aux assurés dont la première pension prend effet à compter du 1er janvier 2015. Cette note relative aux pensions est sans rapport apparent avec le CDD après apprentissage : rattachement à contrôler. Elle est signalée sans être transformée en condition de conclusion du CDD."
)

draft(
    'L1242-5',
    """<p>Pendant les six mois qui suivent un licenciement pour motif économique, aucun contrat de travail à durée déterminée ne peut être conclu pour faire face à un accroissement temporaire de l'activité. Cette interdiction vaut aussi pour une tâche occasionnelle, précisément définie et non durable, qui ne relève pas de l'activité normale de l'entreprise.</p>
<p>Dans l'établissement, l'interdiction concerne les postes touchés par le licenciement.</p>
<p>L'interdiction ne s'applique pas dans les cas suivants :</p>
<p>1° Le contrat ne peut pas être renouvelé et sa durée ne dépasse pas trois mois ;</p>
<p>2° Le contrat est lié à la survenance d'une commande exceptionnelle à l'exportation dans l'entreprise de l'entrepreneur principal ou dans celle d'un sous-traitant. L'importance de cette commande doit nécessiter la mise en œuvre de moyens quantitativement ou qualitativement exorbitants de ceux que l'entreprise utilise ordinairement. Avant de procéder à ce recrutement, l'employeur informe et consulte le comité social et économique, s'il existe.</p>
<p>Même dans les cas prévus aux 1° et 2°, l'employeur doit respecter la priorité de réembauche prévue à l'article L. 1233-45.</p>""",
    "Réécriture à droit constant : l'interdiction, son champ dans l'établissement et les deux exceptions restent dans leurs alinéas ; les conditions de la commande exceptionnelle et l'obligation préalable de l'employeur sont séparées en phrases. Aucune réforme de fond ; l'élargissement proposé du motif économique ne supprime pas cette protection.",
    "Délai de six mois, exception d'au plus trois mois sans renouvellement, caractère exceptionnel de la commande à l'exportation et ampleur des moyens nécessaires conservés. L'information et la consultation préalables du comité, s'il existe, restent propres au 2°. La priorité de réembauche de L. 1233-45 demeure applicable aux deux exceptions."
)

draft(
    'L1242-6',
    """<p>En plus des interdictions prévues à l'article L. 1242-5, le recours à un contrat de travail à durée déterminée est interdit dans les cas suivants :</p>
<p>1° Remplacement d'un salarié dont le contrat de travail est suspendu à la suite d'un conflit collectif de travail ;</p>
<p>2° Exécution de certains travaux particulièrement dangereux inscrits sur une liste établie par voie réglementaire, dans les conditions prévues à l'article L. 4154-1.</p>
<p>L'autorité administrative peut, à titre exceptionnel, autoriser une dérogation à l'interdiction prévue au 2°, selon les conditions déterminées par voie réglementaire.</p>""",
    "Réécriture à droit constant : les deux interdictions sont formulées parallèlement et la dérogation administrative est rattachée explicitement aux travaux dangereux. Aucune réforme de fond ni création d'une dérogation au remplacement d'un salarié en conflit collectif.",
    "Renvois à L. 1242-5 et L. 4154-1 maintenus. La portée de la formule source « cette interdiction » est précisée par référence au 2°, en cohérence avec L. 4154-1, lu dans le corpus : ce dernier prévoit la même autorisation exceptionnelle pour les travaux dangereux. Le caractère exceptionnel et le renvoi aux conditions réglementaires sont conservés."
)

draft(
    'L1242-7',
    """<p>Le terme du contrat de travail à durée déterminée doit être fixé avec précision dès la conclusion du contrat.</p>
<p>Par dérogation, le contrat peut être conclu sans terme précis dans les cas suivants :</p>
<p>1° Remplacement d'un salarié absent ;</p>
<p>2° Remplacement d'un salarié dont le contrat de travail est suspendu ;</p>
<p>3° Attente de l'entrée en service effective d'un salarié recruté par contrat à durée indéterminée ;</p>
<p>4° Emplois à caractère saisonnier définis au 3° de l'article L. 1242-2 ou emplois pour lesquels il est d'usage constant de ne pas recourir au contrat de travail à durée indéterminée dans certains secteurs d'activité définis par décret ou par convention ou accord collectif étendu. Cet usage doit tenir à la nature de l'activité exercée et au caractère par nature temporaire de ces emplois ;</p>
<p>5° Remplacement de l'une des personnes visées aux 4° et 5° de l'article L. 1242-2 ;</p>
<p>6° Recrutement d'ingénieurs et de cadres pour réaliser un objet défini, dans le cas prévu au 6° de l'article L. 1242-2.</p>
<p>Dans ces cas, le contrat de travail à durée déterminée fixe une durée minimale. Son terme est la fin de l'absence de la personne remplacée ou la réalisation de l'objet pour lequel il a été conclu.</p>""",
    "Réécriture à droit constant : la règle du terme précis et sa dérogation sont énoncées directement ; le motif justifiant l'usage au 4° est isolé dans une seconde phrase du même alinéa. Aucune réforme de fond ; les six cas, la durée minimale et les événements de fin du contrat sont conservés.",
    "Numérotation et ordre des six cas inchangés ; renvois aux 3°, 4°, 5° et 6° de L. 1242-2 maintenus. La définition de l'usage conserve les secteurs définis par décret ou convention ou accord collectif étendu, la nature de l'activité et le caractère par nature temporaire. Coordination maintenue avec les bornes spéciales de L. 1242-8-2 et la prise d'effet anticipée de L. 1242-9."
)

draft(
    'L1242-8',
    """<p>La durée totale du contrat de travail à durée déterminée peut être fixée par une convention ou un accord de branche étendu. Elle ne peut avoir pour objet ou pour effet de pourvoir durablement un emploi lié à l'activité normale et permanente de l'entreprise.<br /><br />Le présent article ne s'applique ni au contrat de travail à durée déterminée conclu en application du 6° de l'article L. 1242-2 ni à celui conclu en application de l'article L. 1242-3.</p>""",
    "Réécriture à droit constant : la durée totale devient le sujet de la règle de négociation et les deux exclusions sont exprimées séparément dans la même phrase. Aucune réforme de fond de la compétence de la branche ni de l'interdiction du pourvoi durable d'un emploi permanent.",
    "Exigence d'extension de la convention ou de l'accord de branche conservée ; aucun pouvoir nouveau n'est attribué à un accord d'entreprise. Les deux exclusions et les séparations d'alinéas matérialisées par les sauts de ligne de la source sont maintenues. La note source réserve l'application aux contrats conclus postérieurement à la publication de l'ordonnance n° 2017-1387 du 22 septembre 2017, conformément à son article 40-VIII ; cette transition historique demeure à prendre en compte."
)

draft(
    'L1242-8-1',
    """<p>En l'absence de stipulation dans la convention ou l'accord de branche conclu en application de l'article L. 1242-8 fixant la durée totale du contrat de travail à durée déterminée, cette durée ne peut dépasser dix-huit mois. Elle comprend, s'il y a lieu, le ou les renouvellements effectués dans les conditions prévues à l'article L. 1243-13 ou, lorsqu'il s'applique, à l'article L. 1243-13-1.<br /><br />La durée maximale est ramenée à neuf mois si le contrat est conclu dans l'attente de l'entrée en service effective d'un salarié recruté par contrat à durée indéterminée ou pour réaliser des travaux urgents nécessités par des mesures de sécurité.<br /><br />La durée maximale est portée à vingt-quatre mois dans les cas suivants :<br /><br />1° Le contrat est exécuté à l'étranger ;<br /><br />2° Le contrat est conclu à l'occasion du départ définitif d'un salarié précédant la suppression de son poste de travail ;<br /><br />3° Une commande exceptionnelle à l'exportation survient dans l'entreprise de l'entrepreneur principal ou dans celle d'un sous-traitant. Son importance doit nécessiter la mise en œuvre de moyens quantitativement ou qualitativement exorbitants de ceux que l'entreprise utilise ordinairement. Dans ce cas, le contrat doit avoir une durée initiale d'au moins six mois. Avant les recrutements envisagés, l'employeur consulte le comité social et économique, s'il existe.<br /><br />Le présent article ne s'applique ni au contrat de travail à durée déterminée conclu en application du 6° de l'article L. 1242-2 ni à celui conclu en application de l'article L. 1242-3.</p>""",
    "Réécriture à droit constant : le décompte des renouvellements est séparé du plafond général et les conditions de la commande exceptionnelle sont réparties entre plusieurs phrases sans déplacer d'alinéa. Aucune réforme de fond des durées supplétives ni des exclusions.",
    "Conservation des plafonds de dix-huit, neuf et vingt-quatre mois, du minimum initial de six mois au 3°, de la consultation préalable du comité s'il existe, et des renvois à L. 1242-8, L. 1243-13 et L. 1243-13-1. Les trois cas de vingt-quatre mois, les deux cas de neuf mois et les deux exclusions finales restent distincts. Selon la note source et l'article 40-VIII de l'ordonnance n° 2017-1387 du 22 septembre 2017, ces règles s'appliquent aux contrats conclus postérieurement à la publication de cette ordonnance ; les contrats antérieurs ne sont pas basculés dans ce régime."
)

draft(
    'L1242-8-2',
    """<p>Le contrat de travail à durée déterminée prévu au 6° de l'article L. 1242-2 doit être conclu pour au moins dix-huit mois et au plus trente-six mois. Son renouvellement est interdit.</p>""",
    "Réécriture à droit constant : les bornes minimale et maximale sont exprimées directement, puis l'interdiction de renouvellement est énoncée dans une phrase propre. Aucune réforme de fond du CDD à objet défini.",
    "Minimum de dix-huit mois, maximum de trente-six mois et renvoi au seul 6° de L. 1242-2 conservés. La note source maintient l'application aux contrats conclus postérieurement à la publication de l'ordonnance n° 2017-1387 du 22 septembre 2017, en vertu de son article 40-VIII. Aucun renouvellement n'est introduit par coordination avec les règles générales."
)

draft(
    'L1242-9',
    """<p>La prise d'effet du contrat de travail à durée déterminée peut précéder l'absence de la personne à remplacer lorsque le contrat a pour objet le remplacement d'un salarié temporairement absent, d'un salarié dont le contrat de travail est suspendu ou de l'une des personnes mentionnées aux 4° et 5° de l'article L. 1242-2.</p>""",
    "Réécriture à droit constant : la possibilité de prise d'effet anticipée est placée avant les situations qui l'autorisent. Aucune réforme de fond ni ajout d'un motif de remplacement.",
    "Les trois catégories de remplacement et les renvois aux 4° et 5° de L. 1242-2 sont conservés. La prise d'effet reste située avant l'absence de la personne à remplacer. L'inapplicabilité de cette règle pendant la période d'essai prévue à L. 1242-11 est maintenue dans ce dernier article."
)

draft(
    'L1242-10',
    """<p>Une période d'essai peut être prévue dans le contrat de travail à durée déterminée.</p>
<p>La durée de l'essai ne peut excéder celle calculée à raison d'un jour par semaine. Elle est en outre limitée à deux semaines lorsque la durée initialement prévue au contrat est au plus égale à six mois, et à un mois dans les autres cas. Les durées plus courtes prévues par les usages ou les stipulations conventionnelles s'appliquent.</p>
<p>Pour un contrat sans terme précis, la durée minimale du contrat sert de base au calcul de la période d'essai.</p>""",
    "Réécriture à droit constant : la règle de calcul, les deux plafonds et la réserve des durées plus courtes sont exprimés dans des phrases distinctes du même alinéa. Aucune réforme de fond : l'essai de trois mois sans renouvellement prévu pour les nouveaux CDI n'est pas étendu aux CDD.",
    "Calcul d'un jour par semaine, plafond de deux semaines pour une durée initiale au plus égale à six mois et d'un mois dans les autres cas conservés. Les usages et stipulations conventionnelles ne peuvent ici imposer une durée plus longue que ces bornes. La durée minimale reste la base de calcul du contrat sans terme précis. Les trois alinéas sont maintenus."
)

draft(
    'L1242-11',
    """<p>Pendant la période d'essai, les dispositions suivantes ne s'appliquent pas :</p>
<p>1° Celles relatives à la prise d'effet du contrat, prévue à l'article L. 1242-9 ;</p>
<p>2° Celles relatives à la rupture anticipée du contrat, prévue aux articles L. 1243-1 à L. 1243-4 ;</p>
<p>3° Celles relatives au report du terme du contrat, prévu à l'article L. 1243-7 ;</p>
<p>4° Celles relatives à l'indemnité de fin de contrat, prévue à l'article L. 1243-8.</p>""",
    "Réécriture à droit constant : le champ temporel de l'exclusion est placé en tête et les quatre catégories de règles sont présentées parallèlement. Aucune réforme de fond des effets de la période d'essai du CDD.",
    "Les quatre subdivisions et tous les renvois sont conservés, notamment l'ensemble de L. 1243-1 à L. 1243-4. L'accord grammatical de « prévu » avec le report du terme est régularisé sans effet juridique. Aucune nouvelle exclusion de droit n'est ajoutée au titre de la réforme de l'essai des CDI."
)

draft(
    'L1242-12',
    """<p>L'employeur établit le contrat de travail à durée déterminée par écrit et y définit précisément son motif. À défaut, le contrat est réputé conclu pour une durée indéterminée.</p>
<p>Le contrat doit notamment mentionner :</p>
<p>1° Les nom et qualification professionnelle de la personne remplacée, lorsque le contrat est conclu au titre des 1°, 4° et 5° de l'article L. 1242-2 ;</p>
<p>2° La date du terme et, s'il y a lieu, une clause de renouvellement, lorsque le contrat comporte un terme précis ;</p>
<p>3° La durée minimale du contrat lorsqu'aucun terme précis n'est fixé ;</p>
<p>4° La désignation du poste de travail, en indiquant, le cas échéant, s'il figure sur la liste des postes présentant des risques particuliers pour la santé ou la sécurité des salariés prévue à l'article L. 4154-2, la désignation de l'emploi occupé ou, lorsque le contrat est conclu pour assurer au salarié un complément de formation professionnelle au titre du 2° de l'article L. 1242-3, la désignation de la nature des activités auxquelles le salarié participe dans l'entreprise ;</p>
<p>5° L'intitulé de la convention collective applicable ;</p>
<p>6° La durée de la période d'essai, si une telle période est prévue ;</p>
<p>7° Le montant de la rémunération et de chacune de ses composantes, y compris les primes et accessoires de salaire, s'il en existe ;</p>
<p>8° Les nom et adresse de la caisse de retraite complémentaire et, le cas échéant, ceux de l'organisme de prévoyance.</p>""",
    "Réécriture à droit constant : l'employeur est expressément désigné pour l'établissement de l'écrit et la définition du motif ; les mentions sont formulées comme le contenu obligatoire du contrat. Les huit rubriques et la présomption de durée indéterminée restent à leur place. Aucune réforme de fond des formalités du CDD.",
    "Maintien de l'écrit, de la précision du motif, de la sanction prévue au premier alinéa et du caractère non exhaustif de la liste introduite par « notamment ». Le 4° conserve la distinction entre poste, emploi et activités de formation ainsi que L. 4154-2 et le 2° de L. 1242-3. Les mentions relatives aux composantes de rémunération, à la retraite complémentaire et à la prévoyance ne sont pas supprimées au titre d'une simplification administrative."
)

draft(
    'L1242-12-1',
    """<p>Le contrat de travail à durée déterminée conclu en application du 6° de l'article L. 1242-2 doit comporter, en plus des autres mentions requises :</p>
<p>1° La mention « contrat à durée déterminée à objet défini » ;</p>
<p>2° L'intitulé et les références de l'accord collectif instituant ce contrat ;</p>
<p>3° Une clause décrivant le projet et indiquant sa durée prévisible ;</p>
<p>4° La définition des tâches pour lesquelles le contrat est conclu ;</p>
<p>5° L'événement ou le résultat objectif qui détermine la fin de la relation contractuelle ;</p>
<p>6° Le délai de prévenance de l'arrivée du terme et, le cas échéant, de la proposition de poursuivre la relation de travail en contrat à durée indéterminée ;</p>
<p>7° Une clause précisant que chacune des parties peut rompre le contrat à la date anniversaire de sa conclusion pour un motif réel et sérieux. Cette clause précise aussi que, si l'employeur prend l'initiative de cette rupture, le salarié a droit à une indemnité égale à 10 % de sa rémunération totale brute.</p>""",
    "Réécriture à droit constant : la nature supplémentaire des mentions est explicite, la clause de projet est reformulée directement et les deux éléments de la clause de rupture sont répartis entre deux phrases du même 7°. Aucune réforme de fond ni application de l'indemnité légale de licenciement du CDI à cette indemnité propre au CDD.",
    "Les sept mentions, le renvoi au 6° de L. 1242-2, le motif réel et sérieux et le taux de 10 % de la rémunération totale brute sont conservés. Discordance préexistante : le 7° ne mentionne que la date anniversaire, tandis que L. 1243-1, lu dans le corpus, permet aussi la rupture dix-huit mois après la conclusion puis à la date anniversaire. Une coordination de ces deux textes est à examiner ; la possibilité à dix-huit mois n'est pas ajoutée silencieusement à la clause ici."
)

draft(
    'L1242-13',
    """<p>L'employeur transmet le contrat de travail au salarié au plus tard dans les deux jours ouvrables qui suivent l'embauche.</p>""",
    "Réécriture à droit constant : l'employeur devient le sujet explicite de l'obligation de transmission. Aucune réforme de fond du délai ni des modalités prévues par cet article.",
    "Délai maximal de deux jours ouvrables suivant l'embauche conservé, sans substitution de jours ouvrés ni déplacement du point de départ à la signature du contrat. L'écrit reste régi par L. 1242-12."
)

draft(
    'L1242-14',
    """<p>Les dispositions légales, les stipulations conventionnelles et les règles résultant des usages applicables aux salariés en contrat de travail à durée indéterminée s'appliquent aussi aux salariés en contrat à durée déterminée. Les dispositions relatives à la rupture du contrat de travail sont exclues de cette application.</p>""",
    "Réécriture à droit constant : la règle commune et l'exception concernant la rupture sont distinguées dans deux phrases du même alinéa. Aucune réforme de fond du régime d'exécution des CDD ni de leurs règles particulières de rupture.",
    "Les trois sources de règles, légales, conventionnelles et issues des usages, sont conservées ainsi que l'exception relative à la rupture. L'articulation avec les règles spéciales du CDD, notamment l'essai régi par L. 1242-10 et L. 1242-11, est maintenue. Cet article ne crée aucun transfert automatique aux CDD de l'essai de trois mois ou de l'indemnité de licenciement proposés pour les CDI."
)

draft(
    'L1242-15',
    """<p>Le salarié titulaire d'un contrat de travail à durée déterminée doit percevoir une rémunération, au sens de l'article L. 3221-3, au moins égale à celle que percevrait, dans la même entreprise, un salarié en contrat de travail à durée indéterminée de qualification professionnelle équivalente exerçant les mêmes fonctions. La rémunération de comparaison est celle applicable après la période d'essai du salarié en contrat à durée indéterminée.</p>""",
    "Réécriture à droit constant : la rémunération minimale de comparaison et la situation du salarié en CDI après essai sont exposées dans deux phrases. Aucune réforme de fond ; aucune attente liée à l'essai du salarié en CDD n'est créée.",
    "Renvoi à la définition de la rémunération de L. 3221-3, comparaison dans la même entreprise, qualification professionnelle équivalente et identité des fonctions conservés. La référence à l'après-essai concerne le salarié de comparaison en CDI. Aucun abaissement de rémunération n'est introduit par la réforme du contrat de référence."
)

draft(
    'L1242-16',
    """<p>Lorsque le régime de congés applicable dans l'entreprise ne lui permet pas de prendre effectivement ses congés payés, le salarié en contrat de travail à durée déterminée bénéficie d'une indemnité compensatrice de congés payés. Elle lui est due au titre du travail effectivement accompli pendant le contrat, quelle qu'ait été la durée de celui-ci.</p>
<p>Le montant de cette indemnité est calculé en fonction de cette durée. Il doit être au moins égal au dixième de la rémunération totale brute perçue par le salarié pendant son contrat.</p>
<p>L'employeur verse l'indemnité à la fin du contrat, sauf si le contrat à durée déterminée se poursuit par un contrat de travail à durée indéterminée.</p>""",
    "Réécriture à droit constant : la condition tenant au régime des congés est placée en tête ; le droit à indemnité, son calcul et son versement sont précisés dans les trois alinéas d'origine. Aucune réforme de fond du taux minimal ou de l'exception de poursuite en CDI.",
    "Conservation du travail effectivement accompli, de l'absence de durée minimale de contrat, de la condition d'impossibilité de prise effective des congés et du minimum d'un dixième de la rémunération totale brute perçue pendant le contrat. Le versement reste dû à la fin du CDD, sous l'exception inchangée de poursuite par un CDI. Cette indemnité de congés payés reste distincte de l'indemnité de fin de contrat et de l'indemnité de licenciement."
)


def main():
    sources = json.loads(Path('source.json').read_text())
    if len(sources) != 24:
        raise ValueError('Nombre de sources inattendu')
    if set(DRAFTS) != {a['number'] for a in sources}:
        raise ValueError('Liste des articles différente')
    answer = []
    for source in sources:
        xml, reason, notes = DRAFTS[source['number']]
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


if __name__ == '__main__':
    main()
