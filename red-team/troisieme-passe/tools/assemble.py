#!/usr/bin/env python3
"""Merge every reports/dossiers/*.json into one objection register and compute coverage.

Checks: unique ids, required fields, evidence files present; P1 classification coverage
against the triage (every live finding must be classified exactly once).
"""
import collections, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from rounds import active

HOME = Path(__file__).resolve().parent.parent
REQUIRED = ['id', 'priority', 'nature', 'status', 'articles', 'reasoning', 'consequences',
            'minimal_correction', 'preserve', 'uncertainties']
objections, problems = [], []
for f in sorted((HOME / 'reports/dossiers').glob('*.json')):
    try:
        data = json.loads(f.read_text())
    except Exception as e:
        problems.append(f'{f.name}: JSON illisible ({e})'); continue
    items = data if isinstance(data, list) else data.get('objections', [])
    for o in items:
        o['_dossier'] = f.stem
        missing = [k for k in REQUIRED if k not in o]
        if missing:
            problems.append(f"{f.name} {o.get('id')}: champs manquants {missing}")
        for ev in o.get('evidence_files') or []:
            if isinstance(ev, str) and ev.startswith('evidence/') and not (HOME / ev).exists():
                problems.append(f"{f.name} {o.get('id')}: preuve absente {ev}")
        objections.append(o)
dedupe = json.loads((HOME / 'reports/dedupe.json').read_text())
merged = {}
for group, spec in dedupe.items():
    if not isinstance(spec, dict):
        continue
    ref = spec.get('reference') or (group if group.startswith('RT-') else None)
    for inst in (spec.get('instances') or []) + (spec.get('duplicates') or []):
        if inst.startswith('RT-') and ' ' not in inst and ref:
            merged[inst] = ref
ids = {o.get('id') for o in objections}
for inst, ref in merged.items():
    if inst not in ids:
        problems.append(f'dedupe: instance inconnue {inst}')
    if ref not in ids:
        problems.append(f'dedupe: référence inconnue {ref}')
for o in objections:
    if o.get('id') in merged:
        o['_merged_into'] = merged[o['id']]
counted = [o for o in objections if '_merged_into' not in o]
dups = [i for i, n in collections.Counter(o.get('id') for o in objections).items() if n > 1]
if dups:
    problems.append(f'identifiants en double : {dups}')

latest = (HOME / 'snapshots/LATEST').read_text().strip()
triage = json.loads((HOME / 'reports' / f'p1-triage-{latest}.json').read_text())
live = {x['finding_id']: x for x in triage['all'] if x['bucket'] == 'live'}
classified, cls_count = {}, collections.Counter()
for f in sorted((HOME / 'reports/p1-work').glob('*-classification.jsonl')):
    for line in f.read_text().splitlines():
        if line.strip():
            r = json.loads(line)
            if r['finding_id'] in classified:
                problems.append(f"P1 classé deux fois : {r['finding_id']}")
            classified[r['finding_id']] = r
            cls_count[r['classification'].split(' ')[0] if r['classification'].startswith('couvert') else r['classification']] += 1
# Re-qualifications from the diff-review rounds (tools/rounds.py) supersede the earlier line, in round order.
requalified = 0
for f in [f for rnd in active() for f in rnd['files']]:
    for r in json.loads(f.read_text()).get('alerts') or []:
        prev = classified.get(r['finding_id'])
        if prev:
            key = prev['classification'].split(' ')[0] if prev['classification'].startswith('couvert') else prev['classification']
            cls_count[key] -= 1
        classified[r['finding_id']] = dict(r, reexam=f.stem)
        cls_count[r['classification'].split(' ')[0] if r['classification'].startswith('couvert') else r['classification']] += 1
        requalified += 1
unclassified = [k for k in live if k not in classified]

summary = dict(
    objections_raw=len(objections), merged_instances=len(objections) - len(counted),
    objections=len(counted),
    by_priority=collections.Counter(o.get('priority') for o in counted),
    by_priority_status=collections.Counter(f"{o.get('priority')}|{o.get('status')}" for o in counted),
    by_status=collections.Counter(o.get('status') for o in counted),
    by_nature=collections.Counter(o.get('nature') for o in counted),
    by_dossier=collections.Counter(o['_dossier'] for o in counted),
    p1_live=len(live), p1_classified=len([k for k in live if k in classified]),
    p1_unclassified=len(unclassified), p1_classification=cls_count,
    p1_read_in_full=sum(1 for r in classified.values() if r.get('read_in_full')),
    p1_requalified_at_reexam=requalified,
    problems=problems)
(HOME / 'reports/register.json').write_text(json.dumps(
    dict(summary=summary, objections=sorted(objections, key=lambda o: (o.get('priority', 'P9'), o.get('id', '')))),
    ensure_ascii=False, indent=1, default=dict))
print(json.dumps(summary, ensure_ascii=False, indent=1, default=dict))
