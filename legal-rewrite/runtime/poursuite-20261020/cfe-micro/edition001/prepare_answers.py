"""Whole CFE provisions; only the expressly authorised micro-social relief."""
import pathlib,json,re,html
D=pathlib.Path(__file__).resolve().parent
R=json.loads((D/'captured-source-and-references.json').read_text())
S=[next(r for r in R if r['number']==n)for n in ['1447','1477','1478','1647 D']]
def pp(*texts):return '\n'.join('<p>'+t+'</p>'for t in texts)
def plain(v):return re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',v or''))).strip()
A=[]
def make(n,body,reason,notes,benefit,classification,removed=None):
    s=next(x for x in S if x['number']==n);a={k:s[k]for k in ['code_id','source_id','source_sha256','number']}
    a.update(status='retained_unchanged'if body is None else'rewrite_draft',proposed_xml=body,reason=reason,review_notes=notes,benefit_review=benefit,
             substantive_impact={'version':1,'classification':classification,'assessment':reason,
                'scope_limitations':"Mesure limitée à la CFE des activités du champ micro-social L613-7, options minimales et transitionIII incluses. Pas d'extension à tout micro-fiscal, ni modification du taux social ou du versement libératoire. Le coût pour les collectivités reste à chiffrer sans compensation ou économie inventées.",
                'new_burdens_review':"Exonération de plein droit sans demande, option ou attestation propre ; aucune déclaration CFE de remplacement. Les informations déjà légalement disponibles sont utilisées. Le retour à la CFE après fin d'éligibilité conserve les déclarations ordinaires avec une première échéance praticable, sans sanction rétroactive d'une période dispensée.",
                'effects':[]})
    if removed:a.update(change_type='normative_reduction',reform_policy_id='editorial_direction_2026_10_19',removed_provisions=removed)
    A.append(a);return a
def eff(n,kind,mid,before,after,sq,pq,desc):
    a=next(x for x in A if x['number']==n);s=next(x for x in S if x['number']==n)
    assert sq in plain(s['source_xml']),(n,sq)
    assert pq in plain(a['proposed_xml']),(n,pq)
    a['substantive_impact']['effects'].append({'kind':kind,'measure_id':mid,'unit':'legal_duty'if kind!='tax_reduced'else'euro',
        'description':desc,'before':before,'after':after,'source_quote':sq,'proposed_quote':pq,
        'affected_population':"Travailleurs indépendants du champ de L613-7 et EURL micro-sociales à associé unique personne physique dirigeant, pour les seules activités éligibles ; les autres redevables et leurs exonérations restent distincts.",
        'conditions_and_transition':"Années d'imposition à compter du1janvier suivant l'entrée en vigueur de la loi proposée ; application de plein droit. Les années antérieures, exonérations, dégrèvements, restitutions et recours acquis sont conservés sans remboursement général.",
        'replacement_or_new_burdens':"Aucune taxe, demande d'exonération ou attestation de remplacement ; les informations existantes sont réutilisées. En sortie du champ, déclaration CFE normale à première échéance aménagée, aucune nouvelle déclaration pendant l'exonération."})

s=next(x for x in S if x['number']=='1447')
body=s['source_xml'].rstrip()+'\n'+pp(
    "IV. – Sont exonérés de la cotisation foncière des entreprises les travailleurs indépendants, à raison des activités pour lesquelles ils relèvent du champ du régime défini à l'article L. 613-7 du code de la sécurité sociale au cours de l'année d'imposition. Cette exonération demeure applicable lorsqu'ils ont demandé le calcul de cotisations minimales dans les conditions du I de ce même article et pendant la période au cours de laquelle son III maintient l'application de ce régime après une option pour un régime réel d'imposition.",
    "Les sociétés à responsabilité limitée dont l'associé unique est une personne physique qui dirige la société bénéficient de la même exonération pour leur activité lorsque cet associé relève à ce titre du champ de l'article L. 613-7 du code de la sécurité sociale. Les options minimales et la période de maintien mentionnées au premier alinéa du présent IV sont également couvertes.",
    "L'exonération couvre l'ensemble des établissements affectés aux activités éligibles, que la cotisation soit calculée d'après la valeur locative des biens ou d'après la base minimum de l'article 1647 D. Elle n'est subordonnée ni à l'option pour le versement libératoire de l'article 151-0, ni au seuil de chiffre d'affaires ou de recettes de 5 000 € prévu à l'article 1647 D, ni à une délibération locale, ni à une durée limitée suivant la création. Elle n'exonère pas les activités du même redevable qui ne relèvent pas de son champ.",
    "Elle s'applique de plein droit, sans demande préalable, déclaration ou attestation propre à son bénéfice. L'administration utilise les informations qu'elle détient déjà légalement ou auxquelles elle peut légalement accéder pour l'établissement de cet impôt, dans le respect des secrets protégés et de la protection des données personnelles. L'intéressé peut faire corriger une information inexacte et exercer ses voies de réclamation. Les obligations déclaratives propres aux seuls éléments de CFE exonérés sont supprimées dans les conditions du V de l'article 1477.",
    "Le présent IV s'applique aux impositions établies au titre des années commençant à compter du 1er janvier suivant l'entrée en vigueur de la loi qui l'institue. Les impositions des années antérieures restent régies par les règles qui leur sont applicables, avec leurs exonérations, réductions, dégrèvements, restitutions, prescriptions et recours, même si leur liquidation ou leur paiement est ultérieur. Aucun remboursement général d'une cotisation antérieure légalement due n'est créé. Les autres exonérations et allègements de CFE restent applicables dans leur champ.")
make('1447',body,
    "Créer une exonération nationale complète de CFE pour les autoentrepreneurs du champ micro-social, au-delà de la seule cotisation minimum et du seuil actuel de5000€. Elle est permanente tant que les conditions de statut sont remplies et automatique, sans option fiscale libératoire ni délibération locale. Les autres redevables et avantages restent inchangés.",
    "Source entière et note DILA vide lues. 50-0/102ter et leurs propositions actuelles,151-0, CSSL613-7,1477/1478,1467/1467A,1647D et1647Bsexies entier/projet lus. Le champ n'est pas tous les petits revenus microfiscaux : leII deL613-7 et ses extensions légales règlent les indépendants concernés. L'option de cotisations minimales n'est pas une sortie de l'exonération ; le maintien au31décembre prévu auIII est expressément couvert. Les EURL dont l'associé unique dirigeant relève du micro-social pour cette activité sont visées, BIC ou BNC : la personnalité morale ne doit pas faire perdre l'avantage. Cette condition sociale couvre aussi la transitionIII sans imposer cumulativement le maintien fiscal au micro durant l'année de l'option au réel. Les I/II/III antérieurs sont conservés intégralement, y compris locations nues à100000€, organismes non lucratifs et territorialité. Aucune option151-0, condition familiale ou durée de l'ancien1464K abrogé n'est ressuscitée. Le cumul éventuel d'aides d'État et le financement local restent à examiner dans le cadre européen applicable ; ce texte ne prétend y déroger ni inventer une déclaration de minimis.",
    "Toutes les exonérations existantes, y compris celles des organismes non lucratifs, locations hors champ, professions et zones, demeurent. L'avantage nouveau couvre locaux propres, domiciliation et cotisation minimum pour les activités éligibles, y compris au-delà de5000€, options minimales et transition micro-sociale. Il ne retire aucun dégrèvement des années antérieures ni l'exonération de création ; aucun taux social20% n'est fixé.",
    'material_reduction')
eff('1447','tax_reduced','cfe-exoneration-micro-sociale',
    "CFE annuelle éventuellement due par le microentrepreneur sur une base locative ou minimum, selon taux local, malgré son statut ; certains sont déjà exonérés selon leur situation.",
    "CFE égale à zéro pour les seules activités éligibles, dans tous leurs établissements, sans seuil additionnel5000€ ni limite de deux ans ; les activités non éligibles restent à leur régime.",
    "La cotisation foncière des entreprises est due chaque année par les personnes physiques ou morales",
    "Sont exonérés de la cotisation foncière des entreprises les travailleurs indépendants",
    "Exonération totale d'une population déterminée, pas suppression de la CFE pour toutes les entreprises ; montant et recettes locales non chiffrés.")

s=next(x for x in S if x['number']=='1477')
body=s['source_xml'].rstrip()+'\n'+pp(
    "V. – Pour les années et les seules activités exonérées au titre du IV de l'article 1447, les déclarations prévues aux I et II du présent article ne sont pas exigées pour les éléments exclusivement destinés à l'établissement de cette cotisation. Cette dispense comprend la déclaration provisoire de création, de changement d'exploitant ou d'activité et, pour les éléments relevant de ces seules activités exonérées, la déclaration de l'ancien exploitant. Aucun état périodique ni déclaration d'exonération de remplacement n'est requis. Les déclarations qui demeurent nécessaires à l'établissement d'une CFE relative à une autre activité ou à une année non exonérée conservent leur objet propre.",
    "Lorsque l'activité cesse de bénéficier de cette exonération, la première déclaration nécessaire à l'établissement de la CFE au titre de l'année redevenue imposable est souscrite au plus tard le deuxième jour ouvré suivant le 1er mai de cette même année. Les échéances ordinaires s'appliquent ensuite. Les éléments déjà légalement disponibles et exacts ne sont pas fournis à nouveau ; les obligations qui ne pouvaient être exigées pendant une période exonérée ne donnent lieu à aucune sanction pour défaut de déclaration pendant cette période. Cette règle ne dispense ni des impôts légalement dus pour les années non exonérées, ni des informations nécessaires qui ne sont pas déjà disponibles.",
    "Le présent V s'applique aux éléments servant aux impositions couvertes par le IV de l'article 1447, y compris lorsque l'échéance déclarative les précède. Les déclarations déjà régulièrement déposées restent utilisables et ne sont pas à redéposer. Les obligations et procédures relatives aux impositions antérieures conservent leurs règles et leurs voies de recours ; la dispense ne porte pas atteinte aux droits à décharge, réduction ou restitution.")
make('1477',body,
    "Supprimer les déclarations exclusivement CFE pour les activités devenues intégralement exonérées, y compris la déclaration provisoire de création, sans nouveau formulaire d'exonération. Rendre le retour à une CFE taxable opératoire : première déclaration en mai de l'année taxable, sans imposer rétroactivement une échéance expirée pendant l'exonération.",
    "Source entière et note DILA vide lues. I,IIa/IIb,III abrogé etIV de lieu de dépôt sont conservés pour les autres activités et années. IV1447 proposé et1478 annuel entier contrôlés. La première échéance de sortie est une adaptation favorable d'une déclaration déjà prévue, pas une déclaration nouvelle durant l'exonération. Les éléments CFE nécessaires au nouvel exploitant non exonéré restent déclarés par celui-ci ; les seules pièces déjà disponibles ne sont pas collectées deux fois. Aucun nouveau signalement annuel de statut, portail ou certificat URSSAF n'est créé. Les autres obligations fiscales, sociales et les données foncières légalement autonomes ne sont pas abrogées.",
    "La suppression de déclaration n'est pas une condition à remplir pour l'exonération. Les options minimales, sorties au31décembre et EURL éligibles du1447IV sont couvertes. Les droits de réclamation et restitutions anciens demeurent, et la première échéance aménagée évite une sanction de défaut de dépôt alors que la déclaration était dispensée.",
    'material_reduction',removed=["Déclarations des I etII exclusivement destinées à la CFE des activités exonérées au titre du nouveau1447IV, y compris provisoire de création, sans dossier d'exonération de remplacement."])
eff('1477','obligation_removed','cfe-micro-declarations-supprimees',
    "Déclarations CFE de base et provisoires exigibles même en l'absence de somme à payer au titre de certains allègements actuels.",
    "Aucune déclaration exclusivement CFE pour les activités du1447IV ; informations des autres activités et premières années taxables conservées dans leur champ.",
    "Les contribuables doivent déclarer les éléments servant à l'établissement de la cotisation foncière des entreprises",
    "les déclarations prévues aux I et II du présent article ne sont pas exigées",
    "Retirer les déclarations dont la CFE exonérée est le seul objet ; une seule mesure de formalités, distincte du gain fiscal.")
eff('1477','relief_extended','cfe-micro-sortie-premiere-echeance',
    "Échéance ordinaire de mai l'année précédente susceptible d'être déjà passée lorsque prend fin le statut exonéré.",
    "Première déclaration de retour à la CFE en mai de l'année redevenue taxable ; échéances ordinaires ensuite.",
    "l'année précédant celle de l'imposition au plus tard le deuxième jour ouvré suivant le 1er mai",
    "au plus tard le deuxième jour ouvré suivant le 1er mai de cette même année",
    "Première échéance déclarative praticable à la sortie de l'exonération, sans réduire l'impôt de l'année redevenue taxable.")

make('1478',None,
    "Maintien intégral nécessaire : annualité de la CFE, exonération de création, demi-base de première imposition, cessation, saisonnalité et régimes de changement d'exploitant restent utiles aux entreprises hors champ micro-social et aux années antérieures. L'exonération explicite du1447IV est une exception à l'assujettissement, sans imposer une réécriture cosmétique de ces garanties.",
    "Source entière et note2026-103 article44/1janvier2026 lues. Aucun numéro, sous-paragraphe, régime d'organisme non lucratif ou période de deux ans n'est modifié. L'exception électrique de raccordement et les avantages saisonniers demeurent. La sortie du nouveau champ est coordonnée au1477V pour éviter une échéance déclarative rétroactive. Le présent article n'est compté ni comme réécrit ni comme un nouvel allègement.",
    "Exonération de l'année de création, réduction de moitié de la base de première année taxable, prorata de cessation dans ses cas et corrections saisonnières restent applicables. Les autres organismes et contribuables ne perdent aucun avantage ; la nouvelle exonération micro-sociale ne les remplace pas.",
    'retained_necessary')

s=next(x for x in S if x['number']=='1647 D')
old="I. – 1. Les redevables de la cotisation foncière des entreprises sont assujettis à une cotisation minimum établie au lieu de leur principal établissement ;"
new="I. – 1. Les redevables de la cotisation foncière des entreprises, à l'exception des bénéficiaires de l'exonération du IV de l'article 1447 pour leurs activités éligibles, sont assujettis à une cotisation minimum établie au lieu de leur principal établissement ;"
assert s['source_xml'].count(old)==1
body=re.sub(r' (?:align|border)="[^"]*"','',s['source_xml'].replace(old,new,1))
make('1647 D',body,
    "Coordonner expressément le minimum de CFE avec la nouvelle exonération globale : le minimum ne doit pas reconstituer la taxe des activités micro-sociales exonérées. Tout le tableau, la réduction Mayotte, les autres exonérations et le régime des autres redevables sont conservés à l'identique.",
    "Source entière avec tableau à six tranches et note technique de coordination lue. Seul ajout normatif dans le premier alinéa duI1 ; tous les textes, nombres, cellules et subdivisions suivants sont conservés. Les seuls attributs HTML de présentation align/border sont retirés pour le validateur, sans toucher le contenu. Le tableau reste le deuxième alinéa pour le renvoi duIbis1°, aucune insertion ne décale ses références. Seuils10000/32600/100000/250000/500000, bornes250/597/1194/2509/4183/5974/7769, franchise5000 avec sa condition européenne, actualisation, plafond de convergence80%, délais historiques et division Mayotte sont intacts. Aucun montant uniforme de CFE dû par tous les autoentrepreneurs n'est inventé : les montants du tableau sont des bases, pas une taxe forfaitaire nationale.",
    "Les autres redevables conservent notamment l'exonération de cotisation minimum jusqu'à5000€, les avantages Mayotte, le plafonnement de base par tranche et les convergences. Les nouveaux bénéficiaires du1447IV sont exonérés du minimum sans être soumis à ce seuil5000 ou aux conditions de cet avantage distinct ; domiciliations et absence de locaux ne recréent pas de CFE.",
    'coordination_only')
eff('1647 D','coordination','cfe-exoneration-micro-sociale',
    "Les redevables CFE sont assujettis à un minimum, sous leurs exceptions existantes.",
    "L'activité exonérée par1447IV est expressément hors minimum ; tableau et autres exceptions inchangés.",
    "Les redevables de la cotisation foncière des entreprises sont assujettis à une cotisation minimum",
    "à l'exception des bénéficiaires de l'exonération du IV de l'article 1447 pour leurs activités éligibles",
    "Même exonération micro-sociale que1447IV, pas une deuxième baisse fiscale.")

(D/'source.json').write_text(json.dumps(S,ensure_ascii=False,indent=2)+'\n')
(D/'answer.json').write_text(json.dumps(A,ensure_ascii=False,indent=2)+'\n')
print('Four records: 3 whole proposals, 1 integral necessary source')
