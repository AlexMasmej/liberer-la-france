#!/usr/bin/env python3
"""Build and validate a group's proposed corrections against production, read-only.

Usage: python3 -B apply/check_changes.py <GROUP>
Reads apply/<GROUP>/changes.json, builds the complete batch rows exactly as the coordinator's applier
will (existing batch row + new texts + overrides, impact certificate refreshed), runs the project's own
batch validator on them in a temporary folder, and writes apply/<GROUP>/rows.built.json.
Nothing is written to production.

changes.json:
{"group": "A1",
 "changes": [{"objection": "RT-...", "code_id": "LEGITEXT...", "source_id": "LEGIARTI...",
              "mode": "replace" | "new",
              "proposed_xml": "<p>full article</p>", "reason": "full text", "review_notes": "full text",
              "overrides": {"change_type": "...", "removed_provisions": [...], "repeal_policy_id": "...",
                            "repeal_scope": "...", "reform_policy_id": "...", "substantive_impact": {...}}}],
 "requests": [{"code_id": ..., "source_id": ..., "owner_group": ..., "objection": ..., "requested_change": "..."}],
 "skipped": [{"objection": "RT-...", "decision": "arbitrage|non aligné|pièce manquante|hors corpus|déjà réglé", "why": "..."}]}
"""
import copy, hashlib, json, sqlite3, sys, tempfile
from pathlib import Path

PROD = Path('/Users/alexandremasmejean/.codex/.chatgpt-projects/g-p-6ad59c015c308191aa21cba63c71a6dc/legal-rewrite')
HOME = Path(__file__).resolve().parent
sys.path.insert(0, str(PROD))
import register_batches as rb  # noqa: E402
import substantive_impact as impact_audit  # noqa: E402
from review_prior import batch_owners  # noqa: E402

TEXT_FIELDS = ('proposed_xml', 'reason', 'review_notes')


def digest(v):
    return hashlib.sha256((v or '').encode()).hexdigest()


def build(group):
    spec = json.loads((HOME / group / 'changes.json').read_text())
    assignment = json.loads((HOME / 'assignment.json').read_text())
    db = sqlite3.connect(f'file:{PROD}/corpus.sqlite?mode=ro', uri=True)
    db.execute('pragma query_only=1')
    keys = {(c['code_id'], c['source_id']) for c in spec['changes']}
    owners, files = batch_owners(keys)
    rows, problems, seen = [], [], set()
    for c in spec['changes']:
        key = (c['code_id'], c['source_id'])
        k = '|'.join(key)
        tag = f"{c.get('objection')} {k}"
        if key in seen:
            problems.append(f'{tag}: article modifié deux fois dans le groupe ; fusionner les changements'); continue
        seen.add(key)
        own = assignment['owner'].get(k)
        # A variant folder (e.g. "A7b") belongs to its base group ("A7").
        if own and own != group.rstrip('abcdefghijklmnopqrstuvwxyz'):
            problems.append(f'{tag}: article attribué au groupe {own} ; le passer en « requests »'); continue
        art = db.execute('SELECT number,source_sha256 FROM articles WHERE code_id=? AND id=?', key).fetchone()
        if not art:
            problems.append(f'{tag}: version inconnue'); continue
        draft = db.execute('SELECT status FROM drafts WHERE code_id=? AND source_id=?', key).fetchone()
        if c['mode'] == 'replace':
            if key not in owners:
                problems.append(f'{tag}: aucune ligne de lot existante ; utiliser mode "new" seulement si la base n’a pas de brouillon'); continue
            path, index = owners[key]
            row = copy.deepcopy(files[path][index])
        elif c['mode'] == 'new':
            if draft is not None or key in owners:
                problems.append(f'{tag}: un brouillon existe déjà ; utiliser mode "replace"'); continue
            row = dict(code_id=key[0], source_id=key[1], source_sha256=art[1], number=art[0], status='rewrite_draft')
        else:
            problems.append(f'{tag}: mode inconnu'); continue
        for f in TEXT_FIELDS:
            if not isinstance(c.get(f), str) or not c[f].strip():
                problems.append(f'{tag}: champ {f} manquant (texte complet attendu)'); break
            row[f] = c[f]
        else:
            row.update(c.get('overrides') or {})
            row['third_pass_correction'] = dict(objection=c.get('objection'), applied_by='troisième passe (red-team indépendante)')
            if row.get('substantive_impact_certificate') and row.get('substantive_impact'):
                row['substantive_impact_certificate'] = dict(row['substantive_impact_certificate'],
                    proposed_sha256=digest(row['proposed_xml']),
                    assessment_sha256=impact_audit.assessment_digest(row['substantive_impact']))
            rows.append(dict(mode=c['mode'], objection=c.get('objection'), row=row))
    # The project's own validator, on the built rows only, in a temporary batch folder.
    validated = 0
    for item in rows:
        with tempfile.TemporaryDirectory() as tmp:
            # The validator resolves the registry and the author policy under its HERE: point it at a
            # temporary root that links to the production files, so nothing is written in production.
            root = Path(tmp)
            for name in ('registered-batches.json', 'policy-coordinations.json'):
                (root / name).symlink_to(PROD / name)
            folder = root / 'batches' / 'check'; folder.mkdir(parents=True)
            (folder / '00001.json').write_text(json.dumps([item['row']], ensure_ascii=False))
            here = rb.HERE
            try:
                rb.HERE = root
                _, diagnostics, _ = rb.validate_batches(db, root / 'batches')
                item['diagnostics'] = diagnostics
                validated += 1
            except Exception as e:  # report every refusal, keep going
                problems.append(f"{item['objection']} {item['row']['code_id']}|{item['row']['source_id']}: refusé par le validateur : {e}")
                item['error'] = str(e)
            finally:
                rb.HERE = here
    (HOME / group / 'rows.built.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1))
    print(json.dumps(dict(group=group, changes=len(spec['changes']), built=len(rows), validated=validated,
                          requests=len(spec.get('requests') or []), skipped=len(spec.get('skipped') or []),
                          problems=problems), ensure_ascii=False, indent=1))
    return not problems


if __name__ == '__main__':
    sys.exit(0 if build(sys.argv[1]) else 1)
