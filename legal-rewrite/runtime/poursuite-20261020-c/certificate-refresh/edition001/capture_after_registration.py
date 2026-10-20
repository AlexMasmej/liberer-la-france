"""READ ONLY capture. Run only after the parent's explicit registration signal.

No certificates or audits are adopted here. The expected policy JSON must contain
exact SHA256 values approved after phase C policy activation, not today's state.
"""
from pathlib import Path
import argparse,copy,hashlib,json,sqlite3,sys
from datetime import datetime,timezone
H=lambda x:hashlib.sha256(x if isinstance(x,bytes)else(x or'').encode()).hexdigest()
O=Path(__file__).resolve().parent;P=O.parents[1];B=P.parents[1]
def load(p):return json.loads(p.read_text())
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--confirm-phase-c-registered',action='store_true');ap.add_argument('--receipt',type=Path,required=True);ap.add_argument('--expected-policy',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
 if not args.confirm_phase_c_registered:ap.error('Wait for the parent registration signal; capture not authorized yet')
 assert args.receipt.is_file()and load(args.receipt),'Registration receipt required'
 assert not args.output.exists(),'Choose a new isolated output edition'
 sys.path.insert(0,str(B));import reference_coherence as rc
 from ingest import source_notes
 plan=load(O/'plan.json');assert H((B/'reference_coherence.py').read_bytes())==plan['frozen_module_sha256'],'Module changed; new review required'
 expected_policy=load(args.expected_policy);assert expected_policy==rc.policy_state(),'Approved post-activation policy hashes do not match'
 for name,h in plan['selected_frozen_file_sha256'].items():assert H((P/name).read_bytes())==h,('Frozen input changed',name)
 lineage=load(O/'selected-frozen-lineage.json');ss=[];aa=[];before=[]
 d=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);d.row_factory=sqlite3.Row;d.execute('BEGIN')
 try:
  for item in lineage:
   n=item['row_1based']-1;s=copy.deepcopy(load(P/item['source_path'])[n]);a=copy.deepcopy(load(P/item['answer_path'])[n]);assert rc.key(s)==item['target_key']==rc.key(a)
   key=s['code_id'],s['source_id'];actual=d.execute('SELECT source_sha256,content_xml FROM articles WHERE code_id=? AND id=?',key).fetchone();assert tuple(actual)==(s['source_sha256'],s['source_xml']),('Source changed',key)
   assert source_notes(d,*key)==s['source_notes_xml'],('Notes changed',key)
   raw=d.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",key).fetchone()[0];raw=raw.decode()if isinstance(raw,bytes)else raw;assert raw==s['source_document_xml'],('Document changed',key)
   draft=d.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',key).fetchone();assert draft is not None,('Article not registered',key)
   draft=dict(draft);assert(draft['source_sha256'],draft['proposed_xml'])==(a['source_sha256'],a['proposed_xml']),('Registered whole body differs from the counter-read frozen candidate',key)
   before.append({'target_key':rc.key(s),'number':s['number'],'draft':draft});s['previous_draft']=draft;s['current_beforeimage_sha256']=H(draft['proposed_xml']);ss.append(s);aa.append(a)
  snap=rc.capture(d,ss,aa)
  for s,a in zip(ss,aa):
   oldneeded=set(a.get('reference_coherence',{}).get('targets',{}));assert set(snap['requirements'][rc.key(s)])==oldneeded,('Required targets changed; new semantic review required',s['number'])
  changed_keys={x['target_key']for x in plan['changed_targets']};changed_views=[]
  for key,old in plan['old_target_guards'].items():
   new=rc.view(d,key)
   if key in changed_keys:
    target=next(x for x in plan['changed_targets']if x['target_key']==key)
    assert(new['view_sha256'],new['view_kind'])==(target['expected_frozen_view_sha256'],target['expected_frozen_view_kind']),('Changed target differs from whole counter-read text',key)
    for f in ['code_id','source_id','source_sha256','source_xml_sha256','source_notes_sha256']:assert new[f]==old[f],('Target source or notes changed',key,f)
    changed_views.append({'target_key':key,'number':new['number'],'old_guard':old,'actual_post_registration_guard':rc.guard(new)})
   else:assert rc.guard(new)==old,('Unapproved other target change',key)
   snap['targets'][key]=new
  rc.check_guards(d,snap)
  args.output.mkdir(parents=True)
  save(args.output/'source.json',ss);save(args.output/'frozen-answer.json',aa);save(args.output/'beforeimages.json',before);save(args.output/'reference-targets.json',snap)
  candidates=load(O/'four-assessment-candidates.json')
  for v in candidates['assessments']:assert snap['targets'][v['target_key']]['view_sha256']==v['view_sha256']
  candidates.update(status='awaiting_parent_review_of_actual_DB_whole_targets',captured_snapshot_sha256=H((args.output/'reference-targets.json').read_bytes()))
  save(args.output/'assessment-review-template.json',candidates)
  save(args.output/'capture-proof.json',{'captured_at':datetime.now(timezone.utc).isoformat(),'readonly_transaction':True,'registration_receipt_path':str(args.receipt.resolve()),'registration_receipt_sha256':H(args.receipt.read_bytes()),'plan_sha256':H((O/'plan.json').read_bytes()),'expected_policy_approval_sha256':H(args.expected_policy.read_bytes()),'policy_sha256':expected_policy,'articles':len(ss),'existing_certificates':sum(bool(a.get('reference_coherence'))for a in aa),'no_required_certificate':sum(not a.get('reference_coherence')for a in aa),'changed_target_guards':changed_views,'semantic_review_completed_by_capture_script':False,'canonical_mutation':False})
  save(args.output/'manifest.json',{'capture_only':True,'files_sha256':{x.name:H(x.read_bytes())for x in args.output.iterdir()if x.is_file()and x.name!='manifest.json'}})
 finally:d.rollback();d.close()
if __name__=='__main__':main()
