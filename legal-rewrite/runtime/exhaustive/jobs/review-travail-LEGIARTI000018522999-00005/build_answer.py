import json
import re
from html import unescape
from html.parser import HTMLParser
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
references = json.loads(Path('reference-targets.json').read_text())
by_number = {a['number']: a for a in sources}

def plain(xml):
    class Text(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=True)
            self.parts = []
        def handle_data(self, data):
            self.parts.append(data)
    p = Text()
    p.feed(xml)
    return ''.join(p.parts)

def paragraphs(*texts):
    return '\n'.join('<p>' + t + '</p>' for t in texts)

answers = {}
for s in sources:
    a = {k: s[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    a.update({k: s['previous_draft'][k] for k in ('proposed_xml', 'reason', 'review_notes')})
    a['status'] = 'rewrite_draft'
    answers[s['number']] = a

a = answers['D6325-14']
a['reason'] = "Coordination de fond déjà acquise, conservée après comparaison avec toute la source : le salaire minimum des moins de vingt-six ans demeure dû pendant l'action de professionnalisation, désormais portée par le contrat unique sans terme de l'emploi. Aucune coupe supplémentaire du minimum salarial ne se justifie : sa fonction est de protéger la rémunération d'un salarié en formation, sans déclaration, agrément, contribution accessoire ou délai minimal à retirer dans cet article. Les références au CDD ne subsistent que pour les contrats antérieurs."
a['review_notes'] = "L'âge inférieur à vingt-six ans et les deux critères d'âge et de niveau de formation sont conservés. D. 6325-15, D. 6325-16 et D. 6325-17, consultés en entier dans le corpus public, fixent séparément les 55/70 %, 65/80 %, le changement de tranche au premier jour du mois suivant l'anniversaire et les limites de déduction des avantages en nature : aucun de ces paramètres n'est modifié ici. L. 6325-8, également consulté, préserve les stipulations plus favorables et doit rester coordonné sur la seule durée de l'action nouvelle. Ces consultations facultatives ne sont pas ajoutées à reference_checks. Le salaire de droit commun reprend son champ à la fin de l'action ; ni l'emploi ni son ancienneté ne s'interrompent. Les règles de préavis et d'indemnité ordinaire ne conditionnent pas ce salaire."

a = answers['D6325-18']
a['proposed_xml'] = None
a['status'] = 'retained_unchanged'
a['reason'] = "Maintien intégral nécessaire après examen de la source et du brouillon : le plancher de 85 % du minimum de branche protège les salariés âgés d'au moins vingt-six ans, avec le SMIC imposé cumulativement par L. 6325-9. L'article ne contient ni CDD à supprimer ni durée autonome de l'emploi, ni dépôt, agrément, contribution accessoire ou pièce redondante. Son renvoi à L. 6325-9 reste cohérent avec l'action de professionnalisation du contrat unique. Réécrire ce seul plancher ajouterait des mots sans alléger une charge détachable de la protection salariale."
a['review_notes'] = "Le seuil est au moins vingt-six ans et le pourcentage est 85 % du minimum de la convention ou de l'accord collectif de branche de l'entreprise, jamais 85 % du SMIC. La source entière est reproduisible sans modification. La proposition fournie de L. 6325-9 conserve le SMIC, les contrats antérieurs et les phases futures du contrat unique ; elle est un projet, non le droit en vigueur. Le brouillon antérieur explicitait ces règles sans coupe démontrée : il est remplacé par ce maintien motivé. Aucun gain de simplification ni réécriture n'est compté pour cet article."

a = answers['D6331-72']
a.update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19',
         repeal_scope="Liste réglementaire des exclusions du CPF-CDD rendue sans objet pour les périodes d'emploi nouvelles par l'abolition intégrale de cette contribution ; exclusions et recours anciens sauvegardés.")
a['proposed_xml'] = a['proposed_xml'].replace("de la loi portant suppression de la contribution spécifique prévue à l'article L. 6331-6", "de la réforme du contrat unique supprimant la contribution spécifique prévue à l'article L. 6331-6")
a['reason'] = "Abrogation prospective de coordination, déjà acquise dans le brouillon : la liste d'exclusions ne disparaît pour les rémunérations des périodes futures que parce que la contribution CPF-CDD de 1 % disparaît intégralement, sans équivalent. Les 1°, 2°, 3° et 6° demeurent applicables aux périodes anciennes ; les 4° et 5° ne revivent pas. Aucune coupe supplémentaire ne doit enlever une exonération ancienne ou un droit futur à la formation. Ce règlement d'exonération ne supprime pas une deuxième taxe."
a['review_notes'] += " La proposition de L. 6331-6 fournie dans reference-targets.json retient précisément les périodes de travail, y compris sous un ancien CDD, et non la date de versement du salaire. Cette concordance doit être conservée dans la loi et le règlement ; aucune assiette distincte n'est créée ici."

a = answers['R6332-25']
a['proposed_xml'] = a['proposed_xml'].replace(
    "L'absence de transmission dans les quatre mois suivant la fin du contrat ou de la période d'apprentissage n'emporte plus déchéance du solde.",
    "Aucun délai de transmission de quatre mois suivant la fin du contrat ou de la période d'apprentissage ne conditionne le paiement du solde. Les prescriptions de droit commun demeurent applicables.")
old = "V.-Lorsque la déclaration d'activité du centre prévue à l'article L. 6351-1 a été enregistrée depuis moins de six mois, les avances des III et IV sont versées après vérification du début effectif de la formation. Cette vérification repose sur les pièces exactes déjà légalement disponibles pour l'opérateur ou, à défaut, sur une attestation de réalisation du début des actions. La seule ancienneté de l'enregistrement ne permet pas de reporter le premier acompte jusqu'au troisième mois."
new = "V.-L'enregistrement depuis moins de six mois de la déclaration d'activité du centre prévue à l'article L. 6351-1 ne subordonne pas les avances des III et IV à une attestation particulière de réalisation du début des actions de formation. Il ne permet pas de décaler le premier acompte jusqu'au troisième mois. Les contrôles de service fait et de qualité des actions demeurent applicables dans les conditions de droit commun."
assert old in a['proposed_xml']
a['proposed_xml'] = a['proposed_xml'].replace(old, new)
a['proposed_xml'] = a['proposed_xml'].replace("Les simplifications de pièces, la suppression du report spécial du premier acompte et celle de la déchéance de quatre mois", "Les simplifications de pièces, la suppression de l'attestation préalable particulière et du report spécial du premier acompte, ainsi que celle du délai de quatre mois et de sa déchéance")
a.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19', removed_provisions=[
    "Déduction de la participation patronale sur l'avance OPCO pour les contrats nouveaux, coordonnée à sa suppression législative sans diminuer les niveaux de prise en charge.",
    "Communication de la copie de la facture de participation patronale comme condition de paiement du solde, y compris pour les versements encore dus d'anciens contrats.",
    "Délai de transmission de quatre mois après le terme et déchéance automatique du solde en cas de transmission tardive des pièces.",
    "Attestation préalable particulière de début de formation conditionnant les avances du seul fait d'un enregistrement du CFA depuis moins de six mois.",
    "Faculté spéciale de reporter au troisième mois le premier acompte des CFA récemment enregistrés, sans supprimer les contrôles de service fait."
])
a['reason'] = "Réduction de fond par rapport à la source entière : maintien de la suppression de la copie de facture patronale, du délai de quatre mois et de la déchéance du solde, et du report spécial au troisième mois. La seconde passe retire aussi l'attestation préalable particulière des CFA enregistrés depuis moins de six mois, que le brouillon conservait à titre subsidiaire : les contrôles de service fait et de qualité fournissent un fondement autonome de vérification. Les autres factures et preuves nécessaires, échéanciers, niveaux et majorations favorables sont maintenus. La suppression de la déduction patronale coordonne le transfert de financement vers l'OPCO, sans baisse fictive du coût total de formation. Le réemploi de données déjà détenues n'est pas revendiqué comme une mesure nouvelle."
a['review_notes'] = "Conserver les I à VI et les 1° à 4° du III et 1°/2° du IV. Paramètres vérifiés : avance conventionnelle de 30 % au II ; 40/30/20 % et solde au III, trente jours après facture, septième et dixième mois ; 50 % pour une durée inférieure à un an ; majoration possible de 10 % sous son plafond et avec son exclusion pour les titres ministériels à durée réglementaire inférieure à un an ; maintien de six mois après rupture. La durée porte sur l'apprentissage, non sur le CDI. Le troisième alinéa de L. 6222-7-1 vise l'adaptation pédagogique, pas le barème de rupture ; son contenu est fourni. Le décret 2018-1345 reste une référence existante : aucune formule nouvelle n'en est déduite. L. 6222-12-1 et R. 6222-1-1, lus intégralement dans le corpus, concernent deux accès distincts à la formation avant contrat, sans cumul artificiel des conditions. R. 6332-26, lu intégralement avec ses notes, maintient contrôle de service fait, pièces complémentaires nécessaires, contrôle sur place, contradictoire d'au moins sept jours, refus de prise en charge des actions non justifiées et signalements : le V ne crée pas un circuit déclaratif de remplacement. Coordonner l'arrêté de pièces pris sur cet article pour ne pas rétablir l'attestation systématique supprimée. Le retrait de participation exige la correction simultanée du 1° du I et du III de L. 6332-14 : la proposition fournie les maintient encore, contradiction expressément signalée. Les articles R. 6332-25-1/2 sont coordonnés dans ce lot. La note du décret 2025-585 concerne les contrats depuis le 1er juillet 2025, pas la promulgation future ; les cohortes antérieures gardent leurs règles. Aucune décision définitive ni prescription acquise n'est rouverte. Le coût du transfert vers l'OPCO et de l'accélération des paiements n'est pas chiffré."
a['benefit_review'] = "Les facilités de trésorerie du II (échelonnement et avance jusqu'à 30 %), les avances de 40 %, 30 % et 20 %, le solde, l'avance de 50 % des apprentissages courts, la majoration possible de 10 % et son plafond sont conservés dans leurs champs, pour les futurs apprentissages du contrat unique aussi. L'exception de titre ministériel à durée réglementaire inférieure à un an est une limite du 2° du IV, conservée sans extension. La prise en charge et les frais annexes, la période de CFA avant signature dans chacun des cas du VI, ainsi que les versements après rupture jusqu'au nouveau contrat ou à six mois, restent ouverts. La suppression du délai et de la déchéance de quatre mois sécurise le solde restant à payer, sans rouvrir les décisions définitives. La déduction patronale ancienne reste dans son champ ; son retrait pour les contrats nouveaux accompagne la disparition de la charge correspondante, sans minoration de remplacement. L'attestation préalable et le report du V sont des restrictions aux avances, non des avantages à conserver ; les retirer n'éteint aucune aide. Les aides ne sont jamais subordonnées au seuil d'un an de l'indemnité ordinaire."

for number, scope in [
    ('R6332-25-1', "Participation patronale des nouveaux contrats d'apprentissage : forfait de 750 euros au niveau 6 ou supérieur, variante de 50 % proratisée plafonnée à 750 euros et forfait de 200 euros après rupture ; règles anciennes conservées."),
    ('R6332-25-2', "Émission et transmission par les CFA de la facture de participation patronale pour les nouveaux apprentissages ; facturation des créances anciennes et factures de formation distinctes conservées.")]:
    answers[number].update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19', repeal_scope=scope)

answers['R6332-25-1']['reason'] = "Suppression de fond déjà acquise et maintenue après examen des trois alinéas : aucun des forfaits ou prorata de la participation patronale ne subsiste pour un nouveau contrat. L'objectif de formation ne nécessite pas ce cofinancement obligatoire supplémentaire ; les contrôles, qualifications et niveaux de prise en charge ont leurs règles propres. Les plafonds et réductions anciens demeurent. Il s'agit d'un allègement pour l'employeur et d'un transfert vers le financement OPCO, non d'une baisse démontrée du coût total de formation. Aucune charge additionnelle détachable ne reste à retirer dans ce règlement après sa suppression prospective entière."
answers['R6332-25-1']['review_notes'] += " La vue proposée de L. 6332-14 fournie ici n'a pas encore retiré la participation, sa minoration corrélative et l'habilitation du III : cette incohérence doit être corrigée dans cet article législatif, hors du présent lot réglementaire, avant entrée en vigueur commune. Le coût supplémentaire des fonds de formation n'est pas couvert par une recette supposée."
answers['R6332-25-2']['reason'] = "Abrogation de coordination maintenue : la facturation obligatoire n'a plus d'objet pour les nouveaux contrats dès lors que toute la participation est supprimée. La facturation des créances anciennes demeure nécessaire à leur règlement et contestation ; celle du service réel de formation garde sa fonction distincte. La copie adressée à l'OPCO pour payer le solde est supprimée dans R. 6332-25, y compris pour les anciens contrats encore concernés, sans compter deux fois la même pièce ni le même transfert de financement. Aucune formalité de substitution n'est ajoutée."
answers['R6332-25-2']['review_notes'] += " La vue fournie de L. 6222-18 place de nouveaux paragraphes avant le premier alinéa historique : pour les contrats anciens, la référence doit rester matériellement celle des quarante-cinq jours de formation pratique, et non le premier paragraphe nouveau du projet. Cette coordination d'alinéa est indispensable dans la consolidation de L. 6222-18."

a = answers['D7112-1']
a['proposed_xml'] = a['proposed_xml'].replace("reste au moins égale à un mois de salaire par année ou fraction d'année de ces services", "reste au moins égale à un mois des derniers appointements par année ou fraction d'année de ces services")
a['proposed_xml'] = a['proposed_xml'].replace("Lorsqu'elle est due à raison d'une rupture à l'initiative de l'employeur, elle est nulle avant un an d'ancienneté.", "Elle est due uniquement lors d'une rupture à l'initiative de l'employeur, sous les conditions de cet article, notamment son exception de faute grave. Aucune indemnité ordinaire n'est due avant un an d'ancienneté.")
a['proposed_xml'] = a['proposed_xml'].replace("les fractions d'année étant calculées au prorata de leur durée", "les fractions d'année étant calculées au prorata des mois complets de service")
a['proposed_xml'] = a['proposed_xml'].replace("fractions d'année au prorata de leur durée", "fractions d'année au prorata des mois complets de service")
a['proposed_xml'] = a['proposed_xml'].replace("Le salaire de référence de chaque composante est déterminé à la rupture selon son régime applicable.", "Les mois complets de service sont répartis entre les deux composantes ; un mois chevauchant l'entrée en vigueur est réparti à proportion du service accompli de chaque côté, sans perte ni double compte. Le salaire de référence de chaque composante est déterminé à la rupture selon son régime applicable.")
a['proposed_xml'] = a['proposed_xml'].replace("Le minimum d'un mois de salaire par année ou fraction d'année", "Le minimum d'un mois des derniers appointements par année ou fraction d'année")
a.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19', removed_provisions=[
    "Minimum professionnel ordinaire d'un mois par année ou fraction d'année et plafond de quinze mensualités pour les contrats nouveaux, remplacés par le barème commun de rupture.",
    "Acquisition future du barème professionnel ordinaire sur les services des contrats antérieurs accomplis après la réforme, sans supprimer la composante acquise ni l'indemnité spéciale."
])
a['reason'] = "Coordination de la réduction de fond décidée pour l'indemnité ordinaire : le barème professionnel d'un mois par année ou fraction d'année, plafonné à quinze mensualités, laisse place au barème commun pour les nouveaux contrats et les services futurs des contrats anciens. La seconde passe corrige le prorata du brouillon : mois complets, seuil d'un an mesuré au terme effectif avec préavis et totalité de l'ancienneté dès le seuil atteint. La composante antérieure et les indemnités spéciales de L. 7112-5 restent protégées ; les réduire davantage effacerait des droits expressément préservés. Le règlement n'est pas présenté comme une seconde réduction indépendante de la mesure législative."
a['review_notes'] = "La source réglementaire est intégralement examinée avec les cibles L. 7112-3/4/5. L. 7112-3 proposé conserve encore tout le régime ancien aux contrats antérieurs : il faut le coordonner expressément sur leurs deux composantes pour appliquer la transition retenue par coordination.json ; ce règlement seul ne peut abaisser le minimum législatif. Pour la composante antérieure, le salaire de référence reste celui des derniers appointements selon le régime professionnel, sans importation silencieuse de la moyenne commune. L. 7112-4 conserve l'arbitrage au-delà de quinze ans et en matière de faute grave ou de fautes répétées dans son champ ; pas de plafond opposé à sa compétence conservée. L. 7112-5 préserve cession, cessation de publication et changement portant atteinte aux intérêts moraux, ainsi que la dispense de préavis du seul 3°. Le nouveau seuil d'un an ne concerne pas cette indemnité spéciale. L. 1234-9 fourni conserve l'exception de faute grave pour l'indemnité ordinaire, distincte du paiement du préavis nouveau. R. 1234-1/2/4 et L. 7112-2 ont été lus dans le corpus public : mois complets, répartition du mois de bascule, référence commune selon la formule la plus favorable, préavis ancien ou nouveau selon la date du contrat. Ces consultations facultatives ne sont pas ajoutées à reference_checks. Les salaires, congés, dommages et garanties plus favorables ne sont pas réduits par le plafond légal de six mois. Aucun double compte d'une période, aucune remise à zéro lors d'une conversion."

a = answers['R7413-4']
a['proposed_xml'] = a['proposed_xml'].replace("de quinze jours calendaires à compter de sa notification, à l'initiative de l'employeur comme du salarié, selon le calcul prévu à l'article L. 1234-3", "de quinze jours calendaires, à l'initiative de l'employeur comme du salarié. Il se compte à partir du lendemain de la présentation au salarié ou, lorsque la loi autorise un autre mode, de la réception de la notification écrite ; pour une rupture par le salarié, il se compte à partir du lendemain de la réception de sa notification écrite par l'employeur, conformément à l'article L. 1234-3")
a['reason'] = "La moyenne salariale de six mois, nécessaire au calcul du préavis des travailleurs à domicile, est conservée. La coordination de fond du contrat unique maintient le paiement du préavis nouveau même en cas de faute grave, avec les dispenses favorables du salarié et les règles anciennes dans leur champ. La seconde passe rectifie le départ du délai du brouillon pour viser expressément le lendemain de la notification pertinente. Aucune archive ou déclaration détachable n'existe ici à retirer. La suppression de l'exception de faute grave crée une obligation de paiement dans le nouveau champ : elle ne constitue pas une baisse de charge et est recensée comme telle."
a['review_notes'] = "Les onze cibles fournies distinguent durée, notification, effet sur la date de fin et rémunération. Les quinze jours expirent à la fin du quinzième jour, jours non travaillés compris, selon L. 1234-3 ; aucune attente d'ancienneté ne s'y ajoute. La moyenne de six mois n'est ni le préavis ni le barème ordinaire d'indemnité de rupture. L. 1234-5 proposé couvre déjà la faute grave du contrat nouveau, tout en excluant un paiement automatique pour le refus de travail du salarié ; le présent règlement s'y coordonne sans étendre cette garantie aux contrats anciens. L. 1234-6 et L. 1234-7 gardent leurs champs propres de fermeture, réduction d'horaire, cessation et force majeure. Les suspensions et leur exception favorable aux élus locaux restent dans L. 1234-8 pour les contrats anciens. Les autorisations des salariés protégés et les procédures collectives ne sont pas absorbées par le préavis individuel. La source ne précise pas la moyenne en présence de moins de six mois : cette lacune demeure signalée, sans salaire fictif ni prorata inventé. Les six mois sont conservés faute de formule alternative décidée et documentée."

a = answers['L321-4-2']
a.update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19', repeal_scope="Suppression prospective du fondement ancien des nouvelles conventions de reclassement personnalisé et de leurs contributions, sans réactivation d'un régime déjà remplacé ni extinction des droits historiques ou du CSP autonome.")
a['reason'] += " La seconde passe ne retranche pas les protections restantes : elles règlent exclusivement les situations historiques légalement couvertes et les droits autonomes du CSP. Les contributions anciennes ne sont pas présentées comme des prélèvements actuels nouvellement supprimés ; aucune applicabilité générale de cette ancienne codification n'est présumée."
a['review_notes'] += " Les vues de L. 1233-67/68/69 fournies distinguent désormais les adhésions antérieures et nouvelles, le versement de financement supprimé et les sommes maintenues directement au salarié : la réserve du CSP ne rétablit pas ce versement par la formule générale de financement historique. L. 1233-65/66/70 ont été consultés en entier dans le corpus public pour confirmer le parcours autonome, la proposition obligatoire, la contribution pour défaut de proposition et les conventions de financement ; ils ne sont pas ajoutés aux cibles obligatoires. La note d'abrogation générale de l'ancienne partie législative portée par L. 981-4 et la date différée de cette source se contredisent dans l'affichage du corpus : la consolidation chronologique reste à contrôler, sans déclarer une économie actuelle."
a['benefit_review'] = "La source prévoit un accompagnement psychologique, l'orientation, l'évaluation, la formation et le reclassement, le statut de stagiaire, une allocation et un financement collectif et public. Elle double le reliquat DIF plafonné à vingt heures par année et cent vingt heures sur six années, tout en limitant son financement à l'allocation de formation. Elle conserve l'indemnité de licenciement, le solde de préavis au-delà de deux mois, la somme équivalente au préavis légal inférieur à deux mois versée dès la rupture et leurs régimes social et fiscal. Tous ces avantages et leurs financements demeurent pour les conventions et situations anciennes légalement régies par la source, y compris leurs échéances futures. Pour les nouvelles situations, le CSP des articles L. 1233-65 à L. 1233-70 reste ouvert avec accompagnement, formation, allocation, CPF, indemnités et protections dans son champ propre. Le DIF historique n'est ni ressuscité ni converti fictivement en un crédit contemporain : son dispositif relève de l'ancienne codification et son maintien général après 2008 n'est pas établi. La disparition prospective de ce fondement ancien ne ferme pas l'accès futur au CSP ni ne rétablit le versement patronal de financement supprimé dans les propositions L. 1233-68/69."

a = answers['L981-4']
a['reason'] += " La seconde passe ne retranche pas la faculté favorable de financement : elle est optionnelle, porte sur des fonds et actions déterminés et n'impose aucun dépôt individuel supplémentaire. La seule contrainte de signature de l'État demeure liée à l'affectation de fonds collectifs dans les deux textes législatifs ; la supprimer dans cette seule survivance créerait un conflit avec L. 6325-24 sans démonstration d'un doublon de procédure actuel. L'ancienne possibilité de CDD n'est pas comptée comme une charge actuelle nouvellement supprimée."
a['review_notes'] += " L. 6325-1/2 et L. 6325-24 ont été consultés intégralement dans le corpus public, en complément des cibles obligatoires : le dernier conserve expressément l'accord entre organisations représentatives et État pour les fonds d'alternance actuels. Il ne suffit pas à établir une concordance d'assiette avec les anciens L. 951-1 et L. 952-1, dont le contenu n'est pas fourni dans les cibles ; ces références sont conservées uniquement pour leur champ ancien, sans formule de contribution inventée. Aucun nouveau renvoi normatif n'est ajouté par rapport au brouillon ; les références modernes absentes des cibles sont identifiées dans cette note. Le travail temporaire privé ne doit pas être confondu avec un régime d'agents publics."

# Corrections issues de la relecture source/proposition intégrales.
answers['R6332-25']['proposed_xml'] = answers['R6332-25']['proposed_xml'].replace(
    "4° Le solde en même temps que", "4° Le solde est versé en même temps que").replace(
    "VI.-Dans les cas prévus aux articles L. 6222-12-1 et R. 6222-1-1, après la conclusion du contrat d'apprentissage,",
    "VI.-Dans chacun des cas prévus à l'article L. 6222-12-1 ou à l'article R. 6222-1-1, après la conclusion du contrat d'apprentissage,")

answers['R6332-25-1']['proposed_xml'] = answers['R6332-25-1']['proposed_xml'].replace(
    "en cas de rupture pendant la période du premier alinéa de l'article L. 6222-18",
    "en cas de rupture pendant les quarante-cinq premiers jours, consécutifs ou non, de formation pratique en entreprise effectuée par l'apprenti, prévus au premier alinéa de l'article L. 6222-18 dans sa rédaction applicable au contrat antérieur")
answers['R6332-25-2']['proposed_xml'] = answers['R6332-25-2']['proposed_xml'].replace(
    "à l'issue de la période mentionnée au premier alinéa de l'article L. 6222-18, selon les règles antérieures et leurs réductions",
    "à l'issue des quarante-cinq premiers jours, consécutifs ou non, de formation pratique en entreprise effectuée par l'apprenti, prévus au premier alinéa de l'article L. 6222-18 dans sa rédaction applicable au contrat antérieur, selon ces règles et leurs réductions")
for number in ('R6332-25-1', 'R6332-25-2'):
    answers[number]['review_notes'] += " La proposition finale explicite les quarante-cinq jours pratiques et fige le renvoi dans la rédaction applicable au contrat antérieur : elle évite ainsi de viser le nouveau premier paragraphe du projet de L. 6222-18."

answers['D7112-1']['proposed_xml'] = answers['D7112-1']['proposed_xml'].replace(
    "Les mois complets de service sont répartis entre les deux composantes ; un mois chevauchant l'entrée en vigueur est réparti à proportion du service accompli de chaque côté, sans perte ni double compte.",
    "Le prorata des mois complets s'applique à cette seule composante postérieure à l'entrée en vigueur. Un mois complet de service chevauchant cette date n'est retenu dans cette composante qu'à proportion du service accompli après cette date ; le minimum professionnel de la composante antérieure demeure régi par le premier alinéa, sans double compte des services.")
answers['D7112-1']['review_notes'] += " Le prorata des mois complets concerne le barème commun nouveau, non le minimum professionnel acquis d'un mois par année ou fraction d'année : la proposition finale préserve expressément cet arrondi favorable de la composante antérieure."

def source_p(number, index):
    return plain(re.findall(r'<p\b[^>]*>(.*?)</p>', by_number[number]['source_xml'], re.S)[index]).strip()

def proposed_p(number, index):
    return plain(re.findall(r'<p\b[^>]*>(.*?)</p>', answers[number]['proposed_xml'], re.S)[index]).strip()

def effect(number, kind, measure_id, description, before, after, unit, population,
           transition, replacement, source_quote, proposed_quote):
    assert source_quote in plain(by_number[number]['source_xml']), (number, source_quote)
    assert proposed_quote in plain(answers[number]['proposed_xml']), (number, proposed_quote)
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit, affected_population=population,
                conditions_and_transition=transition, replacement_or_new_burdens=replacement,
                source_quote=source_quote, proposed_quote=proposed_quote)

def impact(number, classification, assessment, limitations, burdens, effects):
    answers[number]['substantive_impact'] = dict(
        version=1, classification=classification, assessment=assessment,
        scope_limitations=limitations, new_burdens_review=burdens, effects=effects)

n = 'D6325-14'
impact(n, 'coordination_only',
       "Le texte officiel distingue rémunération pendant le CDD et pendant l'action du CDI. La proposition rattache le même minimum à l'action du contrat unique et réserve le CDD aux situations anciennes. Elle ne réduit ni salaire, ni cotisation, ni formalité ; la mesure de contrat unique n'est pas comptée une seconde fois. La seconde passe ne trouve pas de charge accessoire détachable de ce minimum.",
       "Les taux et avantages en nature figurent dans les articles voisins et restent inchangés. Aucun effet sur l'emploi, le coût salarial global ou le financement de la formation n'est chiffré ; les anciens contrats gardent leur régime.",
       "Aucune charge administrative nouvelle n'est identifiée dans cet article : aucun document, registre, déclaration ou délai n'est ajouté. Le minimum salarial existant reste dû ; la durée indéterminée et ses règles de rupture résultent de la coordination générale, dont le solde n'est pas chiffré ici.",
       [effect(n, 'coordination', 'contrat-unique-duree-indeterminee',
               "Rattachement du salaire de professionnalisation à une phase pédagogique, sans terme automatique de l'emploi.",
               "Salariés de moins de vingt-six ans : minimum selon âge et formation pendant le CDD entier ou l'action du CDI ; aucun montant fixé ici.",
               "Même population et mêmes paramètres salariaux pendant l'action du contrat unique ; poursuite de l'emploi après l'action.",
               'regime', "Salariés privés de moins de vingt-six ans en professionnalisation.",
               "Nouveaux contrats à compter de la réforme ; anciens contrats et rémunérations acquis préservés, sans nouveau CDD ni renouvellement.",
               "Aucun document de substitution ; les règles de rupture du contrat unique restent autonomes.",
               source_p(n, 0), proposed_p(n, 0))])

impact('D6325-18', 'retained_necessary',
       "Le plancher de 85 % du minimum de branche est conservé intégralement, avec le SMIC porté par L. 6325-9. L'examen de la source entière n'identifie aucun agrément, contribution accessoire, justificatif, double dépôt ou délai à supprimer sans retirer la garantie salariale elle-même. Le brouillon antérieur n'apportait pas de coupe supplémentaire.",
       "Maintien limité aux titulaires âgés d'au moins vingt-six ans et au champ de L. 6325-9, y compris sa phase de professionnalisation future et ses transitions. Les autres minima et le salaire après la phase ne sont pas révisés ici ; aucune économie n'est revendiquée.",
       "Aucune charge nouvelle n'est identifiée : le texte source reste reproduit à l'identique, sans registre, donnée, justificatif, délai ou condition supplémentaires. La charge salariale nécessaire déjà existante n'est pas présentée comme une simplification.", [])

n = 'D6331-72'
impact(n, 'coordination_only',
       "L'article officiel ne crée pas la contribution : il en énumère les exclusions. Son abrogation pour les périodes futures est cohérente uniquement avec l'abolition intégrale du CPF-CDD de L. 6331-6. Les quatre exclusions actives et les autres dispenses restent utilisables pour les anciennes périodes. Ce n'est pas une deuxième baisse de 1 %.",
       "La loi doit supprimer le CPF-CDD au même moment et selon le même rattachement aux périodes de travail. Les contributions ordinaires de formation et le financement global du CPF ne sont pas abolis ni chiffrés ici. Les créances anciennes restent régularisables.",
       "Aucune charge nouvelle n'est identifiée : aucun prélèvement, déclaration ou justificatif ne remplace la contribution supprimée. Les règles anciennes nécessaires aux régularisations ne créent pas une collecte sur les rémunérations des périodes nouvelles.",
       [effect(n, 'coordination', 'cpf-cdd-suppression',
               "Extinction prospective de la liste d'exclusions d'une contribution supprimée intégralement dans son article législatif.",
               "CPF-CDD de 1 % du revenu d'activité retenu pour les cotisations des CDD par L. 6331-6 ; exclusions CAE, apprentissage, professionnalisation et L. 6321-9 dans cette liste.",
               "0 % au titre de cette contribution pour les périodes d'emploi futures, y compris sous ancien CDD ; toutes les exclusions restent opposables pour les périodes anciennes.",
               'legal_duty', "Employeurs et contrats relevant de la contribution CPF-CDD et de ses exclusions réglementaires.",
               "Périodes d'emploi à compter de l'entrée en vigueur du contrat unique ; ni exonérations ni restitutions anciennes éteintes.",
               "Aucun prélèvement équivalent, aucune fermeture de droit à la formation ; coordination législative indispensable.",
               source_p(n, 0), "Cette contribution cesse d'être due pour ces rémunérations, y compris lorsqu'elles sont versées au titre d'un contrat à durée déterminée conclu avant cette entrée en vigueur." )])

n = 'R6332-25'
impact(n, 'mixed',
       "Par rapport à toute la source, le solde perd sa condition de copie de facture patronale ainsi que le délai de quatre mois et sa déchéance ; les CFA récemment enregistrés perdent l'attestation préalable spéciale et la possibilité de report au troisième mois. Les prises en charge, avances et majorations restent applicables. La suppression de la déduction de participation déplace du financement patronal vers l'OPCO : elle n'abaisse pas le coût total de la formation. Les simplifications nettes de pièces ne sont pas confondues avec le réemploi déjà prévu par le droit général.",
       "Le montant à payer reste subordonné aux niveaux légaux et aux prestations financées, contrôlables. L. 6332-14 doit encore être modifié dans sa vue fournie. Les situations antérieures au 1er juillet 2025 gardent leurs règles propres et les décisions définitives ne sont pas rouvertes. Le coût public et l'effet net de trésorerie ne sont pas établis.",
       "Aucun registre, donnée périodique, attestation ou dépôt de remplacement n'est ajouté. L'OPCO doit néanmoins supporter la prise en charge sans déduction patronale pour les contrats nouveaux, ce qui augmente son financement par rapport à la source ; les avances peuvent aussi être payées plus tôt. Ces effets financiers ne sont pas une économie nationale et leur solde global reste inconnu.",
       [effect(n, 'coordination', 'apprentissage-participation-employeur-suppression',
               "Suppression de la minoration de l'avance pour les apprentissages nouveaux, en coordination avec le retrait du cofinancement obligatoire.",
               "Avance de 40 % du montant annuel, diminuée le cas échéant de la participation patronale pour la première année du contrat supérieur à un an, même non recouvrée.",
               "Avance de 40 % sans cette minoration pour les nouveaux contrats ; participation ancienne maintenue pour les anciens contrats dans ses conditions.",
               'financing', "OPCO, CFA et employeurs d'apprentis concernés par la participation de L. 6332-14.",
               "Contrats conclus à compter de la suppression législative de la participation ; anciennes dettes et réductions conservées.",
               "Financement supplémentaire pour l'OPCO, sans nouvelle participation de substitution pour l'employeur ; coût total de la formation non diminué par cette seule mesure.",
               source_p(n, 3), "Aucune participation n'est déduite pour un contrat nouveau relevant de cette suppression ;"),
        effect(n, 'obligation_removed', 'apprentissage-solde-copie-participation',
               "Retrait de la copie de la facture patronale comme pièce distincte de liquidation du solde OPCO.",
               "Au solde, le CFA transmet une copie de la facture de participation lorsque l'employeur est redevable, en plus de la facture et de l'attestation de réalisation.",
               "La copie de participation n'est plus une condition du solde, même si une participation ancienne reste due ; facture de formation et preuve de réalisation restent nécessaires.",
               'legal_duty', "CFA demandant à un OPCO le solde d'une prise en charge d'apprentissage.",
               "Versements restant à effectuer après la réforme, sans réouverture des décisions définitives ; aucune seconde suppression comptée dans R. 6332-25-2.",
               "Aucune pièce de substitution à la copie supprimée ; preuve du service réel maintenue dans son champ autonome.",
               source_p(n, 6), "La copie de la facture de participation patronale prévue à l'article R. 6332-25-2 n'est pas exigée pour payer ce solde."),
        effect(n, 'obligation_removed', 'apprentissage-solde-delai-quatre-mois',
               "Suppression du délai de quatre mois assorti d'une perte automatique du solde.",
               "Pièces du solde à transmettre dans les quatre mois suivant le terme, faute de quoi le solde n'est pas dû.",
               "Aucun délai spécial de quatre mois ni déchéance attachée à ce délai ; facturation, preuve des actions et prescriptions de droit commun demeurent.",
               'legal_duty', "CFA ayant une créance de solde sur un OPCO au titre d'une formation financée.",
               "Versements restant à effectuer à l'entrée en vigueur ; prescriptions acquises et décisions définitives non rouvertes.",
               "Aucun délai de remplacement ; le paiement n'est pas accordé à une formation non réalisée.",
               "A défaut de transmission de ces éléments dans ce délai, le solde n'est pas dû.",
               "Aucun délai de transmission de quatre mois suivant la fin du contrat ou de la période d'apprentissage ne conditionne le paiement du solde."),
        effect(n, 'obligation_removed', 'apprentissage-cfa-controle-prealable-special',
               "Suppression de l'attestation préalable spéciale et du report lié au seul enregistrement récent du CFA.",
               "CFA enregistrés depuis moins de six mois : attestation de réalisation du début pour les avances III/IV et premier acompte reportable jusqu'au troisième mois.",
               "Enregistrement récent sans attestation préalable spéciale ni report automatique jusqu'au troisième mois ; contrôle de service fait et de qualité de droit commun conservé.",
               'legal_duty', "CFA dont la déclaration d'activité est enregistrée depuis moins de six mois, et OPCO financeurs.",
               "Avances restant à effectuer à compter de la réforme ; pas de remise en cause d'une décision définitive.",
               "Aucune attestation équivalente ni contrôle préalable systématique de remplacement ; contrôles autonomes et refus des dépenses non justifiées maintenus.",
               source_p(n, 11), proposed_p(n, 11))])

n = 'R6332-25-1'
impact(n, 'financing_transfer',
       "Les trois modalités obligatoires de participation sont entièrement retirées pour les nouveaux contrats : 750 euros, 50 % proratisés plafonnés à 750 euros et 200 euros après rupture. Le gain propre à l'employeur est réel. La prise en charge OPCO n'est plus minorée, de sorte que ce retrait transfère le financement sans démontrer une diminution du coût total de la formation ; aucun montant national d'économie n'est avancé.",
       "Application aux contrats conclus après l'entrée en vigueur commune de la loi et du règlement. Les contrats antérieurs, notamment la cohorte ouverte au 1er juillet 2025, gardent les réductions et plafonds. La vue législative de L. 6332-14 reste à corriger ; les ressources et l'incidence budgétaire de l'OPCO ne sont pas déterminées ici.",
       "Aucune obligation, condition de niveau, déclaration ou donnée nouvelle ne remplace la participation pour l'employeur. La charge de financement correspondante est supportée par l'OPCO à niveau de prise en charge inchangé : cette charge financière supplémentaire est identifiée, sans recette compensatrice inventée ni chiffrage net de l'ensemble des codes.",
       [effect(n, 'financing_transfer', 'apprentissage-participation-employeur-suppression',
               "Suppression du cofinancement patronal réglementaire et rétablissement corrélatif de la prise en charge OPCO sans minoration.",
               "750 euros par contrat visant au moins le niveau 6 ; en rupture pendant la période initiale de L. 6222-18, 50 % de la prise en charge proratisée au nombre de jours dans la limite de 750 euros ; 200 euros pour le nouveau contrat avec autre employeur après rupture.",
               "0 euro de participation sur ces fondements pour tout contrat nouveau ; la prise en charge OPCO n'est pas minorée de ces sommes. Coût réel de la formation inchangé par cette seule suppression.",
               'financing', "Employeurs d'apprentis relevant de la participation de L. 6332-14, CFA et OPCO financeurs.",
               "Nouveaux contrats à compter de la suppression législative ; plafonds, réductions, créances et recours des contrats antérieurs maintenus, sans remboursement général.",
               "Transfert vers le financement OPCO ; aucun autre forfait, déclaration, donnée ou paiement de remplacement pour l'employeur.",
               plain(by_number[n]['source_xml']).strip(), "Pour ces contrats, aucune participation forfaitaire de 750 euros, participation proportionnelle ou participation de 200 euros à la suite d'une rupture n'est due sur ce fondement.")])

n = 'R6332-25-2'
impact(n, 'coordination_only',
       "La facture patronale obligatoire est retirée pour les contrats nouveaux parce que la participation correspondante est entièrement supprimée. Cette coordination n'est pas une deuxième suppression des 750 ou 200 euros, ni une nouvelle suppression de la copie du solde déjà traitée dans R. 6332-25. La facturation des créances anciennes conserve sa fonction de preuve et de contestation.",
       "La suppression législative de L. 6332-14 demeure indispensable. Les créances des contrats anciens restent facturées à l'échéance initiale des quarante-cinq jours de formation pratique ; le nouveau premier paragraphe de L. 6222-18 ne doit pas décaler ce renvoi. Les factures de formation et les charges de gestion de l'OPCO restent distinctes.",
       "Aucune charge nouvelle n'est identifiée dans cette coordination : aucun document, registre, déclaration ou paiement équivalent n'est exigé. Les factures de services et les factures des créances anciennes gardent leurs fondements antérieurs, sans nouveau double envoi.",
       [effect(n, 'coordination', 'apprentissage-participation-employeur-suppression',
               "Retrait du document de facturation d'une participation supprimée pour les contrats nouveaux.",
               "Le CFA émet et transmet à l'employeur une facture de participation à l'issue de la période initiale de L. 6222-18.",
               "Aucune facture de participation pour un contrat nouveau ; anciennes participations facturées et factures des formations réelles maintenues.",
               'legal_duty', "CFA et employeurs d'apprentis soumis à la participation patronale.",
               "Contrats conclus après l'entrée en vigueur de la loi de suppression ; contrats antérieurs et créances correspondantes gardent leurs règles favorables et recours.",
               "Aucun document ou paiement équivalent ; la copie de l'ancienne facture n'est plus exigée par l'OPCO pour le solde selon R. 6332-25.",
               source_p(n, 0), "Le centre de formation d'apprentis n'émet ni ne transmet de facture de cette participation pour ces contrats.")])

n = 'D7112-1'
impact(n, 'coordination_only',
       "Le minimum professionnel ordinaire d'un mois par année ou fraction, plafonné à quinze mensualités, est remplacé dans le nouveau champ par le barème commun de 0,20 mois par année totale, prorata des mois complets et plafond de six mois. L'effet est une réduction de l'indemnité ordinaire patronale, coordonnée à la mesure commune et non comptée comme une deuxième économie. Le seuil nouveau d'un an et la règle du préavis inclus sont explicités. Les indemnités spéciales et la composante antérieure sont conservées.",
       "La transition à deux composantes doit aussi figurer dans L. 7112-3 : sa proposition fournie conserve encore le régime entier des anciens contrats. Les règles plus favorables, l'arbitrage de L. 7112-4, les indemnités spéciales et les dommages ne sont pas plafonnés par cette mesure. Aucun montant agrégé de baisse de coût n'est établi.",
       "Aucun registre, déclaration ou justificatif nouveau n'est identifié. Le seuil d'un an est toutefois une condition nouvelle restrictive d'accès à l'indemnité ordinaire des contrats nouveaux ; le calcul en deux composantes des contrats anciens requiert une ventilation de l'ancienneté déjà connue. Ces éléments sont ceux de la mesure commune, sans double compte ni présomption d'un solde global simplifié.",
       [effect(n, 'coordination', 'contrat-unique-indemnite-ordinaire',
               "Application du barème commun à l'indemnité ordinaire des journalistes avec maintien des composantes anciennes et des cas spéciaux.",
               "Indemnité professionnelle au moins égale à un mois des derniers appointements par année ou fraction d'année, maximum quinze mensualités sous réserve de l'arbitrage légal, sans seuil d'un an fixé par cet article.",
               "Contrats nouveaux : employeur seul, zéro avant un an au terme effectif préavis inclus, puis 0,20 mois de référence par année totale, mois complets au prorata, plafond six mois ; ancienne composante et indemnité spéciale conservées.",
               'regime', "Journalistes professionnels entrant dans le champ de L. 7112-3, sous réserve des cas spéciaux de L. 7112-5.",
               "Nouveaux contrats et services après réforme des anciens contrats selon la transition de la loi ; minimum professionnel acquis avant réforme, références salariales propres et indemnités spéciales futurs préservés.",
               "Pas de prélèvement ou de formalité équivalents ; seuil d'un an nouveau et ventilation de l'ancienneté signalés. Coordination législative des anciens contrats encore requise.",
               source_p(n, 0), proposed_p(n, 1))])

n = 'R7413-4'
impact(n, 'mixed',
       "La formule officielle de moyenne des salaires des six mois reste entière. Le texte coordonne la durée du préavis individuel nouveau de quinze jours, sans prétendre réduire toute la procédure de rupture. Par rapport à la source, la faute grave ne dispense plus l'employeur du préavis payé dans le champ nouveau : c'est une obligation patronale supplémentaire, recensée avec la coordination du délai. Les contrats anciens gardent leur exception. Aucun gain net global n'est démontré.",
       "La source ne précise pas la référence lorsque le salarié est présent moins de six mois : aucun salaire fictif n'est ajouté. La durée ancienne, les suspensions, la force majeure et les procédures collectives conservent leurs textes propres. Le changement de délai ne garantit pas une baisse pour tout salarié dont le préavis antérieur pouvait être plus court ou inexistant.",
       "L'obligation de payer le préavis nouveau même en cas de faute grave est une charge nouvelle pour l'employeur dans ce cas, issue du noyau législatif et explicitement coordonnée ici. Aucun nouveau registre, justificatif ou envoi n'est ajouté par ce règlement ; la notification écrite et sa preuve relèvent du régime commun. Le solde financier net n'est pas établi.",
       [effect(n, 'coordination', 'contrat-unique-preavis-quinze-jours',
               "Conservation de la moyenne salariale spéciale et application du délai individuel commun aux contrats nouveaux.",
               "Travailleurs à domicile en CDI : indemnité d'inobservation du préavis de L. 1234-1 à L. 1234-8 et L. 1237-1 fondée sur la moyenne des six mois, sans durée autonome fixée ici.",
               "Même moyenne de six mois ; quinze jours calendaires individuels des deux côtés pour les contrats nouveaux, à compter du lendemain de la notification pertinente selon L. 1234-3.",
               'calendar_days', "Travailleurs à domicile salariés de droit privé en CDI ancien ou en contrat unique nouveau.",
               "Contrats nouveaux à compter de la loi ; anciens contrats, créances, dispenses du salarié, autorisations et procédures collectives préservés.",
               "Aucun circuit de notification supplémentaire ; l'indemnité de préavis ne relève ni du seuil d'un an ni du plafond de l'indemnité ordinaire.",
               source_p(n, 0), proposed_p(n, 2)),
        effect(n, 'obligation_added', 'contrat-unique-preavis-quinze-jours',
               "Paiement patronal du préavis nouveau malgré la faute grave, à distinguer de la réduction de sa durée dans d'autres situations.",
               "La source exclut l'indemnité d'inobservation du préavis en cas de rupture pour faute grave.",
               "Dans le contrat nouveau, faute grave sans dispense du préavis dû ; paiement si son exécution est impossible, avec référence salariale de six mois.",
               'legal_duty', "Employeurs de travailleurs à domicile sous contrat unique rompu pour faute grave.",
               "Contrats conclus après la réforme ; l'exception de faute grave demeure pour les contrats antérieurs et les règles propres de force majeure ne sont pas supprimées.",
               "Charge financière supplémentaire dans ce cas, sans déclaration ni justificatif supplémentaires ; le refus de travail du salarié ne crée pas automatiquement un droit au paiement.",
               source_p(n, 0), "La faute grave ne dispense pas l'employeur du préavis dû dans ce nouveau régime ; lorsque son exécution est impossible, sa rémunération reste due selon les articles L. 1234-1 à L. 1234-8.")])

n = 'L321-4-2'
impact(n, 'coordination_only',
       "La source appartient à l'ancienne codification et organise la CRP, alors que les cibles actuelles organisent le CSP. L'abrogation prospective empêche la réactivation de ce circuit ancien et de ses contributions, tout en réservant droits et financements historiques et le CSP futur. La chronologie de l'affichage VIGUEUR est incohérente avec la note d'abrogation générale de l'ancienne partie : aucune suppression d'une charge actuelle ni économie nouvelle n'est tenue pour démontrée.",
       "Les anciennes conventions ne sont conservées que lorsqu'elles restent légalement régies par ce texte. Les anciens renvois ne sont pas des concordances financières actuelles vérifiées. La portée temporelle exacte du résidu doit être clarifiée dans la consolidation, sans effacer l'accompagnement du CSP ni la contribution distincte pour défaut de sa proposition.",
       "Aucune charge nouvelle n'est identifiée : aucune convention, contribution, donnée ou déclaration de remplacement n'est créée par cet article. Les conventions anciennes et le CSP restent soumis à leurs obligations autonomes, sans rétablissement du versement patronal nouveau supprimé par les propositions L. 1233-68/69 et sans chiffrage d'un solde global.",
       [effect(n, 'coordination', 'crp-ancienne-codification-consolidation',
               "Clôture prospective du fondement CRP ancien sans réactivation, maintien des droits historiques et du CSP autonome.",
               "Source ancienne : proposition obligatoire de CRP dans son champ, financements et contributions de deux mois selon leurs conditions, avec accompagnement, DIF doublé et indemnités.",
               "Aucune nouvelle CRP ni contribution sur ce seul fondement après réforme ; anciennes situations légalement couvertes préservées et CSP actuel ouvert aux futurs bénéficiaires.",
               'regime', "Employeurs et salariés susceptibles de relever des anciennes CRP ; bénéficiaires futurs du CSP sous son fondement autonome.",
               "Entrée en vigueur de la loi ; aucune réactivation d'un régime déjà remplacé, droits et créances historiques conservés et sanctions non définitives plus douces réservées.",
               "Aucune obligation de remplacement ; le CSP n'est pas créé par cette abrogation et son financement nouveau suit les coordinations L. 1233-67/68/69.",
               source_p(n, 0), proposed_p(n, 0))])

n = 'L981-4'
impact(n, 'coordination_only',
       "L'ancienne ouverture au CDD n'est pas reprise comme fondement d'embauche nouvelle ; les missions et la professionnalisation s'inscrivent dans le contrat unique. La note officielle indique déjà l'abrogation de l'ancienne partie sauf le deuxième alinéa de cet article : cette clarification ne prouve pas une nouvelle obligation actuellement supprimée. L'affectation favorable des fonds est maintenue, avec distinction des anciens fonds et du fondement moderne L. 6325-24.",
       "La source réunit dans un seul paragraphe XML ce que sa note traite comme deux alinéas historiques. Les assiettes des anciens L. 951-1/L. 952-1 ne sont pas transposées automatiquement aux fonds actuels. Le rôle obligatoire de l'État dans l'accord moderne et la concordance des anciens fonds demeurent des limites à toute coupe supplémentaire non démontrée.",
       "Aucune charge nouvelle n'est identifiée : aucun prélèvement, registre, attestation ou signature individuelle n'est ajouté. L'accord de branche et l'État sont déjà requis par les fondements concernés ; la garantie d'emploi indéterminé relève du contrat unique et ne crée pas un terme pédagogique de remplacement. Aucun solde net intercodes n'est chiffré.",
       [effect(n, 'coordination', 'contrat-unique-duree-indeterminee',
               "Coordination de l'intérim en professionnalisation avec le contrat unique, sans extinction des facultés de financement.",
               "Première phrase de l'ancienne source : embauche en CDD sur anciens L. 981-1 à L. 981-3 et L. 122-2 ; portée actuelle limitée par la note d'abrogation de 2008.",
               "Emploi nouveau à durée indéterminée, missions et formation sans fin automatique ; anciens fonds et financement actuel des actions de formation maintenus dans leurs champs.",
               'regime', "Entreprises privées de travail temporaire et salariés intérimaires en professionnalisation.",
               "Nouveaux contrats à compter de la réforme du contrat unique ; droits et créances antérieurs préservés, sans nouveau CDD ni renouvellement.",
               "Aucun financement ou prélèvement de substitution ; accord de branche facultatif d'affectation des fonds maintenu selon ses fondements respectifs.",
               "Les entreprises de travail temporaire peuvent embaucher des personnes visées à l'article L. 981-1 dans les conditions définies aux articles L. 981-1 à L. 981-3 et sous le régime d'un contrat à durée déterminée conclu en application de l'article L. 122-2.",
               "Ni la fin d'une mission ni celle de la professionnalisation ne rompt automatiquement le contrat.")])

# Analyses propres aux trois cibles communes de contrat, préavis et indemnité.
common_checks = {
    'D6325-14': (
        "L. 1234-1 fixe dans sa proposition quinze jours de préavis pour l'emploi nouveau, sans ancienneté minimale. D. 6325-14 règle un salaire pendant la formation : ni le préavis ni sa notification ne conditionnent ce salaire ; les anciens contrats gardent leur durée de préavis.",
        "L. 1221-2 proposé interdit la fin automatique au terme d'une formation et tout nouveau CDD ou renouvellement. D. 6325-14 rattache donc le minimum salarial à l'action du CDI nouveau, sans transformer cette action en terme de l'emploi ; le CDD n'est cité que pour la transition ancienne.",
        "L. 1234-9 proposé ouvre l'indemnité ordinaire patronale à un an au terme effectif, préavis inclus, puis 0,20 mois par année totale, mois complets au prorata et six mois maximum. Ce seuil ne réduit aucun salaire de professionnalisation : D. 6325-14 ne crée pas de condition d'ancienneté salariale."
    ),
    'D6325-18': (
        "Le préavis de L. 1234-1 proposé concerne la rupture du nouveau contrat, indépendamment de l'ancienneté ; D. 6325-18 maintenu ne règle que le minimum salarial. Aucune notification de rupture ne conditionne le droit au plancher de 85 % pendant l'action de professionnalisation.",
        "L. 1221-2 proposé impose le CDI nouveau et distingue la phase de formation de la durée de l'emploi. D. 6325-18 ne mentionne aucun CDD ni terme automatique : son renvoi à L. 6325-9 suffit à conserver ce minimum dans le nouveau cadre, sans nouvelle modification stylistique.",
        "La condition d'un an au terme effectif et le barème de 0,20 mois, mois complets et plafond de six mois de L. 1234-9 concernent l'indemnité ordinaire de rupture. Ils ne sont pas une franchise sur le salaire garanti par D. 6325-18, dû même avant cet anniversaire."
    ),
    'D6331-72': (
        "L. 1234-1 proposé distingue quinze jours pour les nouveaux contrats et préavis antérieurs pour les anciens. Ces délais n'interviennent pas dans les exclusions du CPF-CDD ni dans sa suppression : celle-ci suit les périodes d'emploi et ne dépend pas d'une notification de rupture.",
        "L. 1221-2 proposé ferme les nouvelles conclusions et renouvellements de CDD ; il ne suffit pourtant pas à supprimer le CPF-CDD sur les rémunérations futures d'anciens contrats. D. 6331-72 les couvre expressément avec L. 6331-6 et garde les exonérations des périodes anciennes.",
        "Le seuil d'un an avec préavis et l'indemnité patronale de 0,20 mois par année totale de L. 1234-9 n'ont pas pour assiette la contribution CPF-CDD. D. 6331-72 ne soumet aucune exclusion ancienne ni aucun droit à formation au paiement de cette indemnité ou à l'ancienneté de rupture."
    ),
    'R6332-25': (
        "L. 1234-1 proposé organise le préavis individuel de l'emploi nouveau ; il n'abrège ni la durée pédagogique ni les périodes de prise en charge de R. 6332-25. Les avances et maintiens après rupture suivent leurs conditions propres, pas une formalité de notification de quinze jours au CFA.",
        "L. 1221-2 proposé interdit tout terme d'emploi lié à une formation. Les années, septième et dixième mois et prorata de R. 6332-25 visent donc la période d'apprentissage du CDI nouveau ; le terme des seuls contrats anciens demeure pertinent dans leur transition, sans nouveau CDD.",
        "L. 1234-9 proposé mesure un an au terme effectif, préavis inclus, et calcule 0,20 mois sur toute l'ancienneté reconnue. Ces conditions d'indemnité ordinaire ne limitent ni les avances OPCO ni les prises en charge avant signature et pendant six mois après rupture prévues par R. 6332-25."
    ),
    'R6332-25-1': (
        "Le préavis de quinze jours des contrats nouveaux dans L. 1234-1 n'est pas la période de quarante-cinq jours pratiques qui réduisait l'ancienne participation. R. 6332-25-1 abroge tout forfait pour les nouveaux contrats et conserve cette ancienne réduction dans son seul champ historique.",
        "L. 1221-2 proposé prohibe le CDD nouveau même si une phase d'apprentissage est limitée. La suppression de la participation s'attache à la conclusion du nouveau contrat, non à un prétendu terme d'emploi à la fin de la formation ; un nouveau contrat après rupture ne doit plus déclencher les 200 euros.",
        "La condition d'un an au terme effectif, le préavis inclus et les mois complets de L. 1234-9 sont étrangers aux forfaits d'apprentissage. Aucun employeur n'a à attendre cet anniversaire pour être libéré de la participation supprimée, et aucun droit de formation n'est lié à cette indemnité ordinaire."
    ),
    'R6332-25-2': (
        "L. 1234-1 proposé règle les quinze jours de préavis de l'emploi nouveau. La facture historique de participation reste liée aux quarante-cinq jours pratiques de L. 6222-18 dans son ancien champ, pas à la notification de ce préavis ; aucune facture de participation n'est due pour l'emploi nouveau.",
        "L. 1221-2 proposé rend indéterminée toute nouvelle embauche. Une fin de phase d'apprentissage ne déclenche ni nouvelle facturation patronale ni terme automatique de l'emploi au titre de R. 6332-25-2 ; les créances des contrats antérieurs conservent seulement leur liquidation propre.",
        "L. 1234-9 proposé fixe le seuil d'un an et le barème ordinaire patronal avec préavis inclus et prorata des mois complets. R. 6332-25-2 concerne une facture de financement de formation, non une indemnité de rupture : aucun de ces critères d'ancienneté ne conditionne sa suppression."
    ),
    'D7112-1': (
        "Le préavis de L. 1234-1 proposé est de quinze jours pour le contrat nouveau et reste ancien pour les contrats antérieurs. D. 7112-1 apprécie le seuil au terme effectif avec ce préavis ; le paiement malgré faute grave du préavis nouveau ne vaut pas ouverture de l'indemnité ordinaire dans ce même cas.",
        "L. 1221-2 proposé interdit le terme automatique des emplois nouveaux. D. 7112-1 traite donc la rupture patronale d'un CDI nouveau, préserve l'ancienneté en conversion convenue et répartit les périodes anciennes et futures sans remettre à zéro le service ni assimiler la clause spéciale du journaliste à une démission ordinaire.",
        "L. 1234-9 proposé impose un an au terme effectif préavis inclus, puis 0,20 mois par année totale sans retrancher la première, mois complets au prorata, plafond six mois et exception de faute grave. D. 7112-1 est corrigé sur ces mois complets ; les composantes anciennes et L. 7112-5 restent distinctes."
    ),
    'R7413-4': (
        "L. 1234-1 proposé maintient les durées et l'exception de faute grave des anciens contrats, mais fixe quinze jours payés même en cas de faute grave pour le contrat nouveau. R. 7413-4 cantonne donc son exception aux anciens contrats, sans ajouter une condition d'ancienneté aux quinze jours nouveaux.",
        "L. 1221-2 proposé impose le CDI aux embauches nouvelles et interdit qu'une tâche à domicile finisse automatiquement l'emploi. R. 7413-4 règle seulement la moyenne salariale du préavis de ce CDI ; aucune livraison, commande ou mission n'y devient un terme de contrat.",
        "L. 1234-9 proposé règle une indemnité ordinaire distincte, avec un an au terme effectif, 0,20 mois par année totale et plafond six mois. La moyenne des six mois de R. 7413-4 ne signifie ni six mois de préavis ni un plafond de préavis : son indemnité compensatrice reste due dans son champ propre avant un an."
    ),
    'L321-4-2': (
        "L. 1234-1 proposé réserve les quinze jours au contrat nouveau et maintient les préavis anciens. La CRP historique et le CSP accepté sont des dispositifs de rupture spéciaux ; l'abrogation de L. 321-4-2 ne leur applique pas mécaniquement quinze jours ni ne supprime leurs procédures collectives.",
        "L. 1221-2 proposé interdit les CDD nouveaux, mais une convention d'accompagnement n'est pas elle-même un contrat d'emploi. L'abrogation de l'ancienne CRP ne ferme pas le CSP autonome ; ses périodes de travail doivent rester en CDI nouveau sans terme lié à la durée de l'accompagnement.",
        "L. 1234-9 proposé distingue indemnité ordinaire nouvelle, droits anciens et indemnités spéciales. Le seuil d'un an à fin effective ne réduit pas rétroactivement les indemnités de L. 122-9 ancien réservées par L. 321-4-2 ; les nouvelles sommes du CSP suivent L. 1233-67 et son propre renvoi à cette cible."
    ),
    'L981-4': (
        "L. 1234-1 proposé impose quinze jours individuels aux nouveaux emplois privés sans supprimer protections et procédures autonomes. Les missions et enseignements de L. 981-4 ne déclenchent pas automatiquement ce préavis ni une rupture ; aucun renvoi au régime public n'est utilisé pour l'intérim privé.",
        "L. 1221-2 proposé interdit tout nouveau CDD, y compris par renouvellement, et toute fin automatique de mission ou de formation. L. 981-4 est coordonné sur ce point sans ressusciter sa première phrase ancienne, dont la note officielle ne maintient pas l'application générale après 2008.",
        "Le seuil d'un an au terme effectif, préavis inclus, puis 0,20 mois par année totale et mois complets de L. 1234-9 concernent la rupture patronale. Ils ne limitent ni l'accès à la professionnalisation intérimaire ni l'affectation favorable des fonds ; l'ancienneté n'est pas réinitialisée à chaque mission."
    ),
}

specific_checks = {
    'D6325-18': {
        'L6325-9': "Le texte officiel impose cumulativement SMIC et pourcentage du minimum de branche aux titulaires âgés d'au moins vingt-six ans. D. 6325-18 en fixe le pourcentage à 85 %, sans l'appliquer au SMIC. La proposition de la cible rattache la durée à l'action du contrat unique et préserve les anciens contrats ; aucun renvoi incohérent ne justifie de modifier ce plancher."
    },
    'D6331-72': {
        'L6321-9': "Le 6° de D. 6331-72 vise le CDD de formation d'un saisonnier dont la reconduction est promise. Pour les périodes anciennes, cette exclusion reste applicable. La proposition de L. 6321-9 maintient formation, rémunération de référence et abondement CPF dans le CDI futur : aucun terme d'emploi ni renouvellement de CDD ne renaît par l'exclusion ancienne.",
        'L6331-6': "La cible officielle institue le 1 % sur le revenu d'activité des CDD retenu pour cotisations et exclut formation, alternance et saisonniers. Sa proposition supprime la contribution sur les périodes de travail futures, même d'anciens CDD. L'abrogation de D. 6331-72 est limitée de la même manière ; exclusions et restitutions des périodes anciennes restent ouvertes."
    },
    'R6332-25': {
        'L6222-7-1': "Le troisième alinéa visé par le 2° du IV est la dérogation de durée pédagogique selon compétences ou expériences, avec convention tripartite, et non une rupture d'emploi. Sa proposition conserve six mois à trois ans, prolongations et adaptation au cycle. Le 10 % réglementaire et son plafond restent dans ce champ, sans faire de la fin du cycle un terme du CDI.",
        'L6222-18-2': "La cible impose la poursuite de la formation théorique et le statut de stagiaire pendant six mois après rupture, avec recherche d'un employeur. Le dernier alinéa du VI maintient les versements jusqu'au nouveau contrat ou à l'expiration de six mois ; ni l'ancienneté d'un an ni le préavis de quinze jours ne réduisent ce maintien favorable futur.",
        'R6332-25-2': "Le 4° du III exigeait une copie de la facture patronale de cette cible. Le texte de R. 6332-25 la retire comme condition du solde, même pour un contrat ancien dont la facture reste due. La proposition de la cible supprime la facture pour les nouveaux contrats seulement ; les factures de service réel et la preuve de réalisation gardent leur fonction autonome.",
        'L6332-14': "Le 1° du I fixe la prise en charge, mais sa vue officielle et sa proposition maintiennent encore la participation au niveau 6 et sa minoration, puis le III habilite le forfait ou prorata. Ces passages doivent être supprimés pour les contrats nouveaux en même temps que les règlements ; sinon la non-déduction serait incompatible avec la loi. Les 3° du I, aides et possibilités du II restent préservés, y compris pour futurs bénéficiaires."
    },
    'R6332-25-1': {
        'L6222-18': "Le deuxième alinéa source de R. 6332-25-1 vise les quarante-cinq premiers jours de formation pratique, non quarante-cinq jours calendaires ni quinze jours de préavis. La proposition de L. 6222-18 déplace ce premier alinéa historique après un nouveau paragraphe. La rédaction finale explicite donc les jours pratiques et vise la rédaction applicable au contrat antérieur, sans appliquer leur réduction à un contrat nouveau désormais exempt.",
        'L6222-18-2': "Le forfait de 200 euros vise le nouveau contrat avec un autre employeur après rupture, alors que L. 6222-18-2 garantit six mois de théorie et recherche d'employeur. Le texte supprime ce forfait si le nouveau contrat est postérieur à la réforme, même après rupture ancienne, sans supprimer le maintien de formation ni le statut de stagiaire des futurs cas éligibles.",
        'L6332-14': "L'obligation et la minoration figurent au 1° du I ; le III autorise participation proportionnelle plafonnée ou forfaitaire. La proposition fournie les conserve encore : une coordination législative expresse est indispensable, le règlement ne pouvant seul supprimer une obligation légale. Les niveaux de prise en charge et les aides futures ne sont pas réduits en compensation du retrait des 750/200 euros."
    },
    'R6332-25-2': {
        'L6222-18': "La facture ancienne était émise après les quarante-cinq premiers jours, consécutifs ou non, de formation pratique. Le premier paragraphe nouveau de la proposition de L. 6222-18 vise désormais le régime du CDI : il ne doit pas devenir l'échéance de facturation des contrats anciens. La rédaction finale explicite ces jours et vise la rédaction applicable au contrat antérieur ; aucune facture n'est recréée pour un contrat nouveau.",
        'R6332-25': "Le 4° du III source exigeait une copie de la facture patronale pour le solde OPCO. La proposition de cette cible retire cette copie et la déchéance de quatre mois ; la révision présente maintient cette coupe, y compris pour la participation encore facturable des anciens contrats. La facture de formation et la preuve du service fait restent distinctes et ne rétablissent pas la participation.",
        'L6332-14': "La facture n'est que l'exécution de la participation et de la minoration du 1° du I, complétées par le III. La vue proposée de la cible les maintient encore : il faut les retirer dans la loi pour les contrats nouveaux afin que la suppression de facture soit cohérente. L'absence de cette facture ne doit pas supprimer les prises en charge légales futures ni créer une facture équivalente."
    },
    'D7112-1': {
        'L7112-5': "La cible distingue trois ruptures par le journaliste : cession, cessation de publication, changement portant atteinte à l'honneur, à la réputation ou aux intérêts moraux. Sa proposition conserve l'indemnité spéciale d'un mois des derniers appointements par année ou fraction et la dispense de préavis du seul 3°. D. 7112-1 les exclut du seuil d'un an et du plafond ordinaire de six mois, pour les contrats futurs aussi.",
        'L7112-3': "La source législative fixe un mois des derniers appointements par année ou fraction, maximum quinze ; sa proposition renvoie le nouveau contrat à L. 1234-9 mais garde encore le régime entier des anciens contrats. La transition générale à deux composantes exige donc de compléter cette cible pour les services futurs des anciens contrats : D. 7112-1 ne peut à lui seul abaisser leur minimum légal.",
        'L7112-4': "La commission arbitrale intervient au-delà de quinze ans, ainsi que pour réduction ou suppression en cas de faute grave ou de fautes répétées dans son champ. Sa proposition conserve sa compétence pour l'indemnité spéciale et les composantes anciennes. Le plafond de six mois de l'ordinaire nouveau ne doit donc pas limiter cet arbitrage ni transformer quinze ans en extinction d'une créance acquise."
    },
    'R7413-4': {
        'L1234-2': "La cible proposée rend non écrites les clauses de durée différente des quinze jours du nouveau contrat, mais distingue dispense d'exécution, terme et sommes dues. R. 7413-4 ne crée pas de durée spéciale de six mois : cette durée reste seulement une moyenne de salaires, avec les clauses favorables et l'ancien droit dans leur champ transitoire.",
        'L1234-3': "La proposition compte les quinze jours à partir du lendemain de la présentation de la lettre au salarié ou, si un autre mode est légalement admis, de sa réception ou remise ; côté salarié, du lendemain de la réception de sa notification écrite par l'employeur. Le brouillon de R. 7413-4 disant seulement « à compter de sa notification » est corrigé pour éviter un jour de moins.",
        'L1234-4': "L'inexécution du préavis n'avance pas la date de fin ; la proposition réserve la fin d'essai et les protections ou dispositifs collectifs distincts. R. 7413-4 conserve cette articulation : le salaire moyen n'autorise pas une fin immédiate du contrat ni la confusion de la compensation de préavis avec l'indemnité ordinaire conditionnée à un an.",
        'L1234-5': "La cible proposée paie le préavis nouveau malgré faute grave lorsque l'employeur en dispense l'exécution ou ne respecte pas les quinze jours, sans payer automatiquement un travail refusé par le salarié. Elle garde l'exception ancienne. R. 7413-4 aligne son exception sur cette transition ; la nouvelle obligation de paiement est expressément recensée, sans la qualifier d'allègement.",
        'L1234-6': "La fermeture ou réduction d'horaire déclenche dans cette cible une référence au temps plein légal ou conventionnel, ou au temps partiel contractuel. La moyenne des six mois de R. 7413-4 ne vaut pas abrogation de ce correctif dans ses cas propres et ne permet pas de baisser le salaire contractuel d'un travailleur à domicile ; aucune durée de préavis n'en est déduite.",
        'L1234-7': "La cessation d'entreprise ne dispense pas du préavis ; la proposition réserve la véritable force majeure régie séparément. R. 7413-4 ne transforme donc pas la faute grave ou la fermeture en disparition de l'indemnité du contrat nouveau et ne prétend pas supprimer les règles autonomes de force majeure, ni les procédures collectives de rupture.",
        'L1237-1': "La proposition fixe à quinze jours la démission du contrat nouveau, notifiée et calculée selon L. 1234-3, sans indemnité ordinaire et avec dispenses particulières préservées. R. 7413-4 conserve ces dispenses ; la moyenne salariale du préavis ne crée pas une indemnité de démission ni le paiement automatique d'une inexécution voulue par le salarié.",
        'L1234-8': "La cible proposée écarte toute ancienneté minimale pour le préavis nouveau et maintient, pour les anciens contrats, la continuité pendant suspension avec l'exception favorable des élus locaux pour la durée comptée. R. 7413-4 conserve les règles anciennes dans leur champ et ne fait pas des six mois de référence un seuil d'ancienneté ni une exclusion des suspensions."
    },
    'L321-4-2': {
        'L1233-67': "Le CSP actuel rompt l'emploi à l'adhésion, protège indemnité de rupture, CPF et statut de stagiaire, et impose douze mois de contestation seulement si ce délai est indiqué dans la proposition. Sa vue proposée distingue anciennes et nouvelles adhésions et verse directement au salarié le préavis de référence sans déduire un financement supprimé. L'abrogation de la CRP ne ferme ni ces droits futurs ni leur recours.",
        'L1233-68': "Le 3° officiel organise des périodes de travail en CDD ou mission ; sa proposition les coordonne au CDI nouveau, sans terme lié à l'accompagnement. Le b du 10° proposé réserve le versement de financement aux adhésions anciennes. La réserve générale du CSP dans L. 321-4-2 ne rétablit donc ni nouveau CDD ni versement patronal supprimé, tandis que les allocations et formations demeurent.",
        'L1233-69': "La proposition supprime le versement patronal de financement pour les adhésions nouvelles et conserve anciennes créances, aides et concours publics, sans supprimer la contribution distincte pour défaut de proposition. L. 321-4-2 ne doit pas réintroduire ce versement via ses anciens deux mois de salaire ou une référence générique au financement : ses contributions ne survivent que pour des dettes anciennes légalement nées."
    },
    'L981-4': {
        'L6325-23': "La cible officielle permet le CDD de professionnalisation intérimaire ; sa proposition le remplace par le CDI avec action pédagogique et activités en mission, garanties d'intermission conservées. L. 981-4 ne réactive pas son ancien L. 122-2 : fin de mission et fin de formation ne rompent pas l'emploi nouveau et une conversion ne remet pas l'ancienneté à zéro.",
        'L1251-57': "La cible assimile aux missions les stages, bilans et VAE et les formations liées à l'activité, à l'initiative de l'employeur ou du salarié selon les voies prévues. Sa proposition conserve ces assimilations aux emplois futurs. Le financement évoqué par L. 981-4 et L. 6325-24 garde ainsi cet objet autonome sans transformer la durée d'une action ou d'un congé en terme du contrat.",
        'L6325-3': "La cible exige une formation qualifiante ou des blocs de certification et un emploi en relation avec l'objectif, puis travail et suivi par le salarié. Sa proposition distingue action du CDI nouveau et contrat ancien. L. 981-4 renvoie bien à ces obligations essentielles dans le travail temporaire, sans imposer un nouvel essai ni un terme à la fin de la professionnalisation et sans fermer les avantages futurs."
    }
}

common_numbers = ('L1234-1', 'L1221-2', 'L1234-9')
for number, a in answers.items():
    required = references['requirements'][a['code_id'] + '|' + a['source_id']]
    analyses = dict(zip(common_numbers, common_checks[number]))
    analyses.update(specific_checks.get(number, {}))
    checks = []
    for key in required:
        target = references['targets'][key]
        assessment = analyses.pop(target['number'])
        assert len(assessment) >= 80
        checks.append(dict(target_key=key, view_sha256=target['view_sha256'], assessment=assessment))
    assert not analyses, (number, analyses)
    a['reference_checks'] = checks

Path('answer.json').write_text(json.dumps(list(answers.values()), ensure_ascii=False, indent=2) + '\n')
print('answer.json :', len(answers), 'articles ;', sum(len(a['reference_checks']) for a in answers.values()), 'renvois obligatoires.')
