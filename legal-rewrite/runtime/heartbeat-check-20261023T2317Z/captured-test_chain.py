"""Isolated temporal/identity guard cases; no production imports, DB or models."""
from pathlib import Path
import ast,copy,unittest
tree=ast.parse(Path(__file__).with_name('observe.py').read_text())
function=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='validate_chain')
scope={};exec(compile(ast.Module(body=[function],type_ignores=[]),'actual validate_chain','exec'),scope)
check=scope['validate_chain']

class ChainGuards(unittest.TestCase):
    def fixture(self):return [11,22,dict(pid=11,exit_code=0,stop_requested=True,ended_at_unix=40),30,[dict(pid=11,launched_at_unix=20),dict(pid=22,launched_at_unix=50)],10,dict(pid=22,started_at_unix=55),52]
    def rejects(self,change):
        f=self.fixture();change(f)
        with self.assertRaises((ValueError,KeyError,TypeError)):check(*f)
    def test_actual_two_launch_chain(self):check(*self.fixture())
    def test_old_receipt_cannot_describe_other_pid(self):self.rejects(lambda f:f[2].update(pid=9))
    def test_success_without_stop_is_different_history(self):self.rejects(lambda f:f[2].update(stop_requested=False))
    def test_abnormal_exit_does_not_pass(self):self.rejects(lambda f:f[2].update(exit_code=1))
    def test_no_live_observation_after_exit(self):self.rejects(lambda f:f.__setitem__(3,41))
    def test_one_launch_is_not_two(self):self.rejects(lambda f:f[4].pop())
    def test_extra_launch_is_not_ignored(self):self.rejects(lambda f:f[4].append(dict(pid=33,launched_at_unix=70)))
    def test_launch_before_exit_rejected(self):self.rejects(lambda f:f[4][1].update(launched_at_unix=35))
    def test_birth_before_launch_rejected(self):self.rejects(lambda f:f.__setitem__(7,49))
    def test_run_not_tied_to_birth_rejected(self):self.rejects(lambda f:f[6].update(started_at_unix=80))
    def test_old_pid_cannot_be_adopted_as_new(self):self.rejects(lambda f:f.__setitem__(1,11))
    def test_unknown_exit_is_not_zero(self):self.rejects(lambda f:f[2].pop('exit_code'))

if __name__=='__main__':unittest.main()
