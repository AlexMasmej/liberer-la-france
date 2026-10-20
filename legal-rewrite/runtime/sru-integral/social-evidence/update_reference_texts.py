import tarfile,pathlib,hashlib,json,xml.etree.ElementTree as E
P=pathlib.Path(__file__).parent
ids={'JORFTEXT000000207538','JORFTEXT000000509310','JORFTEXT000000880200','LEGITEXT000006070721'}
rows=[];archives=sorted(pathlib.Path('/private/tmp/legi-updates').glob('*.tar.gz'))
for i,archive in enumerate(archives):
 with tarfile.open(archive,'r|gz') as tar:
  for m in tar:
   if not m.isfile() or not m.name.endswith('.xml'):continue
   hit=next((x for x in ids if x in m.name.split('/')),None)
   if not hit:continue
   raw=tar.extractfile(m).read();root=E.fromstring(raw);identifier=root.findtext('META/META_COMMUN/ID') or root.findtext('ID') or pathlib.PurePosixPath(m.name).stem
   # Preserve the baseline document separately; no reference source is lost.
   q=P/hit/(identifier+'.xml');q.parent.mkdir(exist_ok=True)
   if q.exists() and q.read_bytes()!=raw:
    b=P/'baseline'/hit/(identifier+'.xml');b.parent.mkdir(parents=True,exist_ok=True)
    if not b.exists():b.write_bytes(q.read_bytes())
   q.write_bytes(raw)
   rows.append({'text_id':hit,'id':identifier,'kind':root.tag,'member':m.name,'path':str(q),'sha256':hashlib.sha256(raw).hexdigest(),'archive':archive.name,'source_url':'https://echanges.dila.gouv.fr/OPENDATA/LEGI/'+archive.name})
 if (i+1)%100==0:print('archives',i+1,'updated documents',len(rows),flush=True)
(P/'dila-updates.json').write_text(json.dumps({'last_archive':archives[-1].name,'archive_count':len(archives),'documents':rows},ensure_ascii=False,indent=2)+'\n')
print('complete',len(archives),'archives;',len(rows),'documents')
