from pathlib import Path
import json,hashlib,sqlite3,sys,copy,re,xml.etree.ElementTree as ET
B=Path('legal-rewrite').resolve(); sys.path.insert(0,str(B))
from ingest import source_notes
from run_exhaustive import validate_answer
import reference_coherence as ref
P=B/'runtime/poursuite-20261020/microsocial/edition002';O=B/'runtime/poursuite-20261020/microsocial-independent-review/edition002'
h=lambda b:hashlib.sha256(b if isinstance(b,bytes) else b.encode()).hexdigest()
load=lambda p:json.loads(p.read_text())
def save(n,x):(O/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
m=load(P/'manifest.json');files=[]
for n,sha in m['files'].items():
 raw=(P/n).read_bytes();assert h(raw)==sha,(n,'frozen hash changed');(O/n).write_bytes(raw);files.append({'path':n,'sha256':sha})
(O/'author-manifest.json').write_bytes((P/'manifest.json').read_bytes())
rows={}
for f in ['source.json','capture.json','additional-dependencies.json','territory-scope-dependencies.json','tax-scope-dependencies.json','historical-support.json']:
 for r in load(P/f):
  k=(r['code_id'],r['source_id'])
  if k not in rows:rows[k]=r
checks=[]
db=sqlite3.connect(f'file:{B}/corpus.sqlite?mode=ro',uri=True);db.row_factory=sqlite3.Row;db.execute('BEGIN')
for (code,sid),r in rows.items():
 a=db.execute('SELECT * FROM articles WHERE code_id=? AND id=?',(code,sid)).fetchone();d=db.execute("SELECT xml,sha256 FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",(code,sid)).fetchone();prior=db.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',(code,sid)).fetchone()
 raw=d['xml'];raw=raw.decode() if isinstance(raw,bytes) else raw
 tests={'source_sha':a['source_sha256']==r['source_sha256'],'source_body':a['content_xml']==r['source_xml'],'source_notes':source_notes(db,code,sid)==r['source_notes_xml'],'source_document':raw==r['source_document_xml']}
 if 'previous_draft' in r:
  prev=r['previous_draft'];current=dict(prior) if prior else None
  tests['prior_proposal']=((prev is None and current is None)or(prev is not None and current is not None and all(current.get(k)==v for k,v in prev.items() if k!='proposed_sha256')))
 checks.append({'code_id':code,'source_id':sid,'number':r['number'],'guards':tests,'all_match':all(tests.values())})
policies={n:{'expected':m['files'][n],'actual':h((B/n).read_bytes())} for n in ['policy-coordinations.json','site-summaries.json']}
referror=None
try:ref.check_guards(db,load(P/'reference-targets.json'))
except Exception as e:referror=str(e)
ans=load(P/'answer.json');expected=load(P/'source.json');valerror=None
try:validate_answer(copy.deepcopy(ans),copy.deepcopy(expected))
except Exception as e:valerror=str(e)
def tables(s):
 root=ET.fromstring('<r>'+s+'</r>')
 return [[[(' '.join(''.join(c.itertext()).split()),c.get('colspan'),c.get('rowspan')) for c in tr if c.tag in ('th','td')] for tr in t.iter('tr')] for t in root.iter('table')]
a={r['number']:r for r in ans};s={r['number']:r for r in expected}
t6s=tables(s['D613-6']['source_xml']);t6a=tables(a['D613-6']['proposed_xml']);assert t6s==t6a and len(t6a)==4
sums=[sum(float(row[-1][0].replace('%','').replace(',','.')) for row in t[1:]) for t in t6a]
t4s=tables(s['D613-4']['source_xml']);t4a=tables(a['D613-4']['proposed_xml']);diffs=[]
for ti,(before,after) in enumerate(zip(t4s,t4a)):
 for ri,(br,ar) in enumerate(zip(before,after)):
  for ci,(bc,ac) in enumerate(zip(br,ar)):
   if bc!=ac:diffs.append({'table':ti,'row':ri,'column':ci,'before':bc,'after':ac})
assert len(diffs)==3 and all(d['column']==4 and d['after'][0]=='20 %' for d in diffs)
save('fresh-guards.json',{'snapshot_mode':'mode=ro BEGIN','checks':checks,'source_count':len(rows),'all_match':all(c['all_match'] for c in checks),'policies':policies,'reference_guard_error':referror,'structure_error':valerror,'table_checks':{'D613-6_four_unchanged_tables':t6s==t6a,'D613-6_sums':sums,'D613-4_changes':diffs},'canonical_mutation':False})
save('reviewed-files.json',files)
print(json.dumps({'sources':len(rows),'all_match':all(c['all_match'] for c in checks),'reference_guard_error':referror,'structure_error':valerror,'table_sums':sums,'policy_match':all(v['expected']==v['actual'] for v in policies.values())}))
db.rollback();db.close()
