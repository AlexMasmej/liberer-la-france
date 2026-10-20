from pathlib import Path
import sqlite3,json,hashlib,sys,xml.etree.ElementTree as ET
P=Path(__file__).resolve().parent;B=P.parents[3];sys.path.insert(0,str(B));from ingest import source_notes
H=lambda v:hashlib.sha256(v if isinstance(v,bytes)else(v or'').encode()).hexdigest()
d=sqlite3.connect('file:'+str(B/'corpus.sqlite')+'?mode=ro',uri=True);d.row_factory=sqlite3.Row;d.execute('BEGIN');out=[]
for sid in ['LEGIARTI000006299197','LEGIARTI000006297146']:
 code='LEGITEXT000006069574';s=dict(d.execute('SELECT * FROM articles WHERE code_id=? AND id=?',(code,sid)).fetchone());raw=d.execute("SELECT xml,sha256 FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'",(code,sid)).fetchone();body=raw[0].decode()if isinstance(raw[0],bytes)else raw[0];assert H(body)==s['source_sha256']==raw['sha256'];root=ET.fromstring(body)
 out.append(dict(code_id=code,source_id=sid,number=s['number'],source_xml=s['content_xml'],source_notes_xml=source_notes(d,code,sid),source_sha256=s['source_sha256'],source_document_xml=body,source_document_sha256=H(body),valid_from=s['valid_from'],valid_until=s['valid_until'],state=s['state'],modifying_links=[dict(x.attrib)for x in root.findall('./LIENS/LIEN')],source_url='https://www.legifrance.gouv.fr/codes/article_lc/'+sid,historical_outside_canonical_inventory=True,not_a_new_draft_or_suppression=True))
d.rollback();d.close();(P/'historical-annexe-references.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
for a in out:print(a['number'],a['valid_until'],a['modifying_links'])
