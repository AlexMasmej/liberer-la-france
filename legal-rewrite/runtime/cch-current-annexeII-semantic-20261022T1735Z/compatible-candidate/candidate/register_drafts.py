"""Bind authored drafts to the exact official source version actually read."""
import json,hashlib
from pathlib import Path
from ingest import HERE,open_db,source_notes,source_evidence
db=open_db(HERE/'corpus.sqlite')
drafts=json.loads((HERE/'first_drafts.json').read_text())
bound=[]
for draft in drafts:
    source=db.execute('SELECT source_sha256,number,content_xml,valid_from,valid_until FROM articles WHERE code_id=? AND id=?',(draft['code_id'],draft['source_id'])).fetchone()
    if not source:raise RuntimeError('Missing exact source: '+draft['source_id'])
    sha,number,original,start,end=source
    if number!=draft['number']:raise RuntimeError('Article number mismatch')
    previous=db.execute('SELECT source_sha256 FROM drafts WHERE code_id=? AND source_id=?',(draft['code_id'],draft['source_id'])).fetchone()
    if previous and previous[0]!=sha:
        print('Source changed; preserving the original draft for review:',draft['source_id'])
        continue
    record={**draft,'source_sha256':sha,'status':'rewrite_draft'}
    bound.append(record)
    db.execute('INSERT OR REPLACE INTO drafts VALUES(?,?,?,?,?,?,?)',(draft['code_id'],draft['source_id'],sha,'rewrite_draft',draft['proposed_xml'],draft['reason'],draft['review_notes']))
    db.execute('INSERT OR REPLACE INTO draft_sources VALUES(?,?,?,?,?)',(draft['code_id'],draft['source_id'],source_evidence(original,source_notes(db,draft['code_id'],draft['source_id'])),start,end))
db.commit()
(HERE/'first-drafts-bound.json').write_text(json.dumps(bound,ensure_ascii=False,indent=2))
print(len(bound),'full article drafts linked to exact official source hashes. Drafts are not marked as legally reviewed.')
