from pathlib import Path
import sqlite3,json,hashlib,sys,copy,collections,datetime
O=Path(__file__).resolve().parent;B=O.parents[3];sys.path.insert(0,str(B))
from ingest import source_notes
from run_exhaustive import validate_answer
import reference_coherence as ref
H=lambda v:hashlib.sha256(v if isinstance(v,bytes)else v.encode()).hexdigest()
L=lambda n:json.loads((O/n).read_text())
def S(n,v):
 p=O/n;p.parent.mkdir(exist_ok=True,parents=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
d=sqlite3.connect(f'file:{B}/corpus.sqlite?mode=ro',uri=True);d.row_factory=sqlite3.Row;d.execute('BEGIN')
pairs=[('source.json','answer.json'),('companion-source.json','companion-answer.json'),('papier/source.json','papier/answer.json')]
all_s=[];all_a=[];source_checks=[]
for sn,an in pairs:
 ss,aa=L(sn),L(an);validate_answer(copy.deepcopy(aa),copy.deepcopy(ss));all_s+=ss;all_a+=aa
for s in all_s:
 key=(s['code_id'],s['source_id']);ar=d.execute('SELECT source_sha256,content_xml FROM articles WHERE code_id=? AND id=?',key).fetchone();raw=d.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",key).fetchone()[0];raw=raw.decode()if isinstance(raw,bytes)else raw
 assert ar[0]==s['source_sha256'] and ar[1]==s['source_xml']
 assert raw==s['source_document_xml'] and source_notes(d,*key)==s['source_notes_xml']
 assert d.execute('SELECT 1 FROM drafts WHERE code_id=? AND source_id=?',key).fetchone()is None
 source_checks.append({'code_id':key[0],'source_id':key[1],'number':s['number'],'source_sha256':s['source_sha256'],'source_xml_sha256':H(s['source_xml']),'source_notes_sha256':H(s['source_notes_xml']),'source_document_sha256':H(raw),'prior_proposal_sha256':None,'absence_of_proposal':True})
refs={}
for fn in ['references.json','additional-references.json','precaire-references.json','forms-references.json','copies-references.json']:
 for x in L(fn):
  key=(x['code_id'],x['source_id']);ar=d.execute('SELECT source_sha256,content_xml FROM articles WHERE code_id=? AND id=?',key).fetchone();pr=d.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',key).fetchone();pr=dict(pr)if pr else None
  assert ar[0]==x['source_sha256']and ar[1]==x['source_xml']and source_notes(d,*key)==x['source_notes_xml']and pr==x['previous_draft'],(fn,x['number'])
  refs['|'.join(key)]=ref.view(d,'|'.join(key))
for x in L('papier/electronic-reference.json'):
 refs[x['code_id']+'|'+x['id']]=ref.view(d,x['code_id']+'|'+x['id'])
snapshot=ref.capture(d,all_s,all_a)
snapshot['targets'].update(refs);ref.check_guards(d,snapshot)
for fn in ['policy-coordinations.json','site-summaries.json']:assert H((O/fn).read_bytes())==H((B/fn).read_bytes()),fn
S('reference-targets.json',snapshot);S('source-guards.json',source_checks)
required=sum(bool(v)for v in snapshot['requirements'].values())
assess={
 'L1234-1':'Source et proposition entières lues : préavis de rupture du contrat de travail unique pour les contrats nouveaux, anciens préavis réservés aux contrats antérieurs. Il ne règle ni le terme du permis précaire, ni une division foncière ; aucun préavis salarié ou de logement n’est modifié dans ce lot.',
 'L1221-2':'Source et proposition entières lues : nouveaux contrats de travail uniques sans terme automatique, missions et formations distinctes de la durée d’emploi. Aucun permis précaire ni division de terrain du présent lot n’est un contrat de travail ; aucune ancienne durée d’emploi n’est rétablie.',
 'L1234-9':'Source, note2017 et proposition entières lues : indemnité ordinaire du salarié distincte du droit public de remise en état ou du droit de délaissement. Le présent lot ne touche ni seuil d’un an, ni0,20mois par ancienneté totale, ni plafond6mois, ni prorata des mois complets, ni anciens droits.',
 'L313-6':'Source et proposition entières lues : travaux de restauration, évacuation seulement si nécessaire, réservesL313-7/loi1948 et préavis du bailleur de sixmois maintenus. La suppression du terme automatique hors zoneR433-1 ne supprime ni ces protections de relogement/évacuation ni la condition du secteur protégé b.',
 'L433-3':'Source, notes et proposition entières lues : enlèvement à la date fixée, ou première demande seulement pour emplacement réservé/DUP ; remise en état aux frais du bénéficiaire sous réserveL433-4. R433-1 supprime une fixation obligatoire hors zone, sans transformer b en faculté générale de démolition sur simple demande.',
 'L433-4':'Source, notes et proposition entières lues : indemnité proportionnelle au temps restant lorsque la puissance publique fait remettre en état avant le terme fixé. R433-1 conserve expressément cette garantie et ne retire pas les termes ou indemnités des permis déjà délivrés.',
 'L230-1':'Source et proposition entières lues : droit de délaissement, mairie, personnes à mentionner et publicité pour autres intéressés, délai de deuxmois propre au foncier. R442-1 est conservé intégralement avec ses divisions exemptées : aucun préavis de travail ni délai de délaissement n’est appliqué ou supprimé par homonymie.',
 'L230-3':'Source et proposition entières lues : décision publique sous un an, paiement amiable sous deuxans, saisine et prix du juge, références foncières, indemnités, emprise totale et substitution publique encadrée. Conservation intégraleR442-1 : aucune de ces protections foncières n’est modifiée ni comptée comme allègement nouveau.'}
for a in all_a:
 needed=snapshot['requirements'].get(ref.key(a),[])
 if needed:a['reference_checks']=[{'target_key':k,'view_sha256':snapshot['targets'][k]['view_sha256'],'assessment':assess[snapshot['targets'][k]['number']]}for k in needed]
ref.accept_checks(all_a,all_s,snapshot)
for sn,an in pairs:
 ids={ref.key(s)for s in L(sn)};S(an,[a for a in all_a if ref.key(a)in ids])
counts=collections.Counter(a['substantive_impact']['classification']for a in all_a)
new_ids=['urbanisme-date-naissance-declarant-supprimee','urbanisme-inventaire-generique-autorisations-supprime','declaration-construction-supports-graphiques-fusionnes','amenagement-notice-et-plans-support-commun','declaration-amenagement-croquis-distinct-supprime','permis-precaire-terme-hors-zone-non-automatique','lotissement-accord-lotisseur-forme-libre','urbanisme-depot-papier-exemplaire-unique']
by_source={(s['code_id'],s['source_id']):s for s in all_s}
article_audit=[]
for a in all_a:
 s=by_source[(a['code_id'],a['source_id'])];impact=a['substantive_impact']
 article_audit.append({'code_id':a['code_id'],'source_id':a['source_id'],'number':a['number'],'source_sha256':a['source_sha256'],'source_xml_sha256':H(s['source_xml']),'notes_sha256':H(s['source_notes_xml']),'proposed_xml_sha256':H(a['proposed_xml'])if a['proposed_xml']else None,'status':a['status'],'classification':impact['classification'],'before_after_evidence':impact['effects'],'obligations_removed_or_merged':a.get('removed_provisions',[]),'new_or_transferred_burdens':impact['new_burdens_review'],'benefits':a['benefit_review'],'whole_source_and_notes_read':True,'whole_previous_draft_read':s['previous_draft']is not None,'review_notes':a['review_notes']})
audit={'scope':'24 nouvelles entrées Urbanisme du seul inventaire public30317, deux compagnons indispensables et sous-lot papier de quatre articles. Audit borné ; aucune conclusion sur l’ensemble du code.','method':'Sources et notes canoniques entières en lecture seule ; avant-images des cibles entières ; garde finale SQLite mode=ro BEGIN. Aucun projet sur les30entrées au contrôle final. Les sources hors corpus restent documentaires et ne sont pas des propositions intégrées.','classification_counts':dict(counts),'articles_total':30,'whole_proposals':sum(bool(a['proposed_xml'])for a in all_a),'retained_null':sum(a['proposed_xml']is None for a in all_a),'distinct_new_measure_ids':new_ids,'distinct_new_measures':8,'measure_count_limit':'Huit dispositifs, pas huit procédures abolies : deux champs, des supports distincts, une condition de terme obligatoire, une alternative de preuve et les copies papier. Les données utiles transférées vers un support commun restent dues. Les articles de coordination et avantages déjà existants ne sont pas de nouvelles coupes.','existing_measures_not_recounted':['permis-dossier-commun-autorisations-integrees','permis-reemploi-conventions-publiees','permis-lettre-completude-defrichement','permis-statistiques-annexe-supprimee','residences-demontables-attestation-supprimee'],'budget':'Aucun gain fiscal, budgétaire national, coût net ou délai global gagné chiffré. La reproduction administrative éventuellement nécessaire au dépôt papier unique est une charge transférée à coût public inconnu.','CRPA_filter':'L113-12 interdit déjà la redemande des données détenues ou légalement échangeables. R441-5 et le simple réemploi ne comptent pas comme nouveaux gains ; les champs/supports/copies explicitement supprimés dès le premier dépôt sont distincts.','electronic_filter':'R474-1 I 2° dispense déjà les usagers électroniques des exemplaires supplémentaires. Aucun gain papier n’est attribué à ces usagers, ni aux cas déjà dédupliqués par L425-1.','whole_procedures_abolished':0,'outside_five_codes':['Mise à jour matérielle des modèles et téléprocédures/CERFA par les arrêtés compétents : non accomplie ni publiée dans ce lot. R434-1/R434-2 coordonnent leur habilitation et R423-2 empêche une exigence réglementaire de copies contraires.','Code des transports L6352-1 et R6352-1 à6 : sources DILA entières récupérées ; autorisation, accords aviation/défense et prescriptions de sécurité maintenus, aucune réécriture hors lot.','Code environnement R331-19 et régimes Natura2000/évaluation/participation : pièces utiles et garanties conservées, pas de nouvelle fusion du parc revendiquée.','CRPA et systèmes légaux d’échange : références de droit existant, aucun nouveau traitement de données prétendu autorisé.','L341-7 forestier et le dossier commun L425-1 ont leur propre réforme/transition antérieure ; aucune nouvelle autorisation forestière ou seconde fusion IGH/ERP.'],'important_guarantees':['L433-2 exige encore un terme en secteur protégé : R433-1 b conservé entier ; seule localisation hors zone retirée du a. Indemnités, prolongations et anciens permis préservés.','R442-21 a reste exempt sans accord nouveau ; b conserve nombre de lots, quatre voies de division et accord exprès, attestation simple toujours admise.','Neuf exemptions R442-1, dispense R442-2, exceptions toitures/énergie R441-8-4, salubrité/pollution R441-8-3 et parc R441-8-1 conservés intacts.','R431-36 garde les documents c/d R431-10 en secteurs protégés, avec dispense source de photographie lointaine impossible ; fusion limitée aux autres projets visibles.','Aucun quota SRU ni perte d’exemption littorale/TASCOM. Aucun délai historique de note n’est transformé en date de réforme future.'],'articles':article_audit,'canonical_mutation':False,'juridical_validation_claimed':False}
S('audit.json',audit)
S('validation.json',{'validated_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'validate_answer':{'main24':True,'companions2':True,'paper4':True},'source_document_body_notes_exact':30,'absence_of_proposal_guards':30,'reference_guards':len(snapshot['targets']),'policy_guard':snapshot['policy_sha256'],'reference_check_guards':True,'automatic_reference_assessments_required_for_articles':required,'automatic_reference_note':'Deux articles fonciers déclenchent la détection contractuelle par préavis/indemnité. Huit cibles entières ont été lues et leurs champs distingués, sans prétendre une nouvelle coordination du travail.','classification_counts':dict(counts),'canonical_mutation':False,'concurrency_limit':'Aucune réservation dynamique par article. Absence de proposition vérifiée dans le snapshot final ; root doit revérifier les gardes avant inscription. Trois lots CLI Travail observés à la sélection, sans intersection, et aucun nouveau coordinateur promis pendant la rédaction.'})
d.rollback();d.close()
files={str(p.relative_to(O)):H(p.read_bytes())for p in sorted(O.rglob('*'))if p.is_file()and p.name not in ['manifest.json']}
S('manifest.json',{'edition':'001','frozen':True,'files_sha256':files,'source_pairs':pairs,'new_articles':30,'whole_proposals':24,'retained_unchanged':6,'canonical_mutation':False})
print(json.dumps({'classification_counts':dict(counts),'hashes':{n:H((O/n).read_bytes())for n in ['source.json','answer.json','companion-source.json','companion-answer.json','papier/source.json','papier/answer.json','audit.json','manifest.json']},'refs':len(snapshot['targets'])},ensure_ascii=False,indent=2))
