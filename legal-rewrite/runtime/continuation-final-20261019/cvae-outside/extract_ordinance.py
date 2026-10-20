from pathlib import Path
import gzip,tarfile,hashlib,json,re,xml.etree.ElementTree as E
H=Path(__file__).resolve().parent;B=H.parents[2]
owners={'JORFTEXT000053091516':{'10','49'}}
manifest=json.loads((B/'archive-manifest.json').read_text());records={};audit=[]
for i,item in enumerate([m for m in manifest if m['name'].startswith('LEGI_2026') or m['name'].startswith('LEGI_202512')]):
 p=Path('/private/tmp/legi-global-20250713.tar.gz') if item['name'].startswith('Freemium') else Path('/private/tmp/legi-updates')/item['name']
 with gzip.open(p,'rb')as gz:
  with tarfile.open(fileobj=gz,mode='r|')as tar:
   for m in tar:
    if not m.isfile() or '/article/' not in m.name or not m.name.endswith('.xml'):continue
    owner=next((s for s in m.name.split('/')if s in owners),None)
    if not owner:continue
    raw=tar.extractfile(m).read();n=E.fromstring(raw);num=n.findtext('META/META_SPEC/META_ARTICLE/NUM')
    keep=num in owners[owner] if owners[owner] is not None else (bool(re.search(rb'valeur ajout\xc3\xa9e des entreprises|1586|1679 septies|L711-16',raw))or num in {'L173','L174','L265','L711-16'})
    if not keep:continue
    def body(path):
     e=n.find(path);return (e.text or '')+''.join(E.tostring(c,encoding='unicode')for c in e)if e is not None else ''
    identifier=n.findtext('META/META_COMMUN/ID');meta='META/META_SPEC/META_ARTICLE/'
    records[(owner,identifier)]={'code_id':owner,'source_id':identifier,'number':num,'valid_from':n.findtext(meta+'DATE_DEBUT'),'valid_until':n.findtext(meta+'DATE_FIN'),'state':n.findtext(meta+'ETAT'),'source_xml':body('BLOC_TEXTUEL/CONTENU'),'source_notes_xml':body('NOTA/CONTENU'),'source_document_xml':raw.decode(),'source_sha256':hashlib.sha256(raw).hexdigest(),'source_body_sha256':hashlib.sha256(body('BLOC_TEXTUEL/CONTENU').encode()).hexdigest(),'archive':item['name'],'archive_member':m.name,'archive_source_url':item['url'],'source_url':'https://www.legifrance.gouv.fr/'+('codes'if owner.startswith('LEGITEXT')else'loda')+'/article_lc/'+identifier}
  while gz.read(1048576):pass
 audit.append(item)
 if i%50==0:print('archives',i+1,'records',len(records),flush=True)
result={'as_of':'2026-10-19','archives_replayed':len(audit),'scope':{k:sorted(v)if v is not None else None for k,v in owners.items()},'articles':list(records.values()),'archive_manifest_sha256':hashlib.sha256((B/'archive-manifest.json').read_bytes()).hexdigest()}
(H/'ordinance-source-versions.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('DONE',len(records),flush=True)
