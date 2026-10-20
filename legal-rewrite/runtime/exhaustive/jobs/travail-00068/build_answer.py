import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
by_number = {s['number']: s for s in sources}
answers = {}


def retained(number, reason, notes, assessment, limits, burden):
    source = by_number[number]
    answers[number] = {
        key: source[key]
        for key in ('code_id', 'source_id', 'source_sha256', 'number')
    }
    answers[number].update(
        proposed_xml=None,
        reason=reason,
        review_notes=notes,
        status='retained_unchanged',
        classification='retained_necessary',
        substantive_impact={
            'version': 1,
            'classification': 'retained_necessary',
            'assessment': assessment,
            'scope_limitations': limits,
            'new_burdens_review': burden,
            'effects': [],
        },
    )


def effect(kind, measure, description, before, after, unit, population,
           transition, replacement, source_quote, proposed_quote):
    return dict(
        kind=kind, measure_id=measure, description=description,
        before=before, after=after, unit=unit,
        affected_population=population,
        conditions_and_transition=transition,
        replacement_or_new_burdens=replacement,
        source_quote=source_quote, proposed_quote=proposed_quote,
    )


def rewritten(number, xml, reason, notes, classification, assessment,
              limits, burden, effects, removed=None):
    source = by_number[number]
    result = {key: source[key] for key in
              ('code_id', 'source_id', 'source_sha256', 'number')}
    result.update(
        proposed_xml=xml,
        reason=reason,
        review_notes=notes,
        status='rewrite_draft',
        substantive_impact=dict(
            version=1, classification=classification,
            assessment=assessment, scope_limitations=limits,
            new_burdens_review=burden, effects=effects,
        ),
    )
    if removed:
        result.update(change_type='normative_reduction',
                      reform_policy_id='editorial_direction_2026_10_19',
                      removed_provisions=removed)
    answers[number] = result


retained(
    'L2363-3',
    "Maintien intégral après examen du renvoi : L. 2353-3 à L. 2353-6 délimitent les questions transnationales, organisent la réunion annuelle et la consultation en circonstances exceptionnelles et aménagent l'information en cas d'offre publique d'acquisition. Cette reprise mutualise déjà les règles de la société européenne ; supprimer le renvoi supprimerait les attributions effectives du comité, et non un rapport administratif autonome. Aucune réforme de fond ni reformulation n'est proposée.",
    "Les quatre articles cibles ont été lus intégralement dans travail.json : dix thèmes de réunion annuelle, réunion exceptionnelle à la demande et réunion dans les huit jours suivant la publication d'une offre restent applicables. La confidentialité avant publication demeure possible. Cadre européen à coordonner : directive 2003/72/CE et ses prescriptions subsidiaires d'information-consultation ; leur texte intégral n'est pas joint au lot. Le préavis individuel de quinze jours ne remplace aucun de ces délais collectifs.",
    "Aucune charge supprimée : le renvoi commun demeure nécessaire à l'information et à la consultation transnationales, distinctes des compétences nationales.",
    "Le maintien n'évalue ni le coût des réunions ni l'ensemble des obligations nationales ; aucune baisse de prélèvement ou de complexité globale n'est démontrée.",
    "Aucune charge nouvelle identifiée : maintien du champ, des réunions et des délais existants, sans rapport, registre ni justificatif supplémentaire.",
)

retained(
    'L2363-4',
    "Maintien intégral du renvoi de composition, après lecture de L. 2353-7 à L. 2353-12 : il fixe les catégories de membres, le nombre de sièges, la désignation ou l'élection, le recours judiciaire et l'adaptation conventionnelle de la composition. Il évite déjà de répéter un régime complet. Retirer ces règles compromettrait la représentation des salariés plutôt que supprimer un agrément ou une formalité redondante.",
    "Les six cibles ont été lues : les deux collaborateurs du dirigeant ont seulement voix consultative ; la voie élective demeure ouverte en l'absence d'organisation syndicale et les contestations relèvent du juge judiciaire. L. 2363-5 précise la désignation française. Les modifications de structure peuvent déjà donner lieu à un accord interne au comité. Le cadre de représentation de la directive 2003/72/CE reste à respecter ; aucune modification des sièges n'est proposée.",
    "Conservation de la composition représentative et de sa souplesse conventionnelle ; aucun second régime ni nouvelle procédure de validation n'est créé.",
    "Les effectifs propres à chaque société ne sont pas fournis ; aucun nombre concret de sièges ni coût de représentation n'est calculé.",
    "Aucune charge nouvelle identifiée : les règles de composition mutualisées restent identiques, sans nouvelle désignation ni nouvelle pièce à déposer.",
)

retained(
    'L2363-5',
    "Maintien intégral : la désignation des représentants des personnes participantes, filiales et établissements implantés en France garantit une représentation issue des élections et, en l'absence d'organisation syndicale, une élection directe. Après lecture des deux cibles, le renvoi ne constitue pas une autorisation administrative à supprimer. Il assure la légitimité des représentants sans créer un scrutin supplémentaire lorsque la désignation syndicale est possible.",
    "L. 2352-5 organise la désignation syndicale à partir des résultats des élections au CSE, les collèges et le plus fort reste ; L. 2352-6 ouvre l'élection directe selon les règles du CSE. Les deux sources intégrales ont été lues. La notification de la désignation sert notamment au recours et à la protection du mandat ; aucune suppression propre de cette notification n'est décidée ici. Règles européennes de libre désignation à préserver.",
    "Aucune réduction matérielle proposée : la voie subsidiaire d'élection empêche l'absence de syndicat de priver les salariés de représentation.",
    "Les modalités réglementaires de notification et de contentieux restent distinctes ; aucun allègement de ces procédures n'est compté dans cet article.",
    "Aucune charge nouvelle identifiée : les mêmes représentants sont désignés selon les mêmes résultats ou élus dans les mêmes cas, sans nouvelle approbation.",
)

source6 = by_number['L2363-6']['source_xml']
xml6 = (
    "<p>Les dispositions des articles L. 2353-13 à L. 2353-27-1 relatives au fonctionnement du comité de la société européenne s'appliquent à la société coopérative européenne.</p>"
    "<p>Pour l'application de ces dispositions, les références au secret professionnel et à l'obligation de discrétion prévus à l'article L. 2325-5 s'entendent des obligations définies à l'article L. 2363-7.</p>"
    "<p>Pour l'application de l'article L. 2353-27, les conditions du congé de formation sont celles prévues par l'article L. 2325-44 dans sa dernière rédaction en vigueur avant son abrogation.</p>"
    "<p>Par dérogation à l'article L. 2353-27-1, le recours à la visioconférence pour réunir le comité de la société coopérative européenne n'est subordonné ni à un accord préalable ni à un nombre maximal de réunions par année civile. Les réunions par visioconférence sont tenues dans les conditions prévues aux articles D. 2315-1 et D. 2315-2, applicables au comité de la société coopérative européenne. Les dépenses nécessaires à l'accès des représentants au dispositif sont prises en charge dans les conditions de l'article L. 2353-24.</p>"
    "<p>Les dispositions du quatrième alinéa s'appliquent aux réunions convoquées à compter de l'entrée en vigueur de la loi qui les institue. Elles ne remettent pas en cause les accords en vigueur prévoyant des garanties plus favorables à l'exercice du mandat ni la régularité des réunions antérieures.</p>"
)
rewritten(
    'L2363-6', xml6,
    "Réduction de fond ciblée du régime importé : suppression, pour ce comité, de l'accord préalable autorisant la visioconférence et du plafond supplétif de trois réunions par année civile de L. 2353-27-1. Les garanties techniques existantes D. 2315-1 et D. 2315-2 sont rendues directement applicables, car D. 2353-6 renvoie encore aux anciens D. 2325-1-1 et suivants. Identification, participation effective, suspension de séance, confidentialité et vote secret simultané demeurent, avec financement dans les ressources déjà dues au titre de L. 2353-24. Coordination distincte des renvois de confidentialité et fixation expresse du renvoi historique de formation ; aucun droit de formation n'est supprimé. Toutes les autres règles importées, notamment moyens, rémunération et consultation, restent intégrales.",
    "Lecture intégrale de L. 2353-13 à L. 2353-27-1, de D. 2353-6 et de D. 2315-1 et D. 2315-2. L. 2353-23 et L. 2353-26 utilisent encore L. 2325-5 : la règle spéciale les rattache ici à L. 2363-7 rédigé dans ce lot. L. 2353-27 vise L. 2325-44, absent du corpus courant : le renvoi est rendu expressément historique, sans lui substituer automatiquement L. 2315-63, dont le seuil, les titulaires et le financement ne doivent pas restreindre implicitement le droit antérieur. La dernière rédaction historique de L. 2325-44 n'est pas fournie et reste une pièce documentaire à confronter ; aucune équivalence intégrale avec le régime actuel du CSE n'est certifiée. D. 2353-6 doit être coordonné séparément pour son propre champ ; la dérogation législative assure immédiatement la règle pour les SCE. Les garanties conventionnelles plus favorables sont conservées. Le cadre européen d'implication effective des salariés reste applicable ; son texte intégral n'est pas joint. Aucun nombre de déplacements évités ni gain financier n'est inventé.",
    'material_reduction',
    "La source importe une autorisation conventionnelle au-delà de trois visioconférences annuelles ; la proposition retire cette condition et ce plafond pour les SCE. Les renvois techniques et de confidentialité sont coordonnés sans être comptés comme des suppressions supplémentaires. La formation reste attachée à ses conditions historiques.",
    "L'allègement concerne les comités de SCE et les convocations nouvelles, sous réserve des garanties conventionnelles plus favorables ; il ne modifie pas le régime propre du comité de société européenne ni celui des autres instances. Le coût net et la concordance historique complète du congé de formation ne sont pas établis.",
    "Aucune charge nouvelle identifiée : aucun accord, registre ou justificatif ne remplace l'accord supprimé ; les garanties techniques reprennent les règles du CSE et les dépenses d'accès relèvent des ressources déjà dues par L. 2353-24. Aucun équipement ou abonnement n'est mis à la charge du salarié. Le solde de l'ensemble des codes n'est pas chiffré.",
    [
        effect(
            'obligation_removed', 'sce-visioconference-sans-plafond',
            "Suppression de l'accord préalable et de la limite supplétive annuelle de recours à la visioconférence.",
            "Le renvoi à L. 2353-27-1 subordonne la visioconférence à un accord ; en l'absence d'accord, elle est limitée à trois réunions par année civile.",
            "Pour le comité de SCE, aucun accord préalable ni plafond légal annuel ; les conditions techniques, moyens financés et garanties conventionnelles plus favorables subsistent.",
            'legal_duty', 'Comités des sociétés coopératives européennes relevant du présent article.',
            "Réunions convoquées à compter de l'entrée en vigueur ; régularité antérieure et garanties conventionnelles plus favorables préservées.",
            "Aucune procédure de remplacement ; accès et secret du vote assurés dans le cadre des moyens déjà à la charge de la société.",
            source6,
            "le recours à la visioconférence pour réunir le comité de la société coopérative européenne n'est subordonné ni à un accord préalable ni à un nombre maximal de réunions par année civile.",
        ),
        effect(
            'coordination', 'sce-confidentialite-renvois',
            "Rattachement des références de confidentialité importées à la règle spéciale de L. 2363-7.",
            "Le renvoi général importe L. 2353-23 et L. 2353-26 qui visent L. 2325-5, absent du corpus courant.",
            "Les mêmes obligations sont définies par L. 2363-7 ; aucune seconde obligation de confidentialité n'est créée ni supprimée.",
            'legal_duty', 'Membres du comité de SCE et experts soumis aux règles importées.',
            "Coordination des références, sans suppression de la protection des informations confidentielles.",
            "Pas de déclaration ou d'attestation de confidentialité supplémentaire.",
            source6,
            "les références au secret professionnel et à l'obligation de discrétion prévus à l'article L. 2325-5 s'entendent des obligations définies à l'article L. 2363-7.",
        ),
        effect(
            'coordination', 'sce-formation-renvoi-historique',
            "Explicitation de la version historique régissant le congé importé de L. 2353-27.",
            "L. 2353-27 est incorporé avec un renvoi non daté à L. 2325-44, absent du corpus courant.",
            "Le renvoi désigne expressément la dernière rédaction en vigueur avant abrogation, sans appliquer les conditions distinctes du CSE actuel.",
            'other', 'Membres du comité de la société coopérative européenne.',
            "Maintien du droit de formation et de ses conditions historiques ; aucune extinction pour les futurs membres.",
            "Aucun dossier ou contrôle nouveau ; la confrontation du texte historique reste nécessaire.",
            source6,
            "les conditions du congé de formation sont celles prévues par l'article L. 2325-44 dans sa dernière rédaction en vigueur avant son abrogation.",
        ),
    ],
    ["L'accord préalable de recours à la visioconférence imposé par le renvoi à L. 2353-27-1 n'est plus requis pour le comité de SCE.",
     "La limite de trois réunions par visioconférence par année civile en l'absence d'accord est supprimée dans le champ des SCE."],
)

confidentiality = (
    "sont tenus au secret professionnel pour toutes les questions relatives aux procédés de fabrication et à une obligation de discrétion à l'égard des informations revêtant un caractère confidentiel et présentées comme telles par l'employeur."
)
xml7 = "<p>Les membres du comité de la société coopérative européenne ainsi que les experts qui les assistent " + confidentiality + "</p>"
rewritten(
    'L2363-7', xml7,
    "Coordination nécessaire : le texte source nomme le comité de la société européenne dans le titre de la SCE et vise l'ancien L. 2325-5. Le nouveau corps identifie expressément le comité de la société coopérative européenne et reproduit les qualifications matérielles de secret et de discrétion de L. 2315-3, lu intégralement. Cette protection est conservée pour permettre l'information utile du comité ; aucune confidentialité générale ou simple commodité de l'employeur ne remplace les deux conditions cumulatives de l'obligation de discrétion. Il ne s'agit pas d'une réduction de charge.",
    "Confronter avec L. 2353-23 et L. 2353-26, lus : leur ancien renvoi est adapté dans L. 2363-6 pour le champ SCE. Coordination commune avec L. 2364-4. L. 2315-3 fournit la qualification actuelle des procédés de fabrication et des informations confidentielles présentées comme telles. L. 2325-5 n'est pas présent dans le corpus courant ; aucune réactivation de cet ancien article n'est proposée. Les exigences européennes de confidentialité et le contrôle juridictionnel restent à leur champ. La formation et les autres informations transmissibles ne sont pas fermées.",
    'coordination_only',
    "Correction du champ institutionnel et remplacement du renvoi obsolète par la règle qualifiée de confidentialité ; aucune réduction d'impôt ou d'obligation essentielle n'est revendiquée.",
    "La dernière version historique de L. 2325-5 n'est pas jointe ; la concordance repose sur les qualifications actuelles de L. 2315-3, sans prétendre établir un gain de complexité net.",
    "Aucune charge nouvelle identifiée : les représentants et experts restent soumis aux seules catégories de secret et de discrétion déjà visées, sans attestation, registre ou extension à toute information.",
    [effect(
        'coordination', 'sce-confidentialite-renvois',
        "Correction de l'intitulé du comité et explicitation des obligations de confidentialité.",
        "Le texte du titre SCE désigne le comité de la société européenne et renvoie à L. 2325-5.",
        "Le comité de la société coopérative européenne et ses experts sont expressément visés ; procédés de fabrication et informations confidentielles désignées comme telles restent protégés.",
        'legal_duty', 'Membres du comité de SCE et experts les assistant.',
        "Coordination de la protection existante, applicable également aux futurs membres ; aucune levée du secret antérieurement dû.",
        "Aucune formalité de remplacement ; aucun nouvel engagement écrit.",
        "Les membres du comité de la société européenne ainsi que les experts qui les assistent",
        "Les membres du comité de la société coopérative européenne ainsi que les experts qui les assistent",
    )],
)

retained(
    'L2363-8',
    "Maintien intégral des règles subsidiaires de participation : le 1° conserve au moins le niveau de droits existant lors d'une transformation ; le 2° organise le choix de la forme de participation après examen des systèmes nationaux lorsque les seuils de L. 2362-7 sont atteints. Il s'agit de garanties contre la disparition de la représentation à l'occasion de la création de la SCE, et non d'un agrément ou d'un prélèvement accessoire. La liberté de conclure un accord et la décision qualifiée de ne pas négocier demeurent.",
    "L. 2362-7 a été lu intégralement : double majorité ordinaire, décision spéciale aux deux tiers, interdiction de cette dernière pour certaines transformations, seuils de 25 % pour la fusion et de 50 % pour les autres constitutions concernés par son troisième alinéa. Ces règles ne sont pas fusionnées avec les seuils de cinquante salariés de L. 2363-11 ou L. 2363-13. Le cadre de participation de la directive 2003/72/CE reste à respecter ; aucune baisse de droits n'est proposée.",
    "Les deux branches de participation sont conservées, avec l'équivalence protectrice en cas de transformation et les seuils renvoyés ; aucun allègement matériel nouveau.",
    "Aucun effectif, système national ou accord propre à une opération n'est fourni ; le niveau concret de participation n'est pas déterminé dans ce lot.",
    "Aucune charge nouvelle identifiée : mêmes cas subsidiaires, mêmes seuils et mêmes droits, sans examen administratif ou pièce supplémentaire.",
)

retained(
    'L2363-9',
    "Maintien intégral de la mutualisation des règles de participation en l'absence d'accord. Les quatre cibles lues fixent le choix entre systèmes existants, le niveau le plus élevé de participation, les modalités de recommandation ou d'élection et la répartition transnationale des sièges. Ce mécanisme protège des droits représentatifs et contient déjà une voie de décision en l'absence d'accord du groupe ; sa suppression n'allégerait pas une autorisation redondante mais retirerait les garanties de participation.",
    "Lecture de L. 2353-29 à L. 2353-32 : choix patronal subsidiaire limité par le niveau le plus élevé, exception de territorialité pour l'élection, répartition proportionnelle et attribution d'au moins un siège dans la mesure du possible. L. 2363-10 ajoute le siège garanti de l'Etat du siège social et reste entier. Les cibles de commerce L. 225-28 à L. 225-34 et L. 225-80 ne sont pas jointes au corpus autorisé ; leur rédaction n'est pas présentée comme vérifiée ni modifiée. Cadre européen de participation conservé.",
    "Aucun second prélèvement ni formalité supprimé : le renvoi commun et la dérogation protectrice de L. 2363-10 demeurent nécessaires.",
    "Le contrôle documentaire des articles du code de commerce visés par L. 2353-31 reste extérieur au corpus fourni ; aucun gain sur leurs procédures n'est revendiqué.",
    "Aucune charge nouvelle identifiée : le choix subsidiaire, l'élection et les sièges gardent leur régime existant ; aucun visa ou dépôt de remplacement.",
)

retained(
    'L2363-10',
    "Maintien intégral de la dérogation favorable : l'Etat du siège social bénéficie d'au moins un siège, en dérogation à la répartition proportionnelle importée par L. 2363-9. Cet avantage de représentation n'est ni une taxe ni une autorisation ; sa suppression retirerait une garantie sans éliminer le régime général de participation. Il reste applicable aux répartitions futures, et non seulement aux mandats déjà en cours.",
    "L. 2353-32 a été lu : proportionnalité au premier alinéa et garantie seulement dans la mesure du possible au second. Le renvoi de L. 2363-10 vise précisément le premier alinéa et assure ici un siège en tout état de cause. Ne pas transformer cette garantie de représentation en exonération fiscale ni compter son maintien comme une réduction nouvelle. Articulation à conserver avec le cadre de participation de la directive 2003/72/CE.",
    "L'avantage de représentation minimale du pays du siège est conservé intégralement pour les répartitions futures ; aucune réduction matérielle nouvelle.",
    "Aucun effectif ni nombre total de sièges propre à une SCE n'est fourni ; l'incidence concrète de la dérogation sur chaque répartition n'est pas chiffrée.",
    "Aucune charge nouvelle identifiée : la garantie d'au moins un siège est maintenue à l'identique, sans nouvelle condition de preuve ou de demande.",
)
answers['L2363-10']['benefit_review'] = (
    "L'unique avantage identifié est la dérogation assurant, en tout état de cause, au moins un siège à l'Etat dans lequel se trouve le siège social de la SCE, même si la seule proportionnalité du premier alinéa de L. 2353-32 ne le lui attribuait pas. Cet avantage représentatif, et non fiscal, est conservé intégralement avec son renvoi exact par L. 2363-9. Il reste ouvert aux constitutions, recompositions et répartitions futures éligibles, sans condition nouvelle et sans limitation aux droits déjà acquis. Aucune taxe n'est instituée ou supprimée par cet article."
)

retained(
    'L2363-11',
    "Maintien intégral de la dispense favorable de constitution initiale du groupe spécial et du régime ordinaire associé. Elle vise les SCE formées exclusivement de personnes physiques ou d'une seule personne morale et de plusieurs personnes physiques, employant ensemble moins de cinquante salariés ou au moins cinquante dans un seul Etat membre. Supprimer cette exception pendant que le régime général subsiste alourdirait les obligations. La dispense reste ouverte aux nouvelles constitutions recevables ; les règles nationales et les déclencheurs ultérieurs restent distincts.",
    "Les deux branches d'effectif sont conservées sans les confondre : moins de cinquante salariés, ou au moins cinquante dans un seul Etat membre. Lire avec L. 2363-12 pour les droits nationaux et L. 2363-13 pour la demande d'un tiers dans au moins deux Etats ou le seuil transnational de cinquante salariés. Le cadre européen spécial des SCE constituées par des personnes physiques est identifié dans la directive 2003/72/CE ; la dispense n'est pas étendue aux SCE formées de plusieurs personnes morales.",
    "Conservation de l'exemption initiale pour toutes les futures sociétés éligibles ; aucune nouvelle dispense ni baisse de charge n'est comptée.",
    "La dispense ne supprime ni les droits nationaux d'implication ni les déclencheurs transnationaux ultérieurs et ne couvre pas toutes les formes de constitution d'une SCE.",
    "Aucune charge nouvelle identifiée : maintien des deux branches favorables, sans déclaration nouvelle de dispense ni autorisation préalable.",
)

retained(
    'L2363-12',
    "Maintien intégral des deux branches nationales d'implication des salariés des SCE dispensées du dispositif initial. L'article préserve la consultation et, le cas échéant, la participation selon le droit français, l'exception à la territorialité de L. 225-28 et la proportionnalité transnationale ; les filiales et établissements relèvent du droit de leur Etat. Il ne crée pas un second comité européen. Retirer les garanties ou l'exception territoriale au motif d'une simplification fermerait des droits utiles.",
    "Les titres Ier et II actuels du livre ont été identifiés dans le corpus : comité social et économique et conseil d'entreprise, ce dernier exerçant les attributions du CSE conformément à L. 2321-1, et institué selon L. 2321-2. Le renvoi n'est donc pas supprimé au seul motif de son ancienneté. Les articles L. 225-27 à L. 225-34, L. 225-79 et L. 225-80 du code de commerce ne sont pas joints ; leur concordance détaillée reste à contrôler hors corpus. Aucune suppression de l'exception territoriale ou du caractère éventuel de la participation. Les deux subdivisions sont conservées.",
    "Aucun allègement nouveau : le régime national protège les salariés sans rétablir le groupe spécial initial dont L. 2363-11 les dispense.",
    "Les cibles du code de commerce ne sont pas disponibles dans les fichiers autorisés ; aucune conformité de leurs modalités ni application à une opération déterminée n'est certifiée.",
    "Aucune charge nouvelle identifiée : les mêmes obligations nationales, le caractère éventuel de la participation et la dérogation territoriale restent inchangés, sans dossier européen additionnel.",
)

retained(
    'L2363-13',
    "Maintien intégral des déclencheurs ultérieurs du groupe spécial de négociation pour les SCE initialement dispensées : demande d'au moins un tiers des salariés employés dans au moins deux Etats membres, ou atteinte du seuil de cinquante salariés dans au moins deux Etats membres. Ces déclencheurs évitent qu'une dispense liée à la petite taille initiale ferme durablement la représentation après développement transnational. Aucune autorisation administrative autonome, taxe ou justification répétée n'est imposée ici.",
    "Le chapitre II a été lu pour les dispositions utiles, notamment L. 2362-4 : négociation dès constitution du groupe, six mois et prolongation conventionnelle dans la limite d'un an, rémunération des réunions. Ni un tiers ni cinquante salariés ne sont remplacés par le seuil de 10 % de réouverture propre à L. 2354-3. Cadre spécial européen des SCE initialement dispensées à préserver. Le renvoi de période de L. 2363-16 est coordonné dans ce lot.",
    "Conservation des deux déclencheurs transnationaux et des droits de négociation ; la dispense initiale subsiste dans son propre champ.",
    "Aucun droit de convocation au-dessous de ces conditions n'est créé ; les effectifs et demandes propres à une société ne sont pas disponibles.",
    "Aucune charge nouvelle identifiée : mêmes seuils, même demande et même négociation ; aucune nouvelle déclaration périodique d'effectifs n'est introduite.",
)

retained(
    'L2363-14',
    "Maintien intégral du comité subsidiaire en cas d'échec de la négociation ouverte après la dispense initiale. L'absence d'accord ne peut priver les salariés d'implication, sauf décision qualifiée du groupe spécial de ne pas poursuivre selon L. 2362-7. Le renvoi mutualise les règles ordinaires de mise en place, attributions et fonctionnement au lieu de créer un dispositif parallèle. La suppression de ce filet de protection ne serait pas la suppression d'un doublon.",
    "L. 2363-13 renvoie au chapitre II et donc à la période de L. 2362-4 ; il ne fixe pas lui-même un autre délai. L. 2363-1 et L. 2363-2 et la décision qualifiée de L. 2362-7 ont été lus. L'application de L. 2363-7 vise la règle de confidentialité coordonnée dans le présent lot ; celle de L. 2363-6 bénéficie de sa réforme propre, sans nouvelle réduction à compter ici. Conserver le dispositif subsidiaire européen et la rémunération des mandats.",
    "Maintien de la représentation subsidiaire après échec ; la mutualisation des règles existe déjà et ne constitue pas une fusion nouvelle.",
    "Le gain éventuel de visioconférence relève exclusivement de la mesure de L. 2363-6 et n'est pas recompensé comme une réduction autonome dans cet article.",
    "Aucune charge nouvelle identifiée : aucun comité supplémentaire ni nouvelle durée de négociation ; les règles communes existantes et leurs coordinations s'appliquent.",
)

retained(
    'L2363-15',
    "Maintien intégral des deux règles de désignation : pour la France, premier alinéa de L. 2352-5 ou voie élective de L. 2352-6 ; pour les autres Etats membres, droit de chacun de ces Etats. Cette répartition évite une procédure française supplémentaire pour les représentants étrangers. La désignation démocratique et l'élection subsidiaire sont nécessaires à la légitimité du comité et ne sont pas des agréments administratifs à supprimer.",
    "Les cibles L. 2352-5 et L. 2352-6 ont été lues intégralement ; la mention du premier alinéa de L. 2352-5 est conservée exactement, sans étendre silencieusement le renvoi. L'absence de syndicat ne ferme pas l'élection directe. La mention de la Communauté européenne est historique ; son seul remplacement lexical ne justifie pas un nouveau corps normatif. Aucune compétence française nouvelle sur les désignations étrangères n'est créée.",
    "Aucune réforme matérielle : le partage entre désignation française et droits nationaux des autres Etats demeure une garantie et une limitation de procédure.",
    "Les législations des autres Etats ne sont pas jointes ; leur contenu et leurs délais propres ne sont pas présentés comme vérifiés.",
    "Aucune charge nouvelle identifiée : aucune validation en France des désignations étrangères ni notification supplémentaire n'est ajoutée.",
)

xml16 = "<p>Lorsque, à l'issue de la période de négociation prévue à l'article L. 2363-13, aucun accord n'a été conclu et que le groupe spécial de négociation n'a pas pris la décision prévue au deuxième alinéa de l'article L. 2362-7, la participation des salariés est organisée conformément aux dispositions des articles L. 2363-8 à L. 2363-10.</p>"
rewritten(
    'L2363-16', xml16,
    "Coordination nécessaire à droit constant : le texte source attribue une période de négociation à L. 2363-14 alors que cet article organise le comité après échec. Le renvoi est corrigé vers L. 2363-13, qui ouvre la négociation conformément au chapitre II. Le cas d'absence d'accord, la décision de L. 2362-7 et toutes les garanties de participation de L. 2363-8 à L. 2363-10 restent identiques. Aucune suppression de charge n'est revendiquée.",
    "Incohérence préexistante identifiée expressément : L. 2363-14 ne définit pas une période de négociation. L. 2363-13 et L. 2362-4 lus ensemble donnent les six mois de négociation et l'éventuelle prolongation conventionnelle dans la limite d'un an. La correction ne recommence aucun délai, ne ferme pas une négociation en cours et ne modifie ni l'exclusion qualifiée de L. 2362-7 ni le siège favorable de L. 2363-10. Aucune réduction du délai collectif n'est tirée du préavis individuel de quinze jours.",
    'coordination_only',
    "Le seul changement est la correction du renvoi de période, de L. 2363-14 vers L. 2363-13 ; les droits subsidiaires et les délais restent inchangés.",
    "La correction n'établit aucun gain de coût ou de durée et n'altère pas le cadre européen de participation après échec des négociations.",
    "Aucune charge nouvelle identifiée : pas de nouvelle négociation, de nouveau dépôt ni de remise à zéro d'une période ; seul le renvoi erroné est remplacé.",
    [effect(
        'coordination', 'sce-negociation-renvoi-periode',
        "Correction du renvoi vers l'article qui ouvre la négociation des SCE initialement dispensées.",
        "La période est attribuée à L. 2363-14, qui organise le comité après échec.",
        "La période renvoie à L. 2363-13 et, par son intermédiaire, au chapitre II ; durées et droits inchangés.",
        'other', 'Salariés et SCE relevant des articles L. 2363-11 à L. 2363-16.',
        "Correction sans recommencement des périodes en cours ni restriction des participations déjà ouvertes.",
        "Aucune formalité ou charge de remplacement.",
        "à l'issue de la période de négociation prévue à l'article L. 2363-14",
        "à l'issue de la période de négociation prévue à l'article L. 2363-13",
    )],
)

retained(
    'L2363-17',
    "Maintien intégral de l'équivalence minimale des droits de participation en cas de transfert du siège vers un autre Etat membre. Cette règle protège les salariés contre la perte de droits par déplacement du siège ; elle n'impose pas une autorisation, un formulaire ou un prélèvement. Elle demeure applicable aux transferts futurs aussi bien qu'aux droits existants. Sa suppression serait une régression de la participation et non la suppression d'un doublon administratif.",
    "L'article ne fixe ni quota fiscal ni délai d'attente ; il vise les seules SCE régies par des règles de participation. Articulation avec L. 2364-3 et les changements de structure ou de localisation de L. 2354-4, lus dans le corpus. Le régime européen de la SCE et de l'implication des salariés demeure distinct des formalités commerciales de transfert, hors du lot. Le mot Communauté n'est pas réécrit pour produire un changement purement stylistique.",
    "La garantie de niveau au moins équivalent est conservée pour les transferts futurs, sans extension du champ ni nouvelle procédure de contrôle.",
    "Aucun transfert déterminé ni droit étranger n'est fourni ; le respect de l'équivalence dans une opération particulière n'est pas évalué.",
    "Aucune charge nouvelle identifiée : même maintien de droits, sans attestation d'équivalence ou agrément de transfert ajouté par cet article.",
)

retained(
    'L2363-18',
    "Maintien intégral de la voie de participation avec droit de vote aux assemblées générales, de section ou de branche, lorsque le droit de l'Etat du siège et les statuts de la SCE la prévoient conformément au règlement européen. Les dirigeants français organisent alors la désignation selon les modalités de la SCE. Ce mécanisme donne effet à un droit de vote déjà choisi ; il ne généralise pas une nouvelle représentation obligatoire à toutes les coopératives. Supprimer ce mécanisme fermerait un avantage aux salariés.",
    "Toutes les conditions sont conservées : Etat du siège admettant le système, conditions du paragraphe 4 de l'article 59 du règlement (CE) n° 1435/2003, prévision statutaire et société effectivement régie par ce système. Le règlement n'est pas joint intégralement ; sa formule et ses conditions ne sont pas remplacées par une inférence. Coordination avec la rémunération de L. 2363-19, la confidentialité de L. 2364-4 et la protection de L. 2364-5. Aucun nouveau dossier de désignation n'est ajouté.",
    "Maintien de la possibilité de vote et de sa mise en œuvre en France pour les futurs salariés éligibles ; aucune obligation générale supplémentaire.",
    "Le règlement européen et les statuts d'une SCE particulière ne sont pas joints ; leur application détaillée n'est pas réputée contrôlée.",
    "Aucune charge nouvelle identifiée : la désignation ne joue que pour les sociétés déjà régies par ce système et reste organisée selon leurs modalités existantes.",
)

retained(
    'L2363-19',
    "Maintien intégral de l'assimilation des réunions d'assemblées au temps de travail et du paiement à l'échéance normale. C'est une garantie de rémunération permettant l'exercice effectif du droit de participation prévu par L. 2363-18, non une taxe ou un document redondant. La réforme du contrat unique et de l'indemnité de rupture ne supprime aucun salaire dû pour ces réunions. Le droit demeure ouvert aux futurs participants éligibles.",
    "L. 2363-18 a été lu : un seul alinéa définit les assemblées générales, de section ou de branche concernées ; le renvoi à son premier alinéa reste opérant. Le maintien de salaire n'est pas confondu avec l'indemnité ordinaire de rupture, ni plafonné à six mois ou conditionné à un an d'ancienneté. La visioconférence n'enlève pas le caractère rémunéré des réunions.",
    "Conservation du salaire des participants aux assemblées ; aucune réduction de rémunération, de cotisation ou de coût de conformité n'est revendiquée.",
    "Le montant salarial dépend des réunions et des rémunérations individuelles non fournis ; aucun coût global ni gain d'emploi n'est chiffré.",
    "Aucune charge nouvelle identifiée : le temps rémunéré et l'échéance de paiement restent identiques, sans justificatif ou condition d'ancienneté nouveau.",
)

retained(
    'L2364-1',
    "Maintien intégral de la faculté conventionnelle d'aménager ou supprimer les institutions nationales qui auraient vocation à disparaître par perte d'autonomie juridique après immatriculation de la SCE. Cette disposition permet déjà de traiter les doubles structures sans dissolution automatique des droits représentatifs. La supprimer retirerait une souplesse favorable ; la transformer en suppression patronale unilatérale méconnaîtrait le consentement collectif. Aucun allègement nouveau n'est donc compté.",
    "L. 2362-10 et son renvoi au contenu de l'accord ont été lus pour le cadre de négociation ; la possibilité d'un accord collectif au niveau approprié demeure alternative. Conserver les conditions de perte d'autonomie juridique d'une ou plusieurs sociétés participantes situées en France et l'immatriculation préalable. Aucun maintien imposé de structures réellement redondantes n'est ajouté, aucune majorité de conclusion d'accord n'est abaissée.",
    "La faculté d'aménagement ou de suppression par accord existe déjà et reste ouverte aux opérations futures ; elle n'est pas une nouvelle fusion de régimes.",
    "Aucun accord ni périmètre national particulier n'est fourni ; aucune institution concrète n'est réputée supprimée par le présent maintien.",
    "Aucune charge nouvelle identifiée : même voie d'accord, sans agrément administratif, rapport périodique ou condition de délai supplémentaire.",
)

retained(
    'L2364-2',
    "Maintien intégral de l'examen après quatre ans de l'opportunité d'une négociation et du maintien du comité jusqu'à son renouvellement ou remplacement. L'examen n'impose pas de conclure un accord ; le comité fait lui-même office de groupe spécial, ce qui évite déjà la création d'un second organe. Cette réévaluation et la continuité de représentation répondent aux prescriptions subsidiaires européennes ; aucune fonction purement redondante n'est démontrée permettant de les supprimer.",
    "Conserver les trois alinéas et le délai de quatre ans, distinct du délai de deux ans de réouverture après refus de négocier de L. 2354-3. L. 2362-1 et L. 2362-2, lus, définissent le groupe et sa mission. L'examen après quatre ans figure dans le cadre des prescriptions subsidiaires de la directive 2003/72/CE à coordonner ; aucun nouveau rapport annuel n'en est déduit. Le comité ne disparaît pas à l'expiration des quatre ans.",
    "Aucun allègement nouveau : l'organe existant assume déjà la négociation et reste en fonction, sans doublon institutionnel à supprimer ici.",
    "Aucun comité particulier ni date de constitution n'est fourni ; le texte européen intégral n'est pas joint et n'est pas réputé abrogé par une réforme nationale.",
    "Aucune charge nouvelle identifiée : même examen ponctuel après quatre ans, aucune réunion annuelle de remplacement ni nouveau groupe à constituer.",
)

xml43 = (
    "<p>Les articles L. 2354-3 et L. 2354-4 relatifs aux règles applicables postérieurement à l'immatriculation de la société européenne s'appliquent aux sociétés coopératives européennes dans les conditions suivantes.</p>"
    "<p>Pour leur application, les références au chapitre II et au chapitre III s'entendent de références aux mêmes chapitres du présent titre.</p>"
    "<p>Pour l'application de l'article L. 2354-3, la référence à la décision prévue à l'article L. 2352-13 s'entend de la référence à la décision prévue au deuxième alinéa de l'article L. 2362-7.</p>"
    "<p>Pour l'application de l'article L. 2354-4, la référence aux modalités d'implication arrêtées en application de l'article L. 2353-28 et suivants s'entend de la référence aux modalités arrêtées en application des articles L. 2363-8 à L. 2363-10. En cas d'échec des négociations, les dispositions applicables sont celles des articles L. 2363-3 à L. 2363-10 ; la condition préalable à l'immatriculation prévue à l'article L. 2363-2 ne remet pas en cause l'immatriculation déjà intervenue.</p>"
)
rewritten(
    'L2364-3', xml43,
    "Coordination nécessaire du régime commun postérieur à l'immatriculation : les cibles L. 2354-3 et L. 2354-4 renvoient au régime de négociation et de participation de la société européenne. Le nouveau corps les adapte expressément au titre de la SCE, à sa décision qualifiée de L. 2362-7 et à sa participation subsidiaire de L. 2363-8 à L. 2363-10. Le seuil de demande de 10 %, le délai de deux ans avec réouverture anticipée d'accord commun et l'obligation de renégociation en cas de changement substantiel restent ceux des cibles, sans altération. La condition d'immatriculation importée dans un régime postérieur à celle-ci est clarifiée sans invalider une immatriculation existante. Aucun nouvel allègement autonome n'est revendiqué.",
    "L. 2354-3 et L. 2354-4 ont été lus intégralement. Incohérence préexistante signalée : L. 2354-4 prévoit, après immatriculation, l'application de L. 2353-2 et suivants, dont le premier texte conditionne précisément l'immatriculation. La proposition applique à l'échec de la renégociation les droits matériels SCE de L. 2363-3 à L. 2363-10 et exclut toute remise en cause rétroactive de l'immatriculation sur cette seule base ; elle ne supprime pas les conditions initiales de L. 2363-2. Les changements de structure, de localisation du siège ou d'effectif substantiels restent tous concernés. R. 2364-1, lu intégralement avec ses notes de 2020, conserve une voie de recours cohérente : procédure accélérée au fond devant le président du tribunal judiciaire et pouvoir d'ordonner la constitution du groupe spécial. Son renvoi à L. 2364-3 en tant qu'il applique L. 2354-4 reste opérant ; il n'est pas présenté comme réécrit. Le régime propre des sociétés européennes n'est pas réécrit ici. Les règles européennes de réouverture et de protection contre le contournement restent à respecter.",
    'coordination_only',
    "Les renvois incorporés sont adaptés au titre SCE et la difficulté d'une condition d'immatriculation après immatriculation est explicitée. Les seuils, délais et droits de renégociation ne sont pas réduits.",
    "Aucun changement propre du régime des sociétés européennes ni allègement de leurs procédures n'est proposé ; les textes réglementaires d'application restent à coordonner séparément.",
    "Aucune charge nouvelle identifiée : aucune seconde négociation ou immatriculation n'est exigée ; les cas, le seuil de 10 % et la faculté d'accord pour anticiper la reprise restent ceux des textes incorporés.",
    [effect(
        'coordination', 'sce-renegociation-renvois-propres',
        "Adaptation expresse des renvois internes de la société européenne au régime de la SCE.",
        "Renvoi à L. 2354-3 et L. 2354-4, qui utilisent les chapitres et les articles de la société européenne, dont une condition préalable d'immatriculation dans un régime postérieur.",
        "Même mécanisme avec chapitres II et III du titre SCE, décision L. 2362-7 et participation L. 2363-8 à L. 2363-10 ; pas de remise en cause de l'immatriculation déjà intervenue.",
        'other', 'SCE déjà immatriculées relevant des cas de réouverture ou de changement substantiel.',
        "Seuil de 10 %, deux ans sauf accord pour anticiper et cas de renégociation inchangés ; aucun délai en cours n'est recommencé.",
        "Aucune nouvelle formalité ni condition d'immatriculation additionnelle.",
        "Les articles L. 2354-3 et L. 2354-4 relatifs aux règles applicables postérieurement à l'immatriculation de la société européenne s'appliquent aux sociétés coopératives européennes.",
        "les références au chapitre II et au chapitre III s'entendent de références aux mêmes chapitres du présent titre.",
    )],
)

xml44 = "<p>Les représentants des salariés siégeant au sein de l'organe d'administration ou de surveillance, ou participant à l'assemblée générale ou aux assemblées de section ou de branche, " + confidentiality + "</p>"
rewritten(
    'L2364-4', xml44,
    "Coordination nécessaire : remplacement du renvoi à l'ancien L. 2325-5 par les qualifications explicites de secret de fabrication et de discrétion de L. 2315-3. Le cercle exact des représentants d'administration, de surveillance et des assemblées est conservé. Cette protection rend possible leur accès aux informations utiles ; elle n'est pas remplacée par une confidentialité indifférenciée. Aucune suppression de droit de vote ni de rémunération, aucun allègement matériel nouveau.",
    "L. 2315-3 a été lu intégralement et fournit les deux qualifications : procédés de fabrication ; informations ayant un caractère confidentiel et présentées comme telles par l'employeur. La version historique de L. 2325-5 n'est pas jointe au corpus courant. Coordination sous la même mesure que L. 2363-7, sans compter deux obligations supprimées. Les droits d'information, la rémunération de L. 2363-19 et la protection de L. 2364-5 restent intégraux. Les règles européennes de confidentialité restent à leur champ.",
    'coordination_only',
    "La proposition rend la confidentialité lisible et opérante sans renvoi à l'ancien article, avec le même cercle de représentants et les qualifications actuelles ; aucun gain matériel n'est compté.",
    "La concordance historique intégrale de L. 2325-5 n'est pas établie à partir du seul corpus courant ; aucun solde net de charge n'est affirmé.",
    "Aucune charge nouvelle identifiée : ni nouveau destinataire, ni attestation, ni registre ; la discrétion exige toujours à la fois un caractère confidentiel et sa présentation comme tel.",
    [effect(
        'coordination', 'sce-confidentialite-renvois',
        "Remplacement du renvoi obsolète par les deux catégories qualifiées de confidentialité.",
        "Les représentants des organes et assemblées sont soumis au secret et à la discrétion par renvoi à L. 2325-5.",
        "Les mêmes représentants sont soumis expressément au secret des procédés de fabrication et à la discrétion sur les informations confidentielles présentées comme telles.",
        'legal_duty', 'Représentants des salariés dans les organes et assemblées visés de la SCE.',
        "Maintien de la confidentialité pour les représentants actuels et futurs, sans suppression des obligations relatives aux informations déjà reçues.",
        "Aucune formalité ou engagement nouveau ; aucune extension à toute information de l'entreprise.",
        "sont tenus au secret professionnel et à l'obligation de discrétion prévus à l'article L. 2325-5.",
        confidentiality,
    )],
)

retained(
    'L2364-5',
    "Maintien intégral de la protection des représentants des salariés dans les conseils et assemblées. La protection du mandat contre le licenciement garantit l'indépendance de la participation et la non-discrimination ; elle ne constitue pas un agrément économique dispensable. La nouvelle faculté de rupture avec quinze jours calendaires de préavis ne supprime ni cette protection spéciale ni les autorisations distinctes. Elle reste ouverte aux futurs représentants éligibles.",
    "L. 2411-1 et L. 2411-12 ont été lus : la liste protège notamment les représentants des comités européens et L. 2411-12 exige l'autorisation de l'inspecteur du travail dans son propre champ. Les représentants d'administration ou d'assemblées visés par L. 2364-5 conservent leur protection ; la lecture de la seule liste ne doit pas servir à fermer leur droit exprès. Aucune extension du préavis individuel aux procédures collectives ou d'autorisation. Le cadre européen de protection des représentants reste distinct.",
    "La protection spéciale contre le licenciement est conservée pour les représentants actuels et futurs ; aucune suppression d'autorisation n'est revendiquée.",
    "Les procédures détaillées de licenciement des différentes catégories protégées ne sont pas toutes assignées ; aucun délai complet de quinze jours n'est promis.",
    "Aucune charge nouvelle identifiée : maintien du régime protecteur existant, sans autorisation supplémentaire ni nouvelle catégorie de contrôle créée ici.",
)

xml51 = (
    "<p>Le fait d'apporter une entrave soit à la constitution d'un groupe spécial de négociation ou d'un comité de la société coopérative européenne mis en place ou non par accord, soit à la libre désignation de leurs membres est puni d'une amende de 7 500 €.</p>"
    "<p>Le fait d'apporter une entrave à leur fonctionnement régulier est puni d'une amende de 7 500 €.</p>"
    "<p>La suppression de la peine d'emprisonnement s'applique aux faits commis à compter de l'entrée en vigueur de la loi qui la prévoit ainsi qu'aux faits antérieurs n'ayant pas donné lieu à une condamnation passée en force de chose jugée. Les condamnations définitives antérieures restent régies par les règles d'application de la loi pénale dans le temps. Les amendes, les actions civiles et les recours relatifs aux entraves demeurent régis par les règles qui leur sont applicables.</p>"
)
rewritten(
    'L2365-1', xml51,
    "Réduction de fond : suppression de la peine d'un an d'emprisonnement propre à l'entrave à la constitution ou à la libre désignation. Les deux incriminations demeurent complètes et conservent chacune leur amende de 7 500 €, ainsi que les actions civiles et recours. La sanction pécuniaire assure le maintien d'une sanction de l'entrave ; la prison n'est pas une condition nécessaire du fonctionnement représentatif démontrée par la source. Ce choix ne dépénalise ni les violences, ni les discriminations, ni les infractions ayant un fondement distinct. Il ne s'agit pas d'une taxe supprimée.",
    "Les deux alinéas ont été relus : l'emprisonnement n'existait que pour la constitution et la libre désignation, non pour le fonctionnement régulier. Aucun abaissement des deux amendes de 7 500 € ni restriction de l'infraction n'est décidé. La loi plus douce bénéficie expressément aux faits anciens non définitivement jugés ; les condamnations définitives restent soumises aux règles de droit pénal dans le temps, sans effacement général inventé. Hors des cinq codes, coordination à confronter avec les articles 112-1 et 112-4 du code pénal ; ces textes ne sont pas joints ni réécrits. La directive 2003/72/CE impose des mesures assurant l'effectivité des droits : l'adéquation de l'amende maintenue, des recours et de leur mise en œuvre reste à apprécier, sans présumer une validation européenne. Aucun effet budgétaire ou pénitentiaire national n'est chiffré.",
    'material_reduction',
    "Suppression démontrée de la peine d'un an d'emprisonnement pour l'entrave à la constitution ou à la libre désignation ; maintien des deux infractions et des amendes de 7 500 €. Aucun impôt ni devoir de représentation n'est supprimé.",
    "L'allègement ne touche pas les infractions distinctes, ne supprime pas les amendes et ne vaut pas effacement des condamnations définitives ; l'effectivité européenne de l'ensemble des recours n'est pas certifiée.",
    "Aucune charge nouvelle identifiée : les éléments des deux infractions et les recours demeurent ; aucune déclaration, sanction de remplacement ou taxe additionnelle n'est instituée. Le solde financier global reste inconnu.",
    [effect(
        'obligation_removed', 'sce-entrave-suppression-emprisonnement',
        "Retrait d'une sanction privative de liberté ; l'obligation de ne pas entraver la représentation demeure sanctionnée par l'amende.",
        "Entrave à la constitution ou à la libre désignation : un an d'emprisonnement et 7 500 € d'amende ; entrave au fonctionnement : 7 500 € d'amende.",
        "Deux infractions conservées, chacune punie de 7 500 € d'amende ; aucune peine d'emprisonnement sur ce seul fondement.",
        'other', 'Auteurs d' + "une entrave relevant de L. 2365-1, sans distinction nouvelle de statut ou d'effectif.",
        "Faits futurs et faits anciens non définitivement jugés pour la loi plus douce ; condamnations définitives et infractions autonomes selon leur droit propre.",
        "Aucune peine, formalité ni taxe de remplacement ; amendes et voies de recours existantes conservées.",
        "est puni d'un emprisonnement d'un an et d'une amende de 7 500 €.",
        "est puni d'une amende de 7 500 €.",
    )],
    ["La peine d'un an d'emprisonnement pour entrave à la constitution du groupe spécial ou du comité de SCE, ou à la libre désignation de leurs membres, est supprimée."],
)

retained(
    'L2371-1',
    "Maintien intégral des trois catégories territoriales et du renvoi définissant les opérations transfrontalières. Cet article délimite la protection de participation ; il ne crée par lui-même ni taxe, ni autorisation, ni déclaration autonome à supprimer. Réduire sa portée ferait perdre les droits des salariés de sociétés françaises participantes ou issues de l'opération et des filiales françaises de sociétés européennes. Les fusions, scissions, transformations et apports partiels d'actifs sont tous conservés, pour les opérations futures également.",
    "Les trois subdivisions et le dernier alinéa sont conservés. La source contient la coquille « de la l'Union européenne » ; aucune réécriture purement stylistique n'est produite pour la corriger. L. 2371-2 et L. 2371-3 ont été lus : dispense en l'absence de participation pour la fusion dans son champ propre, accord et faculté de règles subsidiaires sans négociation préalable pour certaines fusions. Ne pas étendre ces exceptions aux autres opérations sans fondement. Le renvoi à la section 4 du chapitre VI du titre III du livre II du code de commerce reste à confronter hors corpus, ce code n'étant pas fourni. Cadre européen identifié : directive (UE) 2017/1132 modifiée notamment par la directive (UE) 2019/2121 ; aucune modification de ce cadre n'est réputée accomplie.",
    "Maintien du périmètre territorial et matériel des droits de participation transfrontalière ; aucune procédure nouvelle ni réduction matérielle n'est comptée.",
    "Les textes commerciaux et européens intégraux ne sont pas joints ; aucun contrôle exhaustif des opérations de commerce ni des législations étrangères n'est affirmé.",
    "Aucune charge nouvelle identifiée : mêmes catégories d'opérations et de sociétés, aucun agrément, déclaration ou délai additionnel introduit par cet article de champ.",
)


assert set(answers) == set(by_number), (set(by_number) - set(answers))
Path('answer.json').write_text(
    json.dumps([answers[s['number']] for s in sources], ensure_ascii=False, indent=2)
    + '\n'
)
