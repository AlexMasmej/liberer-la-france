import tarfile,pathlib,hashlib,json,xml.etree.ElementTree as E
P=pathlib.Path(__file__).parent
ids={'LEGITEXT000005630252','LEGITEXT000006069108','LEGITEXT000006068256','LEGITEXT000006070721'}
rows=[];count=0
with tarfile.open('/private/tmp/legi-global-20250713.tar.gz','r|gz') as tar:
 for m in tar:
  count+=1
  if not m.isfile() or not m.name.endswith('.xml'):continue
  hit=next((x for x in ids if x in m.name.split('/')),None)
  if not hit:continue
  raw=tar.extractfile(m).read();root=E.fromstring(raw);identifier=root.findtext('META/META_COMMUN/ID') or root.findtext('ID') or pathlib.PurePosixPath(m.name).stem
  q=P/hit/(identifier+'.xml');q.parent.mkdir(exist_ok=True);q.write_bytes(raw)
  rows.append({'code_id':hit,'id':identifier,'kind':root.tag,'member':m.name,'path':str(q),'sha256':hashlib.sha256(raw).hexdigest()})
(P/'dila-extraction.json').write_text(json.dumps({'archive':'/private/tmp/legi-global-20250713.tar.gz','archive_source_url':'https://echanges.dila.gouv.fr/OPENDATA/LEGI/Freemium_legi_global_20250713-140000.tar.gz','snapshot_date':'2025-07-13','not_verified_current_to_2026_10_19':True,'documents':rows},ensure_ascii=False,indent=2))
print('members inspected',count,'documents retained',len(rows))
