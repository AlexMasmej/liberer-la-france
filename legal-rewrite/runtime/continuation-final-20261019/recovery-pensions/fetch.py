from pathlib import Path
import concurrent.futures,hashlib,json,urllib.request
root=Path(__file__).parent
jobs=[('cnav-css-D351-9.json','https://legislation.lassuranceretraite.fr/api/v1/reference/referencesByFileLeafRef/LO_CSS_D351-9.aspx'),('cnav-decret-2003-1376.json','https://legislation.lassuranceretraite.fr/api/v1/reference/referencesByFileLeafRef/DEC_20031376_31122003.aspx'),('cnav-decret-2010-1737.json','https://legislation.lassuranceretraite.fr/api/v1/reference/referencesByFileLeafRef/DEC_20101737_30122010.aspx'),('cnav-css-D653-4.json','https://legislation.lassuranceretraite.fr/api/v1/reference/referencesByFileLeafRef/LO_CSS_D653-4.aspx'),('cnav-css-D643-7.json','https://legislation.lassuranceretraite.fr/api/v1/reference/referencesByFileLeafRef/LO_CSS_D643-7.aspx')]
def fetch(job):
 name,url,*payload=job
 try:
  req=urllib.request.Request(url,data=json.dumps(payload[0]).encode() if payload else None,headers={'User-Agent':'Mozilla/5.0',**({'Content-Type':'application/json'} if payload else {})})
  with urllib.request.urlopen(req,timeout=25) as r:body=r.read();status=r.status;ctype=r.headers.get('Content-Type');final=r.url
  (root/name).write_bytes(body)
  return {'file':name,'url':url,'final_url':final,'status':status,'content_type':ctype,'bytes':len(body),'sha256':hashlib.sha256(body).hexdigest(),'pdf_header':body.startswith(b'%PDF')}
 except Exception as e:return {'file':name,'url':url,'error':str(e)}
rows=list(concurrent.futures.ThreadPoolExecutor(4).map(fetch,jobs));(root/'fetch-log-9.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2));print(json.dumps(rows,ensure_ascii=False,indent=2))
