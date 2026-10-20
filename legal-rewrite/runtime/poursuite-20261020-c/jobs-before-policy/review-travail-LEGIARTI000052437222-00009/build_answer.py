import json
import re
from html import unescape
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
references = json.loads(Path('reference-targets.json').read_text())
by_number = {a['number']: a for a in sources}
answer = []
for src in sources:
    old = src['previous_draft']
    answer.append({
        **{k: src[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')},
        'proposed_xml': old['proposed_xml'],
        'reason': '',
        'review_notes': '',
        'status': 'rewrite_draft',
    })
out = {a['number']: a for a in answer}

def replace(number, old, new):
    assert out[number]['proposed_xml'].count(old) == 1, (number, old)
    out[number]['proposed_xml'] = out[number]['proposed_xml'].replace(old, new)

replace('L2312-26',
    "Elles comprennent les éléments qui ont conduit l'employeur à recourir, pendant l'année écoulée, aux contrats à durée déterminée antérieurement conclus, aux missions de travail temporaire ou au portage salarial, et ceux qui pourraient le conduire à recourir à des missions de travail temporaire ou au portage salarial pendant l'année à venir.",
    "Elles comprennent les éléments qui ont conduit l'employeur à recourir, pendant l'année écoulée, aux contrats à durée déterminée antérieurement conclus, aux missions de travail temporaire ou au portage salarial. Aucune justification spécifique des recours envisagés pour l'année suivante n'est exigée au titre du présent 9°. Cette dispense ne supprime pas l'information sur les perspectives générales d'emploi nécessaire à la consultation du comité.")
replace('L2312-26',
    "L'employeur indique où ce contenu est accessible et fournit les seuls compléments manquants ou modifiés nécessaires à une consultation utile.",
    "Seuls les compléments manquants ou modifiés nécessaires à une consultation utile sont fournis.")
replace('L2312-26',
    "La dispense de remise répétée s'applique aux mises à disposition restant à effectuer à compter de l'entrée en vigueur de la présente rédaction, y compris pour des données de périodes antérieures, sans reprise des consultations achevées ni remise en cause des droits et recours antérieurs.",
    "Les dispenses de remise répétée et de justification spécifique des recours envisagés pour l'année suivante s'appliquent aux mises à disposition restant à effectuer à compter de l'entrée en vigueur de la présente rédaction, y compris au cours d'une consultation déjà engagée. Aucun document déjà fourni n'est à refaire. Les consultations achevées, les droits et les recours antérieurs ne sont pas remis en cause.")

replace('L2312-70',
    "À cette réunion, l'employeur communique au comité le nombre de ces salariés, les motifs du recours à leurs contrats ou à leur mise à disposition et le nombre de journées de travail qu'ils ont accomplies depuis la dernière communication sur ce sujet. Pour les informations exactes et à jour déjà effectivement accessibles au comité, l'indication de leur emplacement et l'accès utile à leur contenu tiennent lieu de nouvelle communication ; seuls les éléments manquants ou modifiés sont fournis.",
    "À cette réunion, l'employeur communique au comité le nombre de ces salariés et les motifs du recours à leurs contrats ou à leur mise à disposition. Aucun décompte particulier des journées de travail accomplies depuis la dernière communication n'est exigé au titre du présent article. Les informations exactes et à jour déjà effectivement accessibles au comité et utilisables pour cet examen n'ont pas à être communiquées une seconde fois ; seuls les éléments manquants ou modifiés sont fournis.")
replace('L2312-70',
    "La dispense de communication répétée s'applique aux réunions tenues à compter de l'entrée en vigueur de la présente rédaction, sans remise en cause des droits et recours antérieurs.",
    "Les dispenses de décompte particulier et de communication répétée s'appliquent aux réunions tenues à compter de l'entrée en vigueur de la présente rédaction, y compris lorsque les données concernent des périodes antérieures. Les informations sur les effectifs et le temps de travail dues sur un autre fondement ainsi que les droits et recours antérieurs sont conservés.")

replace('L2312-71',
    "Si le comité a déjà reçu le rapport ou y a effectivement accès, l'employeur n'est pas tenu de le transmettre de nouveau et en indique la référence lors de la communication de sa réponse. Celle-ci précise, en tant que de besoin, les mesures prises pour faire cesser les abus et réduire la précarité, sans obligation d'établir un plan distinct.",
    "Si le comité a déjà reçu le rapport ou y a effectivement accès et peut l'utiliser utilement, sa transmission n'a pas à être répétée. La réponse précise, en tant que de besoin, les mesures prises pour faire cesser les abus et réduire la précarité. Ces mesures n'ont pas à être organisées dans un plan de résorption de la précarité ni à faire l'objet d'un document distinct de la réponse.")
replace('L2312-71',
    "Les dispenses de double transmission et de plan distinct s'appliquent",
    "Les dispenses de transmission répétée et de plan de résorption de la précarité s'appliquent")

# Une stipulation de terme interdite ne doit jamais faire disparaître une protection.
out['L2412-1']['proposed_xml'] += "<p>La stipulation d'un terme en méconnaissance du contrat unique ne peut être opposée au salarié pour le priver des protections applicables à son emploi et à son mandat. Elle ne dispense pas l'employeur de l'autorisation préalable requise au titre du chapitre Ier.</p>"
out['L23-114-2']['proposed_xml'] += "<p>La stipulation d'un terme interdit ne prive pas le salarié de la protection prévue au présent article.</p>"
replace('L2412-11',
    "Pour le contrat unique et les conversions convenues, la protection contre le licenciement relève de l'article L. 2411-18, sans interruption des périodes protégées.",
    "Pour le contrat unique et les conversions convenues, les garanties de l'article L. 231-11 du code de la sécurité sociale et la protection contre le licenciement prévue à l'article L. 2411-18 demeurent applicables, sans interruption des périodes protégées.")

out['L2312-26']['reason'] = (
    "Réforme de fond : le décompte du II, 5°, d), devenu sans objet avec la suppression du minimum légal général à temps partiel, reste supprimé ; cette seconde passe retire en plus la justification spécifique des recours envisagés pour l'année suivante au II, 9°. Les perspectives générales d'emploi, les motifs des recours passés et tous les autres thèmes sont maintenus. La règle de réemploi est conservée, mais sans obligation supplémentaire de signaler un emplacement. Elle prolonge un mécanisme déjà présent dans L2312-18 et n'est donc pas présentée comme une réduction entièrement nouvelle. La coordination distingue anciens CDD, missions et emploi indéterminé et conserve les avantages des situations futures éligibles. Aucun prélèvement n'est supprimé par une rubrique d'information.")
out['L2312-26']['review_notes'] = (
    "Lecture intégrale de la source, de sa note et du brouillon. La note du 24 octobre 2025 concerne la rédaction entrée en vigueur le 1er janvier 2026, pas la date de la réforme proposée. Les 1° à 9°, les 4° bis et ter et les lettres a à e restent identifiables ; le d est explicitement abrogé. L2312-15, L2312-18, L2312-21 et L2312-36 ont été lus dans le corpus : information précise, examen utile, base actualisée, confidentialité et recours subsistent. Les perspectives générales sur trois années prévues par L2312-36 ne sont pas supprimées ; seule l'explication spéciale par forme de recours de l'année suivante disparaît. Coordonner R2312-8/R2312-9 et les règlements de mise à disposition pour ne pas rétablir les deux exigences retirées ; leurs tableaux ne sont pas réécrits dans ce lot. Maintenir les dispenses conventionnelles et spéciales de L3123-7, le volume contractuel et le minimum parental de L3123-3. Aucun relèvement automatique des régimes annuels ou plurihebdomadaires à 1607 heures. Les aides à la formation, à l'insertion et au logement et les obligations de santé, d'égalité et de handicap restent à leur champ propre. Les contraintes européennes d'information-consultation et de non-discrimination demandent une vérification d'ensemble ; elles ne sont pas écartées. Aucun solde budgétaire chiffré.")
out['L2312-26']['benefit_review'] = (
    "Le choix d'un avis unique ou d'avis séparés reste ouvert. La couverture conventionnelle du droit d'expression conserve son effet dérogatoire. Les informations relatives au handicap, aux accidentés du travail, aux invalides de guerre et assimilés et aux invalides civils ne constituent pas des taxes : les protections et facilités correspondantes sont maintenues. Apprentissage, professionnalisation, reconversion, CPF, stages, accompagnement dans l'emploi et initiative emploi conservent leurs droits, aides, exonérations et dispenses pour les situations futures éligibles dans le contrat unique ; la durée de formation ou d'aide ne termine pas l'emploi. L'information sur le logement des travailleurs étrangers subsiste, sans suppression de la contribution de construction ni des garanties autonomes de logement. La suppression du décompte des dérogations à temps partiel ne ferme ni les dispenses favorables de L3123-7, notamment personnelles, de cumul, de remplacement, d'insertion, d'âge et d'études, ni les minima conventionnels plus favorables, ni le minimum parental spécial. Les salaires, congés, droits de formation et recours ne sont pas réduits par les deux dispenses d'information. Aucune condition fiscale ou sociale nouvelle n'est exigée pour conserver ces avantages.")

out['L2312-70']['reason'] = (
    "Réforme de fond supplémentaire au brouillon : suppression du calcul spécial des journées accomplies depuis la dernière communication, dont le point de départ variable impose un suivi supplémentaire ; les effectifs et les motifs restent dus et permettent d'examiner l'accroissement. La majorité, la prochaine réunion ordinaire et le point de comparaison ne changent pas. La réutilisation de l'information accessible demeure, sans nouvelle indication formelle d'emplacement. Le suivi vise les salariés mis à disposition même sous CDI et les anciens CDD sans permettre une nouvelle embauche à terme. Il ne s'agit ni d'abolir l'alerte ni de supprimer les informations générales sur le temps de travail.")
out['L2312-70']['review_notes'] = (
    "Source, note et brouillon relus intégralement. La majorité porte sur les membres du comité ; aucun remplacement par les seuls titulaires. Le nombre total est comparé à la dernière réunion ayant traité ce sujet ; le calcul des journées depuis la dernière communication est, lui, expressément retiré pour les réunions futures, même portant sur des périodes passées. Les données générales d'effectifs et de temps de travail conservent leurs bases autonomes. L2312-15 et L2312-18 permettent déjà la mise à disposition : la dispense de répétition n'est pas comptée comme une seconde suppression certaine. L1251-58-1 à L1251-58-3 ont été lus : un intérimaire peut déjà être en CDI ; sa prise en compte ne crée pas une population d'information entièrement nouvelle. Coordonner les textes de suivi et L2312-26/L2312-71 ; l'inspection peut toujours examiner les abus. La note de 2017/2018 n'est pas la date de la réforme. Pas de réduction d'effectifs déclarés, d'exonération sociale ni de taux fiscal déduite de cet allègement documentaire.")

out['L2312-71']['reason'] = (
    "La saisine de l'inspection, ses compétences, le rapport de constatations et la réponse motivée sont nécessaires à la prévention des abus et sont conservés. La réduction porte exactement sur l'obligation d'organiser les moyens correctifs dans un plan de résorption de la précarité ; la source n'exigeait pas expressément un second document matériel, ce qui interdit de compter deux suppressions. La seconde passe précise cette suppression et retire la référence formelle supplémentaire au rapport déjà accessible. Les mesures concrètes nécessaires restent dans la réponse. La saisine couvre les nouveaux CDD illégalement conclus, les anciens contrats, le portage et les missions sous emploi indéterminé. Aucun autre retrait du contrôle effectif n'est justifié.")
out['L2312-71']['review_notes'] = (
    "L'accroissement important reste un motif de saisine, pas une présomption automatique d'infraction ; les faits susceptibles de caractériser un abus restent distincts. Les articles L8112-1 et suivants et L8113-7 ne sont pas modifiés par leur renvoi. Les constatations et la réponse conservent leur motivation et leur utilité ; une simple accessibilité théorique du rapport ne suffit pas à la dispense. L2312-15 lu dans le corpus confirme que la mise à disposition utile est déjà une voie d'information : la dispense de répétition n'est pas revendiquée comme une réduction autonome certaine. Aucun délai ni procédure d'inspection n'est supprimé. L'absence de plan obligatoire vaut pour les réponses futures, y compris après constatations anciennes ; elle n'efface ni mesures correctrices dues, ni créances, ni recours. L'intérim en CDI reste suivi ; aucune rémunération générale des périodes sans prestation du portage n'est créée. La note de 2018 reste historique. La nécessité des protections européennes contre les abus n'est pas réputée satisfaite par ce seul lot.")

out['L2314-20']['reason'] = (
    "Coordination de fond déjà présente dans le brouillon, conservée sans changement supplémentaire : le calcul tient compte du contrat indéterminé et de ses intermissions, des anciennes missions et de l'ancienneté conservée lors d'une conversion. Les trois et six mois ainsi que les fenêtres de douze, dix-huit et six mois sont maintenus. Ces seuils organisent le rattachement électoral et l'aptitude à représenter une collectivité de travail, sans dossier, autorisation ni prélèvement redondant à retirer ici. Les intermissions sont déjà assimilées à du travail effectif pour l'ancienneté par L1251-58-2 : aucune extension entièrement nouvelle ni réduction de cotisations n'est comptée à ce titre. Supprimer ces règles spéciales risquerait de rétablir le seuil général d'éligibilité d'un an.")
out['L2314-20']['review_notes'] = (
    "Source entière, note et brouillon relus. L2314-18/L2314-19 lus : les âges de seize et dix-huit ans, les droits civiques, exclusions personnelles et règles d'éligibilité multiple gardent leur fondement ; le seuil spécial d'éligibilité de six mois ne devient pas un an. Le dernier alinéa réduit la fenêtre de recherche à six mois en cas de création ou d'ouverture, non le seuil de trois mois d'électorat. L1251-58-2 lu confirme les intermissions ; aucune fin de mission ne rompt l'emploi. L2314-22 du présent lot règle séparément les exclusions liées au non-rappel. Les listes antérieures et leurs contestations ne sont pas refaites. La date historique limite du 1er janvier 2018 ne devient pas une date future. Aucune autre coupe ni baisse financière démontrée dans cet article.")

out['L2314-22']['reason'] = (
    "La suppression déjà acquise des exclusions pour absence de prochaine mission est conservée : ni le souhait du salarié ni la décision de non-rappel de l'entreprise ne retirent les droits électoraux lorsque l'emploi subsiste. C'est une réduction réelle d'une restriction, pas une simple reformulation. L'existence du lien d'emploi et les conditions d'ancienneté restent nécessaires pour rattacher le vote à une entreprise ; les supprimer ouvrirait le vote hors de cette collectivité. La seconde passe n'identifie donc pas de restriction supplémentaire supprimable sans ce risque. Le texte inclut les intermissions du CDI et les anciens contrats, sans recréer de CDD.")
out['L2314-22']['review_notes'] = (
    "Source, note et brouillon lus intégralement. Les 1° et 2° restent repérables et énoncent la disparition des exclusions pour les listes nouvelles. Le renvoi à L2314-20 conserve trois et six mois sur douze et dix-huit mois, fenêtre ramenée à six mois en cas de création ou ouverture ; les périodes sans mission de l'emploi indéterminé sont incluses. La mesure n'accorde aucun droit après disparition effective du lien d'emploi et ne rétablit pas un contrat rompu. L2314-18 et L2314-19 restent distincts. L2314-23 et L1111-2 ont été lus : le choix de vote vise seulement les salariés mis à disposition relevant de son champ, sans l'étendre mécaniquement à tout intérimaire ni créer de double vote. Les élections antérieures et recours sont préservés. Aucun abaissement d'ancienneté ou de délai de rupture n'est décidé par cet article électoral.")

out['L2315-13']['reason'] = (
    "Le brouillon est conservé après examen des deux obligations réelles : qualifier les heures conventionnelles de délégation comme travail et les rattacher à la paie et aux cotisations. Leur suppression retirerait une rémunération et des droits sociaux essentiels aux représentants entre missions. Le rattachement au contrat indéterminé corrige la référence devenue inadaptée au dernier contrat de mission ; la fiction ancienne reste utile pour les droits du stock. La condition conventionnelle n'est ni durcie ni supprimée en créant une obligation salariale générale nouvelle. Aucune baisse de prélèvement ne résulte de cette coordination et aucune coupe supplémentaire n'est justifiée dans cet article.")
out['L2315-13']['review_notes'] = (
    "Lecture entière de la source, de la note et du brouillon. Les bénéficiaires restent les membres titulaires du comité utilisant leurs heures entre deux missions conformément aux dispositions conventionnelles. L1251-58-2 et L1251-58-3 lus dans le corpus : ancienneté, congés et garantie mensuelle du CDI intérimaire sont maintenus ; la même heure ne reçoit pas deux paiements au titre de cette coordination. La rémunération et les cotisations suivent le CDI en cours ou la fiction du dernier ancien contrat pour les droits qui en relèvent. Ni la fin d'une mission ni une conversion ne remettent à zéro les droits. Les créances d'heures antérieures et leurs recours subsistent. Coordonner les règles de paie applicables aux intermissions ; aucune suppression de cotisation décidée dans un autre code n'est présumée par ce renvoi. Note d'entrée en vigueur de 2018 sans effet sur la date future du projet.")

out['L23-114-2']['reason'] = (
    "La protection des membres, anciens membres et salariés figurant sur la propagande électorale est nécessaire contre les représailles. La prohibition du motif lié au mandat et l'autorisation administrative ne constituent pas deux autorisations redondantes : la première interdit un motif, la seconde contrôle préalablement la rupture. Le brouillon est donc conservé pour son fond, avec une précision empêchant l'employeur d'invoquer un terme interdit pour soustraire un salarié à la protection. Les anciens CDD et les futurs contrats uniques sont distingués. Aucun retrait supplémentaire de procédure ni baisse financière n'est démontré.")
out['L23-114-2']['review_notes'] = (
    "L2411-25 et L2412-16 ont été lus dans le corpus : les six mois après notification de la propagande et les six mois après expiration du mandat demeurent, avec l'imminence protégée dans son champ propre. Le renvoi initial à L23-112-2 et au livre IV reste inchangé ; il ne crée pas un régime d'embauche public ou un nouveau CDD. Le préavis de quinze jours ne remplace aucune autorisation et ne fixe pas la durée totale de la procédure. La source n'a pas de note historique. La continuité de protection concerne aussi les mandats futurs et la qualification irrégulière d'un contrat, sans autoriser de renouvellement à terme. Les simplifications de négociation collective ne suppriment pas l'indépendance des représentants. Aucune procédure collective distincte n'est réputée supprimée.")

out['L2412-1']['reason'] = (
    "La liste protectrice complète et la transition du brouillon sont conservées. Elle ne contient ni taxe ni formulaire autonome ; retirer des mandats ou des contrôles de rupture porterait atteinte à l'indépendance des représentants, aux protections de santé-sécurité ou aux garanties transnationales. La réforme est une coordination du stock des CDD vers le chapitre Ier pour l'emploi indéterminé, sans renouvellement nouveau ni perte de droits. La seconde passe ajoute la règle selon laquelle un terme interdit ne peut priver le salarié des protections du contrat unique. La présence de clauses anciennes ne vaut pas autorisation de les renouveler ; aucune économie supplémentaire n'est attribuée à cette seule coordination.")
out['L2412-1']['review_notes'] = (
    "Les dix-huit entrées, dont 7° bis et ter, sont maintenues sans déplacement. L2411-1 a été lu : il comporte vingt-deux entrées et des numéros différents ; aucun report mécanique de numéro n'est effectué. Le renvoi ajouté au chapitre Ier, dont la liste officielle a été lue dans le corpus, n'est pas une cible distincte fournie dans reference-targets.json. Coordonner L2412-2 à L2412-16, L2421-7 et les règlements de procédure pour le stock et le passage à l'emploi indéterminé ; ces articles hors lot ne sont pas déclarés réécrits. L2421-7 lu renvoie à la procédure de licenciement, pas à une simple notification sous quinze jours. Les catégories agricoles, minières, environnementales et maritimes conservent leurs champs autonomes : aucune durée de contrat public n'est modifiée. Les textes extérieurs non joints ne sont pas réputés vérifiés. L2411-23 lu cite le 19 décembre 1926 alors que le 14° cite le 17 décembre : incohérence préexistante conservée et signalée. Les garanties européennes de représentation demandent coordination explicite. Les aides et exonérations restent ouvertes aux situations futures éligibles selon leurs régimes propres ; la transition ne les limite pas au stock.")

out['L2412-6']['reason'] = (
    "Le brouillon est conservé : rupture anticipée pour faute grave ou inaptitude médicalement constatée et arrivée du terme sans renouvellement d'une clause sont toujours contrôlées pour les anciens CDD. Les deux catégories de représentants européens restent couvertes. L'autorisation protège l'indépendance de la représentation et ne fait double emploi ni avec le constat médical ni avec le préavis. Aucune coupe supplémentaire n'est justifiée. Le relais vers la protection du licenciement du contrat unique est une coordination, pas une suppression d'autorisation ou une nouvelle réduction du nombre des régimes.")
out['L2412-6']['review_notes'] = (
    "Source entière sans note et brouillon relus. Le renvoi ajouté à L2411-11 n'est pas fourni comme cible de reference-targets.json ; son texte officiel entier a été lu dans le corpus et soumet les deux mêmes catégories à autorisation. L2412-1 conserve le stock, les créances, le contrôle de l'arrivée du terme et la protection en cas de terme illicitement stipulé. L2421-7 lu conserve la procédure de licenciement. Aucun renouvellement futur n'est ouvert par la clause ancienne et aucun terme de mission n'est un terme du contrat unique. Les exigences européennes relatives au groupe spécial de négociation et au comité d'entreprise européen ne sont pas effacées ni déclarées intégralement auditées. Le préavis individuel n'absorbe aucun temps d'instruction ou recours distinct.")

out['L2412-7']['reason'] = (
    "Le brouillon est maintenu après examen des motifs et des catégories : le groupe spécial et les représentants des trois comités ont besoin du contrôle préalable contre les représailles. Ni la faute grave ni l'inaptitude ne remplacent ce contrôle. La coordination limite les références au terme et au renouvellement au stock des anciens CDD, tout en relayant la protection du futur contrat unique par L2411-12. Retirer une catégorie, le contrôle de non-renouvellement ou l'autorisation ferait disparaître une protection essentielle ; aucune coupe supplémentaire ni économie chiffrée n'est donc revendiquée.")
out['L2412-7']['review_notes'] = (
    "Le renvoi ajouté à L2411-12 n'est pas une cible fournie dans reference-targets.json ; son texte officiel complet a été lu dans le corpus. Il couvre le groupe spécial et les comités de société européenne, coopérative européenne et société issue d'une fusion transfrontalière. Le renvoi ne substitue pas une autre institution ni une autre opération au texte source. Le stock et les stipulations de terme interdites relèvent de la transition de L2412-1. L2421-7 et les règlements associés doivent rester cohérents ; les règlements ne sont pas réécrits ici. L'autorisation n'est pas obtenue par l'écoulement du préavis individuel. Les exigences européennes d'implication des salariés et de protection des représentants restent identifiées et à coordonner dans leurs textes propres. Source sans note historique ; aucune nouvelle date inventée.")

out['L2412-10']['reason'] = (
    "Le contrôle de la rupture des deux catégories de salariés mandatés est conservé, avec les motifs et la clause de renouvellement de la source. Les simplifications de négociation collective n'enlèvent ni le mandat ni le risque de représailles : l'autorisation demeure nécessaire et ne constitue pas une transmission répétée à une commission. La transition du brouillon est donc conservée sans coupe supplémentaire ; elle réserve les termes anciens et renvoie le contrat unique à la protection de licenciement appropriée. Cette coordination n'est pas comptée comme une baisse de prélèvement ou un nouveau retrait de procédure.")
out['L2412-10']['review_notes'] = (
    "Le renvoi ajouté à L2411-4 n'est pas fourni comme cible dans reference-targets.json ; son texte officiel entier a été lu dans le corpus. Il protège dès l'imminence connue de la désignation et pendant douze mois après la fin du mandat, avec point de départ à la fin de la négociation matérialisée par procès-verbal de désaccord si aucun accord n'a été conclu. Ces règles ne sont pas ramenées à quinze jours ou au seul mandat en cours. Les renvois initiaux L2232-23-1/L2232-26 demeurent : aucune majorité, aucun consentement ni mandat syndical supprimé par une coordination au contrat unique. L2412-1 et L2421-7 assurent stock et procédure sans nouvelle possibilité de CDD. Les créances et recours, y compris contre une rupture discriminatoire dès le début de l'emploi, subsistent. Pas de note source historique.")

out['L2412-11']['reason'] = (
    "Le renvoi à la protection des administrateurs et membres des conseils des caisses est nécessaire ; sa suppression retirerait une garantie d'indépendance sans éliminer de doublon prouvé. Le brouillon est conservé avec une précision : le futur contrat unique et les conversions continuent de relever aussi des garanties de L231-11 du CSS, et pas uniquement d'une lecture étroite du renvoi à L2411-18. Les anciennes durées, candidatures, prolongations saisonnières et recours restent à leur champ. Il s'agit d'une coordination protectrice, sans autorisation supprimée ni cotisation diminuée.")
out['L2412-11']['review_notes'] = (
    "L231-11 du CSS a été lu intégralement dans reference-targets.json, source et proposition distinguées. Sa source renvoie encore à L412-18 et se termine par « période habituelle » sans complément ; le brouillon CSS joint recodifie le renvoi et propose l'interruption habituelle d'activité, mais n'est pas le droit en vigueur et cette précision doit être étayée dans son dossier. Le renvoi ajouté à L2411-18 n'est pas une cible fournie ; son texte officiel et celui de L2411-3 ont été lus dans le corpus, notes comprises. Leur réserve de la décision 2012-242 QPC du 14 mai 2012 reste applicable ; le texte intégral de cette décision n'est pas fourni ni présenté comme vérifié ici. Les six mois des anciens membres, trois mois des candidats à compter de la publication et prolongations saisonnières du CSS ne sont pas absorbés par le préavis ou le seuil indemnitaire d'un an. Coordonner CSS et règlements hors lot sans prétendre les modifier par ce seul renvoi.")

def plain(xml):
    return unescape(re.sub('<[^>]*>', '', xml))

def effect(number, kind, measure_id, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    assert len(source_quote) >= 12 and source_quote in plain(by_number[number]['source_xml']), (number, source_quote)
    assert len(proposed_quote) >= 12 and proposed_quote in plain(out[number]['proposed_xml']), (number, proposed_quote)
    return dict(kind=kind, measure_id=measure_id, description=description, before=before,
                after=after, unit=unit, affected_population=population,
                conditions_and_transition=transition, replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)

def impact(number, classification, assessment, limits, burdens, effects):
    out[number]['substantive_impact'] = dict(version=1, classification=classification,
        assessment=assessment, scope_limitations=limits, new_burdens_review=burdens, effects=effects)

impact('L2312-26', 'material_reduction',
    "Par rapport à la source officielle entière, deux exigences sont effectivement retirées : le comptage des demandes de dérogation au minimum général à temps partiel et la justification spéciale des recours envisagés l'année suivante. Cette dernière coupe est supplémentaire au brouillon. Les informations de santé, égalité, formation, handicap et logement restent. Le réemploi ne constitue pas à lui seul une réduction nouvelle démontrée car L2312-18 prévoit déjà la mise à disposition actualisée.",
    "La contribution de construction, le CPF, les contributions sociales et les minima conventionnels ne sont pas supprimés. Les perspectives générales d'emploi et les informations autonomes de la base restent dues ; les tableaux réglementaires demandent coordination. Aucun gain de coût chiffré ni solde net de tous les codes n'est établi.",
    "Aucune charge nouvelle n'est identifiée dans cet article : pas de formulaire, de registre, de prévision de substitution, d'attestation ou d'indication formelle d'emplacement. L'accès utile et les compléments nécessaires relèvent déjà de l'information du comité. Les aides n'acquièrent aucune condition nouvelle.",
    [effect('L2312-26', 'obligation_removed', 'temps-partiel-sans-plancher-general',
        "Retrait du seul décompte de demandes du II, 5°, d) ; les dispenses de fond demeurent.",
        "Nombre de demandes individuelles de dérogation au minimum hebdomadaire des articles L3123-7, L3123-19 et L3123-27 à fournir au CSE.",
        "Aucun décompte de ces demandes pour les consultations engagées après suppression du minimum légal général ; autres minima et droits inchangés.",
        'legal_duty', "Employeurs et CSE des entreprises d'au moins cinquante salariés ; salariés à temps partiel concernés.",
        "Consultations engagées à compter de la suppression du minimum général ; droits antérieurs et dispenses favorables conservés.",
        "Pas de décompte ou de déclaration de remplacement ; le bilan général du temps partiel subsiste.",
        "Le nombre de demandes individuelles formulées par les salariés à temps partiel pour déroger à la durée hebdomadaire minimale prévue au premier alinéa de l'article L. 3123-7 et aux articles L. 3123-19 et L. 3123-27",
        "Aucun décompte des demandes individuelles de dérogation au plancher général légal de durée du travail à temps partiel supprimé n'est exigé pour les consultations engagées à compter de l'entrée en vigueur de cette suppression"),
     effect('L2312-26', 'obligation_removed', 'cse-suppression-justification-recours-futurs',
        "Suppression de l'explication prospective spéciale du II, 9°, sans retirer les perspectives générales d'emploi.",
        "Éléments motivant le recours passé et envisagé pour l'année à venir aux CDD, missions et portage.",
        "Motifs des recours passés maintenus ; aucune justification spécifique par forme de recours pour l'année suivante.",
        'legal_duty', "Employeurs soumis à la consultation annuelle supplétive et leur CSE.",
        "Mises à disposition restant à effectuer après entrée en vigueur, consultations en cours incluses ; pas de reprise des consultations achevées.",
        "Pas de déclaration de remplacement ; informations générales sur l'emploi et ses perspectives déjà dues conservées.",
        "qui pourraient le conduire à faire appel pour l'année à venir, à des contrats de travail à durée déterminée, à des contrats de mission conclus avec une entreprise de travail temporaire ou à des contrats conclus avec une entreprise de portage salarial.",
        "Aucune justification spécifique des recours envisagés pour l'année suivante n'est exigée au titre du présent 9°. Cette dispense ne supprime pas l'information sur les perspectives générales d'emploi nécessaire à la consultation du comité.")])

impact('L2312-70', 'material_reduction',
    "La source impose trois éléments à l'alerte : effectifs, motifs et journées depuis la dernière communication. La proposition conserve les deux premiers et supprime le troisième calcul particulier, contrairement au brouillon. La majorité et le droit à examen ne changent pas. L'économie de production de ce calcul n'est pas chiffrée et peut être faible si les données sont déjà disponibles.",
    "Les décomptes de temps de travail et les informations d'effectifs dus ailleurs restent applicables ; aucune économie globale de paie ou baisse de cotisation n'est démontrée. La mise à disposition n'est pas une innovation intégrale au regard de L2312-15/L2312-18.",
    "Aucune charge nouvelle n'est identifiée : aucune série statistique, inscription préalable, attestation ni déclaration ne remplace le calcul supprimé. Effectifs, motifs, majorité et prochaine réunion ordinaire existaient déjà. L'intérim en CDI est déjà possible dans la source légale environnante.",
    [effect('L2312-70', 'obligation_removed', 'cse-alerte-sans-decompte-special-journees',
        "Retrait du cumul particulier des journées depuis la dernière communication dans cette alerte.",
        "À la réunion demandée par la majorité en cas d'accroissement important, obligation de donner les journées travaillées depuis la dernière communication, en plus du nombre et des motifs.",
        "Nombre de salariés et motifs seulement au titre de cette obligation spéciale ; aucun cumul particulier de journées depuis la dernière communication.",
        'legal_duty', "Employeurs et CSE concernés par l'accroissement important du recours aux salariés temporaires et anciens CDD.",
        "Réunions à compter de l'entrée en vigueur, même pour des données antérieures ; autres droits d'information et recours conservés.",
        "Pas de calcul substitutif ; obligations générales de temps de travail et d'information maintenues à leur fondement propre.",
        "le nombre des journées de travail accomplies par les intéressés depuis la dernière communication faite à ce sujet.",
        "Aucun décompte particulier des journées de travail accomplies depuis la dernière communication n'est exigé au titre du présent article.")])

impact('L2312-71', 'material_reduction',
    "Le cadre obligatoire du plan de résorption disparaît, tandis que le signalement, les constatations et les mesures correctrices dans une réponse motivée restent exigibles. La réduction est celle de cette organisation imposée, pas la suppression d'un rapport de l'inspection. La source ne prouvait pas qu'un deuxième document distinct était obligatoire : aucune économie supplémentaire n'est comptée à ce titre.",
    "Les compétences de l'inspection, l'information utile du CSE, les obligations de faire cesser les illégalités et les recours des salariés sont conservés. L'ampleur des coûts évités et le solde global de complexité ne sont pas établis ; l'application européenne nécessite coordination hors de ce lot.",
    "Aucune charge nouvelle n'est identifiée : la réponse motivée et les moyens correctifs existent déjà dans la source. Aucun rapport, registre, délai ni indication formelle de référence supplémentaire n'est ajouté. Les CDD illégaux restent contrôlables sans créer une nouvelle autorisation de recrutement.",
    [effect('L2312-71', 'obligation_removed', 'cse-alerte-sans-plan-precarite-obligatoire',
        "Suppression du cadre obligatoire du plan, sans suppression de la réponse et de ses mesures nécessaires.",
        "Préciser, en tant que de besoin, les moyens mis en œuvre dans le cadre d'un plan de résorption de la précarité.",
        "Préciser dans la réponse les mesures nécessaires contre les abus ; aucune organisation dans un plan ni document supplémentaire exigé.",
        'legal_duty', "Employeurs destinataires de constatations après saisine de l'inspection par le CSE.",
        "Réponses à compter de l'entrée en vigueur, même après constatations anciennes ; contrôles et droits des salariés préservés.",
        "La réponse motivée préexistante porte toujours les mesures nécessaires ; aucun instrument de planification de remplacement.",
        "les moyens qu'il met en œuvre dans le cadre d'un plan de résorption de la précarité destiné à limiter le recours à ces formes de contrats de travail.",
        "Ces mesures n'ont pas à être organisées dans un plan de résorption de la précarité ni à faire l'objet d'un document distinct de la réponse.")])

impact('L2314-20', 'coordination_only',
    "Les seuils et fenêtres de la source entière ne sont pas diminués. Le contrat indéterminé et ses intermissions sont expressément inclus et l'ancienneté antérieure conservée. L'assimilation des intermissions existe déjà dans L1251-58-2 : le présent texte rend les renvois cohérents avec le contrat unique et ne constitue pas une seconde extension certaine de ces droits.",
    "Les conditions d'âge, de droits civiques et les exclusions générales restent distinctes ; aucune réduction de coût, taxe ou formalité n'est démontrée ici. Les élections et recours antérieurs gardent leur régime. Le lot ne chiffre pas le coût du contrat unique.",
    "Aucune charge nouvelle n'est identifiée : pas de registre, pièce, autorisation ou délai ajouté. La prise en compte de l'emploi et de ses intermissions utilise l'ancienneté déjà suivie ; les seuils restent de trois et six mois avec leurs fenêtres initiales.",
    [effect('L2314-20', 'coordination', 'interim-droits-electoraux-emploi',
        "Rattachement explicite de l'ancienneté électorale à l'emploi indéterminé et à ses intermissions.",
        "Trois mois d'ancienneté pour voter, six pour être éligible, missions sur douze ou dix-huit mois ; fenêtre de six mois à la création ou ouverture.",
        "Mêmes seuils et fenêtres ; périodes d'emploi indéterminé et intermissions incluses, anciennes missions et ancienneté de conversion conservées.",
        'regime', "Salariés temporaires des entreprises de travail temporaire, anciens contrats et contrats uniques.",
        "Listes confectionnées à compter de l'entrée en vigueur ; opérations antérieures et recours préservés.",
        "Pas de justificatif nouveau ; aucune nouvelle possibilité d'embauche ou de renouvellement à terme.",
        "Ces conditions sont appréciées en totalisant les périodes pendant lesquelles ces salariés ont été liés à ces entreprises par des contrats de mission",
        "Les périodes sans mission du contrat à durée indéterminée sont prises en compte comme périodes d'emploi ; une conversion ne remet pas à zéro l'ancienneté déjà acquise.")])

impact('L2314-22', 'material_reduction',
    "La source entière retire le droit électoral à ceux qui ne veulent plus de prochaine mission ou à qui l'agence annonce un non-rappel. Ces deux exclusions sont effectivement levées tant que l'emploi subsiste, y compris entre missions. Cette réduction d'une restriction était déjà dans le brouillon ; elle n'est pas une coupe supplémentaire de cette passe. L'ancienneté et le lien d'emploi restent nécessaires.",
    "Aucun droit après la fin effective de l'emploi ni double vote n'est créé. Les listes et litiges anciens restent régis par leur droit. Aucun coût employeur évité ni solde net financier n'est démontré par l'extension des droits électoraux.",
    "Aucune charge nouvelle de formulaire, registre, donnée ou délai n'est identifiée. L'organisation des élections existe déjà ; la mesure impose seulement de ne pas radier un salarié toujours lié à l'entreprise pour l'un des deux motifs supprimés, ce qui est l'effet direct de l'extension du droit et non un circuit administratif ajouté.",
    [effect('L2314-22', 'relief_extended', 'interim-droits-electoraux-emploi',
        "Levée des deux exclusions de droits liées à l'absence de prochaine mission pour un salarié toujours employé.",
        "Perte d'électorat et d'éligibilité en cas de souhait de ne plus bénéficier d'un nouveau contrat de mission ou de décision patronale de ne plus rappeler le salarié.",
        "Ces motifs seuls ne privent plus le salarié de ses droits tant que le contrat subsiste et que L2314-20 est respecté.",
        'regime', "Salariés temporaires satisfaisant aux autres conditions électorales, liés à l'agence lors de la confection des listes.",
        "Listes futures, anciens contrats encore en cours inclus ; pas de remise en cause des opérations anciennes ni de rétablissement d'un emploi rompu.",
        "Aucun scrutin ou dossier supplémentaire ; les règles générales de liste et de recours subsistent.",
        "Les salariés à qui l'entrepreneur de travail temporaire a notifié sa décision de ne plus faire appel à eux pour de nouveaux contrats de mission.",
        "La décision de l'entreprise de ne pas proposer une nouvelle mission ne prive pas, à elle seule, le salarié de ces droits tant que son contrat de travail subsiste.")])

impact('L2315-13', 'coordination_only',
    "La source entière rémunère et assujettit déjà les heures conventionnelles de délégation entre missions. Le texte corrige leur rattachement au contrat indéterminé et maintient la fiction du dernier ancien contrat pour les droits du stock. Aucun salaire, cotisation ou condition conventionnelle n'est supprimé ; le brouillon substantiellement identique est conservé pour cette coordination nécessaire.",
    "Le montant de la rémunération mensuelle garantie et les règles autonomes de cotisations ne sont pas modifiés. Aucun gain net de prélèvement ou de coût administratif n'est démontré ; le financement des droits sociaux reste à son champ propre.",
    "Aucune charge nouvelle n'est identifiée : la qualification de travail, la paie et les charges sociales existent dans la source. Aucun paiement en double, attestation, registre ou nouveau délai n'est créé ; le changement désigne le contrat auquel rattacher les heures.",
    [effect('L2315-13', 'coordination', 'contrat-unique-sans-nouveaux-cdd',
        "Rattachement de la paie des heures de délégation au contrat indéterminé en cours, sans perte des droits anciens.",
        "Heures conventionnelles de délégation entre missions réputées rattachées au dernier contrat de mission pour rémunération et charges sociales.",
        "Rattachement au CDI en cours ; fiction du dernier contrat maintenue pour les anciens contrats de mission concernés.",
        'regime', "Membres titulaires du CSE employés par une entreprise de travail temporaire.",
        "Anciennes heures et créances conservées ; conversion sans perte d'ancienneté ; pas de nouveau CDD ou renouvellement.",
        "Aucun nouveau paiement ou prélèvement ; maintien de ceux déjà attachés aux heures de travail.",
        "Ces heures de délégation sont réputées rattachées, en matière de rémunération et de charges sociales, au dernier contrat de mission",
        "Pour la rémunération et les charges sociales, ces heures sont rattachées au contrat à durée indéterminée qui lie le salarié à l'entreprise au titre de laquelle il a été élu.")])

protected = {
    'L23-114-2': (
        "Membres et anciens membres de la commission paritaire régionale interprofessionnelle, salariés figurant sur la propagande électorale.",
        "Le licenciement et la rupture du contrat à durée déterminée d'un membre de la commission sont soumis à la procédure d'autorisation administrative prévue au livre IV de la présente deuxième partie.",
        "La protection demeure ouverte aux mandats et candidatures futurs dans le contrat unique.",
        "L'interdiction du motif lié au mandat et l'autorisation de rupture demeurent ; la coordination distingue le stock des CDD et l'emploi indéterminé et empêche l'invocation d'un terme interdit contre la protection. Aucun délai de protection ou circuit d'autorisation de la source n'est supprimé."),
    'L2412-1': (
        "Salariés investis des dix-huit mandats énumérés, candidats et anciens titulaires dans les champs des articles protecteurs.",
        "Bénéficie de la protection en cas de rupture d'un contrat à durée déterminée prévue par le présent chapitre le salarié investi de l'un des mandats suivants :",
        "Le salarié recruté dans le contrat unique bénéficie, pour les mandats, candidatures et périodes de protection qui relèvent de son champ, de la protection prévue au chapitre Ier du présent titre.",
        "Les dix-huit entrées et leurs protections sont conservées. Le passage du stock des CDD au chapitre Ier pour les nouveaux emplois est une coordination de la suppression décidée ailleurs, sans nouveau retrait d'autorisation. Une clause de terme illicite ne permet plus de soutenir que la transition exclut le salarié de toute protection."),
    'L2412-6': (
        "Membres du groupe spécial de négociation et du comité d'entreprise européen.",
        "ne peut intervenir qu'après autorisation de l'inspecteur du travail.",
        "Pour le contrat unique et les conversions convenues, la protection contre le licenciement relève de l'article L. 2411-11.",
        "L'autorisation préalable pour les deux catégories et tous les cas de la source reste. Le renvoi protecteur du contrat indéterminé et la transition des termes anciens ne constituent aucune baisse supplémentaire de charge ; le brouillon est conservé après examen de la fonction anti-représailles."),
    'L2412-7': (
        "Membres du groupe spécial et représentants aux comités de société européenne, coopérative européenne et société issue de fusion transfrontalière.",
        "ne peut intervenir qu'après autorisation de l'inspecteur du travail.",
        "Pour le contrat unique et les conversions convenues, la protection contre le licenciement relève de l'article L. 2411-12",
        "Tous les groupes, les trois comités et les cas de la source sont maintenus avec autorisation. La coordination vers le chapitre Ier remplace seulement la lecture d'une embauche à terme future ; elle ne fusionne ni n'abolit les garanties européennes distinctes."),
    'L2412-10': (
        "Salariés mandatés au titre de L2232-23-1 ou L2232-26 et protégés dans leur champ.",
        "ne peut intervenir qu'après autorisation de l'inspecteur du travail.",
        "La protection du salarié mandaté employé dans le contrat unique ou dont le contrat est converti d'un commun accord relève de l'article L. 2411-4.",
        "Les deux voies de mandatement, les motifs anticipés et le contrôle du non-renouvellement du stock restent. Le relais L2411-4 est une coordination de la même mesure de contrat unique ; aucune autorisation supprimée et aucun allègement distinct de négociation n'est attribué ici."),
    'L2412-11': (
        "Salariés membres du conseil ou administrateurs d'une caisse de sécurité sociale, avec les catégories protégées par le CSS.",
        "il bénéficie des garanties et protections prévues à l'article L. 231-11 du code de la sécurité sociale.",
        "Pour le contrat unique et les conversions convenues, les garanties de l'article L. 231-11 du code de la sécurité sociale et la protection contre le licenciement prévue à l'article L. 2411-18 demeurent applicables, sans interruption des périodes protégées.",
        "Le renvoi protecteur de la source demeure pour le stock et est explicitement préservé pour l'emploi indéterminé. Candidatures, anciennes fonctions et prolongations saisonnières ne disparaissent pas. Cette coordination ne supprime aucune autorisation ni cotisation et ne résout pas à elle seule les anomalies du texte CSS.")
}
for number, (population, sq, pq, assessment) in protected.items():
    impact(number, 'coordination_only', assessment,
        "Les contrats antérieurs, les périodes de protection propres à chaque mandat et les recours restent à leur régime. Les textes de procédure, les coordinations extérieures et les exigences européennes ou constitutionnelles signalées ne sont pas tous traités ici. Aucun coût net ni solde d'ensemble des codes n'est établi.",
        "Aucune charge nouvelle n'est identifiée dans cet article : l'autorisation protectrice existe déjà et n'est ni doublée d'une déclaration ni remplacée par un registre. La continuité vers le contrat unique et la conservation des droits ne créent pas une seconde procédure ; le préavis individuel ne vaut pas autorisation.",
        [effect(number, 'coordination', 'contrat-unique-sans-nouveaux-cdd',
            "Continuité des protections lors de l'extinction prospective des nouvelles embauches à durée déterminée.",
            "Protection liée au mandat dans le régime de rupture des CDD ; nouveaux CDD encore permis par le droit source dans leurs cas légaux. Aucun taux ni assiette fiscale en cause.",
            "Garanties des anciens contrats maintenues ; futurs emplois et conversions couverts par les protections de l'emploi indéterminé, sans nouveau CDD ni renouvellement à terme.",
            'regime', population,
            "Contrats conclus avant l'entrée en vigueur conservés dans le stock ; mandats futurs et conversions protégés sans interruption. Créances et recours antérieurs maintenus.",
            "Aucune déclaration ou autorisation supplémentaire ; autorisation protectrice existante conservée. Les charges générales du contrat unique ne sont pas chiffrées par cette coordination.",
            sq, pq)])

for number, removed in {
    'L2312-26': [
        "Suppression du décompte des demandes de dérogation au minimum légal général à temps partiel au II, 5°, d), après la suppression de ce minimum.",
        "Suppression de la justification spécifique des recours aux formes d'emploi envisagés pour l'année suivante au II, 9°, avec maintien des perspectives générales d'emploi."],
    'L2312-70': [
        "Suppression du décompte spécial des journées travaillées depuis la dernière communication pour l'examen de l'accroissement du recours aux salariés concernés."],
    'L2312-71': [
        "Suppression de l'obligation d'organiser les moyens correctifs dans un plan de résorption de la précarité ; la réponse motivée et les mesures nécessaires restent dues."],
    'L2314-22': [
        "Suppression des deux exclusions de droits électoraux tenant à l'absence de prochaine mission tant que la relation d'emploi avec l'entreprise subsiste."]
}.items():
    out[number].update(change_type='normative_reduction',
        reform_policy_id='editorial_direction_2026_10_19', removed_provisions=removed)

# Chaque appréciation porte sur la cible requise, y compris sans renvoi direct.
checks = {
    'L2312-26': {
        'L1234-1': "Aucun renvoi direct : la consultation annuelle porte sur l'emploi, pas sur le droit au préavis. La cible proposée de quinze jours pour les nouveaux contrats ne réduit ni les délais d'examen du CSE ni les procédures collectives ; les anciens préavis restent à leur régime.",
        'L1221-2': "Le II, 1° et 9° doit cesser de prévoir de futurs CDD mais suivre le stock et les missions. La cible proposée interdit aussi les nouveaux termes liés à une formation ou aide ; les rubriques de professionnalisation, apprentissage et insertion restent donc ouvertes dans l'emploi indéterminé, sans perte des avantages futurs.",
        'L3121-34': "Cette cible est comprise dans la plage L3121-28 à L3121-39 du II, 5°, b). Elle vise les périodes saisonnières de décompte des heures supplémentaires et repos, non une autorisation de CDD. Sa proposition retire le préalable L1244-2 et garde le décompte contradictoire ; le présent renvoi préserve cette dérogation sans relever automatiquement les références annuelles.",
        'L1234-9': "Aucun renvoi direct : les informations de salaires et d'emploi ne changent pas l'indemnité. La cible proposée retient un an au terme effectif, préavis inclus, puis 0,20 mois par année totale, mois complets au prorata, plafond légal de six mois et initiative patronale, avec ses exceptions. Aucun montant de rupture n'est déduit d'une rubrique statistique.",
        'L3123-7': "Le II, 5°, d) vise le premier alinéa source du minimum légal général. La proposition cible le supprime mais maintient le volume garanti, les minima conventionnels et leurs dispenses futures, avec demandes non motivées pour les cas prévus. Le décompte supprimé ne doit donc pas être recréé à propos de ces dispenses, ni supprimer ces avantages ou le minimum parental spécial."},
    'L2312-70': {
        'L1234-1': "Pas de renvoi direct : l'inscription à la prochaine réunion ordinaire reste un droit du CSE, sans être soumise au préavis individuel de quinze jours proposé pour les contrats nouveaux. Les anciens préavis et les procédures collectives conservent leur champ ; l'alerte ne vaut pas notification d'une rupture.",
        'L1221-2': "La référence source aux CDD est limitée au stock antérieur ; les salariés mis à disposition sous CDI restent comptés. La cible proposée interdit tout nouveau terme ou renouvellement et distingue mission et emploi : le suivi d'une augmentation des missions ne peut rétablir une embauche à terme.",
        'L1234-9': "La réunion d'alerte et son décompte d'effectifs ne fixent aucune indemnité. La cible proposée apprécie l'année d'ancienneté à la fin effective avec préavis inclus et calcule 0,20 mois sur l'ancienneté totale, fractions par mois complets, plafond de six mois. Ce seuil ne conditionne ni l'alerte ni le droit de faire contrôler un abus."},
    'L2312-71': {
        'L1234-1': "Le signalement à l'inspection et la réponse aux constatations ne sont pas des notifications de rupture. Le préavis de quinze jours de la cible proposée pour les nouveaux contrats ne remplace ni le contrôle ni les délais et procédures collectives ; aucune date butoir de quinze jours n'est introduite ici.",
        'L1221-2': "La saisine doit couvrir aussi les CDD nouvellement conclus ou renouvelés illégalement, et pas uniquement le stock licite antérieur. La cible proposée rend l'emploi nouveau indéterminé même pour les missions ; le texte conserve donc l'alerte sur les missions et le portage sans attribuer à leur fin un effet de rupture.",
        'L1234-9': "Aucun renvoi indemnitaire n'existe ici. L'absence d'indemnité ordinaire avant un an au terme effectif, préavis compris, ne supprime pas les dommages d'une illégalité ni le signalement dès le début de l'emploi. Le barème proposé de 0,20 mois sur toutes les années après le seuil et son plafond de six mois ne sont pas appliqués aux réparations d'abus."},
    'L2314-20': {
        'L1234-1': "Les trois et six mois de cet article sont des anciennetés électorales, pas des préavis. La cible proposée fixe quinze jours pour une rupture patronale du contrat nouveau, sans remplacer les fenêtres de douze/dix-huit/six mois ; une période de préavis pendant laquelle l'emploi subsiste ne constitue pas une intermission exclue.",
        'L1221-2': "La cible proposée rend le nouvel emploi intérimaire indéterminé et interdit qu'une fin de mission termine le contrat. Le calcul électoral inclut donc ces périodes d'emploi et les intermissions, conserve les anciennes missions et l'ancienneté d'une conversion ; aucune mission nouvelle à durée déterminée n'est autorisée par la période de référence.",
        'L1234-9': "Le seuil indemnitaire proposé d'un an au terme effectif avec préavis inclus est étranger aux seuils électoraux de trois et six mois. Ni la totalité des années au taux de 0,20 mois, ni le prorata en mois complets, ni le plafond de six mois de salaire ne doivent être importés dans les fenêtres d'électorat et d'éligibilité."},
    'L2314-22': {
        'L1234-1': "La notification patronale de non-rappel mentionnée au 2° source n'est pas, à elle seule, la notification mettant fin à un contrat unique. Le préavis de quinze jours proposé doit relever de sa procédure propre ; tant que le lien d'emploi subsiste lors de la confection des listes, l'absence de prochaine mission ne suffit pas à retirer le droit.",
        'L1221-2': "La distinction de la cible proposée entre mission limitée et emploi indéterminé impose de retirer les deux exclusions par non-rappel pendant l'emploi. Les anciens CDD encore en cours restent suivis ; aucune fin ou absence de nouvelle mission ne crée un terme du contrat unique ni ne rétablit un contrat déjà rompu.",
        'L1234-9': "Aucun renvoi direct à l'indemnité : le seuil d'un an au terme effectif avec préavis inclus ne conditionne pas l'inscription électorale. Le taux proposé de 0,20 mois par année totale, prorata en mois complets et plafond de six mois, concerne une rupture patronale ordinaire, non une radiation pour absence de mission.",
        'L2314-20': "Renvoi direct au calcul spécial : trois mois pour voter et six pour être éligible sur douze/dix-huit mois, fenêtres ramenées à six mois à la création ou ouverture. La proposition cible inclut l'emploi indéterminé et ses intermissions ; le présent article exige toujours ce lien d'emploi à la confection des listes et ne rétablit pas un seuil général d'un an."},
    'L2315-13': {
        'L1234-1': "La paie des heures de délégation entre missions n'est pas une indemnité de préavis. La cible proposée de quinze jours pour le contrat nouveau ne raccourcit ni la période de mandat ni les créances de ces heures ; les anciens contrats conservent leurs droits et la procédure d'une rupture reste distincte de leur rattachement social.",
        'L1221-2': "La cible proposée empêche la fin automatique de l'emploi à la fin d'une mission. Les heures conventionnelles de délégation sont donc rattachées au CDI en cours, avec maintien de la fiction du dernier contrat pour les anciens droits. Aucun nouveau CDD ni essai ne découle de cette imputation de paie.",
        'L1234-9': "Le seuil d'un an proposé pour l'indemnité ordinaire ne peut priver un représentant de la rémunération des heures de délégation dès le début de l'emploi. Le barème de 0,20 mois sur l'ancienneté totale, prorata par mois complets et plafond de six mois, ne remplace ni ces salaires ni les cotisations attachées à des heures de travail."},
    'L23-114-2': {
        'L1234-1': "Le préavis patronal de quinze jours de la cible proposée ne vaut pas autorisation du livre IV. Les six mois protecteurs de la propagande et de l'ancien mandat conservent leur champ ; la notification de candidature n'est pas confondue avec la notification de rupture, et les anciens préavis ne sont pas effacés.",
        'L1221-2': "Le contrat unique indéterminé proposé couvre les futurs membres et candidats sans exiger une durée déterminée du mandat égale à celle de l'emploi. Les anciens CDD restent protégés, aucun renouvellement n'est rouvert, et une stipulation de terme interdite ne peut supprimer l'autorisation protectrice.",
        'L1234-9': "L'autorisation contre les représailles existe dès la période protégée et n'est pas conditionnée à l'année d'ancienneté de l'indemnité ordinaire. Le seuil proposé au terme effectif avec préavis inclus et le barème de 0,20 mois sur toutes les années après seuil, prorata en mois complets et plafond légal de six mois, ne limitent ni protection ni dommages d'une illégalité."},
    'L2412-1': {
        'L1234-1': "La transition maintient expressément les autorisations des représentants en plus du préavis de quinze jours proposé pour les nouveaux contrats. L'autorisation n'est ni acquise au bout de quinze jours ni remplacée par une notification ; les préavis des anciens contrats et les procédures collectives restent à leur régime propre.",
        'L1221-2': "La cible proposée interdit de nouveaux CDD, y compris sous couvert de durée de mandat ou de mission. Le chapitre II devient celui du stock, tandis que le chapitre Ier protège l'emploi indéterminé et les conversions sans interruption. Un terme illégal ne peut être opposé pour écarter ces protections ; les aides futures restent à leurs dispositifs propres.",
        'L1234-9': "La liste des mandats et leurs périodes protégées ne dépendent pas du seuil d'un an de l'indemnité ordinaire proposée. Ce seuil se mesure au terme effectif, préavis compris ; le calcul de 0,20 mois sur toute l'ancienneté, prorata en mois complets et plafond de six mois, ne réduit ni salaires, primes anciennes, dommages ni indemnités spéciales.",
        'L231-11': "Le 11° vise exactement les membres de conseil et administrateurs de caisse, pas tout agent public. La source CSS maintient anciens membres six mois, candidats trois mois et prolongation saisonnière, mais renvoie encore à L412-18 et dit seulement période habituelle. La proposition CSS jointe recodifie sans être le droit en vigueur ; ces garanties et la réserve constitutionnelle ne sont pas effacées par la transition."},
    'L2412-6': {
        'L1234-1': "L'autorisation de l'inspecteur pour le groupe spécial et le comité européen demeure préalable. Les quinze jours proposés de préavis individuel ne remplacent ni cette décision ni la procédure distincte ; les anciens CDD ne deviennent pas résiliables pour un motif nouveau par ce renvoi de coordination.",
        'L1221-2': "Le champ de la rupture à terme est limité aux contrats conclus avant la réforme ; aucun groupe spécial ni mandat européen ne justifie un nouveau CDD. La cible proposée empêche la fin automatique à l'échéance d'une mission ; le contrat unique ou une conversion relève de la protection de licenciement de L2411-11.",
        'L1234-9': "Ni l'autorisation des deux catégories ni le constat d'inaptitude ne sont conditionnés à un an de service. La cible proposée ne traite que l'indemnité ordinaire : seuil au terme effectif préavis inclus, 0,20 mois par année totale, mois complets au prorata, plafond de six mois. Les garanties spéciales et dommages ne sont pas absorbés.",
        'L2412-1': "Le 6° de la liste cible vise le groupe spécial et le comité d'entreprise européen. La proposition cible maintient le contrôle de l'ancien terme même sans renouvellement désormais licite et relaie les futurs emplois vers le chapitre Ier. Le présent article conserve faute grave, inaptitude médicalement constatée et clause de renouvellement sans créer un nouveau contrat à terme."},
    'L2412-7': {
        'L1234-1': "La cible proposée prévoit un préavis individuel patronal de quinze jours pour les nouveaux emplois ; elle conserve les autorisations distinctes. Aucun groupe ou comité transnational du présent article ne peut donc être privé du contrôle préalable par une simple notification ou par l'écoulement de quinze jours.",
        'L1221-2': "La durée d'un groupe spécial ou d'une représentation dans une société européenne n'est pas un terme d'emploi. La cible proposée interdit les nouvelles embauches à terme ; le texte réserve le régime de terme aux anciens CDD, maintient leur protection et renvoie le CDI nouveau ou converti à L2411-12.",
        'L1234-9': "L'ancienneté indemnitaire d'un an se mesure, dans la cible proposée, au terme effectif avec préavis inclus ; elle ne conditionne aucune autorisation du présent article. Le calcul de 0,20 mois sur l'ancienneté totale, par mois complets au prorata et plafond légal de six mois, ne remplace pas les garanties européennes ni les réparations d'une illégalité.",
        'L2412-1': "Les 7°, 7° bis et 7° ter de la liste cible correspondent aux sociétés européenne, coopérative européenne et issue d'une fusion transfrontalière. Le groupe spécial et chacun des comités restent couverts. Le stock et le refus de renouvellement restent contrôlés sans renouvellement nouveau ; les futurs emplois relèvent du chapitre Ier et les périodes protégées ne sont pas interrompues."},
    'L2412-10': {
        'L1234-1': "Le salarié mandaté n'est pas privé de l'autorisation préalable par le préavis de quinze jours de la cible proposée. La notification de rupture ne vaut pas connaissance de l'imminence du mandat ni décision de l'inspecteur ; les procédures et anciennes situations protégées restent distinctes de cette durée individuelle.",
        'L1221-2': "Le mandat de négociation et la durée d'une négociation n'autorisent aucun nouveau CDD selon la cible proposée. Le présent texte conserve le contrôle des anciens termes et renvoie le nouvel emploi indéterminé ou converti à L2411-4, sans interrompre les protections de l'imminence ou d'après-mandat.",
        'L1234-9': "Le mandat protège indépendamment du seuil d'un an d'ancienneté de l'indemnité ordinaire proposée. Le préavis est inclus au terme effectif pour ce seuil, puis toutes les années entrent dans les 0,20 mois, prorata en mois complets, plafond de six mois. Cette règle ne réduit ni les douze mois de protection après mandat ni les dommages pour représailles.",
        'L2412-1': "Le 10° de la liste cible conserve les deux voies L2232-23-1 et L2232-26 en entreprise sans délégué syndical. Son régime de stock maintient l'autorisation sur les anciens termes, pas un droit de renouveler. Les simplifications de transmission et de négociation ne retirent pas le mandat, et le chapitre Ier assure la continuité du contrat unique."},
    'L2412-11': {
        'L1234-1': "Le préavis individuel de quinze jours de la cible proposée ne remplace pas l'autorisation exigée par le régime du membre de conseil ou administrateur. Les notifications de candidature et de rupture restent de nature différente ; les durées protectrices CSS ne sont pas ramenées à quinze jours, et les anciens préavis sont préservés.",
        'L1221-2': "La cible proposée transforme l'embauche nouvelle en emploi indéterminé sans supprimer le statut protecteur des membres de caisse. Le présent texte conserve le stock des anciens CDD et les garanties CSS pour les futurs contrats uniques et conversions ; ni fin de mandat ni période saisonnière ne termine automatiquement cet emploi.",
        'L1234-9': "Le seuil proposé d'un an au terme effectif préavis inclus ne conditionne ni la protection du mandat, ni les candidatures, ni les recours pour rupture illicite. Les 0,20 mois par année totale avec prorata des mois complets et plafond légal de six mois concernent l'indemnité ordinaire patronale ; ils ne plafonnent pas les dommages prévus par le CSS.",
        'L2412-1': "Le 11° de la liste cible reprend exactement le mandat de caisse et le renvoi CSS. La transition maintient les anciens contrats et le relais vers le chapitre Ier, sans effacer les catégories ou périodes plus précises de L231-11. La précision apportée ici conserve ces garanties aussi pour les futurs emplois indéterminés et les conversions.",
        'L231-11': "Le renvoi direct vise l'interdiction de rupture liée au mandat, la réparation, les six mois d'après-mandat, les trois mois de candidature dès publication et la prolongation saisonnière. La source CSS cite encore L412-18 et une période habituelle imprécise ; sa proposition recodifie et précise mais n'est pas le droit en vigueur. Les anomalies sont signalées sans déduire de L3121-34 un régime public ou un terme d'emploi."}
}

for obj in answer:
    key = obj['code_id'] + '|' + obj['source_id']
    required = references['requirements'][key]
    obj['reference_checks'] = []
    for target_key in required:
        target = references['targets'][target_key]
        assessment = checks[obj['number']][target['number']]
        obj['reference_checks'].append(dict(target_key=target_key,
            view_sha256=target['view_sha256'], assessment=assessment))

Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
