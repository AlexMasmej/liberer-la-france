from pathlib import Path
import sqlite3,json,hashlib,sys,copy,datetime
P=Path(__file__).resolve().parent;L=P.parents[3];OLD=P.parent/'edition001';sys.path.insert(0,str(L));from ingest import source_notes;import reference_coherence as ref
sha=lambda s:hashlib.sha256(s if isinstance(s,bytes)else(s or'').encode()).hexdigest()
def put(n,v):(P/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
policies={n:(L/n).read_bytes()for n in ['policy-coordinations.json','site-summaries.json']}
for n,b in policies.items():(P/n).write_bytes(b)
oldpolicy=json.loads((OLD/'policy-coordinations.json').read_text());newpolicy=json.loads(policies['policy-coordinations.json']);assert oldpolicy['travail']==newpolicy['travail']
s=json.loads((OLD/'source.capture.json').read_text());a=json.loads((OLD/'answer.capture.json').read_text());oldstates={(x['code_id'],x['source_id']):x for x in json.loads((OLD/'current-snapshot.json').read_text())}
db=sqlite3.connect('file:'+str(L/'corpus.sqlite')+'?mode=ro',uri=True);db.row_factory=sqlite3.Row;db.execute('BEGIN');current=[]
for x,y in zip(s,a):
 c,i=x['code_id'],x['source_id'];r=dict(db.execute('select * from articles where code_id=? and id=?',(c,i)).fetchone());d=dict(db.execute('select * from drafts where code_id=? and source_id=?',(c,i)).fetchone());raw=dict(db.execute("select xml,sha256 from documents where code_id=? and id=? and kind='ARTICLE'",(c,i)).fetchone());notes=source_notes(db,c,i)
 assert r['content_xml']==x['source_xml']and notes==x['source_notes_xml'];assert d['proposed_xml']==y['proposed_xml']and d['status']==y['status'];assert sha(raw['xml'])==raw['sha256']==r['source_sha256']
 z=copy.deepcopy(x);z.update(source_sha256=r['source_sha256'],source_xml=r['content_xml'],source_notes_xml=notes,source_body_sha256=sha(r['content_xml']),source_notes_sha256=sha(notes),source_document_xml=raw['xml'].decode('utf-8') if isinstance(raw['xml'],bytes) else raw['xml'],source_document_sha256=sha(raw['xml']),previous_draft={**d,'proposed_sha256':sha(d['proposed_xml'])},current_beforeimage_sha256=sha(d['proposed_xml']),status=d['status'],proposed_xml=d['proposed_xml'],reason=d['reason'],review_notes=d['review_notes'],reference_recheck_only=True);current.append(z)
snapshot=ref.capture(db,current,a)
# Every final target body/source/note was fully read in independent edition001.
for t in snapshot['targets'].values():
 prior=oldstates[t['code_id'],t['source_id']];assert t['source_xml']==prior['source_xml']and t['source_notes_xml']==prior['source_notes_xml'];assert t['proposed_xml']==(prior['current_draft']or{}).get('proposed_xml')
db.rollback();db.close();assert all((L/n).read_bytes()==b for n,b in policies.items());put('source.json',current);put('reference-targets.json',snapshot);put('answer.before.json',a)
put('capture.json',dict(captured_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),read_only_transaction='mode=ro BEGIN',candidates=12,targets=len(snapshot['targets']),all_bodies_strictly_unchanged=True,all_final_target_bodies_identical_to_whole_texts_read_in_edition001=True,policy_sha256={n:sha(b)for n,b in policies.items()},former_policy_sha256=sha((OLD/'policy-coordinations.json').read_bytes()),travail_policy_identical=True,global_policy_equivalence=False,changed_policy_keys=sorted(k for k in oldpolicy.keys()|newpolicy.keys()if oldpolicy.get(k)!=newpolicy.get(k)),semantic_review_by_jurist=False,other_approvals_rebound=False))
print('CAPTURE',len(current),len(snapshot['targets']),sha(policies['policy-coordinations.json']))
