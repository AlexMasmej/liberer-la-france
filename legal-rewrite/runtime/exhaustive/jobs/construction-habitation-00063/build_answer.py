import json
from pathlib import Path


ROOT = Path(__file__).parent
sources = json.loads((ROOT / 'source.json').read_text())
references = json.loads((ROOT / 'reference-targets.json').read_text())
answers = []


def impact(classification, assessment, limitations, burdens, effects=None):
    return {
        'version': 1,
        'classification': classification,
        'assessment': assessment,
        'scope_limitations': limitations,
        'new_burdens_review': burdens,
        'effects': effects or [],
    }


def effect(kind, measure, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure, description=description,
                before=before, after=after, unit=unit,
                affected_population=population,
                conditions_and_transition=transition,
                replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


def base(number):
    source = next(a for a in sources if a['number'] == number)
    a = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    a['reference_checks'] = []
    answers.append(a)
    return a


def retain(number, reason, notes, assessment, limitations, benefits):
    a = base(number)
    a.update(proposed_xml=None, reason=reason, review_notes=notes,
             status='retained_unchanged', classification='retained_necessary',
             benefit_review=benefits,
             substantive_impact=impact(
                 'retained_necessary', assessment, limitations,
                 "Aucune charge nouvelle n'est identifiée : le texte officiel est maintenu intégralement, sans nouveau formulaire, registre, délai, condition ni procédure de remplacement."))
    return a


fnal_measure = 'contribution-allocation-logement-sociale-suppression'
fnal_date = "l'entrée en vigueur de la loi supprimant la contribution relative à l'allocation de logement sociale"
old_rule = (
    "Les dispositions du présent article dans leur rédaction antérieure demeurent applicables aux revenus d'activité afférents aux périodes d'activité antérieures à cette date, y compris lorsque leur liquidation, leur paiement, leur recouvrement ou leur régularisation intervient après cette date. "
    "Les exonérations, réductions, dispenses, remises, imputations, restitutions, prescriptions, garanties et voies de recours applicables à ces revenus sont conservées. "
    "Il n'est institué ni restitution générale des sommes légalement dues ni double imputation ou double remboursement."
)
common_fnal_notes = (
    "Mesure unique dédupliquée sous contribution-allocation-logement-sociale-suppression ; L813-4 supprime le prélèvement, L813-5 à L813-12 en retirent le tarif et les modalités pour les périodes nouvelles. "
    "La coupure repose sur la période d'activité, non sur la date d'encaissement : une régularisation tardive de périodes anciennes conserve son régime. "
    "Les revenus afférents à une période chevauchant l'entrée en vigueur sont répartis entre les deux périodes ; pas de suppression des autres cotisations. "
    "Les coordinations non rédigées dans ce lot concernent CCH L861-1 à L861-3, L862-1, L863-1, CSS L213-1 I 4°, L241-13 I/III/VII, L243-1-3 1°, D241-7 III/VI et D711-8 II, ainsi que les nomenclatures et rubriques exclusivement FNAL des déclarations sociales. "
    "CSS L241-10 III et D311-2 visent encore l'ancien L834-1 : concordance historique à établir, sans leur attribuer un nouveau contenu par hypothèse. "
    "Les réductions sur les prélèvements maintenus, notamment l'aide à domicile et la réduction générale, restent ouvertes aux situations futures éligibles ; aucune fraction FNAL fictive n'est remboursable. "
    "Les coefficients et imputations devront être coordonnés sans diminuer, du seul fait de la suppression, les avantages portant sur les prélèvements maintenus. "
    "La perte de recettes et l'articulation des affectations sociales avec la garantie d'équilibre de CCH L813-3 restent à documenter dans les lois financières ; aucune recette de remplacement ni économie nationale n'est présumée. "
    "Le code rural, les textes ultramarins extérieurs et les formulaires ne sont pas présentés comme réécrits."
)


# L812-1 : retrait d'une transmission nominative de pilotage et limitation du flux de contrôle.
a = base('L812-1')
a['proposed_xml'] = """<p>Les aides personnelles au logement et les primes de déménagement sont liquidées et payées, pour le compte du fonds national d'aide au logement et selon ses directives, par les organismes chargés de gérer les prestations familiales.</p>
<p>Ces organismes transmettent au fonds :</p>
<p>1° Les seules données nécessaires au contrôle de la liquidation et du paiement de ces aides et primes ainsi qu'à la justification de l'emploi des fonds ;</p>
<p>2° Abrogé.</p>
<p>La nature de ces informations ainsi que leurs modalités de transmission et d'utilisation sont fixées par voie réglementaire dans les conditions prévues au paragraphe 4 de l'article 36 du règlement (UE) 2016/679 du Parlement européen et du Conseil en date du 27 avril 2016 relatif à la protection des personnes physiques à l'égard du traitement des données à caractère personnel et à la libre circulation de ces données, et abrogeant la directive 95/46/ CE (règlement général sur la protection des données).</p>
<p>L'article 226-13 du code pénal n'est pas applicable aux personnes qui transmettent des informations confidentielles dans les conditions et aux fins prévues au présent article.</p>
<p>Aucune transmission d'informations permettant l'identification directe ou indirecte des bénéficiaires ne peut être exigée au seul titre du suivi, du pilotage ou de l'évaluation de ces aides et primes. Ces finalités sont assurées au moyen des informations agrégées déjà légalement disponibles, sans nouveau relevé ni traitement statistique supplémentaire imposé aux organismes payeurs sur le fondement du présent article.</p>
<p>La limitation des transmissions s'applique à compter de l'entrée en vigueur de la loi limitant les transmissions prévues au présent article, y compris pour les données relatives à des périodes antérieures. Les directives et conventions ne peuvent imposer les transmissions ainsi supprimées. Les contrôles de la régularité des prestations et de l'emploi des fonds restent applicables. Les données déjà transmises demeurent soumises aux règles de protection des données à caractère personnel.</p>"""
a.update(
    reason="Réforme de fond : retrait du flux individuel de suivi, pilotage et évaluation du 2°, et de l'exhaustivité systématique du 1°. Le flux de contrôle est limité aux données nécessaires à la régularité des paiements et à l'emploi des fonds. Les missions de liquidation et de paiement, le contrôle des fonds, la consultation prévue par le RGPD et l'encadrement du secret demeurent. Il ne s'agit pas d'une reformulation à droit constant.",
    review_notes="Les 1° et 2° conservent leur place ; le 2° est expressément abrogé. Les restitutions financières agrégées de R813-4 et R813-6, lues en entier, permettent le suivi budgétaire sans nouveau reporting nominatif. Les directives de R812-1 et les conventions de L812-2/L812-3 doivent respecter la limitation nouvelle ; leur objet financier et les contrôles autonomes subsistent. Les dispositions réglementaires fixant les catégories détaillées de données au titre de L812-1 restent à inventorier et à coordonner ; aucun dispositif d'accès à de nouvelles données n'est créé. Le renvoi au paragraphe 4 de l'article 36 du RGPD et celui à l'article 226-13 du code pénal sont conservés à leur objet, sans prétendre avoir réécrit ces textes. Ni anonymisation nouvelle obligatoire ni suppression d'une transmission nécessaire à un contrôle légal autonome. Coût net technique et public non chiffré.",
    status='rewrite_draft', change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=[
        "Transmission systématique de l'ensemble des données de liquidation et de paiement, même sans nécessité pour le contrôle des fonds.",
        "Transmission d'informations identifiant les bénéficiaires pour les seules finalités de suivi, de pilotage et d'évaluation, sans reporting de remplacement."
    ],
    benefit_review="La liquidation et le paiement des aides personnelles et primes de déménagement restent assurés aux bénéficiaires actuels et futurs. La réforme ne restreint aucun droit à prestation, exonération ou recours ; elle réduit seulement les données exigibles par le fonds, tout en gardant les contrôles nécessaires.",
    substantive_impact=impact(
        'material_reduction',
        "Par rapport à la source entière, le fonds ne reçoit plus par principe toutes les données disponibles ni un flux nominatif destiné au pilotage. Les données de contrôle et l'organisation du paiement sont maintenues ; le 2° ne peut être rétabli par convention ou directive.",
        "La mesure porte sur les seuls flux vers le fonds fondés sur L812-1 ; elle ne retire pas les contrôles légalement autonomes ni les obligations des allocataires. Les catégories réglementaires de données sont encore à coordonner ; aucun solde global de complexité ou de coût n'est établi.",
        "Aucune charge nouvelle n'est identifiée : le pilotage utilise les informations agrégées déjà disponibles sans relevé, calcul statistique, registre, donnée ou déclaration de remplacement. L'adaptation ponctuelle des flux informatiques reste à évaluer.",
        [effect(
            'obligation_removed', 'fnal-limitation-transmissions-beneficiaires',
            "Suppression du reporting nominatif de pilotage et de l'exigence de transmission exhaustive des données disponibles.",
            "Les organismes payeurs transmettent toutes les données de liquidation/paiement et les informations relatives aux bénéficiaires pour le suivi, le pilotage et l'évaluation, sans limitation expresse de nécessité dans l'article.",
            "Seules les données nécessaires au contrôle des paiements et des fonds restent transmissibles ; aucune donnée identifiante n'est exigible pour le seul pilotage, dont les besoins sont satisfaits par les agrégats déjà disponibles.",
            'legal_duty', "Organismes payeurs des aides personnelles au logement et des primes de déménagement ; bénéficiaires dont les données sont concernées.",
            "Toutes transmissions à compter de l'entrée en vigueur, y compris concernant des périodes anciennes ; protection des données déjà transmises conservée.",
            "Aucun relevé, traitement statistique imposé ou flux de remplacement ; maintien des contrôles autonomes et des paiements.",
            "2° Les informations relatives à leurs bénéficiaires permettant à l'Etat d'exercer sa compétence de suivi, de pilotage et d'évaluation de ces aides et primes.",
            "Aucune transmission d'informations permettant l'identification directe ou indirecte des bénéficiaires ne peut être exigée au seul titre du suivi, du pilotage ou de l'évaluation de ces aides et primes."
        )])
)


retain('L812-2',
       "Maintien intégral nécessaire : les conventions nationales organisent la mise à disposition des fonds, le paiement par les caisses et le remboursement de leurs frais. Ce financement et la solution réglementaire en l'absence d'accord empêchent un blocage du service des aides. L'article ne crée ni prélèvement employeur ni dossier supplémentaire pour un allocataire ; supprimer ces garanties ne démontre pas un allègement utile.",
       "L812-1 limite désormais le contenu transmissible, et L812-3 retire le second accord préalable pour les adaptations locales : les conventions ne peuvent rétablir ces charges. L832-1 concerne le versement de l'APL au bailleur, établissement ou gestionnaire, avec exceptions ; L842-1 concerne le tiers payant de l'allocation et les déductions/reversements. Ces deux sources et leurs propositions courantes ont été lues ; le mécanisme de demande expresse déjà proposé à L842-1 ne doit pas être annulé par les modalités techniques. Aucun renvoi au contrat unique n'est nécessaire.",
       "Les conventions, le financement des caisses et le remboursement des frais sont maintenus sans nouvelle rédaction. Leur existence assure le versement effectif des prestations ; aucune simplification ou économie nouvelle n'est comptée pour cet article.",
       "Le maintien ne valide pas chaque stipulation des conventions nationales, qui ne sont pas jointes. Les frais effectifs et les gains des autres articles ne sont pas chiffrés ici.",
       "Le financement du service des aides et des primes reste garanti pour les futurs bénéficiaires éligibles. La faculté de conclure les conventions et le remboursement des frais demeurent ; aucune aide ni dispense n'est retirée.")


a = base('L812-3')
a['proposed_xml'] = """<p>Les dispositions de ces conventions nationales s'imposent aux organismes mentionnés à l'article L. 812-1. Toutefois, des adaptations peuvent leur être apportées en vertu d'accords particuliers conclus entre l'Etat et ces organismes.</p>
<p>Aucun accord préalable distinct de la caisse nationale ou centrale dont relève l'organisme n'est requis pour ces adaptations. Cette suppression s'applique aux accords particuliers conclus à compter de l'entrée en vigueur de la loi supprimant cet accord préalable, y compris lorsque leur préparation a commencé avant cette date, sans nouveau dépôt. Les accords particuliers antérieurs demeurent valables.</p>"""
a.update(
    reason="Réforme de fond : suppression de l'accord préalable de la caisse nationale ou centrale, qui s'ajoutait à l'accord particulier entre l'Etat et l'organisme et à la convention nationale. Les deux parties à l'adaptation restent responsables de son contenu ; l'opposabilité de la convention nationale et la faculté d'adaptation sont conservées.",
    review_notes="Le consentement de l'Etat et de l'organisme à l'accord particulier demeure ; seul le second accord administratif est retiré, sans déclaration, visa ou délai d'opposition de remplacement. Les conventions de L812-2 et directives ne peuvent rétablir cette condition supprimée. Les compétences et contrôles légaux autonomes des caisses subsistent, sans pouvoir valoir un nouveau veto sur ce seul fondement. Les accords antérieurs ne sont ni annulés ni à déposer de nouveau. L'encadrement des données de L812-1 reste opposable.",
    status='rewrite_draft', change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=["Accord préalable de la caisse nationale ou centrale pour chaque adaptation convenue entre l'Etat et l'organisme payeur dans un accord particulier."],
    benefit_review="La possibilité favorable d'adapter une convention nationale par accord particulier demeure ouverte aux organismes pour les situations futures, avec moins de conditions. Les accords déjà conclus et les droits des bénéficiaires des aides restent protégés ; aucune prestation n'est diminuée.",
    substantive_impact=impact(
        'material_reduction',
        "La source impose trois consentements pour une adaptation : Etat, organisme et caisse nationale ou centrale. La proposition supprime le troisième, sans procédure équivalente ; elle conserve le cadre national et la faculté d'adaptation.",
        "La réduction ne concerne que l'accord de la caisse sur les adaptations de L812-3. Elle n'abolit ni la convention nationale, ni les contrôles comptables, ni les compétences légales autonomes ; le temps et le coût gagnés ne sont pas mesurés.",
        "Aucune charge nouvelle n'est identifiée : pas de déclaration, registre, document supplémentaire, délai minimal ou autorisation de remplacement. Les accords en préparation se poursuivent sans nouveau dépôt.",
        [effect('authorization_removed', 'fnal-adaptations-fin-accord-caisse',
                "Suppression du second accord préalable sur les adaptations des conventions de paiement.",
                "L'accord particulier Etat-organisme suppose en plus l'accord de la caisse nationale ou centrale de rattachement.",
                "L'accord particulier Etat-organisme suffit pour adapter la convention, sans accord distinct de la caisse.",
                'legal_duty', "Etat et organismes payeurs relevant de la CNAF ou de la CCMSA.",
                "Accords particuliers conclus après l'entrée en vigueur ; préparations en cours couvertes ; accords antérieurs valables.",
                "Aucun visa, déclaration ni délai de remplacement ; convention nationale et contrôles autonomes conservés.",
                "après accord de la caisse, nationale ou centrale, dont ils relèvent.",
                "Aucun accord préalable distinct de la caisse nationale ou centrale dont relève l'organisme n'est requis pour ces adaptations.")])
)


retain('L813-1',
       "Maintien nécessaire de la liste des ressources du fonds : contribution de l'Etat, revenus de placement et recettes déjà autorisées par d'autres textes. Ce texte n'institue aucun prélèvement et ne permet pas au fonds d'en créer un. Le maintien de ces ressources soutient les aides sans convertir la contribution employeur supprimée en une autre taxe.",
       "Les numéros 1°, 5° et 6° sont conservés exactement ; les 2° à 4° ne sont pas réintroduits. Incohérence préexistante constatée après lecture de R813-5 : son 2° renvoie au 2° de L813-1, absent de la source actuelle, et son 1° à l'état prévisionnel de R813-3 alors que R813-4 contient cet état. Ces renvois réglementaires restent à coordonner, sans modifier silencieusement la présente liste. Le 6° ne constitue pas un fondement autonome de perception de la contribution supprimée par L813-4. La destination actuelle de son produit et la perte de recettes sociales restent à établir, sans compensation fiscale inventée.",
       "La contribution de l'Etat et les ressources non fiscales sont maintenues ; aucune taxe n'est supprimée par ce seul article, qui ne comporte pas de fait générateur ni de tarif de contribution employeur.",
       "Les autorisations de recettes extérieures à l'article ne sont pas toutes auditées ; le budget et les affectations ne sont pas chiffrés. Les incohérences de R813-5 sont signalées sans présenter leur correction comme déjà rédigée.",
       "La conservation des ressources légales protège le financement des aides présentes et futures. Aucun avantage fiscal n'est supprimé, et les anciennes rubriques de recettes abrogées ne sont pas restaurées.")

retain('L813-2',
       "Maintien intégral nécessaire : la liste autorise les dépenses de prestations, de gestion, de recouvrement résiduel et de procédure du fonds. Elle ne crée ni taxe ni nouvelle formalité pour un ménage. Retirer la capacité de payer les aides ou les frais de leur service compromettrait les prestations sans démontrer la disparition d'un doublon.",
       "L811-1, lu dans le corpus public, renvoie aux aides et primes définies à L821-1 et en attribue le financement au fonds : le renvoi du 1° est indirect mais cohérent. Le 3° continue de couvrir les frais des recettes légales et du recouvrement ancien ; il n'autorise aucun nouveau prélèvement FNAL ni aucune pénalité future sur une contribution supprimée. Le 7° n'est pas une habilitation à imposer une cotisation nouvelle.",
       "La totalité des sept catégories de dépenses est maintenue, notamment les prestations et les frais qui permettent leur paiement. L'article n'impose pas de démarche privée à supprimer et ne réalise pas lui-même de baisse de dépense.",
       "Le maintien ne démontre pas l'efficience de chaque dépense diverse ni l'absence de doublon dans les budgets exécutés. Les coûts et la coordination des recettes supprimées restent distincts.",
       "Les dépenses de prestations et primes de déménagement restent autorisées sans réserver leur paiement aux droits anciens. Les frais nécessaires au service de ces avantages peuvent toujours être financés ; aucune exonération n'est retirée.")

retain('L813-3',
       "Maintien intégral de la garantie d'équilibre par l'Etat : elle protège la continuité du financement des aides malgré la suppression proposée du prélèvement employeur. Cet engagement public n'est ni une taxe sur les bénéficiaires ni un dossier supplémentaire ; son retrait déplacerait le risque vers les caisses ou les allocataires.",
       "Aucune recette nouvelle ni montant de compensation n'est ajouté. La garantie concerne le fonds, tandis que l'affectation actuelle du produit de la contribution employeur et les incidences sur les organismes sociaux nécessitent un examen financier distinct. Les lois de finances et de financement de la sécurité sociale devront traiter les effets documentés ; aucune suffisance budgétaire ou économie automatique n'est affirmée.",
       "La garantie financière existante reste inchangée. Elle ne diminue pas un prélèvement et n'est pas comptée comme un effet matériel de la suppression FNAL.",
       "Le coût de la garantie et les besoins consolidés après suppression de recettes restent inconnus. Le présent article ne vote pas les crédits ni une compensation aux branches sociales.",
       "L'équilibre assuré par l'Etat soutient la continuité des aides au logement pour les bénéficiaires actuels comme pour les futures situations éligibles. Aucun impôt, avantage fiscal ou droit à aide n'est modifié par ce maintien.")


# L813-4 à L813-12 : une seule suppression de contribution, neuf articles coordonnés.
a = base('L813-4')
a['proposed_xml'] = f"""<p>Le présent article est abrogé pour les revenus d'activité afférents aux périodes d'activité courant à compter de {fnal_date}.</p>
<p>Aucune contribution relative à l'allocation de logement sociale n'est due sur ces revenus, quel que soit l'effectif de l'employeur, son activité, le régime de sécurité sociale de ses salariés ou le territoire dans lequel cette contribution était applicable. Aucun prélèvement équivalent ne lui est substitué sur le fondement du présent article.</p>
<p>Pour une période d'activité comprenant cette date, la contribution ne demeure applicable qu'aux revenus afférents à la partie antérieure de cette période.</p>
<p>{old_rule}</p>
<p>Pour les revenus exclus de la contribution, aucune déclaration, donnée, liquidation, échéance, majoration ou formalité exclusivement liée à cette contribution ne peut être exigée, y compris au titre des adaptations territoriales de son recouvrement et des versements libératoires propres aux caisses de congés payés. Les obligations communes nécessaires à d'autres prélèvements demeurent applicables, sans dépôt distinct au seul titre de la contribution supprimée.</p>
<p>La suppression n'affecte ni les droits aux aides personnelles au logement et aux primes de déménagement, ni les exonérations, réductions ou dispenses applicables aux autres cotisations et contributions, y compris pour les situations futures éligibles. L'extinction de la seule fraction d'un avantage imputable à la contribution supprimée ne peut, à elle seule, diminuer les fractions de cet avantage portant sur les prélèvements maintenus. Elle ne crée aucune créance correspondant à une contribution fictive.</p>"""
a.update(
    reason="Réforme de fond : suppression complète et prospective de la contribution employeur d'allocation de logement sociale, prélèvement sur la masse salariale distinct des droits des ménages. Sa fonction de recette ne justifie pas son maintien dans l'orientation de baisse des prélèvements ; les aides demeurent et leur financement public doit être traité explicitement, sans taxe de remplacement. Les créances anciennes et leurs avantages restent régis par le droit antérieur.",
    review_notes=common_fnal_notes + " Les textes territoriaux lus adaptent le recouvrement et, à Mayotte, le plafond ; ils ne peuvent faire renaître la contribution pour les périodes nouvelles. L861-1 vise aussi les non-salariés agricoles, décalage préexistant avec la rédaction employeur de L813-4 : ne pas étendre leur assiette par interprétation ; l'extinction couvre la seule contribution ainsi désignée dans son champ légal existant.",
    status='rewrite_draft', change_type='full_repeal',
    repeal_policy_id='editorial_direction_2026_10_19',
    repeal_scope="Suppression pour les périodes d'activité nouvelles de toute contribution employeur relative à l'allocation de logement sociale, de ses adaptations territoriales et des formalités exclusivement nécessaires à sa perception ; maintien du régime des périodes anciennes.",
    benefit_review="La contribution entière disparaît pour les périodes nouvelles, y compris là où des taux, plafonds, exonérations ou réductions étaient plus favorables. Ces avantages demeurent pour les périodes anciennes. Les exonérations portant sur d'autres prélèvements et les aides au logement restent ouvertes aux situations futures ; aucune contribution de remplacement ni assiette élargie n'est créée.",
    substantive_impact=impact(
        'material_reduction',
        "Le fait générateur employeur est supprimé pour les périodes nouvelles : la contribution auparavant tarifée à 0,1 % sur revenus plafonnés ou 0,5 % sur revenus déplafonnés n'est plus due. Les huit articles d'exécution du lot ne sont pas huit suppressions supplémentaires. Les droits à aide restent autonomes.",
        "Le gain effectif dépend des exonérations et réductions antérieures ; il n'est pas automatiquement égal à la contribution brute, notamment si elle était déjà neutralisée. Les coefficients sociaux, affectations, textes ruraux et formulaires nécessitent des coordinations identifiées. La perte de recettes et le solde public consolidé ne sont pas chiffrés.",
        "Aucune charge nouvelle n'est identifiée : pas de déclaration, registre, justificatif, prélèvement ou financement compensatoire imposé. Les formalités communes et les régularisations anciennes demeurent. Les adaptations ponctuelles de paie et de recouvrement ne sont pas chiffrées.",
        [effect('tax_removed', fnal_measure,
                "Abolition de la contribution employeur d'allocation de logement sociale pour les périodes d'activité nouvelles.",
                "Tout employeur de salariés agricoles ou non agricoles : 0,1 % de l'assiette des cotisations patronales maladie dans la limite du plafond vieillesse pour les moins de cinquante salariés et les catégories agricoles/cooperatives de L813-5 1° ; 0,5 % de la même assiette sans plafond pour les autres, sous exonérations et réductions applicables.",
                "Aucune contribution d'allocation de logement sociale sur les revenus des périodes nouvelles ; aucun taux ni assiette de remplacement ; les autres prélèvements et leurs avantages demeurent distincts.",
                'percent', "Employeurs assujettis dans le champ agricole, non agricole, général, spécial et territorial de la contribution existante.",
                "Périodes d'activité à compter de l'entrée en vigueur de la loi de suppression ; partage de la période chevauchante ; droit antérieur pour les périodes anciennes, même payées ou régularisées ultérieurement.",
                "Aucun prélèvement ni formulaire de remplacement ; maintien des données communes nécessaires aux autres cotisations et des dettes anciennes avec leurs garanties.",
                "La contribution relative à l'allocation de logement sociale mentionnée au b du 2° de l'article L. 821-1 est due par toute personne physique ou morale employant un ou plusieurs salariés relevant soit des professions non agricoles, soit des professions agricoles.",
                "Aucune contribution relative à l'allocation de logement sociale n'est due sur ces revenus, quel que soit l'effectif de l'employeur, son activité, le régime de sécurité sociale de ses salariés ou le territoire dans lequel cette contribution était applicable.")])
)


execution = {
    'L813-5': (
        "le tarif de 0,1 % sur revenus plafonnés et de 0,5 % sur revenus déplafonnés",
        "Le barème n'est plus applicable aux revenus exclus de la contribution par l'article L. 813-4.",
        "Les deux taux et assiettes disparaissent pour les périodes nouvelles, y compris la distinction d'effectif et les catégories agricoles favorables ; le barème ancien reste applicable aux périodes anciennes avec son plafond et ses avantages.",
        "2° Pour les autres employeurs, par application d'un taux de 0,5 % sur les revenus d'activité tels qu'ils sont pris en compte pour la détermination de l'assiette des cotisations patronales d'assurance maladie affectées au financement des régimes de base de l'assurance maladie.",
        "Barème : 0,1 % sur l'assiette patronale maladie plafonnée pour les catégories du 1°, 0,5 % sur toute cette assiette pour les autres employeurs, avec exonérations/réductions applicables.",
        "Aucun barème FNAL pour les revenus des périodes nouvelles ; barème et plafond maintenus exclusivement pour les périodes anciennes.",
        "Le renvoi au premier alinéa de CSS L241-3 est un renvoi de plafond, pas un renvoi au contrat privé ni une incorporation du volet de capitalisation proposé. L130-1, lu, porte les règles d'effectif et de franchissement favorables : elles restent pertinentes pour les anciennes périodes, sans conditionner l'extinction future."
    ),
    'L813-6': (
        "l'attribution du recouvrement courant de la contribution aux organismes sociaux ou agricoles",
        "Aucun organisme de recouvrement ne peut appeler cette contribution au titre des revenus exclus par l'article L. 813-4.",
        "La compétence de recouvrement n'a plus d'objet pour les périodes nouvelles ; elle reste applicable aux créances anciennes. La dérogation de L813-8 reste uniquement pertinente pour ce stock ancien.",
        "La contribution est, sous réserve des dispositions de l'article L. 813-8, recouvrée par les organismes chargés du recouvrement des cotisations de sécurité sociale ou d'assurances sociales agricoles.",
        "Recouvrement de la contribution par les organismes sociaux ou agricoles, sous réserve des régimes spéciaux.",
        "Aucun appel FNAL pour les revenus nouveaux ; compétence ancienne conservée pour liquider, recouvrer ou restituer les créances anciennes.",
        "CSS L213-1 I 4°, lu intégralement, conserve un renvoi d'attribution à coordonner avec cette extinction ; le retrait de ce seul renvoi n'abolit aucune autre contribution recouvrée par l'Urssaf."
    ),
    'L813-7': (
        "l'application des règles des cotisations du régime général à la contribution future",
        "Les règles de liquidation, de paiement, de recouvrement, de contrôle et de contentieux ne peuvent être appliquées à une contribution qui n'est plus due sur les revenus exclus par l'article L. 813-4.",
        "Le renvoi procédural au régime général cesse de fonder des appels nouveaux ; les cinq opérations et garanties demeurent pour les périodes anciennes. Les cotisations du régime général ne sont pas abrogées.",
        "aux règles applicables aux cotisations de sécurité sociale pour la liquidation, le paiement, le recouvrement, le contrôle et le contentieux de cette contribution.",
        "Employeurs du régime général soumis pour le FNAL aux règles de liquidation, paiement, recouvrement, contrôle et contentieux des cotisations.",
        "Aucune procédure FNAL pour les revenus exclus ; procédures et recours antérieurs conservés pour les seules périodes anciennes.",
        "L813-8 et l'adaptation mahoraise de L861-3, lues, doivent être limités au même stock ancien. Les garanties du cotisant et le contentieux des autres prélèvements restent applicables."
    ),
    'L813-8': (
        "les deux circuits de recouvrement FNAL des régimes spéciaux pour les périodes nouvelles",
        "Aucun des organismes mentionnés aux 1° et 2° dans la rédaction antérieure ne peut appeler la contribution au titre des revenus exclus par l'article L. 813-4.",
        "Les deux circuits, Urssaf déjà chargée d'une part patronale ou organisme maladie du régime spécial, cessent pour les périodes nouvelles. Leur compétence et leurs règles restent conservées pour les créances anciennes, sans toucher au régime spécial lui-même.",
        "2° Dans les autres cas, l'organisme chargé du recouvrement de la cotisation patronale affectée à l'assurance maladie du régime spécial auquel sont assujettis les salariés intéressés, assure également celui de la contribution relative à l'allocation de logement sociale.",
        "Deux circuits FNAL selon l'organisme déjà chargé d'une cotisation patronale ; procédures du régime général ou de l'assurance maladie spéciale.",
        "Aucun circuit d'appel pour les revenus nouveaux ; les deux branches de compétence restent utilisables pour les créances anciennes.",
        "Le renvoi à CSS L711-1 délimite des régimes de sécurité sociale et ne transforme pas leurs agents en titulaires du contrat unique. Aucune règle d'emploi public, cotisation maladie ou protection spéciale n'est supprimée."
    ),
    'L813-9': (
        "le renvoi au recouvrement agricole de la contribution future",
        "Les caisses de mutualité sociale agricole ne peuvent appeler cette contribution au titre des revenus exclus par l'article L. 813-4.",
        "Le volet agricole est supprimé au même rythme que le volet non agricole. Les règles agricoles de liquidation, paiement, recouvrement, contrôle et contentieux demeurent pour les périodes anciennes et les autres cotisations.",
        "aux règles applicables aux cotisations d'assurances sociales agricoles, pour la liquidation, le paiement, le recouvrement, le contrôle et le contentieux de cette contribution.",
        "Les employeurs agricoles versent la contribution sous les règles des assurances sociales agricoles à la MSA.",
        "Aucun FNAL sur les revenus des périodes nouvelles ; recouvrement, restitutions et recours conservés pour les anciennes périodes agricoles.",
        "Les références agricoles de L813-5 1° restent conservées par le droit ancien. Les coordinations du code rural, hors du lot et des cinq codes, sont à identifier dans leur texte complet ; aucune prétendue réécriture de ce code."
    ),
    'L813-10': (
        "l'exigibilité et les majorations de retard propres à la contribution sur les périodes nouvelles",
        "Aucune mise en recouvrement, exigibilité ou majoration de retard ne peut être fondée sur une contribution supprimée au titre des revenus exclus par l'article L. 813-4.",
        "Les échéances et majorations accessoires disparaissent avec le principal pour les périodes nouvelles. La faculté favorable de remise et toutes les garanties restent disponibles pour les créances anciennes, même si la remise est demandée après la réforme.",
        "Ces majorations peuvent faire l'objet d'une remise dans les mêmes conditions que celles qui s'appliquent aux cotisations de sécurité sociale ou d'assurances sociales agricoles.",
        "Même échéance que les cotisations sociales, majorations de retard en cas d'impayé et faculté de remise selon le régime social applicable.",
        "Aucune échéance ou majoration FNAL sur les revenus nouveaux ; échéances, remises, garanties et voies de recours anciennes maintenues.",
        "Ne pas confondre la suppression des accessoires d'un principal aboli avec celle des majorations sur d'autres cotisations. La remise n'est pas fermée aux demandes futures portant sur les créances anciennes ; aucun remboursement général ni amnistie non décidé."
    ),
    'L813-11': (
        "l'attribution du contentieux du recouvrement d'une contribution nouvelle supprimée",
        "Aucune procédure contentieuse de recouvrement ne peut avoir pour objet une contribution qui n'est plus due sur les revenus exclus par l'article L. 813-4.",
        "L'attribution procédurale demeure pour les contestations de créances anciennes, sans extinction d'action ni suppression du recours au juge. Elle ne peut servir de base à une contribution nouvelle.",
        "Le contentieux du recouvrement de la contribution relative à l'allocation de logement sociale est de la compétence des organismes chargés du recouvrement des cotisations de sécurité sociale ou d'assurances sociales agricoles.",
        "Compétence des organismes de recouvrement pour le contentieux de la contribution, sans distinction temporelle dans la source.",
        "Compétence conservée pour le stock ancien ; aucun recouvrement contentieux d'un FNAL inexistant pour les périodes nouvelles.",
        "La formule source de compétence des organismes est maintenue par la clause de droit ancien sans l'interpréter comme une suppression de compétence juridictionnelle. Les voies de recours et délais anciens restent ouverts dans leurs conditions."
    ),
    'L813-12': (
        "l'imputation de paiements partiels sur une contribution future supprimée",
        "Aucune part d'un versement ne peut être affectée à une contribution qui n'est plus due sur les revenus exclus par l'article L. 813-4.",
        "La priorité d'affectation subsiste pour les véritables dettes anciennes, mais aucun paiement partiel ne peut reconstituer un FNAL nouveau. L'ordre général des paiements sociaux n'est pas supprimé.",
        "s'effectue selon les règles de priorité prévues à l'article L. 133-4-11 du code de la sécurité sociale.",
        "Les versements insuffisants du redevable FNAL suivent les priorités de CSS L133-4-11.",
        "Aucune affectation à une dette FNAL nouvelle inexistante ; ordre d'imputation antérieur pour les seules dettes anciennes réellement dues.",
        "CSS L133-4-11, lu intégralement, donne priorité au principal puis aux accessoires et, pour les employeurs, aux cotisations salariales. Ces priorités favorables sur les dettes réelles restent intactes ; aucune créance fictive ni nouvelle priorité n'est créée."
    ),
}

for number, (scope, operative, assessment, quote, before, after, notes) in execution.items():
    a = base(number)
    a['proposed_xml'] = (
        f"<p>Le présent article est abrogé pour les revenus d'activité afférents aux périodes d'activité courant à compter de {fnal_date}.</p>\n"
        f"<p>{operative}</p>\n<p>{old_rule}</p>"
    )
    a.update(
        reason=f"Coordination nécessaire de la réforme de fond de L813-4 : retrait pour l'avenir de {scope}. " + assessment + " Il ne s'agit pas d'une seconde suppression de taxe ni d'une simple reformulation.",
        review_notes=notes + ' ' + common_fnal_notes,
        status='rewrite_draft', change_type='full_repeal',
        repeal_policy_id='editorial_direction_2026_10_19',
        repeal_scope=f"Suppression prospective de {scope}, exclusivement pour les revenus des périodes nouvelles ; maintien des droits, avantages et procédures des périodes anciennes.",
        benefit_review="Les avantages attachés à la contribution, notamment les exonérations, plafonds, réductions, dispenses et remises applicables, restent utilisables pour les périodes anciennes, y compris sur demande ultérieure. Pour les périodes nouvelles, le principal entier est supprimé sans remplacement ; les avantages relatifs aux prélèvements maintenus et les aides au logement restent ouverts aux situations futures éligibles.",
        substantive_impact=impact(
            'coordination_only', assessment + " La réduction du principal est comptée une seule fois à L813-4, sous la même measure_id.",
            "Le texte ne supprime que l'exécution du FNAL sur les revenus nouveaux ; les dettes anciennes, contrôles et recours subsistent. Les textes sociaux, territoriaux et formulaires identifiés dans les notes restent à coordonner ; aucun gain net global n'est chiffré.",
            "Aucune charge nouvelle n'est identifiée : aucun dossier, donnée, registre, délai ni prélèvement de remplacement. Le traitement du stock ancien et les formalités communes aux prélèvements maintenus conservent leurs conditions légales.",
            [effect('coordination', fnal_measure,
                    "Coordination de l'extinction du FNAL : " + scope + '.',
                    before, after, 'legal_duty',
                    "Employeurs et organismes de recouvrement relevant du champ de cet article ; redevables et créanciers concernés par le stock ancien.",
                    "Même bascule par période d'activité que L813-4, y compris périodes chevauchantes ; règles antérieures conservées pour les anciennes périodes et leurs régularisations ultérieures.",
                    "Aucun dispositif de remplacement ; obligations communes et garanties anciennes maintenues ; aucune deuxième réduction comptabilisée.",
                    quote, operative)])
    )


retain('L821-1',
       "Maintien intégral nécessaire du champ du livre et de la distinction entre APL, allocation familiale, allocation sociale et primes de déménagement. Cet article institue un cadre de droits, sans déclaration, autorisation ou prélèvement accessoire à retirer. Une fusion nominale de ces aides ne supprimerait aucune démarche démontrée et risquerait de modifier leurs champs.",
       "Les subdivisions 1°, 2°, a) et b) sont conservées : elles sont notamment visées par CGI 81 2° bis, L813-4 pour la seule désignation de l'ALS et les textes de versement. La suppression de la contribution de financement n'abroge pas l'ALS ni les autres aides. Pas de restriction aux droits anciens ou aux titulaires d'un type de contrat de travail.",
       "Les trois aides et les primes restent définies dans le même champ ; aucune obligation administrative ou taxe n'est modifiée dans cet article. Le maintien ne compte pas comme simplification ni comme avantage nouveau.",
       "Les conditions propres aux aides et primes figurent ailleurs et ne sont pas fusionnées ici. Leur financement après suppression du prélèvement employeur et leur coût restent à traiter séparément.",
       "Les trois catégories d'aides et les primes de déménagement sont conservées pour toutes les situations futures répondant aux conditions légales. Aucun droit, exonération ou dérogation favorable n'est réservé aux seuls bénéficiaires déjà connus.")

retain('L821-2',
       "Maintien nécessaire de l'affectation des aides à la résidence principale. Cette condition rattache le financement au logement effectivement occupé et prévient la prise en charge de résidences secondaires ; elle ne constitue ni agrément ni justificatif autonome à déposer. Sa suppression étendrait la prestation sans périmètre ni financement décidé.",
       "La condition de résidence principale demeure dans son champ propre ; les modalités de preuve, dérogations et règles de résidence des autres articles ne sont pas remplacées. Le contrat unique ne crée pas de nouvelle condition d'accès au logement.",
       "La condition essentielle de résidence principale demeure intégralement ; aucun dossier, délai ou justificatif supplémentaire n'est créé ou supprimé par cet article.",
       "Les exceptions de résidence et les conditions de preuve relèvent d'autres dispositions et ne sont pas toutes auditées dans ce lot ; aucune extension aux résidences secondaires n'est décidée.",
       "Le droit aux aides pour la résidence principale reste ouvert aux futurs ménages éligibles. L'article n'institue pas de taxe ni d'exonération ; son maintien ne retire aucune dérogation prévue par un autre texte.")

retain('L821-3',
       "Maintien nécessaire de la coordination entre l'aide au logement personnelle d'un enfant et sa prise en compte dans les prestations familiales. Elle évite de retenir simultanément le même enfant comme allocataire autonome et comme enfant à charge dans ce calcul. L'article ne demande ni nouvelle déclaration distincte ni agrément ; sa suppression changerait l'articulation des prestations sans décision sur ce cumul.",
       "La non-prise en compte est limitée au bénéfice des prestations familiales : elle ne vaut ni perte de rattachement fiscal automatique ni exclusion générale des solidarités. Aucun contrat à durée déterminée, condition d'ancienneté ou indemnité de rupture n'est visé.",
       "La règle d'articulation des deux statuts de l'enfant demeure inchangée ; aucun allègement de prélèvement, suppression de formalité ou réduction de délai n'est revendiqué.",
       "L'incidence financière propre à chaque famille et les autres règles de calcul des prestations ne sont pas évaluées ici. Le maintien ne présume pas qu'une nouvelle règle de cumul aurait un coût nul.",
       "L'enfant conserve son accès à une aide personnelle au logement lorsqu'il est éligible ; seules les conséquences de cette perception sur les prestations familiales sont maintenues dans leur champ existant, sans condition nouvelle pour l'avenir.")

retain('L821-4',
       "Maintien intégral nécessaire : le non-cumul empêche une double couverture des mêmes frais de déménagement et le second alinéa garantit le complément lorsque l'autre aide est moindre. Supprimer l'article entier ferait disparaître ce droit favorable ; retirer seulement le non-cumul changerait la coordination financière sans supprimer une formalité démontrée.",
       "L823-8, lu intégralement, porte la prime due aux ménages avec enfant du rang requis et le délai d'ouverture du droit, même sans paiement effectif de l'aide dans le cas qu'il vise. Le renvoi est cohérent et les deux alinéas sont conservés. Les indemnités de préavis et de rupture du code du travail réparent une rupture d'emploi ; elles ne sont pas des primes de déménagement par leur seule dénomination. Les trois cibles imposées sont analysées séparément dans reference_checks. Aucun nouveau renvoi à ces cibles n'est ajouté.",
       "Le non-cumul de financements destinés aux mêmes frais et le versement différentiel favorable demeurent entiers ; la source ne contient pas de délai, dossier ou agrément de plus à retirer.",
       "L'article ne règle pas les indemnités de licenciement ni le préavis. L'éligibilité précise de chaque prime extérieure dépend de son objet réel ; aucun cumul supplémentaire ni suppression d'un droit du travail n'est décidé.",
       "Le complément différentiel prévu au second alinéa est conservé pour les personnes et ménages futurs comme actuels. Une prime extérieure inférieure n'empêche donc pas d'atteindre le montant de prime légalement dû au titre de L823-8 ; aucun avantage de contrat de travail n'est supprimé.")

retain('L821-5',
       "Maintien nécessaire de l'attribution d'une seule aide parmi les trois aides personnelles au logement. Cette règle prévient trois financements concurrents d'une même résidence et organise l'aiguillage réglementaire quand plusieurs champs d'éligibilité se rencontrent. L'article ne crée ni dossier distinct pour chaque aide ni déclaration supplémentaire à abroger.",
       "L821-1 définit les trois aides sans renumérotation. La détermination réglementaire de l'aide applicable reste bornée par les conditions légales propres à chaque régime ; elle ne doit pas être confondue avec une autorisation préalable ou avec la suppression de la contribution employeur. Les droits au versement et aux contestations restent ceux du livre VIII.",
       "La règle de choix entre aides alternatives demeure intégrale ; aucune taxe ni démarche nouvelle n'est supprimée par ce maintien nécessaire.",
       "Le règlement d'aiguillage et les écarts individuels entre aides ne sont pas chiffrés ici. Une fusion des trois prestations dépasserait la seule suppression de leurs éventuels doublons administratifs.",
       "L'accès à chacune des trois aides demeure pour les futures situations qui remplissent son champ. La non-concurrence des versements ne devient pas une fermeture d'accès ; aucune exonération ni dispense favorable n'est retirée.")

retain('L821-6',
       "Maintien intégral nécessaire de l'incessibilité et de l'insaisissabilité des aides et de leurs trois exceptions circonscrites : indus, tiers payant logement et créances alimentaires. Cette protection du revenu de logement et la conciliation avec l'entretien des enfants ne sont pas des obligations administratives inutiles. Retirer la protection ou ses réserves essentielles n'est pas une simplification de démarche.",
       "Les trois numéros sont conservés. CSS L581-1 et L581-3, lus intégralement, visent l'aide au recouvrement alimentaire et le mandat/les avances de l'organisme, non des cotisations. Le troisième alinéa de L553-2, lu avec l'article entier, module les retenues selon composition, ressources, logement et prestations, avec règles spécifiques de fraude ; les garanties et remises du reste du régime ne sont pas écartées. Les tiers payants restent dans le champ de L832-1/L842-1. Aucune nouvelle exception de saisie n'est ajoutée.",
       "La protection patrimoniale de l'aide et les trois exceptions restent identiques à la source entière ; aucune nouvelle charge ou économie n'est attribuée à cet article.",
       "Le montant des retenues, les indus et les créances alimentaires individuels ne sont pas recalculés. Les procédures civiles de saisie et tous leurs textes extérieurs ne sont pas présentés comme audités.",
       "L'incessibilité et l'insaisissabilité restent garanties aux futurs allocataires aussi. Les exceptions ne sont pas élargies et les droits du créancier alimentaire, de l'organisme payeur et du bénéficiaire restent soumis à leurs protections existantes.")

retain('L821-7',
       "Maintien intégral nécessaire de la prescription des actions de paiement et de recouvrement et de ses causes civiles d'interruption. Cette règle assure la sécurité juridique et limite les reprises d'indus sans supprimer le droit au paiement ou le traitement de la fraude. Aucun délai minimal de démarche, justificatif ou agrément inutile n'est imposé par cet article.",
       "CSS L553-1 et sa note ont été lus en entier : deux ans pour l'action de paiement et le recouvrement ordinaire, cinq ans pour manoeuvre frauduleuse ou fausse déclaration, et interruption dans le cas de recouvrements croisés indiqué par le texte. La note corrige une référence parasite à L844-3 dans ce texte extérieur ; l'incohérence est signalée sans correction silencieuse de L553-1. Le renvoi du présent article reste cohérent et ne vise aucun préavis ou délai du contrat unique. Les causes civiles d'interruption restent celles légalement applicables, non réécrites ici.",
       "La prescription et l'interruption restent à droit constant par maintien du texte officiel ; aucun délai d'action supplémentaire n'est réduit et aucune obligation nouvelle n'est créée.",
       "Le maintien ne vérifie pas toutes les causes d'interruption du code civil ni les situations contentieuses individuelles. Les délais de prescription ne sont pas assimilés à une attente administrative supprimable sans examiner les droits opposés.",
       "Les limites au recouvrement, le droit de réclamer le paiement et les interruptions favorables prévues par le droit applicable demeurent utilisables dans les situations futures, sans restriction nouvelle liée à la réforme des contrats de travail.")

retain('L821-8',
       "Maintien intégral nécessaire d'un double avantage : exonération d'impôt sur le revenu des aides personnelles au logement et exclusion de ces aides des ressources servant à attribuer les prestations listées. Les renvois fiscaux sont cohérents ; aucune formalité ni taxe ne peut être supprimée ici sans risquer de retirer l'avantage alors que l'impôt sur le revenu subsiste.",
       "CGI 81 et ses notes, dans la source et la proposition fournies, ont été lus en entier : le 2° maintient l'exonération des prestations familiales et le 2° bis celle de l'APL et de l'ALS. CSS L511-1, lu en entier dans le corpus, comprend l'allocation de logement au 4°, ce qui confirme l'articulation pour l'ALF sans élargir les régimes fiscaux. L'exclusion des ressources vieillesse, prestations familiales, aide sociale et AAH reste entière. Le gel de revalorisation proposé de certaines pensions ne s'applique pas à ces aides ; aucune assimilation à un salaire ou capital de retraite.",
       "Les deux avantages de la source officielle sont maintenus sans rédaction de substitution ; leur conservation ne constitue pas une réduction fiscale nouvelle à comptabiliser.",
       "Les modalités de calcul de chaque prestation et les textes fiscaux autres que la cible fournie ne sont pas refondus ici. Aucun coût budgétaire de l'avantage ni solde de l'ensemble des codes n'est chiffré.",
       "L'exonération d'IR et l'exclusion des ressources sont conservées pour toutes les aides personnelles au logement, y compris pour les futurs bénéficiaires éligibles. Ni les plafonds de ressources des autres prestations ni la suppression du FNAL ne transforment ces aides en revenus imposables ou retenus.")

retain('L822-1',
       "Maintien intégral nécessaire de l'égalité d'application des règles entre conjoint, partenaire de PACS et concubin, dans les trois champs expressément visés. Cette règle rend les droits accessibles sans exiger un mariage et évite une lacune de calcul ; elle n'impose ni registre ni agrément spécifique à supprimer.",
       "Le champ reste celui des dispositions relatives au bénéficiaire, à la résidence principale et aux ressources applicables au conjoint, dans les mêmes conditions. Il ne crée ni solidarité patrimoniale civile générale ni assimilation fiscale extérieure au livre VIII. La réforme de l'emploi ne justifie pas de modifier cette règle familiale autonome.",
       "L'extension de champ favorable aux partenaires et concubins reste identique à la source ; aucune obligation supplémentaire ou réduction de charge nouvelle n'est revendiquée.",
       "La règle ne dispense pas des conditions légales propres à chaque aide et ne refond pas les critères de ressources du ménage. Les autres codes de la famille et de la fiscalité ne sont pas modifiés.",
       "Les partenaires de PACS et concubins, présents comme futurs, conservent l'application des mêmes règles que les conjoints dans les champs énumérés. Aucune dispense, exonération ou possibilité d'aide n'est fermée aux unions futures.")


# Exactement les cibles imposées, y compris celles qui ne relèvent pas de l'objet de l'article.
checks = {
    'L813-5': {
        'LEGITEXT000006073189|LEGIARTI000051289018':
        "Le 1° de la source de L813-5 vise exclusivement le plafond annuel du premier alinéa de CSS L241-3 : cotisations vieillesse plafonnées, revalorisation selon les salaires et absence de baisse du plafond. La proposition cible conserve cette règle au I et ajoute un transfert progressif en capitalisation au II et suivants pour certains salariés privés. Ce transfert n'est ni une nouvelle assiette FNAL ni une baisse du plafond. L'abrogation du barème pour les périodes nouvelles n'affecte pas la vieillesse ; pour les périodes anciennes, le renvoi et le plafond applicables restent ceux du droit antérieur. Aucun critère d'ancienneté, notification de rupture ou contrat unique n'est incorporé dans ce renvoi financier."
    },
    'L821-4': {
        'LEGITEXT000006072050|LEGIARTI000006901112':
        "L1234-1 concerne le préavis de licenciement : source modulée selon l'ancienneté et les dispositions plus favorables, proposition de quinze jours pour les nouveaux contrats avec conservation des anciens régimes et des procédures distinctes. L821-4 vise seulement les versements destinés à couvrir des frais de déménagement et ne renvoie pas à cet article du travail. Une indemnité de préavis n'a pas cet objet par nature ; la notification et l'ancienneté du salarié ne conditionnent donc pas le complément différentiel de déménagement. Aucun renvoi au contrat privé ni aucune réduction de préavis n'est introduit dans l'aide au logement.",
        'LEGITEXT000006072050|LEGIARTI000019071087':
        "L1221-2 définit la forme de l'emploi : CDI de droit commun et possibilités de CDD dans la source ; contrat unique indéterminé pour les nouveaux contrats et protection des anciens dans la proposition. L821-4 ne fixe aucune durée d'emploi ni condition de CDD ; il coordonne des aides ayant le même objet de déménagement. Le non-cumul et le droit au complément restent applicables aux futurs salariés éligibles sous contrat unique comme aux autres ménages. Ni terme de mission ni fin de formation ne devient un terme d'emploi ou une condition de la prime par ce maintien.",
        'LEGITEXT000006072050|LEGIARTI000035644154':
        "L1234-9 porte l'indemnité de licenciement : seuil source de huit mois avec exception de faute grave ; proposition avec seuil d'un an à la fin effective, préavis inclus sous sa réserve d'essai, puis 0,20 mois par année totale, prorata des mois complets et plafond de six mois, employeur seul, avec droits anciens et indemnités spéciales distincts. L821-4 ne vise aucune de ces indemnités par renvoi ; il vise seulement celles réellement destinées aux frais de déménagement. Le zéro avant un an et la notification de rupture ne retirent donc pas la prime ni son complément aux futurs ménages éligibles. Aucun montant ni condition du droit du travail n'est importé."
    },
    'L821-8': {
        'LEGITEXT000006069577|LEGIARTI000054703556':
        "Le renvoi vise exactement les 2° et 2° bis de CGI 81, lus avec tout l'article, ses notes et la proposition : prestations familiales au 2°, APL et allocation sociale désignées par L821-1 au 2° bis. L'ALF relève de l'articulation du 2° avec CSS L511-1 4°, vérifié dans le corpus. La proposition cible conserve ces exonérations ; L821-8 reste donc cohérent sans déplacement de subdivision ni condition fiscale nouvelle. Les exonérations de salaires, indemnités ou retraites figurant ailleurs dans 81 n'introduisent ici aucun seuil d'ancienneté, notification ou restriction aux anciens contrats. L'exonération et l'exclusion des ressources demeurent ouvertes aux aides futures éligibles."
    },
}

for a in answers:
    key = a['code_id'] + '|' + a['source_id']
    required = references['requirements'][key]
    assessments = checks.get(a['number'], {})
    assert set(required) == set(assessments)
    a['reference_checks'] = [
        dict(target_key=k, view_sha256=references['targets'][k]['view_sha256'],
             assessment=assessments[k])
        for k in required
    ]

order = {s['source_id']: i for i, s in enumerate(sources)}
answers.sort(key=lambda a: order[a['source_id']])
(ROOT / 'answer.json').write_text(json.dumps(answers, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answers)} articles')
