"""Run existing offline regression cases against isolated proposed modules."""
from pathlib import Path
import sys, types, unittest

FOLDER=Path(__file__).resolve().parent
LEGAL=FOLDER.parents[2]
sys.path.insert(0,str(LEGAL))
for name, filename in [('contrat_unique_priority','contrat_unique_priority.proposed.py.txt'),
                       ('review_prior','review_prior.py.proposed.txt'),
                       ('run_exhaustive','run_exhaustive.py.proposed.txt')]:
    module=types.ModuleType(name)
    module.__file__=str(LEGAL/(name+'.py'))
    sys.modules[name]=module
    exec(compile((FOLDER/filename).read_text(),module.__file__,'exec'),module.__dict__)
suite=unittest.defaultTestLoader.loadTestsFromNames([
    'test_drafting_queue','test_review_prior','test_sru_context','test_pipeline_memory'])
result=unittest.TextTestRunner(verbosity=1).run(suite)
raise SystemExit(0 if result.wasSuccessful() else 1)
