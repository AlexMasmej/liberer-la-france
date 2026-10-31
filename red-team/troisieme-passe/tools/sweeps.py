#!/usr/bin/env python3
"""Mechanical candidate lists for the defect families, on the live production text (read-only).

Usage: python3 -I tools/sweeps.py   → audit/sweeps/candidates.json and a printed summary.
Candidates are leads for qualification, never findings: every one must be read in full.
  S1  a legislative proposal repeals or reduces an article, and a regulatory article (same code, or
      CGI annexes for the CGI) still cites it without being repealed itself            (family F1)
  S2  a provision carrying a penalty cites an article whose proposal is a repeal         (family F2)
  S3  a proposal cites an L/R/D/A number that has no version in the code at all          (family F3)
  S4  a proposal claims not to defer a repeal while the next version replaces the text   (family F4)
  S5  a current version has a proposal, its published successor has none                  (family F4)
  S6  names used for the reform law                                                       (issue #3)
"""
import collections, html, json, re, sqlite3
from pathlib import Path

PROD = Path('/Users/alexandremasmejean/.codex/.chatgpt-projects/g-p-6ad59c015c308191aa21cba63c71a6dc/legal-rewrite')
HOME = Path(__file__).resolve().parent.parent
CODES = {'LEGITEXT000006069577': 'cgi', 'LEGITEXT000006069568': 'a1', 'LEGITEXT000006069569': 'a2',
         'LEGITEXT000006069574': 'a3', 'LEGITEXT000006069576': 'a4', 'LEGITEXT000006072050': 'travail',
         'LEGITEXT000006073189': 'css', 'LEGITEXT000006074075': 'urba', 'LEGITEXT000006074096': 'cch'}
CGI_FAMILY = {'cgi', 'a1', 'a2', 'a3', 'a4'}
AS_OF = '2026-10-18'
REPEAL = re.compile(r'^\s*(?:\(?Abrog[ée]|Le présent article est abrogé)', re.I)
PENALTY = re.compile(r"\b(?:amende|puni|punie|emprisonnement|contravention|majoration de|sanction pécuniaire)\b", re.I)
FALSE_DEFERRAL = re.compile(r"ne report\w*[^.]{0,80}abrogation|abrogation différée|abrogation[^.]{0,40}prévue au 1er janvier", re.I)
REFORM_LAW = re.compile(r"loi (?:portant (?:la présente|cette|ladite) (?:réforme|modification|coordination)|instituant le contrat (?:de travail )?unique|supprimant [^,.;]{3,60}|abrogeant [^,.;]{3,60}|qui (?:les )?institue|portant réforme[^,.;]{0,40})", re.I)


def plain(x):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', x or ''))).strip()


def refs(text):
    """L/R/D/A article numbers cited in a text, normalised ("R. 3122-9" -> "R3122-9")."""
    return {re.sub(r'[\s.*]', '', m).upper() for m in
            re.findall(r'\b(?:LO|L|R\*?|D|A)\.?\s*\d{1,5}(?:-\d+){1,4}\b', text)}


ALINEA = re.compile(r"\b((?:premier|deuxième|second|troisième|quatrième|cinquième|sixième|septième|huitième|neuvième|dixième|dernier|avant-dernier) alinéa) (?:du [IVX]+ )?de l'article ((?:LO|L|R\*?|D|A)\.?\s*\d{1,5}(?:-\d+){1,4})", re.I)


def paragraphs(xml):
    """Number of non-empty paragraphs, as a reader counts alinéas."""
    parts = re.split(r'<br\s*/?>|</p>|\n', xml or '')
    return sum(1 for x in parts if plain(x))


ORDINALS = {'premier': 1, 'deuxième': 2, 'second': 2, 'troisième': 3, 'quatrième': 4, 'cinquième': 5, 'sixième': 6,
            'septième': 7, 'huitième': 8, 'neuvième': 9, 'dixième': 10}
HISTORICAL = re.compile(r"rédaction|antérieur|ancien|abrog|avant (?:son|leur|la|le)|demeure|transitoire|en vigueur avant|issu", re.I)


def plist(xml):
    return [plain(x) for x in re.split(r'<br\s*/?>|</p>|\n', xml or '') if plain(x)]


def shifted(ordinal, source, proposal):
    """The cited paragraph of the proposal no longer carries the cited paragraph of the source."""
    import difflib
    a, b = plist(source), plist(proposal)
    word = ordinal.split()[0].lower()
    if word in ('dernier', 'avant-dernier'):
        k = -1 if word == 'dernier' else -2
        if len(a) < -k or len(b) < -k:
            return False
        sa, sb = a[k], b[k]
    else:
        i = ORDINALS.get(word)
        if not i or i > len(a):
            return False
        if i > len(b):
            return True
        sa, sb = a[i - 1], b[i - 1]
    return difflib.SequenceMatcher(None, sa, sb, autojunk=False).ratio() < 0.5


def historical_context(text, ref):
    """The reference sits in a historical or transitional phrase (e.g. "dans sa rédaction antérieure")."""
    for m in re.finditer(re.escape(ref[0]) + r'\.?\s*' + re.escape(ref[1:]) + r'\b', text):
        window = text[max(0, m.start() - 160):m.end() + 160]
        if not HISTORICAL.search(window):
            return False
    return True


def norm(number):
    return re.sub(r'[\s.*]', '', number or '').upper()


def main():
    db = sqlite3.connect(f'file:{PROD}/corpus.sqlite?mode=ro', uri=True)
    db.execute('pragma query_only=1')
    arts = collections.defaultdict(list)          # (code, normalised number) -> versions
    for c, i, n, st, vf, vu, x in db.execute('SELECT code_id,id,number,state,valid_from,valid_until,content_xml FROM articles'):
        arts[(CODES[c], norm(n))].append(dict(id=i, number=n, state=st, vf=vf or '', vu=vu or '', src=x))
    drafts = {(CODES[c], s): (st, p) for c, s, st, p in db.execute('SELECT code_id,source_id,status,proposed_xml FROM drafts')}

    def current(code, num):
        for v in arts.get((code, num), []):
            if v['vf'] <= AS_OF < (v['vu'] or '9999') and v['state'] in ('VIGUEUR', 'ABROGE_DIFF', 'VIGUEUR_DIFF'):
                return v
        return None

    def effective(code, v):
        st, p = drafts.get((code, v['id']), (None, None))
        return plain(p) if p else plain(v['src']), st, p

    repealed = {}                                  # (code, num) -> source_id, for current versions proposed as repealed
    for (code, num), vs in arts.items():
        v = current(code, num)
        if v:
            st, p = drafts.get((code, v['id']), (None, None))
            if p and REPEAL.match(plain(p)):
                repealed[(code, num)] = v['id']

    s1, s2, s3, s4, s5, s7, s8 = [], [], [], [], [], [], []
    names = collections.Counter()
    for (code, num), vs in arts.items():
        v = current(code, num)
        if not v:
            continue
        text, st, p = effective(code, v)
        own_repealed = bool(p) and bool(REPEAL.match(text))
        regulatory = code in CGI_FAMILY - {'cgi'} or num[:1] in 'RDA'
        cited = refs(text)
        scope = [code] if code not in CGI_FAMILY else ['cgi', 'a1', 'a2', 'a3', 'a4']
        for r in cited:
            target = next(((c, r) for c in scope if (c, r) in repealed), None)
            if target and not own_repealed and target != (code, num):
                lead = dict(code=code, number=v['number'], source_id=v['id'], status=st,
                            cites=r, target_code=target[0], target_source_id=repealed[target])
                if regulatory and r[:1] in 'L':
                    s1.append(lead)
                if PENALTY.search(text):
                    s2.append(lead)
            # A number absent from every code of the corpus (references to other codes are excluded).
            if code not in CGI_FAMILY and p and r[:1] in 'LRDA' and not any(arts.get((c, r)) for c in set(CODES.values())) \
                    and not re.search(re.escape(r[0]) + r'\.?\s*' + re.escape(r[1:]) + r"[^.;]{0,80}\b(?:code|loi|ordonnance|décret)\b(?! du travail| de la sécurité sociale| de l'urbanisme| de la construction)", text):
                s3.append(dict(code=code, number=v['number'], source_id=v['id'], cites=r))
        # S8: same-code reference to a number whose versions all ended before the corpus date (and none to come).
        for r in cited:
            vs_r = arts.get((code, r)) if code not in CGI_FAMILY else None
            if vs_r and not any((w['vu'] or '9999') > AS_OF for w in vs_r) and r != num and not own_repealed \
                    and not historical_context(text, r):
                s8.append(dict(code=code, number=v['number'], source_id=v['id'], status=st, cites=r,
                               cited_ended=max(w['vu'] for w in vs_r)))
        # S7: "<ordinal> alinéa de l'article X" where X's proposal changes its paragraph count.
        for m in ALINEA.finditer(text):
            r = norm(m.group(2))
            tv = current(code, r) if code not in CGI_FAMILY else None
            if tv:
                tp = drafts.get((code, tv['id']), (None, None))[1]
                if tp and shifted(m.group(1), tv['src'], tp):
                    s7.append(dict(code=code, number=v['number'], source_id=v['id'], status=st, phrase=m.group(0)[:120],
                                   target=tv['number'], target_source_id=tv['id'],
                                   paragraphs_source=paragraphs(tv['src']), paragraphs_proposal=paragraphs(tp)))
        if p and FALSE_DEFERRAL.search(text):
            nxt = sorted((w for w in vs if w['vf'] >= (v['vu'] or '9999')), key=lambda w: w['vf'])
            if nxt and not REPEAL.match(plain(nxt[0]['src'])):
                s4.append(dict(code=code, number=v['number'], source_id=v['id'], successor=nxt[0]['id'], successor_from=nxt[0]['vf'],
                               successor_has_proposal=bool(drafts.get((code, nxt[0]['id']), (None, None))[1])))
        if p and st == 'rewrite_draft' and v['vu'] and v['vu'] < '2999':
            nxt = sorted((w for w in vs if w['vf'] >= v['vu']), key=lambda w: w['vf'])
            if nxt and not drafts.get((code, nxt[0]['id']), (None, None))[1] and not REPEAL.match(plain(nxt[0]['src'])):
                s5.append(dict(code=code, number=v['number'], source_id=v['id'], successor=nxt[0]['id'], successor_from=nxt[0]['vf']))
        if p:
            for m in REFORM_LAW.findall(text):
                names[re.sub(r'\s+', ' ', m.lower())[:70]] += 1
    out = dict(read_from='production', as_of=AS_OF,
               S1_formality_kept_by_regulation=s1, S2_orphan_penalty=s2, S3_unknown_reference=s3,
               S4_false_deferral_claim=s4, S5_successor_without_proposal=s5,
               S6_reform_law_names=names.most_common(60),
               S7_paragraph_reference_shifted=s7, S8_reference_to_long_repealed=s8)
    dest = HOME / 'audit/sweeps'; dest.mkdir(parents=True, exist_ok=True)
    (dest / 'candidates.json').write_text(json.dumps(out, ensure_ascii=False, indent=1))
    for k, v in out.items():
        if isinstance(v, list):
            print(k, len(v), collections.Counter(x['code'] for x in v if isinstance(x, dict)).most_common() if v and isinstance(v[0], dict) else '')
    print('repealed current articles', len(repealed))


if __name__ == '__main__':
    main()
