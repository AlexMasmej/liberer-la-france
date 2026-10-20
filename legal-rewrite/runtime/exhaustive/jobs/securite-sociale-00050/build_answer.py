import json
import re
import html
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
references = json.loads(Path('reference-targets.json').read_text())
answers = []

def plain(xml):
    return html.unescape(re.sub(r'<[^>]+>', '', xml or ''))

def replace_once(text, old, new):
    assert text.count(old) == 1, old
    return text.replace(old, new, 1)

def append_paragraph(xml, text):
    return xml.rstrip() + '\n<p>' + text + '</p>\n'

def complete_paragraph_quote(xml, excerpt):
    for paragraph in re.findall(r'<p>(.*?)</p>', xml or '', re.S):
        paragraph = plain(paragraph).strip()
        if excerpt in paragraph:
            return paragraph
    return excerpt

def effect(kind, measure_id, description, before, after, unit, population,
           transition, replacement, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit,
                affected_population=population,
                conditions_and_transition=transition,
                replacement_or_new_burdens=replacement,
                source_quote=source_quote, proposed_quote=proposed_quote)

for source in sources:
    answers.append({k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')})

def retained(i, reason, notes, assessment, limitations, burdens, benefits):
    a = answers[i]
    a.update(proposed_xml=None, status='retained_unchanged',
             classification='retained_necessary', reason=reason,
             review_notes=notes, benefit_review=benefits,
             substantive_impact=dict(version=1, classification='retained_necessary',
                                     assessment=assessment, scope_limitations=limitations,
                                     new_burdens_review=burdens, effects=[]))

def rewritten(i, xml, reason, notes, assessment, limitations, burdens,
              effects, benefits, removed=None, repeal_scope=None, classification='material_reduction'):
    a = answers[i]
    a.update(proposed_xml=xml, status='rewrite_draft', reason=reason,
             review_notes=notes, benefit_review=benefits,
             substantive_impact=dict(version=1, classification=classification,
                                     assessment=assessment, scope_limitations=limitations,
                                     new_burdens_review=burdens, effects=effects))
    if removed:
        a.update(change_type='normative_reduction',
                 reform_policy_id='editorial_direction_2026_10_19',
                 removed_provisions=removed)
    if repeal_scope:
        a.update(change_type='full_repeal',
                 repeal_policy_id='editorial_direction_2026_10_19',
                 repeal_scope=repeal_scope)

# L321-2 : le document médical authentifiable subsiste ; la sanction du seul retard disparaît.
xml = replace_once(sources[2]['source_xml'], ' et, sous les sanctions prévues par décret,', ',')
xml = replace_once(xml,
    "Le directeur de la caisse primaire met en oeuvre le dispositif de sanctions prévu à l'alinéa précédent.",
    "Le seul dépassement du délai d'envoi ne peut entraîner ni refus, réduction ou récupération des indemnités journalières, ni sanction à l'encontre de l'assuré, lorsque l'incapacité de travail est médicalement établie. Cette règle ne fait pas obstacle au refus des indemnités correspondant à une période pendant laquelle le contrôle a effectivement été rendu impossible, ni aux mesures applicables en cas de fraude. Elle ne dispense pas de produire un avis authentique signé par le prescripteur.")
xml = append_paragraph(xml,
    "La suppression des sanctions fondées sur le seul retard s'applique aux envois effectués à compter de l'entrée en vigueur de la loi portant la présente modification, y compris pour un arrêt prescrit antérieurement, ainsi qu'aux sanctions non définitives à cette date. Les autres conditions d'ouverture des droits, les prescriptions et les recours demeurent applicables. Elle n'ouvre pas de droit général à restitution des sommes légalement retenues en vertu de décisions devenues définitives, sous réserve des dispositions répressives plus douces applicables.")
rewritten(2, xml,
    "Réforme de fond : retrait des sanctions et pertes d'indemnisation fondées sur le seul envoi tardif d'un arrêt médicalement établi. L'obligation d'envoi, son délai, le formulaire homologué et la signature sont conservés pour l'authentification et la liquidation. Le contrôle effectivement empêché et la fraude restent distinctement opposables ; aucun formulaire de remplacement n'est créé.",
    "R321-2 lu : le délai est de deux jours et l'envoi par l'assuré n'est déjà exigé qu'en l'absence de prescription ou prolongation dématérialisée ; cette dispense n'est donc pas un gain nouveau. Coordonner sa mention des sanctions et le dispositif réglementaire des retards avec la suppression législative. R323-12, lu, conserve le refus pour contrôle effectivement impossible, qui ne doit pas devenir une présomption automatique attachée au retard. Les sanctions autonomes de fraude et les règles de preuve médicale restent applicables. Les dates de 2025 sont historiques, non celles de la présente réforme.",
    "Le texte officiel autorise des sanctions du retard déclaratif ; la proposition les retire lorsque le retard est le seul grief et que l'incapacité est établie, sans supprimer la preuve de l'arrêt ni la dette résultant d'une fraude.",
    "Pas de baisse de taux de cotisation ni de modification de l'assiette. Le coût des indemnités qui ne seraient plus minorées et la coordination des règlements de retard restent à évaluer.",
    "Aucune charge nouvelle identifiée : le même avis homologué signé et le même délai subsistent ; aucune attestation de bonne foi, nouvelle déclaration ou autorisation de remplacement n'est exigée.",
    [effect('obligation_removed', 'arret-maladie-fin-sanction-seul-retard',
        "Suppression des conséquences défavorables attachées au seul retard d'envoi de l'avis médical.",
        "Envoi dans le délai réglementaire, assorti de sanctions réglementaires contre l'assuré retardataire.",
        "Envoi toujours dû ; aucune sanction ou perte d'indemnité pour le seul retard si l'incapacité est établie, hors contrôle effectivement impossible ou fraude.",
        'legal_duty', "Assurés tenus de transmettre un avis d'arrêt de travail à leur caisse primaire.",
        "Envois à compter de l'entrée en vigueur, y compris arrêts antérieurs, et sanctions non définitives ; prescriptions et recours conservés.",
        "Aucune déclaration substitutive ; maintien du document authentique et des contrôles.",
        "Le directeur de la caisse primaire met en oeuvre le dispositif de sanctions prévu à l'alinéa précédent.",
        "Le seul dépassement du délai d'envoi ne peut entraîner ni refus, réduction ou récupération des indemnités journalières, ni sanction à l'encontre de l'assuré, lorsque l'incapacité de travail est médicalement établie.")],
    "L'article ne prévoit pas d'exonération fiscale. La dispense réglementaire d'envoi par l'assuré lorsque la prescription est dématérialisée reste acquise. Le droit à indemnisation est mieux protégé contre le seul retard ; aucun avantage lié à la maladie ou à un arrêt ancien n'est fermé pour les situations futures.",
    removed=["Les sanctions réglementaires et pertes d'indemnités fondées uniquement sur le dépassement du délai d'envoi d'un arrêt médicalement établi sont supprimées dans le nouveau champ temporel."])

# L322-5 : conservation des seize autres composantes et des repères d'alinéas.
xml = sources[4]['source_xml']
old = "Lorsqu'un patient refuse le transport partagé que lui propose une entreprise de transport sanitaire ou une entreprise de taxi conventionnée, alors que son état de santé n'est pas incompatible avec une telle solution de transport et que la proposition répond à des conditions de mise en œuvre du transport tenant en particulier aux caractéristiques du trajet et à l'organisation de la prise en charge sur le lieu de soins, ses frais de transport sont pris en charge après application au prix facturé d'un coefficient de minoration."
xml = replace_once(xml, old,
    "Le refus par le patient d'un transport partagé ne peut, à lui seul, entraîner une minoration de la prise en charge de ses frais de transport. Les autres conditions de prescription, de prise en charge et de tarification demeurent applicables.")
xml = replace_once(xml,
    "3° Les conditions relatives aux besoins territoriaux de transport des patients auxquelles sont subordonnés l'accès au conventionnement et le maintien du conventionnement des entreprises de taxi, qui peuvent être adaptées au niveau local ;",
    "3° L'accès au conventionnement et le maintien du conventionnement des entreprises de taxi ne peuvent être subordonnés aux besoins territoriaux de transport des patients, à un contingentement ou à un critère équivalent limitant le nombre d'entreprises conventionnées ;")
xml = replace_once(xml, 'les éléments mentionnés aux 3° à 7° applicables', 'les éléments mentionnés aux 4° à 7° applicables')
xml = append_paragraph(xml,
    "L'interdiction de minorer la prise en charge en raison du seul refus d'un transport partagé s'applique aux transports réalisés à compter de l'entrée en vigueur de la loi portant la présente modification, y compris sur prescription antérieure. La suppression des conditions territoriales de conventionnement s'applique à compter de cette même date aux demandes en cours, aux nouvelles demandes et au maintien des conventions existantes ; les clauses qui imposent ces seules conditions cessent de produire effet, sans déclaration de remplacement. Les conventions existantes, les aides à l'équipement, les dispenses d'avance de frais et les autres stipulations compatibles demeurent applicables. Les transports antérieurs, créances, restitutions, prescriptions et recours correspondants conservent leur régime, sans remboursement rétroactif général. Un refus ancien fondé sur les seuls besoins territoriaux ne fait pas obstacle à une nouvelle demande.")
rewritten(4, xml,
    "Deux réductions de fond : suppression de la minoration du remboursement pour refus du transport partagé et suppression de la sélection des taxis selon les besoins territoriaux ou un contingentement équivalent. Le conventionnement tarifaire, la prescription, le trajet le moins onéreux compatible, la durée maximale de cinq ans, les tarifs et suppléments, les aides, le contrôle de la facturation et l'approbation nationale demeurent. Le deuxième alinéa et le 3° gardent leur place ; la plage 3° à 7° du renvoi local devient 4° à 7°.",
    "Coordonner L322-5-1 dans ce lot pour conserver le tiers payant en cas de refus du partage. Les conventions-cadres, conventions types, textes d'application du coefficient et règles locales doivent retirer les conditions supprimées ; la loi les rend déjà inopposables dans son nouveau champ. L162-4-1 2° vise la justification médicale du déplacement et du mode, L162-5-15 l'identification du prescripteur : ni l'un ni l'autre n'est un régime de rupture du travail. La note de la loi de 2025 conserve sa transition de deux mois propre aux anciennes conventions. L162-15-1, lu dans le corpus, continue de sanctionner les engagements licites, pas les clauses rendues inopposables. L1111-3-5 du code de la santé publique est un renvoi source conservé, dont le texte n'est pas fourni ici ; aucune réécriture de ce code n'est revendiquée. Effets financiers sur l'assurance maladie et les transporteurs à chiffrer, sans tarif nouveau.",
    "La comparaison intégrale met en évidence deux contraintes réellement retirées : un moindre remboursement imposé au patient qui refuse le partage et une condition territoriale d'entrée ou de maintien des taxis. Le tarif conventionnel et le contrôle antifraude subsistent.",
    "Les autres motifs de refus de conventionnement ne sont pas supprimés. Le coût des transports non partagés et l'effet de l'ouverture du conventionnement ne sont pas chiffrés ; aucune baisse nationale de dépense ou de cotisation n'est démontrée.",
    "Aucune charge nouvelle identifiée : aucune déclaration ne remplace la sélection territoriale, les tarifs et la prescription subsistent sans pièce nouvelle, et le patient n'a pas à justifier son refus du partage.",
    [effect('relief_extended','transport-partage-fin-penalisation-refus',
        "Retrait de la minoration du remboursement attachée au refus du partage.",
        "Patient médicalement compatible refusant une proposition répondant aux conditions légales : prix facturé minoré par un coefficient.",
        "Aucun coefficient de minoration pour le seul refus ; bases, tarifs et autres conditions de remboursement inchangés.",
        'other', 'Patients utilisant un transport sanitaire ou un taxi conventionné.',
        "Transports à compter de l'entrée en vigueur même sur prescription antérieure ; transports anciens sans restitution générale.",
        "Aucune justification nouvelle du refus ; autres conditions de prise en charge conservées.",
        old,
        "Le refus par le patient d'un transport partagé ne peut, à lui seul, entraîner une minoration de la prise en charge de ses frais de transport."),
     effect('authorization_removed','taxis-conventionnement-fin-contingent-territorial',
        "Suppression du seul filtre territorial de conventionnement, sans suppression du cadre tarifaire.",
        "L'accès et le maintien du conventionnement des taxis peuvent dépendre des besoins territoriaux, adaptés localement.",
        "Ni besoins territoriaux, ni contingentement, ni critère équivalent limitant le nombre d'entreprises ; autres conditions licites conservées.",
        'legal_duty','Entreprises de taxi candidates au conventionnement ou déjà conventionnées.',
        "Demandes en cours et futures et maintien des conventions à l'entrée en vigueur ; nouvelle demande ouverte après ancien refus territorial.",
        "Aucune déclaration ou nouvelle autorisation substitutive ; la convention tarifaire reste nécessaire.",
        "3° Les conditions relatives aux besoins territoriaux de transport des patients auxquelles sont subordonnés l'accès au conventionnement et le maintien du conventionnement des entreprises de taxi, qui peuvent être adaptées au niveau local ;",
        "3° L'accès au conventionnement et le maintien du conventionnement des entreprises de taxi ne peuvent être subordonnés aux besoins territoriaux de transport des patients, à un contingentement ou à un critère équivalent limitant le nombre d'entreprises conventionnées ;")],
    "La dispense d'avance de frais du 2°, les aides à l'équipement du 8°, les suppléments pour mobilité réduite du 6°, les adaptations tarifaires territoriales et la prescription excluant un partage médicalement inadapté sont conservés pour les bénéficiaires futurs comme actuels. Le refus d'un partage n'entraîne plus de minoration ; aucun taux de remboursement, aide ou tarif favorable n'est supprimé pour financer cette ouverture.",
    removed=["La minoration de prise en charge du patient refusant un transport partagé pourtant compatible avec son état est supprimée pour les transports futurs.",
             "La condition de besoins territoriaux pour accéder au conventionnement des taxis ou le conserver, avec son adaptation locale et ses équivalents de contingentement, est supprimée."])

xml = replace_once(sources[5]['source_xml'],
    "Cette dispense d'avance des frais ne s'applique pas lorsque le patient refuse un transport partagé dans les conditions prévues au deuxième alinéa de l'article L. 322-5.",
    "Cette dispense d'avance des frais s'applique également lorsque le patient refuse un transport partagé dans les conditions prévues au deuxième alinéa de l'article L. 322-5.")
xml = append_paragraph(xml,
    "Le maintien de la dispense en cas de refus d'un transport partagé s'applique aux transports réalisés à compter de l'entrée en vigueur de la loi portant la présente modification, y compris sur prescription antérieure. Les créances, remboursements, prescriptions et recours concernant les transports antérieurs conservent leur régime ; aucune restitution générale des avances anciennes n'est instituée.")
rewritten(5, xml,
    "Réduction de fond coordonnée avec L322-5 : retrait de l'exclusion du tiers payant pour refus d'un transport partagé. La part garantie par les régimes obligatoires et la base de participation de l'assuré restent intégralement celles de la source ; aucune extension au reste à charge ni aux entreprises non conventionnées n'est créée.",
    "Le deuxième alinéa de L322-5 est conservé à sa place et interdit désormais la minoration pour seul refus. L322-5-1 retire la sanction de trésorerie distincte, sans compter une seconde abolition de taxe. L162-14-1 et L162-14-2, lus intégralement dans le corpus, fixent le cadre conventionnel et arbitral des tarifs ; la participation continue d'y être calculée. La dispense porte uniquement sur la part obligatoire, non sur tout prix facturé.",
    "Le patient refusant le partage retrouve une dispense réelle d'avance, auparavant exclue : gain de trésorerie, sans baisse de dette finale due à ce seul article. En contrepartie, le tiers payant des prestataires conventionnés est étendu à ce cas ; le solde de coût n'est pas établi. Le coefficient de remboursement est traité dans L322-5 sous la même mesure.",
    "Le coût de trésorerie et de traitement pour les caisses et prestataires n'est pas mesuré. Les transports anciens, les prestataires non conventionnés et les parts non garanties ne sont pas couverts par cette ouverture ; aucun solde net de charge n'est démontré.",
    "L'obligation existante de tiers payant du prestataire conventionné est étendue aux patients refusant le partage : charge de trésorerie et de gestion supplémentaire possible, non chiffrée. Aucune nouvelle pièce, déclaration, donnée ni échéance n'est ajoutée au patient ; le circuit préexistant reste utilisé.",
    [effect('payment_deferred','transport-partage-fin-penalisation-refus',
        "Extension de la dispense d'avance existante au patient qui refuse le partage.",
        "Refus du partage : exclusion de la dispense d'avance de la part garantie par les régimes obligatoires.",
        "Même refus : dispense de cette avance maintenue, avec participation calculée selon les mêmes tarifs.",
        'financing','Assurés transportés par une entreprise de transports sanitaires conventionnée.',
        "Transports réalisés dès l'entrée en vigueur ; aucune restitution générale d'avances anciennes.",
        "Circuit de tiers payant préexistant, sans formalité de remplacement ; financement de trésorerie non chiffré.",
        "Cette dispense d'avance des frais ne s'applique pas lorsque le patient refuse un transport partagé dans les conditions prévues au deuxième alinéa de l'article L. 322-5.",
        "Cette dispense d'avance des frais s'applique également lorsque le patient refuse un transport partagé dans les conditions prévues au deuxième alinéa de l'article L. 322-5."),
     effect('obligation_added','transport-partage-fin-penalisation-refus',
        "Extension corrélative de la prise en charge en tiers payant par le prestataire conventionné, sans nouveau circuit imposé.",
        "Le prestataire n'est pas tenu de dispenser l'avance lorsque le patient refuse le partage dans le cas prévu par la source.",
        "Le prestataire conventionné doit aussi appliquer la dispense d'avance de la part obligatoire dans ce cas ; aucune réduction de la dette finale n'en est déduite.",
        'legal_duty','Entreprises de transports sanitaires conventionnées et organismes payeurs concernés.',
        "Transports réalisés dès l'entrée en vigueur ; pas de retraitement général des avances anciennes.",
        "Extension de périmètre du tiers payant existant ; coût de financement et traitement non chiffré, aucun formulaire nouveau.",
        "Cette dispense d'avance des frais ne s'applique pas lorsque le patient refuse un transport partagé dans les conditions prévues au deuxième alinéa de l'article L. 322-5.",
        "Cette dispense d'avance des frais s'applique également lorsque le patient refuse un transport partagé dans les conditions prévues au deuxième alinéa de l'article L. 322-5.")],
    "La dispense de l'avance de la part obligatoire est intégralement maintenue et ouverte également aux futurs patients refusant un transport partagé. La base conventionnelle de participation reste identique. Le bénéfice n'est ni réservé aux transports anciens ni conditionné à une justification nouvelle du refus.",
    removed=["L'exclusion de la dispense d'avance de frais frappant le patient qui refuse un transport partagé est supprimée pour les transports nouveaux."],
    classification='mixed')

xml = "<p>Le présent article est abrogé pour les journées d'incapacité de travail à compter de l'entrée en vigueur de la loi portant la présente abrogation, y compris au cours d'un arrêt commencé antérieurement.</p><p>La limitation particulière du nombre d'indemnités journalières fondée sur l'âge et la perception d'une pension, rente ou allocation de vieillesse cesse de s'appliquer à ces journées. Les assurés concernés relèvent des conditions et limites de droit commun de l'article L. 323-1 et des dispositions plus favorables qui leur sont applicables. Les personnes mentionnées à l'article L. 161-22-1-5 conservent le bénéfice de l'absence de cette limitation particulière. Les indemnités déjà servies restent prises en compte uniquement pour les limites de droit commun auxquelles elles sont légalement imputables, sans remise à zéro ni double compte.</p><p>Les droits, créances, liquidations, restitutions, prescriptions et recours relatifs aux journées antérieures demeurent régis par les règles qui leur étaient applicables, y compris la dérogation en faveur des personnes mentionnées à l'article L. 161-22-1-5. Aucune restitution rétroactive générale ni indemnisation sans incapacité médicalement constatée n'est instituée. Les autres règles de cumul de prestations demeurent applicables.</p>"
rewritten(13, xml,
    "Abrogation de fond de la limite spéciale d'indemnités journalières attachée au cumul d'une activité, d'un certain âge et d'un avantage de vieillesse. Les limites ordinaires de l'assurance maladie suffisent à borner le droit, sans plafond supplémentaire définitif sur toute la période de retraite. La dérogation favorable de la retraite progressive reste acquise, pour les journées futures comme anciennes.",
    "R323-2 lu : plafond actuel de soixante jours pour l'ensemble de la période au-delà de l'âge de L161-17-2 ; retirer ses deux premiers alinéas dans une coordination réglementaire, en conservant la règle distincte de non-cumul avec l'allocation chômage. L161-22-1-5 vise les trois voies de retraite progressive et leurs exclusions, pas le préavis privé. L323-1 demeure intégralement maintenu dans ce lot ; ses périodes et plafonds ne sont pas remis à zéro. L622-1 renvoie aussi à cet article : son renvoi doit devenir la règle commune dans le champ des indépendants sous ses adaptations, sans leur attribuer le contrat unique ni la capitalisation salariée. La note du 1er janvier 2026 n'est pas une date de réforme future. Dépense supplémentaire et financement à évaluer, aucune recette supposée.",
    "Suppression d'une limitation supplémentaire de couverture maladie pour les retraités qui travaillent, distincte des limites ordinaires conservées. Il s'agit d'une extension de prestation, sans réduction de cotisation ni économie publique revendiquée.",
    "La dépense supplémentaire n'est pas chiffrée. Les conditions médicales et d'ouverture de droits, le droit commun de durée et les règles distinctes de cumul restent applicables ; pas de réouverture générale des journées anciennes.",
    "Aucune charge nouvelle identifiée : aucun justificatif ou registre ne remplace le plafond supprimé. Les caisses liquident dans les conditions de droit commun déjà existantes, sans nouvelle condition pour la retraite progressive.",
    [effect('relief_extended','ij-retraites-fin-plafond-special',
        "Suppression du plafond spécial d'indemnisation maladie des actifs titulaires d'un avantage vieillesse.",
        "À l'âge fixé par décret et avec pension, rente ou allocation vieillesse : limite spéciale pour toute la période, sauf retraite progressive visée au second alinéa.",
        "Absence de limite spéciale liée à l'âge et à l'avantage vieillesse ; limites de droit commun et dérogations plus favorables maintenues.",
        'other','Assurés actifs titulaires des avantages vieillesse visés par la source, hors limitation déjà écartée pour retraite progressive.',
        "Journées d'incapacité à compter de l'entrée en vigueur, même arrêt antérieur ; journées anciennes et comptes de droit commun conservés.",
        "Aucune obligation substitutive, ni prestation automatique sans conditions médicales.",
        "Par dérogation à l'article L. 323-1, le nombre d'indemnités journalières dont peuvent bénéficier les personnes ayant atteint un âge déterminé et titulaires d'une pension, rente ou allocation de vieillesse servie par un régime de sécurité sociale ou par le régime des pensions civiles et militaires, ou par tout autre régime législatif ou réglementaire de retraite, ne peut dépasser une limite fixée par décret pour l'ensemble de la période pendant laquelle, ayant atteint cet âge, elles bénéficient de cet avantage.",
        "Les assurés concernés relèvent des conditions et limites de droit commun de l'article L. 323-1 et des dispositions plus favorables qui leur sont applicables.")],
    "Le second alinéa est une dérogation favorable : les personnes en retraite progressive relevant de L161-22-1-5 échappent au plafond spécial. Ce bénéfice n'est pas supprimé : la règle plus favorable s'étend désormais à tous les assurés visés pour l'avenir, et la dérogation reste expressément protégée pour les journées antérieures. Les autres avantages de retraite progressive ne sont pas modifiés.",
    repeal_scope="Suppression prospective de la limite particulière d'indemnités journalières liée à l'âge et à la perception d'un avantage vieillesse, avec application des limites ordinaires et conservation des droits anciens favorables.")

xml = sources[15]['source_xml']
xml = replace_once(xml,
    "sous réserve qu'après avis du médecin-conseil la durée de ces actions soit compatible avec la durée prévisionnelle de l'arrêt de travail. La caisse fait part de son accord à l'assuré et, le cas échéant, à l'employeur et au le médecin du travail.",
    "lorsque la durée de ces actions est compatible avec la durée prévisionnelle de l'arrêt de travail. Ce maintien de l'indemnité n'est soumis ni à un avis préalable du médecin-conseil ni à une autorisation distincte de la caisse. Les contrôles médicaux de droit commun demeurent applicables.")
xml = append_paragraph(xml,
    "La dispense d'avis et d'autorisation préalables s'applique aux actions commencées à compter de l'entrée en vigueur de la loi portant la présente modification, y compris pendant un arrêt antérieur ; elle s'applique également à la poursuite, après cette date, des actions en cours, sans nouveau dossier. Elle ne dispense ni de l'accord du médecin traitant ni, pour la rééducation professionnelle mentionnée au 2°, de la convention et des garanties prévues à l'article L. 5213-3-1 du code du travail. La durée d'une action ou d'une convention ne fixe pas le terme de l'emploi. Les conventions, droits acquis, indemnités et recours relatifs aux périodes antérieures conservent leur régime ; aucune autorisation déjà obtenue n'est à renouveler du seul fait de la réforme.")
rewritten(15, xml,
    "Réduction de fond : suppression du second examen préalable du médecin-conseil et de l'autorisation distincte de la caisse pour le maintien des indemnités pendant les actions de formation ou d'accompagnement. L'accord du médecin traitant, la compatibilité des durées, les catégories d'actions, l'essai encadré et la convention de rééducation sont conservés. Le contrat unique est coordonné sans transformer la durée de l'action en durée de l'emploi. La coquille source « au le » disparaît avec la phrase d'autorisation supprimée, non par changement de destinataire.",
    "L5213-3-1 fourni et lu : convention tripartite, rémunération maintenue, mise à disposition, indemnité après démission et déduction intégrale de la mise à disposition de l'essai restent distinctes du visa supprimé. L6313-1 lu comprend formation, bilan, validation d'acquis et apprentissage. R323-3-1 lu conserve les montants, le régime AT-MP après vingt-huit jours, la durée maximale distincte et le maintien de trois mois après certaines démissions ; son renvoi au quatrième alinéa vise le 2° de L323-3-1, dont la position logique est conservée. L433-1, L622-1 et D622-10-1 lus étendent ou adaptent ce dispositif : les exclusions des actions 1° et 2° pour les indépendants demeurent ; pas d'extension implicite. La suppression du visa doit être répercutée dans les procédures d'application, sans supprimer la convention ni les règles de sécurité de l'essai. Aucun nouveau renvoi à une cible absente du dossier de références n'est créé.",
    "La source cumule accord du médecin traitant, avis du médecin-conseil et accord de la caisse ; la proposition retire les deux derniers préalables pour le maintien des IJ. Le contrat tripartite de rééducation et les contrôles de fond restent nécessaires et sont conservés.",
    "Les montants et durées réglementaires d'indemnisation ne sont pas modifiés. Les régimes agricole, indépendant et AT-MP conservent leurs adaptations propres ; les coûts de traitement et effets de la dispense ne sont pas chiffrés.",
    "Aucune charge nouvelle identifiée : pas de déclaration, certificat ou accord substitutif ; accord du médecin traitant et compatibilité de durée existaient déjà. La convention de rééducation reste celle du droit existant, sans second avenant rétabli.",
    [effect('authorization_removed','formation-arret-fin-double-visa-medical',
        "Retrait de l'avis préalable du médecin-conseil et de l'autorisation distincte de caisse pour le maintien des IJ pendant les actions autorisées médicalement.",
        "Accord du médecin traitant, avis du médecin-conseil sur la durée puis accord de la caisse pour le maintien des IJ.",
        "Accord du médecin traitant et compatibilité de la durée, sans avis ni autorisation distincte préalables ; convention de rééducation maintenue.",
        'legal_duty','Assurés en arrêt souhaitant accéder aux actions de formation et accompagnement entrant dans le champ du texte.',
        "Actions nouvelles et poursuite des actions en cours après l'entrée en vigueur, même arrêt antérieur ; droits et conventions anciens préservés.",
        "Aucun visa de remplacement ; contrôles médicaux de droit commun et contrat tripartite de rééducation conservés.",
        "La caisse fait part de son accord à l'assuré et, le cas échéant, à l'employeur et au le médecin du travail.",
        "Ce maintien de l'indemnité n'est soumis ni à un avis préalable du médecin-conseil ni à une autorisation distincte de la caisse.")],
    "Le maintien des IJ pendant les formations et accompagnements, l'essai encadré, l'indemnisation de la rééducation et les garanties de L5213-3-1 restent ouverts aux situations futures éligibles. La suppression d'un avis préalable ne ferme aucune aide, n'abrège pas les indemnités spéciales et ne fait pas de la fin pédagogique un terme d'emploi.",
    removed=["L'avis préalable obligatoire du médecin-conseil sur la compatibilité de la durée des actions avec l'arrêt et l'autorisation distincte de la caisse pour le maintien des IJ sont supprimés, sans retirer l'accord du médecin traitant ni la convention de rééducation."])

xml = replace_once(sources[17]['source_xml'], 'Au cours de toute interruption de travail dépassant trente jours,', 'Au cours de toute interruption de travail, sans durée minimale préalable,')
xml = append_paragraph(xml,
    "La suppression de la durée minimale s'applique aux démarches engagées à compter de l'entrée en vigueur de la loi portant la présente modification, y compris au cours d'un arrêt déjà commencé. Elle n'impose ni visite supplémentaire systématique ni démarche nouvelle à l'assuré et ne modifie ni la durée de l'arrêt prescrit ni les conditions de son indemnisation. Les démarches et droits antérieurs conservent leurs effets.")
rewritten(17, xml,
    "Réduction de fond ciblée : suppression du seuil préalable de trente jours pour solliciter le médecin du travail en vue de préparer la reprise ou une formation. La démarche reste facultative pour le médecin-conseil, en liaison avec le médecin traitant ; l'assistance de l'assuré par une personne de son choix est maintenue. Aucun examen systématique n'est ajouté.",
    "D323-3 lu conserve encore un seuil de plus de trois mois et un renvoi ancien à R241-51 du code du travail ; il faut le coordonner avec l'ouverture sans seuil de cet article et identifier la concordance réglementaire du renvoi de préreprise. Cette incohérence préexistante n'est pas présentée comme déjà corrigée hors lot. Le délai de vingt jours du retour médical dans D323-3 n'est pas le préavis individuel de quinze jours. La source de décembre 2025 entre immédiatement en vigueur historiquement ; elle ne fixe pas la date de cette réforme.",
    "La source ne permet la sollicitation sur ce fondement qu'au-delà de trente jours ; la proposition permet une préparation plus précoce sans imposer de nouvelle visite. Il s'agit du retrait d'un seuil d'accès, non d'une réduction du délai de licenciement.",
    "La diminution effective des délais de retour à l'emploi et le coût d'éventuelles sollicitations plus précoces ne sont pas mesurés. La durée médicale de l'arrêt, les visites obligatoires distinctes et les procédures de rupture restent hors réforme.",
    "Aucune charge nouvelle identifiée : la sollicitation reste facultative, la liaison médicale et l'assistance existaient déjà ; le texte exclut expressément une visite systématique ou une démarche supplémentaire de l'assuré.",
    [effect('deadline_reduced','reprise-travail-preparation-sans-seuil',
        "Retrait du seuil de trente jours préalable à la sollicitation facultative du médecin du travail.",
        "Interruption de travail devant dépasser trente jours pour cette sollicitation.",
        "Sollicitation possible pendant toute interruption, sans minimum de jours ; aucune visite obligatoire nouvelle.",
        'calendar_days',"Assurés en interruption de travail et médecins préparant une reprise ou une formation.",
        "Démarches engagées après l'entrée en vigueur, même arrêt déjà commencé ; démarches anciennes maintenues.",
        "Aucune obligation systématique ; coût des sollicitations facultatives plus précoces inconnu.",
        "Au cours de toute interruption de travail dépassant trente jours,",
        "Au cours de toute interruption de travail, sans durée minimale préalable,")],
    "L'assuré conserve son droit d'être assisté par une personne de son choix. La préparation de sa reprise peut commencer plus tôt, sans nouvelle visite obligatoire, sans raccourcissement de son arrêt et sans réduction de ses IJ ou de ses garanties de santé.",
    removed=["Le minimum préalable de plus de trente jours d'interruption pour solliciter le médecin du travail sur ce fondement est supprimé."])

# L323-6 : les places 3°, 4° et 5° sont conservées.
xml = sources[19]['source_xml']
xml = replace_once(xml,
    "3° De respecter les heures de sorties autorisées par le praticien selon des règles et des modalités prévues par décret en Conseil d'Etat après avis de la Haute Autorité de santé ;",
    "3° Abrogé ;")
xml = replace_once(xml, "4° De s'abstenir de toute activité non autorisée ;",
    "4° De s'abstenir d'une activité rémunérée non autorisée par le praticien et de toute activité incompatible avec les prescriptions mentionnées au 1°. Les activités non rémunérées compatibles avec ces prescriptions ne sont soumises à aucune autorisation préalable ;")
xml = replace_once(xml, "5° D'informer sans délai la caisse de toute reprise d'activité intervenant avant l'écoulement du délai de l'arrêt de travail ;",
    "5° D'informer sans délai la caisse de toute reprise d'activité intervenant avant l'écoulement du délai de l'arrêt de travail, sauf lorsque l'employeur est subrogé dans les droits de l'assuré pour la période concernée ; dans ce cas, l'information incombe au seul employeur dans les conditions de l'article L. 323-6-1 ;")
xml = append_paragraph(xml,
    "La suppression du 3° et la dispense d'autorisation des activités non rémunérées compatibles avec les prescriptions s'appliquent aux comportements à compter de l'entrée en vigueur de la loi portant la présente modification, y compris pendant un arrêt antérieur. Les seules heures de présence au domicile ne peuvent plus conditionner le service de l'indemnité ; les prescriptions médicales individualisées, l'obligation de se soumettre aux contrôles et l'information de l'adresse de contrôle restent applicables. La dispense de déclaration de l'assuré en cas de subrogation s'applique aux reprises intervenant à compter de cette même date, sans nouvelle déclaration de remplacement. Les droits, créances et recours antérieurs sont conservés, sous réserve de l'application des dispositions répressives plus douces aux sanctions non définitives. Les dispositions favorables aux élus locaux demeurent applicables sans autorisation préalable, sauf avis contraire de leur praticien.")
rewritten(19, xml,
    "Réduction de fond de trois contraintes : suppression des heures générales de présence à domicile, retrait de l'autorisation préalable pour les activités non rémunérées compatibles avec les prescriptions et suppression de la déclaration de reprise par l'assuré lorsque l'employeur subrogé doit déjà déclarer. Les 1° à 6° restent à leur place ; le 3° porte son abrogation. Prescriptions, contrôles, adresse, déclaration hors subrogation, récupération pour manquement volontaire, sanctions des activités rémunérées irrégulières et exception des élus sont maintenus.",
    "R323-11-1 lu : présence de 9 h à 11 h et de 14 h à 16 h avec sorties libres motivées ; ses horaires et autorisations d'activités doivent être retirés dans le champ nouveau, sans supprimer les restrictions thérapeutiques individualisées. L315-2 IV garde les contrôles et leur sanction ; une absence à une plage abrogée ne doit pas être assimilée à un refus de contrôle. L133-4-1 et L114-17-1, lus dans le dossier, gardent restitution, rectification et garanties ; les pénalités ne peuvent reconstituer les obligations supprimées. L323-6-1 est coordonné dans ce lot pour l'employeur subrogé. L324-1 est également coordonné pour ne pas rétablir l'autorisation générale aux assurés ALD. L433-1 et L622-1, lus, renvoient à L323-6 : la réduction suit leur champ légal sous leurs adaptations propres, sans leur appliquer la réforme privée de rupture ni la capitalisation salariée. Aucun taux de cotisation n'est modifié.",
    "Trois obligations présentes dans la source entière sont réellement retirées ou fusionnées. Les contrôles et les conséquences d'une fraude ou d'une activité rémunérée non autorisée restent distincts ; les activités libres doivent respecter les prescriptions médicales.",
    "Le coût net de conformité et les effets sur les contrôles et indus ne sont pas établis. Les actes rémunérés, les prescriptions médicales et la notification de l'adresse de contrôle restent dans leur champ ; les sanctions historiques sont traitées sous réserve de la loi plus douce.",
    "Aucune charge nouvelle identifiée : l'employeur déclarait déjà la reprise en cas de subrogation, aucun nouveau registre ni justificatif d'activité libre n'est exigé. Les contrôles et l'adresse étaient déjà obligatoires ; aucune convocation nouvelle systématique n'est créée.",
    [effect('obligation_removed','arret-maladie-fin-horaires-domicile',
        "Suppression des heures générales de sorties et de présence au domicile, avec conservation des contrôles et prescriptions individualisées.",
        "Respect des heures de sorties autorisées selon le règlement, assorti de restitution en cas de manquement volontaire.",
        "3° abrogé ; aucune condition générale d'horaires à domicile ; prescriptions, contrôles et adresse conservés.",
        'legal_duty',"Bénéficiaires d'IJ entrant dans le champ de L323-6 et des renvois applicables.",
        "Comportements après l'entrée en vigueur, même arrêt antérieur ; réserve des sanctions non définitives plus douces.",
        "Aucun calendrier ou registre substitutif ; contrôles médicaux existants maintenus.",
        "3° De respecter les heures de sorties autorisées par le praticien selon des règles et des modalités prévues par décret en Conseil d'Etat après avis de la Haute Autorité de santé ;",
        "Les seules heures de présence au domicile ne peuvent plus conditionner le service de l'indemnité ; les prescriptions médicales individualisées, l'obligation de se soumettre aux contrôles et l'information de l'adresse de contrôle restent applicables."),
     effect('authorization_removed','arret-maladie-activites-gratuites-sans-visa',
        "Suppression de l'autorisation préalable générale pour les activités non rémunérées médicalement compatibles.",
        "Obligation de s'abstenir de toute activité non autorisée, sous réserve de la dérogation des élus locaux.",
        "Pas d'autorisation préalable des activités non rémunérées compatibles ; activité rémunérée soumise à autorisation et prescriptions toujours opposables.",
        'legal_duty',"Assurés indemnisés pratiquant une activité non rémunérée pendant leur arrêt.",
        "Comportements futurs même arrêt ancien ; dérogation des élus maintenue et dispositions répressives plus douces réservées.",
        "Aucune déclaration ou preuve périodique de l'activité libre ne remplace l'autorisation supprimée.",
        "4° De s'abstenir de toute activité non autorisée ;",
        "Les activités non rémunérées compatibles avec ces prescriptions ne sont soumises à aucune autorisation préalable ;"),
     effect('obligation_merged','reprise-anticipee-subrogation-declaration-unique',
        "Fusion des deux déclarations de reprise anticipée au profit de celle déjà due par l'employeur subrogé.",
        "Information sans délai due par le bénéficiaire au 5° et par l'employeur subrogé à L323-6-1 pour une même reprise.",
        "Employeur subrogé seul déclarant ; assuré déclarant dans les autres cas, avec même exigence de célérité.",
        'legal_duty',"Salariés en reprise anticipée et employeurs subrogés pour la période concernée.",
        "Reprises à compter de l'entrée en vigueur ; déclarations antérieures et indus anciens conservés.",
        "Aucune nouvelle charge patronale : la déclaration patronale existait déjà ; aucune attestation nouvelle du salarié.",
        "5° D'informer sans délai la caisse de toute reprise d'activité intervenant avant l'écoulement du délai de l'arrêt de travail ;",
        "dans ce cas, l'information incombe au seul employeur dans les conditions de l'article L. 323-6-1 ;")],
    "La dérogation favorable des élus locaux demeure : ils peuvent poursuivre leur mandat sauf avis contraire du praticien. Les activités non rémunérées compatibles deviennent libres pour tous les bénéficiaires futurs. Les droits sociaux, l'indemnisation médicale et les garanties de restitution et de recours ne sont pas réduits par l'abrogation des horaires.",
    removed=["L'obligation générale de respecter des heures de sorties et de présence à domicile pendant l'arrêt est supprimée sans calendrier de remplacement.",
             "L'autorisation médicale préalable de toute activité non rémunérée, même compatible avec les prescriptions, est supprimée.",
             "L'information distincte de la caisse par le salarié sur une reprise anticipée est supprimée lorsque l'employeur subrogé est déjà tenu de l'effectuer."])

xml = "<p>L'employeur subrogé dans les droits de son salarié en arrêt de travail informe par tout moyen l'organisme local d'assurance maladie assurant le service de l'indemnité journalière de la reprise anticipée du travail par ce salarié. Pour la période de subrogation concernée, cette information incombe au seul employeur ; le salarié est dispensé de la déclaration distincte prévue au 5° de l'article L. 323-6.</p><p>En cas de manquement par l'employeur à cette obligation et si ce manquement a occasionné le versement indu d'indemnités journalières, il peut être prononcé à son encontre une sanction financière dans les conditions prévues à l'article L. 114-17-1.</p><p>L'organisme d'assurance maladie procède à la récupération des indemnités journalières auprès de l'employeur dans les conditions prévues à l'article L. 133-4-1.</p><p>La déclaration unique s'applique aux reprises anticipées intervenant à compter de l'entrée en vigueur de la loi portant la présente modification. Les reprises antérieures, déclarations déjà effectuées, indus, prescriptions et recours correspondants conservent leur régime ; aucune déclaration ancienne n'est à refaire.</p>"
rewritten(20, xml,
    "Coordination nécessaire de la déclaration unique retenue au 5° de L323-6 : l'information de reprise déjà due par l'employeur subrogé devient expressément la seule déclaration pour la période concernée. L'article conserve la liberté de moyen, la causalité entre manquement et indu exigée pour la sanction et la récupération auprès de l'employeur. La suppression de la déclaration salariée est comptée une fois dans L323-6.",
    "L133-4-1 conserve rectification, voies de recours et conditions de recouvrement ; L114-17-1 conserve les sanctions patronales dans son champ et l'exception de bonne foi applicable aux manquements visés. La dispense du salarié n'est pas conditionnée au respect effectif de l'obligation par l'employeur : elle ne devient pas une nouvelle vigilance déclarative. La subrogation elle-même et les règles de maintien du salaire de R323-11, lu, ne sont pas modifiées. Le renvoi au 5° de L323-6 est nouveau dans cet article mais vise la source assignée et sa proposition lues intégralement ; il ne s'ajoute pas aux reference_checks requis. La date du 1er janvier 2017 appartient à la transition source.",
    "Cet article ne supprime pas une seconde obligation : il rend cohérente l'information patronale existante avec la dispense salariée opérée dans L323-6, sous une mesure commune. Sanction et récupération des indus demeurent.",
    "Pas d'effet supplémentaire de taux ou de montant ; la réduction de déclarations est attribuée à L323-6. Les reprises sans subrogation et le maintien du salaire restent hors de cette coordination.",
    "Aucune charge nouvelle identifiée : l'employeur devait déjà informer l'organisme par tout moyen. Le salarié n'a ni à vérifier l'envoi patronal ni à produire une attestation nouvelle pour être dispensé.",
    [effect('coordination','reprise-anticipee-subrogation-declaration-unique',
        "Coordination de l'obligation patronale existante avec la dispense de déclaration salariée de L323-6.",
        "L'employeur subrogé informe déjà la caisse, en parallèle de l'obligation générale du salarié.",
        "Même déclaration patronale, explicitement exclusive pendant la période de subrogation ; aucune seconde réduction comptée.",
        'legal_duty','Employeurs subrogés et leurs salariés en reprise anticipée.',
        "Reprises dès l'entrée en vigueur ; reprises antérieures, indus et recours conservés.",
        "Aucun nouveau délai, destinataire, donnée ni registre ; aucune sanction nouvelle.",
        "L'employeur subrogé dans les droits de son salarié en arrêt de travail informe par tout moyen l'organisme local d'assurance maladie assurant le service de l'indemnité journalière de la reprise anticipée du travail par ce salarié.",
        "Pour la période de subrogation concernée, cette information incombe au seul employeur ; le salarié est dispensé de la déclaration distincte prévue au 5° de l'article L. 323-6.")],
    "La subrogation et le maintien du salaire ne sont pas retirés. Les droits de défense et de rectification lors du recouvrement demeurent. La dispense nouvelle protège aussi les futurs salariés concernés sans attestation de transmission par leur employeur.",
    classification='coordination_only')

xml = "<p>Le présent article est abrogé pour les prescriptions d'arrêt de travail établies à compter de l'entrée en vigueur de la loi portant la présente abrogation.</p><p>Pour ces prescriptions, la seule circonstance qu'une suspension des indemnités journalières ait été décidée antérieurement ne subordonne plus la reprise du service des indemnités à un avis préalable systématique du service du contrôle médical. Les conditions médicales et administratives de droit commun, les contrôles, les décisions de suspension fondées sur la situation médicalement constatée et les recours demeurent applicables. Aucune indemnité n'est due du seul fait de l'abrogation pour une période dont l'absence de justification médicale est établie.</p><p>Les prescriptions antérieures, les décisions relatives aux périodes antérieures, les créances, restitutions, prescriptions et recours correspondants conservent leur régime. L'abrogation n'annule pas une suspension ancienne et ne vaut ni réouverture générale des périodes non indemnisées ni restitution générale.</p>"
rewritten(21, xml,
    "Abrogation de fond du visa préalable systématique après une suspension : une nouvelle prescription médicalement justifiée est soumise au droit commun, sans second verrou automatique au seul motif de sa proximité avec une suspension. Les contrôles médicaux et les suspensions fondées sur une absence de justification restent opposables ; la décision ancienne n'est pas effacée.",
    "D323-4 lu : le visa s'applique actuellement à une interruption dans les dix jours francs de la suspension et doit être rendu dans les quatre jours francs suivant réception de l'avis. Ce règlement doit être abrogé pour les nouvelles prescriptions, avec la même transition. L315-2 fourni dans le dossier général conserve les contrôles et suspensions de droit commun ; aucun renvoi nouveau à cet article n'est ajouté au corps. L622-1, lu, renvoie à L323-7 sous adaptations : retirer ce renvoi pour le futur sans fermer les IJ des indépendants ni modifier leur régime social. L'effet est un retrait d'autorisation, non une garantie de paiement automatique ni la fixation d'un nouveau délai de liquidation.",
    "Le préalable obligatoire du contrôle médical est réellement supprimé pour les nouvelles prescriptions rapprochées d'une suspension. Le bien-fondé médical, les décisions antérieures et les contrôles ordinaires subsistent ; aucune suppression d'indu n'est présumée.",
    "Les délais effectifs de paiement et les effets financiers ou antifraude ne sont pas mesurés. La réforme ne couvre pas les prescriptions antérieures ni les périodes dépourvues de justification médicale.",
    "Aucune charge nouvelle identifiée : pas de déclaration, certificat ou engagement supplémentaire en remplacement du visa ; la prescription ordinaire et les contrôles déjà prévus demeurent.",
    [effect('authorization_removed','ij-nouvelle-prescription-fin-visa-systematique',
        "Suppression du visa médical préalable automatique déclenché par la seule proximité d'une suspension d'IJ.",
        "Nouvelle prescription dans la période fixée par décret après suspension : reprise du paiement subordonnée à un avis préalable du contrôle médical.",
        "Nouvelle prescription sous droit commun, sans visa systématique du seul fait d'une suspension antérieure ; contrôles et suspensions justifiés conservés.",
        'legal_duty','Assurés recevant une nouvelle prescription après une décision de suspension des IJ.',
        "Prescriptions à compter de l'entrée en vigueur ; décisions et périodes antérieures sans annulation automatique.",
        "Aucune formalité substitutive ; le contrôle médical peut toujours exercer ses pouvoirs de droit commun.",
        sources[21]['source_xml'],
        "Pour ces prescriptions, la seule circonstance qu'une suspension des indemnités journalières ait été décidée antérieurement ne subordonne plus la reprise du service des indemnités à un avis préalable systématique du service du contrôle médical.")],
    "L'article source est un préalable restrictif, non une exonération ou une dispense favorable. Son retrait facilite les situations futures médicalement éligibles tout en préservant les droits et recours anciens ; il ne remplace pas une prestation par un avantage moins favorable.",
    repeal_scope="Suppression pour les nouvelles prescriptions du visa médical préalable systématique à la reprise des indemnités journalières après une suspension, sans effacement des décisions et périodes anciennes.")

xml = sources[22]['source_xml']
xml = replace_once(xml, "3° De s'abstenir de toute activité non autorisée ;",
    "3° De s'abstenir d'une activité rémunérée non autorisée et de toute activité incompatible avec les prescriptions mentionnées au 1°. Les activités non rémunérées compatibles avec ces prescriptions ne sont soumises à aucune autorisation préalable, sans préjudice de la faculté des élus locaux de poursuivre leur mandat dans les conditions prévues à l'article L. 323-6 ;")
xml = replace_once(xml, "en application des 3° et 4° de l'article L. 322-3 (1).", "en application des 3° et 4° de l'article L. 160-14.")
xml = replace_once(xml,
    "Sauf en cas d'urgence, le patient ou son représentant légal est tenu de communiquer son protocole au médecin consulté pour bénéficier de la limitation ou de la suppression de sa participation.",
    "Le patient ou son représentant légal peut communiquer son protocole au médecin consulté. L'absence de cette communication ne peut, à elle seule, faire obstacle au bénéfice de la limitation ou de la suppression de sa participation lorsque les conditions médicales et les droits correspondants sont établis.")
xml = replace_once(xml,
    "Le médecin, qu'il exerce en ville ou en établissement de santé, est tenu de certifier, lors de l'établissement des documents nécessaires au remboursement ou à la prise en charge, qu'il a pris connaissance du protocole et de se conformer aux dispositions réglementant la limitation ou la suppression de la participation de l'assuré.",
    "Le médecin, qu'il exerce en ville ou en établissement de santé, est tenu de se conformer aux dispositions réglementant la limitation ou la suppression de la participation de l'assuré. Il tient compte du protocole dont il a connaissance, sans avoir à certifier cette prise de connaissance lors de chaque établissement des documents nécessaires au remboursement ou à la prise en charge.")
xml = append_paragraph(xml,
    "La dispense d'autorisation des activités non rémunérées compatibles avec les prescriptions s'applique aux comportements à compter de l'entrée en vigueur de la loi portant la présente modification, y compris pour une affection reconnue antérieurement. La suppression de la communication obligatoire du protocole par le patient et de la certification répétée par le médecin s'applique aux actes et prestations réalisés à compter de cette même date, y compris sous un protocole antérieur. Les protocoles et décisions favorables existants conservent leurs effets, sans nouvelle demande ni certification de remplacement. L'établissement, la révision et l'examen médical du protocole restent applicables. Les droits, créances, restitutions et recours relatifs aux périodes antérieures conservent leur régime, sous réserve de l'application des dispositions répressives plus douces aux sanctions non définitives.")
rewritten(22, xml,
    "Réduction de fond : retrait de l'obligation personnelle de présenter le protocole pour chaque consultation et de la certification répétée de sa lecture par le médecin. Les droits et conditions médicaux doivent rester établis, mais l'absence de remise du protocole ne suffit plus à refuser l'exonération. La liberté des activités non rémunérées compatibles est coordonnée avec L323-6 pour éviter son rétablissement en ALD. Le renvoi obsolète L322-3 est expressément remplacé par L160-14 3° et 4°, sans modifier leurs critères. Protocole, révision, avis avec silence favorable, notification et obligations de soins sont conservés.",
    "L160-14 a été lu intégralement dans le corpus : ses 3° et 4° portent les ALD de liste et les affections graves ou multiples avec traitement prolongé et coûteux ; le renvoi source à L322-3 est introuvable dans ce corpus et ne doit pas subsister. Ce nouveau renvoi n'est pas une cible contractuelle à ajouter aux reference_checks ; sa source est LEGIARTI000054711279. L323-6 est lu dans le lot et coordonné pour les activités libres et la dérogation des élus. Aucun accès nouveau aux données médicales n'est créé ; le médecin utilise les informations légalement accessibles ou volontairement communiquées. R324-1 lu contient un renvoi à une expertise au deuxième alinéa qui n'apparaît pas dans le L324-1 fourni : incohérence préexistante à coordonner explicitement, sans faire disparaître les recours. Les formulaires et instructions doivent retirer la certification et la condition de présentation supprimées. Le coût de traitement et l'effet financier sur les droits auparavant refusés ne sont pas chiffrés.",
    "Deux formalités propres à l'exonération ALD disparaissent effectivement, au-delà du seul réemploi de données déjà permis par le CRPA. L'activité non rémunérée sans visa est la coordination de la mesure portée par L323-6 ; le protocole de soins et les conditions de l'exonération restent entiers.",
    "Les exonérations ne deviennent pas automatiques sans conditions médicales. Aucun coût net national ni ouverture de droits hors champ ALD n'est établi ; la coordination réglementaire et des formulaires reste nécessaire.",
    "Aucune charge nouvelle identifiée : pas de déclaration ou attestation substitutive, pas de nouveau partage de données. Le protocole, l'avis médical et la notification existent déjà ; la connaissance clinique n'est plus certifiée sur chaque remboursement.",
    [effect('obligation_removed','ald-protocole-fin-formalites-repetees',
        "Suppression de la présentation obligatoire du protocole par le patient et de la certification récurrente de lecture par le médecin.",
        "Hors urgence, communication du protocole obligatoire pour l'avantage ; certification de sa connaissance lors des documents de remboursement.",
        "Communication facultative ; aucune certification répétée ; protocole, décision et conditions médicales conservés.",
        'legal_duty','Patients en ALD, représentants légaux et médecins consultés en ville ou en établissement.',
        "Actes et prestations dès l'entrée en vigueur, même protocole ancien ; droits et décisions déjà favorables conservés.",
        "Aucun certificat ni dépôt substitutif ; aucun accès supplémentaire aux données médicales.",
        "Sauf en cas d'urgence, le patient ou son représentant légal est tenu de communiquer son protocole au médecin consulté pour bénéficier de la limitation ou de la suppression de sa participation.",
        "Le patient ou son représentant légal peut communiquer son protocole au médecin consulté."),
     effect('coordination','arret-maladie-activites-gratuites-sans-visa',
        "Coordination de l'obligation ALD pour ne pas rétablir l'autorisation des activités non rémunérées supprimée dans L323-6.",
        "Le 3° interdit toute activité non autorisée aux assurés relevant de la procédure ALD.",
        "Activités non rémunérées compatibles libres, avec maintien des prescriptions et de la dérogation des élus ; même mesure que L323-6.",
        'legal_duty','Assurés relevant du protocole et des conditions de L324-1.',
        "Comportements dès l'entrée en vigueur, même affection antérieure ; dispositions plus douces réservées.",
        "Aucune autorisation ou donnée de remplacement ; prescriptions et contrôle médical conservés.",
        "3° De s'abstenir de toute activité non autorisée ;",
        "Les activités non rémunérées compatibles avec ces prescriptions ne sont soumises à aucune autorisation préalable, sans préjudice de la faculté des élus locaux de poursuivre leur mandat dans les conditions prévues à l'article L. 323-6 ;"),
     effect('coordination','ald-renvoi-exoneration-l160-14',
        "Concordance explicite du fondement des exonérations ALD, sans nouvelle exonération comptée.",
        "Renvoi source aux 3° et 4° de L322-3, article absent du corpus actuel.",
        "Renvoi aux 3° et 4° de L160-14 correspondant aux mêmes catégories d'affections ; critères conservés.",
        'other','Assurés dont la participation est limitée ou supprimée au titre des ALD visées.',
        "Fondement actuel explicité ; décisions anciennes et futures favorables préservées.",
        "Aucune demande de reconnaissance nouvelle créée par la concordance.",
        "en application des 3° et 4° de l'article L. 322-3 (1).",
        "en application des 3° et 4° de l'article L. 160-14.")],
    "Les limitations ou suppressions de participation pour les ALD relevant des 3° et 4° de L160-14 restent ouvertes aux nouvelles affections éligibles. Le protocole périodiquement révisable, son adaptation aux progrès thérapeutiques, la durée recommandée, le silence médical favorable et la notification sont maintenus. L'exception d'urgence n'est pas perdue : la présentation devient facultative pour tous, y compris en urgence. Les décisions favorables antérieures ne sont pas à refaire ; l'absence de protocole remis ne suffit plus à priver un patient dont les droits sont établis de son avantage.",
    removed=["La présentation du protocole par le patient au médecin consulté comme condition particulière de l'exonération, hors urgence, est supprimée.",
             "La certification répétée par le médecin de sa prise de connaissance du protocole dans les documents de remboursement est supprimée.",
             "L'autorisation préalable générale des activités non rémunérées compatibles avec les prescriptions est écartée également dans la procédure ALD pour coordonner L323-6."])

xml = sources[23]['source_xml']
xml = replace_once(xml, "et qui en demandent le bénéfice dans un délai et selon des modalités déterminés par décret,",
    "et qui en demandent le bénéfice selon des modalités déterminées par décret, sans délai de forclusion,")
xml = replace_once(xml,
    "à condition qu'ils en fassent la demande dans un délai de deux ans à compter de la liquidation de leur pension ou de la publication de la loi n° 2016-1827 du 23 décembre 2016 de financement de la sécurité sociale pour 2017.",
    "sur demande, sans délai de forclusion lié à la date de liquidation de leur pension ou à la publication de la loi n° 2016-1827 du 23 décembre 2016 de financement de la sécurité sociale pour 2017.")
xml = append_paragraph(xml,
    "III.-La suppression des délais de forclusion prévus au 10° du II et pour les titulaires d'un avantage vieillesse relevant des 8° à 11° qui résident dans un autre Etat de l'Union européenne s'applique aux demandes présentées ou en cours à compter de l'entrée en vigueur de la loi portant la présente modification, pour les périodes de couverture courant à compter de cette date. Un refus antérieur fondé sur le seul dépassement d'un de ces délais ne fait pas obstacle à une nouvelle demande pour ces périodes. Les conditions de résidence, d'affiliation et de durée d'assurance, les prestations, les droits des membres de la famille et les dispositions plus favorables légalement applicables demeurent inchangés. Les affiliations et droits déjà reconnus sont maintenus, sans nouvelle demande. Les périodes antérieures, cotisations, créances, restitutions, prescriptions et recours correspondants conservent leur régime ; aucune restitution ou couverture rétroactive générale n'est instituée.")
rewritten(23, xml,
    "Réduction de fond ciblée de deux forclusions d'accès au régime complémentaire local : la demande du 10° et celle des retraités des 8° à 11° résidant dans un autre Etat de l'Union européenne ne sont plus enfermées dans un délai. Tous les I et II, onze catégories, extensions familiales a à c, durées d'affiliation, champs territoriaux et prestations sont repris intégralement hors ces deux restrictions. Le régime obligatoire et ses cotisations distinctes ne sont pas supprimés ; aucun contrat public n'est converti en contrat privé.",
    "D325-1-2 lu fixe à un an la demande du 10° : retirer cette forclusion en coordination, sans supprimer les voies de demande ni les assimilations favorables de R325-2 et R325-3, également lus. D325-1-3 organise le circuit existant ; aucune nouvelle pièce n'est ajoutée. L161-8, L161-9 et L311-5 fournis gardent le maintien des droits en espèces visé aux 4° et 5°. Les deux coquilles ou références anciennes de la source restent signalées : « règlement (CEE) n° 883/2004 » au 11° alors que le 5° indique CE ; loi 86-33 article 2 au 2° à confronter à la recodification publique hors corpus. Elles ne sont pas silencieusement transformées en contrat privé. La version assignée est marquée ABROGE_DIFF au 1er janvier 2028 : cette borne de version n'établit pas à elle seule l'abolition du régime ; la version succédant en 2028 n'est pas fournie et sa coordination reste à contrôler, sans prétendre l'avoir réécrite. Les prestations complémentaires et le forfait journalier ne sont pas des prélèvements fiscaux sur succession, même pour les titulaires de réversion. Incidence sur cotisations, prestations et équilibre local à chiffrer.",
    "La proposition retire effectivement deux délais susceptibles de fermer une couverture complémentaire pourtant ouverte sur le fond. Toutes les prestations, conditions d'affiliation matérielles, catégories et assimilations familiales de la source entière restent conservées, avec une ouverture future après ancien refus tardif.",
    "Pas de baisse de cotisation démontrée : l'affiliation obligatoire et son financement demeurent. Le coût de la couverture supplémentaire et la coordination de la version de 2028 restent à établir ; aucune couverture rétroactive générale n'est promise.",
    "Aucune charge nouvelle identifiée : la demande et les conditions matérielles existaient déjà ; aucune option, attestation, donnée ou contrôle supplémentaire n'est créé pour remplacer la forclusion. Les affiliations reconnues ne sont pas à redemander.",
    [effect('relief_extended','regime-local-demandes-sans-forclusion',
        "Suppression des forclusions de demande pour les retraités visés au 10° et les catégories 8° à 11° résidant dans un autre Etat de l'UE.",
        "10° : demande dans le délai fixé par décret ; retraités 8° à 11° dans un autre Etat UE : demande dans les deux ans de la liquidation ou de la publication de la loi de 2016.",
        "Demande sans forclusion liée à ces dates ; résidence, affiliation, durées d'assurance, prestations et financement restent distinctement applicables.",
        'legal_duty','Retraités remplissant les conditions du 10° et retraités des 8° à 11° résidant dans un autre Etat de l’Union européenne.',
        "Demandes nouvelles ou en cours pour couverture après l'entrée en vigueur ; nouvelle demande permise après refus tardif, sans réouverture générale du passé.",
        "Demande existante conservée sans nouveau justificatif ni déclaration périodique.",
        "Le régime local est applicable aux titulaires d'un avantage vieillesse relevant des 8°, 9°, 10° et 11° qui résident dans un autre Etat de l'Union européenne, à condition qu'ils en fassent la demande dans un délai de deux ans à compter de la liquidation de leur pension ou de la publication de la loi n° 2016-1827 du 23 décembre 2016 de financement de la sécurité sociale pour 2017.",
        "Le régime local est applicable aux titulaires d'un avantage vieillesse relevant des 8°, 9°, 10° et 11° qui résident dans un autre Etat de l'Union européenne, sur demande, sans délai de forclusion lié à la date de liquidation de leur pension ou à la publication de la loi n° 2016-1827 du 23 décembre 2016 de financement de la sécurité sociale pour 2017.")],
    "Les prestations complémentaires du I, la possibilité de prise en charge du forfait journalier, les onze catégories du II, les maintiens de droits, les régimes frontaliers, les variantes cinq ans ou dix sur quinze, les soixante trimestres, les anciens salariés du Port autonome de Strasbourg et les droits familiaux a, b, c sont intégralement préservés. Les assimilations réglementaires de réversion et d'ayant droit restent favorables. Les futurs retraités matériellement éligibles peuvent demander le régime sans forclusion ; les bénéficiaires déjà affiliés n'ont rien à refaire. La suppression des délais ne supprime aucune exonération ni dispense de cotisation existante.",
    removed=["Le délai de forclusion réglementaire imposé aux titulaires d'un avantage vieillesse relevant du 10° du II pour demander le régime local est supprimé.",
             "Le délai de deux ans lié à la liquidation de la pension ou à la publication de la loi de 2016, pour les titulaires des 8° à 11° résidant dans un autre Etat de l'Union européenne, est supprimé."])

retained(0,
    "Maintien intégral nécessaire après examen : la transmission limitée des informations d'arrêt au service de prévention permet de prévenir la désinsertion professionnelle, sous accord de l'assuré. Elle est effectuée par l'organisme ou le contrôle médical, sans dossier supplémentaire imposé au salarié. Supprimer le consentement, la limitation des données ou l'avis CNIL retirerait une protection de santé ou de confidentialité ; aucun doublon déclaratif autonome n'est établi dans cet article.",
    "L4622-2 lu dans le corpus : prévention, maintien dans l'emploi et conseil sanitaire, sans pouvoir de rupture du contrat. Le renvoi au II de L1110-4 du code de la santé publique est conservé pour son champ de partage médical ; sa source externe au corpus des cinq codes n'est pas fournie et aucune réécriture n'en est revendiquée. La date du 1er janvier 2024 est une entrée historique. Le préavis privé de quinze jours et les indemnités ordinaires ne gouvernent ni l'accord de transmission ni l'affiliation au service de santé.",
    "Aucune modification par rapport à la source officielle entière : maintien d'un échange sanitaire ciblé et consenti nécessaire à la prévention, sans compter sa conservation comme réduction de charge.",
    "Le coût des échanges n'est pas mesuré et l'absence de doublons dans l'ensemble des systèmes n'est pas démontrée ; l'article n'autorise aucune baisse de cotisation ni suppression de contrôle sanitaire.",
    "Aucune charge nouvelle identifiée puisque le corps source est intégralement conservé ; aucune collecte, donnée, attestation de consentement supplémentaire ou échéance n'est ajoutée.",
    "L'accord de l'assuré, la prévention de sa désinsertion et les garanties de transmission confidentielle sont préservés pour les futurs arrêts. Il n'existe ici ni taxe, ni réduction fiscale à supprimer ; la réforme du contrat unique ne ferme pas le bénéfice de cette prévention.")

retained(1,
    "Maintien intégral nécessaire : l'article constitue le fondement même des indemnités maladie en cas d'incapacité médicalement constatée. Les compétences du médecin, de la sage-femme et du chirurgien-dentiste ainsi que l'exception favorable pour certaines cures thermales sont conservées. L'exigence d'une incapacité et d'une prescription authentifiée protège le bénéficiaire et le financement social ; elle ne peut être supprimée comme simple formalité. Aucun prélèvement ni déclaration en double n'est institué par cet article.",
    "L162-4-1 1° est fourni : motivation médicale, plafond réglementaire ne pouvant être inférieur à un mois initialement ou à deux mois pour prolongation, et dérogation motivée restent à leur champ. D323-1 lu conserve le bénéfice des IJ de cure pour les ressources inférieures au plafond majoré de 50 % selon les personnes à charge ; il ne doit pas être fermé par le maintien de la réserve générale. L6316-1 troisième alinéa du code de la santé publique est un renvoi source non fourni en texte intégral ; aucune extension de téléprescription ou conformité supérieure nouvelle n'est affirmée. La note du 31 décembre 2025 est historique.",
    "Aucun changement de la règle officielle entière : ouverture des IJ conservée dans toutes ses qualifications médicales, avec sa dérogation thermale et sans nouvelle autorisation ou baisse de prélèvement revendiquée.",
    "Le texte ne règle ni le taux des IJ ni l'indemnité de rupture. La source intégrale du renvoi sanitaire extérieur au corpus reste à contrôler ; aucune économie ou extension de couverture n'est chiffrée.",
    "Aucune charge nouvelle identifiée : aucune modification du corps, de la signature, de la durée, des données médicales ou des conditions de ressources n'est introduite.",
    "La possibilité de faire constater l'incapacité par la sage-femme ou le chirurgien-dentiste dans leurs compétences et l'exception pour les cures justifiées restent ouvertes aux situations futures éligibles. La règle ne réserve aucun droit aux contrats anciens ni à une durée minimale d'emploi nouvelle.")

retained(3,
    "Maintien intégral nécessaire : examen de santé gratuit avec droit de le demander en cas de carence de la caisse, coordination explicite contre le double emploi avec d'autres visites et information des jeunes ciblés. La charge est une mission d'accès à la prévention, pas un dossier administratif imposé au patient. Le texte prévoit déjà l'évitement des doublons ; aucune suppression additionnelle démontrée ne justifie de réécrire cette garantie.",
    "L6221-1, L6325-1 1° et L6313-1 ont été lus dans le corpus : l'apprentissage et la professionnalisation restent des objets de formation accessibles dans le contrat unique, avec information sur l'examen. Une durée pédagogique ne termine pas l'emploi. La note renvoie à L371-6 : sa dernière phrase exclut seulement les titulaires de pension militaire bénéficiaires de l'indemnité de soins auxquels tout travail est interdit, non tous les pensionnés militaires. Les articles extérieurs relatifs aux écoles, service civique et service militaire adapté restent des renvois source, non des contrats privés nouvellement vérifiés dans leur code respectif.",
    "L'examen intégral ne révèle pas de formalité personnelle inutile à retirer : gratuité, droit de sollicitation, information et prévention des doubles examens sont maintenus, sans nouvelle simplification comptabilisée.",
    "La réduction concrète des doubles examens dépend de l'application réglementaire et n'est pas démontrée ici. Le régime militaire et les autres formes de volontariat gardent leur champ propre.",
    "Aucune charge nouvelle identifiée : le texte source demeure entier et n'ajoute aucun bilan, transmission, justificatif ni examen systématique de remplacement.",
    "L'examen demeure gratuit pour l'assuré et sa famille, le droit de le demander est conservé et tous les groupes de jeunes informés restent couverts pour l'avenir. La prévention des doubles emplois est un avantage existant, non une nouvelle dispense créée dans le lot.")

retained(6,
    "Maintien intégral nécessaire du cadre conventionnel national des transports sanitaires : négociation avec les organisations représentatives, durée au plus égale à cinq ans, obligations réciproques, contrôles, conditions de conventionnement, financement des instances, détermination des sommes et rémunération de la garde. Les contrôles de sécurité et de facturation et les droits à rémunération ont une fonction essentielle ; aucune déclaration périodique ou autorisation individuelle redondante n'est créée directement par cet article.",
    "L322-5-4 et L162-15, lu, organisent approbation et garanties ; L162-14-1 I, lu intégralement, confirme la borne de cinq ans. La rémunération de garde du 6° est préservée ; le dernier alinéa de L6312-5 du code de la santé publique est un renvoi source extérieur dont le texte n'est pas fourni ici. La suppression des critères territoriaux propres aux taxis de L322-5 ne vaut pas abolition de la convention des ambulanciers. L'examen du contenu de chaque annexe annuelle hors source n'est pas revendiqué.",
    "Aucune réduction par rapport à la source entière : le cadre garantit prestations rémunérées et contrôles de la dépense, sans obligation personnelle nouvelle à fusionner dans cet article.",
    "Les frais des instances et les éventuels doublons contenus dans les conventions et leurs annexes ne sont pas chiffrés ni audités par ce maintien. Aucune suppression de tarif ou d'agrément sanitaire distinct n'est prétendue.",
    "Aucune charge nouvelle identifiée : les six rubriques et la durée maximales de la source sont conservées sans ajout de déclaration, registre, avis ni délai.",
    "Les conditions de rémunération, y compris la participation à la garde départementale et la détermination conventionnelle des sommes dues, restent applicables aux situations futures. Aucun avantage tarifaire ou financier n'est fermé au motif de la réforme des taxis ou du contrat unique.")

retained(7,
    "Maintien intégral nécessaire : la convention des transports sanitaires doit être opposable dans le cadre protecteur d'approbation de L162-15, et les assurés utilisant une entreprise non conventionnée conservent une base de remboursement fixée par arrêté. Il ne s'agit pas d'une seconde autorisation d'exercer ; retirer cette articulation sans autre fondement fragiliserait les tarifs opposables et la couverture des patients.",
    "L162-15 a été lu intégralement : approbation réputée acquise après vingt et un jours sous réserves précises, oppositions représentatives, publication et mécanismes conventionnels. Le renvoi de L322-5-4 vise le cadre sanitaire, sans rapport avec les majorités des accords d'entreprise de L2232. L322-5-2 demeure entier dans le lot. Aucun ancien préavis professionnel n'est réintroduit par la durée de la convention. L'arrêté tarifaire des entreprises non conventionnées n'est pas joint et n'est pas déclaré réécrit.",
    "Maintien sans modification de l'approbation protectrice et de la base de remboursement hors convention ; aucune suppression de charge ou baisse tarifaire démontrée dans cet article.",
    "Les tarifs des arrêtés et les conventions externes ne sont pas évalués dans ce maintien. L'approbation de santé publique reste distincte d'un agrément professionnel ou d'une autorisation de rupture du travail.",
    "Aucune charge nouvelle identifiée : mêmes renvois et mêmes compétences, sans nouvelle procédure, pièce, déclaration, délai ou visa de remplacement.",
    "La base de remboursement des entreprises non régies par la convention reste disponible pour les futurs transports. Les effets conventionnels et garanties d'accès aux soins ne sont pas retirés au prétexte de supprimer une approbation nécessaire à leur opposabilité.")

retained(8,
    "Maintien intégral nécessaire du renvoi aux sanctions conventionnelles : les violations de tarifs, facturations ou engagements licites des transporteurs doivent rester contrôlables, avec défense. Ce texte ne crée pas un rapport ou un agrément supplémentaire. Les clauses territoriales rendues inopposables par la proposition de L322-5 ne peuvent plus constituer un engagement sanctionnable pour l'avenir ; aucune réécriture générale du dispositif antifraude n'est justifiée ici.",
    "L162-15-1 lu intégralement dans le corpus, version du 27 juin 2026 : observations du professionnel, suspension d'urgence, fraude grave répétée sur cinq ans, seuil de huit plafonds mensuels et possibilité de plan d'apurement sont distincts du conventionnement territorial supprimé. L322-5 et L322-5-2 restent des supports conventionnels actifs dans le lot ; le premier neutralise expressément les clauses nouvelles illicites. La cible requise L321-1 ne porte pas sur ces sanctions mais sur l'incapacité ouvrant droit aux IJ ; elle n'est pas artificiellement traitée comme un renvoi direct du présent article.",
    "Aucune modification de la source entière : maintien d'un recours aux sanctions des engagements conventionnels subsistants, avec exclusion juridique des clauses supprimées par L322-5, sans nouvelle sanction comptée.",
    "Le contenu de chaque convention n'est pas audité ni l'effet des sanctions chiffré. L'article ne rend pas les besoins territoriaux supprimés à nouveau opposables et ne réforme pas l'assurance chômage.",
    "Aucune charge nouvelle identifiée : le renvoi existant reste entier, sans nouvelle pénalité, transmission ni condition de conventionnement ajoutée.",
    "Aucune exonération de taxe n'est présente dans cet article. Les droits de défense et possibilités favorables prévues par le régime de sanctions, notamment le plan d'apurement permettant le retour au conventionnement dans son champ, restent disponibles ; les avantages de remboursement ne sont pas fermés par le maintien du contrôle.")

retained(9,
    "Maintien intégral nécessaire du champ de la prestation de prothèse dentaire : appareils fonctionnels et thérapeutiques, ou nécessaires à l'exercice d'une profession. La conjonction entre les deux premières qualifications et l'alternative professionnelle sont conservées exactement ; elles ne deviennent ni trois voies indépendantes ni trois exigences cumulatives. La limitation distingue le soin assuré des demandes dépourvues de finalité couverte ; sa suppression élargirait la prestation sans démonstration médicale ni financière, plutôt que supprimer un doublon.",
    "Aucun taux, plafond monétaire ni délai d'emploi n'est fixé dans cette source. Le caractère nécessaire à l'exercice d'une profession est une voie de couverture, pas une ancienneté de contrat ni une condition de quinze jours. Les nomenclatures de soins et dispositifs dentaires extérieurs à ce seul article ne sont pas déclarés revus. Les membres de la famille sont expressément conservés.",
    "Aucune modification de la norme officielle entière : maintien des appareils fonctionnels et thérapeutiques ou nécessaires à l'exercice d'une profession, avec la même articulation des qualifications et sans prélèvement supplémentaire créé.",
    "Le contenu des nomenclatures et le reste à charge effectif ne sont pas évalués ici. L'absence de chiffrage ne permet pas de présenter une extension indifférenciée aux demandes non thérapeutiques comme une économie.",
    "Aucune charge nouvelle identifiée : le texte source reste entier, sans procédure ou critère de nécessité additionnel et sans modification des deux branches de couverture.",
    "Les appareils fonctionnels et thérapeutiques, ou nécessaires à l'exercice d'une profession, restent couverts dans le champ exact de la source pour l'assuré et sa famille, y compris pour les situations futures éligibles. La conjonction et l'alternative sont conservées ; aucun fondement favorable n'est effacé ou réduit à un droit ancien.")

retained(10,
    "Maintien intégral nécessaire des bornes d'indemnisation maladie : paiement de chaque jour ouvrable ou non, durée maximale, période propre à chaque affection longue et plafond pour les autres affections. Les durées déterminent l'articulation avec la couverture de longue maladie et d'invalidité ; supprimer sans coordination toutes ces limites créerait une prestation différente sans financement établi. Les dérogations favorables sans carence restent expresses et intactes dans les articles suivants. Il n'existe pas de double déclaration dans cet article.",
    "R323-1 lu, version du 19 septembre 2026 : départ au quatrième jour, carence au seul premier arrêt d'une même ALD, périodes trois ans ou un an selon exonération, reprise d'un an et plafond 360 IJ sur trois ans. Sa note du 15 octobre 2026 conserve le régime antérieur plus favorable pour les situations qu'elle définit : ne pas le supprimer par une réécriture de principe. L323-1-1, L323-1-2 et L323-3 sont maintenus dans le lot. L324-1 conserve son protocole et la concordance des exonérations est corrigée dans ce lot. Aucun délai médical n'est aligné sur le préavis individuel de quinze jours.",
    "Aucun changement par rapport à la source entière ; les bornes et dérogations de la prestation sont maintenues, sans assimilation d'un maintien utile à une simplification ou une baisse de prélèvement.",
    "Les dépenses d'IJ et les droits d'invalidité ne sont pas chiffrés. La réforme ne décide pas une suppression générale de la carence maladie ; les exceptions favorables et transitions réglementaires continuent de s'appliquer.",
    "Aucune charge nouvelle identifiée : aucune modification des périodes, du calcul de date à date, des conditions de reprise ou du nombre maximal n'est créée par le maintien intégral.",
    "Les jours non ouvrables restent indemnisables, le calcul séparé par affection et le redémarrage après reprise sont conservés. Les dispenses de carence pour deuil, interruptions de grossesse et temps partiel thérapeutique demeurent ouvertes à l'avenir ; aucune transition favorable de R323-1 n'est fermée.")

retained(11,
    "Maintien intégral nécessaire de l'indemnisation sans carence pour la première incapacité dans les treize semaines suivant le décès d'un enfant de moins de vingt-cinq ans ou d'une personne de cet âge à charge effective et permanente. Les bornes définissent l'avantage sans introduire de formalité autonome ; leur conservation ne doit pas être comptée comme une nouvelle baisse. La réforme de suppression des droits de succession ne supprime pas une protection sociale liée au deuil.",
    "L323-1 est maintenu intégralement : son premier alinéa conserve la carence générale, ce qui rend la dérogation cohérente et nécessaire. La date du 1er juillet 2020 vise les décès couverts historiquement et n'est pas la date de la présente réforme. Le délai de treize semaines n'est pas une durée d'emploi et la première incapacité ne dépend pas du seuil d'un an d'indemnité ordinaire de rupture.",
    "Aucun changement de la source officielle entière : maintien de l'exemption de carence, de ses deux catégories de bénéficiaires et de son application à la première incapacité couverte.",
    "Le coût du maintien n'est pas calculé ; aucune extension à un décès hors des conditions légales ni effet sur les donations ou l'impôt successoral n'est revendiqué.",
    "Aucune charge nouvelle identifiée : même dérogation, mêmes treize semaines et seuil de moins de vingt-cinq ans ; aucune déclaration, attestation ou autorisation supplémentaire ajoutée.",
    "L'avantage est la suppression de carence pour la première incapacité de travail dans les treize semaines suivant le décès visé. Il demeure entier pour les décès futurs éligibles, pour l'enfant comme pour la personne à charge effective et permanente. Aucune nouvelle condition d'ancienneté, de contrat ou de succession n'en restreint l'accès.")

retained(12,
    "Maintien intégral nécessaire de la dispense de carence après interruption spontanée de grossesse avant la vingt-deuxième semaine d'aménorrhée ou interruption pour motif médical. L'incapacité doit être constatée, mais l'article n'ajoute ni agrément ni déclaration redondante. Retirer ses conditions sans motif modifierait le champ médical ; supprimer la dérogation elle-même serait défavorable alors que la carence générale est conservée.",
    "L323-1 premier alinéa et L321-1 sont maintenus : la dérogation supprime le délai, pas la constatation d'incapacité ni la compétence professionnelle. Les articles L2213-1 à L2213-5 du code de la santé publique sont des renvois source non fournis en texte intégral, non un régime de CDD. La note donne une mise en œuvre au plus tard le 1er juillet 2024, qu'il ne faut pas repousser à une réforme future. Le seuil de vingt-deux semaines concerne la branche spontanée, non une limite nouvelle des interruptions pour motif médical.",
    "Aucune modification de la source officielle entière : l'indemnisation sans carence dans les deux branches médicales reste intégralement conservée, sans réduction nouvelle revendiquée.",
    "Aucun coût ni droit nouveau hors champ médical n'est évalué ; les textes sanitaires extérieurs conservent leurs conditions et ne sont pas présentés comme réécrits.",
    "Aucune charge nouvelle identifiée : aucun certificat de remplacement, délai de demande, seuil d'emploi ou nouvelle autorisation n'est introduit dans le corps maintenu.",
    "La dispense de délai des IJ est conservée pour les interruptions spontanées avant vingt-deux semaines et celles pratiquées pour motif médical selon les articles cités. Elle demeure accessible pour les futurs arrêts éligibles sans condition d'un an d'emploi ni fermeture aux titulaires du contrat unique.")

retained(14,
    "Maintien intégral nécessaire de l'indemnisation du temps partiel thérapeutique : amélioration de la santé ou rééducation/réadaptation vers un emploi compatible, absence de carence et calcul réglementaire. Ces critères justifient une prestation pour perte de revenu médicalement liée ; ils ne doublonnent pas une procédure de rupture. L'article ne pose ni plancher de vingt-quatre heures ni terme automatique d'emploi à supprimer.",
    "R323-3 lu conserve le plafond égal à la perte de gain journalière et la durée de maintien dans son champ, avec les transitions favorables du décret de septembre 2026. L323-1 et L321-1 restent actifs dans le lot ; le premier alinéa de L323-1 porte bien le délai écarté ici. Les conditions des deux cas, 1° et 2°, ne sont pas transformées en exigences cumulatives. Aucune modification d'heures supplémentaires ni de durée contractuelle n'est opérée par l'expression temps partiel thérapeutique.",
    "Aucun changement de la source officielle entière : maintien d'un dispositif médical favorable et de sa dispense de carence, sans prétendre qu'un renvoi maintenu crée une réduction de cotisation.",
    "L'effet financier et l'organisation du temps partiel ne sont pas chiffrés ; les durées et montants réglementaires, ainsi que les adaptations d'autres régimes, restent distincts.",
    "Aucune charge nouvelle identifiée : les deux voies, le calcul et la dispense de délai sont conservés sans nouvelle déclaration, autorisation, durée minimale ni justificatif.",
    "Le service des IJ en temps partiel thérapeutique et l'absence de carence restent applicables aux situations futures dans les deux cas prévus. Aucune condition de durée de contrat ou d'indemnité ordinaire de licenciement n'est ajoutée ; les transitions réglementaires plus favorables ne sont pas fermées.")

retained(16,
    "Maintien intégral nécessaire de la base de calcul des indemnités : revenus d'activité soumis à cotisations antérieurs à l'interruption, plafond, valeur journalière, dernières payes et renvoi réglementaire pour fraction et modalités. Cette règle donne un fondement déterminable à la prestation ; supprimer plafond ou référence salariale sans dispositif coordonné serait une extension indéfinie, pas le retrait d'un doublon. Aucun taux supplémentaire ni formalité personnelle n'est fixé ici.",
    "La note conserve la transition des arrêts prescrits à partir du 1er juillet 2020 et de ceux prescrits antérieurement qui n'avaient pas atteint trente jours consécutifs à cette date. Ni cette durée historique ni les dernières payes ne sont le seuil d'un an de rupture ou son salaire de référence. Le taux de CSG salariale et les transferts vieillesse relèvent d'autres articles ; ils ne modifient pas silencieusement la fraction ou le plafond des IJ. Les renvois reçus à la rupture privée sont des contrôles de champ, non des renvois directs du présent corps.",
    "Aucune modification de la source entière : conservation de la règle de calcul qui rend les IJ liquidables ; aucune baisse de prélèvement ou simplification de données n'est démontrée par ce maintien.",
    "Les paramètres réglementaires et les effets des baisses de CSG ou transferts vieillesse ne sont pas chiffrés par cet article. Pas d'alignement du salaire de référence des IJ sur celui de l'indemnité de rupture.",
    "Aucune charge nouvelle identifiée : le corps source n'est pas modifié ; aucune nouvelle assiette, déclaration salariale, attestation ou transmission n'est introduite.",
    "La référence aux dernières payes et aux revenus effectivement soumis à cotisations, ainsi que les situations historiquement protégées par la note, restent intégralement conservées. Aucun avantage d'IJ ni régime de calcul favorable n'est retiré pour financer les réformes de prélèvements prévues ailleurs.")

retained(18,
    "Maintien intégral nécessaire de la protection des indemnités journalières contre la saisie et la cession au-delà des conditions et limites applicables aux rémunérations. La contrainte pèse sur l'exécution forcée et protège les moyens de subsistance du malade ; elle ne constitue ni taxe accessoire ni formalité redondante à supprimer. Retirer la limitation serait défavorable à l'assuré sans baisse démontrée de prélèvement.",
    "La source ne vise aucun montant fixe ni renvoi à L1234-9 : les plafonds de six mois de l'indemnité ordinaire de rupture ne s'appliquent pas à la saisissabilité des IJ. Les procédures de saisie des rémunérations hors des cinq codes et leurs éventuelles évolutions restent à leur champ propre ; aucune réécriture ni suppression de procédure judiciaire n'est revendiquée ici. Les droits des créanciers restent ceux du droit applicable aux rémunérations.",
    "Aucun changement par rapport à la source officielle entière : maintien de la protection légale de la prestation sans l'assimiler à une nouvelle dispense ou à une baisse de cotisation.",
    "La quotité saisissable et les effets des procédures extérieures ne sont pas chiffrés ni redéfinis. La protection n'est pas une immunité absolue contre toute saisie ou cession.",
    "Aucune charge nouvelle identifiée : mêmes conditions et limites légales, sans certificat d'insaisissabilité, déclaration ou autorisation préalable ajouté.",
    "L'assuré conserve pour l'avenir la protection des IJ dans les conditions et limites de saisie des rémunérations. Cet avantage de subsistance n'est pas retiré et n'est pas confondu avec l'indemnité de licenciement ou son plafond ; aucun droit nouveau n'est présenté comme déjà créé.")

# Contrôles de renvois : les trois cibles de travail sont des vérifications de champ,
# et non des renvois directs fictifs dans les articles d'assurance maladie.
contexts = {
 0: "L315-4 organise le partage consenti d'informations pour prévenir la désinsertion.",
 1: "L321-1 ouvre les IJ pour incapacité médicalement constatée, indépendamment de la rupture d'emploi.",
 3: "L321-3 garantit un examen gratuit et l'information des apprentis et jeunes en professionnalisation.",
 4: "L322-5 règle le remboursement du transport prescrit et le conventionnement des taxis.",
 8: "L322-5-5 vise les engagements conventionnels des transporteurs et leurs sanctions.",
 10: "L323-1 fixe les périodes d'indemnisation de maladie et la carence générale avec ses dérogations.",
 11: "L323-1-1 écarte la carence pour le premier arrêt dans les treize semaines du deuil visé.",
 12: "L323-1-2 écarte la carence après les interruptions de grossesse qu'il définit.",
 13: "L323-2 retire ici le plafond spécial d'IJ des titulaires d'avantages vieillesse, pas les règles ordinaires.",
 14: "L323-3 maintient les IJ et la dispense de carence pendant un temps partiel thérapeutique.",
 15: "L323-3-1 maintient les IJ pendant les actions compatibles de formation et de rééducation.",
 16: "L323-4 détermine le revenu journalier antérieur de référence des IJ.",
 18: "L323-5 protège les IJ dans les limites de saisie des rémunérations.",
 19: "L323-6 définit les obligations pendant l'arrêt médical et retire horaires, visa d'activités gratuites et déclaration salariée en cas de subrogation.",
 20: "L323-6-1 coordonne l'information de reprise anticipée déjà due par l'employeur subrogé.",
 21: "L323-7 supprime le visa automatique de reprise des IJ pour les nouvelles prescriptions après suspension.",
 23: "L325-1 conserve les catégories privées et publiques du régime local et retire seulement des forclusions de demande.",
}
special_checks = {
 (1, 'L162-4-1'): "Le 1° vise les motifs médicaux et la durée de l'arrêt, y compris sages-femmes et dentistes, avec plafonds réglementaires d'au moins un mois initial et deux mois en prolongation, et dépassement justifié. Le maintien de L321-1 garde toutes ces conditions et exceptions ; la proposition fournie ne constitue pas une règle déjà en vigueur.",
 (3, 'L371-6'): "La cible conserve les soins des pensionnés militaires, la dispense de participation pour les affections non militaires et des IJ dans leurs conditions propres. Sa dernière phrase exclut le titre II pour les titulaires de l'indemnité de soins auxquels tout travail est interdit ; la note de L321-3 ne doit pas être lue comme excluant tous les pensionnés de l'examen gratuit.",
 (4, 'L162-4-1'): "Le renvoi vise le 2°, justification médicale du déplacement et du mode de transport, ainsi que l'identification et l'authentification du prescripteur. Les plafonds de durée du 1° concernent les arrêts de travail, non les transports ; le retrait du coefficient de minoration et du filtre territorial ne supprime pas cette prescription médicale.",
 (8, 'L321-1'): "Cette cible définit le droit aux IJ pour incapacité constatée et n'est pas citée directement par L322-5-5. Le renvoi réellement opérant de celui-ci est L162-15-1, lu séparément dans le corpus pour les sanctions conventionnelles ; aucun délai d'arrêt ou seuil d'ancienneté n'est artificiellement appliqué aux transporteurs.",
 (10, 'L321-1'): "Le renvoi de L323-1 reprend bien l'indemnité due en raison de l'incapacité physique médicalement constatée, avec compétences des trois professions et exception thermale. Les bornes de durée et de carence de L323-1 ne modifient ni la compétence de constatation ni la dérogation de cure ; les deux articles sont maintenus dans ce lot.",
 (11, 'L323-1'): "Le premier alinéa de la cible porte la carence générale à laquelle le deuil déroge. L323-1 est maintenu intégralement dans le lot : l'exemption de délai de L323-1-1 reste donc opérante pour la première incapacité dans les treize semaines, sans ancienneté d'un an ni délai de notification de rupture.",
 (12, 'L323-1'): "Le renvoi au premier alinéa vise la carence maladie, conservée dans ce lot. La dérogation après interruption de grossesse écarte ce seul délai ; elle ne supprime pas les autres durées maximales et n'est subordonnée ni à une année de services ni au préavis de rupture.",
 (12, 'L321-1'): "La cible reste le fondement des IJ pour incapacité de poursuivre ou reprendre le travail, avec constatation médicale dans le champ des prescripteurs compétents. L323-1-2 supprime uniquement le délai, pas l'incapacité ; la condition des vingt-deux semaines ne vise que l'interruption spontanée, non une restriction nouvelle des motifs médicaux.",
 (13, 'L323-1'): "La cible contient la carence et les limites ordinaires par affection ou nombre d'IJ. Après retrait du plafond spécial de L323-2, ces limites restent applicables aux pensionnés actifs : la proposition exclut remise à zéro et double compte. Cette vérification porte sur la cible officielle fournie, que le lot conserve entière.",
 (13, 'L161-22-1-5'): "La cible définit les trois accès à la retraite progressive, la liquidation provisoire coordonnée, majorations et exclusions du II. Le second alinéa source de L323-2 protège déjà ces personnes contre le plafond spécial : la proposition conserve expressément cet avantage pour le passé et étend l'absence de plafond spécial pour les journées futures sans modifier les conditions de retraite progressive.",
 (14, 'L323-1'): "Le délai du premier alinéa est bien la carence écartée pour le temps partiel thérapeutique. Les périodes maximales restent distinctes et sont articulées par R323-3, lu, avec les 2° et 3° de R323-1 ; l'absence de carence n'est pas une suppression de toute durée maximale ni un préavis d'emploi.",
 (14, 'L321-1'): "La cible fonde la prestation maladie pour incapacité médicalement constatée ; L323-3 en permet le service dans les deux situations de temps partiel thérapeutique. Le maintien des deux textes conserve le périmètre médical sans condition nouvelle de forme du contrat, d'ancienneté ou de notification de rupture.",
 (15, 'L5213-3-1'): "Le 2° vise la convention tripartite de rééducation, pas une nouvelle embauche à durée déterminée. L'accord conventionnel, la rémunération protégée, la mise à disposition, le maintien conditionnel d'IJ après démission et la déduction de toute la mise à disposition de l'essai subsistent. La suppression du visa distinct de caisse ne dispense pas de conclure la convention ; sa fin ne termine pas le contrat unique.",
 (19, 'L133-4-1'): "Le renvoi porte sur la restitution des IJ correspondant aux manquements volontaires subsistants. La cible conserve rectification, recouvrement différé selon la procédure, situation du ménage et recours ; sa majoration de 10 % concerne une fraude de l'assuré, non le seul exercice d'une activité gratuite désormais dispensée ni l'absence de déclaration salariée légalement supprimée.",
 (19, 'L315-2'): "Le 2° et le 6° de L323-6 visent les contrôles médicaux et l'adresse où ils sont réalisables. Les III et IV de la cible conservent suspension médicalement fondée, information et recours, ainsi que sanction du refus de contrôle. Ni la source ni sa proposition retirant les seuls motifs économiques d'accord préalable n'autorisent à sanctionner de nouveau les horaires généraux abrogés ; les contrôles restent distincts du préavis privé.",
 (19, 'L114-17-1'): "Le renvoi de L323-6 vise la sanction possible lorsque l'activité irrégulière a procuré un revenu. La cible distingue bénéficiaires et employeurs, bonne foi selon les manquements, gravité et fraude, avec ses plafonds propres. La proposition ne crée aucun nouveau montant et n'autorise aucune sanction pour le seul défaut d'un visa d'activité gratuite supprimé ; elle conserve le traitement des activités rémunérées irrégulières.",
 (20, 'L133-4-1'): "L323-6-1 désigne spécialement l'employeur subrogé comme débiteur du remboursement et renvoie aux conditions de récupération ; il ne transfère pas automatiquement cette dette au salarié. Rectification, notification et recours de la cible restent opposables dans leur champ. La déclaration unique ne modifie ni l'indu principal ni les délais de cette procédure et ne dépend pas du seuil d'un an de rupture.",
 (20, 'L114-17-1'): "Le I 2° de la cible inclut les employeurs et le II traite les manquements ayant causé un indu, avec les garanties et réserves de bonne foi applicables. L323-6-1 conserve la condition causale entre omission patronale et indu ; la déclaration déjà due n'est ni étendue à de nouveaux salariés ni assortie d'un taux nouveau. La dispense du salarié ne devient pas une obligation de surveiller son employeur.",
 (23, 'L161-9'): "Le 4° du II de L325-1 reprend le maintien des prestations en espèces après congé parental, maladie ou nouvelle maternité ; la cible conserve ces trois séquences et ne fixe pas une durée d'emploi. L'affiliation locale future reste ouverte dans ce champ. Le renvoi interne ancien de la cible à L122-28-1 du code du travail doit être coordonné séparément avec le congé parental recodifié ; il ne justifie pas de fermer le droit local.",
 (23, 'L311-5'): "Le 5° du II vise le maintien de la qualité d'assuré des bénéficiaires d'allocations et revenus de remplacement définis par la cible, y compris maintien après congé parental et IJ nulles ou faibles dans leur champ. La proposition fournie précise notamment l'indemnité propre de L1235-16 ; elle n'est pas l'indemnité ordinaire plafonnée à six mois. Les droits locaux restent ouverts aux futurs éligibles et aux frontaliers selon leurs conditions propres.",
 (23, 'L161-8'): "Le 4° du II vise le maintien des prestations en espèces après perte des conditions d'activité, tant que résidence et séjour restent remplis et sans réouverture équivalente ailleurs. La cible prévoit prolongation pour inscription comme demandeur d'emploi et protections des IJ nulles ou de maternité faible. Ces durées réglementaires sont conservées ; aucune des forclusions de demande supprimées dans L325-1 ne les raccourcit.",
}

special_checks.update({
 (19, 'L323-6-1'): "La cible officielle oblige déjà l'employeur subrogé à informer la caisse de la reprise anticipée. Le 5° proposé retire la déclaration salariée parallèle, sans attendre la diligence patronale ; L323-6-1 est coordonné dans ce lot. Cette information n'est pas une notification de rupture et ne dépend pas d'une ancienneté d'un an.",
 (20, 'L323-6'): "Le 5° de la source officielle impose encore une déclaration de reprise à l'assuré. Sa proposition dans ce lot la retire pendant la subrogation : l'employeur reste le seul déclarant, sans seconde réduction comptée. Ni préavis de quinze jours ni ancienneté de rupture ne conditionnent cette dispense.",
 (22, 'L323-6'): "La vue fournie conserve la faculté des élus locaux de poursuivre leur mandat sauf avis contraire du praticien. La proposition de L324-1 maintient expressément cette exception et coordonne la liberté des activités non rémunérées compatibles proposée dans L323-6, sans importer d'ancienneté ou de préavis d'emploi."
})

for i, (source, answer) in enumerate(zip(sources, answers)):
    key = source['code_id'] + '|' + source['source_id']
    checks = []
    for target_key in references['requirements'][key]:
        target = references['targets'][target_key]
        n = target['number']
        context = contexts.get(i, source['number'] + ' conserve son champ propre de protection sociale.')
        if n == 'L1234-1':
            assessment = (context + " La cible distingue préavis antérieurs et préavis patronal proposé de quinze jours calendaires pour les contrats nouveaux, sans condition d'ancienneté ; elle conserve les procédures collectives et protections. Ce n'est pas un renvoi direct du présent article : ni ses délais médicaux ni ses droits sociaux ne sont ramenés à quinze jours, et aucune nouvelle notification de rupture n'est exigée pour leur bénéfice.")
        elif n == 'L1221-2':
            assessment = (context + " La proposition de cette cible impose une durée indéterminée aux nouvelles embauches privées, sans terme de mission, formation ou saison ; les contrats anciens gardent leur transition. Les situations futures éligibles au présent dispositif restent couvertes dans le contrat unique ; aucun CDD n'est rétabli par un délai médical ou pédagogique, et les agents publics ne sont pas convertis implicitement.")
        elif n == 'L1234-9':
            assessment = (context + " La cible proposée réserve l'indemnité ordinaire à la rupture patronale sous ses exceptions : seuil d'un an à la fin effective préavis inclus, 0,20 mois par année totale, mois complets au prorata et plafond six mois, avec anciens droits et indemnités spéciales préservés. Ce barème ne règle pas la prestation ici examinée ; aucun seuil d'ancienneté, plafond ou notification de licenciement n'y est importé.")
        else:
            assessment = special_checks[(i, n)]
        checks.append(dict(target_key=target_key, view_sha256=target['view_sha256'], assessment=assessment))
    answer['reference_checks'] = checks
    for item in answer['substantive_impact']['effects']:
        item['source_quote'] = complete_paragraph_quote(source['source_xml'], item['source_quote'])
        item['proposed_quote'] = complete_paragraph_quote(answer['proposed_xml'], item['proposed_quote'])

Path('answer.json').write_text(json.dumps(answers, ensure_ascii=False, indent=2) + '\n')
