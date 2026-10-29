#!/usr/bin/env python3
"""Deliverable D: compare two snapshot manifests and list objections whose articles changed.

Usage: diff_review.py <old-manifest.json> <new-manifest.json>
Writes reports/diff-<old>-<new>.json. Compares source, XML, NOTA, bounds, status, proposal,
reason and review notes per article, and the policy files.
"""
import collections, json, sys
from pathlib import Path

HOME = Path(__file__).resolve().parent.parent
old, new = (json.loads(Path(p).read_text()) for p in sys.argv[1:3])
FIELDS = ['source_sha256', 'source_xml_sha256', 'source_notes_sha256', 'valid_from', 'valid_until', 'state',
          'status', 'proposed_sha256', 'reason_sha256', 'review_notes_sha256', 'second_pass']
changed = {}
for key in set(old['articles']) | set(new['articles']):
    a, b = old['articles'].get(key), new['articles'].get(key)
    if a is None or b is None:
        changed[key] = ['added' if a is None else 'removed']
        continue
    diff = [f for f in FIELDS if f in a and f in b and a[f] != b[f]]
    if diff:
        changed[key] = diff
policy = {k: (old.get('policy_sha256', {}).get(k), v) for k, v in new.get('policy_sha256', {}).items()
          if old.get('policy_sha256', {}).get(k) != v}

reg = json.loads((HOME / 'reports/register.json').read_text())
by_id = {}
codes = dict(cgi='LEGITEXT000006069577', a1='LEGITEXT000006069568', a2='LEGITEXT000006069569',
             a3='LEGITEXT000006069574', a4='LEGITEXT000006069576', travail='LEGITEXT000006072050',
             css='LEGITEXT000006073189', urba='LEGITEXT000006074075', cch='LEGITEXT000006074096')
for o in reg['objections']:
    hits = []
    for a in o.get('articles') or []:
        if not isinstance(a, dict) or not a.get('source_id'):
            continue
        code_id = codes.get(str(a.get('code', '')).lower(), a.get('code_id'))
        key = f"{code_id}|{a['source_id']}"
        if key in changed:
            hits.append(dict(key=key, number=a.get('number'), fields=changed[key]))
    if hits:
        by_id[o['id']] = dict(priority=o.get('priority'), status=o.get('status'), dossier=o['_dossier'],
                              merged_into=o.get('_merged_into'), changed_articles=hits)
out = dict(old=old['snapshot_id'], new=new['snapshot_id'], articles_changed=len(changed),
           field_counts=collections.Counter(f for v in changed.values() for f in v),
           policy_changed=policy,
           records_added_removed={k: v[0] for k, v in changed.items() if v[0] in ('added', 'removed')},
           objections_to_reexamine=by_id)
dest = HOME / 'reports' / f"diff-{old['snapshot_id']}-{new['snapshot_id']}.json"
dest.write_text(json.dumps(out, ensure_ascii=False, indent=1))
print(json.dumps({k: out[k] for k in ('old', 'new', 'articles_changed', 'field_counts', 'policy_changed')},
                 ensure_ascii=False, indent=1))
print('objections à réexaminer :', len(by_id), collections.Counter(v['priority'] for v in by_id.values()))
print('written', dest)
