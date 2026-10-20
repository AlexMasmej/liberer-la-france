import json
from pathlib import Path


drafts = {}


def add(number, proposed_xml, reason, review_notes):
    drafts[number] = {
        "proposed_xml": proposed_xml.strip(),
        "reason": reason,
        "review_notes": review_notes,
    }


add(
    "L141-9",
    """
<p>En fonction des circonstances locales, le document d'orientation et d'objectifs peut également prévoir qu'un secteur nouveau ne peut être ouvert à l'urbanisation qu'après la réalisation d'une évaluation environnementale, dans les conditions prévues à l'article L. 122-1 du code de l'environnement.</p>
""",
    "Réécriture à droit constant : la condition préalable à toute ouverture à l'urbanisation d'un secteur nouveau est exprimée directement, en conservant le caractère facultatif de sa fixation et l'appréciation des circonstances locales. Aucune réforme de fond n'est appliquée à cet article.",
    "Le renvoi à l'article L. 122-1 du code de l'environnement et l'exigence d'une évaluation préalable sont conservés. La note source fixe l'entrée en vigueur au 1er avril 2021, conformément à l'article 7 de l'ordonnance n° 2020-744 du 17 juin 2020 ; cette date historique n'est pas une date d'entrée en vigueur du projet de réforme.",
)

add(
    "L141-10",
    """
<p>Le document d'orientation et d'objectifs définit les éléments suivants en tenant compte des enjeux de préservation de l'environnement et des ressources naturelles, de prévention des risques naturels et de transition écologique, énergétique et climatique :</p>
<p>1° Les objectifs chiffrés de consommation économe de l'espace et de lutte contre l'étalement urbain, pour chaque secteur géographique ;</p>
<p>2° Les orientations de préservation des paysages et celles relatives à l'insertion et à la qualité paysagères des activités économiques, agricoles, forestières et de production et de transport d'énergie. Il définit également les espaces naturels, agricoles, forestiers ou urbains à protéger, notamment en raison de leur contribution à l'amélioration du cadre de vie. Il précise comment les paysages vécus et leurs composantes naturelles, historiques et socio-culturelles sont pris en compte dans les choix d'aménagement et veille à limiter les effets de saturation visuelle. Il transpose, à une échelle appropriée, les dispositions pertinentes des chartes de parcs naturels régionaux ;</p>
<p>3° Les modalités de protection des espaces nécessaires au maintien de la biodiversité ainsi qu'à la préservation ou à la remise en bon état des continuités écologiques et de la ressource en eau. À cette fin, il peut identifier des zones préférentielles de renaturation par transformation de sols artificialisés en sols non artificialisés, ainsi que des zones propices à l'accueil de sites naturels de compensation, de restauration et de renaturation ;</p>
<p>4° Les orientations contribuant à la transition énergétique et climatique, notamment à la lutte contre les émissions territoriales de gaz à effet de serre et de polluants atmosphériques, à l'accroissement du stockage de carbone dans les sols et les milieux naturels et au développement des énergies renouvelables au sens de l'article L. 211-2 du code de l'énergie.</p>
<p>Le document d'orientation et d'objectifs peut également identifier des zones d'accélération pour l'implantation d'installations terrestres de production d'énergies renouvelables arrêtées en application de l'article L. 141-5-3 du même code.</p>
<p>Dans le périmètre des communes non couvertes par un plan local d'urbanisme ou une carte communale, le document d'orientation et d'objectifs peut également délimiter, sur proposition ou avis conforme des communes concernées, des secteurs où l'implantation d'installations de production d'énergies renouvelables est soumise à conditions. Cette faculté s'exerce lorsque ces installations sont incompatibles avec le voisinage habité ou avec l'usage des terrains situés à proximité, ou lorsqu'elles portent atteinte à la sauvegarde des espaces naturels et des paysages, à la qualité architecturale, urbaine et paysagère, à la mise en valeur du patrimoine et à l'insertion des installations dans le milieu environnant.</p>
<p>Dans le périmètre des communes non couvertes par un plan local d'urbanisme ou une carte communale, le document d'orientation et d'objectifs peut également délimiter des secteurs où l'implantation d'installations de production d'énergies renouvelables est exclue, dans les départements où une cartographie des zones d'accélération pour l'implantation d'installations terrestres de production d'énergies renouvelables a été préalablement arrêtée en application de l'article L. 141-5-3 du code de l'énergie. Cette faculté est subordonnée à un avis du comité régional de l'énergie estimant, dans les conditions prévues au même article L. 141-5-3, que les zones d'accélération identifiées par cette cartographie sont suffisantes pour atteindre les objectifs régionaux établis en application de l'article L. 141-5-1 du même code. L'exclusion peut être prévue lorsque les installations sont incompatibles avec le voisinage habité ou avec l'usage des terrains situés à proximité, ou lorsqu'elles portent atteinte à la sauvegarde des espaces naturels et des paysages, à la qualité architecturale, urbaine et paysagère, à la mise en valeur du patrimoine et à l'insertion des installations dans le milieu environnant. Les secteurs délimités en application du présent alinéa s'appliquent uniquement aux projets dont la demande d'autorisation auprès de l'autorité compétente est déposée après l'approbation du schéma de cohérence territoriale qui les délimite. Ils ne s'appliquent ni aux procédés de production d'énergies renouvelables en toiture ni aux procédés de chaleur à usage individuel.</p>
""",
    "Réécriture à droit constant : les éléments du 2° sont distingués par des phrases complètes et les conditions cumulatives de délimitation des secteurs d'exclusion sont exposées successivement au sein du même alinéa. Les deux régimes, implantation soumise à conditions et implantation exclue, restent distincts. Aucune réforme de fond n'est introduite.",
    "Les 1° à 4° et les huit alinéas sont conservés. Le dernier alinéa conserve la cartographie préalable, l'avis de suffisance du comité régional, les motifs d'exclusion, l'application aux seules demandes déposées après l'approbation du schéma et les exceptions relatives aux toitures et à la chaleur individuelle. L'exigence de proposition ou d'avis conforme communal reste propre à l'avant-dernier alinéa. Tous les renvois au code de l'énergie sont maintenus. Selon la note source, le VI de l'article 15 de la loi n° 2023-175 du 10 mars 2023 rend ces dispositions applicables aux évolutions des schémas prescrites à compter de la promulgation de cette loi, le 10 mars 2023 ; cette condition temporelle demeure attachée au texte. Les protections environnementales et paysagères ne sont pas écartées au titre de la réforme du logement.",
)

add(
    "L141-11",
    """
<p>En zone de montagne, le document d'orientation et d'objectifs définit, pour les unités touristiques nouvelles structurantes, leur localisation, leur nature et leur capacité globale d'accueil et d'équipement, notamment pour le logement des salariés, y compris des travailleurs saisonniers.</p>
<p>Lorsque les enjeux de préservation du patrimoine naturel, architectural et paysager spécifique à la montagne le nécessitent, il définit les objectifs de la politique de réhabilitation et de diversification de l'immobilier de loisir.</p>
""",
    "Réécriture à droit constant : les caractéristiques à définir sont rattachées explicitement aux unités touristiques nouvelles structurantes, et la condition de définition des objectifs immobiliers est formulée directement. Le logement des saisonniers et les enjeux patrimoniaux sont maintenus. Aucune réforme de fond n'est appliquée.",
    "Les deux alinéas et la capacité globale d'accueil et d'équipement sont conservés, sans étendre le régime aux unités touristiques non structurantes. La note source indique une entrée en vigueur le 1er avril 2021, en application de l'article 7 de l'ordonnance n° 2020-744 du 17 juin 2020.",
)

add(
    "L141-11-1",
    """
<p>Dans les communes riveraines d'un plan d'eau intérieur d'une superficie supérieure à 1 000 hectares, au sens du 1° de l'article L. 321-2 du code de l'environnement, et soumises aux chapitres I<sup>er</sup> et II du titre II du présent livre, le document d'orientation et d'objectifs peut, en fonction des spécificités locales, déterminer les secteurs auxquels le chapitre I<sup>er</sup> du titre II du présent livre ne s'applique pas. Ces secteurs doivent être situés en dehors de la bande littorale de cent mètres définie à l'article L. 121-16 du présent code.</p>
""",
    "Réécriture à droit constant : le champ des communes est présenté avant la faculté de délimitation, et l'obligation de situer les secteurs hors de la bande littorale fait l'objet d'une phrase distincte dans le même alinéa. La dérogation préexistante n'est ni créée ni étendue par la réforme.",
    "Le seuil strictement supérieur à 1 000 hectares, le cumul des chapitres I et II et l'exclusion de la bande de cent mètres sont conservés. Le renvoi à L. 121-16 a été vérifié dans le corpus public ; il définit cette bande et renvoie lui aussi aux plans d'eau du 1° de L. 321-2 du code de l'environnement. Aucun régime général de dérogation aux protections du littoral ou de la montagne n'est ajouté. La source ne comporte pas de note d'application.",
)

add(
    "L141-12",
    """
<p>Un schéma de cohérence territoriale dont le périmètre comprend une ou plusieurs communes littorales peut fixer les orientations fondamentales pour l'aménagement, la protection et la mise en valeur de la mer et du littoral.</p>
""",
    "Réécriture à droit constant : le lien entre le périmètre du schéma et la présence de communes littorales est explicité, en conservant la faculté de fixer les orientations maritimes et littorales. Aucune réforme de fond n'est introduite.",
    "Les trois objets des orientations, aménagement, protection et mise en valeur, sont maintenus. La note source fixe l'entrée en vigueur au 1er avril 2021, conformément à l'article 7 de l'ordonnance n° 2020-744 du 17 juin 2020.",
)

add(
    "L141-13",
    """
<p>Le document d'orientation et d'objectifs fixe les critères permettant d'identifier les villages, agglomérations et autres secteurs déjà urbanisés prévus à l'article L. 121-8. Il en définit la localisation.</p>
<p>Il définit les orientations suivantes :</p>
<p>1° Les orientations visant à équilibrer les enjeux environnementaux et climatiques, d'une part, et les activités, notamment économiques, résidentielles et touristiques, d'autre part ;</p>
<p>2° Les orientations concernant l'accès au littoral et le partage des usages, notamment pour le développement des énergies marines renouvelables ainsi que pour le maintien et le développement des activités de loisirs, aquacoles ou halieutiques ;</p>
<p>3° Les orientations concernant la gestion des milieux aquatiques, la prévention des risques naturels liés à la mer et l'adaptation des territoires au recul du trait de côte. Le document peut identifier des secteurs propices à l'accueil d'ouvrages de défense contre la mer destinés à protéger des secteurs habités denses ou des équipements d'intérêt général ou publics. Il peut aussi identifier des secteurs destinés à accueillir des installations et des constructions pour des projets de relocalisation. Ces secteurs de relocalisation doivent se situer au-delà de la bande littorale et des zones délimitées en application de l'article L. 121-22-2, ainsi qu'en dehors des espaces remarquables du littoral.</p>
""",
    "Réécriture à droit constant : l'identification et la localisation sont exprimées dans deux phrases du même alinéa, puis les objets des orientations sont rendus plus directs. Les conditions d'implantation des secteurs de relocalisation sont formulées comme des obligations explicites. Aucune réforme de fond n'est introduite.",
    "Les 1° à 3° et leur place sont conservés. Les renvois à L. 121-8 et L. 121-22-2 ont été vérifiés dans le corpus : ils portent respectivement sur l'urbanisation littorale et les zones exposées au recul du trait de côte. La protection par des ouvrages reste liée aux secteurs habités denses ou aux équipements d'intérêt général ou publics ; les relocalisations restent exclues de la bande littorale, des zones visées et des espaces remarquables. La source ne comporte pas de note d'application.",
)

add(
    "L141-14",
    """
<p>Dans une perspective de gestion intégrée de la zone côtière, le document d'orientation et d'objectifs précise les vocations des différents secteurs de l'espace maritime. Il précise les conditions de compatibilité de leurs différents usages et les conséquences qui en résultent pour l'utilisation des diverses parties du littoral liées à cet espace.</p>
<p>Il précise les mesures destinées à protéger le milieu marin.</p>
<p>S'il y a lieu, il définit les orientations et les principes de localisation des équipements industriels et portuaires.</p>
<p>Il indique les orientations concernant l'aquaculture marine et les activités de loisirs.</p>
""",
    "Réécriture à droit constant : la phrase relative à la gestion intégrée est divisée dans le même alinéa et les usages concernés sont explicités. Les quatre fonctions du document et le caractère conditionnel des orientations industrielles et portuaires sont conservés. Aucune réforme de fond n'est appliquée.",
    "Les quatre alinéas sont maintenus dans leur ordre. Les effets sur le littoral restent rattachés à l'espace maritime concerné. La note source prévoit l'entrée en vigueur au 1er avril 2021 en application de l'article 7 de l'ordonnance n° 2020-744 du 17 juin 2020.",
)

add(
    "L141-15",
    """
<p>Les annexes présentent les éléments suivants :</p>
<p>1° Le diagnostic du territoire, qui expose les besoins d'aménagement de l'espace, de ressource en eau, d'équilibre social de l'habitat, de mobilités, d'équipements et de services, notamment au regard des prévisions économiques et démographiques. Ce diagnostic prend en compte la localisation des structures et équipements existants, les besoins globaux en matière d'immobilier, la maîtrise des flux de personnes, les enjeux de consommation économe de l'espace et de préservation de l'environnement, notamment de la biodiversité et du potentiel agronomique, des paysages et du patrimoine architectural, ainsi que les enjeux de prévention des risques naturels et d'adaptation au changement climatique. En zone de montagne, il est également établi au regard des besoins de réhabilitation de l'immobilier de loisir et d'unités touristiques nouvelles structurantes ;</p>
<p>2° L'évaluation environnementale prévue aux articles L. 104-1 et suivants ;</p>
<p>3° La justification des choix retenus pour établir le projet d'aménagement stratégique et le document d'orientation et d'objectifs ;</p>
<p>4° L'analyse de la consommation d'espaces naturels, agricoles et forestiers au cours des dix années précédant le projet de schéma, ainsi que la justification des objectifs chiffrés de limitation de cette consommation définis dans le document d'orientation et d'objectifs ;</p>
<p>5° Lorsque le schéma de cohérence territoriale tient lieu de plan climat-air-énergie territorial, les éléments mentionnés au deuxième alinéa de l'article L. 141-17.</p>
<p>Les annexes peuvent en outre comprendre tous les documents, analyses, évaluations et autres éléments utilisés pour élaborer le schéma que l'établissement public estime nécessaire de présenter à titre indicatif, ainsi que le programme d'actions mentionné à l'article L. 141-19.</p>
""",
    "Réécriture à droit constant : le contenu obligatoire des annexes est annoncé directement, la phrase du diagnostic est allégée et l'ajout facultatif de pièces indicatives est distingué. Tous les besoins, enjeux et contenus énumérés sont conservés. Aucune réforme de fond n'est introduite dans cet article du schéma de cohérence territoriale.",
    "Les 1° à 5°, les sept alinéas, la période de dix années et les renvois à L. 104-1 et suivants, au deuxième alinéa de L. 141-17 et à L. 141-19 sont conservés. Les deux alinéas de L. 141-17 restent à leur place dans le présent lot. Le diagnostic d'équipements et les enveloppes de densification prévus par coordination.json visent L. 151-4 et L. 151-26 : ils ne sont pas transposés ici en nouvelles obligations du schéma. La note source fixe l'entrée en vigueur au 1er avril 2021, conformément à l'article 7 de l'ordonnance n° 2020-744 du 17 juin 2020.",
)

add(
    "L141-16",
    """
<p>Le schéma de cohérence territoriale peut tenir lieu du plan climat-air-énergie territorial défini à l'article L. 229-26 du code de l'environnement si l'ensemble des établissements de coopération intercommunale délibèrent pour transférer l'élaboration de ce plan à l'établissement public mentionné à l'article L. 143-16.</p>
<p>Dans ce cas, la délibération de prescription est également notifiée à l'ensemble des collectivités territoriales et de leurs groupements mentionnés à l'article L. 229-25 du code de l'environnement et inclus dans le périmètre du schéma de cohérence territoriale. Ces collectivités et groupements doivent décider s'ils intègrent au schéma leur bilan d'émission de gaz à effet de serre ainsi que leur plan de transition, en application du même article.</p>
<p>La délibération de prescription du schéma de cohérence territoriale précise si l'établissement public mentionné à l'article L. 143-16 est également chargé du suivi et de l'évaluation du plan climat-air-énergie territorial prévus au IV de l'article L. 229-26 du code de l'environnement, ainsi que de la fonction de coordinateur de la transition énergétique définie à l'article L. 2224-34 du code général des collectivités territoriales.</p>
""",
    "Réécriture à droit constant recherchée : le sujet de la faculté de tenir lieu de plan est nommé expressément et la notification est séparée de la décision des collectivités dans le même alinéa. La décision de tous les établissements pour le transfert, les compétences complémentaires et tous les renvois sont conservés. Aucune réforme de fond n'est introduite ; l'ambiguïté préexistante du premier alinéa est signalée dans review_notes.",
    "Incohérence rédactionnelle préexistante : dans la source, « ce dernier » désigne grammaticalement l'établissement public alors qu'il est dit pouvoir tenir lieu de plan climat-air-énergie territorial. La proposition désigne explicitement le schéma de cohérence territoriale, en cohérence avec L. 141-17 et L. 141-18 ; cette clarification est à contrôler. Le renvoi à L. 143-16 a été vérifié dans le corpus : cet article désigne l'établissement chargé du schéma. Les trois alinéas sont conservés. La note source prévoit l'entrée en vigueur le 1er avril 2021, en application de l'article 7 de l'ordonnance n° 2020-744 du 17 juin 2020.",
)

add(
    "L141-17",
    """
<p>Lorsqu'il tient lieu de plan climat-air-énergie territorial, le schéma de cohérence territoriale poursuit les objectifs énoncés au 1° du II de l'article L. 229-26 du code de l'environnement. Ces objectifs sont définis par le projet d'aménagement stratégique et sont également déclinés dans le document d'orientation et d'objectifs.</p>
<p>Le schéma comprend également en annexe les éléments énumérés au II de l'article L. 229-26 du code de l'environnement qui concernent la mise en œuvre et le suivi de ces objectifs.</p>
""",
    "Réécriture à droit constant : la condition tenant à la double fonction du schéma est placée en tête et le sujet du second alinéa est explicité. La définition et la déclinaison des objectifs restent distinctes. Aucune réforme de fond n'est appliquée.",
    "Les deux alinéas sont maintenus : le renvoi du 5° de L. 141-15 au deuxième alinéa demeure exact. Les références distinctes au 1° du II et au II de L. 229-26 du code de l'environnement sont conservées. La note source indique une entrée en vigueur le 1er avril 2021 conformément à l'article 7 de l'ordonnance n° 2020-744 du 17 juin 2020.",
)

add(
    "L141-18",
    """
<p>La mise à jour, le cas échéant, ou l'adaptation du plan climat-air-énergie territorial et des documents qui le composent peut être effectuée conformément aux articles L. 229-25 et L. 229-26 du code de l'environnement sans réviser ni modifier l'ensemble du schéma de cohérence territoriale.</p>
""",
    "Réécriture à droit constant : la faculté de mettre à jour ou d'adapter les documents est exprimée sans la tournure impersonnelle relative à la nécessité d'une révision globale. Le cadre environnemental reste applicable. Aucune réforme de fond n'est introduite.",
    "Les deux renvois au code de l'environnement, la réserve « le cas échéant » et la portée limitée à l'absence de révision ou de modification de l'ensemble du schéma sont conservés. La note source fixe l'entrée en vigueur au 1er avril 2021, conformément à l'article 7 de l'ordonnance n° 2020-744 du 17 juin 2020.",
)

add(
    "L141-19",
    """
<p>Pour accompagner sa mise en œuvre, le schéma de cohérence territoriale peut comprendre un programme d'actions.</p>
<p>Ce programme précise les actions prévues sur le territoire pour mettre en œuvre la stratégie, les orientations et les objectifs du schéma de cohérence territoriale, en tenant compte des compétences de chacun. Ces actions peuvent être portées par la structure chargée d'élaborer le schéma, par les établissements publics de coopération intercommunale membres de cette structure ou par tout autre acteur public ou privé du territoire qui concourt à la mise en œuvre du schéma ou est associé à son élaboration.</p>
<p>Le programme peut également recenser les actions prévues relatives aux objectifs nationaux de l'Etat et aux objectifs régionaux, ou les mesures prévues par les conventions ou contrats qui les concernent, quand ils existent, dès lors que ceux-ci concourent à la mise en œuvre du schéma de cohérence territoriale.</p>
""",
    "Réécriture à droit constant : la finalité du programme est placée en tête, puis les actions et leurs porteurs sont présentés dans des phrases distinctes du même alinéa. Le respect des compétences, le caractère facultatif du programme et son rattachement à la mise en œuvre du schéma sont maintenus. Aucune réforme de fond n'est introduite.",
    "Les trois alinéas sont conservés. Le dernier alinéa de la source emploie « ils » et « ceux-ci » après plusieurs antécédents possibles, dont les objectifs et les conventions ou contrats. Cette ambiguïté préexistante est signalée et les rattachements pronominaux sont conservés sans arbitrage de fond ; leur portée doit être clarifiée avant toute modification normative. Aucun effet nouveau n'est donné aux contrats. La note source indique une entrée en vigueur le 1er avril 2021 en application de l'article 7 de l'ordonnance n° 2020-744 du 17 juin 2020.",
)


add(
    "L142-1",
    """
<p>Les documents, délimitations, opérations et autorisations suivants doivent être compatibles avec le document d'orientation et d'objectifs du schéma de cohérence territoriale :<br/><br/>1° Les programmes locaux de l'habitat prévus au chapitre II du titre préliminaire du livre III du code de la construction et de l'habitation ;<br/><br/>2° Les plans de mobilité prévus au chapitre IV du titre premier du livre II de la première partie du code des transports ;<br/><br/>3° La délimitation des périmètres d'intervention prévus à l'article L. 113-16 ;<br/><br/>4° Les opérations foncières et les opérations d'aménagement définies par décret en Conseil d'Etat ;<br/><br/>5° Les autorisations prévues à l'article L. 752-1 du code de commerce ;<br/><br/>6° Les autorisations prévues à l'article L. 212-7 du code du cinéma et de l'image animée ;<br/><br/>7° Les permis de construire tenant lieu d'autorisation d'exploitation commerciale prévus à l'article L. 425-4.</p>
""",
    "Réécriture à droit constant : la règle introductive exprime explicitement l'obligation de compatibilité pour toutes les catégories énumérées. Les intitulés légaux et la liste des sept catégories sont conservés, sans substitutions artificielles. Aucune réforme de fond n'est introduite.",
    "Les 1° à 7° restent dans le même ordre, séparés comme dans la source par des sauts de ligne. L'exigence demeure une compatibilité, sans devenir une conformité. Les renvois à L. 113-16 et L. 425-4 ont été vérifiés dans le corpus public et correspondent aux périmètres d'intervention et aux permis tenant lieu d'autorisation commerciale. La note source précise que l'article 7 de l'ordonnance n° 2020-745 du 17 juin 2020 rend ces dispositions applicables aux schémas de cohérence territoriale, plans locaux d'urbanisme, documents en tenant lieu et cartes communales dont l'élaboration ou la révision est engagée à compter du 1er avril 2021 ; cette portée temporelle doit être conservée.",
)

add(
    "L142-2",
    """
<p>Lorsque l'approbation d'un schéma de cohérence territoriale intervient après celle d'un programme local de l'habitat ou d'un plan de mobilité, ce programme ou ce plan doit, si nécessaire, être rendu compatible avec le schéma dans un délai de trois ans.</p>
""",
    "Réécriture à droit constant : le document à mettre en compatibilité et le schéma de référence sont nommés expressément, en conservant la condition d'antériorité de l'approbation et le délai de trois ans. Aucune réforme de fond n'est introduite.",
    "Le délai de trois ans et la réserve de nécessité sont conservés. La compatibilité s'articule avec L. 142-1, qui désigne le document d'orientation et d'objectifs du schéma comme référence. La note source fixe l'entrée en vigueur au 1er janvier 2021 conformément au XI de l'article 16 de la loi n° 2019-1428 du 24 décembre 2019.",
)

add(
    "L142-4",
    """
<p>Dans les communes où aucun schéma de cohérence territoriale n'est applicable, les restrictions suivantes s'appliquent :<br/><br/>1° À l'occasion de l'élaboration ou d'une procédure d'évolution d'un document d'urbanisme, ne peuvent être ouvertes à l'urbanisation les zones à urbaniser délimitées après le 1er juillet 2002, ainsi que les zones naturelles, agricoles ou forestières d'un plan local d'urbanisme ou d'un document en tenant lieu ;<br/><br/>2° À l'occasion de l'élaboration ou d'une procédure d'évolution d'une carte communale, les secteurs non constructibles de cette carte ne peuvent être ouverts à l'urbanisation ;<br/><br/>3° Les secteurs situés en dehors des parties urbanisées des communes non couvertes par un document d'urbanisme ne peuvent être ouverts à l'urbanisation pour autoriser les projets mentionnés aux 3° et 4° de l'article L. 111-4 ;<br/><br/>4° Dans une zone ou un secteur rendu constructible après le 4 juillet 2003, aucune autorisation d'exploitation commerciale ne peut être délivrée en application de l'article L. 752-1 du code de commerce, ni aucune autorisation en application des articles L. 212-7 et L. 212-8 du code du cinéma et de l'image animée.<br/><br/>Pour l'application du présent article, ont valeur de schéma de cohérence territoriale les schémas d'aménagement régional des collectivités de l'article 73 de la Constitution mentionnés à l'article L. 4433-7 du code général des collectivités territoriales, le schéma directeur de la région d'Ile-de-France prévu à l'article L. 123-1 et le plan d'aménagement et de développement durable de Corse prévu à l'article L. 4424-9 du code général des collectivités territoriales.</p>
""",
    "Réécriture à droit constant : la règle territoriale commune est annoncée directement, les occasions d'application des 1° et 2° sont placées en tête et l'interdiction de délivrer les autorisations du 4° est formulée explicitement. Les quatre restrictions et les trois catégories de documents équivalents sont conservées. Aucune réforme de fond n'est introduite.",
    "Les subdivisions et les sauts séparant les alinéas logiques sont conservés. Les deux dates distinctes, 1er juillet 2002 pour les zones à urbaniser et 4 juillet 2003 pour les zones ou secteurs rendus constructibles, ne sont pas harmonisées. Les renvois aux seuls 3° et 4° de L. 111-4 ont été vérifiés dans le corpus ; les autres cas de cet article ne sont pas ajoutés. Les équivalences avec les schémas régionaux, le schéma francilien et le plan corse restent limitées au présent article. La note source prévoit l'entrée en vigueur au 1er avril 2021 en application de l'article 7 de l'ordonnance n° 2020-744 du 17 juin 2020. La densification prévue par la politique du logement ne crée ici aucune dérogation nouvelle.",
)

add(
    "L142-5",
    """
<p>Une dérogation à l'article L. 142-4 peut être accordée avec l'accord de l'autorité administrative compétente de l'Etat, après avis de la commission départementale de la préservation des espaces naturels, agricoles et forestiers prévue à l'article L. 112-1-1 du code rural et de la pêche maritime et, le cas échéant, de l'établissement public prévu à l'article L. 143-16. Elle ne peut être accordée que si l'urbanisation envisagée respecte toutes les conditions suivantes : elle ne nuit pas à la protection des espaces naturels, agricoles et forestiers ou à la préservation et à la remise en bon état des continuités écologiques ; elle ne conduit pas à une consommation excessive de l'espace ; elle ne génère pas d'impact excessif sur les flux de déplacements ; elle ne nuit pas à une répartition équilibrée entre emploi, habitat, commerces et services.</p>
""",
    "Réécriture à droit constant : l'accord et les avis requis sont présentés avant les conditions de fond, dont le caractère cumulatif est explicité et la lecture facilitée par des points-virgules. Aucune condition n'est supprimée et aucune dérogation nouvelle n'est créée par la réforme.",
    "L'accord de l'Etat reste distinct des avis ; l'avis de l'établissement de L. 143-16 reste requis seulement le cas échéant. La formulation interne « protection ... ou ... préservation et ... remise en bon état » est maintenue, de même que les quatre conditions cumulatives. Les protections écologiques, la consommation d'espace, les déplacements et l'équilibre emploi-habitat-commerces-services sont tous conservés. La source ne comporte pas de note d'application.",
)

add(
    "L143-1",
    """
<p>L'initiative de l'élaboration du schéma de cohérence territoriale appartient aux établissements publics de coopération intercommunale ou aux groupements de collectivités territoriales compétents.</p>
""",
    "Réécriture à droit constant : la titularité de l'initiative est énoncée directement, sans modifier les deux catégories d'acteurs ni l'exigence de compétence. Aucune réforme de fond n'est introduite.",
    "La règle d'initiative est conservée sans la confondre avec la désignation de l'établissement chargé de l'élaboration prévue à L. 143-16. La note source fixe l'entrée en vigueur au 1er avril 2021 conformément à l'article 7 de l'ordonnance n° 2020-744 du 17 juin 2020.",
)

add(
    "L143-2",
    """
<p>Le territoire délimité par le périmètre du schéma de cohérence territoriale doit être d'un seul tenant et ne comporter aucune enclave.</p>
<p>Lorsque ce périmètre concerne des établissements publics de coopération intercommunale compétents en matière de schémas de cohérence territoriale, il doit couvrir la totalité du périmètre de chacun de ces établissements.</p>
""",
    "Réécriture à droit constant : les deux obligations de continuité territoriale et de couverture intégrale sont formulées expressément. Les deux alinéas et le champ des établissements compétents sont conservés. Aucune réforme de fond n'est introduite.",
    "L'exigence de territoire d'un seul tenant et sans enclave n'est pas assortie d'une exception nouvelle. La couverture intégrale s'applique à chacun des établissements concernés. La note source prévoit l'entrée en vigueur au 1er avril 2021, en application de l'article 7 de l'ordonnance n° 2020-744 du 17 juin 2020.",
)

add(
    "L143-3",
    """
<p>Le périmètre du schéma de cohérence territoriale est délimité en prenant en compte les déplacements et les modes de vie quotidiens au sein du bassin d'emploi, les besoins de protection des espaces naturels et agricoles, ainsi que les besoins et les usages des habitants en matière de logements, d'équipements, d'espaces verts, de services et d'emplois.</p>
<p>Sa délimitation prend également en compte :</p>
<p>1° Les périmètres des groupements de communes, des pays et des parcs naturels, ainsi que les périmètres déjà définis des autres schémas de cohérence territoriale, des bassins de mobilité au sens de l'article L. 1215-1 du code des transports, des plans de mobilité, des programmes locaux de l'habitat et des chartes intercommunales de développement et d'aménagement ;</p>
<p>2° Les déplacements urbains, notamment ceux entre le domicile et le lieu de travail et ceux liés à la zone de chalandise des commerces, ainsi que les déplacements vers les équipements culturels, sportifs, sociaux et de loisirs ;</p>
<p>3° Dans les zones de montagne, la communauté d'intérêts économiques et sociaux à l'échelle d'une vallée, d'un pays, d'un massif local ou d'une entité géographique constituant une unité d'aménagement cohérent.</p>
""",
    "Réécriture à droit constant recherchée : la prise en compte des critères est rattachée explicitement à la délimitation du périmètre et la phrase du 2° est rendue grammaticale. Les critères territoriaux, les listes et leur répartition sont conservés. Aucune réforme de fond n'est introduite ; la difficulté rédactionnelle du 2° est signalée.",
    "Le premier alinéa reste à sa place, car L. 143-6 le vise expressément. Les 1° à 3° et le renvoi à L. 1215-1 du code des transports sont conservés. La source présente au 2° une rupture de construction : « les déplacements entre le domicile et le lieu de travail et de la zone de chalandise des commerces ». La proposition explicite les déplacements liés à cette zone ; le sens exact de cette formulation préexistante est à contrôler. La note source fixe l'entrée en vigueur au 1er avril 2021, en application de l'article 7 de l'ordonnance n° 2020-744 du 17 juin 2020.",
)

add(
    "L143-4",
    """
<p>Selon les cas, l'organe délibérant du ou des établissements publics de coopération intercommunale compétents détermine un projet de périmètre selon l'une des règles de majorité suivantes :</p>
<p>1° Soit les deux tiers au moins des communes représentant plus de la moitié de leur population totale ;</p>
<p>2° Soit la moitié au moins des communes représentant les deux tiers de la population totale.</p>
<p>Pour calculer la majorité, chaque établissement public de coopération intercommunale compte pour un nombre de communes égal à celui de ses communes membres.</p>
""",
    "Réécriture à droit constant : les deux majorités alternatives sont annoncées clairement et le décompte des établissements est formulé au singulier pour expliciter son application à chacun. Les seuils et la compétence de détermination du projet restent identiques. Aucune réforme de fond n'est appliquée.",
    "Les quatre alinéas et les deux branches de majorité sont conservés. Le 1° exige les deux tiers au moins des communes et strictement plus de la moitié de la population ; le 2° conserve la moitié au moins des communes et la formulation « les deux tiers de la population totale », sans ajouter « au moins ». La source combine une décision d'organes délibérants d'établissements et une majorité exprimée en communes : cette articulation est conservée, sans inventer un mécanisme de vote. Les renvois de L. 143-7 à ces conditions restent utilisables. La note source indique une entrée en vigueur le 1er avril 2021 conformément à l'article 7 de l'ordonnance n° 2020-744 du 17 juin 2020.",
)

add(
    "L143-5",
    """
<p>L'autorité administrative compétente de l'Etat reçoit communication du projet de périmètre et recueille l'avis de chaque département concerné.</p>
""",
    "Réécriture à droit constant : l'autorité destinataire et sa tâche de consultation sont réunies dans une phrase à sujet explicite. La consultation demeure un avis et vise tous les départements concernés. Aucune réforme de fond n'est introduite.",
    "La source n'identifie pas l'auteur de la communication ; la proposition n'en désigne donc pas un nouveau. Aucun délai de consultation ni accord départemental n'est ajouté. La source ne comporte pas de note d'application.",
)

add(
    "L143-6",
    """
<p>L'autorité administrative compétente de l'Etat arrête le périmètre du schéma de cohérence territoriale à condition que le périmètre retenu prenne en compte les critères mentionnés au premier alinéa de l'article L. 143-3 et permette de mettre en cohérence les questions d'urbanisme, d'habitat, de développement économique, de déplacements et d'environnement. Elle tient compte des situations locales et des autres périmètres arrêtés ou proposés.</p>
""",
    "Réécriture à droit constant : les conditions de l'arrêté sont exprimées directement et l'autorité chargée de tenir compte du contexte local est nommée. Les domaines à mettre en cohérence et le renvoi ciblé restent identiques. Aucune réforme de fond n'est introduite.",
    "Le renvoi demeure limité au premier alinéa de L. 143-3, conservé à cette place dans le présent lot ; il n'est pas étendu aux critères supplémentaires des 1° à 3°. Les situations locales et les périmètres aussi bien arrêtés que proposés restent pris en compte. La note source fixe l'entrée en vigueur au 1er avril 2021 conformément à l'article 7 de l'ordonnance n° 2020-744 du 17 juin 2020.",
)

add(
    "L143-7",
    """
<p>L'autorité administrative compétente de l'Etat intervient lorsqu'elle constate, notamment en raison d'un nombre important de demandes de dérogation présentées sur le fondement de l'article L. 142-5, que l'absence de schéma de cohérence territoriale nuit gravement à la cohérence des politiques publiques d'urbanisme, d'habitat, de développement économique, de développement rural, de transports et de déplacements et de protection des espaces naturels, agricoles et forestiers, ou à la préservation et à la remise en bon état des continuités écologiques, ou conduit à une consommation excessive de l'espace. Elle intervient également lorsqu'elle constate que le périmètre d'un schéma de cohérence territoriale ne permet pas d'atteindre les objectifs définis à l'article L. 143-6. Dans ces cas, elle adresse aux établissements publics de coopération intercommunale compétents en matière de schéma de cohérence territoriale ou aux établissements publics prévus à l'article L. 143-16 et aux communes non membres d'un tel établissement, susceptibles d'être concernés, une demande tendant :</p>
<p>1° Soit à déterminer un périmètre de schéma de cohérence territoriale ;</p>
<p>2° Soit à délibérer sur l'extension d'un périmètre existant.</p>
<p>À compter de la réception de la lettre de l'autorité administrative compétente de l'Etat, les établissements publics de coopération intercommunale et les communes disposent de six mois pour proposer, dans les conditions fixées à l'article L. 143-4, selon les cas, la délimitation d'un périmètre de schéma de cohérence territoriale permettant d'atteindre les objectifs définis à l'article L. 143-6 ou l'extension du périmètre existant. S'ils n'ont pas présenté cette proposition dans ce délai, l'autorité administrative compétente de l'Etat arrête un projet de périmètre, après avis de la commission départementale de la coopération intercommunale prévue à l'article L. 5211-42 du code général des collectivités territoriales. Cet arrêté dresse la liste des établissements publics de coopération intercommunale et des communes concernés.</p>
<p>À compter de la notification de l'arrêté, l'organe délibérant de chaque établissement public de coopération intercommunale et le conseil municipal de chaque commune concernée disposent de trois mois pour se prononcer. En l'absence de délibération dans ce délai, la délibération est réputée favorable.</p>
<p>À l'issue du délai de trois mois prévu à l'alinéa précédent, l'autorité administrative compétente de l'Etat peut, par arrêté, délimiter ou étendre le périmètre avec l'accord des établissements publics de coopération intercommunale compétents et des communes concernés. Cet accord est exprimé dans les conditions de majorité définies à l'article L. 143-4.</p>
<p>En cas de délimitation d'un nouveau périmètre de schéma de cohérence territoriale, le même arrêté crée l'établissement public chargé de son élaboration et de son approbation prévu aux 1° et 2° de l'article L. 143-16. En cas d'extension du périmètre d'un schéma existant, il étend le périmètre de l'établissement public chargé de son suivi prévu aux 1° et 2° du même article L. 143-16.</p>
""",
    "Réécriture à droit constant : la longue condition d'intervention est répartie en phrases dans le premier alinéa, puis les étapes de proposition, de consultation et de décision sont formulées chronologiquement. Les délais, l'accord tacite et les majorités restent inchangés. Aucune réforme de fond n'est introduite.",
    "Les 1° et 2° et la succession des sept alinéas logiques matérialisés par les sauts de ligne de la source sont conservés. Le renvoi à « l'alinéa précédent » vise toujours le délai de trois mois suivant la notification. Le délai initial de six mois court toujours à la réception de la lettre de l'Etat ; les trois mois de consultation courent à la notification de l'arrêté. L'avis de la commission et l'accord à la majorité de L. 143-4 restent requis. L. 143-16 a été vérifié dans le corpus : il comporte aussi un 3°, mais la source ne vise ici que ses 1° et 2° ; ce champ est conservé sans extension silencieuse. La source ne comporte pas de note d'application. Ces délais ne sont pas remplacés par les délais d'instruction des permis visés par la réforme du logement.",
)

add(
    "L143-8",
    """
<p>Tout établissement public prévu à l'article L. 143-16 et tout établissement public de coopération intercommunale compétent en matière de schéma de cohérence territoriale peuvent, pour étendre le périmètre de leur schéma, proposer à l'autorité administrative compétente de l'Etat d'engager la procédure prévue à l'article L. 143-7.</p>
<p>La proposition indique le nom des communes concernées. L'autorité administrative compétente de l'Etat n'est pas liée par la liste de communes établie par l'établissement public qui présente la proposition.</p>
<p>L'autorité administrative compétente de l'Etat doit répondre dans les trois mois suivant la réception de la proposition. Si elle refuse d'engager la procédure, elle motive son refus.</p>
""",
    "Réécriture à droit constant : la finalité de la proposition est rapprochée de son auteur et le délai de réponse ainsi que l'obligation de motiver un refus sont exprimés directement. La liberté de l'Etat à l'égard de la liste proposée demeure. Aucune réforme de fond n'est introduite.",
    "Les trois alinéas et les renvois à L. 143-16 et L. 143-7 sont conservés. Le délai de trois mois court toujours à la réception de la proposition et aucun effet nouveau du silence n'est ajouté. La faculté reste une proposition d'engagement de la procédure, sans droit automatique à l'extension. La source ne comporte pas de note d'application.",
)


sources = json.loads(Path("source.json").read_text())
if set(drafts) != {a["number"] for a in sources}:
    raise ValueError("Lot de propositions incomplet ou surnuméraire")
answer = []
for source in sources:
    record = {key: source[key] for key in ("code_id", "source_id", "source_sha256", "number")}
    record.update(drafts[source["number"]])
    record["status"] = "rewrite_draft"
    answer.append(record)
Path("answer.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")
