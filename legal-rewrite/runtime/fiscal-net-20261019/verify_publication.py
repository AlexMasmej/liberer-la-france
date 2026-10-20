"""Compare the actual public archive with the approved complete articles."""
from pathlib import Path
from io import BytesIO
import hashlib
import json
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]/'continuation-final-20261019'
LEGAL = ROOT.parents[1]
sys.path.insert(0, str(LEGAL))
from source_assets import safe_html, load_companions, asset_path
from coordination_downloads import load as load_coordinations

LIVE = Path(sys.argv[1])
SITE = LEGAL.parent/'sites/liberer-la-retraite/dist'
sha = lambda data: hashlib.sha256(data).hexdigest()
manifest = json.loads((LIVE/'manifest.json').read_text())
assert (LIVE/'manifest.json').read_bytes() == (SITE/'downloads/manifest.json').read_bytes()
assert manifest['source_records'] == 30317
assert manifest['exhaustive_rewriting_complete'] is False
assert manifest['graphic_source_coverage']['unresolved_articles'] == 9

packs = [ROOT/'d912-rewrite', ROOT/'cvae-approved-003',
         ROOT/'travail-negociation/edition001',
         ROOT/'travail-negociation-coordinations/edition001',
         ROOT.parent/'sru-preserve-benefits/coastal',
         ROOT.parent/'sru-preserve-benefits/drained-job-audit']
for branch in ['logement-next', 'css-next']:
    registered = sorted((ROOT/branch).glob('edition*/registration.json'))
    if registered:
        packs.append(registered[-1].parent)
expected, sources = {}, {}
for pack in packs:
    for a in json.loads((pack/'answer.json').read_text()):
        key = a['code_id'], a['source_id']
        assert key not in expected
        expected[key] = a
    for a in json.loads((pack/'source.json').read_text()):
        sources[(a['code_id'], a['source_id'])] = a

active = load_coordinations()
outside = {item['slug']: item for item in active}
source_companions = load_companions()
checked, companions_seen, outside_keys, assets_seen = set(), set(), set(), set()
payload = (LIVE/'cinq-codes-complets.zip').read_bytes()
assert len(payload) == manifest['all']['bytes']
assert sha(payload) == sha((SITE/'downloads/cinq-codes-complets.zip').read_bytes())
with zipfile.ZipFile(BytesIO(payload)) as common:
    assert common.testzip() is None
    inner = json.loads(common.read('manifest.json'))
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
                    slug = name.split('/')[1]
                    assert group == outside[slug]
                    companions_seen.add(slug)
                    for a in group['articles']:
                        key = a.get('code_id', a['source_url']), a.get('source_id', a['number'])
                        assert key != ('JORFTEXT000000875580', 'LEGIARTI000042913715')
                        outside_keys.add(key)
                elif name.endswith('/articles.json'):
                    code_slug = name.split('/')[0]
                    for a in json.loads(archive.read(name)):
                        key = a['code_id'], a['source_id']
                        if key in expected:
                            assert a['proposed_xml'] == safe_html(expected[key]['proposed_xml']), key
                            assert a['source_xml'] == safe_html(sources[key]['source_xml']), key
                            assert a['source_notes_xml'] == safe_html(sources[key]['source_notes_xml']), key
                            checked.add(key)
                        if key in source_companions:
                            record = source_companions[key]
                            assert a['source_companions'] == record
                            for field in ['media', 'documents']:
                                for media in record.get(field, []):
                                    data = archive.read(code_slug+'/'+media['path'])
                                    assert sha(data) == media['sha256']
                                    assert data == asset_path(media['path']).read_bytes()
                                    assets_seen.add(media['path'])
assert checked == set(expected)
assert companions_seen == set(outside)
assert len(outside_keys) == sum(len(a['articles']) for a in active)
assert 'complementaire/d912-15-jo-20150628-copie.pdf' in assets_seen
assert {'media/css-d912-15-modeles-page3.png', 'media/css-d912-15-modeles-page4.png'} <= assets_seen
html_checks = {}
for label, slug in [('retraite', 'liberer-la-retraite'), ('embauche', 'nouveaudroitdutravail'),
                    ('revenu', 'liberer-le-revenu'), ('entreprise', 'liberer-lentreprise'),
                    ('logement', 'liberer-le-logement')]:
    public = (LIVE/(label+'.html')).read_bytes()
    assert public == (LEGAL.parent/'sites'/slug/'dist/index.html').read_bytes(), label
    html_checks[label] = sha(public)
housing = (LIVE/'logement.html').read_text()
assert 'franchise TASCOM' in housing and 'dérogations littorales' in housing
assert 'CVAE' in (LIVE/'entreprise.html').read_text()
method = (LIVE/'chiffrage-is-net.html').read_bytes()
assert method == (LEGAL.parent/'sites/liberer-lentreprise/dist/chiffrage-is-net.html').read_bytes()
assert b'chiffrage-is-net.html' in (LIVE/'entreprise.html').read_bytes()
assert 'Mesurer l’effet net sur les finances publiques.' in (LIVE/'entreprise.html').read_text()
assert 'CIR' in method.decode() and 'Bpifrance' in method.decode()
assert 'Aucun solde français chiffré' in method.decode()
report = {'public_edition_verified': True, 'net_fiscal_method_verified': True, 'method_sha256': sha(method), 'whole_articles_compared': len(checked),
          'withdrawn_repeals_absent': True, 'outside_code_inventory_articles': len(outside_keys),
          'source_companion_assets_verified': len(assets_seen), 'graphic_articles_unresolved': 9,
          'common_archive_sha256': sha(payload), 'five_sites_sha256': html_checks,
          'drafted_articles': manifest['drafted_articles'], 'source_records': 30317,
          'exhaustive_rewriting_complete': False}
(Path(__file__).resolve().parent/'live-verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(report, ensure_ascii=False, indent=2))
