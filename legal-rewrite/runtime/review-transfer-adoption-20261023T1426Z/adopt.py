"""Postlaunch adoption only. Never installs, launches, signals or registers.

The unchanged old command guard refused a macOS launcher/image difference.
This separately reviewed adopter proves the exact physical pair with lsof,
then retains all the other native guards and requires real accepted work.
"""
from pathlib import Path
import hashlib,json,sys

ROOT=Path('/Users/alexandremasmejean/.codex/.chatgpt-projects/g-p-6ad59c015c308191aa21cba63c71a6dc/legal-rewrite')
SOURCE=ROOT/'runtime/review-transfer-release-20261023T1414Z'
SOURCE_MANIFEST_SHA='6c990145d221b9353ca4342ba77254d40a57b3a7e74e4c9c486cb06c1f4b381a'
RUN=SOURCE/'runs/transfer-73618-resumed-20261023T1420Z'
OWNER='af204a5b-7dfe-4e7f-b549-937900406b1e'
LAUNCH_SHA='cb773394642afbfa7ce933ee17b090b441857ad9550e32bfdbb99a3eb32b7b2e'
PID=78943

def verify_source():
    manifest=SOURCE/'manifest.json'
    if hashlib.sha256(manifest.read_bytes()).hexdigest()!=SOURCE_MANIFEST_SHA:raise RuntimeError('Reviewed controller seal differs')
    for name,item in json.loads(manifest.read_text())['files'].items():
        path=SOURCE/name
        if Path(name).name!=name or path.is_symlink() or hashlib.sha256(path.read_bytes()).hexdigest()!=item['sha256']:
            raise RuntimeError('Reviewed controller source differs: '+name)

def collect_and_finish(*,finish=False,output=None):
    if output is not None:
        target=Path(output).resolve()
        if target.parent!=Path(__file__).resolve().parent or target.exists():raise RuntimeError('Adoption proof output must be fresh and bounded')
    verify_source();sys.path.insert(0,str(SOURCE))
    try:
        import transfer_controller as t
        from native_attestation import native_launch_attestation
        from accepted_work import accepted_review
        controller=t.Transfer(ROOT,ROOT/'runtime/review-reallocation-rebase-20261023T1058Z',RUN)
        backend=controller.backend;release=backend.reconciliation_precondition()
        with t.locked(RUN/'controller.lock'),t.locked(ROOT/'runtime/supervision/supervisor.lock'):
            state=t.required_json(RUN/'state.json');controller.state=state
            if state.get('owner')!=OWNER:raise t.Conflict('The transfer owner is not the reviewed owner')
            if t.sha(t.raw(RUN/'launch/launch.json'))!=LAUNCH_SHA:raise t.Blocked('The exact one-time launch receipt changed')
            if state.get('phase') not in {'LAUNCHED','ADOPTION_VERIFIED','COMPLETE'}:raise t.Blocked('Existing launch is not the current transfer phase')
            if state.get('root')!=str(ROOT) or state.get('seal')!=t.SEAL or state.get('production_release')!=release or state.get('pins')!=release['expected_baseline_pins']:
                raise t.Blocked('Existing launch/controller/baseline identity differs')
            marker=state['mutations'][t.DISABLED];expected=t.decoded(marker['after'])
            own=t.packed(dict(transfer_owner=state['owner'],state_file=str(RUN/'state.json'),candidate_manifest_sha256=t.SEAL))
            if marker['before'] is not None or expected!=own:raise t.Conflict('Pause owner or beforeimage is unknown')
            actual=t.raw(ROOT/t.DISABLED)
            release_intent=dict(owner=state['owner'],owned_marker_sha256=t.sha(expected),restore=None)
            already_released=state['phase'] in {'ADOPTION_VERIFIED','COMPLETE'} and state.get('pause_release_intent')==release_intent and actual is None
            if actual!=expected and not already_released:raise t.Conflict('An intervening pause or removal is never adopted')
            controller.assert_pins(installed=True)
            # effective_pins validates all journalled current bytes. Never trust
            # a new ready flag, arbitrary replacement policy or modified module.
            pins=controller.effective_pins();backend.check_pins(pins)
            rows=backend.processes();live,workers=t.classify(ROOT,rows)
            if len(live)!=1:raise t.Blocked('New coordinator is not unique')
            run=t.required_json(ROOT/'runtime/exhaustive/coordinator-run.json')
            if live[0]['pid']!=PID:raise t.Blocked('The actual launched PID changed')
            launch=t.required_json(RUN/'launch/launch.json')
            if abs(live[0]['os_started_at_unix']-launch['launched_at_unix'])>2:raise t.Blocked('OS birth no longer binds to this one-time launch')
            phase=t.required_json(ROOT/'runtime/exhaustive/continuation-phase.json')
            hot=t.required_json(ROOT/t.HOT)
            if phase.get('coordinator_pid')!=PID or phase.get('phase')!='review_tail':raise t.Blocked('Actual review-tail phase is not bound to this PID')
            if hot.get('workers')!=8 or hot.get('role_limits')!={'new':6,'review':0} or type(hot.get('review_tail_limit')) is not int or not 0<=hot['review_tail_limit']<=8:raise t.Blocked('Actual explicit tail admission control differs')
            live[0]=t.bind_process(live[0],run,backend.now())
            proof=native_launch_attestation(ROOT,RUN/'launch',live,workers,pins,backend.now())
            proof.update(phase='POSTLAUNCH_NATIVE_ATTESTED',original_command_refusal_preserved=True,
                         no_second_launch=True,adopter_source=str(Path(__file__).resolve()))
            if finish:
                proof['accepted_review']=accepted_review(ROOT,proof['pid'],pins,backend.now())
                worklist_path=ROOT/'runtime/radical-review-20261019.json'
                worklist_raw=t.raw(worklist_path);worklist=json.loads(worklist_raw)
                wanted={(x['code_id'],x['source_id']) for x in proof['accepted_review']['rows']}
                completed={(x['code_id'],x['source_id']) for x in worklist['prior_articles'] if x['review_status']=='completed'}
                if not wanted<=completed:raise t.Blocked('Accepted review is not recorded completed in the canonical worklist')
                if t.raw(worklist_path)!=worklist_raw:raise t.Blocked('Worklist changed during adoption observation; recollect')
                proof['accepted_review']['manifest_completed_rows']=len(wanted)
                proof['accepted_review']['manifest_sha256']=t.sha(worklist_raw)
                backend.check_pins(pins);verify_source()
                if t.raw(ROOT/t.DISABLED)!=actual:raise t.Conflict('Pause intervened during acceptance collection')
                with t.locked(ROOT/'runtime/exhaustive/manual-agent-slots.lock'):
                    if t.required_json(ROOT/'runtime/exhaustive/manual-agent-slots.json')!=[]:raise t.Blocked('Manual reservations changed')
                    controller.finish_adoption(proof)
                proof['phase']=controller.state['phase']
            if output is not None:
                t.durable(target,t.packed(proof))
            return proof
    finally:sys.path.pop(0)

if __name__=='__main__':
    raise SystemExit('Use the reviewed parent orchestration; this module has no launch or configuration flag.')
