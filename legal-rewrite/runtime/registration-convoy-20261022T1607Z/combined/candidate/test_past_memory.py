"""Memory integration security boundaries; never contacts past.dev."""
from pathlib import Path
from unittest.mock import patch
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest

import past_memory


class MemoryBoundaries(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.folder = Path(self.tmp.name)
        rows = json.dumps([{'id': 'approved-source'}]).encode()
        (self.folder/'test-records.proposed.json').write_bytes(rows)
        (self.folder/'approval.json').write_text(json.dumps({'test_import_approved': True, 'records_sha256': hashlib.sha256(rows).hexdigest()}))
        (self.folder/'project-binding.json').write_text(json.dumps({'project_slug': 'approved-project', 'oauth_verified': True}))
        self.addCleanup(patch.stopall)
        patch('past_memory.SETUP', self.folder).start()
        self.client = object.__new__(past_memory.PastClient)

    def test_changed_project_never_receives_recall(self):
        calls = []
        def request(method, path, payload=None):
            calls.append((method, path))
            return {'project': {'slug': 'different-project'}}
        self.client.request = request
        with self.assertRaisesRegex(past_memory.PastError, 'project-does-not-match'):
            self.client.recall('Quels avantages conserver ?')
        self.assertEqual(calls, [('GET', '/api/v1/usage')])

    def test_unapproved_and_unattributed_results_never_reach_model(self):
        sent = []
        def request(method, path, payload=None):
            if method == 'GET':
                return {'project': {'slug': 'approved-project'}}
            sent.append(payload)
            return {'results': [
                {'content': 'Allowed', 'sources': [{'sourceId': 'approved-source'}]},
                {'content': 'Another application', 'sources': [{'sourceId': 'other-app'}]},
                {'content': 'Mixed', 'sources': [{'sourceId': 'approved-source'}, {'sourceId': 'other-app'}]},
                {'content': 'No attribution', 'sources': []}]}
        self.client.request = request
        result = self.client.recall('Quels avantages conserver ?')
        self.assertEqual([row['content'] for row in result['results']], ['Allowed'])
        self.assertEqual(result['filtered_documents'], 3)
        self.assertEqual(sent[0]['identity'], 'legal-rewrite')

    def test_credential_pattern_is_refused_before_network(self):
        def request(*args, **kwargs):
            self.fail('Credential-bearing query reached a network request')
        self.client.request = request
        with self.assertRaisesRegex(past_memory.PastError, 'credential-pattern'):
            self.client.recall('Find past_sk_not_a_real_key')

    def test_mcp_offers_only_recall_and_no_reader_or_mutation_override(self):
        messages = [
            {'jsonrpc': '2.0', 'id': 1, 'method': 'initialize', 'params': {'protocolVersion': '2025-06-18'}},
            {'jsonrpc': '2.0', 'method': 'notifications/initialized'},
            {'jsonrpc': '2.0', 'id': 2, 'method': 'tools/list'},
            {'jsonrpc': '2.0', 'id': 3, 'method': 'tools/call', 'params': {'name': 'ingest_memory', 'arguments': {}}},
            {'jsonrpc': '2.0', 'id': 4, 'method': 'tools/call', 'params': {'name': 'past_recall', 'arguments': {'question': 'test', 'identity': 'outsider'}}}]
        result = subprocess.run([sys.executable, str(Path(past_memory.__file__).with_name('past_memory_mcp.py'))], input='\n'.join(json.dumps(m) for m in messages)+'\n', text=True, capture_output=True, check=True)
        responses = [json.loads(line) for line in result.stdout.splitlines()]
        self.assertEqual(len(responses), 4)
        tools = responses[1]['result']['tools']
        self.assertEqual([tool['name'] for tool in tools], ['past_recall'])
        self.assertTrue(tools[0]['annotations']['readOnlyHint'])
        self.assertEqual(responses[2]['error']['code'], -32602)
        self.assertEqual(responses[3]['error']['code'], -32602)


if __name__ == '__main__':
    unittest.main()
