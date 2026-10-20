import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
answer = json.loads(Path('previous-answer.json').read_text())
references = json.loads(Path('reference-targets.json').read_text())
by_number = {a['number']: a for a in answer}
target_by_number = {v['number']: (k, v) for k, v in references['targets'].items()}

# Le brouillon n'est qu'un point de départ ; identités contrôlées contre les sources.
assert len(sources) == len(answer) == 24
for source, article in zip(sources, answer):
    for field in ('code_id', 'source_id', 'source_sha256', 'number'):
        assert source[field] == article[field], (article['number'], field)

by_number['L2312-24']['review_notes'] = (
    "Même mesure contrat-unique-duree-indeterminee que L1221-2 proposé, sans seconde suppression des CDD. "
    "Le texte officiel entier et la proposition actuelle de L2312-26 ont été relus dans reference-targets.json : "
    "ses II 1° et 9° proposés distinguent le stock des anciens CDD, les missions et le portage ; son II 5° d) "
    "proposé retire le décompte lié au plancher général de temps partiel. Il s'agit de coordinations proposées, "
    "non du droit en vigueur. Ses aides, exonérations et formations demeurent ouvertes aux situations futures "
    "éligibles au sein du contrat unique. La présente consultation ne crée aucun terme d'emploi ni régime "
    "spécial permettant un nouveau CDD. L1234-1 et L1234-9 proposés ont été lus ; leurs conditions de rupture "
    "individuelle n'affectent pas les obligations collectives conservées ici. Aucun nouveau renvoi normatif "
    "à ces articles de rupture n'est inséré."
)
by_number['L2312-28']['review_notes'] = (
    "L2311-1 et L2312-35 lus pour le champ ; la suppression du bilan ne transforme pas un agent public en "
    "salarié de droit privé. L2312-26 officiel et sa proposition actuelle, désormais fournis en entier, ont été "
    "comparés : ses I et II conservent la consultation et les informations sociales autonomes ; ses II 1°/9° "
    "proposés coordonnent les anciens CDD, les missions et le portage ; son II 5° d) proposé retire le décompte "
    "du plancher de temps partiel supprimé. Le renvoi nouveau à L2312-26 porte sur ces informations, sans "
    "restaurer bilan ni CDD. L2312-29/30/32 sont abrogés pour la même bascule ; L2312-31/33/35 sont coordonnés "
    "dans ce lot. L2317-2 lu : amende de 7 500 euros et renvoi préexistant erroné à L2312-14 ; sa sanction "
    "spéciale reste à coordonner hors lot, avec réserve de la loi pénale plus douce et des effets de "
    "l'article 112-4 du code pénal, dont le texte intégral n'est pas fourni. Ne pas sanctionner les bilans "
    "désormais non exigibles. D4626-7/32 ont été lus : coordonner leurs mentions de présentation/annexion, "
    "sans retirer les rapports médicaux ou les bilans ayant un fondement public autonome. Les empreintes "
    "des quatre cibles sont celles de la vue actuelle ; elles n'attestent pas une validation juridique."
)
by_number['L2312-30']['review_notes'] = (
    "Aucune rubrique du bilan n'est réputée supprimée d'un tableau réglementaire lorsqu'elle possède aussi "
    "une base dans L2312-26 ou L2312-36. Le texte officiel entier de L2312-26 et sa proposition actuelle ont "
    "été comparés : le nouveau renvoi conserve notamment emploi, salaires, formation, égalité, prévention "
    "et logement dans leur champ ; les missions limitées ne terminent pas l'emploi. Les deux années "
    "historiques de L2312-36 demeurent distinctes de la récapitulation propre au bilan supprimé. R2312-20 a "
    "été lu ; le tableau de R2312-9 et les rubriques réglementaires restent à examiner intégralement hors "
    "lot, sans prétendre les avoir supprimés. Les régimes de détachement et de logement restent autonomes. "
    "Les consultations déjà engagées et l'accès aux bilans existants restent couverts. Les cibles de rupture "
    "ne sont pas incorporées à l'information collective par cette abrogation."
)

article = by_number['L2312-33']
article['proposed_xml'] = article['proposed_xml'].replace(
    '<p>Les obligations, créances, droits et recours nés avant cette entrée en vigueur',
    "<p>Les consultations engagées avant cette entrée en vigueur demeurent régies par les dispositions "
    "antérieures. Les obligations, créances, droits et recours nés avant cette entrée en vigueur"
)
article['reason'] = article['reason'].replace(
    'Les obligations et créances anciennes, droits de formation et aides autonomes restent protégés.',
    "Les consultations déjà engagées restent soumises au texte antérieur, en cohérence avec L2312-28 et "
    "L2312-30. Les obligations et créances anciennes, droits de formation et aides autonomes restent protégés."
)
article['review_notes'] = (
    "Incohérence préexistante : L6331-12 est absent du corpus public fourni ; son historique et son éventuelle "
    "abrogation restent à vérifier, sans déduire une abrogation de cette seule absence. Le nouveau corps "
    "n'en ressuscite aucun versement et ne conserve pas de renvoi futur à cette cible non vérifiable. "
    "La transition conserve expressément les consultations déjà engagées. Le texte officiel entier et la "
    "proposition actuelle de L2312-26 ont été lus : ses I et II 1°/3°/4°/4° bis/4° ter portent les informations "
    "de formation, apprentissage, professionnalisation, entretiens, reconversion et CPF indépendantes du bilan. "
    "Le renvoi nouveau à la consultation ne crée ni programme ni donnée supplémentaire ; chaque programme "
    "reste requis par son fondement propre. La proposition de L2312-26 conserve les aides et exonérations "
    "pour les situations futures éligibles dans le contrat unique. L1221-2 proposé interdit qu'une fin de "
    "formation ou d'aide termine l'emploi nouveau. Même mesure que L2312-28, sans baisse de contribution "
    "alléguée ; ni préavis ni indemnité ordinaire ne sont créés par ce renvoi."
)
article['substantive_impact']['scope_limitations'] = (
    "L'historique de L6331-12 demeure une lacune documentaire signalée ; aucun montant ni suppression "
    "d'une contribution supposée n'est avancé. Les consultations déjà engagées conservent le régime antérieur."
)
article['substantive_impact']['effects'][0]['conditions_and_transition'] = (
    "Nouvelles consultations après bascule ; consultations déjà engagées régies par les dispositions "
    "antérieures, et créances, droits, recours et aides anciennes ou futures préservés selon leur fondement."
)

by_number['L2312-36']['review_notes'] = (
    "R2312-10 a été relu en entier : coordonner son exigence de projections chiffrées ou tendances à trois "
    "ans et les raisons de leur indisponibilité ; ne pas rétablir par règlement une justification générale "
    "de non-prévision. R2312-8/9 restent à examiner intégralement pour leurs rubriques prospectives, sans "
    "prétendre réécrire leurs tableaux dans ce lot. L2312-26 officiel et sa proposition actuelle ont été lus "
    "en entier dans les cibles : son II 2° conserve un renvoi exact au 2° du présent article, maintenu à sa "
    "place et intégralement. Ses II 1° et 9° proposés coordonnent le stock CDD, les missions et le portage ; "
    "son II 5° d) proposé supprime le décompte de dérogations au plancher général de temps partiel. "
    "Ces propositions ne sont pas le droit en vigueur et ne permettent pas d'effacer les minima conventionnels "
    "ou le plancher parental spécial. L'ancienneté du diagnostic d'égalité au 2° n'est ni le seuil de "
    "l'indemnité ordinaire ni le déclencheur d'un préavis. Le dernier alinéa de discrétion demeure le dernier "
    "pour préserver les renvois de R2312-12/13, relus. La note de 2023 au 1er janvier 2025 reste historique."
)

# Analyses nouvelles, propres à chaque couple source/cible. Aucune ancienne attestation réemployée.
assessments = {
    'L2312-28': {
        'L1234-1': (
            "L2312-28 impose un bilan collectif à partir de trois cents salariés ; il ne renvoie à aucun "
            "préavis individuel. L1234-1 officiel distingue moins de six mois, six mois à moins de deux ans "
            "et au moins deux ans ; sa proposition conserve ces règles pour les anciens contrats et fixe "
            "quinze jours calendaires sans condition d'ancienneté pour les nouveaux, même si la faute grave "
            "impose un préavis payé non exécuté. La bascule du bilan dépend de l'engagement de la consultation, "
            "non de la notification d'une rupture. Aucune procédure collective ou protection spéciale n'est supprimée."
        ),
        'L1221-2': (
            "Le champ du bilan découle de L2311-1 et des adaptations de L2312-35, non de la forme du contrat. "
            "L1221-2 officiel permet encore les CDD ; sa proposition interdit les nouvelles embauches, "
            "renouvellements ou reconductions à terme après la bascule, en conservant les anciens contrats "
            "et leurs litiges selon la transition. L'abrogation du bilan ne rouvre aucun CDD et ne clôt "
            "aucun contrat à la fin d'une mission ou d'une formation. Les agents publics ne sont pas "
            "convertis implicitement en contrats privés."
        ),
        'L1234-9': (
            "L'obligation supplémentaire de bilan ne détermine aucune indemnité de rupture. L1234-9 "
            "officiel ouvre l'indemnité à huit mois, sauf faute grave ; la proposition exige pour les "
            "nouveaux contrats un an à la fin effective, préavis inclus, puis 0,20 mois par année totale, "
            "fractions en mois complets et plafond de six mois. Elle réserve anciens contrats, dispositions "
            "plus favorables et indemnités spéciales. Rien dans l'abrogation de L2312-28 ne réduit ces "
            "droits ni ne transforme les trois cents salariés du bilan en condition individuelle d'ancienneté."
        ),
        'L2312-26': (
            "Ce renvoi est nouveau et sa cible est maintenant fournie en entier. Le I de L2312-26 porte "
            "la consultation sociale ; les II 1° à 9° fournissent l'information autonome conservée, et non "
            "un bilan supplémentaire. La proposition coordonne les II 1°/9° aux anciens CDD et aux missions, "
            "retire le II 5° d) et maintient les aides et formations éligibles à l'avenir. Les obligations "
            "de prévention, d'égalité et de logement demeurent. Le renvoi ne recrée ni synthèse distincte "
            "ni prévision de recrutement sous une forme interdite ; les consultations anciennes gardent leur régime."
        ),
    },
    'L2312-30': {
        'L1234-1': (
            "La récapitulation sociale sur trois exercices prévue par L2312-30 n'est pas un délai de "
            "préavis. L1234-1 proposé fixe quinze jours calendaires indépendamment de l'ancienneté pour "
            "les nouveaux contrats ; le stock ancien conserve les paliers officiels et les règles plus "
            "favorables qui lui sont applicables. L'abrogation des rubriques du bilan prend effet selon "
            "la date d'engagement de la consultation, sans déplacer le départ du préavis lié à la notification "
            "écrite et sans supprimer les procédures collectives ou autorisations distinctes."
        ),
        'L1221-2': (
            "La rubrique d'emploi du bilan supprimé n'est pas une autorisation de conclure un contrat. "
            "L1221-2 proposé remplace pour l'avenir la faculté officielle de CDD par le contrat unique "
            "indéterminé ; il préserve le stock antérieur sans permettre renouvellement ou reconduction "
            "postérieurs. Le renvoi conservé aux informations sociales n'exige pas de nouveaux CDD : "
            "les missions, formations et aides peuvent être limitées sans mettre fin à l'emploi. Les "
            "règles autonomes de détachement et de logement de la source ne sont pas abrogées."
        ),
        'L1234-9': (
            "Les trois années d'observation du bilan ne mesurent pas l'ouverture d'une indemnité. "
            "L1234-9 officiel prévoit huit mois, avec exception de faute grave ; sa proposition distingue "
            "le stock ancien du contrat unique nouveau, dont l'ancienneté s'apprécie au terme effectif "
            "préavis inclus. À un an, toute l'ancienneté entre dans 0,20 mois par année, fractions de "
            "mois complets et plafond de six mois, sans soustraire la première année ; les droits spéciaux "
            "subsistent. L'abrogation de L2312-30 ne touche à aucun de ces calculs ni à leur preuve autonome."
        ),
        'L2312-26': (
            "Le renvoi nouveau aux informations légalement dues a été confronté au I et au II entiers "
            "de L2312-26. Les informations d'emploi, salaires, formation, égalité, handicap, durée du "
            "travail et logement possèdent ce fondement distinct ; aucune récapitulation triennale du "
            "bilan n'est réintroduite. La proposition cible coordonne les II 1°/9° au contrat unique et "
            "retire le II 5° d), sans retirer les aides aux situations futures éligibles. Les anciennes "
            "consultations restent régies par leur droit et l'accès aux bilans établis demeure assuré par L2312-31."
        ),
    },
    'L2312-33': {
        'L1234-1': (
            "Le programme annuel de formation visé par L2312-33 n'est ni une période d'emploi ni un "
            "préavis. L1234-1 officiel organise les préavis selon l'ancienneté ; sa proposition réserve "
            "ces règles aux anciens contrats et substitue quinze jours calendaires pour les nouveaux. "
            "Le réemploi d'informations de formation n'ajoute aucune condition de notification et ne "
            "réduit aucune procédure collective. La fin d'un programme annuel n'autorise pas une rupture "
            "automatique ou une dispense de préavis ; les consultations déjà engagées conservent leur transition propre."
        ),
        'L1221-2': (
            "L1221-2 proposé interdit expressément de fixer le terme de l'emploi à la fin d'une "
            "formation, contrairement à la faculté officielle générale de contrats à terme dans les "
            "cas du titre IV. L2312-33 proposé n'établit qu'un support pour les programmes requis ailleurs : "
            "il ne crée ni durée d'emploi, ni nouveau CDD ou renouvellement. Les anciens contrats "
            "conservent leurs droits et les aides ou financements restent ouverts aux formations "
            "futures éligibles dans le contrat unique, sans réserver ces avantages aux seuls anciens CDD."
        ),
        'L1234-9': (
            "Aucun versement de rupture n'est institué par la référence aux programmes de formation. "
            "Le seuil officiel de huit mois de L1234-9 et sa transition proposée pour les anciens contrats "
            "restent distincts. Pour le nouveau contrat unique, la cible proposée exige un an au terme "
            "effectif préavis inclus, puis 0,20 mois par année totale, mois complets au prorata, plafond "
            "de six mois et employeur seul, sous son exception de faute grave. La fin d'une aide ou "
            "formation ne remet pas l'ancienneté à zéro ; salaires, droits acquis et indemnités spéciales restent autonomes."
        ),
        'L2312-26': (
            "La cible complète désormais jointe justifie le nouveau renvoi : le I, puis les II 1°, "
            "3°, 4°, 4° bis et 4° ter, couvrent les informations de formation, compétences, CPF, "
            "professionnalisation, entretiens et reconversion. Le programme utilise les seules informations "
            "déjà établies ; aucune obligation autonome de programme ni bilan alternatif n'est créée. "
            "La proposition cible conserve les avantages pour les situations futures éligibles dans "
            "le contrat unique. Les consultations déjà engagées demeurent expressément soumises au "
            "régime antérieur ; le renvoi ancien à L6331-12 reste une lacune historique signalée."
        ),
    },
    'L2312-36': {
        'L1234-1': (
            "L2312-36 ne renvoie pas au préavis : ses années d'historique et de perspectives concernent "
            "la base collective. L1234-1 proposé donne aux nouveaux contrats quinze jours calendaires "
            "sans seuil d'ancienneté, avec préavis payé si une faute grave interdit le maintien au "
            "travail ; les paliers officiels demeurent pour les anciens contrats. Supprimer les "
            "perspectives générales à trois ans ne modifie ni notification de rupture, ni départ "
            "du préavis, ni autorisations et procédures collectives. L'ancienneté du diagnostic "
            "d'égalité au 2° reste un critère d'analyse, non un seuil de préavis."
        ),
        'L1221-2': (
            "Le 1° de L2312-36 proposé a été confronté à L1221-2 officiel et proposé : les contrats "
            "précaires antérieurement conclus restent suivis, mais la rubrique ne permet aucun nouveau "
            "CDD, renouvellement ou reconduction après la bascule. Les stages demeurent distincts "
            "des contrats de travail ; une mission, affectation ou phase pédagogique limitée ne "
            "fixe pas le terme du nouveau contrat indéterminé. Le suivi général de l'emploi et "
            "des conditions de travail reste dû ; aucun régime public ou contrat ancien n'est "
            "converti tacitement et aucun registre de missions nouveau n'est créé."
        ),
        'L1234-9': (
            "Le diagnostic d'égalité du 2° conserve l'analyse des écarts en fonction de l'ancienneté. "
            "Il n'applique pas le seuil d'indemnisation de L1234-9, officiel à huit mois et proposé "
            "à un an pour les nouveaux contrats au terme effectif préavis inclus. Dans cette cible, "
            "le seuil atteint entraîne 0,20 mois sur toute l'ancienneté, mois complets au prorata "
            "et plafond de six mois ; anciens droits, conventions plus favorables et indemnités "
            "spéciales demeurent. La suppression de prévisions triennales ne retire aucune créance, "
            "ne soustrait pas la première année et ne transforme pas une démission en rupture indemnisable."
        ),
    },
}

for article in answer:
    key = article['code_id'] + '|' + article['source_id']
    required = references['requirements'][key]
    article['reference_checks'] = []
    named = assessments.get(article['number'], {})
    assert set(named) == {references['targets'][k]['number'] for k in required}
    for target_key in required:
        target = references['targets'][target_key]
        article['reference_checks'].append({
            'target_key': target_key,
            'view_sha256': target['view_sha256'],
            'assessment': named[target['number']],
        })

Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print('answer.json :', len(answer), 'articles ;',
      sum(len(a['reference_checks']) for a in answer), 'analyses de renvoi actuelles.')
