from pathlib import Path
import gzip,tarfile,hashlib,json,re,xml.etree.ElementTree as E
H=Path(__file__).resolve().parent;B=H.parents[2]
owners={'JORFTEXT000046845631':{'55'},'JORFTEXT000048727345':{'79'},'JORFTEXT000051168007':{'62'},'LEGITEXT000006069583':None,'LEGITEXT000005634379':None,'JORFTEXT000053091516':{'10','49'}}
manifest=json.loads((B/'archive-manifest.json').read_text());records={}
def save(raw,name,item):
 owner=next((s for s in name.split('/')if s in owners),None)
 if not owner:return
 n=E.fromstring(raw)
 if n.tag!='ARTICLE':return
 num=n.findtext('META/META_SPEC/META_ARTICLE/NUM')
 keep=num in owners[owner] if owners[owner] is not None else (bool(re.search(rb'valeur ajout\xc3\xa9e des entreprises|1586|1679 septies|L711-16',raw))or num in {'L173','L174','L265','L711-16'})
 if not keep:return
 def body(path):
  e=n.find(path);return (e.text or '')+''.join(E.tostring(c,encoding='unicode')for c in e)if e is not None else''
 identifier=n.findtext('META/META_COMMUN/ID');meta='META/META_SPEC/META_ARTICLE/'
 records[owner,identifier]={'code_id':owner,'source_id':identifier,'number':num,'valid_from':n.findtext(meta+'DATE_DEBUT'),'valid_until':n.findtext(meta+'DATE_FIN'),'state':n.findtext(meta+'ETAT'),'source_xml':body('BLOC_TEXTUEL/CONTENU'),'source_notes_xml':body('NOTA/CONTENU'),'source_document_xml':raw.decode(),'source_sha256':hashlib.sha256(raw).hexdigest(),'source_body_sha256':hashlib.sha256(body('BLOC_TEXTUEL/CONTENU').encode()).hexdigest(),'archive':item['name'],'archive_member':name,'archive_source_url':item['url'],'source_url':'https://www.legifrance.gouv.fr/'+('codes'if owner.startswith('LEGITEXT')else'loda')+'/article_lc/'+identifier}
def output(path,archive_count):
 data={'as_of':'2026-10-19','archives_replayed':archive_count,'scope':{k:sorted(v)if v is not None else None for k,v in owners.items()},'articles':list(records.values()),'archive_manifest_sha256':hashlib.sha256((B/'archive-manifest.json').read_bytes()).hexdigest()}
 (H/path).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
for p in (H/'raw-stock').rglob('*.xml'):
 if '/article/'not in str(p):continue
 save(p.read_bytes(),str(p.relative_to(H/'raw-stock')),manifest[0])
print('STOCK',len(records),flush=True);output('checkpoint.json',1)
for i,item in enumerate(manifest[1:]):
 p=Path('/private/tmp/legi-updates')/item['name']
 with gzip.open(p,'rb')as gz:
  with tarfile.open(fileobj=gz,mode='r|')as tar:
   for m in tar:
    if not m.isfile()or '/article/'not in m.name or not m.name.endswith('.xml')or not any(o in m.name for o in owners):continue
    save(tar.extractfile(m).read(),m.name,item)
  while gz.read(1048576):pass
 if i%25==0:print('updates',i+1,'records',len(records),flush=True);output('checkpoint.json',i+2)
output('source-versions.json',len(manifest));print('DONE',len(records),flush=True)
