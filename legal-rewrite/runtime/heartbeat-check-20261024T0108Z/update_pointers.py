"""CAS publication of monitoring metadata with complete before-images."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os
OUT=Path(__file__).resolve().parent;R=OUT.parent
def sha(b):return hashlib.sha256(b).hexdigest()
def encoded(x):return (json.dumps(x,ensure_ascii=False,indent=2)+'\n').encode()
def read(p):return json.loads(p.read_bytes())
def put(n,x):
    with (OUT/n).open('xb') as f:f.write(encoded(x));f.flush();os.fsync(f.fileno())
audit_before=(R/'global-reference-audit-latest.json').read_bytes()
c=read(OUT/'CONTROL.json');o=read(OUT/'final-native-and-process.json')
assert o['new_pid']==58195 and o['current_successful_articles']==0 and o['actual_current_distinct_native_responses']==0
metrics_before=(R/'exhaustive/job-metrics.jsonl').read_bytes()
assert not [x for x in metrics_before.splitlines() if json.loads(x).get('coordinator_pid')==58195]
assert not (R/'coherence-rollout-20261023T2042Z/RESOLUTION.json').exists()
budget=read(OUT/'next-audit-storage-budget.json');dispositions=read(OUT/'current-dispositions.json')
names=['coherence-rollout-latest.json','second-pass-coherence-human-directive-latest.json',
       'second-pass-parallelism-latest.json','completion-coverage-latest.json',
       'deferred-recovery-latest.json','audit-refresh-deferred.json','network-incident-latest.json']
before={n:(R/n).read_bytes() for n in names};data={n:json.loads(b) for n,b in before.items()}
for n,b in before.items():
    with (OUT/('before-'+n)).open('xb') as f:f.write(b);f.flush();os.fsync(f.fileno())
now=datetime.now(timezone.utc).isoformat();control=str(OUT/'CONTROL.json');proof=str(OUT/'final-native-and-process.json')
wave=str(R/'coherence-current-policy-response-confirmation-20261024T0004Z/CONTROL.json')
semantic=str(R/'urbanisme-procedure-coherence-followup-20261024T0112Z/CONTROL.json')
semantic_hash='79fa7bc78a43d13fa1cb1c07cea7c77d480a716c4478e43ae215402bbcc8687c'
data[names[0]].update(phase='CURRENT_NATIVE_RETRY_INTERRUPTION_FIRST_ACCEPTANCE_PENDING',
    new_pid=58195,latest_observation=control,last_observed_at_utc=o['at_utc'],
    historical_eight_response_confirmation=wave,current_native_response_count=0,
    current_native_process_count=8,current_attempt_number=2,current_attempt_response_verified=False,
    accepted_review_still_required=True,first_new_accepted_review_verification_pending=True,
    resumption_finalizer_not_executed=True,latest_native_retry_diagnostic=str(OUT/'native-retry-diagnostic.json'))
data[names[1]].update(state='coherence_priority_installed_current_native_retries_without_response_acceptance_pending',
    current_coordinator_pid=58195,new_coordinator_pid=58195,latest_observation=control,
    latest_response_confirmation=wave,historical_eight_response_confirmation=wave,
    native_response_verification_complete=False,current_native_response_count=0,
    accepted_review_verification_complete=False,latest_bounded_semantic_work=semantic,
    latest_bounded_semantic_manifest_sha256=semantic_hash,latest_bounded_semantic_reads=19,
    latest_bounded_semantic_historical_versions=3,new_unregistered_text_candidates=1,
    unregistered_parent_candidates_total=9,
    fresh_scope='19 whole local texts, including3historical versions: R121-22/23 textual coordination, no exhaustive external CRPA/publicity or jurist certification')
data[names[2]].update(state='guarded_review_tail_native_retry_interruption',pid=58195,
    role_limits={'new':0,'review':8},execution_verified=False,
    current_execution_proof=proof,latest_native_execution_proof=proof,
    latest_native_execution_observed_at_utc=o['at_utc'],current_physical_process_proof=proof,
    latest_operational_observation=c,current_responding_distinct_sessions_at_observation=0,
    current_native_processes_at_observation=8,historical_eight_response_confirmation=wave,
    last_checked_at_utc=now,new_coordinator_acceptance_verified=False,performance_gain_measured=False)
data[names[3]].update(latest_read_only_progress_check=c,last_checked_at_utc=now)
d=data[names[4]]
d.update(state='known_pending_unchanged_current_native_retries_without_acceptance',
    coordinator_pid=58195,current_execution_proof=proof,current_resumption_proof=control,
    current_native_responses_verified=False,current_responding_native_count=0,current_native_worker_count=8,
    native_execution_verified_at_utc=o['at_utc'],current_disposition_proof=str(OUT/'current-dispositions.json'),
    last_checked_at_utc=now,latest_disposition=dispositions,
    latest_current_review_failure_diagnostic=str(OUT/'native-retry-diagnostic.json'),
    failed_reviews_pending=24,unique_prior_reviews_pending=24,cohort_nonaccepted_jobs=2,
    cohort_deferred_jobs=2,original_cohort_historical_deferred_metrics=31,
    historical_unattempted_new_jobs_before_accessible_first_pass_recovery=4,unattempted_new_jobs=0,
    native_retry_attempts_not_terminal_deferred_jobs=True,
    no_new_recovery_claimed_on_queue_presence=True,counts_scope='Original3122 pending24; prior78943 deferred45; stale41583 pending70; overlap-adjusted known union106. Native58195 retry attempts have no terminal metric.')
old_cch='review-construction-habitation-LEGIARTI000046123749-00001'
if old_cch not in d['verified_freshly_recovered_original_jobs']:d['verified_freshly_recovered_original_jobs'].append(old_cch)
data[names[5]].update(proof=control,last_checked_at_utc=now,
    validation=str(R/'global-reference-audit-20261023T2044Z/validation.json'),
    concurrent_capture_preflight=str(R/'global-reference-audit-20261023T2044Z/preflight.json'),
    current_storage_check=str(OUT/'next-audit-storage-budget.json'),next_capture_budget=str(OUT/'next-audit-storage-budget.json'),
    available_free_bytes=budget['free_bytes'],available_free_gib=budget['free_gib'],current_wal_bytes=budget['wal_bytes'],
    next_capture_admissible_at_observation=False,refresh_still_due=False,additional_treatments_since_new_audit_baseline=238,
    new_baseline_postlaunch_reviewed_articles=3604,canonical_writes_continue=False,
    current58195_successful_writes_attested=False,pipeline_remains_active=True,
    semantic_reviews_guarded_against_new_snapshot=False,semantic_reviews_requiring_new_review=['L1242-2','CVAE'],
    formal_semantic_reviews_still_not_redeclared_applicable=True,no_new_snapshot_launched=True)
# Replace the ambiguous historical current-state fields with a fresh incident
# pointer; its complete former bytes and historical resolution remain reachable.
data[names[6]]=dict(folder=str(OUT),state='native_routing_timeout_and_replacement_startup_delays',
    coordinator_pid=58195,last_checked_at_utc=o['at_utc'],diagnostic=str(OUT/'native-retry-diagnostic.json'),
    report=control,previous_resolved_incident=read(OUT/('before-'+names[6])),
    current_attempt_number=2,current_native_processes=8,current_actual_native_responses=0,
    historical_current_pid_eight_response_confirmation=wave,
    current_first_accepted_review_pending=True,general_recovery_not_attested=True,
    no_auth_quota_cause_established=True,no_general_disk_network_or_deadlock_cause_established=True,
    no_manual_signal_launch_retry_reset_pause_code_policy_or_admission_change=True,
    runner_bounded_native_retry_policy_unchanged=True,monitor_active=True,notification_sent=True)
for n in names:data[n]['previous_pointer_preserved']=str(OUT/('before-'+n))
intent=dict(at_utc=now,metadata_only=True,global_audit_pointer_unchanged=True,
    changes=[dict(pointer=n,before_sha256=sha(before[n]),after_sha256=sha(encoded(data[n]))) for n in names])
put('pointer-update-intent.json',intent)
assert (R/'global-reference-audit-latest.json').read_bytes()==audit_before
assert (R/'exhaustive/job-metrics.jsonl').read_bytes()==metrics_before
for n in names:
    p=R/n;tmp=p.with_name(p.name+'.heartbeat-0108.tmp');b=encoded(data[n])
    with tmp.open('xb') as f:f.write(b);f.flush();os.fsync(f.fileno())
    assert p.read_bytes()==before[n],n
    os.replace(tmp,p);assert p.read_bytes()==b
put('pointer-updates.json',intent|{'published':True})
assert (R/'global-reference-audit-latest.json').read_bytes()==audit_before
print(json.dumps(dict(published=len(names),global_audit_pointer_unchanged=True),ensure_ascii=False))
