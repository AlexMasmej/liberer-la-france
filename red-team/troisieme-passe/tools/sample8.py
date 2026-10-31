#!/usr/bin/env python3
"""Eighth audit: a second fresh paired sample (replication of the seventh), read on the rewritten text and on the official text (read-only).

Usage: python3 -I tools/sample7.py   → audit/sample-8.json, audit/packet-S01..S20.json (rewritten text)
       and audit/baseline/packet-OS01..OS20.json (official text, status hidden).
Same strata as the six audits (code × level); allocation doubled for precision: max(12, round(618 × stratum / N)).
The 1,879 articles of the six earlier samples are excluded. Seed 20261105.
"""
import collections, glob, json, random, sqlite3, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from baseline_sample import CODES, PROD, level  # noqa: E402

HOME = Path(__file__).resolve().parent.parent
SEED = 20261106


def main():
    db = sqlite3.connect(f'file:{PROD}/corpus.sqlite?mode=ro', uri=True)
    db.execute('pragma query_only=1')
    inv = json.loads((PROD / 'runtime/radical-review-20261019.json').read_text())['prior_articles']
    seen = set()
    for f in glob.glob(str(HOME / 'audit/sample*.json')):
        seen |= {x['source_id'] for x in json.load(open(f))['sample']}
    strata = collections.defaultdict(list)
    for a in inv:
        n = db.execute('SELECT number FROM articles WHERE code_id=? AND id=?', (a['code_id'], a['source_id'])).fetchone()[0]
        st = db.execute('SELECT status FROM drafts WHERE code_id=? AND source_id=?', (a['code_id'], a['source_id'])).fetchone()
        code = CODES[a['code_id']]
        strata[(code, level(code, n))].append(dict(code=code, level=level(code, n), code_id=a['code_id'],
                                                   source_id=a['source_id'], number=n, status=st[0] if st else None))
    N = sum(len(v) for v in strata.values())
    rng = random.Random(SEED)
    sample = []
    for key in sorted(strata):
        pop = sorted((x for x in strata[key] if x['source_id'] not in seen), key=lambda x: x['source_id'])
        k = max(12, round(618 * len(strata[key]) / N))
        for x in rng.sample(pop, k):
            sample.append(dict(x, stratum_size=len(strata[key]), stratum_sample=k))
    rng.shuffle(sample)
    for i, x in enumerate(sample, 1):
        x['sample_id'] = f'P{i:03d}'
    (HOME / 'audit/sample-8.json').write_text(json.dumps(dict(seed=SEED, population=N, excluded_previous_samples=len(seen), method=(
        'Huitième échantillon, apparié : tirage stratifié frais (allocation doublée), hors des 2 511 articles déjà tirés ; '
        'lu une fois sur le texte réécrit actuel, une fois sur le texte officiel.'), sample=sample), ensure_ascii=False, indent=1))
    for g in range(20):
        part = sample[g::20]
        (HOME / f'audit/packet-P{g + 1:02d}.json').write_text(json.dumps(dict(group=f'P{g + 1:02d}', articles=part), ensure_ascii=False, indent=1))
        hidden = [{k: v for k, v in x.items() if k != 'status'} for x in part]
        (HOME / f'audit/baseline/packet-OP{g + 1:02d}.json').write_text(json.dumps(dict(group=f'OP{g + 1:02d}', paired_with=f'P{g + 1:02d}', articles=hidden), ensure_ascii=False, indent=1))
    print(N, len(seen), len(sample), collections.Counter((x['code'], x['level']) for x in sample).most_common())


if __name__ == '__main__':
    main()
