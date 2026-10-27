import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from common import *
# v10 : C6 (plafond de longueur) retiré — choix de politique rédactionnelle, hors périmètre ; XREF à forme exacte.
# v9 : C1 compare des phrases (t04_patterns.introduced_sentences) ; C2 n'excepte qu'une phrase identique dans la source de l'entrée hôte ; C6 plafond dur par entrée.
# v8 : C1 et C2 portent sur trav/ (batches/automatic-travail) ET trav2/ (batches/travail), toutes entrées, tout statut, tout champ de proposition.
A = load(); c = db()
t = T('travail-04')
auto = [e for e in A if e['_file'].startswith('trav/')]
src = {r[0]: r[1] for r in c.execute("select id,plain_text from articles where code_id=?", (CT,))}
RW = [e for e in auto if e.get('status') == 'rewrite_draft']
from t04_patterns import introduced, src_sentences, norm, flat, nonlatin, proposals, TRANSITION_FILE, FIXTURE
FX = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), FIXTURE)))
def PT(x): return txt(x).replace('’', "'")
S_ = lambda e: src.get(e.get('source_id'), '')
bad = []; nl = []; ru = []
for e in A:
    for p in proposals(e):
        q = PT(p)
        if introduced(q, S_(e)): bad.append(e)
        if set(nonlatin(q)) - set(nonlatin(S_(e))): nl.append(e)
        if e.get('status') == 'retained_unchanged' and norm(q) != norm(S_(e)): ru.append(e)
withp = sum(1 for e in A if proposals(e))
t.check("C1 aucune proposition (trav/ + trav2/, tout statut, tout champ propos*) n'introduit de clause temporelle/transitoire absente du plain_text source "
        "(t04_patterns v8 : NFKC, invisibles retirés, sosies cyrilliques/grecs repliés, texte aplati sans ponctuation) ; aucune lettre non latine introduite ; "
        "aucune entrée retained_unchanged ne porte une proposition différente de sa source",
        not (bad or nl or ru), f"{len({id(e) for e in bad})}/{withp} entrées à clause introduite, {len(nl)} à lettres non latines, {len(ru)} retained_unchanged modifiées")
tf = os.path.join(ROOT, TRANSITION_FILE)  # aucun override par variable d'environnement
try:
    TF = json.load(open(tf)); TF = TF.get('rules', TF) if isinstance(TF, dict) else TF
    assert isinstance(TF, list)
except Exception: TF = None
# Toute phrase de référence (aplatie) encore présente dans une proposition de trav/ ou trav2/, sauf si l'entrée qui la porte
# a exactement cette phrase (normalisée, aplatie) dans son propre plain_text en vigueur. Partager des formes ne suffit plus.
# Index : pour chaque entrée, les phrases (aplaties) de ses propositions qui ne sont PAS à l'identique une phrase de son propre
# plain_text en vigueur. Une phrase de référence « subsiste » si elle est contenue dans l'une d'elles.
from t04_patterns import sentences as _sents
_pool = []
for e in A:
    _S = src_sentences(S_(e))
    for p in proposals(e):
        _pool.extend(f for f in (flat(x) for x in _sents(PT(p))) if f not in _S)
blob = '\n'.join(_pool)
def _left(s, owner):
    fs = flat(s); return bool(fs) and fs in blob
left = sum(1 for o, ss in FX.items() for s in ss if _left(s, o))
nfx = sum(map(len, FX.values()))
lab = f"C2 {TRANSITION_FILE} contient, pour chacun des {len(FX)} source_id de référence, toutes ses phrases transitoires d'origine (normalisées) ; aucune règle sans phrase d'origine ; aucune phrase de référence ne subsiste dans trav/ ou trav2/"
if TF is None:
    t.check(lab, False, f"fichier absent ou illisible ; {left}/{nfx} phrases encore dans les lots")
else:
    rules = {}; junk = 0
    for r in TF:
        if not (isinstance(r, dict) and r.get('number') and isinstance(r.get('rule'), str)): junk += 1; continue
        sid = r.get('source_id'); rn = norm(r['rule'])
        if sid not in FX or not any(s in rn for s in FX[sid]): junk += 1; continue
        rules.setdefault(sid, []).append(rn)
    miss = sum(1 for sid, ss in FX.items() for s in ss if not any(s in rn for rn in rules.get(sid, [])))
    t.check(lab, miss == 0 and junk == 0 and left == 0, f"{miss}/{nfx} phrases manquantes, {junk} règles non rattachées, {left}/{nfx} phrases encore dans les lots")
DES = re.compile(r"\bloi (?:portant|instituant|qui|supprimant)[^.,;]{0,60}")
def des(x): return {m.group(0).strip() for m in DES.finditer(norm(x))}
d = {x for e in auto for x in des(P(e)) - des(src.get(e.get('source_id'), ''))}
t.check("C3 la regex /\\bloi (portant|instituant|qui|supprimant)[^.,;]{0,60}/ (texte normalisé) ne trouve aucune désignation introduite", not d, f"{len(d)} désignations distinctes introduites")
fr = [e for e in RW if e.get('change_type') == 'full_repeal']
long_ = [e for e in fr if e.get('proposed_xml') is not None and len(P(e)) > 120]
t.check("C4 toute full_repeal a proposed_xml null ou ≤ 120 caractères", not long_, f"{len(long_)}/{len(fr)}")
sp = sum(len(src[e['source_id']]) for e in fr); pp = sum(len(P(e)) for e in fr)
t.check("C5 total caractères proposed_xml des full_repeal ≤ 10 % du total des sources abrogées", pp <= 0.10 * sp, f"{sp} → {pp}")
t.done()
