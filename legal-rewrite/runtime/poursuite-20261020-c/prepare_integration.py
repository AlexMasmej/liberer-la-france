"""Stage only frozen, counter-read whole texts with exact before-images."""
from pathlib import Path
from datetime import datetime, timezone
import copy, hashlib, json, sqlite3, sys

P=Path(__file__).resolve().parent; B=P.parents[1]
sys.path.insert(0,str(B))
from ingest import source_notes
from run_exhaustive import validate_answer
import reference_coherence as rc
def read(p): return json.loads(p.read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,d): p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')

# Later editions replace the same article, never create a second article.
specs=read(P/'integration-specs.json')
selected={}; lineage=[]
for item in specs:
    folder=P/item['folder']; sn=item.get('source','source.json'); an=item.get('answer','answer.json')
    assert (P/item['review']).exists(),item
    manifest_folder=P/item.get('manifest_folder',item['folder'])
    m=read(manifest_folder/'manifest.json')
    assert m.get('frozen') is True,item
    for f,h in m.get('files',m.get('files_sha256',{})).items():
        assert sha(manifest_folder/f)==h,(manifest_folder,f)
    ss,aa=read(folder/sn),read(folder/an)
    validate_answer(copy.deepcopy(aa),copy.deepcopy(ss))
    assert len(ss)==len(aa)
    for s,a in zip(ss,aa):
        k=rc.key(s); assert k==rc.key(a)
        if k in selected:
            assert item.get('override') is True,('Unapproved duplicate',k)
            old=selected[k][0]
            assert (old['source_sha256'],old['source_xml'],old['source_notes_xml'])==(s['source_sha256'],s['source_xml'],s['source_notes_xml']),k
        selected[k]=(s,a,item)
    lineage.append(dict(**item,source_sha256=sha(folder/sn),answer_sha256=sha(folder/an),manifest_sha256=sha(manifest_folder/'manifest.json')))

db=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True); db.execute('BEGIN')
snap=dict(version=3,scope='Phase C whole-text counter-read sources and bounded dependencies',policy_sha256=rc.policy_state(),requirements={},targets={},referrers={},semantic_review_by_jurist=False)
def merge(k,v):
    if k in selected: return
    if k in snap['targets']: assert rc.guard(snap['targets'][k])==rc.guard(v),('Divergent external captures',k)
    assert rc.guard(rc.state(db,k))==rc.guard(v),('External dependency changed',k)
    snap['targets'][k]=v

def check_source(s):
    k=(s['code_id'],s['source_id'])
    assert db.execute('SELECT source_sha256,content_xml FROM articles WHERE code_id=? AND id=?',k).fetchone()==(s['source_sha256'],s['source_xml']),k
    assert source_notes(db,*k)==s['source_notes_xml'],k
    raw=s.get('source_document_xml')
    if raw is not None:
        actual=db.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",k).fetchone()[0]
        actual=actual.decode() if isinstance(actual,bytes) else actual
        assert actual==raw,k
    current=db.execute('SELECT source_sha256,proposed_xml FROM drafts WHERE code_id=? AND source_id=?',k).fetchone()
    old=s.get('previous_draft')
    assert current==((old['source_sha256'],old['proposed_xml']) if old else None),('Before-image changed',k)

for item in specs:
    folder=P/item['folder']
    if (folder/'reference-targets.json').exists():
        captured=read(folder/'reference-targets.json')
        rc.check_guards(db,captured)
        for k,v in captured['targets'].items(): merge(k,v)
        snap['requirements'].update(captured.get('requirements',{}))
        snap['referrers'].update(captured.get('referrers',{}))
    for f in item.get('contexts',[]):
        ctx=read(folder/f)
        if isinstance(ctx,dict): ctx=[ctx]
        for s in ctx:
            k=rc.key(s)
            if k in selected: continue
            if 'view_kind' in s: merge(k,s)
            else:
                check_source(s)
                merge(k,rc.view(db,k))
for s,a,item in selected.values(): check_source(s)
rc.check_guards(db,snap);db.close()
out=P/'integration/edition001';out.mkdir(parents=True,exist_ok=True)
assert not (out/'registration.json').exists()
save(out/'source.json',[x[0] for x in selected.values()])
save(out/'answer.json',[x[1] for x in selected.values()])
save(out/'reference-targets.json',snap)
save(out/'preflight.json',dict(checked_at=datetime.now(timezone.utc).isoformat(),packages=lineage,
    articles=len(selected),external_guarded_targets=len(snap['targets']),canonical_mutation=False,
    all_five_codes_completed=False,new=sum(not x[0].get('previous_draft') for x in selected.values()),
    revisions=sum(bool(x[0].get('previous_draft')) for x in selected.values())))
print(json.dumps(dict(articles=len(selected),dependencies=len(snap['targets']),schema_and_guards=True)))
