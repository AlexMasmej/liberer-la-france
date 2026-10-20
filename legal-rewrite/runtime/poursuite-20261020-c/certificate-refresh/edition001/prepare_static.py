from pathlib import Path
import json,hashlib,re
O=Path(__file__).resolve().parent;P=O.parents[1];B=P.parents[1]
H=lambda v:hashlib.sha256(v if isinstance(v,bytes)else(v or'').encode()).hexdigest()
L=lambda p:json.loads(p.read_text())
def S(n,v):(O/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
folders=['fiscal/edition001','fiscal/edition001/csi-coordination','social/edition001','travail/edition001','travail-coordination-supplement/edition001','logement/edition001','logement/coherence/edition002','logement/transition/edition001','logement/metadata-crpa/edition001']
selected={};files={};origins={}
for folder in folders:
 q=P/folder
 for sn,an in [('source.json','answer.json'),('companion-source.json','companion-answer.json')]:
  if not(q/an).exists():continue
  ss=L(q/sn);aa=L(q/an);assert len(ss)==len(aa)
  for f in [q/sn,q/an]:files[str(f.relative_to(P))]=H(f.read_bytes())
  for i,(s,a)in enumerate(zip(ss,aa)):
   k=s['code_id']+'|'+s['source_id'];assert k==a['code_id']+'|'+a['source_id'];selected[k]={'source_path':str((q/sn).relative_to(P)),'answer_path':str((q/an).relative_to(P)),'row_1based':i+1,'source':s,'answer':a};origins[k]=folder
inventory=[];changed={};oldguards={}
for f in sorted(P.rglob('reference-targets.json')):
 if O in f.parents:continue
 snap=L(f);rec={'path':str(f.relative_to(P)),'sha256':H(f.read_bytes()),'policy_sha256':snap.get('policy_sha256'),'target_count':len(snap.get('targets',{})),'requirements_count':len(snap.get('requirements',{})),'intrapack_target_changes':[],'role':'independent_review_copy'if'-independent-review/'in str(f.relative_to(P))else'obsolete_documentary_edition'if'coherence/edition001/'in str(f.relative_to(P))else'producer_frozen_capture'}
 for k,v in snap['targets'].items():
  guard={field:v[field]for field in ['code_id','source_id','source_sha256','view_kind','view_sha256','source_xml_sha256','source_notes_sha256']}
  if k in oldguards:assert oldguards[k]==guard,('divergent captures',k)
  oldguards[k]=guard
  if k not in selected:continue
  a=selected[k]['answer'];body=a['proposed_xml'];view=body if body is not None else selected[k]['source']['source_xml'];kind='proposal'if body is not None else'official_source_only'
  if H(view)==v['view_sha256']and kind==v['view_kind']:continue
  changed[k]={'target_key':k,'number':a['number'],'source_id':a['source_id'],'expected_frozen_view_sha256':H(view),'expected_frozen_view_kind':kind,'old_guard':guard,'selected_answer_path':selected[k]['answer_path'],'selected_row_1based':selected[k]['row_1based'],'hypothetical_until_verified_in_post_registration_DB':True}
  rec['intrapack_target_changes'].append({'target_key':k,'number':a['number'],'old_view_sha256':v['view_sha256'],'expected_frozen_view_sha256':H(view),'requirement_referrers':[rk for rk,needs in snap.get('requirements',{}).items()if k in needs]})
 inventory.append(rec)
S('all-reference-targets-inventory.json',inventory)
recerts=[];readset=[]
for k,item in selected.items():
 a=item['answer'];hits=[v for v in a.get('reference_checks',[])if v['target_key']in changed];cert_hits=set(a.get('reference_coherence',{}).get('targets',{}))&set(changed)
 assert cert_hits=={x['target_key']for x in hits},(a['number'],cert_hits,hits)
 if not hits:continue
 text=(P/item['answer_path']).read_text();match=re.search('^    "source_id": "'+a['source_id']+'"',text,re.M);assert match
 recerts.append({'referrer_key':k,'number':a['number'],'source_id':a['source_id'],'answer_path':item['answer_path'],'row_1based':item['row_1based'],'source_id_line_1based':text[:match.start()].count('\n')+1,'frozen_body_sha256':H(a['proposed_xml']),'status':a.get('status'),'required_targets':sorted(a['reference_coherence']['targets']),'old_reference_checks':a['reference_checks'],'changed_assessments':hits,'expected_reference_policy_sha256':a['reference_coherence']['policy_sha256'],'requires_whole_new_target_read_and_parent_approval':True})
 readset.append({'role':'dependent_referrer_read','source':item['source'],'frozen_answer':a})
for k,v in changed.items():readset.append({'role':'expected_intrapack_target_read_not_canonical','source':selected[k]['source'],'frozen_answer':selected[k]['answer']})
S('read-set.json',readset)
S('selected-frozen-lineage.json',[{'target_key':k,'number':v['answer']['number'],'source_id':v['answer']['source_id'],'source_path':v['source_path'],'answer_path':v['answer_path'],'row_1based':v['row_1based'],'source_sha256':v['source']['source_sha256'],'source_xml_sha256':H(v['source']['source_xml']),'source_notes_sha256':H(v['source']['source_notes_xml']),'source_document_sha256':H(v['source']['source_document_xml']),'expected_frozen_proposed_sha256':H(v['answer']['proposed_xml']),'expected_status':v['answer'].get('status')}for k,v in selected.items()])
plan={'scope':'PhaseC statique seulement : quatre certificats sociaux et cinq cibles de snapshots ; aucun état DB après inscription encore lu.','not_registration_or_recertification':True,'selected_frozen_file_sha256':files,'selection_order':folders,'selected_article_count':len(selected),'snapshot_inventory_count':len(inventory),'changed_targets':list(changed.values()),'recertify_rows':recerts,'old_target_guards':oldguards,'frozen_module_sha256':H((B/'reference_coherence.py').read_bytes()),'expected_policy_sha256':recerts[0]['expected_reference_policy_sha256'],'conditions':['Attendre signal explicite du parent et receipt d’enregistrement existant.','Tous les articles sélectionnés doivent être réellement inscrits, sources/notes/XML et corps exactement égaux aux fichiers figés. Aucune substitution depuis un texte prévu seulement.','Quatre analyses dépendantes doivent être actualisées après lecture du vrai corps DB et validation du parent ; les autres évaluations restent textuellement identiques.','Toute autre cible externe modifiée, politique modifiée, source modifiée, nouveau renvoi requis ou corps divergent impose arrêt et nouvelle revue.','Les cinq contextes intrapaquet changés sont capturés ; L5151-6 et R362-2 ne demandent aucun certificat supplémentaire car ils ne figurent dans aucune requirement/reference_checks finale.','Le script produit des avant-images, des vrais snapshots et une checklist de revue seulement ; aucun accept_checks, aucun certificat, aucune écriture SQLite ou registre.']}
assert len(recerts)==4
S('plan.json',plan);print('STATIC',len(selected),len(inventory),len(changed),len(recerts))
