import json
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
drafts = {}


def add(number, xml, reason, notes):
    assert number not in drafts
    drafts[number] = {
        'proposed_xml': xml.strip(),
        'reason': reason,
        'review_notes': notes,
        'status': 'rewrite_draft',
    }


electronic_dates = (
    "La note source renvoie à l'article 3 du décret n° 2022-1299 du 7 octobre 2022, "
    "modifié par l'article 2 du décret n° 2024-266 du 25 mars 2024 : pour les opérations "
    "de l'article 289 bis du CGI, application aux factures émises à compter du 1er septembre 2026, "
    "reportée au 1er septembre 2027 pour les microentreprises et PME visées aux deuxième et troisième "
    "alinéas du A du III de l'article 26 de la loi n° 2022-1157 du 16 août 2022 qui ne sont pas membres "
    "d'un assujetti unique de l'article 256 C. Pour les opérations des articles 290 et 290 A, "
    "application aux factures émises ou, à défaut, aux opérations réalisées à compter du 1er septembre 2026, "
    "avec report au 1er septembre 2027 pour les catégories d'entreprises désignées par la note. "
    "Ces dates historiques d'application ne fixent pas l'entrée en vigueur de la présente proposition. "
)

transport_coordination = (
    "Décalage temporel préexistant à contrôler : la source continue de viser l'article 298 sexies du CGI, "
    "alors que le corpus local signale, dans la note de cet article, son abrogation "
    "au 1er septembre 2026 par les articles 9 (27°), 15 et 49 de l'ordonnance n° 2025-1247 du 17 décembre 2025, "
    "sous réserve du maintien transitoire de ses V bis et V ter jusqu'à leur reprise réglementaire. "
    "Le renvoi de la source est conservé ; sa coordination avec cette recodification doit être contrôlée, "
    "sans attribuer un numéro de remplacement non établi par le corpus consulté. "
)

add('242 nonies J', '''
<p>Les factures électroniques mentionnées à l'article 289 bis du code général des impôts présentent sous une forme structurée les données à transmettre à l'administration. Ces données sont sélectionnées parmi les mentions obligatoires prévues au I de l'article 242 nonies A, aux articles L. 441-9, R. 123-237 et R. 123-238 du code de commerce et à l'article L. 541-10 du code de l'environnement. Elles excluent la dénomination précise du bien livré ou du service rendu, conformément aux obligations des personnes dépositaires du secret professionnel prévues à l'article 226-13 du code pénal. Un arrêté du ministre chargé du budget précise la liste de ces données, dont le nombre varie selon les normes de formats.</p>
''',
    "À droit constant, la phrase initiale est divisée pour distinguer la présentation structurée, les textes qui déterminent les mentions, l'exclusion de la dénomination précise et le rôle de l'arrêté. Aucune réforme de fond n'est appliquée au champ des données ni au secret professionnel.",
    electronic_dates + "Tous les renvois et l'exclusion de la dénomination précise sont conservés. La liste et le nombre de données restent du ressort de l'arrêté et des normes de formats ; aucune liste nouvelle n'est créée.")

add('242 nonies K', '''
<p>Pour mettre en œuvre les 4°, 5° et 7° de l'article 242 nonies E, les plateformes agréées contrôlent la conformité des données de facturation. Un arrêté du ministre chargé du budget précise ces contrôles.</p>
''',
    "À droit constant, l'obligation de contrôle est formulée directement et la compétence du ministre pour en préciser le contenu fait l'objet d'une phrase distincte. Aucune réforme de fond.",
    "Les renvois aux 4°, 5° et 7° de l'article 242 nonies E ont été vérifiés dans le corpus local et sont maintenus. Le 2° de cet article E renvoie lui-même aux contrôles du présent article ; aucune renumérotation ni modification des services concernés.")

add('242 nonies L', '''
<p>La plateforme agréée de l'émetteur transmet les données de facturation à l'administration dans un délai de vingt-quatre heures à compter du dépôt de la facture électronique sur cette plateforme. Un arrêté du ministre chargé du budget fixe les conditions de cette transmission.</p>
''',
    "À droit constant, la plateforme de l'émetteur devient le sujet explicite de l'obligation ; le point de départ du délai et le rôle de l'arrêté sont séparés. Aucune réforme de fond ni modification du délai.",
    electronic_dates + "Le délai de vingt-quatre heures court du dépôt sur la plateforme de l'émetteur, et non de la date d'émission ou de réception par le destinataire.")

add('242 nonies M', '''
<p>I. - Pour les transactions mentionnées aux I et II de l'article 290 du code général des impôts réalisées avec des personnes non assujetties, l'assujetti transmet les données suivantes :</p>
<p>1° Son numéro d'identification mentionné au 1° du I de l'article 242 nonies A ;</p>
<p>2° La période au titre de laquelle il effectue la transmission ;</p>
<p>3° La mention « option pour le paiement de la taxe d'après les débits », lorsqu'il y a lieu ;</p>
<p>4° La catégorie de transaction :</p>
<p>a) Livraisons de biens soumises à la taxe sur la valeur ajoutée ;</p>
<p>b) Prestations de services soumises à la taxe sur la valeur ajoutée ;</p>
<p>c) Livraisons de biens et prestations de services réalisées par des assujettis établis en France et qui, en application du 1° du I de l'article 258 A et de l'article 259 B du code général des impôts, ne sont pas situées en France ;</p>
<p>d) Opérations auxquelles s'appliquent les régimes prévus au e du 1 de l'article 266 et aux articles 268 et 297 A du même code ;</p>
<p>5° Pour chaque taux d'imposition, la base d'imposition totale hors taxe et le montant de la taxe correspondante ;</p>
<p>6° Le montant total de la taxe due en France en application des articles 258 à 259 D du même code. Pour les transactions établies en devise étrangère, ce montant est exprimé en euros ;</p>
<p>7° La devise ;</p>
<p>8° La date des transactions.</p>
<p>II. - Pour les transactions mentionnées aux I et II de l'article 290 du code général des impôts autres que celles réalisées avec des personnes non assujetties, l'assujetti transmet les données mentionnées à l'article 242 nonies J. En l'absence du numéro d'identification prévu au 1° du I de l'article 242 nonies A, la facture comporte un identifiant défini par arrêté du ministre chargé du budget.</p>
<p>III. - Un arrêté du ministre chargé du budget définit le format et les modalités de transmission des données mentionnées aux I et II.</p>
''',
    "À droit constant, l'assujetti est nommé comme débiteur de la transmission. Les catégories, l'option d'après les débits et la conversion en euros sont rendues plus lisibles sans fusionner les I et II. Les subdivisions et leur ordre sont conservés ; aucune réforme de fond.",
    electronic_dates + "Conservation des huit données du I, des quatre catégories du 4° et de tous les renvois. La conversion en euros du 6° ne remplace pas la donnée distincte relative à la devise du 7°. L'identifiant de substitution du II reste défini par arrêté ; aucune identification nouvelle n'est inventée.")

add('242 nonies N', '''
<p>Les plateformes agréées contrôlent la conformité des données de transaction mentionnées à l'article 242 nonies M lors de leur transmission. Un arrêté du ministre chargé du budget précise ces contrôles.</p>
''',
    "À droit constant, les plateformes sont placées en sujet et la détermination des contrôles par arrêté est isolée. Aucune réforme de fond.",
    "Le contrôle reste attaché à la transmission des seules données de transaction de l'article 242 nonies M. Il n'est pas assimilé au contrôle de complétude des données de paiement de l'article 242 nonies P.")

add('242 nonies O', '''
<p>L'assujetti communique les données mentionnées à l'article 242 nonies M, conformément au III de l'article 290 du code général des impôts, selon la fréquence suivante :</p>
<p>1° Trois transmissions par mois lorsqu'il est soumis au régime réel normal mensuel d'imposition prévu au 2 de l'article 287 du même code ;</p>
<p>2° Une transmission par mois lorsqu'il est soumis au régime réel normal trimestriel d'imposition prévu au 2 de l'article 287 du même code ;</p>
<p>3° Une transmission par mois lorsqu'il est soumis aux régimes simplifiés d'imposition prévus au 1° du I de l'article 298 bis et à l'article 302 septies A du même code ;</p>
<p>4° Une transmission tous les bimestres civils lorsqu'il bénéficie de la franchise en base prévue à l'article 293 B du même code ou du régime de remboursement forfaitaire prévu aux articles 298 quater et 298 quinquies de ce code.</p>
<p>Le nombre et la fréquence des transmissions s'apprécient séparément pour chacune des plateformes agréées choisies par l'assujetti.</p>
<p>L'assujetti n'est tenu à aucune transmission en l'absence de transactions mentionnées aux I et II de l'article 290 du code général des impôts.</p>
<p>Un arrêté du ministre chargé du budget fixe les échéances de ces transmissions.</p>
''',
    "À droit constant, chaque fréquence est placée au début du cas correspondant et l'absence de transmission en l'absence de transactions est énoncée directement. Les quatre régimes, l'appréciation par plateforme et l'arrêté d'échéances sont conservés. Aucune réforme de fond.",
    electronic_dates + "Les fréquences restent respectivement trois par mois, une par mois, une par mois et une par bimestre civil. Le régime réel normal trimestriel n'entraîne donc pas une transmission trimestrielle. L'exemption en l'absence de transactions n'est pas étendue aux données de paiement de l'article 242 nonies P.")

add('242 nonies P', '''
<p>I. - Pour l'application de l'article 290 A du code général des impôts, les données de paiement à transmettre sont les suivantes :</p>
<p>1° Le numéro d'identification mentionné au 1° du I de l'article 242 nonies A ;</p>
<p>2° La période au titre de laquelle la transmission est effectuée ou, pour les opérations donnant lieu à une facture électronique, la date de cette facture ;</p>
<p>3° La date de l'encaissement effectif ;</p>
<p>4° Le montant encaissé en euros, ventilé par taux d'imposition de la taxe sur la valeur ajoutée ;</p>
<p>5° Pour les opérations donnant lieu à une facture, le numéro de cette facture.</p>
<p>Un arrêté du ministre chargé du budget définit les modalités de transmission de ces données.</p>
<p>II. - Lors de la transmission des données de paiement, les plateformes agréées vérifient que toutes les données attendues sont présentes sous une forme structurée.</p>
<p>III. - L'assujetti communique les données mentionnées au I selon la fréquence suivante :</p>
<p>1° Une transmission par mois lorsqu'il est soumis aux régimes d'imposition prévus au 2 de l'article 287, au 1° du I de l'article 298 bis ou à l'article 302 septies A du code général des impôts ;</p>
<p>2° Une transmission tous les bimestres civils lorsqu'il bénéficie de la franchise en base prévue à l'article 293 B du même code ou du régime de remboursement forfaitaire prévu aux articles 298 quater et 298 quinquies de ce code.</p>
<p>Le nombre et la fréquence des transmissions s'apprécient séparément pour chacune des plateformes agréées choisies par l'assujetti.</p>
<p>Un arrêté du ministre chargé du budget fixe les échéances de ces transmissions.</p>
''',
    "À droit constant, le contrôle de complétude est exprimé en termes directs et les fréquences sont placées au début de chaque cas. Les cinq données, la ventilation par taux et les trois subdivisions sont préservées. Aucune réforme de fond.",
    electronic_dates + "La date de facture ne remplace la période qu'en présence d'une facture électronique ; le numéro de facture est exigé pour toute opération donnant lieu à facture. Encaissement effectif, expression en euros, transmission mensuelle ou par bimestre civil et appréciation par plateforme sont conservés. Aucune dispense pour absence de transactions n'est ajoutée.")

add('242 decies', '''
<p>Les personnes mentionnées au 2° du I de l'article 256 bis du code général des impôts informent par écrit et sans délai le service des impôts dès qu'elles ne peuvent plus bénéficier du régime dérogatoire prévu à ce 2°. Elles s'adressent au service auprès duquel elles déposent leur déclaration de bénéfices ou, à défaut, à celui dont relève leur principal établissement.</p>
<p>Elles remplissent également un document conforme au modèle fourni par l'administration. Elles sont dispensées de ce document si elles ont déjà satisfait à l'obligation de déclaration d'existence prévue au 1° du I de l'article 286 du code général des impôts et détiennent le numéro d'identification de leur établissement délivré par l'INSEE.</p>
<p>Le service des impôts leur attribue un numéro individuel d'identification conformément au 2° de l'article 286 ter du code général des impôts.</p>
''',
    "À droit constant, le destinataire de l'information est précisé dans une phrase distincte et les deux conditions cumulatives de dispense du document sont regroupées. Les trois alinéas de fond sont conservés sous forme de paragraphes. Aucune réforme de fond.",
    "Conservation de l'écrit, de l'exigence d'agir sans délai et du service subsidiaire du principal établissement. La dispense concerne seulement le document complémentaire, et suppose à la fois la déclaration d'existence et le numéro d'établissement INSEE ; elle ne dispense pas d'informer le service. Ce numéro reste distinct du numéro individuel attribué au titre de l'article 286 ter.")

add('242 undecies', '''
<p>Les assujettis désignés au II de l'article 298 sexies du code général des impôts font figurer les éléments suivants sur les factures qu'ils délivrent :</p>
<p>1° Le nom et l'adresse de l'assujetti qui effectue la livraison ;</p>
<p>2° Le nom et l'adresse de l'acquéreur, ainsi que le nom de l'Etat membre vers lequel le moyen de transport neuf est expédié ou transporté ;</p>
<p>3° Les éléments d'identification complète du moyen de transport :</p>
<p>a) Sa nature ;</p>
<p>b) Son genre ;</p>
<p>c) Sa marque ;</p>
<p>d) Son type ;</p>
<p>e) Son numéro dans la série du type ;</p>
<p>f) Pour un véhicule terrestre, sa cylindrée ou sa puissance ;</p>
<p>g) Pour un aéronef, son poids total au décollage ;</p>
<p>h) Pour un bateau, sa longueur, sa vitesse maximale et, le cas échéant, la puissance de son ou de ses moteurs ;</p>
<p>i) Sa date de première mise en circulation ou, pour les bateaux, la date du permis de navigation ou, pour les aéronefs, la date de délivrance du premier certificat de navigabilité ou du certificat de navigabilité export ;</p>
<p>j) Son numéro ou sa marque d'immatriculation ;</p>
<p>4° La date de la livraison ;</p>
<p>5° Entre la date de première mise en circulation et celle de la livraison, la distance parcourue pour les véhicules terrestres, le nombre d'heures de vol effectuées pour les aéronefs ou le nombre d'heures de navigation effectuées pour les bateaux. Lorsque le moyen de transport n'a pas déjà été mis en circulation, une mention indique qu'il n'a fait l'objet d'aucune utilisation ;</p>
<p>6° Le prix de vente hors taxe sur la valeur ajoutée ;</p>
<p>7° La mention : « exonération de la taxe sur la valeur ajoutée, art. 298 sexies du code général des impôts ».</p>
''',
    "À droit constant, les caractéristiques sont rattachées explicitement au moyen de transport et les données propres à chaque catégorie de véhicule sont placées en tête des items concernés. Les sept rubriques et les lettres a à j sont maintenues. Aucune réforme de fond.",
    transport_coordination + "Le renvoi au II de l'article 298 sexies et la mention d'exonération obligatoire sont conservés, y compris le numéro d'article dans cette mention. Les alternatives du i, l'absence d'utilisation du 5° et les caractéristiques techniques ne sont ni réduites ni fusionnées.")

add('242 duodecies', '''
<p>Pour obtenir le remboursement de la taxe sur la valeur ajoutée qu'ils ont acquittée lors de l'achat, de l'importation ou de l'acquisition intracommunautaire du moyen de transport, les assujettis visés au IV de l'article 298 sexies du code général des impôts établissent une demande sur un imprimé dont le modèle est fixé par l'administration.</p>
<p>Le demandeur établit que le moyen de transport est affecté aux besoins d'un résident d'un autre Etat membre.</p>
<p>Il dépose sa demande auprès du service des impôts dans le ressort duquel se situe le siège de son activité ou, à défaut, son domicile.</p>
<p>Le remboursement est subordonné à la production, à l'appui de la demande, des pièces suivantes :</p>
<p>a) Le document justifiant que le demandeur a précédemment acquitté la taxe sur la valeur ajoutée sur le moyen de transport neuf qu'il vend : facture d'achat, déclaration d'importation ou document en tenant lieu, ou certificat délivré par l'administration des impôts dans les conditions prévues à l'article 242 quaterdecies ;</p>
<p>b) La facture de vente établie par le demandeur conformément à l'article 242 undecies ;</p>
<p>c) L'original ou une copie certifiée du document correspondant au moyen de transport :</p>
<p>Pour les véhicules terrestres à moteur, le certificat d'immatriculation annoté conformément à la réglementation applicable en matière d'immatriculation ;</p>
<p>Pour les aéronefs et les bateaux destinés à la navigation intérieure, le certificat de radiation de l'immatriculation ;</p>
<p>Pour les autres bateaux, le certificat de radiation de la francisation.</p>
''',
    "À droit constant, la demande et son dépôt sont formulés avec un sujet explicite. Les justificatifs du c sont présentés par catégorie de moyen de transport, dans l'ordre de la source. La condition d'affectation et la condition de production des pièces sont préservées. Aucune réforme de fond.",
    transport_coordination + "Le champ du IV de l'article 298 sexies, les trois origines de la taxe remboursable, la priorité du siège de l'activité sur le domicile, les renvois aux articles 242 quaterdecies et 242 undecies, ainsi que l'alternative entre original et copie certifiée sont conservés. La référence historique à la francisation n'est pas modernisée sans coordination.")

add('242 terdecies', '''
<p>I. - Toute personne qui acquiert, en provenance d'un autre Etat membre de l'Union européenne, un moyen de transport mentionné au 1 du III de l'article 298 sexies du code général des impôts demande à l'administration fiscale dont elle relève le certificat fiscal prévu au V bis du même article.</p>
<p>La présentation de ce certificat est obligatoire pour obtenir l'immatriculation ou la francisation d'un moyen de transport mentionné au premier alinéa et provenant d'un autre Etat membre de l'Union européenne.</p>
<p>Lorsqu'un véhicule terrestre à moteur d'occasion est acquis auprès d'un assujetti revendeur qui a appliqué à la revente le régime prévu à l'article 297 A du code général des impôts, cet assujetti revendeur demande le certificat. Toutefois, si l'opération a été réalisée par l'intermédiaire d'un mandataire agissant au nom et pour le compte de l'acquéreur du véhicule, ce mandataire demande le certificat à sa place.</p>
<p>II. - Pour les moyens de transport qui ne sont pas soumis à immatriculation, l'utilisateur conserve ce certificat afin de le présenter à toute demande de l'administration.</p>
''',
    "À droit constant, l'obligation générale de demander le certificat, son usage et la personne chargée de le demander en cas de revente sont distingués. Le cas du mandataire est isolé dans le même alinéa. Aucune réforme de fond.",
    transport_coordination + "Le V bis demeure transitoirement en vigueur selon la note de l'article 298 sexies ; le corpus désigne l'article L. 171-1 du code des impositions sur les biens et services pour sa reprise réglementaire. La définition du 1 du III appelle une coordination distincte. Les trois alinéas du I sont conservés, notamment le dernier auquel renvoie le 4° de l'article 242 quaterdecies. La condition d'application effective de l'article 297 A et l'action du mandataire au nom et pour le compte de l'acquéreur sont maintenues.")

add('242 quaterdecies', '''
<p>Pour l'application de l'article 242 terdecies :</p>
<p>1° L'assujetti et la personne morale non assujettie, autres qu'une personne bénéficiant du régime dérogatoire prévu au 2° du I de l'article 256 bis du code général des impôts, indiquent sur le certificat fiscal mentionné au I de l'article 242 terdecies, selon leur situation, que la taxe sera acquittée sur leur déclaration de chiffre d'affaires, qu'elle a déjà été acquittée ou que l'acquisition intracommunautaire n'est pas taxable. L'administration vise ce certificat après mise en œuvre des dispositions de l'article 242 quindecies ;</p>
<p>2° Les personnes mentionnées au 1° joignent à la déclaration de chiffre d'affaires prévue à l'article 287 du code général des impôts un relevé détaillé sur papier libre. Ce relevé indique, pour la période couverte par la déclaration :</p>
<p>a) L'identification, le prix et la date de chacune des acquisitions intracommunautaires de moyens de transport taxables en application du 1° du I de l'article 256 bis du code général des impôts ;</p>
<p>b) L'identification, le prix et la date de chacune des acquisitions intracommunautaires de moyens de transport non taxables en application du 2° bis du I du même article ;</p>
<p>c) L'identification, le prix et la date de chacune des acquisitions de moyens de transport en provenance d'un autre Etat membre de l'Union européenne qui ne relèvent d'aucune des deux catégories précédentes ;</p>
<p>3° Les personnes autres que celles mentionnées au 1° indiquent sur le certificat fiscal mentionné au I de l'article 242 terdecies, selon leur situation, que la taxe sur la valeur ajoutée exigible a été acquittée ou qu'aucune taxe n'est due au titre de l'opération au vu des renseignements communiqués.</p>
<p>4° L'assujetti revendeur ou, selon le cas, le mandataire mentionné au dernier alinéa du I de l'article 242 terdecies joint à sa demande de certificat fiscal :</p>
<p>a) Une copie du certificat définitif d'immatriculation délivré à l'étranger, lorsque le véhicule y a fait l'objet de cette formalité ;</p>
<p>b) Une copie de la facture d'achat du véhicule remise à l'assujetti revendeur ;</p>
<p>c) Lorsque l'assujetti revendeur n'a pas acquis le véhicule directement auprès du titulaire du certificat d'immatriculation, une copie de la facture de vente du véhicule par ce titulaire indiquant que la vente n'a pas été soumise à la taxe sur la valeur ajoutée. A défaut de cette copie, l'assujetti revendeur ou le mandataire joint une attestation signée par ce titulaire. L'attestation mentionne les nom et prénom ou la raison sociale du titulaire, son adresse, son numéro individuel d'identification à la taxe sur la valeur ajoutée, le numéro et la date d'émission de la facture de vente, les nom et prénom ou la raison sociale et l'adresse de l'acquéreur, ainsi que les caractéristiques du véhicule. Elle indique que le titulaire du certificat d'immatriculation n'a pas soumis cette vente à la taxe sur la valeur ajoutée ou, le cas échéant, qu'il n'est pas un assujetti à cette taxe. Si l'attestation est rédigée dans une autre langue que le français, une traduction certifiée y est jointe.</p>
<p>L'administration peut demander les originaux des documents mentionnés aux a et b. Elle les restitue ensuite au demandeur. Le défaut de production de ces originaux constitue un motif de refus de délivrance du certificat fiscal.</p>
''',
    "À droit constant, les trois situations fiscales du 1° et les informations du relevé du 2° sont exposées directement. Le long c du 4° est divisé en phrases sans changer d'alinéa ni omettre une mention de l'attestation. Aucune réforme de fond et aucun allègement des justificatifs de la chaîne de vente.",
    "Les quatre numéros et leurs lettres sont conservés. Le renvoi au dernier alinéa du I de l'article 242 terdecies reste exact. L'exclusion du régime dérogatoire, le visa subordonné à l'article 242 quindecies, le papier libre, la traduction certifiée et la restitution des originaux sont maintenus. La demande d'originaux reste limitée aux a et b du 4°. Le régime du certificat dépend du V bis de l'article 298 sexies, maintenu transitoirement selon le corpus jusqu'à la reprise réglementaire visée à l'article L. 171-1 du code des impositions sur les biens et services ; coordination à contrôler sans remplacer ici les renvois.")

add('242 quindecies', '''
<p>I. - Pour l'application du premier alinéa du V bis de l'article 298 sexies du code général des impôts, le service des impôts dont relève l'assujetti ou la personne morale non assujettie fixe le montant de la caution exigée.</p>
<p>II. - La dispense de caution prévue au deuxième alinéa du V bis de l'article 298 sexies du code général des impôts est accordée pour une période de trois mois, renouvelable par tacite reconduction. Si, au cours de cette période ou à son terme, l'administration constate que le demandeur ne présente plus de garanties suffisantes de solvabilité, elle retire la dispense. Elle motive sa décision et la notifie au demandeur.</p>
''',
    "À droit constant, l'autorité qui fixe la caution est exprimée directement. Le renouvellement et le retrait de la dispense sont présentés en phrases distinctes, avec maintien de la motivation et de la notification. Aucune réforme de fond.",
    "Conservation des renvois distincts aux premier et deuxième alinéas du V bis de l'article 298 sexies, de la période de trois mois et du contrôle possible au cours de cette période comme à son terme. Le V bis est maintenu transitoirement selon sa note dans le corpus, jusqu'à la reprise réglementaire visée à l'article L. 171-1 du code des impositions sur les biens et services. La décision demeure soumise aux garanties suffisantes de solvabilité ; aucune dispense définitive n'est créée.")

add('242 sexdecies', '''
<p>Lorsque l'administration le lui demande, l'assujetti revendeur d'un véhicule terrestre à moteur d'occasion lui fournit une copie des documents mentionnés au 4° de l'article 242 quaterdecies.</p>
''',
    "À droit constant, le déclenchement sur demande de l'administration est placé en tête et le verbe d'obligation est simplifié. Aucune réforme de fond.",
    "Le champ reste limité à l'assujetti revendeur et aux véhicules terrestres à moteur d'occasion. Le renvoi porte sur l'ensemble du 4° de l'article 242 quaterdecies, et non sur ses seuls a et b ; seules des copies sont exigées par le présent article.")

add('242 septdecies', '''
<p>I. - La personne qui sollicite l'accréditation pour l'activité de représentation fiscale mentionnée à l'article 289 A du code général des impôts dépose sa demande auprès du service des impôts dont elle relève. Elle la transmet par voie électronique ou, si elle choisit la voie postale, par lettre recommandée avec demande d'avis de réception.</p>
<p>II. - Une accréditation est demandée pour chaque assujetti représenté. La demande est accompagnée des pièces suivantes :</p>
<p>1° Le numéro unique d'identification du représentant qui demande l'accréditation ;</p>
<p>2° Un descriptif de son organisation administrative et des moyens humains et matériels dont il dispose pour exercer son activité de représentation ;</p>
<p>3° Un bulletin n° 3 du casier judiciaire du demandeur ou, s'il est une personne morale, de ses représentants légaux. Ce bulletin doit dater de moins de trois mois ;</p>
<p>4° Les justificatifs de sa solvabilité financière ou d'une garantie financière prévue au 3° du A du IV de l'article 289 A du code général des impôts.</p>
<p>Pour permettre l'appréciation de sa solvabilité financière au regard de ses obligations de représentant fiscal, le demandeur présente ses comptes annuels ou d'autres informations financières disponibles. Cette appréciation tient compte des activités de l'assujetti représenté et, le cas échéant, des autres engagements de représentation du demandeur.</p>
<p>Si, après examen, le service des impôts estime les justifications de solvabilité financière insuffisantes, le demandeur transmet dans un délai de 30 jours la garantie financière prévue au 3° du A du IV de l'article 289 A du code général des impôts ;</p>
<p>5° Le nom ou la dénomination sociale de l'assujetti représenté, l'adresse de son domicile ou de son siège social, le lieu de ses activités, son adresse électronique et une description des activités au titre desquelles il réalise en France des opérations justifiant la désignation d'un représentant fiscal ;</p>
<p>6° Un document par lequel le demandeur s'engage à remplir les formalités et obligations fiscales de la personne représentée et à acquitter la taxe due par celle-ci, conformément au I de l'article 289 A du code général des impôts ;</p>
<p>7° Un document par lequel la personne représentée désigne le demandeur comme représentant fiscal au sens de l'article 289 A du code général des impôts.</p>
<p>Pour instruire la demande, le service des impôts réutilise les informations et pièces mentionnées aux 1° à 4° qu'il détient légalement, dès lors qu'elles sont encore valables, à jour et adaptées à cette demande, notamment aux obligations de représentation à garantir. Lorsque ces conditions sont remplies, il ne demande pas leur production à nouveau. Le demandeur peut faire rectifier les informations inexactes. Cette réutilisation respecte les secrets protégés par la loi et n'étend pas les droits d'accès ou de communication de l'administration.</p>
''',
    "À droit constant, la procédure de dépôt, la liste des pièces et l'examen de solvabilité sont reformulés avec des sujets explicites. Réforme de fond limitée à la mesure « Déclarer une fois, corriger à la source » de policy.json : un dernier alinéa du II impose le réemploi des pièces communes des 1° à 4° déjà légalement détenues, valables et adaptées à la demande, interdit leur demande en double et permet leur rectification. Les pièces propres à chaque représentation et les conditions de fond de l'accréditation restent exigées.",
    "Les I et II, les 1° à 7° et les alinéas intercalés du 4° sont conservés dans leur ordre ; la disposition nouvelle est ajoutée après le 7°. Coordination explicite de l'article 242 octodecies pour les demandes incomplètes. Le réemploi ne dispense ni de l'accréditation par assujetti, ni du bulletin n° 3 datant de moins de trois mois, ni de l'appréciation des activités et des autres engagements, ni d'une garantie adaptée à ceux-ci. Le délai de 30 jours est conservé ; son point de départ, non précisé par la source, n'est pas inventé. Les modalités de rectification et de réemploi doivent respecter les règles applicables aux données personnelles et au casier judiciaire, sans nouvel accès, nouveau fichier ou durée de conservation créée ici. La note source rattache la modification antérieure à l'article 112-I E 1° de la loi n° 2023-1322 du 29 décembre 2023 ; cette date ne fixe pas celle de la réforme proposée. La note de l'article 289 A dans le corpus annonce sa recodification au 1er janvier 2027, avec maintien transitoire des 1° et 3° du A du IV jusqu'aux reprises réglementaires visées au 4° de l'article L. 152-4 et à l'article L. 152-6 du code des impositions sur les biens et services : coordonner cette disposition et l'article 242 octodecies avec cette reprise hors des cinq codes.")

add('242 octodecies', '''
<p>Lorsque la demande est incomplète, compte tenu de la réutilisation des informations et pièces prévue au dernier alinéa du II de l'article 242 septdecies, l'administration fiscale invite la personne qui sollicite l'accréditation à la compléter. Cette personne dispose d'un mois à compter de la réception de la demande de compléments adressée par l'administration.</p>
''',
    "À droit constant, l'invitation et le délai de réponse sont séparés en deux phrases. Réforme de fond par coordination avec le dernier alinéa du II proposé à l'article 242 septdecies : le caractère incomplet du dossier s'apprécie en tenant compte des pièces réutilisables, afin de ne pas les réclamer en double.",
    "Le délai reste d'un mois à compter de la réception par le demandeur de la demande de compléments, sans assimilation à trente jours. Le nouveau renvoi vise exactement l'alinéa ajouté à l'article 242 septdecies ; les deux propositions doivent être adoptées ensemble. Aucun mécanisme de rejet automatique ou de décision tacite n'est ajouté. La coordination de l'accréditation avec la recodification de l'article 289 A du CGI signalée au 1er janvier 2027 reste à effectuer, notamment avec les reprises réglementaires visées au 4° de l'article L. 152-4 et à l'article L. 152-6 du code des impositions sur les biens et services.")

add('242 novodecies', '''
<p>L'accréditation mentionnée à l'article 289 A du code général des impôts est retirée dans les cas suivants :</p>
<p>1° A la demande du représentant fiscal ou de l'assujetti représenté. Le retrait prend effet dès que le service des impôts dont relève le représentant reçoit la demande. Si celle-ci émane du représentant fiscal, le service informe l'assujetti représenté par courrier électronique ;</p>
<p>2° A l'initiative de l'administration fiscale, dans les cas mentionnés au B du IV de l'article 289 A du code général des impôts.</p>
<p>Dans le cas prévu au 2°, le service des impôts informe préalablement le représentant fiscal de son intention de retirer l'accréditation et des motifs du retrait envisagé. Il lui indique qu'il dispose de trente jours pour présenter ses observations ou, le cas échéant, régulariser sa situation. Le service lui notifie le retrait par lettre recommandée avec demande d'avis de réception. Le retrait prend effet à la date de réception de cette lettre. Le service informe également l'assujetti représenté par courrier électronique de la perte d'accréditation de son représentant fiscal.</p>
''',
    "À droit constant, les deux procédures de retrait sont distinguées et les étapes du retrait à l'initiative de l'administration sont présentées dans des phrases successives. Les effets à réception et les informations électroniques sont conservés. Aucune réforme de fond.",
    "Conservation du droit d'observations ou de régularisation de trente jours et de la lettre recommandée avec avis de réception. La source ne fixe pas expressément le point de départ de ces trente jours ; aucun point de départ nouveau n'est ajouté. Selon la note source, pour les accréditations demandées avant l'entrée en vigueur du décret n° 2022-589 du 20 avril 2022, le respect de la condition du 3° du A du IV de l'article 289 A n'est vérifié, pour le 2° du présent article, qu'à compter du 1er janvier 2024. Cette règle historique n'est pas supprimée ni transformée en transition de réforme. Le renvoi au B du IV de l'article 289 A est conservé malgré la recodification annoncée par sa note au 1er janvier 2027 ; coordonner la procédure réglementaire de retrait dans le code des impositions sur les biens et services, sans inventer de renvoi de remplacement.")

add('242 vicies', '''
<p>Le registre détaillé des bénéficiaires et des paiements mentionné au premier alinéa du A du I de l'article 286 sexies du code général des impôts contient les informations suivantes :</p>
<p>1° Pour le prestataire de services de paiement : son code BIC (Bank Identifier Code) ou tout autre code d'identification d'entreprise permettant de l'identifier sans équivoque ;</p>
<p>2° Pour le bénéficiaire qui est une personne morale :</p>
<p>a) Son nom, sa raison sociale et son nom commercial, tels qu'ils figurent dans les registres du prestataire de services de paiement ;</p>
<p>b) S'il est disponible, son numéro d'identification à la taxe sur la valeur ajoutée, ainsi que tout autre numéro fiscal le concernant ;</p>
<p>c) Son numéro IBAN (International Bank Account Number) ou, à défaut, tout autre identifiant qui l'identifie sans équivoque, ainsi que le lieu où il se trouve ;</p>
<p>d) Si elles sont disponibles, son adresse, son adresse de courriel et l'adresse de son site internet, telles qu'elles figurent dans les registres du prestataire de services de paiement. Ces informations comprennent, le cas échéant, l'adresse légale, l'adresse commerciale et l'adresse de l'entrepôt ;</p>
<p>e) Si le bénéficiaire reçoit les fonds sans avoir aucun compte de paiement, le code BIC ou tout autre code d'identification d'entreprise qui identifie sans équivoque le prestataire de services de paiement agissant en son nom et qui donne le lieu où il se trouve ;</p>
<p>3° Pour le bénéficiaire qui est une personne physique :</p>
<p>a) Son nom, son prénom et son nom commercial, tels qu'ils figurent dans les registres du prestataire de services de paiement ;</p>
<p>b) S'il est disponible, son numéro d'identification à la taxe sur la valeur ajoutée, ainsi que tout autre numéro fiscal le concernant ;</p>
<p>c) Son numéro IBAN ou, à défaut, tout autre identifiant qui l'identifie sans équivoque, ainsi que le lieu où il se trouve ;</p>
<p>d) Si elles sont disponibles, son adresse, son adresse de courriel et l'adresse de son site internet, telles qu'elles figurent dans les registres du prestataire de services de paiement ;</p>
<p>e) Si le bénéficiaire reçoit les fonds sans avoir aucun compte de paiement, le code BIC ou tout autre code d'identification d'entreprise qui identifie sans équivoque le prestataire de services de paiement agissant en son nom et qui donne le lieu où il se trouve ;</p>
<p>4° Pour les paiements transfrontaliers mentionnés au 2° du B du I de l'article 286 sexies du code général des impôts :</p>
<p>a) Les détails de tout paiement transfrontalier et de tout remboursement de paiement identifié comme se rapportant à un paiement transfrontalier, ainsi que, le cas échéant, le lien avec l'opération de paiement déclarée :</p>
<p>i) La date et l'heure du paiement ou du remboursement du paiement ;</p>
<p>ii) Le montant et la monnaie du paiement ou du remboursement du paiement ;</p>
<p>iii) Toute autre référence permettant d'identifier sans équivoque le paiement ;</p>
<p>iv) S'il y a lieu, les informations indiquant que le paiement est initié dans les locaux du commerçant ;</p>
<p>b) Selon le cas, l'Etat membre d'origine du paiement reçu par le bénéficiaire ou en son nom, ou l'Etat membre de destination du remboursement, ainsi que les informations utilisées pour déterminer l'origine ou la destination du paiement ou du remboursement de paiement conformément aux 5° et 6° du B du I de l'article 286 sexies du code général des impôts.</p>
''',
    "À droit constant, les rubriques sont introduites par la personne ou l'opération concernée. La condition d'absence de compte est placée en tête des e et les informations d'adresse du 2° d sont réparties en deux phrases dans le même alinéa. Les quatre numéros, leurs lettres et les i à iv sont conservés. Aucune réforme de fond.",
    "Contrôle des données requises pour les personnes morales et physiques effectué séparément : la raison sociale et les adresses légale, commerciale et d'entrepôt du 2° ne sont pas étendues au 3°. Les conditions de disponibilité, les alternatives IBAN/autre identifiant, les codes BIC, les remboursements, les indications de lieu et les renvois au 2° puis aux 5° et 6° du B du I de l'article 286 sexies sont conservés. L'obligation de registre et son seuil restent définis par l'article 286 sexies, sans seuil nouveau dans le présent article.")

add('242 unvicies', '''
<p>I. - Le prestataire de services de paiement, ou le prestataire tiers qu'il désigne, transmet à la direction générale des finances publiques les informations figurant dans le registre mentionné au I de l'article 286 sexies du code général des impôts. La transmission s'effectue par voie électronique sur un support informatique, au moyen d'un dispositif sécurisé dont la direction générale des finances publiques détermine les caractéristiques.</p>
<p>II. - Le prestataire de services de paiement informe ses clients personnes physiques que les données devant figurer dans le registre mentionné au I de l'article 286 sexies du code général des impôts, et transférées à l'administration fiscale française, sont communiquées à l'administration fiscale d'un autre Etat membre de l'Union européenne.</p>
<p>III. - Le prestataire de services de paiement conserve sous format électronique le registre mentionné au I de l'article 286 sexies du code général des impôts pendant trois années à compter de la fin de l'année civile de la date du paiement. Les modalités de conservation garantissent la confidentialité des informations qui y figurent pendant cette période.</p>
''',
    "À droit constant, l'objet de la transmission est séparé de ses modalités techniques, et la durée de conservation est séparée de l'exigence de confidentialité. Les obligations d'information des clients personnes physiques et les trois subdivisions sont conservées. Aucune réforme de fond.",
    "La durée reste de trois années à compter de la fin de l'année civile de la date du paiement, et non de la date de transmission. La désignation d'un prestataire tiers pour transmettre n'est pas étendue à la conservation. Selon la note source et l'article 2 du décret n° 2023-1149 du 6 décembre 2023, entrée en vigueur le 1er janvier 2024 ; cette date n'est pas celle d'une réforme future. Le délai de transmission prévu au III de l'article 286 sexies demeure applicable par ailleurs.")

add('244', '''
<p>I. - Pour les livraisons à soi-même mentionnées au 2° du 1 du II de l'article 257 du code général des impôts et pour l'application de l'article 270 de ce code, le redevable dépose une déclaration spéciale auprès du service des impôts dont il dépend dans le mois de l'achèvement défini au b du 1 de l'article 269 du même code. Il porte sur la déclaration mentionnée à l'article 287 de ce code une mention particulière qui se réfère à la déclaration spéciale et informe l'administration du montant de la livraison à soi-même et de la liquidation de la taxe.</p>
<p>II. - Pour les livraisons à soi-même mentionnées au 2° du 3 du I de l'article 257 du code général des impôts, le redevable dépose une déclaration particulière auprès du service des impôts du lieu de situation de l'immeuble dès qu'il dispose, à la suite de l'achèvement défini au I, de tous les éléments d'information nécessaires à la liquidation de la taxe. Cette déclaration est conforme au modèle fixé par l'administration.</p>
''',
    "À droit constant, le dépôt et la mention sur la déclaration de chiffre d'affaires sont formulés directement. Au II, le service compétent et le déclenchement du dépôt sont rendus plus lisibles sans confondre les deux régimes. Aucune réforme de fond.",
    "Les I et II sont conservés. Le délai du I reste « dans le mois de l'achèvement » ; il n'est pas remplacé par un délai de trente jours. Le service compétent du I et celui du lieu de l'immeuble au II restent distincts. Les deux renvois à l'article 257 ont été vérifiés dans le corpus. Les notes des articles 257 et 270 annoncent une recodification au 1er janvier 2027 par l'ordonnance n° 2025-1247 du 17 décembre 2025, avec maintien transitoire du II de l'article 270 jusqu'à sa reprise réglementaire visée à l'article L. 161-1 du code des impositions sur les biens et services : coordination à prévoir pour les déclarations et les renvois. Aucun déplacement d'alinéa ni numéro de remplacement inventé.")

add('245', '''
<p>Le directeur départemental ou régional des finances publiques dont dépend le service des impôts mentionné au I de l'article 244 peut accorder des prorogations du délai prévu au II de l'article 270 du code général des impôts. La demande doit être motivée par l'impossibilité d'établir la base taxable définitive avant l'expiration de ce délai. Toutefois, si une mutation intervient avant l'expiration du délai prorogé, la taxe exigible sur la livraison à soi-même doit être acquittée avant cette mutation, sur la base des éléments connus à la date de celle-ci.</p>
''',
    "À droit constant, l'autorité compétente, le motif de la demande et le paiement préalable à une mutation sont distingués en trois phrases dans le même alinéa. Aucune réforme de fond ni modification du calcul de la taxe.",
    "La prorogation demeure une faculté accordée sur demande motivée. Le II de l'article 270 du CGI, consulté dans le corpus, exclut expressément toute prorogation pour le délai spécial concernant les livraisons à soi-même d'immeubles neufs mentionnées aux A et C du II de l'article 278 sexies ; le présent renvoi ne permet pas d'écarter cette exclusion. Le paiement reste préalable à toute mutation intervenant avant l'expiration du délai prorogé et fondé sur les éléments connus à la date de mutation. Coordonner avec l'article 244 et la reprise réglementaire du II de l'article 270 visée à l'article L. 161-1 du code des impositions sur les biens et services, selon la note de recodification du corpus.")

add('245 A', '''
<p>I. - Pour l'application du d du 2° du 2 du I de l'article 257 du code général des impôts, les éléments de second œuvre à prendre en compte sont :</p>
<p>a. Les planchers qui ne déterminent pas la résistance ou la rigidité de l'ouvrage ;</p>
<p>b. Les huisseries extérieures ;</p>
<p>c. Les cloisons intérieures ;</p>
<p>d. Les installations sanitaires et de plomberie ;</p>
<p>e. Les installations électriques ;</p>
<p>f. Pour les opérations réalisées en métropole, le système de chauffage.</p>
<p>II. - Pour chacun des éléments mentionnés au I, la proportion prévue au d du 2° du 2 du I de l'article 257 du code général des impôts est fixée à deux tiers.</p>
''',
    "À droit constant, la condition propre aux planchers est explicitée et le II place en tête l'application du seuil à chaque élément. La liste technique est conservée avec ses lettres a à f ; aucune réforme de fond.",
    "Le seuil reste de deux tiers pour chacun des éléments, et non pour un ensemble agrégé. Le système de chauffage reste limité aux opérations réalisées en métropole ; les planchers participant à la résistance ou à la rigidité sont exclus de la rubrique a. La note de l'article 257 du CGI maintient transitoirement son 2° du 2 du I jusqu'à sa reprise réglementaire visée au dernier alinéa de l'article L. 221-12 du code des impositions sur les biens et services, dans le cadre de l'ordonnance n° 2025-1247 du 17 décembre 2025 : coordonner cette liste lors de cette reprise, sans anticiper un renvoi inexistant.")

add('251', '''
<p>Pour bénéficier des dispositions du A de l'article 1594 F quinquies du code général des impôts, l'intéressé justifie de la prise en charge de la taxe sur la valeur ajoutée par les services des impôts compétents.</p>
''',
    "À droit constant, la condition est formulée comme une obligation explicite de justification. Le simple appel de note historique est retiré du corps rédigé, sans réintroduire les mots devenus sans objet. Aucune réforme de fond du régime de mutation ni de son taux.",
    "La justification porte sur la prise en charge de la TVA par les services compétents, et non sur son paiement lors d'une déclaration. La note source précise que les anciens mots « au paiement de la taxe lors du dépôt de la déclaration prévue à l'article 250 ou, dans les autres situations, » sont devenus sans objet à la suite de l'article 64-I F-1 de la loi n° 2012-1510 du 29 décembre 2012. Ils ne sont pas rétablis. Le A de l'article 1594 F quinquies a été vérifié dans le corpus ; son champ et ses exceptions restent déterminés par cet article. La baisse progressive générale des droits de mutation de policy.json appelle des dispositions d'assiette, de taux, de transition et de financement des collectivités dans le CGI et les textes financiers concernés ; elle ne peut être créée par cette seule règle de justification, sans paramètres ni financement définis.")

add('252', '''
<p>I. - La notification préalable mentionnée au premier alinéa du I de l'article 293 B ter du code général des impôts contient les informations suivantes :</p>
<p>1° Le nom, l'activité, la forme juridique et les adresses postale et électronique de l'assujetti, ainsi que les numéros individuels d'identification dont il dispose dans chaque Etat membre de l'Union européenne ;</p>
<p>2° Le ou les Etats membres de l'Union européenne dans lesquels l'assujetti entend utiliser la franchise ;</p>
<p>3° Le montant total des livraisons de biens et des prestations de services effectuées par l'assujetti en France et dans chacun des autres Etats membres de l'Union européenne :</p>
<p>a) Depuis le 1er janvier de l'année en cours ;</p>
<p>b) Au titre de l'année civile précédente ;</p>
<p>c) Au titre de l'avant-dernière année civile, si au moins un des Etats membres de l'Union européenne concernés par la notification préalable a exercé l'option prévue au paragraphe 1 de l'article 288 bis de la directive 2006/112/CE du Conseil du 28 novembre 2006 relative au système commun de la taxe sur la valeur ajoutée.</p>
<p>II. - Lorsque l'assujetti entend utiliser la franchise dans un ou plusieurs Etats membres de l'Union européenne autres que ceux mentionnés dans la notification préalable, il n'a pas à fournir de nouveau les informations mentionnées au I du présent article si elles figurent dans les déclarations qu'il a effectuées en application des III et IV de l'article 293 B ter du code général des impôts.</p>
<p>III. - La mise à jour de la notification préalable mentionnée au troisième alinéa du I de l'article 293 B ter du code général des impôts comporte le numéro individuel d'identification mentionné au deuxième alinéa du I du même article.</p>
''',
    "À droit constant, la liste des informations et les périodes de chiffre d'affaires sont reformulées sans changer leurs subdivisions. La dispense de nouvelle fourniture d'informations déjà déclarées est rendue plus directe. Cette dispense préexistante répond déjà au réemploi souhaité par policy.json ; aucune réforme de fond n'est ajoutée au régime de franchise.",
    "Conservation des I à III, des trois rubriques du I, des périodes a à c et de la condition tenant à l'option d'au moins un Etat membre au paragraphe 1 de l'article 288 bis de la directive 2006/112/CE du 28 novembre 2006. Les renvois aux premier, deuxième et troisième alinéas du I et aux III et IV de l'article 293 B ter ont été vérifiés dans le corpus. Le II ne crée pas une dispense générale de notification. La note source fixe l'entrée en vigueur au 1er janvier 2025 en application de l'article 2 du décret n° 2024-1195 du 21 décembre 2024. La note du CGI maintient transitoirement l'article 293 B ter jusqu'à sa reprise réglementaire visée au 1° de l'article L. 223-7 et à l'article L. 223-24 du code des impositions sur les biens et services, dans le cadre de la recodification prévue au 1er janvier 2027 : coordonner ces renvois lors de cette reprise.")

assert len(sources) == 24
assert set(drafts) == {a['number'] for a in sources}
answer = []
for source in sources:
    row = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    row.update(drafts[source['number']])
    answer.append(row)
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
