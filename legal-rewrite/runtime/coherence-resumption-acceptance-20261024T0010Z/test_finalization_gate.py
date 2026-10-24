"""Isolated fail-closed publication boundary cases."""
import copy,unittest
from finalization_gate import require_complete
class Gate(unittest.TestCase):
    def data(self):
        o=dict(new_pid=58195,guarded_phase_matches_current_pid=True,all77_current_pins_match=True,at_utc='2026-10-24T00:00:00+00:00',
          exact_two_launch_history=[dict(pid=41583),dict(pid=58195)],run=dict(started_at_unix=1792790000),
          accepted_review_verification_complete=True,accepted_reviews=[dict(coordinator_pid=58195,rows=[{'id':'a'}],native_execution=dict(verified=True))])
        w=dict(new_pid=58195,at_utc='2026-10-23T23:30:00+00:00',responders=[dict(execution=dict(session_id=str(i),verified=True,response_started=True,model='gpt-6-astra',reasoning_effort='medium'),current_frozen_policies_match=True,priority_present=True) for i in range(8)])
        return o,w,1792800001
    def reject(self,f):
        o,w,t=self.data();f(o,w)
        with self.assertRaises((ValueError,KeyError,TypeError)):require_complete(o,w,t)
    def test_complete_bound_proof(self):self.assertTrue(require_complete(*self.data()))
    def test_capacity_is_not_response(self):self.reject(lambda o,w:w['responders'].clear())
    def test_header_is_not_response(self):self.reject(lambda o,w:w['responders'][0]['execution'].update(response_started=False))
    def test_repeated_session_not_eight(self):self.reject(lambda o,w:w['responders'][1]['execution'].update(session_id='0'))
    def test_wrong_effort(self):self.reject(lambda o,w:w['responders'][0]['execution'].update(reasoning_effort='high'))
    def test_unknown_phase(self):self.reject(lambda o,w:o.update(guarded_phase_matches_current_pid=False))
    def test_drifted_pin(self):self.reject(lambda o,w:o.update(all77_current_pins_match=False))
    def test_stale_frozen_policy(self):self.reject(lambda o,w:w['responders'][0].update(current_frozen_policies_match=False))
    def test_missing_actual_priority(self):self.reject(lambda o,w:w['responders'][0].update(priority_present=False))
    def test_no_acceptance(self):self.reject(lambda o,w:o['accepted_reviews'].clear())
    def test_unverified_acceptance(self):self.reject(lambda o,w:o.update(accepted_review_verification_complete=False))
    def test_old_acceptance(self):self.reject(lambda o,w:o['accepted_reviews'][0].update(coordinator_pid=41583))
    def test_empty_row_proof(self):self.reject(lambda o,w:o['accepted_reviews'][0]['rows'].clear())
    def test_one_launch_not_this_story(self):self.reject(lambda o,w:o['exact_two_launch_history'].pop(0))
    def test_old_native_wave(self):self.reject(lambda o,w:w.update(new_pid=41583))
    def test_expired_proof(self):self.reject(lambda o,w:o.update(at_utc='2026-10-23T23:00:00+00:00'))
    def test_wave_before_run(self):self.reject(lambda o,w:w.update(at_utc='2026-10-23T20:00:00+00:00'))
if __name__=='__main__':unittest.main()
