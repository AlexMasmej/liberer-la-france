from pathlib import Path
import json,copy,sys,hashlib
P=Path(__file__).resolve().parent;L=P.parents[3];sys.path.insert(0,str(L));import reference_coherence as ref;from run_exhaustive import validate_answer
s=json.loads((P/'source.json').read_text());rows=json.loads((P/'answer.before-reference-checks.json').read_text());snapshot=json.loads((P/'reference-targets.json').read_text());old={x['number']:x for x in json.loads((P.parent/'edition001/answer.json').read_text())};cli={x['number']:x for x in json.loads((P/'accepted-CLI5-batch-rows.json').read_text())};targets=snapshot['targets']
for row in rows:
 base=cli[row['number']]if row['number']in cli else old[row['number']];checks=[];previous={x['target_key']:x for x in base.get('reference_checks',[])}
 for key in snapshot['requirements'][ref.key(row)]:
  t=targets[key];n=t['number'];c=copy.deepcopy(previous[key]);c['view_sha256']=t['view_sha256']
  if row['number']=='R243-45-1'and n=='L243-6-5':
   c['assessment']='La cible canonique capturée est désormais la proposition CLI effectivement inscrite, lue en entier avec source et note2020 : elle permet la transaction pendant/après recours amiable sans procès préalable, supprime approbation particulière et compte rendu annuel, mais garde les conditions I/II, quatre ans, antifraude, concessions, information de tutelle et interruptions favorables de la demande régulière. R243-45-1 de002 en supprime les circuits IV/V/VIII correspondants, conserve les trente jours du dossier complet auIII et la libre négociation. Les transactions anciennes conservent leur régime d’approbation ; la suppression n’est pas appliquée rétroactivement à leurs droits. Le maintien nécessaire de L243-6-4, désormais retained/null en contexte, ne supprime pas la portabilité des transactions. Aucune remise de dette automatique ni nouveau délai contentieux n’est créé.'
  elif row['number']=='R243-19'and n=='R243-15':
   c['assessment']='La vue canonique capturée reste la source entière I à V, sans proposition inscrite : calcul provisoire I avec25/50% et5points, DOETHIII avec25%+5points, régularisation et relèvement8% auIV. Le corps futur de CE PACK002, relu séparément, retire les majorations du seulI et son relèvement propre à8%, applique les exonérations dont conditions et montant sont établis et préserve entièrement DOETHIII et majorations ordinaires de paiement autonomes. Il coordonne aussi la DSN à néant du R133-14 déjà proposé sans fermer dernier mois d’emploi/régularisations/DOETH. R243-19 ne doit pas rétablir ces accessoires supprimés par la compétence de liquidation. La cible future ne constitue pas l’état canonique actuel : nouvelle lecture/certification après inscription indispensable.'
  elif row['number']=='R243-15':
   c['assessment']='Le nouveauI retire les majorations de base conformément au L242-12-1 CLI inscrit ; sonIV retire le seul relèvement propre à8% pour ceI. DOETHIII et retards ordinaires de paiement restent distincts. '+c['assessment']
  elif row['number']=='L243-6':
   c['assessment']='Le corps CLI courant est strictement conservé : remboursement AT-MP d’office seulement si décision et données suffisantes établissent montant/bénéficiaire ; charge d’initiative administrative déclarée mixed, quatre mois et remboursement unique, aucune réouverture de prescription. '+c['assessment']
  checks.append(c)
 row['reference_checks']=checks
# Make public explanations legible; no normative body changed by these replacements.
replacements={'duI':'du I','duIII':'du III','duIV':'du IV','duII':'du II','duV':'du V','auI':'au I','auIII':'au III','auIV':'au IV','leI ':'le I ','leIII':'le III','leIV':'le IV','leV ':'le V ','leII':'le II','ses25':'ses 25','ses30':'ses 30','les641':'les 641','et8%':'et 8 %','à8%':'à 8 %','à30':'à 30','sous20':'sous 20','sous30':'sous 30','25/50%':'25 %/50 %','25%':'25 %','50%':'50 %','8%':'8 %','5points':'5 points','1erjuillet':'1er juillet','1erjanvier':'1er janvier','31décembre':'31 décembre','auIII':'au III','III.':'III.','L242':'L242'}
def clean(v):
 if isinstance(v,str):
  for a,b in replacements.items():v=v.replace(a,b)
  return v
 if isinstance(v,list):return[clean(x)for x in v]
 if isinstance(v,dict):return{k:clean(x)for k,x in v.items()}
 return v
for row in rows:
 for n in ['reason','review_notes','benefit_review','substantive_impact','reference_checks']:row[n]=clean(row[n])
validate_answer(rows,s);ref.accept_checks(rows,s,snapshot)
(P/'answer.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
# Only actual future body changes, never labeled canonical views.
by={ref.key(x):x for x in rows};planned=[]
for k,t in targets.items():
 if k in by and by[k]['proposed_xml']is not None and by[k]['proposed_xml']!=t.get('proposed_xml'):
  future=copy.deepcopy(t);future.update(proposed_xml=by[k]['proposed_xml'],view_kind='proposal',view_sha256=ref.digest(by[k]['proposed_xml']));planned.append(dict(target_key=k,number=t['number'],before=copy.deepcopy(t),future_not_canonical=future,referrers=[next(x['number']for x in s if ref.key(x)==i)for i,v in snapshot['requirements'].items()if k in v]))
(P/'intrapack-planned-targets.json').write_text(json.dumps(dict(scope='Canonical BEFORE captured; explicit future state not certified before registration.',targets=planned),ensure_ascii=False,indent=2)+'\n');print('REFERENCE CHECKS',sum(len(x['reference_checks'])for x in rows),'FUTURE',[(x['number'],x['referrers'])for x in planned])
