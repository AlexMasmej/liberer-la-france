from pathlib import Path
import json,sqlite3,hashlib,sys,datetime,re
P=Path(__file__).resolve().parent;L=P.parents[3];sys.path.insert(0,str(L));from ingest import source_notes
sha=lambda x:hashlib.sha256(x if isinstance(x,bytes)else(x or'').encode()).hexdigest()
css=['L213-1','L752-4','L225-1','L221-1','L646-1','L640-1','L641-1','L652-1','L131-6','L131-6-1','L131-6-2','L136-3','L133-5-5','L133-5-3','L133-5-6','L133-5','L133-7','L241-10','R130-2','R243-6-3','R243-7','R613-2','R613-3','L243-6-1','R142-1','R244-1','L243-7','L641-2','L651-1','L752-1','R131-3'];cgi=['170','175']
exports=json.loads((L/'runtime/export-source/securite-sociale.json').read_text())+json.loads((L/'runtime/export-source/impots.json').read_text());keys={(('LEGITEXT000006073189'if n in css else'LEGITEXT000006069577'),n)for n in css+cgi};db=sqlite3.connect('file:'+str(L/'corpus.sqlite')+'?mode=ro',uri=True);db.row_factory=sqlite3.Row;db.execute('BEGIN');rows=[]
for e in exports:
 if(e['code_id'],e['number'])not in keys:continue
 k=e['code_id'],e['source_id'];a=dict(db.execute('select * from articles where code_id=? and id=?',k).fetchone());a['source_id']=a.pop('id');a['source_xml']=a.pop('content_xml');a['source_notes_xml']=source_notes(db,*k);d=db.execute('select * from drafts where code_id=? and source_id=?',k).fetchone();old=dict(d)if d else None
 if old:old['proposed_sha256']=sha(old['proposed_xml'])
 a.update(previous_draft=old,source_body_sha256=sha(a['source_xml']),source_notes_sha256=sha(a['source_notes_xml']),proposed_xml=old['proposed_xml']if old else None,source_url='https://www.legifrance.gouv.fr/codes/article_lc/'+a['source_id']);rows.append(a)
db.rollback();db.close();(P/'context.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');found={(a['code_id'],a['number'])for a in rows};print('MISSING',keys-found,'COUNT',len(rows),'CHARS',sum(len(a['source_xml'])+len(a['proposed_xml']or'')for a in rows));print([(a['number'],len(a['source_xml']),len(a['proposed_xml']or''))for a in rows])
for a in rows:
 if a['number']in['L243-6-1','R243-6-3','L131-6-1']:
  print(a['number'],'SOURCE',a['source_xml'],'NOTES',a['source_notes_xml'],'CURRENT',a['proposed_xml'])
