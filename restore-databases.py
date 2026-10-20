"""Restore the SQLite snapshots from the checked-in gzip parts."""
from pathlib import Path
import gzip,hashlib,json,shutil,tempfile
root=Path(__file__).resolve().parent
for item in json.loads((root/'database-parts.json').read_text()):
    target=root/item['path']
    if target.exists():
        raise SystemExit(f'Refusing to overwrite {target}')
    with tempfile.TemporaryFile() as archive:
        for part in item['parts']:
            with (root/part).open('rb') as source:
                shutil.copyfileobj(source,archive)
        archive.seek(0)
        temporary=target.with_suffix('.restoring')
        with gzip.GzipFile(fileobj=archive) as source, temporary.open('wb') as output:
            shutil.copyfileobj(source,output)
        with temporary.open('rb') as restored:
            assert hashlib.file_digest(restored,'sha256').hexdigest()==item['sha256'], 'Checksum mismatch'
        temporary.rename(target)
    print(f'Restored {item["path"]}')
