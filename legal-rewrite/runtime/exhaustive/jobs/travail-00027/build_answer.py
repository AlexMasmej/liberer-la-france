import json
from pathlib import Path


DRAFTS = {
    "L2122-7": {
        "proposed_xml": "<p>Une organisation syndicale catégorielle est représentative au niveau de la branche si elle est affiliée à une confédération syndicale catégorielle interprofessionnelle nationale et remplit les conditions de l'article L. 2122-5 dans les collèges électoraux où ses règles statutaires lui donnent vocation à présenter des candidats. Cette représentativité s'exerce à l'égard des personnels relevant de ces collèges.</p>",
        "reason": "Réécriture à droit constant : les conditions d'affiliation et de représentativité précèdent la délimitation des personnels concernés. Aucune réforme de fond n'est appliquée à ce régime catégoriel.",
        "review_notes": "Le renvoi à l'article L. 2122-5 est conservé et vérifié dans le corpus public. Les conditions restent appréciées dans les seuls collèges relevant de la vocation statutaire de l'organisation ; la représentativité n'est pas étendue aux autres personnels.",
    },
    "L2122-8": {
        "proposed_xml": "<p>Les organisations syndicales dont la représentativité est établie fixent, en lien avec les organisations d'employeurs, la liste des sujets de la négociation collective de branche et les modalités d'organisation de cette négociation.</p>",
        "reason": "Réécriture à droit constant : le sujet de la phrase est explicité et la référence à l'organisation de la négociation est clarifiée. Aucune réforme de fond de la négociation de branche n'est introduite.",
        "review_notes": "Le rôle des organisations syndicales représentatives et le lien avec les organisations d'employeurs sont conservés. Seul le paragraphe final vide de la source est supprimé ; il ne contient aucune disposition.",
    },
    "L2122-9": {
        "proposed_xml": "<p>Les organisations syndicales sont représentatives au niveau national et interprofessionnel lorsqu'elles remplissent les conditions suivantes :</p><p>1° Elles satisfont aux critères de l'article L. 2121-1 ;</p><p>2° Elles sont représentatives à la fois dans des branches de l'industrie, de la construction, du commerce et des services ;</p><p>3° Elles ont recueilli au moins 8 % des suffrages exprimés, calculés en additionnant, au niveau national et interprofessionnel, les suffrages exprimés au premier tour des dernières élections des titulaires aux comités sociaux et économiques, quel que soit le nombre de votants, ceux exprimés au scrutin concernant les entreprises de moins de onze salariés, dans les conditions prévues aux articles L. 2122-10-1 et suivants, et ceux exprimés aux élections des membres représentant les salariés aux chambres départementales d'agriculture, dans les conditions prévues à l'article L. 2122-6. L'audience est mesurée tous les quatre ans.</p>",
        "reason": "Réécriture à droit constant : chaque condition a un sujet explicite et les trois composantes du calcul d'audience sont reliées plus directement. Aucune réforme de fond des critères ou du seuil n'est opérée.",
        "review_notes": "Les 1°, 2° et 3° restent dans leurs alinéas respectifs. Sont conservés le seuil d'au moins 8 %, les quatre secteurs, le premier tour des dernières élections des titulaires, l'indifférence au nombre de votants, le champ de moins de onze salariés et la périodicité de quatre ans. Les renvois à L. 2121-1 et L. 2122-6 ont été vérifiés ; la composante agricole demeure soumise au régime spécial de ce dernier article.",
    },
    "L2122-10": {
        "proposed_xml": "<p>Une confédération syndicale catégorielle interprofessionnelle nationale est représentative à l'égard des personnels des collèges électoraux dans lesquels ses règles statutaires lui donnent vocation à présenter des candidats si elle remplit les conditions suivantes :</p><p>1° Elle satisfait aux critères de l'article L. 2121-1 et du 2° de l'article L. 2122-9 ;</p><p>2° Elle a recueilli au moins 8 % des suffrages exprimés dans ces collèges, calculés en additionnant les résultats mentionnés au 3° de l'article L. 2122-9.</p>",
        "reason": "Réécriture à droit constant : les conditions sont formulées avec la confédération pour sujet et le calcul du seuil est explicité. Aucune réforme de fond du régime catégoriel n'est introduite.",
        "review_notes": "Les deux subdivisions et leurs renvois sont maintenus. Le seuil de 8 % reste calculé dans les seuls collèges correspondant à la vocation statutaire ; il n'est pas calculé sur l'ensemble des personnels.",
    },
    "L2122-10-1": {
        "proposed_xml": "<p>Un scrutin régional est organisé tous les quatre ans pour mesurer l'audience des organisations syndicales auprès des salariés des entreprises de moins de onze salariés. Les salariés relevant des branches mentionnées à l'article L. 2122-6 sont exclus de ce scrutin. Un décret fixe la période pendant laquelle le scrutin se déroule.</p>",
        "reason": "Réécriture à droit constant : l'objet du scrutin, l'exclusion agricole et la fixation de sa période sont exprimés en trois phrases. Aucune réforme de fond du champ ou du calendrier n'est appliquée.",
        "review_notes": "Sont maintenus le niveau régional, la périodicité de quatre ans, le seuil de moins de onze salariés et la fixation de la période par décret simple. Le renvoi à L. 2122-6 et l'exclusion des salariés relevant de ces branches sont conservés, en cohérence avec R. 2122-8.",
    },
    "L2122-10-2": {
        "proposed_xml": "<p>Pour être électeurs, les salariés des entreprises qui emploient moins de onze salariés au 31 décembre de l'année précédant le scrutin doivent être titulaires d'un contrat de travail au cours de ce même mois de décembre et être âgés de seize ans révolus. Ils ne doivent faire l'objet d'aucune interdiction, déchéance ou incapacité relative à leurs droits civiques.</p>",
        "reason": "Réécriture à droit constant : les conditions d'électorat sont présentées comme des exigences cumulatives et la condition relative aux droits civiques est isolée dans une phrase. Aucune réforme de fond n'est introduite.",
        "review_notes": "Le seuil de moins de onze salariés s'apprécie au 31 décembre de l'année précédant le scrutin ; la détention du contrat reste exigée au cours de ce mois, sans ajouter une présence au seul 31 décembre. L'âge de seize ans révolus et les trois empêchements civiques sont maintenus. La source ne précise pas ici la date d'appréciation de l'âge ; aucune date supplémentaire n'est ajoutée.",
    },
    "L2122-10-3": {
        "proposed_xml": "<p>Les caisses de sécurité sociale communiquent aux services du ministre chargé du travail, par dérogation à leurs obligations de secret professionnel, les données relatives aux entreprises employant un ou plusieurs salariés ainsi que les données relatives à ces salariés figurant sur les déclarations sociales et nécessaires à l'établissement de la liste électorale.</p>",
        "reason": "Réécriture à droit constant : les caisses et le destinataire de la transmission sont placés en tête de phrase, tout en maintenant la dérogation au secret professionnel et la finalité électorale. Aucune réforme de fond de l'accès aux données n'est appliquée.",
        "review_notes": "La transmission reste limitée au dispositif de constitution de la liste électorale, sans nouveau destinataire ni nouvelle finalité. Le champ des entreprises employant un ou plusieurs salariés est conservé ; il n'est pas remplacé par un seuil de moins de onze salariés. Les qualifications relatives aux déclarations sociales et à la nécessité des données sont maintenues.",
    },
    "L2122-10-4": {
        "proposed_xml": "<p>L'autorité compétente de l'Etat établit la liste électorale. Les électeurs sont répartis entre deux collèges, l'un « cadres » et l'autre « non cadres ». Leur inscription dans l'un de ces collèges dépend des informations sur leur affiliation à une institution de retraite complémentaire figurant dans les déclarations sociales des entreprises, selon les conditions fixées par décret en Conseil d'Etat.</p>",
        "reason": "Réécriture à droit constant : la compétence de l'Etat, les deux collèges et la règle d'inscription sont distingués en trois phrases dans le même alinéa. Aucune réforme de fond du classement électoral n'est introduite.",
        "review_notes": "Les deux collèges, le critère d'affiliation à une institution de retraite complémentaire et le décret en Conseil d'Etat sont conservés. La mise en œuvre de ce critère doit être contrôlée avec les affiliations nommément mentionnées aux articles R. 2122-10 et R. 2122-12 du corpus ; aucun critère professionnel nouveau ne leur est substitué.",
    },
    "L2122-10-5": {
        "proposed_xml": "<p>Tout électeur peut contester une inscription sur la liste électorale devant le juge judiciaire, lui-même ou par l'intermédiaire d'un représentant qu'il a désigné, dans les conditions fixées par décret en Conseil d'Etat.</p><p>Le juge saisi vérifie que les électeurs concernés par la contestation remplissent les conditions prévues aux articles L. 2122-10-2 et L. 2122-10-4.</p>",
        "reason": "Réécriture à droit constant : la faculté de contestation, la représentation de l'électeur et le contrôle du juge sont formulés directement. Aucune réforme de fond du recours n'est introduite.",
        "review_notes": "Les deux alinéas de fond sont conservés. Le recours porte toujours sur une inscription, sans restriction à l'inscription du seul requérant. La compétence judiciaire, la désignation du représentant, les deux renvois et le décret en Conseil d'Etat sont maintenus.",
    },
    "L2122-10-6": {
        "proposed_xml": "<p>Les organisations syndicales de salariés déclarent leur candidature auprès des services du ministre chargé du travail si elles satisfont aux critères de respect des valeurs républicaines, d'indépendance et de transparence financière, sont légalement constituées depuis au moins deux ans et ont, selon leurs statuts, vocation à être présentes dans le champ géographique concerné. Les syndicats affiliés à une organisation syndicale représentative au niveau national et interprofessionnel déclarent également leur candidature auprès de ces services. Les conditions de ces déclarations sont fixées par décret en Conseil d'Etat.</p>",
        "reason": "Réécriture à droit constant : les deux catégories pouvant déclarer une candidature sont distinguées dans des phrases séparées au sein du même alinéa. Aucune réforme de fond des conditions de candidature n'est opérée.",
        "review_notes": "Les trois critères, la constitution légale depuis au moins deux ans et la vocation géographique statutaire restent cumulés pour la première catégorie. La seconde voie d'accès, fondée sur l'affiliation à une organisation représentative nationale et interprofessionnelle, est conservée sans lui ajouter les conditions de la première. Aucun point de départ nouveau de l'ancienneté n'est créé.",
    },
    "L2122-10-7": {
        "proposed_xml": "<p>Le scrutin se déroule par voie électronique et par correspondance. L'employeur qui ne dispose pas du matériel informatique nécessaire au vote électronique n'est pas tenu de le mettre à la disposition des salariés.</p><p>Un décret en Conseil d'Etat fixe les conditions de déroulement du scrutin et de confidentialité du vote. Il précise aussi les modalités de l'information donnée aux salariés.</p>",
        "reason": "Réécriture à droit constant : l'exception concernant le matériel est rattachée explicitement à l'employeur qui n'en dispose pas et le rôle du décret est formulé directement. Aucune réforme de fond des modalités de vote n'est appliquée.",
        "review_notes": "Les deux alinéas de fond, les deux voies de vote et la confidentialité sont maintenus. L'absence d'obligation de fournir du matériel reste conditionnée à son indisponibilité chez l'employeur ; aucune dispense générale ni obligation nouvelle d'achat n'est ajoutée. Le décret reste un décret en Conseil d'Etat.",
    },
    "L2122-10-8": {
        "proposed_xml": "<p>Les opérations électorales sont soumises aux règles prévues aux articles L. 10 et L. 67 du code électoral.</p>",
        "reason": "Réécriture à droit constant : les opérations électorales deviennent le sujet de la phrase, sans modification de la portée du renvoi. Aucune réforme de fond n'est introduite.",
        "review_notes": "Les deux références au code électoral sont conservées exactement. Ce code se situe hors du corpus public fourni ; le contenu de ces dispositions n'a pas été vérifié ni remplacé par une formulation supposée équivalente.",
    },
    "L2122-10-9": {
        "proposed_xml": "<p>L'employeur accorde aux salariés le temps nécessaire pour voter depuis leur lieu de travail et garantit la confidentialité du vote. Si le vote intervient pendant les horaires de travail, le temps qui lui est consacré est considéré comme du temps de travail et payé à l'échéance normale.</p>",
        "reason": "Réécriture à droit constant : les obligations de l'employeur et la condition de rémunération du temps de vote sont énoncées directement. Aucune réforme de fond du temps de travail ou du salaire n'est introduite.",
        "review_notes": "Sont conservés le vote depuis le lieu de travail, le temps nécessaire, la confidentialité et le paiement à l'échéance normale. L'assimilation à du temps de travail reste subordonnée au vote pendant les horaires de travail ; elle n'est pas étendue au vote hors de ces horaires.",
    },
    "L2122-10-10": {
        "proposed_xml": "<p>L'employeur accorde aux salariés de son entreprise désignés, pour ce scrutin, comme assesseur, délégué ou mandataire des organisations syndicales candidates le temps nécessaire à l'exercice de leurs fonctions. Le temps effectivement consacré à ces fonctions pendant les horaires de travail, y compris hors de l'entreprise, est considéré comme du temps de travail et payé à l'échéance normale.</p><p>L'employeur ne peut sanctionner un salarié ni rompre son contrat de travail en raison de l'exercice des fonctions d'assesseur, de délégué ou de mandataire des organisations syndicales candidates.</p>",
        "reason": "Réécriture à droit constant : chaque fonction est identifiée comme ouvrant les garanties et l'interdiction de sanction ou de rupture est formulée comme une obligation de l'employeur. Aucune réforme de fond des protections syndicales n'est appliquée.",
        "review_notes": "Les deux alinéas sont maintenus. L'énumération des fonctions est exprimée avec « ou » pour rendre explicite la protection attachée à chacune, sans exiger leur cumul. Le temps nécessaire reste distinct du temps effectivement exercé pendant les horaires de travail, seul assimilé ici à du temps de travail payé ; l'exercice hors de l'entreprise et l'échéance normale sont conservés.",
    },
    "L2122-10-11": {
        "proposed_xml": "<p>Le juge judiciaire est compétent pour connaître des contestations portant sur le déroulement des opérations électorales, dans les conditions fixées par décret en Conseil d'Etat.</p>",
        "reason": "Réécriture à droit constant : la juridiction compétente est placée en sujet et l'objet de sa compétence est exprimé directement. Aucune réforme de fond du contentieux électoral n'est introduite.",
        "review_notes": "Le champ demeure le déroulement des opérations électorales. La compétence judiciaire et le décret en Conseil d'Etat sont conservés ; aucune condition de recevabilité ou de délai n'est ajoutée.",
    },
    "L2122-11": {
        "proposed_xml": "<p>Le ministre chargé du travail, après avis du Haut Conseil du dialogue social, arrête la liste des organisations syndicales reconnues représentatives dans chaque branche professionnelle et des organisations syndicales reconnues représentatives au niveau national et interprofessionnel, en application des articles L. 2122-5 à L. 2122-10.</p><p>Le Haut Conseil du dialogue social réunit des représentants des organisations d'employeurs représentatives au niveau national, des représentants des organisations syndicales de salariés nationales et interprofessionnelles, des représentants du ministre chargé du travail et des personnalités qualifiées.</p><p>Un décret en Conseil d'Etat fixe les modalités d'organisation et de fonctionnement du Haut Conseil.</p>",
        "reason": "Réécriture à droit constant : la compétence du ministre est mise en tête, les deux niveaux de représentativité restent distingués et le Haut Conseil est nommé dans l'alinéa relatif au décret. Aucune réforme de fond de la reconnaissance ou de la composition n'est introduite.",
        "review_notes": "Les trois alinéas et le renvoi aux articles L. 2122-5 à L. 2122-10 restent à leur place. L'avis du Haut Conseil demeure préalable, sans être transformé en avis conforme. Pour sa composition, la représentativité nationale expressément exigée des organisations d'employeurs n'est pas ajoutée à la qualification des organisations de salariés figurant dans la source.",
    },
    "L2122-12": {
        "proposed_xml": "<p>Pour l'application du présent chapitre, les résultats des élections professionnelles sont recueillis et consolidés selon les modalités fixées par décret.</p>",
        "reason": "Réécriture à droit constant : le recueil et la consolidation sont formulés comme les opérations encadrées par le décret. Aucune réforme de fond du calcul de l'audience n'est appliquée.",
        "review_notes": "Les deux opérations et le champ du présent chapitre sont conservés. Le texte renvoie toujours à un décret simple ; aucune exigence de décret en Conseil d'Etat ni méthode de calcul nouvelle n'est ajoutée.",
    },
    "L2122-13": {
        "proposed_xml": "<p>Le ministre chargé du travail présente au Haut Conseil du dialogue social les modalités d'organisation retenues pour le scrutin prévu à l'article L. 2122-10-1. Cette présentation intervient avant l'ouverture du scrutin.</p>",
        "reason": "Réécriture à droit constant : l'obligation de présentation et son échéance sont formulées en deux phrases au sein du même alinéa. Aucune réforme de fond de la procédure n'est introduite.",
        "review_notes": "Le destinataire, le renvoi à L. 2122-10-1 et l'antériorité par rapport à l'ouverture du scrutin sont conservés. La présentation n'est pas transformée en demande d'avis ou d'autorisation du Haut Conseil.",
    },
    "L2131-1": {
        "proposed_xml": "<p>Les syndicats professionnels ont pour objet exclusif d'étudier et de défendre les droits ainsi que les intérêts matériels et moraux, collectifs comme individuels, des personnes mentionnées dans leurs statuts.</p>",
        "reason": "Réécriture à droit constant : les substantifs « étude » et « défense » sont remplacés par des verbes, sans modifier l'objet exclusif des syndicats. Aucune réforme de fond des libertés collectives n'est introduite.",
        "review_notes": "L'exclusivité de l'objet, les droits, les intérêts matériels et moraux, leurs dimensions collective et individuelle et le périmètre statutaire des personnes sont conservés. Les seuls sauts de ligne de présentation sont normalisés en un paragraphe.",
    },
    "L2131-2": {
        "proposed_xml": "<p>Les personnes exerçant la même profession, des métiers similaires, des métiers connexes concourant à l'établissement de produits déterminés ou la même profession libérale peuvent librement constituer des syndicats ou des associations professionnels.</p><p>Par dérogation au premier alinéa, les particuliers qui occupent des employés de maison peuvent se grouper en syndicat pour défendre les intérêts qu'ils ont en commun en qualité d'employeurs de ces salariés.</p>",
        "reason": "Réécriture à droit constant : les personnes pouvant constituer le groupement deviennent le sujet de la première phrase et la dérogation est rattachée explicitement au premier alinéa. Aucune réforme de fond du droit de constitution n'est appliquée.",
        "review_notes": "Les deux alinéas sont conservés, avec les quatre catégories professionnelles et la condition propre aux métiers connexes. La dérogation demeure réservée aux particuliers employant des employés de maison et à leurs intérêts communs d'employeurs ; elle n'est pas étendue aux associations ni à d'autres employeurs.",
    },
    "L2131-3": {
        "proposed_xml": "<p>Les fondateurs de tout syndicat professionnel déposent ses statuts ainsi que les noms des personnes chargées, à quelque titre que ce soit, de son administration ou de sa direction.</p><p>Ce dépôt doit être renouvelé en cas de changement de la direction ou de modification des statuts.</p>",
        "reason": "Réécriture à droit constant : les personnes dont le nom doit être déposé sont désignées plus directement et l'obligation de renouveler le dépôt est explicite. Aucune réforme de fond des formalités de constitution n'est introduite.",
        "review_notes": "Les deux alinéas sont maintenus. Le premier vise l'administration et la direction, à quelque titre que ce soit ; le second ne mentionne, dans la source, que le changement de direction ou des statuts. Cette dissymétrie est conservée et doit être contrôlée, sans ajouter un cas de renouvellement. R. 2131-1 précise le lieu de dépôt des statuts ; il n'est pas incorporé dans cet article.",
    },
    "L2131-4": {
        "proposed_xml": "<p>Tout adhérent d'un syndicat professionnel qui remplit les conditions prévues à l'article L. 2131-5 peut accéder aux fonctions d'administration ou de direction de ce syndicat.</p>",
        "reason": "Réécriture à droit constant : la condition d'accès est intégrée directement au sujet et les fonctions sont rattachées explicitement au syndicat d'adhésion. Aucune réforme de fond de l'accès à ces fonctions n'est introduite.",
        "review_notes": "Le renvoi à L. 2131-5 est conservé et vérifié dans le lot. Il n'est ajouté aucune condition de nationalité ou d'âge dans le présent article, ni aucune procédure de nomination ; les deux catégories de fonctions sont maintenues.",
    },
    "L2131-5": {
        "proposed_xml": "<p>Tout membre français d'un syndicat professionnel qui est chargé de son administration ou de sa direction doit jouir de ses droits civiques. Il ne doit faire l'objet d'aucune interdiction, déchéance ou incapacité relative à ces droits.</p><p>Tout ressortissant étranger adhérent à un syndicat peut accéder aux fonctions d'administration ou de direction de ce syndicat s'il est âgé de dix-huit ans accomplis et remplit les mêmes conditions relatives aux droits civiques.</p>",
        "reason": "Réécriture à droit constant : les exigences civiques sont réparties en deux phrases et les conditions propres au ressortissant étranger sont énoncées directement. Aucune réforme de fond des conditions personnelles n'est appliquée.",
        "review_notes": "Les deux alinéas et la distinction entre membres français et ressortissants étrangers sont conservés. L'âge de dix-huit ans accomplis reste dans le seul second alinéa. Le renvoi de ce second alinéa aux mêmes conditions civiques est maintenu, sans supposer l'existence de droits politiques français ni remplacer silencieusement cette formulation par une autre condition de capacité.",
    },
    "L2131-6": {
        "proposed_xml": "<p>Lorsque le syndicat est dissous volontairement, en application de ses statuts ou par décision de justice, ses biens sont dévolus selon les dispositions de ses statuts. A défaut de dispositions statutaires, ils sont dévolus selon les règles fixées par l'assemblée générale.</p><p>Les biens du syndicat ne peuvent en aucun cas être répartis entre ses membres adhérents.</p>",
        "reason": "Réécriture à droit constant : les trois formes de dissolution et l'ordre d'application des règles de dévolution sont exprimés en phrases plus courtes. Aucune réforme de fond du patrimoine syndical n'est introduite.",
        "review_notes": "Les deux alinéas sont maintenus. Le rôle subsidiaire de l'assemblée générale, en l'absence de dispositions statutaires, et l'interdiction absolue de répartition entre membres adhérents restent inchangés. Aucun bénéficiaire de la dévolution n'est ajouté.",
    },
}


def main():
    sources = json.loads(Path("source.json").read_text())
    assert len(sources) == 24
    assert set(DRAFTS) == {source["number"] for source in sources}
    result = []
    for source in sources:
        article = {
            key: source[key]
            for key in ("code_id", "source_id", "source_sha256", "number")
        }
        article.update(DRAFTS[source["number"]])
        article["status"] = "rewrite_draft"
        result.append(article)
    Path("answer.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    )


if __name__ == "__main__":
    main()
