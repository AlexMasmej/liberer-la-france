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

proposal = paragraphs(
    "La création du périmètre est décidée par une délibération du conseil départemental.",
    "Cette délibération, accompagnée des plans de situation et de délimitation, est publiée au recueil des actes administratifs du département et affichée pendant un mois à l'hôtel du département, dans les mairies des communes incluses dans le périmètre et, le cas échéant, au siège de l'établissement public de coopération intercommunale compétent en matière de plan local d'urbanisme. Ces publications et affichages indiquent les lieux où le dossier peut être consulté. Pour l'application de l'article L. 3131-1 du code général des collectivités territoriales, la date à prendre en compte pour l'affichage est celle du premier jour où il est effectué. Aucune mention dans un journal n'est exigée au titre du présent article.",
    "Aucune transmission individuelle de cette délibération et de ses plans au directeur départemental des finances publiques, au Conseil supérieur du notariat, à la chambre départementale des notaires, aux barreaux ou aux greffes des tribunaux judiciaires n'est exigée au seul titre du présent article. Les obligations de transmission ayant un fondement distinct demeurent applicables.",
    "La présente rédaction s'applique aux délibérations prises à compter de l'entrée en vigueur du décret portant la présente réforme. Les règles antérieures restent applicables à la publicité et à la prise d'effet des délibérations prises avant cette date ; aucun délai de recours expiré n'est rouvert.")
add('R113-22', proposal,
    "Réduction de fond : retrait de l'annonce dans un journal et du circuit de copies individuelles de la délibération et de ses plans vers les finances publiques, organisations notariales, barreaux et greffes. Le périmètre reste décidé par délibération, publié officiellement avec ses deux plans, affiché un mois dans tous les lieux prévus et consultable aux lieux indiqués. Cette publicité territoriale et documentaire rend les copies professionnelles supplémentaires dispensables ; aucune donnée nécessaire à la définition du périmètre n'est retirée.",
    "Source et note du décret 2019-966 lues en entier : le 1er janvier 2020 est une date historique de changement de juridiction, pas celle de la réforme proposée. Les trois alinéas fonctionnels restent repérables et le second conserve plans, mois d'affichage, lieux de consultation et date du premier jour. Son renvoi est celui repris par R113-26, coordonné dans ce lot ; suppression de l'annonce propagée à ce programme sans compter un deuxième allègement autonome. Les obligations de publicité et de transmission au contrôle de légalité sur un fondement distinct ne sont pas supprimées. CGCT L3131-1 appelle vérification de concordance avec les règles actuelles de publication des actes, hors corpus fourni ; ce renvoi n'est pas transformé en dispense de contrôle. Le champ réglementaire départemental demeure plus étroit que la faculté législative de portage de L113-16 : harmonisation encore à réaliser, sans inventer une compétence exclusive du département.",
    "Un support de presse et les envois spécialisés de la même délibération sont effectivement supprimés ; publication officielle, deux plans, accès local et affichage d'un mois restent inchangés.",
    "Les délibérations anciennes gardent leur régime. Les transmissions autonomes et la concordance CGCT restent hors de cette dispense ; le coût public de publication n'est pas chiffré.",
    "Aucune charge nouvelle n'est identifiée : les publicités conservées et la mise à disposition existaient déjà ; aucun abonnement, registre ou demande d'information compensatoire n'est imposé." + no_global,
    [effect('obligation_removed', 'urbanisme-publicite-fonciere-sans-presse',
        "Suppression de l'annonce de presse lors de la création du périmètre périurbain.",
        "Mention dans un journal diffusé dans le département, en plus du recueil et des affichages.",
        "Aucune annonce de presse ; recueil avec les deux plans, affichage d'un mois et indication des lieux de consultation maintenus.",
        'legal_duty', "Département créant un périmètre périurbain et public concerné.",
        "Délibérations prises dès l'entrée en vigueur réglementaire ; publicité et effet des délibérations antérieures préservés.",
        "Aucun support nouveau ; les obligations autonomes d'information et de contrôle de légalité restent.",
        "fait l'objet d'une mention dans un journal diffusé dans le département.",
        "Aucune mention dans un journal n'est exigée au titre du présent article."),
     effect('obligation_removed', 'urbanisme-zonages-fin-copies-professionnelles',
        "Retrait du circuit de copies spécialisées de la délibération et des plans déjà publiés.",
        "Envoi simultané au directeur départemental des finances publiques, aux deux échelons notariaux, aux barreaux et aux greffes concernés.",
        "Pas de ces copies sur ce seul fondement ; plans publiés et dossier public maintenus.",
        'legal_duty', "Département et destinataires professionnels ou judiciaires du périmètre.",
        "Délibérations nouvelles ; autres transmissions légalement autonomes conservées.",
        "Aucune déclaration de remplacement ni nouvel accès à des données personnelles ; publicité existante conservée.",
        "Cette délibération, accompagnée des plans de situation et de délimitation, est simultanément transmise au directeur départemental des finances publiques, au Conseil supérieur du notariat, à la chambre départementale des notaires, aux barreaux constitués près les   tribunaux judiciaires dans le ressort desquels est institué le périmètre de protection ainsi qu'au greffe de ces tribunaux.",
        "Aucune transmission individuelle de cette délibération et de ses plans au directeur départemental des finances publiques, au Conseil supérieur du notariat, à la chambre départementale des notaires, aux barreaux ou aux greffes des tribunaux judiciaires n'est exigée au seul titre du présent article.")],
    removed=["Mention obligatoire de la délibération de création du périmètre dans un journal diffusé dans le département, en supplément de ses publicités officielles et locales.",
             "Transmission individuelle simultanée de la délibération et des plans aux finances publiques, instances notariales, barreaux et greffes sur le seul fondement de R113-22."],
    benefit="L'accès au dossier et aux deux plans demeure pour le public et les professionnels, dans les mêmes lieux. La faculté de définir un périmètre et les exclusions de L113-17 ne sont pas restreintes ; l'allègement vaut pour toutes les futures délibérations recevables.")

add('R113-23', None,
    "Maintien intégral de l'enquête publique limitée aux seules communes concernées par une extension. Cette règle évite une enquête sur tout le périmètre et assure la participation des propriétaires et habitants auxquels s'appliqueront les nouvelles restrictions. Il ne s'agit ni d'une déclaration supplémentaire ni d'une répétition d'enquête dans les communes inchangées.",
    "L113-16 et L113-19 lus : l'extension du périmètre reste distincte de sa création et du retrait de terrains. La suppression des avis de création dans R113-20 ne supprime pas les consultations propres à la modification. Aucun minimum de délai, tableau ou pièce supplémentaire dans cet article. Le renvoi implicite au régime d'enquête reste compatible avec R113-21 et les exigences environnementales autonomes.",
    "La limitation géographique de l'enquête est déjà un allègement dans la source entière. Le maintien n'est pas compté comme une nouvelle réduction ni comme une réécriture.",
    "Ni la durée ni le régime général de l'enquête ne sont modifiés ; la règle ne couvre que les extensions et non tous les changements de périmètre.",
    "Aucune charge nouvelle n'est identifiée : l'enquête reste limitée aux communes de l'extension, sans formalité de confirmation dans les autres communes." + no_global,
    benefit="Le bénéfice de l'enquête circonscrite aux seules communes intéressées par l'extension reste ouvert aux extensions futures, sans réserve aux situations antérieures. La participation du public directement concerné est conservée.")

proposal = paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur du décret portant la présente réforme. Les décrets prévus à l'article L. 113-19 ne sont plus soumis à l'obligation d'un rapport conjoint des ministres chargés de l'agriculture, de l'urbanisme et de l'environnement sur le seul fondement du présent article.",
    "La présente abrogation s'applique aux décrets pris à compter de cette entrée en vigueur, y compris lorsque leur préparation est en cours. Les actes préparatoires régulièrement accomplis restent utilisables sans recommencement. Elle ne dispense ni du décret exigé par l'article L. 113-19, ni de ses conditions de fond, accords, avis et procédures applicables, ni des règles de signature et de contreseing ayant un fondement distinct. Les décrets pris antérieurement et les voies de recours demeurent régis par les règles qui leur sont applicables ; aucun délai expiré n'est rouvert.")
add('R113-24', proposal,
    "Abrogation de fond de l'obligation réglementaire de présenter le décret de retrait de terrains sur rapport conjoint de trois ministres. La source prescrit un rapport des trois ministres, non trois documents distincts. Le niveau de décision exigé par L113-19 reste celui du décret ; les accords et garanties de la modification ne sont pas retirés. Ce préalable de présentation ne démontre pas une fonction protectrice supplémentaire par rapport à cette décision et aux règles de contreseing constitutionnelles, lesquelles ne sont pas abolies par un règlement.",
    "L113-19 lu intégralement : les modifications par déclaration d'utilité publique ou déclaration de projet d'infrastructure avec leurs conditions sont distinctes des autres retraits nécessitant décret. L'article R113-24 ne contient aucun tableau ni avantage fiscal et ne fixe aucune consultation publique autonome. L'abrogation porte uniquement sur son rapport de présentation conjoint ; ne pas en tirer suppression du décret ni des signatures et contreseings nécessaires sur un fondement supérieur. Les règles hors des cinq codes concernant l'élaboration des décrets ne sont pas présentées comme réécrites.",
    "La seule obligation de l'article officiel, une présentation par trois ministres, est supprimée pour les nouveaux décrets ; le pouvoir législatif de retrait et ses garanties demeurent.",
    "Le décret, les accords légaux et les contreseings autonomes restent requis. Aucun délai total de retrait ni coût ministériel économisé n'est démontré.",
    "Aucune charge nouvelle n'est identifiée : aucun rapport de remplacement, déclaration ni autorisation supplémentaire n'est créé pour remplacer le rapport conjoint supprimé." + no_global,
    [effect('obligation_removed', 'urbanisme-retrait-perimetre-fin-rapport-interministeriel',
        "Suppression du préalable d'un rapport conjoint de trois ministres prévu exclusivement par R113-24.",
        "Décret de L113-19 pris sur rapport des ministres de l'agriculture, de l'urbanisme et de l'environnement.",
        "Pas de rapport imposé par R113-24 ; décret et exigences autonomes conservés.",
        'legal_duty', "Services préparant les décrets de retrait de terrains d'un périmètre périurbain.",
        "Décrets pris après entrée en vigueur, y compris préparation en cours ; actes antérieurs et recours préservés.",
        "Aucun rapport de remplacement ; signatures et contreseings de fondement distinct restent.",
        "Le décret prévu à l'article L. 113-19 est pris sur le rapport des ministres chargés de l'agriculture, de l'urbanisme et de l'environnement.",
        "Les décrets prévus à l'article L. 113-19 ne sont plus soumis à l'obligation d'un rapport conjoint des ministres chargés de l'agriculture, de l'urbanisme et de l'environnement sur le seul fondement du présent article.")],
    repeal_scope="Suppression pour les nouveaux décrets de retrait de terrains du périmètre périurbain de l'obligation de présentation sur rapport conjoint des trois ministres désignés par R113-24 ; maintien du décret et des exigences autonomes.",
    benefit="Aucun avantage fiscal ou social ne figure dans la source. La faculté légale de retirer des terrains, notamment par les voies particulières liées aux infrastructures de transport, demeure ouverte pour les décisions futures sous les conditions de L113-19.")

add('R113-25', None,
    "Maintien intégral des accords locaux et consultations techniques du programme d'action, distincts des deux avis de création du périmètre supprimés à R113-20. La chambre d'agriculture, l'ONF pour les seules parcelles soumises au régime forestier et l'organe de parc dans son seul territoire contribuent aux orientations concrètes d'usage et de gestion ; ce ne sont pas des copies de l'avis sur le tracé. Le silence favorable à deux mois évite un blocage.",
    "L113-21, L113-22 et L113-23 lus : ils imposent les accords et consultations du programme ; l'avis de l'agence des espaces verts prévu à L113-21 n'est pas supprimé du seul fait qu'il n'est pas répété dans R113-25. Préserver les deux mois, le champ conditionnel ONF/parcs et les deux branches commune/EPCI. La faculté de préparer le programme alors que le périmètre est encore projeté demeure. Le règlement décrit le portage départemental ; L113-21 admet aussi L143-16 : harmonisation réglementaire de compétence à effectuer sans retirer cette faculté légale. Aucun tableau ou prélèvement contenu dans la source.",
    "Les consultations portent sur le contenu opératoire de gestion des terrains et gardent leur fondement législatif propre. Aucun nouveau gain n'est attribué au maintien du silence favorable déjà existant.",
    "La dispense des avis de création ne couvre pas le programme d'action. Le portage par l'établissement public admis par L113-21 nécessite une harmonisation réglementaire distincte.",
    "Aucune charge nouvelle n'est identifiée : maintien exact des accords, avis ciblés et silence favorable à deux mois, sans élargissement géographique ni nouvelle pièce." + no_global,
    benefit="L'avis favorable implicite à deux mois et la préparation du programme avant approbation du périmètre restent disponibles pour les projets futurs. Les consultations ONF et parcs ne deviennent pas générales hors de leurs conditions actuelles.")

proposal = paragraphs(
    "Le programme d'action est adopté par une délibération du conseil départemental.",
    "Les modalités de publicité prévues au deuxième alinéa de l'article R. 113-22 sont applicables à cette délibération. Aucune mention dans un journal n'est exigée à ce titre ; les publications, affichages et indications des lieux de consultation prévus par cet alinéa demeurent applicables.",
    "La présente rédaction s'applique aux délibérations d'adoption du programme prises à compter de l'entrée en vigueur du décret portant la présente réforme. Les délibérations antérieures conservent leur régime de publicité et de prise d'effet.")
add('R113-26', proposal,
    "Coordination de la publicité du programme avec le deuxième alinéa de R113-22 réécrit dans ce lot : l'annonce de presse supprimée ne revient pas par le renvoi. Délibération, publication officielle, affichages et lieux de consultation sont conservés. Le troisième alinéa de R113-22 n'était pas visé : ne pas compter une seconde suppression de ses copies spécialisées.",
    "Contrôle de la position du deuxième alinéa de R113-22 : elle est conservée dans la proposition. L'alinéa initial d'adoption reste à son emplacement ; précision de publicité ajoutée au deuxième et transition à la fin. Aucun délai d'affichage d'un mois retiré, aucune transmission du troisième alinéa de R113-22 ajoutée au programme. La limite de portage départemental de ce règlement par rapport à L113-21 reste signalée ; le pouvoir légal de l'établissement L143-16 n'est pas supprimé. Note de 2020 de R113-22 non transposée en date de réforme.",
    "L'effet sur le programme procède du renvoi déjà existant à R113-22 ; la proposition sécurise cette coordination sans compter une mesure matérielle supplémentaire.",
    "La modification n'efface pas les publicités utiles ni les règles propres aux programmes anciens. Aucune seconde obligation de copies n'était contenue dans le renvoi source.",
    "Aucune charge nouvelle n'est identifiée : mêmes affichages et accès au dossier, sans nouvelle diffusion ni transmission individuelle à des destinataires supplémentaires." + no_global,
    [effect('coordination', 'urbanisme-publicite-fonciere-sans-presse',
        "Application au programme de la suppression de presse opérée dans le renvoi de R113-22.",
        "Renvoi au deuxième alinéa de R113-22 comprenant une mention de presse.",
        "Renvoi au même alinéa allégé ; absence de mention de presse expressément confirmée.",
        'legal_duty', "Département adoptant le programme d'action d'un périmètre périurbain.",
        "Délibérations nouvelles ; régime de publicité et d'effet des anciennes préservé.",
        "Pas de publicité de remplacement, ni extension du renvoi aux copies professionnelles du troisième alinéa.",
        "Les modalités de publicité prévues au deuxième alinéa de l'article R. 113-22 sont applicables à cette délibération.",
        "Aucune mention dans un journal n'est exigée à ce titre ; les publications, affichages et indications des lieux de consultation prévus par cet alinéa demeurent applicables.")],
    impact_class='coordination_only',
    benefit="L'accès public au programme adopté, les accords locaux et les consultations ciblées restent entiers. La suppression de presse profite aussi aux futurs programmes sans limiter leur élaboration anticipée autorisée par R113-25.")

add('R113-27', None,
    "Maintien intégral de l'appel de candidatures et de l'avis affiché au moins quinze jours pour attribuer un bien acquis dans un périmètre protégé. L'avis donne à chacun les mêmes informations sur le bien, les charges, le prix, la date limite et les renseignements disponibles. Ce délai et ces données assurent une possibilité réelle de candidature et protègent l'attribution des biens publics ; les supprimer ne serait pas retirer un simple doublon.",
    "L113-24 à L113-28 et R113-28/29 lus. Ne pas confondre les quinze jours de publicité foncière avec le préavis individuel du travail. La cession de gré à gré permise par L113-28 n'exonère pas de l'information égale des candidats. Aucun registre ni pièce personnelle n'est exigé ici. Les prix et clauses restent ceux annoncés ; aucun tarif fiscal ni autorisation des candidats n'est instauré. Le délai source est un minimum d'affichage de l'avis, pas un délai de quinze jours ajouté à chaque candidature.",
    "L'article ne prévoit qu'un mécanisme ciblé de transparence des attributions et son contenu indispensable. Aucun support en double ni prélèvement n'y est identifié.",
    "Aucune réduction du minimum de quinze jours ou de la transparence des prix n'est proposée. Le régime de sélection et les règles autonomes des contrats restent hors de ce maintien.",
    "Aucune charge nouvelle n'est identifiée : maintien de l'avis unique avec ses données et du minimum existant, sans nouvelle pièce justificative ni enquête sur les candidats." + no_global,
    benefit="La faculté d'acquérir, louer ou recevoir une concession du bien demeure ouverte à tous les futurs candidats selon les règles applicables. La possibilité de connaître le cahier des charges et le prix protège aussi les candidats non retenus.")

add('R113-28', None,
    "Maintien intégral de la faculté conventionnelle de mise à disposition à la SAFER. Elle permet de gérer le foncier sans cession supplémentaire et impose seulement le maintien ou le rétablissement agricole, le respect environnemental et le cahier des charges légal. Ce contenu protège l'affectation des terrains acquis avec des moyens publics ; il n'impose ni agrément distinct ni déclaration périodique.",
    "L113-24 à L113-28 lus. Le renvoi R113-29 reste cohérent avec ses clauses types réécrites dans ce lot : la suppression de l'accord préalable de revente figurant dans la partie A ne supprime pas les obligations agricoles et environnementales de la mise à disposition. L142-6 du code rural est hors du corpus autorisé fourni : sa convention et ses règles autonomes ne sont pas présentées comme abrogées ni intégralement vérifiées. Ne pas transformer la simple faculté en obligation de passer par une SAFER.",
    "La disposition source ouvre une voie volontaire de gestion foncière et protège sa destination ; elle ne crée pas de prélèvement ou circuit d'autorisation à retirer dans cet article.",
    "Les règles rurales de la convention et les obligations du propriétaire restent à leur champ. Le maintien ne chiffre aucune économie ni ne modifie les contrats existants.",
    "Aucune charge nouvelle n'est identifiée : la convention reste facultative et ses deux objectifs existants sont conservés, sans registre, visa ou justificatif supplémentaire." + no_global,
    benefit="La mise à disposition conventionnelle demeure possible pour les terrains futurs éligibles comme pour les terrains déjà acquis. La souplesse de cette voie n'est pas fermée par la réforme des clauses types de R113-29.")

# L'annexe entière reste reproduite, seule la clause d'accord préalable change.
n = 'R113-29'
old = "A s'engage à ne pas procéder à la cession, la location ou la concession temporaire du terrain sans avoir obtenu l'accord du département. Le silence gardé par le département pendant deux mois à compter de la demande vaut accord."
new = "La cession, la location ou la concession temporaire du terrain n'est subordonnée à aucun accord préalable du département au titre du présent cahier des charges. Elle ne modifie pas les fins d'utilisation prescrites par ce cahier des charges."
proposal = replace_once(by_number[n]['source_xml'], old, new)
proposal += '\n' + paragraphs(
    "Les clauses types dans leur présente rédaction sont applicables aux cahiers des charges annexés aux actes conclus à compter de l'entrée en vigueur du décret portant la présente réforme, y compris lorsque leur préparation est en cours. Les contrats et cahiers des charges valablement conclus avant cette date, les droits acquis, les créances et les voies de recours qui en résultent restent régis par les dispositions et stipulations qui leur sont applicables. Aucun agrément, déclaration, information préalable ou justificatif de remplacement ne peut être exigé sur le seul fondement de la clause d'accord préalable supprimée pour les actes relevant de la présente rédaction. Les droits du propriétaire public lorsqu'il demeure propriétaire et les autorisations ayant un fondement distinct sont préservés.")
add(n, proposal,
    "Réduction de fond de la partie A : retrait de l'accord du département avant une nouvelle cession, location ou concession temporaire du terrain déjà cédé. La destination imposée par le programme, le cahier des charges transmis à l'acquéreur et le recours judiciaire en résolution suffisent à protéger l'usage ; le visa préalable ajoute un contrôle systématique sans fonction autonome démontrée. L'annexe entière, parties A et B, et tous ses modèles et alternatives sont conservés, sauf cette clause expressément remplacée.",
    "Comparaison complète de l'annexe, y compris l'alternative espace naturel sensible, les engagements à compléter et les recours judiciaires des deux parties. Aucun tableau n'y figure. Conserver exactement la présentation de la source et son emploi de « société d'aménagement foncier et de développement rural » dans B, discordant avec la dénomination de R113-28 : incohérence source signalée, non corrigée en silence. L113-27/28 conservent les fins d'utilisation et les modes de résolution. Le propriétaire public conserve ses droits lorsqu'il n'a pas cédé le bien. La réforme concerne les nouveaux cahiers ; elle ne réécrit pas les contrats anciens, qui peuvent garder l'accord et le silence favorable à deux mois. Aucun nouvel accord ni déclaration de transfert ne remplace le visa retiré.",
    "La source officielle complète imposait un accord départemental à la revente, location ou concession dans la clause A. Ce visa et l'attente de deux mois sont retirés dans les nouveaux cahiers ; la destination et la sanction contractuelle demeurent.",
    "Les cahiers anciens ne sont pas libérés de leurs stipulations par cette réforme. Les autres autorisations et les droits du propriétaire qui n'a pas cédé restent ; le gain de coût n'est pas chiffré.",
    "Aucune charge nouvelle n'est identifiée : aucun préavis, déclaration ou preuve de conformité nouvelle ne remplace l'accord. L'obligation d'usage et l'information de l'acquéreur étaient déjà présentes." + no_global,
    [effect('authorization_removed', 'urbanisme-cession-periurbaine-sans-accord-departemental',
        "Suppression du visa départemental des transferts ultérieurs dans les nouvelles clauses de cession.",
        "Acquéreur du terrain : accord départemental avant cession, location ou concession ; silence favorable au terme de deux mois après demande.",
        "Même acquéreur sous nouveau cahier : aucun accord ni demande sur ce fondement ; fins d'utilisation et transmission des obligations conservées.",
        'legal_duty', "Acquéreurs de terrains publics périurbains sous la partie A des nouveaux cahiers des charges.",
        "Cahiers annexés aux actes conclus après entrée en vigueur réglementaire ; contrats anciens et droits acquis préservés.",
        "Pas de déclaration ni visa de remplacement ; les autres autorisations et droits réels restent autonomes.",
        old, new)],
    removed=["Accord préalable du département avant cession, location ou concession du terrain dans la clause type A, avec demande et délai de deux mois de silence valant accord."],
    benefit="La suppression du visa englobe sa condition et son délai : le silence favorable de deux mois ne disparaît donc pas pendant que l'accord subsisterait pour les nouveaux actes. Il demeure pour les contrats anciens selon leur régime. Les possibilités de cession, location, concession ou mise à disposition, et les alternatives concernant les espaces naturels sensibles, restent ouvertes aux futures opérations éligibles.")

add('R114-1', None,
    "Maintien intégral du champ des études de sécurité publique, ciblé sur les grands projets, établissements très fréquentés, établissements scolaires, gares et opérations de rénovation à incidence particulière. Leur fonction est la protection contre les menaces et agressions, expressément essentielle selon l'orientation de réforme. Les règles incendie ou environnementales n'analysent pas à elles seules ces risques ; aucun doublon démontré ne justifie d'effacer ce champ.",
    "Tous les seuils et branches ont été relus : agglomération de plus de 100 000 habitants ; aménagement supérieur à 70 000 m² au 1° a ; construction supérieure ou égale à 70 000 m² au 1° c ; augmentation de plus de 10 % ou modification des accès, catégories d'ERP et établissements d'enseignement, gares ferroviaires/routières/maritimes, secteurs préfectoraux motivés et démolition d'au moins 500 logements. L114-1/2/4, R114-2/3, R311-5-1, R311-6, R424-5-1 et R431-16 lus ; les renvois à l'étude restent utiles après le seul retrait de l'examen systématique vidéo à R114-2. R143-19 du CCH est vérifié dans le corpus pour ses catégories. Le décret ANRU de 2004 et les règles de commissions hors des cinq codes restent à leur champ, sans prétendre les réécrire.",
    "Le champ entier est conservé après examen des catégories et seuils ; aucune suppression de taxe, d'étude de sécurité ou de catégorie n'est revendiquée.",
    "La nécessité propre à chaque projet et l'efficacité empirique de ces seuils ne sont pas quantifiées. Aucune extension de champ ni purge des textes de sécurité hors corpus n'est affirmée.",
    "Aucune charge nouvelle n'est identifiée : les quatre branches et leurs seuils sont intégralement conservés ; aucun nouveau type d'étude, registre ou autorisation n'est créé." + no_global,
    benefit="Les limitations de champ constituent des dispenses pour les opérations qui n'atteignent pas les critères. Elles demeurent pour les opérations futures, notamment la distinction strictement supérieur/supérieur ou égal à 70 000 m² et la limitation des travaux sur ERP existants.")

n = 'R114-2'
old = "L'étude se prononce sur l'opportunité d'installer ou non un système de vidéoprotection.<br />"
new = "L'examen d'un système de vidéoprotection n'est pas obligatoire en tant que tel. Un tel système peut être proposé lorsque l'analyse des risques de sécurité publique et les mesures de prévention le justifient, sans dispense des règles propres à son autorisation et à la protection des données.<br />"
proposal = replace_once(by_number[n]['source_xml'], old, new)
proposal += '\n' + paragraphs(
    "La suppression de l'examen systématique de cette technique s'applique aux études remises à compter de l'entrée en vigueur du décret portant la présente réforme, y compris pour les demandes en cours. Aucune étude déjà remise n'est à refaire du seul fait de cette suppression ; les autres conditions de contenu et de réutilisation prévues au présent article demeurent applicables.")
add(n, proposal,
    "Réduction de fond ciblée : suppression de l'examen obligatoire d'une technologie déterminée, la vidéoprotection, dans chaque étude même lorsque les risques identifiés ne le justifient pas. L'analyse complète des risques et les mesures pour les prévenir et faciliter les secours restent exigées dans toutes leurs composantes. Le choix de cette technique demeure possible mais n'est plus un passage obligé de rédaction. Les assouplissements propres aux ERP existants sont maintenus mot pour mot.",
    "Source relue entièrement : 1° diagnostic social et urbain, 2° risques, 3° ensemble des caractéristiques et mesures, a/b, diagnostic limité aux interactions pour les travaux sur ERP existants, étude de moins de quatre ans jointe et nouvelle étude limitée aux modifications de plus de 10 % ou aux accès, tous conservés. L114-1 à L114-4, R114-1/3, R424-5-1 et R431-16 i lus : leurs renvois continuent à viser le contenu utile. Le texte n'autorise aucun dispositif vidéo ni nouveau traitement de données ; les autorisations et protections légales autonomes demeurent. Aucun chiffre, seuil ou faveur de réemploi modifié. Le gain porte seulement sur la question technologique systématique, pas sur toute l'étude.",
    "Une obligation d'analyse technologique systématique disparaît de la source entière. Le diagnostic, l'analyse des menaces et les mesures de prévention restent ; il ne s'agit pas d'une suppression de l'étude de sécurité.",
    "Les projets présentant un besoin réel peuvent toujours proposer la vidéo ; aucune économie nationale ni diminution de fréquence des études n'est démontrée. Les règles de protection des données restent autonomes.",
    "Aucune charge nouvelle n'est identifiée : aucune justification de non-recours à la vidéo, attestation ou avis de remplacement n'est exigé ; l'analyse des risques était déjà obligatoire." + no_global,
    [effect('obligation_removed', 'etude-securite-fin-examen-video-systematique',
        "Retrait de l'obligation de traiter systématiquement l'opportunité d'une vidéoprotection.",
        "Toute étude doit se prononcer sur l'installation ou la non-installation d'un système vidéo, indépendamment des risques diagnostiqués.",
        "Pas d'examen de la vidéo obligatoire en tant que tel ; possibilité de la proposer selon les risques, avec toutes ses règles propres.",
        'legal_duty', "Maîtres d'ouvrage et auteurs des études relevant de R114-1.",
        "Études remises après entrée en vigueur, dossiers en cours inclus ; aucune réfection des études déjà remises sur ce seul motif.",
        "Aucun document de remplacement ; diagnostic, prévention et facilitation des secours restent requis.",
        "L'étude se prononce sur l'opportunité d'installer ou non un système de vidéoprotection.",
        "L'examen d'un système de vidéoprotection n'est pas obligatoire en tant que tel.")],
    removed=["Examen obligatoire, dans toute étude de sécurité publique, de l'opportunité d'installer ou non un système de vidéoprotection indépendamment du diagnostic de risques."],
    benefit="Les deux allègements existants pour les ERP restent intacts et ouverts aux futurs projets : diagnostic limité à l'interaction pour les travaux concernés et réemploi de l'étude de moins de quatre ans, avec nouvelle analyse limitée aux modifications visées. Aucun passage à un nouveau seuil de 10 % ni perte du droit de réemploi n'est créé.")

add('R114-3', None,
    "Maintien intégral du silence valant avis favorable au terme de deux mois. Ce plafond évite que l'expertise de la commission de sécurité bloque indéfiniment la décision, sans supprimer l'examen des menaces et agressions nécessaire aux ERP. Il ne commande pas d'attendre deux mois si l'avis intervient plus tôt et ne constitue pas un agrément distinct à réformer.",
    "L114-2/4 et R114-1/2 lus. L'avis favorable implicite porte sur la commission et non sur le permis lui-même ; les pouvoirs de décision et le contenu nécessaire de l'étude subsistent. Le retrait de la question vidéo obligatoire dans R114-2 n'exige pas de changer ce renvoi. Ne pas confondre les deux mois de cet avis avec un délai de contrôle social, un préavis de travail ou la caducité foncière.",
    "La source est déjà une garantie de calendrier favorable. Aucun changement du maximum de deux mois ou de la portée de l'avis n'est proposé ni compté comme gain nouveau.",
    "Le délai global du permis et les contrôles distincts ne sont pas modifiés ; le maintien ne garantit pas une autorisation dans les deux mois.",
    "Aucune charge nouvelle n'est identifiée : maintien entier du silence favorable et de son délai, sans attestation ni preuve supplémentaire à demander au pétitionnaire." + no_global,
    benefit="Le bénéfice du silence favorable de la commission demeure pour toutes les opérations futures relevant de L114-2. Il ne devient ni refus implicite ni condition de production d'un certificat administratif.")

proposal = paragraphs(
    "La délibération du conseil municipal décidant de délimiter une ou plusieurs zones de protection dans lesquelles peut s'exercer le pouvoir d'opposition aux divisions foncières prévu à l'article L. 115-3 est affichée en mairie pendant un mois et tenue à la disposition du public à la mairie. Aucune mention dans un journal régional ou local n'est exigée au titre du présent article.",
    "La délibération du conseil municipal prend effet à compter de l'accomplissement des formalités de publicité définies à l'alinéa précédent. Pour l'application du présent alinéa, la date à prendre en considération pour l'affichage en mairie est celle du premier jour où il est effectué.",
    "Aucune copie individuelle de cette délibération au Conseil supérieur du notariat, à la chambre départementale des notaires, aux barreaux ou aux greffes des tribunaux judiciaires n'est exigée au seul titre du présent article. Les transmissions ayant un fondement distinct demeurent applicables. La délibération ne rétablit aucune déclaration, demande d'autorisation, information préalable ou attestation de non-opposition supprimée par l'article L. 115-3.",
    "La présente rédaction s'applique aux délibérations prises à compter de l'entrée en vigueur du décret portant la présente réforme. Les zones régulièrement délimitées et rendues publiques avant cette date conservent leur existence dans les conditions de l'article L. 115-3, sans nouvelle délibération ni nouvelle publicité. Les délibérations antérieures restent soumises à leurs règles de publicité et de prise d'effet. Les actes, oppositions, droits acquis et recours antérieurs restent régis par la transition de cet article, sans réouverture d'un délai expiré.")
add('R115-1', proposal,
    "Réduction de fond : retrait de l'annonce en presse et des copies aux instances notariales, barreaux et greffes, tout en conservant l'affichage d'un mois et le dossier public en mairie. Coordination avec L115-3 proposé : le zonage sert au pouvoir ciblé d'opposition et ne soumet plus toute division à un dossier préalable. Cette dernière suppression relève de la loi et n'est pas comptée une deuxième fois comme nouvelle mesure réglementaire.",
    "Source et note 2019-966 lues : le 1er janvier 2020 est historique, sans date future de promulgation inventée. L115-3 source et proposition lus entièrement, avec ses trois dispenses, cinq ans de prescription, oppositions déjà notifiées et anciens actes. Le règlement ne supprime pas le zonage ni l'information des propriétaires ; la date du premier jour d'affichage reste entière. R151-52 4° et R*421-23 b, hors lot, doivent être coordonnés au zonage sans dossier obligatoire ; ne pas confondre avec les vrais lotissements du a et leurs autorisations autonomes. Le contrôle spécial utilise seulement les informations légalement disponibles, sans obligation nouvelle de les fournir. Les délais et les effets de recours liés à l'ancienne publicité restent préservés, aucun ancien affichage défectueux n'étant validé.",
    "La source entière imposait presse, affichage, dossier et copies spécialisées. Presse et copies disparaissent pour les nouvelles délibérations ; le renvoi au dossier préalable supprimé est corrigé sans nouveau formulaire.",
    "Les règles autonomes des lotissements, travaux et protections environnementales ne disparaissent pas. Les autres règlements de zonage restent à coordonner ; aucun gain global de délai ou de finances n'est chiffré.",
    "Aucune charge nouvelle n'est identifiée : affichage et accès en mairie existaient déjà. Aucun certificat, renseignement préalable ou registre ne remplace la déclaration supprimée au niveau législatif." + no_global,
    [effect('obligation_removed', 'urbanisme-publicite-fonciere-sans-presse',
        "Suppression de la mention de presse des nouvelles zones de protection des divisions.",
        "Affichage d'un mois et dossier en mairie plus mention dans un journal régional ou local.",
        "Affichage d'un mois et dossier maintenus, sans annonce de presse.",
        'legal_duty', "Communes délimitant de nouvelles zones au titre de L115-3.",
        "Délibérations nouvelles ; anciennes zones régulièrement publiées conservées sans republication.",
        "Pas de nouvelle publicité ; les formalités autonomes et recours restent.",
        "Mention en est publiée dans un journal régional ou local diffusé dans le département.",
        "Aucune mention dans un journal régional ou local n'est exigée au titre du présent article."),
     effect('obligation_removed', 'urbanisme-zonages-fin-copies-professionnelles',
        "Retrait des copies spécialisées de la délibération communale déjà rendue publique.",
        "Copies sans délai aux deux échelons notariaux, aux barreaux et aux greffes concernés.",
        "Aucune copie individuelle sur ce fondement ; dossier public et transmissions autonomes maintenus.",
        'legal_duty', "Communes et destinataires professionnels ou judiciaires des zones de L115-3.",
        "Délibérations nouvelles ; anciennes règles de publicité et prise d'effet préservées.",
        "Pas d'envoi ou registre de remplacement, ni nouvel accès à des données protégées.",
        "Copie en est adressée sans délai, à l'initiative de son auteur, au Conseil supérieur du notariat, à la chambre départementale des notaires, aux barreaux constitués près les   tribunaux judiciaires dans le ressort desquels sont situées la ou les zones concernées et au greffe des mêmes tribunaux.",
        "Aucune copie individuelle de cette délibération au Conseil supérieur du notariat, à la chambre départementale des notaires, aux barreaux ou aux greffes des tribunaux judiciaires n'est exigée au seul titre du présent article."),
     effect('coordination', 'urbanisme-divisions-foncieres-sans-declaration-speciale',
        "Suppression de la description réglementaire du zonage comme instituant un dossier préalable obligatoire.",
        "Zones dans lesquelles les divisions foncières sont subordonnées à déclaration préalable.",
        "Zones de protection conservées pour l'opposition légale, sans rétablir un dossier, une information préalable ou une attestation.",
        'regime', "Parties aux divisions foncières relevant du pouvoir spécial de L115-3.",
        "Application de la transition législative aux ventes et locations nouvelles, zones anciennes et droits acquis préservés.",
        "Aucune formalité préalable de remplacement ; autorisations des autres fondements distinctes.",
        "les divisions foncières sont subordonnées à déclaration préalable",
        "La délibération ne rétablit aucune déclaration, demande d'autorisation, information préalable ou attestation de non-opposition supprimée par l'article L. 115-3.")],
    removed=["Mention de la délibération de zonage dans un journal régional ou local, en supplément de l'affichage et du dossier public en mairie.",
             "Copies individuelles obligatoires de la délibération aux organisations notariales, barreaux et greffes des tribunaux concernés.",
             "Qualification des zones comme rétablissant une déclaration préalable de division, incompatible avec la dispense législative de L115-3."],
    benefit="Les trois dispenses législatives des opérations d'aménagement autorisées, de l'aménagement foncier rural avant clôture et des baux ruraux professionnels restent ouvertes pour l'avenir. Les non-oppositions et droits acquis antérieurs sont protégés selon L115-3 ; les zones anciennes restent utilisables sans nouvelles démarches et n'imposent pas de déclaration générale.")

add('R121-1', None,
    "Maintien intégral de l'autorité compétente pour la dérogation littorale des stations d'épuration non liées à une urbanisation nouvelle. Une autorisation conjointe identifie les responsables de l'urbanisme et de l'environnement dans une seule décision ; la supprimer sans fondement substitutif fermerait la dérogation ou effacerait ses conditions protectrices. Aucun second agrément, avis ou déclaration n'est institué ici.",
    "L121-5 lu en entier, source et proposition du corpus : exception pour les seules stations d'épuration d'eaux usées sans urbanisation nouvelle, non un pouvoir général de construire sur le littoral. Le renvoi et les deux portefeuilles ministériels restent cohérents. Aucun taux, délai minimal ou pièce justificative dans cet article. Le maintien ne modifie ni les schémas de plage de L121-28 à L121-30 ni leurs procédures et exemptions ; aucune fermeture de dérogation future.",
    "Le texte officiel rend opératoire une dérogation favorable par une décision ministérielle conjointe. Aucun doublon de dépôt ni prélèvement ne peut être retiré de ce seul article.",
    "Les conditions environnementales et autres titres de l'installation restent à leur champ ; le maintien ne démontre ni délai total d'autorisation ni conformité européenne exhaustive.",
    "Aucune charge nouvelle n'est identifiée : maintien exact d'une seule autorisation conjointe, sans nouvelle déclaration, procédure locale ou justificatif." + no_global,
    benefit="La dérogation aux règles littorales pour les stations d'épuration de L121-5 est conservée pour toutes les opérations futures qui en remplissent les conditions, sans limitation aux droits acquis et sans retrait implicite de ses autorités de décision.")

add('R*121-1-1', None,
    "Maintien intégral du régime de silence pour l'autorisation exceptionnelle des ouvrages du réseau public de transport d'électricité sur le littoral. La décision doit apprécier le bilan technique, financier et environnemental, les variantes d'enfouissement et, dans les secteurs les plus sensibles, la nécessité technique impérative et l'absence d'atteinte excessive. Un accord automatique sans appréciation de ces conditions pourrait effacer des protections essentielles ; la dérogation expresse reste entièrement ouverte.",
    "L121-5-2 lu en entier, source et proposition : objectifs énergétiques énumérés, exclusion des zones de recul L121-22-2, avis local dans un mois et avis CDNPS, bilan à trois composantes, principe d'enfouissement et trois motifs de dérogation, régime particulier bande littorale/espaces remarquables/milieux, refus pour atteinte excessive, tous restent à leur champ. Le règlement porte seulement sur le silence des deux ministres : pas de nouveau veto, délai ou certificat. Le choix de maintenir le refus tacite ne ferme pas l'autorisation expresse future ni ses recours. Les dispositions énergétiques et environnementales hors corpus ne sont pas prétendues entièrement coordonnées.",
    "La source ne comporte qu'une règle de décision implicite sur une dérogation sensible ; elle est maintenue pour permettre le contrôle effectif des conditions légales sans retirer l'accès à la dérogation.",
    "Aucun passage général au silence favorable ou délai de traitement réduit n'est proposé. Les obligations supérieures et autorisations autonomes ne sont pas examinées exhaustivement dans ce lot.",
    "Aucune charge nouvelle n'est identifiée : le refus implicite existant est maintenu, sans nouvelle demande, attestation, donnée ou condition pour l'autorisation expresse." + no_global,
    benefit="Les ouvrages futurs remplissant L121-5-2 gardent accès à l'autorisation littorale dérogatoire et à ses exceptions d'enfouissement ; aucune limitation aux seuls projets antérieurs n'est introduite. Le schéma de plage et les autres dérogations littorales favorables ne sont pas concernés par cette règle de silence.")


class MarkupCheck(HTMLParser):
    allowed = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())

    def handle_starttag(self, tag, attrs):
        assert tag in self.allowed, tag
        for name, value in attrs:
            assert name in {'rowspan', 'colspan'} and value.isdigit(), (tag, name, value)

    handle_startendtag = handle_starttag


assert len(sources) == 24
assert set(answers) == set(by_number)
ordered = [answers[src['number']] for src in sources]
for src, obj in zip(sources, ordered):
    for key in ('code_id', 'source_id', 'source_sha256', 'number'):
        assert obj[key] == src[key]
    impact = obj['substantive_impact']
    for field in ('assessment', 'scope_limitations', 'new_burdens_review'):
        assert len(impact[field]) >= 40
    if src.get('benefit_check_required'):
        assert len(obj['benefit_review']) >= 100
    if obj['proposed_xml'] is None:
        assert obj['status'] == 'retained_unchanged'
        assert obj['classification'] == 'retained_necessary'
        assert impact['effects'] == []
    else:
        MarkupCheck().feed(obj['proposed_xml'])
        assert obj['proposed_xml'] != src['source_xml']
        for e in impact['effects']:
            assert len(e['source_quote']) >= 12 and e['source_quote'] in plain(src['source_xml']), (src['number'], 'source', e['source_quote'])
            assert len(e['proposed_quote']) >= 12 and e['proposed_quote'] in plain(obj['proposed_xml']), (src['number'], 'proposal', e['proposed_quote'])
            assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', e['measure_id']) and 6 <= len(e['measure_id']) <= 96
    if obj.get('change_type') == 'normative_reduction':
        assert all(len(s) >= 30 for s in obj['removed_provisions'])
    if obj.get('change_type') == 'full_repeal':
        assert plain(obj['proposed_xml']).startswith(('Le présent article est abrogé', 'Abrogé'))
        assert len(obj['repeal_scope']) >= 30

Path('answer.json').write_text(json.dumps(ordered, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'output_file': 'answer.json', 'article_count': len(ordered)}, ensure_ascii=False))
