from pathlib import Path
import json,hashlib,sqlite3,sys
from datetime import datetime,timezone
P=Path(__file__).resolve().parent;B=P.parents[3];sys.path.insert(0,str(B));from ingest import source_notes
H=lambda x:hashlib.sha256(x if isinstance(x,bytes)else(x or'').encode()).hexdigest()
A=B/'runtime/poursuite-20261020-e/social-coordination';packs=[A/'edition001',A/'complement-r243-59/edition001']
wanted={}
for p in packs:
 for a in json.loads((p/'source.json').read_text()):wanted[(a['code_id'],a['source_id'])]=a
 for a in json.loads((p/'reference-targets.json').read_text())['targets'].values():wanted.setdefault((a['code_id'],a['source_id']),a)
for a in json.loads((packs[0]/'additional-context.json').read_text()):wanted.setdefault((a['code_id'],a['source_id']),a)
for a in json.loads((P/'references.json').read_text()):wanted.setdefault((a['code_id'],a['source_id']),a)
c=json.loads((packs[1]/'C-R243-59-real-referrers.json').read_text());
for a in c:
 a=dict(a,source_sha256=a['guard']['source_sha256']);wanted.setdefault((a['code_id'],a['source_id']),a)
d=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);d.row_factory=sqlite3.Row;d.execute('BEGIN');out=[]
for k,s in wanted.items():
 a=dict(d.execute('select *from articles where code_id=?and id=?',k).fetchone());raw=d.execute("select xml,sha256 from documents where code_id=?and id=?and kind='ARTICLE'",k).fetchone();r=raw['xml'].decode()if isinstance(raw['xml'],bytes)else raw['xml'];notes=source_notes(d,*k);old=d.execute('select *from drafts where code_id=?and source_id=?',k).fetchone();prior=dict(old)if old else None
 g=dict(source_identity=a['source_sha256']==s['source_sha256'],source_body=a['content_xml']==s['source_xml'],notes=notes==s['source_notes_xml'],raw_xml=H(r)==a['source_sha256']==raw['sha256'],current_proposed_body=((prior or{}).get('proposed_xml')==s.get('proposed_xml')if 'proposed_xml'in s else(prior or{}).get('proposed_xml')==(s.get('previous_draft')or{}).get('proposed_xml')))
 assert all(g.values()),(a['number'],g)
 out.append(dict(code_id=k[0],source_id=k[1],number=a['number'],source_sha256=a['source_sha256'],source_xml=a['content_xml'],source_notes_xml=notes,source_document_xml=r,source_document_sha256=H(r),source_archive=a['archive'],source_url='https://www.legifrance.gouv.fr/codes/article_lc/'+k[1],previous_draft=prior,guards=g,source_body_sha256=H(a['content_xml']),source_notes_sha256=H(notes),prior_proposed_sha256=H((prior or{}).get('proposed_xml')),prior_full_row_sha256=H(json.dumps(prior,ensure_ascii=False,sort_keys=True))if prior else None))
d.rollback();d.close();(P/'actual-read-capture.json').write_text(json.dumps(dict(captured_at=datetime.now(timezone.utc).isoformat(),mode='SQLite mode=ro BEGIN',guard_count=5*len(out),rows=out,canonical_mutation=False),ensure_ascii=False,indent=2)+'\n');print(len(out),len(out)*5)
