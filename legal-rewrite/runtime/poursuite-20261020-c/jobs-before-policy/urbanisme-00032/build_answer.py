import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
drafts = {}


def add(number, proposed_xml, reason, review_notes, removed=None, repeal=None):
    item = {
        'proposed_xml': proposed_xml.strip(),
        'reason': reason,
        'review_notes': review_notes,
        'status': 'rewrite_draft',
    }
    if removed:
        item.update(
            change_type='normative_reduction',
            reform_policy_id='editorial_direction_2026_10_19',
            removed_provisions=removed,
        )
    if repeal:
        item.update(
            change_type='full_repeal',
            repeal_policy_id='editorial_direction_2026_10_19',
            repeal_scope=repeal,
        )
    assert number not in drafts
    drafts[number] = item


add('L424-1', '''
<p>L'autorité compétente statue par arrêté sur une demande de permis. Elle statue également par arrêté sur une déclaration préalable lorsqu'elle s'y oppose ou impose des prescriptions.</p>
<p>Elle peut surseoir à statuer sur une demande d'autorisation concernant des travaux, des constructions ou des installations dans les cas prévus au 6° de l'article L. 102-13, aux articles L. 121-22-3, L. 121-22-7, L. 153-11 et L. 311-2 du présent code et à l'article L. 331-6 du code de l'environnement.</p>
<p>Elle peut aussi surseoir à statuer dans les cas suivants :</p>
<p>1° À compter de l'ouverture de l'enquête préalable à la déclaration d'utilité publique d'une opération, lorsque la demande porte sur des travaux, des constructions ou des installations à réaliser sur des terrains destinés à être compris dans cette opération ;</p>
<p>2° Lorsque les travaux, constructions ou installations risquent de compromettre l'exécution de travaux publics, si l'autorité compétente a pris en considération la mise à l'étude du projet de travaux publics et si les terrains affectés par ce projet ont été délimités ;</p>
<p>3° Lorsque les travaux, constructions ou installations risquent de compromettre la réalisation d'une opération d'aménagement, si la commune ou l'établissement public de coopération intercommunale compétent a pris en considération le projet d'aménagement et si les terrains affectés par ce projet ont été délimités. Pour les zones d'aménagement concerté, le sursis peut être prononcé à compter de la publication de l'acte créant la zone, conformément à l'article L. 311-2 du présent code.</p>
<p>Dans les cas prévus aux 2° et 3° du présent article et à l'article L. 102-13, la décision de prise en considération doit avoir été publiée avant le dépôt de la demande d'autorisation. Cette décision cesse de produire effet si l'exécution des travaux publics ou la réalisation de l'opération d'aménagement n'a pas commencé dans les dix ans suivant son entrée en vigueur. Dans les cas prévus aux 2° et 3° du présent article, au 6° de l'article L. 102-13 et aux articles L. 153-11 et L. 311-2, la seule augmentation du coût d'exécution du projet, du plan ou de l'opération ne justifie pas un sursis.</p>
<p>Le sursis doit être motivé. Sa durée ne peut dépasser deux ans. À son expiration, l'autorité compétente ne peut opposer à la même demande un nouveau sursis fondé sur le même motif. Si une autre disposition législative permet un nouveau sursis pour un motif différent, la durée cumulée des sursis ne peut dépasser trois ans. À l'expiration du sursis, l'autorité compétente pour délivrer l'autorisation reprend l'instruction sans que l'intéressé ait à confirmer sa demande et notifie une décision définitive dans les deux mois. À défaut de notification dans ce délai, l'autorisation est accordée dans les termes de la demande, sous réserve des cas dans lesquels un permis tacite ne peut être acquis en application de l'article L. 424-2.</p>
<p>Lorsqu'un sursis a été prononcé, les propriétaires des terrains auxquels un refus d'autorisation de construire ou d'utiliser le sol a été opposé peuvent mettre en demeure la collectivité ou le service public à l'origine du projet d'acquérir leur terrain, dans les conditions et délais prévus aux articles L. 230-1 et suivants.</p>
<p>L'exclusion du seul motif d'augmentation du coût s'applique aux sursis prononcés à compter de l'entrée en vigueur de la loi instituant cette exclusion. La reprise de l'instruction sans confirmation s'applique aux sursis dont la durée de validité expire à compter de cette entrée en vigueur, y compris s'ils ont été prononcés auparavant. Elle ne rouvre pas les demandes dont les effets avaient déjà cessé avant cette date. Les sursis antérieurs conservent leurs autres effets jusqu'à leur expiration.</p>
''',
    "Réforme de fond : retrait du pouvoir de bloquer une demande pour le seul renchérissement d'un projet public ou d'un futur plan, y compris dans les dispositions législatives expressément coordonnées. Suppression de la confirmation de la demande et de son délai de forclusion de deux mois après le sursis ; la reprise devient automatique. À droit constant, maintien des autres motifs, de la publication préalable, des dix ans, des plafonds de deux et trois ans et du droit de délaissement. Les deux formulations répétitives du délai de décision sont réunies. La réserve expresse relative aux exceptions au permis tacite protège les procédures qui exigent une décision expresse.",
    "Coordinations à reporter au 6° de L102-13, au troisième alinéa de L153-11 et au 2° de L311-2 : leur rédaction source permet encore le motif du seul renchérissement ; la proposition l'écarte expressément. Aucun déplacement des 1°, 2° et 3° ni des alinéas consacrés à la publication, aux délais et au délaissement. La source répète deux fois la décision dans les deux mois suivant la confirmation : doublon signalé et supprimé. Elle associe en outre un sursis à un « refus » dans le dernier alinéa ; cette condition est conservée, sans élargir silencieusement les bénéficiaires du délaissement. Articuler le silence après sursis avec L424-2, R*424-2, R424-2-1 et R*424-3 : la source ne formule pas cette réserve, alors que le corpus exclut notamment l'accord tacite pour l'évaluation environnementale. Les garanties des articles littoraux et des parcs ne sont pas supprimées. L230-2, atteint par le renvoi général au délaissement, devra séparément être neutralisé pour les nouveaux décès conformément à successions, sans supprimer les droits d'acquisition ni les situations fiscales antérieures.",
    removed=[
        "Possibilité de surseoir pour la seule augmentation du coût des travaux publics, opérations d'aménagement ou futur plan dans les cas expressément visés.",
        "Obligation pour le demandeur de confirmer sa demande après le sursis, avec perte de la reprise de procédure si cette confirmation n'intervient pas dans les deux mois.",
        "Double énoncé, au même alinéa, de l'obligation de statuer dans les deux mois suivant la confirmation de la demande.",
    ])

add('L424-2', '''
<p>Si aucune décision n'a été notifiée au demandeur à l'expiration du délai d'instruction, le permis est accordé tacitement.</p>
<p>Un décret en Conseil d'État détermine les cas dans lesquels le silence de l'autorité compétente ne peut donner naissance à un permis tacite.</p>
''',
    "Réécriture à droit constant : le point de départ de l'accord tacite et l'habilitation à définir ses exceptions sont énoncés directement. Le mécanisme simplifie déjà la délivrance des permis ; supprimer ses exceptions sans examen de leurs protections environnementales, patrimoniales et de sécurité serait injustifié.",
    "Aucun délai d'instruction nouveau. Conserver les exceptions de R*424-2, R424-2-1 et R*424-3 ainsi que leurs transitions propres ; la réserve ajoutée à L424-1 renvoie à ce dispositif. Le présent article ne crée pas de permis tacite pour les projets soumis à évaluation environnementale.")

add('L424-3', '''
<p>L'autorité compétente motive la décision qui rejette une demande ou s'oppose à une déclaration préalable.</p>
<p>Elle y expose tous les motifs qui justifient le rejet ou l'opposition. Elle indique notamment chaque non-conformité des travaux aux dispositions législatives et réglementaires mentionnées à l'article L. 421-6.</p>
<p>Elle motive également la décision qui impose des prescriptions, prononce un sursis à statuer ou accorde une dérogation ou une adaptation mineure aux règles d'urbanisme applicables. Elle en expose tous les motifs. L'obligation de motiver la dérogation ne s'applique pas à celles accordées en application des 1° à 6° de l'article L. 152-6.</p>
''',
    "Réécriture à droit constant avec désignation de l'autorité responsable et séparation du contenu de la motivation. Maintien de l'exhaustivité des motifs, garantie contre les refus successifs incomplets et condition d'un recours effectif. L'exemption de motivation des dérogations des 1° à 6° de L152-6 est conservée.",
    "Conserver les trois alinéas et le champ des 1° à 6° de L152-6. L'exemption porte sur la dérogation concernée et ne dispense pas de motiver d'autres prescriptions ou un refus contenus dans la même décision. Coordonner R*424-5, dont la formulation générale ne reproduit pas cette exemption. Aucun allègement de la motivation des refus, sursis ou prescriptions n'est proposé.")

add('L424-4', '''
<p>La décision qui autorise un projet soumis à évaluation environnementale contient tous les éléments mentionnés au I de l'article L. 122-1-1 du code de l'environnement. Ces éléments figurent dans le corps de la décision ou dans une annexe qui en fait partie intégrante. Lorsqu'ils figurent déjà dans la décision, il n'est pas exigé de document annexé distinct qui les reproduise.</p>
<p>Cette faculté de présentation s'applique aux décisions prises à compter de l'entrée en vigueur de la loi qui l'institue. Elle ne modifie ni les conditions d'application dans le temps de l'évaluation environnementale ni les obligations attachées aux décisions antérieures.</p>
''',
    "Réforme de fond limitée à la suppression du document annexe obligatoire lorsqu'une décision contient elle-même tous les éléments requis. L'information environnementale, les prescriptions et le suivi exigés par le renvoi sont intégralement maintenus ; seule leur reproduction formelle est retirée. La transition ne remet pas en cause les décisions antérieures.",
    "La note source renvoie à l'article 6 de l'ordonnance n° 2016-1058 du 3 août 2016 pour le champ temporel initial : ce renvoi historique n'est pas la date de la présente réforme et reste à respecter. Coordonner la présentation avec le I de L122-1-1 du code de l'environnement et les textes réglementaires d'application, hors du présent lot. Les exigences européennes d'évaluation, de motivation, de publicité et de suivi demeurent ; l'annexe facultative n'autorise aucune omission de leur contenu.",
    removed=[
        "Obligation de constituer un document annexé distinct pour des éléments environnementaux déjà intégralement contenus dans la décision d'autorisation.",
    ])

add('L424-5', '''
<p>L'autorité compétente ne peut retirer une décision de non-opposition à une déclaration préalable ou un permis de construire, d'aménager ou de démolir, tacite ou explicite, que si cette décision est illégale et si le retrait intervient dans les trois mois suivant sa date. Après ces trois mois, elle ne peut procéder au retrait que sur demande expresse du bénéficiaire.</p>
<p>Le bénéficiaire d'une autorisation d'urbanisme peut déposer une nouvelle demande pour le même terrain sans faire retirer l'autorisation déjà délivrée. Le dépôt de cette demande n'entraîne pas non plus le retrait implicite de l'autorisation antérieure.</p>
''',
    "Réécriture à droit constant : les deux conditions cumulatives du retrait et l'absence de retrait préalable ou implicite en cas de nouvelle demande sont formulées directement. L'article protège déjà la stabilité des autorisations et supprime une démarche de retrait inutile ; il ne contient pas de charge supplémentaire à abolir.",
    "Délai de trois mois conservé, ainsi que les décisions tacites ou explicites, les trois catégories de permis et la demande expresse du bénéficiaire après ce délai. La nouvelle demande n'annule pas l'ancien titre ; les autres causes de disparition des autorisations ne sont pas modifiées par cet article.")

add('L424-6', '''
<p>Le présent article est abrogé pour les permis tacites et les décisions de non-opposition à déclaration préalable intervenus à compter de l'entrée en vigueur de la loi prononçant son abrogation. Aucune participation ne peut être fixée à leur bénéficiaire par un arrêté postérieur sur le fondement du présent article.</p>
<p>Pour les permis tacites et les décisions de non-opposition intervenus avant cette entrée en vigueur, le présent article demeure applicable dans sa rédaction antérieure : les participations peuvent être fixées dans les deux mois suivant l'intervention de ces permis ou décisions. Les participations régulièrement établies pour ces situations antérieures restent soumises aux règles de recouvrement, de restitution, de prescription et de recours qui leur sont applicables.</p>
<p>Cette abrogation ne supprime ni les taxes directement exigibles en vertu de leurs dispositions propres, ni les participations résultant d'une convention régulièrement conclue, ni celles régulièrement prescrites par une décision expresse sur un autre fondement légal. Elle n'autorise pas à rétablir, par le retrait ou la modification du titre sur le seul fondement de cette abrogation, la fixation postérieure de participations pour les permis tacites et les décisions de non-opposition auxquels l'abrogation s'applique.</p>
''',
    "Abrogation de fond de la faculté d'imposer des participations par un arrêté distinct après qu'un permis tacite ou une non-opposition est intervenu. La charge financière discrétionnairement prescrite après le titre disparaît pour les faits nouveaux. La transition conserve exactement la fenêtre de deux mois pour les anciens titres et leurs dettes, restitutions et recours. Les taxes légales et engagements conventionnels distincts ne sont pas supprimés sous couvert de cette abrogation.",
    "Coordonner R*424-8 et le deuxième alinéa de R*424-10 pour réserver leur application aux titres antérieurs. L332-28 et R*424-7 restent utiles aux prescriptions financières régulièrement contenues dans les décisions expresses et aux situations historiques ; ne pas les abroger globalement. Les équipements propres de L332-15 et les autres obligations de L332-6 ne sont pas éteints. La suppression concerne le pouvoir de prescription tardive, pas une baisse générale de taxe d'aménagement : effet financier à documenter sans inventer de compensation ni d'économie.",
    repeal="Suppression, pour les permis tacites et non-oppositions futurs, du pouvoir de fixer par arrêté distinct des participations dans les deux mois suivant leur intervention ; conservation des titres antérieurs et des autres fondements fiscaux ou conventionnels.")

add('L424-7', '''
<p>Lorsque le maire agit au nom de la commune ou que le président de l'établissement public de coopération intercommunale est compétent, le permis délivré par arrêté est exécutoire dès sa notification au demandeur, sous réserve de l'article L. 424-9. Par dérogation à la condition de transmission préalable résultant des articles L. 2131-1 et L. 2131-2 du code général des collectivités territoriales, le retard de transmission au préfet ne reporte pas cette prise d'effet. L'autorité compétente reste tenue de transmettre le permis au préfet dans les conditions prévues par ces articles ; les pouvoirs de contrôle de légalité et de saisine du juge du représentant de l'État sont maintenus.</p>
<p>Cette règle s'applique aux arrêtés notifiés à compter de l'entrée en vigueur de la loi qui l'institue. Les arrêtés notifiés auparavant restent soumis aux conditions de prise d'effet applicables à la date de leur notification.</p>
''',
    "Réforme de fond : suppression du report de l'exécution d'un permis du seul fait que la collectivité n'a pas encore effectué sa transmission au préfet. La notification au demandeur devient suffisante dans le champ de l'article. Le contrôle de légalité, sa transmission obligatoire et le délai spécial des démolitions restent protégés. La règle nouvelle ne modifie pas rétroactivement la date de prise d'effet des anciens arrêtés.",
    "Coordination législative hors des cinq codes : articles L2131-1 et L2131-2 du code général des collectivités territoriales, et dispositions qui en étendent le régime aux EPCI. La dérogation est expressément limitée à la prise d'effet du permis ; aucune dispense de transmission ni réduction du délai de contrôle n'en résulte. Coordonner R*424-11 et R*424-12. L424-9 conserve le délai spécial pour les décisions qu'il vise. Cette simplification ne s'étend pas aux autres actes locaux.",
    removed=[
        "Condition de transmission préalable du permis au préfet pour son caractère exécutoire, lorsque le bénéficiaire a déjà reçu notification de l'arrêté.",
    ])

add('L424-8', '''
<p>Le permis tacite devient exécutoire à la date à laquelle il est acquis. Il en va de même de la décision de non-opposition à une déclaration préalable.</p>
''',
    "Réécriture à droit constant en deux phrases pour distinguer les deux décisions. La prise d'effet immédiate constitue déjà une simplification et ne doit pas être remplacée par une attestation ou une formalité nouvelle.",
    "Maintien de la date d'acquisition comme date de prise d'effet, sous la dérogation légale de L424-9. Le certificat de R*424-13 reste un moyen de preuve demandé par l'intéressé ; il ne devient pas une condition d'exécution.")

add('L424-9', '''
<p>Par dérogation aux articles L. 424-7 et L. 424-8, le permis de démolir et la décision de non-opposition à la déclaration prévue à l'article L. 421-4 ne deviennent exécutoires qu'après l'expiration du délai déterminé par décret en Conseil d'État.</p>
''',
    "Réécriture à droit constant de la dérogation et de son effet. Le délai avant les démolitions et certaines interventions irréversibles est maintenu pour permettre l'exercice utile des protections et recours ; sa suppression générale ne se justifie pas par le seul objectif de rapidité.",
    "Renvois à L424-7, L424-8 et L421-4 conservés. Le corpus R*424-1 précise un mois pour les coupes et abattages déclarés ; ce chiffre réglementaire n'est pas inséré dans l'habilitation législative. La réforme de L424-7 ne neutralise pas ce délai spécial.")

add('L425-1', '''
<p>Lorsque les constructions ou travaux mentionnés aux articles L. 421-1 à L. 421-4 relèvent, du fait de leur emplacement, de leur utilisation ou de leur nature, d'une autorisation ou de prescriptions prévues par une autre législation ou réglementation que le code de l'urbanisme, le permis de construire, d'aménager ou de démolir ou la décision prise sur la déclaration préalable vaut autorisation au titre de cette autre législation ou réglementation dans les cas déterminés par décret en Conseil d'État. L'autorité compétente au titre de cette législation ou réglementation doit avoir donné son accord à la décision.</p>
<p>Dans ces cas, la demande d'urbanisme et les pièces nécessaires à l'accord sont réunies dans un seul dossier, déposé auprès du service chargé de recevoir la demande d'urbanisme. Ce service transmet aux autorités concernées les pièces nécessaires à leur compétence. Aucune demande séparée ni nouvel exemplaire d'une pièce déjà présente dans ce dossier ne peut être exigé pour l'autorisation dont la décision d'urbanisme tient lieu. Une pièce à jour, légalement accessible à l'administration pour cette instruction et identifiée par le demandeur, est réutilisée sans nouvelle production. Le demandeur peut en obtenir communication et demander la rectification des données inexactes. La réutilisation respecte les secrets protégés par la loi.</p>
<p>Le dossier commun ne dispense d'aucun accord, avis, évaluation ni participation du public requis par les législations concernées. Il ne modifie ni les délais ordinaires d'instruction ni les cas de majoration ou de suspension légalement applicables en vertu de l'article L. 423-1. Une demande de pièce déjà disponible dans les conditions du deuxième alinéa ne peut interrompre ni prolonger ces délais.</p>
<p>Les règles du dossier commun prévues aux deuxième et troisième alinéas s'appliquent à l'expiration de six mois à compter de l'entrée en vigueur de la loi qui les institue. Elles s'appliquent aussi aux demandes en cours à cette date, sans imposer un nouveau dépôt ni faire recommencer les délais déjà écoulés. Les décisions déjà prises et les accords déjà recueillis restent valables dans leur champ propre.</p>
''',
    "Réforme de fond : le mécanisme d'autorisation intégrée est complété par un dépôt commun opposable aux services, l'interdiction des demandes et exemplaires en double et le réemploi des pièces légalement disponibles. La demande d'une pièce déjà détenue ne crée plus de délai supplémentaire. À droit constant, maintien des cas fixés par décret et de l'accord de l'autorité sectorielle. Transition de six mois pour l'organisation des services, conformément à la coordination logement.",
    "Coordonner L423-1 et ses dispositions réglementaires, notamment R*423-38, R*423-39 et R*423-41, pour empêcher la relance de délai par une pièce déjà disponible. Ce texte ne fusionne que les autorisations dont le titre d'urbanisme tient effectivement lieu ; il ne dispense pas des décisions autonomes des articles L425-6 et suivants. Les accords tacites légalement prévus restent possibles : aucune exigence générale d'accord exprès n'est créée. Les délais ordinaires et exceptions existants ne sont pas réinitialisés par la transition. Les échanges doivent rester dans le champ des accès légaux et des secrets protégés, sans présumer une interconnexion universelle.",
    removed=[
        "Dépôt d'une demande sectorielle séparée pour une autorisation déjà intégrée au titre d'urbanisme dans les cas prévus par les textes.",
        "Production répétée d'exemplaires ou de pièces à jour déjà présentes au dossier commun ou légalement accessibles et identifiées pour son instruction.",
        "Interruption ou prolongation de l'instruction fondée sur la redemande d'une pièce déjà disponible dans les conditions légales de réemploi.",
    ])

add('L425-2', '''
<p>Pour un projet portant sur un immeuble de grande hauteur, le permis de construire vaut autorisation au titre des articles L. 141-2, L. 145-1 et L. 146-1 du code de la construction et de l'habitation si l'autorité chargée de la police de la sécurité a donné son accord à sa délivrance.</p>
''',
    "Réécriture à droit constant de la condition d'accord et de l'équivalence entre permis et autorisation de sécurité. L'article évite déjà une seconde autorisation ; conserver l'accord de sécurité pour les immeubles de grande hauteur répond à une protection essentielle contre l'incendie.",
    "Les trois renvois sont conservés. Incohérence préexistante relevée dans le corpus : L145-1 concerne la moyenne hauteur, tandis que L146-1 concerne la grande hauteur ; L141-2 définit les règles de sécurité plutôt qu'une autorisation autonome. Aucun de ces renvois n'est corrigé silencieusement. R*425-14 ne reproduit pas L141-2. La note source fixe le terme historique d'entrée en vigueur au 1er juillet 2021 par l'article 8 de l'ordonnance 2020-71 du 29 janvier 2020 ; aucune nouvelle date n'en est déduite. Les dispenses déjà prévues par les articles du CCH lorsque la sécurité incendie n'est pas affectée conservent leur champ.")

add('L425-3', '''
<p>Pour un projet portant sur un établissement recevant du public, lorsque l'autorisation prévue à l'article L. 122-3 du code de la construction et de l'habitation est requise, le permis de construire en tient lieu si l'autorité administrative compétente a donné son accord à sa délivrance. Cette autorité peut imposer, en application de l'article L. 143-2 du même code, des prescriptions relatives à l'exploitation des bâtiments ; le permis les mentionne. Si, lors du dépôt de la demande de permis, l'aménagement intérieur de tout ou partie de l'établissement n'est pas connu, le permis indique qu'une autorisation complémentaire au titre de l'article L. 122-3 devra être demandée et obtenue pour l'aménagement intérieur du bâtiment ou de la partie concernée avant son ouverture au public. Les dispenses d'autorisation et les cas dans lesquels cet article substitue une déclaration à l'autorisation restent régis par cet article.</p>
''',
    "Réécriture à droit constant du mécanisme d'autorisation intégrée, de la mention des prescriptions d'exploitation et du complément limité à l'intérieur non connu au dépôt. La précision sur le caractère requis de l'autorisation évite que ce renvoi ne rétablisse une autorisation supprimée ou remplacée par une déclaration dans le CCH. Aucun allègement du contrôle de sécurité ou d'accessibilité applicable n'est créé.",
    "Décalage préexistant signalé : la source L425-3 de 2021 ne décrit pas les dispenses et la déclaration désormais présentes dans L122-3 du CCH fourni au corpus. La proposition reconnaît expressément leur champ propre, sans étendre la déclaration à tous les ERP. Le seuil de moins de 300 mètres carrés, l'extinction adaptée ou la situation en gare, la même activité et la certification indépendante restent dans L122-3 et ne sont pas supprimés par le renvoi. Préserver R*425-15 et la décision complémentaire avant ouverture pour les aménagements concernés lorsqu'elle est requise. La note source relative à l'article 8 de l'ordonnance 2020-71 et au 1er juillet 2021 demeure historique.")

add('L425-4', '''
<p>Lorsqu'un projet relève de l'autorisation d'exploitation commerciale prévue à l'article L. 752-1 du code de commerce, le permis de construire vaut cette autorisation si la commission départementale d'aménagement commercial ou, le cas échéant, la Commission nationale d'aménagement commercial a rendu un avis favorable sur la demande de permis. Si une modification substantielle au sens de l'article L. 752-15 du même code n'affecte pas la conformité des travaux aux dispositions législatives et réglementaires mentionnées à l'article L. 421-6 du présent code, le demandeur sollicite une nouvelle autorisation d'exploitation commerciale auprès de la commission départementale.</p>
<p>Les personnes mentionnées à l'article L. 752-17 du code de commerce peuvent saisir directement le juge d'un recours contre la décision de l'autorité administrative compétente pour délivrer le permis de construire. L'absence de saisine préalable de la Commission nationale d'aménagement commercial ne rend pas ce recours irrecevable. La saisine de cette commission est facultative ; les règles de l'article L. 752-17 s'y appliquent à l'exclusion de toute condition faisant de cette saisine un préalable au recours contentieux. Les autres conditions de recevabilité du recours contentieux restent applicables.</p>
<p>La faculté de recours direct s'applique aux recours contentieux introduits à compter de l'entrée en vigueur de la loi qui l'institue, y compris contre une décision antérieure si le délai de recours reste ouvert. Elle ne rouvre aucun délai expiré et ne remet pas en cause les décisions juridictionnelles définitives. Les saisines de la commission nationale déjà effectuées conservent les effets attachés à ces saisines sur les délais de recours.</p>
''',
    "Réforme de fond : suppression du recours administratif préalable obligatoire devant la commission nationale et de la sanction d'irrecevabilité qui lui était attachée. Le recours au juge est directement ouvert et la voie administrative reste facultative. À droit constant, maintien de l'avis favorable pour l'autorisation intégrée et de l'examen commercial des modifications substantielles qui n'affectent pas la conformité urbanistique. Les délais expirés et jugements définitifs sont préservés.",
    "Coordination hors des cinq codes à opérer dans L752-17 du code de commerce pour rendre le recours national facultatif et articuler ses délais avec le recours direct ; les articles L752-1 et L752-15 ne sont pas abrogés. L600-1-4 du présent code, lu dans le corpus, conserve la distinction entre conclusions commerciales et conclusions d'urbanisme ainsi que les moyens recevables : la suppression du préalable n'étend pas l'intérêt pour agir. Adapter R*425-15-1 et les mentions de R*423-44-1 au caractère facultatif du recours, sans supprimer les avis nécessaires ni réinitialiser les délais des saisines antérieures.",
    removed=[
        "Obligation de saisir la Commission nationale d'aménagement commercial avant de pouvoir contester le permis devant le juge et irrecevabilité sanctionnant cette absence de saisine.",
    ])

add('L425-5', '''
<p>Pour un projet portant sur un immeuble classé au titre des monuments historiques, l'autorisation prévue au premier alinéa de l'article L. 621-9 du code du patrimoine dispense de permis de construire, d'aménager ou de démolir et de déclaration préalable, si l'autorité compétente pour statuer sur les demandes de permis de construire a donné son accord à cette autorisation.</p>
''',
    "Réécriture à droit constant du mécanisme qui remplace déjà quatre démarches d'urbanisme par l'autorisation patrimoniale coordonnée. La condition d'accord est conservée : elle évite une seconde demande tout en assurant le contrôle des règles d'urbanisme. Supprimer l'autorisation patrimoniale elle-même ne serait pas une suppression de doublon.",
    "Conserver le seul immeuble classé, le premier alinéa de L621-9 du code du patrimoine et l'accord de l'autorité des permis de construire. Ne pas étendre cette dispense aux seuls immeubles inscrits, régis notamment par R*425-16. R*425-23 formule un champ matériel plus étroit ; signaler ce décalage lors de la coordination réglementaire sans réduire silencieusement la dispense législative.")

add('L425-6', '''
<p>Lorsqu'une opération ou des travaux nécessitent l'autorisation de défrichement prévue aux articles L. 341-1 et L. 341-3 du code forestier, le permis peut être délivré avant cette autorisation, par dérogation à l'ordre de délivrance prévu à l'article L. 341-7 du même code. Le seul fait que cette autorisation soit encore en cours d'instruction ne justifie pas le refus du permis ni la prolongation de son instruction. Le permis indique que sa mise en œuvre est subordonnée à l'obtention de l'autorisation de défrichement et s'effectue dans le respect des prescriptions de celle-ci. Il ne vaut pas autorisation de défrichement. Les évaluations et participations du public légalement requises avant la délivrance du permis restent exigées.</p>
<p>Ces règles s'appliquent aux demandes de permis en cours à l'entrée en vigueur de la loi qui les institue et à celles déposées ensuite. Elles ne font pas recommencer les délais déjà écoulés et ne rouvrent pas les refus devenus définitifs. Les autorisations de défrichement déjà délivrées conservent leurs conditions et leurs effets.</p>
''',
    "Réforme de fond : retrait de la séquence obligatoire qui imposait d'attendre l'autorisation forestière avant de délivrer le permis. L'instruction parallèle devient possible sans report motivé par cette seule attente. Le verrou est maintenu avant toute mise en œuvre du permis, avec respect des prescriptions forestières, des évaluations et de la participation du public. Aucun droit de défricher ni exemption environnementale n'est créé.",
    "Coordination législative hors des cinq codes : L341-7 du code forestier doit reprendre l'ordre nouveau expressément prévu ici. Adapter R*423-29 et R*423-34, qui organisent des délais fondés sur l'autorisation forestière préalable, ainsi que R*431-19 et R*441-7 pour le réemploi des pièces. R*423-34 utilise encore les anciens renvois L311-5 et R312-1 du code forestier : incohérence préexistante à contrôler, sans les considérer comme nouveaux renvois de la proposition. Les procédures d'évaluation et de participation ne sont pas anticipées par un simple permis ; l'interdiction de mise en œuvre vaut jusqu'à l'autorisation forestière requise. Les autres régimes spéciaux, notamment les autorisations de travaux en montagne, ne sont pas supprimés par cette disposition.",
    removed=[
        "Obligation d'obtenir l'autorisation de défrichement avant la délivrance du permis, avec blocage de l'instruction du seul fait de son attente, remplacée par une condition préalable à l'exécution.",
    ])

add('L425-8', '''
<p>Pour un projet de création, d'extension ou de réouverture au public d'un établissement de spectacles cinématographiques soumis à l'autorisation prévue aux articles L. 212-7 et L. 212-8 du code du cinéma et de l'image animée, l'autorité compétente ne peut délivrer le permis de construire qu'après l'obtention de cette autorisation. La seule introduction ou la seule pendance d'un recours contre cette autorisation ne suspend pas la mise en œuvre du permis. Une décision juridictionnelle de suspension ou d'annulation et les interdictions légales de travaux ayant un objet distinct de cette attente de l'issue des recours restent opposables au bénéficiaire.</p>
<p>La suppression de la suspension automatique par le recours s'applique à compter de l'entrée en vigueur de la loi qui l'institue, y compris aux autorisations et permis antérieurs et aux recours en cours. Elle ne remet pas en cause les décisions juridictionnelles déjà rendues.</p>
''',
    "Réforme de fond : suppression du gel automatique de l'exécution du permis pendant les recours contre l'autorisation cinématographique. L'autorisation reste exigée avant le permis ; le juge conserve le pouvoir de suspendre et les décisions d'annulation restent opposables. L'allègement vise un effet suspensif automatique, sans supprimer le recours ni le contrôle commercial du projet.",
    "Coordonner les dispositions du code du cinéma et de l'image animée relatives aux autorisations visées par L212-7 et L212-8 et à leurs recours, hors des cinq codes ; le régime distinct de ces recours ne doit pas rétablir le gel général retiré ici. Cette proposition ne supprime pas les prolongations liées à l'obtention initiale d'une autorisation refusée, notamment R*423-36 et R*423-44-1, ni le cas de rejet implicite de R*424-2 I g. Elle supprime l'attente de l'issue des recours une fois l'autorisation obtenue. La rédaction source « expiration des recours entrepris » est ambiguë sur le terme exact de cette attente : ambiguïté signalée, et règle remplacée expressément. Ne pas confondre ces recours avec ceux relatifs à la légalité urbanistique du permis.",
    removed=[
        "Interdiction automatique de mettre en œuvre le permis de construire tant que les recours engagés contre l'autorisation d'exploitation cinématographique ne sont pas achevés.",
    ])

add('L425-9', '''
<p>Les travaux ayant pour objet le changement d'usage de locaux destinés à l'habitation et soumis à l'autorisation préalable prévue à l'article L. 631-7 du code de la construction et de l'habitation ne peuvent commencer qu'après l'obtention de cette autorisation.</p>
<p>Lorsque ces mêmes travaux nécessitent un permis ou une déclaration préalable, la demande d'urbanisme peut aussi valoir demande d'autorisation de changement d'usage si elle comporte les éléments nécessaires à cette décision. Avec l'accord de l'autorité compétente pour autoriser le changement d'usage, le permis ou la décision de non-opposition tient lieu de cette autorisation et en mentionne les conditions. Aucun dossier ni acte d'autorisation séparé n'est alors exigé. Les conditions de fond, les avis requis, le caractère personnel de l'autorisation ou son rattachement au local en cas de compensation, les obligations de compensation et la publicité foncière restent régis par le code de la construction et de l'habitation. Le transfert du permis n'emporte pas transfert d'une autorisation de changement d'usage accordée à titre personnel.</p>
<p>Cette intégration s'applique aux demandes déposées à compter de l'expiration d'un délai de six mois suivant l'entrée en vigueur de la loi qui l'institue. À compter de cette même date, elle peut aussi être demandée pour les dossiers en cours, sans nouvelle production des pièces déjà disponibles ni reprise des délais écoulés. Les autorisations déjà délivrées conservent leur champ et leurs conditions ; un permis antérieur ne vaut pas, par lui-même, autorisation de changement d'usage.</p>
''',
    "Réforme de fond : création d'une décision commune facultative pour le changement d'usage et l'urbanisme, supprimant la demande et l'acte séparés lorsque l'accord sectoriel est acquis. Le verrou avant travaux demeure ; l'autorisation de changement d'usage n'est pas abolie. Les protections du parc de logements, les compensations et les effets personnels ou réels du titre sont maintenus. Transition de six mois pour l'organisation des services et absence de conversion automatique des permis antérieurs.",
    "Coordonner L631-7 et L631-7-1 du CCH : l'accord du maire et, à Paris, Marseille et Lyon, l'avis du maire d'arrondissement restent nécessaires dans leurs champs. L631-7 exige actuellement que la preuve par l'autorisation d'urbanisme soit accompagnée d'une autorisation de changement d'usage ; reconnaître la décision commune comme ces deux titres, sans effacer les conditions de compensation et de publicité de L631-7-1. La note de L631-7 du corpus mentionne une application pour les impositions de 2027 : ne pas transposer cette date fiscale à la présente procédure. Le classement de l'article dans la section 4 devra tenir compte de cette exception d'intégration, sans déplacer silencieusement un alinéa. Cette simplification ne transforme pas une location touristique en location de longue durée et ne modifie pas les droits civils des occupants.",
    removed=[
        "Dossier et acte d'autorisation distincts de changement d'usage lorsque le dossier d'urbanisme contient les éléments nécessaires et que l'autorité de changement d'usage a donné son accord.",
    ])

add('L425-10', '''
<p>Si une demande d'enregistrement a été déposée au titre de l'article L. 512-7 du code de l'environnement, le bénéficiaire ne peut commencer les travaux avant la décision d'enregistrement prévue à l'article L. 512-7-3 du même code.</p>
''',
    "Réécriture à droit constant en identifiant l'interdiction et son destinataire. Maintien de la décision d'enregistrement avant travaux pour les installations concernées : elle porte des protections contre les risques et nuisances et n'est pas une seconde autorisation d'urbanisme à supprimer.",
    "Renvois L512-7 et L512-7-3 conservés sans transformation de l'enregistrement en simple déclaration. L'article ne subordonne pas, à lui seul, la délivrance du permis à l'enregistrement ; il vise l'exécution des travaux. R425-31-1 organise séparément un préalable temporel à la décision de permis et comporte sa propre transition pour les anciennes demandes d'enregistrement.")

add('L425-11', '''
<p>Si des opérations d'archéologie préventive ont été prescrites, le bénéficiaire ne peut commencer les travaux avant leur achèvement.</p>
''',
    "Réécriture à droit constant du déclencheur et de l'interdiction avant travaux. Le verrou ne concerne que les opérations effectivement prescrites ; le retirer détruirait potentiellement les vestiges avant leur étude. Aucune formalité autonome redondante n'est identifiée dans cet article.",
    "Maintenir l'achèvement des opérations prescrites et non le seul dépôt d'un dossier ou la seule délivrance d'un permis. R*425-31 prévoit les pièces et l'intervention du préfet de région au titre du code du patrimoine : leur coordination ne doit pas permettre des travaux détruisant les vestiges pendant les opérations prescrites. Aucune règle nouvelle de redevance d'archéologie n'est créée ici.")

add('L425-12', '''
<p>Pour un projet portant sur une installation nucléaire de base qui nécessite l'autorisation de création prévue à l'article L. 593-7 du code de l'environnement ou une nouvelle autorisation au titre du II de l'article L. 593-14 du même code, le bénéficiaire ne peut commencer les travaux avant la clôture de l'enquête publique préalable à cette autorisation.</p>
''',
    "Réécriture à droit constant du champ nucléaire et de la condition temporelle. La clôture de l'enquête préalable est maintenue pour préserver la participation du public avant le commencement des travaux. Supprimer ce préalable ne serait pas la suppression d'un doublon administratif démontré.",
    "Maintien de L593-7, du II de L593-14 et du terme exact : clôture de l'enquête, non délivrance de l'autorisation. Ce texte ne déclare pas l'ensemble des travaux nucléaires libres après l'enquête ; les autres autorisations, protections de sûreté et exigences environnementales, notamment européennes et conventionnelles, gardent leurs champs.")

add('L425-13', '''
<p>Lorsque le demandeur joint à sa demande de permis de construire une demande de dérogation au titre de l'article L. 112-13 du code de la construction et de l'habitation, l'autorité compétente peut délivrer le permis avant l'obtention de cette dérogation. Le permis mentionne qu'il ne peut être mis en œuvre avant que la dérogation soit obtenue et que les prescriptions de celle-ci doivent être respectées. La seule attente de la décision de dérogation ne justifie ni le refus du permis ni la prolongation de son instruction. Le permis ne vaut pas dérogation.</p>
<p>Cette règle s'applique aux demandes en cours à l'entrée en vigueur de la loi qui l'institue et aux demandes déposées ensuite, sans recommencement des délais déjà écoulés ni réouverture des refus devenus définitifs. Les dérogations déjà obtenues conservent leurs conditions et leurs effets.</p>
''',
    "Réforme de fond : suppression du blocage de la délivrance du permis pendant l'examen d'une dérogation technique jointe au dossier. Le contrôle est conservé avant la mise en œuvre du permis et ses prescriptions restent obligatoires. L'allègement permet l'instruction parallèle sans créer de dérogation tacite nouvelle ni supprimer les exigences de sécurité, d'accessibilité ou de non-dégradation du bâtiment existant.",
    "L112-13 du CCH fourni au corpus vise les extensions verticales de bâtiments achevés depuis plus de deux ans, prévoit des conditions techniques, des mesures compensatoires possibles et une acceptation après trois mois de silence. Ces paramètres demeurent propres à cet article ; la délivrance anticipée du permis ne les remplace pas. Coordonner R*424-2 I j, qui utilise encore l'ancien renvoi CCH L111-4-1 et rattache le rejet tacite du permis au refus de dérogation : incohérence préexistante et séquencement désormais modifié. Les interdictions de travaux et autres obstacles urbanistiques restent applicables. La note source de l'ordonnance 2020-71, avec terme historique au 1er juillet 2021, n'est pas une date de la réforme.",
    removed=[
        "Obligation d'attendre l'obtention de la dérogation technique jointe au dossier avant de délivrer le permis de construire, remplacée par une condition avant sa mise en œuvre.",
    ])

add('L425-14', '''
<p>Sans préjudice du deuxième alinéa de l'article L. 181-30 du code de l'environnement, lorsque le projet relève de l'autorisation environnementale prévue au chapitre unique du titre VIII du livre Ier de ce code ou de la déclaration prévue à la section 1 du chapitre IV du titre Ier de son livre II, le bénéficiaire ne peut mettre en œuvre le permis ou la décision de non-opposition à déclaration préalable :</p>
<p>1° Avant d'avoir obtenu l'autorisation environnementale mentionnée à l'article L. 181-1 du même code, sauf décision spéciale prise sur le fondement de l'article L. 181-30 de ce code ;</p>
<p>2° Avant la décision d'acceptation, si les installations, ouvrages, travaux ou activités sont soumis à déclaration au titre du II de l'article L. 214-3 du même code.</p>
''',
    "Réécriture à droit constant avec sujet explicite et conservation des 1° et 2°. Le contrôle préalable à l'exécution protège l'environnement et l'eau ; l'article comporte déjà l'exception de décision spéciale qui permet une anticipation encadrée. Cette exception est conservée sans créer une dispense générale.",
    "Tous les niveaux de renvoi sont conservés : deuxième alinéa de L181-30, chapitre unique du titre VIII du livre Ier, section 1 du chapitre IV du titre Ier du livre II, L181-1 et II de L214-3 du code de l'environnement. Ne pas transformer la décision d'acceptation prévue par la source en un simple dépôt de déclaration. Les contraintes européennes d'évaluation et de protection de l'eau restent à leur champ ; aucune conformité ou dispense nouvelle n'est présumée.")

add('L425-15', '''
<p>Si les travaux projetés nécessitent une dérogation au titre du 4° du I de l'article L. 411-2 du code de l'environnement, le bénéficiaire ne peut mettre en œuvre le permis ou la décision de non-opposition à déclaration préalable avant d'avoir obtenu cette dérogation.</p>
''',
    "Réécriture à droit constant : la nécessité de la dérogation, le titulaire et l'interdiction avant son obtention sont clairement articulés. Maintien du préalable qui protège les espèces et habitats concernés, sans substituer une autorisation d'urbanisme à la dérogation environnementale.",
    "Conserver précisément le 4° du I de L411-2, les permis et la non-opposition à déclaration préalable. Les conditions de dérogation et les contraintes européennes de protection des espèces restent régies par le code de l'environnement et le droit de l'Union ; le présent article ne les écarte pas. L'attribut de présentation align de la source est supprimé conformément aux balises autorisées, sans effet normatif.")

add('L425-16', '''
<p>Pour les constructions soumises à l'obligation de démolition prévue au I de l'article L. 121-22-5, le bénéficiaire ne peut mettre en œuvre le permis de construire ou d'aménager ou la décision de non-opposition à déclaration préalable avant d'avoir effectué la consignation prévue au même article. La Caisse des dépôts et consignations transmet directement au maire le récépissé de consignation. Par dérogation à l'obligation d'envoi prévue au II de l'article L. 121-22-5, aucun nouvel envoi du récépissé n'est exigé du bénéficiaire. Si la consignation est effectuée et que le bénéficiaire dispose du récépissé, un retard de sa transmission au maire ne fait pas obstacle à la mise en œuvre de l'autorisation ; le bénéficiaire conserve ce récépissé et le présente à l'autorité compétente qui le demande.</p>
<p>Les dispositions du premier alinéa s'appliquent aux consignations effectuées à compter de l'expiration d'un délai de six mois suivant l'entrée en vigueur de la loi qui les institue. Pour les consignations antérieures, le bénéficiaire reste tenu d'adresser au maire le récépissé avant la mise en œuvre de l'autorisation, selon les règles précédemment applicables ; les récépissés déjà transmis n'ont pas à être envoyés une nouvelle fois. Le montant, l'affectation et les conditions de libération des sommes consignées ne sont pas modifiés.</p>
''',
    "Réforme de fond : suppression de l'envoi personnel du récépissé au maire et du blocage des travaux pour un retard de transmission lorsque la consignation est prouvée. La Caisse transmet directement le justificatif. La garantie financière de démolition face au recul du trait de côte, son montant et son affectation sont maintenus. Transition de six mois pour organiser la transmission directe, sans nouveau dépôt des reçus déjà transmis.",
    "Coordonner le troisième alinéa de L121-22-5, situé dans son II : il impose aujourd'hui l'envoi du récépissé par le bénéficiaire avant travaux ; la dérogation proposée le vise expressément. Le I définit les constructions concernées et demeure le renvoi du premier alinéa. Adapter les modalités réglementaires prises au titre du II pour la transmission directe par la Caisse des dépôts et consignations ; aucune dispense de consignation ni diminution du coût garanti n'est décidée. R424-6-1 continue de fixer la mention du montant selon sa formule ; l'exception au permis tacite de R*424-2 II subsiste. La preuve disponible et présentable remplace le blocage dû au seul acheminement du document.",
    removed=[
        "Obligation pour le bénéficiaire de transmettre lui-même au maire le récépissé de consignation, remplacée par la transmission directe de la Caisse des dépôts et consignations.",
        "Interdiction de commencer les travaux pour le seul retard de transmission du récépissé lorsque la consignation obligatoire est effectuée et prouvée par le récépissé détenu.",
    ])


assert len(sources) == 24
assert set(drafts) == {source['number'] for source in sources}
answer = []
for source in sources:
    item = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    item.update(drafts[source['number']])
    answer.append(item)
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
