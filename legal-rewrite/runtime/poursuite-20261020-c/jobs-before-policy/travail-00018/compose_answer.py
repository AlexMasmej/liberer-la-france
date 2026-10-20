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


add('L1262-4-5', '''
<p>Sur les chantiers de bâtiment ou de génie civil relevant de l'article L. 4532-10, le maître d'ouvrage doit afficher, sur les lieux de travail, les informations relatives à la réglementation applicable aux salariés détachés en vertu de l'article L. 1262-4. L'affiche doit être facilement accessible. Elle doit être traduite dans l'une des langues officielles parlées dans chacun des États d'appartenance de ces salariés.</p>
<p>Un décret fixe les conditions de mise en œuvre de cette obligation, notamment le contenu des informations mentionnées au premier alinéa.</p>
''',
    "Réécriture à droit constant : l'obligation d'affichage du maître d'ouvrage est exprimée directement et les exigences d'accessibilité et de traduction sont présentées dans des phrases distinctes. Aucune réforme de fond n'est appliquée à cette information des salariés détachés.",
    "Les deux alinéas et les renvois aux articles L. 4532-10 et L. 1262-4 sont conservés. La traduction reste exigée dans une langue officielle parlée dans chacun des États d'appartenance des salariés ; elle n'est pas remplacée par une seule langue commune. Le contenu de l'affiche reste fixé par décret.")

add('L1262-5', '''
<p>Un décret en Conseil d'État fixe :</p>
<p>1° Les conditions et les modalités d'application des dispositions qui relèvent des matières énumérées à l'article L. 1262-4 ;</p>
<p>2° Les conditions dans lesquelles les prestataires étrangers sont tenus d'accomplir des formalités déclaratives ;</p>
<p>3° Les dispenses de formalités accordées à ces prestataires ;</p>
<p>4° Les modalités de désignation du représentant mentionné au II de l'article L. 1262-2-1 et les attributions de ce représentant ;</p>
<p>5° Les modalités d'exécution des obligations prévues à l'article L. 1262-4-1 ;</p>
<p>6° Les modalités de mise en œuvre de l'article L. 1264-3 ;</p>
<p>7° Les conditions d'application de l'article L. 1263-7, notamment les documents qui doivent être traduits en français et les modalités de leur conservation sur le territoire national.</p>
''',
    "Réécriture à droit constant de l'habilitation réglementaire : les prestataires et le représentant sont nommés explicitement et la liste est débarrassée des sauts de ligne parasites. Les sept rubriques sont maintenues. Le projet de guichet unique ne conduit pas à supprimer les formalités propres au détachement.",
    "Numérotation 1° à 7° et tous les renvois conservés, notamment celui du 6° à L. 1264-3. Les obligations de traduction et de conservation demeurent confiées à un décret en Conseil d'État. Aucun transfert de compétence ni aucune dispense nouvelle n'est créé.")

add('L1262-6', '''
<p>Sans préjudice de l'article L. 1262-3 et de la section 2 du présent chapitre, les employeurs qui détachent un ou plusieurs salariés dans les conditions prévues aux 1° et 2° de l'article L. 1262-1 sont dispensés des obligations prévues aux I et II de l'article L. 1262-2-1 lorsque le détachement concerne des prestations et opérations de courte durée ou des événements ponctuels et que les salariés détachés exercent une activité figurant sur une liste fixée par arrêté du ministre chargé du travail.</p>
<p>Pour chaque activité figurant sur cette liste, l'arrêté mentionné au premier alinéa du présent article précise la durée maximale d'activité en France sur une période de référence.</p>
<p>Un décret en Conseil d'État fixe, le cas échéant, les adaptations dont bénéficient les employeurs mentionnés au même premier alinéa pour l'application de l'article L. 1263-7. Ces adaptations portent notamment sur les documents qui doivent être traduits en français et sur les modalités de leur conservation sur le territoire national.</p>
''',
    "Réécriture à droit constant : les conditions cumulatives de la dispense sont replacées après son énoncé, et les adaptations documentaires sont expliquées dans une phrase distincte au sein du troisième alinéa. Aucune extension de la dispense n'est apportée au titre des réformes d'embauche.",
    "Trois alinéas conservés. La dispense reste limitée aux détachements des 1° et 2° de L. 1262-1, aux activités listées et aux opérations ou événements visés ; L. 1262-3 et la section 2 restent réservés. Les durées ne sont pas inventées : elles restent fixées par l'arrêté. L'exclusion des entreprises de travail temporaire et des agences de mannequins demeure portée par L. 1262-7.")

add('L1262-7', '''
<p>La présente section ne s'applique ni aux entreprises de travail temporaire définies à l'article L. 1251-2 ni aux agences de mannequins définies à l'article L. 7123-12.</p>
''',
    "Réécriture à droit constant : une formulation directe remplace la tournure passive pour énoncer les deux exclusions de la section. Aucune réforme de fond ni extension des dispenses n'est introduite.",
    "Le périmètre demeure celui de toute la présente section, avec les deux catégories et leurs renvois L. 1251-2 et L. 7123-12. Cette exclusion continue notamment d'encadrer la dispense de L. 1262-6.")

add('L1263-1', '''
<p>Pour assurer l'application du présent titre, les agents de contrôle mentionnés à l'article L. 8112-1 et les autorités chargées de coordonner leurs actions peuvent échanger entre eux tous les renseignements et documents nécessaires.</p>
<p>Ils peuvent aussi transmettre ces renseignements et documents aux agents qui disposent de pouvoirs analogues dans les États étrangers ainsi qu'aux autorités chargées de coordonner les actions de ces agents dans ces États.</p>
<p>Les agents de contrôle mentionnés à l'article L. 8271-1-2 ont le droit d'accéder aux données issues des déclarations de détachement transmises à l'inspection du travail en application des articles L. 1262-2-1 et L. 1262-4-1, dans la mesure où ces données sont nécessaires à leur mission de lutte contre le travail illégal.</p>
''',
    "Réécriture à droit constant : la finalité des échanges est placée en tête, les échanges réciproques sont distingués des transmissions internationales et la limite du droit d'accès aux données est exprimée directement. Aucune interconnexion ni réutilisation supplémentaire n'est créée par les orientations de simplification.",
    "Trois alinéas conservés. Les transmissions internationales restent limitées aux agents disposant de pouvoirs analogues et à leurs autorités de coordination ; elles ne deviennent pas une publication. Le droit d'accès reste attaché à L. 8271-1-2 et aux seules données nécessaires à la lutte contre le travail illégal. Coordination maintenue avec la protection des données prévue par L. 1263-2.")

add('L1263-2', '''
<p>Un décret en Conseil d'État précise la nature des informations qui peuvent être communiquées ainsi que les conditions dans lesquelles la protection des données à caractère personnel est assurée.</p>
''',
    "Réécriture à droit constant : le décret est le sujet de la phrase et les deux objets de l'habilitation sont explicités. Aucune réforme de fond ne modifie les garanties de protection des données.",
    "La détermination des informations communicables et de la protection des données reste confiée à un décret en Conseil d'État, en articulation avec L. 1263-1. Le texte ne crée pas de droit général de communication ou de dispense de protection.")

add('L1263-3', '''
<p>L'agent de contrôle de l'inspection du travail mentionné à l'article L. 8112-1 enjoint par écrit à l'employeur établi hors de France qui détache des salariés sur le territoire national de faire cesser la situation dans un délai fixé par décret en Conseil d'État lorsqu'il constate :<br />— un manquement grave commis par cet employeur à l'article L. 3131-1 relatif au repos quotidien, à l'article L. 3132-2 relatif au repos hebdomadaire, à l'article L. 3121-18 relatif à la durée quotidienne maximale de travail ou à l'article L. 3121-20 relatif à la durée hebdomadaire maximale de travail ;<br />— le non-paiement total ou partiel du salaire minimum légal ou conventionnel ;<br />— un manquement de l'employeur ou de son représentant à l'obligation prévue à l'article L. 1263-7, en vue du contrôle du respect des articles L. 3231-2, L. 3131-1, L. 3132-2, L. 3121-18 et L. 3121-20 du présent code ;<br />— des conditions de travail ou d'hébergement incompatibles avec la dignité humaine, sanctionnées à l'article 225-14 du code pénal ;<br />— le défaut de paiement des sommes dues par l'employeur au titre d'une amende administrative qui lui a été notifiée en application des articles L. 1263-6, L. 1264-1, L. 1264-2 ou L. 8115-1 du présent code.</p>
<p>L'agent en informe, dans les plus brefs délais, le maître d'ouvrage ou le donneur d'ordre de l'employeur concerné.</p>
<p>La communication par l'employeur d'informations délibérément erronées à l'agent de contrôle constitue un manquement grave au sens du premier alinéa.</p>
<p>Pour l'application du présent article, lorsque l'employeur établi hors de France détache sur le territoire national des salariés exerçant des activités relevant du code rural et de la pêche maritime, le renvoi à l'article L. 3132-2 du présent code est remplacé par un renvoi à l'article L. 714-1 du code rural et de la pêche maritime.</p>
''',
    "Réécriture à droit constant : les cinq situations justifiant l'injonction sont présentées séparément par des retours à la ligne à l'intérieur du premier alinéa, sans créer de numérotation. Le rôle de l'agent, l'information du donneur d'ordre et la règle agricole sont explicités. Le relèvement du seuil des heures supplémentaires prévu ailleurs ne modifie pas ici les repos, les durées maximales ou les minima salariaux.",
    "Les quatre alinéas sont conservés : la liste reste entièrement dans le premier, que vise le troisième. La qualification de manquement grave attachée aux repos et durées maximales, le paiement total ou partiel du minimum légal ou conventionnel, les documents de contrôle, la dignité humaine et les amendes notifiées sont tous maintenus. Les informations délibérément erronées restent un manquement grave. La substitution agricole ne concerne que L. 3132-2, remplacé par L. 714-1 du code rural et de la pêche maritime ; aucun régime agricole distinct n'est réformé.")

add('L1263-4', '''
<p>Si l'employeur n'a pas régularisé la situation constatée dans le délai mentionné à l'article L. 1263-3, l'autorité administrative compétente peut, dès lors qu'elle a connaissance d'un rapport d'un agent de contrôle de l'inspection du travail constatant le manquement, lui ordonner de suspendre la réalisation de la prestation de services concernée pour une durée d'au plus un mois. Elle statue par une décision motivée, en tenant compte de la répétition ou de la gravité des faits constatés.</p>
<p>L'autorité administrative met fin à la suspension dès que l'employeur justifie que le manquement constaté a cessé.</p>
''',
    "Réécriture à droit constant : les conditions de la suspension, son fondement dans le rapport de contrôle et l'obligation de motivation sont répartis en phrases distinctes. La levée de la mesure reste impérative dès justification de la régularisation. Aucune réforme de fond n'affecte ce contrôle du détachement.",
    "Le renvoi au délai de L. 1263-3, la durée maximale d'un mois, le caractère facultatif du prononcé et la prise en compte de la répétition ou de la gravité sont conservés. Les deux blocs de texte séparés par des retours à la ligne dans la source sont présentés en deux paragraphes ; aucun alinéa numéroté n'est déplacé. L'attribut de présentation align, non autorisé, est supprimé.")

add('L1263-4-1', '''
<p>Si, à l'expiration d'un délai de quarante-huit heures à compter du début du détachement d'un salarié, l'agent de contrôle de l'inspection du travail ou l'agent de contrôle assimilé mentionné au dernier alinéa de l'article L. 8112-1 n'a pas reçu la déclaration de détachement mentionnée au deuxième alinéa du I de l'article L. 1262-4-1, il peut saisir l'autorité administrative compétente par un rapport motivé. Au regard de la gravité du manquement, cette autorité peut, par décision motivée, ordonner la suspension de la réalisation de la prestation de services pour une durée d'au plus un mois.</p>
<p>L'autorité administrative met fin à la suspension dès qu'elle reçoit, pour les salariés concernés, la déclaration de détachement transmise par l'employeur, le donneur d'ordre ou le maître d'ouvrage.</p>
<p>La sanction prévue au premier alinéa du présent article peut se cumuler avec l'amende administrative prévue aux articles L. 1264-1 et L. 1264-2.</p>
<p>Un décret en Conseil d'État fixe les modalités d'application du présent article.</p>
''',
    "Réécriture à droit constant : le délai et l'absence de déclaration sont placés au début de la condition de saisine ; la décision et la fin de la suspension ont chacune un sujet explicite. Aucun allègement de contrôle ni changement de sanction n'est introduit.",
    "Quatre alinéas conservés. Les quarante-huit heures courent toujours du début du détachement, et la déclaration visée reste celle du deuxième alinéa du I de L. 1262-4-1. Le mois maximal, les deux motivations, le critère de gravité, les trois auteurs possibles de la transmission et le cumul de sanctions sont maintenus.")

add('L1263-4-2', '''
<p>L'agent de contrôle de l'inspection du travail ou l'agent de contrôle assimilé mentionné au dernier alinéa de l'article L. 8112-1 saisit l'autorité administrative compétente par un rapport motivé lorsqu'il constate, le cas échéant à la réception de la déclaration mentionnée à l'article L. 1262-2-1, qu'un employeur établi à l'étranger, détachant un ou plusieurs salariés dans les conditions prévues aux articles L. 1262-1 ou L. 1262-2, n'a pas payé les sommes dues au titre d'une amende prévue aux articles L. 1263-6, L. 1264-1, L. 1264-2 ou L. 8115-1 qui lui a été notifiée. Avant le début de la prestation, l'autorité administrative informe sans délai l'entreprise concernée du manquement constaté et lui enjoint d'y mettre fin en payant les sommes dues.</p>
<p>Si la situation n'est pas régularisée avant le début de la prestation, l'autorité administrative peut, au regard de la gravité du manquement et par décision motivée, interdire la prestation de services pour une durée de deux mois renouvelable. Tant que le manquement n'est pas régularisé, la prestation ne peut pas débuter.</p>
<p>L'autorité administrative autorise la prestation dès que les sommes mentionnées au premier alinéa du présent article sont payées.</p>
''',
    "Réécriture à droit constant : le défaut de paiement est formulé directement, puis sont distinguées l'information préalable, l'injonction de payer, l'interdiction et l'autorisation après paiement. La nature préventive du dispositif et la possibilité de renouvellement sont préservées. Aucune réforme de fond n'est appliquée.",
    "Trois alinéas conservés. Le rapport reste obligatoire en cas de constat, l'amende doit avoir été notifiée, l'information intervient sans délai avant la prestation, et l'interdiction demeure de deux mois renouvelable sans plafond de renouvellement inventé. La prestation ne peut débuter sans régularisation ; son autorisation est due dès paiement. Le décalage de vocabulaire avec la « suspension » mentionnée à L. 1263-5 est signalé dans les observations de cet article, sans modifier ici l'interdiction.")

add('L1263-5', '''
<p>Une décision de suspension de la prestation de services prise par l'autorité administrative en application des articles L. 1263-4, L. 1263-4-1 ou L. 1263-4-2 ne rompt ni ne suspend le contrat de travail des salariés concernés. Elle n'entraîne pour eux aucun préjudice pécuniaire.</p>
''',
    "Réécriture à droit constant : les effets sur le contrat et la garantie pécuniaire des salariés sont exprimés dans deux phrases au sein du même alinéa. Aucune réduction de protection ni réforme de la rupture du contrat n'est introduite.",
    "Incohérence préexistante conservée et à coordonner expressément : le texte qualifie de « suspension » les décisions des trois articles cités, alors que L. 1263-4-2 prévoit une interdiction avant le début de la prestation. Le renvoi à cet article et toutes les garanties des salariés sont maintenus ; aucune substitution silencieuse de qualification n'est faite.")

add('L1263-6', '''
<p>L'employeur qui ne respecte pas une décision administrative mentionnée à l'article L. 1263-4, L. 1263-4-1 ou L. 1263-4-2 encourt une amende administrative. L'autorité administrative compétente prononce cette amende sur le rapport motivé d'un agent de contrôle de l'inspection du travail mentionné à l'article L. 8112-1.</p>
<p>Pour fixer le montant de l'amende, l'autorité administrative tient compte des circonstances et de la gravité du manquement, du comportement de son auteur ainsi que de ses ressources et de ses charges. L'amende ne peut dépasser 10 000 € par salarié concerné par le manquement.</p>
<p>L'action de l'administration visant à sanctionner le manquement par une amende administrative se prescrit par deux années révolues à compter du jour où ce manquement a été commis.</p>
<p>L'employeur peut contester la décision administrative devant le tribunal administratif. Tout recours hiérarchique est exclu.</p>
<p>L'amende est recouvrée selon les règles applicables aux créances de l'État étrangères à l'impôt et au domaine. Une opposition à l'exécution ou aux poursuites ne suspend pas l'action en recouvrement de la créance.</p>
''',
    "Réécriture à droit constant : l'employeur est désigné comme auteur du manquement, le prononcé de la sanction et le recours sont exposés en phrases courtes, et la prescription est formulée directement. Aucun montant ni régime de sanction n'est modifié par le projet.",
    "Les cinq alinéas restent dans le même ordre. Plafond de 10 000 € par salarié, critères de fixation, rapport motivé, prescription de deux années révolues depuis la commission, tribunal administratif, exclusion du recours hiérarchique et absence d'effet suspensif des deux oppositions sont conservés. Ce plafond n'est pas confondu avec ceux de L. 1264-3.")

add('L1263-7', '''
<p>L'employeur qui détache temporairement des salariés sur le territoire national, ou son représentant mentionné au II de l'article L. 1262-2-1, doit présenter à l'inspection du travail, sur le lieu de réalisation de la prestation, des documents traduits en français permettant de vérifier le respect des dispositions du présent titre.</p>
''',
    "Réécriture à droit constant : l'obligation de présentation est rendue explicite et ses destinataire et lieu sont rapprochés du verbe. Les documents de contrôle ne sont ni supprimés ni remplacés par une déclaration générale au titre de la simplification.",
    "L'alternative entre employeur et représentant du II de L. 1262-2-1, la présentation sur le lieu de prestation et la traduction en français sont conservées. Articulation à maintenir avec les adaptations de L. 1262-6 et L. 1263-8 et l'habilitation du 7° de L. 1262-5. L'attribut de présentation align est supprimé sans effet normatif.")

add('L1263-8', '''
<p>Sur demande d'un ou de plusieurs employeurs détachant de manière récurrente des salariés dans les conditions prévues aux 1° et 2° de l'article L. 1262-1, ou d'un organisme ayant mandat, l'autorité administrative peut aménager les modalités d'exécution des obligations prévues aux I et II de l'article L. 1262-2-1 et à l'article L. 1263-7. Elle ne peut accorder ces aménagements que si la demande est appuyée par des informations attestant le respect des dispositions légales et des stipulations conventionnelles dans les matières énumérées à l'article L. 1262-4.</p>
<p>Les aménagements sont accordés pour une durée d'au plus un an et sont notifiés au demandeur.</p>
<p>Pendant cette durée, l'autorité administrative peut demander la communication des documents prévus à l'article L. 1263-7.</p>
<p>L'autorité administrative met fin aux aménagements accordés en application du premier alinéa du présent article si les modalités définies sur le fondement du même premier alinéa n'ont pas été respectées ou si un manquement aux règles applicables dans les matières énumérées à l'article L. 1262-4 est constaté.</p>
<p>La demande de renouvellement des aménagements doit être accompagnée de tout élément attestant, pour la période écoulée, le respect des dispositions légales et des stipulations conventionnelles dans les matières énumérées au même article L. 1262-4.</p>
<p>Un décret en Conseil d'État fixe la nature des aménagements qui peuvent être accordés en application du présent article.</p>
''',
    "Réécriture à droit constant : la demande et ses justificatifs sont distingués dans le premier alinéa, puis la durée, le contrôle, la cessation et le renouvellement sont exposés avec des sujets explicites. Aucun droit automatique à l'aménagement ni dispense nouvelle n'est créé.",
    "Six alinéas conservés avec les renvois internes au premier alinéa. La récurrence, le champ des seuls 1° et 2° de L. 1262-1, les obligations des I et II de L. 1262-2-1 et de L. 1263-7, la durée maximale d'un an, la notification et les deux motifs alternatifs de cessation sont maintenus. Le renouvellement exige toujours des éléments portant sur la période écoulée.")

historical_2020 = (
    "Notes historiques lues : entrée en vigueur le 30 juillet 2020 selon les I et II de l'article 7 "
    "de l'ordonnance n° 2019-116 du 20 février 2019 ; modalités d'application à vérifier au II "
    "de cet article 7 et au III de l'article 25 de la loi n° 2021-1308 du 8 octobre 2021. "
    "Ces dates et règles d'application ne constituent pas une entrée en vigueur de la réforme projetée."
)

add('L1264-1', '''
<p>L'employeur qui détache un ou plusieurs salariés encourt une amende administrative dans les conditions prévues à l'article L. 1264-3 s'il ne respecte pas l'une des obligations mentionnées à l'article L. 1262-2-1, au troisième alinéa du II de l'article L. 1262-4, à l'article L. 1262-4-4 ou à l'article L. 1263-7.</p>
''',
    "Réécriture à droit constant : l'employeur devient le sujet de la sanction et la méconnaissance est formulée comme une condition explicite, en conservant l'intégralité des obligations visées. Aucune réforme de fond n'est appliquée aux sanctions du détachement.",
    "Tous les renvois sont conservés, spécialement celui au troisième alinéa du II de L. 1262-4, relatif à la déclaration motivée de prorogation, vérifié dans le corpus local. L. 1264-3 demeure le texte fixant le régime de l'amende. " + historical_2020)

add('L1264-2', '''
<p>I. – Le maître d'ouvrage, le donneur d'ordre ou l'entreprise utilisatrice encourt une amende administrative, dans les conditions prévues à l'article L. 1264-3, dans les cas suivants :</p>
<p>1° S'il ne respecte pas l'une des obligations mentionnées au I de l'article L. 1262-4-1, alors que son cocontractant n'a pas rempli au moins l'une des obligations qui lui incombent en application de l'article L. 1262-2-1 ;</p>
<p>2° S'il ne respecte pas l'obligation mentionnée à l'article L. 1262-4-4 ;</p>
<p>3° S'il ne respecte pas l'obligation mentionnée à l'article L. 1262-4-5 ;</p>
<p>4° En cas de manquement à l'obligation d'information prévue au V de l'article L. 1262-2-1 et en cas de manquement de l'employeur tel que prévu au 4° de l'article L. 8115-1.</p>
<p>II. – Le maître d'ouvrage encourt une amende administrative dans les conditions prévues à l'article L. 1264-3 s'il ne respecte pas l'obligation mentionnée au II de l'article L. 1262-4-1 et si l'un des sous-traitants directs ou indirects de ses cocontractants ou l'une des entreprises exerçant une activité de travail temporaire n'a pas rempli l'obligation mentionnée au I de l'article L. 1262-2-1. L'entreprise utilisatrice encourt également une amende administrative dans les conditions prévues à l'article L. 1264-3 si elle ne respecte pas l'obligation mentionnée au IV de l'article L. 1262-2-1.</p>
''',
    "Réécriture à droit constant : les personnes sanctionnées et les conditions de leurs manquements sont exprimées directement, en conservant les I et II et les quatre rubriques du I. Le lien entre le défaut de vigilance et le défaut du cocontractant ou du sous-traitant demeure explicite. Aucune sanction supplémentaire n'est créée par les réformes d'embauche.",
    "Six paragraphes et subdivisions conservés, y compris les deux règles dans l'unique alinéa du II. Le 1° conserve le défaut d'au moins une obligation du cocontractant. La conjonction « et » du 4° est volontairement maintenue : sa portée entre défaut d'information et manquement salarial de l'employeur ne doit pas être modifiée sans clarification expresse. Les V et IV de L. 1262-2-1 et le 4° de L. 8115-1 ont été vérifiés dans le corpus. " + historical_2020)

add('L1264-3', '''
<p>L'autorité administrative compétente prononce l'amende administrative mentionnée aux articles L. 1264-1 et L. 1264-2 après qu'un des agents de contrôle de l'inspection du travail mentionnés aux articles L. 8112-1 et L. 8112-5 a constaté le manquement.</p>
<p>L'amende ne peut dépasser 4 000 € par salarié détaché. Ce plafond est porté à 8 000 € en cas de réitération dans un délai de deux ans à compter du jour de la notification de la première amende. Le montant total de l'amende ne peut dépasser 500 000 €.</p>
<p>Pour fixer le montant de l'amende, l'autorité administrative tient compte des circonstances et de la gravité du manquement, du comportement de son auteur, notamment de sa bonne foi, ainsi que de ses ressources et de ses charges.</p>
<p>L'action de l'administration visant à sanctionner le manquement par une amende administrative se prescrit par deux années révolues à compter du jour où ce manquement a été commis.</p>
<p>L'employeur, le maître d'ouvrage ou le donneur d'ordre peut contester la décision administrative devant le tribunal administratif. Tout recours hiérarchique est exclu.</p>
<p>L'amende est recouvrée selon les règles applicables aux créances de l'État étrangères à l'impôt et au domaine. Une opposition à l'exécution ou aux poursuites ne suspend pas l'action en recouvrement de la créance.</p>
''',
    "Réécriture à droit constant : le prononcé de l'amende est formulé à la voix active, les trois plafonds sont distingués et les règles de prescription, de recours et de recouvrement sont simplifiées sans modifier leur portée. Aucune réforme de fond ne change ces sanctions.",
    "Six alinéas conservés. Contrôle des chiffres : 4 000 € par salarié, 8 000 € en réitération, deux ans depuis la notification de la première amende, plafond total de 500 000 €, prescription distincte de deux années révolues depuis le manquement. Bonne foi et autres critères conservés. Deux points préexistants nécessitent une coordination expresse : le renvoi à L. 8112-5 n'a pas de cible dans le fichier travail.json fourni ; l'entreprise utilisatrice, sanctionnable par L. 1264-2, n'est pas nommée dans l'alinéa relatif au recours. Ni le renvoi ni la liste des requérants ne sont corrigés silencieusement. " + historical_2020)

add('L1264-4', '''
<p>L'État constate la sanction ou l'amende administrative pécuniaire infligée à un prestataire de services établi en France et notifiée par l'autorité compétente d'un État membre de l'Union européenne autre que la France, lorsqu'elle concerne un détachement de salariés dans les conditions prévues par la directive 96/71/CE du Parlement européen et du Conseil du 16 décembre 1996 concernant le détachement de travailleurs effectué dans le cadre d'une prestation de services. Il procède à cette constatation en application de l'article 15 de la directive 2014/67 UE du Parlement européen et du Conseil du 15 mai 2014 relative à l'exécution de la directive 96/71 CE concernant le détachement de travailleurs effectué dans le cadre d'une prestation de services et modifiant le règlement (UE) n° 1024/2012 concernant la coopération administrative par l'intermédiaire du système d'information du marché intérieur (« règlement IMI »).</p>
<p>La sanction ou l'amende est recouvrée selon les règles applicables aux créances étrangères à l'impôt et au domaine. Une opposition à l'exécution ou aux poursuites ne suspend pas l'action en recouvrement de la créance.</p>
<p>Le ministre chargé du travail émet les titres de perception.</p>
<p>L'action en recouvrement du comptable public se prescrit selon les dispositions de l'article L. 274 du livre des procédures fiscales.</p>
<p>Le produit de ces sanctions ou amendes est versé au budget général de l'État.</p>
''',
    "Réécriture à droit constant : la constatation par l'État et son fondement européen sont séparés en deux phrases, et l'émission des titres est formulée à la voix active. Les conditions transfrontières, le recouvrement et l'affectation du produit demeurent identiques. Aucun financement nouveau n'est attribué à cette recette.",
    "Cinq alinéas conservés, avec les références complètes aux directives des 16 décembre 1996 et 15 mai 2014, à l'article 15, au règlement (UE) n° 1024/2012 et à L. 274 du livre des procédures fiscales. Les graphies 2014/67 UE et 96/71 CE sont celles de la source. Note historique conservée pour l'application : selon le A du XI de l'article 160 de la loi n° 2020-1721 du 29 décembre 2020, entrée en vigueur le 1er janvier 2022 et application à l'action en recouvrement dont le délai de prescription commence à courir ou dont une cause interruptive de prescription intervient à compter du 1er janvier 2022. Cette transition n'est pas transformée en date d'une réforme future ; aucun délai chiffré absent du texte n'est ajouté.")

add('L1265-1', '''
<p>Les organisations syndicales représentatives peuvent exercer en justice, en faveur d'un salarié, toutes les actions résultant de l'application du présent titre sans avoir à justifier d'un mandat de ce salarié.</p>
<p>Il suffit que le salarié ait été averti dans les conditions fixées par voie réglementaire et qu'il ne se soit pas opposé à l'action dans un délai de quinze jours à compter de la date à laquelle l'organisation syndicale lui a notifié son intention.</p>
<p>Le salarié peut toujours intervenir dans l'instance engagée par le syndicat. Il peut mettre fin à cette instance à tout moment.</p>
''',
    "Réécriture à droit constant : les pronoms sont remplacés par la désignation du salarié et l'objet du droit d'opposition et de l'intervention est explicité. Le pouvoir d'action du syndicat et la maîtrise de l'instance par le salarié sont intégralement conservés ; aucune réforme de fond ne restreint le recours au juge.",
    "Les trois alinéas matériels de la source sont présentés en paragraphes. Le délai de quinze jours reste calculé depuis la notification de l'intention du syndicat, sans exigence nouvelle de mandat ou d'accord positif. Représentativité, information réglementaire, faculté d'intervention et droit de mettre fin à l'instance sont maintenus.")

add('L1271-1', '''
<p>Le chèque emploi-service universel prend la forme d'un titre emploi ou d'un titre spécial de paiement.</p>
<p>A. – Le titre emploi permet de déclarer :</p>
<p>1° Les salariés mentionnés au 3° de l'article L. 133-5-6 du code de la sécurité sociale ;</p>
<p>2° Les stagiaires aides familiaux placés au pair mentionnés au 6° de l'article L. 133-5-6 du même code ;</p>
<p>3° Les accueillants familiaux mentionnés à l'article L. 441-1 du code de l'action sociale et des familles.</p>
<p>B. – Le titre spécial de paiement permet de régler tout ou partie du montant des rémunérations, cotisations, contributions, prestations ou contreparties suivantes :</p>
<p>1° La rémunération et les cotisations et contributions sociales afférentes des salariés occupant des emplois entrant dans le champ des services à la personne mentionnés à l'article L. 7231-1, ainsi que des assistants maternels agréés en application de l'article L. 421-1 du code de l'action sociale et des familles ;</p>
<p>2° Les prestations de services fournies par les organismes agréés ou déclarés au titre des articles L. 7232-1 et L. 7232-1-1 ;</p>
<p>3° Dans les conditions et limites fixées par décret, les prestations de services fournies par les organismes et établissements spécialisés mentionnés à l'article L. 1271-10 ;</p>
<p>4° Les prestations de services fournies par les organismes ou personnes mentionnés au premier alinéa de l'article L. 2324-1 du code de la santé publique ;</p>
<p>5° Les prestations de services fournies par les organismes ou les personnes organisant un accueil sans hébergement prévu au même article L. 2324-1 ;</p>
<p>6° Les prestations de services fournies par les personnes organisant un accueil des enfants scolarisés en école maternelle ou élémentaire limité aux heures qui précèdent ou suivent la classe ;</p>
<p>7° Les prestations d'aide à domicile fournies par des salariés ou des organismes de services à la personne à ses ascendants bénéficiaires de l'allocation personnalisée d'autonomie ;</p>
<p>8° Les prestations de transport de voyageurs par taxi financées par les prestations sociales destinées spécifiquement aux personnes âgées ou à mobilité réduite ;</p>
<p>9° Les contreparties financières définies à l'article L. 442-1 du code de l'action sociale et des familles.</p>
''',
    "Réécriture à droit constant : les deux fonctions du chèque sont distinguées par des introductions complètes et les objets des déclarations et paiements sont présentés comme listes homogènes. Les trois catégories du A et les neuf catégories du B restent intégrales. Aucun nouveau guichet, emploi éligible ou usage du titre n'est créé au titre du projet de simplification.",
    "Les quinze paragraphes, les lettres A et B, les numéros et tous les renvois sont conservés. Les conditions du décret au B, 3°, l'agrément des assistants maternels, les limites horaires de l'accueil périscolaire et le financement spécifique des taxis sont maintenus. Points préexistants à contrôler expressément : L. 1271-10 décrit dans le corpus les émetteurs et le remboursement du titre, alors que le B, 3° vise des prestataires de services ; le possessif « ses ascendants » du B, 7° n'a pas d'antécédent personnel explicite. Le renvoi et ce possessif sont maintenus sans trancher silencieusement leur portée.")

add('L1271-4', '''
<p>Lorsque le nombre d'heures de travail effectuées par un salarié ne dépasse pas un seuil fixé par décret, la rémunération portée sur le chèque emploi-service universel comprend une indemnité compensatrice de congés payés égale à un dixième de la rémunération brute. Pour apprécier les conditions d'ouverture des droits aux prestations sociales, le temps d'emploi effectif indiqué sur la déclaration est majoré à due proportion. Le présent alinéa s'applique aussi au-delà de ce seuil si l'employeur et le salarié en conviennent.</p>
<p>Lorsque des salariés consacrent tout ou partie de leur temps de travail à une activité contribuant à l'exercice de la profession de leur employeur ou de l'acheteur des prestations, et pour le compte de celui-ci, le chèque emploi-service universel ne peut être utilisé ni pour leur rémunération directe ni pour le paiement des prestations qu'ils réalisent.</p>
''',
    "Réécriture à droit constant : le seuil réglementaire est présenté comme condition d'inclusion de l'indemnité et l'accord permettant l'application au-delà du seuil est formulé directement. L'interdiction d'utiliser le chèque pour une activité professionnelle de l'employeur ou de l'acheteur demeure complète. Aucune réforme du congé payé n'est introduite.",
    "Deux alinéas conservés, dont les trois règles du premier : seuil fixé par décret, indemnité d'un dixième du brut et majoration proportionnelle du temps déclaré pour les droits sociaux. L'accord bilatéral demeure nécessaire au-delà du seuil. L'exclusion du second alinéa vise toujours une activité consacrant tout ou partie du temps, la rémunération directe et l'achat de prestations, avec l'exigence « pour le compte de celui-ci » inchangée dans sa portée.")

add('L1271-5', '''
<p>Lorsque la durée de travail d'un emploi ne dépasse pas trois heures par semaine au cours d'une période de référence de quatre semaines, l'employeur et le salarié qui utilisent le chèque emploi-service universel sont réputés satisfaire aux obligations mises à la charge de l'un ou de l'autre par les articles L. 1242-12 et L. 1242-13, pour un contrat de travail à durée déterminée, et par l'article L. 3123-6, pour un contrat de travail à temps partiel, ou par les articles L. 741-2 et L. 741-9 du code rural et de la pêche maritime.</p>
<p>Les emplois mentionnés au premier alinéa du présent article ne sont pas soumis à l'obligation prévue à l'article L. 1221-5-1 du présent code.</p>
<p>Pour les emplois dont la durée de travail est supérieure, le contrat de travail doit être établi par écrit.</p>
''',
    "Réécriture à droit constant : la condition de durée précède la présomption et les obligations visées sont rattachées explicitement à chaque catégorie de contrat. L'exception d'information écrite et l'exigence de contrat écrit au-delà du seuil sont maintenues. La réforme du temps partiel n'est pas étendue automatiquement à ce régime spécial.",
    "Trois alinéas conservés ; seuil de trois heures par semaine et période de référence de quatre semaines inchangés, sans conversion en seuil moyen nouveau. Les renvois aux CDD, au temps partiel et au code rural restent complets. L'exception à L. 1221-5-1 demeure celle de la source. Coordination à vérifier expressément avec la rédaction réformée de L. 3123-6 concernant le volume contractuel garanti : ne pas élargir par déduction la dispense spéciale du CESU ni supprimer une garantie de volume sans disposition expresse.")

add('L1271-6', '''
<p>Un autre moyen de paiement peut remplacer le titre spécial de paiement, dans les limites des interdictions de paiement en espèces prévues aux articles L. 112-6 à L. 112-8 du code monétaire et financier.</p>
''',
    "Réécriture à droit constant : le remplacement du titre par un autre moyen de paiement est exprimé directement, sous réserve des mêmes interdictions de paiement en espèces. La tournure défectueuse de la source est explicitement signalée dans les observations ; aucune nouvelle modalité de paiement n'est instituée.",
    "Anomalie textuelle préexistante : la source porte « en remplacement ou du titre spécial de paiement », avec un « ou » sans second terme identifiable. La proposition retient le sens du remplacement du titre et omet ce « ou » isolé ; cette correction rédactionnelle doit être contrôlée expressément, sans lui attribuer une alternative non écrite. Les limites des articles L. 112-6 à L. 112-8 du code monétaire et financier sont intégralement maintenues.")

add('L1271-7', '''
<p>Les prestations sociales obligatoires ou facultatives peuvent être versées sous la forme d'un titre spécial de paiement si elles ont le caractère de prestations en nature et sont destinées à couvrir tout ou partie du coût des services mentionnés au B de l'article L. 1271-1.</p>
''',
    "Réécriture à droit constant : la faculté de versement est suivie de ses deux conditions explicites, relatives à la nature de la prestation et à sa destination. Aucune prestation nouvelle ni modification des financements sociaux n'est introduite.",
    "Le caractère obligatoire ou facultatif des prestations, leur nature de prestations en nature, la couverture totale ou partielle et le renvoi au seul B de L. 1271-1 sont conservés. Ce mécanisme de paiement n'est pas étendu aux autres prestations sociales par les projets fiscaux ou de retraite.")


assert len(sources) == 24
assert set(drafts) == {a['number'] for a in sources}
answer = []
for source in sources:
    row = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    row.update(drafts[source['number']])
    answer.append(row)
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
