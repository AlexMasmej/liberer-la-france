from pathlib import Path
from tempfile import TemporaryDirectory
import json
import unittest

from review_lane_observation import observe


class Observation(unittest.TestCase):
    def setUp(self):
        self.temp=TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.runtime=Path(self.temp.name)
        (self.runtime/'coordinator-run.json').write_text(json.dumps({'pid':12,'capacity':8,'role_limits':{'new':6,'review':2},'started_at_unix':100}))
        (self.runtime/'parallelism-plan.json').write_text(json.dumps({'capacity':8,'current_workers':8,'role_limits':{'new':6,'review':2}}))
        self.workers=[{'pid':200+i,'ppid':12,'kind':'new' if i<6 else 'review',
                       'execution':{'verified':True,'model':'gpt-6-astra','reasoning_effort':'medium','session_id':'session-'+str(i)}} for i in range(8)]

    def check(self,workers=None,coordinators=None):
        return observe(self.runtime,[{'pid':12}] if coordinators is None else coordinators,
                       self.workers if workers is None else workers,1000)

    def test_only_distinct_native_responses_prove_the_eight_workers(self):
        for key,value in [('verified',False),('model','other'),('reasoning_effort','ultra'),('session_id','session-0')]:
            workers=json.loads(json.dumps(self.workers));workers[-1]['execution'][key]=value
            with self.subTest(key=key):
                self.assertFalse(self.check(workers)['simultaneous_six_new_plus_two_review_verified'])
                self.assertFalse((self.runtime/'review-lanes-execution.json').exists())
        self.assertTrue(self.check()['simultaneous_six_new_plus_two_review_verified'])
        proof=json.loads((self.runtime/'review-lanes-execution.json').read_text())
        self.assertEqual(len(proof['active_agents']),8)

    def test_configuration_or_old_pid_never_counts_as_execution(self):
        self.assertFalse(self.check([])['simultaneous_six_new_plus_two_review_verified'])
        self.assertFalse(self.check(coordinators=[{'pid':11}])['simultaneous_six_new_plus_two_review_verified'])
        self.assertFalse(self.check(coordinators=[{'pid':12},{'pid':13}])['simultaneous_six_new_plus_two_review_verified'])

    def test_metrics_do_not_mix_previous_pid_or_incomplete_append(self):
        metrics=[{'coordinator_pid':11,'kind':'new','outcome':'accepted','articles':999,'started_at_unix':110,'finished_at_unix':120},
                 {'coordinator_pid':12,'kind':'new','outcome':'accepted','articles':24,'started_at_unix':110,'finished_at_unix':130},
                 {'coordinator_pid':12,'kind':'review','outcome':'reviewed','articles':12,'started_at_unix':150,'finished_at_unix':250}]
        (self.runtime/'job-metrics.jsonl').write_text('\n'.join(map(json.dumps,metrics))+'\n{"partial":')
        report=self.check()
        self.assertEqual(report['cohort_articles'],{'new':24,'review':12})
        self.assertEqual(report['measured_successful_by_kind'],{'new':0,'review':1})
        self.assertFalse(report['measurement_complete'])


if __name__=='__main__':unittest.main()
