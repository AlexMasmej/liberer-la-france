import json,re,html,copy
from xml.etree import ElementTree as ET
S=json.load(open('source.json'));A=json.load(open('answer.json'));R=json.load(open('reference-targets.json'))
def plain(x):return html.unescape(re.sub('<[^>]+>','',x or ''))
def p(t):return '<p>'+t+'</p>'
by={a['number']:a for a in A}; sb={a['number']:a for a in S}
a=by['R7232-19']
a['proposed_xml']=p("Aucun état trimestriel d'activité, bilan annuel qualitatif et quantitatif ou tableau statistique annuel n'est exigé au titre du présent article. Aucune transmission de ces documents au préfet ou aux ministres n'est requise.")+p("Cette dispense s'applique également aux états et bilans distinguant l'activité de chaque établissement lorsque la personne morale ou l'entrepreneur individuel dispose de plusieurs établissements.")+p("L'utilisation du logotype identifiant le secteur des services à la personne est facultative. Ce logotype est mis gratuitement à la disposition des personnes morales et des entrepreneurs individuels par le ministre chargé de l'économie.")+p("Ces dispositions s'appliquent à compter de l'entrée en vigueur de la réforme, y compris aux formalités restant à accomplir. L'absence de ces documents et la non-utilisation du logotype ne peuvent justifier le retrait d'un avantage fiscal ou social. Les droits, créances et recours relatifs aux périodes antérieures sont préservés, sous réserve des dispositions répressives plus douces.")
e=a['substantive_impact']['effects'][0]
e.update(description='Suppression du reporting périodique spécifique, de ses ventilations et transmissions, ainsi que de l’apposition obligatoire du logo.',before='États au moins trimestriels, bilan qualitatif et quantitatif annuel et tableau statistique annuel, ventilés par établissement et transmis ; logo imposé sur tous les supports commerciaux.',after='Aucun de ces états, bilans, tableaux ou transmissions exigé ; logo facultatif et toujours gratuit.',source_quote=plain(sb['R7232-19']['source_xml']).strip(),proposed_quote=plain(a['proposed_xml']))
# Une seule entrée démontre les deux modalités retirées d'une même procédure d'information.
a=by['R7232-21'];e=a['substantive_impact']['effects'][0]
e.update(source_quote=plain(sb['R7232-21']['source_xml']).strip(),proposed_quote=plain(a['proposed_xml']),before='Information sans délai par lettre individuelle ; à défaut et après mise en demeure, publication payante dans deux journaux locaux ou un local et un national si activité dans au moins deux régions.',after='Information sans délai de chaque bénéficiaire par tout moyen prouvable ; suppression du support imposé et de toute publication payante au titre de cet article.')
# Précision : le renvoi réserve une règle opératoire, il ne vise pas un emplacement « Réservé ».
a=by['R7331-4'];a['review_notes']="L7332-2 conserve la responsabilité de la coopérative pour durée du travail, repos, congés, santé et sécurité lorsque les conditions sont fixées par elle ou soumises à son accord, ainsi que les avantages légaux dans tous les cas. Le devoir d'information et de conseil de R7331-4 complète cette protection ; aucun préavis ni seuil d'indemnité ne le limite."
a['substantive_impact']['scope_limitations']=a['review_notes']
# Ne pas présenter l'exclusion générale AT-MP comme absolue : fraction spécialement exonérée au III.
a=by['R7232-18'];a['benefit_review']="L'exonération sociale des structures déclarées est ouverte plus tôt, dès réception du dossier complet, aux rémunérations futures éligibles comme aux dossiers complets en cours pour les périodes postérieures. Les exonérations des I, II et III, les déductions de 2 € et de 3,70 €, les seuils de 120 % et 160 % du SMIC et l'exonération vieillesse de 100 % des agents territoriaux restent dans leurs champs propres. L'exclusion générale AT-MP n'efface pas la fraction spécialement exonérée au III pour certains employeurs privés. Aucun plafond, non-cumul, avantage fiscal autonome ou droit ancien n'est supprimé."
for n in ['R7232-20','R7232-21','D7233-1']:
 a=by[n]
 a['review_notes'] += " La coordination fiscale suppose l'entrée en vigueur concomitante des dispenses de L7233-2 et 199 sexdecies ; aucune dispense sociale générale n'en résulte. Les cibles supplémentaires L7232-8, L7233-2 et R7232-17 ont été consultées dans le corpus public ; elles ne font pas partie des empreintes requises de reference-targets.json."
# Réduction d'attente : extension de période exonérée, pas modification du taux.
e=by['R7232-18']['substantive_impact']['effects'][0]
e['unit']='other';e['before']="Pour les structures déclarées, ouverture de l'exonération le premier jour du mois suivant la publication du récépissé, aux assiettes, taux et plafonds propres à L241-10."
e['after']="Pour les mêmes structures et assiettes, ouverture dès réception du dossier complet ; aucun taux ni plafond changé. Les rémunérations de cette période supplémentaire deviennent éligibles."
# Vérifications structurelles et citations exactes ; pas une validation juridique.
assert len(A)==len(S)==24
for s,a in zip(S,A):
 for k in ['code_id','source_id','source_sha256','number']:assert a[k]==s[k],(a['number'],k)
 imp=a['substantive_impact'];assert imp['version']==1
 for k in ['assessment','scope_limitations','new_burdens_review']:assert len(imp[k])>=40
 effects=imp['effects'];keys=[(e['measure_id'],e['kind']) for e in effects];assert len(keys)==len(set(keys)),a['number']
 for e in effects:
  assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',e['measure_id']) and 6<=len(e['measure_id'])<=96
  for k,body in [('source_quote',s['source_xml']),('proposed_quote',a['proposed_xml'])]:assert len(e[k])>=12 and e[k] in plain(body),(a['number'],k)
 req=R['requirements'][s['code_id']+'|'+s['source_id']]
 assert sorted(req)==sorted(x['target_key'] for x in a['reference_checks'])
 for x in a['reference_checks']:assert x['view_sha256']==R['targets'][x['target_key']]['view_sha256'] and len(x['assessment'])>=80
 if s.get('benefit_check_required'):assert len(a.get('benefit_review',''))>=100
 if a['proposed_xml'] is not None:
  root=ET.fromstring('<root>'+a['proposed_xml']+'</root>')
  for el in root.iter():
   assert el.tag in 'root p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split()
   for k,v in el.attrib.items():assert k in ['rowspan','colspan'] and v.isdigit()
 if a.get('change_type')=='normative_reduction':assert all(len(t)>=30 for t in a['removed_provisions'])
 if a.get('change_type')=='full_repeal':assert plain(a['proposed_xml']).startswith(('Le présent article est abrogé','Abrogé')) and len(a['repeal_scope'])>=30
 if a['status']=='retained_unchanged':assert a['proposed_xml'] is None and not effects
json.dump(A,open('answer.json','w'),ensure_ascii=False,indent=2)
print('24 articles ; identifiants, citations, XML, avantages requis, renvois et absence de doublons contrôlés.')
print({k:sum(a['status']==k for a in A) for k in ['rewrite_draft','retained_unchanged']})
