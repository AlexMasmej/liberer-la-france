import json
from pathlib import Path


drafts = {}


def add(number, proposed_xml, reason, review_notes):
    assert number not in drafts
    drafts[number] = dict(
        proposed_xml=proposed_xml.strip(),
        reason=reason,
        review_notes=review_notes,
        status="rewrite_draft",
    )


add(
    "L152-1",
    """<p>Toute personne publique ou privée qui exécute des travaux, des constructions, des aménagements, des plantations, des affouillements ou des exhaussements des sols, ou qui ouvre des installations classées appartenant aux catégories déterminées dans le plan, doit respecter le règlement du plan local d'urbanisme et ses documents graphiques.<br />Ces travaux ou opérations doivent, en outre, être compatibles avec les orientations d'aménagement et de programmation, lorsqu'elles existent.</p>""",
    "Réécriture à droit constant : la personne qui réalise les travaux ou ouvre l'installation est expressément désignée comme tenue de respecter le règlement et ses documents graphiques. La phrase suivante conserve le rapport de compatibilité propre aux orientations d'aménagement et de programmation. Aucune réforme de fond n'est introduite dans cet article général.",
    "Les deux alinéas sont conservés dans leur ordre. La conformité au règlement reste distincte de la compatibilité avec les orientations. Les enveloppes de densification prévues dans la coordination relèvent de L151-26, avec le diagnostic de L151-4 ; elles ne dispensent pas ici du respect des règles applicables ni des protections environnementales ou patrimoniales.",
)

add(
    "L152-2",
    """<p>Dès qu'un plan local d'urbanisme est opposable aux tiers, le propriétaire d'un terrain bâti ou non bâti réservé en application de l'article L. 151-41 peut exiger son acquisition par la collectivité ou le service public au bénéfice duquel la réservation a été instituée, dans les conditions et délais prévus aux articles L. 230-1 et suivants. Il peut exercer ce droit même si une décision de sursis à statuer qui lui a été opposée est encore en cours de validité.<br />Lorsqu'une servitude mentionnée à l'article L. 151-41 est instituée, chaque propriétaire d'un terrain concerné peut mettre la commune en demeure d'acquérir ce terrain, dans les conditions et délais prévus aux articles L. 230-1 et suivants.</p>""",
    "Réécriture à droit constant : le point de départ du droit de délaissement est placé en tête et l'absence d'obstacle tiré d'un sursis à statuer fait l'objet d'une phrase distincte. Le second alinéa identifie directement la commune destinataire de la mise en demeure. Aucune réforme de fond du droit d'acquisition n'est proposée.",
    "Maintien des deux alinéas, des terrains bâtis ou non bâtis, du bénéficiaire de la réservation et des renvois à L151-41 et L230-1 et suivants. Les deux mécanismes ne sont pas fusionnés : acquisition par la collectivité ou le service bénéficiaire au premier alinéa, mise en demeure de la commune au second.",
)

add(
    "L152-3",
    """<p>Les règles et servitudes définies par un plan local d'urbanisme sont soumises aux dispositions suivantes :<br />1° Des adaptations mineures peuvent leur être apportées lorsqu'elles sont rendues nécessaires par la nature du sol, la configuration des parcelles ou le caractère des constructions avoisinantes ;<br />2° Aucune autre dérogation ne peut leur être apportée en dehors de celles que prévoient les dispositions de la présente sous-section.</p>""",
    "Réécriture à droit constant : la possibilité d'adaptations mineures est formulée séparément de l'interdiction des autres dérogations. Les trois motifs pouvant rendre ces adaptations nécessaires restent limitativement énoncés. Aucune faculté générale de déroger pour densifier n'est ajoutée.",
    "Les 1° et 2° et leur ordre sont conservés. Incohérence de structure préexistante : le 2° vise la « présente sous-section », alors que le classement public fourni place l'article dans la section 2 « Dérogations au plan local d'urbanisme », sans sous-section indiquée. Le renvoi est conservé ; sa correction demanderait une coordination explicite de la structure du chapitre et du périmètre des dérogations.",
)

add(
    "L152-4",
    """<p>Pour permettre les opérations suivantes, l'autorité compétente pour délivrer le permis de construire peut, par décision motivée, accorder une dérogation à une ou plusieurs règles du plan local d'urbanisme :<br />1° La reconstruction de bâtiments détruits ou endommagés à la suite d'une catastrophe naturelle survenue depuis moins d'un an, lorsque les prescriptions imposées aux constructeurs pour assurer la sécurité des biens et des personnes sont contraires à ces règles ;<br />2° La restauration ou la reconstruction d'immeubles protégés au titre de la législation sur les monuments historiques, lorsque leurs contraintes architecturales propres sont contraires à ces règles ;<br />3° La réalisation de travaux nécessaires pour rendre un logement existant accessible aux personnes handicapées.<br />L'autorité qui délivre le permis recueille l'accord de l'autorité administrative compétente de l'Etat et du maire ou du président de l'établissement public de coopération intercommunale compétent en matière de plan local d'urbanisme, lorsqu'ils ne délivrent pas eux-mêmes le permis de construire.</p>""",
    "Réécriture à droit constant : l'objet de la décision motivée est annoncé avant l'énumération ; les circonstances de destruction, les contraintes propres aux monuments historiques et l'objectif d'accessibilité sont exprimés plus directement. Les accords des autorités concernées restent requis. Aucune réforme de fond n'est introduite.",
    "Maintien des 1°, 2° et 3°, de leur ordre et du dernier alinéa. La catastrophe doit être survenue depuis moins d'un an ; cette condition ne devient pas un délai de dépôt du permis. Les deux premières dérogations restent liées à des prescriptions ou contraintes contraires au PLU. Articuler les accords de cet article avec l'accord du maire prévu à L152-6-10, sans les supprimer ni les remplacer.",
)

add(
    "L152-5",
    """<p>Pour autoriser les opérations énumérées ci-dessous, l'autorité compétente pour délivrer le permis de construire ou le permis d'aménager et pour statuer sur une déclaration préalable peut, par décision motivée et dans les limites fixées par un décret en Conseil d'Etat, déroger aux règles des plans locaux d'urbanisme relatives à l'emprise au sol, à la hauteur, à l'implantation et à l'aspect extérieur des constructions :</p>
<p>1° L'isolation des constructions existantes réalisée en saillie des façades ;</p>
<p>2° L'isolation des constructions existantes réalisée par surélévation des toitures ;</p>
<p>3° La pose, en saillie des façades, de dispositifs de protection contre le rayonnement solaire ;</p>
<p>4° L'installation, sur des aires de stationnement, d'ombrières dotées de procédés de production d'énergies renouvelables ;</p>
<p>5° L'installation d'équipements de production d'énergie renouvelable, telle que définie à l'article L. 211-2 du code de l'énergie, ou d'équipements de réseaux de chaleur ou de froid efficaces au sens de la directive (UE) 2023/1791 du Parlement européen et du Conseil du 13 septembre 2023 relative à l'efficacité énergétique et modifiant le règlement (UE) 2023/955 ;<br /><br />6° La pose de revêtements réflectifs sur les toitures.</p>
<p>L'autorité peut assortir sa décision motivée de prescriptions visant à assurer la bonne intégration architecturale du projet dans le bâti existant et le milieu environnant.</p>
<p>Les dérogations prévues au présent article ne sont pas applicables :</p>
<p>a) Aux immeubles classés ou inscrits au titre des monuments historiques en application du titre II du livre VI du code du patrimoine ;</p>
<p>b) Aux immeubles protégés au titre des abords en application de l'article L. 621-30 du même code ;</p>
<p>c) Aux immeubles compris dans le périmètre d'un site patrimonial remarquable mentionné à l'article L. 631-1 du même code ;</p>
<p>d) Aux immeubles protégés en application de l'article L. 151-19 du présent code.</p>""",
    "Réécriture à droit constant : l'objet des dérogations est annoncé dès l'ouverture, les opérations d'isolation et de protection solaire sont formulées plus directement et l'autorité pouvant imposer les prescriptions d'intégration est explicitée. Les six opérations et les quatre exclusions patrimoniales sont intégralement maintenues. La politique de densification n'est pas utilisée pour étendre ce régime énergétique.",
    "Numérotation 1° à 6° et lettres a) à d) conservées ; le 6° reste dans le même bloc que le 5°, séparé par des sauts de ligne, comme dans la source. Les quatre catégories de règles dérogeables et l'encadrement par décret en Conseil d'Etat sont maintenus. Renvois conservés : énergie L211-2 ; directive (UE) 2023/1791 du 13 septembre 2023 et règlement (UE) 2023/955 ; patrimoine L621-30 et L631-1 ; urbanisme L151-19. Les exclusions patrimoniales ne sont pas écartées par la réforme du logement.",
)

add(
    "L152-5-1",
    """<p>Pour permettre l'installation de dispositifs de végétalisation des façades et des toitures dans les zones urbaines et à urbaniser, l'autorité compétente pour délivrer le permis de construire et pour statuer sur une déclaration préalable peut, par décision motivée, déroger aux règles des plans locaux d'urbanisme relatives à la hauteur et à l'aspect extérieur des constructions. Elle exerce cette faculté dans les limites fixées par un décret en Conseil d'Etat.</p>""",
    "Réécriture à droit constant : l'objectif de végétalisation et le périmètre des zones concernées précèdent la faculté de déroger ; l'encadrement réglementaire est exprimé dans une phrase distincte. Aucune réforme de fond n'est ajoutée.",
    "Un seul alinéa conservé. La dérogation reste limitée à la hauteur et à l'aspect extérieur, aux zones urbaines et à urbaniser, et aux décisions motivées prises dans les limites du décret en Conseil d'Etat. Elle n'est pas étendue à l'emprise au sol ni aux autres catégories de travaux.",
)

add(
    "L152-5-2",
    """<p>L'autorité compétente pour délivrer le permis de construire ou pour statuer sur une déclaration préalable peut autoriser une construction faisant preuve d'exemplarité environnementale à déroger aux règles des plans locaux d'urbanisme relatives à la hauteur, en tenant compte de la nature du projet et de sa zone d'implantation. Cette dérogation vise à éviter que le nombre d'étages soit limité par rapport à un autre type de construction. Un décret en Conseil d'Etat définit les exigences auxquelles la construction doit satisfaire.</p>""",
    "Réécriture à droit constant : la faculté de déroger, son objectif relatif au nombre d'étages et les exigences réglementaires sont répartis entre trois phrases dans le même alinéa. L'exemplarité environnementale reste une condition du régime ; aucune augmentation générale de hauteur n'est créée.",
    "Maintien de l'appréciation tenant à la nature du projet et à sa zone d'implantation, de la seule dérogation de hauteur et du décret en Conseil d'Etat. Aucun pourcentage, étage supplémentaire ou droit automatique n'est inventé. L'accord du maire relève, le cas échéant, de L152-6-10.",
)

add(
    "L152-5-3",
    """<p>Dans les limites précisées par décret en Conseil d'Etat, l'autorité compétente pour délivrer l'autorisation d'urbanisme peut accorder aux projets qualifiés d'intérêt national majeur dans les conditions de l'article L. 300-6-2 une dérogation aux règles des plans locaux d'urbanisme relatives à la hauteur.</p>""",
    "Réécriture à droit constant : la dérogation de hauteur est directement reliée à la qualification d'intérêt national majeur et à ses limites réglementaires. Aucune réforme de fond de ce régime distinct n'est proposée.",
    "Le renvoi existant à L300-6-2 et l'encadrement par décret en Conseil d'Etat sont conservés. Ce régime n'est pas étendu à tout projet de logement ou à toute opération proche des transports. L'attribut de présentation align de la source est supprimé pour respecter les balises autorisées, sans effet juridique.",
)

add(
    "L152-6-1",
    """<p>Lorsque le règlement du plan local d'urbanisme ou du document en tenant lieu impose la réalisation d'aires de stationnement pour les véhicules motorisés, l'autorité compétente pour délivrer le permis de construire peut, par décision motivée et en tenant compte de la nature du projet et de sa zone d'implantation, réduire cette obligation. Chaque réduction d'une aire de stationnement pour véhicule motorisé a pour contrepartie la création d'infrastructures ou l'aménagement d'espaces permettant le stationnement sécurisé d'au moins six vélos.</p>
<p>Lorsque ce règlement impose la réalisation d'aires de stationnement pour les véhicules motorisés, l'autorité compétente pour délivrer le permis de construire peut également, par décision motivée et en tenant compte de la nature du projet et de sa zone d'implantation, autoriser des dérogations aux règles qu'il fixe en application de la dernière phrase du deuxième alinéa de l'article L. 151-33.</p>""",
    "Réécriture à droit constant : le premier alinéa distingue la faculté de réduction de sa contrepartie précise en stationnement sécurisé pour vélos. Le second conserve la faculté distincte de déroger aux conditions locales de satisfaction de l'obligation de stationnement. Aucune réduction automatique ni réforme de fond n'est introduite.",
    "Deux alinéas conservés. Le ratio reste d'une aire pour véhicule motorisé contre au moins six vélos, avec création d'infrastructures ou aménagement d'espaces sécurisés. Le renvoi à la dernière phrase du deuxième alinéa de L151-33 a été vérifié dans le corpus : il concerne les conditions précisées par le règlement, éventuellement différentes selon les secteurs et types de bâtiments. Conserver cette cible lors de la réécriture de L151-33.",
)

add(
    "L152-6-2",
    """<p>Pour permettre le réemploi d'une friche au sens de l'article L. 111-26, l'autorité compétente pour délivrer l'autorisation d'urbanisme peut, par décision motivée, autoriser les projets de construction ou de travaux réalisés sur cette friche à déroger aux règles relatives au gabarit, dans la limite d'une majoration de 30 % de ces règles, ainsi qu'aux obligations en matière de stationnement.</p>""",
    "Réécriture à droit constant : la finalité de réemploi de la friche est placée en tête et l'autorité responsable de la décision motivée devient le sujet de la phrase. La dérogation au gabarit et celle relative au stationnement restent distinctes. Aucune réforme de fond ni extension aux terrains qui ne sont pas des friches n'est apportée.",
    "Le plafond de 30 % porte sur les règles de gabarit ; il n'est pas étendu à la dérogation aux obligations de stationnement. Le renvoi à la définition de la friche de L111-26 est conservé. La règle de non-cumul avec L152-6-4 reste portée par le dernier alinéa de ce dernier article.",
)

add(
    "L152-6-4",
    """<p>Dans le périmètre d'une grande opération d'urbanisme mentionnée à l'article L. 312-3 du présent code ou dans les secteurs d'intervention d'une opération de revitalisation de territoire délimités en application de l'article L. 303-2 du code de la construction et de l'habitation, des dérogations au règlement du plan local d'urbanisme ou du document en tenant lieu peuvent être autorisées dans les conditions et selon les modalités du présent article. Elles ont pour objet de contribuer au développement ou à la revitalisation du territoire et de faciliter le renouvellement urbain et la maîtrise de l'étalement urbain.</p>
<p>L'autorité compétente pour délivrer le permis de construire tient compte de la nature du projet, de sa zone d'implantation, de son intégration harmonieuse dans le tissu urbain existant, de sa contribution au développement, à la transformation ou à la revitalisation de la zone concernée et à la lutte contre la consommation des espaces naturels, agricoles et forestiers. Dans les zones urbaines et dans le respect des objectifs de mixité sociale et fonctionnelle, elle peut, par décision motivée :</p>
<p>1° Déroger aux règles de retrait qui imposent une distance minimale par rapport aux limites séparatives ;</p>
<p>2° Déroger aux règles de gabarit et de densité, sans dépasser une majoration de 30 % du gabarit et de la densité prévus par le document d'urbanisme ;</p>
<p>3° Déroger aux obligations de stationnement, compte tenu de la qualité et des modes de desserte, de la densité urbaine ou des besoins propres au projet au regard des capacités de stationnement existantes à proximité ;</p>
<p>4° Autoriser une destination que le document d'urbanisme n'autorise pas, dès lors qu'elle contribue à diversifier les fonctions urbaines du secteur concerné ;</p>
<p>5° Autoriser une dérogation supplémentaire de 15 % aux règles de gabarit pour les constructions qui contribuent à la qualité du cadre de vie en créant des espaces extérieurs en continuité des habitations et qui assurent un équilibre entre les espaces construits et les espaces libres. Cette dérogation supplémentaire ne peut porter le dépassement total au-delà de 50 %.</p>
<p>Le bénéfice du présent article ne peut se cumuler avec celui des articles L. 152-6 et L. 152-6-2 du présent code.</p>""",
    "Réécriture à droit constant : le périmètre et les finalités sont séparés, puis les critères d'appréciation et les objectifs de mixité sont répartis entre plusieurs phrases dans le même alinéa. Les cinq facultés et l'interdiction de cumul sont intégralement reprises. La réforme de densification ne conduit ni à relever les plafonds existants ni à étendre ce régime hors de son périmètre.",
    "Huit alinéas et 1° à 5° conservés. Maintien de la majoration de 30 % au 2°, du supplément de 15 % et du plafond total de 50 % au 5°, sans recomposer un nouveau taux. La source ne détaille pas le mode de combinaison arithmétique du supplément et de la majoration ; cette question reste à contrôler dans les textes d'application. Renvois à L312-3, CCH L303-2, L152-6 et L152-6-2 conservés. Le non-cumul ne vise pas L152-6-1 : aucune interdiction supplémentaire n'est ajoutée.",
)

add(
    "L152-6-5",
    """<p>I. - Lorsqu'elle délivre une autorisation d'urbanisme, l'autorité compétente peut permettre qu'un bâtiment dont la destination n'est pas l'habitation devienne un bâtiment à destination principale d'habitation, par dérogation aux règles relatives aux destinations fixées par le plan local d'urbanisme ou le document en tenant lieu. Elle tient compte de la nature du projet et de sa zone d'implantation. La dérogation s'étend aux travaux ou aux constructions d'extension ou de surélévation qui font l'objet de l'autorisation d'urbanisme.</p>
<p>L'autorité peut refuser la dérogation au regard des risques de nuisances pour les futurs occupants, de l'insuffisance de l'accessibilité du bâtiment par des transports alternatifs à l'usage individuel de l'automobile et des conséquences du projet sur la démographie scolaire, compte tenu des écoles existantes ou en construction, ou sur les objectifs de mixité sociale et fonctionnelle. Elle motive son refus.</p>
<p>II. - Avant d'accorder la dérogation prévue au I, l'autorité compétente pour délivrer l'autorisation d'urbanisme recueille l'avis conforme de l'autorité compétente en matière de plan local d'urbanisme ou de document en tenant lieu. Cette dernière ne peut rendre un avis défavorable qu'au regard des critères mentionnés au même I.</p>""",
    "Réécriture à droit constant : l'autorisation du changement de destination, les critères de prise en compte du projet et l'extension aux travaux autorisés sont exprimés par des phrases distinctes. L'auteur du refus et celui de l'avis conforme sont explicités. La disposition facilite déjà les transformations visées par la politique ; elle n'est pas convertie en autorisation automatique.",
    "I, II et les trois alinéas conservés, avec tous les critères de refus, les extensions et les surélévations. La coordination du dossier et le réemploi légal des pièces relèvent de L423-1 ; la fiche de parcelle opposable relève de L410-1. Les solutions techniques équivalentes nécessitent leurs dispositions dans le CCH et ne résultent pas de cette dérogation au PLU. La voie de rénovation locative de vingt-quatre mois demande une coordination de la loi n° 89-462 du 6 juillet 1989, notamment ses règles de décence et de location, et ne peut être créée ici. Les obligations de logement social ne sont pas supprimées.",
)

add(
    "L152-6-6",
    """<p>Dans le cadre des procédures prévues aux articles L. 152-6-5 et L. 152-6-11, l'autorité compétente pour délivrer l'autorisation d'urbanisme peut déroger aux règles des plans locaux d'urbanisme relatives à la proportion de logements d'une taille minimale, mentionnées à l'article L. 151-14.</p>""",
    "Réécriture à droit constant : le champ procédural est placé en tête afin d'indiquer immédiatement dans quels cas la dérogation est possible. La coquille « cadredes » est corrigée en « cadre des ». Aucune réforme de fond n'est introduite.",
    "Les deux procédures, L152-6-5 et L152-6-11, sont conservées. Le renvoi à L151-14 concerne la proportion de logements d'une taille minimale, et non les règles de mixité sociale de L151-15 ni les obligations de logement social. La dérogation n'est pas étendue à ces autres obligations.",
)

add(
    "L152-6-7",
    """<p>Dans le périmètre d'une zone d'activité économique définie à l'article L. 318-8-1, l'autorité compétente pour délivrer l'autorisation d'urbanisme peut, par décision motivée, autoriser la réalisation de logements ou d'équipements publics par dérogation aux règles relatives aux destinations fixées par le plan local d'urbanisme ou le document en tenant lieu.</p>
<p>L'autorité peut refuser l'autorisation ou l'assortir de prescriptions spéciales en tenant compte des enjeux d'intégration paysagère et architecturale du projet, de l'insuffisante accessibilité de la zone par des transports alternatifs à l'usage individuel de l'automobile et des nuisances et risques possibles provoqués par les installations et bâtiments voisins, notamment en cas d'incompatibilité avec des activités industrielles. Pour les logements, l'absence de services publics à proximité peut également justifier un refus ou des prescriptions spéciales.</p>
<p>Dans la même décision, l'autorité peut aussi déroger aux règles relatives à l'emprise au sol, au retrait, au gabarit, à la hauteur et à l'aspect extérieur des bâtiments ainsi qu'aux obligations de stationnement. Elle tient alors compte de la nature du projet, de sa zone d'implantation, de son intégration harmonieuse dans le tissu urbain existant et de sa contribution à la transformation de la zone concernée.</p>
<p>Les logements créés en application du présent article peuvent être soumis, en application de l'article L. 151-14-1, à une obligation d'usage en tant que résidence principale.</p>""",
    "Réécriture à droit constant : les finalités autorisées, les motifs de refus ou de prescriptions, les dérogations complémentaires et l'obligation possible de résidence principale restent répartis entre les quatre alinéas. Le critère des services publics est isolé dans une phrase qui le réserve explicitement aux logements. Aucune réforme de fond n'est ajoutée.",
    "Quatre alinéas conservés. Renvois à L318-8-1 et L151-14-1 maintenus et consultés dans le corpus. Les risques restent appréciés même lorsqu'ils sont seulement possibles ; les incompatibilités industrielles et les transports alternatifs ne sont pas écartés. La même décision demeure nécessaire pour les dérogations complémentaires. La résidence principale reste une possibilité fondée sur L151-14-1, non une obligation générale nouvellement créée.",
)

add(
    "L152-6-8",
    """<p>Pour permettre la réalisation d'opérations de logements destinés spécifiquement à l'usage des étudiants dans les zones urbaines ou à urbaniser, l'autorité compétente pour délivrer l'autorisation d'urbanisme peut, par décision motivée, accorder une dérogation aux règles du plan local d'urbanisme ou du document en tenant lieu.</p>""",
    "Réécriture à droit constant : la destination spécifique des logements et les zones concernées sont annoncées avant le pouvoir de dérogation, avec un sujet explicite. Aucune réforme de fond n'est apportée à ce régime particulier de logements étudiants.",
    "Maintien de la décision motivée, des seules zones urbaines ou à urbaniser et de la destination spécifiquement étudiante. La source ne limite pas cette faculté à une liste de règles du PLU ; aucune liste restrictive ni extension aux autres logements n'est inventée. Les autres législations applicables ne sont pas abrogées par cette rédaction.",
)

add(
    "L152-6-9",
    """<p>Lorsqu'elle délivre une autorisation d'urbanisme, l'autorité compétente peut autoriser le changement de destination d'un bâtiment à destination d'exploitation agricole et forestière par dérogation aux règles relatives aux destinations fixées par le plan local d'urbanisme ou le document en tenant lieu. Elle tient compte de la nature du projet et de sa zone d'implantation.</p>
<p>Avant d'accorder la dérogation prévue au premier alinéa, l'autorité compétente pour délivrer l'autorisation d'urbanisme recueille l'avis conforme de l'autorité compétente en matière de plan local d'urbanisme ou de document en tenant lieu.</p>
<p>Dans les zones agricoles, naturelles ou forestières du plan local d'urbanisme, en dehors des secteurs mentionnés à l'article L. 151-13, un changement de destination ne peut être autorisé en application du présent article que s'il est démontré que le bâtiment a cessé d'être utilisé pour une activité agricole ou forestière depuis plus de vingt ans. Ce changement est également subordonné :</p>
<p>1° En zone agricole, à l'avis conforme de la commission départementale de la préservation des espaces agricoles, naturels et forestiers prévue à l'article L. 112-1-1 du code rural et de la pêche maritime ;</p>
<p>2° En zone naturelle, à l'avis conforme de la commission départementale de la nature, des paysages et des sites.</p>""",
    "Réécriture à droit constant : l'auteur de l'autorisation, la prise en compte du projet et l'avis conforme sont exprimés directement. La condition de cessation d'activité depuis plus de vingt ans est séparée des avis complémentaires, sans modifier leur champ. La politique de transformation des bureaux n'est pas étendue au régime distinct des bâtiments agricoles et forestiers.",
    "Cinq alinéas, 1° et 2° conservés. La cessation d'activité doit être prouvée et remonter à plus de vingt ans, sans réduction du délai ni assimilation à une simple vacance du bâtiment. Maintien de L151-13 et du renvoi au code rural et de la pêche maritime L112-1-1. Lacune de précision préexistante : le troisième alinéa vise les zones forestières, mais les 1° et 2° ne désignent d'avis complémentaires qu'en zone agricole et en zone naturelle. Aucune commission n'est ajoutée par interprétation pour une zone forestière. L'avis conforme de l'autorité du PLU reste requis selon le deuxième alinéa.",
)

add(
    "L152-6-10",
    """<p>Lorsque l'autorité compétente pour délivrer l'autorisation d'urbanisme est une autre autorité que le maire, l'accord du maire de la commune d'implantation du projet est nécessaire pour accorder les dérogations prévues à la présente section. Cette exigence ne s'applique pas aux dérogations mentionnées aux articles L. 152-3, L. 152-6-3 et L. 152-6-4.</p>""",
    "Réécriture à droit constant : la condition d'accord du maire est énoncée directement, puis les trois exceptions sont présentées dans une phrase distincte au sein du même alinéa. Aucune réforme de fond des compétences locales n'est proposée.",
    "Les exceptions restent exactement L152-3, L152-6-3 et L152-6-4. Le renvoi à L152-3 inclut les adaptations mineures dans la liste source, sans requalification nouvelle. Ne pas confondre l'accord du maire avec les avis conformes des autorités du PLU exigés notamment par L152-6-5 et L152-6-9, ni avec les accords propres à L152-4.",
)

add(
    "L152-6-11",
    """<p>Dans les zones urbaines ou à urbaniser mentionnées à l'article L. 151-9, l'autorité compétente pour délivrer l'autorisation d'urbanisme peut, par décision motivée, déroger aux règles relatives aux destinations définies par le plan local d'urbanisme ou le document en tenant lieu pour autoriser la réalisation, par construction ou transformation, d'un bâtiment à destination principale d'habitation. Elle tient compte de la nature du projet et de sa zone d'implantation. La dérogation est soumise aux conditions suivantes :</p>
<p>1° Le terrain est détenu par une personne publique ou une entreprise publique, ou a été cédé par l'une ou l'autre à un tiers en vue de loger ou d'héberger les agents publics et salariés mentionnés au 2° du présent article ;</p>
<p>2° Au moins la moitié des locaux d'habitation créés est réservée au bénéfice des agents publics et salariés mentionnés au I de l'article L. 442-7 du code de la construction et de l'habitation.</p>
<p>Le propriétaire des bâtiments mentionnés au premier alinéa du présent article justifie chaque année auprès de l'autorité compétente que la condition du 2° reste satisfaite. Si cette condition n'est plus remplie ou si la déclaration n'a pas été faite, l'autorité compétente met le propriétaire en demeure de mettre le bâtiment en conformité ou de fournir la déclaration justificative dans un délai de trois mois. Si cette mise en demeure reste sans effet à l'expiration du délai imparti, le bâtiment est réputé non conforme à l'autorisation accordée dans les conditions du premier alinéa.</p>""",
    "Réécriture à droit constant : la faculté de déroger, les critères d'appréciation et les deux conditions sont distingués sans changer d'alinéa cible. L'obligation annuelle du propriétaire et les suites de sa défaillance sont formulées dans l'ordre de la procédure. Aucune réforme de fond ni extension à tous les salariés n'est introduite.",
    "Quatre alinéas et 1° et 2° conservés. Maintien du terrain public ou cédé à un tiers pour la finalité indiquée, du seuil d'au moins la moitié des locaux d'habitation, de la justification annuelle et du délai de trois mois après mise en demeure. Les renvois au premier alinéa et au 2° restent à leur place. Le corpus CCH L442-7 consulté comporte un II et des références à un I, mais n'affiche pas la marque I au début du texte fourni : anomalie de présentation préexistante à contrôler, sans modifier ici le renvoi au I. Les bénéficiaires ne sont pas redéfinis. L152-6-6 conserve sa dérogation spécifique à la proportion de logements d'une taille minimale.",
)

add(
    "L152-7",
    """<p>Un délai d'un an court à compter de l'approbation du plan local d'urbanisme ou, pour une servitude d'utilité publique nouvelle définie à l'article L. 151-43, de l'institution de cette servitude. A l'expiration de ce délai, seules les servitudes annexées au plan ou publiées sur le portail national de l'urbanisme prévu à l'article L. 133-1 peuvent être opposées aux demandes d'autorisation d'occupation du sol.<br />Toutefois, si le plan a été approuvé ou la servitude instituée avant la publication du décret qui établit ou complète la liste mentionnée à l'article L. 151-43, le délai d'un an commence à courir à la date de cette publication.</p>""",
    "Réécriture à droit constant : le point de départ du délai est séparé de son effet sur l'opposabilité, et le second alinéa présente directement le point de départ particulier lié au décret. Les deux voies de publicité restent alternatives. Aucune réforme de fond de la publicité des servitudes n'est introduite.",
    "Deux alinéas conservés ; délai d'un an maintenu dans les deux hypothèses et renvois à L151-43 et L133-1 conservés. La note source précise l'entrée en vigueur au 1er janvier 2020, en application du II de l'article 2 de l'ordonnance n° 2013-1184 du 19 décembre 2013, des dispositions issues de son article 1er et anciennement codifiées à L126-1, alinéa 3. Cette date historique n'est pas une date d'entrée en vigueur de la réforme proposée. Coordonner l'information de la fiche de parcelle prévue à L410-1 sans rendre opposables des servitudes qui ne satisfont pas au présent article.",
)

add(
    "L152-8",
    """<p>Les actes pris au titre de la police du stationnement et de la circulation, ainsi que les actes et décisions relatifs à la voirie et à la gestion du domaine public routier, doivent être compatibles avec les dispositions du plan local d'urbanisme tenant lieu de plan de mobilité ou être mis en compatibilité avec elles, dans les conditions prévues aux articles L. 1214-5 et L. 1214-6 du code des transports.</p>""",
    "Réécriture à droit constant : l'exigence de compatibilité et, si nécessaire, de mise en compatibilité est exprimée comme une obligation. Les catégories d'actes et le PLU tenant lieu de plan de mobilité restent inchangés dans leur champ. Aucune réforme de fond n'est proposée.",
    "Un alinéa conservé ; maintien des deux renvois aux articles L1214-5 et L1214-6 du code des transports. La note source rattache l'entrée en vigueur au 1er janvier 2021 au XI de l'article 16 de la loi n° 2019-1428 du 24 décembre 2019. Cette disposition historique est prise en compte et ne fixe aucune date future pour la politique du logement.",
)

add(
    "L152-9",
    """<p>Lorsqu'un programme local de l'habitat ou un plan de mobilité arrive à échéance, ou lorsque son délai de validité expire avant la délibération approuvant un plan local d'urbanisme tenant lieu de programme local de l'habitat ou de plan de mobilité, ce programme ou ce plan peut être prorogé jusqu'à l'approbation du plan local d'urbanisme. L'organe délibérant de l'établissement public de coopération intercommunale compétent décide cette prorogation par délibération, après accord de l'autorité administrative compétente de l'Etat, pour une durée de trois ans renouvelable une fois.<br />La même possibilité de prorogation s'applique lorsqu'un plan local d'urbanisme élaboré par un établissement public de coopération intercommunale est révisé pour y intégrer les dispositions tenant lieu de programme local de l'habitat ou de plan de mobilité.</p>""",
    "Réécriture à droit constant : les hypothèses d'échéance restent exprimées, l'organe qui décide la prorogation devient le sujet de la phrase et le second alinéa précise la portée de la même possibilité lors d'une révision du PLU. Aucune réforme de fond des durées ou des accords n'est apportée.",
    "Deux alinéas conservés. La prorogation demeure liée à l'approbation du PLU, pour trois ans renouvelables une seule fois, avec délibération de l'EPCI et accord de l'autorité administrative compétente de l'Etat. Les hypothèses d'arrivée à échéance et d'expiration avant la délibération sont maintenues malgré leur recoupement rédactionnel dans la source. La note source prévoit l'entrée en vigueur au 1er janvier 2021 au titre du XI de l'article 16 de la loi n° 2019-1428 du 24 décembre 2019 ; elle ne constitue pas une transition nouvelle.",
)

add(
    "L153-1",
    """<p>Le plan local d'urbanisme doit couvrir l'intégralité du territoire :<br />1° De l'établissement public de coopération intercommunale compétent en matière de plan local d'urbanisme, de document d'urbanisme en tenant lieu et de carte communale ;<br />2° De la commune, lorsque celle-ci élabore le plan et n'est pas membre d'un tel établissement public.<br />Toutefois, les parties de ces territoires couvertes par un plan de sauvegarde et de mise en valeur approuvé sont exclues du périmètre du plan local d'urbanisme.</p>""",
    "Réécriture à droit constant : le caractère obligatoire de la couverture territoriale est explicité et l'exception relative au plan de sauvegarde et de mise en valeur est exprimée directement. Les deux situations de compétence restent numérotées. Aucune réforme de fond des périmètres n'est introduite.",
    "Maintien des 1° et 2° et de l'alinéa d'exception. Le plan de sauvegarde et de mise en valeur doit être approuvé pour justifier l'exclusion ; un simple projet ne suffit pas. Les dérogations temporaires propres aux communautés issues d'une fusion demeurent régies par L153-3 et ne sont pas supprimées par cette rédaction générale.",
)

add(
    "L153-2",
    """<p>L'établissement public de coopération intercommunale compétent choisit le moment où il engage une procédure d'élaboration ou de révision d'un plan local d'urbanisme couvrant l'intégralité de son territoire. Il doit toutefois l'engager au plus tard lorsqu'il révise, en application de l'article L. 153-31, l'un des plans locaux d'urbanisme applicables dans son périmètre. Conformément au VI de l'article 1er de la loi n° 2025-1129 du 26 novembre 2025, la règle entrée en vigueur le 26 mai 2026 ne s'applique pas aux procédures d'évolution des schémas de cohérence territoriale ou des plans locaux d'urbanisme en cours à cette date.</p>""",
    "Réécriture à droit constant : le choix initial de l'établissement et l'obligation d'engager la procédure au plus tard lors de la révision sont distingués en deux phrases. La réserve transitoire encore pertinente, donnée dans la note source, est rendue explicite dans le même alinéa. Il s'agit du maintien de cette transition historique et non d'une date ou d'une réforme de fond nouvelle.",
    "Renvoi à L153-31 conservé et consulté dans le corpus. La note source fixe l'entrée en vigueur six mois après la promulgation de la loi n° 2025-1129 du 26 novembre 2025, soit le 26 mai 2026, et exclut les procédures d'évolution des SCoT ou des PLU en cours à cette date. La dernière phrase reprend cette réserve issue du VI de son article 1er ; elle est ajoutée au sein de l'alinéa existant, sans déplacement d'une cible. Ne pas confondre ces six mois historiques avec la transition d'organisation des services prévue par la coordination de L423-1. Maintenir l'articulation avec la dérogation de L153-3.",
)

add(
    "L153-3",
    """<p>Une communauté de communes ou d'agglomération issue de la fusion d'un ou plusieurs établissements publics de coopération intercommunale compétents en matière de plan local d'urbanisme, de document en tenant lieu et de carte communale avec un ou plusieurs établissements publics de coopération intercommunale ne détenant pas cette compétence peut, pendant les cinq ans qui courent à compter de sa création et par dérogation aux articles L. 153-1 et L. 153-2, prescrire la révision d'un plan local d'urbanisme existant. Elle n'est alors pas tenue d'engager l'élaboration d'un plan local d'urbanisme couvrant l'ensemble de son périmètre.</p>""",
    "Réécriture à droit constant : les caractéristiques de la fusion et la période de cinq ans encadrent directement la faculté de prescrire une révision ; la dispense d'engager l'élaboration d'un plan couvrant tout le périmètre fait l'objet d'une phrase distincte. Aucune réforme de fond de cette exception temporaire n'est proposée.",
    "Un alinéa conservé. La période reste de cinq ans à compter de la création, sans renouvellement ni report de son point de départ. Le dispositif reste réservé aux communautés de communes ou d'agglomération issues d'une fusion mêlant des EPCI compétents et non compétents. Les renvois à L153-1 et L153-2 et le caractère existant du PLU révisé sont conservés.",
)


sources = json.loads(Path("source.json").read_text())
assert len(sources) == 24
assert set(drafts) == {a["number"] for a in sources}
answer = []
for article in sources:
    row = {k: article[k] for k in ("code_id", "source_id", "source_sha256", "number")}
    row.update(drafts[article["number"]])
    answer.append(row)

Path("answer.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")
print(f"answer.json : {len(answer)} articles")
