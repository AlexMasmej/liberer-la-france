import sys, os, re, json, csv, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from common import *
A = load(); c = db()
def one(n): r = by_number(A, n); return r[0] if r else {}
t = T('travail-02')
p = P(one('L1234-1'))
t.check("C1a L1234-1 ne contient plus « indépendamment de son ancienneté »", 'indépendamment de son ancienneté' not in p)
new = p.split('Pour les contrats conclus avant')[0]
t.check("C1b régime des contrats nouveaux de L1234-1 : « un mois » lié à une ancienneté ≤ 1 an (ou 6 mois) et « deux mois » lié à ≤ 2 ans",
        re.search(r"(six mois|un an).{0,120}un mois|un mois.{0,120}(six mois|un an)", new) and re.search(r"deux ans.{0,120}deux mois|deux mois.{0,120}deux ans", new))
t.check("C2 L1234-8 ne contient plus « aucune durée d'ancienneté n'est exigée »", "aucune durée d'ancienneté n'est exigée" not in P(one('L1234-8')))
for n in ('L2253-3', 'L2254-1'):
    q = P(one(n)); bad = [s for s in ('durée impérative du préavis', 'préavis impératif', 'ne transforme pas le préavis') if s in q]
    t.check(f"C3 {n} ne contient aucune de « durée impérative du préavis », « préavis impératif », « ne transforme pas le préavis »", not bad, ', '.join(bad))
rc = J(one('L1234-1').get('reference_checks'))
t.check("C4 reference_checks de L1234-1 contient « Charte sociale européenne » et « C158 »", 'Charte sociale européenne' in rc and 'C158' in rc)
t.done()
