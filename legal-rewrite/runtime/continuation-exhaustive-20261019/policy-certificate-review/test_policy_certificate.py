"""Three isolated policy guard tests; no canonical database or policy writes."""
from pathlib import Path
import hashlib
import importlib.util
import json
import sqlite3
import sys
import tempfile
import unittest
from unittest.mock import patch

FOLDER = Path(__file__).resolve().parent
sys.path.insert(0, str(FOLDER.parents[2]))
spec = importlib.util.spec_from_file_location('policy_review_candidate', FOLDER / 'reference_coherence.proposed.py')
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class PolicyCertificate(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.db = sqlite3.connect(':memory:')
        self.addCleanup(self.db.close)
        self.db.executescript('''
            CREATE TABLE articles(code_id,id,number,source_sha256,content_xml);
            CREATE TABLE drafts(code_id,source_id,source_sha256,proposed_xml);
            CREATE TABLE documents(code_id,id,kind,xml);
        ''')
        self.catalog = {}
        for identifier, number, body in [
            ('A', 'L10-1', '<p>Le renvoi L20-1 conserve la garantie.</p>'),
            ('B', 'L20-1', '<p>La garantie reste applicable.</p>'),
        ]:
            article = dict(code_id='CODE', source_id=identifier,
                           number=number, source_sha256='s' + identifier,
                           source_xml=body, source_notes_xml='')
            self.catalog[audit.key(article)] = article
            self.db.execute('INSERT INTO articles VALUES(?,?,?,?,?)',
                            ('CODE', identifier, number, 's' + identifier, body))
        self.article = self.catalog['CODE|A']
        self.body = '<p>Les droits du salarié suivent la garantie L20-1, sans modification.</p>'
        self.policy = {
            'policy-coordinations.json': b'{"cuts_and_reliefs": "orientation initiale"}\n',
            'site-summaries.json': b'{"summary": "anciennete totale"}\n',
        }
        p = patch.object(audit, 'HERE', self.root)
        p.start(); self.addCleanup(p.stop)

    def write_policies(self):
        for name, content in self.policy.items():
            (self.root / name).write_bytes(content)

    def capture_and_certificate(self):
        snapshot = audit.capture(self.db, [self.article], catalog=self.catalog)
        row = self.article | dict(proposed_xml=self.body, reference_checks=[dict(
            target_key=identifier, view_sha256=target['view_sha256'],
            assessment='Le renvoi conserve la garantie de la cible entière et les droits des salariés ; aucune période ni dispense favorable ne disparaît de cette coordination.'
        ) for identifier, target in snapshot['targets'].items()])
        audit.accept_checks([row], [self.article], snapshot, self.catalog)
        return snapshot, row['reference_coherence']

    def test_unchanged_policy_and_missing_fixture_sentinel_are_accepted(self):
        for present in (False, True):
            with self.subTest(policies_present=present):
                if present:
                    self.write_policies()
                snapshot, certificate = self.capture_and_certificate()
                expected = {name: hashlib.sha256(content).hexdigest() if present else 'missing'
                            for name, content in self.policy.items()}
                self.assertEqual(snapshot['version'], 3)
                self.assertEqual(certificate['version'], 3)
                self.assertEqual(snapshot['policy_sha256'], expected)
                self.assertEqual(certificate['policy_sha256'], expected)
                audit.check_guards(self.db, snapshot)
                self.assertTrue(audit.certificate_current(
                    self.db, self.article, self.body, certificate, self.catalog))
                # No alteration to the model's reference_checks response shape.
                self.assertEqual(set(certificate['assessments'][0]),
                                 {'target_key', 'view_sha256', 'assessment'})

    def test_policy_change_after_capture_is_rejected_before_commit(self):
        for name in self.policy:
            with self.subTest(changed_file=name):
                self.write_policies()
                snapshot, _ = self.capture_and_certificate()
                (self.root / name).write_bytes(self.policy[name] + b' ')
                with self.assertRaisesRegex(ValueError, 'policy changed'):
                    audit.check_guards(self.db, snapshot)
        # Appearance of a policy in a fixture that initially lacked it is also a change.
        for name in self.policy:
            (self.root / name).unlink()
        snapshot, _ = self.capture_and_certificate()
        (self.root / 'site-summaries.json').write_bytes(b'{}')
        with self.assertRaisesRegex(ValueError, 'policy changed'):
            audit.check_guards(self.db, snapshot)

    def test_policy_change_after_certificate_invalidates_unchanged_article(self):
        for name in self.policy:
            with self.subTest(changed_file=name):
                self.write_policies()
                _, certificate = self.capture_and_certificate()
                original_referrer_hash = certificate['referrer_sha256']
                (self.root / name).write_bytes(self.policy[name] + b' ')
                self.assertEqual(audit.digest(self.body), original_referrer_hash)
                self.assertFalse(audit.certificate_current(
                    self.db, self.article, self.body, certificate, self.catalog))
        self.write_policies()
        _, certificate = self.capture_and_certificate()
        (self.root / 'policy-coordinations.json').unlink()
        self.assertFalse(audit.certificate_current(
            self.db, self.article, self.body, certificate, self.catalog))


if __name__ == '__main__':
    unittest.main(verbosity=2)
