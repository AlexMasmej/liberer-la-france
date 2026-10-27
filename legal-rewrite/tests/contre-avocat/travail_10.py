import sys, os, re, json, csv, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from common import *
A = load(); c = db()
def one(n): r = by_number(A, n); return r[0] if r else {}
t = T('travail-10')
TAB = list(csv.DictReader(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'travail-10-table-transposition.tsv')), delimiter='\t'))
auto = [e for e in A if e['_file'].startswith('trav/')]
def celex(n): return {t_['celex'] for t_ in TAB if re.search(t_['plage_regex_numero'], n)}
inr = [e for e in auto if celex(e['number'])]
miss = [e for e in inr if not (set(re.findall(r'3\d{4}L\d{4}', J(e.get('eu_source')))) & celex(e['number']))]
t.check("C1 les articles de la table ont un champ eu_source contenant le CELEX de leur plage", not miss, f"{len(miss)}/{len(inr)} sans eu_source")
rw = [e for e in inr if e.get('status') == 'rewrite_draft']
miss2 = [e for e in rw if not (set(re.findall(r'3\d{4}L\d{4}', J(e.get('reference_checks')))) & celex(e['number']))]
t.check("C2 les réécrits de la table ont un reference_checks citant ce CELEX", not miss2, f"{len(miss2)}/{len(rw)}")
MIN = {'32003L0088': ('L3121-20', r'quarante-huit heures'), '31998L0059': ('L1233-46', r'autorité administrative')}
def texte(n):  # retained_unchanged : proposed_xml est null, on lit le plain_text source
    e = one(n)
    if e.get('status') == 'retained_unchanged' or e.get('proposed_xml') is None:
        r = c.execute("select plain_text from articles where code_id=? and id=?", (CT, e.get('source_id'))).fetchone()
        return (r[0] if r else '').replace('’', "'")
    return P(e)
bad = [n for cx, (n, rx) in MIN.items() if not re.search(rx, texte(n)) or cx not in (J(one(n).get('reference_checks')) + J(one(n).get('eu_source')))]
t.check("C3 minima témoins : L3121-20 garde « quarante-huit heures », L1233-46 garde « autorité administrative » (plain_text source si retained_unchanged), et chacun cite son CELEX dans reference_checks ou eu_source", not bad, ', '.join(bad))
t.done()
