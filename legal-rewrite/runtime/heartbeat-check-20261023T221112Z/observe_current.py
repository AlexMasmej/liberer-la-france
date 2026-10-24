"""Read-only observation of rejected frozen policy and preserved fresh work."""
from pathlib import Path
from datetime import datetime, timezone
import copy, hashlib, json, math, os, shutil, subprocess, sys
sys.dont_write_bytecode = True
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
R = ROOT / 'runtime'
WORK = R / 'coherence-rollout-20261023T2042Z'
sys.path.insert(0, str(WORK))
from verify_resumption import observed

def sha(b): return hashlib.sha256(b).hexdigest()
def enc(o): return (json.dumps(o, ensure_ascii=False, indent=2)+'\n').encode()
def put(name, o):
    with (OUT/name).open('xb') as f: f.write(enc(o))
def read(p): return json.loads(p.read_bytes())
def fsha(p): return sha(p.read_bytes())

pid, pins, process = observed()
assert pid == 41583
put('current-native-and-process.json', process)
launchctl = subprocess.run(['/bin/launchctl','print',f'gui/{os.getuid()}/com.libererfrance.exhaustive-rewrite'],
                           capture_output=True, text=True, timeout=20)
assert launchctl.returncode == 0
(OUT/'launchagent.txt').write_text(launchctl.stdout)
old = read(R/'coherence-response-confirmation-20261023T220040Z/eight-native-responses.json')
initial = old['responders']
current_policy_bytes = (ROOT/'site-summaries.json').read_bytes()
current_policy = json.loads(current_policy_bytes)
coordination = read(ROOT/'policy-coordinations.json')
grammar = read(WORK/'concurrent-site-summaries-grammar-review.json')
assert sha(current_policy_bytes) == grammar['current_sha256']
frozen = []
for item in initial:
    d = R/'exhaustive/jobs'/item['job']
    b = (d/'policy.json').read_bytes()
    policy = json.loads(b)
    reconstructed = copy.deepcopy(policy)
    for change in grammar['changes']:
        parts = change['path'].strip('/').split('/')
        parent = reconstructed
        for part in parts[:-1]: parent = parent[int(part)] if isinstance(parent,list) else parent[part]
        key = int(parts[-1]) if isinstance(parent,list) else parts[-1]
        assert isinstance(parent[key],str) and parent[key].count(change['exact_before']) == 1
        parent[key] = parent[key].replace(change['exact_before'],change['exact_after'])
    assert reconstructed == current_policy
    assert read(d/'coordination.json') == coordination
    if not (OUT/'frozen-policy-first-wave.json').exists(): (OUT/'frozen-policy-first-wave.json').write_bytes(b)
    stale = d/'stale-policy.json'
    if stale.exists(): (OUT/('captured-stale-policy-'+item['job']+'.json')).write_bytes(stale.read_bytes())
    log = Path(item['execution']['source_log']); content = log.read_bytes()
    assert log.read_bytes()[:len(content)] == content
    frozen.append(dict(job=item['job'], policy_sha256=sha(b),
        current_policy_equal=False, coordination_equal=True,
        exact_three_grammar_edits_reconstruct_current_policy=True,
        stale_policy_marker=read(stale) if stale.exists() else None,
        log_prefix_bytes=len(content), log_prefix_sha256=sha(content),
        log_last_modified_utc=datetime.fromtimestamp(log.stat().st_mtime,timezone.utc).isoformat(),
        answer_exists=(d/'answer.json').exists(), result_exists=(d/'result.json').exists()))
put('frozen-policy-difference.json', dict(at_utc=datetime.now(timezone.utc).isoformat(),
    all_eight_frozen_policies_differ_only_by_three_reviewed_grammar_edits=True,
    attribution_of_other_changes_author_not_established=True,
    no_old_answer_registered_or_replayed_by_control=True, jobs=frozen))
metrics_b = (R/'exhaustive/job-metrics.jsonl').read_bytes()
assert metrics_b.endswith(b'\n')
metrics = [json.loads(x) for x in metrics_b.splitlines()]
current = [m for m in metrics if m.get('coordinator_pid') == pid]
assert not any(m['outcome'] in {'accepted','reviewed'} for m in current), 'Run complete accepted-review check now'
put('current-coordinator-metrics.json', current)
pointer_b = (R/'global-reference-audit-latest.json').read_bytes(); pointer = json.loads(pointer_b)
audit = Path(pointer['folder']); assert audit.name == 'global-reference-audit-20261023T2044Z'
basis = read(audit/'pre-capture-progress.json')['treatment_count_basis']
assert sha(metrics_b[:basis['metrics_prefix_bytes']]) == basis['metrics_prefix_sha256']
suffix = [json.loads(x) for x in metrics_b[basis['metrics_prefix_bytes']:].splitlines()]
assert {m['coordinator_pid'] for m in suffix} <= {78943,pid}
additional = sum(m['articles'] for m in suffix if m['outcome'] in {'accepted','reviewed'})
work_b = (R/'radical-review-20261019.json').read_bytes()
rows = {(a['code_id'],a['source_id']):a for a in json.loads(work_b)['prior_articles']}
assert len(rows) == 30314
complete = sum(a['review_status']=='completed' for a in rows.values())
pending = sum(a['review_status']=='pending' for a in rows.values()); assert complete+pending == len(rows)
dispositions = []; groups = {'original3122':set(), 'previous78943':set(), 'current41583':set()}
old_jobs = ['review-construction-habitation-LEGIARTI000046123749-00001',
            'review-urbanisme-LEGIARTI000031211073-00002','review-urbanisme-LEGIARTI000042017888-00001']
jobs = [('original3122',n,'historical_nonaccepted') for n in old_jobs]
jobs += [('previous78943',m['job'],m['outcome']) for m in metrics if m.get('coordinator_pid')==78943 and m['outcome']=='deferred']
jobs += [('current41583',m['job'],m['outcome']) for m in current if m['outcome'] not in {'accepted','reviewed'}]
for group, job, outcome in jobs:
    src = read(R/'exhaustive/jobs'/job/'source.json')
    keys = {(a['code_id'],a['source_id']) for a in src}
    remaining = {k for k in keys if rows[k]['review_status']=='pending'}
    groups[group] |= remaining
    dispositions.append(dict(group=group,job=job,outcome=outcome,identities=len(keys),pending=len(remaining)))
assert (R/'radical-review-20261019.json').read_bytes() == work_b
put('current-dispositions.json',dict(jobs=dispositions,original_pending=len(groups['original3122']),
    previous_deferred_pending=len(groups['previous78943']),
    prior_known_union_pending=len(groups['original3122']|groups['previous78943']),
    current_nonaccepted_terminal_pending=len(groups['current41583']),
    unique_all_known_terminal_nonaccepted_pending=len(set.union(*groups.values())),
    no_recovery_claim_from_queue_presence=True,all_other_pending_remain_required=True))
wal = ROOT/'corpus.sqlite-wal'; wal_bytes = wal.stat().st_size if wal.exists() else 0
preflight = read(audit/'preflight.json')
snapshot = audit/'corpus.snapshot.sqlite'
actual = sum((audit/n).stat().st_size for n in ['corpus.snapshot.sqlite','edges.jsonl','findings.jsonl','queue.json'])
non_snapshot = actual-snapshot.stat().st_size
estimate = (ROOT/'corpus.sqlite').stat().st_size + math.ceil(non_snapshot*1.15)
required = 9*2**30 + max(0,estimate-preflight['previous_concurrent_footprint_bytes']) + wal_bytes
free = shutil.disk_usage(ROOT).free
put('next-audit-storage-budget.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),
    free_bytes=free,free_gib=free/2**30,wal_bytes=wal_bytes,
    current_audit_actual_four_large_files_bytes=actual,estimated_next_audit_footprint_bytes=estimate,
    required_free_bytes=required,required_gib=required/2**30,capture_admissible=free>=required,
    refresh_due=additional>=1000,actual_treatments_after_pinned_prefix=additional,
    no_snapshot_launched=True,no_cleanup_performed=True,no_general_storage_cause_established=True,
    reestimate_before_any_actual_capture=True))
preparation = R/'coherence-coordination-guarded-preparation-20261023T221149Z'
assert read(preparation/'CONTROL.json')['ordinary_checks_all_passed']
recovery = read(OUT/'original-cch-review-recovery.json')
assert recovery['current_completed_original_scope'] == 12
summary = dict(at_utc=datetime.now(timezone.utc).isoformat(),coordinator_pid=pid,
    state='STALE_FROZEN_POLICY_RESULTS_REJECTED_NATURAL_SUPERVISED_CONTINUATION_PENDING',
    only_one_coordinator=True,registered_launchagent=True,supervision_pause_exists=False,
    native_workers_in_dated_capture=process['native_workers'],
    actual_native_responders_in_dated_capture=process['native_responding_distinct'],
    native_capture_at_utc=process['checked_at_utc'],
    eight_prior_distinct_native_responses_historical_not_new_acceptance=True,
    new_coordinator_accepted_jobs=0,new_coordinator_accepted_articles=0,
    stale_policy_terminal_jobs=sum(m['outcome']=='stale_policy' for m in current),
    stale_policy_markers=sum(x['stale_policy_marker'] is not None for x in frozen),
    all_eight_frozen_policies_have_exact_reviewed_grammar_drift=True,
    second_pass_completed=complete,second_pass_pending=pending,
    first_pass_accessible_registered=30314,canonical_identities=30317,documentary_holds_unverified=3,
    parent_ordinary_validation_passed_three_candidates_not_registered=str(preparation),
    cch_old_scope_twelve_recovered_by_two_fresh_jobs_verified=str(OUT/'original-cch-review-recovery.json'),
    prior_known_nonaccepted_union_pending=len(groups['original3122']|groups['previous78943']),
    unique_all_known_nonaccepted_terminal_pending=len(set.union(*groups.values())),
    additional_treatments_after_audit_prefix=additional,audit_due=additional>=1000,
    free_gib=free/2**30,wal_bytes=wal_bytes,
    coordinator_sample='One-second sample shows SQLite reads and other threads waiting; no deadlock, network, quota or general disk cause inferred.',
    no_signal_new_pause_launch_code_change_policy_change_or_answer_replay=True,
    resumption_acceptance_finalizer_not_run=True,monitor_remains_active=True,
    next_steps=['Let valid active work finish naturally; keep refusals and source/beforeimage evidence.',
        'Observe actual old-process exit and the existing supervisor continuation; no manual or concurrent launch.',
        'Verify fresh PID/birth/physical interpreter/one supervised continuation, current frozen policies, actual distinct Astra/medium responses with coherence priority, then fully accepted review.',
        'Do not replay the original rollout drain/install/release or call its finalizer with a stale-policy result.',
        'Stage future candidate integration only under fresh ownership, shared reservations, sources/NOTA/versions/whole targets/four policies and full ordinary validation.'],
    no_global_semantic_or_jurist_validation=True)
put('CONTROL.json',summary)
for name,h in pins.items(): assert fsha(ROOT/name)==h, name
assert (R/'global-reference-audit-latest.json').read_bytes()==pointer_b
assert not (R/'supervision/disabled').exists()
put('external-evidence.json', [dict(path=str(p),bytes=p.stat().st_size,sha256=fsha(p)) for p in [
    preparation/'artifact-manifest.json',preparation/'CONTROL.json',WORK/'guarded-finalizer-review.json',
    WORK/'finalize_resolution_guarded.py',WORK/'concurrent-site-summaries-grammar-review.json']])
print(json.dumps(dict(folder=str(OUT),summary=summary),ensure_ascii=False))
