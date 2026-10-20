import sqlite3,json,hashlib,xml.etree.ElementTree as E
from pathlib import Path
H=Path(__file__).resolve().parent
c=sqlite3.connect('file:legal-rewrite/corpus.sqlite?mode=ro',uri=True);c.row_factory=sqlite3.Row
rows=[]
ns=['1447-0','1586 ter','1586 quater','1586 quinquies','1586 sexies','1586 septies','1586 octies','1586 nonies','1679 septies','1600','1647 B sexies','1647 B sexies A','1681 septies','1649 quater B quater']
for a in c.execute('select * from articles where code_id=? and valid_from>"2026-10-19" order by number,valid_from',('LEGITEXT000006069577',)):
 if a['number']not in ns:continue
 a=dict(a);d=dict(c.execute('select * from documents where code_id=? and id=? and kind="ARTICLE"',(a['code_id'],a['id'])).fetchone());raw=d['xml'].decode()if isinstance(d['xml'],bytes)else d['xml'];n=E.fromstring(raw);no=n.find('NOTA/CONTENU');note=(no.text or '')+''.join(E.tostring(ch,encoding='unicode')for ch in no)if no is not None else''
 rows.append({'code_id':a['code_id'],'source_id':a['id'],'number':a['number'],'valid_from':a['valid_from'],'valid_until':a['valid_until'],'state':a['state'],'source_xml':a['content_xml'],'source_notes_xml':note,'source_document_xml':raw,'source_sha256':a['source_sha256'],'source_body_sha256':hashlib.sha256(a['content_xml'].encode()).hexdigest(),'archive':a['archive'],'source_url':'https://www.legifrance.gouv.fr/codes/article_lc/'+a['id']})
(H/'all-future-code-support.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print('DONE',len(rows),flush=True)
for r in rows:print(r['number'],r['source_id'],r['valid_from'],len(r['source_xml']))
