import unittest, json, pathlib, re

R=pathlib.Path(__file__).resolve().parent
def read(p): return json.loads(p.read_text())
def paras(s): return re.findall(r'<p(?:\s[^>]*)?>.*?</p>',s,flags=re.S)

class Preservation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.S={x['number']:x for x in read(R/'edition001/source.json')}
        cls.A={x['number']:x for x in read(R/'edition001/answer.json')}
        cls.C=R/'complement-r243-59/edition001'
        cls.s59=read(cls.C/'source.json')[0]
        cls.a59=read(cls.C/'answer.json')[0]

    def test_exact_three_paragraph_substitutions_and_nothing_else(self):
        text=self.s59['source_xml']
        for d in read(self.C/'three-paragraph-diff.json'):
            self.assertEqual(text.count(d['before']),1)
            text=text.replace(d['before'],d['after'],1)
        self.assertEqual(text,self.a59['proposed_xml'])
        old,new=paras(self.s59['source_xml']),paras(text)
        self.assertEqual(len(old),len(new))
        self.assertEqual(sum(a!=b for a,b in zip(old,new)),3)

    def test_R59_subdivisions_and_all_unmodified_guarantee_paragraphs(self):
        old,new=paras(self.s59['source_xml']),paras(self.a59['proposed_xml'])
        for section in ['I.-','II.-','III.-','IV.-','V.-']:
            self.assertEqual([i for i,p in enumerate(old) if p.startswith('<p>'+section)],
                             [i for i,p in enumerate(new) if p.startswith('<p>'+section)])
        # Each full paragraph is preserved, including ordinal references and response rules.
        for needle in ['La période contradictoire prévue','Dans sa réponse,','Lorsque la personne contrôlée répond',
                       'La période contradictoire prend fin','Lorsqu’un solde créditeur','Lorsqu\'un solde créditeur',
                       'Les dispositions du chapitre II','II.-La personne contrôlée','Sauf autorisation']:
            matches=[p for p in old if needle in p]
            for p in matches: self.assertIn(p,new)
        for phrase in ['huitième alinéa du présent III','dixième alinéa du même III',
                       'deuxième et troisième alinéas du présent IV']:
            self.assertEqual(self.s59['source_xml'].count(phrase), self.a59['proposed_xml'].count(phrase))

    def test_R18_historic_rules_and_adjusted_internal_ordinal(self):
        old=paras(self.S['R243-18']['source_xml']);new=paras(self.A['R243-18']['proposed_xml'])
        self.assertEqual(old[0],new[2]);self.assertEqual(old[2],new[4])
        expected=old[1].replace('Le délai mentionné au premier alinéa','Le délai de six ans mentionné à l’alinéa précédent')
        self.assertEqual(expected,new[3])
        self.assertIn('seules majorations devenues définitives',new[1])
        self.assertIn('sans rouvrir les délais de prescription ou de recours',new[1])
        self.assertIn('ne permettent pas de prononcer une nouvelle majoration',new[0])

    def test_R19_autonomous_list_payment_and_historical_competence(self):
        old=paras(self.S['R243-19']['source_xml']);new=paras(self.A['R243-19']['proposed_xml'])
        self.assertEqual(len(old),4);self.assertEqual(len(new),6)
        for i in [0,1,3]:self.assertEqual(old[i],new[i])
        self.assertEqual(old[2].replace(', L. 243-7-6',''),new[2])
        self.assertIn('seules majorations',new[4]);self.assertIn('devenues définitives',new[4])
        self.assertIn('sans nouvelle notification destinée à rouvrir un délai expiré',new[4])

    def test_R17_retained_in_full_no_cosmetic_proposal(self):
        self.assertIsNone(self.A['R243-17']['proposed_xml'])
        self.assertEqual(self.A['R243-17']['status'],'retained_unchanged')
        self.assertEqual(self.S['R243-17']['source_xml'].count('L. 243-7-6'),3)
        self.assertIn('0,1 %',self.S['R243-17']['source_xml'])
        self.assertIn('plus de deux mois',self.S['R243-17']['source_xml'])

    def test_no_new_material_gain_claimed_by_regulatory_coordination(self):
        for a in list(self.A.values())+[self.a59]:
            impact=a['substantive_impact']
            self.assertIn(impact['classification'],['coordination_only','retained_necessary'])
        ids=[]
        for a in [self.A['R243-18'],self.A['R243-19'],self.a59]:
            for effect in a['substantive_impact']['effects']:ids.append(effect['measure_id'])
        self.assertEqual(set(ids),{'urssaf-majoration-non-conformite-suppression'})

if __name__=='__main__':unittest.main(verbosity=2)
