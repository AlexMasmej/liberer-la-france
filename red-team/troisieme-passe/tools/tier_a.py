#!/usr/bin/env python3
"""Tier A of the systematic reading: every rewritten article in force of the CGI and its annexes (read-only).

Usage: python3 -I tools/tier_a.py   → audit/tier-a/packet-T###.json and audit/tier-a/plan.json.
Articles already read in full by one of the six random audits are left out. Articles are grouped by their
deepest section (LEGI context), sections are kept whole where possible, and packets are cut by reading
weight (one unit per article plus one per 6,000 characters of source and proposal).
"""
import collections, glob, json, re, sqlite3
from pathlib import Path

PROD = Path('/Users/alexandremasmejean/.codex/.chatgpt-projects/g-p-6ad59c015c308191aa21cba63c71a6dc/legal-rewrite')
HOME = Path(__file__).resolve().parent.parent
CODES = {'LEGITEXT000006069577': 'cgi', 'LEGITEXT000006069568': 'a1', 'LEGITEXT000006069569': 'a2',
         'LEGITEXT000006069574': 'a3', 'LEGITEXT000006069576': 'a4'}
AS_OF = '2026-10-18'
TARGET = 34.0
SUFFIXES = ['', 'bis', 'ter', 'quater', 'quinquies', 'sexies', 'septies', 'octies', 'nonies', 'decies', 'undecies',
            'duodecies', 'terdecies', 'quaterdecies', 'quindecies', 'sexdecies', 'septdecies', 'octodecies',
            'novodecies', 'vicies', 'unvicies', 'duovicies', 'tervicies', 'quatervicies', 'quinvicies',
            'sexvicies', 'septvicies', 'octovicies', 'novovicies', 'tricies']


def natural(number):
    toks = re.sub(r'\s+', ' ', number.replace('\xa0', ' ')).strip().split(' ')
    key = []
    m = re.match(r'(\d+)(?:-(\d+))?', toks[0])
    key += [int(m.group(1)) if m else 99999, int(m.group(2) or 0) if m else 0]
    for t in toks[1:]:
        key += [SUFFIXES.index(t) if t in SUFFIXES else 50, t]
    return [str(k).zfill(6) if isinstance(k, int) else k for k in key]


def main():
    db = sqlite3.connect(f'file:{PROD}/corpus.sqlite?mode=ro', uri=True)
    db.execute('pragma query_only=1')
    owner = json.loads((HOME / 'apply/assignment.json').read_text())['owner']
    read = set()
    for f in glob.glob(str(HOME / 'audit/sample*.json')):
        read |= {x['source_id'] for x in json.load(open(f))['sample']}
    arts = []
    q = '''SELECT a.code_id, a.id, a.number, a.state, length(a.content_xml) + length(coalesce(d.proposed_xml, '')), a.valid_from, a.valid_until
           FROM articles a JOIN drafts d ON d.code_id = a.code_id AND d.source_id = a.id
           WHERE d.status = 'rewrite_draft' AND a.code_id IN (%s)''' % ','.join('?' * len(CODES))
    for c, i, n, st, size, vf, vu in db.execute(q, list(CODES)):
        if not ((vf or '') <= AS_OF < (vu or '9999') and st in ('VIGUEUR', 'ABROGE_DIFF', 'VIGUEUR_DIFF')):
            continue
        if i in read:
            continue
        x = db.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'", (c, i)).fetchone()
        s = (x[0].decode() if isinstance(x[0], bytes) else x[0]) if x else ''
        ctx = s[s.find('<CONTEXTE'):s.find('</CONTEXTE>')]
        titles = re.findall(r'<TITRE_TM[^>]*id="([^"]+)"[^>]*>([^<]*)</TITRE_TM>', ctx)
        sec = titles[-1][0] if titles else 'none'
        path = ' > '.join(t for _, t in titles[-3:])
        arts.append(dict(code=CODES[c], code_id=c, number=n, source_id=i, state=st, section=sec, section_path=path,
                         weight=round(1 + size / 6000, 2), previous_owner=owner.get(f'{c}|{i}')))
    order = list(CODES.values())
    arts.sort(key=lambda a: (order.index(a['code']), natural(a['number'])))
    # Sections in order of their first article; articles of a section stay together.
    sections = collections.OrderedDict()
    for a in arts:
        sections.setdefault((a['code'], a['section']), []).append(a)
    packets, cur, w = [], [], 0.0
    for (code, _), members in sections.items():
        sw = sum(a['weight'] for a in members)
        if cur and (cur[-1]['code'] != code or w + sw > TARGET * 1.25):
            packets.append(cur); cur, w = [], 0.0
        for a in members:
            if cur and w + a['weight'] > TARGET * 1.25:
                packets.append(cur); cur, w = [], 0.0
            cur.append(a); w += a['weight']
    if cur:
        packets.append(cur)
    out = HOME / 'audit/tier-a'
    out.mkdir(exist_ok=True)
    plan = []
    for k, p in enumerate(packets, 1):
        g = f'T{k:03d}'
        (out / f'packet-{g}.json').write_text(json.dumps(dict(group=g, articles=p), ensure_ascii=False, indent=1))
        plan.append(dict(group=g, code=p[0]['code'], n=len(p), weight=round(sum(a['weight'] for a in p), 1),
                         first=p[0]['number'], last=p[-1]['number'], owned=sum(1 for a in p if a['previous_owner'])))
    (out / 'plan.json').write_text(json.dumps(plan, ensure_ascii=False, indent=1))
    print(len(arts), 'articles;', len(packets), 'packets;', collections.Counter(a['code'] for a in arts))
    print('weight', round(sum(a['weight'] for a in arts)), 'owned', sum(1 for a in arts if a['previous_owner']))
    print('sizes', sorted(len(p) for p in packets)[::max(1, len(packets) // 10)])


if __name__ == '__main__':
    main()
