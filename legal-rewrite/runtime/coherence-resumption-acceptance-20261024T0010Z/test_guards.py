"""Pure isolated selector/disposition and preservation tests; no model or DB."""
from pathlib import Path
import ast,copy,unittest
OUT=Path(__file__).resolve().parent
def extracted(name,file,scope=None):
    tree=ast.parse((OUT/file).read_text());fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name==name)
    values={} if scope is None else scope
    exec(compile(ast.Module(body=[fn],type_ignores=[]),str(file),'exec'),values)
    return values[name]
select=extracted('select_review','accepted_work_selected.py',{'GuardError':ValueError})
scope={'FIELDS':['source_sha256','status','proposed_xml','reason','review_notes']}
scope['values']=extracted('values','continuation_checks.py',scope)
check=extracted('rejected_disposition','continuation_checks.py',scope)

class Guards(unittest.TestCase):
    def metric(self,job='a',pid=22,outcome='reviewed',kind='review',at=9):
        return dict(job=job,coordinator_pid=pid,outcome=outcome,kind=kind,finished_at_unix=at)
    def fixture(self):
        before=dict(source_sha256='s',status='rewrite_draft',proposed_xml='before',reason='r',review_notes='n')
        after=before|{'proposed_xml':'after'}
        return before,after,{'k':dict(previous_draft=before.copy(),answer=after.copy())}
    def test_selects_explicit_success(self):self.assertEqual(select([self.metric(),self.metric('b',at=10)],22,'a')['job'],'a')
    def test_no_job_keeps_latest_behavior(self):self.assertEqual(select([self.metric(),self.metric('b',at=10)],22)['job'],'b')
    def test_other_coordinator_rejected(self):
        with self.assertRaises(ValueError):select([self.metric(pid=11)],22,'a')
    def test_failed_result_rejected(self):
        with self.assertRaises(ValueError):select([self.metric(outcome='stale_policy')],22,'a')
    def test_new_kind_not_review(self):
        with self.assertRaises(ValueError):select([self.metric(kind='new')],22,'a')
    def test_missing_explicit_job_rejected(self):
        with self.assertRaises(ValueError):select([self.metric()],22,'b')
    def test_duplicate_metric_not_silently_chosen(self):
        with self.assertRaises(ValueError):select([self.metric(),self.metric()],22,'a')
    def test_empty_unknown_is_not_success(self):
        with self.assertRaises(ValueError):select([],22,'a')
    def test_pending_whole_beforeimage_preserved(self):
        b,a,p=self.fixture();self.assertTrue(check('k',b,scope['values'](b),'pending',{}).startswith('pending'))
    def test_changed_pending_without_proof_rejected(self):
        b,a,p=self.fixture()
        with self.assertRaises(ValueError):check('k',b,scope['values'](a),'pending',{})
    def test_completed_flag_alone_rejected(self):
        b,a,p=self.fixture()
        with self.assertRaises(ValueError):check('k',b,scope['values'](b),'completed',{})
    def test_true_recovery_accepted(self):
        b,a,p=self.fixture();self.assertTrue(check('k',b,scope['values'](a),'completed',p).startswith('freshly'))
    def test_retained_identical_fields_still_requires_full_proof(self):
        b,a,p=self.fixture();p['k']['answer']=b.copy();self.assertTrue(check('k',b,scope['values'](b),'completed',p).startswith('freshly'))
    def test_wrong_whole_prior_rejected(self):
        b,a,p=self.fixture();p['k']['previous_draft']['reason']='intervening'
        with self.assertRaises(ValueError):check('k',b,scope['values'](a),'completed',p)
    def test_accepted_answer_db_change_rejected(self):
        b,a,p=self.fixture()
        with self.assertRaises(ValueError):check('k',b,scope['values'](b),'completed',p)
    def test_accepted_but_no_completed_rejected(self):
        b,a,p=self.fixture()
        with self.assertRaises(ValueError):check('k',b,scope['values'](a),'pending',p)
    def test_unknown_review_status_rejected(self):
        b,a,p=self.fixture()
        with self.assertRaises(ValueError):check('k',b,scope['values'](b),'unknown',{})
    def test_whole_beforeimage_field_absence_rejected(self):
        b,a,p=self.fixture();p['k']['previous_draft'].pop('review_notes')
        with self.assertRaises(KeyError):check('k',b,scope['values'](a),'completed',p)
    def test_selector_is_the_only_accepted_review_function_change(self):
        old=next(n for n in ast.parse((OUT/'accepted_work_original.py').read_text()).body if isinstance(n,ast.FunctionDef) and n.name=='accepted_review')
        actual=next(n for n in ast.parse((OUT/'accepted_work_selected.py').read_text()).body if isinstance(n,ast.FunctionDef) and n.name=='accepted_review')
        old.args.args.append(ast.arg(arg='job'));old.args.defaults.append(ast.Constant(None))
        for i,n in enumerate(old.body):
            if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='metric':
                old.body[i]=ast.parse('metric=select_review(candidates,pid,job)').body[0]
        self.assertEqual(ast.dump(old),ast.dump(actual))
    def test_two_launch_guard_exactly_preserved(self):
        old=next(n for n in ast.parse((OUT/'observe_original.py').read_text()).body if isinstance(n,ast.FunctionDef) and n.name=='validate_chain')
        new=next(n for n in ast.parse((OUT/'observe_v2.py').read_text()).body if isinstance(n,ast.FunctionDef) and n.name=='validate_chain')
        self.assertEqual(ast.dump(old),ast.dump(new))

if __name__=='__main__':unittest.main()
