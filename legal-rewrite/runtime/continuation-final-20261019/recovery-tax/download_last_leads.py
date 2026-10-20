import pathlib, urllib.request, urllib.error,json,hashlib,concurrent.futures
P=pathlib.Path(__file__).parent
urls=[('dalloz-coupons','https://www.dalloz.fr/documentation/Document?FromId=CODES_SECS_CGIM_TALPHA&id=CODE_CGIM_ANNE_4_ARTI_14'),('bofip-documents-coupons','https://bofip-archives.impots.gouv.fr/bofip/27494-AIDA.html/identifiant=4J1342-19951101')]
def get(v):
 name,url=v
 try:r=urllib.request.urlopen(url,timeout=20); data=r.read(); status=r.status;typ=r.headers.get('Content-Type','')
 except urllib.error.HTTPError as e:data=e.read();status=e.code;typ=e.headers.get('Content-Type','')
 except Exception as e:return {'url':url,'error':str(e)}
 path=P/(name+'.html');path.write_bytes(data);return {'url':url,'status':status,'content_type':typ,'path':str(path),'sha256':hashlib.sha256(data).hexdigest(),'length':len(data)}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:out=list(ex.map(get,urls))
(P/'last-lead-download-attempts.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False))
