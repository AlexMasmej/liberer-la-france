"""Stage the exact independently reviewed 24+1 fiscal articles, under policy C."""
from pathlib import Path
from datetime import datetime,timezone
import copy,hashlib,json,sqlite3,sys
P=Path(__file__).resolve().parent;B=P.parents[1];sys.path.insert(0,str(B))
from run_exhaustive import validate_answer
from ingest import source_notes
import reference_coherence as rc
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
F=P/'fiscal/edition002';review=P/'fiscal-independent-review/edition002/review.json'
assert review.exists()
m=load(F/'manifest.json');assert m['frozen'] is True
for f,h in m.get('files',m.get('files_sha256',{})).items():assert sha(F/f)==h,f
sources=load(F/'source.json')+load(F/'companion-source.json')
answers=load(F/'answer.json')+load(F/'companion-answer.json')
validate_answer(copy.deepcopy(answers),copy.deepcopy(sources))
keys={rc.key(s)for s in sources};assert len(sources)==len(answers)==len(keys)==25
assert rc.policy_state()=={'policy-coordinations.json':sha(F/'policy-coordinations.json'),'site-summaries.json':sha(F/'site-summaries.json')}
db=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);db.execute('BEGIN')
snapshot=dict(version=3,scope='D24+1 whole articles and bounded context',policy_sha256=rc.policy_state(),requirements={},targets={},referrers={},semantic_review_by_jurist=False)
def check(s):
    k=s['code_id'],s['source_id']
    assert db.execute('SELECT source_sha256,content_xml FROM articles WHERE code_id=? AND id=?',k).fetchone()==(s['source_sha256'],s['source_xml']),k
    assert source_notes(db,*k)==s['source_notes_xml'],k
    if s.get('source_document_xml')is not None:
        raw=db.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",k).fetchone()[0]
        if isinstance(raw,bytes):raw=raw.decode()
        assert raw==s['source_document_xml'],k
    d=db.execute('SELECT source_sha256,proposed_xml FROM drafts WHERE code_id=? AND source_id=?',k).fetchone();old=s.get('previous_draft')
    assert d==((old['source_sha256'],old['proposed_xml'])if old else None),('Before-image changed',k)
def merge(k,v):
    if k in keys:return
    assert rc.guard(rc.state(db,k))==rc.guard(v),k
    if k in snapshot['targets']:assert rc.guard(snapshot['targets'][k])==rc.guard(v),k
    snapshot['targets'][k]=v
captured=load(F/'reference-targets.json');rc.check_guards(db,captured)
for k,v in captured['targets'].items():merge(k,v)
snapshot['requirements'].update(captured['requirements']);snapshot['referrers'].update(captured.get('referrers',{}))
for s in load(F/'references.json'):
    check(s);merge(rc.key(s),rc.view(db,rc.key(s)))
for s,a in zip(sources,answers):check(s);assert rc.key(s)==rc.key(a)
rc.check_guards(db,snapshot);db.close()
out=P/'integration/edition001';out.mkdir(parents=True,exist_ok=True);assert not(out/'registration.json').exists()
save(out/'source.json',sources);save(out/'answer.json',answers);save(out/'reference-targets.json',snapshot)
save(out/'preflight.json',dict(checked_at=datetime.now(timezone.utc).isoformat(),articles=25,
    source_sha256=sha(out/'source.json'),answer_sha256=sha(out/'answer.json'),
    manifest_sha256=sha(F/'manifest.json'),independent_review_sha256=sha(review),
    external_guards=len(snapshot['targets']),policy_unchanged=True,
    rationale='Application de l’autorisation générale de suppressions justifiées article par article ; aucune nouvelle orientation de contrat, taux ou régime central. Les mesures supplémentaires sont documentées dans le fragment D isolé, sans modifier la politique des jobs en cours.',
    exhaustive_rewriting_complete=False))
save(P/'root-independent-review.json',dict(reviewed_at=datetime.now(timezone.utc).isoformat(),
    whole_sources_notes_read=25,whole_proposed_bodies_read=11,
    corrected_bodies_read_entire=['900','1961 ter'],
    critical_C_contexts_read_entire=['1020','1702 bis','1961','881 L'],
    independent_delegate_review=str(review.relative_to(B)),independent_delegate_review_sha256=sha(review),
    corrections=['Aucun supplément de tarif sur timbre valide.','Dérogation au seul premier alinéa1961bis pour double paiement ; imputation du second préservée.','1665bis classé timing, pas baisse définitive de crédit ou IR.'],
    blocking_findings=[],all_new_taxes_or_national_savings=None,semantic_review_by_jurist=False,
    source_sha256=sha(out/'source.json'),answer_sha256=sha(out/'answer.json')))
print(json.dumps(dict(articles=25,external_guarded_targets=len(snapshot['targets']),policy_unchanged=True)))
