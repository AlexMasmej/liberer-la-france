"""Read-only reassessment; no commit, reservation, guard refresh or active write."""
from pathlib import Path
from datetime import datetime,timezone
import ast,copy,hashlib,json,sqlite3,sys,xml.etree.ElementTree as ET
sys.dont_write_bytecode=True
OUT=Path(__file__).resolve().parent;PROJECT=OUT.parents[1]
OLD=PROJECT/'runtime/css-impact-metadata-review-20261022'
sys.path.insert(0,str(PROJECT))
import run_exhaustive as runner
import review_prior as prior
import reference_coherence as refs
import substantive_impact as impact
from ingest import source_notes
from register_batches import validate_batches

def sha(v):return hashlib.sha256(v.encode() if isinstance(v,str) else v or b'').hexdigest()
def dump(n,v):(OUT/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def read(p):return json.loads(p.read_text())
oldcap=read(OLD/'before-images.current.json');capture=read(OUT/'capture.json');sources=read(OUT/'original-source12.json');candidate=read(OUT/'candidate12.metadata-only.json');snapshot=read(OLD/'original-job/reference-targets.json')
row=next(r for r in capture['articles'] if r['article']['number']=='LO111-4-1');oldref=read(OUT/'old-supplemental-reference.json');key=(oldref['code_id'],oldref['id'])
newrow=row['batch_owner']['row'];current_ref=dict(oldref,current_draft={k:row['draft'][k] for k in ('source_sha256','status','proposed_xml','reason','review_notes')})
assert oldref['content_xml']==row['article']['content_xml'] and oldref['source_sha256']==row['article']['source_sha256']
archive=read(OUT/'revision-archive.json');archived=next(a for a in archive if a['source_id']==key[1]);assert {k:archived[k] for k in oldref['current_draft']}==oldref['current_draft'];assert archived['replacement']==newrow
assert sha(json.dumps(archive,ensure_ascii=False,sort_keys=True))=='8e0e91c296fd1eb82f35847b4ec0e50a738281a078da893eaa8831e833212da0'
# Read/validate the original current job row, including all source notes and benefit flag.
lo_source=next(a for a in read(PROJECT/'runtime/exhaustive/jobs/review-securite-sociale-LEGIARTI000045358043-00003/source.json') if a['source_id']==key[1])
assert lo_source['source_xml']==oldref['content_xml'] and lo_source['source_notes_xml']==oldref['source_notes_xml']
lo_impact=impact.validate(copy.deepcopy(newrow),lo_source,required=True)
assert newrow['status']=='retained_unchanged' and newrow['proposed_xml'] is None and newrow['substantive_impact']['effects']==[]
validated=runner.validate_answer(copy.deepcopy(candidate),sources);refs.accept_checks(validated,sources,snapshot)
assert validated==read(OLD/'answer.validated.json')
assert (OUT/'candidate12.metadata-only.json').read_bytes()==(OLD/'answer.metadata-only.json').read_bytes()
for s,a in zip(sources,validated):impact.validate(a,s,required=True)
isolated=OUT/'fresh-candidate/isolated-batches/candidate';isolated.mkdir(parents=True,exist_ok=True);(isolated/'00001.json').write_text(json.dumps(validated,ensure_ascii=False,indent=2)+'\n')
engine=[]
for f in read(OLD/'active-code-policy-hashes.json'):
 current=sha((PROJECT/f['path']).read_bytes());engine.append(dict(f,current_sha256=current,identical_to_original=current==f['sha256']))
before=PROJECT/'runtime/second-pass-parallelism-20261022T061507Z/before/run_exhaustive.py'
def function_ast(p,n):
 tree=ast.parse(p.read_text());node=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name==n);return ast.dump(node,include_attributes=False)
assert sha(before.read_bytes())==next(f['sha256'] for f in engine if f['path']=='run_exhaustive.py')
assert function_ast(before,'validate_answer')==function_ast(PROJECT/'run_exhaustive.py','validate_answer')
assert all(f['identical_to_original'] for f in engine if f['path']!='run_exhaustive.py')
db=sqlite3.connect((PROJECT/'corpus.sqlite').as_uri()+'?mode=ro',uri=True);db.execute('PRAGMA query_only=ON');db.execute('BEGIN')
checks=[];supplemental=[]
try:
 refs.check_guards(db,snapshot)
 for s in sources:
  k=s['code_id'],s['source_id'];before=s['previous_draft'];d=db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?',k).fetchone();a=db.execute('SELECT content_xml,source_sha256,number FROM articles WHERE code_id=? AND id=?',k).fetchone()
  assert d==prior.draft_values(before) and sha(d[2])==before['proposed_sha256'];assert a==(s['source_xml'],s['source_sha256'],s['number']);assert source_notes(db,*k)==s['source_notes_xml'];checks.append({'number':s['number'],'source_id':s['source_id'],'all_original_source_notes_and_previous_draft_guards_match':True})
 for ref in oldcap['supplemental_references']:
  k=ref['code_id'],ref['id'];a=db.execute('SELECT code_id,id,number,content_xml,source_sha256,valid_from,valid_until FROM articles WHERE code_id=? AND id=?',k).fetchone();expected=tuple(ref[f] for f in ('code_id','id','number','content_xml','source_sha256','valid_from','valid_until'));assert a==expected and source_notes(db,*k)==ref['source_notes_xml']
  d=db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?',k).fetchone();expected_d=(current_ref if k==key else ref)['current_draft'];assert d==tuple(expected_d[f] for f in ('source_sha256','status','proposed_xml','reason','review_notes')) if expected_d else d is None
  supplemental.append({'number':ref['number'],'source_and_notes_unchanged':True,'draft_matches_original_guard':ref['current_draft']==expected_d,'explicitly_reassessed':k==key,'current_guard':(current_ref if k==key else ref)})
 records,diagnostics,files=validate_batches(db,OUT/'fresh-candidate/isolated-batches');assert len(records)==12 and len(files)==1
finally:db.close()
for f in read(OUT/'old-proof-files.before.json'):assert sha(Path(f['path']).read_bytes())==f['sha256']
original_job=PROJECT/'runtime/exhaustive/jobs/review-securite-sociale-LEGIARTI000042223830-00001-resume-2uu0letr'
for f in read(OLD/'original-job-files.before.json'):assert sha((original_job/f['path']).read_bytes())==f['sha256']
fresh=OUT/'fresh-candidate';fresh.mkdir(exist_ok=True)
(fresh/'source.original.json').write_bytes((OLD/'original-job/source.json').read_bytes());(fresh/'answer.metadata-only.json').write_bytes((OLD/'answer.metadata-only.json').read_bytes());(fresh/'answer.validated.json').write_bytes((OLD/'answer.validated.json').read_bytes());(fresh/'reference-targets.original.json').write_bytes((OLD/'original-job/reference-targets.json').read_bytes())
dump('fresh-candidate/supplemental-review-guards.json',{'at_utc':datetime.now(timezone.utc).isoformat(),'origin':'Explicit full LO111-4-1 reassessment; not a refresh of the original evidence','references':supplemental,'all_other_supplemental_guards_preserved':True})
dump('engine-review.json',{'engines':engine,'validate_answer_AST_identical_to_pinned_before_code':True,'new_runner_diff_reviewed':'Imports plus concurrency/admission/phase orchestration only; validate_answer unchanged. This evidence does not waive future active-engine guards.'})
dump('validation.json',{'at_utc':datetime.now(timezone.utc).isoformat(),'passed':True,'LO111-4-1_impact_validated':True,'LO111-4-1_retained_source_entire':True,'LO111-4-1_archived_old_tuple_exact':True,'LO111-4-1_archive_replacement_equals_current_batch':True,'all12_answers_and_impacts_validated':True,'all12_validated_answers_identical_to_original_validated_candidate':True,'all12_original_live_guards':checks,'original_reference_snapshot_current':True,'all6_supplemental_references_checked':True,'only_supplemental_draft_change':'LO111-4-1','isolated_batches':{'rows':len(records),'files':len(files),'diagnostics':diagnostics},'old_proof_files_and_28_original_job_files_unchanged':True,'no_live_integration':True,'no_slot_reserved':True,'commit_called':False,'reserve_resolved':False})
print(json.dumps({'passed':True,'candidate_articles':12,'original12_guards_match':True,'only_changed_supplemental':'LO111-4-1','fresh_candidate_isolated':str(fresh),'commit_called':False,'reserve_resolved':False}))
