import copy
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent
source = json.loads((ROOT / 'source.json').read_text())[0]
original = ET.fromstring('<article>' + source['source_xml'] + '</article>')


def text_of(element):
    return ' '.join(''.join(element.itertext()).split())


def set_xml(element, content):
    element.clear()
    fragment = ET.fromstring('<cell>' + content + '</cell>')
    element.text = fragment.text
    element.extend(list(fragment))


def description(content):
    return '<p>' + content + '</p>'


def rewrite():
    root = copy.deepcopy(original)
    for element in root.iter():
        for attr in list(element.attrib):
            if attr not in {'rowspan', 'colspan'}:
                del element.attrib[attr]

    introductions = [
        "I. – Les produits, matériaux de construction, engrais et outillages industriels et agricoles figurant dans le tableau ci-dessous peuvent être importés en Guadeloupe, en Martinique et à La Réunion en franchise de la taxe sur la valeur ajoutée :",
        "II. – Le pain (ex 19-05) et le riz (10-06) s'ajoutent à la liste des produits du I.",
        "III. – Pour les importations à La Réunion, les produits suivants s'ajoutent à la liste du I :",
        "IV. – Pour les importations en Guadeloupe et en Martinique, les produits suivants s'ajoutent à la liste du I :",
    ]
    for p, value in zip(root.findall('p'), introductions):
        set_xml(p, value)

    edits = json.loads((ROOT / 'draft_edits.json').read_text())
    for path in sorted(ROOT.glob('edits_*.json')):
        extra = json.loads(path.read_text())
        assert not (set(edits) & set(extra)), path.name
        edits.update(extra)
    used = set()
    for table_index, table in enumerate(root.findall('table'), 1):
        for row_index, row in enumerate(table.findall('./tbody/tr')):
            code_cell, product_cell = list(row)
            if row_index == 0:
                code_cell.tag = product_cell.tag = 'th'
                set_xml(code_cell, '<p>Codes de la nomenclature combinée</p>')
                set_xml(product_cell, '<p>Désignation des produits</p>')
                continue
            code = text_of(code_cell)
            # Les codes, leur ordre et les cellules vides ne sont pas interprétés.
            set_xml(code_cell, description(code))
            key = str(table_index) + ':' + code
            if key in edits:
                set_xml(product_cell, description(edits[key]))
                used.add(key)
            elif len(product_cell) == 0 or all(x.tag == 'br' for x in product_cell):
                value = text_of(product_cell)
                set_xml(product_cell, description(value) if value else '')
    assert used == set(edits), sorted(set(edits) - used)

    fragments = ROOT / 'fragments'
    fragments.mkdir(exist_ok=True)
    groups = {'I': [], 'II': [], 'III': [], 'IV': []}
    part = None
    for child in root:
        if child.tag == 'p':
            part = text_of(child).split('.')[0]
        groups[part].append(ET.tostring(child, encoding='unicode'))
    for part, values in groups.items():
        (fragments / (part + '.xml')).write_text('\n'.join(values).strip() + '\n')
    proposed = '\n'.join((fragments / (part + '.xml')).read_text().strip()
                         for part in ['I', 'II', 'III', 'IV'])
    return proposed


if __name__ == '__main__':
    proposed = rewrite()
    (ROOT / 'proposed_article.xml').write_text(proposed)
    notes = json.loads((ROOT / 'drafting_notes.json').read_text())
    answer = {key: source[key] for key in
              ['code_id', 'source_id', 'source_sha256', 'number']}
    answer.update(proposed_xml=proposed, reason=notes['reason'],
                  review_notes=notes['review_notes'], status='rewrite_draft')
    (ROOT / 'answer.json').write_text(
        json.dumps([answer], ensure_ascii=False, indent=2) + '\n')
