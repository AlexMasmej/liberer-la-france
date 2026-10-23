from pathlib import Path
import sys,json,sqlite3,hashlib,datetime,ast
sys.dont_write_bytecode=True
P=Path.cwd();sys.path.insert(0,str(P))
import review_prior as prior,reference_coherence as refs,run_exhaustive as runner
from ingest import source_notes
O=P/'runtime/registration-convoy-20261022T1607Z/recovery-preflight';C=P/'runtime/cch-template-diagnostic-20261022T100424Z';S=P/'runtime/css-impact-metadata-review-20261022';R=P/'runtime/css-LO111-4-1-reassessment-20261022T065745Z'
def read(p):return json.loads(p.read_text())
def sha(x):return hashlib.sha256(x.encode() if isinstance(x,str) else x or b'').hexdigest()
def attempt(fn):
 try:return {'passed':True,'result':fn()}
 except Exception as e:return {'passed':False,'error':str(e)}
def asthash(p,name):return sha(ast.dump(next(n for n in ast.parse(p.read_text()).body if isinstance(n,ast.FunctionDef) and n.name==name),include_attributes=False))
db=sqlite3.connect((P/'corpus.sqlite').as_uri()+'?mode=ro',uri=True,timeout=3);db.execute('PRAGMA query_only=ON');db.execute('BEGIN')
report={'at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Read-only targeted queries; no owner corpus scan, locks, code edits, commits or source/policy changes. Not legal validation.'}
def check(s,a):
 k=s['code_id'],s['source_id'];d=db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?',k).fetchone();art=db.execute('SELECT content_xml,source_sha256,number FROM articles WHERE code_id=? AND id=?',k).fetchone();old=s.get('previous_draft')
 return {'number':s['number'],'source_id':s['source_id'],'source_exact':art==(s['source_xml'],s['source_sha256'],s['number']),'notes_exact':source_notes(db,*k)==s.get('source_notes_xml',''),'draft_present':d is not None,'current_status':d[1] if d else None,'current_proposal_sha256':sha(d[2]) if d else None,'beforeimage_exact':d==prior.draft_values(old) if old else d is None,'candidate_db_tuple_exact':d==prior.draft_values(a),'candidate_proposal_exact':d is not None and d[2]==a['proposed_xml']}
report['cch']=[]
for e in sorted((C/'evidence').iterdir()):
 sources=read(e/'source.json');answer=read(e/'answer.json');report['cch'].append({'job':e.name,'articles':[check(s,a) for s,a in zip(sources,answer)],'reference_guards':attempt(lambda:refs.check_guards(db,read(e/'reference-targets.json'))),'active_validate_answer':attempt(lambda:len(runner.validate_answer(answer,sources)))})
sources=read(S/'original-job/source.json');answers=read(S/'answer.validated.json');report['css']={'articles':[check(s,a) for s,a in zip(sources,answers)],'original_reference_guards':attempt(lambda:refs.check_guards(db,read(S/'original-job/reference-targets.json'))),'active_validate_answer':attempt(lambda:len(runner.validate_answer(answers,sources))),'original_policy_current':runner.policy_is_current(S/'original-job')}
cap=read(S/'before-images.current.json');fresh={r['current_guard']['id']:r['current_guard'] for r in read(R/'fresh-candidate/supplemental-review-guards.json')['references']}
report['css']['supplemental']=[]
for ref in cap['supplemental_references']:
 k=ref['code_id'],ref['id'];d=db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?',k).fetchone();a=db.execute('SELECT content_xml,source_sha256 FROM articles WHERE code_id=? AND id=?',k).fetchone()
 def vals(x):return tuple(x[f] for f in ('source_sha256','status','proposed_xml','reason','review_notes')) if x else None
 report['css']['supplemental'].append({'number':ref['number'],'source_exact':a==(ref['content_xml'],ref['source_sha256']),'notes_exact':source_notes(db,*k)==ref['source_notes_xml'],'original_draft_exact':d==vals(ref['current_draft']),'reassessed_draft_exact':d==vals(fresh[ref['id']]['current_draft'])})
db.close()
report['cch_code_guards']=[dict(f,current_sha256=sha((P/f['path']).read_bytes()) if (P/f['path']).exists() else None) for f in read(C/'integration/deployment-manifest.proposed.json')['files']]
report['css_code_guards']=[dict(f,current_sha256=sha((P/f['path']).read_bytes())) for f in read(S/'active-code-policy-hashes.json')]
report['css_runner_validate_ast_matches_reassessment_baseline']=asthash(P/'run_exhaustive.py','validate_answer')==asthash(P/'runtime/second-pass-parallelism-20261022T061507Z/before/run_exhaustive.py','validate_answer')
report['css_known_owner_checks']=[]
for old in cap['batch_rows']:
 if not old.get('path'):continue
 rows=read(P/old['path']);report['css_known_owner_checks'].append({'path':old['path'],'capture_fields':list(old),'matches':[{'source_id':s['source_id'],'beforeimage_row_exact':prior.batch_row_sha256(r)==s['previous_draft'].get('batch_row_sha256'),'candidate_row_exact':r==answers[i],'classification':r.get('substantive_impact',{}).get('classification')} for i,s in enumerate(sources) for r in rows if (r['code_id'],r['source_id'])==(s['code_id'],s['source_id'])]})
(O/'checks.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n');print(json.dumps(report,indent=2,ensure_ascii=False))
