"""Lossless storage maintenance for completed, non-current generated audits.

Original capture and manifest files remain unchanged. Archived data retain their
original byte hashes and can be restored into a temporary inspection folder.
Never operates on the live corpus, canonical sources, or the current audit.
"""
from datetime import datetime, timezone
import gzip
import hashlib
import json
import os
from pathlib import Path

RUNTIME = Path(__file__).resolve().parents[1]
POINTER = RUNTIME / 'global-reference-audit-latest.json'
ALLOWED = ('corpus.snapshot.sqlite', 'edges.jsonl', 'findings.jsonl', 'queue.json')


def sha(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def atomic(path, value):
    temporary = path.with_name(path.name + '.tmp')
    with temporary.open('w') as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write('\n')
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


def current():
    return Path(json.loads(POINTER.read_text())['folder']).resolve()


def archive(folder, name, expected):
    assert folder != current(), 'Current audit is excluded'
    assert name in ALLOWED and folder.parent == RUNTIME
    source = folder / name
    archive_path = source.with_name(name + '.gz')
    receipt = folder / 'storage-data-archives.json'
    prior = json.loads(receipt.read_text()) if receipt.exists() else {'files': []}
    if not source.exists():
        return 0
    before = source.stat()
    assert sha(source) == expected['sha256'] and before.st_size == expected['bytes']
    if name.endswith('.sqlite'):
        wal = source.with_name(name + '-wal')
        assert not wal.exists() or wal.stat().st_size == 0
    assert not archive_path.exists(), 'Existing archive must be reviewed first'
    temporary = archive_path.with_name(archive_path.name + '.partial')
    assert not temporary.exists(), 'Preserve and review interrupted compression first'
    with source.open('rb') as src, temporary.open('wb') as raw:
        with gzip.GzipFile(filename='', mode='wb', fileobj=raw,
                           compresslevel=1, mtime=0) as dst:
            while chunk := src.read(1024 * 1024):
                dst.write(chunk)
        raw.flush()
        os.fsync(raw.fileno())
    restored, digest = 0, hashlib.sha256()
    with gzip.open(temporary, 'rb') as stream:
        while chunk := stream.read(1024 * 1024):
            restored += len(chunk)
            digest.update(chunk)
    assert restored == before.st_size and digest.hexdigest() == expected['sha256']
    assert folder != current() and sha(source) == expected['sha256']
    assert source.stat().st_mtime_ns == before.st_mtime_ns
    os.replace(temporary, archive_path)
    proof = {
        'at_utc': datetime.now(timezone.utc).isoformat(),
        'original_name': name, 'original_bytes': before.st_size,
        'original_sha256': expected['sha256'], 'archive_name': archive_path.name,
        'compressed_bytes': archive_path.stat().st_size,
        'gzip_sha256': sha(archive_path), 'decompression_verified': True,
        'original_manifests_unchanged': True,
        'restoration': 'Decompress into a new temporary inspection folder; compare original_sha256.',
    }
    prior['files'].append(proof)
    atomic(receipt, prior)
    source.unlink()
    saved = before.st_size - archive_path.stat().st_size
    print(json.dumps({'folder': folder.name, 'file': name, 'saved_bytes': saved}), flush=True)
    return saved


def main():
    saved = 0
    for folder in sorted(RUNTIME.glob('global-reference-audit-*')):
        if not folder.is_dir() or folder == current():
            continue
        validation = folder / 'validation.json'
        manifest = folder / 'artifact-manifest.json'
        if not validation.exists() or not manifest.exists():
            continue
        check = json.loads(validation.read_text())
        if not check.get('checks_passed') or check.get('errors'):
            continue
        files = json.loads(manifest.read_text())['files']
        if isinstance(files, list):
            files = {row['path']: row for row in files}
        capture = json.loads((folder / 'capture.json').read_text())
        for name in ALLOWED:
            source = folder / name
            if not source.exists() or source.stat().st_size < 64 * 1024 * 1024:
                continue
            expected = files.get(name)
            if expected is None and name == 'corpus.snapshot.sqlite':
                expected = {'sha256': capture['snapshot_sha256'], 'bytes': source.stat().st_size}
            assert expected is not None, 'Original byte proof missing'
            saved += archive(folder, name, expected)
    print(json.dumps({'saved_bytes': saved, 'current_audit_untouched': True,
                      'live_corpus_and_sources_untouched': True}), flush=True)


if __name__ == '__main__':
    main()
