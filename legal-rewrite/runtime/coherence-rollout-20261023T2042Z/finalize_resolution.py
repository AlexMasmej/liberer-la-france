"""Seal proven rollout and fresh monitoring pointers, never a legal completion."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,shutil,time
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1];R=ROOT/'runtime';RUN=OUT/'run'
def sha(b):return hashlib.sha256(b).hexdigest()
def fsha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()
def read(p):return json.loads(p.read_text())
def dump(n,d):
    with (OUT/n).open('x') as f:json.dump(d,f,ensure_ascii=False,indent=2);f.write('\n')
now=datetime.now(timezone.utc).isoformat();proofs=[read(p) for p in RUN.glob('resumption-proof-*.json')]
qualified=[x for x in proofs if x.get('eight_distinct_new_responses_attested') and x.get('accepted_review')]
if not qualified:raise ValueError('Eight actual distinct native responses and one accepted review still required')
proof=max(qualified,key=lambda x:x['checked_at_utc']);pid=proof['new_coordinator_pid']
assert fsha(ROOT/'run_exhaustive.py')=='d826aac7dbd43e5e07538d07a9bbf770bbb732842352424456ffd19067898802'
assert not (R/'supervision/disabled').exists()
assert read(R/'exhaustive/coordinator-run.json')['pid']==pid
assert read(R/'exhaustive/worker-limit.json')=={'workers':8,'role_limits':{'new':6,'review':0},'review_tail_limit':8}
audit_pointer=read(R/'global-reference-audit-latest.json');audit=Path(audit_pointer['folder'])
assert audit.name=='global-reference-audit-20261023T2044Z'
basis=read(audit/'pre-capture-progress.json')['treatment_count_basis'];metrics= (R/'exhaustive/job-metrics.jsonl').read_bytes()
assert metrics.endswith(b'\n') and sha(metrics[:basis['metrics_prefix_bytes']])==basis['metrics_prefix_sha256']
suffix=[json.loads(x) for x in metrics[basis['metrics_prefix_bytes']:].splitlines()]
assert all(x['coordinator_pid'] in {78943,pid} for x in suffix)
additional=sum(x.get('articles',0) for x in suffix if x['outcome'] in {'accepted','reviewed'})
current=[x for x in map(json.loads,metrics.splitlines()) if x.get('coordinator_pid')==pid]
reviewed=[x for x in current if x['outcome']=='reviewed'];failed=[x for x in current if x['outcome']=='deferred']
work_bytes=(R/'radical-review-20261019.json').read_bytes();work=json.loads(work_bytes)
rows={(x['code_id'],x['source_id']):x for x in work['prior_articles']};assert len(rows)==30314
complete=sum(x['review_status']=='completed' for x in rows.values());pending=len(rows)-complete
assert all(x['review_status'] in {'completed','pending'} for x in rows.values())
old_failed=[x for x in map(json.loads,metrics.splitlines()) if x.get('coordinator_pid')==78943 and x['outcome']=='deferred']
failed_keys=set();failure_dispositions=[]
for m in old_failed+failed:
    sources=read(R/'exhaustive/jobs'/m['job']/'source.json');keys={(x['code_id'],x['source_id']) for x in sources};still={k for k in keys if rows[k]['review_status']=='pending'}
    failed_keys.update(still);failure_dispositions.append(dict(pid=m['coordinator_pid'],job=m['job'],initial_articles=len(keys),currently_pending=len(still),identity_disposition_only_not_new_recovery_certification=True))
old_jobs=['review-construction-habitation-LEGIARTI000046123749-00001','review-urbanisme-LEGIARTI000031211073-00002','review-urbanisme-LEGIARTI000042017888-00001']
old_keys=set();old_disposition=[]
for name in old_jobs:
    sources=read(R/'exhaustive/jobs'/name/'source.json');keys={(x['code_id'],x['source_id']) for x in sources};still={k for k in keys if rows[k]['review_status']=='pending'}
    old_keys.update(still);old_disposition.append(dict(job=name,pending=len(still)))
overlap=old_keys&failed_keys
assert (R/'radical-review-20261019.json').read_bytes()==work_bytes
free=shutil.disk_usage(ROOT).free;wal=ROOT/'corpus.sqlite-wal';walbytes=wal.stat().st_size if wal.exists() else 0
summary=dict(checked_at_utc=now,coordinator_pid=pid,canonical_identities=30317,accessible_first_passes_registered=30314,accessible_first_passes_open=0,documentary_holds_unverified=3,complete_worklist_entries=30314,current_completed=complete,current_pending=pending,new_coordinator_reviewed_jobs=len(reviewed),new_coordinator_reviewed_articles=sum(x['articles'] for x in reviewed),previous_coordinator_verified_reviewed_articles=read(RUN/'queue-disposition.json')['successful_identities'],actual_treatments_after_current_audit_prefix=additional,audit_baseline_metrics_prefix_verified=True,audit_due=additional>=1000,current_validated_audit=str(audit),current_validated_audit_id=audit_pointer['audit_id'],native_processes_in_last_dated_capture=proof['native_workers'],native_responding_in_last_dated_capture=proof['native_responding_distinct'],native_capture_at_utc=proof['checked_at_utc'],eight_distinct_new_native_responses_observed=True,new_priority_present_in_actual_native_inputs=True,free_bytes=free,free_gib=free/2**30,wal_bytes=walbytes,supervision_pause_exists=False,original_review_jobs_pending=old_disposition,original_review_identities_pending=len(old_keys),current_and_previous_failed_job_dispositions=failure_dispositions,failed_review_identities_pending=len(failed_keys),unique_original_and_failed_identities_pending=len(old_keys|failed_keys),no_throughput_gain_or_global_legal_validation_claimed=True)
dump('current-observation.json',summary)
archive=read(R/'global-reference-audit-20261023T1908Z/storage-data-archives.json');saved=sum(x['original_bytes']-x['compressed_bytes'] for x in archive['files']);assert len(archive['files'])==4 and all(x['decompression_verified'] for x in archive['files'])
assert (audit/'corpus.snapshot.sqlite').exists() and not (audit/'corpus.snapshot.sqlite.gz').exists()
resolution=dict(at_utc=now,state='COHERENCE_PRIORITY_INSTALLED_SUPERVISED_RESPONSES_AND_ACCEPTANCE_VERIFIED',old_pid=78943,new_pid=pid,only_installed_file='run_exhaustive.py',previous_sha256='91e898776c7619b89461928010c02f8cd49141745473dcdefbdfd5f6f65c3e40',installed_sha256=fsha(ROOT/'run_exhaustive.py'),only_one_prompt_literal_changed=True,all_other_legal_code_policies_catalogue_and_global_model_unchanged=True,concurrent_presentation_change_review=str(OUT/'concurrent-presentation-change-review-v2.json'),concurrent_builder_only_reviewed_credit_literals_changed=True,isolated_tests_passed=20,production_test_database_or_model_used=False,old_natural_exit=read(RUN/'installation-intent.json')['exit_receipt'],drain_context=str(RUN/'drain-context.json'),full_reconciliation=str(RUN/'reconciliation.json'),queue_partition=read(RUN/'queue-disposition.json'),new_native_and_accepted_evidence=proof,source_documentary_holds_unverified=3,new_global_audit=str(audit),new_global_audit_id=audit_pointer['audit_id'],new_audit_manifest_sha256=fsha(audit/'artifact-manifest.json'),new_audit_snapshot_sha256=audit_pointer['snapshot_sha256'],semantic_reviews_requiring_new_review=audit_pointer['semantic_reviews_requiring_new_review'],fresh_changed_scope_followup=str(OUT/'changed-semantic-scope-packet.json'),fresh_cch_coordination_followup=str(OUT/'cch-financing-followup-qualified.json'),overlapping_pending_identities_deduplicated=len(overlap),old_audit_archived_losslessly_saved_bytes=saved,current_progress=summary,monitor_remains_active=True,global_legal_completion=False,semantic_review_by_jurist=False)
resolution['parent_semantic_followups']={
    'l1242_fifteen_and_two_counterparts':str(OUT/'l1242-fresh-coherence-followup.json'),
    'cch_current_financing_coordination':str(OUT/'cch-financing-followup-qualified.json'),
    'cch_two_clause_candidate_not_registered':str(OUT/'cch-financing-coordination-candidate.json'),
    'fiscal_subset_and_annexeIII38_candidate_not_registered':str(OUT/'fiscal-coherence-followup-and-candidate.json'),
    'fresh_cvae_whole_eighteen':str(OUT/'cvae-fresh-eighteen-coherence-followup.json'),
    'old_semantic_reviews_not_redeclared_applicable':True,
    'no_canonical_correction_by_parent_during_active_jobs':True}
dump('RESOLUTION.json',resolution)
names=['coherence-rollout-latest.json','second-pass-coherence-human-directive-latest.json','second-pass-parallelism-latest.json','completion-coverage-latest.json','deferred-recovery-latest.json','audit-refresh-deferred.json']
before={n:(R/n).read_bytes() for n in names}
for n,b in before.items():(OUT/('before-'+n)).write_bytes(b)
data={n:json.loads(b) for n,b in before.items()}
data['coherence-rollout-latest.json'].update(phase=resolution['state'],new_pid=pid,completed_at_utc=now,resolution=str(OUT/'RESOLUTION.json'),owned_pause_released=True,actual_priority_in_native_inputs_verified=True)
data['second-pass-coherence-human-directive-latest.json'].update(state='human_priority_installed_and_native_accepted_verified',candidate_installed=True,installed_runner_sha256=resolution['installed_sha256'],rollout_resolution=str(OUT/'RESOLUTION.json'),priority_effectively_injected_in_active_worker_sessions=True,new_coordinator_pid=pid,semantic_reviews_requiring_new_review=audit_pointer['semantic_reviews_requiring_new_review'],latest_semantic_followup=str(OUT/'changed-semantic-scope-packet.json'))
data['second-pass-parallelism-latest.json'].update(pid=pid,active_runner_sha256=resolution['installed_sha256'],latest_operational_observation=summary,latest_native_execution_proof=str(OUT/'RESOLUTION.json'),latest_native_execution_observed_at_utc=proof['checked_at_utc'],current_responding_distinct_sessions_at_observation=proof['native_responding_distinct'],coherence_priority_installed=True)
data['completion-coverage-latest.json'].update(first_pass_covered=30314,pending_first_pass=3,last_checked_at_utc=now,latest_current_audit=str(audit),latest_read_only_progress_check=summary)
data['deferred-recovery-latest.json'].update(coordinator_pid=pid,last_checked_at_utc=now,latest_disposition=summary,current_disposition_proof=str(OUT/'current-observation.json'),last_natural_reconstruction=str(OUT/'RESOLUTION.json'),no_replay_or_registration_performed_by_control=True,previous_coordinator_deferred_jobs_preserved=old_failed,new_coordinator_deferred_jobs=failed,unique_original_and_current_deferred_reviews_pending=len(old_keys|failed_keys),original_nonaccepted_review_articles_current_pending=len(old_keys),current_tail_deferred_articles=len(failed_keys),current_tail_deferred_jobs=sum(x['currently_pending']>0 for x in failure_dispositions),counts_scope='Current pending identity disposition; no fresh recovery claimed without its complete native/DB/owner/archive proof.')
data['audit-refresh-deferred.json']=dict(state='refresh_validated_resolved',resolved_at_utc=read(audit/'pointer-update.json')['at_utc'],current_validated_audit=str(audit),current_audit_id=audit_pointer['audit_id'],current_snapshot_sha256=audit_pointer['snapshot_sha256'],validation=str(audit/'validation.json'),proof=str(OUT/'RESOLUTION.json'),current_audit_kept_uncompressed=True,previous_audit_archived_losslessly=True,saved_bytes_verified=saved,available_free_bytes=free,available_free_gib=free/2**30,current_wal_bytes=walbytes,coordinator_pid=pid,canonical_writes_continue=True,additional_treatments_since_new_audit_baseline=additional,refresh_still_due=additional>=1000,new_baseline_metric_proof=str(audit/'pre-capture-progress.json'),new_baseline=basis,next_refresh_after_additional_treatments=1000,minimum_free_bytes_during_writers=9*2**30,reestimate_budget_if_footprint_or_WAL_grows=True,semantic_reviews_requiring_new_review=audit_pointer['semantic_reviews_requiring_new_review'],global_semantic_or_human_jurist_validation_claimed=False,previous_deferred_record=str(OUT/'before-audit-refresh-deferred.json'))
changes=[]
for n,d in data.items():
    d['previous_pointer_preserved']=str(OUT/('before-'+n));p=R/n;b=(json.dumps(d,ensure_ascii=False,indent=2)+'\n').encode();t=p.with_name(p.name+'.coherence-final.tmp')
    with t.open('xb') as f:f.write(b);f.flush();os.fsync(f.fileno())
    assert p.read_bytes()==before[n],n
    os.replace(t,p);assert p.read_bytes()==b;changes.append(dict(pointer=n,before_sha256=sha(before[n]),after_sha256=sha(b)))
dump('pointer-updates.json',dict(at_utc=now,changes=changes,global_audit_pointer_not_rewritten=True))
(OUT/'REPORT.md').write_text('''# Priorité cohérence effectivement chargée\n\nLe coordinateur78943 a fini normalement ses lots, puis ses cinq publications, sans signal. La pause strictement possédée et la seule fermeture des admissionsreview ont permis un drainage naturel ; les non tentés et échecs restent explicitement dans le périmètre pending.\n\nLe rapprochement intégral courant a réussi sous les quatre verrous :30317identités/neufrecueils,30311lignes de lots,1447lots,733intentions,976archives, sourcesXMLentières/NOTA/versions, registres, propriétaires, avantages, impacts, renvois et avant-images.521certificats absents et3410périmés restent travail de convergence ; aucune fraîcheur juridique globale n'en est déduite.\n\nSeul le littéral de consigne de seconde passe du runner a changé, sous empreintes et avant-image durable.20tests isolés ont réussi ; aucun modèle de test ni base de production pour les tests. L'AST et tous les validateurs sont inchangés ailleurs. Le contrôle d'intégrité complet et les empreintesDB/WAL/entrées ont précédé le retrait sous owner/octets de notre seule pause. Le LaunchAgent existant a lancé un seul nouveau coordinateur.\n\nLe nouveau prompt est retrouvé dans les entrées natives de réponses distinctesAstra/Moyen, et une véritable relecture acceptée est confrontée aux cinqchamps source/réponse/lot/DB,NOTA/bornes,registre,propriétaire,archiveavant-imageentière etcompleted. Les preuves datées sont dansrun/. La capacité8 n'est pas un gain de débit mesuré.\n\nL'audit global2044Z est validé et publié, avec gardes complètes ; l'ancien1908Z est archivé sans perte après publication, le courant reste inspectable. Les anciennes revues limitéesL1242-2etCVAE ne s'appliquent plus aux nouvelles propositions changées ; un suivi frais a relu les quinze textes du groupe L1242-2 et deux contreparties, ainsi que les dix-huit textes du groupe CVAE. Huit et sept situations limitées ont été qualifiées sous gardes actuelles ; aucun nouvel override d’héritage n’a été publié. Les coordinations CCH, transfrontalières et CRL préparées restent à enregistrer sous les contrôles ordinaires. Les contradictions prioritaires, sources retenues, toutes secondes passes et audit final frais restent requis. Aucun100%ni validation par juriste.\n''')
files={str(p.relative_to(OUT)):dict(bytes=p.stat().st_size,sha256=fsha(p)) for p in sorted(OUT.rglob('*')) if p.is_file()}
dump('artifact-manifest.json',dict(files=files,new_audit_manifest_sha256=fsha(audit/'artifact-manifest.json'),preparation_manifest_sha256=fsha(OUT/'preparation-manifest.json')))
print(json.dumps(dict(resolution=str(OUT/'RESOLUTION.json'),manifest_sha256=fsha(OUT/'artifact-manifest.json'),new_pid=pid,current_completed=complete,current_pending=pending,additional_since_audit_baseline=additional,global_legal_completion=False)))
