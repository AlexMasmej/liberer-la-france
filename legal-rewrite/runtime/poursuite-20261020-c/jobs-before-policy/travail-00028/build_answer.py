import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
drafts = {}


def add(number, paragraphs, reason, review_notes):
    assert number not in drafts
    drafts[number] = {
        'proposed_xml': '\n'.join(f'<p>{p}</p>' for p in paragraphs),
        'reason': reason,
        'review_notes': review_notes,
    }


add('L2132-1', [
    "Chaque syndicat professionnel est doté de la personnalité civile.",
],
    "Réécriture à droit constant : la règle est formulée au singulier pour exprimer directement l'attribution de la personnalité civile à chaque syndicat professionnel. Aucune réforme de fond prévue par policy.json ne porte sur cette attribution.",
    "La personnalité civile reste attachée aux syndicats professionnels, sans condition supplémentaire. Aucun renvoi ni chiffre à coordonner."
)

add('L2132-2', [
    "Seules les organisations de salariés constituées en syndicats professionnels sont admises à négocier les conventions et accords collectifs de travail.",
    "Toute convention ou tout accord portant sur les conditions collectives du travail est conclu selon les conditions fixées au livre II.",
],
    "Réécriture à droit constant : l'exclusivité de la négociation est placée en tête de phrase et le second alinéa identifie plus simplement les textes soumis aux conditions du livre II. Aucune réforme de fond n'est appliquée aux règles de capacité syndicale.",
    "Les deux alinéas et le renvoi au livre II sont conservés. La portée générale de l'exclusivité énoncée au premier alinéa doit être articulée avec les dispositifs particuliers de négociation prévus par ce livre ; aucune dérogation n'est créée ni supprimée ici."
)

add('L2132-3', [
    "Les syndicats professionnels peuvent agir en justice.",
    "Devant toutes les juridictions, ils peuvent exercer l'ensemble des droits réservés à la partie civile pour les faits qui portent un préjudice direct ou indirect à l'intérêt collectif de la profession qu'ils représentent.",
],
    "Réécriture à droit constant : le droit d'action est exprimé par un verbe direct et le second alinéa distingue le cadre juridictionnel, les droits exercés et l'intérêt collectif protégé. Aucune modification de fond de la qualité pour agir n'est prévue par la réforme.",
    "Conservation des deux alinéas, de toutes les juridictions, de tous les droits réservés à la partie civile et du préjudice direct ou indirect à l'intérêt collectif de la profession représentée."
)

add('L2132-4', [
    "Les biens meubles et immeubles dont les syndicats professionnels ont besoin pour leurs réunions, leurs bibliothèques et leurs formations ne peuvent être saisis.",
],
    "Réécriture à droit constant : l'insaisissabilité est exprimée comme une interdiction de saisie et les trois usages protégés sont rattachés explicitement aux syndicats. Aucune réforme de fond ne concerne ces biens.",
    "Le critère de nécessité et les trois affectations, réunions, bibliothèques et formations, sont maintenus. L'insaisissabilité n'est pas étendue aux autres biens syndicaux."
)

add('L2132-5', [
    "Les syndicats professionnels disposent des facultés suivantes :",
    "1° Créer et administrer des centres d'information consacrés aux offres et aux demandes d'emploi ;",
    "2° Créer, administrer et subventionner des institutions professionnelles de prévoyance ainsi que des organismes d'éducation, de formation, de vulgarisation ou de recherche, dans les domaines qui intéressent la profession ;",
    "3° Subventionner des sociétés coopératives de production ou de consommation ; financer la création d'habitations à loyer modéré ou l'acquisition de terrains destinés à la réalisation de jardins ouvriers ou à l'exercice d'activités physiques et sportives.",
],
    "Réécriture à droit constant : les pouvoirs sont présentés comme des facultés, les objets des centres d'information sont précisés et un point-virgule distingue, au 3°, les subventions des financements. Les trois subdivisions et tous leurs objets sont conservés ; aucune réforme de fond n'est appliquée.",
    "Conserver les 1° à 3° et l'ensemble des objets autorisés, notamment la vulgarisation, la prévoyance, les coopératives de consommation, les habitations à loyer modéré et les deux destinations des terrains. La rédaction ne crée aucune obligation de financer ces activités."
)

add('L2132-6', [
    "Les syndicats professionnels peuvent créer, entre leurs membres, des caisses spéciales de secours mutuels et de retraites.",
    "Les fonds de ces caisses ne peuvent être saisis, dans les limites fixées par le code de la mutualité.",
    "Une personne qui se retire d'un syndicat conserve le droit d'appartenir aux sociétés de secours mutuels et de retraite pour la vieillesse à l'actif desquelles elle a contribué par des cotisations ou des versements de fonds.",
],
    "Réécriture à droit constant : les facultés de création, la protection des fonds et le droit conservé après le départ du syndicat sont exprimés séparément avec des verbes directs. Le régime de ces caisses n'est pas assimilé au compte de retraite envisagé par policy.json ; aucune réforme de fond ne leur est appliquée.",
    "Les trois alinéas sont maintenus. L'insaisissabilité demeure limitée par le code de la mutualité ; le maintien du droit d'appartenance demeure lié à une contribution à l'actif par cotisations ou versements. La réforme de la retraite des salariés privés ne justifie aucune extension à ces caisses distinctes."
)

add('L2133-1', [
    "Les syndicats professionnels régulièrement constitués peuvent se concerter pour étudier et défendre leurs intérêts matériels et moraux.",
],
    "Réécriture à droit constant : les substantifs désignant l'étude et la défense sont remplacés par des verbes qui énoncent directement l'objet de la concertation. La constitution régulière et les deux catégories d'intérêts sont maintenues ; aucune réforme de fond n'est appliquée.",
    "Le droit de concertation reste réservé aux syndicats professionnels régulièrement constitués et porte sur leurs intérêts matériels et moraux."
)

add('L2133-2', [
    "Les dispositions des articles L. 2131-1, L. 2131-3 à L. 2131-5, L. 2141-1 et L. 2141-2 s'appliquent aux unions de syndicats.",
    "Chaque union fait connaître le nom et le siège social de chacun des syndicats qui la composent.",
    "Les statuts de l'union fixent les règles de représentation des syndicats adhérents au sein du conseil d'administration et des assemblées générales.",
],
    "Réécriture à droit constant : les règles applicables sont annoncées directement, puis l'obligation d'information et le rôle des statuts sont rattachés explicitement à l'union. Aucun changement de fond n'est apporté au régime des unions.",
    "Les trois alinéas et tous les renvois sont conservés, y compris la plage L. 2131-3 à L. 2131-5. La représentation statutaire concerne à la fois le conseil d'administration et les assemblées générales."
)

add('L2133-3', [
    "Les unions de syndicats disposent de l'ensemble des droits que le présent titre confère aux syndicats professionnels.",
],
    "Réécriture à droit constant : une proposition relative identifie plus directement l'origine des droits reconnus aux unions, sans en modifier l'étendue. Aucune réforme de fond ne concerne cette équivalence de droits.",
    "Le renvoi porte toujours sur l'ensemble des droits du présent titre, sans restriction ni extension à d'autres titres."
)

add('L2134-1', [
    "Pour déposer leurs marques ou labels, les syndicats professionnels accomplissent les formalités prévues aux articles L. 712-1 et suivants du code de la propriété intellectuelle. Après ce dépôt, ils peuvent en revendiquer la propriété exclusive dans les conditions fixées par ce code.",
    "Les marques ou labels peuvent être apposés sur tout produit ou objet de commerce afin d'en certifier les conditions de fabrication. Toute personne physique ou entreprise qui commercialise ces produits peut les utiliser.",
],
    "Réécriture à droit constant : les formalités du dépôt et la possibilité de revendiquer la propriété exclusive sont présentées dans leur ordre logique ; la dernière phrase désigne directement les utilisateurs. Aucune réforme de fond n'est appliquée au droit des marques syndicales.",
    "Les deux alinéas sont conservés. Les articles L. 712-1 et suivants du code de la propriété intellectuelle, les conditions de propriété exclusive, la certification des conditions de fabrication et le champ des utilisateurs restent inchangés en portée."
)

add('L2134-2', [
    "L'utilisation des marques syndicales ou des labels doit respecter les dispositions des articles L. 2141-5 à L. 2141-8.",
    "Est nul tout accord ou toute disposition qui tend à obliger l'employeur à embaucher ou à conserver à son service uniquement des adhérents du syndicat propriétaire de la marque ou du label.",
],
    "Réécriture à droit constant : l'interdiction de porter atteinte aux garanties citées devient une obligation explicite de les respecter ; la nullité est placée en tête du second alinéa. Les protections de la liberté syndicale sont conservées, sans réforme de fond.",
    "Maintien des deux alinéas, de la plage L. 2141-5 à L. 2141-8 et de la nullité des stipulations tendant à imposer une exclusivité syndicale tant à l'embauche que pour le maintien dans l'emploi."
)

add('L2135-1', [
    "Les syndicats professionnels et leurs unions mentionnés aux articles L. 2131-2, L. 2133-1 et L. 2133-2, relatifs à la création de syndicats professionnels, ainsi que les associations de salariés ou d'employeurs régies par la loi du 1er juillet 1901 relative au contrat d'association ou, dans les départements de la Moselle, du Bas-Rhin et du Haut-Rhin, par le droit local, doivent respecter les obligations comptables définies à l'article L. 123-12 du code de commerce. Lorsque leurs ressources annuelles ne dépassent pas un seuil fixé par décret, ces organisations peuvent présenter leurs comptes sous une forme simplifiée. Dans ce cadre, elles peuvent n'enregistrer leurs créances et leurs dettes qu'à la clôture de l'exercice. Lorsque leurs ressources annuelles ne dépassent pas un second seuil fixé par décret, elles peuvent tenir un livre qui enregistre, dans l'ordre chronologique, l'ensemble des mouvements de leur patrimoine. Un décret fixe les conditions d'application du présent article.",
],
    "Réécriture à droit constant : l'obligation comptable, les deux facultés liées aux seuils et le décret d'application sont formulés avec des sujets et verbes explicites. L'alinéa unique est maintenu ; aucune réforme de fond ni aucun montant de seuil n'est introduit.",
    "Conserver le champ des syndicats, unions et associations, le droit local des trois départements, la référence à la loi du 1er juillet 1901 et l'article L. 123-12 du code de commerce. Les deux seuils réglementaires, la comparaison inclusive et la possibilité d'enregistrement à la clôture restent distincts."
)

add('L2135-2', [
    "Les syndicats professionnels, leurs unions et les associations de salariés ou d'employeurs mentionnés à l'article L. 2135-1 qui contrôlent une ou plusieurs personnes morales au sens de l'article L. 233-16 du code de commerce, sans lien d'adhésion ou d'affiliation avec celles-ci, doivent choisir entre les deux modalités suivantes, dans les conditions fixées par un décret pris après avis de l'Autorité des normes comptables :",
    "a) Établir des comptes consolidés. L'article L. 821-41 du code de commerce ne s'applique pas lorsque les ressources de l'ensemble formé par ces syndicats, unions ou associations et les personnes morales qu'ils contrôlent ne dépassent pas, à la clôture d'un exercice, le seuil mentionné à l'article L. 2135-6 du présent code ;",
    "b) Joindre en annexe à leurs propres comptes les comptes des personnes morales qu'ils contrôlent et une information sur la nature du lien de contrôle. Les comptes de ces personnes morales doivent alors avoir fait l'objet d'un contrôle légal. Ce contrôle n'est toutefois pas exigé lorsque les ressources de l'ensemble formé par les syndicats, unions ou associations et les personnes morales qu'ils contrôlent ne dépassent pas, à la clôture d'un exercice, le seuil mentionné au même article L. 2135-6.",
],
    "Réécriture à droit constant : l'obligation est présentée comme un choix entre consolidation et annexion des comptes ; au b), l'exigence de contrôle légal et son exception sont séparées en deux phrases. Les trois alinéas, les lettres et les conditions de seuil sont conservés. Aucune réforme de fond n'est appliquée.",
    "Les liens de contrôle sans adhésion ni affiliation restent le critère d'application ; ne pas confondre ce régime avec les comptes combinés de L. 2135-3. Les seuils sont appréciés sur l'ensemble contrôlé, à la clôture d'un exercice, avec inclusion de l'égalité. Renvois L. 233-16, L. 821-41 du code de commerce et L. 2135-6 conservés. La note source fixe l'entrée en vigueur au 1er janvier 2024 en application de l'article 32 de l'ordonnance n° 2023-1142 ; il ne s'agit pas d'une date de réforme nouvelle."
)

add('L2135-3', [
    "Lorsque leurs statuts le prévoient, les syndicats professionnels de salariés ou d'employeurs, leurs unions et les associations de salariés ou d'employeurs mentionnés à l'article L. 2135-1 peuvent établir des comptes combinés. Ces comptes intègrent la comptabilité des personnes morales et des entités avec lesquelles ces organisations ont des liens d'adhésion ou d'affiliation. Un décret pris après avis de l'Autorité des normes comptables fixe les conditions de cette combinaison.",
],
    "Réécriture à droit constant : la condition statutaire est placée en tête et la phrase unique est décomposée pour distinguer la faculté, le périmètre des comptes et les modalités réglementaires, sans créer d'alinéa supplémentaire. Aucune réforme de fond n'est appliquée.",
    "Conservation du renvoi à L. 2135-1, du caractère facultatif et de l'avis préalable de l'Autorité des normes comptables. La note de l'article 15 de la loi n° 2008-789 du 20 août 2008, publiée au JORF du 21 août 2008, rend les obligations de L. 2135-1 à L. 2135-3 applicables à compter de l'exercice comptable 2009 ; cette application historique est préservée."
)

add('L2135-4', [
    "L'organe chargé de la direction arrête les comptes. L'assemblée générale des adhérents ou un organe collégial de contrôle désigné par les statuts les approuve.",
],
    "Réécriture à droit constant : deux phrases actives distinguent l'organe qui arrête les comptes de celui qui les approuve, dans le même alinéa. L'alternative entre les deux organes d'approbation reste entière ; aucune réforme de fond n'est appliquée.",
    "La désignation statutaire reste attachée à l'organe collégial de contrôle. La note issue de l'article 15 de la loi n° 2008-789 du 20 août 2008, JORF du 21 août 2008, prévoit l'application de L. 2135-4 aux organisations de L. 2135-1 à compter de l'exercice 2010 aux niveaux confédéral et fédéral, de l'exercice 2011 aux niveaux régional et départemental et de l'exercice 2012 à tous les niveaux. Cette progression historique n'est pas une transition à créer pour la présente réécriture."
)

add('L2135-5', [
    "Les syndicats professionnels de salariés ou d'employeurs, leurs unions et les associations de salariés ou d'employeurs mentionnés à l'article L. 2135-1 qui sont tenus d'établir des comptes doivent en assurer la publicité. Un décret pris après avis de l'Autorité des normes comptables fixe les conditions de cette publicité.",
    "Le syndicat ou l'association qui combine les comptes des organisations mentionnées à l'article L. 2135-3 est soumis au premier alinéa. Les organisations dont les comptes sont ainsi combinés sont alors dispensées de l'obligation de publicité.",
],
    "Réécriture à droit constant : la publicité obligatoire et ses modalités sont énoncées dans deux phrases ; le second alinéa identifie explicitement l'organisme publiant les comptes combinés et les organisations dispensées. Aucune réforme de fond n'est appliquée.",
    "Les deux alinéas, les renvois à L. 2135-1 et L. 2135-3, l'avis de l'Autorité des normes comptables et la dispense de publicité pour les seules organisations dont les comptes sont combinés sont conservés."
)

add('L2135-6', [
    "Les syndicats professionnels d'employeurs, leurs unions et les associations d'employeurs mentionnés à l'article L. 2135-1 qui souhaitent établir leur représentativité sur le fondement du titre V du présent livre Ier doivent nommer au moins un commissaire aux comptes. Ils doivent également nommer un suppléant lorsque les conditions définies au troisième alinéa du I de l'article L. 821-40 sont réunies.",
    "L'obligation prévue au premier alinéa s'applique aussi, lorsque leurs ressources dépassent un seuil fixé par décret, aux syndicats professionnels de salariés, à leurs unions, aux associations de salariés mentionnées au même article L. 2135-1, ainsi qu'aux syndicats professionnels d'employeurs, à leurs unions et aux associations d'employeurs autres que ceux mentionnés au premier alinéa du présent article.",
],
    "Réécriture à droit constant : les nominations du commissaire et du suppléant sont distinguées ; le second alinéa place en tête la condition de ressources applicable aux autres organisations. Les deux alinéas sont maintenus. Aucune réforme de fond des obligations de certification n'est appliquée.",
    "Le premier alinéa reste sans condition de ressources pour les organisations patronales cherchant à établir leur représentativité ; le second conserve un dépassement strict du seuil. Le renvoi au troisième alinéa du I de L. 821-40 ne précise pas le code dans la source : il est conservé et son rattachement au code de commerce doit être confirmé, sans correction silencieuse. La note de l'article 32 de l'ordonnance n° 2023-1142 fixe l'entrée en vigueur au 1er janvier 2024."
)

add('L2135-7', [
    "Un salarié peut, avec son accord exprès, être mis à la disposition d'une organisation syndicale ou d'une association d'employeurs mentionnée à l'article L. 2231-1, dans les conditions prévues à l'article L. 2135-8.",
    "Pendant la mise à disposition, l'employeur reste tenu de ses obligations envers le salarié. La convention ou l'accord prévu à l'article L. 2135-8 doit notamment prévoir des aménagements permettant à l'employeur de respecter l'obligation de formation d'adaptation définie à l'article L. 6321-1.",
    "Les indemnités de fonction que l'organisation syndicale verse, le cas échéant, sont assimilées à des salaires. L'organisation syndicale acquitte les cotisations et charges correspondantes.",
    "À la fin de la mise à disposition, le salarié retrouve son précédent emploi ou un emploi similaire assorti d'une rémunération au moins équivalente.",
],
    "Réécriture à droit constant : les sujets de l'accord, des obligations maintenues et du paiement des cotisations sont explicités ; la règle de retour à l'emploi conserve son alinéa. Aucune réforme de fond du régime de mise à disposition n'est appliquée.",
    "Les quatre alinéas et les renvois à L. 2231-1, L. 2135-8 et L. 6321-1 sont maintenus. L'accord exprès, l'assimilation salariale des indemnités éventuelles et la rémunération au moins équivalente sont conservés. Le troisième alinéa ne vise, comme la source, que les indemnités payées par l'organisation syndicale ; aucune extension aux associations d'employeurs n'est déduite."
)

add('L2135-8', [
    "Les conditions de mise à disposition de salariés auprès d'organisations syndicales ou d'associations d'employeurs sont fixées par une convention collective étendue, un accord collectif de branche étendu ou un accord d'entreprise.",
],
    "Réécriture à droit constant : la phrase désigne directement l'objet de la négociation et énumère séparément les trois instruments collectifs habilités, en rendant explicite l'exigence d'extension de la convention collective et de l'accord de branche. Aucune réforme de fond n'est appliquée.",
    "L'extension est exigée pour la convention collective et l'accord de branche, sans être ajoutée à l'accord d'entreprise. Aucun niveau de négociation non précisé par la source n'est ajouté à la convention collective. Coordination conservée avec les conditions individuelles de L. 2135-7."
)

add('L2135-9', [
    "Un accord conclu entre les organisations représentatives des salariés et des employeurs au niveau national et interprofessionnel crée un fonds paritaire chargé d'une mission de service public. Ce fonds contribue au financement des organisations syndicales de salariés et des organisations professionnelles d'employeurs au titre de leur participation à la conception, à la mise en œuvre, à l'évaluation ou au suivi d'activités concourant au développement et à l'exercice des missions définies à l'article L. 2135-11. L'accord fixe l'organisation et le fonctionnement du fonds conformément à la présente section.",
    "L'accord qui crée le fonds paritaire est soumis à l'agrément du ministre chargé du travail. En l'absence d'accord ou d'agrément, les modalités de création du fonds ainsi que ses conditions d'organisation et de fonctionnement sont fixées par voie réglementaire.",
    "Le fonds paritaire peut recevoir les ressources mentionnées à l'article L. 2135-10 et les attribuer aux organisations syndicales de salariés et aux organisations professionnelles d'employeurs dans les conditions prévues aux articles L. 2135-11 à L. 2135-17.",
],
    "Réécriture à droit constant : la longue phrase de création est divisée pour distinguer l'accord créateur, la mission de financement et les règles d'organisation. L'agrément et la voie réglementaire subsidiaire restent dans leur alinéa. Aucune réforme de fond du financement paritaire n'est prévue par policy.json.",
    "Les trois alinéas, la mission de service public, les quatre formes de participation aux activités, le niveau national et interprofessionnel et les renvois à L. 2135-10 ainsi qu'à L. 2135-11 à L. 2135-17 sont conservés. La création et l'agrément ne sont pas présentés comme de nouvelles formalités déclenchées par la réécriture."
)

add('L2135-10', [
    "I. ― Le fonds paritaire dispose des ressources suivantes :",
    "1° Une subvention de l'association paritaire gestionnaire du fonds mentionnée à l'article L. 2135-15, dans la limite du montant de la contribution mentionnée à l'article L. 2135-15-1 qu'elle perçoit ;",
    "2° Le cas échéant, une participation volontaire d'organismes à vocation nationale dont le champ d'intervention dépasse le cadre d'une ou de plusieurs branches professionnelles et qui sont gérés majoritairement par les organisations syndicales de salariés et les organisations professionnelles d'employeurs. L'accord mentionné au 1° fixe la liste des organismes qui peuvent participer au financement du fonds. En l'absence d'accord ou d'agrément de celui-ci, cette liste est fixée par décret ;",
    "3° Une subvention de l'État ;",
    "4° Le cas échéant, toute autre ressource prévue par des dispositions législatives ou réglementaires, par un accord conclu entre les organisations syndicales de salariés et les organisations professionnelles d'employeurs représentatives au niveau national et interprofessionnel, ou par un accord de branche étendu.",
    "II. ― (Abrogé) ;",
    "III. ― L'accord mentionné au 4° du I du présent article peut mandater des organisations syndicales de salariés et des organisations professionnelles d'employeurs représentatives au niveau de la branche pour conclure une convention avec les organismes mentionnés aux articles L. 225-1-1 du code de la sécurité sociale et L. 723-11 du code rural et de la pêche maritime. Cette convention confie aux organismes mentionnés au II de l'article L. 2135-15-1 le recouvrement de la contribution mentionnée au 4° du I. La contribution est alors versée à l'association gestionnaire du fonds paritaire mentionnée à l'article L. 2135-9 du présent code, qui la répartit entre les branches affectataires.",
    "La convention prévue au premier alinéa du présent III doit respecter les conditions suivantes :",
    "1° Elle prévoit :",
    "a) Un montant minimal de collecte de la contribution, fixé par arrêté ;",
    "b) Sa durée de mise en œuvre, qui est d'au moins huit ans ;",
    "c) Par dérogation aux trois derniers alinéas du 5° de l'article L. 225-1-1 du code de la sécurité sociale, des frais prélevés sur le rendement de la contribution qui correspondent aux coûts réels de mise en œuvre et de gestion de cette contribution. Ces frais sont majorés lorsque la convention est dénoncée avant l'expiration de la durée prévue au b du présent 1° ;",
    "d) Un délai de préavis lorsqu'une partie envisage de dénoncer l'accord. Ce délai doit être au moins égal à la moitié de la durée restant à courir de la convention et ne peut être inférieur à douze mois.",
    "Les b et c ne s'appliquent pas lorsque la branche concernée est engagée dans une procédure de restructuration des branches professionnelles en application des articles L. 2261-32 à L. 2261-34 ;",
    "2° La contribution faisant l'objet de la convention est :",
    "a) Assise sur les revenus d'activité retenus pour déterminer l'assiette définie à l'article L. 242-1 du code de la sécurité sociale et à l'article L. 741-10 du code rural et de la pêche maritime. Elle est calculée à un taux proportionnel, qui ne peut être modulé qu'en fonction de seuils d'effectifs définis par arrêté conjoint des ministres chargés de la sécurité sociale et du travail ou des éléments d'identification de la branche déclarés par l'employeur ;",
    "b) Due pour les périodes au titre desquelles les revenus sont attribués et déclarés mensuellement ;",
    "c) Recouvrée selon les règles et sous les garanties et les sanctions applicables aux cotisations et contributions de sécurité sociale ;",
    "d) Recouvrée à compter du début de l'année civile qui suit une période d'au moins six mois à compter de la signature de la convention, sans que le recouvrement puisse commencer avant le 1er janvier 2026.",
    "Un arrêté conjoint des ministres chargés de la sécurité sociale et du travail fixe le modèle de la convention prévue au premier alinéa du présent III.",
    "Un décret fixe la liste des informations relatives aux entreprises redevables que les organismes chargés du recouvrement communiquent à l'association gestionnaire du fonds paritaire.",
    "Une convention entre l'association gestionnaire du fonds paritaire mentionnée à l'article L. 2135-9 et l'institution mentionnée à l'article L. 6123-5 fixe les modalités de communication des données relatives aux entreprises redevables de la contribution mentionnée au 4° du I du présent article.",
],
    "Réécriture à droit constant : les ressources sont énumérées avec leurs auteurs explicites ; au III, le mandat, le recouvrement et l'affectation sont distingués en phrases successives. Les conditions de durée, de frais, de préavis, d'assiette et de transmission de données sont reformulées dans leurs alinéas d'origine. Les I à III, le II abrogé, les numéros et les lettres sont conservés. Aucune réforme de fond ni nouveau prélèvement n'est introduit.",
    "Incohérence préexistante : le 2° du I renvoie à « l'accord mentionné au 1° », alors que le 1° actuel ne mentionne plus d'accord ; renvoi conservé pour décision de coordination, sans le remplacer d'office par L. 2135-15-1. Au d du 1° du III, la source vise la dénonciation de « l'accord » tout en calculant le préavis sur la durée de la convention ; cette discordance est conservée et doit être contrôlée. Huit ans au minimum, préavis cumulant la moitié de la durée restante et douze mois au minimum, exclusion limitée aux b et c en cas de restructuration, six mois au minimum et borne du 1er janvier 2026 sont tous maintenus. Les trois derniers alinéas du 5° de L. 225-1-1 et tous les autres renvois restent identiques. L. 2135-15 et L. 2135-15-1 ont été consultés dans le corpus public pour distinguer l'association gestionnaire, le fonds et la contribution ; aucun de ces articles n'est modifié."
)

add('L2135-11', [
    "Le fonds paritaire participe au financement des activités suivantes, qui constituent des missions d'intérêt général pour les organisations syndicales de salariés et les organisations professionnelles d'employeurs concernées :",
    "1° La conception, la gestion, l'animation et l'évaluation des politiques menées paritairement. Le fonds y contribue au moyen de la subvention mentionnée au 1° du I de l'article L. 2135-10 et, le cas échéant, des participations volontaires versées en application du 2° du même I ;",
    "2° La participation des organisations syndicales de salariés et des organisations professionnelles d'employeurs à la conception, à la mise en œuvre et au suivi des politiques publiques relevant de la compétence de l'État, notamment par l'animation et la gestion d'organismes de recherche, la négociation, la consultation et la concertation. Le fonds y contribue au moyen de la subvention mentionnée au 3° du I de l'article L. 2135-10 ;",
    "3° La formation économique, sociale, environnementale et syndicale définie aux articles L. 2145-1 et L. 2145-2, destinée aux salariés appelés à exercer des fonctions syndicales ou aux adhérents à une organisation syndicale de salariés amenés à intervenir en faveur des salariés. Sont notamment visées l'indemnisation des salariés bénéficiant de congés de formation, l'animation des activités des salariés exerçant des fonctions syndicales et leur information au titre des politiques mentionnées aux 1° et 2° du présent article, ainsi que les formations communes mentionnées à l'article L. 2212-1. Le fonds contribue au financement de ces activités au moyen des subventions prévues aux 1° et 3° du I de l'article L. 2135-10 ;",
    "4° Toute autre mission d'intérêt général pour laquelle d'autres ressources sont prévues sur le fondement du 4° du I de l'article L. 2135-10.",
],
    "Réécriture à droit constant : dans chaque subdivision, les activités sont distinguées des ressources qui les financent ; la formation et ses bénéficiaires sont présentés avant les exemples de dépenses. Les quatre missions et les affectations correspondantes sont maintenues, sans réforme de fond du financement paritaire.",
    "Les cinq alinéas sont conservés. Chaque ressource reste affectée à la même mission : I, 1° et éventuellement 2° pour la mission 1° ; I, 3° pour la mission 2° ; I, 1° et 3° pour la mission 3° ; I, 4° pour la mission 4°. Tous ces renvois visent L. 2135-10. Les renvois à L. 2145-1, L. 2145-2 et L. 2212-1 et la dimension environnementale de la formation sont maintenus."
)

add('L2135-12', [
    "Les bénéficiaires des crédits du fonds paritaire pour l'exercice des missions mentionnées à l'article L. 2135-11 sont les suivants :",
    "1° Pour la mission mentionnée au 1° du même article L. 2135-11 : les organisations de salariés et d'employeurs représentatives au niveau national et interprofessionnel et leurs organisations territoriales ; les organisations professionnelles d'employeurs représentatives au niveau national et multi-professionnel, ainsi que celles représentatives au niveau de la branche ou, dans le secteur de la production cinématographique, de l'audiovisuel et du spectacle, les organisations professionnelles d'employeurs représentatives de l'ensemble des professions de ce secteur dont les statuts prévoient qu'elles ont vocation à percevoir ces crédits ; les employeurs qui ont maintenu la rémunération, ainsi que les cotisations et contributions sociales correspondantes, des salariés d'entreprise participant aux négociations conformément à l'article L. 2232-8 ;",
    "2° Pour la mission mentionnée au 2° de l'article L. 2135-11 : les organisations de salariés et d'employeurs représentatives au niveau national et interprofessionnel ; les organisations syndicales de salariés dont la vocation statutaire présente un caractère national et interprofessionnel et qui recueillent plus de 3 % des suffrages exprimés lors des élections prévues au 3° de l'article L. 2122-9 ; les organisations professionnelles d'employeurs représentatives au niveau national et multi-professionnel mentionnées à l'article L. 2152-2 ;",
    "3° Pour la mission mentionnée au 3° de l'article L. 2135-11 : les organisations syndicales de salariés représentatives au niveau national et interprofessionnel, ainsi que celles dont la vocation statutaire présente un caractère national et interprofessionnel et qui recueillent plus de 3 % des suffrages exprimés lors des élections prévues au 3° de l'article L. 2122-9 ;",
    "4° Les associations désignées par accord de la branche professionnelle concernée, auxquelles sont attribuées les ressources mentionnées au 4° du I de l'article L. 2135-10 lorsque ces ressources sont recouvrées dans les conditions prévues au III du même article L. 2135-10.",
],
    "Réécriture à droit constant : chaque liste de bénéficiaires est introduite par la mission correspondante et les catégories sont séparées par des points-virgules à l'intérieur de leur subdivision. La condition de perception par les associations de branche est exprimée plus directement. Aucune réforme de fond des bénéficiaires ou des seuils n'est appliquée.",
    "Les cinq alinéas et les 1° à 4° sont maintenus. Le seuil demeure strictement supérieur à 3 % et lié aux élections du 3° de L. 2122-9. Le régime du secteur de la production cinématographique, de l'audiovisuel et du spectacle et sa condition statutaire sont conservés. L. 2232-8 a été lu dans le corpus : son régime de prise en charge n'est pas élargi par la présente réécriture. Les notes source retiennent le 1er janvier 2024 pour les contributions dues à compter de cette date au titre du II de l'article 8 de l'ordonnance n° 2021-797 du 23 juin 2021, et une entrée en vigueur au 1er janvier 2024 au titre du X de l'article 13 de la loi n° 2023-1250 du 26 décembre 2023. Ces dates historiques sont conservées comme telles. La source comporte au 4° l'accord grammatical « branche professionnelle concernées », corrigé en « concernée » sans changement de champ."
)

add('L2135-13', [
    "I. ― Le fonds paritaire répartit ses crédits selon les règles suivantes :",
    "1° Pour la mission mentionnée au 1° de l'article L. 2135-11, les crédits sont répartis à parité entre les organisations syndicales de salariés et les organisations professionnelles d'employeurs, au niveau national et au niveau de la branche. Les modalités de répartition au sein de chacune de ces deux catégories sont fixées par voie réglementaire : la répartition est uniforme entre les organisations syndicales de salariés et dépend de l'audience pour les organisations professionnelles d'employeurs. Cette audience est appréciée à partir de deux critères, chacun pris en compte à hauteur de 50 % : le nombre d'entreprises qui emploient au moins un salarié et adhèrent à des organisations professionnelles d'employeurs représentatives, et le nombre de salariés employés par ces mêmes entreprises ;",
    "2° Pour la mission mentionnée au 2° de l'article L. 2135-11, les crédits sont attribués sur une base forfaitaire identique, fixée par décret, à chacune des organisations syndicales de salariés et des organisations professionnelles d'employeurs représentatives au niveau national et interprofessionnel. Une base forfaitaire identique d'un montant inférieur, fixée par décret, s'applique à chacune des organisations syndicales de salariés dont la vocation statutaire présente un caractère national et interprofessionnel et qui ont recueilli plus de 3 % des suffrages exprimés lors des élections prévues au 3° de l'article L. 2122-9, ainsi qu'à chacune des organisations professionnelles d'employeurs représentatives au niveau national et multi-professionnel mentionnées à l'article L. 2152-2 ;",
    "3° Pour la mission mentionnée au 3° de l'article L. 2135-11, les crédits sont répartis selon des modalités définies par décret, en fonction de l'audience de chacune des organisations syndicales de salariés dont la vocation statutaire présente un caractère national et interprofessionnel et qui ont recueilli plus de 3 % des suffrages exprimés lors des élections prévues au 3° de l'article L. 2122-9.",
    "II. ― Pour attribuer les crédits du fonds aux organisations mentionnées à l'article L. 2135-12, est prise en compte l'année qui suit celle au cours de laquelle :<br /><br />1° Leur représentativité est déterminée et leur audience est mesurée en application des articles L. 2122-5 et L. 2122-9 pour les organisations syndicales de salariés, et des articles L. 2152-1, L. 2152-2 et L. 2152-4 pour les organisations professionnelles d'employeurs ;<br /><br />2° Est publié l'arrêté de fusion des champs conventionnels pris en application de l'article L. 2261-32 ou l'arrêté d'extension de l'accord de fusion de ces champs, et sont appréciées et mesurées, respectivement, la représentativité et l'audience des organisations syndicales de salariés et des organisations professionnelles d'employeurs concernées conformément aux dispositions des 1° et 3° du présent article.",
],
    "Réécriture à droit constant : chaque règle de répartition commence par la mission qu'elle finance ; les deux critères d'audience et les deux niveaux de forfait sont distingués dans leurs subdivisions d'origine. Le II conserve sa structure et son décalage annuel. Aucune réforme de fond des taux de pondération, des bénéficiaires ou du calendrier n'est appliquée.",
    "Parité nationale et de branche, pondérations de 50 % chacune, entreprises adhérentes employant au moins un salarié, seuil strictement supérieur à 3 %, forfait inférieur pour les catégories désignées et année suivant les événements du II sont conservés. Tous les renvois et les subdivisions sont maintenus. Le renvoi final aux « 1° et 3° du présent article » est ambigu, l'article comportant des subdivisions I et II : le rattachement éventuel aux 1° et 3° du I doit être contrôlé, sans précision ajoutée silencieusement. La condition finale liant publication de l'arrêté de fusion et appréciation de la représentativité et de l'audience est conservée."
)


assert len(sources) == 24
assert len(drafts) == len(sources)
assert set(drafts) == {a['number'] for a in sources}
answer = []
for source in sources:
    item = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    item.update(drafts[source['number']])
    item['status'] = 'rewrite_draft'
    answer.append(item)
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
