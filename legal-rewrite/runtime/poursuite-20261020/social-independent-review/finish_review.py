import copy,hashlib,json,sqlite3,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT));from ingest import source_notes
from run_exhaustive import validate_answer
base=ROOT/'runtime/poursuite-20261020';out=base/'social-independent-review'
def H(v):return hashlib.sha256((v or '').encode() if not isinstance(v,bytes) else v).hexdigest()
def read(p):return json.loads(p.read_text())
def write(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
packs=[base/'social/edition001',base/'social-legislative-complement/edition001']
expected_hashes=[('677ac463515ab8a0c7fef9d1549f3ef0aa4b3cb1102a257d69cfa5107c79d74b','2ab169896f9d32a9f251f3526e19c251b5dd4809b1f98755eda2d59655a1439f'),('eff617d4f6129221bdd99b51c8a1cafcc2ccc55ed0eb8f48123ec111bbcaba49','4c72d4dafc10a5ae36b2421f740ab52d6851f465c7297f21472b5923784bd683')]
findings={
'L242-1-3':'Transmission inter-organismes des corrections de droits sociaux et de retraite complémentaire maintenue ; aucune nouvelle formalité employeur et aucune exonération supprimée.',
'L242-1-4':'Franchise de 15 % du SMIC mensuel et contribution libératoire de 20 % jusqu’à 1,5 SMIC mensuel annuels conservées ; seuils, exclusions de groupe et anti-fraude inchangés. La copie documentaire ne conditionne pas un avantage supplémentaire.',
'L242-3':'Répartition des plafonds multi-employeurs et option alternative du II intactes ; les abattements et les forfaits spéciaux ne sont pas absorbés par une règle générale.',
'L242-8':'Abattement de plafond à temps partiel conservé, dans son champ propre.',
'L242-9':'Application par échéance et exclusion lors du dépassement des heures normales de l’établissement conservées ; aucune assimilation silencieuse au seul seuil nouveau de quarante heures.',
'L242-10':'Exclusions et régimes propres, dont travail temporaire et activité partielle, conservés. Aucun effacement des droits d’intermission.',
'L242-14':'Suppression effective de la notification annuelle autonome d’attributions d’actions et de la déchéance de l’exclusion liée à son omission ; l’exclusion de L242-1 II 6°, les déclarations autonomes et les contrôles restent opérants. Champ des sociétés étrangères conservé et transition par périodes de cotisation.',
'R133-13':'Coordination nécessaire : le signalement suit la fin effective de l’emploi, non la seule fin d’affectation, mission ou formation. Les six subdivisions, destinataires, finalités et garanties DSN sont conservés ; pas de dispense du dernier mois d’emploi ni de contrats encore en cours.',
'R133-14-1':'Échéance des déclarations de revenus de remplacement au dix du mois suivant et report au jour ouvrable conservés. Aucun nouveau plafond de cumul de retraite.',
'R133-14-2':'Rectification contradictoire et délai minimal de trente jours conservés ; opposition et recouvrement distincts.',
'R133-14-3':'Substitution et information de l’employeur et du salarié conservées ; aucune disparition de droits sociaux par correction silencieuse.',
'R133-14-4':'Réponse motivée aux observations avant recouvrement conservée.',
'R133-14-5':'Notification du trop-versé et imputation ou remboursement conservés.',
'R133-14-6':'Correction technique sans quitus matériel de contrôle conservée ; pas d’extension du pouvoir de substitution.',
'R133-15':'Barèmes proportionnés de 0,5 % et 0,25 % du plafond mensuel, limites et remises conservés. La suppression réglementaire seule de toutes pénalités ne serait pas opérante face à L133-5-4.',
'R133-16':'Reversement préalable des parts salariales et du prélèvement à la source pour le plan de règlement conservé ; détournement distinct d’une simple erreur de bonne foi.',
'R133-43':'Choix et périmètre du mandat conservés, recours aux données déclaratives existantes plutôt que répétition. Fraude personnelle distincte de la situation de l’ensemble de la structure.',
'R133-44':'Double avis du mandataire sous huit jours supprimé ; notification de l’organisme au client, contradictoire d’un mois, durée maximale de cinq ans et restitution des pièces sous un mois maintenus. Opérante avec le correctif conjoint L133-11, dont le texte ancien imposait encore le second avis.',
'R242-3':'Modèle ministériel obligatoire et retransmission des données déjà légalement disponibles retirés ; seuls les éléments manquants restent exigibles. Échéances de fin de mois ou trimestre et cinq premiers jours du trimestre inchangées ; calcul subsidiaire, remboursement, recours R242-4 et alternative L242-3 II conservés.',
'R242-4':'Contestation et répartition subsidiaire par l’organisme compétent conservées.',
'D242-2-2':'Copie du document du salarié non imposée à l’employeur lorsque l’information effective est fournie par un document ou échange existant. Montants de l’avantage et des contributions, deux échéances alternatives et règles de franchise préservés. L’information du salarié due par une autre norme subsiste.',
'R243-27':'Paiement des cotisations sur revenus de remplacement coordonné à leur DSN ; aucune confusion avec une rémunération d’activité.',
'R243-28':'Garanties de recouvrement, remises et dispositions territoriales conservées ; pas de remise en cause d’exonération ni de cumul de pension.',
'R243-29':'Conservé : l’information annuelle des bénéficiaires ne prescrit pas un relevé séparé. Aucune simplification fictive ni suppression des quatre montants utiles au bénéficiaire.',
'L133-11':'Correctif législatif entier nécessaire à R133-44 : l’avis sans délai donné par l’organisme tient lieu d’information du client et le règlement ne peut recréer un second avis. Mandat, réponse aux organismes, fraude, maximum de cinq ans et recouvrement inchangés ; transition des décisions nouvelles sans réouverture des anciennes.'}
db=sqlite3.connect('file:'+str(ROOT/'corpus.sqlite')+'?mode=ro',uri=True);db.row_factory=sqlite3.Row;db.execute('BEGIN')
rows=[];packages=[]
for p,(sh,ah) in zip(packs,expected_hashes):
 assert H((p/'source.json').read_bytes())==sh;assert H((p/'answer.json').read_bytes())==ah
 sources=read(p/'source.json');answer=read(p/'answer.json');validate_answer(copy.deepcopy(answer),sources)
 packages.append({'path':str(p.relative_to(ROOT)),'source_sha256':sh,'answer_sha256':ah,'article_count':len(sources)})
 for s,a in zip(sources,answer):
  assert (s['code_id'],s['source_id'])==(a['code_id'],a['source_id'])
  key=(s['code_id'],s['source_id']);ar=db.execute('select * from articles where code_id=? and id=?',key).fetchone();raw=db.execute("select xml from documents where code_id=? and id=? and kind='ARTICLE'",key).fetchone()[0];notes=source_notes(db,*key);dr=db.execute('select * from drafts where code_id=? and source_id=?',key).fetchone()
  prior=s.get('previous_draft');doc=s['source_document_xml'];body=s['source_xml']
  guards={
  'source_identity':{'expected':s['source_sha256'],'actual':ar['source_sha256'],'matches':s['source_sha256']==ar['source_sha256']},
  'source_body':{'expected':H(body),'actual':H(ar['content_xml']),'matches':body==ar['content_xml']},
  'source_notes':{'expected':H(s['source_notes_xml']),'actual':H(notes),'matches':s['source_notes_xml']==notes},
  'source_document':{'expected':H(doc),'actual':H(raw),'matches':H(doc)==H(raw)},
  'previous_draft':{'expected':None if not prior else {'source_sha256':prior['source_sha256'],'proposed_sha256':H(prior['proposed_xml'])},'actual':None if not dr else {'source_sha256':dr['source_sha256'],'proposed_sha256':H(dr['proposed_xml'])},'matches':(dr is None if prior is None else dr is not None and dr['source_sha256']==prior['source_sha256'] and dr['proposed_xml']==prior['proposed_xml'])}}
  rows.append({'code_id':key[0],'source_id':key[1],'number':s['number'],'source_url':s.get('source_url'),'read_scope':'source_xml, notes et proposition ou conservation/null, plus avant-image entière si présente','guards':guards,'all_five_guards_match':all(g['matches'] for g in guards.values()),'proposal_sha256':None if a['proposed_xml'] is None else H(a['proposed_xml']),'status':a['status'],'verdict':'conforme_sous_coordination_conjointe' if s['number']=='R133-44' else 'aucun_defaut_concret_releve','finding':findings[s['number']],'measure_id':(a.get('substantive_impact',{}).get('measure_id'))})
db.rollback();db.close()
assert all(r['all_five_guards_match'] for r in rows),[r['number'] for r in rows if not r['all_five_guards_match']]
read_deps=['L133-5-3','L133-5-3-1','L133-5-4','L133-5-5','L133-5-6','L133-5-8','L241-3','L242-1','L242-4-4','R130-2','R133-12-1','R133-14','R242-1','R242-2','R243-6','R243-11','R243-12','R243-13','R243-14','R243-15','R243-19','R243-20','R243-21','R244-1','R244-3','L1221-2','L3123-1','L3123-6']
write(out/'review.json',{'review_type':'independent_full_text_review','packages':packages,'scope':{'assigned_articles':24,'legislative_complement':1,'dependencies_entirely_read':read_deps,'captured_dependencies':45,'all_captured_dependencies_claimed_read':False},'conclusion':'Quatre allègements distincts et une coordination de contrat unique ; dix-neuf articles conservés sans réécriture comptée. Le seul défaut opératoire identifié, l’obligation législative de second avis L133-11, est résolu dans le complément conjoint relu. Aucun autre défaut concret relevé dans ce périmètre.','counting':'L133-11 et R133-44 sont une seule mesure mandataire-double-avis-retrait.','limits':['Revue bornée aux dispositions lues ; aucun arrêt ou texte externe non récupéré prétendu réécrit.','R243-15 et la dispense DSN de R133-14 déjà proposée restent des règles de champ à surveiller en concordance : aucune taxe provisionnelle ne doit naître en absence de données encore légalement dues ; cette revue ne démontre pas de contradiction nouvelle du paquet.','Les conditions d’accès légal aux données, la confidentialité, les obligations autonomes de déclaration et de contrôle restent maintenues ; aucune suppression générale de la DSN.'],'articles':rows})
write(out/'manifest.json',{'files':[{'path':str(p.relative_to(ROOT)),'sha256':H(p.read_bytes())} for p in [out/'review.json',*sum(([x/'source.json',x/'answer.json'] for x in packs),[])]],'all_125_guard_checks_match':True,'canonical_mutation':False})
print('Review complete:',len(rows),'articles;',sum(len(r['guards']) for r in rows),'guards; review SHA',H((out/'review.json').read_bytes()))
