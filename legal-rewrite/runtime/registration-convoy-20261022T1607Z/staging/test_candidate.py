import contextlib, hashlib, importlib.util, io, json, os, sys, tempfile, unittest
from pathlib import Path
STAGE=Path(__file__).resolve().parent
PROJECT=STAGE.parents[2]
sys.path.insert(0,str(PROJECT));sys.dont_write_bytecode=True
tempfile.tempdir=str(STAGE)
import register_batches as old
import test_register_batches as regtests
import test_review_prior as revtests
import review_prior as review
spec=importlib.util.spec_from_file_location('register_candidate',STAGE/'register_batches_candidate.py')
new=importlib.util.module_from_spec(spec);spec.loader.exec_module(new)
results={}

def state(case):
    tables={name:case.db.execute('SELECT * FROM '+name+' ORDER BY 1,2').fetchall() for name in ('articles','documents','drafts','draft_sources')}
    files={str(p.relative_to(case.root)):json.loads(p.read_text()) for p in case.root.rglob('*.json')}
    return {'tables':tables,'files':files}

def exercise(mod,scenario):
    regtests.mod=mod
    case=regtests.BatchRegistrationTests();case.setUp()
    try:
        # Three independent articles, including official application notes.
        base=case.db.execute('SELECT * FROM articles').fetchone()
        for i in range(3):
            key='ARTICLE'+str(i);source=list(base);source[1]=key;source[2]='L'+str(i)
            case.db.execute('INSERT INTO articles VALUES(?,?,?,?,?,?,?,?,?,?)',source)
            xml='<ARTICLE><NOTA><CONTENU><p>Application historique '+str(i)+'.</p></CONTENU></NOTA></ARTICLE>'
            case.db.execute('INSERT INTO documents VALUES(?,?,?,?,?,?)',('CODE',key,'ARTICLE',xml,'docsha'+str(i),'archive'))
            row=case.row|{'source_id':key,'number':'L'+str(i)}
            (case.folder/(str(i)+'.json')).write_text(json.dumps([row]))
        case.db.commit()
        with contextlib.redirect_stdout(io.StringIO()):mod.register(case.db,case.root/'batches',True)
        if scenario=='new_row':
            case.db.execute("DELETE FROM drafts WHERE source_id='ARTICLE1'");case.db.execute("DELETE FROM draft_sources WHERE source_id='ARTICLE1'");case.db.commit()
        if scenario=='null_existing':
            case.db.execute("UPDATE drafts SET proposed_xml=NULL WHERE source_id='ARTICLE1'");case.db.commit()
            p=case.root/'registered-batches.json';registry=json.loads(p.read_text());registry['CODE|ARTICLE1']['proposed_sha256']=hashlib.sha256(b'').hexdigest();p.write_text(json.dumps(registry))
        if scenario=='draft_source_mismatch':
            case.db.execute("UPDATE drafts SET source_sha256='other' WHERE source_id='ARTICLE1'");case.db.commit()
        if scenario=='missing_evidence':case.db.execute("DELETE FROM draft_sources WHERE source_id='ARTICLE1'");case.db.commit()
        if scenario in ('changed','reason','review_notes','status'):
            p=case.folder/'1.json';rows=json.loads(p.read_text());field={'changed':'proposed_xml'}.get(scenario,scenario)
            rows[0][field]={'changed':'<p>Le délai est désormais de quatre mois.</p>','reason':'Motif modifié','review_notes':'Réserve modifiée','status':'another_status'}[scenario];p.write_text(json.dumps(rows))
        if scenario=='invalid_unrelated':
            p=case.folder/'2.json';rows=json.loads(p.read_text());rows[0]['proposed_xml']='<p>TODO</p>';p.write_text(json.dumps(rows))
        if scenario=='wrong_source':
            case.db.execute("UPDATE articles SET source_sha256='changed' WHERE id='ARTICLE2'");case.db.commit()
        if scenario=='duplicate':(case.folder/'9.json').write_bytes((case.folder/'2.json').read_bytes())
        before=state(case);changes=case.db.total_changes;calls=[];original=mod.source_notes
        def notes(*a):calls.append(a[2]);return original(*a)
        mod.source_notes=notes
        try:
            with contextlib.redirect_stdout(io.StringIO()):mod.register(case.db,case.root/'batches',True)
            error=None
        except ValueError as e:error=str(e)
        finally:mod.source_notes=original
        after=state(case)
        if error:assert before==after,(scenario,'rejection mutated state')
        return after,error,case.db.total_changes-changes,len(calls)
    finally:case.tearDown()

for scenario in ('unchanged','changed','reason','review_notes','status','missing_evidence','new_row','null_existing','draft_source_mismatch','invalid_unrelated','wrong_source','duplicate'):
    a=exercise(old,scenario);b=exercise(new,scenario)
    assert a[:2]==b[:2],scenario
    results[scenario]={'equal_final_state_and_error':True,'old_changes':a[2],'candidate_changes':b[2],'old_notes_calls':a[3],'candidate_notes_calls':b[3],'error':a[1]}

# Differential actual review commit, including durable archive and manifest.
def review_case(mod):
    revtests.batches=mod;review.register_locked=mod._register
    case=revtests.PriorReviewTests();case.setUp()
    try:
        with contextlib.redirect_stdout(io.StringIO()):review.commit([case.new.copy()],case.expected)
        return state(case)
    finally:case.tearDown()
assert review_case(old)==review_case(new)
results['review_archive_manifest_differential']='exact match'

# Existing focused regression suites run entirely on temporary fixtures.
for label,mod in [('baseline',old),('candidate',new)]:
    regtests.mod=mod;revtests.batches=mod;review.register_locked=mod._register
    suite=unittest.TestSuite([unittest.defaultTestLoader.loadTestsFromModule(regtests),unittest.defaultTestLoader.loadTestsFromModule(revtests)])
    log=io.StringIO()
    with contextlib.redirect_stdout(log):result=unittest.TextTestRunner(stream=log,verbosity=2).run(suite)
    (STAGE/(label+'-tests.log')).write_text(log.getvalue())
    results[label+'_suite']={'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors)}
    assert result.wasSuccessful(),log.getvalue()
(STAGE/'results.json').write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(results,indent=2,ensure_ascii=False))
