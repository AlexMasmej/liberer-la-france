"""A fresh read-only check; integration must still use review_prior.commit guards."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sqlite3,sys
sys.dont_write_bytecode=True
OUT=Path(__file__).resolve().parent;PROJECT=OUT.parents[1]
sys.path.insert(0,str(PROJECT))
import review_prior as prior
import reference_coherence as refs
import run_exhaustive as runner
from ingest import source_notes
def sha(x):return hashlib.sha256(x.encode() if isinstance(x,str) else x or b'').hexdigest()
capture=json.loads((OUT/'before-images.current.json').read_text())
sources=json.loads((OUT/'original-job/source.json').read_text())
snapshot=json.loads((OUT/'original-job/reference-targets.json').read_text())
paths={r['path'] for r in capture['batch_rows'] if r['path']}
files={p:(PROJECT/p).read_bytes() for p in paths}
owners={}
for p,raw in files.items():
 for row in json.loads(raw):
  k=row['code_id'],row['source_id']
  if k in {(s['code_id'],s['source_id']) for s in sources}:
   assert k not in owners
   owners[k]=row
db=sqlite3.connect((PROJECT/'corpus.sqlite').as_uri()+'?mode=ro',uri=True);db.execute('PRAGMA query_only=ON');db.execute('BEGIN')
results=[]
try:
 refs.check_guards(db,snapshot)
 for s in sources:
  k=s['code_id'],s['source_id'];old=s['previous_draft']
  a=db.execute('SELECT content_xml,source_sha256,number FROM articles WHERE code_id=? AND id=?',k).fetchone()
  d=db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?',k).fetchone()
  actual=prior.batch_row_sha256(owners[k]) if k in owners else None
  checks={'source_and_number_exact':a==(s['source_xml'],s['source_sha256'],s['number']),'notes_exact':source_notes(db,*k)==s['source_notes_xml'],'previous_draft_tuple_exact':d==prior.draft_values(old),'previous_proposal_hash_exact':sha(d[2])==old['proposed_sha256'],'whole_batch_row_hash_exact':actual==old.get('batch_row_sha256')}
  assert all(checks.values()),(s['number'],checks)
  results.append({'number':s['number'],'source_id':s['source_id'],'checks':checks})
finally:db.close()
assert all((PROJECT/p).read_bytes()==raw for p,raw in files.items()),'Batch changed during fresh read'
assert runner.policy_is_current(OUT/'original-job')
fingerprints=json.loads((OUT/'active-code-policy-hashes.json').read_text())
assert all(sha((PROJECT/f['path']).read_bytes())==f['sha256'] for f in fingerprints)
report={'at_utc':datetime.now(timezone.utc).isoformat(),'passed':True,'articles':results,'reference_guards_current':True,'policies_current':True,'active_code_and_policy_hashes_unchanged_since_validation':True,'known_owner_files_stable_during_read':True,'read_only_DB':True,'writer_lock_acquired_for_this_recheck':False,'scope':'Known captured batch owners checked; review_prior.commit must rescan all batch owners under its existing writer lock before integration.','commit_called':False}
(OUT/'fresh-guards.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'passed':True,'articles':len(results),'reference_guards_current':True,'known_owner_files_stable':True,'commit_called':False}))
