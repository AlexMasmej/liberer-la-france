"""Read-only capture; refuses partial CLI5 acceptance or unexpected existing drafts. No DB mutation."""
from pathlib import Path
import json,sqlite3,hashlib,sys,datetime,copy
P=Path(__file__).resolve().parent;OLD=P/'edition001';OUT=P/'edition002';L=P.parents[2];sys.path.insert(0,str(L));from ingest import source_notes
sha=lambda v:hashlib.sha256(v if isinstance(v,bytes)else(v or '').encode()).hexdigest()
old=json.loads((OLD/'source.json').read_text());ctx=json.loads((OLD/'context.json').read_text());five={x['source_id']for x in old[:5]};db=sqlite3.connect('file:'+str(L/'corpus.sqlite')+'?mode=ro',uri=True);db.row_factory=sqlite3.Row;db.execute('BEGIN');present={x['source_id']:db.execute('select * from drafts where code_id=? and source_id=?',(x['code_id'],x['source_id'])).fetchone()for x in old};pending=[x['number']for x in old if x['source_id']in five and present[x['source_id']]is None];unexpected=[x['number']for x in old if x['source_id']not in five and present[x['source_id']]is not None]
if pending or unexpected:
 print(json.dumps(dict(captured_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),ready=False,pending_CLI5=pending,unexpected_other_drafts=unexpected)));db.rollback();db.close();sys.exit(0)
assert not OUT.exists(),'Never overwrite an existing002capture'
rows=[];contexts=[];deltas=[]
for group,source,dest in [('candidate',old,rows),('context',ctx,contexts)]:
 for x in source:
  y=copy.deepcopy(x);c,i=x['code_id'],x['source_id'];r=dict(db.execute('select * from articles where code_id=? and id=?',(c,i)).fetchone());d=db.execute('select * from drafts where code_id=? and source_id=?',(c,i)).fetchone();d=dict(d)if d else None
  if d:d['proposed_sha256']=sha(d['proposed_xml'])
  raw=dict(db.execute("select xml,sha256 from documents where code_id=? and id=? and kind='ARTICLE'",(c,i)).fetchone());notes=source_notes(db,c,i);assert r['content_xml']==x['source_xml'];assert sha(raw['xml'])==raw['sha256']==x['source_sha256'];y.update(source_notes_xml=notes,source_body_sha256=sha(r['content_xml']),source_notes_sha256=sha(notes),source_document_xml=raw['xml'].decode()if isinstance(raw['xml'],bytes)else raw['xml'],source_document_sha256=sha(raw['xml']),previous_draft=d)
  if d!=x.get('previous_draft')or notes!=x.get('source_notes_xml'):deltas.append(dict(group=group,number=x['number'],source_id=i,before=x.get('previous_draft'),current=d,notes_changed=notes!=x.get('source_notes_xml')))
  dest.append(y)
db.rollback();db.close();OUT.mkdir();
for n,v in [('source.json',rows),('context.json',contexts),('canonical-beforeimage-deltas.json',deltas)]: (OUT/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
for n in ['policy-coordinations.json','site-summaries.json']:(OUT/n).write_bytes((L/n).read_bytes())
capture=dict(captured_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),mode='ro BEGIN',only_expected_five_existing=True,nineteen_still_absent=True,source_count=len(rows),context_count=len(contexts),current_policies={n:sha((OUT/n).read_bytes())for n in ['policy-coordinations.json','site-summaries.json']},policy_changed_since001={n:sha((OUT/n).read_bytes())!=sha((OLD/n).read_bytes())for n in ['policy-coordinations.json','site-summaries.json']},candidate_body_decisions_pending=True,no_answer_written=True,no_canonical_mutation=True)
(OUT/'capture.json').write_text(json.dumps(capture,ensure_ascii=False,indent=2)+'\n');print(json.dumps(capture))
