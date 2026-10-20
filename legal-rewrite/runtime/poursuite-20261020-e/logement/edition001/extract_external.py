from pathlib import Path
import tarfile,xml.etree.ElementTree as E,hashlib,json
O=Path(__file__).resolve().parent;archive=Path('/private/tmp/legi-global-20250713.tar.gz');wanted={'LEGITEXT000006070633':{'L1617-5','R2342-4'},'LEGITEXT000031366350':{'L112-3','R112-5','R112-6','L112-6'}};out=[]
with tarfile.open(archive,'r|gz')as t:
 for m in t:
  if not m.isfile()or'/article/'not in m.name:continue
  code=next((c for c in wanted if '/'+c+'/'in m.name),None)
  if not code:continue
  raw=t.extractfile(m).read();r=E.fromstring(raw);n=r.findtext('./META/META_SPEC/META_ARTICLE/NUM');end=r.findtext('./META/META_SPEC/META_ARTICLE/DATE_FIN')
  if n not in wanted[code]or end!='2999-01-01':continue
  out.append({'code_id':code,'number':n,'source_id':r.findtext('./META/META_COMMUN/ID'),'source_document_xml':raw.decode(),'sha256':hashlib.sha256(raw).hexdigest(),'archive':str(archive),'member':m.name,'source_url':'https://echanges.dila.gouv.fr/OPENDATA/LEGI/Freemium_legi_global_20250713-140000.tar.gz','snapshot_date':'2025-07-13','raw_2026_updates_replayed':False})
(O/'external-baseline-references.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print([(x['number'],x['source_id'])for x in out])
