#!/usr/bin/env python3
"""travail-cse-commissions r4 : python3 t_cse.py <racine du dépôt corrigé>. Lit seulement les lots JSON de cet arbre ; aucune mutation en mémoire."""
import sys, os, json, glob, re, html, hashlib
ROOT = sys.argv[1]; CT = 'LEGITEXT000006072050'
def rank(d): return (0 if d.startswith('automatic-') else 2 if d == 'third-pass-corrections' else 1, d)
E = {}
for p in sorted(glob.glob(os.path.join(ROOT, 'legal-rewrite', 'batches', '*')), key=lambda p: rank(os.path.basename(p))):
    for f in sorted(glob.glob(os.path.join(p, '*.json'))):
        try: d = json.load(open(f))
        except Exception: continue
        if isinstance(d, dict): d = d.get('entries', [])
        for e in d if isinstance(d, list) else []:
            if isinstance(e, dict) and e.get('code_id') == CT and e.get('number'): E[e['number']] = e
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
REPEAL_TEXTS = {'', 'Le présent article est abrogé.', 'Abrogé.'}  # forme vide ou formule d'abrogation usuelle du dépôt, rien d'autre
TARGETS = set(REPEAL) | set(EXACT)
def H(e): return hashlib.sha256(json.dumps(e, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
def perimeter():
    lines = sorted(f'{n}\t{H(e)}' for n, e in E.items() if n not in TARGETS)
    return len(lines), hashlib.sha256('\n'.join(lines).encode()).hexdigest()
if len(sys.argv) > 2 and sys.argv[2] == '--print-perimeter': print(*perimeter()); sys.exit(0)
PERIM = (11578, "34ea35518c2bc77fa510230b6dabe1259adb02af6855a865879eb8bb4f6d6af9")
L2315_45 = "23f3950710282cc7b4ff2a0b676a0034211a0dffe847dca2ddd781630f3ffb86"
def T(e):  # balises retirées, entités décodées ; seuls espaces ASCII/sauts de ligne fusionnés (une espace insécable reste un écart)
    s = html.unescape(re.sub(r'<[^>]+>', ' ', (e or {}).get('proposed_xml') or '')).replace('\u2019', "'")
    return re.sub(r'[ \t\r\n]+', ' ', s).strip()
res = []
def ck(lbl, ok): res.append(bool(ok)); print(('PASS ' if ok else 'FAIL ') + lbl)
# Seuls status, change_type, texte proposé et reason sont verrouillés sur les 14 cibles ; les autres métadonnées
# (source_sha256, review_notes, substantive_impact, certificat, policy_review_id, prior_proposal_sha256…) sont libres.
for n in REPEAL:
    e = E.get(n) or {}
    ck(f'C1 {n} abrogé : status rewrite_draft, change_type full_repeal, texte vide ou formule d\'abrogation', e.get('status') == 'rewrite_draft' and e.get('change_type') == 'full_repeal' and T(e) in REPEAL_TEXTS)
    ck(f'C1r {n} : reason exacte', e.get('reason') == REASON[n])
for n, want in EXACT.items():
    e = E.get(n) or {}
    ck(f'C2 {n} : rewrite_draft, normative_reduction, texte exact', e.get('status') == 'rewrite_draft' and e.get('change_type') == 'normative_reduction' and T(e) == want)
    ck(f'C2r {n} : reason exacte', e.get('reason') == REASON[n])
bad = re.compile(r"L\. ?2315-(4[6-9]|56)\b|commission (économique|de la formation|de l'égalité professionnelle)")
hits = [n for n, e in E.items() if e.get('status') == 'rewrite_draft' and e.get('change_type') != 'full_repeal' and bad.search(T(e).replace('de la commission économique supprimée', ''))]
ck(f'C3 aucun renvoi pendant {hits}', not hits)
e45 = E.get('L2315-45')
ck('C4 L2315-45 verrouillé (entrée identique à HEAD)', bool(e45) and H(e45) == L2315_45)
n, h = perimeter()
ck(f'C5 périmètre : les {n} autres entrées du Code du travail identiques à HEAD (attendu {PERIM[0]})', (n, h) == tuple(PERIM))
print(f'== {sum(res)}/{len(res)} PASS'); sys.exit(0 if all(res) else 1)
