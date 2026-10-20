import json
from pathlib import Path
from xml.sax.saxutils import escape

sources = json.loads(Path('source.json').read_text())
out = Path('fragments')
out.mkdir(exist_ok=True)


def paras(text):
    return ''.join('<p>' + escape(line.strip()) + '</p>' for line in text.strip().splitlines() if line.strip())


def cell(text, **attrs):
    attributes = ''.join(' ' + k + '="' + str(v) + '"' for k, v in attrs.items())
    return '<td' + attributes + '>' + paras(text) + '</td>'


rows = []


def full(text):
    rows.append('<tr>' + cell(text, colspan=2) + '</tr>')


def pair(label, text, rowspan=None):
    rows.append('<tr>' + cell(label, **({'rowspan': rowspan} if rowspan else {})) + cell(text) + '</tr>')


def following(text):
    rows.append('<tr>' + cell(text) + '</tr>')


full('1° Investissements :')
pair('A-Investissement social :', '''a) Évolution des effectifs par type de contrat, âge et ancienneté :
i-Effectif :
Effectif total au 31 décembre (1) (I) ;
Effectif permanent (2) (I) ;
Nombre, au 31 décembre, de salariés dont le contrat à durée déterminée a été conclu avant l'entrée en vigueur de la réforme du contrat unique et demeure en cours (I) ;
Effectif mensuel moyen de l'année considérée (3) (I) ;
Répartition de l'effectif total au 31 décembre par sexe (I), par âge (4) (I), par ancienneté (5) (I) et selon une structure détaillée de qualification (II).
ii-Travailleurs extérieurs :
Nombre de salariés d'une entreprise extérieure (6) (23) ;
Nombre de stagiaires, notamment d'écoles ou d'universités (7) ; évolution du nombre de stagiaires ;
Nombre mensuel moyen de salariés temporaires (8) ;
Durée moyenne des contrats de travail temporaire pour les contrats antérieurs à la réforme ; pour les emplois nouveaux, durée moyenne des missions, distincte de la durée de l'emploi ;
Nombre de salariés de l'entreprise détachés et nombre de salariés détachés accueillis.''', rowspan=6)
following('''b) Évolution des emplois, notamment par catégorie professionnelle :
i-Embauches :
Nombre d'embauches en contrat à durée indéterminée, y compris en contrat unique ;
Nombre d'embauches au titre de contrats à durée déterminée conclus avant l'entrée en vigueur de la réforme du contrat unique, en distinguant les contrats de travailleurs saisonniers (I) ;
Nombre de salariés de moins de vingt-cinq ans embauchés.
ii-Départs :
Nombre total de départs (I) ;
Nombre de démissions (I) ;
Nombre de licenciements pour motif économique, dont départs en retraite et préretraite (I) ;
Nombre de licenciements pour d'autres causes (I) ;
Nombre de fins de contrats à durée déterminée conclus avant l'entrée en vigueur de la réforme du contrat unique (I) ;
Nombre de départs pendant la période d'essai (9) (I) ;
Nombre de mutations entre établissements (I) ;
Nombre de départs volontaires en retraite et préretraite (10) (I) ;
Nombre de décès (I).
iii-Promotions : nombre de salariés promus dans une catégorie supérieure pendant l'année (11).
iv-Chômage :
Nombre de salariés placés en chômage partiel pendant l'année (I) ; nombre total d'heures de chômage partiel (12) (I), en distinguant les heures indemnisées et non indemnisées ;
Nombre de salariés placés en chômage intempéries pendant l'année (I) ; nombre total d'heures de chômage intempéries (I), en distinguant les heures indemnisées et non indemnisées.''')
following('''c) Évolution de l'emploi des personnes handicapées et mesures destinées à le développer :
Nombre de travailleurs handicapés employés pendant l'année considérée (13) ;
Nombre, parmi les salariés employés pendant cette année, de travailleurs handicapés à la suite d'un accident du travail survenu dans l'entreprise.''')
following('d) Abrogé. Les données relatives aux stagiaires sont réunies au a), ii, sans second relevé.')
following('''e) Formation professionnelle : investissements en formation et publics concernés :
i-Formation professionnelle continue (44) :
Pourcentage de la masse salariale consacré à la formation continue ;
Montants consacrés respectivement à la formation interne, à la formation assurée en application de conventions, aux versements aux organismes de recouvrement, aux versements aux organismes agréés et aux autres dépenses ; montant total ;
Nombre de stagiaires (II) ;
Nombre d'heures de stage (II), en distinguant les heures rémunérées et non rémunérées ;
Répartition par type de stage, par exemple : adaptation, formation professionnelle, entretien ou perfectionnement des connaissances.
ii-Congés de formation :
Nombre de salariés ayant bénéficié d'un congé de formation rémunéré ; nombre de bénéficiaires d'un congé de formation non rémunéré ; nombre de salariés auxquels un congé de formation a été refusé.
iii-Apprentissage : nombre de contrats d'apprentissage conclus pendant l'année. Pour les contrats uniques, la durée de la phase d'apprentissage ne détermine pas celle de l'emploi.''')
following('''f) Conditions de travail :
Durée et aménagement du travail, dont travail à temps partiel ; exposition aux risques et aux facteurs de pénibilité ; accidents du travail, maladies professionnelles, absentéisme et dépenses de sécurité.
i-Accidents du travail et de trajet :
Taux de fréquence des accidents du travail (I) ;
Nombre d'accidents avec arrêt de travail divisé par le nombre d'heures travaillées ;
Nombre d'accidents du travail avec arrêt × 106 divisé par le nombre d'heures travaillées ;
Taux de gravité des accidents du travail (I) ;
Nombre de journées perdues divisé par le nombre d'heures travaillées ;
Nombre de journées perdues × 10 ³ divisé par le nombre d'heures travaillées ;
Nombre d'incapacités permanentes, partielles ou totales, notifiées à l'entreprise pendant l'année considérée ;
Nombre d'accidents mortels, en distinguant les accidents du travail et de trajet ;
Nombre d'accidents de trajet ayant entraîné un arrêt de travail ;
Nombre d'accidents subis dans l'entreprise par les salariés temporaires ou par les salariés des prestataires de services ;
Taux et montant de la cotisation de sécurité sociale au titre des accidents du travail.
ii-Répartition des accidents par élément matériel (28) :
Nombre d'accidents liés à des risques graves : codes 32 à 40 ;
Nombre d'accidents liés à des chutes avec dénivellation : code 02 ;
Nombre d'accidents occasionnés par des machines, hors risques précédents : codes 09 à 30 ;
Nombre d'accidents de circulation, manutention et stockage : codes 01, 03, 04, 06, 07 et 08 ;
Nombre d'accidents occasionnés par des objets, masses ou particules en mouvement accidentel : code 05 ;
Autres cas.
iii-Maladies professionnelles :
Nombre et dénomination des maladies professionnelles déclarées à la sécurité sociale pendant l'année ;
Nombre de salariés atteints d'affections pathologiques à caractère professionnel et caractérisation de ces affections ;
Nombre de déclarations par l'employeur de procédés de travail susceptibles de provoquer des maladies professionnelles (29).
iv-Dépenses de sécurité :
Effectif formé à la sécurité pendant l'année ;
Montant des dépenses de formation à la sécurité réalisées dans l'entreprise ;
Taux de réalisation du programme de sécurité présenté l'année précédente ;
Existence et nombre de plans spécifiques de sécurité.
v-Durée et aménagement du temps de travail :
Horaire hebdomadaire moyen affiché des ouvriers, employés ou catégories assimilées (30) (I) ;
Nombre de salariés ayant bénéficié d'un repos compensateur (I), au titre du présent code (31) ou d'un régime conventionnel (I) ;
Nombre de salariés bénéficiant d'horaires individualisés (32) (I) ;
Nombre de salariés à temps partiel (I), en distinguant ceux travaillant entre 20 et 30 heures (33) et les autres formes de temps partiel ;
Nombre de salariés ayant bénéficié, pendant toute l'année considérée, de deux jours consécutifs de repos hebdomadaire (I) ;
Nombre moyen de jours de congés annuels, hors repos compensateur (34) (I) ;
Nombre de jours fériés payés (35) (I).
vi-Absentéisme (14) :
Nombre de journées d'absence (15) (I) ; nombre de journées théoriques travaillées ;
Nombre de journées d'absence pour maladie (I) et répartition selon leur durée (16) (I) ;
Nombre de journées d'absence pour accident du travail, accident de trajet ou maladie professionnelle (I) ;
Nombre de journées d'absence pour maternité (I) ;
Nombre de journées d'absence pour congés autorisés, notamment événements familiaux et congés spéciaux pour les femmes (I) ;
Nombre de journées d'absence pour d'autres causes (I).
vii-Organisation et contenu du travail :
Nombre de personnes occupant des emplois à horaires alternants ou de nuit ;
Nombre de personnes de plus de cinquante ans occupant ces emplois ;
Nombre de salariés affectés à des tâches répétitives au sens de l'article D. 4163-2 (36), en distinguant les femmes et les hommes.
viii-Conditions physiques de travail :
Nombre de personnes habituellement et régulièrement exposées à plus de 80 à 85 db à leur poste de travail (37) ;
Nombre de salariés exposés au froid ou à la chaleur au sens des articles R. 4223-13 à R. 4223-15 ;
Nombre de salariés exposés aux températures extrêmes au sens de l'article D. 4163-2 (38) ;
Nombre de salariés travaillant habituellement et régulièrement aux intempéries au sens de l'article L. 5424-8 (39) ;
Nombre de prélèvements, d'analyses de produits toxiques et de mesures (40).
ix-Transformation de l'organisation du travail : expériences visant à améliorer le contenu du travail (41).
x-Dépenses d'amélioration des conditions de travail :
Montant des dépenses consacrées à cette amélioration dans l'entreprise (42) ; taux de réalisation du programme de l'année précédente.
xi-Médecine du travail (43) :
Nombre de visites d'information et de prévention et d'examens médicaux, en distinguant les travailleurs en suivi de droit commun et en suivi individuel renforcé ;
Nombre d'examens complémentaires, en distinguant les travailleurs soumis à surveillance et les autres ;
Part du temps consacré par le médecin du travail à l'analyse et à l'intervention en milieu de travail.
xii-Travailleurs inaptes :
Nombre de salariés déclarés définitivement inaptes à leur emploi par le médecin du travail ;
Nombre de salariés reclassés dans l'entreprise à la suite d'une inaptitude.''')
pair('B-Investissement matériel et immatériel :', 'a) Évolution des immobilisations, nettes des amortissements et des éventuelles dépréciations.', rowspan=3)
following('b) Dépenses de recherche et développement, le cas échéant.')
following("c) Évolution de la productivité et taux d'utilisation des capacités de production, lorsque l'entreprise peut les mesurer.")
full("2° Égalité professionnelle entre les femmes et les hommes au sein de l'entreprise :")
full("I. Indicateurs de la situation comparée des femmes et des hommes dans l'entreprise :")
pair("A-Conditions générales d'emploi :", '''a) Effectifs : répartition chiffrée par sexe et catégorie professionnelle, selon les contrats de travail. Les contrats uniques à durée indéterminée sont distingués des contrats à durée déterminée antérieurs à la réforme qui demeurent en cours.''', rowspan=5)
following('''b) Durée et organisation du travail : données chiffrées par sexe :
Répartition des effectifs entre temps complet, temps partiel compris entre 20 et 30 heures et autres formes de temps partiel ;
Répartition selon l'organisation du travail : travail posté, de nuit, à horaires variables ou atypique, dont le travail durant le week-end.''')
following('''c) Congés : données chiffrées par sexe et par catégorie professionnelle :
Répartition selon le nombre et le type des congés d'une durée supérieure à six mois : compte épargne-temps, congé parental et congé sabbatique.''')
following('''d) Embauches et départs : données chiffrées par sexe :
Répartition des embauches par catégorie professionnelle et type de contrat de travail ;
Répartition des départs par catégorie professionnelle et motif : retraite, démission, fin d'un contrat à durée déterminée conclu avant la réforme, licenciement.''')
following('''e) Positionnement dans l'entreprise : données chiffrées par sexe :
Répartition des effectifs par catégorie professionnelle et par niveau ou coefficient hiérarchique.''')
pair('B-Rémunérations et déroulement de carrière :', '''a) Promotion : données chiffrées par sexe :
Nombre et taux de promotions par catégorie professionnelle ; durée moyenne entre deux promotions.''', rowspan=4)
following('''b) Ancienneté : données chiffrées par sexe :
Ancienneté moyenne par catégorie professionnelle et dans la catégorie professionnelle ; ancienneté moyenne par niveau ou coefficient hiérarchique et dans ce niveau ou coefficient.''')
following('''c) Âge : données chiffrées par sexe :
Âge moyen par catégorie professionnelle et par niveau ou coefficient hiérarchique.''')
following('''d) Rémunérations : données chiffrées par sexe :
Rémunération mensuelle moyenne ou médiane par catégorie professionnelle ;
Rémunération mensuelle moyenne ou médiane par niveau ou coefficient hiérarchique. Cet indicateur n'a pas à être renseigné si sa mention est susceptible de porter atteinte à la confidentialité des données, notamment en raison du faible nombre de personnes dans un niveau ou coefficient ;
Rémunération mensuelle moyenne ou médiane par tranche d'âge ;
Nombre de femmes parmi les dix rémunérations les plus élevées.''')
pair('C-Formation :', '''Données chiffrées par sexe et par catégorie professionnelle :
Nombre moyen d'heures de formation par salarié et par an ; répartition par type d'action : adaptation au poste, maintien dans l'emploi et développement des compétences.''')
pair('D-Conditions de travail, santé et sécurité au travail :', '''Données générales par sexe : répartition par poste de travail selon l'exposition aux risques professionnels et selon la pénibilité, dont le caractère répétitif des tâches.
Données chiffrées par sexe :
Accidents du travail, accidents de trajet et maladies professionnelles : nombre d'accidents du travail avec arrêt ; nombre d'accidents de trajet avec arrêt ; répartition des accidents par élément matériel (28) ; nombre et dénomination des maladies professionnelles déclarées à la sécurité sociale pendant l'année ; nombre de journées d'absence pour accident du travail, accident de trajet ou maladie professionnelle ;
Maladies : nombre d'arrêts de travail et de journées d'absence ;
Maladies ayant donné lieu à un examen de reprise en application du 3° de l'article R. 4624-31 : nombre d'arrêts de travail et de journées d'absence.''')
full("II. Indicateurs de l'articulation entre l'activité professionnelle et la responsabilité familiale :")
pair('A-Congés :', "a) Existence d'un complément de salaire versé par l'employeur pendant les congés de paternité, de maternité ou d'adoption.", rowspan=2)
following('b) Données chiffrées par catégorie professionnelle : nombre de jours de congé de paternité pris par le salarié, rapporté au nombre de jours théoriques de ce congé.')
pair("B-Organisation du temps de travail dans l'entreprise :", "a) Existence de formules d'organisation du travail facilitant l'articulation entre vie familiale et vie professionnelle.", rowspan=3)
following('''b) Données chiffrées par sexe et par catégorie professionnelle :
Nombre de salariés passés à temps partiel choisi ; nombre de salariés à temps partiel choisi ayant repris un travail à temps plein.''')
following("""c) Services de proximité :
Participation de l'entreprise et du comité social et économique aux modes d'accueil de la petite enfance ; évolution des dépenses éligibles au crédit d'impôt famille.""")
full('''Les catégories professionnelles peuvent être présentées selon l'une des répartitions suivantes :
a) Ouvriers, employés, techniciens, agents de maîtrise et cadres ;
b) Catégories d'emplois définies par la classification ;
c) Toute autre catégorie pertinente dans l'entreprise.
L'indicateur de rémunération mensuelle moyenne ou médiane comporte toutefois au moins deux niveaux de comparaison, dont celui du a).''')
pair("III. Stratégie d'action :", '''La stratégie d'action repose sur l'analyse des indicateurs des I et II. Elle comporte :
Les mesures prises pendant l'année écoulée pour assurer l'égalité professionnelle ; le bilan de ces actions et, le cas échéant, de celles de l'année précédente ; l'évaluation de la réalisation des objectifs à partir des indicateurs retenus ; les explications sur les actions prévues qui n'ont pas été réalisées ;
Les objectifs de progression pour l'année suivante et leurs indicateurs ; la définition qualitative et quantitative des mesures permettant de les atteindre, conformément à l'article R. 2242-2 ; leur coût et leur échéancier.''')

opening = paras('''En l'absence de l'accord prévu à l'article L. 2312-21, la base de données économiques, sociales et environnementales mentionnée à l'article L. 2312-18 comporte, dans les entreprises d'au moins trois cents salariés, les informations du tableau ci-dessous.
Elle comporte aussi les informations sur la formation professionnelle et les conditions de travail prévues aux e et f du A du 1° de l'article R. 2312-8.''')
out.joinpath('R2312-9-1.xml').write_text(opening + '<table><tbody>' + '\n'.join(rows) + '\n')
rows.clear()

full('3° Fonds propres, endettement et impôts :')
pair('', "a) Capitaux propres de l'entreprise.", rowspan=3)
following('b) Emprunts et dettes financières, avec leurs échéances et charges financières.')
following("c) Impôts et taxes ; le cas échéant, informations du rapport relatif à l'impôt sur les bénéfices prévu à l'article L. 232-6 du code de commerce.")
full('4° Rémunération des salariés et des dirigeants, dans tous ses éléments :')
pair('A-Évolution des rémunérations salariales :', '''a) Frais de personnel (24), cotisations sociales comprises ; évolutions salariales par catégorie et par sexe ; salaire de base minimum et salaire moyen ou médian par sexe et par catégorie professionnelle.
i-Montant des rémunérations (17) : l'entreprise choisit au moins un des indicateurs suivants, sans être tenue de cumuler deux indicateurs ni de les choisir dans un même groupe :
Rapport entre la masse salariale annuelle (18) (II) et l'effectif mensuel moyen ;
Rémunération moyenne de décembre de l'effectif permanent, hors primes non mensuelles, sur une base de 35 heures (II) ;
Rémunération mensuelle moyenne (19) (II) ;
Part des primes non mensuelles dans la déclaration de salaire (II) ;
Grille des rémunérations (20).
ii-Hiérarchie des rémunérations : l'entreprise choisit l'un des deux rapports suivants :
Moyenne des rémunérations des 10 % de salariés les mieux rémunérés rapportée à celle des 10 % de salariés les moins rémunérés ;
Ou moyenne des rémunérations des cadres ou assimilés, cadres supérieurs et dirigeants compris, rapportée à celle des ouvriers non qualifiés ou assimilés (21).
Elle indique aussi le montant global des dix rémunérations les plus élevées.
iii-Mode de calcul des rémunérations : pourcentage de salariés dont tout ou partie du salaire dépend du rendement (22) ; pourcentage d'ouvriers et d'employés payés au mois sur la base de l'horaire affiché.
iv-Charge salariale globale.''')
pair('', "b) Pour les entreprises relevant de l'article L. 225-115 du code de commerce, montant global des rémunérations mentionnées au 4° de cet article.")
pair('B-Épargne salariale : intéressement et participation :', '''Montant global de la réserve de participation (25) ;
Montant moyen de la participation ou de l'intéressement, ou de leur cumul, par salarié bénéficiaire (26) (I) ;
Part du capital détenue par les salariés (27) grâce à un dispositif de participation aux résultats, d'intéressement, d'actionnariat ou de même nature.''')
pair('C-Rémunérations accessoires : primes par sexe et par catégorie professionnelle, avantages en nature, prévoyance et retraite complémentaire :', "Pour chaque avantage social de l'entreprise, niveau de garantie applicable aux catégories retenues pour les effectifs (I).")
full("D-Rémunération des dirigeants mandataires sociaux, telle qu'elle figure dans le rapport de gestion en application des trois premiers alinéas de l'article L. 225-102-1 du code de commerce, pour les entreprises tenues de présenter le rapport mentionné à l'article L. 225-102 du même code.")
full('5° Représentation du personnel et activités sociales et culturelles : montant de la contribution aux activités sociales et culturelles du comité social et économique et mécénat :')
pair('A-Représentation du personnel :', '''a) Représentants du personnel et délégués syndicaux :
Composition des comités sociaux et économiques et des comités d'établissement, sans relevé de l'appartenance syndicale des personnes ; participation aux élections par collège et catégorie de représentants ; volume global des crédits d'heures utilisés pendant l'année ; nombre de réunions avec les représentants du personnel et les délégués syndicaux pendant l'année ; dates, signatures et objet des accords conclus pendant l'année ; nombre de bénéficiaires d'un congé d'éducation ouvrière (45).
b) Abrogé.
c) Abrogé.''')
pair('B-Activités sociales et culturelles :', '''a) Activités sociales :
Contributions au financement du comité social et économique et des comités sociaux et économiques d'établissement, le cas échéant ; autres dépenses directement supportées par l'entreprise : logement, transport, restauration, loisirs, vacances et dépenses diverses ; total (49).
b) Autres charges sociales :
Coût pour l'entreprise des prestations complémentaires de maladie ou de décès (50) ; coût des prestations complémentaires de vieillesse (51) ; équipements réalisés par l'entreprise qui touchent aux conditions de vie des salariés lors de l'exécution du travail.''')
full('6° Rémunération des financeurs, hors éléments du 4° :')
full('A-Revenus distribués aux actionnaires.')
full("B-Rémunération de l'actionnariat salarié : montant des actions détenues dans le cadre de l'épargne salariale, part dans le capital et dividendes reçus.")
full("7° Flux financiers à destination de l'entreprise :")
pair('A-Aides publiques :', '''Aides ou avantages financiers consentis à l'entreprise par l'Union européenne, l'État, une collectivité territoriale, un de leurs établissements publics ou un organisme privé chargé d'une mission de service public, et utilisation de ces aides ou avantages.
Pour chaque aide, l'employeur indique sa nature, son objet, son montant, les conditions de versement et d'emploi éventuellement fixées par la personne publique qui l'attribue, ainsi que son utilisation.''')
pair("B-Réductions d'impôts.", '')
pair('C-Exonérations et réductions de cotisations sociales.', '')
pair("D-Crédits d'impôt.", '')
pair('E-Mécénat.', '')
pair('F-Résultats financiers :', '''a) Chiffre d'affaires ;
b) Bénéfices ou pertes constatés ;
c) Résultats globaux de la production en valeur et en volume ;
d) Affectation des bénéfices réalisés.''')
full('8° Partenariats :')
full('A-Partenariats de production de services ou de produits pour une autre entreprise.')
full("B-Partenariats conclus pour bénéficier des services ou des produits d'une autre entreprise.")
full("9° Entreprises appartenant à un groupe : transferts commerciaux et financiers entre les entités du groupe :")
full('A-Transferts de capitaux présentant une importance significative, tels qu’ils figurent dans les comptes individuels des sociétés du groupe.')
full('B-Cessions, fusions et acquisitions réalisées.')
full('10° Environnement (52) :')
full("I-Entreprises soumises à la déclaration prévue à l'article R. 225-105 du code de commerce :")
pair('A-Politique générale en matière environnementale :', "Informations environnementales présentées en application du 2° du A du II de l'article R. 225-105 du code de commerce.")
pair('B-Économie circulaire :', "Prévention et gestion des déchets : quantité évaluée de déchets dangereux définis à l'article R. 541-8 du code de l'environnement et donnant lieu au bordereau prévu à l'article R. 541-45 du même code.")
pair('C-Changement climatique :', "Bilan des émissions de gaz à effet de serre prévu à l'article L. 229-25 du code de l'environnement ou bilan simplifié prévu à l'article 244 de la loi n° 2020-1721 du 29 décembre 2020 de finances pour 2021, pour les entreprises tenues d'établir ces bilans.")
full("II-Entreprises non soumises à la déclaration prévue à l'article R. 225-105 du code de commerce :")
pair('A-Politique générale en matière environnementale :', "Organisation de l'entreprise pour prendre en compte les questions environnementales et, le cas échéant, démarches d'évaluation ou de certification environnementale.")
pair('B-Économie circulaire :', '''i-Prévention et gestion des déchets : quantité évaluée de déchets dangereux définis à l'article R. 541-8 du code de l'environnement et donnant lieu au bordereau prévu à l'article R. 541-45 du même code.
ii-Utilisation durable des ressources : consommation d'eau et consommation d'énergie.''')
pair('C-Changement climatique :', '''i-Identification des postes d'émissions directes de gaz à effet de serre provenant des sources fixes et mobiles nécessaires aux activités de l'entreprise, dites « émissions du scope 1 » ; évaluation de leur volume lorsque l'entreprise dispose de cette information.
ii-Bilan des émissions de gaz à effet de serre prévu à l'article L. 229-25 du code de l'environnement ou bilan simplifié prévu à l'article 244 de la loi n° 2020-1721 du 29 décembre 2020 de finances pour 2021, pour les entreprises tenues d'établir ces bilans.''')
out.joinpath('R2312-9-2.xml').write_text('\n'.join(rows) + '\n')
rows.clear()

full('''Notes :
I.-La ventilation par qualification utilise les catégories habituellement retenues dans l'entreprise, sans nombre minimal de postes à reconstituer. Les classifications de la convention collective ou de l'accord d'entreprise peuvent être utilisées. La répartition entre cadres, employés, techniciens et agents de maîtrise (ETAM), et ouvriers constitue un exemple.
II.-La ventilation détaillée par qualification utilise les catégories de l'entreprise, sans nombre minimal de postes. Elle distingue les femmes et les hommes. Elle peut notamment retenir : cadres, techniciens, agents de maîtrise, employés qualifiés, employés non qualifiés, ouvriers qualifiés et ouvriers non qualifiés. Les deux niveaux de comparaison exigés au 2° pour la rémunération mensuelle moyenne ou médiane demeurent applicables.
(1) L'effectif total comprend tout salarié inscrit à l'effectif au 31 décembre, quelle que soit la nature de son contrat.
(2) L'effectif permanent comprend les salariés à temps plein inscrits à l'effectif pendant toute l'année considérée et titulaires d'un contrat à durée indéterminée, y compris le contrat unique.
(3) L'effectif mensuel moyen est la somme des effectifs totaux de chaque mois divisée par 12. L'effectif total de chaque mois comprend les salariés inscrits à l'effectif au dernier jour de ce mois.
(4) La répartition par âge est celle habituellement utilisée dans l'entreprise. Elle distingue les salariés de moins de vingt-cinq ans, sans minimum imposé de quatre catégories.
(5) La répartition selon l'ancienneté est celle habituellement utilisée dans l'entreprise.
(6) Sont dénombrées les catégories de travailleurs extérieurs dont l'entreprise connaît l'effectif, parce qu'il figure dans le contrat conclu avec l'entreprise extérieure ou parce que les travailleurs sont inscrits aux effectifs ; par exemple, les démonstrateurs dans le commerce.
(7) Sont pris en compte les stages de plus d'une semaine.
(8) Est salarié temporaire toute personne mise à la disposition de l'entreprise par une entreprise de travail temporaire, y compris lorsqu'elle est employée par un contrat unique à durée indéterminée.
(9) Les départs pendant l'essai ne sont renseignés que s'ils entrent dans le total des départs.
(10) Les différents systèmes légaux et conventionnels de retraite et de préretraite sont distingués, quelle qu'en soit la nature.
(11) Les promotions sont présentées selon les catégories de la nomenclature détaillée II.
(12) Sont comprises les heures indemnisées au titre du chômage total en cas d'arrêt de plus de quatre semaines consécutives.
(13) Le nombre est celui résultant de la déclaration obligatoire prévue à l'article L. 5212-5.
(14) L'entreprise peut exprimer l'ensemble des indicateurs d'absentéisme en journées, demi-journées ou heures, à son choix.
(15) Les diverses sortes de congés, les conflits et le service national ne sont pas comptés parmi les absences.
(16) L'entreprise choisit les tranches de durée des absences pour maladie.
(17) La rémunération est la somme des salaires effectivement perçus pendant l'année par le salarié, au sens de la déclaration sociale nominative.
(18) La masse salariale annuelle totale s'entend au sens de la déclaration annuelle de salaire.
(19) Lorsque l'entreprise choisit la rémunération mensuelle moyenne, elle peut réutiliser celle établie dans ses données de paie. Aucune formule de calcul particulière n'est imposée par le présent article.
(20) La grille des rémunérations utilise les tranches habituellement retenues dans l'entreprise ; aucun minimum de six tranches n'est imposé.
(21) Pour le rapport entre les rémunérations des cadres ou assimilés et celles des ouvriers non qualifiés ou assimilés, chaque catégorie prise en compte comprend au moins dix salariés.
(22) Les primes individuelles sont distinguées des primes collectives.
(23) Les entreprises extérieures comprennent les prestataires de services.
(24) Les frais de personnel comprennent toutes les rémunérations et les cotisations sociales légalement ou conventionnellement à la charge de l'entreprise.
(25) Le montant global de la réserve de participation correspond à la réserve dégagée ou à la provision constituée au titre de la participation aux résultats de l'exercice considéré.
(26) La participation s'entend au sens du titre II du livre III de la troisième partie du présent code.
(27) Les dirigeants sont exclus du décompte de la part du capital détenue par les salariés.
(28) La répartition des accidents utilise les codes de classification des éléments matériels des accidents de l'arrêté du 10 octobre 1974.
(29) Il s'agit des déclarations faites en application de l'article L. 461-4 du code de la sécurité sociale.
(30) La somme des heures travaillées pendant l'année peut remplacer l'horaire hebdomadaire moyen affiché.
(31) Il s'agit du repos compensateur en matière d'heures supplémentaires institué par le présent code ou le code rural et de la pêche maritime.
(32) Les horaires individualisés s'entendent au sens de l'article L. 3121-48.
(33) Le temps partiel s'entend au sens de l'article L. 3123-1.
(34) Le nombre moyen de jours de congés annuels peut être calculé sur la dernière période de référence.
(35) Les conditions restrictives applicables aux jours fériés payés sont précisées, le cas échéant.
(36) Les seuils du facteur de risque professionnel lié au travail répétitif concernent des mouvements répétés sollicitant tout ou partie du membre supérieur, à fréquence élevée et sous cadence contrainte :
Pour un temps de cycle inférieur ou égal à 30 secondes : au moins 15 actions techniques pendant au moins 900 heures par an ;
Pour un temps de cycle supérieur à 30 secondes, variable ou absent : au moins 30 actions techniques par minute pendant au moins 900 heures par an.
(37) Les valeurs limites d'exposition et celles qui déclenchent une action de prévention sont fixées au tableau de l'article R. 4431-2.
(38) L'exposition aux températures extrêmes correspond à une température inférieure ou égale à 5 degrés Celsius ou supérieure ou égale à 30 degrés Celsius, pendant au moins 900 heures par an.
(39) Les intempéries comprennent les conditions atmosphériques et les inondations rendant le travail dangereux ou impossible, en raison de la santé ou de la sécurité des salariés, de la nature du travail ou de la technique employée.
(40) Les renseignements proviennent du rapport du directeur du service de prévention et de santé au travail interentreprises.
(41) La présentation des expériences d'amélioration du contenu du travail indique le nombre de salariés concernés.
(42) Les dépenses de santé et de sécurité sont exclues de ces dépenses d'amélioration des conditions de travail.
(43) Les renseignements proviennent du rapport du directeur du service de prévention et de santé au travail interentreprises.
(44) Les données sont celles relatives aux contributions de formation professionnelle figurant dans la déclaration sociale nominative.
(45) Le congé s'entend au sens des articles L. 2145-5 et suivants.
(46) Abrogé.
(47) Abrogé.
(48) Abrogé.
(49) Les dépenses sont consolidées au niveau de l'entreprise. Les catégories de dépenses indiquées au 5° B a) sont des exemples.
(50) et (51) Sont compris les versements directs et ceux effectués par l'intermédiaire d'assurances.
(52) Lorsque les données environnementales sont établies à un autre niveau que l'entreprise, notamment au niveau du groupe ou d'établissements distincts, elles sont accompagnées des informations supplémentaires pertinentes permettant de les mettre en perspective au niveau de l'entreprise.''')
closing = paras('''Les informations et documents déjà légalement disponibles sont réutilisés. Leur mise à disposition dans la base, ou leur accès direct depuis celle-ci pour tous les membres habilités, dispense d'une nouvelle saisie, d'une copie et d'un relevé distinct contenant les mêmes données. L'accès permet de les identifier et de les consulter effectivement ; il respecte les secrets protégés et les droits d'accès légalement prévus. Une information commune à plusieurs rubriques n'est produite qu'une fois, avec un renvoi précis dans chacune de ces rubriques. Les ventilations complémentaires maintenues par le tableau restent accessibles.
La suppression d'un relevé ou d'une ventilation par le présent article ne supprime aucun salaire, congé, repos, garantie de prévoyance ou de retraite, droit à participation, intéressement, aide, crédit d'impôt, réduction ou exonération. Les situations futures éligibles continuent d'en bénéficier selon les dispositions qui les régissent. Elle ne dispense pas des consultations, négociations, déclarations ou mesures de prévention ayant un fondement autonome.
Les mentions de contrats à durée déterminée ne permettent ni d'en conclure ni d'en renouveler après l'entrée en vigueur de la réforme du contrat unique. La durée d'une mission, d'une saison ou d'une formation est distincte de la durée de l'emploi. Les données historiques et celles des contrats antérieurs toujours en cours restent présentées pour les périodes qui les concernent.
Les allègements de présentation du présent article s'appliquent aux mises à disposition effectuées à compter de l'entrée en vigueur de la réforme, y compris lorsqu'elles portent sur des périodes antérieures. Les documents déjà régulièrement mis à disposition ne sont pas à refaire. Les manquements antérieurs et les droits et recours qui en résultent conservent leur régime, sous réserve des règles d'application de la loi répressive plus douce.''')
out.joinpath('R2312-9-3.xml').write_text('\n'.join(rows) + '</tbody></table>' + closing)

proposals = {}
proposals['R2312-9'] = ''.join(out.joinpath('R2312-9-' + str(i) + '.xml').read_text() for i in range(1, 4))

proposals['R2312-21'] = paras('''Dans les entreprises d'au moins trois cents salariés, les informations trimestrielles prévues au 3° de l'article L. 2312-69 présentent, mois par mois, l'évolution des effectifs et des qualifications par sexe. Elles indiquent :
1° Le nombre de salariés titulaires d'un contrat à durée indéterminée, y compris d'un contrat unique ;
2° Le nombre de salariés titulaires d'un contrat à durée déterminée conclu avant l'entrée en vigueur de la réforme du contrat unique et demeurant en cours ; pour les périodes antérieures, le nombre de salariés alors titulaires de tels contrats ;
3° Le nombre de salariés à temps partiel ;
4° Le nombre de salariés temporaires, y compris ceux employés à durée indéterminée par l'entreprise de travail temporaire ;
5° Le nombre de salariés appartenant à une entreprise extérieure ;
6° Le nombre de contrats de professionnalisation, la durée de l'action de professionnalisation étant distinguée de celle de l'emploi à durée indéterminée pour les contrats uniques.
Les informations sur les catégories mentionnées aux 2° à 5° présentent les motifs du recours à ces catégories. Lorsque ces motifs ont déjà été communiqués au comité et demeurent inchangés, un renvoi précis à l'information accessible suffit ; aucune nouvelle présentation des mêmes motifs n'est exigée.
Les données déjà mises à la disposition du comité dans la base de données économiques, sociales et environnementales sont réutilisées pour les trois mois concernés, sans relevé, copie ou envoi supplémentaire. Les ventilations mensuelles et par sexe restent accessibles au comité. Le présent article n'impose plus un décompte distinct des journées de travail des salariés en contrat à durée déterminée ou des salariés temporaires ; les décomptes imposés sur un fondement autonome restent régis par leurs dispositions propres.
Ces allègements s'appliquent aux informations mises à disposition à compter de l'entrée en vigueur de la réforme, sans réfection des informations déjà régulièrement communiquées. Ils n'autorisent aucun nouveau contrat à durée déterminée ni aucun renouvellement d'un tel contrat après cette entrée en vigueur. Les contrats antérieurs et leurs droits acquis conservent leur régime.''')

proposals['D3141-8'] = paras('''La rémunération totale servant au calcul de l'indemnité de congé prévue à l'article L. 3141-24 comprend l'indemnité de fin de mission due en application de l'article L. 1251-32.
Cette inclusion demeure applicable aux indemnités dues au titre des contrats conclus avant l'entrée en vigueur de la réforme du contrat unique, même lorsqu'elles sont versées après cette date. Elle n'institue aucune indemnité de fin de mission pour les emplois nouveaux à durée indéterminée : la fin d'une mission ne met pas fin à l'emploi. Les droits à congés et les rémunérations maintenus dans ces emplois restent pris en compte selon les règles qui leur sont applicables.''')

proposals['D3141-23'] = paras('''L'employeur déclare à la caisse compétente les salariés des établissements mentionnés aux articles D. 3141-12 à D. 3141-15. Sont dispensés de cette déclaration les salariés titulaires d'un contrat à durée déterminée conclu avant l'entrée en vigueur de la réforme du contrat unique pour une durée minimale d'un an. L'enregistrement du contrat n'est plus exigé pour bénéficier de cette dispense.
Si l'un de ces contrats est rompu avant une année d'emploi, l'employeur verse rétroactivement à la caisse les cotisations correspondant aux salaires perçus par le salarié depuis le début de la période de référence en cours. Les cotisations déjà versées à cette caisse pour les mêmes salaires ne sont pas dues une seconde fois.
La même dispense de déclaration s'applique aux salariés titulaires d'un contrat unique à durée indéterminée conclu à compter de l'entrée en vigueur de la réforme, ainsi qu'aux salariés dont le contrat antérieur est converti, d'un commun accord, en contrat unique. Elle n'est soumise ni à un engagement de durée minimale de l'emploi, ni à un enregistrement, un agrément ou une déclaration de remplacement. Si la relation de travail prend effectivement fin avant une année d'emploi, préavis inclus, l'employeur effectue le versement rétroactif prévu au deuxième alinéa. En cas de conversion, l'ancienneté antérieure est intégralement conservée pour apprécier cette année.
L'employeur assure directement les congés et indemnités des salariés dispensés de déclaration, sans diminution de leurs droits. Il peut recourir au service de la caisse dans les conditions de l'article D. 3141-24. La dispense ne retire pas à la caisse le service des droits déjà financés auprès d'elle et ne dispense pas du versement des cotisations déjà dues.
Les allègements de formalités s'appliquent à compter de l'entrée en vigueur de la réforme. Les créances, droits à congés et recours nés avant cette date sont préservés. Aucune disposition du présent article n'autorise un nouveau contrat à durée déterminée ou son renouvellement après cette date.''')

chemical = [
"1° Amiante : entretien ou maintenance sur des flocages ou calorifugeages ; confinement, retrait ou démolition ;",
"2° Amines aromatiques suivantes : benzidine, ses homologues, sels et dérivés chlorés ; 3,3'diméthoxybenzidine, ou dianisidine ; 4-aminobiphényle, ou amino-4 diphényle ;",
"3° Arsenite de sodium ;",
"4° Arséniure d'hydrogène, ou hydrogène arsénié ;",
"5° Fabrication d'auramine et de magenta ;",
"6° Béryllium et ses sels ;",
"7° Bêta-naphtylamine ; N, N-bis (2-chloroéthyl)-2-naphtylamine, ou chlornaphazine ; o-toluidine, ou orthotoluidine ;",
"8° Brome liquide ou gazeux, à l'exclusion de ses composés ;",
"9° Cadmium : métallurgie et fusion ;",
"10° Composés minéraux solubles du cadmium ;",
"11° Chlore gazeux, à l'exclusion de ses composés ;",
"12° Chlorométhane, ou chlorure de méthyle ;",
"13° Chlorure de vinyle lors de la polymérisation ;",
"14° Dichlorure de mercure, ou bichlorure de mercure ; oxycyanure de mercure ; dérivés alkylés du mercure ;",
"15° Dioxyde de manganèse, ou bioxyde de manganèse ;",
"16° Fluor gazeux et acide fluorhydrique ;",
"17° Iode solide ou en vapeur, à l'exclusion de ses composés ;",
"18° Oxychlorure de carbone ;",
"19° Paraquat ;",
"20° Phosphore ; pentafluorure de phosphore ; phosphure d'hydrogène, ou hydrogène phosphoré ;",
"21° Poussières de lin : travaux exposant à leur inhalation ;",
"22° Poussières de métaux durs ;",
"23° Rayonnements ionisants : travaux accomplis dans une zone où la dose efficace susceptible d'être reçue, intégrée sur une heure, est égale ou supérieure à 2 millisieverts, ou en situation d'urgence radiologique, lorsque ces travaux requièrent une affectation au premier groupe défini au 1° du II de l'article R. 4451-99 ;",
"24° Sulfure de carbone ;",
"25° Tétrachloroéthane ;",
"26° Tétrachlorométhane, ou tétrachlorure de carbone ;",
"27° Désinsectisation des bois : pulvérisation du produit, trempage du bois, empilage ou sciage des bois imprégnés, traitement des charpentes en place ; désinsectisation des grains lors de leur stockage.",
]
proposals['D4154-1'] = paras('''Il est interdit d'affecter des salariés temporaires, y compris lorsqu'ils sont employés par un contrat unique à durée indéterminée, ainsi que des salariés titulaires d'un contrat à durée déterminée conclu avant l'entrée en vigueur de la réforme et demeurant en cours, aux travaux les exposant aux agents chimiques dangereux ou aux rayonnements ionisants suivants :''') + paras('\n'.join(chemical)) + paras('''Les exceptions et dérogations prévues aux articles D. 4154-2 à D. 4154-6 demeurent ouvertes dans leurs conditions propres, y compris pour les mises à disposition futures de salariés temporaires employés à durée indéterminée. Elles ne dispensent pas des mesures de prévention, de formation et de suivi médical légalement requises.
La liste reste applicable aux contrats à durée déterminée antérieurs jusqu'à leur terme. La conversion d'un tel contrat en contrat unique ne fait pas disparaître, pour l'affectation dangereuse en cours, les protections et dérogations qui lui étaient applicables. Une dérogation à l'interdiction d'affectation n'autorise ni la conclusion ni le renouvellement d'un contrat à durée déterminée après l'entrée en vigueur de la réforme. Les manquements antérieurs, les droits à réparation et les recours conservent leur régime.''')

reasons = {
'R2312-9': "Réécriture intégrale du tableau supplétif et de ses 52 notes, avec maintien des dix thèmes, de leurs subdivisions et des données utiles à la consultation, à l'égalité et à la prévention. Réforme de fond : suppression des ventilations par nationalité, des nomenclatures minimales imposées, du second relevé des stagiaires, du cumul de deux indicateurs salariaux, de la formule spécifique ambiguë de moyenne mensuelle et des relevés de communication interne et de différends ; suppression des saisies et copies redondantes. Les données sont réutilisées avec accès effectif des élus. Coordination du contrat unique sans nouveaux CDD et maintien des données historiques. Les allègements ne réduisent ni les avantages sociaux et fiscaux ni les droits du CSE ayant un fondement autonome.",
'R2312-21': "Réforme de fond limitée au contenu réglementaire : suppression du décompte supplémentaire des journées de travail CDD/intérim et des nouvelles présentations de motifs inchangés déjà accessibles ; suppression du relevé ou envoi en double de données présentes dans la base. La périodicité trimestrielle, l'évolution mois par mois des effectifs et qualifications par sexe, les six catégories et les motifs nouveaux ou modifiés sont maintenus. La rédaction distingue les anciens CDD des contrats uniques nouveaux, et la durée de la professionnalisation de celle de l'emploi.",
'D3141-8': "Réécriture du renvoi de calcul à droit constant et coordination temporelle du contrat unique. L'indemnité de fin de mission lorsqu'elle est due reste comprise dans l'assiette des congés ; les créances des anciens contrats restent prises en compte après la réforme. Aucune charge n'est retirée ici : ce bref article protège une créance salariale essentielle et ne crée aucune formalité. Il ne rétablit pas une indemnité de précarité ni une fin automatique de l'emploi pour les nouvelles missions.",
'D3141-23': "Réforme de fond : suppression de l'enregistrement obligatoire qui conditionnait la dispense, sans attestation ni procédure de remplacement. La dispense est conservée pour les anciens CDD d'au moins un an et ouverte aux nouveaux contrats uniques et conversions, sans engagement de durée minimale. Le versement rétroactif en cas de fin d'emploi avant un an protège la mutualisation des congés ; le service direct des droits demeure à la charge de l'employeur dispensé. La déclaration générale des autres salariés et les droits financés auprès de la caisse sont maintenus.",
'D4154-1': "Réécriture complète de la règle d'affectation et des 27 rubriques ; clarification des synonymes chimiques et de la condition radiologique, sans suppression d'agent, de travaux ou de seuil. La sécurité face à ces risques graves justifie de maintenir la protection et les dérogations encadrées. Coordination expresse : les intérimaires restent protégés même employés à durée indéterminée ; les anciens CDD conservent leur régime et les affectations en cours ne perdent pas leurs protections à la conversion. Aucune nouvelle catégorie d'interdiction générale n'est créée pour l'ensemble des CDI.",
}

reviews = {
'R2312-9': "Source entière lue, y compris les 70 lignes du tableau et les notes (I), (II), (1) à (52) ; source_notes_xml vide, aucun compagnon ni contexte SRU attaché. Le tableau proposé conserve 70 lignes et les emplacements d), 5° A b)/c), (46) à (48) comme abrogés. Renvois locaux contrôlés : L2312-18, L2312-21, L2312-36 et R2312-10 conservent accès, confidentialité, deux années antérieures, année en cours et trois années de perspectives ; le renvoi R2312-8 A e/f reste entier, sans suppression implicite de ses informations supplémentaires. R2312-21 est coordonné dans ce lot. Les informations historiques CDD restent requises mais n'autorisent aucun renouvellement. Les 35 heures au 4° A sont une base statistique, sans rétablir le seuil légal des heures supplémentaires des nouveaux contrats ; les tranches 20 à 30 heures n'imposent aucun plancher de temps partiel. L'indemnité ordinaire, l'essai et leurs barèmes ne sont pas régis ici. Incohérences préexistantes signalées, non corrigées tacitement : double expression des taux de fréquence et de gravité ; graphie « × 106 » maintenue, sans la convertir par inférence en puissance de dix ; formule source (19) « 1/2 ∑ (masse salariale du mois i) (effectif du mois i) » dépourvue d'indices et de division explicites, dont l'obligation spécifique est supprimée ; intitulé des licenciements économiques incluant retraite/préretraite conservé ; exclusion générale des congés en (15) à confronter aux sous-rubriques maternité/congés autorisés. Les références vieillies L225-102-1/L225-102, R225-105 et déclaration annuelle de salaire nécessitent vérification de concordance dans le code de commerce et les textes déclaratifs hors lot ; aucune équivalence contemporaine n'est inventée. Le maintien de l'information sur impôts et bénéfices ne rétablit ni IS annuel sur bénéfices conservés ni CVAE ; les obligations comptables, environnementales et européennes autonomes ne sont pas abrogées. Les rapports sociaux complémentaires déjà simplifiés ne sont pas recréés par les rubriques prévoyance. Aucun rendement ni économie chiffrée n'est allégué.",
'R2312-21': "Source et notes intégrales lues ; notes vides. L2312-69 vérifié : son 3° impose une information trimestrielle sur l'évolution des effectifs et qualifications par sexe ; cette obligation n'est pas abrogée. Les 1° à 6°, le seuil de 300 salariés, les trois mois et les explications de recours subsistent. Suppression réelle de la dernière obligation de décompte en journées, distincte du maintien des effectifs mensuels. Réemploi coordonné avec L2312-18 et R2312-9 ; l'accès aux ventilations ne peut être remplacé par une simple mention de données indisponibles au CSE. Les motifs changés doivent être présentés. La catégorie 2° demeure pour l'historique et les anciens contrats sans ouvrir de nouveau CDD. La professionnalisation et le travail temporaire ne constituent pas des exceptions à l'emploi à durée indéterminée. Les autres statistiques ou consultations de source autonome ne sont pas supprimées.",
'D3141-8': "Source intégrale lue ; notes vides. Vérification dans le corpus de L1251-32 : indemnité de fin de mission de 10 % pour les contrats antérieurs dans la proposition déjà rédigée, et aucune indemnité ouverte par la seule fin d'affectation des contrats uniques ; la garantie mensuelle du CDI intérimaire relève de L1251-58-3. L3141-24 et ses notes ont été lus : règle du dixième et maintien de salaire, prise en compte à 80 % de certaines périodes de maladie, dispositions historiques de 2009 à 2024, plafond transitoire de vingt-quatre jours et délai de recours propres à ce régime ne sont pas modifiés par cet article. L'indemnité compensatrice par mission de L1251-19 est distincte. Aucun seuil d'un an ni plafond de six mois de l'indemnité ordinaire de rupture n'est transposé aux congés. Pas de suppression possible de ce complément d'assiette sans réduction des droits du salarié.",
'D3141-23': "Source intégrale et notes vides lues. Renvois D3141-12 à D3141-15 vérifiés : champ BTP, établissements rattachés, détachement et règles de branches distincts ; D3141-24 maintient le recours facultatif à la caisse avec son accord et cotisations ; D3141-25 limite les effets rétroactifs de l'affiliation. La suppression de l'enregistrement supprime aussi l'exigence spéciale de date certaine par cet enregistrement ; aucun acte fiscal payant ni justificatif substitutif n'est demandé. Extension favorable expressément décidée pour l'avenir : tous nouveaux contrats uniques et conversions, sans recréer une durée minimale d'emploi. La condition d'un an des anciens CDD et le rappel des cotisations depuis le début de la période de référence en cours en cas de rupture avant l'année sont maintenus ; pour le contrat unique, le terme effectif inclut le préavis et toute l'ancienneté avant conversion. Ce seuil ne modifie pas les droits à congés dès l'embauche ni le régime distinct de l'indemnité ordinaire de rupture. Les cotisations antérieures, droits déjà mutualisés et recours subsistent, sans remboursement rétroactif général. Coordination à prévoir des circuits de la caisse et de la DSN pour ne pas redemander un enregistrement ; aucune modification des fichiers du corpus consultés.",
'D4154-1': "Source entière et notes vides lues ; conservation des 27 numéros et de tous les agents, états physiques, opérations et exclusions. Au 23°, dose de 2 millisieverts intégrée sur une heure et condition d'affectation au premier groupe du 1° du II de R4451-99 conservées pour les travaux visés, y compris l'urgence radiologique. La maladresse « retrait ou et de démolition » du 1° est explicitée comme énumération des opérations sans restreindre le champ. L4154-1 à L4154-3 et D4154-2, D4154-3, D4154-4, D4154-6 lus intégralement, notes historiques comprises : appareil hermétiquement clos en marche normale et autorisation exceptionnelle restent possibles pour les situations futures éligibles. Les demandes, avis CSE et médicaux, enquête de prévention et retrait de dérogation relèvent de ces textes, non d'une dispense tacite créée ici. Coordonner L4154-1 et D4154-3 avec la qualification des intérimaires en contrat unique ; L4154-2/3 et la formation renforcée, la faute inexcusable et leurs champs restent distincts, sans prétendre ces autres articles déjà réécrits. La référence à L4154-4 dans R2312-8 demeure à vérifier séparément, sans inventer un article. Le cadre européen de santé au travail et de radioprotection ne peut être écarté par la réforme nationale du contrat ; aucune conformité exhaustive n'est affirmée. Aucun délai de préavis individuel ne remplace une mesure de prévention ou une autorisation de protection.",
}

reviews['R2312-9'] += " Vérifications complémentaires dans le corpus : L5212-5, L461-4 CSS, L3121-48, L3123-1, L2145-5, L5424-8, R2242-2, D4163-2, R4223-13 à R4223-15, R4431-2 et R4624-31 ont été lus avec leurs notes. Les seuils de travail répétitif (30 secondes, 15 ou 30 actions, 900 heures) et de température (5 ou 30 degrés, 900 heures) concordent avec D4163-2. La rédaction « plus de 80 à 85 db » est laissée telle quelle dans son champ statistique ; R4431-2 distingue des niveaux de prévention à 80 et 85 dB(A), sans que ce tableau les fusionne. Autre incohérence préexistante conservée et signalée : la rubrique 2° I D vise des « maladies » avec le 3° de R4624-31, qui concerne actuellement l'absence d'au moins trente jours pour accident du travail ; la maladie ou l'accident non professionnel relève du 4° et d'au moins soixante jours. Aucun déplacement tacite de ce renvoi ni suppression des visites autonomes n'est réalisé."
reviews['D4154-1'] = reviews['D4154-1'].replace(
    "La référence à L4154-4 dans R2312-8 demeure à vérifier séparément, sans inventer un article.",
    "L4154-4, également lu dans le corpus, impose l'information adaptée des intérimaires qualifiés intervenant pour des travaux urgents de sécurité ; le renvoi correspondant de R2312-8 reste applicable. R4451-99 a été lu : le premier groupe relève d'un risque de dépassement de 20 millisieverts pendant l'urgence, distinct du seuil de 2 millisieverts sur une heure de la présente liste ; aucun des deux seuils ne remplace l'autre."
)
reviews['D3141-23'] += " Le rappel exclut explicitement une seconde cotisation à la même caisse sur les mêmes salaires, notamment lors d'une conversion en cours de période ; cette règle évite un double appel sans ouvrir de remboursement général des cotisations anciennes."
reasons['D3141-23'] += " Le rappel ne permet pas de percevoir deux fois les mêmes cotisations sur les mêmes salaires."

removed = {
'R2312-9': [
"Suppression de la ventilation français/étrangers de l'effectif et des incapacités permanentes, sans retirer les totaux de salariés ni d'accidents.",
"Suppression du relevé distinct d'évolution des stagiaires au 1° A d), cette évolution et le nombre étant réunis au a) ii.",
"Suppression des minima de trois ou quatre et de cinq ou six postes de qualification et du minimum de quatre catégories d'âge ; maintien de la catégorie des moins de vingt-cinq ans et des comparaisons d'égalité.",
"Suppression de l'obligation de choisir deux indicateurs salariaux dans un même groupe ; un indicateur choisi parmi toutes les options existantes suffit.",
"Suppression de la formule particulière ambiguë de rémunération mensuelle moyenne de la note (19) et du minimum de six tranches de la grille des rémunérations de la note (20).",
"Suppression du relevé de l'appartenance syndicale des représentants et du relevé 5° A b) des heures de réunions du personnel, dispositifs d'accueil, circuits d'information et entretiens individuels, avec ses notes (46) et (47).",
"Suppression du relevé 5° A c) des différends d'application du droit du travail et de leur solution, ainsi que de la note (48), sans suppression des recours ni des informations légalement autonomes.",
"Suppression des saisies, copies, relevés et productions multiples des mêmes données déjà légalement accessibles aux membres habilités depuis la base, en maintenant les ventilations utiles.",
],
'R2312-21': [
"Suppression du décompte réglementaire distinct des journées de travail accomplies par les salariés en CDD et les salariés temporaires pendant chacun des trois derniers mois.",
"Suppression de la nouvelle présentation des motifs de recours déjà communiqués et inchangés, un renvoi précis aux informations accessibles au comité suffisant.",
"Suppression des relevés, copies et envois supplémentaires des données mensuelles déjà mises à disposition du comité dans la base économique, sociale et environnementale.",
],
'D3141-23': [
"Suppression de l'enregistrement obligatoire et de l'exigence spéciale de date certaine par cet enregistrement pour bénéficier de la dispense de déclaration à la caisse.",
"Suppression de la déclaration obligatoire à la caisse pour les nouveaux contrats uniques et les conversions éligibles, sans engagement de durée minimale ni formalité de remplacement.",
"Suppression d'un second appel des mêmes cotisations sur les mêmes salaires lorsque le versement rétroactif inclut une période déjà financée auprès de la caisse.",
],
}

answer = []
for source in sources:
    n = source['number']
    article = {k: source[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}
    article.update(proposed_xml=proposals[n], reason=reasons[n], review_notes=reviews[n], status='rewrite_draft')
    if n in removed:
        article.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19', removed_provisions=removed[n])
    if source.get('benefit_check_required'):
        article['benefit_review'] = "L'article organise l'information et ne crée pas lui-même les avantages financiers énumérés. Sont préservés : aide à l'emploi des personnes handicapées et formation ; congés de formation rémunérés ou non et accès à l'apprentissage ; chômage partiel et intempéries indemnisé ; repos compensateurs légaux ou conventionnels, temps partiel choisi et retour à temps plein, congés annuels et jours fériés payés ; compléments de salaire de paternité, maternité et adoption et accueil de la petite enfance ; crédit d'impôt famille et ses dépenses éligibles ; participation, intéressement, actionnariat salarié et avantages en nature ; garanties maladie, décès, prévoyance et retraite complémentaire ; prestations de logement, transport, restauration, loisirs et vacances ; aides publiques, réductions d'impôts, exonérations et réductions de cotisations, crédits d'impôt et mécénat. Leur information reste au tableau, et la clause finale conserve expressément leur régime pour les situations futures éligibles et les droits antérieurs, sans nouveau critère d'accès. La dispense de l'indicateur de rémunération par coefficient protégeant la confidentialité au 2° I B d), le choix moyenne/médiane, les alternatives de catégories professionnelles, le choix d'un rapport de hiérarchie salariale, la règle de dix salariés, les options de comptage de l'absentéisme, de remplacement par les heures travaillées, de dernière période de référence et les limites de disponibilité des données environnementales sont conservés. Les nomenclatures et options salariales deviennent plus souples ; aucune option plus favorable n'est supprimée. Le retrait d'un relevé statistique ne retire ni une aide, ni un droit salarial, ni une exonération, et ne conditionne aucune demande future à un document nouveau."
    answer.append(article)
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
