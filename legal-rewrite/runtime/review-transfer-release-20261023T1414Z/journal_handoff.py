"""Bounded migration of our drained, never-installed transfer journal.

No model/launcher or canonical registration is called. A new controller cannot
resume another controller's bytes without this exact owned-pause handoff.
"""
import copy,json,time
from pathlib import Path
from contextlib import ExitStack
from transfer_controller import (NativeBackend,APPROVED_ROOT,PACKAGE,SEAL,HOT,DISABLED,
    raw,packed,sha,encoded,decoded,durable,locked,required_json,Blocked,Conflict)

OLD_PACKAGE='review-transfer-release-20261023T1348Z'
OLD_MANIFEST_SHA='b3e6014b7c89395ce50c1bdf0f0165420934f5ae556e969b75ba86f8087a9b04'

def handoff(root,old_folder,new_folder):
    root=Path(root).resolve();old_folder=Path(old_folder).resolve();new_folder=Path(new_folder).resolve()
    if (root!=APPROVED_ROOT or not old_folder.is_relative_to(root/'runtime'/OLD_PACKAGE/'runs') or
            not new_folder.is_relative_to(root/'runtime'/PACKAGE/'runs') or old_folder==new_folder):
        raise Blocked('Journal handoff is outside the reviewed exact project/folders')
    backend=NativeBackend(root);release=backend.reconciliation_precondition()
    package=root/'runtime'/OLD_PACKAGE
    data=raw(package/'manifest.json')
    if data is None or sha(data)!=OLD_MANIFEST_SHA:raise Blocked('Old release seal differs')
    manifest=json.loads(data)
    for name,item in manifest['files'].items():
        if Path(name).name!=name or raw(package/name) is None or sha(raw(package/name))!=item['sha256']:
            raise Blocked('Old sealed release source differs: '+name)
    new_folder.mkdir(parents=True,exist_ok=True)
    with ExitStack() as locks:
        for name in ['runtime/supervision/supervisor.lock','runtime/exhaustive/coordinator.lock',
                     'draft-writer.lock','runtime/exhaustive/manual-agent-slots.lock']:
            locks.enter_context(locked(root/name))
        locks.enter_context(locked(old_folder/'controller.lock'))
        locks.enter_context(locked(new_folder/'controller.lock',must_exist=False))
        receipt=new_folder/'handoff-complete.json'
        if receipt.exists():return required_json(receipt)
        old_bytes=raw(old_folder/'state.json');old=required_json(old_folder/'state.json')
        if (old.get('root')!=str(root) or old.get('seal')!=SEAL or
                old.get('phase') not in {'NATURALLY_DRAINED','RECONCILIATION_REQUIRED'} or
                set(old.get('mutations',{}))!={HOT,DISABLED}):
            raise Blocked('Only an exact naturally-drained, never-installed journal can migrate')
        if old['pins']!=release['expected_baseline_pins']:raise Blocked('Old baseline differs from sealed current release')
        previous=old.get('production_release') or {}
        if (previous.get('controller_sha256')!=manifest['files']['transfer_controller.py']['sha256'] or
                previous.get('release_helpers_sha256')!=manifest['files']['release-input-pins.json']['sha256']):
            raise Blocked('Old journal was not produced by the sealed predecessor')
        if required_json(root/'runtime/exhaustive/manual-agent-slots.json')!=[]:
            raise Blocked('Manual reservations are unknown or nonempty')
        backend.check_pins(old['pins'])
        if raw(root/HOT)!=decoded(old['mutations'][HOT]['after']):raise Conflict('Owned admission control changed')
        idle,_=backend.idle(old['entry']['identity'],set(old.get('worker_groups',[])))
        if not idle:raise Blocked('An old process or descendant remains')
        proof=backend.first_pass_inventory(old['pins'])
        marker=old['mutations'][DISABLED]
        old_marker=decoded(marker['after'])
        expected_marker=dict(transfer_owner=old['owner'],state_file=str(old_folder/'state.json'),candidate_manifest_sha256=SEAL)
        if marker['before'] is not None or json.loads(old_marker)!=expected_marker:
            raise Blocked('The predecessor does not exclusively own this pause')
        new_marker=packed(expected_marker|dict(state_file=str(new_folder/'state.json')))
        original_worker=raw(old_folder/'original-worker-control.json')
        if original_worker is None:raise Blocked('Original worker control beforeimage is unknown')
        intent_path=new_folder/'handoff-intent.json'
        if not intent_path.exists():
            if raw(root/DISABLED)!=old_marker:raise Conflict('Owned predecessor pause was replaced')
            current=copy.deepcopy(old);current['phase']='RECONCILIATION_REQUIRED'
            current['production_release']=release
            current['mutations'][DISABLED]['after']=encoded(new_marker)
            current['handoff_origin']=dict(folder=str(old_folder),journal_sha256=sha(old_bytes),
                predecessor_manifest_sha256=OLD_MANIFEST_SHA,owner=old['owner'])
            current.setdefault('events',[]).append(dict(phase='RECONCILIATION_REQUIRED',at=backend.now(),
                reason='owned_drained_journal_handoff_no_installation'))
            intended=packed(current)
            intent=dict(owner=old['owner'],old_state_sha256=sha(old_bytes),new_state_sha256=sha(intended),
                old_pause=encoded(old_marker),new_pause=encoded(new_marker),new_state=encoded(intended),
                original_worker_control_sha256=sha(original_worker),
                release=release)
            durable(new_folder/'predecessor-state.json',old_bytes)
            durable(new_folder/'predecessor-pause.bin',old_marker)
            durable(new_folder/'handoff-first-pass-inventory.json',packed(proof))
            durable(intent_path,packed(intent))
        intent=required_json(intent_path)
        if (intent['owner']!=old['owner'] or intent['old_state_sha256']!=sha(old_bytes) or
                intent['release']!=release or decoded(intent['old_pause'])!=old_marker or
                decoded(intent['new_pause'])!=new_marker or sha(decoded(intent['new_state']))!=intent['new_state_sha256']):
            raise Conflict('Handoff intent or predecessor changed')
        if raw(root/DISABLED) not in {old_marker,new_marker}:raise Conflict('Intervening supervisor pause is never replaced')
        target=new_folder/'state.json';current=raw(target)
        if current not in {None,decoded(intent['new_state'])}:raise Conflict('Intervening new journal is never replaced')
        original=raw(old_folder/'original-worker-control.json')
        if original is None or sha(original)!=intent['original_worker_control_sha256']:
            raise Conflict('Original admission beforeimage changed')
        copied=raw(new_folder/'original-worker-control.json')
        if copied not in {None,original}:raise Conflict('New original admission beforeimage differs')
        backend.check_pins(old['pins'])
        if copied is None:durable(new_folder/'original-worker-control.json',original)
        if current is None:durable(target,decoded(intent['new_state']))
        if raw(old_folder/'state.json')!=old_bytes:raise Conflict('Predecessor journal intervened before pause CAS')
        if raw(root/DISABLED)==old_marker:durable(root/DISABLED,new_marker)
        if raw(root/DISABLED)!=new_marker:raise Conflict('New pause receipt cannot be issued')
        result=dict(owner=old['owner'],completed_at_unix=backend.now(),old_folder=str(old_folder),new_folder=str(new_folder),
            old_journal_sha256=sha(old_bytes),new_journal_sha256=intent['new_state_sha256'],
            old_pause_sha256=sha(old_marker),new_pause_sha256=sha(new_marker),
            old_sources_and_journal_preserved=True,canonical_writes=0,modules_installed=0,launches=0,
            next_required_phase='fresh_full_reconciliation_under_exclusion')
        durable(receipt,packed(result));return result
