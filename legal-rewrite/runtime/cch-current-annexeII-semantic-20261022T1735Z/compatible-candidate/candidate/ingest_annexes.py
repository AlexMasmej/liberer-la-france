"""Import the four separately distributed CGI annexes from cached official files.

bsdtar filters archive entries into a temporary tar stream, without extracting
paths to disk. Original source archives remain available and checksummed in
the primary database. The filtered subset is parsed by the same lossless XML
importer. No network calls or model-generated source material are involved.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess,json,time,sqlite3
import ingest

HERE=ingest.HERE
config=ingest.CONFIG
ingest.TARGETS={r['id']:r for r in config['annexes']}
manifest=json.loads((HERE/'archive-manifest.json').read_text())
cache=Path('/private/tmp/legi-annex-filtered');cache.mkdir(exist_ok=True)
db=ingest.open_db(HERE/'annexes.sqlite')
already_imported={row[0] for row in db.execute('SELECT name FROM archives WHERE complete=1')}
pending=[row for row in manifest if row['name'] not in already_imported]

def filter_one(row):
    source=Path('/private/tmp/legi-global-20250713.tar.gz') if row['name'].startswith('Freemium') else Path('/private/tmp/legi-updates')/row['name']
    while not source.exists():time.sleep(1)
    target=cache/row['name']
    if not target.exists():
        temp=Path(str(target)+'.filtering')
        cmd=['tar','-czf',str(temp)]
        for identifier in ingest.TARGETS:cmd.extend(['--include','*/'+identifier+'/*'])
        cmd.append('@'+str(source));subprocess.run(cmd,check=True)
        temp.rename(target)
    return row,target

with ThreadPoolExecutor(max_workers=4) as pool:
    for n,(row,path) in enumerate(pool.map(filter_one,pending),1):
        count=ingest.import_archive(db,path,row['url'])
        if n==1 or n%50==0:print('Annex sources',n,'/',len(manifest),count,'documents in this batch',flush=True)
db.close()

main=ingest.open_db(HERE/'corpus.sqlite')
main.execute('ATTACH DATABASE ? AS annex',(str(HERE/'annexes.sqlite'),))
main.execute('INSERT OR REPLACE INTO documents SELECT * FROM annex.documents')
main.execute('INSERT OR REPLACE INTO articles SELECT * FROM annex.articles')
main.execute('INSERT OR REPLACE INTO scope_completion VALUES(?,?)',('cgi-annexes',len(manifest)))
main.commit()
print('All four CGI annexes merged from',len(manifest),'dated official archives.',flush=True)
