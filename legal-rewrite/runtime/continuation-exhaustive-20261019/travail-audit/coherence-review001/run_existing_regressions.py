"""Existing offline checks against proposed isolated modules, no activation."""
from pathlib import Path
import sys,types,unittest

P=Path(__file__).resolve().parent
LEGAL=P.parents[3]
sys.path.insert(0,str(LEGAL))
for name,filename in [('reference_coherence','reference_coherence.py.proposed.txt'),
                      ('review_prior','review_prior.py.proposed.txt'),
                      ('run_exhaustive','run_exhaustive.py.baseline.txt')]:
    module=types.ModuleType(name);module.__file__=str(LEGAL/(name+'.py'));sys.modules[name]=module
    exec(compile((P/filename).read_text(),module.__file__,'exec'),module.__dict__)
suite=unittest.defaultTestLoader.loadTestsFromNames([
    'test_reference_coherence','test_review_prior','test_drafting_queue',
    'test_pipeline_memory','test_register_batches'])
result=unittest.TextTestRunner(verbosity=1).run(suite)
raise SystemExit(0 if result.wasSuccessful() else 1)
