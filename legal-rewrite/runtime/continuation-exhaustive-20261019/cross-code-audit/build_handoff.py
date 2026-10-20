from pathlib import Path
import json,hashlib,collections
P=Path(__file__).resolve().parent
sha=lambda x:hashlib.sha256(x).hexdigest()
inventory=json.loads((P/'edition001/reference-inventory.json').read_text())
packs={};selected={}
for edition in ['edition001','edition002','edition003']:
    sources=json.loads((P/edition/'source.json').read_text());answers=json.loads((P/edition/'answer.json').read_text())
    packs[edition]={'articles':len(answers),'source_sha256':sha((P/edition/'source.json').read_bytes()),'answer_sha256':sha((P/edition/'answer.json').read_bytes()),'path':str(P/edition)}
    for s,a in zip(sources,answers):selected[(s['code_id'],s['source_id'])]={'edition':edition,'number':s['number'],'slug':s['slug'],'proposed_sha256':hashlib.sha256(a['proposed_xml'].encode()).hexdigest()}
compatible={
 ('securite-sociale','L137-15'):"Les exclusions de forfait social visent les indemnités de licenciement/retraite/PSE et ne sont pas conditionnées à un supportCDD ; les nouvelles ruptures patronales gardent la qualification de licenciement et les renvoisTravail sont maintenus.",
 ('securite-sociale','L242-1'):"Exclusions d'assiette des indemnités liées à80duodecies et protection complémentaireL911-7-1 ne subordonnent pas le droit à unCDD ; plafonds2/5/10PASS et cumul des indemnités restent distincts du barème de droit du travail.",
 ('securite-sociale','L311-4'):"Le travail temporaire subsiste sous le nouveau CDI intérimaireL1251-1 ; maintien du régime général même chez utilisateur d'autre régime, sous réserve agricole, sans condition de terme de l'emploi.",
 ('securite-sociale','D323-6'):"L'essai encadré est déjà ouvert au salarié du régime général ainsi qu'aux bénéficiairesL1251-1/L6221-1 ; le nouveau support ne les exclut pas et ne transforme pas cet essai thérapeutique en essai d'embauche.",
 ('securite-sociale','R130-2'):"Affectation déclarative à l'établissement du registre uniqueL1221-13 sans conditionCDD ni durée de mission ; aucune donnéeCVAE nouvelle n'en résulte.",
 ('securite-sociale','R242-1-4'):"Dispense favorable de taux uniforme pour prise en charge intégrale des temps partiels/apprentis au seuil10% du brut ; foyer et prévoyance restent indépendants du terme du contrat.",
 ('securite-sociale','D160-15'):"Le changement automatique d'organisme couvre déjà toutCDI ; les nouveaux contrats uniques ne perdent donc pas cette voie par la condition alternativeCDD6mois. Conditions100heures/100SMIC et exceptions restent distinctes.",
 ('construction-habitation','L421-12'):"DirecteurOPH : contrat et détachement de droit public spécial, réintégration du fonctionnaire et indemnité propre ; aucun alignement silencieux sur le préavis/barème privé.",
 ('construction-habitation','L421-12-2'):"Convention de rupture du directeurOPH et exclusion du fonctionnaire détaché relèvent du statut propre ; ni indemnité ni assistance ne sont supprimées par le CDI privé.",
 ('construction-habitation','L631-12'):"Accueil des apprentis/professionnalisation et jeunes en formation : les contrats d'apprentissage/professionnalisation restent nommés tels dansL6222-7/L6325-5 avec phase initiale sousCDI ; pas de conditionCDD. Le bail universitaire conserve son régime distinct.",
 ('construction-habitation','L631-16-1'):"Résidence à vocationd'emploi : critère matériel d'études/formation/apprentissage/mutation/mission temporaire, sans exigerCDD. La limite1semaine–18mois est celle du logement, pas celle de l'emploi.",
 ('construction-habitation','D822-0-2'):"Présomption favorable de bourse pour apprentis/professionnalisation au sensL6221-1/L6325-1 reste applicable pendant les phases de même objet ; ces qualifications demeurent sous les nouveauxCDI, sans conditionCDD.",
 ('impots','80 duodecies'):"Indemnités de licenciement et ruptures conventionnelles exemptées selon leurs plafonds et garanties, indépendamment d'unCDD ; le nouveau barème matérielL1234-9 n'est pas une nouvelle catégorie d'IR. Maintien des plafonds6/5PASS, minima conventionnels plusfavorables, PSE, réparations et agentspublics.",
 ('impots','80 sexies'):"Régime propre assistantsmaternels/familiauxCASF ; abattements3/4SMIChoraire et+1pour24heures conservés. Le présent audit ne soumet pas ces salariés au nouveau barème privé en effaçant leCASF horscorpus.",
 ('impots','231 bis R'):"Exonération taxe sursalaires des enseignantsCFA fondée sur leurs fonctions, sans condition de terme du contrat.",
 ('impots','244 quater F'):"Crédit famille50%/25% et dispositions historiques10% concernant dépenses2009 ; aucune conditionCDD. Démission/licenciement du b restent des qualifications des ruptures sous contrat unique. Les crédits ne sont pas supprimés par le report de l'IS à la distribution.",
 ('impots','1468'):"Réductions de baseCFE3/4,1/2,1/4 et exclusion des apprentis souscontrat restent accessibles pendant l'apprentissageL6222-7 ; lescoopératives et anciennes étapes mutuelles demeurent distinctes. Pas de conditionCDD ni de créationCVAE.",
 ('impots-annexe-2','310 HA'):"Prorata tempspartiel/saisonniers fondé sur durée réelle et définition apprentissageL6221-1àL6225-8 conservée sousnouveauCDI ; absence de conditionCDD. Définitions des handicapés et établissement restent autonomes.",
 ('impots-annexe-3','40 A'):"La déduction déclarative des rémunérations d'apprentis/personneshandicapées reste matérielle. La proposition antérieure supprime déjà le calculCVAE futur et les doubles pièces ; aucune restauration de ces obligations.",
 ('impots-annexe-3','322 H'):"Emplois permanents définis parCDI : les nouveaux contrats uniques satisfont déjà cette condition ; ajout d'une restriction nouvelle aux affectations temporaires aurait fermé un avantage sans mandat. Tempspartielprorata et emploisnets intacts.",
 ('impots-annexe-3','328 G quater'):"La proposition actuelle abroge toutes les déclarations de personnelCVAE pour les années supprimées, y compris missions ; ne pas réécrire les anciensCDD pour faire renaître une obligation future. Droits et obligations des anciennes années préservés.",
}
results=[]
for x in inventory:
    key=x['code_id'],x['source_id'];y=x.copy();name=x['slug'],x['number']
    if key in selected:y.update(audit_status='whole_article_candidate_delivered',delivery=selected[key],requires_independent_review=True)
    elif name in compatible:y.update(audit_status='whole_article_review_no_new_coordination_identified',decision=compatible[name])
    elif x['draft_category']=='previously_contract_unique_coordinated':y.update(audit_status='previous_integrated_contract_unique_draft_matches_snapshot',decision='Concordance exacte avec le lot antérieur enregistrée à la capture ; toute mutation ultérieure doit périmer ce contrôle. Pas de prétention de nouvelle rédaction dans le présent lot.')
    else:y.update(audit_status='pending_concordance_queue',decision='Recherche positive seulement. Corps/notes/avant-image capturés entiers, mais pas encore examen juridique complet de cette entrée ; ne pas compter comme relue, corrigée ou compatible.',priority='contract_or_employment_context'if any(t in x['tags']for t in ['fixed_term','indefinite','mission_temporary','training_season_replacement','employment_termination'])else'outgoing_reference_or_broad_indemnity_filter')
    results.append(y)
(P/'concordance-queue.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
summary={'canonical_candidates':len(inventory),'examined_current_articles_for_text_and_link_search':18724,'candidate_unique_articles':len(selected),'candidate_articles_inside_initial_inventory':sum((x['code_id'],x['source_id'])in selected for x in inventory),'additional_candidate_not_matched_initial_broad_search':[v for k,v in selected.items()if k not in {(x['code_id'],x['source_id'])for x in inventory}],'status_counts':dict(collections.Counter(x['audit_status']for x in results)),'frozen_packs':packs,'merge_rule':'Take edition001 except AnnIII39, replaced by edition002; add four other edition002 articles and all four edition003 articles.28distinctidentifiers. No integration by author.','remaining_queue_not_normatively_completed':True,'all_proposals_or_reviews_invalidated_on_dependency_change':True}
(P/'handoff.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n');print(json.dumps(summary,ensure_ascii=False,indent=2))
