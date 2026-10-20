import json
import re
from html import unescape
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
by_number = {a['number']: a for a in sources}
answers = {}


def plain(xml):
    return unescape(re.sub(r'<[^>]*>', '', xml or ''))


def paragraphs(*parts):
    return ''.join('<p>' + p + '</p>' for p in parts)


def impact(classification, assessment, limitations, burdens, effects=None):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=limitations, new_burdens_review=burdens,
                effects=effects or [])


def effect(kind, measure, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure, description=description,
                before=before, after=after, unit=unit,
                affected_population=population,
                conditions_and_transition=transition,
                replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


def save(number, proposed, reason, notes, substantive, removed=None, repeal=None):
    src = by_number[number]
    a = {k: src[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    a.update(proposed_xml=proposed, reason=reason, review_notes=notes,
             status='retained_unchanged' if proposed is None else 'rewrite_draft',
             substantive_impact=substantive)
    if proposed is None:
        a['classification'] = 'retained_necessary'
    if removed:
        a.update(change_type='normative_reduction',
                 reform_policy_id='editorial_direction_2026_10_19',
                 removed_provisions=removed)
    if repeal:
        a.update(change_type='full_repeal',
                 repeal_policy_id='editorial_direction_2026_10_19',
                 repeal_scope=repeal)
    answers[number] = a


def retain(number, reason, notes, assessment, limitations, burdens):
    save(number, None, reason, notes,
         impact('retained_necessary', assessment, limitations, burdens))


save('L642-18', paragraphs(
    "Le titulaire du droit d'usage peut exercer le droit de reprise prévu à l'article L. 642-6 à condition d'avoir :",
    "1° Adressé à l'attributaire un préavis d'un an ;",
    "2° Indemnisé celui-ci du montant des travaux non amortis ; ce paiement intervient au plus tard à la date de la reprise.",
    "Ces dispositions s'appliquent aux préavis adressés à compter de l'entrée en vigueur de la loi. Les préavis antérieurs et les indemnités qui s'y rattachent restent régis par les dispositions antérieures."),
    "Réforme de fond limitée au calendrier : suppression du paiement obligatoire de l'indemnité trois mois avant la fin du préavis. L'indemnisation des travaux non amortis reste une condition de la reprise et doit être réglée au plus tard lors de celle-ci. Le préavis d'un an protège l'organisation du relogement ; le supprimer sans coordonner les baux fragiliserait cette protection.",
    "L642-6 entier lu dans le corpus : le droit de reprise ne s'ouvre qu'après neuf ans à compter de la notification de l'arrêté ; ce seuil n'est pas modifié. R642-10 entier lu : sa lettre recommandée avec avis de réception concerne le préavis, non l'avance d'indemnisation. Les 1° et 2° sont conservés. Ni le montant indemnisable ni le tableau d'amortissement mentionné à L642-1 ne sont réformés. Aucun préavis de travail ni barème de licenciement n'est applicable. Pas de remboursement d'avances antérieures ni de baisse de dette revendiquée.",
    impact('payment_timing_relief',
        "Le seul allègement démontré est le report de l'échéance de paiement de trois mois jusqu'à la reprise ; l'indemnité des travaux non amortis n'est pas abolie.",
        "Seuls les préavis nouveaux bénéficient du report. Le délai d'un an et l'ouverture du droit après neuf ans demeurent ; le coût financier de ce décalage pour l'attributaire n'est pas chiffré.",
        "Aucune charge nouvelle identifiée : le paiement, son bénéficiaire et la condition d'indemnisation existent déjà ; aucun justificatif, agrément ou dépôt de remplacement n'est créé.",
        [effect('payment_deferred', 'requisition-indemnite-paiement-a-la-reprise',
            "Suppression de l'avance obligatoire de trois mois sur l'indemnité de reprise.",
            "Indemnité des travaux non amortis payée trois mois avant l'expiration du préavis d'un an.",
            "Même indemnité payable au plus tard à la reprise, sans réduction de montant décidée.",
            'other', "Titulaires du droit d'usage exerçant la reprise et attributaires indemnisés.",
            "Préavis adressés dès l'entrée en vigueur ; les préavis antérieurs gardent leur calendrier.",
            "Aucune formalité nouvelle ; besoin de trésorerie de l'attributaire potentiellement décalé.",
            "Indemnisé celui-ci, trois mois avant l'expiration du délai de préavis, du montant des travaux non amortis.",
            "2° Indemnisé celui-ci du montant des travaux non amortis ; ce paiement intervient au plus tard à la date de la reprise.")]),
    removed=["Paiement obligatoire des travaux non amortis trois mois avant l'expiration du préavis de reprise."])

retain('L642-19',
    "Maintien intégral utile : l'attribution au juge judiciaire des litiges entre titulaire du droit d'usage et attributaire garantit un recours sur l'indemnisation et les droits portant sur les locaux. Elle ne crée ni autorisation, ni déclaration, ni prélèvement accessoire à supprimer.",
    "Compétence limitée aux relations de la section 3 ; ne pas l'étendre à l'ensemble du contentieux administratif de la réquisition ni la confondre avec les litiges du bénéficiaire du bail. Aucun renvoi numéroté à rectifier dans cette phrase.",
    "La source entière organise la compétence judiciaire, indispensable au recours sur les relations patrimoniales de la réquisition ; aucune simplification matérielle n'est revendiquée.",
    "Ne règle pas la compétence pour la légalité de l'arrêté de réquisition ni le financement des indemnités ; aucune réduction globale de coûts n'est démontrée.",
    "Aucune charge nouvelle identifiée puisque la source est conservée intégralement ; aucune saisine supplémentaire, donnée ou condition de recevabilité n'est ajoutée.")

retain('L642-20',
    "Maintien intégral de l'habilitation au décret en Conseil d'Etat pour les sections 1 à 3. Elle permet l'exécution des garanties et de l'indemnisation ; sa suppression seule ne retirerait aucune formalité précise et pourrait rendre leurs modalités incertaines.",
    "Le champ s'arrête à la section 3 et ne vaut pas habilitation particulière pour créer des conditions de bail dans la section 4. Le décret ne peut rétablir l'avance de trois mois supprimée dans L642-18. R642-10 a été lu séparément ; son mode d'envoi du préavis subsiste.",
    "Aucun prélèvement ni dossier n'est directement institué par cette habilitation générale ; maintien nécessaire à l'exécution du chapitre sans allègement comptabilisé.",
    "Ne vaut pas examen exhaustif de tous les décrets des sections 1 à 3 ; seules les coordinations liées aux articles de ce lot sont appréciées.",
    "Aucune charge nouvelle identifiée : aucun règlement nouveau, document ou calendrier supplémentaire n'est imposé par le maintien de la source.")

retain('L642-21',
    "Maintien intégral du socle de la loi du 6 juillet 1989, sous les réserves spéciales de la section : il protège le bénéficiaire et les rapports locatifs, sans justifier la suppression globale des règles de salubrité, de décence ou de recours. Aucune formalité autonome doublonnée n'est énoncée ici.",
    "La loi 89-462 est extérieure aux cinq codes et son texte intégral n'est pas joint au lot ; elle n'est ni réécrite ni réputée abrogée. Les règles spéciales de L642-22 à L642-27 priment dans leur champ, notamment le congé sans préavis proposé à L642-24. La durée du bail n'est pas celle d'un emploi.",
    "Le renvoi général au régime locatif reste nécessaire ; la source entière ne contient aucune charge détachable précisément supprimée par le présent article.",
    "Le maintien ne constitue pas un audit de chaque obligation de la loi 89-462 ; les éventuelles réformes de cette loi doivent être rédigées dans leur propre champ.",
    "Aucune charge nouvelle identifiée : le bail conserve le socle légal déjà applicable et aucun nouveau dossier, agrément ou justificatif n'est créé.")

retain('L642-22',
    "Maintien intégral : la durée annuelle, limitée par le reliquat de réquisition, articule le titre d'occupation avec la jouissance temporaire des locaux. L'absence de dépôt de garantie et de caution simple ou solidaire est un avantage essentiel à conserver pour les futurs baux aussi.",
    "La reconduction est régie par L642-26 et la sortie de la réquisition par L642-27. L'interdiction de nouveaux CDD concerne l'emploi privé et ne transforme pas ce bail d'habitation en contrat à durée indéterminée. Aucun lien avec l'ancienneté professionnelle ou les indemnités de rupture.",
    "La source entière protège l'accès au logement sans avance ni garant ; sa durée reste liée à une réquisition temporaire. Aucun allègement nouveau n'est compté.",
    "Le maintien ne prolonge pas la réquisition ni ne crée un droit général au bail après sa fin ; les droits de relogement demeurent distincts.",
    "Aucune charge nouvelle identifiée : ni dépôt, ni caution, ni attestation supplémentaire ; les deux phrases de la source sont maintenues sans restriction de l'avantage.")

retain('L642-23',
    "Maintien intégral du loyer réglementé au mètre carré, de la révision annuelle selon les indices énoncés et du paiement mensuel à terme échu. Le prix de base et le paiement après occupation protègent les ménages bénéficiaires ; aucun prélèvement public ni justificatif redondant n'est institué par cet article.",
    "L641-7 fourni dans reference-targets renvoie au montant déterminé ici ; sa garantie de recouvrement ne doit pas être confondue avec une indemnité de licenciement. La formule de révision mentionne la variation moyenne de l'indice du coût de la construction et les indices des trois trimestres précédents : conservée telle quelle, sans substitution d'un indice ou d'un pourcentage nouveau. Décret de prix non réécrit dans ce lot.",
    "La source complète fixe les trois règles économiques du loyer, toutes conservées pour éviter une hausse ou la perte du terme échu ; aucune baisse de loyer n'est alléguée.",
    "Le montant du prix de base réglementaire et les séries d'indices ne sont pas chiffrés ici ; aucune économie budgétaire ou baisse automatique des loyers n'est établie.",
    "Aucune charge nouvelle identifiée : mêmes modalités de calcul, de révision et de paiement, sans déclaration ou vérification supplémentaire à la charge du locataire.")

save('L642-24', paragraphs(
    "Le bénéficiaire peut donner congé à tout moment, sans délai de préavis.",
    "Le congé prend effet à la date de sa réception par l'attributaire ou à la date ultérieure indiquée par le bénéficiaire.",
    "Ces dispositions s'appliquent aux congés reçus à compter de l'entrée en vigueur de la loi, y compris pour les contrats en cours. Les loyers et autres sommes échus avant la prise d'effet du congé restent dus."),
    "Réforme de fond : suppression du mois de préavis imposé au bénéficiaire pour quitter un logement réquisitionné. Le congé demeure nécessaire pour porter la sortie à la connaissance de l'attributaire ; aucune déclaration administrative, pièce ou autorisation ne le remplace. Le bénéficiaire peut choisir une date ultérieure.",
    "Le régime concerne exclusivement le congé du locataire de la section 4. Il ne réduit ni le préavis d'un an du titulaire du droit d'usage, ni les délais de relogement, ni un préavis d'emploi. La réception est le point d'effet du congé et non une autorisation de départ ; aucun support supplémentaire n'est imposé. La transition couvre les baux en cours pour les congés nouveaux et préserve les sommes déjà échues.",
    impact('material_reduction',
        "Suppression réelle du mois de préavis locatif : le bénéficiaire peut faire cesser le bail dès réception du congé, au lieu de rester tenu pendant un mois supplémentaire.",
        "Ne s'applique pas aux congés déjà reçus avant la réforme ni aux autres catégories de baux. L'incidence sur les recettes et la rotation des locaux de l'attributaire n'est pas chiffrée.",
        "Aucune charge nouvelle identifiée : le congé existait déjà ; sa réception détermine son effet sans visa, pièce, registre ou procédure administrative de remplacement.",
        [effect('deadline_reduced', 'requisition-conge-beneficiaire-sans-preavis',
            "Suppression du mois d'attente obligatoire après le congé du bénéficiaire.",
            "Délai de préavis d'un mois pour le congé du bénéficiaire du bail de réquisition.",
            "Aucun délai de préavis ; effet à réception ou à une date ultérieure choisie par le bénéficiaire.",
            'other', "Bénéficiaires des baux de la section 4 et attributaires bailleurs.",
            "Congés reçus dès l'entrée en vigueur, y compris pour les baux en cours ; dettes échues préservées.",
            "Aucun dépôt de remplacement ; les formes légalement applicables au congé ne sont pas durcies.",
            "Le bénéficiaire peut donner congé à tout moment, avec un délai de préavis d'un mois.",
            "Le bénéficiaire peut donner congé à tout moment, sans délai de préavis.")]),
    removed=["Délai minimal d'un mois de préavis imposé au bénéficiaire qui donne congé de son logement réquisitionné."])

retain('L642-25',
    "Maintien intégral de l'interdiction de céder le bail ou de sous-louer : le logement est attribué personnellement, sous plafond de ressources et en raison de mauvaises conditions de logement. Retirer cette règle sans dispositif cohérent détournerait la réquisition de ses bénéficiaires désignés ; aucun agrément ou dossier supplémentaire n'est créé ici.",
    "L642-5 entier lu dans le corpus : la désignation préfectorale et le plafond concernent les bénéficiaires du premier alinéa, distincts de l'hébergement d'urgence du second. La restriction préserve cette affectation sociale, sans transposer les règles du contrat de travail unique ni fermer les aides futures.",
    "La source entière protège l'affectation personnelle d'un logement obtenu dans un régime social exceptionnel ; aucune réduction d'obligation n'est revendiquée.",
    "Ne crée pas d'autorisation générale de cession ni de sous-location et ne statue pas sur les droits d'hébergement des proches fondés sur des règles distinctes.",
    "Aucune charge nouvelle identifiée : maintien de la seule interdiction existante, sans contrôle périodique, déclaration de composition du ménage ou nouvelle pièce.")

save('L642-26', paragraphs(
    "Trois mois avant l'expiration du contrat intervenant avant la fin de la réquisition, le représentant de l'Etat dans le département peut proposer au bénéficiaire un autre logement correspondant à ses besoins et à ses possibilités. Le refus de cette offre n'entraîne pas la perte du titre d'occupation avant la fin de la réquisition.",
    "A défaut d'offre de relogement acceptée, le bail est reconduit pour une durée d'un an, ou pour la durée de la réquisition restant à courir si celle-ci est inférieure à un an.",
    "Ces dispositions s'appliquent aux contrats dont le terme intervient à compter de l'entrée en vigueur de la loi, y compris aux contrats en cours. Elles ne rétablissent pas un bail déjà expiré et ne remettent pas en cause les décisions juridictionnelles devenues définitives avant cette date."),
    "Réforme de fond : retrait de la déchéance du titre pour refus d'une offre avant la fin de la réquisition. La reconduction couvre désormais l'absence d'offre acceptée, sans imposer au bénéficiaire de prouver un motif légitime et sérieux pour rester dans son logement pendant la réquisition. L'offre adaptée, son anticipation de trois mois et la limite de durée de la reconduction sont conservées.",
    "Aucun maintien n'est créé au-delà du terme de la réquisition : L642-27 reste applicable. Le droit du titulaire de reprendre dans les conditions de L642-6 et L642-18 n'est pas élargi ni supprimé. Le second alinéa reste celui de la reconduction annuelle ou du reliquat inférieur à un an. La réforme ne crée pas de droit à obtenir simultanément deux logements ; le départ par congé reste régi par L642-24.",
    impact('material_reduction',
        "Le bénéficiaire n'est plus contraint d'accepter un relogement sous peine de perdre son titre avant la fin de la réquisition ; la reconduction devient ouverte en cas de refus.",
        "Le bénéfice s'arrête à la fin de la réquisition et ne rétablit aucun bail expiré ni ne défait un jugement définitif ; l'incidence sur les capacités de relogement n'est pas chiffrée.",
        "Aucune charge nouvelle identifiée : disparition de la justification d'un motif de refus et de la déchéance, sans nouvelle pièce ; l'offre et la reconduction existaient déjà.",
        [effect('relief_extended', 'requisition-refus-relogement-maintien-bail',
            "Ouverture de la reconduction en cas de refus de l'offre avant la fin de la réquisition.",
            "Refus sans motif légitime et sérieux : déchéance au terme du contrat ; reconduction seulement à défaut d'offre.",
            "Refus sans perte de titre avant la fin de la réquisition ; reconduction faute d'offre acceptée, limitée à un an ou au reliquat inférieur.",
            'legal_duty', "Bénéficiaires dont le bail expire avant la fin de la réquisition.",
            "Termes contractuels dès l'entrée en vigueur ; baux déjà expirés et jugements définitifs non remis en cause.",
            "Aucune condition documentaire nouvelle ; obligation éventuelle de poursuivre un bail dans la durée de réquisition existante, sans prolonger celle-ci.",
            "A défaut d'offre de relogement, le bail est reconduit pour une durée d'un an, ou pour la durée de la réquisition restant à courir si celle-ci est inférieure à un an.",
            "A défaut d'offre de relogement acceptée, le bail est reconduit pour une durée d'un an, ou pour la durée de la réquisition restant à courir si celle-ci est inférieure à un an.")]),
    removed=["Déchéance du titre d'occupation avant la fin de la réquisition en cas de refus de relogement sans motif légitime et sérieux.",
             "Exclusion de la reconduction annuelle du bail lorsque le bénéficiaire a reçu mais n'a pas accepté une offre de relogement."])

retain('L642-27',
    "Maintien intégral : à la fin de la réquisition, l'offre adaptée par l'attributaire ou, à défaut, par l'Etat protège le bénéficiaire éligible au logement social ; l'anticipation de trois mois rend ce relogement effectif. Le terme du titre d'occupation respecte la fin de la réquisition. La suppression de cette articulation priverait soit le ménage de son offre, soit le propriétaire de la restitution.",
    "La condition d'éligibilité HLM, les besoins et possibilités du bénéficiaire, le caractère subsidiaire mais obligatoire de l'offre de l'Etat et la faculté de conclure directement un bail avec le titulaire sont conservés. La déchéance du titre n'autorise aucune expulsion privée ; le recours au juge et les protections légales d'exécution restent distincts. L642-26 réformé ne s'étend pas au-delà du terme de la réquisition.",
    "La source complète garantit une offre de relogement à l'échéance de la réquisition et distingue cette fin du renouvellement intermédiaire ; maintien sans gain de simplification compté.",
    "Ne promet pas de logement social en dehors des conditions d'attribution et ne prolonge pas la réquisition ; l'effectivité des offres et leur coût ne sont pas évalués ici.",
    "Aucune charge nouvelle identifiée : mêmes acteurs, conditions d'éligibilité, offre adaptée et échéance de trois mois ; aucune acceptation ou attestation supplémentaire.")

retain('L642-27-1',
    "Maintien intégral de la définition des bénéficiaires : le renvoi au seul premier alinéa de L642-5 réserve le régime du bail aux personnes désignées pour leurs mauvaises conditions de logement et sous plafond de ressources. Il évite la confusion avec l'hébergement d'urgence, sans ajouter de formalité.",
    "L642-5 entier lu : son second alinéa vise l'hébergement d'urgence des personnes sans abri, distinct du bail de la présente section. Aucun terme de formation, mission ou emploi n'est visé ; le contrat unique de travail est inapplicable.",
    "Le renvoi définit précisément la population protégée par la section ; sa suppression brouillerait le champ des avantages sans retirer une charge autonome.",
    "Le montant réglementaire du plafond et le régime de l'hébergement d'urgence ne sont pas réécrits ; aucun élargissement ou restriction d'éligibilité n'est réalisé.",
    "Aucune charge nouvelle identifiée : le renvoi et son alinéa cible demeurent identiques, sans création d'une preuve de ressources ou d'une nouvelle désignation.")

retain('L642-28',
    "Maintien intégral des infractions de dissimulation frauduleuse de vacance et de dégradation intentionnelle pour faire obstacle à la réquisition. Ces protections visent une fraude et des atteintes matérielles, non un simple retard ou une formalité redondante. La remise en état demeure une faculté du tribunal, nécessaire pour réparer le dommage.",
    "I, ses 1° et 2°, le II déjà abrogé et le III sont conservés. Un an d'emprisonnement et 15 000 euros ne sont ni des droits de succession ni une taxe sur l'activité. Le but de faire obstacle et l'existence d'une notification d'intention de réquisitionner au 2° restent des éléments du champ pénal. Aucun rétablissement du II.",
    "La totalité de la source sanctionne des comportements frauduleux ou des dégradations ciblées ; ces fonctions essentielles justifient le maintien sans simplification fictive.",
    "Aucune appréciation des sanctions d'autres régimes ni du nombre de poursuites n'est fournie ; aucune baisse de prélèvement ni économie nationale n'est démontrée.",
    "Aucune charge nouvelle identifiée : mêmes éléments constitutifs, maximums et faculté judiciaire de remise en état, sans déclaration, contrôle périodique ou garantie nouvelle.")

source_blocks = re.split(r'<br\s*/?>', by_number['L651-1']['source_xml'])
first_three = [plain(p).strip() for p in source_blocks if plain(p).strip()][:3]
save('L651-1', paragraphs(*first_three,
    "Aucune peine ne peut être prononcée sur le seul fondement du fait, pour un intermédiaire, un agent de location ou une autre personne, de solliciter ou d'obtenir une commission, une ristourne ou une rétribution supérieure à celles en usage dans la profession à l'occasion de l'application des titres Ier, II, III et IV du présent livre. Les infractions reposant sur un fondement distinct restent applicables.",
    "La suppression de cette incrimination s'applique aux faits antérieurs n'ayant pas donné lieu à une condamnation passée en force de chose jugée. La peine cesse de recevoir exécution lorsque les faits pour lesquels elle a été prononcée n'ont plus le caractère d'une infraction pénale. Les réparations civiles restent régies par leurs règles propres."),
    "Réforme de fond : suppression de l'incrimination spéciale qui appliquait les peines de corruption au seul dépassement des rémunérations en usage dans la profession par les intermédiaires. Les trois premiers alinéas, relatifs aux agents publics, au corrupteur et à la participation aux fraudes, sont conservés intégralement ; la fraude ou la corruption sur un autre fondement n'est pas dépénalisée. Aucun nouveau plafond ou barème d'honoraires n'est créé.",
    "Les exclusions L612-1, L631-1 à L631-6, L641-12 et L641-14 des trois premiers alinéas restent inchangées. Le L641-12 fourni porte sur la réquisition de locaux professionnels, pas sur le préavis de salariés. Les articles 432-11 et 433-1 du code pénal sont des renvois existants dont les corps ne sont pas fournis ; aucune modification de leurs éléments ou peines n'est affirmée. Application de la loi pénale plus douce expressément formulée, sans restitution civile générale ni disparition des réparations.",
    impact('material_reduction',
        "Une incrimination autonome fondée seulement sur le dépassement des rémunérations usuelles est supprimée ; les protections contre la corruption et la participation aux fraudes sont conservées.",
        "Ne libère pas des plafonds ou obligations civiles ayant un fondement distinct ; ni le contenu intégral du code pénal ni les montants des honoraires ne sont réformés ou chiffrés ici.",
        "Aucune charge nouvelle identifiée : aucune déclaration de prix, grille d'honoraires ou autorisation ne remplace l'incrimination retirée ; les réparations et infractions distinctes subsistent.",
        [effect('obligation_removed', 'logement-fin-delit-remuneration-usuelle',
            "Suppression de l'interdiction pénale spéciale du seul dépassement des rémunérations professionnelles usuelles.",
            "Les intermédiaires dépassant les commissions, ristournes ou rétributions en usage encourent les mêmes peines que celles visées aux premiers alinéas.",
            "Aucune peine au seul motif du dépassement de l'usage ; corruption, fraude et règles distinctes restent applicables.",
            'legal_duty', "Intermédiaires, agents de location et autres personnes intervenant dans l'application des titres Ier à IV.",
            "Incrimination supprimée à l'entrée en vigueur ; faits antérieurs non définitivement jugés et cessation d'exécution traités selon la loi pénale plus douce.",
            "Aucun contrôle tarifaire ou registre de remplacement ; pas de suppression des obligations civiles autonomes.",
            "sollicitent ou obtiennent des commissions, ristournes ou rétributions supérieures à celles en usage dans la profession.",
            "Aucune peine ne peut être prononcée sur le seul fondement du fait, pour un intermédiaire, un agent de location ou une autre personne, de solliciter ou d'obtenir une commission, une ristourne ou une rétribution supérieure à celles en usage dans la profession à l'occasion de l'application des titres Ier, II, III et IV du présent livre.")]),
    removed=["Incrimination spéciale appliquant les peines visées par l'article au seul dépassement des commissions, ristournes ou rétributions usuelles des intermédiaires."])

save('L651-2', paragraphs(
    "Aucune amende civile ne peut être prononcée sur le fondement du présent article pour la méconnaissance des articles L. 631-7 ou L. 631-7-1 A ou des conditions ou obligations imposées en application de ces articles.",
    "Le président du tribunal judiciaire statue selon la procédure accélérée au fond, sur assignation de la commune dans laquelle est situé le local irrégulièrement transformé ou de l'Agence nationale de l'habitat. Le tribunal judiciaire compétent est celui dans le ressort duquel est situé le local.",
    "Sur assignation de la commune dans laquelle est situé le local irrégulièrement transformé ou de l'Agence nationale de l'habitat, le président du tribunal ordonne le retour à l'usage d'habitation du local transformé sans autorisation, dans un délai qu'il fixe. A l'expiration de celui-ci, il prononce une astreinte d'un montant maximal de 1 000 € par jour et par mètre carré utile du local irrégulièrement transformé. Le produit en est intégralement versé à la commune dans laquelle est situé le local irrégulièrement transformé.",
    "Le présent article ne permet pas à l'administration de procéder d'office à l'expulsion des occupants ou à l'exécution de travaux aux frais du contrevenant. L'exécution de la décision judiciaire demeure soumise aux règles de droit commun.",
    "La suppression de l'amende civile s'applique à compter de l'entrée en vigueur de la loi, y compris aux instances non définitivement jugées à cette date. Les amendes prononcées par une décision devenue définitive avant cette date restent recouvrables selon les règles antérieures, sous réserve des restitutions et recours légalement ouverts ; aucune restitution générale n'est instituée. La suppression du pouvoir administratif d'exécution d'office s'applique aux mesures non encore exécutées. Les obligations d'usage et les décisions judiciaires imposant le retour à l'habitation ne sont pas supprimées."),
    "Réforme de fond : suppression de l'amende civile pouvant atteindre 100 000 euros par local et du pouvoir administratif spécial d'expulsion et de travaux d'office. L'obligation d'usage, l'action judiciaire en retour à l'habitation, le délai fixé par le juge et l'astreinte plafonnée restent opérants : la protection du parc résidentiel conserve une voie d'exécution sans cette amende cumulative et cette voie administrative exceptionnelle.",
    "L631-7, L631-7-1 A, L631-7-1, L631-8 et L631-9 entiers lus dans le corpus : les autorisations et compensations subsistent, ainsi que les exemptions de résidence principale et la dérogation de résidence-services ; aucune condition n'est durcie. Le dossier commun de L425-9 ne les supprime pas. Le maintien du troisième alinéa conserve 1 000 euros par jour ET par mètre carré utile, son affectation communale, les demandeurs commune/ANAH et l'ordre de retour à l'habitation ; l'autorité organisatrice et l'EPCI n'avaient dans la source que l'action en amende désormais supprimée. Note historique de procédure au 1er janvier 2020 conservée comme contexte, non date de réforme. L321-1 III 3° entier lu prévoit le produit des amendes pour l'ANAH alors que L651-2 l'affecte à la commune : incohérence préexistante d'affectation signalée, sans nouvelle recette de compensation. Cette rubrique hors lot doit être bornée aux recettes anciennes ; elle ne rétablit aucune amende future. L651-2-1 est abrogé dans ce lot.",
    impact('material_reduction',
        "Suppression effective de la sanction civile de 100 000 euros par local et d'une exécution administrative spéciale ; le juge conserve la remise à l'habitation et l'astreinte, sans suppression de l'autorisation d'usage.",
        "Ne constitue pas une abolition de taxe ni une liberté générale de changement d'usage. L'astreinte maximale de 1 000 euros par jour et mètre carré demeure ; les effets sur le logement et les recettes ne sont pas chiffrés.",
        "Aucune charge nouvelle identifiée : l'action de retour, le délai judiciaire et l'astreinte sont déjà dans la source ; aucun agrément, déclaration ou voie de sanction de remplacement n'est créé.",
        [effect('obligation_removed', 'changement-usage-suppression-amendes-civiles',
            "Suppression de l'amende civile spéciale du contrevenant principal, distincte de l'astreinte.",
            "Amende civile maximale de 100 000 euros par local irrégulièrement transformé, pour violation des articles et conditions visés.",
            "Aucune amende civile de ce chef pour les faits et instances couverts ; ordre judiciaire de retour et astreinte conservés.",
            'euro', "Personnes qui méconnaissent L631-7 ou L631-7-1 A et leurs conditions ou obligations.",
            "Entrée en vigueur et instances non définitives ; condamnations définitives anciennes recouvrables selon leur régime.",
            "Pas de sanction de remplacement ; le plafond existant d'astreinte est maintenu, sans hausse.",
            "une amende civile dont le montant ne peut excéder 100 000 € par local irrégulièrement transformé.",
            "Aucune amende civile ne peut être prononcée sur le fondement du présent article pour la méconnaissance des articles L. 631-7 ou L. 631-7-1 A ou des conditions ou obligations imposées en application de ces articles."),
         effect('obligation_removed', 'changement-usage-fin-execution-administrative-speciale',
            "Retrait de l'expulsion et des travaux d'office aux frais du contrevenant par cette voie administrative spéciale.",
            "Après le délai judiciaire, l'administration peut expulser d'office les occupants et faire les travaux aux frais du contrevenant.",
            "Cette voie administrative est retirée ; l'exécution de la décision du juge suit les règles de droit commun.",
            'legal_duty', "Occupants des locaux et personnes supportant les travaux d'office dans ce régime.",
            "Mesures non encore exécutées à l'entrée en vigueur ; travaux réalisés et décisions judiciaires non annulés.",
            "Aucune nouvelle procédure d'autorisation ou titre d'exécution n'est créé par l'article.",
            "Passé ce délai, l'administration peut procéder d'office, aux frais du contrevenant, à l'expulsion des occupants et à l'exécution des travaux nécessaires.",
            "Le présent article ne permet pas à l'administration de procéder d'office à l'expulsion des occupants ou à l'exécution de travaux aux frais du contrevenant.")]),
    removed=["Amende civile spéciale d'un maximum de 100 000 euros par local pour violation des règles ou conditions de changement d'usage, avec son action et son affectation futures.",
             "Pouvoir administratif spécial d'expulsion des occupants et de réalisation d'office des travaux aux frais du contrevenant après le délai judiciaire."])

save('L651-2-1', paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi. Aucune amende civile ne peut être prononcée sur son fondement à compter de cette date, y compris dans les instances non définitivement jugées.",
    "Les amendes prononcées par une décision devenue définitive avant cette date restent régies, pour leur recouvrement, leur affectation, les restitutions et les recours légalement ouverts, par les dispositions antérieures. Aucune restitution générale n'est instituée.",
    "Les obligations relatives à l'usage des locaux et les responsabilités reposant sur un fondement distinct demeurent applicables. Aucun prélèvement ni déclaration ne remplace l'amende supprimée."),
    "Abrogation intégrale de la sanction civile spéciale des personnes concourant au changement d'usage irrégulier par entremise, négociation ou services. L'amende de 100 000 euros par local, son action et son affectation pour l'avenir sont retirées avec la sanction principale de L651-2 ; aucune sanction de substitution n'est créée. L'exclusion des plateformes numériques n'est pas perdue : l'ensemble du prélèvement répressif disparaît pour toutes ces personnes.",
    "Même mesure que l'amende principale de L651-2, sans la compter comme une taxe ni un deuxième dispositif déclaratif supprimé. Les obligations des articles L631-7 et L631-7-1 A subsistent, comme l'action de retour de L651-2. Les faits antérieurs non définitivement jugés bénéficient de la suppression ; seules les condamnations définitives anciennes conservent leur régime de recouvrement et d'affectation communale. Les voies civiles autonomes, la fraude et la corruption ne sont pas abolies. La suppression de l'exception favorable des plateformes n'a aucun effet défavorable puisque l'incrimination entière est retirée sans remplacement.",
    impact('material_reduction',
        "L'article entier, composé de la sanction des concours et de sa procédure, cesse de produire de nouvelles amendes civiles ; la suppression appartient à la même mesure que celle de L651-2.",
        "Les conditions d'usage ne sont pas abrogées et les amendes définitives antérieures subsistent ; aucune baisse d'impôt ou estimation globale de recettes n'est revendiquée.",
        "Aucune charge nouvelle identifiée : aucune amende, autorisation, déclaration ou donnée de remplacement ; les plateformes déjà exclues restent au moins aussi favorablement traitées.",
        [effect('obligation_removed', 'changement-usage-suppression-amendes-civiles',
            "Suppression du volet de la même sanction civile visant les concours et intermédiaires.",
            "Jusqu'à 100 000 euros par local à la charge des personnes concourant à l'infraction, hors mise à disposition de plateforme numérique.",
            "Aucune amende civile sur ce fondement ; l'exclusion des plateformes est absorbée par la suppression totale de la sanction.",
            'euro', "Personnes prêtant concours par entremise, négociation ou mise à disposition de services.",
            "Suppression immédiate, y compris instances non définitives ; amendes anciennes définitives et voies de recours conservées.",
            "Aucune sanction de substitution ; mesure commune à L651-2, sans double comptage de taxe supprimée.",
            "est condamnée à une amende civile dont le montant ne peut excéder 100 000 € par local irrégulièrement transformé.",
            "Aucune amende civile ne peut être prononcée sur son fondement à compter de cette date, y compris dans les instances non définitivement jugées.")]),
    repeal="Sanction civile spéciale, jusqu'à 100 000 euros par local, des concours par entremise, négociation ou services au changement d'usage irrégulier, ainsi que sa procédure et son affectation pour les décisions nouvelles.")

first = plain(by_number['L651-3']['source_xml']).strip().split('\n')[0]
save('L651-3', paragraphs(first,
    "Le présent article n'entraîne, par lui-même, ni résiliation du bail ni expulsion des locataires. Les demandes de résiliation ou d'expulsion reposant sur un fondement distinct restent soumises à leurs conditions propres.",
    "La suppression de la résiliation et de l'expulsion obligatoires s'applique à compter de l'entrée en vigueur de la loi, y compris aux procédures non définitivement jugées. Les décisions devenues définitives ne sont pas remises en cause, sous réserve des règles de cessation d'exécution d'une peine lorsque les faits n'ont plus le caractère d'une infraction pénale. Les infractions maintenues au premier alinéa ne sont pas supprimées."),
    "Réforme de fond partielle : maintien intégral de la répression des fausses déclarations sciemment faites et de la dissimulation frauduleuse, mais suppression de la résiliation et de l'expulsion obligatoirement prononcées en supplément. Le juge n'est plus tenu de faire perdre le logement sur ce seul fondement ; les fondements autonomes de résiliation ou d'expulsion ne sont pas supprimés.",
    "Le premier alinéa conserve exactement les titres, exclusions L612-1, L631-1 à L631-6, L641-12 et L641-14, les manoeuvres frauduleuses, la tentative, un an et 80 000 euros, ainsi que l'alternative entre les deux peines. L641-6 entier lu étend les peines de L651-3 à la mise à disposition d'un tiers : ce renvoi reste opérant pour les peines du premier alinéa. L621-6 entier lu conserve un fondement autonome d'expulsion et doit être coordonné hors lot pour son dernier alinéa ; ne pas prétendre avoir supprimé ce régime distinct. La source est ABROGE_DIFF au 1er janvier 2029 : la rédaction ne doit pas proroger cette version au-delà de son abrogation programmée. Aucun contrat de travail ni indemnité de licenciement n'est visé.",
    impact('material_reduction',
        "Suppression réelle de deux conséquences obligatoires de la condamnation, résiliation du bail et expulsion, sans disparition des infractions de fraude du premier alinéa.",
        "Les expulsions et résiliations fondées sur d'autres textes, notamment L621-6, ne sont pas retirées ; la version source cesse selon son calendrier d'abrogation au 1er janvier 2029.",
        "Aucune charge nouvelle identifiée : aucune nouvelle action, attestation ou autorisation de rester n'est créée ; les demandes autonomes restent soumises à leurs conditions existantes.",
        [effect('obligation_removed', 'logement-fin-resiliation-expulsion-automatiques',
            "Suppression de la résiliation et de l'expulsion que le tribunal correctionnel devait prononcer en supplément.",
            "Le tribunal correctionnel prononce obligatoirement la résiliation du bail et l'expulsion des locataires irrégulièrement installés.",
            "Ni résiliation ni expulsion sur le seul fondement de cet article ; les actions distinctes demeurent possibles selon leurs conditions.",
            'legal_duty', "Locataires concernés par les poursuites de L651-3 et juridictions statuant sur ces faits.",
            "Entrée en vigueur et procédures non définitives ; décisions définitives et règles d'exécution traitées expressément, sans proroger la version de 2029.",
            "Aucun mécanisme de résiliation ou d'expulsion de remplacement n'est créé.",
            "Le tribunal correctionnel prononce, en outre, la résiliation du bail et l'expulsion des locataires irrégulièrement installés.",
            "Le présent article n'entraîne, par lui-même, ni résiliation du bail ni expulsion des locataires.")]),
    removed=["Résiliation du bail obligatoirement prononcée par le tribunal correctionnel en supplément des peines de fraude.",
             "Expulsion obligatoire des locataires irrégulièrement installés sur le seul fondement du second alinéa de cet article."])

save('L651-4', paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi. Aucune amende ne peut être prononcée sur son fondement à compter de cette date, y compris dans les procédures non définitivement jugées.",
    "La peine cesse de recevoir exécution lorsque les faits pour lesquels elle a été prononcée n'ont plus le caractère d'une infraction pénale. Pour les sanctions n'ayant pas ce caractère, les condamnations devenues définitives avant cette date restent régies par les règles antérieures de recouvrement, de restitution et de recours. Aucune restitution générale des sommes déjà acquittées n'est instituée.",
    "L'abrogation ne supprime pas les déclarations légalement dues sur un fondement distinct, les infractions de fraude ni la sanction de l'obstruction volontaire au contrôle. Elle ne crée aucune déclaration, majoration ou pénalité de remplacement pour le seul retard supprimé."),
    "Abrogation de l'amende générale de 2 250 euros frappant le seul défaut de production dans les délais des déclarations du livre VI et de ses textes d'application. La répression de la fraude, l'obstruction volontaire et les obligations déclaratives dont le fondement subsiste sont distinguées. La saisine d'office en référé n'est plus une procédure de sanction du simple retard.",
    "L651-7 est coordonné dans ce lot : il porte directement la même amende de 2 250 euros et la procédure existante pour l'obstruction volontaire, sans étendre celle-ci au retard. L651-9 et L661-1 retirent leur renvoi à L651-4. La recherche dans le CCH public a identifié ces trois renvois, tous traités ; les homonymes du code de commerce dans le CGI ne relèvent pas de cet article. La source nomme une amende poursuivie en référé tandis que L651-7 la qualifie de civile : ambiguïté préexistante signalée, d'où une transition distinguant le cas pénal et les condamnations civiles définitives, sans prétendre requalifier définitivement l'ancienne sanction. La date historique du 1er janvier 2020 n'est pas utilisée comme date de réforme.",
    impact('material_reduction',
        "L'amende transversale de 2 250 euros pour simple retard déclaratif est réellement supprimée ; aucune déclaration ni cotisation principale n'est abolie par cette seule abrogation.",
        "Les sanctions autonomes de fraude et d'obstruction restent applicables ; la nature de l'ancienne amende doit être appréciée selon la procédure concernée. Aucun produit budgétaire national n'est estimé.",
        "Aucune charge nouvelle identifiée : pas de déclaration, pénalité répétée ou majoration de remplacement ; la reprise dans L651-7 concerne seulement l'obstruction volontaire déjà sanctionnée.",
        [effect('obligation_removed', 'logement-fin-amende-retard-declaratif',
            "Suppression de l'amende générale pour retard des déclarations du livre VI.",
            "Amende de 2 250 euros pour non-production dans les délais des déclarations prescrites par le livre VI et ses textes.",
            "Aucune amende sur ce fondement pour le simple retard ; déclarations encore légalement dues et sanctions autonomes conservées.",
            'euro', "Personnes tenues aux déclarations du livre VI et des textes pris pour son application.",
            "Suppression dès l'entrée en vigueur et procédures non définitives ; règles de loi pénale plus douce et sort des condamnations civiles définitives explicités.",
            "Aucune pénalité de remplacement ; le montant de l'obstruction volontaire reste inchangé dans L651-7.",
            "Quiconque ne produit pas, dans les délais fixés, les déclarations prescrites par le présent livre et par les dispositions prises pour son application est passible d'une amende de 2 250 euros.",
            "Aucune amende ne peut être prononcée sur son fondement à compter de cette date, y compris dans les procédures non définitivement jugées.")]),
    repeal="Amende générale de 2 250 euros pour le seul défaut de production dans les délais des déclarations du livre VI et de ses textes d'application, avec sa poursuite d'office en référé pour ce seul manquement.")

first = plain(by_number['L651-5']['source_xml']).strip().split(" L'intéressé est, en outre,")[0]
save('L651-5', paragraphs(first,
    "La condamnation n'entraîne pas, par elle-même, une déchéance du bénéfice des articles L. 631-1 à L. 631-6. Les conditions d'attribution de ces aides et les restitutions légalement dues demeurent applicables.",
    "L'absence de déchéance s'applique aux demandes sur lesquelles il est statué à compter de l'entrée en vigueur de la loi, y compris lorsqu'une déchéance de plein droit résultait d'une condamnation antérieure. Elle ne rouvre pas les décisions de refus devenues définitives et n'ouvre aucun droit à restitution générale."),
    "Réforme de fond : suppression de la déchéance automatique de l'ensemble des aides de déménagement et de réinstallation, en supplément de la sanction pénale. L'élément intentionnel, la perception ou tentative indue, le taux abusif, trois mois d'emprisonnement et 3 000 euros ou l'une des peines seulement sont maintenus. Les futures demandes éligibles ne sont plus fermées par cette déchéance générale.",
    "L631-1 à L631-6 entiers lus : ressources et territoires, règle d'une seule aide de l'Etat au même bénéficiaire, propriété du logement de réinstallation, compléments locaux, arrêté de montant L631-4, financement ANAH et remboursement en cas de retour sous trois ans avec motif légitime demeurent distincts. La suppression de la déchéance ne permet ni une double aide contraire à L631-1 ni la conservation d'un indu. Aucun taux d'aide ni budget nouveau n'est créé. La transition ouvre les décisions futures sans réviser les refus définitivement clos.",
    impact('material_reduction',
        "Suppression d'une exclusion automatique attachée à la condamnation ; les aides restent ouvertes aux demandes futures remplissant leurs conditions, sans dépénaliser la perception frauduleuse.",
        "Ne modifie ni les plafonds, territoires ou conditions des aides ni la règle d'une aide d'Etat unique ; les restitutions d'indus et les décisions de refus définitives demeurent.",
        "Aucune charge nouvelle identifiée : pas d'agrément de réhabilitation, de délai d'attente ou de pièce de remplacement ; l'instruction applique seulement les conditions existantes des aides.",
        [effect('relief_extended', 'logement-aides-fin-decheance-automatique',
            "Retrait de la déchéance de plein droit fermant l'accès aux régimes d'aide.",
            "La condamnation entraîne de plein droit la déchéance du bénéfice de tous les articles L631-1 à L631-6, sans durée précisée dans l'article.",
            "La condamnation n'emporte plus cette déchéance ; une demande reste examinée selon les conditions propres des aides.",
            'legal_duty', "Personnes condamnées pour fraude aux primes de déménagement ou de réinstallation.",
            "Décisions sur demandes prises dès l'entrée en vigueur, y compris déchéance ancienne ; refus définitifs non rouverts et restitutions dues préservées.",
            "Aucune procédure nouvelle ; aucune seconde aide autorisée en contrariété avec les conditions existantes.",
            "L'intéressé est, en outre, déchu de plein droit du bénéfice des articles L. 631-1 à L. 631-6.",
            "La condamnation n'entraîne pas, par elle-même, une déchéance du bénéfice des articles L. 631-1 à L. 631-6.")]),
    removed=["Déchéance de plein droit du bénéfice de l'ensemble des articles L631-1 à L631-6 en supplément des peines de fraude aux primes de déménagement ou de réinstallation."])

src_paras = re.findall(r'<p>(.*?)</p>', by_number['L651-6']['source_xml'], flags=re.S)
save('L651-6', paragraphs(src_paras[0],
    "La nomination de ces agents n'est soumise à aucune limitation de nombre ni à une autorisation ministérielle.",
    *src_paras[2:],
    "Ces dispositions s'appliquent aux nominations à compter de l'entrée en vigueur de la loi. Elles ne mettent fin à aucune nomination en cours et n'imposent ni recrutement ni suppression d'emploi."),
    "Réforme de fond : retrait du ratio légal d'un agent par 30 000 habitants ou fraction de ce chiffre et de la décision ministérielle nécessaire pour augmenter cet effectif. La commune peut organiser ses moyens sans ce contingentement national ; aucun dossier ou avis n'est substitué à la décision supprimée. Serment, secret professionnel, mission territoriale et garanties de visite sont conservés intégralement.",
    "Les cinq alinéas initiaux gardent leur fonction et leur ordre ; seul le deuxième est remplacé et une transition est ajoutée. Les heures de huit à dix-neuf heures, l'ordre de mission personnel, la carte avec photographie, la présence de l'occupant ou gardien et le secret sont inchangés. L621-4 et R641-8 entiers lus : ils empruntent les prérogatives des agents pour leurs champs propres, sans créer un nouveau régime de recrutement. La suppression du ratio ne constitue pas une économie de personnel garantie ; aucun poste ni contrôle n'est supprimé de plein droit. La note historique de 2020 ne date pas la réforme.",
    impact('material_reduction',
        "Retrait réel du contingentement démographique et de l'autorisation ministérielle d'augmentation d'effectif ; les protections du contrôle des logements restent intégrales.",
        "Ne supprime pas les contrôles ni les emplois existants et ne démontre aucune baisse de dépenses : l'effectif et son financement restent du ressort des autorités compétentes.",
        "Aucune charge nouvelle identifiée : le maire nomme déjà les agents ; aucun nouvel acte d'effectif, rapport, registre, recrutement minimal ou pièce de nomination n'est exigé.",
        [effect('authorization_removed', 'logement-agents-fin-contingentement-ministeriel',
            "Suppression de la décision ministérielle préalable à l'augmentation du nombre d'agents.",
            "Nombre fixé à un agent pour 30 000 habitants ou fraction ; augmentation par décision ministérielle.",
            "Nomination sans contingent démographique ni autorisation ministérielle, sans obligation de recruter.",
            'legal_duty', "Communes et autorités compétentes pour la nomination des agents du service municipal du logement.",
            "Nominations dès l'entrée en vigueur ; mandats et emplois en cours non interrompus.",
            "Aucune déclaration ou validation d'effectif de remplacement ; garanties de visite conservées.",
            "Leur nombre est fixé à 1 par 30 000 habitants ou fraction de ce chiffre. Ce nombre peut être augmenté par décision ministérielle.",
            "La nomination de ces agents n'est soumise à aucune limitation de nombre ni à une autorisation ministérielle.")]),
    removed=["Ratio national fixant le nombre d'agents à un pour 30 000 habitants ou fraction de ce chiffre.",
             "Décision ministérielle préalable pour augmenter le nombre des agents assermentés du service municipal du logement."])

first = re.findall(r'<p>(.*?)</p>', by_number['L651-7']['source_xml'], flags=re.S)[0]
save('L651-7', paragraphs(first,
    "Quiconque fait volontairement obstacle, en violation des prescriptions ci-dessus, à la mission des agents du service municipal du logement, est passible d'une amende civile de 2 250 euros.",
    "Le ministère public poursuit d'office l'application de cette amende devant le président du tribunal judiciaire du lieu de l'immeuble, statuant en référé.",
    "Les procédures en cours relatives à cette seule obstruction se poursuivent sans nouvelle saisine."),
    "Coordination nécessaire à l'abrogation de L651-4 : le montant de 2 250 euros et la procédure déjà applicables par renvoi sont portés directement dans L651-7 pour la seule obstruction volontaire. Ce n'est pas une sanction nouvelle ni le maintien de la pénalité du simple retard déclaratif. Le premier alinéa est conservé intégralement pour le contrôle effectif de l'occupation des locaux.",
    "Le renvoi source désignait une amende civile alors que L651-4 nommait seulement une amende et prévoyait une poursuite d'office en référé : la qualification civile propre à L651-7 est conservée, non étendue à tous les retards. L'élément volontaire et la violation des prescriptions demeurent nécessaires. Propriétaires, locataires, autres occupants, administrations et syndics gardent exactement leur champ ; aucun nouveau droit d'accès aux données ou obligation d'archivage n'est créé. L621-4 et R641-8, lus, conservent leurs renvois aux prérogatives dans leur champ distinct. Aucun nouvel exemplaire, justificatif périodique ou registre n'est imposé.",
    impact('coordination_only',
        "Seule la sanction de l'obstruction déjà existante est autonomisée pour éviter un renvoi orphelin ; aucune nouvelle réduction ni nouvelle amende n'est comptée dans cet article.",
        "La suppression du simple retard appartient à L651-4 ; ici, ni le montant de l'obstruction ni les pouvoirs de contrôle ne sont réduits ou étendus.",
        "Aucune charge nouvelle identifiée : mêmes personnes, élément volontaire, 2 250 euros et procédure en référé ; la poursuite en cours ne nécessite aucune nouvelle saisine.",
        [effect('coordination', 'logement-fin-amende-retard-declaratif',
            "Autonomisation de la seule sanction existante de l'obstruction après suppression de l'amende générale de retard.",
            "Obstruction volontaire sanctionnée par renvoi à l'amende de 2 250 euros de L651-4 et à sa procédure.",
            "Même amende civile de 2 250 euros et même procédure inscrites directement, sans sanction du seul retard.",
            'euro', "Personnes faisant volontairement obstacle aux missions prévues au premier alinéa.",
            "Coordination à l'entrée en vigueur ; les procédures d'obstruction en cours se poursuivent sans nouvelle saisine.",
            "Aucune charge nouvelle : déplacement explicite d'une sanction et de sa procédure existantes, sans extension de l'infraction.",
            "est passible de l'amende civile prévue à l'article L. 651-4.",
            "est passible d'une amende civile de 2 250 euros.")]))

retain('L651-8',
    "Maintien intégral de la faculté de délégation : elle permet aux ministres de confier localement l'exercice de pouvoirs déjà prévus sans multiplier les décisions centrales. Le seuil de sous-directeur pour les fonctionnaires délégataires protège la compétence et la responsabilité ; aucun dossier à la charge du public n'est énoncé.",
    "Le représentant de l'Etat dans le département et les fonctionnaires ayant au moins rang de sous-directeur restent les deux catégories possibles. Une délégation n'élargit pas le pouvoir délégué : elle ne peut rétablir les sanctions ou l'autorisation d'effectif supprimées dans ce lot.",
    "La source entière est une faculté d'organisation administrative utile, sans obligation autonome de dépôt ou de paiement à retirer ; maintien sans allègement supplémentaire compté.",
    "Ne réécrit pas les arrêtés de délégation existants ni les pouvoirs substantiels des autres articles du livre ; aucune économie d'effectif n'est démontrée.",
    "Aucune charge nouvelle identifiée : même faculté de délégation par arrêté, mêmes délégataires et aucun nouveau document ou calendrier imposé aux administrés.")

save('L651-9', paragraphs(
    "Les dispositions des articles L. 611-1, L. 621-1 à L. 621-6, L. 631-7 à L. 631-9, L. 641-1 à L. 641-10, L. 651-1, L. 651-2, L. 651-3 et L. 651-6 à L. 651-8 sont d'ordre public.",
    "La présente disposition ne prolonge pas l'application d'un article au-delà de son abrogation."),
    "Coordination nécessaire : retrait des références à L651-4 abrogé et à L651-2-1, jusque-là compris dans la plage L651-1 à L651-4. L'ordre public des règles restantes est conservé ; il protège les droits du bénéficiaire et ne peut faire revivre les sanctions supprimées. Il ne s'agit pas d'une nouvelle obligation supprimée en plus des dispositions abrogées.",
    "L611-1 et L621-1 à L621-6 entiers lus dans le corpus. L621-6 et L651-3 sont annoncés abrogés au 1er janvier 2029 : l'ordre public ne proroge aucune version. Les cibles fournies L641-7, L641-8, L641-9 et L641-10 ont été lues en source et, lorsqu'elle existe, en proposition : garantie de l'Etat, indemnités, recours et protections des travaux restent distincts des nouvelles suppressions de sanction. La source L641-9 présente encore des renvois anciens et le mot « déculpe » ; sa proposition les coordonne, sans devenir du droit en vigueur. Les propositions ne sont pas réputées automatiquement adoptées. Les autres plages demeurent dans leur champ actuel, sans transposition du contrat unique.",
    impact('coordination_only',
        "L'énumération d'ordre public est ajustée aux abrogations ; elle ne supprime par elle-même ni taxe, ni déclaration, ni procédure supplémentaire.",
        "Ne vaut pas refonte des régimes des articles énumérés ou de leurs versions futures ; les abrogations programmées et transitions des articles concernés restent déterminantes.",
        "Aucune charge nouvelle identifiée : l'ordre public préexistait et la liste est resserrée ; aucune collecte, formalité ou condition supplémentaire n'est instituée.",
        [effect('coordination', 'logement-fin-amende-retard-declaratif',
            "Retrait de L651-4 de l'énumération d'ordre public après son abrogation.",
            "La plage L651-1 à L651-4 comprenait la pénalité générale de retard et L651-2-1.",
            "Enumération limitée aux articles subsistants L651-1, L651-2 et L651-3, sans prorogation d'un texte abrogé.",
            'other', "Personnes et juridictions appliquant les dispositions d'ordre public du livre VI.",
            "Même entrée en vigueur que les abrogations ; leurs règles anciennes et transitoires ne sont pas rétablies par le renvoi.",
            "Aucune charge nouvelle ; simple coordination de liste sans seconde réduction comptée.",
            "L. 651-1 à L. 651-4",
            "L. 651-1, L. 651-2, L. 651-3"),
         effect('coordination', 'changement-usage-suppression-amendes-civiles',
            "Fin de l'inclusion de L651-2-1 dans la plage d'ordre public, sans nouvel effet de sanction.",
            "L651-2-1 était inclus dans la plage L651-1 à L651-4.",
            "L651-2-1 n'est plus compris dans la liste, l'article de sanction étant abrogé.",
            'other', "Intermédiaires et autres personnes autrefois visées par L651-2-1.",
            "Coordination immédiate avec l'abrogation ; les condamnations définitives suivent leur transition propre.",
            "Aucune charge nouvelle et aucune suppression distincte supplémentaire revendiquée.",
            "L. 651-1 à L. 651-4",
            "L. 651-1, L. 651-2, L. 651-3")]))

retain('L651-10',
    "Maintien intégral : la désignation judiciaire d'un administrateur protège les occupants d'un hébergement portant atteinte à la dignité, la sécurité ou la santé. L'information des propriétaires, la publicité de la confiscation, la citation de la personne non poursuivie, sa défense et son appel sont des garanties essentielles ; elles ne sont pas des déclarations redondantes à retirer.",
    "I à IV lus en entier : critères de danger ou de violation sanitaire, durée de la procédure, faculté de désigner un organisme agréé L365-4, double information des propriétaires, registres de commerce et de sûretés, décision spéciale motivée, citation indiquant les peines possibles, observations et appel, transfert du fonds à l'Etat et subrogation sont conservés. L521-4 entier fourni, source et proposition, renvoie en son dernier alinéa à L651-10 pour l'hébergement ; ses infractions, personnes vulnérables et confiscations restent à leur champ propre. La note historique de l'ordonnance 2020-71 et de son échéance au plus tard le 1er juillet 2021 n'est pas une date de réforme. Les autres articles du code pénal et du code de la santé publique ne sont pas fournis intégralement et ne sont pas déclarés réécrits. L'agrément déjà obtenu d'un organisme peut permettre sa désignation, sans imposer une nouvelle procédure d'agrément dans cet article.",
    "La source entière combine protection contre l'habitat indigne et garanties juridictionnelles des tiers ; aucune charge sans fonction essentielle démontrée n'y est retirée et aucun gain nouveau n'est attribué.",
    "Ne vaut pas réexamen intégral du droit pénal, des peines complémentaires ou des registres hors corpus ; les propositions des cibles ne remplacent pas leur source officielle.",
    "Aucune charge nouvelle identifiée : l'information, la publicité et la citation sont celles de la source ; leur maintien protège la défense, les tiers et l'opposabilité sans nouvelle donnée ni dépôt.")

save('L661-1', paragraphs(
    "Le présent livre ne s'applique pas en Guadeloupe, en Guyane, en Martinique, à La Réunion et à Mayotte, à l'exception des chapitres III et IV du titre Ier, du chapitre II du titre II, des chapitres Ier bis et III du titre III et du titre IV. Les articles L. 631-7 à L. 631-9, L. 651-1 et L. 651-2 sont toutefois applicables dans ces départements et collectivités territoriales. Ils ont un caractère d'ordre public."),
    "Coordination nécessaire : suppression du seul renvoi à l'amende générale de L651-4, abrogée. Toutes les exceptions territoriales du livre VI et l'ordre public des articles restants sont conservés. Cette coordination ne crée pas une deuxième baisse de sanction ni une extension de contrôle outre-mer.",
    "Guadeloupe, Guyane, Martinique, La Réunion et Mayotte restent nommément incluses. Le titre IV demeure dans les exceptions : les garanties de réquisition et de bail de ce lot y restent applicables dans leur champ. L651-6 et L651-7 ne sont pas ajoutés à la liste des articles du titre V applicables ; l'autonomisation de l'amende d'obstruction à L651-7 ne l'étend donc pas à ces territoires. Les règles transitoires de l'abrogation de L651-4 valent pour son ancien champ territorial. La note renvoie au III de l'article 139 de la loi 2022-217, non fourni intégralement : conditions territoriales à contrôler dans ce texte extérieur, sans prétendre les avoir réécrites ni les écarter.",
    impact('coordination_only',
        "Le renvoi territorial à l'article abrogé est retiré ; les autres exceptions et garanties restent identiques, sans nouvelle suppression comptée en plus de L651-4.",
        "Le III de l'article 139 de la loi 2022-217 n'est pas réécrit ; aucune extension de L651-7 ou du contrôle municipal aux territoires exclus n'est présumée.",
        "Aucune charge nouvelle identifiée : mêmes territoires et exceptions, avec retrait d'un renvoi de sanction ; aucun régime, déclaration ou contrôle de remplacement n'est ajouté.",
        [effect('coordination', 'logement-fin-amende-retard-declaratif',
            "Retrait du renvoi qui rendait l'amende générale applicable dans les cinq territoires cités.",
            "L651-4 est expressément rendu applicable avec L631-7 à L631-9, L651-1 et L651-2.",
            "Le renvoi à L651-4 disparaît ; la liste restante et son ordre public sont conservés.",
            'other', "Personnes relevant de l'ancien champ de L651-4 dans les cinq territoires cités.",
            "Coordination dès l'entrée en vigueur ; transition des sanctions anciennes selon l'abrogation, sans extension de L651-7.",
            "Aucune charge nouvelle ; pas de nouveau contrôle ou d'amende territoriale de remplacement.",
            "Les articles L. 631-7 à L. 631-9, L. 651-1, L. 651-2 et L. 651-4 sont toutefois applicables dans ces départements et collectivités territoriales.",
            "Les articles L. 631-7 à L. 631-9, L. 651-1 et L. 651-2 sont toutefois applicables dans ces départements et collectivités territoriales.")]))

# L'élargissement de la reconduction comporte une contrepartie pour le bailleur.
ai = answers['L642-26']['substantive_impact']
ai['classification'] = 'mixed'
ai['assessment'] = "Le refus de relogement ne fait plus perdre le titre avant la fin de la réquisition. Cet avantage impose corrélativement à l'attributaire la poursuite d'un bail qui pouvait auparavant expirer ; aucun solde net de charges n'est établi."
ai['new_burdens_review'] = "Charge nouvelle identifiée pour l'attributaire : reconduction du bail après une offre refusée, auparavant exclue sauf motif légitime et sérieux. Aucun dossier ni justificatif nouveau ; la réquisition n'est pas prolongée et le coût net reste inconnu."
ai['effects'].append(effect('obligation_added', 'requisition-refus-relogement-maintien-bail',
    "Contrepartie de l'avantage : poursuite du bail par l'attributaire après refus d'une offre de relogement.",
    "Le refus sans motif légitime et sérieux permettait la fin du titre au terme du bail avant la fin de la réquisition.",
    "L'attributaire doit poursuivre le bail faute d'offre acceptée, pour un an ou pour le reliquat de réquisition inférieur à un an.",
    'legal_duty', "Attributaires bailleurs d'un logement réquisitionné dont le bénéficiaire refuse le relogement.",
    "Termes contractuels dès l'entrée en vigueur ; aucun rétablissement de bail expiré ni prolongation de la réquisition.",
    "Obligation de maintien du bail élargie, sans transmission, registre ou pièce supplémentaire ; solde économique non chiffré.",
    "Sauf motif légitime et sérieux, le bénéficiaire qui n'accepte pas l'offre de relogement est déchu de tout titre d'occupation au terme du contrat.",
    "A défaut d'offre de relogement acceptée, le bail est reconduit pour une durée d'un an, ou pour la durée de la réquisition restant à courir si celle-ci est inférieure à un an."))

reference_assessments = {
    'L642-18': {
        'L1234-1': "L1234-1 règle le préavis du salarié licencié : ancienneté et un ou deux mois dans la source, quinze jours calendaires pour les nouveaux contrats dans la proposition. Le préavis d'un an de L642-18 est celui d'une reprise de locaux après le seuil de neuf ans de L642-6 ; aucune ancienneté d'emploi ni notification de rupture salariale ne lui est applicable.",
        'L1221-2': "La proposition de L1221-2 impose une durée indéterminée aux nouveaux emplois privés et protège les contrats antérieurs. L642-18 ne porte pas sur une embauche : son titulaire du droit d'usage exerce un droit de reprise immobilière. La notification d'un préavis locatif ne transforme ni la réquisition ni le bail en CDD de travail.",
        'L1234-9': "La source ouvre une indemnité de licenciement après huit mois ; la proposition fixe, pour le contrat unique, le seuil d'un an au terme préavis inclus puis 0,20 mois par année totale, mois complets et plafond de six mois, employeur seul. L642-18 indemnise les travaux non amortis de l'attributaire, sans salaire ni ancienneté : aucun de ces seuils ou plafonds n'est transposé."
    },
    'L642-24': {
        'L1234-1': "Le préavis de L1234-1 concerne l'initiative de l'employeur et conserve les anciennes durées selon l'ancienneté pour les contrats antérieurs dans la proposition. L642-24 règle le congé du bénéficiaire d'un bail ; le mois locatif supprimé ne devient pas le préavis individuel de quinze jours de l'emploi. La réception retenue ici n'est pas la notification de licenciement.",
        'L1221-2': "La durée indéterminée proposée à L1221-2 vise le nouvel emploi privé, pas le bail temporaire de locaux réquisitionnés. Le congé peut donc être allégé pour les baux en cours et futurs sans convertir ces baux en contrat de travail, sans ancienneté d'emploi et sans rouvrir les anciens CDD. La réception du congé fixe seulement la sortie du logement.",
        'L1234-9': "L1234-9 proposé indemnise une rupture par l'employeur après un an au terme préavis inclus et préserve les composantes anciennes et les réparations spéciales. Le bénéficiaire qui donne congé au titre de L642-24 ne rompt aucun emploi : aucune indemnité de 0,20 mois, aucun plafond de six mois ni seuil d'ancienneté n'est applicable à son bail."
    },
    'L651-1': {
        'L1234-1': "L651-1 conserve la répression de la corruption et de la participation aux fraudes du logement. Il ne contient aucun renvoi à L1234-1 : les offres, commissions et rétributions ne constituent pas un préavis de salarié. Les quinze jours de la proposition, sa distinction entre nouveaux et anciens emplois et l'ancienneté n'affectent pas cette incrimination.",
        'L1221-2': "L1221-2 proposé supprime les nouvelles embauches à terme, avec transition des anciens emplois. Les agents publics et intermédiaires nommés dans L651-1 interviennent dans la police du logement ; leur qualité ne soumet pas ce texte répressif au contrat unique. Aucun terme d'emploi, renouvellement de CDD ni condition de notification professionnelle n'est institué ici.",
        'L1234-9': "L1234-9 porte sur une indemnité ordinaire de rupture salariale, avec ancienneté mesurée au terme, composantes anciennes et protections spéciales. Les dons, présents, commissions et peines de L651-1 ne sont pas une indemnité de licenciement. La suppression de l'incrimination du dépassement des usages ne modifie ni le seuil d'un an ni le barème proposé de 0,20 mois.",
        'L641-12': "Le L641-12 fourni est une source officielle sans proposition : réquisition des locaux commerciaux, artisanaux, professionnels et accessoires vacants, avec renvois d'indemnisation. Il est expressément exclu du champ des premiers alinéas de L651-1 ; cette exclusion est conservée. Ce n'est ni une durée d'emploi ni un renvoi à une ancienneté ou notification de rupture du travail."
    },
    'L651-3': {
        'L1234-1': "L651-3 concerne fausses déclarations, dissimulation frauduleuse et sanctions relatives aux locaux ; aucun renvoi n'y désigne le préavis de licenciement de L1234-1. Retirer résiliation et expulsion obligatoires n'impose pas quinze jours de préavis au bail et ne modifie pas les préavis des emplois anciens selon leur ancienneté ni leur notification.",
        'L1221-2': "La résiliation source de L651-3 est celle d'un bail, non celle d'un emploi à terme. La proposition de L1221-2 sur les nouveaux contrats privés indéterminés et la transition des anciens CDD reste étrangère à cette sanction. Aucun nouveau CDD, durée de formation, ancienneté salariale ou notification de rupture n'est déduit du maintien du premier alinéa pénal.",
        'L1234-9': "L1234-9 proposé distingue une indemnité ordinaire après un an, préavis compris, et les réparations ou indemnités spéciales. Les 80 000 euros et un an de L651-3 sont des peines de fraude, non une indemnité salariale. Ils ne sont ni plafonnés à six mois de salaire ni effacés avant un an d'ancienneté ; la suppression porte seulement sur les conséquences locatives obligatoires.",
        'L641-12': "L641-12 permet la réquisition de catégories de locaux vacants et organise leur indemnisation ; son texte fourni n'a pas de proposition. L651-3 l'exclut explicitement des déclarations et dissimulations réprimées par son premier alinéa. Cette exclusion reste exacte dans le nouveau corps ; aucune ancienne situation de réquisition n'est assimilée à un ancien contrat de travail."
    },
    'L651-9': {
        'L1234-1': "L651-9 rend d'ordre public des règles immobilières déterminées par leurs numéros CCH. La plage L641-1 à L641-10 ne vise pas L1234-1 du travail ; les quinze jours proposés pour les nouveaux emplois et les préavis anciens selon ancienneté n'ont pas d'effet sur cette liste. Aucun préavis locatif n'est remplacé par une notification de licenciement.",
        'L1221-2': "Les contrats et occupations du livre VI ne sont pas les emplois de L1221-2. L'ordre public conservé pour les réquisitions ne crée aucun CDD privé ni aucune dérogation au contrat unique proposé. Les anciens baux et réquisitions gardent leurs transitions propres, sans que le terme de leur occupation soit une fin automatique d'emploi.",
        'L1234-9': "Les indemnités d'occupation et de dommages des articles L641-7 à L641-9 inclus par L651-9 n'ont ni assiette salariale ni ancienneté de service. L1234-9 proposé, son seuil d'un an au terme préavis inclus et son barème de 0,20 mois plafonné à six mois restent donc inapplicables ; les droits acquis immobiliers ne sont pas des composantes d'indemnité de licenciement.",
        'L641-8': "L651-9 englobe L641-8 dans sa plage d'ordre public. La source prévoit deux envois et des délais de quinze jours avec déchéance du recours contre l'Etat ; la proposition les allège et protège les demandes non définitivement jugées, tout en conservant le délai de paiement après réception. Ces quinze jours ne sont pas le préavis d'emploi ; l'ordre public ne rétablit pas une déchéance supprimée si cette proposition est adoptée.",
        'L641-10': "La cible fournie est uniquement la source officielle : travaux strictement indispensables à l'habitabilité non opposables par le propriétaire, aux frais du bénéficiaire, sans indemnité de travaux et avec possible remise en état à la fin. L651-9 conserve son ordre public sans l'élargir ni supprimer cette faculté de travaux ; aucune ancienneté ou notification de rupture professionnelle n'est concernée.",
        'L641-7': "L641-7 fourni, sans proposition, règle le montant de l'indemnité selon L642-23, le paiement direct suivant les usages et le privilège civil de recouvrement. Son inclusion dans L651-9 reste cohérente avec le maintien du loyer réglementé de L642-23 ; il ne renvoie pas au barème de licenciement et ne comporte aucun seuil d'ancienneté ou préavis professionnel.",
        'L641-9': "La source garantit les dommages par l'Etat et comporte un délai renvoyé à L641-8 ainsi qu'une amende quotidienne de maintien dans les lieux. La proposition retire délai de déchéance et amende, coordonne le sursis d'expulsion par L613-1 et protège les condamnations définitives. L651-9 conserve le statut d'ordre public de la règle applicable sans rétablir les dispositions supprimées ; les quinze jours sont immobiliers, sans ancienneté d'emploi."
    },
    'L651-10': {
        'L1234-1': "L651-10 organise une administration provisoire judiciaire d'un hébergement dangereux pendant la procédure, pas un licenciement de l'exploitant ou du personnel. Le préavis d'emploi de L1234-1, quinze jours pour les nouveaux contrats dans la proposition et anciennes durées selon ancienneté, n'abrège ni la procédure judiciaire ni les citations nécessaires avant confiscation.",
        'L1221-2': "La durée de la mission de l'administrateur provisoire, limitée à la procédure, n'est pas le terme d'un contrat de travail. L1221-2 proposé sur l'emploi privé indéterminé et la transition des anciens CDD ne transforme pas la désignation judiciaire en embauche ni n'impose de faire cesser des emplois avec la mission. Le régime des agents publics n'est pas modifié.",
        'L1234-9': "L651-10 vise les pouvoirs de gestion et les droits des propriétaires d'immeuble ou de fonds, sans indemnité salariale. Le seuil d'un an au terme préavis inclus, le calcul de 0,20 mois par année totale, le plafond de six mois et les composantes anciennes de L1234-9 proposé n'y sont donc pas applicables. Les garanties de défense des propriétaires ne sont pas des indemnités de rupture.",
        'L521-4': "L651-10 I vise les poursuites fondées sur L521-4, dont le dernier alinéa, en source comme en proposition, renvoie à L651-10 pour les exploitants d'hébergements. Les infractions de menace, loyers interdits ou refus de relogement, l'aggravation pour vulnérabilité et les peines de confiscation restent dans leur champ. Maintien cohérent des quatre subdivisions de L651-10, de la citation du tiers non poursuivi, de sa défense et de son appel."
    }
}

# Les renvois pénaux recyclés exigent un nouveau corps : maintien simple exclu.
corrected_65110 = by_number['L651-10']['source_xml'].strip().replace(
    'L. 511-6, L. 521-4 et L. 184-1',
    'L. 511-22, L. 521-4 et L. 184-4 à L. 184-6')
corrected_65110 += paragraphs(
    "V.-La coordination des renvois prévue au I s'applique aux procédures en cours à compter de l'entrée en vigueur de la loi. Les désignations, informations, citations et mesures régulièrement intervenues avant cette date restent valables et n'ont pas à être renouvelées de ce seul fait. Les décisions devenues définitives ne sont pas remises en cause.")
save('L651-10', corrected_65110,
    "Coordination nécessaire d'une incohérence préexistante : les références pénales L511-6 et L184-1 du I sont remplacées par L511-22 et L184-4 à L184-6. Les cibles actuelles L511-6 et L184-1 portent respectivement sur le signalement et la police administrative, sans définir les infractions visées. L511-22 VI et L184-9 renvoient expressément eux-mêmes à L651-10 pour ces poursuites d'exploitants. Tous les autres termes des I à IV sont conservés ; une transition préserve les actes et garanties des procédures en cours. Aucun allègement matériel n'est compté pour cette correction.",
    "Sources publiques lues intégralement dans le corpus : L511-6 (LEGIARTI000042342656), L511-22 (LEGIARTI000049778895), L184-1 à L184-9 et L365-4. Nouveaux renvois explicites non fournis comme cibles dans reference-targets.json : L511-22, L184-4 (LEGIARTI000041571403), L184-5 (LEGIARTI000041571405), L184-6 (LEGIARTI000041571407) ; leurs corps officiels ont été vérifiés dans construction-habitation.json, sans inventer de cible ou d'empreinte supplémentaire. L511-22 VI et L184-9 établissent le raccord actuel, indépendamment d'une simple similitude de numéros. I à IV conservent critères sanitaires et de dignité, durée judiciaire, organismes agréés, notifications aux deux propriétaires, registres, citation motivée du tiers non poursuivi, défense et appel, confiscation et subrogation de l'Etat. L365-4 proposé dans le corpus allège durée et territoire de l'agrément ; son renvoi ici n'ajoute aucun renouvellement, son texte source et sa proposition restent distincts. La correction ne modifie aucun élément constitutif ni peine des infractions. La loi pénale et la validité des actes antérieurs gardent leur régime ; le V ne valide pas un acte irrégulier. Les textes pénaux et sanitaires extérieurs cités ne sont pas intégralement fournis ni déclarés réécrits. La date historique du 1er juillet 2021 reste distincte de la réforme.",
    impact('coordination_only',
        "Deux renvois à des articles administratifs devenus impropres sont raccordés aux dispositions pénales actuelles qui renvoient déjà à L651-10 ; les garanties des quatre subdivisions sont intégralement conservées.",
        "Aucune baisse de prélèvement ni d'obligation n'est revendiquée. Les codes pénal et sanitaire extérieurs ne sont pas réécrits ; la correction n'étend pas les infractions ni leurs peines.",
        "Aucune charge nouvelle identifiée : mêmes désignation judiciaire, durée, informations, registres et droits de défense ; la transition dispense de refaire les actes réguliers et ne crée aucun agrément.",
        [effect('coordination', 'habitat-indigne-coordination-renvois-penaux',
            "Correction des deux références devenues administratives dans l'énumération des fondements de poursuite.",
            "Le I cite L511-6 et L184-1, qui régissent actuellement un signalement et la police administrative des hébergements.",
            "Le I cite L511-22 et L184-4 à L184-6, dispositions pénales dont les articles d'application raccordent déjà les poursuites à L651-10.",
            'other', "Exploitants poursuivis, occupants et propriétaires d'hébergements concernés par l'administration provisoire.",
            "Procédures en cours à l'entrée en vigueur ; actes réguliers non renouvelés et décisions définitives non remises en cause.",
            "Aucune procédure ou pièce nouvelle ; les conditions judiciaires et garanties des I à IV sont inchangées.",
            "L. 511-6, L. 521-4 et L. 184-1 du présent code",
            "L. 511-22, L. 521-4 et L. 184-4 à L. 184-6 du présent code")]))

for number, answer in answers.items():
    source = by_number[number]
    required = refs['requirements'][source['code_id'] + '|' + source['source_id']]
    answer['reference_checks'] = []
    for key in required:
        target = refs['targets'][key]
        assessment = reference_assessments[number][target['number']]
        answer['reference_checks'].append(dict(target_key=key,
            view_sha256=target['view_sha256'], assessment=assessment))

ordered = [answers[s['number']] for s in sources]
Path('answer.json').write_text(json.dumps(ordered, ensure_ascii=False, indent=2) + '\n')
