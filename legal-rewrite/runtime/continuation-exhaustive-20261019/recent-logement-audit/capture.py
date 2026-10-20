from pathlib import Path
import datetime,hashlib,json,re,sqlite3,sys
B=Path(__file__).resolve().parents[3]
P=Path(__file__).resolve().parent
sys.path.insert(0,str(B))
from ingest import source_notes
H=lambda v:hashlib.sha256(v.encode()if isinstance(v,str)else v).hexdigest()
manual=set();automatic={}
for path in sorted((B/'batches').glob('*/*.json')):
    if not re.fullmatch(r'(?:batch)?\d+\.json',path.name):continue
    for row in json.loads(path.read_text()):
        k=row['code_id'],row['source_id']
        if not path.parent.name.startswith('automatic-'):manual.add(k)
        else:automatic[k]=(row,str(path.relative_to(B)))
c=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True)
c.row_factory=sqlite3.Row;c.execute('BEGIN');cu=[];seen=set()
for path in sorted((B/'batches/automatic-urbanisme').glob('*.json'),key=lambda p:p.stat().st_mtime,reverse=True):
    for row in json.loads(path.read_text()):
        k=row['code_id'],row['source_id']
        if k in manual or k in seen or row.get('prior_proposal_sha256'):continue
        d=c.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',k).fetchone()
        if not d or d['proposed_xml']!=row['proposed_xml']:continue
        seen.add(k);cu.append((k,str(path.relative_to(B))))
        if len(cu)==24:break
    if len(cu)==24:break
cch=[]
for d in c.execute('SELECT rowid,* FROM drafts WHERE code_id=? ORDER BY rowid DESC',('LEGITEXT000006074096',)):
    k=d['code_id'],d['source_id']
    if k in manual or k not in automatic:continue
    row,path=automatic[k]
    if row.get('prior_proposal_sha256')or row['proposed_xml']!=d['proposed_xml']:continue
    cch.append((k,path))
    if len(cch)==8:break
assert len(cu)==24 and len(cch)==8
rows=[];selected=[]
for k,path in cu+cch:
    x=dict(c.execute('SELECT * FROM articles WHERE code_id=? AND id=?',k).fetchone())
    d=dict(c.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',k).fetchone())
    raw=c.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",k).fetchone()[0]
    raw=raw.decode()if isinstance(raw,bytes)else raw
    x['source_id']=x.pop('id');x['source_xml']=x.pop('content_xml')
    x['source_document_xml']=raw;x['source_notes_xml']=source_notes(c,*k)
    x['previous_draft']=d;x['batch_path']=path
    assert H(raw)==x['source_sha256'];rows.append(x)
    selected.append(dict(code_id=k[0],source_id=k[1],number=x['number'],source_sha256=x['source_sha256'],source_body_sha256=H(x['source_xml']),notes_sha256=H(x['source_notes_xml']),proposed_sha256=H(d['proposed_xml']),batch_path=path))
c.rollback();c.close()
for name in ['policy-coordinations.json','site-summaries.json']:(P/name).write_bytes((B/name).read_bytes())
(P/'source.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
manifest=dict(captured_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),sqlite_access='mode=ro; BEGIN, one snapshot for32 selected source/draft/note/document records',method='24CU rows by automatic-batch modification order (first15 eligible from00001, then9 from00046), plus8CCH rows by descending draft rowid; matching automatic-batch body required; exclude every key in nonautomatic numeric batches and every row carrying prior_proposal_sha256',limitations='Modification times and rowids are not an absolute chronology of first acceptance. Nine rows of CU00001 already carry prior_proposal_sha256 and are excluded. This is a bounded useful sample, not a globally latest32 assertion.',count=32,excluded_manual_keys=len(manual),policy_sha256={n:H((P/n).read_bytes())for n in ['policy-coordinations.json','site-summaries.json']},articles=selected)
(P/'selection-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([dict(number=x['number'],source_id=x['source_id'],batch_path=x['batch_path'])for x in rows],ensure_ascii=False,indent=2))
