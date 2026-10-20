from pathlib import Path
import json,hashlib
O=Path(__file__).resolve().parent
B=next(p for p in O.parents if p.name=='legal-rewrite')
P=B/'runtime/poursuite-20261020-d/fiscal/c-context-impact/edition001'
D=B/'runtime/poursuite-20261020-d/fiscal/edition002'
I=B/'runtime/poursuite-20261020-d/fiscal-independent-review/edition002'
H=lambda x:hashlib.sha256(x if isinstance(x,bytes) else (x or '').encode()).hexdigest()
L=lambda p:json.loads(p.read_text())
S=lambda n,x:(O/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
expected={'context_manifest':'3ed98902745b27cfdbefbf830b07fd5db75d59db51fdc25ca2c589a584aad3b7','D_manifest':'fa70b5b8084dc352f29acfcc90504db69c4e297efe3cb6ef5484660540917b2f','D_answer':'af17e8a898e72462e11e87326a503b6d1272c19265ec57646070ed6772edb1cc','D_independent_review':'0df5147717bc42bf2b75b0deffa12e4ccd8244ee05f64725e3fb12f6922938a0'}
for key,file in [('context_manifest',P/'manifest.json'),('D_manifest',D/'manifest.json'),('D_answer',D/'answer.json'),('D_independent_review',I/'review.json')]:assert H(file.read_bytes())==expected[key],key
for n,h in L(P/'manifest.json')['files_sha256'].items():assert H((P/n).read_bytes())==h,n
plan=L(P/'bounded-context-review-plan.json');assert plan['basis']['D_manifest_sha256']==expected['D_manifest']
for n,h in plan['basis']['policy_sha256'].items():assert H((B/n).read_bytes())==h,n
answers={x['code_id']+'|'+x['source_id']:x for x in L(D/'answer.json')}
sources={x['code_id']+'|'+x['source_id']:x for x in L(D/'source.json')}
refs={x['code_id']+'|'+x['source_id']:x for x in L(D/'references.json')}
cs=L(P/'C-direct-sources.json');ds=L(P/'D-relevant-contexts-full.json');impact=L(P/'C-audit-dependency-impact.json')
assert len(cs)==2 and len(ds)==3 and len(impact)==144
approved_targets={}
for x in ds:
 k=x['key'];s=sources[k];a=answers[k]
 assert s['source_xml']==x['official_source_xml'] and s['source_notes_xml']==x['official_source_notes_xml'] and s['source_document_xml']==x['source_document_xml']
 assert H(x['source_document_xml'])==x['source_sha256']
 assert a['proposed_xml']==x['future_proposed_xml'] and H(a['proposed_xml'])==x['future_proposed_sha256']
 assert a['reason']==x['future_reason'] and a['review_notes']==x['future_review_notes']
 assert [q for q in x['guard_before'] if x['guard_before'][q]!=x['guard_future'][q]]==['proposed_sha256']
 assert x['guard_future']['proposed_sha256']==H(a['proposed_xml'])
 approved_targets[k]={'number':x['number'],'before_guard':x['guard_before'],'future_guard':x['guard_future'],'source_document_sha256':H(x['source_document_xml']),'future_proposed_sha256':H(a['proposed_xml'])}
read_C=[]
for x in cs:
 k=x['code_id']+'|'+x['source_id'];r=refs[k]
 for field in ['source_xml','source_notes_xml','source_document_xml','source_sha256','previous_draft']:assert x[field]==r[field],(k,field)
 assert H(x['source_document_xml'])==x['source_sha256']
 read_C.append({'key':k,'number':x['number'],'source_sha256':x['source_sha256'],'source_body_sha256':H(x['source_xml']),'source_notes_sha256':H(x['source_notes_xml']),'proposed_sha256':H(x['previous_draft']['proposed_xml']),'whole_source_notes_proposal_read':True})
for x in impact:
 assert x['current_own_certificate_exact'] and not x['own_certificate_mismatches'] and not x['currently_stale_dependencies']
 changes=x['hypothetical_D_changed_dependency_guards'];assert len(changes)==3 and {y['target_key']for y in changes}==set(approved_targets)
 for y in changes:
  t=approved_targets[y['target_key']]
  assert y['currently_exact'] and y['changed_fields_vs_stored_guard']==['proposed_sha256']
  assert y['before_guard']==y['actual_before_guard']==t['before_guard'] and y['hypothetical_future_guard']==t['future_guard']
proof={'status':'frozen_context_evidence_checks_passed_not_post_registration_DB_check','expected_input_sha256':expected,'bound_files_sha256':{n:H((P/n).read_bytes())for n in ['bounded-context-review-plan.json','C-direct-sources.json','D-relevant-contexts-full.json','C-audit-dependency-impact.json','compatibility-findings.json','input-state.json']},'policy_sha256':plan['basis']['policy_sha256'],'C_five_text_scope':read_C,'D_targets':approved_targets,'mechanical_capture_check':{'audits':144,'guard_replacements':432,'changed_fields':['proposed_sha256'],'all_144_semantically_reread':False,'post_registration_DB_verified':False},'canonical_mutation':False}
S('verification.json',proof)
print('PASS: five whole-text bindings, three exact D002 targets, 144 snapshot dependency records / 432 specified substitutions; no DB access or mutation')
