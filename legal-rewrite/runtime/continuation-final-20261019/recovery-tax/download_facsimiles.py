import pathlib,urllib.request,urllib.error,json,hashlib,concurrent.futures
P=pathlib.Path(__file__).parent
urls=[('copy-ptz-jo-20101231','https://www.fichier-pdf.fr/2011/09/23/ptz-journal-officiel/ptz-journal-officiel.pdf'),('copy-arrete-20110525-ptz','https://www.moneyvox.fr/r/arrete-20110525-ptz.pdf'),('copy-decret-2010-1704','https://www.moneyvox.fr/r/decret-2010-1704-ptz.pdf')]
def get(v):
 name,url=v
 try:r=urllib.request.urlopen(url,timeout=20);data=r.read();status=r.status;typ=r.headers.get('Content-Type','')
 except urllib.error.HTTPError as e:data=e.read();status=e.code;typ=e.headers.get('Content-Type','')
 except Exception as e:return {'url':url,'error':str(e)}
 path=P/(name+('.pdf' if data.startswith(b'%PDF') else '.html'));path.write_bytes(data);return {'url':url,'status':status,'content_type':typ,'path':str(path),'sha256':hashlib.sha256(data).hexdigest(),'length':len(data),'authentication_jo_verified':False}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:records=list(ex.map(get,urls))
(P/'facsimile-download-attempts.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
for r in records:print(r)
