from pathlib import Path
from datetime import datetime,timezone
import sqlite3,json,hashlib,sys
P=Path(__file__).resolve().parent;B=P.parents[3];sys.path.insert(0,str(B))
from ingest import source_notes
H=lambda v:hashlib.sha256(v if isinstance(v,bytes)else(v or'').encode()).hexdigest()
def save(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
nums=['849','850','853','854','855','856','857','860','862','863','864','865','866','867','868','870','871','873','876','877','886','887','888','889']
canon=json.loads((B/'runtime/export-source/impots.json').read_text());by={x['number']:x for x in canon};d=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);d.row_factory=sqlite3.Row;d.execute('BEGIN');out=[]
for n in nums:
 x=by[n];key=x['code_id'],x['source_id'];a=d.execute('SELECT * FROM articles WHERE code_id=? AND id=?',key).fetchone();raw=d.execute("SELECT xml,sha256,archive FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",key).fetchone();prior=d.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',key).fetchone();assert prior is None,('Already treated',n)
 body=raw['xml'].decode()if isinstance(raw['xml'],bytes)else raw['xml'];assert H(body)==a['source_sha256']==raw['sha256']
 out.append(dict(code_id=key[0],source_id=key[1],number=n,source_xml=a['content_xml'],source_notes_xml=source_notes(d,*key),source_sha256=a['source_sha256'],source_document_xml=body,source_document_sha256=H(body),source_archive=a['archive'],source_url='https://www.legifrance.gouv.fr/codes/article_lc/'+key[1],source_valid_from=a['valid_from'],source_valid_until=a['valid_until'],source_state=a['state'],previous_draft=None))
d.rollback();d.close();save('source.json',out);save('selection.json',dict(captured_at=datetime.now(timezone.utc).isoformat(),canonical_inventory='runtime/export-source/impots.json',canonical_inventory_sha256=H((B/'runtime/export-source/impots.json').read_bytes()),read_transaction='SQLite mode=ro BEGIN',sources=[{k:x[k]for k in ['code_id','source_id','number','source_sha256']}for x in out],source_count=len(out),source_body_characters=sum(len(x['source_xml'])for x in out),policy_final_not_yet_captured=False,canonical_mutation=False))
print(json.dumps(dict(sources=len(out),chars=sum(len(x['source_xml'])for x in out))))
