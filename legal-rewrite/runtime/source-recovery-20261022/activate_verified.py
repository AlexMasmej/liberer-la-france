"""Activate reviewed documentary companions; never register a legal draft."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import fcntl
import hashlib
import json
import sqlite3
import sys

HERE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(HERE))
from automatic_parallelism import atomic
from ingest import source_notes
from source_assets import asset_path, graphic_markers, load_companions, recovery_complete


def sha(value):
    return hashlib.sha256(value.encode() if isinstance(value, str) else value).hexdigest()


def check_source(db, record, captured):
    key = record['code_id'], record['source_id']
    row = db.execute('SELECT content_xml,source_sha256,number FROM articles WHERE code_id=? AND id=?', key).fetchone()
    if row != (captured['source_xml'], captured['source_sha256'], captured['number']):
        raise ValueError('Canonical source differs from the documentary review: ' + key[1])
    notes = source_notes(db, *key)
    if notes != captured['source_notes_xml']:
        raise ValueError('Canonical notes differ from the documentary review: ' + key[1])
    document = db.execute("SELECT xml FROM documents WHERE code_id=? AND id=? AND kind='ARTICLE'", key).fetchone()
    expected_document = captured.get('raw_document_xml', captured.get('source_document_xml'))
    if document is not None and isinstance(document[0], bytes) and isinstance(expected_document, str):
        expected_document = expected_document.encode('utf-8')
    if document is None or document[0] != expected_document:
        raise ValueError('Canonical ARTICLE document differs: ' + key[1])
    if record['source_sha256'] != row[1] or record['expected_markers'] != len(graphic_markers(row[0])):
        raise ValueError('Source fingerprint or omission count differs: ' + key[1])
    if not recovery_complete(row[0], record):
        raise ValueError('Documentary recovery is incomplete: ' + key[1])
    return {'source_sha256': row[1], 'source_body_sha256': sha(row[0]),
            'source_notes_sha256': sha(notes), 'article_document_sha256': sha(document[0])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('candidates', nargs='+', type=Path)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    attachments = HERE / 'attachments'
    load_companions(attachments)
    db = sqlite3.connect((HERE / 'corpus.sqlite').as_uri() + '?mode=ro', uri=True)
    plans = []
    try:
        for candidate in args.candidates:
            candidate = candidate.resolve()
            if not candidate.is_relative_to(Path(__file__).parent):
                raise ValueError('Candidate is outside this recovery dossier')
            root, group = candidate.parents[1], candidate.parents[2]
            record = json.loads(candidate.read_text())
            for flag in ('ready_for_activation', 'documentary_recovery_complete',
                         'official_jo_crosscheck_complete', 'canonical_version_concordance_complete'):
                if record.get(flag) is not True:
                    raise ValueError('Missing reviewed evidence ' + flag + ': ' + candidate.name)
            if not all(m.get('verified_visually') is True for m in record.get('media', [])):
                raise ValueError('Unreviewed original image: ' + candidate.name)
            documents = {d['path'] for d in record.get('documents', [])}
            for transcription in record.get('transcriptions', []):
                literal = transcription.get('verified_visually') is True
                consolidated = (
                    all(transcription.get(k) is True for k in (
                        'verified_against_explicit_primary_chain',
                        'primary_graphic_verified_visually', 'express_amendments_only'))
                    and transcription.get('source_document') in documents
                    and transcription.get('amendment_document') in documents
                    and bool(transcription.get('amendment_locator')))
                if not (literal or consolidated):
                    raise ValueError('Unreviewed transcription or consolidation: ' + candidate.name)
            verified = load_companions(root)[(record['code_id'], record['source_id'])]
            if verified != record:
                raise ValueError('Candidate does not match its verified registry')
            snapshot = json.loads((group / 'source-snapshot.json').read_text())
            rows = snapshot if isinstance(snapshot, list) else snapshot['records']
            captured = next(r for r in rows if (r['code_id'], r['source_id']) == (record['code_id'], record['source_id']))
            guard = check_source(db, record, captured)
            owners = [p for p in (attachments / 'records').glob('*.json')
                      if (lambda d: (d['code_id'], d['source_id']) == (record['code_id'], record['source_id']))(json.loads(p.read_text()))]
            if len(owners) > 1:
                raise ValueError('Duplicate active companion owner')
            target = owners[0] if owners else attachments / 'records' / candidate.name
            assets = []
            for field in ('documents', 'media'):
                for item in record.get(field, []):
                    source = asset_path(item['path'], root)
                    data = source.read_bytes()
                    if sha(data) != item['sha256']:
                        raise ValueError('Reviewed asset changed: ' + item['path'])
                    destination = attachments / item['path']
                    if destination.exists() and sha(destination.read_bytes()) != item['sha256']:
                        raise ValueError('Refusing to replace a different existing asset: ' + item['path'])
                    assets.append((destination, data))
            plans.append((record, captured, guard, target, assets))
        if len({(r['code_id'], r['source_id']) for r, *_ in plans}) != len(plans):
            raise ValueError('Duplicate activation candidate')
        report = {'at_utc': datetime.now(timezone.utc).isoformat(), 'applied': args.apply,
                  'article_drafts_registered': 0, 'canonical_sources_modified': False,
                  'coordinator_restarted': False, 'records': []}
        # Complete assets are installed before exposing their manifest. This
        # file copying does not hold the pipeline writer lock.
        if args.apply:
            for _, _, _, _, assets in plans:
                for destination, data in assets:
                    if destination.exists():
                        continue
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    temporary = destination.with_name(destination.name + '.recovery-tmp')
                    temporary.write_bytes(data)
                    temporary.replace(destination)
        archive = Path(__file__).parent / 'activation-before-images'
        # Documentary-only lock: the six drafting workers never acquire it.
        with (Path(__file__).parent / 'activation.lock').open('a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            for record, captured, guard, target, assets in plans:
                if check_source(db, record, captured) != guard:
                    raise ValueError('Source changed before activation')
                before = target.read_bytes() if target.exists() else None
                previous = json.loads(before) if before is not None else None
                already_active = bool(previous and previous.get('canonical_guard') == guard
                                      and all(previous.get(k) == v for k, v in record.items()))
                item = {'source_id': record['source_id'], 'number': record['number'],
                        'target': str(target), 'guard': guard,
                        'candidate_sha256': sha(json.dumps(record, ensure_ascii=False, sort_keys=True)),
                        'previous_record_sha256': sha(before) if before is not None else None,
                        'already_active': already_active}
                if args.apply and not already_active:
                    archive.mkdir(parents=True, exist_ok=True)
                    archive_name = record['source_id'] + '-' + (sha(before) if before is not None else 'absent') + '.json'
                    if not (archive / archive_name).exists():
                        atomic(archive / archive_name, {'target': str(target), 'previous_record': previous})
                    activated = record | {'documentary_activation': report['at_utc'],
                                          'canonical_guard': guard, 'count_as_completed': False}
                    atomic(target, activated)
                report['records'].append(item)
        if args.apply:
            active = load_companions(attachments)
            for record, captured, *_ in plans:
                if not recovery_complete(captured['source_xml'], active[(record['code_id'], record['source_id'])]):
                    raise ValueError('Post-activation validation failed')
        if args.apply:
            stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
            atomic(Path(__file__).parent / ('activation-' + stamp + '.json'), report)
        atomic(Path(__file__).parent / ('activation.json' if args.apply else 'activation-dry-run.json'), report)
        print(json.dumps(report, ensure_ascii=False, indent=2))
    finally:
        db.close()


if __name__ == '__main__':
    main()
