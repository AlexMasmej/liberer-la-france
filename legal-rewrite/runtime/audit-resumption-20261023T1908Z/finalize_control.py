"""Verify published evidence and update only mutable monitoring pointers."""
from pathlib import Path
from datetime import datetime, timezone
import gzip, hashlib, json, math, os, shutil

OP = Path(__file__).resolve().parent
ROOT = OP.parents[1]
R = ROOT / 'runtime'
AUDIT = R / 'global-reference-audit-20261023T1908Z'
OLD = R / 'global-reference-audit-20261023T1557Z'
CVAE = R / 'cvae-guard-change-followup-20261023T1912Z'

def sha(b): return hashlib.sha256(b).hexdigest()
def file_sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()
def load(p): return json.loads(p.read_text())
def write(p,d):
    with p.open('x') as f: json.dump(d,f,ensure_ascii=False,indent=2);f.write('\n')

now=datetime.now(timezone.utc).isoformat()
pointer_bytes=(R/'global-reference-audit-latest.json').read_bytes()
pointer=json.loads(pointer_bytes)
publication=load(AUDIT/'pointer-update.json')
assert pointer['audit_id']=='384c85d78606cdafab4c33a86b86533004b1ba9ee0a1006779014a07ce0351f6'
assert sha(pointer_bytes)==publication['pointer_sha256']
assert file_sha(AUDIT/'artifact-manifest.json')==publication['artifact_manifest_sha256']
manifest=load(AUDIT/'artifact-manifest.json')
for entry in manifest['files']:
    p=AUDIT/entry['path']
    assert p.stat().st_size==entry['bytes'] and file_sha(p)==entry['sha256'],entry['path']
assert file_sha(AUDIT/'corpus.snapshot.sqlite')==pointer['snapshot_sha256']
validation=load(AUDIT/'validation.json')
assert validation['checks_passed'] and not validation['errors']
assert validation['semantic_reviews_requiring_new_review']==['CVAE']

archive_checks=[]
assert file_sha(OLD/'artifact-manifest.json')=='ff6b32be8ebc200511e042c66cfbf11c7cf42a76f7dfaeb67655852acea172d1'
for item in load(OLD/'storage-data-archives.json')['files']:
    p=OLD/item['archive_name']
    assert p.stat().st_size==item['compressed_bytes'] and file_sha(p)==item['gzip_sha256']
    h=hashlib.sha256();size=0
    with gzip.open(p,'rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b);size+=len(b)
    assert h.hexdigest()==item['original_sha256'] and size==item['original_bytes']
    assert not (OLD/item['original_name']).exists()
    archive_checks.append(dict(file=str(p),original_sha256_verified=h.hexdigest(),uncompressed_bytes_verified=size,full_decompression_verified=True))
assert len(archive_checks)==4
assert (AUDIT/'corpus.snapshot.sqlite').exists() and not (AUDIT/'corpus.snapshot.sqlite.gz').exists()
write(OP/'published-audit-and-archives-verification.json',dict(at_utc=now,published_manifest_sha256=publication['artifact_manifest_sha256'],all_published_manifest_files_rehashed=True,snapshot_sha256=pointer['snapshot_sha256'],four_old_archives_independently_decompressed=archive_checks,current_audit_uncompressed=True))

obs=load(OP/'post-publication-observation.json')
assert obs['current_validated_audit_id']==pointer['audit_id']
basis=load(AUDIT/'pre-capture-progress.json')['treatment_count_basis']
metrics=(R/'exhaustive/job-metrics.jsonl').read_bytes()
assert sha(metrics[:basis['metrics_prefix_bytes']])==basis['metrics_prefix_sha256']
wal=ROOT/'corpus.sqlite-wal';wal_bytes=wal.stat().st_size if wal.exists() else 0
free=shutil.disk_usage(ROOT).free
audit_footprint=sum((AUDIT/e['path']).stat().st_size for e in manifest['files'])
snapshot_bytes=(AUDIT/'corpus.snapshot.sqlite').stat().st_size
live_bytes=(ROOT/'corpus.sqlite').stat().st_size
prior_footprint=load(AUDIT/'preflight.json')['previous_concurrent_footprint_bytes']
estimate=live_bytes+math.ceil(max(0,audit_footprint-snapshot_bytes)*1.15)
required=9*2**30+max(0,estimate-prior_footprint)+wal_bytes
budget=dict(at_utc=now,free_bytes=free,free_gib=free/2**30,required_free_bytes=required,required_gib=required/2**30,base_concurrent_floor_bytes=9*2**30,estimated_next_audit_footprint_bytes=estimate,wal_bytes=wal_bytes,output_growth_allowance_fraction=0.15,capture_admissible=free>=required,refresh_due=False,reestimate_before_next_capture=True)
write(OP/'post-archive-storage.json',budget)

summary=dict(checked_at_utc=obs['checked_at_utc'],coordinator_pid=78943,canonical_identities=30317,
    accessible_first_passes_registered=30314,accessible_first_passes_open=0,documentary_holds_unverified=3,
    complete_worklist_entries=30314,current_completed=obs['completed'],current_pending=obs['pending'],
    postlaunch_reviewed_jobs=obs['postlaunch_reviewed_jobs'],postlaunch_reviewed_articles=obs['postlaunch_reviewed_articles'],
    postlaunch_outcomes=obs['postlaunch_outcomes'],original_nonaccepted_review_jobs_still_pending=obs['original_nonaccepted_review_jobs_current_pending'],
    original_nonaccepted_review_articles_still_pending=obs['original_nonaccepted_review_articles_current_pending'],
    current_tail_deferred_jobs=obs['current_tail_deferred_jobs'],current_tail_deferred_articles=obs['current_tail_deferred_articles'],
    unique_original_and_current_deferred_reviews_pending=obs['unique_original_and_current_deferred_reviews_pending'],
    current_validated_audit=str(AUDIT),current_validated_audit_id=pointer['audit_id'],
    additional_treatments_since_current_audit_baseline=obs['audit_additional_treatments_since_current_validated_baseline'],
    audit_baseline_metrics_prefix_verified=True,audit_due=False,new_snapshot_created=True,
    next_capture_admissible=budget['capture_admissible'],next_capture_required_gib=budget['required_gib'],
    native_processes_at_capture=obs['native_processes'],distinct_responding_sessions_at_capture=obs['native_responding_distinct_sessions'],
    free_bytes=free,free_gib=free/2**30,storage_observed_at_utc=now,wal_bytes=wal_bytes,
    supervision_pause_exists=obs['supervision_pause_exists'],no_legal_completion_or_throughput_gain_claimed=True,
    scope='Operational observation and one accepted article independently verified against whole source/NOTA/versions, all five response/batch/DB fields, registry and full archived beforeimage/completed. All45 current deferred article sources and five unchanged beforeimage fields checked read-only. Not a fresh global reconciliation of all acceptances or a legal certification.')
write(OP/'current-observation.json',summary)
resolution=dict(at_utc=now,state='fresh_global_audit_validated_published_old_audit_archived',
    audit_id=pointer['audit_id'],audit_folder=str(AUDIT),audit_manifest_sha256=publication['artifact_manifest_sha256'],
    snapshot_sha256=pointer['snapshot_sha256'],published_at_utc=publication['at_utc'],
    full_technical_validation_passed=True,semantic_reviews_requiring_new_review=['CVAE'],
    cvae_followup=str(CVAE),cvae_followup_manifest_sha256=file_sha(CVAE/'artifact-manifest.json'),
    L1242_limited_review_still_applicable=True,CVAE_full_fresh_review_complete=False,
    former_audit_archived=str(OLD),verified_saved_bytes=sum(x['original_bytes']-x['compressed_bytes'] for x in load(OLD/'storage-data-archives.json')['files']),
    current_storage=budget,current_progress=summary,new_baseline=basis,
    no_installation_adoption_relaunch_pause_signal_or_canonical_source_mutation=True,
    native_execution_count_is_dated_observation_only=True,monitor_remains_active=True,global_legal_completion=False)
write(OP/'RESOLUTION.json',resolution)

names=['audit-refresh-deferred.json','completion-coverage-latest.json','deferred-recovery-latest.json','second-pass-parallelism-latest.json']
before={n:(R/n).read_bytes() for n in names}
for n,b in before.items(): (OP/('before-'+n)).write_bytes(b)
updated={n:json.loads(b) for n,b in before.items()}
updated['audit-refresh-deferred.json']=dict(state='refresh_validated_resolved',resolved_at_utc=publication['at_utc'],
    last_checked_at_utc=now,current_validated_audit=str(AUDIT),current_audit_id=pointer['audit_id'],current_snapshot_sha256=pointer['snapshot_sha256'],
    proof=str(OP/'RESOLUTION.json'),validation=str(AUDIT/'validation.json'),new_snapshot_created=True,
    concurrent_capture_preflight=str(AUDIT/'preflight.json'),current_audit_kept_uncompressed=True,previous_audit_archived_losslessly=True,
    saved_bytes_verified=resolution['verified_saved_bytes'],available_free_bytes=free,available_free_gib=free/2**30,current_wal_bytes=wal_bytes,
    coordinator_pid=78943,canonical_writes_continue=True,source_policy_control_or_model_changed=False,refresh_still_due=False,
    additional_treatments_since_new_audit_baseline=summary['additional_treatments_since_current_audit_baseline'],
    next_refresh_after_additional_treatments=1000,new_baseline_metric_proof=str(AUDIT/'pre-capture-progress.json'),
    new_baseline_postlaunch_reviewed_articles=basis['postpublication_reviewed_articles'],new_baseline=basis,
    count_rule='Count actual accepted/reviewed articles after new pinned prefix; include later verified PIDs, never subtract completed counters from different worklists.',
    minimum_free_bytes_during_writers=9*2**30,minimum_free_bytes_otherwise=6*2**30,reestimate_budget_if_footprint_or_WAL_grows=True,
    previous_deferred_record=str(OP/'before-audit-refresh-deferred.json'),notification='User informed once in the current space-resumption turn; do not repeat if unchanged.',
    semantic_reviews_guarded_against_new_snapshot=True,semantic_reviews_requiring_new_review=['CVAE'],cvae_followup=str(CVAE),
    current_storage_check=str(OP/'post-archive-storage.json'),global_semantic_or_human_jurist_validation_claimed=False)
coverage=updated['completion-coverage-latest.json']
coverage.update(latest_read_only_progress_check=summary,last_checked_at_utc=now,latest_current_audit=str(AUDIT),first_pass_covered=30314,pending_first_pass=3)
observation_evidence={n:dict(bytes=(OP/n).stat().st_size,sha256=file_sha(OP/n)) for n in ('post-publication-observation.json','observe-post-publication.py','post-publication-observation.log')}
write(OP/'post-publication-evidence-manifest.json',dict(files=observation_evidence))
deferred=updated['deferred-recovery-latest.json']
deferred.update(last_checked_at_utc=now,latest_disposition=summary,current_disposition_proof=str(OP/'post-publication-observation.json'),
    current_native_worker_count=obs['native_processes'],current_responding_native_count=obs['native_responding_distinct_sessions'],
    native_execution_verified_at_utc=obs['checked_at_utc'],latest_current_review_failure_diagnostic=str(OP/'post-publication-observation.json'),
    latest_current_review_failure_manifest_sha256=file_sha(OP/'post-publication-evidence-manifest.json'),latest_current_review_failure_manifest=str(OP/'post-publication-evidence-manifest.json'),current_tail_deferred_jobs=obs['current_tail_deferred_jobs'],
    current_tail_deferred_articles=obs['current_tail_deferred_articles'],
    unique_original_and_current_deferred_reviews_pending=obs['unique_original_and_current_deferred_reviews_pending'],
    original_nonaccepted_review_articles_current_pending=obs['original_nonaccepted_review_articles_current_pending'])
parallel=updated['second-pass-parallelism-latest.json']
parallel.update(latest_operational_observation=summary,latest_native_execution_proof=str(OP/'post-publication-observation.json'),
    latest_native_execution_observed_at_utc=obs['checked_at_utc'],current_responding_distinct_sessions_at_observation=obs['native_responding_distinct_sessions'])
mutations=[]
for n,d in updated.items():
    d['previous_pointer_preserved']=str(OP/('before-'+n))
    p=R/n;assert p.read_bytes()==before[n],f'Intervening update: {n}'
    b=(json.dumps(d,ensure_ascii=False,indent=2)+'\n').encode();tmp=p.with_name(p.name+'.audit1908.tmp')
    with tmp.open('xb') as f:f.write(b);f.flush();os.fsync(f.fileno())
    assert p.read_bytes()==before[n],f'Intervening update: {n}'
    os.replace(tmp,p);assert p.read_bytes()==b
    mutations.append(dict(pointer=str(p),before_sha256=sha(before[n]),after_sha256=sha(b),before_preserved=str(OP/('before-'+n))))
write(OP/'pointer-updates.json',dict(at_utc=now,atomic_mutations=mutations,global_audit_pointer_not_rewritten=True))
(OP/'REPORT.md').write_text('''# Reprise après libération d’espace

Le signalement humain de l'espace libéré a permis une nouvelle capture cohérente et un audit technique intégral, validé puis publié atomiquement à 19:12:20 UTC. Aucun agent n'a été arrêté, relancé ou ajouté par ce contrôle et aucun texte source ou politique n'a changé.

Les quatre gros fichiers de l'ancien audit 1557Z ont été archivés seulement après publication du nouveau pointeur. Leurs empreintes compressées et leur décompression intégrale ont été revérifiées séparément. Le nouvel audit 1908Z reste non compressé et inspectable. Les archives, manifestes, refus et sources sont conservés.

La revue limitée L1242-2 reste applicable sous ses gardes exactes. La revue CVAE ne l'est plus : deux propositions ont changé. Un dossier de comparaison entière de ces deux textes est conservé et la relecture fraîche des treize articles demeure requise. Aucune conclusion juridique globale ni validation humaine n'est annoncée.

Le relevé postpublication observe huit réponses natives Astra/Moyen distinctes et 343 lots/2400 articles réellement relus sous le coordinateur unique 78943 ; cet effectif est daté. La liste complète porte 3442 completed et 26872 pending. Le nouveau quatrième différé concerne neuf articles fiscaux, après trois refus de validation, dernier motif « Payment timing relief is not a permanent tax cut ». Ses sources/NOTA/bornes et cinq champs d'avant-image sont inchangés et tous ses fichiers/refus restent préservés. Les quatre différés courants/45 identités s'ajoutent sans chevauchement aux trois anciens lots/36 : 81 identités uniques restent à reconstruire au point sûr, sans rejeu.

Les 30314 premières passes accessibles sont couvertes ; trois réserves documentaires restent non vérifiées. Toutes les secondes passes, la convergence des renvois et la qualification prioritaire, puis un audit final frais restent requis. La nouvelle baseline est le préfixe métrique de 622344 octets sous hash ddb234d11cdf14a010601394ea383be31288c88a23ea72c1e2c448f1127d397d : 2290 articles reviewed de 78943 avant capture. Le relevé postpublication compte 110 traitements supplémentaires. Les anciens totaux ne rendent pas ce nouvel audit immédiatement dû.
''')
files={str(p.relative_to(OP)):dict(bytes=p.stat().st_size,sha256=file_sha(p)) for p in sorted(OP.rglob('*')) if p.is_file()}
write(OP/'artifact-manifest.json',dict(files=files,external_audit_manifest_sha256=publication['artifact_manifest_sha256'],external_CVAE_followup_manifest_sha256=file_sha(CVAE/'artifact-manifest.json')))
print(json.dumps(dict(resolution=str(OP/'RESOLUTION.json'),manifest_sha256=file_sha(OP/'artifact-manifest.json'),free_gib=free/2**30,updated_pointers=len(mutations))))
