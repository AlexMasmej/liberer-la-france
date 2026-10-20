"""Return a reserved drafting slot after a manual agent has finished."""
from pathlib import Path
import fcntl,json,sys
folder=Path(__file__).resolve().parent/'runtime/exhaustive'
with (folder/'manual-agent-slots.lock').open('a') as lock:
    fcntl.flock(lock,fcntl.LOCK_EX)
    p=folder/'manual-agent-slots.json';agents=json.loads(p.read_text())
    agents=[a for a in agents if a!=sys.argv[1]]
    for p,value in [(p,agents),(folder/'worker-limit.json',{'workers':max(1,3-len(agents))})]:
        temporary=p.with_suffix('.tmp');temporary.write_text(json.dumps(value)+'\n');temporary.replace(p)
    print('Drafting slots available:',max(1,3-len(agents)))
