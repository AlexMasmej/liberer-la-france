import json,hashlib,sqlite3,sys,copy,shutil
from pathlib import Path
from datetime import datetime,timezone
P=Path(__file__).parent;src=P.parents[1]/'social/edition001';LEGAL=Path('legal-rewrite').resolve();sys.path.insert(0,str(LEGAL))
from ingest import source_notes
from run_exhaustive import validate_answer
from substantive_impact import plain
H=lambda s:hashlib.sha256(s if isinstance(s,bytes)else(s or '').encode()).hexdigest()
def load(n):return json.loads((src/n).read_text())
def save(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert H((src/'source.json').read_bytes())=='9fbca2630e93dc49fdaab45ed75c4b91db6ffc2ed19245661178d21c8fcfbd44'
assert H((src/'answer.json').read_bytes())=='4b7c0982bba570c6e13e158571d03751519c2f26e508651dba690074eb019e9f'
s=load('source.json');a=load('answer.json');ctx=load('context.json');critical={'R243-6-3','R243-7','L131-6-1','L131-6-2','L243-6-1','R142-1','R130-2','L133-5','L133-5-3','L133-5-5','L225-1','L213-1','L752-1','L752-4','R244-1','R613-2','R613-3','170','175'};cs=[x for x in ctx if x['number']in critical];assert len(cs)==19
for name in ['source.json','answer.json','crpa-primary-bodies.json','policy-coordinations.json','site-summaries.json']:
 shutil.copyfile(src/name,P/('reviewed-'+name))
checks=[];db=sqlite3.connect('file:'+str(LEGAL/'corpus.sqlite')+'?mode=ro',uri=True);db.row_factory=sqlite3.Row;db.execute('BEGIN')
for x in s+cs:
 k=(x['code_id'],x['source_id']);b=db.execute('select source_sha256,content_xml from articles where code_id=? and id=?',k).fetchone();doc=db.execute("select xml from documents where code_id=? and id=? and kind='ARTICLE'",k).fetchone()[0];old=db.execute('select source_sha256,proposed_xml from drafts where code_id=? and source_id=?',k).fetchone();pr=x.get('previous_draft');docstr=doc.decode()if isinstance(doc,bytes)else doc
 if x in cs:x['source_document_xml']=docstr;x['source_document_sha256']=H(doc)
 g={'source_identity':b[0]==x['source_sha256'],'source_body':b[1]==x['source_xml'],'source_notes':source_notes(db,*k)==x['source_notes_xml'],'source_document':H(doc)==x['source_document_sha256'],'previous_draft':old is None if pr is None else old is not None and old[0]==pr['source_sha256']and old[1]==pr['proposed_xml']}
 checks.append({'code_id':k[0],'source_id':k[1],'number':x['number'],'guards':g,'all_match':all(g.values())})
db.rollback();db.close();assert all(x['all_match']for x in checks)
validate_answer(copy.deepcopy(a),copy.deepcopy(s))
save('reviewed-critical-references.json',cs)
issues=[{'id':'social-001','number':'L613-2','severity':'requires_correction','source_quote':'les travailleurs indépendants sont tenus d’effectuer la déclaration','proposed_quote':"les seuls éléments nécessaires au calcul qui ne leur ont pas déjà été transmis ou auxquels ils n'ont pas légalement accès",'primary_control':'CRPA L113-12, L114-8/9, L100-3 ; L133-5-3 projetIIter','counterexample':'Une donnée n’a pas encore été transmise à l’Urssaf, mais est directement obtenable légalement de laDGFiP pour ce calcul. Le premier membre duOU est vrai, donc la phrase peut la réclamer malgré le droit existant. La phrase suivante sur donnéesdéjàdisponibles n’exprime pas assez clairement le droit aux données obtenables.','required_change':'Définir comme restantàtransmettre les seules données ni détenues/transmises ni directement obtenables légalement, exactes et àjour ; conserver corrections des erreurs, élémentsmanquants et déclarationfiscale.','author_acknowledged':True,'new_edition_pending':True},{'id':'social-002','number':'R243-8','severity':'requires_correction','source_quote':"L'autorisation de versement des cotisations à un organisme de recouvrement unique est délivrée sur demande de l'entreprise",'proposed_quote':"Le dépôt de cette demande vaut option ; aucune autorisation préalable n'est requise.",'primary_control':'CSS L243-1-2 et R243-8-1 entiers, R243-6-3III entier','counterexample':'Un employeur étranger sans établissement enFrance, déjà obligatoirement rattaché à un organisme désigné en application deL243-1-2/R243-8-1, n’entre pas nécessairement dansR243-6-3. La nouvelle option générale lui permet littéralement de choisir un autre organisme. L’ancienne demande devait obtenir une autorisation ; le nouveau droit ne doit pas contourner le rattachement légal obligatoire.','required_change':'Réserve expresse des affectations obligatoires L243-1-2/R243-8-1 et autres compétences légales spéciales ; garder la suppression d’autorisation pour les entreprises réellement admissibles.','author_acknowledged':True,'new_edition_pending':True}]
findings={
'L243-1-2':'Maintien justifié : organisme unique obligatoire des employeurs étrangers, moyens électroniques et forfait conditionnel. Aucune durée de séjour transformée en terme automatique du contrat ; régime de paiement et exclusions conservés.',
'L611-1':'Maintien du champ des indépendants et options loueurs, seuils20%PASS/recettes et conjoints ; aucun avantage d’affiliation retiré.',
'L613-2':'Correction nécessaire : conditionOU à clarifier pour les données directement obtenables légalement, sans redéclaration fiscale supprimée.',
'L613-3':'Information, simulation indicative, échéancier et recouvrementcoordonné demeurent ; aucun allègement nouveau artificiel.',
'L613-4':'Radiation après deux années civiles, information/opposition et transmissions autresregistres restent protectrices ; dettes non remises.',
'R131-3-1':'Annualisation/prorata conservés, deux premières années exclues ; aucun appel annuel intégral pour une affiliationpartielle nouvelle.',
'R131-9':'Report ouvert malgré premierversement, mais uniquement sommesrestantdues et demande30jours ; pas de remboursement fondé sur le report. L131-6-1 conserve12mois/5ans/fractions20%/unefois5ans et absence majoration. Cessation60jours et prorata inchangés. Facilité de trésorerie, pas taxe supprimée.',
'R611-1':'Réemploi exact/légal/suffisant et délai30jours préservés ; CRPA protège déjà le droit, classificationcoordination prudente.',
'R611-2':'Radiation contradictoire : échangesorganismes6mois, opposition1mois et notificationrecours préservés ; versionactuelle seule.',
'R611-3':'Affiliation par résidence, dérogationssanté/activité/étranger et effet début/finactivité inchangés.',
'R613-1-1':'Donnéesnécessaires et délaisfiscaux restent ; transmissionDGFiP7jours et libéraux1mois, donnéesPAMC et manquantes conservées. Pénalité5% réservée au manquement restant, non au doublon dispensé. Dépend de correctionL613-2.',
'R613-1-2':'Calculsprovisoires/plancher50%PASS/majoration25% conservés, donnéesfiscales utiles et demandedesmanquantes2mois ;10%ne frappe pas la seule absence d’un doublon. Régularisation, contradictoire et délais30–180/15jours maintenus. Renvois ordinaux préexistants non corrigés silencieusement.',
'R613-1-3':'Tropversé remboursé/imputé puis reliquatrestauré, priorité desdettes anciennes ; créancepositive et solde négatif inchangés.',
'R613-1-5':'Cessation90jours et paiement/remboursement30jours gardés ; donnéesdéjàlégalementdisponibles et manquantes ensemble pour liquidation définitive. Aucun nouveau formulaire.',
'R613-5':'Échéancier15jours déjà multi-usages, remboursements/ordreimputation conservés ; pas de fusionnouvelle comptée.',
'R613-17':'PASSannuel proratisé affiliationincomplète préservé.',
'R613-18':'Documents complémentaires réellementnécessaires et contrôle distinct restent ; rapprochementdéjàexistant non comptécomme coupe.',
'R613-19':'Notifications, modecalcul, assistance,30jours et réponsemotivée restent ; indusrestituables inchangés.',
'R243-6':'DSN/versement parétablissement et échéances5/15 conservés ; optionunique ne change ni dette ni affectation salariésR130-2.',
'R243-6-1':'Optiontrimestrielle<11salariés et tacitereconduction préexistante conservées, DSNmensuelle subsiste ; aucune fusion prétendue.',
'R243-8':'Suppression réelle de l’autorisation, conditionspaiement/déclarationsàjour et choixcaisse conservés. Réserve desaffectationsobligatoires à rendre expresse avant approbation.',
'R243-8-1':'Rattachements sectoriels et étrangers obligatoires maintenus ; ne doivent pas être contournés parR243-8nouveau.',
'R243-10':'Correction d’erreurs, remboursementàdemande et exceptionsauxmajorations demeurent ; pas de nouvelle pénalité.',
'R243-43-1':'Réemploi limitéauxdocuments identifiables/légalementobtenables ; demande écrite/motivée, interruptionrecours maisnonprescription, complétude30jours, position40jours, notifications30jours identiques. DroitCRPAdéjàexistant noncomptécommegainnouveau.'}
for x,y in zip(s,a):
 c=next(z for z in checks if z['code_id']==x['code_id']and z['source_id']==x['source_id'])
 c.update(source_body_sha256=H(x['source_xml']),source_notes_sha256=H(x['source_notes_xml']),source_document_sha256=x['source_document_sha256'],reviewed_proposed_sha256=H(y['proposed_xml'])if y.get('proposed_xml')else None,full_source_notes_proposal_read=True,classification=y['substantive_impact']['classification'],verdict='requires_correction'if x['number']in['L613-2','R243-8']else'no_other_concrete_defect_found',finding=findings[x['number']])
report={'reviewed_at':datetime.now(timezone.utc).isoformat(),'edition':'001','verdict':'changes_requested_two_articles','source_sha256':H((src/'source.json').read_bytes()),'answer_sha256':H((src/'answer.json').read_bytes()),'context_sha256':H((src/'context.json').read_bytes()),'frozen_inputs_unchanged':True,'full_source_notes_proposal_reads':24,'full_critical_context_reads':19,'crpa_full_primary_bodies_read':['L100-3','L113-12','L114-8','L114-9'],'technical_checks':{'validate_answer':'passed_on_deepcopy','guards_per_article':5,'total_article_guards':len(checks)*5,'all_match':True,'policy_checks':{f:H((src/f).read_bytes())==H((LEGAL/f).read_bytes())for f in['policy-coordinations.json','site-summaries.json']}},'issues':issues,'article_findings':checks[:24],'critical_reference_guards':checks[24:],'counting_review':{'R243_8':'Une autorisation retirée, sous correction du champ des affectations obligatoires.','R131_9':'Une facilité de calendrier, sans baisse de cotisations ni remboursement de paiements valables.','six_reemployment_coordinations':'Coordination_only ; CRPA2022 couvre déjà administrationssociales et données détenues/obtenables. Aucune nouvelle économie nationale démontrée.','retained':'16maintenusnull, ne sont ni réécrits ni simplificationsnouvelles.'},'limits':['19ciblescritiques lues entières ; les14autrescontexte sont fournis par l’auteur mais pas revendiqués comme relusentièrement ici.','Pas de XMLDILAoriginal CRPA : corps primairesLégifrance/search entiers et réponses conservés ; distinction2022/historique conservée.','Pas de validation globale du financement ni de tous lescodes.','001nonapprouvée : nouvelleédition à capturer et contre-lire sans écraser l’état de rejet.'],'canonical_mutations':False}
save('review.json',report);save('review-001.json',report)
(P/'audit.md').write_text('''# Contrelecture indépendante social001

Verdict : deux corrections nécessaires, sur L613-2 et R243-8. Les24sources/notes/propositions ont été lues en entier ;19cibles critiques et les4corps primairesCRPA ont été relus. Les215gardes des43articles contrôlés concordent etvalidate_answer passe, sans emporter approbation du fond.

1. L613-2 : une donnée non encore transmise mais légalement obtenable auprès deDGFiP satisfait le premier membre du«OU». Cette rédaction peut réimposer le doublon protégé parCRPAL113-12. L’auteur a confirmé la correction : seules données ni détenues/transmises ni directement obtenables légalement restent à fournir, sans perdre lescorrections/élémentsmanquants ni la déclaration fiscale.
2. R243-8 : le droitd’option doit expressément respecter les affectations obligatoires deL243-1-2/R243-8-1. Un employeurétranger sous250salariés pourrait sinon invoquer l’option générale pour choisir une autre caisse que celle imposée par la loi. L’auteur a confirmé une réserve explicite, sans retour à l’autorisation des entreprises ordinaires admissibles.

Aucun autre défaut concret relevé. R131-9 ouvre une facilité sur les seules sommesrestantdues, sans remboursement du seul fait du report ;12mois,5ans,20%,unefois5ans et cessation60jours restent cohérents avecL131-6-1 entier. Les6coordinations de réemploi sont correctement non comptées comme nouveaux gains ; le droit existe déjà auCRPA, dans sonchamp et sesfinalités. Les16maintiensnull ne sont pas comptés comme réécrits.

L’édition001 et ses empreintes sont archivées. Aucune candidature de l’auteur, base, politique ou publication n’est modifiée. Le verdict d’une édition corrigée fera l’objet d’un fichier distinct.
''')
files=[f for f in sorted(P.iterdir())if f.is_file()and f.name!='manifest.json'];save('manifest.json',{'frozen':True,'edition_reviewed':'001','files':{f.name:H(f.read_bytes())for f in files},'canonical_mutations':False})
print('review',H((P/'review.json').read_bytes()),'manifest',H((P/'manifest.json').read_bytes()))
