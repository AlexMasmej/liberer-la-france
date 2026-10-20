"""Drain the sample, preserve its work, then resume with clarified instructions."""
from pathlib import Path
import fcntl, hashlib, json, os, sqlite3, subprocess, sys, time

FOLDER=Path(__file__).resolve().parent
LEGAL=FOLDER.parents[1]
sys.path.insert(0,str(LEGAL))
from register_batches import writer_lock

activation=json.loads((FOLDER/'policy-bound-activation.json').read_text())
assert {a['target'] for a in activation['files']}=={'reference_coherence.py','test_reference_policy.py'}
plan=json.loads((FOLDER/'policy-clarification-plan.json').read_text())
planned=(FOLDER/'policy-clarification.proposed.json').read_bytes()
sha=lambda data:hashlib.sha256(data).hexdigest()
assert sha(planned)==plan['after_sha256']
print('Waiting for the three in-flight review jobs; their policy is preserved.',flush=True)
with (LEGAL/'runtime/exhaustive/coordinator.lock').open('a') as lock:
    fcntl.flock(lock,fcntl.LOCK_EX)
    with writer_lock():
        for item in activation['files']:
            target=LEGAL/item['target'];candidate=FOLDER/item['candidate']
            current=sha(target.read_bytes()) if target.exists() else None
            assert current in {item['before_sha256'],item['after_sha256']}, 'Reviewed module changed independently'
            content=candidate.read_bytes();assert sha(content)==item['after_sha256']
            temporary=target.with_suffix('.py.tmp');temporary.write_bytes(content);temporary.replace(target)
    with (FOLDER/'coherence-engine/activated-v3-tests.log').open('w') as output:
        subprocess.run([sys.executable,'-m','unittest','discover','-s',str(LEGAL),'-p','test_*.py'],cwd=LEGAL.parent,stdout=output,stderr=subprocess.STDOUT,check=True,timeout=120)
    with writer_lock():
        policy=LEGAL/'policy-coordinations.json'
        assert sha(policy.read_bytes()) in {plan['before_sha256'],plan['after_sha256']}, 'Instructions changed independently'
        if sha(policy.read_bytes())==plan['before_sha256']:
            before=FOLDER/'policy-coordinations.before-clarification.json'
            if before.exists():assert sha(before.read_bytes())==plan['before_sha256']
            else:before.write_bytes(policy.read_bytes())
        db=sqlite3.connect('file:'+str(LEGAL/'corpus.sqlite')+'?mode=ro',uri=True)
        try:
            for item in plan['operative_article_guards']:
                row=db.execute('SELECT proposed_xml FROM drafts WHERE code_id=? AND source_id=?',(item['code_id'],item['source_id'])).fetchone()
                assert row and sha(row[0].encode())==item['proposed_sha256'], item['number']+' changed independently'
        finally:db.close()
        temporary=policy.with_suffix('.json.tmp')
        temporary.write_bytes(planned);temporary.replace(policy)
        (FOLDER/'policy-clarification-applied.json').write_text(json.dumps({'updated_at_unix':int(time.time()),'policy_sha256':plan['after_sha256'],'operative_articles_unchanged':True,'reference_certificate_version':3},indent=2)+'\n')
print('Complete-month prorata and next-day notice clarified; resuming the entire queue.',flush=True)
os.chdir(LEGAL.parent)
os.execv(sys.executable,[sys.executable,str(LEGAL/'run_exhaustive.py'),'--workers','3','--interleave-review','--wait-for-coordinator','--export-every','200','--deploy-on-export','--publish-at-end'])
