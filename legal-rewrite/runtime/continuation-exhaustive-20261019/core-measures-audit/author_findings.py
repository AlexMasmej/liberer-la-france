from pathlib import Path
from copy import deepcopy
from datetime import datetime,timezone
import hashlib,json,re,sys,sqlite3
P=Path(__file__).resolve().parent;LEGAL=P.parents[2];sys.path.insert(0,str(LEGAL))
import substantive_impact as rules
from ingest import source_notes
sources=json.loads((P/'sources.json').read_text());by_number={x['number']:x for x in sources}
dependencies=json.loads((P/'dependencies.json').read_text())+json.loads((P/'extra-dependencies.json').read_text())
sha=lambda value:hashlib.sha256(value if isinstance(value,bytes)else(value or '').encode()).hexdigest()
policy_sha=sha((LEGAL/'policy-coordinations.json').read_bytes())
now=datetime.now(timezone.utc).isoformat()

def paragraph(number,index,proposed=False):
    body=by_number[number]['proposed_xml' if proposed else 'source_xml']
    return rules.plain(re.findall(r'<p\b[^>]*>.*?</p>',body,re.S)[index])

def effect(kind,measure,description,before,after,unit,population,conditions,replacements,source_quote,proposed_quote):
    return dict(kind=kind,measure_id=measure,description=description,before=before,after=after,unit=unit,
        affected_population=population,conditions_and_transition=conditions,replacement_or_new_burdens=replacements,
        source_quote=source_quote,proposed_quote=proposed_quote)

findings=[]
def add(number,classification,assessment,limits,burdens,effects,dependency_numbers):
    source=by_number[number]
    impact=dict(version=1,classification=classification,assessment=assessment,scope_limitations=limits,new_burdens_review=burdens,effects=effects)
    row={k:source[k]for k in ('code_id','source_id','number','source_sha256','source_body_sha256','source_notes_sha256','proposed_sha256')}
    proposed=dict(status=source['previous_draft']['status'],proposed_xml=source['proposed_xml'],substantive_impact=impact)
    rules.validate(proposed,source,required=True,enforce_workflow=False)
    row.update(substantive_impact=impact,substantive_impact_certificate=rules.certificate(proposed,source,policy_sha),
        policy_sha256=policy_sha,reviewed_at=now,reviewed_by='Agent rewrite_travail — relecture de fond bornée',
        review_scope='Full source, official notes and current proposal read; listed dependencies read in full.',
        dependency_guards=[{k:x[k]for k in ('code_id','source_id','number','source_sha256','source_body_sha256','source_notes_sha256','proposed_sha256')}
            for x in dependencies if x['number']in dependency_numbers],
        review_provenance={'distinct_from_worker_self_assessment':True,
            'independence_from_initial_author':False if number in {'L1221-2','L1234-1','L1234-9'}else'not_asserted',
            'prior_contribution_disclosure':'Le présent créneau a contribué au paquet45 initial de ces trois articles centraux ; une contrelecture distincte est requise avant qualification publique d’indépendance envers leur auteur.'if number in {'L1221-2','L1234-1','L1234-9'}else'Cette relecture ne revendique aucune qualification de juriste ni validation générale du projet.'},
        semantic_review_by_jurist=False,national_savings={'status':'unknown','value':None},net_global_effect='not_established')
    findings.append(row)

add('L1221-2','mixed',
    'Le projet remplace pour l’avenir les nouveaux CDI/CDD par un contrat unique sans terme. Il fusionne les formes d’embauche et leurs coordinations, mais impose aussi une durée indéterminée pour des besoins auparavant susceptibles de CDD : la fin du besoin, de la mission ou de la formation ne met plus automatiquement fin à l’emploi. Cet effet de contrainte doit être présenté avec la fusion ; ce n’est ni zéro droit ni une suppression démontrée de tous les coûts d’embauche.',
    'Cette passe ne valide pas tous les régimes spéciaux ni toutes les coordinations des cinq codes. La date commune de la loi future reste à fixer. Les contrats antérieurs gardent leur terme et leurs droits selon L1241-1 proposé, avec conversion seulement convenue et sans nouvel essai ; aucun renouvellement ordinaire nouveau ne peut créer un CDD. L’effet net sur l’emploi, la précarité ou le coût national n’est pas établi.',
    'La contrainte nouvelle est l’interdiction des nouveaux termes CDD, y compris pour un besoin temporaire : la fin de l’emploi passe par les règles de rupture applicables au contrat unique. Les quinze jours de préavis, l’indemnité ordinaire et les protections ne sont pas supprimés par L1221-2 et sont analysés sous leurs clés propres. Aucune déclaration nouvelle n’est identifiée dans cet article ; aucune fusion n’est comptée une seconde fois sous les articles d’exécution.',
    [effect('regime_merged','contract-unique','Un contrat sans terme pour les nouvelles embauches relevant du Code du travail.',
        'CDI forme normale et générale ; CDD possibles dans les cas et conditions du titreIV.',
        'Contrat unique à durée indéterminée pour les nouveaux contrats ; une durée de mission, formation ou tâche ne fixe pas le terme de l’emploi.',
        'regime','Employeurs et salariés dont le contrat relève du Code du travail ; nouveaux contrats après la date d’entrée en vigueur à fixer.',
        'Contrats antérieurs et droits associés préservés selon la transition ; pas de nouveau CDD par renouvellement ou reconduction décidés après la réforme.',
        'Fusion des formes accompagnée d’une obligation de CDI pour les besoins auparavant admis en CDD ; aucune économie nette déduite de cette seule fusion.',
        paragraph('L1221-2',1),paragraph('L1221-2',0,True)),
     effect('obligation_added','contract-unique','Interdiction d’une fin automatique du nouvel emploi temporairement nécessaire.',
        'Le contrat pouvait avoir un terme fixé précisément ou résultant de la réalisation de son objet dans les cas légaux de CDD.',
        'Le nouvel emploi n’a pas de terme automatique, même si le besoin, la saison, la mission ou la formation prend fin ; une rupture régie par les règles applicables est nécessaire.',
        'legal_duty','Nouveaux employeurs et salariés du contrat unique, notamment pour les besoins auparavant couverts par un CDD.',
        'Anciens CDD conservant leur terme ; droits de reconduction ou réemploi réalisés après la réforme sous emploi sans terme selon L1241-1.',
        'Nouvelle contrainte de durée indéterminée ; coûts et protections de rupture distincts, sans chiffrage global.',
        paragraph('L1221-2',1),paragraph('L1221-2',0,True))],
    {'L1241-1','L1242-1','L1242-2','L1243-13','L1234-3','L1234-5','L1237-1'})

add('L1234-1','mixed',
    'Pour les nouveaux contrats, le préavis patronal devient quinze jours calendaires indépendamment de l’ancienneté, en substitution des durées conventionnelles, contractuelles et d’usage. Il est plus court que les préavis légaux ordinaires d’un ou deux mois à partir de six mois d’ancienneté ; il peut en revanche créer ou augmenter un coût là où aucun tel préavis n’était dû, notamment en faute grave, désormais payée même sans exécution. La mesure a donc des effets mixtes.',
    'Ne pas promettre une baisse uniforme ni une procédure de rupture achevée en quinze jours : autorisations, salariés protégés, procédures collectives et recours restent distincts. Le délai part du lendemain de la notification selon L1234-3 ; la démission relève de L1237-1 et l’essai de L1221-25. Avant six mois et pour la démission, la comparaison dépendait des règles ou usages applicables. La conventionalité pour de longues anciennetés n’est pas tranchée par cette passe.',
    'Une charge explicite nouvelle est le préavis payé de quinze jours même en faute grave, auparavant exclu du droit au préavis et de sa compensation dans le régime ordinaire. L1234-5 conserve les salaires, avantages et congés du préavis et le distingue de l’indemnité de rupture ; la franchise d’un an et le plafond de six mois ne l’absorbent pas. Aucune nouvelle déclaration n’est identifiée dans L1234-1.',
    [effect('deadline_reduced','preavis-quinze-jours','Préavis patronal ordinaire ramené à quinze jours pour les nouveaux contrats.',
        'Hors faute grave : un mois de six mois à moins de deux ans d’ancienneté, puis deux mois dès deux ans, sous réserve des règles plus favorables.',
        'Quinze jours calendaires pour les contrats nouveaux, en substitution des durées et conditions de préavis légales de cet article, conventionnelles, contractuelles ou d’usage.',
        'calendar_days','Contrats nouveaux, notamment salariés qui auraient atteint les tranches de six mois ou deux ans ; employeurs et salariés concernés par leur rupture.',
        'Anciens contrats : ancien régime conservé. Notification au lendemain selonL1234-3 ; procédures collectives et autorisations distinctes. Coordinations handicap/journalistes/VRP examinées sans compter trois autres réductions.',
        'Le même délai constitue une nouvelle charge en faute grave ; il ne supprime aucune indemnité compensatrice de préavis lorsqu’elle est due.',
        paragraph('L1234-1',2)+' '+paragraph('L1234-1',3),paragraph('L1234-1',0,True)),
     effect('obligation_added','preavis-quinze-jours','Préavis payé désormais dû même en faute grave pour les contrats nouveaux.',
        'L1234-1 ouvre le préavis lorsque le licenciement n’est pas motivé par une faute grave ; L1234-5 exclut également sa compensation dans ce cas.',
        'La faute grave n’exonère plus des quinze jours : s’il est impossible de maintenir le salarié au travail, le préavis est payé sans être exécuté.',
        'legal_duty','Employeurs rompant pour faute grave un contrat conclu après la date d’entrée en vigueur de la réforme.',
        'Exception d’absence d’indemnité ordinaire de rupture en faute grave maintenue dansL1234-9 ; les deux créances ne doivent pas être confondues. Anciens contrats inchangés.',
        'Charge salariale nouvelle de préavis dans ce cas précis, sans taxe nouvelle ni économie nette calculée.',
        paragraph('L1234-1',0),paragraph('L1234-1',0,True))],
    {'L1234-3','L1234-5','L1237-1','L1221-25','L5213-9','L7112-2','L7313-9'})

add('L1234-9','material_reduction',
    'La condition ordinaire d’ouverture passe de huit mois à un an pour les nouveaux contrats : l’obligation de cette indemnité disparaît entre huit mois et le premier anniversaire. Une fois le seuil atteint au terme effectif, le préavis inclus sauf régime d’essai, toute l’ancienneté reconnue est calculée à0,20mois du salaire brut de référence par année, mois complets au prorata, avec plafond légal de six mois. Les barèmes réglementaires sources sont un quart de mois par année jusqu’à dix ans, puis un tiers au-delà. Ce n’est pas une baisse d’impôt.',
    'Le plafond de six mois n’est ni celui de tous les coûts de rupture ni celui des dommages d’illégalité ou d’inaptitude professionnelle. Les indemnités conventionnelles ou contractuelles plus favorables ne sont pas plafonnées par ce texte. Pour les contrats antérieurs, ouverture à huit mois et minima acquis avant la réforme conservés ; seule la composante d’ancienneté future suit0,20et son plafond. Aucun coût national ni effet comportemental n’est quantifié.',
    'Aucun nouveau taux fiscal, justificatif, déclaration ou indemnité patronale n’est créé par cet article. L’indemnité est à l’initiative de l’employeur seulement et reste exclue en faute grave ; l’ordinaire n’est pas due lors d’une démission. Les salaires, congés, indemnités de préavis, réparations d’illégalité et indemnités spéciales demeurent distincts. La nouvelle règle protège le même salaire brut de référence le plus favorable deR1234-4, avec fenêtres de rémunération avant notification ; elle ne remet pas l’ancienneté à zéro.',
    [effect('obligation_removed','indemnite-rupture-ordinaire','Fin de l’indemnité ordinaire entre huit mois et un an pour les nouveaux contrats.',
        'Le CDI licencié hors faute grave ouvre droit à l’indemnité ordinaire dès huit mois d’ancienneté ininterrompue.',
        'Pour le nouveau contrat unique, aucune indemnité ordinaire avant un an mesuré à la fin effective, préavis inclus sous la réserve d’essai ; les autres créances restent dues selon leur régime.',
        'legal_duty','Employeurs et salariés de nouveaux contrats uniques rompus à l’initiative de l’employeur, hors faute grave.',
        'Dès le seuil atteint, la première année n’est pas soustraite : toute l’ancienneté est retenue. Anciens contrats gardent leur ouverture antérieure à huit mois.',
        'Pas de taxe supprimée ni de franchise sur salaires, congés, préavis ou réparation d’une rupture illicite.',
        paragraph('L1234-9',0),paragraph('L1234-9',1,True)),
     effect('coordination','indemnite-rupture-ordinaire','Barème légal, salaire de référence et droits antérieurs coordonnés sous la même mesure.',
        'L1234-9 renvoie au règlement : R1234-2 fixe1/4mois par année jusqu’à dix ans puis1/3au-delà ; R1234-1 prévoit les mois complets ; salaire brut le plus favorable selonR1234-4.',
        'Pour les contrats nouveaux :0,20mois par année totale, prorata des mois complets, plafond légal six mois. Pour les anciens contrats : part antérieure protégée et part future0,20seule plafonnée ; salaire de référence commun à la rupture.',
        'other','Nouveaux contrats uniques, et seule ancienneté postérieure à la réforme des contrats anciens, sous leurs règles propres.',
        'Seuil d’un an au terme effectif pour les nouveaux contrats, pas remise à zéro à ce seuil. Plus favorable conventionnel/contractuel et dommages hors plafond ; faute grave exclue pour cette seule indemnité.',
        'Coordination du même barème : aucune seconde économie ni nouvel impôt n’est compté ; aucune suppression d’indemnité spéciale n’est déduite.',
        paragraph('L1234-9',1),paragraph('L1234-9',1,True))],
    {'R1234-1','R1234-2','R1234-4','L1221-25','L1234-3','L1234-5','L1237-1'})

add('L3123-27','material_reduction',
    'Le plancher légal supplétif de vingt-quatre heures par semaine et ses équivalents mensuel ou aménagé sont supprimés. Sans minimum fixé par un accord de branche étendu, la durée est celle garantie par le contrat écrit. Les minima conventionnels et les dispenses favorables sont préservés ou coordonnés parL3123-7/L3123-19 ; ce n’est pas une autorisation de réduire unilatéralement les heures ou le salaire garanti d’un contrat en cours.',
    'La réforme ne supprime pas tout minimum conventionnel ni les durées minimales d’un régime spécial. Le projetL3123-7 applique la réforme aux contrats en cours comme futurs dans leur champ, préserve les créances antérieures et les garanties du contrat. Les dérogations étudiantes, retraite progressive et besoins temporaires gardent leurs conditions propres. Aucun nombre d’emplois créé ni économie nationale n’est déduit de ce seul retrait.',
    'L’écrit et la durée garantie ne sont pas une obligation créée par cette suppression : ils figuraient déjà dansL3123-6 source. Les règles d’horaires et la priorité d’accès à une durée plus élevée demeurent à leurs articles. Aucune nouvelle déclaration, justification ou taxe n’est ajoutée parL3123-27. La suppression du seuil général ne permet pas un horaire variable à la seule discrétion de l’employeur.',
    [effect('obligation_removed','temps-partiel-plancher-24h','Suppression du plancher légal supplétif de vingt-quatre heures à temps partiel.',
        'À défaut d’accord de branche prévu àL3123-19 : minimum de24heures par semaine ou équivalent mensuel/aménagé, avec dérogations légales.',
        'Aucun minimum légal général de24heures ou équivalent ; sans minimum de branche applicable, durée hebdomadaire ou mensuelle garantie par le contrat écrit.',
        'legal_duty','Employeurs et salariés à temps partiel relevant du dispositif général, sous réserve d’un minimum de branche et des régimes spéciaux.',
        'Contrats en cours et futurs selonL3123-7 proposé ; aucune diminution unilatérale de la durée ou de la rémunération garantie ; droits antérieurs et dispenses favorables conservés.',
        'Écrit, durée garantie et règles conventionnelles subsistent ; aucune formalité équivalente au seuil supprimé n’est créée dans cet article.',
        paragraph('L3123-27',0),paragraph('L3123-27',0,True))],
    {'L3123-3','L3123-6','L3123-7','L3123-19','L3121-44'})

add('L136-8','material_reduction',
    'Le1°duI est le seul alinéa modifié : le taux de CSG passe de9,2%à6,6%pour les rémunérations salariées versées par un employeur de droit privé. Les2,6points portent sur l’assiette de CSG, pas automatiquement sur100%du salaire brut ni sur le net après impôt. L136-1-1 maintient inclusions/exclusions ; L136-2 maintient notamment l’abattement de1,75%sous4PASS dans son champ, ses exceptions et assiettes forfaitaires. Aucun élargissement de l’assiette n’est identifié dans ces textes.',
    'Les autres revenus d’activité, les revenus de remplacement et le patrimoine ne bénéficient pas de cette baisse ciblée : leurs taux/dérogations et seuils revalorisés sont conservés. La CRDS et les autres prélèvements ne sont pas baissés parL136-8. Le financement, les régimes particuliers et la date d’effet de la réforme restent à traiter ; les notes officielles2026 sont celles du droit source, pas une date inventée pour la réforme. Aucun gain national ni net aprèsIR n’est établi.',
    'Aucune nouvelle déclaration, cotisation ou condition de ressources n’est ajoutée parL136-8 ; la restriction à l’employeur de droit privé délimite l’avantage. La coordinationCGI154quinquies proposée rend déductible la CSG privée effectivement payée au taux6,6%, dans sa propre assiette abattue, contre6,8points de déduction dans la source : cet effet sur la base d’IR empêche d’annoncer le même gain aprèsIR pour tous. Il ne s’agit pas d’un nouvel impôt créé dansL136-8 et il n’est pas compté comme une seconde mesure.',
    [effect('tax_reduced','csg-salaires-prives','CSG salariale privée ramenée de9,2%à6,6%, à assiette conservée.',
        'Taux9,2%sur les revenus d’activité visés parL136-1 ; pour les rémunérations salariées privées éligibles, assietteL136-1-1 et abattementL136-2 de1,75%sous4PASS, exceptions et exclusions comprises.',
        'Taux6,6%sur la même assiette des seules rémunérations salariées versées par un employeur de droit privé ; pas de baisse générale des autres revenus.',
        'percent','Salariés percevant des rémunérations versées par un employeur de droit privé et assujettis selonL136-1 ; revenus exonérés restant exonérés.',
        'Autres revenus d’activité, rémunérations publiques et revenus de remplacement à leurs taux propres ; pensions à3,8/6,6/8,3selonconditions, chômage/IJ6,2et autres taux10,6/7,2/9,2ou25dans leurs champs inchangés. Abattements et exemptions maintenus ; entrée en vigueur à coordonner avec le financement.',
        'Pas de nouvelle charge dans cet article ; effet sur l’IR à lire avec154quinquies. Les2,6points d’assietteCSG ne sont pas une hausse universelle de2,6%du brut ou du net aprèsIR.',
        paragraph('L136-8',1),paragraph('L136-8',1,True))],
    {'L136-1','L136-1-1','L136-1-2','L136-2','154 quinquies'})

# Public prose is readable; evidence quotes and stable identifiers stay exact.
def readable(value):
    value=re.sub(r'(?<=\d)%(?=\S)', ' % ', value)
    value=re.sub(r'(?<=\d)%', ' %', value)
    value=re.sub(r'(?<=\d)(?=[A-Za-zÀ-ÿ])', ' ', value)
    value=re.sub(r'(?<=[a-zà-ÿ])(?=(?:L|R)\d)', ' ', value)
    value=re.sub(r'(?<=[a-zà-ÿ])(?=\d)', ' ', value)
    value=value.replace('1°duI', '1° du I').replace('titreIV', 'titre IV').replace('CGI154', 'CGI 154')
    return value
for row in findings:
    assessment=row['substantive_impact']
    for field in ('assessment','scope_limitations','new_burdens_review'):
        assessment[field]=readable(assessment[field])
    for effect in assessment['effects']:
        for field in ('description','before','after','affected_population','conditions_and_transition','replacement_or_new_burdens'):
            effect[field]=readable(effect[field])
    if row['number']=='L136-8':
        assessment['effects'][0]['conditions_and_transition']='Autres revenus d’activité, rémunérations publiques et revenus de remplacement à leurs taux propres : les taux sources de 6,2 %, 8,3 %, 3,8 %, 6,6 %, 10,6 %, 7,2 %, 9,2 % ou 25 % restent dans leurs champs et dérogations respectifs. Les conditions de ressources, exonérations, écrêtements et abattements sont conservés. La baisse ciblée privée n’est pas une extension du taux de 6,6 % à tous ces revenus ; son entrée en vigueur reste à coordonner avec le financement.'
    source=by_number[row['number']]
    proposed=dict(status=source['previous_draft']['status'],proposed_xml=source['proposed_xml'],substantive_impact=assessment)
    rules.validate(proposed,source,required=True,enforce_workflow=False)
    row['substantive_impact_certificate']=rules.certificate(proposed,source,policy_sha)

# Establish one coherent present read of all captured source/notes/proposal views.
guards=[]
with sqlite3.connect('file:'+str(LEGAL/'corpus.sqlite')+'?mode=ro',uri=True)as db:
    db.execute('BEGIN')
    for x in sources+dependencies:
        key=x['code_id'],x['source_id'];raw=db.execute('SELECT source_sha256,content_xml FROM articles WHERE code_id=? AND id=?',key).fetchone()
        assert raw==(x['source_sha256'],x['source_xml']),x['number']
        assert source_notes(db,*key)==x['source_notes_xml'],x['number']
        current=db.execute('SELECT proposed_xml FROM drafts WHERE code_id=? AND source_id=?',key).fetchone()
        assert (current[0]if current else None)==x['proposed_xml'],x['number']
        guards.append(dict(number=x['number'],source_id=x['source_id'],source_and_notes_match=True,proposal_sha256=sha(x['proposed_xml'])))
    db.rollback()
assert policy_sha==sha((LEGAL/'policy-coordinations.json').read_bytes())
# L136-8 really changes only its targeted I,1 paragraph.
x=by_number['L136-8'];old=re.findall(r'<p\b[^>]*>.*?</p>',x['source_xml'],re.S);new=re.findall(r'<p\b[^>]*>.*?</p>',x['proposed_xml'],re.S)
assert len(old)==len(new)and[i for i,(a,b)in enumerate(zip(old,new))if a!=b]==[1]
(P/'article-findings.json').write_text(json.dumps(findings,ensure_ascii=False,indent=2)+'\n')
(P/'validation.json').write_text(json.dumps({'checked_at':now,'articles_read_in_full':5,'dependencies_read_in_full':len(dependencies),'source_notes_and_proposal_consistency_transaction':'read_only_BEGIN','all_guards_current':True,'checks':guards,'classifications':{x['number']:x['substantive_impact']['classification']for x in findings},'CSG_changed_paragraph_only':'I,1°','approved_manifest_modified':False,'database_modified':False,'new_proposals_written':False,'article_findings_sha256':sha((P/'article-findings.json').read_bytes())},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'articles':len(findings),'dependencies':len(dependencies),'classifications':{x['number']:x['substantive_impact']['classification']for x in findings},'all_guards_current':True,'findings_sha256':sha((P/'article-findings.json').read_bytes())},ensure_ascii=False,indent=2))
