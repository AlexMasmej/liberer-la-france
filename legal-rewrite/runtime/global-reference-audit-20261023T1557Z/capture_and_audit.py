from pathlib import Path
import json,shutil,datetime,sys
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[1]
sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT))
import global_reference_audit as audit
pre=json.loads((OUT/'preflight.json').read_text())
wal=ROOT/'corpus.sqlite-wal'
walbytes=wal.stat().st_size if wal.exists() else 0
required=pre['required_free_bytes']+max(0,walbytes-pre['wal_observed_bytes'])+max(0,(ROOT/'corpus.sqlite').stat().st_size-pre['new_live_database_bytes'])
free=shutil.disk_usage(ROOT).free
check={'at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'free_bytes':free,'required_free_bytes':required,'wal_exists':wal.exists(),'wal_bytes':walbytes,'capture_permitted':free>=required}
(OUT/'immediate-storage-preflight.json').write_text(json.dumps(check,indent=2)+'\n')
assert check['capture_permitted'],check
print(json.dumps({'stage':'preflight_admitted','free_gib':free/2**30,'required_gib':required/2**30}),flush=True)
audit.main(['--db',str(ROOT/'corpus.sqlite'),'--output',str(OUT),'--as-of','2026-10-18'])
