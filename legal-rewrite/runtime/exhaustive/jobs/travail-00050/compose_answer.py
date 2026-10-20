import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
references = json.loads(Path('reference-targets.json').read_text())
by_number = {a['number']: a for a in sources}
answers = {}


def retain(number, reason, notes, assessment, limitations, burdens, benefit=None):
    a = by_number[number]
    obj = {k: a[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    obj.update(
        proposed_xml=None,
        reason=reason,
        review_notes=notes,
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
        reference_checks=[],
    )
    if benefit:
        obj['benefit_review'] = benefit
    answers[number] = obj


def effect(kind, measure, description, before, after, unit, population,
           transition, replacement, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure, description=description,
                before=before, after=after, unit=unit,
                affected_population=population,
                conditions_and_transition=transition,
                replacement_or_new_burdens=replacement,
                source_quote=source_quote, proposed_quote=proposed_quote)


def rewrite(number, xml, reason, notes, classification, assessment,
            limitations, burdens, effects, removed=None, repeal=None):
    a = by_number[number]
    obj = {k: a[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    obj.update(proposed_xml=xml, reason=reason, review_notes=notes,
               status='rewrite_draft', reference_checks=[],
               substantive_impact=dict(version=1, classification=classification,
                   assessment=assessment, scope_limitations=limitations,
                   new_burdens_review=burdens, effects=effects))
    if repeal:
        obj.update(change_type='full_repeal',
                   repeal_policy_id='editorial_direction_2026_10_19',
                   repeal_scope=repeal)
    if removed:
        obj.update(change_type='normative_reduction',
                   reform_policy_id='editorial_direction_2026_10_19',
                   removed_provisions=removed)
    answers[number] = obj


pv_measure = 'depot-pv-desaccord-suppression'
annual_measure = 'expression-salaries-fin-consultation-annuelle-inchangee'
cadence_measure = 'conseils-atelier-fin-cadence-bimestrielle'
penal_measure = 'expression-salaries-suppression-emprisonnement'

deposit_xml = (
    '<p>L’accord collectif relatif au droit d’expression des salariés est déposé dans '
    'les conditions prévues à l’article L. 2231-6. Aucun dépôt supplémentaire n’est '
    'exigé au titre du présent article.</p>'
    '<p>Le procès-verbal de désaccord relatif au droit d’expression des salariés, '
    'établi en application de l’article L. 2242-5, n’est soumis à aucun dépôt auprès '
    'de l’autorité administrative ou du greffe. Aucun envoi ni déclaration de '
    'remplacement n’est exigé. Le procès-verbal et son contenu restent régis par '
    'l’article L. 2242-5.</p>'
    '<p>La dispense de dépôt du procès-verbal s’applique à compter de l’entrée en '
    'vigueur de la loi, y compris aux procès-verbaux établis antérieurement dont le '
    'dépôt n’a pas encore été effectué. Aucun dépôt tardif ou de régularisation '
    'n’est exigé après cette date.</p>'
    '<p>Les dépôts déjà effectués conservent leurs effets. Aucun texte ni procès-verbal '
    'déjà établi n’est à refaire. Les droits et recours liés à ces actes sont préservés, '
    'sous réserve de l’application des dispositions répressives plus douces.</p>'
)
rewrite(
    'L2281-8', deposit_xml,
    'Coordination nécessaire du fondement spécial, avec suppression du dépôt '
    'des procès-verbaux de désaccord déjà proposée à L2242-5. La source imposait le dépôt de '
    'l’accord ou du procès-verbal ; l’accord demeure soumis au dépôt de droit commun de '
    'L2231-6 et le procès-verbal demeure établi avec son contenu utile. La suppression du '
    'dépôt du même procès-verbal constitue une seule mesure, sans seconde réduction attribuée à cet article.',
    'L2242-5 et L2231-6 ont été lus intégralement dans le corpus public, sources et propositions '
    'distinguées : le premier garde la preuve du désaccord mais dispense de dépôt ; le second '
    'conserve un dépôt général des accords, déjà proposé unique. R2242-1 reste une coordination '
    'réglementaire à réaliser hors de ce lot. Le renvoi à L2231-6 est nouveau dans cet article '
    'et ne figure pas dans les cibles de reference-targets.json ; son texte a été lu dans le '
    'corpus, sans ajouter de cible à reference_checks. L2242-5 est une référence existante. '
    'Ce dernier règle le procès-verbal et non l’établissement de l’accord : la proposition '
    'distingue explicitement les deux fondements de la phrase source. '
    'La transition couvre aussi les procès-verbaux anciens non encore déposés ; elle ne '
    'supprime ni les droits issus des accords ni le dépôt général de ces accords.',
    'coordination_only',
    'Le dépôt spécial du procès-verbal disparaît par rapport à la source entière ; '
    'la règle de dépôt de l’accord est maintenue par renvoi au droit commun. La dispense '
    'du dépôt du procès-verbal est la même mesure que celle de L2242-5 ; aucun double dépôt '
    'effectif d’accord n’étant démontré, aucune seconde formalité supprimée n’est comptée.',
    'Le dépôt de droit commun des accords reste obligatoire ; le règlement R2242-1 n’est '
    'pas réécrit ici. Aucun coût net de la mesure commune ni solde de complexité des codes n’est établi.',
    'Aucune charge nouvelle identifiée : pas de déclaration, registre, transmission ou '
    'certificat substitué au dépôt du procès-verbal ; le dépôt général des accords existait déjà.',
    [effect(
        'coordination', pv_measure,
        'Retrait du fondement spécial qui pourrait rétablir le dépôt du procès-verbal de désaccord.',
        'Dépôt administratif de l’accord ou du procès-verbal relatif au droit d’expression ; '
        'le procès-verbal est également visé par L2242-5.',
        'Aucun dépôt du procès-verbal sur ce fondement ; accord soumis au seul régime général de dépôt.',
        'legal_duty', 'Parties à la négociation sur le droit d’expression des salariés.',
        'Dépôts à effectuer après l’entrée en vigueur, même pour un procès-verbal déjà établi ; '
        'actes déjà déposés et droits associés préservés.',
        'Aucun envoi de remplacement ; établissement et contenu du procès-verbal conservés.',
        "L'accord ou le procès-verbal de désaccord, établi en application de l'article L. 2242-5, "
        "est déposé auprès de l'autorité administrative dans des conditions prévues par voie réglementaire.",
        'Le procès-verbal de désaccord relatif au droit d’expression des salariés, '
        'établi en application de l’article L. 2242-5, n’est soumis à aucun dépôt auprès '
        'de l’autorité administrative ou du greffe.'
    )],
    removed=['Obligation spéciale de dépôt du procès-verbal de désaccord relatif au '
             'droit d’expression des salariés, sans suppression du dépôt de l’accord collectif.']
)

retain(
    'L2281-9',
    'Maintien intégral à droit constant de la faculté de négocier par établissement ou '
    'groupe d’établissements. Elle évite une négociation obligatoirement centralisée. '
    'L’exigence de couverture de tous les établissements empêche que la décentralisation '
    'prive une partie des salariés de leur droit d’expression ; aucune autorisation ni '
    'transmission administrative n’est imposée par cette règle.',
    'La condition porte sur la couverture de la négociation, non sur la conclusion '
    'obligatoire d’un accord dans chaque établissement. Aucun seuil, durée ou renvoi '
    'n’est modifié. Cette faculté reste ouverte aux entreprises et établissements futurs.',
    'La source entière offre une organisation décentralisée sans multiplier légalement '
    'les dépôts. Sa conservation protège cette faculté ; aucun allègement nouveau n’est revendiqué.',
    'Les règles générales de validité et de dépôt des accords restent distinctes ; '
    'la négociation par établissement ne dispense pas de couvrir les autres unités.',
    'Aucune charge nouvelle identifiée : texte source conservé sans dossier, délai ou '
    'condition supplémentaire à la négociation décentralisée.'
)

retain(
    'L2281-10',
    'Maintien intégral à droit constant des cinq objets de l’accord supplétif : réunions, '
    'outils disponibles, liberté et transmission des expressions, connaissance des suites '
    'et situation de l’encadrement. Ces éléments rendent le droit d’expression effectif '
    'sans exiger un outil nouveau, un agrément ou un rapport administratif. Les retrancher '
    'laisserait sans garanties pratiques les salariés en l’absence d’accord d’organisation respecté.',
    'L2242-11 a été lu dans le corpus : il organise les thèmes, informations et périodicités '
    'de négociation, avec durée maximale de quatre ans ; le renvoi reste approprié au '
    'déclenchement supplétif et n’est pas un délai de rupture. Les 1° à 5° sont conservés '
    'sans changement d’ordre. Le 2° vise les outils disponibles et n’impose ni achat '
    'de plateforme ni expression exclusivement numérique. Le 4° maintient tous les destinataires.',
    'Les cinq garanties de contenu sont maintenues après examen de leurs charges ; '
    'aucune déclaration distincte ou doublon de dépôt ne résulte de cet article.',
    'La règle ne modifie ni la validité des accords ni les modalités spéciales des '
    'conseils d’atelier ; aucune économie de négociation n’est démontrée.',
    'Aucune charge nouvelle identifiée : pas de nouvelle donnée ni de support imposé ; '
    'les outils déjà disponibles et les cinq objets de l’accord restent ceux de la source.'
)

consult_xml = (
    "<p>Dans les entreprises où aucun délégué syndical n'a été désigné ou dans lesquelles "
    "un accord portant sur l'égalité professionnelle entre les femmes et les hommes et "
    "la qualité de vie et des conditions de travail n'a pas été conclu, l'employeur consulte "
    "le comité social et économique sur les modalités d'exercice du droit d'expression des salariés.</p>"
    '<p>Cette consultation intervient lors de la définition des modalités d’exercice du droit '
    'd’expression et de leur modification. Elle n’est pas renouvelée à échéance annuelle '
    'lorsque les modalités déjà soumises au comité demeurent inchangées.</p>'
    '<p>La suppression du renouvellement annuel s’applique à compter de l’entrée en vigueur '
    'de la loi, y compris aux modalités définies avant cette date. Les consultations déjà '
    'engagées sont menées à leur terme. Les avis déjà émis et les accords antérieurs '
    'conservent leurs effets. Les stipulations plus favorables relatives à l’exercice '
    'du droit d’expression et les obligations distinctes de négociation collective demeurent applicables.</p>'
)
rewrite(
    'L2281-11', consult_xml,
    'Réforme de fond : suppression de la consultation annuelle automatique sur des '
    'modalités inchangées dans les entreprises sans délégué syndical. Le champ du premier '
    'alinéa est intégralement maintenu ; la consultation reste préalable à la définition '
    'et à la modification des modalités, sans formalité de remplacement. La répétition '
    'calendaire ne justifie pas une charge autonome lorsque le même objet a déjà été soumis au comité.',
    'Coordination opératoire avec L2283-2 dans ce lot : aucun refus d’une répétition '
    'annuelle désormais non due ne peut être sanctionné. L2281-5 à L2281-7 et L2242-17 '
    'ont été lus : négociation et suivi syndicaux sont distincts et ne sont pas supprimés '
    'par cette dispense. L2281-6 prévoit trois ans, tandis que L2281-7 évoque un an en '
    'cas d’accord et trois ans sans accord : cette articulation préexistante n’est pas '
    'corrigée implicitement et ne rétablit pas une consultation annuelle du CSE. La note '
    'source du 31 mars 2022 reste historique. Ni majorité, secret, rémunération, recours '
    'ni information sur les changements ne sont retirés.',
    'material_reduction',
    'La source impose un renouvellement au moins annuel sans délégué syndical. La '
    'proposition retire effectivement ce renouvellement si l’objet déjà examiné ne '
    'change pas ; elle conserve la consultation nécessaire à toute définition ou modification.',
    'L’allègement ne couvre pas les modalités jamais soumises au comité, leurs modifications, '
    'les consultations déjà engagées ni les obligations de négociation ou stipulations '
    'plus favorables. Le gain de temps n’est pas chiffré.',
    'Aucune charge nouvelle identifiée : la consultation sur la définition ou la '
    'modification concrétise l’objet de la consultation déjà obligatoire. Aucune '
    'attestation annuelle d’absence de changement ni information de remplacement n’est créée.',
    [effect(
        'obligation_removed', annual_measure,
        'Suppression de la répétition annuelle sans modification des modalités déjà consultées.',
        'Dans les entreprises sans délégué syndical, consultation au moins une fois par an, même sans changement.',
        'Pas de renouvellement annuel pour les modalités déjà consultées et inchangées ; consultation sur leur définition et leurs modifications.',
        'legal_duty', 'Employeurs et CSE des entreprises sans délégué syndical soumis à L2281-11.',
        'À compter de l’entrée en vigueur, même pour des modalités antérieures ; '
        'consultations engagées achevées, accords et stipulations plus favorables maintenus.',
        'Aucun reporting de stabilité ni autre dépôt substitué ; consultation de fond conservée.',
        "Dans les entreprises où aucun délégué syndical n'a été désigné, cette consultation a lieu au moins une fois par an.",
        'Elle n’est pas renouvelée à échéance annuelle lorsque les modalités déjà soumises au comité demeurent inchangées.'
    )],
    removed=['Renouvellement au moins annuel de la consultation du CSE en l’absence de '
             'délégué syndical lorsque les modalités déjà consultées restent inchangées.']
)

retain(
    'L2282-1',
    'Maintien intégral à droit constant du champ complémentaire propre aux entreprises '
    'de la loi du 26 juillet 1983. Ce renvoi évite de confondre les conseils d’atelier '
    'du secteur public avec le régime général et ne crée aucune démarche d’accès. '
    'Le supprimer ferait disparaître le fondement des droits de réunion maintenus à L2282-2 et L2282-3.',
    'Le caractère complémentaire est conservé. L’article 1er de la loi n° 83-675 est '
    'un texte extérieur aux cinq codes et son corps n’est pas fourni dans les cibles '
    'de ce lot : aucune modification de son énumération ou de son évolution n’est '
    'présumée. Le contrat unique de droit privé ne remplace pas les statuts d’agents publics.',
    'Le texte entier fixe seulement le champ du régime complémentaire ; son maintien '
    'est nécessaire pour les droits de réunion, sans nouvelle simplification comptabilisée.',
    'Le contenu externe de la loi de 1983 n’est pas réécrit et le champ des agents '
    'publics n’est pas étendu au contrat unique par ce renvoi.',
    'Aucune charge nouvelle identifiée : maintien de la seule règle de champ, sans '
    'autorisation, déclaration ou pièce de rattachement ajoutée.'
)

atelier_xml = (
    "<p>L'ensemble des salariés, y compris le personnel d'encadrement direct, de chaque "
    "atelier ou bureau constituant une unité de travail bénéficient du droit de réunion "
    "en conseil d'atelier ou de bureau.</p>"
    "<p>Les salariés se réunissent par atelier ou par bureau à raison d'au moins six "
    "heures par an pendant le temps de travail. Le temps consacré à ces réunions ne peut "
    "donner lieu à réduction de rémunération. Les salariés s'y expriment dans tous les "
    "domaines intéressant la vie de l'atelier ou du bureau.</p>"
    "<p>Le personnel d'encadrement ayant la responsabilité directe de l'atelier ou du "
    "bureau est associé à l'organisation des réunions et aux suites à leur donner.</p>"
    '<p>La suppression de la périodicité obligatoire d’une réunion tous les deux mois '
    's’applique aux réunions à organiser à compter de l’entrée en vigueur de la loi. '
    'Elle ne réduit ni le minimum annuel de six heures, ni les rémunérations, droits '
    'et créances nés avant cette date. Les accords en vigueur conservent leurs effets '
    'et les stipulations plus favorables restent applicables, y compris pour les salariés '
    'embauchés après cette date.</p>'
)
rewrite(
    'L2282-2', atelier_xml,
    'Réforme de fond ciblée : retrait de la cadence légale bimestrielle des conseils '
    'd’atelier ou de bureau, pour permettre de répartir les réunions selon l’organisation '
    'du travail. Le minimum annuel de six heures, la rémunération intégrale, le champ '
    'de tous les salariés, la liberté des sujets et l’association de l’encadrement '
    'sont maintenus intégralement. Il n’est pas démontré que six échéances séparées '
    'soient nécessaires au-delà du volume garanti et des modalités négociées.',
    'L2282-3, traité dans ce lot, garde notamment son 2° relatif à la fréquence et à la '
    'durée : le calendrier peut être négocié sans intervalle maximal imposé par L2282-2. '
    'L2281-4 lu dans le corpus assure le temps de travail rémunéré ; il n’est pas '
    'neutralisé. R2282-1, lu intégralement, prévoit encore un rapport annuel d’activité : '
    'ce rapport distinct n’est ni supprimé ni ajouté par cette proposition et son examen '
    'reste hors lot. La transition ne fait pas disparaître les périodicités conventionnelles '
    'en vigueur et ne réduit pas le minimum annuel par un prorata nouveau.',
    'material_reduction',
    'La source cumule une réunion au moins tous les deux mois avec six heures annuelles '
    'payées. Seule la contrainte de dispersion bimestrielle est supprimée ; le droit '
    'annuel et sa rémunération restent entiers. Ce changement n’est pas une baisse de salaire.',
    'Le gain porte sur l’organisation du calendrier dans le champ de L2282-1, sans '
    'minimum conventionnel bimestriel maintenu. Aucun nombre net de réunions évitées '
    'ni coût annuel économisé n’est démontré ; le volume minimal reste six heures.',
    'Aucune charge nouvelle identifiée : pas de déclaration ni de calendrier administratif '
    'substitutif ; la détermination conventionnelle de la fréquence existe déjà à L2282-3.',
    [effect(
        'obligation_removed', cadence_measure,
        'Suppression de l’intervalle légal maximal de deux mois entre les conseils d’atelier ou de bureau.',
        'Réunion au moins tous les deux mois et au moins six heures par an, toutes rémunérées comme temps de travail.',
        'Au moins six heures par an rémunérées ; aucun intervalle bimestriel légal, accords plus favorables préservés.',
        'legal_duty', 'Entreprises du secteur public relevant de L2282-1 et salariés des unités de travail concernées.',
        'Réunions à organiser après l’entrée en vigueur ; droits, rémunérations et '
        'créances antérieurs et périodicités conventionnelles préservés.',
        'Aucun nouveau dépôt ou rapport ; six heures annuelles et association de l’encadrement conservées.',
        "Les salariés se réunissent par atelier ou par bureau au moins une fois tous les "
        "deux mois et à raison d'au moins six heures par an pendant le temps de travail.",
        "Les salariés se réunissent par atelier ou par bureau à raison d'au moins six heures par an pendant le temps de travail."
    )],
    removed=['Cadence légale imposant au moins une réunion du conseil d’atelier ou de '
             'bureau tous les deux mois, indépendamment du volume annuel rémunéré.']
)
answers['L2282-2']['benefit_review'] = (
    'Le droit de réunion de tous les salariés et de l’encadrement, le minimum de six '
    'heures annuelles pendant le travail et l’absence de réduction de rémunération sont '
    'expressément conservés. Les accords plus favorables gardent leurs effets pour les '
    'salariés actuels et futurs ; les rémunérations et créances antérieures demeurent '
    'dues. La seule cadence légale bimestrielle est retirée, sans plafond de six heures '
    'ni suppression du droit de négocier une fréquence plus favorable.'
)

retain(
    'L2282-3',
    'Maintien intégral à droit constant des sept objets du régime complémentaire '
    'd’expression. L’unité de taille réduite, la participation des équipes isolées, '
    'l’association de l’encadrement, les compétences et les liaisons rendent effectif '
    'le droit de réunion. L’article n’exige ni second accord distinct, ni agrément, '
    'ni transmission administrative ; aucune suppression de formalité autonome n’y est démontrée.',
    'Les 1° à 7° et la faculté finale d’attribuer des responsabilités demeurent à leur '
    'place. Le 2° permet de régler la fréquence et la durée après suppression de la '
    'seule cadence bimestrielle à L2282-2 : il ne fixe lui-même aucun intervalle de '
    'deux mois. Les conditions de travail, programmes d’activité et d’investissement, '
    'innovation et productivité du 5° sont conservés sans réduire les domaines de compétence.',
    'Le contenu utile de l’accord est maintenu ; les recoupements avec L2281-10 ne '
    'prouvent pas deux négociations ou documents obligatoirement distincts à fusionner.',
    'Ce maintien ne revendique pas une seconde simplification de calendrier ; le '
    'minimum annuel de six heures demeure celui de L2282-2 et les accords existants restent applicables.',
    'Aucune charge nouvelle identifiée : les sept objets et la faculté de déléguer '
    'des responsabilités restent ceux de la source, sans rapport ou protocole additionnel.'
)

penal_transition = (
    '<p>La suppression de la peine d’emprisonnement prend effet à l’entrée en vigueur '
    'de la loi. Elle bénéficie aux faits antérieurs dans les conditions d’application '
    'de la loi pénale plus douce. Les effets des condamnations antérieures sont régis '
    'par les règles générales d’application de la loi pénale dans le temps. Les droits '
    'des salariés et les actions tendant à la mise en œuvre de la négociation ou de '
    'la consultation légalement due demeurent préservés.</p>'
)
neg_penal = (
    "<p>Le fait pour l'employeur de refuser d'engager la négociation en vue de la "
    "conclusion d'un accord définissant les modalités d'exercice du droit d'expression "
    "des salariés, prévue à l'article L. 2281-5, est puni d'une amende de 3 750 euros.</p>"
    + penal_transition
)
rewrite(
    'L2283-1', neg_penal,
    'Réforme de fond : suppression de l’emprisonnement d’un an pour le seul refus '
    'd’engager la négociation sur l’expression des salariés. L’infraction et l’amende '
    'de 3 750 euros restent intégralement applicables ; l’obligation de négocier et '
    'l’accès au juge subsistent. Le maintien de cette répression pécuniaire permet '
    'de retirer la peine privative de liberté sans dépénaliser le refus ni supprimer le droit protégé.',
    'L2281-5 a été lu dans le corpus : négociation sur l’égalité professionnelle et '
    'la qualité de vie et des conditions de travail, non autorisation de licenciement. '
    'La peine pécuniaire de 3 750 euros n’est ni augmentée ni indexée. La transition '
    'réserve les règles de la loi pénale plus douce et les effets légaux des condamnations, '
    'sans promettre une restitution générale des amendes définitives. Même mesure de '
    'retrait de l’emprisonnement à L2283-2 ; les deux hypothèses ne sont pas deux formalités supprimées.',
    'material_reduction',
    'La source prévoit cumulativement un an d’emprisonnement et 3 750 euros d’amende. '
    'La proposition ne conserve que l’amende : allègement pénal réel, sans suppression '
    'de la négociation, de l’infraction ou de sa sanction pécuniaire.',
    'Aucune baisse de taxe, de nombre de négociations ou d’obligations déclaratives '
    'n’en résulte. L’effet dissuasif résiduel et les coûts contentieux ne sont pas '
    'chiffrés ; les autres infractions demeurent autonomes.',
    'Aucune charge nouvelle identifiée : ni procédure administrative substitutive '
    'ni amende nouvelle. Le fait réprimé et le montant de l’amende sont ceux de la source.',
    [effect(
        'relief_extended', penal_measure,
        'Régime pénal plus favorable par retrait de la peine privative de liberté, avec maintien de l’amende.',
        'Pour le refus de négocier visé à L2281-5 : un an d’emprisonnement et 3 750 euros d’amende.',
        'Pour le même refus : 3 750 euros d’amende, sans peine d’emprisonnement prévue par cet article.',
        'other', 'Employeurs auteurs du refus de négocier défini à L2283-1.',
        'À l’entrée en vigueur et aux faits antérieurs selon les règles de loi pénale plus douce ; '
        'effets des condamnations antérieures soumis au droit général.',
        'Aucune sanction de remplacement ; obligation de négocier, infraction et amende maintenues.',
        "Le fait pour l'employeur de refuser d'engager la négociation en vue de la conclusion "
        "d'un accord définissant les modalités d'exercice du droit d'expression des salariés, "
        "prévue à l'article L. 2281-5, est puni d'un emprisonnement d'un an et d'une amende de 3 750 euros.",
        "Le fait pour l'employeur de refuser d'engager la négociation en vue de la conclusion "
        "d'un accord définissant les modalités d'exercice du droit d'expression des salariés, "
        "prévue à l'article L. 2281-5, est puni d'une amende de 3 750 euros."
    )],
    removed=['Peine d’emprisonnement d’un an pour le refus d’engager la négociation sur '
             'les modalités d’exercice du droit d’expression des salariés.']
)

consult_penal = (
    "<p>Dans les entreprises et organismes où aucun délégué syndical n'a été désigné "
    "ou dans lesquels l'accord définissant les modalités d'exercice du droit d'expression "
    "des salariés, prévu à l'article L. 2281-5, n'a pas été conclu, le fait de refuser "
    "de consulter le comité social et économique, lorsque cette consultation est "
    "requise en application de l'article L. 2281-11, est puni d'une amende de 3 750 euros.</p>"
    '<p>L’absence de renouvellement annuel d’une consultation qui n’est plus exigé '
    'par l’article L. 2281-11 ne constitue pas l’infraction prévue au premier alinéa.</p>'
    + penal_transition
)
rewrite(
    'L2283-2', consult_penal,
    'Réforme de fond : suppression de l’emprisonnement d’un an pour le refus de '
    'consultation, avec maintien de l’amende de 3 750 euros et du recours à une '
    'consultation effective. Coordination nécessaire : la sanction ne vise que les '
    'consultations légalement dues et ne rétablit pas la répétition annuelle supprimée '
    'à L2281-11. Les conditions de champ initiales restent cumulées avec cette exigence, '
    'sans extension de l’infraction à une autre catégorie d’employeurs.',
    'Décalage préexistant identifié : L2283-2 vise l’absence d’accord définissant '
    'l’expression selon L2281-5, tandis que L2281-11 vise l’absence d’accord d’égalité '
    'professionnelle et de qualité de vie et des conditions de travail. La proposition '
    'ne les assimile pas ; elle conserve les conditions initiales et exige en outre '
    'une consultation réellement obligatoire. Le renvoi nouveau à L2281-11, fourni '
    'dans source.json mais absent des cibles de reference-targets.json, est expressément '
    'signalé ; aucune cible facultative n’est ajoutée à reference_checks. Même mesure '
    'pénale que L2283-1 et simple coordination de la dispense annuelle : pas deux '
    'gains de consultation. La loi pénale plus douce s’applique selon ses règles propres, '
    'sans amnistie générale ni effacement promis des amendes définitives.',
    'material_reduction',
    'Le retrait de la peine d’emprisonnement allège réellement le régime répressif. '
    'Le texte subordonne aussi la sanction à une consultation due, en cohérence '
    'avec la dispense annuelle ; cette dernière est une coordination de la mesure de L2281-11.',
    'Le refus d’une consultation obligatoire reste puni de 3 750 euros ; l’examen '
    'des actes et condamnations antérieurs relève du droit pénal transitoire. Aucune '
    'économie nationale ni diminution du nombre de contentieux n’est démontrée.',
    'Aucune charge nouvelle identifiée : l’amende existante demeure sans relèvement '
    'et le renvoi à L2281-11 borne l’infraction au lieu de créer une consultation ou '
    'une sanction administrative de remplacement.',
    [effect(
        'relief_extended', penal_measure,
        'Retrait de la peine privative de liberté dans l’hypothèse du refus de consultation du CSE.',
        'Pour le refus visé par la source : un an d’emprisonnement et 3 750 euros d’amende.',
        'Pour le refus de consultation réellement due dans le champ initial : 3 750 euros d’amende, sans emprisonnement.',
        'other', 'Employeurs relevant des conditions d’incrimination de L2283-2.',
        'À l’entrée en vigueur ; faits et condamnations antérieurs traités selon '
        'les règles générales de loi pénale plus douce.',
        'Aucune nouvelle amende ni procédure de remplacement ; consultation légalement due maintenue.',
        "Dans les entreprises et organismes où aucun délégué syndical n'a été désigné ou "
        "dans lesquelles l'accord définissant les modalités d'exercice du droit d'expression "
        "des salariés, prévu à l'article L. 2281-5, n'a pas été conclu, le fait de refuser "
        "de consulter le comité social et économique est puni d'un emprisonnement d'un an "
        "et d'une amende de 3 750 euros.",
        "Dans les entreprises et organismes où aucun délégué syndical n'a été désigné "
        "ou dans lesquels l'accord définissant les modalités d'exercice du droit d'expression "
        "des salariés, prévu à l'article L. 2281-5, n'a pas été conclu, le fait de refuser "
        "de consulter le comité social et économique, lorsque cette consultation est "
        "requise en application de l'article L. 2281-11, est puni d'une amende de 3 750 euros."
    ), effect(
        'coordination', annual_measure,
        'Exclusion expresse de la sanction pour le renouvellement annuel désormais dispensé.',
        'La sanction du refus de consultation pouvait couvrir la consultation annuelle obligatoire de L2281-11.',
        'L’absence de répétition annuelle non due ne constitue pas l’infraction ; '
        'les refus de consultations réellement obligatoires restent sanctionnés.',
        'legal_duty', 'Employeurs du champ pénal de L2283-2 bénéficiant de la dispense de L2281-11.',
        'Même entrée en vigueur que la dispense annuelle ; application de la loi pénale plus douce dans son champ.',
        'Aucune consultation de remplacement ; la mesure de dispense n’est comptée qu’une fois.',
        'le fait de refuser de consulter le comité social et économique est puni '
        "d'un emprisonnement d'un an et d'une amende de 3 750 euros.",
        'L’absence de renouvellement annuel d’une consultation qui n’est plus exigé '
        'par l’article L. 2281-11 ne constitue pas l’infraction prévue au premier alinéa.'
    )],
    removed=['Peine d’emprisonnement d’un an pour le refus de consultation du comité '
             'social et économique dans le champ du droit d’expression des salariés.']
)

retain(
    'L2301-1',
    'Maintien intégral à droit constant de la prise en compte, pour ce livre, des '
    'salariés des 2° et 4° de L1111-3. Cette dérogation empêche que les exclusions '
    'd’effectifs des emplois aidés retirent leurs droits de représentation. Elle '
    'n’est ni un prélèvement ni une déclaration ; l’abroger réduirait les garanties '
    'collectives au lieu de supprimer une formalité redondante.',
    'L1111-3 a été lu intégralement dans le corpus : 2° contrat initiative-emploi '
    'pendant l’aide L5134-72, 4° contrat d’accompagnement pendant l’aide L5134-30 ; '
    'les 1° et 6° n’entrent pas dans ce renvoi dérogatoire. La durée de l’aide '
    'ne devient pas la durée de l’emploi. La dérogation reste applicable aux emplois '
    'aidés futurs éligibles sous contrat unique. Le problème européen des exclusions '
    'd’effectifs résiduelles signalé dans les notes du corpus à L1111-3 reste à '
    'coordonner séparément, notamment au regard de l’article 3, paragraphe 1, '
    'de la directive 2002/14/CE et de l’arrêt CJUE du 15 janvier 2014, Association '
    'de médiation sociale, C-176/12. Ces textes primaires extérieurs ne sont pas '
    'fournis dans ce lot ; leur mention issue des notes ne vaut pas une nouvelle '
    'vérification de conformité. Cet article ne réduit pas les effectifs dérogatoires '
    'et ne prétend pas résoudre la difficulté pour tous les régimes.',
    'La dérogation favorable à la représentation des salariés aidés est intégralement '
    'maintenue ; aucun nouveau gain fiscal, social ou administratif n’est revendiqué.',
    'La règle vise le livre sur les institutions représentatives et les seuls 2° '
    'et 4° de L1111-3. Elle ne modifie pas les effectifs sociaux, les aides ou leurs '
    'durées ; la question européenne des autres exclusions n’est pas résolue dans ce lot.',
    'Aucune charge nouvelle identifiée : le calcul dérogatoire existant est conservé '
    'sans déclaration, attestation d’aide ni justificatif supplémentaire.',
    'Les avantages possibles sont la dérogation au décompte qui garantit la '
    'représentation des salariés en contrats initiative-emploi ou d’accompagnement '
    'dans l’emploi, et les aides auxquelles renvoient indirectement les 2° et 4° '
    'de L1111-3. La première reste intégralement applicable ; aucune aide, dispense '
    'ou exonération liée à ces emplois n’est supprimée. Le bénéfice vaut aussi '
    'pour les futurs emplois aidés éligibles dans le contrat unique, pendant la '
    'période d’aide pertinente, sans fixer de terme automatique à l’emploi.'
)

retain(
    'L2311-1',
    'Maintien intégral à droit constant du champ du CSE et des adaptations possibles '
    'pour les établissements publics. La réserve des mêmes garanties empêche une '
    'simplification de structure qui retirerait la représentation des salariés. '
    'L’article n’impose à l’employeur ni demande d’agrément ni dossier déclaratif '
    'susceptible d’être supprimé.',
    'Employeurs privés, EPIC et EPA employant dans les conditions du droit privé '
    'restent distingués. Les adaptations relèvent de décrets en Conseil d’État et '
    'doivent assurer les mêmes garanties ; cela n’assujettit pas les agents publics '
    'statutaires au contrat unique. La note d’entrée en vigueur au plus tard le '
    '1er janvier 2018 est historique, sans nouvelle date de bascule.',
    'La règle de champ et la garantie d’équivalence sont utiles ; aucune procédure '
    'individuelle d’autorisation n’y est créée et aucun allègement nouveau n’est compté.',
    'Les décrets d’adaptation propres à chaque établissement ne sont pas réécrits '
    'et l’applicabilité aux personnes publiques demeure limitée au champ de la source.',
    'Aucune charge nouvelle identifiée : le champ, la faculté d’adaptation et la '
    'garantie d’équivalence restent inchangés, sans dépôt ou donnée supplémentaire.'
)

retain(
    'L2311-2',
    'Maintien intégral à droit constant du CSE à onze salariés pendant douze mois '
    'consécutifs. La durée de franchissement évite la création immédiate de l’instance '
    'à la moindre fluctuation ; le seuil maintient une représentation effective. '
    'Le contrat unique n’impose de modifier ni ces deux chiffres ni les renvois '
    'fonctionnels aux règles générales et à celles du travail temporaire.',
    'Les cinq cibles requises ont été examinées séparément dans reference_checks, '
    'avec distinction des sources et propositions. Seuls L1111-2 et L1251-54 sont '
    'des renvois du corps source ; ni L1234-1, ni L1234-9, ni L1221-2 n’y sont cités. '
    'La proratisation, les exclusions de remplacement, le décompte distinct des '
    'intérimaires et l’absence de double compte des propositions cibles sont '
    'compatibles avec le maintien des renvois. La condition de trois mois de missions '
    'de L1251-54 n’est ni le seuil de douze mois de cet article ni une durée d’emploi. '
    'La note du 1er janvier 2018 est une entrée historique. Aucune procédure collective '
    'ou autorisation de rupture n’est réputée accomplie par un préavis individuel de quinze jours.',
    'La source conserve un seuil et une condition de stabilité déjà favorables '
    'aux petites entreprises, avec représentation à leur franchissement. Le '
    'maintien ne constitue pas une suppression d’instance ni une nouvelle baisse de charge.',
    'Les propositions de calcul d’effectifs doivent entrer en vigueur avec leurs '
    'propres transitions ; leur validité globale, notamment européenne, n’est pas '
    'établie par ce contrôle. Les règles de rupture ne sont pas des conditions de mise en place du CSE.',
    'Aucune charge nouvelle identifiée : seuil de onze et douze mois inchangés, '
    'aucun registre de missions ou justificatif de préavis ajouté par cet article.'
)

retain(
    'L2312-1',
    'Maintien intégral à droit constant de la répartition des attributions selon '
    'l’effectif. La section 2 donne les garanties de proximité et la section 3 '
    'les attributions plus larges à partir de cinquante salariés. La dernière '
    'phrase récapitulative n’est pas une obligation distincte : la retirer ne '
    'supprimerait aucune charge et ne justifie pas une réécriture stylistique.',
    'Les deux renvois aux sections du même chapitre restent exacts. Le seuil '
    'de cinquante ne se confond pas avec les onze salariés de mise en place '
    'de L2311-2 ; les transitions de L2312-2 et L2312-3 sont conservées dans ce lot. '
    'La note du 1er janvier 2018 ne fixe aucune échéance future.',
    'La répartition complète des compétences est maintenue ; aucune attribution '
    'n’est supprimée et le rappel général ne compte pas comme un doublon de procédure fusionné.',
    'Les moyens matériels et consultations détaillées des sections suivantes '
    'restent régis par leurs textes ; aucune économie de seuil n’est chiffrée.',
    'Aucune charge nouvelle identifiée : les seuils, sections et compétences '
    'restent inchangés, sans nouveau calcul ou transmission.'
)

retain(
    'L2312-2',
    'Maintien intégral à droit constant des délais d’adaptation lors du passage '
    'à cinquante salariés. Ces délais constituent déjà un allègement de transition : '
    'les supprimer accélérerait les obligations, contrairement à l’orientation '
    'retenue. La condition liée au mandat évite une extension récurrente '
    'immédiatement suivie d’un renouvellement.',
    'Premier alinéa : douze mois consécutifs à cinquante, puis douze mois pour '
    'les attributions récurrentes ; si le mandat restant est inférieur à un an '
    'à l’expiration de ce délai, celui-ci court du renouvellement. Second alinéa : '
    'en l’absence de CSE, un an depuis sa mise en place pour l’ensemble des '
    'attributions de la section 3. Ces champs différents sont maintenus et '
    'ne deviennent pas un délai de préavis. Note d’application historique de 2018 lue.',
    'Les délais protecteurs de mise en conformité sont conservés dans toute '
    'leur portée ; il n’y a ni délai raccourci ni obligation nouvelle.',
    'La règle ne dispense pas de toutes les consultations ponctuelles avant '
    'le terme du premier alinéa ; aucune extension de la transition à un autre '
    'seuil ou à un régime public n’est proposée.',
    'Aucune charge nouvelle identifiée : maintien des deux branches et de '
    'leurs délais existants, sans nouvelle déclaration de franchissement de seuil.'
)

retain(
    'L2312-3',
    'Maintien intégral à droit constant du retour aux seules attributions de '
    'la section 2 lors du renouvellement après baisse durable sous cinquante '
    'salariés. Cette règle allège déjà les attributions sans supprimer '
    'brutalement en cours de mandat les garanties collectives.',
    'Le contrôle porte sur les douze mois précédant le renouvellement et '
    'non sur douze mois suivant une rupture individuelle. Les renvois aux '
    'sections 2 et 3 restent cohérents avec L2312-1. La règle ne prononce '
    'pas la disparition du CSE à onze salariés ; note historique de 2018 conservée à son objet.',
    'La réduction de compétences déjà prévue après baisse d’effectif reste '
    'disponible pour les renouvellements futurs ; aucun gain supplémentaire n’est attribué au maintien.',
    'Le moment de bascule et les attributions de la section 2 restent '
    'inchangés ; aucun effet sur les mandats ou créances en cours n’est ajouté.',
    'Aucune charge nouvelle identifiée : même période de douze mois, même '
    'renouvellement et aucun document justificatif supplémentaire.'
)

retain(
    'L2312-4',
    'Maintien intégral à droit constant de la réserve des dispositions '
    'conventionnelles et usages plus favorables. Cette clause protège '
    'l’autonomie collective et les avantages de représentation, pour '
    'l’avenir aussi ; elle ne prescrit ni autorisation ni déclaration à retirer.',
    'La réserve vise les attributions du CSE, non un rétablissement de CDD '
    'ni une modification des paramètres individuels de rupture. Aucun accord '
    'ou usage n’est dénoncé de plein droit par ce maintien. La note '
    'd’application de 2018 reste purement historique.',
    'La clause favorable est intégralement préservée ; sa suppression '
    'ne serait pas un allègement administratif mais un retrait de droits collectifs.',
    'La validité, la dénonciation et la portée de chaque accord ou usage '
    'restent régies par leurs règles propres ; aucun avantage nouveau chiffré n’est attribué.',
    'Aucune charge nouvelle identifiée : la faculté de prévoir ou conserver '
    'des attributions plus favorables demeure sans approbation ou justificatif nouveau.'
)

retain(
    'L2312-5',
    'Maintien intégral à droit constant des réclamations salariales et sociales, '
    'de la prévention, des enquêtes, de l’alerte et de la saisine de l’inspection. '
    'L’accès au conseil d’administration sur demande est nécessaire lorsque '
    'l’employeur immédiat ne peut donner suite aux réclamations. La présentation '
    'des actions de prévention donne accès à leur contenu utile et n’impose '
    'pas un second document distinct du document unique.',
    'Lecture de L4121-3-1 : le 2° du III vise bien la liste d’actions consignée '
    'au document unique pour les moins de cinquante salariés, distincte du '
    'programme du 1°. L2312-59 et L2312-60 lus intégralement conservent '
    'les alertes sur les droits, les dangers graves et la santé publique. '
    'Les cinq alinéas, la demande devant le conseil d’administration et '
    'la présence du directeur ou de son représentant informé sont maintenus. '
    'La note du 31 mars 2022 est historique. Ces garanties ne sont pas '
    'écartées par les quinze jours de préavis individuel.',
    'Le contrôle de la source entière ne révèle pas de rapport autonome '
    'redondant imposé par cet article ; ses obligations servent la protection '
    'des salaires, de la santé et des recours, et sont conservées.',
    'Les formalités du document unique, les pouvoirs de l’inspection et '
    'les procédures d’alerte restent autonomes ; aucune suppression de leurs '
    'supports n’est inférée de ce maintien.',
    'Aucune charge nouvelle identifiée : présentation de la liste existante '
    'et voies de recours inchangées, sans nouveau rapport, registre ou justificatif.'
)

retain(
    'L2312-6',
    'Maintien intégral à droit constant de l’accès aux attributions du CSE '
    'pour les travailleurs, les salariés extérieurs et les intérimaires. '
    'Ces extensions assurent des recours chez l’utilisateur sur les matières '
    'qu’il maîtrise ; elles ne sont ni une déclaration d’emploi temporaire '
    'ni une permission de conclure de nouveaux CDD.',
    'L4111-5 et L1251-18, L1251-21 à L1251-24 ont été lus dans le corpus : '
    'rémunération et jours fériés sans ancienneté ; conditions de travail '
    'pendant la mission, santé et équipements gratuits ; accès égal aux '
    'transports et installations collectifs et remboursement au CSE des '
    'dépenses supplémentaires. Les 1°, 2°, 3° et a), b), c) sont conservés. '
    'Salarié temporaire décrit l’intérim, pas nécessairement un contrat '
    'à terme : les droits valent pour le futur contrat unique intérimaire '
    'sans rupture automatique à la fin de la mission et pour les anciens '
    'contrats dans leur transition. La note de 2018 ne crée pas de nouvelle date.',
    'Toutes les catégories et tous les objets de réclamation restent '
    'ouverts, y compris aux intérimaires futurs. La coordination du contrat '
    'unique n’exige pas de modifier ces renvois fonctionnels.',
    'La compétence du chef d’établissement utilisateur limite le 2°. '
    'L’article ne crée pas de rémunération d’intermission pour le portage '
    'et ne modifie ni les missions commerciales ni les contrats antérieurs.',
    'Aucune charge nouvelle identifiée : mêmes droits et mêmes destinataires, '
    'sans déclaration de mission, nouveau dossier ou attestation exigée.'
)

retain(
    'L2312-7',
    'Maintien intégral à droit constant du droit pour les travailleurs '
    'de présenter eux-mêmes leurs observations. Cette voie directe '
    'évite de transformer le CSE en intermédiaire obligatoire et conserve '
    'une liberté individuelle essentielle ; aucune formalité n’est à retirer.',
    'Aucune restriction d’effectif, d’ancienneté ou de forme écrite n’est '
    'ajoutée. La faculté vaut aussi pour les salariés sous contrat unique '
    'et n’écarte pas les réclamations par les représentants. La note '
    'historique de 2018 ne limite pas les situations futures.',
    'La source entière offre déjà un accès direct sans autorisation '
    'ni filtre ; elle reste nécessaire et aucun gain nouveau n’est compté.',
    'Les garanties contre les sanctions et les compétences des représentants '
    'relèvent de leurs textes ; aucune procédure contentieuse n’est modifiée.',
    'Aucune charge nouvelle identifiée : maintien du droit direct, sans '
    'délai de saisine, registre ou formulaire ajouté.'
)

retain(
    'L2312-8',
    'Maintien intégral à droit constant de la mission collective et des '
    'consultations générales sur l’emploi, l’organisation, le travail, '
    'les technologies et l’inclusion. Ces consultations protègent la '
    'participation effective et la santé ; la source n’exige pas une '
    'seconde procédure environnementale ou un rapport séparé qu’il '
    'serait possible de compter comme supprimé.',
    'Les I à IV, les cinq rubriques du II et la consultation sur leurs '
    'conséquences environnementales au III sont intégralement maintenus. '
    'L2312-14, L2312-15, L2312-16 et L2312-19 ont été lus : décision '
    'précédée de consultation avec exceptions, information utile, délai '
    'suffisant, majorité d’accord et articulation des consultations. '
    'Le présent maintien ne prétend ni supprimer ces procédures par '
    'le préavis individuel de quinze jours ni présumer la conformité '
    'de toutes les règles d’effectifs au droit européen d’information '
    'et de consultation, qui demeure à coordonner. La note de 2018 est historique.',
    'La source organise une consultation sur les décisions importantes, '
    'sans imposer dans son III un second vote ou dossier autonome. '
    'Aucune fusion nouvelle de procédures distinctes n’est démontrée ; les garanties sont maintenues.',
    'Les délais, expertises, consultations ponctuelles et obligations '
    'européennes restent à leur champ propre. Aucun délai global de '
    'quinze jours ni coût net de consultation n’est promis.',
    'Aucune charge nouvelle identifiée : champs de consultation et '
    'conséquences environnementales inchangés, sans inventaire, donnée '
    'ou avis supplémentaire ajouté.'
)

retain(
    'L2312-9',
    'Maintien intégral à droit constant des trois fonctions de santé '
    'et sécurité : analyse des risques, inclusion des femmes et personnes '
    'handicapées, initiatives contre le harcèlement et les agissements '
    'sexistes. La motivation du refus patronal rend cette prévention '
    'contrôlable ; elle n’est pas un justificatif administratif redondant.',
    'L4161-1 a été lu avec sa note sur les expositions 2015, 2016 et '
    'trois premiers trimestres de 2017 : les familles de risques restent '
    'visées sans restriction implicite. L1142-2-1 définit bien les '
    'agissements sexistes. Femmes enceintes, maternité, accès et maintien '
    'des personnes handicapées durant la vie professionnelle sont '
    'conservés. La note de 2018 et les périodes historiques de la '
    'cible risques ne sont pas des dates de réforme future.',
    'Les obligations conservées ont pour objet les risques professionnels '
    'et les discriminations ; leur examen n’a révélé aucun dépôt ou '
    'autorisation autonome à supprimer dans cet article.',
    'Les autres obligations d’évaluation des risques et les sanctions '
    'du harcèlement ne sont pas réécrites ; aucun gain de coût ni '
    'suppression de garantie de santé n’est revendiqué.',
    'Aucune charge nouvelle identifiée : analyse, initiatives et '
    'motivation des refus restent celles de la source, sans nouveau '
    'rapport ou donnée individuelle collectée.'
)

retain(
    'L2312-10',
    'Maintien intégral à droit constant de l’information des représentants '
    'lors d’une visite de l’inspection et de l’accompagnement facultatif '
    'de l’agent. Ces garanties empêchent que le contrôle soit privé '
    'des observations des salariés ; le caractère facultatif de '
    'l’accompagnement évite déjà une présence systématiquement imposée.',
    'L8112-1 a été lu dans le corpus : il définit les agents de contrôle '
    'et leur indépendance, y compris les contrôleurs jusqu’à extinction '
    'de leur corps. Les deux alinéas restent distincts : information '
    'par l’employeur, puis accompagnement si le membre du comité le '
    'souhaite. Aucun préavis de visite de l’inspection n’est ajouté. '
    'La note historique de 2018 est conservée à son objet.',
    'La source entière contient une information ponctuelle nécessaire '
    'à un contrôle éclairé par les observations des salariés et une faculté d’accompagnement, '
    'sans dépôt ou compte rendu distinct à retirer.',
    'L’autonomie des agents et leurs pouvoirs de contrôle restent '
    'inchangés ; le maintien ne transforme pas la visite en procédure '
    'soumise au consentement de l’employeur.',
    'Aucune charge nouvelle identifiée : aucun délai, formulaire de '
    'visite ni attestation d’information n’est ajouté au texte source.'
)

retain(
    'L2312-11',
    'Maintien intégral à droit constant de la réserve des compétences '
    'syndicales et de l’expression collective. Elle empêche la substitution '
    'du CSE aux libertés syndicales sans imposer deux procédures '
    'identiques. Aucun circuit administratif ou obligation de négocier '
    'distincte n’est créé par cette seule clause.',
    'La réserve reste cohérente avec les modalités d’expression de '
    'L2281-9 à L2281-11 et les majorités de négociation maintenues '
    'par les orientations. Elle ne rétablit ni transmission CPPNI '
    'ni consultation annuelle sur modalités inchangées supprimées '
    'à L2281-11. Note d’application de 2018 lue et historique.',
    'La clause préserve l’indépendance des voies collectives. Elle '
    'n’est pas un doublon d’obligation susceptible d’être supprimé '
    'comme une seconde formalité administrative.',
    'L’articulation concrète des consultations et des négociations '
    'reste régie par leurs textes ; aucune fusion de représentations '
    'ou suppression de majorité n’est proposée.',
    'Aucune charge nouvelle identifiée : maintien d’une réserve '
    'de compétences sans document, réunion ou transmission ajouté.'
)

retain(
    'L2312-12',
    'Maintien intégral à droit constant de l’initiative du CSE et de '
    'l’examen des propositions patronales sur le travail, l’emploi, '
    'la formation, la vie dans l’entreprise et la protection complémentaire. '
    'Ce droit favorise des solutions concrètes et n’exige ni rapport '
    'annuel, ni agrément, ni pièce autonome. Il reste utile après '
    'suppression des états de protection complémentaire décidée ailleurs.',
    'L911-2 du code de la sécurité sociale est lu intégralement dans '
    'reference-targets.json ; la cible est une source officielle '
    'sans proposition. Son champ comprend salariés, anciens salariés '
    'et ayants droit, décès, santé, maternité, incapacité, invalidité, '
    'inaptitude, chômage et avantages de retraite ou de fin de carrière. '
    'Le renvoi ne soumet pas ces avantages au seuil d’un an de '
    'l’indemnité ordinaire. Aucun état E1 à E3 ni délai de deux mois '
    'supprimé n’est rétabli. La note d’application de 2018 reste historique.',
    'La faculté d’initiative et l’examen des propositions restent '
    'nécessaires aux attributions du comité et aux garanties collectives ; '
    'aucune obligation déclarative distincte n’est révélée par la source entière.',
    'Le montant des garanties et les contributions de protection '
    'complémentaire ne sont pas fixés ici ; aucune suppression '
    'd’avantage, réduction de prélèvement ou transfert de financement n’est déduit de ce maintien.',
    'Aucune charge nouvelle identifiée : mêmes thèmes et même '
    'initiative, sans rapport périodique, modèle de données ou '
    'condition d’ancienneté nouvelle.'
)


checks_2311 = {
    'L1234-1': 'Cette cible règle le préavis de licenciement, non les effectifs du CSE. '
        'La source L2311-2 ne lui renvoie pas. La proposition cible distingue les nouveaux '
        'contrats, avec quinze jours calendaires sans condition d’ancienneté, et les '
        'anciens contrats gardant leurs durées. Elle ne déplace ni le seuil de onze '
        'salariés pendant douze mois ni les procédures collectives ou autorisations '
        'distinctes ; la notification et son point de départ relèvent de L1234-3, '
        'non de la règle d’effectifs maintenue ici.',
    'L1251-54': 'Renvoi direct du troisième alinéa de L2311-2 : il concerne les effectifs '
        'de l’entreprise de travail temporaire, avec permanents au 1° et temporaires '
        'au 2°, au moins trois mois de missions dans la dernière année civile. La '
        'proposition cible applique ce total aux missions du contrat unique, sans '
        'assimiler l’intérimaire au personnel permanent ni le compter deux fois. '
        'Cette durée n’est pas un terme d’emploi, ni une ancienneté de rupture ; '
        'les périodes anciennes conservent leurs règles et les douze mois du seuil '
        'CSE demeurent inchangés. Aucune notification de rupture n’en est déduite.',
    'L1221-2': 'Cette cible pose la durée indéterminée du nouvel emploi et protège '
        'les contrats antérieurs ; L2311-2 ne lui renvoie pas directement. Une '
        'mission ou formation limitée ne termine pas le contrat unique. Le maintien '
        'du seuil CSE s’articule avec les règles spécifiques de proratisation '
        'de L1111-2 et L1251-54, plutôt qu’avec un comptage intégral automatique '
        'de tout intérimaire. Aucun terme, délai de notification ou condition '
        'd’ancienneté individuelle n’est ajouté dans l’article conservé.',
    'L1111-2': 'Renvoi direct du troisième alinéa de L2311-2 : 1° temps plein, '
        '2° proratisations et exclusions de remplacement, 3° temps partiel. '
        'La proposition cible conserve les anciens CDD et transpose aux '
        'affectations temporaires réelles du contrat unique les règles de '
        'proratisation et de remplacement ; elle empêche le double compte '
        'des intérimaires chez l’utilisateur. Le renvoi demeure fonctionnel '
        'sans rétablir un terme d’emploi. L’année de présence et l’ancienneté '
        'de rupture sont distinctes ; aucune notification ni nouvelle pièce '
        'n’est imposée ici. La dérogation de L2301-1 reste applicable à son champ.',
    'L1234-9': 'Cette cible règle l’indemnité ordinaire, sans renvoi dans le '
        'corps de L2311-2. La proposition cible exige un an au terme effectif, '
        'préavis inclus ; à ce seuil elle compte toute l’ancienneté, à 0,20 mois '
        'par année, fractions en mois complets et plafond de six mois, à '
        'l’initiative de l’employeur et sous l’exception de faute grave qu’elle '
        'énonce. Elle préserve les anciennes composantes et indemnités '
        'spéciales. Ces paramètres ne sont ni une condition de représentation '
        'ni un report de mise en place du CSE. La notification n’est pas le '
        'terme auquel apprécier le seuil d’un an.',
}

for source in sources:
    number = source['number']
    key = source['code_id'] + '|' + source['source_id']
    for target_key in references['requirements'][key]:
        target = references['targets'][target_key]
        if number == 'L2311-2':
            assessment = checks_2311[target['number']]
        elif number == 'L2312-12':
            assessment = (
                'Le renvoi vise les objets de garanties collectives de L911-2 CSS, '
                'non le contrat privé de rupture. La source cible couvre les salariés, '
                'anciens salariés et ayants droit pour décès, santé et maternité, '
                'incapacité, invalidité, inaptitude, chômage et avantages de retraite '
                'ou fin de carrière. L2312-12 conserve intégralement l’initiative '
                'du comité à leur sujet ; aucune condition générale d’un an, de '
                'notification ou de préavis de quinze jours ne leur est appliquée. '
                'La suppression des modèles annuels de reporting social ne ferme '
                'aucune garantie future et le renvoi conservé ne rétablit pas ces modèles.'
            )
        else:
            raise ValueError(number)
        answers[number]['reference_checks'].append(dict(
            target_key=target_key, view_sha256=target['view_sha256'], assessment=assessment))

Path('answer.json').write_text(
    json.dumps([answers[a['number']] for a in sources], ensure_ascii=False, indent=2) + '\n'
)
