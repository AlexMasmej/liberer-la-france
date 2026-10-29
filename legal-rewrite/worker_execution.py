"""Pin drafting sessions and verify the CLI's own observed execution header.

A requested configuration or argv is never treated as execution evidence.
Only whitelisted startup fields are returned; agent prompts and reasoning are
not copied into operational receipts.
"""
from pathlib import Path
import hashlib,json,re

MODEL='gpt-6-astra'
EFFORT='medium'
REVIEW={'model':'gpt-6.1-sol','reasoning_effort':'high'}
APPROVED={(MODEL,EFFORT),(REVIEW['model'],REVIEW['reasoning_effort'])}


def requested_execution(runtime,kind=None):
    path=runtime/'model-policy.json'
    spec=json.loads(path.read_text()) if path.exists() else {'model':MODEL,'reasoning_effort':EFFORT}
    if spec.get('model')!=MODEL or spec.get('reasoning_effort')!=EFFORT:
        raise ValueError('Drafting execution policy must explicitly select gpt-6-astra and medium')
    if kind=='review' and 'review_execution' in spec:
        review=spec['review_execution']
        if review!=REVIEW:raise ValueError('Second-pass policy must select gpt-6.1-sol high')
        return dict(REVIEW)
    if kind not in (None,'new','review'):raise ValueError('Unknown execution role')
    return {'model':MODEL,'reasoning_effort':EFFORT}


def cli_options(spec):
    if (spec.get('model'),spec.get('reasoning_effort')) not in APPROVED:
        raise ValueError('Unapproved drafting model or reasoning effort')
    return ['--model',spec['model'],'-c','model_reasoning_effort='+json.dumps(spec['reasoning_effort']),'--color','never']


def parse_startup_log(path):
    path=Path(path)
    if not path.exists():return {'source_log':str(path),'response_started':False}
    with path.open('r',encoding='utf-8',errors='replace') as stream:text=stream.read(524288)
    # CLI warnings can precede the header. Only the first native header block
    # counts; later tool output must not replace the observed startup settings.
    match=re.search(r'(?m)^OpenAI Codex v([^\r\n]+)\r?\n-{8}\r?\n(.*?)\r?\n-{8}(?:\r?\n|$)',text,re.S)
    if not match:return {'source_log':str(path),'response_started':False}
    header=match.group(0);fields={}
    for line in match.group(2).splitlines():
        if ': ' not in line:continue
        name,value=line.split(': ',1)
        if name in fields:return {'source_log':str(path),'response_started':False,'invalid_header':True}
        fields[name]=value
    tail=text[match.end():]
    return {'source_log':str(path),'cli_version':match.group(1),
            'model':fields.get('model'),'reasoning_effort':fields.get('reasoning effort'),
            'session_id':fields.get('session id'),'provider':fields.get('provider'),
            'workdir':fields.get('workdir'),
            'header_sha256':hashlib.sha256(header.encode()).hexdigest(),
            'response_started':bool(re.search(r'(?m)^(?:thinking|exec|codex)\r?$',tail))}


def verify_execution(folder,expected=None,stderr_path=None):
    folder=Path(folder);expected=expected or {'model':MODEL,'reasoning_effort':EFFORT}
    if stderr_path is None:
        paths=list(folder.glob('errors-*.log'))
        stderr_path=max(paths,key=lambda p:p.stat().st_mtime) if paths else folder/'missing-startup.log'
    observed=parse_startup_log(stderr_path)
    observed.update(verified=False,evidence_kind='native_cli_startup_header_and_model_response')
    if (expected.get('model'),expected.get('reasoning_effort')) not in APPROVED:
        observed['status']='unapproved_expected_execution';return observed
    if not observed.get('header_sha256'):
        observed['status']='no_runtime_header';return observed
    if (observed.get('model'),observed.get('reasoning_effort'))!=(expected.get('model'),expected.get('reasoning_effort')):
        observed['status']='model_or_effort_mismatch';return observed
    if observed.get('provider')!='openai':
        observed['status']='provider_mismatch';return observed
    if not re.fullmatch(r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}',observed.get('session_id') or '',re.I):
        observed['status']='invalid_session_id';return observed
    if not observed.get('workdir') or Path(observed['workdir']).resolve()!=folder.resolve():
        observed['status']='workdir_mismatch';return observed
    if not observed['response_started']:
        observed['status']='awaiting_model_response';return observed
    observed.update(verified=True,status='verified')
    return observed
