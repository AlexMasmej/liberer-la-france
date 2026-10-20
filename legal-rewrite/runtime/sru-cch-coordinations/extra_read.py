import json,sqlite3,hashlib,sys,pathlib
sys.path.insert(0,'legal-rewrite');from ingest import source_notes
P=pathlib.Path(__file__).parent
rows=json.loads((P/'source.json').read_text()); seen={a['number'] for a in rows}
c=sqlite3.connect('file:legal-rewrite/corpus.sqlite?mode=ro',uri=True);c.row_factory=sqlite3.Row
pub=json.load(open('sites/liberer-la-retraite/dist/corpus/construction-habitation.json'))
for n in ['L302-1','L302-3','L302-4-1','R631-20','R631-21','R823-2','R863-4','L443-15-2','L443-15-2-1']:
 if n in seen: continue
 a=dict(next(a for a in pub if a['number']==n));raw=c.execute('select * from articles where code_id=? and id=?',(a['code_id'],a['source_id'])).fetchone()
 a['source_xml']=raw['content_xml']; a['source_sha256']=raw['source_sha256'];a['source_content_sha256']=hashlib.sha256(a['source_xml'].encode()).hexdigest();a['source_notes_xml']=source_notes(c,a['code_id'],a['source_id'])
 d=c.execute('select * from drafts where code_id=? and source_id=?',(a['code_id'],a['source_id'])).fetchone()
 if d:
  a['previous_draft']={k:d[k] for k in ['source_sha256','status','proposed_xml','reason','review_notes']};a['previous_draft']['proposed_sha256']=hashlib.sha256((d['proposed_xml'] or '').encode()).hexdigest()
 else:a['previous_draft']=None
 rows.append(a)
(P/'source.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
for n in ['L302-1','L302-3','L302-4-1','R631-20','R631-21','R823-2','R863-4','L443-15-2','L443-15-2-1']:
 a=next(a for a in rows if a['number']==n);print(n,len(a['source_xml']),len((a.get('previous_draft') or {}).get('proposed_xml','')))
