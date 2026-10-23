"""Prepared recovery of one evidence space, executable only after a full drain.

No worker is launched or stopped. No live coordinator is ever adopted by this
helper: its in-memory dependency reservations cannot protect an external writer.
Default mode is a fully guarded dry run. Nothing here has been applied.
"""
from pathlib import Path
from contextlib import contextmanager, ExitStack
from datetime import datetime, timezone
import argparse, copy, fcntl, hashlib, json, os, re, shlex, sqlite3, subprocess, sys

FOLDER = Path(__file__).resolve().parent
HERE = FOLDER.parents[2]
sys.path.insert(0, str(HERE))
import run_exhaustive as runner
import supervise_exhaustive as supervisor
import register_batches
from ingest import source_notes, source_evidence
from worker_execution import requested_execution, verify_execution

JOB_NAME = 'travail-00396-resume-d9t22r7o'
KEY = ('LEGITEXT000006072050','LEGIARTI000033407486')
BEFORE = '2° Un comité stratégique peut être institué ;3° Un comité des nominations et des rémunérations peut être institué.'
AFTER = '2° Un comité stratégique peut être institué ; 3° Un comité des nominations et des rémunérations peut être institué.'
LOCKS = ('runtime/supervision/supervisor.lock', 'runtime/exhaustive/coordinator.lock',
         'draft-writer.lock', 'runtime/exhaustive/manual-agent-slots.lock')

def digest(data):
    return hashlib.sha256(data.encode() if isinstance(data,str) else data).hexdigest()

def atomic_durable(path,value):
    """Keep a durable intent before the canonical commit and mirrors after it."""
    path=Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_name('.'+path.name+'.'+str(os.getpid())+'.tmp')
    if temporary.exists():raise ValueError('Unreconciled helper temporary file: '+str(temporary))
    data=(json.dumps(value,ensure_ascii=False,indent=2)+'\n').encode()
    descriptor=os.open(temporary,os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
    try:
        with os.fdopen(descriptor,'wb') as stream:
            stream.write(data);stream.flush();os.fsync(stream.fileno())
        os.replace(temporary,path)
        parent_fd=os.open(path.parent,os.O_RDONLY)
        try:os.fsync(parent_fd)
        finally:os.close(parent_fd)
    finally:
        if temporary.exists():temporary.unlink()

def assert_patch_scope(original,candidate):
    if not isinstance(original,list) or not isinstance(candidate,list) or len(original)!=24 or len(candidate)!=24:
        raise ValueError('The complete frozen 24-article array is required')
    altered=copy.deepcopy(original)
    positions=[i for i,row in enumerate(altered) if (row.get('code_id'),row.get('source_id'))==KEY]
    if len(positions)!=1:raise ValueError('Pinned metadata article is absent or duplicated')
    row=altered[positions[0]]
    if row.get('number')!='R5315-5':raise ValueError('Pinned metadata article number differs')
    effects=row.get('substantive_impact',{}).get('effects',[])
    if len(effects)!=1 or effects[0].get('measure_id')!='afpa-comites-facultatifs' or effects[0].get('proposed_quote')!=BEFORE:
        raise ValueError('Pinned original effect differs')
    effects[0]['proposed_quote']=AFTER
    if altered!=candidate:
        raise ValueError('Change exceeds the one evidence-space correction, including other metadata')
    return True

def assert_idle_inventory(inventory=None):
    # A failed or unavailable ps inventory raises; unknown is never empty.
    if inventory is None:
        output=subprocess.check_output(['/bin/ps','-axo','pid=,ppid=,command='],text=True,timeout=15)
        if not output.strip():raise ValueError('System process inventory unexpectedly empty')
        rows=[]
        for line in output.splitlines():
            parts=line.strip().split(None,2)
            relevant=(str(HERE/'run_exhaustive.py') in line or str(HERE/'runtime/exhaustive/jobs') in line)
            try:
                if len(parts)!=3:raise ValueError('Malformed process record')
                args=shlex.split(parts[2])
                rows.append({'pid':int(parts[0]),'ppid':int(parts[1]),'args':args})
            except ValueError:
                if relevant:raise ValueError('Relevant process inventory is ambiguous')
    else:rows=inventory
    if not isinstance(rows,list):raise ValueError('System process inventory unavailable')
    coordinators=supervisor.coordinator_processes(rows)
    workers=supervisor.job_workers(rows)
    if coordinators or workers:
        raise ValueError('Full drain required: coordinator or native workers still present')
    return {'coordinators':0,'native_workers':0,'inventory_observed':True}

@contextmanager
def drained_locks(root=HERE, inventory_check=assert_idle_inventory):
    # Supervisor lock prevents its launch; coordinator lock prevents a manual
    # coordinator launch; writer and manual-slot locks exclude cooperating
    # canonical/manual mutations. All stay held through commit and mirroring.
    with ExitStack() as stack:
        for relative in LOCKS:
            path=root/relative
            stream=stack.enter_context(path.open('a'))
            try:fcntl.flock(stream,fcntl.LOCK_EX|fcntl.LOCK_NB)
            except BlockingIOError:raise ValueError('Required drain lock is busy: '+relative)
        proof=inventory_check()
        yield proof
        inventory_check()

def assert_pins(manifest):
    for item in manifest['files']:
        path=HERE/item['path']
        if not path.is_file() or digest(path.read_bytes())!=item['sha256']:
            raise ValueError('Pinned evidence/code/policy/catalogue file changed: '+item['path'])

def assert_no_owners(keys,batch_path):
    if batch_path.exists():raise ValueError('Recovery batch path already exists; reconcile, never overwrite')
    owners=[]
    for path in sorted((HERE/'batches').glob('*/*.json')):
        if not re.fullmatch(r'(?:batch)?\d+\.json',path.name):continue
        rows=json.loads(path.read_text())
        for row in rows:
            if (row.get('code_id'),row.get('source_id')) in keys:
                owners.append({'path':str(path),'source_id':row.get('source_id')})
    if owners:raise ValueError('An active batch already owns a recovery identity: '+str(owners))
    registry_path=HERE/'registered-batches.json'
    registry=json.loads(registry_path.read_text())
    if any('|'.join(key) in registry for key in keys):
        raise ValueError('A recovery identity already has a registry owner')
    return registry

def assert_source_guards(db,sources,manifest):
    expected=manifest['canonical_sources']
    if len(sources)!=24 or len(expected)!=24:raise ValueError('Incomplete source guards')
    for source in sources:
        key=source['code_id'],source['source_id']
        saved=expected['|'.join(key)]
        actual=db.execute('SELECT number,source_sha256,content_xml,valid_from,valid_until,state,archive FROM articles WHERE code_id=? AND id=?',key).fetchone()
        if actual is None:raise ValueError('Missing canonical source '+key[1])
        if digest(json.dumps(list(actual),ensure_ascii=False,separators=(',',':')))!=saved['article_fields_sha256']:
            raise ValueError('Canonical source/version fields changed '+key[1])
        if actual[0]!=source['number'] or actual[1]!=source['source_sha256'] or actual[2]!=source['source_xml'] or actual[3:5]!=(source['valid_from'],source['valid_until']):
            raise ValueError('Frozen article source differs '+key[1])
        notes=source_notes(db,*key)
        if notes!=source.get('source_notes_xml','') or digest(notes)!=saved['source_notes_sha256']:
            raise ValueError('Canonical NOTA changed '+key[1])
        document=db.execute("SELECT xml,sha256,archive FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",key).fetchone()
        if document is None:raise ValueError('Missing whole source document '+key[1])
        raw=document[0].encode() if isinstance(document[0],str) else bytes(document[0])
        if digest(raw)!=saved['whole_document_sha256'] or list(document[1:])!=saved['document_record']:
            raise ValueError('Whole source document changed '+key[1])
        for table in ['drafts','draft_sources']:
            if db.execute('SELECT 1 FROM '+table+' WHERE code_id=? AND source_id=?',key).fetchone():
                raise ValueError('Recovery before-image is no longer absent in '+table+': '+key[1])

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply',action='store_true')
    args=parser.parse_args()
    manifest=json.loads((FOLDER/'drained-registration-guards.json').read_text())
    if (FOLDER/'registration-intent.json').exists() or (FOLDER/'registration-complete.json').exists():
        raise ValueError('Prior recovery intent/completion exists: reconcile manually, do not repeat')
    with drained_locks() as inventory:
        assert_pins(manifest)
        job=HERE/'runtime/exhaustive/jobs'/JOB_NAME
        sources=json.loads((FOLDER/'source.json').read_text())
        original=json.loads((FOLDER/'answer.original.json').read_text())
        candidate=json.loads((FOLDER/'answer.candidate.json').read_text())
        assert_patch_scope(original,candidate)
        if json.loads((job/'answer.json').read_text())!=original:
            raise ValueError('Original failed response has changed')
        if not runner.policy_is_current(job):raise ValueError('Frozen drafting policy is stale')
        execution=verify_execution(job,requested_execution(runner.RUNTIME),job/'errors-3.log')
        if not execution.get('verified'):raise ValueError('Native execution is unverified')
        snapshot=json.loads((FOLDER/'reference-targets.json').read_text())
        keys={(s['code_id'],s['source_id']) for s in sources}
        if len(keys)!=24:raise ValueError('Duplicate source identity')
        manual=json.loads((HERE/'runtime/exhaustive/manual-agent-slots.json').read_text())
        if manual not in ({},[]):raise ValueError('Manual reservations need explicit drained reconciliation')
        batch_path=HERE/'batches/automatic-travail/00396.json'
        registry=assert_no_owners(keys,batch_path)
        validated=runner.validate_answer(copy.deepcopy(candidate),sources)
        runner.reference_audit.accept_checks(validated,sources,snapshot)
        # Dry run opens the canonical database read-only. Applying opens only the
        # established database, with no schema or journal-mode changes.
        uri='file:'+str(HERE/'corpus.sqlite')+('?mode=rw' if args.apply else '?mode=ro')
        db=sqlite3.connect(uri,uri=True,timeout=0)
        canonical_committed=False
        report={'checked_at_utc':datetime.now(timezone.utc).isoformat(),'job':JOB_NAME,
                'mode':'apply' if args.apply else 'drained_preflight','registered':False,
                'only_change':'R5315-5 impact proposed_quote: one inserted space',
                'all_24_normative_texts_and_other_metadata_unchanged':True,
                'sources':24,'new_model_calls':0,'global_settings_changed':False,
                'inventory':inventory,'native_execution':execution,'batch_path':str(batch_path),
                'guards_manifest_sha256':digest((FOLDER/'drained-registration-guards.json').read_bytes()),
                'semantic_review_by_jurist':False}
        try:
            db.execute('BEGIN IMMEDIATE' if args.apply else 'BEGIN')
            assert_source_guards(db,sources,manifest)
            runner.reference_audit.check_guards(db,snapshot)
            records,diagnostics,files=register_batches.validate_batches(db,FOLDER/'isolated-batches')
            if len(records)!=24:raise ValueError('Real batch gate did not validate 24 articles')
            assert_pins(manifest)
            if not runner.policy_is_current(job):raise ValueError('Policy changed before canonical commit')
            assert_idle_inventory()
            assert_no_owners(keys,batch_path)
            if args.apply:
                registry_path=HERE/'registered-batches.json'
                atomic_durable(FOLDER/'registry-before.json',registry)
                atomic_durable(FOLDER/'failed-resolutions-before.json',json.loads((runner.RUNTIME/'failed-job-resolutions.json').read_text()))
                for row in validated:
                    key=row['code_id'],row['source_id']
                    source=next(s for s in sources if (s['code_id'],s['source_id'])==key)
                    db.execute('INSERT INTO drafts VALUES(?,?,?,?,?,?,?)',(*key,row['source_sha256'],row['status'],row['proposed_xml'],row['reason'],row['review_notes']))
                    db.execute('INSERT INTO draft_sources VALUES(?,?,?,?,?)',(*key,source_evidence(source['source_xml'],source['source_notes_xml']),source['valid_from'],source['valid_until']))
                    registry['|'.join(key)]={'source_sha256':row['source_sha256'],'proposed_sha256':runner.digest(row['proposed_xml'])}
                # Intent contains the complete accepted row candidates and pins,
                # durable before SQLite commit. Failed mirrors require recovery,
                # never another insertion or acceptance claim.
                atomic_durable(FOLDER/'registration-intent.json',report|{'rows':validated,'candidate_sha256':digest((FOLDER/'answer.candidate.json').read_bytes())})
                db.commit();canonical_committed=True
                atomic_durable(batch_path,validated)
                atomic_durable(registry_path,registry)
                report.update(registered=True,accepted_articles=24)
                atomic_durable(FOLDER/'registration-complete.json',report)
                resolution_path=runner.RUNTIME/'failed-job-resolutions.json'
                resolutions=json.loads(resolution_path.read_text())
                if any(r.get('job')==JOB_NAME for r in resolutions):raise ValueError('Duplicate resolution: reconcile completed registration')
                resolutions.append({'job':JOB_NAME,'accepted_articles':24,'resolution':str(FOLDER/'registration-complete.json'),'at_utc':report['checked_at_utc'],'original_failure_preserved':True})
                atomic_durable(resolution_path,resolutions)
            else:
                db.rollback()
        except BaseException:
            if not canonical_committed:db.rollback()
            # A committed DB is never falsely rolled back by a mirror error.
            raise
        finally:db.close()
        atomic_durable(FOLDER/('adoption.json' if args.apply else 'drained-preflight.json'),report)
        print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
