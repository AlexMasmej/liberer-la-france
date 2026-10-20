import json
import re
from html import unescape
from html.parser import HTMLParser
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
targets_by_number = {v['number']: (k, v) for k, v in refs['targets'].items()}
answer = []
for s in sources:
    d = {k: s[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}
    d.update({k: s['previous_draft'][k] for k in ['proposed_xml', 'reason', 'review_notes']})
    d['status'] = 'rewrite_draft'
    answer.append(d)
by_number = {d['number']: d for d in answer}
source_by_number = {s['number']: s for s in sources}

def paragraphs(*items):
    return '\n'.join('<p>' + t + '</p>' for t in items)

def update(n, **kw):
    by_number[n].update(kw)

def reduction(n, *removed):
    update(n, change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19', removed_provisions=list(removed))

update('L1235-15', proposed_xml=None, status='retained_unchanged',
       reason="Après lecture intégrale de la source et du brouillon, maintien nécessaire du texte officiel plutôt qu'une nouvelle reformulation. La réparation d'au moins un mois de salaire brut sanctionne l'absence de représentation collective lorsque l'employeur devait organiser le CSE et ne dispose pas d'un procès-verbal de carence. Les deux conditions évitent de sanctionner une élection régulièrement tentée mais infructueuse. Supprimer le procès-verbal ou la sanction affaiblirait la preuve et l'effectivité de cette protection essentielle ; aucune taxe, déclaration périodique, autorisation ou pièce redondante n'est imposée par cet article. Le brouillon antérieur n'apportait qu'un changement de rédaction, sans réduction normative à conserver.",
       review_notes="Les deux alinéas de la source sont maintenus intégralement. Les conditions restent cumulatives ; le minimum est un mois de salaire brut, sans absorption des indemnités de licenciement et de préavis. La sanction est une réparation d'illégalité, indépendante de l'indemnité ordinaire : le seuil d'un an et le plafond de six mois de L. 1234-9 proposé ne s'y appliquent pas. L. 1234-1 proposé conserve les procédures collectives même pour les nouveaux contrats soumis à quinze jours de préavis. Le calcul du préavis nouveau relève de L. 1234-3, consulté dans le corpus public, hors des cibles fournies ; le présent article n'en crée pas de renvoi. Aucune suppression supplémentaire n'est justifiée dans ce champ et aucun effet de simplification n'est revendiqué.")

update('L1235-16',
       reason="La comparaison à la source officielle entière confirme la réduction déjà inscrite au brouillon : l'employeur n'a plus à communiquer une seconde fois la même décision complète au même salarié qui l'a déjà reçue avec date certaine. Aucun certificat de substitution n'est demandé. Le reste est maintenu à droit constant : réintégration consentie avec avantages acquis, indemnité minimale des six derniers mois, nouvelle décision administrative motivée sous quinze jours et effets de cette seule régularisation. Une coupe supplémentaire du contrôle du plan ou de l'information effective des salariés retirerait une protection ou un recours ; elle n'est pas retenue.",
       review_notes="Quatre alinéas maintenus, notamment le renvoi du premier au dernier. L. 1233-57-2, L. 1233-57-3 et L. 1235-10 ont été consultés intégralement dans le corpus public : validation de l'accord, homologation du document et nullité pour absence ou insuffisance du PSE restent distinctes. La dispense ne concerne que l'information future déjà effectivement délivrée, avec date certaine, au même salarié ; une omission passée et les créances ou recours correspondants ne sont pas effacés. Le délai de quinze jours court de la notification du jugement à l'administration et ne constitue pas le préavis individuel. Le minimum de réparation de six mois n'est pas un plafond et ne dépend pas de l'ancienneté d'un an ; l'indemnité ordinaire de L. 1234-9 reste distincte avec sa transition. Les cibles hors du fichier de renvois ont été lues localement et ne sont pas présentées comme réécrites.")
reduction('L1235-16', "Obligation pour l'employeur d'adresser de nouveau la même décision complète à un salarié qui l'a déjà reçue avec date certaine, notamment de l'administration.")

update('L1236-7', proposed_xml=paragraphs(
    "Lorsque l'employeur prend l'initiative de rompre le contrat conclu pour une mission à l'exportation dans le champ de l'article L. 1223-5, la rupture relève des dispositions du chapitre II relatives au licenciement pour motif personnel.",
    "Pour les contrats conclus à compter de l'entrée en vigueur de la loi instituant le contrat de travail unique, l'emploi est à durée indéterminée. La fin de la mission à l'exportation ne rompt pas automatiquement le contrat. L'employeur qui entend le rompre respecte les règles de rupture applicables au contrat unique, le contrôle du motif et les garanties propres à la mission, notamment celles de l'article L. 1223-6. Le préavis individuel est de quinze jours calendaires, calculés dans les conditions de l'article L. 1234-3 ; il ne tient pas lieu des autorisations ou procédures distinctes légalement requises.",
    "Les contrats conclus avant cette entrée en vigueur conservent leurs conditions de recours et leurs garanties propres à la mission, sous réserve des dispositions transitoires de l'article L. 1234-9 relatives au calcul de l'indemnité légale. Une conversion convenue en contrat unique conserve toute l'ancienneté et les créances acquises, sans compter deux fois une même période dans le calcul d'une même indemnité. Le minimum spécial de l'article L. 1223-6 reste ouvert sans condition d'ancienneté. Les indemnités spéciales et les garanties conventionnelles ou contractuelles plus favorables restent applicables dans leur champ."),
    reason="Coordination du renvoi à la procédure de licenciement personnel avec le contrat unique, en conservant les acquis du brouillon. La durée de la mission ne termine pas l'emploi nouveau ; le préavis individuel est rattaché à sa règle de notification. La dérogation de L. 1223-5 au licenciement économique et les garanties spéciales de L. 1223-6 subsistent. Aucune suppression autonome ne peut être déduite de cet article de procédure : le contrôle du motif, la défense du salarié et le recours sont nécessaires. La précision de transition évite de promettre le maintien intégral de l'ancien calcul ordinaire alors que L. 1234-9 distingue les périodes de service.",
    review_notes="Les sources et propositions complètes de L. 1223-5 et L. 1223-6 ont été lues dans reference-targets.json : mission en majeure partie hors du territoire national, retrait proposé de l'accord collectif préalable, suppression proposée du minimum de six mois de mission et indemnité spéciale sans ancienneté minimale. Ce sont des propositions, non le droit en vigueur. Le présent article ne recrée ni accord préalable ni durée minimale. Le 3° de L. 1223-6 proposé vise 0,20 mois par année totale et six mois pour le seul minimum nouveau ; ses mots 'au prorata' doivent être coordonnés avec les mois complets de R. 1234-1, sans prorata journalier. L. 1234-3, absent des cibles fournies, a été lu intégralement dans le corpus public pour le nouveau renvoi : quinze jours à partir du lendemain de la présentation ou réception de la notification écrite. Les règles antérieures de préavis demeurent pour les contrats anciens, et la part indemnitaire antérieure reste protégée sans double compte. Aucun régime d'agent public n'est modifié.")

update('L1237-3',
       reason="Maintien des deux suppressions de fond du brouillon après comparaison à tous les cas de la source : retrait de la solidarité du nouvel employeur fondée sur sa seule connaissance d'un contrat précédent, à l'embauche ou pendant la poursuite de l'emploi. Cette responsabilité sans intervention démontrée dans l'abus entrave la mobilité. Le cas du 1°, exigeant une intervention prouvée dans une rupture abusive et un dommage, reste nécessaire contre la participation à l'abus. La responsabilité du salarié et les fautes personnelles distinctes demeurent réparables. Aucune suppression supplémentaire n'est retenue de ces protections ; aucun nouveau CDD n'est autorisé.",
       review_notes="Les 1°, 2° et 3° restent repérables ; les deux derniers sont abrogés pour les faits générateurs nouveaux. Leurs exceptions anciennes (terme du CDD, expiration du préavis, quinze jours écoulés lors de l'avertissement) ne sont pas fermées pour les faits antérieurs : leur régime entier reste applicable. Pour les faits nouveaux, la suppression des cas correspondants rend ces exceptions inutiles et plus aucune solidarité n'est encourue pour la seule connaissance. Le délai de quinze jours de l'ancien 3° n'est pas le nouveau préavis individuel. L. 1237-2 a été consulté dans le corpus public, hors des cibles fournies pour ce renvoi conservé : il répare seulement la rupture abusive à l'initiative du salarié. Le texte n'écarte ni loyauté, non-concurrence valable, règles de durée du travail, ni faute distincte. L'ancienneté d'un an et l'indemnité patronale de L. 1234-9 ne conditionnent pas cette responsabilité.")
reduction('L1237-3',
          "Solidarité du nouvel employeur du seul fait d'avoir embauché un salarié qu'il savait encore lié par un contrat à un précédent employeur, ancien 2°.",
          "Solidarité du nouvel employeur pour la seule poursuite de l'emploi après connaissance du contrat précédent et mécanisme d'avertissement et de délais de l'ancien 3°.")

update('L1237-9',
       reason="La réduction du brouillon est conservée après examen des quatre alinéas officiels : l'accès volontaire à l'affectation de l'indemnité de retraite au maintien de rémunération ne dépend plus de l'existence préalable d'un accord collectif ; les parties peuvent la convenir directement à défaut. Il n'est créé ni agrément ni déclaration. La demande du salarié, l'accord de l'employeur, le temps réduit de fin de carrière et le versement du reliquat restent nécessaires pour préserver l'option favorable. Les trois premiers alinéas restent à droit constant. Supprimer l'indemnité, son calcul protecteur ou son reliquat ne serait pas une suppression de formalité et retirerait un droit spécial expressément conservé.",
       review_notes="Quatre alinéas ; le dernier reste la cible de la réserve du troisième. D. 1237-1 et D. 1237-2, consultés en entier dans le corpus public, maintiennent les minima d'un demi-mois après dix ans, d'un mois après quinze ans, d'un mois et demi après vingt ans et de deux mois après trente ans, avec la référence la plus favorable entre douzième des douze derniers mois et tiers des trois derniers mois et primes proratisées. L'unicité de l'indemnité, la pension de droit propre et le régime de base de l'emploi occupé restent inchangés. L. 1237-7 distingue la mise à la retraite ; L. 1237-10, également lu, renvoie au préavis de L. 1234-1 sans transformer le départ volontaire en rupture patronale. L'indemnité spéciale n'est pas soumise au seuil d'un an, au taux de 0,20 mois ou au plafond de six mois de l'indemnité ordinaire. La faculté directe reste ouverte aux futures situations éligibles ; aucune affectation déjà convenue n'est réduite. Les cibles réglementaires hors du fichier ont été vérifiées localement, sans modification de leurs fichiers.")
reduction('L1237-9', "Condition d'existence préalable d'un accord collectif pour convenir, à la demande du salarié et avec l'employeur, de l'affectation de l'indemnité de retraite au maintien de rémunération.")

update('L1237-15',
       reason="La suppression acquise au brouillon du jour d'attente après autorisation est maintenue pour les conventions nouvelles du premier alinéa. La date convenue peut être le jour de l'autorisation, après le délai de rétractation, sans demande supplémentaire. L'autorisation indépendante et l'avis médical préalable sont conservés : ils protègent la représentation collective et l'indépendance du médecin du travail et ne sont pas doublonnés par une homologation ordinaire. Les renvois procéduraux sont maintenus à droit constant. Le nouveau préavis individuel ne justifie pas leur suppression ; aucune autre coupe de ces garanties essentielles n'est retenue.",
       review_notes="Deux alinéas et les trois ensembles procéduraux du premier sont conservés. L. 2411-1 et L. 2411-2 ont été consultés intégralement : mandats légaux, conventionnels et protections même en procédure collective. L. 1237-11, L. 1237-12 et L. 1237-14 ont aussi été lus : consentement libre, assistance et régime ordinaire d'homologation restent distincts. Ici l'autorisation remplace cette homologation, sans seconde demande ni transposition de son acceptation tacite ou de ses quinze jours ouvrables. Les quinze jours calendaires de rétractation de L. 1237-13 ne sont pas le préavis. La règle nouvelle est limitée aux conventions conclues après l'entrée en vigueur ; elle n'avance pas la date convenue et n'efface pas un obstacle légal ou juridictionnel autonome. L. 1237-18-4 et L. 1237-19-2, lus localement, gardent leur lendemain d'autorisation pour leurs ruptures distinctes. Le 2e alinéa conserve son autorisation et son avis sans assimilation. R. 4745-2, lu, doit être coordonné avec les obligations subsistantes ; son renvoi ne peut rétablir le jour retiré. Le minimum spécifique de L. 1237-13 reste sans seuil d'un an, avec protection de la part antérieure ; ses règles de notification de rétractation restent entières.",
       benefit_review="L'accès des salariés protégés à la rupture conventionnelle est conservé pour les conventions futures comme antérieures. La dérogation à l'homologation ordinaire maintient une seule autorisation de l'inspecteur, sans double procédure ; la dérogation de date devient plus favorable dans le nouveau champ. L'autorisation pour les titulaires de mandats, celle des médecins du travail et l'avis du médecin inspecteur préservent leurs protections. La rétractation, le consentement libre et l'indemnité spécifique restent applicables ; les conventions antérieures gardent leurs droits et leur régime de date.")
reduction('L1237-15', "Attente légale jusqu'au lendemain de l'autorisation de l'inspecteur, pour les conventions nouvelles relevant du premier alinéa, après rétractation et à la date convenue.")

def special_indemnity(subject):
    return (f"Le renvoi au barème de l'article L. 1234-9 pour fixer ce minimum ne soumet pas {subject} à la condition d'un an propre à l'indemnité ordinaire de rupture. Pour un contrat unique conclu à compter de l'entrée en vigueur de la loi instituant ce contrat, le minimum est calculé à 0,20 mois de salaire brut de référence par année totale d'ancienneté, au prorata des mois complets pour une année incomplète, dans la limite de six mois de ce salaire, sans retrancher la première année. Pour les contrats antérieurs, la composante correspondant aux services accomplis avant cette entrée en vigueur conserve son régime et ses minima ; elle s'ajoute à la composante correspondant aux services postérieurs, calculée à 0,20 mois par année avec le même prorata et seule plafonnée à six mois. Toute l'ancienneté est conservée sans double compte d'une même période. Les indemnités déjà convenues et les garanties conventionnelles ou contractuelles plus favorables ne sont pas diminuées ni plafonnées par ce minimum légal.")

d = by_number['L1237-18-2']
parts = re.findall(r'<p>(.*?)</p>', d['proposed_xml'], flags=re.S)
parts[-1] = "7° Les indemnités de rupture garanties au salarié. Leur montant ne peut être inférieur à celui des indemnités légales dues en cas de licenciement pour motif économique. " + special_indemnity("l'indemnité spécifique de départ d'un commun accord")
d['proposed_xml'] = paragraphs(*parts)
update('L1237-18-2',
       reason="Le retrait des doubles informations du brouillon reste une réduction de fond par rapport au 6° officiel : les mêmes représentants n'ont pas à recevoir les mêmes données déjà effectivement communiquées. Les nouveautés et compléments restent dus. Les sept thèmes du congé volontaire et rémunéré sont conservés car ils rendent effectifs le consentement, la formation, la rémunération et l'indemnité spéciale. Le 4° distingue la durée des activités de celle de l'emploi nouveau. Le 7° est précisé selon les cibles fournies : minimum spécial sans seuil d'un an, calcul sur toute l'ancienneté avec mois complets, plafond de la seule part nouvelle et part antérieure protégée. Aucune suppression supplémentaire de ces droits n'est retenue.",
       review_notes="Les 1° à 7° demeurent à leur place. L. 1237-17, L. 1237-18 et L. 1237-18-3 à L. 1237-18-5 ont été lus dans le corpus public, en plus des cibles fournies. La rupture volontaire du contrat support reste régie par L. 1237-18-4 ; le nouvel emploi accompli pendant le congé suit L. 1237-18-1, dont la proposition interdit de nouveaux CDD et conserve le reliquat de congé selon l'accord. Il ne s'agit pas d'une extinction automatique de l'emploi de reprise à la fin de sa formation. Au 6°, la dispense exige que chaque destinataire ait réellement reçu les données ; aucun registre ou certificat nouveau n'est requis. Au 7°, le nouveau minimum ne reprend ni la condition d'un an ni une exclusion pour faute d'une indemnité spéciale de départ consenti. R. 1234-1, R. 1234-2 et R. 1234-4 ont été lus localement : mois complets, distinction chronologique des services et salaire de référence le plus favorable demeurent à coordonner dans leur champ propre. L. 1237-18-3 conserve rémunération minimale et régime social favorable pour douze mois, pouvant être portés à vingt-quatre en reconversion, y compris pour les futurs bénéficiaires. La note de l'ordonnance de 2017 concerne l'entrée en vigueur historique au plus tard le 1er janvier 2018 ; elle ne date pas cette réforme. Les cibles complémentaires hors du fichier ne sont pas présentées comme réécrites ici.")
reduction('L1237-18-2', "Répétition des mêmes informations aux mêmes représentants déjà effectivement informés dans leurs attributions, sans certificat, registre ou transmission de remplacement.")

d = by_number['L1237-19-1']
parts = re.findall(r'<p>(.*?)</p>', d['proposed_xml'], flags=re.S)
parts[4] = "4° Les modalités de présentation et d'examen des candidatures des salariés au départ. Pour les conventions individuelles conclues à compter de l'entrée en vigueur de la loi portant la présente réforme, le consentement écrit du salarié au dispositif est exprimé dans la convention individuelle de rupture mentionnée au 4° bis ou, le cas échéant, au 4° ter, sans transmission préalable d'un accord écrit distinct. Par dérogation au premier alinéa de l'article L. 1237-19-2, la seule acceptation d'une candidature par l'employeur n'emporte pas rupture du contrat : celle-ci suppose la conclusion de cette convention et le respect du droit de rétractation applicable. La candidature seule ne vaut pas consentement à la rupture ;"
parts[7] = "5° Les modalités de calcul des indemnités de rupture garanties au salarié. Leur montant ne peut être inférieur à celui des indemnités légales dues en cas de licenciement. " + special_indemnity("l'indemnité spécifique de rupture conventionnelle collective").rstrip('.') + " ;"
d['proposed_xml'] = paragraphs(*parts)
update('L1237-19-1',
       reason="Le consentement au dispositif est regroupé dans la convention individuelle déjà requise aux 4° bis ou 4° ter : suppression, conservée du brouillon, de l'écrit préalable distinct et de sa transmission. L'article entier maintient le nombre maximal de départs, la durée du dispositif, l'examen et le départage des candidatures, la rétractation, les mesures d'accompagnement et le suivi. Le 4° coordonne expressément l'acceptation de candidature de L. 1237-19-2, qui ne doit pas produire une rupture avant la convention exprimant le consentement. Le 5° précise le minimum spécial sans seuil d'un an et la protection des services antérieurs. Les garanties collectives conservées n'ont pas de doublon retiré démontré au-delà de cet écrit ; aucune coupe supplémentaire de ces protections n'est retenue.",
       review_notes="Tous les numéros demeurent, notamment 4° bis, 4° ter, 7° bis et 8°, ainsi que l'alinéa historique final. Le nouveau renvoi au premier alinéa de L. 1237-19-2 n'est pas une cible fournie : cet article a été lu en entier dans le corpus public, source et proposition, qui font encore produire la rupture par la seule acceptation de candidature ; une réécriture coordonnée y est indispensable pour reproduire la dérogation du 4°. Ses autorisations pour salariés protégés et médecins demeurent. L. 1237-19 et L. 1237-19-3 à L. 1237-19-5, L. 1237-19-7, L. 1237-19-8, D. 1237-9 et D. 1237-12 ont aussi été lus : validation, dossier, bilan et recours restent dans leur champ ; ils ne doivent pas réclamer l'écrit distinct supprimé. La convention individuelle n'est pas créée par la réforme : elle figurait déjà aux 4° bis et 4° ter. Le 5° protège la part antérieure sans la plafonner à six mois ; seul le minimum nouveau est plafonné, avec années totales et mois complets, sans condition d'un an. R. 1234-1, R. 1234-2 et R. 1234-4 ont été consultés localement. L. 6324-1 et le II de L. 6324-9 préservent qualification, rémunération, frais pédagogiques et accord à la mobilisation du CPF. Les actions dont l'avenant a été conclu avant le 1er janvier 2026 gardent leur transition légale. La note du II de l'article 11 de la loi 2025-989 concerne sa seule entrée en vigueur au 1er janvier 2026 ; l'alinéa de 2017 n'est pas une date de la présente réforme. La durée d'une action ne termine aucun emploi nouveau et aucun renvoi n'impose de nouveau l'attente de trois mois retirée dans L. 6324-9 proposé.")
reduction('L1237-19-1', "Écrit d'adhésion au dispositif distinct de la convention individuelle de rupture et transmission préalable de cet écrit, pour les conventions nouvelles.")

update('L1251-4', proposed_xml=None, status='retained_unchanged',
       reason="Maintien nécessaire de la source entière après examen de ses trois alinéas et du brouillon stylistique. Le 1° autorise le placement privé et le 2° le travail à temps partagé, par dérogation à l'exclusivité de L. 1251-2. Ces deux ouvertures favorables ne créent ni formalité, ni taxe, ni autorisation supplémentaire. Les supprimer restreindrait l'activité des entreprises ; leur bénéfice doit aussi rester accessible aux entreprises futures. Le principe d'exclusivité figure dans un autre article : sa suppression ne peut être déduite d'une réécriture de ces seules dérogations. Aucun changement stylistique nouveau n'est fabriqué et aucune simplification n'est comptée.",
       review_notes="Le renvoi à L. 1251-2 et les numéros 1° et 2° restent intégraux. La cible fournie L. 1251-2 conserve l'exclusivité dans sa proposition et coordonne l'emploi intérimaire nouveau en contrat unique avec garanties d'intermission. L. 5321-1 et L. 1252-1, L. 1252-2, L. 1252-4 ont été lus intégralement dans le corpus public : le placement rapproche offres et demandes sans faire du placeur une partie à l'emploi ; le travail à temps partagé est une activité distincte, dont le contrat est déjà réputé à durée indéterminée. La conservation de ces activités ne permet ni nouveau CDD, ni disparition des garanties salariales applicables à l'intérim, ni assimilation des utilisateurs publics à des employeurs privés. Aucune cible nouvelle n'est introduite ; les fichiers publics lus n'ont pas été modifiés.",
       benefit_review="Les deux avantages possibles sont les dérogations à l'exclusivité permettant, au 1°, le placement privé de L. 5321-1 et, au 2°, l'activité d'entreprise de travail à temps partagé. La source entière est conservée : les deux activités restent accessibles aux entreprises et opérations futures entrant dans leur champ, sans agrément, pièce ou condition nouvelle. Les droits attachés au travail à temps partagé et au contrat indéterminé conservent leurs fondements propres.")

update('L1251-5',
       reason="La source entière interdit le pourvoi durable d'un emploi permanent de l'utilisateur, par l'objet ou l'effet de la mission, quel qu'en soit le motif. Cette protection est conservée : l'emploi indéterminé auprès de l'agence ne justifie pas une affectation permanente abusive auprès du client. La proposition antérieure est maintenue comme coordination avec le contrat unique, sans revendiquer une réduction autonome. Les garanties d'intermission et la transition des contrats déjà conclus empêchent qu'un renvoi à la lettre de mission ne réintroduise un CDD. Aucune déclaration, autorisation ou durée minimale n'est créée par la règle source et aucune coupe supplémentaire n'est justifiée.",
       review_notes="L'alternative objet ou effet, l'activité normale et permanente et l'indifférence du motif restent entières au premier alinéa. L. 1251-58-2 et L. 1251-58-3 fournis conservent congés, ancienneté et garantie mensuelle, qui ne doivent pas être confondus avec un terme de mission. L. 1251-1, L. 1251-12, L. 1251-40 et L. 1251-58-1, L. 1251-58-4 à L. 1251-58-6 ont été lus dans le corpus public : la lettre constate l'affectation, la dispense de durée totale subsiste, et le salarié conserve les droits envers l'utilisateur en cas de recours illicite, même s'il est déjà employé à durée indéterminée par l'agence. La proposition de L. 1251-40 consultée distingue déjà ces deux employeurs et les périodes historiques, mais ne vaut pas droit en vigueur. Le passage obligatoire à l'emploi indéterminé étend aux anciens recrutements en mission des garanties qui ont un coût pour l'agence ; le présent renvoi n'est pas une seconde réduction. La directive 2008/104/CE et les règles d'utilisateurs publics demandent une coordination distincte ; aucun texte européen n'a été consulté à l'extérieur ni sa compatibilité réputée acquise.")

d = by_number['L1251-7']
p = d['proposed_xml']
p = p.replace("2° Lorsque l'entreprise de travail temporaire et l'entreprise utilisatrice s'engagent à assurer au salarié un complément de formation professionnelle, pour une durée et dans des conditions fixées par décret ou par accord de branche étendu ;", "2° Lorsque l'entreprise de travail temporaire et l'entreprise utilisatrice s'engagent à assurer au salarié un complément de formation professionnelle. Ce cas de mise à disposition est ouvert sans qu'un décret ou un accord de branche étendu doive en fixer préalablement la durée et les conditions. Les règles de fond applicables à la formation, les stipulations conventionnelles plus favorables et les engagements de formation déjà convenus demeurent applicables ;")
p = p.replace("Les suppressions de l'habilitation préalable du 1° et de la durée minimale du 5°", "Les suppressions des préalables normatifs des 1° et 2° et de la durée minimale du 5°")
d['proposed_xml'] = p
update('L1251-7',
       reason="Les réductions du brouillon sont conservées : le 1° ne dépend plus d'une disposition légale spéciale ou d'un accord étendu, et le 5° n'impose plus un mois de mission d'insertion. Une coupe supplémentaire est opérée au 2° : l'engagement de complément de formation des deux entreprises suffit à ouvrir le cas de recours, sans attendre qu'un décret ou un accord de branche étendu en fixe la durée et les conditions. Ce préalable ne démontre pas une fonction essentielle distincte des obligations de formation maintenues ; aucun agrément, déclaration ou document ne le remplace. Les cinq voies favorables, le cadre qualifiant de l'apprentissage et les droits d'insertion sont conservés, avec l'emploi nouveau à durée indéterminée. Cette fusion des formes d'emploi étend aussi des obligations de maintien d'emploi et de rémunération : elle n'est pas présentée comme une baisse nette démontrée des charges.",
       review_notes="Les 1° à 5°, les conteneurs des 1° et 2° et le regroupement des 4° et 5° demeurent. Le préalable retiré au 2° est un encadrement normatif obligatoire du cas de recours, non un agrément administratif individuel ; les obligations légales et garanties de formation restent applicables, sans nouveau dossier. Aucun décret d'application de ce seul préalable n'a été identifié dans les articles D/R1251 du corpus consulté : cela ne prouve pas l'absence d'accords de branche ou de textes extérieurs. Le 12° de L. 2253-1, lu source et proposition, doit être coordonné pour que les 1° et 2° puissent être ouverts sans habilitation préalable, tout en conservant les garanties de formation plus favorables. L. 5132-6 fourni propose déjà l'inclusion de la section 4 bis, les garanties d'intermission, l'absence de terme au parcours et les dispenses de carence ; il faut adopter cette coordination avec le présent article, non la déclarer droit en vigueur. L. 1251-6 et L. 1251-40 ont été lus : les motifs d'affectation et recours subsistent pour les conditions conservées. L. 6221-1 et L. 5212-13 ont été consultés en entier : alternance des deux lieux, RNCP et exclusion du seul 5° de L. 5212-13 restent exacts. Le renvoi à une pension au titre des agents publics dans L. 5212-13 définit un public éligible ; il ne soumet pas les contrats des agents publics au contrat privé unique. Les règles d'apprentissage et de financement hors de cet article demeurent à coordonner. Le minimum d'un mois supprimé ne concerne ni le plancher hebdomadaire, ni une durée de formation, ni les engagements des missions antérieures. Les aides futures ne sont ni réservées aux anciens CDD ni étendues à des publics sans éligibilité propre.",
       benefit_review="Les cinq voies de mise à disposition sont examinées : recrutement des personnes sans emploi en difficultés sociales et professionnelles au 1°, complément de formation au 2°, apprentissage qualifiant avec alternance et RNCP au 3°, publics de L. 5212-13 hors son 5° au 4°, insertion de L. 5132-6 au 5°. Elles restent ouvertes aux situations futures ; les trois restrictions retirées élargissent leur accès sans supprimer les engagements ou garanties favorables de formation. Les aides, exonérations, droits sociaux, logement et formation demeurent ouverts selon leurs autres conditions au contrat unique. Les dispenses de carence du régime d'insertion et l'accès aux garanties mensuelles et d'intermission doivent rester coordonnés avec L. 5132-6 proposé ; les droits et primes des anciens contrats sont préservés.")
reduction('L1251-7',
          "Préalable d'une disposition légale spéciale ou d'un accord de branche étendu pour la mise à disposition à finalité de recrutement d'insertion du 1°.",
          "Préalable d'un décret ou d'un accord de branche étendu fixant la durée et les conditions du complément de formation pour ouvrir le cas de recours du 2°.",
          "Durée minimale légale d'un mois de la mission d'insertion du 5°, sans réduction unilatérale des missions antérieures ni suppression des engagements de formation.")

update('L1251-9',
       reason="La suppression du gel de six mois déjà rédigée est conservée après comparaison à l'article officiel entier. La reprise temporaire d'activité n'a plus à satisfaire le plafond de trois mois sans renouvellement ou la commande exceptionnelle à l'exportation. L'information-consultation préalable fondée uniquement sur cette dernière exception disparaît sans remplacement. Les dérogations favorables ne sont pas retirées pendant que leur interdiction subsiste : c'est cette interdiction entière qui disparaît pour le nouveau champ. La priorité de réembauche et les règles autonomes contre les abus et risques restent nécessaires. Le contrat unique concerne l'emploi à l'agence et n'autorise pas l'affectation permanente chez l'utilisateur ; ses obligations de rémunération ne sont pas comptées comme des économies.",
       review_notes="Les 1° et 2° restent repérables comme abrogés. La transition vise les mises à disposition nouvelles, sans réduire les engagements des contrats antérieurs ; la loi répressive plus douce reste réservée. L. 1233-45 a été lu : priorité pendant un an à compter de la rupture à la demande du salarié dans ce délai, emplois compatibles et nouvelle qualification signalée, information des représentants. L. 1251-10, lu, doit perdre son renvoi introductif à l'interdiction retirée mais conserver remplacement de grévistes, travaux dangereux avec dérogation favorable et médecins du travail. L. 1251-58-5, lu, ne peut rétablir le gel par substitution de lettre à contrat de mission. L. 1255-5, lu source et proposition, vise encore l'interdiction supprimée : retirer cette cible pour les faits nouveaux, en conservant les autres sanctions (3 750 euros, récidive six mois et 7 500 euros) dans leur champ. Hors des cinq codes, les articles 112-1 et 112-4 du code pénal restent à coordonner pour la loi plus douce ; leur contenu officiel n'est pas fourni ni prétendu réécrit ici. Le délai supprimé est six mois, sans conversion inventée en 180 jours. Les dispositions favorables des 1° et 2° restent utilisables pour les anciennes situations ; pour les nouvelles, elles sont rendues inutiles par la suppression de leur seule interdiction de base. Les obligations européennes et les utilisateurs publics demeurent à leur champ propre.",
       benefit_review="Les deux avantages sont la dérogation pour une mission d'au plus trois mois non renouvelable et celle pour une commande exceptionnelle à l'exportation, y compris chez le sous-traitant. Pour les mises à disposition nouvelles, l'interdiction de six mois qu'elles écartaient est entièrement supprimée, sans gel, plafond ou consultation de remplacement : les bénéficiaires peuvent donc toujours recruter dans ces cas et dans les autres cas légaux. Les anciennes situations conservent les exceptions et droits antérieurs. La priorité de réembauche de L. 1233-45 reste entière pour les salariés éligibles futurs ; les garanties de rémunération et d'intermission des emplois nouveaux ne sont pas supprimées.")
reduction('L1251-9',
          "Interdiction de recourir à l'intérim pour accroissement temporaire d'activité durant les six mois suivant un licenciement économique sur les postes concernés de l'établissement.",
          "Conditions de durée maximale de trois mois non renouvelables ou de commande exceptionnelle à l'exportation pour déroger à cette seule interdiction de six mois.",
          "Information et consultation préalables du CSE exigées uniquement pour la dérogation de commande exceptionnelle à l'exportation de l'ancien 2°.")

def effect(kind, measure_id, description, before, after, unit, population, transition, burdens, sq, pq):
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit, affected_population=population,
                conditions_and_transition=transition, replacement_or_new_burdens=burdens,
                source_quote=sq, proposed_quote=pq)

def impact(n, classification, assessment, limitations, burdens, effects):
    by_number[n]['substantive_impact'] = dict(version=1, classification=classification,
        assessment=assessment, scope_limitations=limitations, new_burdens_review=burdens, effects=effects)

impact('L1235-15', 'retained_necessary',
       "La source officielle est maintenue intégralement : réparation minimale d'un mois de salaire brut pour licenciement économique sans CSE obligatoire ni procès-verbal de carence. Le brouillon n'avait produit aucune réduction de cette charge ; aucune économie ni simplification n'est attribuée au maintien.",
       "Le maintien porte seulement sur cette sanction protectrice et ses deux conditions cumulatives. Il n'établit ni le coût global des élections, ni la conformité de chaque procédure, ni un solde de charges de l'ensemble du code.",
       "Aucune charge nouvelle n'est identifiée : le texte officiel entier reste applicable sans ajout de registre, pièce, délai ou condition. Le procès-verbal et le minimum indemnitaire sont des exigences déjà présentes, nécessaires à la représentation et à sa réparation.", [])

impact('L1235-16', 'material_reduction',
       "Par rapport à la source entière, une seconde communication patronale est retirée lorsque le même salarié a déjà reçu la décision complète avec date certaine. Cette dispense ne supprime ni la première information effective ni les réparations, et ne réduit pas les quinze jours de régularisation administrative.",
       "La réduction dépend de l'existence d'une communication antérieure prouvable et ne vaut donc pas pour tous les dossiers. Aucun nombre d'envois évités, gain monétaire ou solde national de conformité n'est établi ; les anciens manquements restent distincts.",
       "Aucune charge nouvelle n'est identifiée : la date certaine et l'information étaient déjà requises. Les éléments de preuve existants suffisent, sans attestation, registre ou déclaration de substitution. L'employeur garde l'information résiduelle des salariés non encore destinataires.", [
       effect('obligation_removed', 'pse-decision-communication-unique',
              "Suppression de la retransmission par l'employeur d'une décision déjà effectivement reçue par le même salarié.",
              "Après régularisation, l'employeur informe chaque salarié licencié avec date certaine, même si l'administration lui a déjà communiqué la même décision.",
              "Aucun second envoi n'est dû au salarié déjà informé de la décision complète avec date certaine ; les autres destinataires restent informés.",
              'legal_duty', "Employeurs et salariés licenciés après la première validation ou homologation annulée pour insuffisance de motivation.",
              "Informations restant à délivrer à compter de l'entrée en vigueur ; pas d'effacement des omissions et créances antérieures.",
              "Aucun remplacement documentaire ; réemploi des preuves de communication déjà disponibles.",
              "Cette décision est portée par l'employeur à la connaissance des salariés licenciés à la suite de la première décision de validation ou d'homologation, par tout moyen permettant de conférer une date certaine à cette information.",
              "Pour les informations à délivrer à compter de l'entrée en vigueur de la loi portant la présente réforme, aucune nouvelle transmission n'est exigée à un salarié auquel la même décision a déjà été communiquée avec date certaine, notamment par l'autorité administrative.")])

impact('L1236-7', 'coordination_only',
       "La source entière est un renvoi à la procédure de licenciement personnel pour la mission d'exportation. Cette procédure demeure ; le texte coordonne sa mise en œuvre avec l'emploi indéterminé nouveau, le préavis et les garanties spéciales. Il ne supprime pas une seconde autorisation ou un prélèvement autonome.",
       "Les réductions de préalables et de durée minimale relèvent de L. 1223-5 et L. 1223-6 proposés, et ne sont pas recomptées ici. Le coût du maintien d'emploi au-delà de la mission et le solde global de la réforme ne sont pas chiffrés. Les contrats antérieurs restent dans leur transition propre.",
       "Aucun registre, déclaration ou contrôle préalable nouveau n'est ajouté. Le maintien de l'emploi nouveau après mission et les droits de préavis résultent de la mesure commune du contrat unique et peuvent accroître des obligations patronales ; ils sont explicités sans être présentés comme une baisse de charges. Le motif contrôlable reste requis.", [
       effect('coordination', 'contrat-unique-emploi-indetermine',
              "Articulation de la procédure personnelle de rupture avec la mission sans terme automatique de l'emploi.",
              "L'article renvoie au licenciement personnel du contrat de mission d'exportation de L. 1223-5, sans fixer lui-même de durée d'emploi ou de préavis.",
              "Même procédure personnelle, emploi nouveau indéterminé, préavis de quinze jours selon L. 1234-3, indemnité spéciale sans seuil d'ancienneté et protections distinctes.",
              'regime', "Salariés de droit privé en mission d'exportation dans le champ de L. 1223-5 et leurs employeurs.",
              "Contrats conclus après l'entrée en vigueur ; contrats anciens et composantes indemnitaires antérieures protégés sans double compte.",
              "Aucun écrit de remplacement ; l'obligation de maintenir l'emploi après mission appartient à la mesure commune, non à une seconde coupe.",
              "La rupture à l'initiative de l'employeur du contrat de mission à l'exportation prévu à l'article L. 1223-5 est soumise aux dispositions du chapitre II relatives au licenciement pour motif personnel.",
              "La fin de la mission à l'exportation ne rompt pas automatiquement le contrat.")])

impact('L1237-3', 'material_reduction',
       "Sur l'ensemble des trois cas officiels, les cas de solidarité du nouvel employeur fondés sur la seule connaissance d'un contrat précédent sont supprimés pour les faits nouveaux. Le cas d'intervention prouvée dans une rupture abusive et la réparation des fautes personnelles subsistent. Les deux cas retirés constituent une même mesure de mobilité.",
       "Aucune suppression générale de responsabilité civile, loyauté ou non-concurrence valable n'est établie. La réforme ne libère pas le salarié d'un abus prouvé ; les faits antérieurs conservent les anciennes exceptions et prescriptions. Aucun gain financier ou effet d'emploi n'est chiffré.",
       "Aucune charge nouvelle n'est identifiée : il n'est demandé ni vérification d'un registre d'emploi antérieur ni certificat de libération. L'intervention fautive, le dommage et les preuves relevaient déjà du 1° et du droit commun ; les responsabilités pour faute distincte ne sont pas créées.", [
       effect('obligation_removed', 'solidarite-debauchage-faute-prouvee',
              "Retrait de la solidarité fondée sur la connaissance du contrat précédent lors de l'embauche, sans participation démontrée à l'abus.",
              "Ancien 2° : nouvel employeur solidaire du dommage s'il engage un salarié qu'il sait encore lié, sous la condition générale de rupture abusive.",
              "La connaissance seule ne suffit plus ; seule l'intervention prouvée dans la rupture abusive maintient la solidarité spéciale.",
              'legal_duty', "Nouveaux employeurs de salariés ayant rompu abusivement un contrat précédent.",
              "Faits générateurs à compter de l'entrée en vigueur ; créances, dispenses et recours anciens préservés.",
              "Aucune attestation ni déclaration de libération ne remplace la responsabilité retirée ; fautes distinctes toujours réparables.",
              "2° Si le nouvel employeur a engagé un salarié qu'il savait déjà lié par un contrat de travail ;",
              "La seule embauche du salarié ou la poursuite de son emploi, même en connaissance du contrat précédent, ne suffit pas à engager cette responsabilité."),
       effect('obligation_removed', 'solidarite-debauchage-faute-prouvee',
              "Retrait du cas de solidarité pour poursuite de l'emploi après connaissance du lien antérieur, deuxième volet de la même mesure.",
              "Ancien 3° : poursuite de l'emploi après connaissance du contrat précédent, sauf terme déjà expiré, préavis achevé ou quinze jours écoulés lors de l'avertissement.",
              "Aucune solidarité spéciale sur ce seul fait pour l'avenir ; les exceptions temporelles anciennes restent applicables aux faits anciens.",
              'legal_duty', "Nouveaux employeurs avertis du contrat précédent de leur salarié.",
              "Même transition par faits générateurs ; ne modifie pas le préavis individuel de quinze jours du contrat unique.",
              "Pas de délai de surveillance ou de dossier de substitution ; intervention fautive et faute personnelle restent réparables.",
              "3° Si le nouvel employeur a continué d'employer le salarié après avoir appris que ce dernier était encore lié à un autre employeur par un contrat de travail.",
              "La seule embauche du salarié ou la poursuite de son emploi, même en connaissance du contrat précédent, ne suffit pas à engager cette responsabilité.")])

impact('L1237-9', 'material_reduction',
       "La source entière conserve indemnité de retraite, unicité, calcul réglementaire et reliquat. La suppression du préalable collectif ouvre l'affectation au maintien de rémunération par accord direct à défaut de texte collectif, y compris pour les situations futures. Il s'agit d'un accès élargi à un avantage existant et non d'une baisse d'indemnité patronale.",
       "Le taux de l'indemnité spéciale n'est pas diminué et aucune économie globale n'est démontrée. Le consentement des parties, la situation de fin de carrière et les minima réglementaires demeurent ; l'article ne modifie ni le financement des pensions ni les règles de capitalisation.",
       "Aucune charge nouvelle n'est identifiée : la demande du salarié et l'accord de l'employeur existaient déjà. Le texte n'exige ni formulaire ni autorisation ni registre supplémentaires ; il ajoute une faculté d'accord direct, sans imposer l'affectation à une partie ou une réduction de rémunération.", [
       effect('relief_extended', 'retraite-affectation-accord-direct',
              "Accès à l'affectation de l'indemnité de retraite en l'absence d'accord collectif préalable.",
              "L'affectation de l'indemnité au maintien total ou partiel de rémunération doit être prévue par accord d'entreprise ou d'établissement ou, à défaut, de branche.",
              "À défaut de texte collectif, accord direct du salarié et de l'employeur possible aux mêmes conditions, avec versement du reliquat et garanties plus favorables.",
              'legal_duty', "Salariés en fin de carrière demandant, avec accord de l'employeur, un temps partiel ou réduit en jours.",
              "Faculté directe à compter de l'entrée en vigueur ; affectations déjà convenues et droits plus favorables préservés.",
              "Aucun agrément ou document distinct ; l'accord des deux parties reste volontaire.",
              "Un accord d'entreprise ou d'établissement ou, à défaut, une convention ou un accord de branche peut prévoir la possibilité d'affecter l'indemnité de départ à la retraite au maintien total ou partiel de la rémunération du salarié en fin de carrière",
              "À compter de l'entrée en vigueur de la loi portant la présente réforme, en l'absence d'un tel texte collectif, le salarié et l'employeur peuvent convenir directement de cette affectation dans les mêmes conditions.")])

impact('L1237-15', 'material_reduction',
       "La comparaison à la source complète établit le retrait d'un seul jour d'attente après autorisation dans le premier alinéa. Les salariés protégés gardent l'accès à la rupture conventionnelle, l'autorisation indépendante et la rétractation ; le deuxième alinéa médical est conservé. Il n'y a pas suppression de l'autorisation ou réduction de son délai d'instruction.",
       "Le gain maximal est un jour entre autorisation et rupture convenue, sans garantie d'une rupture plus précoce si les parties ont fixé une autre date. Les autres ruptures collectives ou congés de mobilité ne sont pas concernés ; aucune réduction globale des procédures n'est chiffrée.",
       "Aucune charge nouvelle n'est identifiée : date convenue et rétractation sont déjà inhérentes à la convention. Aucune demande, homologation, donnée ou condition de remplacement n'est créée. L'autorisation et l'avis du médecin inspecteur restent des garanties préexistantes nécessaires.", [
       effect('deadline_reduced', 'rupture-protegee-sans-attente-lendemain',
              "Retrait du lendemain obligatoire après autorisation pour les conventions nouvelles du premier alinéa.",
              "Rupture au plus tôt le lendemain du jour de l'autorisation, soit un décalage d'un jour après celle-ci, dans le champ des salariés protégés du premier alinéa.",
              "Rupture possible le jour même de l'autorisation, à la date convenue et après rétractation ; zéro jour d'attente supplémentaire sur ce seul fondement.",
              'calendar_days', "Parties à une rupture conventionnelle d'un salarié protégé relevant du premier alinéa de L. 1237-15.",
              "Conventions conclues après l'entrée en vigueur ; anciennes conventions et autres obstacles légaux conservent leur régime.",
              "Aucune autorisation remplacée : elle demeure, ainsi que les garanties distinctes ; aucune déclaration supplémentaire.",
              "Dans ce cas, et par dérogation aux dispositions de l'article L. 1237-13, la rupture du contrat de travail ne peut intervenir que le lendemain du jour de l'autorisation.",
              "Dans ce cas, par dérogation à l'article L. 1237-13, la rupture intervient à la date convenue par les parties, au plus tôt le jour de l'autorisation et après expiration du délai de rétractation.")])

impact('L1237-18-2', 'material_reduction',
       "Le retrait démontré par rapport aux sept clauses de la source porte sur la répétition des informations déjà effectivement reçues par les mêmes représentants. Les autres clauses restent nécessaires au congé volontaire et indemnisé. Le minimum spécial est coordonné au barème commun sans le fermer avant un an ; ce renvoi n'est pas une seconde réduction de coût ordinaire.",
       "Le nombre de transmissions évitées dépend des informations déjà disponibles. Les conséquences du nouveau minimum pour les services futurs relèvent du barème commun, sans estimation monétaire. Les mesures collectives, le régime social du congé et le contrat support conservent leurs champs et transitions propres.",
       "Aucune nouvelle attestation, registre, déclaration ou condition d'éligibilité n'est identifiée. L'information des données nouvelles, le consentement écrit et l'indemnité spécifique préexistaient. Le maintien de l'emploi nouveau pendant une mission découle du contrat unique ; son coût éventuel n'est pas une économie imputée à la dispense d'information.", [
       effect('obligation_removed', 'mobilite-information-unique-representants',
              "Dispense de répéter aux mêmes représentants des informations déjà effectivement communiquées dans leurs attributions.",
              "Le 6° impose de fixer l'information des institutions représentatives sans dispense expresse en cas de communication déjà accomplie.",
              "Pas de nouvelle transmission du même contenu aux mêmes destinataires ; seuls changements et compléments nécessaires sont dus.",
              'legal_duty', "Entreprises organisant un congé de mobilité et leurs institutions représentatives du personnel.",
              "Informations à délivrer après l'entrée en vigueur ; chaque destinataire doit avoir effectivement reçu le contenu dispensé.",
              "Aucune preuve formalisée ou transmission de remplacement ; les garanties d'information effective restent en place.",
              "6° Les conditions d'information des institutions représentatives du personnel ;",
              "Pour les informations à délivrer à compter de l'entrée en vigueur de la loi portant la présente réforme, les mêmes informations déjà effectivement communiquées aux mêmes destinataires dans l'exercice de leurs attributions n'ont pas à leur être transmises de nouveau ; seuls les compléments et changements nécessaires sont communiqués ;"),
       effect('coordination', 'contrat-unique-indemnite-ordinaire',
              "Coordination du minimum spécial de départ amiable au nouveau barème de référence, sans appliquer le seuil ordinaire d'un an.",
              "Minimum référé au licenciement économique : un quart de mois de salaire brut de référence par année des dix premières années, puis un tiers au-delà, avec prorata des mois complets selon R. 1234-1 et R. 1234-2 officiels ; le 7° n'énonce aucun seuil propre au congé.",
              "Minimum nouveau de 0,20 mois de salaire brut par année totale avec prorata des mois complets, plafonné à six mois, sans seuil d'un an ; part antérieure protégée et seule part postérieure plafonnée pour les anciens contrats.",
              'other', "Salariés bénéficiant d'un congé de mobilité avec rupture d'un commun accord.",
              "Droits et indemnités déjà convenus et garanties plus favorables préservés ; aucun double compte d'ancienneté.",
              "Aucun dossier nouveau ; le barème de référence est coordonné, pas une nouvelle indemnité ajoutée à l'existante.",
              "7° Les indemnités de rupture garanties au salarié, qui ne peuvent être inférieures aux indemnités légales dues en cas de licenciement pour motif économique.",
              "Le renvoi au barème de l'article L. 1234-9 pour fixer ce minimum ne soumet pas l'indemnité spécifique de départ d'un commun accord à la condition d'un an propre à l'indemnité ordinaire de rupture.")])

impact('L1237-19-1', 'material_reduction',
       "L'article officiel impose à la fois un accord écrit du salarié au dispositif et une convention individuelle. Le premier écrit est fusionné dans cette convention déjà obligatoire ; la candidature et son acceptation ne valent plus seules rupture dans le champ nouveau. Les clauses protectrices, le suivi et les mesures de reclassement demeurent ; le minimum indemnitaire spécial est coordonné sans seuil d'un an.",
       "Le bilan et le contrôle administratif relèvent d'autres articles et ne sont pas abrogés ici. L. 1237-19-2 doit reproduire la coordination expresse sur le consentement ; ses fichiers ne sont pas modifiés. Les effets monétaires du barème de référence et le solde national de conformité ne sont pas établis.",
       "Aucune nouvelle convention n'est créée : les 4° bis et 4° ter l'exigeaient déjà. L'écrit préalable disparaît dans le même document et la rétractation demeure. La coordination retire l'effet de rupture d'une candidature seule sans registre ni déclaration nouveaux ; les autres clauses et le suivi préexistaient.", [
       effect('obligation_merged', 'rcc-consentement-convention-unique',
              "Regroupement du consentement écrit au dispositif dans la convention individuelle déjà obligatoire, sans écrit préalable distinct.",
              "Accord écrit du salarié au dispositif à transmettre selon le 4°, en plus de la convention individuelle prévue aux 4° bis ou 4° ter.",
              "Un seul support de consentement, la convention individuelle ; absence de transmission préalable d'un accord distinct et candidature seule sans effet de rupture.",
              'legal_duty', "Salariés candidats et employeurs sous accord de rupture conventionnelle collective.",
              "Conventions individuelles conclues après l'entrée en vigueur ; consentement libre et rétractation conservés, droits déjà garantis non diminués.",
              "Pas de formulaire ou signature supplémentaires : l'écrit rejoint la convention préexistante ; coordination nécessaire de L. 1237-19-2.",
              "4° Les modalités de présentation et d'examen des candidatures au départ des salariés, comprenant les conditions de transmission de l'accord écrit du salarié au dispositif prévu par l'accord collectif ;",
              "Pour les conventions individuelles conclues à compter de l'entrée en vigueur de la loi portant la présente réforme, le consentement écrit du salarié au dispositif est exprimé dans la convention individuelle de rupture mentionnée au 4° bis ou, le cas échéant, au 4° ter, sans transmission préalable d'un accord écrit distinct."),
       effect('coordination', 'contrat-unique-indemnite-ordinaire',
              "Application du barème de référence au minimum spécial de RCC, sans franchise d'un an ni plafonnement des droits antérieurs ou négociés.",
              "Minimum référé au licenciement : un quart de mois de salaire brut de référence par année des dix premières années, puis un tiers au-delà, avec prorata des mois complets selon R. 1234-1 et R. 1234-2 officiels ; aucun seuil propre n'est créé par le 5°.",
              "Minimum de référence nouveau de 0,20 mois de salaire brut par année totale, prorata des mois complets et plafond de six mois ; pas de seuil d'un an pour cette indemnité spéciale, part antérieure protégée et seule part nouvelle plafonnée.",
              'other', "Salariés quittant l'entreprise dans une rupture conventionnelle collective.",
              "Ancienneté totale conservée sans double emploi ; garanties des accords et conventions déjà conclus et garanties plus favorables maintenues.",
              "Aucune seconde indemnité ou déclaration n'est ajoutée ; aucune réduction autonome supplémentaire n'est comptée pour ce renvoi.",
              "5° Les modalités de calcul des indemnités de rupture garanties au salarié, qui ne peuvent être inférieures aux indemnités légales dues en cas de licenciement ;",
              "Le renvoi au barème de l'article L. 1234-9 pour fixer ce minimum ne soumet pas l'indemnité spécifique de rupture conventionnelle collective à la condition d'un an propre à l'indemnité ordinaire de rupture.")])

impact('L1251-4', 'retained_necessary',
       "La source officielle est conservée intégralement : elle accorde deux possibilités d'activité dérogatoires à l'exclusivité. Le brouillon n'avait modifié que les mots. Le maintien des deux avantages, aussi pour les opérations futures, ne constitue aucune réduction nouvelle d'impôt ou de contrainte.",
       "L'exclusivité générale de L. 1251-2 et les règles autonomes du placement ou du temps partagé ne sont pas réformées ici. Aucun effet global sur la concurrence, l'emploi ou les coûts n'est mesuré ; le régime des agents publics n'est pas étendu implicitement.",
       "Aucune charge nouvelle n'est identifiée : aucun mot de la source n'est ajouté et aucune autorisation ou déclaration supplémentaire n'est créée. Les deux facultés sont préservées sans restriction temporelle nouvelle, avec leurs fondements autonomes déjà existants.", [])

impact('L1251-5', 'coordination_only',
       "L'interdiction officielle de pourvoir durablement un emploi permanent chez l'utilisateur est conservée. La proposition distingue cette affectation du nouvel emploi indéterminé à l'agence et renvoie aux garanties d'intermission. Aucune interdiction ni formalité autonome n'est supprimée par cet article ; il ne constitue pas une baisse de coût démontrée.",
       "La suppression des nouveaux contrats de mission déterminés relève de la mesure commune. Les droits auprès de l'utilisateur et la dispense de plafond de mission sont coordonnés dans d'autres articles ; leur coût et la compatibilité européenne ne sont pas établis par le présent contrôle local.",
       "Aucun document nouveau n'est créé, mais le passage obligatoire des futurs recrutements à l'emploi indéterminé étend les obligations de continuité d'emploi et de garantie mensuelle aux cas auparavant conclus en mission déterminée. Ces charges de la mesure commune sont signalées ; les mentions et lettres de mission préexistaient au CDI intérimaire.", [
       effect('coordination', 'contrat-unique-emploi-indetermine',
              "Maintien de la prévention des affectations permanentes abusives, tout en séparant la mission de l'emploi indéterminé et de ses intermissions.",
              "Interdiction visant le contrat de mission quel qu'en soit le motif, sans distinguer dans cet article les garanties du CDI intérimaire.",
              "Même interdiction sur l'affectation, y compris par lettre de mission ; emploi nouveau indéterminé à l'agence, droits d'intermission et contrats antérieurs préservés.",
              'regime', "Entreprises utilisatrices, agences et leurs salariés sous nouvelles embauches de droit privé.",
              "Nouveaux contrats après l'entrée en vigueur ; anciens contrats à leur terme en cours, sans nouvelle conclusion ou renouvellement déterminés.",
              "Garantie mensuelle et continuité d'emploi étendues par la mesure commune, avec coût possible non chiffré ; pas de nouvelle formalité indépendante.",
              "Le contrat de mission, quel que soit son motif, ne peut avoir ni pour objet ni pour effet de pourvoir durablement un emploi lié à l'activité normale et permanente de l'entreprise utilisatrice.",
              "La fin de la mission ne rompt pas le contrat et ne fait pas perdre les garanties de rémunération, de congés et d'ancienneté des périodes sans mission prévues aux articles L. 1251-58-2 et L. 1251-58-3.")])

impact('L1251-7', 'mixed',
       "Trois restrictions d'accès de la source complète sont retirées : support légal spécial ou accord étendu du 1°, encadrement préalable par décret ou accord étendu du 2°, minimum d'un mois du 5°. Les cinq voies et leurs avantages subsistent. La coordination au contrat unique rend aussi obligatoires, pour les futurs emplois auparavant en mission déterminée, le maintien de l'emploi et les garanties d'intermission ; le solde net n'est pas établi.",
       "Les aides demeurent soumises à leurs éligibilités et ne sont pas créées pour de nouveaux publics. Le 12° de L. 2253-1, les textes de formation et d'insertion et le droit de l'Union restent à coordonner. Aucun accord de branche extérieur n'a été examiné et aucun gain d'emploi ou montant net de charges n'est inventé.",
       "Aucun agrément, formulaire, registre ou dépôt ne remplace les préalables retirés. En revanche, l'extension de l'emploi indéterminé rend applicables aux nouveaux recrutements concernés les obligations salariales et d'intermission du CDI intérimaire, auparavant non générales. Cette charge de la mesure commune est recensée avec le caractère mixte ; les engagements de formation existaient déjà.", [
       effect('obligation_removed', 'interim-insertion-acces-direct',
              "Ouverture directe du cas de recrutement d'insertion du 1° sans support légal spécial ou accord de branche étendu préalable.",
              "La finalité d'insertion ne suffit qu'en application de dispositions légales ou d'un accord de branche étendu.",
              "Finalité d'insertion toujours exigée, sans habilitation normative préalable ; engagements et garanties applicables conservés.",
              'legal_duty', "Entreprises et personnes sans emploi rencontrant des difficultés sociales et professionnelles particulières.",
              "Mises à disposition convenues après l'entrée en vigueur ; engagements des missions anciennes et conditions propres des aides maintenus.",
              "Aucune déclaration ou demande d'autorisation de remplacement.",
              "1° Lorsque la mission de travail temporaire vise, en application de dispositions légales ou d'un accord de branche étendu, à favoriser le recrutement de personnes sans emploi rencontrant des difficultés sociales et professionnelles particulières ;",
              "Le recours à ce cas ne nécessite pas une habilitation par une disposition légale spéciale ou un accord de branche étendu ;"),
       effect('obligation_removed', 'interim-formation-acces-direct',
              "Suppression supplémentaire du préalable normatif fixant durée et conditions pour ouvrir le complément de formation du 2°.",
              "Les deux entreprises s'engagent au complément de formation pour une durée et dans des conditions fixées par décret ou accord de branche étendu.",
              "Leur engagement de formation ouvre le cas de recours sans préalable de décret ou d'accord étendu ; règles de fond, garanties favorables et engagements acquis maintenus.",
              'legal_duty', "Entreprises de travail temporaire, utilisateurs et salariés recevant un complément de formation professionnelle.",
              "Mises à disposition convenues après l'entrée en vigueur ; pas de suppression des garanties pédagogiques ni des engagements de missions antérieures.",
              "Pas de programme ou document distinct nouvellement imposé ; maintien des obligations de formation autonomes.",
              "2° Lorsque l'entreprise de travail temporaire et l'entreprise utilisatrice s'engagent, pour une durée et dans des conditions fixées par décret ou par accord de branche étendu, à assurer un complément de formation professionnelle au salarié ;",
              "Ce cas de mise à disposition est ouvert sans qu'un décret ou un accord de branche étendu doive en fixer préalablement la durée et les conditions."),
       effect('deadline_reduced', 'interim-insertion-sans-minimum-mission',
              "Suppression du minimum d'un mois de mission d'insertion, sans limiter la durée de l'emploi ou de la formation.",
              "Mission conclue en application de L. 5132-6 d'une durée minimale d'un mois.",
              "Aucune durée minimale légale d'un mois pour la mission ; emploi nouveau indéterminé et garanties de rémunération préservées.",
              'other', "Salariés éligibles à l'intérim d'insertion de L. 5132-6 et entreprises concernées.",
              "Missions nouvelles seulement ; aucune réduction unilatérale d'engagement antérieur. Le mois n'est pas converti en un nombre fictif de jours.",
              "Pas de justificatif ou condition de remplacement ; le volume de formation et les engagements applicables subsistent.",
              "5° Lorsque le contrat de mission, d'une durée minimale d'un mois, est conclu en application de l'article L. 5132-6.",
              "5° Lorsque la mise à disposition est réalisée en application de l'article L. 5132-6, sans durée minimale légale d'un mois pour cette mission."),
       effect('coordination', 'contrat-unique-emploi-indetermine',
              "Ouverture des cinq voies sous emploi indéterminé, avec extension des obligations de garantie salariale et d'intermission auparavant propres au CDI intérimaire.",
              "L'article permet notamment un contrat de mission d'insertion limité ; l'emploi indéterminé et ses garanties ne sont pas généralisés par la source.",
              "Nouveaux salariés employés à durée indéterminée, sans fin d'emploi au terme de mission, apprentissage ou insertion ; rémunération mensuelle et droits d'intermission applicables, avantages futurs préservés.",
              'regime', "Futurs salariés des cinq voies de mise à disposition et leurs entreprises de travail temporaire.",
              "Nouvelles embauches après l'entrée en vigueur ; contrats antérieurs, primes et créances conservés, aucune nouvelle durée déterminée.",
              "Extension de continuité d'emploi et de garantie salariale, coût net non mesuré. Pas de nouveau contrat à chaque mission ; lettres prévues par les textes communs.",
              "5° Lorsque le contrat de mission, d'une durée minimale d'un mois, est conclu en application de l'article L. 5132-6.",
              "La rémunération mensuelle garantie et les droits des périodes sans mission demeurent applicables selon les articles L. 1251-58-2 et L. 1251-58-3.")])

impact('L1251-9', 'mixed',
       "La source entière est allégée du gel de six mois et de ses conditions dérogatoires, dont la consultation propre à l'exportation ; la priorité de réembauche reste entière. Les possibilités de mission courte ou d'exportation ne sont pas fermées : elles deviennent accessibles sans cette interdiction de base. La coordination de l'emploi indéterminé et des garanties salariales ajoute toutefois des obligations pour les futurs recrutements autrefois en mission déterminée ; aucun solde net global n'est démontré.",
       "La liberté de recours reste limitée aux affectations temporaires légales et aux autres interdictions. Les coordinations répressives de L. 1255-5, introductive de L. 1251-10 et hors corpus pénal sont identifiées, non réécrites ici. Aucune suppression générale de consultation du CSE ou de droit européen n'est affirmée.",
       "Aucun dossier, agrément ou déclaration ne remplace le gel ni sa consultation spéciale. La priorité de réembauche et les consultations autonomes préexistaient. La continuité d'emploi et la rémunération d'intermission sont étendues aux recrutements nouveaux par la mesure commune du contrat unique ; leur coût ne peut être déduit fictivement des charges retirées.", [
       effect('obligation_removed', 'interim-sans-gel-apres-licenciement',
              "Retrait de l'interdiction générale de six mois pour accroissement temporaire d'activité sur les postes licenciés de l'établissement.",
              "Six mois d'interdiction après licenciement économique, sous deux exceptions : mission de trois mois non renouvelable ou commande exceptionnelle d'exportation.",
              "Aucun gel sur ce seul fondement, y compris pour les mêmes postes ; autres règles de recours et priorité de réembauche d'un an maintenues.",
              'legal_duty', "Entreprises utilisatrices ayant licencié pour motif économique et salariés concernés par de nouvelles mises à disposition.",
              "Mises à disposition nouvelles après l'entrée en vigueur ; droits et contrats antérieurs préservés, réserve de loi pénale plus douce.",
              "Pas de demande ou plafond de substitution ; maintien du caractère temporaire et des protections autonomes.",
              "Dans les six mois suivant un licenciement pour motif économique, il est interdit de faire appel à un salarié temporaire au titre d'un accroissement temporaire de l'activité, y compris pour l'exécution d'une tâche occasionnelle, précisément définie et non durable, ne relevant pas de l'activité normale de l'entreprise utilisatrice.",
              "Aucun délai d'attente de six mois n'est imposé sur ce fondement."),
       effect('obligation_removed', 'interim-sans-gel-apres-licenciement',
              "Retrait de la consultation spéciale d'exportation, conséquence de la même suppression d'interdiction et non d'une seconde liberté générale de recours.",
              "Pour déroger au gel par commande exceptionnelle d'exportation, information et consultation préalables du CSE, s'il existe.",
              "Cette information-consultation sur le seul fondement de l'ancien 2° n'est plus due ; consultations ayant un fondement autonome maintenues.",
              'legal_duty', "Utilisateurs, entrepreneurs principaux ou sous-traitants et CSE dans l'ancien cas dérogatoire d'exportation.",
              "Même transition des mises à disposition nouvelles, sans reprise d'engagements anciens ni disparition de procédures collectives distinctes.",
              "Aucun avis, déclaration ou pièce ne remplace la consultation retirée.",
              "Cette possibilité de recrutement est subordonnée à l'information et à la consultation préalables du comité social et économique, s'il existe.",
              "L'information et la consultation préalables du comité social et économique exigées sur le seul fondement de l'ancien 2° ne sont plus requises."),
       effect('coordination', 'contrat-unique-emploi-indetermine',
              "La liberté nouvelle de mission après licenciement n'autorise pas de nouveau CDD et s'articule avec les garanties d'emploi et de salaire à l'agence.",
              "Les exceptions officielles reposent sur des contrats de mission et leur durée, sans généralisation de l'emploi indéterminé dans cet article.",
              "Pour les nouveaux recrutements, contrat indéterminé de l'agence et garantie salariale des intermissions, sans rupture automatique à la fin de l'affectation.",
              'regime', "Entreprises de travail temporaire et salariés nouvellement recrutés pour ces affectations.",
              "Embauches après la réforme, anciens contrats à leur régime transitoire ; aucune durée déterminée nouvellement permise.",
              "Continuité d'emploi et rémunération garantie étendues par la mesure commune ; solde de coûts inconnu, aucun nouveau formulaire.",
              "1° Lorsque la durée du contrat de mission n'est pas susceptible de renouvellement et n'excède pas trois mois ;",
              "La fin de la mission ne rompt pas cet emploi ; la rémunération garantie et les droits des périodes sans mission restent applicables.")])

checks = {
    'L1235-15': {
        'L1234-1': "La source de L. 1234-1 prévoit les durées historiques selon ancienneté ; sa proposition institue quinze jours pour le seul contrat nouveau et maintient les procédures collectives. L'absence de CSE obligatoire n'est donc pas régularisée par le respect de ce préavis et la sanction distincte d'un mois reste due.",
        'L1221-2': "La proposition de L. 1221-2 supprime les nouveaux CDD sans terme automatique ; elle ne dispense pas les nouvelles relations privées de la représentation collective. La sanction de L. 1235-15 demeure accessible aux salariés futurs éligibles et aux contrats anciens dans leur champ, sans transposition aux agents publics.",
        'L1234-9': "Les huit mois de l'ouverture officielle de L. 1234-9 deviennent un an, préavis inclus à la fin effective pour les nouveaux contrats, avec part ancienne protégée. Cette condition et le plafond de six mois ne limitent pas la réparation autonome de L. 1235-15 ; elle reste d'au moins un mois brut sans condition d'un an."
    },
    'L1235-16': {
        'L1234-1': "Les quinze jours de L. 1235-16 courent de la notification du jugement à l'administration, alors que L. 1234-1 proposé fixe le préavis patronal nouveau à quinze jours calendaires. Ces deux délais n'ont ni le même débiteur ni le même départ ; les procédures collectives et les préavis anciens restent distincts.",
        'L1221-2': "La proposition de L. 1221-2 rend indéterminées les relations nouvelles sans supprimer les licenciements collectifs ni leur contrôle. Les droits de réintégration et de réparation de L. 1235-16 restent applicables aux situations futures ; aucune condition de CDD ou de durée de mission n'est introduite par la dispense de second envoi.",
        'L1234-9': "Le renvoi exprès du deuxième alinéa porte sur l'indemnité légale de licenciement, qui s'ajoute à la réparation minimale des six derniers mois. Le seuil nouveau d'un an s'apprécie préavis inclus pour cette seule indemnité ordinaire ; huit mois et part de service antérieure gardent la transition prévue pour les anciens contrats, sans réduire la réparation spéciale."
    },
    'L1236-7': {
        'L1223-5': "La source subordonne la mission majoritairement hors de France à un accord collectif ; la proposition consultée retire ce préalable et conserve la procédure personnelle de L. 1236-7. Le présent texte maintient ce champ, sans réintroduire l'accord, une fin automatique d'emploi ou une dispense des protections applicables aux ruptures nouvelles.",
        'L1223-6': "Les 1° à 5° officiels incluent un minimum de six mois de mission et un minimum indemnitaire sans ancienneté. La proposition retire les préalables mais conserve rémunération, formation, reclassement et minimum spécial sans seuil d'un an ; le présent texte réserve cette garantie, avec mois complets à coordonner et composante ancienne préservée.",
        'L1234-1': "Le préavis personnel auquel conduit la procédure source est historiquement fonction de l'ancienneté. La proposition de L. 1234-1 applique quinze jours calendaires au contrat nouveau, y compris en faute grave avec paiement sans exécution si nécessaire ; les autorisations et les contrats anciens restent distincts, sans promesse d'une procédure complète en quinze jours.",
        'L1221-2': "La fin de la mission d'exportation ne peut devenir le terme d'un nouveau contrat au regard de L. 1221-2 proposé. L'emploi est donc expressément indéterminé et sa rupture patronale demeure motivée et contrôlable. Les contrats antérieurs, conversions consenties, ancienneté et créances sont protégés sans nouveau CDD ou renouvellement déterminé.",
        'L1234-9': "L'ouverture ordinaire d'un an à la fin effective préavis inclus, le taux de 0,20 mois et le plafond de six mois n'effacent pas le minimum sans ancienneté de L. 1223-6. Le dernier alinéa réserve désormais la transition de L. 1234-9 pour éviter de maintenir à tort tous les taux ordinaires anciens sur les services futurs ; la même période n'est pas comptée deux fois."
    },
    'L1237-3': {
        'L1234-1': "Le préavis patronal de L. 1234-1 et le préavis individuel nouveau ne sont pas le délai d'exonération de quinze jours de l'ancien 3° de L. 1237-3. Ce dernier appartient au cas de solidarité supprimé pour l'avenir ; ses règles demeurent pour les faits antérieurs, et une rupture régulièrement notifiée ne devient pas abusive du seul changement d'emploi.",
        'L1221-2': "L. 1221-2 proposé interdit les nouveaux termes d'emploi, mais la suppression des anciens 2° et 3° de solidarité porte sur les faits générateurs nouveaux, y compris quand le premier contrat est ancien. Les anciens délais et exceptions de terme du CDD restent conservés pour les faits anciens ; aucune nouvelle durée déterminée ne résulte de la réforme de responsabilité.",
        'L1234-9': "L. 1234-9 règle une indemnité ordinaire à l'initiative de l'employeur, avec seuil d'un an pour le nouveau contrat et transition des huit mois anciens. L. 1237-3 concerne un dommage à l'ancien employeur après abus du salarié : aucun taux, plafond de six mois ou seuil d'ancienneté ne lui est importé ; le cas d'intervention prouvée reste réparable."
    },
    'L1237-9': {
        'L1234-1': "Le préavis du départ volontaire à la retraite est rattaché par L. 1237-10, consulté localement, à L. 1234-1. La durée nouvelle de quinze jours ne modifie pas l'indemnité de retraite de L. 1237-9 ; les durées des contrats antérieurs et les règles de notification restent à leur régime sans confusion avec la mise à la retraite patronale.",
        'L1221-2': "L'emploi nouveau indéterminé de L. 1221-2 peut se terminer par un départ volontaire à la retraite selon ses règles propres ; l'affectation en fin de carrière n'en fixe pas un terme automatique. La faculté directe d'affectation reste ouverte aux futurs salariés éligibles, sans imposer de CDD et sans fermer les accords ou droits déjà acquis.",
        'L1234-9': "L'indemnité spéciale de départ volontaire est régie par L. 1237-9 et D. 1237-1/2, non par le barème ordinaire de L. 1234-9. Le zéro avant un an, le taux de 0,20 mois et le plafond de six mois ne remplacent donc ni ses paliers de dix à trente ans, ni son reliquat, ni ses références salariales favorables. Une démission ordinaire reste distincte de ce départ spécial."
    },
    'L1237-15': {
        'L1234-1': "Le préavis patronal nouveau de quinze jours selon L. 1234-1 ne remplace ni l'autorisation de l'inspecteur pour les salariés protégés ni la rétractation d'une rupture conventionnelle. Le jour retiré ici se situe seulement après autorisation, à la date convenue ; les procédures de protection et les contrats anciens ne sont pas supprimés par ce préavis.",
        'L1221-2': "Les salariés protégés employés sous le contrat unique proposé par L. 1221-2 conservent l'accès à la rupture conventionnelle et ses contrôles propres. L'absence de terme automatique ne fait pas obstacle à une rupture consentie, et la transition du présent article conserve le régime de date des conventions anciennes, sans nouvelle embauche déterminée.",
        'L1237-13': "La source vise l'indemnité spécifique au premier alinéa, le lendemain d'homologation au deuxième et quinze jours calendaires de rétractation au troisième. La proposition consultée maintient la rétractation et un minimum sans ancienneté ; la dérogation de L. 1237-15 substitue autorisation à homologation et retire seulement son lendemain pour les nouvelles conventions, sans fermer les droits indemnitaires.",
        'L1234-9': "Le renvoi indirect par L. 1237-13 est un montant minimum spécifique de rupture conventionnelle, sans importer le seuil d'un an ni l'absence d'indemnité de démission ordinaire. L. 1234-9 proposé garde huit mois et la part ancienne pour les contrats antérieurs ; la proposition de L. 1237-13 protège ce minimum spécial même avant un an et réserve les conventions déjà conclues."
    },
    'L1237-18-2': {
        'L1234-1': "Les périodes de travail et la rupture amiable du contrat support ne sont pas un licenciement soumis automatiquement au préavis patronal de L. 1234-1. Le préavis nouveau s'applique à une rupture unilatérale du nouvel emploi selon son régime ; les congés, autorisations pour salariés protégés et procédures collectives restent distincts de ces quinze jours.",
        'L1221-2': "La durée du congé ou des actions de formation ne fixe pas le terme d'un emploi nouveau selon L. 1221-2 proposé. Le 4° distingue donc cette activité de la rupture consentie du contrat support régie par L. 1237-18-4. Les contrats antérieurs conservent leurs droits et aucune reprise d'activité sous CDD nouveau n'est autorisée.",
        'L1234-9': "Le 7° renvoie désormais explicitement au barème de L. 1234-9 pour le seul montant de référence : 0,20 mois par année totale, fractions en mois complets, six mois pour la part nouvelle. Le seuil d'un an apprécié préavis inclus pour l'ordinaire n'est pas importé au minimum spécial ; la part de service antérieure et les garanties négociées restent protégées sans double compte."
    },
    'L1237-19-1': {
        'L1234-1': "L. 1234-1 proposé règle le préavis de la rupture patronale, non la durée des candidatures ou des conventions de RCC. La convention individuelle et sa rétractation demeurent avec les procédures collectives et autorisations distinctes. Les quinze jours calendaires nouveaux ne valent ni validation collective ni consentement écrit du salarié.",
        'L1221-2': "Le contrat unique de L. 1221-2 exclut les nouveaux CDD et la fin automatique d'emploi par une formation ou une aide. La durée mentionnée au 2° reste celle du dispositif de départ, pas celle d'une nouvelle relation d'emploi ; la rupture requiert la convention et les protections propres à la RCC, avec préservation des contrats antérieurs.",
        'L1237-18-1': "Le renvoi du 7° à la plage L. 1237-18-1 à L. 1237-18-5 inclut les périodes de travail du congé de mobilité. La source prévoit un CDD de L. 1242-3, tandis que sa proposition ne l'admet plus pour l'avenir et préserve la reprise du reliquat. Le renvoi au congé ne doit donc réintroduire ni un nouveau terme d'emploi ni la disparition des droits du contrat support.",
        'L1237-18-2': "La vue fournie fixe sept thèmes du congé, avec dispense de double information au 6° et minimum spécifique au 7°. Le renvoi du 7° de L. 1237-19-1 les conserve sans imposer une transmission supprimée. Le présent lot précise également leur minimum avec mois complets et part ancienne non plafonnée ; le seuil d'un an ordinaire n'est opposable ni à ce congé ni à la RCC.",
        'L1234-9': "Le 5° utilise seulement le barème de référence de L. 1234-9 ; la condition d'un an à la fin effective du contrat avec préavis inclus ne ferme pas le minimum de RCC avant un an. Le texte précise années totales, mois complets, six mois pour la part nouvelle et minima de la part ancienne, sans plafond des garanties déjà négociées ni double emploi des services.",
        'L6324-9': "Le 7° bis vise exactement le II de L. 6324-9 : écart de rémunération, prolongation de reconversion, indemnités légales selon la rupture et frais pédagogiques avec accord CPF. Le I proposé retire l'attente de trois mois, que le renvoi ne rétablit pas. La note conserve les actions dont l'avenant est antérieur au 1er janvier 2026 ; aucun terme à l'emploi nouveau ne peut être déduit de la durée de formation."
    },
    'L1251-4': {
        'L1234-1': "Les deux activités autorisées par L. 1251-4 ne créent aucun préavis particulier. Les salariés relevant de la relation privée nouvelle restent dans le champ de L. 1234-1 proposé en cas de rupture patronale, les anciens contrats dans leur régime. L'exercice du placement ne fait pas du placeur l'employeur du candidat et n'applique donc pas artificiellement ce préavis au placement.",
        'L1251-2': "La source et la proposition de L. 1251-2 conservent l'activité exclusive de travail temporaire ; les 1° et 2° de L. 1251-4 restent donc des dérogations opérantes, pour les entreprises futures aussi. La proposition de la cible soumet les recrutements nouveaux au contrat unique et aux garanties d'intermission ; l'ouverture au placement ou temps partagé n'y déroge pas implicitement.",
        'L1221-2': "Le renvoi de définition d'activité n'est pas un cas de CDD : L. 1221-2 proposé impose le contrat nouveau indéterminé, tandis que le temps partagé est déjà indéterminé selon L. 1252-4 consulté. La conservation intégrale des deux dérogations ne ferme pas ces activités futures et ne modifie pas les contrats publics ou leurs statuts.",
        'L1234-9': "Aucune indemnité de rupture n'est fixée par L. 1251-4. Le seuil nouveau d'un an, apprécié à la fin effective avec préavis, et le barème ordinaire de L. 1234-9 ne sont pas une condition d'accès au placement ou au temps partagé. Les garanties spéciales ou antérieures de chaque emploi restent indépendantes de ces possibilités d'activité."
    },
    'L1251-5': {
        'L1234-1': "L. 1234-1 proposé fixe le préavis patronal de quinze jours pour l'emploi nouveau de l'agence et maintient les protections distinctes. La fin d'affectation chez l'utilisateur ne déclenche pas à elle seule ce préavis ni une rupture. Les anciens contrats conservent leurs règles de préavis et de terme dans le champ de la transition.",
        'L1221-2': "Le premier alinéa préserve l'interdiction visant la mission et le deuxième la distingue de l'emploi indéterminé de L. 1221-2 proposé. Un événement de mission ne peut donc terminer automatiquement l'emploi nouveau. La conversion consentie conserve ancienneté et créances ; aucun renouvellement déterminé nouveau n'est permis même si la première mission était ancienne.",
        'L1234-9': "L. 1234-9 proposé s'applique à la rupture patronale de l'emploi de l'agence, avec un an mesuré à la fin effective préavis inclus pour le contrat nouveau. Il ne limite pas les droits de congé, d'ancienneté et de rémunération pendant intermission ni les recours contre l'utilisateur ; le minimum ordinaire et la part ancienne suivent leur régime distinct.",
        'L1251-58-2': "Le deuxième alinéa de la cible officielle assimile les intermissions au travail effectif pour congés et ancienneté ; son écrit comporte huit mentions, dont lettre de mission. Le renvoi de L. 1251-5 conserve ces droits sous contrat unique et ne transforme pas la lettre en nouveau contrat déterminé ; aucun nouvel essai ne découle de la fin d'une affectation.",
        'L1251-58-3': "La garantie mensuelle est au moins le SMIC multiplié par les heures correspondant à la durée légale du mois, compte tenu des rémunérations de mission déjà versées. La proposition la maintient aussi sans mission : le renvoi ne peut la fermer lors de l'achèvement de l'affectation ni promettre une rémunération ajoutée deux fois à celle des missions."
    },
    'L1251-7': {
        'L1234-1': "Les cinq voies de mission ne dispensent pas l'agence employeur du préavis nouveau de quinze jours lorsque l'emploi nouveau est rompu à son initiative selon L. 1234-1 proposé. Le délai concerne la rupture, non une durée minimale de mission ou de formation. Les autorisations et procédures collectives ainsi que les règles des anciens contrats restent distinctes.",
        'L1221-2': "Les 1° à 5° visent l'affectation, l'insertion ou la formation et ne sont pas des cas nouveaux de CDD au regard de L. 1221-2 proposé. Le texte maintient les aides et avantages pour les futurs publics éligibles sous emploi indéterminé, sans transformer une échéance pédagogique ou d'aide en terme d'emploi ni renouveler un ancien CDD après la réforme.",
        'L1234-9': "La fin d'une mission d'insertion, d'apprentissage ou de formation ne constitue pas une rupture patronale ouvrant automatiquement l'indemnité ordinaire de L. 1234-9. Si l'emploi nouveau est rompu par l'employeur, le seuil d'un an se mesure à la fin effective préavis inclus, sur toute l'ancienneté ; les primes, congés et indemnités spéciales restent autonomes et les services anciens protégés.",
        'L1251-6': "La clause introductive 'en plus' conserve les cinq motifs généraux et leurs qualifications propres. Le 3° de la cible proposée définit la saison et la mission temporaire sans terme d'emploi ; la suppression des préalables des 1° et 2° de L. 1251-7 ne supprime pas ces conditions générales, les interdictions de recours ou la protection contre une affectation permanente abusive.",
        'L1251-58-2': "Le renvoi préserve le contrat écrit et les huit mentions existantes, l'ancienneté et les congés des périodes sans mission. L'extension aux nouveaux emplois d'insertion doit être coordonnée avec la section 4 bis dans L. 5132-6 ; elle ne peut rester une simple affirmation si cette exclusion officielle n'est pas réformée. La lettre de mission ne termine aucun emploi nouveau.",
        'L1251-58-3': "La garantie mensuelle reste calculée au moins sur le SMIC et les heures de durée légale, en intégrant les salaires de mission déjà payés. Elle couvre les intermissions dans la proposition fournie. Le renvoi n'est pas une prime supplémentaire ni une baisse de prélèvement : sa généralisation aux nouveaux recrutements auparavant déterminés est une charge patronale recensée.",
        'L5132-6': "La source exclut encore la section 4 bis et prévoit contrats de mission, vingt-quatre mois et embauche en CDD de deux mois pour une dispense de carence. La proposition fournie ouvre le contrat unique, les garanties mensuelles et les dispenses futures sans terme minimal d'emploi ; le 5° de L. 1251-7 ne conserve aucun CDD ni minimum d'un mois, tout en protégeant les missions anciennes et les aides éligibles."
    },
    'L1251-9': {
        'L1234-1': "La suppression du gel de six mois chez l'utilisateur ne supprime pas le préavis de l'emploi du salarié de l'agence. L. 1234-1 proposé exige quinze jours pour les ruptures patronales nouvelles avec protections distinctes ; ni le licenciement économique précédent ni la fin de mission ne dispensent l'employeur de la notification et des règles applicables.",
        'L1251-5': "La vue fournie conserve l'interdiction de pourvoir durablement un poste permanent de l'utilisateur et l'articule aux intermissions. Le présent article retire le seul gel après licenciement économique, sans écarter cette interdiction ni les droits du salarié auprès de l'utilisateur en cas de recours abusif. La version finale du lot conserve cette articulation et sa transition des anciens contrats.",
        'L1221-2': "Le retrait des exceptions du contrat de mission court ne permet pas un nouveau terme d'emploi contraire à L. 1221-2 proposé. La liberté nouvelle porte sur la mise à disposition, avec emploi indéterminé à l'agence pour les recrutements futurs ; les anciens contrats et leurs garanties restent protégés et aucune reconduction déterminée après la réforme n'est autorisée.",
        'L1234-9': "Le nouvel intérimaire conserve l'ancienneté des intermissions pour le seuil d'un an de L. 1234-9, apprécié à la fin effective de l'emploi avec préavis inclus. Le gel supprimé ne change ni ce calcul, ni la part d'ancienneté antérieure des anciens emplois, ni la priorité de réembauche d'un an du salarié précédemment licencié, qui obéit à L. 1233-45.",
        'L1251-6': "Les cinq motifs généraux d'affectation temporaire demeurent requis : le renvoi explicite englobe l'accroissement temporaire du 2° et la saison du 3°, sans convertir cette mission en emploi déterminé. La liberté après licenciement ne crée pas un motif permanent de recours et ne ferme pas les remplacements agricoles ou professionnels dont les régimes restent distincts.",
        'L1251-7': "La vue fournie ouvre cinq voies favorables d'insertion, formation, apprentissage et publics éligibles, en retirant déjà le préalable du 1° et le minimum du 5°. Le présent lot retire aussi le préalable du 2°, avec règles de fond et droits futurs préservés. Le renvoi de L. 1251-9 maintient ces ouvertures et garanties sans recréer les préalables ni une fin automatique d'emploi."
    }
}

checks['L1236-7']['L1234-3'] = "La source de L. 1234-3 fixe le départ historique du préavis à la présentation de la lettre recommandée. La proposition fournie compte les quinze jours calendaires nouveaux à partir du lendemain de la présentation ou, si une autre notification est légalement admise, de la réception ou remise ; la notification écrite du salarié suit le même calcul. Le nouveau renvoi explicite de L. 1236-7 conserve ce mode de calcul, sans avancer le terme effectif pour le seuil ordinaire d'un an ni remplacer les autorisations distinctes. Les contrats antérieurs gardent leur régime."
by_number['L1236-7']['review_notes'] = by_number['L1236-7']['review_notes'].replace("L. 1234-3, absent des cibles fournies, a été lu intégralement dans le corpus public pour le nouveau renvoi", "L. 1234-3, dont la source et la proposition sont fournies dans reference-targets.json, a été lu intégralement pour le nouveau renvoi")
by_number['L1235-15']['review_notes'] = by_number['L1235-15']['review_notes'].replace("L. 1234-3, consulté dans le corpus public, hors des cibles fournies", "L. 1234-3, lu dans les cibles fournies pour L. 1236-7")
by_number['L1237-3']['review_notes'] = by_number['L1237-3']['review_notes'].replace("L. 1237-2 a été consulté dans le corpus public, hors des cibles fournies pour ce renvoi conservé", "Le renvoi explicite à L. 1237-2, nouveau par rapport à la source officielle et déjà présent dans le brouillon, vise une cible non fournie dans reference-targets.json ; cet article a été consulté intégralement dans le corpus public")
by_number['L1237-18-2']['review_notes'] += " Le renvoi explicite à L. 1237-18-4 est nouveau par rapport à la source officielle et vise une cible non fournie dans reference-targets.json : sa source entière, lue localement, réserve la rupture consentie du contrat support à l'issue du congé et les autorisations protectrices ; il ne règle pas le terme de l'emploi de reprise."
by_number['L1251-9']['review_notes'] += " Le renvoi explicite à L. 1251-10 est nouveau par rapport à la source officielle et vise une cible non fournie dans reference-targets.json : son texte entier a été lu dans le corpus public ; il maintient les trois interdictions autonomes et la dérogation favorable pour travaux dangereux, sans prolonger le gel supprimé."

for d in answer:
    key = d['code_id'] + '|' + d['source_id']
    d['reference_checks'] = []
    for target_key in refs['requirements'][key]:
        t = refs['targets'][target_key]
        assessment = checks[d['number']][t['number']]
        d['reference_checks'].append(dict(target_key=target_key, view_sha256=t['view_sha256'], assessment=assessment))

class TextContent(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
    def handle_data(self, data):
        self.parts.append(data)

def plain(xml):
    p = TextContent()
    p.feed(xml)
    return ''.join(p.parts)

# Une seule entrée décrit les deux volets d'une même mesure dans un article.
# On conserve les citations complètes et toutes les limites de la suppression.
si = by_number['L1237-3']['substantive_impact']
e = si['effects'][0]
e['description'] = "Retrait des deux cas de solidarité fondés sur la seule connaissance du contrat précédent, à l'embauche comme pendant la poursuite de l'emploi, sans intervention prouvée dans la rupture abusive."
e['before'] = "Sous la condition générale d'une rupture abusive et d'un dommage, solidarité du nouvel employeur au 2° pour embauche en connaissance du contrat précédent et au 3° pour poursuite de l'emploi après cette connaissance ; le 3° écarte la responsabilité si le terme ou le préavis est expiré ou si quinze jours se sont écoulés lors de l'avertissement."
e['after'] = "Ces deux cas sont supprimés pour les faits nouveaux. Seule l'intervention prouvée dans la rupture abusive maintient la solidarité spéciale ; la seule embauche ou poursuite de l'emploi en connaissance du contrat précédent ne suffit plus. Les fautes personnelles distinctes et la responsabilité du salarié restent réparables."
e['affected_population'] = "Nouveaux employeurs de salariés ayant rompu abusivement un contrat précédent, qu'ils connaissent ce lien dès l'embauche ou en soient informés pendant la poursuite de l'emploi."
e['conditions_and_transition'] = "Faits générateurs à compter de l'entrée en vigueur ; créances, anciennes dispenses de terme, de préavis ou de quinze jours, prescriptions et recours restent soumis au droit antérieur pour les faits anciens. Le délai de l'ancien 3° ne se confond pas avec le nouveau préavis individuel."
e['source_quote'] = plain(source_by_number['L1237-3']['source_xml']).strip()
si['effects'] = [e]

si = by_number['L1251-9']['substantive_impact']
e = si['effects'][0]
e['description'] = "Suppression du gel de six mois après licenciement économique et de ses conditions dérogatoires, y compris l'information-consultation spéciale pour une commande exceptionnelle à l'exportation."
e['before'] = "Sur les postes licenciés dans l'établissement, interdiction d'intérim pour accroissement temporaire pendant six mois, sauf mission d'au plus trois mois non renouvelable ou commande exceptionnelle à l'exportation ; cette seconde exception impose l'information et la consultation préalables du CSE s'il existe. La priorité de réembauche reste due dans les deux cas."
e['after'] = "Aucun gel de six mois ni condition de brièveté, non-renouvellement ou exportation sur ce seul fondement. La consultation propre à l'ancien 2° disparaît avec ce régime ; les consultations autonomes, les autres conditions de recours et la priorité de réembauche restent dues."
e['replacement_or_new_burdens'] = "Aucune demande, consultation, déclaration ou pièce ne remplace le gel et sa consultation dérogatoire. Les procédures collectives autonomes et la priorité de réembauche préexistaient ; les obligations communes du contrat unique sont recensées dans l'effet de coordination distinct, sans réduction supplémentaire comptée."
e['source_quote'] = plain(source_by_number['L1251-9']['source_xml']).strip()
e['proposed_quote'] = '\n'.join(plain(by_number['L1251-9']['proposed_xml']).split('\n')[:3])
si['effects'] = [e, si['effects'][2]]

by_number['L1237-9']['substantive_impact']['effects'][0]['source_quote'] = plain(source_by_number['L1237-9']['source_xml']).strip().split('\n')[-1]

allowed_tags = {'p','br','table','thead','tbody','tfoot','tr','th','td','b','strong','i','em','u','sup','sub','ul','ol','li','div','span','blockquote'}
class ValidateHTML(HTMLParser):
    def handle_starttag(self, tag, attrs):
        assert tag in allowed_tags, tag
        assert all(k in {'rowspan','colspan'} and v and v.isdigit() for k,v in attrs), attrs
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

assert len(answer) == len(sources) == 12
for s, d in zip(sources, answer):
    assert all(d[k] == s[k] for k in ['code_id','source_id','source_sha256','number'])
    si = d['substantive_impact']
    assert si['version'] == 1
    assert all(len(si[k]) >= 40 for k in ['assessment','scope_limitations','new_burdens_review'])
    if d['proposed_xml'] is None:
        assert d['status'] == 'retained_unchanged'
        assert si['classification'] == 'retained_necessary'
        assert si['effects'] == []
    else:
        assert d['status'] == 'rewrite_draft'
        ValidateHTML().feed(d['proposed_xml'])
    if s.get('benefit_check_required'):
        assert len(d['benefit_review']) >= 100
    if d.get('change_type') == 'normative_reduction':
        assert d['reform_policy_id'] == 'editorial_direction_2026_10_19'
        assert d['removed_provisions'] and all(len(t) >= 30 for t in d['removed_provisions'])
    for e in si['effects']:
        assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', e['measure_id']) and 6 <= len(e['measure_id']) <= 96
        for field, xml in [('source_quote',s['source_xml']), ('proposed_quote',d['proposed_xml'])]:
            assert len(e[field]) >= 12, (d['number'], field)
            assert e[field] in plain(xml), (d['number'],field,e[field])
    pairs = [(e['measure_id'], e['kind']) for e in si['effects']]
    assert len(pairs) == len(set(pairs)), (d['number'], 'Duplicate measure and effect in one article')
    assert {c['target_key'] for c in d['reference_checks']} == set(refs['requirements'][d['code_id']+'|'+d['source_id']])
    assert all(len(c['assessment']) >= 80 and c['view_sha256'] == refs['targets'][c['target_key']]['view_sha256'] for c in d['reference_checks'])

Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'output_file':'answer.json','article_count':len(answer), 'proposed_articles':sum(d['proposed_xml'] is not None for d in answer), 'reference_checks':sum(len(d['reference_checks']) for d in answer)}, ensure_ascii=False))
