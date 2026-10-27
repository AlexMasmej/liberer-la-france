"""Read-only helpers over a frozen snapshot (never over production).

Hash conventions are re-implemented independently from the production code
(review_prior.digest / batch_row_sha256, ingest.source_notes) so that the
production guards can be checked rather than trusted.
"""
import hashlib, json, re, sqlite3
import xml.etree.ElementTree as ET
from pathlib import Path


def digest(value):
    return hashlib.sha256((value or '').encode()).hexdigest()


def row_digest(row):
    return digest(json.dumps(row, ensure_ascii=False, sort_keys=True,
                             separators=(',', ':'), allow_nan=False))


def connect(snapshot):
    db = sqlite3.connect((Path(snapshot).resolve() / 'corpus.sqlite').as_uri() + '?mode=ro', uri=True)
    db.execute('pragma query_only=1')
    return db


def nota(xml):
    """Content of NOTA/CONTENU, same extraction rule as ingest.source_notes."""
    if not xml:
        return ''
    root = ET.fromstring(xml)
    content = root.find('NOTA/CONTENU')
    if content is None:
        return ''
    if not ''.join(content.itertext()).strip() and content.find('.//img') is None:
        return ''
    return ((content.text or '') + ''.join(ET.tostring(c, encoding='unicode') for c in content)).strip()


def owners(snapshot):
    """Active owner rows: batches/<dir>/(batch)?NNN.json, as review_prior.batch_owners."""
    result, duplicates = {}, []
    for path in sorted((Path(snapshot) / 'batches').glob('*/*.json')):
        if not re.fullmatch(r'(?:batch)?\d+\.json', path.name):
            continue
        for index, row in enumerate(json.loads(path.read_text())):
            key = f"{row['code_id']}|{row['source_id']}"
            if key in result:
                duplicates.append(key)
            result[key] = (str(path.relative_to(snapshot)), index, row)
    return result, duplicates


def article_states(snapshot):
    """Every hashed element needed for diffing and consistency, keyed code|id."""
    db = connect(snapshot)
    arts = {f'{c}|{i}': dict(number=n, valid_from=vf, valid_until=vu, state=st,
                             source_sha256=sh, source_xml_sha256=digest(x))
            for c, i, n, vf, vu, st, sh, x in db.execute(
                'select code_id,id,number,valid_from,valid_until,state,source_sha256,content_xml from articles')}
    notes = {f'{c}|{i}': digest(nota(x)) for c, i, x in
             db.execute("select code_id,id,xml from documents where kind='ARTICLE'")}
    dsrc = {f'{c}|{i}': dict(draft_source_xml_sha256=digest(x), ds_valid_from=vf, ds_valid_until=vu)
            for c, i, x, vf, vu in db.execute(
                'select code_id,source_id,source_xml,valid_from,valid_until from draft_sources')}
    drafts = {f'{c}|{i}': dict(draft_source_sha256=sh, status=st,
                               proposed_sha256=digest(p) if p is not None else None,
                               reason_sha256=digest(r), review_notes_sha256=digest(n))
              for c, i, sh, st, p, r, n in db.execute(
                  'select code_id,source_id,source_sha256,status,proposed_xml,reason,review_notes from drafts')}
    db.close()
    return arts, notes, dsrc, drafts
