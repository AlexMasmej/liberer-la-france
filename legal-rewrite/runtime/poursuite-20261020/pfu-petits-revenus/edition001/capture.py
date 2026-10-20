from pathlib import Path
import json,hashlib,sqlite3,sys,datetime
P=Path(__file__).resolve().parent;L=P.parents[3];sys.path.insert(0,str(L))
from ingest import source_notes
sha=lambda x:hashlib.sha256(x if isinstance(x,bytes)else(x or'').encode()).hexdigest()
imp=json.loads((L/'runtime/export-source/impots.json').read_text());css=json.loads((L/'runtime/export-source/securite-sociale.json').read_text());index={(x['code_id'],x['number']):x for x in imp+css}
selected=[('LEGITEXT000006069577',n)for n in ['200 A','117 quater','125 A','125 D','154 quinquies']]+[('LEGITEXT000006073189','L136-8')]
depkeys=[('LEGITEXT000006069577',n)for n in ['1417','197','235 ter','125-0 A','158']]+[('LEGITEXT000006073189',n)for n in ['L136-6','L136-7']]
db=sqlite3.connect('file:'+str(L/'corpus.sqlite')+'?mode=ro',uri=True);db.row_factory=sqlite3.Row;db.execute('BEGIN')
def get(key):
 e=index[key];k=e['code_id'],e['source_id'];a=dict(db.execute('SELECT * FROM articles WHERE code_id=? AND id=?',k).fetchone());a['source_id']=a.pop('id');a['source_xml']=a.pop('content_xml');a['source_notes_xml']=source_notes(db,*k);raw=db.execute("SELECT xml,sha256 FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",k).fetchone();doc=raw[0].decode()if isinstance(raw[0],bytes)else raw[0];assert sha(doc)==raw[1]==a['source_sha256'];d=db.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',k).fetchone();old=dict(d)if d else None
 if old:old['proposed_sha256']=sha(old['proposed_xml'])
 a.update(source_document_xml=doc,source_document_sha256=sha(doc),source_body_sha256=sha(a['source_xml']),source_notes_sha256=sha(a['source_notes_xml']),previous_draft=old,current_beforeimage_sha256=sha(old['proposed_xml'])if old else None,proposed_xml=old['proposed_xml']if old else None,proposed_sha256=sha(old['proposed_xml'])if old else sha(''),source_url='https://www.legifrance.gouv.fr/codes/article_lc/'+k[1],benefit_check_required=True,impact_check_required=True);return a
sources=[get(k)for k in selected];deps=[get(k)for k in depkeys];db.rollback();db.close()
(P/'source-all.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2)+'\n');(P/'references.json').write_text(json.dumps(deps,ensure_ascii=False,indent=2)+'\n');policies={}
for n in ['policy-coordinations.json','site-summaries.json']:
 raw=(L/n).read_bytes();(P/n).write_bytes(raw);policies[n]=sha(raw)
raw=(L/'runtime/poursuite-20261020/user-decisions.json').read_bytes();(P/'user-decisions.capture.json').write_bytes(raw)
(P/'capture.json').write_text(json.dumps(dict(captured_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),transaction='mode=ro BEGIN',policy_sha256=policies,user_decisions_capture_sha256=sha(raw)),ensure_ascii=False,indent=2)+'\n')
print([(x['number'],len(x['source_xml']),len(x['proposed_xml']or''))for x in sources+deps])
