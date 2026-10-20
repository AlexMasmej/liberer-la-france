import json
import re
import html
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
by_number = {a['number']: a for a in sources}
answer = {}


def plain(xml):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]*>', ' ', xml or ''))).strip()


def paragraphs(*texts):
    return ''.join('<p>' + html.escape(t, quote=False) + '</p>' for t in texts)


def effect(kind, measure_id, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit,
                affected_population=population, conditions_and_transition=transition,
                replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


def entry(number, reason, notes, assessment, limitations, burdens,
          xml=None, classification='retained_necessary', effects=None,
          change_type=None, removed=None, repeal_scope=None):
    a = by_number[number]
    out = {k: a[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    out.update(proposed_xml=xml, reason=reason, review_notes=notes,
               status='retained_unchanged' if xml is None else 'rewrite_draft')
    if xml is None:
        out['classification'] = 'retained_necessary'
    out['substantive_impact'] = dict(version=1, classification=classification,
        assessment=assessment, scope_limitations=limitations,
        new_burdens_review=burdens, effects=effects or [])
    if change_type:
        out['change_type'] = change_type
        if change_type == 'full_repeal':
            out['repeal_policy_id'] = 'editorial_direction_2026_10_19'
            out['repeal_scope'] = repeal_scope
        else:
            out['reform_policy_id'] = 'editorial_direction_2026_10_19'
            out['removed_provisions'] = removed
    answer[number] = out
    return out


no_new_retained = "Aucune charge nouvelle n'est identifiée : le texte officiel est maintenu sans ajout de pièce, de déclaration, de délai ou de condition d'accès. Aucun solde de l'ensemble des codes n'est chiffré."

# Suppression des exclusions de la prime, avec maintien des conditions ordinaires.
prime_measure = 'prime-demenagement-fin-exclusions-territoriales'
for number, territory in [('L861-4', 'Mayotte'), ('L863-2', 'Saint-Pierre-et-Miquelon')]:
    xml = paragraphs(
        "Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant l'exclusion territoriale des primes de déménagement.",
        f"Les articles L. 821-4 et L. 823-8 sont applicables à {territory} pour les déménagements intervenant à compter de cette date. Les conditions d'ouverture du droit, le calcul de la prime et la déduction des autres aides couvrant les mêmes frais restent applicables. La différence prévue à l'article L. 821-4 demeure due lorsque ces autres aides sont inférieures à la prime.",
        "Les déménagements antérieurs demeurent régis par les dispositions applicables à leur date. Les droits régulièrement ouverts, les créances, les restitutions, les prescriptions et les recours antérieurs sont conservés ; aucune réouverture générale des périodes antérieures n'est instituée.")
    source_quote = plain(by_number[number]['source_xml'])
    proposed_quote = f"Les articles L. 821-4 et L. 823-8 sont applicables à {territory} pour les déménagements intervenant à compter de cette date."
    notes = ("Réforme de fond fondée sur cuts_and_reliefs : retrait d'une exclusion géographique, sans suppression de l'anti-cumul ni de son complément différentiel. L823-8 et L821-4 ont été lus dans leur intégralité ; le premier définit la prime et le second le non-cumul avec versement de la différence. D823-20 et D823-22 conservent notamment les trois enfants, la période liée à la grossesse et au deuxième anniversaire, les six mois d'ouverture du droit et les frais réels plafonnés. Aucun montant de prime n'est inventé. La dépense supplémentaire et le coût de gestion restent à évaluer, sans recette de compensation présumée. Les contrats de travail et leurs indemnités ne sont pas le fait générateur de cette aide.")
    if number == 'L861-4':
        notes += " R861-2 confie déjà la gestion des aides à la caisse compétente à Mayotte ; son champ et R823-1 devront viser expressément le paiement de la prime dans cette adaptation. Cette coordination réglementaire hors lot n'est pas présentée comme rédigée."
    else:
        notes += " La note de 2019 fixe au 1er janvier 2022 le début d'application de l'ancien dispositif ; elle ne fixe pas la date de la réforme. R863-6 1° et R863-11 1° a et 3° a, lus intégralement, doivent être coordonnés pour inclure paiement et recours de la prime ; les exclusions procédurales ne peuvent neutraliser l'ouverture législative proposée. R863-1 confirme l'organisme local de gestion. Ces règlements ne sont pas modifiés dans ce lot."
    entry(number,
        f"Réforme de fond : suppression de l'exclusion des primes de déménagement à {territory}. Cette restriction territoriale ne protège ni la sécurité du logement ni l'absence de double remboursement, déjà garanties par les conditions ordinaires et l'article L821-4. Le droit est ouvert aussi aux futurs ménages éligibles, sans modifier les autres critères ni les anciens dossiers.",
        notes,
        f"La source excluait intégralement les primes à {territory} ; la proposition retire cette exclusion pour les nouveaux déménagements. Il s'agit de l'extension d'une aide existante, non d'une baisse de taxe ni d'une économie publique démontrée.",
        "L'extension n'est pas rétroactive et ne supprime ni les conditions familiales ni les plafonds. Les adaptations réglementaires de gestion et de recours restent à coordonner ; la dépense et le coût public net ne sont pas établis.",
        "Aucune nouvelle pièce, aucun registre ni nouveau délai n'est imposé aux ménages. Les organismes devront traiter les demandes désormais éligibles et payer les primes dues : cette extension de leur charge de gestion et de financement reste non chiffrée ; aucune procédure supplémentaire n'est créée.",
        xml=xml, classification='mixed', change_type='full_repeal',
        repeal_scope=f"Suppression pour les déménagements futurs de l'exclusion territoriale de la prime de déménagement à {territory}, sous les conditions ordinaires et sans rétroactivité générale.",
        effects=[effect('relief_extended', prime_measure,
            f"Ouverture de la prime de déménagement aux ménages éligibles à {territory} par retrait de l'exclusion territoriale.",
            f"Exclusion de L821-4 et L823-8 à {territory}, même lorsque les conditions ordinaires de la prime étaient remplies.",
            f"Application de la prime à {territory} aux déménagements futurs, sous conditions familiales, de logement, de frais plafonnés et de non-cumul inchangées.",
            'regime', f"Personnes et ménages déménageant à {territory} et remplissant les conditions ordinaires de la prime.",
            "Déménagements à compter de l'entrée en vigueur ; situations antérieures soumises à leur droit propre ; aucun rattrapage général.",
            "Pas de déclaration de remplacement ; nouvelles demandes et dépense de prime à gérer dans le dispositif existant, coût non établi.",
            source_quote, proposed_quote)])

entry('L861-5',
    "Maintien nécessaire des cinq adaptations mahoraises : rattachement aux prestations locales, neutralisation patrimoniale pour le handicap, maintien temporaire de l'aide en cas de surpeuplement familial, dispense concernant les enfants à charge et cadre local de récupération des indus. Supprimer ces substitutions rendrait les avantages inopérants ou retirerait des garanties. Aucun agrément ni justificatif répété n'est prescrit par cet article.",
    "Les cinq numéros et les deux phrases du L822-10 adapté restent entiers. L822-5, L823-1 et L823-9 ont été lus : les renvois concernent respectivement les ressources, le calcul familial et les indus. Les cibles CSS L821-1 et L553-2 ne se substituent pas automatiquement aux ordonnances locales que cet article rend applicables. La source porte ABROGE_DIFF au 1er janvier 2028 ; ce maintien ne prolonge pas sa validité ni ne réécrit le futur régime. La note de 2020 vise le 1er mai 2021, sans rapport avec l'entrée en vigueur d'une réforme nouvelle. Les ordonnances mahoraises extérieures au corpus ne sont pas présentées comme réécrites ; aucune nouvelle obligation issue de ces textes n'est supposée.",
    "Les adaptations locales et leurs dérogations restent intégralement applicables pendant la validité de l'article. Aucune réduction nouvelle n'est revendiquée pour cette simple conservation d'avantages et de garanties de recouvrement.",
    "L'article n'harmonise pas le régime de Mayotte avec celui de métropole et ne statue pas sur les règles applicables à partir de 2028. Les taux et procédures des ordonnances extérieures ne sont pas modifiés.",
    no_new_retained)

entry('L861-5-1',
    "Maintien nécessaire du fondement territorial d'accès des logements-foyers conventionnés à l'APL. La convention assure la contrepartie sociale de l'aide ; l'article n'ajoute ni autorisation d'exploiter ni dossier distinct. Supprimer cette adaptation pourrait refermer le régime plus favorable que le 5° ordinaire de L831-1.",
    "L831-1 a été lu intégralement : son 5° ordinaire exige une assimilation aux catégories 2° et 3° et des conventions déterminées, alors que l'adaptation couvre les logements-foyers conventionnés dans les cinq territoires cités. R861-20 précise ce dispositif, avec ses conditions propres de décence et de financement ; il ne s'agit pas d'un quota SRU. Ne pas retirer cette ouverture pour les conventions futures éligibles. Aucun lien avec un terme d'emploi ou avec l'IS à la distribution.",
    "Conservation intégrale de l'ouverture territoriale de l'APL aux logements-foyers conventionnés ; aucune suppression de taxe ou de formalité nouvelle n'est comptabilisée.",
    "L'accès reste subordonné à la convention et aux règles réglementaires propres aux foyers ; aucun élargissement automatique à des logements non conventionnés n'est démontré.",
    no_new_retained)

entry('L861-6',
    "Maintien nécessaire des catégories bénéficiaires adaptées et de leurs droits familiaux : enfants à charge, régimes agricoles, handicap, apprentissage et formation, situations mahoraises de statut civil ancien. La dérogation favorable d'accession attachée aux financements décidés avant fin 2018 et aux prêts signés avant fin 2019 reste protégée. Ces conditions désignent les bénéficiaires et ne constituent pas des autorisations ou déclarations doublonnées.",
    "L841-1 a été lu en entier : les 3°, 4° et 5° y désignent les jeunes ménages, ascendants et personnes handicapées, ce qui concorde avec le a) de la source. Le b) renvoie à l'allocation mahoraise dans une adaptation couvrant cinq territoires : cette portée rédactionnelle préexistante doit être contrôlée lors du raccordement prévu en 2028 ; elle n'est pas étendue par une correction silencieuse. L'apprentissage et le stage visent la situation de l'enfant, pas un CDD obligatoire : les phases pédagogiques d'un contrat unique restent éligibles aux conditions de ressources et d'âge. Le maintien ne rouvre pas les prêts au-delà des dates de 2017/2019 et ne transforme pas la date historique en date future de réforme. La source porte ABROGE_DIFF au 1er janvier 2028, échéance non modifiée.",
    "La source entière est conservée, y compris les droits des enfants en formation et l'exception historique d'accession. Ni nouvelle baisse de prélèvement ni nouvelle simplification n'est alléguée.",
    "Les prêts futurs hors des fenêtres légales ne sont pas réouverts. Les règlements d'âge et de ressources ainsi que le raccordement de 2028 demeurent distincts ; l'emploi public n'est pas soumis au contrat privé par cet article.",
    no_new_retained)

entry('L861-7',
    "Maintien nécessaire de la dispense mahoraise de conservation des allocations par le payeur. Abroger cette exclusion ferait revenir une contrainte et pourrait interrompre des versements favorables ; ce serait contraire à la préservation des dérogations. Les obligations autonomes de décence et de sécurité des logements demeurent, sans être abolies par cette dispense procédurale.",
    "Les sept références L843-1 à L843-7 sont conservées. La dispense ne constitue ni une exonération générale du bailleur de ses devoirs de décence ni une autorisation de louer un logement dangereux. R861-11 reprend l'adaptation réglementaire ; aucun nouveau signalement ni justificatif n'est proposé.",
    "La dispense territoriale existante est maintenue pour les situations futures éligibles. La conservation d'un avantage déjà en vigueur ne produit pas de réduction nouvelle à compter.",
    "Les protections indépendantes contre l'insalubrité et les obligations civiles du bailleur restent à leur champ propre ; leur suppression n'est pas décidée ici.",
    no_new_retained)

xml = paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant l'exclusion professionnelle de l'allocation de logement à Mayotte.",
    "Pour les périodes de droit à compter de cette date, le bénéfice de l'allocation de logement à Mayotte ne peut être refusé à un magistrat ou à un fonctionnaire civil ou militaire de l'Etat au seul motif que le centre de ses intérêts matériels et familiaux est situé hors de Mayotte. Les autres conditions d'ouverture et de calcul du droit demeurent applicables.",
    "Les périodes de droit antérieures restent soumises aux dispositions qui leur étaient applicables. Les droits régulièrement ouverts, les créances, les restitutions, les prescriptions et les recours relatifs à ces périodes sont conservés ; aucune réouverture générale des droits antérieurs n'est instituée.")
entry('L861-8',
    "Réforme de fond : retrait de l'exclusion automatique des agents de l'Etat dont le centre des intérêts matériels et familiaux est extérieur à Mayotte. Les conditions ordinaires de ressources et de logement suffisent à cibler cette aide ; la source ne démontre pas que ce critère de statut protège la sécurité ou constitue un contrôle indispensable. Le régime de l'emploi public n'est pas modifié.",
    "L'abrogation porte sur l'exclusion entière, sans supprimer une aide existante ni accorder une dispense générale des ressources ou de la résidence. Le traitement des logements fournis et des autres avantages demeure celui des règles ordinaires, sans cumul supplémentaire créé par cet article. La dépense nouvelle potentielle et les adaptations des formulaires doivent être évaluées, sans montant ni financement inventés. La réforme du contrat unique de droit privé est inapplicable aux fonctions et statuts publics cités.",
    "La source refusait l'allocation en raison du seul statut professionnel associé au centre des intérêts situé hors de Mayotte ; cette exclusion disparaît pour les périodes nouvelles. Le gain est une ouverture d'éligibilité, sans baisse de taux ni économie publique démontrée.",
    "Les autres conditions d'aide, notamment ressources et logement, subsistent. Aucune rétroactivité générale ni évaluation du nombre d'agents effectivement éligibles ou du coût public n'est établie.",
    "Aucune nouvelle déclaration ni nouvelle pièce n'est créée pour les agents. La caisse devra traiter les situations nouvellement éligibles et payer les droits ouverts ; l'effet sur sa gestion et les finances publiques reste à mesurer.",
    xml=xml, classification='mixed', change_type='full_repeal',
    repeal_scope="Suppression pour les périodes nouvelles de l'exclusion de l'allocation de logement visant les magistrats et fonctionnaires de l'Etat dont les intérêts matériels et familiaux sont hors de Mayotte.",
    effects=[effect('relief_extended', 'mayotte-allocation-fin-exclusion-agents-etat',
        "Suppression du critère professionnel et territorial excluant certains agents de l'Etat de l'allocation de logement.",
        "Exclusion à Mayotte des magistrats et fonctionnaires civils ou militaires de l'Etat lorsque leur centre des intérêts matériels et familiaux est extérieur au territoire.",
        "Accès de ces agents selon les conditions ordinaires d'aide pour les périodes de droit nouvelles, sans exclusion sur ce seul motif.",
        'regime', "Magistrats et fonctionnaires civils et militaires de l'Etat relevant de l'exclusion mahoraise.",
        "Périodes de droit à compter de l'entrée en vigueur ; anciennes périodes et leurs recours conservés.",
        "Aucune formalité de remplacement ; dépense et charge de traitement des droits nouveaux non chiffrées.",
        plain(by_number['L861-8']['source_xml']),
        "le bénéfice de l'allocation de logement à Mayotte ne peut être refusé à un magistrat ou à un fonctionnaire civil ou militaire de l'Etat au seul motif que le centre de ses intérêts matériels et familiaux est situé hors de Mayotte.")])

entry('L861-9',
    "Maintien nécessaire du cadre légal des échanges fiscaux utiles au calcul et au contrôle des aides à Mayotte. Ce renvoi autorise des échanges encadrés et n'impose pas de déclaration périodique supplémentaire au ménage. Sa disparition n'abolirait pas une taxe et pourrait renvoyer la collecte des ressources sur les demandeurs.",
    "L851-1 a été lu : il privilégie l'obtention des informations par les organismes et ne recourt au demandeur qu'à défaut. L'adaptation conserve les deux plages exactes L97 à L99 et L152 à L162 B du LPF ; elle n'ouvre aucun accès nouveau ni ne lève les secrets au-delà des bases légales. Le LPF extérieur au corpus ne fait pas l'objet d'une réécriture ni d'une vérification exhaustive dans ce lot.",
    "Le renvoi territorial d'accès légal à l'information est conservé intégralement, sans nouvelle collecte ni allègement fiscal revendiqué.",
    "Les modalités précises du LPF et les habilitations d'accès restent celles des textes compétents ; aucune économie de saisie ou suppression d'une formalité supplémentaire n'est démontrée.",
    no_new_retained)

# Une seule mesure FNAL : ces deux articles n'en sont que l'exécution territoriale.
fnal_measure = 'contribution-allocation-logement-sociale-suppression'
old_fnal = "Les dispositions du présent article dans leur rédaction antérieure demeurent applicables aux revenus d'activité afférents aux périodes antérieures à cette date, y compris lorsque leur liquidation, leur paiement, leur recouvrement ou leur régularisation intervient après cette date. Les exonérations, réductions, dispenses, remises, imputations, restitutions, prescriptions, garanties et voies de recours applicables à ces revenus sont conservées. Il n'est institué ni restitution générale des sommes légalement dues ni double imputation ou double remboursement."
for number, territory in [('L862-1', 'Saint-Barthélemy et Saint-Martin'), ('L863-1', 'Saint-Pierre-et-Miquelon')]:
    xml = paragraphs(
        "Le présent article est abrogé pour les revenus d'activité afférents aux périodes d'activité courant à compter de l'entrée en vigueur de la loi supprimant la contribution relative à l'allocation de logement sociale.",
        f"Aucune contribution prévue à l'article L. 813-4 ne peut être appelée à {territory} sur les revenus exclus de cette contribution par ce même article. Pour une période d'activité comprenant cette date, seuls les revenus afférents à sa partie antérieure restent soumis à la contribution.",
        old_fnal,
        "Aucune déclaration, donnée ou formalité exclusivement liée à cette contribution n'est exigée pour les revenus qui en sont exclus. Les obligations communes nécessaires aux autres prélèvements demeurent applicables, sans dépôt distinct au seul titre de la contribution supprimée.",
        "Les droits aux aides personnelles au logement et aux primes de déménagement ainsi que les exonérations, réductions et dispenses portant sur les autres prélèvements restent applicables, y compris aux situations futures éligibles. Aucune taxe de remplacement ni créance correspondant à une contribution fictive n'est instituée.")
    source_quote = ("Le recouvrement de la contribution prévue à l'article L. 813-4 est assuré :" if number == 'L862-1'
        else plain(by_number[number]['source_xml']))
    notes = ("Coordination de la proposition actuelle L813-4, lue intégralement avec sa source et ses notes, et non affirmation du droit en vigueur : cette proposition éteint la contribution pour les périodes d'activité nouvelles. L813-5 à L813-7 ont également été lus. Même mesure contribution-allocation-logement-sociale-suppression, sans seconde taxe supprimée ni taux autonome attribué à l'adaptation. Les déclarations communes, les anciennes dettes et leurs garanties demeurent. La perte de recettes est celle du dispositif FNAL, non une économie territoriale supplémentaire ; financement et solde public consolidé non établis. Le champ des salariés, agricoles ou non, n'est pas limité aux nouveaux contrats privés.")
    if number == 'L862-1':
        notes += " Le 2° relatif aux règles fiscales locales, inclus dans la seule section de la contribution, est conservé pour les anciennes périodes par la clause de survie. Il n'a plus d'objet autonome pour les périodes exemptes du prélèvement ; aucun impôt local distinct n'est aboli. Les deuxième et troisième alinéas de CSS L752-1 continuent seulement à désigner l'ancien recouvrement dans le champ de cette contribution. Leur texte n'est pas une cible fournie ici et n'est pas inventé ; les autres fonctions éventuelles de ces alinéas ne sont pas retirées."
    else:
        notes += " L'attribution à la caisse de prévoyance sociale reste acquise pour les revenus des périodes antérieures. La note de l'ordonnance de 2019 vise les contributions et prestations dues depuis le 1er janvier 2022, non une date d'extinction. R863-2 5°, lu, doit être coordonné pour le recouvrement futur ; ses autres règles de financement des aides restent distinctes."
    entry(number,
        "Coordination nécessaire de la suppression proposée de la contribution d'allocation de logement sociale : l'attribution territoriale de son recouvrement cesse pour les périodes nouvelles. La règle ancienne demeure entière pour les revenus des périodes antérieures, même encaissés tardivement. Il ne s'agit ni d'une seconde abolition de prélèvement ni d'une suppression des aides.",
        notes,
        f"Le mécanisme territorial de recouvrement à {territory} est limité au stock ancien, en cohérence avec L813-4 proposé. Cet article ne produit pas une baisse supplémentaire de taux ou d'assiette indépendante de la mesure FNAL.",
        "Coordination tributaire de l'adoption de la suppression de L813-4 ; aucune modification autonome des autres prélèvements, des anciennes périodes ou du financement public des aides n'est démontrée. Les règlements et déclarations communs restent à coordonner dans leur champ propre.",
        "Aucune charge nouvelle n'est identifiée : pas de cotisation de remplacement ni de déclaration distincte nouvelle. Les opérations et garanties de l'ancien recouvrement subsistent ; les obligations communes déjà nécessaires aux autres prélèvements sont conservées sans création de données.",
        xml=xml, classification='coordination_only', change_type='full_repeal',
        repeal_scope=f"Extinction prospective du recouvrement territorial de la seule contribution d'allocation de logement sociale à {territory}, avec survie complète du régime des périodes antérieures.",
        effects=[effect('coordination', fnal_measure,
            "Retrait du fondement de recouvrement territorial pour les revenus des périodes nouvelles, accessoire de la suppression unique de la contribution FNAL.",
            f"Adaptation du recouvrement de la contribution L813-4 à {territory} sans exclusion des périodes futures dans la source.",
            "Aucun appel de la contribution pour les périodes nouvelles ; anciens revenus, exonérations et recours conservés, quelle que soit la date de recouvrement.",
            'legal_duty', f"Employeurs et organismes de recouvrement de {territory} dans le champ de L813-4.",
            "Coupure par période d'activité, avec ventilation de la seule période chevauchant l'entrée en vigueur ; pas par date de paiement.",
            "Aucune obligation de remplacement ni taxe locale ou sociale nouvelle ; formalités communes maintenues pour les autres prélèvements.",
            source_quote, f"Aucune contribution prévue à l'article L. 813-4 ne peut être appelée à {territory} sur les revenus exclus de cette contribution par ce même article.")])

for number, territory, adjective in [('L862-2', 'Saint-Barthélemy et Saint-Martin', 'définies'), ('L863-3', 'Saint-Pierre-et-Miquelon', 'fixées')]:
    entry(number,
        f"Maintien nécessaire des cinq adaptations des aides à {territory} : neutralisation des aides dans les ressources sociales, référence fiscale locale, décence, six assimilations favorables aux loyers et indexation sur l'indice local ou, à défaut, métropolitain. Les équivalences de prêts, location-accession et charges particulières rendent les aides accessibles sans nouvelle autorisation. Les exigences de décence protègent la santé des occupants.",
        "L821-8, L822-9 et la cible L823-3 ont été lus intégralement. Les six catégories locales de charges sont conservées, y compris les rémunérations de redressement de copropriété, indemnités d'expropriation, redevances et accueil familial. La substitution du 1° laisse à la fiscalité locale le traitement fiscal, sans introduire un impôt français nouveau. Le 5° conserve l'alternative d'indice et les paramètres de L823-4, sans les confondre avec un taux fiscal. Les références aux travaux, aux contrats de location-accession et aux opérations d'un opérateur ne sont pas des renvois à des CDD. " + ("La note d'application au 1er janvier 2022 reste une règle historique ; aucune date de réforme future n'en est déduite." if number == 'L863-3' else "Aucune obligation de quota, rattrapage ou carence SRU n'est réintroduite."),
        f"La totalité du régime territorial à {territory} est conservée, avec ses exclusions favorables de ressources et ses six assimilations aux loyers. Ce maintien ne compte pas comme une simplification nouvelle.",
        "Ni le barème des aides ni la fiscalité locale ne sont réformés ici. La décence et les conditions de chaque charge assimilée demeurent ; le solde national de coût ou de complexité n'est pas établi.",
        no_new_retained)

# Rectification ciblée d'une contradiction interne de numérotation.
src = by_number['L862-3']['source_xml']
old = "les 2°, 3° et 5° deviennent respectivement, les 1°, 2° et 3°"
new = "les 3°, 4° et 5° deviennent respectivement les 1°, 2° et 3°"
assert old in src
xml = src.replace(old, new)
entry('L862-3',
    "Coordination nécessaire, sans allègement fiscal nouveau : rectification du a), qui prétendait renuméroter le 2° tout en l'abrogeant. Les 3°, 4° et 5° de L841-1 désignent réellement les trois catégories survivantes ; leur renumérotation devient cohérente. Toutes les catégories ajoutées, conditions d'enfant à charge et règles de L843-7 restent intégralement reproduites. Il ne s'agit pas d'une reformulation stylistique.",
    "Incohérence préexistante explicitement constatée après lecture intégrale de L841-1 : le 2° est supprimé par la même phrase et ne peut devenir le nouveau 1° ; le 4° concernant l'ascendant était omis. La correction suit 3°/4°/5°, cohérente aussi avec L861-6, sans supprimer une catégorie utile. L'apprentissage visé à l'alinéa final du b) est une situation pédagogique ouvrant potentiellement le droit ; il inclut les phases éligibles des contrats uniques nouveaux sans imposer un CDD ou un terme à l'emploi. Les anciens contrats et autres conditions d'âge, rémunération, maladie et handicap restent à leur champ. Le renvoi du 2° à L843-7 conserve sa portée locale d'opérations, sans quota SRU. La source annonce ABROGE_DIFF au 1er janvier 2028 : cette correction ne prolonge pas le dispositif après cette date.",
    "La seule modification est la correction d'une discordance de renumérotation empêchant la lecture cohérente des catégories bénéficiaires. Les autres mots et conditions de la source entière sont conservés ; aucune deuxième mesure de contrat unique n'est comptée.",
    "L'article ne crée pas de nouvelle catégorie d'allocation, ne réforme pas le contrôle de décence et ne modifie pas la fin de validité annoncée en 2028. Le raccordement futur demeure distinct.",
    "Aucune charge nouvelle n'est identifiée : la correction n'exige ni dossier ni notification supplémentaires et ne change aucune condition d'ancienneté d'emploi ou de ressources.",
    xml=xml, classification='coordination_only',
    effects=[effect('coordination', 'allocation-logement-outre-mer-numerotation-coherente',
        "Rectification de la numérotation contradictoire des catégories survivantes de L841-1, sans suppression de bénéficiaire.",
        "Le a) abroge les 1°, 2° et 6° mais prétend renuméroter les 2°, 3° et 5°, en omettant le 4°.",
        "Le a) abroge toujours les 1°, 2° et 6° et renumérote les 3°, 4° et 5° ; les catégories ajoutées et conditions demeurent.",
        'other', "Bénéficiaires des allocations de logement à Saint-Barthélemy et Saint-Martin.",
        "Correction pendant la validité de l'article, sans modifier son abrogation différée au 1er janvier 2028 ni supprimer des droits valablement ouverts.",
        "Aucun dépôt, aucune information ou formalité supplémentaire.", old, new)])

for number, territory in [('L862-4', 'Saint-Barthélemy et Saint-Martin'), ('L863-5', 'Saint-Pierre-et-Miquelon')]:
    entry(number,
        f"Maintien nécessaire du cadre légal des informations et pièces de contrôle à {territory}. Les renvois au LPF fixent les limites de communication ; ils ne sont ni une taxe ni une demande générale supplémentaire adressée aux allocataires. Les supprimer affaiblirait la vérification des ressources et l'échange légal des données sans gain administratif démontré.",
        "L851-1 et L851-3 ont été lus intégralement : obtention des données utiles à l'ouverture et au calcul des droits, puis contrôle par personnel assermenté et communication des pièces nécessaires. Les références L97 à L99, L152 à L162 B et L152 A du LPF sont maintenues dans leurs fonctions distinctes. Elles ne créent pas un accès illimité, et le LPF extérieur n'est pas présenté comme entièrement audité. " + ("Le 3° conserve le président du conseil territorial comme autorité locale de L851-4, sans rapport avec une notification de rupture d'emploi." if number == 'L862-4' else "La note d'entrée en application des contributions et prestations au 1er janvier 2022 n'est pas une date de réforme nouvelle."),
        "Les adaptations de communication et de contrôle sont conservées intégralement. Aucun double dossier ni nouvelle déclaration à supprimer n'est identifié dans la source de cet article, et aucun gain nouveau n'est compté.",
        "L'article ne réécrit ni l'ensemble des procédures fiscales ni les pouvoirs autonomes de contrôle. Le besoin d'informations reste limité par les finalités des articles cités et leurs garanties légales.",
        no_new_retained)

entry('L863-4',
    "Maintien nécessaire de la dispense de conservation des allocations de logement à Saint-Pierre-et-Miquelon. Ce régime favorable évite le blocage des paiements selon la procédure nationale visée ; supprimer la dispense alourdirait le régime. Elle ne retire pas les protections autonomes contre les logements dangereux ou indignes.",
    "Les sept articles L843-1 à L843-7 demeurent exclus exactement comme dans la source ; R863-16 en reprend les adaptations réglementaires. L863-3 conserve parallèlement la décence comme condition de l'aide. Les dérogations locales et les droits des occupants ne sont pas transformés en dispense générale de sécurité. La note fixe le début d'application au 1er janvier 2022 et ne commande aucune fermeture future.",
    "La dérogation territoriale favorable est maintenue pour tous les cas éligibles, y compris futurs. Son maintien n'est pas présenté comme une formalité nouvellement supprimée.",
    "La dispense est limitée au mécanisme de conservation expressément visé ; les devoirs civils du bailleur et les procédures autonomes d'insalubrité ne sont pas abrogés.",
    no_new_retained)

entry('R111-1',
    "Maintien nécessaire de la définition du bâtiment d'habitation et des foyers pour personnes âgées autonomes. Les exclusions des locaux professionnels, ERP et immeubles de grande hauteur évitent de superposer des régimes de sécurité différents. Les seuils de dépendance assurent un classement adapté aux risques des résidents ; aucune procédure d'autorisation ou pièce récurrente n'est créée par cette définition.",
    "Les renvois R143-2 et R146-3, les deux critères de dépendance et toute l'énumération des pièces principales, de service, dégagements et dépendances restent entiers. L'arrêté conjoint définit des seuils techniques : aucun nouveau seuil n'est inventé ni déplacé dans le présent article. Les autres catégories de bâtiments ne sont pas dispensées de leurs protections par l'exclusion du seul champ habitation.",
    "Conservation intégrale des définitions et limites de champ techniques ; aucune réduction nouvelle de formalité ou de coût n'est démontrée par une modification de ces définitions.",
    "Les arrêtés de dépendance et les régimes ERP et grande hauteur ne sont pas réécrits ici. Aucune réduction de protection des personnes âgées n'est proposée.",
    no_new_retained)

entry('R111-2',
    "Maintien nécessaire des définitions des gros et menus ouvrages et de l'exclusion des appareils installés en l'état. La distinction identifie précisément les éléments relevant des règles de construction ; la supprimer ferait perdre les limites utiles de champ sans retirer une déclaration, taxe ou agrément. Les énumérations techniques ne sont pas des pièces à produire.",
    "Les subdivisions I, II 1° a/b, II 2° et III, les six exemples des gros ouvrages, les deux exemples des menus ouvrages et toutes les exclusions sont conservés. Les appareils mécaniques ou électriques livrés en l'état restent exclus de la seule notion d'ouvrage ici définie, sans exemption générale des règles de sécurité. Aucun terme d'emploi, revenu ou prélèvement n'est visé.",
    "Maintien de la définition complète et de ses exclusions techniques. La source ne contient pas d'obligation déclarative autonome dont le retrait serait démontré ; aucune simplification nouvelle n'est revendiquée.",
    "La qualification civile des garanties de construction et les règles propres aux équipements ne sont pas modifiées par cet article de définition.",
    no_new_retained)

entry('R112-1',
    "Maintien nécessaire du dossier d'évaluation et de l'indépendance de l'organisme tiers pour les solutions d'effet équivalent. L'article autorise déjà un dossier et une attestation uniques pour plusieurs solutions dans les champs de compétence de l'organisme ; cette faculté favorable reste ouverte. Supprimer l'évaluation priverait l'équivalence de démonstration et ferait disparaître une garantie de sécurité, non un doublon.",
    "L112-9 et L112-10 ont été lus intégralement dans le corpus, avec source, notes et propositions : l'attestation d'objectif précède la mise en œuvre et le contrôle d'exécution est distinct. R112-1 renvoie aux pièces et mentions de R112-2 et R112-3 dont les allègements sont proposés dans ce lot ; la référence générale reste opérante après conservation de leurs numéros. Ni l'indépendance de fond ni l'information nécessaire aux intervenants ne sont remplacées par une simple déclaration. La faculté de dossier commun n'est pas comptée à nouveau comme une fusion créée.",
    "La source est maintenue intégralement : la faculté de dossier unique et l'exigence d'un tiers indépendant sont déjà en vigueur. Les véritables suppressions documentaires sont portées aux articles R112-2 et R112-3, sans compter ce renvoi comme un gain supplémentaire.",
    "Aucune attestation de sécurité n'est abolie. Le regroupement reste limité aux champs dans lesquels l'organisme est compétent ; il ne remplace pas le contrôleur distinct de l'exécution.",
    no_new_retained)

# Réductions documentaires, sans affaiblir les preuves techniques.
dossier_measure = 'solutions-effet-equivalent-dossier-allege'
support_measure = 'solutions-effet-equivalent-formulaires-facultatifs'
independence_measure = 'solutions-effet-equivalent-independance-sans-attestation'
protocol_measure = 'solutions-effet-equivalent-protocole-sans-double-annexe'

xml = paragraphs(
    "Le dossier de demande de l'attestation de respect des objectifs est présenté par le maître d'ouvrage à l'organisme tiers et comporte :",
    "1° Au titre des pièces relatives à la description du projet de construction :",
    "a) Abrogé ;",
    "b) Les références cadastrales du terrain du projet de construction ;",
    "2° Au titre des pièces relatives aux conditions de réalisation du projet de construction :",
    "a) Une présentation détaillée de la solution envisagée, du dispositif de mise en œuvre et des éléments de suivi de cette mise en œuvre que le maître d'ouvrage entend mettre en place ;",
    "b) Abrogé ;",
    "c) La justification du respect des objectifs généraux fixés aux titres III à VII, pour le champ technique concerné par la solution proposée ;",
    "d) La justification que la solution prévue permet d'atteindre des résultats au moins équivalents à ceux de la solution de référence à laquelle elle se substitue ;",
    "e) La démonstration que la solution proposée ne porte pas atteinte au respect des autres règles de construction applicables à l'opération ainsi que, le cas échéant, aux autres solutions d'effet équivalent mises en œuvre dans l'opération ;",
    "f) La liste des compétences et qualifications requises de tous les constructeurs intervenant au cours de l'opération dans le champ technique concerné par la solution d'effet équivalent et la liste des missions qui leur sont confiées ;",
    "g) Abrogé ;",
    "3° Au titre des pièces relatives au contrôle de la bonne mise en œuvre de la solution d'effet équivalent :",
    "a) Le protocole de contrôle, tout au long du projet de construction, de la conformité des moyens mis en œuvre par les constructeurs à ceux décrits dans le dispositif de mise en œuvre mentionné au a) du 2° ;",
    "b) Le cas échéant, les consignes d'exploitation, d'entretien périodique et de maintenance de la solution d'effet équivalent ;",
    "4° Abrogé.",
    "Le dossier comporte, le cas échéant, les éléments complémentaires propres à certains champs techniques prévus par les dispositions du présent livre.",
    "Les allègements documentaires du présent article sont applicables aux dossiers déposés à compter de l'entrée en vigueur du décret qui les prévoit ainsi qu'aux dossiers en cours d'examen à cette date. Aucune des pièces supprimées ne peut être exigée pour achever cet examen ; les éléments déjà remis n'ont pas à être déposés de nouveau. Les obligations légales d'assurance, la justification de l'équivalence et les règles légales de délivrance et de transmission préalable de l'attestation demeurent applicables.")
entry('R112-2',
    "Réforme de fond : retrait du plan de situation distinct, de la fiche sommaire destinée à la diffusion publique, de l'engagement ou attestation d'assurance dommages-ouvrage dans ce dossier et de la demande générale indéterminée de tout autre document. Suppression également de l'obligation de présenter le dossier dès la simple intention de recourir à une solution. Les références cadastrales, démonstrations techniques, qualifications, protocole et consignes demeurent ; l'assurance légalement obligatoire n'est pas supprimée.",
    "Les a), b), g) et 4° supprimés conservent leur emplacement comme abrogés ; aucun déplacement des c) à f) ou des renvois du 3°. Le plan n'est plus une pièce autonome de localisation en plus du cadastre ; les éléments techniques nécessaires de la présentation restent. R112-3 II 4° est coordonné pour ne pas rétablir la description sommaire publique. Les pièces sectorielles expressément prévues subsistent ; le 4° ne devient pas une habilitation à reconstituer un dossier indéfini. L112-9 conserve la délivrance avant mise en œuvre et, selon le cas, la transmission avant la demande d'urbanisme : supprimer le dépôt dès l'intention ne supprime pas ces échéances légales. La référence L242-1 du code des assurances était déjà dans la source ; ses obligations autonomes ne sont ni réécrites ni retirées, et le texte extérieur n'est pas supposé lu intégralement. Le décret et ses formulaires devront retirer ces rubriques, sans attestation de remplacement.",
    "La proposition supprime réellement cinq contraintes de calendrier ou de dossier par rapport à la source entière, sans remplacer les justificatifs retirés par une déclaration. L'évaluation de l'équivalence et les preuves de sécurité restent complètes ; aucun gain monétaire n'est chiffré.",
    "L'allègement porte sur le dossier d'effet équivalent, pas sur les pièces autonomes d'un permis, les assurances légales ou les compléments sectoriels expressément nécessaires. Les coûts nets et le nombre de projets concernés ne sont pas établis.",
    "Aucune charge nouvelle n'est identifiée : les pièces techniques conservées existaient déjà, aucun registre, attestation de substitution ou nouveau délai n'est créé. L'application aux dossiers en cours dispense de produire les pièces retirées sans demander un nouveau dépôt.",
    xml=xml, classification='material_reduction', change_type='normative_reduction',
    removed=[
        "Présentation obligatoire du dossier dès que le recours à une solution d'effet équivalent est simplement envisagé.",
        "Plan de situation autonome demandé en sus des références cadastrales du terrain au 1° a).",
        "Description sommaire validée destinée à une diffusion publique exigée au 2° b).",
        "Engagement sur l'honneur ou attestation d'assurance dommages-ouvrage imposé comme pièce de ce dossier au 2° g).",
        "Catégorie générale du 4° imposant tout autre document de nature à appuyer la demande sans délimitation technique."],
    effects=[effect('obligation_removed', dossier_measure,
        "Retrait de pièces documentaires générales et du dépôt dès l'intention, avec maintien du dossier technique nécessaire à l'équivalence.",
        "Dossier dès le recours envisagé, plan de situation, description sommaire publique, engagement ou attestation dommages-ouvrage et catégorie générale de tout autre document, outre les preuves techniques.",
        "Ces cinq contraintes sont supprimées ; références cadastrales, démonstrations, qualifications, protocole, consignes et compléments sectoriels demeurent, ainsi que l'assurance légale et les échéances de L112-9.",
        'legal_duty', "Maîtres d'ouvrage demandant l'attestation de respect des objectifs d'une solution d'effet équivalent.",
        "Dossiers nouveaux et en cours à l'entrée en vigueur du décret ; pas de remise en cause des attestations délivrées ni des règles légales préalables.",
        "Aucun justificatif de remplacement ni nouveau délai ; pièces techniques existantes maintenues.",
        "Le dossier de demande de l'attestation de respect des objectifs est présenté par le maître d'ouvrage à l'organisme tiers dès que le recours à une solution d'effet équivalent est envisagé et comporte :",
        "Le dossier de demande de l'attestation de respect des objectifs est présenté par le maître d'ouvrage à l'organisme tiers et comporte :")])

src = by_number['R112-3']['source_xml']
form_old = "Cette attestation est établie sur un formulaire électronique normalisé disponible sur l'application numérique mise à disposition par le ministère chargé de la construction."
form_new = "Cette attestation est établie sur tout support écrit. Le formulaire électronique normalisé disponible sur l'application numérique mise à disposition par le ministère chargé de la construction peut être utilisé."
summary_old = "4° La description sommaire de la solution d'effet équivalent prévue au b) du 2° de l'article R. 112-2 ;"
ind_old = "2° Une déclaration, établie par l'organisme tiers, de son indépendance et de son impartialité."
assert all(s in src for s in [form_old, summary_old, ind_old])
xml = src.replace(form_old, form_new).replace(summary_old, '4° Abrogé ;').replace(ind_old, '2° Abrogé.')
xml += paragraphs("Les dispositions du présent article sont applicables aux attestations établies à compter de l'entrée en vigueur du décret qui les prévoit, y compris pour un dossier antérieurement déposé. Les attestations déjà délivrées conservent leurs effets et n'ont pas à être rééditées. L'obligation d'indépendance et d'impartialité de l'organisme tiers demeure applicable ; aucune déclaration distincte n'est exigée à ce titre.")
entry('R112-3',
    "Réforme de fond : suppression de l'exclusivité du formulaire électronique ministériel et de la déclaration séparée d'indépendance, laquelle doublonne l'obligation de fond de R112-1. Coordination de la suppression de la description sommaire publique de R112-2. Les sept numéros, l'analyse indépendante, le rapport, les objectifs, les équivalences, la reproduction du dispositif et du protocole, les consignes et l'attestation d'assurance du tiers sont conservés sauf le seul 4° expressément abrogé.",
    "II 4° et III 2° restent à leur place comme abrogés ; les 5°, 6° et 7° ne sont pas renumérotés. Le contenu du contrôle demeure entier, y compris la validation de R112-2 2° e/f et 3° a/b. L112-9 conserve l'assurance du tiers et ses règles de transmission : le choix d'un support écrit ne dispense pas des transmissions légalement nécessaires et ne crée pas un droit à un simple avis oral. La déclaration d'indépendance retirée ne retire pas l'interdiction de liens affectant l'indépendance. Formulaires et application ministériels à adapter hors lot ; aucune saisie équivalente ne peut y rétablir le résumé ou la déclaration supprimés.",
    "Deux obligations autonomes de forme disparaissent : support ministériel exclusif et déclaration distincte d'indépendance. Le retrait du résumé ne compte qu'en coordination du dossier allégé de R112-2. Les attestations et leur contenu technique subsistent intégralement dans les autres rubriques.",
    "La suppression ne porte ni sur l'assurance ni sur l'indépendance effective ni sur la démonstration d'équivalence. Les coûts de l'organisme et des transmissions légales ne sont pas chiffrés ; aucun droit de transmission électronique dégradée n'est créé.",
    "Aucune charge nouvelle n'est identifiée : le support écrit libre est une alternative au formulaire déjà obligatoire, sans donnée ni signature supplémentaire imposée ici. Les attestations antérieures sont préservées sans réédition ni déclaration de remplacement.",
    xml=xml, classification='material_reduction', change_type='normative_reduction',
    removed=[
        "Usage exclusif du formulaire électronique normalisé du ministère pour l'attestation de respect des objectifs.",
        "Mention obligatoire de la description sommaire publique au II 4°, en coordination du retrait de cette pièce dans R112-2.",
        "Déclaration annexée distincte d'indépendance et d'impartialité exigée de l'organisme tiers au III 2°."],
    effects=[
        effect('obligation_removed', support_measure,
            "Fin du formulaire ministériel obligatoire pour l'attestation de respect des objectifs, qui peut rester utilisé volontairement.",
            "L'attestation ne peut être établie que sur le formulaire électronique normalisé de l'application ministérielle.",
            "Tout support écrit est admis pour le même contenu ; le formulaire normalisé est facultatif et les transmissions légales restent dues.",
            'legal_duty', "Organismes tiers établissant l'attestation de respect des objectifs et maîtres d'ouvrage destinataires.",
            "Attestations établies après entrée en vigueur, même pour un ancien dossier ; pas de réédition des attestations déjà délivrées.",
            "Aucun contenu nouveau ni déclaration de substitution ; conservation du contenu technique et des règles légales de transmission.",
            form_old, "Cette attestation est établie sur tout support écrit."),
        effect('obligation_removed', independence_measure,
            "Suppression de l'annexe déclarative d'indépendance qui double l'obligation effective d'impartialité et d'indépendance.",
            "Déclaration distincte de l'organisme tiers annexée obligatoirement à chaque attestation, outre l'indépendance exigée par R112-1.",
            "Déclaration distincte non exigée ; indépendance et impartialité effectives toujours opposables et contrôlables.",
            'legal_duty', "Organismes tiers délivrant l'attestation de respect des objectifs.",
            "Attestations nouvelles et dossiers en cours ; anciennes attestations non remises en cause.",
            "Pas d'attestation ou de déclaration équivalente de remplacement ; assurance et contrôle de fond maintenus.",
            ind_old, "L'obligation d'indépendance et d'impartialité de l'organisme tiers demeure applicable ; aucune déclaration distincte n'est exigée à ce titre."),
        effect('coordination', dossier_measure,
            "Suppression de la rubrique de résumé public devenue sans objet après l'allègement du dossier de R112-2.",
            "II 4° exige la description sommaire publique renvoyant au 2° b) de R112-2.",
            "II 4° est abrogé et les autres numéros sont conservés ; les présentations et preuves techniques demeurent dans leurs rubriques.",
            'legal_duty', "Organismes tiers et maîtres d'ouvrage concernés par le même dossier d'effet équivalent.",
            "Même transition que les nouvelles attestations ; pas de réédition du stock.",
            "Aucune rubrique de remplacement ni nouvelle synthèse publique obligatoire.",
            summary_old, "4° Abrogé ; 5° La reproduction du dispositif de mise en œuvre de la solution d'effet équivalent proposé par le maître d'ouvrage et prévu au a) du 2° de l'article R. 112-2 ;")])

entry('R112-4',
    "Maintien nécessaire des voies de compétence des tiers dans les trois champs techniques. Le 3° admet déjà plusieurs voies dont la certification, sans imposer une seconde autorisation générale à tous les organismes du 1°. Retirer tout agrément ou accréditation rendrait l'équivalence de sécurité et d'incendie non garantie, alors que L112-9 impose un tiers compétent et indépendant. Aucun dépôt propre à chaque projet n'est ajouté ici.",
    "Les trois numéros, le renvoi à L121-1, l'article 44 de la loi du 28 mai 2013 et l'agrément L125-3 restent entiers. L125-3 a été lu intégralement : l'agrément du contrôle technique est distinct de la délivrance du dossier d'équivalence. La note du décret 2021-872 prévoit la transition des 2°/3° au plus tard le 1er janvier 2024 et les anciennes qualifications en incendie et autres domaines ; elle a été lue en entier et ne doit pas rouvrir ces solutions temporaires après leur terme. Aucun taux, nouvelle qualification ou certification de remplacement n'est créé. Les arrêtés et l'article 44 extérieur au code ne sont pas présentés comme réécrits ni comme une contrainte européenne identifiée par cet article seul.",
    "Le dispositif existant de reconnaissance des compétences et ses voies alternatives est conservé intégralement. Aucun gain nouveau d'agrément supprimé n'est attribué à la simple conservation des alternatives déjà permises.",
    "Les règles supérieures de compétence de L112-9 et d'agrément L125-3 demeurent. Les modalités des arrêtés sectoriels ne sont pas auditées intégralement ni modifiées dans ce lot.",
    no_new_retained)

src = by_number['R112-5']['source_xml']
form_old = "II.-L'attestation de bonne mise en œuvre est établie sur un formulaire électronique normalisé disponible sur l'application numérique mise à disposition par le ministère chargé de la construction."
form_new = "II.-L'attestation de bonne mise en œuvre est établie sur tout support écrit. Le formulaire électronique normalisé disponible sur l'application numérique mise à disposition par le ministère chargé de la construction peut être utilisé."
protocol_old = "2° Le protocole de contrôle prévu au a) du 3° de l'article R. 112-2 et la liste des éléments de suivi transmis par le maître d'ouvrage ;"
protocol_new = "2° La liste des éléments de suivi transmis par le maître d'ouvrage ;"
refusal_old = "IV.-Dans le cas où le vérificateur estime ne pas pouvoir délivrer l'attestation de bonne mise en œuvre, il renseigne le formulaire prévu par le II, y joint les annexes prévues par le III et précise les motifs qui font obstacle à la délivrance de l'attestation."
refusal_new = "IV.-Dans le cas où le vérificateur estime ne pas pouvoir délivrer l'attestation de bonne mise en œuvre, il établit sur tout support écrit un document comportant les éléments prévus par le II, y joint les annexes prévues par le III et précise les motifs qui font obstacle à la délivrance de l'attestation."
assert all(s in src for s in [form_old, protocol_old, refusal_old])
xml = src.replace(form_old, form_new).replace(protocol_old, protocol_new).replace(refusal_old, refusal_new)
xml += paragraphs("Le protocole de contrôle demeure reproduit dans l'attestation de respect des objectifs qui accompagne l'attestation de bonne mise en œuvre ; aucune seconde annexion du même protocole n'est exigée au titre du III.",
    "Les dispositions du présent article sont applicables aux attestations et documents établis à compter de l'entrée en vigueur du décret qui les prévoit, y compris pour les opérations en cours. Les attestations antérieurement délivrées conservent leurs effets et n'ont pas à être rééditées. Les obligations légales de vérification et de transmission des attestations demeurent applicables.")
entry('R112-5',
    "Réforme de fond : suppression de la seconde annexion du protocole de contrôle, déjà reproduit dans l'attestation de respect des objectifs qui accompagne légalement celle de bonne mise en œuvre. Coordination du support écrit libre pour l'attestation et pour le refus motivé, sans formulaire exclusif. Les missions du vérificateur, ses vérifications avant et pendant les travaux, les transmissions de suivi, les quatre informations du II, le rapport et les preuves des constructeurs sont conservés.",
    "L112-10 a été lu intégralement : il exige un contrôleur sans lien avec le tiers initial et la transmission conjointe des deux attestations à l'achèvement. R112-3 II 6° conserve expressément la reproduction du protocole ; sa présence dans le document accompagnant justifie le retrait du seul duplicata de R112-5 III 2°. La liste des éléments de suivi demeure à ce numéro. I et V restent inchangés : le contrôle technique, le protocole avant travaux, les suivis pendant travaux et la valeur de confirmation de la transmission en ligne subsistent. Le IV garde toutes les informations, annexes maintenues et motifs de refus. Le choix du support ne retire pas la transmission légale et n'exige pas une signature, un registre ou un document de plus. Les formulaires devront être adaptés hors lot sans rétablir la copie supprimée.",
    "Un duplicata de protocole est effectivement retiré, le contenu restant dans l'attestation d'objectif légalement jointe. Le formulaire facultatif est une application de la même mesure de support libre que R112-3, non une seconde suppression générale du contrôle.",
    "La réforme ne supprime aucune vérification ni assurance, aucune preuve de réalisation et aucune transmission prescrite par L112-10. Les économies de reproduction ou de saisie ne sont pas chiffrées et la charge technique de contrôle demeure.",
    "Aucune charge nouvelle n'est identifiée : le document de refus comporte les mêmes informations et annexes maintenues que le formulaire antérieur, sans nouveau contenu. La copie du protocole disparaît sans accès, registre ou attestation de remplacement.",
    xml=xml, classification='material_reduction', change_type='normative_reduction',
    removed=[
        "Deuxième annexion du protocole de contrôle au III 2°, déjà reproduit dans l'attestation d'objectif accompagnant légalement l'envoi.",
        "Exclusivité du formulaire électronique normalisé pour l'attestation de bonne mise en œuvre et le document de refus motivé."],
    effects=[
        effect('obligation_removed', protocol_measure,
            "Suppression du duplicata du protocole en annexe de l'attestation de bonne mise en œuvre, avec conservation de la liste de suivi.",
            "Le protocole doit être annexé au III 2° alors qu'il est déjà reproduit dans l'attestation d'objectif, légalement transmise avec celle de bonne mise en œuvre.",
            "Seule la liste des éléments de suivi reste au III 2° ; le protocole est conservé dans l'attestation d'objectif accompagnant et dans le travail du vérificateur.",
            'legal_duty', "Vérificateurs et maîtres d'ouvrage transmettant les attestations d'une solution d'effet équivalent.",
            "Documents établis après entrée en vigueur, y compris opérations en cours ; aucune réédition du stock ni suppression des obligations anciennes de contrôle.",
            "Pas de copie, index ou attestation de remplacement ; contrôle et autres pièces inchangés.",
            protocol_old, "Le protocole de contrôle demeure reproduit dans l'attestation de respect des objectifs qui accompagne l'attestation de bonne mise en œuvre ; aucune seconde annexion du même protocole n'est exigée au titre du III."),
        effect('coordination', support_measure,
            "Application du choix de support écrit aux attestations d'exécution et aux refus, dans la même mesure de formulaires facultatifs que R112-3.",
            "Formulaire électronique ministériel imposé au II et au IV, y compris lorsque l'attestation ne peut être délivrée.",
            "Support écrit libre avec les mêmes informations et motifs ; formulaire utilisable volontairement et transmissions légales conservées.",
            'legal_duty', "Vérificateurs agréés établissant l'attestation d'exécution ou exposant un refus.",
            "Documents établis après entrée en vigueur ; pas de nouvelle attestation imposée aux projets déjà achevés.",
            "Aucune information nouvelle ; le refus existait déjà et garde ses garanties.",
            form_old, "II.-L'attestation de bonne mise en œuvre est établie sur tout support écrit.")])

xml = paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur du décret supprimant le signalement de l'abandon d'une solution d'effet équivalent.",
    "A compter de cette date, le maître d'ouvrage qui décide de ne pas mettre en œuvre une solution d'effet équivalent n'est tenu, sur le fondement du présent article, ni d'en informer l'administration ni d'établir un formulaire, y compris lorsque l'attestation de respect des objectifs a été délivrée avant cette date. Aucun signalement tardif ou rattrapage de cette seule formalité ne peut être exigé après cette date.",
    "L'abandon de la solution ne dispense pas du respect des règles de construction applicables aux travaux effectivement réalisés, des autorisations d'urbanisme ni des contrôles légalement requis. Il n'affecte pas les droits des occupants et des tiers.",
    "Les informations déjà recueillies restent soumises aux règles de conservation et de protection qui leur sont applicables. Les créances et recours antérieurs demeurent régis par les règles applicables, sous réserve des dispositions relatives à l'application dans le temps des sanctions plus douces.")
entry('R112-6',
    "Réforme de fond : suppression entière du signalement immédiat, de son échéance maximale de deux mois après achèvement et du formulaire électronique d'abandon. Une solution non mise en œuvre ne justifie pas un second circuit déclaratif ; le respect des règles pour l'ouvrage réellement exécuté et les contrôles de sécurité restent exigés. Aucun avis ou déclaration équivalente ne remplace le signalement supprimé.",
    "L112-9 et L112-10 concernent l'utilisation effective de la solution et ses attestations ; ils ne sont pas abrogés par le retrait de cette information d'abandon. R112-7, lu intégralement, organise statistiques et diffusion à partir des données recueillies : son application et les formulaires doivent être coordonnés pour qu'aucune donnée d'abandon ne soit réclamée sur le fondement supprimé. Les autres données légalement recueillies et leur protection demeurent. Aucun rappel futur de cette seule formalité n'est exigible, même pour une attestation ou un abandon antérieur ; les régimes de sanction autonomes ne sont pas présumés abrogés. Aucun gain national ou budget compensatoire n'est inventé.",
    "La source imposait un avis à l'administration immédiatement, au plus tard deux mois après les travaux, et un formulaire. Ces obligations disparaissent réellement pour toutes les demandes de signalement futures, sans déclaration équivalente. Les normes de l'ouvrage réalisé demeurent.",
    "La suppression ne vaut pas dispense de conformité des travaux ni retrait des attestations requises pour une solution réellement exécutée. La coordination de l'application et des statistiques reste nécessaire, sans économie nationale chiffrée.",
    "Aucune charge nouvelle n'est identifiée : ni registre d'abandons, ni notification de remplacement, ni délai supplémentaire. Les garanties des occupants, les contrôles ordinaires et la protection des données déjà recueillies sont maintenus sans nouvelle collecte.",
    xml=xml, classification='material_reduction', change_type='full_repeal',
    repeal_scope="Suppression du signalement à l'administration de l'abandon d'une solution d'effet équivalent, de son délai immédiat et maximal de deux mois après travaux et du formulaire obligatoire, sans rattrapage futur.",
    effects=[effect('obligation_removed', 'solutions-effet-equivalent-fin-signalement-abandon',
        "Fin de l'avis d'abandon et de son formulaire obligatoire, avec retrait de l'échéance attachée au seul avis supprimé.",
        "Avis immédiat d'abandon à l'administration, au plus tard deux mois après achèvement, et formulaire électronique ministériel obligatoire.",
        "Aucun avis, formulaire ni rattrapage de cette seule formalité après l'entrée en vigueur ; conformité de l'ouvrage effectivement réalisé et contrôles autonomes maintenus.",
        'legal_duty', "Maîtres d'ouvrage renonçant à une solution d'effet équivalent ayant donné lieu à une attestation d'objectif.",
        "Suppression de tout signalement exigé après l'entrée en vigueur, y compris en présence d'une ancienne attestation ; protection des informations et recours antérieurs.",
        "Aucun avis de remplacement, registre ou donnée de substitution ; autres obligations de construction inchangées.",
        "Si le maître d'ouvrage décide de ne pas mettre en œuvre la solution d'effet équivalent pour laquelle il a obtenu une attestation de respect des objectifs, il en informe l'administration immédiatement et, au plus tard, dans un délai de deux mois à compter de l'achèvement des travaux.",
        "Aucun signalement tardif ou rattrapage de cette seule formalité ne peut être exigé après cette date.")])

# L'ouverture d'un droit accroît aussi l'obligation de paiement de l'organisme.
# Les deux faces de cette même règle restent dans un seul effet, sans double compte.
for number in ['L861-4', 'L861-8', 'L863-2']:
    out = answer[number]
    si = out['substantive_impact']
    gain = si['effects'][0]
    gain['replacement_or_new_burdens'] = "Pas de nouvelle démarche ou pièce imposée aux bénéficiaires. L'organisme compétent doit instruire et payer les droits désormais ouverts sous les conditions ordinaires : extension de l'obligation publique de paiement et de la gestion dans le régime existant, dépense et solde public non établis. Cette conséquence est recensée ici, sans second effet comptant à nouveau la même ouverture de droit."
    si['assessment'] += " Le classement mixte recense aussi l'obligation publique de traiter et financer les droits supplémentaires ; son coût net reste inconnu."

# Analyses des seules cibles requises, à partir de leur vue fournie.
contexts = {
    'L861-4': "L861-4 concerne l'exclusion puis l'ouverture proposée de la prime de déménagement à Mayotte.",
    'L861-6': "L861-6 adapte les catégories familiales et l'aide à l'accession outre-mer ; l'apprentissage y décrit la situation de l'enfant à charge.",
    'L862-2': "L862-2 règle les ressources, la décence et les charges assimilées aux loyers à Saint-Barthélemy et Saint-Martin.",
    'L862-3': "L862-3 adapte les bénéficiaires familiaux et les opérations de logement à Saint-Barthélemy et Saint-Martin ; seule sa renumérotation contradictoire est corrigée.",
    'L863-1': "L863-1 désigne la caisse de recouvrement de la contribution FNAL à Saint-Pierre-et-Miquelon, désormais limitée aux anciennes périodes par la coordination proposée.",
    'L863-2': "L863-2 concerne l'exclusion puis l'ouverture proposée de la prime de déménagement à Saint-Pierre-et-Miquelon.",
    'L863-3': "L863-3 adapte les ressources, la décence, les charges de logement et leur indexation à Saint-Pierre-et-Miquelon.",
    'L863-4': "L863-4 dispense Saint-Pierre-et-Miquelon de la procédure nationale de conservation des allocations de logement.",
    'L863-5': "L863-5 encadre les échanges d'informations et de pièces de contrôle des aides à Saint-Pierre-et-Miquelon."
}
labor = {
    'L1234-1': "La cible officielle fixe le préavis patronal selon l'ancienneté (moins de six mois, un mois, deux mois) et sa proposition réserve quinze jours calendaires aux contrats nouveaux tout en maintenant les anciens. Cet article de logement ne contient aucun renvoi opératoire à ces durées : aucune ancienneté ni notification de licenciement n'y est ajoutée. Le point de départ après notification prévu par la coordination générale n'est pas un délai de demande d'aide ; les procédures collectives et autorisations spéciales demeurent distinctes.",
    'L1221-2': "La cible officielle permet des contrats à terme ; sa proposition réserve l'emploi nouveau au contrat unique à durée indéterminée, avec survie des anciens contrats et interdiction des nouveaux renouvellements à terme. Aucun renvoi de cet article n'impose un CDD. Une durée d'apprentissage, de stage, d'opération ou d'aide ne termine pas l'emploi ; les avantages de logement restent accessibles aux futures situations éligibles dans le contrat unique. Le champ de l'emploi public n'est pas absorbé par cette cible de droit privé.",
    'L1234-9': "La cible officielle ouvre l'indemnité après huit mois sous exception de faute grave ; la proposition distingue les anciens contrats et le nouveau seuil d'un an au terme effectif, préavis inclus. Après ce seuil, le calcul porte sur toute l'ancienneté : 0,20 mois par an, fractions par mois complets, plafond légal de six mois, employeur seul, sans soustraire la première année. Cet article d'aide au logement ne renvoie pas à cette indemnité ni à une notification de rupture ; aucun seuil d'emploi, suppression de salaires, congés, réparation d'illégalité ou indemnité spéciale n'est introduit."
}

for a in sources:
    n = a['number']
    out = answer[n]
    key = a['code_id'] + '|' + a['source_id']
    checks = []
    for target_key in refs['requirements'][key]:
        t = refs['targets'][target_key]
        tn = t['number']
        if t['code_id'] == 'LEGITEXT000006072050':
            assessment = contexts[n] + ' ' + labor[tn]
        elif n == 'L861-5' and tn == 'L553-2':
            assessment = "Le 5° de L861-5 remplace précisément la référence de L823-9 à CSS L161-1-5 et L553-2 par les deux fondements mahorais d'indus. La cible L553-2 entière prévoit les retenues, le choix de remboursement, la modulation familiale, la remise pour précarité et les garanties, avec indemnité de 10 % en fraude et majoration de retenue pouvant atteindre 50 %, doublée en réitération sous cinq ans. Ces règles nationales ne sont pas importées indistinctement à Mayotte par la lecture de la cible : la substitution locale demeure. Ni ancienneté ni préavis de contrat privé ne sont concernés. L'adaptation prend fin selon la validité annoncée de 2028, sans fermeture anticipée des remises locales ni création d'une taxe."
        elif n == 'L861-5' and tn == 'L821-1':
            assessment = "Le 2° de L861-5 remplace la référence de L822-5 à l'AAH de CSS L821-1 par l'allocation mahoraise de l'article 35 de l'ordonnance 2002-411. La cible fournie est celle de la sécurité sociale, non CCH L821-1 : sa source et sa note de juillet 2026 concernent AAH, résidence, handicap, subsidiarité vieillesse-invalidité et maintien jusqu'au paiement effectif de l'avantage. La neutralisation patrimoniale de L822-5 reste donc accessible aux bénéficiaires locaux éligibles ; aucune condition d'ancienneté, notification ou terme d'emploi ne s'y ajoute. La proposition ne confond pas ce raccordement avec le contrat privé et ne prolonge pas implicitement L861-5 après 2028. Les renvois anciens L900-2/L900-3/L311-5 figurant dans la cible ne sont pas des renvois nouveaux introduits dans cet article."
        elif tn == 'L821-4':
            assessment = contexts[n] + " La cible règle uniquement l'anti-cumul des aides couvrant les mêmes frais de déménagement, avec versement obligatoire de la différence favorable si l'autre aide est inférieure. La suppression de l'exclusion territoriale rend ce mécanisme applicable aux déménagements futurs, sans supprimer le complément ni permettre un double remboursement. L823-8, lu séparément dans le corpus, garde les critères familiaux et de logement. Il ne s'agit pas d'une indemnité de licenciement ; ancienneté et notification de contrat privé sont inapplicables à ce renvoi."
        elif tn == 'L823-3':
            assessment = contexts[n] + " Le 4° réécrit localement les six catégories de L823-3 : prêts d'acquisition/amélioration, location-accession, redressement de copropriété, occupation après expropriation, redevance de parties communes et accueil familial. La source nationale et l'adaptation locale ont été lues intégralement ; ces qualifications de charges restent ouvertes aux situations futures éligibles. Un contrat de location-accession ou une mission d'opérateur n'est pas un contrat de travail à terme ; aucune ancienneté ou notification de rupture n'est requise ici."
        elif tn == 'L863-3':
            if n == 'L863-3':
                assessment = "La cible est la source officielle complète de l'article lui-même, et non un renvoi de cet article vers le code du travail. Les cinq adaptations sont conservées : exclusion des aides des ressources sociales, référence fiscale locale, décence, six charges assimilées et indice de loyer local ou métropolitain. Sa note fixe l'application aux contributions et prestations dues depuis le 1er janvier 2022. Aucun seuil d'ancienneté ou notification de rupture ne s'applique ; les assimilations de charges ne valent pas autorisation de CDD. La vue officielle est distinguée des propositions de réforme."
            else:
                assessment = contexts[n] + " La cible L863-3 règle séparément le calcul des aides dans le même territoire : neutralisation des ressources, fiscalité locale, décence, six charges assimilées et indexation. Ces protections et avantages demeurent applicables aux futures situations éligibles ; ni la suppression du seul recouvrement FNAL, ni l'ouverture de la prime, ni la dispense de conservation, ni les échanges fiscaux ne les abrogent. Aucun renvoi de cet article à L863-3 n'incorpore une ancienneté ou une notification de rupture ; le voisinage dans le livre VIII ne crée pas une règle de contrat privé."
        else:
            raise AssertionError((n, tn))
        checks.append(dict(target_key=target_key, view_sha256=t['view_sha256'], assessment=assessment))
    out['reference_checks'] = checks

    if a.get('benefit_check_required'):
        # Ce lot ne contient pas de drapeau positif ; ne pas produire une analyse générique de secours.
        raise AssertionError('Analyse spécifique de bénéfice manquante pour ' + n)

Path('answer.json').write_text(json.dumps([answer[a['number']] for a in sources], ensure_ascii=False, indent=2) + '\n')
print('answer.json:', len(answer), 'articles')
