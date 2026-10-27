#!/usr/bin/env python3
"""Copy the dated (sealed) evidence folders cited by notes-contradictions/INDEX.md and the
25 October audit details into ../evidence/sealed/, never rotated.

Every file is hashed; files above LIMIT are hashed but not copied unless whitelisted.
Re-running verifies that production's sealed folders have not changed since the copy.
"""
import hashlib, json, shutil, sys
from pathlib import Path

PROD = Path('/Users/alexandremasmejean/.codex/.chatgpt-projects/'
            'g-p-6ad59c015c308191aa21cba63c71a6dc/legal-rewrite')
DEST = Path(__file__).resolve().parent.parent / 'evidence' / 'sealed'
LIMIT = 3 << 20
FOLDERS = [
    'runtime/coherence-joint-twelve-readonly-20261025T1915Z',
    'runtime/coherence-joint-twelve-typed-guard-20261025T2012Z',
    'runtime/institut-nomination-note-readonly-20261026T0656Z',
    'runtime/union-statutes-public-source-followup-20261026T0546Z',
    'runtime/union-statutes-normative-followup-20261026T0245Z',
    'runtime/alcohol-denaturation-coherence-readonly-20261026T1305Z',
    'runtime/alcohol-2005-scoped-readonly-20261026T1505Z',
    'runtime/alcohol-2005-normative-followup-20261026T1501Z',
    'runtime/alcohol-2006-normative-followup-20261026T1600Z',
    'runtime/cibs-alcohol-public-followup-20261026T1707Z',
    'runtime/cibs-2021-primary-pistes-followup-20261026T1808Z',
    'runtime/coherence-nine-activation-20261024T0553Z',
    'runtime/tsca-two-activation-20261024T1222Z',
    'runtime/source-recovery-20261022/css/captcha-authorized-followup',
    'runtime/source-recovery-20261022/css/pages',
    'runtime/source-recovery-20261022/css/web',
    'runtime/source-recovery-followup-20261024',
    'runtime/validation-optimization-20261024',
    'runtime/validation-optimization-20261026',
    'runtime/global-reference-audit-20261025T2341Z',
    'runtime/cvae-semantic-recheck-20261023T1956Z',
    'runtime/l1242-semantic-recheck-20261022T183007Z',
]
# Large audit results needed to qualify P1 findings.
WHITELIST = {'findings.jsonl', 'queue.json', 'article-manifest.jsonl', 'global-validation-diagnostics.json'}


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


manifest_path = DEST / 'sealed-manifest.json'
previous = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
manifest, changed = {}, []
for folder in FOLDERS:
    root = PROD / folder
    if not root.exists():
        manifest[folder] = None; continue
    for path in sorted(p for p in root.rglob('*') if p.is_file() or p.is_symlink()):
        rel = str(path.relative_to(PROD))
        if path.is_symlink():
            # Live pointers (e.g. staged-batches -> production batches/) are not sealed
            # evidence: record the target, never copy moving content.
            (DEST / rel).unlink(missing_ok=True)
            manifest[rel] = dict(symlink=str(path.readlink()), copied=False)
            continue
        h, size = sha(path), path.stat().st_size
        copied = size <= LIMIT or path.name in WHITELIST
        if rel in previous and previous[rel].get('sha256') != h:
            changed.append(rel)
        target = DEST / rel
        if copied and (not target.exists() or sha(target) != h):
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)
        manifest[rel] = dict(sha256=h, size=size, copied=copied,
                             mtime=path.stat().st_mtime)
manifest_path.write_text(json.dumps(manifest, indent=1))
print(len(manifest), 'files hashed;', sum(1 for v in manifest.values() if v and v['copied']), 'copied;', sum(1 for v in manifest.values() if v and 'symlink' in v), 'symlinks recorded', 
      'changed since previous run:', changed[:20], len(changed))
