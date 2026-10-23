from pathlib import Path
import importlib.util
import unittest

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('offline_access', HERE/'access_failure.py')
offline = importlib.util.module_from_spec(spec)
spec.loader.exec_module(offline)


class TerminalAccessFailures(unittest.TestCase):
    def test_real_routing_incident_not_legal_quota(self):
        log = HERE.parent/'exhaustive/jobs/travail-00472/errors-3.log'
        self.assertTrue(log.is_file(), 'Preserved original incident is required')
        self.assertFalse(offline.native_access_failure(log.read_text()))

    def test_legal_source_and_model_output_are_not_cli_failures(self):
        for text in [
            'user\nQuota exceeded, authentication required, HTTP 429\n',
            'codex\nERROR: authentication failed\nCette phrase est citée.\n',
            'exec\nERROR: quota exceeded\n<p>Quota communal.</p>\n',
            'user\nquota\nERROR: workspace routing discovery timed out\n',
            'codex\ninsufficient justification\nERROR: request timed out\n']:
            with self.subTest(text=text):
                self.assertFalse(offline.native_access_failure(text))

    def test_explicit_native_access_failures_remain_blocking(self):
        for text in ['rate limit exceeded', 'usage limit reached',
                     'insufficient_quota', 'quota exceeded', 'quota exhausted',
                     'authentication failed', 'authentication required',
                     'Unauthorized', 'Unauthorised', 'invalid API key',
                     'not logged in', 'not signed in', 'Please sign in',
                     'sign in again', 'sign in to continue', 'too many requests',
                     'insufficient credits', 'insufficient funds',
                     'credit balance is too low', 'HTTP 401 Unauthorized',
                     'HTTP error 403', 'HTTP/2 429', 'status code: 429',
                     'unexpected status code: 401']:
            with self.subTest(text=text):
                self.assertTrue(offline.native_access_failure('ERROR: '+text+'\n'))

    def test_footer_and_native_timestamp(self):
        self.assertTrue(offline.native_access_failure(
            '2026-10-23T09:15:36.274873Z ERROR codex_models_manager::manager: '
            'authentication failed\nERROR: request timed out\ntokens used\n16,316\n\n'))

    def test_transport_errors_do_not_imply_access_denial(self):
        for text in ['Reconnecting... 5/5', 'workspace routing discovery timed out',
                     'stream disconnected before completion', 'HTTP 500',
                     'insufficient evidence', 'quota communal',
                     'authentication transport request timed out']:
            with self.subTest(text=text):
                self.assertFalse(offline.native_access_failure('ERROR: '+text+'\n'))

    def test_nonterminal_error_cannot_leak_into_fatal_suffix(self):
        self.assertFalse(offline.native_access_failure(
            'ERROR: quota exceeded\ncodex\nAn article about quotas.\n'
            'ERROR: workspace routing discovery timed out\ntokens used\n100\n'))


if __name__ == '__main__':
    unittest.main()
