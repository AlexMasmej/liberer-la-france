#!/usr/bin/env python3
"""Mechanical re-qualification of the 25 October audit's P1 findings against the current snapshot.

Only sorts findings; it never concludes on legal coherence. Buckets:
  target_no_longer_repealed  current target proposal no longer opens with a repeal formula
  reference_gone             referrer field changed and the cited number no longer appears in it
  live                       target still repealed and the reference still present (or field unchanged)
Usage: p1_triage.py   (uses snapshots/LATEST and evidence/sealed audit)
"""
import collections, html, json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from corpus import connect, digest

HOME = Path(__file__).resolve().parent.parent
SNAP = HOME / 'snapshots' / (HOME / 'snapshots' / 'LATEST').read_text().strip()
AUDIT = HOME / 'evidence/sealed/runtime/global-reference-audit-20261025T2341Z'


def plain(x):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', x or ''))).strip()


def repeal(markup):  # same explicit-formula rule as the audit (global_reference_audit.repeal_proposed)
    return bool(re.match(r'(?:(?:Le\s+)?pr[ée]sent\s+article\s+est\s+)?abrog[ée]\b', plain(markup), re.I))


db = connect(SNAP)
drafts = {f'{c}|{i}': (sh, st, p) for c, i, sh, st, p in
          db.execute('select code_id,source_id,source_sha256,status,proposed_xml from drafts')}
arts = {f'{c}|{i}': (n, sh, x) for c, i, n, sh, x in
        db.execute('select code_id,id,number,source_sha256,content_xml from articles')}

p1 = [json.loads(l) for l in open(AUDIT / 'findings.jsonl') if '"priority": 1,' in l]
p1 = [f for f in p1 if f['priority'] == 1]
out, buckets = [], collections.Counter()
for f in p1:
    key, tkey, field = f['source_key'], f.get('target_key'), f['evidence']['field']
    ref = f['evidence']['reference']
    d = drafts.get(key)
    t = drafts.get(tkey) if tkey else None
    g = f['source_guard']
    cur_status = d[1] if d else None
    cur_prop = d[2] if d else None
    # Which text carries the reference now?
    if field == 'proposal' or (field == 'source_body' and cur_status == 'rewrite_draft'):
        text, now_field = cur_prop, 'proposal'
        unchanged = field == 'proposal' and digest(cur_prop) == g.get('proposal_sha256')
    else:
        text, now_field = arts.get(key, (None, None, ''))[2], 'source_body'
        unchanged = arts.get(key, (None, None))[1] == g.get('source_sha256')
    num = ref.get('number') or ''
    # The audit normalises numbers ("1406BIS", "1599QUATERA"); the text writes "1406 bis", "1599 quater A".
    # A letter prefix may be followed by a dot in the text ("R. 442-23", "L. 813-5").
    pattern = r'\s*'.join(re.escape(ch) + (r'\.?' if ch.isalpha() and i == 0 else '') for i, ch in enumerate(num))
    present = unchanged or (bool(num) and re.search(r'(?<![\w-])' + pattern + r'(?![\w-])', plain(text), re.I) is not None)
    target_repealed = bool(t and t[2] and repeal(t[2]))
    target_changed = bool(t) and digest(t[2]) != (f.get('target_guard') or {}).get('proposal_sha256')
    if f['kind'] in ('proposal_refers_to_proposed_repeal', 'unrewritten_referrer_to_proposed_repeal') and not target_repealed:
        bucket = 'target_no_longer_repealed'
    elif not present:
        bucket = 'reference_gone'
    else:
        bucket = 'live'
    buckets[(f['kind'], bucket)] += 1
    out.append(dict(finding_id=f['finding_id'], kind=f['kind'], bucket=bucket, source_key=key,
                    number=f['number'], field_at_audit=field, field_now=now_field,
                    referrer_status_now=cur_status, referrer_unchanged=unchanged,
                    cited_number=num, context=ref.get('context'), target_key=tkey,
                    target_number=arts.get(tkey, ('?',))[0] if tkey else None,
                    target_repealed_now=target_repealed, target_proposal_changed=target_changed))

by_target = collections.defaultdict(list)
for o in out:
    if o['bucket'] == 'live':
        by_target[o['target_key']].append(o)
clusters = sorted(({'target_key': k, 'target_number': v[0]['target_number'],
                    'code_id': k.split('|')[0] if k else None, 'findings': v,
                    'referrers': sorted({x['source_key'] for x in v})} for k, v in by_target.items()),
                  key=lambda c: (c['code_id'] or '', -len(c['findings'])))
dest = HOME / 'reports' / f'p1-triage-{SNAP.name}.json'
dest.write_text(json.dumps(dict(snapshot=SNAP.name, audit='global-reference-audit-20261025T2341Z',
                                total=len(p1), buckets={f'{k}|{b}': n for (k, b), n in buckets.items()},
                                live_clusters=clusters, all=out), ensure_ascii=False, indent=1))
print(len(p1), 'P1;', dict(buckets))
print('live clusters', len(clusters), 'live findings', sum(len(c['findings']) for c in clusters),
      'live referrers', len({r for c in clusters for r in c['referrers']}))
print(collections.Counter(c['code_id'] for c in clusters))
print('written', dest)
