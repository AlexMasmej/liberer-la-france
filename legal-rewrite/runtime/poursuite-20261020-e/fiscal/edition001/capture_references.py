from pathlib import Path
from datetime import datetime,timezone
import sqlite3,json,hashlib,sys
P=Path(__file__).resolve().parent;B=P.parents[3];sys.path.insert(0,str(B));from ingest import source_notes
H=lambda v:hashlib.sha256(v if isinstance(v,bytes)else(v or'').encode()).hexdigest()
nums={'impots':['1402','635','647','658','677','664','1701','1704','1837','1840 B','1840 C','1840 D','1729','1754','886','887','890','891'], 'impots-annexe-3':['253','255','256','257']}
d=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);d.row_factory=sqlite3.Row;d.execute('BEGIN');out=[];missing=[]
for slug,wanted in nums.items():
 by={x['number']:x for x in json.loads((B/f'runtime/export-source/{slug}.json').read_text())}
 for n in wanted:
  if n not in by:missing.append([slug,n]);continue
  x=by[n];k=x['code_id'],x['source_id'];s=d.execute('SELECT * FROM articles WHERE code_id=? AND id=?',k).fetchone();r=d.execute("SELECT xml,sha256 FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",k).fetchone();old=d.execute('SELECT * FROM drafts WHERE code_id=? AND source_id=?',k).fetchone();raw=r['xml'].decode()if isinstance(r['xml'],bytes)else r['xml'];assert H(raw)==s['source_sha256']==r['sha256']
  a=dict(slug=slug,code_id=k[0],source_id=k[1],number=n,source_xml=s['content_xml'],source_notes_xml=source_notes(d,*k),source_sha256=s['source_sha256'],source_document_xml=raw,source_document_sha256=H(raw),source_url='https://www.legifrance.gouv.fr/codes/article_lc/'+k[1],source_archive=s['archive'],previous_draft=dict(old)if old else None)
  out.append(a)
d.rollback();d.close();(P/'references.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');(P/'missing-canonical-reference-numbers.json').write_text(json.dumps(missing,ensure_ascii=False,indent=2)+'\n');print(len(out),missing)
