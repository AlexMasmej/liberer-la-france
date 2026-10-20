from pathlib import Path
import sqlite3,json,hashlib,sys,re
sys.path.insert(0,'legal-rewrite')
from ingest import source_notes,xml_contents
p=Path(__file__).parent;db=sqlite3.connect('file:legal-rewrite/corpus.sqlite?mode=ro',uri=True);db.row_factory=sqlite3.Row
slugs=['impots','impots-annexe-1','impots-annexe-2','impots-annexe-3','impots-annexe-4'];core={'1586 ter','1586 quater','1586 quinquies','1586 sexies','1586 septies','1586 octies','1586 nonies','1679 septies','1447-0','1647 B sexies'}
rows=[]
for slug in slugs:
 exports=json.loads(Path('sites/liberer-la-retraite/dist/corpus/'+slug+'.json').read_text())
 for ex in exports:
  r=db.execute('SELECT * FROM articles WHERE code_id=? AND id=?',(ex['code_id'],ex['source_id'])).fetchone();body=r['plain_text'].lower()
  if not (('valeur ajoutée des entreprises' in body) or re.search(r'\b1586\s+(?:ter|quater|quinquies|sexies|septies|octies|nonies)\b',body) or '1679 septies' in body or (slug=='impots' and r['number'] in core)):continue
  a=dict(r);a['source_id']=a.pop('id');a['source_xml']=a.pop('content_xml');a['source_notes_xml']=source_notes(db,a['code_id'],a['source_id']);raw=db.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",(a['code_id'],a['source_id'])).fetchone()[0];raw=raw.encode() if isinstance(raw,str) else raw;a['source_document_xml']=raw.decode();a['source_document_sha256']=hashlib.sha256(raw).hexdigest();assert a['source_document_sha256']==a['source_sha256'];a['source_body_sha256']=hashlib.sha256(a['source_xml'].encode()).hexdigest();a['archive_metadata']=dict(db.execute('SELECT * FROM archives WHERE name=?',(a['archive'],)).fetchone());d=db.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',(a['code_id'],a['source_id'])).fetchone();a['current_beforeimage']=dict(d) if d else None;a['current_beforeimage_sha256']=hashlib.sha256((d['proposed_xml'] or '').encode()).hexdigest() if d else None;a['source_url']='https://www.legifrance.gouv.fr/codes/article_lc/'+a['source_id'];a['slug']=slug;a['core']=slug=='impots' and r['number'] in core;rows.append(a)
(p/'expected.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');(p/'core-sources.json').write_text(json.dumps([a for a in rows if a['core']],ensure_ascii=False,indent=2)+'\n');print('current bounded inventory',len(rows),'core',sum(a['core'] for a in rows));print('\n'.join(a['slug']+' '+a['number']+' '+a['source_id']+' chars='+str(len(a['source_xml']))+' prior='+str(len((a['current_beforeimage'] or {}).get('proposed_xml') or '')) for a in rows))
