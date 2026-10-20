from pathlib import Path
import gzip, hashlib, json, tarfile, xml.etree.ElementTree as E

H = Path(__file__).resolve().parent
B = H.parents[1]
owners = {
    'LEGITEXT000006070633': {'L1523-5','L1523-6','L1525-3','L2254-1','L5216-5','L5214-16','L5215-20'},
    'JORFTEXT000000875580': {'3'},
    'JORFTEXT000000196404': {'12','13','14'},
    'JORFTEXT000000207538': {'88','89'},
}
manifest = json.loads((B / 'archive-manifest.json').read_text())
paths = [('Freemium_legi_global_20250713-140000.tar.gz', Path('/private/tmp/legi-global-20250713.tar.gz'))]
paths += [(r['name'], Path('/private/tmp/legi-updates')/r['name']) for r in manifest if not r['name'].startswith('Freemium')]
records = {}
for i, (name, path) in enumerate(paths):
    with gzip.open(path, 'rb') as gz:
        with tarfile.open(fileobj=gz, mode='r|') as tar:
            for m in tar:
                if not m.isfile() or not m.name.endswith('.xml') or '/article/' not in m.name:
                    continue
                owner = next((c for c in m.name.split('/') if c in owners), None)
                if not owner:
                    continue
                raw = tar.extractfile(m).read()
                node = E.fromstring(raw)
                num = node.findtext('META/META_SPEC/META_ARTICLE/NUM')
                if num not in owners[owner]:
                    continue
                identifier = node.findtext('META/META_COMMUN/ID')
                c = node.find('BLOC_TEXTUEL/CONTENU')
                note = node.find('NOTA/CONTENU')
                def contents(el):
                    return (el.text or '') + ''.join(E.tostring(a, encoding='unicode') for a in el) if el is not None else ''
                records[owner,identifier] = {
                    'owner':owner, 'source_id':identifier, 'number':num,
                    'valid_from':node.findtext('META/META_SPEC/META_ARTICLE/DATE_DEBUT'),
                    'valid_until':node.findtext('META/META_SPEC/META_ARTICLE/DATE_FIN'),
                    'state':node.findtext('META/META_SPEC/META_ARTICLE/ETAT'),
                    'whole_article_xml':raw.decode(), 'source_xml':contents(c),
                    'source_notes_xml':contents(note), 'source_sha256':hashlib.sha256(raw).hexdigest(),
                    'archive':name, 'archive_member':m.name,
                    'source_url':'https://www.legifrance.gouv.fr/'+('codes' if owner.startswith('LEGITEXT') else 'loda')+'/article_lc/'+identifier,
                }
        while gz.read(1024*1024):
            pass
    if i % 50 == 0:
        print('archives',i+1,'records',len(records),flush=True)
result = {'as_of':'2026-10-18', 'archives_replayed':len(paths), 'articles':list(records.values())}
(H / 'full-law-outside-evidence.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
print('DONE',len(records),flush=True)
