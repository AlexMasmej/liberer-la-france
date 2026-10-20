import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
drafts = {}


def add(number, xml, reason, notes):
    assert number not in drafts
    drafts[number] = (xml.strip(), reason, notes)


add('95 K', '''
<p>Pour l'application de la réduction d'impôt prévue au I de l'article 199 undecies B du code général des impôts, les investissements productifs neufs réalisés dans les départements d'outre-mer, à Saint-Pierre-et-Miquelon, à Saint-Barthélemy, à Saint-Martin, en Nouvelle-Calédonie, en Polynésie française, dans les îles Wallis et Futuna et les Terres australes et antarctiques françaises s'entendent des acquisitions ou créations d'immobilisations corporelles neuves et amortissables. Ces immobilisations doivent être affectées à des activités relevant des secteurs éligibles au titre du I de cet article.</p>
''',
    "Réécriture à droit constant : la définition des investissements est séparée de leur condition d'affectation, en conservant l'intégralité du champ territorial et les caractères corporel, neuf et amortissable. Aucune réforme de fond prévue par policy.json ne modifie cette définition.",
    "Renvoi au I de l'article 199 undecies B conservé. Toutes les désignations territoriales ou ensembles territoriaux de la source sont maintenus ; aucune extension de l'éligibilité sectorielle n'est introduite.")

add('95 M', '''
<p>Pour l'application du i. du I de l'article 199 undecies B du code général des impôts, relèvent du secteur de la maintenance les activités qui contribuent, pour l'essentiel, à entretenir ou à réparer le matériel technique utilisé pour la production de biens ou de services.</p>
''',
    "Réécriture à droit constant : le renvoi est placé en tête et les opérations d'entretien ou de réparation sont formulées par des verbes. Le critère de contribution essentielle et la nature technique du matériel demeurent. Aucune réforme de fond n'est applicable à cette définition.",
    "Le i du I de l'article 199 undecies B distingue bien la maintenance des services aux entreprises exclus. La réserve « pour l'essentiel » et la production tant de biens que de services sont conservées.")

add('95 N', '''
<p>Pour l'application du j. du I de l'article 199 undecies B du code général des impôts, relèvent du secteur de la production audiovisuelle et cinématographique les activités qui contribuent directement à créer ou à étendre outre-mer soit des établissements qui y produisent des œuvres audiovisuelles et cinématographiques, soit des industries techniques de production de ces œuvres. Le secteur de la diffusion comprend les activités qui contribuent directement à créer ou à étendre des établissements implantés outre-mer et qui y diffusent des œuvres audiovisuelles et cinématographiques, quel que soit le support technique utilisé. Les activités d'achat-revente et de location des supports techniques en sont exclues.</p>
''',
    "Réécriture à droit constant : les deux composantes de la production sont explicitées et l'exclusion propre à la diffusion fait l'objet d'une phrase autonome. Le lien direct avec la création ou l'extension outre-mer est maintenu. Aucune réforme de fond ne vise ce secteur.",
    "Renvoi au j du I de l'article 199 undecies B conservé. La production par des établissements et les industries techniques restent deux branches alternatives ; tous les supports demeurent admis pour la diffusion, sous l'exclusion de l'achat-revente et de la location de ces supports.")

add('95 O', '''
<p>Pour l'application du i de l'article 199 undecies B du code général des impôts, les activités du secteur des services informatiques ne sont pas considérées comme des services fournis aux entreprises.</p>
''',
    "Réécriture à droit constant : le renvoi ouvre la phrase et l'exclusion de qualification est exprimée directement. Il ne s'agit ni d'une exonération nouvelle ni d'une modification sectorielle issue de policy.json.",
    "Imprécision préexistante maintenue : la source vise le « i de l'article 199 undecies B » sans préciser le I. Le i relatif aux services fournis aux entreprises se trouve au I dans le corpus local. Une éventuelle précision de ce renvoi devra être coordonnée expressément.")

add('95 P', '''
<p>Pour l'application du h du I de l'article 199 undecies B du code général des impôts, relèvent du secteur de la navigation de croisière les activités organisées sur des navires dont l'autorisation d'embarquement porte sur plus de cinquante passagers.</p>
''',
    "Réécriture à droit constant : la définition est introduite par son renvoi et le seuil est rattaché explicitement à l'autorisation du navire. Aucune réforme de fond ne modifie ce régime distinct.",
    "Seuil strictement supérieur à cinquante passagers conservé : il concerne la capacité autorisée, et non le nombre de passagers effectivement embarqués. Le renvoi au h du I de l'article 199 undecies B est maintenu.")

add('95 Q', '''
<p>Sous réserve de la deuxième phrase du vingtième alinéa du I de l'article 199 undecies B du code général des impôts, la réduction d'impôt prévue au I de cet article est pratiquée au titre de l'année de mise en service de l'immobilisation ou de sa mise à la disposition de l'entreprise dans le cadre d'un contrat de crédit-bail. En cas de crédit-bail, le contribuable crédit-preneur ou les associés ou membres de l'entreprise crédit-preneuse pratiquent la réduction d'impôt.</p>
<p>Le calcul de la réduction d'impôt tient compte des aides publiques obtenues ainsi que de celles qui ont été demandées mais n'ont pas encore été accordées au 31 décembre de l'année mentionnée au premier alinéa. Si une régularisation est nécessaire, elle est effectuée au titre de cette même année, sur demande du contribuable.</p>
''',
    "Réécriture à droit constant : le fait déterminant l'année d'imputation, les bénéficiaires en crédit-bail et la prise en compte des aides sont énoncés dans des phrases distinctes. La demande de régularisation reste nécessaire. Aucune réforme de fond ne modifie ce calendrier.",
    "Les deux alinéas, le 31 décembre et la régularisation au titre de la même année sont conservés. La deuxième phrase du vingtième alinéa du I de l'article 199 undecies B vise bien les fondations des immeubles à construire. Le même alinéa comporte aussi une règle d'achèvement des travaux de rénovation ou de réhabilitation : la réserve de la source ne la vise pas expressément ; cette portée doit être contrôlée sans élargissement silencieux du renvoi.")

add('95 S', '''
<p>La réduction d'impôt prévue au I de l'article 199 undecies B du code général des impôts ne peut être imputée ni sur l'impôt résultant de la reprise de réductions d'impôt antérieurement pratiquées, ni sur celui résultant de la majoration du revenu global effectuée en application des vingt-troisième, vingt-cinquième et vingt-sixième alinéas de ce I et du 7 de l'article 199 undecies A du même code.</p>
<p>La créance sur l'Etat prévue au I de l'article 199 undecies B ne peut pas davantage servir à payer l'impôt résultant des reprises de réductions d'impôt, des majorations du revenu global et des réintégrations au revenu net global mentionnées au premier alinéa.</p>
''',
    "Réécriture à droit constant : les deux interdictions d'utilisation de l'avantage fiscal sont exprimées par des verbes explicites et restent réparties entre la réduction d'impôt et la créance sur l'Etat. Aucune réforme de fond ne porte sur ces interdictions.",
    "Renvois aux vingt-troisième, vingt-cinquième et vingt-sixième alinéas du I de l'article 199 undecies B et au 7 de l'article 199 undecies A conservés. Incohérence préexistante : le second alinéa renvoie à des « réintégrations au revenu net global » qui ne sont pas expressément nommées au premier ; certains alinéas législatifs visés décrivent des reprises plutôt que des majorations du revenu global. Ces formulations ne sont pas corrigées implicitement.")

add('95 T', '''
<p>I. - Les contribuables qui bénéficient de la réduction d'impôt prévue au I de l'article 199 undecies B du code général des impôts joignent à leur déclaration des revenus de l'année au titre de laquelle ils pratiquent cette réduction un état relatif à chaque investissement concerné. Pour les états prévus au présent article, l'administration fiscale réutilise les informations qu'elle détient déjà légalement, dans le respect des secrets protégés, sans demander une nouvelle communication des mêmes informations. Elle met les contribuables et les sociétés concernés en mesure de vérifier ces informations et d'en demander la correction à la source. Pour chaque investissement, l'état indique :</p>
<p>a) Le nom et l'adresse du siège social de l'entreprise propriétaire de l'investissement ou, en cas de crédit-bail, de l'entreprise qui en est locataire, ainsi que le chiffre d'affaires de l'entreprise qui exploite l'investissement, apprécié selon les modalités du premier alinéa du I de l'article 199 undecies B du code général des impôts ;</p>
<p>b) Le cas échéant, le pourcentage des droits aux résultats que le contribuable détient, directement ou indirectement, dans la société ou le groupement propriétaire de l'investissement ;</p>
<p>c) La nature précise de l'investissement ;</p>
<p>d) Le prix de revient hors taxe de l'investissement, la valeur réelle des biens remplacés et le montant des aides publiques obtenues ainsi que de celles demandées mais non encore accordées pour financer l'investissement ;</p>
<p>e) La date de mise en service de l'investissement ou, en cas de construction ou d'acquisition d'un immeuble à construire, la date d'achèvement des fondations ou, pour un bien faisant l'objet d'un contrat de crédit-bail, la date de sa mise à la disposition de l'entreprise ;</p>
<p>f) La ou les dates des décisions d'octroi des aides publiques ;</p>
<p>g) Le nom, l'adresse et la nature de l'activité de l'établissement dans lequel l'investissement est exploité ;</p>
<p>h) Le cas échéant, une copie de la décision d'agrément.</p>
<p>II. - (Périmé).</p>
<p>III. - Les sociétés propriétaires d'un hôtel, d'une résidence de tourisme ou d'un village de vacances classés ayant fait l'objet de travaux de rénovation et de réhabilitation qui ont ouvert droit, pour leurs associés, à la réduction d'impôt prévue au dix-huitième alinéa du I de l'article 199 undecies B du code général des impôts joignent un état à leur déclaration de résultats lorsque ce bien est donné en location dans les conditions du vingt-sixième alinéa du I de l'article 199 undecies B. Cet état indique :</p>
<p>a) Le montant global de l'investissement ;</p>
<p>b) Le montant des travaux de rénovation et de réhabilitation qui ont ouvert droit, pour les associés, à la réduction d'impôt prévue au dix-huitième alinéa du I de l'article 199 undecies B ;</p>
<p>c) (Périmé) ;</p>
<p>d) La liste des associés, avec leurs noms et adresses et le pourcentage de leurs droits aux résultats de la société ;</p>
<p>e) (Périmé).</p>
''',
    "À droit constant, les obligations déclaratives sont formulées avec un sujet explicite et les données, conditions, subdivisions et emplacements périmés sont conservés. Réforme de fond limitée, issue de la mesure « Déclarer une fois, corriger à la source » de policy.json : l'administration doit réutiliser les informations qu'elle détient déjà légalement pour les états du I et du III, sans les redemander, en respectant les secrets protégés et en permettant leur vérification et leur correction. Aucun taux, avantage fiscal ou condition d'éligibilité n'est modifié.",
    "Les I, II et III, les a à h du I et les a à e du III restent dans leur ordre et leur alinéa d'origine. Les renvois aux premier, dix-huitième et vingt-sixième alinéas du I de l'article 199 undecies B sont conservés. La règle nouvelle de réemploi doit être coordonnée avec les formulaires et les modalités de dépôt des deux états, la traçabilité des données et leur correction à la source ; elle ne dispense pas de fournir les informations manquantes ni de satisfaire les conditions fiscales. Les données détenues par le seul tiers de confiance ne sont pas assimilées à des informations détenues par l'administration. Aucun échange de données au-delà de ce qui est légalement détenu n'est autorisé.")

add('95 U', '''
<p>Le taux de rétrocession mentionné aux vingt-sixième et vingt-neuvième alinéas du I de l'article 199 undecies B du code général des impôts est égal au rapport suivant :</p>
<p>a) Au numérateur, la différence entre le montant hors taxes de l'investissement, diminué de la fraction de son prix de revient financée par une aide publique, et la valeur actualisée de toutes les sommes mises à la charge du locataire pour disposer du bien et en acquérir la propriété au terme de la location ;</p>
<p>b) Au dénominateur, le montant de la réduction d'impôt.</p>
<p>Pour actualiser les sommes payées par le locataire, le taux retenu est la moyenne des taux d'intérêt des emprunts souscrits par le bailleur pour financer l'investissement, pondérée par le montant de ces emprunts. Pour un emprunt à taux d'intérêt variable, seul le premier taux connu entre dans le calcul de cette moyenne. Ce calcul ne tient pas compte de l'avantage consenti, en application de ces mêmes dispositions, par les associés ou membres de cette entreprise.</p>
''',
    "Réécriture à droit constant : le rapport est présenté explicitement, sans changer son numérateur ni son dénominateur, et le calcul du taux d'actualisation est formulé en deux étapes. Aucune réforme de fond ne modifie la rétrocession ou son calcul.",
    "Renvois aux vingt-sixième et vingt-neuvième alinéas du I de l'article 199 undecies B vérifiés dans le corpus local. La pondération demeure fondée sur les montants empruntés ; pour un emprunt à taux variable, le calcul retient uniquement le premier taux connu. La portée de « ce calcul » et l'identification de « cette entreprise » dans la dernière phrase, déjà peu explicites dans la source, sont conservées et appellent un contrôle de coordination plutôt qu'une réinterprétation.")

add('95 ZA', '''
<p>Le tiers de confiance mentionné à l'article 170 ter du code général des impôts, après avoir conclu avec l'administration fiscale la convention individuelle prévue à l'article 95 ZG, signe avec son client un contrat définissant sa mission ainsi que les droits et obligations de chacune des parties.</p>
<p>La mission du tiers de confiance commence à la date à laquelle ce contrat est signé avec le client.</p>
''',
    "Réécriture à droit constant : l'articulation entre la convention administrative et le contrat du client est rendue explicite ; la prise d'effet de la mission est exprimée directement. Aucune réforme de fond ne modifie ces conditions.",
    "Renvois aux articles 170 ter du CGI et 95 ZG maintenus. La date de signature du contrat avec le client reste le point de départ de la mission ; elle n'est pas remplacée par celle de la convention individuelle.")

add('95 ZB', '''
<p>Le tiers de confiance conserve sur papier ou sous forme dématérialisée les pièces mentionnées au I de l'article 170 ter du code général des impôts.</p>
<p>Pendant toute la durée de conservation, les pièces dématérialisées doivent pouvoir être éditées à tout moment. Le tiers de confiance garantit que ces éditions sont parfaitement conformes et inaltérables.</p>
<p>(Alinéa disjoint).</p>
''',
    "Réécriture à droit constant : les deux modes de conservation et la disponibilité des éditions sont formulés plus directement, en maintenant les garanties de conformité et d'inaltérabilité. L'alinéa disjoint conserve sa place. Aucune réforme de fond ne supprime cette conservation probatoire.",
    "Le I de l'article 170 ter impose la conservation jusqu'à l'extinction du délai de reprise ; aucune durée différente n'est créée ici. La simplification déclarative de policy.json ne justifie pas de supprimer la conservation des pièces par le tiers de confiance.")

add('95 ZC', '''
<p>Dans les trente jours suivant la notification de la demande de l'administration, le tiers de confiance lui transmet les pièces justificatives et leur liste récapitulative, accompagnée des montants figurant sur ces pièces.</p>
''',
    "Réécriture à droit constant : le délai est placé en tête et le contenu de la transmission est rattaché explicitement aux pièces justificatives. Aucune réforme de fond ne modifie les demandes de pièces dans ce dispositif de contrôle.",
    "Délai de trente jours et point de départ à la notification, non à l'envoi de la demande, conservés. La liste et les montants restent à transmettre avec les justificatifs, conformément à la mission définie au I de l'article 170 ter.")

add('95 ZD', '''
<p>En exécution du contrat prévu à l'article 95 ZA, le tiers de confiance transmet par voie électronique à l'administration fiscale, pour le compte de ses clients, leurs déclarations annuelles de revenus et les annexes de ces déclarations. Cette obligation ne s'applique pas aux déclarations à souscrire pour les revenus perçus pendant l'année au cours de laquelle sa mission de tiers de confiance prend fin.</p>
<p>Pour une année donnée, le contribuable mentionné au I de l'article 170 ter du code général des impôts est considéré comme le client d'un tiers de confiance si le contrat prévu à l'article 95 ZA le lie à ce professionnel et a été conclu au plus tard lors du dépôt, par celui-ci, de la déclaration annuelle des revenus.</p>
''',
    "Réécriture à droit constant : l'obligation de transmission, son exception pour l'année de fin de mission et la condition de rattachement annuel du client sont distinguées clairement. Aucune réforme de fond ne modifie ces règles.",
    "Les deux alinéas sont conservés. L'exception porte sur l'année de perception des revenus au cours de laquelle la mission s'achève, et non sur l'année matérielle du dépôt. Le contrat doit être conclu au plus tard lors du dépôt effectué par le professionnel. Renvois aux articles 95 ZA et 170 ter inchangés.")

add('95 ZE', '''
<p>Le client qui souhaite bénéficier du dispositif du tiers de confiance s'engage, dans le contrat prévu à l'article 95 ZA, à donner son accord à la télétransmission de sa déclaration annuelle de revenus.</p>
<p>Dans ce contrat, le client reconnaît que le tiers de confiance l'a informé :</p>
<p>1° Que le dispositif prévu à l'article 170 ter du code général des impôts ne modifie pas les modalités de contrôle que l'administration fiscale exerce à son égard ;</p>
<p>2° Qu'il reste tenu de conserver un exemplaire des pièces justificatives pour répondre, le cas échéant, aux demandes de l'administration.</p>
''',
    "Réécriture à droit constant : l'accord du client et les informations qu'il reconnaît avoir reçues sont formulés avec des sujets explicites. Les 1° et 2° et leur portée sont maintenus. Aucune réforme de fond ne modifie les pouvoirs de contrôle ni la conservation des justificatifs.",
    "Les articles 95 ZA et 170 ter restent les fondements du contrat et du dispositif. Le client s'engage à donner son accord, sans présomption d'accord automatique ; la conservation personnelle d'un exemplaire demeure distincte de celle du tiers de confiance.")

add('95 ZF', '''
<p>La direction générale des finances publiques et les organismes qui représentent au niveau national les professions concernées concluent la convention nationale prévue au IV de l'article 170 ter du code général des impôts. Ils utilisent le modèle fixé par arrêté du ministre chargé du budget.</p>
<p>Cette convention demeure valide tant qu'aucune des parties signataires ne l'a dénoncée.</p>
''',
    "Réécriture à droit constant : les parties deviennent les sujets de l'obligation et l'exigence du modèle est isolée dans une phrase. La durée indéterminée jusqu'à dénonciation est conservée. Aucune réforme de fond ne vise la convention nationale.",
    "Le IV de l'article 170 ter est conservé et concorde sur la dénonciation de la convention nationale. La durée de trois ans des conventions individuelles n'est pas étendue à cette convention.")

add('95 ZG', '''
<p>La personne qui souhaite exercer la mission de tiers de confiance demande par écrit à conclure une convention individuelle. Elle adresse sa demande au directeur de la direction départementale ou régionale des finances publiques dans le ressort de laquelle elle est établie. Si elle possède plusieurs établissements, elle saisit le directeur de la direction départementale ou régionale dont relève son établissement principal.</p>
<p>Le tiers de confiance qui ne possède aucun établissement en France adresse sa demande au directeur général des finances publiques.</p>
''',
    "Réécriture à droit constant : la demande écrite et les trois règles de compétence sont exprimées dans des phrases successives. Aucune réforme de fond ne modifie les autorités compétentes ou la procédure de conventionnement.",
    "Le ressort de l'établissement principal reste déterminant en cas de pluralité d'établissements. La compétence du directeur général suppose l'absence de tout établissement en France, et non la seule situation étrangère du siège.")

add('95 ZH', '''
<p>Selon le cas, le directeur départemental ou régional des finances publiques ou le délégataire du directeur général des finances publiques statue sur la demande de conventionnement dans le mois qui suit sa notification. Il examine préalablement la situation du demandeur ainsi que, lorsque celui-ci est une personne morale, celle de ses dirigeants et administrateurs.</p>
<p>Il peut refuser de conclure la convention si les faits suivants ont été constatés, au cours des cinq années précédant la demande, à l'encontre du demandeur et, lorsqu'il s'agit d'une personne morale, de ses dirigeants et administrateurs :</p>
<p>a) Des manquements aux obligations fiscales de déclaration ou de paiement ;</p>
<p>b) L'application de pénalités prévues aux articles 1728, 1729, 1730 à 1734 et 1737 du code général des impôts ;</p>
<p>c) Une condamnation définitive pour fraude fiscale en application des articles 1741, 1743, 1746 et 1747 du code général des impôts, pour escroquerie à la TVA ou à un autre impôt ou taxe, ou pour complicité de ces infractions ;</p>
<p>d) L'application de sanctions disciplinaires comportant une suspension ou une interdiction définitive d'exercer ;</p>
<p>e) L'application d'une amende fiscale prononcée par un tribunal.</p>
<p>Le délai de décision peut être porté à trois mois si l'autorité administrative rencontre des difficultés pour obtenir les éléments nécessaires à sa décision.</p>
<p>La décision de refus est motivée et notifiée au demandeur par lettre recommandée avec demande d'avis de réception.</p>
<p>En cas d'acceptation, le directeur départemental ou régional des finances publiques ou le délégataire du directeur général des finances publiques adresse au demandeur une convention individuelle conforme au modèle établi par arrêté du ministre chargé du budget. Cette autorité et le tiers de confiance, ou la personne habilitée à le représenter, datent et signent la convention. Chaque partie en conserve un exemplaire.</p>
''',
    "Réécriture à droit constant : les étapes d'examen et de décision, le refus motivé et la signature sont exprimés plus directement, en maintenant les cinq catégories de faits et les délais. Aucune réforme de fond ne modifie les garanties du conventionnement.",
    "Délais conservés : un mois après notification de la demande, cinq années de faits antérieurs et prolongation possible à trois mois pour difficulté d'obtention des éléments. Le point de départ inhabituel formulé comme « notification de la demande » n'est pas remplacé par sa réception. La conjonction entre le demandeur personne morale et ses dirigeants et administrateurs est conservée. Tous les renvois fiscaux sont maintenus ; l'article 1733, inclus dans la plage 1730 à 1734, n'est pas retrouvé dans le corpus local. Plusieurs autres articles ont une abrogation différée signalée par le corpus, sans suppression anticipée de ces renvois.")

add('95 ZI', '''
<p>Le professionnel ne peut ni céder ni transmettre la convention qu'il a signée en qualité de tiers de confiance.</p>
<p>L'administrateur provisoire désigné demande par écrit à conclure une convention selon les modalités de l'article 95 ZG en cas d'incapacité temporaire ou définitive d'exercer, de démission ou de décès du professionnel personne physique, ou de cessation ou de cession d'activité du professionnel personne morale. Il adresse cette demande au directeur départemental ou régional des finances publiques ou au délégataire du directeur général des finances publiques. Cette autorité statue sur la demande et informe l'administrateur provisoire de sa décision dans les conditions de l'article 95 ZH.</p>
<p>Si sa demande est rejetée, l'administrateur provisoire en informe ses clients et leur restitue toutes les pièces justificatives qu'il détient dans les trois mois suivant la notification du refus du directeur départemental ou régional des finances publiques ou du délégataire du directeur général des finances publiques.</p>
<p>Dans les cas prévus au deuxième alinéa, la convention mentionnée à l'article 95 ZG cesse de produire ses effets et devient caduque.</p>
''',
    "Réécriture à droit constant : l'interdiction de transfert, les situations imposant une demande par l'administrateur provisoire et les suites d'un rejet sont formulées avec des sujets explicites. Les quatre alinéas sont maintenus. Aucune réforme de fond ne modifie ces cas de caducité.",
    "Le renvoi au deuxième alinéa reste exact. Les cas propres aux personnes physiques et morales demeurent distincts ; l'incapacité temporaire n'est pas omise. La restitution de toutes les pièces reste due dans les trois mois après notification du refus. La caducité prévue par la source n'est pas reportée à l'issue de la demande de l'administrateur provisoire. Renvois aux articles 95 ZG et 95 ZH maintenus.")

add('95 ZJ', '''
<p>La convention individuelle est conclue pour trois ans. Elle est renouvelée une seule fois par tacite reconduction pour une nouvelle période de trois ans, sauf si le directeur départemental ou régional des finances publiques, le délégataire du directeur général des finances publiques ou le professionnel la dénonce au moins trois mois avant l'expiration de la convention en cours.</p>
<p>Elle peut ensuite être renouvelée par périodes de trois ans selon la procédure des articles 95 ZG et 95 ZH. La demande doit être présentée au moins trois mois avant l'expiration de la convention en cours.</p>
<p>Le directeur départemental ou régional des finances publiques ou le délégataire du directeur général des finances publiques statue sur la demande et informe le demandeur de sa décision dans les conditions de l'article 95 ZH.</p>
<p>Lorsque la convention prévue à l'article 95 ZG n'est pas renouvelée, le tiers de confiance en informe ses clients et leur restitue toutes les pièces justificatives qu'il détient dans les trois mois suivant la notification du non-renouvellement.</p>
<p>Le directeur départemental ou régional des finances publiques ou le délégataire du directeur général des finances publiques informe l'organisme représentant au niveau national la profession dont le demandeur est membre de toutes les décisions prises au sujet de la convention individuelle prévue à l'article 95 ZG.</p>
<p>Les organismes représentant au niveau national la profession concernée établissent, mettent à jour et rendent publique la liste des professionnels qui exercent la mission de tiers de confiance. Ils transmettent cette liste à l'administration fiscale avant le 30 avril de chaque année.</p>
''',
    "Réécriture à droit constant : les phases de renouvellement sont distinguées, les délais sont rattachés à leur événement et les obligations des organismes professionnels sont formulées à la voix active. Aucune réforme de fond ne modifie la durée des conventions ou les obligations d'information.",
    "Les six alinéas sont maintenus. Durée de trois ans, une seule tacite reconduction, délais d'au moins trois mois avant expiration et restitution dans les trois mois de la notification sont conservés. La liste reste à transmettre avant le 30 avril, et non au plus tard le 30 avril. Renvois aux articles 95 ZG et 95 ZH maintenus.")

add('95 ZK', '''
<p>Le directeur départemental ou régional des finances publiques ou le délégataire du directeur général des finances publiques peut résilier la convention lorsqu'il constate les faits suivants concernant le tiers de confiance ou la société dans laquelle celui-ci exerce sa profession et, dans ce dernier cas, ses dirigeants ou administrateurs :</p>
<p>a) Des manquements aux obligations fiscales de déclaration ou de paiement ;</p>
<p>b) L'application de pénalités prévues aux articles 1728, 1729, 1730 à 1734 et 1737 du code général des impôts ;</p>
<p>c) Une condamnation définitive pour fraude fiscale en application des articles 1741, 1743, 1746 et 1747 du code général des impôts, pour escroquerie à la TVA ou à un autre impôt ou taxe, ou pour complicité de ces infractions ;</p>
<p>d) L'application de sanctions disciplinaires comportant une suspension ou une interdiction définitive d'exercer ;</p>
<p>e) Une amende fiscale prononcée par un tribunal ;</p>
<p>f) Des manquements à l'une des obligations stipulées dans la convention individuelle prévue à l'article 95 ZG.</p>
<p>Avant de décider, cette autorité met le tiers de confiance en mesure de présenter ses observations sur les faits qui lui sont reprochés.</p>
<p>La décision de résiliation est motivée et notifiée au tiers de confiance par lettre recommandée avec demande d'avis de réception.</p>
''',
    "Réécriture à droit constant : le pouvoir de résiliation et les six catégories de faits sont présentés directement, en conservant la procédure contradictoire et la notification motivée. Aucune réforme de fond ne modifie les motifs ou garanties de résiliation.",
    "Les a à f et les deux derniers alinéas demeurent à leur place. Le périmètre visant le professionnel, la société et, dans ce dernier cas, les dirigeants ou administrateurs est conservé sans résolution implicite de la conjonction de la source. Aucun délai de cinq ans n'est importé de l'article 95 ZH. L'article 1733, compris dans le renvoi 1730 à 1734, est absent du corpus local ; les renvois aux articles dont l'abrogation est différée ne sont pas supprimés par anticipation.")

add('95 ZL', '''
<p>En cas de résiliation de la convention prévue à l'article 95 ZG, le tiers de confiance informe ses clients de cette résiliation et leur restitue toutes les pièces justificatives qu'il détient dans les trois mois suivant la notification de la décision.</p>
''',
    "Réécriture à droit constant : la résiliation est placée en tête et les deux obligations du tiers de confiance sont exprimées directement. Aucune réforme de fond ne modifie le délai ni la restitution des pièces.",
    "Le délai de trois mois court à compter de la notification de la résiliation. La totalité des pièces détenues doit être restituée. Le renvoi à l'article 95 ZG est conservé.")

add('95 ZM', '''
<p>Lorsque sa convention est devenue caduque ou a été résiliée en application des articles 95 ZI ou 95 ZK, le tiers de confiance doit attendre l'expiration d'un délai de six mois avant de déposer une nouvelle demande de convention. Il doit, en outre, ne plus faire l'objet d'une suspension et être toujours membre de l'organisme représentant sa profession au niveau national.</p>
<p>La nouvelle demande suit la procédure prévue aux articles 95 ZG et 95 ZH.</p>
''',
    "Réécriture à droit constant : le délai d'attente est dissocié des deux conditions qui s'y ajoutent, sans modifier leur caractère cumulatif. Aucune réforme de fond ne modifie les conditions d'une nouvelle demande.",
    "Délai de six mois et quatre renvois internes conservés. Imprécision préexistante : la source ne définit pas expressément le point de départ du délai de six mois. La proposition n'ajoute ni date de notification ni autre événement déclencheur. L'absence de suspension et le maintien de l'appartenance professionnelle restent tous deux exigés.")

add('95 ZN', '''
<p>Le dispositif du tiers de confiance ne peut être sollicité que pour les déductions du revenu global, réductions ou crédits d'impôt prévus aux articles 199 quater C, 199 quater F, 199 septies, 199 decies I, 199 decies E, 199 decies EA, 199 decies G et 199 decies H, 199 undecies A, 199 undecies B, 199 undecies C et 199 undecies D, aux I à VI ter de l'article 199 terdecies-0 A, à l'article 199 terdecies-0 B, aux 1 à 4 de l'article 199 sexdecies, aux articles 199 tervicies, 199 sexvicies, 200, 200 quater, 200 quater A, 200 quater B et 200 decies A du code général des impôts, ainsi qu'à l'article 18 bis de l'annexe IV à ce code.</p>
''',
    "Réécriture à droit constant : le dispositif est placé en sujet et l'énumération exhaustive des avantages admis est conservée, avec ses limites de subdivisions. Aucune réforme de fond ne justifie d'étendre cette liste ou d'en retirer des régimes historiques.",
    "Tous les renvois sont conservés, y compris les I à VI ter de l'article 199 terdecies-0 A et les 1 à 4 de l'article 199 sexdecies. Le renvoi à l'article 18 bis de l'annexe IV existe dans le corpus local. L'article 199 decies H n'y est pas retrouvé : renvoi préexistant à contrôler, sans le supprimer. Les articles 200, 200 quater et 200 quater A sont signalés en abrogation différée au 1er janvier 2027 ; aucune suppression anticipée ni extinction des droits historiques n'est déduite de ce signalement.")

add('95 ZO', '''
<p>I. – La personne tenue d'effectuer la retenue à la source mentionnée au 1° du 2 de l'article 204 A du code général des impôts peut corriger une erreur qu'elle constate dans une déclaration souscrite au titre d'un mois. Elle procède à cette régularisation par une inscription distincte dans une déclaration souscrite au titre d'un mois de la même année civile.</p>
<p>II. – Si l'erreur corrigée a entraîné un excédent de retenue à la source, cet excédent est imputé sur le montant de la retenue à la source due au titre du mois pour lequel la déclaration est souscrite. Lorsque l'excédent dépasse ce montant, la différence est remboursée dans les conditions de l'article L. 190 du livre des procédures fiscales. La différence dont le remboursement a été demandé ne peut pas être imputée.</p>
''',
    "Réécriture à droit constant : la faculté de correction, l'inscription distincte et le traitement de l'excédent sont exprimés en phrases successives. Les I et II sont maintenus. Aucune réforme de fond ne modifie la retenue, son remboursement ou le calendrier de régularisation.",
    "Le renvoi au 1° du 2 de l'article 204 A est vérifié dans le corpus local. Le renvoi à l'article L. 190 du livre des procédures fiscales est conservé ; ce livre n'est pas inclus dans le corpus fourni. La correction reste limitée aux déclarations au titre de mois d'une même année civile ; la différence demandée en remboursement ne peut être imputée. La note source est prise en compte : application aux revenus perçus ou réalisés à compter du 1er janvier 2019, conformément à l'article 6 du décret n° 2017-866 du 9 mai 2017 modifié par l'article 2 du décret n° 2017-1676 du 7 décembre 2017. Cette date historique n'est pas une date d'entrée en vigueur d'une réforme future.")


assert len(sources) == len(drafts) == 24
answer = []
for source in sources:
    xml, reason, notes = drafts[source['number']]
    item = {key: source[key] for key in ['code_id', 'source_id', 'source_sha256', 'number']}
    item.update(proposed_xml=xml, reason=reason, review_notes=notes, status='rewrite_draft')
    answer.append(item)

Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
