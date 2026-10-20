import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sources = json.loads((ROOT / 'source.json').read_text())

# Motifs et points de contrôle propres à chaque article, dans l'ordre des sources.
metadata = [
    (
        "Réécriture à droit constant : les deux plafonds de dépenses d'hébergement sont présentés séparément par territoire, sans modifier l'assiette ni le renvoi au crédit d'impôt.",
        "Plafonds conservés : 270 € pour Paris, les Hauts-de-Seine, la Seine-Saint-Denis et le Val-de-Marne ; 200 € pour les autres départements. Le renvoi au i du 1° du III de l'article 220 sexdecies est conservé. Aucune unité supplémentaire de plafonnement n'est ajoutée à celle de la source."
    ),
    (
        "Réécriture à droit constant : le format, le délai et l'auteur de la déclaration sont exprimés dans des phrases distinctes. Le rôle de la société mère et l'inclusion de ses propres crédits sont explicites.",
        "Les deux alinéas sont conservés. Les délais restent ceux de la déclaration annuelle de résultat de l'article 223 ; la déclaration du groupe intervient lors du dépôt du résultat d'ensemble. Le périmètre reste celui de l'article 223 A, sans extension à un autre régime de groupe."
    ),
    (
        "Réécriture à droit constant : la phrase exprime directement l'ordre d'imputation du crédit d'impôt, sans modifier les prélèvements et crédits prioritaires.",
        "Conserver l'imputation après les prélèvements non libératoires et les crédits d'impôt non restituables. Aucun taux ni régime nouveau n'est introduit dans le crédit de l'article 220 sexdecies."
    ),
    (
        "Réécriture à droit constant : l'obligation de présentation au bilan est formulée directement ; la réserve et son sous-compte distinct restent identiques.",
        "Renvoi vérifié dans le corpus : le septième alinéa du f du I de l'article 219 concerne bien la réserve spéciale. Le régime est historique et ses limites temporelles demeurent celles de l'article 219 ; la réécriture ne rouvre aucune option et n'applique pas rétroactivement la réforme du taux normal."
    ),
    (
        "Réécriture à droit constant : l'obligation de joindre les documents est formulée à l'actif, et les trois pièces restent identifiées sous les lettres a, b et c. Le premier exercice auquel se rattache l'engagement est explicité.",
        "Conserver les trois exercices bénéficiaires, les modèles administratifs et le suivi des bénéfices à incorporer au capital. Le f du I de l'article 219 contient un dispositif historique fermé aux nouvelles options selon ses propres règles ; ni la baisse proposée du taux normal ni le réexamen des aides ne le réactivent ou ne le suppriment."
    ),
    (
        "Réécriture à droit constant : les deux états à joindre sont distingués et le contribuable débiteur de l'obligation est nommé dans chacun des deux alinéas. Le taux réduit n'est pas modifié.",
        "Les deux alinéas et les modèles administratifs sont maintenus. Le b du I de l'article 219 conserve son champ propre, distinct du taux national normal proposé à 20 %. La part territoriale de zéro à cinq points appelle des dispositions législatives propres sur son assiette, son vote, sa répartition entre établissements et la péréquation ; le présent article ne crée ni cette part ni un renvoi à un article inexistant."
    ),
    (
        "Réécriture à droit constant : les catégories de sociétés redevables de la première obligation sont séparées dans la phrase ; la seconde obligation indique d'abord les plus-values à détailler, puis la déclaration concernée.",
        "Les deux alinéas sont conservés. Au premier, le renvoi fiscal est le IV de l'article 219 ; au second, la dernière phrase du premier alinéa du IV est bien celle de l'article 208 C, vérifiée dans le corpus. Conserver la distinction entre option au titre des II et III bis, option au titre du seul II et transformation en société de placement à prépondérance immobilière à capital variable. Les taxations particulières ne sont pas assimilées au taux normal réformé."
    ),
    (
        "Réécriture à droit constant : les personnes tenues de joindre la copie sont désignées comme sujets, et les déclarations sont rattachées explicitement à l'exercice de cession ou de fusion. La condition de surface est conservée.",
        "I, II et les trois alinéas restent en place. Renvois vérifiés : premier alinéa du II de l'article 210 F pour l'engagement initial, quatrième alinéa pour la substitution de l'absorbante. La proportion déclarée reste celle de la surface totale affectée à l'habitation ; aucune condition du dispositif fiscal n'est remplacée par les orientations de simplification des autorisations d'urbanisme."
    ),
    (
        "Réécriture à droit constant : le classement des communes est énoncé directement, en conservant les deux zones et le renvoi au code de la construction et de l'habitation.",
        "Les zones A bis et A et l'avant-dernier alinéa du I de l'article 210 F sont conservés. L'article D. 304-1 du CCH définit le classement ; la zone A bis est incluse dans la zone A. La note source relative à l'ordonnance du 21 octobre 2019 et au décret du 21 août 2019 est une note de coordination historique, sans date d'effet à attribuer à une réforme future."
    ),
    (
        "Réécriture à droit constant : la demande initiale, son contenu, l'autorité compétente et le renouvellement sont exprimés dans quatre alinéas distincts, comme dans la source, avec des phrases plus courtes.",
        "Délais conservés : quatre ou six ans et dépôt au plus tard trois mois avant le terme initial, puis trois mois avant le terme de la prolongation initiale. Le renvoi final aux deux alinéas précédents est maintenu : il couvre le contenu de la demande et l'autorité compétente. La source rattache l'explication des travaux au délai initial, même pour le renouvellement par ce renvoi ; cette formulation préexistante mérite une clarification coordonnée si l'on souhaite viser expressément le terme de la première prolongation."
    ),
    (
        "Réécriture à droit constant : les renvois successifs sont rendus plus lisibles et les montants du loyer, des ressources et des coûts justifiés sont exprimés directement. Les trois alinéas restent distincts.",
        "L'article 140 nonies de l'annexe II a été vérifié : documents au premier alinéa, changement de locataire au deuxième et plafonds au troisième. Renvois conservés : II de 46 AG quaterdecies, 1° du I de 217 undecies, 1 et 2 de 46 AG duodecies, sixième alinéa du I de 217 undecies et VI de 46 AG sexdecies. Le montant réel et justifié demeure exigé. Aucun assouplissement général du logement n'est étendu à cette déduction outre-mer."
    ),
    (
        "Réécriture à droit constant : le ministre et l'arrêté deviennent le sujet de la phrase, qui conserve la définition réglementaire des véhicules strictement indispensables.",
        "Le renvoi reste le troisième alinéa du I de l'article 217 undecies, vérifié dans le corpus. L'arrêté doit être lu dans les limites législatives de cet alinéa ; la réécriture n'élargit pas les véhicules ou activités éligibles."
    ),
    (
        "Réécriture à droit constant : la définition du sous-groupe est formulée directement et les attributs de présentation non autorisés sont supprimés.",
        "Conserver les trois composantes de la définition : ensemble d'entités, même État ou territoire, détermination distincte du taux effectif prévue par la loi. La réforme du taux national normal de l'IS ne modifie pas cette définition d'imposition minimale mondiale."
    ),
    (
        "Réécriture à droit constant : le cadre déclaratif est posé en début de phrase, puis les deux indications supplémentaires sont exposées. Le caractère conditionnel de l'identification d'une entité désignée est conservé.",
        "Le I de l'article 223 WW vise les éléments déjà déclarés ; son III vise le relevé de liquidation. L'identité de l'entité désignée reste liée à l'option de l'article 1679 decies. L'alinéa unique et la distinction déclaration de résultat/relevé de liquidation sont conservés."
    ),
    (
        "Réécriture à droit constant : l'obligation de dépôt et ses modalités sont réparties en deux phrases dans le même alinéa, avec identification explicite des entités concernées.",
        "Conserver l'alternative entre l'entité de l'article 223 WW et, le cas échéant, celle de l'article 223 WW bis, ainsi que le modèle administratif et les conditions et délais du II de l'article 223 WW. Le contenu et les modalités des articles 46 quater-0 ZZD à ZZG restent coordonnés sur cette déclaration."
    ),
    (
        "Réécriture à droit constant de l'intégralité de la déclaration : les listes de données sont introduites par des formulations directes, les phrases complexes sont scindées sans déplacer d'alinéa, et la répartition du résultat d'une entité interposée est distinguée de celle d'un établissement stable. Les cinq états sont rédigés en fragments puis assemblés intégralement.",
        "Les 54 alinéas, les 1° à 5°, leurs lettres et les conditions i à iv du b du 4° sont conservés. Les euros ou la monnaie consolidée restent permis. Les champs de données, options, régimes de protection, règles transitoires, exclusions et renvois sont maintenus, notamment l'exclusion des entités entrées ou sorties dans la déclaration agrégée. La syntaxe elliptique du d du 4° est explicitée à partir des deux familles de renvois, 223 VQ à VQ quinquies et 223 VR à VR sexies, vérifiées dans le corpus. Les mentions d'impôt complémentaire additionnel au a, au c et au d du 5° sont maintenues malgré leur répétition. Aucune baisse automatique de cette imposition internationale ne découle de la réforme du taux normal de l'IS."
    ),
    (
        "Réécriture à droit constant : l'option et ses deux conditions cumulatives sont formulées directement ; la portée des données agrégées et l'obligation individuelle dérogatoire sont explicitées, sans supprimer aucun des douze postes du III.",
        "Conserver les 20 alinéas et les I à III. Bornes cumulatives : ouverture au plus tard le 31 décembre 2028 et clôture au plus tard le 30 juin 2030 ; absence d'impôt nécessitant une répartition. Le II reste agrégé et net, le III individuel. Les renvois au III sont maintenus, y compris 223 WQ et WQ bis au 4°, WQ bis et WR bis au 7°, et VW à VW sexies au 8°, sans les confondre avec les références plus larges de l'article ZZD. Le renvoi structurel du 1° du III ne nomme pas le chapitre II bis, dans lequel le corpus situe la sous-section 3 « Transferts d'actifs et de passifs » de la section VI ; cette imprécision préexistante est conservée et appelle un contrôle de coordination. Ces dates existantes ne sont pas des dates de la réforme proposée."
    ),
    (
        "Réécriture à droit constant : les droits de réception des informations sont exprimés directement pour chaque catégorie de destinataires. Les deux dérogations sont conservées dans leurs alinéas respectifs.",
        "Les six alinéas restent en place. Vérifier conjointement le h du 1° et le g du 5° de l'article 46 quater-0 ZZD, conservés aux mêmes emplacements. L'intégralité reçue par l'État de l'entité mère ultime demeure conditionnelle ; l'exclusion de la synthèse h pour l'impôt national seul et la limitation lorsque le pourcentage d'attribution est de zéro sont maintenues."
    ),
    (
        "Réécriture à droit constant : le ministre est le sujet de l'obligation et les trois conditions d'inscription sur la liste sont distinguées dans le même alinéa.",
        "Conserver la correspondance respective des 31°, 41° et 42° de l'article 223 VK avec les trois instruments qualifiés. L'adoption de l'instrument, l'accord avec la France et le respect de cet accord restent cumulatifs. Aucune liste d'États ni aucun accord nouveau n'est créé."
    ),
    (
        "Réécriture à droit constant : la société, l'acte de notification, le service destinataire et le délai sont placés dans une phrase principale ; le champ familial et les activités figurent dans la même subdivision, sans déplacement d'alinéa.",
        "Notification toujours antérieure à l'ouverture de l'exercice et activités industrielle, commerciale, artisanale ou agricole inchangées. Décalage préexistant vérifié dans le corpus : l'article 239 bis AA vise aussi les partenaires liés par un PACS, absents de l'énumération de l'article 46 terdecies A. Ce décalage est signalé sans modifier silencieusement cette énumération ; sa mise en cohérence appelle une coordination expresse de 46 terdecies A et de ses renvois, notamment 46 terdecies B et D."
    ),
    (
        "Réécriture à droit constant : les conditions de l'effet immédiat sont séparées en phrases courtes ; les deux opérations assimilées et l'acte correspondant sont explicités dans le second alinéa.",
        "Les deux alinéas, l'effet en droit d'apport et en impôt sur les bénéfices, les liens de parenté, la copie au service et l'absence de personne morale nouvelle sont conservés. Le renvoi aux personnes parentes de 46 terdecies A garde son champ source ; le décalage de cet article avec les partenaires de PACS visés à 239 bis AA appelle une coordination expresse, non une extension implicite dans la présente réécriture."
    ),
    (
        "Réécriture à droit constant : la notification et sa date limite sont énoncées en deux phrases ; le caractère définitif de la renonciation reste dans le second alinéa.",
        "La date limite reste antérieure à l'ouverture du premier exercice d'application de la renonciation. L'interdiction d'opter à nouveau est maintenue. Ne pas confondre ce régime avec la notification dans les trois premiers mois prévue pour l'option distincte de l'article 239 bis AB."
    ),
    (
        "Réécriture à droit constant : l'obligation de signature par tous les associés est énoncée à l'actif, puis les mentions obligatoires sont réparties en phrases lisibles au sein du même alinéa.",
        "Les notifications des articles 46 terdecies A et C sont toutes deux couvertes. La raison sociale, les deux lieux éventuels, la répartition du capital et toutes les données d'identité et de parenté sont conservés. La question des partenaires de PACS signalée pour 46 terdecies A doit aussi être examinée pour la mention du lien entre associés, sans dispense de signature créée ici."
    ),
    (
        "Réécriture à droit constant : les sociétés, les associés signataires et les pièces à joindre sont identifiés directement. Les informations relatives au capital et aux fonctions de direction restent détaillées sous les six numéros du II, et la renonciation demeure au III.",
        "Les 12 alinéas et les I à III sont conservés. Seuils inchangés : au moins 50 % au 4° et au moins 34 % au 5°, portant chacun sur le capital et les droits de vote. Les dates d'appréciation, la liste à l'ouverture, les variations de l'exercice, les exclusions de signataires et les calculs du deuxième alinéa du I de 239 bis AB sont maintenus. La note source du décret n° 2022-1014 du 19 juillet 2022 est historique ; elle ne fixe aucune date future. Le présent article ne réécrit pas les délais d'option ou de renonciation fixés par 239 bis AB."
    ),
]

assert len(sources) == len(metadata) == 24
answer = []
for index, (source, (reason, notes)) in enumerate(zip(sources, metadata)):
    if index == 15:
        fragments = [ROOT / 'drafts' / f'15-{part}.xml' for part in range(1, 6)]
        xml = '\n'.join(fragment.read_text().strip() for fragment in fragments)
        (ROOT / 'drafts' / '15.xml').write_text(xml + '\n')
    else:
        xml = (ROOT / 'drafts' / f'{index:02d}.xml').read_text().strip()
    entry = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    entry.update(proposed_xml=xml, reason=reason, review_notes=notes, status='rewrite_draft')
    answer.append(entry)
(ROOT / 'answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
