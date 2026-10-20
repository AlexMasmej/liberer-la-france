import json
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
drafts = {}

def add(number, paragraphs, reason, review):
    assert number not in drafts
    drafts[number] = {
        'proposed_xml': '\n'.join('<p>' + p + '</p>' for p in paragraphs),
        'reason': reason,
        'review_notes': review,
        'status': 'rewrite_draft',
    }

add('L322-3-1', [
    "Lorsque la localisation ou la configuration des parcelles limite de façon importante l'utilisation des droits à construire prévus par les documents d'urbanisme, l'autorité administrative peut autoriser une association foncière urbaine de remembrement à la demande ou avec l'accord d'au moins la moitié des propriétaires. Cette autorisation déroge aux règles de majorité fixées à l'article L. 322-3."
],
    "Réécriture à droit constant : la condition tenant aux parcelles est placée avant la faculté d'autorisation ; la dérogation de majorité est énoncée dans une phrase distincte, au sein du même alinéa. Aucune réforme de fond.",
    "La moitié au moins des propriétaires suffit, sur demande ou avec leur accord ; aucun seuil de superficie n'est ajouté. La limitation importante doit concerner les droits à construire prévus par les documents d'urbanisme. Le contrôle du renvoi à L. 322-3 confirme que la dérogation concerne les majorités : les autres conditions de cet article ne sont pas écartées."
)

add('L322-3-2', [
    "Avant la création de l'association, lorsque la commune concernée est couverte par un plan local d'urbanisme communal ou intercommunal, l'autorité administrative recueille l'accord de l'assemblée délibérante de l'autorité compétente en matière de plan local d'urbanisme. Dans les autres cas, ou lorsque l'association foncière urbaine est située à l'intérieur d'un périmètre d'opération d'intérêt national, l'autorité administrative recueille l'avis de cette assemblée délibérante."
],
    "Réécriture à droit constant : la chronologie de la consultation est explicitée et le second renvoi à l'assemblée est allégé. La distinction entre accord et avis demeure ; aucune réforme de fond.",
    "L'accord préalable reste requis en présence d'un PLU communal ou intercommunal, sous réserve du cas d'une opération d'intérêt national, soumis à un avis. Dans les autres cas, la source désigne la même assemblée délibérante par renvoi ; cette désignation est conservée sans inventer d'autorité de substitution."
)

add('L322-4', [
    "À défaut d'accord amiable entre les propriétaires intéressés ou de constitution d'une association foncière libre ou autorisée, l'autorité administrative peut constituer d'office une association foncière urbaine dans les cas suivants :",
    "1° Pour le remembrement de parcelles :",
    "Lorsque les règles d'urbanisme imposent une discipline spéciale à l'implantation et au volume des constructions et que la disposition actuelle des parcelles compromettrait ou empêcherait sa mise en œuvre ;",
    "Ou lorsqu'il est équitable de répartir entre un ensemble de propriétés la charge des prélèvements de terrains effectués par cession ou expropriation au profit des emprises publiques, ainsi que la charge des servitudes liées à la présence des ouvrages construits sur ces emprises ;",
    "Ou lorsqu'il convient de modifier les limites de lots dans un lotissement à la suite de l'application des articles L. 315-3 à L. 315-5 ;",
    "2° Pour l'entretien et la gestion d'ouvrages d'intérêt collectif dans les ensembles immobiliers aménagés à l'initiative privée ou publique, lorsque le défaut d'entretien ou de gestion de ces ouvrages peut nuire à l'intérêt public ; ainsi que pour la construction d'ouvrages d'intérêt collectif à l'exécution desquels l'autorité compétente aurait subordonné la modification d'un lotissement en application des articles L. 315-3 à L. 315-5 ;",
    "3° Pour la restauration prévue au 5° de l'article L. 322-2, lorsqu'elle porte sur des parties d'immeubles visibles de l'extérieur ;",
    "4° Afin que les propriétaires de parcelles bénéficiant directement de servitudes non aedificandi édictées pour réserver une vue participent à la réparation du dommage direct, matériel et certain que peuvent subir les propriétaires des parcelles grevées par ces servitudes. Dans ce cas, la commune est membre de droit de l'association ;",
    "5° Pour les remembrements ou groupements de parcelles prévus au 6° de l'article L. 322-2, lorsque la disposition actuelle des parcelles compromettrait ou empêcherait la mise en œuvre d'un programme de restructuration urbaine d'un grand ensemble ou d'un quartier d'habitat dégradé mentionné au premier alinéa du 3 de l'article 42 de la loi n° 95-115 du 4 février 1995 précitée."
],
    "Réécriture à droit constant : les cas de constitution d'office sont annoncés directement, les conditions du remembrement sont simplifiées et les bénéficiaires et débiteurs de la réparation liée aux vues sont identifiés. Les neuf alinéas et les 1° à 5° sont maintenus. Aucune réforme de fond ni extension de la constitution d'office.",
    "Les trois cas alternatifs du 1°, les deux objets du 2°, la visibilité extérieure du 3°, les trois caractères cumulatifs du dommage au 4° et l'appartenance de droit de la commune sont conservés. Anomalie de renvoi à contrôler : les articles L. 315-3 à L. 315-5, cités deux fois, ne figurent pas dans le corpus public fourni ; leurs références sont maintenues sans substitution par des dispositions contemporaines. Le renvoi au premier alinéa du 3 de l'article 42 de la loi de 1995 est repris sans modification ; cette loi est hors du corpus fourni."
)

add('L322-4-1', [
    "Le président de l'association foncière urbaine exerce les compétences que lui attribue l'article 23 de l'ordonnance du 1er juillet 2004 précitée. Pour l'assister, il peut recourir à une personne physique ou morale intervenant comme prestataire de services. Le contrat précise les missions de ce prestataire et son mode de rémunération. Il est conclu dans les conditions fixées par le décret pris pour l'application de l'article 26 de l'ordonnance du 1er juillet 2004 précitée."
],
    "Réécriture à droit constant : le recours au prestataire est rattaché explicitement à l'assistance du président, puis les exigences du contrat sont énoncées séparément. Aucune réforme de fond des compétences ou de la contractualisation.",
    "Le prestataire peut rester une personne physique ou morale ; ses missions et son mode de rémunération doivent figurer au contrat. Les articles 23 et 26 de l'ordonnance du 1er juillet 2004 sont conservés ; son identification comme ordonnance n° 2004-632 est confirmée par L. 322-1 du corpus. Aucun transfert des compétences du président n'est ajouté."
)

add('L322-5', [
    "Les propriétaires qui n'ont pas adhéré à une association foncière urbaine autorisée peuvent délaisser, moyennant indemnité, leurs immeubles compris dans son périmètre. Ils disposent pour cela de trois mois à compter de la publication de la décision administrative autorisant l'association. À défaut d'accord amiable, l'indemnité est fixée comme en matière d'expropriation.",
    "Lorsque l'association a pour objet le groupement de parcelles, tous les propriétaires d'immeubles compris dans le périmètre syndical peuvent, en outre, délaisser moyennant indemnité leurs propriétés ou leurs quote-parts de propriété sur les parcelles groupées. Ils disposent pour cela de trois mois à compter de la publication de l'arrêté de l'autorité administrative visé à l'article L. 322-7 (troisième alinéa). À défaut d'accord amiable, l'indemnité est fixée comme en matière d'expropriation.",
    "Les droits des créanciers régulièrement inscrits sur l'immeuble délaissé avant la publication de l'acte de délaissement au fichier immobilier sont reportés sur l'indemnité de délaissement, dans le respect du rang de préférence reconnu à ces créanciers.",
    "Lorsque l'indemnité convenue à l'amiable est inférieure au total des créances ayant fait l'objet d'une inscription pour leur recouvrement, les créanciers inscrits peuvent exiger que l'indemnité acceptée par leur débiteur soit soumise au juge.",
    "Les envoyés en possession provisoire peuvent valablement délaisser les biens des absents après avoir obtenu l'autorisation du tribunal judiciaire. Celui-ci statue sur simple requête, après avoir entendu le ministère public."
],
    "Réécriture à droit constant : les bénéficiaires de chacun des deux droits de délaissement sont explicités ; les délais et leurs points de départ sont isolés dans des phrases courtes. Les droits des créanciers et l'autorisation judiciaire concernant les absents sont reformulés sans changement de fond, dans les cinq alinéas d'origine.",
    "Les deux délais de trois mois ont des points de départ distincts et restent dans leurs alinéas respectifs. Décalage préexistant : L. 322-5 vise le troisième alinéa de L. 322-7 pour l'arrêté, alors que, dans les cinq paragraphes substantiels de la source fournie, le troisième est le b) et l'arrêté figure au quatrième. Le renvoi est conservé ; une coordination explicite de L. 322-5 avec L. 322-7 serait nécessaire pour le rectifier. Le rang des créanciers, la condition d'inscription antérieure à la publicité du délaissement et le recours au juge sont maintenus. La note source rattache l'entrée en vigueur au 1er janvier 2022 au I de l'article 37 de l'ordonnance n° 2021-1192 du 15 septembre 2021 : il s'agit d'une date historique, sans effet de calendrier pour le projet. Le régime ancien des envoyés en possession provisoire est conservé."
)

add('L322-6', [
    "Lorsque l'objet d'une association foncière urbaine autorisée ou constituée d'office porte sur les travaux prévus au 1° et au 6° de l'article L. 322-2, l'association exerce les missions suivantes :",
    "a) Elle détermine les bâtiments ou les ouvrages dont le remembrement nécessite la destruction ou le changement d'usage, éventuellement après réparation, aménagement ou transformation.",
    "L'acte amiable de cession d'un bâtiment ou d'un ouvrage à l'association produit, pour l'extinction des droits réels et personnels, les mêmes effets qu'un acte de cession amiable en matière d'expropriation. À défaut d'accord amiable des propriétaires sur la cession, ces bâtiments ou ouvrages sont expropriés dans les conditions fixées par le code de l'expropriation pour cause d'utilité publique ;",
    "b) Elle établit le projet de remembrement et le transmet à l'autorité administrative. Après avoir vérifié sa compatibilité avec la réglementation de l'urbanisme, cette autorité le soumet à une enquête publique réalisée conformément au code de l'expropriation pour cause d'utilité publique.",
    "Après l'enquête publique, l'autorité administrative prononce les transferts et attributions de propriété. Son acte impose, si nécessaire, des prescriptions propres à l'opération qui complètent la réglementation d'urbanisme applicable à la zone concernée. Ces prescriptions figurent dans le dossier soumis à l'enquête.",
    "L'arrêté de l'autorité administrative éteint par lui-même, à sa date et pour les immeubles qu'il concerne, les servitudes et les droits réels conférés aux preneurs par les baux à construction et les baux emphytéotiques. Cette extinction donne lieu à une indemnité due par l'association foncière urbaine et fixée, à défaut d'accord amiable, comme en matière d'expropriation. L'arrêté produit les mêmes effets à l'égard des autres droits réels. Toutefois, ces droits peuvent être reportés sur les immeubles ou les droits indivis de propriété après remembrement. Ils conservent alors leur rang antérieur, à condition que leur publicité soit renouvelée dans les formes et délais fixés par décret ; ils s'exercent, le cas échéant, sur les soultes.",
    "L'arrêté de l'autorité administrative met fin, dans les mêmes conditions, aux contrats de louage portant sur ces immeubles. Si le bail éteint relevait du chapitre V du titre IV du livre Ier du code de commerce, l'association foncière urbaine doit au preneur une indemnité calculée selon les règles de ces dispositions, à moins qu'elle ne préfère lui offrir le bail d'un local équivalent à celui dont il a perdu la jouissance. Pour les locaux d'habitation ou professionnels, le droit au relogement s'exerce comme en matière d'expropriation, quelle que soit la nature du titre d'occupation.",
    "La juridiction prévue à l'article L. 311-5 du code de l'expropriation pour cause d'utilité publique statue sur les contestations relatives à l'évaluation des parcelles remembrées. Elle statue également sur les contestations soulevées à l'occasion du remembrement qui concernent les privilèges, les hypothèques et les autres droits réels.",
    "L'organe compétent de l'association foncière urbaine prend une décision motivée, qui est notifiée aux intéressés. Ceux-ci disposent d'un délai de deux mois pour saisir la juridiction.",
    "Les intéressés qui ne saisissent pas la juridiction dans ce délai sont réputés avoir accepté l'évaluation des parcelles remembrées et avoir renoncé à toute contestation relative aux privilèges, aux hypothèques et aux autres droits réels.",
    "À peine de nullité, la notification doit indiquer ce délai et reproduire en caractères apparents les dispositions de l'alinéa précédent.",
    "Les dispositions du deuxième alinéa a) de l'article L. 322-7 s'appliquent, le cas échéant, aux associations foncières urbaines dont l'objet porte sur les travaux prévus au 6° de l'article L. 322-2."
],
    "Réécriture à droit constant : les missions a) et b) désignent explicitement l'association ; les effets de l'arrêté, les indemnisations, les reports de droits et le contentieux sont formulés en phrases plus courtes. Les douze alinéas restent à leur place, sans réforme de fond.",
    "Contrôle particulier des alinéas 5 à 8, repris par L. 322-7 : ils conservent leurs positions et leur contenu. Le report des autres droits réels demeure conditionné au renouvellement de leur publicité, avec maintien du rang et exercice éventuel sur les soultes. Les baux commerciaux, l'alternative d'un local équivalent et le relogement de tout titulaire d'un titre d'occupation des locaux visés sont maintenus. Le délai de deux mois, la renonciation présumée et la nullité de la notification irrégulière restent aux alinéas 9 à 11. Le dernier alinéa conserve la formulation atypique « deuxième alinéa a) » de L. 322-7 ; dans la source de cet article, le a) forme bien le deuxième paragraphe substantiel. Le renvoi L. 311-5 et ceux au code de commerce ne sont pas remplacés, ces textes n'étant pas compris dans le corpus fourni."
)

add('L322-6-1', [
    "Avant l'approbation du plan de remembrement, lorsque la commune concernée est couverte par un plan local d'urbanisme communal ou intercommunal, l'autorité administrative recueille l'accord de l'assemblée délibérante de l'autorité compétente en matière de plan local d'urbanisme. L'accord porte à la fois sur le plan de remembrement et sur les prescriptions d'urbanisme propres à l'opération. Dans les autres cas, ou lorsque l'association est située à l'intérieur d'un périmètre d'opération d'intérêt national, l'autorité administrative recueille l'avis de cette assemblée délibérante."
],
    "Réécriture à droit constant : le moment de la consultation et ses deux objets sont énoncés directement. L'accord et l'avis restent distingués dans un seul alinéa ; aucune réforme de fond.",
    "L'accord demeure préalable à l'approbation et couvre tant le plan que les prescriptions de l'opération. L'avis s'applique dans les autres cas et en périmètre d'opération d'intérêt national. La procédure complète celle de L. 322-6 sans dispenser de l'enquête publique ni des vérifications de compatibilité."
)

add('L322-7', [
    "Lorsque l'objet d'une association foncière urbaine autorisée porte sur les travaux prévus au 2° de l'article L. 322-2, l'association exerce les missions suivantes :",
    "a) Elle détermine les bâtiments ou les ouvrages dont le groupement de parcelles nécessite la destruction ou le changement d'usage, éventuellement après réparation, aménagement ou transformation. L'acte amiable de cession d'un bâtiment ou d'un ouvrage à l'association foncière urbaine produit, pour l'extinction des droits réels et personnels, les mêmes effets qu'un acte de cession amiable en matière d'expropriation. À défaut d'accord amiable des propriétaires sur la cession, ces bâtiments ou ouvrages sont expropriés dans les conditions fixées par le code de l'expropriation pour cause d'utilité publique ;",
    "b) Elle établit, selon le cas, le projet de contrat de bail à construction, le projet d'acte d'apport ou le projet d'acte de vente des parcelles groupées.",
    "Le contrat de bail, l'acte d'apport ou l'acte de vente ne peut être conclu qu'après que l'autorité administrative a constaté par arrêté la compatibilité du projet avec la réglementation de l'urbanisme et l'accomplissement régulier des formalités prévues par le présent code.",
    "Les alinéas 5, 6, 7 et 8 de l'article L. 322-6 s'appliquent au groupement de parcelles."
],
    "Réécriture à droit constant : les missions de l'association sont explicites ; les effets de la cession et les deux vérifications préalables à la conclusion de l'acte sont séparés en phrases lisibles. Les cinq alinéas substantiels et les lettres a) et b) sont conservés. Aucune réforme de fond.",
    "Le champ reste celui de l'association autorisée et du 2° de L. 322-2. Le a) reste au deuxième alinéa, visé par L. 322-6 ; les renvois aux alinéas 5, 6, 7 et 8 de L. 322-6 sont inchangés et leurs cibles restent en place. Décalage préexistant signalé aussi à L. 322-5 : ce dernier désigne le troisième alinéa de L. 322-7 pour l'arrêté, qui figure pourtant au quatrième paragraphe substantiel. Aucun alinéa n'est déplacé pour corriger ce renvoi. L'application par renvoi des seuls alinéas 5 à 8, sans les alinéas 9 à 11 de L. 322-6, est maintenue et appelle un contrôle de l'articulation contentieuse."
)

add('L322-8', [
    "Lorsque l'objet d'une association foncière urbaine autorisée ou constituée d'office porte sur les travaux prévus au 5° de l'article L. 322-2, l'association décide, s'il y a lieu, des destructions de constructions nécessaires à l'intérieur de son périmètre. À défaut d'accord amiable, les indemnités dues aux propriétaires, locataires ou occupants de ces constructions sont fixées comme en matière d'expropriation."
],
    "Réécriture à droit constant : la décision de destruction et la fixation des indemnités sont réparties entre deux phrases au sein du même alinéa. Les bénéficiaires de l'indemnisation et son régime sont conservés, sans réforme de fond.",
    "Le champ reste limité aux travaux du 5° de L. 322-2 et aux associations autorisées ou constituées d'office. La destruction demeure éventuelle, nécessaire et située à l'intérieur du périmètre. Les propriétaires, locataires et occupants conservent l'indemnisation mentionnée par la source."
)

add('L322-9', [
    "Toutes les créances, de quelque nature qu'elles soient, qu'une association foncière urbaine peut exiger d'un associé sont garanties par une hypothèque légale sur les immeubles de cet associé compris dans le périmètre de l'association, qu'il s'agisse de provisions ou de paiements définitifs. L'inscription et la mainlevée de cette hypothèque sont soumises aux conditions prévues à l'article 19 de la loi n° 65-557 du 10 juillet 1965 fixant le statut de la copropriété des immeubles bâtis.",
    "Lors de la mutation à titre onéreux d'un bien compris dans une association foncière urbaine, un avis de mutation doit être adressé à l'association dans les conditions prévues à l'article 20 de la loi n° 65-557 du 10 juillet 1965 précitée. L'association peut faire opposition dans les conditions prévues à ce même article afin d'obtenir le paiement des sommes restant dues par l'ancien propriétaire."
],
    "Réécriture à droit constant : la garantie est rattachée directement aux créances exigibles et l'avis de mutation est distingué de la faculté d'opposition. Les deux alinéas sont maintenus sans modification de fond.",
    "L'hypothèque reste limitée aux immeubles de l'associé compris dans le périmètre et garantit toutes les natures de créances exigibles, provisions comprises. Le second alinéa conserve la mutation à titre onéreux, l'avis à l'association et l'opposition pour les dettes de l'ancien propriétaire. Les articles 19 et 20 de la loi de 1965 sont repris ; leur version n'est pas vérifiable dans le corpus fourni."
)

add('L322-9-1', [
    "Lorsqu'un ou plusieurs immeubles compris dans le périmètre d'une association foncière urbaine relèvent de la loi n° 65-557 du 10 juillet 1965 fixant le statut de la copropriété des immeubles bâtis, les travaux qui constituent l'objet de l'association sont réputés rendus obligatoires au sens du e de l'article 25 de cette loi.",
    "Dans chaque copropriété, les copropriétaires peuvent désigner un ou plusieurs d'entre eux, un mandataire ad hoc ou le syndic de la copropriété dûment mandaté pour les représenter à l'assemblée des propriétaires de l'association. Un même syndic ne peut recevoir de mandat des copropriétaires de plus d'une copropriété."
],
    "Réécriture à droit constant : le champ des travaux réputés obligatoires est formulé plus directement et les représentants possibles sont désignés dans une construction unique. Les deux alinéas et l'interdiction des mandats multiples du syndic sont maintenus, sans réforme de fond.",
    "Les travaux restent réputés rendus obligatoires au sens du e de l'article 25, sans modification du régime de vote. Le choix entre copropriétaires, mandataire ad hoc et syndic demeure ouvert ; la limite d'une seule copropriété concerne le même syndic. La concordance du e de l'article 25 de la loi de 1965 doit être contrôlée hors du corpus fourni, qui ne contient pas cette loi."
)

add('L322-9-2', [
    "Les taxes des associations autorisées sont recouvrées selon les règles applicables aux contributions directes.",
    "Toutefois, l'association peut décider d'autoriser le règlement de tout ou partie de ces taxes par remise d'immeuble. Les personnes publiques peuvent également acquitter leur contribution sous cette forme, si elles y consentent.",
    "Si l'immeuble n'est pas remis dans les délais prévus, le montant des taxes dues par le propriétaire devient immédiatement exigible."
],
    "Réécriture à droit constant : le mode ordinaire de recouvrement, la faculté de remise d'immeuble et la conséquence d'une remise tardive sont exprimés directement dans leurs trois alinéas d'origine. Aucune réforme de fond.",
    "Le régime ordinaire reste celui des contributions directes. La remise d'immeuble suppose une décision de l'association et peut couvrir tout ou partie du règlement ; les personnes publiques doivent y consentir pour leur contribution. Aucun délai supplémentaire n'est ajouté avant l'exigibilité immédiate des taxes si la remise n'a pas lieu dans les délais prévus."
)

add('L322-9-3', [
    "L'association peut régler ses dépenses par remise d'immeuble si le créancier l'accepte. Le contrat à l'origine de la dépense précise les modalités de ce règlement."
],
    "Réécriture à droit constant : l'association est le sujet explicite de la faculté de paiement et l'exigence contractuelle est formulée directement. L'acceptation du créancier demeure nécessaire ; aucune réforme de fond.",
    "La remise d'immeuble pour payer une dépense demeure distincte de celle prévue pour les contributions à L. 322-9-2. L'accord du créancier et l'inscription des modalités dans le contrat créateur de la dépense sont tous deux conservés."
)

add('L322-10', [
    "Des décrets en Conseil d'État fixent, si nécessaire, les modalités d'application de la présente section. Ils précisent notamment les conditions dans lesquelles les associations foncières urbaines peuvent bénéficier de l'assistance technique de l'État, des collectivités territoriales, des établissements publics ou de personnes privées, physiques ou morales ; les garanties auxquelles les opérations prévues au 2° de l'article L. 322-2 peuvent être subordonnées ; et les formalités de publicité, notamment au fichier immobilier, auxquelles sont soumis les actes concernant ces associations et les immeubles compris dans leur périmètre."
],
    "Réécriture à droit constant : la compétence réglementaire est séparée de ses objets, puis les trois catégories de modalités sont distinguées par des points-virgules dans le même alinéa. Aucune réforme de fond.",
    "Le caractère éventuel des décrets d'application et des garanties est conservé, ainsi que tous les prestataires possibles d'assistance technique. Les garanties restent rattachées au 2° de L. 322-2 et la publicité immobilière demeure expressément mentionnée. La source vise la « présente section », tandis que le chemin fourni situe cet article directement dans le chapitre II : cette discordance de subdivision est signalée sans remplacer le renvoi."
)

add('L322-11', [
    "Les associations syndicales créées en application de l'ordonnance n° 58-1445 du 31 décembre 1958 restent régies par cette ordonnance jusqu'à l'achèvement des travaux pour lesquels elles ont été constituées. Elles peuvent toutefois décider de se soumettre aux articles L. 322-1 à L. 322-10.",
    "Cette décision est prise dans les conditions prévues à l'article 14 de l'ordonnance du 1er juillet 2004 précitée. Elle n'entre en vigueur qu'après la modification des statuts."
],
    "Réécriture à droit constant : le maintien du régime ancien et la faculté d'opter pour le régime du code sont distingués ; la condition d'entrée en vigueur de l'option est formulée directement dans le second alinéa. Aucune réforme de fond.",
    "Le régime historique de l'ordonnance n° 58-1445 du 31 décembre 1958 est maintenu jusqu'à l'achèvement des travaux initiaux, sauf option. Les bornes L. 322-1 à L. 322-10 restent inchangées. L'article 14 de l'ordonnance du 1er juillet 2004 continue à régir la décision et la modification des statuts demeure une condition de son entrée en vigueur. Aucune date nouvelle n'est attribuée à cette transition ancienne."
)

add('L322-12', [
    "L'association foncière urbaine de projet est une association foncière urbaine autorisée. Elle a pour objet de permettre la cession des terrains compris dans son périmètre, après avoir réalisé un projet combinant une opération de remembrement au sens des 1° et 2° de l'article L. 322-2 et une opération d'aménagement au sens de l'article L. 300-1.",
    "Les dispositions du présent chapitre régissent l'association foncière urbaine de projet, sous réserve des articles L. 322-13 à L. 322-16."
],
    "Réécriture à droit constant : la nature de l'association est séparée de son objet et l'articulation avec le régime général est exprimée directement. Les deux alinéas demeurent, sans réforme de fond.",
    "La cession reste postérieure à la réalisation d'un projet associant remembrement et aménagement. Imprécision préexistante conservée : la source vise une opération de « remembrement » au sens des 1° et 2° de L. 322-2, alors que le 2° de cet article porte sur le groupement de parcelles ; le champ n'est ni réduit au seul 1° ni reformulé par une correction de fond implicite. Les renvois L. 300-1 et L. 322-13 à L. 322-16 sont maintenus."
)

add('L322-13', [
    "La commune ou l'établissement public de coopération intercommunale compétent en matière de plan local d'urbanisme, ou le représentant de l'État dans le cadre d'une opération d'intérêt national, peuvent délimiter des périmètres de projet. Dans ces périmètres, les propriétaires fonciers sont incités à se regrouper en association foncière urbaine de projet et les associations foncières urbaines de projet à conduire leurs opérations de manière concertée."
],
    "Réécriture à droit constant : la faculté de délimiter les périmètres est séparée de leurs deux finalités d'incitation et de concertation dans le même alinéa. Aucune réforme de fond.",
    "La délimitation demeure facultative et les propriétaires ne sont pas obligés d'adhérer. La compétence de la commune ou de l'EPCI en matière de PLU et l'intervention du représentant de l'État dans le cadre d'une opération d'intérêt national sont conservées. Aucun effet d'autorisation d'urbanisme n'est attaché à la seule délimitation."
)

add('L322-14', [
    "Les propriétaires qui souhaitent créer une association foncière urbaine de projet adressent leur demande d'autorisation à l'autorité administrative.",
    "Le dossier de demande de création comprend notamment le projet de statuts et le périmètre envisagé pour les opérations. Ce périmètre peut inclure tout ou partie des unités foncières concernées par le projet de l'association. Les statuts respectent le second alinéa de l'article 7 de l'ordonnance n° 2004-632 du 1er juillet 2004 relative aux associations syndicales de propriétaires.",
    "Une copie du dossier est transmise à la commune ou à l'établissement public de coopération intercommunale compétent en matière de plan local d'urbanisme sur le territoire duquel le projet de l'association est prévu."
],
    "Réécriture à droit constant : les demandeurs sont désignés directement et le contenu du dossier est distingué de l'étendue possible du périmètre en phrases plus courtes. Les trois alinéas sont conservés, sans réforme de fond.",
    "L'énumération du dossier reste non exhaustive grâce à « notamment ». Le périmètre peut couvrir tout ou partie des unités foncières et la conformité au second alinéa de l'article 7 de l'ordonnance est conservée. La transmission d'une copie à l'autorité locale compétente demeure. La coordination du dossier d'autorisation d'urbanisme prévue à L. 423-1 par les orientations ne modifie pas automatiquement cette procédure distincte de création d'association."
)

add('L322-15', [
    "L'autorité administrative soumet le projet de création de l'association à une enquête publique conformément à l'article 12 de l'ordonnance n° 2004-632 du 1er juillet 2004 précitée. Le dossier d'enquête comprend, le cas échéant, les prescriptions mentionnées à l'article L. 322-6.",
    "Après l'enquête publique, l'autorité administrative peut autoriser la création de l'association foncière urbaine après avoir recueilli l'accord du conseil municipal ou de l'organe délibérant de l'établissement public de coopération intercommunale compétent en matière de plan local d'urbanisme.",
    "Lorsque le projet s'inscrit dans une opération d'intérêt national, l'autorité administrative peut autoriser la création de l'association foncière urbaine de projet sur avis du conseil municipal ou de l'organe délibérant de l'établissement public de coopération intercommunale compétent en matière de plan local d'urbanisme.",
    "L'acte autorisant la création de l'association foncière urbaine de projet est publié et affiché dans chaque commune dont le territoire est compris, même en partie, dans le périmètre de l'association. Il est également notifié aux propriétaires. Ces formalités sont accomplies dans les conditions prévues par décret en Conseil d'État."
],
    "Réécriture à droit constant : la décision suivant l'enquête est formulée directement et les trois formalités de publicité et de notification sont réparties en phrases distinctes au sein du quatrième alinéa. La différence entre accord et avis est conservée, sans réforme de fond.",
    "Les quatre alinéas sont maintenus. L'enquête renvoie toujours à l'article 12 de l'ordonnance et peut inclure les prescriptions de L. 322-6. Le cas d'une opération d'intérêt national demeure soumis à un avis, et non à l'accord requis dans le cas général. Publication, affichage dans toutes les communes touchées et notification aux propriétaires sont cumulés. La mention générale « association foncière urbaine » au deuxième alinéa, présente dans la source au sein du régime des associations de projet, est conservée."
)

add('L322-16', [
    "La modification des conditions initiales de l'association foncière urbaine de projet est régie par la section 1 du chapitre IV du titre III de l'ordonnance n° 2004-632 du 1er juillet 2004 précitée.",
    "Par dérogation à ces dispositions, les statuts peuvent prévoir une procédure de distraction lorsqu'un membre souhaite vendre tout ou partie de ses terrains aménagés à un acquéreur qui ne veut pas être inclus dans le périmètre de l'association, et que ce membre souhaite distraire ces terrains de ce périmètre. L'assemblée générale peut alors approuver la distraction des terrains à vendre sans enquête publique préalable et fixer les conditions financières dans lesquelles le vendeur reste redevable des emprunts et des participations prévues. Elle statue soit à la majorité des propriétaires représentant au moins les deux tiers de la superficie des terrains de l'association, soit à une majorité d'au moins les deux tiers des propriétaires représentant plus de la moitié de cette superficie.",
    "En dessous d'un seuil de surface fixé par décret en Conseil d'État, la décision de distraction de ces terrains peut être prise à la majorité des membres de l'association.",
    "Lorsque la distraction est approuvée, l'autorité administrative qui a autorisé la création de l'association foncière urbaine de projet modifie son périmètre en conséquence."
],
    "Réécriture à droit constant : la procédure dérogatoire de distraction est décomposée en conditions, objet de la décision et majorités, au sein du même deuxième alinéa. Le régime général, la règle des petites surfaces et la modification administrative du périmètre gardent chacun leur alinéa. Aucune réforme de fond.",
    "La dérogation doit être prévue par les statuts ; elle concerne des terrains aménagés destinés à un acquéreur refusant d'entrer dans le périmètre. Les deux majorités restent alternatives : majorité des propriétaires avec au moins deux tiers de la surface, ou au moins deux tiers des propriétaires avec strictement plus de la moitié de la surface. Le seuil de petite surface demeure renvoyé au décret et la majorité y est celle des membres. Le vendeur reste redevable des emprunts et participations selon les conditions financières fixées. La dispense d'enquête publique est limitée à la distraction, sans dispense d'autorisation d'urbanisme ou de protection environnementale."
)

add('L324-1', [
    "La création des établissements publics fonciers locaux répond à des enjeux d'intérêt général en matière d'aménagement et de développement durables.",
    "Ces établissements élaborent des stratégies foncières pour mobiliser du foncier, favoriser le développement durable, lutter contre l'étalement urbain et limiter l'artificialisation des sols, y compris par des actions ou des opérations de renaturation. Ces stratégies contribuent à la réalisation de logements, notamment sociaux, en tenant compte des priorités définies par les programmes locaux de l'habitat.",
    "Dans le cadre de leurs compétences, ils peuvent contribuer au développement, au maintien ou à la transformation des activités économiques, notamment pour faciliter les projets d'implantations industrielles ; aux politiques de protection contre les risques technologiques et naturels et d'adaptation des territoires au recul du trait de côte ; ainsi que, à titre subsidiaire, à la préservation des espaces naturels et agricoles, en coopération avec la société d'aménagement foncier et d'établissement rural et les autres organismes chargés de préserver ces espaces, au moyen de conventions.",
    "Les établissements publics fonciers créés en application du présent chapitre sont des établissements publics locaux à caractère industriel et commercial. Ils sont compétents pour réaliser toute acquisition foncière ou immobilière, pour leur compte, pour celui de leurs membres ou pour celui de toute personne publique, afin de constituer des réserves foncières en application des articles L. 221-1 et L. 221-2 ou de réaliser des actions ou opérations d'aménagement au sens de l'article L. 300-1. Ils peuvent aussi réaliser ou faire réaliser toutes les actions propres à faciliter l'utilisation et l'aménagement ultérieur, au sens du même article L. 300-1, des biens fonciers ou immobiliers acquis. Dans les périmètres délimités en application de l'article L. 113-16, ils peuvent procéder, en coopération avec la société d'aménagement foncier et d'établissement rural et après information des communes et des établissements publics de coopération intercommunale concernés, aux acquisitions foncières nécessaires à la protection d'espaces agricoles et naturels périurbains, le cas échéant en exerçant, à la demande et au nom du département, le droit de préemption prévu à l'article L. 215-1 ou, en dehors des zones de préemption des espaces naturels sensibles, le droit de préemption prévu au 9° de l'article L. 143-2 du code rural et de la pêche maritime, ainsi qu'à toute acquisition ou cession de baux commerciaux, de fonds de commerce ou de fonds artisanaux.",
    "Ces établissements interviennent sur le territoire des communes ou des établissements publics de coopération intercommunale qui en sont membres. À titre exceptionnel, ils peuvent intervenir à l'extérieur de ce territoire pour des acquisitions nécessaires à des actions ou opérations menées à l'intérieur de celui-ci.",
    "Le droit de préemption exercé en application du deuxième alinéa de l'article L. 210-1 s'inscrit dans le cadre de conventions conclues avec le représentant de l'État dans le département.",
    "Les acquisitions et cessions foncières et immobilières que ces établissements réalisent pour leur propre compte ou pour celui d'une collectivité territoriale, d'un établissement public de coopération intercommunale ou d'un syndicat mixte sont soumises aux dispositions relatives à la transparence des opérations immobilières de ces collectivités ou établissements.",
    "Par délégation de leurs titulaires, ces établissements peuvent exercer les droits de préemption et de priorité définis par le présent code, dans les cas et conditions qu'il prévoit. Ils peuvent également agir par voie d'expropriation et dans le cadre des emplacements réservés prévus à l'article L. 151-41. À la demande de leurs collectivités, ils gèrent les procédures de délaissement prévues aux articles L. 230-1 à L. 230-6.",
    "Les établissements publics fonciers locaux peuvent apporter leur appui aux collectivités territoriales et à leurs groupements en matière d'observation foncière, notamment dans le cadre des observatoires de l'habitat et du foncier prévus au III de l'article L. 302-1 du code de la construction et de l'habitation.",
    "Sauf convention prévue au sixième alinéa du présent article, la réalisation de toute opération de l'établissement public exige l'avis favorable de la commune sur le territoire de laquelle elle est prévue. Cet avis est réputé donné dans un délai de deux mois à compter de la saisine de la commune."
],
    "Réécriture à droit constant : les objectifs fonciers sont formulés avec des verbes directs, les domaines de contribution sont distingués et les compétences, le territoire d'intervention et les procédures sont exposés en phrases plus courtes. Les dix alinéas, dont le sixième visé par l'exception finale, sont conservés. Aucune réforme de fond ni dérogation nouvelle aux obligations de logement social ou aux protections environnementales.",
    "Conserver les objectifs de renaturation et de logement social, les priorités des PLH, le caractère subsidiaire de la préservation des espaces naturels et agricoles, la coopération avec la SAFER et les conventions. L'intervention hors du territoire des membres demeure exceptionnelle et liée aux opérations intérieures. Le renvoi au deuxième alinéa de L. 210-1 a été vérifié dans le corpus ; la convention de préemption reste au sixième alinéa et l'exception finale la vise toujours. Le délai de deux mois et la formule de la source selon laquelle l'avis est réputé donné dans ce délai sont conservés. Ambiguïté préexistante du quatrième alinéa : l'ajout final relatif aux baux commerciaux et fonds est rattaché dans la même phrase aux acquisitions périurbaines ; le champ territorial et procédural de cet ajout appelle une clarification expresse. Sa place et les conditions de la phrase sont maintenues sans isoler une compétence générale nouvelle. Tous les renvois sont conservés, notamment le 9° de L. 143-2 du code rural et de la pêche maritime, hors corpus fourni."
)

add('L324-2', [
    "Le représentant de l'État dans la région crée l'établissement public foncier au vu des délibérations concordantes des organes délibérants d'établissements publics de coopération intercommunale à fiscalité propre et, le cas échéant, de conseils municipaux. Il dispose d'un délai de trois mois à compter de la transmission de ces délibérations. Lorsque les établissements publics de coopération intercommunale et les communes appartiennent à plusieurs régions, les représentants de l'État concernés prennent conjointement l'arrêté. Chacune de ces régions et chacun de leurs départements peuvent participer à la création de l'établissement public ou y adhérer.",
    "Les délibérations fixent la liste des membres de l'établissement public foncier, ses modalités de fonctionnement, sa durée et son siège, ainsi que la composition de son assemblée générale ou, dans le cas prévu au deuxième alinéa de l'article L. 324-3, de son conseil d'administration. Elles tiennent compte de l'importance de la population des communes et des établissements publics de coopération intercommunale membres.",
    "La décision de création reprend les éléments mentionnés à l'alinéa précédent."
],
    "Réécriture à droit constant : l'autorité créatrice est le sujet de la première phrase, le délai est isolé et le contenu des délibérations est rattaché explicitement à l'établissement. Les trois alinéas et les règles de participation sont conservés, sans réforme de fond.",
    "Le délai de trois mois part de la transmission des délibérations concordantes ; aucun effet tacite n'est ajouté. L'arrêté reste conjoint en cas de pluralité de régions ; régions et départements peuvent participer ou adhérer. Le deuxième alinéa de L. 324-3, consulté dans le corpus, permet au conseil d'administration d'exercer les attributions de l'assemblée générale lorsque tous les membres y sont représentés. La prise en compte des populations et la reprise des éléments dans la décision de création sont maintenues."
)

add('L324-2-1 A', [
    "Le représentant de l'État dans la région arrête l'extension du périmètre d'un établissement public foncier local à un établissement public de coopération intercommunale à fiscalité propre au vu des délibérations de l'organe délibérant de cet établissement de coopération intercommunale et de l'établissement public foncier local.",
    "Le périmètre d'un établissement public foncier local peut aussi être étendu à une commune membre d'un établissement public de coopération intercommunale à fiscalité propre qui n'adhère pas à l'établissement public foncier local. Le représentant de l'État dans la région arrête cette extension au vu des délibérations du conseil municipal et de l'établissement public foncier local, après avis de l'établissement public de coopération intercommunale. Cet avis est transmis, à la demande du représentant de l'État, dans un délai de deux mois. Si l'avis est défavorable en raison d'un projet d'adhésion de cet établissement public de coopération intercommunale à l'établissement public foncier local, l'extension à la commune ne peut être arrêtée qu'à l'expiration d'un délai de six mois à compter de la transmission de cet avis.",
    "Lorsque le périmètre de l'établissement public foncier local est étendu à un établissement public de coopération intercommunale à fiscalité propre dont une commune membre adhère déjà à l'établissement public foncier local, cet établissement de coopération intercommunale se substitue de plein droit à cette commune dans les organes de l'établissement public foncier local, ainsi que dans les délibérations et les actes pris par ce dernier."
],
    "Réécriture à droit constant : l'auteur de l'extension est explicite ; l'adhésion communale, la transmission de l'avis et le délai d'attente sont exposés en phrases distinctes. Les trois alinéas et la substitution de plein droit sont conservés, sans réforme de fond.",
    "Les délibérations des deux parties restent requises dans chaque cas. Le délai de transmission de l'avis reste de deux mois ; aucun point de départ non énoncé par la source ni avis tacite n'est ajouté. L'attente de six mois court à compter de la transmission du seul avis défavorable motivé par un projet d'adhésion de l'EPCI. La substitution demeure de plein droit, dans les organes et dans les délibérations et actes de l'établissement public foncier local. Le numéro, y compris l'espace et la lettre A, est conservé exactement."
)

add('L324-2-1 B', [
    "Lorsque les établissements publics de coopération intercommunale membres d'un établissement public foncier local fusionnent en un seul établissement public de coopération intercommunale, l'établissement public foncier local est maintenu si l'établissement issu de la fusion est à fiscalité propre.",
    "Lorsque des établissements publics de coopération intercommunale à fiscalité propre déjà membres d'un établissement public foncier local fusionnent, l'établissement issu de la fusion en est membre de plein droit. De même, en cas de fusion de communes déjà membres d'un établissement public foncier local, la commune issue de la fusion en est membre de plein droit."
],
    "Réécriture à droit constant : le maintien de l'établissement foncier est exprimé sous une condition directe, puis les effets de la fusion d'EPCI et de celle de communes sont distingués dans le second alinéa. Aucune réforme de fond.",
    "Le maintien après fusion en un seul EPCI reste conditionné à la fiscalité propre de cet EPCI. Le second alinéa exige l'appartenance préalable des entités fusionnées et conserve l'adhésion de plein droit de l'entité issue de la fusion. Les deux alinéas et le numéro, avec l'espace et la lettre B, sont conservés."
)

assert len(sources) == 24
assert set(drafts) == {a['number'] for a in sources}
answer = []
for source in sources:
    row = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    row.update(drafts[source['number']])
    answer.append(row)
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
