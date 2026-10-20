"""Register the five approved reference metadata updates under one writer lock.

SQLite has no reference-metadata columns. Only the two reference fields in the
actual owning batches change. No body, impact, registry or workflow field is
changed, and this operation counts no additional drafted article.
"""
from pathlib import Path
from datetime import datetime, timezone
import copy
import importlib.util
import json
import sys

P = Path(__file__).resolve().parent
B = P.parents[1]
sys.path.insert(0, str(B))
from register_batches import writer_lock
import reference_coherence as rc
from run_exhaustive import validate_answer


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def main():
    c = module('archive_primitives', P.parent / 'poursuite-20261020-c/adopt_reviewed.py')
    producer = P / 'social-coordination/recertificate-helper/edition004/prepare_recertificates.py'
    c.require(c.file_sha(producer) == '04fa85c0e85384fc30979155e5136bfb5d24d88f94789afda27b8733cf6f6f21', 'Changed capture helper')
    h = module('actual_capture', producer)
    cap = P / 'social-coordination/recertification/captured001'
    stage = P / 'social-coordination/recertification/staged001'
    c.require(not (stage / 'registration.json').exists(), 'Metadata already registered')
    with writer_lock():
        capture = c.load(cap / 'capture.json')
        proof = c.load(stage / 'staging.json')
        approval = c.load(cap / 'root-approval.json')
        c.require(capture['helper_sha256'] == c.file_sha(producer), 'Capture producer differs')
        c.require(proof['capture_sha256'] == c.file_sha(cap / 'capture.json') == approval['capture_sha256'], 'Capture lineage differs')
        c.require(proof['approval_sha256'] == c.file_sha(cap / 'root-approval.json') and approval['approved'] is True and approval['approved_by'] == 'root', 'No exact parent approval')
        for name, sha in capture['files'].items():
            c.require(c.file_sha(cap / name) == sha, 'Captured evidence changed')
        for name, sha in proof['files'].items():
            c.require(c.file_sha(stage / name) == sha, 'Staged evidence changed')
        before, rows, sources = c.load(cap / 'before-answer.json'), c.load(stage / 'answer.json'), c.load(stage / 'source.json')
        keys = {c.key(r) for r in rows}
        c.require(len(keys) == len(rows) == 5 and keys == {c.key(r) for r in before}, 'Wrong five identities')
        for old, new in zip(before, rows):
            c.require(c.key(old) == c.key(new), 'Changed metadata order')
            h.unchanged_except_references(old, new)
        snapshot = c.load(stage / 'reference-targets.json')
        owners = c.load(cap / 'batch-owners.json')
        db = h.connect()
        try:
            for key, record in c.load(cap / 'db-records.json').items():
                c.require(h.db_record(db, key) == record, 'Actual full DB/raw/notes/proposal changed: ' + key)
            c.require(h.owners(keys) == owners, 'Actual owning batches changed')
            rc.check_guards(db, snapshot)
            validate_answer(copy.deepcopy(rows), copy.deepcopy(sources))
            for source, row in zip(sources, rows):
                c.require(rc.certificate_current(db, source, row['proposed_xml'], row['reference_coherence']), 'Not a current native certificate')
            files, originals = {}, {}
            for row in rows:
                owner = owners[c.key(row)]
                path = c.within(B, owner['path'])
                raw = path.read_bytes()
                c.require(c.sha_bytes(raw) == owner['file_sha256'], 'Owner file changed under lock')
                if path not in files:
                    originals[path] = raw
                    files[path] = json.loads(raw)
                c.require(files[path][owner['index']] == owner['row'], 'Owner row changed')
                files[path][owner['index']] = row
            for path, raw in originals.items():
                c.archived_write(P / 'reference-metadata-history' / (c.sha_bytes(raw) + '.json'), raw)
            changed = []
            try:
                for path, value in files.items():
                    c.atomic_bytes(path, c.encoded(value))
                    changed.append(path)
                actual_owners = h.owners(keys)
                c.require(all(actual_owners[c.key(row)]['row'] == row for row in rows), 'Metadata write differs')
            except BaseException:
                for path in reversed(changed):
                    c.atomic_bytes(path, originals[path])
                raise
            receipt = dict(registered_at=datetime.now(timezone.utc).isoformat(), registered_articles=5,
                           first_drafts=0, revisions=5, metadata_only=True, normative_bodies_changed=0,
                           impacts_changed=0, workflow_fields_changed=0, sqlite_changed=False, registry_changed=False,
                           capture_sha256=c.file_sha(cap / 'capture.json'), approval_sha256=c.file_sha(cap / 'root-approval.json'),
                           staging_sha256=c.file_sha(stage / 'staging.json'),
                           checks=[dict(code_id=row['code_id'], source_id=row['source_id'], number=row['number'],
                                        source_and_notes_verified=True, prior_checked=True,
                                        proposed_sha256=c.digest(row['proposed_xml'])) for row in rows],
                           owning_files=[dict(path=str(path.relative_to(B)), before_sha256=c.sha_bytes(originals[path]),
                                              after_sha256=c.file_sha(path)) for path in files],
                           exhaustive_rewriting_complete=False)
            c.atomic_bytes(stage / 'registration.json', c.encoded(receipt))
            print(json.dumps({k:v for k,v in receipt.items() if k not in ('checks', 'owning_files')}, ensure_ascii=False, indent=2))
        finally:
            db.rollback()
            db.close()


if __name__ == '__main__':
    main()
