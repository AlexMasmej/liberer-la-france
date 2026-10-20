import concurrent.futures,pathlib,urllib.request,urllib.error,json,hashlib
P=pathlib.Path(__file__).parent
urls=[('sgfgas-home','https://www2.sgfgas.fr/'),('convention-ptz-2011','https://www.legifrance.gouv.fr/loda/id/JORFTEXT000024113794/2026-03-10'),('annexe-iv-15-current','https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000019493914/2026-02-24')]
def get(v):
 name,url=v
 try:r=urllib.request.urlopen(url,timeout=20);data=r.read();status=r.status;typ=r.headers.get('Content-Type','');final=r.url
 except urllib.error.HTTPError as e:data=e.read();status=e.code;typ=e.headers.get('Content-Type','');final=e.url
 except Exception as e:return {'url':url,'error':str(e)}
 path=P/(name+('.pdf' if data.startswith(b'%PDF') else '.html'));path.write_bytes(data);return {'url':url,'final_url':final,'status':status,'content_type':typ,'path':str(path),'sha256':hashlib.sha256(data).hexdigest(),'length':len(data)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:records=list(ex.map(get,urls))
(P/'lead-download-attempts.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
for r in records:print(r)
