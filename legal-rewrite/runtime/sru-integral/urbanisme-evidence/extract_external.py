from pathlib import Path
import json,sqlite3,tarfile,gzip,hashlib,zlib,xml.etree.ElementTree as E,time
P=Path(__file__).resolve().parent;ROOT=P.parents[2]
ids={'LEGITEXT000023086525','LEGITEXT000006070633','LEGITEXT000023983208','LEGITEXT000006074236','LEGITEXT000006074220','LEGITEXT000006071367','LEGITEXT000022197698','LEGITEXT000006071366','LEGITEXT000006070299','LEGITEXT000006070208','LEGITEXT000005634379','LEGITEXT000006070667','LEGITEXT000006070933','LEGITEXT000006069583'}
# Our own documentary copy only; canonical corpus and sources/ remain read-only.
db=sqlite3.connect(P/'external-evidence.sqlite');db.execute('pragma journal_mode=WAL')
db.execute('create table if not exists documents(code_id text,id text,kind text,number text,start text,end text,state text,xml_zlib blob,sha256 text,archive text,member text,primary key(code_id,id,kind))')
db.execute('create table if not exists archives(name text primary key,sha256 text,source_url text,complete integer,documents integer)')
canon=sqlite3.connect('file:'+str(ROOT/'corpus.sqlite')+'?mode=ro',uri=True);expected={r[0]:r[1] for r in canon.execute('select name,sha256 from archives where complete=1')};canon.close()
manifest=json.loads((ROOT/'archive-manifest.json').read_text());already={r[0] for r in db.execute('select name from archives where complete=1')}
class Hasher:
 def __init__(self,f):self.f=f;self.h=hashlib.sha256()
 def read(self,n=-1):
  b=self.f.read(n);self.h.update(b);return b
 def seekable(self):return False
 def tell(self):return self.f.tell()
for i,item in enumerate(manifest):
 name=item['name']
 if name in already:continue
 path=Path('/private/tmp/legi-global-20250713.tar.gz') if name.startswith('Freemium') else Path('/private/tmp/legi-updates')/name
 if not path.is_file():raise FileNotFoundError(path)
 count=0;db.execute('BEGIN')
 with path.open('rb') as file:
  reader=Hasher(file)
  with gzip.GzipFile(fileobj=reader,mode='rb') as gz:
   with tarfile.open(fileobj=gz,mode='r|') as tar:
    for m in tar:
     if not m.isfile() or not m.name.endswith('.xml'):continue
     code=next((x for x in m.name.split('/') if x in ids),None)
     if not code:continue
     raw=tar.extractfile(m).read()
     if b'<!DOCTYPE' in raw or b'<!ENTITY' in raw:raise ValueError('Unsupported entities')
     r=E.fromstring(raw);identifier=r.findtext('META/META_COMMUN/ID') or r.findtext('ID') or Path(m.name).stem
     meta='META/META_SPEC/META_ARTICLE/'
     db.execute('insert into documents values(?,?,?,?,?,?,?,?,?,?,?) on conflict(code_id,id,kind) do update set number=excluded.number,start=excluded.start,end=excluded.end,state=excluded.state,xml_zlib=excluded.xml_zlib,sha256=excluded.sha256,archive=excluded.archive,member=excluded.member',(code,identifier,r.tag,r.findtext(meta+'NUM'),r.findtext(meta+'DATE_DEBUT'),r.findtext(meta+'DATE_FIN'),r.findtext(meta+'ETAT'),zlib.compress(raw),hashlib.sha256(raw).hexdigest(),name,m.name));count+=1
   while gz.read(1024*1024):pass
  digest=reader.h.hexdigest()
 if name in expected and digest!=expected[name]:db.rollback();raise ValueError('Archive SHA mismatch '+name)
 db.execute('insert into archives values(?,?,?,?,?)',(name,digest,item.get('url')or item.get('source_url'),1,count));db.commit()
 if i%25==0 or i==len(manifest)-1:print('archives',i+1,'/',len(manifest),'documents latest archive',count,flush=True)
status={'archive_count':db.execute('select count(*) from archives where complete=1').fetchone()[0],'last_archive':manifest[-1]['name'],'official_source':'https://echanges.dila.gouv.fr/OPENDATA/LEGI/','codes':sorted(ids),'as_of':'2026-10-19','database':'external-evidence.sqlite','xml_compression':'zlib; raw document SHA256 stored separately','canonical_database_modified':False,'sources_modified':False,'new_candidates_registered':False}
t=P/'external-evidence-status.json.tmp';t.write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n');t.replace(P/'external-evidence-status.json')
print(json.dumps(status,ensure_ascii=False),flush=True)
