import json
import re
from collections import Counter
from pathlib import Path
import xml.etree.ElementTree as ET


source = json.loads(Path('source.json').read_text())
drafts = json.loads(Path('drafts.json').read_text())

# Make the qualification of the entire list of eligible goods explicit.
for draft in drafts:
    if draft['number'] in {'384 septies-0 C', '396 sexies'}:
        draft['proposed_xml'] = draft['proposed_xml'].replace(
            "par le ministre du budget sur sa proposition.",
            "par le ministre du budget sur proposition du président.",
        )
    if draft['number'] == '384 septies-0 B':
        draft['proposed_xml'] = draft['proposed_xml'].replace(
            "il exerce, pour son fonctionnement, les attributions",
            "il exerce, pour le fonctionnement de cette section, les attributions",
        )
    if draft['number'] == '396 undecies':
        draft['proposed_xml'] = draft['proposed_xml'].replace(
            "Pour délibérer, le comité doit réunir au moins huit membres, titulaires ou suppléants. Une section doit réunir au moins deux membres, titulaires ou suppléants.",
            "Pour délibérer, le comité doit réunir au moins huit de ses membres, titulaires ou suppléants, présents à la séance. Une section doit réunir au moins deux de ses membres, titulaires ou suppléants, présents à la séance.",
        )
    if draft['number'] == '384-0 A bis':
        draft['proposed_xml'] = draft['proposed_xml'].replace(
            "portant sur des œuvres d'art, des livres, des objets de collection ou des documents de haute valeur artistique ou historique,",
            "portant sur des biens de haute valeur artistique ou historique — œuvres d'art, livres, objets de collection ou documents —,",
        ).replace(
            "sur l'acquisition d'œuvres d'art, de livres, d'objets de collection ou de documents de haute valeur artistique ou historique.",
            "sur l'acquisition de biens de haute valeur artistique ou historique, qu'il s'agisse d'œuvres d'art, de livres, d'objets de collection ou de documents.",
        )
    if draft['number'] == '396 bis':
        draft['proposed_xml'] = draft['proposed_xml'].replace(
            "Si la créance subrogée est comprise dans une inscription,",
            "Si la créance concernée par la subrogation est comprise dans une inscription,",
        )

assert len(source) == len(drafts) == 24
assert len({a['source_id'] for a in source}) == 24
allowed_tags = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
answer = []
for original, draft in zip(source, drafts):
    assert original['number'] == draft['number']
    root = ET.fromstring('<root>' + draft['proposed_xml'] + '</root>')
    for element in root.iter():
        assert element.tag == 'root' or element.tag in allowed_tags
        assert all(
            key in {'rowspan', 'colspan'} and re.fullmatch(r'[0-9]+', value)
            for key, value in element.attrib.items()
        )
    assert draft['proposed_xml'].strip() != original['source_xml'].strip()
    entry = {key: original[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    entry.update({key: draft[key] for key in ('proposed_xml', 'reason', 'review_notes')})
    entry['status'] = 'rewrite_draft'
    answer.append(entry)

Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles ; {sum(len(a["proposed_xml"]) for a in answer)} caractères de texte proposé.')
