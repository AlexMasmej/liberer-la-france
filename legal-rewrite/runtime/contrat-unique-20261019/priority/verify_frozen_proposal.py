"""Fail-closed read-only check immediately before an explicit manifest takeover."""
from pathlib import Path
import hashlib, json, sqlite3, types

FOLDER=Path(__file__).resolve().parent
LEGAL=FOLDER.parents[2]
read=lambda name:json.loads((FOLDER/name).read_text())
sha=lambda value:hashlib.sha256(value if isinstance(value,bytes) else value.encode()).hexdigest()
guards=read('guard-report.json')
helper=types.ModuleType('cu_verify')
helper.__file__=str(LEGAL/'contrat_unique_priority.py')
exec(compile((FOLDER/'contrat_unique_priority.proposed.py.txt').read_text(),helper.__file__,'exec'),helper.__dict__)
manifest_bytes=(LEGAL/'runtime/radical-review-20261019.json').read_bytes()
if sha(manifest_bytes)!=guards['manifest_file_sha256']:
    raise ValueError('Active review manifest bytes changed; regenerate proposal')
if sha((LEGAL/'policy-coordinations.json').read_bytes())!=guards['policy_sha256']:
    raise ValueError('Author policy changed; reassess proposal')
for pack in guards['pack_guards']:
    if sha((LEGAL/pack['source_path']).read_bytes())!=pack['source_file_sha256']:
        raise ValueError('Reserved source pack changed: '+pack['pack'])
db=sqlite3.connect('file:'+str(LEGAL/'corpus.sqlite')+'?mode=ro',uri=True)
db.execute('BEGIN')
try:
    sources={(c,i):s for c,i,s in db.execute('SELECT code_id,id,source_sha256 FROM articles')}
    drafts={(c,i):sha(b or '') for c,i,b in db.execute('SELECT code_id,source_id,proposed_xml FROM drafts')}
    manifest=json.loads(manifest_bytes)
    proposal=helper.propose_review_manifest(manifest,read('reopen-operations.proposed.json'),sources,drafts,
        guards['manifest_canonical_sha256'])
    if proposal!=read('review-manifest.proposed.json'):
        raise ValueError('Frozen proposal differs from guarded reconstruction')
    for row in read('priority-targets.proposed.json')['targets']:
        key=row['code_id'],row['source_id']
        if sources.get(key)!=row['source_sha256']:
            raise ValueError('Priority source changed: '+str(key))
finally:
    db.close()
print('Verified: unchanged manifest and policy, current canonical source/draft guards, exact frozen proposal. No mutation performed.')
