"""v9 : voir introduced_sentences (comparaison de phrases).
Motifs partagés par travail_04.py et derive_numbers.py (règles d'application dans le temps), v8.
v8 : sosies cyrilliques/grecs repliés en latin ; détection sur le texte entier aplati (ponctuation retirée), donc insensible
  aux coupures « entrée en. vigueur » ; formes faibles : marqueur temporel dans la phrase (élargie si un fragment voisin fait < 4 mots) ;
  « conclu » et « jusqu' » ne sont plus des marqueurs temporels seuls (seulement « conclus avant/après/à compter », « jusqu'à la date/au terme/… »).
- Normalisation Unicode : NFKC, suppression des caractères invisibles (U+200B–U+200F, U+2060, U+FEFF, U+00AD),
  espaces insécables/fines -> espace, apostrophes typographiques -> ', minuscules, espaces repliés.
- Analyse phrase par phrase. Formes fortes : toujours comptées. Formes faibles (« demeure(nt)/reste(nt)/continue(nt) …
  applicable(s)/régi(e)s/soumis(es)/de s'appliquer ») : comptées seulement si la même phrase contient un marqueur temporel (TIME).
- Une forme n'est « introduite » que si elle est absente du plain_text source de la même entrée."""
import re, unicodedata
INVIS = re.compile('[\u200b-\u200f\u2060-\u2064\ufeff\u00ad\u180e]')
# Sosies cyrilliques/grecs -> latin (sous-ensemble UTS #39 utile au français) ; toute autre lettre non latine restante est signalée par nonlatin().
HOMO = str.maketrans({'а':'a','в':'b','е':'e','ё':'e','к':'k','м':'m','н':'h','о':'o','р':'p','с':'c','т':'t','у':'y','х':'x','і':'i','ї':'i','ј':'j','ѕ':'s','ԁ':'d','ԛ':'q','ԝ':'w','ɡ':'g',
  'А':'a','В':'b','Е':'e','К':'k','М':'m','Н':'h','О':'o','Р':'p','С':'c','Т':'t','У':'y','Х':'x','І':'i','Ј':'j','Ѕ':'s',
  'α':'a','β':'b','ε':'e','ι':'i','κ':'k','ν':'v','ο':'o','ρ':'p','τ':'t','υ':'u','χ':'x','ω':'w','Α':'a','Β':'b','Ε':'e','Ζ':'z','Η':'h','Ι':'i','Κ':'k','Μ':'m','Ν':'n','Ο':'o','Ρ':'p','Τ':'t','Υ':'y','Χ':'x'})
NONLATIN = re.compile(r'[^\W\d_a-zA-Z\u00c0-\u024f\u1e00-\u1eff]')
def nonlatin(s): return NONLATIN.findall(unicodedata.normalize('NFKC', s or ''))
def norm(s):
    s = unicodedata.normalize('NFKC', s or '')
    s = INVIS.sub('', s)
    s = s.translate(HOMO)
    s = unicodedata.normalize('NFC', s)
    s = re.sub(r'[\u00a0\u202f\u2007\u2009\u200a]', ' ', s)
    s = s.replace('’', "'").replace('‘', "'").replace('ʼ', "'").lower()
    return re.sub(r'\s+', ' ', s).strip()
STRONG = re.compile(r"(?:"
    r"entrée en vigueur|prise d'effet|date d'effet|prend(?:ra|ront)? effet|produit (?:ses|son) effets?"
    r"|(?:à compter|à partir) (?:de l'entrée|de la publication|de la promulgation|de (?:cette|la|leur|sa) date|du \d+\w*|du 1er|de l'année|du lendemain|de la prise d'effet)"
    r"|\bdès (?:l'entrée|la publication|la promulgation|cette date|la date|la prise d'effet)"
    r"|à la date (?:de (?:la )?(?:publication|promulgation)|d'entrée|de prise d'effet|de cette loi|de la loi|de la réforme)"
    r"|\b(?:avant|après|antérieurement à|postérieurement à) (?:la|cette|leur|sa) date"
    r"|\b(?:avant|après) (?:l'entrée|la publication|la promulgation|la prise d'effet|la réforme)"
    r"|contrats? (?:conclus?|signés?|souscrits?|formés?|passés?|en cours|antérieurs?|postérieurs?|antérieurement \w+|existants?)(?: (?:avant|après|à compter|jusqu'))?"
    r"|conventions? (?:conclues?|signées?|formées?) (?:avant|après|antérieurement)"
    r"|jusqu'(?:à (?:cette|la|leur) date|au terme (?:du|des) contrats?|à l'expiration (?:du|des) contrats?|à leur terme|alors)"
    r"|dispositions? transitoires?|régime transitoire|à titre transitoire|période transitoire"
    r"|\bauparavant\b|\bantérieurement\b|ancien régime|régime antérieur|régime ancien|rédaction antérieure|rédaction en vigueur avant|dans sa rédaction antérieure"
    r"|situations? (?:en cours|nées? avant|acquises? avant)|effets? antérieurs?"
    r")")
WEAK = re.compile(r"\b(?:demeure|demeurent|reste|restent|continue|continuent) (?:d'être |à être )?(?:régi|soumis|applicables?|de s'appliquer|à s'appliquer|valables?|en vigueur)\w*")
TIME = re.compile(r"(?<!quelle que soit la )(?<!quelle que soit leur )\bdates?\b|vigueur|\bavant\b|\baprès\b|antérieur|postérieur|\bconclus?e?s? (?:avant|après|à compter|antérieurement|postérieurement)|\bsigné|en cours|\bdéjà\b|auparavant|\bancien|jusqu'(?:à |au |aux )?(?:la |l'|leur |cette |son |sa )?(?:date|terme|expiration|échéance|entrée|publication|promulgation|\d|1er|fin du contrat|fin des contrats)|désormais|publication|promulgation|prise d'effet|\bréforme\b|\bnouveau régime\b")
SPLIT = re.compile(r"(?<=[.;!?])(?<!\.\.\.)(?<!\b[lrd]\.)(?<!\bart\.)(?<!\bal\.)\s+")  # pas de coupure après « … » (v9 : « loi n° … du … ») ni après « l. », « r. », « d. », « art. », « al. »
def sentences(s): return [x for x in SPLIT.split(norm(s)) if x]
PUNCT = re.compile(r"[.;:!?,()\[\]«»\"“”/\-–—…*_]+")
def flat(x): return re.sub(r'\s+', ' ', PUNCT.sub(' ', x)).strip()
def _spans(s):
    """Texte entier aplati (ponctuation retirée, donc « entrée en. vigueur » = « entrée en vigueur ») + bornes de chaque phrase."""
    ss = sentences(s); parts = []; pos = 0; bounds = []
    for x in ss:
        f = flat(x); bounds.append((pos, pos + len(f))); parts.append(f); pos += len(f) + 1
    return ss, ' '.join(parts), bounds
def _matches(F, B=None):
    """Formes fortes : texte entier aplati. Formes faibles : marqueur temporel dans la ou les phrases que la forme chevauche,
    élargies aux phrases voisines quand l'une d'elles fait moins de 4 mots (coupure artificielle « demeurent. applicables »)."""
    out = [(m.start(), m.end(), m.group(0).strip()) for m in STRONG.finditer(F)]
    B = B or [(0, len(F))]
    for m in WEAK.finditer(F):
        idx = [i for i, (x, y) in enumerate(B) if x < m.end() and m.start() < y] or [0]
        lo, hi = min(idx), max(idx)
        while lo > 0 and (len(F[B[lo-1][0]:B[lo-1][1]].split()) < 4 or len(F[B[lo][0]:B[lo][1]].split()) < 4): lo -= 1
        while hi < len(B) - 1 and (len(F[B[hi+1][0]:B[hi+1][1]].split()) < 4 or len(F[B[hi][0]:B[hi][1]].split()) < 4): hi += 1
        if TIME.search(F[B[lo][0]:B[hi][1]]): out.append((m.start(), m.end(), m.group(0).strip()))
    return out
def sent_hits(x): return {h for _, _, h in _matches(flat(norm(x)))}
def hits(s):
    _, F, B = _spans(s); return {h for _, _, h in _matches(F, B)}
# v9 : comparaison de PHRASES, pas de types de forme. Une phrase (normalisée, aplatie) d'une proposition est « introduite »
# si elle contient une forme temporelle (forte, ou faible avec marqueur) et n'est pas, à l'identique, une phrase du plain_text
# source de la même entrée. Un hôte dont la source contient déjà « entrée en vigueur » n'absorbe donc plus de nouvelles clauses.
# Seule exception (v10) : UNE phrase de renvoi par proposition, de forme exacte, sans texte libre :
# « Les dispositions transitoires figurent à l'article <n> de la loi n° AAAA-N du <jour> <mois> AAAA. »
# (comparée sur le texte normalisé et aplati : tirets et point final retirés).
MOIS = r"(?:janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)"
XREF = re.compile(r"^les dispositions transitoires figurent à l'article (?:\d+(?: \d+)?|premier|1er) de la loi n° \d{4} \d+ du (?:1er|[1-9]|[12]\d|3[01]) " + MOIS + r" \d{4}$")
def is_xref(x):
    return bool(XREF.match(flat(norm(x))))
def src_sentences(source): return {flat(x) for x in sentences(source)}
def introduced_sentences(prop, source):
    ss, F, B = _spans(prop); keep = set()
    for a, b, h in _matches(F, B):
        for i, (x, y) in enumerate(B):
            if x < b and a < y: keep.add(i)
    S = src_sentences(source); out = []; xref_used = False
    for i in sorted(keep):
        f = flat(ss[i])
        if f in S: continue
        if not xref_used and is_xref(ss[i]): xref_used = True; continue
        out.append(ss[i])
    return out
def introduced(prop, source): return introduced_sentences(prop, source)
TRANSITION_FILE = 'legal-rewrite/transition/loi-contrat-unique.json'  # chemin relatif à la racine du dépôt
FIXTURE = 'travail_04_baseline_sentences.json'  # {source_id: [phrases introduites normalisées]} au snapshot cac48419
def proposals(e):
    """Tous les champs de proposition d'une entrée (proposed_xml et tout autre champ texte « propos* », hors empreintes)."""
    return [v for k, v in e.items() if 'propos' in k.lower() and 'sha' not in k.lower() and isinstance(v, str) and v.strip()]
