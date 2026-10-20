"""RO capture, then root-approved metadata-only staging. Never registers anything."""
import argparse, copy, datetime, hashlib, json, pathlib, re, sqlite3, sys

SCRIPT=pathlib.Path(__file__).resolve(); E=SCRIPT.parents[2]; H=SCRIPT.parents[5]
sys.path.insert(0,str(H))
import reference_coherence as rc
from ingest import source_notes
from run_exhaustive import validate_answer, mentions_possible_relief

D=H/'runtime/poursuite-20261020-d/social-context-review/edition001'
C=H/'runtime/poursuite-20261020-c/certificate-refresh/refreshed003'
TARGET='LEGITEXT000006073189|LEGIARTI000053220874'
OPTIONAL='LEGITEXT000006073189|LEGIARTI000041396065'
NAMES={'R243-17','R243-18','R243-19','R243-59','R243-59-6-A'}
ALLOWED={'reference_checks','reference_coherence'}
FROZEN={E/'edition001/source.json':'46b7e86da226c423cf94c1948dd460a03d79f0e0fe79f27347d95c303004f5d9',
 E/'edition001/answer.json':'8ced38d1de77327a25f2862fe698a7e12a2d1c7e58a1c691c06496e9684356c7',
 E/'complement-r243-59/edition001/source.json':'1c07e5d51674da1b949b272b1a2c1763d1849e2cf01b2c4b38b5106832ea7592',
 E/'complement-r243-59/edition001/answer.json':'4622a98ac16e19485fad22a1f70bc7b4fdf1e6f1e633fc67eebdaac475ce4255',
 C/'answer.json':'626f0d00e183aadff71eb10824c9ce17fc2cb67989e929ea4119ea60378b9e52',
 E/'final-guards.json':'2c8730b9e8521d331f80c51ca4241704f8a3b99e655c34de666a2510f60d8b4d',
 D/'manifest.json':'d96cec5f43ceb7751ad7b742252cb8100d856f47a8d0ca0573c18ae7226ff2e6'}
def read(p):return json.loads(p.read_text())
def sha(s):return hashlib.sha256((s or '').encode()).hexdigest()
def fs(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def digest(x):return sha(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')))
def require(ok,msg):
    if not ok:raise ValueError(msg)
def unchanged_except_references(before,after):
    require({k:v for k,v in before.items() if k not in ALLOWED}==
            {k:v for k,v in after.items() if k not in ALLOWED},'A non-reference field changed')
def approved(approval,capture_sha,pairs,removals):
    require(approval.get('version')==1 and approval.get('approved') is True and
            approval.get('approved_by')=='root' and approval.get('capture_sha256')==capture_sha,
            'Explicit root approval bound to this capture SHA is required')
    require(isinstance(approval.get('approved_at'),str) and approval['approved_at'].strip(),'Approval date required')
    require(approval.get('approved_optional_check_removals')==removals,'Any optional check removal requires explicit root approval')
    rows=approval.get('analyses',[])
    require(isinstance(rows,list) and len(rows)==len(pairs),'Exactly the three changed-target analyses required')
    result={}
    for row in rows:
        pair=(row.get('key'),row.get('target_key'))
        require(pair in pairs and pair not in result,'Unexpected or duplicate approved analysis')
        txt=row.get('assessment')
        require(isinstance(txt,str) and len(txt.strip())>=80,'Article-specific full assessment required')
        result[pair]=txt
    require(set(result)==pairs,'Missing approved analysis');return result
def frozen():
    for p,want in FROZEN.items():require(fs(p)==want,'Frozen evidence changed: '+str(p))
    require(fs(D/'captured-guard-records.json')==read(D/'manifest.json')['files']['captured-guard-records.json'],'Source guard evidence changed')
    oldguards={rc.key(x):x for x in read(D/'captured-guard-records.json')}
    policy=read(E/'final-guards.json')['policy_guards']
    require(rc.policy_state()=={n:x['current_sha256'] for n,x in policy.items()},'Policy changed since E review')
    expected={a['number']:a for a in read(E/'edition001/answer.json')+read(C/'answer.json') if a['number'] in NAMES}
    # The E entries override the older C definitions.
    expected.update({a['number']:a for a in read(E/'edition001/answer.json') if a['number'] in NAMES})
    r59=read(E/'complement-r243-59/edition001/answer.json')[0];expected[r59['number']]=r59
    return oldguards,expected,r59
def connect():
    db=sqlite3.connect('file:'+str(H/'corpus.sqlite')+'?mode=ro',uri=True);db.row_factory=sqlite3.Row;db.execute('BEGIN');return db
def db_record(db,k):
    code,sid=k.split('|');a=db.execute('select * from articles where code_id=? and id=?',(code,sid)).fetchone()
    d=db.execute('select * from drafts where code_id=? and source_id=?',(code,sid)).fetchone()
    raw=db.execute("select xml from documents where code_id=? and id=? and kind='ARTICLE'",(code,sid)).fetchone()
    require(a is not None and raw is not None,'Missing canonical article/raw XML '+k)
    xml=raw['xml'].decode() if isinstance(raw['xml'],bytes) else raw['xml'];notes=source_notes(db,code,sid)
    return {'key':k,'code_id':code,'source_id':sid,'number':a['number'],'source_sha256':a['source_sha256'],
     'source_xml':a['content_xml'],'source_notes_xml':notes,'raw_document_xml':xml,
     'source_body_sha256':sha(a['content_xml']),'source_notes_sha256':sha(notes),'raw_document_sha256':sha(xml),
     'draft':dict(d) if d else None}
def owners(keys):
    found={}
    for p in sorted((H/'batches').glob('*/*.json')):
        if not re.fullmatch(r'(?:batch)?\d+\.json',p.name):continue
        raw=p.read_bytes();rows=json.loads(raw)
        for i,a in enumerate(rows):
            if rc.key(a) in keys:found[rc.key(a)]={'path':str(p.relative_to(H)),'file_sha256':hashlib.sha256(raw).hexdigest(),'index':i,'row':a}
    require(set(found)==set(keys),'Missing canonical batch owner');return found
def check_source(record,oldguards):
    old=oldguards[record['key']]
    for field in ['source_sha256','source_body_sha256','source_notes_sha256','raw_document_sha256']:
        require(record[field]==old[field],'Source/notes/raw XML changed: '+record['key']+' '+field)
def new_folder(out):
    out=out.resolve();base=(E/'recertification').resolve()
    require(base in out.parents and not out.exists(),'Output must be a new isolated subfolder of '+str(base));return out
def capture(out):
    oldguards,expected,r59=frozen();out=new_folder(out);keys={rc.key(x) for x in expected.values()};owned=owners(keys)
    sources=[];before=[];records={};db=connect()
    try:
        for k in sorted(keys):
            r=db_record(db,k);check_source(r,oldguards);a=owned[k]['row'];expected_row=expected[r['number']]
            require(r['draft'] is not None,'Expected registered draft missing '+k)
            for f in ['source_sha256','proposed_xml','status','reason','review_notes']:
                require(a.get(f)==r['draft'][f],'Batch/DB mismatch '+k+' '+f)
            for f,v in expected_row.items():
                if f not in ALLOWED:require(a.get(f)==v,'Approved E/C field not registered exactly '+k+' '+f)
            prior=dict(r['draft']);prior['proposed_sha256']=sha(prior['proposed_xml'])
            sources.append({f:r[f] for f in ['code_id','source_id','number','source_sha256','source_xml','source_notes_xml']}|
              {'previous_draft':prior,'impact_check_required':True,'benefit_check_required':mentions_possible_relief(r['source_xml'])})
            before.append(a);records[k]=r
        snap=rc.capture(db,sources,before)
        for k in snap['targets']:
            records[k]=db_record(db,k);check_source(records[k],oldguards)
        target=records[TARGET]
        require(target['draft'] is not None and target['draft']['proposed_xml']==r59['proposed_xml'] and
                target['draft']['status']==r59['status'],'R243-59 exact E future body is not actually registered')
        removals={}
        for a in before:
            cert=a.get('reference_coherence',{});needs=set(snap['requirements'][rc.key(a)])
            oldneeds=set(cert.get('targets',{}));extra=oldneeds-needs
            require(needs<=oldneeds and extra<={OPTIONAL},'Reference requirements changed beyond the known optional check')
            removals[rc.key(a)]=sorted(extra)
            checks=a.get('reference_checks',[])
            require(len(checks)==len(oldneeds) and {x['target_key'] for x in checks}==oldneeds,'Incomplete old explicit checks')
            for k in needs-{TARGET}:
                require(cert['targets'][k]==rc.guard(snap['targets'][k]),'Another target changed: '+k)
            require((TARGET in needs)==(a['number'] in {'R243-17','R243-18','R243-59-6-A'}),'Unexpected R243-59 referrer set')
        require(owned==owners(keys),'Canonical batch changed during capture');rc.check_guards(db,snap)
    finally:db.rollback();db.close()
    out.mkdir(parents=True)
    for n,x in [('source.json',sources),('before-answer.json',before),('reference-targets.json',snap),('db-records.json',records),('batch-owners.json',owned)]:dump(out/n,x)
    info={'version':1,'captured_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'mode':'RO BEGIN; no registration',
      'helper_sha256':fs(SCRIPT),'files':{n:fs(out/n) for n in ['source.json','before-answer.json','reference-targets.json','db-records.json','batch-owners.json']},
      'expected_R243_59_proposed_sha256':sha(r59['proposed_xml']),'policy_sha256':rc.policy_state(),
      'optional_checks_to_remove':removals,'root_approval_required':True}
    dump(out/'capture.json',info)
    template={'version':1,'approved':False,'approved_by':'root','approved_at':'','capture_sha256':fs(out/'capture.json'),
      'approved_optional_check_removals':removals,'analyses':[{'key':rc.key(a),'target_key':TARGET,'assessment':''} for a in before if TARGET in snap['requirements'][rc.key(a)]]}
    dump(out/'approval.template.json',template);print('Capture only:',out/'capture.json',fs(out/'capture.json'))
def stage(cap,approval_path,out):
    _,_,r59=frozen();cap=cap.resolve();info=read(cap/'capture.json');out=new_folder(out)
    require(info.get('version')==1 and info.get('helper_sha256')==fs(SCRIPT),'Wrong helper/capture version')
    require(info.get('policy_sha256')==rc.policy_state(),'Policy changed after capture')
    require(set(info['files'])=={'source.json','before-answer.json','reference-targets.json','db-records.json','batch-owners.json'},'Unexpected capture file set')
    for n,want in info['files'].items():require(n==pathlib.Path(n).name and fs(cap/n)==want,'Capture evidence changed '+n)
    S=read(cap/'source.json');before=read(cap/'before-answer.json');snap=read(cap/'reference-targets.json')
    require(info['expected_R243_59_proposed_sha256']==sha(r59['proposed_xml']) and
            snap['targets'][TARGET]['proposed_xml']==r59['proposed_xml'],'Capture does not contain the exact registered E R243-59 body')
    require(len(S)==5 and {a['number'] for a in S}==NAMES,'Capture must contain exactly the five reviewed articles')
    pairs={(rc.key(a),TARGET) for a in before if TARGET in snap['requirements'][rc.key(a)]}
    require(len(pairs)==3,'Expected three changed-target analyses')
    analyses=approved(read(approval_path),fs(cap/'capture.json'),pairs,info['optional_checks_to_remove'])
    db=connect()
    try:
        for k,r in read(cap/'db-records.json').items():require(db_record(db,k)==r,'DB source/notes/raw/draft changed '+k)
        require(owners({rc.key(a) for a in before})==read(cap/'batch-owners.json'),'Canonical batch changed after capture')
        rc.check_guards(db,snap);rows=copy.deepcopy(before)
        for a in rows:
            a['reference_checks']=[ck for ck in a['reference_checks'] if ck['target_key'] in snap['requirements'][rc.key(a)]]
            for ck in a['reference_checks']:
                if ck['target_key']==TARGET:
                    ck['view_sha256']=snap['targets'][TARGET]['view_sha256'];ck['assessment']=analyses[(rc.key(a),TARGET)]
        validate_answer(rows,S);rc.accept_checks(rows,S,snap)
        for old,a,s in zip(before,rows,S):
            unchanged_except_references(old,a)
            require(rc.certificate_current(db,s,a['proposed_xml'],a['reference_coherence']),'Generated certificate is not current')
    finally:db.rollback();db.close()
    out.mkdir(parents=True)
    for n,x in [('source.json',S),('answer.json',rows),('reference-targets.json',snap)]:dump(out/n,x)
    report={'metadata_only':True,'allowed_changed_fields':sorted(ALLOWED),'articles':5,'registered':False,
      'capture_sha256':fs(cap/'capture.json'),'approval_sha256':fs(approval_path),'helper_sha256':fs(SCRIPT),
      'files':{n:fs(out/n) for n in ['source.json','answer.json','reference-targets.json']},
      'post_registration_workflow_fields':['policy_review_id','prior_proposal_sha256'],
      'post_registration_limit':'review_prior.commit may update these two workflow-provenance fields; root must compare them explicitly. Bodies, impacts, reasons, notes and every other non-reference field must remain exact. The staging invariant itself allows no provenance-field change.',
      'registration_condition':'Under the registration writer lock recheck these full capture DB/raw/owner guards as well as register_pack reference/own guards. Any later delta blocks inscription; staging is no approval to overwrite it.'}
    dump(out/'staging.json',report);print('Staging only, no registration:',out)
def main():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='mode',required=True)
    a=sub.add_parser('capture');a.add_argument('--out',type=pathlib.Path,required=True)
    b=sub.add_parser('stage');b.add_argument('--capture',type=pathlib.Path,required=True);b.add_argument('--approval',type=pathlib.Path,required=True);b.add_argument('--out',type=pathlib.Path,required=True)
    a=p.parse_args()
    if a.mode=='capture':capture(a.out)
    else:stage(a.capture,a.approval,a.out)
if __name__=='__main__':main()
