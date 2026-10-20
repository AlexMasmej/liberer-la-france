"""Register a manually reviewed whole-article pack without changing sources."""
from pathlib import Path
import argparse
import json
import re
import sys

LEGAL=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(LEGAL))
from ingest import open_db,source_notes
from run_exhaustive import validate_answer,mentions_possible_relief
from source_assets import load_companions
import register_batches
import review_prior

parser=argparse.ArgumentParser()
parser.add_argument('--pack',required=True,type=Path)
parser.add_argument('--batch-name',required=True)
parser.add_argument('--index',required=True,type=int)
parser.add_argument('--reference-snapshot',type=Path)
args=parser.parse_args()
snapshot=json.loads(args.reference_snapshot.read_text()) if args.reference_snapshot else None
assert re.fullmatch('[a-z][a-z0-9-]*',args.batch_name)
rows=json.loads((args.pack/'answer.json').read_text())
sources=json.loads((args.pack/'source.json').read_text())
by_key={(a['code_id'],a['source_id']):a for a in sources}
companions=load_companions()
expected=[]
for row in rows:
    key=row['code_id'],row['source_id']
    source=by_key[key].copy()
    source['benefit_check_required']=mentions_possible_relief(source['source_xml'])
    if key in companions:source['source_companions']=companions[key]
    expected.append(source)
validate_answer(rows,expected)
fresh=[];revisions=[];checks=[]
db=open_db(LEGAL/'corpus.sqlite')
try:
    with register_batches.writer_lock():
        if snapshot:
            from reference_coherence import check_guards
            check_guards(db,snapshot)
        for row,source in zip(rows,expected):
            key=row['code_id'],row['source_id']
            assert db.execute('SELECT number,source_sha256,content_xml FROM articles WHERE code_id=? AND id=?',key).fetchone()==(row['number'],row['source_sha256'],source['source_xml']),key
            assert source_notes(db,*key).strip()==source['source_notes_xml'].strip(),key
            current=db.execute('SELECT source_sha256,proposed_xml FROM drafts WHERE code_id=? AND source_id=?',key).fetchone()
            prior=source.get('previous_draft')
            if prior:
                assert current==(prior['source_sha256'],prior['proposed_xml']),key
                guard=prior.get('proposed_sha256',source.get('current_beforeimage_sha256'))
                assert guard and review_prior.digest(prior['proposed_xml'])==guard,key
                prior['proposed_sha256']=guard
                revisions.append(row)
            else:
                assert current is None,('Independent draft appeared; compare before integration',key)
                fresh.append(row)
            checks.append({'code_id':key[0],'source_id':key[1],'number':row['number'],
                           'source_and_notes_verified':True,'prior_checked':True,
                           'proposed_sha256':review_prior.digest(row['proposed_xml'])})
        if fresh:
            folder=LEGAL/'batches'/args.batch_name;folder.mkdir(exist_ok=True)
            path=folder/f'{args.index:03d}.json'
            assert not path.exists(),'Refusing to replace another batch'
            path.write_text(json.dumps(fresh,ensure_ascii=False,indent=2)+'\n')
            register_batches._register(db,LEGAL/'batches',True)
finally:
    db.close()
if revisions:
    wanted={(a['code_id'],a['source_id']) for a in revisions}
    review_prior.commit(revisions,[s for s in expected if (s['code_id'],s['source_id']) in wanted],reference_snapshot=snapshot)
db=open_db(LEGAL/'corpus.sqlite')
try:
    for row in rows:
        assert db.execute('SELECT proposed_xml FROM drafts WHERE code_id=? AND source_id=?',
                          (row['code_id'],row['source_id'])).fetchone()==(row['proposed_xml'],)
finally:
    db.close()
report={'registered_articles':len(rows),'first_drafts':len(fresh),'revisions':len(revisions),
        'checks':checks,'exhaustive_rewriting_complete':False}
(args.pack/'registration.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
