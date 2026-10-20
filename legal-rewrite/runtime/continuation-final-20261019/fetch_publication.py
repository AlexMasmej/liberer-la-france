"""Download the published edition for comparison with the local release."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import json

ROOT = Path(__file__).resolve().parent
LIVE = ROOT/'live'
LIVE.mkdir(exist_ok=True)
URLS = {
    'manifest.json': 'https://www.libererlaretraite.com/downloads/manifest.json',
    'cinq-codes-complets.zip': 'https://www.libererlaretraite.com/downloads/cinq-codes-complets.zip',
    'retraite.html': 'https://www.libererlaretraite.com/',
    'embauche.html': 'https://www.libererlembauche.com/',
    'revenu.html': 'https://www.libererlerevenu.com/',
    'entreprise.html': 'https://www.libererlentreprise.com/',
    'logement.html': 'https://www.libererlelogement.com/',
}


def fetch(item):
    filename, url = item
    request = Request(url, headers={'Cache-Control': 'no-cache', 'User-Agent': 'Legal-rewrite-publication-check/1.0'})
    with urlopen(request, timeout=120) as response:
        data = response.read()
        assert response.status == 200
    (LIVE/filename).write_bytes(data)
    return {'filename': filename, 'bytes': len(data), 'url': url}


with ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(fetch, URLS.items()))
withdrawn = 'https://www.libererlaretraite.com/downloads/coordination-sru-plages.html'
try:
    with urlopen(withdrawn, timeout=30) as response:
        raise AssertionError('Withdrawn coastal repeal is still publicly accessible')
except HTTPError as error:
    assert error.code == 404
(LIVE/'withdrawn-repeal.json').write_text(json.dumps({'url': withdrawn, 'http_status': 404})+'\n')
(LIVE/'fetch.json').write_text(json.dumps(results, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(results, ensure_ascii=False, indent=2))
