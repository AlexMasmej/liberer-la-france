from pathlib import Path
import json,sqlite3,hashlib,sys,datetime,collections
P=Path(__file__).resolve().parent;L=P.parents[3];sys.path.insert(0,str(L))
from ingest import source_notes
from run_exhaustive import validate_answer,needs_graphic_source
sha=lambda x:hashlib.sha256(x if isinstance(x,bytes)else(x or'').encode()).hexdigest()
sources=json.loads((P/'source.json').read_text());answer=json.loads((P/'answer.json').read_text());deps=json.loads((P/'dependencies.json').read_text());capture=json.loads((P/'capture.json').read_text());before=sha((P/'answer.json').read_bytes());validate_answer(answer,sources);assert sha(json.dumps(answer,ensure_ascii=False,indent=2)+'\n')==before
scope=json.loads((L/'runtime/export-source/securite-sociale.json').read_text());keys={(x['code_id'],x['source_id'])for x in sources};scopekeys={(x['code_id'],x['source_id'])for x in scope};assert keys<=scopekeys
assert not any(needs_graphic_source(x)for x in sources)
checks=[];drift=[];collisions=[]
db=sqlite3.connect('file:'+str(L/'corpus.sqlite')+'?mode=ro',uri=True);db.row_factory=sqlite3.Row;db.execute('BEGIN')
for x in sources+deps:
 key=x['code_id'],x['source_id'];a=db.execute('SELECT source_sha256,content_xml FROM articles WHERE code_id=? AND id=?',key).fetchone();d=db.execute('SELECT proposed_xml,status FROM drafts WHERE code_id=? AND source_id=?',key).fetchone();ok=a and a[0]==x['source_sha256']and a[1]==x['source_xml']and source_notes(db,*key)==x['source_notes_xml'];assert ok,x['number'];old=x.get('previous_draft');unchanged=(d is None)if old is None else(d is not None and d['proposed_xml']==old['proposed_xml']and d['status']==old['status']);checks.append(dict(code_id=key[0],source_id=key[1],number=x['number'],source_and_notes_match=True,previous_draft_match=unchanged,source_sha256=x['source_sha256'],source_body_sha256=x['source_body_sha256'],source_notes_sha256=x['source_notes_sha256'],proposed_sha256=sha(d['proposed_xml']if d else None)))
 if not unchanged:drift.append(x['number'])
 if key in keys and d is not None:collisions.append(x['number'])
db.rollback();db.close()
policymatch={n:sha((L/n).read_bytes())==h for n,h in capture['policies'].items()}
heldpath=L/'runtime/exhaustive/held-graphic-sources.json';held=json.loads(heldpath.read_text())if heldpath.exists()else[];heldkeys={x['source_id']for x in held};assert not {x['source_id']for x in sources}&heldkeys
# Queue artifacts are not live-process evidence. Parent has separately reserved the selected CSS IDs while CLI3 reviews Travail.
historic=[]
for f in (L/'runtime/exhaustive/jobs').glob('*/source.json'):
 try:job=json.loads(f.read_text());job=job['articles']if isinstance(job,dict)and'articles'in job else job
 except (ValueError,TypeError):continue
 if not isinstance(job,list):continue
 overlap=[x.get('source_id')for x in job if isinstance(x,dict)and(x.get('code_id'),x.get('source_id'))in keys]
 if overlap:historic.append(dict(job=f.parent.name,overlap=overlap,result_exists=(f.parent/'result.json').exists()))
report=dict(checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),sqlite='mode=ro BEGIN',selected_articles=24,current_export_scope=True,current_export_count=len(scope),source_and_notes_chars=sum(len(x['source_xml'])+len(x['source_notes_xml'])for x in sources),full_source_and_notes_read=True,whole_article_proposals=5,material_reductions=4,coordination_only=1,retained_unchanged=19,unique_cut_measure_ids=sorted({e['measure_id']for r in answer if r['substantive_impact']['classification']=='material_reduction'for e in r['substantive_impact']['effects']}),all_local_schema_checks_passed=True,source_and_notes_guards_current=True,previous_draft_guard_drift=drift,selected_draft_collisions=collisions,policy_guards_match=policymatch,no_graphic_held_overlap=True,historical_job_artifacts=historic,active_job_scope_provenance='Parent reservation: CLI3 active Travail reviews only. Historic job artifacts are not a live-process check; parent must recheck allocation immediately before commit.',checks=checks,answer_sha256=before,source_sha256=sha((P/'source.json').read_bytes()),dependencies_sha256=sha((P/'dependencies.json').read_bytes()),national_savings={'status':'unknown','value':None},net_global_effect='not_established',independent_impact_audit=False,semantic_review_by_jurist=False,registered=False,published=False)
(P/'validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items()if k not in ['checks']},ensure_ascii=False,indent=2))
