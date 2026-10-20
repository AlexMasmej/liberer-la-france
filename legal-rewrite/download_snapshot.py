"""Download the official LEGI snapshot with four bounded HTTP range requests.

Preserves an existing prefix. Never uses credentials or extracts archive paths.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess, math, json, os

URL='https://echanges.dila.gouv.fr/OPENDATA/LEGI/Freemium_legi_global_20250713-140000.tar.gz'
SIZE=1171027316
DEST=Path('/private/tmp/legi-global-20250713.tar.gz')
STATE=Path('/private/tmp/legi-range-state.json')
if STATE.exists():
    spec=json.loads(STATE.read_text())
else:
    offset=DEST.stat().st_size if DEST.exists() else 0
    step=math.ceil((SIZE-offset)/4)
    spec=[(offset+i*step,min(SIZE-1,offset+(i+1)*step-1),str(DEST)+f'.part{i}') for i in range(4) if offset+i*step<SIZE]
    STATE.write_text(json.dumps(spec))

def fetch(row):
    start,end,path=row;p=Path(path);expected=end-start+1
    if p.exists() and p.stat().st_size==expected:return path
    if p.exists():p.unlink()
    headers=Path(path+'.headers')
    subprocess.run(['curl','-fsSL','--retry','2','--connect-timeout','20','--max-time','1200','--range',f'{start}-{end}','-D',str(headers),URL,'-o',path],check=True)
    if p.stat().st_size!=expected or '206 Partial Content' not in headers.read_text():
        raise RuntimeError('Server did not honour the bounded range request')
    print('Completed range',start,end,flush=True)
    return path

with ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(fetch,spec))
offset=spec[0][0] if spec else SIZE
if DEST.exists() and DEST.stat().st_size!=offset:
    if DEST.stat().st_size==SIZE:print('Already assembled');raise SystemExit(0)
    raise RuntimeError('Snapshot prefix changed')
with DEST.open('ab') as target:
    for start,end,path in spec:
        with Path(path).open('rb') as source:
            while chunk:=source.read(1024*1024):target.write(chunk)
assert DEST.stat().st_size==SIZE
print('Complete official archive:',DEST,flush=True)
