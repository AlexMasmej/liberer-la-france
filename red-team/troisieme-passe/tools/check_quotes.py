#!/usr/bin/env python3
"""Check that the passages quoted as proof of each resolution (« … ») appear verbatim in the final exports.

Usage: check_quotes.py <GROUP> [...]   (reads reports/reexam-final/<GROUP>.json and evidence/cited/<final>/)
"""
import json,glob,re,html,sys,collections
def norm(x):
    x=html.unescape(re.sub(r'<[^>]+>',' ',x or '')).replace('’',"'").replace('\u00a0',' ').replace('\u202f',' ').replace('«',' ').replace('»',' ')
    return re.sub(r'\s+',' ',x).strip()
texts={}
for f in glob.glob('evidence/cited/20261029T034912Z/*.json'):
    d=json.load(open(f)); dr=d.get('draft') or {}
    texts[d['source_id']]=norm(' '.join([d.get('source_xml') or '', dr.get('proposed_xml') or '', dr.get('reason') or '', dr.get('review_notes') or '', d.get('nota') or '']))
alltext=' '.join(texts.values())
for g in sys.argv[1:]:
    d=json.load(open(f'reports/reexam-final/{g}.json'))
    c=collections.Counter()
    for o in d['objections']:
        if o['verdict'] not in ('résolue','obsolète'): continue
        qs=[q for q in re.findall(r'«\s*([^»]{12,})\s*»',o.get('trace') or '')]
        def seg_ok(q):
            segs=[norm(x).strip(' .;,') for x in re.split(r'\[[^\]]*\]',q)]
            segs=[x for x in segs if len(x)>=12]
            return bool(segs) and all(x in alltext for x in segs)
        ok=[q for q in qs if seg_ok(q)]
        bad=[q for q in qs if q not in ok]
        c['resolved']+=1; c['quotes']+=len(qs); c['found']+=len(ok)
        if not qs: print(g,o['id'],'NO QUOTE in trace')
        for q in bad: print(g,o['id'],'QUOTE NOT FOUND:',q[:120])
    print(g,dict(c))
