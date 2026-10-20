from pathlib import Path
import json,sqlite3,hashlib,sys,datetime
P=Path(__file__).resolve().parent;L=P.parents[3];sys.path.insert(0,str(L));from ingest import source_notes
sha=lambda v:hashlib.sha256((v or'').encode()).hexdigest()
num=['L133-5-3','L133-5-4','L213-1','L752-1','L752-4','L151-1','L243-6-4','L243-7','L243-7-1 A','L243-7-2','L243-7-6','L243-7-7','L243-12-1','L244-1','L244-6','L244-8-1','L613-2','R142-1','R155-1','R151-1','R155-4','R244-1','R243-6','R243-6-1','R243-8','R243-8-1','L243-1-2','R243-16','R243-20','R243-21','R243-59','R243-59-2','R243-59-3','R243-59-4','L241-3','R133-12-1','L244-3']
ct=['L5212-2','L5212-5','L8221-1','L8221-3','L8221-5','R1251-26','L1251-49','L1221-2','L1234-1','L1234-9','L1234-3','L1237-1','L1251-52']
db=sqlite3.connect('file:'+str(L/'corpus.sqlite')+'?mode=ro',uri=True);db.row_factory=sqlite3.Row;db.execute('BEGIN');rows=[]
for c,nums in [('LEGITEXT000006073189',num),('LEGITEXT000006072050',ct)]:
 for n in nums:
  ex=json.loads((L/'runtime/export-source'/('securite-sociale.json' if c=='LEGITEXT000006073189' else 'travail.json')).read_text());ident=next(x['source_id']for x in ex if x['number']==n);r=dict(db.execute('select * from articles where code_id=? and id=?',(c,ident)).fetchone());i=r['id'];d=db.execute('select * from drafts where code_id=? and source_id=?',(c,i)).fetchone();draft=dict(d)if d else None
  if draft:draft['proposed_sha256']=sha(draft['proposed_xml'])
  notes=source_notes(db,c,i);rows.append(dict(code_id=c,source_id=i,number=n,source_sha256=r['source_sha256'],source_xml=r['content_xml'],source_body_sha256=sha(r['content_xml']),source_notes_xml=notes,source_notes_sha256=sha(notes),previous_draft=draft))
db.rollback();db.close();(P/'context.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');print('CONTEXT',len(rows),'CHARS',sum(len(x['source_xml'])+len((x['previous_draft']or{}).get('proposed_xml')or'')for x in rows));print([(x['number'],len(x['source_xml']))for x in rows])
