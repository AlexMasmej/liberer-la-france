import json
import re
import html
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET

sources = json.loads(Path('source.json').read_text())
answer = json.loads(Path('answer.json').read_text())
allowed = {'p','br','table','thead','tbody','tfoot','tr','th','td','b','strong','i','em','u','sup','sub','ul','ol','li','div','span','blockquote'}
fields = {'code_id','source_id','source_sha256','number','proposed_xml','reason','review_notes','status'}

def text(value):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', value))).strip()

def alineas(value):
    value = re.sub(r'<br\s*/?>\s*<br\s*/?>', '\n', value, flags=re.I)
    value = re.sub(r'</p\s*>', '\n', value, flags=re.I)
    value = re.sub(r'<[^>]+>', '', value)
    return [x.strip() for x in html.unescape(value).splitlines() if x.strip()]

assert isinstance(answer,list) and len(answer) == len(sources) == 24
assert len({x['source_id'] for x in answer}) == 24
reports=[]
for src, draft in zip(sources, answer):
    assert set(draft) == fields, draft['number']
    for key in ('code_id','source_id','source_sha256','number'):
        assert src[key] == draft[key], (src['number'], key)
    assert draft['status'] == 'rewrite_draft'
    for key in ('proposed_xml','reason','review_notes'):
        assert isinstance(draft[key], str) and draft[key].strip()
    proposed = draft['proposed_xml']
    root = ET.fromstring('<root>'+proposed+'</root>')
    for el in root.iter():
        if el is root: continue
        assert el.tag in allowed, (draft['number'],el.tag)
        for key,value in el.attrib.items():
            assert key in {'rowspan','colspan'} and re.fullmatch('[0-9]+',value)
    assert text(proposed) != text(src['source_xml']), draft['number']
    assert not any(x in proposed.lower() for x in ['texte inchangé','à rédiger','à compléter','...','…','http://','https://','```'])
    source_numbers = Counter(re.findall(r'\d+(?:[.,-]\d+)*', text(src['source_xml'])))
    draft_numbers = Counter(re.findall(r'\d+(?:[.,-]\d+)*', text(proposed)))
    assert source_numbers == draft_numbers, (draft['number'],source_numbers-draft_numbers,draft_numbers-source_numbers)
    source_refs = Counter(re.findall(r'\b[LRD]\.\s*\d+(?:-\d+)*',text(src['source_xml'])))
    draft_refs = Counter(re.findall(r'\b[LRD]\.\s*\d+(?:-\d+)*',text(proposed)))
    assert source_refs == draft_refs, draft['number']
    source_alineas = alineas(src['source_xml'])
    draft_alineas = alineas(proposed)
    assert len(source_alineas) == len(draft_alineas), (draft['number'],len(source_alineas),len(draft_alineas))
    for tag in ('table','tr','th','td'):
        assert len(re.findall('<'+tag+r'\b',src['source_xml'])) == len(root.findall('.//'+tag)), (draft['number'],tag)
    reports.append({'number':draft['number'],'source_chars':len(src['source_xml']),'proposed_chars':len(proposed),'alineas':len(draft_alineas),'references_preserved':True,'numbers_preserved':True,'status':draft['status']})
report = {'article_count':len(answer),'checks':['exact_schema','exact_identifiers','complete_unique_coverage','allowed_xml','nonidentical_text','numeric_literals','article_references','paragraph_count','table_structure'],'articles':reports}
Path('validation_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'file':'answer.json','article_count':len(answer),'all_checks':'passed','alineas':sum(x['alineas'] for x in reports),'tables':0},ensure_ascii=False))
