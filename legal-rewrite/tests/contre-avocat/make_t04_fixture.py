"""Régénère la référence figée de travail-04 (v8) au snapshot cac48419 : toutes les entrées de trav/ et trav2/, quel que soit
leur statut, tous les champs de proposition. Sorties : travail_04_baseline_sentences.json ({source_id: [phrases normalisées]})
et travail_04_baseline_ids.json. À ne lancer que sur le snapshot de référence."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from common import *
from t04_patterns import introduced_sentences, proposals, FIXTURE
src = {r[0]: r[1] for r in db().execute("select id,plain_text from articles where code_id=?", (CT,))}
FX = {}
for e in load():
    for p in proposals(e):
        ss = introduced_sentences(txt(p).replace('’', "'"), src.get(e.get('source_id'), ''))
        if ss: FX.setdefault(e['source_id'], [])
        for x in ss:
            if x not in FX[e['source_id']]: FX[e['source_id']].append(x)
H = os.path.dirname(os.path.abspath(__file__))
json.dump(FX, open(os.path.join(H, FIXTURE), 'w'), ensure_ascii=False, indent=0)
json.dump(sorted(FX), open(os.path.join(H, 'travail_04_baseline_ids.json'), 'w'))
print(len(FX), sum(map(len, FX.values())))
