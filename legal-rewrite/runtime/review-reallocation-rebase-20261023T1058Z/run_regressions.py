"""Reproduce the bounded regression run with production DB/lock guards."""
from pathlib import Path
from contextlib import contextmanager
import json,sqlite3,sys,unittest
from unittest.mock import patch

STAGE=Path(__file__).resolve().parent
PROJECT=STAGE.parents[1]
sys.path.insert(0,str(PROJECT));sys.path.insert(0,str(STAGE/'candidate'))
import run_exhaustive as coordinator
import register_batches

real_lock=register_batches.writer_lock
@contextmanager
def fixture_lock():
    if coordinator.HERE==PROJECT:raise AssertionError('Fixture did not select a temporary root')
    with real_lock(coordinator.HERE):yield

real_connect=sqlite3.connect
def safe_connect(path,*args,**kwargs):
    if str(PROJECT/'corpus.sqlite') in str(path):raise AssertionError('Production corpus forbidden in regression tests')
    return real_connect(path,*args,**kwargs)

names=['test_worker_capacity_roles','test_parallelism','test_drafting_queue',
       'test_review_prior','test_reference_queue','test_review_lane_observation',
       'test_exhaustive_supervision.Decisions',
       'test_exhaustive_supervision.FilesAndProcesses.test_restart_preserves_metadata_and_does_not_touch_job_answers',
       'test_exhaustive_supervision.FilesAndProcesses.test_launch_failure_persists_backoff_and_counts_failed_attempt']
if __name__=='__main__':
    with patch.object(coordinator,'writer_lock',fixture_lock),patch.object(coordinator,'past_before_job',return_value=[]),patch.object(sqlite3,'connect',side_effect=safe_connect):
        with (STAGE/'regression-tests.log').open('w') as stream:
            result=unittest.TextTestRunner(stream=stream,verbosity=2).run(unittest.defaultTestLoader.loadTestsFromNames(names))
    summary={'regression_tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
             'successful':result.wasSuccessful(),'real_models_invoked':False,'production_database_open_forbidden':True,
             'writer_lock':'temporary fixture roots only'}
    (STAGE/'regression-tests.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(summary)
    raise SystemExit(not result.wasSuccessful())
