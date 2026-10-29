#!/usr/bin/env python3
"""Frozen, hashed snapshot of the legal-rewrite production for the third-pass red-team.

Read-only on production: SQLite opened with mode=ro + query_only, files only read.
Order: DB online backup (single step, one read transaction) -> file copies ->
re-hash of the production files copied -> cross-checks of the frozen DB against the
registry AND every owner batch row (source, status, proposal, reason, notes).
Any write caught in flight makes the attempt fail and retry.

Rotation (author's instruction of 2026-10-26): once a new snapshot is verified, older
snapshot folders are deleted; their extended manifests stay in ../manifests/, and
texts cited in findings live in ../evidence/cited/, never rotated.
"""
import datetime, hashlib, json, shutil, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from corpus import connect, digest, row_digest, owners, article_states
import sqlite3

PROD = Path('/Users/alexandremasmejean/.codex/.chatgpt-projects/'
            'g-p-6ad59c015c308191aa21cba63c71a6dc/legal-rewrite')
HOME = Path(__file__).resolve().parent.parent
SNAPSHOTS, MANIFESTS = HOME / 'snapshots', HOME / 'manifests'

FILES = ['GUIDE-TROISIEME-PASSE.md', 'README.md', 'policy-coordinations.json',
         'site-summaries.json', 'registered-batches.json', 'progress.json',
         'reference-focus-extra.json', 'source-image-gaps.json', 'extended-graphic-gaps.json',
         'official-code-registry.json', 'corpus.json', 'archive-manifest.json',
         'runtime/radical-review-20261019.json', 'runtime/exhaustive/status.json',
         'runtime/global-reference-audit-latest.json', 'runtime/supervision/status.json',
         'runtime/contrat-unique-20261019/priority/excluded-packs.json',
         'runtime/contrat-unique-20261019/priority/priority-targets.proposed.json']
TREES = ['notes-contradictions', 'batches', 'coordinations', 'attachments']


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def backup_db(dest):
    src = sqlite3.connect((PROD / 'corpus.sqlite').as_uri() + '?mode=ro', uri=True, timeout=60)
    src.execute('pragma query_only=1')
    out = sqlite3.connect(dest / 'corpus.sqlite')
    src.backup(out, pages=-1)          # single step: one consistent read transaction
    out.execute('pragma journal_mode=delete')
    out.close(); src.close()


def copy_inputs(dest):
    hashes = {}
    for rel in FILES:
        if not (PROD / rel).exists():
            hashes[rel] = None
            continue
        (dest / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(PROD / rel, dest / rel)
        hashes[rel] = sha(dest / rel)
    for rel in TREES:
        shutil.copytree(PROD / rel, dest / rel)
        hashes.update({str(p.relative_to(dest)): sha(p)
                       for p in sorted((dest / rel).rglob('*')) if p.is_file()})
    return hashes


def changed_during_copy(hashes):
    """Production files whose content differs from the frozen copy after the copy."""
    return sorted(rel for rel, h in hashes.items()
                  if h is not None and (not (PROD / rel).exists() or sha(PROD / rel) != h))


def cross_check(dest):
    db = connect(dest)
    assert db.execute('pragma integrity_check').fetchone()[0] == 'ok'
    drafts = {f'{c}|{i}': (sh, st, p, r, n) for c, i, sh, st, p, r, n in db.execute(
        'select code_id,source_id,source_sha256,status,proposed_xml,reason,review_notes from drafts')}
    db.close()
    registry = json.load(open(dest / 'registered-batches.json'))
    own, dup = owners(dest)
    bad = []
    for key, r in registry.items():
        d = drafts.get(key)
        if d is None or r['source_sha256'] != d[0] or r['proposed_sha256'] != digest(d[2]):
            bad.append(('registry', key))
    for key, (path, index, row) in own.items():
        d = drafts.get(key)
        if d is None:
            bad.append(('owner_without_draft', key)); continue
        if (row['source_sha256'], row.get('status', 'rewrite_draft'), row.get('proposed_xml'),
                row.get('reason'), row.get('review_notes')) != d[:5]:
            bad.append(('owner_row', key))
    return bad + [('duplicate_owner', k) for k in dup]


def extended_manifest(dest):
    arts, notes, dsrc, drafts = article_states(dest)
    own, _ = owners(dest)
    inv = json.load(open(dest / 'runtime/radical-review-20261019.json'))
    review = {f"{a['code_id']}|{a['source_id']}": a['review_status'] for a in inv['prior_articles']}
    review.update({f"{a['code_id']}|{a['source_id']}": 'documentary_hold'
                   for a in inv['documentary_holds']})
    out = {}
    for key in sorted(set(drafts) | set(review)):
        rec = dict(arts.get(key, {}))
        rec['source_notes_sha256'] = notes.get(key, digest(''))
        rec.update(dsrc.get(key, {}))
        rec.update(drafts.get(key, {}))
        o = own.get(key)
        rec['owner'] = o[0] if o else None
        rec['batch_row_sha256'] = row_digest(o[2]) if o else None
        rec['second_pass'] = review.get(key, 'outside_current_inventory')
        out[key] = rec
    return out


def main(attempts=5):
    SNAPSHOTS.mkdir(parents=True, exist_ok=True); MANIFESTS.mkdir(parents=True, exist_ok=True)
    for attempt in range(1, attempts + 1):
        stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
        dest = SNAPSHOTS / stamp
        dest.mkdir()
        backup_db(dest)
        hashes = copy_inputs(dest)
        moved = changed_during_copy(hashes)
        bad = cross_check(dest)
        if not moved and not bad:
            break
        print(f'attempt {attempt}: {len(moved)} files moved during copy, {len(bad)} cross-check '
              f'failures {bad[:5]}; retrying', file=sys.stderr)
        shutil.rmtree(dest)
        time.sleep(20)
    else:
        sys.exit('no consistent snapshot after %d attempts' % attempts)

    hashes['corpus.sqlite'] = sha(dest / 'corpus.sqlite')
    status = json.load(open(dest / 'runtime/exhaustive/status.json'))
    manifest = {
        'snapshot_id': stamp, 'production_root': str(PROD), 'corpus_as_of': '2026-10-18',
        'method': 'sqlite online backup first (mode=ro, query_only, single step), then file '
                  'copies re-hashed against production after copy; frozen DB cross-checked '
                  'against registry and every active owner row (source, status, proposal, '
                  'reason, review notes); retry on any discrepancy',
        'attempt': attempt,
        'second_pass_counters': {k: status.get(k) for k in
                                 ('status', 'updated_at_unix', 'prior_drafts_reviewed',
                                  'prior_drafts_awaiting_review', 'drafted_articles',
                                  'retained_unchanged', 'pending', 'jurist_reviewed_articles')},
        'policy_sha256': {k: hashes.get(k) for k in ('policy-coordinations.json', 'site-summaries.json',
                                                      'reference-focus-extra.json',
                                                      'runtime/contrat-unique-20261019/priority/excluded-packs.json',
                                                      'runtime/contrat-unique-20261019/priority/priority-targets.proposed.json')},
        'file_sha256': hashes,
        'articles': extended_manifest(dest),
    }
    (dest / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=1))
    shutil.copy2(dest / 'manifest.json', MANIFESTS / f'{stamp}.json')

    # Rotation: the new snapshot is written and verified; drop older heavy copies.
    for old in SNAPSHOTS.iterdir():
        if old.is_dir() and old.name != stamp:
            if not (MANIFESTS / f'{old.name}.json').exists() and (old / 'manifest.json').exists():
                shutil.copy2(old / 'manifest.json', MANIFESTS / f'{old.name}.json')
            shutil.rmtree(old)
            print('removed old snapshot', old.name)
    (SNAPSHOTS / 'LATEST').write_text(stamp + '\n')
    print(json.dumps({k: manifest[k] for k in ('snapshot_id', 'attempt', 'second_pass_counters')},
                     ensure_ascii=False, indent=1))
    print('corpus.sqlite sha256', hashes['corpus.sqlite'])


if __name__ == '__main__':
    main()
