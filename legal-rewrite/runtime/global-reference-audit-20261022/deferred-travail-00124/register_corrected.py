"""Guarded recovery of a metadata-only correction; no agent is launched."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, copy, hashlib, json, sqlite3, sys

HERE = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(HERE))
import run_exhaustive as runner
import supervise_exhaustive as supervisor
from automatic_parallelism import atomic
from ingest import open_db, source_notes, source_evidence
from register_batches import writer_lock
from worker_execution import requested_execution, verify_execution

FOLDER = Path(__file__).resolve().parent
ORIGINAL = HERE / 'runtime/exhaustive/jobs/travail-00124'


def sha(value):
    return hashlib.sha256(value.encode() if isinstance(value, str) else value).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    sources = json.loads((ORIGINAL / 'source.json').read_text())
    old = json.loads((ORIGINAL / 'answer.json').read_text())
    corrected = json.loads((FOLDER / 'answer.corrected.json').read_text())
    before, after = copy.deepcopy(old), copy.deepcopy(corrected)
    for rows in (before, after):
        rows[21]['substantive_impact'].pop('effects')
    if before != after or len(sources) != 24 or old[21]['number'] != 'L5214-1 B':
        raise ValueError('Correction exceeds its reviewed metadata-only scope')
    if not runner.policy_is_current(ORIGINAL):
        raise ValueError('Policy changed since drafting')
    execution = verify_execution(ORIGINAL, requested_execution(runner.RUNTIME), ORIGINAL / 'errors-3.log')
    if not execution['verified']:
        raise ValueError('Original drafting execution is unverified')
    snapshot = json.loads((ORIGINAL / 'reference-targets.json').read_text())
    validated = runner.validate_answer(copy.deepcopy(corrected), sources)
    runner.reference_audit.accept_checks(validated, sources, snapshot)
    processes = supervisor.processes()
    coordinators = supervisor.coordinator_processes(processes)
    if [c['pid'] for c in coordinators] != [21959] or not supervisor.coordinator_locked():
        raise ValueError('Existing coordinator identity changed')
    writes = {a['code_id'] + '|' + a['source_id'] for a in sources}
    active = supervisor.job_workers(processes)
    for worker in active:
        job = runner.RUNTIME / 'jobs' / worker['job']
        reads = set(json.loads((job / 'reference-targets.json').read_text()).get('targets', {}))
        targets = {a['code_id'] + '|' + a['source_id'] for a in json.loads((job / 'source.json').read_text())}
        if writes & (reads | targets):
            raise ValueError('Active worker currently owns or reads a recovery target: ' + worker['job'])
    batch = HERE / 'batches/automatic-travail/00124.json'
    report = {'checked_at_utc': datetime.now(timezone.utc).isoformat(), 'apply': args.apply,
              'job': ORIGINAL.name, 'correction': 'one impact-effect array; all24 proposed_xml unchanged',
              'new_model_calls': 0, 'worker_limit_changed': False, 'coordinator_restarted': False,
              'original_execution': execution, 'active_dependency_conflicts': [],
              'candidate_sha256': sha((FOLDER / 'answer.corrected.json').read_bytes()),
              'source_file_sha256': sha((ORIGINAL / 'source.json').read_bytes()),
              'reference_file_sha256': sha((ORIGINAL / 'reference-targets.json').read_bytes()),
              'batch_path': str(batch), 'registered': False}
    with writer_lock():
        db = open_db(HERE / 'corpus.sqlite')
        try:
            db.execute('BEGIN IMMEDIATE' if args.apply else 'BEGIN')
            runner.reference_audit.check_guards(db, snapshot)
            if not runner.policy_is_current(ORIGINAL):
                raise ValueError('Policy changed before registration')
            if batch.exists():
                raise ValueError('Batch already exists; reconcile instead of overwriting')
            for article in sources:
                key = article['code_id'], article['source_id']
                actual = db.execute('SELECT source_sha256,content_xml,number FROM articles WHERE code_id=? AND id=?', key).fetchone()
                if actual != (article['source_sha256'], article['source_xml'], article['number']):
                    raise ValueError('Canonical source differs: ' + key[1])
                if source_notes(db, *key) != article['source_notes_xml']:
                    raise ValueError('Canonical application notes differ: ' + key[1])
                if db.execute('SELECT 1 FROM drafts WHERE code_id=? AND source_id=?', key).fetchone():
                    raise ValueError('Refusing to replace any pre-existing draft: ' + key[1])
            if args.apply:
                registry_path = HERE / 'registered-batches.json'
                registry = json.loads(registry_path.read_text())
                for row in validated:
                    key = row['code_id'], row['source_id']
                    source = db.execute('SELECT content_xml,valid_from,valid_until FROM articles WHERE code_id=? AND id=?', key).fetchone()
                    db.execute('INSERT INTO drafts VALUES(?,?,?,?,?,?,?)',
                               (*key, row['source_sha256'], row.get('status', 'rewrite_draft'),
                                row['proposed_xml'], row['reason'], row['review_notes']))
                    db.execute('INSERT INTO draft_sources VALUES(?,?,?,?,?)',
                               (*key, source_evidence(source[0], source_notes(db, *key)), source[1], source[2]))
                    registry['|'.join(key)] = {'source_sha256': row['source_sha256'],
                                               'proposed_sha256': runner.digest(row['proposed_xml'])}
                atomic(FOLDER / 'registration-intent.json', report | {'validated_rows': validated})
                db.commit()
                atomic(batch, validated)
                atomic(registry_path, registry)
                report.update(registered=True, accepted_articles=len(validated))
                atomic(FOLDER / 'registration-complete.json', report)
            else:
                db.rollback()
        except Exception:
            db.rollback()
            raise
        finally:
            db.close()
    atomic(FOLDER / ('adoption.json' if args.apply else 'adoption-dry-run.json'), report)
    if args.apply:
        path = runner.RUNTIME / 'failed-job-resolutions.json'
        resolutions = json.loads(path.read_text()) if path.exists() else []
        resolutions.append({'job': ORIGINAL.name, 'accepted_articles': len(validated),
                            'resolution': str(FOLDER / 'registration-complete.json'),
                            'at_utc': report['checked_at_utc'], 'original_failure_preserved': True})
        atomic(path, resolutions)
    print(json.dumps({k: v for k, v in report.items() if k != 'original_execution'}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
