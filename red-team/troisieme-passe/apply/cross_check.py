#!/usr/bin/env python3
"""List every article touched by more than one group, and every pending cross-group request.

Usage: python3 -B apply/cross_check.py [GROUP ...]   (default: every apply/<GROUP>/changes.json)
"""
import collections, json, sys
from pathlib import Path

HOME = Path(__file__).resolve().parent
groups = sys.argv[1:] or sorted(p.parent.name for p in HOME.glob('*/changes.json'))
touch = collections.defaultdict(list)
requests = []
for g in groups:
    spec = json.loads((HOME / g / 'changes.json').read_text())
    for c in spec['changes']:
        touch[f"{c['code_id']}|{c['source_id']}"].append((g, c.get('objection'), c['mode']))
    for r in spec.get('requests') or []:
        requests.append(dict(r, from_group=g))
dups = {k: v for k, v in touch.items() if len({g.rstrip('abcdefghijklmnopqrstuvwxyz') for g, _, _ in v}) > 1}
print(json.dumps(dict(groups=groups, articles=len(touch), touched_by_several_groups=dups,
                      requests=[{k: r.get(k) for k in ('from_group', 'owner_group', 'code_id', 'source_id', 'objection')} for r in requests]),
                 ensure_ascii=False, indent=1))
