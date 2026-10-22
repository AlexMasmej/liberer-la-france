"""Read-only live capture and an isolated, metadata-only candidate. Never commit."""
from pathlib import Path
from datetime import datetime,timezone
import copy,hashlib,json,sqlite3,sys,shutil,time
sys.dont_write_bytecode=True
OUT=Path(__file__).resolve().parent
PROJECT=OUT.parents[1]
JOB=PROJECT/'runtime/exhaustive/jobs/review-securite-sociale-LEGIARTI000042223830-00001-resume-2uu0letr'
sys.path.insert(0,str(PROJECT))
import run_exhaustive as runner
import review_prior as prior
import substantive_impact as impact
import reference_coherence as references
from ingest import source_notes
from register_batches import writer_lock,validate_batches

def sha(value):
 if isinstance(value,str):value=value.encode()
 return hashlib.sha256(value or b'').hexdigest()
def file_sha(path):return sha(path.read_bytes())
def dump(name,value):
 path=OUT/name;path.parent.mkdir(parents=True,exist_ok=True)
 path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def json_sha(value):return sha(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')))
def capture_call(fun):
 try:return {'passed':True,'result':fun()}
 except Exception as e:return {'passed':False,'error_type':type(e).__name__,'error':str(e)}

OUT.mkdir(parents=True,exist_ok=True)
original_files=json.loads((OUT/'original-job-files.before.json').read_text())
sources=json.loads((OUT/'original-job/source.json').read_text());original=json.loads((OUT/'original-job/answer.json').read_text());ref_snapshot=json.loads((OUT/'original-job/reference-targets.json').read_text());capture=json.loads((OUT/'before-images.current.json').read_text())
assert (JOB/'source.json').read_bytes()==(OUT/'original-job/source.json').read_bytes()
assert (JOB/'answer.json').read_bytes()==(OUT/'original-job/answer.json').read_bytes()
raw=(JOB/'answer.json').read_bytes()
needle=b'"classification": "financing_transfer"'
assert raw.count(needle)==1
patched=raw.replace(needle,b'"classification": "mixed"')
(OUT/'answer.metadata-only.json').write_bytes(patched)
candidate=json.loads(patched)
changes=[]
def diff(a,b,path=''):
 if type(a)!=type(b):changes.append({'path':path,'before':a,'after':b});return
 if isinstance(a,dict):
  assert set(a)==set(b)
  for k in a:diff(a[k],b[k],path+'/'+k)
 elif isinstance(a,list):
  assert len(a)==len(b)
  for i,(x,y) in enumerate(zip(a,b)):diff(x,y,path+'/'+str(i))
 elif a!=b:changes.append({'path':path,'before':a,'after':b})
diff(original,candidate)
assert {x['path'] for x in changes}=={'/2/substantive_impact/classification'}
assert all(x['before']=='financing_transfer' and x['after']=='mixed' for x in changes)
dump('exact-metadata-diff.json',changes)
offset=raw.index(needle);replacement=b'"classification": "mixed"'
assert raw[:offset]==patched[:offset] and raw[offset+len(needle):]==patched[offset+len(replacement):]
dump('file-byte-patch-proof.json',{'offset_zero_based':offset,'before_utf8':needle.decode(),'after_utf8':replacement.decode(),'prefix_byte_exact':True,'suffix_byte_exact':True,'original_bytes':len(raw),'candidate_bytes':len(patched),'only_one_replacement':True})
comparisons=[]
for s,a,b in zip(sources,original,candidate):
 fields={k:{'unchanged':a.get(k)==b.get(k),'before_sha256':sha(json.dumps(a.get(k),ensure_ascii=False,separators=(',',':'))),'after_sha256':sha(json.dumps(b.get(k),ensure_ascii=False,separators=(',',':')))} for k in ('code_id','source_id','number','source_sha256','status','proposed_xml','reason','review_notes','reference_checks','change_type','reform_policy_id','removed_provisions')}
 assert all(v['unchanged'] for v in fields.values())
 assert a['substantive_impact']['effects']==b['substantive_impact']['effects']
 comparisons.append({'number':s['number'],'source_id':s['source_id'],'fields':fields,'previous_draft_preserved':s['previous_draft']==next(x for x in json.loads((OUT/'original-job/source.json').read_text()) if x['source_id']==s['source_id'])['previous_draft'],'current_beforeimage_proposed_sha256':next(x['current_proposed_sha256'] for x in capture['source_rows'] if x['source_id']==s['source_id']),'deferred_answer_proposed_utf8_sha256':sha(a.get('proposed_xml')),'candidate_proposed_utf8_sha256':sha(b.get('proposed_xml')),'source_body_sha256':sha(s['source_xml']),'source_notes_sha256':sha(s['source_notes_xml']),'effects_byte_exact_sha256':json_sha(a['substantive_impact']['effects']),'effects_unchanged':True,'effective_proposed_text_unchanged':(a.get('proposed_xml') or s['source_xml'])==(b.get('proposed_xml') or s['source_xml']),'effective_original_answer_utf8_sha256':sha(a.get('proposed_xml') or s['source_xml']),'effective_candidate_utf8_sha256':sha(b.get('proposed_xml') or s['source_xml']),'effective_utf8_bytes':len((b.get('proposed_xml') or s['source_xml']).encode())})
dump('twelve-article-byte-comparison.json',comparisons)

tests={'baseline_validate_answer':capture_call(lambda:len(runner.validate_answer(copy.deepcopy(original),sources))),'baseline_impacts':[],'candidate_impacts':[]}
for s,a,b in zip(sources,original,candidate):
 tests['baseline_impacts'].append({'number':s['number'],'source_id':s['source_id'],**capture_call(lambda a=a,s=s:bool(impact.validate(a,s,required=True)))})
 tests['candidate_impacts'].append({'number':s['number'],'source_id':s['source_id'],**capture_call(lambda b=b,s=s:bool(impact.validate(b,s,required=True)))})
validated=runner.validate_answer(copy.deepcopy(candidate),sources)
tests['candidate_validate_answer']={'passed':True,'article_count':len(validated),'impact_certificates':sum('substantive_impact_certificate' in x for x in validated)}
tests['candidate_reference_accept_checks']=capture_call(lambda:len(references.accept_checks(validated,sources,ref_snapshot)))
for initial,checked in zip(candidate,validated):
 for field in ('code_id','source_id','number','source_sha256','status','proposed_xml','reason','review_notes','reference_checks','substantive_impact'):
  assert initial.get(field)==checked.get(field), 'Validator changed a protected field: '+field
dump('answer.validated.json',validated)
(OUT/'isolated-batches/candidate').mkdir(parents=True,exist_ok=True)
(OUT/'isolated-batches/candidate/00001.json').write_text(json.dumps(validated,ensure_ascii=False,indent=2)+'\n')
db=sqlite3.connect((PROJECT/'corpus.sqlite').as_uri()+'?mode=ro',uri=True,timeout=30);db.execute('PRAGMA query_only=ON');db.execute('BEGIN')
try:
 tests['candidate_reference_guards_current_after_validation']=capture_call(lambda:references.check_guards(db,ref_snapshot))
 def batch_integrity():
  records,diagnostics,files=validate_batches(db,OUT/'isolated-batches')
  assert len(records)==len(sources) and len(files)==1, 'Isolated batch validator did not inspect all 12 rows'
  return {'article_count':len(records),'diagnostics':diagnostics,'files':files}
 tests['isolated_batch_integrity']=capture_call(batch_integrity)
finally:db.close()
baseline_errors=[x for x in tests['baseline_impacts'] if not x['passed']]
assert len(baseline_errors)==1 and baseline_errors[0]['number']=='L111-2-1'
assert all(x['passed'] for x in tests['candidate_impacts'])
assert candidate[2]['substantive_impact']['effects'][0]['kind']=='financing_transfer'
assert candidate[2]['substantive_impact']['effects'][1]['kind']=='complexity_added'
assert not any(e['kind'].startswith('tax_') for e in candidate[2]['substantive_impact']['effects'])
tests['preserved_benefits']={'mandatory_benefit_review_flags':sum(bool(s['benefit_check_required']) for s in sources),'flags_unchanged':True,'all_12_effective_texts_byte_exact_to_original_answer':all(x['effective_proposed_text_unchanged'] for x in comparisons),'health_I_paragraphs_exact_to_official_source':True,'autonomy_III_paragraphs_exact_to_official_source':True,'no_favourable_rule_changed_by_metadata_patch':True,'semantic_independent_jurist_review':False}
import re
ps=re.findall(r'<p>.*?</p>',sources[2]['source_xml'],re.S);pa=re.findall(r'<p>.*?</p>',candidate[2]['proposed_xml'],re.S)
assert ps[:5]==pa[:5] and ps[-2:]==pa[-2:]
tests['new_burdens']={'L111-2-1':{'classification':'mixed','effects_preserved':['financing_transfer','complexity_added'],'new_account_and_governance_costs_disclosed':True,'tax_cut_claimed':False,'net_cost_quantified':False},'LO111-3-3':{'classification':'mixed','effects_preserved':['obligation_removed','obligation_added'],'identification_and_parliamentary_documents_disclosed':True},'L111-2-3':{'classification':'coordination_only','no_additional_CRPA_gain_counted':True,'organism_adaptation_costs_not_quantified':True}}
tests['all_12_current_source_and_previous_guards_match']=all(all(r[k] for k in ('canonical_body_equals_job_source','canonical_notes_equal_job_source','canonical_source_hash_equals_job_source','current_draft_equals_previous_guard','current_proposed_equals_previous_guard')) for r in capture['source_rows']) and all(r['row_equals_job_previous_guard'] for r in capture['batch_rows'])
tests['job_files_unchanged']=[dict(path=f['path'],unchanged=file_sha(JOB/f['path'])==f['sha256']) for f in original_files]
tests['original_job_intact']=all(x['unchanged'] for x in tests['job_files_unchanged'])
tests['commit_called']=False;tests['register_called']=False;tests['active_code_or_policy_modified']=False;tests['manual_slots_reserved']=False
dump('validation.json',tests)
modules=('substantive_impact.py','run_exhaustive.py','review_prior.py','register_batches.py','reference_coherence.py','ingest.py','policy-coordinations.json','site-summaries.json')
dump('active-code-policy-hashes.json',[dict(path=n,sha256=file_sha(PROJECT/n)) for n in modules])
passed=tests['candidate_reference_accept_checks']['passed'] and tests['isolated_batch_integrity']['passed'] and tests['candidate_reference_guards_current_after_validation']['passed'] and tests['all_12_current_source_and_previous_guards_match'] and capture['live_policy_current'] and tests['original_job_intact']
dump('report.json',{'at_utc':datetime.now(timezone.utc).isoformat(),'status':'metadata_only_candidate_validated_not_integrated' if passed else 'held_additional_guard_or_validation_failure','ready_for_integration_review':passed,'article_count':12,'changed_article_count':1,'changed_leaves':changes,'normative_text_changes':0,'reason_changes':0,'review_notes_changes':0,'effects_changes':0,'classification_rationale':'financing_transfer plus existing complexity_added requires mixed; additions are disclosed, no tax/contribution cut asserted','original_answer_sha256':sha(raw),'candidate_answer_sha256':sha(patched),'validated_answer_sha256':file_sha(OUT/'answer.validated.json'),'before_images':'before-images.current.json','comparisons':'twelve-article-byte-comparison.json','validation':'validation.json','commit_called':False,'live_integration_performed':False,'no_global_net_reduction_claim':True})
print(json.dumps({'status':'candidate_validated' if passed else 'held','baseline_failures':baseline_errors,'candidate_impact_passes':sum(x['passed'] for x in tests['candidate_impacts']),'source_guards':tests['all_12_current_source_and_previous_guards_match'],'references_current':tests['candidate_reference_guards_current_after_validation'],'isolated_integrity':tests['isolated_batch_integrity'],'original_job_intact':tests['original_job_intact'],'commit_called':False},ensure_ascii=False,indent=2))
