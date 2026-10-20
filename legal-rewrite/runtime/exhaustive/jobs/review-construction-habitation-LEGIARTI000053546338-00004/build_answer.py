import json
import re
from pathlib import Path


sources = json.loads(Path('source.json').read_text())


def paragraphs(xml):
    return re.findall(r'<p>.*?</p>', xml, re.S)


def paragraph(text):
    return '<p>' + text + '</p>'


first, second = sources
p1 = paragraphs(first['source_xml'])
original_p1 = list(p1)
p1[1] = paragraph(
    "À compter de l'entrée en vigueur de la loi portant la présente rédaction, la participation des maires d'arrondissement de Paris, Marseille et Lyon ou de leurs représentants à l'élaboration du programme n'est plus obligatoire au titre du présent article. Les obligations de mise en place et de maintien des observatoires de l'habitat et du foncier, de recensement propre à ces observatoires et de compte rendu annuel prévues au III dans sa rédaction antérieure cessent à la même date, y compris pour les programmes en vigueur et les délais de mise en place non échus. Aucun compte rendu antérieur restant à établir n'est exigé après cette date sur ce seul fondement. Les programmes adoptés, les consultations déjà réalisées, les contrats valablement conclus, les aides et les engagements financiers valablement acquis, ainsi que les droits des occupants et des tiers, sont préservés. Les consultations et les protections disposant d'un fondement légal distinct demeurent applicables. Les objectifs définis par le présent article ne peuvent rétablir les quotas communaux, les objectifs de rattrapage, les prélèvements ou les effets de carence supprimés en matière de logements sociaux."
)
p1[4] = p1[4][:-4] + (
    " Pour les programmes dont l'élaboration est engagée après l'entrée en vigueur de la loi portant la présente rédaction, le diagnostic identifie, dans les espaces déjà urbanisés, les possibilités de création de logements par division, extension, surélévation ou transformation de bureaux et de locaux vacants. Il évalue ces possibilités au regard de la desserte effective par les transports collectifs, des capacités d'alimentation en eau, d'assainissement et des autres réseaux, des équipements scolaires, des risques et de la qualité du cadre de vie. Il prend en compte l'éclairement, les espaces de pleine terre, les continuités écologiques et les protections environnementales et patrimoniales. Il identifie les renforcements des réseaux et des équipements nécessaires ; leur calendrier prévisionnel et leur financement sont précisés dans le programme d'actions du IV. Ces exigences nouvelles n'imposent pas, à elles seules, la modification d'un programme en vigueur.</p>"
)
p1[5] = paragraph(
    "La mise en place et le maintien d'un observatoire de l'habitat et du foncier sont facultatifs. L'élaboration et le suivi du programme peuvent être assurés par les services existants ou par un dispositif mutualisé, sans création obligatoire d'une structure distincte."
)
inventory = re.search(r'1° Des friches constructibles ;.*?5°.*?continuités écologiques\.', original_p1[6], re.S).group()
p1[6] = paragraph(
    "Aucun délai de mise en place d'un observatoire ni recensement distinct propre à celui-ci n'est imposé au titre du présent III. Les observatoires, lorsqu'ils existent, et les services chargés du programme peuvent analyser la conjoncture des marchés foncier et immobilier ainsi que l'offre foncière disponible. Cette analyse peut notamment s'appuyer sur un recensement :<br /><br />\n"
    + inventory
    + "<br /><br />\nLorsqu'une telle analyse est réalisée, elle prend également en compte les inventaires des zones d'activité économique prévus à l'article L. 318-8-2 du même code.<br /><br />\n"
    "Les observatoires de l'habitat et du foncier ne sont pas tenus de rendre compte annuellement du nombre de logements construits sur des espaces déjà urbanisés et sur des zones ouvertes à l'urbanisation. Le suivi prévu à l'article L. 302-3 conserve son champ propre ; il ne requiert ni observatoire obligatoire, ni recensement ou rapport de remplacement au titre du présent III.<br /><br />\n"
    "Les communes ou les établissements publics de coopération intercommunale qui ne sont pas couverts par un plan local de l'habitat et qui sont dans l'incapacité de mettre en place un dispositif d'observation de l'habitat et du foncier peuvent conclure une convention avec l'établissement public de coopération intercommunale compétent en matière de plan local de l'habitat le plus proche, dans les conditions qu'ils déterminent.<br /><br />\n"
    "Un décret en Conseil d'Etat détermine les modalités d'application du présent III. Il ne peut imposer la création ou le maintien d'un observatoire, un délai de mise en place, un recensement propre à cet observatoire ou un compte rendu annuel supprimés par le présent III, ni les rétablir par un renvoi à cet observatoire."
)
p1[13] = p1[13].replace("définis au 1° du I de l'article L. 302-16", "définis à l'article L. 302-16")
p1[21] = paragraph(
    "-les moyens, notamment fonciers, à mettre en œuvre pour atteindre les objectifs et principes fixés. Pour les programmes dont l'élaboration est engagée après l'entrée en vigueur de la loi portant la présente rédaction, ces moyens comprennent les actions de division, d'extension, de surélévation et de transformation de bureaux et de locaux vacants retenues au regard du diagnostic du III, ainsi que les renforcements nécessaires des réseaux et des équipements. Le programme précise leur calendrier prévisionnel et leur financement lorsqu'il est arrêté et signale expressément les financements qui ne sont pas arrêtés. Ces actions sont coordonnées avec les dispositions du plan local d'urbanisme relatives à la densification ; elles ne valent pas autorisation et ne dérogent pas aux règles de sécurité, d'accessibilité, de salubrité, de protection de l'environnement ou du patrimoine, ni aux obligations de logement social disposant d'un fondement légal distinct des quotas communaux et objectifs de rattrapage abrogés. Ces exigences nouvelles n'imposent pas, à elles seules, la modification d'un programme en vigueur ;"
)
xml1 = '\n'.join(p1)

p2 = paragraphs(second['source_xml'])
original_p2 = list(p2)
p2[4] = p2[4].replace(' </p>', '</p>')[:-4] + (
    " Lorsque ce seuil est atteint ou dépassé, la modification est également possible à condition qu'il ne soit pas porté atteinte à l'économie générale du programme.</p>"
)
p2[5] = paragraph(
    "Le projet de modification n'est soumis à aucune transmission pour avis préalable au représentant de l'Etat dans le département ou aux personnes morales associées en application de l'article L. 302-2 au titre du présent I. Aucun accord, déclaration ou consultation de remplacement n'est exigé sur ce fondement. Le contrôle de légalité ainsi que les procédures d'évaluation environnementale et de participation du public applicables sur un fondement distinct demeurent."
)
p2[8] = paragraph(
    "II. - À compter de l'entrée en vigueur de la loi portant la présente rédaction, l'obligation de modifier le programme local de l'habitat dans un délai de deux ans pour y intégrer les quotas communaux et les objectifs de rattrapage de logements sociaux supprimés, ainsi que la procédure spéciale d'avis, de demandes préfectorales de modifications et de prise d'effet différée qui l'accompagnait, sont abrogées. Les procédures engagées sur ce seul fondement cessent à cette date. La réaffectation des prélèvements sanctionnant l'absence de cette modification est également supprimée pour l'avenir. Les dispositions transitoires du V de l'article L. 302-5 s'appliquent aux créances légalement nées de faits générateurs antérieurs, aux affectations légalement acquises, aux conventions, aux aides et aux droits des occupants, des cocontractants et des tiers ; aucune créance ni contribution de remplacement n'est créée.<br /><br />"
    "Le I dans sa présente rédaction s'applique aux projets de modification non encore approuvés à cette date, sans nouveau dépôt ni recommencement des étapes déjà accomplies. Les avis déjà recueillis restent utilisables ; aucun avis supplémentaire ni achèvement de la consultation supprimée n'est requis au titre du I. Les délibérations déjà approuvées ne sont pas remises en cause de ce seul fait."
)
xml2 = '\n'.join(p2)


def effect(kind, measure_id, description, before, after, unit, population, transition, burdens, source_quote, proposed_quote):
    return {
        'kind': kind,
        'measure_id': measure_id,
        'description': description,
        'before': before,
        'after': after,
        'unit': unit,
        'affected_population': population,
        'conditions_and_transition': transition,
        'replacement_or_new_burdens': burdens,
        'source_quote': source_quote,
        'proposed_quote': proposed_quote,
    }


effects1 = [
    effect(
        'obligation_removed', 'plh-participation-maires-arrondissement-suppression',
        "Suppression de l'association obligatoire spéciale des maires d'arrondissement, sans nouvelle saisine.",
        "Participation obligatoire des maires d'arrondissement de Paris, Marseille et Lyon ou de leurs représentants à l'élaboration du PLH.",
        "Cette participation cesse d'être obligatoire au titre de L302-1 ; les consultations légalement autonomes restent applicables.",
        'legal_duty', "Autorités élaborant le PLH de Paris, Marseille ou Lyon et maires d'arrondissement concernés.",
        "Entrée en vigueur de la loi portant la nouvelle rédaction, y compris élaboration en cours ; consultations réalisées et programmes adoptés préservés.",
        "Aucune déclaration, autorisation ni autre consultation n'est créée en remplacement.",
        "Pour les communes de Paris, Marseille et Lyon, les maires d'arrondissement ou leurs représentants participent à l'élaboration du programme local de l'habitat.",
        "la participation des maires d'arrondissement de Paris, Marseille et Lyon ou de leurs représentants à l'élaboration du programme n'est plus obligatoire au titre du présent article.",
    ),
    effect(
        'obligation_removed', 'plh-observation-fonciere-facultative',
        "Une seule mesure retire la définition obligatoire des modalités de l'observatoire dans le PLH, sa création sous trois ans, ses recensements propres et son compte rendu annuel des logements construits ; ces composantes ne sont pas décomptées comme plusieurs effets identiques.",
        "Le PLH doit définir la mise en place de l'observatoire, qui doit être créé au plus tard trois ans après le caractère exécutoire du programme ; analyse et recensement des cinq catégories foncières, avec compte rendu annuel des logements construits sur espaces urbanisés et zones ouvertes à l'urbanisation.",
        "Création et maintien facultatifs, sans délai de mise en place, recensement ni compte rendu annuel obligatoires propres à l'observatoire. Le diagnostic initial et les bilans autonomes de L302-3 restent obligatoires à leur champ propre.",
        'legal_duty', "EPCI et communes soumis au PLH, y compris lorsqu'un PLU en tient lieu ; services et observatoires de l'habitat et du foncier concernés.",
        "Suppression dès l'entrée en vigueur, y compris programmes en vigueur et délais non échus ; aucun rattrapage du compte rendu restant à établir sur ce seul fondement. Contrats, aides, engagements acquis et données déjà produites sont préservés.",
        "Aucun observatoire, recensement, compte rendu ou dépôt de remplacement ; diagnostic et suivi légal autonomes demeurent. Les exigences supplémentaires de densification, distinctes de cette suppression, sont recensées séparément ; leur coût net avec les coupes est inconnu.",
        "Les observatoires de l'habitat et du foncier sont mis en place au plus tard trois ans après que le programme local de l'habitat a été rendu exécutoire.",
        "La mise en place et le maintien d'un observatoire de l'habitat et du foncier sont facultatifs.",
    ),
    effect(
        'obligation_added', 'plh-diagnostic-densification-reseaux',
        "Maintien de la réforme de densification du précédent projet : exigences nouvelles de diagnostic et de programmation par rapport à la source officielle.",
        "Diagnostic des marchés, de l'offre et de la mutabilité foncière, avec capacité d'accueil des logements et repérage de l'habitat indigne ; pas de détail exprès des quatre transformations et de leur financement.",
        "Pour les nouvelles élaborations : étude des divisions, extensions, surélévations et transformations, desserte, réseaux, écoles, risques et cadre de vie ; renforcements, calendrier et financement dans le programme d'actions.",
        'legal_duty', "Collectivités engageant l'élaboration d'un nouveau PLH et services qui établissent son diagnostic et son programme d'actions.",
        "Élaborations engagées après l'entrée en vigueur de la loi ; aucune modification des programmes en vigueur exigée de ce seul fait.",
        "Charge d'analyse et de programmation supplémentaire, sans registre, périodicité nouvelle ni autorisation. Le calendrier et le financement ne sont décrits qu'au IV, auquel renvoie le III. Son coût et le solde net avec les suppressions ne sont pas établis.",
        "Le diagnostic comporte notamment une analyse des marchés fonciers, de l'offre foncière et de son utilisation, de la mutabilité des terrains et de leur capacité à accueillir des logements.",
        "le diagnostic identifie, dans les espaces déjà urbanisés, les possibilités de création de logements par division, extension, surélévation ou transformation de bureaux et de locaux vacants.",
    ),
    effect(
        'coordination', 'plh-definition-logements-intermediaires-renvoi',
        "Correction explicite d'un renvoi préexistant à un I absent de la cible locale L302-16, sans modification de sa définition ni de l'assimilation historique.",
        "Renvoi au 1° du I de L302-16, alors que la cible locale comporte une définition en trois conditions numérotées, sans I.",
        "Renvoi à L302-16 dans son ensemble ; les trois conditions de la définition restent ensemble applicables.",
        'other', "PLH décrivant l'offre de logements intermédiaires et logements auxquels cette définition ou l'assimilation historique s'applique.",
        "Nouvelle rédaction ; aucune fermeture des situations futures recevables ni modification de la date historique du 1er mars 2014.",
        "Aucune attestation, taxe ni condition supplémentaire ; concordance du corpus signalée sans prétendre à une mise à jour externe.",
        "Cette typologie peut également préciser l'offre de logements intermédiaires définis au 1° du I de l'article L. 302-16.",
        "Cette typologie peut également préciser l'offre de logements intermédiaires définis à l'article L. 302-16.",
    ),
]

effects2 = [
    effect(
        'obligation_removed', 'plh-modification-avis-prealables-suppression',
        "Suppression du circuit préalable d'avis sur les modifications ordinaires du PLH, sans procédure équivalente.",
        "Transmission du projet au préfet et aux personnes morales associées ; avis réputé donné à défaut de réponse dans les deux mois de la transmission.",
        "Aucune transmission pour avis ni consultation préalable imposée par le I ; approbation par l'organe délibérant, contrôle de légalité et procédures environnementales autonomes conservés.",
        'legal_duty', "EPCI modifiant leur PLH et communes entrant dans le champ de L302-4-1 ; préfet et personnes morales associées.",
        "Projets non encore approuvés à l'entrée en vigueur ; aucun nouveau dépôt ni attente de la fin des consultations supprimées ; avis déjà rendus utilisables.",
        "Aucun accord, déclaration ou consultation de remplacement. La transmission au contrôle de légalité n'est pas supprimée. Le gain de délai n'est pas uniformément de deux mois, les avis pouvant auparavant être rendus plus tôt.",
        "Le projet de modification est transmis pour avis au représentant de l'Etat dans le département ainsi qu'aux personnes morales associées en application de l'article L. 302-2.",
        "Le projet de modification n'est soumis à aucune transmission pour avis préalable au représentant de l'Etat dans le département ou aux personnes morales associées en application de l'article L. 302-2 au titre du présent I.",
    ),
    effect(
        'relief_extended', 'plh-extension-perimetre-modification-simplifiee',
        "Extension de la faculté de modification du PLH aux agrandissements de périmètre atteignant ou dépassant le cinquième de la population, si l'économie générale n'est pas atteinte.",
        "Faculté spéciale ouverte lorsque les communes ajoutées représentent moins du cinquième de la population totale après extension ; pas de cette faculté spéciale au seuil ou au-dessus.",
        "Voie existante sous le cinquième conservée sans condition ajoutée ; au seuil ou au-dessus, modification possible si l'économie générale du programme est préservée.",
        'regime', "EPCI dont le périmètre est étendu à une ou plusieurs communes et communes concernées par cette extension.",
        "Entrée en vigueur et projets non encore approuvés ; pas de modification automatique des PLH déjà adoptés ni des périmètres.",
        "La condition d'économie générale limite seulement la faculté nouvelle au seuil ou au-dessus ; aucun justificatif, autorisation ni condition supplémentaire sous le seuil existant.",
        "si les communes concernées représentent moins du cinquième de la population totale de l'établissement au terme de cette extension de périmètre.",
        "Lorsque ce seuil est atteint ou dépassé, la modification est également possible à condition qu'il ne soit pas porté atteinte à l'économie générale du programme.",
    ),
    effect(
        'coordination', 'sru-quotas-rattrapage-suppression',
        "Coordination du PLH avec la suppression déjà décidée des quotas et du rattrapage : retrait de la modification obligatoire, de sa procédure spéciale et de la réaffectation sanction. Ce n'est pas une nouvelle taxe supprimée.",
        "II : modification obligatoire sous deux ans, avis sous deux mois, demandes préfectorales, prise d'effet différée sous deux mois et réaffectation des prélèvements pour absence de modification.",
        "Aucune obligation ni procédure spéciale sur le fondement des quotas supprimés ; réaffectation sanction supprimée pour l'avenir ; transition commune de L302-5 V pour le stock antérieur.",
        'legal_duty', "EPCI dont les communes étaient soumises aux obligations de logements sociaux, bénéficiaires des anciennes affectations et communes prélevées.",
        "Entrée en vigueur de la loi et procédures en cours ; créances légalement nées de faits antérieurs, affectations acquises, contrats, aides et recours soumis à la transition commune, sans remboursement général.",
        "Aucune modification de remplacement, nouvel inventaire, prélèvement, contribution ou déclaration n'est créé. La suppression de L302-7 constitue la mesure fiscale coordonnée, sans double décompte ici.",
        "II.-Par dérogation au I du présent article, le programme local de l'habitat fait obligatoirement l'objet, dans un délai de deux ans, d'une modification pour prendre en compte de nouvelles obligations applicables aux communes de son territoire en application des articles L. 302-5 et suivants.",
        "Les procédures engagées sur ce seul fondement cessent à cette date. La réaffectation des prélèvements sanctionnant l'absence de cette modification est également supprimée pour l'avenir.",
    ),
]


def record(source, xml, reason, notes, removed, benefit, classification, assessment, limits, burdens, effects):
    return {
        **{k: source[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']},
        'proposed_xml': xml,
        'reason': reason,
        'review_notes': notes,
        'status': 'rewrite_draft',
        'change_type': 'normative_reduction',
        'reform_policy_id': 'editorial_direction_2026_10_19',
        'removed_provisions': removed,
        'benefit_review': benefit,
        'substantive_impact': {
            'version': 1,
            'classification': classification,
            'assessment': assessment,
            'scope_limitations': limits,
            'new_burdens_review': burdens,
            'effects': effects,
        },
    }


answer = [
    record(
        first, xml1,
        "Réforme de fond : conserver la suppression acquise de la participation obligatoire des maires d'arrondissement et retirer en outre l'obligation de créer et maintenir un observatoire sous trois ans, les recensements obligatoires propres à ce dispositif et son obligation annuelle de compte rendu, sans circuit de remplacement. Le diagnostic, les cinq catégories d'observation désormais facultative et la convention de mutualisation restent disponibles ; le suivi autonome de L302-3 n'est pas abrogé. Les ajouts antérieurs sur la densification, les réseaux, les écoles et le financement sont conservés avec leur transition et identifiés comme exigences nouvelles par rapport à la source officielle ; calendrier et financement figurent une seule fois au IV. Droit constant pour le programme intercommunal de six ans, les typologies et le programme d'actions : ils relient les moyens fonciers et financiers aux besoins, aux opérations et au relogement, sans créer de quota. Le diagnostic de l'habitat indigne et les réponses aux besoins des publics vulnérables conservent leur fonction de protection ; les autres passages utiles sont repris sans réécriture stylistique. Coordination expresse du renvoi défectueux à L302-16 et exclusion de toute réintroduction des quotas supprimés.",
        "Lecture intégrale des sources et des deux versions du brouillon : les propositions de premier niveau et previous_draft ont le même contenu normatif après extraction du texte ; leur balisage et l’encodage des apostrophes diffèrent. SRU 58 et ses notes documentaires sont lus : seule la participation des maires d'arrondissement est textuellement attribuable à cet article initial ; le PLH et toutes ses normes actuelles ne sont pas réputés issus de SRU. Les coupes d'observation relèvent de l'orientation générale actuelle, sans attribution historique non établie. Subdivisions I à IV, rang des paragraphes, cinq catégories 1° à 5°, six ans, seuils de plus de 30 000 et de plus de 10 000 habitants, typologies et assimilation au 1er mars 2014 maintenus. Le délai de trois ans propre à la création obligatoire de l'observatoire est supprimé expressément, non le bilan triennal distinct de L302-3. Le dernier alinéa du IV conserve exactement sa place et son contenu pour L302-4-1. Cibles locales consultées : L302-2/3/4-1/4-2/5/16, L321-8, R302-1 à R302-1-5 pour les dispositions pertinentes, CU L151-28/41, L152-6, R151-54/R152-1 et CGI 1406 bis I B 1°. L302-16 (LEGIARTI000031009505, version depuis le 8 août 2015) ne comporte pas de I : renvoi source corrigé explicitement vers l'article entier, dont les conditions cumulatives demeurent. La terminologie source « plan local de l'habitat » dans la convention de mutualisation est conservée ; elle diffère de « programme » et nécessite une harmonisation distincte, sans changement de bénéficiaires ici. À coordonner dans des articles hors lot : R302-1-3 a pour l'observatoire facultatif, R302-1-4 pour supprimer les obligations de recensement et de suivi propres au dispositif obligatoire sans supprimer l'accès légal aux informations ni l'appui volontaire, et CU R151-54 3°/R152-1 pour ne pas rétablir la création obligatoire lorsqu'un PLU tient lieu de PLH. Le décret ne peut contredire le nouveau III. R302-1-5 reste utile à la convention facultative, maintenue à l'avant-dernier alinéa logique du III ; les cinq catégories gardent leur ordre pour le renvoi de R302-1-4 I 2°. L302-3 et R302-13 conservent les bilans autonomes de réalisation, utiles au contrôle public des objectifs et des moyens : aucune suppression de ceux-ci n'est comptée. Dans L302-3, l'appui sur les observatoires doit être coordonné comme facultatif lorsqu'ils existent ; le présent III exclut déjà toute obligation de création par ce renvoi. La note source relative aux impositions 2027, à la vacance et à la loi du 19 février 2026 ne date pas cette réforme et ne modifie pas ici la taxe de 1406 bis. Les protections environnementales, patrimoniales et les droits au logement demeurent ; aucune conformité européenne globale n'est présumée. Ces coordinations signalées ne sont pas présentées comme rédigées ; aucun achèvement des 209 articles SRU n'est revendiqué.",
        [
            "Participation obligatoire des maires d'arrondissement de Paris, Marseille et Lyon ou de leurs représentants à l'élaboration du PLH, sans saisine de substitution.",
            "Obligation de définir dans le PLH les conditions de mise en place des observatoires de l’habitat et du foncier, sans programmation obligatoire de substitution.",
            "Obligation de mettre en place et de maintenir un observatoire de l'habitat et du foncier, échéance de trois ans et recensements obligatoires propres à ce dispositif.",
            "Obligation annuelle de compte rendu des observatoires, quel que soit son support, sur les logements construits en espaces urbanisés et en zones ouvertes à l'urbanisation, y compris tout rattrapage non encore établi.",
        ],
        "Aucune exonération fiscale n'est supprimée dans cet article. Les typologies de logements sociaux, très sociaux, intermédiaires, privés conventionnés et en intermédiation sont maintenues ; l'assimilation historique des logements HLM/SEM et financés par les prêts visés, avec ses plafonds et la date du 1er mars 2014, n'est pas restreinte. Les conventions facultatives d'observation avec l'EPCI compétent le plus proche restent ouvertes aux futures collectivités qui remplissent les conditions de la source. Les orientations de majoration constructible des 2° et 4° de L151-28 restent inscrites au IV, de même que le renvoi à L152-6 et les conditions de protection ; aucune possibilité de construire n'est fermée. Les aides, conventions, contrats et droits acquis sont préservés et les dispositifs autonomes demeurent accessibles aux situations futures éligibles. La suppression des obligations de l'observatoire ne ferme aucun de ces avantages ni le diagnostic utile à la lutte contre l'habitat indigne.",
        'mixed',
        "Par rapport à la source officielle entière, suppression d'une participation locale obligatoire et d'une même famille d'obligations d'observation : création sous trois ans, maintien, recensements obligatoires propres et compte rendu annuel propre au dispositif. Diagnostic et programmation du logement, droits des publics fragiles et bilans de L302-3 demeurent. Les ajouts de densification du précédent brouillon constituent aussi une charge d'analyse et de programmation par rapport à cette source ; leur conservation interdit de qualifier tout le résultat de réduction nette démontrée. Aucun impôt n'est supprimé ou diminué par cet article.",
        "Le PLH reste obligatoire pour les EPCI visés et, selon L302-4-1, les communes concernées ; les procédures d'élaboration, les bilans légaux, les contraintes de sécurité et les droits des tiers restent distincts. Les règlements d'observation et ceux des PLU tenant lieu de PLH doivent être coordonnés aux endroits identifiés. Les délais de diagnostics, coûts publics, effets sur le logement et solde de complexité ne sont pas chiffrés ; aucune conclusion nationale ou sur l'ensemble de SRU n'en découle.",
        "Les diagnostics de densification, l'examen des capacités d'eau, d'assainissement, d'écoles et des autres réseaux, ainsi que la programmation et l'indication des financements arrêtés ou non, sont des exigences supplémentaires par rapport au texte officiel, même si le précédent brouillon les contenait déjà. Leur transition est conservée et aucune réouverture automatique des PLH en vigueur n'en résulte. Aucun registre, nouveau rapport périodique, autorisation, justificatif privé ou collecte obligatoire de remplacement de l'observatoire n'est créé ; la convention facultative et les données légalement accessibles restent dans leur champ. Le coût net de ces ajouts et des coupes n'est pas établi.",
        effects1,
    ),
    record(
        second, xml2,
        "Réforme de fond supplémentaire au premier brouillon : supprimer la transmission pour avis préalable au préfet et aux personnes morales associées pour les modifications du I, sans déclaration de remplacement ; ouvrir la procédure de modification aux extensions de périmètre atteignant ou dépassant le cinquième de la population lorsque l'économie générale n'est pas atteinte. La faculté existante sous le cinquième est intégralement conservée. Maintenir la suppression acquise du II, modification forcée pour quotas SRU, procédure préfectorale spéciale et réaffectation sanction, avec transition expresse et renvoi coordonné au V proposé de L302-5. Droit constant pour l'autorité délibérante, les trois motifs a à c et la voie d'adaptation de L300-6-1 ; contrôle de légalité et procédures environnementales autonomes préservés.",
        "Source entière, notes source vides, previous_draft et contexte SRU 56 lus intégralement. L'insertion SRU 56 concernait en 2000 une phrase de modification pour l'accroissement social minimum ; le II actuel, remanié ultérieurement, n'est pas attribué intégralement à ce seul texte initial. Son retrait repose sur le contenu actuel et la suppression coordonnée des quotas, sans prétendre avoir achevé la filiation de tout SRU 56. Les huit paragraphes du I et les lettres a, b, c restent à leur rang ; le sixième porte la dispense d'avis, et non une suppression silencieuse de deux mois. Ce délai était le délai maximal de l'avis réputé donné, pas nécessairement un délai minimal systématique : aucun gain uniforme de soixante jours n'est revendiqué. L'ancienne faculté d'extension sous le cinquième demeure mot pour mot ; la condition d'économie générale ne s'ajoute qu'à la voie nouvelle au seuil ou au-dessus. Le IV et le V de L302-5 ont été lus dans le projet du corpus ; le V est une disposition proposée de transition, non le droit en vigueur, et doit être adopté simultanément avec les suppressions de L302-5 à L302-9-1-2 pertinentes. La transition distingue les créances antérieures et affectations acquises de toute réaffectation sanction nouvelle ; pas de remboursement général ni de recette de substitution. CU L131-9 comporte le renvoi au dernier alinéa de l'ancien II et nécessite sa coordination avec les quotas supprimés ; il n'est pas rédigé dans ce lot. CCH L302-4-1 étend l'application aux communes de plus de 20 000 habitants hors EPCI visé et exclut littéralement le quatrième alinéa, soit le c), alors que l'extension de périmètre est au cinquième : incohérence préexistante explicitement signalée, sans en présumer l'intention ni déplacer ces alinéas. Ce renvoi reste matériellement inchangé par notre structure et doit faire l'objet d'une décision distincte dans l'article cible ; il n'est pas déclaré résolu. R302-13-1 conserve sa portée d'application communale. L302-2 reste applicable à l'élaboration initiale, sans être réintroduit comme consultation obligatoire du I. L'adaptation favorable de CU L300-6-1 est maintenue après lecture entière de sa cible : champ d'intérêt général, limites, enquête publique, avis et évaluation environnementale propres à la procédure intégrée ne sont pas supprimés. Les contrôles de légalité et de participation disposant d'un fondement distinct demeurent, notamment les exigences européennes qui ne peuvent être écartées par la seule dispense d'avis locale. Aucun autre code ni aucun formulaire n'est présenté comme intégralement coordonné.",
        [
            "Transmission obligatoire pour avis préalable du projet de modification ordinaire au préfet et aux personnes morales associées, avec circuit d'avis réputé donné sous deux mois.",
            "Exclusion de la faculté spéciale de modification lors d'une extension de périmètre atteignant ou dépassant le cinquième de la population totale, pour les projets sans atteinte à l'économie générale.",
            "Modification obligatoire du PLH sous deux ans pour les quotas sociaux supprimés, avec avis, demandes préfectorales, blocage de prise d'effet et réaffectation sanction des prélèvements.",
        ],
        "Les avantages procéduraux sont expressément préservés : faculté de modification selon a, b et c sans nouvelle procédure d'élaboration, faculté spéciale en cas d'extension représentant moins du cinquième de la population et adaptation intégrée selon L300-6-1, y compris pour les projets futurs recevables. La faculté de modification est en outre élargie au seuil ou au-dessus, sous la seule condition d'absence d'atteinte à l'économie générale propre à cette nouvelle voie ; aucune condition n'est ajoutée sous le seuil existant. L'avis réputé donné sous deux mois n'est pas supprimé au détriment du demandeur : toute la consultation obligatoire qui le rendait utile disparaît pour le I, y compris pour les projets non approuvés en cours, sans agrément ni déclaration de remplacement. Les avis déjà acquis restent utilisables. Au II, l'avis réputé favorable après deux mois et la prise d'effet après deux mois sans opposition sont des garanties de la procédure de modification forcée : elles deviennent sans objet avec la suppression entière de cette procédure, sans autorisation de remplacement. La réaffectation aux établissements publics fonciers, à l'office foncier de la Corse ou au fonds national pouvait favoriser ces bénéficiaires ; les affectations légalement acquises sur les créances antérieures sont préservées, mais aucun prélèvement supprimé pour l'avenir n'est recréé pour les alimenter. Les anciennes créances, affectations acquises, aides, conventions et droits des occupants et des tiers conservent la transition de L302-5 V ; aucun dispositif autonome d'aide au logement n'est fermé aux futures situations éligibles par la fin des quotas.",
        'material_reduction',
        "Par rapport à la source officielle entière, le I perd effectivement son circuit obligatoire d'avis préalables et ouvre une faculté de modification pour les extensions de périmètre au seuil d'un cinquième ou au-dessus, sans restreindre celle qui existait sous ce seuil. La suppression du II met en œuvre la mesure déjà décidée de fin des quotas et du rattrapage : elle n'est ni une deuxième abolition de prélèvement ni une suppression de la programmation autonome du logement. La décision délibérante, les motifs du I et les garanties distinctes demeurent.",
        "La dispense vise les avis du I sur les modifications du PLH, non les consultations d'élaboration initiale de L302-2, la procédure intégrée de L300-6-1 ou le contrôle de légalité. Les projets portant atteinte à l'économie générale ne bénéficient pas de la nouvelle voie d'extension au seuil ou au-dessus. La coordination de CU L131-9 et l'ambiguïté historique du renvoi ordinal de L302-4-1 restent identifiées hors lot. Aucun effet budgétaire, gain uniforme de délai ou solde global des codes n'est démontré.",
        "Aucune charge nouvelle n'est identifiée dans cet article : les avis ne sont remplacés ni par un agrément, ni par une déclaration, un rapport ou un nouveau dépôt. La réserve d'économie générale ne limite que la faculté nouvellement ouverte au seuil ou au-dessus du cinquième ; la faculté favorable antérieure sous le seuil n'est pas durcie. L'approbation par l'organe délibérant, le contrôle de légalité, les obligations environnementales et les conditions de la voie intégrée existaient déjà et demeurent à leur champ propre. Les coûts publics et le solde net de l'ensemble des codes ne sont pas chiffrés.",
        effects2,
    ),
]

Path('article-L302-1.xml').write_text(xml1 + '\n')
Path('article-L302-4.xml').write_text(xml2 + '\n')
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print('answer.json:', len(answer), 'articles')
