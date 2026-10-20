import json
import re
from html import unescape
from pathlib import Path


ROOT = Path(__file__).resolve().parent
sources = json.loads((ROOT / 'source.json').read_text())
references = json.loads((ROOT / 'reference-targets.json').read_text())


def paragraphs(xml):
    return re.findall(r'<p>(.*?)</p>', xml, re.S)


def text(xml):
    return unescape(re.sub(r'<[^>]*>', '', xml))


def effect(kind, measure_id, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
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


def impact(classification, assessment, limitations, burdens, effects):
    return {
        'version': 1,
        'classification': classification,
        'assessment': assessment,
        'scope_limitations': limitations,
        'new_burdens_review': burdens,
        'effects': effects,
    }


answers = []
for src in sources:
    answers.append({k: src[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']})
    answers[-1]['status'] = 'rewrite_draft'
    answers[-1]['reference_checks'] = []


# L421-3 : conserver exactement les parties de la source qui ne changent pas.
src, out = sources[0], answers[0]
old_five = paragraphs(src['source_xml'])[7]
new_five = """5° Gérer, en qualité d'administrateurs de biens, des logements situés dans des copropriétés connaissant des difficultés importantes de fonctionnement ou être syndics de ces copropriétés, sans accord préalable du préfet ni du maire de la commune d'implantation. Par dérogation aux dispositions de l'article L. 411-2 qui exigent ces accords, les interventions des offices prévues au présent 5° n'y sont pas soumises. Cette dispense n'affecte ni leur qualification de service d'intérêt général ni leur accès aux exonérations fiscales et aux aides spécifiques attachées à cette qualification lorsque les autres conditions prévues par les textes qui les régissent sont réunies. Aucune demande d'autorisation, déclaration de remplacement ou attente d'un délai d'opposition n'est exigée à ce titre. Dans ces mêmes copropriétés, lorsqu'elles font l'objet d'un plan de sauvegarde en application de l'article L. 615-1 ou d'une opération programmée d'amélioration de l'habitat prévue à l'article L. 303-1 et dédiée aux copropriétés dégradées ou lorsqu'elles sont situées dans le périmètre d'opérations de requalification de copropriétés dégradées prévues à l'article L. 741-1, les offices peuvent acquérir des lots en vue de leur revente, y effectuer tous travaux et les louer provisoirement. La revente des lots ainsi acquis n'est subordonnée à aucun avis préalable de l'administration des finances publiques. Un décret en Conseil d'Etat précise les modalités de ces acquisitions, travaux, reventes et locations provisoires ; ces modalités peuvent déroger aux règles applicables aux habitations à loyer modéré et ne peuvent rétablir les accords, demandes, délais d'opposition ou avis préalables supprimés ;"""
transition = """Les dispenses prévues au 5° s'appliquent à compter de l'entrée en vigueur de la présente loi aux interventions et aux reventes réalisées à compter de cette date, y compris lorsqu'elles concernent des lots antérieurement acquis, ainsi qu'aux demandes en cours. Aucun nouveau dépôt ni renouvellement de dossier n'est exigé à ce titre. Les mandats, opérations, baux, aides et engagements financiers valablement constitués avant cette date ainsi que les droits des occupants, des copropriétaires et des tiers sont préservés."""
out['proposed_xml'] = src['source_xml'].replace('<p>' + old_five + '</p>', '<p>' + new_five + '</p>').rstrip() + '\n<p>' + transition + '</p>'
out['change_type'] = 'normative_reduction'
out['reform_policy_id'] = 'editorial_direction_2026_10_19'
out['removed_provisions'] = [
    "Les accords préalables du préfet et du maire pour la gestion ou le syndic des copropriétés en difficulté relevant du 5° sont supprimés, y compris leur exigence au titre du service d'intérêt général de L. 411-2.",
    "La demande d'autorisation et l'attente du délai d'opposition de deux mois propres à ces accords sont retirées, sans déclaration ni dossier de remplacement.",
    "L'avis préalable de l'administration des finances publiques exigé par R. 421-2 pour la revente des lots acquis dans le cadre du 5° est supprimé pour les reventes futures, même si les lots ont été acquis antérieurement.",
]
out['reason'] = """Réforme de fond : maintien de la coupe déjà acquise des accords du préfet et du maire, de leur demande et de l'attente d'opposition au 5°, avec dérogation expresse à L. 411-2 pour préserver le service d'intérêt général et ses avantages. Coupe supplémentaire après lecture de R. 421-2 : la revente des lots du 5° ne nécessite plus l'avis fiscal préalable. Cet avis consultatif ne constitue ni le mandat de la copropriété, ni une garantie de relogement ou de loyer ; le contrôle de la gestion des actifs publics et sociaux et les responsabilités des organes de l'office subsistent. Il ne reçoit aucune formalité de remplacement. La transition couvre les demandes en cours et les reventes nouvelles de lots anciens. À droit constant, tous les autres paragraphes de la source sont reproduits sans reformulation ; les trois cadres permettant l'acquisition de lots, les travaux et la location provisoire restent entiers. Après réexamen, le caractère subsidiaire, les donneurs d'ordre, les bénéficiaires, le seuil de 99 % et l'encadrement du financement au 6° délimitent l'emploi des moyens d'un établissement social : leur suppression n'est pas justifiée. Le renvoi à un décret au 6° n'est pas un agrément individuel supplémentaire. Aucun impôt n'est diminué par cet article."""
out['review_notes'] = """Source entière, notes vides, précédent brouillon entier et texte initial entier de SRU 146 examinés. Les onze paragraphes initiaux restent dans leur ordre ; seul le 5° change et un paragraphe transitoire est ajouté. Le 2° ter reste dans le paragraphe du 2° bis après ses br. Lecture intégrale des sources locales de L. 411-2, L. 411-3, L. 421-1, R. 421-2, R. 442-23 et L. 312-3-1. R. 442-23 doit retirer, pour le 5° des offices, la demande simultanée, ses pièces et les deux mois d'opposition ; sa mention du maire est également couverte par la dispense, sans modifier les régimes distincts au seul motif de cette coordination. Le 3° de R. 421-2 dispose actuellement : « La revente de ces lots n'est pas soumise aux dispositions du chapitre III du titre IV du livre IV du présent code mais requiert l'avis préalable du directeur départemental ou, le cas échéant, régional des finances publiques. » Supprimer matériellement cette seule exigence d'avis ; conserver l'exemption de ce chapitre, la référence à l'article 40 de la loi de 1989, le plafond fiscal de loyer et les I et II de son article 15 pour les congés du bailleur. L'effet supplémentaire est prouvé par cette disposition d'exécution : la citation de la source assignée dans substantive_impact porte sur l'habilitation réglementaire du 5°, et non sur une exigence d'avis qui y serait écrite. Aucun délai fiscal chiffré de revente n'est inventé. Les autres avis, règles de cession ou accords, notamment au 3° de L. 421-1, restent distincts. L. 411-3 présente lui-même un renvoi aux lots de L. 421-1 sans citer L. 421-3 : cette imprécision préexistante n'est pas corrigée silencieusement ; le régime favorable explicite de R. 421-2 est conservé. L. 312-3-1 garde les garanties d'emprunts et les conventions des opérations du 8°. Les contrôles ANCOLS, le choix du mandataire selon le droit de la copropriété, les fonds SIEG séparés et les droits des occupants demeurent. La décision 2012/21/UE mentionnée par L. 411-2 n'est pas écartée ; aucune conformité européenne nouvelle n'est présumée. Les règlements et la loi du 10 juillet 1965 ne sont pas déclarés réécrits par ce lot. SRU 146 modifiait d'anciens numéros et des compétences ensuite complétées : la filiation complète n'est pas établie et ce volet n'est pas déclaré achevé. Aucune réforme d'impayés ou de rénovation locative de vingt-quatre mois n'est imputée au présent article ; elle demanderait les dispositions autonomes de la loi du 6 juillet 1989 et de ses textes d'application."""
out['benefit_review'] = """Les compétences facultatives des 1° à 8°, y compris l'ingénierie urbaine, la rénovation énergétique, l'insertion et les prestations sociales, demeurent ouvertes aux futures situations éligibles. Au 5°, la qualification SIEG et l'accès aux exonérations fiscales et aides spécifiques de L. 411-2 sont explicitement préservés malgré la disparition des accords ; leurs autres conditions et les exigences européennes restent applicables. L'acquisition-revente, les travaux et la location provisoire dans les trois cadres nommés restent possibles, avec les dérogations réglementaires favorables aux règles HLM. La dispense de régime ordinaire de revente de R. 421-2 demeure : seul son avis fiscal préalable est retiré. Le plafond de loyer et les protections de congé sont conservés, ainsi que les garanties d'emprunts du 8° prévues par L. 312-3-1 et les financements éligibles du 6°. Les 99 % déterminent les sociétés bénéficiaires et ne sont pas un taux de prélèvement. Aucune aide n'est restreinte aux seules opérations anciennes et aucune taxe n'est créée ou étendue."""
out['substantive_impact'] = impact(
    'material_reduction',
    "Par rapport à la source officielle entière, le 5° retire le double accord et son circuit préalable ; l'habilitation d'exécution est en outre restreinte pour supprimer l'avis fiscal à la revente. Ce dernier retrait dépasse le précédent brouillon. Il s'agit de charges de procédure supprimées, sans baisse d'impôt ni économie nationale chiffrée.",
    "Les dispenses ne suppriment ni les cadres de sauvegarde et de requalification, ni les droits des occupants ou les règles SIEG. R. 442-23 et le 3° de R. 421-2 doivent être matériellement coordonnés hors de ce lot. Les coûts évités ne sont pas chiffrés et le solde de l'ensemble des codes n'est pas établi.",
    "Aucune charge nouvelle n'est identifiée : aucun dépôt, déclaration, registre, délai, visa ni contrôle préalable ne remplace les procédures retirées. Le mandat, les conditions sociales, les contrôles et les protections locatives mentionnés existaient déjà ; leur maintien ne constitue pas une obligation nouvelle.",
    [
        effect(
            'authorization_removed', 'hlm-coproprietes-degradees-fin-accords',
            "Suppression du double accord préalable et de son circuit de demande et d'opposition pour les interventions des offices au 5° ; une seule mesure avec ses coordinations SIEG.",
            "Office prestataire : accord du préfet et du maire avant gestion ou syndic en copropriété en difficulté ; demande et opposition préfectorale pendant deux mois dans L. 421-3, avec dossier et opposition des deux autorités dans R. 442-23 ; accord également exigé par L. 411-2 pour le SIEG.",
            "Office prestataire dans le même champ : aucun accord du préfet ou du maire, aucune demande ni attente d'opposition ; accès SIEG et avantages maintenus sous leurs autres conditions.",
            'legal_duty', "Offices publics de l'habitat intervenant dans les copropriétés visées au 5°.",
            "Entrée en vigueur de la loi proposée, interventions futures et demandes en cours ; mandats, baux, aides, engagements et droits des tiers déjà constitués préservés.",
            "Aucune autorisation ou déclaration de remplacement ; contrôles autonomes et droits de la copropriété maintenus.",
            "Avec l'accord du préfet et du maire de la commune d'implantation",
            "sans accord préalable du préfet ni du maire de la commune d'implantation.",
        ),
        effect(
            'obligation_removed', 'oph-revente-lots-fin-avis-fiscal',
            "Suppression supplémentaire de l'avis fiscal préalable à la revente des lots du 5°, exigé dans la réglementation prise sur son habilitation.",
            "L. 421-3 renvoie les modalités d'acquisition-revente au décret ; le 3° de R. 421-2 exige l'avis préalable du directeur départemental ou régional des finances publiques avant la revente, tout en dispensant du régime HLM ordinaire de vente.",
            "Les mêmes reventes sont dispensées de cet avis préalable ; le champ de l'acquisition, la dispense de vente HLM, les plafonds de loyer et les protections de congé restent applicables.",
            'legal_duty', "Offices revendant des lots acquis dans les copropriétés du 5°, y compris des lots acquis avant la réforme.",
            "Reventes réalisées dès l'entrée en vigueur de la loi ; actes antérieurs valables, droits des occupants et engagements conservés. Suppression réglementaire correspondante à réaliser dans R. 421-2.",
            "Aucun avis, attestation, déclaration ou délai de substitution ; responsabilités de gestion et contrôles autonomes conservés.",
            "ils peuvent, selon des modalités précisées par décret en Conseil d'Etat qui peuvent déroger aux règles applicables aux habitations à loyer modéré, acquérir des lots en vue de leur revente, y effectuer tous travaux et les louer provisoirement",
            "La revente des lots ainsi acquis n'est subordonnée à aucun avis préalable de l'administration des finances publiques.",
        ),
    ],
)


# L421-4 : coordination historique ciblée ; aucun changement des autres alinéas.
src, out = sources[1], answers[1]
old_b = paragraphs(src['source_xml'])[5]
new_b = old_b[:-1].rstrip() + ", dans les rédactions de cet alinéa et de ce décret applicables aux opérations régulièrement engagées pendant cette expérimentation. Ce renvoi historique ne rétablit aucune obligation de quota, de rattrapage, de prélèvement ou de carence et ne rouvre pas la période d'expérimentation ;"
out['proposed_xml'] = src['source_xml'].replace('<p>' + old_b + '</p>', '<p>' + new_b + '</p>')
out['reason'] = """Coordination nécessaire, sans réduction matérielle supplémentaire : le b du 3° conserve, pour les opérations régulièrement engagées pendant l'expérimentation de cinq ans ouverte en 2014, l'ancien critère géographique renvoyant au II de L. 302-5 et à son décret. La suppression des quotas SRU ne doit ni rendre ce renvoi orphelin pour ces opérations, ni rouvrir l'expérimentation. Les réformes déjà acquises sont ainsi conservées ; les autres paragraphes sont repris exactement de la source officielle, sans nouvelle reformulation stylistique. Après examen, l'agrément du 9° n'est pas un second agrément HLM identique : il qualifie l'activité distincte d'organisme de foncier solidaire, avec pérennité des baux et réserves affectées à cette activité. Le supprimer sans traiter son régime autonome ne préserverait pas sûrement les preneurs. La convention du 11° identifie les services sociaux d'intérêt direct rendus hors des conditions normales du marché ; elle conserve la destination du service et de ses financements, et n'est pas supprimée par assimilation aux accords de copropriété de L. 421-3. Les plafonds de ressources, bénéficiaires sociaux, 99 % et limites SIEG délimitent les aides et actifs sociaux plutôt qu'un quota communal. Aucune coupe supplémentaire n'est justifiée dans ce corps après cet examen."""
out['review_notes'] = """Source entière, ses deux notes fiscales, précédent brouillon entier et texte initial entier de SRU 146 lus. Le seul changement par rapport à la source est l'ajout, au b du 3°, du gel historique de L. 302-5 II et de son décret et de l'absence de réouverture ; aucune liste SRU n'est recréée. Les autres alinéas sont identiques, y compris les 1° à 11°, a et b, les deux seuils 50 000 et 15 000, les deux seuils de 99 %, les bénéficiaires, l'exemption de la sous-section de vente et les br entre 9°, 10° et 11°. La version assignée entrée en vigueur en 2026 rattache une expérimentation commencée en 2014 à CGI 1406 bis ; ses notes annoncent l'application fiscale en 2027 et la prise en compte de la vacance avant le 1er janvier 2027. Cette articulation temporelle préexistante n'est ni une nouvelle date d'expérimentation ni une preuve de réouverture. La référence 1406 bis n'est pas artificiellement figée à une rédaction de 2014 non fournie : le gel ajouté désigne expressément le seul alinéa de L. 302-5 et son décret. La concordance fiscale historique reste à contrôler dans les versions datées ; aucun effet rétroactif nouveau n'est revendiqué. Les sources locales intégrales de L. 329-1 urbanisme et R. 329-1 à R. 329-3 ont été examinées : agrément OFS distinct, pérennité des baux, non-partage, réserves et comptabilité d'activité justifient de conserver le 9° ici. Cette conservation ne valide pas toutes les pièces ou procédures de l'agrément extérieur au lot. Les six cibles de reference-targets.json sont couvertes exactement dans reference_checks : les trois cibles travail ne sont pas des renvois de cet article ; les trois cibles L. 261 relèvent de la vente immobilière. Un délai de construction, de dépôt de garantie ou de résolution n'est pas une durée d'emploi. Les propositions de ces cibles restent des projets, non le droit en vigueur. SRU 146 visait des versions antérieures d'autres numéros et ne démontre pas la filiation entière du L. 421-4 actuel : cet examen ne clôt ni ce volet ni les 209 articles de SRU."""
out['benefit_review'] = """Le 3° conserve la faculté d'acquisition de nue-propriété ou d'usufruit et son exemption du régime de vente HLM, notamment pour les opérations futures éligibles au a ; le b reste une expérimentation échue dont les opérations régulièrement engagées conservent leurs droits sans nouveau quota. Les locations, sous-locations meublées ou non, services d'insertion, assistance aux personnes âgées, handicapées et victimes de violences, prestations et activité OFS demeurent ouverts selon leurs conditions, ainsi que les baux réels solidaires d'activité. Aucune exonération ni aide liée au SIEG n'est supprimée ; les seuils de 99 % et de ressources restent inchangés. Le gel du renvoi SRU ne réserve pas les autres facultés aux situations anciennes."""
out['substantive_impact'] = impact(
    'coordination_only',
    "La seule différence normative avec la source entière est la sécurisation historique du renvoi géographique de l'expérimentation échue, en coordination avec la suppression des quotas. Aucune taxe, obligation d'agrément, condition de ressources ou durée d'emploi n'est supprimée dans cet article ; aucun allègement autonome n'est compté.",
    "Le b ne permet pas de nouveaux engagements après sa période expérimentale ; les autres facultés restent ouvertes aux futures situations éligibles. La concordance fiscale historique de 1406 bis et le régime réglementaire OFS ne sont pas intégralement résolus par ce lot ; aucune réduction nette globale n'est établie.",
    "Aucune charge nouvelle n'est identifiée : le gel du renvoi ne demande aucune liste, pièce, attestation ni dépôt nouveau. Les conditions sociales, l'agrément OFS et la convention de services maintenus figuraient déjà dans la source ; aucune formalité ne remplace les quotas supprimés.",
    [effect(
        'coordination', 'sru-suppression-quotas-prelevements-carence',
        "Coordination historique du renvoi à L. 302-5 II pour éviter de rétablir les quotas ou de perdre le périmètre des opérations anciennes.",
        "Le b vise le dernier alinéa du II de L. 302-5 et son décret sans préciser la version applicable à l'expérimentation de cinq ans issue de la loi de 2014.",
        "Cette seule référence et son décret sont appliqués dans leurs versions pertinentes pour les opérations régulièrement engagées pendant l'expérimentation, sans quota futur ni nouvelle période expérimentale.",
        'other', "Offices et opérations d'usufruit ou de nue-propriété régulièrement engagées pendant l'expérimentation du b du 3°.",
        "Droits des opérations anciennes préservés ; aucune réouverture de l'expérimentation ni nouvelle obligation liée aux listes SRU.",
        "Aucun inventaire, collecte, dossier ou condition de preuve supplémentaire n'est institué.",
        "définies par décret pris en application du dernier alinéa du II de l'article L. 302-5 du présent code",
        "dans les rédactions de cet alinéa et de ce décret applicables aux opérations régulièrement engagées pendant cette expérimentation.",
    )],
)
assessments = {
    'L1234-1': "L. 421-4 ne vise pas L. 1234-1 : son 2° renvoie à L. 261-1 à L. 261-22 pour la vente d'immeubles à construire. Le préavis de licenciement, anciennement lié aux six mois et deux ans, puis de quinze jours calendaires pour les contrats nouveaux dans le projet cible, n'a donc pas à être inséré ici. Ni ancienneté ni notification de rupture d'emploi ne conditionnent ces ventes. Les droits des anciens salariés et les procédures collectives ou protections spéciales ne sont pas modifiés par cette coordination immobilière.",
    'L1221-2': "L. 1221-2 n'est pas un renvoi du texte assigné : il définit dans le projet le contrat privé unique à durée indéterminée pour les embauches nouvelles, en conservant les situations anciennes. Le délai d'édification visé par le 2° de L. 421-4 et l'expérimentation de cinq ans du b du 3° sont respectivement une obligation du vendeur et une fenêtre d'opérations immobilières, pas un terme d'emploi. Aucun CDD nouveau, ni exception au contrat unique, ni durée d'ancienneté n'est institué ici.",
    'L1234-9': "Aucun renvoi à L. 1234-9 ne figure dans L. 421-4. L'indemnité ordinaire du projet cible, zéro avant un an mesuré au terme effectif préavis inclus, puis 0,20 mois par année totale au prorata des mois complets et au plafond de six mois, employeur seul, concerne la rupture du travail et conserve sa transition et ses indemnités spéciales. Elle ne remplace pas le plafond de 10 % du prix en résolution immobilière de L. 261-14. Aucune condition d'ancienneté ou de notification de licenciement n'est appliquée aux acquéreurs.",
    'L261-1': "Cible réellement comprise dans le renvoi L. 261-1 à L. 261-22 du 2° : définition de la vente d'immeuble à construire, à terme ou en l'état futur d'achèvement, avec délai d'édification fixé au contrat. La cible officielle, qui cite le code civil, et sa proposition ne concernent pas la durée de l'emploi. Ce renvoi et les droits des opérations antérieures comme futures restent applicables ; ni préavis individuel de quinze jours ni condition d'ancienneté du salarié n'y sont substitués.",
    'L261-12': "Cible réellement incluse au 2° : interdiction des versements avant signature ou exigibilité en VEFA ; pour la vente à terme, dépôts progressifs sur compte spécial au nom de l'acquéreur, avec incessibilité, insaisissabilité et indisponibilité sauf paiement du prix. Ces garanties protègent les fonds des acquéreurs, y compris futurs, et sont conservées sans les assimiler à des acomptes de salaire, à une indemnité ou à un préavis. Aucune condition d'ancienneté ou de notification de rupture du travail n'est pertinente.",
    'L261-14': "Cible réellement comprise dans le renvoi du 2° : l'indemnité forfaitaire de résolution de la vente reste plafonnée à 10 % du prix, avec demande possible de réparation du préjudice effectivement subi. Ce sont les parties à la vente et son prix, pas le salarié et son salaire de référence. Le plafond de six mois, le seuil d'un an préavis inclus et les 0,20 mois du projet L. 1234-9 ne modifient pas ce régime civil ni ses opérations futures. La proposition cible est distinguée du texte officiel ; le renvoi demeure cohérent.",
}
key = src['code_id'] + '|' + src['source_id']
for target_key in references['requirements'][key]:
    target = references['targets'][target_key]
    out['reference_checks'].append({
        'target_key': target_key,
        'view_sha256': target['view_sha256'],
        'assessment': assessments[target['number']],
    })


# L421-7 : la réforme antérieure demeure après examen de chaque garantie restante.
src, out = sources[2], answers[2]
out['proposed_xml'] = src['previous_draft']['proposed_xml']
out['change_type'] = 'normative_reduction'
out['reform_policy_id'] = 'editorial_direction_2026_10_19'
out['removed_provisions'] = [
    "Le décret de création ou de dissolution volontaire succédant à une demande de l'organe local compétent est supprimé au profit de sa délibération exécutoire.",
    "L'arrêté préfectoral autorisant les changements volontaires de rattachement, d'appellation et les fusions est supprimé, ainsi que la demande d'autorisation correspondante.",
    "L'avis régional préalable et le circuit de décision préfectorale propres à ces décisions volontaires ne sont plus requis, sans nouvelle déclaration de remplacement.",
]
out['reason'] = """Réforme de fond maintenue après seconde lecture de toute la source : création, dissolution volontaire, changement volontaire de rattachement ou d'appellation et fusion sont décidés par les organes locaux compétents, sans décret ou arrêté d'autorisation ni avis régional préalable. Le projet supprime la seconde décision d'opportunité de l'Etat et le dossier d'autorisation ; les délibérations constituaient déjà l'initiative obligatoire. Aucune déclaration ne remplace ce circuit. Aucune coupe supplémentaire n'est justifiée parmi les garanties restantes : les délibérations concordantes assurent le consentement de chaque personne publique affectée ; les avis des conseils d'administration et consultations du personnel assurent la prise en compte des patrimoines gérés et des droits des agents ; la publicité, le contrôle de légalité, la représentation des locataires et les recours protègent les tiers. Supprimer ces garanties serait distinct de la simplification de l'autorisation étatique. À droit constant restent la transmission universelle du patrimoine dans son état à la réalisation définitive et la dissolution sans liquidation par fusion. Les mesures d'office de L. 421-6 et L. 423-1 ne sont pas abrogées implicitement. Le corps antérieur de réforme est conservé intégralement, sans nouvelle retouche stylistique ni allègement additionnel revendiqué par rapport à ce brouillon."""
out['review_notes'] = """Source entière, notes vides, précédent brouillon entier et SRU 146 entier relus. Les trois alinéas initiaux demeurent dans leur ordre, suivis des garanties et de la transition. Lecture entière des sources locales de L. 421-1, L. 421-6, L. 421-6-1, L. 423-1, R. 421-1 et R. 421-1-1. R. 421-1 doit être coordonné matériellement pour les seules décisions volontaires : retirer les décrets, demandes et arrêtés d'autorisation, les avis régionaux correspondants, les délais préfectoraux de trois mois et leurs rejets implicites ; remplacer, pour le délai d'un mois de désignation des représentants des locataires en fusion, la publication de l'arrêté par la publicité de la décision locale exécutoire. Le délai d'un mois, le mandat des représentants, les autres renouvellements de gouvernance, la publicité et les consultations utiles demeurent. La nomination du liquidateur et les règles budgétaires, comptables et patrimoniales de dissolution ne sont pas abolies : la fin de l'autorisation ne signifie ni extinction du passif ni suppression de la liquidation hors fusion. Les règles autonomes de L. 421-6, dont les rattachements et fusions d'office, et leur exécution par R. 421-1-1 ne sont pas présentées comme simplifiées ici. Les contrats, garanties, gratuités et exonérations historiques de L. 421-6-1 Lyon/Rhône restent applicables ; aucune échéance de 2015-2016 n'est rouverte et aucune créance antérieure n'est anéantie. L'articulation du caractère exécutoire avec le CGCT reste à rédiger hors des cinq codes, notamment ses règles communales, départementales et propres à l'établissement de rattachement : aucune nouvelle demande ni transmission spéciale n'est créée dans le présent article. Les dispositions réglementaires et le CGCT ne sont pas déclarés réécrits. SRU 146 réécrivait les anciens L. 421-2 et L. 421-4 ; le L. 421-7 de 2007 ajoute notamment les effets de fusion. La concordance historique intégrale n'est pas fournie et la filiation partielle reste signalée, sans achèvement du volet SRU 146 ni des 209 articles."""
out['benefit_review'] = """La fusion volontaire et ses avantages de continuité sont préservés pour les futures opérations : dissolution sans liquidation et transmission universelle du patrimoine, sans perte des contrats, garanties, créances ou droits des locataires et personnels. La réforme n'abolit ni les aides attachées aux actifs sociaux ni les gratuités et exonérations historiques distinctes de L. 421-6-1. Les organes locaux peuvent utiliser les consultations déjà accomplies sans nouveau dépôt. Aucun avantage n'est limité aux seules opérations antérieures, sous réserve des régimes historiques qui avaient déjà leur période propre."""
out['substantive_impact'] = impact(
    'material_reduction',
    "Par rapport à la source officielle entière, une autorisation étatique intervenant après l'initiative locale disparaît pour les décisions volontaires d'organisation de l'office ; la délibération locale devient la décision. Ce changement est déjà contenu dans le précédent brouillon, maintenu après examen ; aucune nouvelle réduction n'est ajoutée ni aucun prélèvement supprimé.",
    "Le dispositif ne supprime pas les décisions d'office ni les contrôles de légalité, consultations, publicité, règles de liquidation ou droits des tiers. R. 421-1 et les dispositions pertinentes du CGCT restent à coordonner matériellement ; le coût administratif net et le solde global des codes ne sont pas chiffrés.",
    "Aucune charge nouvelle n'est identifiée : les délibérations et la concordance expriment la décision des organes déjà demandeurs ; publicité, transmission de droit commun et consultations restent celles nécessaires aux actes publics. Aucun dossier spécial, registre, déclaration ou délai d'attente de remplacement n'est institué.",
    [effect(
        'authorization_removed', 'oph-decisions-volontaires-fin-autorisation-etat',
        "Suppression du circuit d'autorisation de l'Etat pour les décisions volontaires d'organisation des offices, sans compter chaque type de décision comme une réduction distincte.",
        "Création ou dissolution sur demande locale par décret ; changement de rattachement ou d'appellation et fusion sur demande locale prononcés par le préfet, avec les circuits d'avis et de décision de R. 421-1.",
        "Délibération locale exécutoire, concordante lorsque plusieurs organes sont compétents ; aucun décret de création ou de dissolution, arrêté préfectoral d'autorisation, avis régional ni demande de remplacement pour ces décisions volontaires.",
        'legal_duty', "Collectivités et établissements publics de rattachement et offices concernés par une création, une dissolution volontaire, une modification volontaire ou une fusion.",
        "Décisions prises dès l'entrée en vigueur ; procédures en cours achevables selon le nouveau régime sans refaire les consultations ; actes antérieurs, contrats et droits préservés ; exceptions d'office maintenues.",
        "Pas d'autorisation ou déclaration nouvelle ; publicité, contrôle de légalité, consultations utiles et recours maintenus.",
        "Le changement de collectivité territoriale ou d'établissement public de rattachement d'un office, le changement de son appellation, ainsi que la fusion de plusieurs offices sont prononcés par le préfet sur demande des organes délibérants des collectivités territoriales et des établissements publics intéressés, dans des conditions définies par décret en Conseil d'Etat.",
        "Les décisions volontaires prévues aux premier et troisième alinéas ne nécessitent ni décret de création ou de dissolution, ni arrêté préfectoral, ni avis du comité régional compétent en matière d'habitat.",
    )],
)


# L421-23 : remplacer les anciens renvois par leur objet statutaire, sans numéro inventé.
src, out = sources[3], answers[3]
out['proposed_xml'] = "<p>Pour la gestion des agents de l'office relevant du statut de la fonction publique territoriale, en activité dans l'office ou placés dans l'une des autres positions prévues par ce statut, le conseil d'administration de l'office constitue l'assemblée délibérante et le directeur général, l'autorité territoriale.</p>"
out['reason'] = """Coordination des renvois statutaires anciens, sans réforme des compétences ni réduction matérielle revendiquée. Le précédent brouillon reproduisait les références à la loi de 1984 et à l'article 12 bis de celle de 1983 tout en signalant leur codification. Le nouveau corps désigne directement le statut de la fonction publique territoriale et toutes ses positions, sans inventer un numéro du code général de la fonction publique absent des pièces. À droit constant, le conseil d'administration reste l'assemblée délibérante et le directeur général l'autorité territoriale pour les mêmes agents, en activité ou dans les autres positions. Après examen, cette attribution est nécessaire pour identifier les autorités de carrière, de rémunération et de position statutaire dans un office ; sa suppression ne retirerait aucune taxe, déclaration ou autorisation de l'agent et rendrait les décisions incertaines. Aucun nouveau contrat privé ni préavis ou barème de rupture n'est étendu à ces agents publics. Cette modification corrige un renvoi matériel ; elle n'est pas une réécriture stylistique comptée comme simplification."""
out['review_notes'] = """Source entière, notes vides, précédent brouillon entier et SRU 148 entier examinés. Le seul alinéa conserve son objet et les deux autorités, sans réduire les positions aux agents en activité ni aux situations passées. Les références anciennes à la loi n° 84-53 du 26 janvier 1984 et à l'article 12 bis de la loi n° 83-634 du 13 juillet 1983 sont remplacées par une désignation matérielle du statut territorial et de ses positions. Aucun nouveau renvoi numéroté n'est introduit ; le code général de la fonction publique et ses tables ne sont pas fournis dans le corpus autorisé, ce qui limite la vérification de concordance extérieure et reste à contrôler. Le présent article attribue les compétences sans réédicter le contenu de ce statut ni celui de ses positions. Les sources locales intégrales de L. 421-24 et L. 421-25 ont été lues : accords des personnels hors fonction publique territoriale et droit syndical gardent leur régime propre. Le contrat privé unique, les quinze jours, la notification et la condition d'ancienneté de son indemnité ordinaire n'ont pas à être ajoutés à cette disposition publique. SRU 148 concernait l'ancien article 120 IV de la loi de 1984, le maintien de la qualité de fonctionnaire, les avancements et les changements de cadre d'emplois lors de transformations d'offices ; il n'établit pas la filiation complète de cette seule règle d'autorité. Ces droits favorables ne sont pas supprimés, et ni SRU 148 ni l'ensemble des 209 articles ne sont déclarés achevés. La coordination externe de codification n'est pas présentée comme un code supplémentaire réécrit."""
out['benefit_review'] = """Aucun prélèvement ni exonération fiscale n'est institué par cette règle de compétence. L'identification des deux autorités permet l'exercice des droits statutaires des agents territoriaux en activité et dans les autres positions, sans fermeture aux situations futures. Les avantages de carrière, avancements, changements de cadre et conservation de la qualité de fonctionnaire évoqués dans SRU 148 restent distincts et ne sont pas abrogés. Le remplacement des références anciennes n'instaure ni ancienneté minimale ni limitation aux agents déjà présents."""
out['substantive_impact'] = impact(
    'coordination_only',
    "La proposition conserve la répartition de compétences de la source entière et substitue l'objet statutaire aux références législatives anciennes signalées par le précédent brouillon. Elle ne supprime ni taxe ni obligation de l'agent et n'est pas comptée comme une baisse de charge ou une simplification matérielle.",
    "Les règles de carrière, la liste et les effets des positions statutaires ne sont pas réécrits ; les tables de codification de la fonction publique ne sont pas fournies pour une concordance extérieure complète. La filiation SRU reste partielle et aucun solde net de complexité de l'ensemble des codes n'est établi.",
    "Aucune charge nouvelle n'est identifiée : aucun acte, registre, donnée, notification, justificatif ou délai n'est ajouté. La désignation du statut et de ses positions ne fait que conserver l'attribution existante aux deux autorités, sans condition supplémentaire pour les agents publics.",
    [effect(
        'coordination', 'oph-competences-gestion-agents-territoriaux',
        "Coordination matérielle de la désignation du statut des agents publics et de leurs positions, sans modifier les autorités compétentes.",
        "L'attribution des compétences vise les agents relevant de la loi de 1984 et les positions énumérées à l'article 12 bis de la loi de 1983, sous des références anciennes.",
        "La même attribution vise directement les agents relevant du statut de la fonction publique territoriale, en activité ou dans ses autres positions, sans nouveau numéro externe ni extension au contrat privé.",
        'other', "Agents des offices relevant du statut de la fonction publique territoriale, dans toutes les positions statutaires concernées.",
        "Coordination sans modification des droits passés ou futurs, de l'ancienneté, des positions ni des compétences du conseil et du directeur général.",
        "Aucun régime, dossier ou contrôle de remplacement n'est créé ; les autorités continuent d'exercer leurs attributions statutaires.",
        "Pour la gestion des agents relevant de la loi n° 84-53 du 26 janvier 1984",
        "Pour la gestion des agents de l'office relevant du statut de la fonction publique territoriale",
    )],
)


assert len(answers) == len(sources) == 4
for src, out in zip(sources, answers):
    assert all(out[k] == src[k] for k in ['code_id', 'source_id', 'source_sha256', 'number'])
    req = references['requirements'][src['code_id'] + '|' + src['source_id']]
    assert [r['target_key'] for r in out['reference_checks']] == req
    for ref in out['reference_checks']:
        assert ref['view_sha256'] == references['targets'][ref['target_key']]['view_sha256']
        assert len(ref['assessment']) >= 80
    si = out['substantive_impact']
    for k in ['assessment', 'scope_limitations', 'new_burdens_review']:
        assert len(si[k]) >= 40
    for e in si['effects']:
        assert len(e['source_quote']) >= 12 and e['source_quote'] in text(src['source_xml'])
        assert len(e['proposed_quote']) >= 12 and e['proposed_quote'] in text(out['proposed_xml'])
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', e['measure_id'])
        assert 6 <= len(e['measure_id']) <= 96
    if src['benefit_check_required']:
        assert len(out['benefit_review']) >= 100
    for provision in out.get('removed_provisions', []):
        assert len(provision) >= 30

(ROOT / 'answer.json').write_text(json.dumps(answers, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'output_file': 'answer.json', 'article_count': len(answers)}, ensure_ascii=False))
