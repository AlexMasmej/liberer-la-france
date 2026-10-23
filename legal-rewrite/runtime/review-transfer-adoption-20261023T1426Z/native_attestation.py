from pathlib import Path
import types
from transfer_guards import (GuardError,integer,document,digest,read_regular,unchanged,verify_pins)
from interpreter_guard import bind_interpreter

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
    image_binding=bind_interpreter(args[0],command[0],args[1:],command[1:],pid)
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
    return {'interpreter_binding':image_binding,'pid': pid, 'started_at_unix': started, 'observed_at_unix': now,
            'native_workers': evidence, 'all_observed_live_workers_responding': True,
            'configured_capacity_or_speed_gain_proven': False}
