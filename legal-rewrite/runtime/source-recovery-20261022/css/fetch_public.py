from pathlib import Path
import concurrent.futures, hashlib, json, urllib.request, urllib.error
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parent
URLS=[
('bo0502-sante.response','https://sante.gouv.fr/fichiers/bo/2005/05-02/bo0502.pdf'),
('bo0401-sante.response','https://sante.gouv.fr/fichiers/bo/2004/04-01/bo0401.pdf'),
('bo0424-sante.response','https://sante.gouv.fr/fichiers/bo/2004/04-24/bo0424.pdf'),
('bo0502-solidarites.response','https://solidarites.gouv.fr/fichiers/bo/2005/05-02/bo0502.pdf'),
('bo0502-social-sante.response','https://social-sante.gouv.fr/fichiers/bo/2005/05-02/bo0502.pdf'),
('bo0502-travail-archive.response','https://travail.gouv.fr/fichiers/bo/2005/05-02/bo0502.pdf'),
('ameli-bareme-search.html','https://circulaires.ameli.fr/?keys=invalidit%C3%A9&title=&field_date_de_publication_value=01%2F01%2F1983&field_date_de_publication_value_1=31%2F12%2F1983'),
]
def fetch(spec):
    name,url=spec
    result={'url':url,'name':name,'method':'ordinary_public_HTTPS_urllib_no_auth_no_cookies','at_utc':datetime.now(timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(url,timeout=35) as r:
            data=r.read();result.update(status=r.status,final_url=r.url,headers=dict(r.headers))
    except urllib.error.HTTPError as e:
        data=e.read();result.update(status=e.code,error=str(e),headers=dict(e.headers))
    except Exception as e:
        result['error']=str(e);return result
    result.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),pdf_header=data.startswith(b'%PDF'))
    if result['pdf_header']: name=name.replace('.response','.pdf')
    (ROOT/'documents'/name).write_bytes(data);result['path']='documents/'+name
    result['html_excerpt']=None if result['pdf_header'] else data[:800].decode('utf-8','replace')
    return result
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    results=list(pool.map(fetch,URLS))
(ROOT/'access-attempts-batch01.json').write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n')
for r in results:print(r['name'],r.get('status'),r.get('bytes'),r.get('pdf_header'),r.get('error',''))
