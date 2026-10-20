from pathlib import Path
import json,sqlite3,hashlib,sys,datetime
P=Path(__file__).resolve().parent;L=P.parents[3];sys.path.insert(0,str(L))
from ingest import source_notes
sha=lambda x:hashlib.sha256(x if isinstance(x,bytes) else (x or '').encode()).hexdigest()
numbers='L242-1-3 L242-1-4 L242-3 L242-8 L242-9 L242-10 L242-14 R133-13 R133-14-1 R133-14-2 R133-14-3 R133-14-4 R133-14-5 R133-14-6 R133-15 R133-16 R133-43 R133-44 R242-3 R242-4 D242-2-2 R243-27 R243-28 R243-29'.split()
export=json.loads((L/'runtime/export-source/securite-sociale.json').read_text());scope={x['number']:x for x in export}
# Required norms of this precise DSN, ceiling and third-party-payment circuit, captured as whole articles.
deps='L133-5-3 L133-5-3-1 L133-5-4 L133-5-5 L133-5-6 L133-5-8 L241-3 L242-1 L242-4-4 R130-2 R133-12-1 R133-14 R242-1 R242-2 R243-6 R243-11 R243-12 R243-13 R243-14 R243-15 R243-19 R243-20 R243-21 R244-1 R244-3'.split()
ctscope={x['number']:x for x in json.loads((L/'runtime/export-source/travail.json').read_text())}
ctdeps='L1221-2 L1234-1 L1234-3 L1234-5 L1234-9 L1221-25 L1237-1 L3123-1 L3123-6 L3123-7 L3123-27 L1251-1 L1251-18 L1251-32 L1251-58-1 L1251-58-2 L1251-58-3 L1251-58-4 L1251-58-5 L1251-58-6'.split()
db=sqlite3.connect('file:'+str(L/'corpus.sqlite')+'?mode=ro',uri=True);db.row_factory=sqlite3.Row;db.execute('BEGIN')
def get(e,fresh=False):
 key=e['code_id'],e['source_id'];a=dict(db.execute('SELECT * FROM articles WHERE code_id=? AND id=?',key).fetchone());a['source_id']=a.pop('id');a['source_xml']=a.pop('content_xml');a['source_notes_xml']=source_notes(db,*key);a['source_body_sha256']=sha(a['source_xml']);a['source_notes_sha256']=sha(a['source_notes_xml']);raw=db.execute("SELECT xml,sha256 FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",key).fetchone();doc=raw[0].decode()if isinstance(raw[0],bytes)else raw[0];assert sha(doc)==a['source_sha256']==raw[1];a.update(source_document_xml=doc,source_document_sha256=sha(doc));draft=db.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',key).fetchone();a['previous_draft']=dict(draft)if draft else None;a['proposed_xml']=draft['proposed_xml']if draft else None;a['proposed_sha256']=sha(a['proposed_xml']);a['current_beforeimage_sha256']=a['proposed_sha256']if draft else None;a.update(slug='securite-sociale'if key[0]=='LEGITEXT000006073189'else'travail',source_url='https://www.legifrance.gouv.fr/codes/article_lc/'+key[1],path=e['path'],benefit_check_required=True,impact_check_required=True)
 if fresh:assert draft is None,a['number']
 return a
sources=[get(scope[n],True)for n in numbers];targets=[get(scope[n])for n in deps]+[get(ctscope[n])for n in ctdeps];db.rollback();db.close()
(P/'source.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2)+'\n');(P/'dependencies.json').write_text(json.dumps(targets,ensure_ascii=False,indent=2)+'\n')
policies={}
for name in ['policy-coordinations.json','site-summaries.json']:
 raw=(L/name).read_bytes();(P/name).write_bytes(raw);policies[name]=sha(raw)
(P/'capture.json').write_text(json.dumps(dict(captured_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),current_export_only=True,current_export_source_count=len(export),selected_count=len(sources),selected_source_notes_chars=sum(len(x['source_xml'])+len(x['source_notes_xml'])for x in sources),policies=policies,sqlite_transaction='mode=ro BEGIN',sources_sha256=sha((P/'source.json').read_bytes()),dependencies_sha256=sha((P/'dependencies.json').read_bytes())),ensure_ascii=False,indent=2)+'\n')
print([(x['number'],len(x['source_xml']),len(x['proposed_xml']or''))for x in targets])
