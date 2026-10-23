"""Fresh accepted review evidence after a single supervised phase transfer."""
from pathlib import Path
import hashlib,importlib,json,re,sqlite3,sys,types
from transfer_guards import GuardError,read_regular,digest,verify_pins,unchanged

def values(row):
    return (row['source_sha256'],row.get('status','rewrite_draft'),row['proposed_xml'],row['reason'],row['review_notes'])

def accepted_review(root,pid,pins,now):
    root=Path(root).resolve();verify_pins(root,pins);base=root/'runtime/exhaustive';stable={}
    def read(path):
        path=Path(path)
        if not path.resolve().is_relative_to(root):raise GuardError('Accepted evidence escapes project')
        data=read_regular(path);stable[path]=data;return json.loads(data)
    data=read_regular(base/'job-metrics.jsonl');stable[base/'job-metrics.jsonl']=data
    if not data.endswith(b'\n'):raise GuardError('Accepted metrics are incomplete')
    metrics=[json.loads(line) for line in data.splitlines()]
    candidates=[m for m in metrics if m.get('coordinator_pid')==pid and m.get('kind')=='review' and m.get('outcome')=='reviewed']
    if not candidates:raise GuardError('A fresh accepted review from the new coordinator is not yet verified')
    metric=max(candidates,key=lambda x:x['finished_at_unix']);name=metric.get('job')
    if not isinstance(name,str) or Path(name).name!=name:raise GuardError('Unknown accepted job folder')
    run=read(base/'coordinator-run.json')
    if run.get('pid')!=pid or not run['started_at_unix']<=metric['started_at_unix']<=metric['finished_at_unix']<=now:
        raise GuardError('Accepted metric is outside the adopted process lifetime')
    folder=base/'jobs'/name;sources=read(folder/'source.json');answer=read(folder/'answer.json')
    observed=read(folder/('execution-observed-'+str(metric['attempts'])+'.json'))
    parser=types.ModuleType('_accepted_native_parser')
    exec(compile(read_regular(root/'worker_execution.py'),str(root/'worker_execution.py'),'exec'),parser.__dict__)
    log=Path(observed['source_log'])
    if log.parent.resolve()!=folder.resolve():raise GuardError('Accepted native log owner differs')
    execution=parser.verify_execution(folder,stderr_path=log)
    if not execution.get('verified') or execution.get('session_id')!=metric.get('execution_session_id'):
        raise GuardError('Accepted job lacks distinct native execution evidence')
    source_map={(x['code_id'],x['source_id']):x for x in sources};answers={(x['code_id'],x['source_id']):x for x in answer}
    if set(source_map)!=set(answers) or len(source_map)!=len(sources) or len(answers)!=len(answer) or metric['articles']!=len(sources):
        raise GuardError('Accepted answer/source assignments differ')
    owners={};paths=[]
    for path in sorted((root/'batches').glob('*/*.json')):
        if not re.fullmatch(r'(?:batch)?\d+\.json',path.name):continue
        paths.append(path)
        for row in read(path):
            key=(row['code_id'],row['source_id'])
            if key not in source_map:continue
            if key in owners:raise GuardError('Duplicate accepted row owner')
            owners[key]=row
    if set(owners)!=set(source_map):raise GuardError('Accepted owner is missing')
    archives={}
    for path in sorted((root/'revisions/radical-review').glob('*.json')):
        archive=read(path)
        if path.stem!=digest(json.dumps(archive,ensure_ascii=False,sort_keys=True).encode()):raise GuardError('Review archive hash differs')
        for entry in archive:
            key=(entry['code_id'],entry['source_id'])
            if key in source_map and entry['replacement']==owners[key]:archives.setdefault(key,[]).append((path,entry))
    # Module identity was checked during the preceding full reconciliation.
    ingest=sys.modules.get('ingest')
    if ingest is None:
        sys.path.insert(0,str(root))
        try:ingest=importlib.import_module('ingest')
        finally:sys.path.pop(0)
    if Path(ingest.__file__).resolve().parent!=root:raise GuardError('Source-note parser identity is unknown')
    registry=read(root/'registered-batches.json');checked=[]
    db=sqlite3.connect((root/'corpus.sqlite').as_uri()+'?mode=ro',uri=True,timeout=15)
    try:
        db.execute('BEGIN')
        for key,source in source_map.items():
            row=owners[key];raw=answers[key];prior=source.get('previous_draft')
            if prior is None:raise GuardError('Accepted review lacks a whole captured beforeimage')
            current=db.execute('SELECT source_sha256,status,proposed_xml,reason,review_notes FROM drafts WHERE code_id=? AND source_id=?',key).fetchone()
            if current!=values(row) or values(raw)!=values(row):raise GuardError('Accepted answer/owner/DB five-field mismatch')
            if db.execute('SELECT source_sha256,content_xml,valid_from,valid_until FROM articles WHERE code_id=? AND id=?',key).fetchone()!=(source['source_sha256'],source['source_xml'],source['valid_from'],source['valid_until']):raise GuardError('Accepted whole source/version changed')
            if ingest.source_notes(db,*key)!=source['source_notes_xml']:raise GuardError('Accepted NOTA changed')
            if db.execute('SELECT source_xml,valid_from,valid_until FROM draft_sources WHERE code_id=? AND source_id=?',key).fetchone()!=(ingest.source_evidence(source['source_xml'],source['source_notes_xml']),source['valid_from'],source['valid_until']):raise GuardError('Accepted source evidence changed')
            if registry.get('|'.join(key))!=dict(source_sha256=row['source_sha256'],proposed_sha256=digest((row['proposed_xml'] or '').encode())):raise GuardError('Accepted registry differs')
            matches=archives.get(key,[])
            if len(matches)!=1:raise GuardError('Accepted review archive is ambiguous or missing')
            path,entry=matches[0]
            before_hash=digest((entry['proposed_xml'] or '').encode())
            if values(entry)!=values(prior) or before_hash!=prior['proposed_sha256'] or before_hash!=row.get('prior_proposal_sha256'):raise GuardError('Accepted whole beforeimage differs')
            checked.append(dict(code_id=key[0],source_id=key[1],archive=str(path.relative_to(root))))
    finally:db.close()
    unchanged(stable);verify_pins(root,pins)
    if paths!=sorted(p for p in (root/'batches').glob('*/*.json') if re.fullmatch(r'(?:batch)?\d+\.json',p.name)):raise GuardError('Owner membership changed during acceptance check')
    return dict(coordinator_pid=pid,job=name,articles=len(checked),native_execution=execution,rows=checked,
                accepted_at_unix=metric['finished_at_unix'],canonical_mutations=0,speed_gain_claimed=False)
