from pathlib import Path
import json,sqlite3,hashlib,sys,datetime,re
P=Path(__file__).resolve().parent;L=P.parents[3];sys.path.insert(0,str(L));from ingest import source_notes;from run_exhaustive import validate_answer
sha=lambda x:hashlib.sha256(x if isinstance(x,bytes)else(x or'').encode()).hexdigest()
s=json.loads((P/'source.json').read_text());a=json.loads((P/'answer.json').read_text());prior=json.loads((P/'answer.json').read_text());validate_answer(a,s);assert a==prior
context=json.loads((P/'context.json').read_text());export=json.loads((L/'runtime/export-source/securite-sociale.json').read_text());scope={(x['code_id'],x['source_id'])for x in export};selected={(x['code_id'],x['source_id'])for x in s};assert selected<=scope
held=json.loads((L/'runtime/exhaustive/held-graphic-sources.json').read_text());held_text=json.dumps(held);held_matches=[x['source_id']for x in s if x['source_id']in held_text];assert not held_matches
# Read only job metadata: most recently active event logs, no processes/signals.
events=[]
for d in (L/'runtime/exhaustive/jobs').iterdir():
 if d.is_dir():
  fs=list(d.glob('events-*.jsonl'))
  if fs:events.append((max(f.stat().st_mtime for f in fs),d))
active=[]
for _,d in sorted(events,reverse=True)[:3]:
 rows=json.loads((d/'source.json').read_text());keys={(x['code_id'],x['source_id'])for x in rows};active.append(dict(job=d.name,evidence='Three most recently modified job event-log sets; metadata only, not proof of live process state',source_ids=[x['source_id']for x in rows],overlap=sorted(i for c,i in selected&keys)))
assert not any(x['overlap']for x in active)
db=sqlite3.connect('file:'+str(L/'corpus.sqlite')+'?mode=ro',uri=True);db.row_factory=sqlite3.Row;db.execute('BEGIN');checks=[]
for x in s+context:
 k=x['code_id'],x['source_id'];v=db.execute('select source_sha256,content_xml from articles where code_id=? and id=?',k).fetchone();d=db.execute('select * from drafts where code_id=? and source_id=?',k).fetchone();old=dict(d)if d else None
 if old:old['proposed_sha256']=sha(old['proposed_xml'])
 tests=dict(source_sha256=v['source_sha256']==x['source_sha256'],body_sha256=sha(v['content_xml'])==x['source_body_sha256'],notes_sha256=sha(source_notes(db,*k))==x['source_notes_sha256'],previous_draft=old==x['previous_draft']);checks.append(dict(number=x['number'],source_id=x['source_id'],checks=tests))
db.rollback();db.close();policies={n:sha((L/n).read_bytes())==sha((P/n).read_bytes())for n in ['policy-coordinations.json','site-summaries.json']}
report=dict(checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),read_only_transaction='mode=ro BEGIN',schema='validate_answer passed without changing certificates',selected_source_count=len(s),current_export_membership=True,selected_without_draft=all(x['previous_draft']is None for x in s),whole_selected_sources_and_notes_read=24,whole_context_sources_notes_and_current_proposals_read=33,checks=checks,policies=policies,held_overlaps=held_matches,recent_job_metadata=active,all_guards_match=all(all(x['checks'].values())for x in checks)and all(policies.values()),taxe_salaires_direct_references=[x['number']for x in s if re.search(r'taxe sur les salaires|article\s+231\b',x['source_xml'],re.I)],limits=['Metadata snapshot cannot prevent a later worker assignment; guards must be rechecked under writer lock before registration.','Source and hash checks are technical, not independent legal validation.','No national savings or net aggregate reduction claimed.'])
(P/'validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');assert report['all_guards_match'];print('SCHEMA PASS; GUARDS',len(checks)*4,'POLICIES',policies,'RECENT JOBS',[x['job']for x in active],'TSS',report['taxe_salaires_direct_references'])
