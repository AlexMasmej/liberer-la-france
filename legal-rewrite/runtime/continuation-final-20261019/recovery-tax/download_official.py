import pathlib,urllib.request,urllib.error,json,hashlib
P=pathlib.Path(__file__).parent
urls=[('jo-2010-1728','https://www.legifrance.gouv.fr/download/pdf?id=63svbPxxA_9vv0UbiiKxBb2WtDEED7w2wigHyhC4AJI%3D')]
records=[]
for name,url in urls:
 try:
  r=urllib.request.urlopen(url,timeout=25);data=r.read();status=r.status;typ=r.headers.get('Content-Type','')
 except urllib.error.HTTPError as e:data=e.read();status=e.code;typ=e.headers.get('Content-Type','')
 except Exception as e:records.append({'url':url,'error':str(e)});continue
 path=P/(name+('.pdf' if data.startswith(b'%PDF') else '-response.html'));path.write_bytes(data);records.append({'url':url,'status':status,'content_type':typ,'path':str(path),'sha256':hashlib.sha256(data).hexdigest(),'length':len(data)})
(P/'download-attempts.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
for r in records:print(r)
