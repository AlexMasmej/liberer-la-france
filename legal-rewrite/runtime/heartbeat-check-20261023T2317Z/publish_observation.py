"""Publish dated monitoring metadata; no article, policy, admission or audit mutation."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os
OUT=Path(__file__).resolve().parent;R=OUT.parent
def sha(b):return hashlib.sha256(b).hexdigest()
def enc(o):return (json.dumps(o,ensure_ascii=False,indent=2)+'\n').encode()
def read(p):return json.loads(p.read_bytes())
def put(n,o):
    with (OUT/n).open('xb') as f:f.write(enc(o));f.flush();os.fsync(f.fileno())

observations=R/'coherence-policy-resumption-20261023T2301Z/observations'
latest=max(observations.glob('*.json'),key=lambda x:x.stat().st_mtime)
final=read(latest)
assert final['new_pid']==58195 and final['current_successful_articles']==0
assert final['actual_current_distinct_native_responses']==0 and not final['guarded_phase_matches_current_pid']
assert final['old_exit_receipt']['pid']==41583 and final['old_exit_receipt']['exit_code']==0
assert not (R/'supervision/disabled').exists()
put('final-native-and-process.json',final)
summary=read(OUT/'CONTROL.json')
summary.update(final_native_capture_at_utc=final['at_utc'],latest_final_observation=str(OUT/'final-native-and-process.json'),
    actual_current_phase_matches_new_PID=False,current_native_processes=0,current_distinct_native_responses=0,
    new_successful_articles=0,new_accepted_review_verification_complete=False)
# The capsule is open until its manifest is created below.
(OUT/'CONTROL.json').write_bytes(enc(summary))
disposition=read(OUT/'current-dispositions.json');budget=read(OUT/'next-audit-storage-budget.json')
names=['coherence-rollout-latest.json','second-pass-coherence-human-directive-latest.json',
       'second-pass-parallelism-latest.json','completion-coverage-latest.json',
       'deferred-recovery-latest.json','audit-refresh-deferred.json']
before={n:(R/n).read_bytes() for n in names};data={n:json.loads(b) for n,b in before.items()}
for n,b in before.items():
    with (OUT/('before-'+n)).open('xb') as f:f.write(b);f.flush();os.fsync(f.fileno())
proof=str(OUT/'CONTROL.json');native=str(OUT/'final-native-and-process.json')
semantic=R/'cross-border-coherence-followup-20261023T230543Z'
data[names[0]].update(phase='NEW_SUPERVISED_STARTUP_AFTER_ACTUAL_STALE_POLICY_EXIT',new_pid=58195,
    previous_refused_pid=41583,last_observed_at_utc=final['at_utc'],latest_observation=proof,
    actual_priority_in_native_inputs_verified=False,eight_distinct_native_responses_verified=False,
    historical_41583_eight_responses_are_not_58195_responses=True,
    old41583_actual_exit_verified=True,exact_supervised_launch_history_since_original_release=[41583,58195],
    current_phase_native_and_accepted_review_still_required=True,
    instructions='Do not replay completed drain/install/release or adoption. The registered supervisor continued once after the actual41583 exit. Verify58195 physical identity, fresh guarded phase, eight new distinct Astra/medium responses under current frozen policies, then a fully confronted accepted review. Preserve the exact two-launch chain; do not force the original one-launch verifier or finalizer.',
    resumption_finalizer_not_executed=True)
data[names[1]].update(state='coherence_installed_new_supervised_startup_no_fresh_response_or_acceptance_yet',
    latest_observation=proof,current_coordinator_pid=58195,accepted_review_verification_complete=False,
    latest_bounded_semantic_work=str(semantic/'CONTROL.json'),
    latest_bounded_semantic_manifest_sha256='28846b3ff04163f2ebc272e4528003573381b81440317180d1efeeea9358694e',
    latest_bounded_semantic_reads=64,new_unregistered_text_candidates=5,
    no_old_limited_review_guards_forced=True)
data[names[2]].update(state='supervised_continuation_startup_current_phase_and_native_execution_pending',
    pid=58195,stage='startup',active_role_limits=None,execution_verified=False,current_execution_proof=None,
    current_physical_process_proof=native,latest_operational_observation=summary,
    latest_native_execution_proof=native,latest_native_execution_observed_at_utc=final['at_utc'],
    current_responding_distinct_sessions_at_observation=0,new_coordinator_acceptance_verified=False,
    configured_review_tail_capacity=8,active_worker_control={'workers':8,'role_limits':{'new':6,'review':0},'review_tail_limit':8},
    prior_execution_proofs_are_historical_for_their_own_PIDs=True,performance_gain_measured=False)
data[names[3]].update(last_checked_at_utc=summary['at_utc'],latest_read_only_progress_check=summary,
    first_pass_coverage_full_inventory_is_prior_dated_evidence=True)
data[names[4]].update(coordinator_pid=58195,last_checked_at_utc=summary['at_utc'],
    current_native_responses_verified=False,current_execution_proof=native,
    current_disposition_proof=str(OUT/'current-dispositions.json'),latest_disposition=disposition,
    original_nonaccepted_review_articles_current_pending=disposition['original_pending'],
    previous_coordinator_deferred_articles_current_pending=disposition['previous_deferred_pending'],
    unique_original_and_current_deferred_reviews_pending=disposition['prior_known_union_pending'],
    refused41583_terminal_pending=disposition['refused_41583_union_pending'],
    current_coordinator_terminal_nonaccepted_pending=disposition['current58195_terminal_pending'],
    unique_all_known_terminal_nonaccepted_pending=disposition['unique_all_known_terminal_nonaccepted_pending'],
    no_recovery_claim_on_queue_presence=True,no_response_replay_or_registration_by_control=True)
data[names[5]].update(state='current_audit_valid_refresh_not_due_prospective_storage_below_budget',proof=proof,
    additional_treatments_since_new_audit_baseline=summary['additional_successful_treatments_after_audit_prefix'],
    refresh_still_due=False,available_free_bytes=budget['free_bytes'],available_free_gib=budget['free_gib'],
    current_wal_bytes=budget['wal_bytes'],coordinator_pid=58195,
    next_capture_budget=str(OUT/'next-audit-storage-budget.json'),next_capture_admissible_at_observation=False,
    minimum_free_bytes_during_writers=9*2**30,no_new_snapshot_launched=True)
for n,d in data.items():d['previous_pointer_preserved']=str(OUT/('before-'+n))
put('pointer-update-intent.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),
    changes=[dict(pointer=n,before_sha256=sha(before[n]),after_sha256=sha(enc(data[n]))) for n in names],
    monitoring_metadata_only=True))
changes=[]
for n,d in data.items():
    p=R/n;b=enc(d);tmp=p.with_name(p.name+'.heartbeat-2317Z.tmp')
    with tmp.open('xb') as f:f.write(b);f.flush();os.fsync(f.fileno())
    assert p.read_bytes()==before[n],n
    os.replace(tmp,p);assert p.read_bytes()==b
    changes.append(dict(pointer=n,before_sha256=sha(before[n]),after_sha256=sha(b)))
put('pointer-updates.json',dict(changes=changes,global_audit_pointer_sources_articles_policies_admissions_not_modified=True))
put('documentation-reference.json',dict(skill_used='OpenAI Docs',
    source='https://learn.chatgpt.com/docs/automations?surface=app',
    scope='Durable same-chat monitoring prompt maintenance; no cadence change and no product behavior inference from the legal task.'))
files={str(p.relative_to(OUT)):dict(bytes=p.stat().st_size,sha256=sha(p.read_bytes()))
       for p in sorted(OUT.iterdir()) if p.is_file() and p.name!='artifact-manifest.json'}
put('artifact-manifest.json',dict(files=files,closed_at_utc=datetime.now(timezone.utc).isoformat(),
    no_global_legal_completion=True,original_rollout_and_new_resumption_work_folders_remain_open=True))
print(json.dumps(dict(folder=str(OUT),manifest_sha256=sha((OUT/'artifact-manifest.json').read_bytes()),files=len(files)),ensure_ascii=False))
