"""Restore the completed second pass over its documented prior snapshot."""
from pathlib import Path
import argparse,gzip,hashlib,io,json,os,shutil,sqlite3,subprocess,sys,tarfile,tempfile
def require(ok,why):
    if not ok:raise ValueError(why)
def digest(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def checked_destination(dest,name):
    p=Path(name);require(not p.is_absolute() and '..' not in p.parts and p.parts and p.parts[0] in ['sites','legal-rewrite'],'Unsafe archive path')
    out=dest/p;require(not any(x.is_symlink() for x in [out,*out.parents]),'Symlink in destination');return out
class Joined(io.RawIOBase):
    def __init__(self,paths):self.paths=iter(paths);self.f=None
    def readable(self):return True
    def readinto(self,b):
        while True:
            if self.f is None:
                try:self.f=next(self.paths).open('rb')
                except StopIteration:return 0
            n=self.f.readinto(b)
            if n:return n
            self.f.close();self.f=None
    def close(self):
        if self.f:self.f.close()
        super().close()
def stream(here,m):
    return io.BufferedReader(Joined([here/x['path'] for x in m['parts']]))
def verify_payload(here,m,dest):
    total=hashlib.sha256()
    for part in m['parts']:
        require(Path(part['path']).name==part['path'],'Part escapes snapshot folder');p=here/part['path']
        require(p.is_file() and not p.is_symlink() and p.stat().st_size==part['size'] and digest(p)==part['sha256'],'Part integrity failure')
        with p.open('rb') as f:
            while b:=f.read(1024*1024):total.update(b)
    require(total.hexdigest()==m['archive_sha256'],'Compressed archive integrity failure')
    expected={x['path']:x for x in m['entries']};require(len(expected)==len(m['entries']),'Duplicate manifest identity');seen=set()
    with stream(here,m) as raw,gzip.GzipFile(fileobj=raw) as gz,tarfile.open(fileobj=gz,mode='r|') as archive:
        for member in archive:
            checked_destination(dest,member.name);require(member.isfile() and member.name in expected and member.name not in seen,'Unexpected or duplicate member')
            require(member.size==expected[member.name]['size'],'Member length differs')
            with archive.extractfile(member) as f:require(hashlib.file_digest(f,'sha256').hexdigest()==expected[member.name]['sha256'],'Member integrity failure')
            seen.add(member.name)
    require(seen==set(expected),'Incomplete archive');return len(seen)
def apply_payload(here,m,dest):
    with stream(here,m) as raw,gzip.GzipFile(fileobj=raw) as gz,tarfile.open(fileobj=gz,mode='r|') as archive:
        for member in archive:
            out=checked_destination(dest,member.name);out.parent.mkdir(parents=True,exist_ok=True)
            fd,name=tempfile.mkstemp(prefix='.second-pass-',dir=out.parent)
            try:
                with os.fdopen(fd,'wb') as f,archive.extractfile(member) as source:shutil.copyfileobj(source,f)
                os.chmod(name,member.mode&0o777);os.replace(name,out)
            finally:
                if os.path.exists(name):os.unlink(name)
def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--destination',required=True);parser.add_argument('--base-already-restored',action='store_true');args=parser.parse_args()
    here=Path(__file__).resolve().parent;dest=Path(args.destination).resolve();m=json.loads((here/'snapshot.json').read_bytes())
    original=Path('/Users/alexandremasmejean/.codex/.chatgpt-projects/g-p-6ad59c015c308191aa21cba63c71a6dc')
    require(dest!=original and original not in dest.parents,'Never restore over drafting originals')
    require(dest.is_dir(),'Create a separate base checkout first')
    head=subprocess.check_output(['git','-C',str(dest),'rev-parse','HEAD'],text=True).strip();require(head==m['initial_restore_base_commit'],'Destination is not the documented initial base commit')
    if not args.base_already_restored:
        repo=here.parent.parent;prior=repo/m['base_snapshot']/'restore-overlay.py';require(prior.is_file(),'Prior snapshot restoration tool missing')
        subprocess.run([sys.executable,str(prior),'--destination',str(dest)],check=True)
    for row in m['unchanged_at_previous_snapshot']:
        p=checked_destination(dest,row['path']);require(p.is_file() and digest(p)==row['sha256'],'Restored prior snapshot differs: '+row['path'])
    count=verify_payload(here,m,dest);apply_payload(here,m,dest)
    with sqlite3.connect((dest/'legal-rewrite/corpus.sqlite').as_uri()+'?mode=ro',uri=True) as db:
        db.execute('PRAGMA query_only=ON');require(db.execute('PRAGMA quick_check').fetchone()==('ok',),'Restored database failed quick_check')
    print(f'Restored {count} changed files. Second pass complete; documentary and legal reserves remain open. No source original or GitHub issue was modified.')
if __name__=='__main__':main()
