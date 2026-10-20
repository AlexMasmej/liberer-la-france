import json
import re
from html import unescape
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
by_number = {s['number']: s for s in sources}
target_by_number = {v['number']: (k, v) for k, v in refs['targets'].items()}


def plain(xml):
    return re.sub(r'\s+', ' ', unescape(re.sub(r'<[^>]*>', ' ', xml))).strip()


def impact(classification, assessment, limitations, burdens, effects=None):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=limitations, new_burdens_review=burdens,
                effects=effects or [])


def effect(kind, measure, description, before, after, unit, population, transition,
           burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure, description=description,
                before=before, after=after, unit=unit,
                affected_population=population, conditions_and_transition=transition,
                replacement_or_new_burdens=burdens, source_quote=source_quote,
                proposed_quote=proposed_quote)


answers = []
for s in sources:
    a = {k: s[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}
    a.update({k: s['previous_draft'][k] for k in ['proposed_xml', 'reason', 'review_notes']})
    a['status'] = 'rewrite_draft'
    answers.append(a)
A = {a['number']: a for a in answers}

# Suppression effective, déjà acquise dans le brouillon, du délai de prévenance.
a = A['L1225-66']
a.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19',
         removed_provisions=["Le délai minimal de quinze jours d'information de l'employeur avant la rupture pour élever un enfant est supprimé."])
a['reason'] = "Réforme de fond maintenue après comparaison avec la source entière : le salarié n'a plus à prévenir quinze jours avant une rupture déjà dispensée de préavis et d'indemnité à sa charge. L'information peut intervenir par tout moyen jusqu'à la rupture. Les dates d'exercice, le motif parental et les deux dispenses demeurent. Aucune autre coupe n'est retenue : l'information permet de constater la cessation de l'emploi ; le rattachement à la naissance, à l'adoption ou à la fin du congé délimite cette dispense particulière. Le brouillon est conservé, sans présenter sa conservation comme une coupe supplémentaire."
a['review_notes'] += " Le choix légal de tout moyen doit primer la forme exclusive du premier alinéa de R. 1225-18 ; ce règlement, non assigné et absent des cibles fournies, a été lu dans travail.json mais n'est pas modifié ici. Le nouveau texte ne conditionne pas la dispense à la preuve d'un envoi recommandé. Les droits de réembauche de L. 1225-67, également lus hors du fichier des cibles, subsistent pour les départs futurs."
a['substantive_impact'] = impact(
    'material_reduction',
    "Par rapport à la source officielle entière, le délai minimal de prévenance de quinze jours disparaît et aucun délai équivalent ne le remplace. Les dispenses de préavis et d'indemnité de rupture sont conservées. Le brouillon comportait déjà cette suppression ; cette passe n'ajoute pas une seconde réduction.",
    "Le droit demeure exercé pour élever l'enfant aux dates légales conservées. La coordination de R. 1225-18 reste à effectuer hors de ce lot. Aucun coût national ni effet sur l'emploi n'est chiffré.",
    "Aucune charge nouvelle n'est identifiée : l'information existante de l'employeur subsiste, sans formulaire, justificatif, recommandé obligatoire ni délai minimal de remplacement.",
    [effect('deadline_reduced', 'depart-parental-sans-prevenance',
            "Suppression de la prévenance minimale pour le départ parental.",
            "Information de l'employeur au moins quinze jours avant la rupture pour élever un enfant.",
            "Information par tout moyen au plus tard le jour de la rupture ; aucun minimum de prévenance.",
            'calendar_days', "Salariés usant de la rupture pour élever leur enfant aux dates prévues par L1225-66.",
            "Ruptures prenant effet à compter de l'entrée en vigueur, y compris pour les contrats antérieurs ; ruptures déjà effectives sous leur ancien régime.",
            "Information maintenue sans formalité de substitution ; R1225-18 à coordonner.",
            "sous réserve d'en informer son employeur au moins quinze jours à l'avance",
            "Il en informe l’employeur par tout moyen, au plus tard à la date de la rupture, sans délai minimal de prévenance.")])

# L'inaptitude non professionnelle garde ses trois alinéas et ses deux régimes temporels.
a = A['L1226-4']
a['proposed_xml'] = a['proposed_xml'].replace(
    "Dans les deux cas, par dérogation à l’article L. 1234-5, l’inexécution du préavis ne donne pas lieu à une indemnité compensatrice.",
    "Dans les deux cas, par dérogation à l’article L. 1234-5, l’inexécution du préavis ne donne pas lieu à une indemnité compensatrice. Les conditions de l’indemnité ordinaire ne limitent pas l’indemnité spéciale prévue à l’article L. 1226-4-3, qui demeure due sans condition minimale d’ancienneté dans son champ propre.")
a['reason'] = "Coordination de fond avec le préavis du contrat unique, et non simple allègement : pour les nouveaux contrats, la rupture immédiate de la source est remplacée par une fin au quinzième jour calculé selon L. 1234-3. Le mois précédant la reprise du salaire, son montant et le constat d'inaptitude à tout emploi restent nécessaires à la protection du salarié et à la recherche de reclassement. La dispense d'exécution et l'absence de compensation propre à cette inaptitude sont préservées. La présente passe ajoute la réserve expresse de l'indemnité spéciale de L. 1226-4-3 proposée, pour éviter que le seuil ordinaire d'un an la ferme. Aucune nouvelle coupe de ces protections n'est justifiée."
a['review_notes'] += " Le maintien du contrat pendant quinze jours est un allongement par rapport à la fin à notification de la source, non une suppression de délai. La dérogation à l'indemnité compensatrice ne dispense pas du salaire dû sur un autre fondement, notamment de sa reprise après le mois légal lorsque ses conditions restent remplies. Le nouveau renvoi exprès à L. 1226-4-3 est fourni dans reference-targets.json : sa proposition étend une garantie spéciale sans seuil aux nouveaux contrats uniques, ce qui n'est pas le champ de sa source CDD. Aucun préavis CDI n'est attribué automatiquement aux anciens CDD : L. 1226-4-2 et L. 1226-4-3 conservent leurs règles propres."
a['benefit_review'] = "Sont conservés la reprise du salaire de l'emploi antérieur après un mois sans reclassement ni licenciement, y compris en cas d'inaptitude à tout emploi, la dispense d'exécution du préavis et sa prise en compte pour l'indemnité. L'absence d'indemnité compensatrice, favorable à l'employeur dans ce cas précis, n'est pas supprimée. Les quinze jours des nouveaux contrats comptent au seuil ordinaire mesuré au terme effectif puis sur l'ancienneté totale. La garantie spéciale sans seuil de L. 1226-4-3 proposée reste distincte, pour les situations futures aussi ; les anciens contrats gardent leur régime. Aucun de ces avantages n'est réservé aux seules inaptitudes déjà constatées."
a['substantive_impact'] = impact(
    'mixed',
    "La source prévoit une fin du contrat à notification ; la proposition maintient les nouveaux contrats quinze jours supplémentaires, sans indemnité compensatrice créée par ce seul article. Elle coordonne aussi le barème ordinaire réduit décidé dans L1234-9 et réserve la garantie spéciale sans seuil. Ce mélange de coordination et d'allongement ne démontre aucune économie nette propre à L1226-4.",
    "La reprise du salaire après un mois demeure ; les charges pendant le maintien du contrat dépendent des droits effectivement ouverts. Anciens contrats et anciens CDD gardent leurs règles spécifiques. Le solde de coût, la conventionalité et les effets de la réforme générale ne sont pas établis par ce lot.",
    "Une charge de calendrier est identifiée : maintien du contrat nouveau quinze jours après notification au lieu de sa fin immédiate, avec les droits légaux qui s'y attachent. La coexistence transitoire de deux régimes ajoute un suivi selon la date du contrat, sur données existantes ; aucun formulaire, registre ni justificatif nouveau n'est ajouté.",
    [effect('deadline_increased', 'contrat-unique-preavis-quinze-jours',
            "Fin différée du nouveau contrat dans le cas spécial d'inaptitude non professionnelle.",
            "Fin à la notification : aucun délai supplémentaire de maintien du contrat prévu par cet article.",
            "Fin à l'expiration de quinze jours calendaires comptés à partir du lendemain de la présentation ou réception légalement admise.",
            'calendar_days', "Employeurs et salariés sous contrat unique nouveau licenciés pour inaptitude non professionnelle.",
            "Nouveaux contrats seulement ; anciens contrats terminés à notification avec leur prise en compte particulière du préavis.",
            "Pas de compensation du seul préavis inexécuté ; autres salaires et droits éventuellement dus restent applicables.",
            "le contrat de travail est rompu à la date de notification du licenciement",
            "Le contrat prend fin à l’expiration du quinzième jour, même non travaillé."),
     effect('coordination', 'contrat-unique-indemnite-ordinaire',
            "Articulation de l'ancienneté de fin de contrat avec le seuil ordinaire, sans plafonner l'indemnité spéciale.",
            "Préavis pris en compte pour l'indemnité de L1234-9 ; source générale de cette cible ouverte à huit mois, sauf faute grave.",
            "Pour les nouveaux contrats : seuil ordinaire d'un an au terme effectif, puis ancienneté totale ; garantie spéciale sans ce seuil selon L1226-4-3 proposé.",
            'other', "Salariés licenciés pour inaptitude non professionnelle dans chaque régime temporel.",
            "Le barème, les fractions en mois complets et la transition des services antérieurs relèvent de L1234-9 et de ses règlements ; pas de déduction de la première année.",
            "Pas de seconde indemnité ordinaire ni de formalité de remplacement créée par ce renvoi.",
            "Le préavis est néanmoins pris en compte pour le calcul de l'indemnité mentionnée à l'article L. 1234-9.",
            "Les conditions de l’indemnité ordinaire ne limitent pas l’indemnité spéciale prévue à l’article L. 1226-4-3, qui demeure due sans condition minimale d’ancienneté dans son champ propre.")])

# Pas de fausse coupe ni de réécriture stylistique du dispositif facultatif de mutualisation.
a = A['L1226-4-1']
a.update(status='retained_unchanged', proposed_xml=None)
a['reason'] = "Maintien intégral de la source nécessaire après examen du brouillon entier. L'article organise le paiement d'indemnités effectivement dues, par l'employeur ou par les seules garanties souscrites ; il n'impose ni adhésion ni cotisation spéciale. La mutualisation constitue une faculté favorable et la désignation du gestionnaire assure sa continuité. Les supprimer ne retirerait pas une charge obligatoire démontrée et pourrait désorganiser le paiement. Les ajouts explicatifs du brouillon ne justifient pas une réécriture normative."
a['review_notes'] = "L. 1226-2-1 et L. 3253-14 ont été lus intégralement dans le corpus public autorisé, hors des cibles fournies : conditions du licenciement pour inaptitude non professionnelle et association gestionnaire, avec sa note historique. Leur régime n'est pas réécrit ici. La gestion du fonds ne rend pas l'AGS débitrice automatique de toutes les indemnités. Les garanties souscrites, anciennes ou futures, restent limitées à leur objet ; les sommes dues et non couvertes restent à la charge de l'employeur. Aucun renvoi vers l'ancien barème n'est figé : les indemnités sont celles légalement dues, y compris les indemnités spéciales sans seuil lorsque leur texte le prévoit. Aucun renvoi à l'annualité fiscale, au CDD futur ou à un régime public n'est créé."
a['substantive_impact'] = impact(
    'retained_necessary',
    "La source entière est maintenue : alternative entre paiement direct et garantie souscrite, avec gestionnaire légal du fonds. Aucune obligation autonome de cotiser ou d'adhérer n'y a été trouvée ; supprimer la faculté de garantie ne serait pas une baisse démontrée de prélèvement.",
    "Aucun examen de solvabilité ni chiffrage des garanties n'est effectué ; les cotisations AGS régies par d'autres articles ne sont pas supprimées. Les montants de rupture et leur transition restent déterminés par leurs propres règles.",
    "Aucune charge nouvelle n'est identifiée : reproduction intégrale de la source, sans les précisions supplémentaires du brouillon et sans nouvelle inscription, donnée ou échéance.")

a = A['L1226-4-2']
a['reason'] = "Coordination prospective nécessaire avec la fin des nouveaux CDD : le renvoi à L. 1226-4 survit pour les contrats déjà conclus et leurs inaptitudes futures. Les contrats uniques relèvent directement du régime commun, avec les garanties spéciales maintenues dans leur champ. Aucune protection ni obligation autonome n'est retirée de cet article : supprimer le renvoi priverait les anciens CDD de la reprise du salaire. Le brouillon est conservé ; sa transition ne constitue pas une deuxième abolition du CDD."
a['review_notes'] += " Le renvoi source global à un article de licenciement, malgré le régime de rupture propre au CDD, est une difficulté préexistante : il ne suffit pas à rendre applicable à l'ancien CDD le préavis CDI. La proposition cible de L. 1226-4-3 prévoit aussi une garantie spéciale future dans le contrat unique sans seuil d'un an ; la phrase d'application directe de L. 1226-4 ne l'écarte pas."
a['substantive_impact'] = impact(
    'coordination_only',
    "La source étend L1226-4 aux CDD sans limite de date. La proposition réserve ce support aux contrats antérieurs, garde la reprise du salaire et les indemnités spéciales, et renvoie les nouvelles embauches au contrat unique. Aucune charge ni taxe supplémentaire n'est supprimée par cet article de coordination.",
    "La suppression du régime CDD repose sur L1221-2 et L1241-1 proposés ; sa réduction globale n'est pas comptée ici. Les règles de rupture des anciens CDD restent distinctes du licenciement et les recours peuvent naître après la réforme.",
    "Aucune charge nouvelle n'est identifiée dans cet article : pas de conversion forcée, formulaire, autorisation ou justification à joindre. La conversion éventuelle préserve ancienneté et créances sans double compte.",
    [effect('coordination', 'contrat-unique-suppression-cdd',
            "Cantonnement du support CDD aux contrats antérieurs, sans extinction de leur protection d'inaptitude.",
            "Application générale de L1226-4 aux salariés en CDD.",
            "Application maintenue aux anciens CDD et application directe de L1226-4 aux contrats uniques nouveaux, avec règles spéciales réservées.",
            'regime', "Salariés atteints d'inaptitude non professionnelle sous ancien CDD ou nouveau contrat unique.",
            "Contrats conclus avant l'entrée en vigueur, même si l'inaptitude est postérieure ; aucun nouveau renouvellement CDD.",
            "Aucun dossier ni acte de conversion obligatoire ; mission, aide ou formation sans terme d'emploi.",
            "Les dispositions visées à l'article L. 1226-4 s'appliquent également aux salariés en contrat de travail à durée déterminée.",
            "Les salariés sous contrat de travail unique relèvent directement de l’article L. 1226-4.")])

a = A['L1226-14']
a['proposed_xml'] = a['proposed_xml'].replace(
    "fractions d’année au prorata, sans retrancher la première année",
    "fractions d’année au prorata des mois complets, sans retrancher la première année")
a.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19',
         removed_provisions=["Pour les nouveaux contrats et les seuls services postérieurs des anciens contrats, l'application au minimum spécial doublé des taux de base de 1/4 puis 1/3 de mois est remplacée par le barème de 0,20 mois avant doublement, avec plafond de la seule composante nouvelle ; droits antérieurs et conventions plus favorables préservés."])
a['reason'] = "Coordination de fond du doublement spécial avec le barème de L. 1234-9 et du préavis avec L. 1234-3. La présente passe précise que les fractions d'année sont calculées en mois complets, conformément à la décision actuelle ; elle conserve l'absence de seuil spécial, le salaire reconstitué de L. 1226-16, la compensation, les règles de non-cumul et l'exception du refus abusif prouvé. La baisse du barème de base décidée ailleurs n'est pas comptée comme une nouvelle mesure autonome. Le maintien du contrat quinze jours et les composantes transitoires doivent aussi être appréciés comme charges de coordination ; aucune coupe supplémentaire de ces garanties de santé n'est justifiée."
a['review_notes'] += " R. 1234-1, R. 1234-2 et R. 1234-4 ont été lus dans travail.json hors des cibles : taux officiels de 1/4 de mois jusqu'à dix ans et 1/3 au-delà ; calcul en mois complets et note transitoire de 2017 ; leurs propositions ne sont pas du droit en vigueur. Le barème doublé nouveau est donc 0,40 mois par année, prorata en mois complets, et au plus douze mois pour la seule composante nouvelle après doublement, sauf convention plus favorable. Il ne faut importer ni le seuil d'un an ni l'exclusion ordinaire pour faute grave dans le minimum spécial ; l'exception expresse de refus abusif reste à son propre champ. L. 1226-12 et L. 1226-16, non fournis comme cibles, ont été lus en entier : les 1° à 3° existent dans la proposition de L. 1226-12, pas dans sa source. Le maintien à quinze jours est un choix du projet, sans conclusion sur un coût net ni sur une conformité internationale acquise."
a['substantive_impact'] = impact(
    'mixed',
    "Le doublement spécial et ses exceptions sont conservés. Le renvoi au barème réduit transforme la composante nouvelle en 0,40 mois par année au plus douze mois après doublement, sans seuil d'un an ; les droits de services antérieurs subsistent. Le projet ajoute aussi le maintien du nouveau contrat pendant quinze jours. Ces effets sont des coordinations des mesures communes ; aucune seconde économie ni solde net propre n'est établi.",
    "Les conventions plus favorables, les composantes antérieures, le salaire spécial reconstitué et les réparations demeurent hors de la baisse revendiquée. L'ancien droit de préavis n'est pas remplacé pour les anciens contrats. L'impact financier dépend des anciennetés et conventions ; aucune estimation nationale n'est fournie.",
    "Le maintien de l'emploi nouveau quinze jours et la ventilation transitoire de l'ancienneté doivent être pris en compte ; ils peuvent ajouter du coût ou du suivi. Aucun registre, formulaire, agrément ni justificatif nouveau n'est imposé par cet article, et une même période de préavis n'est pas payée deux fois.",
    [effect('coordination', 'contrat-unique-indemnite-ordinaire',
            "Application du barème de base coordonné à l'indemnité spéciale, sans importer le seuil ordinaire.",
            "Double de l'indemnité légale calculée selon L1234-9 et les taux officiels réglementaires de 1/4 puis 1/3 de mois ; exception conventionnelle plus favorable.",
            "Double du barème de base de 0,20 mois par année, prorata des mois complets, plafond de la composante nouvelle doublé à douze mois ; aucun seuil spécial d'un an.",
            'other', "Salariés licenciés pour inaptitude d'origine professionnelle dans les cas légaux de L1226-12.",
            "Services antérieurs des anciens contrats à leurs taux et minima ; seule la composante nouvelle plafonnée avant doublement ; refus abusif et non-cumul historique conservés.",
            "Suivi des composantes sans déclaration nouvelle, sans double compte et avec salaire de référence spécial.",
            "sauf dispositions conventionnelles plus favorables, est égale au double de l'indemnité prévue par l'article L. 1234-9.",
            "Elle est due sans condition minimale d’ancienneté : le seuil d’un an de l’indemnité ordinaire ne lui est pas applicable."),
     effect('coordination', 'contrat-unique-preavis-quinze-jours',
            "Coordination de la compensation spéciale avec les quinze jours des nouveaux contrats.",
            "Indemnité spéciale de préavis d'un montant égal à celui prévu par L1234-5, avec durées variables selon le régime applicable.",
            "Pour les nouveaux contrats, quinze jours calendaires non exécutés, compensés une seule fois et compris dans l'ancienneté ; anciens contrats conservés.",
            'calendar_days', "Salariés sous nouveau contrat unique licenciés pour inaptitude professionnelle.",
            "Départ du délai le lendemain selon L1234-3 ; les anciens contrats conservent leur régime et la date de rupture qui en résulte.",
            "Maintien du contrat quinze jours et compensation spéciale ; pas de deuxième indemnité pour la même période.",
            "une indemnité compensatrice d'un montant égal à celui de l'indemnité compensatrice de préavis prévue à l'article L. 1234-5",
            "Ces quinze jours sont compris dans l’ancienneté servant au calcul de l’indemnité spéciale.")])

a = A['L1226-15']
a['reason'] += " Le brouillon reste complet et est conservé sans coupe nouvelle ; sa correction de renvoi est nécessaire à la proposition subdivisée de L. 1226-12, non une réduction d'indemnité."
a['review_notes'] += " L. 1226-8, L. 1226-10, L. 1226-11, L. 1226-12 et L. 1235-2 ne figurent pas parmi les cibles fournies mais leurs sources et propositions ont été lues dans travail.json. Aucune nouvelle cible non fournie n'est présumée : la règle procédurale de L. 1235-2 conserve notamment son plafond d'un mois dans son seul champ."
a['substantive_impact'] = impact(
    'coordination_only',
    "La comparaison intégrale ne montre aucune charge supprimable : réintégration proposée, avantages acquis, réparation et cumul sont maintenus. Le renvoi par objet à la procédure de L1226-12 évite un décalage d'alinéa. La transition historique et la séparation d'avec le barème ordinaire ne constituent pas des baisses de coût.",
    "Les réparations protègent l'emploi et la santé ; les retirer ne relèverait pas d'une formalité redondante. Le minimum de six mois de L1235-3-1 n'est pas un plafond. Aucune conclusion n'est tirée sur les autres motifs de nullité ou l'ensemble des contentieux du travail.",
    "Aucune charge nouvelle n'est identifiée : les obligations de réintégration et de réparation étaient dans la source ; aucun recours préalable, justificatif ou délai nouveau n'est créé.",
    [effect('coordination', 'contrat-unique-protections-speciales',
            "Maintien des réparations de l'illégalité et rectification du renvoi procédural.",
            "Réparation au montant de L1235-3-1, cumul avec L1226-14 et renvoi au dernier alinéa procédural de L1226-12.",
            "Mêmes réparations, renvoi identifié par son objet et exclusion expresse du seuil et du plafond de l'indemnité ordinaire.",
            'legal_duty', "Salariés licenciés en violation de la réintégration ou du reclassement après accident ou maladie professionnels.",
            "Transition source de l'ordonnance du 22 septembre 2017 conservée ; contrats nouveaux également protégés.",
            "Pas de formalité ni sanction nouvelle ; les deux régimes de réparation restent distincts.",
            "le juge octroie une indemnité au salarié dont le montant est fixé conformément aux dispositions de l'article L. 1235-3-1.",
            "Les réparations du présent article ne sont soumises ni au seuil d’un an ni au plafond de six mois propres à l’indemnité ordinaire du contrat de travail unique.")])

a = A['L1226-18']
a['reason'] += " Le texte antérieur proposé est conservé après seconde passe : il ne crée pas un nouveau cas de rupture ni une exception au contrat unique."
a['review_notes'] += " Les renvois explicites à L. 1226-9 et L. 1226-13, absents des cibles fournies, ont été vérifiés dans travail.json en source et proposition : protection du nouveau contrat et nullité demeurent dans leurs champs propres."
a['substantive_impact'] = impact(
    'coordination_only',
    "La protection de suspension de la source, limitée aux exceptions de faute grave et de force majeure, est intégralement maintenue pour les anciens CDD. Les nouveaux emplois relèvent du contrat unique et des protections générales ; aucune autorisation ou démarche autonome n'est supprimée ici.",
    "La limitation de rupture des anciens CDD protège la santé et demeure nécessaire jusqu'à leur extinction et pour les recours ultérieurs. L'impossibilité générale de maintien pour motif étranger à l'accident ne remplace pas leur exception plus stricte de force majeure.",
    "Aucune charge nouvelle n'est identifiée : mêmes exceptions à prouver pour les anciens CDD, sans dossier additionnel. Les nouveaux contrats relèvent des protections générales déjà applicables au contrat sans terme.",
    [effect('coordination', 'contrat-unique-suppression-cdd',
            "Conservation de la protection des CDD antérieurs pendant l'arrêt professionnel.",
            "Protection de tous les CDD contre la rupture pendant la suspension, sauf faute grave ou force majeure.",
            "Protection conservée pour les CDD antérieurs ; nouveaux contrats sans terme protégés selon L1226-9 et L1226-13.",
            'regime', "Victimes d'accident du travail ou de maladie professionnelle sous ancien CDD ou contrat unique nouveau.",
            "Suspensions et ruptures postérieures de contrats anciens incluses ; créances et recours survivent au terme ; aucun nouveau renouvellement CDD.",
            "Pas de préavis libre de quinze jours appliqué à l'ancien CDD ; pas de procédure de remplacement.",
            "l'employeur ne peut rompre le contrat au cours des périodes de suspension du contrat que s'il justifie soit d'une faute grave de l'intéressé, soit d'un cas de force majeure.",
            "Cette protection demeure applicable aux suspensions et aux ruptures de ces contrats intervenant après cette entrée en vigueur.")])

a = A['L1226-19']
a['reason'] += " La source ne porte aucun impôt, agrément ou justificatif à supprimer. Le brouillon est donc conservé pour sa transition, sans comptabiliser la justification du motif et le plancher réparateur comme des charges administratives retirables."
a['review_notes'] += " L. 1241-1, L. 1243-1 et L. 1243-13 sont des coordinations hors des cibles fournies, lues dans travail.json. Les reports légaux du terme mentionnés par L. 1241-1 proposé restent distincts de la suspension pour accident, qui ne reporte pas elle-même l'échéance. La réforme ne doit pas servir de motif automatique de refus indemne de tout contrôle d'une clause antérieure."
a['substantive_impact'] = impact(
    'coordination_only',
    "Les deux règles source sont préservées pour les contrats antérieurs : la suspension n'empêche pas l'échéance et le refus de renouvellement pendant la suspension requiert un motif réel et sérieux étranger à l'accident, avec réparation minimale. La transition interdit un nouveau renouvellement à terme sans effacer les droits attachés à l'ancienne clause.",
    "L'indemnité n'est ni un forfait ordinaire ni un plafond de six mois : elle couvre le préjudice avec salaires et avantages de la période prévue. Son ouverture reste appréciée selon les faits et les clauses antérieures ; aucune indemnité automatique nouvelle ni économie nette n'est déduite de l'interdiction des nouveaux CDD.",
    "Aucune charge nouvelle n'est identifiée : pas d'avenant de conversion imposé ni de preuve supplémentaire du motif. Le contrôle existant du refus et les droits à réparation survivent ; une poursuite convenue se fait dans le contrat unique.",
    [effect('coordination', 'contrat-unique-suppression-cdd',
            "Transition des clauses anciennes de renouvellement sans réouverture du CDD futur.",
            "Échéance du CDD malgré suspension et protection d'une clause de renouvellement contre un refus lié à l'accident.",
            "Anciennes échéances et protection des clauses conservées, mais aucune convention nouvelle de renouvellement à terme ; poursuite convenue sans terme.",
            'regime', "Salariés en CDD antérieur suspendu pour accident du travail ou maladie professionnelle.",
            "Clauses et renouvellements valablement convenus avant réforme protégés, recours après réforme possibles ; reports légaux distincts conservés.",
            "Motif étranger à l'accident et réparation minimale maintenus ; aucune déclaration ni nouvelle condition pour l'indemnité.",
            "l'employeur ne peut, au cours des périodes de suspension, refuser le renouvellement que s'il justifie d'un motif réel et sérieux, étranger à l'accident ou à la maladie.",
            "Le présent article ne permet de convenir d’aucun nouveau renouvellement à durée déterminée à compter de cette entrée en vigueur.")])

a = A['L1226-21']
a['reason'] += " Le brouillon est conservé, sans prétendre supprimer à nouveau le régime général du CDD ni réduire les dommages d'une rupture illégale."
a['review_notes'] += " Les renvois L. 1226-8, L. 1226-10, L. 1226-11 et L. 1226-13, non fournis comme cibles, sont lus dans travail.json ; aucun nouveau renvoi non fourni n'est ajouté. Le seuil et le plafond ordinaires ne limitent ni le plancher des anciens CDD ni le minimum de réparation de L. 1226-15 applicable aux contrats nouveaux."
a['substantive_impact'] = impact(
    'coordination_only',
    "Les deux réparations source, pour le salarié apte ou inapte, sont conservées avec leur plancher de salaires et avantages jusqu'au terme en cours. Le renvoi au deuxième alinéa de L1226-20 est identifié par les cas autorisant la rupture, car la proposition cible ajoute un alinéa introductif. Aucune indemnité de l'illégalité n'est supprimée.",
    "Le régime de terme vise les anciens CDD, même pour les ruptures et recours futurs ; les nouvelles embauches relèvent des protections générales. Aucune conclusion n'est tirée sur une période de renouvellement seulement éventuelle, qui relève de L1226-19, ni sur un solde financier global.",
    "Aucune charge nouvelle n'est identifiée : même réparation du préjudice et même plancher, sans demande préalable ni dossier nouveau. La transition n'impose pas une conversion ou une renonciation aux recours.",
    [effect('coordination', 'contrat-unique-suppression-cdd',
            "Continuité de la réparation des anciens CDD et renvoi précis aux cas d'inaptitude.",
            "Réparation plancher des ruptures illégales du CDD ; second alinéa de L1226-20 officiel visé pour les cas d'inaptitude.",
            "Même réparation pour les anciens CDD, renvoi par objet à L1226-20 proposé et protections distinctes des contrats uniques.",
            'regime', "Salariés sous ancien CDD victimes d'une rupture méconnaissant la réintégration ou le reclassement.",
            "Contrats antérieurs, même en cas de rupture ou de recours après réforme ; ni seuil ordinaire d'un an ni plafond de six mois pour les dommages.",
            "Aucune formalité nouvelle ; pas d'importation de la rupture ordinaire du contrat unique dans l'ancien CDD.",
            "ou du deuxième alinéa de l'article L. 1226-20.",
            "ou des dispositions de l’article L. 1226-20 qui déterminent les cas autorisant la rupture pour inaptitude.")])

a = A['L1226-22']
a['reason'] += " Cette réserve transitoire rend la garantie utilisable pour les anciens contrats sans maintenir de nouveaux CDD ; le brouillon est conservé sans suppression additionnelle."
a['review_notes'] += " Les sources et notes de L. 1226-17 et L. 3253-15, L. 3253-19, L. 3253-20, L. 3253-21 ont été lues dans travail.json, hors des cibles fournies. Leurs délais de dix jours, trois mois, cinq ou huit jours selon l'objet, les relevés et contrôles ne sont ni retirés ni transformés en nouveau dossier par cet article."
a['substantive_impact'] = impact(
    'coordination_only',
    "La garantie de paiement de la source est conservée dans les trois procédures judiciaires avec tous les articles cités. La proposition explicite qu'elle couvre aussi les créances futures des anciens CDD et articule L1226-17 pour les contrats nouveaux. Aucun prélèvement ni formalité autonome de L1226-22 n'est supprimé.",
    "Le paiement reste dans les limites de la garantie salariale et selon ses relevés, fonds et contrôles propres. Les articles L3253 ne sont pas réécrits dans ce lot ; aucun paiement illimité, accélération de leurs délais ou financement supplémentaire n'est annoncé.",
    "Aucune charge nouvelle n'est identifiée : les relevés du mandataire et les contrôles existaient dans les règles appelées par la source. Aucun dossier supplémentaire ni double paiement d'une même créance n'est créé.",
    [effect('coordination', 'contrat-unique-suppression-cdd',
            "Garantie de paiement des indemnités des anciens CDD au-delà de la date de réforme.",
            "Application de L3253-15 et L3253-19 à L3253-21 aux indemnités de L1226-20 et L1226-21.",
            "Même garantie pour les anciens CDD, y compris leurs créances postérieures, et articulation de L1226-17 pour les contrats uniques nouveaux.",
            'regime', "Salariés créanciers d'indemnités d'inaptitude dans une sauvegarde, un redressement ou une liquidation judiciaire.",
            "Ancien contrat déterminé par sa conclusion, non par la date de créance ou d'ouverture de la procédure ; conditions de garantie inchangées.",
            "Pas de nouveau relevé, de paiement doublé ni de cotisation créée par la transition.",
            "les dispositions relatives aux créances salariales mentionnées aux articles L. 3253-15, L. 3253-19 à L. 3253-21 sont applicables au paiement des indemnités prévues aux articles L. 1226-20 et L. 1226-21.",
            "même lorsque la créance naît ou que la procédure collective est ouverte après cette entrée en vigueur.")])

a = A['L1231-2']
a['reason'] += " Le brouillon est conservé parce que la réserve générale doit demeurer opératoire face aux règles nouvelles ; retirer une autorisation particulière par cette clause générale serait une abrogation implicite hors de son objet. Aucune coupe autonome n'est donc revendiquée."
a['review_notes'] += " Le renvoi contextuel à L. 1231-1 a été vérifié dans travail.json hors des cibles ; ses règles d'essai ne sont pas effacées. La compatibilité avec les normes supérieures n'est pas établie par une simple réserve générale et doit être contrôlée sur les textes internationaux pertinents dans la coordination générale, sans nouvel accès externe dans ce travail."
a['benefit_review'] = "La réserve source protège toutes les dispositions légales particulières, sans liste fermée de bénéficiaires. La proposition la conserve et maintient explicitement, pour les futures situations éligibles aussi, santé, maternité, représentation, dispenses favorables de préavis, salaires et congés acquis, indemnités spéciales, réparations et droits transitoires. Les autorisations des salariés protégés et les procédures collectives conservent leur objet essentiel ; ce ne sont ni une exonération fiscale supprimable ni un délai de préavis ordinaire. Le seuil d'un an et le plafond de six mois ne ferment aucun de ces avantages."
a['substantive_impact'] = impact(
    'coordination_only',
    "La réserve générale source demeure entière dans son champ et est explicitée pour les paramètres du contrat unique. Aucune autorisation spéciale ni protection essentielle n'est supprimée par cet article. La dispense favorable de préavis et les réparations restent ouvertes selon leurs conditions, sans réduction autonome attribuée à la clarification.",
    "Les quinze jours concernent le préavis individuel des nouveaux contrats ; ils ne fixent pas la durée d'une procédure collective ni d'une autorisation de salarié protégé. Les règles particulières et les contraintes supérieures nécessitent leur propre examen ; le solde global des codes reste non chiffré.",
    "Aucune charge nouvelle n'est identifiée : les procédures et protections réservées ont un fondement antérieur autonome. Le texte ne crée ni autorisation, déclaration ou registre, ni nouveau délai minimal.",
    [effect('coordination', 'contrat-unique-protections-speciales',
            "Réserve générale des protections face au nouveau préavis et à l'indemnité ordinaire.",
            "Le titre de rupture ne déroge pas aux protections légales particulières.",
            "Même réserve, avec explicitation des dispenses, procédures distinctes, indemnités spéciales et créances hors plafond ordinaire.",
            'legal_duty', "Salariés bénéficiant d'une protection légale particulière, y compris les futurs bénéficiaires sous contrat unique.",
            "Conditions propres de chaque protection et transitions des anciens contrats conservées ; pas de régime public attribué au contrat privé.",
            "Aucune formalité de remplacement ou procédure nouvelle ; les délais spéciaux existants restent distincts.",
            "Les dispositions du présent titre ne dérogent pas aux dispositions légales assurant une protection particulière à certains salariés.",
            "Les dispenses de préavis favorables au salarié, notamment à son initiative, restent applicables selon leurs conditions propres.")])

a = A['L1231-3']
a.update(status='retained_unchanged', proposed_xml=None)
a['reason'] = "Maintien intégral nécessaire de la source après examen du brouillon. L'article fixe seulement le champ du titre lorsque le salarié a plusieurs employeurs : il ne crée ni autorisation de cumul, ni dossier, ni justificatif. Le supprimer introduirait une incertitude sur les droits de rupture sans alléger une charge démontrée. La précision stylistique du brouillon ne justifie pas une nouvelle norme. La source générale s'applique déjà à chaque relation selon son régime propre, y compris le contrat unique nouveau."
a['review_notes'] = "L. 1231-1 a été lu dans travail.json hors des cibles, et L. 1231-2 est examiné dans ce lot. Le maintien de la source ne fusionne pas les employeurs et n'additionne pas les anciennetés de contrats distincts. Un ancien contrat et un nouveau contrat unique peuvent relever de préavis différents ; les dispenses et indemnités spéciales gardent leur champ. Aucun renouvellement de CDD, solidarité nouvelle ou renonciation à un droit n'est créé. Une solidarité ou un coemploi fondé sur un autre texte reste à son régime autonome. Aucun renvoi incohérent ni nouvelle cible non fournie n'est introduit."
a['substantive_impact'] = impact(
    'retained_necessary',
    "La source entière est nécessaire comme règle de champ pour les salariés à plusieurs employeurs. Elle assure l'application du titre sans imposer de démarche autonome. Aucune réduction de prélèvement, de délai ou d'obligation n'est démontrée et la reformulation antérieure n'est pas comptée comme simplification.",
    "Les règles de cumul d'emplois, de temps de travail, de coemploi ou de solidarité ne sont pas modifiées par cette phrase. Chaque contrat garde sa date de référence et ses droits ; aucune mesure du coût de l'ensemble de ces régimes n'a été effectuée.",
    "Aucune charge nouvelle n'est identifiée : la source est maintenue intégralement, sans ajout de preuve, autorisation, déclaration, registre ni consolidation obligatoire des anciennetés.")

# La source de L1226-14 prévoit une compensation, pas le maintien nouveau
# du lien contractuel pendant quinze jours. Décrire aussi cet ajout concret :
# le seul effet « coordination » du montant ne décrit pas cette charge.
a = A['L1226-14']
a['proposed_xml'] = a['proposed_xml'].replace(
    "seule la composante nouvelle est calculée sur le barème de 0,20 mois par année et plafonnée à six mois avant doublement.",
    "seule la composante nouvelle est calculée sur le barème de 0,20 mois par année, au prorata des mois complets, et plafonnée à six mois avant doublement.")
a['substantive_impact']['effects'].append(effect(
    'deadline_increased', 'inaptitude-professionnelle-maintien-quinze-jours',
    "Ajout, dans ce régime spécial, d'un maintien du contrat nouveau jusqu'au terme des quinze jours non exécutés, distinct du calcul de la compensation.",
    "L1226-14 officiel ouvre une indemnité compensatrice de préavis et une indemnité spéciale ; il n'institue pas de période forfaitaire de maintien du contrat après notification. Les durées servant au montant de la compensation résultent des textes de préavis applicables.",
    "Pour le seul contrat unique nouveau, maintien du lien contractuel jusqu'à la fin du quinzième jour calendaire compté du lendemain de la notification selon L1234-3 ; les quinze jours entrent dans l'ancienneté spéciale et la compensation reste due une seule fois.",
    'calendar_days',
    "Employeurs et salariés sous contrat unique nouveau rompu dans les cas d'inaptitude professionnelle de L1226-12.",
    "Nouveaux contrats seulement ; ni modification de la date de rupture des anciens contrats, ni extinction de leur compensation. Les autorisations et procédures distinctes demeurent préalables dans leur champ.",
    "Ajout concret de quinze jours de lien contractuel et de droits d'ancienneté avant clôture ; aucune reprise du travail inapte ni deuxième indemnité de préavis. Le coût net face à la modification du montant de la compensation n'est pas établi.",
    "La rupture du contrat de travail dans les cas prévus au deuxième alinéa de l'article L. 1226-12 ouvre droit, pour le salarié, à une indemnité compensatrice d'un montant égal à celui de l'indemnité compensatrice de préavis prévue à l'article L. 1234-5",
    "il n’est pas exécuté et le contrat prend fin à l’expiration du quinzième jour, même non travaillé."))
a['substantive_impact']['new_burdens_review'] = (
    "Charge nouvelle identifiée : le nouveau contrat reste en vigueur jusqu'à l'expiration du quinzième jour calendaire, alors que la source prévoit une indemnité compensatrice sans instituer ce maintien forfaitaire. Cette prolongation ajoute des droits d'ancienneté et retarde la clôture du contrat. La ventilation des services anciens et futurs ajoute un suivi sur les données de paie existantes. Aucun registre, formulaire, agrément ou justificatif nouveau n'est créé ; la compensation n'est pas payée deux fois. Le solde financier de ces effets et des réductions coordonnées n'est pas établi.")
a['review_notes'] += (
    " L'effet ajouté de maintien du lien contractuel est décrit séparément du renvoi de montant : la source de L. 1226-14 ne fixe pas elle-même une date de fin ni un maintien forfaitaire de quinze jours. Aucun délai antérieur uniforme de zéro, un ou deux mois n'en est déduit sans distinguer date de rupture et durée servant à la compensation. Le nouvel effet identifie la règle expressément introduite dans la proposition ; il n'est pas compté comme une réduction additionnelle. Sa coordination avec les droits sociaux pendant cette période reste à contrôler hors des textes assignés.")

# Identifier exactement les nouveaux renvois non fournis, même si le brouillon
# antérieur les comportait déjà : la comparaison porte sur la source officielle.
a = A['L1226-21']
a['review_notes'] = a['review_notes'].replace(
    "Les renvois L. 1226-8, L. 1226-10, L. 1226-11 et L. 1226-13, non fournis comme cibles, sont lus dans travail.json ; aucun nouveau renvoi non fourni n'est ajouté.",
    "Les renvois sources à L. 1226-8, L. 1226-10 et L. 1226-11 ont été lus dans travail.json. Le renvoi ajouté à L. 1226-13, absent des cibles fournies, est expressément signalé : sa source entière et sa proposition ont été lues dans ce même corpus ; il prévoit la nullité des ruptures contraires à L. 1226-9 ou L. 1226-18, et non le barème de réparation d'un simple défaut de reclassement. Le renvoi ajouté à L. 1226-15 est fourni et contrôlé séparément.")
a = A['L1225-66']
a['review_notes'] = a['review_notes'].replace(
    "le premier alinéa de R. 1225-18", "la première phrase de R. 1225-18").replace(
    "Son second alinéa, relatif à la demande de réembauche", "Sa seconde phrase, relative à la demande de réembauche").replace(
    "du premier alinéa de R. 1225-18", "de la première phrase de R. 1225-18")

# Analyses propres à chaque couple source/cible, avec les empreintes de la vue fournie.
checks = {
 'L1225-66': {
  'L1234-1': "Le préavis patronal de quinze jours de la proposition L1234-1 n'est pas la prévenance parentale : L1225-66 conserve une dispense à l'initiative du salarié. Aucun préavis nouveau n'est donc imposé au départ parental, quelle que soit l'ancienneté ou la date du contrat.",
  'L1221-2': "Le contrat unique sans terme des nouvelles embauches n'empêche pas la rupture parentale spéciale. La dispense demeure pour les contrats antérieurs et futurs ; l'enfant ou la fin du congé ne devient pas un terme automatique d'emploi.",
  'L1234-9': "La dispense d'indemnité à verser par le parent ne doit pas être confondue avec l'indemnité ordinaire due par l'employeur. Ce départ à l'initiative du salarié n'ouvre pas celle-ci ; son seuil d'un an ne conditionne ni la dispense ni la priorité de réembauche."},
 'L1226-4': {
  'L1234-1': "La proposition générale impose quinze jours aux nouveaux contrats ; L1226-4 conserve la non-exécution propre à l'inaptitude non professionnelle. Les anciens contrats gardent leur fin à notification et leur décompte de préavis pour l'indemnité ; aucun délai collectif n'est supprimé.",
  'L1234-3': "Le renvoi porte sur le second alinéa proposé : quinze jours à partir du lendemain de la présentation, ou de la réception/remise si cette forme est légalement autorisée, fin au quinzième jour même non travaillé. Il ne rend pas un courriel quelconque valable et ne modifie pas la notification des anciens contrats.",
  'L1234-5': "La dérogation source excluant la compensation du préavis inexécuté est conservée pour cette seule inaptitude non professionnelle. Elle ne retire pas les autres salaires éventuellement dus ni l'indemnité spéciale sans seuil de L1226-4-3 proposé ; elle n'est pas étendue à L1226-14.",
  'L1221-2': "Le nouveau préavis vise les contrats uniques sans terme conclus après la réforme. Il ne crée pas de rupture libre d'un ancien CDD, lequel conserve ses causes propres via L1226-4-2 et L1226-4-3 ; une mission limitée n'abrège pas le contrat unique.",
  'L1234-9': "Pour le nouveau contrat, le seuil d'un an est apprécié à la fin effective, quinze jours inclus, puis tout le service est calculé à 0,20 mois par année, fractions en mois complets, au plus six mois. La transition des anciens contrats et la garantie spéciale sans seuil restent distinctes.",
  'L1226-4-3': "Le renvoi ajouté réserve la garantie spéciale que cette proposition étend au contrat unique sans seuil d'un an. Sa source officielle ne vise que le CDD : l'extension est donc un choix du projet, non du droit existant. Les modalités anciennes L1243-8 survivent pour les anciens CDD."},
 'L1226-4-1': {
  'L1234-1': "Le paiement direct ou par garantie souscrite ne modifie aucune durée de préavis. Il ne transforme pas l'inaptitude en licenciement libre et ne remplace pas la fin particulière prévue par L1226-4 ; l'ancienneté relève des dispositions d'indemnisation, pas du fonds.",
  'L1221-2': "La faculté de couverture n'est pas attachée au support CDD et reste utilisable pour les futures ruptures de contrats uniques éligibles. La désignation du gestionnaire n'autorise aucun nouveau contrat à terme et ne limite pas l'emploi à la durée d'une garantie.",
  'L1234-9': "Le fonds ne garantit que les indemnités dues et couvertes. Le nouveau barème ordinaire et la transition s'appliquent par leurs textes propres ; aucune ancienne annualité ou condition de huit mois n'est figée ici. Les indemnités spéciales sans seuil ne sont pas fermées par la condition ordinaire d'un an."},
 'L1226-4-2': {
  'L1234-1': "Le préavis de quinze jours de L1234-1 proposé ne s'applique pas comme faculté de rupture d'un ancien CDD. Le renvoi à L1226-4 conserve la reprise du salaire dans son champ et doit être articulé aux causes de rupture propres à l'ancien contrat.",
  'L1221-2': "La proposition interdit toute nouvelle embauche à terme et tout renouvellement décidé après réforme. L1226-4-2 conserve uniquement le régime de contrats déjà conclus, y compris l'inaptitude ultérieure, et ne fait pas de la formation ou d'une aide un terme d'emploi.",
  'L1226-4-3': "La source de la cible organise l'indemnité CDD d'inaptitude et son versement comme la prime de L1243-8. Sa proposition protège les anciens contrats et une indemnité spéciale future du contrat unique sans seuil d'un an ; le renvoi de L1226-4-2 ne doit pas neutraliser cette seconde garantie.",
  'L1226-4': "Le renvoi source à tout L1226-4 est maintenu pour les anciens CDD sous leurs règles de rupture propres. La proposition cible distingue la fin à notification des anciens contrats du délai nouveau ; la proposition finale du lot réserve aussi L1226-4-3, sans attribuer au CDD un préavis CDI inexistant.",
  'L1234-9': "Le seuil ordinaire d'un an et le plafond de six mois ne remplacent pas la garantie spéciale du CDD inapte ni celle étendue au contrat unique par L1226-4-3 proposé. La conversion convenue garde le service acquis et n'autorise aucun double compte d'une même période."},
 'L1226-14': {
  'L1234-1': "Les quinze jours des nouveaux contrats sont non exécutés et compensés dans le cas professionnel ; ils ne sont pas confondus avec les délais de procédure. Les anciens contrats conservent les durées qui résultent de leur régime, et la garantie spéciale ne disparaît pas avant un an.",
  'L1234-3': "Le décompte nouveau reprend le second alinéa proposé : lendemain de présentation ou réception/remise légalement admise, puis expiration à la fin du quinzième jour. Cette date sert à l'ancienneté spéciale ; aucune modification de forme de notification ne résulte du simple renvoi.",
  'L1234-5': "Le renvoi fixe le montant de la compensation spéciale, salaires et avantages compris, sans créer une seconde indemnité pour la même période. L'exclusion particulière de L1226-4 pour l'inaptitude non professionnelle n'est pas transposée ; la condition ordinaire d'un an est inapplicable.",
  'L1221-2': "La règle nouvelle ne vise que l'emploi sans terme des contrats conclus après la réforme. Les anciens contrats gardent leurs droits et le CDD professionnel relève de L1226-20 dans son champ ; la fin d'une mission n'emporte jamais la rupture automatique d'un contrat unique.",
  'L1234-9': "Le renvoi au barème sert au doublement, sans importer le seuil d'un an ou l'exclusion ordinaire pour faute grave. La composante nouvelle de 0,20 mois par année est doublée, avec mois complets et plafond de douze mois après doublement ; les taux et minima de services anciens et conventions plus favorables subsistent."},
 'L1226-15': {
  'L1226-14': "Le cumul vise la compensation de préavis et, s'il y a lieu, l'indemnité spéciale de la cible, non une deuxième indemnité ordinaire. La proposition finale précise les mois complets dans L1226-14 sans changer la vue fournie citée ici ; les dommages de L1226-15 restent hors du seuil et du plafond ordinaires.",
  'L1234-1': "Le préavis nouveau de quinze jours ne remplace pas l'obligation de réintégrer ou de reclasser avant une rupture licite. La réparation d'une violation reste due selon sa propre règle ; sa durée de référence n'est ni quinze jours ni limitée à l'ancienneté d'un an.",
  'L1221-2': "Le contrat unique reçoit les protections de réintégration et de reclassement sans terme de mission ou de formation. Les ruptures anciennes et la transition historique de 2017 restent appréciées selon leurs périodes propres ; le projet de la cible n'est pas le droit actuel.",
  'L1234-9': "L'indemnité ordinaire de 0,20 mois par année et son plafond de six mois ne constituent pas le montant des dommages de L1226-15. Le seuil d'un an ne ferme pas le recours dès le premier jour ; les indemnités spéciales et composantes anciennes gardent leur champ.",
  'L1235-3-1': "Le renvoi source au montant de cette cible conserve le minimum des salaires des six derniers mois et l'absence de barème L1235-3 dans son champ. Ce minimum n'est pas un plafond ; le cumul prévu par L1226-15 et les salaires dus sur un fondement autonome ne sont pas effacés."},
 'L1226-18': {
  'L1234-1': "Le préavis de quinze jours n'autorise pas une rupture d'ancien CDD pendant sa suspension hors faute grave ou force majeure. Pour le nouveau contrat unique, le préavis individuel ne dispense pas de la protection de santé ni des autorisations éventuellement requises.",
  'L1221-2': "Le support CDD de L1226-18 est réservé aux contrats déjà conclus. Les futurs salariés, même affectés à une mission limitée, sont en contrat unique ; la protection de suspension relève alors de L1226-9 et L1226-13 sans création d'un nouveau CDD spécial.",
  'L1234-9': "Aucun seuil d'ancienneté de rupture ordinaire ne conditionne la nullité d'une rupture pendant la suspension. Les dommages d'une illégalité et les créances des anciens CDD ne sont ni supprimés avant un an ni plafonnés par les six mois de L1234-9 proposé."},
 'L1226-19': {
  'L1234-1': "Le maintien du terme ancien malgré la suspension n'est pas un licenciement sous quinze jours. Ni ce préavis ni sa notification n'effacent le contrôle du motif de refus d'une clause ancienne de renouvellement ou le plancher de réparation fondé sur salaires et avantages.",
  'L1221-2': "L'interdiction de décider un nouveau renouvellement à terme après réforme s'applique même à une clause ancienne. Les périodes déjà valablement convenues et les recours liés à cette clause demeurent ; une poursuite convenue est sans terme et conserve l'ancienneté acquise.",
  'L1234-9': "Le plancher réparateur de L1226-19 est lié aux salaires et avantages jusqu'au terme de renouvellement prévu, pas au barème ordinaire. Il n'est donc soumis ni au seuil d'un an ni au plafond de six mois ; l'ancienneté n'est pas remise à zéro en cas de poursuite sans terme."},
 'L1226-21': {
  'L1234-1': "La rupture illégale de l'ancien CDD n'est pas régularisée par quinze jours de préavis. Le droit à réparation jusqu'au terme en cours subsiste, et le nouveau contrat unique relève des protections de L1226-13 ou L1226-15, sans suppression de procédures spéciales.",
  'L1221-2': "La transition limite le régime de terme aux CDD antérieurs et conserve leurs recours après réforme. Pour le contrat unique futur, mission ou formation n'est pas un terme ; les protections générales s'appliquent sans rétablir de nouveau CDD ni son renouvellement.",
  'L1226-20': "Le deuxième alinéa officiel énumère les causes de rupture pour inaptitude professionnelle. Dans la proposition cible, l'alinéa introductif supplémentaire décale cette règle : le renvoi final la vise par son objet, sans viser l'alinéa d'exclusion du régime CDI ni importer le seuil ordinaire d'un an.",
  'L1226-15': "Pour les nouveaux contrats, la réparation de la réintégration ou du reclassement méconnus suit la cible dans son champ, avec minimum L1235-3-1 et cumul spécial. Le plancher jusqu'au terme de L1226-21 reste propre aux anciens CDD ; aucun des deux n'est plafonné par le barème ordinaire.",
  'L1234-9': "Le préjudice et son plancher de salaires et avantages sont distincts de l'indemnité ordinaire de rupture. Le seuil d'un an, le taux de 0,20 mois et le plafond de six mois ne s'appliquent pas à ces dommages ; les situations anciennes et futurs recours sont expressément préservés."},
 'L1226-22': {
  'L1226-14': "Les indemnités des contrats uniques nouveaux pour inaptitude professionnelle suivent la garantie par L1226-17, tandis que les anciens CDD restent sous L1226-20 et L1226-22. Le doublement et la compensation ne donnent pas lieu à deux paiements ; les mois complets seront précisés dans la proposition finale du lot.",
  'L1234-1': "Les délais d'avance des créances salariales ne sont pas le préavis individuel de quinze jours. L1226-22 ne supprime ni jugement d'ouverture ni règles de relevé et ne transforme pas une procédure collective en une rupture complète réalisée dans ce délai.",
  'L1221-2': "La date de conclusion de l'ancien CDD détermine la survie de cette garantie, même si la créance ou l'ouverture judiciaire est future. Le contrat unique sans terme ne ferme pas la garantie d'une situation antérieure et aucune nouvelle embauche CDD n'est autorisée.",
  'L1226-21': "La réparation source et son plancher restent garantis dans les limites des articles L3253 cités, y compris si une rupture d'ancien CDD intervient après la réforme. Les indemnités des contrats uniques sous L1226-15 suivent l'articulation distincte de L1226-17, sans double versement.",
  'L1226-20': "La garantie couvre l'indemnité spéciale des anciens CDD dans les cas légaux d'inaptitude professionnelle, avec droits antérieurs préservés. Le nouveau contrat relève des articles L1226-14 à L1226-17 ; le renvoi de paiement ne lui importe ni un terme ni le seuil ordinaire d'un an.",
  'L1226-15': "Le renvoi contextuel aux réparations des contrats uniques s'articule avec L1226-17 et les conditions de garantie salariale. Il ne rend pas automatiquement payable toute demande et ne soumet pas la réparation de l'illégalité au plafond ordinaire de six mois.",
  'L1234-9': "Le fonds ne calcule pas toutes les créances d'après l'indemnité ordinaire : seuls les renvois de chaque indemnité en fixent la base. Le seuil d'un an ne ferme pas les minima spéciaux ni les dommages, et les composantes antérieures des anciens contrats demeurent protégées."},
 'L1231-2': {
  'L1234-1': "La réserve maintient les autorisations, procédures collectives et protections spéciales malgré le préavis de quinze jours des nouveaux contrats. Elle ne rétablit pas pour eux l'ancien préavis ordinaire ; les dispenses favorables et les régimes des contrats antérieurs gardent leur champ.",
  'L1221-2': "Le contrat unique reste une relation de travail privée sans terme ; il n'abolit pas maternité, santé ou représentation ni ne réforme implicitement les agents publics. Une phase de mission ou de formation n'est pas un terme et les protections restent ouvertes aux futurs bénéficiaires.",
  'L1234-9': "La réserve distingue l'indemnité ordinaire, seuil d'un an et plafond de six mois, des salaires, congés, dommages d'une illégalité et indemnités spéciales. Elle conserve les composantes de services antérieurs sans double compte ; aucune démission ordinaire ne reçoit une indemnité patronale nouvelle."},
 'L1231-3': {
  'L1234-1': "Le maintien intégral de la source applique le régime de préavis à chaque relation selon la date de son contrat : quinze jours pour un contrat unique nouveau, règles antérieures pour l'autre. Aucun préavis commun fusionné ni nouveau justificatif multi-employeurs n'est créé.",
  'L1221-2': "Chaque nouvelle relation concernée est sans terme, mais la pluralité d'employeurs ne transforme pas les anciens contrats ou les régimes publics. Le maintien de la règle source ne rétablit aucun nouveau CDD, terme de mission ou renouvellement décidé après réforme.",
  'L1234-9': "L'ancienneté et la condition d'un an se mesurent chez l'employeur concerné au terme effectif selon chaque contrat ; les anciennetés distinctes ne sont pas additionnées par cet article. La solidarité ou le coemploi sur fondement autonome restent réservés, ainsi que les indemnités spéciales sans seuil."}
}

for a in answers:
    source_key = a['code_id'] + '|' + a['source_id']
    required = refs['requirements'][source_key]
    numbers = [refs['targets'][k]['number'] for k in required]
    a['reference_checks'] = []
    for number in numbers:
        k, v = target_by_number[number]
        a['reference_checks'].append(dict(target_key=k, view_sha256=v['view_sha256'],
                                         assessment=checks[a['number']][number]))

Path('answer.json').write_text(json.dumps(answers, ensure_ascii=False, indent=2) + '\n')
print(f'{len(answers)} articles écrits dans answer.json')
