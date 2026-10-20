"""Activate reviewed policy and concise summaries after guarded registration."""
from pathlib import Path
from datetime import datetime, timezone
import fcntl, hashlib, json, sys

P=Path(__file__).resolve().parent
B=P.parents[1]
sys.path.insert(0,str(B))
from run_exhaustive import atomic
from register_batches import writer_lock

def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

registration=load(P/'integration/edition001/registration.json')
assert registration['registered_articles']==96
assert (P/'social-independent-review/edition002/review-002.json').exists()
assert (P/'tsa-independent-review/edition002/review.json').exists()
assert (P/'dpae-independent-review/edition001/audit.json').exists()
assert (P/'urbanisme/edition001/root-independent-review.json').exists()
assert (P/'crpa-classification-independent-review/edition001/review.json').exists()
amendment=load(P/'tsa/edition002/policy-amendment.proposed.json')
with (B/'runtime/publication.lock').open('a') as publication_lock:
 fcntl.flock(publication_lock,fcntl.LOCK_EX)
 with writer_lock():
  assert sha(B/'policy-coordinations.json')==amendment['expected_policy_sha256']
  assert sha(B/'site-summaries.json')==amendment['expected_site_summaries_sha256']
  policy=load(B/'policy-coordinations.json');sites=load(B/'site-summaries.json')
  atomic(P/'policy-before.json',policy);atomic(P/'site-summaries-before.json',sites)
  for op in amendment['operations']:
   if op['op']=='add_section':
    assert op['key'] not in policy
    policy[op['key']]=op['value']
   elif op['op']=='append':policy[op['key']].append(op['value'])
   else:raise ValueError(op)
  policy['substantive_outcomes_2026_10_19'].extend([
   'Droit existant et nouveau gain : CRPA L113-12 et L114-8 interdisent déjà certaines demandes d’informations détenues ou légalement échangeables, y compris auprès des organismes sociaux selon L100-3. Une simple reprise de ce droit est coordination_only, sans nouvelle obligation supprimée. Identifier précisément toute dispense qui va au-delà, sans ouvrir un nouvel accès aux données.',
   'Les copies et supports matériels expressément supprimés au premier dépôt sont distincts de la simple réutilisation de données déjà détenues. Dédupliquer par dispositif, garder le contenu utile et les exonérations favorables. Le dépôt papier unique peut transférer un coût aux services : classement mixed, coût net inconnu ; aucun gain nouveau pour les dépôts électroniques déjà dispensés.',
   'La suppression d’une conservation obligatoire de doubles et accusés DPAE est une obligation privée retirée, distincte du CRPA. Ne pas compter une seconde fusion du dépôt sanitaire déjà coordonné ; préserver les informations et preuves réellement disponibles, les contrôles, l’affiliation et le suivi de santé.'
  ])
  policy['autorisations_urbanisme'].append(
   'Poursuite20261020 : un seul exemplaire pour les dépôts papier PC/PA/PD/DP, sans suppléments de circulation aux frais du demandeur ; reproduction et transmission par les services, destinataires et délais maintenus. R423-2/13 et A431-9/A441-9 constituent une seule mesure urbanisme-depot-papier-exemplaire-unique, mixte à coût public inconnu. R474-1 dispense déjà les dépôts électroniques, ne pas les recompter. Retirer les dates de naissance et inventaires génériques d’autres demandes ; conserver les signalements sectoriels nécessaires. Fusionner les supports graphiques hors secteurs protégés dans les cas prévus, admettre notice et plans communs, retirer le croquis distinct R441-10. Conserver les neuf exemptions R442-1, les pièces ouvrant des dérogations favorables et l’accord exprès du lotisseur, prouvable aussi par acte signé. R433-1 : retirer seulement le terme obligatoire du a hors zone ; b protégé, caractère précaire et garanties L433-2à7 maintenus.'
  )
  policy['reporting_social'].append(
   'Poursuite20261020 : R243-8 remplace l’autorisation préalable de versement à un organisme unique par une option, avec conditions d’accès conservées et affectations obligatoires L243-1-2/R243-8-1 réservées. R131-9 ouvre le report après premier paiement uniquement pour le solde restant dû, sans remboursement artificiel : paiement différé, pas baisse de cotisations. L613-2 et coordinations de réemploi reprennent le droit existant, sans nouveau gain CRPA compté.'
  )
  company=next(s for s in sites if s['slug']=='entreprise')
  company['ideas'].insert(2,[
   'Supprimer la taxe sur les salaires',
   'Supprimer cette taxe employeur, distincte des cotisations sociales, pour les rémunérations versées après l’entrée en vigueur. Elle concerne surtout les employeurs peu ou pas soumis à la TVA. Retirer les déclarations et acomptes exclusivement liés à cette taxe. Garder les exonérations et allègements pour les rémunérations anciennes.'
  ])
  company['finance']+=' Pour la taxe sur les salaires, distinguer la perte brute de recettes sociales et le solde public consolidé : certains employeurs publics ou financés publiquement dépenseraient moins. Cet effet reste à chiffrer, avec les besoins de financement des branches sociales ; aucun autofinancement n’est présumé.'
  work=next(s for s in sites if s['slug']=='embauche')
  work['ideas'].append([
   'Retirer des archives imposées à chaque embauche',
   'Supprimer la conservation obligatoire des doubles et accusés de réception de la déclaration préalable, sans empêcher de garder une preuve utile. Lorsque le papier reste autorisé, permettre la remise contre reçu si l’organisme la propose. Conserver l’affiliation sociale et le suivi de santé.'
  ])
  housing=next(s for s in sites if s['slug']=='logement')
  housing['ideas'][0][0]='Un dossier et moins de pièces séparées'
  housing['ideas'][0][1]+=' Pour les dépôts papier, fournir un seul exemplaire, sans jeux supplémentaires pour les services. Selon le projet, réunir notice et plans ou les représentations graphiques sur un support commun, en conservant les informations nécessaires et les pièces des secteurs protégés.'
  housing['finance']+=' Le dossier papier unique réduit les copies à fournir mais peut transférer des frais de reproduction et de transmission aux services. Ce coût public reste à mesurer ; les dossiers électroniques bénéficient déjà d’une dispense de copies.'
  atomic(B/'policy-coordinations.json',policy)
  atomic(B/'site-summaries.json',sites)
  atomic(P/'activation.json',dict(activated_at=datetime.now(timezone.utc).isoformat(),
   reviewed_articles_registered=96,policy_sha256=sha(B/'policy-coordinations.json'),
   site_summaries_sha256=sha(B/'site-summaries.json'),
   national_net_cost=None,exhaustive_rewriting_complete=False))
print('Reviewed phase B policy and five concise site summaries activated.')
