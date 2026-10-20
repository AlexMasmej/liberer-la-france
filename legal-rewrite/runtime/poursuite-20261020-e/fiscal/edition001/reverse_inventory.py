from pathlib import Path
import json,re,sqlite3,sys,hashlib
P=Path(__file__).resolve().parent;B=P.parents[3];sys.path.insert(0,str(B));from ingest import source_notes
H=lambda v:hashlib.sha256(v if isinstance(v,bytes)else(v or'').encode()).hexdigest()
pat=re.compile(r'(?<![\dA-Za-z])(?:849|853|855|856|860|873|886|889)(?![\dA-Za-z])',re.I)
d=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);d.row_factory=sqlite3.Row;d.execute('BEGIN');out=[];canon=0
for file in sorted((B/'runtime/export-source').glob('*.json')):
 if file.stem.endswith('-structure')or file.stem=='coverage':continue
 inventory=json.loads(file.read_text())
 if not isinstance(inventory,list):continue
 for entry in inventory:
  if not isinstance(entry,dict)or'code_id'not in entry:continue
  canon+=1;k=entry['code_id'],entry['source_id'];s=d.execute('SELECT * FROM articles WHERE code_id=? AND id=?',k).fetchone();pr=d.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',k).fetchone();notes=source_notes(d,*k);contexts=[]
  for field,value in [('source_xml',s['content_xml']),('source_notes_xml',notes),('previous_proposed_xml',pr['proposed_xml']if pr else'')]:
   for m in pat.finditer(value or''):
    contexts.append(dict(field=field,matched=m.group(),context=value[max(0,m.start()-140):m.end()+180]))
  if not contexts:continue
  raw=d.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",k).fetchone()[0];raw=raw.decode()if isinstance(raw,bytes)else raw
  out.append(dict(slug=file.stem,code_id=k[0],source_id=k[1],number=s['number'],source_sha256=s['source_sha256'],source_xml=s['content_xml'],source_notes_xml=notes,source_document_xml=raw,source_document_sha256=H(raw),previous_draft=dict(pr)if pr else None,matched_contexts=contexts))
d.rollback();d.close();(P/'reverse-reference-captures.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print('canonical',canon,'hits',len(out))
for x in out:print(x['slug'],x['number'],x['source_id'],sorted(set(v['matched']for v in x['matched_contexts'])))
