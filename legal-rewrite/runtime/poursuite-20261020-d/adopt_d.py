"""Adopt only the 25 frozen, independently reviewed D dispositions.

The prior 428 readings are preserved byte-for-byte as objects, including any
now-stale dependency pins. Context compatibility is a separate operation.
No canonical articles, policies or validators are changed by this command.
"""
from pathlib import Path
from datetime import datetime, timezone
import copy
import importlib.util
import json
import sqlite3
import sys

P = Path(__file__).resolve().parent
B = P.parents[1]
sys.path.insert(0, str(B))
spec = importlib.util.spec_from_file_location('phase_c_evidence', P.parent / 'poursuite-20261020-c/adopt_reviewed.py')
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
from ingest import source_notes, xml_contents
from register_batches import writer_lock
from substantive_impact import certificate, validate
import reference_coherence as rc
from build_substantive_report import _checked


def main():
    with writer_lock():
        tracked = {}
        def read(path):
            raw = path.read_bytes()
            tracked[path] = c.sha_bytes(raw)
            return json.loads(raw)
        frozen = P / 'fiscal/edition002'
        manifest = read(frozen / 'manifest.json')
        c.require(manifest['frozen'] is True, 'Unfrozen D package')
        for name, sha in manifest['files_sha256'].items():
            c.require(c.file_sha(frozen / name) == sha, 'Changed frozen D file: ' + name)
            tracked[frozen / name] = sha
        review_path = P / 'fiscal-independent-review/edition002/review.json'
        review = read(review_path)
        c.require(review['verdict'] == 'approved_bounded_independent_review', 'No independent approval')
        c.require(not review.get('blocking_findings'), 'Blocking findings remain')
        pack = P / 'integration/edition001'
        sources, rows = read(pack / 'source.json'), read(pack / 'answer.json')
        pre = read(pack / 'preflight.json')
        registration = read(pack / 'registration.json')
        root = read(P / 'root-independent-review.json')
        c.require(len(rows) == len(sources) == registration['registered_articles'] == 25, 'Wrong selection')
        c.require(len({c.key(r) for r in rows}) == 25, 'Duplicate D source')
        for field, path in [('source_sha256', pack / 'source.json'), ('answer_sha256', pack / 'answer.json')]:
            c.require(pre[field] == root[field] == c.file_sha(path), 'Changed root-reviewed D package')
        c.require(pre['independent_review_sha256'] == c.file_sha(review_path), 'Changed independent review')
        c.require(c.file_sha(frozen / 'answer.json') in c.hashes_in(review)
                  and c.file_sha(frozen / 'companion-answer.json') in c.hashes_in(review),
                  'Review does not bind both exact final answers')
        c.require(rows == read(frozen / 'answer.json') + read(frozen / 'companion-answer.json'), 'Staged answer mismatch')
        c.require(sources == read(frozen / 'source.json') + read(frozen / 'companion-source.json'), 'Staged source mismatch')
        policy = rc.policy_state()
        for name, sha in policy.items():
            c.require(c.file_sha(frozen / name) == sha, 'Policy changed since D reading')
            tracked[B / name] = sha
        snapshot = read(pack / 'reference-targets.json')
        db = sqlite3.connect('file:' + str(B / 'corpus.sqlite') + '?mode=ro', uri=True)
        db.execute('BEGIN')
        try:
            rc.check_guards(db, snapshot)
            materials = {}
            for identifier in {c.key(s) for s in sources} | set(snapshot['targets']):
                source = c.verified_sources(db, identifier, source_notes, xml_contents)
                row = c.source_only_or_draft(db, source)
                materials[identifier] = source, row
            guards = {k: c.pin(s, r) for k, (s, r) in materials.items()}
            ledger = B / 'runtime/substantive-audits.json'
            old_raw = ledger.read_bytes()
            old = json.loads(old_raw)
            old_entries = {c.key(a): a for a in old['audits']}
            c.require(len(old_entries) == len(old['audits']) == 428, 'Unexpected ledger; obtain a fresh edition')
            c.require(not ({c.key(r) for r in rows} & set(old_entries)), 'D audit already exists')
            stamp = datetime.now(timezone.utc).isoformat()
            additions = []
            for expected, row in zip(sources, rows):
                identifier = c.key(row)
                source, _ = materials[identifier]
                c.require(all(source[k] == expected[k] for k in ('source_sha256', 'source_xml', 'source_notes_xml')), 'Changed D source')
                actual = c.current_row(db, source)
                c.require(all(actual[k] == row[k] for k in ('source_sha256', 'status', 'proposed_xml')), 'Changed registered D proposal')
                notes = db.execute('SELECT reason,review_notes FROM drafts WHERE code_id=? AND source_id=?', identifier.split('|')).fetchone()
                c.require(notes == (row['reason'], row['review_notes']), 'Changed D registered notes')
                validate(copy.deepcopy(row), source, required=True, enforce_workflow=False)
                if row.get('reference_coherence'):
                    c.require(rc.certificate_current(db, source, row.get('proposed_xml'), row['reference_coherence']), 'Stale D reference certificate')
                audit = dict(code_id=row['code_id'], source_id=row['source_id'],
                             assessment=copy.deepcopy(row['substantive_impact']),
                             certificate=certificate(row, source, policy['policy-coordinations.json']),
                             source_body_sha256=c.digest(source['source_xml']),
                             reviewed_by='Contrelecture intégrale IA indépendante du rédacteur, édition fiscale D002 ; lecture intégrale du parent',
                             approved_at=stamp, evidence_file=str(review_path.relative_to(B)),
                             evidence_sha256=c.file_sha(review_path),
                             parent_review_file=str((P / 'root-independent-review.json').relative_to(B)),
                             parent_review_sha256=c.file_sha(P / 'root-independent-review.json'),
                             dependency_guards=[v for k, v in sorted(guards.items()) if k != identifier],
                             semantic_review_by_jurist=False)
                exported = {(s['code_id'], s['source_id']): dict(s, **r) for s, r in materials.values()}
                c.require(_checked(audit, dict(source, **actual), policy['policy-coordinations.json'], approved=True, exported=exported) == audit['assessment'], 'Invalid new impact certificate')
                additions.append(audit)
            for path, sha in tracked.items():
                c.require(c.file_sha(path) == sha, 'Tracked evidence changed: ' + str(path))
            c.require(ledger.read_bytes() == old_raw and rc.policy_state() == policy, 'Concurrent change before adoption')
            c.archived_write(P / 'audit-ledger-history' / (c.sha_bytes(old_raw) + '.json'), old_raw)
            new = copy.deepcopy(old)
            new['audits'].extend(additions)
            new['approved_at'] = stamp
            c.require(new['audits'][:428] == old['audits'], 'Prior audit mutated')
            raw = c.encoded(new)
            c.atomic_bytes(ledger, raw)
            receipt = dict(adopted_at=stamp, new_independent_readings=25, stored_audits=453,
                           previous_audits_left_entirely_unchanged=428, policy_sha256=policy,
                           previous_ledger_sha256=c.sha_bytes(old_raw), resulting_ledger_sha256=c.sha_bytes(raw),
                           source_sha256=c.file_sha(pack / 'source.json'), answer_sha256=c.file_sha(pack / 'answer.json'),
                           independent_review_sha256=c.file_sha(review_path),
                           exhaustive_rewriting_complete=False, semantic_review_by_jurist=False,
                           global_net_complexity_reduction='not_established', national_savings=None)
            c.atomic_bytes(P / 'audit-adoption.json', c.encoded(receipt))
            print(json.dumps(receipt, ensure_ascii=False, indent=2))
        finally:
            db.close()


if __name__ == '__main__':
    main()
