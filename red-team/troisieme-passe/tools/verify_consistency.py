#!/usr/bin/env python3
"""Inventory reconciliation and DB / owner-batch / inventory-guard consistency on a snapshot.

Reports discrepancies; never repairs anything. Usage: verify_consistency.py <snapshot-dir>
"""
import collections, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from corpus import digest, row_digest, owners, article_states, connect

snap = Path(sys.argv[1]).resolve()
arts, notes, dsrc, drafts = article_states(snap)
own, dup_owners = owners(snap)
inv = json.load(open(snap / 'runtime/radical-review-20261019.json'))
registry = json.load(open(snap / 'registered-batches.json'))
status = json.load(open(snap / 'runtime/exhaustive/status.json'))
codes = json.load(open(snap / 'policy-coordinations.json')).get('scope')

prior = {f"{a['code_id']}|{a['source_id']}": a for a in inv['prior_articles']}
holds = {f"{a['code_id']}|{a['source_id']}": a for a in inv['documentary_holds']}
hist = {f"{a['code_id']}|{a['source_id']}": a for a in inv['historical_outside_current_inventory']}

out = collections.defaultdict(list)
# --- 1. Inventory reconciliation -------------------------------------------------
sets = dict(drafts=set(drafts), prior=set(prior), holds=set(holds), historical=set(hist),
            registry=set(registry), owners=set(own))
recon = {k: len(v) for k, v in sets.items()}
recon['status_source_records'] = status['source_records']
recon['prior_and_holds_disjoint'] = not (sets['prior'] & sets['holds'])
recon['prior_plus_holds'] = len(sets['prior'] | sets['holds'])
recon['drafts_minus_prior'] = sorted(sets['drafts'] - sets['prior'])
recon['prior_minus_drafts'] = sorted(sets['prior'] - sets['drafts'])
recon['holds_in_drafts'] = sorted(sets['holds'] & sets['drafts'])
recon['drafts_not_registered'] = sorted(sets['drafts'] - sets['registry'])
recon['drafts_without_owner'] = sorted(sets['drafts'] - sets['owners'])
recon['owners_without_draft'] = sorted(sets['owners'] - sets['drafts'])
recon['duplicate_owner_rows'] = dup_owners


def bounds(key):
    a = arts.get(key, {})
    return dict(number=a.get('number'), valid_from=a.get('valid_from'),
                valid_until=a.get('valid_until'), state=a.get('state'))


AS_OF = '2026-10-18'


def in_force(key):
    a = arts.get(key)
    if not a:
        return None
    vf, vu = a['valid_from'] or '', a['valid_until'] or '2999-01-01'
    return vf <= AS_OF < vu


recon['outside_prior_detail'] = {k: dict(bounds(k), in_force_2026_10_18=in_force(k),
                                         in_historical_list=k in hist, registered=k in registry,
                                         owner=own.get(k, (None,))[0])
                                 for k in sorted(((sets['drafts'] | sets['holds']) - sets['prior'])
                                                 | set(recon['drafts_not_registered']))}
recon['prior_not_in_force_2026_10_18'] = sorted(k for k in prior if in_force(k) is False)
recon['prior_missing_article'] = sorted(k for k in prior if in_force(k) is None)
recon['state_values_prior'] = collections.Counter(arts.get(k, {}).get('state') for k in prior)
recon['review_status_counts'] = collections.Counter(a['review_status'] for a in prior.values())

# --- 2. DB vs owner batch rows ----------------------------------------------------
for key, (path, index, row) in own.items():
    d = drafts.get(key)
    if d is None:
        continue
    checks = dict(source_sha256=(row['source_sha256'], d['draft_source_sha256']),
                  status=(row.get('status', 'rewrite_draft'), d['status']),
                  proposed=(digest(row.get('proposed_xml')) if row.get('proposed_xml') is not None else None,
                            d['proposed_sha256']),
                  reason=(digest(row.get('reason')), d['reason_sha256']),
                  review_notes=(digest(row.get('review_notes')), d['review_notes_sha256']))
    for field, (a, b) in checks.items():
        if a != b:
            out['db_vs_owner'].append(dict(key=key, owner=path, index=index, field=field))
# DB draft source vs canonical article
for key, d in drafts.items():
    a = arts.get(key)
    if a is None:
        out['draft_without_article'].append(key)
    elif a['source_sha256'] != d['draft_source_sha256']:
        out['draft_source_sha_vs_article'].append(key)
    s = dsrc.get(key)
    if s and a and (s['ds_valid_from'], s['ds_valid_until']) != (a['valid_from'], a['valid_until']):
        out['draft_source_bounds_vs_article'].append(dict(key=key, draft_source=(s['ds_valid_from'], s['ds_valid_until']),
                                                          article=(a['valid_from'], a['valid_until'])))
    if s and a and s['draft_source_xml_sha256'] != a['source_xml_sha256']:
        out['draft_source_xml_vs_article_xml'].append(key)
# registry vs DB
for key, r in registry.items():
    d = drafts.get(key)
    if d and (r['source_sha256'] != d['draft_source_sha256']
              or r['proposed_sha256'] != (d['proposed_sha256'] or digest(None))):
        out['registry_vs_db'].append(key)

# --- 3. Inventory guards vs recomputed state -------------------------------------
for key, entry in prior.items():
    g = entry.get('current_guard') or {}
    d, a, s = drafts.get(key, {}), arts.get(key, {}), dsrc.get(key, {})
    o = own.get(key)
    actual = dict(source_sha256=a.get('source_sha256'), draft_status=d.get('status'),
                  proposed_sha256=d.get('proposed_sha256') or (digest(None) if d else None),
                  reason_sha256=d.get('reason_sha256'), review_notes_sha256=d.get('review_notes_sha256'),
                  source_notes_sha256=notes.get(key, digest('')),
                  valid_from=a.get('valid_from'), valid_until=a.get('valid_until'),
                  owner=o[0] if o else None, batch_row_sha256=row_digest(o[2]) if o else None)
    for field, value in actual.items():
        if field in g and g[field] != value:
            out['guard_mismatch'].append(dict(key=key, field=field, review_status=entry['review_status']))
    if 'source_xml_sha256' in g and g['source_xml_sha256'] not in (a.get('source_xml_sha256'),
                                                                   s.get('draft_source_xml_sha256')):
        out['guard_mismatch'].append(dict(key=key, field='source_xml_sha256', review_status=entry['review_status']))
    for top in ('proposed_sha256', 'reason_sha256', 'review_notes_sha256', 'source_sha256'):
        if top in entry and entry[top] is not None and g.get(top) is not None and entry[top] != g[top]:
            out['entry_vs_own_guard'].append(dict(key=key, field=top, review_status=entry['review_status']))

summary = {k: len(v) for k, v in out.items()}
by_field = collections.Counter((m['field'], m['review_status']) for m in out['guard_mismatch'])
report = dict(snapshot=snap.name, scope=codes, reconciliation=recon, discrepancy_counts=summary,
              guard_mismatch_by_field_and_status={f'{f}|{s}': n for (f, s), n in by_field.items()},
              discrepancies={k: v[:400] for k, v in out.items()},
              truncated={k: len(v) > 400 for k, v in out.items()})
dest = snap.parent.parent / 'reports' / f'consistency-{snap.name}.json'
dest.parent.mkdir(exist_ok=True)
dest.write_text(json.dumps(report, ensure_ascii=False, indent=1, default=list))
print(json.dumps({k: report[k] for k in ('reconciliation', 'discrepancy_counts',
                                         'guard_mismatch_by_field_and_status')},
                 ensure_ascii=False, indent=1, default=list)[:9000])
print('written', dest)
