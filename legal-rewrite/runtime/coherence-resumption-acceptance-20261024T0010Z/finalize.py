"""Seal only the coherence-prompt rollout after the exact current two-launch proof.

No coordinator, pause, policy, admission, source or canonical article is changed.
An incomplete prior metadata publication refuses rather than being overwritten.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,sys,time
sys.dont_write_bytecode=True
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1];R=ROOT/'runtime'
ROLLOUT=R/'coherence-rollout-20261023T2042Z'
WAVE=R/'coherence-current-policy-response-confirmation-20261024T0004Z'
def sha(b):return hashlib.sha256(b).hexdigest()
def encoded(o):return (json.dumps(o,ensure_ascii=False,indent=2)+'\n').encode()
def read(p):return json.loads(p.read_bytes())
def put_new(p,o):
    with p.open('xb') as f:f.write(encoded(o));f.flush();os.fsync(f.fileno())
def verify_manifest(folder,name,expected):
    p=folder/name;b=p.read_bytes()
    if sha(b)!=expected:raise ValueError('Prepared evidence manifest changed')
    for n,item in json.loads(b)['files'].items():
        b=(folder/n).read_bytes()
        if len(b)!=item['bytes'] or sha(b)!=item['sha256']:raise ValueError('Evidence differs: '+n)

def finalize(preparation_sha):
    verify_manifest(OUT,'preparation-manifest.json',preparation_sha)
    verify_manifest(ROLLOUT,'preparation-manifest.json','02ce2af5585aab80e698f5efd02be9e8a38b114e024f39153092d82e2f47d8e9')
    verify_manifest(WAVE,'artifact-manifest.json','7d74d53f8295a51bbc9d36fbb554a852e2ce55a1f4f496dc16e4b46be0f40266')
    if (ROLLOUT/'RESOLUTION.json').exists() or (ROLLOUT/'artifact-manifest.json').exists():
        raise ValueError('A prior final publication exists: inspect its exact state, never overwrite')
    sys.path.insert(0,str(OUT))
    from observe_v2 import observe
    from finalization_gate import require_complete
    proof=observe(accept=True)
    wave=read(WAVE/'eight-native-responses.json')
    require_complete(proof,wave,time.time())
    # Recheck the actual retained native prefixes, not just cached status flags.
    for item in wave['responders']:
        log=Path(item['execution']['source_log']);b=log.read_bytes()[:item['log_prefix_bytes']]
        if sha(b)!=item['log_prefix_sha256']:raise ValueError('Native response prefix changed')
        job=R/'exhaustive/jobs'/item['job']
        if read(job/'policy.json')!=read(ROOT/'site-summaries.json') or read(job/'coordination.json')!=read(ROOT/'policy-coordinations.json'):
            raise ValueError('Attested native wave policies are no longer current')
    pins=read(ROLLOUT/'resumption-observation-pins-v4.json')|{'run_exhaustive.py':'d826aac7dbd43e5e07538d07a9bbf770bbb732842352424456ffd19067898802'}
    for n,h in pins.items():
        if sha((ROOT/n).read_bytes())!=h:raise ValueError('Unknown code/policy difference: '+n)
    if (R/'supervision/disabled').exists():raise ValueError('Unexpected pause')
    audit_b=(R/'global-reference-audit-latest.json').read_bytes();audit=json.loads(audit_b)
    if Path(audit['folder']).name!='global-reference-audit-20261023T2044Z':raise ValueError('Global audit changed: re-evaluate baseline')
    if audit['audit_id']!='b8e5f14afb9810ccbdb390e0966565f219ac3640e58e849628483afba9bc67a7':raise ValueError('Global audit identity differs')
    basis=read(Path(audit['folder'])/'pre-capture-progress.json')['treatment_count_basis']
    metrics_b=(R/'exhaustive/job-metrics.jsonl').read_bytes()
    if not metrics_b.endswith(b'\n') or sha(metrics_b[:basis['metrics_prefix_bytes']])!=basis['metrics_prefix_sha256']:
        raise ValueError('Actual metric prefix changed')
    suffix=[json.loads(x) for x in metrics_b[basis['metrics_prefix_bytes']:].splitlines()]
    if {m['coordinator_pid'] for m in suffix}-{78943,41583,58195}:raise ValueError('Unknown coordinator in baseline suffix')
    additional=sum(m['articles'] for m in suffix if m['outcome'] in {'accepted','reviewed'})
    work_b=(R/'radical-review-20261019.json').read_bytes();rows=read(R/'radical-review-20261019.json')['prior_articles']
    if len(rows)!=30314 or any(a['review_status'] not in {'completed','pending'} for a in rows):raise ValueError('Current worklist scope/status differs')
    complete=sum(a['review_status']=='completed' for a in rows);pending=len(rows)-complete
    if (R/'radical-review-20261019.json').read_bytes()!=work_b:raise ValueError('Worklist changed during final progress capture')
    now=datetime.now(timezone.utc).isoformat()
    summary=dict(at_utc=now,coordinator_pid=58195,current_completed=complete,current_pending=pending,
        actual_treatments_after_audit_prefix=additional,refresh_due=additional>=1000,
        accepted_review_jobs_fully_confronted=len(proof['accepted_reviews']),
        accepted_review_articles_fully_confronted=sum(len(x['rows']) for x in proof['accepted_reviews']),
        current_native_processes_at_capture=proof['native_process_count'],
        current_native_responses_at_capture=proof['actual_current_distinct_native_responses'],
        native_capture_at_utc=proof['at_utc'],eight_distinct_new_responses_attested_at_utc=wave['at_utc'],
        old41583_refusals_freshly_recovered_with_full_proof=proof['actual_fresh_recoveries_of_41583'],
        capacity_is_not_throughput_or_constant_headcount=True,
        completed_is_not_absence_of_contradictions=True,global_legal_completion=False)
    resolution=dict(at_utc=now,state='COHERENCE_PRIORITY_CURRENT_POLICIES_TWO_LAUNCH_CONTINUATION_AND_ACCEPTED_REVIEW_VERIFIED',
        original_pid=78943,first_resumed_pid=41583,current_pid=58195,
        exact_supervised_launch_history_since_initial_pause_release=[41583,58195],
        old41583_actual_exit=proof['old_exit_receipt'],old41583_successful_articles=0,
        old41583_stale_policy_jobs=8,old41583_stale_policy_articles=70,
        only_installed_file_by_rollout='run_exhaustive.py',installed_sha256=pins['run_exhaustive.py'],
        original_preparation_manifest_sha256='02ce2af5585aab80e698f5efd02be9e8a38b114e024f39153092d82e2f47d8e9',
        finalizer_preparation_folder=str(OUT),finalizer_preparation_sha256=preparation_sha,
        exact_installed_runner_and77_current_pins_verified=True,
        concurrent_reviewed_presentation_and_formal_policy_grammar_changes_preserved=True,
        all_policies_unchanged_from_original_snapshot=False,
        old_limited_semantic_review_inheritance_not_forced=True,
        owned_pause_previously_released_no_new_pause=True,
        no_signal_manual_launch_code_policy_admission_or_canonical_mutation_by_finalizer=True,
        eight_native_wave=str(WAVE/'CONTROL.json'),eight_native_wave_manifest_sha256='7d74d53f8295a51bbc9d36fbb554a852e2ce55a1f4f496dc16e4b46be0f40266',
        full_current_native_and_acceptance_proof='current-policy-acceptance-proof.json',current_progress=summary,
        prior_full_reconciliation=str(ROLLOUT/'run/reconciliation.json'),
        prior_reconciliation_is_dated_not_a_fresh_global_reconciliation=True,
        global_validated_audit=str(audit['folder']),global_audit_pointer_unchanged=True,
        documentary_reserves_unverified=3,monitor_remains_active=True,
        previous_three_CCH_CRL_candidates_not_registered=str(R/'coherence-coordination-guarded-preparation-20261023T221149Z/CONTROL.json'),
        five_cross_border_candidates_not_registered=str(R/'cross-border-ordinary-preparation-20261024T0005Z/CONTROL.json'),
        all_remaining_passes_sources_convergence_priority_qualifications_and_fresh_final_audit_required=True,
        global_legal_completion=False,semantic_review_by_jurist=False)
    names=['coherence-rollout-latest.json','second-pass-coherence-human-directive-latest.json','second-pass-parallelism-latest.json','completion-coverage-latest.json','deferred-recovery-latest.json','audit-refresh-deferred.json']
    before={n:(R/n).read_bytes() for n in names};data={n:json.loads(b) for n,b in before.items()}
    for n,b in before.items():
        with (ROLLOUT/('before-final-current-policy-'+n)).open('xb') as f:f.write(b);f.flush();os.fsync(f.fileno())
    resolution_path=str(ROLLOUT/'RESOLUTION.json')
    data[names[0]].update(phase=resolution['state'],resolution=resolution_path,new_pid=58195,
        accepted_review_still_required=False,first_new_accepted_review_verification_pending=False,
        native_responses_and_new_review_still_required=False,native_responses_and_accepted_review_still_required=False,
        current_phase_native_and_accepted_review_still_required=False,
        actual_priority_in_native_inputs_verified=True,eight_distinct_native_responses_verified=True,
        latest_observation=resolution_path,last_observed_at_utc=now,resumption_finalizer_not_executed=False)
    data[names[1]].update(state='coherence_priority_current_policies_native_and_accepted_review_verified',
        latest_observation=resolution_path,rollout_resolution=resolution_path,current_coordinator_pid=58195,
        accepted_review_verification_complete=True,native_response_verification_complete=True,
        first_new_accepted_review_verification_pending=False)
    data[names[2]].update(state='current_guarded_review_tail_native_responses_and_accepted_review_verified',
        pid=58195,stage='review_tail',active_role_limits={'new':0,'review':8},execution_verified=True,
        current_execution_proof=resolution_path,latest_operational_observation=summary,
        current_responding_distinct_sessions_at_observation=proof['actual_current_distinct_native_responses'],
        new_coordinator_acceptance_verified=True,performance_gain_measured=False)
    data[names[3]].update(latest_read_only_progress_check=summary,last_checked_at_utc=now)
    data[names[4]].update(coordinator_pid=58195,current_native_responses_verified=True,current_execution_proof=resolution_path,
        last_checked_at_utc=now,latest_accepted_review_proof=resolution_path,
        identity_dispositions_need_current_refresh=True,no_recovery_claim_on_queue_presence=True)
    data[names[5]].update(proof=resolution_path,coordinator_pid=58195,
        additional_treatments_since_new_audit_baseline=additional,refresh_still_due=additional>=1000,
        no_new_snapshot_launched=True)
    for n,d in data.items():d['previous_pointer_preserved']=str(ROLLOUT/('before-final-current-policy-'+n))
    intent=dict(at_utc=now,changes=[dict(pointer=n,before_sha256=sha(before[n]),after_sha256=sha(encoded(data[n]))) for n in names],
        metadata_only=True,global_audit_pointer_unchanged=True)
    put_new(ROLLOUT/'final-current-policy-pointer-intent.json',intent)
    if (R/'global-reference-audit-latest.json').read_bytes()!=audit_b:raise ValueError('Global audit intervened before metadata publication')
    put_new(ROLLOUT/'current-policy-acceptance-proof.json',proof)
    put_new(ROLLOUT/'current-policy-final-observation.json',summary)
    put_new(ROLLOUT/'RESOLUTION.json',resolution)
    for n,d in data.items():
        p=R/n;tmp=p.with_name(p.name+'.current-policy-final.tmp');b=encoded(d)
        with tmp.open('xb') as f:f.write(b);f.flush();os.fsync(f.fileno())
        if p.read_bytes()!=before[n]:raise ValueError('Intervening metadata write: '+n)
        os.replace(tmp,p)
        if p.read_bytes()!=b:raise ValueError('Published monitoring metadata differs')
    put_new(ROLLOUT/'final-current-policy-pointer-updates.json',intent|{'published':True})
    paths=sorted(p for p in ROLLOUT.rglob('*') if p.is_file())
    files={str(p.relative_to(ROLLOUT)):dict(bytes=p.stat().st_size,sha256=sha(p.read_bytes())) for p in paths}
    if paths!=sorted(p for p in ROLLOUT.rglob('*') if p.is_file()):raise ValueError('Rollout evidence membership changed during sealing')
    put_new(ROLLOUT/'artifact-manifest.json',dict(files=files,closed_at_utc=now,
        original_preparation_manifest_sha256=resolution['original_preparation_manifest_sha256'],
        finalizer_preparation_sha256=preparation_sha,rollout_only_completion=True,global_legal_completion=False))
    return dict(resolution=resolution_path,manifest_sha256=sha((ROLLOUT/'artifact-manifest.json').read_bytes()),progress=summary)

if __name__=='__main__':
    if len(sys.argv)!=3 or sys.argv[1]!='--preparation-sha':raise ValueError('Explicit reviewed preparation manifest hash required')
    print(json.dumps(finalize(sys.argv[2]),ensure_ascii=False))
