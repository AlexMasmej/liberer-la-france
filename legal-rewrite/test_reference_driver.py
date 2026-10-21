"""Real reviewed run_job with mocked worker and isolated temporary database."""
from pathlib import Path
from unittest import TestCase,main
from unittest.mock import patch
from tempfile import TemporaryDirectory
from types import ModuleType,SimpleNamespace
from contextlib import contextmanager,redirect_stdout
import io,json,sys,threading
from test_reference_integrity_regressions import audit,P,LEGAL
from ingest import open_db
from test_execution_fixture import emit_cli_startup

class DriverBranches(TestCase):
    def setUp(self):
        self.tmp=TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name);self.runtime=self.root/'runtime';self.runtime.mkdir()
        for name in ['site-summaries.json','policy-coordinations.json']:(self.root/name).write_text('{}')
        self.module=ModuleType('reviewed_driver');self.module.__file__=str(LEGAL/'run_exhaustive.py')
        with patch.dict(sys.modules,{'reference_coherence':audit}):
            exec(compile((LEGAL/'run_exhaustive.py').read_text(),self.module.__file__,'exec'),self.module.__dict__)
        self.rows=[];self.catalog={};db=open_db(self.root/'corpus.sqlite')
        for identifier,number,body in [('A','L10-1','<p>Le salarié bénéficie des garanties de L20-1.</p>'),('B','L20-1','<p>Garantie officielle B.</p>'),('C','L20-2','<p>Garantie officielle C.</p>')]:
            sha=audit.digest(body)
            row={'code_id':'CODE','source_id':identifier,'number':number,'source_xml':body,'source_notes_xml':'','source_sha256':sha}
            self.rows.append(row);self.catalog[audit.key(row)]=row
            db.execute('INSERT INTO articles VALUES(?,?,?,?,?,?,?,?,?,?)',('CODE',identifier,number,'2020-01-01','2999-01-01','VIGUEUR',body,body,sha,'test-official'))
        self.b1='<p>Garantie proposée B, première version complète.</p>'
        db.execute('INSERT INTO drafts VALUES(?,?,?,?,?,?,?)',('CODE','B',self.rows[1]['source_sha256'],'rewrite_draft',self.b1,'Clarifie B.','Contrôler B.'))
        db.commit();db.close()

    def run_case(self,mode):
        calls=[];held=[];guard_checks=[]
        @contextmanager
        def lock():
            held.append(True)
            try:yield
            finally:held.pop()
        original_guard=audit.check_guards
        def guarded(db,snapshot):
            self.assertTrue(held,'New-draft guard must run under writer lock')
            self.assertTrue(db.in_transaction,'New-draft guard must share registration transaction')
            guard_checks.append(snapshot)
            return original_guard(db,snapshot)
        def worker(*args,**kwargs):
            emit_cli_startup(kwargs)
            folder=kwargs['cwd'];snapshot=json.loads((folder/'reference-targets.json').read_text())
            self.assertFalse((folder/'answer.json').exists(),'Old worker answer must be removed before retry')
            self.assertFalse((folder/'result.json').exists(),'Old worker result must be removed before retry')
            if calls:
                previous=json.loads((folder/'previous-answer.json').read_text())
                self.assertEqual(previous[0]['source_id'],self.rows[0]['source_id'])
                self.assertEqual(previous[0]['source_sha256'],self.rows[0]['source_sha256'])
                self.assertEqual(previous[0]['proposed_xml'],calls[0]['draft_body'])
            body='<p>Les garanties de L20-1 s’appliquent au salarié pendant l’exécution du contrat.</p>'
            if mode=='new_ref':body='<p>Les garanties de L20-1 et de L20-2 s’appliquent au salarié pendant l’exécution du contrat.</p>'
            row={k:self.rows[0][k] for k in ['code_id','source_id','source_sha256','number']}
            row.update(proposed_xml=body,status='rewrite_draft',reason='Préserve les garanties visées.',review_notes='Renvois examinés sur leurs textes complets.',
                       reference_checks=[{'target_key':k,'view_sha256':v['view_sha256'],
                         'assessment':'La cible '+k+' conserve les garanties du salarié et sa transition applicable ; aucun droit des anciens contrats ni avantage des futures situations éligibles n’est retiré.'} for k,v in snapshot['targets'].items()])
            if calls and mode=='target_change':self.assertEqual(snapshot['targets']['CODE|B']['proposed_xml'],'<p>Garantie B modifiée par un auteur concurrent.</p>')
            if calls and mode=='new_ref':self.assertIn('CODE|C',snapshot['targets'])
            (folder/'answer.json').write_text(json.dumps([row]))
            (folder/'result.json').write_text(json.dumps({'output_file':'answer.json','article_count':1}))
            if not calls and mode=='target_change':
                db=open_db(self.root/'corpus.sqlite');db.execute('UPDATE drafts SET proposed_xml=? WHERE source_id=?',('<p>Garantie B modifiée par un auteur concurrent.</p>','B'));db.commit();db.close()
            calls.append(snapshot|{'draft_body':body})
            return SimpleNamespace(returncode=0)
        with patch.object(self.module,'HERE',self.root),patch.object(self.module,'ROOT',self.root),patch.object(self.module,'RUNTIME',self.runtime),patch.object(self.module,'STOP',threading.Event()),patch.object(self.module,'past_before_job',return_value=[]),patch.object(self.module,'writer_lock',lock),patch.object(self.module,'invoke_agent',side_effect=worker),patch.object(audit,'focus',return_value=self.catalog),patch.object(audit,'check_guards',side_effect=guarded),redirect_stdout(io.StringIO()):
            self.module.run_job(('travail',1,[self.rows[0]]),'NO_MODEL',{'travail':self.rows})
        self.assertEqual(len(calls),2)
        answer=json.loads((self.runtime/'jobs/travail-00001/answer.json').read_text())[0]
        batch=json.loads((self.root/'batches/automatic-travail/00001.json').read_text())[0]
        self.assertEqual(answer['proposed_xml'],batch['proposed_xml'])
        db=open_db(self.root/'corpus.sqlite')
        try:
            self.assertTrue(audit.certificate_current(db,self.rows[0],batch['proposed_xml'],batch['reference_coherence'],self.catalog))
        finally:db.close()
        self.assertTrue(guard_checks)

    def test_changed_target_retries_with_fresh_snapshot_and_cleared_outputs(self):
        self.run_case('target_change')

    def test_new_reference_on_first_answer_is_frozen_on_retry(self):
        self.run_case('new_ref')

if __name__=='__main__':main(verbosity=2)
