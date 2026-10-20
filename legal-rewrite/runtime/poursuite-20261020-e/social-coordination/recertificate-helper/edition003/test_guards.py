"""Execute pure AST-selected guards only: no helper import, DB, process or model."""
import ast,copy,pathlib,unittest

P=pathlib.Path(__file__).with_name('prepare_recertificates.py')
tree=ast.parse(P.read_text())
nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in {'require','approved','unchanged_except_references'}]
ns={'ALLOWED':{'reference_checks','reference_coherence'}}
exec(compile(ast.Module(body=nodes,type_ignores=[]),str(P),'exec'),ns)

class Guards(unittest.TestCase):
    def setUp(self):
        self.pairs={('a','target'),('b','target'),('c','target')}
        self.removals={'a':['optional'],'b':['optional'],'c':[]}
        self.approval={'version':1,'approved':True,'approved_by':'root','approved_at':'2026-10-20',
          'capture_sha256':'exact','approved_optional_check_removals':self.removals,
          'analyses':[{'key':a,'target_key':b,'assessment':('Specific actual committed article rule and its unchanged procedural guarantees. ')*2} for a,b in sorted(self.pairs)]}
    def check(self,a=None):return ns['approved'](self.approval if a is None else a,'exact',self.pairs,self.removals)
    def test_exact_root_approval_accepted(self):self.assertEqual(set(self.check()),self.pairs)
    def test_missing_or_wrong_authorization_refused(self):
        for f,v in [('approved',False),('approved_by','agent'),('capture_sha256','other'),('approved_at','')]:
            a=copy.deepcopy(self.approval);a[f]=v
            with self.subTest(field=f),self.assertRaises(ValueError):self.check(a)
    def test_optional_removal_must_be_approved_per_identity(self):
        a=copy.deepcopy(self.approval);del a['approved_optional_check_removals']['b']
        with self.assertRaises(ValueError):self.check(a)
    def test_incomplete_duplicate_or_short_analysis_refused(self):
        for change in ['missing','duplicate','short']:
            a=copy.deepcopy(self.approval)
            if change=='missing':a['analyses'].pop()
            elif change=='duplicate':a['analyses'][1]=a['analyses'][0]
            else:a['analyses'][0]['assessment']='verified'
            with self.subTest(change=change),self.assertRaises(ValueError):self.check(a)
    def test_metadata_only_references_accepted(self):
        old={'proposed_xml':None,'substantive_impact':{'effects':[]},'reason':'same','reference_checks':[]}
        new=old|{'reference_checks':[{'assessment':'new'}],'reference_coherence':{'version':3}}
        ns['unchanged_except_references'](old,new)
    def test_every_other_field_is_preserved(self):
        old={'proposed_xml':'whole text','substantive_impact':{'effects':[]},'reason':'same',
             'benefit_review':'same','status':'rewrite_draft','substantive_impact_certificate':{'hash':'same'}}
        for f in list(old)+['added_field']:
            new=copy.deepcopy(old);new[f]='changed'
            with self.subTest(field=f),self.assertRaises(ValueError):ns['unchanged_except_references'](old,new)
    def test_script_compiles_without_running_it(self):compile(tree,str(P),'exec')

if __name__=='__main__':unittest.main(verbosity=2)
