"""Keep prior audit history; adopt only exact registered independent readings."""
from pathlib import Path
from datetime import datetime, timezone
import ast, hashlib, json, sqlite3, sys

P=Path(__file__).resolve().parent;B=P.parents[1];A=P.parent/'poursuite-20261020'
sys.path.insert(0,str(B))
from ingest import source_notes
from substantive_impact import validate,certificate,digest
from register_batches import writer_lock
from run_exhaustive import atomic
import reference_coherence as rc

def load(p):return json.loads(p.read_text())
tree=ast.parse((A/'adopt-reviewed.py').read_text())
prior_packages=next(ast.literal_eval(n.value) for n in tree.body
 if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='packages' for t in n.targets))
packages=[(A/name,A/evidence,reviewer)for name,evidence,reviewer in prior_packages]
specs=[
 ('tsa/edition002','source.json','answer.json','tsa-independent-review/edition002/review.json'),
 ('social/edition002','source.json','answer.json','social-independent-review/edition002/review-002.json'),
 ('dpae/edition001','source.json','answer.json','dpae-independent-review/edition001/audit.json'),
 ('urbanisme/edition001','source.json','answer.json','urbanisme/edition001/root-independent-review.json'),
 ('urbanisme/edition001','companion-source.json','companion-answer.json','urbanisme/edition001/root-independent-review.json'),
 ('urbanisme/edition001/papier','source.json','answer.json','urbanisme/edition001/root-independent-review.json'),
 ('crpa-classification/edition001','source.json','answer.json','crpa-classification-independent-review/edition001/review.json'),
]
integrated=load(P/'integration/edition001/registration.json')
assert integrated['registered_articles']==96
lineage=load(P/'integration/edition001/preflight.json')['packages']
for item,(name,sn,an,evidence)in zip(lineage,specs):
 assert item['package']==name
 for fn,field in [(sn,'source_sha256'),(an,'answer_sha256')]:
  assert hashlib.sha256((P/name/fn).read_bytes()).hexdigest()==item[field]
 assert (P/evidence).exists()
extra=P/'cli-independent-review/edition002'
if (extra/'registration.json').exists():
 assert load(extra/'registration.json')['registered_articles']==12
 ss={rc.key(s):s for s in load(extra/'source.json')}
 for row in load(extra/'answer.json'):
  assert row['proposed_xml']==ss[rc.key(row)]['previous_draft']['proposed_xml']
 specs.append(('cli-independent-review/edition002','source.json','answer.json','cli-independent-review/edition001/review.json'))
pup=P/'crpa-pup-classification/edition001'
if (pup/'registration.json').exists():
 assert load(pup/'registration.json')['registered_articles']==1
 ss={rc.key(s):s for s in load(pup/'source.json')}
 for row in load(pup/'answer.json'):
  assert row['proposed_xml']==ss[rc.key(row)]['previous_draft']['proposed_xml']
 specs.append(('crpa-pup-classification/edition001','source.json','answer.json','crpa-pup-classification/edition001/review.json'))
reviewed={}
for folder,evidence,reviewer in packages:
 assert (folder/'registration.json').exists() and evidence.exists()
 sources={rc.key(s):s for s in load(folder/'source.json')}
 for row in load(folder/'answer.json'):
  reviewed[rc.key(row)]=(sources[rc.key(row)],row,folder,evidence,reviewer)
for name,sn,an,evidence in specs:
 sources={rc.key(s):s for s in load(P/name/sn)}
 for row in load(P/name/an):
  reviewed[rc.key(row)]=(sources[rc.key(row)],row,P/name,P/evidence,
   'Contrelecture intégrale IA distincte de l’auteur ; delta corrigé relu le cas échéant')

db=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);db.execute('BEGIN')
current={};skipped=[]
for k,entry in reviewed.items():
 source,row,folder,evidence,reviewer=entry;key=row['code_id'],row['source_id']
 state=db.execute('SELECT source_sha256,status,proposed_xml FROM drafts WHERE code_id=? AND source_id=?',key).fetchone()
 if state!=(row['source_sha256'],row['status'],row['proposed_xml']):
  skipped.append(dict(source_id=key[1],reason='Whole proposal superseded; prior certificate not rebound'));continue
 assert db.execute('SELECT source_sha256,content_xml FROM articles WHERE code_id=? AND id=?',key).fetchone()==(source['source_sha256'],source['source_xml'])
 assert source_notes(db,*key)==source['source_notes_xml']
 validate(row,source,required=True,enforce_workflow=False)
 current[k]=entry

def pin(s,r):
 return dict(code_id=r['code_id'],source_id=r['source_id'],number=r['number'],
  source_sha256=s['source_sha256'],source_body_sha256=digest(s['source_xml']),
  source_notes_sha256=digest(s['source_notes_xml']),proposed_sha256=digest(r['proposed_xml']))

def guards(entry):
 source,row,folder,_,_=entry;refs=rc.token_refs(row.get('proposed_xml')or'');found={}
 for k,(s,r,other,_,_)in current.items():
  if k==rc.key(row):continue
  if folder==other or rc.normalize(r['number'])in refs:found[k]=pin(s,r)
 capture_files=[]
 if str(folder).startswith(str(P)):
  capture_files.append(P/'integration/edition001/reference-targets.json')
 if folder==extra:
  capture_files.append(extra/'reference-targets.json')
 if folder==A/'pfu-petits-revenus/edition002':
  capture_files.append(folder/'integration-reference-targets.json')
 for file in capture_files:
  for k,target in load(file)['targets'].items():
   if k==rc.key(row):continue
   if k in current:
    s,r,*_=current[k];found[k]=pin(s,r);continue
   # Strictly compare the captured external view; no blind use of a later draft.
   assert rc.guard(rc.state(db,k))==rc.guard(target),('External dependency changed',k)
   code,sid=k.split('|');proposal=db.execute('SELECT proposed_xml FROM drafts WHERE code_id=? AND source_id=?',(code,sid)).fetchone()
   s=dict(source_sha256=target['source_sha256'],source_xml=target['source_xml'],source_notes_xml=target['source_notes_xml'])
   r=dict(code_id=code,source_id=sid,number=target['number'],proposed_xml=proposal[0]if proposal else None)
   found[k]=pin(s,r)
 return list(found.values())

stamp=datetime.now(timezone.utc).isoformat();policy=digest((B/'policy-coordinations.json').read_text())
ledger=B/'runtime/substantive-audits.json';old=load(ledger)
entries={(a['code_id'],a['source_id']):a for a in old['audits']}
adopted=[]
for k,entry in current.items():
 source,row,folder,evidence,reviewer=entry
 audit=dict(code_id=row['code_id'],source_id=row['source_id'],assessment=row['substantive_impact'],
  certificate=certificate(row,source,policy),reviewed_by=reviewer,approved_at=stamp,
  evidence_file=str(evidence.relative_to(B)),dependency_guards=guards(entry),semantic_review_by_jurist=False)
 entries[(row['code_id'],row['source_id'])]=audit
 adopted.append(dict(package=str(folder.relative_to(B)),source_id=row['source_id'],classification=audit['assessment']['classification']))
db.close()
with writer_lock():
 assert load(ledger)==old,'Audit ledger changed concurrently'
 history=P/'audit-ledger-history';history.mkdir(exist_ok=True)
 archive_hash=hashlib.sha256(ledger.read_bytes()).hexdigest()
 archived=history/(archive_hash+'.json')
 if not archived.exists():atomic(archived,old)
 atomic(ledger,dict(version=1,scope='Bounded independently counter-read whole texts; no corpus-wide net balance or jurist audit',approved_at=stamp,policy_sha256=policy,audits=list(entries.values())))
 atomic(P/'audit-adoption.json',dict(adopted=adopted,skipped=skipped,
  prior_unreviewed_policy_certificates_not_rebound=True,global_net_reduction='not_established',national_savings=None))
print(json.dumps(dict(current_independent_readings=len(adopted),stored_audits=len(entries),superseded_not_rebound=len(skipped),global_net_reduction=False)))
