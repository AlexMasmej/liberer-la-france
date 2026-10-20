from pathlib import Path
import sqlite3,json,hashlib,sys,xml.etree.ElementTree as E
H=Path(__file__).resolve().parent;B=H.parents[3]
sys.path.insert(0,str(B));from ingest import source_notes
sha=lambda v:hashlib.sha256(v.encode()).hexdigest()
C='LEGITEXT000006073189';public=json.loads((B.parent/'sites/liberer-la-retraite/dist/corpus/securite-sociale.json').read_text())
want={'D133-12-1','D133-13','D133-13-11-1','D133-13-11-2'}|{'D133-13-'+str(i)for i in range(1,21)}
refs={'L133-5-6','L133-5-7','L133-5-8','L133-5-9','L133-5-10','L133-5-11','L133-5-12','L133-8-3','L133-8-6','R243-6'}
c=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);c.row_factory=sqlite3.Row
rows=[];reference=[]
for ex in public:
 if ex['number']not in want|refs:continue
 a=dict(c.execute('SELECT * FROM articles WHERE code_id=? AND id=?',(C,ex['source_id'])).fetchone());a['source_id']=a.pop('id');a['source_xml']=a.pop('content_xml');a['source_notes_xml']=source_notes(c,C,a['source_id']);raw=c.execute('SELECT xml FROM documents WHERE code_id=? AND id=? AND kind="ARTICLE"',(C,a['source_id'])).fetchone()[0];raw=raw.decode()if isinstance(raw,bytes)else raw;a['source_document_xml']=raw;a['source_document_sha256']=sha(raw);assert sha(raw)==a['source_sha256'];a['source_body_sha256']=sha(a['source_xml']);a['source_notes_sha256']=sha(a['source_notes_xml']);a['archive_metadata']=dict(c.execute('SELECT * FROM archives WHERE name=?',(a['archive'],)).fetchone());d=c.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',(C,a['source_id'])).fetchone();a['current_beforeimage']=dict(d)if d else None;a['current_beforeimage_sha256']=sha(d['proposed_xml']or'')if d else None;a['previous_draft']=a['current_beforeimage'];a['source_url']='https://www.legifrance.gouv.fr/codes/article_lc/'+a['source_id'];a['benefit_check_required']=True
 if a['number']in want:
  if d:print('CONCURRENT ALREADY',a['number']);continue
  rows.append(a)
 else:reference.append(a)
c.close()
assert len(rows)==24,(len(rows),[r['number']for r in rows])
for name,value in [('source.json',rows),('expected.json',rows),('references.json',reference)]: (H/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
print('SOURCE',len(rows),'REFERENCES',len(reference));print('\n'.join(r['number']+' '+r['source_id']+' chars='+str(len(r['source_xml']))for r in rows))
