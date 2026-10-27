#!/usr/bin/env python3
"""Export the full record of articles from the latest snapshot into evidence/cited/ and print it.

Usage: cite.py <code> <number-or-LEGIARTI> [...]   code: css cgi travail urba cch a1 a2 a3 a4
Every version of the number is exported (in-force and historical), with source XML,
NOTA, bounds, state, proposal, reason, review notes, owner row and inventory entry.
"""
import html, json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from corpus import connect, digest, nota, owners, row_digest

CODES = dict(cgi='LEGITEXT000006069577', a1='LEGITEXT000006069568', a2='LEGITEXT000006069569',
             a3='LEGITEXT000006069574', a4='LEGITEXT000006069576', travail='LEGITEXT000006072050',
             css='LEGITEXT000006073189', urba='LEGITEXT000006074075', cch='LEGITEXT000006074096')
HOME = Path(__file__).resolve().parent.parent
SNAP = HOME / 'snapshots' / (HOME / 'snapshots' / 'LATEST').read_text().strip()


def plain(x):
    x = re.sub(r'<br\s*/?>|</p>|</li>|</tr>', '\n', x or '')
    x = re.sub(r'</t[dh]>', ' | ', x)
    return html.unescape(re.sub(r'<[^>]+>', '', x)).strip()


def main(code, refs, quiet=False):
    code_id = CODES[code]
    db = connect(SNAP)
    own, _ = owners(SNAP)
    inv = json.load(open(SNAP / 'runtime/radical-review-20261019.json'))
    entries = {f"{a['code_id']}|{a['source_id']}": a
               for a in inv['prior_articles'] + inv['documentary_holds'] + inv['historical_outside_current_inventory']}
    out_dir = HOME / 'evidence' / 'cited' / SNAP.name
    out_dir.mkdir(parents=True, exist_ok=True)
    for ref in refs:
        q = 'id=?' if ref.startswith('LEGIARTI') else 'number=?'
        rows = db.execute(f'select id,number,state,valid_from,valid_until,content_xml,source_sha256 '
                          f'from articles where code_id=? and {q} order by valid_from', (code_id, ref)).fetchall()
        if not rows:
            print('NOT FOUND', code, ref); continue
        for vid, number, state, vf, vu, xml, ssha in rows:
            key = f'{code_id}|{vid}'
            doc = db.execute("select xml,sha256 from documents where code_id=? and id=? and kind='ARTICLE'",
                             (code_id, vid)).fetchone()
            d = db.execute('select source_sha256,status,proposed_xml,reason,review_notes from drafts '
                           'where code_id=? and source_id=?', (code_id, vid)).fetchone()
            o = own.get(key)
            notes = nota(doc[0]) if doc else ''
            rec = dict(snapshot=SNAP.name, code=code, code_id=code_id, source_id=vid, number=number,
                       state=state, valid_from=vf, valid_until=vu, source_sha256=ssha,
                       source_xml=xml, source_xml_sha256=digest(xml), nota=notes, nota_sha256=digest(notes),
                       document_xml=doc[0].decode() if doc and isinstance(doc[0], bytes) else (doc[0] if doc else None),
                       document_sha256=doc[1] if doc else None,
                       draft=None if d is None else dict(source_sha256=d[0], status=d[1], proposed_xml=d[2],
                                                         proposed_sha256=digest(d[2]) if d[2] is not None else None,
                                                         reason=d[3], reason_sha256=digest(d[3]),
                                                         review_notes=d[4], review_notes_sha256=digest(d[4])),
                       owner=None if o is None else dict(path=o[0], index=o[1], row_sha256=row_digest(o[2]),
                                                         row={k: v for k, v in o[2].items()
                                                              if k not in ('proposed_xml', 'reason', 'review_notes')}),
                       inventory=entries.get(key, {}).get('review_status', 'not_in_inventory'))
            path = out_dir / f'{code}_{number.replace(" ", "_").replace("/", "-")}_{vid}.json'
            path.write_text(json.dumps(rec, ensure_ascii=False, indent=1))
            if quiet:
                print(path.name); continue
            print('=' * 100)
            print(f'{code} {number} {vid} state={state} {vf}→{vu} inventory={rec["inventory"]} '
                  f'owner={rec["owner"] and rec["owner"]["path"]}')
            print('--- SOURCE'); print(plain(xml))
            if notes:
                print('--- NOTA'); print(plain(notes))
            if d:
                print(f'--- DRAFT status={d[1]}'); print(plain(d[2]) if d[2] else '(no proposed body)')
                print('--- REASON'); print(d[3])
                print('--- REVIEW NOTES'); print(d[4])
            print('--- saved', path)


if __name__ == '__main__':
    args = sys.argv[1:]
    quiet = '-q' in args
    args = [a for a in args if a != '-q']
    main(args[0], args[1:], quiet)
