"""Offline checks of proposed helper and actual patched queue functions."""
from pathlib import Path
from types import ModuleType, SimpleNamespace
from unittest import TestCase, main
from unittest.mock import patch
from tempfile import TemporaryDirectory
import ast, copy, itertools, json, sys

LEGAL = Path(__file__).resolve().parent
FOLDER = LEGAL/'runtime/contrat-unique-20261019/priority'
cu = ModuleType('cu_proposal_test')
cu.__file__ = str(LEGAL/'contrat_unique_priority.py')
exec(compile((LEGAL/'contrat_unique_priority.py').read_text(),cu.__file__,'exec'),cu.__dict__)
SHA = 'a'*64
KEY = ('WORK','A')

def article(identifier='A', priority=True, sru=False, length=20):
    return {'code_id':'WORK','source_id':identifier,'source_sha256':SHA if priority else 'b'*64,
            'source_xml':'x'*length,'source_notes_xml':'','previous_draft':{'proposed_xml':'y'},
            'sru_context':[{'id':'SRU'}] if sru else []}

def function_node(path, name):
    return next(n for n in ast.parse(path.read_text()).body if isinstance(n, ast.FunctionDef) and n.name == name)

def exec_nodes(nodes, namespace):
    exec(compile(ast.fix_missing_locations(ast.Module(body=nodes,type_ignores=[])),'proposed-queue','exec'),namespace)

def sru(job):
    return 0 if any(a.get('sru_context') for a in job[2]) else 1

class ExactPriorityTests(TestCase):
    def test_exact_identity_and_hash(self):
        self.assertEqual(cu.article_priority(article(),{KEY:SHA}),0)
        for changed in [article(priority=False),article()|{'code_id':'OTHER'},article('B'),{'source_id':'A','code_id':'WORK'}]:
            self.assertEqual(cu.article_priority(changed,{KEY:SHA}),1)

    def test_generic_words_cannot_promote_an_article(self):
        self.assertEqual(cu.article_priority(article('B')|{'source_xml':'CDD rupture préavis intérim'}, {KEY:SHA}),1)

    def test_empty_job_is_ordinary(self):
        self.assertEqual(cu.priority(('travail',1,[]),{KEY:SHA}),1)

    def test_load_targets_and_reject_duplicate_or_bad_guard(self):
        with TemporaryDirectory() as directory:
            path=Path(directory)/'targets.json'
            row={'code_id':'WORK','source_id':'A','source_sha256':SHA}
            path.write_text(json.dumps({'schema_version':1,'targets':[row]}))
            self.assertEqual(cu.load_targets(path),{KEY:SHA})
            for data in [{'schema_version':2,'targets':[]}, {'schema_version':1,'targets':[row,row]},
                         {'schema_version':1,'targets':[row|{'source_sha256':'short'}]}]:
                cu.load_targets.cache_clear();path.write_text(json.dumps(data))
                with self.assertRaises(ValueError):cu.load_targets(path)

class ManifestGuards(TestCase):
    def setUp(self):
        self.entry={'code_id':'WORK','source_id':'A','source_sha256':SHA,'proposed_sha256':'b'*64,'review_status':'completed'}
        self.manifest={'prior_articles':[self.entry],'completed_second_pass':1,'prior_draft_count_at_directive':5932}
        self.operation={'code_id':'WORK','source_id':'A','source_sha256':SHA,'proposed_sha256':'b'*64,
                        'previous_manifest_entry':copy.deepcopy(self.entry),'reason':'CDD explicitement prévu dans le texte.'}
        self.sources={KEY:SHA};self.drafts={KEY:'b'*64}

    def propose(self, operations=None, sources=None, drafts=None, guard=None):
        return cu.propose_review_manifest(self.manifest, operations if operations is not None else [self.operation],
            self.sources if sources is None else sources,self.drafts if drafts is None else drafts,
            guard or cu.object_digest(self.manifest))

    def test_reopens_completed_preserving_history_without_mutation(self):
        before=copy.deepcopy(self.manifest);result=self.propose()
        self.assertEqual(self.manifest,before)
        self.assertEqual(result['prior_articles'][0]['review_status'],'pending')
        self.assertEqual(result['completed_second_pass'],0)
        self.assertEqual(result['prior_draft_count_at_directive'],5932)
        self.assertEqual(result['prior_articles'][0]['contract_unique_review_history'][0]['previous_entry'],self.entry)
        self.assertFalse(result['contract_unique_reopen_proposal']['counts_as_rewritten'])

    def test_manifest_guard_fails_closed(self):
        with self.assertRaisesRegex(ValueError,'manifest changed'):self.propose(guard='c'*64)

    def test_source_guard_fails_closed(self):
        with self.assertRaisesRegex(ValueError,'source changed'):self.propose(sources={KEY:'c'*64})

    def test_draft_guard_fails_closed(self):
        with self.assertRaisesRegex(ValueError,'Draft changed'):self.propose(drafts={KEY:'c'*64})

    def test_entry_guard_fails_closed(self):
        op=self.operation|{'previous_manifest_entry':None}
        with self.assertRaisesRegex(ValueError,'entry changed'):self.propose(operations=[op])

    def test_duplicate_operation_fails_closed(self):
        with self.assertRaisesRegex(ValueError,'Duplicate'):self.propose(operations=[self.operation,self.operation])

    def test_missing_entry_is_added_only_with_explicit_none_guard(self):
        self.manifest['prior_articles']=[]
        result=self.propose(operations=[self.operation|{'previous_manifest_entry':None}])
        self.assertEqual(len(result['prior_articles']),1)
        self.assertEqual(result['prior_articles'][0]['review_status'],'pending')

class ActualQueueTests(TestCase):
    def setUp(self):
        self.targets={('WORK',str(i)):SHA for i in range(30)}
        self.priority=lambda a:cu.article_priority(a,self.targets)
        self.job_priority=lambda job:cu.priority(job,self.targets)

    def test_review_chunks_keep_priority_bands_separate_and_sru_second(self):
        rows=[article('ordinary',sru=True)]+[article(str(i)) for i in range(15)]+[article('last')]
        namespace={'pending_sources':lambda _: {'travail':copy.deepcopy(rows)},'json':json,'itertools':itertools,
                   'cu_article_priority':self.priority,'cu_priority':self.job_priority,'sru_priority':sru}
        exec_nodes([function_node(LEGAL/'review_prior.py','build_jobs')],namespace)
        jobs=namespace['build_jobs']({})
        self.assertEqual([self.job_priority(j) for j in jobs],[0,0,1])
        self.assertEqual([len(j[2]) for j in jobs],[12,3,2])
        self.assertEqual([a['source_id'] for a in jobs[-1][2]],['ordinary','last'])
        self.assertEqual(len({a['source_id'] for j in jobs for a in j[2]}),17)
        self.assertTrue(all(len({self.priority(a) for a in j[2]})==1 for j in jobs))

    def test_review_long_article_stays_complete_and_ordinary_round_robin_survives(self):
        sources={'travail':[article('ordinary',length=60000),article('tail')],
                 'impots':[article('tax')]}
        namespace={'pending_sources':lambda _:copy.deepcopy(sources),'json':json,'itertools':itertools,
                   'cu_article_priority':self.priority,'cu_priority':self.job_priority,'sru_priority':sru}
        exec_nodes([function_node(LEGAL/'review_prior.py','build_jobs')],namespace)
        jobs=namespace['build_jobs']({})
        self.assertEqual([j[0] for j in jobs],['travail','impots','travail'])
        self.assertEqual(len(jobs[0][2][0]['source_xml']),60000)

    def test_actual_new_queue_contract_before_sru_and_no_chunk_contamination(self):
        main_node=function_node(LEGAL/'run_exhaustive.py','main')
        start=next(i for i,n in enumerate(main_node.body) if isinstance(n,ast.Assign) and ast.unparse(n).startswith('sources = load_sources'))
        finish=next(i for i,n in enumerate(main_node.body) if i>start and isinstance(n,ast.Expr) and ast.unparse(n).startswith('jobs.sort'))
        rows=[article('ordinary',sru=True)]+[article(str(i)) for i in range(25)]+[article('last')]
        with TemporaryDirectory() as directory:
            namespace={'load_sources':lambda _: {'travail':copy.deepcopy(rows)},'SLUGS':['travail'],
                       'args':SimpleNamespace(slugs='travail'),'existing':set(),'needs_graphic_source':lambda _:False,
                       'json':json,'HERE':Path(directory),'cu_article_priority':self.priority,
                       'cu_priority':self.job_priority,'sru_priority':sru}
            exec_nodes(main_node.body[start:finish+1],namespace)
        jobs=namespace['jobs']
        self.assertEqual([self.job_priority(j) for j in jobs],[0,0,1])
        self.assertEqual([len(j[2]) for j in jobs],[24,1,2])
        self.assertEqual(len({a['source_id'] for j in jobs for a in j[2]}),27)

    def test_interleave_sorts_priority_before_max_jobs_cut(self):
        source=LEGAL/'run_exhaustive.py'
        main_node=function_node(source,'main')
        interleave_if=next(n for n in main_node.body if isinstance(n,ast.If) and ast.unparse(n.test)=='args.interleave_review')
        helper_ns={};exec_nodes([function_node(source,'interleave_jobs')],helper_ns)
        new=[('travail',1,[article('0')]),('travail',2,[article('ordinary',sru=True)])]
        review=[('travail',3,[article('1')]),('travail',4,[article('2')])]
        namespace={'args':SimpleNamespace(interleave_review=True,max_jobs=2),'jobs':new,
                   'interleave_jobs':helper_ns['interleave_jobs'],'sources':{},'RUNTIME':Path('/unused'),
                   'atomic':lambda *args:None,'print':lambda *args,**kwargs:None,
                   'cu_mixed_priority':lambda item:self.job_priority(item[0])}
        with patch.dict(sys.modules,{'review_prior':SimpleNamespace(build_jobs=lambda _:review)}):
            exec_nodes([interleave_if],namespace)
        self.assertEqual([(j[1],old) for j,old in namespace['scheduled']],[(1,False),(3,True)])

class RealInventoryGuards(TestCase):
    def test_exclusions_and_snapshot_arithmetic(self):
        targets=json.loads((FOLDER/'priority-targets.proposed.json').read_text())['targets']
        excluded=json.loads((FOLDER/'excluded-packs.json').read_text())
        # Generator report is also checked independently of any pipeline side effect.
        report=json.loads((FOLDER/'guard-report.json').read_text())
        excluded_rows=excluded['records'] if isinstance(excluded,dict) else excluded
        keys=lambda rows:{(r['code_id'],r['source_id']) for r in rows}
        self.assertFalse(keys(targets)&keys(excluded_rows))
        self.assertEqual(len(keys(targets)),len(targets))
        self.assertEqual(report['guard_failures'],[])
        counts=report['counts']
        self.assertEqual(len(targets),counts.get('reopen_completed',0)+counts.get('already_pending_guard_current',0)+counts.get('first_draft_priority',0)+counts.get('append_new_review_candidate',0)+counts.get('refresh_pending_guard',0))
        extras=json.loads((FOLDER/'outside-initial-inventory-leads.json').read_text())
        self.assertEqual(len(extras),48)
        self.assertTrue(keys(extras)<=keys(targets))

if __name__=='__main__':main()
