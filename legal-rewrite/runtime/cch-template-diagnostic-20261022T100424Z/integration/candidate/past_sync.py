"""Explicit, bounded past.dev synchronization. Importing this module does no IO.

No scheduler or recall hook. Credentials are loaded only after approved changes
or a pending ingestion require an actual request. Durable intent precedes POST;
the committed body ledger changes only after completed ingestion.
"""
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote
import argparse
import copy
import fcntl
import hashlib
import json
import os
import re
import sys

LEGAL = Path(__file__).resolve().parent
SETUP = LEGAL / 'past-setup'
PROJECT = 'default-project'
READER = 'legal-rewrite'
AUDIENCES = {'orientations', 'coordinations'}
AUTHORIZATION = 'reply call_59e7245f52e54c5fba61ab228800962d'
SECRET = re.compile(r'past_[sm]k_|BEGIN (?:RSA |EC )?PRIVATE KEY|(?:API_KEY|TOKEN)\s*=\s*\S+')


class SyncError(Exception):
    def __init__(self, code):
        self.code = code
        super().__init__(code)


def sha(value):
    return hashlib.sha256(value if isinstance(value, bytes) else value.encode()).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))


def load(path):
    try:
        return json.loads(Path(path).read_text())
    except (OSError, ValueError):
        raise SyncError('local-json-unavailable') from None


def save(path, data):
    path = Path(path)
    temporary = path.with_name(path.name + '.tmp')
    with temporary.open('w') as output:
        os.chmod(temporary, 0o600)
        output.write(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
        output.flush()
        os.fsync(output.fileno())
    temporary.replace(path)
    descriptor = os.open(path.parent, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def body_of(row):
    try:
        header, separator, body = row['content'].partition('\n\n')
        if not separator or not header or not body.strip() or SECRET.search(row['content']):
            raise ValueError()
        return body
    except (KeyError, TypeError, AttributeError, ValueError):
        raise SyncError('invalid-or-credential-bearing-record') from None


def source_key(row):
    metadata = row['metadata']
    return metadata['source_path'], metadata.get('source_section')


class Scope:
    def __init__(self, setup=SETUP, root=None):
        self.setup = Path(setup)
        self.root = Path(root) if root is not None else LEGAL.parent
        self.legal = self.root / 'legal-rewrite'
        self.approval = load(self.setup / 'full-approval.json')
        manifest_bytes = (self.setup / 'full-proposal.json').read_bytes()
        records_bytes = (self.setup / 'full-records.proposed.json').read_bytes()
        self.manifest_sha = sha(manifest_bytes)
        self.records_sha = sha(records_bytes)
        approval = self.approval
        if (approval.get('full_import_approved') is not True
                or approval.get('full_records_sha256') != self.records_sha
                or approval.get('full_manifest_sha256') != self.manifest_sha
                or approval.get('reader') != READER
                or approval.get('project_slug') != PROJECT
                or str(approval.get('user_authorization', '')).split(':', 1)[0] != AUTHORIZATION
                or approval.get('recall_mode') != 'only_when_useful'
                or approval.get('audiences') != ['orientations', 'coordinations']):
            raise SyncError('full-approval-or-manifest-mismatch')
        binding = load(self.setup / 'project-binding.json')
        if binding.get('project_slug') != PROJECT or binding.get('oauth_verified') is not True:
            raise SyncError('approved-project-binding-mismatch')
        manifest = json.loads(manifest_bytes)
        self.rows = json.loads(records_bytes)
        if (manifest.get('records_sha256') != self.records_sha
                or manifest.get('data_points') != 26
                or manifest.get('policy_documents') != 19
                or manifest.get('audit_documents') != 7
                or not isinstance(self.rows, list) or len(self.rows) != 26):
            raise SyncError('approved-26-source-scope-required')
        self.by_id = {}
        keys = set()
        kinds = {'policy_snapshot': 0, 'audit_snapshot': 0}
        for row in self.rows:
            try:
                identifier, metadata = row['id'], row['metadata']
                kind = metadata['kind']
                if (not isinstance(identifier, str)
                        or not re.fullmatch(r'[A-Za-z0-9._-]{1,200}', identifier)
                        or identifier in self.by_id or kind not in kinds
                        or not isinstance(row['label'], str) or not row['label'].strip()):
                    raise ValueError()
                if kind == 'policy_snapshot':
                    if (row['audience'] != 'orientations'
                            or metadata['source_path'] != 'legal-rewrite/policy-coordinations.json'
                            or not isinstance(metadata.get('source_section'), str)
                            or not metadata['source_section']):
                        raise ValueError()
                elif (row['audience'] != 'coordinations'
                      or metadata.get('source_section') is not None
                      or not metadata['source_path'].startswith('legal-rewrite/')
                      or Path(metadata['source_path']).suffix != '.md'):
                    raise ValueError()
                target = self.root / metadata['source_path']
                if not target.resolve().is_relative_to(self.legal.resolve()):
                    raise ValueError()
                key = source_key(row)
                if key in keys or sha(body_of(row)) != metadata['body_sha256']:
                    raise ValueError()
                moment = datetime.fromisoformat(row['timestamp'].replace('Z', '+00:00'))
                if moment.tzinfo is None or len(row['content']) >= 32000:
                    raise ValueError()
                kinds[kind] += 1
                keys.add(key)
                self.by_id[identifier] = row
            except (KeyError, TypeError, ValueError, AttributeError):
                raise SyncError('invalid-approved-source-scope') from None
        if kinds != {'policy_snapshot': 19, 'audit_snapshot': 7}:
            raise SyncError('approved-source-counts-mismatch')
        # The ten existing sources must be reused, never duplicated under new IDs.
        test_rows = load(self.setup / 'test-records.proposed.json')
        if len(test_rows) != 10 or len({r['id'] for r in test_rows}) != 10:
            raise SyncError('ten-test-source-ids-required')
        for row in test_rows:
            approved = self.by_id.get(row['id'])
            if (approved is None or source_key(approved) != source_key(row)
                    or approved['audience'] != row['audience']):
                raise SyncError('test-source-id-not-reused')

    def current_bodies(self):
        # Only frozen source paths/sections are read: new sections are ignored.
        policy = load(self.legal / 'policy-coordinations.json')
        result = {}
        for row in self.rows:
            path, section = source_key(row)
            target = self.root / path
            if not target.resolve().is_relative_to(self.legal.resolve()):
                raise SyncError('source-path-escaped-approved-root')
            try:
                body = (json.dumps(policy[section], ensure_ascii=False, indent=2)
                        if section is not None else target.read_text())
            except (OSError, KeyError):
                raise SyncError('approved-source-removed-or-unreadable') from None
            if not body.strip() or SECRET.search(body):
                raise SyncError('empty-or-credential-bearing-source')
            result[row['id']] = body
        return result


def approved_source_ids(setup=SETUP):
    """Read-only helper for the proposed recall patch; never authenticates."""
    setup = Path(setup)
    full = setup / 'full-approval.json'
    if full.exists() and load(full).get('full_import_approved') is True:
        return set(Scope(setup).by_id)
    approval = load(setup / 'approval.json')
    payload = (setup / 'test-records.proposed.json').read_bytes()
    if (approval.get('test_import_approved') is not True
            or sha(payload) != approval.get('records_sha256')):
        raise SyncError('approved-test-records-changed')
    return {row['id'] for row in json.loads(payload)}


def real_client():
    # Deliberately lazy: neither importing nor an unchanged updates run reads a key.
    from past_memory import PastClient
    return PastClient()


@contextmanager
def exclusive(setup):
    with (Path(setup) / 'sync.lock').open('a') as lock:
        os.chmod(lock.name, 0o600)
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise SyncError('synchronization-already-running') from None
        try:
            yield
        finally:
            fcntl.flock(lock, fcntl.LOCK_UN)


class Synchronizer:
    def __init__(self, setup=SETUP, root=None, client_factory=real_client, now=None):
        self.setup = Path(setup)
        self.root = root
        self.client_factory = client_factory
        self.now = now or (lambda: datetime.now(timezone.utc).isoformat())
        self.client = None
        self.path = self.setup / 'sync-state.json'

    def event(self, kind, **values):
        # Never log document content, exception text, headers, or credentials.
        with (self.setup / 'sync-events.jsonl').open('a') as output:
            os.chmod(output.name, 0o600)
            output.write(canonical({'event': kind, **values}) + '\n')
            output.flush()
            os.fsync(output.fileno())

    def network(self):
        if self.client is None:
            candidate = self.client_factory()
            usage = candidate.request('GET', '/api/v1/usage')
            if usage.get('project', {}).get('slug') != PROJECT:
                raise SyncError('remote-project-mismatch')
            identity = candidate.request('GET', '/api/v1/identities/' + READER)
            if (identity.get('identity') != READER
                    or not AUDIENCES.issubset(set(identity.get('audiences') or []))):
                raise SyncError('fixed-reader-audiences-unavailable')
            self.client = candidate
        return self.client

    def new_state(self, scope):
        state = {'version': 1, 'project': PROJECT, 'reader': READER,
                 'manifest_sha256': scope.manifest_sha, 'records_sha256': scope.records_sha,
                 'entries': {}, 'pending': None, 'initial_completed': False}
        # Seed only an approved, completed and verified test, avoiding timestamp-only
        # replacements of the same ten bodies during the initial full import.
        approval = load(self.setup / 'approval.json')
        payload = (self.setup / 'test-records.proposed.json').read_bytes()
        receipt = load(self.setup / 'test-ingestion.json')
        poll = load(self.setup / 'test-poll.json')
        report = load(self.setup / 'test-report.json')
        rows = json.loads(payload)
        if (approval.get('test_import_approved') is not True
                or approval.get('records_sha256') != sha(payload)
                or poll.get('status') != 'completed'
                or report.get('all_checks_passed') is not True
                or report.get('project') != PROJECT
                or report.get('on_demand_reader') != READER
                or {x.get('sourceId') for x in receipt.get('items', [])}
                   != {x['id'] for x in rows}
                or not receipt.get('ingestionId')):
            raise SyncError('completed-test-evidence-required')
        for row in rows:
            state['entries'][row['id']] = {
                'body_sha256': sha(body_of(row)), 'timestamp': row['timestamp'],
                'ingestion_id': receipt['ingestionId'], 'origin': 'completed-approved-test'}
        return state

    def check_state(self, scope, state):
        if (state.get('version') != 1 or state.get('project') != PROJECT
                or state.get('reader') != READER
                or state.get('manifest_sha256') != scope.manifest_sha
                or state.get('records_sha256') != scope.records_sha
                or not isinstance(state.get('entries'), dict)
                or not set(state['entries']).issubset(scope.by_id)):
            raise SyncError('ledger-scope-mismatch')
        pending = state.get('pending')
        if not pending:
            return
        request = pending['request']
        if (request.get('idempotencyKey') != self.replay_key(request['items'])
                or not request['items'] or len(request['items']) > 26):
            raise SyncError('pending-request-mismatch')
        ids = set()
        for item in request['items']:
            frozen = scope.by_id.get(item.get('id'))
            if (frozen is None or item['id'] in ids
                    or set(item) != set(frozen) | {'identity'}
                    or item.get('audience') != frozen['audience']
                    or item.get('identity') != READER
                    or item.get('label') != frozen['label']
                    or source_key(item) != source_key(frozen)
                    or set(item['metadata']) != set(frozen['metadata'])
                    or item['metadata'].get('kind') != frozen['metadata']['kind']
                    or sha(body_of(item)) != item['metadata'].get('body_sha256')):
                raise SyncError('pending-request-outside-approved-scope')
            ids.add(item['id'])

    @staticmethod
    def replay_key(items):
        # Includes the persisted timestamp, so a real A→B→A revision is new;
        # retries of one saved intent retain exactly the same key and payload.
        return 'legal-rewrite-sync-' + sha(canonical({'project': PROJECT, 'items': items}))

    def complete(self, scope, state):
        pending = state['pending']
        for item in pending['request']['items']:
            state['entries'][item['id']] = {
                'body_sha256': item['metadata']['body_sha256'],
                'timestamp': item['timestamp'], 'ingestion_id': pending['ingestion_id'],
                'origin': pending['mode']}
        if pending['mode'] == 'initial':
            state['initial_completed'] = set(state['entries']) == set(scope.by_id)
        ingestion = pending['ingestion_id']
        state['pending'] = None
        save(self.path, state)
        self.event('completed', ingestion_id=ingestion)

    def poll_pending(self, scope, state):
        pending = state['pending']
        if not pending.get('ingestion_id'):
            return 'receipt-unknown'
        receipt = self.network().request('GET', '/api/v1/ingest/' + quote(pending['ingestion_id'], safe=''))
        status = receipt.get('status')
        if status not in {'queued', 'processing', 'completed', 'failed'}:
            raise SyncError('invalid-ingestion-status')
        pending['status'] = status
        save(self.path, state)
        self.event('polled', ingestion_id=pending['ingestion_id'], status=status)
        if status == 'completed':
            self.complete(scope, state)
        return status

    def send_pending(self, scope, state):
        pending = state['pending']
        receipt = self.network().request('POST', '/api/v1/ingest/batch', pending['request'])
        if (not isinstance(receipt.get('ingestionId'), str)
                or not re.fullmatch(r'[A-Za-z0-9-]{1,100}', receipt['ingestionId'])
                or receipt.get('status') not in {'queued', 'processing', 'completed'}
                or {x.get('sourceId') for x in receipt.get('items', [])}
                   != {x['id'] for x in pending['request']['items']}):
            raise SyncError('invalid-ingestion-receipt')
        pending['ingestion_id'] = receipt['ingestionId']
        pending['status'] = receipt['status']
        save(self.path, state)
        self.event('accepted', ingestion_id=pending['ingestion_id'], status=pending['status'])
        if receipt['status'] == 'completed':
            self.complete(scope, state)
        return receipt['status']

    def run(self, mode):
        if mode not in {'initial', 'poll', 'updates'}:
            raise SyncError('unsupported-sync-command')
        with exclusive(self.setup):
            scope = Scope(self.setup, self.root)
            if mode == 'updates' and scope.approval.get('automatic_ingestion_approved') is not True:
                raise SyncError('future-updates-not-approved')
            state = load(self.path) if self.path.exists() else self.new_state(scope)
            self.check_state(scope, state)
            if state['pending']:
                status = self.poll_pending(scope, state)
                if status == 'receipt-unknown' and mode != 'poll':
                    status = self.send_pending(scope, state)
                if status != 'completed':
                    return {'status': status, 'pending': True, 'new_sources': 0}
            if mode == 'poll':
                return {'status': 'completed' if state['initial_completed'] else 'not-started', 'pending': False}
            if mode == 'initial' and state['initial_completed']:
                return {'status': 'unchanged', 'changed_sources': 0}
            if mode == 'updates' and not state['initial_completed']:
                raise SyncError('initial-import-not-completed')
            bodies = ({r['id']: body_of(r) for r in scope.rows}
                      if mode == 'initial' else scope.current_bodies())
            changed = [r for r in scope.rows if state['entries'].get(r['id'], {}).get('body_sha256') != sha(bodies[r['id']])]
            if not changed:
                if mode == 'initial':
                    state['initial_completed'] = True
                    save(self.path, state)
                return {'status': 'unchanged', 'changed_sources': 0}
            timestamp = self.now()
            items = []
            for row in changed:
                item = copy.deepcopy(row)
                body = bodies[row['id']]
                # Initial sends are the exact approved snapshot; updated bodies
                # get a new captured-at header only when the actual body changed.
                if mode == 'updates':
                    heading = ('Orientation de réécriture : ' + row['metadata']['source_section']
                               if row['audience'] == 'orientations' else row['label'])
                    item['content'] = (heading + '\nInstantané capturé le ' + timestamp
                                       + '. Date de capture, pas date historique de décision.\n\n' + body)
                    item['timestamp'] = timestamp
                    item['metadata']['body_sha256'] = sha(body)
                item['identity'] = READER
                if len(item['content']) >= 32000:
                    raise SyncError('approved-document-too-large-no-automatic-splitting')
                items.append(item)
            request = {'items': items, 'idempotencyKey': self.replay_key(items)}
            state['pending'] = {'mode': mode, 'status': 'prepared', 'ingestion_id': None, 'request': request}
            self.check_state(scope, state)
            save(self.path, state)  # Survives acceptance followed by a lost response.
            self.event('prepared', mode=mode, source_ids=[x['id'] for x in items], idempotency_key=request['idempotencyKey'])
            status = self.send_pending(scope, state)
            return {'status': status, 'changed_sources': len(items), 'pending': state['pending'] is not None}


def main():
    parser = argparse.ArgumentParser(description='Synchronisation explicite des26sources approuvées ; aucun rappel ni service permanent.')
    parser.add_argument('action', choices=['initial', 'poll', 'updates'])
    args = parser.parse_args()
    try:
        result = Synchronizer().run(args.action)
        print(json.dumps(result, ensure_ascii=False))
        return 1 if result['status'] in {'failed', 'receipt-unknown'} else 0
    except Exception as error:
        # Only known codes, never raw network/IO errors or credentials.
        code = error.code if isinstance(error, SyncError) else 'synchronization-unavailable'
        print(json.dumps({'error': code}), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
