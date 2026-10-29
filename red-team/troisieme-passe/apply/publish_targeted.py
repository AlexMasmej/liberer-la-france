#!/usr/bin/env python3
"""Targeted publication of the current legal state to the GitHub export checkout (no push).

Usage: python3 -B apply/publish_targeted.py <since-ISO-UTC>   e.g. 2026-10-29T07:40:00Z
Copies into /private/tmp/liberer-france-export, fast-forwarded to origin/main:
  legal-rewrite/batches/, registered-batches.json, batch-validation.json, progress.json,
  revisions/radical-review/ archives newer than <since>, the five sites' dist/,
  consistent compressed parts of every changed database (same method as prepare-france-export.py),
  and the third-pass documentation (red-team/troisieme-passe/).
Oversized files are then split by the project's package-large-exports.py; secrets, size and
database restoration are checked; the result is staged. Runtime logs are never copied.
"""
import gzip, hashlib, json, re, shutil, sqlite3, subprocess, sys, tempfile, time
from contextlib import closing
from datetime import datetime
from pathlib import Path

PROJECT = Path('/Users/alexandremasmejean/.codex/.chatgpt-projects/g-p-6ad59c015c308191aa21cba63c71a6dc')
PROD = PROJECT / 'legal-rewrite'
EXPORT = Path('/private/tmp/liberer-france-export')
THIRD = Path(__file__).resolve().parent.parent
SITES = ['liberer-la-retraite', 'liberer-le-logement', 'liberer-le-revenu', 'liberer-lentreprise', 'nouveaudroitdutravail']
SECRET = re.compile(rb'(?:gh[pousr]_[A-Za-z0-9]{25,}|github_pat_[A-Za-z0-9_]{30,}|past_sk_[A-Za-z0-9_-]{15,}|sk-proj-[A-Za-z0-9_-]{20,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|Bearer\s+[A-Za-z0-9_.-]{30,}|"(?:access_token|refresh_token|api_key|password)"\s*:\s*"[^"\s]{12,}")', re.I)


def git(*args):
    return subprocess.check_output(['git', '-C', str(EXPORT), *args], text=True).strip()


def rsync(src, dst, *excludes):
    subprocess.run(['rsync', '-a', *sum([['--exclude', e] for e in excludes], []), f'{src}/', f'{dst}/'], check=True)


def databases():
    index = json.loads((EXPORT / 'database-parts.json').read_text())
    out, changed = [], []
    for item in index:
        src = PROJECT / item['path']
        if not src.exists():
            out.append(item); continue
        with tempfile.TemporaryDirectory() as tmp:
            temp = Path(tmp) / 'db.sqlite'
            with closing(sqlite3.connect(f'file:{src}?mode=ro', uri=True)) as a, closing(sqlite3.connect(temp)) as b:
                a.backup(b)
            with temp.open('rb') as f:
                digest = hashlib.file_digest(f, 'sha256').hexdigest()
            if digest == item['sha256']:
                out.append(item); continue
            gz = Path(tmp) / 'db.gz'
            with temp.open('rb') as a, gzip.open(gz, 'wb', compresslevel=6) as b:
                shutil.copyfileobj(a, b)
            parts, i = [], 0
            with gz.open('rb') as f:
                while chunk := f.read(48 * 1024 * 1024):
                    name = item['path'] + f'.gz.part{i:03d}'
                    (EXPORT / name).write_bytes(chunk); parts.append(name); i += 1
        base = EXPORT / item['path']
        for old in base.parent.glob(base.name + '.gz.part*'):
            if str(old.relative_to(EXPORT)) not in parts:
                old.unlink()
        out.append(dict(item, parts=parts, sha256=digest)); changed.append(item['path'])
    (EXPORT / 'database-parts.json').write_text(json.dumps(out, indent=2) + '\n')
    return changed, out


def main(since):
    cut = datetime.fromisoformat(since.replace('Z', '+00:00')).timestamp()
    git('checkout', '-q', '--', '.'); git('clean', '-fdq')
    git('fetch', '-q', 'origin', 'main'); git('merge', '-q', '--ff-only', 'origin/main')
    rsync(PROD / 'batches', EXPORT / 'legal-rewrite/batches', '*.tmp')
    for name in ('registered-batches.json', 'batch-validation.json', 'progress.json'):
        shutil.copy2(PROD / name, EXPORT / 'legal-rewrite' / name)
    archives = [p for p in (PROD / 'revisions/radical-review').glob('*.json') if p.stat().st_mtime >= cut]
    for p in archives:
        shutil.copy2(p, EXPORT / 'legal-rewrite/revisions/radical-review' / p.name)
    for site in SITES:
        rsync(PROJECT / 'sites' / site / 'dist', EXPORT / 'sites' / site / 'dist', '.env*', 'node_modules')
    changed_db, index = databases()
    red = EXPORT / 'red-team/troisieme-passe'
    for brief in THIRD.glob('BRIEF-*.md'):
        shutil.copy2(brief, red / brief.name)
    rsync(THIRD / 'apply', red / 'apply', '__pycache__', 'TEST', 'changes.before-coordinator.json')
    rsync(THIRD / 'reports', red / 'reports', 'new-repeals-since-audit-*')
    rsync(THIRD / 'issues', red / 'issues')
    rsync(THIRD / 'audit', red / 'audit')
    subprocess.run([sys.executable, '-B', str(PROJECT / 'github-sync-support/package-large-exports.py')], check=True)
    git('add', '-A')
    names = [n for n in git('diff', '--cached', '--name-only', '-z').split('\0') if n]
    secrets, big = [], []
    for n in names:
        p = EXPORT / n
        if not p.exists():
            continue
        if p.stat().st_size >= 100 * 1024 * 1024:
            big.append(n)
        if p.suffix in ('.json', '.jsonl', '.md', '.py', '.html', '.txt', '.js') and SECRET.search(p.read_bytes()):
            secrets.append(n)
    for item in index:
        if item['path'] not in changed_db:
            continue
        with tempfile.TemporaryFile() as c:
            for part in item['parts']:
                with (EXPORT / part).open('rb') as f:
                    shutil.copyfileobj(f, c)
            c.seek(0)
            with gzip.GzipFile(fileobj=c) as f:
                assert hashlib.file_digest(f, 'sha256').hexdigest() == item['sha256'], item['path']
    runtime = [n for n in names if n.startswith('legal-rewrite/runtime/')]
    print(json.dumps(dict(staged=len(names), archives=len(archives), databases_changed=changed_db,
                          secrets=secrets, over_100MiB=big, runtime_files=len(runtime),
                          shortstat=git('diff', '--cached', '--shortstat')), indent=1))
    if secrets or big or runtime:
        sys.exit('refusing: secrets, oversized files or runtime logs staged')
    print('TARGETED_EXPORT_READY')


if __name__ == '__main__':
    main(sys.argv[1])
