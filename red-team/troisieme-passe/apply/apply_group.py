#!/usr/bin/env python3
"""Apply one group's validated corrections to production with the project's guarded tools.

Usage: python3 -B apply/apply_group.py <GROUP> [--commit]   (dry run by default)
- "replace" rows: review_prior.commit (before-image of DB and batch row checked and archived,
  whole-corpus registration, rollback on failure).
- "new" rows: appended to batches/third-pass-corrections/<NNNNN>.json, then whole-corpus
  registration under the writer lock; the file is removed again if registration fails.
Rows are rebuilt by check_changes.py first, so they match what the agent validated.
Every application is logged in apply/<GROUP>/applied.json with before/after hashes.
"""
import hashlib, json, sqlite3, subprocess, sys, time
from pathlib import Path

PROD = Path('/Users/alexandremasmejean/.codex/.chatgpt-projects/g-p-6ad59c015c308191aa21cba63c71a6dc/legal-rewrite')
HOME = Path(__file__).resolve().parent
sys.path.insert(0, str(PROD))
import review_prior  # noqa: E402
from review_prior import batch_owners, batch_row_sha256, draft_values  # noqa: E402
from register_batches import writer_lock, _register  # noqa: E402
from ingest import open_db  # noqa: E402


def digest(v):
    return hashlib.sha256((v or '').encode()).hexdigest()


def main(group, commit):
    if subprocess.run([sys.executable, '-B', str(HOME / 'check_changes.py'), group]).returncode:
        sys.exit('check_changes failed: fix the group before applying')
    built = json.loads((HOME / group / 'rows.built.json').read_text())
    if any('error' in b for b in built):
        sys.exit('a built row carries a validator error')
    replace = [b['row'] for b in built if b['mode'] == 'replace']
    new = [b['row'] for b in built if b['mode'] == 'new']
    db = sqlite3.connect(f'file:{PROD}/corpus.sqlite?mode=ro', uri=True)
    db.execute('pragma query_only=1')
    keys = {(r['code_id'], r['source_id']) for r in replace}
    owners, files = batch_owners(keys)
    expected, log = [], []
    for r in replace:
        key = (r['code_id'], r['source_id'])
        cur = db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?', key).fetchone()
        path, index = owners[key]
        batch = files[path][index]
        assert draft_values(batch) == cur, f'batch and DB differ: {key}'
        expected.append(dict(code_id=key[0], source_id=key[1], previous_draft=dict(
            source_sha256=cur[0], status=cur[1], proposed_xml=cur[2], reason=cur[3], review_notes=cur[4],
            proposed_sha256=digest(cur[2]), batch_row_sha256=batch_row_sha256(batch))))
        log.append(dict(mode='replace', key='|'.join(key), number=r['number'], objection=r['third_pass_correction']['objection'],
                        before=dict(proposed_sha256=digest(cur[2]), reason_sha256=digest(cur[3]), review_notes_sha256=digest(cur[4])),
                        after=dict(proposed_sha256=digest(r['proposed_xml']), reason_sha256=digest(r['reason']), review_notes_sha256=digest(r['review_notes']))))
    for r in new:
        key = (r['code_id'], r['source_id'])
        assert db.execute('SELECT 1 FROM drafts WHERE code_id=? AND source_id=?', key).fetchone() is None, f'draft appeared: {key}'
        log.append(dict(mode='new', key='|'.join(key), number=r['number'], objection=r['third_pass_correction']['objection'],
                        after=dict(proposed_sha256=digest(r['proposed_xml']), reason_sha256=digest(r['reason']), review_notes_sha256=digest(r['review_notes']))))
    db.close()
    print(f'{group}: {len(replace)} replacements, {len(new)} new rows')
    if not commit:
        print('DRY RUN — nothing written'); return
    if replace:
        review_prior.commit(replace, expected)
        print('replacements committed')
    if new:
        folder = PROD / 'batches' / 'third-pass-corrections'
        with writer_lock():
            folder.mkdir(exist_ok=True)
            index = 1 + max((int(p.stem) for p in folder.glob('*.json')), default=0)
            path = folder / f'{index:05d}.json'
            path.write_text(json.dumps(new, ensure_ascii=False, indent=2) + '\n')
            db = open_db(PROD / 'corpus.sqlite')
            try:
                _register(db, PROD / 'batches', True)
            except Exception:
                db.rollback()
                path.unlink()
                raise
            finally:
                db.close()
        print('new rows registered in', path.relative_to(PROD))
    out = HOME / group / 'applied.json'
    previous = json.loads(out.read_text()) if out.exists() else []
    previous.append(dict(applied_at_unix=time.time(), items=log))
    out.write_text(json.dumps(previous, ensure_ascii=False, indent=1))
    print('logged', out)


if __name__ == '__main__':
    main(sys.argv[1], '--commit' in sys.argv)
