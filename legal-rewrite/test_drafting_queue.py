from unittest import TestCase
from unittest.mock import patch
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import hashlib
import io
import threading
from contextlib import redirect_stdout
from types import SimpleNamespace
import run_exhaustive as coordinator
from ingest import open_db

from run_exhaustive import interleave_jobs, policy_is_current, mentions_possible_relief, validate_answer, needs_graphic_source
from review_prior import build_jobs


class DraftingQueue(TestCase):
    def test_one_failed_batch_stays_pending_while_the_next_one_is_registered(self):
        with TemporaryDirectory() as directory:
            root=Path(directory);runtime=root/'runtime';runtime.mkdir()
            (root/'site-summaries.json').write_text('{}')
            (root/'policy-coordinations.json').write_text('{}')
            body='<p>Le délai est de trois mois.</p>'
            sources=[];db=open_db(root/'corpus.sqlite')
            for identifier in ['BAD','GOOD']:
                source={'code_id':'CODE','source_id':identifier,'source_sha256':hashlib.sha256(body.encode()).hexdigest(),
                        'number':identifier,'source_xml':body,'source_notes_xml':''}
                db.execute('INSERT INTO articles VALUES(?,?,?,?,?,?,?,?,?,?)',('CODE',identifier,identifier,'2020-01-01','2999-01-01','VIGUEUR',body,body,source['source_sha256'],'archive'))
                sources.append(source)
            db.commit();db.close()
            def child(*args,**kwargs):
                folder=kwargs['cwd']
                if folder.name.endswith('00001'):return SimpleNamespace(returncode=1)
                row={k:sources[1][k] for k in ['code_id','source_id','source_sha256','number']}
                row.update(proposed_xml='<p>Le délai applicable est fixé à trois mois.</p>',reason='Clarifie le délai.',review_notes='Les trois mois sont conservés.')
                (folder/'answer.json').write_text(json.dumps([row]))
                (folder/'result.json').write_text(json.dumps({'output_file':'answer.json','article_count':1}))
                return SimpleNamespace(returncode=0)
            with patch.object(coordinator,'HERE',root),patch.object(coordinator,'RUNTIME',runtime),patch.object(coordinator,'STOP',threading.Event()),patch.object(coordinator.subprocess,'run',side_effect=child),redirect_stdout(io.StringIO()):
                coordinator.run_job(('travail',1,[sources[0]]),'mock',{'travail':sources})
                self.assertFalse(coordinator.STOP.is_set())
                coordinator.run_job(('travail',2,[sources[1]]),'mock',{'travail':sources})
            db=open_db(root/'corpus.sqlite')
            self.assertIsNone(db.execute("SELECT proposed_xml FROM drafts WHERE source_id='BAD'").fetchone())
            self.assertIsNotNone(db.execute("SELECT proposed_xml FROM drafts WHERE source_id='GOOD'").fetchone())
            db.close()
            status=json.loads((runtime/'status.json').read_text())
            self.assertEqual((status['drafted_articles'],status['pending']),(1,1))
            self.assertFalse(json.loads((runtime/'failed-jobs.json').read_text())[0]['accepted'])

    def test_recovered_graphic_article_is_released_but_incomplete_one_is_held(self):
        article={'source_xml':'<p>Vous pouvez consulter le tableau dans le Journal officiel.</p>'}
        self.assertTrue(needs_graphic_source(article))
        companion={'expected_markers':1,'documentary_recovery_complete':True,
                   'documents':[{'path':'source.pdf'}],
                   'transcriptions':[{'marker':1,'text':'Formule entière vérifiée'}]}
        article['source_companions']=companion
        self.assertFalse(needs_graphic_source(article))
        companion['transcriptions']=[]
        self.assertTrue(needs_graphic_source(article))

    def test_favourable_relief_requires_an_explicit_review_before_acceptance(self):
        source={'code_id':'CODE','source_id':'ARTICLE','source_sha256':'hash','number':'L1',
                'source_xml':'<p>Les entreprises sont exonérées de cette taxe dans les conditions prévues au présent article.</p>',
                'benefit_check_required':True}
        row={k:source[k] for k in ['code_id','source_id','source_sha256','number']}
        row.update(proposed_xml='<p>Les entreprises bénéficient d’une exonération de cette taxe selon les conditions du présent article.</p>',
                   reason='Conserver cette exonération.',review_notes='Contrôler les conditions dans les articles liés.')
        self.assertTrue(mentions_possible_relief(source['source_xml']))
        with self.assertRaisesRegex(ValueError,'Explicit benefit review'):
            validate_answer([row],[source])
        row['benefit_review']='L’exonération des entreprises reste ouverte à toutes les situations futures remplissant les conditions du présent article ; aucune condition ni restriction supplémentaire n’est introduite.'
        self.assertEqual(validate_answer([row],[source]),[row])

    def test_work_from_old_author_instructions_is_rejected(self):
        with TemporaryDirectory() as directory:
            root=Path(directory)
            job=root/'job';job.mkdir()
            policy={'preserved_benefits':['TASCOM','coastal']}
            for name in ['coordination.json','policy.json']:
                (job/name).write_text(json.dumps(policy))
            for name in ['policy-coordinations.json','site-summaries.json']:
                (root/name).write_text(json.dumps(policy,indent=2))
            with patch('run_exhaustive.HERE',root):
                self.assertTrue(policy_is_current(job))
                (root/'policy-coordinations.json').write_text(json.dumps({'preserved_benefits':['TASCOM']}))
                self.assertFalse(policy_is_current(job))

    def test_new_drafting_and_review_both_advance(self):
        new = ['new1', 'new2', 'new3', 'new4', 'new5']
        old = ['old1', 'old2', 'old3']
        scheduled = interleave_jobs(new, old)
        self.assertEqual(scheduled[:3], [('new1', False), ('new2', False), ('old1', True)])
        self.assertEqual([j for j, review in scheduled if not review], new)
        self.assertEqual([j for j, review in scheduled if review], old)
        self.assertEqual(len(scheduled), len(new)+len(old))

    def test_remaining_queue_is_never_dropped(self):
        self.assertEqual(interleave_jobs([], ['review']), [('review', True)])
        self.assertEqual(interleave_jobs(['new'], []), [('new', False)])
        self.assertEqual(interleave_jobs([], []), [])

    def test_zero_interval_cannot_stall_queue(self):
        with self.assertRaises(ValueError):
            interleave_jobs(['new'], [], 0)

    def test_every_code_gets_a_review_before_the_second_batch(self):
        sources = {
            'travail': [self.article(i) for i in range(25)],
            'impots': [self.article(25)],
            'logement': [self.article(26)],
        }
        with patch('review_prior.pending_sources', return_value=sources):
            jobs = build_jobs({})
        self.assertEqual([slug for slug, _, _ in jobs[:3]], ['travail', 'impots', 'logement'])
        seen = [a['id'] for _, _, articles in jobs for a in articles]
        self.assertEqual(sorted(seen), list(range(27)))
        self.assertEqual(len(seen), len(set(seen)))
        self.assertTrue(all(len(articles)<=12 for _, _, articles in jobs))

    def test_long_article_is_whole_and_not_skipped(self):
        sources = {'impots': [self.article(1, 60000), self.article(2)]}
        with patch('review_prior.pending_sources', return_value=sources):
            jobs = build_jobs({})
        self.assertEqual(len(jobs), 2)
        self.assertEqual(len(jobs[0][2][0]['source_xml']), 60000)
        self.assertEqual(jobs[1][2][0]['id'], 2)

    @staticmethod
    def article(identifier, length=10):
        return {'id': identifier, 'source_xml': 'x'*length,
                'previous_draft': {'proposed_xml': 'y'}}
