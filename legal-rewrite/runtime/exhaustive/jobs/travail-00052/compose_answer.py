import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
by_number = {a['number']: a for a in sources}
answers = {}


def impact(classification, assessment, scope, burdens, effects=None):
    return {
        'version': 1,
        'classification': classification,
        'assessment': assessment,
        'scope_limitations': scope,
        'new_burdens_review': burdens,
        'effects': effects or [],
    }


def entry(number, reason, notes, assessment, scope, burdens):
    source = by_number[number]
    result = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    result.update(
        proposed_xml=None,
        reason=reason,
        review_notes=notes,
        status='retained_unchanged',
        classification='retained_necessary',
        substantive_impact=impact('retained_necessary', assessment, scope, burdens),
    )
    answers[number] = result
    return result


def rewrite(number, xml, reason, notes, assessment, scope, burdens, effects,
            removed=None, classification='material_reduction'):
    source = by_number[number]
    result = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    result.update(
        proposed_xml=xml.strip(), reason=reason, review_notes=notes,
        status='rewrite_draft',
        substantive_impact=impact(classification, assessment, scope, burdens, effects),
    )
    if removed:
        result.update(change_type='normative_reduction',
                      reform_policy_id='editorial_direction_2026_10_19',
                      removed_provisions=removed)
    answers[number] = result
    return result


def effect(kind, measure, description, before, after, unit, population,
           transition, replacement, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure, description=description,
                before=before, after=after, unit=unit,
                affected_population=population, conditions_and_transition=transition,
                replacement_or_new_burdens=replacement,
                source_quote=source_quote, proposed_quote=proposed_quote)


# Les trois alinéas sources restent entiers ; la dispense nouvelle ne vise
# que les mises à jour techniques des deux premiers.
xml38 = by_number['L2312-38']['source_xml'].strip() + """
<p>Pour les modifications mentionnées aux deux premiers alinéas, l'information préalable n'est pas requise lorsqu'elles sont exclusivement techniques et ne changent ni la finalité des méthodes ou traitements, ni les données utilisées, ni les critères d'évaluation ou de décision, ni les effets sur les droits, les libertés ou les conditions de travail des personnes concernées. Cette dispense ne s'applique pas à l'information et à la consultation prévues au troisième alinéa. Elle ne dispense pas des informations ou consultations exigées sur un autre fondement légal ou par le droit de l'Union européenne. Aucun dossier, déclaration ou attestation propre au bénéfice de cette dispense n'est exigé.</p>
<p>La dispense s'applique aux modifications décidées à compter de l'entrée en vigueur de la loi qui l'institue. Les droits et recours relatifs aux décisions antérieures demeurent régis par les dispositions qui leur étaient applicables.</p>
"""
rewrite(
    'L2312-38', xml38,
    "Réforme de fond : suppression de l'information préalable systématique du CSE pour les seules modifications exclusivement techniques, sans effet sur les finalités, données, critères ou droits protégés. Les trois alinéas initiaux sont maintenus : information sur l'introduction des outils de recrutement et de gestion du personnel, information sur leurs autres modifications et consultation préalable sur la surveillance de l'activité. La dispense retire une démarche sans déclaration de remplacement ; ce n'est pas une reformulation à droit constant.",
    "L2312-8, L2312-14 et L2312-15 ont été lus dans le corpus : leurs consultations utiles et les recours ne sont pas écartés. Une mise à jour d'algorithme modifiant le classement des candidats, une nouvelle donnée ou une capacité de surveillance ne relève pas de la dispense. Les obligations autonomes de protection des données et celles du droit de l'Union, notamment relatives aux systèmes d'IA employés au travail, sont réservées ; leur texte intégral n'est pas fourni ici et leur conformité détaillée n'est pas affirmée. R342-30 CCH, lu intégralement, reprend cette attribution pour le comité social d'administration de l'ANCOLS : l'incidence de cette reprise réglementaire doit être coordonnée dans son lot, sans modification du statut des agents ni extension du contrat unique aux agents publics. La note d'entrée en vigueur de 2017 ne date pas cette réforme.",
    "La source entière imposait l'information sur toute modification des deux catégories d'outils. La proposition en excepte effectivement les modifications exclusivement techniques sans effets protégés ; elle laisse entière la consultation sur le contrôle des salariés. Aucun prélèvement n'est modifié.",
    "Le gain concerne uniquement l'information fondée sur les deux premiers alinéas. Il peut être nul lorsqu'un autre fondement impose la même information. La reprise de cette attribution par R342-30 CCH pour l'ANCOLS est identifiée, sans audit de toutes les reprises extérieures. Ni les coûts individuels ni un solde global des codes ne sont chiffrés.",
    "Aucune charge nouvelle n'est identifiée : pas de registre, dossier, attestation ou déclaration de dispense. Les critères délimitent l'allègement sans imposer une preuve administrative préalable ; les garanties et procédures autonomes restent celles du droit applicable.",
    [effect(
        'obligation_removed', 'cse-modifications-techniques-information',
        "Retrait de la notification préalable des mises à jour purement techniques des outils de recrutement et de gestion du personnel.",
        "Dans les entreprises relevant de cette section, information préalable sur toute modification des méthodes de recrutement et des traitements automatisés de gestion du personnel, y compris purement technique.",
        "Aucune information préalable au titre des deux premiers alinéas pour les seules modifications techniques sans changement des finalités, données, critères ou effets protégés ; les autres cas demeurent soumis à information.",
        'legal_duty', "Employeurs et CSE des entreprises d'au moins cinquante salariés relevant de la section.",
        "Modifications décidées après l'entrée en vigueur ; décisions antérieures et obligations européennes ou légales autonomes réservées.",
        "Aucune déclaration, attestation ou procédure de remplacement ; consultation sur les moyens de contrôle inchangée.",
        "Le comité social et économique est informé, préalablement à leur utilisation, sur les méthodes ou techniques d'aide au recrutement des candidats à un emploi ainsi que sur toute modification de celles-ci.",
        "Pour les modifications mentionnées aux deux premiers alinéas, l'information préalable n'est pas requise lorsqu'elles sont exclusivement techniques et ne changent ni la finalité des méthodes ou traitements, ni les données utilisées, ni les critères d'évaluation ou de décision, ni les effets sur les droits, les libertés ou les conditions de travail des personnes concernées.",
    )],
    ["Information préalable obligatoire du CSE sur les modifications exclusivement techniques des outils de recrutement et de gestion du personnel, dans les limites expresses de la dispense nouvelle."],
)

entry(
    'L2312-39',
    "Maintien intégral nécessaire après examen des charges : la saisine en temps utile, l'avis sur la restructuration assortie d'un PSE et sa communication à l'administration assurent une représentation collective effective avant les suppressions d'emploi. L'exclusion des accords des articles L1237-17 et suivants est conservée pour les accords futurs aussi. Le préavis individuel de quinze jours ne supprime ni cette consultation ni la procédure collective.",
    "L1233-30 et L1233-48 ont été lus : le procès-verbal adressé à l'administration comprend déjà les avis. Un même envoi peut donc satisfaire les deux textes ; aucune seconde transmission matériellement distincte n'est démontrée et aucune réduction fictive n'est comptée. L1237-17 et L1237-19-1 maintiennent un régime propre d'information pour les ruptures collectives consenties. Le renvoi obsolète à L2323-31 présent dans L1233-30 et L1233-58 est une incohérence de ces cibles, à coordonner vers les attributions actuelles, notamment L2312-39, sans modifier ces fichiers hors lot. La note de 2017 est historique.",
    "La totalité de la norme est conservée : pas de réunion, avis, délai ou transmission supprimé dans cet article. Le doublon de fondement ne prouve pas deux envois. La dérogation pour les accords collectifs demeure ouverte.",
    "Le maintien ne valide pas les renvois anciens des articles cibles hors lot et ne fixe pas à quinze jours la procédure collective. Aucun effet budgétaire ou coût net de conformité n'est établi.",
    "Aucune charge nouvelle n'est identifiée, puisque le texte source entier reste applicable sans nouveau dossier, délai, donnée ou destinataire. La transmission existante ne devient pas un envoi supplémentaire.",
)

entry(
    'L2312-40',
    "Maintien intégral du renvoi opératoire aux règles du licenciement collectif économique : il détermine la consultation du CSE dans un régime distinct de la rupture individuelle du contrat unique. Le supprimer sans maintenir cette articulation affaiblirait une protection collective essentielle ; il n'ordonne pas une consultation additionnelle indépendante de celle du titre visé.",
    "Lecture de L1233-30, L1233-48 et L1233-58 : délais de consultation, information administrative et traitement des procédures judiciaires demeurent distincts du préavis individuel. Les anciens renvois à L2323-31 dans certaines cibles doivent être coordonnés dans ces articles, sans les reproduire comme nouvelle référence ici. Le renvoi du présent article porte sur le titre III du livre II de la première partie, non sur un ancien numéro du comité d'entreprise. Aucune règle fiscale, indemnité ou aide n'est modifiée.",
    "La source entière est conservée ; le renvoi organise la consultation collective existante et ne constitue pas deux obligations cumulatives. Aucune réduction matérielle n'est revendiquée.",
    "Les modalités des licenciements collectifs sont hors du corps de cet article. Leur compatibilité européenne et leurs coordinations ne se déduisent pas du seul préavis du contrat unique.",
    "Aucune charge nouvelle n'est identifiée : maintien exact du texte, sans consultation supplémentaire, autorisation nouvelle, pièce ou nouveau délai.",
)

entry(
    'L2312-41',
    "Maintien intégral : la réunion sous trois jours permet l'information utile lors d'une concentration ; l'expertise demeure facultative et sa restitution intervient seulement si elle est décidée. La dispense déjà prévue lorsque le CSE se réunit au titre d'une OPA évite le véritable doublon. Supprimer la première information ou l'audition des conclusions retirerait une garantie d'examen de changements économiques majeurs.",
    "L2315-92 et L2315-93 ont été lus : l'expertise et l'accès aux documents des sociétés intéressées restent dans leur champ. Les trois jours sont un délai maximal d'information, non un délai minimal bloquant l'opération ; ils ne sont pas le préavis individuel. Le troisième alinéa et sa dispense pour les OPA restent applicables aux opérations futures. Les renvois L430-1/L430-3 du commerce et au règlement 139/2004 sont conservés tels que fournis ; ces textes extérieurs ne sont pas disponibles intégralement dans le corpus autorisé et leur concordance détaillée reste à vérifier, sans examen extérieur présenté comme accompli.",
    "Les trois alinéas sources restent entiers, y compris la faculté d'expertise et la réunion OPA satisfaisant la première obligation. Aucun nouveau gain ne résulte de la conservation de cette dispense déjà existante.",
    "Ni l'autorisation de concentration ni le droit de l'Union ne sont supprimés. L'article ne commande pas une réunion séparée exclusivement consacrée à chaque objet ; aucune suppression fictive d'un tel support n'est comptée.",
    "Aucune charge nouvelle n'est identifiée : aucun nouveau rapport, réunion, registre ou délai, puisque l'intégralité de la source est maintenue.",
)

entry(
    'L2312-42',
    "Maintien intégral des premières informations des CSE de la cible et de l'offrant et des facultés d'audition et d'expertise : elles rendent effectif l'examen des conséquences sur l'emploi. Le deuxième alinéa règle spécialement la réunion chez l'offrant par L2312-49 ; il ne commande pas, à lui seul, une seconde réunion identique. La suppression d'un prétendu double circuit ne serait donc pas un gain démontré.",
    "L2312-43 à L2312-50 et L2315-92/93 ont été confrontés. L'information sur le caractère sollicité de l'offre, le choix d'entendre l'offrant et le jugement amical ou hostile sont tous conservés. La dérogation L2312-49 dispense de consultation avant lancement, y compris pour les offres futures ; ses deux jours ouvrables sont distincts de l'immédiateté de l'information de la cible et du préavis individuel. L'allègement de publication du rapport proposé à L2312-46 ne supprime ni sa désignation ni son examen.",
    "Le dispositif initial de l'OPA reste intégralement en source. Il protège la participation des salariés sans imposer d'expertise systématique. Aucune réunion ou taxe supprimée n'est revendiquée.",
    "La conservation ne préjuge pas de la réglementation financière extérieure. Elle n'assimile ni une information à une autorisation de l'OPA ni deux dispositions organisant la même réunion à deux réunions obligatoires.",
    "Aucune charge nouvelle n'est identifiée : les deux réunions des deux entreprises, les informations et les facultés du comité sont maintenues telles qu'elles figurent dans la source.",
)

entry(
    'L2312-43',
    "Maintien intégral de l'audition, lorsqu'elle est choisie par le CSE : son contenu industriel, financier, stratégique, territorial et social permet de confronter les intentions de l'offrant à leurs conséquences. L'assistance libre de l'offrant et celle du comité par l'expert sont conservées. La semaine est une borne maximale d'audition, non une attente obligatoire à retirer.",
    "Concordance vérifiée avec le dernier alinéa de L2312-42 et avec L2312-45/46. Le terme « dernier alinéa » reste exact puisque L2312-42 est maintenu intégralement. La disparition proposée du suivi légal périodique L2312-51 n'efface pas les engagements pris lors de l'audition ni leurs effets contractuels autonomes. Le délai d'une semaine ne devient pas quinze jours par application du contrat unique. La note de 2017 reste historique.",
    "La source entière est maintenue, avec une audition subordonnée au choix du comité et des droits d'assistance des deux côtés. Il n'y a ni nouveau prélèvement ni formalité répétitive supprimée.",
    "L'audition ne vaut pas autorisation de l'offre ni engagement automatique de l'offrant sur chaque déclaration. Les effets des engagements relèvent de leur fondement propre, non d'une estimation de coût dans cet article.",
    "Aucune charge nouvelle n'est identifiée : aucun écrit, compte rendu périodique ou délai supplémentaire ne s'ajoute aux garanties sources.",
)

entry(
    'L2312-44',
    "Maintien intégral de la remise au CSE de la note d'information publiée : l'accès effectif du représentant des salariés à la documentation de l'offre est nécessaire et l'article ne lui impose pas de constituer un second dossier. Une publication destinée au marché ne prouve pas que le CSE a reçu une information effectivement utilisable. Les trois jours ne sont pas un délai minimal à supprimer.",
    "Le renvoi au III de L621-8 du code monétaire et financier concorde avec celui de L2312-50 et L2312-51 source. Son contenu intégral n'est pas fourni dans le corpus autorisé ; aucune suppression d'une exigence financière européenne n'est présumée. La source n'a pas de note historique. La réduction de publication du rapport d'expert à L2312-46 ne supprime pas la note d'information ni sa remise. Les supports de communication ne sont pas nouvellement prescrits.",
    "L'obligation unique de communication de la note, dans les trois jours de sa publication, est conservée ; elle matérialise l'information utile du CSE. Aucun doublon d'envoi effectivement distinct n'est démontré.",
    "Le présent maintien n'audite pas la note financière extérieure ni son calendrier de publication et ne promet aucun gain à partir d'une simple substitution de copie par un lien.",
    "Aucune charge nouvelle n'est identifiée : le document existe déjà pour l'offre, le destinataire et le délai restent ceux du texte source, sans nouveau registre ni accusé imposé.",
)

entry(
    'L2312-45',
    "Maintien intégral du rapport d'expertise choisi par le CSE et de son contenu complet : politique industrielle et financière, plans stratégiques, intérêts, emploi, sites et centres de décision. Le rapport éclaire l'avis du comité et n'est pas un rapport administratif annuel imposé à toute entreprise. Le délai de trois semaines protège la possibilité d'examen avant l'avis d'un mois.",
    "L2312-42, L2312-46 et L2315-92/93 ont été lus : la désignation reste facultative et l'accès aux pièces utiles subsiste. La suppression de la reproduction publique du rapport à L2312-46 ne touche pas son établissement, son examen ou les destinataires légalement nécessaires. Aucun délai minimal n'est créé ; aucune coordination du contrat unique n'affecte ces trois semaines. Le renvoi au dernier alinéa de L2312-42 reste opérant.",
    "La totalité du rapport source est maintenue pour les expertises décidées ; il n'est ni résumé ni remplacé par une attestation. Aucun gain matériel propre à cet article n'est compté.",
    "Le coût de l'expertise et son financement relèvent des dispositions propres non modifiées ici. Le retrait de sa publicité dans un autre article n'est pas compté une seconde fois comme suppression du rapport.",
    "Aucune charge nouvelle n'est identifiée : désignation, contenu et délai existants inchangés, sans nouveau rapport destiné à compenser l'allègement de L2312-46.",
)

xml46 = by_number['L2312-46']['source_xml'].replace(
    "L'avis du comité social et économique ainsi que le rapport de l'expert-comptable sont reproduits",
    "L'avis du comité social et économique est reproduit",
).strip() + """
<p>L'obligation de reproduire le rapport de l'expert-comptable dans la note en réponse ou dans la note d'information commune est supprimée pour les projets d'offre déposés à compter de l'entrée en vigueur de la loi qui institue cette suppression. Toutefois, si la consultation a été engagée avant cette date dans les conditions prévues à l'article L. 2312-47, cette obligation reste régie par les dispositions antérieures. La suppression ne dispense ni de l'établissement du rapport et de son examen par le comité dans les conditions prévues à l'article L. 2312-45 et au I du présent article, ni des informations exigées sur un fondement légal distinct dans les documents de l'offre. Elle n'impose aucun document de remplacement.</p>
"""
rewrite(
    'L2312-46', xml46,
    "Réforme de fond ciblée : suppression de la reproduction obligatoire du rapport intégral de l'expert-comptable dans la note en réponse ou la note commune. L'avis du CSE reste reproduit. Le I et le II sont conservés pour le reste, notamment rapport examiné avant l'avis du conseil, possibilité de présence de l'offrant, mois d'examen, consultation réputée acquise, communication judiciaire des pièces et prolongation exceptionnelle. L'allègement porte sur la publicité du rapport, non sur l'expertise ni sur le recours.",
    "Les cinq alinéas d'origine ont été comparés sans raccourcissement du II : dernier ressort, procédure accélérée au fond et exception tenant à la rétention manifeste de la société cible restent entiers. L2312-45 et L2315-93 conservent l'établissement et l'accès documentaire. L2312-47 applique toujours le présent article, avec sauvegarde expresse des consultations anticipées déjà engagées. Coordination financière hors lot : confronter le règlement général de l'AMF, ses instructions de notes et le code monétaire et financier ; les obligations autonomes d'information du marché restent réservées. Vérifier le socle européen d'information et de publication de l'avis des salariés, notamment la directive 2004/25/CE, sans prétendre qu'il a été intégralement relu ici. Aucun texte extérieur n'est déclaré modifié.",
    "La source entière imposait la reproduction de l'avis et du rapport d'expert. Seule celle du rapport est retirée pour les offres nouvelles ; l'expertise, l'avis public, les délais et les recours demeurent. Cette réduction documentaire ne réduit ni un impôt ni le nombre d'expertises.",
    "Pas d'allègement pour les offres déposées avant la réforme ou les consultations anticipées déjà engagées. Les informations financières dues sur un fondement autonome restent exigées ; leur coût et la conformité détaillée des textes extérieurs restent à vérifier.",
    "Aucune charge nouvelle n'est identifiée : pas de résumé, annexe, attestation ni publication de remplacement. Les informations autonomes réservées existaient déjà et ne sont ni étendues ni transformées en obligation de reproduire le rapport supprimée.",
    [effect(
        'obligation_removed', 'cse-opa-publication-rapport-expert',
        "Suppression de la reproduction obligatoire du rapport d'expert dans les notes publiques de l'OPA, en maintenant celle de l'avis du CSE.",
        "Société cible ou auteurs d'une note commune tenus d'y reproduire l'avis du CSE et le rapport de son expert-comptable.",
        "Seul l'avis du CSE doit être reproduit au titre de cet article ; le rapport reste établi et examiné par le comité, sans publicité intégrale obligatoire sur ce fondement.",
        'legal_duty', "Entreprises et auteurs des notes des OPA soumises à L2312-46, sous les exclusions de L2312-52.",
        "Projets déposés à compter de l'entrée en vigueur, sauf consultations anticipées engagées auparavant ; obligations autonomes d'information financière maintenues.",
        "Aucun document de remplacement ; avis public et expertise interne maintenus à leur champ antérieur.",
        "L'avis du comité social et économique ainsi que le rapport de l'expert-comptable sont reproduits dans la note en réponse établie par la société faisant l'objet de l'offre ou, s'il y a lieu, dans la note d'information commune établie par l'auteur de l'offre et la société faisant l'objet de l'offre.",
        "L'avis du comité social et économique est reproduit dans la note en réponse établie par la société faisant l'objet de l'offre ou, s'il y a lieu, dans la note d'information commune établie par l'auteur de l'offre et la société faisant l'objet de l'offre.",
    )],
    ["Reproduction obligatoire du rapport intégral de l'expert-comptable du CSE dans la note en réponse ou la note d'information commune des offres nouvelles, sans retrait de l'avis public du CSE."],
)

entry(
    'L2312-47',
    "Maintien intégral de l'option d'anticipation de l'information-consultation dès l'annonce de l'offre, à la demande de l'offrant et avec la possibilité pour la cible de réunir son CSE. Les deux jours ouvrables, le départ anticipé des délais et la reprise limitée aux changements significatifs sont conservés. La caducité protège un avis éclairé lorsque l'offre change ; ce n'est pas une formalité gratuite à retirer.",
    "Les renvois L2312-42 à L2312-46 restent actifs. L2312-46 proposé préserve l'ancienne obligation de reproduction du rapport pour les consultations anticipées déjà engagées avant la réforme. Le second alinéa distingue bien « deux jours » de « deux jours ouvrables » au premier ; aucune harmonisation silencieuse n'est faite. Le nouvel avis après changement significatif n'est pas transformé en procédure systématique pour chaque modification. Note historique de 2017 lue.",
    "La source entière et sa faculté d'anticipation demeurent applicables aux offres futures. Aucun délai supplémentaire n'est supprimé ici et la conservation d'une option favorable n'est pas une nouvelle mesure de réduction.",
    "Le maintien ne supprime pas les délais légaux d'OPA et ne permet pas de conserver un avis caduc. Le droit financier extérieur et les coûts de l'anticipation ne sont pas évalués globalement.",
    "Aucune charge nouvelle n'est identifiée : même option, mêmes points de départ et même reprise conditionnelle ; aucun consentement tacite, attestation ou nouvelle réunion systématique n'est ajouté.",
)

entry(
    'L2312-48',
    "Maintien intégral de la sanction garantissant l'effectivité de l'audition de l'offrant, personne morale ou physique, et des deux mécanismes favorables de levée. L'extension aux sociétés contrôlantes ou contrôlées prévient le contournement des droits de vote par le groupe. La supprimer isolément affaiblirait le droit d'être informé et entendu lors d'un changement de contrôle sans supprimer une formalité redondante.",
    "L2312-42 et L2312-46 maintiennent la demande d'audition. La sanction cesse le lendemain de l'audition ou faute de nouvelle convocation dans les quinze jours : ces garanties restent ouvertes aux situations futures, sans nouveau justificatif. Ces quinze jours ne sont pas le préavis individuel du contrat unique. L233-16 du commerce est une référence extérieure de contrôle inchangée, non une assimilation à une condition de taux inventée. La sanction ne frappe pas l'offre du seul fait de son dépôt.",
    "Aucune partie des quatre alinéas n'est supprimée. La sanction ciblée et sa levée automatique protègent simultanément l'audition du CSE et l'absence de blocage indéfini. Aucun allègement nouveau n'est compté.",
    "L'articulation avec les droits de vote et le contrôle du groupe relève aussi du code de commerce non fourni intégralement. Aucune conformité indépendante ou économie nationale n'est déduite du maintien.",
    "Aucune charge nouvelle n'est identifiée : pas de sanction, durée, déclaration ou procédure ajoutée ; les conditions existantes de levée restent exactement celles de la source.",
)

a49 = entry(
    'L2312-49',
    "Maintien intégral de la dérogation dispensant l'offrant de consulter le CSE avant de lancer l'OPA, pour toutes les offres futures éligibles. La réunion d'information postérieure sous deux jours ouvrables demeure nécessaire pour rendre l'information sociale effective sans rétablir la consultation préalable écartée. L'information écrite et précise sur l'offre et ses conséquences pour l'emploi est conservée sans rapport supplémentaire.",
    "L2312-14, L2312-42 et L2312-47 ont été lus : la dispense préalable a un renvoi exprès dans le droit commun, la réunion chez l'offrant relève du présent calendrier et l'annonce anticipée conserve son effet. Le premier alinéa de L2232-12 n'est pas en cause ici. Les deux jours ouvrables ne sont ni une attente de deux jours ni une modification du préavis individuel. La source de 2018 et sa note n'établissent aucune date d'entrée en vigueur du projet.",
    "La source entière conserve un avantage de procédure déjà existant, l'absence de consultation avant le lancement, et son information postérieure. Ni nouvelle réduction ni obligation supprimée ne sont revendiquées.",
    "La dispense vise le lancement de l'offre par l'offrant ; elle ne couvre pas les décisions ultérieures de restructuration, licenciement ou modification des conditions de travail soumises à leurs règles propres.",
    "Aucune charge nouvelle n'est identifiée : dispense, réunion, informations écrites et délai restent identiques, sans nouvelle approbation, plateforme ou attestation.",
)
a49['benefit_review'] = (
    "L'avantage identifié est la dérogation expresse à L2312-14 : l'employeur offrant peut lancer l'OPA sans consultation préalable du CSE. Il est maintenu intégralement, sans limitation aux offres anciennes, condition supplémentaire ou agrément de remplacement. L'option d'annonce anticipée de L2312-47 demeure également utilisable. La réunion sous deux jours ouvrables et les informations écrites précises sont la garantie postérieure existante, non une autorisation préalable réintroduite. Aucun autre avantage fiscal ou exonération de prélèvement ne figure dans cet article."
)

entry(
    'L2312-50',
    "Maintien intégral du dispositif d'information directe des salariés lorsqu'aucun CSE n'existe chez l'offrant ou dans la cible. Il évite qu'une absence de représentation prive les salariés de la note de l'offre. La transmission par l'employeur cible assure le relais vers ses salariés ; sa suppression au profit d'une publication générale ne garantirait pas le même accès effectif.",
    "Les trois étapes sont conservées : information directe par l'employeur sans CSE, envoi par l'offrant de la note à l'employeur cible sous trois jours de sa publication, relais sans délai aux salariés. Le III de L621-8 CMF est le même renvoi que dans L2312-44 ; texte extérieur non lu intégralement ici. La source est dépourvue de note historique. Le relais aux salariés n'est pas compté comme un doublon puisqu'il change de destinataire. L'exclusion de L2312-52 demeure entière dans son champ.",
    "L'information de remplacement de la représentation absente est conservée en entier. Aucun des relais à des destinataires distincts n'est artificiellement compté comme envoi redondant supprimé.",
    "Les obligations d'information financière de l'offre et les moyens concrets d'accès des salariés ne sont pas réécrits dans les textes extérieurs. Aucune économie chiffrée n'est démontrée.",
    "Aucune charge nouvelle n'est identifiée : aucun canal imposé, fichier de salariés, accusé individuel ou nouveau délai ne s'ajoute à la source.",
)

xml51 = """<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi qui prononce son abrogation.</p>
<p>Les comptes rendus périodiques au comité social et économique, prévus au cours des sixième, douzième et vingt-quatrième mois suivant la clôture d'une offre publique ayant donné à son auteur le contrôle de la société, ne sont plus exigés lorsque leur échéance est postérieure ou égale à cette date, y compris pour les offres clôturées auparavant. Aucun compte rendu de remplacement ni rattrapage de ces échéances supprimées ne peut être exigé sur le seul fondement du présent article ou d'un renvoi à celui-ci.</p>
<p>Les obligations dont l'échéance était antérieure à cette date ainsi que les droits, responsabilités et recours nés de leur inexécution restent régis par les dispositions antérieurement applicables.</p>
<p>L'abrogation ne libère pas l'auteur de l'offre des engagements valablement pris en matière d'emploi, de maintien des sites d'activité et de localisation des centres de décision. Les contrats, accords et obligations conventionnelles autonomes ainsi que les droits acquis demeurent applicables selon leurs règles propres. Les droits d'information et de consultation du comité et les obligations de l'auteur de l'offre ou de l'employeur fondés sur d'autres dispositions légales ne sont pas supprimés et ne sont pas étendus par le présent article.</p>"""
a51 = rewrite(
    'L2312-51', xml51,
    "Abrogation intégrale pour l'avenir de la norme spéciale de suivi périodique post-OPA. Les comptes rendus obligatoires à six, douze et vingt-quatre mois sont supprimés, sans nouveau rapport ni nouveau calendrier. Le suivi général du CSE et ses alertes économiques disposent de fondements autonomes ; cette triple reddition obligatoire ajoute un circuit sectoriel sans nécessité essentielle démontrée. Les engagements pris en matière d'emploi, de sites et de centres de décision ne sont pas effacés. Les échéances anciennes déjà dues, responsabilités et recours sont préservés.",
    "L2312-8, L2312-15, L2312-18/36 et L2312-63 à L2312-67 ont été lus : information utile et droit d'alerte restent autonomes. L2312-52 est coordonné dans le lot vers L2312-45 à L2312-50. L2316-2, lu intégralement dans le corpus public, contient encore la plage L2312-42 à L2312-51 : son extrémité doit devenir L2312-50 dans son propre lot, sans retirer les autres compétences centrales. La clause opératoire interdit déjà qu'un tel renvoi recrée les comptes rendus. L2315-92/93, également lus, conservent l'expertise OPA sous la plage jusqu'à L2312-52 ; ils ne recréent pas de suivi semestriel. Ne pas confondre R2312-51, article distinct relatif aux contributions sociales et culturelles, avec le présent article législatif. Les conditions de contrôle L233-1/3/16 du commerce et la note CMF ne donnent lieu à aucune nouvelle obligation de substitution. Les engagements financiers ou sociaux autonomes restent justiciables ; les textes européens et financiers extérieurs doivent être confrontés sans conformité présumée.",
    "Par rapport à la source entière, la triple obligation légale de rendre compte après acquisition du contrôle est retirée pour toutes les échéances futures, y compris des offres anciennes. L'abrogation ne supprime pas les engagements de fond et n'étend aucune taxe. Le gain démontré est un circuit de reporting supprimé, comportant trois échéances, non trois impôts ni trois mesures distinctes.",
    "Les obligations déjà échues, les conventions autonomes et les autres informations-consultations restent dues. L2316-2 hors lot appelle une coordination de borne ; les textes extérieurs de marché ne sont pas réécrits. Le coût net et le nombre d'entreprises concernées ne sont pas chiffrés.",
    "Aucune charge nouvelle n'est identifiée : aucun compte rendu à la demande substitué, registre, relevé annuel, attestation ou nouvelle échéance. Les autres fondements maintenus ne sont ni élargis ni utilisés pour rétablir automatiquement les trois comptes rendus.",
    [effect(
        'obligation_removed', 'cse-opa-suivi-periodique-suppression',
        "Suppression du reporting légal post-OPA à trois échéances fixes après acquisition du contrôle.",
        "L'auteur de l'offre ayant acquis le contrôle rend compte au CSE au sixième, douzième et vingt-quatrième mois après clôture de l'exécution de ses intentions et engagements sociaux et territoriaux.",
        "Aucun de ces comptes rendus légaux n'est dû aux échéances atteintes à compter de l'entrée en vigueur, même si l'offre était déjà clôturée ; engagements et fondements autonomes conservés.",
        'legal_duty', "Auteurs d'OPA ayant acquis le contrôle d'une cible soumise à l'article, sous les exemptions de L2312-52.",
        "Fin des échéances postérieures ou égales à l'entrée en vigueur ; obligations échues avant cette date et recours préservés, ainsi que les conventions autonomes.",
        "Aucun reporting de remplacement ; maintien des seuls droits d'information et d'alerte ayant un fondement légal distinct, sans extension de leur champ.",
        "Si, à l'issue de l'offre publique, l'auteur de l'offre a acquis le contrôle de l'entreprise faisant l'objet de l'offre au sens des articles L. 233-1, L. 233-3 et L. 233-16 du code de commerce, il rend compte au comité social et économique de cette société, au cours du sixième, du douzième et du vingt-quatrième mois suivant la clôture de l'offre, de la manière dont il a mis en œuvre les déclarations d'intention et, le cas échéant, les engagements qu'il a pris auprès du comité social et économique, dans le cadre des auditions prévues aux articles L. 2312-43 et L. 2312-46 du présent code, en matière d'emploi, de maintien des sites d'activité et de localisation des centres de décision exprimés dans la note d'information mentionnée au III de l'article L. 621-8 du code monétaire et financier.",
        "Les comptes rendus périodiques au comité social et économique, prévus au cours des sixième, douzième et vingt-quatrième mois suivant la clôture d'une offre publique ayant donné à son auteur le contrôle de la société, ne sont plus exigés lorsque leur échéance est postérieure ou égale à cette date, y compris pour les offres clôturées auparavant.",
    )],
)
a51.update(
    change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19',
    repeal_scope="Suppression pour les échéances futures des comptes rendus obligatoires de suivi post-OPA au sixième, douzième et vingt-quatrième mois, y compris pour les offres déjà clôturées, avec conservation des obligations échues et des engagements autonomes.",
)

xml52 = by_number['L2312-52']['source_xml'].replace('L. 2312-45 à L. 2312-51', 'L. 2312-45 à L. 2312-50')
a52 = rewrite(
    'L2312-52', xml52,
    "Coordination nécessaire de la borne de la plage exclue, à la suite de l'abrogation prospective de L2312-51. Les exclusions applicables aux offres de rachat visées au commerce et aux offres d'entités déjà majoritaires sont conservées en entier, pour l'avenir comme pour les situations anciennes. Le seuil demeure strictement plus de la moitié du capital ou des droits de vote et l'action de concert garde sa référence. Aucun avantage nouveau ni nouvelle réduction autonome n'est revendiqué.",
    "La plage est ramenée de L2312-45 à L2312-50 ; le régime transitoire de L2312-51 n'impose pas d'ancienne obligation aux offres qui en étaient déjà exemptées. Le texte de L2312-51 maintient uniquement les obligations anciennement exigibles selon leur champ légal, donc sous les anciennes exemptions. Les renvois L225-207, L22-10-62 et L233-10 du commerce ne sont ni remplacés ni élargis ; les articles commerciaux ne sont pas disponibles intégralement ici. La note d'entrée en vigueur au 1er janvier 2021 est historique et ne devient pas la date de la réforme.",
    "La seule modification est une borne de renvoi devenue sans objet pour l'avenir. Les mêmes offres restent exclues des règles L2312-45 à L2312-50 ; aucune deuxième suppression de reporting n'est comptée.",
    "La coordination n'étend pas l'exemption aux articles L2312-42 à L2312-44. Les offres déjà exclues ne deviennent pas soumises à des obligations anciennes du fait de la transition de L2312-51.",
    "Aucune charge nouvelle n'est identifiée : seules les bornes du renvoi changent, sans déclaration, attestation de majorité ni nouvelle condition pour bénéficier de l'exclusion.",
    [effect(
        'coordination', 'cse-opa-suivi-periodique-suppression',
        "Mise en concordance de la plage d'exclusion avec l'abrogation du reporting post-OPA, sans nouveau gain distinct.",
        "Exclusion des articles L2312-45 à L2312-51 pour les offres de rachat visées et celles d'entités détenant déjà plus de la moitié du capital ou des droits de vote, seules ou de concert.",
        "Même exclusion pour L2312-45 à L2312-50 ; L2312-51 supprime lui-même les échéances futures et conserve le seul champ ancien sous ses anciennes exemptions.",
        'other', "Offres mentionnées aux articles commerciaux cités et offres des entités déjà majoritaires dans les conditions conservées.",
        "Coordination dès l'entrée en vigueur de l'abrogation ; maintien des exemptions dans le traitement des échéances anciennes.",
        "Aucune obligation de substitution et aucun élargissement des opérations soumises au reporting ancien.",
        "Les articles L. 2312-45 à L. 2312-51 du présent code ne s'appliquent pas aux offres mentionnées aux articles L. 225-207 et L. 22-10-62 du code de commerce ou lorsque la société fait l'objet d'une offre publique engagée par des entités, agissant seules ou de concert au sens de l'article L. 233-10 du même code, détenant plus de la moitié du capital ou des droits de vote de la société faisant l'objet de l'offre.",
        "Les articles L. 2312-45 à L. 2312-50 du présent code ne s'appliquent pas aux offres mentionnées aux articles L. 225-207 et L. 22-10-62 du code de commerce ou lorsque la société fait l'objet d'une offre publique engagée par des entités, agissant seules ou de concert au sens de l'article L. 233-10 du même code, détenant plus de la moitié du capital ou des droits de vote de la société faisant l'objet de l'offre.",
    )], classification='coordination_only',
)
a52['benefit_review'] = "Les exclusions sont intégralement conservées : offres de rachat visées aux deux articles du commerce et offres d'entités déjà détentrices, seules ou de concert, de plus de la moitié du capital ou des droits de vote. La nouvelle borne retire seulement l'article abrogé ; elle n'impose aucune formalité aux offres futures exclues et ne réactive pas les comptes rendus anciens pour une opération qui en était exemptée."

entry(
    'L2312-53',
    "Maintien intégral des consultations du CSE avant ou pendant les procédures collectives judiciaires. Les quatre subdivisions identifient des situations différentes de sauvegarde, redressement et liquidation, et le dernier alinéa articule les licenciements économiques avec L1233-58. Ce n'est pas un agrément administratif à retirer : il s'agit de représentation et de défense collectives dans une procédure pouvant emporter cessation d'activité et perte des emplois.",
    "Les 1° à 4° et tous leurs alinéas de renvoi sont conservés sans contraction. L1233-58 a été lu intégralement ; ses anciens renvois à L2323-31, L2325-35, L4614-12-1 et L2324-8 demandent une coordination expresse dans cette cible hors lot et ne sont pas corrigés silencieusement par une paraphrase ici. Les dispositions du commerce visées ne sont pas intégralement présentes dans le corpus autorisé : la concordance détaillée des renvois au troisième, premier, avant-dernier et deuxième alinéas y demeure à contrôler. Ce constat documentaire ne diffère pas le traitement du présent article, maintenu en entier. Le préavis de quinze jours ne remplace aucune de ces procédures.",
    "Les consultations aux différents stades de l'insolvabilité sont conservées dans leur totalité. Aucune suppression d'autorisation, de coût de licenciement ou de délai judiciaire n'est avancée.",
    "Les cibles commerciales et les anciennes références de L1233-58 ne sont pas déclarées réécrites. Les garanties européennes d'insolvabilité et de licenciements collectifs ne sont pas réputées effacées par le contrat unique.",
    "Aucune charge nouvelle n'est identifiée : ni consultation, information, contrôle ou délai ajouté, puisque le texte source reste entier avec ses quatre subdivisions.",
)

entry(
    'L2312-54',
    "Maintien intégral du droit d'audition par la juridiction des personnes désignées par le CSE. Les trois séries de procédures et leurs situations précises donnent une voix aux salariés dans la sauvegarde, le redressement et la cession d'actifs. Il ne s'agit ni d'une seconde autorisation de l'employeur ni d'un justificatif répétitif ; supprimer ces auditions retirerait une garantie de participation au procès.",
    "L661-10 et les articles commerciaux énumérés restent dans leur champ propre. Le renvoi au premier alinéa de L642-5 est conservé tel que la source le prévoit, distinct des renvois plus larges de L2312-53. Le commerce ne figure pas en texte intégral dans le corpus des cinq codes : contrôler les concordances et alinéas lors de sa coordination, sans affirmer une vérification intégrale extérieure ni modifier ces articles hors dossier. Les dates de la note de 2017 ne valent pas calendrier de la réforme.",
    "L'ensemble de la source est conservé : même désignation et mêmes auditions dans les trois catégories de procédure. Aucun allègement documentaire ou financier ne peut être attribué à ce maintien.",
    "Les procédures judiciaires du commerce et leurs concordances détaillées restent extérieures au lot. Le maintien du droit d'être entendu ne préjuge ni d'un délai de rupture ni de la décision de la juridiction.",
    "Aucune charge nouvelle n'est identifiée : aucune audience, désignation, donnée ni preuve supplémentaire n'est créée ; seuls les droits sources sont maintenus.",
)

entry(
    'L2312-55',
    "Maintien intégral d'une faculté conventionnelle de simplification : adapter contenu, modalités et nombre de réunions, ainsi que les délais des consultations ponctuelles. Les majorités et les garanties d'ordre public évitent qu'un allègement imposé unilatéralement prive le CSE de son consentement effectif. Aucun rapport ou transmission supplémentaire n'est imposé par cet article ; retirer ses conditions de validité ne serait pas supprimer un doublon.",
    "Premier alinéa de L2232-12 lu : signature de syndicats ayant recueilli plus de 50 % des suffrages en faveur d'organisations représentatives, pas 50 % du personnel. En l'absence de délégué syndical, la majorité demeure celle des membres titulaires du CSE, sans transposer les majorités d'autres voies de négociation. L2312-8, L2312-37 et L2312-15 ont été lus. Les réformes L2312-38/46 et l'abrogation L2312-51 ne sont pas rétablies par le simple renvoi à l'ordre public : un engagement conventionnel autonome reste distinct. Les deux notes historiques ont été lues, y compris l'application aux instances existantes.",
    "La latitude de négocier des modalités plus simples demeure intégralement ouverte pour les accords futurs. Les majorités et les garanties sources sont maintenues ; cette faculté préexistante n'est pas une nouvelle fusion de régimes.",
    "L'article ne permet pas de supprimer conventionnellement les protections d'ordre public ni de tenir le silence pour un consentement. Aucun accord futur ou coût de conformité résultant de son usage n'est présumé.",
    "Aucune charge nouvelle n'est identifiée : pas de dépôt, transmission, délai minimal ou protocole ajouté ; les conditions existantes de conclusion et le champ des accords sont inchangés.",
)

entry(
    'L2312-56',
    "Maintien intégral de l'option de consultation au comité de groupe. La transmission de son avis à chaque CSE et à l'organe de l'entreprise dominante ne constitue pas deux envois au même destinataire ; elle rend la coordination utile. La consultation locale porte expressément sur les conséquences propres à chaque entreprise et ne doit pas être confondue avec une répétition de l'avis sur le projet de groupe.",
    "L2312-8 et L2312-37 ont été lus. Les deux destinataires et les 1°/2° sont maintenus, de même que la référence à l'entreprise dominante L2331-1. La faculté d'accord de groupe reste ouverte aux futures opérations. Le texte n'impose pas un observatoire, une convention supplémentaire ou un minimum de réunions. Les réformes ponctuelles de ce lot ne sont pas annulées par le choix du niveau de consultation.",
    "La source conserve une option de mutualisation déjà en vigueur et une consultation locale de portée distincte. Aucun nouveau régime fusionné ou nombre de réunions supprimé n'est démontré.",
    "La répartition concrète des consultations dépend de l'accord de groupe et des conséquences propres aux entreprises. Aucun solde net de coût ou allègement automatique pour l'ensemble des groupes n'est chiffré.",
    "Aucune charge nouvelle n'est identifiée : mêmes deux destinataires, même option conventionnelle et même consultation locale, sans registre ni nouveau circuit d'approbation.",
)

xml57 = by_number['L2312-57']['source_xml'].replace(
    "l'employeur lui communique une documentation économique et financière précisant :",
    "l'employeur lui communique les éléments manquants ou modifiés d'une documentation économique et financière précisant :",
).strip() + """
<p>Les informations exactes et à jour déjà effectivement accessibles aux nouveaux membres du comité, notamment dans la base de données économiques, sociales et environnementales, n'ont pas à être communiquées de nouveau. La dispense ne s'applique qu'aux informations mentionnées aux 1° à 4° effectivement accessibles et utilisables par ces membres au moment où la communication est exigible ; à défaut, elles leur sont communiquées. Aucun dossier récapitulatif distinct, inventaire des pièces déjà accessibles ou attestation de leur disponibilité n'est exigé au titre du présent article.</p>
<p>Cette dispense de communication répétée s'applique aux communications exigibles à compter de l'entrée en vigueur de la loi qui l'institue, y compris après une élection antérieure. Elle ne remet pas en cause les droits et recours résultant d'une obligation déjà échue avant cette date.</p>
"""
rewrite(
    'L2312-57', xml57,
    "Réforme de fond limitée au renouvellement automatique de l'information après chaque élection : seuls les éléments manquants ou modifiés sont communiqués lorsque les nouveaux élus disposent effectivement d'informations exactes, actuelles et utilisables. La documentation ne doit plus être reconstituée ni retransmise pour ses éléments déjà accessibles. Le mois après l'élection, le caractère supplétif, les quatre rubriques, le seuil strictement supérieur à 10 % et la limite des informations disponibles chez l'employeur sont conservés. Aucun simple changement de vocabulaire ne constitue le gain revendiqué.",
    "L2312-18 et L2312-36 ont été lus : la BDESE rend déjà accessibles de nombreuses informations récurrentes, mais le présent article concerne la communication postélectorale distincte. Le gain est limité à la dispense expresse de nouvelle communication ; il n'est pas attribué au CRPA. Les données absentes ou non accessibles aux nouveaux élus restent à fournir et aucune nouvelle information n'est collectée. Le 4° conserve la répartition du capital selon les seules informations dont dispose l'employeur et les actionnaires de plus de 10 %. R342-30 CCH, lu intégralement, reprend aussi cette attribution pour le comité social d'administration de l'ANCOLS, tout en excluant L2312-18 à L2312-21 et L2312-36 : la dispense reste fondée sur l'accès effectif, sans lui imposer une BDESE sur ce seul fondement. Cette incidence appelle une coordination de son lot, sans extension du contrat unique aux agents publics. Ne pas exiger de liste de réemploi ou d'attestation au titre de ce texte.",
    "La source entière imposait une communication après chaque élection de la documentation à quatre rubriques. La proposition retire cette communication répétée pour les seules données effectivement accessibles aux nouveaux élus ; elle garde le contenu utile et n'exige que les éléments manquants ou modifiés. Le gain peut être nul si tout doit être nouvellement fourni.",
    "La dispense ne couvre ni les informations manquantes, ni les données périmées, ni un accès théorique ou réservé aux anciens élus. Les obligations récurrentes autonomes de BDESE ne sont pas supprimées. La reprise de cette attribution par R342-30 CCH pour l'ANCOLS est signalée sans lui étendre les règles BDESE exclues ; aucune économie nationale n'est chiffrée.",
    "Aucune charge nouvelle n'est identifiée : accès et contenu étaient déjà dus au CSE et aucun nouveau droit d'accès aux données d'un tiers n'est créé. Pas de registre de réemploi, attestation, inventaire ou dossier distinct ; seuls les éléments déjà dus et non disponibles restent communiqués.",
    [effect(
        'obligation_removed', 'cse-information-postelection-reemploi',
        "Dispense de recommuniquer après chaque élection les éléments de documentation déjà effectivement accessibles aux nouveaux élus.",
        "À défaut d'accord, communication un mois après chaque élection d'une documentation économique et financière à quatre rubriques, y compris ses éléments inchangés déjà accessibles.",
        "Au même moment et à défaut d'accord, communication des seuls éléments manquants ou modifiés ; pas de nouvelle communication des informations exactes et à jour effectivement utilisables par les nouveaux membres.",
        'legal_duty', "Employeurs et nouveaux élus des CSE relevant de cette section, à défaut d'accord applicable.",
        "Communications exigibles dès l'entrée en vigueur, même après une élection antérieure ; manquements déjà échus et recours conservés.",
        "Aucun dossier, inventaire ou attestation de réemploi ; aucun gain pour les informations devant déjà être entièrement fournies faute d'accès effectif.",
        "A défaut d'accord, un mois après chaque élection du comité social et économique, l'employeur lui communique une documentation économique et financière précisant :",
        "Les informations exactes et à jour déjà effectivement accessibles aux nouveaux membres du comité, notamment dans la base de données économiques, sociales et environnementales, n'ont pas à être communiquées de nouveau.",
    )],
    ["Nouvelle communication systématique après chaque élection des éléments inchangés de documentation déjà effectivement accessibles et utilisables par les nouveaux élus du CSE."],
)

entry(
    'L2312-58',
    "Maintien intégral de l'alerte vers l'entreprise sous-traitante puis son CSE lorsque la restructuration du donneur d'ordre affecte son activité ou ses emplois. Les destinataires et leurs salariés sont distincts : ce circuit n'est pas une redemande de la même pièce. L'immédiateté et l'explication utile assurent une anticipation du risque social sans imposer un rapport périodique ni un agrément.",
    "Le caractère supplétif à défaut d'accord est conservé. L2312-39 et L2312-55/56 distinguent projet de restructuration, négociation des modalités et répartition au sein du groupe ; une entreprise sous-traitante peut être extérieure à ce groupe. Le préavis individuel ne remplace pas l'information de la sous-traitance. Aucune nouvelle liste des sous-traitants ni collecte récurrente de leurs données n'est créée. La note d'application de 2017 est historique.",
    "Les deux alinéas sources sont maintenus : information événementielle du sous-traitant puis de son CSE et explications utiles. Aucune suppression de transmission à un même destinataire n'est démontrée.",
    "Le champ reste limité aux projets susceptibles d'affecter activité ou emploi du sous-traitant et au cas sans accord. L'information ne garantit ni un volume de commandes ni l'absence de licenciement.",
    "Aucune charge nouvelle n'est identifiée : pas de rapport annuel, déclaration administrative ou fichier supplémentaire, et mêmes destinataires distincts qu'en source.",
)

entry(
    'L2312-59',
    "Maintien intégral nécessaire de l'alerte sur les atteintes aux droits, à la santé et aux libertés, de l'enquête sans délai, de la remédiation et du recours prud'homal accéléré. La liste complète des domaines de discrimination, l'information écrite du salarié et son droit d'opposition à la saisine par un élu sont conservés. La demande de réduction des contraintes ne justifie pas de retirer les protections contre harcèlement et discrimination ni les pouvoirs du juge.",
    "Les quatre alinéas et l'astreinte liquidée au profit du Trésor restent entiers. La mention du renouvellement de contrat ne crée aucune permission de conclure ou renouveler un CDD nouveau : elle protège les faits et contrats anciens ainsi que toute décision discriminatoire ; la liste est expressément non exhaustive. Il n'est pas nécessaire de la supprimer ou de limiter les futurs droits d'alerte pour coordonner le contrat unique. L'indemnité ordinaire n'affecte ni les réparations ni les mesures de cessation d'une illégalité. La note de procédure du 1er janvier 2020 est conservée dans son champ historique.",
    "La source entière est maintenue comme protection essentielle, non comme simple formalité administrative. L'enquête, l'accès au juge et le consentement protégé du salarié ne sont pas comptés comme simplifications ou charges nouvelles.",
    "La conservation de l'alerte ne rétablit aucun nouveau CDD ni indemnité ordinaire supprimée. Les conditions de fond des discriminations et réparations restent dans leurs dispositions propres.",
    "Aucune charge nouvelle n'est identifiée : aucun contrôle, registre, justificatif ou délai supplémentaire n'est ajouté aux protections intégralement conservées.",
)

entry(
    'L2312-60',
    "Maintien intégral des droits d'alerte en cas de danger grave et imminent ainsi qu'en santé publique et environnement. Les deux séries de renvois distinguent deux mécanismes essentiels et ne sont pas des autorisations préalables d'embauche. Retirer ce renvoi affaiblirait la sécurité et la possibilité de signaler un risque ; aucun doublon documentaire propre à cet article n'est identifié.",
    "Les plages L4132-1 à L4132-5 et L4133-1 à L4133-4 sont conservées sans confondre droit d'alerte, droit de retrait et préavis de rupture. Les cibles sont lues dans la vérification finale de ce lot ; le registre de danger demeure une garantie de suivi du risque, non un registre nouveau créé par la proposition. Le droit de l'Union en santé au travail n'est pas déclaré abrogé. La note historique de 2017 ne fixe pas l'entrée en vigueur du projet.",
    "La norme entière est maintenue pour sa fonction de prévention et d'alerte sur les risques graves et collectifs. Aucun prélèvement, délai minimal ou document redondant n'est supprimé par ce maintien.",
    "Les effets préventifs ne sont pas chiffrés. L'article ne couvre pas indistinctement toutes les obligations environnementales ni le régime de rupture individuelle du contrat.",
    "Aucune charge nouvelle n'est identifiée : les droits et procédures d'alerte demeurent dans leur état source, sans nouvelle déclaration, donnée ou autorisation.",
)

xml63 = by_number['L2312-63']['source_xml'].replace(
    "Ce rapport, au titre du droit d'alerte économique, est transmis à l'employeur et au commissaire aux comptes.",
    "Ce rapport, au titre du droit d'alerte économique, est transmis à l'employeur. Le comité social et économique ou, le cas échéant, la commission économique peut également le transmettre au commissaire aux comptes ; cette transmission n'est pas obligatoire au titre du présent article.",
).strip() + """
<p>La suppression de la transmission obligatoire au commissaire aux comptes s'applique aux rapports établis à compter de l'entrée en vigueur de la loi qui l'institue. Les obligations antérieurement exigibles ainsi que les droits et recours qui s'y rapportent demeurent régis par les dispositions antérieures. Le droit de convoquer le commissaire aux comptes prévu à l'article L. 2312-64, les attributions et obligations légales propres de celui-ci ainsi que les règles de confidentialité restent applicables. Aucun autre envoi, dépôt ou document de remplacement n'est exigé au titre de cette suppression.</p>
"""
rewrite(
    'L2312-63', xml63,
    "Réforme de fond : suppression de la transmission automatique au commissaire aux comptes de chaque rapport d'alerte économique, désormais laissée au choix du comité ou de la commission économique. Le rapport, sa transmission à l'employeur, la demande d'explications, son inscription de droit à l'ordre du jour et la compétence de la commission dans les entreprises d'au moins mille salariés sont conservés. La faculté de convoquer le commissaire et ses obligations autonomes préviennent la perte des garanties utiles ; le routage systématique n'a pas de fonction essentielle distincte démontrée.",
    "L2312-64 à L2312-67 et L2315-45/46/92 ont été lus : expertise, cinq heures rémunérées pour chacun des deux salariés adjoints, convocation du commissaire, avis sur saisine des organes dirigeants, majorités et confidentialité restent opérants. Les renvois au rapport ne sont pas orphelins puisque celui-ci demeure intégralement requis. Le seuil de mille salariés et la réserve de l'accord prévu à L2315-45 sont conservés sans renumérotation ni déplacement de leur alinéa. Les obligations propres d'alerte ou de signalement du commissaire prévues au commerce restent à leur champ ; aucun automatisme général ne les remplace ici. Les textes commerciaux extérieurs ne sont pas déclarés réécrits.",
    "La source entière imposait deux destinataires du rapport. La proposition retire seulement l'envoi obligatoire au commissaire aux comptes, tout en permettant cet envoi et sa convocation. La démarche d'alerte économique et le rapport demeurent ; il s'agit d'une transmission obligatoire en moins, non d'un rapport supprimé.",
    "L'allègement porte sur les rapports établis dès l'entrée en vigueur et seulement sur la transmission due au titre de L2312-63. Les obligations autonomes du commissaire, les envois déjà exigibles et la confidentialité ne sont pas supprimés. Le gain de coût net reste inconnu.",
    "Aucune charge nouvelle n'est identifiée : pas de rapport abrégé, attestation, registre ou destinataire de remplacement. La transmission facultative au même destinataire n'est pas une obligation nouvelle ; rapport et envoi à l'employeur étaient déjà dus.",
    [effect(
        'obligation_removed', 'cse-alerte-economique-envoi-cac',
        "Retrait de l'envoi systématique au commissaire aux comptes du rapport d'alerte économique, en maintenant l'option d'envoi.",
        "Chaque rapport d'alerte économique du comité ou de sa commission doit être transmis à l'employeur et au commissaire aux comptes.",
        "Le rapport reste transmis à l'employeur ; le comité ou la commission choisit sa transmission au commissaire, dont les attributions autonomes et la convocation restent possibles.",
        'legal_duty', "CSE ou commissions économiques établissant un rapport d'alerte au sein des entreprises relevant de cette section.",
        "Rapports établis dès l'entrée en vigueur ; obligations antérieurement exigibles et recours conservés ; respect des devoirs autonomes du commissaire.",
        "Aucun envoi ou rapport de remplacement ; confidentialité, rapport et transmission à l'employeur maintenus sans extension.",
        "Ce rapport, au titre du droit d'alerte économique, est transmis à l'employeur et au commissaire aux comptes.",
        "Ce rapport, au titre du droit d'alerte économique, est transmis à l'employeur. Le comité social et économique ou, le cas échéant, la commission économique peut également le transmettre au commissaire aux comptes ; cette transmission n'est pas obligatoire au titre du présent article.",
    )],
    ["Transmission systématique obligatoire au commissaire aux comptes du rapport d'alerte économique, remplacée par une faculté du comité ou de sa commission sans envoi obligatoire de substitution."],
)

assert len(answers) == len(sources) == 24
output = [answers[a['number']] for a in sources]
Path('answer.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
