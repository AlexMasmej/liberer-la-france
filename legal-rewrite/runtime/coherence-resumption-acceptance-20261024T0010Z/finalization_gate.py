"""Pure finalization gate; no file, model or production DB access."""
from datetime import datetime
def require_complete(observation,wave,now):
    if observation.get('new_pid')!=58195 or wave.get('new_pid')!=58195:
        raise ValueError('This proof is attached only to58195')
    if not observation.get('guarded_phase_matches_current_pid') or not observation.get('all77_current_pins_match'):
        raise ValueError('Actual current phase and current exact pins required')
    at=datetime.fromisoformat(observation['at_utc']).timestamp()
    if not 0<=now-at<300:raise ValueError('Fresh complete acceptance observation required')
    launches=observation.get('exact_two_launch_history',[])
    if [x['pid'] for x in launches]!=[41583,58195]:raise ValueError('Exact two-launch history required')
    responders=wave.get('responders',[])
    if len(responders)!=8 or len({x['execution']['session_id'] for x in responders})!=8:
        raise ValueError('Eight genuinely distinct new responses required')
    wave_at=datetime.fromisoformat(wave['at_utc']).timestamp()
    if not observation['run']['started_at_unix']<=wave_at<=now:raise ValueError('Native wave outside actual run lifetime')
    for x in responders:
        e=x['execution']
        if not e.get('verified') or not e.get('response_started') or e.get('model')!='gpt-6-astra' or e.get('reasoning_effort')!='medium':
            raise ValueError('Actual Astra/medium response required, not a startup header')
        if not x.get('current_frozen_policies_match') or not x.get('priority_present'):
            raise ValueError('Current frozen policy and actual coherence input required')
    accepted=observation.get('accepted_reviews',[])
    if observation.get('accepted_review_verification_complete') is not True or not accepted:
        raise ValueError('Complete fresh accepted review proof required')
    if any(a.get('coordinator_pid')!=58195 or not a.get('rows') or not a['native_execution'].get('verified') for a in accepted):
        raise ValueError('Accepted review proof belongs to another run or lacks full rows')
    return True
