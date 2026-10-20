from pathlib import Path
import sqlite3,json,hashlib,sys
H=Path(__file__).resolve().parent;B=H.parents[3];sys.path.insert(0,str(B));from ingest import source_notes
c=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);c.row_factory=sqlite3.Row
want={'securite-sociale':{'R133-14','R243-16','R323-10','R441-4','L341-4','L541-1'},'travail':{'D1272-1','R1221-13','L1221-11','R3243-1','L3141-24','L3141-22','L1271-1','R1271-8'}};out=[]
for slug,nums in want.items():
 p=B.parent/'sites/liberer-la-retraite/dist/corpus'/ (slug+'.json')
 pub=json.loads(p.read_text())
 for ex in pub:
  if ex['number']not in nums:continue
  a=dict(c.execute('select * from articles where code_id=? and id=?',(ex['code_id'],ex['source_id'])).fetchone());a['source_id']=a.pop('id');a['source_xml']=a.pop('content_xml');a['source_notes_xml']=source_notes(c,a['code_id'],a['source_id']);raw=c.execute('select xml from documents where code_id=? and id=? and kind="ARTICLE"',(a['code_id'],a['source_id'])).fetchone()[0];a['source_document_xml']=raw.decode()if isinstance(raw,bytes)else raw;d=c.execute('select * from drafts where code_id=? and source_id=?',(a['code_id'],a['source_id'])).fetchone();a['previous_draft']=dict(d)if d else None;out.append(a)
c.close();(H/'direct-links.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print('\n'.join(r['number']+' '+r['source_id']+' len='+str(len(r['source_xml']))for r in out))
