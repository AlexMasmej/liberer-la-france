"""Isolated design demonstrator ONLY; never imported by the live pipeline.
Validates the placeholder gate, not article completion or legal correctness.
"""
import hashlib, json, re
from pathlib import Path
from html.parser import HTMLParser
ROOT=Path(__file__).parent
BAD=re.compile(r'\[\s*(?:\.\.\.|…|à compléter|texte inchangé)\s*\]|<placeholder>|TODO',re.I)
class Text(HTMLParser):
    def __init__(self):super().__init__(convert_charrefs=True);self.words=[]
    def handle_data(self,data):self.words.append(data)
    def result(self):return ' '.join(' '.join(self.words).split())
def normalized(body):
    p=Text();p.feed(body);return p.result()
def sha(body):return hashlib.sha256(body.encode()).hexdigest()
def gate(source, proposed, registry):
    text=normalized(proposed)
    key=source['code_id']+'|'+source['source_id']
    certified=registry.get(key)
    if certified:
        if (source['source_sha256']!=certified['source_sha256'] or
            sha(source['source_xml'])!=certified['source_xml_sha256'] or
            sha(source.get('source_notes_xml',''))!=certified['notes_sha256']):
            raise ValueError('Certified source changed')
        original=normalized(source['source_xml'])
        start,end=certified['start'],certified['end']
        if original.count(start)!=1 or original.count(end)!=1 or text.count(start)!=1 or text.count(end)!=1:
            raise ValueError('Missing or duplicated clause boundaries')
        lo,hi=text.index(start),text.index(end)
        block=text[lo:hi]
        if sha(block)!=certified['block_sha256'] or block!=original[original.index(start):original.index(end)]:
            raise ValueError('Capital clause changed, truncated, or filled')
        matches=list(BAD.finditer(block))
        if [(m.start(),m.group()) for m in matches]!=[tuple(x) for x in certified['slots']]:
            raise ValueError('Field inventory mismatch')
        # Only certified character intervals are ignored by this lexical test.
        # No alteration to the actual article, no mass substitution of ellipses.
        chars=list(text)
        for m in matches:chars[lo+m.start():lo+m.end()]=' '*len(m.group())
        text=''.join(chars)
    if BAD.search(text):raise ValueError('Incomplete placeholder outside certified source fields')
    return {'placeholder_gate':'passed','article_completed':False}
