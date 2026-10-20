import copy
import hashlib
import json
from html import escape
from pathlib import Path

REFERENCE_FILE_SHA256 = '2f0eda16ac4ce2688cede762a381728209dce600b72cccc749803ba6b2b448b4'
assert hashlib.sha256(Path('reference-targets.json').read_bytes()).hexdigest() == REFERENCE_FILE_SHA256
sources = json.loads(Path('source.json').read_text())
references = json.loads(Path('reference-targets.json').read_text())
answer = copy.deepcopy(json.loads(Path('previous-answer.json').read_text()))


def paragraphs(*parts):
    return '\n'.join('<p>' + escape(part, quote=False) + '</p>' for part in parts)


# Conserver les articles complets de l'essai précédent ; rectifier le champ des
# renvois après lecture des sources et des vues courantes, sans certificat repris.
a = answer[1]
a['proposed_xml'] = paragraphs(
    "Tout salarié peut demander à la commission paritaire interprofessionnelle régionale compétente la prise en charge d'un projet de transition professionnelle pendant l'exécution de son contrat de travail, quelle que soit la nature de ce contrat. Cette faculté demeure ouverte dans le contrat unique à durée indéterminée et pour les contrats antérieurs à la réforme.",
    "Par dérogation à la condition d'accord préalable prévue à l'article R. 6323-11, la demande de prise en charge peut être déposée avant la réponse de l'employeur à la demande de congé. La prise en charge ne dispense pas d'obtenir le congé prévu à l'article R. 6323-10 lorsque la formation se déroule, même en partie, sur le temps de travail. L'autorisation expresse ou tacite de ce congé suffit ; aucun second accord de l'employeur sur la prise en charge n'est requis.",
    "L'ancienneté exigible est celle du 1° du I de l'article D. 6323-9, sous réserve des dispenses et des voies spéciales applicables. Aucune durée minimale dans l'entreprise, aucune période de référence de cinq ans ni aucune condition de quatre mois de travail au cours des douze derniers mois n'est exigée pour la voie générale. Aucune des périodes mentionnées aux 1° à 5° du II de cet article n'est exclue du calcul de l'ancienneté. Celle-ci est appréciée au départ en formation, conformément au III du même article.",
    "Ces dispositions s'appliquent aux demandes en cours et aux demandes nouvelles à compter de l'entrée en vigueur de la loi instituant le contrat unique, y compris pour les périodes d'emploi antérieures. Les ouvertures de droits et décisions favorables antérieures sont conservées. Elles n'autorisent ni la conclusion ni le renouvellement d'un contrat à durée déterminée après cette date et ne subordonnent pas les droits de formation au paiement d'une contribution CPF-CDD."
)
a['reason'] = "Réforme de fond maintenue : le dossier financier peut être déposé sans attendre la réponse au congé et l'accès n'est plus réservé au CDD. Rectification nécessaire au regard de D. 6323-9 proposé dans sa vue actuelle : sa voie générale est désormais de vingt-quatre mois de salariat, sans douze mois dans l'entreprise, sans fenêtre de cinq ans ni condition de quatre mois sur douze. Le renvoi antérieur à son 2° aurait rétabli des conditions supprimées ; il est retiré. Les cinq catégories de périodes sont admises. Cette coordination n'est pas une nouvelle réduction autonome de ces seuils. L'autorisation d'absence, les dispenses et le contrôle du financement sont conservés car ils organisent le travail et protègent l'effectivité du projet."
a['review_notes'] = "D. 6323-9 officiel conserve deux voies ; sa proposition fournie abroge le 2° du I et supprime la durée locale du 1°. Le présent texte suit cette proposition sans la présenter comme le droit en vigueur : vingt-quatre mois de salariat sans fenêtre, appréciés au départ, sauf dispenses et voies spéciales. L'absence pour maladie professionnelle dans les vingt-quatre mois précédant la demande et les autres absences d'au moins six mois prévues par cette cible restent dispensatoires ; les autres dispenses légales sont réservées. R. 6323-11, lu au corpus, conserve choix territorial et interdiction des demandes simultanées ; sa seule attente de l'accord est écartée ici. R. 6323-14 conserve contrôle d'accès et de qualité, mais ne doit pas rétablir les délais ou conditions supprimés. Ces renvois complémentaires ne figurent pas parmi les cibles imposées. D. 6323-18-3 du lot détache les bases salariales de douze/quatre mois de l'ancien 2° abrogé, sans réduire une moyenne favorable ni créer de condition d'accès."
a['removed_provisions'] = [
    "Suppression de l'accord de congé comme condition préalable au dépôt de la demande de financement.",
    "Retrait coordonné de la restriction au CDD et des anciennes conditions locales et temporelles d'accès supprimées dans la proposition actuelle de D. 6323-9."
]
impact = a['substantive_impact']
impact['assessment'] = "Par rapport à la source officielle entière, le dépôt financier n'attend plus l'accord au congé et n'est plus réservé au titulaire d'un CDD. Le renvoi suit la voie générale fusionnée de D. 6323-9 proposé : vingt-quatre mois de salariat, sans ancienneté locale, sans fenêtres de cinq ans ou quatre mois sur douze et sans exclusions du II. Ces suppressions d'accès sont une coordination dédupliquée, pas de nouvelles coupes propres à cet article."
impact['scope_limitations'] = "Une formation sur temps de travail requiert encore un congé expressément ou tacitement autorisé. Les vingt-quatre mois, la date d'appréciation au départ et les conditions de financement demeurent, sous réserve des dispenses et voies spéciales. Le coût de l'accès élargi n'est pas chiffré ; la proposition cible n'est pas le droit en vigueur."
effect = impact['effects'][1]
effect.update(
    description="Le dépôt suit l'accès général fusionné proposé à D. 6323-9, sans restaurer son ancien 2°.",
    before="Le présent article vise le CDD ; la source officielle de D. 6323-9 exige vingt-quatre mois dont douze dans l'entreprise, ou vingt-quatre mois sur cinq ans dont quatre mois de CDD sur douze, avec exclusions.",
    after="Dépôt ouvert à tout salarié ; voie générale de vingt-quatre mois de salariat, sans durée locale ni fenêtre de cinq ans ou quatre mois sur douze, avec toutes les périodes admises et les dispenses maintenues.",
    affected_population="Salariés relevant de la voie générale de D. 6323-9 proposé, de ses dispenses ou d'une voie spéciale applicable.",
    proposed_quote="Aucune des périodes mentionnées aux 1° à 5° du II de cet article n'est exclue du calcul de l'ancienneté."
)

# Les montants de formation doivent rester déterminables après la fusion des
# voies d'ancienneté ; une période de calcul n'est pas un seuil d'accès.
a = answer[7]
a['proposed_xml'] = paragraphs(
    "I.-La rémunération du bénéficiaire d'un projet de transition professionnelle correspond à un pourcentage de son salaire moyen de référence, établi à partir des salaires perçus pendant la période de référence applicable.",
    "II.-Pour le salarié qui remplit les conditions d'ancienneté du 1° du I de l'article D. 6323-9, ou bénéficie d'une dispense applicable à cette voie, le salaire moyen de référence est calculé sur les salaires perçus au cours des douze mois précédant la formation, sous réserve du III.",
    "III.-Le salaire moyen de référence est également calculé sur les salaires perçus au cours des quatre derniers mois de travail précédant la formation, quelle que soit la nature des contrats correspondants. La moyenne la plus favorable entre celle du II et celle du présent III est retenue. Ces périodes de douze et quatre mois servent exclusivement au calcul du salaire ; elles ne constituent ni une durée minimale d'emploi, ni une condition supplémentaire d'accès au projet. Aucune période n'est exclue du calcul de la moyenne des quatre mois du seul fait qu'elle relève de l'une des catégories mentionnées aux 1° à 5° du II de l'article D. 6323-9.",
    "Pour le salarié qui satisfait également aux conditions de l'ancien 2° du I de l'article D. 6323-9, dans sa rédaction antérieure à la réforme, le salaire moyen de référence ne peut être inférieur à celui calculé sur les quatre derniers mois en contrat à durée déterminée, en excluant les contrats mentionnés au II du même article dans cette rédaction. Cette garantie ne subordonne pas l'accès au projet aux anciennes conditions ; elle protège uniquement un calcul plus favorable. Elle demeure applicable aux situations futures qui satisfont à ces anciennes conditions avec des périodes de CDD antérieures à la réforme.",
    "Les règles de salaire propres aux artistes et techniciens intermittents du spectacle et aux salariés des entreprises de travail temporaire prévues à l'article R. 6323-18-3-1 restent applicables dans leur champ. Les calculs du présent article ne remplacent pas ces bases spéciales.",
    "Ces règles s'appliquent aux demandes en cours et futures à compter de l'entrée en vigueur de la loi portant réforme du contrat de travail, y compris pour les périodes d'emploi antérieures. Les décisions favorables, rémunérations et créances déjà acquises sont conservées. La conversion convenue d'un contrat antérieur conserve les périodes et l'ancienneté correspondantes, sans double compte. Le calcul ne requiert ni nouveau contrat à durée déterminée ni rupture de l'emploi ; il ne limite pas la durée du contrat unique. Les données et pièces exactes et à jour déjà légalement disponibles sont réutilisées sans nouvelle attestation des mêmes salaires."
)
a['reason'] = "Coordination de fond nécessaire : le 2° du I de D. 6323-9 est abrogé dans la proposition cible actuelle ; la référence salariale de quatre mois ne peut donc plus en dépendre. Les bases de douze et quatre mois sont maintenues comme bases de calcul et non comme conditions d'entrée. L'application de la moyenne la plus favorable est explicitement étendue à la voie générale fusionnée, avec ses dispenses, pour ne fermer ni le calcul de quatre mois aux nouvelles situations ni celui de douze mois aux anciens bénéficiaires. Le plancher du calcul ancien de CDD est conservé pour les personnes qui satisfont encore à ses anciennes conditions avec leurs périodes antérieures. Aucun pourcentage de rémunération n'est modifié. Cette garantie et l'extension imposent des comparaisons supplémentaires : classification mixte, sans réduction nette de complexité alléguée. Les bases spéciales spectacle/intérim ne sont pas remplacées."
a['review_notes'] = "Renumérotation évitée : I, II et III sont conservés. Le renvoi du II vise le 1° du I actuel proposé de D. 6323-9, soit vingt-quatre mois de salariat sans durée locale ni fenêtre, avec dispenses et appréciation au départ. Le III ne renvoie plus à un 2° abrogé pour l'accès : les quatre mois sont une période salariale autonome. Le choix de la moyenne la plus favorable est une extension normative expressément assumée, pas une formule attribuée à la source ; il maintient au moins les deux calculs du brouillon précédent dans leur ancien champ. Pour le plancher CDD, seules les anciennes conditions servent au calcul favorable, jamais à refuser l'entrée désormais élargie. Les exclusions anciennes sont utilisées uniquement pour ce plancher, car les intégrer d'office pourrait abaisser la moyenne. R. 6323-18-3-1, lu dans ce lot mais hors des cibles imposées à cet article, conserve ses bases spéciales. Les taux et planchers de D. 6323-18-4, lu au corpus, restent autonomes. Les comparaisons requièrent des données historiques et ont un coût de traitement non chiffré ; aucun accès nouveau aux données n'est créé."
a['removed_provisions'] = [
    "Suppression du rattachement de la moyenne de quatre mois à une voie d'accès abrogée et à la seule nature déterminée du contrat, avec maintien des calculs favorables.",
    "Retrait des cinq exclusions de périodes pour la moyenne nouvelle de quatre mois, sans supprimer leur emploi limité au calcul ancien servant de plancher favorable."
]
a['substantive_impact'] = {
    'version': 1,
    'classification': 'mixed',
    'assessment': "La source entière rattache douze mois et quatre mois à deux voies d'ancienneté distinctes. Après fusion de l'accès dans D. 6323-9 proposé, les deux périodes salariales sont conservées et leur comparaison favorable est étendue à la voie générale, sans exiger de nouveau CDD ni quatre mois sur douze pour être admis. Le calcul ancien CDD plus favorable reste garanti dans son ancien champ. Cette extension de rémunération peut ajouter des calculs et des dépenses : aucun gain net de complexité ou de prélèvements n'est démontré.",
    'scope_limitations': "Les pourcentages de rémunération ne changent pas et les bases spéciales spectacle/intérim restent distinctes. La comparaison favorable de douze/quatre mois est une décision normative de ce texte, pas le contenu officiel de la cible. Les droits antérieurs sont protégés ; le plancher CDD ne crée aucune période de CDD fictive. Coûts de calcul et dépenses supplémentaires non chiffrés.",
    'new_burdens_review': "Des comparaisons de calcul supplémentaires sont identifiées : moyennes de douze et quatre mois puis, pour les anciens éligibles concernés, plancher CDD. Des salaires historiques peuvent être nécessaires. Aucun nouveau registre, déclaration ou attestation standard n'est créé ; le réemploi légal est prévu sans accès nouveau. Le solde net de complexité et de financement n'est pas établi.",
    'effects': [
        {
            'kind': 'coordination', 'measure_id': 'ptp-anciennete-acces-elargi',
            'description': "La base salariale ne dépend plus du 2° abrogé de la règle d'accès.",
            'before': "Le III source rattache les quatre mois de salaire au 2° de D. 6323-9, qui vise l'ancienne voie CDD.",
            'after': "Douze mois et quatre mois deviennent des périodes de calcul sans nouvelle condition d'accès dans la voie générale fusionnée.",
            'unit': 'regime',
            'affected_population': "Salariés de la voie générale de D. 6323-9 et bénéficiaires de ses dispenses, hors bases spéciales.",
            'conditions_and_transition': "Demandes en cours et futures, périodes antérieures comprises ; ancienneté et créances conservées, régimes spéciaux réservés.",
            'replacement_or_new_burdens': "La coordination exige une règle de calcul autonome ; les comparaisons supplémentaires sont recensées séparément, sans seconde suppression d'un seuil.",
            'source_quote': "Le salaire moyen de référence du salarié qui remplit les conditions d'ancienneté mentionnées au 2° de l'article D. 6323-9 est calculé",
            'proposed_quote': "Ces périodes de douze et quatre mois servent exclusivement au calcul du salaire ; elles ne constituent ni une durée minimale d'emploi, ni une condition supplémentaire d'accès au projet."
        },
        {
            'kind': 'relief_extended', 'measure_id': 'ptp-salaire-reference-plus-favorable',
            'description': "Conservation et extension du bénéfice des bases salariales les plus favorables après fusion de l'accès.",
            'before': "Moyenne de douze mois pour la première voie et moyenne des quatre derniers mois de CDD éligibles pour la seconde ; aucune comparaison générale prescrite.",
            'after': "Pour la voie générale fusionnée, moyenne la plus favorable de douze/quatre mois, sans restriction de nature du contrat ; plancher ancien CDD pour les salariés satisfaisant encore à ses conditions.",
            'unit': 'regime',
            'affected_population': "Bénéficiaires de la voie générale et de ses dispenses ; calcul CDD favorable seulement pour les anciens éligibles correspondants.",
            'conditions_and_transition': "Demandes en cours et futures à l'entrée en vigueur ; décisions favorables et créances déjà acquises conservées.",
            'replacement_or_new_burdens': "Comparaison de calcul et besoin possible de salaires historiques, sans taux nouveau ni dépôt distinct ; dépense supplémentaire éventuelle non chiffrée.",
            'source_quote': "sur la base des salaires perçus au cours des quatre derniers mois en contrat de travail à durée déterminée, à l'exclusion des contrats mentionnés au II de l'article D. 6323-9.",
            'proposed_quote': "La moyenne la plus favorable entre celle du II et celle du présent III est retenue."
        },
        {
            'kind': 'complexity_added', 'measure_id': 'ptp-salaire-reference-plus-favorable',
            'description': "Comparaisons supplémentaires rendues explicites pour protéger les moyennes favorables.",
            'before': "Calcul attaché à chaque ancienne voie sans prescription générale de comparaison des moyennes.",
            'after': "Comparaison de douze et quatre mois puis, lorsque ses anciennes conditions sont remplies, du plancher ancien de quatre mois de CDD éligibles.",
            'unit': 'regime',
            'affected_population': "Commissions régionales calculant la rémunération des bénéficiaires de la voie générale fusionnée.",
            'conditions_and_transition': "Demandes en cours et nouvelles ; pas de recherche de CDD inexistant et bases spéciales non remplacées.",
            'replacement_or_new_burdens': "Calculs et données salariales supplémentaires possibles ; réemploi sans nouvelle attestation standard ; coût net inconnu.",
            'source_quote': "Le salaire moyen de référence du salarié qui remplit les conditions d'ancienneté mentionnées au 1° de l'article D. 6323-9 est calculé sur la base des salaires perçus au cours des douze mois précédant la formation.",
            'proposed_quote': "Pour le salarié qui satisfait également aux conditions de l'ancien 2° du I de l'article D. 6323-9, dans sa rédaction antérieure à la réforme, le salaire moyen de référence ne peut être inférieur à celui calculé sur les quatre derniers mois en contrat à durée déterminée, en excluant les contrats mentionnés au II du même article dans cette rédaction."
        }
    ]
}

# Le renvoi spécial n'ajoute ni les 220 jours/cachets supprimés ni les 600 heures
# d'entreprise retirées par la nouvelle vue de R. 6323-9-1.
answer[2]['review_notes'] = answer[2]['review_notes'].replace(
    "Sa proposition actuelle retire les 600 heures dans l'entreprise mais conserve les 1 600 heures de branche sur dix-huit mois et les intermissions.",
    "Sa proposition actuelle retire le seuil cumulatif de 220 jours ou cachets et les 600 heures dans l'entreprise ou le groupe ; elle conserve les seuils propres aux trois activités du spectacle, les 1 600 heures de branche sur dix-huit mois et les intermissions du CDI."
)
answer[6]['review_notes'] = answer[6]['review_notes'].replace(
    "La proposition actuelle de R. 6323-9-1 retire les 600 heures d'entreprise : ce seuil n'est pas réintroduit ici.",
    "La proposition actuelle de R. 6323-9-1 retire les 600 heures d'entreprise ou de groupe et le seuil cumulatif de 220 jours ou cachets du spectacle : ni le II ni le I ne les réintroduisent. Restent les seuils spectacle 130/65, 88/44, 60/30 dans leurs unités propres et les 1 600 heures de branche sur dix-huit mois, appréciés au départ avec les intermissions du CDI."
)
answer[8]['review_notes'] += " La vue actuelle de R. 6323-9-1 retire aussi les 220 jours ou cachets cumulatifs du spectacle : le I du présent article vise uniquement ses 1°, 2° et 3° pour les périodes salariales et ne rétablit pas ce seuil. Ses fenêtres et seuils professionnels demeurent, comme la voie générale et les dispenses réservées par la cible."

# Lever l'ambiguïté de 'cette période' : la coupe déjà décidée autorise aussi le
# dépôt pendant l'exécution de la reconversion, sans changer le délai de décision.
answer[9]['proposed_xml'] = answer[9]['proposed_xml'].replace(
    "Il peut intervenir avant ou pendant cette période.",
    "La demande peut être déposée avant le début de la période de reconversion ou pendant son exécution."
)

# Les analyses optionnelles restent dans review_notes, jamais dans la liste
# exacte des cibles imposées à chaque article.
answer[4]['review_notes'] += " Analyse facultative de R. 6323-14-1 : la vue fournie conserve encore six mois pour commencer après la fin effective ; l'article complet du présent lot retire ce délai en coordination avec R. 6323-11-2. Son statut de stagiaire et ses garanties demeurent. Cette cible n'étant pas requise pour R. 6323-14-3, elle ne figure pas dans ses reference_checks."

answer[5]['proposed_xml'] = answer[5]['proposed_xml'].replace(
    "Cette règle vaut après un contrat à durée déterminée conclu avant la réforme comme après un contrat unique à durée indéterminée, sans fermeture du droit aux situations éligibles futures.",
    "Cette règle vaut après tout contrat antérieur à la réforme, notamment à durée déterminée, comme après un contrat unique à durée indéterminée, sans fermeture du droit aux situations éligibles futures."
)
answer[5]['substantive_impact']['effects'][0]['proposed_quote'] = "Cette règle vaut après tout contrat antérieur à la réforme, notamment à durée déterminée, comme après un contrat unique à durée indéterminée, sans fermeture du droit aux situations éligibles futures."
answer[5]['review_notes'] += " La mention de tout contrat antérieur couvre aussi les anciens CDI admis par R. 6323-11-1 dans le présent lot ; elle évite que l'exemple des anciens CDD soit lu comme une exclusion."

answer[6]['review_notes'] += " Le I et le II décrivent les modalités spéciales attachées à leurs conditions professionnelles respectives ; ils ne ferment pas l'accès général ou les dispenses réservés par R. 6323-9-1 proposé. Lorsqu'un salarié n'entre pas dans ce champ spécial mais est admis par la voie générale, les circuits généraux et les règles salariales de D. 6323-18-1 à D. 6323-18-4 demeurent à leur champ, sans lui opposer les seuils spéciaux comme condition générale d'accès."
answer[8]['review_notes'] += " Le II salarial spécial continue de viser les salariés relevant du II de R. 6323-9-1, sous les dispenses applicables ; il ne transforme pas ce seuil spécial en condition d'accès à la voie générale. Les bénéficiaires admis hors de ce champ spécial restent régis par les bases générales de D. 6323-18-3, sans cumul de deux salaires de référence."

answer[11]['review_notes'] += " Point de coordination de la cible actuelle : la formule « engagées au début d'un contrat unique » de L. 6325-13 proposé ajoute une borne qui n'apparaît pas dans son premier alinéa officiel pour les actions dans un CDI. Cette restriction potentielle doit être réexaminée dans l'article législatif lui-même afin de ne pas fermer des phases futures recevables ; son fichier n'est pas modifié ici et son traitement n'est pas déclaré achevé. L'abrogation du seul D. 6325-12 ne crée pas cette borne et ne la résout pas."
answer[11]['substantive_impact']['scope_limitations'] += " La proposition cible de L. 6325-13 contient en outre une borne « au début » du contrat unique, absente de son alinéa officiel sur le CDI ; cette coordination favorable reste à régler dans la cible, sans être attribuée à la présente abrogation."

checks = {}

checks['R6323-10'] = {
    'L1234-1': "Les 120/60 jours du I officiel sont des prévenances de congé, non les préavis de licenciement. La vue proposée de L. 1234-1 maintient les durées des anciens contrats selon six mois/deux ans et prévoit quinze jours calendaires pour les nouveaux, y compris un préavis payé si la faute grave empêche son exécution. Aucun de ces préavis ne remplace la réponse au congé sous trente jours ; la notification de rupture reste distincte.",
    'L1251-2': "Le destinataire du dernier alinéa est bien l'entrepreneur de travail temporaire qui recrute et rémunère, et non l'entreprise utilisatrice. La cible officielle définit cette activité ; sa proposition impose le contrat unique aux nouveaux recrutements et réserve rémunération et intermissions. Le congé lui est donc demandé sans créer de nouveau contrat de mission ; la formation n'est pas une notification de rupture.",
    'L1221-2': "La proposition de L. 1221-2 interdit un terme d'emploi nouveau fixé par une formation, une mission ou un chantier. La durée indiquée dans la demande de congé identifie seulement l'absence et la formation ; elle ne peut terminer le contrat unique. La transition conserve les contrats antérieurs et interdit les nouveaux CDD ou renouvellements après la réforme.",
    'L1234-9': "L'ancienneté du IV concerne l'accès au congé, pas l'indemnité de rupture. L. 1234-9 proposé mesure l'année au terme effectif, préavis inclus, puis compte toute l'ancienneté à 0,20 mois par année, fractions en mois complets, plafond de six mois et exception de faute grave. Les anciennes composantes, droits plus favorables et indemnités spéciales sont réservés ; aucun de ces seuils ne conditionne la demande de congé."
}

checks['R6323-11-1'] = {
    'L1234-1': "Le dépôt financier anticipé concerne l'attente d'un congé, sans notification de rupture. Les quinze jours calendaires de L. 1234-1 proposé ne sont ni une durée d'ancienneté ni un délai d'instruction de ce dossier ; les anciens préavis restent au régime antérieur. Le salarié doit encore obtenir l'autorisation expresse ou tacite d'absence, distincte des procédures de rupture collective ou protégée.",
    'L1221-2': "L. 1221-2 officiel admet encore des CDD dérogatoires ; sa proposition les exclut pour les nouveaux emplois. R. 6323-11-1 est donc ouvert à tout salarié et non plus au seul CDD, tout en conservant les demandes des anciens contrats. Le dépôt de financement et la durée de formation ne permettent aucun nouveau terme ni renouvellement de CDD.",
    'L1234-9': "Le 1° du I de D. 6323-9 proposé fixe l'accès général à la formation ; il ne doit pas être remplacé par l'année d'ouverture de L. 1234-9. Cette dernière s'apprécie au terme effectif avec préavis inclus pour la rupture patronale ordinaire, puis 0,20 mois par année totale, prorata de mois complets et six mois au plus dans son champ. Le dossier de formation ne crée ni cette créance ni une renonciation aux droits antérieurs ou spéciaux.",
    'R6323-10': "La vue fournie de R. 6323-10 supprime les prévenances de 120/60 jours mais maintient écrit, réponse sous trente jours, accord tacite et refus motivé. Le présent lot y retire aussi les mentions distinctes d'examen. R. 6323-11-1 permet seulement le dépôt financier avant cette réponse ; aucune absence d'office ne résulte du dépôt. Ni délai supprimé ni seconde autorisation financière patronale ne doit être rétabli.",
    'D6323-9': "La source officielle distingue vingt-quatre mois dont douze dans l'entreprise et vingt-quatre mois sur cinq ans dont quatre mois de CDD sur douze, avec cinq exclusions. La vue actuelle fournie fusionne l'accès au 1° du I : vingt-quatre mois de salariat sans durée locale ni fenêtre ; son 2° est abrogé et toutes les périodes du II sont admises. Le troisième alinéa est donc rectifié pour ne plus viser quatre mois ni les anciennes fenêtres. Le III maintient l'appréciation au départ ; dispenses, voies spéciales et droits favorables antérieurs restent ouverts."
}

checks['R6323-11-2'] = {
    'L1234-1': "Les quatre mois de dépôt et six mois de début de formation sont des limites postérieures au terme, distinctes du préavis. Leur suppression ne rompt pas un contrat qui continue après une mission. Si l'employeur rompt réellement un contrat nouveau, le préavis de quinze jours calendaires et sa notification restent nécessaires ; les anciens contrats gardent leurs préavis, et les procédures collectives restent autonomes.",
    'L1221-2': "L. 1221-2 proposé permet qu'une mission soit limitée sans que l'emploi indéterminé le soit. La demande après dernière mission peut donc être reçue pendant un emploi maintenu, avec le congé requis sur temps de travail ; elle ne présume aucune rupture. Les périodes des contrats antérieurs restent prises en compte sans autoriser un nouveau CDD.",
    'L1234-9': "La fin de mission ou la présentation d'un projet n'ouvre pas l'indemnité ordinaire. Dans L. 1234-9 proposé, la rupture patronale doit atteindre un an au terme effectif, préavis inclus, avec l'exception de faute grave ; le calcul compte alors toute l'ancienneté à 0,20 mois, fractions en mois complets et plafond de six mois. Les quatre/six mois supprimés ici ne changent ni ce régime ni ses anciennes composantes et garanties spéciales.",
    'R6323-9-1': "Lecture de la vue actuelle entière : le I proposé retire aussi les 220 jours ou cachets cumulatifs, en conservant pour le spectacle enregistré 130/65 jours, le vivant 88/44 jours, et l'artiste 60/30 jours ou cachets, selon vingt-quatre/douze mois. Le II garde 1 600 heures de branche sur dix-huit mois et les intermissions du CDI, mais retire les 600 heures d'entreprise/groupe. Le III apprécie l'ancienneté au départ. Le renvoi n'en rétablit aucun seuil retiré ; supprimer quatre/six mois ne supprime pas les fenêtres professionnelles restantes, la voie générale ni les dispenses réservées par la cible."
}

checks['R6323-14-1'] = {
    'L1234-1': "La fin effective qui ouvre le financement post-emploi ne résulte pas du seul début d'une formation. Les anciens préavis de L. 1234-1 restent réservés ; le contrat nouveau bénéficie des quinze jours calendaires, avec notification distincte et protections de rupture maintenues. La suppression de la limite de six mois pour commencer le projet ne raccourcit pas ce préavis ni les procédures collectives.",
    'L1221-2': "La proposition de L. 1221-2 exclut le terme automatique d'un emploi nouveau à la fin d'une mission ou formation. Le I vise par conséquent la fin effective du contrat, et le II ne fait pas du statut de stagiaire une rupture. Les droits de rémunération et de protection sociale restent ouverts après les anciens contrats et les futurs contrats uniques éligibles.",
    'L1234-9': "Le statut de stagiaire, sa rémunération et les trois garanties sociales du II ne constituent pas l'indemnité ordinaire de L. 1234-9. L'année d'ancienneté au terme effectif, préavis inclus, puis les 0,20 mois sur l'ancienneté totale avec mois complets et plafond de six mois ne permettent d'en retrancher aucun versement. La rupture à l'initiative du salarié ne reçoit pas cette indemnité ordinaire ; droits anciens et spéciaux restent distincts du financement du projet.",
    'R6323-11-1': "La vue fournie de R. 6323-11-1 ouvre le contrat unique et le dépôt avant réponse au congé, mais son troisième alinéa maintient encore une voie de quatre mois et des exclusions devenues incompatibles avec D. 6323-9 actuel proposé. Le présent lot le rectifie vers la voie générale de vingt-quatre mois sans ces conditions. Le renvoi du I suit donc toutes les situations éligibles, pas les seuls anciens CDD, en maintenant l'autorisation d'absence quand l'emploi continue et sans transformer une mission en terme d'emploi."
}

checks['R6323-14-3'] = {
    'L1234-1': "Le mois suivant la fin du préavis au 2° du II officiel imposait un réemploi pour garder le financement. Sa suppression ne modifie pas les anciens préavis ni les quinze jours calendaires du contrat nouveau prévus par L. 1234-1 proposé. La décision de rupture doit rester datable, sans confondre cette preuve avec le justificatif spécial retiré ; les notifications et procédures collectives restent applicables.",
    'L1221-2': "Le financement ne dépend plus d'un nouveau contrat après le départ du bénéficiaire. S'il retrouve un emploi nouveau, L. 1221-2 proposé impose sa durée indéterminée ; une formation suivie sur ce temps de travail requiert le congé. La poursuite du projet ne crée ni CDD de remplacement ni rupture automatique de cet emploi, et les contrats antérieurs gardent leurs droits.",
    'L1234-9': "Le maintien des cinq postes financés après départ volontaire ne vaut pas indemnité patronale ordinaire. L. 1234-9 proposé exclut cette indemnité à l'initiative du salarié, puis prévoit dans son champ patronal un an au terme effectif avec préavis et 0,20 mois sur l'ancienneté totale, fractions de mois complets, plafond de six mois. Ces paramètres ne réduisent ni les frais, ni la rémunération, ni les cotisations du I ; garanties spéciales et anciennes restent distinctes.",
    'R6323-10': "Le congé chez un nouvel employeur reste soumis au circuit de R. 6323-10 : écrit, réponse sous trente jours, accord tacite à défaut et refus motivé selon les conditions restantes. La vue fournie retire les 120/60 jours et le présent lot retire les mentions distinctes d'examen. Le II de R. 6323-14-3 réserve cette autorisation à l'absence sur temps de travail : elle n'est plus une condition patronale de maintien financier ou de réemploi."
}

checks['D6323-18-2'] = {
    'L1234-1': "Le circuit de versement post-emploi ne fixe pas la date de rupture. Le préavis nouveau de quinze jours calendaires de L. 1234-1 proposé suppose sa notification ; les anciens préavis subsistent dans leur champ. Un salarié encore employé pendant le préavis ou une intermission ne bascule donc pas vers le versement post-emploi pour la seule fin de sa mission.",
    'L1221-2': "La référence officielle au terme du CDD ne couvre plus les nouveaux contrats indéterminés imposés par L. 1221-2 proposé. Elle est remplacée par une fin effective d'emploi, en préservant les anciens CDD et les droits futurs du contrat unique. La seule fin de mission ou de formation n'ouvre pas ce circuit si le contrat continue.",
    'L1234-9': "Le paiement dû ici est une rémunération de formation versée par la commission. Ce n'est pas l'indemnité de L. 1234-9 : son année au terme effectif avec préavis inclus, ses 0,20 mois par année totale avec mois complets et son plafond de six mois ne peuvent en réduire le montant ou changer le payeur. Les anciennes composantes et indemnités spéciales sont également sans incidence sur ce circuit.",
    'R6323-14-1': "Le renvoi vise la prise en charge après fin effective du I et la rémunération avec garanties du II de R. 6323-14-1. La vue fournie garde une limite de début de six mois ; le présent lot la retire expressément pour les demandes en cours et futures sans réouverture des décisions définitives. D. 6323-18-2 ne peut la réintroduire par renvoi et maintient le même payeur, sans double rémunération pendant un emploi poursuivi.",
    'R6323-18-2-1': "La vue fournie distingue versement mensuel direct au spectacle au I et rémunération patronale remboursée pour l'intérim des II/III, avec avances du IV pour moins de cinquante salariés plafonnées à 90 %. Le présent lot retire en plus la copie intégrale de paie et la facture distincte. Ce circuit pendant l'emploi reste distinct du versement après cessation effective ; une simple lettre de formation ou fin de mission n'y substitue pas D. 6323-18-2."
}

checks['R6323-18-2-1'] = {
    'L1234-1': "L'affectation pédagogique par lettre au II ne notifie pas une rupture de contrat. Les quinze jours calendaires proposés par L. 1234-1 pour les nouveaux emplois et les anciens préavis demeurent distincts du mois de remboursement du III et des trente jours d'avance du IV. La fin de formation ne dispense ni de notification ni des procédures collectives ou protégées applicables.",
    'L1221-2': "La création obligatoire d'un contrat de mission à terme pour une nouvelle formation contredirait L. 1221-2 proposé. Le II prévoit donc une lettre d'affectation dans l'emploi indéterminé, sans nouvel essai ni terme. La transition conserve les contrats de mission déjà valables et leurs droits jusqu'au terme, sans autoriser un nouveau CDD ou renouvellement après la réforme.",
    'L1234-9': "Les rémunérations, remboursements et avances ne sont pas des indemnités ordinaires de rupture. L. 1234-9 proposé exige, sauf exception de faute grave, un an à la fin effective avec préavis inclus, puis calcule 0,20 mois sur toute l'ancienneté, fractions de mois complets et plafond de six mois. Cette règle ne plafonne aucun financement du présent article ; la lettre de formation ne remet pas l'ancienneté à zéro et ne retranche pas les anciennes composantes ni garanties spéciales.",
    'L1251-58-1': "La cible confirme au 2° la lettre de mission et au 1° le contrat de mise à disposition avec l'utilisateur. La source écrivait « L. 125158-1 » : le numéro est expressément rectifié. La proposition cible généralise le CDI nouveau et conserve ancienneté et garanties des CDI antérieurs. La lettre pédagogique n'exige pas un nouveau terme ni un contrat commercial fictif avec un utilisateur lorsque le salarié est en formation.",
    'L1251-57': "Cette cible assimile aux missions les stages, bilans, VAE et formations liées à l'activité prévues par accord ; elle ne commande pas un CDD de formation. Sa proposition maintient ces assimilations dans le contrat unique et les contrats antérieurs. Le II conserve ce champ pédagogique dans une lettre d'affectation, sans faire de la durée de formation un terme d'emploi ou une nouvelle période d'essai.",
    'R6323-9-1': "Le renvoi officiel au III pour l'ancienneté intérimaire est inexact : le II contient les heures, le III leur date d'appréciation au départ. La rectification vers le II est explicite. Dans la vue actuelle, 1 600 heures de branche sur dix-huit mois et intermissions du CDI subsistent, mais les 600 heures d'entreprise/groupe disparaissent. Au I spectacle, les 220 jours ou cachets cumulatifs disparaissent également, sans effacer les seuils 130/65, 88/44 et 60/30 dans leurs unités et fenêtres. Aucun de ces deux seuils retirés n'est rétabli par les renvois du I ou du II ; voies générales et dispenses restent réservées."
}

checks['D6323-18-3'] = {
    'L1234-1': "Les douze et quatre mois de ce texte sont des périodes salariales, et non un préavis ou une notification de rupture. Le salarié peut se former sans rupture de l'emploi ; lorsqu'une rupture intervient, les préavis anciens ou les quinze jours calendaires du nouvel emploi prévus par L. 1234-1 proposé restent applicables. La comparaison favorable n'abrège aucune procédure collective ni autorisation de rupture.",
    'L1221-2': "L. 1221-2 proposé ne permet plus de nouveaux mois de CDD. La période salariale de quatre mois est donc ouverte à tous contrats et détachée du terme d'emploi, tout en protégeant le calcul ancien de CDD lorsqu'il demeure favorable avec des périodes antérieures. Le contrat unique continue après la formation ; la conversion conserve les périodes acquises sans double compte.",
    'L1234-9': "Le salaire moyen de formation de D. 6323-18-3 ne se confond pas avec le salaire de référence de l'indemnité de L. 1234-9. Le seuil d'un an au terme effectif préavis inclus, le taux de 0,20 mois sur l'ancienneté totale, le prorata des mois complets et le plafond de six mois restent propres à la rupture patronale ordinaire. Ils ne conditionnent pas les bases de douze/quatre mois, ni leurs garanties favorables ou les rémunérations déjà acquises.",
    'R6323-11-1': "La vue fournie permet le dépôt pendant le contrat unique et avant la réponse au congé, mais rattache encore quatre mois au 2° du I de D. 6323-9 avec des exclusions. Le présent lot rectifie cet accès vers le seul 1° général actuel proposé. D. 6323-18-3 conserve donc quatre mois comme base de salaire autonome, sans rétablir par ce renvoi les quatre mois sur douze ni une attente d'accord financier patronal ; le congé d'absence reste distinct.",
    'D6323-9': "La vue actuelle abroge le 2° du I et ses quatre mois sur douze/cinq ans, retire les douze mois dans l'entreprise du 1° et admet toutes les périodes du II. Le III garde l'appréciation au départ, avec dispenses et voies spéciales réservées. Le salaire de quatre mois ne peut donc rester attaché au 2° comme condition d'accès. La nouvelle comparaison favorable douze/quatre mois conserve les deux bases salariales ; son extension est une réforme explicitée dans cet article, non une formule contenue dans la cible. Les anciennes conditions ne servent qu'au plancher CDD favorable, jamais à refermer l'accès fusionné."
}

checks['R6323-18-3-1'] = {
    'L1234-1': "Les 600 heures du II constituent une base salariale de formation ; elles n'indiquent aucun préavis. La proposition de L. 1234-1 réserve quinze jours calendaires au nouvel emploi après notification et maintient les anciens préavis dans leur champ. La fin d'une mission ou l'application du calcul subsidiaire ne rompt donc pas l'emploi ni ne dispense des procédures distinctes.",
    'L1221-2': "Les missions peuvent être temporaires dans le contrat indéterminé prévu par L. 1221-2 proposé. La référence aux heures de mission reste utilisable sans exiger un terme de contrat ; le calcul sans 600 heures chez l'entreprise dépositaire ouvre les situations futures admissibles. Les intermissions gardent leur rôle d'ancienneté sans devenir des heures de mission et les droits des contrats antérieurs restent protégés.",
    'L1234-9': "Le calcul subsidiaire de salaire ne crée aucune indemnité ordinaire de rupture. Le régime de L. 1234-9 proposé requiert dans son champ patronal un an au terme effectif avec préavis, puis 0,20 mois par année totale, fractions en mois complets et six mois au plus, sous ses exceptions. Aucun de ces paramètres ne réduit la rémunération minimale de formation ni les garanties intérimaires, les anciennes composantes ou les indemnités spéciales.",
    'R6323-9-1': "La vue actuelle supprime au I les 220 jours ou cachets cumulatifs, tout en gardant les seuils professionnels 130/65, 88/44 et 60/30 sur vingt-quatre/douze mois. Le I salarial ne doit pas réintroduire le seuil supprimé. Au II, seuls les 1 600 heures de branche sur dix-huit mois subsistent pour l'accès, avec intermissions du CDI et date du départ au III ; les 600 heures d'entreprise/groupe sont retirées. Les 600 heures du présent article restent une base de salaire : à défaut chez l'entreprise, calcul dans la branche, sur les heures disponibles, puis garantie mensuelle sans mission, sans nouveau seuil d'accès. Les règles générales et dispenses que réserve la cible ne sont pas fermées par ce calcul."
}

checks['R6324-1'] = {
    'L1234-1': "La fenêtre de trente jours de la source concerne le dépôt de reconversion, pas la rupture. Sa suppression ne dispense pas de la notification ni du préavis si le contrat d'origine ou d'accueil est ensuite rompu. Les quinze jours calendaires du nouveau contrat proposés par L. 1234-1 et les anciens préavis restent distincts des vingt jours de décision de l'opérateur et des procédures collectives ou protégées.",
    'L1221-2': "Le dépôt systématique du contrat d'accueil complet est retiré, sans retirer l'obligation de conclure un emploi régulier. Pour les recrutements nouveaux, L. 1221-2 proposé impose le contrat indéterminé : la durée de la reconversion et la suspension de l'emploi d'origine ne peuvent en constituer le terme. Les contrats antérieurs restent dans leur transition ; aucune nouvelle voie de CDD ne résulte du 3° abrogé.",
    'L1234-9': "La suspension pour reconversion et le retour anticipé ne constituent pas à eux seuls une rupture patronale indemnisable. L. 1234-9 proposé fixe pour cette dernière le seuil d'un an au terme effectif avec préavis inclus, puis 0,20 mois sur l'ancienneté totale, fractions de mois complets et plafond de six mois. Ces paramètres ne limitent pas les rémunérations et financements de reconversion ni les anciennes composantes et indemnités spéciales.",
    'L6324-3': "Au I, l'accord écrit protège durée d'organisation, maintien du contrat et rémunération inchangée ; au II, il fixe suspension et retour anticipé. La source admet un CDD d'au moins six mois avec essai ; la proposition fournie impose pour le nouveau recrutement le contrat unique et un essai seulement expressément stipulé selon le régime commun. Les pièces de R. 6324-1 ne peuvent rétablir CDD, minimum de six mois d'emploi ou essai obligatoire. Le dépôt peut réunir les contenus sans annexe séparée et le contrat complet n'est plus transmis systématiquement, sans enlever les consentements. La note législative maintient l'ancienne rédaction pour avenants d'avant le 1er janvier 2026 ; la note réglementaire ambiguë ne la remplace pas."
}

checks['R6324-4'] = {
    'L1234-1': "L'abrogation retire une transmission ministérielle, sans toucher à une notification de rupture. Les quinze jours calendaires du contrat nouveau et les anciens préavis de L. 1234-1 proposé restent applicables si une rupture intervient. La motivation et la notification du refus de financement aux parties, réservées par R. 6324-3, relèvent encore d'une autre procédure et ne sont pas supprimées.",
    'L1221-2': "Supprimer le dépôt central ne supprime pas la forme indéterminée des nouveaux emplois prévue par L. 1221-2 proposé. L'accord de reconversion reste valable sans dépôt ministériel et ne peut fixer un terme à l'emploi d'accueil. Les anciens contrats et droits sont conservés ; l'abrogation documentaire ne rétablit aucun CDD, renouvellement ou rupture automatique en fin de reconversion.",
    'L1234-9': "Aucun élément de l'indemnité de L. 1234-9 n'est abrogé avec ce dépôt. Sa proposition limite l'indemnité ordinaire à l'initiative patronale, à partir d'un an au terme effectif préavis inclus, puis 0,20 mois sur l'ancienneté totale avec mois complets et plafond de six mois dans son champ. Les anciennes composantes et garanties spéciales, comme la rémunération de reconversion, demeurent indépendantes de la transmission ministérielle supprimée.",
    'L6324-3': "La cible officielle et sa proposition maintiennent l'accord écrit interne et les garanties de suspension et de retour externe. Seul le dépôt et le circuit de refus institués par R. 6324-4 sont abrogés ; l'accord n'est ni annulé ni dispensé. La proposition cible exige le contrat unique d'accueil et réserve un essai expressément stipulé, sans CDD nouveau. Les anciens avenants, notamment ceux d'avant le 1er janvier 2026 selon la note législative, gardent leurs droits mais n'exigent aucun futur dépôt de rattrapage sur le fondement supprimé."
}

checks['D6325-12'] = {
    'L1234-1': "L'échéance d'une convention pédagogique n'est pas une notification de licenciement. L'abrogation du fondement spécial de signature laisse donc intacts les préavis de L. 1234-1 proposé : quinze jours calendaires pour le contrat nouveau et règles antérieures pour les anciens. Les procédures collectives et protections de rupture ne sont pas remplacées par l'achèvement d'une formation.",
    'L1221-2': "La convention générale de formation maintenue peut organiser une phase limitée, sans fixer le terme de l'emploi nouveau indéterminé imposé par L. 1221-2 proposé. L'abrogation de D. 6325-12 ne rouvre aucun CDD de professionnalisation. Les anciens contrats restent dans leur transition et les aides ou exonérations demeurent ouvertes aux nouvelles situations éligibles dans le contrat unique.",
    'L6325-13': "La cible conserve positionnement, évaluation, accompagnement et enseignements, par organisme ou service interne. Sa proposition rapporte les 15 % à 25 % et le minimum de 150 heures à la phase de professionnalisation, non à l'emploi, et réserve les anciens contrats. Elle vise aussi les actions « au début » du contrat unique, borne absente de l'alinéa officiel pour le CDI : cette restriction potentielle est signalée pour coordination dans la cible, non validée ni corrigée par cette abrogation réglementaire. Retirer D. 6325-12 n'abolit ni les prestations ni leurs durées ; la convention générale L. 6353-1 subsiste dans son champ sans signature de remplacement.",
    'L1234-9': "Les prestations et financements maintenus ne sont pas l'indemnité patronale ordinaire de L. 1234-9 proposé. Le zéro avant un an, le seuil à la fin effective avec préavis inclus, puis 0,20 mois sur toute l'ancienneté avec prorata des mois complets et plafond de six mois ne réduisent aucune rémunération de formation. L'abrogation laisse aussi les anciennes composantes, congés, réparations d'illégalité et indemnités spéciales à leurs régimes."
}

for source, article in zip(sources, answer):
    for name in ('code_id', 'source_id', 'source_sha256', 'number'):
        assert source[name] == article[name]
    key = source['code_id'] + '|' + source['source_id']
    required_keys = references['requirements'][key]
    required_numbers = {references['targets'][target]['number'] for target in required_keys}
    assert set(checks[source['number']]) == required_numbers
    article['reference_checks'] = [
        {
            'target_key': target,
            'view_sha256': references['targets'][target]['view_sha256'],
            'assessment': checks[source['number']][references['targets'][target]['number']]
        }
        for target in required_keys
    ]
    assert all(len(check['assessment']) >= 80 for check in article['reference_checks'])

assert hashlib.sha256(Path('reference-targets.json').read_bytes()).hexdigest() == REFERENCE_FILE_SHA256
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles ; références issues de la vue locale courante.')
