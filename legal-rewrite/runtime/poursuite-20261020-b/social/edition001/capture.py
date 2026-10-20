from pathlib import Path
import json,sqlite3,hashlib,sys,datetime
P=Path(__file__).resolve().parent;L=P.parents[3];sys.path.insert(0,str(L));from ingest import source_notes
sha=lambda x:hashlib.sha256(x if isinstance(x,bytes)else(x or'').encode()).hexdigest()
numbers=['L611-1','L613-2','L613-3','L613-4','R611-1','R611-2','R611-3','R613-1-1','R613-1-2','R613-1-3','R613-1-5','R613-5','R613-8','R613-9','R613-10','R613-12','R613-13','R613-17','R613-18','R613-19','R131-3-1','R131-9','L243-1-2']
export=json.loads((L/'runtime/export-source/securite-sociale.json').read_text());wanted=[a for a in export if a['number']in numbers];db=sqlite3.connect('file:'+str(L/'corpus.sqlite')+'?mode=ro',uri=True);db.row_factory=sqlite3.Row;db.execute('BEGIN');rows=[]
for e in wanted:
 k=e['code_id'],e['source_id'];a=dict(db.execute('select * from articles where code_id=? and id=?',k).fetchone());a['source_id']=a.pop('id');a['source_xml']=a.pop('content_xml');a['source_notes_xml']=source_notes(db,*k);d=db.execute('select * from drafts where code_id=? and source_id=?',k).fetchone();assert d is None,k
 doc=db.execute("select xml,sha256 from documents where code_id=? and id=? and kind='ARTICLE'",k).fetchone();raw=doc['xml'].decode()if isinstance(doc['xml'],bytes)else doc['xml'];assert sha(raw)==doc['sha256']==a['source_sha256']
 a.update(previous_draft=None,source_body_sha256=sha(a['source_xml']),source_notes_sha256=sha(a['source_notes_xml']),source_document_xml=raw,source_document_sha256=sha(raw),source_url='https://www.legifrance.gouv.fr/codes/article_lc/'+a['source_id'],benefit_check_required=True,impact_check_required=True);rows.append(a)
db.rollback();db.close();(P/'source-candidates.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');guards={}
for n in ['policy-coordinations.json','site-summaries.json']:
 raw=(L/n).read_bytes();(P/n).write_bytes(raw);guards[n]=sha(raw)
(P/'capture.json').write_text(json.dumps(dict(captured_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),transaction='mode=ro BEGIN',scope='Only current export-source/securite-sociale.json versions; no prior draft',policy_sha256=guards),ensure_ascii=False,indent=2)+'\n')
print([(a['number'],a['source_id'],len(a['source_xml']))for a in rows]);print('total',sum(len(a['source_xml'])for a in rows))
