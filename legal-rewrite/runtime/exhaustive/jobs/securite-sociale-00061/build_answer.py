import json, re, html
from pathlib import Path
S=json.loads(Path('source.json').read_text())
R=json.loads(Path('reference-targets.json').read_text())
B={a['number']:a for a in S}
A={}

def text(x):
    return html.unescape(re.sub('<[^>]+>', '', x or ''))

def add(n, reason, notes, assessment, scope, burdens, benefit, proposed=None, classification='retained_necessary', removed=None, repeal=None):
    s=B[n]
    a={k:s[k] for k in ['code_id','source_id','source_sha256','number']}
    a.update(proposed_xml=proposed,reason=reason,review_notes=notes,status='retained_unchanged' if proposed is None else 'rewrite_draft',benefit_review=benefit)
    if proposed is None:
        a['classification']='retained_necessary'
    if removed:
        a.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19',removed_provisions=removed)
    if repeal:
        a.update(change_type='full_repeal',repeal_policy_id='editorial_direction_2026_10_19',repeal_scope=repeal)
    a['substantive_impact']=dict(version=1,classification=classification,assessment=assessment,scope_limitations=scope,new_burdens_review=burdens,effects=[])
    A[n]=a
    return a

def effect(n,kind,measure,description,before,after,unit,pop,conditions,replacement,sq,pq):
    assert sq in text(B[n]['source_xml']), (n,'source',sq)
    assert pq in text(A[n]['proposed_xml']), (n,'proposal',pq)
    assert len(sq)>=12 and len(pq)>=12
    effects=A[n]['substantive_impact']['effects']
    assert not any(e['measure_id']==measure and e['kind']==kind for e in effects), (n,'Duplicate measure and effect',measure,kind)
    effects.append(dict(kind=kind,measure_id=measure,description=description,before=before,after=after,unit=unit,affected_population=pop,conditions_and_transition=conditions,replacement_or_new_burdens=replacement,source_quote=sq,proposed_quote=pq))

def replace(n,old,new):
    s=B[n]['source_xml']
    assert s.count(old)==1, (n,old)
    return s.replace(old,new)

def append(s,*paras):
    return s.rstrip()+''.join('\n<p>'+p+'</p>' for p in paras)+'\n'

p=replace('L432-1',
    "Les dispositions du II et du III de l'article L. 160-13 sont applicables aux bénéficiaires du présent livre.",
    "Les participations forfaitaires et les franchises prévues aux II et III de l'article L. 160-13 ne sont pas dues au titre des prestations servies en application du présent livre.")
p=append(p,
    "Cette suppression s'applique aux actes, consultations, produits, transports et autres prestations réalisés ou délivrés à compter de l'entrée en vigueur de la loi portant la présente modification, y compris lorsque le sinistre est antérieur à cette date. Aucun prélèvement ou reste à charge de remplacement n'est institué à ce titre. Les participations et franchises afférentes aux prestations antérieures restent soumises aux règles qui leur étaient applicables, avec leurs exonérations, plafonds, modalités de paiement, restitutions, prescriptions et recours. Aucun remboursement général des sommes légalement dues pour ces prestations antérieures n'est ouvert.")
add('L432-1',
    "Réduction de fond : suppression de l'application aux prestations AT-MP des participations forfaitaires et franchises des II et III de L. 160-13. Le renvoi source impose bien des paiements accessoires ; leur fonction essentielle propre aux soins du risque professionnel n'est pas démontrée. Le premier alinéa demeure entier : paiement direct des prestations des 1° et 3° de L. 431-1 et possibilité de remboursement des transports. Aucun financement ou prélèvement de remplacement n'est créé.",
    "L. 160-8 et L. 160-13 ont été lus en entier avec leurs notes dans le corpus public. Le II impose une participation par acte ou consultation médicale et acte de biologie, avec plafonds ; le III une franchise sur médicaments, actes d'auxiliaires, transports hors urgence et prestations d'officine, avec plafonds. Les montants réglementaires ne figurent pas dans la source assignée et ne sont pas inventés. La suppression ne concerne que les prestations servies au titre du livre IV, sans exonérer toute dépense de maladie sans rapport avec ce risque ni modifier le I de L. 160-13. Coordonner les règlements de liquidation et récupération des II et III pour les prestations AT-MP nouvelles ; les plafonds et exemptions plus favorables restent pour le stock ancien et les autres prestations. Les 1° et 3° de L. 431-1 visent les soins et frais accessoires puis les prestations hors rentes au décès ; le 2° de L. 160-8 concerne les transports. Les prestations de décès ne sont pas un droit fiscal de succession. Perte de recettes et solde public net à établir, sans recette de compensation présumée.",
    "Par rapport à la source officielle entière, le paiement accessoire résultant du deuxième alinéa disparaît pour les prestations AT-MP nouvelles. Il s'agit d'une suppression durable dans ce champ, distincte d'un simple décalage de paiement et du maintien du tiers payant.",
    "Les soins de maladie sans lien avec le risque professionnel et les participations ayant un autre fondement restent hors champ. Aucun montant individuel ou national, ni solde net de l'ensemble des codes, n'est établi ; les textes de liquidation doivent être coordonnés.",
    "Aucune charge nouvelle n'est identifiée : aucune attestation, déclaration, autorisation ou donnée supplémentaire ne remplace les paiements supprimés. La reconnaissance du risque professionnel et les contrôles existants gardent leur objet sans nouveau circuit.",
    "Le paiement direct et le remboursement des transports sont maintenus pour les futures victimes. La franchise du III de L. 160-13 est un reste à charge et non une franchise fiscale exonérante. Les exonérations et plafonds des participations anciennes restent applicables ; pour les prestations AT-MP nouvelles, leur avantage devient sans objet parce que ces paiements sont entièrement supprimés dans ce champ, sans équivalent ni extension d'assiette. Les droits favorables applicables aux soins relevant d'autres risques ne sont pas retirés.",p,'material_reduction',[
        "Application aux prestations AT-MP nouvelles des participations forfaitaires et franchises des II et III de l'article L. 160-13, y compris leur paiement et leur récupération sur les prestations futures."
    ])
effect('L432-1','obligation_removed','atmp-participations-franchises-suppression',
    "Suppression du paiement des participations et franchises sur les prestations servies au titre du risque professionnel.",
    "Application des II et III de L. 160-13 : participations par acte, consultation ou biologie et franchises par produit ou prestation, aux montants et plafonds de leur régime ; aucune assiette salariale ni taux fiscal n'est en cause.",
    "Aucune participation ou franchise de ces II et III due sur les prestations du livre IV réalisées ou délivrées après l'entrée en vigueur ; les autres risques et prestations anciennes gardent leur régime.",'legal_duty',
    "Bénéficiaires des prestations d'accidents du travail et de maladies professionnelles du livre IV.",
    "Prestations nouvelles même liées à un sinistre ancien ; dettes, exonérations, plafonds, restitutions et recours des prestations antérieures protégés.",
    "Aucun paiement, formalité ou prélèvement de remplacement ; reconnaissance de l'origine professionnelle et contrôles existants maintenus.",
    "Les dispositions du II et du III de l'article L. 160-13 sont applicables aux bénéficiaires du présent livre.",
    "Les participations forfaitaires et les franchises prévues aux II et III de l'article L. 160-13 ne sont pas dues au titre des prestations servies en application du présent livre.")

add('L432-2',
    "Maintien intégral du libre choix du médecin, du pharmacien et des auxiliaires médicaux prescrits. Cette liberté protège la victime et ne constitue pas une autorisation administrative ou un justificatif redondant. La supprimer créerait une contrainte ; aucun nouveau corps stylistique n'est utile.",
    "La prescription ne concerne ici que l'intervention des auxiliaires médicaux ; ne pas l'étendre au choix du médecin ou du pharmacien. Aucun changement des conditions de couverture ni des compétences professionnelles.",
    "Aucun changement normatif : la liberté de choix est maintenue avec la qualification de prescription propre aux auxiliaires médicaux.",
    "Les conditions médicales et tarifaires extérieures à cet article ne sont pas supprimées ; aucune réduction nette de coût n'est revendiquée.",
    "Aucune charge nouvelle n'est identifiée puisque la règle source est conservée sans formalité, registre ou délai supplémentaire.",
    "Le libre choix est l'avantage même du texte. Il reste ouvert aux futures victimes et n'est ni remplacé par un réseau imposé ni subordonné à une autorisation de la caisse.")

p=replace('L432-3',"Les praticiens et auxiliaires médicaux ne peuvent demander d'honoraires à la victime qui présente la feuille d'accident prévue à l'article L. 441-5, sauf le cas de dépassement de tarif dans les conditions prévues à l'article L. 162-35 et dans la mesure de ce dépassement.","Les praticiens et auxiliaires médicaux ne peuvent demander d'honoraires à la victime bénéficiaire du présent livre, sauf le cas de dépassement de tarif dans les conditions prévues à l'article L. 162-35 et dans la mesure de ce dépassement. Le bénéfice de cette interdiction n'est pas subordonné à la présentation de la feuille d'accident prévue à l'article L. 441-5 ; la qualité de bénéficiaire peut être établie par tout moyen.")
p=append(p,"La dispense de présentation de la feuille d'accident s'applique aux soins dispensés à compter de l'entrée en vigueur de la loi portant la présente modification, y compris au titre d'un accident antérieur. La feuille demeure utilisable et sa délivrance par l'employeur reste régie par l'article L. 441-5. Aucune attestation ou déclaration de remplacement n'est exigée de la victime. Les créances et recours relatifs aux soins antérieurs sont conservés.")
add('L432-3',
    "Réduction de fond : la protection contre la demande d'honoraires ne dépend plus de la présentation d'un support imposé. La qualité de bénéficiaire reste à établir, par tout moyen, sans attestation équivalente. Le premier alinéa est maintenu intégralement : tarifs maladie, majoration des produits non soumis au prix de L. 165-3 dans la limite des frais réels et application aux prothèses dentaires. Les dépassements légalement permis restent distincts.",
    "L. 441-5 et ses notes de sanction ont été lus dans le corpus : l'employeur doit toujours délivrer la feuille, dont la victime peut se servir ; cet article n'est pas réécrit dans ce lot. Coordonner ses modalités réglementaires d'utilisation pour qu'elles ne rétablissent pas la présentation obligatoire dans le champ de L. 432-3. L. 162-35, lu en entier, concerne la justification des dépassements et l'examen en commission ; ce contrôle est maintenu. Le gain porte sur l'exclusivité du document même lorsque les données ne sont pas déjà détenues, et non sur une nouvelle reprise du CRPA.",
    "La source entière conditionnait l'interdiction de demander des honoraires à la présentation de la feuille. Ce support cesse d'être une condition exclusive ; les plafonds et majorations favorables de remboursement demeurent.",
    "La preuve du droit et les dépassements autorisés demeurent. Les règles d'utilisation de la feuille hors lot restent à coordonner ; ni coût net global ni gratuité de tout dépassement ne sont établis.",
    "Aucune charge nouvelle n'est identifiée : la preuve par tout moyen élargit les supports admissibles et aucune déclaration, attestation ou connexion obligatoire ne remplace la feuille.",
    "La majoration des produits et prestations non tarifés par L. 165-3, sa limite aux frais réellement exposés et son extension à la cotation des prothèses dentaires sont conservées mot pour mot. Le tiers payant est rendu accessible sans feuille imposée, pour les soins futurs même liés à un accident ancien.",p,'material_reduction',[
        "Présentation obligatoire de la feuille d'accident comme condition exclusive de la protection contre la demande d'honoraires à la victime."
    ])
effect('L432-3','obligation_removed','atmp-tiers-payant-fin-feuille-exclusive',
    "Suppression du support obligatoire pour faire valoir l'interdiction d'avance d'honoraires.",
    "Victime tenue de présenter la feuille de L. 441-5 pour bénéficier de l'interdiction de demander les honoraires, sous réserve des dépassements permis.",
    "Qualité de bénéficiaire prouvable par tout moyen ; aucune feuille ni attestation de remplacement obligatoire ; mêmes dépassements permis.",'legal_duty','Victimes AT-MP et praticiens ou auxiliaires médicaux concernés.',
    "Soins dispensés après l'entrée en vigueur, même pour accident ancien ; créances et recours antérieurs préservés.",
    "Preuve du droit conservée, sans nouveau support imposé ; délivrance de la feuille par l'employeur non supprimée.",
    "à la victime qui présente la feuille d'accident prévue à l'article L. 441-5",
    "Le bénéfice de cette interdiction n'est pas subordonné à la présentation de la feuille d'accident prévue à l'article L. 441-5")

add('L432-4',
    "Maintien intégral nécessaire : l'autorisation visée est celle des établissements admis à dispenser des soins aux assurés sociaux, non un second agrément individuel de la victime. Elle protège la qualité et le financement des soins ; les tarifs communs évitent un régime AT-MP distinct. L'accès aux établissements des caisses et mutualistes demeure utile.",
    "L. 162-21 a été lu en entier dans le corpus : il pose l'autorisation de soigner les assurés sociaux et une faculté de vérification d'identité, sans créer une autorisation AT-MP supplémentaire. R. 432-2, également lu, conserve ses exceptions favorables d'urgence et circonstances exceptionnelles au plafonnement privé. Aucun de ces textes hors lot n'est modifié.",
    "La source ne crée pas de double procédure d'agrément propre aux AT-MP ; sa condition d'établissement et ses trois alinéas sont maintenus pour leur fonction de sécurité et d'accès aux soins.",
    "L'article ne réforme pas le droit général des autorisations sanitaires ni les tarifs hospitaliers ; aucun gain administratif ou budgétaire nouveau n'est revendiqué.",
    "Aucune charge nouvelle n'est identifiée : ni autorisation du patient ni justificatif supplémentaire ne sont ajoutés au régime existant.",
    "Les possibilités de soins dans les établissements publics, privés autorisés, mutualistes ou fondés par les caisses restent ouvertes aux futures victimes. Les exceptions réglementaires d'urgence ne sont pas supprimées.")

p='''<p>En cas d'interruption de travail ou de soins continus supérieurs à une durée fixée par décret, la caisse fait établir un protocole de soins lorsque l'état de santé de la victime le nécessite, à partir des éléments du suivi médical disponibles. La seule durée de l'interruption ou des soins ne peut justifier un examen spécial conjoint périodique par le médecin traitant et le médecin-conseil. Ce protocole, révisable notamment en fonction de l'état de santé de la victime et des avancées thérapeutiques, définit notamment les actes et prestations nécessités par le traitement de l'accident ou de la maladie professionnelle, compte tenu, le cas échéant, des recommandations établies par la Haute Autorité de santé. La signature du protocole par la victime ne peut être exigée pour l'établissement du protocole ni pour le service des prestations ; le consentement aux soins demeure requis dans les conditions de droit commun.</p>
<p>Le service de l'indemnité journalière est subordonné au respect par la victime de l'obligation :</p>
<p>1° De se soumettre aux traitements et mesures de toute nature prescrits par le médecin traitant, dans le respect du consentement aux soins ;</p>
<p>2° De se soumettre aux visites médicales et contrôles spéciaux organisés par la caisse ;</p>
<p>3° De s'abstenir d'une activité rémunérée qui n'est ni autorisée par le praticien ni permise par les dispositions applicables à la rééducation ou à la formation, ainsi que de toute activité incompatible avec les prescriptions mentionnées au 1°. Les activités non rémunérées compatibles avec ces prescriptions ne sont soumises à aucune autorisation préalable ;</p>
<p>4° D'accomplir les exercices ou travaux prescrits en vue de favoriser sa rééducation ou son reclassement professionnel.</p>
<p>En cas d'inobservation volontaire des obligations énumérées ci-dessus, la caisse peut suspendre, réduire ou supprimer le service de l'indemnité journalière pour la période correspondante. Cette décision ne peut interrompre la prise en charge des prestations en nature ni le paiement des soins aux praticiens ou établissements. Les contrôles portant sur le caractère professionnel, la nécessité médicale et la réalité des soins demeurent applicables.</p>
<p>La suppression de l'examen conjoint périodique systématique et de la signature obligatoire, la dispense d'autorisation des activités non rémunérées compatibles avec les prescriptions et le maintien des prestations en nature s'appliquent à compter de l'entrée en vigueur de la loi portant la présente rédaction, y compris aux soins, traitements et arrêts en cours. Aucun nouveau protocole ni renouvellement de signature ne sont exigés du seul fait de cette réforme. Les décisions antérieures de suspension des prestations en nature cessent de produire effet pour les soins dispensés à compter de cette date sur le seul fondement d'un manquement aux obligations du présent article. Les créances et recours relatifs aux périodes antérieures sont préservés, sous réserve de l'application de la loi répressive plus douce aux sanctions non définitives.</p>'''
add('L432-4-1',
    "Réduction de fond : retrait de l'examen conjoint périodique déclenché systématiquement par la durée et de la signature obligatoire du protocole. Le protocole reste possible lorsque médicalement nécessaire ; ses objets, les recommandations HAS et sa révision sont préservés. Les obligations 1° à 4° gardent leurs numéros ; le 3° est coordonné à la liberté des activités non rémunérées compatibles et aux actions de rééducation permises. Les sanctions ne peuvent plus couper les soins ou leur paiement ; elles sont limitées à l'indemnité journalière en cas de manquement volontaire.",
    "La note de 2019 règle l'entrée en vigueur des voies de contestation au plus tard le 1er janvier 2022, non celle de la présente réforme. Maintenir les contrôles médicaux justifiés, le consentement aux soins et les voies de recours de droit commun. Coordonner les textes d'exécution du protocole et des sanctions pour qu'ils ne rétablissent pas périodicité systématique, signature ou coupure des soins. Le 3° suit le même allègement que L. 323-6 proposé, dont le texte intégral est fourni comme cible de L. 433-1 : coordination facultative exposée ici, sans ajout aux reference_checks requis de cet article. Aucun double gain général de liberté d'activité n'est compté.",
    "Deux formalités systématiques sont retirées et la prise en charge des soins est dissociée des sanctions comportementales. Les éléments cliniques utiles et le contrôle des indemnités restent ; ce n'est pas une simple reformulation de la source.",
    "Les contrôles de réalité des soins, d'incapacité et de fraude subsistent ; les règlements d'exécution sont à coordonner. L'effet sur les dépenses de soins ou d'indemnités n'est pas chiffré.",
    "Aucune charge nouvelle autonome n'est identifiée : le protocole devient conditionnel au besoin médical, aucun rapport ou examen de remplacement n'est imposé. Les contrôles et le consentement étaient déjà requis par leur régime propre.",
    "Le protocole reste un instrument de prise en charge des actes nécessaires, sans signature bloquante. Les prestations en nature sont protégées même en cas de manquement, et les futures situations éligibles bénéficient de la réforme, y compris pendant un arrêt ancien.",p,'material_reduction',[
        "Examen spécial conjoint et périodique imposé systématiquement après une durée d'interruption de travail ou de soins continus.",
        "Signature du protocole par la victime imposée comme formalité obligatoire dans le suivi des soins prolongés.",
        "Possibilité de suspendre, réduire ou supprimer les prestations en nature en raison d'un manquement aux obligations de suivi de la victime.",
        "Possibilité de sanctionner une simple inobservation involontaire des obligations de suivi par une suspension, réduction ou suppression de l'indemnité journalière.",
        "Autorisation indistincte de toute activité, coordonnée à la dispense pour les activités non rémunérées médicalement compatibles."
    ])
effect('L432-4-1','obligation_removed','atmp-protocole-fin-formalites-systematiques',
    "Retrait de l'examen conjoint périodique automatique et de la signature imposée du protocole.",
    "Examen spécial conjoint périodique au-delà d'une durée réglementaire et protocole signé par la victime.",
    "Protocole seulement si nécessaire médicalement ; aucune périodicité automatique ni signature conditionnant les prestations.",'legal_duty','Victimes en interruption de travail ou soins continus prolongés et caisses.',
    "Après entrée en vigueur, y compris suivi en cours ; aucun nouveau protocole pour la seule réforme.",
    "Suivi médical existant réutilisé ; aucun nouveau rapport ou déclaration de remplacement.",
    "Ce protocole est signé par la victime.","La signature du protocole par la victime ne peut être exigée pour l'établissement du protocole ni pour le service des prestations")
effect('L432-4-1','relief_extended','atmp-soins-fin-sanctions-de-suivi',
    "Protection des soins contre les sanctions liées aux obligations de suivi et limitation des sanctions d'indemnité aux manquements volontaires et à leur période.",
    "Possibilité de suspendre, réduire ou supprimer le service des prestations pour inobservation, sans distinction explicite entre manquement volontaire ou involontaire, ni entre soins et indemnités.",
    "Seule l'indemnité journalière peut être affectée pour la période de manquement volontaire ; soins et paiement des professionnels maintenus.",'regime','Victimes AT-MP soumises au suivi prolongé, professionnels et établissements.',
    "Soins après entrée en vigueur, même pour suspension ancienne ; pas de restitution générale des périodes antérieures.",
    "Contrôles médicaux et de réalité des soins conservés, sans formalité nouvelle.",
    "En cas d'inobservation des obligations énumérées ci-dessus, la caisse peut suspendre, réduire ou supprimer le service des prestations.",
    "En cas d'inobservation volontaire des obligations énumérées ci-dessus, la caisse peut suspendre, réduire ou supprimer le service de l'indemnité journalière pour la période correspondante. Cette décision ne peut interrompre la prise en charge des prestations en nature ni le paiement des soins aux praticiens ou établissements.")
effect('L432-4-1','coordination','arret-travail-activites-non-remunerees',
    "Coordination du régime spécial de suivi avec la dispense d'autorisation des activités non rémunérées compatibles déjà proposée à L. 323-6.",
    "Abstention de toute activité non autorisée dans le 3°.",
    "Activités non rémunérées compatibles sans autorisation ; activités rémunérées et prescriptions médicales gardent leur régime.",'legal_duty','Victimes AT-MP en suivi prolongé.',
    "Comportements après entrée en vigueur même pendant un arrêt antérieur ; sanctions non définitives sous réserve de la loi plus douce.",
    "Aucune déclaration de remplacement ; ce renvoi de cohérence n'est pas une seconde mesure générale supprimée.",
    "3° De s'abstenir de toute activité non autorisée ;",
    "Les activités non rémunérées compatibles avec ces prescriptions ne sont soumises à aucune autorisation préalable")

add('L432-6',
    "Maintien intégral du droit au traitement spécial de réadaptation fonctionnelle. Cette disposition attributive ne contient ni déclaration, ni prélèvement, ni autorisation préalable propre à supprimer ; sa disparition retirerait le fondement d'une prestation utile.",
    "R. 432-6 et R. 432-7 ont été lus en entier dans le corpus : ils organisent avis, décision et réponse sous un mois, distincts du droit posé ici. Ils ne sont pas modifiés dans ce lot ; leur examen administratif ne doit pas être présenté comme déjà achevé par le maintien de L. 432-6.",
    "La règle source est intégralement nécessaire à l'accès à la réadaptation ; aucun effet nouveau de réduction de charge n'est attribué à ce maintien.",
    "Le présent maintien ne valide ni ne réforme les circuits réglementaires de décision qui nécessitent leur propre examen dans leur lot.",
    "Aucune charge nouvelle n'est identifiée : aucun nouveau dossier, justificatif ou calendrier n'est créé pour accéder à ce droit.",
    "Le droit au traitement spécial de réadaptation fonctionnelle reste ouvert à toutes les futures victimes éligibles et aux prises en charge en cours ; il n'est pas cantonné aux contrats antérieurs.")

add('L432-7',
    "Maintien intégral nécessaire : accès aux établissements de réadaptation et indemnité journalière pendant toute la période du traitement spécial. L'autorisation porte sur l'établissement, par renvoi au régime général de L. 432-4, sans nouvel agrément de la victime. La suppression de cet article retirerait des garanties plutôt qu'une charge inutile.",
    "L'article précédent désigne L. 432-6. Le premier alinéa de L. 432-4, conservé dans ce lot, est bien celui de l'autorisation de l'établissement. Le renvoi à L. 433-1 fournit le régime de l'indemnité et bénéficie de son allègement pour le travail aménagé ; il ne soumet pas la durée du traitement à un terme de contrat. Le maximum de L. 433-1 et ses transitions doivent être lus avec la garantie spéciale de toute la période de réadaptation ; aucune extinction additionnelle n'est introduite.",
    "La source garantit le maintien de revenu pendant la réadaptation et un accès à des établissements habilités. Aucun doublon autonome d'autorisation n'est identifié dans cet article.",
    "Les conditions réglementaires d'admission et les versions futures de L. 433-1 conservent leur champ ; aucune modification globale des durées d'indemnisation n'est revendiquée.",
    "Aucune charge nouvelle n'est identifiée : la règle n'est pas remplacée et aucune durée minimale d'emploi ou pièce de suivi supplémentaire n'est ajoutée.",
    "L'indemnité journalière pendant toute la réadaptation et le choix entre établissements publics et autorisés sont maintenus pour les situations futures et en cours ; aucun seuil d'un an n'est importé de l'indemnité de rupture.")

p='''<p>Le bénéficiaire des dispositions de l'article L. 432-7 est tenu :</p>
<p>1°) de se soumettre aux traitements et mesures de toute nature prescrits dans les conditions prévues au présent code ou par les autorités sanitaires compétentes, dans le respect du consentement aux soins ;</p>
<p>2°) de se soumettre aux visites médicales et contrôles organisés par la caisse ;</p>
<p>3°) de s'abstenir d'une activité rémunérée qui n'est ni autorisée par le praticien ni permise par les dispositions applicables à la rééducation ou à la formation, ainsi que de toute activité incompatible avec les prescriptions mentionnées au 1°. Les activités non rémunérées compatibles avec ces prescriptions ne sont soumises à aucune autorisation préalable ;</p>
<p>4°) d'accomplir les exercices ou travaux prescrits en vue de favoriser sa rééducation ou son reclassement professionnel, sans préjudice des dispositions des articles L. 432-9 et L. 432-10.</p>
<p>En cas d'inobservation volontaire des obligations ci-dessus indiquées, la caisse peut suspendre le service de l'indemnité ou en réduire le montant pour la période correspondante, sauf recours du bénéficiaire devant les organismes du contentieux de la sécurité sociale. Cette décision ne peut interrompre la prise en charge des prestations en nature ni le paiement des soins aux praticiens ou établissements. Les contrôles portant sur le caractère professionnel, la nécessité médicale et la réalité des soins demeurent applicables.</p>
<p>La dispense d'autorisation des activités non rémunérées compatibles avec les prescriptions et le maintien des prestations en nature s'appliquent à compter de l'entrée en vigueur de la loi portant la présente rédaction, y compris aux traitements et arrêts en cours. Les décisions antérieures de cessation du paiement des frais cessent de produire effet pour les soins dispensés à compter de cette date sur le seul fondement d'un manquement aux obligations du présent article. Les créances et recours relatifs aux périodes antérieures sont préservés, sous réserve de l'application de la loi répressive plus douce aux sanctions non définitives.</p>'''
add('L432-8',
    "Coordination de la protection des soins portée à L. 432-4-1 : suppression de la cessation du paiement des frais à raison des manquements aux obligations de réadaptation ; les indemnités restent contrôlables pour un manquement volontaire. Le 3° coordonne les activités non rémunérées médicalement compatibles et les actions de formation autorisées par leur régime. Les 1°, 2° et 4°, leurs numéros, la réserve de L. 432-9 et L. 432-10 et le recours sont conservés.",
    "Même mesure de protection des soins que L. 432-4-1, sans compter deux fois une abolition générale. Le bénéfice de L. 432-7 demeure celui de la réadaptation, et L. 432-9 conserve gratuité, maintien de revenu et supplément. Les exercices prescrits ne deviennent ni un nouveau contrat à terme ni une autorisation de facturer les soins à la victime. La coordination d'activité suit L. 323-6 fourni dans le contexte de L. 433-1, sans cible supplémentaire dans reference_checks ; les sanctions définitives et créances anciennes ne sont pas annulées indistinctement.",
    "La source faisait cesser l'obligation de la caisse de payer tous frais aux professionnels ; cette exclusion est retirée pour coordonner le régime de réadaptation avec la protection de L. 432-4-1. Les deux effets sont des coordinations des mesures communes, sans seconde réduction comptée. Les contrôles et l'indemnité journalière restent distincts des soins nécessaires.",
    "Les sanctions propres à d'autres fondements, la fraude et la réalité médicale ne sont pas abolies ; les conséquences budgétaires de la continuité des soins ne sont pas chiffrées.",
    "Aucune charge nouvelle n'est identifiée : pas de justificatif de remplacement ni d'autorisation pour les activités non rémunérées compatibles ; les contrôles médicaux existants subsistent.",
    "L'accès effectif à la réadaptation et le paiement de ses frais sont protégés, sans retrait de l'indemnité, des suppléments de L. 432-9 ni des recours. Ces garanties valent pour les soins futurs même si le traitement ou le manquement est ancien.",p,'coordination_only',[
        "Cessation du paiement par la caisse des frais de toute nature aux praticiens et établissements à raison d'un manquement aux obligations de réadaptation.",
        "Possibilité de sanctionner une simple inobservation involontaire des obligations de réadaptation par la suspension de l'indemnité ou la réduction de son montant.",
        "Autorisation indistincte de toute activité, coordonnée à la dispense des activités non rémunérées compatibles avec les prescriptions."
    ])
effect('L432-8','coordination','atmp-soins-fin-sanctions-de-suivi',
    "Coordination de la protection des soins et de la limitation des sanctions d'indemnité aux manquements volontaires dans le régime spécial de réadaptation.",
    "La caisse peut suspendre ou réduire l'indemnité en cas d'inobservation des obligations, sans condition explicite de volonté, et cesse d'être tenue de payer les frais de toute nature aux professionnels.",
    "Le paiement des soins demeure ; seule l'indemnité peut être suspendue ou réduite pour le manquement volontaire correspondant.",'regime','Victimes en réadaptation, praticiens et établissements concernés.',
    "Soins futurs et traitements en cours ; effets futurs des anciennes coupures supprimés, créances anciennes et recours préservés.",
    "Pas de contrôle ou déclaration supplémentaire ; même famille de protection des soins que L. 432-4-1.",
    "En cas d'inobservation des obligations ci-dessus indiquées, la caisse peut suspendre le service de l'indemnité ou en réduire le montant, sauf recours du bénéficiaire devant les organismes du contentieux de la sécurité sociale. Dans le même cas, elle cesse d'être tenue au paiement des frais de toute nature à l'égard des praticiens ou établissements intéressés.",
    "En cas d'inobservation volontaire des obligations ci-dessus indiquées, la caisse peut suspendre le service de l'indemnité ou en réduire le montant pour la période correspondante, sauf recours du bénéficiaire devant les organismes du contentieux de la sécurité sociale. Cette décision ne peut interrompre la prise en charge des prestations en nature ni le paiement des soins aux praticiens ou établissements.")
effect('L432-8','coordination','arret-travail-activites-non-remunerees',
    "Coordination de l'interdiction d'activité du régime de réadaptation avec la dispense déjà proposée à L. 323-6.",
    "Toute activité non autorisée est interdite sans distinction dans le 3°.",
    "Activités non rémunérées compatibles sans autorisation ; prescriptions et activités rémunérées demeurent encadrées.",'legal_duty','Victimes bénéficiant du traitement spécial de réadaptation.',
    "Comportements futurs y compris pendant traitement ancien, sous réserve des sanctions non définitives plus douces.",
    "Aucune formalité équivalente ; cette coordination n'est pas comptée comme une nouvelle suppression générale.",
    "3°) de s'abstenir de toute activité non autorisée ;",
    "Les activités non rémunérées compatibles avec ces prescriptions ne sont soumises à aucune autorisation préalable")

p=replace('L432-9','Elle subit à cet effet un examen psychotechnique préalable.',"Aucun examen psychotechnique préalable systématique ne conditionne l'exercice de ce droit.")
p=append(p,"La suppression de l'examen psychotechnique préalable systématique s'applique aux admissions et placements non encore décidés à l'entrée en vigueur de la loi portant la présente modification ainsi qu'aux demandes ultérieures, sans nouveau dossier du seul fait de cette suppression. Elle ne remet en cause ni les admissions et placements déjà accordés, ni les indemnités, suppléments et rentes acquis. Les conditions d'aptitude requises pour l'exercice de la profession choisie demeurent applicables.")
add('L432-9',
    "Réduction de fond : l'examen psychotechnique préalable systématique est retiré sans dossier, agrément ou test obligatoire équivalent. Les conditions d'aptitude au métier demeurent. Les trois alinéas conservent admission gratuite ou placement chez un employeur, libre choix de profession, droit même sans réadaptation antérieure, maintien intégral de l'indemnité ou de la rente, supplément au salaire antérieur ou au SMIC plus élevé et absence de réduction de rente du fait du nouveau métier.",
    "Coordonner les textes d'exécution de la rééducation qui imposeraient encore le test automatique ; un examen médical individualisé utile à la sécurité n'est pas aboli par cette suppression. La durée d'un placement ou d'une formation n'est pas un terme d'emploi : si une embauche privée nouvelle est conclue, L. 1221-2 proposé s'applique ; les contrats anciens gardent leurs droits. L. 433-1 est le renvoi de période d'indemnité, pas une condition d'ancienneté ou de rupture. L'incohérence rédactionnelle préexistante de la source (« celle-ci reçoit » après « mutilé ») n'est pas corrigée silencieusement dans l'alinéa financier maintenu.",
    "Une étape préalable universelle est effectivement supprimée, les critères d'aptitude restant ciblés sur la profession. Aucun avantage de rémunération ou de gratuité de la source entière n'est retiré.",
    "Les examens de sécurité propres au métier et les conventions de formation restent à leur champ ; aucune économie nationale ou réduction des cotisations n'est déduite de ce seul test retiré.",
    "Aucune charge nouvelle n'est identifiée : aucune déclaration, nouveau test ou pièce ne remplace l'examen systématique ; les conditions professionnelles existantes restent identiques.",
    "La gratuité, le choix de profession, le maintien intégral de l'indemnité ou de la rente, le supplément jusqu'au salaire antérieur ou au SMIC plus élevé, et la non-réduction de rente sont conservés pour les situations futures éligibles, pas seulement pour les anciens contrats.",p,'material_reduction',[
        "Examen psychotechnique préalable imposé systématiquement à toute victime sollicitant une rééducation professionnelle ou un placement."
    ])
effect('L432-9','obligation_removed','atmp-reeducation-fin-test-systematique',
    "Suppression du test psychotechnique préalable universel.",
    "Examen psychotechnique préalable obligatoire avant exercice du droit à rééducation ou placement.",
    "Pas d'examen psychotechnique systématique conditionnant le droit ; aptitude professionnelle, gratuité et garanties de revenu maintenues.",'legal_duty',"Victimes devenues inaptes à leur profession ou ayant besoin d'une nouvelle adaptation.",
    "Admissions et placements non encore décidés à l'entrée en vigueur et demandes futures ; droits déjà accordés conservés.",
    "Aucun test ni dossier de remplacement ; règles d'aptitude propres à la profession inchangées.",
    "Elle subit à cet effet un examen psychotechnique préalable.",
    "Aucun examen psychotechnique préalable systématique ne conditionne l'exercice de ce droit.")

add('L432-10',
    "Maintien intégral nécessaire : droit au reclassement professionnel et habilitation fixant la participation financière de la caisse aux frais. Aucun agrément, dépôt supplémentaire ou minimum d'emploi n'est imposé ici ; supprimer l'habilitation fragiliserait le financement favorable de la rééducation.",
    "L. 432-9 est maintenu dans son champ financier et allégé du test systématique dans ce lot. Le décret pris sur le présent article ne peut réintroduire ce préalable. Les obligations de reclassement de l'employeur en cas d'inaptitude ont une base distincte, non effacée par le préavis individuel de quinze jours.",
    "Maintien de la source entière, sans formalité autonome redondante identifiée. Le financement du reclassement et de la rééducation garde une base légale.",
    "Les modalités réglementaires et les obligations patronales d'inaptitude relèvent de leurs textes propres ; aucun gain net ni montant de financement n'est établi ici.",
    "Aucune charge nouvelle n'est identifiée : ni nouvelle autorisation ni nouvelle demande n'est ajoutée au droit au reclassement.",
    "Le droit au reclassement et la participation de la caisse aux frais restent ouverts aux futures victimes éligibles, y compris sous contrat unique ; aucune ancienneté ni durée d'emploi n'est introduite.")

add('L432-11',
    "Maintien intégral de la validation de la rééducation professionnelle pour la pension vieillesse. C'est un avantage de solidarité et non une cotisation accessoire ou une formalité redondante ; son retrait diminuerait des droits sociaux sans baisse de prélèvement démontrée.",
    "Ne pas appliquer à cette validation le gel de revalorisation de certaines pensions ni transformer cette période en cotisation nouvelle de capitalisation. La transition du projet de retraite protège les droits constitués ; les règles futures de raccordement devront préserver ce fondement de solidarité.",
    "Aucun changement normatif : la période de rééducation conserve sa validation pour les droits à pension ; aucun transfert de financement n'est opéré dans cet article.",
    "La validation ne détermine pas à elle seule tous les paramètres de liquidation ou de raccordement entre régimes ; aucun rendement ou montant de pension futur n'est inventé.",
    "Aucune charge nouvelle n'est identifiée : aucun compte, registre ou justificatif supplémentaire n'est créé pour cette validation.",
    "La validation est conservée pour les périodes futures de rééducation éligibles ainsi que pour les droits acquis. Elle n'est pas réservée aux contrats anciens ni neutralisée par le seuil d'un an de l'indemnité ordinaire de rupture.")

add('L432-12',
    "Maintien intégral de l'abondement du CPF pour reconversion à raison d'une incapacité permanente au moins égale au seuil réglementaire. Ce soutien est distinct de la contribution CPF-CDD de 1 % supprimée ailleurs ; sa suppression retirerait une aide sans démontrer la disparition de son objet.",
    "Le renvoi à L. 6323-1 désigne le CPF et non la durée du contrat. Le seuil d'incapacité est une condition de l'aide médicale et sociale, pas une ancienneté d'un an. La note d'entrée en vigueur au plus tard le 1er janvier 2019 est historique ; elle n'est pas une date de réforme. Maintenir l'accès des futures situations éligibles sous contrat unique.",
    "L'abondement et son seuil d'incapacité sont maintenus sans nouvelle formalité ; aucune diminution de cotisation n'est comptée dans ce maintien.",
    "Le montant et les modalités réglementaires de l'abondement ne sont pas redéfinis ; aucune recette de compensation ou budget national n'est estimé.",
    "Aucune charge nouvelle n'est identifiée : aucun dossier ou contrôle supplémentaire n'est ajouté au dispositif d'abondement existant.",
    "L'abondement de reconversion demeure ouvert aux victimes futures remplissant le taux d'incapacité, quelle que soit la forme passée de leur contrat. La suppression du financement CPF-CDD ailleurs ne ferme pas cette aide.")

p=replace('L433-1',"si ce travail est reconnu par le médecin-conseil de la caisse primaire comme de nature à favoriser la guérison ou la consolidation de la blessure.","lorsque ce travail est de nature à favoriser la guérison ou la consolidation de la blessure. Le versement n'est soumis ni à une reconnaissance préalable du médecin-conseil ni à une autorisation distincte de la caisse. Les contrôles médicaux de droit commun demeurent applicables.")
p=append(p,
    "La dispense de reconnaissance et d'autorisation préalables prévue au quatrième alinéa s'applique aux périodes de travail aménagé ou à temps partiel accomplies à compter de l'entrée en vigueur de la loi portant la présente modification, y compris pendant un arrêt antérieur ou en exécution d'un certificat antérieur. Aucun nouveau certificat ni renouvellement d'autorisation n'est exigé au seul motif de cette dispense. Les créances et recours relatifs aux périodes antérieures sont préservés.",
    "Pour les contrats de travail uniques conclus à compter de l'entrée en vigueur de la loi instituant ces contrats, le licenciement mentionné au sixième alinéa s'entend de la fin effective du contrat à l'expiration du préavis individuel applicable, sans préjudice des autorisations, procédures collectives et protections spéciales dont dépend la rupture. Ce préavis ne réduit ni le délai mentionné à l'article L. 1226-11 du code du travail ni l'obligation de reprise du salaire qui en résulte. Les autres conditions du sixième alinéa, notamment l'absence de rémunération liée à l'activité salariée et l'imputation de la rente, demeurent applicables. Les contrats antérieurs conservent leur régime de rupture.",
    "Les présentes modifications ne changent pas le champ temporel des autres dispositions du présent article, notamment l'application aux victimes dont le sinistre est intervenu à compter du 1er janvier 2027 des dispositions issues de l'article 81 de la loi n° 2025-1403 du 30 décembre 2025.")
add('L433-1',
    "Réduction de fond au quatrième alinéa : le certificat du médecin traitant autorisant le travail aménagé ou à temps partiel suffit lorsque celui-ci est de nature à favoriser la guérison ou la consolidation sans seconde reconnaissance préalable du médecin-conseil ou autorisation distincte de la caisse. Les contrôles médicaux restent. Les huit alinéas sources sont conservés à leur place, avec leurs autres conditions et exceptions. Une coordination de la cessation d'indemnité avec la fin effective du nouveau contrat évite de confondre notification, préavis individuel et délai d'inaptitude.",
    "L. 323-1 1° fournit le plancher du maximum d'indemnisation, non une nouvelle carence AT-MP. L. 323-3-1 proposé retire son avis/accord préalable propre aux actions de formation et de rééducation ; le renvoi du cinquième alinéa n'en rétablit aucun. L. 323-6 proposé conserve contrôles, adresse et prescriptions avec dispenses d'activité et de double déclaration. R. 433-15, lu en entier, devra être coordonné pour supprimer la reconnaissance préalable sans retirer le certificat utile, les éléments de salaire nécessaires au calcul, le contradictoire et les recours. L. 1226-11 et L. 1226-14 ont été lus hors cibles dans le corpus : un mois pour la reprise du salaire, indemnité spéciale sans seuil, et nouveau préavis payé non exécuté restent distincts. Les notes de 2025 et le champ des sinistres à compter du 1er janvier 2027 sont expressément préservés, sans date de promulgation inventée. La limite de trois jours attachée au renvoi de télémédecine demeure dans son champ de contrôle d'une prescription régulière.",
    "Suppression d'une validation préalable cumulée pour le travail thérapeutique ; maintien du certificat, des contrôles et de l'absence de maximum pour cette indemnité. La coordination de fin effective du contrat n'est pas comptée comme une nouvelle baisse du barème de rupture.",
    "Les règles de calcul, le maximum ordinaire, la télémédecine et leurs transitions restent distincts. R. 433-15 et les coordinations sociales de la période de préavis restent à adapter ; le coût net n'est pas établi.",
    "Aucune charge nouvelle n'est identifiée : le certificat autorisant le travail était déjà requis et aucun contenu documentaire supplémentaire, second dépôt ou renouvellement n'est imposé. L'utilité médicale reste une condition déjà présente, contrôlable par les contrôles de droit commun.",
    "Salaire du jour de l'accident, indemnité sans carence y compris dimanches et jours fériés, rechute/aggravation, absence de maximum en travail thérapeutique, accès aux actions de rééducation et indemnité temporaire d'inaptitude sont conservés. Le seuil d'un an de l'indemnité ordinaire n'affecte aucun de ces droits ni l'indemnité spéciale ; les accidents anciens restent couverts selon leur régime.",p,'material_reduction',[
        "Reconnaissance préalable par le médecin-conseil de l'utilité du travail aménagé ou à temps partiel, cumulée avec le certificat du médecin traitant."
    ])
effect('L433-1','authorization_removed','atmp-travail-therapeutique-fin-double-accord',
    "Le certificat médical utile ne requiert plus une seconde reconnaissance préalable.",
    "Certificat du médecin traitant et reconnaissance par le médecin-conseil du caractère favorable à la guérison ou à la consolidation.",
    "Certificat autorisant le travail et condition d'utilité médicale maintenus ; pas de reconnaissance ou autorisation préalable distincte, contrôles conservés.",'legal_duty','Victimes AT-MP reprenant un travail aménagé ou à temps partiel thérapeutique.',
    "Périodes après entrée en vigueur, même couvertes par ancien arrêt ou certificat ; droits et recours antérieurs préservés.",
    "Aucune déclaration de remplacement ni certificat à renouveler du seul fait de la réforme.",
    "si ce travail est reconnu par le médecin-conseil de la caisse primaire comme de nature à favoriser la guérison ou la consolidation de la blessure.",
    "Le versement n'est soumis ni à une reconnaissance préalable du médecin-conseil ni à une autorisation distincte de la caisse.")
effect('L433-1','coordination','contrat-unique-inaptitude-preavis',
    "Précision de la fin d'indemnisation dans le nouveau contrat au regard du préavis et du salaire d'inaptitude.",
    "L'indemnité cesse lorsque l'employeur reclasse le salarié ou le licencie ; le texte ne définit pas la date de fin du nouveau contrat.",
    "Pour le contrat unique, le licenciement désigne la fin effective avec préavis ; absence de rémunération, imputation de rente et délai d'un mois restent.",'regime','Salariés inaptes couverts par le contrat unique nouveau et leur caisse.',
    "Contrats conclus après l'entrée en vigueur du contrat unique ; contrats anciens gardant leur régime, pas de cumul avec salaire.",
    "Pas de seconde indemnité de préavis créée ; coordination avec les obligations de rupture déjà décidées ailleurs.",
    "Le versement de l'indemnité cesse dès que l'employeur procède au reclassement dans l'entreprise du salarié inapte ou le licencie.",
    "le licenciement mentionné au sixième alinéa s'entend de la fin effective du contrat à l'expiration du préavis individuel applicable, sans préjudice des autorisations, procédures collectives et protections spéciales dont dépend la rupture.")

add('L433-2',
    "Maintien intégral nécessaire : assiette salariale, plafond rattaché à L. 241-3, majoration de l'indemnité et possibilité de révision en cas d'augmentation générale des salaires. Ces paramètres financent et définissent une prestation de remplacement, sans contribution accessoire ni déclaration autonome. Aucun taux nouveau ni délai de majoration arbitraire n'est créé.",
    "L. 241-3 fourni conserve son plafond annuel dans le I proposé ; le transfert éventuel de cotisations vers un compte capitalisé n'est pas une réduction de ce plafond ni de l'indemnité AT-MP. R. 433-3 a été lu : majoration à 80 % à partir du vingt-neuvième jour ; ce délai est une modulation de prestation selon sa durée, non une carence générale. Sa suppression n'est pas décidée ici par un taux intermédiaire inventé. Ne pas appliquer aux indemnités le gel proposé de certaines pensions.",
    "La source entière et ses mécanismes favorables d'augmentation sont maintenus ; aucune baisse de prélèvement ou nouveau transfert de financement n'est réalisé par cet article.",
    "Les fractions, pourcentages, durées réglementaires et montants individuels restent régis par leurs textes ; aucune économie ou hausse de revenu uniforme n'est chiffrée.",
    "Aucune charge nouvelle n'est identifiée : ni déclaration ni seuil d'ancienneté ni donnée supplémentaire ne sont ajoutés aux paramètres de calcul.",
    "La majoration après la durée réglementaire et la révision en cas de hausse générale des salaires restent possibles pour les futures victimes. Le plafond vieillesse est maintenu comme référence de calcul, sans diminuer la prestation en raison d'un transfert de cotisations.")

p="<p>L'indemnité journalière n'est cessible et saisissable que dans les limites fixées par les articles L. 3252-2 et L. 3252-3 du code du travail en ce qui concerne le salaire.</p>\n<p>Cette coordination de référence s'applique sans modifier les fractions protégées, les correctifs, les exceptions ni les règles d'application dans le temps propres à la saisie et à la cession des rémunérations. Les droits acquis et recours relatifs aux mesures antérieures sont conservés.</p>"
add('L433-3',
    "Coordination nécessaire, sans allègement nouveau : remplacement du renvoi ancien à L. 145-1 du code du travail par les dispositions actuelles sur les proportions et seuils et sur l'assiette et la fraction insaisissable, L. 3252-2 et L. 3252-3. Le caractère partiellement insaisissable et incessible de l'indemnité reste intégralement protégé.",
    "Nouveaux renvois hors reference-targets.json, signalés expressément : L. 3252-2 (LEGIARTI000006902878) et L. 3252-3 (LEGIARTI000033812428), lus en entier avec notes dans travail.json. L. 3252-1 et L. 3252-5 ont aussi été lus : champ toutes formes de contrat et exception des pensions alimentaires avec minimum laissé au débiteur. L. 3252-2 réserve déjà L. 3252-5 ; cette exception n'est pas effacée. Le corpus ne fournit pas l'ancienne version entière L. 145-1 : aucune identité mot pour mot avec ce texte historique n'est affirmée. Le renvoi contemporain, ses garanties et cette limite documentaire sont explicites, sans changer silencieusement le barème.",
    "Le renvoi ordinal périmé est actualisé ; aucune fraction saisissable, protection du débiteur ou exception alimentaire n'est modifiée par la proposition.",
    "L'ancienne version entière de L. 145-1 n'est pas dans le corpus local consulté ; la concordance historique détaillée reste à documenter. Aucun nouveau gain administratif n'est compté.",
    "Aucune charge nouvelle n'est identifiée : le nouveau texte ne crée ni procédure, ni donnée, ni délai supplémentaire et conserve les règles autonomes de saisie.",
    "La limitation des saisies et cessions, le minimum protégé et les correctifs pour personnes à charge restent applicables aux futures indemnités ; l'actualisation ne convertit pas l'indemnité en salaire pour les autres régimes.",p,'coordination_only')
effect('L433-3','coordination','atmp-indemnites-renvoi-saisie-remunerations',
    "Actualisation du renvoi de protection de l'indemnité journalière contre saisies et cessions.",
    "Renvoi à l'ancien L. 145-1 du code du travail pour les limites applicables au salaire.",
    "Renvoi aux limites et assiette de L. 3252-2 et L. 3252-3, sans modification autonome de ces limites.",'regime',"Bénéficiaires d'indemnités journalières AT-MP et leurs créanciers.",
    "Règles propres aux mesures et périodes conservées ; pas de réouverture de procédure ou de modification des droits acquis.",
    "Aucune nouvelle formalité ni fraction de saisie ajoutée.",
    "dans les limites fixées par l'article L. 145-1 du code du travail",
    "dans les limites fixées par les articles L. 3252-2 et L. 3252-3 du code du travail")

add('L433-4',
    "Maintien intégral de ce régime protecteur propre aux personnes détenues : maintien des indemnités liquidées avant détention, droit dès le lendemain pour accident en emploi pénitentiaire ou formation, rechute et règles de mise en paiement. Le contrat d'emploi pénitentiaire n'est pas assimilé à une embauche privée ordinaire. La reconnaissance de l'origine professionnelle n'est pas un agrément superflu de la victime.",
    "Les trois paragraphes contenus dans le p source sont conservés sans déplacement. Le renvoi à l'article 723 du code de procédure pénale relève d'un code extérieur, non fourni dans les cibles et non réécrit ; il ne peut être remplacé par le préavis de quinze jours. La note de l'ordonnance de 2022 fixe l'entrée en vigueur au plus tard le 1er décembre 2024 ; la version assignée a une borne au 1er janvier 2029. Ne pas étendre à ce régime spécial le maximum de L. 433-1 ou les règles du contrat unique sans texte exprès. L'origine professionnelle, la date de paiement et le droit dès le premier jour restent des questions distinctes.",
    "Aucun nouveau corps n'est nécessaire pour préserver le maintien des prestations en détention. Les règles spéciales de paiement ne sont pas identifiées comme un doublon d'autorisation privée dans la source.",
    "L'article 723 et les versions postérieures au 1er janvier 2029 ne sont pas fournis dans ce lot ; aucune refonte du droit pénitentiaire ni validation de son calendrier extérieur n'est revendiquée.",
    "Aucune charge nouvelle n'est identifiée : aucun dossier, justificatif, contrôle ou délai nouveau n'est ajouté aux conditions spéciales existantes.",
    "Le maintien des indemnités antérieures à la détention et les droits nés d'accidents en emploi pénitentiaire ou en formation sont préservés pour les futurs bénéficiaires. Les jours non ouvrables, rechutes et aggravations restent couverts dans le champ exact du texte.")

p=replace('L434-1',"Cette indemnité est versée lorsque la décision est devenue définitive.","Cette indemnité est versée dès la notification de la décision qui l'attribue, sans attendre que cette décision soit devenue définitive. L'exercice d'un recours ne suspend pas ce versement.")
p=append(p,"La suppression de l'attente du caractère définitif de la décision s'applique aux indemnités relevant du présent article qui n'ont pas encore été versées à l'entrée en vigueur de la loi portant la présente modification ainsi qu'aux indemnités attribuées ultérieurement dans son champ. Elle ne modifie ni le montant dû, ni la revalorisation ou la révision, ni les règles de prescription, de recours et de récupération des indus applicables. Aucun second versement n'est dû au titre d'une indemnité déjà payée. Les champs respectifs des versions successives de la législation sur l'indemnisation de l'incapacité permanente sont conservés.")
add('L434-1',
    "Allègement de calendrier réel : suppression de l'attente d'une décision définitive avant le paiement du capital attribué ; la notification suffit et le recours n'est pas suspensif du paiement. Le montant selon incapacité, le barème, sa revalorisation annuelle au 1er avril, la révision en cas d'aggravation sous le seuil et l'incessibilité/insaisissabilité sont intégralement maintenus. Ce n'est ni une baisse de taux ni une hausse du capital.",
    "La version assignée est bornée au 1er novembre 2026. La proposition règle les indemnités relevant de cette version sans remettre en vigueur son champ pour les sinistres qu'une version nouvelle régit ; la nouvelle rédaction postérieure et son article L. 434-1 A ne sont pas fournis comme cibles complètes. Coordonner les modalités réglementaires de paiement pour retirer l'attente du caractère définitif, sans créer de double paiement. Les recours, prescriptions et indus gardent leurs bases propres. Le gel proposé de certaines pensions ne s'applique pas à cette revalorisation de capital.",
    "Le capital est payable avant l'issue définitive des recours, à montant et barème identiques. Le seul effet démontré est un accès plus rapide à une somme déjà attribuée.",
    "Aucun délai chiffré de traitement ni montant d'avance national n'est estimé ; la législation future d'indemnisation conserve son champ et les indus restent récupérables selon leur régime.",
    "Aucune charge nouvelle autonome n'est identifiée : pas de demande d'avance, garantie ou attestation nouvelle ; l'organisme exécute le paiement déjà dû plus tôt et conserve le traitement des recours et indus.",
    "Le capital, sa révision, sa revalorisation au 1er avril et sa protection contre saisie ou cession demeurent pour toutes situations relevant de la version applicable. Le paiement anticipé n'est pas conditionné à une renonciation au recours.",p,'material_reduction',[
        "Attente du caractère définitif de la décision d'attribution comme condition préalable au versement de l'indemnité en capital."
    ])
effect('L434-1','deadline_reduced','atmp-capital-versement-sans-attente-definitive',
    "Fin du différé légal de versement du capital : paiement avancé au bénéficiaire, sans diminution de prélèvement ni changement du montant dû.",
    "Capital versé seulement lorsque la décision est définitive ; durée d'attente variable selon les recours.",
    "Capital versé dès notification de la décision attributive, sans attendre l'issue définitive ; montant et barème inchangés.",'other',"Victimes titulaires d'une indemnité en capital relevant du champ temporel de cet article.",
    "Sommes non encore versées à l'entrée en vigueur et attributions ultérieures dans le même champ ; aucun second paiement.",
    "Pas de dossier d'avance ni garantie ; règles d'indus et de recours préservées. La condition d'attente est supprimée : il ne s'agit ni d'un report de dette du cotisant ni d'une réduction de montant.",
    "Cette indemnité est versée lorsque la décision est devenue définitive.",
    "Cette indemnité est versée dès la notification de la décision qui l'attribue, sans attendre que cette décision soit devenue définitive.")

add('L434-2',
    "Maintien intégral nécessaire des six alinéas d'indemnisation permanente : évaluation individualisée, rente, prestation pour tierce personne revalorisée, cumul des taux d'accidents successifs avec choix capital/rente, plancher d'invalidité et information sur la retraite anticipée. La demande dans le régime d'accidents successifs matérialise un choix patrimonial entre deux modes d'indemnisation et n'est pas un agrément redondant. Aucune cotisation accessoire n'est instituée ici.",
    "La version assignée s'arrête au 1er novembre 2026 et n'a pas de I ; elle ne doit pas être présentée comme la future rédaction fractionnée. L. 434-1 conserve son capital, avec seul allègement de calendrier dans ce lot. L. 351-1-4 proposé conserve les conditions favorables et dispenses de preuve, tout en supprimant la commission : informer de ce droit ne recrée pas sa saisine. Les seuils réglementaires ne sont pas inventés dans la proposition. R. 434-1 à R. 434-3 ont été lus pour distinguer seuil de 10 %, calcul du taux utile et assistance ; leurs montants et fractions restent dans leur propre version.",
    "La source entière remplit une fonction d'indemnisation et de solidarité sans doublon administratif propre identifié. Ses garanties et ses conditions de non-double indemnisation sont maintenues sans gain nouveau compté.",
    "La rédaction postérieure au 1er novembre 2026 n'est pas fournie intégralement dans ce lot ; aucune assimilation de rente professionnelle et de composante fonctionnelle future n'est décidée.",
    "Aucune charge nouvelle n'est identifiée : aucun nouveau contrôle, dossier, registre ou information périodique n'est ajouté ; l'information utile du bénéficiaire subsiste.",
    "Rente, aide pour tierce personne et revalorisation, choix en cas d'accidents successifs, plancher d'invalidité et information sur retraite anticipée restent applicables aux futures situations relevant de leur version et aux droits antérieurs. L'option de capital n'est pas supprimée au nom de l'automaticité.")

p='''<p>La victime titulaire d'une rente prévue à l'article L. 434-2 peut en demander la conversion partielle en rente réversible au bénéfice de son conjoint, du partenaire lié à elle par un pacte civil de solidarité ou de son concubin. Lorsque la rente relève d'une rédaction de cet article comportant un I, la faculté de conversion porte sur la seule rente mentionnée à ce I. Les conditions de cette conversion sont fixées par décret en Conseil d'Etat.</p>
<p>Cette rente est, à compter de son versement, revalorisée dans les conditions prévues à l'article L. 434-17.</p>
<p>Cette coordination du renvoi ne modifie ni les conditions de conversion des rentes relevant des dispositions antérieures, ni les conditions d'application dans le temps résultant du III de l'article 96 de la loi n° 2025-1403 du 30 décembre 2025. Les conversions accordées et les droits, créances et recours relatifs aux périodes antérieures sont préservés.</p>'''
add('L434-3',
    "Coordination nécessaire des versions : la source renvoie au I de L. 434-2 alors que la vue de ce dernier applicable avant le 1er novembre 2026 n'est pas subdivisée. Le renvoi vise la rente de cette rédaction et reste limité au I lorsqu'une rédaction subdivisée s'applique. Aucun élargissement à une autre composante de rente n'est opéré ; bénéficiaires, conversion partielle facultative et revalorisation sont conservés.",
    "La note source de 2025 distingue entrée en vigueur et application aux pensions prenant effet à la date fixée selon l'article 90 V de la loi de 2025. Cette transition est conservée expressément, sans lui substituer une date de notre réforme. R. 434-5, lu en entier, confirme la faculté de conversion des rentes anciennes, son tarif et sa neutralité de charge pour la caisse ; sa version s'arrête aussi au 1er novembre 2026. L. 434-20 fourni est un régime distinct d'indemnisation des travailleurs/ayants droit étrangers cessant de résider en France ou non résidents, sous réserves internationales ; il n'est pas réformé par la conversion ni assimilé au contrat unique. Les rédactions nouvelles de L. 434-2 et du règlement restent à confronter dans leurs lots ; aucune conformité internationale globale n'est affirmée.",
    "Le renvoi est rendu lisible entre versions successives sans compter une nouvelle ouverture de droit. Les exclusions de détention et de placement éducatif sont supprimées aux articles L. 434-4 et L. 434-5, pas par ce renvoi.",
    "La version future complète de L. 434-2 n'est pas dans les cibles ; la clause conditionnelle conserve expressément le seul I et n'en invente pas les composantes. Aucun effet budgétaire supplémentaire n'est établi.",
    "Aucune charge nouvelle n'est identifiée : pas de dossier, option ou délai ajouté à la demande volontaire de conversion et pas de nouvelle condition de parenté.",
    "La conversion partielle au profit du conjoint, partenaire de PACS ou concubin et la revalorisation dès le versement restent disponibles, y compris pour les rentes anciennes selon leurs conditions. La coordination ne réduit pas le champ des futurs bénéficiaires du I applicable.",p,'coordination_only')
effect('L434-3','coordination','rente-atmp-conversion-renvoi-versions',
    "Coordination explicite de la référence à L. 434-2 entre rédaction non subdivisée et rédaction comportant un I.",
    "Mention exclusive du I de L. 434-2 dans la source, face à une vue antérieure sans ce I et une note d'application différée.",
    "Rente de L. 434-2 visée dans la version non subdivisée ; seule rente du I visée lorsque cette subdivision s'applique, transitions maintenues.",'regime','Titulaires de rentes AT-MP souhaitant une réversibilité partielle et leurs proches éligibles.',
    "Dates d'application de la loi de 2025 et conditions des rentes antérieures conservées ; conversions acquises protégées.",
    "Aucun nouveau contrôle ni extension à un autre régime de rente.",
    "La victime titulaire d'une rente mentionnée au I de l'article L. 434-2",
    "Lorsque la rente relève d'une rédaction de cet article comportant un I, la faculté de conversion porte sur la seule rente mentionnée à ce I.")

for n,restriction,persons,quote in [
    ('L434-4',"l'attente de la libération définitive de la personne détenue",'Personnes détenues victimes d’accidents du travail et proches bénéficiaires de la conversion.',"La conversion de rente prévue à l'article L. 434-3 ne peut intervenir qu'après la libération définitive du détenu, victime d'un accident du travail."),
    ('L434-5',"l'attente de la perte de la qualité de pupille de l'éducation surveillée",'Victimes ayant la qualité de pupille de l’éducation surveillée et proches bénéficiaires de la conversion.',"La conversion de rente prévue à l'article L. 434-3 ne peut intervenir qu'à compter du jour où la victime a perdu la qualité de pupille de l'éducation surveillée.")
]:
    p=("<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant cette abrogation.</p>\n"
       "<p>À compter de cette date, "+restriction+" ne peut plus conditionner la conversion partielle en rente réversible prévue à l'article L. 434-3. Cette suppression s'applique aux demandes en cours et aux demandes ultérieures, y compris pour des rentes attribuées avant cette date. Elle n'emporte aucune conversion automatique ; la demande volontaire, les conditions de conversion et les règles de capacité, de représentation et de protection juridique applicables demeurent.</p>\n"
       "<p>Les rentes et conversions déjà accordées, les arrérages acquis, les créances et les recours relatifs aux périodes antérieures sont préservés. Les refus définitifs antérieurs ne sont pas annulés, mais ne font pas obstacle à une nouvelle demande pour l'avenir fondée sur la suppression de cette restriction, sans délai d'attente supplémentaire.</p>")
    add(n,
        "Abrogation prospective de fond : suppression de "+restriction+" comme exclusion catégorielle de la faculté de conversion de L. 434-3. La conversion reste volontaire et soumise à ses règles actuarielles et de protection juridique ; aucune fonction essentielle ne justifie ce gel général fondé seulement sur le statut de la victime. Les droits anciens ne sont ni liquidés de force ni recalculés rétroactivement.",
        "La note de l'article 83 II de la loi de 2019 (entrée au 1er janvier 2020) est historique. Coordonner tout règlement qui reprendrait encore cette attente ; ne supprimer ni représentation des personnes protégées ni consentement, ni barème ou neutralité actuarielle. La réversibilité n'est ni une sortie générale en capital ni un droit de succession. Les anciens refus gardent leurs effets passés et n'interdisent pas une demande future sous la loi nouvelle.",
        "La seule norme de l'article est une attente catégorielle : elle est réellement retirée pour les conversions futures, sans suppression des droits à rente ou de la demande de conversion.",
        "Les conditions générales, les protections des personnes vulnérables et les règles actuarielles subsistent ; aucun gain national ni effet sur tous les régimes de détention n'est chiffré.",
        "Aucune charge nouvelle n'est identifiée : aucune déclaration ou autorisation ne remplace l'attente supprimée ; une demande volontaire reste nécessaire à une conversion patrimoniale.",
        "La faculté de réversibilité est étendue aux victimes de ce statut pour les demandes futures et en cours, même sur rente ancienne. Le consentement et la protection juridique demeurent, et aucune rente déjà accordée n'est amputée par une conversion automatique.",p,'material_reduction',repeal="Suppression de "+restriction+" comme condition de la conversion partielle volontaire de la rente AT-MP en rente réversible ; droits antérieurs et protections juridiques conservés.")
    effect(n,'relief_extended','conversion-rente-atmp-fin-exclusions-statutaires',
        "Suppression de "+restriction+" pour la réversibilité partielle de rente.",
        "Conversion impossible tant que n'est pas accomplie la condition statutaire propre à cet article, même si les autres conditions sont remplies.",
        "Conversion volontaire accessible sans cette attente statutaire, sous les conditions générales et la protection juridique existantes.",'regime',persons,
        "Demandes en cours et futures après entrée en vigueur, même pour rente ancienne ; aucun recalcul automatique des périodes passées.",
        "Pas d'agrément, de déclaration ni de délai de remplacement ; demande volontaire et règles actuarielles existantes maintenues.",
        quote,"À compter de cette date, "+restriction+" ne peut plus conditionner la conversion partielle en rente réversible prévue à l'article L. 434-3.")

add('L434-6',
    "Maintien intégral nécessaire du cumul des rentes AT-MP avec les pensions de statut particulier constituées par retenues, du plafonnement pour les seules infirmités de même accident et du plancher de rente. La retenue évoquée décrit les pensions éligibles ; cet article ne crée pas un prélèvement autonome à supprimer. La limite évite un double remplacement de revenu sans retirer le plancher favorable.",
    "Le plafond ne vaut que si la pension d'invalidité résulte de l'accident à l'origine de la rente ; ne pas l'étendre à toutes retraites. Le salaire de comparaison et son coefficient de L. 434-17 restent inchangés. L. 434-2 est la garantie minimale de rente applicable dans sa version ; aucun seuil d'ancienneté ou plafond de six mois d'indemnité de rupture ne s'y transpose.",
    "La source entière conserve le cumul autorisé et son plancher en évitant le double remplacement pour un même accident. Aucun prélèvement ni formalité nouvelle n'est retiré dans cet article.",
    "Les statuts particuliers, fractions et revalorisations restent à leurs textes propres ; le maintien ne démontre pas une baisse du montant des retenues ou un solde net national.",
    "Aucune charge nouvelle n'est identifiée : ni nouveau calcul déclaratif ni registre ni délai supplémentaire ne sont créés.",
    "Le cumul favorable et le minimum de rente sont conservés pour les futures situations recevables et les droits en cours. La limite spéciale ne s'étend pas aux pensions d'invalidité d'une autre cause ni indistinctement aux retraites.")

add('L434-7',
    "Maintien intégral du principe de pension aux ayants droit en cas de décès consécutif à l'accident. C'est une prestation sociale, non un droit fiscal de succession ; la suppression des impôts au décès ne justifie pas de retirer cette protection. Aucun prélèvement ni formalité supplémentaire n'est créé par cet article.",
    "Les personnes et conditions sont celles des articles suivants, notamment L. 434-8 réécrit dans ce lot et L. 434-10 fourni comme cible. La prise d'effet « à partir du décès » n'est pas silencieusement remplacée par celle du premier paiement d'arrérages dans un règlement. Le décès n'est ni un nouveau contrat ni une ancienneté de rupture.",
    "Aucun changement normatif : maintien du droit de base des ayants droit, sans gain de simplification ou d'impôt compté.",
    "Les modalités et quotes-parts des différentes catégories d'ayants droit restent dans leurs articles propres ; aucune dépense ou recette nationale n'est estimée.",
    "Aucune charge nouvelle n'est identifiée : aucune nouvelle démarche ou condition n'est ajoutée au principe attributif de la pension.",
    "La pension au décès reste ouverte à tous les futurs ayants droit éligibles selon les articles suivants, sans assimilation à un capital successoral taxé ou disparition des droits d'enfants.")

old="Sous réserve des dispositions des alinéas suivants, le conjoint ou le concubin ou la personne liée par un pacte civil de solidarité a droit à une rente viagère égale à une fraction du salaire annuel de la victime, à condition que le mariage ait été contracté, le pacte civil de solidarité conclu ou la situation de concubinage établie antérieurement à l'accident ou, à défaut, qu'ils l'aient été depuis une durée déterminée à la date du décès. Toutefois, ces conditions ne sont pas exigées si les époux, les concubins ou les partenaires du pacte civil de solidarité ont eu un ou plusieurs enfants."
new="Sous réserve des dispositions des alinéas suivants, le conjoint ou le concubin ou la personne liée par un pacte civil de solidarité a droit à une rente viagère égale à une fraction du salaire annuel de la victime. L'antériorité du mariage, du pacte civil de solidarité ou du concubinage par rapport à l'accident et leur durée à la date du décès ne conditionnent pas ce droit, que les intéressés aient ou non eu des enfants."
p=replace('L434-8',old,new)
old2="Le pourcentage minimal et la durée minimale de cette incapacité sont fixés par décret en Conseil d'Etat."
new2="Le pourcentage minimal de cette incapacité est fixé par décret en Conseil d'Etat. Aucune durée minimale d'incapacité ne conditionne ce complément ; il est dû pour les périodes pendant lesquelles la condition d'incapacité est remplie."
assert old2 in p
p=p.replace(old2,new2)
p=append(p,"La suppression des conditions d'antériorité et de durée du mariage, du pacte civil de solidarité ou du concubinage s'applique aux décès intervenus à compter de l'entrée en vigueur de la loi portant la présente modification. La suppression de la durée minimale d'incapacité s'applique aux périodes de complément de rente à compter de cette date, y compris lorsque le décès est antérieur. Les conditions et répartitions prévues aux deuxième à cinquième alinéas, la réserve de l'article suivant et le pourcentage minimal d'incapacité demeurent applicables. Les droits acquis, arrérages, créances et recours relatifs aux périodes antérieures sont préservés ; les présentes suppressions n'ouvrent pas une restitution générale pour ces périodes.")
add('L434-8',
    "Réduction de fond des délais d'accès : retrait de l'antériorité du lien conjugal/PACS/concubinage à l'accident et, à défaut, de sa durée minimale au décès. La dispense favorable liée aux enfants devient universelle dans ce champ, sans fermer son avantage. Retrait aussi de la durée minimale d'incapacité pour le complément du survivant ; le taux minimal et la persistance de l'incapacité restent. Les six alinéas restent à leur place, avec intégralité des règles sur ex-conjoint, ex-partenaire, minimum du nouveau conjoint, sanctions familiales/transfert aux enfants et âge ou incapacité du complément.",
    "R. 434-10 a été lu en entier : rente de 40 %, délai de lien de deux ans, fraction d'ex-conjoint de 20 %, minimum de nouveau conjoint moitié de 40 %, complément de 20 %, âge de 55 ans, incapacité de 50 % et durée de trois mois. Seuls les deux ans et les trois mois sont privés de fondement par la présente réforme ; les autres paramètres restent. R. 434-11 à R. 434-13 ont été lus : demande, contrôle médical, date de première constatation, contrôle du maintien de l'incapacité gardent leur champ, à coordonner sans réintroduire les durées supprimées. L. 434-9, lu en entier, conserve ses avantages avec enfants et le rétablissement de rente : la réserve du sixième alinéa n'est pas supprimée. Les mots « l'article suivant » restent ce renvoi, sans déplacement. L. 434-10 fournit bien enfants, descendants et enfants recueillis pour le transfert en cas de déchéance. Aucune de ces prestations n'est un prélèvement successoral ; coûts supplémentaires possibles non chiffrés.",
    "Deux barrières temporelles sont supprimées : lien de deux ans à défaut d'antériorité à l'accident, et incapacité d'au moins trois mois pour le complément avant l'âge. Les fractions de rente, seuil d'incapacité, bénéficiaires et protections familiales subsistent.",
    "Le lien familial doit toujours être réel et l'incapacité contrôlable ; les ex-conjoints et ex-partenaires gardent leurs conditions et limites. L'effet sur dépenses et nombre de bénéficiaires n'est pas chiffré.",
    "Aucune charge nouvelle n'est identifiée : ni déclaration, preuve d'enfant, nouvelle durée ni autorisation ne remplace les conditions retirées. Les contrôles du lien réel et de l'incapacité demeurent ceux existants.",
    "La dispense de durée liée aux enfants n'est pas supprimée au détriment de ses bénéficiaires : la dispense est étendue à tous les liens éligibles. Minimum du nouveau conjoint, droits d'ex-conjoint/ex-partenaire, transfert aux enfants, réintégration et complément d'âge ou incapacité restent ouverts pour les situations futures ; les avantages de L. 434-9 sont aussi conservés.",p,'material_reduction',[
        "Condition d'antériorité du mariage, du pacte civil de solidarité ou du concubinage par rapport à l'accident, ou à défaut condition de durée minimale au décès.",
        "Durée minimale d'incapacité générale de travail pour l'accès au complément de rente du survivant avant l'âge réglementaire."
    ])
effect('L434-8','relief_extended','rente-survivant-fin-durees-minimales',
    "Suppression des deux barrières temporelles d'accès à la rente du survivant et à son complément d'incapacité, regroupées en un seul effet de cette mesure.",
    "Au premier alinéa, antériorité du lien à l'accident ou, à défaut, lien d'au moins deux ans au décès selon R. 434-10, sauf enfants communs. Au sixième alinéa, incapacité générale au taux minimal pendant au moins trois mois selon R. 434-10 pour le complément avant l'âge réglementaire. Les fractions de salaire annuel sont celles de ces régimes.",
    "Au premier alinéa, aucune antériorité ou durée du lien, avec ou sans enfant. Au sixième alinéa, même taux minimal d'incapacité mais sans durée minimale : complément pour les périodes admissibles. Aucun taux ni assiette de rente modifié ; règles des ex-conjoints, ex-partenaires, minimum du nouveau conjoint et droits des enfants maintenus.",
    'regime','Conjoints, partenaires de PACS et concubins survivants de victimes AT-MP, dont les bénéficiaires du complément pour incapacité générale.',
    "Suppression des conditions du lien pour les décès à compter de l'entrée en vigueur ; suppression de la durée d'incapacité pour les périodes de complément à compter de cette date, même sur décès antérieur. Droits anciens préservés et aucun rappel général pour les périodes antérieures.",
    "Aucune condition, déclaration ou preuve supplémentaire ; lien réel, taux d'incapacité, contrôles médicaux et conditions distinctes existantes conservés. Aucun coût public net chiffré.",
    text(B['L434-8']['source_xml']).strip(),
    text(A['L434-8']['proposed_xml']).strip())

# Chaque analyse vise la vue fournie, dont l'empreinte est recopiée sans recalcul
# sur une proposition nouvelle rédigée dans ce lot.
context={
'L432-1':(
 "Le tiers payant de L. 432-1 ne renvoie pas à L. 1234-1 : les quinze jours calendaires proposés après notification sont un préavis, ni une carence de soins ni une limite du remboursement. Les préavis des contrats anciens demeurent distincts.",
 "Les soins et prestations après décès de L. 432-1 restent dus aux bénéficiaires du livre IV ; le contrat unique privé proposé ne subordonne pas ce droit à une nouvelle embauche et ne ferme pas les droits des anciens contrats.",
 "Les frais de soins ne constituent pas l'indemnité ordinaire de rupture de L. 1234-9. Ni le seuil d'un an mesuré préavis inclus ni le calcul à 0,20 mois par année totale et plafond de six mois ne s'appliquent au tiers payant."),
'L432-3':(
 "L'interdiction de demander des honoraires et la preuve par tout moyen ne dépendent pas du préavis de L. 1234-1. Les quinze jours proposés après notification ne sont pas une période sans remboursement, pour nouveaux comme anciens contrats.",
 "L. 1221-2 proposé impose le contrat indéterminé aux futures embauches privées ; il ne limite pas la prise en charge des soins des victimes d'anciens CDD. La dispense de feuille vaut selon la date des soins, pas selon la forme du contrat.",
 "Le tarif majoré et la protection contre l'avance d'honoraires sont étrangers au barème ordinaire de rupture. Le seuil d'un an, le prorata en mois complets et le plafond de six mois de L. 1234-9 ne réduisent pas ces droits médicaux."),
'L432-7':(
 "L'indemnité pendant la réadaptation de L. 432-7 ne se confond pas avec le préavis de licenciement. Les quinze jours proposés courant du lendemain de la notification ne mettent pas fin par eux-mêmes au traitement ni aux droits sociaux de la victime.",
 "La durée limitée d'une réadaptation n'est pas un terme d'emploi au sens de L. 1221-2 proposé. Si une nouvelle embauche privée est conclue, elle est indéterminée ; la fin du traitement ne termine pas l'emploi, et les anciens droits restent couverts.",
 "L'indemnité journalière de réadaptation n'est pas l'indemnité ordinaire de rupture. Le seuil d'un an à fin effective, préavis inclus, et le calcul à 0,20 mois par année totale de L. 1234-9 n'y sont pas importés ; aucune année de soins n'est retranchée."),
'L432-8':(
 "Les contrôles médicaux et leurs sanctions de L. 432-8 ont un objet distinct du préavis de L. 1234-1. Les quinze jours proposés après notification ne dispensent pas des contrôles et n'autorisent aucune coupure automatique de soins à leur expiration.",
 "La réadaptation ne devient pas un nouveau CDD : L. 1221-2 proposé distingue sa durée de celle de l'emploi. Les obligations médicales modifiées et la continuité des soins s'appliquent aussi aux anciens contrats, selon les périodes de soins visées.",
 "La suspension possible de l'indemnité journalière n'est pas le zéro avant un an de l'indemnité ordinaire de L. 1234-9. L'ancienneté de rupture, ses mois complets et son plafond de six mois ne remplacent pas les conditions médicales de réadaptation."),
'L432-9':(
 "La rééducation et son supplément de revenu ne sont pas limités par le préavis de L. 1234-1. Les quinze jours proposés courent après notification écrite, non après la fin de la formation ; aucune rupture collective ou protégée n'est rendue automatique.",
 "Le placement chez un employeur vise l'apprentissage d'une profession. Sa phase pédagogique peut être limitée, mais une embauche privée nouvelle relève du contrat indéterminé de L. 1221-2 proposé ; la fin de la phase ne termine pas cet emploi. Anciens contrats préservés.",
 "Le maintien intégral de l'indemnité ou de la rente et le supplément jusqu'au salaire/SMIC ne sont pas une indemnité de licenciement. Le seuil d'un an avec préavis inclus et le plafond ordinaire de six mois de L. 1234-9 ne les neutralisent pas."),
'L432-10':(
 "Le droit au reclassement de L. 432-10 n'est pas une durée de préavis. Le délai individuel de quinze jours proposé à L. 1234-1 ne supprime ni la recherche de reclassement ni les procédures spéciales et autorisations nécessaires à une rupture.",
 "La rééducation et le reclassement peuvent avoir une durée propre ; L. 1221-2 proposé interdit d'en faire le terme automatique d'un nouvel emploi privé. Le financement de ces droits reste ouvert aux situations futures et aux victimes d'anciens contrats.",
 "La participation de la caisse aux frais de reclassement ne relève pas de l'indemnité ordinaire de L. 1234-9. Aucun seuil d'un an ni plafond de six mois n'y est transposé ; les indemnités spéciales d'inaptitude gardent leur base distincte."),
'L432-12':(
 "L'abondement du CPF est une aide à la reconversion, sans renvoi au préavis de L. 1234-1. Le délai de quinze jours proposé après notification ne ferme pas le compte et ne limite pas la durée d'utilisation de l'abondement.",
 "Le CPF et son abondement restent accessibles sous contrat unique futur ; la durée de la formation ne termine pas l'emploi en application de L. 1221-2 proposé. La suppression des nouveaux CDD n'efface ni droits acquis ni aides de même objet.",
 "Le seuil de L. 432-12 est un taux d'incapacité fixé par décret et non l'ancienneté d'un an de L. 1234-9. L'abondement n'est ni calculé à 0,20 mois par année ni plafonné à six mois de salaire ; sa conservation concerne les futures victimes."),
'L433-1':(
 "Le préavis individuel proposé à L. 1234-1 est de quinze jours calendaires à compter du lendemain de la présentation ou réception de la notification selon L. 1234-3. Le sixième alinéa est précisé pour que la seule notification n'arrête pas prématurément l'indemnité du nouveau contrat ; salaire, reclassement et protections restent distincts.",
 "L. 1221-2 proposé impose l'emploi indéterminé nouveau sans terme de formation ou rééducation. Les indemnités AT-MP de L. 433-1 ne sont pas réservées aux seuls contrats nouveaux : les anciens CDD et les arrêts en cours conservent leurs droits, selon les transitions de sinistre.",
 "Le zéro avant un an et les 0,20 mois par année totale, mois complets et plafond de six mois de L. 1234-9 concernent la rupture ordinaire patronale, non les indemnités journalières. Le seuil se mesure fin effective préavis inclus ; il ne supprime ni salaire repris à un mois ni indemnité spéciale d'inaptitude sans seuil."),
'L433-2':(
 "Le délai de majoration de l'indemnité journalière n'est pas le préavis de L. 1234-1. Les quinze jours proposés après notification n'avancent ni ne retardent cette majoration, et les anciens préavis conservent leur régime.",
 "L'assiette salariale et la majoration de l'indemnité restent applicables quelle que soit la forme passée du contrat. L. 1221-2 proposé ne transforme pas l'arrêt en contrat à terme ni la fin de l'indemnisation en fin automatique de l'emploi.",
 "La fraction du salaire journalier de L. 433-2 est indépendante des 0,20 mois par année totale et du plafond de six mois de L. 1234-9 proposé. Le seuil d'un an d'indemnité ordinaire n'est pas une condition pour percevoir ou majorer l'indemnité AT-MP."),
'L433-3':(
 "La fraction saisissable d'une indemnité journalière est indépendante du préavis de L. 1234-1. Les quinze jours proposés après notification ne changent ni seuils ni correctifs de saisie, pour les contrats anciens comme pour les nouveaux.",
 "L. 1221-2 proposé ne transforme pas l'indemnité en rémunération d'un contrat à terme ; la protection par renvoi aux limites du salaire reste pour tout bénéficiaire AT-MP, sans condition de nouvelle embauche à durée indéterminée.",
 "L. 1234-9 régit une indemnité ordinaire de rupture, non la quotité saisissable de l'indemnité journalière. Ni son ancienneté d'un an préavis inclus ni son plafond de six mois ne limitent la protection conservée par L. 433-3."),
'L433-4':(
 "Le contrat d'emploi pénitentiaire est un régime spécial ; le préavis privé de quinze jours proposé à L. 1234-1 ne remplace ni le calendrier de détention ni le renvoi à l'article 723 du code de procédure pénale. Aucun délai privé de notification n'y est importé.",
 "L. 1221-2 proposé vise les contrats relevant du code du travail. Le contrat d'emploi pénitentiaire et le stage cité par L. 433-4 ne sont pas artificiellement requalifiés en contrat privé unique ; la durée du stage ne prouve aucun terme d'emploi privé.",
 "Les indemnités journalières maintenues pendant la détention ne sont pas l'indemnité ordinaire patronale de L. 1234-9. Le seuil d'un an et son barème de mois de salaire ne s'appliquent pas à ce régime ; aucun ancien droit du détenu n'est fermé."),
'L434-1':(
 "La notification permettant le versement du capital est une décision de caisse, pas celle de licenciement de L. 1234-1. Les quinze jours proposés après notification patronale n'en deviennent pas un délai de paiement ni une condition d'ancienneté.",
 "L'indemnité en capital relève de l'incapacité permanente, pas de la durée du contrat. Le contrat unique proposé à L. 1221-2 ne réduit pas les droits de victimes d'anciens contrats ni n'étend le champ temporel de cette version au-delà de ses règles propres.",
 "Le capital d'incapacité n'est pas l'indemnité ordinaire de L. 1234-9 : le seuil d'un an, les 0,20 mois par année totale et le plafond de six mois ne s'y appliquent pas. La notification de caisse accélère seulement un paiement au barème AT-MP."),
'L434-2':(
 "L'évaluation de l'incapacité et la rente n'ont pas pour délai le préavis de L. 1234-1. Les quinze jours proposés après notification de rupture ne ferment ni l'aide tierce personne ni l'information sur la retraite anticipée ; procédures spéciales distinctes.",
 "La rente et le choix capital/rente après accidents successifs concernent aussi les victimes d'anciens contrats. L. 1221-2 proposé n'en fait pas des aides réservées à une nouvelle embauche et ne confond pas fin de rééducation avec terme d'emploi.",
 "Le barème de L. 1234-9 proposé, avec un an préavis inclus puis 0,20 mois par année totale, ne calcule aucune des rentes de L. 434-2. Il ne faut ni plafonner cette rente à six mois ni retirer une première année à son assiette annuelle."),
'L434-3':(
 "La notification de rupture et le préavis de L. 1234-1 sont étrangers à la conversion volontaire de rente. Les quinze jours proposés ne deviennent ni délai de demande ni délai d'attente pour réversibilité ; les rentes anciennes restent régies par leurs conditions.",
 "L. 1221-2 proposé traite des emplois privés futurs, pas de la durée des rentes d'incapacité. La réversibilité peut bénéficier aux victimes d'anciens contrats et à leurs proches sans nouvelle embauche ni condition de CDI unique.",
 "La conversion de rente AT-MP ne dépend pas du barème d'indemnité ordinaire de L. 1234-9. Aucun seuil d'un an, prorata en mois complets ou plafond de six mois de salaire n'est imposé à sa demande ou à sa revalorisation."),
'L434-6':(
 "Le cumul avec une pension de statut particulier ne renvoie pas au préavis de L. 1234-1. Les quinze jours proposés après notification ne réduisent ni le cumul permis ni le plancher de rente et ne modifient pas un statut public par assimilation.",
 "Les pensions de statut particulier peuvent relever de régimes publics que L. 1221-2 proposé ne réforme pas implicitement. Le cumul reste ouvert aux futures situations éligibles sans exiger un emploi privé nouveau ; les anciens droits restent couverts.",
 "La limite de cumul pour un même accident n'est pas le plafond de six mois de l'indemnité ordinaire de L. 1234-9. Son seuil d'un an préavis inclus ne conditionne ni la pension de statut particulier ni le plancher AT-MP."),
'L434-8':(
 "L'antériorité et la durée du lien familial retirées ici ne sont pas le préavis de L. 1234-1. Les quinze jours proposés après notification de licenciement ne remplacent ni l'âge ni le contrôle d'incapacité du survivant et ne fixent pas sa prise d'effet au décès.",
 "Les conjoints, partenaires et concubins survivants restent couverts si la victime relevait d'un ancien contrat. L. 1221-2 proposé ne réserve pas la rente aux nouveaux CDI uniques ; les conditions des ex-conjoints et les droits d'enfants gardent leur champ.",
 "La durée d'union et la durée d'incapacité supprimées ne sont pas le seuil d'ancienneté d'un an de L. 1234-9. Le barème ordinaire à 0,20 mois par année totale, plafond six mois, n'est appliqué ni à la rente du survivant ni à son complément.")
}

extra={
('L432-1','L431-1'):"Les 1° et 3° de L. 431-1 visés par L. 432-1 sont les frais médicaux et assimilés puis les prestations hors rentes au décès. La charge revient aux caisses ; ni le 2° d'indemnité journalière ni le 4° de rente ne sont substitués à ces cibles.",
('L432-3','L431-1'):"Le 1° de L. 431-1 couvre notamment produits de L. 165-1 et prothèses dentaires : c'est bien le champ de la majoration tarifaire de L. 432-3. Les frais sont couverts même sans interruption de travail ; la dispense de feuille n'élargit pas les produits au-delà de ce champ.",
('L432-7','L433-1'):"Le renvoi fournit l'indemnité journalière durant la réadaptation, sans ancienneté de rupture. L. 433-1 distingue maximum ordinaire, exception du travail thérapeutique, reprise de revenu et sinistres depuis le 1er janvier 2027 ; L. 432-7 conserve sa garantie spéciale de toute la période du traitement, sans créer une autorisation de formation contraire au L. 323-3-1 proposé.",
('L432-8','L432-7'):"L. 432-7 ouvre traitement en établissement autorisé et indemnité pendant la réadaptation. L. 432-8 en est le régime de suivi, pas une nouvelle admission. Sa proposition ne retire ni la durée de prise en charge de L. 432-7 ni son renvoi à l'indemnité de L. 433-1.",
('L432-8','L432-9'):"La réserve du 4° vise la rééducation gratuite, le maintien de l'indemnité ou rente et le supplément de L. 432-9. La proposition du présent lot retire seulement son test préalable systématique ; aucun exercice prescrit ne supprime ces garanties ou ne transforme la formation en nouveau CDD.",
('L432-9','L433-1'):"Le renvoi du deuxième alinéa vise la période d'indemnité journalière, avec ses régimes et transitions, non le préavis de rupture. Son maintien intégral avec la rente et le supplément ne dépend ni d'une année d'emploi ni d'un nouvel agrément ; les garanties propres à la rééducation restent.",
('L432-10','L432-9'):"L. 432-9 est bien le droit de rééducation dont le décret organise les frais, avec admission gratuite, maintien de revenu, supplément et rente non diminuée après reconversion. La suppression du seul examen psychotechnique dans ce lot ne permet pas au décret de rétablir un test automatique.",
('L433-1','L323-1'):"Le deuxième alinéa vise exactement le 1° de L. 323-1 pour que le maximum AT-MP ne soit pas plus court que sa période de date à date. Ce renvoi ne rétablit pas la carence maladie dans les AT-MP ; interruption/reprise et date de sinistre restent distinctes du contrat unique.",
('L433-1','L323-3-1'):"Le cinquième alinéa étend le dispositif aux arrêts AT-MP. La proposition cible supprime avis préalable du médecin-conseil et accord distinct de caisse, avec médecin traitant, durée compatible, convention spéciale et anciens droits conservés. Le renvoi maintenu ne reconstitue pas ce double accord et ne fait pas du terme d'une action celui de l'emploi.",
('L433-1','L323-6'):"Le septième alinéa vise les conditions de l'indemnité : la proposition cible retire les horaires de sortie, libère les activités non rémunérées compatibles et évite la double information en subrogation, mais conserve contrôles, adresse et prescriptions. L. 432-4-1 et L. 432-8 sont coordonnés dans ce lot pour ne pas rétablir l'interdiction générale d'activité ; aucun seuil de rupture n'y est importé.",
('L433-2','L241-3'):"Le premier alinéa de L. 433-2 utilise le maximum de rémunération vieillesse, conservé au I du L. 241-3 proposé. Ses II à VII ajoutent un transfert conditionnel de cotisations pour salariés privés ; ce financement n'abaisse ni ce plafond de calcul ni le salaire de référence AT-MP et ne s'étend pas automatiquement aux employeurs publics.",
('L434-2','L434-1'):"Le quatrième alinéa offre le choix d'un capital selon L. 434-1 pour accidents successifs et impute les capitaux antérieurement versés si une rente est choisie. L'allègement du paiement proposé dans ce lot ne supprime ni le choix ni cette imputation. Les deux versions assignées ont une borne au 1er novembre 2026, qui ne vaut pas date de notre réforme.",
('L434-2','L351-1-4'):"Le dernier alinéa est une information sur la retraite anticipée d'incapacité, pas un renvoi au préavis. La proposition cible conserve taux plein, âges, taux et dispenses liées aux maladies professionnelles, tout en retirant la commission obligatoire ; cette information ne recrée pas sa saisine. La cible mentionne L. 434-1 A avec une transition de pensions en 2025, à distinguer de la version antérieure de L. 434-2 sans I.",
('L434-3','L434-20'):"L. 434-20 concerne capital de départ du territoire des étrangers, ayants droit non résidents et réserves conventionnelles ; ce n'est pas la conversion volontaire pour réversibilité de L. 434-3. Aucun renvoi direct n'est ajouté, ni règle internationale ou de résidence effacée par le contrat privé unique ou par le présent ajustement de versions.",
('L434-3','L434-2'):"La vue officielle de L. 434-2 ne comporte pas de I et expire au 1er novembre 2026 ; L. 434-3 a une note d'application aux pensions de la réforme de 2025. La proposition distingue expressément rente de la version non subdivisée et seule rente du I lorsqu'il existe, sans étendre à une composante différente ni avancer les dates applicables. Le droit antérieur de conversion est conservé.",
('L434-6','L434-2'):"Le dernier alinéa de L. 434-6 garantit au moins la rente qui aurait été servie selon L. 434-2. Ce renvoi vise le calcul d'incapacité applicable, pas une indemnité de licenciement. Le maintien de L. 434-2 et de ses versions temporelles conserve le plancher, sans cumuler deux fois une pension d'invalidité de même accident.",
('L434-8','L434-10'):"Le cinquième alinéa transfère les droits du proche déchu aux enfants et descendants de L. 434-10 ; la cible inclut filiation adoptive, relèvements d'âge, orphelins, descendants et enfants recueillis à charge. Aucun groupe n'est retiré par la suppression des durées du lien conjugal ; apprentissage ou recherche d'emploi restent des conditions de prestation, non des CDD à recréer."
}
common_numbers=['L1234-1','L1221-2','L1234-9']
for s in S:
    n=s['number']; key=s['code_id']+'|'+s['source_id']
    checks=[]
    for target_key in R['requirements'][key]:
        target=R['targets'][target_key]
        tn=target['number']
        if tn in common_numbers:
            assessment=context[n][common_numbers.index(tn)]
        else:
            assessment=extra[(n,tn)]
        assert len(assessment)>=80
        checks.append(dict(target_key=target_key,view_sha256=target['view_sha256'],assessment=assessment))
    A[n]['reference_checks']=checks

out=[A[s['number']] for s in S]
Path('answer.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'output_file':'answer.json','article_count':len(out)},ensure_ascii=False))
