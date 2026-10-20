import json
import re
from html import unescape
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
by_number = {s['number']: s for s in sources}
answer = []


def plain(xml):
    return unescape(re.sub(r'<[^>]*>', '', xml)).replace('\\n', '\n')


def impact(classification, assessment, limitations, burdens, effects=()):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=limitations, new_burdens_review=burdens, effects=list(effects))


def effect(kind, measure_id, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit, affected_population=population,
                conditions_and_transition=transition, replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


def add(number, proposed, reason, notes, substantive, removed=None, benefit=None):
    source = by_number[number]
    row = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    row.update(proposed_xml=proposed, reason=reason, review_notes=notes,
               status='retained_unchanged' if proposed is None else 'rewrite_draft',
               substantive_impact=substantive)
    if removed:
        row.update(change_type='normative_reduction',
                   reform_policy_id='editorial_direction_2026_10_19',
                   removed_provisions=removed)
    if benefit:
        row['benefit_review'] = benefit
    answer.append(row)
    return row


def previous(number):
    return by_number[number]['previous_draft']['proposed_xml'].replace('\\n', '\n')


add('L1231-4', None,
    "Après lecture de la source et du brouillon entiers, maintien intégral de la source nécessaire : l'interdiction réciproque de renonciation anticipée empêche de vider dès l'embauche les règles de rupture de leur effet. Elle ne demande aucun dossier, prélèvement, autorisation, déclaration ou délai. Le brouillon ne faisait que reformuler cette protection ; il n'est pas reconduit comme une simplification. Aucune réforme de fond supplémentaire n'est justifiée.",
    "L'unique alinéa vise le titre III relatif à la rupture du CDI, applicable au contrat unique dans son champ. Il ne prohibe pas, par lui-même, les ruptures convenues ou transactions licites selon leurs conditions propres. Le préavis individuel de quinze jours et le plafond de six mois de l'indemnité ordinaire n'autorisent aucune renonciation anticipée aux salaires, congés acquis, protections spéciales ou réparations. Les procédures collectives et autorisations protectrices demeurent distinctes. Aucun renvoi numéroté ni chiffre à modifier.",
    impact('retained_necessary',
           "La source officielle entière est conservée : aucune réduction normative ni nouvelle réécriture stylistique n'est revendiquée. Sa fonction est de rendre effectives les garanties impératives de rupture.",
           "Ce maintien ne démontre aucun gain de coût ou de complexité. Il ne tranche pas les régimes autonomes de transaction et ne modifie ni les anciens contrats ni les règles des agents publics.",
           "Aucune charge nouvelle n'est identifiée : le texte source reste intégralement applicable sans nouveau document, donnée, registre, délai ou condition."))

add('L1231-5', None,
    "Maintien intégral nécessaire après examen des trois alinéas et du brouillon. Le rapatriement et le réemploi protègent le salarié envoyé à l'étranger par la société mère contre l'abandon de ses droits par l'organisation du groupe. La reconnaissance du service dans la filiale préserve l'ancienneté. Ces obligations ont une fonction essentielle concrète ; aucun agrément, double justificatif, déclaration ni délai minimal accessoire n'est prévu ici. La reformulation antérieure n'est pas comptée comme une réduction.",
    "Conditions cumulatives conservées : engagement par la mère, mise à disposition d'une filiale étrangère et contrat avec cette filiale ; son licenciement déclenche rapatriement et emploi compatible avec l'importance des fonctions antérieures dans la mère. Le licenciement ultérieur par la mère relève du présent titre. La durée étrangère est reconnue pour l'indemnité et pour le préavis des anciens contrats ; elle ne rallonge pas le préavis fixe du contrat unique nouveau. Pour L. 1234-9 proposé : seuil d'un an à la fin effective, préavis inclus lorsqu'il existe, puis toute l'ancienneté, 0,20 mois par année et fractions en mois complets, plafond légal de six mois ; les composantes anciennes et minima favorables demeurent, sans double compte. La source ne règle ni la loi du contrat étranger ni le statut des agents publics.",
    impact('retained_necessary',
           "La source complète reste inchangée. Le coût de retour et de réemploi demeure une protection liée à la décision d'expatriation de la mère ; aucune baisse de prélèvement ou suppression d'obligation n'est démontrée ici.",
           "L'application du droit international privé et l'affectation de l'ancienneté entre composantes anciennes et nouvelles nécessitent leur examen propre ; aucun coût agrégé n'est calculé.",
           "Aucune charge nouvelle n'est identifiée : maintien des seules obligations de rapatriement, de réemploi et de reprise d'ancienneté qui existent dans les trois alinéas sources."),
    benefit="Le rapatriement, le nouvel emploi compatible et la reprise du temps passé dans la filiale sont trois garanties favorables conservées intégralement, y compris pour les futures mises à disposition répondant aux conditions de la source. Aucun avantage n'est réservé aux seuls détachements antérieurs.")

add('L1232-1', None,
    "Maintien intégral nécessaire des deux alinéas sources. La cause réelle et sérieuse et sa motivation rendent le motif patronal contrôlable et permettent au salarié de se défendre. Ce ne sont ni deux dépôts administratifs ni deux pièces en double. Les supprimer neutraliserait une protection expressément conservée dans la section travail de la coordination. Le brouillon à droit constant est écarté comme simple changement de mots ; aucune coupe supplémentaire n'est retenue.",
    "Le champ est celui du licenciement pour motif personnel ; l'adaptation économique de L. 1233-3 reste distincte. Les allègements de L. 1232-2 et L. 1232-6 ne retirent pas ces deux exigences. L. 1235-2 et R. 1232-13, lus en entier dans le corpus public, conservent les précisions de motifs et leurs conditions : les quinze jours de ces précisions ne sont pas le préavis du contrat unique. Harmoniser leur vocabulaire de lettre avec les notifications écrites admises, sans supprimer les demandes du salarié, les limites du litige ou les recours. Aucune procédure collective ou autorisation spéciale n'est écartée.",
    impact('retained_necessary',
           "Aucun changement réel par rapport à la source entière : maintien de la justification et de la motivation du licenciement personnel, nécessaires à la défense et au contrôle du juge.",
           "L'article ne fixe ni durée de préavis ni barème d'indemnité ; leurs modifications dans d'autres articles ne sont pas des réductions réalisées ici. Aucun solde économique n'est établi.",
           "Aucune charge nouvelle n'est identifiée : les deux exigences sources subsistent sans formulaire, registre, autorisation ni délai additionnel."))

p2 = previous('L1232-2')
add('L1232-2', p2,
    "Réforme de fond conservée après seconde lecture : retrait de l'exclusivité du recommandé ou de la remise contre décharge et du minimum uniforme de cinq jours ouvrables. Le brouillon intégral est reconduit, sans nouvelle retouche stylistique. L'entretien avant décision, la preuve de la convocation et le temps réel de préparation et d'assistance restent nécessaires ; les couper davantage supprimerait la défense. Le report individualisé est explicite et est recensé comme contrepartie, sans le confondre avec une absence totale de délai.",
    "Les trois alinéas sources gardent leur place ; la transition est ajoutée à la fin. Convocations nouvelles : tous les moyens écrits donnant preuve du contenu et date certaine de réception sont admis ; pour le recommandé, première présentation. Un simple envoi de courriel ne prouve pas sa réception. Le report doit permettre les droits effectifs de L. 1232-4, sans nouveau délai forfaitaire. R. 1232-1 et R. 1232-2 ont été lus intégralement : objet, date, heure, lieu, rappel d'assistance et information du conseiller et de l'employeur gardent leur utilité ; adapter le terme de lettre sans réintroduire les modes exclusifs. Le préavis de quinze jours commence après notification de rupture, non après convocation. L. 1233-11 à L. 1233-13 et les procédures collectives restent hors de cette réduction. La compatibilité de l'organisation individualisée avec les garanties de défense, notamment l'article 7 de la convention OIT n° 158, appelle une vérification supérieure distincte ; ce texte extérieur n'est pas fourni ici et aucune conformité n'est présumée.",
    impact('mixed',
           "Par rapport aux trois alinéas officiels, deux contraintes sont réellement retirées : supports exclusifs et attente fixe de cinq jours ouvrables. Le temps nécessaire et le report demandé pour une défense effective les remplacent partiellement ; le gain net de délai ou de coût n'est pas établi pour chaque procédure.",
           "La réduction vise les convocations adressées à compter de l'entrée en vigueur, y compris concernant un ancien contrat ; elle ne réduit pas son préavis. Aucune durée totale de licenciement en quinze jours ni économie nationale n'est démontrée.",
           "La préparation effective et le report nécessaire sont rendus expressément obligatoires, avec appréciation individualisée. Les moyens alternatifs exigent une preuve de contenu et de réception. Aucun registre, dépôt, attestation ou déclaration nouvelle n'est imposé ; le solde net de ces contreparties n'est pas chiffré.",
           [effect('compliance_cost_reduced', 'licenciement-convocation-support-libre',
                   "Fin des deux supports exclusivement admis pour convoquer le salarié.",
                   "Convocation seulement par recommandé ou lettre remise en main propre contre décharge.",
                   "Ces deux voies restent ouvertes ; tout autre écrit prouvant contenu et date de réception est admis.",
                   'legal_duty', "Employeurs et salariés concernés par l'entretien préalable pour motif personnel.",
                   "Convocations adressées après l'entrée en vigueur ; procédures déjà convoquées sous l'ancien régime.",
                   "Preuve exigée pour l'alternative ; aucun dépôt de remplacement ni chiffrage du coût évité.",
                   "La convocation est effectuée par lettre recommandée ou par lettre remise en main propre contre décharge.",
                   "ou transmise par tout autre moyen écrit permettant d'établir son contenu et de donner date certaine à sa réception par le salarié."),
            effect('deadline_reduced', 'licenciement-preparation-sans-delai-forfaitaire',
                   "Suppression du minimum uniforme de cinq jours ouvrables avant entretien.",
                   "Au moins cinq jours ouvrables après présentation du recommandé ou remise de la convocation.",
                   "Aucun minimum général chiffré ; temps de préparation et d'assistance effectivement nécessaire.",
                   'working_days', "Salariés convoqués et employeurs envisageant un licenciement personnel.",
                   "Convocations nouvelles seulement ; aucun entretien imposé sans possibilité effective de défense.",
                   "Un délai individualisé et un report nécessaire subsistent ; aucune économie uniforme de cinq jours n'est affirmée.",
                   "L'entretien préalable ne peut avoir lieu moins de cinq jours ouvrables après la présentation de la lettre recommandée ou la remise en main propre de la lettre de convocation.",
                   "L'entretien n'est soumis à aucun délai minimal général chiffré à compter de la convocation."),
            effect('obligation_added', 'licenciement-preparation-sans-delai-forfaitaire',
                   "Contrepartie explicite de l'attente fixe supprimée : reporter l'entretien si la défense ne peut être effectivement préparée.",
                   "L'article source impose un minimum de cinq jours ouvrables et ne formule pas ce devoir individualisé de report.",
                   "À la demande du salarié, report pour le temps nécessaire à la préparation et à l'assistance effectives.",
                   'legal_duty', "Employeurs ayant choisi une convocation relevant du régime nouveau.",
                   "Même transition que la suppression du minimum ; condition liée à l'exercice effectif des droits.",
                   "Appréciation individualisée et éventuel report ; aucun justificatif standard supplémentaire exigé.",
                   "L'entretien préalable ne peut avoir lieu moins de cinq jours ouvrables",
                   "À la demande du salarié, l'entretien est reporté lorsque le temps laissé ne permet pas l'exercice effectif de ces droits ; le report porte sur le temps nécessaire à leur exercice.")]),
    removed=["Exclusivité de la lettre recommandée ou de la lettre remise en main propre contre décharge pour toute convocation nouvelle.",
             "Attente minimale générale de cinq jours ouvrables avant l'entretien, remplacée par la préparation et l'assistance effectives."])

add('L1232-3', None,
    "Maintien intégral de l'alinéa officiel après lecture du brouillon : exposer les motifs envisagés et recueillir les explications sont les deux fonctions essentielles de l'entretien. L'article ne demande aucun compte rendu, rapport ou procès-verbal distinct susceptible d'être supprimé. Les délais fixes étant allégés dans les articles voisins, la défense avant décision doit rester effective. La version purement stylistique n'est pas reconduite comme une réforme.",
    "La décision est encore envisagée pendant l'entretien ; les explications doivent pouvoir influer sur elle. L. 1232-2 conserve le temps nécessaire et L. 1232-4 l'assistance ; L. 1232-6 autorise une notification sans attente fixe après examen des explications. Aucun nouveau renvoi n'est introduit dans l'article et aucun document de restitution n'en est déduit. Le préavis, l'indemnité ordinaire et les autorisations spéciales ont leurs champs propres.",
    impact('retained_necessary',
           "La source entière est maintenue sans modification : les deux composantes de l'audition restent nécessaires au contrôle du motif et ne constituent pas des formalités administratives doublonnées.",
           "Aucune réduction du nombre d'entretiens ni de coût n'est démontrée ici. Les simplifications des articles de convocation et de notification ne sont pas recomptées comme effets de cet alinéa.",
           "Aucune charge nouvelle n'est identifiée : ni compte rendu, ni procès-verbal, ni donnée, ni délai nouveau ; maintien des seuls échanges exigés par la source."))

p4 = previous('L1232-4')
add('L1232-4', p4,
    "Réduction de fond déjà acquise, maintenue sans nouvelle modification du brouillon : les adresses des services ne sont plus systématiquement imposées si la liste officielle à jour ou un accès officiel effectif et gratuit sont donnés. Le droit de choisir un assistant du personnel et, en l'absence de représentants, un conseiller officiel reste entier. Supprimer la liste, le choix ou l'information neutraliserait la défense ; aucune coupe supplémentaire n'est justifiée. L'accès de secours à fournir est recensé comme contrepartie nouvelle de la faculté.",
    "Les trois alinéas sont conservés, suivis de la transition par date d'envoi de la convocation. Le deuxième alinéa reste réservé aux entreprises sans institutions représentatives. L. 1232-7 et D. 1232-5 ont été lus intégralement : liste préfectorale publiée et mise à disposition dans chaque section d'inspection et chaque mairie. Leur maintien ne suppose pas une nouvelle liste privée ni collecte des coordonnées par l'employeur. R. 1232-1 et R. 1232-2 conservent les informations et démarches utiles à l'assistance ; leur vocabulaire de lettre est à harmoniser. Le salarié n'est pas tenu d'utiliser un support numérique. Les garanties autonomes du conseiller ne sont pas abrogées ; leurs textes hors lot ne sont pas déclarés réécrits. La préparation effective de L. 1232-2 ne devient ni préavis de rupture ni délai général chiffré.",
    impact('mixed',
           "La source imposait les adresses des services dans la convocation. La proposition offre une alternative d'accès direct à la liste officielle, mais ajoute une obligation de secours si cet accès échoue ; le gain net de conformité dépend du moyen choisi.",
           "La dispense porte seulement sur l'indication des adresses, pas sur l'assistance ou la liste officielle. Elle vaut pour les convocations nouvelles ; aucun gain monétaire global ni raccourcissement automatique n'est établi.",
           "Le recours à l'alternative exige une liste officielle à jour et un accès effectif gratuit ; en cas d'échec, l'employeur doit donner accès sans frais avant l'entretien. Cette contrepartie est explicitement nouvelle par rapport à l'article source ; aucun registre, attestation ou déclaration n'est créé.",
           [effect('compliance_cost_reduced', 'licenciement-acces-liste-conseillers',
                   "Dispense conditionnelle de reproduire les adresses des services tenant la liste.",
                   "La convocation mentionne le conseiller et précise les adresses des services où la liste est accessible.",
                   "Mention du conseiller maintenue ; adresses facultatives si liste officielle à jour ou accès officiel effectif et gratuit.",
                   'legal_duty', "Employeurs et salariés des entreprises dépourvues d'institutions représentatives.",
                   "Convocations adressées à compter de l'entrée en vigueur ; ancien régime pour les précédentes.",
                   "Alternative facultative avec accès de secours à la charge de l'employeur, sans seconde déclaration.",
                   "précise l'adresse des services dans lesquels la liste de ces conseillers est tenue à sa disposition.",
                   "L'indication de ces adresses n'est pas exigée si la convocation comporte la liste officielle à jour ou une référence officielle permettant au salarié de la consulter effectivement et gratuitement."),
            effect('obligation_added', 'licenciement-acces-liste-conseillers',
                   "Garantie d'accès de secours lorsque l'alternative aux adresses ne fonctionne pas pour le salarié.",
                   "L'article impose des adresses de services ; il ne met pas expressément l'accès de secours à la charge de l'employeur.",
                   "L'employeur ayant choisi une référence inutilisable doit donner accès sans frais avant l'entretien.",
                   'legal_duty', "Employeurs utilisant l'alternative et salariés ne pouvant consulter effectivement la liste.",
                   "Uniquement dans le nouveau régime de convocation et si l'accès indiqué n'est pas effectif.",
                   "Devoir résiduel nouveau d'accès gratuit ; aucune preuve formalisée ni collecte nouvelle n'est demandée.",
                   "la liste de ces conseillers est tenue à sa disposition.",
                   "Si le moyen indiqué ne lui permet pas cette consultation, l'employeur lui donne accès sans frais à cette liste avant l'entretien.")]),
    removed=["Indication obligatoire des adresses des services dans toute convocation lorsque l'accès direct effectif à la liste officielle rend cette indication redondante."],
    benefit="Le choix d'un assistant appartenant au personnel est conservé ; en l'absence d'institutions représentatives, le salarié peut toujours choisir un conseiller sur la liste officielle. L'information et l'accès gratuit restent effectifs pour les convocations futures, avec un secours si la référence ne peut être consultée. La dispense nouvelle profite à l'employeur sans fermer l'assistance au salarié.")

p5 = previous('L1232-5')
add('L1232-5', p5,
    "Coordination normative du pouvoir réglementaire conservée après relecture, sans nouvelle retouche : ses modalités utiles d'organisation de l'entretien restent nécessaires, mais elles ne peuvent rétablir supports exclusifs, attente générale ou adresses devenues facultatives. Il ne s'agit pas de trois suppressions indépendantes supplémentaires : les mesures sont portées par L. 1232-2 et L. 1232-4. Abroger toute l'habilitation priverait de fondement des modalités utiles d'assistance, sans suppression ciblée mieux justifiée.",
    "L'habilitation concerne seulement la section de l'entretien préalable. R. 1232-1 et R. 1232-2 lus entièrement fixent date, heure, lieu, rappel de l'assistance et information du conseiller et de l'employeur ; D. 1232-5 organise la liste publique. Ils ne sont pas abrogés dans ce lot. Les transitions de L. 1232-2 et L. 1232-4 gardent les procédures antérieures sous leur ancien régime ; les limitations du pouvoir réglementaire visent les procédures bénéficiant de leurs nouvelles règles. Aucun formulaire exclusif, dépôt ou confirmation de remplacement ne peut être déduit de l'habilitation générale. Les deux cibles explicites sont fournies dans reference-targets.json.",
    impact('coordination_only',
           "Par rapport à l'habilitation générale officielle, le pouvoir réglementaire est expressément borné pour assurer les trois allègements législatifs voisins. Ces limites ne constituent pas trois nouvelles réductions à additionner aux articles porteurs.",
           "Les règlements d'organisation ne sont pas réécrits ici. Le contrôle de tous leurs effets et de leurs modifications futures reste distinct ; aucun solde de coût n'est quantifié.",
           "Aucune charge nouvelle n'est identifiée : l'habilitation existante est conservée et limitée, sans nouvelle compétence d'exiger des données, registres, déclarations ou délais.",
           [effect('coordination', 'licenciement-convocation-support-libre',
                   "Interdiction réglementaire de rétablir l'exclusivité des modes de convocation.",
                   "Habilitation générale à fixer les modalités de la section.",
                   "Même habilitation, limitée par le libre choix des moyens admis à L. 1232-2.",
                   'legal_duty', "Pouvoir réglementaire et procédures d'entretien relevant du régime nouveau.",
                   "Suit la transition de L. 1232-2 ; pas d'abrogation des garanties réglementaires utiles.",
                   "Aucun remplacement ; coordination de la mesure portée par L. 1232-2.",
                   "Un décret en Conseil d'Etat détermine les modalités d'application de la présente section.",
                   "Il ne peut imposer un mode exclusif de convocation parmi les moyens admis à l'article L. 1232-2"),
            effect('coordination', 'licenciement-preparation-sans-delai-forfaitaire',
                   "La réduction du minimum légal ne peut être annulée par un minimum réglementaire général.",
                   "Habilitation générale pour la section d'entretien.",
                   "Pas de délai minimal général chiffré imposable par ce décret ; préparation effective maintenue.",
                   'working_days', "Pouvoir réglementaire et parties aux entretiens du régime nouveau.",
                   "Anciennes procédures régies par la transition de L. 1232-2.",
                   "Aucun nouveau délai ; effet de coordination de la suppression déjà portée par L. 1232-2.",
                   "détermine les modalités d'application de la présente section.",
                   "fixer un délai minimal général chiffré entre la convocation et l'entretien"),
            effect('coordination', 'licenciement-acces-liste-conseillers',
                   "Le décret ne peut neutraliser l'alternative aux adresses prévue dans L. 1232-4.",
                   "Habilitation générale pour organiser l'entretien et l'assistance.",
                   "Les adresses ne peuvent redevenir obligatoires quand la dispense légale s'applique.",
                   'legal_duty', "Pouvoir réglementaire et employeurs utilisant l'alternative de L. 1232-4.",
                   "Suit la transition des convocations de L. 1232-4, sans réouverture des procédures passées.",
                   "Aucune nouvelle obligation ; pas de seconde réduction comptée.",
                   "Un décret en Conseil d'Etat détermine les modalités d'application",
                   "ni imposer l'indication des adresses des services lorsque la dispense prévue à l'article L. 1232-4 est applicable.")]),
    removed=["Faculté réglementaire de rétablir les supports exclusifs, le minimum général d'attente et les adresses obligatoires supprimés dans les seuls champs nouveaux de L. 1232-2 et L. 1232-4."])

p6 = previous('L1232-6')
old_models = "Un arrêté du ministre chargé du travail fixe les modèles que l'employeur peut utiliser pour notifier le licenciement ; leur utilisation est facultative."
new_models = "L'employeur peut utiliser les modèles de notification mis à disposition par le ministre chargé du travail. Leur utilisation est facultative et la notification n'est subordonnée ni à leur établissement ni à leur actualisation par arrêté."
assert old_models in p6
p6 = p6.replace(old_models, new_models)
add('L1232-6', p6,
    "Réformes acquises conservées : retrait du recommandé avec avis de réception obligatoire, du minimum de deux jours ouvrables après entretien et du doublon disciplinaire de ce minimum. Coupe supplémentaire par rapport au brouillon : suppression de l'obligation ministérielle d'établir les modèles par arrêté ; les modèles restent utilisables, leur absence ou défaut d'actualisation ne bloquent pas la notification. L'écrit prouvable, la motivation, l'examen des explications, le maximum disciplinaire d'un mois et les procédures spéciales demeurent nécessaires. Quatre alinéas conservés dans leur ordre, puis transition.",
    "L. 1234-3 fourni distingue le départ du préavis ancien et le décompte nouveau : pour le contrat unique, lendemain de première présentation ou de réception/remise certaine, expiration à la fin du quinzième jour calendaire même non travaillé. La substitution de réception est opératoire dans l'alinéa 1, y compris pour la notification alternative d'un ancien contrat dont la durée de préavis reste protégée. Le renvoi exprès ajouté à L. 1332-2 n'est pas une cible fournie dans reference-targets.json ; cet article a été lu intégralement dans le corpus : seule son attente minimale est écartée ici pour le licenciement ; maximum d'un mois conservé, autres sanctions hors champ. Coordonner expressément son dernier alinéa hors lot. L. 1235-2 et R. 1232-13 lus en entier : maintenir précisions et recours, harmoniser les mentions de lettre et modes écrits sans confondre leurs quinze jours avec le préavis. Les règles économiques, autorisations protectrices et procédures collectives restent applicables. Les modèles et leur arrêté extérieur ne sont pas fournis intégralement : retirer l'obligation d'un arrêté pour leur établissement ou actualisation, tout en conservant leur usage facultatif ; la source ne faisait déjà pas de cet arrêté une condition de validité de chaque notification. Aucun modèle ou annexe extérieure n'est réputé vérifié ou réécrit.",
    impact('material_reduction',
           "La comparaison avec les quatre alinéas officiels démontre le retrait d'un support exclusif, de l'attente fixe de deux jours ouvrables et de l'obligation d'un arrêté de modèles. Le doublon disciplinaire est écarté dans le même champ. Les exigences essentielles préexistantes de décision motivée après audition sont conservées ; aucun montant global économisé n'est avancé.",
           "Les procédures convoquées avant la réforme restent sous l'ancien article. Les délais économiques, collectifs, protecteurs et le maximum disciplinaire ne sont pas raccourcis. L'effet pratique de la suppression de l'arrêté de modèles n'est pas chiffré.",
           "Aucune charge nouvelle autonome n'est identifiée : motivation et audition existaient déjà ; contenu et réception prouvables conditionnent seulement les nouveaux moyens facultatifs. Ni registre, ni rapport d'examen, ni nouvelle déclaration, ni modèle imposé n'est créé. Les reports nécessaires de L. 1232-2 sont recensés dans cet article porteur.",
           [effect('compliance_cost_reduced', 'licenciement-notification-support-libre',
                   "Fin du recommandé avec avis de réception comme unique support légal de notification.",
                   "Notification patronale par lettre recommandée avec avis de réception.",
                   "Écrit motivé, recommandé, remise contre décharge ou autre moyen donnant preuve du contenu et date certaine de réception.",
                   'legal_duty', "Employeurs et salariés concernés par une procédure de licenciement pour motif personnel nouvelle.",
                   "Convocation adressée à compter de l'entrée en vigueur ; durée des préavis des anciens contrats conservée.",
                   "Réception et contenu doivent pouvoir être prouvés ; aucune déclaration de remplacement.",
                   "il lui notifie sa décision par lettre recommandée avec avis de réception.",
                   "ou tout autre moyen écrit permettant d'établir le contenu de la notification et de donner date certaine à sa réception."),
            effect('deadline_reduced', 'licenciement-notification-sans-attente',
                   "Suppression du minimum de deux jours ouvrables, avec neutralisation du même minimum disciplinaire.",
                   "Envoi au moins deux jours ouvrables après la date prévue de l'entretien.",
                   "Notification après entretien et examen des explications, sans attente fixe ; absence du salarié traitée après date et heure prévues, reports nécessaires inclus.",
                   'working_days', "Licenciements personnels, y compris disciplinaires, relevant de la nouvelle procédure.",
                   "Anciennes convocations sous l'ancien régime ; maximum disciplinaire d'un mois et procédures spéciales conservés.",
                   "L'examen des explications n'impose pas un document distinct ; pas de délai général de remplacement.",
                   "Elle ne peut être expédiée moins de deux jours ouvrables après la date prévue de l'entretien préalable au licenciement auquel le salarié a été convoqué.",
                   "La notification peut être adressée après l'entretien préalable et après examen des explications du salarié, sans délai minimal d'attente."),
            effect('obligation_removed', 'licenciement-modeles-sans-arrete-obligatoire',
                   "Suppression de l'obligation d'établir les modèles de notification par arrêté, sans retirer leur usage facultatif.",
                   "Un arrêté ministériel doit fixer les modèles utilisables par l'employeur.",
                   "Les modèles mis à disposition restent facultatifs ; leur établissement ou actualisation par arrêté ne conditionne pas la notification.",
                   'legal_duty', "Ministre chargé du travail ; employeurs souhaitant utiliser des modèles.",
                   "Régime des procédures convoquées à compter de l'entrée en vigueur ; usage des modèles déjà disponibles possible.",
                   "Aucun formulaire, agrément ou déclaration remplaçant l'arrêté obligatoire.",
                   "Un arrêté du ministre chargé du travail fixe les modèles que l'employeur peut utiliser pour procéder à la notification du licenciement.",
                   "la notification n'est subordonnée ni à leur établissement ni à leur actualisation par arrêté.")]),
    removed=["Exclusivité du recommandé avec avis de réception pour notifier les licenciements relevant de la nouvelle procédure.",
             "Attente minimale de deux jours ouvrables après l'entretien, y compris le minimum identique de L. 1332-2 pour le seul licenciement disciplinaire.",
             "Obligation pour le ministre de fixer par arrêté les modèles de notification, qui demeurent librement utilisables lorsqu'ils sont mis à disposition."])

p67 = previous('L1233-67')
add('L1233-67', p67,
    "Brouillon de fond conservé après examen complet, sans nouvelle reformulation : fin de la défalcation du versement CSP supprimé pour les nouvelles adhésions et paiement de l'équivalent intégral du préavis au salarié. Cette obligation directe nouvelle est une contrepartie du retrait du prélèvement, pas une économie patronale acquise. Coordination des périodes de travail au contrat unique, sans nouveau CDD ni renouvellement, avec avantages futurs maintenus. La prescription avec information, les indemnités, le CPF, le statut de stagiaire et les possibilités de travail conservent des fonctions nécessaires ; aucune coupe supplémentaire ne peut les retirer sans fermer des droits.",
    "Cinq alinéas conservés. Douze mois à compter de l'adhésion, opposables seulement si mentionnés dans la proposition de CSP. L. 1233-68 fourni est une proposition, non le droit en vigueur : son 3° coordonne déjà les contrats nouveaux au contrat unique et son 10° b réserve déjà le versement aux anciennes adhésions ; l'ancienne note prétendant ce b encore non coordonné est corrigée. L. 1233-69 ci-dessous supprime le versement aux financeurs pour les nouvelles adhésions mais conserve les créances anciennes. Le CSP constitue une rupture volontaire spéciale sans préavis exécuté : la fin effective est l'adhésion, non la fin de l'accompagnement. Le renvoi légal à L. 1234-9 reste soumis à ses conditions propres ; ne pas ajouter quinze jours fictifs d'emploi pour atteindre un an. Le terme hypothétique du préavis demeure la référence expressément donnée pour l'indemnité conventionnelle et pour le montant représentatif versé ; le décompte est rattaché à la notification qui aurait eu lieu à l'adhésion, conformément à L. 1234-3, cible non fournie pour cet article mais lue dans le paquet de références pour L. 1232-6. Les règles d'accord plus favorables de calcul du CSP doivent être confrontées à l'accord agréé extérieur non fourni ; aucune extinction de ces avantages n'est décidée. R. 1234-1, R. 1234-2 et R. 1234-4 lus dans le corpus : mois complets, première année entière dans le calcul une fois le seuil atteint, salaire de référence distinct de la date d'ancienneté. La note antérieure demandant de remplacer les mois complets est retirée comme contraire à la décision actuelle. Seuil ordinaire, zéro et plafond ne limitent ni versement en lieu de préavis, ni congés, ni réparations, ni indemnités spéciales, ni aides. Les textes CSP extérieurs et leurs conditions plus favorables ne sont pas réputés réécrits.",
    impact('mixed',
           "Face à la source entière, la proposition retire la déduction au profit du financeur pour les nouvelles adhésions, mais impose à l'employeur le paiement intégral équivalent au salarié. Elle ferme le renvoi autorisant des emplois nouveaux à durée déterminée tout en conservant accompagnement, CPF et droits futurs. Aucune diminution nette du coût patronal de cette réaffectation n'est démontrée.",
           "Les adhésions anciennes gardent le solde et la défalcation antérieurs ; les anciens contrats gardent leur durée hypothétique de préavis. L'accord agréé CSP, son financement et ses garanties de calcul nécessitent coordination hors lot ; le déficit éventuel des financeurs n'est pas chiffré.",
           "Une obligation directe nouvelle porte sur l'équivalent intégral du préavis au salarié, au lieu du seul solde après défalcation. Le maintien de l'emploi en CDI succède aux périodes en CDD nouvelles : ce n'est pas une baisse générale d'obligations. Aucun registre ou dossier nouveau n'est prévu ; le solde net global des coûts n'est pas établi.",
           [effect('coordination', 'csp-versement-preavis',
                   "Fin de la défalcation coordonnée avec le retrait du versement au financeur de L. 1233-69 ; aucune seconde suppression de prélèvement comptée.",
                   "Le salarié reçoit le cas échéant le solde de l'indemnité compensatrice hypothétique après défalcation du versement de financement.",
                   "Pour les nouvelles adhésions, aucun versement supprimé n'est défalqué ; les sommes vont directement au salarié selon le nouvel alinéa.",
                   'financing', "Salariés adhérant au CSP et employeurs qui leur proposent ce dispositif.",
                   "Nouvelles adhésions à compter de l'entrée en vigueur ; solde ancien maintenu pour adhésions antérieures.",
                   "Paiement direct intégral institué par la même réforme ; financement du CSP à coordonner, sans recette inventée.",
                   "après défalcation du versement de l'employeur représentatif de cette indemnité mentionné au 10° de l'article L. 1233-68.",
                   "aucun versement supprimé par l'article L. 1233-69 n'est déduit"),
            effect('obligation_added', 'csp-versement-preavis',
                   "Paiement patronal intégral au salarié en lieu du seul solde : charge de remplacement explicitement recensée.",
                   "Seulement le solde éventuel au salarié ; le montant représentatif plafonné à trois mois augmenté des cotisations allait au financeur selon L. 1233-69.",
                   "Totalité de l'indemnité compensatrice hypothétique au salarié : quinze jours calendaires pour le contrat nouveau, durée antérieure pour l'ancien contrat, régimes sociaux et fiscaux du préavis.",
                   'financing', "Employeurs et bénéficiaires des adhésions CSP nouvelles, indépendamment du seuil ordinaire de licenciement.",
                   "Notification économique hypothétique à la date de l'adhésion ; aucun préavis exécuté ni ancienneté fictive d'accompagnement.",
                   "Obligation remplaçant la destination financière antérieure ; cotisations sur les sommes versées non supprimées par cet article.",
                   "au solde de ce qu'aurait été l'indemnité compensatrice de préavis en cas de licenciement",
                   "le salarié reçoit de l'employeur la totalité du montant de l'indemnité compensatrice de préavis qui aurait été due si le licenciement économique avait été notifié à la date de l'adhésion."),
            effect('coordination', 'cdd-contrat-unique',
                   "Le renvoi aux périodes de travail ne peut plus autoriser un nouvel emploi à terme, sans fermer aides et exonérations futures.",
                   "Renvoi au 3° de L. 1233-68, dont la source autorise CDD et contrats de travail temporaire pour les périodes de travail.",
                   "Emploi nouveau à durée indéterminée ; fin d'accompagnement sans terme de l'emploi ; anciens contrats et avantages éligibles futurs conservés.",
                   'regime', "Bénéficiaires du CSP reprenant un emploi et employeurs de ces périodes de travail.",
                   "Contrats nouveaux à compter de l'entrée en vigueur ; anciens CDD et missions sous leurs transitions, sans nouveau renouvellement à terme.",
                   "Maintien de l'emploi hors période d'accompagnement selon ses règles de rupture ; pas de dossier ou déclaration nouvelle.",
                   "Le contrat de sécurisation professionnelle peut comprendre des périodes de travail réalisées dans les conditions prévues au 3° de l'article L. 1233-68.",
                   "Les contrats de travail conclus à compter de l'entrée en vigueur de la loi instituant le contrat de travail unique sont à durée indéterminée ; la fin d'une période de travail, de formation ou d'accompagnement ne rompt pas ces contrats.")]),
    removed=["Défalcation du versement patronal de financement du CSP sur les droits au préavis des nouvelles adhésions, avec paiement direct intégral de remplacement au salarié.",
             "Possibilité de fonder un nouveau CDD ou un renouvellement à durée déterminée sur le renvoi aux périodes de travail du CSP."],
    benefit="Sont maintenus pour les futures adhésions éligibles : indemnité légale selon son régime propre, indemnités conventionnelles, équivalent du préavis sans défalcation du versement supprimé, régime social et fiscal de ce versement, CPF, statut de stagiaire et accès aux périodes de travail. Les aides, exonérations et droits sociaux suivent les situations de même objet sous contrat unique ; les anciens soldes et droits restent protégés. Les conditions plus favorables de l'accord CSP extérieur ne sont pas supprimées par la présente réécriture.")

p69 = previous('L1233-69')
add('L1233-69', p69,
    "Suppression prospective acquise conservée dans le texte intégral du brouillon : versement patronal représentatif du préavis au financeur CSP, majoration et circuit de calcul/exigibilité/recouvrement supprimés pour les nouvelles adhésions. Ils subsistent pour les seules créances anciennes. Les contributions publiques facultatives et les droits des bénéficiaires ne peuvent être retirés sans fermer des avantages. Aucun prélèvement de remplacement n'est créé. Toutefois L. 1233-67 attribue désormais l'équivalent intégral du préavis au salarié : l'effet économique est une réaffectation de financement à analyser, pas une baisse patronale du montant intégral ancien.",
    "Transition par date d'adhésion, non de paiement : plafond de trois mois et cotisations afférentes conservés pour les adhésions anciennes ; créances, recouvrements, restitutions, prescriptions et recours sauvegardés, sans remboursement rétroactif général. L. 1233-68 fourni réserve déjà son 10° b aux adhésions anciennes ; maintenir cette coordination et empêcher accord ou décret de recréer le versement. Le renvoi exprès ajouté à L. 1233-66 n'est pas une cible fournie dans reference-targets.json ; sa source et celle de L. 5422-16 ont été lues intégralement dans le corpus : contribution distincte de deux mois, portée à trois en cas d'adhésion après défaut de proposition, conservée ; limiter le recouvrement relatif à L. 1233-69 aux seules adhésions antérieures, sans toucher au recouvrement général. L. 5427-1 lu identifie organisme gestionnaire et recouvreurs, dont les règles distinctes ne sont pas supprimées. D. 1233-49 lu maintient un financement par les opérateurs de compétences de 20 % du coût pédagogique, hors transport, repas et hébergement : son renvoi à L. 1233-69 est préexistant alors que la source législative ne nomme plus ces opérateurs ; le signaler et le coordonner sans supprimer silencieusement cet autre financement. L. 6341-1 conserve plusieurs financeurs des stagiaires. Le renvoi régional à L. 214-13 du code de l'éducation, hors cinq codes et non fourni, est conservé à son champ, sans le transformer en règle de contrat privé. L'accord agréé CSP extérieur et les textes financiers hors lot restent à coordonner. La perte de financement n'est ni compensée ni chiffrée par hypothèse ; les droits ne sont pas subordonnés à un financement futur supposé. Cotisations normalement dues sur les sommes allant au salarié maintenues.",
    impact('financing_transfer',
           "Le versement représentatif du préavis aux financeurs du CSP est effectivement retiré pour les nouvelles adhésions, mais L. 1233-67 en dirige l'équivalent intégral vers le salarié. Il existe un changement de destinataire et un retrait du circuit de recouvrement, sans preuve d'une baisse nette correspondante de la charge patronale ni d'une économie publique.",
           "Les dettes des adhésions anciennes et la contribution pour défaut de proposition subsistent. Le financement des allocations, formations et aides conservées reste à documenter avec l'accord CSP et les financeurs ; aucun solde consolidé ni recette compensatrice n'est établi.",
           "Aucun prélèvement, registre ou déclaration nouvelle n'est créé ici. La charge de remplacement est le paiement direct intégral au salarié dans L. 1233-67, avec ses cotisations propres. Son existence interdit de présenter le montant brut du versement retiré comme une économie nette ; les coûts administratifs résiduels ne sont pas chiffrés.",
           [effect('financing_transfer', 'csp-versement-preavis',
                   "Suppression du versement de financement au titre du préavis et réaffectation coordonnée au salarié, sans baisse fictive de prélèvement net.",
                   "Employeur : versement représentatif de l'indemnité compensatrice de préavis, dans la limite de trois mois de salaire majoré des cotisations et contributions obligatoires ; seul solde éventuel au salarié selon L. 1233-67.",
                   "Zéro versement de ce fondement au financeur pour les nouvelles adhésions ; paiement direct intégral au salarié selon L. 1233-67, quinze jours hypothétiques pour le contrat nouveau ou préavis antérieur pour l'ancien, charges sociales propres conservées.",
                   'financing', "Employeurs et salariés concernés par une nouvelle adhésion CSP ; financeurs du dispositif privés de cette recette.",
                   "Adhésions à compter de l'entrée en vigueur uniquement ; créances, majoration et recours des adhésions anciennes conservés.",
                   "Paiement direct remplaçant la destination du préavis ; aucun nouvel impôt ; besoin de financement CSP non résolu et non chiffré.",
                   "L'employeur contribue au financement du contrat de sécurisation professionnelle par un versement représentatif de l'indemnité compensatrice de préavis, dans la limite de trois mois de salaire majoré de l'ensemble des cotisations et contributions obligatoires afférentes.",
                   "le versement patronal représentatif de l'indemnité compensatrice de préavis destiné au financement du dispositif est supprimé.")]),
    removed=["Versement patronal représentatif du préavis, majoré des cotisations et contributions obligatoires, aux financeurs du CSP pour les adhésions nouvelles.",
             "Calcul, exigibilité et recouvrement de ce versement de financement pour les seules nouvelles adhésions ; les dettes nées des anciennes adhésions sont conservées."],
    benefit="La suppression de la recette CSP ne ferme ni l'accès futur au dispositif ni allocations, aides, formations et droits sociaux éligibles. Les financements facultatifs de l'État, de l'assurance chômage et des régions restent ouverts dans leurs champs. Les droits du salarié de L. 1233-67, dont l'équivalent intégral du préavis, sont expressément réservés ; créances et restitutions anciennes demeurent. La participation distincte des opérateurs de compétences n'est pas supprimée par un renvoi incertain.")

add('L1235-3', None,
    "Maintien intégral nécessaire après lecture des cinq alinéas, des deux tableaux, de la note historique et du brouillon entier. Les dommages réparent un licenciement sans cause réelle et sérieuse, non une rupture licite ordinaire. Les minimums et la réintégration garantissent le recours ; les maximums et les minimums dérogatoires des entreprises de moins de onze salariés limitent la charge patronale. Aucune de ces protections réciproques n'est retirée. Aucun dépôt ou prélèvement accessoire n'existe ici. La reformulation antérieure et la réinsertion stylistique de la note ne sont pas comptées comme une réduction.",
    "Conservation des deux tableaux entiers depuis la source : 31 lignes de 0 à 30 ans et au-delà, puis 11 lignes de 0 à 10 ans ; années complètes, salaire brut, Sans objet, demi-mois, maximum de vingt mois, entreprises employant habituellement moins de onze salariés. Ne pas déplacer l'alinéa de dérogation visant l'alinéa précédent. Exclusion de l'indemnité légale de L. 1234-9 de la prise en compte judiciaire maintenue ; cumul avec L. 1235-12, L. 1235-13 et L. 1235-15 dans la limite des maximums du présent article. Les deux premiers ont été lus dans le corpus, le troisième dans reference-targets.json. Le plafond ordinaire de six mois et le seuil d'un an ne régissent pas cette réparation ; la ligne zéro reste applicable. L. 1235-3-1 garde l'exclusion du barème pour les nullités, avec minimum des six derniers mois sans ce plafond. La note source de l'article 40-I de l'ordonnance n° 2017-1387 est conservée comme donnée d'applicabilité historique : licenciements postérieurs à la publication de l'ordonnance, sans date de réforme future inventée.",
    impact('retained_necessary',
           "La source officielle entière, ses deux tableaux et sa portée temporelle sont maintenus sans réduction : réparation nécessaire d'une illégalité avec limites protectrices de l'employeur, distincte de l'indemnité ordinaire.",
           "Les effets contentieux et le coût des dommages ne sont pas chiffrés ; le maintien ne constitue pas un audit de conventionnalité du barème ni une baisse du coût d'un licenciement licite.",
           "Aucune charge nouvelle n'est identifiée : tableaux, cumuls et limites existants restent applicables sans registre, document, délai ni condition supplémentaire."),
    benefit="La réintégration avec avantages acquis, les minimums de réparation et l'exclusion de l'indemnité légale de la prise en compte sont conservés pour les licenciements futurs. Les maximums, le cumul plafonné et les minimums spécifiques des petites entreprises restent également entiers. Le barème n'est ni supprimé ni soumis au zéro de première année ou au plafond de six mois de l'indemnité ordinaire.")

add('L1235-3-1', None,
    "Maintien intégral nécessaire après lecture des trois alinéas, des six cas, de la note et du brouillon. L'exclusion du barème, la poursuite du contrat, le minimum réparateur et les salaires dus protègent libertés, non-discrimination, santé, maternité et représentation. Leur retrait supprimerait précisément les protections essentielles réservées par l'auteur. Aucun agrément, double justificatif ou prélèvement accessoire n'est contenu dans cet article. La reformulation antérieure n'est pas comptée comme simplification.",
    "Les 1° à 6° restent au deuxième alinéa, pour le renvoi interne et celui de L. 1235-3-2 lu intégralement. Minimum : salaires des six derniers mois, sans plafond de réparation ni ancienneté d'un an. Les neuf articles visés aux 2° à 6° ont été lus, L. 2412-1 dans le paquet de références et les autres dans le corpus public ; leurs champs ne sont pas élargis. L. 2412-1 protège encore les anciens CDD, sans en autoriser de nouveaux ; les futurs contrats uniques protégés relèvent du chapitre Ier et de L. 2411-1. Le rappel de salaire ne devient pas universel et reste soumis aux fondements visés. Discordance préexistante conservée et signalée : le dernier alinéa mentionne un salaire dû en application de L. 1225-71, tandis que ce dernier renvoie, dans sa source fournie, à l'indemnité de L. 1235-3-1. Cette circularité appelle vérification du fondement des rappels, sans extinction déduite du droit ni correction silencieuse. La note de l'article 40-I de l'ordonnance n° 2017-1387 demeure applicable aux licenciements postérieurs à sa publication ; elle n'est pas une transition de la réforme future. Les indemnités spéciales, légales, conventionnelles et contractuelles conservent leurs conditions propres.",
    impact('retained_necessary',
           "La source entière est maintenue, avec six catégories de nullité et minimum des six derniers mois. Il s'agit de la réparation d'atteintes essentielles, non d'un coût de rupture ordinaire que la réforme permettrait d'effacer.",
           "Le renvoi circulaire de L. 1225-71 reste signalé ; l'article ne démontre ni le montant individuel d'un rappel de salaire ni une réduction nette de complexité dans les autres codes.",
           "Aucune charge nouvelle n'est identifiée : toutes les conditions, indemnités et références restent celles de la source, sans nouvelle donnée, autorisation, déclaration ou délai."),
    benefit="Sont conservés pour toutes les situations futures recevables : poursuite du contrat ou réintégration selon leurs règles, exclusion du barème, indemnité minimale des six derniers mois, salaires dus au titre des fondements protecteurs et indemnités légale, conventionnelle ou contractuelle éventuelles. Les six cas de nullité restent entiers, y compris les protections des anciens CDD ; aucun avantage ne dépend du seuil d'un an ou du plafond ordinaire de six mois.")

# Analyses des cibles : la vue fournie est toujours identifiée comme proposition,
# sans lui attribuer l'autorité du texte officiel lu en parallèle.
contexts = {
    'L1231-4': (
        "L'interdiction de renonciation anticipée protège le préavis applicable : elle ne modifie ni les quinze jours des contrats nouveaux ni les durées anciennes, ni les autorisations distinctes.",
        "L'interdiction subsiste pour le futur contrat à durée indéterminée ; elle ne transforme ni une formation ni une mission en terme automatique et ne recrée aucun CDD.",
        "L'interdiction de renoncer d'avance s'étend aux indemnités réellement dues, sans créer d'indemnité ordinaire avant le seuil ou en démission et sans permettre de renoncer aux réparations dès le premier jour."),
    'L1231-5': (
        "Le service dans la filiale étrangère compte pour les préavis anciens variables avec l'ancienneté ; il ne transforme pas les quinze jours fixes des nouveaux contrats en durée croissante. Le rapatriement est distinct.",
        "La mise à disposition dans une filiale étrangère n'est pas un cas autonome de nouveau CDD français. La loi du contrat étranger n'est toutefois pas désignée par L. 1221-2 ni par cet article.",
        "Le temps de filiale reste reconnu pour atteindre le seuil à la fin effective et pour calculer toute l'ancienneté, sans retirer la première année. Les périodes étrangères doivent être affectées sans double compte aux composantes anciennes et nouvelles."),
    'L1232-1': (
        "Le motif personnel doit rester réel, sérieux et motivé, même si le préavis est de quinze jours. L'audition, les délais collectifs et les autorisations protectrices ne sont pas remplacés par ce préavis.",
        "La justification patronale reste exigée pour le contrat unique nouveau. L'interdiction des CDD nouveaux ne crée pas une rupture automatique à la fin d'une tâche ; les anciens contrats gardent leur transition.",
        "L'existence d'un motif contrôlable ne dépend pas de l'ouverture de l'indemnité ordinaire. Le zéro avant un an et le plafond de six mois n'effacent donc aucune réparation d'un motif illégal."),
    'L1232-2': (
        "Les cinq jours ouvrables retirés sont un temps de procédure avant décision, distinct du préavis de quinze jours après notification. Le temps de défense et les autorisations restent nécessaires ; anciens préavis conservés.",
        "La transition choisie concerne la date de convocation, y compris d'un ancien CDI ; elle ne convertit pas rétroactivement l'emploi en contrat unique et n'autorise aucun CDD nouveau.",
        "La préparation de l'entretien n'est ni une franchise d'ancienneté ni la date d'ouverture de l'indemnité. Celle-ci reste appréciée à la fin effective avec préavis inclus lorsque dû, sans perte de première année après le seuil."),
    'L1232-3': (
        "L'exposé des motifs et le recueil des explications interviennent avant décision, non pendant un préavis réputé suffisant. Les quinze jours ne dispensent pas de cette défense ni des protections spéciales.",
        "L'audition demeure applicable à la rupture patronale du contrat unique ; aucune fin de mission ou formation ne dispense du motif contrôlable et des règles de rupture. Les anciens CDD ne deviennent pas nouveaux.",
        "L'audition protège le salarié dès la première année, alors même qu'aucune indemnité ordinaire ne serait due. Les dommages d'une illégalité ne relèvent ni du seuil d'un an ni du plafond ordinaire."),
    'L1232-4': (
        "Le droit d'assistance ne disparaît pas du fait du préavis individuel fixe ; il s'exerce avant décision avec le temps effectif prévu à L. 1232-2. Les autorisations et procédures spéciales restent distinctes.",
        "La faculté d'assistance reste ouverte aux futurs contrats uniques. Son accès ne dépend d'aucun ancien statut de CDD et la durée de l'accompagnement ne peut limiter l'emploi nouveau.",
        "L'assistance n'est pas subordonnée au seuil d'un an de l'indemnité ordinaire ; elle vaut dès le début de l'emploi, avec maintien des réparations d'illégalité et des indemnités spéciales."),
    'L1232-5': (
        "L'habilitation de la section d'entretien ne régit pas la durée du préavis de rupture. La limitation du décret ne supprime ni les quinze jours nouveaux ni les préavis anciens ou procédures spéciales.",
        "Le décret de l'entretien ne peut servir de fondement à un nouveau contrat à terme ; la durée indéterminée des emplois nouveaux et les anciens contrats demeurent régis par leurs textes propres.",
        "L'habilitation d'entretien n'autorise aucun changement du seuil d'un an, du prorata ou du plafond indemnitaire ; elle ne peut conditionner l'assistance au droit de toucher l'indemnité ordinaire."),
    'L1232-6': (
        "Le libre choix d'un écrit de notification ne change pas la durée applicable : quinze jours pour les contrats nouveaux, règles antérieures pour les anciens. Il ne dispense d'aucune autorisation ou procédure collective.",
        "La notification écrite met fin selon ses règles au contrat unique ; elle ne permet aucun terme automatique de mission ni CDD nouveau. La transition de procédure par convocation ne transforme pas l'ancien contrat.",
        "La date de notification n'est pas substituée à la fin effective pour le seuil d'un an. Le préavis entre dans l'ancienneté de droit commun ; le salaire de référence et les réparations d'illégalité ont leurs règles distinctes."),
    'L1233-67': (
        "Le CSP est la rupture volontaire spéciale sans préavis exécuté. Les quinze jours nouveaux servent au montant hypothétique versé ; les anciens contrats conservent leur préavis antérieur, sans durée nouvelle d'emploi créée par le CSP.",
        "Le renvoi au travail pendant le CSP ne doit pas rétablir les CDD : les emplois nouveaux sont indéterminés ; la durée du parcours ou de la formation ne met pas fin à l'emploi. Les avantages futurs suivent les situations éligibles.",
        "Le renvoi à l'indemnité légale garde ses conditions propres : rupture effective à l'adhésion sans emploi fictif d'accompagnement ; le préavis hypothétique mentionné pour l'indemnité conventionnelle et le versement ne devient pas préavis exécuté. Les garanties conventionnelles plus favorables restent à contrôler."),
    'L1233-69': (
        "La suppression du versement de financement n'abolit pas le préavis ordinaire. L'équivalent dû directement au salarié selon L. 1233-67 dépend de quinze jours pour le contrat nouveau ou de la durée antérieure pour l'ancien.",
        "L'article finance un accompagnement et non un contrat d'emploi temporaire ; sa durée ne rétablit donc aucun CDD nouveau. La suppression de recette ne ferme pas les aides des futurs emplois éligibles.",
        "Le versement supprimé est représentatif du préavis, non l'indemnité ordinaire de L. 1234-9. Le seuil d'un an, le taux et le plafond de cette dernière ne conditionnent ni les allocations du CSP ni le versement direct en lieu de préavis."),
    'L1235-3': (
        "Le préavis ordinaire de quinze jours ne définit ni l'illégalité du motif ni les dommages du barème. Les anciens préavis restent protégés, et les consultations collectives ou autorisations conservent leur fonction.",
        "Le barème demeure applicable dans son champ au contrat unique sans recréer un CDD. Les anciens contrats et litiges relatifs à leur terme ne sont pas rétroactivement assimilés à un licenciement relevant de ce seul article.",
        "L'article exclut expressément cette indemnité légale de la prise en compte par le juge. Ses propres tableaux gardent la ligne zéro, les années complètes et leurs maximums, sans seuil d'un an ni plafond général de six mois importé de la cible."),
    'L1235-3-1': (
        "Le préavis de quinze jours ne purge aucune nullité : motif discriminatoire, statut protecteur et autorisations restent distincts. Le minimum des six derniers mois n'est ni un préavis ni son plafond.",
        "Les futurs salariés du contrat unique conservent leurs protections essentielles ; le renvoi à L. 2412-1 reste utile pour les anciens CDD, sans autoriser de nouvelle embauche à durée déterminée.",
        "L'indemnité légale éventuelle conserve son seuil et ses exceptions, mais ils ne régissent pas la réparation de nullité. Le minimum des six derniers mois reste dû dans les conditions de l'article sans ancienneté d'un an ni plafond de six mois."),
}

common_numbers = ['L1234-1', 'L1221-2', 'L1234-9']
common_explanations = {
    'L1234-1': "La source officielle de L. 1234-1 prévoit des durées variables et l'exception de faute grave ; la vue proposée réserve ces règles aux anciens contrats et fixe quinze jours calendaires aux nouveaux, y compris payés en cas de faute grave. ",
    'L1221-2': "La source officielle de L. 1221-2 admet encore les termes du titre IV ; sa proposition supprime ces nouvelles embauches et renouvellements à terme, en préservant contrats et droits antérieurs. Elle ne concerne pas implicitement les agents publics. ",
    'L1234-9': "La source officielle de L. 1234-9 ouvre le droit à huit mois hors faute grave ; la proposition prévoit pour les nouveaux contrats un an à la fin effective, préavis inclus lorsqu'il existe, puis 0,20 mois sur l'ancienneté totale, fractions en mois complets, plafond légal de six mois et initiative patronale, hors faute grave selon sa rédaction. Anciennes composantes, indemnités plus favorables et réparations restent distinctes. ",
}

extra_checks = {
    ('L1232-2', 'L1232-4'): "La source de L. 1232-4 maintient le choix d'un membre du personnel et, sans représentants, d'un conseiller officiel. La proposition de cible rend les adresses dispensables sous accès effectif à la liste ; elle ne supprime pas l'assistance. Le nouvel entretien sans cinq jours forfaitaires doit laisser le temps d'organiser ce choix et être reporté si nécessaire ; la date de convocation règle la transition des deux articles.",
    ('L1232-5', 'L1232-2'): "La vue proposée de L. 1232-2, distincte de la source qui impose deux supports et cinq jours ouvrables, ouvre les écrits prouvables et remplace l'attente fixe par la préparation effective et le report nécessaire. La limitation réglementaire porte exactement sur ces moyens et ce minimum ; elle ne supprime pas l'entretien ni l'ancien régime des convocations antérieures.",
    ('L1232-5', 'L1232-4'): "La proposition fournie dispense d'adresses seulement si la liste officielle ou son accès gratuit effectif sont donnés, avec accès de secours ; la source imposait les adresses. L'habilitation limitée doit laisser cette faculté opérante sans modifier la liste publique, les conditions d'absence de représentants ou les droits d'assistance ; la transition suit les nouvelles convocations.",
    ('L1232-6', 'L1232-2'): "La proposition de convocation supprime les cinq jours fixes mais impose le temps réel de défense et les reports nécessaires. La notification ne peut les court-circuiter, même en cas d'absence : date et heure de l'entretien, reports inclus, doivent être passées. Cette transition par convocation est distincte de la transition par date du contrat pour le préavis.",
    ('L1232-6', 'L1232-3'): "Source et proposition de cible imposent d'exposer les motifs envisagés et de recueillir les explications. La notification après examen n'ajoute pas de rapport ni de procès-verbal : elle garantit que la décision suit réellement l'audition. Le maintien final de la source de L. 1232-3 ne change pas cette analyse de la vue stylistique fournie.",
    ('L1232-6', 'L1232-4'): "L'assistance de la source est maintenue dans la proposition avec une alternative d'accès à la liste des conseillers. La notification sans attente de deux jours ne peut précéder l'organisation effective de cette assistance et les reports nécessaires, ni transformer l'accès extérieur en faculté ouverte dans toute entreprise sans sa condition de représentation.",
    ('L1232-6', 'L1234-3'): "La source fixe le départ à la présentation du recommandé ; la proposition compte les quinze jours nouveaux à partir du lendemain de présentation ou, si autre forme légale, de réception/remise, jusqu'à la fin du quinzième jour même non travaillé. L'alinéa 1 de L. 1232-6 opère cette substitution pour l'écrit alternatif. Les anciens contrats gardent leur durée et leur règle de départ ; la nouvelle réception remplace seulement la présentation devenue sans objet. La notification salariale est distincte.",
    ('L1233-67', 'L1233-68'): "Lecture de la source et de la proposition entières : le 3° source autorise CDD et contrats temporaires, tandis que sa proposition coordonne déjà les emplois nouveaux au contrat unique. Le 10° b proposé réserve déjà le financement patronal aux adhésions antérieures et interdit sa reconstitution ; aucune lacune actuelle de ce b n'est donc affirmée. Les conditions d'ancienneté propres au CSP, l'accord agréé, les réponses du salarié et les droits d'allocation restent distincts du seuil indemnitaire de L. 1234-9.",
    ('L1233-67', 'L1233-69'): "La source de L. 1233-69 institue le versement plafonné à trois mois majoré des contributions ; sa proposition le supprime pour les adhésions nouvelles et conserve les créances antérieures. L. 1233-67 réserve donc la défalcation aux anciennes adhésions et verse l'équivalent intégral au salarié pour les nouvelles. Ce changement de destinataire n'est pas une économie patronale démontrée ; cotisations sur les sommes salariales et contribution pour défaut de proposition restent distinctes.",
    ('L1233-69', 'L1233-67'): "La source ne verse au salarié qu'un solde éventuel après défalcation du financement ; la proposition attribue aux nouvelles adhésions la totalité de l'indemnité hypothétique. Cette charge directe est le remplacement à déduire de toute économie alléguée au titre de L. 1233-69. Le CSP rompt sans préavis exécuté ; quinze jours servent au montant des nouveaux contrats et les anciens gardent leur durée. Le seuil d'un an de l'indemnité ordinaire ne ferme pas ce versement.",
    ('L1233-69', 'L1233-68'): "Le 10° b de la source autorise le financement patronal plafonné ; la proposition fournie le limite déjà aux seules adhésions antérieures et interdit son retour par accord ou décret. L. 1233-69 conserve exactement cette transition et les autres financeurs ; les 1°, 2° et 8° continuent de régir l'accès et les allocations. Le 3° concerne les périodes de travail, pas une durée déterminée de l'emploi nouveau. Le renvoi ne permet ni nouveau prélèvement ni suppression d'aide future.",
    ('L1235-3', 'L1235-15'): "La source de L. 1235-15 et sa proposition réparent l'absence de CSE obligatoire sans procès-verbal de carence, par au moins un mois de salaire brut, sans préjudice du préavis et du licenciement. Le dernier alinéa de L. 1235-3 conserve le cumul dans ses maximums ; ni le seuil d'un an ni le plafond ordinaire de six mois ne sont importés dans cette sanction de l'irrégularité collective.",
    ('L1235-3-1', 'L2412-1'): "La source énumère les mandats protégés pour les CDD ; la proposition entière maintient ce chapitre pour les seuls contrats à terme antérieurs et leurs contrôles, même en cas de non-renouvellement. Elle ne permet aucun nouveau CDD ni renouvellement ; les futurs contrats uniques relèvent du chapitre Ier pour leurs mandats et périodes propres. Le renvoi du 5° demeure donc utile et ne doit pas être supprimé comme devenu sans objet ; le préavis de quinze jours ne remplace pas l'autorisation.",
    ('L1235-3-1', 'L1235-3'): "Les deux tableaux complets de la source de L. 1235-3 et de sa proposition concernent l'absence de cause réelle et sérieuse ; ils sont exclus pour les nullités des 1° à 6° du deuxième alinéa de L. 1235-3-1. Les six derniers mois sont ici un minimum sans plafond, non le plafond ordinaire du contrat unique. Le maintien final de L. 1235-3 depuis sa source ne modifie ni cette exclusion ni l'applicabilité historique de 2017.",
}

for row in answer:
    key = row['code_id'] + '|' + row['source_id']
    checks = []
    for target_key in refs['requirements'][key]:
        target = refs['targets'][target_key]
        tn = target['number']
        if tn in common_numbers:
            assessment = common_explanations[tn] + contexts[row['number']][common_numbers.index(tn)]
        else:
            assessment = extra_checks[(row['number'], tn)]
        checks.append(dict(target_key=target_key, view_sha256=target['view_sha256'], assessment=assessment))
    row['reference_checks'] = checks

Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles ; {sum(len(a["reference_checks"]) for a in answer)} analyses de cibles')
