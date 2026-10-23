"""Offline rebase tests: production SQLite and model processes forbidden."""
from pathlib import Path
import json
import sqlite3
import sys
import unittest
from unittest.mock import patch

STAGE=Path(__file__).resolve().parent
ROOT=STAGE.parents[1]
sys.path.insert(0,str(ROOT));sys.path.insert(0,str(STAGE/'candidate'));sys.path.insert(0,str(STAGE))
real_connect=sqlite3.connect
def safe_connect(path,*args,**kwargs):
    if str(ROOT/'corpus.sqlite') in str(path):raise AssertionError('Production DB forbidden')
    return real_connect(path,*args,**kwargs)

with patch.object(sqlite3,'connect',side_effect=safe_connect):
    suite=unittest.defaultTestLoader.loadTestsFromNames(
        ['test_preflight','test_access_failure','test_access_integration'])
    with (STAGE/'targeted-tests.log').open('w',buffering=1) as output:
        result=unittest.TextTestRunner(stream=output,verbosity=2).run(suite)
summary=dict(tests_run=result.testsRun,failures=len(result.failures),errors=len(result.errors),
             success=result.wasSuccessful(),production_db_forbidden=True,model_invocations=0)
(STAGE/'targeted-tests.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary))
if not result.wasSuccessful():print((STAGE/'targeted-tests.log').read_text()[-7000:])
raise SystemExit(not result.wasSuccessful())
