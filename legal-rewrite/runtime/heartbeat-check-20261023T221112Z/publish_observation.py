"""Publish monitoring metadata only, preserving every prior pointer."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,os
OUT=Path(__file__).resolve().parent;R=OUT.parent
def sha(b):return hashlib.sha256(b).hexdigest()
def enc(o):return (json.dumps(o,ensure_ascii=False,indent=2)+'\n').encode()
def read(p):return json.loads(p.read_bytes())
summary=read(OUT/'CONTROL.json');disposition=read(OUT/'current-dispositions.json');budget=read(OUT/'next-audit-storage-budget.json')
names=['coherence-rollout-latest.json','second-pass-coherence-human-directive-latest.json','second-pass-parallelism-latest.json','completion-coverage-latest.json','deferred-recovery-latest.json','audit-refresh-deferred.json']
before={n:(R/n).read_bytes() for n in names};data={n:json.loads(b) for n,b in before.items()}
for n,b in before.items():
    with (OUT/('before-'+n)).open('xb') as f:f.write(b)
proof=str(OUT/'CONTROL.json')
data[names[0]].update(phase=summary['state'],new_pid=41583,latest_observation=proof,
    first_new_accepted_review_verification_pending=True,accepted_review_still_required=True,
    native_responses_and_accepted_review_still_required=True,
    actual_frozen_policy_refusals_verified=True,resumption_finalizer_not_executed=True)
data[names[1]].update(state='installed_coherence_priority_frozen_policy_results_refused_fresh_continuation_required',
    accepted_review_verification_complete=False,first_new_accepted_review_verification_pending=True,
    latest_observation=proof,actual_frozen_policy_refusals_verified=True,
    no_retroactive_policy_acceptance_or_response_replay=True)
data[names[2]].update(state='supervised_review_tail_installed_stale_policy_results_refused',pid=41583,
    latest_operational_observation=summary,latest_native_execution_proof=str(OUT/'current-native-and-process.json'),
    latest_native_execution_observed_at_utc=summary['native_capture_at_utc'],
    current_responding_distinct_sessions_at_observation=summary['actual_native_responders_in_dated_capture'],
    new_coordinator_acceptance_verified=False)
data[names[3]].update(first_pass_covered=30314,pending_first_pass=3,
    last_checked_at_utc=summary['at_utc'],latest_read_only_progress_check=summary)
data[names[4]].update(coordinator_pid=41583,last_checked_at_utc=summary['at_utc'],
    latest_disposition=disposition,current_disposition_proof=str(OUT/'current-dispositions.json'),
    original_nonaccepted_review_articles_current_pending=disposition['original_pending'],
    previous_coordinator_deferred_articles_current_pending=disposition['previous_deferred_pending'],
    current_coordinator_terminal_nonaccepted_pending=disposition['current_nonaccepted_terminal_pending'],
    unique_original_and_current_deferred_reviews_pending=disposition['prior_known_union_pending'],
    unique_all_known_terminal_nonaccepted_pending=disposition['unique_all_known_terminal_nonaccepted_pending'],
    original_cch_recovery_freshly_verified=str(OUT/'original-cch-review-recovery.json'),
    no_response_replay_or_registration_by_control=True,
    counts_scope='Separate prior deferred union and current stale-policy terminal union; no subtraction across worklists and no recovery claim on queue presence.')
data[names[5]].update(state='current_audit_valid_refresh_not_due_prospective_storage_below_budget',
    proof=proof,additional_treatments_since_new_audit_baseline=summary['additional_treatments_after_audit_prefix'],
    refresh_still_due=False,available_free_bytes=budget['free_bytes'],available_free_gib=budget['free_gib'],
    current_wal_bytes=budget['wal_bytes'],coordinator_pid=41583,
    next_capture_budget=str(OUT/'next-audit-storage-budget.json'),
    next_capture_admissible_at_observation=budget['capture_admissible'],
    minimum_free_bytes_during_writers=9*2**30,no_new_snapshot_launched=True)
changes=[]
for n,d in data.items():
    d['previous_pointer_preserved']=str(OUT/('before-'+n));p=R/n;b=enc(d)
    tmp=p.with_name(p.name+'.heartbeat-221112Z.tmp')
    with tmp.open('xb') as f:f.write(b);f.flush();os.fsync(f.fileno())
    assert p.read_bytes()==before[n],n
    os.replace(tmp,p);assert p.read_bytes()==b
    changes.append(dict(pointer=n,before_sha256=sha(before[n]),after_sha256=sha(b)))
with (OUT/'pointer-updates.json').open('xb') as f:f.write(enc(dict(changes=changes,global_audit_pointer_sources_articles_policies_and_admissions_not_modified=True)))
files={str(p.relative_to(OUT)):dict(bytes=p.stat().st_size,sha256=sha(p.read_bytes())) for p in sorted(OUT.iterdir()) if p.is_file()}
with (OUT/'artifact-manifest.json').open('xb') as f:f.write(enc(dict(files=files,closed_at_utc=datetime.now(timezone.utc).isoformat(),no_global_legal_completion=True)))
print(json.dumps(dict(folder=str(OUT),manifest_sha256=sha((OUT/'artifact-manifest.json').read_bytes()),files=len(files)),ensure_ascii=False))
