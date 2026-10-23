"""Task-specific parallelism; never changes account-wide agent settings."""
import json

MAX_WORKERS=8
LEGACY_MAX_WORKERS=6

def known_empty_manual_slots(runtime):
    """Unknown reservations are never equivalent to an empty inventory."""
    try:agents=json.loads((runtime/'manual-agent-slots.json').read_text())
    except (OSError,ValueError) as error:raise ValueError('Manual reservation inventory is unknown') from error
    if not isinstance(agents,list) or agents:
        raise ValueError('Manual reservation inventory must be explicitly empty')
    return agents

def _roles(value, *, ceiling=None):
    if not isinstance(value,dict) or set(value)!={'new','review'}:
        raise ValueError('Both drafting and review limits must be explicit')
    for role,limit in [('new',6),('review',2)]:
        count=value[role]
        if type(count) is not int or not 0<=count<=limit:
            raise ValueError('Invalid task role limit')
        if ceiling is not None and count>ceiling[role]:
            raise ValueError('Role limit exceeds authorized capacity')
    return dict(value)

def settings(runtime):
    path=runtime/'parallelism-plan.json'
    if not path.exists():return {'capacity':3,'current_workers':3}
    plan=json.loads(path.read_text())
    for name in ['capacity','current_workers']:
        value=plan[name]
        if type(value) is not int or not 1<=value<=MAX_WORKERS:raise ValueError('Invalid task worker configuration')
    if plan['current_workers']>plan['capacity']:raise ValueError('Worker limit exceeds task capacity')
    roles=plan.get('role_limits')
    if roles is not None:
        roles=_roles(roles)
        if roles['new']<1 or sum(roles.values())!=plan['current_workers']:
            raise ValueError('Role capacities must sum to the authorized worker count')
    elif plan['capacity']>LEGACY_MAX_WORKERS:
        raise ValueError('Extra capacity requires separate drafting and review limits')
    tail=plan.get('review_tail_capacity')
    if tail is not None and (type(tail) is not int or not 1<=tail<=MAX_WORKERS or roles is None):
        raise ValueError('Invalid explicit review-tail authorization')
    mode=plan.get('continuation_mode')
    if mode is not None and (mode!='recover_new_before_reviews' or tail is None):
        raise ValueError('Invalid explicit continuation mode')
    return plan

def drafting_slots(runtime,manual_agents=()):
    return slot_document(runtime,manual_agents)['workers']

def slot_document(runtime,manual_agents=()):
    plan=settings(runtime)
    phase_path=runtime/'continuation-phase.json'
    phase=json.loads(phase_path.read_text()) if phase_path.exists() else {}
    if phase.get('phase')=='review_tail':
        if manual_agents:raise ValueError('Manual reservations require a new coordination and fully drained review tail')
        admission_limits(runtime,plan['capacity'],review_tail=True)
        return json.loads((runtime/'worker-limit.json').read_text())
    if plan.get('role_limits') is None:
        return {'workers':max(1,plan['current_workers']-len(manual_agents))}
    roles=dict(plan['role_limits'])
    if len(manual_agents)>roles['new']:
        raise ValueError('Manual reservations exceed the drafting capacity')
    roles['new']-=len(manual_agents)
    return {'workers':sum(roles.values()),'role_limits':roles}

def admission_limits(runtime,maximum,*,review_tail=False):
    """One atomic control file may pause reviews without borrowing drafting slots."""
    if type(maximum) is not int or not 1<=maximum<=MAX_WORKERS:
        raise ValueError('Invalid coordinator worker capacity')
    plan=settings(runtime)
    path=runtime/'worker-limit.json'
    document=json.loads(path.read_text()) if path.exists() else {'workers':maximum}
    total=document['workers']
    if type(total) is not int or not 1<=total<=MAX_WORKERS:
        raise ValueError('Invalid effective worker limit')
    ceiling=plan.get('role_limits')
    if ceiling is None:
        if maximum>LEGACY_MAX_WORKERS or total>LEGACY_MAX_WORKERS or 'role_limits' in document:
            raise ValueError('Additional reviewers require an explicit role plan')
        return {'workers':min(maximum,total),'role_limits':None}
    if maximum>plan['capacity'] or total>plan['current_workers']:
        raise ValueError('Effective limit exceeds the authorized task capacity')
    roles=_roles(document.get('role_limits',ceiling),ceiling=ceiling)
    if sum(roles.values())>min(maximum,total):
        raise ValueError('Role limits exceed the effective worker limit')
    if review_tail:
        tail=plan.get('review_tail_capacity')
        if tail is None:raise ValueError('Review-tail reallocation requires explicit task authorization')
        known_empty_manual_slots(runtime)
        limit=document.get('review_tail_limit')
        if type(limit) is not int or not 0<=limit<=min(total,tail):
            raise ValueError('Explicit review_tail_limit must be within the effective task capacity')
        total=min(maximum,total,tail)
        return {'workers':total,'role_limits':{'new':0,'review':min(limit,total)}}
    return {'workers':min(maximum,total),'role_limits':roles}
