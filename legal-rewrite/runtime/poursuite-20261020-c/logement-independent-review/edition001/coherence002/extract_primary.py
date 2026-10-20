from pathlib import Path
import tarfile,gzip,json,hashlib,xml.etree.ElementTree as E
O=Path(__file__).resolve().parent;B=O.parents[4];OUT=O/'primary';OUT.mkdir(exist_ok=True)
families={'LEGITEXT000025024948':'cpce','JORFTEXT000025009816':'ordonnance2011','JORFTEXT000000172847':'loi1991','LEGITEXT000037701019':'commande'}
# Copier seulement des normes utiles, dans un dossier documentaire isolé.
nums={'cpce':{'L111-1','L111-2','L111-3','L111-4'},'ordonnance2011':{'1','2','4','6'},'loi1991':{'3'},'commande':{'L1','L2','L3','L6','L1110-1','L1111-1','L1211-1','L2124-1','R2431-36','R2431-37'}}
manifest=json.loads((B/'archive-manifest.json').read_text());records={};archives=[]
class HashReader:
 def __init__(self,f):self.f=f;self.h=hashlib.sha256()
 def read(self,n=-1):
  b=self.f.read(n);self.h.update(b);return b
 def seekable(self):return False
 def tell(self):return self.f.tell()
for i,item in enumerate(manifest):
 name=item['name'];path=Path('/private/tmp/legi-global-20250713.tar.gz')if name.startswith('Freemium')else Path('/private/tmp/legi-updates')/name
 count=0
 with path.open('rb')as f:
  reader=HashReader(f)
  with gzip.GzipFile(fileobj=reader,mode='rb')as gz:
   with tarfile.open(fileobj=gz,mode='r|')as tar:
    for m in tar:
     if not m.isfile()or not m.name.endswith('.xml'):continue
     fam=next((v for k,v in families.items()if k in m.name.split('/')),None)
     if not fam:continue
     raw=tar.extractfile(m).read();r=E.fromstring(raw);num=r.findtext('META/META_SPEC/META_ARTICLE/NUM');ident=r.findtext('META/META_COMMUN/ID')or Path(m.name).stem
     if r.tag!='ARTICLE'or num not in nums[fam]:continue
     q=OUT/fam/(ident+'.xml');q.parent.mkdir(exist_ok=True)
     if q.exists()and q.read_bytes()!=raw:
      old=q.parent/'previous';old.mkdir(exist_ok=True);(old/(ident+'-'+hashlib.sha256(q.read_bytes()).hexdigest()[:12]+'.xml')).write_bytes(q.read_bytes())
     q.write_bytes(raw);records[fam+'|'+ident]={'family':fam,'id':ident,'number':num,'state':r.findtext('META/META_SPEC/META_ARTICLE/ETAT'),'valid_from':r.findtext('META/META_SPEC/META_ARTICLE/DATE_DEBUT'),'valid_until':r.findtext('META/META_SPEC/META_ARTICLE/DATE_FIN'),'path':str(q.relative_to(O)),'sha256':hashlib.sha256(raw).hexdigest(),'archive':name,'member':m.name,'url':'https://www.legifrance.gouv.fr/codes/article_lc/'+ident};count+=1
   while gz.read(1024*1024):pass
  digest=reader.h.hexdigest()
 archives.append({'name':name,'sha256':digest,'source_url':item.get('url')or item.get('source_url'),'documents_saved':count})
 if i%40==0 or i==len(manifest)-1:print('archives',i+1,'/',len(manifest),'records',len(records),flush=True)
(O/'primary-records.json').write_text(json.dumps(list(records.values()),ensure_ascii=False,indent=2)+'\n');(O/'primary-archives.json').write_text(json.dumps(archives,ensure_ascii=False,indent=2)+'\n');print('DONE',len(records),flush=True)
