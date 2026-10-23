"""Publish a bounded review origin, leaving the global audit files intact."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,sqlite3,sys
sys.dont_write_bytecode=True
OP=Path(__file__).resolve().parent;ROOT=OP.parents[1];R=ROOT/'runtime'
sys.path.insert(0,str(ROOT))
from ingest import source_notes
F=R/'cvae-semantic-recheck-20261023T1956Z'
A=R/'global-reference-audit-20261023T1908Z'
def sha(b):return hashlib.sha256(b if isinstance(b,bytes) else (b or '').encode()).hexdigest()
def load(p):return json.loads(p.read_text())
def save(n,d):
    with (OP/n).open('x') as f:json.dump(d,f,ensure_ascii=False,indent=2);f.write('\n')

assert sha((F/'artifact-manifest.json').read_bytes())=='c3fd1e986393502b893657cd5ae5b301dd9bf544a6c51da37620fc3f882c069d'
for n,e in load(F/'artifact-manifest.json')['files'].items():
    b=(F/n).read_bytes();assert sha(b)==e['sha256'] and len(b)==e['bytes']
assert load(F/'validation.json')['passed']
articles=load(F/'review-packet.json')['articles']+load(F/'review-dependencies.json')['articles']
assert len(articles)==18
before=(R/'global-reference-audit-latest.json').read_bytes();pointer=json.loads(before)
assert pointer['audit_id']=='384c85d78606cdafab4c33a86b86533004b1ba9ee0a1006779014a07ce0351f6'
checks=[]
db=sqlite3.connect((ROOT/'corpus.sqlite').as_uri()+'?mode=ro',uri=True);db.row_factory=sqlite3.Row
db.execute('PRAGMA query_only=ON');db.execute('BEGIN')
for a in articles:
    key=(a['code_id'],a['id']);d=dict(db.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',key).fetchone());s=dict(db.execute('SELECT * FROM articles WHERE code_id=? AND id=?',key).fetchone())
    assert all(d[k]==a['draft'][k] for k in ['source_sha256','status','proposed_xml','reason','review_notes']),a['key']
    assert all(s[k]==a[k] for k in ['content_xml','source_sha256','valid_from','valid_until']),a['key']
    assert source_notes(db,*key)==a['source_notes_xml']
    checks.append(dict(key=a['key'],whole_source_notes_boundaries_and_five_fields_match=True))
db.close()
for n,e in load(F/'final-state-check.json')['policies'].items():assert sha((ROOT/n).read_bytes())==e['current_sha256']
findings=load(F/'findings-reviewed.json')
all_scope=load(F/'current-scope-structural-findings.json')['findings']
p1=[x for x in all_scope if x['priority']==1]
target='LEGITEXT000006069577|LEGIARTI000048847020'
cvae=[x for x in p1 if x.get('target_key')==target]
others=[x for x in p1 if x.get('target_key')!=target]
assert len(cvae)==4 and len(others)==8
save('current-P1-scope-disposition.json',dict(current_scope_findings=len(all_scope),current_P1=len(p1),current_CVAE_homologues=[x['finding_id'] for x in cvae],other_P1_not_globally_qualified=[dict(finding_id=x['finding_id'],number=x['number'],target_key=x.get('target_key')) for x in others],none_administratively_resolved=True,qualification_scope='Seven historical CVAE situations and their current internal context; not all216 findings or12 current P1.'))
at=datetime.now(timezone.utc).isoformat()
save('semantic-override-preflight.json',dict(at_utc=at,articles=checks,all18match=True,all_four_policies_match=True,origin_manifest_verified=True,code_policy_capacity_or_canonical_mutations=False))
(OP/'before-semantic-global-reference-audit-latest.json').write_bytes(before)
old_override=pointer['semantic_review_overrides']['CVAE']
new_override=dict(folder=str(F),manifest_sha256=sha((F/'artifact-manifest.json').read_bytes()),review_id=findings['review_id'],guarded_audit_id=pointer['audit_id'],scope='Fresh limited CVAE review of13whole texts plus5whole counterparties; all18exactguards/fourpolicies and wider limits must be preserved. FourcurrentCVAE P1 homologues examined; eightotherP1 in source group remain unqualified globally.',last_checked_audit_id=pointer['audit_id'],classification_applies_to_last_checked_snapshot=True)
intent=dict(at_utc=at,action='Add fresh bounded CVAE origin under exact18guards; no published audit/source files modified',pointer_before_sha256=sha(before),previous_CVAE_origin=old_override,new_CVAE_origin=new_override)
save('semantic-override-intent.json',intent)
pointer.setdefault('semantic_review_override_history',[]).append(dict(label='CVAE',replaced_at_utc=at,entry=old_override))
pointer['semantic_review_overrides']['CVAE']=new_override
pointer.setdefault('additional_semantic_review_history',[]).extend(pointer.get('additional_semantic_reviews',[]))
pointer['additional_semantic_reviews']=[dict(folder=str(F),report=str(F/'REPORT.md'),findings_reviewed=7,full_articles_read=18,CVAE_group_articles=13,additional_context_articles=5,effective_inconsistencies_established=0,classification_applies_to_new_snapshot=True,automatic_change=False,jurist_review=False,review_id=findings['review_id'],limits=findings['limits'])]
pointer['semantic_reviews_requiring_new_review']=[x for x in pointer.get('semantic_reviews_requiring_new_review',[]) if x!='CVAE']
pointer['semantic_review_complete']=False
pointer['semantic_review_by_jurist']=False
pointer['latest_semantic_review_amendment']=dict(at_utc=at,evidence=str(OP/'semantic-override-intent.json'),review_origin=str(F),audit_files_immutable_and_unchanged=True,published_inheritance_is_historical_before_this_fresh_review=True,global_contradictions_and_other_scopes_still_open=True)
data=(json.dumps(pointer,ensure_ascii=False,indent=2)+'\n').encode();p=R/'global-reference-audit-latest.json';temp=p.with_name(p.name+'.cvae1956.tmp')
with temp.open('xb') as f:f.write(data);f.flush();os.fsync(f.fileno())
assert p.read_bytes()==before,'Intervening global pointer update'
os.replace(temp,p);assert p.read_bytes()==data
save('semantic-override-published.json',dict(at_utc=at,atomic_replace_completed=True,pointer_before_sha256=sha(before),pointer_after_sha256=sha(data),origin_manifest_sha256=new_override['manifest_sha256'],review_id=findings['review_id'],whole18guards_current=True,no_audit_snapshot_manifest_source_policy_or_pipeline_change=True,global_semantic_or_jurist_validation=False))
print(json.dumps(dict(published=True,review_id=findings['review_id'],origin_manifest_sha256=new_override['manifest_sha256'],global_semantic_review_complete=False)))
