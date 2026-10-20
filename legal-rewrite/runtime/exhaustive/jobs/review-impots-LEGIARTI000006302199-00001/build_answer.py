import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
answers = []
for source in sources:
    item = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    item.update(
        proposed_xml=source['previous_draft']['proposed_xml'],
        reason='',
        review_notes='',
        status='rewrite_draft',
    )
    answers.append(item)
by_number = {item['number']: item for item in answers}


def set_article(number, reason, notes, text=None, removed=None):
    item = by_number[number]
    item['reason'] = reason
    item['review_notes'] = notes
    if text is not None:
        item['proposed_xml'] = text
    if removed:
        item.update(
            change_type='normative_reduction',
            reform_policy_id='editorial_direction_2026_10_19',
            removed_provisions=removed,
        )


set_article(
    '1 A',
    'Seconde passe à droit constant : la définition de l’impôt personnel, les huit catégories de revenus et la déduction des charges restent nécessaires pour déterminer l’assiette commune. Supprimer une catégorie créerait une exonération générale sans justification propre à ses revenus ; les décisions relatives aux successions et à l’IS ne le commandent pas. La réécriture distingue les deux groupes de rémunérations de dirigeants et rend explicite le calcul du total net, en rétablissant les tirets et les dix alinéas de la source au lieu de la numérotation et de l’alinéa supplémentaires du premier projet.',
    'Les renvois aux articles 14 à 155 et 156 à 168, ainsi qu’au IV de l’article 3 du décret n° 55-594 du 20 mai 1955 modifié, sont conservés. L’annualité vise exclusivement l’impôt sur le revenu des personnes physiques ; elle ne doit pas servir à imposer annuellement à l’IS les bénéfices conservés. L’article 62 du corpus comporte des références complémentaires aux options des articles 239 bis AA et 239 bis AB et aux associés des 4° et 5° de l’article 8 : cette différence préexistante avec la liste générale du présent article est signalée sans élargissement silencieux de celle-ci. La coordination de l’article 62 avec l’IS à la distribution doit préserver l’imposition des rémunérations professionnelles réelles sans l’assujettir à une distribution préalable.',
    '''<p>L’impôt sur le revenu est un impôt annuel unique dû par les personnes physiques. Il porte sur le revenu net global du contribuable, déterminé conformément aux articles 156 à 168.</p>
<p>Le revenu net global est calculé à partir du total des revenus nets des catégories suivantes :</p>
<p>– Les revenus fonciers ;</p>
<p>– Les bénéfices industriels et commerciaux ;</p>
<p>– Les rémunérations, d’une part, des gérants majoritaires des sociétés à responsabilité limitée qui n’ont pas opté pour le régime fiscal des sociétés de personnes dans les conditions prévues au IV de l’article 3 du décret n° 55-594 du 20 mai 1955 modifié et des gérants des sociétés en commandite par actions ; d’autre part, les rémunérations des associés en nom des sociétés de personnes et des membres des sociétés en participation lorsque ces sociétés ont opté pour le régime fiscal des sociétés de capitaux ;</p>
<p>– Les bénéfices de l’exploitation agricole ;</p>
<p>– Les traitements, salaires, indemnités, émoluments, pensions et rentes viagères ;</p>
<p>– Les bénéfices des professions non commerciales et les revenus qui leur sont assimilés ;</p>
<p>– Les revenus de capitaux mobiliers ;</p>
<p>– Les plus-values de cession à titre onéreux de biens ou de droits de toute nature. Les revenus nets de ces catégories sont déterminés conformément aux articles 14 à 155. Les charges énumérées à l’article 156 sont retranchées de leur total pour obtenir le revenu net global.</p>''',
)

set_article(
    '4 A',
    'Seconde passe à droit constant : la rédaction antérieure est conservée après réexamen des deux obligations. La distinction entre l’imposition de l’ensemble des revenus des résidents et celle des seuls revenus français des non-résidents définit la compétence fiscale de la France. La supprimer rendrait indéterminé le champ de l’impôt personnel ou créerait une exonération territoriale générale sans justification identifiée. Cet article n’institue ni déclaration supplémentaire ni prélèvement successoral ou IS sur les bénéfices conservés.',
    'Les deux alinéas et leurs champs respectifs sont maintenus. Les critères de domicile relèvent de l’article 4 B, dont la réserve conventionnelle est conservée ; les attributions conventionnelles relèvent de l’article 4 bis. Les règles de source et les conventions internationales conservent leur portée. Aucun changement de résidence fiscale, de barème ou de fiscalité personnelle des dividendes n’est introduit.',
)

set_article(
    '4 B',
    'Seconde passe à droit constant : conserver les critères alternatifs de domicile, les preuves contraires et la réserve des conventions. La présomption concernant certains dirigeants sert à établir le lieu de l’activité principale, reste contestable et n’est pas une formalité autonome à supprimer. Son retrait affaiblirait le contrôle des domiciliations sans supprimer un doublon démontré. Le rattachement des agents publics à l’étranger évite une absence d’imposition personnelle lorsque le pays d’exercice ne taxe pas leur revenu mondial. Aucune de ces règles ne constitue un droit de succession ou un IS annuel.',
    'Le seuil reste strictement supérieur à 250 millions d’euros annuels réalisés en France ; la phrase propre à l’agrégation du chiffre d’affaires des entreprises contrôlées au sens de l’article L. 233-16 du code de commerce est maintenue sans ajouter de critère territorial à cette agrégation. Les trois alinéas du b et la liste complète des dirigeants restent en place. Le 2 exige toujours l’absence, dans le pays étranger, d’un impôt personnel sur l’ensemble des revenus ; il ne suffit pas que l’agent y soit moins imposé. Aucun transfert automatique de ces critères à la territorialité des successions supprimées ou au fait générateur du nouvel IS.',
)

set_article(
    '4 bis',
    'Seconde passe à droit constant : le 2° fournit la base interne de l’assujettissement lorsque la convention attribue l’imposition à la France, indépendamment de la nationalité et du domicile. Il complète les articles 4 A et 4 B ; l’abroger comme un simple renvoi risquerait de retirer cette base au lieu de supprimer une démarche inutile. La phrase est réécrite autour de la personne qui perçoit le revenu et le repère du 1° déjà abrogé est conservé.',
    'Le texte maintient l’exigence d’une convention internationale relative aux doubles impositions attribuant effectivement l’imposition à la France. Il ne transforme pas toute clause conventionnelle en nouvel impôt et ne modifie ni les limitations conventionnelles ni les règles d’assiette. Le 1° n’est pas une source « Réservé. » : l’article demeure une réécriture complète avec un 2° actif.',
    '''<p>Sont également soumises à l’impôt sur le revenu les personnes suivantes :</p>
<p>1° Abrogé ;</p>
<p>2° Les personnes de nationalité française ou étrangère qui perçoivent des bénéfices ou des revenus dont une convention internationale relative aux doubles impositions attribue l’imposition à la France, que leur domicile fiscal soit ou non situé en France.</p>''',
)

set_article(
    '5',
    'Seconde passe à droit constant : maintenir l’exonération des représentants diplomatiques et consulaires étrangers et sa condition de réciprocité. Retirer cet avantage augmenterait une charge ; supprimer la réciprocité créerait un avantage unilatéral sans besoin établi et affecterait les relations conventionnelles. Les repères historiques ne portent aucune obligation actuelle à réduire. L’introduction est corrigée pour ne pas présenter cet article comme la liste exhaustive de toutes les exonérations d’impôt sur le revenu.',
    'Les 1°, 2° et 2° bis restent respectivement périmé, abrogé et abrogé. Le 3° conserve les quatre catégories de représentants, la nationalité étrangère et la réciprocité limitée aux avantages analogues accordés aux agents français. Les engagements internationaux applicables ne sont pas écartés par cette réécriture nationale ; aucune modification de traité n’est proposée.',
    '''<p>Sont exonérés de l’impôt sur le revenu :</p>
<p>1° Disposition périmée ;</p>
<p>2° Abrogé ;</p>
<p>2° bis Abrogé ;</p>
<p>3° Les ambassadeurs, agents diplomatiques, consuls et agents consulaires de nationalité étrangère, dans la seule mesure où les pays qu’ils représentent accordent des avantages analogues aux agents diplomatiques et consulaires français.</p>''',
)

six = by_number['6']['proposed_xml']
six = six.replace('les revenus d’un enfant réputé', 'les revenus perçus par un enfant réputé')
six = six.replace('sur les revenus de chacun d’eux', 'sur les revenus perçus par chacun d’eux')
six = six.replace('sur ses revenus personnels de cette année', 'sur les revenus dont il a personnellement disposé pendant cette année')
six = six.replace('Elle est exclue lorsque les époux', 'Cette option est exclue lorsque les époux')
six = six.replace(
    'L’option est irrévocable et s’exerce dans le délai de dépôt de la déclaration initiale prévue à l’article 170.',
    'L’option s’exerce dans le délai de dépôt de la déclaration initiale prévue à l’article 170. Elle peut également être exercée ou révoquée, d’un commun accord entre les deux intéressés, dans le délai de réclamation applicable à l’impôt établi au titre de cette année. Les intéressés déposent les déclarations rectificatives nécessaires à la cohérence de leurs impositions.',
)
six += '\n<p>La faculté d’exercer ou de révoquer l’option prévue au second alinéa du 5 après le délai de dépôt de la déclaration initiale s’applique à l’imposition des revenus des années civiles commençant à compter de l’entrée en vigueur de la loi portant la présente réforme. Les revenus des années antérieures restent soumis aux dispositions qui leur étaient applicables, y compris pour le recouvrement, les restitutions, les réclamations et les prescriptions.</p>'
set_article(
    '6',
    'Réforme de fond ciblée : supprimer l’irrévocabilité et la forclusion au seul dépôt initial de l’option pour une imposition distincte l’année de l’union. Une erreur commune peut désormais être corrigée dans le délai ordinaire de réclamation, sans nouveau délai fiscal spécial ; l’accord des deux intéressés et la concordance de leurs déclarations évitent des impositions incompatibles. À droit constant pour le reste, conserver le foyer fiscal, les droits de rattachement et d’imposition séparée, tous les âges et exceptions ainsi que la répartition des revenus au décès. Ces règles servent au calcul de l’impôt personnel et ne sont pas des droits de succession. La réforme est réservée aux années civiles commençant à compter de l’entrée en vigueur.',
    'Les 1 à 8, les 1° à 3° du 3, les a à c du 4 et tous les renvois sont conservés ; la transition est ajoutée après le 8. Coordonner les déclarations de l’article 170 et leurs modalités réglementaires avec les rectifications concordantes, sans double imposition ou double restitution. Le renvoi au quatrième alinéa du 2° du II de l’article 156 reste inchangé. La source répète au second alinéa du 6 une présomption de partage par moitié après une règle comparable au premier alinéa : sa portée potentiellement générale justifie de la conserver plutôt que de la supprimer silencieusement. La formule source « de l’un ou des parents de l’un des conjoints » reste également conservée. Le 8 porte sur les bénéfices et revenus non taxés, pas sur le capital transmis : l’abolition des droits de succession ne l’abroge pas. Aucun changement du quotient familial ni des situations des années antérieures.',
    six,
    [
        'Suppression du caractère irrévocable de l’option des époux ou partenaires pour des impositions distinctes au titre de l’année de leur union.',
        'Suppression de la perte définitive de cette option faute de choix dans le délai de la déclaration initiale : exercice ou révocation communs admis jusqu’au terme du délai de réclamation applicable.',
    ],
)

set_article(
    '7',
    'Seconde passe à droit constant : maintenir l’égalité fiscale générale entre les partenaires pacsés et les contribuables mariés. L’article 6 ne traite que certaines règles du foyer ; il ne remplace pas cette extension à l’ensemble des règles d’assiette, de liquidation et de déclaration du code. L’abrogation de cet article retirerait une garantie d’égalité plutôt qu’une formalité en double. La formulation antérieure, qui distingue la règle et ses quatre composantes, est conservée.',
    'La note source maintient l’application à compter de l’imposition des revenus de 2011 et le décret prévu par l’article 95 IV et V de la loi n° 2010-1657 du 29 décembre 2010. Ces éléments historiques ne deviennent pas la date de la présente réforme. L’égalité s’étend à la faculté de rectification proposée au second alinéa du 5 de l’article 6 avec la même transition ; aucune déclaration additionnelle n’est créée ici.',
)

eight = by_number['8']['proposed_xml']
eight = eight.replace('sur le résultat déjà imposé au nom de l’usufruitier', 'sur le résultat imposé au nom de l’usufruitier')
eight = eight.replace(
    '<p>2° Aux membres des sociétés en participation, y compris les syndicats financiers, qui sont indéfiniment responsables et dont les nom et adresse ont été déclarés à l’administration ;</p>',
    '<p>2° Aux membres des sociétés en participation, y compris les syndicats financiers, qui sont indéfiniment responsables et dont les noms et adresses sont connus de l’administration. Cette condition est remplie lorsque l’administration détient légalement ces informations à jour et peut les rattacher sans ambiguïté à leur qualité de membre de la société concernée. Dans ce cas, ces informations ne font l’objet d’aucune communication supplémentaire, y compris dans les états annuels relatifs aux membres de la société. À défaut, seules les informations manquantes ou modifiées nécessaires à cette identification sont communiquées. Les obligations de déclarer les résultats et leur répartition entre les membres restent applicables ;</p>',
)
eight += '\n<p>La dispense de communication prévue au 2° s’applique aux résultats des exercices ouverts à compter de l’entrée en vigueur de la loi portant la présente réforme, y compris pour les sociétés déjà constituées. Les résultats des exercices ouverts avant cette entrée en vigueur restent soumis aux dispositions qui leur étaient applicables, y compris pour le recouvrement, les restitutions, les réclamations et les prescriptions.</p>'
set_article(
    '8',
    'Réforme de fond : supprimer la retransmission des noms et adresses des membres indéfiniment responsables d’une société en participation lorsque l’administration les détient légalement, à jour et reliés à cette société. La dispense vaut aussi pour les états annuels : elle retire une répétition réelle, tout en maintenant l’identification des redevables, la communication des seules données manquantes ou modifiées et la déclaration des résultats et de leur répartition. À droit constant pour le reste, conserver les sept catégories, leurs options et les règles de démembrement ; la suppression du mot « déjà » du premier projet évite de conditionner la non-imposition du nu-propriétaire au paiement préalable de l’impôt par l’usufruitier. Le régime d’IR des sociétés de personnes ne devient pas un régime d’imposition à la distribution.',
    'Pour les seuls membres de sociétés en participation visés au 2°, coordonner le 4 de l’article 206, l’article 162, le second alinéa de l’article 138 de l’annexe II et le 2 de l’article 359 de l’annexe III : les noms et adresses légalement détenus et rattachables à la société doivent être réputés indiqués à l’administration pour les mêmes exercices. Le 1° du 2 de l’article 48 de l’annexe III doit cesser d’exiger les noms et domiciles déjà connus ; la présente dispense législative couvre expressément cet état annuel. Elle ne supprime pas ses autres renseignements ni la part des bénéfices prévue au 2° du même 2. Les coordonnées inexactes ou non rattachables à la société doivent être fournies ou actualisées ; aucun accès nouveau à des données protégées n’est autorisé. Transition commune aux exercices ouverts à compter de l’entrée en vigueur. Le contrôle de ces renvois ne maintient pas les acomptes annuels d’IS ordinaire de l’article 359 sur les bénéfices conservés : sa refonte doit suivre celle de l’article 1668. Les faits générateurs de l’IS se coordonnent aux articles 209, 219 et 1668, sans étendre ce report à l’IR personnel maintenu ici ; le minimum international conserve son champ propre.',
    eight,
    [
        'Suppression de l’exigence d’une communication des noms et adresses des membres d’une société en participation lorsque ces informations à jour sont déjà légalement détenues et rattachables à la société par l’administration.',
        'Suppression de la retransmission annuelle de ces mêmes noms et adresses déjà connus dans les états fiscaux relatifs aux membres des sociétés en participation, sans supprimer les résultats ni leur répartition.',
    ],
)

set_article(
    '8 bis',
    'Réforme de fond par suppression d’un doublon législatif : abroger intégralement cet article, dont la seule règle est déjà énoncée au second alinéa de l’article 1655 ter. Ce dernier assujettit personnellement les associés ou actionnaires, à l’IR ou à l’IS selon leur régime, pour la part des revenus correspondant à leurs droits. La règle complète utile demeure donc dans l’article de référence ; la présente abrogation retire une répétition du code et ne prétend pas supprimer l’impôt des associés. Les impositions antérieures et leurs suites sont expressément préservées.',
    'Vérification en lecture seule de l’article 1655 ter : son second alinéa reprend intégralement la règle d’IR et couvre aussi l’IS ; il doit rester opératoire avec ses réserves à l’article 60, au 2° du I de l’article 827 et au 2° du I de l’article 828. L’article 218 bis renvoie directement à l’article 1655 ter. Aucun renvoi explicite au présent article 8 bis n’a été relevé dans le CGI et ses quatre annexes ; les renvois des articles 6, 7, 8, 10 et 10 bis A de l’annexe III visent l’article 8 bis de cette annexe, à conserver. Aucune suppression de déclaration ou baisse de prélèvement n’est annoncée au titre de cette seule abrogation de doublon. Le régime d’IR maintenu par 1655 ter reste distinct du nouvel IS à la distribution.',
    '''<p>Le présent article est abrogé à compter de l’entrée en vigueur de la loi portant la présente réforme.</p>
<p>Les impositions relatives aux revenus des périodes antérieures à cette entrée en vigueur restent régies par les dispositions qui leur étaient applicables. Le recouvrement, les restitutions, les réclamations et les prescriptions afférents à ces impositions sont préservés.</p>''',
)
by_number['8 bis'].update(
    change_type='full_repeal',
    repeal_policy_id='editorial_direction_2026_10_19',
    repeal_scope='Suppression de la disposition autonome qui répète l’assujettissement personnel à l’impôt sur le revenu des associés ou actionnaires des sociétés visées à l’article 1655 ter pour leur part des revenus sociaux ; l’obligation fiscale demeure fondée sur le second alinéa de cet article 1655 ter.',
)

set_article(
    '8 ter',
    'Seconde passe à droit constant : conserver l’attribution personnelle des bénéfices aux associés des sociétés civiles professionnelles, y compris coopératives. La soumettre désormais à une distribution étendrait sans justification la réforme de l’IS à un régime d’IR distinct. La référence à l’ordonnance définit les sociétés professionnelles concernées et leur fonctionnement ; elle n’institue ici aucun agrément fiscal ni déclaration séparée à supprimer. La rédaction antérieure est conservée, avec deux phrases distinguant l’assiette et le cas coopératif.',
    'Le livre II de l’ordonnance n° 2023-77 du 8 février 2023 et l’exercice en commun de la profession des membres sont conservés. La date du 1er septembre 2024 résulte de la note source et du premier alinéa du I de l’article 134 de cette ordonnance ; elle n’est pas une entrée en vigueur de la présente réforme. La réserve de l’article 8 ter au 1 de l’article 206 et la possibilité d’option du h du 3 de cet article 206, via l’article 239, doivent rester cohérentes : la présente réécriture ne supprime pas l’option à l’IS ni n’en impose les effets à des sociétés restées à l’IR. L’ordonnance extérieure au corpus n’est pas présentée comme modifiée.',
)

set_article(
    '8 quater',
    'Seconde passe à droit constant : conserver l’attribution à chaque copropriétaire de navire de sa part du résultat déclaré. Cette transparence détermine le redevable et son assiette ; supprimer le résultat déclaré ou attendre une distribution créerait une exonération ou un report d’IR distincts de la réforme de l’IS. L’article ne demande aucun état individuel supplémentaire. Le premier projet rend déjà directement lisible le champ maritime et la proportion des droits ; sa rédaction est conservée.',
    'Les bornes L. 5114-30 à L. 5114-50 du code des transports sont maintenues sans réécriture de ce code extérieur au lot. L’article 61 A du CGI conserve la déclaration d’un résultat déterminé selon le bénéfice réel avant amortissement du navire ; l’article 218 bis règle le cas des membres soumis à l’IS. Les résultats et quotes-parts demeurent nécessaires, indépendamment de la dispense ciblée de retransmission des coordonnées des sociétés en participation proposée à l’article 8. Aucun report à la distribution n’est créé pour les copropriétaires personnes physiques.',
)

set_article(
    '8 quinquies',
    'Réforme de fond : supprimer la conformité obligatoire à des statuts types approuvés par décret comme condition fiscale de l’imposition personnelle des copropriétaires d’étalon. L’assiette déclarée, les droits de chacun et le renvoi à l’article 238 bis M suffisent ici à rattacher le résultat ; une uniformité des conventions civiles n’est pas nécessaire à cette attribution. La réécriture maintient ces règles communes aux chevaux de course et aux étalons, sans modifier les clauses des conventions en cours ni les protections civiles, sanitaires ou animales. La suppression ne concerne que les exercices ouverts à compter de l’entrée en vigueur ; les exercices antérieurs restent sous leur régime.',
    'Le premier alinéa, les deux catégories de copropriétés et le renvoi à l’article 238 bis M sont maintenus. Ce dernier article, lu dans le corpus, vise l’inscription à l’actif des biens mis en propriété commune par les associés d’une société en participation : la portée de ce renvoi pour les copropriétés équines est une difficulté préexistante, qui n’est pas corrigée silencieusement. Les articles 39 F, 61 A et 218 bis restent nécessaires pour l’amortissement, le résultat à déclarer et les copropriétaires soumis à l’IS. Coordonner le décret d’approbation des statuts types pris sur le fondement du second alinéa de l’article 8 quinquies : ses prescriptions ne peuvent plus conditionner ce régime fiscal pour les exercices nouveaux. Ce décret extérieur aux sources fournies n’est ni identifié par un numéro inventé ni présenté comme déjà réécrit. Les engagements civils des copropriétés existantes sont maintenus.',
    '''<p>Pour une copropriété de cheval de course ou d’étalon remplissant les conditions de l’article 238 bis M, chaque membre est personnellement soumis à l’impôt sur le revenu sur la part des résultats déclarés par la copropriété qui correspond à ses droits.</p>
<p>L’application du premier alinéa n’est pas subordonnée à la conformité des statuts ou des modalités de fonctionnement d’une copropriété d’étalon à des statuts types approuvés par décret. Cette suppression de condition fiscale s’applique aux résultats des exercices ouverts à compter de l’entrée en vigueur de la loi portant la présente réforme, y compris pour les copropriétés déjà constituées. Les exercices ouverts avant cette entrée en vigueur restent soumis aux dispositions qui leur étaient applicables, y compris pour le recouvrement, les restitutions, les réclamations et les prescriptions. Les conventions en cours conservent leurs effets civils ; leurs clauses ne sont ni annulées ni modifiées de plein droit. Les règles civiles régissant la copropriété ainsi que les règles sanitaires et de protection animale demeurent applicables.</p>''',
    [
        'Suppression de l’obligation, pour l’application du régime fiscal aux résultats des exercices nouveaux d’une copropriété d’étalon, de conformer ses statuts et ses modalités de fonctionnement à des statuts types approuvés par décret.',
    ],
)

assert len(answers) == 12
Path('answer.json').write_text(json.dumps(answers, ensure_ascii=False, indent=2) + '\n')
