#!/usr/bin/env python3
"""Generate reports/REGISTRE.md and reports/CORRECTIONS.md from reports/register.json.

The synthesis (reports/RAPPORT.md) is written by hand; this only renders the register.
"""
import collections, json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from rounds import INITIAL, active

HOME = Path(__file__).resolve().parent.parent
reg = json.loads((HOME / 'reports/register.json').read_text())
objs = reg['objections']
NOT_OBJECTION = {'alerte écartée', 'faux positif'}


CLOSED = {'faux positif', 'résolu', 'obsolète'}
SNAP = (HOME / 'snapshots/LATEST').read_text().strip()


def retained(o):
    return '_merged_into' not in o and o.get('status') not in CLOSED and o.get('nature') not in NOT_OBJECTION


def closed(o):
    return '_merged_into' not in o and o.get('status') in ('résolu', 'obsolète') and o.get('nature') not in NOT_OBJECTION


def arts(o, n=6):
    out = []
    for a in o.get('articles') or []:
        if isinstance(a, dict):
            out.append(f"{a.get('code', '?')} {a.get('number', '?')}")
    s = ', '.join(dict.fromkeys(out))
    parts = s.split(', ')
    return ', '.join(parts[:n]) + (f' (+{len(parts) - n})' if len(parts) > n else '')


def one_line(text, n=260):
    text = re.sub(r'\s+', ' ', str(text or '')).strip()
    return (text[:n] + '…') if len(text) > n else text


def cell(text):
    return one_line(text).replace('|', '/')


order = {'P0': 0, 'P1': 1, 'P2': 2}
kept = sorted((o for o in objs if retained(o)), key=lambda o: (order.get(o.get('priority'), 9), o['_dossier'], o['id']))
merged = [o for o in objs if '_merged_into' in o]
resolved = sorted((o for o in objs if closed(o)), key=lambda o: o['id'])
dismissed = [o for o in objs if '_merged_into' not in o and not retained(o) and not closed(o)]

rounds = active()
final = any(r['label'] == 'final' for r in rounds)
done = ' puis '.join(f"l'instantané {r['label']} `{r['new']}` (`reports/{r['dir']}/`)" for r in rounds)
lines = ['# Registre des objections — troisième passe' + ('' if final else ' (provisoire)'), '',
         f"Établi sur l'instantané `{INITIAL}`, réexaminé sur {done}. {len(kept)} objections retenues · "
         f"{len(resolved)} résolues ou obsolètes depuis · {len(merged)} doublons fusionnés · "
         f"{len(dismissed)} alertes écartées ou faux positifs documentés.", '',
         'La colonne « Réexamen » donne le verdict de la dernière revue des différences qui a touché l’objection, '
         'suivi de « (final) » pour la revue finale : « — » signifie qu’aucun article cité n’a changé ; '
         '« nouveau » marque un constat apparu au réexamen. Une priorité suivie de « ← P1 » a changé.', '',
         'Statuts et priorités tels que qualifiés par les dossiers, après fusion des doublons (`reports/dedupe.json`). '
         'Les preuves, citations et empreintes complètes de chaque objection sont dans `reports/dossiers/<dossier>.json` '
         'et `reports/register.json`. Revue IA, sans validation par un juriste.', '']
c = collections.Counter((o['priority'], o['status']) for o in kept)
lines += ['| Priorité | confirmé | à confirmer | total |', '|---|---|---|---|']
for p in ('P0', 'P1', 'P2'):
    lines.append(f"| {p} | {c[(p, 'confirmé')]} | {c[(p, 'à confirmer')]} | {sum(v for (q, _), v in c.items() if q == p)} |")
lines.append('')
for p in ('P0', 'P1', 'P2'):
    group = [o for o in kept if o.get('priority') == p]
    lines += [f'## {p} — {len(group)} objections', '',
              '| ID | Dossier | Nature | Statut | Réexamen | Articles | Constat |', '|---|---|---|---|---|---|---|']
    for o in group:
        rx = (o.get('reexam') or {}).get('verdict') or '—'
        if (o.get('reexam') or {}).get('round') == 'final':
            rx += ' (final)'
        was = (o.get('initial') or {}).get('priority')
        if was and was != o.get('priority'):
            rx += f' ← {was}'
        lines.append(f"| {o['id']} | {o['_dossier']} | {o.get('nature')} | {o.get('status')} | {rx} | {cell(arts(o))} | "
                     f"{cell(o.get('reasoning'))} |")
    lines.append('')
lines += [f'## Résolues ou obsolètes au réexamen — {len(resolved)}', '',
          '| ID | Priorité initiale | Verdict | Trace |', '|---|---|---|---|']
lines += [f"| {o['id']} | {(o.get('initial') or {}).get('priority')} | {o['reexam']['verdict']} | {cell(o['reexam'].get('trace'))} |"
          for o in resolved]
lines += ['', '## Doublons fusionnés', '', '| ID | Fusionné dans |', '|---|---|']
lines += [f"| {o['id']} | {o['_merged_into']} |" for o in sorted(merged, key=lambda o: o['id'])]
lines += ['', '## Alertes écartées et faux positifs documentés', '', '| ID | Dossier | Motif |', '|---|---|---|']
lines += [f"| {o['id']} | {o['_dossier']} | {cell(o.get('reasoning'), )} |" for o in dismissed]
(HOME / 'reports/REGISTRE.md').write_text('\n'.join(lines) + '\n')

cl = ['# Propositions de correction — séparées des textes courants' + ('' if final else ' (provisoire)'), '',
      'Corrections minimales proposées par objection retenue, P0 puis P1. Les rédactions complètes (articles entiers, '
      'transitions, dépendances) figurent dans le rapport du dossier indiqué (`reports/dossiers/<dossier>.md`, '
      'section « Propositions de correction »). Aucune n\'est appliquée ; chacune doit être confrontée aux empreintes '
      'de la version finale de la seconde passe avant usage.', '']
for o in kept:
    if o.get('priority') not in ('P0', 'P1'):
        continue
    cl += [f"## {o['id']} ({o['priority']}, {o.get('status')}) — {o['_dossier']}", '',
           f"**Articles :** {arts(o, 12)}", '',
           f"**Correction minimale :** {re.sub(r'\s+', ' ', str(o.get('minimal_correction') or '')).strip()}", '']
    rev = (o.get('reexam') or {}).get('revised_minimal_correction')
    if rev:
        cl += [f"**Correction révisée au réexamen ({o['reexam'].get('snapshot') or SNAP}) :** {re.sub(r'\s+', ' ', str(rev)).strip()}", '']
    if o.get('other_options'):
        opts = o['other_options'] if isinstance(o['other_options'], list) else [o['other_options']]
        cl += ['**Autres options :**'] + [f'- {one_line(x, 600)}' for x in opts] + ['']
    if o.get('preserve'):
        pres = o['preserve'] if isinstance(o['preserve'], list) else [o['preserve']]
        cl += ['**À préserver :** ' + '; '.join(one_line(x, 200) for x in pres), '']
(HOME / 'reports/CORRECTIONS.md').write_text('\n'.join(cl) + '\n')
print(len(kept), 'retenues', collections.Counter(o['priority'] for o in kept), len(resolved), 'résolues/obsolètes',
      len(merged), 'fusionnées', len(dismissed), 'écartées')
