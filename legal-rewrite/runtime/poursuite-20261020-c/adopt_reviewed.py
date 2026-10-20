"""Adopt bounded Phase C readings ONLY after the parent's registration/activation signal.

No work runs on import. This tool never writes SQLite, batches or policies. The
only active write is the audit ledger, under the shared writer lock, after all
checks. Its old bytes are first archived under their SHA256. A policy refresh is
not a new semantic review; stale prior readings remain stored with their OLD
certificate. Run only when explicitly instructed by the parent.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import copy
import hashlib
import json
import os
import sqlite3
import sys
import xml.etree.ElementTree as ET

P = Path(__file__).resolve().parent
B = P.parents[1]


def sha_bytes(raw):
    return hashlib.sha256(raw).hexdigest()


def digest(value):
    return sha_bytes((value or '').encode())


def canonical_digest(value):
    return digest(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')))


def load(path):
    return json.loads(path.read_text())


def key(row):
    return row['code_id'] + '|' + row.get('source_id', row.get('id', ''))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def within(root, value):
    path = (root / value).resolve()
    require(path.is_relative_to(root.resolve()), 'Path outside approved runtime root: ' + str(value))
    return path


def pin(source, row):
    return dict(code_id=row['code_id'], source_id=row['source_id'], number=row['number'],
                source_sha256=source['source_sha256'], source_body_sha256=digest(source['source_xml']),
                source_notes_sha256=digest(source.get('source_notes_xml')),
                proposed_sha256=digest(row.get('proposed_xml')))


def dependency_matches(expected, actual):
    """Missing pins never match; null proposal and source-only view stay distinct."""
    fields = ('code_id', 'source_id', 'source_sha256', 'source_body_sha256',
              'source_notes_sha256', 'proposed_sha256')
    return all(field in expected and expected[field] == actual[field] for field in fields)


def prior_reasons(audit, source, row, actual_dependencies):
    """Pure strict check. A failed dependency never gets substituted by Phase C."""
    cert = audit.get('certificate', {})
    expected = dict(version=1, source_sha256=source['source_sha256'],
                    source_notes_sha256=digest(source.get('source_notes_xml')),
                    proposed_sha256=digest(row.get('proposed_xml')),
                    assessment_sha256=canonical_digest(audit.get('assessment')))
    failures = [field for field, value in expected.items() if cert.get(field) != value]
    if audit.get('source_body_sha256') and audit['source_body_sha256'] != digest(source['source_xml']):
        failures.append('source_body_sha256')
    if not audit.get('reviewed_by') or not audit.get('approved_at'):
        failures.append('missing_independent_reading_identity')
    guards = audit.get('dependency_guards')
    if not isinstance(guards, list):
        return failures + ['missing_dependency_guard_list']
    seen = set()
    for guard in guards:
        identifier = key(guard)
        if identifier in seen:
            failures.append('duplicate_dependency:' + identifier)
        seen.add(identifier)
        current = actual_dependencies.get(identifier)
        if current is None or not dependency_matches(guard, current):
            failures.append('changed_dependency:' + identifier)
    return failures


def prior_allowlist(old_entries, phase_b):
    """Only Phase B's 204 genuinely adopted readings may be reattested.

    The other 80 ledger entries deliberately kept expired certificates. Having
    a reviewer name and an empty dependency list is NOT evidence of adoption.
    """
    by_id = {}
    for identifier, audit in old_entries.items():
        by_id.setdefault(audit['source_id'], []).append(identifier)
    allowed = set()
    require(len(phase_b['adopted']) == 204, 'Phase B adoption allowlist must identify exactly 204 independent readings')
    for item in phase_b['adopted']:
        identifiers = by_id.get(item['source_id'], [])
        if item.get('code_id'):
            identifiers = [i for i in identifiers if old_entries[i]['code_id'] == item['code_id']]
        require(len(identifiers) == 1, 'Missing or ambiguous Phase B adopted source_id: ' + item['source_id'])
        require(identifiers[0] not in allowed, 'Duplicate Phase B adopted identity: ' + identifiers[0])
        allowed.add(identifiers[0])
    return allowed


def hashes_in(value):
    """Review formats vary; exact file hashes must occur in structured evidence."""
    if isinstance(value, str):
        return {value}
    if isinstance(value, list):
        return set().union(*(hashes_in(x) for x in value)) if value else set()
    if isinstance(value, dict):
        return set().union(*(hashes_in(x) for x in value.values())) if value else set()
    return set()


def file_sha(path):
    return sha_bytes(path.read_bytes())


def verified_sources(db, identifier, source_notes, xml_contents):
    """Verify the raw official XML against the historical source hash too.

    Prior certificates predate source-body pins. Their raw document SHA binds
    the exact source body; reconstructing it avoids trusting a changed DB body
    merely because its source_sha256 column was not updated.
    """
    code, sid = identifier.split('|', 1)
    official = db.execute('SELECT number,source_sha256,content_xml FROM articles WHERE code_id=? AND id=?', (code, sid)).fetchone()
    require(official is not None, 'Missing article: ' + identifier)
    raw = db.execute("SELECT xml,sha256 FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'", (code, sid)).fetchone()
    require(raw is not None, 'Missing complete official document: ' + identifier)
    binary = raw[0].encode() if isinstance(raw[0], str) else raw[0]
    require(sha_bytes(binary) == raw[1] == official[1], 'Official XML hash mismatch: ' + identifier)
    parsed = ET.fromstring(binary)
    require(xml_contents(parsed.find('BLOC_TEXTUEL/CONTENU')) == official[2], 'Official body differs from authenticated source document: ' + identifier)
    return dict(code_id=code, source_id=sid, number=official[0], source_sha256=official[1],
                source_xml=official[2], source_notes_xml=source_notes(db, code, sid))


def current_row(db, source):
    row = db.execute('SELECT source_sha256,status,proposed_xml FROM drafts WHERE code_id=? AND source_id=?',
                     (source['code_id'], source['source_id'])).fetchone()
    require(row is not None, 'Article has no registered disposition: ' + key(source))
    require(row[0] == source['source_sha256'], 'Draft source mismatch: ' + key(source))
    return dict(code_id=source['code_id'], source_id=source['source_id'], number=source['number'],
                source_sha256=row[0], status=row[1], proposed_xml=row[2])


def source_only_or_draft(db, source):
    row = db.execute('SELECT source_sha256,proposed_xml FROM drafts WHERE code_id=? AND source_id=?',
                     (source['code_id'], source['source_id'])).fetchone()
    require(row is None or row[0] == source['source_sha256'], 'Dependency draft source mismatch: ' + key(source))
    return dict(code_id=source['code_id'], source_id=source['source_id'], number=source['number'],
                proposed_xml=row[1] if row else None)


def archived_write(path, raw):
    """Immutable byte-for-byte archive; refuse a collision rather than replace."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        require(path.read_bytes() == raw, 'Archive collision: ' + str(path))
        return
    with path.open('xb') as out:
        out.write(raw)
        out.flush()
        os.fsync(out.fileno())


def atomic_bytes(path, raw):
    temp = path.with_name(path.name + '.phase-c-' + str(os.getpid()) + '.tmp')
    try:
        with temp.open('xb') as out:
            out.write(raw)
            out.flush()
            os.fsync(out.fileno())
        temp.replace(path)
    finally:
        if temp.exists():
            temp.unlink()


def encoded(data):
    return (json.dumps(data, ensure_ascii=False, indent=2) + '\n').encode()


def staged_packages(read):
    """Replay exact final preflight order; explicit overrides alone may win."""
    specs = read(P / 'integration-specs.json')
    pre = read(P / 'integration/edition001/preflight.json')
    require(len(pre['packages']) == len(specs), 'Preflight/specification package count mismatch')
    selected = {}
    provenance = []
    for spec, frozen in zip(specs, pre['packages']):
        require(all(frozen.get(k) == v for k, v in spec.items()), 'Changed integration specification: ' + spec['folder'])
        folder = within(P, spec['folder'])
        sp, ap = folder / spec.get('source', 'source.json'), folder / spec.get('answer', 'answer.json')
        require(file_sha(sp) == frozen['source_sha256'], 'Changed frozen sources: ' + str(sp))
        require(file_sha(ap) == frozen['answer_sha256'], 'Changed frozen answer: ' + str(ap))
        manifest_folder = within(P, spec.get('manifest_folder', spec['folder']))
        require(file_sha(manifest_folder / 'manifest.json') == frozen['manifest_sha256'], 'Changed frozen manifest: ' + str(manifest_folder))
        manifest = read(manifest_folder / 'manifest.json')
        require(manifest.get('frozen') is True, 'Unfrozen package: ' + str(folder))
        for name, expected in manifest.get('files', manifest.get('files_sha256', {})).items():
            require(file_sha(within(manifest_folder, name)) == expected, 'Frozen package file changed: ' + name)
        proof_path = within(P, spec['review'])
        proof = read(proof_path)
        for field in ('blocking_findings', 'blocking_issues', 'unresolved_blocking_findings'):
            require(not proof.get(field), 'Blocking independent findings: ' + str(proof_path))
        verdict = str(proof.get('verdict', '')).lower()
        conditional = verdict == 'main21_ready_only_with_two_required_coordination_articles_pending_parent_review'
        require(not any(word in verdict for word in ('rejected', 'reject', 'blocked', 'not_approved')), 'Rejected independent review: ' + str(proof_path))
        require(bool(proof.get('approved_at')) or conditional or 'no remaining concrete' in verdict or 'no_concrete_defect' in verdict or 'approved' in verdict,
                'Review has no explicit approval or identified resolved conditional verdict: ' + str(proof_path))
        require(frozen['answer_sha256'] in hashes_in(proof), 'Independent evidence does not identify exact answer: ' + str(ap))
        ss, aa = read(sp), read(ap)
        require(len(ss) == len(aa), 'Source/answer length mismatch')
        for source, row in zip(ss, aa):
            identifier = key(source)
            require(identifier == key(row), 'Source/answer order mismatch')
            if identifier in selected:
                require(spec.get('override') is True, 'Unapproved duplicate: ' + identifier)
                old = selected[identifier]['source']
                require(all(old.get(k) == source.get(k) for k in ('source_sha256', 'source_xml', 'source_notes_xml')), 'Override source changed: ' + identifier)
            selected[identifier] = dict(source=source, row=row, spec=spec, proof=proof_path,
                                         proof_sha256=file_sha(proof_path), folder=folder)
        provenance.append(dict(**frozen, review_sha256=file_sha(proof_path)))
    require(len(selected) == pre['articles'], 'Final selection count differs from preflight')
    if any(entry['spec']['folder'] == 'travail/edition001' for entry in selected.values()):
        for sid in ('LEGIARTI000006901816', 'LEGIARTI000006902866'):
            require('LEGITEXT000006072050|' + sid in selected and
                    selected['LEGITEXT000006072050|' + sid]['spec']['folder'] == 'travail-coordination-supplement/edition001',
                    'Conditional Travail21 review requires the independently approved whole-text supplement: ' + sid)
    ss, aa = read(P / 'integration/edition001/source.json'), read(P / 'integration/edition001/answer.json')
    require(ss == [entry['source'] for entry in selected.values()], 'Staged source changed/order mismatch')
    require(aa == [entry['row'] for entry in selected.values()], 'Staged answer not the final metadata selection')
    return selected, pre, provenance


def refresh_context(args, read, selected, policy, registration_sha, rc, db):
    """Consume the real post-registration refresh and its parent approval chain."""
    receipt_path = within(P, args.refresh_receipt)
    receipt = read(receipt_path)
    folder = receipt_path.parent
    manifest = read(folder / 'manifest.json')
    require(manifest.get('frozen') is True and manifest.get('metadata_staging_only') is True,
            'Refresh is not a frozen metadata-only final edition')
    for relative, expected in manifest['files_sha256'].items():
        path = within(folder, relative)
        require(file_sha(path) == expected, 'Refresh proof file changed: ' + relative)
        read(path)
    require(receipt['policy_sha256'] == policy, 'Refresh policy differs from activated policy')
    require(receipt['articles'] == len(selected) and receipt['all_normative_bodies_byte_identical'] is True
            and receipt['all_other_answer_fields_unchanged'] is True, 'Incomplete refresh coverage')
    original_certificate_count = sum(bool(entry['row'].get('reference_coherence')) for entry in selected.values())
    require(isinstance(receipt['assessments_changed'], int) and receipt['assessments_changed'] >= 0
            and receipt['reference_certificates_reemitted'] == original_certificate_count
            and receipt['articles_without_required_certificate'] == len(selected) - original_certificate_count,
            'Unexpected reference certificate/analysis counts')
    # Explicit paths are included by the author; an unexplained hash alone is not approval.
    capture_manifest_path = Path(receipt['capture_manifest_path']).resolve()
    approved_path = Path(receipt['approved_assessments_path']).resolve()
    require(capture_manifest_path.is_relative_to(P) and approved_path.is_relative_to(P), 'External refresh evidence path')
    require(file_sha(capture_manifest_path) == receipt['capture_manifest_sha256'], 'Capture manifest changed')
    require(file_sha(approved_path) == receipt['approved_assessments_sha256'], 'Parent assessment approval changed')
    cap_folder = capture_manifest_path.parent
    capture_manifest = read(capture_manifest_path)
    for name, expected in capture_manifest['files_sha256'].items():
        path = within(cap_folder, name)
        require(file_sha(path) == expected, 'Actual capture file changed: ' + name)
        read(path)
    capture = read(cap_folder / 'capture-proof.json')
    require(capture['registration_receipt_sha256'] == registration_sha, 'Capture belongs to another registration')
    require(receipt['registration_receipt_sha256'] == registration_sha, 'Refresh belongs to another registration')
    require(capture['policy_sha256'] == policy and capture['readonly_transaction'] is True,
            'Actual capture does not match current policy')
    capture_proof_path = Path(receipt['capture_proof_path']).resolve()
    require(capture_proof_path == cap_folder / 'capture-proof.json' and file_sha(capture_proof_path) == receipt['capture_proof_sha256'], 'Capture proof provenance mismatch')
    require(Path(receipt['registration_receipt_path']).resolve() == P / 'integration/edition001/registration.json', 'Unexpected registration receipt path')
    plan_path = within(P, args.refresh_plan)
    plan = read(plan_path)
    require(plan['selected_article_count'] == len(selected), 'Final plan covers another selection')
    require(plan['certificate_count'] == original_certificate_count and
            plan['without_required_certificate_count'] == len(selected) - original_certificate_count, 'Final plan certificate counts differ')
    require(file_sha(B / 'reference_coherence.py') == plan['frozen_module_sha256'], 'Reference protocol changed since final plan')
    for relative, expected in plan['selected_frozen_file_sha256'].items():
        require(file_sha(within(P, relative)) == expected, 'Final plan frozen file changed: ' + relative)
    require(file_sha(plan_path) == capture['plan_sha256'] == receipt['plan_sha256'], 'Refresh plan changed')
    approval = read(approved_path)
    require(approval['status'] == 'approved_by_parent_after_whole_actual_DB_target_read', 'Missing explicit parent review')
    require(approval['captured_snapshot_sha256'] == file_sha(cap_folder / 'reference-targets.json'), 'Approval targets another capture')
    require(receipt['beforeimages_sha256'] == file_sha(cap_folder / 'beforeimages.json'), 'Capture before-images changed')
    context_path = Path(receipt['context_beforeimages_path']).resolve()
    require(context_path == cap_folder / 'context-beforeimages.json' and
            file_sha(context_path) == receipt['context_beforeimages_sha256'], 'Additional context provenance mismatch')
    additional_context_keys = []
    from ingest import source_notes, xml_contents
    for context in read(context_path):
        identifier = context['target_key']
        source = verified_sources(db, identifier, source_notes, xml_contents)
        require(all(source[f] == context['source'][f] for f in ('source_sha256', 'source_xml', 'source_notes_xml')),
                'Additional actual context source/notes changed: ' + identifier)
        cursor = db.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?', identifier.split('|', 1))
        record = cursor.fetchone()
        actual = dict(zip([field[0] for field in cursor.description], record)) if record is not None else None
        require(actual == context['draft'], 'Additional actual context before-image changed: ' + identifier)
        additional_context_keys.append(identifier)
    require(receipt['source_sha256'] == file_sha(folder / 'source.json')
            and receipt['answer_sha256'] == file_sha(folder / 'answer.json'), 'Final refresh source/answer hashes mismatch')
    ss, aa = read(folder / 'source.json'), read(folder / 'answer.json')
    require(len(ss) == len(aa) == len(selected), 'Refresh does not cover exact final selection')
    refreshed = {}
    allowed = {'reference_checks', 'reference_coherence'}
    changed = {}
    # Only reference checks/certificates may change; impact metadata stays final.
    for source, row in zip(ss, aa):
        identifier = key(source)
        require(identifier == key(row) and identifier in selected and identifier not in refreshed, 'Unexpected refresh identity')
        original = selected[identifier]
        require(all(source.get(f) == original['source'].get(f) for f in
                    ('source_sha256', 'source_xml', 'source_notes_xml', 'source_document_xml')), 'Refresh source changed')
        old_core = {k: v for k, v in original['row'].items() if k not in allowed}
        new_core = {k: v for k, v in row.items() if k not in allowed}
        require(old_core == new_core, 'Refresh altered body/status/impact or another unapproved field: ' + identifier)
        before = original['row'].get('reference_checks', [])
        after = row.get('reference_checks', [])
        require(len(before) == len(after), 'New or removed reference assessment: ' + identifier)
        for old_check, new_check in zip(before, after):
            require(old_check['target_key'] == new_check['target_key'], 'Reference assessment identity changed')
            if old_check != new_check:
                changed[(identifier, new_check['target_key'])] = new_check
        refreshed[identifier] = row
    expected_pairs = {(r['referrer_key'], v['target_key']) for r in plan['recertify_rows'] for v in r['changed_assessments']}
    require(set(changed) == expected_pairs and receipt['assessments_changed'] == len(expected_pairs),
            'Changed analyses differ from exact final approved plan')
    approved = {(a['referrer_key'], a['target_key']): {k: a[k] for k in ('target_key', 'view_sha256', 'assessment')}
                for a in approval['assessments']}
    require(len(approval['assessments']) == len(approved) and approved == changed, 'Refreshed assessments differ from explicit parent approval')
    snapshot = read(folder / 'reference-targets.json')
    rc.check_guards(db, snapshot)
    require(snapshot == read(cap_folder / 'reference-targets.json'), 'Snapshot differs from actual parent-reviewed capture')
    certificates = 0
    for identifier, row in refreshed.items():
        source = selected[identifier]['source']
        has_cert = bool(selected[identifier]['row'].get('reference_coherence'))
        if has_cert:
            require(rc.certificate_current(db, source, row.get('proposed_xml'), row.get('reference_coherence')), 'Refreshed certificate not current: ' + identifier)
            certificates += 1
        else:
            require(not row.get('reference_coherence'), 'Artificial certificate for a row without required references')
    require(certificates == original_certificate_count, 'Final certificate count differs')
    return snapshot, refreshed, dict(file=str(receipt_path.relative_to(B)), sha256=file_sha(receipt_path),
                                    parent_approval_file=str(approved_path.relative_to(B)), parent_approval_sha256=file_sha(approved_path),
                                    additional_context_keys=additional_context_keys)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--after-registration-and-activation', action='store_true',
                        help='Use only after the parent explicitly signals registration and activation complete.')
    parser.add_argument('--refresh-plan', required=True,
                        help='Phase C relative FINAL frozen plan; do not supply superseded preparatory editions.')
    parser.add_argument('--refresh-receipt', required=True,
                        help='Phase C relative receipt of real post-registration, parent-approved reference recertification.')
    args = parser.parse_args(argv)
    require(args.after_registration_and_activation, 'No adoption without explicit post-registration/activation invocation')
    sys.path.insert(0, str(B))
    from ingest import source_notes, xml_contents
    from substantive_impact import validate, certificate
    from register_batches import writer_lock
    import reference_coherence as rc

    # Acquire the same lock as registration BEFORE opening the read snapshot.
    with writer_lock():
        tracked = {}
        def read(path):
            path = path.resolve()
            raw = path.read_bytes()
            if path in tracked:
                require(tracked[path] == sha_bytes(raw), 'Input changed during adoption: ' + str(path))
            tracked[path] = sha_bytes(raw)
            return json.loads(raw)
        activation = read(P / 'activation.json')
        registration_path = P / 'integration/edition001/registration.json'
        registration = read(registration_path)
        policy = rc.policy_state()
        require(policy == {'policy-coordinations.json': activation['policy_sha256'],
                           'site-summaries.json': activation['site_summaries_sha256']}, 'Activation does not match current policy')
        for name, expected in policy.items():
            require(file_sha(B / name) == expected, 'Active policy mismatch')
            tracked[(B / name).resolve()] = expected
        selected, preflight, lineage = staged_packages(read)
        require(registration['registered_articles'] == preflight['articles'] == activation['registered_reviewed_articles'], 'Not all reviewed articles registered/activated')
        receipt_checks = {key(c): c for c in registration['checks']}
        require(set(receipt_checks) == set(selected), 'Registration receipt identities differ from exact reviewed selection')
        for identifier, entry in selected.items():
            check = receipt_checks[identifier]
            require(check.get('source_and_notes_verified') is True and check.get('prior_checked') is True
                    and check.get('proposed_sha256') == digest(entry['row'].get('proposed_xml')), 'Incomplete registration check: ' + identifier)
        ledger = B / 'runtime/substantive-audits.json'
        old_raw = ledger.read_bytes()
        previous_adoption = P / 'audit-adoption.json'
        if previous_adoption.exists():
            previous = read(previous_adoption)
            require(previous['resulting_ledger_sha256'] == sha_bytes(old_raw), 'Previous adoption exists but ledger changed; obtain a new reviewed edition')
            require(previous['reference_recertification']['sha256'] == file_sha(within(P, args.refresh_receipt)), 'Different refresh from completed adoption')
            require(previous['policy_sha256'] == policy and previous['registration_sha256'] == file_sha(registration_path), 'Different activation/registration from completed adoption')
            print(json.dumps(dict(already_adopted=True, stored=previous['stored_audits'])))
            return
        old = read(ledger)
        require(old.get('version') == 1, 'Unsupported prior audit ledger')
        old_entries = {key(a): a for a in old['audits']}
        require(len(old_entries) == len(old['audits']), 'Duplicate old audit identities')
        phase_b_adoption_path = P.parent / 'poursuite-20261020-b/audit-adoption.json'
        allowed_prior = prior_allowlist(old_entries, read(phase_b_adoption_path))
        db = sqlite3.connect('file:' + str(B / 'corpus.sqlite') + '?mode=ro', uri=True)
        db.execute('BEGIN')
        try:
            cache = {}
            def material(identifier):
                if identifier not in cache:
                    source = verified_sources(db, identifier, source_notes, xml_contents)
                    cache[identifier] = (source, source_only_or_draft(db, source))
                return cache[identifier]
            for identifier, entry in selected.items():
                source, _ = material(identifier)
                require(all(source.get(f) == entry['source'].get(f) for f in ('source_sha256', 'source_xml', 'source_notes_xml')), 'Registered full source/notes changed: ' + identifier)
                current = current_row(db, source)
                row = entry['row']
                actual_metadata = db.execute('SELECT reason,review_notes FROM drafts WHERE code_id=? AND source_id=?',
                                             (source['code_id'], source['source_id'])).fetchone()
                require(actual_metadata == (row['reason'], row['review_notes']), 'Registered latest reason/notes differ: ' + identifier)
                require(all(current[f] == row[f] for f in ('source_sha256', 'status', 'proposed_xml')), 'Registered full proposal changed: ' + identifier)
                validate(copy.deepcopy(row), source, required=True, enforce_workflow=False)
            snapshot, refreshed, refresh_proof = refresh_context(args, read, selected, policy,
                    file_sha(registration_path), rc, db)
            stamp = datetime.now(timezone.utc).isoformat()
            entries = copy.deepcopy(old_entries)
            prior_valid, prior_stale, adopted = [], [], []
            for identifier, audit in old_entries.items():
                if identifier not in allowed_prior:
                    prior_stale.append(dict(key=identifier, reasons=['Not among Phase B 204 independently adopted identities; expired certificate intentionally preserved'], certificate_left_unchanged=True))
                    continue
                try:
                    source, _ = material(identifier)
                    row = current_row(db, source)
                    deps = {}
                    for guard in audit.get('dependency_guards', []):
                        target = key(guard)
                        try:
                            s, r = material(target)
                            deps[target] = pin(s, r)
                        except ValueError:
                            pass
                    failures = prior_reasons(audit, source, row, deps)
                    validate(dict(row, substantive_impact=audit['assessment']), source, required=True, enforce_workflow=False)
                    require((B / audit['evidence_file']).is_file(), 'Prior reading evidence missing')
                    if audit.get('evidence_sha256'):
                        require(file_sha(B / audit['evidence_file']) == audit['evidence_sha256'], 'Prior evidence changed')
                except (ValueError, KeyError, TypeError, ET.ParseError) as error:
                    failures = [str(error)]
                if failures:
                    # Deliberately leave this entire stored entry unchanged.
                    prior_stale.append(dict(key=identifier, reasons=failures, certificate_left_unchanged=True))
                    continue
                updated = copy.deepcopy(audit)
                if updated['certificate'].get('policy_sha256') != policy['policy-coordinations.json']:
                    updated.setdefault('reattestation_history', []).append(dict(
                        certificate=copy.deepcopy(audit['certificate']), approved_at=audit['approved_at'],
                        reattested_at=stamp, reason='Exact official document, body, notes, proposal, assessment and every recorded dependency unchanged; policy-only refresh, no new semantic reading'))
                    updated['certificate'] = certificate(dict(row, substantive_impact=audit['assessment']), source, policy['policy-coordinations.json'])
                    updated['source_body_sha256'] = digest(source['source_xml'])
                    updated['reattested_at'] = stamp
                entries[identifier] = updated
                prior_valid.append(identifier)
            # The refreshed snapshot pins all actual external and intra-package views.
            # Conservative dependency set: every Phase C sibling + captured target.
            # This may invalidate a reading earlier than necessary, never later.
            all_pins = {}
            integration_targets = read(P / 'integration/edition001/reference-targets.json')['targets']
            for identifier, captured in integration_targets.items():
                require(rc.guard(rc.state(db, identifier)) == rc.guard(captured), 'External preflight dependency changed: ' + identifier)
            for identifier in set(selected) | set(snapshot['targets']) | set(integration_targets) | set(refresh_proof['additional_context_keys']):
                s, r = material(identifier)
                all_pins[identifier] = pin(s, r)
            for identifier, entry in selected.items():
                source, _ = material(identifier)
                row = entry['row']  # latest impact metadata, not the earliest duplicate
                audit = dict(code_id=row['code_id'], source_id=row['source_id'], assessment=copy.deepcopy(row['substantive_impact']),
                    certificate=certificate(row, source, policy['policy-coordinations.json']),
                    source_body_sha256=digest(source['source_xml']),
                    reviewed_by='Contrelecture intégrale IA indépendante du rédacteur ; variantes finales et analyses dépendantes recertifiées selon le plan final approuvé',
                    approved_at=stamp, evidence_file=str(entry['proof'].relative_to(B)), evidence_sha256=entry['proof_sha256'],
                    reference_recertification=refresh_proof,
                    dependency_guards=[value for target, value in sorted(all_pins.items()) if target != identifier],
                    semantic_review_by_jurist=False)
                if identifier in old_entries:
                    audit['superseded_audit_history'] = copy.deepcopy(old_entries[identifier].get('superseded_audit_history', []))
                    audit['superseded_audit_history'].append(copy.deepcopy(old_entries[identifier]))
                entries[identifier] = audit
                adopted.append(dict(key=identifier, package=entry['spec']['folder'], classification=row['substantive_impact']['classification']))
            require(set(old_entries) <= set(entries), 'Prior audit disappeared')
            for identifier in set(old_entries) - allowed_prior - set(selected):
                require(entries[identifier] == old_entries[identifier], 'Previously expired unadopted audit must remain identical: ' + identifier)
            for path, expected in tracked.items():
                require(file_sha(path) == expected, 'Tracked input changed before ledger adoption: ' + str(path))
            require(ledger.read_bytes() == old_raw, 'Audit ledger changed concurrently')
            require(rc.policy_state() == policy, 'Policy changed before adoption')
            new = dict(version=1, scope='Bounded independently counter-read whole texts; no corpus-wide net balance or jurist audit',
                approved_at=stamp, policy_sha256=policy['policy-coordinations.json'], audits=list(entries.values()))
            new_raw = encoded(new)
            old_sha = sha_bytes(old_raw)
            history = P / 'audit-ledger-history' / (old_sha + '.json')
            archived_write(history, old_raw)
            report = dict(adopted_at=stamp, prior_ledger_sha256=old_sha, resulting_ledger_sha256=sha_bytes(new_raw),
                policy_sha256=policy, registration_sha256=file_sha(registration_path),
                prior_count=len(old_entries), stored_audits=len(entries), phase_c_articles=len(adopted),
                prior_independent_allowlist_count=len(allowed_prior),
                prior_allowlist_file=str(phase_b_adoption_path.relative_to(B)),
                prior_allowlist_sha256=file_sha(phase_b_adoption_path),
                prior_exactly_reattested=prior_valid, prior_stale_kept_with_original_certificate=prior_stale,
                adopted=adopted, package_lineage=lineage, reference_recertification=refresh_proof,
                global_net_reduction='not_established', national_savings=None, semantic_review_by_jurist=False,
                exhaustive_rewriting_complete=False, no_SQLite_or_policy_or_site_mutation=True)
            # Archive the previous ledger and prepare receipt before active replacement.
            # A failed check above performs NO ledger/report mutation.
            atomic_bytes(P / 'audit-adoption.json', encoded(report))
            atomic_bytes(ledger, new_raw)
            print(json.dumps(dict(phase_c=len(adopted), stored=len(entries), prior_reattested=len(prior_valid),
                                 prior_stale=len(prior_stale), global_net_reduction='not_established')))
        finally:
            db.close()


if __name__ == '__main__':
    main()
