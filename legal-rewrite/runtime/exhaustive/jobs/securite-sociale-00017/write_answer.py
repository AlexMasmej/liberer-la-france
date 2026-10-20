import json
from pathlib import Path


def paragraphs(*items):
    return '\n'.join('<p>' + item + '</p>' for item in items)


drafts = {}


def draft(number, text, reason, notes):
    assert number not in drafts
    drafts[number] = dict(proposed_xml=text, reason=reason,
                          review_notes=notes, status='rewrite_draft')


draft('L161-8', paragraphs(
    "Les personnes qui ne remplissent plus les conditions d'activité requises pour être affiliées à l'assurance maladie, maternité, invalidité et décès du régime dont elles relevaient conservent leur droit aux prestations en espèces pour ces risques pendant une durée fixée par décret. Ce maintien s'applique tant qu'elles continuent de remplir les conditions de résidence et de séjour mentionnées à l'article L. 111-2-3 et ne justifient pas à nouveau des conditions d'ouverture du droit aux mêmes prestations, dans ce régime ou dans un autre régime. Pour les personnes relevant de l'article L. 5411-1 du code du travail, cette durée est prolongée dans les conditions fixées par décret.",
    "Ce maintien des droits bénéficie également aux assurés qui établissent à nouveau qu'ils remplissent, au titre de leur nouvelle activité, les conditions d'ouverture du droit aux indemnités journalières de maladie, mais dont les indemnités journalières sont nulles.<br/><br/>Les assurés qui établissent à nouveau qu'ils remplissent, au titre de leur nouvelle activité, les conditions d'ouverture du droit aux indemnités journalières de maternité peuvent également bénéficier de ce maintien lorsque les indemnités journalières forfaitaires qui leur sont versées en application de l'article L. 623-1 sont égales à un niveau fixé par décret."
),
    "Réécriture à droit constant : la durée du maintien, ses conditions cumulatives et sa prolongation sont exposées dans des phrases distinctes. Les deux situations de nouvelle activité restent distinguées : droit au maintien en cas d'indemnités de maladie nulles et possibilité de maintien pour certaines indemnités forfaitaires de maternité. Aucune réforme de fond n'est appliquée à ces prestations.",
    "Renvois L. 111-2-3, L. 5411-1 du code du travail et L. 623-1 conservés ; les durées et le niveau d'indemnité restent réglementaires. La note source, fondée sur le deuxième alinéa du V de l'article 96 de la loi n° 2021-1754 du 23 décembre 2021, maintient l'application aux arrêts commencés à compter du 1er janvier 2020 et, pour les travailleuses indépendantes ayant commencé leur activité à compter du 1er janvier 2019, aux périodes de versement des indemnités journalières de maternité commencées à compter du 1er novembre 2019, dans les conditions fixées par décret. Cette transition externe à l'article reste applicable et n'est pas une date de la réforme proposée."
)

draft('L161-9', paragraphs(
    "Lorsqu'ils reprennent le travail, les bénéficiaires de la prestation partagée d'éducation de l'enfant prévue à l'article L. 531-4 du titre III du livre V du code de la sécurité sociale ou du congé parental d'éducation prévu à l'article L. 122-28-1 du code du travail retrouvent leurs droits aux prestations en espèces des assurances maladie, maternité, invalidité et décès. Un décret fixe la durée de ce rétablissement des droits.",
    "Si une maladie ou une nouvelle maternité empêche la reprise du travail à l'issue du congé parental d'éducation, les personnes concernées retrouvent leurs droits aux prestations en espèces du régime dont elles relevaient avant ce congé. Ces droits sont rétablis pendant l'arrêt de travail pour maladie ou le congé légal de maternité qui suit le congé parental.",
    "Lorsque ces personnes reprennent le travail à l'issue de l'arrêt pour maladie ou du congé de maternité, elles retrouvent leurs droits aux prestations pendant une période fixée par décret."
),
    "Réécriture à droit constant : les trois situations de reprise immédiate, d'absence de reprise pour maladie ou nouvelle maternité, puis de reprise différée sont formulées séparément, avec leur régime et leur durée. Aucune modification des prestations ou de leurs bénéficiaires n'est proposée.",
    "Les trois alinéas et les deux renvois sont conservés. Incohérence préexistante : la source vise l'ancien article L. 122-28-1 du code du travail, absent du corpus courant fourni. L'article L. 1225-47 de ce corpus régit le congé parental d'éducation ; une actualisation du renvoi suppose de vérifier la concordance complète issue de la recodification. Aucun remplacement silencieux n'est effectué."
)

draft('L161-9-2', paragraphs(
    "La personne qui bénéficie successivement et sans interruption d'un congé parental d'éducation ou de la prestation prévue au 3° de l'article L. 531-1, puis d'un congé de présence parentale ou de l'allocation journalière de présence parentale, retrouve, lorsqu'elle reprend une activité, les droits aux prestations qu'elle avait acquis avant le congé parental d'éducation ou cette prestation. Il en va de même lorsque ces dispositifs se succèdent dans l'ordre inverse. Le rétablissement des droits intervient dans les conditions prévues à l'article L. 161-9."
),
    "Réécriture à droit constant : l'enchaînement sans interruption, l'ordre inverse et le rétablissement des droits lors de la reprise d'activité sont répartis entre trois phrases, sans modifier les alternatives entre congés et prestations. Aucune réforme de fond.",
    "Renvois au 3° de L. 531-1 et à L. 161-9 maintenus. La note source du VI de l'article 8 de la loi n° 2014-873 du 4 août 2014 réserve cette rédaction aux enfants nés ou adoptés à partir du 1er octobre 2014 ; pour les enfants nés ou adoptés avant cette date, la rédaction antérieure à l'entrée en vigueur de cet article 8 demeure applicable. Cette réserve historique est conservée séparément et ne doit pas être écartée par la réécriture."
)

draft('L161-9-3', paragraphs(
    "Pendant toute la durée du congé prévu à l'article L. 3142-6 du code du travail, au chapitre III du titre III du livre VI du code général de la fonction publique et à l'article L. 4138-6 du code de la défense, les bénéficiaires conservent leurs droits aux prestations en espèces des assurances maladie, maternité, invalidité et décès de leur régime d'origine.",
    "Après avoir bénéficié de ce maintien, ces personnes conservent leurs droits aux mêmes prestations auprès du régime obligatoire dont elles relevaient avant et pendant le congé dans les situations suivantes :",
    "1° Lorsqu'elles reprennent le travail à l'issue du congé ;",
    "2° Lorsqu'elles ne reprennent pas le travail à l'issue du congé en raison d'une maladie ou d'une maternité ;",
    "3° Lorsqu'elles reprennent le travail à l'issue du congé de maladie ou de maternité.",
    "Un décret fixe les périodes pendant lesquelles ces droits sont maintenus. Ce maintien s'applique sans préjudice de l'article L. 161-8 du présent code."
),
    "Réécriture à droit constant : la durée du congé et les trois situations qui lui succèdent sont présentées avec un sujet explicite. Les trois numéros et les six alinéas sont maintenus ; les prestations et les régimes concernés ne changent pas.",
    "Les trois références au congé dans les codes du travail, de la fonction publique et de la défense, ainsi que la réserve de L. 161-8, sont conservées. Les durées de maintien après le congé restent fixées par décret ; aucune durée ni date nouvelle n'est introduite."
)

draft('L161-13-1', paragraphs(
    "Lorsqu'elles ne sont plus écrouées, les personnes qui ont relevé de l'article L. 381-30 retrouvent, pour déterminer les conditions d'attribution des prestations en espèces, les droits ouverts dans leur régime d'affiliation avant la mise sous écrou. S'y ajoutent, le cas échéant, les droits ouverts pendant la détention provisoire. Un décret en Conseil d'État fixe les conditions de ce rétablissement. Il détermine notamment la durée maximale de mise sous écrou permettant d'en bénéficier et la durée du maintien des droits aux prestations en espèces pour les personnes qui ne reprennent pas d'activité professionnelle à la fin de leur mise sous écrou."
),
    "Réécriture à droit constant : la récupération des droits antérieurs et l'ajout éventuel des droits de détention provisoire sont explicités, puis les deux durées à fixer par décret sont identifiées. Aucune extension des droits acquis en détention n'est créée.",
    "Le renvoi à L. 381-30 et la compétence du décret en Conseil d'État sont maintenus. L'ajout de droits reste limité à ceux ouverts pendant la détention provisoire ; il n'est pas étendu à toute période d'incarcération. Les deux durées réglementaires ne sont pas chiffrées par le présent article."
)

draft('L161-15', paragraphs(
    "Le conjoint séparé de droit ou de fait dispose d'une action directe en paiement des prestations de prise en charge des frais de santé de ses enfants mineurs en cas de maladie et de maternité lorsque l'autre conjoint, en ne présentant pas les justifications requises, l'empêche d'obtenir cette prise en charge. Un décret en Conseil d'État fixe les conditions d'exercice de cette action."
),
    "Réécriture à droit constant : le titulaire de l'action et son objet sont placés en tête, puis la cause précise du blocage est exposée. Le champ reste celui des frais de santé des enfants mineurs et aucune réforme de fond n'est ajoutée.",
    "La séparation de droit ou de fait, le défaut de présentation des justifications par l'autre conjoint et le décret en Conseil d'État sont conservés. L'action ne devient pas un droit général au paiement de toute prestation familiale."
)

draft('L161-15-1', paragraphs(
    "La prise en charge des frais de santé en cas de maladie et de maternité ne peut être retirée à une personne que si elle ne remplit plus la condition de résidence prévue à l'article L. 160-1 ou si elle est présumée absente dans les conditions de l'article 112 du code civil."
),
    "Réécriture à droit constant : la règle limitant les cas de perte de la prise en charge est formulée directement, en conservant ses deux seules hypothèses. Aucune cause supplémentaire de retrait n'est créée.",
    "Les deux conditions restent alternatives et les renvois à L. 160-1 et à l'article 112 du code civil sont inchangés. La formulation conserve une limitation des possibilités de retrait, sans rendre celui-ci automatique."
)

draft('L161-15-2', paragraphs(
    "Lors d'un changement d'organisme d'affiliation, l'organisme qui verse les prestations en espèces doit poursuivre leur service jusqu'à la date à laquelle le nouvel organisme compétent se substitue à lui. Il ne peut interrompre les prestations avant la prise d'effet de cette substitution."
),
    "Réécriture à droit constant : l'obligation de continuité du service est énoncée d'abord, puis l'interdiction d'interruption prématurée est rappelée. Le transfert d'affiliation ne change pas la date de fin de responsabilité de l'organisme initial.",
    "L'article reste limité aux prestations en espèces et conserve pour terme la substitution effective du nouvel organisme. La note source du III de l'article 62 de la loi n° 2016-1827 du 23 décembre 2016 fixe l'entrée en vigueur des dispositions au 1er janvier 2017 ; cette date historique ne fixe aucune entrée en vigueur de réforme future."
)

draft('L161-15-3', paragraphs(
    "Lorsque leurs deux parents sont assurés d'un régime d'assurance maladie et maternité, les enfants peuvent être rattachés à chacun d'eux en qualité d'ayant droit, par dérogation à toute disposition contraire.",
    "Un décret en Conseil d'État fixe les modalités d'application du présent article."
),
    "Réécriture à droit constant : la condition tenant à l'assurance des deux parents précède la faculté de double rattachement. Les deux alinéas, la dérogation et le décret d'application sont conservés.",
    "Le rattachement à chacun des parents demeure une faculté, sans condition nouvelle d'identité de leur régime. Le texte ne supprime pas la qualité d'ayant droit ni ne remplace le décret en Conseil d'État par un décret simple."
)

draft('L161-15-4', paragraphs(
    "La personne qui cesse de bénéficier de la prise en charge des frais de santé au titre des articles L. 160-1 à L. 160-4 doit en informer son organisme d'assurance maladie dans le délai fixé par arrêté du ministre chargé de la sécurité sociale. Le moyen d'identification électronique dont elle dispose fait immédiatement l'objet de l'opposition prévue au I de l'article L. 161-31. Si ce moyen est matériel, elle doit le restituer à cet organisme. S'il est immatériel, elle doit mettre en œuvre la procédure de désactivation prévue au I de l'article L. 161-31.",
    "En cas de manquement aux obligations du premier alinéa, les dispositions de l'article L. 114-17-1 s'appliquent.",
    "Par dérogation au premier alinéa, les adhérents à l'une des assurances volontaires maladie-maternité-invalidité ou maladie-maternité prévues aux chapitres II, III et V du titre VI du livre VII du présent code sont dispensés de la restitution. Cette dispense vise à faciliter le service et la prise en charge, par la Caisse des Français de l'étranger, des soins mentionnés à l'article L. 766-2."
),
    "Réécriture à droit constant : les obligations d'information, d'opposition, de restitution matérielle et de désactivation immatérielle sont rendues explicites. La sanction par renvoi et l'exception de restitution pour les assurances volontaires sont maintenues dans leurs alinéas d'origine.",
    "Les trois alinéas sont conservés. La dispense du troisième alinéa reste limitée à la restitution, conformément à la source : elle n'est pas élargie à l'information, à l'opposition ou à la désactivation. Maintien des chapitres II, III et V du titre VI du livre VII et des renvois L. 160-1 à L. 160-4, L. 161-31 I, L. 114-17-1 et L. 766-2. Aucun délai chiffré n'est inventé."
)

draft('L161-16', paragraphs(
    "Les assurés sociaux anciens déportés ou internés, titulaires de la carte de déporté ou interné de la Résistance ou de la carte de déporté ou interné politique, sont présumés atteints d'une invalidité les rendant absolument incapables d'exercer une profession quelconque lorsqu'ils cessent toute activité professionnelle et ont atteint un âge minimum. Cette présomption est réservée à ceux dont la pension militaire d'invalidité a été accordée pour un taux d'invalidité global déterminé.",
    "La pension d'invalidité qui leur est accordée à leur demande, en application de ces dispositions et au titre de leur régime d'assurance invalidité, peut être cumulée avec leur pension militaire d'invalidité sans limitation de montant."
),
    "Réécriture à droit constant : les conditions de la présomption d'invalidité sont réparties entre deux phrases dans le premier alinéa. Le second alinéa maintient la demande de l'assuré et le cumul sans plafond avec la pension militaire.",
    "La règle historique est conservée intégralement : cartes de la Résistance ou politiques, taux global déterminé de pension militaire, cessation de toute activité, âge minimum et incapacité absolue à toute profession. La source ne chiffre ni le taux global ni l'âge minimum ; aucune valeur n'est ajoutée. Le cumul concerne les deux pensions identifiées, sans extension à d'autres revenus."
)

draft('L161-16-1', paragraphs(
    "Pour obtenir un avantage d'invalidité, la personne de nationalité étrangère qui réside en France doit établir la régularité de son séjour dans les conditions prévues à l'article L. 111-2-3."
),
    "Réécriture à droit constant : la condition de séjour régulier est formulée avec un sujet et un objet directs, tout en maintenant le champ des personnes étrangères résidant en France. Aucune réforme de fond.",
    "Le renvoi à L. 111-2-3 demeure la règle de justification applicable ; aucune liste autonome de titres, condition de durée de résidence ou condition de nationalité supplémentaire n'est créée."
)

draft('L161-17-1', paragraphs(
    "L'Union des institutions et services de retraites est un groupement d'intérêt public créé dans les conditions du chapitre II de la loi n° 2011-525 du 17 mai 2011 de simplification et d'amélioration de la qualité du droit. Elle réunit l'ensemble des organismes gestionnaires des régimes de retraite légalement obligatoires, la Caisse des dépôts et consignations et les services de l'État chargés de liquider les pensions en application du code des pensions civiles et militaires de retraite. Elle est dotée d'un conseil d'administration.",
    "L'union assure le pilotage stratégique de tous les projets de coordination, de simplification et de mutualisation destinés à améliorer les relations des régimes avec leurs usagers auxquels participent tout ou partie de ses membres. Elle veille à leur mise en œuvre. Elle assure notamment la mise en œuvre des droits prévus aux I à V de l'article L. 161-17 et le pilotage des projets prévus aux articles L. 161-17-1-1 et L. 161-17-1-2. Pour les assurés titulaires du compte prévu au II de l'article L. 241-3, elle assure également la mise en œuvre de l'information distincte sur les droits par répartition et les actifs de capitalisation prévue au VII de l'article L. 161-17.",
    "L'union pilote et met en œuvre les dispositions de l'article L. 224-7-1 du code monétaire et financier. Elle peut percevoir des recettes correspondant aux prestations facturées aux représentants professionnels des gestionnaires de produits d'épargne retraite en application de ce même article L. 224-7-1.",
    "L'autorité compétente de l'État conclut avec l'Union des institutions et services de retraites un contrat fixant les objectifs pluriannuels de simplification et de mutualisation de l'assurance vieillesse. Ce contrat comprend un schéma directeur des systèmes d'information et couvre une période d'au moins quatre ans.",
    "Un décret en Conseil d'État précise, en tant que de besoin, les modalités d'application du présent article."
),
    "Les cinq alinéas sont réécrits à droit constant pour préciser la composition du groupement, son pilotage, ses recettes et le contrat pluriannuel. Une coordination de fond est ajoutée dans le deuxième alinéa : l'union met en œuvre l'information séparant répartition et capitalisation déjà prévue au VII proposé de L. 161-17. Ses compétences de gestion financière ne sont pas étendues.",
    "Le VII proposé de L. 161-17 et le II proposé de L. 241-3 ont été vérifiés dans le corpus public local ; ce sont des dispositions proposées, non des références au droit source en vigueur. La mission ajoutée suit leur mise en œuvre et leur champ initial, sans raccordement automatique des salariés agricoles ou des employeurs publics. Adapter la convention du groupement, le schéma directeur et les textes réglementaires aux flux d'information des futurs gestionnaires, à leur financement et aux garanties de données ; leur désignation et la gouvernance du compte restent soumises au VI proposé de L. 241-3. Ni ces conditions ni le financement des transferts ne sont déclarés acquis. Le contrat conserve sa durée minimale de quatre ans, et L. 224-7-1 du code monétaire et financier conserve sa portée propre."
)

draft('L161-17-1-1', paragraphs(
    "Les organismes et services qui gèrent les régimes de retraite de base et complémentaires légaux ou rendus légalement obligatoires se communiquent par voie électronique les informations nécessaires à la détermination du droit aux prestations de retraite, au maintien des droits et, s'il y a lieu, au calcul de ces prestations. Ces échanges servent notamment à appliquer l'article 2 de l'ordonnance n° 2004-605 du 24 juin 2004 simplifiant le minimum vieillesse, les articles L. 173-2, L. 353-1, L. 353-6, L. 355-3, L. 815-1, L. 815-7 et L. 815-24 du présent code et l'article L. 732-54-3 du code rural et de la pêche maritime. Lors de la mise en œuvre du II de l'article L. 161-23-1, ils échangent aussi les seules données nécessaires à l'établissement du total des pensions et à l'application du seuil unique, dans les conditions prévues à ce II. Un décret en Conseil d'État fixe les modalités d'application du présent article. Il peut prévoir, pour les mêmes finalités, la création d'un répertoire national."
),
    "Réécriture à droit constant des finalités et des références des échanges, en distinguant leur objet de leurs modalités. Coordination de fond avec le II proposé de L. 161-23-1 : les échanges nécessaires au total des pensions cumulées et au seuil unique sont explicités, sous les conditions de ce dispositif et à sa mise en œuvre.",
    "Tous les renvois d'origine, y compris l'ordonnance n° 2004-605 et L. 732-54-3 du code rural et de la pêche maritime, sont conservés. Le II proposé de L. 161-23-1, vérifié dans le corpus local, prévoit une durée maximale de trois années civiles, un seuil revalorisé, la proportion entre régimes, un décret en Conseil d'État après avis de la CNIL et la rectification des données. L'ajout ne modifie pas ces paramètres et ne constitue pas une habilitation générale à échanger des données de capitalisation. Les coordinations expresses des régimes hors du code et des accords complémentaires restent nécessaires pour le champ de la mesure de pensions cumulées. La note source du B du VIII de l'article 87 de la loi n° 2025-199 du 28 février 2025 fixe au 1er janvier 2026 l'entrée en vigueur de la modification source ; elle ne déclenche pas la réforme future. Le répertoire national reste facultatif."
)

draft('L161-17-1-2', paragraphs(
    "Un répertoire unique de gestion des carrières est créé. Les régimes de retraite de base et complémentaires légalement obligatoires et les services de l'État chargés de liquider les pensions transmettent régulièrement à la caisse nationale mentionnée à l'article L. 222-1 l'ensemble des informations concernant la carrière de leurs assurés pour alimenter ce répertoire. Un décret en Conseil d'État fixe les modalités d'application du présent article. Le répertoire contient également les points acquis au titre du compte mentionné à l'article L. 4163-4 du code du travail.",
    "Le répertoire mentionné au premier alinéa fournit les informations et les données à caractère personnel nécessaires :<br/><br/>1° Au système d'information du compte personnel de formation mentionné au II de l'article L. 6323-8 du code du travail, pour déterminer si le titulaire d'un compte personnel de formation peut financer une action de formation au moyen des droits inscrits sur ce compte ;<br/><br/>2° Au recensement des parcours professionnels et des acquis de l'expérience professionnelle pour le passeport d'orientation, de formation et de compétences mentionné au III du même article L. 6323-8."
),
    "Réécriture à droit constant : les obligations d'alimentation du répertoire, son contenu et les deux usages de données sont formulés directement. Les deux alinéas et les 1° et 2° sont maintenus, sans nouvel usage du répertoire.",
    "Renvois à L. 222-1, L. 4163-4 du code du travail et aux II et III de L. 6323-8 conservés. La transmission reste régulière et porte sur l'ensemble des informations de carrière. Le répertoire de carrières n'est pas transformé en registre des actifs de capitalisation : les flux nécessaires au VII proposé de L. 161-17 doivent être organisés sous leur base juridique propre, avec la mission coordonnée de L. 161-17-1 et les futurs textes de gestion du compte."
)

draft('L161-17-2', paragraphs(
    "Pour les assurés nés à compter du 1<sup>er</sup> janvier 1969, l'âge d'ouverture du droit à une pension de retraite est fixé à soixante-quatre ans. Cet âge est celui mentionné au premier alinéa de l'article L. 351-1 du présent code, au 1° du I de l'article L. 24 et au 1° de l'article L. 25 du code des pensions civiles et militaires de retraite.",
    "Pour les assurés nés avant cette date, cet âge est fixé comme suit :",
    "1° Soixante-deux ans et trois mois pour les assurés nés du 1<sup>er</sup> septembre 1961 au 31 décembre 1961 ;",
    "2° Soixante-deux ans et six mois pour les assurés nés en 1962 ;",
    "3° Soixante-deux ans et neuf mois pour les assurés nés du 1<sup>er</sup> janvier 1963 au 31 mars 1965 ;",
    "4° Soixante-trois ans pour les assurés nés du 1<sup>er</sup> avril au 31 décembre 1965 ;",
    "5° Soixante-trois ans et trois mois pour les assurés nés en 1966 ;",
    "6° Soixante-trois ans et six mois pour les assurés nés en 1967 ;",
    "7° Soixante-trois ans et neuf mois pour les assurés nés en 1968.",
    "Pour les assurés nés avant le 1<sup>er</sup> septembre 1961, l'âge applicable reste celui fixé par le présent article dans sa rédaction antérieure à la loi n° 2025-1403 du 30 décembre 2025 de financement de la sécurité sociale pour 2026."
),
    "Réécriture à droit constant : le champ des générations est placé avant l'âge de droit commun, et les bornes des générations sont présentées uniformément. Les sept numéros, tous les âges et la réserve de la rédaction historique sont conservés. La réforme de capitalisation fournie ne modifie pas ces âges.",
    "Contrôle des bornes : 64 ans dès le 1er janvier 1969 ; 62 ans et 3 mois de septembre à décembre 1961 ; 62 ans et 6 mois en 1962 ; 62 ans et 9 mois du 1er janvier 1963 au 31 mars 1965 ; 63 ans du 1er avril au 31 décembre 1965 ; puis 63 ans et 3, 6 et 9 mois respectivement pour 1966, 1967 et 1968. La rédaction historique reste applicable aux personnes nées avant le 1er septembre 1961. Les notes sources distinguent l'application des modifications de l'article 87 de la loi n° 2025-199 aux pensions prenant effet à compter du 1er janvier 2026, l'entrée en vigueur immédiate de la loi n° 2025-1403 et l'application de la rédaction issue de son article 105 aux pensions prenant effet à compter du 1er septembre 2026 selon son VI. Ne pas confondre entrée en vigueur et application aux pensions ; ces dates ne sont pas celles de la réforme proposée."
)

draft('L161-17-3', paragraphs(
    "Pour les assurés des régimes auxquels s'applique l'article L. 161-17-2, la durée d'assurance requise pour bénéficier d'une pension de retraite au taux plein et la durée des services et bonifications requise pour obtenir le pourcentage maximum d'une pension civile ou militaire de retraite sont les suivantes :",
    "1° 167 trimestres pour les assurés nés du 1<sup>er</sup> janvier 1958 au 31 décembre 1960 ;",
    "2° 168 trimestres pour les assurés nés du 1<sup>er</sup> janvier 1961 au 31 août 1961 ;",
    "3° 169 trimestres pour les assurés nés du 1<sup>er</sup> septembre 1961 au 31 décembre 1962 ;",
    "4° 170 trimestres pour les assurés nés du 1<sup>er</sup> janvier 1963 au 31 mars 1965 ;",
    "5° 171 trimestres pour les assurés nés du 1<sup>er</sup> avril 1965 au 31 décembre 1965 ;",
    "6° 172 trimestres pour les assurés nés à compter du 1<sup>er</sup> janvier 1966."
),
    "Réécriture à droit constant : l'objet des deux durées exigées est formulé plus directement et les intervalles de naissance sont harmonisés. Les six subdivisions, les durées de 167 à 172 trimestres et toutes les bornes sont maintenues. Aucun palier de capitalisation ne modifie ces conditions d'assurance.",
    "Les tranches sont contrôlées sans déplacement : 1958-1960, janvier-août 1961, septembre 1961-décembre 1962, janvier 1963-mars 1965, avril-décembre 1965, puis naissances à compter de 1966. Le renvoi à L. 161-17-2 et la distinction entre taux plein et pourcentage maximum restent intacts. Les notes sources prévoient l'entrée en vigueur immédiate de la loi n° 2025-1403 du 30 décembre 2025 et, selon le VI de son article 105, l'application de cette rédaction aux pensions prenant effet à compter du 1er septembre 2026. La future réduction des droits par répartition sur les seules cotisations transférées appelle les règles de calcul visées par L. 241-3 proposé ; elle n'autorise pas à réduire silencieusement les trimestres ici fixés."
)

draft('L161-17-4', paragraphs(
    "Dans les conditions et limites fixées par décret, l'âge prévu à l'article L. 161-17-2 est réduit d'une durée correspondant au nombre de trimestres attribués au titre de la majoration de durée d'assurance prévue à l'article L. 351-6-1."
),
    "Réécriture à droit constant : la réduction à due concurrence est exprimée comme une durée correspondant au nombre de trimestres attribués. La réserve réglementaire est placée en tête sans modifier son champ.",
    "Les renvois L. 161-17-2 et L. 351-6-1, ainsi que les conditions et limites fixées par décret, sont maintenus. Aucun nouveau nombre de trimestres ni abaissement forfaitaire de l'âge n'est créé."
)

draft('L161-18', paragraphs(
    "Pour la liquidation des droits à l'assurance vieillesse, l'appréciation de l'inaptitude au travail effectuée dans les conditions de l'article L. 351-7 du présent code par le régime général, le régime des non-salariés des professions agricoles ou le régime des salariés agricoles vaut également à l'égard des autres régimes de cette liste."
),
    "Réécriture à droit constant : la reconnaissance réciproque de l'appréciation de l'inaptitude entre les trois régimes est exprimée directement. Aucun régime ni critère d'inaptitude n'est ajouté.",
    "La portée reste limitée à la liquidation des droits à l'assurance vieillesse et à l'appréciation effectuée selon L. 351-7. Selon la note source du C du VIII de l'article 87 de la loi n° 2025-199 du 28 février 2025, la modification s'applique aux pensions prenant effet à compter du 1er janvier 2026. Cette coordination existante avec les régimes agricoles ne les fait pas entrer dans le premier champ du transfert proposé à L. 241-3."
)

draft('L161-18-1', paragraphs(
    "Pour obtenir un avantage de vieillesse, la personne de nationalité étrangère résidant en France doit établir la régularité de son séjour en produisant un titre ou un document inscrit sur une liste fixée par décret."
),
    "Réécriture à droit constant : l'obligation de produire un justificatif de séjour est formulée directement, sans changer les personnes concernées ni la liste réglementaire. Aucune réforme de fond.",
    "Réserve historique essentielle de la note source : l'article 48 de la loi n° 93-1027 du 24 août 1993 maintient, nonobstant L. 161-18-1, L. 161-25-1, L. 161-25-2 et L. 356-1, les droits à prestations ouverts aux personnes de nationalité étrangère à raison de cotisations versées avant l'entrée en vigueur de cette loi. Cette garantie externe demeure applicable ; la réécriture ne la supprime ni ne soumet à nouveau ces droits acquis à la condition de titre."
)

draft('L161-19', paragraphs(
    "Pour l'ouverture du droit aux avantages de vieillesse et leur liquidation, toute période de service national légal, de mobilisation ou de captivité est assimilée à une période d'assurance, sans condition préalable."
),
    "Réécriture à droit constant : les deux effets de l'assimilation sont placés en tête, suivis des trois catégories de périodes. L'absence de condition préalable est maintenue expressément.",
    "L'assimilation concerne à la fois l'ouverture du droit et la liquidation. Les trois catégories historiques sont conservées sans exigence nouvelle de cotisation, de durée ou de justification d'une affiliation antérieure."
)

draft('L161-19-1', paragraphs(
    "Les périodes durant lesquelles l'assuré a été affilié à un régime obligatoire de pension d'une institution européenne ou d'une organisation internationale à laquelle la France est partie sont prises en compte pour déterminer la durée d'assurance mentionnée au deuxième alinéa de l'article L. 351-1, au I des articles L. 643-3 et L. 653-2 du présent code, au premier alinéa du I de l'article L. 14 du code des pensions civiles et militaires de retraite et au II de l'article L. 732-24 du code rural et de la pêche maritime. Cette prise en compte est subordonnée à l'affiliation de l'assuré à ce seul régime de retraite obligatoire."
),
    "Réécriture à droit constant : les périodes prises en compte sont identifiées avant la liste complète des textes concernés, et la condition d'affiliation exclusive fait l'objet d'une phrase distincte. Aucun droit ni régime supplémentaire n'est créé.",
    "Les cinq références de durée d'assurance, avec leurs alinéas et subdivisions, sont conservées, ainsi que la condition que la France soit partie à l'organisation internationale et l'affiliation au seul régime obligatoire considéré. La note source du C du VIII de l'article 87 de la loi n° 2025-199 du 28 février 2025 réserve l'application de la modification aux pensions prenant effet à compter du 1er janvier 2026. La prise en compte de ces périodes n'est pas assimilée à une alimentation du compte de capitalisation proposé."
)

draft('L161-20', paragraphs(
    "Par dérogation à toute disposition législative contraire, des décrets fixent les conditions de prise en compte des périodes de détention provisoire pour l'ouverture du droit à pension dans les régimes législatifs ou réglementaires d'assurance vieillesse auxquels l'article L. 351-3 ne s'applique pas. Dans chacun de ces régimes, les personnes en détention provisoire ne peuvent en aucun cas bénéficier d'un traitement plus favorable que les personnes en chômage involontaire."
),
    "Réécriture à droit constant : la compétence des décrets et les régimes concernés sont formulés directement, puis la limite de traitement est énoncée avec les personnes comparées. Aucune extension à la liquidation ou à une autre forme de détention n'est ajoutée.",
    "La dérogation législative, l'exclusion des régimes soumis à L. 351-3 et le plafond de traitement par rapport au chômage involontaire sont maintenus. La note source du C du VIII de l'article 87 de la loi n° 2025-199 du 28 février 2025 prévoit l'application de la modification aux pensions prenant effet à compter du 1er janvier 2026."
)

draft('L161-21', paragraphs(
    "Dans les conditions et limites fixées par décret en Conseil d'État, les périodes de versement de l'indemnité de soins aux tuberculeux prévue à l'article L. 41 du code des pensions militaires d'invalidité et des victimes de la guerre sont prises en compte pour l'ouverture et le calcul des droits à pension de vieillesse lorsqu'elles succèdent à des périodes d'assurance ou à des périodes validables au titre de l'article L. 161-19. Ces périodes comprennent celles pendant lesquelles les intéressés ont été hospitalisés en raison de l'affection ayant justifié le versement de cette indemnité.",
    "Les personnes qui ont cessé de bénéficier de l'indemnité de soins aux tuberculeux, ou leurs conjoints survivants, peuvent demander la validation des périodes mentionnées au premier alinéa.",
    "Cette demande peut être présentée quelle que soit la date d'entrée en jouissance de la pension.",
    "Les rachats effectués en application de l'article L. 742-4 pour les périodes validées au titre du premier alinéa sont annulés et remboursés aux intéressés.",
    "Les premier, deuxième et troisième alinéas s'appliquent aux assurés des régimes d'assurance vieillesse d'origine législative ou réglementaire, dans le cadre des règles propres à chacun de ces régimes."
),
    "Réécriture à droit constant : la prise en compte des périodes, la demande de validation et l'annulation-remboursement des rachats sont exposées dans les cinq alinéas d'origine. Les périodes d'hospitalisation sont explicitées sans modifier le lien avec l'affection indemnisée, ni les conditions de succession des périodes.",
    "Conserver le caractère historique de cette indemnité et les renvois L. 161-19 et L. 742-4. Le renvoi source à L. 41 du code des pensions militaires d'invalidité et des victimes de la guerre est maintenu ; sa concordance avec la recodification de ce code, absent du corpus fourni, nécessite une vérification distincte, sans substitution non vérifiée. Le deuxième alinéa continue de viser le premier ; le quatrième conserve l'annulation et le remboursement ; le cinquième ne vise que les trois premiers alinéas et n'étend pas de lui-même le remboursement à tous les régimes. Les conditions réglementaires et la succession à une période d'assurance ou validable s'appliquent aussi aux hospitalisations comprises dans les périodes de versement."
)


sources = json.loads(Path('source.json').read_text())
assert len(sources) == 24
assert set(drafts) == {a['number'] for a in sources}
result = []
for source in sources:
    item = {key: source[key] for key in
            ('code_id', 'source_id', 'source_sha256', 'number')}
    item.update(drafts[source['number']])
    result.append(item)
Path('answer.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(result)} articles')
