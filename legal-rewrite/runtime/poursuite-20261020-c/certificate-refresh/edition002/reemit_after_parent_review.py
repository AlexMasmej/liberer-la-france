"""Stage reference metadata only; never write SQLite or adopt any certificate."""
from pathlib import Path
import argparse,copy,hashlib,json,sqlite3,sys
H=lambda x:hashlib.sha256(x if isinstance(x,bytes)else(x or'').encode()).hexdigest()
O=Path(__file__).resolve().parent;P=O.parents[1];B=P.parents[1]
def load(p):return json.loads(p.read_text())
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--captured',type=Path,required=True);ap.add_argument('--reviewed-assessments',type=Path,required=True);ap.add_argument('--confirm-parent-review',action='store_true');ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
 if not args.confirm_parent_review:ap.error('Parent whole-target review required; no certificate re-emission yet')
 assert not args.output.exists(),'Choose a new isolated edition'
 sys.path.insert(0,str(B));import reference_coherence as rc
 from run_exhaustive import validate_answer
 from ingest import source_notes
 plan=load(O/'plan.json');assert H((B/'reference_coherence.py').read_bytes())==plan['frozen_module_sha256']
 cap=args.captured;manifest=load(cap/'manifest.json')
 for n,h in manifest['files_sha256'].items():assert H((cap/n).read_bytes())==h,('Capture changed',n)
 proof=load(cap/'capture-proof.json');assert proof['plan_sha256']==H((O/'plan.json').read_bytes())
 ss=load(cap/'source.json');old=load(cap/'frozen-answer.json');aa=copy.deepcopy(old);snap=load(cap/'reference-targets.json');review=load(args.reviewed_assessments)
 assert review['status']=='approved_by_parent_after_whole_actual_DB_target_read','Four analyses are not approved'
 assert review['captured_snapshot_sha256']==H((cap/'reference-targets.json').read_bytes())
 expected={(r['referrer_key'],v['target_key'])for r in plan['recertify_rows']for v in r['changed_assessments']};updates={}
 for v in review['assessments']:
  pair=v['referrer_key'],v['target_key'];assert pair in expected and pair not in updates
  assert v['view_sha256']==snap['targets'][v['target_key']]['view_sha256'];assert isinstance(v['assessment'],str)and len(v['assessment'].strip())>=80;updates[pair]=v
 assert set(updates)==expected
 d=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);d.row_factory=sqlite3.Row;d.execute('BEGIN')
 try:
  rc.check_guards(d,snap);assert rc.policy_state()==proof['policy_sha256']
  for s,entry in zip(ss,load(cap/'beforeimages.json')):
   key=s['code_id'],s['source_id'];row=d.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',key).fetchone();assert row is not None and dict(row)==entry['draft'],('Before-image changed after capture',key)
   r=d.execute('SELECT source_sha256,content_xml FROM articles WHERE code_id=? AND id=?',key).fetchone();assert tuple(r)==(s['source_sha256'],s['source_xml'])and source_notes(d,*key)==s['source_notes_xml']
   raw=d.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",key).fetchone()[0];raw=raw.decode()if isinstance(raw,bytes)else raw;assert raw==s['source_document_xml']
  diffs=[]
  for a,b in zip(aa,old):
   key=rc.key(a);a.pop('reference_coherence',None)
   for item in a.get('reference_checks',[]):
    pair=key,item['target_key']
    if pair in updates:
     v=updates[pair];diffs.append({'referrer_key':key,'number':a['number'],'target_key':item['target_key'],'old_assessment':copy.deepcopy(item),'new_assessment':{k:v[k]for k in ['target_key','view_sha256','assessment']}});item.update({k:v[k]for k in ['view_sha256','assessment']})
    else:assert item['view_sha256']==snap['targets'][item['target_key']]['view_sha256'],('Unreviewed assessment would need rebinding',pair)
  rc.accept_checks(aa,ss,snap);validate_answer(copy.deepcopy(aa),copy.deepcopy(ss))
  for s,a,b in zip(ss,aa,old):
   assert a['proposed_xml']==b['proposed_xml'];assert {k:v for k,v in a.items()if k not in['reference_coherence','reference_checks']}=={k:v for k,v in b.items()if k not in['reference_coherence','reference_checks']}
   assert rc.certificate_current(d,s,a['proposed_xml'],a.get('reference_coherence'))
  assert len(diffs)==4 and sum(bool(a.get('reference_coherence'))for a in aa)==36
  args.output.mkdir(parents=True);save(args.output/'source.json',ss);save(args.output/'answer.json',aa);save(args.output/'reference-targets.json',snap);save(args.output/'assessment-diff.json',diffs)
  save(args.output/'refresh-proof.json',{'plan_sha256':H((O/'plan.json').read_bytes()),'capture_manifest_path':str((cap/'manifest.json').resolve()),'capture_manifest_sha256':H((cap/'manifest.json').read_bytes()),'capture_proof_path':str((cap/'capture-proof.json').resolve()),'capture_proof_sha256':H((cap/'capture-proof.json').read_bytes()),'registration_receipt_path':proof['registration_receipt_path'],'registration_receipt_sha256':proof['registration_receipt_sha256'],'approved_assessments_path':str(args.reviewed_assessments.resolve()),'approved_assessments_sha256':H(args.reviewed_assessments.read_bytes()),'source_sha256':H((args.output/'source.json').read_bytes()),'answer_sha256':H((args.output/'answer.json').read_bytes()),'articles':144,'all_normative_bodies_byte_identical':True,'all_other_answer_fields_unchanged':True,'reference_certificates_reemitted':36,'articles_without_required_certificate':108,'assessments_changed':4,'policy_sha256':proof['policy_sha256'],'beforeimages_path':str((cap/'beforeimages.json').resolve()),'beforeimages_sha256':H((cap/'beforeimages.json').read_bytes()),'semantic_review_by_script':False,'canonical_mutation':False,'no_publication':True})
  save(args.output/'manifest.json',{'frozen':True,'metadata_staging_only':True,'source_pairs':[['source.json','answer.json']],'files_sha256':{x.name:H(x.read_bytes())for x in args.output.iterdir()if x.is_file()and x.name!='manifest.json'}})
 finally:d.rollback();d.close()
if __name__=='__main__':main()
