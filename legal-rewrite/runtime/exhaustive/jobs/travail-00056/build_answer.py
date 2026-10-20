import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
by_number = {a['number']: a for a in sources}
answers = {}


def retain(number, reason, review, assessment, limitations, burdens, benefit=None):
    a = by_number[number]
    out = {k: a[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    out.update(
        proposed_xml=None,
        reason=reason,
        review_notes=review,
        status='retained_unchanged',
        classification='retained_necessary',
        substantive_impact={
            'version': 1,
            'classification': 'retained_necessary',
            'assessment': assessment,
            'scope_limitations': limitations,
            'new_burdens_review': burdens,
            'effects': [],
        },
    )
    if benefit:
        out['benefit_review'] = benefit
    answers[number] = out


def rewrite(number, proposed, reason, review, assessment, limitations, burdens,
            effects, removed=None, benefit=None):
    a = by_number[number]
    out = {k: a[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    category = 'material_reduction' if removed else 'coordination_only'
    out.update(
        proposed_xml=proposed,
        reason=reason,
        review_notes=review,
        status='rewrite_draft',
        substantive_impact={
            'version': 1,
            'classification': category,
            'assessment': assessment,
            'scope_limitations': limitations,
            'new_burdens_review': burdens,
            'effects': effects,
        },
    )
    if removed:
        out.update(
            change_type='normative_reduction',
            reform_policy_id='editorial_direction_2026_10_19',
            removed_provisions=removed,
        )
    if benefit:
        out['benefit_review'] = benefit
    answers[number] = out


def effect(kind, measure, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    return {
        'kind': kind,
        'measure_id': measure,
        'description': description,
        'before': before,
        'after': after,
        'unit': unit,
        'affected_population': population,
        'conditions_and_transition': transition,
        'replacement_or_new_burdens': burdens,
        'source_quote': source_quote,
        'proposed_quote': proposed_quote,
    }


retain(
    'L2315-9',
    "Maintien intégral du droit de répartir chaque mois les crédits d'heures entre titulaires et avec les suppléants. Cette faculté évite que des heures disponibles restent inutilisables par le représentant qui en a besoin. L'article ne crée ni prélèvement, ni agrément, ni dépôt distinct : son habilitation réglementaire organise l'exercice d'un avantage, sans justifier sa suppression. Aucune réécriture stylistique ni réduction de fond n'est revendiquée.",
    "Lecture de R2315-6 : plafond individuel d'une fois et demie le crédit d'un titulaire, information écrite nominative et quantitative huit jours avant utilisation. Ces conditions réglementaires ne sont pas supprimées par le maintien de L2315-9 ; elles ne sont pas comptées comme allégées dans ce lot. L2315-8 et R2315-5 concernent distinctement le cumul sur douze mois. La note source d'entrée en vigueur en 2018 est historique, non une date de réforme future.",
    "La source entière est conservée : même faculté mensuelle de mutualisation au profit des titulaires et suppléants, sans nouvelle réduction démontrée.",
    "La présente décision conserve l'habilitation législative ; elle ne réécrit ni les huit jours ni le plafond réglementaire de R2315-6 et ne mesure pas leur coût.",
    "Aucune charge nouvelle n'est identifiée : aucun texte nouveau, justificatif, registre ou délai n'est ajouté aux règles de répartition existantes.",
)

retain(
    'L2315-10',
    "Maintien intégral du paiement de plein droit des heures de délégation à l'échéance normale et de la saisine du juge par l'employeur qui en conteste l'usage. Le paiement constitue une garantie de rémunération et d'indépendance du mandat ; le contentieux évite qu'une contestation unilatérale prive d'abord le représentant de son salaire. Ni doublon déclaratif ni autorisation préalable ne figure dans cet article.",
    "Ne pas substituer une validation patronale au paiement de plein droit. Articuler avec les crédits de L2315-7 à L2315-9 et les temps non imputables de L2315-11 et L2315-12, sans doubler leur rémunération. Le préavis individuel du contrat unique ne modifie pas ces droits collectifs.",
    "Le maintien porte sur les deux règles de la source officielle : rémunération normale des heures et recours judiciaire de l'employeur contestant leur utilisation.",
    "Aucune baisse du salaire ni du crédit d'heures n'est proposée ; les litiges concrets sur l'utilisation des heures demeurent du ressort du juge.",
    "Aucune charge nouvelle n'est identifiée : la conservation de la garantie salariale et de la voie judiciaire n'ajoute aucune preuve ni procédure préalable.",
)

retain(
    'L2315-11',
    "Maintien intégral des 1°, 2° et 3° et de la non-imputation sur le crédit de délégation. La recherche de mesures préventives en urgence grave, les réunions et les enquêtes après accident ou risque grave exigent une participation effective et rémunérée. Supprimer ce paiement ou l'imputer au crédit ordinaire retirerait une protection, sans supprimer un rapport ou une formalité redondante. La limite conventionnelle ou réglementaire du 2° reste à son champ.",
    "L4132-2 a été lu : avis écrit de danger et enquête immédiate conjointe demeurent distincts. R2315-7 a été lu : limites annuelles de 30 et 60 heures et dérogation CSSCT. Ses deux tranches mentionnent le seuil de 1 000 salariés de façon chevauchante ; cette difficulté réglementaire préexistante n'est pas corrigée silencieusement ici. Les 1° et 3° ne sont pas soumis par ce maintien au plafond du 2°.",
    "Aucun changement par rapport à la source entière : les trois catégories de temps restent rémunérées et ne consomment pas le crédit de délégation dans leurs conditions propres.",
    "La portée précise du plafond réglementaire et le chevauchement au seuil de 1 000 salariés ne sont pas résolus par ce maintien législatif.",
    "Aucune charge nouvelle n'est identifiée : les obligations de paiement sont conservées sans nouveau plafond, justificatif, registre ou circuit d'autorisation.",
)

retain(
    'L2315-12',
    "Maintien intégral de la rémunération des réunions avec l'employeur pour les représentants syndicaux au CSE et de leur non-imputation sur les heures de délégation dans les entreprises d'au moins cinq cent un salariés. Il s'agit d'un droit salarial et d'un moyen d'exercice de la liberté syndicale, non d'une formalité administrative supprimable. La distinction de seuil est conservée, sans extension implicite ni retrait d'avantage.",
    "Seuil exact : au moins 501 salariés, non 500. Coordination lue avec L2315-7, qui ouvre le crédit de délégation correspondant. Le maintien ne crée pas un crédit autonome pour les entreprises situées sous ce seuil et ne confond pas représentants syndicaux et membres élus.",
    "La source entière reste applicable : paiement des réunions et non-déduction du crédit dans le seul champ d'effectif qu'elle désigne.",
    "Aucune réduction du nombre de réunions ou de leur rémunération n'est démontrée ; les autres temps syndicaux gardent leur régime distinct.",
    "Aucune charge nouvelle n'est identifiée : aucun état d'heures supplémentaire ni nouvelle condition de paiement n'accompagne le maintien.",
)

retain(
    'L2315-14',
    "Maintien intégral des déplacements hors de l'entreprise pendant les heures de délégation et de la circulation interne pendant ces heures ou hors des horaires habituels. Ces libertés permettent de représenter effectivement les salariés ; la réserve de gêne importante pour leur travail assure une limite proportionnée. Le texte ne soumet ces déplacements ni à un agrément ni à une déclaration qui pourrait être retirée.",
    "Conserver la différence entre déplacement extérieur pendant la délégation et circulation interne également hors des horaires habituels. L2315-1, lu, protège aussi les salariés dispersés ou travaillant hors de l'entreprise. Les règles de confidentialité de L2315-3 restent autonomes. Aucun renvoi n'est rendu incohérent par les modifications du lot.",
    "Les deux libertés de déplacement et de contact de la source officielle sont maintenues avec leur réserve exacte de gêne importante.",
    "Ce maintien ne dispense pas des règles autonomes de sécurité ; il ne crée pas de rémunération générale de tout déplacement hors des heures de délégation.",
    "Aucune charge nouvelle n'est identifiée : aucune autorisation patronale, déclaration de trajet ou pièce supplémentaire n'est instaurée.",
)

retain(
    'L2315-15',
    "Maintien intégral du droit d'affichage sur les emplacements syndicaux prévus et aux portes d'entrée. Ces supports assurent une information accessible aussi aux salariés dépourvus d'accès numérique ; les supprimer ou imposer leur remplacement électronique ferait perdre un moyen collectif utile. La source organise une faculté des élus et un accès matériel nécessaire, sans envoi périodique ni double déclaration.",
    "Les deux lieux d'affichage demeurent : emplacements destinés aux communications syndicales et portes d'entrée des lieux de travail. Aucune substitution obligatoire par une plateforme ou aucun accord préalable de l'employeur n'est ajouté. Ce droit ne se confond pas avec les règles d'ordre du jour des réunions.",
    "Le droit d'information par affichage reste intégralement celui de la source officielle ; aucune suppression de formalité nouvelle n'est revendiquée.",
    "Le maintien ne chiffre ni les coûts matériels existants ni l'accès numérique effectif des salariés ; aucune fermeture de l'accès physique n'est proposée.",
    "Aucune charge nouvelle n'est identifiée : aucun canal supplémentaire, compte numérique ou abonnement n'est imposé aux salariés ou à l'employeur.",
)

retain(
    'L2315-16',
    "Maintien intégral de la formation sur temps de travail rémunéré, sans déduction des heures de délégation. Cette règle empêche de faire financer l'acquisition des compétences du mandat par une perte de salaire ou de moyens de représentation. Elle ne comporte ni rapport autonome, ni agrément, ni justificatif redondant ; sa suppression serait une réduction de droit et non une simplification.",
    "Règle commune aux formations du chapitre, à articuler avec L2315-17 et L2315-18 sans double décompte. La rémunération du temps et le financement du coût pédagogique sont deux questions distinctes ; la faculté de prise en charge OPCO de L2315-22-1 est conservée.",
    "Le maintien reproduira intégralement la source : formation payée sur le temps de travail et crédit de délégation laissé disponible.",
    "Aucune diminution du salaire ni de la durée de formation n'est proposée ; le financement pédagogique conserve ses dispositions spécifiques.",
    "Aucune charge nouvelle n'est identifiée : pas de formulaire ou d'attestation nouvelle pour conserver la rémunération et la non-imputation existantes.",
)

retain(
    'L2315-17',
    "Maintien intégral de la version officielle applicable depuis le 28 mai 2026 : deux voies d'accès aux organismes de formation et renouvellement après quatre années de mandat, consécutives ou non. L'enregistrement de droit commun et l'accès aux organismes de L2145-5 permettent de former les représentants sans recréer un agrément spécial. La formation renouvelée garde une fonction essentielle de compétence du mandat ; aucun dépôt supplémentaire n'est institué par cet article.",
    "Lecture intégrale de L6351-1 à L6351-8 et de L2145-5. L'enregistrement se rattache à la déclaration d'activité de droit commun, non à un agrément nouveau du CSE. R2315-8, également lu, vise encore une liste préfectorale d'organismes : discordance réglementaire préexistante avec la version législative de mai 2026, à coordonner dans cet article réglementaire hors lot, sans rétablir une liste exclusive pour la première voie. Ne pas présenter cette coordination comme réalisée ici. Quatre ans, consécutifs ou non, sont conservés.",
    "Aucun changement au texte officiel récent : accès par organisme enregistré ou par organisme de L2145-5, puis renouvellement de formation après quatre années de mandat.",
    "La réglementation de L6351 et la discordance de R2315-8 ne sont pas réécrites dans ce lot ; aucun agrément ancien n'est réputé supprimé une seconde fois.",
    "Aucune charge nouvelle n'est identifiée : aucune seconde déclaration, liste obligatoire ou nouvelle preuve n'est ajoutée aux deux voies légales existantes.",
    "Les avantages possibles sont l'accès aux organismes simplement enregistrés selon L6351-1 à L6351-8, la voie alternative des organismes de L2145-5 et le renouvellement après quatre années de mandat même non consécutives. Tous sont maintenus intégralement pour les représentants et formations futurs comme pour les droits existants. Aucun agrément spécial, délai supplémentaire ou exclusivité de liste préfectorale n'est réintroduit ; le règlement ancien discordant est expressément signalé.",
)

retain(
    'L2315-18',
    "Maintien intégral du droit à la formation santé, sécurité et conditions de travail des élus et du référent, des minima de cinq jours au premier mandat, puis trois jours ou cinq jours selon les cas, et de son financement. Ces minima rendent effective la prévention des risques et du harcèlement ; leur retrait n'est pas justifié par un doublon administratif. La prise en charge possible par l'OPCO reste expressément réservée.",
    "L2314-1 a été lu : le référent visé au dernier alinéa lutte contre le harcèlement sexuel et les agissements sexistes. Au renouvellement : trois jours pour chaque membre quelle que soit la taille, cinq jours pour les membres de la CSSCT dans les entreprises d'au moins 300 salariés. Maintenir le renvoi à L2315-22-1. La note de la loi de 2021 porte sur une entrée en vigueur au 31 mars 2022, non sur la réforme proposée.",
    "Aucune réduction de la source entière : bénéficiaires, durées minimales, seuil de 300 salariés et financement employeur sous réserve de l'OPCO restent inchangés.",
    "Les modalités réglementaires du coût et de l'organisation ne sont pas réécrites ; aucune économie de formation ou de prévention n'est chiffrée.",
    "Aucune charge nouvelle n'est identifiée : aucun stage, durée minimale, dossier ou condition de remboursement supplémentaire n'est ajouté.",
)

retain(
    'L2315-19',
    "Maintien intégral de l'exercice individuel des droits reconnus au comité dans les entreprises de moins de cinquante salariés. Ce mécanisme dispense précisément les représentants d'une décision collective préalable pour exercer ces droits ; l'abroger recréerait une difficulté d'accès. L'article ne prescrit ni réunion supplémentaire, ni pièce, ni déclaration.",
    "Champ de la section : entreprises de moins de 50 salariés disposant d'un CSE, non toutes les entreprises sans condition d'effectif. L2311-2 et L2312-1 ont été lus. Les demandes individuelles de L2315-21 et les nouvelles modalités documentaires de L2315-22 restent compatibles avec cette règle.",
    "L'exercice individuel des droits de la section reste intégralement garanti par la source ; aucune nouvelle simplification n'est comptabilisée.",
    "Le maintien n'étend pas la personnalité civile du CSE d'au moins cinquante salariés aux comités relevant de cette section.",
    "Aucune charge nouvelle n'est identifiée : aucune majorité, procuration, autorisation ou formalité collective préalable n'est créée.",
)

retain(
    'L2315-20',
    "Maintien intégral du local nécessaire à la mission et aux réunions des représentants dans les entreprises de moins de cinquante salariés. Un espace de rencontre effectif protège l'exercice de la représentation ; la source n'exige ni local exclusivement affecté, ni surface chiffrée, ni agrément. Elle est déjà limitée à la nécessité et ne constitue pas un doublon avec le régime distinct des entreprises d'au moins cinquante salariés.",
    "Ne pas importer les exigences de local aménagé et de matériel de L2315-25 dans ce champ. Le maintien du local ne crée pas de plateforme de substitution et ne supprime pas le droit à des échanges confidentiels. Les règles de réception de L2315-21 demeurent.",
    "La seule mise à disposition du local nécessaire prévue par la source est conservée, sans extension du matériel ou des surfaces exigés.",
    "Aucune économie immobilière n'est démontrée ; le choix concret du local reste apprécié au regard des besoins de la mission.",
    "Aucune charge nouvelle n'est identifiée : pas d'exclusivité, équipement, surface minimale, registre d'occupation ou contrôle préalable ajouté.",
)

retain(
    'L2315-21',
    "Maintien intégral de la réception collective mensuelle, de la réception sur demande en urgence et des demandes individuelles ou par catégorie, atelier, service ou spécialité. Dans les entreprises de moins de cinquante salariés, ce dispositif constitue le canal direct d'examen des réclamations ; sa fonction ne se réduit pas à une réunion administrative. Le plafonnement des assistants de l'employeur garantit l'équilibre de la réception et reste inchangé.",
    "Ne pas confondre la réception au moins mensuelle de cette section avec les réunions supplétives de L2315-28 dans les entreprises d'au moins 50 salariés. Les collaborateurs et l'employeur ne peuvent ensemble dépasser le nombre des titulaires. L'allègement de L2315-22 n'affecte aucune de ces facultés de réception.",
    "Tous les modes de réception et l'équilibre numérique de la source restent inchangés ; aucun nombre de réunions supprimées n'est revendiqué.",
    "La nécessité d'une réception urgente demeure appréciée dans chaque situation ; aucune dispense générale de traiter les réclamations n'est créée.",
    "Aucune charge nouvelle n'est identifiée : aucune réunion, liste, motif écrit d'urgence ou pièce préalable supplémentaire n'est imposé.",
)


proposed_22 = """<p>Sauf circonstances exceptionnelles, les membres de la délégation du personnel du comité social et économique remettent à l'employeur une note écrite exposant l'objet des demandes présentées avant la réunion. Aucun délai minimal de remise de cette note n'est exigé.</p>
<p>L'employeur répond par écrit à ces demandes, au plus tard dans les six jours ouvrables suivant la réunion.</p>
<p>Les demandes des membres de la délégation du personnel du comité social et économique et les réponses motivées de l'employeur sont conservées sur tout support permettant leur consultation, sans obligation de registre spécial, de transcription ou d'annexion à un tel registre.</p>
<p>Ces demandes et réponses sont tenues à la disposition des salariés de l'entreprise désirant en prendre connaissance, pendant un jour ouvrable par quinzaine et en dehors de leur temps de travail.</p>
<p>Elles sont également tenues à la disposition de l'agent de contrôle de l'inspection du travail mentionné à l'article L. 8112-1 et des membres de la délégation du personnel du comité social et économique.</p>
<p>Ces dispositions s'appliquent aux demandes présentées à compter de l'entrée en vigueur de la loi. Les demandes présentées auparavant demeurent régies par les règles applicables lors de leur présentation et les délais de réponse déjà en cours ne sont pas recommencés. Les demandes et réponses antérieures ainsi que les registres existants restent accessibles dans les conditions prévues aux quatrième et cinquième alinéas, sans nouvelle transcription ni transfert de support obligatoire.</p>"""

rewrite(
    'L2315-22', proposed_22,
    "Réforme de fond : suppression du délai minimal de deux jours ouvrables pour remettre la note et suppression du registre spécial, de sa transcription ou de son alimentation par annexes. Le délai de réponse de six jours ouvrables après réunion donne à l'employeur un temps d'examen sans rendre une demande irrecevable pour sa seule remise tardive. Les demandes et réponses écrites, leur motivation, leur conservation consultable et les droits d'accès sont intégralement conservés dans leur champ. Le choix du support retire une formalité distincte ; aucune déclaration ou registre de remplacement n'est créé.",
    "Les cinq alinéas fonctionnels sont conservés dans leur ordre, suivis d'une transition. Maintien de l'exception de circonstances exceptionnelles, des six jours ouvrables, du jour ouvrable par quinzaine hors temps de travail et des deux catégories de destinataires institutionnels. L8112-1 a été lu. Les demandes antérieures gardent leur régime ; les archives existantes restent consultables sans ressaisie. Le registre du danger grave de L4132-2 et les registres du personnel sont autonomes et ne sont pas supprimés. Pas de conservation supplémentaire chiffrée inventée.",
    "Par rapport à la source entière, deux contraintes disparaissent : l'anticipation de deux jours ouvrables et la tenue du registre spécial par transcription ou annexes. Les écrits utiles et tous les accès demeurent ; il ne s'agit pas d'un simple changement de vocabulaire.",
    "La réduction vise les demandes nouvelles de cette section, dans les entreprises de moins de cinquante salariés. Le temps de préparation éventuellement déplacé vers l'après-réunion et le gain net de coût ne sont pas chiffrés ; les demandes anciennes conservent leur régime.",
    "Aucune charge nouvelle n'est identifiée : la conservation consultable remplace la tenue du registre sans données nouvelles, deuxième dépôt, transfert obligatoire d'archives ou délai de réponse raccourci. Le solde de coût de l'ensemble des codes n'est pas établi.",
    [
        effect(
            'deadline_reduced', 'cse-demandes-suppression-delai-minimal',
            "Suppression de l'anticipation minimale imposée aux représentants pour leurs demandes.",
            "Note écrite à remettre deux jours ouvrables avant la réception, sauf circonstances exceptionnelles, dans les entreprises relevant de la section des moins de cinquante salariés.",
            "Note remise avant la réunion sans nombre minimal de jours ouvrables d'anticipation ; exception de circonstances exceptionnelles et réponse sous six jours ouvrables conservées.",
            'working_days', "Membres de la délégation du personnel du CSE dans les entreprises de moins de cinquante salariés.",
            "Demandes présentées à compter de l'entrée en vigueur de la loi ; régime antérieur et délais en cours conservés pour les demandes antérieures.",
            "Aucune nouvelle déclaration ; la note écrite existante demeure, de même que le délai de réponse de l'employeur.",
            "deux jours ouvrables avant la date à laquelle ils doivent être reçus.",
            "Aucun délai minimal de remise de cette note n'est exigé.",
        ),
        effect(
            'obligation_removed', 'cse-registre-special-suppression',
            "Suppression du support spécial obligatoire et des opérations de transcription ou d'annexion qui lui sont liées.",
            "Demandes et réponses motivées obligatoirement transcrites sur un registre spécial ou annexées à celui-ci, avec accès des salariés, élus et inspection.",
            "Conservation consultable des mêmes demandes et réponses sur tout support, sans registre spécial, transcription ou annexion obligatoires ; mêmes droits d'accès.",
            'legal_duty', "Employeurs et représentants relevant de la section des entreprises de moins de cinquante salariés.",
            "Demandes nouvelles après l'entrée en vigueur ; archives et registres antérieurs accessibles sans ressaisie ou migration obligatoire.",
            "Pas de registre ni de dépôt de remplacement ; seule la conservation des écrits et leur consultation déjà nécessaires sont maintenues.",
            "Les demandes des membres de la délégation du personnel du comité social et économique et les réponses motivées de l'employeur sont, soit transcrites sur un registre spécial, soit annexées à ce registre.",
            "Les demandes des membres de la délégation du personnel du comité social et économique et les réponses motivées de l'employeur sont conservées sur tout support permettant leur consultation, sans obligation de registre spécial, de transcription ou d'annexion à un tel registre.",
        ),
    ],
    [
        "Délai minimal obligatoire de deux jours ouvrables avant la réception des représentants pour la remise de leur note écrite.",
        "Tenue d'un registre spécial des demandes et réponses, par transcription des écrits ou par annexion obligatoire de ceux-ci au registre.",
    ],
    "L'exception de circonstances exceptionnelles reste ouverte. Les représentants conservent la réponse écrite motivée sous six jours ouvrables ; salariés, représentants et inspection gardent leur accès, y compris aux archives. La suppression du registre n'éteint aucun de ces droits pour les demandes futures et ne force aucune ressaisie des pièces anciennes.",
)

retain(
    'L2315-22-1',
    "Maintien intégral de la possibilité de prise en charge OPCO des formations santé, sécurité et conditions de travail. Cette faculté allège le coût supporté par les petites entreprises sans diminuer la formation des représentants ; la supprimer contredirait la préservation des aides pour les situations futures. Le renvoi réglementaire ne crée pas à lui seul un second dossier obligatoire ou une contribution nouvelle.",
    "L6332-3 a été lu dans sa version applicable en 2026 : son 2° concerne toujours les entreprises de moins de cinquante salariés ; le renvoi reste cohérent. L2315-18 maintient la prise en charge employeur sans préjudice de cette possibilité. La note de 2022 est historique ; aucun plafond ni enveloppe budgétaire n'est inventé.",
    "L'aide facultative de la source est conservée intégralement pour les formations éligibles ; aucune suppression supplémentaire de cotisation n'est revendiquée.",
    "Une prise en charge possible ne garantit pas le financement intégral de chaque dossier ; ses modalités réglementaires et ressources ne sont pas chiffrées ici.",
    "Aucune charge nouvelle n'est identifiée : aucune demande, pièce, condition d'éligibilité ou contribution supplémentaire n'est ajoutée au dispositif existant.",
)

retain(
    'L2315-23',
    "Maintien intégral de la personnalité civile, de la gestion du patrimoine, de la présidence et des fonctions de secrétaire et de trésorier. Ces règles identifient la personne capable d'agir, d'administrer les fonds et d'établir les actes du comité ; leur suppression laisserait les comptes et le patrimoine sans gouvernance définie. L'assistance par trois collaborateurs au plus reste consultative, sans extension de leur vote.",
    "Champ de la section : entreprises d'au moins cinquante salariés. Le secrétaire établit l'ordre du jour avec le président selon L2315-29 et les procès-verbaux selon L2315-34, lus ; les fonctions financières sont distinctes de la voix consultative des collaborateurs. Le maintien ne modifie pas la majorité de L2315-32.",
    "Les trois composantes de la source officielle sont conservées : capacité patrimoniale, présidence assistée et désignation des deux fonctions parmi les titulaires.",
    "Aucune fusion de personne morale ou de fonctions n'est démontrée par ce maintien ; le coût de gouvernance existant n'est pas assimilé à un prélèvement supprimé.",
    "Aucune charge nouvelle n'est identifiée : aucun poste, rapport, compte ou nombre de collaborateurs supplémentaire n'est créé.",
)

retain(
    'L2315-24',
    "Maintien intégral du règlement intérieur de fonctionnement et de ses limites. Il fixe les relations du comité avec les salariés et fournit notamment le cadre des modalités d'arrêté des comptes ; le rendre globalement facultatif sans reprendre ces fondements créerait des lacunes. Le second alinéa protège déjà l'employeur contre des obligations extralégales imposées sans son accord et permet la dénonciation de son engagement avec information et délai raisonnable. Aucun nouveau document distinct n'est ajouté.",
    "L2315-68, lu, renvoie aux modalités d'arrêté des comptes prévues au règlement intérieur : ce fondement demeure. Conserver l'accord de l'employeur pour les seules obligations qui excèdent la loi, la qualification d'engagement unilatéral, le délai raisonnable et l'information des élus. Ne pas assimiler cet accord protecteur à un agrément administratif ni inventer un délai chiffré de dénonciation.",
    "La source entière reste inchangée, y compris la limitation des obligations supplémentaires et leur possibilité de dénonciation ; aucune simplification fictive n'est comptée.",
    "Le maintien ne constitue pas un examen de chaque clause des règlements locaux ; les obligations autonomes de comptabilité et les accords plus favorables ne sont pas supprimés.",
    "Aucune charge nouvelle n'est identifiée : le règlement existant n'est pas doublé par une charte, un registre ou une transmission administrative supplémentaire.",
)

retain(
    'L2315-25',
    "Maintien intégral du local aménagé et du matériel nécessaire au CSE. Ils permettent la gestion de son patrimoine, les échanges et l'exercice réel de ses attributions dans les entreprises d'au moins cinquante salariés. La source se limite à la nécessité et n'impose ni achat de logiciel déterminé, ni surface, ni autorisation administrative ; aucun doublon matériel précis ne justifie une suppression.",
    "Distinguer ce régime du local seulement nécessaire de L2315-20 pour les entreprises de moins de cinquante salariés. La suppression ciblée d'autorisation pour les invités de L2315-26 ne crée pas un droit à de nouveaux locaux, équipements ou prestations financées par l'employeur.",
    "Le maintien conserve uniquement les moyens matériels nécessaires prévus par la source, sans nouvelle obligation d'équipement.",
    "Les besoins concrets du comité et les coûts d'aménagement ne sont pas évalués quantitativement ; aucune économie immobilière n'est avancée.",
    "Aucune charge nouvelle n'est identifiée : aucun équipement, abonnement, superficie ou support numérique supplémentaire n'est imposé.",
)


old_26 = "Le comité peut inviter des personnalités extérieures, syndicales ou autres, dans les conditions prévues par les dispositions des articles L. 2142-10 et L. 2142-11."
new_26 = "Le comité peut inviter des personnalités extérieures, syndicales ou autres, à ces réunions dans le local mis à sa disposition, sans autorisation préalable de l'employeur. Les règles de sécurité et de sûreté applicables à l'accès à ce local demeurent applicables. Les dispositions de l'article L. 2142-11 demeurent applicables."
proposed_26 = by_number['L2315-26']['source_xml'].replace(old_26, new_26).strip()
proposed_26 += "\n<p>La dispense d'autorisation s'applique aux invitations adressées à compter de l'entrée en vigueur de la loi, y compris pour les comités déjà constitués. Les invitations régulièrement adressées avant cette date demeurent valables.</p>"

rewrite(
    'L2315-26', proposed_26,
    "Réforme de fond : retrait, pour les réunions d'information internes organisées par le CSE dans son local, de l'autorisation patronale issue du renvoi à L2142-10 pour les personnalités extérieures. La maîtrise du local attribué au comité et les règles ordinaires de sécurité suffisent dans ce périmètre ; le veto sur l'identité syndicale ou non syndicale de l'invité n'est pas conservé. Ni déclaration de remplacement ni extension à d'autres locaux n'est créée. Organisation des réunions, temps hors travail et usage des heures de délégation sont maintenus.",
    "L2142-10 et L2142-11 ont été lus en entier. Le premier prévoit notamment l'accord de l'employeur pour les invités non syndicaux et, dans certains cas, les autres locaux ; son renvoi général est remplacé par la règle spéciale du CSE dans son seul local. Les règles propres aux sections syndicales et aux autres locaux ne sont pas réécrites. L2142-11 et le troisième alinéa sur le temps des réunions sont conservés. Le maintien des règles de sécurité ne crée pas une autorisation personnelle de remplacement ; les recours contre une entrave restent distincts. Pas de financement automatique de frais d'invités ajouté.",
    "La proposition retire une autorisation effectivement applicable par renvoi, sans supprimer la réunion ni les droits de participation. Le gain concerne principalement les invités non syndicaux ; aucune dispense nouvelle n'est comptée pour une invitation déjà libre sous la source.",
    "Dispense limitée aux réunions internes du personnel organisées par le CSE dans le local mis à sa disposition. Les réunions de sections syndicales, d'autres locaux et les règles autonomes d'accès et de sécurité ne sont pas libéralisés indistinctement ; le coût net n'est pas chiffré.",
    "Aucune charge nouvelle n'est identifiée : pas d'avis, déclaration d'invité, liste ou autorisation de substitution. Les règles ordinaires de sécurité et le régime du temps de réunion préexistent et sont conservés.",
    [effect(
        'authorization_removed', 'cse-invites-local-fin-autorisation',
        "Dispense d'autorisation patronale pour inviter des personnalités extérieures dans le local du CSE aux réunions internes d'information.",
        "L2315-26 renvoie à L2142-10 : accord de l'employeur notamment pour les personnalités non syndicales ; invitations syndicales déjà libres dans les locaux syndicaux visés par ce dernier texte.",
        "Aucune autorisation préalable de l'employeur pour ces invitations du CSE dans son local ; maintien des règles ordinaires de sécurité et du temps de réunion.",
        'legal_duty', "CSE relevant de la section des entreprises d'au moins cinquante salariés, invités extérieurs et employeurs concernés.",
        "Invitations adressées après l'entrée en vigueur, y compris par les comités existants ; validité des invitations régulières antérieures préservée.",
        "Aucun avis ni déclaration de remplacement ; pas de droit nouveau d'utiliser d'autres locaux ou d'obtenir le paiement de prestations d'invités.",
        old_26,
        "Le comité peut inviter des personnalités extérieures, syndicales ou autres, à ces réunions dans le local mis à sa disposition, sans autorisation préalable de l'employeur.",
    )],
    ["Autorisation préalable de l'employeur imposée par le renvoi à L2142-10 pour les invités extérieurs concernés, dans le seul local du CSE et pour ses réunions internes d'information."],
    "La faculté d'organiser des réunions d'information et d'y inviter des personnes syndicales ou autres reste ouverte pour les réunions futures. L'accès déjà libre n'est pas restreint ; les représentants conservent l'usage de leur temps de délégation et les salariés ne perdent aucun droit salarial existant. Le texte ne crée ni frais à la charge des salariés ni condition nouvelle d'éligibilité.",
)


old_27 = "L'employeur informe annuellement l'agent de contrôle de l'inspection du travail mentionné à l'article L. 8112-1, le médecin du travail et l'agent des services de prévention des organismes de sécurité sociale du calendrier retenu pour les réunions consacrées aux sujets relevant de la santé, de la sécurité ou des conditions de travail, et leur confirme par écrit au moins quinze jours à l'avance la tenue de ces réunions."
new_27 = "L'employeur informe par écrit, au moins quinze jours à l'avance, l'agent de contrôle de l'inspection du travail mentionné à l'article L. 8112-1, le médecin du travail et l'agent des services de prévention des organismes de sécurité sociale de la tenue des réunions consacrées aux sujets relevant de la santé, de la sécurité ou des conditions de travail. Aucune information annuelle distincte portant sur le calendrier de ces réunions n'est exigée au titre du présent alinéa, y compris par un renvoi à celui-ci. Les règles propres aux invitations, aux ordres du jour et aux délais particuliers de réunion demeurent applicables."
proposed_27 = by_number['L2315-27']['source_xml'].replace(old_27, new_27).strip()
proposed_27 += "\n<p>La suppression de l'information annuelle distincte s'applique aux transmissions non encore effectuées à la date d'entrée en vigueur de la loi, y compris pour une année déjà commencée. Aucune transmission de rattrapage n'est exigée après cette date sur ce seul fondement. Les informations et convocations régulièrement adressées auparavant restent valables ; les droits et recours relatifs aux situations antérieures sont conservés.</p>"

rewrite(
    'L2315-27', proposed_27,
    "Réforme de fond limitée au doublon d'information : suppression de la transmission annuelle du calendrier, alors que l'avis écrit de chaque réunion quinze jours à l'avance subsiste à l'égard des trois destinataires. Cette annonce individuelle protège leur participation sans maintenir un envoi annuel distinct. Les quatre réunions annuelles au moins, les réunions liées aux risques et accidents graves et la convocation par l'inspection en cas de défaillance restent intégralement maintenues. Aucun rapport ni calendrier de remplacement n'est institué.",
    "Les trois premiers alinéas sont conservés à leur place : les renvois de L2314-3, R2312-4 et R4643-32 restent utilisables. Quatrième alinéa : mêmes trois destinataires et même anticipation écrite de quinze jours, distincte du préavis individuel de rupture. L'articulation de cette anticipation avec les réunions urgentes après accident est une difficulté préexistante, non une dispense ou un report créé par la suppression du calendrier. L2315-30 conserve l'ordre du jour au moins trois jours avant. R4523-15, lu, conserve son délai spécial de trente jours. R4643-32, lu, renvoie encore au calendrier du quatrième alinéa : la suppression vise expressément ce renvoi ; sa dernière phrase doit être coordonnée pour retirer ce seul calendrier, sans supprimer invitation, voix consultative ou ordre du jour du représentant de prévention. Cette rédaction réglementaire n'est pas présentée comme effectuée. Les obligations non exécutées de calendrier cessent sans rattrapage ; pas d'annulation générale de sanctions anciennes affirmée.",
    "La transmission annuelle du calendrier disparaît réellement ; l'information individuelle de réunion déjà due sous la source est conservée et n'est pas comptée comme une seconde obligation supprimée. Les obligations essentielles de réunion et de prévention restent inchangées.",
    "L'allègement ne supprime ni la réunion, ni les invitations, ni l'ordre du jour, ni les délais spéciaux. La coordination rédactionnelle de R4643-32 reste hors lot ; le coût d'organisation et le solde public net ne sont pas chiffrés.",
    "Aucune charge nouvelle n'est identifiée : l'avis écrit quinze jours à l'avance existait déjà et conserve ses destinataires ; aucun tableau, calendrier, donnée ou circuit alternatif obligatoire n'est ajouté.",
    [effect(
        'obligation_removed', 'cse-calendrier-annuel-transmission-suppression',
        "Suppression de l'envoi annuel distinct du calendrier des réunions santé, sécurité et conditions de travail.",
        "Information annuelle du calendrier à l'inspection, au médecin du travail et à la prévention sociale, puis confirmation écrite de chaque réunion au moins quinze jours à l'avance.",
        "Aucun envoi annuel distinct sur ce fondement, même par renvoi ; information écrite de chaque réunion aux mêmes trois destinataires au moins quinze jours à l'avance conservée.",
        'legal_duty', "Employeurs des entreprises relevant de la section d'au moins cinquante salariés et destinataires de l'information de prévention.",
        "Transmissions annuelles non effectuées à l'entrée en vigueur, même pour l'année en cours ; aucun rattrapage requis ; convocations anciennes et droits historiques conservés.",
        "Aucun rapport de remplacement ; maintien de l'information individuelle, des invitations et des délais autonomes déjà applicables.",
        old_27,
        "Aucune information annuelle distincte portant sur le calendrier de ces réunions n'est exigée au titre du présent alinéa, y compris par un renvoi à celui-ci.",
    )],
    ["Transmission annuelle distincte du calendrier des réunions de santé, sécurité et conditions de travail aux destinataires du quatrième alinéa, y compris lorsqu'un règlement y renvoie."],
    "Les quatre réunions au moins, les réunions supplémentaires de prévention, l'intervention de l'inspection en cas de défaillance et la participation des professionnels de prévention demeurent. Les salariés et représentants futurs conservent ces protections ; la suppression du calendrier annuel ne ferme ni la formation, ni les enquêtes, ni les invitations, ni les recours.",
)


proposed_28 = by_number['L2315-28']['source_xml'].replace("à l'article 2312-19", "à l'article L. 2312-19")
rewrite(
    'L2315-28', proposed_28,
    "Coordination nécessaire, sans réforme de fréquence : correction du renvoi incomplet « article 2312-19 » en « article L. 2312-19 », dont le contenu a été vérifié. Les réunions mensuelles à partir de trois cents salariés, bimestrielles en dessous dans cette section, et la seconde réunion à la demande de la majorité sont conservées. L'accord permet déjà d'adapter le calendrier dans le respect de son propre plancher ; aucune suppression automatique de réunion n'est justifiée par cette seule correction.",
    "L2312-19 a été lu en entier : accord dans les conditions qu'il fixe, au moins six réunions annuelles et autres garanties propres aux consultations. L2315-28 relève de la section des entreprises d'au moins cinquante salariés : « moins de trois cents » ne vise pas ici les entreprises de moins de cinquante. R2312-47, lu, rend aussi cette disposition applicable au comité des activités sociales et culturelles interentreprises ; la correction ne modifie pas cette extension. L2315-27 conserve les réunions de sécurité et L2315-31 les questions demandées par la majorité.",
    "Seul le repère législatif incomplet est corrigé. Aucune fréquence, majorité, compétence de convocation ou formalité de la source entière n'est retirée.",
    "La coordination ne démontre aucune baisse de coût ni de nombre de réunions ; elle n'étend pas la règle bimestrielle aux entreprises d'au moins trois cents salariés.",
    "Aucune charge nouvelle n'est identifiée : la correction renvoie au même article existant et ne crée aucun accord, dossier, délai ou réunion supplémentaire.",
    [effect(
        'coordination', 'cse-renvoi-accord-periodicite',
        "Rétablissement de la lettre L manquante dans le renvoi à l'accord sur les consultations et réunions.",
        "Renvoi écrit « article 2312-19 », sans lettre de la partie législative ; fréquences supplétives et demande majoritaire inchangées.",
        "Renvoi explicite à L. 2312-19, avec les mêmes fréquences supplétives, seuils et faculté majoritaire de seconde réunion.",
        'other', "CSE relevant de L2315-28 et instances auxquelles ce texte est rendu applicable.",
        "Correction du repère sans transition substantielle, sans remise en cause des accords ou convocations existants et sans réouverture d'un délai.",
        "Aucune charge nouvelle ; aucun nombre de réunions supprimées n'est attribué à cette coordination.",
        "A défaut d'accord prévu à l'article 2312-19",
        "A défaut d'accord prévu à l'article L. 2312-19",
    )],
)

retain(
    'L2315-29',
    "Maintien intégral de l'ordre du jour commun au président et au secrétaire et de l'inscription de plein droit des consultations obligatoires par l'un ou l'autre. La première règle organise la réunion ; la seconde empêche un blocage unilatéral de la consultation. Le document n'est pas un double rapport et sa suppression affaiblirait la participation éclairée des élus. Aucune nouvelle cosignature ni autorisation préalable n'est ajoutée.",
    "Articuler avec L2315-23 sur la désignation du secrétaire, L2315-30 sur la communication et L2315-31 sur les questions jointes à une demande majoritaire. L'inscription de plein droit reste ouverte séparément au président ou au secrétaire ; elle n'est pas subordonnée à l'accord des deux. Aucune consultation supprimée dans un autre lot n'est rétablie par ce maintien général.",
    "Les deux voies d'établissement et d'inscription de la source sont maintenues, sans transformer l'ordre du jour en nouveau rapport.",
    "L'article ne définit pas lui-même les consultations : seules celles qui restent obligatoires sur un fondement en vigueur sont concernées.",
    "Aucune charge nouvelle n'est identifiée : aucun document annexe, justificatif, deuxième vote ou signature supplémentaire n'est exigé.",
)

retain(
    'L2315-30',
    "Maintien intégral de la communication de l'ordre du jour trois jours au moins avant la réunion aux membres, à l'inspection et à la prévention sociale. Ce minimum assure un temps utile de préparation et le contrôle effectif ; l'ordre du jour n'est pas identique au calendrier annuel supprimé à L2315-27. Le texte n'impose aucun support postal exclusif ni second exemplaire à retirer.",
    "Délai exact de trois jours, sans ajout de la qualification ouvrable ou calendaire absente de la source. L2315-27 garde l'annonce écrite à quinze jours pour les réunions de santé et sécurité, qui porte sur une information distincte ; R4523-15 conserve trente jours pour la commission élargie. Pas de nouvelle exigence d'ordre du jour quinze jours avant toutes les réunions. Les destinataires de cette source ne sont pas modifiés.",
    "Le délai et les destinataires de la source entière sont maintenus. L'envoi de l'ordre du jour n'est pas compté comme un doublon supprimé avec le calendrier annuel.",
    "Le maintien ne tranche pas les règles de computation des délais ; les dispositions spéciales plus longues demeurent dans leur champ propre.",
    "Aucune charge nouvelle n'est identifiée : ni support imposé, ni nouveau destinataire, ni anticipation accrue, ni ordre du jour en double n'est ajouté.",
)

retain(
    'L2315-31',
    "Maintien intégral de l'inscription à l'ordre du jour des questions jointes à la demande de réunion de la majorité. Cette conséquence rend effectif le droit de réunion de L2315-28 : sans elle, la convocation pourrait être vidée de son objet. Elle réemploie les questions déjà présentées et ne requiert pas un nouveau dossier ou un vote supplémentaire.",
    "La majorité reste celle des membres visée par le texte, sans la remplacer par une majorité des présents. Articuler avec L2315-28 et L2315-29 ; aucun changement n'est fait à la majorité de délibération de L2315-32, distincte de la demande de convocation.",
    "La source entière reste applicable : les questions déjà jointes à la demande majoritaire entrent à l'ordre du jour, sans charge documentaire distincte.",
    "Le maintien n'ouvre pas une réunion à la demande d'un seul membre et ne modifie pas les autres convocations ou consultations obligatoires.",
    "Aucune charge nouvelle n'est identifiée : les questions existantes sont utilisées sans nouvelle attestation de majorité, note explicative ou dépôt.",
)

retain(
    'L2315-32',
    "Maintien intégral de la majorité des membres présents et de l'exclusion du président du vote lorsqu'il consulte les élus en tant que délégation du personnel. Ces règles assurent la décision collective et l'indépendance de l'avis des salariés ; supprimer la majorité ou autoriser le vote patronal dans ce cas atteindrait une protection essentielle. Aucune formalité de scrutin supplémentaire n'est exigée dans cet article.",
    "Distinguer majorité des membres présents pour les résolutions et majorité des membres pour la demande de réunion de L2315-28 et L2315-31. L2314-1 renvoie à cette majorité pour la désignation du référent ; ce renvoi reste cohérent. L'exclusion du président est liée à la consultation des élus comme délégation, non à toutes les décisions du comité indistinctement.",
    "Aucune modification par rapport à la source entière : même assiette de majorité et même exclusion ciblée du vote du président.",
    "Les règles spéciales de secret ou de majorité prévues ailleurs ne sont pas remplacées par cette règle générale ; aucune simplification du vote n'est revendiquée.",
    "Aucune charge nouvelle n'est identifiée : aucun quorum, registre électoral, formalité de vote ou recours préalable n'est ajouté.",
)


assert len(sources) == 24
assert set(answers) == set(by_number)
ordered = [answers[a['number']] for a in sources]
Path('answer.json').write_text(json.dumps(ordered, ensure_ascii=False, indent=2) + '\n')
