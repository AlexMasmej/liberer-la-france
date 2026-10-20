"""Documentary edges only: no inference that an entire descendant is an SRU norm."""
import sqlite3,zlib,xml.etree.ElementTree as E,json,hashlib
from pathlib import Path
P=Path(__file__).parent
c=sqlite3.connect('file:'+str(P/'external-evidence.sqlite')+'?mode=ro',uri=True);c.row_factory=sqlite3.Row
loti='JORFTEXT000000319738';sru='JORFTEXT000000207538'
edges=[];ord_ids={}
for a in c.execute("select * from documents where kind='ARTICLE' and start<=? and end>? and state!='ABROGE'",('2026-10-19','2026-10-19')):
 raw=zlib.decompress(a['xml_zlib']);r=E.fromstring(raw);ls=[]
 for e in r.findall('.//LIEN'):
  if e.get('sens')=='source' and e.get('typelien')=='CONCORDANCE' and (e.get('cidtexte') in [loti,sru] or '59-151' in (e.text or '') or '75-534' in (e.text or '') or '82-684' in (e.text or '') or '73-1193' in (e.text or '')):
   ls.append(dict(e.attrib,text=(e.text or '').strip()))
  elif e.get('cidtexte')==sru and e.get('typelien') in ['MODIFIE','MODIFICATION','CREATION','CREE','CONCORDANCE']:
   ls.append(dict(e.attrib,text=(e.text or '').strip()))
 if ls:
  edges.append({'code_id':a['code_id'],'number':a['number'],'source_id':a['id'],'source_sha256':a['sha256'],'valid_from':a['start'],'valid_until':a['end'],'archive':a['archive'],'archive_member':a['member'],'relations':ls,'semantic_retention_verified':False})
out={'as_of':'2026-10-19','archive_count':467,'source':'Official DILA stock and 466 daily updates; raw XML and SHA in external-evidence.sqlite','warning':'Documentary CONCORDANCE/MODIFIE edges only. No article is a verified repeal target until its initial SRU provision and subsequent autonomous modifications have been compared in full. A concordance with LOTI does not show that SRU created that entire LOTI article.','records':edges}
t=P/'external-current-lineage.json.tmp';t.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');t.replace(P/'external-current-lineage.json')
print('external current documentary records',len(edges))
