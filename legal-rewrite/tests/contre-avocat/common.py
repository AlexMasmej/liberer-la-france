"""Chargeur commun : lots du snapshot cac48419 (trav = legal-rewrite/batches/automatic-travail, trav2 = legal-rewrite/batches/travail)
+ base LEGI corpus.sqlite (par défaut legal-rewrite/corpus.sqlite, ou variable d'environnement CONTRE_AVOCAT_CORPUS)."""
import json, glob, re, html, sqlite3, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))  # racine du dépôt
DIRS = {'trav': os.path.join('legal-rewrite', 'batches', 'automatic-travail'), 'trav2': os.path.join('legal-rewrite', 'batches', 'travail')}
CORPUS = os.environ.get('CONTRE_AVOCAT_CORPUS') or os.path.join(ROOT, 'legal-rewrite', 'corpus.sqlite')
CT = 'LEGITEXT000006072050'
def load(dirs=('trav', 'trav2')):
    out = []
    for d in dirs:
        for f in sorted(glob.glob(os.path.join(ROOT, DIRS[d], '*.json'))):
            data = json.load(open(f))
            if isinstance(data, dict): data = data.get('entries', [])
            for e in data:
                e['_file'] = f'{d}/{os.path.basename(f)}'; out.append(e)
    return out
def db():
    return sqlite3.connect(CORPUS)
def txt(x):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', x or ''))).strip()
def by_number(entries, n, rewrite_only=False):
    r = [e for e in entries if e.get('number') == n and (not rewrite_only or e.get('status') == 'rewrite_draft')]
    return r
def P(e): return txt(e.get('proposed_xml')).replace('’', "'") if e else ''  # apostrophes typographiques normalisées
def J(x): return json.dumps(x, ensure_ascii=False) if x is not None else ''
class T:
    def __init__(s, name): s.name, s.res = name, []
    def check(s, label, ok, detail=''):
        s.res.append((label, bool(ok))); print(f"{'PASS' if ok else 'FAIL'}  {label}" + (f"  [{detail}]" if detail else ''))
    def done(s):
        f = sum(1 for _, o in s.res if not o)
        print(f"== {s.name}: {len(s.res)-f}/{len(s.res)} PASS, {f} FAIL -> {'FAIL' if f else 'PASS'}")
        sys.exit(1 if f else 0)
