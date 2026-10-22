#!/usr/bin/env python3
"""Integrate one reviewed metadata correction, only at a coordinator-safe point.

Default: verify only. --apply is the only mutation path. Never starts/stops a
process, rewrites an original job, refreshes frozen guards, or edits a policy.
The coordinator lock is nonblocking; review_prior.commit owns its writer locks.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import copy
import fcntl
import hashlib
import json
import sqlite3
import sys

sys.dont_write_bytecode = True
OUT = Path(__file__).resolve().parent
PROJECT = OUT.parents[1]
RUNTIME = PROJECT / 'runtime/exhaustive'
JOB = RUNTIME / 'jobs/review-securite-sociale-LEGIARTI000042223830-00001-resume-2uu0letr'
INTENT = OUT / 'integration-intent.json'
COMPLETE = OUT / 'integration-complete.json'
LEDGER = RUNTIME / 'failed-job-resolutions.json'
BASE_MANIFEST_SHA = 'afef743baf20373231bed14e4c3b9396e741dfe240d2eebba4c4e5eeb714ae38'
PROTECTED = ('code_id', 'source_id', 'number', 'source_sha256', 'status',
             'proposed_xml', 'reason', 'review_notes', 'reference_checks', 'substantive_impact')

class Refusal(ValueError):
    pass

def require(condition, message):
    if not condition:
        raise Refusal(message)

def read(path):
    return json.loads(path.read_text(encoding='utf-8'))

def sha(value):
    if isinstance(value, str):
        value = value.encode('utf-8')
    return hashlib.sha256(value or b'').hexdigest()

def jsha(value):
    return sha(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False))

def key(row):
    return row['code_id'], row.get('source_id', row.get('id'))

def changes(before, after, path=''):
    if type(before) is not type(after):
        return [(path, before, after)]
    if isinstance(before, dict):
        require(before.keys() == after.keys(), 'Changed JSON members: ' + path)
        return sum((changes(before[k], after[k], path + '/' + k) for k in before), [])
    if isinstance(before, list):
        require(len(before) == len(after), 'Changed JSON list length: ' + path)
        return sum((changes(a, b, path + '/' + str(i)) for i, (a, b) in enumerate(zip(before, after))), [])
    return [] if before == after else [(path, before, after)]

def original_job_intact():
    baseline = read(OUT / 'original-job-files.before.json')
    actual = sorted(str(p.relative_to(JOB)) for p in JOB.rglob('*') if p.is_file())
    require(actual == sorted(f['path'] for f in baseline), 'Original failed job file inventory changed')
    for f in baseline:
        raw = (JOB / f['path']).read_bytes()
        require(len(raw) == f['bytes'] and sha(raw) == f['sha256'], 'Original failed job changed: ' + f['path'])
    return len(baseline)

def proof_inputs():
    require(sha((OUT / 'manifest.json').read_bytes()) == BASE_MANIFEST_SHA, 'Reviewed evidence manifest changed')
    for f in read(OUT / 'manifest.json')['files']:
        raw = (OUT / f['path']).read_bytes()
        require(len(raw) == f['bytes'] and sha(raw) == f['sha256'], 'Reviewed evidence changed: ' + f['path'])
    extra = read(OUT / 'integration-manifest.json')
    for f in extra['files']:
        require(sha((OUT / f['path']).read_bytes()) == f['sha256'], 'Integration script/document changed: ' + f['path'])
    original_job_intact()
    sources = read(OUT / 'original-job/source.json')
    before = read(OUT / 'original-job/answer.json')
    candidate = read(OUT / 'answer.metadata-only.json')
    require(len(sources) == len(before) == len(candidate) == 12, 'Expected exactly 12 articles')
    require(len({key(s) for s in sources}) == 12, 'Duplicate frozen source')
    require(changes(before, candidate) == [('/2/substantive_impact/classification', 'financing_transfer', 'mixed')],
            'Candidate is not the single approved classification correction')
    raw = (OUT / 'original-job/answer.json').read_bytes()
    needle = b'"classification": "financing_transfer"'
    require(raw.count(needle) == 1 and raw.replace(needle, b'"classification": "mixed"') == (OUT / 'answer.metadata-only.json').read_bytes(),
            'Candidate raw bytes differ beyond the single approved replacement')
    require(all(key(s) == key(a) == key(b) for s, a, b in zip(sources, before, candidate)), 'Frozen article order mismatch')
    for a, b in zip(before, candidate):
        require(a['substantive_impact']['effects'] == b['substantive_impact']['effects'], 'Effect changed')
    require([e['kind'] for e in candidate[2]['substantive_impact']['effects']] == ['financing_transfer', 'complexity_added'],
            'Expected transfer and disclosed added complexity')
    pins = read(OUT / 'active-code-policy-hashes.json')
    for f in pins:
        require(sha((PROJECT / f['path']).read_bytes()) == f['sha256'], 'Active engine/policy changed: ' + f['path'])
    require(sha((PROJECT / 'automatic_parallelism.py').read_bytes()) == '86c789ce047d4032e86129e8eea8db21694625ad916a4b24c55747f5a2b669eb', 'Atomic helper changed')
    return sources, candidate, read(OUT / 'original-job/reference-targets.json'), read(OUT / 'before-images.current.json'), pins

def merge_resolution(existing, entry):
    require(isinstance(existing, list), 'Resolution ledger must be a list')
    matching = [r for r in existing if r.get('job') == entry['job']]
    require(len(matching) <= 1, 'Duplicate existing resolution for this job')
    if matching:
        require(matching[0] == entry, 'Conflicting existing resolution for this job')
        return existing
    return existing + [entry]

def ro_db():
    db = sqlite3.connect((PROJECT / 'corpus.sqlite').as_uri() + '?mode=ro', uri=True, timeout=30)
    db.row_factory = sqlite3.Row
    db.execute('PRAGMA query_only=ON')
    db.execute('BEGIN')
    return db

def run(apply):
    sources, candidate, snapshot, capture, pins = proof_inputs()
    # Opening an existing lock r+ neither creates nor truncates it.
    lock_path = RUNTIME / 'coordinator.lock'
    require(lock_path.is_file(), 'Existing coordinator lock missing; refuse to create it')
    with lock_path.open('r+') as coordinator_lock:
        try:
            fcntl.flock(coordinator_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            return {'status': 'coordinator_busy', 'exit_code': 3, 'apply_requested': apply,
                    'reviewed_evidence_verified': True, 'original_job_intact': True,
                    'commit_called': False, 'live_writes': False,
                    'reason': 'Nonblocking coordinator lock unavailable; no writer lock or active import attempted'}
        sys.path.insert(0, str(PROJECT))
        import run_exhaustive as runner
        import review_prior as prior
        import reference_coherence as refs
        import substantive_impact as impact
        from ingest import source_notes
        from register_batches import writer_lock, validate_batches
        from automatic_parallelism import atomic
        # Validators may add certificates only; the reviewed validated answer is pinned.
        validated = runner.validate_answer(copy.deepcopy(candidate), sources)
        refs.accept_checks(validated, sources, snapshot)
        require(validated == read(OUT / 'answer.validated.json'), 'Validator output differs from frozen validated answer')
        for a, b, s in zip(candidate, validated, sources):
            require(all(a.get(f) == b.get(f) for f in PROTECTED), 'Validator changed protected content')
            impact.validate(b, s, required=True)
        require(runner.policy_is_current(OUT / 'original-job'), 'Original policies are stale')
        new_rows = copy.deepcopy(validated)
        for row, source in zip(new_rows, sources):
            row['policy_review_id'] = 'substantive_outcomes_2026_10_19'
            row['prior_proposal_sha256'] = source['previous_draft']['proposed_sha256']
        source_map = {key(s): s for s in sources}
        expected_rows = {key(r): r for r in new_rows}
        frozen_canonical = {key(r): r for r in capture['source_rows']}
        frozen_batches = {key(r): r for r in capture['batch_rows']}
        archive = []
        for s, row in zip(sources, new_rows):
            old = s['previous_draft']
            archive.append({k: v for k, v in dict(code_id=s['code_id'], source_id=s['source_id'],
                source_sha256=old['source_sha256'], status=old.get('status', 'rewrite_draft'), proposed_xml=old['proposed_xml'],
                reason=old['reason'], review_notes=old['review_notes'], replacement=row).items()})
        archive_id = sha(json.dumps(archive, ensure_ascii=False, sort_keys=True))
        archive_path = PROJECT / 'revisions/radical-review' / (archive_id + '.json')
        binding = {'version': 1, 'job': JOB.name, 'base_manifest_sha256': BASE_MANIFEST_SHA,
                   'metadata_answer_sha256': sha((OUT / 'answer.metadata-only.json').read_bytes()),
                   'validated_answer_sha256': sha((OUT / 'answer.validated.json').read_bytes()),
                   'original_source_sha256': sha((OUT / 'original-job/source.json').read_bytes()),
                   'original_reference_snapshot_sha256': sha((OUT / 'original-job/reference-targets.json').read_bytes()),
                   'archive_path': str(archive_path), 'archive_identifier': archive_id,
                   'expected_rows_sha256': jsha(new_rows), 'active_pins': pins}

        def check_static_again():
            proof_inputs()
            require(runner.policy_is_current(OUT / 'original-job'), 'Policies changed during integration')

        def inspect():
            """Caller holds writer_lock; never writes or refreshes original guards."""
            check_static_again()
            owners, files = prior.batch_owners(set(source_map))
            require(set(owners) == set(source_map), 'Missing/duplicate active batch owner')
            registry = read(PROJECT / 'registered-batches.json')
            manifest = read(prior.revisions_manifest())
            selected = [a for a in manifest['prior_articles'] if key(a) in source_map]
            require(len(selected) == 12 and len({key(a) for a in selected}) == 12, 'Review manifest ownership changed')
            for a in selected:
                old = source_map[key(a)]['previous_draft']
                require(a['source_sha256'] == old['source_sha256'] and a['proposed_sha256'] == old['proposed_sha256'],
                        'Review manifest before-image changed: ' + a['source_id'])
                require(a['review_status'] in ('pending', 'completed'), 'Unexpected review manifest state')
            states, reports = [], []
            db = ro_db()
            try:
                refs.check_guards(db, snapshot)  # Always the ORIGINAL frozen snapshot.
                for s in sources:
                    k = key(s); old = s['previous_draft']; frozen = frozen_canonical[k]
                    canonical = dict(db.execute('SELECT * FROM articles WHERE code_id=? AND id=?', k).fetchone() or {})
                    raw = db.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'", k).fetchone()
                    require(canonical == frozen['canonical_article'], 'Entire canonical article changed: ' + s['number'])
                    require(raw is not None and sha(raw[0]) == frozen['canonical_ARTICLE_xml_sha256'], 'Canonical ARTICLE XML changed: ' + s['number'])
                    require(source_notes(db, *k) == s['source_notes_xml'], 'Official notes changed: ' + s['number'])
                    current = db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?', k).fetchone()
                    require(current is not None, 'Missing draft: ' + s['number'])
                    current = tuple(current)
                    is_old = current == prior.draft_values(old) and sha(current[2]) == old['proposed_sha256']
                    is_new = current == prior.draft_values(expected_rows[k])
                    require(is_old or is_new, 'Changed draft guard: ' + s['number'])
                    # A retained row may have identical old/new draft values: batch metadata resolves state.
                    path, index = owners[k]
                    require(str(path.relative_to(PROJECT)) == frozen_batches[k]['path'], 'Batch owner moved: ' + s['number'])
                    batch = files[path][index]
                    batch_old = prior.batch_row_sha256(batch) == old['batch_row_sha256']
                    batch_new = batch == expected_rows[k]
                    require(batch_old or batch_new, 'Changed whole batch row guard: ' + s['number'])
                    old_registry = {'source_sha256': old['source_sha256'], 'proposed_sha256': old['proposed_sha256']}
                    new_registry = {'source_sha256': s['source_sha256'], 'proposed_sha256': sha(expected_rows[k]['proposed_xml'])}
                    require(registry.get('|'.join(k)) in (old_registry, new_registry), 'Unknown registry mirror: ' + s['number'])
                    states.append((is_old, is_new))
                    reports.append({'number': s['number'], 'source_id': s['source_id'], 'DB_old': is_old, 'DB_new': is_new,
                                    'batch_old': batch_old, 'batch_new': batch_new, 'registry_old': registry.get('|'.join(k)) == old_registry,
                                    'registry_new': registry.get('|'.join(k)) == new_registry, 'source_notes_and_raw_ARTICLE_exact': True,
                                    'effects_sha256': jsha(expected_rows[k]['substantive_impact']['effects'])})
                # Supplemental references were read for the substantive review; preserve their captured content too.
                for ref in capture['supplemental_references']:
                    k = key(ref)
                    row = db.execute('SELECT code_id,id,number,content_xml,source_sha256,valid_from,valid_until FROM articles WHERE code_id=? AND id=?', k).fetchone()
                    expected = {f: ref[f] for f in ('code_id', 'id', 'number', 'content_xml', 'source_sha256', 'valid_from', 'valid_until')}
                    require(row is not None and dict(row) == expected and source_notes(db, *k) == ref['source_notes_xml'], 'Supplemental source changed: ' + ref['number'])
                    draft = db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?', k).fetchone()
                    require((dict(draft) if draft else None) == ref['current_draft'], 'Supplemental reference draft changed: ' + ref['number'])
                db.row_factory = None  # The existing validator compares fetched tuples.
                records, diagnostics, checked_files = validate_batches(db, OUT / 'isolated-batches')
                require(len(records) == 12 and len(checked_files) == 1, 'Isolated validation did not inspect exactly 12 rows')
            finally:
                db.close()
            all_old = all(a for a, b in states)
            all_new = all(b for a, b in states)
            require(all_old or all_new, 'Mixed pre/post DB state; manual review required, no guard refresh')
            if all_new:
                require(INTENT.exists() and read(INTENT)['binding'] == binding, 'Post-commit DB without matching durable intent')
                require(archive_path.exists() and read(archive_path) == archive, 'Post-commit DB without exact before-image archive')
                state = 'post_commit'
            else:
                require(all(r['batch_old'] and r['registry_old'] for r in reports), 'DB is pre-commit but a batch/registry mirror was replaced; manual review required')
                require(all(a['review_status'] == 'pending' for a in selected), 'Pre-commit review manifest already completed')
                require(not COMPLETE.exists(), 'Completion proof exists but DB regressed')
                state = 'pre_commit'
            return {'state': state, 'articles': reports, 'owners': owners, 'files': files, 'registry': registry,
                    'manifest': manifest, 'manifest_selected': selected, 'isolated_diagnostics': diagnostics}

        with writer_lock():
            state = inspect()
            if INTENT.exists():
                require(read(INTENT)['binding'] == binding, 'Existing intent binds different evidence')
            if archive_path.exists():
                require(read(archive_path) == archive, 'Conflicting existing before-image archive')
            existing_ledger = read(LEDGER) if LEDGER.exists() else []
            matching = [e for e in existing_ledger if e.get('job') == JOB.name]
            if matching:
                require(COMPLETE.exists(), 'Resolution exists without local completion proof')
                require(read(COMPLETE).get('binding') == binding, 'Existing completion proof binds other evidence')
                require(len(matching) == 1 and matching[0] == read(COMPLETE)['resolution_entry'], 'Conflicting existing resolution')
                require(state['state'] == 'post_commit', 'Resolution exists before verified commit')
            before_intent = {'binding': binding, 'manifest_selected_before': state['manifest_selected']}
            if state['state'] == 'pre_commit':
                if INTENT.exists():
                    require(read(INTENT) == before_intent, 'Pre-commit manifest changed since durable intent')
                if apply:
                    atomic(INTENT, before_intent)
        if not apply:
            return {'status': 'dry_run_ready', 'exit_code': 0, 'state': state['state'], 'articles': state['articles'],
                    'candidate_and_reference_validations': 12, 'original_reference_snapshot_used': True,
                    'coordinator_lock_nonblocking': True, 'commit_called': False, 'live_writes': False,
                    'archive_identifier': archive_id, 'binding': binding}
        committed_here = False
        if state['state'] == 'pre_commit':
            # Never surround this call with writer_lock: commit acquires that non-reentrant lock itself.
            prior.commit(copy.deepcopy(validated), sources, reference_snapshot=snapshot)
            committed_here = True
        with writer_lock():
            state = inspect()
            require(state['state'] == 'post_commit', 'Commit did not produce the complete expected DB state')
            intent = read(INTENT)
            # A resume may reconcile ONLY recognizable old mirrors after exact DB+archive proof.
            for path, items in state['files'].items():
                changed = False
                for k, (owner_path, index) in state['owners'].items():
                    if owner_path == path and items[index] != expected_rows[k]:
                        require(prior.batch_row_sha256(items[index]) == source_map[k]['previous_draft']['batch_row_sha256'], 'Unrecognized batch mirror')
                        items[index] = copy.deepcopy(expected_rows[k]); changed = True
                if changed:
                    atomic(path, items)
            registry = state['registry']; changed = False
            for k, row in expected_rows.items():
                wanted = {'source_sha256': row['source_sha256'], 'proposed_sha256': sha(row['proposed_xml'])}
                if registry['|'.join(k)] != wanted:
                    registry['|'.join(k)] = wanted; changed = True
            if changed:
                atomic(PROJECT / 'registered-batches.json', registry)
            baseline = {key(a): a for a in intent['manifest_selected_before']}
            for a in state['manifest_selected']:
                old = baseline[key(a)]
                require({k: v for k, v in a.items() if k != 'review_status'} == {k: v for k, v in old.items() if k != 'review_status'},
                        'Review manifest changed beyond completion state')
                a['review_status'] = 'completed'
            manifest = state['manifest']
            count = sum(a['review_status'] == 'completed' for a in manifest['prior_articles'])
            if manifest.get('completed_second_pass') != count or any(a['review_status'] != 'completed' for a in state['manifest_selected']):
                manifest['completed_second_pass'] = count
                atomic(prior.revisions_manifest(), manifest)
            else:
                # selected dictionaries were edited in-memory; compare disk to detect a needed status repair.
                if read(prior.revisions_manifest()) != manifest:
                    atomic(prior.revisions_manifest(), manifest)
            post = inspect()
            require(all(r['DB_new'] and r['batch_new'] for r in post['articles']), 'Postverification draft/batch mismatch')
            require(all(a['review_status'] == 'completed' for a in post['manifest_selected']), 'Manifest completion missing')
            require(post['manifest']['completed_second_pass'] == sum(a['review_status'] == 'completed' for a in post['manifest']['prior_articles']), 'Manifest completion count mismatch')
            for k, row in expected_rows.items():
                require(post['registry']['|'.join(k)] == {'source_sha256': row['source_sha256'], 'proposed_sha256': sha(row['proposed_xml'])}, 'Registry postverification failed')
            original_job_intact()
            if COMPLETE.exists():
                completed = read(COMPLETE)
                require(completed['binding'] == binding and completed['articles'] == post['articles'], 'Completion evidence differs')
                require(completed['archive_sha256'] == sha(archive_path.read_bytes()), 'Archived proof bytes changed after completion')
            else:
                entry = {'job': JOB.name, 'accepted_articles': 12, 'resolution': str(COMPLETE),
                         'at_utc': datetime.now(timezone.utc).isoformat(), 'original_failure_preserved': True}
                completed = {'binding': binding, 'articles': post['articles'], 'resolution_entry': entry,
                             'archive_sha256': sha(archive_path.read_bytes()), 'original_job_intact': True,
                             'all_12_sources_notes_and_effects_unchanged': True,
                             'all_12_DB_and_batch_rows_exact': True, 'manifest_completed': True,
                             'original_reference_snapshot_validated': True}
                atomic(COMPLETE, completed)
            # Re-read under writer_lock, preserve all entries, atomically append exactly once.
            ledger = read(LEDGER) if LEDGER.exists() else []
            merged = merge_resolution(ledger, completed['resolution_entry'])
            if merged != ledger:
                atomic(LEDGER, merged)
            require(read(LEDGER) == merged and all(e in merged for e in ledger), 'Resolution ledger postverification failed')
            require(read(COMPLETE) == completed and read(archive_path) == archive, 'Durable proof postverification failed')
        return {'status': 'integrated' if committed_here else 'already_integrated_verified', 'exit_code': 0,
                'articles': 12, 'commit_called': committed_here, 'original_job_intact': True,
                'completion': str(COMPLETE), 'archive_identifier': archive_id,
                'resolution_ledger_preserved': True, 'new_effects_or_normative_changes_by_correction': False}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='Explicitly commit at the externally managed safe point')
    args = parser.parse_args()
    try:
        report = run(args.apply)
    except Exception as error:
        report = {'status': 'refused', 'exit_code': 2, 'error_type': type(error).__name__, 'error': str(error),
                  'apply_requested': args.apply, 'instruction': 'Preserve evidence; investigate. Never refresh frozen guards to force acceptance.'}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return report['exit_code']

if __name__ == '__main__':
    raise SystemExit(main())
