#!/usr/bin/env python3
"""Fourth-round lead families, generalised from the defects of the fourth random audit (read-only).

Usage: python3 -I tools/sweeps4.py   → audit/sweeps/candidates-4.json and a printed summary.
Leads are for qualification, never findings: every one must be read in full.
  S9x  a regulation applying a reduced law still uses the distinctive words of the provisions the law
       removed (word overlap with removed_provisions; widens S9n, which kept a fixed list of
       formality words and missed K011 and K260)                                        (F1, F5)
  S12  a proposal says that another article is (or will be) repealed, while that article's current
       version is ABROGE_DIFF and is replaced by a published VIGUEUR_DIFF version          (F4, K058)
  S13  a reference to "n° de l'article X" where X, as proposed, or its next published version,
       has no item n                                                                       (F3, K299)
  S14  side findings of earlier audits and sweeps (incidental_findings)                    (K098)
  S15  a proposal makes its own effect depend on a future legislative change               (F5, K041)
"""
import collections, glob, html, json, re, sqlite3
from pathlib import Path

PROD = Path('/Users/alexandremasmejean/.codex/.chatgpt-projects/g-p-6ad59c015c308191aa21cba63c71a6dc/legal-rewrite')
HOME = Path(__file__).resolve().parent.parent
CODES = {'LEGITEXT000006069577': 'cgi', 'LEGITEXT000006069568': 'a1', 'LEGITEXT000006069569': 'a2',
         'LEGITEXT000006069574': 'a3', 'LEGITEXT000006069576': 'a4', 'LEGITEXT000006072050': 'travail',
         'LEGITEXT000006073189': 'css', 'LEGITEXT000006074075': 'urba', 'LEGITEXT000006074096': 'cch'}
CGI_FAMILY = {'cgi', 'a1', 'a2', 'a3', 'a4'}
AS_OF = '2026-10-18'
REPEAL = re.compile(r'^\s*(?:\(?Abrog[ée]|Le présent article est abrogé)', re.I)
STOP = set("""article articles alinéa alinéas présent présente code général impôts travail sécurité sociale
urbanisme construction habitation conditions dispositions mentionnés mentionnées mentionné mentionnée prévue
prévues prévus prévu applicable applicables lorsque compter suppression supprimé supprimée supprimés supprimées
retiré retirée retirés retirées abrogé abrogée abrogation ancien ancienne anciens anciennes régime réforme loi décret
leurs elles celles ceux cette entre avant après depuis selon ainsi toute toutes autre autres notamment également
dernier première premier deuxième second seconde troisième faveur favorable personnes personne celui celle
lequel laquelle lesquels desquels auxquels""".split())
LAW_CHANGE = re.compile(r"(?:sous réserve|à compter|dès|jusqu'à)[^.;]{0,40}(?:de l'entrée en vigueur d'une|de la|d'une) (?:modification|coordination|disposition|loi) législative"
                        r"|lorsque l'article L\.\s*[\d-]+[^.;]{0,60}aura été (?:modifié|coordonné)"
                        r"|subordonn\w+ à (?:la|une) (?:modification|coordination) (?:de l'article|législative)"
                        r"|dans l'attente d'une (?:modification|coordination) législative", re.I)
ITEM_REF = re.compile(r"\b(\d{1,2})°((?:\s*(?:,|et|ou|à)\s*\d{1,2}°)*)\s+(?:du [IVX]+ |de l'alinéa [^,;]{0,20} )?de l'article ((?:LO|L|R\*?|D|A)\.?\s*\d{1,5}(?:-\d+){1,4})\b")


def plain(x):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', x or ''))).strip()


def norm(number):
    return re.sub(r'[\s.*]', '', number or '').upper()


def words(text):
    return {w for w in re.findall(r"[a-zàâçéèêëîïôûùüÿœ]{7,}", text.lower()) if w not in STOP}


def items(text):
    """Item numbers (1°, 2°…) that open a paragraph."""
    return {int(n) for n in re.findall(r'(?:^|<br\s*/?>|<p>|\n)\s*(\d{1,2})°', text or '')}


def main():
    db = sqlite3.connect(f'file:{PROD}/corpus.sqlite?mode=ro', uri=True)
    db.execute('pragma query_only=1')
    arts = collections.defaultdict(list)
    byid = {}
    for c, i, n, st, vf, vu, x in db.execute('SELECT code_id,id,number,state,valid_from,valid_until,content_xml FROM articles'):
        v = dict(id=i, code=CODES[c], number=n, state=st, vf=vf or '', vu=vu or '', src=x)
        arts[(CODES[c], norm(n))].append(v); byid[(CODES[c], i)] = v
    drafts = {(CODES[c], s): (st, p) for c, s, st, p in db.execute('SELECT code_id,source_id,status,proposed_xml FROM drafts')}

    def current(code, num):
        for v in arts.get((code, num), []):
            if v['vf'] <= AS_OF < (v['vu'] or '9999') and v['state'] in ('VIGUEUR', 'ABROGE_DIFF', 'VIGUEUR_DIFF'):
                return v
        return None

    def successor(code, v):
        nxt = sorted((w for w in arts[(code, norm(v['number']))] if v['vu'] and w['vf'] >= v['vu']), key=lambda w: w['vf'])
        return nxt[0] if nxt else None

    removed = {}
    for f in glob.glob(f'{PROD}/batches/*/*.json'):
        if not re.fullmatch(r'(?:batch)?\d+\.json', f.split('/')[-1]):
            continue
        for r in json.load(open(f)):
            if r.get('change_type') == 'normative_reduction' and r.get('removed_provisions'):
                removed[r['source_id']] = ' '.join(r['removed_provisions'])

    # S9x: unswept S9 leads whose regulation shares distinctive words with what the law removed.
    cand = json.loads((HOME / 'audit/sweeps/candidates.json').read_text())
    swept = {a['key'].split('|')[1] for f in glob.glob(str(HOME / 'audit/sweeps/packet-[WY]*.json'))
             for a in json.load(open(f))['articles']}
    s9x = []
    for x in cand['S9_regulation_of_reduced_law']:
        rem = removed.get(x['target_source_id'])
        if not rem or x['source_id'] in swept:
            continue
        st, p = drafts.get((x['code'], x['source_id']), (None, None))
        text = plain(p) if p else plain(byid.get((x['code'], x['source_id']), {}).get('src'))
        if REPEAL.match(text):
            continue
        shared = sorted(words(rem) & words(text))
        if len(shared) >= 3:
            s9x.append(dict(x, shared_words=shared[:12], score=len(shared)))
    s9x.sort(key=lambda x: -x['score'])

    s12, s13, s15 = [], [], []
    seen13 = set()
    for (code, num), vs in arts.items():
        v = current(code, num)
        if not v:
            continue
        st, p = drafts.get((code, v['id']), (None, None))
        if not p:
            continue
        text = plain(p)
        if REPEAL.match(text):
            continue
        scope = [code] if code not in CGI_FAMILY else ['a1', 'a2', 'a3', 'a4']
        # S12
        seen12 = set()
        for a in re.finditer(r'abrog', text, re.I):
            sent = text[max(0, a.start() - 220):a.end() + 120]
            for m in re.finditer(r'\b(?:LO|L|R\*?|D|A)\.?\s*\d{1,5}(?:-\d+){1,4}\b', sent):
                r = norm(m.group(0))
                for c in scope:
                    t = current(c, r)
                    if not t or t['state'] != 'ABROGE_DIFF' or (c, r) == (code, num):
                        continue
                    nx = successor(c, t)
                    tp = drafts.get((c, t['id']), (None, None))[1]
                    if nx and not REPEAL.match(plain(nx['src'])) and not (tp and REPEAL.match(plain(tp))) and t['id'] not in seen12:
                        seen12.add(t['id'])
                        s12.append(dict(code=code, number=v['number'], source_id=v['id'], status=st, cites=t['number'],
                                        cited_source_id=t['id'], cited_successor=nx['id'], successor_from=nx['vf'],
                                        sentence=sent[:300]))
        # S13
        for m in ITEM_REF.finditer(text):
            nums = {int(m.group(1))} | {int(n) for n in re.findall(r'\d{1,2}', m.group(2))}
            r = norm(m.group(3))
            window = text[max(0, m.start() - 120):m.end() + 120]
            if re.search(r'ancien|rédaction (?:antérieure|applicable)|issu', window, re.I):
                continue
            for c in scope:
                t = current(c, r)
                if not t:
                    continue
                tp = drafts.get((c, t['id']), (None, None))[1]
                have = items(tp or t['src'])
                nx = successor(c, t)
                have_next = items(nx['src']) if nx and nx['vf'] < '2028' and not drafts.get((c, nx['id']), (None, None))[1] else None
                missing = sorted(n for n in nums if have and n not in have)
                missing_next = sorted(n for n in nums if have_next and n not in have_next)
                if (missing or missing_next) and (v['id'], t['id'], m.group(0)) not in seen13:
                    seen13.add((v['id'], t['id'], m.group(0)))
                    s13.append(dict(code=code, number=v['number'], source_id=v['id'], status=st, phrase=m.group(0)[:140],
                                    target=t['number'], target_source_id=t['id'], items_now=sorted(have),
                                    missing_now=missing, next_version=nx['id'] if missing_next else None,
                                    next_from=nx['vf'] if missing_next else None, missing_next=missing_next))
                break
        # S15
        if LAW_CHANGE.search(text):
            s15.append(dict(code=code, number=v['number'], source_id=v['id'], status=st,
                            phrase=LAW_CHANGE.search(text).group(0)[:200]))

    # S14: side findings recorded by earlier audits and sweeps.
    s14 = []
    for f in sorted(glob.glob(str(HOME / 'audit/[UVQK]??.json')) + glob.glob(str(HOME / 'audit/sweeps/[WY]??*.json'))):
        if 'packet' in f:
            continue
        d = json.load(open(f))
        for a in d.get('articles', []) + d.get('leads', []):
            for x in a.get('incidental_findings') or []:
                s14.append(dict(found_in=Path(f).name, while_reading=a.get('number') or a.get('key'), finding=x))
        for x in d.get('incidental_findings') or []:
            s14.append(dict(found_in=Path(f).name, finding=x))

    out = dict(read_from='production', as_of=AS_OF, S9x_regulation_uses_removed_words=s9x,
               S12_false_repeal_of_other_article=s12, S13_missing_item_reference=s13,
               S14_incidental_findings=s14, S15_effect_depends_on_future_law=s15)
    (HOME / 'audit/sweeps/candidates-4.json').write_text(json.dumps(out, ensure_ascii=False, indent=1))
    for k, v in out.items():
        if isinstance(v, list):
            print(k, len(v), collections.Counter(x.get('code', '?') for x in v).most_common())


if __name__ == '__main__':
    main()
