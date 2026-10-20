from pathlib import Path
import json,sqlite3,sys,re
O=Path(__file__).resolve().parent;B=O.parents[3];sys.path.insert(0,str(B));from ingest import source_notes
d=sqlite3.connect(f'file:{B}/corpus.sqlite?mode=ro',uri=True);d.row_factory=sqlite3.Row;d.execute('BEGIN');inv=json.loads((B/'runtime/export-source/construction-habitation.json').read_text());sel={s['source_id']for s in json.loads((O/'source.json').read_text())};wanted=['L365-1','L365-2','L365-3','L365-4','L365-5','L365-7','L481-2','L481-6','L481-8','L423-1-1','L423-1-2','L342-2','L342-12','L452-1','L452-2-1','R362-2','L482-3','L482-3-1','L482-4','D423-1-1','D423-1-2','D423-1-3','D442-3-1','D442-3-2','L442-7','L353-9-2','R441-31','R442-3-3','L621-2'];a=[]
for n in wanted:
 if n in ['D442-3-1','D442-3-2']:n='R'+n[1:]
 s=next(x for x in inv if re.sub(r'[*. ]','',x['number'])==n);k=(s['code_id'],s['source_id']);r=dict(d.execute('SELECT * FROM articles WHERE code_id=? AND id=?',k).fetchone());raw=d.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",k).fetchone()[0];pr=d.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',k).fetchone();r['source_id']=r.pop('id');r['source_xml']=r.pop('content_xml');r.update(source_notes_xml=source_notes(d,*k),source_document_xml=raw.decode()if isinstance(raw,bytes)else raw,previous_draft=dict(pr)if pr else None);a.append(r)
(O/'references.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n');print('REFERENCES',[(x['number'],len(x['source_xml']),len((x['previous_draft']or{}).get('proposed_xml')or''))for x in a]);d.rollback();d.close()
