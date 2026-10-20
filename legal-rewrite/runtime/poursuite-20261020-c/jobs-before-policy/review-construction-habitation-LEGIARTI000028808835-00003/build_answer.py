import json
import re
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
answers = []


def paragraphs(*items):
    return '\n'.join(f'<p>{item}</p>' for item in items)


def add(index, proposed_xml, reason, review_notes, removed=None):
    source = sources[index]
    result = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    result.update(
        proposed_xml=proposed_xml,
        reason=reason,
        review_notes=review_notes,
        status='rewrite_draft',
    )
    if removed:
        result.update(
            change_type='normative_reduction',
            reform_policy_id='editorial_direction_2026_10_19',
            removed_provisions=removed,
        )
    answers.append(result)


add(
    0,
    sources[0]['previous_draft']['proposed_xml'],
    "Seconde passe : maintien de la proposition antérieure, qui réécrit réellement la longue phrase de qualification et distingue les trois activités. Aucune coupe supplémentaire n'est justifiée dans cet article : il ne crée ni agrément, ni déclaration, ni prélèvement, mais définit le champ des services sociaux de logement et de leur financement. Le reste à charge strictement inférieur à 50 % protège les personnes en difficulté ; les financeurs et les trois voies de financement ouvrent le dispositif, et les références européennes encadrent les compensations publiques. Retirer ces éléments risquerait de fermer un régime favorable ou de méconnaître le cadre des aides d'État. Les charges administratives distinctes sont réduites dans L. 365-2 à L. 365-4. La réécriture de cet article demeure à droit constant.",
    "Source et proposition relues en entier : cinq alinéas de fond, trois activités, trois types de bail au 1°, locataires et propriétaires occupants, II de L. 301-1, financement par décision, convention de subvention ou marché et seuil strictement inférieur à 50 % conservés. Le j du 2 de l'article 2 de la directive 2006/123/CE du 12 décembre 2006, la décision 2012/21/UE du 20 décembre 2011 et l'article 106, paragraphe 2, du traité restent à leur place. Le texte initial de SRU 141 portait sur l'utilité sociale et des agréments ; il ne correspond pas à toute la rédaction actuelle, applicable depuis le 27 mars 2014 selon les métadonnées. Sa présence ne justifie donc pas la disparition de cette qualification actuelle ni des avantages qui s'y rattachent. Les conventions facultatives des fédérations ont aujourd'hui un fondement distinct à L. 365-7, consulté. La durée indéterminée d'un agrément proposée aux articles suivants ne vaut pas prolongation indéfinie d'un mandat ou d'une compensation de service public. Ni conformité européenne nouvelle ni examen achevé des 209 articles SRU ne sont affirmés.",
)

add(
    1,
    paragraphs(
        "L'autorité administrative agrée les organismes qui exercent les activités de maîtrise d'ouvrage mentionnées au 1° de l'article L. 365-1, selon les modalités définies par décret en Conseil d'État. L'agrément est accordé au regard des capacités financières de l'organisme, de sa compétence dans le domaine du logement et du caractère désintéressé de la gestion de ses dirigeants.",
        "La délivrance ou la modification de cet agrément ne requiert aucun avis du comité régional de l'habitat et de l'hébergement. L'organisme n'a pas à saisir ce comité ni à produire son avis.",
        "Pour les demandes prévues au présent article et aux articles L. 365-3 et L. 365-4, les pièces et renseignements communs sont fournis une seule fois. L'autorité saisie les transmet aux autres autorités compétentes dans le respect des règles de protection et d'accès aux données. Les pièces et renseignements exacts et à jour que l'administration détient déjà légalement ou auxquels elle a légalement accès ne peuvent être exigés à nouveau.",
        "Les deuxième et troisième alinéas s'appliquent aux demandes nouvelles et à celles en cours à la date d'entrée en vigueur de la loi. Les demandes en cours sont instruites sans nouveau dépôt et sans reprise des délais déjà courus. Les agréments délivrés, les aides accordées et les conventions valablement conclues avant cette date conservent leurs effets.",
    ),
    "Réforme de fond supplémentaire : suppression de la consultation régionale préalable à l'agrément de maîtrise d'ouvrage, de la saisine du comité et de la copie de son avis à la charge du demandeur ; suppression des dépôts multiples de pièces communes aux trois agréments et des justificatifs exacts et à jour déjà légalement disponibles. Ce circuit consultatif double l'examen des capacités par l'autorité qui décide et n'apporte pas de protection essentielle distincte démontrée. L'agrément lui-même et ses trois critères sont conservés : ils identifient les opérateurs pouvant détenir durablement un patrimoine locatif social, bénéficier des concours de la CGLLS et de régimes fiscaux particuliers, sous contrôle de l'ANCOLS. La simple suppression de cette qualification risquerait de fermer ces droits ou de désarticuler ce contrôle. Le premier alinéa reprend la réécriture antérieure à droit constant ; les alinéas suivants retirent effectivement des démarches, sans déclaration de remplacement.",
    "Coordinations précises à effectuer, non présentées comme déjà rédigées : R. 362-2, 8°, R. 365-2, première phrase, et R. 365-5, 10° c, doivent perdre la consultation régionale, sa saisine et la copie d'avis. R. 365-5 et les circuits de R. 365-6 et R. 365-6-1 doivent permettre les pièces communes déposées une seule fois, sans nouvel exemplaire ni attestation équivalente. R. 365-2 prévoit déjà une durée illimitée : aucune nouvelle période de cinq ans n'est introduite. Les critères financiers, de compétence et de gestion désintéressée, les conditions de fond des aides et le contrôle de L. 342-2 et L. 342-14, lus, subsistent ; aucune cotisation distincte n'est abolie par ce texte. L. 365-5 et L. 452-1, lus intégralement, gardent leurs concours et la protection locative par L. 411-4. Les références fiscales à l'agrément, notamment CGI 207, 1, 4° quater et 1051, lus, continuent de s'appliquer aux futurs organismes éligibles, sous leurs conditions propres. La consultation de R. 362-2, 8°, est distincte des consultations autonomes et de la suppression du dernier alinéa de cet article déjà retenue dans coordination.json. SRU 141 ne décrit pas le régime actuel issu de textes postérieurs ; pas d'abrogation par seule filiation. Les dates historiques du 1er janvier 2010 et du 1er janvier 2011 dans les notes de L. 365-3 et L. 365-4, ainsi que celles du 1er janvier 2014 et du 1er janvier 2015 à L. 371-4 pour Mayotte, ne sont ni réinitialisées ni utilisées comme date de la réforme.",
    [
        "La consultation obligatoire du comité régional de l'habitat et de l'hébergement pour la délivrance ou la modification de l'agrément de maîtrise d'ouvrage.",
        "La saisine du comité régional par l'organisme demandeur et la production de la copie de son avis dans le dossier d'agrément.",
        "La remise répétée des pièces et renseignements communs aux demandes relevant de L. 365-2, L. 365-3 et L. 365-4, ainsi que des justificatifs exacts et à jour déjà légalement disponibles.",
    ],
)

for index, activity, subdivision in (
    (2, "d'ingénierie sociale, financière et technique", '2°'),
    (3, "d'intermédiation locative et de gestion locative sociale", '3°'),
):
    number = sources[index]['number']
    is_engineering = index == 2
    specific_reason = (
        "L'agrément initial permet de vérifier les capacités d'opérateurs qui accompagnent des personnes défavorisées, notamment dans leurs démarches DALO et leurs recours ; les dispenses et agréments de plein droit déjà prévus restent ouverts."
        if is_engineering else
        "L'agrément initial permet de vérifier les capacités d'opérateurs qui prennent des logements à bail, les sous-louent ou gèrent des logements et des fonds pour des personnes défavorisées ; l'assimilation des maîtres d'ouvrage pour la gestion de leur propre parc et les autres dispenses existantes demeurent."
    )
    specific_notes = (
        "R. 365-1, 2° b et c, conserve les assimilations des organismes sociaux et les agréments de plein droit ; aucune nouvelle demande n'est exigée de leurs bénéficiaires. Les renvois relatifs à l'accompagnement et au DALO ne deviennent pas un agrément supplémentaire."
        if is_engineering else
        "R. 365-1, dernier alinéa, conserve l'assimilation des organismes de maîtrise d'ouvrage pour leur propre parc. La carte professionnelle de gérance visée au dernier alinéa de R. 365-5, sur le fondement de la loi n° 70-9 du 2 janvier 1970 hors des cinq codes, reste distincte et n'est pas réputée supprimée. Les obligations de sécurité des détecteurs de fumée de R. 142-3 et R. 142-5, lus, restent à leur champ. Les avantages fiscaux et locatifs conditionnés à cet agrément restent accessibles aux opérations futures remplissant leurs autres conditions ; ils ne sont pas réservés aux anciens bénéficiaires."
    )
    add(
        index,
        paragraphs(
            f"L'autorité administrative agrée les organismes qui exercent les activités {activity} mentionnées au {subdivision} de l'article L. 365-1, selon les modalités définies par décret en Conseil d'État. L'agrément est délivré pour une durée indéterminée.",
            "L'agrément vaut sur l'ensemble du territoire national pour les activités qu'il couvre. L'extension territoriale de ces activités n'est soumise ni à une nouvelle demande d'agrément ni à une autorisation ou à une déclaration d'extension. Aucun renouvellement ni aucune confirmation ou déclaration périodique tenant lieu de renouvellement ne sont exigés. Les dispenses et les agréments de plein droit demeurent applicables dans leur champ propre. Les contrôles et les possibilités de retrait de l'agrément restent applicables. Les actes confiant une mission de service public ou accordant son financement conservent leurs propres champs, durées et conditions.",
            "Ces dispositions s'appliquent aux agréments délivrés à compter de la date d'entrée en vigueur de la loi. Les agréments en cours de validité à cette date deviennent de plein droit des agréments à durée indéterminée, valables sur l'ensemble du territoire national pour les activités qu'ils couvrent, sans demande ni formalité. Les demandes initiales en cours sont poursuivies sans nouveau dépôt ni reprise des délais déjà courus ; les demandes de renouvellement ou d'extension territoriale d'un agrément encore valide deviennent sans objet. Les agréments devenus caducs ou retirés avant cette date ne sont pas rétablis. Les aides, conventions et droits des bénéficiaires valablement constitués avant cette date sont préservés.",
        ),
        "Réforme de fond par rapport à la proposition antérieure à droit constant : suppression de la durée de cinq ans et du renouvellement périodique, ainsi que de la nouvelle demande et des consultations attachées à une simple extension territoriale des mêmes activités. Le renouvellement sur échéance et la répétition de l'agrément dans d'autres départements ou régions sont retirés au profit d'une qualification initiale durable et nationale, sans déclaration équivalente. Les contrôles pendant l'activité et le retrait contradictoire permettent de traiter les manquements sans recommencer systématiquement la procédure. " + specific_reason + " La compétence des autorités, les activités agréées et les conditions de fond non incompatibles restent fixées par les dispositions d'application ; la simplification n'accorde pas à elle seule un financement public national illimité.",
        f"{number} : le renvoi au {subdivision} de L. 365-1 et toutes les activités sont conservés. Coordination requise de R. 365-3 et R. 365-4 pour retirer les cinq ans renouvelables, de R. 365-5 pour retirer les dossiers de renouvellement, et de R. 365-6 pour supprimer les demandes d'extension et les consultations départementales correspondantes. Les demandes initiales gardent leur autorité compétente et le délai réglementaire de trois mois ; aucun dossier commun à L. 365-2 à L. 365-4 ni justificatif déjà disponible ne doit être redéposé, conformément à L. 365-2 proposé. R. 365-7 conserve ses contrôles et ses obligations autonomes de suivi : ils ne peuvent devenir une demande annuelle de maintien de l'agrément. R. 365-8, lu, conserve les motifs de retrait et la présentation préalable des observations. La suppression du terme de cinq ans vaut aussi pour les agréments valides à l'entrée en vigueur, sans rétablissement des agréments anciens caducs. Les notes de la loi n° 2009-323 du 25 mars 2009, article 2, IV, ont été lues : demandes à compter du 1er janvier 2010 et caducité au 1er janvier 2011 restent des transitions historiques ; L. 371-4, 9°, conserve son champ historique de Mayotte, 1er janvier 2014 et 1er janvier 2015. " + specific_notes + " R. 300-2-2, lu, garde l'accès aux concours du Fonds national d'accompagnement et ses conventions de financement. La décision 2012/21/UE maintenue à L. 365-1 impose sa coordination propre : agrément indéfini et territorialité nationale de la qualification ne prolongent ni n'élargissent automatiquement un mandat ou sa compensation. L'historique joint de SRU 141 ne prouve pas l'origine SRU de toute la norme actuelle, dont la source situe la rédaction en 2009. Ces seuls textes ne soldent pas le volet SRU 141 dans tous ses descendants.",
        [
            "La limitation de l'agrément à une période de cinq ans renouvelable et les demandes périodiques de renouvellement avec leurs dossiers.",
            "Les nouvelles demandes d'agrément, consultations et décisions nécessaires à la seule extension territoriale des activités déjà agréées.",
            "Toute confirmation ou déclaration périodique de substitution qui rétablirait le renouvellement supprimé ou l'autorisation d'extension territoriale.",
        ],
    )

add(
    4,
    paragraphs(
        "Un ou plusieurs départements, une métropole et l'État peuvent prendre conjointement l'initiative de créer une association d'information sur le logement. Cette association réunit les collectivités territoriales, les établissements publics de coopération intercommunale compétents et tout organisme concerné par le logement. Elle est départementale, interdépartementale, métropolitaine ou départementale-métropolitaine.",
        "L'association informe gratuitement les usagers sur leurs droits et obligations et sur les solutions de logement adaptées à leur situation. Cette information porte notamment sur les conditions d'accès au parc locatif et sur les aspects juridiques et financiers de leur projet d'accession à la propriété. Elle exclut tout acte administratif, contentieux ou commercial.",
        "Les associations mentionnées au premier alinéa exercent leur mission sans agrément ni avis préalable d'une association nationale. Elles sont assimilées de plein droit, sans demande ni formalité, aux associations agréées mentionnées dans les dispositions législatives et réglementaires prises pour l'application du présent article ou qui s'y réfèrent. L'association nationale est composée, d'une part, de représentants des associations mentionnées au premier alinéa et, d'autre part, des instances nationales auxquelles les organismes membres de ces associations sont affiliés.",
        "Un décret fixe les statuts types et les conditions de contrôle de l'association nationale et des associations mentionnées au premier alinéa. Il fixe également les conditions d'agrément de l'association nationale.",
        "L'association compétente pour le département du Rhône en application du premier alinéa l'est également sur le territoire de la métropole de Lyon. Elle porte le nom d'« association départementale-métropolitaine d'information sur le logement ».",
        "En Corse, la collectivité de Corse et l'État peuvent prendre conjointement l'initiative de créer l'association mentionnée au premier alinéa.",
        "La suppression de l'agrément et de l'avis préalable des associations mentionnées au premier alinéa prend effet à la date d'entrée en vigueur de la loi et bénéficie également aux associations déjà constituées conformément au présent article. Les demandes d'agrément en cours deviennent sans objet. Les aides accordées, les conventions valablement conclues et les droits des usagers ne sont pas interrompus par cette suppression. Aucun nouvel agrément, aucune confirmation ni déclaration ne sont exigés à ce titre.",
    ),
    "Réforme de fond : suppression de l'agrément ministériel individuel des associations territoriales d'information sur le logement et de l'avis préalable de l'association nationale. L'initiative est déjà conjointe avec l'État et les collectivités ; le second circuit ministériel ne justifie pas une autorisation supplémentaire pour assurer une information gratuite, excluant les actes administratifs, commerciaux et contentieux. Aucune déclaration de remplacement n'est créée. L'assimilation légale préserve la qualité exigée par les textes pour les aides et les participations au réseau, y compris pour les futures associations recevables. Les statuts types, les contrôles, la composition de l'association nationale et son propre agrément sont maintenus afin de conserver la neutralité, la compétence et la surveillance du réseau d'information. Les missions et les variantes territoriales sont réécrites à droit constant.",
    "Les six alinéas initiaux conservent leur ordre ; seule la transition est ajoutée en septième position. L'initiative conjointe du premier alinéa n'est pas transformée en alternatives ; la dérogation corse et la compétence Rhône/Lyon sont maintenues. SRU 201 a créé le socle, mais ses termes départementaux ne décrivent pas les variantes territoriales actuelles : aucune suppression de celles-ci par filiation. Coordinations à effectuer : R. 366-5 pour détacher les clauses statutaires de l'agrément territorial tout en conservant ces clauses, R. 366-6 et R. 366-7 pour supprimer arrêté, demande, recommandé, dossier spécifique et transmission à l'ANIL aux fins d'avis, ainsi que le délai d'un mois lié à cet avis. L'annexe à R. 366-1, lue en entier avec celle de R. 366-5, doit perdre le circuit obligatoire de l'avis et de la commission d'agrément des ADIL ; le soutien du réseau reste possible sans formalité préalable imposée. L'annexe à R. 366-5 conserve ses protections de compétence juridique et financière, neutralité et gratuité et ses exclusions de mission. R. 366-1 à R. 366-4 continuent de régir l'agrément national ; le délai de quatre mois et le contradictoire de R. 366-4 ne sont pas supprimés. L'assimilation du troisième alinéa protège les futurs organismes territoriaux comme ceux déjà créés : elle couvre notamment l'accès aux aides de L. 452-1 et la qualité de membre du réseau, sans attribuer automatiquement une aide ni supprimer ses autres conditions. L. 441-2-8 et R. 411-4, lus, conservent participation à l'information des demandeurs et accès aux données dans leur champ légal. Ces articles et annexes extérieurs au lot n'ont pas été modifiés.",
    [
        "L'agrément ministériel préalable des associations territoriales d'information sur le logement, avec sa demande et son dossier spécifique.",
        "L'avis préalable obligatoire de l'association nationale, la transmission du dossier à cette fin et le circuit de consultation lié à l'agrément territorial.",
    ],
)

old_411_1 = re.findall(r'<p>(.*?)</p>', sources[5]['previous_draft']['proposed_xml'], flags=re.S)
old_411_1[1] = (
    "Des dépendances, des annexes et des jardins privatifs ou collectifs peuvent être adjoints à ces habitations, qu'ils soient accolés ou non aux immeubles. Aucune condition particulière d'adjonction ne peut être imposée par décision administrative sur le fondement du présent alinéa."
)
old_411_1.append(
    "La suppression des conditions administratives particulières d'adjonction prévue au deuxième alinéa s'applique à compter de la date d'entrée en vigueur de la loi, y compris aux opérations en cours, sans remise en cause des droits des tiers, des aides accordées et des engagements contractuels valablement souscrits avant cette date."
)
add(
    5,
    paragraphs(*old_411_1),
    "Réforme de fond supplémentaire : suppression de l'habilitation à imposer des conditions administratives spéciales pour adjoindre des dépendances, annexes et jardins aux logements sociaux, et de l'assujettissement à ces conditions. Ces aménagements restent soumis aux règles générales applicables au projet, sans filtre supplémentaire propre à cette adjonction. Les caractéristiques techniques et de prix de revient du logement social et sa destination aux personnes de ressources modestes sont maintenues : elles définissent le champ des aides et des règles protectrices, au lieu de constituer un agrément d'annexe. Les huit alinéas initiaux restent à leur place. Les facultés de location libre des stationnements issues de SRU 144, leur précarité et les droits des locataires sont conservés et réécrits à droit constant ; leur origine SRU ne justifie pas la disparition de ces facultés favorables.",
    "Le second alinéa de R. 411-1, lu, doit être retiré et les dispositions des arrêtés qu'il habilite doivent être recensées pour leur seule composante de conditions particulières d'adjonction ; leurs intitulés et dates ne figurent pas dans les pièces fournies, et leur traitement exhaustif n'est pas affirmé. Le premier alinéa de R. 411-1 relatif aux caractéristiques techniques et au prix de revient demeure autonome. La suppression ne dispense pas des règles de sécurité, d'accessibilité, de salubrité ou d'urbanisme ayant un fondement distinct ; aucun nouveau dossier n'est créé. Les locaux communs et constructions accessoires nécessaires à la vie économique et sociale restent au troisième alinéa : maintien du support des exonérations sur leurs produits de CGI 207, 1, 4° b et 4° quater b, lu en entier, pour les situations futures aussi. Les alinéas quatre à huit conservent la liberté de location, la révocabilité à tout moment, le droit d'usage de toute place libre, l'absence de préférence sur une place identifiée et la limite des droits dont dispose le bailleur. L. 442-6-4, lu, conserve le droit de renoncer au stationnement et la réduction correspondante de loyer et de charges. Le renvoi source à L. 151-47 du code de l'urbanisme est maintenu mais appelle un contrôle de concordance : le texte fourni de cet article traite du PLU tenant lieu de plan de mobilité et ne formule pas expressément ce régime de mutualisation ; L. 151-33 et R. 151-45 comportent des règles de stationnement mutualisé distinctes, sans permettre de substituer silencieusement l'un à l'autre. Cette difficulté préexistante n'est pas présentée comme résolue. SRU 144 n'avait ajouté que les deux alinéas sur la location des places vacantes ; les autres parties de l'article ne lui sont pas attribuées en bloc.",
    [
        "L'assujettissement de l'adjonction de dépendances, annexes et jardins à des conditions particulières fixées par décision administrative au titre du deuxième alinéa.",
        "L'habilitation à maintenir ou imposer, sur ce seul fondement, un régime administratif spécial d'adjonction de ces dépendances, annexes et jardins.",
    ],
)

old_411_3 = re.findall(r'<p>(.*?)</p>', sources[6]['previous_draft']['proposed_xml'], flags=re.S)
old_411_3[9] = (
    "Les règles de fond du présent article s'appliquent de plein droit aux actes qui transfèrent la propriété ou la jouissance de ces logements ou qui constatent ce transfert, sans qu'il soit nécessaire de les reproduire. La seule absence de reproduction du présent article dans un acte n'entraîne pas sa nullité."
)
old_411_3[10] = (
    "À la demande de tout intéressé ou de l'autorité administrative, le juge annule tout contrat qui méconnaît les règles de fond du présent article. Il ordonne, le cas échéant, la réaffectation des lieux à un usage d'habitation locative."
)
old_411_3.append(
    "La dispense de reproduction prévue au dixième alinéa s'applique aux actes conclus à compter de la date d'entrée en vigueur de la loi. Pour les actes conclus avant cette date, l'obligation de reproduction, la nullité de plein droit et l'action en nullité pour défaut de reproduction restent régies par les dispositions antérieures. Cette action peut être intentée par tout intéressé ou par l'autorité administrative dans un délai de cinq ans à compter de la publication de l'acte au fichier immobilier, même si cette publication intervient après l'entrée en vigueur de la loi. Les droits des occupants et les actions fondées sur la violation des règles de fond sont préservés."
)
add(
    6,
    paragraphs(*old_411_3),
    "Réforme de fond : suppression, pour les actes nouveaux, de la reproduction intégrale de l'article dans chaque acte de transfert de propriété ou de jouissance et de la nullité fondée sur cette seule omission. Copier une norme d'ordre public déjà applicable de plein droit ne justifie pas une cause autonome d'anéantissement du contrat. Aucune attestation ni mention de substitution n'est exigée. Les règles substantielles d'attribution, de ressources et de loyers, le maintien dans les lieux et l'action judiciaire avec réaffectation éventuelle restent essentiels pour empêcher la perte des protections attachées à un logement financé par l'État lors d'une cession. Les six exclusions favorables demeurent ouvertes aux futures opérations remplissant leurs conditions. Le reste de l'article reprend la réécriture claire antérieure à droit constant ; une transition protège les actes et recours antérieurs.",
    "Les onze alinéas initiaux restent dans leur ordre, avec la dispense au dixième et le pouvoir du juge au onzième ; un douzième alinéa porte la transition. Les deux voies d'entrée dans le champ, les logements appartenant ou ayant appartenu à un organisme, l'ordre public et les cessions non volontaires sont conservés. Les six exceptions restent distinctes : ventes selon L. 443-11, II premier alinéa et III et VI, ou L. 353-15, VI ; vente à un OFS selon L. 443-11, I premier alinéa ; SCI de L. 443-6-2 et suivants avec propriété d'un associé personne physique ; usufruit temporaire ; retour au bailleur après bail à construction ou emphytéotique ; lots de copropriétés sous plan de sauvegarde de L. 615-1 avec les précisions de L. 421-1, L. 422-2 et L. 422-3. Aucune exception supplémentaire de L. 411-4 n'est importée. L. 443-11, L. 353-15, L. 443-6-2 et L. 615-1 ont été lus pour contrôler les renvois. Coordination indispensable hors du lot : le VII de L. 353-15 exclut encore les communes des I ou II de L. 302-5 du bénéfice de son VI ; cette restriction fondée sur les quotas supprimés doit être retirée dans L. 353-15, conformément à sru_abrogation. Le renvoi conservé au VI ne vaut ni rétablissement de ce filtre ni réécriture de cet article extérieur au lot. Le renvoi à L. 442-6 et les protections des locataires demeurent ; L. 353-14 et L. 442-6 ont été lus. Le délai spécial de cinq ans à compter de la publication immobilière subsiste pour l'ancienne nullité de forme, y compris en cas de publication ultérieure ; il n'est ni transposé aux violations de fond ni redémarré par la réforme. R. 491-1, R. 491-2, R. 491-5 et R. 491-6, lus, conservent les plafonds, leur actualisation et les informations de bail sur leur montant et leur origine : ces informations utiles ne sont pas la copie intégrale abolie. Le texte initial de SRU 145 a été confronté à la source : les exceptions ont été enrichies et les anciens renvois à L. 353-15-1 et L. 442-6-1 ne sont pas réintroduits. Les protections et dérogations actuelles ont leur décision propre de maintien ; cette réduction ne vaut pas abrogation générale des effets de SRU 145.",
    [
        "L'obligation de reproduire intégralement L. 411-3 dans les actes nouveaux transférant la propriété ou la jouissance des logements ou constatant ce transfert.",
        "La nullité de plein droit et l'action spéciale fondées, pour ces actes nouveaux, sur la seule omission de la reproduction légale, sans suppression des actions protégeant les règles de fond.",
    ],
)

old_411_4 = re.findall(r'<p>(.*?)</p>', sources[7]['previous_draft']['proposed_xml'], flags=re.S)
old_411_4[1] = (
    "Les règles du premier alinéa s'appliquent de plein droit aux actes qui transfèrent la propriété ou la jouissance de ces logements ou qui constatent ce transfert, sans qu'il soit nécessaire de les reproduire. La seule absence de reproduction de cet alinéa dans un acte n'entraîne pas sa nullité."
)
old_411_4.append(
    "La dispense de reproduction prévue au deuxième alinéa s'applique aux actes conclus à compter de la date d'entrée en vigueur de la loi. Pour les actes conclus avant cette date, l'obligation de reproduction du premier alinéa, la nullité de plein droit et l'action en nullité pour défaut de reproduction restent régies par les dispositions antérieures. Cette action peut être intentée par tout intéressé ou par l'autorité administrative dans un délai de cinq ans à compter de la publication de l'acte au fichier immobilier, même si cette publication intervient après l'entrée en vigueur de la loi. Les droits des occupants et les recours fondés sur la violation des règles de fond sont préservés."
)
add(
    7,
    paragraphs(*old_411_4),
    "Réforme de fond : suppression, pour les actes nouveaux, de la copie obligatoire du premier alinéa et de la nullité attachée à sa seule omission. Les conditions de ressources et les maxima de loyers continuent de s'appliquer de plein droit ; aucun document ni déclaration ne remplace la reproduction. Leur maintien après déconventionnement ou transfert protège les locataires et l'affectation sociale des aides initiales, fonction essentielle que la simplification formelle ne doit pas retirer. Toutes les exclusions favorables subsistent pour les opérations futures recevables comme pour les situations antérieures. Les premier et troisième alinéas reprennent la réécriture antérieure à droit constant et la transition maintient le régime des actes anciens.",
    "Les trois alinéas initiaux restent à leur place, suivis de la transition. La date du 5 janvier 1977, les trois modalités de réalisation avec aide de l'État, la convention de L. 831-1, l'expiration de cette convention, les transferts même non volontaires et le renvoi à L. 353-19, lu, sont conservés. Quatre exclusions restent entières : retour des constructions au propriétaire du terrain après expiration du bail à construction ou emphytéotique ; ventes SEM de L. 443-11, II premier alinéa et III et VI ; accession progressive par SCI de L. 443-6-2 et suivants avec propriété d'un associé personne physique ; usufruit temporaire. La source omet « de » dans « des III et VI l'article L. 443-11 » : correction grammaticale expressément signalée, sans modification des subdivisions. L'ancienne nullité concerne la reproduction du seul premier alinéa, à la différence de L. 411-3 ; le délai de cinq ans court toujours de la publication de chaque acte ancien, même ultérieure à la réforme. Aucun délai de recours expiré n'est rouvert. R. 491-3, R. 491-4, R. 491-5 et R. 491-6, lus, conservent leurs plafonds, leur actualisation et les mentions utiles aux locataires. L. 365-5, lu, rend toujours le régime applicable aux logements des organismes agréés de maîtrise d'ouvrage ; l'allègement de L. 365-2 ne ferme ni ce fondement ni ses exceptions. SRU 145 ne comportait pas toutes les exclusions actuelles et visait anciennement L. 351-2, L. 353-15-1 et L. 442-6-1 : ces anciens renvois ne sont pas restaurés. La filiation initiale est distinguée du texte actuel ; aucune conclusion d'achèvement des 209 articles n'en est tirée.",
    [
        "L'obligation de reproduire le premier alinéa de L. 411-4 dans les actes nouveaux transférant la propriété ou la jouissance des logements ou constatant ce transfert.",
        "La nullité de plein droit et l'action spéciale attachées à la seule omission de cette reproduction dans les actes nouveaux, avec maintien des droits et recours relatifs aux actes antérieurs.",
    ],
)

Path('answer.json').write_text(json.dumps(answers, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answers)} articles')
