#!/usr/bin/env python3
"""Stratum-weighted defect rate of a random audit, with a 95 % interval (read-only).

Usage: python3 -I tools/audit_rate.py <sample.json> <verdict files...>
Rate = Σ_h (N_h/N) p_h ; variance = Σ_h (N_h/N)² p_h (1 − p_h) / n_h, with N_h the stratum size and n_h the
number of articles read in it.
"""
import collections, json, math, sys


def rate(sample, verdicts, keep):
    strata = {}
    for x in sample:
        strata[(x['code'], x['level'])] = x['stratum_size']
    read = collections.defaultdict(lambda: [0, 0])
    level = {x['sample_id']: (x['code'], x['level']) for x in sample}
    for sid, v in verdicts.items():
        h = level[sid]
        read[h][0] += 1
        read[h][1] += v in keep
    N = sum(strata.values())
    p = sum(strata[h] / N * k / n for h, (n, k) in read.items())
    var = sum((strata[h] / N) ** 2 * (k / n) * (1 - k / n) / n for h, (n, k) in read.items() if n)
    return 100 * p, 196 * math.sqrt(var)


def main():
    sample = json.load(open(sys.argv[1]))['sample']
    verdicts = {}
    for f in sys.argv[2:]:
        for a in json.load(open(f))['articles']:
            verdicts[a['sample_id']] = a['verdict']
    c = collections.Counter(verdicts.values())
    g, gi = rate(sample, verdicts, {'G'})
    gm, gmi = rate(sample, verdicts, {'G', 'm'})
    print(f'read {len(verdicts)}/{len(sample)}  G {c["G"]}  m {c["m"]}  0 {c["0"]}  '
          f'G rate {g:.1f} % ± {gi:.1f}  G+m {gm:.1f} % ± {gmi:.1f}')


if __name__ == '__main__':
    main()
