"""Publish dated response and preparation evidence only; no pipeline mutation."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os
OUT=Path(__file__).resolve().parent;R=OUT.parent
def sha(b):return hashlib.sha256(b).hexdigest()
def enc(o):return (json.dumps(o,ensure_ascii=False,indent=2)+'\n').encode()
def read(p):return json.loads(p.read_bytes())
def put(n,d):
    with (OUT/n).open('xb') as f:f.write(enc(d));f.flush();os.fsync(f.fileno())
s=read(OUT/'CONTROL.json');o=read(OUT/'native-and-process.json')
assert o['new_pid']==58195 and o['actual_current_distinct_native_responses']==8
assert o['guarded_phase_matches_current_pid'] and not o['accepted_review_verification_complete']
assert not (R/'coherence-rollout-20261023T2042Z/RESOLUTION.json').exists()
disposition=read(OUT/'current-dispositions.json');budget=read(OUT/'next-audit-storage-budget.json')
names=['coherence-rollout-latest.json','second-pass-coherence-human-directive-latest.json','second-pass-parallelism-latest.json','completion-coverage-latest.json','deferred-recovery-latest.json','audit-refresh-deferred.json']
before={n:(R/n).read_bytes() for n in names};data={n:json.loads(b) for n,b in before.items()}
for n,b in before.items():
    with (OUT/('before-'+n)).open('xb') as f:f.write(b);f.flush();os.fsync(f.fileno())
proof=str(OUT/'CONTROL.json');native=str(OUT/'native-and-process.json')
wave=str(R/'coherence-current-policy-response-confirmation-20261024T0004Z/CONTROL.json')
data[names[0]].update(phase='CURRENT_POLICY_EIGHT_NEW_RESPONSES_FIRST_ACCEPTED_REVIEW_PENDING',
    new_pid=58195,latest_observation=proof,last_observed_at_utc=o['at_utc'],
    actual_priority_in_native_inputs_verified=True,eight_distinct_native_responses_verified=True,
    latest_response_confirmation=wave,current_phase_native_and_accepted_review_still_required=True,
    first_new_accepted_review_verification_pending=True,accepted_review_still_required=True,
    resumption_finalizer_not_executed=True,
    acceptance_verifier_and_finalizer_preparation=s['acceptance_finalizer_preparation'],
    acceptance_verifier_and_finalizer_preparation_sha256=s['acceptance_finalizer_preparation_sha256'])
data[names[1]].update(state='coherence_priority_and_current_policy_new_native_responses_verified_acceptance_pending',
    latest_observation=proof,current_coordinator_pid=58195,native_response_verification_complete=True,
    priority_effectively_injected_in_active_worker_sessions=True,accepted_review_verification_complete=False,
    first_new_accepted_review_verification_pending=True,
    latest_ordinary_checked_five_candidates=s['five_cross_border_ordinary_preparation'],
    latest_ordinary_checked_five_candidates_manifest_sha256=s['five_cross_border_ordinary_manifest_sha256'])
data[names[2]].update(state='guarded_review_tail_eight_actual_responses_current_policy_acceptance_pending',
    pid=58195,stage='review_tail',active_role_limits={'new':0,'review':8},execution_verified=True,
    current_execution_proof=wave,current_physical_process_proof=native,
    latest_native_execution_proof=native,latest_native_execution_observed_at_utc=o['at_utc'],
    current_responding_distinct_sessions_at_observation=8,new_coordinator_acceptance_verified=False,
    latest_operational_observation=s,performance_gain_measured=False)
data[names[3]].update(last_checked_at_utc=s['at_utc'],latest_read_only_progress_check=s,
    first_pass_coverage_full_inventory_is_prior_dated_evidence=True)
data[names[4]].update(coordinator_pid=58195,last_checked_at_utc=s['at_utc'],current_native_responses_verified=True,
    current_execution_proof=wave,current_disposition_proof=str(OUT/'current-dispositions.json'),latest_disposition=disposition,
    actual_fresh_native_assignments_of_old_refused_scope=str(OUT/'new-first-wave-assignment.json'),
    fresh_native_assignment_not_acceptance=True,unique_all_known_terminal_nonaccepted_pending=106,
    no_recovery_claim_on_queue_presence=True,no_response_replay_or_registration_by_control=True)
data[names[5]].update(proof=proof,coordinator_pid=58195,
    additional_treatments_since_new_audit_baseline=s['additional_successful_treatments_after_audit_prefix'],
    refresh_still_due=False,available_free_bytes=budget['free_bytes'],available_free_gib=budget['free_gib'],
    current_wal_bytes=budget['wal_bytes'],next_capture_budget=str(OUT/'next-audit-storage-budget.json'),
    next_capture_admissible_at_observation=budget['capture_admissible'],minimum_free_bytes_during_writers=9*2**30,
    no_new_snapshot_launched=True)
for n,d in data.items():d['previous_pointer_preserved']=str(OUT/('before-'+n))
changes=[dict(pointer=n,before_sha256=sha(before[n]),after_sha256=sha(enc(data[n]))) for n in names]
put('pointer-update-intent.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),changes=changes,monitoring_metadata_only=True))
for n,d in data.items():
    p=R/n;tmp=p.with_name(p.name+'.heartbeat-20261024T0016Z.tmp');b=enc(d)
    with tmp.open('xb') as f:f.write(b);f.flush();os.fsync(f.fileno())
    assert p.read_bytes()==before[n],n
    os.replace(tmp,p);assert p.read_bytes()==b
put('pointer-updates.json',dict(changes=changes,global_audit_pointer_sources_articles_policies_admissions_not_modified=True))
files={str(p.relative_to(OUT)):dict(bytes=p.stat().st_size,sha256=sha(p.read_bytes())) for p in sorted(OUT.iterdir()) if p.is_file()}
put('artifact-manifest.json',dict(files=files,closed_at_utc=datetime.now(timezone.utc).isoformat(),
    no_accepted_resumption_yet=True,no_global_legal_completion=True))
print(json.dumps(dict(folder=str(OUT),manifest_sha256=sha((OUT/'artifact-manifest.json').read_bytes()),files=len(files)),ensure_ascii=False))
