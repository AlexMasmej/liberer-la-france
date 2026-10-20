from pathlib import Path
import difflib, hashlib, json

HERE=Path(__file__).resolve().parent
base=(HERE/'run_exhaustive.base.py.txt').read_text()
hook='''def past_job_enabled():
    """An absent, invalid or non-opt-in integration never activates memory."""
    try:
        settings=json.loads((HERE/'past-setup/integration.json').read_text())
    except (OSError,ValueError):
        return False
    return (isinstance(settings,dict) and settings.get('enabled') is True
            and settings.get('recall_mode')=='only_when_useful')


def past_before_job():
    """Changed-body updates only; bounded failure never aborts legal drafting."""
    enabled=past_job_enabled()
    # Always suppress the account-level server in this worker, even on opt-out.
    options=['-c','mcp_servers.past.enabled=false',
             '-c','mcp_servers.legal_rewrite_memory.enabled=false']
    if not enabled:
        return options
    try:
        # The subprocess bounds network latency and suppresses response/secret
        # logging. Synchronizer itself skips credentials/network if unchanged.
        # Its durable pending intent and idempotency key survive a timeout.
        subprocess.run([sys.executable,'-c',
                        'from past_sync import Synchronizer as SyncEngine; '
                        'SyncEngine().run("updates")'],
                       cwd=HERE,stdin=subprocess.DEVNULL,stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL,timeout=30,check=True)
    except Exception:
        print('MEMORY updates unavailable; continuing with local sources',flush=True)
    server=HERE/'past_memory_mcp.py'
    if not server.is_file():
        print('MEMORY local recall unavailable; continuing with local sources',flush=True)
        return options
    # Only the fixed read-only tool is exposed. Initialization lists the tool
    # without reading credentials or performing a recall. No prompt hook.
    readonly='{'+','.join([
        'command='+json.dumps(sys.executable,ensure_ascii=False),
        'args='+json.dumps([str(server)],ensure_ascii=False),
        'cwd='+json.dumps(str(HERE),ensure_ascii=False),
        'enabled=true','required=false','enabled_tools=["past_recall"]',
        'startup_timeout_sec=10','tool_timeout_sec=120'])+'}'
    return options+['-c','mcp_servers.legal_rewrite_memory='+readonly]


'''
anchor='def run_job(job,codex,sources,review=False):\n'
assert base.count(anchor)==1
proposed=base.replace(anchor,hook+anchor)
before="    name=(f\"review-{slug}-{expected[0]['source_id']}-{index:05d}\" if review else f'{slug}-{index:05d}')"
assert proposed.count(before)==1
proposed=proposed.replace(before,"    memory_options=past_before_job()\n"+before)
before="            cmd=[codex,'exec','--ephemeral'"
assert proposed.count(before)==1
proposed=proposed.replace(before,"            cmd=[codex,'exec',*memory_options,'--ephemeral'")
compile(proposed,str(HERE/'run_exhaustive.proposed.py.txt'),'exec')
(HERE/'run_exhaustive.proposed.py.txt').write_text(proposed)
patch=''.join(difflib.unified_diff(base.splitlines(True),proposed.splitlines(True),fromfile='a/legal-rewrite/run_exhaustive.py',tofile='b/legal-rewrite/run_exhaustive.py'))
(HERE/'run_exhaustive.past-hook.proposed.patch').write_text(patch)
(HERE/'patch-manifest.json').write_text(json.dumps({'base_sha256':hashlib.sha256(base.encode()).hexdigest(),'proposed_sha256':hashlib.sha256(proposed.encode()).hexdigest(),'patch_sha256':hashlib.sha256(patch.encode()).hexdigest(),'changes_only':'legal-rewrite/run_exhaustive.py','canonical_modified':False,'instructions_modified':False,'paid_or_network_test_calls':0},indent=2)+'\n')
print('Prepared isolated pipeline patch; canonical source unchanged')
