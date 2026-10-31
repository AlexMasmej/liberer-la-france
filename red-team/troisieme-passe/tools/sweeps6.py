#!/usr/bin/env python3
"""Sixth-round lead families, generalised from the defects of the sixth random audit (read-only).

Usage: python3 -I tools/sweeps6.py   → audit/sweeps/candidates-6.json and a printed summary.
  S16b a regulatory article (rewritten or maintained) cites a same-code L article whose versions all
       ended before the corpus date; only "dans sa rédaction antérieure"-type phrases are excluded
       (S16 also dropped any window containing "abrog" and missed R371-10)              (F3, E152)
  S18  an article that is not repealed relies on an article of the same code (or, in an annex, of
       the same annex) whose proposal is a repeal, outside a transitional phrase: half-repealed
       chapters                                                                           (F1/F5, E135, E223, E240, E268)
  S19a "n-ième alinéa de l'article X" where the next published version of X shifts that paragraph (F3, E148)
  S19b a published future version without proposal applies, "dans la rédaction suivante", an article
       that has a proposal (local adaptation that overrides the reform)                  (F4, E261)
Leads already placed in an earlier sweep packet are left out.
"""
import collections, glob, json, re, sqlite3, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sweeps import ALINEA, plain, shifted  # noqa: E402

PROD = Path('/Users/alexandremasmejean/.codex/.chatgpt-projects/g-p-6ad59c015c308191aa21cba63c71a6dc/legal-rewrite')
HOME = Path(__file__).resolve().parent.parent
CODES = {'LEGITEXT000006069577': 'cgi', 'LEGITEXT000006069568': 'a1', 'LEGITEXT000006069569': 'a2',
         'LEGITEXT000006069574': 'a3', 'LEGITEXT000006069576': 'a4', 'LEGITEXT000006072050': 'travail',
         'LEGITEXT000006073189': 'css', 'LEGITEXT000006074075': 'urba', 'LEGITEXT000006074096': 'cch'}
ANNEXES = {'a1', 'a2', 'a3', 'a4'}
AS_OF = '2026-10-18'
REPEAL = re.compile(r'^\s*(?:\(?Abrog[ée]|Le présent article est abrogé|Les articles [^.]{0,80} sont abrogés)', re.I)
PAST = re.compile(r"dans (?:sa|leur) rédaction (?:antérieure|applicable|en vigueur (?:avant|jusqu))|ancien(?:ne)?s? (?:article|régime)|en vigueur avant|antérieurement à|demeurent? régi|restent? régi|transitoire|jusqu'à leur terme|nés? (?:avant|sous)", re.I)
L_REF = re.compile(r'\b(?:LO|L|R\*?|D|A)\.?\s*\d{1,5}(?:-\d+){1,4}\b')
OTHER = re.compile(r"^[^.;]{0,60}?\b(?:du code (?!général des impôts)|de la loi|de l'ordonnance|du décret|du règlement|de la directive)", re.I)
SUFFIX = r"(?:bis|ter|quater|[a-z]{2,12}ies|[A-ZÀ-Ýİ]{1,3}|0|-0|-\d+)"
NUM_REF = re.compile(r"\barticles?\s+(\d{1,4}(?:-\d+)?(?:\s+" + SUFFIX + r"){0,4})(?![\w-])")
CGI_NAMED = re.compile(r"^[^.;]{0,90}?(?:code général des impôts|même code|dudit code|de ce code)")
APPLIES = re.compile(r"(?:est|sont) applicables?[^.;]{0,120}dans (?:sa|leur) rédaction suivante|dans (?:sa|leur) rédaction suivante|sous réserve des adaptations suivantes", re.I)


def normk(code, n):
    n = (n or '').replace('\xa0', ' ')
    return re.sub(r'\s+', ' ', n).strip() if code in ANNEXES | {'cgi'} else re.sub(r'[\s.*]', '', n).upper()


def main():
    db = sqlite3.connect(f'file:{PROD}/corpus.sqlite?mode=ro', uri=True)
    db.execute('pragma query_only=1')
    arts = collections.defaultdict(list)
    for c, i, n, st, vf, vu, x in db.execute('SELECT code_id,id,number,state,valid_from,valid_until,content_xml FROM articles'):
        code = CODES[c]
        arts[(code, normk(code, n))].append(dict(id=i, number=n, state=st, vf=vf or '', vu=vu or '', src=x))
    drafts = {(CODES[c], s): (st, p) for c, s, st, p in db.execute('SELECT code_id,source_id,status,proposed_xml FROM drafts')}
    swept = {a['key'].split('|')[1] for f in glob.glob(str(HOME / 'audit/sweeps/packet-*.json')) if 'S11pilot' not in f
             for a in json.load(open(f))['articles']}

    def current(code, key):
        for v in arts.get((code, key), []):
            if v['vf'] <= AS_OF < (v['vu'] or '9999') and v['state'] in ('VIGUEUR', 'ABROGE_DIFF', 'VIGUEUR_DIFF'):
                return v
        return None

    def ended(code, key):
        vs = arts.get((code, key))
        return bool(vs) and not any((w['vu'] or '9999') > AS_OF for w in vs)

    def proposed_repeal(code, key):
        v = current(code, key)
        if not v:
            return None
        p = drafts.get((code, v['id']), (None, None))[1]
        return v if p and REPEAL.match(plain(p)) else None

    def successor(code, v):
        nxt = sorted((w for w in arts[(code, normk(code, v['number']))] if v['vu'] and w['vf'] >= v['vu']), key=lambda w: w['vf'])
        return nxt[0] if nxt else None

    def cited(code, text):
        """(target code, key, start, end) for each article cited in the same code or, in an annex, the same annex."""
        out = []
        if code in ANNEXES:
            for m in NUM_REF.finditer(text):
                k = ' '.join(m.group(1).split())
                after = text[m.end():]
                if CGI_NAMED.match(after) or OTHER.match(after) or re.match(r"^\s*(?:de l'annexe|du présent code)", after):
                    continue
                if (code, k) in arts:
                    out.append((code, k, m.start(), m.end()))
        else:
            for m in L_REF.finditer(text):
                if OTHER.match(text[m.end():]):
                    continue
                out.append((code, normk(code, m.group(0)), m.start(), m.end()))
        return out

    s16b, s18, s19a, s19b = [], [], [], []
    for (code, key), vs in arts.items():
        v = current(code, key)
        if not v:
            continue
        st, p = drafts.get((code, v['id']), (None, None))
        text = plain(p) if p else plain(v['src'])
        if REPEAL.match(text) or v['id'] in swept:
            continue
        regulatory = code in ANNEXES or key[:1] in 'RDA'
        seen16, seen18 = set(), set()
        for tc, tk, a, b in cited(code, text):
            if tk == key:
                continue
            window = text[max(0, a - 140):b + 140]
            if PAST.search(window):
                continue
            if code not in ANNEXES and regulatory and tk[:1] == 'L' and ended(tc, tk) and tk not in seen16:
                seen16.add(tk)
                s16b.append(dict(code=code, number=v['number'], source_id=v['id'], status=st, cites=tk,
                                 cited_ended=max(w['vu'] for w in arts[(tc, tk)]), context=window[:300]))
            t = proposed_repeal(tc, tk)
            if t and tk not in seen18:
                seen18.add(tk)
                s18.append(dict(code=code, number=v['number'], source_id=v['id'], status=st, cites=t['number'],
                                cited_source_id=t['id'], context=window[:300]))
        if code not in ANNEXES | {'cgi'}:
            for m in ALINEA.finditer(text):
                r = normk(code, m.group(2))
                tv = current(code, r)
                nx = successor(code, tv) if tv else None
                if nx and nx['vf'] < '2031' and nx['state'] in ('VIGUEUR_DIFF',) and shifted(m.group(1), tv['src'], nx['src']):
                    s19a.append(dict(code=code, number=v['number'], source_id=v['id'], status=st, phrase=m.group(0)[:120],
                                     target=tv['number'], target_next=nx['id'], next_from=nx['vf']))
    # S19b: future versions (not yet in force) without a proposal that adapt an article which has one.
    for (code, key), vs in arts.items():
        for w in vs:
            if w['vf'] <= AS_OF or w['state'] != 'VIGUEUR_DIFF' or drafts.get((code, w['id']), (None, None))[1]:
                continue
            text = plain(w['src'])
            if not APPLIES.search(text):
                continue
            hits = []
            for tc, tk, a, b in cited(code, text):
                tv = current(tc, tk)
                if tv and drafts.get((tc, tv['id']), (None, None))[0] == 'rewrite_draft' and tk not in hits:
                    hits.append(tk)
            if hits:
                s19b.append(dict(code=code, number=w['number'], source_id=w['id'], status=None, valid_from=w['vf'],
                                 adapts_rewritten=hits[:15], n_rewritten=len(hits)))
    out = dict(read_from='production', as_of=AS_OF, S16b_regulation_on_ended_law=s16b, S18_relies_on_repealed_sibling=s18,
               S19a_alinea_shifted_by_future_version=s19a, S19b_future_adaptation_without_proposal=s19b)
    (HOME / 'audit/sweeps/candidates-6.json').write_text(json.dumps(out, ensure_ascii=False, indent=1))
    for k, v in out.items():
        if isinstance(v, list):
            print(k, len(v), collections.Counter(x.get('code', '?') for x in v).most_common())


if __name__ == '__main__':
    main()
