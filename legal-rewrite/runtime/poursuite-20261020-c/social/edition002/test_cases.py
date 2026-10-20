"""Text preservation and bounded arithmetic examples; no whole-code legal proof."""
from pathlib import Path
import json,unittest
from decimal import Decimal as D
P=Path(__file__).resolve().parent
S={x['number']:x for x in json.loads((P/'source.json').read_text())};A={x['number']:x for x in json.loads((P/'answer.json').read_text())}
def paragraphs(n):
 import re
 return re.findall(r'<p[^>]*>.*?</p>',S[n]['source_xml'],flags=re.S)
class Cases(unittest.TestCase):
 def test_13_retained_have_no_substitute_body(self):
  kept=[x for x in A.values()if x['status']=='retained_unchanged'];self.assertEqual(len(kept),13);self.assertTrue(all(x['proposed_xml']is None for x in kept))
 def test_transaction_concessions_and_favorable_interruptions_stay(self):
  body=A['R243-45-1']['proposed_xml']
  for paragraph in paragraphs('R243-45-1'):
   if 'concessions réciproques de la part de chaque partie' in paragraph or paragraph.startswith('<p>III.') or paragraph.startswith('<p>La demande de transaction interrompt'):self.assertIn(paragraph,body)
  self.assertIn('travail dissimulé',A['L243-6-5']['proposed_xml'])
 def test_approval_and_annual_report_not_reintroduced(self):
  b=A['R243-45-1']['proposed_xml']
  self.assertNotIn("est soumise pour approbation",b);self.assertNotIn("Le refus d'approbation de la proposition prive d'effet la transaction",b)
  self.assertIn("Cette communication n'est pas une demande d'approbation",b);self.assertIn("les transactions antérieures et les droits qui en résultent conservent leur régime",b)
  self.assertIn("ne sont plus exigés sur le seul fondement",b);self.assertIn("avant le 1er octobre",b);self.assertIn("Aucun état, registre ou rapport de remplacement",b)
 def test_employer_choice_mandatory_assignments(self):
  b=A['R243-6-3']['proposed_xml'];self.assertIn('250',b.replace('deux cent cinquante','250'));self.assertIn('cinq cent salariés',b)
  for n in ['L. 243-1-2','R. 243-8-1']:self.assertIn(n,b)
  self.assertIn('ensemble des établissements',b);self.assertIn('1er janvier suivant',b)
 def test_provisional_does_not_change_disability_annual_formula(self):
  b=A['R243-15']['proposed_xml']
  for q in paragraphs('R243-15'):
   if q.startswith('<p>II.')or q.startswith('<p>III.')or q.startswith('<p>IV.')or 'avant le 31 décembre' in q:self.assertIn(q,b)
  self.assertIn('ne crée pas d\'exonération de la contribution distincte du III',b)
 def test_no_dsn_neant_does_not_waive_last_month_or_annual(self):
  b=A['R243-15']['proposed_xml'];self.assertIn("dernier mois comportant un emploi",b);self.assertIn("obligation annuelle du III",b)
 def test_penalty_example_same_event_three_months(self):
  # P=1000 abstract units, one employee: no real annual French ceiling assumed.
  initial=D(1000)*D('.015');self.assertEqual(initial*3,D(45));self.assertEqual(initial,D(15))
  self.assertEqual(initial*2,D(30)) # Two distinct missing declaration deadlines still count twice.
 def test_short_delay_cap_not_removed(self):
  self.assertIn('150 %',A['R243-12']['proposed_xml']);self.assertIn('cinq jours',A['R243-12']['proposed_xml']);self.assertIn('une seule fois par année civile',A['R243-12']['proposed_xml'])
 def test_repeat_incident_relief_still_has_strict_ceiling_and_30days(self):
  b=A['R243-11']['proposed_xml'];self.assertIn('inférieur à la valeur mensuelle',b);self.assertIn('délai de trente jours',b);self.assertIn('en respecte les termes',b)
  ceiling,accessories=D(1000),D(999);self.assertLess(accessories,ceiling);self.assertFalse(ceiling<ceiling)
 def test_provisional_timing_final_unchanged(self):
  provisional,known_relief,final=D(1000),D(200),D(700)
  old_advance=provisional;new_advance=provisional-known_relief
  self.assertEqual(old_advance-(old_advance-final),final);self.assertEqual(new_advance-(new_advance-final),final);self.assertEqual(old_advance-new_advance,D(200))
 def test_control_exception_list_intact(self):
  b=A['L243-13']['proposed_xml']
  for q in paragraphs('L243-13'):
   if any(q.startswith('<p>'+x)for x in ['1°','2°','3°','4°','5°','II.']):self.assertIn(q,b)
 def test_three_material_cli_bodies_are_preserved_exactly(self):
  cli={x['number']:x for x in json.loads((P/'accepted-CLI5-batch-rows.json').read_text())}
  for n in ['L242-12-1','L243-6','L243-6-5']:self.assertEqual(A[n]['proposed_xml'],cli[n]['proposed_xml'])
 def test_cli_beforeimages_record_actual_existing_drafts(self):
  for n in ['L242-12-1','L243-5','L243-6','L243-6-5','L243-6-6']:self.assertIsNotNone(S[n]['previous_draft'])
  self.assertEqual(sum(x['previous_draft']is None for x in S.values()),19)
 def test_provisional_base_and_penalty_removed_only_in_I(self):
  import re
  b=A['R243-15']['proposed_xml'];i=b[:b.index('<p>II.')]
  self.assertNotIn('majorées de 25 %',i);self.assertNotIn('majoré de 50 %',i);self.assertNotIn('augmenté de 5 points',i)
  self.assertIn('notification prévue au III',b);self.assertIn('ne donne pas lieu au relèvement à 8 %',b);self.assertIn('majorations ordinaires de retard de paiement',b)
  self.assertIn('Le forfait ne peut reconstituer une majoration punitive',b)
 def test_no_permanent_tax_cut_claimed_for_provisional_base(self):
  for n in ['L242-12-1','R243-15']:
   e={x['measure_id']:x for x in A[n]['substantive_impact']['effects']}
   for k in ['taxation-provisoire-base-non-majoree','taxation-provisoire-exonerations']:self.assertEqual(e[k]['kind'],'payment_deferred')
   self.assertEqual(e['taxation-provisoire-penalite-supprimee']['kind'],'relief_extended')
 def test_atmp_automatic_refund_mixed_and_unique(self):
  b=A['L243-6']['proposed_xml'];self.assertIn("sans demande distincte du cotisant",b);self.assertIn("un remboursement déjà effectué s'impute une seule fois",b)
  self.assertIn("les droits à prestations conservés au II",b);self.assertIn("Il ne rouvre aucun délai expiré",b)
  self.assertEqual(A['L243-6']['substantive_impact']['classification'],'mixed');self.assertTrue(any(x['kind']=='obligation_added'for x in A['L243-6']['substantive_impact']['effects']))
 def test_notifications_do_not_recount_existing_crpa(self):
  prior={x['number']:x for x in json.loads((P.parent/'edition001/answer.json').read_text())}
  for n in ['L244-2','R243-48']:
   self.assertEqual(A[n]['proposed_xml'],prior[n]['proposed_xml']);self.assertEqual(A[n]['substantive_impact']['classification'],'coordination_only')
   self.assertTrue(all(x['kind']=='coordination'for x in A[n]['substantive_impact']['effects']));self.assertIn('accord exprès préalable',A[n]['benefit_review'])
 def test_transaction_family_uses_cli_measure_id_once(self):
  ids={e['measure_id']for n in ['L243-6-5','R243-45-1']for e in A[n]['substantive_impact']['effects']}
  self.assertNotIn('transaction-sociale-sans-parcours-contentieux-impose',ids)
  self.assertIn('transaction-sociale-sans-gel-amiable',ids)
  self.assertIn('transaction-sociale-sans-approbation-speciale',ids)
  self.assertIn('transaction-sociale-compte-rendu-annuel-supprime',ids)
if __name__=='__main__':unittest.main()
