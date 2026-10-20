import json
import html
import re
from pathlib import Path

S = json.loads(Path('source.json').read_text())
R = json.loads(Path('reference-targets.json').read_text())
A = []

def paras(*items):
    return '\n'.join('<p>' + html.escape(x, quote=False) + '</p>' for x in items)

def effect(kind, measure, description, before, after, unit, population,
           transition, replacement, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure, description=description,
                before=before, after=after, unit=unit,
                affected_population=population, conditions_and_transition=transition,
                replacement_or_new_burdens=replacement,
                source_quote=source_quote, proposed_quote=proposed_quote)

def make(i, proposed, reason, notes, classification, assessment, limitations, burdens, effects,
         change=None, removed=None, scope=None):
    s = S[i]
    a = {k: s[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}
    a.update(proposed_xml=proposed, reason=reason, review_notes=notes, status='rewrite_draft')
    if change:
        a['change_type'] = change
        if change == 'full_repeal':
            a['repeal_policy_id'] = 'editorial_direction_2026_10_19'
            a['repeal_scope'] = scope
        else:
            a['reform_policy_id'] = 'editorial_direction_2026_10_19'
            a['removed_provisions'] = removed
    a['substantive_impact'] = dict(version=1, classification=classification,
        assessment=assessment, scope_limitations=limitations,
        new_burdens_review=burdens, effects=effects)
    A.append(a)
    return a

def repeal_ratio(i, employment, extra):
    p = paras(
        "Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant cette abrogation.",
        "Le plafond de 25 % de la durée totale du contrat applicable à la durée cumulée des périodes de mise en situation en milieu professionnel est supprimé pour les périodes débutant à compter de cette date et pour la fraction postérieure à cette date des périodes en cours, y compris lorsque le contrat de travail a été conclu auparavant. Aucun plafond fondé sur une durée présumée du contrat unique, de la mission, de l'aide ou du parcours ne lui est substitué.",
        "Les conditions et limites propres à chaque période, notamment celles de l'article D. 5135-3, la prescription, la convention individuelle et l'accord de l'employeur demeurent applicables. Le maintien du statut et de l'indemnisation, le droit au retour au poste, les protections de santé et de sécurité et les interdictions de substitution à un emploi prévues au chapitre V du présent titre sont conservés.",
        "Les périodes accomplies avant cette entrée en vigueur restent appréciées selon les règles alors applicables pour leurs effets antérieurs. Les droits acquis, les créances et les recours correspondants sont conservés. La suppression du plafond ne régularise pas un dépassement antérieur et ne prolonge pas automatiquement une convention individuelle. Les conventions valablement conclues demeurent applicables, sous réserve de la suppression du plafond pour leur exécution future. La fin d'une période d'immersion ne met pas fin au contrat de travail.")
    return make(i, p,
        "Réforme de fond : suppression du seul ratio global de 25 %, sans plafond de substitution. Les limites individuelles et les protections contre l'utilisation d'une immersion comme emploi gratuit restent fondées sur le chapitre V. " + extra,
        "Le renvoi source vise " + employment + ", dont le deuxième alinéa autorise les immersions ; ses durées de parcours ne sont pas une durée totale d'emploi. D5135-3, lu dans le corpus public, conserve un mois de date à date, un renouvellement pour objectifs non atteints et, dans une même structure sur douze mois, deux conventions d'objets ou objectifs différents et soixante jours au total, renouvellements compris. L5135-3 à L5135-8 conservent statut, indemnisation, retour au poste, financement, sécurité, libertés et interdictions. Aucun seuil d'ancienneté ni délai de notification de rupture n'est créé. Le renvoi explicite à D5135-3, absent des cibles fournies mais déjà présent au brouillon, a été contrôlé en source officielle locale (LEGIARTI000029763898). Coordonner formulaires et clauses types, sans affirmer les avoir réécrits.",
        'material_reduction',
        "Par rapport à la source officielle entière, le plafond cumulé de 25 % disparaît réellement pour l'exécution future, y compris celle d'anciens contrats. Il ne s'agit ni d'une baisse de prélèvement ni d'un calcul sur une durée fictive de CDI. " + extra,
        "Les effets antérieurs et les limites individuelles demeurent ; la liberté d'immersion n'est donc pas illimitée. Les autres articles d'exécution et formulaires hors lot restent à coordonner. Le coût net national n'est pas établi.",
        "Aucune charge nouvelle n'est identifiée : ni déclaration, ni autorisation, ni ratio, ni registre ne remplace le plafond. Les conventions, durées et protections rappelées existent déjà dans le chapitre V ; aucun dossier supplémentaire n'est imposé.",
        [effect('obligation_removed', 'suppression-plafond-global-pmsmp',
            'Retrait du ratio global d’immersion rapporté à la durée du contrat de travail.',
            'Pour les salariés relevant de ' + employment + ', durée cumulée des immersions limitée à 25 % de la durée totale du contrat.',
            'Aucun ratio global pour l’exécution postérieure à l’entrée en vigueur, y compris des contrats antérieurs ; limites individuelles maintenues.',
            'percent', 'Salariés en insertion relevant de ' + employment,
            'Suppression prospective de la fraction future des périodes ; droits, contrôles et recours relatifs aux fractions antérieures conservés.',
            'Aucune règle de remplacement ; conventions individuelles et protections antérieures maintenues.',
            "ne peut représenter plus de 25 % de la durée totale du contrat.",
            "Le plafond de 25 % de la durée totale du contrat applicable à la durée cumulée des périodes de mise en situation en milieu professionnel est supprimé")],
        'full_repeal', scope="Suppression du plafond cumulé d'immersion de 25 % de la durée du contrat, pour toute exécution future, sans retirer les protections individuelles ni les effets antérieurs.")

repeal_ratio(0, 'L5132-5',
    "Le brouillon antérieur supprimait déjà le plafond pour les fractions futures des périodes, même en cours : ce champ favorable est conservé après réexamen, sans prétendre ajouter une seconde réduction. Les garanties individuelles maintenues ont une fonction autonome de protection.")

p = paras(
    "La convention conclue avec une entreprise de travail temporaire d'insertion comporte les mentions suivantes :",
    "1° Une présentation du projet d'insertion de la structure précisant :",
    "a) Les caractéristiques générales de la structure ;",
    "b) Les principales caractéristiques des personnes en difficulté embauchées ;",
    "c) Les modalités d'accompagnement des salariés en insertion et de collaboration avec l'opérateur France Travail et les organismes chargés de leur insertion sociale et professionnelle. La structure peut mentionner un label délivré par un tiers certificateur attestant de la qualité de son projet ; ce label n'est pas exigé ;",
    "d) Abrogé ;",
    "e) Abrogé ;",
    "f) Abrogé ;",
    "g) Le cas échéant, le champ territorial d'intervention de l'entreprise lorsqu'il dépasse le seul ressort départemental ;",
    "2° Les moyens en personnel, matériels et financiers mobilisés pour mettre en œuvre le projet d'insertion et accomplir les tâches administratives et les obligations comptables résultant de l'activité de l'entreprise ;",
    "3° Le nombre de postes d'insertion ouvrant droit à l'aide financière prévue à l'article R. 5132-10-12 ;",
    "4° Les engagements d'insertion de la structure et les indicateurs rendant compte des actions et des résultats ;",
    "5° Abrogé ;",
    "6° La nature et le montant des autres aides publiques directes ou privées perçues les années antérieures, seulement lorsqu'elles financent les mêmes postes ou dépenses que la convention et que ces informations sont nécessaires au contrôle des règles de cumul applicables ;",
    "7° Les modalités de suivi, de contrôle et d'évaluation de la convention.",
    "Les informations et pièces exactes et à jour déjà légalement détenues par l'autorité de conventionnement sont réutilisées sans nouvelle production par la structure. Aucune mention, déclaration, autorisation ou certification équivalente ne remplace les mentions supprimées aux d), e) et f) du 1° et au 5°. La collaboration prévue au c), l'affectation des aides à leur objet et le contrôle de la réalité des actions d'insertion demeurent.",
    "Ces dispositions s'appliquent dès l'entrée en vigueur de la loi les prévoyant aux conventions nouvelles et aux procédures en cours, sans nouveau dépôt ni reprise des délais. Les conventions déjà conclues restent valables ; leurs clauses imposant seulement les formalités supprimées cessent de les imposer pour l'avenir, sans affecter les engagements autonomes, les aides accordées ni les créances antérieures. Les emplois de droit privé conclus après l'entrée en vigueur du contrat unique sont à durée indéterminée ; la durée de la convention, de l'aide ou d'une mission ne met pas fin à ces emplois.")
s = S[1]
ef = []
for quote, desc, after, pq in [
    ("Le cas échéant, la mention de l'existence d'une autre convention au titre d'une structure de l'insertion par l'activité économique ;", "Retrait de la mention obligatoire d'une autre convention d'insertion.", 'La convention ne comporte plus cette mention obligatoire.', 'd) Abrogé ;'),
    ("L'adéquation du projet économique et social de la structure avec l'environnement local et l'offre d'insertion déjà existante ;", "Retrait de la justification de l'adéquation à l'offre d'insertion locale existante.", "L'existence d'une offre locale ne justifie plus cette formalité de conventionnement.", 'e) Abrogé ;'),
    ("Les modalités de dépôt des offres d'emploi auprès de l'institution précitée ;", "Retrait du circuit conventionnel obligatoire de dépôt des offres.", 'Aucune modalité obligatoire de dépôt auprès de France Travail au titre de cet article ; collaboration maintenue.', '5° Abrogé ;')]:
    ef.append(effect('obligation_removed', 'simplification-convention-etti', desc,
        'Mention imposée dans la convention : ' + quote, after, 'legal_duty',
        "Entreprises de travail temporaire d'insertion conventionnées et candidates au conventionnement.",
        'Conventions nouvelles, procédures en cours et seules clauses formelles des conventions existantes pour leur exécution future ; droits antérieurs préservés.',
        'Aucune déclaration ou autorisation de substitution ; contrôles autonomes conservés.', quote, pq))
ef.append(effect('compliance_cost_reduced', 'simplification-convention-etti',
    'Réduction de l’historique général des aides aux informations nécessaires aux cumuls sur les mêmes postes ou dépenses.',
    'Nature et montant de toutes les autres aides publiques directes ou privées des années antérieures à mentionner sans ciblage.',
    'Seules les informations antérieures nécessaires au contrôle des cumuls sur les mêmes postes ou dépenses sont requises ; réemploi des pièces détenues.',
    'legal_duty', "Entreprises de travail temporaire d'insertion demandant ou exécutant une convention.",
    'Application immédiate aux conventions nouvelles et aux obligations futures des conventions en cours ; pas de modification rétroactive des aides.',
    'Pas de collecte des aides actuelles ajoutée, ni nouvelle attestation ; autres fondements légaux de contrôle conservés.',
    "La nature et le montant des autres aides publiques directes ou privées dont la structure a bénéficié les années antérieures ;",
    "seulement lorsqu'elles financent les mêmes postes ou dépenses que la convention et que ces informations sont nécessaires au contrôle des règles de cumul applicables"))
ef.append(effect('coordination', 'etti-fin-activite-exclusive',
    'Suppression de la mention qui aurait rétabli l’exclusivité d’activité retirée dans L5132-6 proposé.',
    'La convention doit décrire le respect de l’activité exclusive et l’intégralité des moyens humains et matériels.',
    'La lettre f) est abrogée ; aides affectées à leur objet et moyens du projet maintenus ; suppression principale portée par L5132-6 proposé.',
    'legal_duty', "Entreprises de travail temporaire d'insertion, y compris structures exerçant d'autres activités.",
    "Coordination à l'entrée en vigueur de la réforme ; engagements autonomes et créances antérieures conservés.",
    "Aucune déclaration de diversification ni autorisation de remplacement ; ne compte pas comme une seconde suppression de l'exclusivité.",
    "Les modalités selon lesquelles la condition d'activité exclusive définie à l'article L. 5132-6 est respectée, notamment l'intégralité des moyens humains et matériels ;", 'f) Abrogé ;'))
# Les citations très courtes des lettres abrogées sont complétées par leur contexte exact.
for e in ef:
    if len(e['proposed_quote']) < 12:
        e['proposed_quote'] = "Aucune mention, déclaration, autorisation ou certification équivalente ne remplace les mentions supprimées aux d), e) et f) du 1° et au 5°."
make(1, p,
    "Réforme de fond conservant les coupes antérieures : retrait des mentions d'autre convention, d'adéquation à l'offre locale et de dépôt obligatoire des offres ; historique des aides limité aux cumuls pertinents et réemploi des pièces. Coupe supplémentaire de la lettre f), nécessaire pour ne pas rétablir l'exclusivité d'activité supprimée par L5132-6 proposé. Les moyens dédiés au projet, les postes aidés, l'accompagnement, les indicateurs et les contrôles restent nécessaires à la réalité de l'insertion et à l'emploi des fonds ; leur suppression supplémentaire n'est pas justifiée. Le label demeure facultatif.",
    "Confrontation intégrale avec L5132-6 fourni : sa proposition retire explicitement exclusivité et intégralité des moyens ; le brouillon de R5132-10-7 était donc incohérent sur f). La source officielle conserve cette exclusivité : la coupe est une réforme, pas le droit actuel. Les lettres a) à g) et les 1° à 7° gardent leur place. R5132-10-8/9 lus dans le corpus maintiennent viabilité, comptes, suivi annuel et contrôle des actions ; ils ne sont pas réécrits ici. R5132-10-14 interdit le cumul au même poste : les informations nécessaires restent accessibles. La note historique du décret 2024-606 fixe le 1er juillet 2024, pas l'entrée en vigueur de ce projet. Adapter les formulaires et les clauses types sans recréer les mentions abrogées ; aucune hausse ni montant d'aide inventé.",
    'material_reduction',
    "La source officielle entière impose un ensemble ouvert de mentions. La proposition retire trois rubriques documentaires, borne l'historique des aides et interdit les productions répétées ; elle retire aussi f) par coordination avec la fin de l'exclusivité dans L5132-6. Les autres rubriques servent l'allocation et le contrôle des aides. Ces effets ne constituent pas cinq taxes supprimées ni un rendement chiffré.",
    "Les comptes, bilans annuels et contrôles de R5132-10-8/9 gardent leur fondement autonome hors lot. L'affectation des fonds aux actions éligibles subsiste ; les obligations européennes de cumul ne sont pas réputées supprimées. Le solde global de coût n'est pas chiffré.",
    "Aucune charge nouvelle n'est identifiée : pas de déclaration de remplacement, de certification, de registre ou de délai supplémentaire. La connaissance des financements est restreinte aux besoins existants du contrôle des cumuls ; les pièces exactes détenues sont réutilisées.", ef,
    'normative_reduction', removed=[
        "Mention obligatoire de l'existence d'une autre convention d'insertion au 1° d).",
        "Justification de l'adéquation du projet avec l'offre locale déjà existante au 1° e).",
        "Description du respect de l'activité exclusive et de l'intégralité des moyens au 1° f), en coordination avec L5132-6 proposé.",
        "Fixation obligatoire des modalités de dépôt des offres auprès de France Travail au 5°.",
        "Collecte générale de l'historique des autres aides sans nécessité liée aux règles de cumul au 6°, et nouvelle production de pièces exactes déjà détenues."])

p = S[2]['previous_draft']['proposed_xml']
p = p.replace("l'entreprise peut demander le dispositif le plus favorable", "le dispositif le plus favorable s'applique")
p = p.replace(" Les garanties propres à l'emploi intérimaire à durée indéterminée, notamment la garantie mensuelle et le décompte des intermissions, restent applicables.", "")
p = p.replace("La durée indéterminée du nouvel emploi ne peut, à elle seule, exclure l'aide ou en réduire le montant.", "La durée indéterminée du nouvel emploi ne peut, à elle seule, exclure l'aide ou en réduire le montant. La conversion convenue d'un contrat antérieur conserve toute l'ancienneté, les créances et les droits à l'aide pour les périodes restant éligibles, sans recommencer le décompte des périodes déjà financées par un même dispositif. La première année propre à l'aide particulière reste déterminée dans les conditions de l'article D. 5132-10-15.")
make(2, p,
    "Coordination de fond du contrat unique : l'aide ordinaire n'exige plus un contrat de mission à terme et reste ouverte aux futurs emplois éligibles. Le socle, la modulation annuelle, le plafond de postes et ses trois critères sont conservés, car ils déterminent l'avantage ; aucune coupe d'aide n'est décidée. Le choix favorable déjà acquis entre aide ordinaire et aide particulière devient applicable sans demande supplémentaire propre à cet article. Le rappel redondant des garanties intérimaires est retiré sans supprimer leur fondement dans L5132-6 proposé.",
    "R5132-10-13, R5132-10-13-1/2 et R5132-10-14 ont été lus en source dans le corpus : versement au prorata, revalorisation, aide particulière de 100 % du socle la première année et 70 % ensuite, non-cumul au même poste. Ces renvois particuliers sont absents des cibles fournies mais figuraient déjà au brouillon ; sources LEGIARTI000043996457/459 et LEGIARTI000043999758. Aucune réinitialisation d'une même aide par conversion ; le nouveau renvoi à D5132-10-15, absent des cibles mais intégralement rédigé dans ce lot à partir de sa source, distingue l'accès initial à l'aide particulière de la poursuite d'une aide déjà consommée. La proposition de L5132-6 ouvre la section 4 bis et les garanties de rémunération et d'intermission ; ce coût propre au contrat unique n'est pas une baisse de prélèvement démontrée par cet article. Le renvoi de R5132-10-13-1 à L5132-6-1, abrogé dans son projet, doit être coordonné pour conserver la catégorie bénéficiaire ; D5132-10-15 du présent lot en précise le fondement. Arrêtés de versement hors lot à adapter.",
    'coordination_only',
    "Par rapport à la source officielle entière, le support contractuel de l'aide change pour éviter sa disparition avec les nouveaux contrats de mission à terme. Le montant de l'aide n'est pas abaissé, le contingent n'est pas supprimé et le contrôle annuel de modulation subsiste. La mesure principale est le contrat unique avec maintien des aides, non une nouvelle suppression de prélèvement.",
    "L'aide n'est pas due pendant toute la vie du CDI par le seul effet de sa durée. Les critères d'éligibilité, postes, financement, arrêtés et règles de non-cumul demeurent ; les coordinations réglementaires extérieures ne sont pas présentées comme achevées.",
    "Aucune formalité nouvelle n'est identifiée dans cet article : le dispositif le plus favorable ne requiert pas de demande additionnelle et les conventions existantes restent utilisables. La garantie mensuelle entre missions et l'emploi sans terme découlent de L5132-6 proposé ; leurs charges propres sont identifiées, sans prétendre à un solde global chiffré.",
    [effect('coordination', 'contrat-unique-insertion-aides',
        "Maintien de l'aide ordinaire ETTI et de l'accès favorable à l'aide particulière sous contrat unique.",
        'Aide réservée ici aux embauches en contrat de mission, avec socle, modulation annuelle et contingent conventionnel.',
        'Mêmes composantes et critères pour les nouveaux contrats uniques éligibles ; aides anciennes conservées et dispositif le plus favorable sans cumul au même poste et à la même période.',
        'regime', "Personnes éligibles à l'insertion embauchées par les entreprises de travail temporaire d'insertion.",
        "Nouvelles embauches dès la réforme ; contrats antérieurs et périodes restant éligibles préservés, sans renouvellement d'un CDD ni double compte.",
        "Aucun nouveau conventionnement du seul fait du CDI ; garanties de l'emploi intérimaire fixées dans L5132-6 proposé, sans économie alléguée ici.",
        "en contrat de mission par les entreprises de travail temporaire d'insertion ouvre droit",
        "sous contrat unique à durée indéterminée ouvre droit à une aide financière")],
    'normative_reduction', removed=["Condition de support en contrat de mission à terme pour ouvrir l'aide ordinaire aux futures embauches d'insertion ; aucune autorisation de remplacement."])

p = paras(
    "Les personnes âgées d'au moins cinquante-sept ans rencontrant des difficultés sociales et professionnelles particulières peuvent bénéficier, pour leur emploi à durée indéterminée par une entreprise de travail temporaire d'insertion dans le cadre de l'article L. 5132-6, des aides particulières prévues aux articles R. 5132-10-13-1 et R. 5132-10-13-2, dans leurs autres conditions d'attribution. Pour l'application de ces articles, le renvoi à la catégorie de bénéficiaires de l'ancien article L. 5132-6-1 s'entend des personnes définies au présent alinéa. Ce bénéfice est ouvert dès le début du parcours d'insertion par l'activité économique.",
    "Ni une attente minimale de douze mois, ni un contrat à durée déterminée antérieur, ni un examen supplémentaire distinct de l'appréciation de l'éligibilité au parcours prévue à l'article L. 5132-3 ne sont exigés. L'accueil, l'accompagnement individualisé et les actions de formation restent régis par leurs dispositions propres. Le critère d'âge du premier alinéa délimite cette catégorie d'aide particulière ; il ne subordonne pas l'accès au contrat unique.",
    "Pour les emplois relevant du contrat unique, la première année prévue à l'article R. 5132-10-13-2 est la première année d'accès à l'aide particulière pour l'emploi concerné. Les périodes déjà financées par cette aide ne sont pas recomptées du seul fait d'une conversion ou du changement de support contractuel. Les périodes antérieures financées par l'aide ordinaire ne sont pas déduites de cette première année au titre de l'aide particulière. Les aides particulières antérieurement accordées poursuivent leur calendrier sans recommencement.",
    "Ces dispositions s'appliquent à compter de l'entrée en vigueur de la loi les prévoyant, y compris aux personnes dont le parcours a commencé avant cette date. Elles conservent l'accès aux aides et garanties de l'ancien contrat à durée indéterminée d'inclusion pour les situations futures éligibles. Les contrats et aides déjà accordés, l'ancienneté, les créances et les recours sont préservés. Une conversion convenue conserve toute l'ancienneté et les créances acquises, sans recommencer le décompte des périodes déjà financées par un même dispositif. Aucun versement rétroactif général n'est créé. Les nouveaux emplois sont conclus sous contrat unique à durée indéterminée ; ni la durée d'une mission, ni celle du parcours, de l'accompagnement ou de l'aide ne met fin à l'emploi. Aucun nouveau CDD ni renouvellement d'un CDD n'est autorisé après l'entrée en vigueur du contrat unique.")
make(3, p,
    "Réforme de fond conservant la suppression des douze mois d'attente et du CDD préalable. Coupe supplémentaire : suppression du second examen d'accès au CDI d'inclusion, distinct de l'appréciation d'éligibilité au parcours déjà exigée par L5132-3. Correction du renvoi au L5132-6-1 abrogé dans sa proposition : l'âge de cinquante-sept ans et les difficultés particulières identifient désormais la catégorie bénéficiaire des aides maintenues, sans interdire le contrat unique aux autres personnes éligibles. La première année de l'aide particulière reste ouverte au premier accès à ce dispositif, même après une aide ordinaire, sans recommencer une aide déjà consommée. L'accompagnement n'est pas supprimé.",
    "L5132-6-1 fourni abroge la dérogation spéciale et le plafond de mission de trente-six mois pour les nouvelles missions : contrairement au brouillon antérieur, ce plafond n'est pas présenté comme maintenu pour l'avenir. Les missions et contrats antérieurs gardent leurs règles sans prolongation automatique. R5132-10-13-1/2 lus dans le corpus (LEGIARTI000043996457/459) maintiennent aide particulière, prorata et taux de 100 % du socle la première année puis 70 % ; ces nouveaux renvois normatifs explicites ne sont pas fournis comme cibles et leur texte proposé manque. Le premier alinéa donne un sens opératoire au renvoi de R5132-10-13-1 à la catégorie de l'ancien L5132-6-1 ; le troisième adapte le point de départ de la première année au premier accès à l'aide particulière pour éviter que la signature plus ancienne du contrat unique absorbe son avantage. Il ne remet pas à zéro une aide particulière déjà commencée. Coordonner R5132-10-13-1/2 par acte du rang requis ; leurs textes ne sont pas présentés comme réécrits. La qualification de difficultés particulières reprend L5132-6-1 officiel et n'est pas une restriction nouvelle. L5132-3, lu intégralement en source locale, conserve l'appréciation d'éligibilité et l'accompagnement ; son nouveau renvoi exprès vise cette fonction existante, sans dossier supplémentaire. L5132-6 fourni fonde l'emploi unique et les garanties intérimaires. Aucune date de promulgation ni nouveau taux d'aide n'est inventé ; le coût de l'accès anticipé n'est pas chiffré.",
    'material_reduction',
    "La source officielle entière imposait douze mois de parcours, un CDD antérieur et un examen spécifique avant le CDI d'inclusion. Ces obstacles sont retirés ; l'âge et les difficultés sont conservés pour identifier l'aide particulière, ouverte aux futures situations. L'examen d'éligibilité général et l'accompagnement demeurent. La réduction n'est pas une baisse d'impôt ni un droit à aide illimité.",
    "Les conditions financières et le non-cumul des aides subsistent. Le renvoi de R5132-10-13-1 doit être réécrit hors lot ; aucune suppression automatique des critères généraux de parcours ni versement rétroactif n'est affirmé. Le coût de l'accès anticipé reste non chiffré.",
    "Aucune charge nouvelle n'est identifiée : l'âge et les difficultés reprennent la catégorie déjà légale, l'examen supplémentaire est retiré et aucune demande, attestation ou autorisation ne le remplace. L'appréciation générale de L5132-3 reste distincte et préexistante.",
    [effect('deadline_reduced', 'acces-immediat-inclusion-etti',
        'Suppression de la durée minimale de parcours avant accès au dispositif favorable d’inclusion.',
        "Au moins douze mois après le début du parcours pour les personnes d'au moins cinquante-sept ans concernées.",
        "Accès dès le début du parcours, sous les autres conditions d'aide, sans attente minimale.", 'other',
        "Personnes d'au moins cinquante-sept ans rencontrant des difficultés sociales et professionnelles particulières.",
        'Parcours nouveaux et en cours dès la réforme ; aides antérieures conservées, sans versement rétroactif général.',
        'Aucune démarche de substitution ; les contrôles généraux existants demeurent.',
        "à l'issue d'un délai minimal de douze mois après le début de leur parcours d'insertion par l'activité économique.",
        "Ce bénéfice est ouvert dès le début du parcours d'insertion par l'activité économique."),
     effect('obligation_removed', 'acces-immediat-inclusion-etti',
        'Retrait du CDD préalable et du second examen spécifique d’accès, sans retrait de l’accompagnement.',
        'Examen spécifique par l’entreprise de la situation et des actions réalisées dans le CDD précédent avant conclusion du CDI d’inclusion.',
        'Ni CDD préalable ni examen distinct de l’éligibilité au parcours ; accueil et accompagnement conservés.', 'legal_duty',
        "Bénéficiaires de l'aide particulière d'inclusion et entreprises de travail temporaire d'insertion.",
        'Application aux situations futures et aux parcours commencés, avec conservation des droits antérieurs.',
        'Aucune attestation, demande à un prescripteur ou autorisation additionnelle de remplacement.',
        "Ce contrat est conclu après examen par l'entreprise de travail temporaire d'insertion de la situation de la personne au regard de l'emploi et des actions d'accompagnement et de formation effectuées dans le cadre du contrat à durée déterminée précédent conclu en application du premier alinéa de l'article L. 5132-6.",
        "Ni une attente minimale de douze mois, ni un contrat à durée déterminée antérieur, ni un examen supplémentaire distinct de l'appréciation de l'éligibilité au parcours prévue à l'article L. 5132-3 ne sont exigés."),
     effect('coordination', 'contrat-unique-insertion-aides',
        'Préservation du calendrier favorable de première année de l’aide particulière lors de son premier accès sous contrat unique.',
        "La source renvoie au CDI d'inclusion distinct ; R5132-10-13-2, lu dans le corpus, fixe 100 % du socle pour la première année d'exécution de ce CDI, puis 70 %. Un contrat unique signé plus tôt ne doit pas absorber cette première année.",
        "La première année de l'aide particulière est celle de son premier accès pour cet emploi ; taux, prorata et règles de versement inchangés. Les périodes d'aide ordinaire ne sont pas déduites ; aucune aide particulière déjà commencée n'est remise à zéro.",
        'regime', "Personnes d'au moins cinquante-sept ans éligibles à l'aide particulière d'inclusion, notamment après une aide ordinaire.",
        "Situations nouvelles et en cours sous contrat unique ; calendriers d'aides particulières antérieurement accordées conservés, sans cumul sur un même poste et une même période.",
        "Aucun taux nouveau, registre ou demande supplémentaire ; suivi des périodes déjà financées dans le dispositif existant. Effet public net non chiffré.",
        "un contrat à durée indéterminée d'inclusion prévu à l'article L. 5132-6-1",
        "Pour les emplois relevant du contrat unique, la première année prévue à l'article R. 5132-10-13-2 est la première année d'accès à l'aide particulière pour l'emploi concerné.")],
    'normative_reduction', removed=[
        "Attente minimale de douze mois depuis le début du parcours pour accéder au régime particulier d'inclusion.",
        "Passage préalable imposé par un contrat à durée déterminée avant accès au régime favorable d'inclusion.",
        "Examen préalable supplémentaire de la situation et des actions du CDD précédent, distinct de l'appréciation existante d'éligibilité au parcours."])

make(4, S[4]['previous_draft']['proposed_xml'],
    "Maintien de la proposition antérieure après examen des six mentions : l'écrit identifie les parties à la mise à disposition et sa preuve ; noms, tâches, lieu et terme délimitent l'affectation ; la rémunération de comparaison et les équipements assurent égalité et sécurité. Une coupe supplémentaire de ces données n'est pas justifiée. La seule réforme est la coordination explicite du terme commercial avec le contrat unique : il n'emporte ni fin d'emploi ni nouvel essai. Les reformulations conservées ne sont pas comptées comme réduction.",
    "Les 1° à 6° sont conservés dans leur ordre ; le 4° porte seulement sur la mise à disposition. Le 5° garde la référence après essai, la qualification équivalente, le même poste, primes et accessoires ; le 6° ne modifie pas la répartition de la fourniture des équipements. Aucun renvoi normatif nouveau n'est ajouté. L5132-11-1 fourni distingue parcours et emploi ; son régime des dispenses favorables de préavis n'est pas remplacé par la seule arrivée du terme commercial. Les anciens contrats gardent leur régime. Les procédures collectives et autorisations protectrices ne sont pas supprimées par cette coordination.",
    'coordination_only',
    "La source officielle entière comporte six mentions nécessaires au contrat de mise à disposition. Elles sont toutes maintenues ; aucune suppression de charge documentaire n'est revendiquée. L'ajout distingue la durée de l'affectation de l'emploi sans terme dans le nouveau régime général ; c'est une coordination de cette réforme, pas une seconde fusion de contrats.",
    "Aucun taux, salaire, durée d'emploi garantie ou préavis spécial n'est fixé ici. L'allègement global du contrat unique ne se déduit pas de cet article ; les obligations autonomes de mise à disposition et de sécurité demeurent.",
    "Aucune charge documentaire nouvelle n'est identifiée : les six mentions et l'écrit sont déjà exigés. La continuité de l'emploi et l'absence d'un nouvel essai découlent du régime du contrat unique ; leur coût d'emploi n'est pas chiffré ni présenté comme une économie.",
    [effect('coordination', 'contrat-unique-emploi-sans-terme',
        'Distinction du terme de mise à disposition et de la rupture du nouvel emploi.',
        'Le contrat avec l’utilisateur comporte un terme de mise à disposition ; la source ne formule pas cette articulation avec le nouveau contrat unique.',
        'Le terme commercial reste mentionné, mais ne rompt pas le nouvel emploi et ne permet pas un nouvel essai ; anciens contrats préservés.', 'regime',
        'Salariés des associations intermédiaires mis à disposition chez un utilisateur.',
        'Coordination des emplois conclus après la réforme ; les contrats antérieurs gardent leurs droits.',
        'Aucune mention ni pièce supplémentaire ; continuité de l’emploi issue de la réforme générale, sans solde de coût établi.',
        "4° Le terme de la mise à disposition ;",
        "le terme prévu au 4° concerne uniquement la mise à disposition.")])

def aid_coord(i, target, population, source_quote, proposed_quote, notes, extra=''):
    p = S[i]['previous_draft']['proposed_xml']
    return make(i, p,
        "Coordination de fond conservée après seconde passe : retrait de la condition de CDD pour les futures situations éligibles au contrat unique, sans supprimer l'aide. Le contingent de postes, le socle, la modulation annuelle et ses critères définissent l'avantage et empêchent de traiter les aides comme une dette illimitée de l'Etat ; aucune coupe supplémentaire de ces garanties financières n'est justifiée. Les modifications de rédaction seules ne sont pas comptées comme allègements. " + extra,
        notes,
        'coordination_only',
        "Comparée à la source officielle entière, la proposition conserve les composantes et critères d'aide et adapte leur support au contrat unique, avec protection des anciens droits et des situations futures. Aucun prélèvement n'est supprimé ici et la condition contractuelle est coordonnée sous la même mesure que les autres aides d'insertion. " + extra,
        "Les limites de postes, conditions d'éligibilité et de versement ainsi que la durée propre de l'aide demeurent. Arrêtés et conventions hors lot doivent être adaptés ; aucun droit au versement pendant toute la vie du CDI ni coût public net n'est démontré.",
        "Aucune charge nouvelle n'est identifiée dans cet article : pas de dossier de conversion, de nouveau registre, de justification ou de délai supplémentaire. Le contrat unique relève des règles générales et la fin de l'aide n'en constitue pas un terme ; la continuité d'emploi n'est pas une économie chiffrée.",
        [effect('coordination', 'contrat-unique-insertion-aides',
            "Maintien de l'aide pour les nouveaux emplois éligibles sans support CDD.",
            'La catégorie salariée est rattachée au CDD ; contingent et composantes de l’aide fixés par les règles propres au dispositif.',
            'Même aide ouverte aux contrats uniques éligibles de ' + target + ', sans condition de CDD ; droits anciens et périodes restant éligibles conservés sans nouveau décompte.',
            'regime', population,
            'Nouveaux emplois à compter de la réforme ; aides des anciens contrats et conversions convenues conservées dans leurs périodes éligibles.',
            'Aucune déclaration de remplacement ni suppression des contrôles existants ; emploi sans terme issu de la réforme générale.', source_quote, proposed_quote)],
        'normative_reduction', removed=["Condition de conclusion d'un CDD pour conserver le bénéfice des aides aux futures situations éligibles sous contrat unique ; aucune formalité équivalente de remplacement."])

aid_coord(5, 'L5132-11-1', 'Personnes éligibles employées en insertion par les associations intermédiaires.',
    "en contrat à durée déterminée par les associations intermédiaires ouvre droit",
    "sans condition de conclusion d'un contrat à durée déterminée.",
    "L5132-11-1 fourni organise le parcours distinct du CDI, avec les prolongations favorables et les dispenses de préavis à leur champ propre. R5132-24 lu en source officielle locale conserve prorata des postes, arrêté, revalorisation annuelle et date historique du 1er janvier 2015. Le renvoi à R5132-24 est déjà dans la source, non une cible nouvelle. La note source vise les V et VI de l'article 2 du décret 2021-1128 du 30 août 2021 ; sa portée transitoire n'est ni abrogée ni réinterprétée comme une date future. Adapter les arrêtés et conventions sans rétablir l'exigence de CDD. Aucun taux ni montant nouveau n'est décidé.")

def repeal_framework(i, employer, target, companion):
    p = paras(
        "Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant cette abrogation.",
        employer + " peut organiser des périodes de mise en situation en milieu professionnel pour ses salariés relevant de l'article " + target + ", sans habilitation particulière inscrite dans la convention de financement mentionnée à l'article L. 5132-2. Cette convention n'a plus à préciser le nombre prévisionnel de salariés concernés, les structures d'accueil, les modalités d'accompagnement propres à ces périodes ou leurs objets. Aucune déclaration, liste, annexe ou autorisation équivalente ne remplace ces mentions.",
        "Chaque période reste soumise à la prescription, à la convention individuelle et à l'accord de l'employeur, ainsi qu'aux conditions et protections du chapitre V du présent titre. Les objets admissibles, les objectifs individuels et le suivi du bénéficiaire demeurent régis par ce chapitre. L'accueil et l'accompagnement dus au salarié ne sont pas supprimés.",
        "La suppression s'applique aux périodes organisées et aux formalités restant à accomplir à compter de cette entrée en vigueur, y compris au cours d'un contrat de travail antérieur. Aucune régularisation ou mise à jour de la convention de financement n'est exigée sur le seul fondement du présent article. Les actes valablement accomplis, les conventions individuelles, les aides accordées, les créances, les droits acquis et les recours relatifs aux effets antérieurs demeurent régis par les règles qui leur étaient applicables. Les clauses reprenant seulement les mentions supprimées cessent de les imposer pour l'avenir. La durée d'une immersion ne fixe pas celle du contrat de travail ; les nouveaux emplois relèvent du contrat unique à durée indéterminée.")
    make(i, p,
        "Abrogation intégrale de la norme spéciale de conventionnement des immersions : outre l'habilitation, le nombre prévisionnel et la liste d'accueillants déjà retirés au brouillon, les mentions répétées des modalités d'accompagnement et des objets dans la convention de financement sont supprimées. Le chapitre V, les conventions individuelles et l'accompagnement de l'insertion suffisent à leur fonction. Aucun formulaire de substitution n'est imposé et aucune protection individuelle n'est abrogée.",
        "Lecture intégrale de " + target + " fourni : son deuxième alinéa autorise les immersions par convention L5135-4. L5135-1 à L5135-8 et D5135-1 à D5135-5 lus dans le corpus public : objets, objectifs, structure d'accueil, référent, tâches, horaires, suivi, sécurité et durées sont déjà encadrés individuellement ; l'accompagnement de l'insertion reste aussi fondé sur L5132-1 et L5132-3. Le réemploi conditionnel prévu au brouillon pour les 3° et 4° est remplacé par leur suppression complète dans la seule convention de financement. " + companion + " imposent encore la convention individuelle et sa copie à l'ASP : cette transmission autonome est un point hors lot à réexaminer, pas une obligation réputée supprimée. Les renvois normatifs à L5132-2 et au chapitre V étaient déjà présents dans le brouillon ; aucun nouveau numéro de cible n'est inventé. Les droits et les effets antérieurs sont conservés sans laisser renaître une mise à jour purement formelle.",
        'material_reduction',
        "La source officielle entière conditionne l'organisation des immersions à la convention de financement et lui impose quatre rubriques supplémentaires. La proposition retire l'ensemble de cette couche, au-delà du brouillon qui gardait encore les 3° et 4°. La même mesure est dédupliquée pour associations intermédiaires et ateliers/chantiers ; elle ne supprime pas la convention individuelle.",
        "Le conventionnement de l'organisme et de ses aides subsiste ; seules les clauses spéciales d'immersion sont retirées. La prescription, l'accompagnement, les limites et la transmission autonome à l'ASP restent applicables. Le coût de conformité évité n'est pas quantifié.",
        "Aucune charge nouvelle n'est identifiée : ni annexe, ni déclaration, ni nouvelle mention individuelle ne remplace les quatre rubriques supprimées. Les informations et protections individuelles rappelées ont déjà leur fondement légal et réglementaire.",
        [effect('obligation_removed', 'suppression-convention-cadre-pmsmp',
            'Suppression des quatre rubriques d’immersion de la convention de financement et de la permission spéciale qu’elle portait.',
            'Convention de financement prévoyant la possibilité d’immersion et précisant effectif prévisionnel, accueillants, accompagnement spécifique et objets.',
            'Aucune habilitation ou rubrique spéciale d’immersion dans cette convention ; convention individuelle, accompagnement et protection maintenus.',
            'legal_duty', employer + ' et ses salariés en insertion.',
            'Périodes et formalités futures, même au cours d’anciens contrats ; effets antérieurs et droits aux aides conservés.',
            'Aucune liste ni annexe de remplacement ; les obligations individuelles existantes demeurent.',
            "1° Le nombre prévisionnel de salariés concernés ;",
            "Cette convention n'a plus à préciser le nombre prévisionnel de salariés concernés, les structures d'accueil, les modalités d'accompagnement propres à ces périodes ou leurs objets.")],
        'full_repeal', scope="Suppression de la permission spéciale et des quatre mentions obligatoires d'immersion dans la convention de financement, sans retirer les conventions individuelles ni l'accompagnement.")

repeal_framework(6, "L'association intermédiaire signataire de la convention de financement", 'L. 5132-11-1', 'D5132-26-2 et D5132-26-4')
repeal_ratio(7, 'L5132-11-1',
    "Coupe supplémentaire par rapport au brouillon : les anciens contrats bénéficient aussi de la suppression pour leur exécution future, sans attendre une conversion convenue ; les droits et irrégularités relatifs aux périodes antérieures restent distincts.")

aid_coord(8, 'L5132-15-1', "Salariés des ateliers et chantiers d'insertion ; personnes détenues sous contrat d'emploi pénitentiaire conservées séparément.",
    "en contrat à durée déterminée ou l'emploi des personnes détenues ayant signé un contrat d'emploi pénitentiaire",
    "sans condition de conclusion d'un contrat à durée déterminée.",
    "L5132-15-1 et R5132-38 fournis ont été lus en entier, sources, notes et propositions. Le contrat d'emploi pénitentiaire demeure un régime distinct ; la formule de la proposition ne le transforme pas en contrat privé. La note source vise les V et VI de l'article 2 du décret 2021-1128 du 30 août 2021 et conserve son champ historique. Le socle, la part modulée, les trois critères, le prorata et la revalorisation sont conservés ; adapter les arrêtés et conventions hors lot sans exiger de nouveau CDD. Aucune nouvelle cible normative n'est ajoutée.",
    "Le régime d'emploi pénitentiaire et son aide ne sont pas assimilés au contrat privé.")

make(9, S[9]['previous_draft']['proposed_xml'],
    "Coordination de l'aide maintenue : retrait de la référence au CDD comme support des montants et de la revalorisation pour les futurs salariés en insertion. Le versement par poste occupé, son prorata, les deux composantes, l'arrêté conjoint et l'indexation annuelle sur le SMIC ont une fonction de détermination et de maintien de l'avantage ; leur suppression supplémentaire diminuerait sa sécurité ou ses bénéficiaires et n'est pas justifiée. Le brouillon est donc conservé, sans attribuer de réduction aux seules reformulations.",
    "L5132-15-1 fourni ne transforme pas les durées d'accompagnement en terme d'emploi. R5132-37 est coordonné dans le présent lot ; le R5132-38 fourni comme cible conserve aussi les deux catégories salariée et pénitentiaire. Le montant maximal modulé reste un pourcentage fixé par arrêté, non inventé ici. La revalorisation annuelle en fonction du SMIC et le 1er janvier 2015 sont conservés comme règle et date historiques. La note sur les V et VI de l'article 2 du décret 2021-1128 reste à son champ propre. Aucun nouveau renvoi normatif n'est ajouté. Les arrêtés extérieurs doivent ouvrir leurs montants aux emplois uniques éligibles, sans réduire l'aide ni rétablir le CDD.",
    'coordination_only',
    "La source officielle entière fixe le versement par poste et renvoie aux arrêtés pour les salariés en CDD et les personnes détenues. La proposition maintient ces paramètres et leur revalorisation en retirant l'obstacle du support CDD. C'est la coordination de la même mesure de maintien des aides, sans baisse de contribution ni nouvelle économie autonome.",
    "Les montants et pourcentages ne figurent pas dans cet article et ne sont pas reconstitués. Les arrêtés hors lot, l'éligibilité, la durée des aides et le régime pénitentiaire demeurent distincts ; aucune hausse d'aide générale ou baisse nette de coût public n'est démontrée.",
    "Aucune charge nouvelle n'est identifiée : le prorata et les arrêtés annuels existaient déjà ; aucune démarche de conversion ou preuve périodique n'est ajoutée. L'ouverture au contrat unique maintient un avantage, sans financer une mesure par une réduction d'aide implicite.",
    [effect('coordination', 'contrat-unique-insertion-aides',
        'Application des montants et de la revalorisation aux futurs contrats uniques d’insertion.',
        'Montants et versement arrêtés pour salariés recrutés sous CDD, avec catégorie pénitentiaire distincte et revalorisation SMIC annuelle depuis le 1er janvier 2015.',
        'Mêmes règles pour les nouveaux emplois éligibles sans condition de CDD ; prorata, catégorie pénitentiaire et revalorisation conservés.', 'regime',
        'Organismes conventionnés en atelier ou chantier d’insertion et leurs postes éligibles.',
        'Nouvelles embauches après réforme ; contrats antérieurs et périodes éligibles après conversion protégés, sans nouveau décompte.',
        'Aucune formalité ajoutée ; maintien des règles de détermination existantes.',
        "pour les salariés en insertion recrutés sous contrat de travail à durée déterminée",
        "les montants et la revalorisation prévus pour les salariés en insertion s'appliquent aux emplois éligibles de l'article L. 5132-15-1 sans condition de CDD.")],
    'normative_reduction', removed=["Réservation des montants et de la revalorisation des aides d'insertion aux recrutements en CDD pour les futures situations éligibles ; cette condition n'est pas remplacée."])

repeal_framework(10, "L'organisme conventionné au titre d'un atelier ou chantier d'insertion signataire de la convention de financement", 'L. 5132-15-1', 'D5132-43-2 et D5132-43-4')
repeal_ratio(11, 'L5132-15-1',
    "Coupe supplémentaire par rapport au brouillon : la suppression couvre aussi l'exécution future des anciens contrats sans attendre leur conversion ; aucune créance ni réparation d'une irrégularité antérieure n'est effacée.")

# Chaque contrôle distingue le texte officiel et la proposition dont l'empreinte est fournie.
contexts = {
    0: "La suppression du ratio global d'immersion des entreprises d'insertion",
    1: "Le contenu de la convention des entreprises de travail temporaire d'insertion",
    2: "L'aide ordinaire des entreprises de travail temporaire d'insertion",
    3: "L'accès immédiat à la catégorie favorable d'inclusion et à ses aides",
    4: "Le contrat commercial de mise à disposition de l'association intermédiaire",
    5: "L'aide au poste des associations intermédiaires",
    6: "La suppression de la couche de conventionnement des immersions des associations intermédiaires",
    7: "La suppression du ratio d'immersion des associations intermédiaires",
    8: "L'aide des ateliers et chantiers d'insertion, distincte de l'emploi pénitentiaire",
    9: "Les montants, le prorata et la revalorisation de l'aide des ateliers et chantiers",
    10: "La suppression de la couche de conventionnement des immersions des ateliers et chantiers",
    11: "La suppression du ratio d'immersion des ateliers et chantiers",
}
common = {
    'L1234-1': " ne modifie pas directement L1234-1 ni ses 1° à 3°. La source prévoit les paliers de six mois et deux ans ; la proposition substitue quinze jours calendaires aux nouveaux emplois seulement. Ni une échéance d'aide, ni une fin d'immersion ou de mise à disposition ne vaut notification de rupture. Le point de départ relève de L1234-3 proposé selon coordination.json, cible non fournie dans ce fichier : lendemain de la présentation ou réception écrite. Anciennes règles et procédures collectives ou protectrices restent distinctes.",
    'L1221-2': " doit être lu avec la proposition de L1221-2, et non avec la seule dérogation CDD de sa source officielle. Tout nouvel emploi privé est sans terme, y compris en insertion ; la durée d'une mission, immersion, convention, formation ou aide n'est pas celle de l'emploi. Le texte final préserve les anciens contrats et leurs créances sans autoriser de nouveau CDD ni de renouvellement à terme ; il ne reconduit pas un emploi public ou pénitentiaire dans ce champ privé.",
    'L1234-9': " ne fixe pas d'indemnité de rupture et ne transforme pas la fin du dispositif en licenciement. L1234-9 proposé distingue les nouveaux contrats : zéro indemnité ordinaire avant un an mesuré au terme effectif, préavis inclus, puis 0,20 mois par année totale, fractions en mois complets et plafond de six mois, employeur seul, avec son exception de faute grave. La source et les anciens contrats ont leur condition de huit mois ; les droits antérieurs, congés, salaires, dommages et indemnités spéciales ne sont pas effacés.",
    'L5135-7': " conserve l'interdiction autonome de substituer une immersion à un emploi permanent, temporairement accru, saisonnier ou de remplacement. La proposition de L5135-7 remplace la référence au CDD saisonnier par sa définition propre ; retirer un ratio ou une formalité ne permet donc ni emploi gratuit ni retour du CDD. L'interdiction n'a pas de seuil d'ancienneté ni de préavis ; les droits antérieurs et les protections de chaque immersion restent applicables.",
}

for i, a in enumerate(A):
    key = a['code_id'] + '|' + a['source_id']
    checks = []
    for tk in R['requirements'][key]:
        t = R['targets'][tk]
        n = t['number']
        c = contexts[i]
        if n in common:
            assessment = c + common[n]
        elif n == 'L5132-5':
            assessment = "Le renvoi source vise L5132-5 et son deuxième alinéa d'autorisation des immersions ; sa proposition distingue parcours initial de quatre mois, limite de vingt-quatre mois et prolongations favorables de l'emploi indéfini. D5132-10-3 ne calcule plus 25 % sur aucune de ces durées. Les anciennes fractions restent régies par leur droit, les fractions futures sont libérées du ratio même sans conversion. Les suspensions et départs favorables sans préavis de la cible ne sont pas supprimés."
        elif n == 'L5132-11-1':
            assessment = c + " vise le champ des associations intermédiaires de L5132-11-1. Son deuxième alinéa permet les immersions par convention individuelle ; ses quatre mois initiaux, vingt-quatre mois et prolongations de parcours ne sont pas un terme du CDI. Le plancher spécial de vingt heures et ses dispenses, les prolongations favorables et la sortie sans préavis pour embauche restent à leur champ propre. Le texte final ne ferme ni les aides futures ni les droits anciens et ne demande pas de nouveau CDD."
        elif n == 'L5132-15-1':
            assessment = c + " vise les emplois privés des ateliers et chantiers dans L5132-15-1, notamment son deuxième alinéa pour les immersions. Les périodes de quatre mois, vingt-quatre mois, prolongations de formation et décisions exceptionnelles d'un an jusqu'à soixante mois restent des périodes de parcours dans sa proposition. Le contrat d'emploi pénitentiaire ne devient pas un CDI privé. Les dispenses favorables de préavis, les droits anciens et les aides futures ne sont pas supprimés par le texte final."
        elif n == 'L5132-6':
            if i == 1:
                assessment = "Le 1° f) du brouillon rétablissait l'exclusivité et l'intégralité des moyens de L5132-6 officiel, alors que sa proposition les retire expressément. La lettre f) est donc abrogée ; le 2° décrit seulement les moyens du projet aidé. L'affectation des aides, l'éligibilité et le contrôle restent nécessaires. La cible prévoit emploi sans terme, section 4 bis et garanties d'intermissions ; la convention ne leur oppose ni plafond de mission ni ancienneté d'accès artificielle."
            else:
                assessment = c + " relève du contrat unique de L5132-6 proposé, qui retire l'exclusivité, ouvre la section 4 bis et garantit rémunération mensuelle et ancienneté pendant les intermissions. La source officielle exclut cette section : ce sont des réformes proposées, pas le droit actuel. Les anciens contrats restent protégés sans nouveau CDD ; la durée d'une aide ou mission n'est pas un terme. Le coût de ces garanties n'est pas assimilé à une baisse de prélèvement dans cet article."
        elif n == 'L5132-6-1':
            assessment = "Le brouillon renvoyait au CDI d'inclusion de L5132-6-1 comme si ce régime et son plafond de trente-six mois demeuraient pour l'avenir. La cible propose au contraire son abrogation en préservant les aides aux personnes d'au moins cinquante-sept ans, y compris futures. Le texte final retire ce renvoi opératoire et identifie la catégorie favorable dans D5132-10-15, sous L5132-6, sans attente de douze mois ni CDD. Les missions anciennes gardent leur plafond et leurs droits sans prolongation automatique ; aucune ancienneté de rupture n'est modifiée."
        elif n == 'R5132-10-12':
            assessment = "Le 3° de R5132-10-7 renvoie au nombre de postes ouvrant l'aide, non à la durée de l'emploi. R5132-10-12 fourni conserve socle, part modulée annuelle, trois critères et aide particulière future. Le texte final de cette cible figure aussi au présent lot ; il applique le dispositif favorable sans demande additionnelle. Ni le nombre de postes ni la convention ne reconstituent un CDD ; les aides anciennes demeurent et la fin du financement ne vaut pas notification de rupture."
        elif n == 'R5132-38':
            assessment = "R5132-37 renvoie exactement à R5132-38 pour le versement par poste à temps plein, son prorata, les montants arrêtés et la revalorisation annuelle SMIC depuis le 1er janvier 2015. La proposition fournie et le texte final du lot gardent les deux catégories, salariée et pénitentiaire, sans condition future de CDD. Aucun pourcentage ou montant absent de la source n'est inventé ; aucun décompte d'ancienneté ni préavis ne découle de la durée de l'aide."
        else:
            raise AssertionError(n)
        checks.append(dict(target_key=tk, view_sha256=t['view_sha256'], assessment=assessment))
    a['reference_checks'] = checks

Path('answer.json').write_text(json.dumps(A, ensure_ascii=False, indent=2) + '\n')
print('answer.json :', len(A), 'articles')
