from pathlib import Path
import json,sqlite3,hashlib,sys,datetime
P=Path(__file__).resolve().parent;L=P.parents[3];AUTHOR=L/'runtime/poursuite-20261020-b/tsa/edition001';sys.path.insert(0,str(L));from ingest import source_notes;from run_exhaustive import validate_answer
sha=lambda x:hashlib.sha256(x if isinstance(x,bytes)else(x or'').encode()).hexdigest()
s=json.loads((P/'source.capture.json').read_text());a=json.loads((P/'answer.capture.json').read_text());old=json.loads((P/'answer.capture.json').read_text());validate_answer(a,s);assert a==old
records=s+json.loads((P/'reviewed-support.capture.json').read_text())+json.loads((P/'dependencies.capture.json').read_text())+json.loads((P/'additional-targets.json').read_text());assert len({(x['code_id'],x['source_id'])for x in records})==len(records)
db=sqlite3.connect('file:'+str(L/'corpus.sqlite')+'?mode=ro',uri=True);db.row_factory=sqlite3.Row;db.execute('BEGIN');checks=[]
for x in records:
 k=x['code_id'],x['source_id'];v=db.execute('select source_sha256,content_xml from articles where code_id=? and id=?',k).fetchone();raw=db.execute("select xml,sha256 from documents where code_id=? and id=? and kind='ARTICLE'",k).fetchone();d=db.execute('select * from drafts where code_id=? and source_id=?',k).fetchone();before=dict(d)if d else None
 if before:before['proposed_sha256']=sha(before['proposed_xml'])
 tests=dict(source_sha256=v['source_sha256']==x['source_sha256'],body_sha256=sha(v['content_xml'])==x['source_body_sha256'],notes_sha256=sha(source_notes(db,*k))==x['source_notes_sha256'],previous_draft=before==x['previous_draft'],raw_document_sha256=sha(raw['xml'])==raw['sha256']==x['source_sha256']);checks.append(dict(number=x['number'],source_id=x['source_id'],checks=tests))
db.rollback();db.close();frozen={n:sha((AUTHOR/n).read_bytes())==sha((P/(n.replace('.json','.capture.json'))).read_bytes())for n in ['source.json','answer.json','manifest.json','dependencies.json','reviewed-support.json','reference-targets.json']};pol={n:sha((AUTHOR/n).read_bytes())==sha((L/n).read_bytes())for n in ['policy-coordinations.json','site-summaries.json']}
r=dict(checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),read_only='mode=ro BEGIN',schema_valid=True,source_count=len(records),guards=checks,author_freeze=frozen,policies=pol,all_guards_match=all(all(c['checks'].values())for c in checks)and all(frozen.values())and all(pol.values()),independent_legal_validation=False)
(P/'guard-review.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print('RECORDS',len(records),'GUARDS',len(records)*5,'PASS',r['all_guards_match']);print('FAILURES',[x for x in checks if not all(x['checks'].values())]);print('FREEZE',frozen,'POLICY',pol)
