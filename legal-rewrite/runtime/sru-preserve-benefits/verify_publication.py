"""Check the downloaded public edition against the approved restorations."""
from pathlib import Path
from io import BytesIO
import hashlib
import json
import sys
import zipfile

LEGAL = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(LEGAL))
from source_assets import safe_html

ROOT = Path(__file__).resolve().parent
LIVE = Path(sys.argv[1])
SITE = LEGAL.parent / 'sites/liberer-la-retraite/dist'
sha = lambda data: hashlib.sha256(data).hexdigest()
manifest = json.loads((LIVE/'manifest.json').read_text())
assert (LIVE/'manifest.json').read_bytes() == (SITE/'downloads/manifest.json').read_bytes()
assert manifest['source_records'] == 30317
assert manifest['exhaustive_rewriting_complete'] is False
companions = manifest['outside_code_inventory_coordinations']
assert sum(a['articles'] for a in companions) == 17
assert all(a['filename'] != 'coordination-sru-plages.html' for a in companions)
expected = {}
sources = {}
for name in ['coastal', 'drained-job-audit']:
    for a in json.loads((ROOT/name/'answer.json').read_text()):
        expected[(a['code_id'], a['source_id'])] = a
    for a in json.loads((ROOT/name/'source.json').read_text()):
        sources[(a['code_id'], a['source_id'])] = a
restored, companion_keys = set(), set()
payload = (LIVE/'cinq-codes-complets.zip').read_bytes()
assert len(payload) == manifest['all']['bytes']
assert sha(payload) == sha((SITE/'downloads/cinq-codes-complets.zip').read_bytes())
with zipfile.ZipFile(BytesIO(payload)) as common:
    assert common.testzip() is None
    inner = json.loads(common.read('manifest.json'))
    assert inner['as_of'] == manifest['as_of']
    assert inner['downloads'] == manifest['downloads']
    assert inner['exhaustive_rewriting_complete'] is False
    for item in manifest['downloads']:
        nested = common.read(item['filename'])
        assert sha(nested) == item['sha256']
        with zipfile.ZipFile(BytesIO(nested)) as archive:
            assert archive.testzip() is None
            assert not any('/sru-plages/' in n for n in archive.namelist())
            for name in archive.namelist():
                if name.startswith('coordinations/') and name.endswith('/articles.json'):
                    group = json.loads(archive.read(name))
                    for a in group['articles']:
                        key = a.get('code_id',a['source_url']), a.get('source_id',a['number'])
                        assert key != ('JORFTEXT000000875580', 'LEGIARTI000042913715')
                        companion_keys.add(key)
                        if a['number'] == 'R3211-15':
                            approved = json.loads((ROOT/'discount/answer.json').read_text())[0]
                            assert a['source_xml'] == approved['source_xml']
                            assert a['proposed_xml'] == approved['proposed_xml']
                elif name.endswith('/articles.json'):
                    for a in json.loads(archive.read(name)):
                        key = a['code_id'], a['source_id']
                        if key in expected:
                            assert a['proposed_xml'] == safe_html(expected[key]['proposed_xml'])
                            assert a['source_xml'] == safe_html(sources[key]['source_xml'])
                            assert a['source_notes_xml'] == safe_html(sources[key]['source_notes_xml'])
                            restored.add(key)
assert restored == set(expected)
assert len(companion_keys) == 17
html_checks = {}
for label, slug in [('retraite','liberer-la-retraite'),
                    ('embauche','nouveaudroitdutravail'),
                    ('revenu','liberer-le-revenu'),
                    ('entreprise','liberer-lentreprise'),
                    ('logement','liberer-le-logement')]:
    public = (LIVE/(label+'.html')).read_bytes()
    assert public == (LEGAL.parent/'sites'/slug/'dist/index.html').read_bytes()
    html_checks[label] = sha(public)
housing = (LIVE/'logement.html').read_text()
assert 'franchise TASCOM' in housing and 'dérogations littorales' in housing
report = {'public_edition_verified': True, 'whole_article_corrections_checked': len(restored),
          'discount_benefit_checked': True, 'withdrawn_repeals_absent': True,
          'outside_code_inventory_articles': len(companion_keys),
          'common_archive_sha256': sha(payload), 'five_sites_sha256': html_checks,
          'drafted_articles': manifest['drafted_articles'],
          'exhaustive_rewriting_complete': False}
(ROOT/'live-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
