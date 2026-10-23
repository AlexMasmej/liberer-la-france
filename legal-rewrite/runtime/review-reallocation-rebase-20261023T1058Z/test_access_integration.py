from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest import TestCase
from unittest.mock import patch
import hashlib
import io
import json
import threading

import run_exhaustive as runner
from ingest import open_db
from test_execution_fixture import emit_cli_startup


class InvocationFailureDisposition(TestCase):
    def exercise(self, diagnostic, blocked):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            runtime = root/'runtime'; runtime.mkdir()
            for name in ['site-summaries.json', 'policy-coordinations.json']:
                (root/name).write_text('{}')
            body = '<p>Le délai applicable est de trois mois.</p>'
            source_hash = hashlib.sha256(body.encode()).hexdigest()
            rows = []
            db = open_db(root/'corpus.sqlite')
            for key in ['FAIL', 'NEXT']:
                row = dict(code_id='TEST', source_id=key, number=key,
                           source_sha256=source_hash, source_xml=body,
                           source_notes_xml='')
                rows.append(row)
                db.execute('INSERT INTO articles VALUES(?,?,?,?,?,?,?,?,?,?)',
                           ('TEST', key, key, '2020-01-01', '2999-01-01',
                            'VIGUEUR', body, body, source_hash, 'fixture'))
            db.commit(); db.close()
            calls = []

            def invoke(*args, **kwargs):
                folder = kwargs['cwd']; calls.append(folder.name)
                if folder.name.endswith('00001'):
                    kwargs['stderr'].write(diagnostic)
                    return SimpleNamespace(returncode=1)
                emit_cli_startup(kwargs)
                row = {k: rows[1][k] for k in [
                    'code_id', 'source_id', 'source_sha256', 'number']}
                row.update(proposed_xml='<p>Le délai applicable est fixé à trois mois.</p>', reason='Conserve le délai.',
                           review_notes='Le délai de trois mois demeure.')
                (folder/'answer.json').write_text(json.dumps([row]))
                (folder/'result.json').write_text(json.dumps(
                    dict(output_file='answer.json', article_count=1)))
                return SimpleNamespace(returncode=0)

            with patch.object(runner, 'HERE', root), \
                    patch.object(runner, 'RUNTIME', runtime), \
                    patch.object(runner, 'STOP', threading.Event()), \
                    patch.object(runner, 'invoke_agent', side_effect=invoke), \
                    patch.object(runner, 'past_before_job', return_value=[]), \
                    redirect_stdout(io.StringIO()):
                runner.run_job(('travail', 1, [rows[0]]), 'no-model', {'travail': rows})
                self.assertEqual(runner.STOP.is_set(), blocked)
                runner.run_job(('travail', 2, [rows[1]]), 'no-model', {'travail': rows})
            db = open_db(root/'corpus.sqlite')
            self.assertIsNone(db.execute(
                "SELECT proposed_xml FROM drafts WHERE source_id='FAIL'").fetchone())
            self.assertEqual(db.execute(
                "SELECT COUNT(*) FROM drafts WHERE source_id='NEXT'").fetchone()[0],
                0 if blocked else 1)
            db.close()
            self.assertEqual(len(calls), 1 if blocked else 4)
            metrics = [json.loads(x) for x in
                       (runtime/'job-metrics.jsonl').read_text().splitlines()]
            self.assertEqual(metrics[0]['outcome'],
                             'blocked_auth_or_usage' if blocked else 'deferred')
            self.assertEqual(metrics[0]['attempts'], 1 if blocked else 3)
            if not blocked:
                self.assertEqual(metrics[-1]['outcome'], 'accepted')

    def test_routing_and_legal_quota_preserve_pending_and_admit_next(self):
        self.exercise('user\nNe pas rétablir les quotas SRU.\n'
                      'ERROR: workspace routing discovery timed out\n'
                      'tokens used\n16,316\n', blocked=False)

    def test_genuine_access_denial_stops_without_retries_or_next_admission(self):
        self.exercise('ERROR: HTTP 429: usage limit reached\n', blocked=True)
