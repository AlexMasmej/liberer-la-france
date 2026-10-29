"""Contre-Avocat, issue #14 : commissions supplétives du CSE (coupes seules).

Lancer depuis legal-rewrite/ : python3 -m unittest test_contre_avocat_issue_14
Lit uniquement les lots JSON de batches/ (précédence automatic < thématiques < third-pass-corrections),
sans base ni réseau. Variable facultative CA14_ROOT : autre racine legal-rewrite/ à vérifier.
Seules les 14 entrées visées et L2315-45 sont verrouillées ; aucune empreinte globale de HEAD.
"""
import glob, html, json, os, re
from pathlib import Path
from unittest import TestCase

ROOT = Path(os.environ.get('CA14_ROOT') or Path(__file__).resolve().parent)
CT = 'LEGITEXT000006072050'
REPEAL = ['L2315-46', 'L2315-47', 'L2315-48', 'L2315-49', 'L2315-56']

REASON = {
 "L2315-46": "Abrogation : commission supplétive facultative, déjà possible par accord (L2315-45) ; le CSE conserve toutes ses attributions d'information et de consultation.",
 "L2315-47": "Abrogation : commission supplétive facultative, déjà possible par accord (L2315-45) ; le CSE conserve toutes ses attributions d'information et de consultation.",
 "L2315-48": "Abrogation : commission supplétive facultative, déjà possible par accord (L2315-45) ; le CSE conserve toutes ses attributions d'information et de consultation.",
 "L2315-49": "Abrogation : commission supplétive facultative, déjà possible par accord (L2315-45) ; le CSE conserve toutes ses attributions d'information et de consultation.",
 "L2315-56": "Abrogation : commission supplétive facultative, déjà possible par accord (L2315-45) ; le CSE conserve toutes ses attributions d'information et de consultation.",
 "L2312-63": "Coordination : suppression des seules mentions des commissions abrogées (L2315-46 à L2315-49, L2315-56) ; attributions du CSE inchangées.",
 "L2312-41": "Coordination : suppression des seules mentions des commissions abrogées (L2315-46 à L2315-49, L2315-56) ; attributions du CSE inchangées.",
 "L2312-64": "Coordination : suppression des seules mentions des commissions abrogées (L2315-46 à L2315-49, L2315-56) ; attributions du CSE inchangées.",
 "L2312-65": "Coordination : suppression des seules mentions des commissions abrogées (L2315-46 à L2315-49, L2315-56) ; attributions du CSE inchangées.",
 "L2312-66": "Coordination : suppression des seules mentions des commissions abrogées (L2315-46 à L2315-49, L2315-56) ; attributions du CSE inchangées.",
 "R2312-30": "Coordination : suppression des seules mentions des commissions abrogées (L2315-46 à L2315-49, L2315-56) ; attributions du CSE inchangées.",
 "R2315-28": "Coordination : suppression des seules mentions des commissions abrogées (L2315-46 à L2315-49, L2315-56) ; attributions du CSE inchangées.",
 "R2315-30": "Coordination : suppression des seules mentions des commissions abrogées (L2315-46 à L2315-49, L2315-56) ; attributions du CSE inchangées.",
 "R2315-31": "Coordination : suppression des seules mentions des commissions abrogées (L2315-46 à L2315-49, L2315-56) ; attributions du CSE inchangées."
}
EXACT = {
 "L2312-63": "Lorsque le comité social et économique a connaissance de faits de nature à affecter de manière préoccupante la situation économique de l'entreprise, il peut demander à l'employeur de lui fournir des explications. Cette demande est inscrite de droit à l'ordre du jour de la prochaine séance du comité. Si le comité n'a pu obtenir de réponse suffisante de l'employeur ou si celle-ci confirme le caractère préoccupant de la situation, il établit un rapport. Ce rapport, au titre du droit d'alerte économique, est transmis à l'employeur. Le comité social et économique peut également le transmettre au commissaire aux comptes ; cette transmission n'est pas obligatoire au titre du présent article. La suppression de la transmission obligatoire au commissaire aux comptes s'applique aux rapports établis à compter de l'entrée en vigueur de la loi qui l'institue. Les obligations antérieurement exigibles ainsi que les droits et recours qui s'y rapportent demeurent régis par les dispositions antérieures. Le droit de convoquer le commissaire aux comptes prévu à l'article L. 2312-64, les attributions et obligations légales propres de celui-ci ainsi que les règles de confidentialité restent applicables. Aucun autre envoi, dépôt ou document de remplacement n'est exigé au titre de cette suppression. Le comité reprend les travaux en cours de la commission économique supprimée sans réitération des actes régulièrement accomplis ni établissement d'un second rapport sur les mêmes faits. Les rapports déjà établis, les droits à rémunération et les engagements valablement pris demeurent préservés.",
 "L2312-41": "Lorsqu'une entreprise est partie à une opération de concentration, telle que définie à l'article L. 430-1 du code de commerce, l'employeur réunit le comité social et économique au plus tard dans un délai de trois jours à compter de la publication du communiqué relatif à la notification du projet de concentration, émanant soit de l'autorité administrative française en application de l'article L. 430-3 du même code, soit de la Commission européenne en application du règlement (CE) n° 139/2004 du Conseil du 20 janvier 2004 sur les concentrations. Au cours de cette réunion, le comité social et économique peut proposer le recours à un expert-comptable dans les conditions prévues aux articles L. 2315-92 et L. 2315-93. Dans ce cas, le comité tient une deuxième réunion afin d'entendre les résultats des travaux de l'expert. Les dispositions du premier alinéa sont réputées satisfaites lorsque le comité social et économique se réunit suite au dépôt d'une offre publique d'acquisition en application des dispositions du sous-paragraphe 5.",
 "L2312-64": "Le comité social et économique peut se faire assister, une fois par exercice comptable, de l'expert-comptable prévu à l'article L. 2315-92, convoquer le commissaire aux comptes et s'adjoindre avec voix consultative deux salariés de l'entreprise choisis pour leur compétence et en dehors du comité social et économique. Ces salariés disposent de cinq heures chacun pour assister le comité en vue de l'établissement du rapport prévu à l'article L. 2312-63. Ce temps est rémunéré comme temps de travail.",
 "L2312-65": "Le rapport du comité social et économique conclut en émettant un avis sur l'opportunité de saisir de ses conclusions l'organe chargé de l'administration ou de la surveillance dans les sociétés ou personnes morales qui en sont dotées, ou d'en informer les associés dans les autres formes de sociétés ou les membres dans les groupements d'intérêt économique. Au vu de ce rapport, le comité social et économique peut décider, à la majorité des membres présents de procéder à cette saisine ou de faire procéder à cette information. Dans ce cas, l'avis de l'expert-comptable est joint à la saisine ou à l'information.",
 "L2312-66": "Dans les sociétés à conseil d'administration ou à conseil de surveillance, la demande d'explication sur le caractère préoccupant de la situation économique de l'entreprise est inscrite à l'ordre du jour de la prochaine séance du conseil d'administration ou du conseil de surveillance. La réponse de l'employeur est motivée. Dans les autres personnes morales, ces dispositions s'appliquent à l'organe chargé de l'administration ou de la surveillance, lorsqu'elles en sont dotées. Dans les autres formes de sociétés ou dans les groupements d'intérêt économique, lorsque le comité social et économique a décidé d'informer les associés ou les membres de la situation de l'entreprise, le gérant ou les administrateurs leur communiquent le rapport du comité. Les dispositions du présent article s'appliquent aux séances tenues à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris lorsque la saisine est antérieure. Les délibérations déjà intervenues et les droits et recours relatifs à celles-ci demeurent régis par les dispositions qui leur étaient applicables.",
 "R2312-30": "Dans les sociétés autres que celles qui ont un conseil d'administration ou de surveillance ou dans les groupements d'intérêt économique, les administrateurs communiquent aux associés et aux membres du groupement le rapport du comité social et économique dans les huit jours de la délibération du comité social et économique demandant cette communication.",
 "R2315-28": "En l'absence d'accord prévu à l'article L. 2315-45, les membres des commissions peuvent être choisis parmi des salariés de l'entreprise n'appartenant pas au comité social et économique. Sans préjudice des dispositions de l'article L. 2315-39, les commissions du comité sont présidées par un de ses membres.",
 "R2315-30": "En l'absence d'accord prévu à l'article L. 2315-45, le comité social et économique est consulté sur les problèmes généraux relatifs à la mise en œuvre : 1° Des dispositifs de formation professionnelle continue, prévus aux chapitres Ier à III du titre II du livre III de la sixième partie ; 2° De la validation des acquis de l'expérience, prévue au titre II du livre IV de la sixième partie.",
 "R2315-31": "En l'absence d'accord prévu à l'article L. 2315-45, le comité social et économique est informé des possibilités de congé qui ont été accordées aux salariés, des conditions dans lesquelles ces congés ont été accordés ainsi que des résultats obtenus."
}
REPEAL_TEXTS = {'Le présent article est abrogé.', 'Abrogé.'}


def rank(d):
    return (0 if d.startswith('automatic-') else 2 if d == 'third-pass-corrections' else 1, d)


def effective(root=ROOT):
    entries = {}
    for p in sorted(glob.glob(str(root / 'batches' / '*')), key=lambda p: rank(os.path.basename(p))):
        for f in sorted(glob.glob(os.path.join(p, '*.json'))):
            try:
                d = json.load(open(f, encoding='utf-8'))
            except Exception:
                continue
            if isinstance(d, dict):
                d = d.get('entries', [])
            for e in d if isinstance(d, list) else []:
                if isinstance(e, dict) and e.get('code_id') == CT and e.get('number'):
                    entries[e['number']] = e
    return entries


def text(e):
    s = html.unescape(re.sub(r'<[^>]+>', ' ', (e or {}).get('proposed_xml') or '')).replace('\u2019', "'")
    return re.sub(r'[ \t\r\n]+', ' ', s).strip()


BAD = re.compile(r"L\. ?2315-(4[6-9]|56)\b|commission (économique|de la formation|de l'égalité professionnelle)")


class ContreAvocatIssue14(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.E = effective()

    def test_repeals(self):
        for n in REPEAL:
            with self.subTest(n):
                e = self.E.get(n) or {}
                self.assertEqual(e.get('status'), 'rewrite_draft')
                self.assertEqual(e.get('change_type'), 'full_repeal')
                self.assertIn(text(e), REPEAL_TEXTS)
                self.assertEqual(e.get('reason'), REASON[n])

    def test_cuts_exact(self):
        for n, want in EXACT.items():
            with self.subTest(n):
                e = self.E.get(n) or {}
                self.assertEqual(e.get('status'), 'rewrite_draft')
                self.assertEqual(e.get('change_type'), 'normative_reduction')
                self.assertEqual(text(e), want)
                self.assertEqual(e.get('reason'), REASON[n])

    def test_no_dangling_reference(self):
        hits = [n for n, e in self.E.items() if e.get('status') == 'rewrite_draft' and e.get('change_type') != 'full_repeal'
                and BAD.search(text(e).replace('de la commission économique supprimée', ''))]
        self.assertEqual(hits, [])

    def test_l2315_45_kept(self):
        e = self.E.get('L2315-45')
        self.assertIsNotNone(e)
        self.assertNotEqual(e.get('change_type'), 'full_repeal')
        if e.get('status') != 'retained_unchanged':
            self.assertIn('commission', text(e))
