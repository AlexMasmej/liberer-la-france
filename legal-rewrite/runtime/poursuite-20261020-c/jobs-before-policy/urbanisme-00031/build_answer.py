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
    "L421-3",
    """<p>La démolition d'une construction existante ne peut commencer qu'après la délivrance d'un permis de démolir lorsque la construction relève d'une protection particulière définie par décret en Conseil d'État ou se situe dans une commune, ou une partie de commune, où le conseil municipal a instauré ce permis.</p>""",
    "Réécriture à droit constant : l'interdiction de commencer la démolition sans permis préalable est exprimée directement, avec les deux fondements alternatifs de cette obligation. Aucune dispense nouvelle n'est créée.",
    "Les deux champs sont conservés : protection particulière définie par décret en Conseil d'État, ou instauration du permis par le conseil municipal sur tout ou partie de la commune. La coordination du dossier prévue à L423-1 ne modifie pas ce champ d'application.",
)

add(
    "L421-4",
    """<p>Un décret en Conseil d'État établit la liste des constructions, aménagements, installations et travaux soumis à déclaration préalable, y compris ceux mentionnés à l'article 40 de la loi n° 2023-175 du 10 mars 2023 relative à l'accélération de la production d'énergies renouvelables. Cette formalité concerne ceux dont les dimensions, la nature ou la localisation ne justifient pas d'exiger un permis.</p>
<p>Le même décret détermine les cas dans lesquels les clôtures sont également soumises à déclaration préalable.</p>
<p>Il énumère aussi les exceptions à l'obligation de déclaration préalable des coupes et abattages d'arbres. Cette obligation concerne les bois, forêts ou parcs situés dans les communes où l'établissement d'un plan local d'urbanisme a été prescrit, ainsi que tout espace boisé identifié en application des articles L. 113-1, L. 151-19 ou L. 151-23 ou classé en application de l'article L. 113-1.</p>""",
    "Réécriture à droit constant en trois alinéas conservés : distinction entre la liste des opérations déclarées, le cas des clôtures et les exceptions concernant les arbres. Les critères de dimensions, de nature et de localisation restent ceux de la source.",
    "Maintien de l'article 40 de la loi n° 2023-175 du 10 mars 2023 et de tous les renvois relatifs aux espaces boisés. Le dernier alinéa conserve la distinction entre espaces identifiés et espaces classés, y compris le double emploi de L113-1 dans la source. Aucune dispense supplémentaire pour la densification ou la transformation de bureaux.",
)

add(
    "L421-5",
    """<p>Un décret en Conseil d'État fixe la liste des constructions, aménagements, installations et travaux dispensés de toute formalité au titre du présent code, par dérogation aux articles L. 421-1 à L. 421-4. Ces dispenses reposent sur les motifs suivants :</p>
<p>a) Leur importance est très faible ;</p>
<p>b) Leur maintien en place est de courte durée ou ils présentent un caractère temporaire compte tenu de l'usage auquel ils sont destinés ;</p>
<p>c) Ils doivent être tenus secrets pour des raisons de sûreté ou leur confidentialité doit être préservée pour sauvegarder les intérêts de la défense nationale ;</p>
<p>d) Leur contrôle est exclusivement assuré par une autre autorisation ou une autre législation ;</p>
<p>e) Leur nature et leur implantation en mer, sur le domaine public maritime immergé au-delà de la laisse de la basse mer, justifient cette dispense.</p>""",
    "Réécriture à droit constant : le décret et la portée dérogatoire sont explicités avant les cinq motifs, puis chaque lettre énonce directement la situation concernée. Le champ des dispenses n'est pas étendu.",
    "Lettres a à e et ordre des six alinéas conservés, notamment pour le renvoi aux seuls b et e par L421-8. Les exigences de sûreté et de défense nationale restent distinctes ; au e, nature et implantation restent cumulatives. Les dispenses demeurent fixées par décret, et ne résultent pas directement de la seule énumération.",
)

add(
    "L421-5-1",
    """<p>Aucune formalité au titre du présent code n'est exigée pour les travaux nécessaires à l'exécution de l'arrêté pris en application de l'article L. 121-22-5 qui ordonne la démolition des constructions et la remise en état du terrain.</p>""",
    "Réécriture à droit constant : la dispense est formulée directement et rattachée aux travaux d'exécution de l'arrêté de démolition et de remise en état, sans étendre son objet.",
    "Renvoi à L121-22-5 conservé. L'exemption vise les seuls travaux nécessaires à l'exécution de l'arrêté ; elle ne supprime ni cet arrêté ni les obligations du propriétaire prévues par l'article de renvoi. Coordination avec l'exception de L421-8 maintenue.",
)

add(
    "L421-5-2",
    """<p>Les travaux nécessaires pour exécuter l'obligation d'enlèvement et de remise en état du terrain prévue à l'article L. 111-32 ne sont soumis à aucune formalité au titre du présent code.</p>""",
    "Réécriture à droit constant : la phrase distingue l'obligation d'enlèvement et de remise en état des formalités dont ses travaux d'exécution sont dispensés.",
    "L111-32 est conservé comme fondement de l'obligation ; la dispense ne vaut que pour les travaux nécessaires à son exécution. Articulation maintenue avec les prescriptions de L421-6-2 et l'exception de L421-8.",
)

add(
    "L421-5-3",
    """<p>I. – Par dérogation aux articles L. 421-1 à L. 421-5, les constructions temporaires et démontables exclusivement affectées au relogement temporaire d'occupants délogés à titre définitif ou provisoire sont dispensées de toute formalité au titre du présent code. Cette dispense s'applique pendant la durée de l'opération, sans dépasser l'échéance fixée par l'accord mentionné au II du présent article. Elle couvre les situations suivantes :<br/>– le relogement rendu nécessaire par des opérations d'aménagement ayant pour objet la lutte contre l'habitat dégradé ou indigne ou réalisées dans le cadre du nouveau programme national de renouvellement urbain définies à l'article 9-1 de la loi n° 2003-710 du 1er août 2003 d'orientation et de programmation pour la ville et la rénovation urbaine ;<br/>– le relogement rendu nécessaire par des actions de lutte contre l'habitat indigne réalisées dans le cadre d'une opération programmée d'amélioration de l'habitat mentionnée à l'article L. 303-1 du code de la construction et de l'habitation ou d'une opération de requalification des copropriétés dégradées mentionnée à l'article L. 741-1 du même code ;<br/>– le relogement rendu nécessaire dans le cadre des procédures d'expropriation mentionnées aux articles L. 511-1 et L. 512-1 du code de l'expropriation pour cause d'utilité publique.</p>
<p>Les constructions mentionnées au premier alinéa du présent I doivent respecter des conditions minimales de confort et d'habitabilité fixées par décret.</p>
<p>Le présent article ne porte pas atteinte aux dispositions des articles L. 314-1 à L. 314-9 du présent code relatives à la protection des occupants ni, le cas échéant, à celles des articles L. 423-1 à L. 423-5 du code de l'expropriation pour cause d'utilité publique relatives aux droits de relogement.</p>
<p>II. – Le maître d'ouvrage soumet l'implantation des constructions mentionnées au I à l'accord préalable du maire de la commune d'implantation, au plus tard un mois avant la date de début d'implantation. L'accord indique la nature et l'usage du projet de construction ainsi que les dates de début et de fin d'implantation. Il peut être renouvelé dans les mêmes conditions, au plus tard trois mois avant l'expiration de sa durée de validité.</p>
<p>III. – Le maître d'ouvrage doit remettre les lieux occupés dans leur état initial avant l'expiration du délai mentionné au I ou, si elle est antérieure, avant la date fixée au II.</p>
<p>IV. – Le présent article ne s'applique pas dans les zones où un plan de prévention des risques naturels prévisibles approuvé interdit de construire ou d'aménager, ni dans celles où ce plan soumet ces opérations à des conditions de réalisation, d'utilisation ou d'exploitation.</p>""",
    "Réécriture à droit constant : le premier alinéa distingue l'objet exclusif des constructions, la limite de durée et les situations ouvrant la dispense, présentées par retours à la ligne sans créer de subdivision numérotée. Les autres alinéas identifient les obligations du maître d'ouvrage, le contenu de l'accord et les exclusions liées aux risques. Les subdivisions I à IV et les six alinéas sont conservés.",
    "Tous les dispositifs de relogement et renvois sont conservés, dont la loi n° 2003-710 du 1er août 2003, les deux procédures d'expropriation et les droits des occupants. Maintien des délais d'un mois et de trois mois, du renouvellement facultatif et de la remise en état avant la plus proche des échéances. Ambiguïté préexistante au II : la source rattache le délai d'un mois à une implantation soumise à accord « par le maître d'ouvrage », sans distinguer clairement la saisine du maire et la délivrance de l'accord. La proposition conserve l'exigence de soumission à accord préalable et n'ajoute ni délai de réponse ni accord tacite ; ce rattachement doit être précisé par une coordination expresse si un choix de fond est retenu. Le IV exclut aussi les zones seulement soumises à conditions par le plan approuvé, et pas uniquement celles où construire est interdit ; cette portée est maintenue.",
)

add(
    "L421-6",
    """<p>L'autorité compétente ne peut délivrer un permis de construire ou d'aménager que si les travaux projetés respectent les dispositions législatives et réglementaires relatives à l'utilisation des sols, à l'implantation, à la destination, à la nature, à l'architecture, aux dimensions et à l'assainissement des constructions ainsi qu'à l'aménagement de leurs abords. Ces travaux ne doivent pas non plus être incompatibles avec une déclaration d'utilité publique.</p>
<p>Si les travaux envisagés sont de nature à compromettre la protection ou la mise en valeur du patrimoine bâti ou non bâti, du patrimoine archéologique, des quartiers, des monuments ou des sites, l'autorité compétente peut refuser le permis de démolir ou subordonner sa délivrance au respect de prescriptions spéciales.</p>""",
    "Réécriture à droit constant : les conditions de délivrance du permis de construire ou d'aménager sont distinguées de l'exigence de non-incompatibilité avec une déclaration d'utilité publique. Le second alinéa énonce d'abord le risque patrimonial puis les deux décisions possibles sur la démolition.",
    "Deux alinéas conservés et aucune catégorie de règles ou de patrimoine supprimée. Maintien de la non-incompatibilité avec une déclaration d'utilité publique, sans la transformer en exigence différente de conformité. Les renvois de L421-7 et L421-8 restent opérants. Le dossier coordonné n'écarte aucune de ces conditions de fond.",
)

add(
    "L421-6-1",
    """<p>Le permis de construire, le permis d'aménager ou la décision de non-opposition à déclaration préalable doit prescrire la consignation de la somme prévue à l'article L. 121-22-5.</p>""",
    "Réécriture à droit constant : les trois catégories de décisions sont nommées séparément et l'obligation de prescrire la consignation est exprimée directement.",
    "Renvoi à L121-22-5 conservé pour le champ, le montant et les modalités de la consignation ; aucun montant nouveau et aucune garantie de substitution ne sont institués. Articulation avec le 7° de L421-9 préservée.",
)

add(
    "L421-6-2",
    """<p>Le permis de construire ou la décision de non-opposition à déclaration préalable prescrit l'enlèvement des ouvrages de production d'électricité à partir de l'énergie solaire ainsi que la remise en état du terrain, conformément à l'obligation prévue à l'article L. 111-32. Il précise notamment la durée mentionnée au 2° du même article L. 111-32.</p>""",
    "Réécriture à droit constant : l'enlèvement des ouvrages et la remise en état du terrain sont formulés comme deux composantes de la prescription, puis la précision de durée fait l'objet d'une phrase distincte.",
    "Le raccord grammatical défectueux de la source (« l'enlèvement […] et de remise en état […] prévue ») est explicité sans changer l'obligation renvoyant à L111-32. Le renvoi au 2° de cet article et les seules décisions visées, permis de construire et non-opposition, sont maintenus. Aucune durée nouvelle n'est fixée.",
)

add(
    "L421-7",
    """<p>Pour les constructions, aménagements, installations et travaux soumis à déclaration préalable, l'autorité compétente doit s'opposer à leur exécution ou leur imposer des prescriptions si les conditions de l'article L. 421-6 ne sont pas réunies.</p>""",
    "Réécriture à droit constant : le champ de la déclaration préalable est placé en tête et le caractère obligatoire de l'opposition ou des prescriptions demeure explicite.",
    "Renvoi à l'ensemble des conditions de L421-6 conservé. Aucune priorité nouvelle entre opposition et prescriptions, aucune autorisation automatique et aucune dispense liée au dossier coordonné ne sont créées.",
)

add(
    "L421-8",
    """<p>Les constructions, aménagements, installations et travaux dispensés de toute formalité au titre du présent code doivent néanmoins respecter les dispositions mentionnées à l'article L. 421-6. Cette obligation ne s'applique pas aux constructions et aux travaux mentionnés aux b et e de l'article L. 421-5 ni à ceux mentionnés aux articles L. 421-5-1, L. 421-5-2 et L. 421-5-3.</p>""",
    "Réécriture à droit constant : la règle de respect des dispositions de fond précède ses exceptions, dans le même alinéa. La dispense de formalité et la dispense de conformité sont ainsi distinguées sans élargir les exceptions.",
    "Renvois aux seuls b et e de L421-5 et aux trois articles L421-5-1 à L421-5-3 maintenus. L'exception demeure formulée pour les constructions et travaux visés par la source ; elle n'est pas étendue aux autres lettres de L421-5.",
)

add(
    "L421-9",
    """<p>Lorsque l'achèvement d'une construction remonte à plus de dix ans, son irrégularité initiale au regard du droit de l'urbanisme ne peut justifier ni un refus de permis de construire ni une décision d'opposition à déclaration préalable.</p>
<p>La règle du premier alinéa ne s'applique pas dans les cas suivants :</p>
<p>1° Lorsque, du fait de sa situation, la construction peut exposer ses usagers ou des tiers à un risque de mort ou de blessures susceptibles d'entraîner une mutilation ou une infirmité permanente ;</p>
<p>2° Lorsqu'une action en démolition a été engagée dans les conditions de l'article L. 480-13 ;</p>
<p>3° Lorsque la construction se situe dans un parc national créé en application des articles L. 331-1 et suivants du code de l'environnement ou dans un site classé en application des articles L. 341-2 et suivants du même code ;</p>
<p>4° Lorsque la construction se trouve sur le domaine public ;</p>
<p>5° Lorsqu'un permis de construire était requis mais que la construction a été réalisée sans qu'aucun permis de construire ait été obtenu ;</p>
<p>6° Lorsque la construction se situe dans les zones mentionnées au 1° du II de l'article L. 562-1 du code de l'environnement ;</p>
<p>7° Lorsque la construction a été réalisée sans que la somme prescrite par l'autorisation d'urbanisme ait été consignée.</p>""",
    "Réécriture à droit constant : la portée de l'ancienneté de la construction est exprimée à partir des motifs de refus interdits ; chacune des sept exceptions est formulée comme une condition distincte. Numérotation et ordre des alinéas conservés.",
    "Le délai reste strictement supérieur à dix ans depuis l'achèvement ; il ne vaut pas régularisation générale. Les sept exceptions, le 1° du II de L562-1 et les mentions « et suivants » des deux séries du code de l'environnement sont préservés. Le 5° conserve l'absence de tout permis requis, et le 7° l'absence de consignation prescrite, sans les remplacer par de simples irrégularités de conformité.",
)

add(
    "L422-1",
    """<p>La compétence pour délivrer les permis de construire, d'aménager ou de démolir et pour statuer sur les projets soumis à déclaration préalable appartient aux autorités suivantes :</p>
<p>a) Le maire, au nom de la commune, dans les communes dotées d'un plan local d'urbanisme ou d'un document d'urbanisme en tenant lieu, ainsi que dans celles qui se sont dotées d'une carte communale après la date de publication de la loi n° 2014-366 du 24 mars 2014 pour l'accès au logement et un urbanisme rénové. Dans les communes qui se sont dotées d'une carte communale avant cette date, le maire exerce cette compétence au nom de la commune après délibération du conseil municipal. En l'absence de décision du conseil municipal, il l'exerce au nom de la commune à compter du 1er janvier 2017. Le transfert de compétence à la commune est définitif ;</p>
<p>b) Le préfet ou le maire, au nom de l'État, dans les autres communes.</p>
<p>Les demandes de permis de construire, d'aménager ou de démolir et les déclarations préalables sur lesquelles aucune décision n'a été prise à la date du transfert de compétence demeurent soumises aux règles d'instruction et de compétence applicables à la date de leur dépôt.</p>""",
    "Réécriture à droit constant : les actes concernés, l'autorité et le nom au titre duquel elle agit sont explicités. La chronologie relative aux cartes communales et le maintien des règles des dossiers en cours sont conservés dans leurs alinéas respectifs.",
    "Maintien de la loi n° 2014-366 du 24 mars 2014, du critère de sa date de publication et du 1er janvier 2017. La transition des demandes déjà déposées et le caractère définitif du transfert ne sont pas supprimés au motif de leur ancienneté. Les exceptions de L422-2 et L422-3-1, la délégation de L422-3 et les règles du dossier coordonné ne sont pas assimilées à un nouveau transfert de compétence.",
)

add(
    "L422-2",
    """<p>Par exception au a de l'article L. 422-1, l'autorité administrative de l'État statue sur les projets portant sur les opérations ou ouvrages suivants :</p>
<p>a) Les travaux, constructions et installations réalisés pour le compte d'États étrangers ou d'organisations internationales, de l'État, de ses établissements publics ou de ses concessionnaires ;</p>
<p>b) Les ouvrages de production, de transport, de distribution et de stockage d'énergie, ainsi que ceux utilisant des matières radioactives. Un décret en Conseil d'État détermine la nature et l'importance des ouvrages concernés ;</p>
<p>c) Les travaux, constructions et installations réalisés dans les périmètres des opérations d'intérêt national mentionnées à l'article L. 132-1, à l'exception des secteurs délimités en application de l'article L. 102-14 ;</p>
<p>d) Les opérations de logement situées dans les secteurs arrêtés par le préfet en application du deuxième alinéa de l'article L. 302-9-1 du code de la construction et de l'habitation et relevant des catégories de constructions ou d'aménagements énumérées dans l'arrêté pris en application du même article L. 302-9-1. Sont également concernées les opérations ayant fait l'objet, pendant la durée d'application de cet arrêté, d'une convention fondée sur le sixième alinéa du même article L. 302-9-1 ;</p>
<p>e) Les logements, locaux d'hébergement et résidences hôtelières à vocation sociale construits ou exploités par des sociétés de construction dont l'État détient au moins un tiers du capital ;</p>
<p>f) Les ouvrages, constructions ou installations visés à l'article L. 2124-18 du code général de la propriété des personnes publiques ;</p>
<p>g) Les travaux, constructions et installations réalisés pour le compte de la société SNCF Réseau mentionnée à l'article L. 2111-9 du code des transports ou de sa filiale mentionnée au 5° de cet article, dans le cadre des missions de service public que ce même article leur confie ;</p>
<p>h) Les travaux, installations, constructions et aménagements d'un projet qualifié de projet d'intérêt national majeur par décret.</p>
<p>Lorsque le préfet prend la décision, il recueille l'avis du maire ou du président de l'établissement public de coopération intercommunale compétent.</p>""",
    "Réécriture à droit constant : les huit catégories de compétence de l'État sont conservées, avec séparation des deux branches du d et clarification de la mission de SNCF Réseau au g. La consultation finale reste distincte des critères de compétence.",
    "Lettres a à h et dix alinéas conservés. Maintien du seuil d'au moins un tiers du capital, du 5° de L2111-9 et des deuxième et sixième alinéas de L302-9-1, vérifiés dans le corpus public. Le renvoi du c à L132-1, article général mentionnant les opérations d'intérêt national, est conservé ; leur qualification relève de L102-12 et l'exception sectorielle de L102-14, sans substitution silencieuse de référence. L'avis final reste simple, non conforme. Le dossier coordonné de L423-1 ne transfère aucune de ces compétences à la commune et ne dispense pas des obligations de logement social.",
)

add(
    "L422-3",
    """<p>Une commune membre d'un établissement public de coopération intercommunale peut lui déléguer, avec son accord, la compétence prévue au a de l'article L. 422-1. Le président de l'établissement exerce alors cette compétence au nom de l'établissement.</p>
<p>Après chaque renouvellement du conseil municipal ou après l'élection d'un nouveau président de l'établissement public, la délégation de compétence doit être confirmée dans les mêmes formes.</p>
<p>Pour chaque demande de permis et chaque déclaration préalable, le maire transmet son avis au président de l'établissement public.</p>""",
    "Réécriture à droit constant : l'accord de l'établissement et l'exercice de la compétence par son président sont présentés en deux phrases. Les événements imposant la confirmation et l'avis du maire restent dans leurs alinéas d'origine.",
    "Trois alinéas et renvoi au a de L422-1 conservés. L'accord de l'établissement, la confirmation après chacun des événements prévus et l'avis du maire sur chaque dossier sont maintenus. La délégation de compétence ne doit pas être confondue avec la mutualisation technique de L423-3 ou le dossier coordonné de L423-1.",
)

add(
    "L422-3-1",
    """<p>Dans le périmètre d'une grande opération d'urbanisme au sens de l'article L. 312-3, il est dérogé à l'article L. 422-1, sauf dans le cas prévu à l'article L. 312-5-1. La compétence pour délivrer les permis de construire, d'aménager ou de démolir et pour statuer sur les projets soumis à déclaration préalable appartient au maire de Paris, au président de la métropole de Lyon ou au président d'un établissement public mentionné aux 1° ou 2° de l'article L. 312-1 ayant décidé de la qualification de grande opération d'urbanisme en application de l'article L. 312-4.</p>""",
    "Réécriture à droit constant : une première phrase définit le périmètre et les deux articulations dérogatoires ; la seconde regroupe les actes relevant de la compétence spéciale puis les autorités. L'unique alinéa est conservé.",
    "Renvois à L312-3, L312-5-1, aux seuls 1° ou 2° de L312-1 et à L312-4 conservés. L'exception de L312-5-1 permettant l'exercice selon L422-1 dans tout ou partie du périmètre a été vérifiée dans le corpus ; aucune compétence spéciale supplémentaire n'est créée. La qualification de grande opération d'urbanisme demeure nécessaire.",
)

add(
    "L422-4",
    """<p>Pour statuer sur les demandes de permis ou les déclarations préalables, l'autorité compétente recueille l'accord ou l'avis des autorités ou commissions compétentes. Elle procède notamment à ces consultations dans les cas prévus au chapitre V du titre II du présent livre.</p>""",
    "Réécriture à droit constant : l'obligation de recueillir les accords ou avis est séparée de la référence aux cas prévus par le code, qui conserve son caractère non exhaustif.",
    "Renvoi au chapitre V du titre II du livre IV conservé. La distinction entre accord et avis est maintenue ; leur réunion dans un dossier coordonné ne les fusionne pas et ne vaut pas délivrance d'une autre autorisation. Les garanties du patrimoine et des autres législations demeurent applicables.",
)

add(
    "L422-5",
    """<p>Lorsqu'il est compétent pour statuer sur le projet, le maire ou le président de l'établissement public de coopération intercommunale doit recueillir l'avis conforme du préfet si le projet se situe :</p>
<p>a) Sur une partie du territoire communal qui n'est couverte ni par une carte communale, ni par un plan local d'urbanisme, ni par un document d'urbanisme en tenant lieu ;</p>
<p>b) Dans un périmètre institué à l'initiative d'une personne autre que la commune et dans lequel les mesures de sauvegarde prévues au deuxième alinéa de l'article L. 424-1 peuvent être appliquées.</p>""",
    "Réécriture à droit constant : l'obligation d'avis conforme est énoncée expressément, puis les deux conditions territoriales sont reformulées sans modifier leur alternative. Au b, l'initiative du périmètre précède son régime de sauvegarde.",
    "Lettres a et b et trois alinéas conservés. L'avis reste conforme et non simple. Le renvoi exact au deuxième alinéa de L424-1 est maintenu ; le b exige la possibilité d'appliquer les mesures, sans exiger qu'elles aient déjà été appliquées. Le dossier coordonné ne dispense pas de cet avis.",
)

add(
    "L422-5-1",
    """<p>Si le projet concerne des constructions et installations destinées à l'exercice d'un culte, le maire ou le président de l'établissement public de coopération intercommunale, lorsqu'il est compétent, doit recueillir l'avis du représentant de l'État dans le département.</p>""",
    "Réécriture à droit constant : le champ des projets cultuels est placé en tête de la phrase, suivi de l'autorité tenue à la consultation et de la condition de sa compétence.",
    "L'avis du représentant de l'État reste un avis simple ; il n'est pas assimilé aux avis conformes des articles L422-5 et L422-6. Aucune extension à d'autres destinations ni dispense dans le cadre du dossier coordonné.",
)

add(
    "L422-6",
    """<p>Lorsqu'une carte communale, un plan local d'urbanisme ou un document d'urbanisme en tenant lieu est annulé par une juridiction, abrogé ou fait l'objet d'une constatation d'illégalité par la juridiction administrative ou l'autorité compétente, le maire ou le président de l'établissement public de coopération intercommunale doit recueillir l'avis conforme du préfet si cette décision ne remet pas en vigueur un document d'urbanisme antérieur. Cette obligation porte sur les demandes de permis et les déclarations préalables postérieures à l'annulation, à l'abrogation ou à la constatation d'illégalité.</p>""",
    "Réécriture à droit constant : les trois événements affectant le document d'urbanisme, l'absence de remise en vigueur d'un document antérieur et le champ temporel des demandes sont distingués en deux phrases dans le même alinéa.",
    "Maintien du caractère conforme de l'avis, des trois types de documents, des trois causes de déclenchement et de la condition tenant à l'absence de remise en vigueur d'un document antérieur. La règle reste limitée aux demandes et déclarations postérieures à l'événement ; aucune rétroactivité n'est introduite.",
)

add(
    "L422-7",
    """<p>Lorsque le maire ou le président de l'établissement public de coopération intercommunale est intéressé, personnellement ou comme mandataire, au projet soumis à demande de permis ou à déclaration préalable, le conseil municipal ou l'organe délibérant de l'établissement public, selon le cas, désigne un autre de ses membres pour prendre la décision.</p>""",
    "Réécriture à droit constant : les deux formes d'intérêt au projet sont rapprochées et le lien entre l'autorité intéressée et l'organe qui désigne son remplaçant est explicité.",
    "La désignation porte toujours sur un autre membre du conseil municipal ou de l'organe délibérant concerné. Les projets soumis à permis comme ceux soumis à déclaration préalable restent couverts. La coordination technique de l'instruction ne remplace pas cette règle de décision.",
)

add(
    "L422-8",
    """<p>Le maire ou le président de l'établissement public de coopération intercommunale compétent peut recourir gratuitement aux services déconcentrés de l'État pour l'étude technique des demandes de permis ou des déclarations préalables dont il estime qu'elles justifient l'assistance technique de ces services. Cette faculté est ouverte lorsque la commune compte moins de 10 000 habitants et n'appartient pas à un établissement public de coopération intercommunale regroupant 10 000 habitants ou plus, ou lorsque l'établissement public de coopération intercommunale compétent regroupe des communes dont la population totale est inférieure à 10 000 habitants. Pendant la mise à disposition, les services et leurs personnels agissent en concertation avec le maire ou le président de l'établissement public. Celui-ci leur adresse toutes les instructions nécessaires à l'exécution des tâches qu'il leur confie.</p>
<p>Les services déconcentrés de l'État peuvent également apporter gratuitement une assistance juridique et technique ponctuelle, pour l'instruction des demandes de permis, à toutes les communes et à tous les établissements publics de coopération intercommunale compétents.</p>""",
    "Réécriture à droit constant en deux alinéas : le recours technique gratuit est présenté avant ses deux conditions alternatives de population, puis ses modalités de fonctionnement. L'assistance ponctuelle ouverte à toutes les collectivités compétentes reste distincte. Les dispositions transitoires de la loi de 2014 figurant en note sont explicitées dans review_notes sans les recodifier.",
    "Seuils conservés : commune de moins de 10 000 habitants hors EPCI de 10 000 habitants ou plus, ou EPCI compétent regroupant moins de 10 000 habitants au total. La gratuité et la concertation restent prévues ; le second alinéa vise seulement l'instruction des demandes de permis, sans ajout des déclarations préalables. Note source intégralement prise en compte : l'article 134, III, de la loi n° 2014-366 du 24 mars 2014 fixe l'entrée en vigueur au 1er juillet 2015 ; si les seuils du premier alinéa sont dépassés en raison de la création, après le 1er juillet 2015, d'un nouvel EPCI de 10 000 habitants ou plus, la mise à disposition ne peut cesser avant un an à compter de cette création. Une convention entre l'État et la collectivité territoriale définit l'étendue et les modalités de la mise à disposition des services déconcentrés. Pour les collectivités tenues d'y mettre fin, une convention de transition peut définir les modalités d'accompagnement de l'État. Ces dispositions extérieures à l'article ne sont ni abrogées ni remplacées et doivent accompagner sa consolidation ; leurs dates historiques ne fixent aucune entrée en vigueur de la réforme future. Le dossier coordonné de L423-1 ne crée ici ni droit supplémentaire à une mise à disposition gratuite ni relèvement des seuils.",
)

add(
    "L423-2",
    """<p>Les pièces des dossiers de demande de permis et de déclaration préalable sont mises à la disposition de l'administration à des fins de contrôle et pour le traitement des taxes d'urbanisme. Elles le sont également pour le suivi des changements relatifs aux propriétés bâties dans le cadre de l'assiette de la fiscalité directe locale, pour la mise en œuvre et le suivi des politiques publiques fondées sur la construction neuve, ainsi qu'à des fins statistiques.</p>
<p>Le décret prévu à l'article L. 426-1 précise les modalités et les conditions dans lesquelles l'autorité mentionnée à l'article L. 422-1 transmet aux autorités administratives compétentes les informations contenues dans ces demandes et déclarations.</p>
<p>Pour l'instruction d'un dossier coordonné mentionné à l'article L. 423-1, les services compétents réutilisent les pièces en cours de validité déjà détenues et légalement accessibles, dans les conditions prévues au même article. Ils ne transmettent à chaque service que les informations nécessaires à ses missions, dans le respect des secrets protégés et de la protection des données personnelles. Le présent alinéa s'applique à la même date et selon les mêmes règles transitoires que les dispositions de l'article L. 423-1 relatives au dossier coordonné.</p>""",
    "Les deux alinéas existants sont réécrits à droit constant : les finalités de mise à disposition sont réparties entre deux phrases et le décret de transmission est identifié comme sujet. Réforme de fond au troisième alinéa : coordination avec le dossier partagé de L423-1 pour réutiliser les pièces déjà détenues et légalement accessibles et limiter les échanges aux informations nécessaires, avec la même transition.",
    "Toutes les finalités existantes, y compris le contrôle, les taxes d'urbanisme, l'assiette de la fiscalité directe locale, les politiques fondées sur la construction neuve et les statistiques, sont conservées. Les deux premiers alinéas conservent leur place ; l'ajout intervient à la fin. Le renvoi source à la seule autorité de L422-1 est maintenu : sa portée à l'égard des compétences spéciales de L422-2 et L422-3-1 doit être contrôlée dans le décret de L426-1, sans élargissement silencieux du renvoi. Coordonner ce décret avec les modalités du dossier prévues à L423-1, les habilitations d'accès et le droit de correction prévu par cet article. Le nouvel alinéa suit l'application aux demandes déposées à compter du sixième mois suivant la publication de la loi créant le dispositif ; les demandes antérieures conservent leur procédure, sauf demande expresse de coordination sans remise à zéro des délais déjà courus, conformément à la rédaction de L423-1 vérifiée dans le corpus. Aucun transfert de compétence ni suppression d'une autorisation. Les délais ordinaires de deux mois pour une maison et de trois mois pour les autres permis, ainsi que leurs exceptions, restent à préserver et à annoncer dans les textes d'instruction, sans nouveau délai créé ici.",
)

add(
    "L423-3",
    """<p>Les communes dont le nombre total d'habitants est supérieur à 3 500 doivent disposer d'une téléprocédure spécifique pour recevoir et instruire sous forme dématérialisée les demandes d'autorisation d'urbanisme déposées à compter du 1er janvier 2022. Elles peuvent mutualiser cette téléprocédure au travers du service chargé de l'instruction des actes d'urbanisme.</p>
<p>Le ministre chargé de l'urbanisme fixe, par arrêté, les modalités de mise en œuvre de cette téléprocédure.</p>
<p>Pour les communes mentionnées au premier alinéa, la téléprocédure permet le dépôt des éléments communs du dossier coordonné prévu à l'article L. 423-1 et la réutilisation des pièces en cours de validité déjà détenues et légalement accessibles, dans les conditions prévues au même article. Elle permet d'indiquer au demandeur les pièces réutilisées et, en cas d'impossibilité de réutilisation, son motif. Elle permet aussi de recueillir ses demandes de correction d'une donnée inexacte ou devenue obsolète. L'accès des services aux pièces est limité aux informations nécessaires à leurs missions et respecte les secrets protégés et la protection des données personnelles. Ces fonctionnalités sont mises en œuvre à la même date et selon les mêmes règles transitoires que les dispositions de l'article L. 423-1 relatives au dossier coordonné.</p>""",
    "Réécriture à droit constant des deux alinéas existants : l'obligation des communes et la faculté de mutualisation sont exprimées séparément, puis le ministre est identifié comme auteur de l'arrêté. Réforme de fond au troisième alinéa : adaptation de la téléprocédure au dossier coordonné de L423-1, à la réutilisation des pièces et à la réception des demandes de correction, avec accès limité des services.",
    "Seuil strictement supérieur à 3 500 habitants et date historique du 1er janvier 2022 conservés ; le nouvel alinéa ne rend pas cette téléprocédure obligatoire pour les communes de 3 500 habitants ou moins. Les deux alinéas existants conservent leur ordre et l'ajout est final. Adapter l'arrêté ministériel en cohérence avec le décret de L423-1, les transmissions de L423-2 et le décret de L426-1 ; prévoir les moyens techniques nécessaires sans les présenter comme financés. L'application des nouvelles fonctionnalités suit celle du dossier coordonné : demandes déposées à compter du sixième mois suivant la publication de la loi créant le dispositif, et demandes antérieures seulement sur demande expresse de coordination sans remise à zéro des délais déjà courus. Le 1er janvier 2022 n'est pas une date de la réforme future. Chaque autorité garde sa décision et ses délais ; les délais ordinaires de deux et trois mois et leurs exceptions ne sont pas modifiés ici. La rénovation locative limitée à vingt-quatre mois exige une disposition dans la loi n° 89-462 du 6 juillet 1989, notamment son article 6 et ses coordinations sur la décence ; le traitement des impayés appelle notamment son article 24 et les textes de procédure civile et d'exécution. Ces mesures hors du présent code ne sont pas réputées adoptées par la téléprocédure et aucun article nouveau fictif n'est cité.",
)


sources = json.loads(Path("source.json").read_text())
assert len(sources) == 24
assert set(drafts) == {s["number"] for s in sources}
answer = []
for source in sources:
    row = {key: source[key] for key in ("code_id", "source_id", "source_sha256", "number")}
    row.update(drafts[source["number"]])
    answer.append(row)
Path("answer.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")
