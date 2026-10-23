"""Read-only diagnostic, without controller, activation, locks or model calls."""
from pathlib import Path
import hashlib,json,traceback,time
from registration_reconciliation import collect
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
started=time.time();out=HERE/'live-reconciliation-attempt-1.json'
if out.exists():raise RuntimeError('Preserve the preceding diagnostic')
pins=json.loads((HERE/'baseline-policy-pins.json').read_text())
try:
    report=collect(ROOT,pins)
    with out.open('x') as stream:json.dump(report,stream,ensure_ascii=False,indent=2)
    print(json.dumps({k:report[k] for k in ['integrity_status','canonical_identities','collections','validated_batch_records','validated_batch_files','registration_intents','reference_certificates','required_second_pass_states']}))
except Exception as error:
    report=dict(diagnostic='refused',error_type=type(error).__name__,error=str(error),traceback=traceback.format_exc(),elapsed_seconds=time.time()-started,controller_called=False,canonical_writes=False)
    with out.open('x') as stream:json.dump(report,stream,ensure_ascii=False,indent=2)
    print(json.dumps(report))
