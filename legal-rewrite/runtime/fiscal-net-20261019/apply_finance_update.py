"""Apply the financing clarification only after current legal jobs have drained."""
from pathlib import Path
import fcntl
import json
import time

ROOT = Path(__file__).resolve().parent
LEGAL = ROOT.parents[1]


def atomic(path, data):
    tmp = path.with_name(path.name+'.finance-tmp')
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
    tmp.replace(path)


with (LEGAL/'runtime/exhaustive/coordinator.lock').open('a') as lock:
    print('Waiting for the previous coherent publication to finish.', flush=True)
    fcntl.flock(lock, fcntl.LOCK_EX)
    print('No legal job is running; applying financing clarification.', flush=True)
    names = ['policy-coordinations.json', 'site-summaries.json', 'run_exhaustive.py']
    for name in names:
        backup = ROOT/(name+'.before')
        if not backup.exists():
            backup.write_bytes((LEGAL/name).read_bytes())
    policy = json.loads((LEGAL/'policy-coordinations.json').read_text())
    policy['chiffrage_net_is_2026_10_19'] = json.loads((ROOT/'coordination.proposed.json').read_text())
    old = 'Chiffrer séparément le décalage et la baisse des recettes ; le réinvestissement espéré n\'est pas une compensation budgétaire démontrée.'
    new = 'Évaluer l’effet net consolidé selon chiffrage_net_is_2026_10_19 : distinguer report et baisse durable d’IS, puis intégrer autofinancement, dette, résilience, innovation, emploi, recettes induites et aides effectivement évitées dans des scénarios explicites.'
    assert sum(old in text for text in policy['is_distribution']) == 1
    policy['is_distribution'] = [text.replace(old, new) for text in policy['is_distribution']]
    items = json.loads((LEGAL/'site-summaries.json').read_text())
    item = next(item for item in items if item['slug'] == 'entreprise')
    item['finance_title'] = 'Mesurer l’effet net sur les finances publiques.'
    item['finance'] = 'Chiffrer le bilan complet : IS payé plus tard, investissements et embauches supplémentaires, recettes d’IR, de TVA et de cotisations, aides d’innovation et de crise effectivement évitées. Une entreprise mieux financée peut croître avec moins de dette et mieux absorber les chocs. Tester aussi une réduction des dispositifs que l’autofinancement peut remplacer : CIR, niches et interventions de Bpifrance, avec leur coût public net et les effets de leur retrait. Publier le besoin de trésorerie initial, puis les soldes à cinq et dix ans selon plusieurs scénarios. Les hypothèses de croissance et d’économies restent à mesurer.'
    source = (LEGAL/'run_exhaustive.py').read_text()
    anchor = 'Lis cvae_removal en entier :'
    assert source.count(anchor) == 1
    source = source.replace(anchor, 'Lis chiffrage_net_is_2026_10_19 pour les notes de chiffrage : intégrer les effets nets d’autofinancement, dette, innovation, emploi, recettes et aides publiques, avec hypothèses explicites et sans inventer un rendement. Ce cadre ne supprime aucun crédit, avantage ni dispositif juridique supplémentaire.\n'+anchor)
    atomic(LEGAL/'policy-coordinations.json', policy)
    atomic(LEGAL/'site-summaries.json', items)
    (LEGAL/'run_exhaustive.py').write_text(source)
    atomic(ROOT/'applied.json', {'updated_at_unix': int(time.time()), 'policy_key': 'chiffrage_net_is_2026_10_19', 'legal_bodies_changed': False, 'previous_coordinator_drained': True})
    print('Applied net fiscal evaluation framework; legal bodies and benefits unchanged.', flush=True)
