import json,sqlite3,hashlib,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT));from ingest import source_notes
out=ROOT/'runtime/poursuite-20261020/fiscal-1684/edition001';out.mkdir(parents=True,exist_ok=True)
def H(x):return hashlib.sha256(x if isinstance(x,bytes) else (x or '').encode()).hexdigest()
db=sqlite3.connect('file:'+str(ROOT/'corpus.sqlite')+'?mode=ro',uri=True);db.row_factory=sqlite3.Row;db.execute('BEGIN')
ids=['LEGIARTI000033812284','LEGIARTI000038584307','LEGIARTI000033812095','LEGIARTI000033780786'];rows=[]
for ident in ids:
 code='LEGITEXT000006069577';a=dict(db.execute('select * from articles where code_id=? and id=?',(code,ident)).fetchone());raw=db.execute("select xml from documents where code_id=? and id=? and kind='ARTICLE'",(code,ident)).fetchone()[0];notes=source_notes(db,code,ident);d=db.execute('select * from drafts where code_id=? and source_id=?',(code,ident)).fetchone();d=dict(d) if d else None
 if d:d['proposed_sha256']=H(d['proposed_xml'])
 body=a.pop('content_xml');a['source_id']=a.pop('id');a.update(source_xml=body,source_body_sha256=H(body),source_notes_xml=notes,source_notes_sha256=H(notes),source_document_xml=raw.decode() if isinstance(raw,bytes) else raw,source_document_sha256=H(raw),previous_draft=d,benefit_check_required=True,impact_check_required=True,source_url='https://www.legifrance.gouv.fr/codes/article_lc/'+ident);rows.append(a)
db.rollback();db.close()
for name,val in [('source.json',rows[:1]),('dependencies.json',rows[1:])]: (out/name).write_text(json.dumps(val,ensure_ascii=False,indent=2)+'\n')
for name in ['policy-coordinations.json','site-summaries.json']:(out/name).write_bytes((ROOT/name).read_bytes())
print('captured',[(x['number'],bool(x['previous_draft'])) for x in rows])
