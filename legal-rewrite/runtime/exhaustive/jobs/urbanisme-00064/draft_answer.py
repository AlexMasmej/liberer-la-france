import copy
import html
import json
import re
from pathlib import Path


SOURCES = json.loads(Path('source.json').read_text())
BY_NUMBER = {a['number']: a for a in SOURCES}
ANSWERS = {}


def plain(xml):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]*>', ' ', xml))).strip()


def effect(number, kind, measure_id, description, before, after, unit,
           population, transition, burdens, source_quote, proposed_quote):
    assert source_quote in plain(BY_NUMBER[number]['source_xml']), (number, source_quote)
    return {
        'kind': kind, 'measure_id': measure_id, 'description': description,
        'before': before, 'after': after, 'unit': unit,
        'affected_population': population,
        'conditions_and_transition': transition,
        'replacement_or_new_burdens': burdens,
        'source_quote': source_quote, 'proposed_quote': proposed_quote,
    }


def add(number, proposed, reason, notes, classification, assessment, limitations,
        burdens, effects=None, removed=None, benefit=None):
    source = BY_NUMBER[number]
    a = {k: source[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}
    a.update(proposed_xml=proposed, reason=reason, review_notes=notes,
             status='retained_unchanged' if proposed is None else 'rewrite_draft')
    a['substantive_impact'] = {
        'version': 1, 'classification': classification,
        'assessment': assessment, 'scope_limitations': limitations,
        'new_burdens_review': burdens, 'effects': effects or [],
    }
    if proposed is None:
        a['classification'] = 'retained_necessary'
    if removed:
        a.update(change_type='normative_reduction',
                 reform_policy_id='editorial_direction_2026_10_19',
                 removed_provisions=removed)
    if benefit:
        a['benefit_review'] = benefit
    for e in a['substantive_impact']['effects']:
        assert proposed is not None and e['proposed_quote'] in plain(proposed), (number, e['proposed_quote'])
    ANSWERS[number] = a


def retain(number, reason, notes, assessment, limitations, benefit=None):
    add(number, None, reason, notes, 'retained_necessary', assessment, limitations,
        "Aucune charge nouvelle n'est identifiée : le corps officiel est maintenu intégralement, sans nouveau dossier, donnée, registre, délai ou condition.",
        benefit=benefit)


retain('R141-9',
       "Maintien intégral nécessaire, après examen de la charge documentaire : le rapport environnemental annexé donne accès aux incidences du SCoT, aux solutions de substitution, aux mesures d'évitement, de réduction et de compensation et au suivi. Il ne s'agit ni d'une autorisation supplémentaire ni d'un second rapport imposé en plus de celui de R. 104-18. Sa suppression affaiblirait l'évaluation et l'information du public ; aucun prélèvement, justificatif fiscal ou quota communal n'est institué ici.",
       "R. 104-18 a été lu intégralement dans le corpus : ses sept rubriques, dont Natura 2000, les indicateurs et le résumé non technique, sont préservées. Coordination avec L. 104-4 et avec le cadre européen d'évaluation des plans et programmes ; la conformité à ce cadre n'est pas certifiée par ce maintien. La note source relative à l'article 7 du décret n° 2021-639 et aux deuxième à cinquième alinéas de l'article 7 de l'ordonnance n° 2020-744 conserve son champ historique. Aucun achèvement de l'examen des 209 articles SRU n'est déduit de cet article.",
       "L'obligation existante d'annexer le rapport environnemental est conservée pour protéger l'évaluation et la participation ; aucune suppression de charge ni réécriture n'est revendiquée.",
       "Ce maintien ne valide pas tous les contenus des rapports ni les procédures hors du corpus ; aucune économie ou réduction nette de complexité n'est établie.")


p = """<p>En cas de modification ou de mise en compatibilité du schéma de cohérence territoriale, les annexes sont complétées par l'exposé des motifs des changements apportés. Toutefois, cet exposé n'a pas à être reproduit dans les annexes lorsqu'il figure déjà intégralement dans le dossier de la procédure accessible au public. Cette dispense ne porte ni sur l'exposé des motifs lui-même ni sur les pièces requises au titre de l'évaluation environnementale ou de la participation du public.</p>
<p>La dispense de reproduction s'applique aux procédures en cours à la date d'entrée en vigueur de la présente réforme. Elle n'impose ni de refaire les annexes déjà établies ni de renouveler une consultation ou une participation du public régulièrement accomplie.</p>"""
add('R141-10', p,
    "Réduction de fond ciblée : suppression de la reproduction obligatoire, dans les annexes, d'un exposé des motifs déjà intégralement présent dans le dossier accessible au public. Le motif de chaque changement reste exigé ; en l'absence d'exposé déjà accessible, la règle d'annexion demeure. Ce n'est pas une simple reformulation ni la suppression de la motivation environnementale.",
    "L. 143-34 a été lu : le projet de modification et l'exposé de ses motifs font déjà partie de la mise à disposition. La dispense porte sur la reproduction réglementaire dans les annexes et ne supprime pas les pièces exigées par L. 143-43, L. 143-44 et L. 143-46, ni le rapport de R. 141-9. Aucun nouveau droit d'accès aux données ni gain propre au CRPA n'est compté. Dossiers en cours couverts sans réouverture de participation ; les actes déjà adoptés ne sont pas invalidés.",
    'material_reduction',
    "Par rapport à la source entière, la duplication réglementaire de l'exposé des motifs dans les annexes cesse lorsque le dossier public le contient déjà ; son contenu et son accessibilité restent nécessaires.",
    "La dispense ne concerne pas un exposé absent du dossier public ni les pièces environnementales obligatoires. Le volume des copies évitées et le solde des coûts ne sont pas chiffrés.",
    "Aucune charge nouvelle n'est identifiée : la dispense est fondée sur un dossier et un accès public déjà existants ; elle n'oblige ni à créer un site, ni à publier une pièce supplémentaire, ni à fournir une attestation.",
    [effect('R141-10', 'obligation_removed', 'scot-expose-motifs-sans-duplication',
            "Fin de la reproduction systématique du même exposé dans les annexes du SCoT.",
            "Pour toute modification ou mise en compatibilité, ajout de l'exposé des motifs aux annexes, même si le dossier public le comporte déjà.",
            "Aucune reproduction dans les annexes si l'exposé est déjà intégralement dans le dossier accessible au public ; obligation inchangée dans les autres cas.",
            'legal_duty', "Établissements publics chargés des SCoT modifiés ou mis en compatibilité.",
            "Dispense applicable aux procédures en cours ; pas de réfection des annexes ni de participation régulière à renouveler.",
            "Aucun document de remplacement ; motivation et pièces environnementales conservées.",
            "les annexes sont complétées par l'exposé des motifs des changements apportés.",
            "cet exposé n'a pas à être reproduit dans les annexes lorsqu'il figure déjà intégralement dans le dossier de la procédure accessible au public.")],
    ["Reproduction obligatoire dans les annexes d'un exposé des motifs déjà intégralement présent dans le dossier de procédure accessible au public."])


retain('R141-11',
       "Maintien intégral utile du régime intégré SCoT–PCAET. Les 1°, 2° a), b) et c) placent la stratégie, le diagnostic, les actions, leurs responsables et le suivi dans les documents du SCoT : cette articulation permet un plan commun, elle n'impose pas deux plans distincts. Retirer une de ces composantes laisserait le schéma incomplet au regard de L. 141-17. Aucun taux, prélèvement ou agrément ne peut être supprimé dans ce texte de composition sans changer ce fondement.",
       "L. 141-16, L. 141-17 et L. 141-18 ont été lus ; le transfert et le plan commun restent facultatifs dans leurs conditions légales. Les renvois à R. 229-51 I à IV et R. 229-52 du code de l'environnement restent entiers ; leurs textes ne figurent pas dans les pièces locales consultées et aucune réécriture de ce code n'est affirmée. La note de transition de 2021 est conservée séparément dans la source, sans en faire la date de la réforme proposée.",
       "La source entière organise déjà l'intégration des éléments climat dans le schéma. Elle est maintenue, sans compter cette intégration existante comme un nouveau regroupement de régimes.",
       "Le contenu réglementaire environnemental externe n'a pas été intégralement vérifié faute de pièce locale ; aucun allègement supplémentaire ni bilan global n'est établi.")


p = """<p>Lorsque le schéma de cohérence territoriale tient lieu de plan climat-air-énergie territorial, la délibération prescrivant l'élaboration du schéma et précisant les objectifs poursuivis et les modalités de concertation prévue par l'article L. 143-17 est notifiée, outre aux personnes mentionnées au second alinéa de cet article, au préfet de région. La notification supplémentaire aux représentants des autorités organisatrices mentionnées à l'article L. 2224-31 du code général des collectivités territoriales et aux gestionnaires de réseaux d'énergie présents dans le périmètre du schéma n'est pas requise au titre du présent article. Les notifications dont ces personnes sont destinataires en application de l'article L. 143-17 demeurent requises.</p>
<p>Dans les deux mois à compter de la transmission de cette information, le préfet de région et le président du conseil régional adressent à l'établissement public de coopération intercommunale ou au groupement de collectivités territoriales compétent les informations qu'ils estiment utiles à l'élaboration des dispositions valant plan climat-air-énergie territorial du schéma.</p>
<p>La suppression des notifications supplémentaires s'applique aux formalités restant à accomplir à la date d'entrée en vigueur de la présente réforme, sans remise à zéro des délais ni renouvellement des notifications déjà effectuées. Elle ne supprime ni l'association et les consultations prévues par la loi ni l'accès du public à la procédure.</p>"""
add('R141-12', p,
    "Réduction de fond : les envois initiaux systématiques ajoutés par ce seul article à l'ensemble des autorités organisatrices de l'énergie et gestionnaires de réseaux sont retirés. Leur utilité ne justifie pas un circuit imposé à tous les schémas intégrés, en plus des notifications législatives, de l'association et de la participation maintenues. Le préfet de région reste destinataire ; le retour utile du préfet et de la région reste encadré par deux mois. Aucune déclaration de remplacement n'est créée.",
    "L. 143-17, L. 132-7, L. 132-8 et L. 132-11 ont été lus : tous les destinataires et droits d'association imposés par ces articles sont expressément réservés, même si une même personne relève aussi d'une catégorie énergétique. L. 143-20 7° conserve les consultations du volet PCAET. Vérifier hors des cinq codes l'articulation avec R. 229-53 du code de l'environnement et L. 2224-31 du CGCT ; leur texte intégral n'est pas disponible dans les pièces locales consultées. La réduction démontrée est celle du circuit supplémentaire de R. 141-12, sans affirmer que toute notification énergétique autonome disparaît. La note historique du décret n° 2021-639 reste applicable à son champ ; transition nouvelle limitée aux formalités non accomplies.",
    'material_reduction',
    "La notification additionnelle obligatoire à deux catégories d'acteurs énergétiques disparaît du corps officiel ; les notifications législatives et l'échange utile sous deux mois sont conservés.",
    "Le gain est limité aux envois supplémentaires fondés sur cet article. Les obligations éventuellement autonomes du code de l'environnement et du CGCT restent à confronter ; aucun solde intercodes n'est démontré.",
    "Aucune charge nouvelle n'est identifiée : pas d'attestation, de déclaration ni de portail en remplacement. Les obligations de notification législatives et les contributions sous deux mois existaient déjà.",
    [effect('R141-12', 'obligation_removed', 'scot-pcaet-fin-notifications-energetiques',
            "Suppression du circuit réglementaire additionnel de notification initiale aux acteurs énergétiques.",
            "Notification de prescription supplémentaire aux représentants des autorités organisatrices de l'énergie et à tous les gestionnaires de réseaux présents dans le périmètre.",
            "Aucun envoi supplémentaire à ces catégories sur ce fondement ; les notifications qui leur sont dues par L. 143-17 subsistent.",
            'legal_duty', "Établissements publics élaborant un SCoT tenant lieu de PCAET ; destinataires énergétiques concernés.",
            "Formalités restant à accomplir dès l'entrée en vigueur ; délais commencés et notifications régulières conservés.",
            "Pas de déclaration ni d'envoi de substitution ; obligations légales autonomes réservées.",
            "aux représentants des autorités organisatrices mentionnées à l'article L. 2224-31 du code général des collectivités territoriales ainsi qu'aux gestionnaires de réseaux d'énergie présents dans le périmètre du schéma.",
            "La notification supplémentaire aux représentants des autorités organisatrices mentionnées à l'article L. 2224-31 du code général des collectivités territoriales et aux gestionnaires de réseaux d'énergie présents dans le périmètre du schéma n'est pas requise au titre du présent article.")],
    ["Notification initiale supplémentaire imposée aux représentants des autorités organisatrices de l'énergie, en dehors des notifications législatives qui demeurent applicables.",
     "Notification initiale supplémentaire imposée aux gestionnaires de réseaux d'énergie présents dans le périmètre, sans déclaration de remplacement."])


retain('R141-13',
       "Maintien intégral nécessaire de la consultation régionale lorsque le SCoT vaut PCAET : l'avis porte sur la cohérence du projet arrêté avec les compétences climatiques et énergétiques de l'État. L. 143-20 7° conserve précisément les consultations du volet PCAET. Le texte coordonne leur application, sans exiger expressément deux avis du même préfet sur le même objet. Supprimer ce seul renvoi ne démontrerait donc pas la disparition d'une procédure autonome.",
       "L. 143-20 a été lu en entier ; ses autres destinataires, les consultations sur demande et les conditions de montagne sont conservés. Le renvoi à R. 229-54 du code de l'environnement reste entier ; son contenu externe n'a pas été récupéré localement et aucun délai n'est inventé. Les conditions d'entrée en vigueur de la note du décret n° 2021-639 restent distinctes de toute réforme future.",
       "Le renvoi procédural officiel est maintenu, car il met en œuvre une consultation du plan intégré appuyée sur la loi ; aucune deuxième consultation supprimée n'est prouvée.",
       "Sans le texte intégral local de R. 229-54, aucune suppression d'avis autonome ni réduction de son délai n'est revendiquée ; le bilan des coûts est inconnu.")


retain('R141-14',
       "Maintien intégral du rapport d'exécution du volet climat : il vérifie la réalisation des actions, complète le suivi prévu dans les annexes et ne constitue pas une taxe ou une autorisation. Le suivi et l'évaluation du PCAET sont expressément rattachés par L. 141-16 à L. 229-26 IV. L'article n'impose pas un second rapport en plus de celui auquel il renvoie ; son abrogation isolée n'établirait donc aucun gain réel.",
       "L. 141-16 et R. 141-11 ont été lus ; les responsables et le dispositif de suivi restent identifiés dans le plan intégré. R. 229-51 IV du code de l'environnement reste à vérifier sur pièce complète hors corpus ; aucune périodicité n'est modifiée ou reconstituée ici. La note de 2021 garde ses conditions historiques d'application. Le maintien n'est ni un audit des rapports produits ni une validation juridique externe.",
       "Le rapport réglementaire par renvoi est conservé pour rendre le suivi opérant ; la source ne démontre pas deux rapports obligatoires distincts que ce lot pourrait fusionner.",
       "L'articulation du rapport avec les autres bilans demeure à examiner sur les textes environnementaux complets ; aucune économie ni simplification nouvelle n'est comptée.")


retain('R141-15',
       "Maintien intégral d'une règle utile : la mise à jour du seul volet PCAET est coordonnée à L. 141-18, qui évite de réviser ou modifier l'ensemble du SCoT. La condition initiale évite une nouvelle mise à jour lorsque la révision l'a déjà réalisée. Retirer cet article pourrait rendre moins lisible cette voie favorable sans abolir l'obligation environnementale autonome.",
       "L. 141-18 a été lu : sa faculté d'adaptation ou de mise à jour sans révision globale demeure ouverte aux situations futures. Renvoi entier à R. 229-55, dont le texte n'est pas disponible dans les pièces locales consultées ; aucun délai de mise à jour n'est changé. La note du décret n° 2021-639 et de l'ordonnance n° 2020-744 est conservée dans son champ historique.",
       "La coordination existante évite une révision générale inutile ; elle est maintenue intégralement sans compter cet avantage déjà en vigueur comme une nouvelle réduction.",
       "La fréquence et le détail de la procédure environnementale ne sont pas réécrits ici ; aucune baisse de prélèvement ou de coût national n'est établie.")


p = """<p>Les opérations foncières et les opérations d'aménagement mentionnées au 4° de l'article L. 142-1 sont :</p>
<p>1° Les zones d'aménagement différé et les périmètres provisoires de zones d'aménagement différé ;</p>
<p>2° Les zones d'aménagement concerté ;</p>
<p>3° (Abrogé).</p>
<p>4° (Abrogé).</p>
<p>À compter de l'entrée en vigueur de la présente réforme, les lotissements, les remembrements réalisés par des associations foncières urbaines et les constructions soumises à autorisations portant sur une surface de plancher de plus de 5 000 mètres carrés, ainsi que la constitution, par des collectivités et établissements publics, de réserves foncières de plus de cinq hectares d'un seul tenant, ne sont plus soumis à la compatibilité directe avec le document d'orientation et d'objectifs du schéma de cohérence territoriale sur le fondement du 4° de l'article L. 142-1, sauf lorsqu'ils relèvent également du 1° ou du 2° du présent article. Les obligations résultant des autres dispositions de l'article L. 142-1, des documents d'urbanisme applicables et des législations environnementales, littorales, patrimoniales et de prévention des risques demeurent applicables.</p>
<p>Cette suppression s'applique aux décisions restant à prendre, y compris dans les procédures en cours, sans nouveau dépôt ni reprise des délais. Elle n'emporte ni modification des prescriptions des autorisations déjà délivrées ni remise en cause des décisions définitives ; les procédures ordinaires de modification et les recours demeurent applicables.</p>"""
add('R142-1', p,
    "Réduction de fond des doubles niveaux d'opposabilité : retrait des opérations diffuses et des réserves foncières des 3° et 4° de la liste réglementaire soumise directement au DOO du SCoT. Le seuil de 5 000 mètres carrés et celui de cinq hectares ne déclenchent plus cette obligation. La compatibilité stratégique des ZAD, périmètres provisoires et ZAC est conservée, ainsi que les documents d'urbanisme, les autres branches de L. 142-1 et les protections essentielles. Les subdivisions restent en place.",
    "L. 142-1 a été lu : son 4° renvoie précisément au décret pour cette liste ; aucun nouveau permis ni déclaration n'est substitué aux catégories retirées. L. 131-4 maintient la compatibilité des PLU et cartes communales avec le SCoT ; en l'absence de PLU, la disparition de l'opposabilité directe est aussi un changement réel, non une simple déduplication. Les autorisations commerciales, cinématographiques et permis tenant lieu d'autorisation commerciale des 5° à 7° de L. 142-1 restent soumis à leur compatibilité propre. Les opérations intégrées à une ZAD ou ZAC restent couvertes par les 1° et 2°. Transition explicite pour les décisions à intervenir ; prescriptions anciennes et droits de recours conservés. Ni quotas SRU ni restrictions aux dérogations littorales ne sont ajoutés.",
    'material_reduction',
    "La liste officielle entière perd deux catégories de compatibilité directe au SCoT. Les seuils antérieurs cessent de déclencher cette obligation ; les deux catégories stratégiques et les fondements autonomes subsistent.",
    "La mesure ne dispense pas des PLU, autorisations, évaluations ni autres compatibilités légales. Les effets sur l'environnement, la construction et le contentieux ne sont pas chiffrés ; sans PLU, la réduction n'est pas seulement un doublon retiré.",
    "Aucune charge nouvelle n'est identifiée : aucun contrôle, formulaire, registre ou autorisation de remplacement. Les réserves relatives aux ZAD, ZAC et autres législations maintiennent des obligations déjà existantes.",
    [effect('R142-1', 'obligation_removed', 'scot-fin-compatibilite-directe-operations-diffuses',
            "Retrait des catégories 3° et 4° du champ de la compatibilité directe au DOO.",
            "Compatibilité directe des lotissements, remembrements d'associations foncières urbaines et constructions de plus de 5 000 m², et des réserves publiques de plus de cinq hectares d'un seul tenant.",
            "Ces deux seuils ne déclenchent plus la compatibilité directe du 4° de L. 142-1 ; couverture maintenue en cas de ZAD ou ZAC et par les autres branches légales.",
            'legal_duty', "Porteurs des opérations et constructions du 3° ; collectivités et établissements publics constituant les réserves du 4°.",
            "Décisions à prendre après l'entrée en vigueur, y compris dossiers en cours ; titres et prescriptions antérieurs non réécrits.",
            "Aucune formalité de substitution ; documents locaux, évaluations et compatibilités autonomes demeurent.",
            "3° Les lotissements, les remembrements réalisés par des associations foncières urbaines et les constructions soumises à autorisations, lorsque ces opérations ou constructions portent sur une surface de plancher de plus de 5 000 mètres carrés ; 4° La constitution, par des collectivités et établissements publics, de réserves foncières de plus de cinq hectares d'un seul tenant.",
            "ne sont plus soumis à la compatibilité directe avec le document d'orientation et d'objectifs du schéma de cohérence territoriale sur le fondement du 4° de l'article L. 142-1, sauf lorsqu'ils relèvent également du 1° ou du 2° du présent article.")],
    ["Compatibilité directe avec le DOO du SCoT imposée par le 3° aux lotissements, remembrements d'associations foncières urbaines et constructions au-delà de 5 000 mètres carrés, hors rattachement aux catégories conservées.",
     "Compatibilité directe imposée par le 4° à la constitution publique de réserves foncières de plus de cinq hectares d'un seul tenant, hors rattachement aux catégories conservées."])


p = """<p>La dérogation prévue à l'article L. 142-5 est accordée par le préfet de département. Si le préfet ne s'est pas prononcé dans les deux mois suivant la date de sa saisine, il est réputé avoir donné son accord.</p>
<p>L'avis de la commission départementale de la préservation des espaces naturels, agricoles et forestiers est réputé favorable s'il n'est pas intervenu dans un délai de deux mois à compter de la saisine du préfet. L'avis de cette même commission, requis de façon concomitante dans le cadre d'une procédure d'élaboration ou de révision d'un plan local de l'urbanisme ou d'une carte communale, tient lieu de l'avis demandé au titre de l'application de l'article L. 142-5, dès lors qu'il porte sur les mêmes secteurs.</p>
<p>Lorsque le projet a été soumis pour avis à la commission départementale d'aménagement commercial en application de l'article L. 752-4 du code de commerce, son examen par cette commission n'est pas subordonné à l'obtention préalable de la dérogation. L'autorisation ne peut toutefois être délivrée avant que la dérogation requise par les articles L. 142-4 et L. 142-5 ait été accordée, expressément ou tacitement.</p>
<p>Lorsqu'il est requis, l'avis de l'établissement public compétent pour élaborer le schéma de cohérence territoriale est réputé favorable s'il n'est pas intervenu dans un délai de deux mois à compter de sa saisine. Les avis requis sont sollicités en parallèle, dès la saisine du préfet ; leur sollicitation ne reporte pas le point de départ du délai dont il dispose pour statuer.</p>
<p>Le présent article s'applique aux demandes dont le préfet est saisi à compter de l'entrée en vigueur de la présente réforme. Pour les demandes en cours à cette date, le délai pour statuer expire à la première des deux dates suivantes : l'échéance du délai antérieur de quatre mois ou l'expiration de deux mois suivant cette entrée en vigueur. Les avis déjà recueillis restent valables ; les délais d'avis en cours ne recommencent pas. La faculté d'examiner le projet avant l'obtention de la dérogation s'applique aux examens restant à effectuer. Aucun refus définitif n'est rouvert.</p>"""
add('R142-2', p,
    "Réduction de fond : le délai de décision préfectorale passe de quatre à deux mois, avec accord tacite maintenu ; le verrou obligeant à obtenir la dérogation avant même l'examen commercial est supprimé. Les avis sont instruits en parallèle, dans leurs délais favorables de deux mois. La dérogation, ses conditions légales et l'interdiction de délivrer l'autorisation sans elle subsistent. Le réemploi de l'avis de la commission sur les mêmes secteurs est intégralement conservé, sans être présenté comme nouveau.",
    "L. 142-4 et L. 142-5 ont été lus : l'accord de l'État, les avis et les conditions environnementales et de déplacements ne sont pas supprimés. Le délai de deux mois est un nouveau choix de simplification, aligné sur les avis, et non un taux fiscal ou une durée déjà en vigueur. Le parallélisme est expressément organisé pour ne pas conserver deux mois supplémentaires après les avis. Hors des cinq codes, vérifier les modalités d'application de L. 752-4 du code de commerce pour supprimer tout gel préalable purement procédural ; son texte n'est pas présent dans les pièces locales consultées. Dossiers en cours : aucune naissance rétroactive d'un accord tacite ; échéance la plus favorable selon la transition explicite. Aucun avis tacite favorable ni usage futur de la dérogation n'est retiré.",
    'mixed',
    "La source entière prévoyait quatre mois de décision et un ordre obligatoire avant examen commercial. Le projet ramène le maximum à deux mois et retire cet ordre ; il impose en contrepartie l'organisation parallèle des saisines aux services.",
    "Les deux mois sont des mois, sans conversion artificielle en soixante jours. Les conditions de fond et l'obtention préalable à la délivrance de l'autorisation restent ; l'effet net sur les coûts des services est inconnu et la coordination commerciale externe reste à vérifier.",
    "Charge d'organisation explicitée pour les services : solliciter les avis en parallèle dès la saisine. Aucun nouveau justificatif privé, registre, donnée ou avis n'est créé. Le calendrier plus court peut accroître la charge d'instruction ; aucun solde public net n'est présumé.",
    [effect('R142-2', 'deadline_reduced', 'urbanisation-limitee-derogation-deux-mois',
            "Réduction du délai maximal de décision avec conservation de l'accord tacite favorable.",
            "Préfet : quatre mois à compter de la saisine, puis accord tacite ; avis de deux mois.",
            "Préfet : deux mois à compter de la saisine, puis accord tacite ; avis de deux mois maintenus et parallélisés.",
            'other', "Demandeurs de dérogation L. 142-5 et préfets instructeurs.",
            "Nouvelles saisines dès l'entrée en vigueur ; dossiers en cours à la première échéance entre ancien délai et deux mois après réforme.",
            "Saisines parallèles à organiser par les services ; aucun nouveau avis ni document privé.",
            "Si le préfet ne s'est pas prononcé dans les quatre mois suivant la date de sa saisine, il est réputé avoir donné son accord.",
            "Si le préfet ne s'est pas prononcé dans les deux mois suivant la date de sa saisine, il est réputé avoir donné son accord."),
     effect('R142-2', 'obligation_removed', 'urbanisation-limitee-fin-gel-examen-commercial',
            "Fin de la subordination de l'examen commercial à une dérogation déjà obtenue.",
            "Dérogation obligatoire avant l'examen du projet par la commission départementale d'aménagement commercial saisie pour avis.",
            "Examen possible en parallèle ; l'autorisation demeure subordonnée à l'accord exprès ou tacite de dérogation.",
            'legal_duty', "Porteurs de projets soumis à l'avis commercial de L. 752-4 et commissions départementales.",
            "Examens non encore effectués à l'entrée en vigueur ; refus définitifs non rouverts.",
            "Aucun avis de remplacement et aucune nouvelle autorisation ; condition légale de délivrance maintenue.",
            "la dérogation doit être obtenue avant l'examen du projet par ladite commission.",
            "son examen par cette commission n'est pas subordonné à l'obtention préalable de la dérogation."),
     effect('R142-2', 'obligation_added', 'urbanisation-limitee-derogation-deux-mois',
            "Organisation obligatoire de la sollicitation parallèle des avis pour rendre effectif le délai réduit.",
            "La source fixe les délais d'avis mais ne prescrit pas expressément leur sollicitation parallèle dès la saisine.",
            "Le préfet sollicite les avis requis en parallèle dès sa saisine, sans différer son délai de décision.",
            'legal_duty', "Préfectures et organismes dont l'avis est légalement requis.",
            "Nouvelles demandes ; les avis déjà recueillis et les délais d'avis en cours ne sont pas repris.",
            "Organisation publique plus contrainte, sans ajout d'avis ; coût net non établi.",
            "L'avis de la commission départementale de la préservation des espaces naturels, agricoles et forestiers est réputé favorable s'il n'est pas intervenu dans un délai de deux mois à compter de la saisine du préfet.",
            "Les avis requis sont sollicités en parallèle, dès la saisine du préfet ; leur sollicitation ne reporte pas le point de départ du délai dont il dispose pour statuer.")],
    ["Deux mois supplémentaires du délai de décision préfectorale sur les nouvelles demandes de dérogation, le maximum passant de quatre à deux mois avec accord tacite.",
     "Obligation d'obtenir la dérogation avant l'examen du projet par la commission départementale d'aménagement commercial saisie pour avis en application de L. 752-4."] ,
    "La dérogation à l'urbanisation limitée de L. 142-5 reste ouverte aux opérations futures comme aux demandes en cours, sous toutes ses conditions de fond. L'accord tacite du préfet subsiste et intervient plus tôt pour les nouvelles saisines. Les deux avis tacites favorables à deux mois sont conservés, ainsi que l'avis concomitant de la commission tenant lieu d'avis pour les mêmes secteurs. La suppression du gel concerne l'examen commercial, sans supprimer la voie dérogatoire ni imposer une attestation nouvelle ; les refus définitifs et les autorisations antérieures ne sont pas rouverts.")


p = """<p>Pour les projets relevant du 4° de l'article L. 142-4, la demande d'autorisation vaut demande de dérogation à cet article. Le demandeur n'a pas à présenter une demande de dérogation distincte. L'autorité qui reçoit la demande d'autorisation la transmet sans délai au préfet de département et lui communique sa date de dépôt. Ce dépôt vaut saisine du préfet pour le calcul du délai prévu à l'article R. 142-2. Les éléments nécessaires à l'examen des conditions de l'article L. 142-5 sont instruits dans ce dossier commun, sans seconde production des mêmes pièces.</p>
<p>Le présent article s'applique aux demandes d'autorisation déposées à compter de l'entrée en vigueur de la présente réforme. Pour les demandes en cours à cette date qui n'ont pas déjà donné lieu à la saisine du préfet, l'autorité qui les détient les lui transmet sans nouveau dépôt du demandeur ; le délai de l'article R. 142-2 court alors de cette entrée en vigueur. Les dérogations acquises et les dates de saisine déjà établies sont conservées ; une demande déjà présentée n'est pas renouvelée et aucun délai ne recommence.</p>"""
add('R142-3', p,
    "Réduction de fond et transfert explicite de circuit : le demandeur ne présente plus personnellement une demande de dérogation distincte de son autorisation pour le 4° de L. 142-4. La demande d'autorisation vaut saisine et l'autorité réceptrice transmet au préfet. La décision dérogatoire et les données utiles à ses conditions restent distinctes de la décision d'autorisation ; aucune déclaration équivalente ne remplace la demande supprimée.",
    "L. 142-4 4° et L. 142-5 ont été lus ; la fusion de saisine ne s'étend pas aux ouvertures à l'urbanisation des 1° à 3°. R. 142-2 conserve la compétence du préfet et ses accords tacites ; même famille de mesure pour ce circuit, sans compter une seconde suppression d'autorisation. Hors corpus : coordonner les formulaires et circuits des autorisations du code de commerce L. 752-1 et du code du cinéma L. 212-7 et L. 212-8, sans affirmer ces textes déjà réécrits. Nouvelle obligation publique de transmission et risque de retard imputable aux services expressément assumés, avec point de départ conservé au dépôt. La transition ne crée pas d'accord tacite rétroactif à une date antérieure à la réforme et ne remet pas à zéro une saisine existante.",
    'mixed',
    "La source entière faisait présenter la demande de dérogation par le demandeur d'autorisation. Le dépôt unique supprime cette saisine personnelle distincte, mais ajoute une transmission et la communication de la date entre autorités.",
    "Le préfet continue à décider et à contrôler les conditions de L. 142-5. Seuls les projets du 4° sont couverts ; formulaires et circuits commerciaux et cinématographiques externes restent à coordonner. Le solde public et privé n'est pas chiffré.",
    "Charge nouvelle pour l'autorité réceptrice : transmettre au préfet le dossier et sa date, y compris les dossiers en cours non encore transmis. Aucune nouvelle donnée, attestation ou déclaration du demandeur ; les éléments de fond nécessaires restent requis une seule fois.",
    [effect('R142-3', 'obligation_merged', 'urbanisation-limitee-saisine-unique-autorisation',
            "Fusion de la saisine personnelle de dérogation avec le dépôt d'autorisation pour le seul 4°.",
            "Demande de dérogation au 4° présentée par le demandeur d'autorisation, en plus de sa demande d'autorisation.",
            "Le dépôt d'autorisation vaut demande et saisine préfectorale ; pas de demande distincte ni de seconde production des mêmes pièces.",
            'legal_duty', "Demandeurs d'autorisations commerciales et cinématographiques concernés par L. 142-4 4°.",
            "Nouveaux dépôts dès la réforme ; dossiers en cours transmis d'office si préfet non encore saisi, sans perdre les accords ou saisines acquis.",
            "Transmission désormais à la charge de l'autorité réceptrice ; aucune autorisation de fond supprimée.",
            "La demande de dérogation au 4° de l'article L. 142-4 est présentée par le demandeur de l'autorisation.",
            "Le demandeur n'a pas à présenter une demande de dérogation distincte."),
     effect('R142-3', 'obligation_added', 'urbanisation-limitee-saisine-unique-autorisation',
            "Transmission administrative du dossier commun et de sa date au préfet.",
            "La source met la présentation de la demande de dérogation à la charge du demandeur, sans transmission d'office prévue ici.",
            "L'autorité recevant l'autorisation transmet sans délai au préfet et communique la date de dépôt, point de départ du délai.",
            'legal_duty', "Autorités réceptrices et préfectures compétentes.",
            "Nouveaux dépôts et demandes en cours non encore soumises au préfet ; délais déjà ouverts non recommencés.",
            "Charge de circulation publique explicitement ajoutée ; coût net inconnu et aucune nouvelle donnée privée.",
            "La demande de dérogation au 4° de l'article L. 142-4 est présentée par le demandeur de l'autorisation.",
            "L'autorité qui reçoit la demande d'autorisation la transmet sans délai au préfet de département et lui communique sa date de dépôt.")],
    ["Présentation personnelle obligatoire d'une demande de dérogation distincte de la demande d'autorisation pour les projets relevant de L. 142-4 4°."] ,
    "L'article organise l'accès à une dérogation favorable au 4° de L. 142-4 : cet accès demeure ouvert à tous les projets futurs éligibles, sans option préalable ni double demande. Les dérogations déjà acquises et les saisines en cours conservent leurs effets ; l'accord exprès ou tacite et les avis favorables de R. 142-2 ne sont pas retirés. La fusion du dépôt ne modifie aucune condition de fond de L. 142-5 et ne se substitue pas à une exonération fiscale, inexistante dans cette source.")


retain('R143-2',
       "Maintien intégral nécessaire de la règle désignant le président qui conduit l'élaboration du SCoT. Elle ne crée ni commission, agrément, déclaration ni délai et ne duplique pas une saisine du porteur de projet. La compétence institutionnelle est indispensable au déroulement de la procédure ; sa suppression laisserait incertain l'acteur chargé de l'exécuter sans démontrer de charge retirée.",
       "L. 143-16 a été lu intégralement : l'établissement reste chargé de l'élaboration, de l'approbation, du suivi et de l'évolution ; la conduite présidentielle ne transfère pas la compétence de l'organe délibérant. Aucun changement des catégories d'établissement ou des droits de vote territoriaux n'est introduit.",
       "Le sujet compétent pour conduire la procédure demeure celui de la source entière. Ce maintien institutionnel ne constitue ni une simplification ni une obligation supprimée.",
       "Aucun effet fiscal ou de délai ne découle de ce maintien ; les autres règles de compétence et de délibération gardent leur champ propre.")


retain('R143-3',
       "Maintien intégral de la consultation sur demande des personnes associées et de leurs représentants, pendant l'élaboration ou la révision. Il ne s'agit pas d'une réunion périodique imposée à tous : le texte met en œuvre le droit d'association de L. 132-11. Limiter arbitrairement le nombre de demandes pourrait empêcher une observation utile sur un projet modifié et supprimer un droit légal sans supprimer son fondement.",
       "L. 132-7, L. 132-8 et L. 132-11 ont été lus en entier. Le droit légal de demander une consultation durant l'élaboration demeure ; aucune règle n'impose ici un dossier supplémentaire ou un support particulier. Les consultations sur projet arrêté et la participation du public restent distinctes. Ce maintien ne rétablit aucun délai ni transmission supprimés en matière de négociation collective, hors champ.",
       "La source entière assure une consultation demandée par les personnes légalement associées. Aucun minimum de réunions ni nouveau reporting n'est conservé sous un autre nom.",
       "Les pratiques locales de consultations répétées ne sont pas mesurées ; le maintien d'un droit légal ne prouve aucune réduction de coût ou de délai.")


retain('R143-5',
       "Maintien intégral des avis techniques en cas de réduction des espaces agricoles ou forestiers, avec trois mois au maximum et avis favorable par silence. La chambre d'agriculture, l'INAO dans les zones AOC et, le cas échéant, le CNPF examinent des enjeux distincts ; aucune seconde consultation expressément obligatoire de chacun sur le même objet n'est prouvée par cette source. Le renvoi législatif rural empêche de présenter une abrogation réglementaire isolée comme la suppression de ces avis.",
       "L. 143-20, L. 132-7 et R. 143-4 ont été lus : la chambre est aussi personne associée et le délai général des avis est de trois mois, mais la source ne prescrit pas deux documents d'avis distincts. Le texte intégral de L. 112-3 du code rural et de la pêche maritime n'est pas présent dans les pièces locales consultées : sa coordination éventuelle ne peut être réputée faite. Trois mois et silence favorable sont intégralement conservés pour l'élaboration, la révision et la modification. La note historique de 2021 reste à son champ, sans date future inventée.",
       "La consultation technique ciblée et son silence favorable sont conservés intégralement. Aucun doublon formel démontré, taxe ou autorisation nouvelle n'est supprimé artificiellement.",
       "Les conditions législatives rurales extérieures restent à confronter sur texte entier. L'économie d'une éventuelle mutualisation déjà possible n'est pas comptée comme un gain nouveau.")


p = """<p>Lorsque le périmètre du schéma de cohérence territoriale comprend une ou des communes littorales et que le schéma fait application des articles L. 141-12 à L. 141-14, le préfet maritime est consulté préalablement à :</p>
<p>1° (Abrogé) ;</p>
<p>2° L'arrêt du projet de schéma en application de l'article L. 143-20 ;</p>
<p>3° (Abrogé).</p>
<p>À compter de l'entrée en vigueur de la présente réforme, la consultation distincte du préfet maritime n'est plus requise au titre du présent article pour l'arrêt du périmètre du schéma ou son approbation. La consultation préalable à l'arrêt du projet, les règles de protection du milieu marin, les dispositions particulières au littoral et les dérogations légalement applicables demeurent.</p>
<p>Ces dispositions s'appliquent aux consultations restant à effectuer dans les procédures en cours. Les avis déjà recueillis restent au dossier ; leur suppression pour l'avenir n'impose ni nouvelle consultation ni reprise de la procédure et ne remet pas en cause les actes déjà adoptés ou les droits de recours.</p>"""
add('R143-6', p,
    "Réduction de fond : deux des trois consultations réglementaires successives du préfet maritime sont retirées, celles sur le périmètre et avant approbation. Une consultation demeure avant l'arrêt du projet, lorsque son contenu maritime peut être effectivement examiné ; l'État reste associé et les protections de fond ne sont pas abaissées. Les numéros 1° et 3° restent explicitement abrogés. Aucune déclaration ni approbation de remplacement n'est ajoutée.",
    "L. 143-6, L. 143-20, L. 143-23, R. 141-8 et L. 141-12 à L. 141-14 ont été lus intégralement. La définition du périmètre reste une décision de l'État ; le diagnostic littoral, le contenu maritime et les mesures de protection du milieu marin demeurent. Cette réduction ne ferme ni le schéma de plage ni les dérogations littorales de L. 121-28 à L. 121-30 et ne modifie pas leurs avis autonomes. La filiation SRU de ces dispositions n'est pas affirmée sans dossier historique ; aucun achèvement des 209 articles. La note source de 2021 conserve son champ historique ; seuls les avis futurs sur ce fondement sont supprimés, y compris en procédure pendante.",
    'material_reduction',
    "La source entière exigeait trois étapes de consultation maritime ; le projet en conserve une avant l'arrêt du projet et supprime celles du périmètre et de l'approbation, sans réduction des protections littorales de fond.",
    "Les avis maritimes prescrits par d'autres régimes demeurent. La fréquence réelle des avis évités et l'effet sur les délais ou l'environnement ne sont pas chiffrés ; aucune filiation historique exhaustive n'est démontrée.",
    "Aucune charge nouvelle n'est identifiée : pas de déclaration, registre ni consultation de remplacement. Le maintien au dossier des avis déjà recueillis ne crée pas de collecte ni d'envoi nouveau.",
    [effect('R143-6', 'obligation_removed', 'scot-consultation-maritime-projet-seul',
            "Suppression des consultations maritimes distinctes sur le périmètre et avant approbation.",
            "Consultation du préfet maritime avant trois étapes : périmètre, arrêt du projet, approbation du SCoT maritime et littoral.",
            "Seule la consultation avant l'arrêt du projet demeure sur ce fondement ; avis autonomes et protections de fond conservés.",
            'legal_duty', "Établissements chargés de SCoT littoraux faisant application de L. 141-12 à L. 141-14 et préfets maritimes.",
            "Consultations restant à accomplir dès la réforme ; avis existants conservés et aucun acte antérieur remis en cause.",
            "Aucune déclaration ni consultation compensatrice ; les régimes dérogatoires littoraux restent ouverts.",
            "1° L'arrêt du périmètre du schéma en application de l'article L. 143-6 ; 2° L'arrêt du projet de schéma en application de l'article L. 143-20 ; 3° L'approbation du schéma en application de l'article L. 143-23.",
            "la consultation distincte du préfet maritime n'est plus requise au titre du présent article pour l'arrêt du périmètre du schéma ou son approbation.")],
    ["Consultation systématique distincte du préfet maritime avant l'arrêt du périmètre du SCoT faisant application de L. 141-12 à L. 141-14.",
     "Consultation systématique distincte du préfet maritime avant l'approbation du SCoT, en plus de l'avis conservé avant l'arrêt du projet."])


retain('R143-7',
       "Maintien intégral d'une faculté favorable : la même délibération peut arrêter le projet de SCoT et tirer le bilan de la concertation. Aucun acte séparé obligatoire, délai minimal ni pièce nouvelle n'en résulte. Supprimer cette faculté ou rendre deux délibérations obligatoires augmenterait les contraintes ; aucun allègement supplémentaire justifié n'est nécessaire.",
       "Le renvoi à L. 103-6 est conservé pour le bilan de concertation ; les garanties de concertation et la compétence de l'organe délibérant ne sont pas retirées. La simultanéité est facultative et reste ouverte pour les procédures futures, sans réexaminer les délibérations anciennes.",
       "La source entière autorise déjà une délibération commune. Cette possibilité est conservée sans être comptée comme une nouvelle fusion d'obligations.",
       "Le maintien ne modifie pas les modalités légales de concertation ni les actes exigés sur d'autres fondements ; aucun gain nouveau n'est mesuré.")


retain('R143-10',
       "Maintien intégral de l'examen conjoint avant enquête et de son procès-verbal au dossier : ces exigences rendent visible au public l'analyse de la compatibilité proposée et mettent en œuvre des obligations législatives. L'examen commun réunit déjà plusieurs intervenants ; rien n'impose dans cet article une seconde réunion séparée, un format physique ni un procès-verbal doublé. Aucun gain réel ne résulterait d'une simple reformulation.",
       "L. 143-43, L. 143-44 et L. 143-46 ont été lus intégralement : l'examen conjoint, son antériorité et le procès-verbal au dossier sont fondés par la loi. Les renvois de la source ne sont pas orphelins. Le maintien porte sur le champ de la source, sans transformer l'enquête en simple consultation ni prouver la conformité de chaque procédure au droit européen.",
       "La source entière organise l'examen commun et sa traçabilité dans l'enquête. Ces garanties législativement nécessaires restent entières ; aucun nouveau regroupement n'est revendiqué.",
       "Le maintien ne réduit pas la durée ni les pièces légalement requises de l'enquête ; aucune suppression de réunion doublonnée n'est démontrée.")


retain('R143-11',
       "Maintien intégral du mécanisme par lequel la déclaration de projet de l'établissement chargé du SCoT approuve aussi sa mise en compatibilité. Les deux voies des 1° et 2°, l'absence de DUP requise et la prise en compte des avis et résultats d'enquête restent nécessaires. Il s'agit déjà d'un acte commun, sans autorisation supplémentaire imposée par cette source ; retirer les pièces d'enquête ou l'examen conjoint affaiblirait l'instruction et la participation.",
       "L. 143-44, L. 143-46, L. 143-48 et L. 143-49 ont été lus : les acteurs, le projet d'intérêt général, l'enquête à double objet et l'approbation par déclaration de projet sont cohérents. Les renvois à L. 126-1 du code de l'environnement et L. 300-6 sont conservés ; aucune modification des régimes externes ni réouverture d'un acte ancien n'est affirmée.",
       "La source entière permet déjà que la déclaration de projet emporte approbation du schéma. Le maintien conserve cette intégration et les garanties du dossier, sans effet nouveau compté.",
       "Les dossiers concrets et le texte environnemental externe ne sont pas audités ici ; l'absence de nouveau corps ne démontre ni baisse de coût ni réduction du délai d'enquête.")


p = BY_NUMBER['R143-12']['source_xml'].replace(
    "Celui-ci dispose d'un délai de deux mois pour approuver ou refuser la mise en compatibilité du schéma.",
    "Celui-ci dispose, conformément au 4° de l'article L. 143-49, d'un délai de deux mois à compter de la réception de l'avis du commissaire enquêteur ou de la commission d'enquête pour approuver ou refuser la mise en compatibilité du schéma. La transmission du dossier ne reporte pas le point de départ de ce délai.")
p += """<p>La précision du point de départ du délai s'applique aux procédures engagées à compter de l'entrée en vigueur de la présente réforme, sous réserve des dispositions législatives applicables. Elle ne remet en cause ni les actes déjà adoptés, ni les droits acquis, ni l'application de l'article L. 143-49 aux procédures en cours et ne rouvre aucun délai expiré.</p>"""
add('R143-12', p,
    "Coordination nécessaire du délai avec son fondement législatif, sans réduction nouvelle revendiquée : le point de départ des deux mois est expressément la réception de l'avis du commissaire enquêteur ou de la commission d'enquête, comme le prévoit L. 143-49 4°, et non une transmission ultérieure du dossier susceptible de le reporter. Tout le reste du corps source est conservé : deux voies, tous les acteurs dont SNCF Réseau et sa filiale, conduite, pièces, substitution préfectorale, deux mois de notification et destinataire final. Aucun simple toilettage stylistique n'est ajouté.",
    "Écart préexistant corrigé explicitement après lecture de L. 143-44, L. 143-46, L. 143-48 et L. 143-49 : la source réglementaire ne précisait pas le déclencheur législatif à la réception de l'avis. L'avis visé par la loi n'est pas assimilé silencieusement au rapport et aux conclusions énumérés dans le dossier. Autre articulation préexistante laissée visible : R. 143-12 prévoit aussi la substitution en cas de désaccord, tandis que L. 143-49 4° énonce le défaut de délibération ; sécuriser expressément cette voie existante par une coordination de L. 143-49 4°, hors lot, sans retirer la possibilité d'approbation préfectorale aux projets. Le présent article ne prétend pas modifier ce fondement législatif. L. 2111-9 5° du code des transports reste à confronter hors corpus. La précision s'applique aux procédures nouvelles, sans neutraliser la loi déjà applicable aux procédures en cours ; aucune prescription ni délai de recours n'est rouvert.",
    'coordination_only',
    "La source entière est conservée, à l'exception de la précision du déclencheur légal des deux mois de décision locale et de sa transition. Ce délai ne peut pas repartir d'une transmission de dossier plus tardive ; aucun nouveau gain chiffré de délai n'est revendiqué.",
    "La coordination législative explicite de la substitution en cas de désaccord reste à sécuriser dans L. 143-49 hors lot, sans présenter cette voie réglementaire existante comme nouvellement créée. Le texte externe du code des transports et le solde des coûts ne sont pas vérifiés.",
    "Aucune charge nouvelle autonome n'est identifiée : le délai et son déclencheur sont déjà imposés par L. 143-49 4°. Aucun avis, pièce, donnée ou transmission supplémentaire n'est ajouté ; la compétence et les notifications existantes demeurent.",
    [effect('R143-12', 'coordination', 'scot-mise-compatibilite-delai-approbation-local',
            "Alignement exprès du départ des deux mois sur le fait prévu par la loi.",
            "Après transmission du dossier, la source donne deux mois à l'établissement sans préciser la réception de l'avis visée au 4° de L. 143-49.",
            "Deux mois depuis la réception de l'avis du commissaire enquêteur ou de la commission d'enquête ; une transmission ultérieure du dossier ne reporte pas ce départ.",
            'other', "Établissements chargés du SCoT et personnes publiques portant les projets visés aux 1° et 2°.",
            "Précision pour les procédures engagées après réforme ; loi applicable aux procédures en cours, actes et droits acquis préservés.",
            "Aucune procédure de remplacement ; aucun nouveau document d'avis requis par ce texte.",
            "Celui-ci dispose d'un délai de deux mois pour approuver ou refuser la mise en compatibilité du schéma.",
            "Celui-ci dispose, conformément au 4° de l'article L. 143-49, d'un délai de deux mois à compter de la réception de l'avis du commissaire enquêteur ou de la commission d'enquête pour approuver ou refuser la mise en compatibilité du schéma.")])


retain('R143-13',
       "Maintien intégral de la déclaration de projet de l'État, de l'avis de l'établissement dans un délai de deux mois avec silence favorable et de l'approbation simultanée du SCoT. Les deux branches, l'absence de DUP requise et l'ensemble du dossier préservent les compétences et la participation. Aucune formalité supplémentaire de demandeur ni second acte d'approbation n'est imposé ici ; la source est déjà intégrée.",
       "L. 143-48 1° et L. 143-49 2° ont été lus : l'avis local et l'approbation par déclaration de projet de l'État correspondent à ces fondements. Le silence favorable et le délai de deux mois demeurent, y compris pour les situations futures ; aucune réduction de délai n'est inventée. Les références environnementales externes restent à leur champ.",
       "La source entière intègre déclaration de projet et approbation des nouvelles dispositions du schéma, avec avis tacite favorable. Elle est conservée sans attribuer un gain à ce mécanisme existant.",
       "Aucune procédure externe de DUP ou de participation environnementale n'est supprimée ; les effets économiques et les durées concrètes ne sont pas évalués.")


p = """<p>I.-Font l'objet des mesures de publicité et d'information prévues à l'article R. 143-15 :</p>
<p>1° L'arrêté préfectoral qui délimite ou modifie le périmètre du schéma de cohérence territoriale, en application des articles L. 143-6 à L. 143-8 ;</p>
<p>2° L'arrêté préfectoral prononçant la déclaration d'utilité publique d'une opération ou, si une déclaration d'utilité publique n'est pas requise, la déclaration de projet, et mettant le schéma de cohérence territoriale en compatibilité avec cette opération dans les conditions prévues à l'article L. 143-49 ;</p>
<p>3° L'arrêté préfectoral mettant le schéma de cohérence territoriale en compatibilité avec une opération faisant l'objet d'une procédure intégrée mentionnée à l'article L. 300-6-1, dans les conditions prévues à l'article L. 143-49 ;</p>
<p>4° L'arrêté préfectoral mettant le schéma de cohérence territoriale en compatibilité avec les normes et documents mentionnés aux articles L. 131-1 et L. 131-2, en application des articles L. 143-42 et L. 143-43.</p>
<p>II.-Font l'objet des modalités de publicité sous forme électronique précisées à l'article R. 143-16 :</p>
<p>1° La délibération qui prescrit l'élaboration ou la révision du schéma de cohérence territoriale et qui définit les objectifs poursuivis ainsi que les modalités de la concertation. Il en est de même, le cas échéant, de la délibération qui définit les objectifs poursuivis et les modalités de la concertation lors de la modification du schéma de cohérence territoriale, en application du dernier alinéa de l'article L. 103-3 ;</p>
<p>2° La délibération qui arrête le projet de schéma de cohérence territoriale en application de l'article L. 143-20 ;</p>
<p>3° La délibération décidant de maintenir en vigueur ou de mettre en révision un schéma de cohérence territoriale, en application de l'article L. 143-28 ;</p>
<p>4° La décision ou la délibération prononçant la déclaration de projet, en application de l'article L. 143-49 ;</p>
<p>5° La délibération qui approuve la modification ou la révision du schéma de cohérence territoriale ;</p>
<p>6° La délibération ou l'arrêté mettant le schéma en compatibilité dans le cadre d'une procédure intégrée prévue à l'article L. 300-6-1 ;</p>
<p>7° La décision mentionnée à l'article R. 104-33, de réaliser ou non une évaluation environnementale lors de l'élaboration du projet de schéma de cohérence territorial, ou en cas de modification ou de mise en compatibilité.</p>
<p>Les corrections de renvois du présent article s'appliquent aux mesures de publicité restant à accomplir à la date d'entrée en vigueur de la présente réforme. Les procédures demeurant régies par les dispositions antérieures conservent les normes et documents de référence prévus par ces dispositions. Les publicités régulièrement accomplies ne sont pas renouvelées et aucun délai de recours expiré n'est rouvert.</p>"""
add('R143-14', p,
    "Coordination nécessaire, sans nouvelle réduction comptée : le I 4° est rattaché aux normes supérieures du SCoT de L. 131-1 et L. 131-2, au lieu des listes propres aux PLU de L. 131-4 et L. 131-5. Au II 1°, la référence à L. 103-3 vise son dernier alinéa au lieu du quatrième, aujourd'hui consacré à SNCF Réseau ; au II 5°, la référence inadaptée à L. 143-42 et L. 143-43 est retirée de la catégorie générale des délibérations approuvant modification ou révision. Les onze rubriques de publicité, leurs subdivisions, les deux circuits et les décisions d'évaluation restent entiers. Les allègements de presse sont portés par R. 143-15 et R. 143-16, pas comptés une nouvelle fois ici.",
    "Incohérences préexistantes identifiées, non correction silencieuse : lecture entière de L. 103-3, L. 131-1 à L. 131-5, L. 143-29, L. 143-32 à L. 143-34, L. 143-36 et L. 143-42 à L. 143-43. Le dernier alinéa de L. 103-3 porte la possibilité de fixer les modalités d'une concertation organisée sans obligation, alors que son quatrième alinéa vise désormais SNCF Réseau et sa filiale. L. 131-1 et L. 131-2 énumèrent les normes et documents du SCoT ; L. 131-4 et L. 131-5 concernent les documents locaux. L. 143-42 et L. 143-43 traitent de la mise en compatibilité à l'initiative de l'État et ne constituent pas le fondement général des révisions et modifications. L. 143-24 III impose déjà la publicité des évolutions et de leurs délibérations ; aucune catégorie nouvelle n'est revendiquée. Renvoi de L. 143-36 jusqu'à L. 143-26 absent du corpus signalé comme coordination législative hors lot. Les régimes historiques demeurent selon leurs transitions, notamment celle des procédures en cours au 26 mai 2026 ; cette date source n'est pas celle de la présente réforme. Aucun quota communal n'est recréé par la liste.",
    'coordination_only',
    "Les renvois de la liste officielle de publicité sont remis en cohérence avec les normes applicables aux SCoT et les catégories d'évolutions. Les actes à rendre publics restent les mêmes ; aucun allègement autonome n'est compté.",
    "Cette coordination ne réécrit ni les procédures législatives ni les régimes antérieurs ; l'articulation du renvoi absent L. 143-26 reste à traiter hors lot. Aucun solde de coût ou de complexité n'est établi.",
    "Aucune charge nouvelle n'est identifiée : la liste conserve ses catégories et L. 143-24 III impose déjà la publicité des évolutions ; aucune nouvelle pièce, donnée, déclaration ou publication en double n'est demandée.",
    [effect('R143-14', 'coordination', 'scot-publicite-renvois-normes-superieures',
            "Correction des listes de normes supérieures visées par la publicité des mises en compatibilité.",
            "I 4° renvoie aux listes L. 131-4 et L. 131-5 propres aux documents locaux, alors qu'il vise un arrêté de mise en compatibilité du SCoT.",
            "I 4° vise L. 131-1 et L. 131-2, normes de compatibilité et de prise en compte du SCoT ; publicité de l'acte maintenue.",
            'other', "Préfets et établissements publics chargés de publier les actes relatifs aux SCoT.",
            "Publicités restant à accomplir ; références historiques conservées pour les procédures soumises au droit antérieur, sans recommencer les recours.",
            "Aucun dispositif de remplacement ni acte supplémentaire ; correction de renvoi uniquement.",
            "avec un document mentionné aux articles L. 131-4 et L. 131-5 en application des articles L. 143-42 et L. 143-43.",
            "avec les normes et documents mentionnés aux articles L. 131-1 et L. 131-2, en application des articles L. 143-42 et L. 143-43."),
     effect('R143-14', 'coordination', 'scot-publicite-renvois-evolutions',
            "Suppression d'un renvoi inadapté de la rubrique générale des modifications et révisions.",
            "II 5° rattache la délibération de modification ou révision aux seules procédures de L. 143-42 et L. 143-43.",
            "La rubrique vise la même délibération sans renvoi inadapté ; L. 143-24 III conserve sa portée de publicité des évolutions.",
            'other', "Établissements publics publiant une délibération de modification ou de révision de SCoT.",
            "Mesures futures de publicité, sans renouvellement des formalités accomplies ni réouverture des délais expirés.",
            "Aucune nouvelle catégorie d'actes et aucune publication supplémentaire revendiquée.",
            "5° La délibération qui approuve la modification ou la révision du schéma de cohérence territoriale en application des articles L. 143-42 et L. 143-43 ;",
            "5° La délibération qui approuve la modification ou la révision du schéma de cohérence territoriale ;"),
     effect('R143-14', 'coordination', 'scot-publicite-renvoi-concertation',
            "Rétablissement de l'alinéa pertinent de L. 103-3 pour la concertation lors d'une modification.",
            "II 1° vise le quatrième alinéa de L. 103-3, aujourd'hui consacré à SNCF Réseau et sa filiale.",
            "II 1° vise le dernier alinéa de L. 103-3, qui prévoit notamment la concertation organisée sans obligation ; aucune nouvelle concertation n'est créée.",
            'other', "Établissements publics rendant publique une délibération de concertation lors d'une modification de SCoT.",
            "Publicités restant à accomplir ; droit historique des procédures antérieures réservé.",
            "Aucun nouvel acte ou délai, simple correction explicite de référence ordinale.",
            "en application du quatrième alinéa de l'article L. 103-3 ;",
            "en application du dernier alinéa de l'article L. 103-3 ;")])


p = """<p>Tout acte mentionné au I de l'article R. 143-14 est publié au Recueil des actes administratifs de l'Etat dans le département.</p>
<p>Les actes mentionnés aux 2° à 4° du I de l'article R. 143-14 sont également affichés pendant un mois au siège de l'établissement public de coopération intercommunale compétent et dans les mairies des communes membres concernées. Cet affichage mentionne le ou les lieux où le dossier peut être consulté.</p>
<p>Aucune insertion dans un journal diffusé dans le département n'est requise au titre du présent article.</p>
<p>La suppression de l'insertion s'applique aux formalités de publicité restant à accomplir à la date d'entrée en vigueur de la présente réforme, y compris pour des actes antérieurs. Les publications et affichages déjà accomplis conservent leurs effets ; aucun affichage régulier n'est à recommencer pour ajouter cette mention. Aucun délai de recours expiré n'est rouvert. Les mesures de publicité ou d'information imposées par un autre fondement légal demeurent applicables.</p>"""
add('R143-15', p,
    "Réduction de fond : suppression de l'annonce obligatoire dans un journal départemental, en plus du recueil administratif et des affichages. L'information sur les lieux de consultation du dossier est reportée sur l'affichage déjà obligatoire : le contenu reste accessible sans acheter une insertion de presse. Publication au recueil, affichage d'un mois et lieux d'affichage demeurent. Ce transfert limité de contenu est identifié comme charge nouvelle d'affichage, sans prétendre à un solde national chiffré.",
    "Une seule famille de mesure avec R. 143-16 : scot-publicite-sans-annonce-presse. L. 143-43 et L. 143-50 conservent leurs conditions de publication et d'affichage, toutes deux maintenues ; L. 143-24 et ses dispositions de contrôle de légalité ne sont pas modifiés. Les publicités de DUP, d'enquête et environnementales fondées sur d'autres textes ne sont pas supprimées par ce seul article. Vérifier hors corpus les arrêtés et modèles de publicité pour ne pas réimposer cette insertion sur le seul fondement retiré. Transition applicable aux formalités non encore faites, même pour un acte ancien ; aucune réfection de publicité régulière ni réouverture des recours expirés.",
    'mixed',
    "L'insertion de presse obligatoire de la source entière disparaît ; le recueil et l'affichage d'un mois restent. L'affichage porte désormais l'adresse de consultation déjà exigée pour la publicité de presse, ce qui doit être recensé séparément.",
    "Seule l'annonce fondée sur R. 143-15 est retirée ; les autres publicités autonomes et leurs délais demeurent. Le coût des annonces évitées et celui de l'adaptation des affiches ne sont pas chiffrés ; le solde net global est inconnu.",
    "Ajout limité : reporter sur l'affichage existant les lieux de consultation du dossier. Aucune donnée supplémentaire à recueillir, aucun registre ni délai nouveau. Les affiches déjà régulières ne sont pas refaites ; coût d'adaptation public non évalué.",
    [effect('R143-15', 'obligation_removed', 'scot-publicite-sans-annonce-presse',
            "Fin de l'annonce départementale de presse en supplément du recueil et de l'affichage.",
            "Insertion en caractères apparents dans un journal diffusé dans le département, après publication au recueil et affichage.",
            "Aucune insertion de presse sur ce fondement ; recueil, affichage d'un mois et accès au dossier conservés.",
            'legal_duty', "Autorités publiant les actes préfectoraux des 2° à 4° du I de R. 143-14.",
            "Toute insertion restant à accomplir dès la réforme, même pour un acte ancien ; effets acquis et recours non rouverts.",
            "Lieu de consultation reporté sur l'affichage existant ; autres fondements de publicité maintenus.",
            "Mention de cet affichage est insérée en caractères apparents dans un journal diffusé dans le département.",
            "Aucune insertion dans un journal diffusé dans le département n'est requise au titre du présent article."),
     effect('R143-15', 'obligation_added', 'scot-publicite-sans-annonce-presse',
            "Report de la mention du lieu de consultation sur le support d'affichage existant.",
            "La formalité de presse mentionne le ou les lieux où le dossier peut être consulté.",
            "L'affichage existant indique le ou les lieux de consultation, sans annonce séparée ni reprise des affiches déjà régulières.",
            'legal_duty', "Services établissant les affichages des actes concernés.",
            "Affichages non encore accomplis après la réforme ; pas de réfection des affiches régulières antérieures.",
            "Contenu déplacé d'un support supprimé ; adaptation publique limitée, coût net non mesuré.",
            "Cette formalité de publicité mentionne le ou les lieux où le dossier peut être consulté.",
            "Cet affichage mentionne le ou les lieux où le dossier peut être consulté.")],
    ["Insertion en caractères apparents dans un journal départemental de la mention de l'affichage des actes visés aux 2° à 4° du I de R. 143-14."])


p = """<p>Par dérogation au premier alinéa de l'article R. 2131-1 du code général des collectivités territoriales, la publication sous forme électronique des actes mentionnés au II de l'article R. 143-14 ainsi que celle des documents sur lesquels ils portent s'effectue sur le portail national de l'urbanisme mentionné à l'article L. 133-1 selon des modalités fixées par arrêté du ministre chargé de l'urbanisme.</p>
<p>Lorsque la publication prévue au premier alinéa a été empêchée pour des raisons liées au fonctionnement du portail national de l'urbanisme ou à des difficultés techniques avérées, la publication sous forme électronique s'effectue dans les conditions prévues à l'article R. 2131-1 du code général des collectivités territoriales.</p>
<p>Lorsque la publication des actes mentionnés au II de l'article R. 143-14 du présent code est effectuée par voie d'affichage dans les conditions prévues au IV, relatif aux communes de moins de 3 500 habitants, de l'article L. 2131-1 du code général des collectivités territoriales, ces actes sont, le cas échéant, affichés pendant une durée d'un mois au siège de l'établissement public de coopération intercommunale compétent et dans les mairies des communes membres concernées.</p>
<p>Cet affichage mentionne le ou les lieux où le dossier peut être consulté. Aucune insertion dans un journal diffusé dans le département n'est requise au titre du présent article.</p>
<p>La suppression de l'insertion s'applique aux formalités de publicité restant à accomplir à la date d'entrée en vigueur de la présente réforme, y compris pour des actes antérieurs. Les publications et affichages déjà accomplis conservent leurs effets ; aucun affichage régulier n'est à recommencer pour ajouter cette mention. Aucun délai de recours expiré n'est rouvert. Les mesures de publicité ou d'information imposées par un autre fondement légal demeurent applicables.</p>"""
add('R143-16', p,
    "Réduction de fond coordonnée à R. 143-15 : retrait de l'annonce de presse lorsque la publicité prend la voie d'affichage. La publication des actes et documents sur le portail, le secours électronique en cas de panne ou difficulté avérée et l'option légale d'affichage pour les communes de moins de 3 500 habitants sont maintenus intégralement. Les lieux de consultation figurent désormais sur l'affichage existant ; ce report de contenu est expressément recensé, sans nouvelle plateforme ni attestation.",
    "Même measure_id scot-publicite-sans-annonce-presse que R. 143-15 : deux champs de la même mesure, non deux suppressions de taxe. L. 143-24 a été lu ; il conserve ses exigences propres, dont la publication de secours, l'information du préfet et la publication ultérieure sous six mois dans son champ. Les renvois du CGCT R. 2131-1 et L. 2131-1 IV sont maintenus ; leur texte intégral et l'arrêté ministériel d'application ne figurent pas dans les pièces locales consultées et ne sont pas déclarés réécrits. Seuil de 3 500 habitants, durée d'un mois, caractère éventuel de l'affichage et tous les documents publiés sont conservés. Aucune fermeture de la voie favorable en cas de panne ni de l'option légale d'affichage pour les situations futures.",
    'mixed',
    "Par rapport à la source entière, seule l'insertion de presse est retirée et son information de consultation rejoint l'affichage existant. Le portail, les documents, les secours techniques et l'option légale d'affichage restent ouverts.",
    "Cette branche complète la même mesure que R. 143-15 et ne vaut pas une taxe ou un portail supprimé. Les publicités de droit autonome subsistent ; le coût net et l'effet sur les recours ne sont pas mesurés.",
    "Ajout limité au contenu de l'affiche : indiquer les lieux de consultation déjà exigés pour l'annonce supprimée. Aucune donnée nouvelle, registre, compte numérique ni délai supplémentaire ; les affiches régulièrement faites ne sont pas refaites.",
    [effect('R143-16', 'obligation_removed', 'scot-publicite-sans-annonce-presse',
            "Retrait de l'annonce de presse dans la branche de publicité par affichage du II de R. 143-14.",
            "En cas d'affichage légal, une mention doit aussi paraître en caractères apparents dans un journal départemental.",
            "Affichage et accès au dossier conservés, sans insertion de presse sur ce fondement ; les voies électroniques demeurent identiques.",
            'legal_duty', "Établissements et communes concernés par la publicité des actes du II de R. 143-14 par affichage légal.",
            "Insertions restant à effectuer dès la réforme, même pour actes anciens ; aucune reprise d'affichage régulier ni recours expiré rouvert.",
            "Information de consultation reportée sur l'affiche ; aucune plateforme ni déclaration supplémentaire.",
            "Mention de cet affichage est insérée en caractères apparents dans un journal diffusé dans le département.",
            "Aucune insertion dans un journal diffusé dans le département n'est requise au titre du présent article."),
     effect('R143-16', 'obligation_added', 'scot-publicite-sans-annonce-presse',
            "Mention des lieux de consultation sur l'affiche, au lieu de l'annonce supprimée.",
            "Lieux de consultation mentionnés dans la formalité de publicité de presse.",
            "Lieux mentionnés sur l'affichage déjà prévu, sans devoir refaire les affiches régulièrement accomplies.",
            'legal_duty', "Services réalisant les affiches dans le champ du troisième alinéa.",
            "Affichages restant à accomplir après entrée en vigueur ; affichages réguliers préservés.",
            "Adaptation du support existant et données déjà requises ; coût public net inconnu.",
            "Cette formalité de publicité mentionne le ou les lieux où le dossier peut être consulté.",
            "Cet affichage mentionne le ou les lieux où le dossier peut être consulté.")],
    ["Insertion obligatoire en caractères apparents dans un journal départemental de la mention de l'affichage légal des actes du II de R. 143-14."] ,
    "Les avantages procéduraux possibles sont intégralement préservés : publication commune des actes et documents sur le portail national, voie électronique de secours en cas de panne ou de difficulté technique avérée, et publication par affichage dans le champ légal des communes de moins de 3 500 habitants. Ils restent disponibles pour les situations futures éligibles, avec la durée d'un mois et les lieux d'affichage inchangés. L'annonce de presse est supprimée ; aucune attestation de panne ou nouvelle condition d'accès n'est ajoutée. Les droits des publicités déjà régulièrement accomplies demeurent.")


p = """<p>Le rapport de présentation :</p>
<p>1° Expose les principales conclusions du diagnostic sur lequel il s'appuie ainsi que, le cas échéant, les analyses des résultats de l'application du plan prévues par les articles L. 153-27 à L. 153-30 ;</p>
<p>2° Analyse les capacités de densification et de mutation de l'ensemble des espaces bâtis identifiés par le rapport de présentation en vertu du quatrième alinéa de l'article L. 151-4.</p>
<p>Les études et les évaluations dont sont issues les conclusions et analyses mentionnées au 1° n'ont pas à être annexées au rapport sur le fondement du présent article. Cette dispense ne porte ni sur les conclusions et analyses elles-mêmes ni sur les pièces exigées au titre de l'évaluation environnementale, de la participation du public ou d'une autre disposition législative ou réglementaire.</p>
<p>La dispense d'annexion s'applique aux rapports restant à établir ou à compléter à la date d'entrée en vigueur de la présente réforme, dans le champ des procédures auxquelles le présent article est applicable. Elle ne modifie pas les règles transitoires de l'article 26 du décret n° 2021-1345 du 13 octobre 2021, n'impose pas la réfection des rapports déjà établis et n'entraîne pas le renouvellement des consultations ou participations régulièrement accomplies.</p>"""
add('R151-1', p,
    "Réduction de fond : suppression de l'annexion systématique de toutes les études et évaluations à l'origine des conclusions du diagnostic et des analyses. Le rapport conserve les conclusions, les analyses de résultats le cas échéant et l'analyse de densification et mutation de tous les espaces bâtis. Les pièces environnementales et de participation légalement requises restent entières ; aucune liste, attestation ou nouveau dépôt de remplacement n'est imposé. Les 1° et 2° ne sont pas renumérotés.",
    "L. 151-4 et R. 151-3 ont été lus intégralement : le diagnostic, la consommation d'espace, la densification, la justification des objectifs et l'évaluation environnementale restent opposables. Le quatrième alinéa de L. 151-4 reste celui de l'analyse de densification ; l'orientation de coordination ajoutant un diagnostic de réseaux dans un alinéa final ne déplace pas ce renvoi. La note source de l'article 26 du décret n° 2021-1345 est expressément réservée : procédures avec dispense antérieure et autres procédures historiquement régies par le droit antérieur ne sont pas fusionnées silencieusement. La réforme ne supprime pas les droits d'accès de droit commun aux études et n'invente pas de portail pour les remplacer. Le rapport environnemental et ses sept rubriques ne sont pas résumés ou abrogés.",
    'material_reduction',
    "La source entière impose l'annexion de toutes les études et évaluations sous-jacentes au 1°. Cette obligation générique disparaît ; les analyses et justifications utiles ainsi que les annexes imposées par d'autres fondements restent exigées.",
    "La suppression ne concerne que l'annexion générique de R. 151-1 dans son champ historique ; elle ne dispense ni d'étudier les enjeux ni des pièces environnementales autonomes. Aucun nombre de pages, délai gagné ou coût net n'est estimé.",
    "Aucune charge nouvelle n'est identifiée : pas de nouvelle liste des études, d'attestation ni de publication de remplacement. Le contenu essentiel du rapport et les pièces légalement exigées restent des obligations préexistantes.",
    [effect('R151-1', 'obligation_removed', 'plu-fin-annexion-generale-etudes-diagnostic',
            "Fin de l'annexion générique de toutes les études et évaluations sous-jacentes au diagnostic et aux analyses.",
            "Rapport exposant conclusions et analyses, avec annexion des études et évaluations dont elles sont issues.",
            "Conclusions et analyses conservées ; aucune annexion générique sur ce fondement, sous réserve des pièces environnementales et autres obligations légales autonomes.",
            'legal_duty', "Collectivités et établissements élaborant les rapports de présentation des PLU dans le champ de R. 151-1.",
            "Rapports à établir ou compléter dès la réforme, sans étendre le champ historique de l'article 26 du décret de 2021 ni refaire les procédures régulières.",
            "Aucun inventaire, justificatif ou dépôt de remplacement ; évaluation, participation et accès légal aux pièces préservés.",
            "et comporte, en annexe, les études et les évaluations dont elles sont issues ;",
            "Les études et les évaluations dont sont issues les conclusions et analyses mentionnées au 1° n'ont pas à être annexées au rapport sur le fondement du présent article.")],
    ["Annexion systématique au rapport de présentation des études et évaluations à l'origine des conclusions du diagnostic et des analyses, hors pièces requises par un fondement légal autonome."])


retain('R151-2',
       "Maintien intégral des six justifications des choix du PLU : elles permettent de contrôler la nécessité et la proportion des contraintes imposées aux constructeurs, la cohérence des orientations, la délimitation des zones et les servitudes d'attente. Retirer la justification des différences entre constructions ou des interdictions ferait disparaître une garantie contre les restrictions arbitraires. Le regroupement dans un seul rapport existe déjà ; aucune seconde série de rapports n'est imposée. Aucun impôt ou agrément n'est créé ici.",
       "L. 151-4, L. 151-9, L. 151-41, R. 151-19 et R. 151-20 ont été lus en entier : le 5° garde la justification particulière des zones sans règlement spécifique et des servitudes du 5° de L. 151-41. Les droits d'adaptation, de changement de destination, de réfection et d'extension limitée des constructions existantes préservés par ce dernier ne sont pas restreints. La durée maximale de cinq ans prévue au texte de renvoi n'est pas transformée en nouveau délai par le présent maintien. Les renvois à L. 151-6 et aux textes de zonage ne sont pas supprimés pour créer une dispense de motivation. Aucun quota communal ou objectif SRU de rattrapage n'est réintroduit.",
       "Le rapport reste l'unique support des justifications de la source entière ; celles-ci contrôlent les contraintes du règlement et les zonages. Aucun gain nouveau de regroupement, aucune taxe ni obligation supprimée n'est revendiqué.",
       "Ce maintien ne mesure pas le coût de chaque justification et ne vaut pas validation des restrictions d'un PLU donné ; les assouplissements de construction d'autres articles conservent leur champ propre.")


assert set(ANSWERS) == set(BY_NUMBER)
out = [ANSWERS[a['number']] for a in SOURCES]
Path('answer.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'output_file': 'answer.json', 'article_count': len(out)}, ensure_ascii=False))
