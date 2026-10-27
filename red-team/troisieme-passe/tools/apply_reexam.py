#!/usr/bin/env python3
"""Apply the diff-review verdicts (reports/reexam/<GROUP>.json) to reports/register.json.

Run after assemble.py and before build_report.py. Each re-examined objection keeps its initial
priority and status under `initial`, and gets a `reexam` record (snapshot, verdict, trace,
revised correction). New findings from the re-examination are added with `_dossier = RX-<GROUP>`.
"""
import collections, json
from pathlib import Path

HOME = Path(__file__).resolve().parent.parent
NEW = (HOME / 'snapshots/LATEST').read_text().strip()
STATUS = {'résolue': 'résolu', 'obsolète': 'obsolète'}
reg = json.loads((HOME / 'reports/register.json').read_text())
by_id = {o['id']: o for o in reg['objections']}
problems = []
for f in sorted((HOME / 'reports/reexam').glob('*.json')):
    if f.name.startswith('packet') or f.name == 'merges.json':
        continue
    data = json.loads(f.read_text())
    group = data.get('group') or f.stem
    for v in data.get('objections') or []:
        o = by_id.get(v['id'])
        if o is None:
            problems.append(f'{f.name}: objection inconnue {v["id"]}'); continue
        if 'reexam' in o:
            problems.append(f'{f.name}: {v["id"]} réexaminée deux fois'); continue
        o['initial'] = dict(priority=o.get('priority'), status=o.get('status'), snapshot='20261026T230545Z')
        o['reexam'] = dict(snapshot=NEW, group=group, verdict=v.get('verdict'), trace=v.get('trace'),
                           revised_minimal_correction=v.get('revised_minimal_correction'),
                           articles_read=v.get('articles_read'))
        if v.get('new_priority'):
            o['priority'] = v['new_priority']
        o['status'] = STATUS.get(v.get('verdict')) or v.get('new_status') or o.get('status')
    for n in data.get('new_findings') or []:
        if n.get('id') in by_id:
            problems.append(f'{f.name}: identifiant déjà pris {n.get("id")}'); continue
        n['_dossier'] = f'RX-{group}'
        n['reexam'] = dict(snapshot=NEW, group=group, verdict='nouveau')
        reg['objections'].append(n); by_id[n['id']] = n

extra = json.loads((HOME / 'reports/reexam/merges.json').read_text())
for inst, spec in extra['merges'].items():
    if inst not in by_id or spec['into'] not in by_id:
        problems.append(f'merges: identifiant inconnu {inst} -> {spec["into"]}'); continue
    by_id[inst]['_merged_into'] = spec['into']
    by_id[inst]['_merge_note'] = spec['note']
for oid, spec in extra['closures'].items():
    if oid not in by_id:
        problems.append(f'closures: identifiant inconnu {oid}'); continue
    by_id[oid]['status'] = spec['status']
    by_id[oid]['reexam'].update(verdict='résolue', trace=spec['trace'])

NOT = {'alerte écartée', 'faux positif'}
kept = [o for o in reg['objections'] if '_merged_into' not in o and o.get('nature') not in NOT
        and o.get('status') not in ('faux positif', 'résolu', 'obsolète')]
reg['summary']['after_reexam'] = dict(
    snapshot=NEW, retained=len(kept),
    by_priority_status=collections.Counter(f"{o.get('priority')}|{o.get('status')}" for o in kept),
    verdicts=collections.Counter(o['reexam']['verdict'] for o in reg['objections'] if 'reexam' in o),
    problems=problems)
reg['objections'].sort(key=lambda o: (o.get('priority', 'P9'), o.get('id', '')))
(HOME / 'reports/register.json').write_text(json.dumps(reg, ensure_ascii=False, indent=1, default=dict))
print(json.dumps(reg['summary']['after_reexam'], ensure_ascii=False, indent=1, default=dict))
