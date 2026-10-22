from pathlib import Path
from tempfile import TemporaryDirectory
from datetime import datetime,timezone
from unittest import TestCase,main
from unittest.mock import Mock,patch
import json

import automatic_parallelism as promotion


class AutomaticPromotion(TestCase):
    def setUp(self):
        temp=TemporaryDirectory();self.addCleanup(temp.cleanup)
        self.root=Path(temp.name);self.runtime=self.root/'exhaustive';self.runtime.mkdir()
        proof=self.root/'proof';proof.mkdir();promotion.atomic(proof/'cohort-start-failed-jobs.json',[])
        self.plan={'capacity':6,'current_workers':4,'target_workers':6,'stage_coordinator_pid':12,
            'stage_started_at_utc':datetime.fromtimestamp(1000,timezone.utc).isoformat(),
            'model_migration_proof_directory':str(proof),'explicit_promotion_authorization':{'approved':True},
            'promotion':{'automatic_minute_check':True,'minimum_hours_at_four_workers':2,
                'minimum_successful_jobs':12,'maximum_retry_job_fraction':.31126760563380285,
                'baseline_successful_jobs_per_hour':11.833333333333334,
                'minimum_job_throughput_gain_over_baseline':.1}}
        self.save_plan()
        promotion.atomic(self.runtime/'coordinator-run.json',{'pid':12,'capacity':6,'requested_execution':promotion.EXECUTION})
        promotion.atomic(self.runtime/'worker-limit.json',{'workers':4})
        promotion.atomic(self.runtime/'manual-agent-slots.json',[])
        promotion.atomic(self.runtime/'failed-jobs.json',[])
        self.metrics=[{'coordinator_pid':12,'started_at_unix':1000+i*5,'finished_at_unix':1100+i*5,
            'job':'job-'+str(i),'outcome':'accepted' if i%3 else 'reviewed','attempts':1,
            'kind':'new' if i%3 else 'review','slug':sorted(promotion.MAIN_CODES)[i%5],
            'execution_verified':True,**promotion.EXECUTION} for i in range(36)]
        self.save_metrics()
        self.live=[{'pid':12}];self.workers=[{'ppid':12,'execution':{'verified':True,**promotion.EXECUTION}}]
        self.status={'status':'running','failure':None}
        self.audit=Mock(side_effect=lambda _,rows:{'jobs':len(rows),'source_benefit_impact_reference_checks_passed':True})

    def save_plan(self):promotion.atomic(self.runtime/'parallelism-plan.json',self.plan)
    def save_metrics(self):
        (self.runtime/'job-metrics.jsonl').write_text(''.join(json.dumps(m)+'\n' for m in self.metrics))
    def refresh(self):return self.live,self.workers,True,self.status
    def run_check(self,now=8201):return promotion.promote_if_ready(self.runtime,self.refresh,now,audit=self.audit)

    def test_promotes_hot_without_launching_or_stopping_any_process(self):
        result=self.run_check()
        self.assertEqual(result['decision'],'promoted_to_six')
        self.assertEqual(promotion.read(self.runtime/'worker-limit.json'),{'workers':6})
        self.assertEqual(promotion.read(self.runtime/'parallelism-plan.json')['current_workers'],6)
        self.assertEqual(promotion.read(self.runtime/'promotion-intent.json')['state'],'complete')
        self.assertIsNone(self.run_check())
        self.audit.assert_called_once()

    def test_cannot_promote_just_before_two_hours(self):
        self.assertIn('minimum_observation_window',self.run_check(now=8199)['reasons'])
        self.audit.assert_not_called()
        self.assertEqual(promotion.read(self.runtime/'worker-limit.json'),{'workers':4})

    def test_effective_six_requires_six_native_proofs_and_is_recorded_once(self):
        self.run_check()
        self.workers*=6
        self.workers[-1]['execution']=dict(self.workers[-1]['execution'],verified=False)
        self.assertIsNone(self.run_check())
        self.workers=[{'pid':100+i,'ppid':12,'execution':{'verified':True,'session_id':'session-'+str(i),**promotion.EXECUTION}} for i in range(6)]
        self.assertEqual(self.run_check()['decision'],'six_agents_effectively_verified')
        self.assertEqual(len(promotion.read(self.runtime/'promotion-execution.json')['active_workers']),6)
        self.assertIsNone(self.run_check())

    def test_other_coordinator_and_warmup_results_do_not_pad_the_sample(self):
        for i,m in enumerate(self.metrics):
            if i<12:m['coordinator_pid']=99
            else:m['started_at_unix']=999
        self.save_metrics();self.assertIn('minimum_successful_jobs',self.run_check()['reasons'])
        self.audit.assert_not_called()

    def test_preserves_manual_agent_reservations(self):
        promotion.atomic(self.runtime/'manual-agent-slots.json',['manual-a','manual-b'])
        self.run_check();self.assertEqual(promotion.read(self.runtime/'worker-limit.json'),{'workers':4})
        self.assertEqual(promotion.read(self.runtime/'parallelism-plan.json')['current_workers'],6)

    def test_new_deferred_or_bad_model_keeps_four(self):
        promotion.atomic(self.runtime/'failed-jobs.json',[{'job':'new failure'}])
        self.assertIn('new_deferred_registry_entries',self.run_check()['reasons'])
        promotion.atomic(self.runtime/'failed-jobs.json',[])
        self.workers[0]['execution']['model']='gpt-6.1-sol'
        self.assertIn('active_execution_not_yet_verified',self.run_check()['reasons'])
        self.audit.assert_not_called()

    def test_retry_rate_and_all_five_codes_are_binding(self):
        for m in self.metrics:m['attempts']=2;m['slug']='urbanisme'
        self.save_metrics();reasons=self.run_check()['reasons']
        self.assertIn('retry_fraction',reasons);self.assertIn('five_code_sample',reasons)

    def test_failed_validation_audit_never_changes_worker_limit(self):
        self.audit.side_effect=ValueError('source mismatch')
        result=self.run_check();self.assertIn('validation_audit_failed',result['reasons'])
        self.assertEqual(promotion.read(self.runtime/'worker-limit.json'),{'workers':4})

    def test_partial_telemetry_holds_without_breaking_health_supervision(self):
        with (self.runtime/'job-metrics.jsonl').open('a') as f:f.write('{"partial":')
        self.assertIn('promotion_telemetry_unavailable',self.run_check()['reasons'])
        self.audit.assert_not_called()

    def test_disabling_automatic_mode_during_audit_is_respected(self):
        def disable(*_):
            self.plan['promotion']['automatic_minute_check']=False;self.save_plan()
            return {'jobs':36,'source_benefit_impact_reference_checks_passed':True}
        self.audit.side_effect=disable
        self.assertIn('plan_changed_during_check',self.run_check()['reasons'])
        self.assertEqual(promotion.read(self.runtime/'worker-limit.json'),{'workers':4})

    def test_failed_limit_write_reconciles_from_durable_intent(self):
        real=promotion.atomic
        def fail_limit(path,value):
            if path.name=='worker-limit.json':raise OSError('simulated write failure')
            return real(path,value)
        with patch.object(promotion,'atomic',side_effect=fail_limit),self.assertRaises(OSError):self.run_check()
        self.assertEqual(promotion.read(self.runtime/'promotion-intent.json')['state'],'prepared')
        self.assertEqual(promotion.read(self.runtime/'worker-limit.json'),{'workers':4})
        self.assertEqual(self.run_check()['decision'],'promoted_to_six')
        self.assertEqual(promotion.read(self.runtime/'worker-limit.json'),{'workers':6})
        self.assertEqual(promotion.read(self.runtime/'promotion-intent.json')['state'],'complete')


if __name__=='__main__':main()
