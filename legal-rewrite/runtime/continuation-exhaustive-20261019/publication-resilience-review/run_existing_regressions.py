from pathlib import Path
from contextlib import redirect_stdout
import json,sys,types,unittest

P=Path(__file__).resolve().parent;LEGAL=P.parents[2]
sys.path.insert(0,str(LEGAL))
for name in ['publish_snapshot','run_exhaustive']:
    m=types.ModuleType(name);m.__file__=str(LEGAL/(name+'.py'));sys.modules[name]=m
    exec(compile((P/(name+'.py.proposed.txt')).read_text(),m.__file__,'exec'),m.__dict__)
suite=unittest.defaultTestLoader.discover(str(LEGAL),pattern='test_*.py')
with (P/'existing-regressions.log').open('w') as output,redirect_stdout(output):
    result=unittest.TextTestRunner(stream=output,verbosity=1).run(suite)
summary={'tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'successful':result.wasSuccessful(),'network_calls':'All model and publication subprocesses remain mocked in the existing suites.'}
(P/'existing-regressions.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
raise SystemExit(0 if result.wasSuccessful() else 1)
