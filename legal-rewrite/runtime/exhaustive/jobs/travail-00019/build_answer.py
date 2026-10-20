import json
from pathlib import Path


drafts = {}


def add(number, proposed_xml, reason, review_notes):
    if number in drafts:
        raise ValueError(f"Doublon : {number}")
    drafts[number] = {
        "proposed_xml": proposed_xml,
        "reason": reason,
        "review_notes": review_notes,
    }


add(
    "L1271-8",
    """<p>Dans les conditions prévues à l'article L. 1271-12, les personnes morales de droit public peuvent acquérir des titres spéciaux de paiement préfinancés. Le prix d'acquisition est égal à la valeur libératoire des titres, à laquelle s'ajoute, le cas échéant, une commission.</p>""",
    "Réécriture à droit constant : l'autorisation d'acquérir les titres et la règle de détermination du prix sont énoncées dans deux phrases distinctes. Aucune réforme de fond n'est appliquée à ce mécanisme d'acquisition par les personnes publiques.",
    "Le renvoi à L. 1271-12, la valeur libératoire et le caractère éventuel de la commission sont conservés. Aucun montant de commission n'est ajouté.",
)

add(
    "L1271-10",
    """<p>Lorsque le chèque emploi-service universel constitue un titre spécial de paiement, il est émis par des organismes et établissements spécialisés ou par les établissements mentionnés à l'article L. 1271-9. Ces émetteurs doivent être habilités dans les conditions fixées par décret. Ils assurent le remboursement des titres aux personnes mentionnées à l'article L. 1271-1.</p>""",
    "Réécriture à droit constant : les catégories d'émetteurs, leur habilitation et leur obligation de remboursement sont présentées successivement, au lieu d'être réunies dans une seule phrase. Les réformes relatives au contrat de travail ne modifient pas ce régime d'émission.",
    "Le corpus public fourni ne contient pas d'article L. 1271-9, alors que la source y renvoie. Ce renvoi préexistant est conservé et son état doit être contrôlé, sans lui substituer un autre article. Le bénéficiaire du remboursement reste défini par L. 1271-1 ; l'habilitation demeure réglementaire.",
)

add(
    "L1271-11",
    """<p>Tout émetteur de chèques emploi-service universels constituant des titres spéciaux de paiement qui n'est pas soumis aux articles L. 312-4 à L. 312-18 du code monétaire et financier doit faire ouvrir un compte bancaire ou postal. Il y verse obligatoirement les fonds reçus en contrepartie de la cession de ces titres. Ces fonds restent sur ce compte jusqu'à leur remboursement ; aucun autre fonds ne peut y être versé.</p>""",
    "Réécriture à droit constant : le champ des émetteurs concernés, l'ouverture du compte, son alimentation obligatoire et l'exclusivité des fonds sont distingués. Aucun changement de fond n'est apporté à la protection des sommes encaissées.",
    "La condition de non-assujettissement aux articles L. 312-4 à L. 312-18 du code monétaire et financier est conservée, de même que le choix entre compte bancaire et compte postal et la conservation des fonds jusqu'au remboursement. Les modalités de fonctionnement restent visées au 5° de L. 1271-17.",
)

add(
    "L1271-12",
    """<p>Une personne peut préfinancer, en tout ou partie, le chèque emploi-service universel lorsqu'il constitue un titre spécial de paiement, au bénéfice de ses salariés, agents, ayants droit, retraités, administrés, sociétaires, adhérents ou assurés, ainsi que du chef d'entreprise ou, lorsque l'entreprise est une personne morale, de son président, de son directeur général, de son ou ses directeurs généraux délégués, de ses gérants ou des membres de son directoire, dès lors que ce titre peut également bénéficier à l'ensemble des salariés de l'entreprise selon les mêmes règles d'attribution.</p>
<p>Lorsqu'il est ainsi préfinancé, le titre de paiement porte, dès son émission, une valeur faciale. Celle-ci ne peut dépasser le montant fixé par un arrêté conjoint des ministres chargés du travail, de la sécurité sociale et de l'économie.</p>
<p>La personne qui préfinance ces chèques peut en réserver l'utilisation à certaines catégories de services parmi les activités mentionnées à l'article L. 1271-1.</p>""",
    "Réécriture à droit constant : la personne qui préfinance devient le sujet de la première phrase ; la règle de valeur faciale est divisée en deux phrases et la faculté de réserver l'utilisation est formulée directement. Aucune réforme de fond n'affecte les bénéficiaires ou le financement des titres.",
    "Toutes les catégories de bénéficiaires et de dirigeants sont maintenues. La condition tenant à la possibilité d'attribution à l'ensemble des salariés selon les mêmes règles reste à la fin du premier alinéa, sans changement de portée. Le plafond demeure fixé par arrêté conjoint des trois ministres ; aucun montant n'est créé. Les trois alinéas substantiels et le renvoi à L. 1271-1 sont conservés.",
)

add(
    "L1271-13",
    """<p>Le titre spécial de paiement est établi au nom de son bénéficiaire, dont il porte le nom.</p>
<p>Un décret peut déterminer les cas dans lesquels :</p>
<p>1° Le titre spécial de paiement est stipulé payable à une personne dénommée, notamment lorsque son préfinancement est assuré par une personne publique ou par une personne privée chargée d'une mission de service public ;</p>
<p>2° En cas d'urgence, le titre spécial de paiement demeure non nominatif jusqu'à son attribution au bénéficiaire.</p>""",
    "Réécriture à droit constant : le caractère nominatif est exprimé par l'établissement du titre au nom du bénéficiaire ; les deux cas relevant du décret sont reformulés en conservant leur numérotation. Aucune dérogation nouvelle n'est créée.",
    "Le paiement à une personne dénommée et le caractère temporairement non nominatif sont deux cas distincts. La mention des personnes privées chargées d'une mission de service public, le caractère non exhaustif de l'exemple du 1° et la condition d'urgence du 2° sont conservés.",
)

add(
    "L1271-14",
    """<p>Un arrêté conjoint des ministres chargés du travail, de la sécurité sociale et de l'économie fixe les caractéristiques du chèque emploi-service universel lorsqu'il constitue un titre spécial de paiement.</p>""",
    "Réécriture à droit constant : la phrase désigne directement l'acte réglementaire qui fixe les caractéristiques du titre, au lieu d'employer une construction passive. Aucun changement de fond n'est apporté à la compétence ministérielle.",
    "La compétence conjointe des trois ministres est maintenue. Cette disposition concerne seulement le chèque ayant la nature d'un titre spécial de paiement, et non toutes les formes du chèque emploi-service universel.",
)

add(
    "L1271-15",
    """<p>Le chèque emploi-service universel peut, selon le cas, être :</p>
<p>1° Encaissé auprès des établissements, institutions et services mentionnés à l'article L. 1271-9 ;</p>
<p>2° Remboursé auprès des organismes et établissements habilités mentionnés à l'article L. 1271-10.</p>""",
    "Réécriture à droit constant : les deux possibilités d'utilisation du chèque sont exprimées par les opérations d'encaissement et de remboursement, avec maintien des 1° et 2°. Aucun circuit nouveau n'est institué.",
    "Le corpus public fourni ne contient pas d'article L. 1271-9 : le renvoi du 1° est conservé mais son état doit être contrôlé, comme pour L. 1271-10. Les établissements, institutions et services du 1° restent distincts des organismes et établissements habilités du 2°.",
)

add(
    "L1271-15-1",
    """<p>Pour le remboursement des chèques emploi-service universels, les émetteurs perçoivent une rémunération versée par les personnes morales ou les entrepreneurs individuels rémunérés au moyen de ces titres. Les conditions de cette rémunération sont fixées par décret.</p>
<p>Par dérogation au premier alinéa, aucune rémunération n'est perçue par les émetteurs pour les prestations mentionnées aux 4°, 5° et 6° du B de l'article L. 1271-1.</p>""",
    "Réécriture à droit constant : l'objet de la rémunération, les personnes qui la versent et le renvoi au décret sont séparés ; l'exemption est formulée explicitement dans son alinéa propre. Aucune réforme de fond ne modifie les frais de remboursement.",
    "Les 4°, 5° et 6° du B de L. 1271-1 ont été retrouvés dans le corpus public. L'exemption reste limitée à ces prestations ; elle n'est pas étendue aux autres services à la personne. Aucun tarif n'est ajouté et le renvoi au premier alinéa demeure exact.",
)

add(
    "L1271-16",
    """<p>Les informations concernant les personnes mentionnées aux 1° et 3° du A de l'article L. 1271-1, rémunérées au moyen de chèques emploi-service universels préfinancés dans les conditions de l'article L. 1271-12, sont transmises à l'organisme ou à l'établissement chargé de rembourser ces titres. Cette transmission a pour seule finalité le contrôle du bon usage des titres.</p>
<p>Les modalités de transmission doivent garantir la confidentialité des données. Les personnes concernées sont informées de l'existence de ce dispositif de contrôle.</p>""",
    "Réécriture à droit constant : la transmission et sa finalité exclusive sont énoncées séparément ; l'exigence de confidentialité est formulée comme une obligation. Aucun élargissement de l'utilisation des données n'est proposé.",
    "Les catégories des 1° et 3° du A de L. 1271-1 ont été vérifiées dans le corpus public. Les deux alinéas, le préfinancement selon L. 1271-12, le destinataire chargé du remboursement, la finalité exclusive, la confidentialité et l'information des personnes sont maintenus. Aucun émetteur de la transmission n'est inventé.",
)

add(
    "L1271-17",
    """<p>Des décrets fixent les modalités d'utilisation et de fonctionnement du chèque emploi-service universel. Ils précisent notamment :</p>
<p>1° Les modalités d'encaissement et de remboursement des chèques emploi-service universels, ainsi que celles relatives aux obligations de contrôle, de vérification et de vigilance des organismes et établissements qui émettent ces chèques sous forme de titres spéciaux de paiement ;</p>
<p>2° Les modalités applicables aux chèques emploi-service universels préfinancés pour rémunérer les personnes ou payer les services mentionnés à l'article L. 421-1 du code de l'action sociale et des familles et au premier alinéa de l'article L. 2324-1 du code de la santé publique ;</p>
<p>3° Les modalités applicables aux chèques emploi-service universels préfinancés pour rémunérer les personnes mentionnées au 2° de l'article L. 722-20 du code rural et de la pêche maritime, employées par des particuliers pour la mise en état et l'entretien de jardins ;</p>
<p>4° Les modalités d'échange d'informations entre l'organisme de recouvrement habilité et les organismes ou établissements mentionnés à l'article L. 1271-10 ;</p>
<p>5° Les modalités de fonctionnement du compte prévu à l'article L. 1271-11.</p>""",
    "Réécriture à droit constant : l'habilitation réglementaire est suivie d'une liste homogène de modalités, avec des verbes directs pour la rémunération et le paiement. Les cinq subdivisions et toutes les catégories de contrôle sont conservées ; aucune réforme de fond n'est ajoutée.",
    "Les 1° à 5° restent à leur place. Le premier alinéa de L. 2324-1 du code de la santé publique et le 2° de L. 722-20 du code rural et de la pêche maritime restent les cibles précises des renvois. La portée des renvois aux codes de l'action sociale et des familles, de la santé publique et rural, absents du corpus fourni, n'a pas pu être vérifiée localement ; ils sont conservés. Le 3° demeure limité aux particuliers employeurs pour la mise en état et l'entretien de jardins. Le compte du 5° reste celui de L. 1271-11.",
)

add(
    "L1272-4",
    """<p>Pour les associations et les fondations qui l'utilisent, le chèque-emploi associatif vaut accomplissement de l'ensemble des formalités liées à l'embauche et à l'emploi de leurs salariés. Sont notamment concernées les formalités suivantes :</p>
<p>1° La déclaration préalable à l'embauche prévue à l'article L. 1221-10 ;</p>
<p>2° L'inscription au registre unique du personnel prévue à l'article L. 1221-13 ;</p>
<p>3° Pour les contrats de travail à durée déterminée, l'établissement d'un contrat écrit, l'inscription des mentions obligatoires et la transmission du contrat au salarié, prévus aux articles L. 1242-12 et L. 1242-13 ;</p>
<p>4° Pour les contrats de travail à temps partiel, l'établissement d'un contrat écrit et l'inscription des mentions obligatoires prévus à l'article L. 3123-6 ;</p>
<p>5° Les déclarations au titre de la médecine du travail et du régime des prestations du revenu de remplacement mentionnées à l'article L. 5421-2.</p>""",
    "Réécriture à droit constant : l'effet du recours au chèque-emploi associatif est énoncé directement ; les catégories de contrats sont placées au début des 3° et 4° pour identifier immédiatement les formalités concernées. La réforme du temps partiel n'est pas étendue à un régime distinct par cet article.",
    "Les cinq subdivisions et le caractère non exhaustif de la liste sont conservés. Coordination avec la réécriture de L. 3123-6 retenue dans coordination.json : les éléments recueillis pour le contrat à temps partiel doivent permettre d'inscrire le volume contractuel garanti. Le renvoi dynamique à cet article est maintenu ; la fiction d'accomplissement des formalités ne dispense pas des règles de fond du contrat. La suppression du plancher général de vingt-quatre heures ne supprime aucun minimum spécial ou conventionnel par ce texte.",
)

add(
    "L1273-3",
    """<p>L'entreprise qui recourt au service « Titre Emploi-Service Entreprise » bénéficie notamment des services suivants :</p>
<p>1° Le calcul des rémunérations dues aux salariés en application du présent code et des conventions collectives, ainsi que le calcul de l'ensemble des cotisations et contributions instituées par la loi et des cotisations et contributions conventionnelles rendues obligatoires par celle-ci ;</p>
<p>2° La souscription, dans les conditions prévues à l'article L. 133-5 du code de la sécurité sociale, des déclarations obligatoires relatives aux cotisations et contributions sociales à adresser aux organismes qui gèrent les régimes mentionnés dans ce code, à l'institution mentionnée à l'article L. 5312-1 du présent code et, le cas échéant, aux caisses de congés payés mentionnées à l'article L. 3141-32 du présent code.</p>
<p>Les organismes auxquels sont reversées des cotisations et contributions sociales en application du 1° de l'article L. 133-5-7 du code de la sécurité sociale ne peuvent demander à une entreprise des données ou informations qu'elle a déjà produites au titre des informations mentionnées au premier alinéa de l'article L. 133-5-8 du même code. Toute demande de cette nature est nulle de plein droit.</p>""",
    "Réécriture à droit constant : les services de calcul et de déclaration sont présentés comme deux prestations distinctes. L'interdiction des demandes de données déjà produites précède l'énoncé de leur nullité de plein droit. Cette règle existante de non-redemande est préservée ; aucun guichet unique général nouveau n'est réputé créé.",
    "Les renvois à L. 133-5, au 1° de L. 133-5-7 et au premier alinéa de L. 133-5-8 du code de la sécurité sociale ont été vérifiés dans le corpus public. La nullité reste limitée aux organismes et aux informations désignés, et les caisses de congés payés restent visées seulement le cas échéant. Le guichet unique général d'embauche annoncé par policy.json appelle une disposition nouvelle d'organisation au chapitre Ier du titre II du livre II de la première partie du code du travail, coordonnée avec L. 1221-10, L. 1272-4, L. 1273-3 et L. 1273-5 ainsi qu'avec les dispositifs des articles L. 133-5-6 à L. 133-5-8 du code de la sécurité sociale ; le présent service spécialisé ne réalise pas seul cette généralisation. Aucun numéro d'article nouveau n'est présumé existant.",
)

add(
    "L1273-5",
    """<p>L'employeur qui utilise le « Titre Emploi-Service Entreprise » est réputé avoir accompli les formalités suivantes lorsqu'il remet au salarié et envoie à l'organisme habilité les éléments du titre emploi respectivement destinés à chacun :</p>
<p>1° Le respect des règles d'établissement du contrat de travail, dans les conditions prévues à l'article L. 1221-1 ;</p>
<p>2° La déclaration préalable à l'embauche prévue à l'article L. 1221-10 ;</p>
<p>3° La délivrance du certificat de travail prévue à l'article L. 1234-19 ;</p>
<p>4° Pour les contrats de travail à durée déterminée, l'établissement d'un contrat écrit, l'inscription des mentions obligatoires et la transmission du contrat au salarié, prévus aux articles L. 1242-12 et L. 1242-13 ;</p>
<p>5° Pour les contrats de travail à temps partiel, l'établissement d'un contrat écrit et l'inscription des mentions obligatoires prévus à l'article L. 3123-6.</p>""",
    "Réécriture à droit constant : les deux transmissions conditionnant l'accomplissement réputé des formalités sont explicitées. Les 4° et 5° commencent par la catégorie de contrats concernée. Aucune dispense des règles de fond du contrat ni réforme autonome du temps partiel n'est ajoutée.",
    "Les cinq subdivisions et tous les renvois sont maintenus. Le salarié et l'organisme habilité doivent chacun recevoir les éléments qui leur sont destinés. Coordination avec L. 3123-6 réécrit : le titre doit permettre de recueillir les mentions du volume contractuel garanti, sans supprimer les minima conventionnels ou spéciaux. L'article n'instaure pas à lui seul le guichet unique général annoncé par policy.json ; voir le besoin de disposition nouvelle identifié pour L. 1273-3.",
)

add(
    "L1273-6",
    """<p>L'employeur qui utilise le « Titre Emploi-Service Entreprise » peut mandater un tiers pour accomplir les formalités liées à ce service.</p>""",
    "Réécriture à droit constant : le recours au mandat est formulé par un verbe direct et les formalités sont rattachées explicitement au service utilisé. Aucune réforme de fond ni nouvelle catégorie de mandataires n'est introduite.",
    "Le mandat demeure facultatif et porte sur les formalités correspondant au Titre Emploi-Service Entreprise. Aucun transfert de responsabilité ni pouvoir supplémentaire du tiers n'est ajouté.",
)

add(
    "L1311-1",
    """<p>Les établissements des employeurs de droit privé sont soumis aux dispositions du présent livre.</p>
<p>Les établissements publics à caractère industriel et commercial sont également soumis à ces dispositions.</p>""",
    "Réécriture à droit constant : les établissements concernés deviennent les sujets des deux phrases définissant le champ d'application. Les réformes de l'embauche n'entraînent aucune extension ou restriction du champ de ce livre.",
    "Les deux alinéas sont conservés. Le premier vise les établissements des employeurs de droit privé ; le second vise les établissements publics à caractère industriel et commercial, sans extension aux autres établissements publics.",
)

add(
    "L1311-2",
    """<p>Les entreprises ou établissements qui emploient au moins cinquante salariés doivent établir un règlement intérieur.<br/><br/>Cette obligation s'applique à l'expiration d'un délai de douze mois à compter de la date à laquelle le seuil de cinquante salariés a été atteint, conformément à l'article L. 2312-2.</p>
<p>Des règles particulières peuvent être prévues pour une catégorie de personnel ou pour une division de l'entreprise ou de l'établissement.</p>""",
    "Réécriture à droit constant : l'entreprise ou l'établissement est expressément tenu d'établir le règlement ; le délai et la faculté de prévoir des règles particulières sont formulés directement. Aucune réforme de seuil n'est introduite sur le fondement de l'orientation générale de simplification.",
    "Le seuil d'au moins cinquante salariés, le délai de douze mois et le renvoi à L. 2312-2 sont conservés. Ce dernier article, vérifié dans le corpus public, comporte ses propres conditions de franchissement du seuil et délais : ils ne sont ni remplacés ni cumulés par une règle nouvelle ici. Les séparations internes du premier bloc source sont maintenues. La note source se rapporte à l'entrée en vigueur au 1er janvier 2020 prévue au XIV de l'article 11 de la loi n° 2019-486 du 22 mai 2019 ; cette date historique n'est pas une date d'entrée en vigueur de la réforme proposée.",
)

add(
    "L1321-1",
    """<p>Le règlement intérieur est un document écrit dans lequel l'employeur fixe uniquement les éléments suivants :</p>
<p>1° Les mesures d'application des règles de santé et de sécurité dans l'entreprise ou l'établissement, notamment les instructions prévues à l'article L. 4122-1 ;</p>
<p>2° Les conditions dans lesquelles les salariés peuvent être appelés, à la demande de l'employeur, à participer au rétablissement de conditions de travail protectrices de la santé et de la sécurité des salariés lorsque ces conditions paraissent compromises ;</p>
<p>3° Les règles générales et permanentes de discipline, notamment la nature et l'échelle des sanctions que l'employeur peut prononcer.</p>""",
    "Réécriture à droit constant : le contenu exclusif du règlement est annoncé clairement ; au 2°, la demande de l'employeur et la condition tenant à la santé et à la sécurité sont rapprochées des actions qu'elles encadrent. Aucune réforme de fond ne réduit le socle de santé ou les garanties disciplinaires.",
    "Les 1°, 2° et 3°, le renvoi à L. 4122-1, la portée exclusive de l'énumération et le caractère général et permanent des règles disciplinaires sont conservés. Le 2° reste applicable lorsque les conditions paraissent compromises, sans exiger une atteinte déjà réalisée ni ouvrir une faculté générale étrangère à la santé et à la sécurité.",
)

add(
    "L1321-2",
    """<p>Le règlement intérieur doit rappeler les éléments suivants :</p>
<p>1° Les règles relatives aux droits de la défense des salariés, définies aux articles L. 1332-1 à L. 1332-3 ou par la convention collective applicable ;</p>
<p>2° Les règles du présent code relatives au harcèlement moral, au harcèlement sexuel et aux agissements sexistes ;</p>
<p>3° L'existence du dispositif de protection des lanceurs d'alerte prévu au chapitre II de la loi n° 2016-1691 du 9 décembre 2016 relative à la transparence, à la lutte contre la corruption et à la modernisation de la vie économique.</p>""",
    "Réécriture à droit constant : l'obligation de rappel est exprimée directement et les deux formes de harcèlement sont nommées séparément. La mention légale des lanceurs d'alerte et la structure en trois points sont préservées ; aucune réforme de fond n'est proposée.",
    "Les droits de la défense issus des articles L. 1332-1 à L. 1332-3 ou de la convention collective restent visés. Le 3° impose de rappeler l'existence du dispositif, sans exiger ici la reproduction de toute la loi. La note source rattache l'entrée en vigueur au premier jour du sixième mois suivant la promulgation de la loi n° 2022-401 du 21 mars 2022 (article 18) ; il s'agit d'une règle historique, cohérente avec la date de validité source du 1er septembre 2022, et non de la transition d'une réforme future.",
)

add(
    "L1321-2-1",
    """<p>Le règlement intérieur peut inscrire le principe de neutralité et prévoir des restrictions à la manifestation des convictions des salariés. Ces restrictions doivent être justifiées par l'exercice d'autres libertés et droits fondamentaux ou par les nécessités du bon fonctionnement de l'entreprise. Elles doivent également être proportionnées au but recherché.</p>""",
    "Réécriture à droit constant : la faculté d'inscrire la neutralité, les justifications alternatives des restrictions et l'exigence cumulative de proportionnalité sont réparties en trois phrases. Aucune réforme de fond n'élargit les restrictions aux convictions des salariés.",
    "Un seul alinéa est conservé. L'exercice d'autres libertés et droits fondamentaux et les nécessités du bon fonctionnement de l'entreprise restent deux justifications alternatives ; la proportionnalité est requise dans tous les cas. L'attribut de présentation align de la source est supprimé conformément aux balises et attributs autorisés.",
)

add(
    "L1321-3",
    """<p>Les dispositions suivantes sont interdites dans le règlement intérieur :</p>
<p>1° Les dispositions contraires aux lois et règlements ou aux stipulations des conventions et accords collectifs de travail applicables dans l'entreprise ou l'établissement ;</p>
<p>2° Les restrictions aux droits des personnes et aux libertés individuelles et collectives qui ne seraient ni justifiées par la nature de la tâche à accomplir ni proportionnées au but recherché ;</p>
<p>3° Les dispositions qui discriminent les salariés dans leur emploi ou leur travail, à capacité professionnelle égale, en raison de leur origine, de leur sexe, de leurs mœurs, de leur orientation sexuelle ou de leur identité de genre, de leur âge, de leur situation de famille ou de leur grossesse, de leurs caractéristiques génétiques, de leur appartenance ou de leur non-appartenance, vraie ou supposée, à une ethnie, une nation ou une race, de leurs opinions politiques, de leurs activités syndicales ou mutualistes, de leurs convictions religieuses, de leur apparence physique, de leur nom de famille, de leur état de santé ou de leur handicap.</p>""",
    "Réécriture à droit constant : les interdictions sont annoncées directement ; le 3° emploie un verbe conjugué et clarifie les rattachements grammaticaux des motifs de discrimination. La liste des motifs et les conditions des restrictions sont intégralement maintenues, sans réforme de fond.",
    "Les trois subdivisions, la capacité professionnelle égale et tous les motifs énumérés par la source sont conservés, y compris les mœurs, l'identité de genre, les activités mutualistes et l'appartenance ou la non-appartenance vraie ou supposée. La construction négative associant justification par la tâche et proportionnalité au 2° est maintenue, sans réinterprétation silencieuse. Au 1°, le lien « ou » explicite qu'une contrariété à l'une des normes énumérées suffit à l'interdiction ; les mêmes catégories de normes sont conservées.",
)

add(
    "L1321-4",
    """<p>L'employeur doit soumettre le règlement intérieur à l'avis du comité social et économique avant de l'introduire.</p>
<p>Le règlement intérieur précise sa date d'entrée en vigueur. Il ne peut entrer en vigueur avant l'expiration d'un délai d'un mois à compter de l'accomplissement des formalités de publicité.</p>
<p>L'employeur communique à l'inspecteur du travail le règlement intérieur accompagné de l'avis du comité social et économique, en même temps qu'il accomplit les mesures de publicité.</p>
<p>Ces obligations s'appliquent également lorsqu'une clause du règlement intérieur est modifiée ou retirée.</p>""",
    "Réécriture à droit constant : l'employeur est désigné comme responsable de la consultation et de la communication ; le délai précédant l'entrée en vigueur est formulé comme un délai à respecter. La modification et le retrait des clauses restent soumis aux mêmes obligations. Aucune réforme de fond n'est ajoutée.",
    "La version source applicable depuis le 28 mai 2026 est retenue, sans réintroduire une formalité de dépôt absente de cette source. Les quatre alinéas, la consultation pour avis (et non une autorisation du comité), le délai d'un mois, la publicité et la communication simultanée à l'inspecteur avec l'avis du comité sont conservés. Cette date de validité source ne fixe aucune entrée en vigueur de la réforme future.",
)

add(
    "L1321-5",
    """<p>Lorsqu'un règlement intérieur existe, les notes de service et les autres documents qui comportent des obligations générales et permanentes dans les matières mentionnées aux articles L. 1321-1 et L. 1321-2 constituent des adjonctions à ce règlement. Ces documents sont soumis aux dispositions du présent titre, qu'un règlement intérieur existe ou non.</p>
<p>Toutefois, si l'urgence le justifie, les obligations relatives à la santé et à la sécurité peuvent être appliquées immédiatement. Les prescriptions correspondantes sont alors communiquées immédiatement et simultanément au secrétaire du comité social et économique et à l'inspection du travail.</p>""",
    "Réécriture à droit constant : la règle applicable aux documents est explicitée selon qu'il existe ou non un règlement intérieur ; la dérogation d'urgence et la communication qui l'accompagne sont formulées séparément. Aucun changement de fond n'est apporté au contrôle ou à la santé et à la sécurité.",
    "Les deux alinéas sont conservés. Le caractère à la fois général et permanent des obligations, les renvois à L. 1321-1 et L. 1321-2 et l'application du présent titre en toute hypothèse restent inchangés. L'application immédiate demeure limitée à la santé et à la sécurité lorsque l'urgence la justifie. La communication doit rester à la fois immédiate et simultanée aux deux destinataires, dont le secrétaire du comité et non le seul comité en général.",
)

add(
    "L1321-6",
    """<p>L'employeur rédige le règlement intérieur en français. Il peut y joindre des traductions en une ou plusieurs langues étrangères.</p>
<p>Tout document qui impose des obligations au salarié ou contient des dispositions dont la connaissance est nécessaire à l'exécution de son travail est soumis aux mêmes règles de rédaction et de traduction.</p>
<p>Les documents reçus de l'étranger ou destinés à des étrangers ne sont pas soumis à ces règles.</p>""",
    "Réécriture à droit constant : l'obligation de rédaction est attribuée à l'employeur ; son extension aux documents de travail et les deux exceptions sont formulées directement. La traduction demeure facultative et aucune réforme de fond n'est appliquée.",
    "Les trois alinéas sont conservés. Le deuxième vise alternativement les obligations imposées au salarié et les dispositions nécessaires à l'exécution de son travail. Les documents reçus de l'étranger et ceux destinés à des étrangers restent deux exceptions alternatives ; aucune condition linguistique ou territoriale supplémentaire n'est créée.",
)

add(
    "L1322-1",
    """<p>Lorsqu'une disposition est contraire aux articles L. 1321-1 à L. 1321-3 ou à l'article L. 1321-6, l'inspecteur du travail peut, à tout moment, en exiger le retrait ou la modification.</p>""",
    "Réécriture à droit constant : la contrariété à une disposition de référence est placée avant le pouvoir de l'inspecteur, afin de rendre explicite le motif de son intervention. Le retrait et la modification demeurent les deux mesures possibles ; aucune réforme de fond n'est ajoutée.",
    "Le pouvoir d'intervention à tout moment, son caractère facultatif et les renvois à L. 1321-1 jusqu'à L. 1321-3 ainsi qu'à L. 1321-6 sont conservés. La plage de renvoi comprend L. 1321-2-1 ; aucun nouvel article contrôlé ni délai de recours n'est ajouté.",
)


sources = json.loads(Path("source.json").read_text())
assert len(sources) == 24
assert set(drafts) == {source["number"] for source in sources}
answer = []
for source in sources:
    item = {key: source[key] for key in ("code_id", "source_id", "source_sha256", "number")}
    item.update(drafts[source["number"]])
    item["status"] = "rewrite_draft"
    answer.append(item)
Path("answer.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")
print(f"answer.json : {len(answer)} articles")
