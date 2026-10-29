#!/usr/bin/env python3
"""Apply the diff-review verdicts of every round (tools/rounds.py) to reports/register.json.

Run after assemble.py and before build_report.py. Each re-examined objection keeps its initial
priority and status under `initial`, and gets a `reexam` record for its latest round (snapshot,
verdict, trace, revised correction); earlier rounds move to `reexam_history`. New findings are
added with `_dossier = <prefix>-<GROUP>`.
"""
import collections, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from rounds import HOME, INITIAL, active, merges

STATUS = {'résolue': 'résolu', 'obsolète': 'obsolète'}
reg = json.loads((HOME / 'reports/register.json').read_text())
by_id = {o['id']: o for o in reg['objections']}
problems = []
rounds = active()
for rnd in rounds:
    seen = set()
    for f in rnd['files']:
        data = json.loads(f.read_text())
        group = data.get('group') or f.stem
        for v in data.get('objections') or []:
            o = by_id.get(v['id'])
            if o is None:
                problems.append(f'{rnd["dir"]}/{f.name}: objection inconnue {v["id"]}'); continue
            if v['id'] in seen:
                problems.append(f'{rnd["dir"]}/{f.name}: {v["id"]} réexaminée deux fois'); continue
            seen.add(v['id'])
            o.setdefault('initial', dict(priority=o.get('priority'), status=o.get('status'), snapshot=INITIAL))
            if 'reexam' in o:
                o.setdefault('reexam_history', []).append(o['reexam'])
            o['reexam'] = dict(snapshot=rnd['new'], round=rnd['label'], group=group, verdict=v.get('verdict'),
                               trace=v.get('trace'), revised_minimal_correction=v.get('revised_minimal_correction'),
                               articles_read=v.get('articles_read'))
            if v.get('new_priority'):
                o['priority'] = v['new_priority']
            o['status'] = STATUS.get(v.get('verdict')) or v.get('new_status') or o.get('status')
        for n in data.get('new_findings') or []:
            if n.get('id') in by_id:
                problems.append(f'{rnd["dir"]}/{f.name}: identifiant déjà pris {n.get("id")}'); continue
            n['_dossier'] = f'{rnd["prefix"]}-{group}'
            n['reexam'] = dict(snapshot=rnd['new'], round=rnd['label'], group=group, verdict='nouveau')
            reg['objections'].append(n); by_id[n['id']] = n

    extra = merges(rnd)
    for inst, spec in extra.get('merges', {}).items():
        if inst not in by_id or spec['into'] not in by_id:
            problems.append(f'{rnd["dir"]} merges: identifiant inconnu {inst} -> {spec["into"]}'); continue
        by_id[inst]['_merged_into'] = spec['into']
        by_id[inst]['_merge_note'] = spec['note']
    for oid, spec in extra.get('closures', {}).items():
        if oid not in by_id:
            problems.append(f'{rnd["dir"]} closures: identifiant inconnu {oid}'); continue
        by_id[oid]['status'] = spec['status']
        by_id[oid].setdefault('reexam', dict(snapshot=rnd['new'], round=rnd['label']))
        by_id[oid]['reexam'].update(verdict='résolue', trace=spec['trace'])

NOT = {'alerte écartée', 'faux positif'}
kept = [o for o in reg['objections'] if '_merged_into' not in o and o.get('nature') not in NOT
        and o.get('status') not in ('faux positif', 'résolu', 'obsolète')]
reg['summary']['after_reexam'] = dict(
    rounds=[dict(dir=r['dir'], old=r['old'], new=r['new']) for r in rounds], retained=len(kept),
    by_priority_status=collections.Counter(f"{o.get('priority')}|{o.get('status')}" for o in kept),
    verdicts={r['label']: collections.Counter(
        x['verdict'] for o in reg['objections']
        for x in (o.get('reexam_history') or []) + ([o['reexam']] if 'reexam' in o else [])
        if x.get('round', 'intermédiaire') == r['label']) for r in rounds},
    problems=problems)
reg['objections'].sort(key=lambda o: (o.get('priority', 'P9'), o.get('id', '')))
(HOME / 'reports/register.json').write_text(json.dumps(reg, ensure_ascii=False, indent=1, default=dict))
print(json.dumps(reg['summary']['after_reexam'], ensure_ascii=False, indent=1, default=dict))
