import json, html, hashlib, os
from pathlib import Path
root=Path('legal-rewrite')
sources=json.loads((root/'runtime/sru-reglementaire/sources.json').read_text())
by={a['number']:a for a in sources}
rows=[]
policy='editorial_direction_2026_10_19'
common_notes="Source canonique et note DILA intégralement lues ; la note est vide pour cette version. Direction expresse : abroger les quotas communaux SRU et leurs mécanismes propres. Le IV et le V de L. 302-5 cités sont ceux de la proposition coordonnée : définition autonome du parc social et transition, non le droit actuellement en vigueur. Aucun inventaire de remplacement. Les règles étrangères à ce régime ne sont pas abrogées par cette proposition. Contrôle matériel du brouillon, sans validation juridique revendiquée."

def para(s):return '<p>'+html.escape(s,quote=False)+'</p>'
def add(number,paragraphs,reason,scope,notes='',repeal=True):
 a=by[number]
 row={k:a[k] for k in ('code_id','source_id','source_sha256','number')}
 row.update(proposed_xml='\n'.join(para(p) for p in paragraphs),reason=reason,review_notes=common_notes+' '+notes)
 if repeal:row.update(change_type='full_repeal',repeal_policy_id=policy,repeal_scope=scope)
 else:row.update(change_type='normative_reduction',reform_policy_id=policy,removed_provisions=scope)
 rows.append(row)

add('R302-1-3',[
"Le programme d'actions du programme local de l'habitat précise :",
"a) Les modalités de suivi et d'évaluation du programme ainsi que les conditions de mise en place de l'observatoire de l'habitat et du foncier prévu au III de l'article L. 302-1 ;",
"b) Les objectifs chiffrés de logements à réaliser ou à mobiliser, répartis par typologie, notamment pour les personnes mentionnées au II de l'article L. 301-1. Il localise l'offre nouvelle de logements et d'hébergement dans chaque commune et, lorsque de tels secteurs sont définis sur le territoire couvert par le programme, dans chaque secteur géographique ;",
"c) Les principales actions d'amélioration et de réhabilitation du parc public et privé existant ainsi que les dispositifs opérationnels envisagés pour les conduire. Ces actions et dispositifs sont précisés pour chaque commune et, le cas échéant, pour chaque secteur géographique défini sur le territoire couvert par le programme ;",
"d) Les opérations de rénovation urbaine et de requalification des quartiers anciens dégradés. Pour les opérations de rénovation urbaine, il précise les modalités de reconstitution de l'offre de logement social ;",
"e) Les interventions foncières nécessaires aux actions du programme.",
"Il indique, pour chaque commune et, le cas échéant, pour chaque secteur géographique défini sur le territoire couvert par le programme, les incidences éventuelles des actions retenues sur les plans locaux d'urbanisme et les cartes communales.",
"Il évalue les moyens financiers nécessaires à sa mise en œuvre et désigne, pour chaque type d'actions, les catégories d'intervenants chargées de leur réalisation."
],"Retirer du programme d'actions la déclinaison communale obligatoire du rattrapage SRU, tout en conservant l'ensemble de la programmation générale de l'habitat.",[
"Au b, suppression de l'obligation propre aux EPCI comportant des communes soumises aux quotas de fixer, pour chaque commune, le nombre de logements imposé par L. 302-8 sur la durée du programme."
],"Les objectifs chiffrés généraux, leur localisation, l'observatoire, la réhabilitation et la reconstitution de l'offre sociale en rénovation urbaine sont maintenus. Les opérations déjà engagées relèvent de la transition commune, sans nouvelle obligation de rattrapage.",False)

add('R302-7',[
"Dans les trois mois suivant la transmission de la délibération prévue à l'article R. 302-3, le préfet communique au président de l'établissement public de coopération intercommunale les informations utiles à l'élaboration du programme local de l'habitat. Elles portent notamment sur l'évolution démographique, le développement économique local, les options d'aménagement des schémas de cohérence territoriale ou des schémas directeurs et les objectifs à prendre en compte en matière d'habitat et de répartition équilibrée des différents types de logements dans l'agglomération concernée.",
"Il lui communique également les objectifs propres à certains quartiers, notamment à ceux couverts par les conventions pluriannuelles conclues avec l'Agence nationale de rénovation urbaine en application des articles 10 et 10-1 de la loi n° 2003-710 du 1er août 2003 d'orientation et de programmation pour la ville et la rénovation urbaine.",
"Pendant l'élaboration et la réalisation du programme, il transmet au président de l'établissement public les objectifs et informations nouveaux.",
"Le préfet ou son représentant est entendu à tout moment, à sa demande ou à celle de l'organe délibérant ou du président de l'établissement public. Lorsque le président l'entend, il en rend compte à l'organe délibérant."
],"Supprimer le porter à connaissance des quotas SRU, en maintenant les informations et objectifs nécessaires à la politique générale de l'habitat.",[
"Au premier alinéa, suppression de la mention des obligations résultant de L. 302-5 ; aucun quota ni objectif de rattrapage obligatoire n'est réintroduit par les informations du préfet."
],"Délai de trois mois, répartition équilibrée, objectifs ANRU, actualisation continue et conditions d'audition du préfet conservés. La loi du 1er août 2003, extérieure aux cinq codes, n'est pas modifiée.",False)

add('R302-14',[
"Le présent article est abrogé.",
"À l'entrée en vigueur de cette abrogation, cessent les procédures propres aux quotas communaux de logements sociaux relatives au décompte de population, aux ratios de demande et d'attribution, aux seuils de production, aux listes de communes ou de territoires assujettis et aux exemptions. Aucune liste, actualisation, demande d'exemption ou consultation nouvelle n'est établie ou poursuivie sur ce fondement.",
"Les données et actes antérieurs ne peuvent être utilisés au titre de ce régime que dans les limites du V de l'article L. 302-5, pour les créances nées de faits générateurs antérieurs et les recours ou restitutions qui s'y rapportent. Ils ne permettent aucun nouveau constat de carence, aucune nouvelle majoration ni aucune obligation de production fondés sur le seul défaut passé d'atteinte d'un quota."
],"Mettre fin aux critères d'assujettissement et d'exemption qui n'ont plus d'objet après la suppression des quotas SRU.","Abrogation intégrale des I à IV : définition de population propre au régime, ratios de tension, seuils, listes territoriales et communales, critères de croissance, exemptions, calendriers triennaux, transmissions et avis de la commission nationale.","Les règles générales de population du CGCT, le système national d'enregistrement des demandes de logement social et la taxe sur les logements vacants ne sont pas modifiés. La conservation éventuelle d'un périmètre géographique pour des règles d'urbanisme autonomes exige leur coordination propre, confiée à un autre rédacteur.")

add('R302-14-1',[
"Le présent article est abrogé.",
"À l'entrée en vigueur de cette abrogation, les établissements publics de coopération intercommunale n'ont plus à identifier des pôles de centralité, à établir les indicateurs d'isolement ou de faible attractivité ni à transmettre une proposition motivée d'exemption pour l'application des quotas communaux de logements sociaux.",
"Les procédures d'exemption encore en cours cessent sans déclaration de remplacement. Les pièces déjà établies ne peuvent servir, au titre du régime supprimé, qu'au traitement des créances antérieures, restitutions et recours préservés par le V de l'article L. 302-5."
],"Supprimer l'instruction et la justification des exemptions au régime de quotas abrogé.","Suppression de l'identification des pôles de centralité, de l'analyse des temps de transport, des cinq indicateurs de faible attractivité et de la transmission motivée des listes de communes proposées à l'exemption.","Les documents d'urbanisme, les schémas territoriaux et les données INSEE mentionnés dans la source conservent leurs fonctions autonomes ; aucune de ces règles extérieures n'est abrogée.")

add('R302-15',[
"I.-Abrogé.",
"II.-Abrogé.",
"III.-Pour l'application de la définition autonome des logements locatifs sociaux et assimilés du IV de l'article L. 302-5, les structures mentionnées au 4° de ce IV qui ne comprennent pas de logements autonomes sont comptées en logements équivalents. Le nombre retenu est la partie entière du nombre de lits de logements-foyers divisé par trois ou du nombre de places de centres d'hébergement et de réinsertion sociale ou de centres d'accueil pour demandeurs d'asile divisé par trois.",
"Dans ces structures, est autonome le logement qui remplit les conditions de l'article R. 151-1. Chacune de ces conditions constitue un élément de vie au sens de la dernière phrase du 4° du IV de l'article L. 302-5.",
"III bis.-Pour l'application du 5° du IV de l'article L. 302-5, chaque terrain familial locatif correspond à un logement équivalent.",
"IV.-Abrogé.",
"V.-Abrogé.",
"VI.-Abrogé.",
"Les inventaires et déclarations propres aux quotas communaux de logements sociaux prennent fin à l'entrée en vigueur de la réforme. Les équivalences définies aux III et III bis ne créent aucune obligation de recensement ou de déclaration supplémentaire. Pour la liquidation d'une créance née de faits générateurs antérieurs et maintenue par le V de l'article L. 302-5, seuls les justificatifs nécessaires à cette liquidation peuvent être demandés ; ils ne constituent pas un inventaire périodique de remplacement."
],"Abolir l'inventaire SRU et ses données déclaratives, tout en conservant les équivalences et conditions d'autonomie utilisées par les autres dispositifs de logement social.",[
"Au I, suppression de l'inventaire par bâtiment, de l'identification des propriétaires et gestionnaires, des données de localisation, de conventionnement et de financement et des tableaux de catégories dédiés au décompte SRU.",
"Au II, suppression des déclarations des dates d'expiration des conventions et de cession aux seules fins des assimilations dans l'inventaire SRU.",
"Au III bis, suppression de l'inventaire par les gestionnaires de terrains familiaux, des identités et localisations, de la date du rapport de vérification et de celle du bail ; maintien de la seule équivalence autonome d'un logement pour un terrain.",
"Aux IV, V et VI, suppression des inventaires et transmissions spécifiques de l'intermédiation locative, de la location-accession et des baux réels solidaires, y compris leur insertion dans le rapport OFS pour la seule finalité SRU."
],"Numérotation III et III bis conservée pour les équivalences autonomes. Diviseurs de trois, arrondi à la partie entière, référence aux conditions de R. 151-1 et équivalence un terrain/un logement intégralement conservés ; les durées et catégories du IV de L. 302-5 ne sont pas supprimées. Coordination nécessaire : R. 445-24 renvoie actuellement au 4° du I, catégorie de l'inventaire abrogé ; ce renvoi doit être remplacé sans supprimer les garanties CUS. R. 329-11 du code de l'urbanisme est coordonné par l'autre rédacteur. Les obligations de sécurité du décret n° 2019-1478 et la loi de location-accession n° 84-595 restent autonomes.",False)

add('R302-16',[
"Le présent article est abrogé.",
"Aucune dépense ni moins-value n'ouvre, à compter de cette abrogation, un droit à déduction au titre d'un prélèvement dont le fait générateur est postérieur à l'entrée en vigueur de la réforme.",
"Pour les seules créances nées de faits générateurs antérieurs et maintenues par le V de l'article L. 302-5, les déductions sont déterminées selon les catégories de dépenses, conditions d'affectation, modalités de calcul, plafonds et justificatifs applicables avant l'abrogation. Les droits à déduction opposables à ces créances ainsi que les recours et restitutions correspondants demeurent préservés. Les crédits de déduction inutilisés ne donnent lieu à aucun remboursement général.",
"L'abrogation ne remet pas en cause les opérations valablement engagées, les aides déjà attribuées ni les droits des occupants ou des tiers préservés par ce même V."
],"Supprimer le calcul de déductions d'un prélèvement SRU aboli, sans augmenter rétroactivement les dettes anciennes ni supprimer les aides et opérations engagées.","Abrogation du catalogue de dépenses et moins-values déductibles : subventions foncières et ZAC avec prorata, travaux et évictions sur biens communaux, moins-values de cession, intermédiation locative sous conditions et plafonds, investissements en aires d'accueil, de grand passage et terrains familiaux.","Les conditions anciennes restent applicables uniquement au calcul de créances réellement nées avant réforme : aucune nouvelle aide ou condition technique n'est créée. Les subventions et dispositifs autonomes des articles L. 321-4, L. 321-8, L. 365-4 et les règles des opérations d'aménagement ne sont pas abrogés.")

add('R302-16-1',[
"Le présent article est abrogé.",
"Le report des dépenses et moins-values déductibles ne peut servir à établir ou à compenser un prélèvement dont le fait générateur est postérieur à l'entrée en vigueur de la réforme.",
"Lorsqu'un report est opposable à une créance née de faits générateurs antérieurs et maintenue par le V de l'article L. 302-5, sa durée et son montant sont déterminés selon les règles en vigueur avant l'abrogation, y compris le calcul du rapport et son arrondi à l'entier supérieur. Les reports inutilisés ne sont pas transformés en créance de remboursement ; les recours et restitutions afférents aux créances antérieures restent préservés dans les limites de ce V."
],"Mettre fin aux reports de déductions d'un prélèvement aboli, en préservant leur effet sur les créances antérieures qui subsistent.","Suppression, pour les périodes nouvelles, du report au-delà de deux ans fondé sur le rapport entre logements réalisés et tiers de l'obligation triennale ainsi que de la durée maximale qui en résulte.","Aucun remboursement général d'un report devenu sans objet. Pour une liquidation historique maintenue, les règles exactes de rapport supérieur à trois et d'arrondi à l'entier supérieur demeurent celles de la rédaction antérieure.")

add('R302-16-2',[
"Le présent article est abrogé.",
"Le plafond de déduction des dépenses d'intermédiation locative ne s'applique plus à un prélèvement dont le fait générateur est postérieur à l'entrée en vigueur de la réforme.",
"Pour la seule liquidation des créances antérieures maintenues par le V de l'article L. 302-5 et des recours ou restitutions correspondants, le plafond applicable aux dépenses reste celui de la rédaction antérieure : 10 000 euros par logement et par an dans les communes d'Ile-de-France et de Provence-Alpes-Côte d'Azur, et 5 000 euros par logement et par an dans les autres communes."
],"Supprimer le plafond propre aux déductions du prélèvement SRU, sans changer les plafonds opposables à la liquidation des anciennes créances.","Abrogation, pour les faits générateurs nouveaux, des plafonds géographiques annuels de déduction des dépenses d'intermédiation locative liés au prélèvement supprimé.","Les deux montants, leur périodicité et leur champ géographique sont reproduits exactement pour la transition historique ; il ne s'agit pas d'un plafond général des aides à l'intermédiation locative.")

add('R302-17',[
"Le présent article est abrogé.",
"À l'entrée en vigueur de cette abrogation, cessent l'envoi annuel de l'état des dépenses et moins-values déductibles, sa certification et ses annexes ainsi que son annexion au budget primitif, lorsqu'ils ont pour seul objet le prélèvement SRU supprimé. Aucune déclaration périodique de remplacement n'est exigée.",
"Pour liquider une créance née de faits générateurs antérieurs et maintenue par le V de l'article L. 302-5, ou statuer sur le recours ou la restitution qui s'y rapporte, seuls les justificatifs nécessaires à cette créance peuvent être demandés. Ce traitement ponctuel ne rétablit ni l'échéance annuelle du 31 octobre ni une annexe budgétaire propre au régime abrogé."
],"Supprimer le dossier déclaratif annuel des dépenses déductibles du prélèvement SRU.","Suppression de l'état annuel certifié à transmettre avant le 31 octobre, des données par opération et des pièces annexées, ainsi que de l'obligation d'annexion au budget primitif pour le calcul du prélèvement aboli.","Les règles ordinaires de comptabilité, d'archivage et de preuve subsistent selon leur droit propre. La transition autorise seulement les pièces nécessaires à une créance antérieure effectivement maintenue, et non un nouveau dossier annuel pour tout l'ancien régime.")

add('R302-18',[
"Le présent article est abrogé.",
"Aucune reprise de déduction ne peut naître d'un défaut de commencement d'exécution dont le délai de deux ans expire après l'entrée en vigueur de la réforme. Une déduction pratiquée avant cette date ne suffit pas à créer une telle créance.",
"Les reprises ou rectifications légalement nées de faits générateurs antérieurs ne subsistent que dans les limites du V de l'article L. 302-5, même si leur échéance ou leur encaissement est ultérieur. Pour leur examen, les conditions de déduction et la définition du commencement d'exécution demeurent celles de la rédaction antérieure : signature de la convention prévue à l'article L. 831-1, ou, pour les terrains familiaux locatifs et les aires permanentes d'accueil ou de grand passage, déclaration d'ouverture de chantier, ou, pour les logements non conventionnés mobilisés en intermédiation locative, mise en location.",
"La liquidation d'une créance antérieure n'autorise ni nouveau prélèvement pour un fait générateur postérieur ni nouveau constat de carence ou nouvelle majoration fondés sur le seul défaut passé d'atteinte d'un quota. Les règles relatives aux recours, restitutions et sanctions non définitives prévues au V de l'article L. 302-5 demeurent applicables."
],"Abolir les reprises futures de déductions SRU tout en distinguant les créances anciennes des manquements dont le fait générateur surviendrait après réforme.","Suppression des reprises nouvelles pour absence de commencement d'exécution dans les deux ans et du mécanisme permanent d'ajout au prélèvement suivant des dépenses indûment déduites ; maintien limité aux reprises ou rectifications déjà légalement nées de faits antérieurs.","La date d'une déduction ancienne n'est pas assimilée au fait générateur d'une reprise. L'expiration postérieure du délai de deux ans ne produit aucune dette nouvelle. La référence aux dépenses hors champ n'autorise pas à qualifier automatiquement de créance née toute vérification ultérieure : naissance légale à examiner selon les faits et le V proposé.")

add('R302-18-1',[
"Le présent article est abrogé.",
"La définition des dépenses réelles de fonctionnement propre au plafonnement des prélèvements et majorations SRU cesse de s'appliquer pour les faits générateurs postérieurs à l'entrée en vigueur de la réforme.",
"Pour les seules créances antérieures maintenues par le V de l'article L. 302-5 et les recours ou restitutions correspondants, le calcul reste soumis aux exclusions de la rédaction antérieure : productions immobilisées, charges transférées en section d'investissement, prélèvements alimentant les fonds de péréquation correspondant à des atténuations de produits et prélèvement SRU lui-même."
],"Retirer une définition comptable qui servait exclusivement au calcul des plafonds du régime SRU aboli.","Abrogation du retraitement spécifique des dépenses réelles de fonctionnement servant aux plafonds du prélèvement et des majorations SRU, avec sauvegarde limitée au calcul des créances anciennes.","Les exclusions sont conservées exactement pour les seules liquidations historiques. La définition des dépenses de fonctionnement dans les autres régimes de finances locales n'est pas modifiée.")

add('R302-19',[
"Le présent article est abrogé.",
"Aucune imputation sur les attributions mentionnées au premier alinéa de l'article L. 2332-2 du code général des collectivités territoriales ne peut être effectuée au titre d'un prélèvement dont le fait générateur est postérieur à l'entrée en vigueur de la réforme.",
"Pour une créance de prélèvement légalement née de faits générateurs antérieurs et maintenue par le V de l'article L. 302-5, l'imputation demeure effectuée par neuvième, de mars à novembre, dans les conditions antérieurement applicables. Les échéances postérieures à l'entrée en vigueur ne constituent pas, à elles seules, de nouveaux faits générateurs. L'abrogation n'entraîne ni exigibilité anticipée du solde ni remboursement général des versements ; les prescriptions, recours et restitutions restent régis par ce même V."
],"Arrêter les prélèvements futurs tout en conservant l'échelonnement de paiement des créances annuelles nées avant réforme.","Suppression du mécanisme annuel d'imputation et des neuf retenues sur attributions fiscales communales pour les nouveaux faits générateurs ; maintien transitoire du seul échéancier des créances légalement nées antérieurement.","Point de coordination transmis au rédacteur législatif : les neuf échéances de mars à novembre ne sont pas neuf faits générateurs. Une créance annuelle antérieure peut continuer à être payée après entrée en vigueur. Le CGCT n'est pas prétendu modifié par cet article.")

add('R302-19-1',[
"Le présent article est abrogé.",
"À l'entrée en vigueur de cette abrogation, aucune nouvelle contribution communale obligatoire ne peut être créée sur le fondement d'une opération imposée au titre d'un constat de carence dont les effets futurs ont cessé. Un avenant ne peut, sur ce seul fondement, imposer une opération nouvelle ou accroître les obligations d'une commune.",
"Les contrats et opérations valablement engagés, les droits des opérateurs et des tiers et les aides déjà attribuées sont préservés dans les limites du V de l'article L. 302-5. Les créances publiques légalement nées de faits générateurs antérieurs restent liquidées selon les règles et plafonds antérieurement applicables et peuvent être recouvrées après l'entrée en vigueur, selon le décret n° 2012-1246 du 7 novembre 2012 relatif à la gestion budgétaire et comptable publique, notamment ses articles 112 à 124. Un titre émis après l'entrée en vigueur ne peut avoir pour objet que le recouvrement d'une telle créance antérieure maintenue ; il ne crée pas une contribution nouvelle.",
"Ces dispositions transitoires n'autorisent ni nouveau constat de carence ni nouvelle majoration à raison du seul défaut passé d'atteinte d'un quota. Les prescriptions, recours, restitutions et règles de droit répressif plus doux restent soumis au V de l'article L. 302-5."
],"Supprimer les contributions obligatoires attachées à la carence et leurs nouvelles mises en recouvrement, sans anéantir les engagements valables ni les créances nées avant réforme.","Suppression du calcul permanent de la contribution communale obligatoire par référence aux aides R. 331-15 et R. 331-25-1, ainsi que des titres de perception propres aux opérations forcées du régime de carence aboli.","Les droits contractuels et créances des opérateurs pour des opérations déjà engagées sont distingués de la création interdite de nouvelles opérations forcées. Les plafonds anciens ne sont utilisés que pour des créances légalement maintenues. Le décret GBCP conserve sa portée autonome ; il n'est pas abrogé.")

add('R302-20',[
"Le présent article est abrogé.",
"À l'entrée en vigueur de cette abrogation, les bénéficiaires des reversements de prélèvements SRU n'établissent plus le rapport annuel propre à ce régime et ne le transmettent plus au représentant de l'Etat. Cette suppression s'applique également aux rapports portant sur des sommes antérieurement reçues ; aucun état périodique de remplacement n'est exigé.",
"Les aides déjà attribuées, contrats et opérations valablement engagés demeurent préservés dans les conditions du V de l'article L. 302-5. Les obligations de comptabilité et de contrôle résultant de leurs régimes propres subsistent. Pour la seule liquidation d'une créance antérieure maintenue par ce V ou le traitement des recours et restitutions qui s'y rapportent, les justificatifs strictement nécessaires peuvent être demandés sans rétablir le rapport annuel supprimé."
],"Abolir le rapport annuel d'utilisation des reversements SRU, y compris pour les soldes anciens, sans supprimer le contrôle ordinaire des fonds publics.","Suppression du rapport cumulatif des sommes reçues, engagées et inutilisées, des principes d'utilisation, de la liste détaillée des opérations et des perspectives d'emploi des soldes, ainsi que de sa transmission annuelle au préfet.","Aucun suivi annuel SRU supplémentaire des soldes historiques n'est réintroduit. Les droits et obligations d'opérations valablement engagées et les contrôles autonomes des aides ne sont pas supprimés.")

add('R302-26',[
"Le présent article est abrogé.",
"À l'entrée en vigueur de cette abrogation, prennent fin les missions, mandats, désignations et fonctions de secrétariat de la commission nationale propres au contrôle des quotas communaux de logements sociaux. Aucun membre n'est nommé ou renouvelé pour ces missions.",
"Les procédures d'exemption, de rattrapage et de carence encore pendantes cessent lorsqu'elles n'ont d'autre objet que le respect des quotas supprimés. Le traitement des créances antérieures, recours et restitutions préservés par le V de l'article L. 302-5 ne rétablit ni cette commission ni ses consultations et ne permet aucun nouvel arrêté de carence fondé sur un quota passé."
],"Supprimer l'organe national et les procédures consultatives propres aux quotas et à la carence SRU.","Abrogation des règles de présidence, désignation et nomination des membres, des mandats de trois ans renouvelables, du fonctionnement collégial et du secrétariat ministériel de la commission SRU.","Les règles générales des commissions administratives du code des relations entre le public et l'administration ne sont pas abrogées. Les recours relèvent des voies de droit ordinaires, sans commission SRU transitoire de remplacement.")

add('R362-2',[
"Le comité régional de l'habitat et de l'hébergement est également consulté sur les actes, demandes et bilans suivants :",
"1° Le projet annuel de répartition des crédits publics entre établissements publics de coopération intercommunale et départements, établi par le préfet de région en application du troisième alinéa de l'article L. 301-3 ;",
"2° Les projets de programmes locaux de l'habitat prévus à l'article L. 302-2, les projets de plans locaux d'urbanisme intercommunaux tenant lieu de programmes locaux de l'habitat en application de l'article L. 153-16 du code de l'urbanisme et le projet de plan métropolitain de l'habitat et de l'hébergement tenant lieu de programme local de l'habitat en application du V de l'article L. 5219-1 du code général des collectivités territoriales ;",
"3° Les bilans prévus à l'article L. 302-3 ;",
"4° La décision du représentant de l'Etat dans le département ou la région, selon le cas, de dénoncer une convention de délégation en application du II de l'article L. 301-5-1 ou du III de l'article L. 302-4-2 ;",
"5° Abrogé.",
"6° La création, la dissolution ou la modification des compétences d'un organisme d'habitations à loyer modéré qui exerce ou demande à exercer son activité dans la région. La consultation n'est toutefois pas requise lorsque la dissolution ou la modification des compétences est prononcée à titre de sanction en application de l'article L. 342-14 ;",
"7° Les projets de plans départementaux d'action pour le logement et l'hébergement des personnes défavorisées ;",
"8° Les demandes d'agrément ou de modification d'agrément concernant la maîtrise d'ouvrage prévue à l'article L. 365-2 ;",
"9° Le bilan présenté par le délégué régional de l'Agence nationale de l'habitat ou son représentant sur l'utilisation des aides au parc privé, des aides à la lutte contre l'habitat indigne dans ce parc et des aides aux établissements d'hébergement prévues au III de l'article R. 321-12 ;",
"10° L'arrêté du représentant de l'Etat dans la région prévu au second alinéa du III de l'article 199 novovicies du code général des impôts ;",
"11° L'arrêté du représentant de l'Etat dans la région prévu au deuxième alinéa du IV de l'article 199 novovicies du code général des impôts ;",
"12° La demande d'agrément d'un observatoire des loyers prévue au troisième alinéa de l'article 16 de la loi n° 89-462 du 6 juillet 1989 ;",
"13° La liste des terrains mobilisables en faveur du logement établie par le représentant de l'Etat dans la région en application du 2° du II de l'article L. 3211-7 du code général de la propriété des personnes publiques ;",
"14° Les rapports annuels des représentants de l'Etat dans les départements de la région sur l'application du supplément de loyer, prévus à l'article L. 441-10 ;",
"15° Les rapports annuels sur les ventes de logements d'habitation à loyer modéré établis par les représentants de l'Etat dans les départements de la région et, le cas échéant, par les présidents de conseil des métropoles, en application des articles L. 443-7 et L. 443-15-2 ;",
"16° Les rapports annuels d'activité des fonds de solidarité pour le logement prévus à l'article 6 de la loi n° 90-449 du 31 mai 1990 ;",
"17° Les projets d'intérêt majeur prévus au 2° de l'article L. 350-3 du code de l'urbanisme ;",
"18° En Ile-de-France, la décision de déléguer aux établissements publics de coopération intercommunale l'attribution des aides à la pierre en application de l'article L. 302-13 ; le cahier des charges régional établi par le représentant de l'Etat dans la région auquel doivent se conformer les dispositifs de l'article L. 441-2-7 ; et, sur proposition du préfet de région, les critères de cotation susceptibles d'être communs aux territoires mettant en œuvre le système prévu à l'article L. 441-2-8, afin d'accompagner les réflexions propres à chacun de ces territoires ;",
"19° Les créations ou extensions des établissements publics fonciers de l'Etat ou locaux prévues aux articles L. 321-2, L. 324-2 et L. 324-2-1 A du code de l'urbanisme ;",
"20° Le bilan annuel des actions des établissements publics fonciers de l'Etat prévu à l'article L. 321-6 du code de l'urbanisme, celui des établissements publics fonciers locaux prévu à l'article L. 324-2-2 du même code et celui de l'office foncier de la Corse mentionné à l'article L. 4424-26-1 du code général des collectivités territoriales, ainsi que les modalités d'intervention et moyens de ces établissements et de l'office définis dans leurs programmes pluriannuels d'intervention ;",
"21° Abrogé.",
"Le comité peut déléguer tout ou partie des compétences prévues aux 2° à 21° à son bureau ou aux commissions spécialisées mentionnées aux articles R. 362-11 et R. 362-15.",
"Chaque année, le préfet de région communique au comité les éléments prévus au septième alinéa de l'article L. 443-13."
],"Abroger l'avis du comité régional sur les arrêtés de carence SRU, sans créer de consultation obligatoire sur les bilans généraux du PLH et sans modifier les autres compétences du comité.",[
"Au 5°, abrogation de la consultation sur les projets d'arrêtés de carence de L. 302-9-1, effectuée au vu des bilans triennaux. La source n'imposait pas une consultation distincte sur le bilan lui-même ; aucune consultation obligatoire nouvelle n'est créée."
],"Distinction corrigée après relecture intégrale du 5° source : le comité était consulté sur les arrêtés de carence au vu des bilans, et non obligatoirement sur les bilans eux-mêmes. Le 5° est donc abrogé sans compétence de remplacement. La communication du bilan général au comité demeure prévue au L. 302-9 proposé par le coordinateur. Les 1° à 4° et 6° à 20°, l'abrogation préexistante du 21°, la faculté de délégation et l'information annuelle sont conservés. La plage de délégation 2° à 21° et la plage de renvois de R. 371-1 incluent des entrées abrogées sans rétablir leur compétence. Les renvois fiscaux et les lois n° 89-462, n° 90-449 ainsi que le CG3P et le CGCT ne sont pas prétendus réécrits par cette seule coordination.",False)

assert len(rows)==16 and len({a['source_id'] for a in rows})==16
rows.sort(key=lambda a:next(i for i,s in enumerate(sources) if s['source_id']==a['source_id']))
path=root/'runtime/sru-reglementaire/articles.candidates.json'
temp=path.with_suffix('.json.tmp');temp.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');temp.replace(path)
print('Authored candidates:',len(rows),'full repeals:',sum(r['change_type']=='full_repeal' for r in rows),'reductions:',sum(r['change_type']=='normative_reduction' for r in rows))
# Coordination additionnelle explicitement attribuée par le coordinateur.
a=json.loads((root/'runtime/sru-reglementaire/r445-24.source.json').read_text())
paragraphs=[
"Pour calculer la part du patrimoine de l'organisme relevant des articles L. 633-1 et R. 832-20, ce patrimoine est exprimé en logements équivalents. Les logements, lits, places et chambres mentionnés au 4° du IV de l'article L. 302-5 sont retenus selon les règles d'équivalence et d'autonomie du III de l'article R. 302-15. Cette référence aux catégories et équivalences ne crée aucune obligation d'inventaire liée aux quotas communaux abrogés.",
"Si moins de 50 % de ce patrimoine relève des articles L. 633-1 et R. 832-20, la convention d'utilité sociale de l'organisme comprend, pour la catégorie autonome des logements-foyers, le tableau prévu à l'article R. 445-36, dûment renseigné.",
"Si la part de ce patrimoine relevant des articles L. 633-1 et R. 832-20 est au moins égale à 50 % et inférieure à 100 %, la convention comporte une partie intitulée « logements-foyers », constituée des éléments prévus aux articles suivants de la présente sous-section.",
"Si la totalité du patrimoine relève des articles L. 633-1 et R. 832-20, la convention d'utilité sociale « logements-foyers » est constituée des éléments prévus aux articles suivants de la présente sous-section."
]
r={k:a[k] for k in ('code_id','source_id','source_sha256','number')}
r.update(proposed_xml='\n'.join(para(p) for p in paragraphs),
reason="Coordonner les équivalences autonomes avec la suppression de l'inventaire SRU et supprimer le renvoi obsolète au tableau de R. 445-37 déjà abrogé, tout en conservant R. 445-36, les seuils et le contenu autonome des conventions d'utilité sociale.",
review_notes=common_notes.replace("la note est vide pour cette version", "la note DILA non vide indique l'application aux contributions et prestations dues à compter du 1er janvier 2022, conformément à l'article 6 du décret n° 2021-1750 du 21 décembre 2021")+" Source canonique et éventuel brouillon antérieur lus intégralement ; aucun brouillon antérieur présent lors de la rédaction. Le renvoi source au 4° du I de R. 302-15 désignait les logements, lits, places et chambres du 4° du IV de L. 302-5 ; leurs équivalences restent au III de R. 302-15. Le III bis, relatif aux terrains familiaux, n'est pas pertinent pour les logements-foyers. Les seuils moins de 50 %, au moins 50 % et moins de 100 %, et totalité du patrimoine, le tableau de R. 445-36 et le contenu autonome des conventions sont conservés. Coordination supplémentaire expressément attribuée après lecture par le coordinateur : suppression de l'ancien renvoi facultatif au tableau de R. 445-37 au titre de la suppression des charges obsolètes. Statut, document complet et note vérifiés dans le corpus canonique : LEGIARTI000034661611, état ABROGE, fin de validité 29 juillet 2019, empreinte b6f534364bf6b43b6fcc6f9a9f2dab901dcdeab81932fbf122390bbe2312ef2b. Aucun tableau abrogé n'est réactivé. La note DILA 2022 de R. 445-24 demeure conservée dans la preuve source et n'est pas transformée en nouvelle règle CUS.",
change_type='normative_reduction',reform_policy_id=policy,
removed_provisions=["Suppression du renvoi au 4° du I de R. 302-15, ancienne catégorie de l'inventaire SRU, remplacé par le 4° du IV de L. 302-5 et le III de R. 302-15 autonomes.","Suppression de la mention du tableau facultatif de R. 445-37 : cet article est déjà abrogé depuis le 29 juillet 2019 dans le corpus canonique ; aucun tableau inapplicable ne doit être réactivé."])

rows.append(r)
# Évite le cas-limite du jour d'entrée en vigueur : aucune naissance nouvelle dès cette date.
for r in rows:
 if r['number']=='R302-18':r['proposed_xml']=r['proposed_xml'].replace("dont le délai de deux ans expire après l'entrée en vigueur de la réforme", "dont le délai de deux ans expire à compter de l'entrée en vigueur de la réforme")
assert len(rows)==17 and len({a['source_id'] for a in rows})==17
temp=path.with_suffix('.json.tmp');temp.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');temp.replace(path)
print('Additional coordination R445-24; total',len(rows))
