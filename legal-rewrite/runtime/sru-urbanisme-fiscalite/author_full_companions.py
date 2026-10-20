from pathlib import Path
import copy, hashlib, json, re, sqlite3, sys

H=Path(__file__).resolve().parent
B=H.parents[1]
OUT=B/'runtime/sru-integral/collectivites-companions/002'
OUT.mkdir(parents=True,exist_ok=True)
sys.path.insert(0,str(B))
from run_exhaustive import validate_answer
from register_batches import Markup
db=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True)
db.row_factory=sqlite3.Row
raw=json.loads((H/'full-law-outside-evidence.json').read_text())['articles']
by={a['number']:a for a in raw if a['valid_from']<='2026-10-18'<a['valid_until']}
rows=[]
def sha(s):return hashlib.sha256(s.encode()).hexdigest()
def replace(s,b,a):
    assert s.count(b)==1,b
    return s.replace(b,a)
def add(num,body,reason,review,removed=None,repeal=None):
    a=copy.deepcopy(by[num])
    a['kind']='code_article'if a['owner'].startswith('LEGITEXT')else'noncodified_article'
    a['code_id']=a['owner']
    a['title']=({'LEGITEXT000006070633':'CGCT','JORFTEXT000000875580':'Loi n° 72-657 du 13 juillet 1972','JORFTEXT000000207538':'Loi SRU n° 2000-1208 du 13 décembre 2000'}[a['owner']])+' — article '+num
    a['source_article_raw_sha256']=a['source_sha256']
    a['source_body_sha256']=sha(a['source_xml'])
    assert sha(a['whole_article_xml'])==a['source_sha256']
    archive=dict(db.execute('SELECT *FROM archives WHERE name=?',(a['archive'],)).fetchone())
    a['provenance']={'provider':'DILA — LEGI','archive':a['archive'],'archive_sha256':archive['sha256'],'archive_source_url':archive['source_url'],'article_member':a['archive_member'],'as_of':'2026-10-18','archives_replayed':467}
    a.update(proposed_xml=body,proposed_sha256=sha(body),status='proposal_not_adopted',reason=reason,review_notes=review,prior_proposal_sha256=None,excluded_from_30317_counter=True)
    if removed:a.update(change_type='normative_reduction',reform_policy_id='editorial_direction_2026_10_19',removed_provisions=removed)
    if repeal:a.update(change_type='full_repeal',repeal_policy_id='editorial_direction_2026_10_19',repeal_scope=repeal)
    test=copy.deepcopy(a);test['status']='rewrite_draft';validate_answer([test],[a])
    rows.append(a)

transition='Les contrats, conventions, opérations, aides et droits des tiers antérieurement valablement engagés ou constitués, ainsi que les créances légalement nées à leur titre, ne sont pas remis en cause par cette seule abrogation. Leur exécution, leurs voies ordinaires de modification, de contrôle, de restitution et de recours demeurent régies par les règles qui leur sont applicables. Les compétences ou concours disposant d’un fondement légal distinct ne sont ni supprimés ni étendus. Aucun remboursement général ni compensation automatique n’est créé.'
entry='à compter de l’entrée en vigueur de la loi abrogeant la loi n° 2000-1208 du 13 décembre 2000'
for num,scope in (
    ('L1523-5','Habilitation spéciale créée par SRU 62 pour les subventions, avances et cessions immobilières des collectivités et groupements aux SEM logement, et ses obligations d’étude, plafonnement et convention propres.'),
    ('L1523-6','Habilitation spéciale créée par SRU 62 pour les subventions exceptionnelles de redressement aux SEM logement, et ses obligations de rapport spécial, certification et information annuelle propres.'),
    ('L2254-1','Obligation communale et intercommunale d’intervention foncière, d’aménagement ou de subvention permettant la réalisation de logements sociaux pour la mixité, créée par SRU 64 I1°.')):
    body='<p>Le présent article est abrogé '+entry+'.</p><p>'+transition+'</p>'
    if num=='L1523-5':body+='<p>Les effets des validations de conventions antérieures légalement acquis avant cette abrogation sont préservés, sous réserve des décisions de justice devenues définitives et des recours régis par le droit qui leur est applicable. L’abrogation ne rétablit pas les obligations de tableau de cessions supprimées lors d’une réforme antérieure.</p>'
    add(num,body,'Abroger la norme spéciale effectivement créée par SRU, avec préservation des engagements et droits antérieurs ; ne pas supprimer les pouvoirs de droit commun préexistants.',
        'Source actuelle, notes et source SRU initiale entièrement lues ; aucune proposition précédente hors corpus. '+('L1523-5 reste en vigueur depuis 2010 ; la seule suppression ultérieure d’une référence au tableau des cessions ne remplace pas son habilitation principale. La note de l’ordonnance 2009-1400 vise l’exercice 2010 et ne fixe pas la date de notre réforme. Les validations historiques sont expressément sauvegardées.'if num=='L1523-5'else'Norme créée au 14 décembre 2000 et toujours en vigueur sans changement de fond dans la source actuelle. La suppression vaut pour l’avenir ; aucune annulation rétroactive de financements ou extinction de créances légales. Le fait que la norme autorise certains concours ne permet pas de prétendre à une économie budgétaire chiffrée.'),repeal=scope)

body=replace(by['L1525-3']['source_xml'],', à l’exception des articles L. 1523-5 et L. 1523-6', '')if ', à l’exception des articles L. 1523-5 et L. 1523-6'in by['L1525-3']['source_xml']else replace(by['L1525-3']['source_xml'],", à l'exception des articles L. 1523-5 et L. 1523-6",'')
body+='<p>Le retrait de la seule exception du 3° prend effet à la date d’abrogation des articles L. 1523-5 et L. 1523-6, sous les mêmes dispositions transitoires pour les conventions, aides, opérations, validations et droits antérieurs. Il ne soumet pas les sociétés mentionnées au présent article aux autres dispositions du titre dont elles demeurent exclues.</p>'
add('L1525-3',body,'Retirer uniquement l’exception aux exclusions du titre créée par SRU 63, devenue sans objet après abrogation des deux habilitations de financement.',
    'Article entier lu avec sa note vide. Introduction et exclusions 1°/2°/3° conservées, dont les renvois aux sociétés HLM, aux sociétés régionales de financement et à la loi 46-860. Seuls les mots rendant L1523-5/6 applicables aux SEM outre-mer sont supprimés. Transition alignée sur les deux articles abrogés, aucune généralisation du titre.',
    removed=['Suppression de l’exception du 3° qui étendait aux SEM outre-mer les seuls concours spéciaux de L1523-5 et L1523-6 créés par SRU.'])

body=by['L5216-5']['source_xml']
body=replace(body,'actions et aides financières en faveur du logement social d’intérêt communautaire ; réserves foncières pour la mise en oeuvre de la politique communautaire d’équilibre social de l’habitat ; ','')if 'actions et aides financières en faveur du logement social d’intérêt communautaire'in body else replace(body,"actions et aides financières en faveur du logement social d'intérêt communautaire ; réserves foncières pour la mise en oeuvre de la politique communautaire d'équilibre social de l'habitat ; ",'')
body=re.sub(r'<p>II bis\.-La communauté d.agglomération est titulaire du droit de préemption urbain.*?</p>','<p>II bis. – Abrogé.</p>',body,count=1,flags=re.S)
body+='<p>VIII. – Le retrait des seules compétences explicites d’aides financières et d’actions en faveur du logement social et de réserves foncières ajoutées au 3° du I par SRU, ainsi que l’abrogation du II bis, prennent effet '+entry+'. Les autres compétences de ce 3° et les autres groupes de compétences restent applicables. Les compétences, délégations et droits de préemption disposant d’un fondement légal distinct conservent leur régime ; le seul ancien II bis ne fonde plus une décision nouvelle de préemption. Les décisions de préemption déjà valablement prises, acquisitions, contrats, opérations, biens, engagements et droits des tiers ne sont pas annulés de ce seul fait. Les modalités ordinaires de transfert ou de restitution des compétences, biens, contrats et personnels demeurent applicables ; aucun transfert matériel ou résiliation n’est opéré automatiquement par le présent VIII.</p>'
add('L5216-5',body,'Retirer les deux ajouts de compétence financière/foncière de SRU 64 I2° et la préemption spéciale créée par I3°, sans supprimer les compétences habitat antérieures de la communauté d’agglomération.',
    'Source actuelle de 2022, note mobilité 2021 et version antérieure au 14 décembre 2000 entièrement lues. I3° conserve PLH, politique du logement d’intérêt communautaire, opérations pour personnes défavorisées et amélioration du parc, déjà présentes en 1999. Les seules clauses actions/aides sociales et réserves foncières ajoutées sont retirées. II bis devient abrogé sans renumérotation. Tous les autres I1°/2°/4°–10°, II, III–VII, eau, assainissement, tourisme et conventions sont intégraux. VIII assure la transition, sans annuler d’acquisition ni attribuer une compétence nouvelle. Aucun retour automatique à toutes les versions de 1999.',
    removed=['Suppression des compétences expresses d’actions et aides financières au logement social et de réserves foncières ajoutées par SRU au I3°, tout en conservant les compétences habitat préexistantes.','Suppression de la préemption communautaire spéciale fondée seulement sur le II bis créé par SRU 64 I3°, sans toucher aux fondements de droit commun.'])

body=by['L5214-16']['source_xml']
body=re.sub(r'<p>VI\. ― La communauté de communes, lorsqu.elle est dotée d.une compétence dans ce domaine, peut exercer le droit de préemption urbain.*?</p>','<p>VI. – Abrogé.</p>',body,count=1,flags=re.S)
body+='<p>VIII. – L’abrogation du seul VI prend effet '+entry+'. Les compétences habitat et d’urbanisme, les délégations et les droits de préemption disposant d’un autre fondement légal conservent leur régime. Le seul ancien VI ne fonde plus une décision nouvelle de préemption. Les décisions de préemption déjà valablement prises, acquisitions, contrats, opérations et droits des tiers ne sont pas annulés de ce seul fait. Les voies ordinaires de modification, de transfert, de restitution et de recours restent applicables, sans transfert matériel automatique de biens, contrats ou personnels.</p>'
add('L5214-16',body,'Abroger seulement la préemption spéciale pour l’équilibre social de l’habitat créée au VI par SRU 64 I4°, en conservant toutes les compétences de droit commun de la communauté de communes.',
    'Article entier actuel 2025 et note vide lus. VI devient abrogé sans décaler VII ; I à V et VII, tous groupes de compétences, eau/assainissement 2025, tourisme, délais deux mois/deux ans et majorité qualifiée conservés. VIII garantit les opérations et droits antérieurs, sans faire survivre l’ancien VI comme titre exclusif pour une préemption nouvelle. Les délégations et autres fondements de préemption ne sont pas supprimés.',
    removed=['Suppression de la seule habilitation spéciale de préemption urbaine pour l’équilibre social de l’habitat au VI, créée par SRU 64 I4°.'])

body=replace(by['L5215-20']['source_xml'],'; aides financières au logement social ; actions en faveur du logement social','')
body+='<p>VI. – Le retrait des seules compétences explicites d’aides financières et d’actions en faveur du logement social introduites au b du 3° du I par SRU prend effet '+entry+'. La politique du logement, les actions en faveur des personnes défavorisées, le programme local de l’habitat et les autres compétences préexistantes ne sont pas supprimés. Les concours, opérations et contrats antérieurement valablement engagés, les biens et droits des tiers demeurent protégés selon leurs règles propres. Les voies ordinaires de modification, de transfert ou de restitution de compétences, biens, contrats et personnels restent applicables ; aucun transfert matériel ou résiliation n’est opéré automatiquement par le présent VI.</p>'
add('L5215-20',body,'Retirer les seules compétences expresses d’aides financières et d’actions de logement social issues de SRU 64 I5°, sans supprimer la politique du logement ni les autres compétences habitat antérieures.',
    'Source actuelle 2022, note mobilité 2021 et version antérieure à SRU lues entièrement. La politique du logement social existait avant 2000 ; SRU l’a remplacée par ces deux habilitations. Les limites d’intérêt communautaire ont ensuite été réformées ; elles ne sont pas restaurées artificiellement. Tous I1°–7°, II abrogé, III–V et les autres subdivisions restent intégraux. VI protège engagements et droits sans rétablir la norme supprimée pour les décisions futures.',
    removed=['Suppression des seules compétences expresses d’aides financières et d’actions en faveur du logement social substituées par SRU 64 I5° à la rédaction antérieure, sans supprimer les autres compétences de logement.'])

body=replace(by['3']['source_xml'],"<p>Les établissements situés à l'intérieur des quartiers prioritaires de la politique de la ville bénéficient d'une franchise de 1 500 euros sur le montant de la taxe dont ils sont redevables.</p>",'<p>Les établissements situés à l’intérieur des quartiers prioritaires de la politique de la ville ne bénéficient plus de la franchise de 1 500 euros pour les impositions dont le fait générateur est postérieur à l’entrée en vigueur de la loi abrogeant la loi n° 2000-1208 du 13 décembre 2000. Les impositions dont le fait générateur est antérieur restent régies par les règles qui leur étaient applicables, avec leurs droits à la franchise, dettes, contrôles, réclamations et restitutions. Aucun remboursement général ni reprise rétroactive de cette franchise n’est créé. Les autres taux, assiettes, seuils, réductions et majorations du présent article ne sont pas modifiés par cette suppression.</p>')
add('3',body,'Retirer la franchise de TASCOM créée par SRU 68 et aujourd’hui de 1 500 € en QPV. Cette suppression accroît la taxe des établissements auparavant éligibles ; elle n’est pas présentée comme une baisse fiscale et ne change aucun taux.',
    'Arbitrage exprès du parent selon la demande la plus récente « Toute la loi SRU ». Article 3 actuel de la loi 72-657 et notes 2014/2015 lus entièrement ; aucune proposition antérieure. Tous les autres paragraphes, tarifs, formules, plafonds, surfaces et seuils sont intégraux. Le sixième paragraphe est remplacé par la suppression et sa transition afin de conserver les renvois ordinaux. Aucune hausse nationale chiffrée, nouveau tarif ou rendement budgétaire inventé. Les faits générateurs antérieurs gardent leur franchise et leurs recours ; les dates de 2015 en note ne deviennent pas la date de la réforme.',
    removed=['Suppression prospective de la franchise TASCOM de 1 500 euros des établissements situés en QPV, descendant de la franchise de 10 000 francs créée en ZUS par SRU 68.'])

for num,scope in (
    ('88','Création du fonds de revitalisation économique et habilitation à verser les aides propres à ce fonds, issues de SRU 88 et désormais définies pour les QPV et certains autres territoires prioritaires.'),
    ('89','Régime spécial des sociétés d’investissement régional, concours régionaux, interventions, représentation, seuil du tiers du capital et des voix, et rapport annuel propres à SRU 89.')):
    body='<p>Le présent article est abrogé '+entry+'.</p><p>'+transition+'</p>'
    if num=='88':body+='<p>Aucune aide nouvelle ne peut être accordée sur le seul fondement du fonds institué par l’ancien présent article. Les aides antérieurement valablement décidées demeurent exécutées sous leurs conditions, sans prorogation ou renouvellement automatique. Les dispositifs d’aide disposant d’une autre base légale conservent leur champ et leurs conditions.</p>'
    else:body+='<p>Cette abrogation ne dissout pas les sociétés existantes, ne modifie pas automatiquement leurs statuts, leur capital ou les participations détenues et n’impose aucune cession forcée. Les droits attachés aux participations et conventions déjà valablement constituées, ainsi que les engagements de restitution ou de garantie qui en résultent, demeurent protégés. Les décisions nouvelles de participation, de prêt, de garantie ou de subvention doivent disposer d’un fondement légal distinct ; le seul ancien présent article ne les autorise plus. Les clauses statutaires ou conventionnelles existantes ne sont modifiées que selon les règles qui leur sont applicables.</p>'
    add(num,body,'Abroger la norme autonome de la loi SRU elle-même, avec protection des engagements, sociétés et droits antérieurs ; aucune abrogation nominale d’un article modificatif n’est substituée à ce retrait.',
        'Source initiale entière et source actuelle entière lues, notes et provenance conservées. '+('Article 88 modifié en 2014, en vigueur depuis le 1er janvier 2015 : trois paragraphes, QPV et aides, renvoi au décret. La présence du texte ne prouve ni crédits ni activité opérationnelle actuels ; aucune économie budgétaire chiffrée revendiquée. Le sort des mesures réglementaires prises pour ce fonds reste à confronter avant toute assertion de purge exhaustive.'if num=='88'else'Article 89 toujours en vigueur depuis le 14 décembre 2000, I à III intégraux dans la source. La suppression couvre son habilitation spéciale et ses propres obligations, sans liquidation forcée ni suppression des compétences générales d’investissement. La citation ancienne de CGI 217 quaterdecies a été vérifiée : support abrogé au 1er janvier 2014 par loi 2013-1278 article 26, dernière version LEGIARTI000022328038. Aucun avantage fiscal courant à supprimer ou recréer au seul titre de cette citation périmée ; source historique entière conservée dans sir-supporting-source.json. Les droits et contentieux antérieurs restent distincts.'),repeal=scope)

cgct=[a for a in rows if a['owner']=='LEGITEXT000006070633']
rows=[a for a in rows if a['owner']!='LEGITEXT000006070633']
pending=OUT.parent/'pending-cgct'
pending.mkdir(exist_ok=True)
(pending/'manifest.json').write_text(json.dumps({'title':'CGCT matérialisé avant checkpoint — contrôle croisé restant','status':'pending_cross_reference_review_do_not_integrate','outside_code_inventory':True,'excluded_from_30317_counter':True,'articles':cgct,'limits':['7 propositions complètes matérialisées avant le dernier checkpoint du parent ; validation structurelle passée, contrôle croisé de toutes les références CGCT restant.','Ne pas intégrer ce fichier avec le lot validé TASCOM/88/89 sans revue distincte.']},ensure_ascii=False,indent=2)+'\n')
manifest={'title':'Compagnons candidats — TASCOM SRU68 et normes autonomes SRU88/89','as_of':'2026-10-18','outside_code_inventory':True,'excluded_from_30317_counter':True,'status':'candidate_not_registered_not_published','articles':rows,'limits':['3 articles complets, hors compteur des 30 317 entrées.','Ces candidats ne prouvent pas à eux seuls la purge réglementaire de tous les descendants de SRU 88/89.','Aucune économie chiffrée n’est déduite mécaniquement de l’abrogation du fonds ou du régime SIR.','Le retrait TASCOM est explicitement moins favorable aux établissements auparavant éligibles, selon arbitrage exprès du parent.','L’ancien CGI217quaterdecies issu de SRU90 est déjà abrogé depuis 2014 : citation historique vérifiée, aucun renvoi fiscal actif identifié sur ce lien.']}
support=json.loads((H/'sir-supporting-source.json').read_text())
support.update(kind='code_article',source_xml=support['content_xml'],status='source_reference_only',proposed_xml=None,excluded_from_30317_counter=True,review_notes='Support historique de SRU90 déjà abrogé au 1er janvier 2014 ; citation de la métadonnée de SRU89 périmée, non comptée comme réécriture nouvelle.')
manifest['supporting_sources']=[support]
(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
proof={'validated_articles':len(rows),'registered':False,'published':False,'articles':[{'number':a['number'],'source_id':a['source_id'],'proposed_sha256':a['proposed_sha256']}for a in rows]}
(OUT/'validation.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2)+'\n')
print('VALIDATED',len(rows))
