import concurrent.futures,pathlib,urllib.request,urllib.error,json,hashlib
P=pathlib.Path(__file__).parent
urls=[('jo-20101231-integral','https://www.legifrance.gouv.fr/download/pdf?id=63svbPxxA_9vv0UbiiKxBU1tUE4pff_NWtPY0T-2KIM%3D'),('bofip-ptz-current','https://bofip.impots.gouv.fr/export/pdf/314646'),('bofip-archive-coupons-1995','https://bofip-archives.impots.gouv.fr/bofip/27444-AIDA.html/identifiant=4J1-19951101')]
def get(v):
 name,url=v
 try:
  r=urllib.request.urlopen(url,timeout=25);data=r.read();status=r.status;typ=r.headers.get('Content-Type','')
 except urllib.error.HTTPError as e:data=e.read();status=e.code;typ=e.headers.get('Content-Type','')
 except Exception as e:return {'url':url,'error':str(e)}
 path=P/(name+('.pdf' if data.startswith(b'%PDF') else '.html'));path.write_bytes(data);return {'url':url,'status':status,'content_type':typ,'path':str(path),'sha256':hashlib.sha256(data).hexdigest(),'length':len(data)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:records=list(ex.map(get,urls))
(P/'source-download-attempts.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
for r in records:print(r)
