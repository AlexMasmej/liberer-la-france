"""Read-only transfer guards, prepared offline; no activation entry point.

These checks establish technical identity and terminal queue disposition only.
They cannot replace the still-missing full registration reconciliation. In
particular, a deferred identity remains pending, and stale legal certificates
are neither refreshed nor accepted here. No locks, models or processes start.
"""
from pathlib import Path
import hashlib
import json
import sqlite3
import stat
import types

REQUIRED_PINS = frozenset((
    'continuation_tail.py', 'review_lane_observation.py', 'review_lanes.py',
    'run_exhaustive.py', 'supervise_exhaustive.py', 'worker_capacity.py',
    'register_batches.py', 'review_prior.py', 'reference_coherence.py',
    'reference_queue.py', 'ingest.py', 'source_assets.py',
    'substantive_impact.py', 'worker_execution.py', 'corpus.json',
    'policy-coordinations.json', 'site-summaries.json',
    'reference-focus-extra.json', 'runtime/exhaustive/model-policy.json'))


class GuardError(RuntimeError):
    pass


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read_regular(path):
    path = Path(path)
    if path.is_symlink() or not path.is_file():
        raise GuardError('Required regular evidence is unknown: ' + str(path))
    if not stat.S_ISREG(path.stat().st_mode):
        raise GuardError('Non-regular evidence: ' + str(path))
    return path.read_bytes()


def document(path):
    data = read_regular(path)
    try:
        return data, json.loads(data)
    except (ValueError, UnicodeError) as error:
        raise GuardError('Malformed evidence: ' + str(path)) from error


def integer(value, name, minimum=0):
    if type(value) is not int or value < minimum:
        raise GuardError('Unknown integer: ' + name)
    return value


def unchanged(records):
    for path, before in records.items():
        if read_regular(path) != before:
            raise GuardError('Evidence changed during collection: ' + str(path))


def verify_pins(root, pins):
    root = Path(root).resolve()
    if not isinstance(pins, dict) or not REQUIRED_PINS <= pins.keys():
        raise GuardError('Code and policy pins are unknown')
    if any(not isinstance(name, str) for name in pins):
        raise GuardError('Invalid pin identity')
    records = root / 'attachments/records'
    if records.is_symlink() or not records.is_dir():
        raise GuardError('Normative companion catalogue is unknown')
    actual_records = {str(p.relative_to(root)) for p in records.glob('*.json')}
    pinned_records = {n for n in pins if n.startswith('attachments/records/')}
    if actual_records != pinned_records:
        raise GuardError('Normative companion catalogue membership changed')
    for name, expected in pins.items():
        if not isinstance(name, str) or not isinstance(expected, str):
            raise GuardError('Invalid pin identity')
        target = root / name
        if (Path(name).is_absolute() or '..' in Path(name).parts
                or not target.resolve().is_relative_to(root) or len(expected) != 64
                or any(c not in '0123456789abcdef' for c in expected)):
            raise GuardError('Invalid pin identity')
        if digest(read_regular(target)) != expected:
            raise GuardError('Code/policy/catalogue pin changed: ' + name)


def terminal_new_queue(root, identity, live_workers, now):
    """Fresh alternative to a stale admission timestamp, using actual files/DB.

    The caller must supply the exact process identity and worker inventory from
    a fresh OS collector. Absence of a worker list is unknown, not an empty list.
    Every scheduled new job needs exactly one terminal metric of the same PID;
    accepted/skipped identities must actually exist under the current source
    hash. Deferred source identities are explicitly returned as still pending.
    """
    root = Path(root).resolve()
    base = root / 'runtime/exhaustive'
    if (root / 'runtime').is_symlink() or base.is_symlink():
        raise GuardError('Runtime identity must not be a symlink')
    if not isinstance(identity, dict):
        raise GuardError('Process identity is unknown')
    pid = integer(identity.get('pid'), 'process PID', 1)
    started = integer(identity.get('started_at_unix'), 'process start', 1)
    if live_workers is None or not isinstance(live_workers, list):
        raise GuardError('Native process inventory is unknown')
    if any(w.get('ppid') != pid or w.get('kind') not in {'new', 'review'}
           for w in live_workers):
        raise GuardError('Foreign or unknown native worker')
    if any(w['kind'] == 'new' for w in live_workers):
        raise GuardError('First-pass native worker remains active')
    stable = {}

    def get(path):
        data, value = document(path)
        stable[Path(path)] = data
        return value

    run = get(base / 'coordinator-run.json')
    ad = get(base / 'admission-status.json')
    plan = get(base / 'queue-admission-plan.json')
    pid_raw = read_regular(base / 'coordinator.pid')
    stable[base / 'coordinator.pid'] = pid_raw
    if pid_raw != str(pid).encode():
        raise GuardError('Coordinator PID file differs')
    if run.get('pid') != pid or run.get('started_at_unix') != started:
        raise GuardError('Observed process and run start disagree')
    if ad.get('coordinator_pid') != pid or plan.get('coordinator_pid') != pid:
        raise GuardError('Queue/admission PID differs')
    stamp = integer(ad.get('updated_at_unix'), 'admission timestamp')
    if not started <= stamp <= now:
        raise GuardError('Admission timestamp is outside this process lifetime')
    for name in ('pending_by_kind', 'reserved_or_running_by_kind', 'admitted_by_kind'):
        values = ad.get(name)
        if not isinstance(values, dict) or set(values) != {'new', 'review'}:
            raise GuardError('Admission counters are unknown: ' + name)
        for role, value in values.items():
            integer(value, name + '.' + role)
    if ad['pending_by_kind']['new'] or ad['reserved_or_running_by_kind']['new']:
        raise GuardError('First-pass queue/reservations are not empty')
    # A review may be validating in the coordinator with no live model process.
    if sum(w['kind'] == 'review' for w in live_workers) > ad['reserved_or_running_by_kind']['review']:
        raise GuardError('Live reviews exceed known reservations')
    queue_name = plan.get('queue_file')
    if queue_name not in {'queue.json', 'mixed-queue.json'}:
        raise GuardError('Current queue identity is unknown')
    queue = get(base / queue_name)
    if not isinstance(queue, list):
        raise GuardError('Current queue is not a complete list')
    scheduled = {}
    all_jobs = set()
    ids_seen = set()
    counts = {'new': 0, 'review': 0}
    for item in queue:
        if not isinstance(item, dict) or type(item.get('review')) is not bool:
            raise GuardError('Unknown queue role')
        slug, index, ids = item.get('slug'), item.get('index'), item.get('source_ids')
        integer(index, 'queue index', 1)
        if not isinstance(slug, str) or not slug or not isinstance(ids, list) or not ids:
            raise GuardError('Malformed complete queue assignment')
        if any(not isinstance(i, str) or not i for i in ids) or len(set(ids)) != len(ids):
            raise GuardError('Duplicate/unknown queue source identity')
        key = (slug, index, item['review'])
        if key in all_jobs:
            raise GuardError('Duplicate queue assignment')
        all_jobs.add(key)
        counts['review' if item['review'] else 'new'] += 1
        if not item['review']:
            if any((slug, i) in ids_seen for i in ids):
                raise GuardError('Duplicate first-pass identity across assignments')
            ids_seen.update((slug, i) for i in ids)
            scheduled[(slug, index)] = ids
    scheduled_counts = plan.get('scheduled_by_kind')
    if not isinstance(scheduled_counts, dict) or set(scheduled_counts) != {'new', 'review'}:
        raise GuardError('Scheduled counts are unknown')
    for role, value in scheduled_counts.items():
        integer(value, 'scheduled.' + role)
    if scheduled_counts != counts:
        raise GuardError('Queue length and scheduled counts disagree')
    if ad['admitted_by_kind']['new'] != len(scheduled):
        raise GuardError('Not all frozen first-pass assignments were admitted')
    metrics_path = base / 'job-metrics.jsonl'
    metrics_raw = read_regular(metrics_path)
    stable[metrics_path] = metrics_raw
    if metrics_raw and not metrics_raw.endswith(b'\n'):
        raise GuardError('Metrics contain an incomplete record')
    terminal = {}
    for line in metrics_raw.splitlines():
        try:
            row = json.loads(line)
        except (ValueError, UnicodeError) as error:
            raise GuardError('Malformed metric record') from error
        if row.get('coordinator_pid') != pid or row.get('kind') != 'new':
            continue
        key = (row.get('slug'), row.get('index'))
        if key not in scheduled or key in terminal:
            raise GuardError('Unscheduled or duplicate terminal first-pass metric')
        if row.get('outcome') not in {'accepted', 'skipped', 'deferred'}:
            raise GuardError('First-pass result is nonterminal or blocked')
        start, end = row.get('started_at_unix'), row.get('finished_at_unix')
        if (type(start) not in (int, float) or type(end) not in (int, float)
                or not started <= start <= end <= now):
            raise GuardError('Metric time is outside this process lifetime')
        terminal[key] = row
    if set(terminal) != set(scheduled):
        raise GuardError('Frozen first-pass queue has no complete terminal accounting')
    config = get(root / 'corpus.json')
    specs = config.get('codes', []) + config.get('annexes', [])
    if any(not isinstance(c, dict) or not isinstance(c.get('slug'), str)
           or not c['slug'] or not isinstance(c.get('id'), str) or not c['id'] for c in specs):
        raise GuardError('Canonical collection identity is malformed')
    code_ids = {c['slug']: c['id'] for c in specs}
    if len(code_ids) != len(specs) or len(code_ids) != 9 or len(set(code_ids.values())) != 9:
        raise GuardError('All nine canonical collection identities are required')
    assigned = {}
    for key, metric in terminal.items():
        if key[0] not in code_ids:
            raise GuardError('Unknown canonical collection in queue')
        assigned[key] = {}
        if metric['outcome'] == 'skipped':
            # The real runner skips before creating a job directory. The DB
            # must still account for every identity in the complete assignment.
            continue
        job_name = metric.get('job')
        prefix = key[0] + '-' + str(key[1]).zfill(5)
        if (not isinstance(job_name, str) or Path(job_name).name != job_name
                or not (job_name == prefix or job_name.startswith(prefix + '-resume-'))):
            raise GuardError('Terminal job folder is not bound to its assignment')
        folder = base / 'jobs' / job_name
        if folder.is_symlink() or not folder.resolve().is_relative_to(base / 'jobs'):
            raise GuardError('Terminal job folder escaped the project')
        source = get(folder / 'source.json')
        integer(metric.get('articles'), 'terminal assigned article count', 1)
        if not isinstance(source, list) or not source or metric.get('articles') != len(source):
            raise GuardError('Terminal job source inventory differs from metrics')
        for article in source:
            if (not isinstance(article, dict) or article.get('code_id') != code_ids[key[0]]
                    or article.get('source_id') not in scheduled[key]
                    or article['source_id'] in assigned[key]
                    or not isinstance(article.get('source_sha256'), str)):
                raise GuardError('Terminal job and frozen queue identities differ')
            assigned[key][article['source_id']] = article['source_sha256']
    db_path = root / 'corpus.sqlite'
    # Check regular-file identity before connecting; mode=ro never creates a DB.
    if db_path.is_symlink() or not db_path.is_file():
        raise GuardError('Canonical database is unknown')
    db = sqlite3.connect(db_path.as_uri() + '?mode=ro', uri=True, timeout=15)
    dispositions = []
    try:
        db.execute('BEGIN')
        for key, ids in sorted(scheduled.items()):
            if key[0] not in code_ids:
                raise GuardError('Unknown canonical collection in queue')
            metric = terminal[key]
            for identifier in ids:
                article_key = (code_ids[key[0]], identifier)
                source = db.execute('SELECT source_sha256 FROM articles WHERE code_id=? AND id=?', article_key).fetchone()
                if not source:
                    raise GuardError('Queued canonical source is missing')
                if identifier in assigned[key] and assigned[key][identifier] != source[0]:
                    raise GuardError('Canonical source changed since the terminal job')
                draft = db.execute('SELECT source_sha256,status,proposed_xml FROM drafts WHERE code_id=? AND source_id=?', article_key).fetchone()
                present = bool(draft and draft[0] == source[0] and (draft[2] or draft[1] == 'retained_unchanged'))
                if not present and (metric['outcome'] != 'deferred' or identifier not in assigned[key]):
                    raise GuardError('Accepted/skipped identity is not actually registered')
                dispositions.append({'code_id': article_key[0], 'source_id': identifier,
                                     'source_sha256': source[0], 'outcome': metric['outcome'],
                                     'current_disposition': 'registered_requires_full_reconciliation' if present else 'deferred_still_pending'})
    finally:
        db.close()
    unchanged(stable)
    return {'coordinator_pid': pid, 'process_started_at_unix': started,
            'observed_at_unix': now, 'terminal_new_jobs': len(terminal),
            'new_processes_and_reservations_zero': True,
            'all_first_passes_complete': False,
            'scope': 'Queue accounting only; full guarded registration reconciliation is still mandatory',
            'dispositions': dispositions,
            'evidence_sha256': {str(p.relative_to(root)): digest(data) for p, data in stable.items()}}


def successful_exit(root, identity, observed_at_unix, now):
    """Bind the actual exit file to a previously observed process lifetime."""
    root = Path(root)
    pid = integer(identity.get('pid'), 'process PID', 1)
    started = integer(identity.get('started_at_unix'), 'process start', 1)
    if not started <= observed_at_unix <= now:
        raise GuardError('Process observation time is unknown')
    base = root / 'runtime/exhaustive'
    run_raw, run = document(base / 'coordinator-run.json')
    path = base / 'coordinator-exit.json'
    receipt_raw, receipt = document(path)
    ended = integer(receipt.get('ended_at_unix'), 'process end', 1)
    if (run.get('pid') != pid or run.get('started_at_unix') != started
            or receipt.get('pid') != pid or not started <= ended <= now
            or ended + 1 < observed_at_unix or path.stat().st_mtime + 1 < observed_at_unix
            or type(receipt.get('exit_code')) is not int or receipt['exit_code'] != 0
            or receipt.get('exit_type') is not None
            or receipt.get('stop_requested') is not False):
        raise GuardError('Successful natural exit is not bound to the observed process')
    unchanged({base / 'coordinator-run.json': run_raw, path: receipt_raw})
    return {'pid': pid, 'started_at_unix': started, 'ended_at_unix': ended,
            'observed_alive_at_unix': observed_at_unix,
            'run_sha256': digest(run_raw), 'exit_sha256': digest(receipt_raw)}


def native_launch_attestation(root, launch_dir, coordinators, workers, pins, now):
    """Check pins and actual native headers after one already-completed launch.

    Process identities are supplied by the native OS collector, never by a
    saved approval. This function does not launch or retry a model. Startup
    without a response remains an explicit guard failure that can be rechecked.
    """
    root = Path(root).resolve()
    verify_pins(root, pins)
    receipt_raw, receipt = document(Path(launch_dir) / 'launch.json')
    pid = integer(receipt.get('pid'), 'new coordinator PID', 1)
    launch_time = integer(receipt.get('launched_at_unix'), 'launch timestamp', 1)
    if not isinstance(coordinators, list) or len(coordinators) != 1:
        raise GuardError('Launched coordinator is not unique')
    coordinator = coordinators[0]
    if coordinator.get('pid') != pid:
        raise GuardError('Launched coordinator identity is unknown')
    args = coordinator.get('args')
    command = receipt.get('command')
    if not isinstance(args, list) or not isinstance(command, list) or not args or not command:
        raise GuardError('Launched command is unknown')
    if Path(args[0]).resolve() != Path(command[0]).resolve() or args[1:] != command[1:]:
        raise GuardError('Observed and launched commands differ')
    if str(root / 'run_exhaustive.py') not in args[1:3] or '--recover-new-before-reviews' not in args:
        raise GuardError('Wrong continuation mode')
    started = integer(coordinator.get('started_at_unix'), 'new run start', 1)
    born = integer(coordinator.get('os_started_at_unix'), 'actual new OS birth', 1)
    if not launch_time - 1 <= born <= started or not 0 <= started-born <= 60:
        raise GuardError('OS birth and run start are not the same timestamp')
    if not launch_time - 1 <= started <= now:
        raise GuardError('Launch receipt is not bound to this process lifetime')
    base = root / 'runtime/exhaustive'
    run_raw, run = document(base / 'coordinator-run.json')
    if (run.get('pid') != pid or run.get('started_at_unix') != started
            or run.get('requested_execution') != {'model': 'gpt-6-astra', 'reasoning_effort': 'medium'}):
        raise GuardError('New run identity or requested execution differs')
    if not isinstance(workers, list) or not workers:
        raise GuardError('No current native response is attested')
    module_path = root / 'worker_execution.py'
    if pins.get('worker_execution.py') != digest(read_regular(module_path)):
        raise GuardError('Native execution parser is not pinned')
    # Compile in memory: even a bytecode cache write is unnecessary here.
    module = types.ModuleType('_offline_transfer_native_parser')
    exec(compile(read_regular(module_path), str(module_path), 'exec'), module.__dict__)
    evidence = []
    sessions = set()
    stable = {Path(launch_dir) / 'launch.json': receipt_raw, base / 'coordinator-run.json': run_raw}
    for worker in workers:
        name = worker.get('job')
        if not isinstance(name, str) or Path(name).name != name or worker.get('ppid') != pid:
            raise GuardError('Foreign native worker identity')
        folder = base / 'jobs' / name
        if folder.is_symlink() or not folder.resolve().is_relative_to(base / 'jobs'):
            raise GuardError('Native job folder escaped the project')
        worker_pid = integer(worker.get('pid'), 'worker PID', 1)
        process_path = folder / ('process-' + str(worker_pid) + '.json')
        process_raw, process = document(process_path)
        stable[process_path] = process_raw
        if (process.get('pid') != worker_pid or process.get('ended_at_unix') is not None
                or type(process.get('started_at_unix')) is not int
                or not started <= process['started_at_unix'] <= now):
            raise GuardError('Native worker lifetime is unknown')
        worker_born = integer(worker.get('os_started_at_unix'), 'actual native worker birth', 1)
        if not started <= worker_born <= process['started_at_unix'] <= worker_born+2:
            raise GuardError('Native process record and actual OS birth disagree')
        log = Path(process.get('stderr_log') or '')
        if log.parent.resolve() != folder.resolve() or log.is_symlink():
            raise GuardError('Native header log ownership differs')
        observed = module.verify_execution(folder, stderr_path=log)
        if not observed.get('verified'):
            raise GuardError('Native response is not attested: ' + observed.get('status', 'unknown'))
        session = observed['session_id']
        if session in sessions:
            raise GuardError('Native sessions are not distinct')
        sessions.add(session)
        evidence.append({'pid': worker_pid, 'job': name, 'execution': observed})
    unchanged(stable)
    verify_pins(root, pins)
    return {'pid': pid, 'started_at_unix': started, 'observed_at_unix': now,
            'native_workers': evidence, 'all_observed_live_workers_responding': True,
            'configured_capacity_or_speed_gain_proven': False}
