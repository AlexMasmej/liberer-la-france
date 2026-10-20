import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
references = json.loads(Path('reference-targets.json').read_text())
by_number = {article['number']: article for article in sources}
answers = {}


def impact(classification, assessment, limitations, burdens, effects=None):
    return {
        'version': 1,
        'classification': classification,
        'assessment': assessment,
        'scope_limitations': limitations,
        'new_burdens_review': burdens,
        'effects': effects or [],
    }


def effect(kind, measure, description, before, after, unit, population, transition,
           burdens, source_quote, proposed_quote):
    return dict(
        kind=kind, measure_id=measure, description=description,
        before=before, after=after, unit=unit, affected_population=population,
        conditions_and_transition=transition,
        replacement_or_new_burdens=burdens,
        source_quote=source_quote, proposed_quote=proposed_quote,
    )


def base(number):
    source = by_number[number]
    return {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}


def retain(number, reason, notes, assessment, limitations, burdens, benefit=None):
    item = base(number)
    item.update(
        proposed_xml=None, reason=reason, review_notes=notes,
        status='retained_unchanged', classification='retained_necessary',
        substantive_impact=impact('retained_necessary', assessment, limitations, burdens),
        reference_checks=[],
    )
    if benefit:
        item['benefit_review'] = benefit
    answers[number] = item


def rewrite(number, xml, reason, notes, assessment, limitations, burdens,
            effects, removed=None, benefit=None, classification='material_reduction',
            repeal_scope=None):
    item = base(number)
    item.update(
        proposed_xml=xml, reason=reason, review_notes=notes, status='rewrite_draft',
        substantive_impact=impact(classification, assessment, limitations, burdens, effects),
        reference_checks=[],
    )
    if repeal_scope:
        item.update(change_type='full_repeal',
                    repeal_policy_id='editorial_direction_2026_10_19',
                    repeal_scope=repeal_scope)
    else:
        item.update(change_type='normative_reduction',
                    reform_policy_id='editorial_direction_2026_10_19',
                    removed_provisions=removed)
    if benefit:
        item['benefit_review'] = benefit
    answers[number] = item


rewrite(
    'L2314-21',
    """<p>Dans les entreprises de portage salarial, les conditions d'ancienneté sont, pour les salariés en portage salarial, de trois mois pour être électeur et de six mois pour être éligible.</p>
<p>Ces conditions sont appréciées en totalisant les périodes pendant lesquelles ces salariés ont été liés à ces entreprises par des contrats de travail au cours des douze mois ou des dix-huit mois précédant l'élection, selon qu'il s'agit d'électorat ou d'éligibilité. Les périodes sans prestation de portage salarial pendant lesquelles le contrat de travail subsiste sont comprises dans ce calcul.</p>
<p>Ce délai est réduit à six mois en cas de création d'entreprise ou d'ouverture d'établissement.</p>
<p>Ces dispositions s'appliquent aux listes confectionnées à compter de l'entrée en vigueur de la loi portant la présente rédaction. Elles prennent en compte les périodes d'emploi antérieures comprises dans les périodes de référence ; la conversion d'un contrat en contrat unique ne remet pas à zéro l'ancienneté acquise. Les opérations électorales antérieures et les recours qui s'y rapportent restent soumis aux règles qui leur étaient applicables. La prise en compte d'un contrat antérieur n'autorise aucune nouvelle embauche ni aucun renouvellement à durée déterminée après l'entrée en vigueur de la loi instituant le contrat de travail unique.</p>""",
    "Réforme de fond : l'ancienneté électorale du salarié porté n'est plus limitée aux seules périodes de prestation. Toute période couverte par le contrat, y compris sans prestation, entre dans les mêmes fenêtres de référence. Les seuils de trois et six mois, la totalisation, les fenêtres de douze et dix-huit mois et la règle favorable de six mois à la création ou à l'ouverture restent maintenus. Cette extension de droits électoraux accompagne l'emploi à durée indéterminée ; elle ne crée ni rémunération générale des périodes sans prestation ni régime nouveau de rupture.",
    "Coordination avec L2314-24 du lot : une prestation en cours n'est plus exigée lors de la confection des listes. Le dernier alinéa substantiel de la source dit seulement « Ce délai » ; cette formulation est conservée, sans lui attribuer silencieusement un autre objet. L'articulation des deux fenêtres de référence avec leur réduction à six mois demeure à préciser dans la coordination générale, sans supprimer cette réduction favorable. Les dérogations d'ancienneté de L2314-25 restent ouvertes. Lecture complémentaire de L1254-19 à L1254-21 dans le corpus : le II de L1254-21 laisse les périodes sans prestation non rémunérées ; aucun changement de cette règle n'est opéré ici. Les notes de 2017/2018 ne fixent pas l'entrée en vigueur du projet. Les trois cibles imposées sont analysées ci-dessous, sans renvoi normatif nouveau à ces articles.",
    "Par rapport à la source officielle entière, la restriction aux périodes de prestations effectivement réalisées est retirée. Des périodes d'emploi sans prestation peuvent désormais ouvrir plus tôt le vote ou l'éligibilité, sans abaissement des seuils ni remise à zéro des périodes anciennes. Il s'agit d'un allègement d'une condition électorale, pas d'une baisse de cotisations ni d'un coût patronal chiffré.",
    "Seules les périodes où le contrat subsiste sont ajoutées : les intervalles sans contrat ne deviennent pas de l'ancienneté. Les règles d'âge, d'incompatibilité et les autres conditions électorales ne sont pas supprimées. Le nombre de bénéficiaires et le coût de mise à jour des listes ne sont pas établis ; aucune économie globale n'est revendiquée.",
    "Aucun registre, justificatif, déclaration ni délai nouveau n'est identifié : les dates d'emploi servent au calcul déjà nécessaire. L'élargissement du corps électoral peut modifier les listes à établir selon les obligations existantes ; son coût net n'est pas mesuré. Aucune rémunération nouvelle des périodes sans prestation n'est instituée.",
    [effect(
        'relief_extended', 'portage-droits-electoraux-sans-prestation',
        "Prise en compte des périodes d'emploi sans prestation dans l'ancienneté électorale des salariés portés.",
        "Trois mois pour voter et six mois pour être éligible, calculés sur les périodes de prestations au cours des douze ou dix-huit mois précédant l'élection ; réduction de référence à six mois dans les cas prévus.",
        "Mêmes seuils et fenêtres, mais les périodes sans prestation couvertes par un contrat de travail sont aussi totalisées ; aucune période sans contrat ajoutée.",
        'legal_duty', "Salariés portés liés à une entreprise de portage, notamment ceux dont l'emploi se poursuit entre deux prestations.",
        "Listes confectionnées après l'entrée en vigueur de la nouvelle rédaction ; périodes antérieures incluses dans les fenêtres conservées ; anciens scrutins et recours protégés.",
        "Pas de déclaration de remplacement ; calcul sur les périodes d'emploi, sans garantie de salaire pour l'absence de prestation ni nouveau CDD.",
        "Ces conditions sont appréciées en totalisant les périodes pendant lesquelles ces salariés ont effectué des prestations de portage salarial dans le cadre de contrats de travail conclus avec ces entreprises au cours des douze mois ou des dix-huit mois précédant l'élection, selon qu'il s'agit d'électorat ou d'éligibilité.",
        "Les périodes sans prestation de portage salarial pendant lesquelles le contrat de travail subsiste sont comprises dans ce calcul.",
    )],
    removed=["La restriction du calcul de l'ancienneté électorale aux seules périodes de prestations, qui excluait les périodes sans prestation couvertes par un contrat de travail."],
)


retain(
    'L2314-23',
    "Maintien intégral utile : le texte organise le rattachement électoral des salariés mis à disposition sans leur imposer un double vote. Le choix entre employeur et utilisateur reste une faculté favorable, tandis que douze mois continus assurent un rattachement durable à l'utilisateur. L'inéligibilité chez celui-ci conserve la distinction avec la représentation chez l'employeur. Aucun agrément, dépôt ou justificatif supplémentaire n'est institué par cet article ; sa suppression retirerait le droit d'option sans simplifier le contrat de travail.",
    "Le renvoi au 2° de L1111-2 vise la mise à disposition par une entreprise extérieure et ses conditions propres, non tous les salariés mentionnés dans cette subdivision. La cible fournie conserve cette catégorie, même avec des emplois à durée indéterminée. Le texte n'impose pas de CDD et ne confond pas douze mois de présence électorale avec l'ancienneté d'indemnisation de rupture. Le traitement des remplacements dans l'effectif de L1111-2 ne doit pas être réécrit ici en règle nouvelle de vote. Les trois autres cibles imposées concernent le contrat ou sa rupture, sans renvoi direct dans la source.",
    "La source entière reste inchangée : douze mois continus chez l'utilisateur, absence d'éligibilité chez lui et libre choix du lieu de vote dans les conditions existantes. Aucune réduction nouvelle n'est comptée ; le droit d'option et la cohérence de la représentation justifient le maintien.",
    "La règle ne vaut que pour la mise à disposition relevant du renvoi existant, sans extension à tous les contrats uniques, aux agents publics ou aux seuls contrats de mission. La charge d'organisation des scrutins n'est pas évaluée et les règles de calcul des effectifs restent celles de leur article propre.",
    "Aucune charge nouvelle n'est identifiée puisque le corps source est maintenu sans formulaire, attestation ou nouvelle notification. Le choix électoral existant demeure nécessaire pour éviter le double exercice du vote ; il n'est pas transformé en une autorisation.",
)


rewrite(
    'L2314-24',
    """<p>Dans les entreprises de portage salarial, sont électeurs ou éligibles tous les salariés en portage salarial satisfaisant aux conditions d'ancienneté définies par l'article L. 2314-21 et liés à l'entreprise par un contrat de travail au moment de la confection des listes, y compris lorsqu'ils n'effectuent alors aucune prestation de portage.</p>
<p>Ces dispositions s'appliquent aux listes confectionnées à compter de l'entrée en vigueur de la loi portant la présente rédaction. Les opérations électorales antérieures et les recours qui s'y rapportent restent soumis aux règles qui leur étaient applicables. Le maintien des droits électoraux pendant une période sans prestation suppose que le contrat de travail subsiste ; il ne rétablit aucun contrat déjà rompu et n'autorise aucune nouvelle embauche ni aucun renouvellement à durée déterminée après l'entrée en vigueur de la loi instituant le contrat de travail unique.</p>""",
    "Coordination nécessaire de fond avec L2314-21 : la condition d'une prestation en cours lors de la confection des listes est retirée. Le rattachement repose sur le contrat encore en vigueur, ce qui permet au salarié porté entre deux prestations d'exercer les droits issus du calcul élargi d'ancienneté. Le renvoi à L2314-21 et le rattachement à l'entreprise sont maintenus ; aucune durée de mission ne met fin à l'emploi ni aux droits électoraux tant que le contrat subsiste.",
    "Même mesure que L2314-21 : ne pas compter cette coordination comme une seconde extension indépendante. Le renvoi conserve son objet exact, les seuils de trois et six mois, les fenêtres de douze et dix-huit mois et la règle favorable de six mois. Les autres conditions d'électorat et d'éligibilité restent à leur champ propre. Les cibles L1234-1 et L1234-9 ne sont pas des règles de radiation pendant une prestation interrompue : seule une rupture effective peut mettre fin au rattachement contractuel. La rédaction ne crée pas de rémunération d'une période sans prestation et ne valide aucun nouveau CDD.",
    "La source officielle exigeait une prestation au moment précis des listes. La proposition retire cette condition pour rendre effectif le maintien des droits entre prestations prévu dans la mesure de L2314-21. Cette exécution de la même mesure est classée coordination_only et n'est pas additionnée comme un allègement autonome.",
    "Le salarié doit toujours être lié à l'entreprise et remplir l'ancienneté requise ; les anciens contrats rompus ne revivent pas. L'extension concerne les listes futures, y compris pour un contrat antérieur encore valable, sans rouvrir les scrutins passés. Aucun gain financier ou effet sur tous les salariés du code n'est démontré.",
    "Aucune charge nouvelle de déclaration, de preuve ou de registre n'est identifiée : le contrat en cours remplace le contrôle d'une prestation à la date des listes. L'éventuelle augmentation du nombre d'inscrits relève de l'extension coordonnée de droits électoraux et n'est pas présentée comme une économie administrative chiffrée.",
    [effect(
        'coordination', 'portage-droits-electoraux-sans-prestation',
        "Coordination du rattachement lors des listes avec la prise en compte des périodes sans prestation de L2314-21.",
        "Le salarié porté doit, outre l'ancienneté requise, effectuer une prestation au moment de la confection des listes.",
        "L'ancienneté reste requise ; un contrat en cours suffit au rattachement même sans prestation à cette date.",
        'legal_duty', "Salariés portés ayant l'ancienneté requise et un contrat en cours lors des listes, mais sans prestation à cet instant.",
        "Application aux nouvelles listes ; scrutins antérieurs et recours préservés, contrats déjà rompus non rétablis, aucun nouveau CDD permis.",
        "Aucun agrément ni déclaration de remplacement ; les règles de rémunération et de rupture restent distinctes.",
        "et effectuant au moment de la confection des listes une prestation de portage dans le cadre d'un contrat de travail conclu avec l'entreprise.",
        "et liés à l'entreprise par un contrat de travail au moment de la confection des listes, y compris lorsqu'ils n'effectuent alors aucune prestation de portage.",
    )],
    removed=["L'exigence d'effectuer une prestation de portage à la date de confection des listes, alors même que le salarié reste lié à l'entreprise par son contrat de travail."],
    classification='coordination_only',
)


rewrite(
    'L2314-25',
    """<p>Les conditions d'ancienneté pour être électeur sont écartées de plein droit lorsque leur application aurait pour effet de réduire à moins des deux tiers de l'effectif le nombre de salariés remplissant ces conditions. Cette dispense s'applique sans autorisation ni déclaration préalable. Dans les autres cas, l'inspecteur du travail peut, après avoir consulté les organisations syndicales représentatives dans l'entreprise, autoriser des dérogations aux conditions d'ancienneté pour être électeur.</p>
<p>Les conditions d'ancienneté pour l'éligibilité sont écartées de plein droit lorsque leur application conduirait à une réduction du nombre des candidats qui ne permettrait pas l'organisation normale des opérations électorales. Cette dispense s'applique sans autorisation ni déclaration préalable.</p>
<p>La décision de l'autorité administrative peut faire l'objet d'un recours devant le juge judiciaire, à l'exclusion de tout autre recours administratif ou contentieux. Les contestations relatives à l'application des dispenses de plein droit relèvent également du juge judiciaire.</p>
<p>Les dispenses prévues aux deux premiers alinéas ne concernent que l'ancienneté ; les autres conditions d'électorat et d'éligibilité demeurent applicables. Elles s'appliquent aux listes confectionnées à compter de l'entrée en vigueur de la loi portant la présente rédaction, sans nouvelle demande pour les situations qui les remplissent. Les dérogations déjà accordées conservent leurs effets. Les opérations électorales antérieures et les recours qui s'y rapportent restent soumis aux règles qui leur étaient applicables.</p>""",
    "Réforme de fond : les deux situations où la dérogation évite un corps électoral insuffisant ou une impossibilité d'organiser normalement les élections deviennent des dispenses légales d'ancienneté. L'autorisation de l'inspecteur et la consultation syndicale préalable qui la conditionnait disparaissent dans ces cas, sans déclaration de remplacement. La possibilité plus large de dérogation à l'électorat hors du cas des deux tiers est conservée avec consultation syndicale. Le contrôle judiciaire et les autres conditions électorales demeurent ; le bénéfice de la dérogation n'est pas fermé aux futurs salariés.",
    "Le seuil est strictement moins des deux tiers de l'effectif, et non deux tiers des votants ni une majorité de validation. Le second critère conserve l'impossibilité d'une organisation normale due au nombre de candidats, sans nombre nouveau inventé. Les conditions d'âge et les incompatibilités ne sont pas levées. R2314-4 lu dans le corpus : son délai de quinze jours suivant notification reste pertinent pour les décisions administratives résiduelles ; les dispenses légales ne sont pas soumises à cette notification ni à un nouveau délai d'attente. R2314-24 et R2314-25, lus intégralement, régissent les contestations judiciaires dans leur champ propre ; leur rédaction doit distinguer les dispenses sans décision administrative si une coordination réglementaire est nécessaire. Aucun de ces délais ne correspond au préavis de rupture. Aucun renvoi normatif nouveau à une cible non fournie n'est ajouté.",
    "La source subordonne les dérogations à une autorisation après consultation. La proposition retire effectivement ce circuit dans les deux situations expressément identifiées par la source, tout en maintenant la voie favorable d'électorat dans les autres cas et le recours au juge. La réduction démontrée porte sur l'autorisation préalable et sa consultation accessoire, sans réduction fiscale alléguée.",
    "L'autorisation demeure pour les autres dérogations à l'électorat, car supprimer cette faculté fermerait un avantage existant. Les exigences d'ancienneté subsistent hors dispenses et les autres critères électoraux restent applicables. Le volume de dossiers évités, les coûts et le solde de complexité ne sont pas chiffrés.",
    "Aucune charge nouvelle de déclaration, attestation, registre ou attente n'est identifiée : les circonstances déjà prévues par la source produisent désormais directement la dispense. Leur éventuel contrôle est judiciaire, sans saisine obligatoire nouvelle. La consultation syndicale reste limitée à la voie administrative résiduelle déjà existante.",
    [effect(
        'authorization_removed', 'cse-dispenses-anciennete-de-plein-droit',
        "Suppression de l'autorisation et de la consultation préalable pour les dispenses d'ancienneté dans les deux situations légales.",
        "Dérogations d'électorat, notamment sous le seuil de deux tiers de l'effectif, et d'éligibilité en cas d'organisation normale impossible : autorisation de l'inspecteur après consultation syndicale.",
        "Dans ces deux situations, dispense légale sans autorisation ni déclaration ; les autres dérogations d'électorat restent accessibles à l'inspecteur après consultation.",
        'legal_duty', "Salariés, candidats et entreprises dont les conditions d'ancienneté réduisent excessivement le corps électoral ou empêchent l'organisation normale des élections.",
        "Nouvelles listes après entrée en vigueur ; dérogations déjà accordées, autres conditions électorales et recours conservés.",
        "Aucun agrément, déclaration ou justificatif de substitution ; recours au juge maintenu sans saisine préalable obligatoire.",
        "L'inspecteur du travail peut, après avoir consulté les organisations syndicales représentatives dans l'entreprise, autoriser des dérogations aux conditions d'ancienneté pour être électeur, notamment lorsque leur application aurait pour effet de réduire à moins des deux tiers de l'effectif le nombre de salariés remplissant ces conditions.",
        "Les conditions d'ancienneté pour être électeur sont écartées de plein droit lorsque leur application aurait pour effet de réduire à moins des deux tiers de l'effectif le nombre de salariés remplissant ces conditions. Cette dispense s'applique sans autorisation ni déclaration préalable.",
    )],
    removed=[
        "L'autorisation de l'inspecteur du travail et sa consultation syndicale préalable pour la dérogation à l'ancienneté électorale lorsque moins des deux tiers de l'effectif rempliraient cette condition.",
        "L'autorisation de l'inspecteur du travail et sa consultation syndicale préalable pour la dérogation à l'ancienneté d'éligibilité quand le nombre de candidats empêche l'organisation normale du scrutin.",
    ],
    benefit="Les deux avantages possibles sont les dérogations d'ancienneté pour voter et pour être candidat. Le cas de l'électorat sous les deux tiers et celui de l'éligibilité insuffisante deviennent des dispenses de plein droit pour toutes les listes futures éligibles. La faculté plus large d'obtenir une dérogation d'électorat dans les autres situations reste ouverte auprès de l'inspecteur après consultation syndicale. Les dérogations déjà accordées et le recours judiciaire demeurent. La consultation retirée dans les cas automatiques ne supprime pas le bénéfice de la dérogation : elle cesse précisément d'en conditionner l'accès.",
)


retain(
    'L2314-26',
    "Maintien intégral à droit constant : le secret du vote et les votes distincts des titulaires et suppléants dans chaque collège garantissent la sincérité des mandats. Le vote électronique est déjà une possibilité, y compris par décision de l'employeur à défaut d'accord ; le texte n'impose ni autorisation individuelle ni double dépôt. Supprimer le secret, les collèges ou la séparation des mandats retirerait une protection électorale plutôt qu'une formalité redondante.",
    "Les trois phrases et leurs champs sont conservés. Les garanties techniques ne sont pas assimilées à une autorisation administrative. R2314-16 lu dans le corpus protège les émargements et l'absence de résultats partiels, ainsi que l'ordre des opérations si les deux modes coexistent. La suppression du plafond des réunions en visioconférence de L2315-4 ne modifie ni ce scrutin électoral ni son décret après avis de la CNIL.",
    "Aucun changement réel n'est introduit par rapport à la source entière : scrutin secret, option électronique existante et votes séparés sont conservés comme garanties nécessaires. Aucune autorisation ou formalité nouvelle supprimée n'est comptée.",
    "Le maintien concerne l'élection du CSE, sans étendre ses règles aux consultations d'accords collectifs ni confondre vote électronique et simple visioconférence. Les coûts des solutions techniques et la conformité de chaque logiciel ne sont pas évalués.",
    "Aucune charge nouvelle n'est identifiée : le texte source reste intact et n'impose ni outil numérique obligatoire, ni abonnement, ni transmission supplémentaire. Les garanties et options existantes ne deviennent pas une nouvelle procédure.",
)


retain(
    'L2314-27',
    "Maintien intégral utile : tenir l'élection pendant le travail permet l'exercice effectif du vote, et l'accord unanime des organisations représentatives conserve une dérogation praticable, notamment en travail continu. L'unanimité protège l'accès au scrutin lorsqu'il est déplacé hors du temps de travail ; elle n'est pas un agrément administratif ni une formalité doublonnée.",
    "Conserver l'ensemble des organisations syndicales représentatives, sans remplacer cette assiette par la majorité de L2314-6 ou par celles des accords d'entreprise. La dérogation vaut également pour de futures organisations du travail continu. La règle n'est ni un préavis de quinze jours ni une durée minimale d'emploi.",
    "La source entière est maintenue : principe de l'élection pendant le travail et exception par accord unanime. La participation électorale et la dérogation d'organisation justifient ce maintien ; aucun allègement nouveau n'est déclaré.",
    "Le texte ne règle pas à lui seul la rémunération de toutes les situations de vote ni les autres modalités du protocole préélectoral. Aucun coût ou effet national n'est chiffré ; la dérogation existante n'est pas présentée comme une suppression nouvelle.",
    "Aucune charge nouvelle n'est identifiée, car ni accord supplémentaire ni notification ou registre nouveau n'est créé. L'accord requis pour déroger reste celui déjà prévu dans la source.",
)


retain(
    'L2314-28',
    "Maintien intégral : la négociation des modalités du scrutin sous la majorité de L2314-6 et le respect des principes électoraux assurent le consentement collectif et la sincérité du vote. Le juge peut régler les points non convenus ; aucune approbation administrative ne s'ajoute à l'accord. Supprimer ce mécanisme transférerait les garanties vers une procédure à inventer sans doublon démontré.",
    "L2314-6 a été lu dans le corpus : majorité des organisations ayant participé, comprenant celles représentatives ayant recueilli la majorité des suffrages, ou majorité des représentatives si ces résultats ne sont pas disponibles. Ces assiettes ne sont pas celles des voies de négociation de L2232. Le présent maintien ne rétablit aucune transmission CPPNI ni aucun délai de négociation supprimé par coordination.json. Aucun renvoi nouveau n'est ajouté.",
    "Aucun nouveau corps n'est nécessaire après comparaison de la source entière. La règle d'accord et le recours judiciaire subsidiaire sont maintenus pour leur fonction électorale essentielle ; ils ne constituent pas une autorisation à supprimer ni une simplification nouvelle.",
    "Les règles des accords collectifs et leurs délais distincts ne sont pas modifiés ici. L'absence de doublon démontré porte sur ce mécanisme précis, sans valider l'ensemble des formalités électorales réglementaires ni leur coût.",
    "Aucune charge nouvelle n'est identifiée : les deux règles sources sont reprises par maintien, sans protocole supplémentaire, délai d'attente ou nouvelle pièce imposée.",
)


retain(
    'L2314-29',
    "Maintien intégral : la proportionnelle, les deux tours, le quorum du premier tour et le traitement des ratures déterminent les élus et la représentativité. La communication des procès-verbaux aux syndicats candidats et négociateurs leur permet de connaître les résultats et d'exercer leurs recours. Elle est déjà ouverte par tout moyen ; aucune deuxième transmission des mêmes destinataires ou rapport supplémentaire n'est établi dans cet article. Retirer cette information essentielle n'est pas justifié par la seule recherche d'un allègement.",
    "L2314-5, premier et deuxième alinéas, a été lu intégralement dans le corpus : le renvoi identifie les organisations invitées et habilitées à présenter des listes au premier tour, et ne renvoie pas aux délais de ses alinéas suivants. Conserver la moitié des inscrits, quinze jours pour le second tour, le seuil strictement inférieur à 10 % de ratures et l'ordre de présentation. Quinze jours est ici un délai électoral maximal, distinct du préavis individuel. Les envois à d'autres destinataires sur d'autres fondements ne sont pas réputés supprimés.",
    "La source entière reste inchangée : ses cinq alinéas règlent la détermination et la publicité utile des résultats. Aucun prélèvement ni doublon autonome à retirer n'est démontré ici ; aucun gain nouveau n'est compté.",
    "L'article ne décrit pas toutes les hypothèses de second tour ou tous les dépôts réglementaires des procès-verbaux. Leur exhaustivité n'est pas affirmée. Aucun coût de communication ou d'organisation des tours n'est chiffré.",
    "Aucune charge nouvelle n'est identifiée : les mêmes procès-verbaux, destinataires et liberté de moyen restent en place, sans déclaration, support ou délai additionnel créé.",
)


retain(
    'L2314-30',
    "Maintien intégral : les règles de proportion et d'alternance protègent l'accès des femmes et des hommes aux mandats. Elles ne constituent ni taxe, agrément ni justificatif redondant. Les règles d'arrondi, le siège impair en égalité stricte et la possibilité d'un candidat du sexe autrement exclu limitent les effets excessifs de cette contrainte et doivent rester ouvertes aux futures listes éligibles. Aucune suppression compatible avec la protection contre la discrimination n'est retenue dans ce texte.",
    "Conserver les deux phrases du premier alinéa : L2314-32 les vise séparément pour les sanctions de proportion et de positionnement. Les 1° et 2°, le chiffre 5 de la décimale tel qu'il figure dans la source, l'impossibilité de placer en tête le candidat dérogatoire et l'application distincte aux titulaires et suppléants sont maintenus sans réinterprétation silencieuse de la formulation de l'arrondi. L2314-29, présent dans le lot, reste intact.",
    "La norme officielle entière est maintenue pour la représentation équilibrée, avec toutes ses souplesses. Les calculs et alternances restent nécessaires à cette protection ; aucune réduction nouvelle n'est revendiquée.",
    "Le maintien ne vaut pas étude empirique des effets de la parité sur chaque liste et ne modifie pas les règles judiciaires d'application des arrondis. Aucun nouveau quota de logement ni règle SRU n'a de rapport avec ce mécanisme électoral.",
    "Aucune charge nouvelle n'est identifiée puisque les mêmes calculs, dérogations et listes restent applicables. Aucun certificat de parité, dépôt additionnel ou autorisation préalable n'est ajouté.",
)


retain(
    'L2314-31',
    "Maintien intégral utile : l'information sur la proportion de femmes et d'hommes de chaque collège rend applicables les règles de composition des candidatures et permet leur contrôle. La date certaine garantit l'information des salariés ; le choix de tout moyen évite déjà l'imposition d'un courrier ou support exclusif. Cette information unique n'est pas identifiée comme un doublon dispensable.",
    "Le fait déclencheur reste l'accord ou la décision de répartition du personnel, sans ajouter un délai chiffré ni un envoi à une administration. L2314-30 et ses exceptions, ainsi que le recours de L2314-32, sont maintenus dans le même lot ; retirer la donnée nécessaire à leur application les rendrait moins effectifs.",
    "La source entière demeure nécessaire à la préparation de listes conformes et au contrôle de l'équilibre des candidatures. Aucun changement normatif, aucune transmission supprimée ni baisse de coûts n'est compté.",
    "L'article ne détermine pas la méthode de répartition du personnel et ne justifie pas de nouvelles données individuelles. La charge de l'information existante n'est pas mesurée et aucun bilan global de simplification n'en est déduit.",
    "Aucune charge nouvelle n'est identifiée : la seule information collective déjà prévue reste donnée par tout moyen à date certaine, sans fichier nominatif ni justificatif nouveau.",
)


retain(
    'L2314-32',
    "Maintien intégral : le juge judiciaire assure les recours électoraux et le contrôle de la représentation équilibrée. La prise en charge par l'État des mesures d'instruction indispensables est une garantie d'accès au juge. Les annulations ciblées sanctionnent les seules élections concernées au lieu d'anéantir indistinctement le scrutin. Ni cette garantie financière ni les recours ne sont des charges administratives à supprimer.",
    "Les cinq alinéas sont conservés. L2314-30, lu dans le lot, garde l'ordre des deux phrases visées au premier alinéa ; le nombre d'élus surnuméraires, l'ordre inverse et la sanction de positionnement ne sont pas fusionnés. L2314-10 a été lu intégralement dans le corpus : absence de représentation d'un collège ou réduction de moitié des titulaires, exception à moins de six mois du terme, sièges vacants et mandat restant à courir. Le recours contre les décisions résiduelles de L2314-25 et les contestations des dispenses légales demeurent judiciaires. R2314-24 et R2314-25 ont été lus pour leurs délais propres, sans les confondre avec une rupture d'emploi.",
    "La comparaison à la source officielle entière conduit à un maintien nécessaire : compétences du juge, frais d'instruction supportés par l'État et sanctions proportionnées de listes irrégulières sont conservés. Aucun allègement financier ou procédural nouveau n'est attribué à ce maintien.",
    "La prise en charge ne couvre que la mesure d'instruction indispensable, pas tous les frais de tout litige. Les délais réglementaires et les autres droits de recours restent à leur champ ; aucune validation du traitement de cas individuels n'est donnée.",
    "Aucune charge nouvelle n'est identifiée, car aucun recours obligatoire supplémentaire, nouvelle pièce ou dépense transférée aux parties n'est créé. La charge étatique existante des mesures indispensables est maintenue.",
    benefit="L'avantage explicite est la prise en charge par l'État des dépenses de la mesure d'instruction rendue indispensable par une contestation électorale : il reste intégralement applicable aux futures instances éligibles. La compétence judiciaire et les annulations limitées aux élus surnuméraires ou mal positionnés préservent également les recours et les autres mandats. Aucun de ces droits n'est fermé aux situations nouvelles, et le renvoi aux élections partielles conserve son exception favorable à moins de six mois du terme.",
)


retain(
    'L2314-33',
    "Maintien intégral utile : le mandat de quatre ans donne une durée stable à la représentation et ses causes de fin correspondent à la disparition du titulaire ou du lien représentatif. Le maintien du mandat lors d'un changement de catégorie évite une déchéance et de nouvelles opérations inutiles. Le texte source récent ne contient pas de limitation du nombre de mandats successifs ; aucune règle ancienne n'est réintroduite.",
    "La source est valable depuis le 26 octobre 2025 : ne pas reconstituer les alinéas de versions antérieures. La rupture du contrat ne met fin aux fonctions qu'avec ses effets légaux, et la fin d'une mission ou d'une formation ne devient pas la rupture du contrat unique. Les autorisations et protections de représentants restent distinctes du préavis de quinze jours. L2314-34 conserve la dérogation conventionnelle de deux à quatre ans.",
    "La source entière est maintenue sans ajout : durée de quatre ans, causes de fin et maintien en cas de changement de catégorie. Aucune formalité récurrente ni limitation supplémentaire n'est créée ou supprimée ; la continuité de représentation justifie le maintien.",
    "Le texte ne fixe pas les procédures de rupture d'un salarié protégé ni les conditions de fin des anciens CDD. Ces régimes ne sont pas abolis par une cause de fin de mandat. Aucun effet financier ou diminution de fréquence d'élections n'est chiffré.",
    "Aucune charge nouvelle n'est identifiée : le mandat existant et les faits qui y mettent fin restent les mêmes, sans nouvelle déclaration ni limitation des mandats successifs.",
)


retain(
    'L2314-34',
    "Maintien intégral de la dérogation favorable : la branche, le groupe ou l'entreprise peut adapter la durée du mandat entre deux et quatre ans au lieu d'appliquer uniformément quatre ans. Supprimer cette faculté imposerait une contrainte uniforme supplémentaire. L'accord reste nécessaire au choix de cette dérogation ; il ne constitue pas un agrément public ni une obligation de renégociation périodique.",
    "L2314-33, présent dans le lot dans sa version depuis octobre 2025, conserve le mandat de quatre ans. La dérogation porte seulement sur cette durée, non sur une ancienne limite de mandats successifs ou sur la durée de l'emploi. Les trois niveaux d'accord et les deux bornes sont conservés pour les accords futurs aussi.",
    "La source entière reste en vigueur dans la proposition par maintien : la possibilité conventionnelle de choisir de deux à quatre ans est nécessaire pour préserver cette souplesse. Aucune extension nouvelle ou simplification nouvelle n'est comptée.",
    "La faculté reste conventionnelle et bornée ; elle ne donne pas un pouvoir unilatéral de raccourcir un mandat ni ne modifie les règles de validité des accords. Aucun gain de coût de scrutin n'est démontré.",
    "Aucune charge nouvelle n'est identifiée : aucun accord n'est imposé à ceux qui conservent quatre ans, et aucun dépôt ou délai supplémentaire n'est ajouté à la dérogation existante.",
    benefit="L'avantage est la dérogation à la durée légale de quatre ans par accord de branche, de groupe ou d'entreprise, permettant une durée comprise entre deux et quatre ans. Elle reste entièrement ouverte aux futurs accords recevables, aux trois niveaux et avec les mêmes bornes. Le maintien ne la réserve pas aux mandats déjà engagés et ne crée aucune autorisation administrative pour en bénéficier.",
)


retain(
    'L2314-35',
    "Maintien intégral : la continuité des mandats en cas de transfert protège la représentation et évite des élections imposées du seul fait d'une modification juridique. L'ajustement conventionnel de durée permet le raccordement au calendrier de l'entreprise d'accueil sans décision unilatérale. L'autonomie juridique et le maintien d'établissements distincts déterminent le champ utile ; les retirer ferait disparaître les garanties plutôt qu'un doublon.",
    "L1224-1 a été lu dans le corpus : les contrats en cours subsistent lors de la modification juridique, notamment succession, vente, fusion, transformation ou mise en société. Le renvoi n'est pas un droit fiscal de succession et n'est donc pas supprimé par la réforme des transmissions par décès. Conserver les trois alinéas : autonomie juridique, maintien du caractère d'établissement et accord de réduction ou prorogation avec les organisations existantes ou, à défaut, la délégation intéressée. La continuité des contrats uniques ne rétablit aucun nouveau CDD.",
    "La norme entière est conservée pour protéger la continuité des mandats et la faculté d'harmoniser leur calendrier. Elle contient déjà une souplesse évitant un renouvellement forcé ; ce maintien n'est pas une réduction nouvelle.",
    "Les conséquences des transferts sans autonomie ni établissement distinct ne sont pas inventées ici. Les protections supérieures attachées au transfert et les autres règles de consultation restent distinctes ; aucun chiffrage d'élections évitées n'est produit.",
    "Aucune charge nouvelle n'est identifiée : pas de nouvelle convention ou transmission obligatoire ; seul l'accord existant reste requis pour modifier la durée au titre de cette faculté.",
)


retain(
    'L2314-36',
    "Maintien intégral : la proposition du syndicat présentateur, le vote secret et la majorité du collège protègent l'indépendance de l'élu contre une révocation patronale ou minoritaire. Cette procédure ne constitue ni taxe, autorisation administrative ni déclaration redondante ; la supprimer affaiblirait le mandat ou fermerait la faculté de révocation démocratique.",
    "Conserver la majorité du collège électoral auquel appartient l'élu, et non la seule majorité des suffrages exprimés ou de l'effectif de l'entreprise. Le secret et l'identité de l'organisation ayant présenté le membre restent exigés. Le mécanisme ne remplace ni la rupture d'emploi ni l'autorisation requise pour un salarié protégé.",
    "La source entière demeure nécessaire à l'équilibre entre responsabilité de l'élu et indépendance du mandat. Aucun changement normatif ni procédure nouvellement supprimée n'est recensé.",
    "La règle ne crée pas de voie de révocation de candidats sans organisation présentatrice ni ne modifie les autres causes de fin du mandat. Les effets sur le contentieux ou les coûts d'un scrutin de révocation ne sont pas établis.",
    "Aucune charge nouvelle n'est identifiée : le même vote et les mêmes conditions de déclenchement sont maintenus, sans dossier administratif, registre ou délai additionnel.",
)


retain(
    'L2314-37',
    "Maintien intégral : la succession de remplaçants assure la continuité du siège sans élection systématique et respecte la liste, la catégorie et les suffrages déjà exprimés. Les priorités ne sont pas un doublon, mais départagent des candidats différents. Leur suppression exigerait une nouvelle désignation et risquerait de retirer les droits des suppléants ou candidats non élus.",
    "Conserver les cinq alinéas dans leur ordre : suppléant de la même organisation, priorité de catégorie, candidat non élu suivant le dernier titulaire ou à défaut suppléant, puis suppléant d'une autre organisation de même catégorie ayant le plus de voix, et terme au retour ou au renouvellement. Aucune mission de travail n'est assimilée à la fin du mandat ni au terme du contrat unique.",
    "La source officielle entière reste inchangée. La procédure de remplacement automatique évite déjà un renouvellement inutile tout en protégeant le choix électoral ; aucun gain nouveau n'est attribué à cette règle existante.",
    "Les élections partielles restent régies par leur article propre en cas de sièges durablement vacants selon ses seuils. L'article ne couvre pas toutes les listes sans affiliation dans des conditions non décrites ; aucune solution nouvelle à ces cas n'est inventée.",
    "Aucune charge nouvelle n'est identifiée : aucune candidature supplémentaire, autorisation ou déclaration n'est créée. Les priorités existantes restent applicables sans nouveau scrutin de désignation.",
)


retain(
    'L2315-1',
    "Maintien intégral : l'effectivité de la représentation des salariés hors de l'entreprise ou dans des unités dispersées est une protection nécessaire. L'article impose un résultat fonctionnel sans registre, rapport, nombre minimal de réunions ni agrément. Sa suppression exposerait précisément ces salariés à une représentation moins accessible, alors que l'allègement de la visioconférence peut faciliter ce résultat.",
    "La suppression du plafond de visioconférence dans L2315-4 n'écarte pas cette exigence. Le texte vise l'activité hors de l'entreprise et les unités dispersées sans ajouter une catégorie limitée aux seuls télétravailleurs. Il ne crée ni condition de présence physique pour voter ni condition de durée de mission.",
    "La source entière est conservée comme garantie d'effectivité pour les salariés dispersés, sans corps nouveau ni allègement additionnel compté. Aucune formalité autonome inutile n'y est identifiée.",
    "Les moyens concrets restent déterminés par les autres règles applicables et les situations de l'entreprise. Aucun équipement imposé à chaque salarié ni financement supplémentaire n'est déduit de cette phrase ; les coûts ne sont pas mesurés.",
    "Aucune charge nouvelle n'est identifiée puisque le maintien n'ajoute ni procédure ni donnée à fournir. L'obligation générale existante de représentation effective conserve son champ.",
)


retain(
    'L2315-2',
    "Maintien intégral nécessaire de la clause de faveur : les pouvoirs et le fonctionnement du CSE peuvent rester plus favorables en vertu d'accords collectifs ou d'usages. Supprimer cette réserve retirerait des avantages alors que les règles générales subsistent, en contradiction avec la priorité de préservation des allègements et garanties favorables. Elle n'impose pas de conclure un accord supplémentaire.",
    "La réserve couvre les accords et les usages, y compris leurs applications futures éligibles, sans les figer au jour de la réforme. Elle doit être articulée avec L2315-4 proposé : les modalités conventionnelles valables demeurent, tandis que le plafond légal de trois réunions sans accord disparaît. Elle ne crée pas d'exception aux règles propres du contrat unique par un simple renvoi au fonctionnement du CSE.",
    "La source entière reste maintenue pour empêcher que la simplification du droit commun ferme les dispositions plus favorables du CSE. Aucune nouvelle extension ou réduction n'est comptée.",
    "La clause ne détermine pas à elle seule le caractère plus favorable d'un accord particulier et ne modifie pas les règles de conclusion, révision ou dénonciation des accords et usages. Aucun avantage financier n'est chiffré.",
    "Aucune charge nouvelle n'est identifiée : aucun accord, usage, rapport ou procédure de reconnaissance n'est créé. La réserve favorable reste directement formulée comme dans la source.",
)


retain(
    'L2315-3',
    "Maintien intégral : le secret des procédés de fabrication et la discrétion sur les informations objectivement confidentielles présentées comme telles permettent l'information du CSE tout en protégeant des intérêts légitimes. Les deux obligations portent sur des objets et des personnes qui ne se confondent pas ; leur fusion ne supprimerait pas une formalité. Aucun rapport, registre ou engagement écrit supplémentaire n'est exigé.",
    "Conserver la distinction : secret professionnel des membres de la délégation pour les procédés, discrétion de ces membres et des représentants syndicaux pour les informations confidentielles présentées comme telles. Le marquage par l'employeur ne remplace pas la condition de caractère confidentiel ; le texte ne donne pas un droit de classer toute information. Aucune restriction nouvelle à l'accès légal du CSE ou au recours au juge n'est ajoutée.",
    "Aucun changement par rapport à la source entière : les deux protections de confidentialité restent nécessaires à un accès effectif aux informations sensibles. Aucune obligation administrative nouvelle supprimée n'est déclarée.",
    "Les durées et sanctions des obligations ainsi que leurs limites légales demeurent régies par leurs fondements propres. Le maintien n'atteste pas la confidentialité de chaque information communiquée ni la conformité de chaque pratique patronale.",
    "Aucune charge nouvelle n'est identifiée : aucun serment, engagement contractuel, registre des informations ou classement périodique n'est ajouté aux obligations substantielles existantes.",
)


rewrite(
    'L2315-4',
    """<p>Le recours à la visioconférence pour réunir le comité social et économique peut être organisé par accord entre l'employeur et les membres élus de la délégation du personnel du comité. En l'absence d'accord, ce recours est possible sans limitation du nombre de réunions par année civile. Un décret détermine les conditions dans lesquelles le comité social et économique peut, dans ce cadre, procéder à un vote à bulletin secret.</p>
<p>Cette suppression de la limite légale s'applique aux réunions convoquées à compter de l'entrée en vigueur de la loi portant la présente rédaction. Elle ne rend pas la visioconférence obligatoire et ne remet pas en cause les modalités d'organisation résultant d'accords valablement conclus, tant qu'elles demeurent applicables. Les garanties d'identification des membres, de participation effective aux délibérations et de secret des votes demeurent applicables. Les réunions convoquées avant cette date restent soumises aux règles qui leur étaient applicables.</p>""",
    "Réforme de fond : le plafond de trois réunions par année civile en l'absence d'accord disparaît réellement. Il n'est donc plus nécessaire d'obtenir un accord pour dépasser ce nombre ; un accord peut toujours organiser les modalités des réunions et les accords valables restent applicables. La possibilité de réunion à distance n'impose pas ce mode et ne supprime ni la participation effective ni le secret du vote. Ce retrait d'une autorisation conventionnelle au-delà du plafond ne modifie pas les majorités des accords collectifs.",
    "D2315-1 et D2315-2 ont été lus intégralement dans le corpus : identification, retransmission continue et simultanée du son et de l'image, suspensions de séance, confidentialité et sécurité du vote, accès technique de tous et durée identique de vote sont maintenus. Aucun renvoi normatif nouveau à ces cibles non fournies dans reference-targets.json n'est ajouté ; le renvoi au décret reste inchangé. Les droits de rémunération des réunions de L2315-11, lu dans le corpus, et la clause de faveur de L2315-2 subsistent. La suppression du plafond ne porte ni sur un nombre minimum de consultations ni sur les exigences supérieures de représentation effective ; aucune conformité générale de toutes les pratiques n'est présumée.",
    "La source entière plafonnait à trois réunions par année civile le recours sans accord. La proposition retire ce plafond et l'accord requis pour le dépasser, en maintenant les garanties du décret et les accords valables. L'allègement démontré concerne ce choix d'organisation ; aucune baisse de salaire, d'heures de délégation ou de prélèvement n'en résulte.",
    "Aucun coût net de visioconférence ou de déplacement évité n'est établi. Les accords existants, les règles de consultation, les moyens d'accès et le secret restent opposables ; la mesure ne rend pas possibles des délibérations techniquement inaccessibles à des membres.",
    "Aucune charge nouvelle de registre, déclaration, équipement imposé au salarié ou réunion supplémentaire n'est identifiée : le mode reste facultatif et les garanties techniques existaient déjà. Un recours plus fréquent peut modifier les coûts techniques et de déplacement ; leur solde net n'est pas démontré.",
    [effect(
        'authorization_removed', 'cse-visioconference-fin-plafond-legal',
        "Suppression du plafond légal de trois visioconférences et de l'accord nécessaire pour le dépasser.",
        "Sans accord employeur-élus, au plus trois réunions du CSE par année civile pouvaient être tenues en visioconférence.",
        "Sans accord, aucune limite légale du nombre de réunions en visioconférence ; accords d'organisation et garanties techniques conservés.",
        'legal_duty', "Employeurs et membres des CSE recourant à la visioconférence sans accord d'organisation.",
        "Réunions convoquées après l'entrée en vigueur ; réunions déjà convoquées et modalités conventionnelles valables préservées.",
        "Aucun accord, déclaration ou réunion de remplacement ; identification, participation, vote secret et rémunération restent exigés dans leur champ existant.",
        "En l'absence d'accord, ce recours est limité à trois réunions par année civile.",
        "En l'absence d'accord, ce recours est possible sans limitation du nombre de réunions par année civile.",
    )],
    removed=[
        "La limitation légale à trois réunions du comité social et économique par année civile en visioconférence lorsqu'aucun accord n'est conclu.",
        "La nécessité d'obtenir un accord entre l'employeur et les membres élus pour dépasser ce plafond légal de visioconférences.",
    ],
)


rewrite(
    'L2315-5',
    """<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant cette abrogation pour les supports de substitution aux registres mis en place à compter de cette date. La mise en place d'un tel support n'est plus soumise à la consultation préalable supprimée par cette abrogation. Aucun avis ni aucune transmission d'avis ne peut être exigé sur le seul fondement de cette consultation supprimée.</p>
<p>Cette abrogation ne porte atteinte ni aux droits d'accès aux registres tenus sur le support substitué, ni aux garanties de contrôle équivalentes, de présentation, d'intégrité et de conservation exigées sur un fondement distinct. Les consultations prévues par d'autres dispositions, notamment pour un projet modifiant l'organisation ou les conditions de travail, de santé ou de sécurité, demeurent applicables dans leur champ propre.</p>
<p>Les situations et recours relatifs aux supports mis en place avant cette date demeurent régis par les dispositions antérieures, sous réserve de l'application des règles relatives à la loi répressive plus douce. Aucun support déjà régulièrement mis en place n'a à être établi à nouveau du seul fait de cette abrogation.</p>""",
    "Abrogation prospective intégrale de la seule norme autonome de cet article : la consultation obligatoire du CSE avant un changement de support des registres auxquels il a accès. Les droits d'accès et les garanties de contrôle et d'intégrité reposent sur d'autres textes et restent applicables ; les consultations pour un véritable changement d'organisation ou de conditions de travail ne sont pas supprimées. La consultation spéciale du seul support et l'envoi d'un avis exclusivement issu de cette consultation ne sont remplacés par aucune déclaration, autorisation ni avis équivalent.",
    "Incohérence préexistante signalée : L8113-4, lu dans le corpus, autorise la présentation des livres, registres et documents à l'inspection mais ne décrit pas les conditions de substitution auxquelles la dernière partie de la source renvoie. Le fondement de la substitution est L8113-6, lu intégralement, ainsi que D8113-2 et D8113-3. L'abrogation retire le renvoi incohérent sans prétendre réécrire ces articles. D1221-27, lu intégralement, doit perdre son second alinéa d'envoi à l'inspection de l'avis prévu par L2315-5 ; la disposition proposée exclut déjà une exigence fondée sur ce seul avis supprimé, mais le règlement n'est pas déclaré réécrit dans ce lot. L1221-14 et les garanties de D8113-2 demeurent autonomes. D8113-3 conserve dans le corpus une ancienne référence à un récépissé de déclaration CNIL : son articulation avec le droit actuel des données doit être contrôlée séparément, sans faire renaître ici cette formalité. L2312-8 a été lu pour distinguer les consultations sur les projets substantiels. Aucun renvoi normatif nouveau à une cible non fournie n'est inséré.",
    "La source officielle entière contient une obligation spéciale de consultation préalable pour le seul support. Elle est entièrement retirée pour les changements futurs et l'avis qui en dépend ne peut la rétablir par règlement. Les garanties des registres et les consultations pour des projets substantiels subsistent sur leurs bases autonomes ; une seule suppression de procédure est comptée.",
    "La mesure ne supprime ni les registres eux-mêmes, ni leur contenu ou durée de conservation, ni les contrôles, ni les consultations nécessaires sur un fondement distinct. La coordination formelle du second alinéa de D1221-27 reste à rédiger hors de ce lot. Aucun coût national, temps gagné ou solde net global n'est établi.",
    "Aucune charge nouvelle n'est identifiée : la consultation spéciale n'est remplacée par aucun avis, déclaration, registre ou notification. Les garanties techniques et les consultations substantielles citées existaient déjà sur des fondements autonomes et ne sont pas élargies par l'abrogation.",
    [effect(
        'obligation_removed', 'cse-fin-consultation-seul-support-registres',
        "Suppression de la consultation spéciale préalable au changement du seul support de registres accessibles au CSE.",
        "Lorsqu'il dispose d'un droit légal d'accès aux registres visés, le CSE doit être consulté avant la mise en place d'un support de substitution.",
        "Aucune consultation fondée sur le seul changement de support ni avis exclusivement dérivé de cette procédure ; accès, garanties et consultations sur autres fondements maintenus.",
        'legal_duty', "Employeurs mettant en place un support de substitution pour des registres auxquels le CSE a légalement accès.",
        "Supports mis en place après l'entrée en vigueur ; situations et recours antérieurs préservés, sous réserve de la loi répressive plus douce.",
        "Aucune déclaration ou consultation de remplacement ; les procédures autonomes liées à des changements substantiels demeurent dans leur champ.",
        "le comité social et économique est consulté préalablement à la mise en place d'un support de substitution dans les conditions prévues à ce même article.",
        "La mise en place d'un tel support n'est plus soumise à la consultation préalable supprimée par cette abrogation.",
    )],
    repeal_scope="Suppression pour les nouveaux supports de substitution de l'obligation spéciale de consulter préalablement le CSE et de tout avis exigé sur le seul fondement de cette consultation, sans supprimer les droits d'accès, les garanties de contrôle ni les consultations autonomes sur les projets substantiels.",
)


retain(
    'L2315-6',
    "Maintien intégral : l'accès du CSE aux documents environnementaux déjà établis pour les autorités protège l'information sur les risques industriels et miniers. L'article ne demande pas de produire un rapport environnemental supplémentaire, seulement de porter des documents existants à la connaissance du comité. Cette information a une fonction de santé, sécurité et représentation qui justifie le maintien plutôt qu'une suppression indistincte de transmission.",
    "Le champ est conservé tel que sourcé : installations soumises à autorisation au titre de L512-1 du code de l'environnement et catégories citées du code minier. Les imperfections grammaticales de la source (« L. 512-1 code », « soumise ») ne justifient pas une réécriture stylistique. Les textes entiers des codes extérieurs ne figurent pas dans le lot ni parmi les cibles fournies : leur concordance actuelle n'est pas déclarée vérifiée. Aucun renvoi nouveau, extension de régime ou nouvelle autorisation n'est créé, et le présent maintien ne vaut pas validation juridique de ces concordances.",
    "La source entière est maintenue pour l'information sur des risques graves à partir de documents déjà établis. Aucun nouveau rapport distinct n'est identifié dans ce texte ; aucune transmission supprimée ou économie nouvelle n'est comptée.",
    "L'examen ne couvre pas les procédures propres aux autorités environnementales ou minières ni une concordance exhaustive de leurs codes extérieurs. La charge exacte des modalités réglementaires d'information et son coût net ne sont pas établis.",
    "Aucune charge nouvelle n'est identifiée : mêmes documents existants, destinataire et champ réglementaire, sans dossier, justificatif ou périodicité supplémentaire imposé par ce maintien.",
)


retain(
    'L2315-7',
    "Maintien intégral : le temps nécessaire et les minima d'heures de délégation rendent les fonctions représentatives effectives. Supprimer ces droits réduirait une garantie essentielle et retirerait un avantage aux futurs élus et représentants remplissant les conditions. Les seuils organisent des droits distincts et ne sont ni prélèvements ni justificatifs redondants ; aucune nouvelle obligation de rapport n'est prévue.",
    "Conserver les 1° à 3°, le seuil d'au moins cinq cent un salariés dans les deux cas syndicaux, l'absence d'établissement atteignant ce seuil pour le comité central, et les minima de dix heures par mois sous cinquante salariés et seize heures dans les autres entreprises. Les critères réglementaires restent à la fois les effectifs et le nombre de membres. L2315-10 et L2315-11, lus dans le corpus, conservent paiement et temps distincts : aucune limitation indirecte par le préavis individuel ou par l'absence d'indemnité ordinaire avant un an.",
    "Aucune modification de la source entière : personnes bénéficiaires, temps nécessaire et minima de dix ou seize heures restent en place. Il s'agit d'un maintien nécessaire de représentation et de droits favorables, sans réduction nouvelle de charges revendiquée.",
    "L'article ne contient pas le tableau réglementaire complet des heures ni toutes les règles de mutualisation et de paiement. Le maintien ne prétend ni les réécrire ni chiffrer leur coût, et ne s'étend pas par analogie à tous les représentants hors de son champ.",
    "Aucune charge nouvelle n'est identifiée : ni crédit d'heures supplémentaire, nouveau suivi, déclaration ou justificatif n'est ajouté. Les droits existants et leurs conditions sont conservés sans restriction future.",
)


retain(
    'L2315-8',
    "Maintien intégral : l'utilisation des heures de délégation au-delà du mois constitue une souplesse favorable et non un rapport mensuel à supprimer. Le renvoi réglementaire permet de préciser son exercice sans fermer le cumul aux situations futures. Abroger cette habilitation seule ne supprimerait aucune formalité concrète de la source et pourrait fragiliser l'avantage de cumul.",
    "R2315-5 a été lu intégralement dans le corpus : cumul sur douze mois, plafond mensuel d'une fois et demie et information huit jours avant usage. Ces conditions ne figurent pas dans L2315-8 ; aucune suppression du délai réglementaire ne peut être comptée au titre du présent maintien. Un examen propre de ce délai est à conduire dans le lot réglementaire sans fermer le cumul ni modifier silencieusement le crédit de base. La mutualisation entre personnes de L2315-9, également lue, est un mécanisme distinct.",
    "La source entière reste inchangée pour garder le fondement d'une utilisation pluri-mensuelle favorable. Aucun changement réel de délai, de volume d'heures ou de formalité n'est introduit et aucune simplification nouvelle n'est comptée.",
    "Seule l'habilitation législative est maintenue ; les conditions réglementaires identifiées ne sont pas prétendues déjà simplifiées. Leur coût, les populations effectivement utilisatrices et le solde global restent non mesurés.",
    "Aucune charge nouvelle n'est identifiée : aucun délai, registre, autorisation ou pièce ne s'ajoute au droit existant. Le maintien du renvoi ne constitue pas l'invention d'une nouvelle procédure réglementaire.",
)


# Only the target keys required for each source are emitted. Optional checks stay
# in review_notes and do not expand these lists.
target_keys = {value['number']: key for key, value in references['targets'].items()}

reference_assessments = {
    'L2314-21': {
        'L1234-1': "La cible règle le préavis de licenciement : la source distingue moins de six mois, six mois à moins de deux ans et deux ans ; la proposition passe à quinze jours calendaires pour les contrats nouveaux en préservant les anciens et les protections. L2314-21 ne la vise pas directement. Ses trois ou six mois sont des conditions électorales, non des délais de rupture : aucune fin de prestation ni notification de préavis n'efface l'emploi encore en cours ou ne remet l'ancienneté à zéro.",
        'L1221-2': "La source admet le CDI normal et certains CDD ; la proposition impose la durée indéterminée aux nouveaux emplois et interdit de faire d'une fin de mission le terme du contrat. Le calcul électoral proposé comprend donc les périodes où l'emploi porté subsiste sans prestation, tout en totalisant les périodes d'anciens contrats encore dans la fenêtre applicable. Il ne permet ni nouveau CDD ni renouvellement à durée déterminée et ne modifie pas les droits des contrats antérieurs.",
        'L1234-9': "Les trois et six mois d'ancienneté électorale ne sont pas le seuil indemnitaire. La cible officielle ouvre l'indemnité à huit mois hors faute grave ; sa proposition exige un an à la fin effective, préavis compris, puis 0,20 mois par année totale au prorata des mois complets, plafond légal de six mois et initiative patronale. L2314-21 ne la vise pas et ne transpose aucun de ces seuils au vote ; il n'altère ni composante des anciens contrats ni indemnités spéciales.",
    },
    'L2314-23': {
        'L1234-1': "La cible porte sur la durée du préavis patronal, avec ancienneté dans la source et quinze jours calendaires pour les seuls contrats nouveaux dans la proposition, protections distinctes conservées. Le maintien de douze mois continus chez l'utilisateur pour le vote ne renvoie pas à ce préavis et n'est pas modifié par une notification de rupture avant sa prise d'effet. La représentation chez l'utilisateur ne permet pas de contourner les autorisations de rupture des salariés protégés.",
        'L1221-2': "Le contrat unique proposé remplace les nouvelles embauches à terme par un emploi à durée indéterminée ; il n'abolit pas la mise à disposition chez un tiers. L2314-23 s'applique à cette situation sans exiger de CDD : le lien d'emploi reste avec l'entreprise qui emploie le salarié et le droit de vote chez l'utilisateur reste un choix sous condition de présence. Aucune nouvelle durée déterminée ni fin automatique d'emploi n'est induite par le maintien.",
        'L1111-2': "Le renvoi exprès au 2° concerne les salariés mis à disposition par une entreprise extérieure présents dans les locaux de l'utilisateur et y travaillant depuis au moins un an. Il ne transforme pas toutes les catégories du 2° en électeurs de l'utilisateur. La proposition de la cible garde cette catégorie et coordonne séparément les nouveaux contrats uniques, remplacements et proratisations. L2314-23 conserve douze mois continus, l'inéligibilité et l'option de vote ; la durée de mise à disposition n'est pas le terme de l'emploi.",
        'L1234-9': "L'ancienneté de douze mois continus chez l'utilisateur est électorale, distincte des services chez le même employeur pour l'indemnité. La source cible retient huit mois ; la proposition retient, pour le nouveau contrat, un an au terme effectif avec préavis, 0,20 mois par année totale au prorata des mois complets et plafond de six mois, à l'initiative de l'employeur. Aucun renvoi de L2314-23 n'importe ce barème ni son régime de notification dans le choix du lieu de vote ; les anciens contrats gardent leur transition.",
    },
    'L2314-24': {
        'L1234-1': "La fin d'une prestation lors de la confection des listes n'est pas un licenciement ni une notification de préavis. La cible proposée fixe quinze jours calendaires aux nouveaux contrats et maintient les règles des anciens ainsi que les protections ; aucune de ces durées ne commande l'inscription électorale. La proposition de L2314-24 exige le contrat encore en vigueur et n'anticipe pas sa rupture du seul fait d'une absence de prestation, sans supprimer les procédures de rupture protégée.",
        'L1221-2': "La cible officielle admet encore le terme dans les cas légaux ; sa proposition interdit le terme automatique de la nouvelle relation de travail, y compris à la fin d'une mission. Exiger une prestation à l'instant des listes deviendrait une exclusion entre prestations malgré le maintien de l'emploi. L2314-24 est donc coordonné vers le contrat en cours, avec ancienneté de L2314-21 et anciens contrats encore valables ; il ne permet aucun nouveau CDD et ne ressuscite aucun contrat rompu.",
        'L1234-9': "La cible règle une indemnité de licenciement, non l'électorat. Sa proposition prévoit un an au terme effectif avec préavis, puis 0,20 mois par année totale en mois complets proratisés, au plus six mois, hors démission ordinaire, avec protection des composantes anciennes et des indemnités spéciales. La suppression de la prestation en cours dans L2314-24 n'abaisse ni ne réhausse ce seuil : le contrat maintient le rattachement électoral jusqu'à sa rupture effective selon ses règles propres.",
    },
}

for number, checks in reference_assessments.items():
    source = by_number[number]
    key = source['code_id'] + '|' + source['source_id']
    required = references['requirements'][key]
    actual = []
    for target_key in required:
        target = references['targets'][target_key]
        actual.append({
            'target_key': target_key,
            'view_sha256': target['view_sha256'],
            'assessment': checks[target['number']],
        })
    answers[number]['reference_checks'] = actual


assert set(answers) == set(by_number)
output = [answers[source['number']] for source in sources]
Path('answer.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(output)} articles')
