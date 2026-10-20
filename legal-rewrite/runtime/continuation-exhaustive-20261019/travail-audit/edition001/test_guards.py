"""Offline race/false-certificate cases for the audit's read-only guard."""
from unittest import TestCase,main
import copy
from verify import compare_record,sha

class SnapshotRaces(TestCase):
    def setUp(self):
        self.row={'source_xml':'<p>Texte officiel complet.</p>','source_sha256':'a'*64,
                  'source_notes_xml':'<p>Entrée en vigueur réservée.</p>',
                  'previous_draft':{'source_sha256':'a'*64,'status':'rewrite_draft',
                      'proposed_xml':'<p>Proposition antérieure entière.</p>',
                      'reason':'Motif antérieur.','review_notes':'Réserve antérieure.'}}
        self.row['previous_draft']['proposed_sha256']=sha(self.row['previous_draft']['proposed_xml'])
        self.source=self.row['source_xml'],self.row['source_sha256']
        prior=self.row['previous_draft']
        self.draft=tuple(prior[k] for k in ['source_sha256','status','proposed_xml','reason','review_notes'])

    def test_unchanged_snapshot_passes_without_mutation(self):
        original=copy.deepcopy(self.row)
        self.assertEqual(compare_record(self.row,self.source,self.row['source_notes_xml'],self.draft),[])
        self.assertEqual(self.row,original)

    def test_new_author_proposal_cannot_be_overwritten(self):
        changed=list(self.draft);changed[2]='<p>Nouvelle décision d’un auteur concurrent.</p>'
        self.assertIn('prior_draft_changed',compare_record(self.row,self.source,self.row['source_notes_xml'],tuple(changed)))

    def test_dependency_reason_change_also_invalidates_snapshot(self):
        changed=list(self.draft);changed[3]='Nouveau sens ou champ de la réforme.'
        self.assertIn('prior_draft_changed',compare_record(self.row,self.source,self.row['source_notes_xml'],tuple(changed)))

    def test_official_note_change_is_detected_when_body_stays_identical(self):
        errors=compare_record(self.row,self.source,'<p>Nouvelle condition transitoire.</p>',self.draft)
        self.assertIn('official_application_notes_changed',errors)

    def test_new_draft_of_previously_undrafted_dependency_is_detected(self):
        self.row['previous_draft']=None
        self.assertIn('prior_draft_changed',compare_record(self.row,self.source,self.row['source_notes_xml'],self.draft))

    def test_changed_official_hash_and_corrupt_local_guard_fail(self):
        self.row['previous_draft']['proposed_sha256']='b'*64
        errors=compare_record(self.row,(self.source[0],'c'*64),self.row['source_notes_xml'],self.draft)
        self.assertIn('canonical_source_changed',errors)
        self.assertIn('corrupt_before_image_guard',errors)

if __name__=='__main__':main()
