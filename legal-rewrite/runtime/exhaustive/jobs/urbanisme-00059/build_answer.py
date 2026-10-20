import json
import re
import html
from html.parser import HTMLParser
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
by_number = {a['number']: a for a in sources}
answers = {}


def plain(value):
    return html.unescape(re.sub(r'<[^>]*>', '', value or ''))


def paragraphs(*items):
    return '\n'.join('<p>' + s + '</p>' for s in items)


def replace_once(value, old, new):
    assert value.count(old) == 1, old
    return value.replace(old, new, 1)


def effect(kind, measure_id, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit,
                affected_population=population,
                conditions_and_transition=transition,
                replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


def add(number, proposed, reason, notes, assessment, limitations, burdens,
        effects=None, impact_class='material_reduction', removed=None,
        benefit=None, repeal_scope=None):
    src = by_number[number]
    obj = {k: src[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    obj.update(proposed_xml=proposed, reason=reason, review_notes=notes,
               status='retained_unchanged' if proposed is None else 'rewrite_draft')
    if proposed is None:
        obj['classification'] = 'retained_necessary'
        impact_class = 'retained_necessary'
    if removed:
        obj.update(change_type='normative_reduction',
                   reform_policy_id='editorial_direction_2026_10_19',
                   removed_provisions=removed)
    if repeal_scope:
        obj.update(change_type='full_repeal',
                   repeal_policy_id='editorial_direction_2026_10_19',
                   repeal_scope=repeal_scope)
    if benefit is not None:
        obj['benefit_review'] = benefit
    obj['substantive_impact'] = dict(version=1, classification=impact_class,
        assessment=assessment, scope_limitations=limitations,
        new_burdens_review=burdens, effects=effects or [])
    answers[number] = obj


no_global = " Aucun solde net de coût ou de complexité de l'ensemble des codes n'est établi."

# R113-12 : le transfert reste la contrepartie, sans caducité réglementaire.
n = 'R113-12'
proposal = paragraphs(
    "L'autorisation ne produit ses effets qu'après le transfert de propriété. Le plan local d'urbanisme est alors mis à jour conformément à l'article R. 153-18.",
    "Le transfert de propriété n'est soumis à aucun délai de caducité de l'autorisation au titre du présent article. Cette règle s'applique aux autorisations publiées à compter de l'entrée en vigueur du décret portant la présente réforme ainsi qu'aux autorisations dont le délai de transfert n'est pas expiré à cette date. Elle ne remet pas en vigueur une autorisation devenue caduque avant cette date et ne modifie ni les conditions de fond de la compensation ni les délais applicables sur un fondement distinct.")
add(n, proposal,
    "Réforme de fond : retrait du délai de deux ans imposé pour réaliser la cession compensatrice d'un espace boisé. Le transfert effectif demeure la condition préalable à l'effet de l'autorisation : l'allègement ne permet donc pas de construire sans fournir la contrepartie foncière. La mise à jour du PLU reste entière. La caducité automatique ne protège pas davantage le boisement tant que l'autorisation demeure sans effet avant la cession.",
    "Lecture de L113-3 à L113-5 et R113-8 à R113-11 : le dixième de superficie, l'acquisition à date certaine depuis cinq ans, la limite de valeur, l'accord communal, le décret et les engagements de préservation ne sont pas modifiés. R153-18 a été lu : la mise à jour et la communication de l'annexe restent à leur champ. Le délai retiré n'est ni le délai de décision de R113-8 ni une prorogation générale des permis. Préserver les cessions déjà conclues et les autres causes de caducité sur un fondement autonome ; ne pas rouvrir les autorisations déjà caduques.",
    "La source entière liait la compensation au transfert et à une limite de deux ans. Seule cette limite extinctive est supprimée ; le projet reste sans effet jusqu'au transfert.",
    "Les autorisations déjà caduques et les délais propres aux autres titres ne sont pas couverts. Aucun gain financier national ni nombre d'opérations sauvées n'est démontré.",
    "Aucune charge nouvelle n'est identifiée : ni déclaration de maintien, ni demande de prorogation, ni preuve périodique ne remplace les deux ans supprimés." + no_global,
    [effect('obligation_removed', 'urbanisme-compensation-boisee-sans-caducite',
        "Suppression de l'obligation de réaliser le transfert dans les deux ans sous peine de perdre l'autorisation.",
        "Propriétaires bénéficiaires de la compensation : transfert au plus tard deux ans après publication du décret ; autorisation sans effet avant transfert.",
        "Mêmes propriétaires : aucun délai extinctif de transfert sur ce fondement ; autorisation toujours sans effet avant le transfert.",
        'legal_duty', "Propriétaires bénéficiaires du 2° de L113-3.",
        "Autorisations nouvelles et délais non expirés à l'entrée en vigueur ; aucune renaissance d'une autorisation caduque.",
        "Aucune formalité de remplacement ; les conditions de compensation et la mise à jour du PLU restent.",
        "le transfert de propriété qui doit intervenir au plus tard dans les deux ans qui suivent la publication dudit décret.",
        "Le transfert de propriété n'est soumis à aucun délai de caducité de l'autorisation au titre du présent article.")],
    removed=["Délai de deux ans après publication du décret pour effectuer le transfert de propriété conditionnant l'effet de l'autorisation."],
    benefit="La possibilité de construire à titre de compensation reste ouverte aux futurs propriétaires éligibles ; sa contrepartie et ses limites de L113-3/4 sont conservées. La suppression de la caducité rend l'exercice de cet avantage moins fragile sans autoriser une construction avant la cession.")

add('R113-13', None,
    "Maintien intégral nécessaire de l'information du pétitionnaire lorsqu'une compensation boisée ne peut aboutir : irrecevabilité de fond, désaccord communal, refus exprès ou refus né du silence. Cette information protège l'exercice d'un recours et l'accès à la dérogation ; sa suppression économiserait une notification au détriment du demandeur sans retirer le pouvoir de refus.",
    "R113-8, L113-3 et L113-4 lus. Le délai de deux mois est celui du refus implicite après envoi du dossier par le préfet, non le délai de transfert supprimé dans R113-12. Pas de renvoi déplacé. La graphie source « ne peut-être » est laissée dans la source, sans fabriquer une réécriture stylistique. Aucune obligation de dépôt ou pièce à la charge du demandeur n'est ajoutée.",
    "L'article ne prélève rien et n'institue pas une autorisation distincte : il impose à l'administration d'informer le demandeur de l'échec de sa demande de compensation.",
    "Le régime du décret et le délai de R113-8 demeurent hors de cette modification de R113-12 ; aucune accélération globale de la procédure n'est revendiquée.",
    "Aucune charge nouvelle n'est identifiée puisque le texte est maintenu intégralement. L'information protectrice n'est remplacée par aucun registre ni justificatif." + no_global,
    benefit="L'information de refus demeure accessible pour les demandes futures de compensation ; elle permet de contester le refus ou de revoir le projet sans retirer la possibilité de construire prévue par L113-3.")

add('R113-14', None,
    "Maintien intégral du mécanisme favorable qui empêche l'avis d'une collectivité voisine de bloquer indéfiniment une convention volontaire d'ouverture au public. Les trois mois bornent une consultation territoriale prévue par L113-7 ; ils ne constituent pas un délai minimal obligatoire lorsque la réponse arrive plus tôt. Aucun second dossier ou agrément n'est créé ici.",
    "L113-6 et L113-7 lus en entier : financement total ou partiel des aménagements, entretien, réparations, assurance et rémunération du propriétaire restent possibles. Le mot « refus » de la source concerne l'avis consultatif, non un veto nouveau sur la convention ; pas de transformation en autorisation. Les trois mois et l'avis favorable implicite sont conservés.",
    "Le texte source contient déjà une garantie favorable de silence valant avis favorable ; aucun doublon matériel à supprimer n'est démontré dans cet article.",
    "Aucun délai maximal plus court ni suppression de la consultation législative n'est proposé. La convention et ses financements restent régis par leurs textes propres.",
    "Aucune charge nouvelle n'est identifiée : maintien intégral du délai maximal et de l'effet favorable du silence, sans attestation ni nouvelle déclaration." + no_global,
    benefit="Le silence favorable demeure pour toutes les conventions futures relevant de L113-7. Les facultés de financement et de rémunération de L113-6 ne sont ni supprimées ni réservées aux conventions anciennes.")

# Police ENS : retirer la police spéciale supprimée au niveau législatif,
# conserver le classement boisé et corriger expressément l'autorité compétente.
proposal = paragraphs(
    "Pour l'application du classement prévu à l'article L. 113-11, le président du conseil départemental, sur proposition du conseil départemental, saisit pour avis le conseil municipal de chaque commune intéressée, ainsi que la commission départementale de la nature, des paysages et des sites, d'un projet tendant à déterminer les bois, forêts et parcs à soumettre au régime des espaces boisés classés en application de l'article L. 113-1 et des textes pris pour son application. Le classement ne peut être prononcé que dans le champ et aux conditions de l'article L. 113-11.",
    "Aucune mesure de réglementation de l'utilisation du sol ne peut être édictée sur le seul fondement de l'article L. 113-12 abrogé.",
    "1° Abrogé.",
    "2° Abrogé.",
    "La présente rédaction s'applique aux arrêtés pris à compter de l'entrée en vigueur du décret portant la présente réforme, y compris dans les procédures en cours, sans recommencement des consultations régulièrement accomplies sur le même projet. Elle ne régularise pas les actes antérieurs pris par une autorité incompétente. Les prescriptions fondées exclusivement sur l'article L. 113-12 cessent de produire effet dans les conditions de son abrogation ; les protections et dérogations ayant un fondement distinct demeurent applicables.")
add('R113-15', proposal,
    "Coordination de fond avec la suppression proposée de L113-12 : retrait des deux catégories de restrictions spéciales sur les chemins, adductions d'eau, terrains de camping et hébergements de loisirs. Le classement boisé autonome de L113-11 et son expertise environnementale restent. Correction expresse de l'incohérence de compétence : la loi attribue l'arrêté au président du conseil départemental, non au préfet. L'avis communal demeure ; le règlement ne peut dispenser de la délibération communale exigée par la loi au moyen d'un seul avis d'EPCI.",
    "L113-1/2 et L113-8 à L113-14, sources et propositions du corpus, lus. L113-11 proposé conserve le pouvoir dans les seuls départements ayant antérieurement satisfait à son préalable fiscal, sans rétablir la part départementale supprimée ; cette limite s'impose au classement réglementaire. Le passage de L113-12 à L113-11 est délibéré, pas une correction silencieuse. Le préfet est remplacé au même emplacement ; la saisine du conseil municipal assure la délibération législativement requise, sans seconde consultation d'EPCI imposée. Les 1° et 2° restent repérés comme abrogés. Les exceptions agricoles et de desserte des bâtiments ne deviennent pas des interdictions : toute la restriction spéciale correspondante disparaît. Préserver L113-13, les classements autonomes, les dérogations de L113-2 et les règles littorales. Aucun achèvement de filiation SRU n'est affirmé.",
    "La source entière combinait classement boisé et restrictions supplémentaires d'usage du sol. Les deux pouvoirs supplémentaires sont retirés en exécution de L113-12 ; ce n'est pas une seconde mesure autonome de suppression.",
    "La réduction dépend de l'adoption de l'abrogation législative de L113-12 ; elle n'efface ni classement de L113-11 ni normes environnementales autonomes. Les actes anciens ne sont pas validés rétroactivement.",
    "Aucune charge nouvelle n'est identifiée : le classement, la proposition départementale, la délibération communale légale et l'avis environnemental subsistent ; aucune déclaration ne remplace les restrictions retirées." + no_global,
    [effect('coordination', 'espaces-naturels-sensibles-fin-police-speciale',
        "Retrait réglementaire des restrictions propres au pouvoir de L113-12 supprimé.",
        "Pouvoir d'imposer des restrictions particulières de travaux, d'adduction d'eau et d'accueil de loisirs dans les zones de préemption.",
        "Aucune prescription sur ce seul fondement ; classement boisé et protections d'autres fondements maintenus.",
        'legal_duty', "Propriétaires et porteurs de projets situés dans les zones de préemption ENS.",
        "Coordination avec l'abrogation législative ; arrêtés nouveaux et cessation des effets exclusivement fondés sur L113-12 selon sa transition.",
        "Pas de déclaration ou autorisation de remplacement ; pas de retrait des protections légales autonomes.",
        "Interdire ou soumettre à des conditions particulières l'aménagement et l'ouverture des terrains destinés à accueillir de manière habituelle des tentes, des caravanes ou des habitations légères de loisirs.",
        "Aucune mesure de réglementation de l'utilisation du sol ne peut être édictée sur le seul fondement de l'article L. 113-12 abrogé."),
     effect('coordination', 'classement-boise-competence-departementale',
        "Mise en cohérence de la compétence réglementaire avec L113-11.",
        "Règlement visant le préfet et l'avis municipal ou intercommunal, alors que L113-11 attribue la décision au président départemental après délibération communale.",
        "Président départemental compétent ; avis de chaque conseil municipal et commission des sites conservés dans le champ légal du classement.",
        'regime', "Départements et communes concernés par le classement autonome de L113-11.",
        "Arrêtés pris après entrée en vigueur réglementaire ; actes anciens non régularisés par cette seule coordination.",
        "Aucune consultation supplémentaire d'EPCI n'est créée ; la délibération communale était déjà légalement requise.",
        "le préfet, sur proposition du conseil départemental, saisit pour avis le conseil municipal de la commune intéressée ou l'organe délibérant de l'établissement public de coopération intercommunale compétent, ainsi que la commission départementale de la nature, des paysages et des sites",
        "le président du conseil départemental, sur proposition du conseil départemental, saisit pour avis le conseil municipal de chaque commune intéressée, ainsi que la commission départementale de la nature, des paysages et des sites")],
    impact_class='coordination_only',
    removed=["Pouvoir réglementaire spécial de limiter les chemins et adductions d'eau des particuliers dans les seules zones de préemption ENS.",
             "Pouvoir réglementaire spécial d'interdire ou de conditionner l'accueil habituel de tentes, caravanes et habitations légères de loisirs sur le fondement abrogé de L113-12."],
    benefit="Les exceptions de desserte des bâtiments existants et d'amélioration agricole ne sont pas retranchées d'une règle générale encore applicable : cette règle spéciale est entièrement retirée. Les dérogations au classement boisé de L113-2, dont les gisements reconnus avant le 10 juillet 1973, restent ouvertes aux futures demandes recevables, ainsi que les dérogations littorales autonomes.")

proposal = paragraphs(
    "L'avis du conseil municipal de chaque commune concernée doit être transmis au président du conseil départemental dans les trois mois à compter du jour où le maire a reçu la demande d'avis. Il est réputé favorable si aucune réponse n'a été donnée dans ce délai.",
    "Au vu des avis recueillis, le président du conseil départemental fixe par arrêté le classement prévu à l'article L. 113-11, dans le champ et aux conditions de cet article.",
    "La présente rédaction s'applique aux arrêtés pris à compter de l'entrée en vigueur du décret portant la présente réforme. Pour les consultations en cours portant sur le même projet, les avis déjà recueillis et le temps déjà écoulé sont conservés ; aucun nouveau délai de trois mois ne commence du seul fait du changement d'autorité destinataire. Elle ne régularise pas les actes antérieurs pris par une autorité incompétente et ne rétablit aucune mesure fondée exclusivement sur l'article L. 113-12 abrogé.")
add('R113-16', proposal,
    "Coordination nécessaire de la compétence et du champ avec R113-15 et L113-11 : la décision appartient au président du conseil départemental, et non au préfet ; elle ne porte plus sur la police spéciale supprimée de L113-12. Le délai maximal de trois mois et l'avis favorable implicite restent entiers. Aucune réduction propre de délai n'est revendiquée.",
    "Incohérence préexistante président/préfet identifiée dans L113-11 : correction expresse, sans validation des arrêtés anciens. La consultation communale est requise par la loi ; l'alternative EPCI du règlement ne peut l'écarter. Conservation de l'avis CDNPS prévu à R113-15 : le second alinéa vise tous les avis recueillis, pas les seuls avis communaux. Ni nouveau préalable fiscal, ni nouveau pouvoir de restriction. R113-17 conserve les garanties de publicité dans sa rédaction coordonnée.",
    "La proposition retire la discordance d'autorité et cantonne l'arrêté au classement maintenu. Le délai de trois mois et son effet favorable ne changent pas par rapport à la source officielle.",
    "La légalité des actes antérieurs et les recours relèvent de leurs règles propres. La disparition de la police spéciale relève de L113-12 et n'est pas comptée une deuxième fois.",
    "Aucune charge nouvelle n'est identifiée : mêmes avis utiles et même délai, sans nouvelle saisine obligatoire ni remise à zéro des consultations en cours." + no_global,
    [effect('coordination', 'classement-boise-competence-departementale',
        "Correction de l'auteur de l'arrêté et de son destinataire d'avis.",
        "Avis adressés au préfet, puis arrêté préfectoral fixant les mesures de protection ; trois mois et silence favorable.",
        "Avis adressés au président départemental, puis arrêté limité au classement de L113-11 ; trois mois et silence favorable conservés.",
        'regime', "Communes et département concernés par un projet de classement boisé.",
        "Arrêtés nouveaux ; consultations en cours conservées sans nouveau départ de délai.",
        "Pas de nouvelle déclaration, pas de délai supplémentaire, pas de régularisation automatique d'actes anciens.",
        "Au vu des avis recueillis, le préfet fixe par arrêté les mesures de protection.",
        "Au vu des avis recueillis, le président du conseil départemental fixe par arrêté le classement prévu à l'article L. 113-11, dans le champ et aux conditions de cet article.")],
    impact_class='coordination_only',
    benefit="L'avis réputé favorable au terme de trois mois est conservé pour les procédures futures et celles déjà engagées. Le temps déjà écoulé n'est pas perdu du fait de la coordination de compétence.")

proposal = paragraphs(
    "L'arrêté du président du conseil départemental prévu à l'article R. 113-16 fait l'objet d'une publication au recueil des actes administratifs du département. Aucune mention dans un journal n'est exigée au titre du présent article.",
    "Les effets juridiques attachés à cet arrêté ont pour point de départ sa publication au recueil des actes administratifs du département.",
    "En outre, un dossier comportant l'arrêté et un document graphique est tenu à la disposition du public dans les mairies des communes intéressées, à la préfecture, au siège du conseil départemental et au service de l'Etat chargé de l'urbanisme dans le département.",
    "La présente rédaction s'applique aux arrêtés pris à compter de l'entrée en vigueur du décret portant la présente réforme. Les règles antérieures de publicité et de prise d'effet restent applicables aux arrêtés pris avant cette date ; la présente rédaction n'en régularise ni la compétence ni la publicité. Elle ne prolonge pas les effets d'un arrêté au-delà du terme prévu à l'article L. 113-13.")
add('R113-17', proposal,
    "Réduction de fond : suppression des deux annonces obligatoires en journaux, en maintenant la publication officielle et la consultation locale du dossier avec son plan dans chacun des lieux prévus. Ces annonces reproduisent l'existence d'un acte déjà publié et accessible ; aucun contenu de protection n'en dépend. Coordination expresse du préfet vers le président départemental conformément à L113-11 et R113-16, et de la prise d'effet vers la seule publication officielle.",
    "Les trois alinéas fonctionnels restent dans l'ordre : publicité, prise d'effet, dossier public ; transition ajoutée à la fin. Le dossier reste disponible dans les mairies, à la préfecture, au département et au service d'urbanisme ; aucun déplacement vers un accès uniquement numérique. Le premier jour de la publication officielle remplace l'achèvement des deux mentions pour les seuls arrêtés nouveaux. Anciennes publicités et contentieux restent sous leur régime. Cessation favorable lors de l'approbation d'un PLU selon L113-13 maintenue ; la publication ne peut faire revivre les restrictions de L113-12.",
    "Deux annonces de presse sont effectivement retirées pour les nouveaux arrêtés ; l'information officielle et le plan restent accessibles. La compétence est coordonnée sans gain fiscal revendiqué.",
    "Le coût des annonces et l'incidence de la prise d'effet plus précoce ne sont pas chiffrés. Le régime des arrêtés anciens ne change pas ; aucune nouvelle restriction foncière n'est créée par cet article.",
    "Aucune charge nouvelle n'est identifiée : la publication au recueil et la disponibilité du dossier existaient déjà. Aucun site, registre, copie certifiée ou envoi de remplacement n'est imposé." + no_global,
    [effect('obligation_removed', 'urbanisme-publicite-fonciere-sans-presse',
        "Retrait des deux mentions de presse de l'arrêté de classement.",
        "Publication au recueil plus mentions dans deux journaux régionaux ou locaux diffusés dans le département.",
        "Publication au recueil sans mention de presse, avec maintien du dossier et du plan à disposition du public.",
        'legal_duty', "Département auteur du classement de L113-11 ; personnes consultant ses mesures.",
        "Arrêtés pris dès l'entrée en vigueur réglementaire ; arrêtés antérieurs sous leurs anciennes règles.",
        "Aucun support supplémentaire ; la prise d'effet suit la publication officielle déjà obligatoire.",
        "d'une publication au recueil des actes administratifs du département et d'une mention dans deux journaux régionaux ou locaux diffusés dans le département.",
        "Aucune mention dans un journal n'est exigée au titre du présent article."),
     effect('coordination', 'classement-boise-competence-departementale',
        "Identification de l'auteur légal de l'arrêté publié.",
        "Le règlement organise la publicité d'un arrêté du préfet, en discordance avec L113-11.",
        "Le règlement vise l'arrêté du président départemental, sans nouveau pouvoir de classement.",
        'regime', "Département compétent au titre de L113-11.",
        "Arrêtés nouveaux ; actes anciens non régularisés par cette rédaction.",
        "Aucune charge nouvelle liée au changement d'autorité ; autres lieux d'accès au dossier conservés.",
        "L'arrêté du préfet prévu à l'article R. 113-16",
        "L'arrêté du président du conseil départemental prévu à l'article R. 113-16")],
    removed=["Double mention obligatoire de l'arrêté dans deux journaux régionaux ou locaux, en plus de la publication officielle et du dossier public."],
    benefit="Les dérogations et la cessation des effets du classement prévues par ses textes légaux restent entières. Le public conserve tous les lieux d'accès au dossier et à son document graphique ; aucune dérogation littorale ou possibilité de compensation n'est fermée.")

proposal = paragraphs(
    "Les recettes de la part départementale de la taxe d'aménagement destinée au financement des espaces naturels sensibles, correspondant à des faits générateurs antérieurs à sa suppression prévue à l'article L. 113-10, ainsi que les emplois de ces recettes, font l'objet d'un bilan dans un tableau annexe au budget de la collectivité territoriale compétente. Ce bilan demeure établi tant que des recettes anciennes ou leurs emplois restent à retracer.",
    "Le tableau retrace également les régularisations et restitutions afférentes à ces faits générateurs. Il ne constitue ni un fondement d'imposition pour des faits générateurs nouveaux ni une déclaration à la charge des redevables. Les affectations des produits anciens, les exonérations et autres avantages, les règles de liquidation et de recouvrement ainsi que les prescriptions et voies de recours restent ceux applicables à ces faits générateurs.")
add('R113-18', proposal,
    "Coordination avec l'abolition proposée de la part départementale à L113-10 : le tableau ne peut ni supposer l'institution d'une taxe future ni en permettre le rétablissement. Le suivi des seuls anciens produits et de leurs emplois reste nécessaire à leur affectation légale et aux restitutions. Il n'est pas supprimé comme un rapport sans fonction et n'impose aucun dépôt fiscal au contribuable.",
    "L113-8 et L113-10, source et proposition, lus. Le fait générateur ancien se distingue d'un encaissement ou d'une échéance postérieurs ; le tableau doit retracer ces produits, leurs emplois et les restitutions, sans les faire disparaître du budget. Les coordinations CGI 1586 II, 1635 quater A/K/L/M/T et les règles budgétaires du CGCT signalées dans le corpus ne sont pas réputées rédigées ici. L'ancien renvoi de L113-10 à L331-3 présente un problème de concordance fiscale préexistant ; la rédaction n'en tire aucun pouvoir fiscal nouveau. Maintien du tableau, et non création d'un nouveau rapport annuel ou registre parallèle.",
    "Le texte officiel organisait un bilan d'une taxe instituée. La proposition le réserve au stock de recettes et d'emplois anciens de la taxe supprimée par L113-10 ; elle n'abolit pas une seconde taxe.",
    "L'abolition et son champ territorial dépendent du texte législatif et des coordinations fiscales. Le coût du suivi budgétaire résiduel et la perte de recettes ne sont pas évalués dans ce lot.",
    "Aucune charge nouvelle n'est identifiée : le tableau budgétaire existant est conservé pour les mêmes flux anciens ; ni contribuable ni collectivité ne doit produire un état de remplacement." + no_global,
    [effect('coordination', 'part-departementale-taxe-amenagement-suppression',
        "Cantonnement du bilan budgétaire aux flux anciens de la part départementale supprimée.",
        "Tableau de recettes et d'emplois lorsque la part départementale destinée aux ENS a été instituée.",
        "Même support de bilan pour les seules recettes et emplois anciens ; aucune imposition ou déclaration future fondée sur ce tableau.",
        'regime', "Collectivités bénéficiaires des anciens produits affectés aux ENS.",
        "Faits générateurs antérieurs à la suppression de L113-10, même en cas d'encaissement ultérieur ; suivi jusqu'à extinction des flux à retracer.",
        "Aucun nouveau registre ni déclaration fiscale ; affectations, restitutions et recours anciens maintenus.",
        "un tableau annexe au budget de cette collectivité fait le bilan des recettes et des emplois de cette taxe.",
        "Il ne constitue ni un fondement d'imposition pour des faits générateurs nouveaux ni une déclaration à la charge des redevables.")],
    impact_class='coordination_only',
    benefit="Le tableau n'est pas une exonération, mais le suivi des restitutions et des avantages anciens est préservé. Les exonérations des autres parts de taxe d'aménagement restent ouvertes aux opérations futures selon leurs textes ; aucun taux ou assiette n'est augmenté ici.")

add('R113-19', None,
    "Maintien intégral du plan et de la notice qui justifient le choix du périmètre périurbain. Cette décision rend durablement des terrains inconstructibles au titre de L113-20 et ouvre des facultés d'acquisition : l'identification des limites et l'analyse initiale motivée protègent les propriétaires et le public. Aucun second dossier, formulaire, déclaration privée ou étude périodique n'est exigé par cet article.",
    "L113-15 à L113-20 et R113-20 à R113-23 lus. La suppression proposée des avis de création n'efface pas les pièces utiles à l'accord communal et à l'enquête publique ; le plan de délimitation ne se confond pas avec le seul plan de situation de R113-21/22. Aucune obligation de supports distincts n'est imposée par la source, donc aucun gain de fusion artificiel n'est revendiqué. Les exclusions de L113-17 restent favorables aux terrains concernés.",
    "La source exige les informations minimales justifiant une restriction foncière durable. Aucun élément redondant ou prélèvement autonome n'y est identifié après examen du corps entier.",
    "Le présent maintien ne valide ni un périmètre particulier ni les pouvoirs de préemption ; il ne couvre pas les modifications régies par L113-19.",
    "Aucune charge nouvelle n'est identifiée : maintien exact du plan et de la notice, sans nouveau support obligatoire, attestation ou collecte de données." + no_global,
    benefit="Les terrains exclus du périmètre par L113-17 conservent leurs exclusions. Le mécanisme facultatif et l'accès aux documents de L113-16 restent ouverts aux futurs projets, avec motivation des bénéfices agricoles, forestiers et environnementaux.")

proposal = paragraphs(
    "Le président du conseil départemental soumet le projet, pour accord, aux communes ou aux établissements publics compétents en matière de plan local d'urbanisme concernés.",
    "La création du périmètre ne nécessite pas la saisine pour avis de la chambre départementale d'agriculture ni de l'établissement public chargé du schéma de cohérence territoriale. Aucun délai d'attente de ces avis n'est exigé.",
    "La présente rédaction s'applique aux décisions de création prises à compter de l'entrée en vigueur du décret portant la présente réforme, y compris dans les procédures en cours. Les accords et autres actes régulièrement accomplis sur le même projet restent utilisables sans nouveau dépôt ni reprise de délai. Elle ne modifie pas les consultations propres aux modifications du périmètre ou à l'élaboration et à la modification du programme d'action prévues aux articles L. 113-19, L. 113-21 à L. 113-23 et R. 113-25.")
add('R113-20', proposal,
    "Coordination de la suppression des deux avis de création déjà retenue à L113-16 : retrait de la saisine de la chambre d'agriculture, de celle de l'établissement du SCoT et de l'attente de deux mois. L'accord des autorités locales compétentes demeure, sans nouvel agrément de remplacement. Cette exécution réglementaire n'est pas une seconde réduction autonome.",
    "Source officielle et proposition de L113-16 lues intégralement. R113-21 est coordonné pour ne pas exiger les avis retirés au dossier d'enquête. L113-18 maintient la compatibilité SCoT ; L113-21/22 et R113-25 conservent les consultations du programme d'action. L'accord communal n'est pas rendu tacite par suppression du délai attaché aux seuls avis. Portée rédactionnelle départementale conservée : L113-16 autorise aussi l'établissement de L143-16 à être porteur ; cette compétence législative demeure et les modalités réglementaires correspondantes restent à harmoniser, sans lui imposer ici une nouvelle consultation. Aucune filiation SRU présumée.",
    "Les deux saisines pour avis et leur attente disparaissent du règlement conformément à L113-16 ; l'accord local et l'enquête publique subsistent. Aucune seconde procédure supprimée n'est comptée.",
    "Seule la création est couverte : les modifications et le programme d'action gardent leurs consultations légales. Les règles de portage par l'établissement de L143-16 demandent une harmonisation de compétence distincte.",
    "Aucune charge nouvelle n'est identifiée : les avis retirés ne sont remplacés par aucune déclaration, étude, attestation ou confirmation ; les accords existants sont conservés." + no_global,
    [effect('coordination', 'urbanisme-perimetre-periurbain-fin-avis-prealables',
        "Exécution réglementaire de la fin des deux consultations obligatoires de création.",
        "Saisine pour avis de la chambre d'agriculture et de l'établissement du SCoT, avec silence favorable au terme de deux mois.",
        "Ni ces saisines ni l'attente de deux mois ; accord local maintenu, sans créer un accord tacite.",
        'legal_duty', "Département créant un périmètre périurbain ; organismes précédemment consultés.",
        "Décisions de création nouvelles et procédures en cours ; pas de recommencement des accords et actes réguliers.",
        "Aucune formalité de remplacement ; enquêtes et consultations du programme restent distinctes.",
        "Le projet est également adressé, pour avis, à la chambre départementale d'agriculture ainsi qu'à l'établissement public chargé du schéma de cohérence territoriale s'il existe.",
        "La création du périmètre ne nécessite pas la saisine pour avis de la chambre départementale d'agriculture ni de l'établissement public chargé du schéma de cohérence territoriale.")],
    impact_class='coordination_only',
    removed=["Saisines obligatoires pour avis de la chambre départementale d'agriculture et de l'établissement public du SCoT pour la création du périmètre.",
             "Attente de deux mois attachée aux avis de création désormais supprimés, sans toucher aux accords locaux ou aux avis propres du programme d'action."],
    benefit="L'allègement est ouvert aux projets futurs et en cours ; les accords locaux existants ne sont pas à renouveler. Les enquêtes conjointes permises par L113-16 et les exclusions favorables de L113-17 restent possibles.")

proposal = paragraphs(
    "Le projet de création du périmètre, assorti d'un plan de situation et de l'ensemble des accords recueillis, est soumis à enquête publique selon la procédure prévue aux articles R. 123-7 à R. 123-23 du code de l'environnement, par le président du conseil départemental qui exerce les compétences attribuées au préfet par ces dispositions.",
    "Les avis dont la saisine n'est plus exigée pour la création du périmètre en application de l'article L. 113-16 ne sont pas des pièces obligatoires du dossier d'enquête. Leur absence n'entraîne ni nouveau dépôt, ni report, ni recommencement de l'enquête. Cette règle s'applique aux procédures en cours à l'entrée en vigueur du décret portant la présente réforme ; elle ne remet pas en cause les enquêtes régulièrement accomplies ni les accords locaux requis.")
add('R113-21', proposal,
    "Coordination nécessaire du dossier d'enquête avec L113-16 et R113-20 : ne plus exiger les avis dont la saisine est supprimée. Le plan de situation, tous les accords nécessaires et l'enquête environnementale complète demeurent. Il s'agit de la même mesure de suppression des avis, et non d'une seconde autorisation ou d'un nouveau délai supprimé.",
    "Renvois de L113-16, L113-19, R113-19/20/22 lus. La substitution « accords recueillis » à « accords et avis recueillis » n'exonère pas d'autres pièces exigées sur un fondement autonome par la procédure d'enquête. Le renvoi R123-7 à R123-23 du code de l'environnement est conservé ; le texte intégral de ce code n'est pas dans le corpus des cinq codes indiqué, donc aucune conformité environnementale exhaustive n'est prétendue. La rédaction garde le portage départemental de la source ; l'harmonisation réglementaire avec le portage légal de L143-16 demeure identifiée comme limite. Aucun accord local manquant n'est réputé acquis.",
    "Le dossier obligatoire ne réintroduit plus les avis de création supprimés. Les pièces de localisation, les accords et la participation publique sont intégralement maintenus.",
    "L'enquête publique et les pièces autonomes de son régime restent exigées ; le portage par l'établissement public prévu à L113-16 n'est pas harmonisé par cette seule phrase départementale.",
    "Aucune charge nouvelle n'est identifiée : aucune attestation d'absence d'avis ni nouvelle enquête n'est requise, et les dossiers en cours bénéficient de la dispense sans redépôt." + no_global,
    [effect('coordination', 'urbanisme-perimetre-periurbain-fin-avis-prealables',
        "Retrait du besoin de joindre au dossier les avis de création supprimés.",
        "Projet assorti du plan de situation et de l'ensemble des accords et avis recueillis.",
        "Plan de situation et accords conservés ; les avis de création supprimés ne sont plus des pièces obligatoires.",
        'legal_duty', "Porteurs départementaux de périmètres soumis à enquête et public participant.",
        "Procédures en cours et futures dès entrée en vigueur réglementaire, sans refaire les enquêtes régulières.",
        "Pas de pièce négative ni attestation en remplacement ; procédure environnementale maintenue.",
        "Le projet de création du périmètre, assorti d'un plan de situation et de l'ensemble des accords et avis recueillis, est soumis à enquête publique",
        "Les avis dont la saisine n'est plus exigée pour la création du périmètre en application de l'article L. 113-16 ne sont pas des pièces obligatoires du dossier d'enquête.")],
    impact_class='coordination_only',
    removed=["Exigence de joindre les avis de création retirés par L113-16 au dossier d'enquête publique du périmètre périurbain."],
    benefit="Le droit de participer à l'enquête et la possibilité légale d'enquêtes conjointes restent entiers. Les porteurs futurs bénéficient aussi de la dispense d'avis ; elle ne se limite pas aux dossiers déjà déposés.")
