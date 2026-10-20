import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
drafts = {}
fragments = Path('fragments')
fragments.mkdir(exist_ok=True)


def add(number, text, reason, notes):
    paragraphs = text.strip().splitlines()
    xml = '\n'.join('<p>' + p.strip() + '</p>' for p in paragraphs if p.strip())
    drafts[number] = (xml, reason, notes)
    (fragments / (number.replace(' ', '_') + '.xml')).write_text(xml + '\n')


add('275 ter N', '''
Les organismes de contrôle agréés signalent sans délai, par tout moyen, à la direction régionale des douanes et droits indirects dont ils relèvent toute irrégularité affectant la garantie des ouvrages en métaux précieux.
''', "Réécriture à droit constant : l'obligation de signalement est formulée directement, avec son destinataire et son caractère immédiat. Aucune réforme de fond prévue par policy.json ne concerne cette garantie.", "Le signalement reste sans délai et peut être effectué par tout moyen. Le champ couvre toute irrégularité affectant la garantie des ouvrages en métaux précieux.")

add('275 ter P', '''
Les organismes de contrôle agréés déclarent immédiatement à la direction régionale des douanes et droits indirects dont ils dépendent toute disparition ou tout incident concernant la conservation des poinçons de garantie métalliques ou des fichiers informatiques qui en portent la version dématérialisée et dont ils ont la charge. L'administration mène une enquête, pendant laquelle l'agrément est suspendu. Si la responsabilité de l'organisme est établie à l'issue de l'enquête administrative, l'administration engage une procédure de retrait de l'agrément. Les poinçons de garantie métalliques usagés, les fichiers informatiques devenus défectueux et les poinçons ou fichiers détenus par un organisme dont l'agrément a été retiré sont remis à la direction régionale des douanes et droits indirects dont dépend cet organisme. Après information de l'administration des douanes, ils sont détruits ou renvoyés à la Monnaie de Paris.
''', "À droit constant, les étapes de déclaration, d'enquête, de suspension et de retrait sont rendues plus lisibles. Le sort des poinçons et fichiers est énoncé en deux phrases. Aucune réforme de fond n'est appliquée.", "Le paragraphe unique est conservé. La suspension demeure limitée à la durée de l'enquête ; la procédure de retrait suppose que la responsabilité ait été établie. La remise à la direction régionale et l'information de l'administration avant destruction ou renvoi sont maintenues.")

add('276', '''
Toute personne qui souhaite fabriquer des tabacs manufacturés doit obtenir au préalable un numéro d'identification en qualité de fabricant.
Toute personne qui souhaite importer, introduire ou commercialiser en gros des tabacs manufacturés doit obtenir au préalable un numéro d'identification en qualité de fournisseur.
Le demandeur doit satisfaire aux conditions d'exercice d'une profession commerciale et fournir une caution solvable garantissant à l'administration des douanes et droits indirects le paiement du précompte sur remise prévu à l'article 281.
''', "Réécriture à droit constant : les deux catégories d'identification et les conditions imposées au demandeur sont explicitées sans modifier les activités visées. Aucune réforme de fond n'est applicable à ce régime.", "La source porte le statut ABROGE_DIFF et une fin de validité au 1er août 2027 : cette échéance n'est pas une date d'entrée en vigueur des réformes de policy.json. Le renvoi à l'article 281 est conservé, mais cet article est absent du corpus public fourni ; sa coordination avec le précompte sur remise nécessite contrôle.")

add('278', '''
I. – Dans chaque fabrique et lieu de stockage, le fabricant tient une comptabilité matières conforme aux articles 286 H et 286 J pour les dispositions qui le concernent.
Cette comptabilité doit également indiquer :
a) Les quantités et variétés de tabacs bruts ou semi-ouvrés ainsi que les différents autres produits utilisés dans la fabrication des tabacs manufacturés ;
b) Les quantités de tabacs manufacturés fabriquées et livrées, détaillées par variété de produits et par mois de fabrication et de livraison, avec l'indication des références de vente au détail ;
c) Les quantités de tabacs manufacturés en stock à la fin de chaque mois.
II. – Le fournisseur tient la comptabilité matières.
Pour les quantités de tabacs sorties à destination des débitants de tabacs, cette comptabilité doit également indiquer le numéro et la date du document de livraison.
III. – Le fabricant et le fournisseur présentent la comptabilité matières mentionnée aux I et II à toute réquisition des agents de l'administration des douanes et droits indirects.
''', "À droit constant, les mentions comptables sont présentées avec des sujets explicites, notamment pour la présentation aux agents. Les subdivisions I à III et a à c sont conservées. Aucune réforme de fond n'est introduite.", "Conserver les renvois aux articles 286 H et 286 J, la ventilation mensuelle et par variété, les références de vente au détail et les données du document de livraison. Le II de la source ne détaille pas davantage les règles générales de la comptabilité du fournisseur : aucune condition supplémentaire n'est créée.")

add('279', '''
Si le fabricant ou le fournisseur ne remplit plus les conditions fixées ou commet une infraction aux dispositions du code général des impôts, le ministre de l'économie, des finances et de l'industrie peut lui retirer son numéro d'identification. Il doit auparavant lui permettre de présenter ses observations.
Le retrait est notifié par lettre recommandée avec demande d'avis de réception postal. Dès cette notification, il entraîne pour l'intéressé :
1° S'il s'agit d'un fournisseur, l'interdiction d'importer, d'introduire et de commercialiser en gros des tabacs manufacturés ; s'il s'agit d'un fabricant, l'interdiction de fabriquer des tabacs manufacturés.
2° L'obligation d'inventorier les quantités de tabac en stock à la date de notification du retrait, à l'exclusion des quantités placées en entrepôt douanier, et de remettre cet inventaire à l'administration des douanes et droits indirects dans les cinq jours suivant la notification. L'intéressé dispose alors de trois mois pour écouler le stock inventorié et, le cas échéant, celui qu'il détient en entrepôt douanier.
''', "Réécriture à droit constant : la garantie contradictoire, les effets immédiats du retrait et les obligations de liquidation des stocks sont formulés plus directement, sans réforme de fond.", "Les 1° et 2° restent aux mêmes emplacements. Les cinq jours de remise de l'inventaire et les trois mois d'écoulement sont conservés, ainsi que l'exclusion des stocks en entrepôt douanier du seul inventaire. La source est en abrogation différée au 1er août 2027 ; la dénomination ministérielle historique est conservée.")

add('280', '''
La direction générale des douanes et droits indirects rend la liste des débitants accessible aux fournisseurs titulaires d'un numéro d'identification.
''', "À droit constant, la mise à disposition de la liste est reformulée en précisant les bénéficiaires. Aucune réforme de fond ne concerne cette obligation.", "Aucune modalité technique d'accès n'est ajoutée. La source est en abrogation différée au 1er août 2027 ; cette échéance est distincte des réformes de policy.json.")

add('282', '''
Les fournisseurs peuvent accorder aux débitants les délais et facilités de paiement mentionnés à l'article L. 3512-14-19 du code de la santé publique sous la forme du crédit à la livraison, du crédit de stock et du crédit saisonnier. Ces crédits sont définis par arrêté du ministre de l'économie et des finances (1).
Cet arrêté fixe également la valeur minimale de la commande à partir de laquelle le fournisseur doit livrer au débitant, à ses propres frais, les tabacs commandés (2).
(1) Voir les articles 56 AC à 56 AG de l'annexe IV.
(2) Voir l'article 56 AB de l'annexe IV.
''', "Réécriture à droit constant : les trois formes de crédit et le seuil déclenchant la livraison aux frais du fournisseur sont formulés en phrases plus courtes. Les indications des notes source sont intégrées aux deux notes déjà présentes dans le texte. Aucune réforme de fond n'est appliquée.", "Les renvois de la source et de ses notes vers l'annexe IV sont conservés et leurs articles figurent dans le corpus fourni. Coordonner avec l'obligation prévue à l'article 282 A lorsque le débitant justifie d'une caution solidaire ; le verbe « peuvent » du premier alinéa ne supprime pas cette obligation.")

add('282 A', '''
En application de l'article L. 3512-14-19 du code de la santé publique, chaque fournisseur doit accorder les délais et facilités de paiement prévus à l'article 282 au débitant qui justifie d'une caution solidaire. Cette caution vaut à l'égard de tous les fournisseurs de ce débitant.
''', "À droit constant, l'obligation du fournisseur et sa condition de cautionnement solidaire sont rendues explicites. Aucune réforme de fond n'est introduite.", "Le renvoi à l'article 282 et la portée de la caution envers tous les fournisseurs sont maintenus. L'article 56 AD de l'annexe IV du corpus mentionne en outre l'agrément exprès de la caution par l'administration ; cette exigence distincte n'est ni supprimée ni ajoutée au présent article.")

add('282 B', '''
Le débitant joint à toute demande de délais et facilités de paiement adressée à un fournisseur une attestation de la caution précisant les types de crédit pour lesquels elle lui accorde son cautionnement.
''', "Réécriture à droit constant : le débitant devient le sujet explicite de l'obligation de joindre l'attestation, dont le contenu est conservé. Aucune réforme de fond n'est appliquée.", "L'attestation demeure requise pour toute demande ; elle doit préciser les types de crédit couverts pour le débitant concerné, sans extension automatique aux autres crédits.")

add('282 C', '''
Lorsqu'elle retire sa garantie à un débitant, la caution en informe tous les fournisseurs titulaires d'un numéro d'identification par lettre recommandée avec demande d'avis de réception.
À l'égard de chaque fournisseur, ce retrait prend effet cinq jours francs après la réception de la lettre recommandée. Il rend alors immédiatement exigibles les sommes dues par le gérant du débit de tabac.
''', "À droit constant, le déclenchement du délai est rattaché à la réception par chaque fournisseur et l'exigibilité est énoncée séparément. Aucune réforme de fond n'est introduite.", "Les cinq jours restent des jours francs et se calculent pour chaque fournisseur. L'exigibilité immédiate est l'effet du retrait devenu effectif ; le gérant du débit demeure le débiteur désigné.")

add('284', '''
Chaque année, l'administration établit un calendrier d'au moins six campagnes d'homologation des prix de vente au détail des tabacs manufacturés. L'intervalle entre les campagnes ne peut dépasser trois mois.
À la demande de l'administration, les fabricants de tabacs manufacturés lui transmettent par voie dématérialisée les prix de vente au détail de chacun de leurs produits, par marque et dénomination commerciale, dans les conditions définies aux articles L. 3512-14-15 à L. 3512-14-18 du code de la santé publique. Ils effectuent cette transmission directement ou par l'intermédiaire des fournisseurs agréés, dans les cinq jours ouvrés à compter de la demande. À l'expiration de ce délai, ils ne peuvent déposer aucune demande supplémentaire ni aucune demande de correction.
Les prix sont homologués par arrêté conjoint du ministre chargé du budget et du ministre chargé de la santé, au plus tard trois mois après l'ouverture de la campagne d'homologation par la demande mentionnée à l'alinéa précédent. Ils sont publiés au Journal officiel de la République française.
Lorsqu'un fabricant ou un fournisseur ne dépose pas de prix au cours d'une campagne, l'administration réexamine la liste de prix de la dernière campagne pour laquelle il en a déposé. Si ces prix respectent encore les conditions des dispositions du code de la santé publique mentionnées au deuxième alinéa, elle les homologue selon les modalités de l'alinéa précédent.
''', "Réécriture à droit constant : le calendrier, les modalités de transmission et les deux délais sont distingués par des phrases plus lisibles. Le réexamen des prix antérieurs est conservé, sans réforme de fond.", "Les quatre alinéas et les renvois internes restent en place. Contrôle des paramètres : au moins six campagnes par an, intervalle maximal de trois mois, transmission dans les cinq jours ouvrés, homologation dans les trois mois suivant l'ouverture. L'absence de dépôt peut concerner un fabricant ou un fournisseur, comme dans la source.")

add('285', '''
Lors d'un changement de prix de vente, la différence entre la valeur des stocks en consignation chez les débitants au nouveau prix et leur valeur à l'ancien prix est atténuée de l'incidence de ce changement sur la remise sur vente. En cas de hausse des prix, le débitant doit le montant ainsi déterminé à chacun des fournisseurs qui lui a livré les tabacs. En cas de baisse, le fournisseur le doit à chacun des débitants consignataires.
''', "À droit constant, la règle de calcul est séparée des deux sens de paiement selon la hausse ou la baisse des prix. Aucune réforme de fond n'est appliquée.", "La prise en compte de la remise sur vente et le champ des seuls stocks en consignation sont conservés. La formulation « atténuée de l'incidence » est maintenue sans introduire une nouvelle formule de calcul ni modifier le traitement du signe de la différence.")

add('285 A', '''
La personne mentionnée à l'article 302 F ter du code général des impôts qui exploite un comptoir de vente ou une boutique de vente à bord et souhaite y vendre des tabacs manufacturés demande l'agrément du statut d'acheteur-revendeur prévu à l'article L. 3512-14-5 du code de la santé publique. Elle dépose sa demande auprès du service des douanes et droits indirects dans le ressort territorial duquel se situe le comptoir ou la boutique à bord, au moyen d'un formulaire dont le modèle est fixé par arrêté du ministre chargé du budget.
''', "Réécriture à droit constant : le demandeur, l'agrément sollicité, le service compétent et le formulaire sont énoncés en deux phrases, sans changement de fond.", "Les deux renvois, le ressort territorial et la compétence du ministre chargé du budget pour le modèle de formulaire sont conservés. L'article 302 F ter figure au corpus avec un statut d'abrogation différée et une borne technique 2222-02-22 : contrôler sa coordination avant consolidation, sans traiter cette borne comme une date de réforme.")

add('285 B', '''
La mention « exportation » doit figurer sur chaque unité de conditionnement de tabacs manufacturés vendus dans les comptoirs de vente ou les boutiques de vente à bord, ainsi que sur chaque unité de conditionnement de tabacs manufacturés destinés à l'avitaillement.
''', "À droit constant, l'obligation de marquage est formulée directement et les trois destinations sont explicitées. Aucune réforme de fond n'est introduite.", "La mention obligatoire « exportation » est reproduite exactement. L'obligation demeure applicable à chaque unité de conditionnement, y compris pour l'avitaillement.")

add('286 B', '''
Pour l'accise prévue à l'article L. 314-1 du code des impositions sur les biens et services, les tabacs manufacturés sont considérés comme ayant atteint l'issue de fabrication lorsqu'ils sortent des établissements de production.
''', "Réécriture à droit constant : la définition de l'issue de fabrication est exprimée par le fait qui la caractérise. Aucune réforme de fond n'est appliquée.", "Le fait retenu reste la sortie des établissements de production, sans assimilation à la vente ni ajout d'une condition. Renvoi à l'article L. 314-1 du code des impositions sur les biens et services conservé.")

add('286 D', '''
Lors d'un changement de prix de vente des tabacs, les fournisseurs et les débitants déclarent au service des douanes et droits indirects, dans les cinq jours suivant l'entrée en vigueur des nouveaux prix, les quantités qu'ils détiennent à cette date, qui sont affectées par ce changement et qui ont supporté les droits et taxes exigibles sur la base de l'ancien prix.
Les débitants établissent une déclaration distincte pour les quantités de tabacs en consignation provenant de chaque fournisseur. Le service des douanes et droits indirects adresse un exemplaire de chacune de ces déclarations au fournisseur concerné.
''', "À droit constant, les conditions cumulatives de déclaration et la répartition des tâches entre débitants et service des douanes sont rendues explicites. Aucune réforme de fond n'est introduite.", "Le délai reste de cinq jours, sans ajout du qualificatif « ouvrés » ou « francs ». Le stock est apprécié à la date d'entrée en vigueur des nouveaux prix. Les déclarations distinctes par fournisseur ne concernent que les tabacs en consignation.")

add('286 E', '''
Pour les tabacs déclarés en application de l'article 286 D, la différence entre les droits et taxes calculés aux nouveaux prix et ceux calculés aux anciens prix est, selon le cas, versée par le fournisseur au service des douanes et droits indirects ou restituée au fournisseur par ce service. Ce versement ou cette restitution intervient au plus tard le 5 du quatrième mois suivant celui du changement de prix.
''', "Réécriture à droit constant : le calcul de la différence et l'échéance du versement ou de la restitution sont exposés dans deux phrases. Aucune réforme de fond n'est appliquée.", "Le fournisseur reste l'interlocuteur du service pour les deux sens du règlement. Le délai est le 5 du quatrième mois suivant le mois du changement de prix, et non un délai de quatre mois à compter du jour du changement. Renvoi à l'article 286 D conservé.")

add('286 F', '''
Les articles 276 à 286 E ne s'appliquent pas dans les départements d'outre-mer.
''', "À droit constant, l'exclusion territoriale est formulée directement, sans modifier la plage d'articles visée. Aucune réforme de fond n'est introduite.", "La plage 276 à 286 E et les départements d'outre-mer sont conservés sans élargissement territorial. La source indique une abrogation différée au 1er août 2027 ; l'exclusion n'est pas pérennisée au-delà de cette échéance par une disposition nouvelle.")

add('286 H', '''
I. – 1° L'« entrepôt fiscal suspensif des droits d'accises » mentionné au III de l'article 302 G du code général des impôts désigne chacun des lieux où l'entrepositaire agréé produit, transforme, détient, reçoit ou expédie, dans l'exercice de sa profession, les produits mentionnés à ce III.
2° Après en avoir informé le service des douanes et droits indirects territorialement compétent, l'entrepositaire agréé peut décider de considérer tout ou partie de ses locaux comme un seul entrepôt fiscal suspensif des droits d'accises, dénommé « site d'exploitation », pour tenir la comptabilité matières mentionnée au III de l'article 302 G du même code, ci-après dénommée « la comptabilité matières ».
Dans ce cas, il doit toutefois pouvoir justifier, à toute réquisition des agents des douanes et droits indirects, des productions, transformations, détentions, entrées et sorties sur les lieux mêmes où ces opérations sont effectuées.
II. – (Abrogé)
''', "Réécriture à droit constant : la définition de l'entrepôt et la faculté de regroupement en site d'exploitation sont énoncées avec des sujets explicites. La justification locale des opérations est maintenue, sans réforme de fond.", "Le I, ses 1° et 2° et le II abrogé sont conservés, ainsi que les quatre alinéas. Le regroupement reste précédé d'une information et n'est pas transformé en demande d'autorisation. L'article 302 G du corpus porte un statut d'abrogation différée avec une borne technique 2222-02-22 ; le renvoi au III est maintenu et appelle un contrôle de consolidation.")

add('286 I', '''
I. – 1° Pour les entrepositaires agréés qui produisent des produits vitivinicoles régis par le règlement (CE) n° 1234/2007 du Conseil du 22 octobre 2007 portant organisation commune des marchés dans le secteur agricole et dispositions spécifiques en ce qui concerne certains produits de ce secteur (règlement « OCM unique »), les registres vitivinicoles constituent la comptabilité matières. Ces registres sont ceux prévus par le règlement (CE) n° 436/2009 de la Commission du 26 mai 2009 portant modalités d'application du règlement (CE) n° 479/2008 du Conseil en ce qui concerne le casier viticole, les déclarations obligatoires et l'établissement des informations pour le suivi du marché, les documents accompagnant les transports des produits et les registres à tenir dans le secteur vitivinicole ;
2° À la demande des agents des douanes et droits indirects, l'entrepositaire agréé leur remet une copie des documents qui constituent la comptabilité matières.
II. – Outre le respect de la réglementation communautaire mentionnée au I, l'établissement des registres vitivinicoles obéit aux règles suivantes.
1° Les opérations sont enregistrées chronologiquement, sans blanc ni rature, sur un registre aux pages numérotées ou selon une procédure informatisée. L'enregistrement intervient au plus tard le jour ouvrable suivant l'opération, ou le troisième jour ouvrable pour les sorties.
Par exception, les écritures de chaque opération du mois précédent peuvent être portées sur les registres au plus tard le dixième jour de chaque mois. Cette faculté suppose que les pièces justificatives permettent toujours de contrôler les entrées, les sorties et les manipulations, à toute réquisition des agents des douanes et droits indirects ou des agents de la concurrence, de la consommation et de la répression des fraudes.
Les registres comportent les colonnes dont les intitulés sont exigés par la réglementation communautaire. Pour les transactions soumises au visa de l'établissement mentionné à l'article L. 621-1 du code rural et de la pêche maritime, ils portent les références des contrats d'achat soumis à ce visa.
Sans préjudice des autres dispositions des règlements et accords interprofessionnels visés notamment aux articles L. 632-1 à L. 632-7 du code rural et de la pêche maritime, les registres comportent, pour les vins bénéficiant d'une protection de dénomination, les références aux déclarations de revendication de cette protection prévues par la réglementation en vigueur. Ils comportent également les numéros d'enregistrement des contrats d'achat et les numéros des déclarations de transactions soumis préalablement aux interprofessions, selon les accords interprofessionnels étendus mentionnés à ces articles.
Le cas échéant, les registres portent les références aux comptes d'âges ou de vieillissement prévus par les textes réglementaires en vigueur et les règlements des organismes interprofessionnels.
Lorsque l'article 450 du code général des impôts ou les articles 661 et 662 du code rural ancien s'appliquent, les registres font référence, pour chaque mouvement de produits vitivinicoles mentionnés au règlement (CE) n° 1234/2007 précité, à l'avis de blocage, à l'engagement de garantie ou de mainlevée du porteur du warrant agricole ou du porteur de l'engagement de garantie.
L'identité du détenteur des registres figure sur la première page de chaque registre.
2° Les registres vitivinicoles peuvent être tenus selon une procédure informatisée.
Les personnes qui tiennent ces registres informatisés permettent aux agents de l'administration, à toute réquisition, de vérifier leur conformité à la réglementation communautaire en vigueur, à l'article 286 H et au présent article.
3° Les registres vitivinicoles peuvent être constitués d'éléments d'une comptabilité commerciale informatisée si celle-ci comporte :
a) Toutes les indications nécessaires sur les mouvements des produits et le déroulement des manipulations, conformément aux dispositions européennes et aux informations prévues au 1° du II ;
b) La reprise des inventaires physiques des produits réalisés à la clôture de l'exercice comptable.
III. – Au plus tard le dixième jour de chaque mois, les entrepositaires agréés établissent la balance des registres. Ils y inscrivent, pour tous les produits vitivinicoles, le stock théorique au début et à la fin du mois précédent ainsi que le total des entrées et des sorties de ce mois.
Cette balance ne peut, à elle seule, servir de preuve pour constater les manquants qui rendent l'impôt exigible en application du 2° bis du 1 du I de l'article 302 D du code général des impôts.
Au plus tard le dixième jour de chaque mois, les entrepositaires agréés transmettent au service des douanes et droits indirects territorialement compétent une déclaration récapitulative. Celle-ci comporte les renseignements mentionnés au premier alinéa du présent III et, le cas échéant, ceux prévus au 1° du II.
IV. – Pour les récoltants, y compris les sociétés coopératives et leurs unions, les registres sont clôturés une fois par an. La déclaration annuelle est transmise au service des douanes et droits indirects territorialement compétent au plus tard le dixième jour du deuxième mois suivant la clôture des comptes.
V. – Des annotations au verso des déclarations de récolte et de stocks mentionnées à l'article 407 du code général des impôts peuvent constituer les registres.
VI. – Les registres sont tenus par entrepôt fiscal suspensif de droits d'accises, sur les lieux mêmes où les produits sont détenus.
Au sein d'un site d'exploitation, ils sont tenus au siège de l'exploitation.
Ce siège est le lieu où se situe l'installation principale du site.
Dans ce cas, les entrepositaires agréés indiquent à l'administration des douanes et droits indirects l'adresse de ce lieu.
VII. – Un seul document peut regrouper les registres vitivinicoles.
VIII. – Les registres, les pièces justificatives nécessaires à leur tenue et les documents prévus aux IV et VI sont conservés dans les conditions et selon les modalités fixées à l'article L. 102 B du livre des procédures fiscales.
IX. – Les documents mentionnés aux articles 302 M, 302 M bis et 302 M ter du code général des impôts pour l'expédition ou l'enlèvement des produits vitivinicoles ne peuvent être validés que si l'entrepositaire agréé respecte les obligations de tenue de la comptabilité matières prévues au présent article et les obligations mentionnées à l'article 614.
En cas de manquements graves ou répétés aux dispositions qui précèdent, le directeur interrégional des douanes et droits indirects peut retirer la qualité d'entrepositaire agréé.
''', "Réécriture intégrale à droit constant : les règles de tenue, les possibilités d'informatisation, les conditions du report mensuel des écritures et les obligations déclaratives sont exposées en phrases plus courtes. Les neuf subdivisions et tous les alinéas sont maintenus. Aucune réforme de fond n'est appliquée.", "Délais conservés : jour ouvrable suivant l'opération, troisième jour ouvrable pour les sorties, dérogation au dixième jour du mois, balance et déclaration mensuelles au dixième jour, déclaration annuelle au dixième jour du deuxième mois suivant la clôture. La balance ne suffit pas seule à prouver un manquant. Les règlements (CE) n° 1234/2007 et n° 436/2009, le code rural ancien et les renvois aux articles 302 D, 407, 450, 302 M, 302 M bis, 302 M ter et 614 sont ceux de la source : ces articles du CGI sont absents du corpus fourni, ce qui appelle un contrôle de leur actualité et de leur coordination, sans substitution conjecturale. Le renvoi du VIII aux documents du VI, alors que ce VI traite surtout du lieu de tenue et de l'adresse, mérite également contrôle et reste conservé. La note source rattache une modification à l'article 81-I-9° de la loi n° 2015-1785 du 29 décembre 2015 ; elle est historique et ne fixe aucune entrée en vigueur future.")

add('286 K', '''
La personne qui souhaite obtenir la qualité d'entrepositaire agréé adresse sa demande au directeur interrégional des douanes et droits indirects dans le ressort territorial duquel se situent le ou les entrepôts fiscaux suspensifs des droits d'accises concernés. Si elle choisit de tenir la comptabilité matières de tous ses entrepôts en un lieu unique, elle adresse sa demande au directeur dans le ressort duquel se situe l'entrepôt fiscal suspensif des droits d'accises choisi à cette fin.
Elle joint à sa demande un modèle de sa comptabilité matières et, sauf dispense, toute pièce justifiant l'existence de la caution prévue au V de l'article 302 G du code général des impôts.
Si l'entrepositaire agréé tient la comptabilité matières de chacun de ses entrepôts suspensifs des droits d'accises à l'adresse d'un de ces entrepôts, il précise également dans sa demande l'adresse de l'entrepôt où ces comptabilités sont tenues.
Le directeur interrégional des douanes et droits indirects accorde la qualité d'entrepositaire agréé et attribue à l'intéressé un numéro d'identification, le cas échéant par entrepôt suspensif des droits d'accises.
Les personnes qui avaient le statut de marchand en gros au 31 décembre 1999 ou étaient inscrites à cette date dans le casier viticole informatisé constitué en application du règlement (CEE) n° 2392/86 du Conseil du 24 juillet 1986 sont réputées satisfaire aux obligations du III de l'article 302 G du code général des impôts. Elles ont, de ce fait, la qualité d'entrepositaire agréé à compter du 1er janvier 2000, sans démarche préalable. Le directeur interrégional des douanes et droits indirects leur notifie leur numéro d'identification.
''', "À droit constant, le destinataire de la demande, les pièces jointes et les modalités d'attribution sont rendus explicites. La reconnaissance historique de la qualité d'entrepositaire agréé est réécrite intégralement et conservée. Aucune réforme de fond n'est introduite.", "Les cinq alinéas sont maintenus. La dispense ne concerne que la justification de la caution. Les dates du 31 décembre 1999 et du 1er janvier 2000 et le règlement (CEE) n° 2392/86 du 24 juillet 1986 restent des paramètres du régime historique. Le V de l'article 302 G du corpus prévoit bien la caution et ses dispenses ; ses III et V sont conservés dans les renvois. Cet article porte un statut d'abrogation différée dont les conditions sont renvoyées par sa note à l'article 38 de l'ordonnance n° 2021-1843 du 22 décembre 2021 : sa borne technique 2222-02-22 n'est pas une date de réforme.")

add('286 L', '''
Dans un entrepôt suspensif de droits d'accises, les alcools, les produits intermédiaires, les produits mentionnés à l'article 438 du code général des impôts et les bières détenus en droits acquittés doivent être stockés séparément des mêmes produits détenus en suspension de droits.
''', "Réécriture à droit constant : le lieu et l'obligation de séparation des stocks sont énoncés directement. Toutes les catégories de produits sont maintenues, sans réforme de fond.", "La séparation vise les mêmes produits selon leur statut fiscal, droits acquittés ou suspension de droits. Le renvoi à l'article 438 est conservé ; cet article est absent du corpus public fourni et nécessite un contrôle de coordination.")

add('286 M', '''
En application du IV de l'article 302 G du code général des impôts, l'entrepositaire agréé demande la compensation ou le remboursement des droits acquittés ou supportés au service des douanes et droits indirects dans le ressort territorial duquel se situe l'entrepôt suspensif de droits d'accises où il détient les produits concernés.
L'entrepositaire agréé demande la compensation sur la déclaration de liquidation des droits visée au III de l'article 302 D du code général des impôts.
Il demande le remboursement lorsqu'il ne peut réaliser la compensation des droits au cours des trois mois suivant la demande.
Le directeur interrégional des douanes et droits indirects statue sur ces demandes de compensation ou de remboursement des droits acquittés ou supportés.
''', "À droit constant, l'entrepositaire agréé est le sujet des démarches et la compétence de décision est formulée directement. L'ordre entre compensation et remboursement et les quatre alinéas sont conservés, sans réforme de fond.", "Le délai de trois mois suivant la demande est conservé. Le III de l'article 302 D est absent du corpus ; le IV de l'article 302 G y prévoit toujours une compensation ou un remboursement, sans que sa borne technique 2222-02-22 vaille date de réforme. Les renvois sont maintenus et appellent un contrôle de consolidation.")

long_text = '\n'.join((fragments / name).read_text().strip() for name in (
    '286_J_I_IV.txt', '286_J_V_VIII.txt', '286_J_IX_XI.txt'
))
add('286 J', long_text,
    "Réécriture intégrale à droit constant, assemblée à partir de trois fragments : les options de tenue comptable, les conditions d'agrément, les balances et inventaires, les unités de suivi et toutes les rubriques d'entrées et de sorties sont reformulés avec des sujets explicites. Les onze subdivisions, lettres, numéros et alinéas, y compris les mentions abrogées ou sans objet, sont conservés. Aucune réforme de fond n'est appliquée.",
    "Contrôles particuliers : balance et déclaration ordinaires au dixième jour du mois ; déclaration des produits de l'article 575 A au quinzième jour ; inventaire annuel à la clôture et transmission au dixième jour du deuxième mois suivant ; écritures au plus tard le jour ouvrable suivant l'opération. Les deux comptes de production et de transformation, le régime des fabricants de bières, les fûts sans revêtement d'étanchéité, la séparation des statuts fiscaux et toutes les unités de mesure sont maintenus. Les renvois internes, notamment au troisième alinéa du 1° du IV, gardent leur cible. Les articles 302 B, 302 D, 338, 438, 450, 575 A, 302 M, 302 M bis, 302 M ter et 614 du CGI sont absents du corpus fourni ; les renvois sont conservés et nécessitent un contrôle d'actualité. Les articles 277 A et 302 G y portent un statut d'abrogation différée avec une borne technique 2222-02-22, sans valeur de date de réforme. Le règlement (CE) n° 436/2009 et les articles 661 et 662 du code rural ancien restent les références de la source ; leur actualité nécessite contrôle sans remplacement conjectural. La note source relative à l'article 81-I-9° de la loi n° 2015-1785 du 29 décembre 2015 est historique et ne vaut pas date d'entrée en vigueur future.")

assert len(sources) == 24
assert len(drafts) == 24
answer = []
for source in sources:
    xml, reason, notes = drafts[source['number']]
    item = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    item.update(proposed_xml=xml, reason=reason, review_notes=notes, status='rewrite_draft')
    answer.append(item)
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
