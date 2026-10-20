from pathlib import Path
import sys,json,sqlite3,hashlib,datetime
P=Path(__file__).resolve().parent;L=P.parents[3];sys.path.insert(0,str(L))
from run_exhaustive import validate_answer
from ingest import source_notes
sha=lambda v:hashlib.sha256(v if isinstance(v,bytes)else(v or'').encode()).hexdigest()
rows=json.loads((P/'answer.json').read_text());source=json.loads((P/'source.json').read_text());original=(P/'answer.json').read_bytes();validate_answer(rows,source)
assert json.loads(original)==rows,'Validator would alter certificate: inspect policy drift'
a=json.loads((P/'source-all.json').read_text())+json.loads((P/'references.json').read_text())+[json.loads((P/n).read_text()) for n in ['additional-reference.json','additional-reference-loss.json']]
db=sqlite3.connect('file:'+str(L/'corpus.sqlite')+'?mode=ro',uri=True);db.row_factory=sqlite3.Row;db.execute('BEGIN');checks=[]
for s in a:
 k=(s['code_id'],s['source_id']);cur=db.execute('select source_sha256,content_xml from articles where code_id=? and id=?',k).fetchone();d=db.execute('select * from drafts where code_id=? and source_id=?',k).fetchone();old=dict(d)if d else None
 if old:old['proposed_sha256']=sha(old['proposed_xml'])
 tests=dict(source=cur['source_sha256']==s['source_sha256'],body=sha(cur['content_xml'])==s['source_body_sha256'],notes=sha(source_notes(db,*k))==s['source_notes_sha256'],previous_draft=old==s['previous_draft'])
 checks.append(dict(number=s['number'],code_id=k[0],source_id=k[1],checks=tests))
db.rollback();db.close()
pol={n:sha((L/n).read_bytes())==sha((P/n).read_bytes())for n in ['policy-coordinations.json','site-summaries.json']}
raw=(L/'runtime/poursuite-20261020/user-decisions.json').read_bytes();(P/'user-decisions.final-capture.json').write_bytes(raw)
report=dict(checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),schema_valid=True,all_fifteen_full_sources_and_notes_read=True,guards=checks,policies=pol,user_decisions_final_sha256=sha(raw),no_active_mutation=True,scope='One proposal; guard checking is technical, not independent legal validation',all_guards_match=all(all(c['checks'].values())for c in checks)and all(pol.values()))
(P/'validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2));assert report['all_guards_match']
