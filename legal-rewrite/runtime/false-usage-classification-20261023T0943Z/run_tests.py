"""Run the staged runner with isolated fixtures and forbid the production DB."""
from pathlib import Path
import hashlib
import io
import json
import sqlite3
import sys
import unittest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))
real_connect = sqlite3.connect


def fixture_connect(database, *args, **kwargs):
    value = str(database)
    if str(ROOT/'corpus.sqlite') in value:
        raise AssertionError('Production database access forbidden in tests')
    return real_connect(database, *args, **kwargs)


sqlite3.connect = fixture_connect
import run_exhaustive
assert Path(run_exhaustive.__file__).resolve() == HERE/'run_exhaustive.py'
suite = unittest.TestSuite()
loader = unittest.defaultTestLoader
suite.addTests(loader.discover(str(HERE), pattern='test_access*.py'))
for name in ['test_drafting_queue', 'test_worker_execution',
             'test_exhaustive_supervision', 'test_parallelism',
             'test_worker_capacity_roles', 'test_atomic_status',
             'test_publication_resilience', 'test_reference_driver']:
    suite.addTests(loader.loadTestsFromName(name))
with (HERE/'tests.log').open('w', buffering=1) as stream:
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
report = dict(tests_run=result.testsRun, failures=len(result.failures),
              errors=len(result.errors), success=result.wasSuccessful(),
              production_db_forbidden=True, model_invocations=0,
              tested_runner_sha256=hashlib.sha256(
                  (HERE/'run_exhaustive.py').read_bytes()).hexdigest())
(HERE/'tests.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report))
if not result.wasSuccessful():
    print((HERE/'tests.log').read_text()[-15000:])
    sys.exit(1)
