"""Verify and apply this snapshot to a separately restored base checkout."""
from pathlib import Path
import argparse, gzip, hashlib, json, os, shutil, subprocess, tarfile, tempfile

here=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--destination',required=True,help='Separate base checkout, after restoring its database and large-file manifests')
args=parser.parse_args();dest=Path(args.destination).resolve()
source=Path('/Users/alexandremasmejean/.codex/.chatgpt-projects/g-p-6ad59c015c308191aa21cba63c71a6dc')
assert dest!=source and source not in dest.parents,'Never restore over drafting originals'
m=json.loads((here/'snapshot.json').read_text())
base=subprocess.check_output(['git','-C',str(dest),'rev-parse','HEAD'],text=True).strip()
assert base==m['base_commit'],'Destination must be the documented base commit'
def checked_path(name):
    p=Path(name)
    assert not p.is_absolute() and '..' not in p.parts and p.parts[0] in ('sites','legal-rewrite')
    out=dest/p
    assert not any(x.is_symlink() for x in [out,*out.parents]),'Symlink in destination'
    return out
for manifest_name in ('database-parts.json','large-file-parts.json'):
    manifest_path=dest/manifest_name
    if not manifest_path.exists():continue
    for row in json.loads(manifest_path.read_text()):
        out=checked_path(row['path'])
        if out.exists():
            with out.open('rb') as f:assert hashlib.file_digest(f,'sha256').hexdigest()==row['sha256'],f'Changed base archive: {out}'
            continue
        out.parent.mkdir(parents=True,exist_ok=True)
        with tempfile.TemporaryFile() as joined:
            for name in row['parts']:
                part=checked_path(name)
                with part.open('rb') as f:shutil.copyfileobj(f,joined)
            joined.seek(0)
            fd,tmp=tempfile.mkstemp(prefix='.base-restore-',dir=out.parent)
            try:
                with os.fdopen(fd,'wb') as target,gzip.GzipFile(fileobj=joined) as f:shutil.copyfileobj(f,target)
                with open(tmp,'rb') as f:assert hashlib.file_digest(f,'sha256').hexdigest()==row['sha256']
                os.replace(tmp,out)
            finally:
                if os.path.exists(tmp):os.unlink(tmp)
for row in m['unchanged_at_base']:
    p=checked_path(row['path']);assert p.is_file(),f'Missing restored base file: {p}'
    h=hashlib.sha256() if row.get('packed_at_base') else hashlib.sha1(f'blob {p.stat().st_size}\0'.encode())
    with p.open('rb') as f:
        while b:=f.read(1024*1024):h.update(b)
    assert h.hexdigest()==row.get('sha256',row.get('git_blob')),f'Changed base file: {p}'
parts=json.loads((here/'large-file-parts.json').read_text())
archives=[{'path':'payload.tar.gz','sha256':m['archive_sha256'],'entries':m['entries']},*m.get('supplemental_archives',[])]
all_paths=set();prepared=[]
with tempfile.TemporaryDirectory(prefix='verified-overlay-') as temp:
    for index,record in enumerate(archives):
        item=next(x for x in parts if x['path']==record['path'])
        combined=Path(temp)/f'combined-{index}.gz';payload=Path(temp)/f'payload-{index}.tar.gz'
        with combined.open('wb') as out:
            for name in item['parts']:
                p=(here/name).resolve();assert p.parent==here
                with p.open('rb') as f:shutil.copyfileobj(f,out)
        with gzip.open(combined,'rb') as f,payload.open('wb') as out:shutil.copyfileobj(f,out)
        combined.unlink()
        with payload.open('rb') as f:sha=hashlib.file_digest(f,'sha256').hexdigest()
        assert sha==item['sha256']==record['sha256'],'Archive checksum mismatch'
        expected={x['path']:x for x in record['entries']};seen=set()
        assert len(expected)==len(record['entries']) and not all_paths.intersection(expected)
        with tarfile.open(payload,'r|gz') as archive:
            for member in archive:
                checked_path(member.name)
                assert member.isfile() and member.name in expected and member.name not in seen
                with archive.extractfile(member) as f:assert hashlib.file_digest(f,'sha256').hexdigest()==expected[member.name]['sha256']
                seen.add(member.name)
        assert seen==set(expected),'Incomplete archive'
        all_paths.update(expected);prepared.append(payload)
    for payload in prepared:
        with tarfile.open(payload,'r|gz') as archive:
            for member in archive:
                out=checked_path(member.name);out.parent.mkdir(parents=True,exist_ok=True)
                fd,tmp=tempfile.mkstemp(prefix='.snapshot-',dir=out.parent)
                try:
                    with os.fdopen(fd,'wb') as target,archive.extractfile(member) as f:shutil.copyfileobj(f,target)
                    os.chmod(tmp,member.mode&0o777);os.replace(tmp,out)
                finally:
                    if os.path.exists(tmp):os.unlink(tmp)
print(f'Verified and restored {len(all_paths)} files; read snapshot.json for exclusions and deferred files.')
