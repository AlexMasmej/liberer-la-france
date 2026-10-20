from pathlib import Path
import json,hashlib,shutil,sys
P=Path(__file__).resolve().parent;A=P.parent/'edition001';L=P.parents[3];sys.path.insert(0,str(L));from substantive_impact import certificate
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def put(n,v):(P/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
for n in ['source.json','context.json','capture.json','policy-coordinations.json','site-summaries.json','crpa-primary-bodies.json','crpa-primary-search.json','crpa-definitions-primary-search.json','selection.json','verify.py','drafting-decisions.json']:
 shutil.copyfile(A/n,P/n)
rows=json.loads((A/'answer.json').read_text());sources=json.loads((P/'source.json').read_text());by={s['source_id']:s for s in sources}
for r in rows:
 if r['number']=='L613-2':
  old="qui ne leur ont pas déjà été transmis ou auxquels ils n'ont pas légalement accès."
  new="qui ne leur ont pas déjà été transmis et qu'ils ne peuvent pas obtenir directement et légalement auprès d'une autre administration."
  assert r['proposed_xml'].count(old)==1;r['proposed_xml']=r['proposed_xml'].replace(old,new)
  r['review_notes']+=" Correction après contrelecture de l’édition001 : les deux conditions d’une demande subsidiaire sont cumulatives, absence de transmission et impossibilité d’obtention directe légale auprès d’une autre administration. Une donnée fiscale légalement obtenable n’est pas redemandée au seul motif qu’elle n’est pas encore transmise. Les données inexactes restent à corriger selon la phrase inchangée. Aucun élargissement des finalités d’accès, secret ou contrôle."
  r['substantive_impact']['effects'][0]['after']="Seuls les éléments manquants non déjà transmis et non directement obtenables légalement auprès d’une autre administration sont réclamés ; les données disponibles doivent rester exactes, à jour et légalement réutilisables. Cette coordination explicite le droit existant du CRPA, sans gain neuf revendiqué."
  r['substantive_impact']['assessment']+=" Les conditions de demande subsidiaire sont cumulatives ; une donnée légalement obtenable auprès de l’administration fiscale ne devient pas redemandable du seul fait qu’elle n’est pas encore transmise."
 elif r['number']=='R243-8':
  old="Le dépôt de cette demande vaut option ; aucune autorisation préalable n'est requise."
  new=old+" Cette faculté et le choix de l'organisme unique s'exercent sans déroger aux affectations obligatoires prévues à l'article L. 243-1-2 ou prises en application de l'article R. 243-8-1, pour les personnels qu'elles concernent."
  assert r['proposed_xml'].count(old)==1;r['proposed_xml']=r['proposed_xml'].replace(old,new)
  r['review_notes']+=" Correction après contrelecture de l’édition001 : la demande valant option ne permet pas de contourner l’organisme obligatoirement désigné pour employeurs étrangers ou personnels particuliers. L243-1-2 et R243-8-1, sources et notes entières relues, gardent leur champ propre ; les autres personnels demeurent dans la faculté générale si admissibles."
  r['benefit_review']+=" Les affectations spéciales obligatoires de L243-1-2 et R243-8-1 demeurent applicables aux personnels concernés ; les facilités particulières des employeurs étrangers sont conservées, sans choix d’un organisme contraire à ces affectations."
  r['substantive_impact']['effects'][0]['after']="La demande existante vaut option sans autorisation ; admissibilité, sommes dues et affectations obligatoires spéciales de L243-1-2 et R243-8-1 restent applicables aux personnels concernés."
  r['substantive_impact']['effects'][0]['affected_population']="Entreprises admissibles au versement en lieu unique volontaire, sans dérogation aux affectations obligatoires applicables aux personnels concernés."
  r['substantive_impact']['assessment']+=" La suppression de l’autorisation ne crée pas un droit de contourner les affectations obligatoires spéciales L243-1-2/R243-8-1."
 else:continue
 r['substantive_impact_certificate']=certificate(r,by[r['source_id']],sha(P/'policy-coordinations.json'))
put('answer.json',rows)
a=json.loads((A/'answer.json').read_text());changed=[x['number']for x,y in zip(a,rows)if x!=y];assert changed==['L613-2','R243-8'];assert sha(P/'source.json')==sha(A/'source.json');assert sha(P/'context.json')==sha(A/'context.json')
put('edition-delta.json',dict(predecessor='edition001',predecessor_answer_sha256=sha(A/'answer.json'),changed_articles=changed,other_objects_strictly_identical=22,sources_identical=True,context_identical=True,corrections=['L613-2 : ET cumulatif pour données non transmises et non directement obtenables légalement, non OU.','R243-8 : option sans agrément sous réserve expresse des affectations obligatoires L243-1-2/R243-8-1 pour leurs personnels.'],counterexamples=[dict(case='Donnée exacte déjà légalement obtenable auprès de la DGFiP mais non encore transmise',edition001='La première branche OU pouvait justifier une nouvelle demande.',edition002='La condition cumulative ne permet pas de redemander cette donnée pour cette seule raison.'),dict(case='Personnel affecté obligatoirement à un organisme désigné',edition001='Le choix libre pouvait sembler supplanter l’affectation obligatoire.',edition002='L’option ne déroge pas à l’affectation obligatoire de ce personnel.')],material_measure_ids_unchanged=True,national_savings=None))
(P/'REPORT.md').write_text((A/'REPORT.md').read_text()+"\n\nÉdition002 : deux corrections normatives seulement après contrelecture indépendante. L613-2 cumule absence de transmission et impossibilité d’obtention directe légale auprès d’une autre administration. R243-8 réserve les affectations obligatoires de L243-1-2 et R243-8-1 pour leurs personnels. Les22autres objets, les24sources, notes et avant-images et les33cibles restent identiques. Aucun nouveau gain n’est compté ; la dispense CRPA demeure une coordination. Sources primaires CRPA et limites de provenance inchangées. L’édition001 reste conservée avec son rejet ; aucun actif modifié.\n")
print('ANSWER',sha(P/'answer.json'))
