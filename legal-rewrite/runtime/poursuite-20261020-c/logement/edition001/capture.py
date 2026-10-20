from pathlib import Path
import sqlite3,json,sys,re,shutil,hashlib
O=Path(__file__).resolve().parent;B=O.parents[3];sys.path.insert(0,str(B));from ingest import source_notes
H=lambda b:hashlib.sha256(b).hexdigest()
def S(n,v):(O/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
inventory=json.loads((B/'runtime/export-source/construction-habitation.json').read_text());d=sqlite3.connect(f'file:{B}/corpus.sqlite?mode=ro',uri=True);d.row_factory=sqlite3.Row;d.execute('BEGIN');sel=[]
for a in inventory:
 if not(re.match(r'^(R365|[LRD]481)',a['number'])or a['number']in['L482-1','L482-2','L482-5']):continue
 k=(a['code_id'],a['source_id']);pr=d.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',k).fetchone()
 if pr:continue
 r=dict(d.execute('SELECT * FROM articles WHERE code_id=? AND id=?',k).fetchone());raw=d.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",k).fetchone()[0];assert r['source_sha256']==a['source_sha256']and r['content_xml']==a['source_xml']
 r['source_id']=r.pop('id');r['source_xml']=r.pop('content_xml');r.update(source_notes_xml=source_notes(d,*k),source_document_xml=raw.decode()if isinstance(raw,bytes)else raw,previous_draft=None,benefit_check_required=True,impact_check_required=True);sel.append(r)
assert len(sel)==48,len(sel);S('source.json',sel)
for n in ['policy-coordinations.json','site-summaries.json']:shutil.copyfile(B/n,O/n)
S('selection.json',{'inventory':'runtime/export-source/construction-habitation.json','inventory_sha256':H((B/'runtime/export-source/construction-habitation.json').read_bytes()),'entries':[{'code_id':s['code_id'],'source_id':s['source_id'],'number':s['number'],'source_sha256':s['source_sha256']}for s in sel],'body_characters':sum(len(s['source_xml'])for s in sel),'mode':'SQLite mode=ro BEGIN ; absence de proposition à capture ; pas de réservation dynamique ; trois CLI Travail actifs selon parent.','policies':{n:H((O/n).read_bytes())for n in ['policy-coordinations.json','site-summaries.json']},'canonical_mutation':False})
d.rollback();d.close();print('CAPTURED',len(sel))
