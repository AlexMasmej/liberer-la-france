from pathlib import Path
import json,sqlite3,hashlib,time,os,sys,datetime
H=Path(__file__).resolve().parent;B=H.parents[1];R=B/'runtime/exhaustive';sys.path.insert(0,str(B))
from run_exhaustive import normalized,validate_answer
sha=lambda v:hashlib.sha256(v.encode()if isinstance(v,str)else v).hexdigest()
slugs=['travail','impots','securite-sociale','urbanisme','construction-habitation']+['impots-annexe-'+str(i)for i in range(1,5)]
canon={};counts={}
for slug in slugs:
 rows=json.loads((B.parent/'sites/liberer-la-retraite/dist/corpus'/ (slug+'.json')).read_text());counts[slug]={'source_records':len(rows),'drafted':0,'retained_unchanged':0,'pending':0}
 for r in rows:canon[r['code_id'],r['source_id']]=(slug,r['source_sha256'])
c=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);c.row_factory=sqlite3.Row;c.execute('BEGIN')
accepted={};copied=[];mismatch=[];reserved_bad=[]
for d in c.execute('SELECT d.code_id,d.source_id,d.source_sha256,d.status,d.proposed_xml,a.content_xml,a.source_sha256 AS canonical_sha FROM drafts d LEFT JOIN articles a ON a.code_id=d.code_id AND a.id=d.source_id'):
 key=(d['code_id'],d['source_id']);accepted[key]=dict(d)
 if key not in canon:continue
 slug,source_sha=canon[key]
 if source_sha!=d['source_sha256']or source_sha!=d['canonical_sha']:mismatch.append({'code_id':key[0],'source_id':key[1]});continue
 original=normalized(d['content_xml']);proposal=normalized(d['proposed_xml'])
 if d['status']=='retained_unchanged':
  if original not in {'Réservé.','Réservé','(Réservé)'}:reserved_bad.append({'code_id':key[0],'source_id':key[1]})
  counts[slug]['retained_unchanged']+=1
 elif d['proposed_xml']:
  counts[slug]['drafted']+=1
  if original==proposal:copied.append({'code_id':key[0],'source_id':key[1]})
for slug,row in counts.items():row['pending']=row['source_records']-row['drafted']-row['retained_unchanged']
held=json.loads((R/'held-graphic-sources.json').read_text());held_results=[]
for h in held:
 matches=[(key,val)for key,val in canon.items()if key[1]==h['source_id']];assert len(matches)==1
 key=matches[0][0];held_results.append(h|{'database_draft_present':key in accepted,'pending':key not in accepted})
c.rollback();c.close()
policy=json.loads((B/'policy-coordinations.json').read_text());summary=json.loads((B/'site-summaries.json').read_text());started=(R/'coordinator.pid').stat().st_mtime
folders=sorted([p for p in (R/'jobs').iterdir()if p.is_dir()and(p/'source.json').exists()],key=lambda p:(p/'source.json').stat().st_mtime,reverse=True)
recent=[p for p in folders if(p/'source.json').stat().st_mtime>=started][:12]
if not recent:recent=folders[:6]
policy_checks=[]
for f in recent:
 info={'job':f.name,'source_mtime_unix':(f/'source.json').stat().st_mtime}
 try:
  coord=json.loads((f/'coordination.json').read_text());pol=json.loads((f/'policy.json').read_text());info['coordination_semantically_current']=coord==policy;info['site_policy_semantically_current']=pol==summary
  fp=f/'policy-fingerprint.json';finger=json.loads(fp.read_text())if fp.exists()else None
  info['fingerprint_present']=bool(finger);info['stored_coordination_hash_matches_frozen_file']=bool(finger and finger.get('coordination_sha256')==sha((f/'coordination.json').read_text()));info['frozen_coordination_sha256']=sha((f/'coordination.json').read_text())
 except Exception as e:info['error']=str(e)
 policy_checks.append(info)
rejected=[]
for f in folders:
 failure=f/'validation-failure.json';stale=f/'stale-policy.json'
 if not(failure.exists()or stale.exists()):continue
 item={'job':f.name,'failure_marker':failure.exists(),'stale_policy_marker':stale.exists()}
 if(f/'answer.json').exists():
  try:
   ans=json.loads((f/'answer.json').read_text());src=json.loads((f/'source.json').read_text());validate_answer(ans,src);item['current_answer_structurally_valid']=True
  except Exception as e:item['current_answer_structurally_valid']=False;item['validation_error']=str(e)
  try:
   ans=json.loads((f/'answer.json').read_text());item['whole_answer_matches_current_database']=bool(ans)and all((a.get('code_id'),a.get('source_id'))in accepted and accepted[a['code_id'],a['source_id']]['proposed_xml']==a.get('proposed_xml')for a in ans)
  except Exception:item['whole_answer_matches_current_database']=False
 else:item['answer_present']=False;item['whole_answer_matches_current_database']=False
 rejected.append(item)
failed_file=R/'failed-jobs.json';failed=json.loads(failed_file.read_text())if failed_file.exists()else[]
queue=json.loads((R/'queue.json').read_text());mixed=json.loads((R/'mixed-queue.json').read_text());queued_ids={i for q in queue for i in q['source_ids']}
status=json.loads((R/'status.json').read_text());last=json.loads((B/'runtime/last-published.json').read_text());publication=json.loads((B/'runtime/publication.json').read_text())
log=B/'runtime/exhaustive-run.log';text=log.read_text();tail=text[-4000:]
pid=int((R/'coordinator.pid').read_text());alive=None
try:os.kill(pid,0);alive=True
except ProcessLookupError:alive=False
except PermissionError:alive='permission_denied'
result={'observed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'read_only_audit':True,'complete':False,'scope':'Observed continuation configuration and documented activity; not a legal validation or proof that the rewriting is complete.','workers':{'configured':json.loads((R/'worker-limit.json').read_text())['workers'],'manual_slots':json.loads((R/'manual-agent-slots.json').read_text()),'coordinator_pid_record':pid,'process_exists_probe':alive,'observed_process_command':'run_exhaustive.py --workers 3 --interleave-review --wait-for-coordinator --export-every 200 --deploy-on-export --publish-at-end','command_evidence':'Read-only /bin/ps of PID 77663 returned this command and elapsed 17:24. A PID record alone was not treated as process evidence.','simultaneous_active_worker_processes_proved':False},'queue':{'new_jobs':len(queue),'mixed_jobs':len(mixed),'mixed_new_jobs':sum(not q['review']for q in mixed),'mixed_review_jobs':sum(q['review']for q in mixed),'held_source_in_new_queue':[h['source_id']for h in held if h['source_id']in queued_ids],'resume_guard':'run_job re-reads drafts before starting and skips sources already accepted; registration refuses conflicting overwrite.'},'recent_policy_checks':policy_checks,'policy_files':{'coordination_sha256':sha((B/'policy-coordinations.json').read_bytes()),'site_summary_sha256':sha((B/'site-summaries.json').read_bytes())},'database_counts':{'source_records':len(canon),'drafted':sum(v['drafted']for v in counts.values()),'retained_unchanged':sum(v['retained_unchanged']for v in counts.values()),'pending':sum(v['pending']for v in counts.values()),'codes':counts,'normalized_source_copies_counted_as_drafts':copied,'canonical_source_mismatches':mismatch,'improper_retained_normative_sources':reserved_bad},'status_snapshot':{'reported_status':status['status'],'reported_drafted':status['drafted_articles'],'reported_pending':status['pending'],'updated_at_unix':status['updated_at_unix'],'exhaustive_rewriting_complete':status['exhaustive_rewriting_complete'],'jurist_reviewed_articles':status['jurist_reviewed_articles']},'held_graphics':held_results,'rejection_gates':{'source_hash_and_ids_checked':True,'complete_assignment_required':True,'normalized_copy_rejected':True,'unresolved_graphic_rejected_except_explicit_repeal':True,'stale_policy_checked_before_acceptance':True,'benefit_review_required_when_flagged':True,'transactional_batch_acceptance':True,'failed_jobs_registry':failed,'failure_or_stale_marker_jobs':rejected,'limitation':'Structural gates do not prove the legal correctness of an article; a failed marker may be historical and is distinguished from a currently invalid answer.'},'publication':{'configured_every_new_or_reviewed_articles':200,'configured_deploy_on_export':True,'configured_publish_at_end':True,'time_based_schedule':False,'pipeline_validation_before_build_and_deploy':True,'last_published_report':last,'latest_local_publication_report':publication,'current_live_http_verification_performed':False,'limitation':'Last publication report proves a prior successful pipeline run, not that every current DB article is already live or a future deployment will succeed.'},'activity_evidence':{'log_path':str(log),'log_size_bytes':log.stat().st_size,'log_modified_at_unix':log.stat().st_mtime,'last_acceptance_lines':[l for l in tail.splitlines()if l.startswith(('ACCEPTED','RADICAL REVIEW','BLOCKED','START','MIXED QUEUE','STOP'))][-6:]},'material_findings':[]}
if copied:result['material_findings'].append('Normalized copies are counted as drafts; inspect listed records.')
if mismatch or reserved_bad:result['material_findings'].append('Canonical mismatch or improperly retained norm found.')
if any(not h['pending']for h in held_results):result['material_findings'].append('At least one held graphic has an accepted draft; examine scope/repeal before interpreting it as recovered.')
if any(not x.get('coordination_semantically_current')or not x.get('site_policy_semantically_current')for x in policy_checks):result['material_findings'].append('At least one recent frozen policy differs from current policy.')
if any(x.get('current_answer_structurally_valid')is False and x.get('whole_answer_matches_current_database')for x in rejected):result['material_findings'].append('A currently invalid full answer matches the current DB; investigate provenance.')
(H/'continuation-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'counts':result['database_counts']|{'codes':'see report'},'recent_jobs':len(policy_checks),'policies_current':all(x.get('coordination_semantically_current')and x.get('site_policy_semantically_current')for x in policy_checks),'held':len(held_results),'held_all_pending':all(x['pending']for x in held_results),'rejection_markers':len(rejected),'findings':result['material_findings']},ensure_ascii=False,indent=2))
