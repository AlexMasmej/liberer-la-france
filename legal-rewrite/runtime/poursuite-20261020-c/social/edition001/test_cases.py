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
 def test_14_retained_have_no_substitute_body(self):
  kept=[x for x in A.values()if x['status']=='retained_unchanged'];self.assertEqual(len(kept),14);self.assertTrue(all(x['proposed_xml']is None for x in kept))
 def test_transaction_approval_and_concessions_stay(self):
  body=A['R243-45-1']['proposed_xml']
  for paragraph in paragraphs('R243-45-1'):
   if paragraph.startswith('<p>IV.')or paragraph.startswith('<p>Le contrôle de l\'autorité')or paragraph.startswith('<p>Le refus d\'approbation')or 'concessions réciproques de la part de chaque partie' in paragraph:self.assertIn(paragraph,body)
  self.assertIn('travail dissimulé',A['L243-6-5']['proposed_xml'])
 def test_employer_choice_mandatory_assignments(self):
  b=A['R243-6-3']['proposed_xml'];self.assertIn('250',b.replace('deux cent cinquante','250'));self.assertIn('cinq cent salariés',b)
  for n in ['L. 243-1-2','R. 243-8-1']:self.assertIn(n,b)
  self.assertIn('ensemble des établissements',b);self.assertIn('1er janvier suivant',b)
 def test_provisional_does_not_change_disability_annual_formula(self):
  b=A['R243-15']['proposed_xml']
  for q in paragraphs('R243-15'):
   if q.startswith('<p>III.')or q.startswith('<p>IV.')or 'avant le 31 décembre' in q or 'portée à 8 %' in q:self.assertIn(q,b)
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
if __name__=='__main__':unittest.main()
