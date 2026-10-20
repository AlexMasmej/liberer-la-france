from pathlib import Path
import json,gzip,tarfile,xml.etree.ElementTree as ET,hashlib,re
O=Path(__file__).resolve().parent;B=O.parents[3];manifest=json.loads((B/'archive-manifest.json').read_text());records={};scanned=[]
NUMS={'L6352-1','R6352-1','R6352-2','R6352-3','R6352-4','R6352-5','R6352-6','R244-1'};CODES={'LEGITEXT000023086525','LEGITEXT000006074234'}
for index,item in enumerate(manifest):
 p=Path('/private/tmp/legi-global-20250713.tar.gz') if item['name'].startswith('Freemium') else Path('/private/tmp/legi-updates')/item['name']
 with gzip.open(p,'rb') as gz:
  with tarfile.open(fileobj=gz,mode='r|') as ar:
   for m in ar:
    if not m.isfile() or not m.name.endswith('.xml'):continue
    code=next((s for s in m.name.split('/') if s in CODES),None)
    if not code:continue
    raw=ar.extractfile(m).read()
    if not any(n.encode() in raw for n in NUMS):continue
    n=ET.fromstring(raw)
    if n.tag!='ARTICLE':continue
    num=n.findtext('META/META_SPEC/META_ARTICLE/NUM');num=re.sub(r'[^A-Za-z0-9-]','',num or '')
    if num not in NUMS:continue
    sid=n.findtext('META/META_COMMUN/ID');start=n.findtext('META/META_SPEC/META_ARTICLE/DATE_DEBUT');end=n.findtext('META/META_SPEC/META_ARTICLE/DATE_FIN');el=n.find('BLOC_TEXTUEL/CONTENU');nota=n.find('NOTA/CONTENU');inner=lambda el:'' if el is None else (el.text or '')+''.join(ET.tostring(c,encoding='unicode')for c in el)
    records[code+'|'+sid]={'code_id':code,'source_id':sid,'number':num,'valid_from':start,'valid_until':end,'state':n.findtext('META/META_SPEC/META_ARTICLE/ETAT'),'source_xml':inner(el),'source_notes_xml':inner(nota),'source_document_xml':raw.decode(),'source_sha256':hashlib.sha256(raw).hexdigest(),'archive':item['name'],'archive_source_url':item.get('url')or item.get('source_url'),'archive_sha256':item.get('sha256'),'member':m.name}
  while gz.read(1024*1024):pass
 scanned.append(item['name'])
 if index%100==0:print(index+1,'archives',len(records),'records',flush=True)
(O/'aviation-official-sources.json').write_text(json.dumps({'as_of':'2026-10-20','archives_scanned':scanned,'records':list(records.values()),'canonical_mutation':False},ensure_ascii=False,indent=2)+'\n');print('COMPLETE',len(records),flush=True)
