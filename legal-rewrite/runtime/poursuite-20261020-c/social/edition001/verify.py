from pathlib import Path
import json,sqlite3,hashlib,sys,copy,datetime
P=Path(__file__).resolve().parent;L=P.parents[3];sys.path.insert(0,str(L));from ingest import source_notes;from run_exhaustive import validate_answer;import reference_coherence as ref
sha=lambda v:hashlib.sha256(v if isinstance(v,bytes)else(v or'').encode()).hexdigest()
s=json.loads((P/'source.json').read_text());a=json.loads((P/'answer.json').read_text());ctx=json.loads((P/'context.json').read_text());snap=json.loads((P/'reference-targets.json').read_text());check=copy.deepcopy(a);validate_answer(check,s);assert check==a
export=json.loads((L/'runtime/export-source/securite-sociale.json').read_text());scope={(x['code_id'],x['source_id'])for x in export};assert all((x['code_id'],x['source_id'])in scope for x in s);assert len({x['source_id']for x in s})==24
held_text=(L/'runtime/exhaustive/held-graphic-sources.json').read_text();assert not any(x['source_id']in held_text for x in s)
recent=[]
for d in (L/'runtime/exhaustive/jobs').iterdir():
 fs=list(d.glob('events-*.jsonl'))if d.is_dir()else[]
 if fs:recent.append((max(f.stat().st_mtime for f in fs),d))
active=[];chosen={(x['code_id'],x['source_id'])for x in s}
for _,d in sorted(recent,reverse=True)[:3]:
 xs=json.loads((d/'source.json').read_text());overlap=sorted(i for c,i in chosen&{(x['code_id'],x['source_id'])for x in xs});active.append(dict(job=d.name,overlap=overlap,evidence='Three most recently modified job event logs, metadata only; not proof of live process state.'))
print('RECENT JOB METADATA',active)
db=sqlite3.connect('file:'+str(L/'corpus.sqlite')+'?mode=ro',uri=True);db.row_factory=sqlite3.Row;db.execute('BEGIN');ref.check_guards(db,snap);checks=[]
for x in s+ctx:
 c,i=x['code_id'],x['source_id'];r=db.execute('select source_sha256,content_xml from articles where code_id=? and id=?',(c,i)).fetchone();d=db.execute('select * from drafts where code_id=? and source_id=?',(c,i)).fetchone();prior=dict(d)if d else None
 if prior:prior['proposed_sha256']=sha(prior['proposed_xml'])
 tests=dict(source_sha256=r['source_sha256']==x['source_sha256'],source_body=sha(r['content_xml'])==x['source_body_sha256'],source_notes=sha(source_notes(db,c,i))==x['source_notes_sha256'],entire_beforeimage=prior==x['previous_draft'])
 if x in s:
  raw=db.execute("select xml,sha256 from documents where code_id=? and id=? and kind='ARTICLE'",(c,i)).fetchone();tests['raw_document']=sha(raw['xml'])==raw['sha256']==x['source_document_sha256']==x['source_sha256'];tests['no_existing_draft']=d is None
 checks.append(dict(number=x['number'],source_id=i,checks=tests))
certs=[dict(number=x['number'],needed=bool(snap['requirements'][ref.key(x)]),current_before_commit=ref.certificate_current(db,x,y['proposed_xml'],y.get('reference_coherence')))for x,y in zip(s,a)]
db.rollback();db.close();pol={n:sha((L/n).read_bytes())==sha((P/n).read_bytes())for n in ['policy-coordinations.json','site-summaries.json']};passed=all(all(x['checks'].values())for x in checks)and all(pol.values())and all(x['current_before_commit']for x in certs)
r=dict(checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),mode='ro BEGIN',schema_valid_articles=24,current_export_membership=True,no_previous_drafts=True,source_and_context_records=len(checks),individual_guards=sum(len(x['checks'])for x in checks),checks=checks,policies=pol,reference_targets=14,reference_checks=sum(len(x.get('reference_checks',[]))for x in a),certificates=certs,all_guards_match=passed,recent_jobs=active,known_future_intrapack_target_changes=json.loads((P/'intrapack-planned-targets.json').read_text()),arithmetic_and_preservation_tests=10,semantic_review_by_jurist=False,independent_legal_approval=False,limits=['Guard state is a dated read-only snapshot, not a reservation. Recheck under writer lock.','Current-reference certificates intentionally use canonical BEFORE states; four dependent rows need recertification after the three target changes in this same pack.','No national savings or net budget calculation; no claim of48articlescompleted.'])
(P/'validation.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print('SCHEMA',24,'RECORDS',len(checks),'GUARDS',r['individual_guards'],'REFERENCES',r['reference_checks'],'ALL PASS',passed,'JOBS',[x['job']for x in active]);assert passed
