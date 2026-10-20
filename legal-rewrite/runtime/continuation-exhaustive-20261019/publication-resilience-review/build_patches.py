from pathlib import Path
import difflib,hashlib,json

P=Path(__file__).resolve().parent
publish=(P/'publish_snapshot.py.baseline.txt').read_text()
header=publish[:publish.index('\ndef publish(')]
header=header.replace('import argparse,fcntl,json,subprocess,sys,time','import argparse,errno,fcntl,json,re,subprocess,sys,time')
publish=header+'\n'+(P/'publish_body.proposed.py.txt').read_text()
driver=(P/'run_exhaustive.py.baseline.txt').read_text()
anchor='def policy_is_current(folder):'
assert driver.count(anchor)==1
driver=driver.replace(anchor,(P/'coordinator_helper.proposed.py.txt').read_text()+'\n'+anchor)
anchor="    atomic(RUNTIME/'status.json',result)"
assert driver.count(anchor)==1
driver=driver.replace(anchor,"    publication_state=RUNTIME/'publication-state.json'\n    result['publication_pending']=bool(json.loads(publication_state.read_text()).get('publication_pending')) if publication_state.exists() else False\n"+anchor)
anchor="subprocess.run([sys.executable,str(HERE/'publish_snapshot.py')]+(['--deploy'] if args.deploy_on_export else []),cwd=ROOT,check=True)"
assert driver.count(anchor)==1
driver=driver.replace(anchor,'publish_checkpoint(args.deploy_on_export)')
anchor="subprocess.run([sys.executable,str(HERE/'publish_snapshot.py')]+(['--deploy'] if args.publish_at_end else []),cwd=ROOT,check=True)"
assert driver.count(anchor)==1
driver=driver.replace(anchor,'publish_checkpoint(args.publish_at_end)')
report={}
for name,updated in [('publish_snapshot.py',publish),('run_exhaustive.py',driver)]:
    original=(P/(name+'.baseline.txt')).read_text();compile(updated,name,'exec')
    (P/(name+'.proposed.txt')).write_text(updated)
    (P/(name+'.patch')).write_text(''.join(difflib.unified_diff(original.splitlines(True),updated.splitlines(True),fromfile='a/legal-rewrite/'+name,tofile='b/legal-rewrite/'+name)))
    report[name]={'baseline_sha256':hashlib.sha256(original.encode()).hexdigest(),'proposed_sha256':hashlib.sha256(updated.encode()).hexdigest()}
(P/'proposed-file-hashes.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
