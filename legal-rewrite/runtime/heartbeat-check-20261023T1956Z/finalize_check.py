"""Seal operational/semantic evidence; update monitoring pointers only."""
from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,math,os,shutil
OP=Path(__file__).resolve().parent;ROOT=OP.parents[1];R=ROOT/'runtime'
A=R/'global-reference-audit-20261023T1908Z'
F=R/'cvae-semantic-recheck-20261023T1956Z'
PREP=R/'coherence-prompt-preparation-20261023T1956Z'
def sha(b):return hashlib.sha256(b).hexdigest()
def file_sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()
def read(p):return json.loads(p.read_text())
def save(n,d):
    with (OP/n).open('x') as f:json.dump(d,f,ensure_ascii=False,indent=2);f.write('\n')
now=datetime.now(timezone.utc).isoformat();pointer=read(R/'global-reference-audit-latest.json')
assert pointer['audit_id']=='384c85d78606cdafab4c33a86b86533004b1ba9ee0a1006779014a07ce0351f6'
assert file_sha(A/'artifact-manifest.json')=='5e97ad0862115a41ee9725e22fca4f93104e6aded55a75b201e85581c9b771e3'
assert file_sha(ROOT/'run_exhaustive.py')=='91e898776c7619b89461928010c02f8cd49141745473dcdefbdfd5f6f65c3e40'
assert file_sha(PREP/'artifact-manifest.json')=='1f5c1180bb7d9df01a89f51a8d2a2dc4f4cfe0a1af6fe3384b41b34ce9876ef2'
assert file_sha(F/'artifact-manifest.json')=='c3fd1e986393502b893657cd5ae5b301dd9bf544a6c51da37620fc3f882c069d'
template=Path(pointer['refresh_validator_template']);assert file_sha(template)==pointer['refresh_validator_template_sha256']
tree=ast.parse(template.read_text());function=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='guarded_review_origins')
space=dict(Path=Path,file_sha=file_sha)
exec(compile(ast.Module(body=[function],type_ignores=[]),str(template),'exec'),space)
origins=space['guarded_review_origins'](read(A/'semantic-review-inheritance.json'),pointer)
assert origins['CVAE']==F
manifest={x['key']:x for x in map(json.loads,(A/'article-manifest.jsonl').open())}
final=read(F/'final-state-check.json');capture=read(A/'capture.json')
assert len(final['articles'])==18
assert all(all(manifest[k][n]==v for n,v in x['current_guard'].items()) for k,x in final['articles'].items())
assert all(x['current_sha256']==capture['policies'][n]['sha256'] for n,x in final['policies'].items())
save('fresh-origin-template-compatibility.json',dict(checked_at_utc=now,unchanged_template_sha256=file_sha(template),real_origin_resolver_function_used_read_only=True,CVAE_origin=str(origins['CVAE']),all18_snapshot_guards_match=True,all_four_policy_guards_match=True,published_audit_files_modified=False,full_validator_not_replayed=True))
save('next-safe-drain-design.json',dict(candidate=str(PREP),installed=False,active_runner_sha256=file_sha(ROOT/'run_exhaustive.py'),
    scheduler_behavior_verified='review_lanes.completed_futures defers unattempted queues when fresh role limit is0 and lets active futures finish; no signal is necessary to drain.',
    supported_control='review_tail_limit0 under manual-agent-slots.lock, preservingworkers8/explicitnew6review0 and known manual reservations.',
    required_before_actual_drain=['Prepare and review a NEW guarded installer/controller with isolated tests, never replay old install_once/activate/adopter.','Fresh unique coordinator identity/birth, LaunchAgent, source/policy/code/control/manual guards.','Owned supervisor pause created under lock with durable intention and exact bytes; never touch a foreign pause.'],
    required_after_natural_exit=['Actual currentPID exit receipt tied to last live birth and known absent descendants/exporters.','Current full technical reconciliation under supervisor/coordinator/writer/manual locks, never hold writer while waiting.','Install only reviewed runner literal change with durable beforeimage/intention and exact pins; restore guarded review_tail8.','Existing supervisor performs exactly one continuation; attest new native Astra/Medium responses and a real accepted review before releasing only owned pause.'],
    stage='CANDIDATE_VERIFIED_CONTROLLER_AND_REAL_SAFE_POINT_STILL_REQUIRED',human_reconfirmation_required=False,no_pause_admission_change_or_signal_performed=True))
obs=read(OP/'final-observation.json');basis=read(A/'pre-capture-progress.json')['treatment_count_basis']
assert obs['audit_baseline_metrics_prefix_verified'] and obs['audit_additional_treatments_since_current_validated_baseline']<1000
free=shutil.disk_usage(ROOT).free;wal=ROOT/'corpus.sqlite-wal';wal_bytes=wal.stat().st_size if wal.exists() else 0
foot=sum(e['bytes'] for e in read(A/'artifact-manifest.json')['files']);snap=(A/'corpus.snapshot.sqlite').stat().st_size
estimate=(ROOT/'corpus.sqlite').stat().st_size+math.ceil((foot-snap)*1.15)
required=9*2**30+max(0,estimate-read(A/'preflight.json')['previous_concurrent_footprint_bytes'])+wal_bytes
budget=dict(at_utc=now,free_bytes=free,free_gib=free/2**30,wal_bytes=wal_bytes,estimated_next_audit_footprint_bytes=estimate,required_free_bytes=required,required_gib=required/2**30,capture_admissible=free>=required,refresh_due=False,actual_treatments_after_pinned_prefix=obs['audit_additional_treatments_since_current_validated_baseline'],new_snapshot_created=False,reestimate_before_next_capture=True)
save('next-audit-storage-budget.json',budget)
summary=dict(checked_at_utc=obs['checked_at_utc'],coordinator_pid=78943,canonical_identities=30317,accessible_first_passes_registered=30314,accessible_first_passes_open=0,documentary_holds_unverified=3,complete_worklist_entries=30314,current_completed=obs['completed'],current_pending=obs['pending'],postlaunch_reviewed_jobs=obs['postlaunch_reviewed_jobs'],postlaunch_reviewed_articles=obs['postlaunch_reviewed_articles'],postlaunch_outcomes=obs['postlaunch_outcomes'],original_nonaccepted_review_jobs_still_pending=obs['original_nonaccepted_review_jobs_current_pending'],original_nonaccepted_review_articles_still_pending=obs['original_nonaccepted_review_articles_current_pending'],current_tail_deferred_jobs=obs['current_tail_deferred_jobs'],current_tail_deferred_articles=obs['current_tail_deferred_articles'],unique_original_and_current_deferred_reviews_pending=obs['unique_original_and_current_deferred_reviews_pending'],current_validated_audit=str(A),current_validated_audit_id=pointer['audit_id'],additional_treatments_since_current_audit_baseline=budget['actual_treatments_after_pinned_prefix'],audit_baseline_metrics_prefix_verified=True,audit_due=False,new_snapshot_created=False,next_capture_admissible=budget['capture_admissible'],next_capture_required_gib=budget['required_gib'],native_processes_at_capture=obs['native_processes'],distinct_responding_sessions_at_capture=obs['native_responding_distinct_sessions'],free_bytes=free,free_gib=free/2**30,storage_observed_at_utc=now,wal_bytes=wal_bytes,supervision_pause_exists=obs['supervision_pause_exists'],no_legal_completion_or_throughput_gain_claimed=True,scope='One fresh10-article CSS review and all45 current deferred whole sources/NOTA/boundaries/five unchanged beforeimage fields independently checked read-only; not a fresh reconciliation of all404 accepted jobs. Separate18article limited semantic review does not increment reviewed counters.')
save('current-observation.json',summary)
save('source-followup.json',dict(at_utc=now,documentary_holds_unverified=3,new_official_facsimile_obtained=False,new_search_claimed=False,source_NOTA_or_companion_changed=False,CAPTCHA_or_third_party_message=False,scope='This control focused on fresh semantic review, not a new documentary retrieval.'))
evidence={n:dict(bytes=(OP/n).stat().st_size,sha256=file_sha(OP/n)) for n in ['final-observation.json','observe-final.py','final-observation.log']}
save('observation-artifact-manifest.json',dict(files=evidence))
names=['completion-coverage-latest.json','deferred-recovery-latest.json','second-pass-parallelism-latest.json','audit-refresh-deferred.json','second-pass-coherence-human-directive-latest.json']
before={n:(R/n).read_bytes() for n in names}
for n,b in before.items():(OP/('before-'+n)).write_bytes(b)
data={n:json.loads(b) for n,b in before.items()}
data['completion-coverage-latest.json'].update(latest_read_only_progress_check=summary,last_checked_at_utc=now,latest_current_audit=str(A),first_pass_covered=30314,pending_first_pass=3)
data['deferred-recovery-latest.json'].update(last_checked_at_utc=now,latest_disposition=summary,current_disposition_proof=str(OP/'final-observation.json'),current_native_worker_count=obs['native_processes'],current_responding_native_count=obs['native_responding_distinct_sessions'],native_execution_verified_at_utc=obs['checked_at_utc'],latest_current_review_failure_diagnostic=str(OP/'final-observation.json'),latest_current_review_failure_manifest=str(OP/'observation-artifact-manifest.json'),latest_current_review_failure_manifest_sha256=file_sha(OP/'observation-artifact-manifest.json'))
data['second-pass-parallelism-latest.json'].update(latest_operational_observation=summary,latest_native_execution_proof=str(OP/'final-observation.json'),latest_native_execution_observed_at_utc=obs['checked_at_utc'],current_responding_distinct_sessions_at_observation=obs['native_responding_distinct_sessions'])
data['audit-refresh-deferred.json'].update(last_checked_at_utc=now,additional_treatments_since_new_audit_baseline=budget['actual_treatments_after_pinned_prefix'],current_storage_check=str(OP/'next-audit-storage-budget.json'),available_free_bytes=free,available_free_gib=free/2**30,current_wal_bytes=wal_bytes,semantic_reviews_requiring_new_review=[],fresh_limited_CVAE_review=str(F),fresh_CVAE_origin_manifest_sha256=file_sha(F/'artifact-manifest.json'),CVAE_other_scopes_and_global_semantic_review_remain_open=True)
data['second-pass-coherence-human-directive-latest.json'].update(latest_semantic_followup=str(F),latest_semantic_followup_manifest_sha256=file_sha(F/'artifact-manifest.json'),fresh_scope='13CVAE articles plus5counterparties, limited no effectiveCVAE inconsistency established; no global qualification.',prepared_runner_candidate=str(PREP),prepared_candidate_manifest_sha256=file_sha(PREP/'artifact-manifest.json'),candidate_installed=False,safe_drain_design=str(OP/'next-safe-drain-design.json'),priority_effectively_injected_in_active_worker_sessions=False)
updates=[]
for n,d in data.items():
    d['previous_pointer_preserved']=str(OP/('before-'+n));p=R/n;b=(json.dumps(d,ensure_ascii=False,indent=2)+'\n').encode();t=p.with_name(p.name+'.1956.tmp')
    with t.open('xb') as f:f.write(b);f.flush();os.fsync(f.fileno())
    assert p.read_bytes()==before[n],f'Intervening monitoring pointer update: {n}'
    os.replace(t,p);assert p.read_bytes()==b
    updates.append(dict(pointer=str(p),before_sha256=sha(before[n]),after_sha256=sha(b)))
save('pointer-updates.json',dict(at_utc=now,atomic_updates=updates,published_audit_files_untouched=True))
(OP/'REPORT.md').write_text('''# Contrôle et priorité de cohérence

Une vraie relecture sémantique a été menée sur13textesCVAE complets et5contreparties : sept situations historiques qualifiées de nouveau,18gardes/fourpolitiques vérifiées. Aucune contradiction CVAE effective n'est établie dans ce seul périmètre. Le nouvel override sous manifeste reprend les limites et ne clôt ni les autresP1 ni les coordinations extérieures. QuatreP1 actuels sont homologuesCVAE ; huit autresP1 du groupe restent hors qualification globale. Les fichiers publiés de l'audit1908Z sont intacts.

Le relevé final à20:05:10UTC constate78943 seul, LaunchAgent enregistré, sept processus natifs et sept réponses distinctesAstra/Moyen ; ce sont des comptes datés.404lots/3039articles reviewed sont observés,4081completed/26233pending sur30314. Un lotCSS de10articles est confronté aux cinqchamps, sourcesentières/NOTA/bornes, propriétaire/registre/archiveentière/completed. Ce n'est pas une réconciliation de toutes les acceptations ni autant de simplifications.

Quatre différés courants/45identités et trois anciens lots/36 restent pending :81identités uniques, avant-images/sources/refus préservés. Le préfixe de l'audit1908Z est vérifié ;749traitements réels supplémentaires, seuil1000non atteint. Aucune nouvelle capture ou opération de nettoyage. Les trois réserves documentaires restent non vérifiées ; aucune nouvelle récupération n'est revendiquée.

La priorité humaine est désormais traduite dans un candidat concret : un seul littéral du prompt de seconde passe est remplacé, AST inchangé ailleurs, compilation réussie. Le candidatd826… est NON INSTALLÉ. Le scheduler existant permet de fermer les admissionsreview avec review_tail_limit0 et de différer la queue non tentée en laissant finir les actifs. Il faut terminer un nouveau contrôleur gardé et ses tests avant de conduire ce drainage naturel, la réconciliation actuelle et une seule reprise supervisée. Aucune pause, modification d'admissions, installation, relance ou signal n'a été effectué ici. Les sessions en cours ne sont pas réputées avoir reçu rétroactivement cette priorité.

La revue fraîche est une avancée limitée et ne prouve aucune cohérence juridique globale ou validation humaine. Le suivi reste actif jusqu'à toutes les passes, sources, coordinations et qualifications prioritaires puis audit final frais.
''')
save('CONTROL-SUMMARY.json',dict(at_utc=now,current_progress=summary,CVAE_fresh_limited_review=str(F),CVAE_manifest_sha256=file_sha(F/'artifact-manifest.json'),CVAE_override_published=True,priority_runner_candidate=str(PREP),candidate_installed=False,technical_and_source_guards_preserved=True,global_legal_completion=False,monitor_remains_active=True))
files={p.name:dict(bytes=p.stat().st_size,sha256=file_sha(p)) for p in sorted(OP.iterdir()) if p.is_file()}
save('artifact-manifest.json',dict(files=files,external_CVAE_manifest_sha256=file_sha(F/'artifact-manifest.json'),external_prompt_preparation_manifest_sha256=file_sha(PREP/'artifact-manifest.json')))
print(json.dumps(dict(folder=str(OP),manifest_sha256=file_sha(OP/'artifact-manifest.json'),free_gib=free/2**30,current_CVAE_origin=str(F),prompt_candidate_installed=False)))
