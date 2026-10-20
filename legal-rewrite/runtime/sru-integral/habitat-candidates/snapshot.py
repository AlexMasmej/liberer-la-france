import sqlite3,json,pathlib,hashlib,sys
sys.path.insert(0,'legal-rewrite');from ingest import source_notes
P=pathlib.Path(__file__).parent;pub=json.load(open('sites/liberer-la-retraite/dist/corpus/construction-habitation.json'));c=sqlite3.connect('file:legal-rewrite/corpus.sqlite?mode=ro',uri=True);c.row_factory=sqlite3.Row;rows=[]
for n in ['L423-13','L411-7','L453-2','R421-10']:
 a=dict(next(a for a in pub if a['number']==n));key=a['code_id'],a['source_id'];s=c.execute('select * from articles where code_id=? and id=?',key).fetchone();a['source_xml']=s['content_xml'];a['source_sha256']=s['source_sha256'];a['source_notes_xml']=source_notes(c,*key)
 d=c.execute('select * from drafts where code_id=? and source_id=?',key).fetchone();a['previous_draft']=dict(d) if d else None
 if d:a['previous_draft']['proposed_sha256']=hashlib.sha256((d['proposed_xml'] or '').encode()).hexdigest()
 rows.append(a)
(P/'sources.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
for a in rows:print('\nARTICLE',a['number'],'SOURCE',a['source_xml'],'NOTES',a['source_notes_xml'],'PREVIOUS',json.dumps(a['previous_draft'],ensure_ascii=False))
