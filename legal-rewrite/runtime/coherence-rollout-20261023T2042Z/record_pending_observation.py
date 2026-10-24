"""Record a truthful pending checkpoint; never relax the acceptance finalizer."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,shutil,subprocess,sys
sys.dont_write_bytecode=True
WORK=Path(__file__).resolve().parent;ROOT=WORK.parents[1];R=ROOT/'runtime'
sys.path.insert(0,str(ROOT))
import supervise_exhaustive as supervisor
def sha(b):return hashlib.sha256(b).hexdigest()
def fsha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()
def read(p):return json.loads(p.read_text())
def encoded(d):return (json.dumps(d,ensure_ascii=False,indent=2)+'\n').encode()
now=datetime.now(timezone.utc);OUT=R/('coherence-rollout-observation-'+now.strftime('%Y%m%dT%H%M%SZ'));OUT.mkdir()
def put(name,d):(OUT/name).write_bytes(encoded(d))
rows=supervisor.processes();live=supervisor.coordinator_processes(rows)
assert len(live)==1 and live[0]['pid']==41583
run=read(R/'exhaustive/coordinator-run.json');phase=read(R/'exhaustive/continuation-phase.json')
assert run['pid']==41583 and phase['coordinator_pid']==41583 and phase['phase']=='review_tail'
assert phase['effective_limits']=={'workers':8,'role_limits':{'new':0,'review':8}}
assert not (R/'supervision/disabled').exists()
assert fsha(ROOT/'run_exhaustive.py')=='d826aac7dbd43e5e07538d07a9bbf770bbb732842352424456ffd19067898802'
launchctl=subprocess.run(['/bin/launchctl','print',f'gui/{os.getuid()}/com.libererfrance.exhaustive-rewrite'],capture_output=True,text=True,timeout=20)
assert launchctl.returncode==0
(OUT/'launchagent.txt').write_text(launchctl.stdout)
pins=read(WORK/'resumption-observation-pins-v3.json')|{'run_exhaustive.py':fsha(ROOT/'run_exhaustive.py')}
drifts=[dict(file=n,expected=h,observed=fsha(ROOT/n)) for n,h in pins.items() if fsha(ROOT/n)!=h]
for drift in drifts:
    b=(ROOT/drift['file']).read_bytes();assert sha(b)==drift['observed']
    (OUT/('unreviewed-current-'+drift['file'].replace('/','__'))).write_bytes(b)
put('current-pin-differences.json',dict(at_utc=now.isoformat(),differences=drifts,no_pin_forced=True))
native=[]
for w in supervisor.job_workers(rows):
    if w['ppid']!=41583:continue
    e=w['execution'];log=Path(e['source_log']);b=log.read_bytes();assert log.read_bytes()[:len(b)]==b
    native.append(dict(pid=w['pid'],job=w['job'],execution=e,log_prefix_bytes=len(b),log_prefix_sha256=sha(b),new_priority_in_native_input='SECONDE PASSE — PRIORITÉ HUMAINE DU23OCTOBRE2026' in b.decode(errors='replace')))
put('native-sessions.json',native)
headers=[x for x in native if x['execution'].get('model')=='gpt-6-astra' and x['execution'].get('reasoning_effort')=='medium' and x['execution'].get('session_id') and x['new_priority_in_native_input']]
initial=read(WORK/'first-eight-native-instruction-headers.json')
assert initial['coordinator_pid']==41583 and initial['eight_distinct_headers_and_priority_verified']
for item in initial['sessions']:
    log=R/'exhaustive/jobs'/item['job']/'errors-1.log'
    assert sha(log.read_bytes()[:item['prefix_bytes']])==item['prefix_sha256']
pointer=read(R/'global-reference-audit-latest.json');audit=Path(pointer['folder']);assert audit.name=='global-reference-audit-20261023T2044Z'
baseline=read(audit/'pre-capture-progress.json')['treatment_count_basis'];metricbytes=(R/'exhaustive/job-metrics.jsonl').read_bytes()
assert metricbytes.endswith(b'\n') and sha(metricbytes[:baseline['metrics_prefix_bytes']])==baseline['metrics_prefix_sha256']
metrics=[json.loads(x) for x in metricbytes.splitlines()]
suffix=[json.loads(x) for x in metricbytes[baseline['metrics_prefix_bytes']:].splitlines()]
assert {x['coordinator_pid'] for x in suffix}<={78943,41583}
additional=sum(x['articles'] for x in suffix if x['outcome'] in {'accepted','reviewed'})
newmetrics=[x for x in metrics if x.get('coordinator_pid')==41583];newsuccess=[x for x in newmetrics if x['outcome'] in {'accepted','reviewed'}]
workbytes=(R/'radical-review-20261019.json').read_bytes();work= json.loads(workbytes)
keys={(x['code_id'],x['source_id']):x for x in work['prior_articles']};assert len(keys)==30314
complete=sum(x['review_status']=='completed' for x in keys.values());pending=sum(x['review_status']=='pending' for x in keys.values());assert complete+pending==30314
oldjobs=['review-construction-habitation-LEGIARTI000046123749-00001','review-urbanisme-LEGIARTI000031211073-00002','review-urbanisme-LEGIARTI000042017888-00001']
oldpending=set();failpending=set();dispositions=[]
for name in oldjobs:
    src=read(R/'exhaustive/jobs'/name/'source.json');still={(x['code_id'],x['source_id']) for x in src if keys[x['code_id'],x['source_id']]['review_status']=='pending'};oldpending|=still;dispositions.append(dict(cohort='original3122',job=name,currently_pending=len(still)))
for m in metrics:
    if m.get('coordinator_pid') not in {78943,41583} or m['outcome']!='deferred':continue
    src=read(R/'exhaustive/jobs'/m['job']/'source.json');still={(x['code_id'],x['source_id']) for x in src if keys[x['code_id'],x['source_id']]['review_status']=='pending'};failpending|=still;dispositions.append(dict(cohort=m['coordinator_pid'],job=m['job'],currently_pending=len(still)))
assert (R/'radical-review-20261019.json').read_bytes()==workbytes
try:walbytes=(ROOT/'corpus.sqlite-wal').stat().st_size;walabsent=False
except FileNotFoundError:walbytes=0;walabsent=True
summary=dict(at_utc=now.isoformat(),coordinator_pid=41583,registered_launchagent=True,only_one_coordinator=True,phase=phase['phase'],effective_limits=phase['effective_limits'],native_processes_in_dated_capture=len(native),distinct_actual_headers_with_new_priority=len(headers),actual_native_response_starts=sum(x['execution'].get('response_started',False) for x in native),new_coordinator_successful_jobs=len(newsuccess),new_coordinator_successful_articles=sum(x['articles'] for x in newsuccess),new_coordinator_metrics=newmetrics,first_pass_registered_accessible=30314,canonical_identities=30317,documentary_holds_unverified=3,second_pass_completed=complete,second_pass_pending=pending,pending_original_review_identities=len(oldpending),pending_failed_review_identities=len(failpending),pending_union=len(oldpending|failpending),pending_dispositions=dispositions,actual_treatments_after_current_audit_prefix=additional,current_validated_audit=str(audit),current_validated_audit_id=pointer['audit_id'],audit_due=additional>=1000,metrics_prefix_verified=True,free_bytes=shutil.disk_usage(ROOT).free,WAL_bytes=walbytes,WAL_absent=walabsent,unreviewed_pin_differences=drifts,formal_site_summary_policy_hash_changed=True,grammar_change_review=str(WORK/'concurrent-site-summaries-grammar-review.json'),native_headers_not_counted_as_responses=True,no_new_accepted_review_proven_by_parent=True,no_throughput_gain_or_global_legal_completion_claimed=True)
put('current-observation.json',summary)
files=['REVIEW.md','preparation-manifest.json','baseline-pins.json','tests.json','inventory-tests.json','concurrent-presentation-change-review.json','concurrent-presentation-change-review-v2.json','concurrent-site-summaries-grammar-review.json','first-eight-native-instruction-headers.json','l1242-fresh-coherence-followup.json','l1242-whole-fifteen-packet.json','l2411-cross-border-counterparts.json','cvae-fresh-eighteen-coherence-followup.json','cvae-whole-eighteen-packet.json','cch-financing-followup-qualified.json','cch-financing-coordination-candidate.json','fiscal-coherence-followup-and-candidate.json','semantic-extra-live-guard-check.json','source-followup.json','verify_resumption.py','finalize_resolution.py','record_pending_observation.py','run/installed.json','run/installation-intent.json','run/pause-released.json','run/queue-disposition.json','run/reconciliation.json']
external=[]
for n in files:
    p=WORK/n;external.append(dict(path=str(p),bytes=p.stat().st_size,sha256=fsha(p)))
put('external-evidence.json',external)
control=dict(at_utc=now.isoformat(),state='INSTALLED_EIGHT_NATIVE_INSTRUCTIONS_VERIFIED_RESPONSE_AND_ACCEPTANCE_PENDING',rollout=str(WORK),resume_installed_steps_must_not_be_replayed=True,priority_on_all_five_codes_and_four_annexes=True,summary=summary,only_file_installed_by_this_control='run_exhaustive.py',pause_released=True,complete_reconciliation_before_release=str(WORK/'run/reconciliation.json'),twenty_isolated_tests_passed=True,global_finalizer_not_run_because_responses_and_acceptance_not_verified=True,old_published_semantic_review_inheritance_not_forced=True,parent_full_reads=dict(travail_group=15,additional_travail_counterparts=2,CVAE_group_and_counterparts=18,CCH_financing=3),parent_prepared_canonical_corrections_registered=0,next_actions=['Continue actual native response/accepted-review verification; no extra launch or signal.','Review any intervening pin difference exactly in a new observation; do not force original sealed pins or revert another change.','Complete acceptance finalizer only after eight distinct real responses and a fresh accepted review are proved.','Keep prepared CCH/CRL and cross-border coordinations open for ordinary guarded integration; whole corpus remains required.','Re-anchor limited semantic work only after all current article and four-policy guards, including changed site-summaries grammar, have been confronted.'],monitor_remains_active=True,legal_completion=False,jurist_validation=False)
put('CONTROL.json',control)
(OUT/'REPORT.md').write_text('''# Point de suivi — priorité transmise, réponses encore à attester

La consigne orientée contradictions et renvois incohérents est installée sur les cinq codes et les quatre annexes. Huit sessions natives distinctes Astra/Moyen l’ont reçue. La réception des instructions ne prouve pas un début de réponse ni un résultat accepté : voir les nombres exacts et datés de current-observation.json.

Le coordinateur précédent a fini naturellement ses lots puis ses publications. Le rapprochement complet a réussi avant le remplacement du seul littéral de consigne et le retrait de notre pause strictement possédée. Une seule reprise supervisée est constatée. Les étapes achevées ne doivent pas être rejouées.

Le parent a relu quinze textes du groupe L1242-2 et deux contreparties, les dix-huit textes du groupe CVAE et trois textes CCH financiers. Les qualifications limitées, les réserves et trois corrections concrètes préparées sont conservées. Aucune correction canonique parentale n’a été enregistrée pendant les lots actifs, aucun compteur de seconde passe n’est augmenté par ces lectures.

Des ajouts de crédits dans les pages et trois changements de grammaire de site-summaries.json sont intervenus séparément. Les comparaisons exactes déjà revues sont préservées ; toute différence supplémentaire reste explicitement bloquante pour l’attestation intégrale. La modification du hash d’une des quatre politiques ne rajeunit aucun ancien héritage sémantique, même si les changements revus sont grammaticaux. Sources, propositions et contrôles juridiques ne sont pas modifiés par cette observation.

L’audit global 2044Z reste le seul validé et non compressé. Les différés, trois réserves documentaires, coordinations prioritaires, autres secondes passes et audit final frais restent ouverts. Suivi actif ; aucune clôture globale ni validation par juriste.
''')
names=['coherence-rollout-latest.json','second-pass-coherence-human-directive-latest.json','second-pass-parallelism-latest.json','completion-coverage-latest.json','deferred-recovery-latest.json','audit-refresh-deferred.json'];before={n:(R/n).read_bytes() for n in names};data={n:json.loads(b) for n,b in before.items()}
for n,b in before.items():(OUT/('before-'+n)).write_bytes(b)
data[names[0]].update(phase=control['state'],new_pid=41583,latest_observation=str(OUT/'CONTROL.json'),owned_pause_released=True,actual_priority_in_native_inputs_verified=True,native_responses_and_accepted_review_still_required=True)
data[names[1]].update(state='installed_eight_native_instructions_verified_responses_pending',candidate_installed=True,installed_runner_sha256=fsha(ROOT/'run_exhaustive.py'),new_coordinator_pid=41583,priority_effectively_injected_in_active_worker_sessions=True,native_response_verification_complete=False,accepted_review_verification_complete=False,latest_observation=str(OUT/'CONTROL.json'),fresh_parental_semantic_work=str(OUT/'external-evidence.json'))
data[names[2]].update(pid=41583,active_runner_sha256=fsha(ROOT/'run_exhaustive.py'),latest_operational_observation=summary,current_responding_distinct_sessions_at_observation=summary['actual_native_response_starts'],latest_native_execution_observed_at_utc=now.isoformat(),coherence_priority_installed=True,latest_native_execution_proof=str(OUT/'native-sessions.json'))
data[names[3]].update(first_pass_covered=30314,pending_first_pass=3,last_checked_at_utc=now.isoformat(),latest_current_audit=str(audit),latest_read_only_progress_check=summary)
data[names[4]].update(coordinator_pid=41583,last_checked_at_utc=now.isoformat(),latest_disposition=summary,current_disposition_proof=str(OUT/'current-observation.json'),unique_original_and_current_deferred_reviews_pending=len(oldpending|failpending),original_nonaccepted_review_articles_current_pending=len(oldpending),current_tail_deferred_articles=len(failpending),no_old_response_replay=True,no_new_recovery_claimed_on_queue_presence=True)
data[names[5]].update(state='refresh_validated_resolved',current_validated_audit=str(audit),current_audit_id=pointer['audit_id'],current_snapshot_sha256=pointer['snapshot_sha256'],proof=str(OUT/'CONTROL.json'),additional_treatments_since_new_audit_baseline=additional,refresh_still_due=additional>=1000,new_baseline_metric_proof=str(audit/'pre-capture-progress.json'),new_baseline=baseline,next_refresh_after_additional_treatments=1000,current_audit_kept_uncompressed=True,minimum_free_bytes_during_writers=9*2**30,reestimate_budget_if_footprint_or_WAL_grows=True,available_free_bytes=summary['free_bytes'],current_wal_bytes=walbytes,coordinator_pid=41583,formal_semantic_reviews_still_not_redeclared_applicable=True)
changes=[]
for n,d in data.items():
    d['previous_pointer_preserved']=str(OUT/('before-'+n));b=encoded(d);target=R/n;tmp=target.with_name(target.name+'.coherence-observation.tmp')
    with tmp.open('xb') as f:f.write(b);f.flush();os.fsync(f.fileno())
    assert target.read_bytes()==before[n]
    os.replace(tmp,target);changes.append(dict(pointer=n,before_sha256=sha(before[n]),after_sha256=sha(b)))
put('pointer-updates.json',changes)
manifest={str(p.relative_to(OUT)):dict(bytes=p.stat().st_size,sha256=fsha(p)) for p in sorted(OUT.iterdir()) if p.is_file()};put('artifact-manifest.json',dict(files=manifest,external_evidence=external,rollout_finalizer_still_guarded=True))
print(json.dumps(dict(folder=str(OUT),manifest_sha256=fsha(OUT/'artifact-manifest.json'),native_responses=summary['actual_native_response_starts'],new_successful_articles=summary['new_coordinator_successful_articles'],unreviewed_pin_differences=drifts,state=control['state']),ensure_ascii=False))
