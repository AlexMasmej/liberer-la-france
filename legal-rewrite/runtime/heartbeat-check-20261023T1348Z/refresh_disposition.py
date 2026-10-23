from pathlib import Path
from collections import Counter,defaultdict
import json,sqlite3,hashlib,sys,datetime
P=Path(__file__).resolve().parent;R=P.parents[1];sys.path.insert(0,str(R))
from ingest import source_notes
stable={}
def read(p):
 data=Path(p).read_bytes();stable[Path(p)]=hashlib.sha256(data).hexdigest();return json.loads(data)
old=read(R/'runtime/false-usage-recovery-20261023T1041Z/locked-disposition.json')
accepted=read(P/'accepted-verification-final.json')
proven_new={(x['code_id'],x['source_id']) for j in accepted['verified_jobs'] for x in j['rows']}
proven_reviews={(x['code_id'],x['source_id']) for j in accepted['verified_reviews'] for x in j['rows']}
manifest=read(R/'runtime/radical-review-20261019.json');prior={(x['code_id'],x['source_id']):x for x in manifest['prior_articles']}
db=sqlite3.connect((R/'corpus.sqlite').as_uri()+'?mode=ro',uri=True);db.execute('BEGIN')
rows=[];group=defaultdict(list);sources={}
for entry in old['rows']:
 job=entry['job'];key=entry['code_id'],entry['source_id']
 if job not in sources:sources[job]={(x['code_id'],x['source_id']):x for x in read(R/'runtime/exhaustive/jobs'/job/'source.json')}
 source=sources[job][key]
 assert db.execute('SELECT source_sha256,content_xml,valid_from,valid_until FROM articles WHERE code_id=? AND id=?',key).fetchone()==(source['source_sha256'],source['source_xml'],source['valid_from'],source['valid_until'])
 assert source_notes(db,*key)==source['source_notes_xml']
 cur=db.execute('SELECT source_sha256,status,proposed_xml FROM drafts WHERE code_id=? AND source_id=?',key).fetchone()
 missing=not(cur and cur[0]==source['source_sha256'] and (cur[2] or cur[1]=='retained_unchanged'))
 review_pending=entry['kind']=='review' and prior[key]['review_status']=='pending'
 resolved=not missing if entry['kind']=='new' else not review_pending
 if resolved:assert key in (proven_new if entry['kind']=='new' else proven_reviews)
 row=entry|dict(first_pass_absent=missing,prior_review_pending=review_pending,resolved_by_fresh_verified_work=resolved)
 rows.append(row);group[job].append(row)
db.close()
for p,h in stable.items():assert hashlib.sha256(p.read_bytes()).hexdigest()==h
jobs=[dict(job=k,kind=v[0]['kind'],historical_outcome=v[0]['outcome'],articles=len(v),current_pending=sum(not x['resolved_by_fresh_verified_work'] for x in v),current_recovered=sum(x['resolved_by_fresh_verified_work'] for x in v)) for k,v in group.items()]
report=dict(checked_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),original_coordinator_pid=3122,current_coordinator_pid=73618,
 original_jobs=len(jobs),current_pending_jobs=sum(x['current_pending']>0 for x in jobs),recovered_original_jobs=[x['job'] for x in jobs if x['current_pending']==0],
 current_original_new_absent=sum(x['kind']=='new' and x['first_pass_absent'] for x in rows),current_original_reviews_pending=sum(x['prior_review_pending'] for x in rows),
 checked_immutable_sources_notes_versions=len(rows),historical_outcomes=dict(Counter(x['historical_outcome'] for x in jobs)),
 current_pending_jobs_by_historical_outcome=dict(Counter(x['historical_outcome'] for x in jobs if x['current_pending'])),
 jobs=jobs,rows=rows,acceptance_proof=str(P/'accepted-verification-final.json'),input_hashes={str(p.relative_to(R)):h for p,h in stable.items()},
 replayed_answers=False,metadata_helper_executed=False,canonical_writes=0,second_pass_completion_of_entire_corpus_claimed=False)
with (P/'deferred-disposition.json').open('x') as f:json.dump(report,f,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in report.items() if k not in ['rows','jobs','input_hashes','recovered_original_jobs']},ensure_ascii=False))
