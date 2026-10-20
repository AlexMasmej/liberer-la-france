from pathlib import Path
import sqlite3,json,hashlib,sys,shutil,datetime,re
O=Path(__file__).resolve().parent;B=next(p for p in O.parents if p.name=='legal-rewrite');sys.path.insert(0,str(B));from ingest import source_notes
H=lambda x:hashlib.sha256(x if isinstance(x,bytes)else x.encode()).hexdigest()
S=lambda n,x:(O/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
inv=json.loads((B/'runtime/export-source/construction-habitation.json').read_text());wanted={*[f'{p}634-{i}'for p in ['L','R']for i in range(1,6)],'L635-1',*[f'L635-{i}'for i in range(3,11)],*[f'R635-{i}'for i in range(1,6)]};assert len(wanted)==24
D=sqlite3.connect(f'file:{B}/corpus.sqlite?mode=ro',uri=True);D.row_factory=sqlite3.Row;D.execute('BEGIN')
def read(x):
 k=x['code_id'],x['source_id'];r=dict(D.execute('SELECT * FROM articles WHERE code_id=? AND id=?',k).fetchone());assert r['content_xml']==x['source_xml']and r['source_sha256']==x['source_sha256'];raw=D.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",k).fetchone()[0];raw=raw.decode()if isinstance(raw,bytes)else raw;assert H(raw)==r['source_sha256'];pr=D.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',k).fetchone();r['source_id']=r.pop('id');r['source_xml']=r.pop('content_xml');r.update(source_notes_xml=source_notes(D,*k),source_document_xml=raw,previous_draft=dict(pr)if pr else None,benefit_check_required=True,impact_check_required=True);return r
ss=[read(x)for x in inv if x['number']in wanted];assert len(ss)==24 and all(x['previous_draft']is None for x in ss)
S('source.json',ss)
refs=[read(x)for x in inv if x['number']in ['L635-2','L635-11','L351-2','L511-1','L511-2','L511-3','L521-1','L521-2','L521-3-1','L521-3-2']];S('references.json',refs)
for n in ['policy-coordinations.json','site-summaries.json']:shutil.copyfile(B/n,O/n)
S('selection.json',{'captured_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'mode':'SQLite mode=ro BEGIN','inventory':'runtime/export-source/construction-habitation.json','inventory_sha256':H((B/'runtime/export-source/construction-habitation.json').read_bytes()),'entries':[{'code_id':s['code_id'],'source_id':s['source_id'],'number':s['number'],'source_sha256':s['source_sha256'],'prior_proposal_absent':True}for s in ss],'body_characters':sum(len(s['source_xml'])for s in ss),'no_dynamic_reservation':True,'active_jobs_check':'parent coordination + current job captures checked separately; absence rechecked before delivery and under parent writer lock before integration','policy_sha256':{n:H((O/n).read_bytes())for n in ['policy-coordinations.json','site-summaries.json']},'canonical_mutation':False})
D.rollback();D.close();print('CAPTURE',len(ss),'REFERENCES',len(refs))
