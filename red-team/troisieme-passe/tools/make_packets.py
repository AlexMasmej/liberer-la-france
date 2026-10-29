#!/usr/bin/env python3
"""Build the re-examination packets of a diff-review round.

Usage: make_packets.py <old> <new> <out-dir> [objections-per-group]
Needs reports/diff-<old>-<new>.json (diff_review.py), reports/p1-triage-<old>.json and
reports/p1-triage-<new>.json (p1_triage.py), and the register after apply_reexam.py.
Writes <out-dir>/packets.json and one <out-dir>/packet-<GROUP>.json per group: objections with
changed articles (closed ones included, to check that the resolution still holds), the P1 alerts
attached to them whose state changed, and the changed live alerts attached to no objection.
"""
import collections, glob, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from rounds import HOME, active

old, new, out_dir = sys.argv[1:4]
size = int(sys.argv[4]) if len(sys.argv) > 4 else 25
out = HOME / 'reports' / out_dir
out.mkdir(parents=True, exist_ok=True)
a = {x['finding_id']: x for x in json.loads((HOME / f'reports/p1-triage-{old}.json').read_text())['all']}
b = {x['finding_id']: x for x in json.loads((HOME / f'reports/p1-triage-{new}.json').read_text())['all']}
cls = {}
for f in sorted(glob.glob(str(HOME / 'reports/p1-work/*-classification.jsonl'))):
    for line in open(f):
        if line.strip():
            r = json.loads(line); cls[r['finding_id']] = r
for f in [f for rnd in active() for f in rnd['files']]:
    for r in json.loads(f.read_text()).get('alerts') or []:
        cls[r['finding_id']] = r
reg = {o['id']: o for o in json.loads((HOME / 'reports/register.json').read_text())['objections']}
NOT = {'alerte écartée', 'faux positif'}


def ref(i):
    o = reg.get(i)
    while o and o.get('_merged_into'):
        o = reg.get(o['_merged_into'].split()[0])
    return o['id'] if o else None


def live(o):
    return o.get('status') != 'faux positif' and o.get('nature') not in NOT


diff = json.loads((HOME / f'reports/diff-{old}-{new}.json').read_text())
pk = collections.defaultdict(lambda: dict(changed_articles=[], alerts=[]))
for k, v in diff['objections_to_reexamine'].items():
    r = ref(k)
    if r and live(reg[r]):
        pk[r]['changed_articles'] += [dict(c, via=k) for c in v['changed_articles']]
unattached = []
for k in a:
    if a[k]['bucket'] != 'live' or k not in b:
        continue
    moved = b[k]['bucket'] != 'live'
    changed = any(a[k][f] != b[k][f] for f in ('referrer_unchanged', 'target_proposal_changed', 'context'))
    if not (moved or changed):
        continue
    c = cls.get(k, {})
    rec = dict(finding_id=k, before=a[k], after=b[k], classification=c.get('classification'),
               objection_id=c.get('objection_id'), motif=c.get('motif'))
    oid = c.get('objection_id')
    r = ref(oid.split()[0]) if oid else None
    if r and live(reg[r]):
        pk[r]['alerts'].append(rec)
    elif b[k]['bucket'] == 'live':
        unattached.append(rec)
# Live alerts of the new triage never classified (e.g. new findings brought back to life).
fresh = [dict(finding_id=k, before=a.get(k), after=x, classification=None, objection_id=None, motif=None)
         for k, x in b.items() if x['bucket'] == 'live' and k not in cls and (k not in a or a[k]['bucket'] != 'live')]

for i, v in pk.items():
    o = reg[i]
    v.update(id=i, priority=o.get('priority'), status=o.get('status'), dossier=o['_dossier'], nature=o.get('nature'),
             previous_reexam=None if 'reexam' not in o else {k: o['reexam'].get(k) for k in ('snapshot', 'verdict', 'trace')})
objs = sorted(pk.values(), key=lambda v: (v['dossier'], v['id']))
groups, cur = [], []
for v in objs:
    if len(cur) >= size and cur[-1]['dossier'] != v['dossier'] or len(cur) >= size * 1.4:
        groups.append(cur); cur = []
    cur.append(v)
if cur:
    if groups and len(cur) < size // 4:
        groups[-1] += cur
    else:
        groups.append(cur)
names = []
for n, g in enumerate(groups, 1):
    name = f'F{n:02d}'
    names.append(name)
    (out / f'packet-{name}.json').write_text(json.dumps(dict(group=name, objections=g), ensure_ascii=False, indent=1))
alerts = unattached + fresh
for n in range(0, len(alerts), 60):
    name = f'FA{n // 60 + 1:02d}'
    names.append(name)
    (out / f'packet-{name}.json').write_text(json.dumps(dict(group=name, alerts=alerts[n:n + 60]), ensure_ascii=False, indent=1))
added = {k: v for k, v in diff.get('records_added_removed', {}).items()}
(out / 'packets.json').write_text(json.dumps(dict(old=old, new=new, groups=names, objections=objs,
                                                 unattached_alerts=unattached, fresh_alerts=fresh,
                                                 records_added_removed=added), ensure_ascii=False, indent=1))
print('objections', len(objs), collections.Counter(v['priority'] for v in objs),
      'closed among them', sum(1 for v in objs if v['status'] in ('résolu', 'obsolète')))
print('changed articles', sum(len(v['changed_articles']) for v in objs), 'attached alerts', sum(len(v['alerts']) for v in objs),
      'unattached alerts', len(unattached), 'fresh alerts', len(fresh))
for name, g in zip(names, groups):
    print(name, len(g), sorted(collections.Counter(v['dossier'] for v in g).items()))
print('alert packets', [x for x in names if x.startswith('FA')])
