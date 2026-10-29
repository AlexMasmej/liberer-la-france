"""Re-examination rounds of the diff review, applied in order.

Each round compares two snapshots; its verdicts live in reports/<dir>/<GROUP>.json, with optional
merges and closures in reports/<dir>/merges.json. A round whose `new` is None runs against
snapshots/LATEST. New findings of a round get the dossier `<prefix>-<GROUP>`.
"""
import json
from pathlib import Path

HOME = Path(__file__).resolve().parent.parent
INITIAL = '20261026T230545Z'
ROUNDS = [dict(dir='reexam', old='20261026T230545Z', new='20261027T044303Z', prefix='RX', label='intermédiaire'),
          dict(dir='reexam-final', old='20261027T044303Z', new=None, prefix='RXF', label='final')]


def latest():
    return (HOME / 'snapshots/LATEST').read_text().strip()


def active():
    """Rounds whose output directory holds at least one verdict file, with `new` resolved."""
    out = []
    for r in ROUNDS:
        files = verdict_files(r)
        if files:
            out.append(dict(r, new=r['new'] or latest(), files=files))
    return out


def verdict_files(r):
    d = HOME / 'reports' / r['dir']
    if not d.is_dir():
        return []
    return [f for f in sorted(d.glob('*.json')) if not f.name.startswith('packet') and f.name != 'merges.json']


def merges(r):
    f = HOME / 'reports' / r['dir'] / 'merges.json'
    return json.loads(f.read_text()) if f.exists() else dict(merges={}, closures={})
