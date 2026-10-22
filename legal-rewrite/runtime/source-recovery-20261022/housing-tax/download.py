from pathlib import Path
import urllib.request, urllib.error, json, hashlib, datetime, concurrent.futures
P=Path(__file__).resolve().parent
def fetch(item):
    name,url=item
    at=datetime.datetime.now(datetime.timezone.utc).isoformat()
    try:
        with urllib.request.urlopen(url,timeout=25) as r:
            data=r.read(); status=r.status; typ=r.headers.get('Content-Type',''); final=r.url
    except urllib.error.HTTPError as e:
        data=e.read(); status=e.code; typ=e.headers.get('Content-Type',''); final=e.url
    except Exception as e:
        return {'name':name,'url':url,'retrieved_at_utc':at,'error':str(e),'method':'standard public GET; no cookies or custom headers'}
    ispdf=data.startswith(b'%PDF-')
    path=('documents/' if ispdf else 'responses/')+name+('.pdf' if ispdf else '.html')
    (P/path).write_bytes(data)
    return {'name':name,'url':url,'final_url':final,'retrieved_at_utc':at,'status':status,'content_type':typ,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'path':path,'is_pdf':ispdf,'method':'standard public GET; no cookies or custom headers'}
if __name__=='__main__':
    import sys
    batch=Path(sys.argv[1])
    records=json.loads(batch.read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        result=list(ex.map(fetch,[(x['name'],x['url']) for x in records]))
    out=P/(batch.stem+'-results.json')
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    for r in result: print(json.dumps(r,ensure_ascii=False))
