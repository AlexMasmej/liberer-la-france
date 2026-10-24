"""Publish dated monitoring facts, with durable before-images and CAS checks."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os
OUT=Path(__file__).resolve().parent;R=OUT.parent
def sha(b):return hashlib.sha256(b).hexdigest()
def enc(o):return (json.dumps(o,ensure_ascii=False,indent=2)+'\n').encode()
def read(p):return json.loads(p.read_bytes())
def put(n,o):
    with (OUT/n).open('xb') as f:f.write(enc(o));f.flush();os.fsync(f.fileno())
audit=(R/'global-reference-audit-latest.json').read_bytes();metrics=(R/'exhaustive/job-metrics.jsonl').read_bytes()
current=[json.loads(x) for x in metrics.splitlines() if json.loads(x).get('coordinator_pid')==58195]
assert not any(x['outcome'] in {'accepted','reviewed'} for x in current),'First complete accepted verification now required'
c=read(OUT/'CONTROL.json');o=read(OUT/'final-native-and-process.json');b=read(OUT/'next-audit-storage-budget.json');storage=read(OUT/'final-storage-observation.json')
assert current==o['current_metrics'] and o['current_successful_articles']==0
assert not (R/'coherence-rollout-20261023T2042Z/RESOLUTION.json').exists()
names=['coherence-rollout-latest.json','second-pass-coherence-human-directive-latest.json','second-pass-parallelism-latest.json',
       'completion-coverage-latest.json','deferred-recovery-latest.json','audit-refresh-deferred.json','network-incident-latest.json']
before={n:(R/n).read_bytes() for n in names};data={n:json.loads(v) for n,v in before.items()}
for n,v in before.items():
    with (OUT/('before-'+n)).open('xb') as f:f.write(v);f.flush();os.fsync(f.fileno())
now=datetime.now(timezone.utc).isoformat();control=str(OUT/'CONTROL.json');proof=str(OUT/'final-native-and-process.json');wave=str(OUT/'native-and-process.json')
data[names[0]].update(phase='CURRENT_NATIVE_RESPONSES_AND_VALIDATION_PENDING_FIRST_ACCEPTANCE_ABSENT',latest_observation=control,
    last_observed_at_utc=o['at_utc'],latest_response_confirmation=wave,current_native_process_count=o['native_process_count'],
    current_native_response_count=o['actual_current_distinct_native_responses'],current_attempt_number=None,
    current_attempts_at_0211_capture={'first_wave_third':6,'fresh_next_jobs_first':2},
    latest_native_retry_diagnostic=str(OUT/'native-and-terminal-diagnostic.json'),current_attempt_response_verified=True,
    current_deferred_jobs=len(current),current_deferred_articles=sum(x['articles'] for x in current),
    accepted_review_still_required=True,resumption_finalizer_not_executed=True)
data[names[1]].update(state='coherence_priority_current_policy_native_responses_verified_first_acceptance_pending',
    latest_observation=control,latest_response_confirmation=wave,native_response_verification_complete=True,
    current_native_response_count=o['actual_current_distinct_native_responses'],accepted_review_verification_complete=False,
    guarded_nine_candidate_global_ordinary_preflight=c['new_guarded_nine_candidate_global_preflight'],
    guarded_nine_candidate_global_ordinary_preflight_manifest_sha256=c['new_guarded_nine_candidate_global_preflight_manifest_sha256'],
    unregistered_parent_candidates_total=9,no_new_semantic_reread_from_guard_refresh=True)
data[names[2]].update(state='guarded_review_tail_native_responses_validation_pending',execution_verified=True,
    current_execution_proof=proof,latest_native_execution_proof=proof,latest_native_execution_observed_at_utc=o['at_utc'],
    current_physical_process_proof=proof,latest_operational_observation=c,
    current_responding_distinct_sessions_at_observation=o['actual_current_distinct_native_responses'],
    current_native_processes_at_observation=o['native_process_count'],dated_eight_responses_at_0211=wave,
    last_checked_at_utc=now,new_coordinator_acceptance_verified=False,performance_gain_measured=False)
data[names[3]].update(latest_read_only_progress_check=c,last_checked_at_utc=now)
data[names[4]].update(state='known_pending_including_two_current_terminal_deferrals',current_execution_proof=proof,
    current_resumption_proof=control,current_native_responses_verified=True,
    current_responding_native_count=o['actual_current_distinct_native_responses'],current_native_worker_count=o['native_process_count'],
    native_execution_verified_at_utc=o['at_utc'],current_disposition_proof=str(OUT/'current-dispositions.json'),
    latest_disposition=read(OUT/'current-dispositions.json'),last_checked_at_utc=now,
    latest_current_review_failure_diagnostic=str(OUT/'native-and-terminal-diagnostic.json'),
    current_coordinator_terminal_nonaccepted_pending=13,current_coordinator_terminal_deferred_jobs=2,
    latest_validation_guard_refusals=str(OUT/'new-validation-refusals.json'),
    current_native_response_does_not_resolve_terminal_deferrals=True)
data[names[5]].update(proof=control,last_checked_at_utc=now,
    current_storage_check=str(OUT/'final-storage-observation.json'),next_capture_budget=str(OUT/'next-audit-storage-budget.json'),
    available_free_bytes=int(storage['free_gib']*2**30),available_free_gib=storage['free_gib'],current_wal_bytes=storage['wal_bytes'],
    refresh_still_due=False,additional_treatments_since_new_audit_baseline=238,next_capture_admissible_at_observation=False,
    current58195_successful_writes_attested=False,no_new_snapshot_launched=True)
data[names[6]].update(folder=str(OUT),state='new_native_responses_attested_first_complete_accepted_work_still_absent',
    last_checked_at_utc=o['at_utc'],diagnostic=str(OUT/'native-and-terminal-diagnostic.json'),report=control,
    current_attempt_number=None,current_native_processes=o['native_process_count'],
    current_actual_native_responses=o['actual_current_distinct_native_responses'],
    dated_eight_current_policy_responses_at_0211=wave,terminal_deferred_jobs=2,terminal_deferred_articles=13,
    current_first_accepted_review_pending=True,general_recovery_not_attested=True,notification_sent=True)
for n in names:data[n]['previous_pointer_preserved']=str(OUT/('before-'+n))
intent=dict(at_utc=now,metadata_only=True,global_audit_pointer_unchanged=True,
    changes=[dict(pointer=n,before_sha256=sha(before[n]),after_sha256=sha(enc(data[n]))) for n in names])
put('pointer-update-intent.json',intent)
assert (R/'global-reference-audit-latest.json').read_bytes()==audit and (R/'exhaustive/job-metrics.jsonl').read_bytes()==metrics
for n in names:
    p=R/n;tmp=p.with_name(p.name+'.heartbeat-0210.tmp');v=enc(data[n])
    with tmp.open('xb') as f:f.write(v);f.flush();os.fsync(f.fileno())
    assert p.read_bytes()==before[n],n
    os.replace(tmp,p);assert p.read_bytes()==v
put('pointer-updates.json',intent|{'published':True})
assert (R/'global-reference-audit-latest.json').read_bytes()==audit
print(json.dumps(dict(published=7,global_audit_pointer_unchanged=True),ensure_ascii=False))
