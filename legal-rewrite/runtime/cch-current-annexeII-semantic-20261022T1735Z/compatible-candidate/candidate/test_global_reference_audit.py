"""Meaningful parser, conservative resolution and source non-mutation checks."""
import json
from pathlib import Path
import re
import contextlib
import io
import sqlite3
import tempfile
import unittest

from global_reference_audit import (
    ANNEXES, CGI, WORK, Catalog, audit, digest, expand_range, file_digest,
    normalize, official_state_class, readonly, repeal_proposed, snapshot_database,
    strongly_connected, text_references,
)


class ParserTests(unittest.TestCase):
    def refs(self, value, own=WORK):
        return text_references(value, own)

    def test_prefixed_range_expands_every_member(self):
        refs = self.refs('Les articles L. 1234-1 à L. 1234-3 du code du travail.')
        self.assertEqual([r['number'] for r in refs], ['L1234-1', 'L1234-2', 'L1234-3'])
        self.assertEqual({r['code_id'] for r in refs}, {WORK})

    def test_range_without_article_trigger_and_shorthand(self):
        refs = self.refs('Voir L. 1234-1 à 3 du présent code.')
        self.assertEqual([r['number'] for r in refs], ['L1234-1', 'L1234-2', 'L1234-3'])
        self.assertEqual({r['code_id'] for r in refs}, {WORK})

    def test_cgi_numbers_suffixes_and_annex(self):
        refs = self.refs('Les articles 39 decies A, 39 decies B et 302 septies A bis du code général des impôts.')
        self.assertEqual([r['number'] for r in refs], ['39DECIESA', '39DECIESB', '302SEPTIESABIS'])
        self.assertEqual({r['code_id'] for r in refs}, {CGI})
        self.assertEqual(self.refs('Article 14 de l’annexe II au code général des impôts.')[0]['code_id'], ANNEXES['II'])

    def test_numeric_cgi_range(self):
        refs = self.refs('Articles 39 à 41 du CGI.')
        self.assertEqual([r['number'] for r in refs], ['39', '40', '41'])
        self.assertEqual({r['code_id'] for r in refs}, {CGI})

    def test_incompatible_ranges_not_invented(self):
        self.assertIsNone(expand_range('L1234-1', 'L1244-3'))
        self.assertIsNone(expand_range('39 bis', '39 ter'))
        self.assertIsNone(expand_range('1', '5000'))
        refs = self.refs('Articles L. 1234-1 à L. 1244-3 du code du travail.')
        self.assertEqual(refs[-1]['range_unexpanded'], ['L. 1234-1', 'L. 1244-3'])

    def test_external_code_not_attributed_to_source_code(self):
        ref = self.refs('Article 131-35 du code pénal.')[0]
        self.assertEqual(ref['qualification'], 'explicit_external_code_title_unresolved')
        self.assertTrue(ref['code_id'].startswith('external:'))

    def test_non_codified_instrument_is_external(self):
        ref = self.refs('Article 8 de l’ordonnance n° 2022-1076.')[0]
        self.assertEqual(ref['qualification'], 'explicit_external_instrument')

    def test_unqualified_and_same_code_antecedent_remain_uncertain(self):
        self.assertIsNone(self.refs('Article 39.')[0]['code_id'])
        self.assertEqual(self.refs('Article 39 du même code.')[0]['qualification'], 'ambiguous_same_code_antecedent')

    def test_scope_and_historical_markers(self):
        ref = self.refs('Le 2° du I de l’article 39 du CGI, dans son ancienne rédaction.')[0]
        self.assertTrue(ref['subdivision_context'])
        self.assertTrue(ref['historical_context'])

    def test_markup_and_entities(self):
        refs = self.refs('<p>articles <b>L. 1234-1</b> et L.&nbsp;1234-2 du présent code.</p>')
        self.assertEqual([r['number'] for r in refs], ['L1234-1', 'L1234-2'])

    def test_following_sentence_does_not_supply_code(self):
        ref = self.refs('Article 39. Le code du travail est modifié.')[0]
        self.assertIsNone(ref['code_id'])

    def test_preceding_sentence_does_not_supply_code(self):
        ref = self.refs('Le code général des impôts est modifié. Article L. 1234-1.')[0]
        self.assertIsNone(ref['code_id'])

    def test_cgi_multiletter_suffix_and_first_article(self):
        refs = self.refs('Les articles 150 U, 150 UB et 171 AS bis du CGI.')
        self.assertEqual([r['number'] for r in refs], ['150U', '150UB', '171ASBIS'])
        self.assertEqual(self.refs('Article 1er du présent code.')[0]['number'], '1')

    def test_deferred_repeal_is_not_current_repeal(self):
        self.assertEqual(official_state_class('ABROGE_DIFF'), 'scheduled_transition_not_current_repeal')
        self.assertEqual(official_state_class('ABROGE'), 'official_inactive_state')

    def test_canonical_external_title_and_unhyphenated_number(self):
        aliases = [(re.compile('livre des procedures fiscales', re.I), 'LPF_VERIFIED_FIXTURE', 'Livre des procédures fiscales')]
        ref = text_references('L’article L. 32 du livre des procédures fiscales.', WORK, aliases)[0]
        self.assertEqual(ref['number'], 'L32')
        self.assertEqual(ref['code_id'], 'LPF_VERIFIED_FIXTURE')
        self.assertEqual(ref['qualification'], 'explicit_canonical_code_title')

    def test_previous_article_qualifier_not_borrowed_by_next_article(self):
        refs = self.refs('Article 976 du code général des impôts, l’article 281 F et le I de l’article 281 H.', ANNEXES['III'])
        self.assertEqual(refs[0]['code_id'], CGI)
        self.assertIsNone(refs[1]['code_id'])
        self.assertIsNone(refs[2]['code_id'])

    def test_historical_combined_code_not_current_urbanisme(self):
        ref = self.refs('Article 274 de l’ancien code de l’urbanisme et de l’habitation.')[0]
        self.assertEqual(ref['code_id'], 'external:historical_urbanisme_et_habitation')
        self.assertTrue(ref['historical_context'])

    def test_substantive_repeal_only_initial_explicit_formula(self):
        self.assertTrue(repeal_proposed('<p>Le présent article est abrogé.</p>'))
        self.assertTrue(repeal_proposed('<p>Abrogé.</p>'))
        self.assertFalse(repeal_proposed('<p>Les références à un article abrogé sont remplacées.</p>'))


def record(code, identifier, number, start='2020-01-01', end='2999-01-01', current=True, state='VIGUEUR'):
    return {'key': code + '|' + identifier, 'code_id': code, 'id': identifier,
            'number': number, 'valid_from': start, 'valid_until': end,
            'in_inventory': current, 'state': state, 'source_sha256': digest(identifier)}


class ResolutionTests(unittest.TestCase):
    def setUp(self):
        self.rows = [record(WORK, 'work1', 'L1234-1'), record(CGI, 'tax1', 'L1234-1'),
                     record(CGI, 'tax39', '39'), record(ANNEXES['II'], 'annex39', '39'),
                     record(WORK, 'old1', 'L1234-1', end='2020-01-01', current=False, state='ABROGE'),
                     record(CGI, 'old40', '40', end='2020-01-01', current=False, state='ABROGE')]
        self.catalog = Catalog(self.rows, [WORK, CGI, ANNEXES['II']], '2026-10-18')

    def test_ambiguous_code_and_explicit_qualification(self):
        resolved = self.catalog.resolve({'number': 'L1234-1'}, WORK)
        self.assertEqual(resolved['status'], 'ambiguous_code_or_version')
        explicit = self.catalog.resolve({'number': 'L1234-1', 'code_id': WORK}, WORK)
        self.assertEqual(explicit['target_key'], WORK + '|work1')

    def test_canonical_code_hint_disambiguates_bare_cgi(self):
        resolved = self.catalog.resolve({'number': '39'}, WORK, {'39': {CGI}})
        self.assertEqual(resolved['target_key'], CGI + '|tax39')
        self.assertEqual(resolved['basis'], 'canonical_citation_code_hint')

    def test_multiple_hints_stay_ambiguous(self):
        result = self.catalog.resolve({'number': '39'}, WORK, {'39': {CGI, ANNEXES['II']}})
        self.assertEqual(result['status'], 'ambiguous_code_or_version')

    def test_exact_historical_target_is_not_redirected(self):
        result = self.catalog.resolve({'number': 'L1234-1', 'code_id': WORK, 'target_id': 'old1'}, WORK)
        self.assertEqual(result['status'], 'historical_identifier')
        self.assertEqual(result['target_key'], WORK + '|old1')
        self.assertEqual(result['current_number_candidates'], [WORK + '|work1'])

    def test_missing_exact_id_is_not_replaced_by_number(self):
        result = self.catalog.resolve({'number': '39', 'code_id': CGI, 'target_id': 'missing'}, WORK)
        self.assertEqual(result['status'], 'unresolved_identifier')
        self.assertNotIn('target_key', result)

    def test_repealed_historical_number_separated_from_missing(self):
        self.assertEqual(self.catalog.resolve({'number': '40', 'code_id': CGI}, WORK)['status'], 'historical_number_only')
        self.assertEqual(self.catalog.resolve({'number': '41', 'code_id': CGI}, WORK)['status'], 'unresolved_number')

    def test_external_code_is_outside_scope(self):
        result = self.catalog.resolve({'number': '39', 'code_id': 'LEGITEXT999999999999'}, WORK)
        self.assertEqual(result['status'], 'outside_scope')

    def test_competing_current_versions_are_not_chosen(self):
        rows = self.rows + [record(WORK, 'work_competing', 'L1234-1')]
        cat = Catalog(rows, [WORK, CGI, ANNEXES['II']], '2026-10-18')
        self.assertEqual(cat.resolve({'number': 'L1234-1', 'code_id': WORK}, WORK)['status'], 'ambiguous_current_version')

    def test_cycles_informational_and_deep_graph_safe(self):
        graph = {str(i): {str(i + 1)} for i in range(2500)}
        graph['2500'] = {'2499'}
        self.assertEqual(strongly_connected(graph), [['2499', '2500']])


class SnapshotTests(unittest.TestCase):
    def test_readonly_backup_does_not_mutate_source(self):
        with tempfile.TemporaryDirectory() as folder:
            source, snapshot = Path(folder) / 'source.sqlite', Path(folder) / 'snapshot.sqlite'
            db = sqlite3.connect(source)
            db.execute('CREATE TABLE evidence(id INTEGER PRIMARY KEY,value TEXT)')
            db.executemany('INSERT INTO evidence(value) VALUES(?)', [(str(i) * 100,) for i in range(1000)])
            db.commit()
            db.close()
            before = file_digest(source)
            captured = snapshot_database(source, snapshot, pages=4)
            self.assertEqual(file_digest(source), before)
            self.assertEqual(captured['quick_check'], 'ok')
            self.assertEqual(captured['snapshot_sha256'], file_digest(snapshot))
            ro = readonly(source)
            with self.assertRaises(sqlite3.OperationalError):
                ro.execute("UPDATE evidence SET value='changed'")
            ro.close()
            check = readonly(snapshot)
            self.assertEqual(check.execute('SELECT COUNT(*) FROM evidence').fetchone()[0], 1000)
            check.close()

    def test_refuses_overwrite_or_source_as_destination(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / 'source.sqlite'
            sqlite3.connect(source).close()
            with self.assertRaises(ValueError):
                snapshot_database(source, source)


class WholeAuditTests(unittest.TestCase):
    def test_deleted_target_differences_and_exact_guards_end_to_end(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder)
            source = output / 'fixture.sqlite'
            db = sqlite3.connect(source)
            db.executescript('''
                CREATE TABLE articles(code_id TEXT,id TEXT,number TEXT,valid_from TEXT,valid_until TEXT,state TEXT,content_xml TEXT,plain_text TEXT,source_sha256 TEXT,archive TEXT);
                CREATE TABLE documents(code_id TEXT,id TEXT,kind TEXT,xml BLOB,sha256 TEXT,archive TEXT);
                CREATE TABLE drafts(code_id TEXT,source_id TEXT,source_sha256 TEXT,status TEXT,proposed_xml TEXT,reason TEXT,review_notes TEXT);
                CREATE TABLE archives(name TEXT,sha256 TEXT);
            ''')
            bodies = {'one': '<p>Les articles L. 1234-2 et L. 1234-4 du présent code s’appliquent.</p>',
                      'two': '<p>La règle est applicable.</p>', 'four': '<p>Autre règle.</p>'}
            hashes = {}
            for identifier, number in [('one', 'L1234-1'), ('two', 'L1234-2'), ('four', 'L1234-4')]:
                body = bodies[identifier]
                raw = ('<ARTICLE><NOTA><CONTENU /></NOTA><BLOC_TEXTUEL><CONTENU>' + body + '</CONTENU></BLOC_TEXTUEL><LIENS /></ARTICLE>').encode()
                sha = digest(raw)
                hashes[identifier] = sha
                db.execute('INSERT INTO articles VALUES(?,?,?,?,?,?,?,?,?,?)',
                           (WORK, identifier, number, '2020-01-01', '2999-01-01', 'VIGUEUR', body, body, sha, 'fixture'))
                db.execute('INSERT INTO documents VALUES(?,?,?,?,?,?)', (WORK, identifier, 'ARTICLE', raw, sha, 'fixture'))
            tree = '<TEXTELR><STRUCT>' + ''.join('<LIEN_ART id="' + identifier + '" />' for identifier in bodies) + '</STRUCT></TEXTELR>'
            db.execute('INSERT INTO documents VALUES(?,?,?,?,?,?)', (WORK, WORK, 'TEXTELR', tree.encode(), digest(tree), 'fixture'))
            proposals = {'one': '<p>Les articles L. 1234-2 et L. 1234-3 du présent code s’appliquent.</p>',
                         'two': '<p>Le présent article est abrogé.</p>'}
            for identifier, body in proposals.items():
                db.execute('INSERT INTO drafts VALUES(?,?,?,?,?,?,?)', (WORK, identifier, hashes[identifier], 'rewrite_draft', body, 'Fixture', 'Fixture'))
            db.commit()
            db.close()
            (output / 'corpus.json').write_text(json.dumps({'codes': [{'id': WORK, 'slug': 'travail', 'title': 'Code du travail'}]}))
            before = file_digest(source)
            with contextlib.redirect_stdout(io.StringIO()):
                audit(source, output, '2026-10-18', {'snapshot_sha256': before, 'policies': {}})
            self.assertEqual(file_digest(source), before)
            summary = json.loads((output / 'summary.json').read_text())
            self.assertEqual(summary['entries_scanned'], 3)
            self.assertEqual(summary['canonical_document_checks']['canonical_body_matches_stored_article_body'], 3)
            findings = [json.loads(line) for line in (output / 'findings.jsonl').read_text().splitlines()]
            kinds = {item['kind'] for item in findings}
            self.assertIn('proposal_refers_to_proposed_repeal', kinds)
            self.assertIn('reference_introduced_in_proposal', kinds)
            self.assertIn('reference_disappeared_from_proposal', kinds)
            repeal = next(item for item in findings if item['kind'] == 'proposal_refers_to_proposed_repeal')
            self.assertEqual(repeal['target_guard']['proposal_sha256'], digest(proposals['two']))
            self.assertEqual(repeal['source_guard']['proposal_sha256'], digest(proposals['one']))
            self.assertFalse(summary['semantic_review_by_jurist'])
            self.assertFalse(summary['automatic_change'])


if __name__ == '__main__':
    unittest.main()
