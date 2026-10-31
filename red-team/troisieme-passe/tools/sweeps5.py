#!/usr/bin/env python3
"""Fifth-round lead families, generalised from the defects of the fifth random audit (read-only).

Usage: python3 -I tools/sweeps5.py   → audit/sweeps/candidates-5.json and a printed summary.
The earlier S1, S2 and S8 lists read only L/R/D/A numbers, so they produced no lead at all in the
CGI and its annexes ("290 quater", "1649 quater N"). This tool reads CGI numbers.
  S1c  an annex article (not repealed) cites a CGI article whose proposal is a repeal      (F1, H056)
  S2c  a CGI article carrying a penalty cites a CGI article repealed, reduced or ended     (F2/F3, H117)
  S8c  a CGI or annex article (not repealed) relies on a CGI article whose versions all ended
       before the corpus date                                                            (F3, H160)
  S16  a rewritten regulatory article (other codes) cites, outside any transitional phrase, a
       same-code L article whose versions all ended before the corpus date               (F3, H091, H309)
  S17  earlier sweep leads qualified "m" and left uncorrected                             (H198, H091)
"""
import collections, glob, html, json, re, sqlite3
from pathlib import Path

PROD = Path('/Users/alexandremasmejean/.codex/.chatgpt-projects/g-p-6ad59c015c308191aa21cba63c71a6dc/legal-rewrite')
HOME = Path(__file__).resolve().parent.parent
CODES = {'LEGITEXT000006069577': 'cgi', 'LEGITEXT000006069568': 'a1', 'LEGITEXT000006069569': 'a2',
         'LEGITEXT000006069574': 'a3', 'LEGITEXT000006069576': 'a4', 'LEGITEXT000006072050': 'travail',
         'LEGITEXT000006073189': 'css', 'LEGITEXT000006074075': 'urba', 'LEGITEXT000006074096': 'cch'}
ANNEXES = {'a1', 'a2', 'a3', 'a4'}
AS_OF = '2026-10-18'
REPEAL = re.compile(r'^\s*(?:\(?Abrog[ée]|Le présent article est abrogé|Les articles [^.]{0,80} sont abrogés)', re.I)
PENALTY = re.compile(r"\b(?:amende|majoration|intérêt de retard|sanction|puni|pénalité)\b", re.I)
HISTORICAL = re.compile(r"rédaction|antérieur|ancien|abrog|avant (?:son|leur|la|le|l')|demeure|transitoire|en vigueur avant|issu|jusqu'au", re.I)
CGI_CODE = re.compile(r"^[^.;]{0,90}?(?:code général des impôts|même code|dudit code|de ce code)")
SUFFIX = r"(?:bis|ter|quater|[a-z]{2,12}ies|[A-ZÀ-Ýİ]{1,3}|0|-0|-\d+)"
OTHER_TEXT = re.compile(r"^\s*(?:,\s*)?(?:[IVX]+,?\s*)?(?:de la loi|de l'ordonnance|du décret|de la directive|du règlement|de l'arrêté|de la convention|du traité|du code (?!général des impôts)|de l'annexe|de la présente annexe|du livre des procédures)", re.I)
CGI_REF = re.compile(r"\barticles?\s+(\d{1,4}(?:-\d+)?(?:\s+" + SUFFIX + r"){0,4})(?![\w-])")


def plain(x):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', x or ''))).strip()


def norm(number):
    return re.sub(r'\s+', ' ', (number or '').replace('\xa0', ' ')).strip()


def norm_l(number):
    return re.sub(r'[\s.*]', '', number or '').upper()


def main():
    db = sqlite3.connect(f'file:{PROD}/corpus.sqlite?mode=ro', uri=True)
    db.execute('pragma query_only=1')
    arts = collections.defaultdict(list)
    for c, i, n, st, vf, vu, x in db.execute('SELECT code_id,id,number,state,valid_from,valid_until,content_xml FROM articles'):
        code = CODES[c]
        key = norm(n) if code in ANNEXES | {'cgi'} else norm_l(n)
        arts[(code, key)].append(dict(id=i, number=n, state=st, vf=vf or '', vu=vu or '', src=x))
    drafts = {(CODES[c], s): (st, p) for c, s, st, p in db.execute('SELECT code_id,source_id,status,proposed_xml FROM drafts')}
    removed = set()
    for f in glob.glob(f'{PROD}/batches/*/*.json'):
        if re.fullmatch(r'(?:batch)?\d+\.json', f.split('/')[-1]):
            removed |= {r['source_id'] for r in json.load(open(f)) if r.get('change_type') == 'normative_reduction'}

    def current(code, key):
        for v in arts.get((code, key), []):
            if v['vf'] <= AS_OF < (v['vu'] or '9999') and v['state'] in ('VIGUEUR', 'ABROGE_DIFF', 'VIGUEUR_DIFF'):
                return v
        return None

    def state(code, key):
        """'repealed' (by its proposal), 'reduced', 'ended' (all versions ended), or None."""
        vs = arts.get((code, key))
        if not vs:
            return None, None
        v = current(code, key)
        if not v:
            if not any((w['vu'] or '9999') > AS_OF for w in vs):
                return 'ended', max(vs, key=lambda w: w['vu'])
            return None, None
        p = drafts.get((code, v['id']), (None, None))[1]
        if p and REPEAL.match(plain(p)):
            return 'repealed', v
        if v['id'] in removed:
            return 'reduced', v
        return None, v

    def cgi_refs(text, own_code):
        """CGI article numbers cited in a text; in an annex, only when the CGI is named just after."""
        out = []
        for m in CGI_REF.finditer(text):
            tokens = m.group(1).split()
            # Only the full number counts: "310 HC" of an annex is not article 310 of the CGI.
            for k in (len(tokens),):
                cand = ' '.join(tokens[:k])
                if ('cgi', cand) in arts:
                    after = text[m.end():m.end() + 90]
                    if OTHER_TEXT.match(after):
                        break
                    if own_code == 'cgi' or CGI_CODE.match(text[m.end():]):
                        out.append((cand, m.start(), m.end()))
                    break
        return out

    s1c, s2c, s8c, s16 = [], [], [], []
    for (code, key), vs in arts.items():
        v = current(code, key)
        if not v:
            continue
        st, p = drafts.get((code, v['id']), (None, None))
        text = plain(p) if p else plain(v['src'])
        if REPEAL.match(text):
            continue
        if code in ANNEXES | {'cgi'}:
            seen = set()
            for num, a, b in cgi_refs(text, code):
                if (code == 'cgi' and num == key) or num in seen:
                    continue
                seen.add(num)
                tstate, t = state('cgi', num)
                if not tstate:
                    continue
                window = text[max(0, a - 160):b + 160]
                lead = dict(code=code, number=v['number'], source_id=v['id'], status=st, cites=num,
                            target_state=tstate, target_source_id=t['id'], context=window[:320])
                if code in ANNEXES and tstate == 'repealed':
                    s1c.append(lead)
                if code == 'cgi' and PENALTY.search(text) and (tstate != 'reduced' or key[:2] == '17'):
                    s2c.append(lead)
                if tstate == 'ended' and not HISTORICAL.search(window):
                    s8c.append(dict(lead, ended=t['vu']))
        elif p and st == 'rewrite_draft' and key[:1] in 'RD':
            for m in re.finditer(r'\bL\.?\s*\d{1,5}(?:-\d+){1,4}\b', text):
                r = norm_l(m.group(0))
                vs_r = arts.get((code, r))
                window = text[max(0, m.start() - 160):m.end() + 160]
                if vs_r and not any((w['vu'] or '9999') > AS_OF for w in vs_r) and not HISTORICAL.search(window) \
                        and not re.search(r"\bcode (?:rural|de|des|du|général des collectivités)", text[m.end():m.end() + 60]):
                    s16.append(dict(code=code, number=v['number'], source_id=v['id'], status=st, cites=r,
                                    cited_ended=max(w['vu'] for w in vs_r), context=window[:320]))
                    break

    s17 = []
    for f in sorted(glob.glob(str(HOME / 'audit/sweeps/[WYJ]??*.json'))):
        if 'packet' in f:
            continue
        for l in json.load(open(f)).get('leads', []):
            if l.get('qualification') == 'm' and not l.get('corrected'):
                s17.append(dict(found_in=Path(f).name, **{k: l.get(k) for k in ('key', 'family', 'evidence')}))

    out = dict(read_from='production', as_of=AS_OF, S1c_annex_applies_repealed_cgi=s1c, S2c_cgi_penalty_on_changed_article=s2c,
               S8c_cgi_relies_on_ended_article=s8c, S16_regulation_on_ended_law=s16, S17_uncorrected_minor_leads=s17)
    (HOME / 'audit/sweeps/candidates-5.json').write_text(json.dumps(out, ensure_ascii=False, indent=1))
    for k, v in out.items():
        if isinstance(v, list):
            print(k, len(v), collections.Counter(x.get('code', '?') for x in v).most_common())


if __name__ == '__main__':
    main()
