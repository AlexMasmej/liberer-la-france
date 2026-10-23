"""Publish only a fully validated frozen audit; preserve the previous pointer."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import os
import tempfile

OUT = Path(__file__).resolve().parent
PROJECT = OUT.parents[1]
POINTER = PROJECT / 'runtime/global-reference-audit-latest.json'

def read(name):
    return json.loads((OUT / name).read_text())

def dump(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def sha(path):
    with Path(path).open('rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()

v, s, cap, baseline, previous = (read(n) for n in ('validation.json','summary.json','capture.json','pre-capture-progress.json','previous-latest.json'))
assert v['checks_passed'] and not v['errors']
assert v['audit_id'] == s['audit_id'] == read('fingerprints.json')['audit_id']
assert s['as_of'] == '2026-10-18' and cap['quick_check'] == 'ok'
assert v['snapshot_byte_hash_matches_capture'] and v['full_inventory_and_logical_fingerprints_recomputed']
assert v['source_and_target_current_guards_match_manifest'] and v['queue_ids_match_findings'] and v['queue_sorted_by_priority']
assert sha(PROJECT / 'global_reference_audit.py') == cap['auditor_sha256']
assert v['frozen_snapshot_counts']['proposals_identical_to_source_body'] == 0
assert sha(OUT / 'validate_refresh.py') == previous['refresh_validator_template_sha256']
assert sha(previous['refresh_validator_template']) == previous['refresh_validator_template_sha256']
preflight = read('preflight.json')
assert read('immediate-storage-preflight.json')['capture_permitted']
assert read('immediate-storage-preflight.json')['free_bytes'] >= 6 * 2**30
assert set(cap['policies']) == {'corpus.json','policy-coordinations.json','site-summaries.json','reference-focus-extra.json'}
assert set(preflight['policies_before_capture']) == set(cap['policies'])
for name, digest in preflight['policies_before_capture'].items():
    assert cap['policies'][name]['sha256'] == digest == sha(PROJECT / name)
assert baseline['observed_at_utc'] < cap['started_at_utc']
assert POINTER.read_bytes() == (OUT / 'previous-latest.json').read_bytes(), 'Latest audit pointer changed; preserve and investigate'
prior_summary = json.loads((Path(previous['folder']) / 'summary.json').read_text())
metrics = {}
for name in ('entries_scanned','findings_count','distinct_articles_with_priority_1_findings','proposed_repeal_targets_with_detected_referrers'):
    metrics[name] = {'previous':prior_summary[name], 'current':s[name], 'change':s[name]-prior_summary[name]}
comparison = {'audit_id':s['audit_id'],'previous_audit_id':previous['audit_id'],'as_of':s['as_of'],'metrics':metrics,
              'occurrences':{'previous':sum(prior_summary['edge_counts'].values()),'current':sum(s['edge_counts'].values())},
              'priority_1':{'previous':prior_summary['findings_by_priority'].get('1',0),'current':s['findings_by_priority'].get('1',0)},
              'progress_before_capture':baseline,'frozen_snapshot_counts':v['frozen_snapshot_counts'],
              'additional_treatments_since_previous_baseline':baseline['additional_treatments_since_previous_baseline'],
              'structural_findings_are_confirmed_legal_errors':False,'automatic_change':False}
dump('refresh-comparison.json',comparison)
reviews = read('semantic-review-inheritance.json')['reviews']
prior_folder = Path(previous['folder'])
prior_artifacts = {item['path']:item for item in json.loads((prior_folder/'artifact-manifest.json').read_text())['files']}
prior_proof_path = prior_folder/'semantic-review-proofs.json'
assert sha(prior_proof_path) == prior_artifacts['semantic-review-proofs.json']['sha256']
prior_proofs = {item['label']:item for item in json.loads(prior_proof_path.read_text())['reviews']}
origins = []
for proof in read('semantic-review-proofs.json')['reviews']:
    label = proof['label']
    override = previous.get('semantic_review_overrides',{}).get(label)
    pinned = override['manifest_sha256'] if override else prior_proofs[label]['manifest_sha256']
    assert proof['manifest_sha256'] == pinned == sha(proof['manifest'])
    matching_review = next(item for item in reviews if item['label'] == label)
    assert set(matching_review['policies']) == set(cap['policies'])
    if override:
        assert matching_review['review_id'] == override['review_id']
    origins.append({'label':label,'manifest':proof['manifest'],'manifest_sha256':pinned,
                    'anchor':'previous pointer override' if override else 'previous published artifact manifest and semantic-review-proofs',
                    'classification_applies_to_new_snapshot':matching_review['classification_applies_to_new_snapshot']})
dump('semantic-origin-anchor-check.json',{'checks_passed':True,'origins':origins,'all_four_policy_guards_present':True,
     'pinned_validator_sha256':sha(OUT/'validate_refresh.py'),'zero_identical_proposals':True})
applicable = {r['label']:r for r in reviews if r['classification_applies_to_new_snapshot']}
review_lines = []
for r in reviews:
    if r['classification_applies_to_new_snapshot']:
        review_lines.append(f"La revue limitée {r['label']} ({r['findings_reviewed']} renvois, {r['articles_checked']} articles et dépendances) conserve sa portée : toutes les gardes d’articles et de politiques concordent. Ses limites sont reprises intégralement ; zéro incohérence effective démontrée dans ce seul groupe, zéro signalement marqué résolu.")
    else:
        review_lines.append(f"La revue {r['label']} doit être reprise : une garde a changé. Ses conclusions restent historiques et ne sont pas héritées comme qualification du nouveau snapshot.")
text = f"""# Rafraîchissement de l’audit global

Corpus au 18 octobre 2026. Capture cohérente du {cap['started_at_utc']} au {cap['completed_at_utc']}, en lecture seule, par étapes de 256 pages (1 Mio maximum), avec contrôle SQLite réussi et {cap['busy_steps']} étape occupée signalée. Le dossier antérieur reste conservé.

- **{s['entries_scanned']:,} entrées** et **{s['all_historical_article_versions_indexed']:,} versions historiques**.
- **{sum(s['edge_counts'].values()):,} occurrences ou liens** ; **{s['findings_count']:,} signalements structurels** à qualifier.
- **{s['findings_by_priority'].get('1',0):,} occurrences P1**, concernant **{s['distinct_articles_with_priority_1_findings']:,} articles distincts** ; **{s['proposed_repeal_targets_with_detected_referrers']:,} cibles proposées à l’abrogation** avec renvois détectés.
- Snapshot : **{v['frozen_snapshot_counts']['proposals_in_canonical_inventory']:,} propositions**, **{v['frozen_snapshot_counts']['retained_unchanged_in_canonical_inventory']:,} maintiens sans modification** ; zéro proposition identique au corps source.

La validation complète recalcule les inventaires, les empreintes logiques de toutes les métadonnées d’articles/documents/archives/propositions, les quatre fichiers de politiques, les gardes source/notes/document/proposition des 30 317 entrées, toutes les gardes source/cible des liens et signalements, les candidats historiques, l’identité et l’ordre de la file, les neuf rapports par recueil, les groupes de coordination et les cycles. Elle a réussi sans erreur. La preuve épinglée des 30 tests du parseur est réutilisée pour l’auditeur byte-identique ; aucun test du parseur n’a été répété. Voir `validation.json` et `parser-tests-inheritance.json`.

{chr(10).join(review_lines)}

Le relevé conservateur pris avant capture est de **{baseline['counters']['drafted_articles']:,} propositions, {baseline['counters']['retained_unchanged']:,} maintiens, {baseline['counters']['prior_drafts_reviewed']:,} secondes passes**, soit **{baseline['additional_treatments_since_previous_baseline']:,} traitements supplémentaires** depuis la baseline précédente. Les compteurs de progression ne sont pas présentés comme transactionnellement synchrones avec SQLite. Le prochain rafraîchissement est dû après 1 000 traitements supplémentaires selon cette base, ou avant clôture.

Aucune priorité de processus actif n’a été modifiée. La sauvegarde a utilisé les lectures bornées prévues. Aucun slot, processus de rédaction, code actif, politique, catalogue, donnée canonique, note, lot ou proposition n’a été modifié par cet audit. La seule publication est le pointeur d’audit, remplacé atomiquement après validation.

Les occurrences et signalements structurels ne constituent pas des fautes juridiques établies. Les ambiguïtés de code, versions historiques, alinéas et transitions restent à qualifier selon les limites du rapport principal. Ces revues limitées ne valent pas revue juridique globale.
"""
(OUT / 'REFRESH.md').write_text(text)
dump('priority-observation.json',{'requested':None,'result':'No priority override attempted; bounded read-only capture used','observed_stderr':None,'backup_read_step_max_bytes':cap['max_read_bytes_per_step'],'no_active_process_priority_modified':True})
now = datetime.now(timezone.utc).isoformat()
contract = applicable.get('L1242-2')
fiscal = next(r for r in reviews if r['label']=='CVAE')
pointer = {'folder':str(OUT),'audit_id':s['audit_id'],'snapshot_sha256':cap['snapshot_sha256'],'recorded_at_utc':now,
           'structural_scan_complete':True,'semantic_review_complete':False,'semantic_review_by_jurist':False,
           'read_only_source':True,'source_entry_count':s['entries_scanned'],
           'reviewed_contract_referrers':contract['findings_reviewed'] if contract else 0,
           'actual_errors_established_in_those_eight':contract['effective_inconsistencies_established'] if contract else None,
           'findings_are_not_confirmed_legal_errors':True,'next_refresh_after_additional_treatments':1000,
           'refresh_progress_observed_after_initial_scan':baseline['counters'],
           'refresh_rule':'New snapshot after at least 1000 additional first-pass/review treatments relative to observed counters or before final closure; publish only after complete validation. Guard limited semantic classifications against exact source/proposal/policy changes.',
           'additional_semantic_reviews':[{'folder':fiscal['folder'],'report':fiscal['report'],'findings_reviewed':fiscal['findings_reviewed'],
             'full_articles_read':fiscal['articles_checked'],'effective_inconsistencies_established':fiscal['effective_inconsistencies_established'],
             'classification_applies_to_new_snapshot':fiscal['classification_applies_to_new_snapshot'],'automatic_change':False,'jurist_review':False}],
           'refresh_progress_basis':{'method':'Conservative observation before snapshot capture; legacy counter field retained for continuity.',
             'observed_at_utc':baseline['observed_at_utc'],'status_updated_at_unix':baseline['status_updated_at_unix'],'evidence':str(OUT/'pre-capture-progress.json')},
           'frozen_snapshot_counts':v['frozen_snapshot_counts'],'as_of':s['as_of'],'validation':str(OUT/'validation.json'),
           'refresh_report':str(OUT/'REFRESH.md'),'semantic_review_inheritance':str(OUT/'semantic-review-inheritance.json'),
           'prior_audit':{k:previous[k] for k in ('folder','audit_id','snapshot_sha256')},'prior_semantic_reviews_are_limited_and_guarded':True,
           'semantic_reviews_requiring_new_review':v['semantic_reviews_requiring_new_review']}
# Carry origins as pinned evidence, independently of applicability in this snapshot.
pointer['refresh_validator_template'] = previous['refresh_validator_template']
pointer['refresh_validator_template_sha256'] = previous['refresh_validator_template_sha256']
pointer['semantic_review_overrides'] = previous.get('semantic_review_overrides',{})
pointer['additional_semantic_review_history'] = previous.get('additional_semantic_review_history',[])
pointer['semantic_review_origin_anchors'] = str(OUT/'semantic-origin-anchor-check.json')
for label, entry in pointer['semantic_review_overrides'].items():
    checked = next(item for item in reviews if item['label'] == label)
    entry['last_checked_audit_id'] = s['audit_id']
    entry['classification_applies_to_last_checked_snapshot'] = checked['classification_applies_to_new_snapshot']
pointer['additional_semantic_reviews'][0]['review_id'] = fiscal['review_id']
dump('latest-pointer.candidate.json',pointer)
excluded = {'artifact-manifest.json','pointer-update.json'}
files = []
for p in sorted(OUT.rglob('*')):
    if not p.is_file() or p.name in excluded or p.name.endswith(('-wal','-shm')):
        continue
    files.append({'path':str(p.relative_to(OUT)),'bytes':p.stat().st_size,'sha256':sha(p)})
manifest = {'audit_id':s['audit_id'],'validated_at_utc':now,
            'exclusions':['Self manifest','Pointer publication proof, which records this manifest hash','SQLite transient -wal/-shm sidecars'],
            'files':files}
dump('artifact-manifest.json',manifest)
for f in files:
    p=OUT/f['path']
    assert p.stat().st_size==f['bytes'] and sha(p)==f['sha256'], f['path']
assert POINTER.read_bytes()==(OUT/'previous-latest.json').read_bytes(), 'Pointer changed before replacement'
assert sha(OUT/'corpus.snapshot.sqlite') == cap['snapshot_sha256'] == s['snapshot_and_policy_fingerprints']['snapshot_sha256']
# A new sibling temporary file avoids truncating the current published pointer.
with tempfile.NamedTemporaryFile(mode='wb',dir=POINTER.parent,delete=False) as stream:
    tmp=Path(stream.name)
    stream.write((OUT/'latest-pointer.candidate.json').read_bytes());stream.flush();os.fsync(stream.fileno())
try:
    tmp.replace(POINTER)
finally:
    tmp.unlink(missing_ok=True)
assert POINTER.read_bytes()==(OUT/'latest-pointer.candidate.json').read_bytes()
dump('pointer-update.json',{'at_utc':datetime.now(timezone.utc).isoformat(),'atomic_replace_completed':True,
     'previous_audit_id':previous['audit_id'],'new_audit_id':s['audit_id'],'validation_passed_before_replace':True,
     'pointer':str(POINTER),'pointer_sha256':sha(POINTER),'artifact_manifest_sha256':sha(OUT/'artifact-manifest.json'),
     'every_manifest_file_rehashed_before_replace':True,'active_corpus_modified':False,'automatic_correction':False})
print(json.dumps({'folder':str(OUT),'report':str(OUT/'REFRESH.md'),'pointer_updated':True,'audit_id':s['audit_id'],
     'entries':s['entries_scanned'],'occurrences':sum(s['edge_counts'].values()),'structural_findings':s['findings_count'],
     'priority_1_occurrences':s['findings_by_priority'].get('1',0),'priority_1_articles':s['distinct_articles_with_priority_1_findings'],
     'proposed_repeal_targets':s['proposed_repeal_targets_with_detected_referrers'],'semantic_reviews_requiring_new_review':v['semantic_reviews_requiring_new_review']},ensure_ascii=False,indent=2))
