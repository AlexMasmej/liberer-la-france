from pathlib import Path
import json,hashlib,sqlite3,sys,copy
sys.path.insert(0,'legal-rewrite');from run_exhaustive import validate_answer
P=Path(__file__).parent;Q=P.parent/'cvae/editions/002';H=lambda t:hashlib.sha256(t if isinstance(t,bytes) else t.encode()).hexdigest()
s=json.loads((P/'audited-edition002-source.json').read_text());a=json.loads((P/'audited-edition002-answer.json').read_text());old={r['source_id']:r for r in json.loads((P/'audited-answer-edition2.json').read_text())};assert len(a)==37
for f in ['source.json','answer.json','expected.json']:assert (Q/f).read_bytes()==(P/('audited-edition002-'+f)).read_bytes()
for r in a:
 assert H(r['proposed_xml'])==r['proposed_sha256']
 if r['source_id'] in old:assert r['proposed_xml']==old[r['source_id']]['proposed_xml']
validate_answer(a,[r for r in s if r['source_id'] in {t['source_id'] for t in a}])
r=next(r for r in a if r['number']=='214');b=next(x for x in s if x['source_id']==r['source_id']);correct=copy.deepcopy(r)
bad='pour les demandes de plafonnement en fonction de la valeur ajoutée prévu à l’article 1647 B sexies du code général des impôts, y compris les demandes relatives aux anciennes années de contribution économique territoriale présentées par une entreprise dont tous les établissements sont situés dans le ressort territorial d\'un service des impôts des entreprises, ainsi que'
good='pour les demandes de plafonnement en fonction de la valeur ajoutée prévu à l’article 1647 B sexies du code général des impôts présentées par une entreprise dont tous les établissements sont situés dans le ressort territorial d\'un service des impôts des entreprises, y compris celles relatives aux anciennes années de contribution économique territoriale, ainsi que'
assert correct['proposed_xml'].count(bad)==1;correct['proposed_xml']=correct['proposed_xml'].replace(bad,good);correct['proposed_sha256']=H(correct['proposed_xml'])
correct['reason']+=' Correction indépendante du I1°c : la condition territoriale préexistante est placée avant l’incise relative aux anciennes années, afin de viser les demandes futures de CFE comme les anciennes demandes de CET ; le champ de délégation n’est pas étendu par inadvertance.'
correct['review_notes']+=' Revue indépendante de l’édition002 (candidat original SHA256 '+r['proposed_sha256']+') : son incise pouvait rattacher la condition « tous les établissements dans le ressort » aux seules anciennes années de CET. La proposition corrigée conserve explicitement cette condition commune, comme la source et l’avant-image, ainsi que le2° relatif aux services regroupés ; aucune nouvelle restriction territoriale ni limite de montant n’est ajoutée. Source, NOTA et avant-image entière relues.'
correct['benefit_review']['preserved']+=' Le rattachement de la condition territoriale est commun à toutes les demandes, sans limitation de la nouvelle CFE à un plafond de montant.'
validate_answer([correct],[b])
db=sqlite3.connect('file:legal-rewrite/corpus.sqlite?mode=ro',uri=True);db.row_factory=sqlite3.Row;guards=[]
for x in s:
 d=db.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',(x['code_id'],x['source_id'])).fetchone();prior=x['current_beforeimage'];assert (d['proposed_xml'] if d else None)==((prior or {}).get('proposed_xml'))
 assert H(x['source_document_xml'])==x['source_sha256'];assert H(x['source_xml'])==x['source_body_sha256']
 guards.append({'code_id':x['code_id'],'source_id':x['source_id'],'number':x['number'],'previous_draft':None if not prior else {'source_sha256':prior['source_sha256'],'proposed_sha256':H(prior['proposed_xml'])},'current_db_matches':True})
(P/'edition002-current-guards.json').write_text(json.dumps(guards,ensure_ascii=False,indent=2)+'\n')
(P/'answer.json').write_text(json.dumps([correct],ensure_ascii=False,indent=2)+'\n')
source=copy.deepcopy(b);source['audited_candidate_before_correction']=r
(P/'correction-source.json').write_text(json.dumps([source],ensure_ascii=False,indent=2)+'\n')
prior=b['current_beforeimage'];expected=[{'code_id':b['code_id'],'source_id':b['source_id'],'previous_draft':{'source_sha256':prior['source_sha256'],'proposed_sha256':H(prior['proposed_xml'])}}]
(P/'expected.json').write_text(json.dumps(expected,ensure_ascii=False,indent=2)+'\n')
(P/'candidate-guards.json').write_text(json.dumps({'package_answer_sha256':H((Q/'answer.json').read_bytes()),'source_id':r['source_id'],'audited_candidate_proposed_sha256':r['proposed_sha256'],'corrected_proposed_sha256':correct['proposed_sha256'],'db_previous_draft_sha256':H(prior['proposed_xml'])},ensure_ascii=False,indent=2)+'\n')
review={'audited_edition':str(Q),'package_sha256':{f:H((Q/f).read_bytes()) for f in ['source.json','answer.json','expected.json']},'candidate_count':37,'source_count':43,'unchanged_from_edition001':35,'new_candidates_reviewed_entirely':['1679 quinquies','214'],'new_source_notes_reviewed_entirely':['1382-0','1635 quater E','1640 B','1679 quinquies','214'],'cgi39_review_extent':'targeted CET/1679quinquies reference only; no claim of global rereview of long CGI39','verdict':'one_specific_correction_required','finding':{'article':'AnnexeIV214 I1°c','severity':'operative_scope_ambiguity','problem':'Territorial condition moved into historical-demand aside, potentially widening unlimited delegation for futureCFE demands despite stated unchanged scope.','minimal_fix':'Common territorial condition precedes historical aside.','candidate_original_sha256':r['proposed_sha256'],'candidate_corrected_sha256':correct['proposed_sha256']},'1679_quinquies':'No concrete defect: prepayment rules unchanged, futureCFE cap setoff retained, oldCET setoff preserved.','future310HC':'Source and note read: distinct2030 territorial rule refers1647BsexiesA, left intact. Not a futureversion of317septiesE.','full_coordination_complete':False,'pending':'Calendar laws2022-1726art55/2023-1322art79/2025-127art62,1647BsexiesA,LPF,CCI and models remain explicitly open per author limits file.','registered_by_reviewer':False,'published_by_reviewer':False}
(P/'edition002-review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n')
(P/'validation.json').write_text(json.dumps({'stable_edition':'002','candidate_count':37,'validate_answer_original37':'passed','validate_answer_corrected214':'passed','first35_bodies_equal_to_edition001':True,'all43_source_raw_and_body_sha':'passed','all43_db_beforeimages':'match','all37_proposed_sha256':'match','correction_candidates':1,'source_read_scope':'42sources entierement; CGI39 long ciblé sur renvoiCET, pas validation globale.','future310HC':'entirebodyandNOTAread; preserved distinct2030 rule','no_db_batches_active_manifest_or_publication_write':True},ensure_ascii=False,indent=2)+'\n')
print(json.dumps(review,ensure_ascii=False,indent=2))
