import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCES = json.loads((ROOT / 'source.json').read_text())
REFS = json.loads((ROOT / 'reference-targets.json').read_text())
BY_NUMBER = {s['number']: s for s in SOURCES}
ANSWERS = {}


def impact(classification, assessment, limitations, burdens, effects=None):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=limitations, new_burdens_review=burdens,
                effects=effects or [])


def effect(kind, measure_id, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit,
                affected_population=population, conditions_and_transition=transition,
                replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


def add(number, proposed, reason, notes, substantive, *, removed=None,
        repeal=None, benefit=None, checks=None):
    s = BY_NUMBER[number]
    a = {k: s[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}
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
    if benefit:
        a['benefit_review'] = benefit
    key = s['code_id'] + '|' + s['source_id']
    required = REFS['requirements'][key]
    checks = checks or {}
    assert set(checks) == set(required), (number, required, checks)
    a['reference_checks'] = [dict(target_key=k,
                                  view_sha256=REFS['targets'][k]['view_sha256'],
                                  assessment=checks[k]) for k in required]
    ANSWERS[number] = a


MONTHS = "mois commençant à compter de l'entrée en vigueur de la loi"
PAST = "Les droits, indus, restitutions, prescriptions et recours relatifs aux mois antérieurs restent régis par les dispositions qui leur étaient applicables."
WORK_NOTICE = 'LEGITEXT000006072050|LEGIARTI000006901112'
WORK_CONTRACT = 'LEGITEXT000006072050|LEGIARTI000019071087'
WORK_SEVERANCE = 'LEGITEXT000006072050|LEGIARTI000035644154'
AAH = 'LEGITEXT000006073189|LEGIARTI000054477862'
SUBLETTING = 'LEGITEXT000006074096|LEGIARTI000045211579'
YOUNG_RESOURCES = 'LEGITEXT000006074096|LEGIARTI000038814932'
OCCUPANCY = 'LEGITEXT000006074096|LEGIARTI000038834286'
COMMON_PROPERTY = 'LEGITEXT000006074096|LEGIARTI000049397652'


# L822-2 : seule la condition de bourse est retirée ; les catégories restent en place.
s = BY_NUMBER['L822-2']
old_student = "3° Les personnes de nationalité étrangère remplissant les conditions prévues au deuxième alinéa du même article L. 512-2, à l'exception des ressortissants étrangers, titulaires d'un visa de long séjour ou d'un titre de séjour, mentionnés aux articles L. 422-1 à L. 422-7 du code de l'entrée et du séjour des étrangers et du droit d'asile, qui ne remplissent pas les conditions d'études, d'âge, de diplôme, de nationalité, de ressources ou de mérite pour être titulaires d'une bourse d'enseignement supérieur sur critères sociaux."
new_student = "3° Les personnes de nationalité étrangère remplissant les conditions prévues au deuxième alinéa du même article L. 512-2."
p = s['source_xml'].replace(old_student, new_student)
assert p != s['source_xml']
p += f"<p>III. - La suppression de la condition d'éligibilité à une bourse d'enseignement supérieur sur critères sociaux s'applique aux aides dues au titre des {MONTHS}, y compris pour les logements déjà occupés. Aucun justificatif de cette éligibilité ne peut être exigé pour ces mois. {PAST}</p>"
add('L822-2', p,
    "Réforme de fond : retrait du filtre de bourse appliqué à certains titulaires de titres de séjour pour études, sans déclaration de remplacement. La régularité du séjour, la résidence principale et les autres conditions d'aide restent entières. La vérification du mérite ou du diplôme pour une bourse ne remplit pas ici de fonction de contrôle de la dépense de logement, déjà soumise aux conditions du livre VIII.",
    "Source et note d'entrée en vigueur au 1er juillet 2026 lues intégralement ; cette date passée n'est pas celle du projet. CSS L512-2 lu dans le corpus : les premier et deuxième alinéas visent des catégories distinctes de séjour régulier, maintenues. D822-0-1 et D822-0-2, lus en entier, sont à retirer pour les mois nouveaux : les dispenses favorables des apprentis, contrats de professionnalisation et étudiants actifs sont absorbées par la suppression générale du filtre, y compris dans le contrat unique. Ne pas rouvrir les mois anciens. L861-5 1° comporte déjà une substitution introuvable dans le 2° actuel de L822-2 ; coordination mahoraise nécessaire, sans attribuer cette incohérence au présent projet. CESEDA et code de l'éducation ne sont pas réécrits ici. Coût de l'extension des aides et articulation avec les textes financiers à établir, sans recette compensatrice présumée.",
    impact('material_reduction',
            "La source entière exclut des étudiants étrangers régulièrement admis au séjour à défaut d'éligibilité à une bourse ; ce motif de refus et sa preuve disparaissent. Les autres conditions d'attribution ne sont pas élargies par assimilation à une bourse.",
            "Pas de suppression des conditions de séjour ni de droit pour les périodes antérieures. L'adaptation de Mayotte et les deux règlements de bourse restent à coordonner hors du lot ; le coût public n'est pas chiffré.",
            "Aucune attestation, déclaration ou autorisation nouvelle n'est identifiée : le critère est supprimé sans substitut. Davantage de personnes peuvent percevoir une aide, avec dépenses et traitement public supplémentaires non évalués.",
            [effect('relief_extended', 'aides-logement-fin-filtre-bourse',
                    "Ouverture de l'aide aux étudiants jusque-là exclus par le seul filtre de bourse.",
                    "Étudiants étrangers des titres visés exclus s'ils ne remplissent pas les conditions de bourse ; aucun taux fiscal en cause.",
                    "Catégorie du deuxième alinéa de CSS L512-2 admise sans condition de bourse, sous les autres conditions du livre VIII.",
                    'legal_duty', "Étudiants étrangers régulièrement admis au séjour relevant du 3°.",
                    "Mois commençant à compter de l'entrée en vigueur ; occupations existantes et nouvelles ; pas de rappel général sur les mois anciens.",
                    "Aucune preuve de remplacement ; volume et montant supplémentaires de prestations à évaluer.",
                    old_student, new_student)]),
    removed=["Exclusion des étudiants étrangers fondée sur les conditions d'études, d'âge, de diplôme, de nationalité, de ressources ou de mérite d'une bourse, et justification de cette éligibilité pour les aides futures."])


# L822-3 : la propriété du demandeur ou du conjoint reste distincte de celle des parents.
old_family = "Les aides personnelles au logement ne sont pas dues aux personnes locataires d'un logement dont elles-mêmes, leurs conjoints ou l'un de leurs ascendants ou descendants, jouissent d'une part de la propriété ou de l'usufruit, personnellement ou par l'intermédiaire de parts sociales de sociétés, quels que soient leurs formes et leurs objets."
new_family = "Les aides personnelles au logement ne sont pas dues aux personnes locataires d'un logement dont elles-mêmes ou leurs conjoints jouissent d'une part de la propriété ou de l'usufruit, personnellement ou par l'intermédiaire de parts sociales de sociétés, quels que soient leurs formes et leurs objets."
family_relief = "Par dérogation à la règle posée au premier alinéa, ces aides peuvent être versées si l'ensemble des parts de propriété et d'usufruit du logement ainsi détenues est inférieur à des seuils fixés par voie réglementaire. Ces seuils ne peuvent excéder 20 % de la propriété ou de l'usufruit du logement."
p = f"<p>{new_family}</p><p>{family_relief}</p><p>La propriété ou l'usufruit détenu par un ascendant ou un descendant ne peut, à raison de ce seul lien de parenté, faire obstacle à l'aide. La suppression de cette exclusion s'applique aux aides dues au titre des {MONTHS}, y compris pour les baux en cours. {PAST}</p>"
add('L822-3', p,
    "Réforme de fond : suppression de l'exclusion automatique lorsque le bailleur propriétaire ou usufruitier est un ascendant ou descendant. Un lien familial ne prouve pas l'absence d'une dépense de logement. L'exclusion pour les parts propres du demandeur ou du conjoint, directes et indirectes, et sa dérogation favorable restent entières ; le paiement d'un loyer et le contrôle des locations fictives subsistent.",
    "R822-1 lu : son seuil effectif est de 10 %, avec cumul strictement inférieur à 10 %, et non le maximum légal de 20 %. Aucun de ces taux n'est relevé par le projet ; le règlement doit seulement cesser d'agréger des parts d'ascendants ou descendants au titre de cette exclusion. Le renvoi de L822-4 reste opérant pour les parts du locataire, sous-locataire et propriétaire dans le champ ainsi réduit. Les revenus ou aides familiales entrant légalement dans les ressources restent soumis à leur régime. Aucune exonération fiscale ni aucun droit de propriété n'est modifié.",
    impact('material_reduction',
            "L'interdiction générale fondée sur les parts d'un ascendant ou descendant est retirée, y compris via une société. Ce changement élargit l'accès à l'aide sans supprimer la règle d'autopropriété ni sa dérogation.",
            "Pas de droit automatique en l'absence de loyer réel ou des autres conditions. L'effet sur les dépenses d'aides et les pratiques de location familiale n'est pas chiffré ; les mois anciens conservent leur droit.",
            "Aucune déclaration, preuve spéciale du lien familial, autorisation ou délai nouveau n'est créé. Les contrôles ordinaires du loyer et des ressources demeurent ; l'extension peut accroître les versements publics sans solde net établi.",
            [effect('relief_extended', 'aides-logement-location-familiale',
                    "Retrait du refus d'aide à raison de la seule propriété des ascendants ou descendants.",
                    "Parts des intéressés, conjoints, ascendants et descendants prises en compte dans l'exclusion, avec dérogation sous seuil réglementaire.",
                    "Seules les parts propres des intéressés ou conjoints déclenchent cette exclusion ; mêmes seuils favorables pour ces parts.",
                    'legal_duty', "Locataires et sous-locataires dont un ascendant ou descendant détient des droits sur le logement.",
                    "Mois nouveaux après entrée en vigueur, baux déjà conclus inclus ; régime antérieur des mois anciens conservé.",
                    "Aucun agrément ou justificatif familial de substitution ; dépense publique supplémentaire non chiffrée.",
                    old_family, new_family)]),
    removed=["Exclusion de l'aide en raison de parts de propriété ou d'usufruit du logement détenues par un ascendant ou descendant, directement ou au travers de sociétés, indépendamment d'une dépense réelle de loyer."],
    benefit="La dérogation permettant le versement pour une faible détention de propriété ou d'usufruit reste intégralement applicable aux parts du demandeur et de son conjoint, pour les situations futures aussi. Le plafond légal de 20 % et le seuil réglementaire actuel de 10 % ne sont pas confondus ni durcis. Les parts des ascendants et descendants cessent de déclencher l'exclusion : leurs locataires sont donc mieux admis que sous la seule dérogation antérieure. Les droits relatifs aux mois anciens sont conservés.")


# L822-4 : la sous-location partielle ne constitue plus en elle-même un obstacle à l'aide.
old_sublet = "Les aides personnelles au logement ne sont pas dues si le local est loué ou sous-loué en partie à des tiers, sauf s'il s'agit d'une personne âgée ou handicapée adulte qui a passé un contrat conforme aux dispositions de l'article L. 442-1 du code de l'action sociale et des familles ou d'une personne de moins de trente ans."
new_sublet = "La location ou la sous-location d'une partie du logement à un tiers ne fait pas obstacle au bénéfice d'une aide personnelle au logement."
p = f"<p>{new_sublet}</p><p>Pour l'attribution d'une aide personnelle au logement, les personnes âgées ou handicapées adultes ayant passé un contrat conforme aux dispositions de l'article L. 442-1 du code de l'action sociale et des familles et les sous-locataires, quel que soit leur âge, sont assimilés à des locataires, au titre de la partie du logement qu'ils occupent.</p><p>Toutefois, les conditions fixées à l'article L. 822-3 du présent code s'appliquent également au locataire, au sous-locataire et au propriétaire.</p><p>Pour l'attribution d'une aide personnelle au logement, en cas d'intermédiation locative et en cas d'application des articles L. 442-8-1 et L. 442-8-1-2 du présent code prévoyant une sous-location totale du logement, le sous-locataire est assimilé au locataire.</p><p>La suppression de l'exclusion liée à la sous-location partielle et l'assimilation des sous-locataires sans condition d'âge s'appliquent aux aides dues au titre des {MONTHS}, y compris pour les locations, sous-locations et accueils en cours. Elles ne dispensent pas du respect des règles régissant la location, la sous-location ou l'accueil familial. {PAST}</p>"
add('L822-4', p,
    "Réforme de fond : retrait du refus d'aide pour sous-location partielle et de la limite de moins de trente ans pour l'assimilation des sous-locataires. Les personnes âgées ou handicapées sous contrat d'accueil, l'intermédiation et les sous-locations totales HLM conservent leur fondement. Les conditions de propriété, dans le champ réduit de L822-3, et les règles de licéité de la sous-location restent distinctes.",
    "Les quatrième et troisième alinéas sources sont conservés sans déplacement. L442-8-1 et sa proposition ainsi que L442-8-1-2 officiel ont été lus en entier : la sous-location saisonnière de six mois est une durée de logement, jamais un terme de l'emploi ; la présente ouverture d'aide n'élargit pas les autorisations de sous-location HLM ni ne rétablit l'information préalable retirée dans la proposition de L442-8-1. Le contrat d'accueil CASF L442-1 reste exigé pour son régime propre ; son texte extérieur au corpus n'est pas réécrit. Les trois cibles de droit du travail sont sans incidence sur le droit d'occupation visé. Coordonner les critères réglementaires d'aide sans supprimer plafonds, garanties de décence ou droits des personnes accueillies. Pas de taxe supprimée ni de coût budgétaire estimé.",
    impact('material_reduction',
            "La source n'admet certaines sous-locations partielles qu'au titre de l'âge ou du handicap et exclut les autres. Cette restriction d'aide est supprimée ; l'assimilation des sous-locataires est étendue sans changer la durée de leur emploi ni les conditions d'accueil familial.",
            "L'ouverture de l'aide n'autorise pas une sous-location interdite par le bail ou une autre loi. Les règlements de liquidation doivent suivre ; aucune augmentation de montant individuel n'est chiffrée et les mois anciens restent distincts.",
            "Aucun contrat de travail, agrément, déclaration ou justificatif nouveau n'est imposé. Le contrat d'accueil reste à son champ existant ; l'examen de davantage de demandes et les aides supplémentaires ont un coût public inconnu.",
            [effect('relief_extended', 'aides-logement-sous-location-partielle',
                    "Suppression de l'exclusion d'aide liée à la sous-location partielle et ouverture sans limite d'âge des sous-locataires.",
                    "Sous-location partielle exclue sauf personnes âgées ou handicapées adultes sous contrat d'accueil ou personnes de moins de trente ans.",
                    "Sous-location partielle non excluante ; sous-locataires de tout âge assimilés pour leur partie occupée ; autres conditions d'aide conservées.",
                    'legal_duty', "Locataires, sous-locataires et personnes accueillies dans une partie du logement.",
                    "Mois nouveaux, contrats d'occupation en cours inclus ; aucun effet rétroactif sur les mois anciens.",
                    "Pas de déclaration remplaçant la restriction ; règles civiles et sociales de sous-location préservées.",
                    old_sublet, new_sublet)]),
    removed=["Exclusion générale des aides lorsque le logement est partiellement loué ou sous-loué à un tiers hors des catégories limitativement admises.",
             "Limite d'âge de moins de trente ans pour l'assimilation d'un sous-locataire à un locataire aux fins d'aide personnelle au logement."],
    checks={
        WORK_NOTICE: "L1234-1 traite du préavis de licenciement : ancien régime selon six mois/deux ans et proposition de quinze jours pour les nouveaux contrats. L822-4 règle l'occupation et l'aide au logement ; aucun préavis locatif ni condition de notification de travail n'en résulte et aucun renvoi à cet article n'est ajouté.",
        WORK_CONTRACT: "L1221-2 proposé interdit un terme pour les nouvelles embauches mais admet une affectation temporaire. L822-4 ne dépend pas d'un CDD ; les sous-locations admises restent accessibles aux salariés du contrat unique, sans que leur durée de logement termine l'emploi. Les anciens contrats ne sont pas requalifiés ici.",
        WORK_SEVERANCE: "L1234-9 concerne l'indemnité de rupture patronale et son seuil d'un an à la fin effective, préavis inclus, avec 0,20 mois par année totale. Aucune indemnité de licenciement n'est visée par L822-4 : ni ce seuil, ni le plafond de six mois, ni l'ancienne condition de huit mois ne conditionnent la sous-location ou son aide.",
        SUBLETTING: "L442-8-1 I autorise des locations aux intermédiaires, notamment pour des sous-locations saisonnières de six mois ; II traite d'accueil partiel de personnes âgées ou handicapées. Son projet maintient l'accès saisonnier sous contrat unique et retire l'information préalable du II. Le renvoi de L822-4 à la sous-location totale est maintenu, sans restaurer cette information, sans condition d'ancienneté et sans confondre six mois de logement et terme de l'emploi."
    })


# L822-5 : suppression du critère de capital et de sa traduction en revenus fictifs.
old_capital = "Les aides personnelles au logement ne sont dues qu'aux personnes payant un minimum de loyer, compte tenu de leurs ressources et de la valeur en capital de leur patrimoine, lorsque cette valeur est supérieure à un montant fixé par voie réglementaire."
new_capital = "La valeur en capital du patrimoine appréciée pour l'ensemble du ménage n'est pas prise en compte dans le calcul de l'aide personnelle au logement."
p = f"<p>Les aides personnelles au logement ne sont dues qu'aux personnes payant un minimum de loyer, compte tenu de leurs ressources.</p><p>{new_capital} Cette exclusion s'applique notamment lorsque le demandeur d'une aide personnelle au logement ou son conjoint est bénéficiaire de l'allocation aux adultes handicapés prévue à l'article L. 821-1 du code de la sécurité sociale ou de l'allocation d'éducation de l'enfant handicapé prévue à l'article L. 541-1 du même code.</p><p>La même exclusion s'applique au demandeur d'une aide personnelle au logement résidant dans un établissement d'hébergement pour personnes âgées dépendantes ou dans une résidence autonomie mentionnés à l'article L. 313-12 du code de l'action sociale et des familles.</p><p>Aucun revenu forfaitaire ne peut être ajouté aux ressources au seul titre de la détention ou de la valeur de ce patrimoine. Aucune déclaration, évaluation ou pièce justificative ne peut être exigée exclusivement pour établir cette valeur. Les revenus effectivement tirés du patrimoine restent soumis aux règles de prise en compte des ressources, avec les exclusions, abattements et neutralisations qui leur sont applicables.</p><p>La suppression de la prise en compte de la valeur en capital s'applique aux aides dues au titre des {MONTHS}, pour les droits en cours comme pour les nouvelles demandes. {PAST}</p>"
add('L822-5', p,
    "Réforme de fond : suppression de l'évaluation du capital du ménage comme critère d'aide et de son imputation forfaitaire en ressources, sans supprimer le critère des ressources ni le minimum de loyer. Le soutien est apprécié d'après les revenus disponibles selon leur régime, plutôt qu'un revenu présumé d'un actif non productif. Les exclusions AAH, AEEH, EHPAD et résidence autonomie sont expressément conservées et généralisées ; la preuve patrimoniale exclusivement liée au critère retiré est interdite.",
    "R822-22 lu en entier, notes comprises : seuil de 30 000 euros, exclusion de la résidence principale et des biens professionnels, absence de double compte des revenus déjà retenus, imputations de 50 %/80 % de valeur locative et 3 % des capitaux, déclaration et mises à jour. Ce règlement évite déjà certains doubles comptes : la réforme retire un critère autonome, elle ne prétend pas supprimer un doublon dans tous les cas. Il faut retirer ces seuls calculs et preuves pour les mois nouveaux ; aucune modification de l'IFI ou des revenus réels n'en découle. L822-6 et L823-1 sont coordonnés dans ce lot sous la même mesure. Les substitutions de L861-5 2° peuvent encore viser les mentions AAH/AEEH maintenues ; les autres adaptations territoriales sont à vérifier sans restriction nouvelle. CSS L541-1 lu ; les conditions propres de l'AEEH et de ses compléments ne changent pas. Les numéros L900-2/L900-3, L311-5 et L141-4 du code du travail présents dans la cible AAH appellent leur concordance propre dans le lot CSS : aucune réattribution au contrat unique n'est faite ici. CASF L313-12 n'est pas réécrit. Dépenses supplémentaires d'aides et économies administratives non chiffrées.",
    impact('material_reduction',
            "La source entière subordonne l'aide au capital au-delà d'un montant réglementaire avec trois exceptions. Le capital et le revenu fictif associé cessent d'affecter tous les ménages ; les revenus réels et leurs allègements restent dans l'assiette des ressources.",
            "Ce n'est ni une suppression de l'IFI ni une exonération des revenus réels du patrimoine. L'effet dépend des ressources, du logement et du barème ; R822-22 reste à coordonner, et aucun solde budgétaire ou national de complexité n'est démontré.",
            "Aucune charge nouvelle de déclaration, d'évaluation ou de justificatif n'est créée ; les demandes exclusivement patrimoniales sont au contraire retirées. L'aide peut augmenter pour certains ménages, ce qui accroît les dépenses publiques sans montant estimé.",
            [effect('relief_extended', 'aides-logement-fin-patrimoine-impute',
                    "Généralisation de l'exclusion de la valeur du capital et retrait de l'imputation de revenu de sa seule détention.",
                    "Capital pris en compte au-delà d'un montant réglementaire, sauf ménages AAH/AEEH et demandeurs en EHPAD/résidence autonomie ; ressources réelles conservées.",
                    "Valeur du capital exclue pour tout ménage ; aucun revenu forfaitaire tiré de cette seule valeur ; revenus réels toujours appréciés selon leurs règles favorables comprises.",
                    'other', "Ménages demandant ou percevant une aide personnelle au logement, notamment détenteurs d'actifs non productifs.",
                    "Mois nouveaux après entrée en vigueur, droits en cours inclus ; calcul et recours des mois antérieurs préservés.",
                    "Ni déclaration ni attestation de remplacement ; coût supplémentaire des prestations non chiffré, revenus réels toujours contrôlables.",
                    old_capital, new_capital)]),
    removed=["Prise en compte de la valeur en capital du patrimoine au-delà d'un montant fixé par règlement pour déterminer le droit ou le montant de l'aide personnelle au logement.",
             "Imputation aux ressources de revenus forfaitaires tirés de la seule valeur patrimoniale et demandes de déclaration, d'évaluation ou de justificatifs exclusivement destinés à cette valeur."],
    benefit="Les avantages possibles sont l'exclusion du capital de tout le ménage lorsque le demandeur ou son conjoint perçoit l'AAH ou l'AEEH, ainsi que l'exclusion pour le demandeur résidant en EHPAD ou résidence autonomie. Ces trois situations restent nommées et couvertes, y compris à l'avenir ; la règle devient générale sans condition supplémentaire. Les dispenses de R822-22 pour la résidence principale et les biens professionnels ainsi que l'absence de double compte sont absorbées par l'exclusion totale du critère de capital. Les abattements et neutralisations sur les revenus réels demeurent et les droits des mois anciens restent régis par leur droit favorable applicable.",
    checks={AAH: "La cible officielle L821-1 du CSS définit l'AAH, ses conditions de séjour, l'articulation avec vieillesse, invalidité et rentes, ainsi que ses compléments différentiels ; elle ne définit aucun préavis ou contrat de travail unique. Le renvoi de L822-5 demeure l'identification d'une catégorie déjà dispensée de prise en compte du capital, désormais incluse dans une exclusion générale. Ni l'âge de retraite, ni les ressources propres de l'AAH, ni ses continuités de paiement ne sont modifiés ; aucune condition d'ancienneté de travail n'est ajoutée."})


p = f"<p>La détermination ainsi que les conditions de prise en compte des ressources sont définies par voie réglementaire.</p><p>Les conditions de prise en compte des ressources, notamment les périodes de référence retenues, peuvent varier en fonction de la nature des ressources.</p><p>Pour les aides dues au titre des {MONTHS}, ces dispositions réglementaires respectent l'exclusion de la valeur en capital du patrimoine et des revenus forfaitaires tirés de sa seule détention prévue à l'article L. 822-5. Les dispositions applicables aux mois antérieurs demeurent réservées.</p>"
add('L822-6', p,
    "Coordination nécessaire de l'habilitation réglementaire avec L822-5 : retrait de la compétence pour prendre en compte la valeur du patrimoine, sans modifier la diversité des périodes selon les ressources. Le règlement ne peut rétablir sous le nom de ressource le revenu forfaitaire de capital supprimé.",
    "Même mesure que L822-5, aucune seconde suppression comptée. R822-3 et R822-4 lus intégralement avec leurs notes : périodes et abattements ne sont pas uniformisés par ce projet. R822-22 doit être coordonné pour les seuls mois nouveaux ; les calculs et avantages des mois anciens sont préservés. L'exclusion du patrimoine ne dispense pas de déclarer un revenu réel légalement pris en compte.",
    impact('coordination_only',
            "Le renvoi réglementaire à la valeur du patrimoine est retiré parce que L822-5 l'exclut désormais ; aucune baisse distincte d'impôt ou nouvelle suppression de déclaration n'est attribuée à cet article d'habilitation.",
            "La définition des ressources, leurs exclusions et leurs périodes restent réglementaires. Les articles d'application ne sont pas réécrits dans ce lot ; effet net budgétaire et charge globale non établis.",
            "Aucune donnée, déclaration, échéance ou condition nouvelle n'est identifiée : l'habilitation est réduite et encadrée par la même exclusion, sans nouvelle procédure de calcul parallèle.",
            [effect('coordination', 'aides-logement-fin-patrimoine-impute',
                    "Limitation de l'habilitation réglementaire aux ressources après retrait du capital.",
                    "Le règlement détermine les ressources et la valeur du patrimoine.",
                    "Le règlement détermine les ressources et respecte l'exclusion légale du capital ; périodes différenciées inchangées.",
                    'legal_duty', "Pouvoir réglementaire et organismes liquidateurs des aides personnelles au logement.",
                    "Même bascule mensuelle que L822-5 ; mois antérieurs réservés.",
                    "Aucun dispositif réglementaire ni dépôt de remplacement autorisé par cette coordination.",
                    "La détermination ainsi que les conditions de prise en compte des ressources et de la valeur du patrimoine sont définies par voie réglementaire.",
                    "La détermination ainsi que les conditions de prise en compte des ressources sont définies par voie réglementaire.")]),
    removed=["Habilitation réglementaire à déterminer et prendre en compte la valeur du patrimoine dans les aides futures, retirée en coordination de L822-5 sans réduction distincte supplémentaire."])


p = f"<p>Le présent article est abrogé pour les aides dues au titre des {MONTHS}.</p><p>Pour ces mois, le rattachement au foyer fiscal de parents assujettis à l'impôt sur la fortune immobilière ne peut faire obstacle à une aide personnelle au logement. Les autres conditions d'attribution et de prise en compte des ressources restent applicables. Aucune déclaration ni pièce justificative relative à l'assujettissement des parents à cet impôt ne peut être exigée au seul titre de l'exclusion supprimée.</p><p>{PAST} La présente abrogation ne modifie pas l'impôt sur la fortune immobilière.</p>"
add('L822-8', p,
    "Abrogation de fond de l'exclusion liée à l'IFI des parents pour les aides futures, sans supprimer l'IFI. Le rattachement fiscal ne suffit pas à établir les ressources disponibles pour le logement ; les ressources effectivement retenues par les autres articles continuent d'être examinées. La preuve de l'IFI parental exclusivement nécessaire à ce filtre disparaît.",
    "R822-3 2° lu en entier : retirer, pour les mois nouveaux, la référence annuelle à l'assujettissement IFI lorsqu'elle sert seulement cette exclusion, en gardant pensions alimentaires, frais de tutelle et frais professionnels et leurs régularisations favorables. L823-1 cesse dans ce lot de renvoyer à L822-8. L'article 964 du CGI n'est ni abrogé ni modifié ; pas de baisse d'IFI revendiquée. L'aide n'est pas accordée sans les autres conditions, ni rétablie rétroactivement pour les mois anciens. Coût d'ouverture des aides à évaluer séparément.",
    impact('material_reduction',
            "La source exclut tout membre du ménage rattaché à des parents imposés à l'IFI ; ce motif de refus et son contrôle spécifique sont entièrement retirés pour les mois nouveaux. L'IFI lui-même subsiste.",
            "L'effet ne concerne que l'accès aux aides personnelles, pas l'assiette ou le taux d'IFI ni les prestations extérieures. Les ressources familiales légalement retenues restent contrôlées et le coût public de l'extension est inconnu.",
            "Aucune attestation familiale ou déclaration d'autonomie de remplacement n'est créée. La preuve du patrimoine ou de l'IFI parental n'est plus exigible sur ce seul fondement ; des versements publics supplémentaires restent possibles et non chiffrés.",
            [effect('relief_extended', 'aides-logement-fin-exclusion-ifi-parents',
                    "Suppression de l'exclusion d'aide fondée sur l'IFI des parents.",
                    "Aucune aide pour les personnes rattachées fiscalement à des parents assujettis à l'IFI, condition appréciée pour chaque membre du ménage.",
                    "Ce rattachement et cet impôt parental n'excluent plus l'aide ; ressources et autres conditions demeurent.",
                    'legal_duty', "Ménages comprenant une personne rattachée au foyer de parents assujettis à l'IFI.",
                    "Mois nouveaux, demandes et droits en cours inclus ; mois anciens régis par leurs règles.",
                    "Aucun test de remplacement ; IFI et obligations fiscales autonomes inchangés.",
                    "Les personnes rattachées au foyer fiscal de leurs parents, lorsque ces derniers sont assujettis à l'impôt sur la fortune immobilière en application de l'article 964 du code général des impôts, ne peuvent bénéficier d'aucune aide personnelle au logement.",
                    "Pour ces mois, le rattachement au foyer fiscal de parents assujettis à l'impôt sur la fortune immobilière ne peut faire obstacle à une aide personnelle au logement.")]),
    repeal="Exclusion de toute aide personnelle au logement en raison de l'IFI des parents et de l'appartenance à leur foyer fiscal ; contrôle et preuve exclusivement attachés à cette exclusion pour les mois nouveaux, sans suppression de l'IFI.")


add('L822-10', None,
    "Maintien intégral nécessaire après examen : les conditions de peuplement protègent les occupants contre une densité incompatible avec un logement adapté. Elles ont une fonction de salubrité distincte des conditions de ressources et ne constituent ni un quota SRU ni une formalité de double dépôt. Leur suppression générale n'est pas retenue au détriment de cette protection.",
    "R822-25 lu en entier : 9 m² pour une personne, 16 m² pour deux, +9 m² par personne, plafond de 70 m² pour huit personnes et plus. R844-1, R844-2 et R844-4 lus : dérogations, maintiens et prorogations demeurent ouverts aux situations futures ; aucune fermeture de ces avantages n'est décidée. L861-5 3° et R861-5 3° prévoient des règles et maintiens propres à Mayotte, à ne pas remplacer par la grille générale. L822-9 et les protections de décence restent distincts. Les allègements éventuels de pièces du régime réglementaire ne sont pas déclarés accomplis par ce maintien.",
    impact('retained_necessary',
            "La condition légale de peuplement et son habilitation sont conservées en entier pour leur fonction de protection de l'occupation. Aucun prélèvement, délai ou autorisation n'est supprimé et aucune simplification n'est comptée.",
            "Le maintien n'audite pas tous les justificatifs réglementaires ; les seuils de surface et les dérogations territoriales ou sociales conservent leur régime, sans chiffrage de coût global.",
            "Aucune charge nouvelle n'est identifiée puisque l'article n'est pas modifié ; aucune surface, attestation ou procédure supplémentaire n'est ajoutée et les dérogations futures restent accessibles."))


old_resources_item = "2° Ses ressources et la valeur en capital de son patrimoine et, s'il y a lieu, de son conjoint et des personnes vivant habituellement à son foyer, telles que définies aux articles L. 822-5 à L. 822-8 ;"
new_resources_item = "2° Ses ressources et, s'il y a lieu, celles de son conjoint et des personnes vivant habituellement à son foyer, telles que définies aux articles L. 822-5 à L. 822-7 ;"
p = BY_NUMBER['L823-1']['source_xml'].replace(old_resources_item, new_resources_item)
assert p != BY_NUMBER['L823-1']['source_xml']
p += f"<p>Le 2°, dans sa rédaction excluant la valeur en capital du patrimoine, s'applique aux aides dues au titre des {MONTHS}. Pour ces mois, le barème ne peut réintroduire la prise en compte du capital ou de revenus forfaitaires tirés de sa seule détention, ni l'exclusion liée à l'impôt sur la fortune immobilière des parents supprimée à l'article L. 822-8. Les dispositions applicables aux mois antérieurs demeurent réservées.</p>"
add('L823-1', p,
    "Coordination de fond indispensable du barème : retirer le capital du 2° et arrêter le renvoi aux ressources à L822-7, sans conserver le filtre de L822-8 abrogé. Les 1°, 3°, 4°, la prise en compte des dépenses accessoires, le plafond de loyer et la condition des enfants de CSS L512-2 sont intégralement maintenus. Cette coordination ne vaut pas nouvelle baisse d'impôt ni nouveau barème chiffré.",
    "Mesures de L822-5 et L822-8 dédupliquées ; ni coefficient ni plafond inventé. L822-7 fourni conserve dans son projet les dispositions de ressources des moins de vingt-cinq ans pour les affectations et périodes temporaires sous contrat unique ; ne pas le neutraliser par un test de CDI au niveau du barème. Le renvoi final à CSS L512-2 vise les enfants à charge, non une condition d'ancienneté de travail ; ce texte officiel a été lu. L861-5 4° écarte à Mayotte le septième alinéa, qui reste en place : pas de déplacement de cette cible. Les règlements et arrêtés du barème restent à coordonner avec les deux suppressions sans retirer leurs abattements. Aucun lissage général des dégressivités du revenu n'est présenté comme déjà chiffré ou réalisé ici.",
    impact('coordination_only',
            "Le seul élément de calcul changé est la coordination du 2° avec le retrait du patrimoine ; le renvoi au filtre IFI cesse également. Les autres composantes du barème demeurent et aucune réduction indépendante n'est comptée.",
            "Les montants et coefficients restent réglementaires, et les neutralisations de L822-7 doivent être coordonnées dans leur propre texte. Aucun gain uniforme d'aide ni effet net sur les finances publiques n'est démontré.",
            "Aucune donnée nouvelle, nouvelle périodicité ou procédure d'emploi n'est créée. L'interdiction de reconstituer les critères retirés limite le barème, sans remplacer ces critères par une déclaration ou une autorisation.",
            [effect('coordination', 'aides-logement-fin-patrimoine-impute',
                    "Retrait du capital dans la liste légale des paramètres du barème.",
                    "Le 2° inclut les ressources et la valeur du capital du demandeur et du foyer.",
                    "Le 2° ne vise que les ressources, avec le même périmètre du foyer et les règles particulières de L822-7.",
                    'other', "Demandeurs, ménages et organismes calculant les aides personnelles au logement.",
                    "Même bascule mensuelle que L822-5 ; calculs des mois anciens réservés.",
                    "Aucun nouveau calcul patrimonial ni preuve de remplacement.",
                    old_resources_item, new_resources_item),
             effect('coordination', 'aides-logement-fin-exclusion-ifi-parents',
                    "Retrait du renvoi de barème à l'exclusion IFI abrogée.",
                    "Renvoi du 2° à L822-5 jusqu'à L822-8, comprenant l'exclusion IFI des parents.",
                    "Renvoi arrêté à L822-7 et interdiction de rétablir le filtre IFI dans le barème des mois nouveaux.",
                    'legal_duty', "Organismes liquidateurs et ménages concernés par l'ancien filtre IFI.",
                    "Mois nouveaux après entrée en vigueur, sans révision automatique des mois anciens.",
                    "Aucun filtre patrimonial familial ou dépôt substitutif.",
                    old_resources_item,
                    "Pour ces mois, le barème ne peut réintroduire la prise en compte du capital ou de revenus forfaitaires tirés de sa seule détention, ni l'exclusion liée à l'impôt sur la fortune immobilière des parents supprimée à l'article L. 822-8.")]),
    removed=["Paramètre de valeur en capital du patrimoine au 2° du barème et renvoi à L822-8 portant l'exclusion IFI, retirés en coordination des mesures de L822-5 et L822-8 sans les compter une seconde fois."],
    checks={
        WORK_NOTICE: "L1234-1 officiel fixe des préavis selon l'ancienneté et son projet quinze jours pour les nouveaux contrats. L823-1 fixe un barème d'aide, sans viser la rupture ou une notification : aucun délai de quinze jours ni seuil de six mois/deux ans ne peut en être déduit pour le foyer ou ses enfants.",
        WORK_CONTRACT: "Le contrat unique proposé à L1221-2 est indéterminé, même si l'affectation ou la formation est limitée. Le barème de L823-1 ne crée pas de condition de CDD ; son renvoi à L822-7 doit laisser les ressources particulières accessibles aux nouvelles situations temporaires, ainsi qu'aux anciens contrats dans leur transition.",
        WORK_SEVERANCE: "L1234-9 distingue indemnité ordinaire patronale, seuil d'un an au terme effectif avec préavis et 0,20 mois sur toute l'ancienneté, des droits anciens et spéciaux. L823-1 ne vise pas cette indemnité : sa prise en compte éventuelle comme ressource suit les textes de ressources, sans ajouter au droit au logement un seuil de travail ou une condition de notification.",
        YOUNG_RESOURCES: "L822-7 officiel autorise des règles spécifiques de ressources pour les moins de vingt-cinq ans hors CDI ; son projet les conserve pour les affectations temporaires et périodes de formation ou insertion sous contrat unique, sans terme d'emploi, et réserve les agents publics. Le renvoi du 2° reste L822-5 à L822-7 : il inclut cette protection future sans l'assujettir à un licenciement, à un an d'ancienneté ou à un préavis."
    })


add('L823-2', None,
    "Maintien intégral nécessaire : la charge effective et permanente de l'enfant et le partage en résidence alternée évitent un rattachement arbitraire ou un double compte tout en garantissant la prise en compte de l'enfant chez les deux parents. La demande conjointe est une voie favorable ; le désaccord ne ferme pas le partage. Aucun doublon déclaratif n'est imposé par cet article.",
    "Le renvoi au 1° de L823-1 reste exact, cette subdivision n'étant pas modifiée. Le renvoi civil 373-2-9 demeure limité à la résidence alternée effective ; aucune règle de garde ou de consentement parental n'est réécrite ici. R823-5 renvoie à son régime de modalités : aucune date ou fréquence nouvelle n'est introduite. La suppression des CDD et le préavis de quinze jours sont étrangers au rattachement de l'enfant.",
    impact('retained_necessary',
            "Les trois alinéas sources conservent la charge effective, la désignation et le partage sur demande ou désaccord. Ces garanties d'attribution ne sont pas remplacées par une démarche nouvelle et ne sont pas comptées comme allègement.",
            "La répartition concrète reste réglementaire et les décisions de résidence relèvent du droit civil extérieur au lot. Aucun effet chiffré sur les deux foyers ni baisse de prélèvement n'est établi.",
            "Aucune charge nouvelle n'est identifiée car la source reste intégrale : aucune attestation de résidence alternée supplémentaire, nouvelle demande périodique ou autorisation n'est créée."))


add('L823-3', None,
    "Maintien intégral de six assimilations favorables indispensables au calcul de l'aide : remboursements d'emprunt, location-accession, rémunération d'opérateur de copropriété, indemnité d'occupation d'expropriation, redevance de parties communes et indemnité d'accueil familial. Il ne s'agit pas d'un prélèvement accessoire à retirer ; abroger l'énumération fermerait l'aide à ces dépenses.",
    "L615-9 et L615-10 officiels ainsi que le projet de L615-10 sont lus intégralement dans les cibles. Les 4° et 5° correspondent aux dépenses de logement et restent exacts ; le projet de L615-10 retire une actualisation de plan, pas la redevance ni son droit à allocation. L'expérience de vingt ans de 2014 n'est ni prolongée ni recommencée. Les 1°, 2°, 3° et 6° restent complets ; les lois de 1984/1965 et CASF L442-1 conservent leur champ propre, sans prétention de réécriture extérieure. Une indemnité d'occupation n'est pas l'indemnité de licenciement de L1234-9.",
    impact('retained_necessary',
            "Les six catégories intégrales maintiennent des dépenses assimilées au loyer ; l'article n'impose ni autorisation ni déclaration autonome. Le maintien protège des avantages futurs et anciens sans créer une réduction nouvelle.",
            "Chaque assimilation reste soumise au champ de son régime, notamment la durée expérimentale de L615-10 et les conditions générales de l'aide ; aucune dette de logement n'est annulée ni aucun montant augmenté par cet article.",
            "Aucune charge nouvelle n'est identifiée : aucune redevance, registre, donnée ou formalité n'est ajouté. Les dépenses de logement préexistent et leur assimilation favorable reste entièrement en vigueur.", []),
    checks={
        WORK_NOTICE: "Le préavis de L1234-1 concerne le licenciement, avec protection des anciens contrats et quinze jours proposés pour les nouveaux. Les mensualités, redevances et indemnités de L823-3 sont des dépenses d'occupation : aucune notification de rupture du travail ni ancienneté de six mois/deux ans ne conditionne leur assimilation au loyer.",
        WORK_CONTRACT: "L1221-2 proposé interdit le terme d'une nouvelle embauche ; aucune des six assimilations de L823-3 ne repose sur un CDD. Le contrat de location-accession est un contrat immobilier et le contrat d'accueil du 6° conserve son régime CASF : ils ne deviennent pas des contrats de travail à durée indéterminée par homonymie.",
        WORK_SEVERANCE: "L1234-9 fixe une indemnité ordinaire de rupture patronale, avec seuil d'un an au terme préavis inclus et calcul de 0,20 mois par année totale. Les indemnités de L823-3 4° et 6° sont respectivement d'occupation et de mise à disposition de pièces ; ni ce seuil, ni le plafond de six mois, ni le régime des anciens licenciements ne s'y appliquent.",
        OCCUPANCY: "L615-9 officiel ouvre aux propriétaires occupants une allocation de logement au titre de l'indemnité versée à l'expropriant. Le 4° de L823-3 vise exactement cette dépense immobilière. Ce renvoi reste cohérent ; il ne désigne ni des dommages de rupture d'emploi ni une indemnité soumise à ancienneté ou préavis de travail.",
        COMMON_PROPERTY: "L615-10 II prévoit la redevance mensuelle proportionnelle à la superficie privative et son droit à allocation ; le 5° de L823-3 l'assimile au loyer. La proposition retire seulement l'actualisation triennale du plan au III et préserve la redevance, les garanties et l'expérience de vingt ans. Aucun nouveau terme d'emploi ni condition d'ancienneté ne résulte de ce renvoi immobilier."
    })


add('L823-4', None,
    "Maintien intégral nécessaire de l'indexation des cinq paramètres du barème : l'échéance annuelle du 1er octobre est une garantie de révision des prestations, pas un délai minimal imposé au demandeur. La supprimer au nom d'une formalité administrative pourrait figer des plafonds favorables. Le cinquième paramètre de participation personnelle conserve aussi son articulation dans l'équilibre du barème.",
    "Tous les chiffres et dates sont conservés : cinq rubriques, 1er octobre, indice du deuxième trimestre de l'année courante et prêts signés après la révision pour le 3°. Le renvoi à l'indice de l'article 17-1 de la loi de 1989 reste à son champ de loyers ; aucun gel de pensions ou seuil de 2 000 euros n'y est transposé. Pas de taux ou d'économie budgétaire inventé, ni d'affirmation d'une hausse uniforme de chaque aide.",
    impact('retained_necessary',
            "Le mécanisme complet de révision et les cinq paramètres indexés restent identiques à la source. Leur maintien est justifié par la continuité du barème, sans compter l'indexation déjà existante comme une extension d'avantage nouvelle.",
            "L'effet de l'indice et de la participation personnelle dépend du barème et de la situation du foyer. Les règles locatives externes et les valeurs d'indice ne sont pas recalculées ni réécrites dans ce lot.",
            "Aucune charge nouvelle n'est identifiée : ni demande annuelle de l'allocataire, ni justificatif, ni délai d'attente n'est ajouté. Le travail de révision publique reste celui de la source."))


add('L823-6', None,
    "Maintien intégral nécessaire des signalements du tiers qui reçoit l'aide lorsque cesse le bail, l'occupation ou la dette de prêt. Ces informations conditionnent l'arrêt correct d'un paiement à ce tiers et préviennent les indus ; rien dans la source entière ne prouve qu'elles sont déjà reçues avec certitude par l'organisme. Aucun double dépôt n'est expressément institué qu'il serait possible de compter comme supprimé.",
    "D823-15 lu intégralement : délai d'un mois, prolongation favorable d'un mois lorsque le bailleur prouve son impossibilité manifeste, et délai d'un mois pour le remboursement du solde du prêt. Ces protections et délais ne sont pas réduits ici. Le déménagement et la résiliation peuvent avoir des dates différentes ; on ne prétend pas fusionner deux obligations identiques. Le réemploi des informations déjà disponibles conserve son droit général sans nouveau gain CRPA revendiqué.",
    impact('retained_necessary',
            "Les deux signalements et leur renvoi réglementaire sont intégralement conservés pour empêcher le paiement d'une aide à un tiers sans dépense correspondante. Aucun canal redondant ou rapport périodique n'est constaté dans l'article.",
            "Le maintien n'établit pas que toutes les pièces d'application sont nécessaires ; il ne vaut pas audit des échanges de données ni dispense générale de l'information du bénéficiaire. Aucun coût net global n'est chiffré.",
            "Aucune charge nouvelle n'est identifiée puisque le texte demeure inchangé : aucun nouveau destinataire, donnée, registre ou délai n'est créé et la prolongation favorable existante est préservée."))


p = f"<p>Le présent article est abrogé pour les aides dues au titre des {MONTHS}.</p><p>Pour ces mois, le versement d'un montant positif d'aide personnelle au logement ne peut être refusé en raison de sa seule faiblesse, quelle que soit la nature de l'aide ou la qualité du demandeur. Les règles distinctes de suspension, de conservation et d'imputation prévues par le présent livre restent applicables. Aucune démarche distincte n'est exigée pour obtenir le versement d'un montant inférieur à l'ancien seuil.</p><p>{PAST} Les droits à prime de déménagement ne sont pas diminués par la présente abrogation.</p>"
add('L823-7', p,
    "Abrogation de fond de la faculté de ne pas verser les petites aides. Le seuil peut priver d'une prestation pourtant calculée et impose une distinction supplémentaire selon l'aide et le statut du demandeur ; il est supprimé sans regroupement de paiement imposé ni nouvelle demande. Ce changement étend les versements, il ne réduit aucun taux d'impôt.",
    "Le montant du seuil relève d'un règlement et peut varier : aucun chiffre réglementaire actuel n'est inventé à partir de cet article. Retirer les dispositions réglementaires ou arrêtés de seuil pour les mois nouveaux, sans modifier barème, arrondis utiles ni conditions d'éligibilité. Les suspensions pour impayés, conservations pour non-décence et imputations légalement prévues ne sont pas effacées par la suppression du seul seuil. L823-8 est coordonné dans ce lot pour maintenir la prime même lorsque l'aide n'a pas été effectivement payée. Le coût des virements supplémentaires et le montant des prestations à verser restent à évaluer, sans économie publique présumée.",
    impact('mixed',
            "La possibilité de refuser le paiement d'un montant mensuel faible disparaît entièrement. L'avantage est étendu aux petits montants ; l'organisme doit désormais les verser, ce qui peut augmenter sa charge de paiement et les prestations publiques.",
            "Ni taux ni assiette du barème ne sont abaissés ; aucun effet sur les mois anciens ni montant national de gain n'est avancé. Les suspensions, conservations et imputations autonomes demeurent ; les seuils d'application restent à retirer dans leurs textes propres.",
            "Aucune démarche ni donnée nouvelle n'est demandée au bénéficiaire. Une charge publique supplémentaire de versement des petits montants remplace la faculté de non-paiement ; son coût net, y compris frais de traitement, n'est pas établi.",
            [effect('relief_extended', 'aides-logement-fin-seuil-non-versement',
                    "Suppression du seuil autorisant le non-versement d'une aide mensuelle positive.",
                    "Aide positive susceptible de ne pas être versée sous un montant réglementaire variable selon l'aide et la qualité du demandeur.",
                    "Montants positifs non écartables au titre de ce seuil ; barème, conditions d'attribution, suspensions, conservations et imputations autonomes inchangés.",
                    'euro', "Bénéficiaires d'aides personnelles d'un montant positif inférieur à l'ancien seuil de non-versement.",
                    "Mois nouveaux après entrée en vigueur ; aucun rappel général sur les mois anciens ; droits à prime protégés.",
                    "Pas de demande distincte ; obligation accrue de paiement et frais publics associés non chiffrés.",
                    "L'aide personnelle au logement peut ne pas être versée lorsque son montant mensuel est inférieur à un montant, qui peut varier selon la nature de l'aide et la qualité du demandeur telle qu'elle est définie au 4° de l'article L. 823-1.",
                    "Pour ces mois, le versement d'un montant positif d'aide personnelle au logement ne peut être refusé en raison de sa seule faiblesse, quelle que soit la nature de l'aide ou la qualité du demandeur.")]),
    repeal="Faculté de ne pas verser une aide personnelle au logement positive en dessous d'un seuil mensuel et habilitation à fixer des seuils variables selon la nature de l'aide ou la qualité du demandeur ; suppression pour les mois nouveaux, sans retrait de la prime.")


s = BY_NUMBER['L823-8']
old_prime = "La prime est due si le droit à l'aide personnelle au logement est ouvert dans un délai fixé par voie réglementaire à compter de la date d'emménagement, même lorsqu'en application de l'article L. 823-7, il n'est pas procédé au versement de l'aide."
new_prime = "La prime est due si le droit à l'aide personnelle au logement est ouvert dans un délai fixé par voie réglementaire à compter de la date d'emménagement, indépendamment du versement effectif de cette aide."
p = s['source_xml'].replace(old_prime, new_prime)
assert p != s['source_xml']
p += "<p>Les droits à prime ouverts avant l'entrée en vigueur de la loi demeurent applicables, y compris lorsque l'aide n'a pas été versée en raison de l'ancien seuil de non-versement. La suppression de ce seuil ne ferme pas les droits à prime des situations futures remplissant les conditions du présent article.</p>"
add('L823-8', p,
    "Coordination nécessaire avec l'abrogation de L823-7 : retirer le renvoi au seuil supprimé tout en conservant le principe favorable selon lequel l'absence de versement effectif ne prive pas de prime. La prime, ses bénéficiaires, le rang de l'enfant, la période du déménagement et le délai d'ouverture du droit restent maintenus ; aucune simple reformulation n'est comptée comme nouvelle suppression.",
    "D823-20 à D823-22 ont été lus intégralement : au moins trois enfants nés ou à naître, fenêtre allant du mois suivant le troisième mois de grossesse au mois précédant les deux ans, ouverture de droit et demande sous six mois, dépenses réellement engagées sous plafond. Ces conditions ne sont ni supprimées ni raccourcies par cette coordination ; les droits des petits montants anciens et futurs restent protégés. Le modèle et les justificatifs réglementaires ne sont pas prétendus allégés ici. L812-1 conserve sa fonction d'identification des organismes payeurs.",
    impact('coordination_only',
            "Le renvoi à la faculté de non-versement abrogée est remplacé par le même principe de prime indépendante du paiement effectif. L'allègement du seuil est imputé à L823-7, pas une seconde fois à la prime.",
            "Le rang de l'enfant, la fenêtre du déménagement, le délai d'ouverture et les dépenses admissibles ne sont pas modifiés. Aucun montant de prime supplémentaire ou baisse de formalités n'est démontré dans cet article.",
            "Aucune charge nouvelle n'est identifiée : ni pièce, ni demande additionnelle, ni autorisation ou délai nouveau n'est créé. Le maintien explicite des droits n'exige aucune nouvelle validation de la prime.",
            [effect('coordination', 'aides-logement-fin-seuil-non-versement',
                    "Maintien de la prime indépendante du paiement effectif après retrait du seuil.",
                    "Prime due sous condition d'ouverture du droit, même si L823-7 écarte le versement de l'aide.",
                    "Prime due sous la même condition de délai, indépendamment du versement effectif ; droits anciens préservés.",
                    'legal_duty', "Ménages remplissant les conditions de la prime de déménagement.",
                    "Droits anciens conservés et nouvelles situations éligibles couvertes, sans réouverture des délais expirés.",
                    "Aucune nouvelle démarche ni réinstruction des primes acquises.",
                    old_prime, new_prime)]))


add('L823-9', None,
    "Maintien intégral nécessaire du fondement de recouvrement des indus avec les garanties de CSS L553-2. La récupération d'une prestation versée sans droit remplit une fonction de protection des fonds et de lutte contre la fraude ; supprimer le renvoi retirerait aussi les retenues adaptées aux ressources et les remises pour précarité. Ce n'est pas un droit de succession à abolir.",
    "CSS L161-1-5 et L553-2 lus en entier : opposition à contrainte, retenues adaptées, option de remboursement, remises hors fraude et règles de récupération croisée demeurent. La mention de succession dans L161-1-5 concerne une dette de prestation, non un prélèvement sur le capital au décès. Aucun élargissement de récupération successorale n'est créé. L861-5 5° adapte le recouvrement à Mayotte ; ses textes extérieurs ne sont pas remplacés ici. Les réformes de cotisations ou d'impôts ne sont pas étendues aux indus d'aide.",
    impact('retained_necessary',
            "Le seul renvoi de l'article reste entier : il permet le recouvrement des aides indûment versées tout en conservant ses modalités favorables et recours. Aucun prélèvement sur une aide régulièrement due n'est créé ou supprimé.",
            "Les textes de recouvrement et leurs sanctions gardent leur champ propre. Ni dette remise, ni économie de gestion, ni baisse de prélèvement n'est chiffrée ; la coordination mahoraise demeure territoriale.",
            "Aucune charge nouvelle n'est identifiée : le fondement, les retenues et la faculté de remise restent ceux de la source ; aucun nouveau certificat de succession ni formalité de remboursement n'est imposé."))


add('L824-1', None,
    "Maintien intégral nécessaire du signalement d'impayé par le tiers qui reçoit l'aide : il permet l'accompagnement et la prévention des expulsions, et évite le maintien aveugle d'un versement sans paiement résiduel. Aucun rapport annuel ni double déclaration n'est imposé dans cet article. Retirer ce signalement priverait les protections de L824-2 de leur déclenchement utile.",
    "Le bailleur ou prêteur visé est celui auprès duquel l'aide est versée, non tout bailleur sans rapport avec le paiement. Le signalement ne vaut ni expulsion, ni suppression automatique d'aide, ni nouveau délai de préavis locatif ou de travail. Les seuils et délais d'application réglementaires restent à leur champ ; aucune procédure de la loi de 1989 n'est prétendue accélérée par cet article inchangé.",
    impact('retained_necessary',
            "Le signalement demeure identique à la source entière parce qu'il déclenche la prévention sociale des impayés. Le maintien ne compte ni une formalité supprimée ni un régime fusionné.",
            "La nécessité de chaque pièce des règlements n'est pas déduite du maintien de la loi. Les conséquences sur le bail et les procédures d'expulsion demeurent extérieures au lot, sans nouveau délai annoncé.",
            "Aucune charge nouvelle n'est identifiée puisque le signalement conserve son auteur et son objet : aucun registre, nouvelle transmission périodique ou donnée supplémentaire n'est demandé."))


add('L824-2', None,
    "Maintien intégral nécessaire de la saisine de prévention des expulsions et de l'accompagnement social et budgétaire. La décision sur le maintien du versement et le diagnostic ne sont pas de simples doubles d'un dossier de ressources : ils visent à traiter l'endettement et protéger le ménage. La voie électronique prévue n'impose pas ici une nouvelle démarche numérique personnelle au locataire.",
    "Les 1° et 2°, la transmission du diagnostic et le système d'information de la loi n°90-449 article7-2 restent entiers. La compétence attribuée par la source à la commission n'est pas remplacée implicitement par une décision unilatérale du bailleur. Le texte extérieur de cette loi et ses procédures ne sont pas réécrits dans ce lot. Aucun accompagnement, maintien favorable de l'aide ou recours n'est fermé pour les dossiers futurs. Le contrat unique et le préavis de quinze jours ne s'appliquent pas à cette procédure sociale.",
    impact('retained_necessary',
            "Le circuit de prévention et d'accompagnement est conservé intégralement pour sa fonction de protection contre la perte du logement. Aucune baisse fictive de transmission ou de coût n'est attribuée à ce maintien.",
            "L'efficacité et les coûts du diagnostic ou du système d'information ne sont pas quantifiés. Les procédures de la commission et les règlements d'impayés nécessitent leurs propres textes, sans pouvoir être déclarés simplifiés ici.",
            "Aucune charge nouvelle n'est identifiée : mêmes destinataires, diagnostic et support d'échange que dans la source ; aucun justificatif ou engagement supplémentaire n'est imposé au ménage."))


add('L824-3', None,
    "Maintien intégral d'un avantage essentiel : la recevabilité du dossier de surendettement rétablit les droits à l'aide du locataire qui bénéficiait d'une aide suspendue. L'effet attaché à une décision déjà prise évite une nouvelle demande de rétablissement ; l'abroger ferait perdre une protection future sans retirer une charge générale.",
    "Le renvoi à consommation L722-10 identifie la recevabilité de la procédure de surendettement, non l'ouverture d'une succession ou la rupture d'un contrat de travail. Le texte de ce code extérieur n'est pas fourni dans le corpus autorisé et n'est pas réécrit ici. L'effet de rétablissement ne dispense pas des conditions de droit à l'aide ni ne vaut annulation des dettes locatives ; aucune ancienne aide suspendue n'est supprimée par les autres réformes du lot.",
    impact('retained_necessary',
            "Le rétablissement favorable des droits du locataire après recevabilité du surendettement reste identique à la source. Il ne constitue pas une nouvelle extension ni une suppression de formalité obtenue par ce lot.",
            "L'article ne règle pas tout le surendettement et ne rembourse pas automatiquement tous les mois de suspension. La procédure de consommation, extérieure aux cinq codes, n'est pas présentée comme vérifiée intégralement.",
            "Aucune charge nouvelle n'est identifiée : le rétablissement demeure attaché à la décision existante, sans nouvelle condition, attestation ou autorisation ajoutée pour le bénéficiaire."))


old_court = "Sous réserve des dispositions de l'article L. 114-17 du code de la sécurité sociale qui attribuent au tribunal de grande instance désigné en application de l'article L. 211-16 du code de l'organisation judiciaire la compétence pour connaître des contestations relatives aux pénalités prononcées en cas de fraude, les recours dirigés contre les décisions prises en matière d'aides personnelles au logement et de primes de déménagement par les organismes mentionnés à l'article L. 812-1 sont portés devant la juridiction administrative."
new_court = "Les contestations relatives aux pénalités prononcées en cas de fraude en application de l'article L. 114-17 du code de la sécurité sociale relèvent du tribunal judiciaire désigné en application de l'article L. 211-16 du code de l'organisation judiciaire."
p = f"<p>{new_court} Les autres recours dirigés contre les décisions prises en matière d'aides personnelles au logement et de primes de déménagement par les organismes mentionnés à l'article L. 812-1 sont portés devant la juridiction administrative.</p>"
add('L825-1', p,
    "Coordination nécessaire de compétence : la source nomme encore le tribunal de grande instance et attribue à CSS L114-17 une règle juridictionnelle que sa source actuelle ne contient plus. Le texte exprime directement la réserve de compétence pour les pénalités de fraude et emploie tribunal judiciaire, sans fusionner les deux ordres de juridiction ni réduire les recours.",
    "Incohérences préexistantes signalées, non corrigées silencieusement : l'appellation tribunal de grande instance est dépassée et CSS L114-17, lu intégralement, ne porte plus l'attribution affirmée par la phrase source. Le renvoi déjà présent à COJ L211-16 est conservé sans inventer de subdivision ; le texte complet de ce code extérieur n'est pas joint et sa concordance de désignation des tribunaux est à vérifier dans le paquet extérieur. La séparation administrative/pénalités de fraude est préservée. Aucun nouveau renvoi n'est ajouté, aucune pénalité, compétence matérielle supplémentaire ou délai de recours n'est créé.",
    impact('coordination_only',
            "La source entière comporte une désignation juridictionnelle obsolète et un renvoi attributif désormais inexact. La coordination les rend explicites sans présenter le changement de nom comme une obligation retirée ou une justice accélérée.",
            "L'organisation judiciaire extérieure au corpus doit être confrontée pour sa désignation territoriale. Aucun effet sur les délais, le coût du procès ou les sanctions n'est démontré ; aucune répartition nouvelle des litiges n'est décidée.",
            "Aucune charge nouvelle n'est identifiée : même contestation et même séparation des recours, sans demande, tribunal supplémentaire ou procédure préalable ajoutée.",
            [effect('coordination', 'aides-logement-competence-juridictionnelle',
                    "Actualisation de la désignation du juge de la pénalité de fraude et expression directe de la réserve.",
                    "Mention d'un tribunal de grande instance et attribution annoncée dans CSS L114-17, sous réserve du contentieux administratif des aides.",
                    "Réserve expresse du tribunal judiciaire déjà désigné par le renvoi existant ; autres recours administratifs conservés.",
                    'regime', "Allocataires contestant une décision d'aide ou une pénalité de fraude et organismes payeurs.",
                    "Coordination d'appellation et de rédaction de compétence, sans réouverture de délais ni dessaisissement d'une juridiction valablement saisie.",
                    "Aucun recours ni formalité supplémentaire.",
                    old_court, new_court)]))


old_appeal = "Les contestations des décisions prises en matière d'aides personnelles au logement et de primes de déménagement par les organismes payeurs doivent faire l'objet d'un recours administratif préalable devant l'organisme payeur qui en est l'auteur, selon des modalités fixées par voie réglementaire."
new_appeal = "Les contestations des décisions prises en matière d'aides personnelles au logement et de primes de déménagement par les organismes payeurs peuvent faire l'objet d'un recours administratif devant l'organisme payeur qui en est l'auteur, selon des modalités fixées par voie réglementaire."
p = f"<p>{new_appeal}</p><p>Ce recours est facultatif et ne conditionne pas la saisine de la juridiction compétente. Aucune décision de rejet d'un recours administratif n'est exigée avant cette saisine.</p><p>La suppression du caractère obligatoire du recours préalable s'applique aux recours contentieux introduits à compter de l'entrée en vigueur de la loi, y compris lorsqu'ils portent sur une décision antérieure. Elle ne rouvre aucun délai déjà expiré. Les recours administratifs engagés avant cette entrée en vigueur restent instruits et conservent leur régime de délai, sans nouvelle saisine de l'organisme payeur.</p>"
add('L825-2', p,
    "Réforme de fond : suppression du recours administratif préalable obligatoire, tout en gardant un recours administratif facultatif et gratuit dans son régime existant. L'accès direct au juge suffit à assurer le contrôle ; l'examen amiable demeure disponible sans être une condition supplémentaire de recevabilité. Aucune autre médiation ou notification de remplacement n'est imposée.",
    "R825-1 à R825-4 lus intégralement : R825-1 doit perdre la condition préalable et sa qualification obligatoire ; R825-2 conserve l'avis et la motivation pour les recours facultatifs ; R825-3 conserve la remise gracieuse, l'accusé sous quinze jours, décision sous deux mois et accès au juge déjà direct. L825-3 reste compétent pour les demandes effectivement présentées. Les règles générales des recours facultatifs et leurs effets de délai doivent être coordonnées avec CRPA/CJA hors du lot ; aucun délai de jugement raccourci n'est promis. Les RAPO déjà engagés gardent leur régime de délai ; les voies expirées ne renaissent pas. Les pénalités de fraude suivent la réserve juridictionnelle de L825-1.",
    impact('material_reduction',
            "La source impose un premier recours à l'organisme comme passage obligé ; cette charge procédurale est supprimée pour les nouvelles saisines du juge. La possibilité de règlement administratif reste disponible, sans nouvelle étape imposée.",
            "Les délais contentieux et les conditions générales de recevabilité ne sont pas abolis. R825-1 et les règles extérieures doivent être coordonnés ; la baisse de durée totale du litige et le coût net public ne sont pas mesurés.",
            "Aucune charge nouvelle n'est identifiée : ni médiation, attestation d'échec, registre ni délai d'attente n'est substitué au recours obligatoire. Le choix de saisir directement le juge peut modifier les volumes de contentieux, sans chiffrage de leur coût.",
            [effect('obligation_removed', 'aides-logement-recours-prealable-facultatif',
                    "Retrait du recours administratif comme condition d'accès au juge.",
                    "Contestation d'une décision d'aide ou de prime subordonnée à un recours administratif préalable obligatoire auprès de l'organisme payeur.",
                    "Recours administratif facultatif ; saisine directe de la juridiction compétente sans rejet préalable exigé.",
                    'legal_duty', "Personnes contestant les décisions d'aides personnelles au logement ou de primes de déménagement.",
                    "Saisines contentieuses à compter de l'entrée en vigueur, décisions anciennes incluses ; délais expirés non rouverts et recours administratifs en cours préservés.",
                    "Aucun recours de remplacement obligatoire ; délais généraux et compétence du juge maintenus.",
                    old_appeal, new_appeal)]),
    removed=["Obligation d'exercer un recours administratif préalable devant l'organisme payeur avant de pouvoir contester une décision d'aide personnelle au logement ou de prime de déménagement devant le juge."])


add('L825-3', None,
    "Maintien intégral nécessaire de l'autorité compétente pour statuer sur les contestations administratives et les remises gracieuses. Rendre le recours facultatif à L825-2 n'enlève pas son utilité lorsqu'il est choisi. La remise de dette est un avantage à conserver pour les situations futures, non une taxe ou une formalité inutile à abroger.",
    "R825-2 et R825-3 lus intégralement : l'avis de la commission de recours amiable, la motivation et les garanties de décision demeurent à leur champ. Les deux rubriques de L825-3 ne contiennent aucun renvoi exigeant encore un RAPO ; le 1° demeure donc cohérent avec le recours facultatif et le 2° avec la précarité de CSS L553-2. Aucune nouvelle demande n'est exigée pour les recours déjà déposés. La remise n'est pas transformée en droit à effacement général d'une dette frauduleuse.",
    impact('retained_necessary',
            "Les deux compétences du directeur restent intégrales, y compris la remise favorable. La suppression de la condition préalable est portée par L825-2 ; cet article n'en constitue pas une seconde réduction.",
            "Le maintien ne raccourcit pas les délais réglementaires de décision et n'accorde pas de remise automatique. La charge de traitement et le nombre de demandes après recours facultatif ne sont pas évalués.",
            "Aucune charge nouvelle n'est identifiée : aucune saisine obligatoire, avis supplémentaire ou nouvelle condition de remise n'est ajouté ; les demandes restent celles du dispositif existant."))


p = f"<p>Le présent article est abrogé pour les aides dues au titre des {MONTHS}.</p><p>Pour ces mois, les logements mentionnés aux 1° et 6° de l'article L. 831-1 peuvent ouvrir droit à l'aide personnalisée au logement quelle que soit la date de signature du prêt ou du contrat de location-accession. Le caractère neuf ou ancien du logement et sa présence ou son absence sur la liste de communes prévue par les dispositions antérieures du présent article ne peuvent plus, sur ce seul fondement, exclure l'aide. Les autres conditions relatives au logement, aux prêts, aux contrats, aux ressources et à l'occupation demeurent applicables.</p><p>Les droits à l'aide antérieurement ouverts, notamment pour les logements anciens relevant de la dérogation territoriale, sont préservés. Les prêts et contrats déjà signés qui n'ouvraient pas droit à l'aide du seul fait des restrictions supprimées peuvent ouvrir droit pour les mois nouveaux dans les mêmes conditions que les prêts et contrats futurs. {PAST}</p>"
add('L831-2', p,
    "Abrogation de fond des dates butoirs de l'APL accession et de leur sélection territoriale. La restriction fondée sur le 31 décembre 2017, assortie d'une ouverture limitée aux logements anciens sous conditions avant le 1er janvier 2020, est retirée ; les conditions de fond des prêts et contrats éligibles de L831-1 restent. La dérogation favorable devient comprise dans une ouverture générale pour les mois futurs, sans fermer les dossiers anciens admissibles.",
    "L831-1 et R831-1 lus intégralement : seuls les 1° et 6° sont concernés, pas tous les emprunts immobiliers ni les logements locatifs conventionnés. L831-1 comporte à ces deux endroits une réserve à L831-2 : ces réserves n'ont plus d'effet restrictif pour les mois nouveaux, la présente transition l'explicitant ; elles doivent être retirées dans le lot de L831-1, non modifié ici. La liste ministérielle perd son rôle d'exclusion pour l'avenir ; ses effets sur les mois anciens restent conservés. Les paramètres de liquidation accession ne sont pas inventés ; règlements, arrêtés et textes financiers sont à coordonner. Cette ouverture augmente potentiellement les dépenses d'aide et ne constitue ni une économie publique ni une baisse de droit de mutation. Aucun montant ou financement nouveau n'est chiffré.",
    impact('material_reduction',
            "La source ferme l'APL accession selon des dates de prêt et une exception territoriale limitée. Ces restrictions sont entièrement retirées pour les mois futurs, y compris pour les prêts actifs jusque-là exclus ; le régime de prêt éligible reste nécessaire.",
            "Tous les prêts ne deviennent pas éligibles : conditions des 1°/6° de L831-1 et du livre VIII conservées. La coordination des réserves de L831-1 et des textes d'application reste identifiée ; coût public de l'ouverture non établi et absence de rappel général sur les mois anciens.",
            "Aucune procédure, garantie, donnée ou agrément supplémentaire n'est ajouté à l'accédant ; les conditions préexistantes du prêt demeurent. L'ouverture crée potentiellement des demandes et versements publics supplémentaires dont le coût n'est pas chiffré.",
            [effect('relief_extended', 'apl-accession-fin-dates-butoirs',
                    "Réouverture prospective de l'APL accession sans la fermeture de 2017 ni l'exception territoriale expirée de 2020.",
                    "Prêts ou location-accession signés après le 31 décembre 2017 exclus, sauf logements anciens de certaines communes pour signatures avant le 1er janvier 2020.",
                    "Dates et liste communale non excluantes pour les mois nouveaux ; autres caractéristiques légales et réglementaires du prêt, contrat et ménage maintenues.",
                    'regime', "Propriétaires occupants et titulaires d'une location-accession relevant des 1° et 6° de L831-1.",
                    "Mois nouveaux ; prêts futurs et prêts déjà conclus jusque-là exclus couverts ; droits dérogatoires et calculs des mois antérieurs protégés.",
                    "Pas de nouveau prêt imposé, d'autorisation ou de dossier de remplacement ; coût accru des aides non évalué.",
                    "Les logements qui ont fait l'objet d'un prêt ou d'un contrat de location-accession mentionné au 1° ou au 6° de l'article L. 831-1 signé après le 31 décembre 2017 n'ouvrent pas droit à l'aide personnalisée au logement.",
                    "Pour ces mois, les logements mentionnés aux 1° et 6° de l'article L. 831-1 peuvent ouvrir droit à l'aide personnalisée au logement quelle que soit la date de signature du prêt ou du contrat de location-accession.")]),
    repeal="Fermeture de l'aide personnalisée au logement accession selon les dates de signature de 2017/2020, sélection par ancienneté du logement et liste de communes, pour les mois futurs ; aucune restriction de cette origine ne subsiste, droits et liquidations anciens conservés.")


add('L832-2', None,
    "Maintien intégral nécessaire de l'imputation de l'aide reçue par un tiers, de l'information du bénéficiaire et du reversement de l'excédent. Ces obligations protègent directement le locataire ou propriétaire contre la conservation indue d'une aide qui lui revient. Supprimer la mention ou le reversement réduirait un avantage et la transparence sans simplification légitime.",
    "Les trois alinéas gardent exactement leur champ : déduction du loyer et dépenses accessoires ou charges de remboursement ; information du bénéficiaire ; excédent du loyer et charges récupérables reversé à l'allocataire. Ce dernier critère n'est pas silencieusement remplacé par le montant total des dépenses accessoires. Aucun support d'information nouveau ni quittance distincte obligatoire n'est déduit de la source. L842-1 lu en entier contient la règle correspondante pour les allocations de logement, qui ne doit pas être confondue avec l'APL ni effacée par la présente conservation.",
    impact('retained_necessary',
            "La source oblige le tiers destinataire à déduire l'aide et reverser l'excédent, avec information du bénéficiaire ; ces protections restent intégrales. Aucun doublon matériel imposé par cet article n'est établi.",
            "Le maintien ne règle pas toutes les modalités des conventions de paiement et n'unifie pas les catégories de dépenses. Aucun gain monétaire supplémentaire ni coût administratif économisé n'est revendiqué.",
            "Aucune charge nouvelle n'est identifiée puisque le contenu est inchangé : aucun document distinct, registre, nouveau destinataire ou délai supplémentaire n'est créé ; les droits de déduction et reversement subsistent."))


p = f"<p>Le présent article est abrogé pour les aides dues au titre des {MONTHS}.</p><p>Pour ces mois, aucune diminution de l'aide personnalisée au logement ne peut être opérée au titre de la réduction de loyer de solidarité définie à l'article L. 442-2-1. Cette réduction de loyer et les droits qui s'y attachent demeurent applicables dans leur champ propre ; son montant n'est pas diminué du fait de la présente abrogation. Les autres règles de calcul de l'aide restent applicables.</p><p>{PAST} La présente abrogation n'entraîne ni restitution générale des diminutions légalement appliquées aux mois anciens ni remise en cause des droits à la réduction de loyer de solidarité.</p>"
add('L832-3', p,
    "Abrogation de fond de la minoration d'APL absorbant une fraction de la réduction de loyer de solidarité. Le prélèvement sur l'avantage de logement, de 90 % à 98 % de cette réduction selon la source, est supprimé pour les mois nouveaux. La réduction de loyer elle-même est expressément préservée, y compris pour les futures situations éligibles ; aucun taux intermédiaire, nouvelle taxe ou hausse de loyer compensatrice n'est créé.",
    "L442-2-1 lu intégralement, deux tableaux et notes compris : périmètre HLM, exception des logements-foyers, ressources, plafonds de réduction, indexations, zonage et mention sur quittance demeurent. La fraction réglementaire actuellement appliquée n'est pas inventée : seule la fourchette légale 90 %-98 % est constatée. Retirer pour les mois nouveaux les dispositions réglementaires/arrêtés qui appliquent cette minoration ; ne pas supprimer la RLS à cette occasion. Les recettes des bailleurs, le budget de l'APL et les transferts doivent être évalués séparément : cette suppression peut accroître l'aide payée, ce n'est pas une économie nationale. Les mois anciens gardent liquidations, indus, restitutions et recours sans restitution générale.",
    impact('material_reduction',
            "La source retranche de l'APL une fraction légale de 90 % à 98 % du montant de RLS. Cette retenue est supprimée pour les mois futurs et la RLS est maintenue sans diminution compensatrice ; le bénéfice net peut donc augmenter.",
            "La fraction n'est pas un taux d'impôt sur le revenu ni un taux d'APL appliqué au loyer total. Les autres paramètres du barème restent en vigueur ; l'impact budgétaire et individuel dépend des dossiers et n'est pas chiffré.",
            "Aucune charge nouvelle de déclaration, de justification, de taux fiscal ou de condition d'aide n'est créée. La suppression de la retenue accroît potentiellement les prestations publiques ; ce coût n'est pas compensé ni déclaré autofinancé.",
            [effect('relief_extended', 'apl-fin-minoration-reduction-loyer-solidarite',
                    "Retrait de la retenue d'APL liée à la RLS sans supprimer la réduction de loyer.",
                    "APL diminuée d'une fraction comprise entre 90 % et 98 % du montant de RLS, pour ses bénéficiaires ; fraction exacte réglementaire non affirmée.",
                    "Aucune minoration d'APL au titre de la RLS ; montant et conditions propres de la réduction de loyer conservés ; autres règles d'APL inchangées.",
                    'percent', "Bénéficiaires d'APL concernés par la réduction de loyer de solidarité de L442-2-1.",
                    "Mois nouveaux après entrée en vigueur, droits en cours inclus ; diminutions légalement appliquées aux mois anciens non remboursées de façon générale.",
                    "Ni taxe ni minoration de loyer de remplacement ; augmentation possible du coût public de l'APL non chiffrée.",
                    "Le montant de l'aide personnalisée au logement est diminué, pour les bénéficiaires concernés par la réduction de loyer de solidarité définie à l'article L. 442-2-1, à hauteur d'une fraction de cette réduction comprise entre 90 % et 98 %.",
                    "Pour ces mois, aucune diminution de l'aide personnalisée au logement ne peut être opérée au titre de la réduction de loyer de solidarité définie à l'article L. 442-2-1.")]),
    repeal="Minoration de l'APL correspondant à 90 % à 98 % de la réduction de loyer de solidarité et habilitation à fixer cette fraction pour les mois nouveaux ; maintien entier de la réduction de loyer, de ses avantages futurs et des situations relatives aux mois antérieurs.")


assert set(ANSWERS) == set(BY_NUMBER)
out = [ANSWERS[s['number']] for s in SOURCES]
(ROOT / 'answer.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json: {len(out)} articles')
