"""Fetch dated official update archives, then import strictly in date order."""
from pathlib import Path
import json,subprocess
from concurrent.futures import ThreadPoolExecutor
from ingest import open_db,import_archive,HERE

cache=Path('/private/tmp/legi-updates');cache.mkdir(exist_ok=True)
manifest=json.loads((HERE/'archive-manifest.json').read_text())
db=open_db(HERE/'corpus.sqlite')
done={r[0] for r in db.execute('SELECT name FROM archives WHERE complete=1')}
pending=[r for r in manifest if r['name'].startswith('LEGI_') and r['name'] not in done]

def fetch(row):
    target=cache/row['name'];temp=target.with_suffix(target.suffix+'.download')
    if not target.exists():
        subprocess.run(['curl','-fsSL','--retry','2','--connect-timeout','20','--max-time','120',row['url'],'-o',str(temp)],check=True)
        temp.rename(target)
    return row,target

# map yields in manifest order even though requests run concurrently.
with ThreadPoolExecutor(max_workers=4) as pool:
    for index,(row,path) in enumerate(pool.map(fetch,pending),1):
        count=import_archive(db,path,row['url'])
        if index==1 or index%20==0:print(index,'/',len(pending),row['name'],count,'selected documents',flush=True)
print('All official daily updates imported.',flush=True)
