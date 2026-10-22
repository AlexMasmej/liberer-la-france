"""Read-only performance observation; execution proof requires native responses."""
import json
import tempfile
from pathlib import Path


def atomic(path,value):
    with tempfile.NamedTemporaryFile(mode='w',encoding='utf-8',dir=path.parent,
                                     prefix='.'+path.name,delete=False) as stream:
        temporary=Path(stream.name)
        json.dump(value,stream,ensure_ascii=False,indent=2)
    try:temporary.replace(path)
    finally:temporary.unlink(missing_ok=True)


def observe(runtime,coordinators,workers,now):
    run_path=runtime/'coordinator-run.json'
    run=json.loads(run_path.read_text()) if run_path.exists() else {}
    pid=run.get('pid')
    expected={'model':'gpt-6-astra','reasoning_effort':'medium'}
    matched=len(coordinators)==1 and coordinators[0]['pid']==pid
    plan_path=runtime/'parallelism-plan.json'
    plan=json.loads(plan_path.read_text()) if plan_path.exists() else {}
    configured=(run.get('capacity')==8 and run.get('role_limits')=={'new':6,'review':2} and
                plan.get('capacity')==8 and plan.get('role_limits')=={'new':6,'review':2})
    actual=[w for w in workers if w.get('ppid')==pid and
            w.get('execution',{}).get('verified') is True and
            all(w['execution'].get(k)==v for k,v in expected.items())]
    counts={kind:sum(w.get('kind')==kind for w in actual) for kind in ['new','review']}
    all_distinct=len({w['pid'] for w in actual})==len(actual) and len({w['execution'].get('session_id') for w in actual})==len(actual)
    complete_scope=len(workers)==8 and len(actual)==8
    report={'coordinator_pid':pid,'observed_at_unix':now,'coordinator_identity_matches':matched,
            'verified_responding_by_kind':counts,'configured_capacity':run.get('capacity'),
            'configuration_matches_authorized_roles':configured,
            'all_active_workers_attested':complete_scope,
            'active_worker_count':len(workers),
            'unattested_or_unexpected_worker_count':len(workers)-len(actual),
            'simultaneous_six_new_plus_two_review_verified':bool(matched and configured and complete_scope and all_distinct and counts=={'new':6,'review':2}),
            'measurement_complete':False,'scope':'Operational evidence; no legal validation or speed gain is inferred from capacity.'}
    if report['simultaneous_six_new_plus_two_review_verified']:
        proof=runtime/'review-lanes-execution.json'
        if not proof.exists() or json.loads(proof.read_text()).get('coordinator_pid')!=pid:
            atomic(proof,report|{'active_agents':actual,**expected})
    metrics=runtime/'job-metrics.jsonl'
    rows=[]
    if metrics.exists():
        for line in metrics.read_text().splitlines():
            try:item=json.loads(line)
            except ValueError:continue # A final append may still be in progress.
            if item.get('coordinator_pid')==pid and item.get('started_at_unix',0)>=run.get('started_at_unix',now):rows.append(item)
    report['cohort_completed_jobs']=len(rows)
    report['cohort_articles']={kind:sum(x.get('articles',0) for x in rows if x.get('kind')==kind and x.get('outcome') in ['accepted','reviewed']) for kind in ['new','review']}
    report['cohort_deferred_jobs']=sum(x.get('outcome')=='deferred' for x in rows)
    successful=[x for x in rows if x.get('outcome') in ['accepted','reviewed']]
    # Exclude initial startup and draining of the former coordinator. A window
    # starts at the first completed job of the new PID and counts later jobs.
    epoch=min((x['finished_at_unix'] for x in successful),default=None)
    hours=(now-epoch)/3600 if epoch is not None else 0
    measured=[x for x in rows if epoch is not None and x.get('started_at_unix',0)>=epoch]
    report['measurement_epoch_unix']=epoch
    report['measurement_hours']=max(0,hours)
    report['measured_successful_by_kind']={kind:sum(x.get('kind')==kind and x.get('outcome') in ['accepted','reviewed'] for x in measured) for kind in ['new','review']}
    report['measurement_complete']=bool(hours>=2 and report['measured_successful_by_kind']['new']>=12 and report['measured_successful_by_kind']['review']>=4)
    report['measured_articles_per_hour']={kind:(sum(x.get('articles',0) for x in measured if x.get('kind')==kind and x.get('outcome') in ['accepted','reviewed'])/hours if hours>0 else None) for kind in ['new','review']}
    report['performance_comparison_limit']='Different codes and article lengths affect throughput; no matched-workload speed or non-regression conclusion is automatic.'
    atomic(runtime/'review-lanes-observation.json',report)
    return report
