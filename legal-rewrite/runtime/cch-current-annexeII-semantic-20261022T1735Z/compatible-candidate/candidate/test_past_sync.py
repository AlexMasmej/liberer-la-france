"""Offline synchronization contracts. Never loads credentials or opens a socket."""
from pathlib import Path
from unittest.mock import patch
import copy
import difflib
import fcntl
import json
import tempfile
import types
import unittest

import past_sync as sync


class FakeClient:
    def __init__(self):
        self.calls = []
        self.status = 'completed'
        self.project = sync.PROJECT
        self.audiences = sorted(sync.AUDIENCES)
        self.fail_post = False

    def request(self, method, path, payload=None):
        self.calls.append((method, path, copy.deepcopy(payload)))
        if path == '/api/v1/usage':
            return {'project': {'slug': self.project}}
        if path == '/api/v1/identities/legal-rewrite':
            return {'identity': sync.READER, 'audiences': self.audiences}
        if method == 'POST':
            if self.fail_post:
                raise ConnectionError('simulated lost response')
            return {'ingestionId': 'receipt-123', 'status': self.status,
                    'items': [{'sourceId': row['id']} for row in payload['items']]}
        return {'status': self.status, 'settled': self.status == 'completed'}


class SyncContracts(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.legal = self.root / 'legal-rewrite'
        self.setup = self.legal / 'past-setup'
        self.setup.mkdir(parents=True)
        policy = {f'section{i}': {'decision': f'Value {i}'} for i in range(19)}
        self.write(self.legal / 'policy-coordinations.json', policy)
        self.rows = []
        for section, value in policy.items():
            body = json.dumps(value, ensure_ascii=False, indent=2)
            self.rows.append(self.record('policy-' + section, 'orientations', body,
                                        'legal-rewrite/policy-coordinations.json', section))
        for i in range(7):
            path = self.legal / f'audit{i}.md'
            body = f'# Audit {i}\n\nComplete document {i}.\n'
            path.write_text(body)
            self.rows.append(self.record(f'audit-{i}', 'coordinations', body, f'legal-rewrite/audit{i}.md'))
        self.write(self.setup / 'full-records.proposed.json', self.rows)
        self.manifest = {'records_sha256': sync.sha((self.setup / 'full-records.proposed.json').read_bytes()),
                         'data_points': 26, 'policy_documents': 19, 'audit_documents': 7}
        self.write(self.setup / 'full-proposal.json', self.manifest)
        self.approval = {'full_import_approved': True, 'automatic_ingestion_approved': True,
                         'full_records_sha256': self.manifest['records_sha256'],
                         'full_manifest_sha256': sync.sha((self.setup / 'full-proposal.json').read_bytes()),
                         'reader': sync.READER, 'project_slug': sync.PROJECT,
                         'audiences': ['orientations', 'coordinations'],
                         'user_authorization': sync.AUTHORIZATION + ': Import et futures mises à jour',
                         'recall_mode': 'only_when_useful'}
        self.write(self.setup / 'full-approval.json', self.approval)
        self.write(self.setup / 'project-binding.json', {'project_slug': sync.PROJECT, 'oauth_verified': True})
        self.write(self.setup / 'test-records.proposed.json', self.rows[:5] + self.rows[19:24])
        tests = sync.load(self.setup / 'test-records.proposed.json')
        self.write(self.setup / 'approval.json', {'test_import_approved': True,
                  'records_sha256': sync.sha((self.setup / 'test-records.proposed.json').read_bytes())})
        self.write(self.setup / 'test-ingestion.json', {'ingestionId': 'test-123',
                  'items': [{'sourceId': r['id']} for r in tests]})
        self.write(self.setup / 'test-poll.json', {'status': 'completed'})
        self.write(self.setup / 'test-report.json', {'all_checks_passed': True,
                  'project': sync.PROJECT, 'on_demand_reader': sync.READER})
        self.fake = FakeClient()
        self.created = 0
        # No code path in these tests may instantiate the credential-bearing client.
        self.addCleanup(patch.stopall)
        patch('past_memory.key_from_environment', side_effect=AssertionError('credentials accessed')).start()

    @staticmethod
    def write(path, value):
        Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

    @staticmethod
    def record(identifier, audience, body, path, section=None):
        metadata = {'kind': 'policy_snapshot' if section else 'audit_snapshot',
                    'source_path': path, 'body_sha256': sync.sha(body)}
        if section:
            metadata['source_section'] = section
        return {'id': identifier, 'label': 'Label ' + identifier,
                'timestamp': '2026-10-19T00:00:00+00:00', 'audience': audience,
                'content': 'Snapshot header\n\n' + body, 'metadata': metadata}

    def factory(self):
        self.created += 1
        return self.fake

    def runner(self, moment='2026-10-20T00:00:00+00:00'):
        return sync.Synchronizer(self.setup, self.root, self.factory, now=lambda: moment)

    def state(self):
        return sync.load(self.setup / 'sync-state.json')

    def posts(self):
        return [x[2] for x in self.fake.calls if x[0] == 'POST']

    def finish_initial(self):
        self.runner().run('initial')
        self.assertTrue(self.state()['initial_completed'])

    def change_policy(self, section='section0', value='Changed'):
        path = self.legal / 'policy-coordinations.json'
        policy = sync.load(path)
        policy[section] = value
        self.write(path, policy)

    def test_initial_reuses_completed_ten_ids_and_only_sends_sixteen_changed_bodies(self):
        result = self.runner().run('initial')
        self.assertEqual(result['changed_sources'], 16)
        self.assertEqual(len(self.state()['entries']), 26)
        self.assertEqual(len(self.posts()[0]['items']), 16)
        self.assertTrue(all(r['audience'] in sync.AUDIENCES and r['identity'] == sync.READER
                            for r in self.posts()[0]['items']))

    def test_recall_helper_allows_exactly_twenty_six_or_approved_test_ids(self):
        self.assertEqual(sync.approved_source_ids(self.setup), {r['id'] for r in self.rows})
        self.approval['full_import_approved'] = False
        self.write(self.setup / 'full-approval.json', self.approval)
        self.assertEqual(sync.approved_source_ids(self.setup),
                         {r['id'] for r in sync.load(self.setup / 'test-records.proposed.json')})

    def proposed_memory(self):
        folder = Path(__file__).parent / 'past-setup'
        base = (folder / 'past_memory_full_scope.base.py.txt').read_text()
        proposed = (folder / 'past_memory_full_scope.proposed.py.txt').read_text()
        expected_patch = ''.join(difflib.unified_diff(
            base.splitlines(True), proposed.splitlines(True),
            fromfile='a/legal-rewrite/past_memory.py', tofile='b/legal-rewrite/past_memory.py'))
        self.assertEqual((folder / 'past_memory_full_scope.proposed.patch').read_text(), expected_patch)
        module = types.ModuleType('proposed_past_memory')
        module.__file__ = str(Path(__file__).parent / 'past_memory.py')
        exec(compile(proposed, module.__file__, 'exec'), module.__dict__)
        module.SETUP = self.setup
        return module, object.__new__(module.PastClient)

    def test_proposed_recall_patch_filters_other_and_mixed_sources_under_full_approval(self):
        module, client = self.proposed_memory()
        def request(method, path, payload=None):
            if method == 'GET':
                return {'project': {'slug': sync.PROJECT}}
            self.assertEqual(payload['identity'], sync.READER)
            return {'results': [
                {'content': 'New approved audit', 'sources': [{'sourceId': 'audit-6'}]},
                {'content': 'Other', 'sources': [{'sourceId': 'other'}]},
                {'content': 'Mixed', 'sources': [{'sourceId': 'audit-6'}, {'sourceId': 'other'}]},
                {'content': 'Missing attribution', 'sources': []}]}
        client.request = request
        result = client.recall('Quels avantages sont conservés ?')
        self.assertEqual([r['content'] for r in result['results']], ['New approved audit'])
        self.assertEqual(result['filtered_documents'], 3)

    def test_proposed_recall_patch_rejects_changed_full_manifest_before_network(self):
        module, client = self.proposed_memory()
        client.request = lambda *args, **kwargs: self.fail('Local scope failure reached network')
        path = self.setup / 'full-proposal.json'
        path.write_bytes(path.read_bytes() + b' ')
        with self.assertRaisesRegex(module.PastError, 'approval-or-manifest-mismatch'):
            client.recall('Quels avantages sont conservés ?')

    def test_audit_symlink_escape_is_refused_before_network(self):
        self.finish_initial()
        outside = self.root / 'outside.md'
        outside.write_text('Not approved source material')
        path = self.legal / 'audit0.md'
        path.unlink()
        path.symlink_to(outside)
        self.created = 0
        with self.assertRaisesRegex(sync.SyncError, 'invalid-approved-source-scope'):
            self.runner().run('updates')
        self.assertEqual(self.created, 0)

    def test_unchanged_updates_does_not_load_key_or_create_client_or_change_timestamp(self):
        self.finish_initial()
        before = (self.setup / 'sync-state.json').read_bytes()
        self.created = 0
        result = self.runner('2030-01-01T00:00:00Z').run('updates')
        self.assertEqual(result['status'], 'unchanged')
        self.assertEqual(self.created, 0)
        self.assertEqual(before, (self.setup / 'sync-state.json').read_bytes())

    def test_pending_intent_exists_before_post_and_ledger_finalizes_only_after_completed(self):
        self.fake.status = 'queued'
        original = self.fake.request
        def request(method, path, payload=None):
            if method == 'POST':
                self.assertEqual(self.state()['pending']['request'], payload)
                self.assertEqual(len(self.state()['entries']), 10)
            return original(method, path, payload)
        self.fake.request = request
        self.runner().run('initial')
        self.assertFalse(self.state()['initial_completed'])
        self.assertEqual(len(self.state()['entries']), 10)
        self.fake.status = 'processing'
        self.runner().run('poll')
        self.assertEqual(len(self.state()['entries']), 10)
        self.fake.status = 'completed'
        self.runner().run('poll')
        self.assertEqual(len(self.state()['entries']), 26)
        self.assertEqual(len(self.posts()), 1)

    def test_lost_receipt_reuses_exact_payload_timestamp_and_key_after_restart(self):
        self.fake.fail_post = True
        with self.assertRaises(ConnectionError):
            self.runner().run('initial')
        request = self.state()['pending']['request']
        self.fake.fail_post = False
        # poll alone must not replay a POST, even with unknown acceptance status.
        self.assertEqual(self.runner().run('poll')['status'], 'receipt-unknown')
        self.assertEqual(len(self.posts()), 1)
        self.runner('2035-01-01T00:00:00Z').run('initial')
        self.assertEqual(self.posts()[1], request)
        self.assertEqual(len(self.state()['entries']), 26)

    def test_failed_ingestion_keeps_pending_and_never_finalizes_or_resends(self):
        self.fake.status = 'queued'
        self.runner().run('initial')
        self.fake.status = 'failed'
        self.assertEqual(self.runner().run('updates')['status'], 'failed')
        self.assertEqual(len(self.state()['entries']), 10)
        self.assertEqual(len(self.posts()), 1)
        self.assertIsNotNone(self.state()['pending'])

    def test_updates_send_only_changed_approved_section_and_audit(self):
        self.finish_initial()
        self.change_policy()
        (self.legal / 'audit0.md').write_text('Changed complete audit.\n')
        self.runner().run('updates')
        self.assertEqual({x['id'] for x in self.posts()[-1]['items']}, {'policy-section0', 'audit-0'})
        self.assertTrue(all(x['timestamp'] == '2026-10-20T00:00:00+00:00' for x in self.posts()[-1]['items']))

    def test_new_section_and_new_file_are_never_auto_added(self):
        self.finish_initial()
        self.change_policy('new_unapproved_section')
        (self.legal / 'new-audit.md').write_text('Unapproved.')
        self.created = 0
        self.assertEqual(self.runner().run('updates')['changed_sources'], 0)
        self.assertEqual(self.created, 0)

    def test_missing_approved_section_fails_before_network(self):
        self.finish_initial()
        policy = sync.load(self.legal / 'policy-coordinations.json')
        del policy['section0']
        self.write(self.legal / 'policy-coordinations.json', policy)
        self.created = 0
        with self.assertRaisesRegex(sync.SyncError, 'removed-or-unreadable'):
            self.runner().run('updates')
        self.assertEqual(self.created, 0)

    def test_modified_approval_or_manifest_or_records_fails_before_credentials(self):
        for name in ['full-proposal.json', 'full-records.proposed.json']:
            path = self.setup / name
            old = path.read_bytes()
            path.write_bytes(old + b' ')
            with self.assertRaisesRegex(sync.SyncError, 'approval-or-manifest-mismatch'):
                self.runner().run('initial')
            path.write_bytes(old)
        self.assertEqual(self.created, 0)

    def test_updates_approval_required_separately(self):
        self.finish_initial()
        self.approval['automatic_ingestion_approved'] = False
        self.write(self.setup / 'full-approval.json', self.approval)
        self.created = 0
        with self.assertRaisesRegex(sync.SyncError, 'updates-not-approved'):
            self.runner().run('updates')
        self.assertEqual(self.created, 0)

    def test_wrong_project_or_missing_reader_scope_never_posts(self):
        self.fake.project = 'other-project'
        with self.assertRaisesRegex(sync.SyncError, 'remote-project-mismatch'):
            self.runner().run('initial')
        self.assertEqual(self.posts(), [])
        self.fake.project = sync.PROJECT
        self.fake.audiences = ['orientations']
        with self.assertRaisesRegex(sync.SyncError, 'reader-audiences-unavailable'):
            self.runner().run('initial')
        self.assertEqual(self.posts(), [])

    def test_credential_pattern_in_changed_body_refused_without_key(self):
        self.finish_initial()
        self.change_policy(value='TOKEN=do-not-send')
        self.created = 0
        with self.assertRaisesRegex(sync.SyncError, 'credential-bearing-source'):
            self.runner().run('updates')
        self.assertEqual(self.created, 0)

    def test_flock_excludes_other_workers_before_client_creation(self):
        with (self.setup / 'sync.lock').open('a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            for _ in range(3):
                with self.assertRaisesRegex(sync.SyncError, 'already-running'):
                    self.runner().run('initial')
        self.assertEqual(self.created, 0)

    def test_body_reversion_gets_new_key_not_old_completed_receipt(self):
        self.finish_initial()
        self.change_policy(value='A')
        self.runner('2026-10-20T00:00:00Z').run('updates')
        first = self.posts()[-1]['idempotencyKey']
        self.change_policy(value='B')
        self.runner('2026-10-21T00:00:00Z').run('updates')
        self.change_policy(value='A')
        self.runner('2026-10-22T00:00:00Z').run('updates')
        self.assertNotEqual(first, self.posts()[-1]['idempotencyKey'])

    def test_no_source_split_when_document_grows_beyond_approved_size(self):
        self.finish_initial()
        (self.legal / 'audit0.md').write_text('x' * 32000)
        self.created = 0
        with self.assertRaisesRegex(sync.SyncError, 'no-automatic-splitting'):
            self.runner().run('updates')
        self.assertEqual(self.created, 0)

    def test_pending_tampering_is_refused_before_any_network(self):
        self.fake.fail_post = True
        with self.assertRaises(ConnectionError):
            self.runner().run('initial')
        state = self.state()
        state['pending']['request']['items'][0]['audience'] = 'project'
        self.write(self.setup / 'sync-state.json', state)
        self.created = 0
        with self.assertRaisesRegex(sync.SyncError, 'pending-request-mismatch'):
            self.runner().run('poll')
        self.assertEqual(self.created, 0)

    def test_completed_test_evidence_required_before_seeding_ledger(self):
        self.write(self.setup / 'test-poll.json', {'status': 'processing'})
        with self.assertRaisesRegex(sync.SyncError, 'test-evidence-required'):
            self.runner().run('initial')
        self.assertEqual(self.created, 0)


if __name__ == '__main__':
    unittest.main()
