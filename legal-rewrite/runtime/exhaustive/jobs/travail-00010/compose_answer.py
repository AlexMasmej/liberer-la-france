import json
from pathlib import Path


drafts = {}


def draft(number, xml, reason, notes):
    assert number not in drafts
    drafts[number] = (xml.strip(), reason, notes)


draft(
    "L1245-1",
    """
<p>Tout contrat de travail conclu en méconnaissance de l'une des dispositions des articles L. 1242-1 à L. 1242-4, L. 1242-6, L. 1242-7, L. 1242-8-1, du premier alinéa de l'article L. 1242-12, du premier alinéa de l'article L. 1243-11, des articles L. 1243-13-1, L. 1244-3-1 et L. 1244-4-1, ou des stipulations des conventions ou accords de branche conclus en application des articles L. 1242-8, L. 1243-13, L. 1244-3 et L. 1244-4, est réputé à durée indéterminée.</p>
<p>Le manquement à l'obligation de transmettre le contrat de mission au salarié dans le délai fixé à l'article L. 1242-13 ne peut, à lui seul, entraîner la requalification en contrat à durée indéterminée. Ce manquement donne au salarié droit à une indemnité à la charge de l'employeur, dont le montant ne peut excéder un mois de salaire.</p>
""",
    "Réécriture à droit constant : le premier alinéa identifie directement les manquements entraînant la qualification de contrat à durée indéterminée et rattache explicitement chaque renvoi à son article ou à son alinéa. Le second distingue l'absence de requalification fondée sur le seul retard de transmission et le droit à indemnité. Aucune réforme de fond du projet ne modifie ici le régime des CDD.",
    "Les deux alinéas et tous les renvois sont conservés, ainsi que le plafond d'un mois de salaire. Incohérence préexistante : le second alinéa vise un « contrat de mission » alors que cet article relève des CDD et que L. 1242-13 régit leur transmission ; cette expression est conservée sans correction silencieuse. Le renvoi à L. 1242-13 maintient son délai, exprimé en jours ouvrables dans le corpus. Note historique à conserver avec l'article : conformément aux I et VIII de l'article 40 de l'ordonnance n° 2017-1387 du 22 septembre 2017, ces dispositions s'appliquent aux licenciements prononcés et aux contrats de travail conclus postérieurement à la publication de cette ordonnance. Cette note n'établit aucune date d'entrée en vigueur de la réforme projetée.",
)

draft(
    "L1245-2",
    """
<p>La demande de requalification d'un contrat de travail à durée déterminée en contrat à durée indéterminée, présentée au conseil de prud'hommes, est portée directement devant le bureau de jugement. Celui-ci statue au fond dans le délai d'un mois suivant sa saisine.</p>
<p>Si le conseil de prud'hommes fait droit à la demande du salarié, il lui accorde une indemnité à la charge de l'employeur, d'un montant au moins égal à un mois de salaire. L'octroi de cette indemnité ne fait pas obstacle à l'application des règles de rupture du contrat de travail à durée indéterminée prévues au titre III du présent livre.</p>
""",
    "Réécriture à droit constant : la saisine directe du bureau de jugement et le délai dans lequel il statue sont présentés en deux phrases. La décision favorable au salarié, le débiteur de l'indemnité et son minimum sont explicités ; l'application des règles de rupture reste distincte. Aucune réforme de fond n'est appliquée à cette indemnité de requalification.",
    "Deux alinéas conservés. Délai de jugement d'un mois à compter de la saisine du bureau et indemnité minimale d'un mois de salaire maintenus. Le renvoi au titre III du livre II est conservé : l'indemnité de requalification ne doit pas être confondue avec l'indemnité légale de licenciement visée par les coordinations L. 1234-9 et R. 1234-1 et suivants.",
)

draft(
    "L1246-1",
    """
<p>Dans les secteurs des spectacles, de l'action culturelle, de l'audiovisuel, de la production cinématographique et de l'édition phonographique, les agents de contrôle mentionnés à l'article L. 8112-1 ainsi que les agents du Centre national du cinéma et de l'image animée, des directions régionales des affaires culturelles, de l'institution mentionnée à l'article L. 5312-1 et de l'organisme gestionnaire du régime d'assurance chômage se communiquent réciproquement, sur demande écrite, tous les renseignements et documents nécessaires à la recherche et à la constatation des infractions aux dispositions du 3° de l'article L. 1242-2. Cette communication porte également, le cas échéant, sur les renseignements et documents nécessaires à la recherche et à la constatation des manquements aux dispositions mentionnées au 11° et des infractions aux dispositions mentionnées au 12° de l'article L. 421-1 du code du cinéma et de l'image animée.</p>
""",
    "Réécriture à droit constant : la longue phrase est scindée au sein du même alinéa pour distinguer les infractions relatives aux CDD des manquements et infractions du code du cinéma. Les destinataires, la réciprocité et l'exigence de demande écrite sont maintenus. Aucune réforme de fond ni extension des échanges de données n'est introduite.",
    "L'alinéa unique, les cinq secteurs et l'ensemble des catégories d'agents sont conservés. Le caractère éventuel du second champ de communication et la distinction entre manquements au titre du 11° et infractions au titre du 12° sont maintenus. Les renvois à L. 8112-1, L. 5312-1 et L. 421-1 du code du cinéma et de l'image animée sont reproduits ; le contenu de ce dernier code, hors corpus fourni, n'a pas été vérifié.",
)

draft(
    "L1247-1",
    """
<p>Les organisations syndicales représentatives dans l'entreprise peuvent engager, en faveur d'un salarié, toutes les actions en justice résultant du présent titre, sans avoir à justifier d'un mandat de ce salarié.</p>
<p>L'action peut être exercée si le salarié, averti dans les conditions fixées par voie réglementaire, ne s'y est pas opposé dans les quinze jours à compter de la date à laquelle l'organisation syndicale lui a notifié son intention d'agir.</p>
<p>Le salarié peut, à tout moment, intervenir dans l'instance engagée par l'organisation syndicale et y mettre un terme.</p>
""",
    "Réécriture à droit constant : la faculté d'action syndicale, la condition d'absence d'opposition du salarié et les pouvoirs de ce dernier dans l'instance sont formulés séparément et avec des sujets explicites. Aucune réforme de fond ne restreint le recours au juge ou les libertés collectives.",
    "Les trois alinéas sont conservés. La représentativité dans l'entreprise, la dispense de justification d'un mandat, les conditions réglementaires d'information et le délai de quinze jours courant depuis la notification de l'intention d'agir demeurent. Le salarié conserve tant l'intervention à l'instance que la faculté d'y mettre fin à tout moment.",
)

draft(
    "L1248-1",
    """
<p>Conclure, en méconnaissance de l'article L. 1242-1, un contrat de travail à durée déterminée ayant pour objet de pourvoir durablement un emploi lié à l'activité normale et permanente de l'entreprise est puni d'une amende de 3 750 euros. Cette peine s'applique également lorsque le contrat a cet effet.</p>
<p>En cas de récidive, les peines sont une amende de 7 500 euros et un emprisonnement de six mois.</p>
""",
    "Réécriture à droit constant : l'infraction est présentée à partir de la conclusion du CDD, en distinguant son objet de son effet. La récidive fait l'objet d'une phrase autonome. Aucune réforme de fond ne modifie l'interdiction ou les peines.",
    "Deux alinéas maintenus. La seconde phrase du premier alinéa vise le même contrat, à durée déterminée. Renvoi à L. 1242-1, amendes de 3 750 et 7 500 euros et emprisonnement de six mois en récidive conservés ; ni l'objet ni l'effet durablement substitutif à un emploi normal et permanent ne sont retirés du champ pénal.",
)

draft(
    "L1248-2",
    """
<p>Conclure un contrat de travail à durée déterminée est puni d'une amende de 3 750 euros si son objet est autre que celui prévu au premier alinéa de l'article L. 1242-2 ou s'il est conclu en dehors des cas prévus à ce même article et à l'article L. 1242-3.</p>
<p>En cas de récidive, les peines sont une amende de 7 500 euros et un emprisonnement de six mois.</p>
""",
    "Réécriture à droit constant : les deux hypothèses de conclusion illicite du CDD sont formulées comme des conditions explicites de la sanction. Le renvoi particulier au premier alinéa reste distinct du renvoi à l'ensemble des cas de recours. Aucune réforme de fond n'est introduite.",
    "Deux alinéas et les deux branches alternatives de l'infraction conservés. L. 1242-2 et L. 1242-3 ont été consultés dans le corpus public pour contrôler les renvois, sans modification de leurs cas de recours. Amendes de 3 750 et 7 500 euros et peine de six mois d'emprisonnement en récidive maintenues.",
)

draft(
    "L1248-3",
    """
<p>Méconnaître les interdictions relatives à la conclusion d'un contrat de travail à durée déterminée, prévues aux articles L. 1242-5 et L. 1242-6, est puni d'une amende de 3 750 euros.</p>
<p>En cas de récidive, les peines sont une amende de 7 500 euros et un emprisonnement de six mois.</p>
""",
    "Réécriture à droit constant : les interdictions sanctionnées sont nommées avant les articles qui les prévoient, et la sanction de la récidive est formulée directement. Aucune réforme de fond n'étend ou ne réduit l'incrimination.",
    "Deux alinéas conservés malgré le remplacement des sauts de ligne de présentation par des paragraphes. Les renvois à L. 1242-5 et L. 1242-6 maintiennent leurs champs et exceptions propres. Amendes de 3 750 et 7 500 euros et emprisonnement de six mois en récidive inchangés.",
)

draft(
    "L1248-4",
    """
<p>Conclure un contrat de travail à durée déterminée sans en fixer précisément le terme dès sa conclusion, en méconnaissance de l'article L. 1242-7, est puni d'une amende de 3 750 euros.</p>
<p>L'employeur encourt la même peine s'il conclut un contrat de travail à durée déterminée sans terme précis et sans en fixer la durée minimale.</p>
<p>En cas de récidive, les peines sont une amende de 7 500 euros et un emprisonnement de six mois.</p>
""",
    "Réécriture à droit constant : les deux comportements sanctionnés sont distingués, l'un concernant la précision du terme exigée par L. 1242-7, l'autre l'absence de durée minimale du CDD sans terme précis. Le sujet employeur est explicite au deuxième alinéa. Aucune réforme de fond n'est appliquée.",
    "Trois alinéas conservés. Le renvoi à L. 1242-7 maintient les cas dans lesquels un CDD peut légalement ne pas comporter de terme précis ; le premier alinéa ne les supprime pas. La durée minimale du deuxième alinéa reste celle de ce régime et n'est pas concernée par la suppression du plancher général de travail à temps partiel. Peines de 3 750 euros, puis 7 500 euros et six mois d'emprisonnement en récidive, maintenues.",
)

draft(
    "L1248-5",
    """
<p>En matière de durée du contrat de travail à durée déterminée, méconnaître les stipulations d'une convention ou d'un accord de branche prises en application de l'article L. 1242-8 ou, lorsqu'elles s'appliquent, les dispositions des articles L. 1242-8-1 et L. 1242-8-2, est puni d'une amende de 3 750 euros. En cas de récidive, les peines sont une amende de 7 500 euros et un emprisonnement de six mois.</p>
""",
    "Réécriture à droit constant : l'objet des règles sanctionnées, la durée du CDD, est placé en tête de phrase. La condition d'application des dispositions légales est conservée, sans confondre leur rôle avec celui des stipulations de branche. Aucune réforme de fond des durées ou des peines n'est introduite.",
    "Alinéa unique et renvois à L. 1242-8, L. 1242-8-1 et L. 1242-8-2 maintenus. Amendes de 3 750 et 7 500 euros et emprisonnement de six mois en récidive conservés. Note historique à conserver avec l'article : l'article 40-VIII de l'ordonnance n° 2017-1387 du 22 septembre 2017 rend ces dispositions applicables aux contrats de travail conclus postérieurement à la publication de cette ordonnance. Les contrats antérieurs ne sont pas soumis rétroactivement à cette rédaction.",
)

draft(
    "L1248-6",
    """
<p>Ne pas établir par écrit le contrat de travail à durée déterminée et ne pas y définir précisément son motif, en méconnaissance du premier alinéa de l'article L. 1242-12, est puni d'une amende de 3 750 euros.</p>
<p>En cas de récidive, les peines sont une amende de 7 500 euros et un emprisonnement de six mois.</p>
""",
    "Réécriture à droit constant : les exigences d'écrit et de définition du motif sont exprimées directement, sans la formule introductive « le fait de ». La structure de l'incrimination et la sanction de la récidive sont conservées. Aucune réforme de fond ne modifie les exigences de forme du CDD.",
    "Deux alinéas maintenus. La conjonction « et » qui relie les deux défauts dans la source est conservée : elle n'est pas remplacée par « ou », ce qui pourrait modifier l'incrimination. Le renvoi reste limité au premier alinéa de L. 1242-12, et non à toutes les mentions de cet article. Amendes de 3 750 et 7 500 euros et emprisonnement de six mois en récidive maintenus.",
)

draft(
    "L1248-7",
    """
<p>L'absence de transmission au salarié du contrat de travail à durée déterminée au plus tard dans les deux jours suivant l'embauche, en méconnaissance de l'article L. 1242-13, est punie d'une amende de 3 750 euros.</p>
<p>En cas de récidive, les peines sont une amende de 7 500 euros et un emprisonnement de six mois.</p>
""",
    "Réécriture à droit constant : le défaut de transmission, son destinataire et son échéance sont regroupés dans une formulation directe, puis la récidive est distinguée. Aucune réforme de fond du délai de transmission ou des sanctions n'est introduite.",
    "Deux alinéas et renvoi à L. 1242-13 conservés. Écart de rédaction préexistant à contrôler : la source pénale mentionne « deux jours », tandis que L. 1242-13, consulté dans le corpus public, mentionne « deux jours ouvrables ». Le qualificatif n'est pas ajouté silencieusement à l'incrimination. Les montants de 3 750 et 7 500 euros et les six mois d'emprisonnement en récidive sont conservés.",
)

draft(
    "L1248-8",
    """
<p>Le versement à un salarié titulaire d'un contrat de travail à durée déterminée d'une rémunération inférieure à la rémunération de référence prévue à l'article L. 1242-15 est puni d'une amende de 3 750 euros. Cette référence est la rémunération que percevrait, dans la même entreprise et après la période d'essai, un salarié sous contrat de travail à durée indéterminée de qualification professionnelle équivalente et occupant les mêmes fonctions.</p>
<p>En cas de récidive, les peines sont une amende de 7 500 euros et un emprisonnement de six mois.</p>
""",
    "Réécriture à droit constant : la première phrase expose le versement sanctionné, et la seconde définit intégralement la rémunération de comparaison dans le même alinéa. Les critères d'entreprise, d'essai, de qualification et de fonctions restent cumulatifs. Aucune réforme de fond ne modifie l'égalité de rémunération.",
    "Deux alinéas conservés. La référence reste hypothétique (« que percevrait ») et ne suppose pas la présence effective d'un salarié comparable en CDI. La mention de la période d'essai n'introduit ici aucune nouvelle durée et n'étend pas aux CDD la réforme de l'essai des nouveaux CDI. Renvoi à L. 1242-15 vérifié dans le corpus. Amendes de 3 750 et 7 500 euros et emprisonnement de six mois en récidive maintenus.",
)

draft(
    "L1248-9",
    """
<p>La méconnaissance des règles de prorogation du contrat de travail à durée déterminée d'un salarié exposé à des rayonnements ionisants, prévues à l'article L. 1243-12, est punie d'une amende de 3 750 euros.</p>
<p>En cas de récidive, les peines sont une amende de 7 500 euros et un emprisonnement de six mois.</p>
""",
    "Réécriture à droit constant : le régime particulier de prorogation et les salariés concernés sont identifiés avant le renvoi qui les régit. La récidive est exprimée séparément. Aucune réforme de fond ne modifie cette protection contre l'exposition aux rayonnements ionisants.",
    "Deux alinéas maintenus. L. 1243-12 a été consulté dans le corpus : il s'agit d'une prorogation liée à l'exposition, non d'un renouvellement ordinaire du CDD ; ce régime distinct est conservé par le renvoi. Amendes de 3 750 et 7 500 euros et emprisonnement de six mois en récidive inchangés.",
)

draft(
    "L1248-10",
    """
<p>Renouveler un contrat de travail à durée déterminée sans respecter les stipulations d'une convention ou d'un accord de branche prises en application de l'article L. 1243-13 ou, lorsqu'elles s'appliquent, les dispositions de l'article L. 1243-13-1, est puni d'une amende de 3 750 euros. En cas de récidive, les peines sont une amende de 7 500 euros et un emprisonnement de six mois.</p>
""",
    "Réécriture à droit constant : le renouvellement irrégulier est formulé directement, en conservant l'articulation entre stipulations de branche et dispositions légales applicables. La peine de récidive est explicitée. Aucune réforme de fond des renouvellements n'est appliquée.",
    "Alinéa unique conservé. Renvois à L. 1243-13 et L. 1243-13-1, amendes de 3 750 et 7 500 euros et emprisonnement de six mois en récidive maintenus. Note historique à conserver avec l'article : conformément à l'article 40-VIII de l'ordonnance n° 2017-1387 du 22 septembre 2017, ces dispositions s'appliquent aux contrats de travail conclus postérieurement à la publication de cette ordonnance. Aucun basculement des contrats antérieurs n'est créé.",
)

draft(
    "L1248-11",
    """
<p>En matière de succession de contrats sur un même poste, méconnaître les stipulations d'une convention ou d'un accord de branche prises en application de l'article L. 1244-3 ou, lorsqu'elles sont applicables, les dispositions de l'article L. 1244-3-1, est puni d'une amende de 3 750 euros. En cas de récidive, les peines sont une amende de 7 500 euros et un emprisonnement de six mois.</p>
""",
    "Réécriture à droit constant : la succession de contrats sur un même poste est annoncée avant les règles dont la méconnaissance est sanctionnée. Le caractère conditionnel de l'application des dispositions légales est conservé. Aucune réforme de fond du délai de carence ou des sanctions n'est introduite.",
    "Alinéa unique, renvois à L. 1244-3 et L. 1244-3-1 et peines de 3 750 euros, puis de 7 500 euros et six mois d'emprisonnement en récidive, maintenus. Note historique à conserver avec l'article : l'article 40-VIII de l'ordonnance n° 2017-1387 du 22 septembre 2017 prévoit l'application aux contrats de travail conclus postérieurement à la publication de cette ordonnance. Les exceptions propres au régime de succession des contrats ne sont pas supprimées par cette réécriture.",
)

draft(
    "L1251-1",
    """
<p>Le travail temporaire consiste, pour une entreprise de travail temporaire, à mettre temporairement un salarié à la disposition d'un client utilisateur pour l'exécution d'une mission.</p>
<p>Pour chaque mission, les contrats suivants sont conclus :</p>
<p>1° Un contrat de mise à disposition entre l'entreprise de travail temporaire et le client utilisateur, appelé « entreprise utilisatrice » ;</p>
<p>2° Un contrat de travail, appelé « contrat de mission », entre le salarié temporaire et son employeur, l'entreprise de travail temporaire.</p>
<p>Si l'utilisateur est une personne morale de droit public, le présent chapitre s'applique sous réserve des dispositions de la section 6.</p>
""",
    "Réécriture à droit constant : la définition décrit directement la mise à disposition, puis énonce les deux contrats et leurs parties. La règle propre à l'utilisateur public est formulée comme une condition explicite. Aucune réforme de fond ne fusionne les contrats ou n'étend les réformes du CDI à la mission.",
    "Les cinq alinéas, les 1° et 2°, les deux dénominations contractuelles et la qualité d'employeur de l'entreprise de travail temporaire sont conservés. La réserve de la section 6 reste applicable aux personnes morales de droit public ; aucun raccordement automatique à une réforme visant les employeurs privés n'est créé.",
)

draft(
    "L1251-2",
    """
<p>Est entrepreneur de travail temporaire toute personne physique ou morale dont l'activité exclusive consiste à mettre temporairement des salariés à la disposition d'entreprises utilisatrices. Cette personne recrute et rémunère ces salariés à cette fin, en fonction d'une qualification convenue.</p>
""",
    "Réécriture à droit constant : la définition et l'exclusivité de l'activité sont isolées dans une première phrase ; la seconde précise qui recrute et rémunère les salariés et à quelle fin. Aucune réforme de fond de l'activité de travail temporaire n'est introduite.",
    "Alinéa unique maintenu. Personnes physiques et morales, exclusivité, mise à disposition temporaire, recrutement et rémunération selon une qualification convenue sont conservés. Lire cette exclusivité avec les dérogations de L. 1251-4 ; aucune nouvelle dérogation n'est ajoutée.",
)

draft(
    "L1251-3",
    """
<p>L'activité de travail temporaire ne peut être exercée qu'au sein d'une entreprise de travail temporaire. Cette interdiction s'applique sous réserve des règles relatives aux opérations de prêt de main-d'œuvre à but non lucratif autorisées par l'article L. 8241-2.</p>
""",
    "Réécriture à droit constant : le renvoi implicite à « une telle entreprise » est remplacé par la désignation explicite de l'entreprise de travail temporaire. La réserve du prêt de main-d'œuvre non lucratif est présentée séparément dans le même alinéa. Aucune réforme de fond de l'interdiction n'est introduite.",
    "Alinéa unique et renvoi à L. 8241-2 conservés. Cet article a été consulté dans le corpus pour confirmer que la réserve concerne les opérations de prêt de main-d'œuvre à but non lucratif autorisées selon leurs conditions propres ; la réécriture ne dispense pas de ces conditions.",
)

draft(
    "L1251-4",
    """
<p>Les entreprises de travail temporaire peuvent, par dérogation au principe d'exclusivité prévu à l'article L. 1251-2, exercer les activités suivantes :</p>
<p>1° Les activités de placement privé prévues à l'article L. 5321-1 ;</p>
<p>2° L'activité d'entreprise de travail à temps partagé.</p>
""",
    "Réécriture à droit constant : le sujet autorisé à exercer les activités est placé au début de l'alinéa et les deux dérogations restent énumérées sous leurs numéros. Les dénominations techniques nécessaires sont conservées. Aucune réforme de fond ni activité supplémentaire n'est introduite.",
    "Trois alinéas et subdivisions 1° et 2° conservés. L'articulation avec l'exclusivité de L. 1251-2 et le renvoi au placement privé prévu à L. 5321-1 sont maintenus. Ce dernier article a été consulté dans le corpus ; les deux activités autorisées ne sont ni fusionnées ni élargies.",
)

draft(
    "L1251-5",
    """
<p>Quel que soit son motif, un contrat de mission ne peut avoir pour objet de pourvoir durablement un emploi lié à l'activité normale et permanente de l'entreprise utilisatrice. Il ne peut pas davantage produire cet effet.</p>
""",
    "Réécriture à droit constant : l'interdiction portant sur l'objet du contrat et celle portant sur ses effets sont énoncées en deux phrases au sein du même alinéa. Le caractère indifférent du motif de recours demeure. Aucune réforme de fond ne permet de pourvoir un emploi permanent par une mission.",
    "Alinéa unique maintenu. Les critères cumulatifs d'emploi lié à l'activité normale et permanente et de pourvoi durable sont conservés, de même que l'alternative entre objet et effet interdits. Cette règle reste distincte des cas de recours énumérés à L. 1251-6 et L. 1251-7.",
)

draft(
    "L1251-6",
    """
<p>Sous réserve de l'article L. 1251-7, le recours à un salarié temporaire est limité à l'exécution d'une tâche précise et temporaire, appelée « mission ». Il n'est autorisé que dans les cas suivants :</p>
<p>1° Le remplacement d'un salarié dans l'une des situations suivantes :</p>
<p>a) L'absence du salarié ;</p>
<p>b) Son passage provisoire à temps partiel, convenu par un avenant à son contrat de travail ou par un échange écrit entre lui et son employeur ;</p>
<p>c) La suspension de son contrat de travail ;</p>
<p>d) Son départ définitif précédant la suppression de son poste de travail après consultation du comité social et économique, s'il existe ;</p>
<p>e) L'attente de l'entrée en service effective d'un salarié recruté par contrat à durée indéterminée pour le remplacer ;</p>
<p>2° L'accroissement temporaire de l'activité de l'entreprise ;</p>
<p>3° Les emplois à caractère saisonnier définis au 3° de l'article L. 1242-2 ou les emplois pour lesquels il est d'usage constant de ne pas recourir au contrat de travail à durée indéterminée en raison de la nature de l'activité exercée et du caractère par nature temporaire de ces emplois. Dans ce dernier cas, les secteurs concernés sont définis par décret ou par convention ou accord collectif étendu ;</p>
<p>4° Le remplacement de l'une des personnes suivantes : un chef d'entreprise artisanale, industrielle ou commerciale ; une personne exerçant une profession libérale ; son conjoint participant effectivement à l'activité de l'entreprise à titre professionnel et habituel ; un associé non salarié d'une société civile professionnelle, d'une société civile de moyens, d'une société d'exercice libéral ou de toute autre personne morale exerçant une profession libérale ;</p>
<p>5° Le remplacement du chef d'une exploitation agricole ou d'une entreprise mentionnée aux 1° à 4° de l'article L. 722-1 du code rural et de la pêche maritime, d'un aide familial, d'un associé d'exploitation ou de leur conjoint mentionné à l'article L. 722-10 du même code, dès lors que ce conjoint participe effectivement à l'activité de l'exploitation agricole ou de l'entreprise.</p>
""",
    "Réécriture à droit constant : la tâche autorisée et le caractère limitatif des cas de recours sont énoncés séparément. Les situations de remplacement conservent leurs lettres ; le 3° distingue les emplois saisonniers des emplois d'usage et précise la définition des secteurs dans une seconde phrase. Le 4° est ponctué pour rendre lisibles les personnes et structures concernées. Aucune réforme de fond ne modifie les cas de recours ou le temps partiel mentionné au b).",
    "Les onze alinéas, les 1° à 5° et les lettres a) à e) sont conservés. Maintien de la réserve de L. 1251-7, du renvoi au 3° de L. 1242-2, de l'avenant ou échange écrit au b), de la consultation du CSE s'il existe au d), et du recrutement en CDI au e). Les secteurs d'usage restent définis par décret ou convention ou accord collectif étendu. Au 4°, la source juxtapose « société civile de moyens d'une société d'exercice libéral » sans virgule : la ponctuation proposée rend explicite l'énumération de ces deux types de sociétés ; ce défaut de ponctuation préexistant est signalé pour contrôle. La formulation « son conjoint » est conservée sans en redéfinir le rattachement. Au 5°, les renvois au code rural et la participation effective du conjoint sont maintenus ; ce code est hors corpus fourni et ses articles n'ont pas été consultés.",
)

draft(
    "L1251-7",
    """
<p>En plus des cas prévus à l'article L. 1251-6, un salarié temporaire peut être mis à la disposition d'une entreprise utilisatrice dans les cas suivants :</p>
<div><p>1° Lorsque la mission de travail temporaire a pour objet, en application de dispositions légales ou d'un accord de branche étendu, de favoriser le recrutement de personnes sans emploi rencontrant des difficultés sociales et professionnelles particulières ;</p></div>
<div><p>2° Lorsque l'entreprise de travail temporaire et l'entreprise utilisatrice s'engagent à assurer au salarié un complément de formation professionnelle, pour une durée et dans des conditions fixées par décret ou par accord de branche étendu ;</p></div>
<p>3° Lorsque l'entreprise de travail temporaire et l'entreprise utilisatrice s'engagent à assurer au salarié une formation professionnelle par la voie de l'apprentissage. Cette formation vise l'obtention d'une qualification professionnelle sanctionnée par un diplôme ou un titre à finalité professionnelle enregistré au répertoire national des certifications professionnelles. Elle est dispensée pour partie dans l'entreprise utilisatrice et pour partie en centre de formation d'apprentis ou section d'apprentissage, en application de l'article L. 6221-1 ;</p>
<p>4° Lorsque le salarié est l'une des personnes mentionnées à l'article L. 5212-13, à l'exclusion de celles mentionnées au 5° du même article L. 5212-13 ;<br /><br />5° Lorsque le contrat de mission est conclu en application de l'article L. 5132-6 pour une durée d'au moins un mois.</p>
""",
    "Réécriture à droit constant : le caractère complémentaire des cas de recours est explicite ; les engagements communs des deux entreprises sont formulés directement. Le 3° distingue l'engagement de formation, la qualification recherchée et les lieux de formation. Aucune réforme de fond ne modifie les publics, les engagements ou la durée minimale du 5°.",
    "Les 1° à 5° restent dans l'ordre source ; les conteneurs des 1° et 2° ainsi que le regroupement des 4° et 5° dans le dernier paragraphe avec sauts de ligne sont conservés. Maintien de l'accord de branche étendu, des conditions réglementaires ou conventionnelles du 2°, du diplôme ou titre enregistré au RNCP, des deux lieux de formation et du renvoi à L. 6221-1. L'exclusion vise toujours le seul 5° de L. 5212-13. Le minimum d'un mois du contrat de mission d'insertion de L. 5132-6 est conservé : il n'est pas le plancher hebdomadaire de vingt-quatre heures visé par la réforme du temps partiel. L. 5132-6 comporte par ailleurs un renvoi à la durée minimale de L. 3123-6 : cette coordination relève de cet autre article et n'est pas réglée en modifiant le présent 5°.",
)

draft(
    "L1251-8",
    """
<p>Pour une mission portant sur l'exercice d'une profession médicale ou paramédicale réglementée, l'entreprise de travail temporaire doit vérifier que le salarié est régulièrement autorisé à exercer cette profession.</p>
""",
    "Réécriture à droit constant : l'obligation de vérification est formulée avec son débiteur explicite et le démonstratif « ce salarié » est remplacé par une désignation directe. L'autorisation est rattachée à la profession concernée. Aucune réforme de fond de l'accès à ces professions n'est introduite.",
    "Alinéa unique maintenu. Le champ couvre les professions tant médicales que paramédicales réglementées. L'obligation reste à la charge de l'entreprise de travail temporaire et porte sur une autorisation régulière d'exercice, sans substitution d'une simple qualification ni transfert de cette obligation à l'entreprise utilisatrice.",
)

draft(
    "L1251-9",
    """
<p>Pendant les six mois qui suivent un licenciement pour motif économique, le recours à un salarié temporaire est interdit pour répondre à un accroissement temporaire de l'activité. Cette interdiction s'applique même si la mission consiste en une tâche occasionnelle, précisément définie et non durable, qui ne relève pas de l'activité normale de l'entreprise utilisatrice.</p>
<p>L'interdiction concerne les postes touchés par le licenciement dans l'établissement.</p>
<p>Elle ne s'applique pas dans les cas suivants :</p>
<p>1° Lorsque le contrat de mission ne peut être renouvelé et que sa durée ne dépasse pas trois mois ;</p>
<p>2° Lorsque le contrat est lié à une commande exceptionnelle à l'exportation survenue dans l'entreprise de l'entrepreneur principal ou dans celle d'un sous-traitant. L'importance de cette commande doit nécessiter la mise en œuvre de moyens quantitativement ou qualitativement exorbitants de ceux que l'entreprise utilise ordinairement. Le recrutement est soumis à l'information et à la consultation préalables du comité social et économique, s'il existe.</p>
<p>Même dans les cas de dérogation prévus aux 1° et 2°, l'employeur reste tenu de respecter la priorité de réembauche prévue à l'article L. 1233-45.</p>
""",
    "Réécriture à droit constant : le délai d'interdiction et son extension aux tâches occasionnelles sont énoncés en deux phrases. Le périmètre des postes, les deux dérogations et le maintien de la priorité de réembauche restent séparés. Les conditions de la commande exceptionnelle sont décomposées dans leur alinéa. Aucune réforme de fond ne supprime cette interdiction après licenciement économique.",
    "Six alinéas et subdivisions 1° et 2° conservés. Contrôle des six mois, du maximum de trois mois non renouvelable et du caractère cumulatif des qualités de la tâche occasionnelle. La commande doit rester exceptionnelle, à l'exportation, et nécessiter les moyens quantitativement ou qualitativement exorbitants décrits par la source ; les entreprises de l'entrepreneur principal et du sous-traitant restent couvertes. Information et consultation préalables du CSE s'il existe maintenues. Renvoi à L. 1233-45 vérifié dans le corpus. L'élargissement documenté du motif économique à L. 1233-3 prévu par coordination.json n'écarte ni cette interdiction ni la priorité de réembauche.",
)


def main():
    sources = json.loads(Path("source.json").read_text())
    assert len(sources) == len(drafts) == 24
    assert {a["number"] for a in sources} == set(drafts)
    answer = []
    for source in sources:
        xml, reason, notes = drafts[source["number"]]
        row = {k: source[k] for k in ("code_id", "source_id", "source_sha256", "number")}
        row.update(proposed_xml=xml, reason=reason, review_notes=notes, status="rewrite_draft")
        answer.append(row)
    Path("answer.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")
    print(f"answer.json : {len(answer)} articles")


if __name__ == "__main__":
    main()
