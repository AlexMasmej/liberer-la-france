"""Task-specific parallelism; never changes account-wide agent settings."""
import json

MAX_WORKERS=6

def settings(runtime):
    path=runtime/'parallelism-plan.json'
    if not path.exists():return {'capacity':3,'current_workers':3}
    plan=json.loads(path.read_text())
    for name in ['capacity','current_workers']:
        value=plan[name]
        if type(value) is not int or not 1<=value<=MAX_WORKERS:raise ValueError('Invalid task worker configuration')
    if plan['current_workers']>plan['capacity']:raise ValueError('Worker limit exceeds task capacity')
    return plan

def drafting_slots(runtime,manual_agents=()):
    return max(1,settings(runtime)['current_workers']-len(manual_agents))
