from pathlib import Path
import json,hashlib,re,html
base=Path('legal-rewrite');work=base/'runtime/sru-reglementaire'
rows=json.loads((work/'articles.candidates.json').read_text());audit=json.loads((work/'reference-audit.json').read_text())
for r in audit['incoming_references']:
 if r['number']=='R445-24':r['assigned']=True;r['resolution']='Coordination attribuée ensuite : catégorie 4° IV L302-5 et équivalences III R302-15 ; seuils CUS conservés.'
 if r['number']=='R371-1':r['resolution']='Le 5° R362-2 est abrogé ; la plage de renvois inclut une entrée abrogée sans rétablir de compétence. La communication du bilan général demeure au L302-9 proposé, sans nouvel avis obligatoire.'
 if r['number']=='R374-1':r['resolution']='Hors lot ; conserver exclusion territoriale applicable aux anciennes créances dans les dispositions transitoires.'
 if r['number'] in ['R362-10','R362-15']:r['resolution']='Renvoi général CRHH conservé ; la délégation ne rétablit aucune compétence sur la carence.'
for r in audit['other_cch_regulatory_SRU_references']:
 r['assigned_to']='is_transition';r['resolution']='Coordination séparément attribuée ; non traitée par ce lot.'
audit['coverage']=[{'number':r['number'],'source_id':r['source_id'],'decision':r.get('change_type','coordination'),'scope':r.get('repeal_scope',r.get('removed_provisions',"Renvoi d'équivalence CUS uniquement ; toutes les autres dispositions conservées."))} for r in rows]
audit['retained_normative_elements']={
'R302-1-3':['suivi et évaluation du PLH','observatoire habitat/foncier','objectifs quantifiés par typologie et publics L301-1 II','localisation communale et sectorielle','réhabilitation parc public/privé et dispositifs opérationnels','rénovation urbaine et quartiers anciens dégradés','reconstitution offre sociale pour rénovation urbaine','interventions foncières','incidences PLU/cartes communales','évaluation financière et catégories de réalisateurs'],
'R302-7':['délai de trois mois','informations démographiques, économiques et documents de planification','objectifs habitat et répartition équilibrée','quartiers et conventions ANRU articles10/10-1 loi2003-710','actualisation pendant élaboration et réalisation','audition préfet/représentant à demande et compte rendu au conseil'],
'R302-15':['III/III bis numérotation','structures4° IV L302-5','un logement pour trois lits/places','arrondi à partie entière','autonomie R151-1 et élément de vie','un logement pour un terrain familial','aucun inventaire de remplacement'],
'R362-2':['compétences1°–4° et6°–20°','5° abrogé : ancien avis sur les arrêtés de carence au vu des bilans, sans consultation nouvelle sur le bilan lui-même','21° déjà abrogé','délégation2°–21° au bureau/commissionsR362-11/R362-15','information annuelle préfet L443-13'],
'R445-24':['catégories4° IV L302-5 et équivalencesIII R302-15','seuil strict moins50%','seuil50%inclus à100%exclus','totalitépatrimoine','tableau R445-36 maintenu ; ancien renvoi au tableau R445-37 supprimé après vérification canonique de son abrogation','partie/convention logements-foyers des articles suivants']}
audit['transition_checks']={
'claims':'Créances légalement nées de faits générateurs antérieurs conservées selon V L302-5 proposé, même si échéance/encaissement postérieur ; aucune créance nouvelle du seul défaut passé de quota.',
'R302-19':'Neuf échéances de mars à novembre pour créance annuelle née avant réforme ; ne sont pas neuf faits générateurs ; ni accélération ni remboursement général.',
'R302-18':'Expiration du délai de deux ans à compter de la réforme : aucune reprise nouvelle du seul défaut de commencement, malgré déduction initiale antérieure. Reprises/rectifications effectivement nées avant réforme seules conservées selon V.',
'R302-16-1':'Reports inutilisés non remboursés en bloc ; opposabilité aux seules créances anciennes préservée.',
'R302-17_R302-20':'Fin des formalités annuelles, même pour fonds antérieurs ; justificatifs ponctuels seulement pour liquidation/recours/restitution d’une créance ancienne maintenue.',
'R302-19-1':'Droits contractuels/opérateurs pour opérations engagées préservés ; pas de nouvelle opération imposée ni d’avenant forcé pour accroître obligations.',
'R302-26':'Aucun maintien/renouvellement de la commission pour liquider des créances anciennes ; voies ordinaires de recours.'}
audit['outside_five_codes_not_rewritten']=[
{'text':'Loi n°2000-1208 du13décembre2000, notamment article55 et autres dispositions de la loi','status':'Périmètre global en cours de coordination par root ; ce lot ne prétend pas abroger tous les articles de la loi.'},
{'text':'CGCT, notamment L2332-2, R2151-1, L5219-1, L4424-26-1 et documents régionaux','status':'Règles autonomes conservées ; renvois de paiement/compétences pas réécriture du CGCT.'},
{'text':'CG3P L3211-7 et CRPA R133-3 à R133-14','status':'Dispositions autonomes non modifiées ; disparition de la commission SRU ne les abroge pas.'},
{'text':'Décret n°2012-1246 du7novembre2012, articles112–124','status':'Recouvrement ordinaire et créances anciennes ; décret non modifié.'},
{'text':'Décret n°2019-1478 du26décembre2019, article13','status':'Suppression de sa date dans un inventaire SRU ; normes techniques de terrains familiaux non abrogées.'},
{'text':'Lois n°84-595 du12juillet1984, n°89-462 du6juillet1989, n°90-449 du31mai1990, n°2003-710 du1août2003','status':'Location-accession, observatoires de loyers, FSL et conventions ANRU autonomes maintenus ; non réécrits ici.'},
{'text':'Décrets de listes/exemptions/seuils SRU, arrêtés de carence et de nomination de la commission','status':'Leurs fonctions ou effets futurs du seul quota cessent par les articles coordonnés ; les actes extérieurs ne sont pas individuellement prétendus réécrits.'}]
audit['cch_outside_scope']=[
{'number':'R302-21 à R302-25','status':'Versions antérieures déjà abrogées ; aucune réactivation ou nouvelle réécriture fictive.'},
{'number':'D302-27 à D302-35','status':'Section autonome logement intermédiaire, non assimilée au régime des quotas SRU.'},
{'number':'R445-37','status':'Déjà ABROGÉ depuis le 29/07/2019 ; statut, document et note vérifiés dans r445-37.canonical-status.json ; renvoi obsolète supprimé de R445-24 sur instruction expresse, sans réactivation du tableau.'}]
audit['integration_dependencies']=['L302-5 IV définition autonome et V transition proposés par root','L302-9 communication du bilan triennal général au CRHH proposée par root, sans nouvelle consultation obligatoire dans R362-2','Urbanisme R329-11 8° et coordinations D411-2/R411-3 traités séparément par is_transition','R374-1 exclusion Mayotte ne doit pas être perdue pour des créances historiques']
audit['registered']=False;audit['published']=False
p=work/'audit.json';t=p.with_suffix('.json.tmp');t.write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n');t.replace(p)
preview=[]
for r in rows:
 preview += ['## '+r['number'], '', re.sub(r'</p>\s*<p>','\n\n',r['proposed_xml']).replace('<p>','').replace('</p>',''),'', '**Motif :** '+r['reason'], '']
p=work/'propositions.md';t=p.with_suffix('.md.tmp');t.write_text(html.unescape('\n'.join(preview)));t.replace(p)
print('Audit and full-article reading preview written.')
