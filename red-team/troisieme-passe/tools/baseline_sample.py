#!/usr/bin/env python3
"""Baseline audit of the official law: stratified random sample, same allocation as the six audits (read-only).

Usage: python3 -I tools/baseline_sample.py   → audit/baseline/sample.json and audit/baseline/packet-O01..O10.json
Population: the 30,314 inventory entries (official version in force on 18 October 2026). Strata: code × level
(statute or regulation), allocation max(6, round(309 × stratum / N)). Seed 20261104. The previous samples are
not excluded: this audit reads the official text, not the proposals.
"""
import collections, json, random, re, sqlite3
from pathlib import Path

PROD = Path('/Users/alexandremasmejean/.codex/.chatgpt-projects/g-p-6ad59c015c308191aa21cba63c71a6dc/legal-rewrite')
HOME = Path(__file__).resolve().parent.parent
CODES = {'LEGITEXT000006069577': 'cgi', 'LEGITEXT000006069568': 'a1', 'LEGITEXT000006069569': 'a2',
         'LEGITEXT000006069574': 'a3', 'LEGITEXT000006069576': 'a4', 'LEGITEXT000006072050': 'travail',
         'LEGITEXT000006073189': 'css', 'LEGITEXT000006074075': 'urba', 'LEGITEXT000006074096': 'cch'}
SEED = 20261104


def level(code, number):
    if code == 'cgi':
        return 'legislatif'
    if code in ('a1', 'a2', 'a3', 'a4'):
        return 'reglementaire'
    return 'legislatif' if re.match(r'\s*L', number) else 'reglementaire'


def main():
    db = sqlite3.connect(f'file:{PROD}/corpus.sqlite?mode=ro', uri=True)
    db.execute('pragma query_only=1')
    inv = json.loads((PROD / 'runtime/radical-review-20261019.json').read_text())['prior_articles']
    strata = collections.defaultdict(list)
    for a in inv:
        n = db.execute('SELECT number FROM articles WHERE code_id=? AND id=?', (a['code_id'], a['source_id'])).fetchone()[0]
        code = CODES[a['code_id']]
        strata[(code, level(code, n))].append(dict(code=code, level=level(code, n), code_id=a['code_id'],
                                                   source_id=a['source_id'], number=n))
    N = sum(len(v) for v in strata.values())
    rng = random.Random(SEED)
    sample = []
    for key in sorted(strata):
        pop = sorted(strata[key], key=lambda x: x['source_id'])
        k = max(6, round(309 * len(pop) / N))
        for x in rng.sample(pop, k):
            sample.append(dict(x, stratum_size=len(pop), stratum_sample=k))
    rng.shuffle(sample)
    for i, x in enumerate(sample, 1):
        x['sample_id'] = f'O{i:03d}'
    out = HOME / 'audit/baseline'
    out.mkdir(exist_ok=True)
    (out / 'sample.json').write_text(json.dumps(dict(seed=SEED, population=N, method=(
        'Audit de référence du droit officiel : même tirage stratifié et même allocation que les six audits, '
        'texte officiel en vigueur au 18 octobre 2026, propositions du projet masquées.'), sample=sample),
        ensure_ascii=False, indent=1))
    for g in range(10):
        part = sample[g::10]
        (out / f'packet-O{g + 1:02d}.json').write_text(json.dumps(dict(group=f'O{g + 1:02d}', articles=part), ensure_ascii=False, indent=1))
    print(N, len(sample), collections.Counter((x['code'], x['level']) for x in sample).most_common())
    print({k: len(v) for k, v in sorted(strata.items())})


if __name__ == '__main__':
    main()
