import json
import re
from html import unescape
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
references = json.loads(Path('reference-targets.json').read_text())
answers = []


def plain(xml):
    return re.sub(r'\s+', ' ', unescape(re.sub(r'<[^>]*>', ' ', xml or ''))).strip()


def article(i, xml, reason, notes, classification, assessment, limitations, burdens):
    src = sources[i]
    obj = {k: src[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    obj.update(proposed_xml=xml, reason=reason, review_notes=notes,
               status='retained_unchanged' if xml is None else 'rewrite_draft',
               substantive_impact=dict(version=1, classification=classification,
                   assessment=assessment, scope_limitations=limitations,
                   new_burdens_review=burdens, effects=[]))
    answers.append(obj)
    return obj


def effect(i, kind, measure, description, before, after, unit, population,
           transition, replacement, source_quote, proposed_quote):
    obj = answers[i]
    assert source_quote in plain(sources[i]['source_xml']), (i, source_quote)
    assert proposed_quote in plain(obj['proposed_xml']), (i, proposed_quote)
    obj['substantive_impact']['effects'].append(dict(
        kind=kind, measure_id=measure, description=description, before=before,
        after=after, unit=unit, affected_population=population,
        conditions_and_transition=transition,
        replacement_or_new_burdens=replacement, source_quote=source_quote,
        proposed_quote=proposed_quote))


def reduction(i, *removed):
    answers[i].update(change_type='normative_reduction',
                      reform_policy_id='editorial_direction_2026_10_19',
                      removed_provisions=list(removed))


article(0, None,
    "Maintien intégral après examen de la consultation et de l'autorisation subsidiaire : ces deux voies protègent l'indépendance du médecin lors de sa nomination. L'autorisation n'est exigée qu'en l'absence d'accord ; la supprimer supprimerait précisément l'arbitrage qui permet la nomination malgré ce désaccord. Aucun doublon documentaire, prélèvement ou délai minimal autonome n'est prévu ici. Le brouillon purement stylistique est écarté sans revendiquer une simplification.",
    "R4623-5 lu intégralement : l'accord concerne le CSE ou, en service interentreprises, le comité interentreprises ou la commission de contrôle, ainsi que le conseil d'administration. La consultation doit précéder la fin de l'essai ; elle ne prolonge pas celui-ci. La coordination travail fixe à trois mois sans renouvellement l'essai des nouveaux contrats, sans faire de la première année un essai. Les notes territoriales de 2009 et 2010 restent historiques. Les règles de notification, préavis et indemnité des L1234-1/L1234-9 ne régissent pas une nomination et ne remplacent pas cette procédure. Aucun renvoi du texte conservé n'est rendu incohérent par le contrat unique.",
    'retained_necessary',
    "La source entière est maintenue : consultation avant la fin de l'essai et autorisation de nomination seulement à défaut d'accord. L'examen n'identifie aucune charge détachable sans retirer une garantie d'indépendance ou la voie de résolution du désaccord.",
    "Aucune réduction de formalité, de coût ou de prélèvement n'est revendiquée. Le régime de l'essai et les procédures de rupture relèvent d'autres articles ; leur réforme n'est pas mesurée ici.",
    "Aucune charge nouvelle n'est identifiée : le texte source est conservé intégralement, sans déclaration, document, délai ni condition de remplacement.")


xml = sources[1]['previous_draft']['proposed_xml']
xml += "\n<p>Le préavis individuel du contrat unique ne dispense ni de cette consultation ni de l'autorisation administrative requise pour la rupture.</p>"
article(1, xml,
    "Coordination de fond avec la fermeture des nouveaux CDD privés, sans suppression de la protection des médecins titulaires d'un ancien CDD. L'audition, les instances compétentes et l'ordre entretien puis consultation restent nécessaires à une défense effective et à l'indépendance médicale. Le brouillon est conservé sur ces points ; le préavis individuel ne permet pas de les contourner. Aucune réduction indépendante de procédure n'est comptée.",
    "L4623-4/5 et R4623-19/21/22 lus en entier : avis des instances, vote secret à la majorité des membres présents ou représentés, un seul pouvoir par membre, enquête contradictoire et décision administrative demeurent distincts. L1232-2 est vérifié dans sa source et sa proposition : maintien de l'entretien, suppression proposée du minimum de cinq jours ouvrables mais temps effectif de préparation et d'assistance ; cet article ne rétablit pas ce minimum. L'entretien de licenciement n'est pas attribué indistinctement à une rupture conventionnelle. L4623-5-1 exige aussi la protection au terme d'un ancien CDD comportant une clause de renouvellement, même lorsque le nouveau renouvellement est interdit. La réserve des contrats publics ne crée aucune extension du champ initial et ne leur applique pas le contrat unique privé.",
    'coordination_only',
    "La seule différence normative par rapport à la source entière est la coordination de la catégorie des CDD privés avec leur extinction prospective. Audition, consultation et ordre procédural subsistent ; aucune suppression autonome d'autorisation ou de délai n'est établie.",
    "Le contrat unique provient de L1221-2 et la protection administrative de L4623-5/5-1 : cette coordination n'est pas une seconde fusion de régimes. Les statuts publics et les anciens CDD ne sont pas supprimés.",
    "Aucune charge nouvelle autonome n'est identifiée : mêmes auditions et instances, sans pièce ou consultation supplémentaire ; le rappel du préavis n'ajoute pas une nouvelle procédure.")
effect(1, 'coordination', 'contrat-unique-protection-medecin',
       "Réserver la branche CDD privée aux contrats antérieurs sans fermer leur protection au terme.",
       "La procédure vise la rupture d'un CDD dans les cas de L4623-5-1, sans distinction de date de conclusion.",
       "Pour le droit privé, elle continue de viser ces cas pour les CDD antérieurs ; les nouveaux emplois sont à durée indéterminée et restent protégés.",
       'regime', "Médecins du travail de droit privé ; réserve du champ public préexistant.",
       "À l'entrée en vigueur du contrat unique ; anciens CDD protégés, aucun nouveau renouvellement autorisé.",
       "Aucune formalité de remplacement ; maintien de l'audition et du contrôle administratif.",
       "dans les cas prévus à l'article L. 4623-5-1",
       "Il en va de même pour la rupture d'un contrat à durée déterminée conclu avant l'entrée en vigueur de la loi instituant le contrat unique à durée indéterminée, dans les cas prévus à l'article L. 4623-5-1.")


xml = """<p>L'employeur adresse à l'inspecteur du travail dont dépend le service de prévention et de santé au travail qui emploie le médecin, par tout moyen permettant de conférer date certaine, la demande d'autorisation de licenciement. Pour les contrats à durée déterminée conclus avant l'entrée en vigueur de la loi instituant le contrat unique à durée indéterminée, il lui adresse dans les mêmes conditions la demande d'autorisation prévue à l'article L. 4623-5-1 ou la demande de constatation de l'arrivée du terme prévue à l'article L. 4623-5-2. Lorsque les deux articles s'appliquent à la même arrivée du terme, une seule demande et une seule décision comportant l'autorisation et la constatation requises suffisent ; aucune seconde saisine n'est exigée.</p>
<p>En cas de licenciement, de rupture anticipée ou de non-renouvellement d'un ancien contrat à durée déterminée, la demande expose les motifs de la mesure envisagée. Elle est accompagnée du procès-verbal de la réunion des instances mentionnées à l'article R. 4623-18, sauf si l'inspecteur saisi en dispose déjà légalement dans sa version complète, exacte et à jour. Les pièces nécessaires déjà légalement détenues par cet inspecteur sont réutilisées sans nouvelle remise ; seules les informations manquantes ou modifiées nécessaires à l'examen peuvent être demandées.</p>
<p>La demande est transmise dans les quinze jours suivant la délibération des instances mentionnées à l'article R. 4623-18, sous réserve du délai de quarante-huit heures applicable en cas de mise à pied. Pour la constatation de l'arrivée du terme d'un ancien CDD, la saisine intervient avant le terme, conformément à l'article L. 4623-5-2 ; aucun délai minimal d'un mois n'est rétabli par le présent article.</p>
<p>En cas de mise à pied, ces instances sont consultées dans les dix jours à compter de celle-ci.</p>
<p>Dans ce cas, la demande d'autorisation de licenciement, de rupture de l'ancien contrat à durée déterminée avant son terme ou de non-renouvellement est transmise à l'inspecteur du travail dans les quarante-huit heures suivant la délibération de ces instances.</p>
<p>La demande commune et la réutilisation des pièces s'appliquent aux demandes nouvelles et aux procédures en cours à compter de l'entrée en vigueur de la loi portant cette simplification, sans nouveau dépôt ni reprise des actes et délais régulièrement accomplis. La régularité des actes antérieurs reste appréciée selon les règles qui leur étaient applicables. Consultation, motivation, enquête contradictoire et autorisation ou constatation demeurent requises ; le silence au terme ne vaut pas décision favorable. Aucun nouveau CDD de droit privé ni renouvellement n'est autorisé après l'entrée en vigueur du contrat unique. Le préavis individuel ne permet pas de rompre avant la décision administrative requise.</p>
<p>Pour les contrats de droit public entrant dans le champ du présent article, les dispositions relatives aux contrats à durée déterminée demeurent applicables sans limitation tenant à la date d'entrée en vigueur du contrat unique de droit privé.</p>"""
article(2, xml,
    "La dispense de nouvelle copie du procès-verbal est conservée et étendue aux pièces nécessaires déjà détenues légalement, sans nouvelle attestation. Le dossier et la décision uniques coordonnent expressément les propositions actuelles de L4623-5-1/5-2 pour l'arrivée du terme d'un ancien CDD ; cette coordination ne constitue pas une seconde suppression. Contrairement au brouillon antérieur, aucun délai minimal d'un mois n'est rétabli. Les délais maximaux de saisine et la voie urgente après mise à pied protègent le médecin et sont maintenus.",
    "Vérification des sources et propositions de L4623-5-1/5-2 et de R4623-18 : une même décision doit comporter autorisation et constatation lorsqu'elles sont toutes deux requises. La proposition actuelle de L4623-5-2 supprime le minimum d'un mois : la note du brouillon qui le disait encore opposable est rectifiée. L'autorité doit toujours statuer avant le terme, sans autorisation tacite. Quinze jours, dix jours et quarante-huit heures sont conservés ; ce sont des délais procéduraux distincts du préavis de quinze jours calendaires. Ambiguïté préexistante signalée : le dernier alinéa source ne répète pas la condition de mise à pied ; le texte retient expressément son rattachement à l'alinéa précédent, déjà retenu dans le brouillon, à confronter à l'historique réglementaire. R4623-21, lu en entier, garde son enquête et ses délais de quinze/huit jours, prolongeables si nécessaires. Aucun nouveau renvoi à une cible absente de reference-targets.json n'est introduit dans le texte.",
    'material_reduction',
    "Par rapport à la source officielle entière, les remises répétées de pièces déjà détenues sont effectivement retirées. La procédure commune et la disparition du minimum d'un mois sont des coordinations des cibles législatives actuelles, sans retrait du contrôle d'indépendance ni double compte de ces mesures.",
    "L'allègement documentaire suppose une détention légale de pièces complètes, exactes et à jour. Les pièces manquantes, l'avis des instances et l'autorisation restent exigibles ; ni le coût total ni les délais réels de décision ne sont chiffrés.",
    "Aucune charge nouvelle n'est identifiée : pas de déclaration, de certificat de détention ou de second dossier. Les informations manquantes demeurent celles nécessaires au contrôle déjà prévu ; la décision unique porte les deux appréciations existantes.")
reduction(2,
    "Nouvelle remise obligatoire du procès-verbal déjà légalement détenu dans sa version complète, exacte et à jour par l'inspecteur saisi.",
    "Remises répétées de pièces nécessaires déjà légalement détenues par le même inspecteur dans la procédure d'autorisation ou de constatation.")
effect(2, 'compliance_cost_reduced', 'medecins-reemploi-pieces-rupture',
       "Dispense des copies répétées de pièces déjà détenues, au-delà du seul procès-verbal visé par le brouillon.",
       "La demande doit être accompagnée du procès-verbal sans dispense expresse de nouvelle copie.",
       "Aucune nouvelle remise des pièces nécessaires déjà légalement détenues, exactes et à jour ; compléments limités aux éléments manquants ou modifiés nécessaires.",
       'legal_duty', "Employeurs demandant l'autorisation de rupture d'un médecin du travail et inspecteur saisi.",
       "Demandes nouvelles et procédures en cours dès l'entrée en vigueur, sans recommencer les actes accomplis.",
       "Aucune attestation de remplacement ; mêmes éléments de fond et contrôle contradictoire.",
       "Elle est accompagnée du procès-verbal de la réunion des instances mentionnées à l'article R. 4623-18.",
       "Les pièces nécessaires déjà légalement détenues par cet inspecteur sont réutilisées sans nouvelle remise ; seules les informations manquantes ou modifiées nécessaires à l'examen peuvent être demandées.")
effect(2, 'coordination', 'medecins-demande-unique-fin-cdd',
       "Mettre le règlement en cohérence avec la saisine et la décision communes de L4623-5-1/5-2 proposés, sans recréer le minimum d'un mois.",
       "Le premier alinéa distingue les demandes d'autorisation et de constatation ; L4623-5-2 officiel prévoit un mois avant le terme.",
       "Une seule demande et une décision à double contenu pour la même fin de CDD ; saisine avant terme, sans minimum d'un mois, décision toujours préalable à la fin du contrat.",
       'legal_duty', "Médecins du travail titulaires d'anciens CDD et leurs employeurs.",
       "Coordination des demandes nouvelles et en cours avec les cibles proposées ; la légalité des actes antérieurs reste appréciée selon leur régime.",
       "Aucune seconde demande ni autorisation tacite ; consultation et contrôle de fond préservés.",
       "la demande de constatation de l'arrivée du terme du contrat dans le cas prévu à l'article L. 4623-5-2",
       "Lorsque les deux articles s'appliquent à la même arrivée du terme, une seule demande et une seule décision comportant l'autorisation et la constatation requises suffisent ; aucune seconde saisine n'est exigée.")


xml = """<p>Le candidat à l'autorisation d'exercice est lié par un contrat de travail conclu avec l'employeur ou le président du service de prévention et de santé au travail interentreprises. Pour les recrutements de droit privé intervenant à compter de l'entrée en vigueur de la loi instituant le contrat unique, ce contrat est à durée indéterminée.</p>
<p>Pour ces nouveaux contrats, les fonctions sont exercées dans les conditions du second alinéa du I de l'article R. 4623-25-3. Lorsqu'un stage est prescrit en application de l'article R. 4111-17 du code de la santé publique, la période d'accomplissement du stage au titre du présent article correspond à sa durée prescrite, dans la limite de trois ans. La fin des fonctions requises ou du stage ne met pas automatiquement fin à l'emploi et ne dispense pas de l'autorisation nécessaire à l'exercice de la médecine.</p>
<p>La rupture individuelle du nouveau contrat de droit privé est soumise à un préavis de quinze jours calendaires pour l'employeur comme pour le salarié, sous réserve des dispenses favorables ouvertes à ce dernier. Le délai se compte à partir du lendemain de la présentation ou, lorsque la forme de notification est légalement admise, de la réception de la notification écrite, dans les conditions de l'article L. 1234-3. Le motif patronal doit être valable et contrôlable ; les garanties de défense, de non-discrimination, de santé, de maternité et de représentation, les autorisations spéciales et les recours restent applicables. Les procédures collectives et leurs délais sont distincts du préavis individuel. Dans les conditions de l'article L. 1234-9, l'indemnité ordinaire est due uniquement lorsque l'employeur rompt : aucune avant un an d'ancienneté ; à partir d'un an, 0,20 mois du salaire brut de référence déterminé selon l'article R. 1234-4 par année totale d'ancienneté, au prorata des mois complets pour une année incomplète conformément à l'article R. 1234-1, avec un plafond légal de six mois de ce salaire. Le seuil est apprécié au terme effectif, préavis inclus ; la première année n'est pas soustraite du calcul une fois le seuil atteint. L'indemnité conventionnelle ou contractuelle plus favorable, les salaires, congés acquis, indemnités de préavis et réparations d'une illégalité restent à leur champ propre. Les indemnités spéciales conservent leur régime, notamment le doublement, le salaire de référence et l'absence de seuil d'ancienneté propres à l'inaptitude professionnelle ; le seuil et le plafond de l'indemnité ordinaire ne les limitent pas.</p>
<p>Pour les contrats conclus avant cette entrée en vigueur et pour les contrats de droit public qui ne relèvent pas du contrat unique, la durée du contrat reste, selon le cas, conforme au second alinéa du I de l'article R. 4623-25-3 ou égale à la durée du stage prescrit en application de l'article R. 4111-17 du code de la santé publique, dans la limite de trois ans. Le non-renouvellement à l'issue d'une période d'engagement est notifié avec un préavis de deux mois ; les démissions sont présentées avec le même préavis. Les contrats antérieurs conservent leur ancienneté, leurs créances et leurs droits acquis, y compris les primes et indemnités propres à leur régime. Lorsqu'une indemnité ordinaire relève de l'article L. 1234-9, ses composantes antérieure et nouvelle sont calculées selon cet article, sans remise à zéro ni double compte d'une même période. Une conversion convenue en contrat unique conserve toute l'ancienneté et les créances acquises. Ces dispositions n'autorisent ni nouveau CDD de droit privé ni renouvellement après cette entrée en vigueur.</p>"""
article(3, xml,
    "Réforme maintenue : dissocier la période de stage de la durée du nouvel emploi privé et remplacer le préavis spécial de deux mois par quinze jours calendaires des deux côtés. Cette seconde passe corrige le point de départ, fixé au lendemain de la notification pertinente, et le prorata limité aux mois complets. Le barème ordinaire est coordonné sans créer un second régime local. La qualification et le stage sont nécessaires à la sécurité médicale ; les retirer davantage ne serait pas justifié. L'emploi indéterminé crée en contrepartie une obligation de continuité jusqu'à une rupture régulière, explicitement recensée.",
    "R4623-25-3 lu en entier : le second alinéa de son I traite du temps plein/partiel, pas d'une durée chiffrée ; incohérence du renvoi source signalée, sans inventer un terme absent. Son II cite R4111-18 CSP, alors que la source présente cite R4111-17 : concordance externe à vérifier, textes CSP non fournis et non réputés réécrits. L1234-1/3/9, R1234-1/4 sont lus dans leurs versions officielles et proposées : quinze jours dès le lendemain, seuil au terme effectif avec préavis, 0,20 mois sur toute l'ancienneté, mois complets, plafond légal de six mois. La réserve de L1234-9 conserve notamment son exception de faute grave et les avantages conventionnels/contractuels ; elle n'efface pas les indemnités spéciales. L1226-14/16/20 officiels lus : doublement, salaire propre et protections professionnelles restent à coordonner sans seuil ordinaire. Nouveaux renvois de précision L1234-3/9 et R1234-1 sont tous fournis dans reference-targets.json. Modèles contractuels extérieurs et références CSP restent à coordonner, sans extension au statut public.",
    'mixed',
    "La source entière liait durée d'emploi et stage et prévoyait deux mois de préavis. Le texte distingue désormais l'emploi indéterminé de la période pédagogique et réduit le préavis individuel à quinze jours calendaires dans le nouveau champ privé. Il reprend le barème général proposé sans revendiquer une économie locale d'indemnité non mesurée.",
    "La réduction de préavis ne s'applique ni aux anciens contrats non convertis ni au droit public. Deux mois ne sont pas convertis artificiellement en soixante jours. L'obligation de poursuivre un emploi indéterminé hors stage subsiste ; aucun solde net de coût ou de complexité n'est établi.",
    "Une charge de continuité de l'emploi jusqu'à une rupture régulière remplace le terme du stage pour les recrutements privés nouveaux. Le barème et la notification écrite coordonnent les règles communes, sans dossier local supplémentaire. Aucun registre, agrément ou justificatif nouveau n'est créé ; les procédures protectrices restent requises.")
reduction(3,
    "Préavis spécial de deux mois pour les démissions dans les nouveaux emplois privés, remplacé par le préavis individuel commun de quinze jours calendaires.",
    "Terme automatique du nouvel emploi privé fixé par la durée du stage, distinct désormais de la période pédagogique dont la limite de trois ans demeure.")
effect(3, 'deadline_reduced', 'contrat-unique-preavis-quinze-jours',
       "Substituer le préavis individuel commun au préavis spécial de deux mois pour les nouveaux contrats privés.",
       "Deux mois pour notifier le non-renouvellement au terme d'une période d'engagement et pour présenter une démission.",
       "Quinze jours calendaires des deux côtés pour la rupture individuelle du nouveau contrat privé, à compter du lendemain de la notification pertinente ; aucune assimilation des deux mois à soixante jours.",
       'calendar_days', "Candidats à l'autorisation d'exercice recrutés sous nouveau contrat unique de droit privé et leurs employeurs.",
       "Nouveaux recrutements dès l'entrée en vigueur ; deux mois conservés pour anciens contrats et statuts publics ; dispenses favorables du salarié et procédures spéciales préservées.",
       "Notification écrite selon le régime commun, sans nouveau dépôt ; la procédure d'autorisation protectrice n'est pas absorbée.",
       "Le non-renouvellement du contrat à l'issue d'une période d'engagement est notifié avec un préavis de deux mois. Les démissions sont présentées avec le même préavis.",
       "La rupture individuelle du nouveau contrat de droit privé est soumise à un préavis de quinze jours calendaires pour l'employeur comme pour le salarié, sous réserve des dispenses favorables ouvertes à ce dernier.")
effect(3, 'coordination', 'contrat-unique-emploi-indetermine',
       "Appliquer le contrat unique au candidat médecin, sans confondre stage et emploi ; continuité d'emploi et rupture régulière remplacent le terme automatique.",
       "La durée du contrat correspond à la durée du stage dans la limite de trois ans ou au renvoi du second alinéa du I de R4623-25-3, dont l'objet est ambigu.",
       "Le nouvel emploi privé est indéterminé ; le stage conserve sa durée prescrite et la limite de trois ans ; sa fin n'éteint pas l'emploi.",
       'regime', "Candidats médecins recrutés dans le nouveau champ privé.",
       "Anciennes durées et droits conservés ; pas de renouvellement de CDD après réforme ; contrats publics distincts.",
       "Obligation de continuité de l'emploi et coût d'une éventuelle rupture régulière ; aucune autorisation de stage ou d'exercice supprimée, aucun remplacement déclaratif créé.",
       "La durée du contrat de travail est, selon le cas, soit conforme aux dispositions du second alinéa du I de l'article R. 4623-25-3, soit égale à la durée du stage prescrit en application de l'article R. 4111-17 du code de la santé publique, dans la limite de trois ans.",
       "La fin des fonctions requises ou du stage ne met pas automatiquement fin à l'emploi et ne dispense pas de l'autorisation nécessaire à l'exercice de la médecine.")


article(4, sources[4]['previous_draft']['proposed_xml'],
    "Coordination nécessaire du suivi de santé avec les anciens CDD et les nouveaux contrats uniques. La seconde passe conserve le brouillon : les dispenses de visites répétées sont déjà prévues par R4624-15/27 et doivent rester ouvertes à toute situation future éligible, y compris après conversion. Supprimer l'égalité de suivi ou ses conditions sanitaires retirerait une protection essentielle ; cet article ne contient pas de formalité autonome supplémentaire à supprimer.",
    "R4624-15 et R4624-27 officiels lus intégralement : cinq ans, ou trois ans pour le travailleur relevant de R4624-17, et deux ans pour l'aptitude ; emploi identique, risques d'exposition équivalents, dernière attestation/avis détenu et absence de mesure ou d'inaptitude durant les périodes prévues restent des conditions cumulatives. Ni conversion ni durée indéterminée ne ferment ces dispenses, mais elles ne suppriment pas le suivi périodique ou l'examen de risques nouveaux. Les références sont déjà dans la source, même si elles ne figurent pas dans le paquet des cibles du contrat unique. La réserve publique conserve le champ initial sans étendre le contrat privé. Préavis, ancienneté et indemnité ne déterminent pas la périodicité médicale.",
    'coordination_only',
    "Les chapitres de suivi et leurs dispenses sont conservés, avec une transition explicite pour le CDD et le contrat unique. La comparaison à la source entière ne démontre aucune nouvelle suppression de visite : les dispenses favorables existent déjà et sont préservées.",
    "La conservation des dispenses dépend de toutes leurs conditions sanitaires ; aucun nombre de visites évitées ou coût n'est établi. Les contrats publics ne sont pas convertis.",
    "Aucune charge nouvelle n'est identifiée : ni visite de conversion, ni attestation nouvelle, ni fréquence accrue. Les pièces et conditions sont celles des deux dispenses existantes.")
effect(4, 'coordination', 'contrat-unique-suivi-sante',
       "Conserver la même protection et les dispenses existantes après le passage au contrat unique.",
       "Les CDD ont un suivi équivalent aux CDI et bénéficient notamment de R4624-15 et R4624-27.",
       "Ancien CDD et futur contrat unique conservent suivi et dispenses conditionnelles ; une conversion ne ferme pas ces dispenses.",
       'regime', "Travailleurs relevant du présent suivi médical, y compris les futures embauches privées éligibles.",
       "Nouveaux contrats uniques et anciens CDD ; champ public conservé sans conversion.",
       "Aucune nouvelle visite ou pièce ; pas de nouvelle réduction comptée pour une dispense existante.",
       "notamment des dispositions prévues aux articles R. 4624-15 et R. 4624-27.",
       "Une conversion convenue d'un ancien contrat en contrat unique ne suffit pas, à elle seule, à rendre ces dispenses inapplicables.")


article(5, sources[5]['previous_draft']['proposed_xml'],
    "Conservation de la suppression effective, déjà acquise au brouillon, de l'information administrative distincte du directeur régional sur la nomination ou le recrutement. Aucun envoi de remplacement n'est créé. La seconde passe ne retire pas davantage les informations aux représentants, l'avis conforme de rupture ou l'avis médical : leur fonction d'indépendance est propre et ne se confond pas avec l'envoi supprimé. La transition privée/publique reste entière.",
    "R4626-9/10/11 lus en entier : qualification, dispense de diplôme des médecins en fonction au 8 septembre 1985 et modèle contractuel restent autonomes. L952-21 éducation et L6152-1 1° CSP sont des réserves de régimes disciplinaires publics : textes extérieurs non fournis, ni réécrits ni attribués artificiellement au contrat privé. La dénomination comité technique d'établissement/CSE est conservée selon la source ; l'actualisation des instances hospitalières nécessite une coordination extérieure documentée, sans suppression de représentation par inférence. L'avis de l'inspecteur est conforme et intervient après consultation et avis médical. La suppression de l'envoi vise aussi les informations restant à transmettre à l'entrée en vigueur, sans annuler les envois déjà faits. Aucune nouvelle cible de renvoi dans le texte.",
    'material_reduction',
    "La source entière exigeait trois destinataires pour l'information de nomination ou recrutement ; la proposition retire le destinataire administratif régional. Les représentants et le contrôle conforme de rupture subsistent, avec la distinction des anciens CDD privés et des contrats publics.",
    "Un envoi distinct est supprimé, sans prétendre supprimer les autres informations légalement autonomes ni l'autorisation de rupture. Le gain administratif n'est pas chiffré et les statuts publics restent distincts.",
    "Aucune charge nouvelle n'est identifiée : pas de déclaration de remplacement, destinataire supplémentaire ou dossier local. Le maintien des avis et informations aux représentants reprend les obligations protectrices déjà présentes.")
reduction(5,
    "Information administrative distincte du directeur régional sur chaque nomination ou recrutement du médecin du travail, y compris les envois encore pendants à la réforme.")
effect(5, 'obligation_removed', 'medecins-notification-recrutement-region',
       "Supprimer l'envoi administratif régional relatif à la nomination ou au recrutement.",
       "Information du comité technique d'établissement, du CSE et du directeur régional sur la nomination ou le recrutement.",
       "Information des représentants conservée ; aucun envoi administratif distinct au directeur régional sur ce fondement.",
       'legal_duty', "Établissements relevant du chapitre VI et médecins du travail recrutés ou nommés.",
       "À l'entrée en vigueur, y compris les informations non encore transmises ; envois déjà faits valables, protections de rupture conservées.",
       "Aucun envoi ou registre de remplacement ; avis conforme et réserves disciplinaires publics restent applicables.",
       "de la nomination ou du recrutement du médecin du travail.",
       "l'information distincte du directeur régional des entreprises, de la concurrence, de la consommation, du travail et de l'emploi sur la nomination ou le recrutement n'est plus requise, y compris pour les informations non encore transmises à cette date.")


article(6, sources[6]['previous_draft']['proposed_xml'],
    "Maintien de l'extension explicite du plancher horaire d'activité partielle aux intérimaires employés à durée indéterminée. Sans cette coordination, la généralisation du contrat unique ferait disparaître la garantie pour les futurs intérimaires. La seconde passe ne supprime ni plafonds ni périodes de référence : ils fixent le montant du droit et évitent la surindemnisation, sans créer ici de dossier redondant. L'extension peut accroître l'obligation de paiement de l'employeur : elle n'est pas présentée comme une baisse de prélèvement.",
    "Source et proposition de L1251-58-1 lues ; L1251-58-2/3 officiels lus en entier pour la garantie mensuelle et les intermissions. L'extension s'applique aux heures chômées futures, y compris des CDI intérimaires existants ; les heures antérieures gardent leur régime, sans double paiement d'une même heure. Maintien de 60 % du brut, plafond de rémunération à 4,5 SMIC, moyenne des douze mois civils ou des mois travaillés, formation à 100 % du net, plafond spécifique d'allocation apprentissage/professionnalisation et plafond du net habituel. La rémunération inférieure au SMIC demeure le plafond horaire du dernier alinéa. L3121-27/28/29/41/44 et L3123-1 officiels lus : quarante heures seulement dans le nouveau champ hebdomadaire ; aucun relèvement automatique des 1 607 heures, règles plurihebdomadaires ou contrats antérieurs. Le 1er janvier 2023 de la note est historique. L'articulation financière avec les allocations et la garantie mensuelle doit être coordonnée sans annoncer une neutralité budgétaire.",
    'mixed',
    "L'exclusion des CDI intérimaires du plancher horaire est retirée par rapport à la source entière ; les autres taux, assiettes et limites sont conservés. Cette extension d'un droit peut relever l'indemnité due par l'employeur ; aucun allègement net de son coût ni baisse d'impôt n'est démontré.",
    "La garantie est bornée par la rémunération horaire habituelle, les cotisations obligatoires et l'exception du dernier alinéa pour le salaire inférieur au SMIC. Financement et effet net sur les employeurs ne sont pas chiffrés ; les intermissions ne deviennent pas automatiquement des heures chômées indemnisables.",
    "Charge de paiement potentiellement accrue pour les employeurs de CDI intérimaires désormais inclus dans le plancher. Aucun registre, déclaration ou justificatif supplémentaire n'est créé ; le coût net après allocation publique et garantie mensuelle reste à établir.")
reduction(6,
    "Exclusion des salariés en CDI intérimaire de la garantie de taux horaire d'indemnité d'activité partielle au moins égal au SMIC, sous réserve du salaire habituel inférieur.")
effect(6, 'relief_extended', 'activite-partielle-plancher-interim',
       "Étendre aux intérimaires en CDI le plancher horaire, avec l'obligation corrélative de paiement patronal et les limites existantes.",
       "Pour les intérimaires hors L1251-58-1 et les salariés à temps partiel, plancher au SMIC horaire ; les CDI intérimaires sont exclus. Indemnité ordinaire de 60 % du brut de référence plafonné à 4,5 SMIC.",
       "Même plancher ouvert aussi aux CDI intérimaires pour les heures éligibles futures ; salaire horaire inférieur au SMIC substitué au plancher et plafond du net habituel conservés. Taux et assiette ordinaires inchangés.",
       'euro', "Intérimaires en CDI existant ou sous futur contrat unique et leurs employeurs.",
       "Heures chômées à compter de l'entrée en vigueur ; antérieures régies par leur droit ; conditions générales d'activité partielle et non-double-paiement maintenues.",
       "Indemnité éventuellement plus élevée à la charge de l'employeur, sans chiffrage du reste après allocation ni suppression de la garantie mensuelle ; aucun nouveau dossier prévu ici.",
       "à l'exception de ceux mentionnés à l'article L. 1251-58-1",
       "y compris ceux mentionnés à l'article L. 1251-58-1")


xml = """<p>Pour l'application du 1° du I de l'article R. 5131-20, sont des ressources intégralement déductibles du montant forfaitaire de l'allocation :</p>
<p>1° Les allocations versées aux travailleurs privés d'emploi en application du titre II du livre IV de la cinquième partie du présent code ainsi que de l'article L. 1233-68 ;</p>
<p>2° Abrogé.</p>
<p>3° Abrogé.</p>
<p>Les revenus tirés des stages de formation professionnelle et la rémunération perçue dans le cadre d'un parcours de formation dispensé par les écoles de la deuxième chance mentionnées à l'article L. 214-14 du code de l'éducation sont des ressources partiellement déductibles de l'allocation. Ils sont pris en compte, avec les ressources mentionnées à l'article R. 5131-22, selon le seuil et le coefficient de dégressivité prévus au 2° du I de l'article R. 5131-20 et à l'article D. 5131-23 ; ils ne sont pas déduits une seconde fois au titre du 1° du I de l'article R. 5131-20.</p>
<p>Ce régime de déduction partielle s'applique au calcul de l'allocation pour les périodes commençant à compter de l'entrée en vigueur de la loi portant cette simplification, y compris pour les parcours déjà engagés. Les droits, créances et recours afférents aux périodes antérieures restent régis par leurs dispositions antérieures. Les autres conditions d'attribution de l'allocation, les ressources intégralement cumulables prévues au II de l'article R. 5131-20 et les exceptions de cumul de l'article R. 5131-24 demeurent applicables. Aucun justificatif supplémentaire n'est exigé du seul fait du passage à la déduction partielle.</p>"""
article(7, xml,
    "Coupe supplémentaire par rapport au brouillon à droit constant : suppression de la déduction intégrale des revenus de formation professionnelle et d'école de la deuxième chance, qui amputait l'allocation euro pour euro. Ces revenus suivent le barème existant de déduction partielle, sans nouveau taux ni cumul intégral inventé. Les allocations chômage et de sécurisation professionnelle restent déductibles intégralement, afin de coordonner les revenus de remplacement. Les trois numéros sont conservés et les futurs parcours éligibles bénéficient de l'allègement.",
    "R5131-20/R5131-22/D5131-23/R5131-25 et L5131-6 officiels lus intégralement. Le nouveau texte rattache expressément les deux revenus de formation au 2° du I de R5131-20 : sans cette précision leur retrait de la liste pourrait conduire à un cumul intégral par le II, non décidé ici. Le seuil de 300 € et la formule de coefficient fondée sur 80 % du SMIC restent ceux de D5131-23, sans nouveau pourcentage. Coordination à porter dans le 1° du I de R5131-20 et l'introduction de R5131-22 pour reconnaître cette catégorie supplémentaire : ces articles hors lot ne sont pas présentés comme réécrits. Le texte spécial donne déjà l'assiette de calcul, sans nouvelle pièce. Le CEJ est un accompagnement, pas un contrat d'emploi ; L1233-68 est visé pour l'allocation CSP, non pour son préavis ni sa contribution patronale. La note du 1er mars 2022 est historique. Nouveaux renvois R5131-22/D5131-23 et subdivisions I/II de R5131-20 non fournis dans reference-targets.json, contrôlés dans le corpus public local ; absence de vue empreintée spécifique signalée. L214-14 éducation reste une référence extérieure maintenue, sans contenu inventé.",
    'material_reduction',
    "Par rapport à la source officielle entière, deux catégories de revenus de formation passent de l'imputation intégrale au régime partiel déjà utilisé pour l'activité. La règle de calcul est effectivement plus favorable dans le barème existant ; elle ne supprime pas l'allocation de formation ni les conditions du CEJ.",
    "Le gain individuel dépend du revenu, du forfait d'allocation, des autres ressources et des conditions d'éligibilité. Les revenus de remplacement du 1° restent intégralement déduits. Le coût public et le solde national ne sont pas chiffrés ; les coordinations de R5131-20/22 hors lot restent nécessaires.",
    "Aucune charge nouvelle n'est identifiée : revenus et pièces étaient déjà nécessaires au calcul, le seuil et le coefficient sont existants et aucun justificatif supplémentaire n'est exigé. La dépense publique peut augmenter avec le droit conservé, sans rendement ou compensation présumés.")
answers[7]['benefit_review'] = "La déduction de cet article est une imputation sur l'allocation CEJ, pas une exonération fiscale. Au 1°, les allocations chômage et CSP ne sont ni supprimées ni diminuées ; leur imputation intégrale demeure et leurs conditions d'accès propres ne changent pas. Les revenus de stage du 2° et la rémunération des écoles de la deuxième chance du 3° restent versés selon leurs régimes et bénéficient désormais du cumul partiel existant, pour les futurs parcours éligibles et ceux en cours sur les périodes futures. L'exhaustivité de la liste des revenus intégralement déduits n'est pas élargie : cumul intégral des autres ressources de R5131-20 II, exceptions de R5131-24, insaisissabilité et exonérations du CEJ prévues à L5131-6 restent applicables. Aucun avantage antérieur, y compris sur les périodes passées, n'est fermé par ce traitement plus favorable."
reduction(7,
    "Déduction intégrale euro pour euro des revenus de stages de formation professionnelle sur l'allocation du contrat d'engagement jeune.",
    "Déduction intégrale euro pour euro de la rémunération des parcours des écoles de la deuxième chance sur l'allocation du contrat d'engagement jeune.")
effect(7, 'relief_extended', 'cej-cumul-revenus-formation',
       "Ouvrir aux deux revenus de formation le cumul partiel du CEJ en supprimant leur imputation intégrale.",
       "Revenus de stage et rémunérations d'école de la deuxième chance entièrement déductibles de l'allocation CEJ, euro pour euro, sans franchise propre dans cet article.",
       "Ces deux revenus sont additionnés aux ressources partiellement déductibles : seuil et coefficient existants de R5131-20 I 2° et D5131-23, sans double imputation ; aucune modification du montant de la rémunération de formation.",
       'euro', "Jeunes éligibles au CEJ percevant des revenus de formation professionnelle ou d'école de la deuxième chance.",
       "Périodes commençant dès l'entrée en vigueur, parcours futurs et déjà engagés ; périodes antérieures et autres conditions de droit préservées.",
       "Aucune pièce nouvelle ni autre prélèvement ; calcul selon un barème existant, coût public supplémentaire éventuel non chiffré.",
       "2° Les revenus tirés de stages de formation professionnelle ;",
       "Les revenus tirés des stages de formation professionnelle et la rémunération perçue dans le cadre d'un parcours de formation dispensé par les écoles de la deuxième chance mentionnées à l'article L. 214-14 du code de l'éducation sont des ressources partiellement déductibles de l'allocation.")


article(8, sources[8]['previous_draft']['proposed_xml'],
    "Conservation de la réforme favorable déjà acquise : retrait de la suspension automatique du CEJ au seul motif d'un salaire d'insertion ou de CUI ; application du barème ordinaire d'activité. La seconde passe maintient les I, II et les cinq autres cas du III : coordination avec RSA, prime d'activité et dispositifs de volontariat, avec toutes leurs exceptions favorables. Aucune autorisation, transmission ou pièce redondante autonome ne subsiste dans cet article à supprimer davantage.",
    "R5131-20/R5131-22/D5131-23 et L5131-6 officiels lus ; salaire soumis au cumul partiel existant, non au cumul intégral. Maintien des exceptions pour personnes à charge, de la prime relative à l'activité antérieure au premier mois et des références exactes des cinq volontariats. Le 6° reste numéroté comme abrogé. Les quatre cibles L5132-5/11-1/15-1/6 sont lues en entier, sources et propositions : parcours, missions et aides ne donnent pas un terme au nouvel emploi, les anciens contrats gardent leur transition. Le CUI de L5134-19-3 désigne CAE/CIE, pas le contrat unique général ; sa source officielle a été lue dans le corpus. La réforme du seul support contractuel ne rétablit pas le non-cumul. R5131-25 et les circuits de versement hors lot doivent éviter la suspension sur l'ancien 6°, sans prétendre leur régime de pièces abrogé. Les renvois R5131-20/22 ajoutés au brouillon ne sont pas des cibles fournies dans reference-targets.json ; leurs subdivisions ont été contrôlées dans le corpus local. Aucun texte extérieur militaire ou de service national n'est prétendu réécrit.",
    'material_reduction',
    "La source entière suspendait l'allocation à raison de cinq supports d'emploi d'insertion visés ensemble au III 6°. La suppression de ce seul 6° ouvre le calcul partiel ordinaire des salaires, pour emplois antérieurs et futurs ; les autres non-cumuls et leurs exceptions sont maintenus.",
    "Le montant peut rester nul selon les ressources et les autres règles du CEJ ; aucune allocation perpétuelle ni cumul intégral n'est garanti. Les conditions RSA, prime d'activité et volontariat demeurent. Coût public et effet net de complexité ne sont pas chiffrés.",
    "Aucune charge nouvelle n'est identifiée : le calcul de ressources et le barème sont déjà utilisés pour les revenus d'activité. Aucun dossier, registre, attestation ou taux de remplacement n'est créé, ni CDD réintroduit.")
reduction(8,
    "Non-cumul et suspension automatique de l'allocation CEJ à raison des rémunérations des emplois d'insertion et du contrat unique d'insertion visés au III 6°.")
effect(8, 'relief_extended', 'cej-cumul-salaires-insertion',
       "Supprimer la suspension propre aux salaires d'insertion et de CUI et leur appliquer le régime partiel ordinaire.",
       "Ces rémunérations ne sont pas cumulables avec le CEJ ; son versement est suspendu pendant leur perception selon le III 6°.",
       "Ces salaires relèvent du seuil et de la dégressivité ordinaires des revenus d'activité, sans suspension due au seul support d'insertion ; les autres exclusions et exceptions demeurent.",
       'euro', "Jeunes encore éligibles au CEJ salariés d'EI, AI, ACI, ETTI ou en CUI.",
       "Ressources des périodes futures dès l'entrée en vigueur, anciens contrats et contrats uniques ; pas de remboursement rétroactif général pour périodes passées.",
       "Aucune formalité ou contribution de remplacement ; conditions de ressources et d'éligibilité existantes maintenues, dépense supplémentaire non chiffrée.",
       "6° La rémunération perçue dans le cadre d'un contrat à durée déterminée conclu en application des dispositions des articles L. 5132-5, L. 5132-11-1 et L. 5132-15-1 du présent code, d'un contrat de mission mentionné à l'article L. 5132-6 ou d'un contrat unique d'insertion mentionné à l'article L. 5134-19-3.",
       "Elles ne justifient plus, à elles seules, la suspension automatique de l'allocation, que l'emploi relève d'un ancien contrat ou du nouveau contrat unique à durée indéterminée.")


article(9, sources[9]['previous_draft']['proposed_xml'],
    "Conservation de la coordination de l'aide au poste avec les futurs contrats uniques éligibles, sans nouveau conventionnement du seul fait de la réforme. Le socle, la modulation et ses trois critères, les postes conventionnés et le régime pénitentiaire restent entiers. Après réexamen, supprimer la convention de financement ou la modulation risquerait de retirer les aides ou leurs possibilités favorables ; aucun dossier ou délai minimal distinct n'est imposé ici. Le retrait de la référence CDD ne compte pas comme une seconde suppression du CDD.",
    "L5132-1/2/3 et L5132-5 officiels lus, ainsi que la proposition complète de L5132-5 et la cible R5132-8. Le parcours spécifique de L5132-5 conserve ses durées et prolongations favorables, mais ne fixe plus le terme du contrat. Le socle et le modulé restent soumis à l'occupation et au contingent de postes, non garantis pour toute la vie du CDI. Les conventions existantes ouvrent l'accès futur éligible sans être refaites au seul motif du contrat unique. Contrat d'emploi pénitentiaire distinct, non assimilé au contrat de travail privé. La note source renvoie aux V et VI de l'article 2 du décret 2021-1128 ; le texte complet de ces dispositions extérieures n'est pas fourni et leur transition historique reste à vérifier pour les dossiers concernés. Arrêtés de montants et versement à coordonner ; aucune hausse, nouveau taux ou économie chiffrée affirmée.",
    'coordination_only',
    "La source entière réserve la branche salariale aux CDD ; la proposition conserve l'aide pour les futurs emplois éligibles sous contrat unique. Le montant et ses trois critères restent identiques. C'est une coordination protectrice de l'aide, pas une nouvelle mesure indépendante de fusion ou de baisse de prélèvement.",
    "L'aide reste limitée aux postes et parcours éligibles conventionnés ; elle ne finance pas automatiquement toute la durée d'un CDI. Les contrats pénitentiaires restent distincts ; les arrêtés extérieurs et transitions historiques ne sont pas réputés réécrits.",
    "Aucune charge nouvelle autonome n'est identifiée : même convention de financement, mêmes critères de modulation, pas de reconventionnement ni nouveau justificatif du seul fait de la substitution du contrat. La continuité de l'emploi découle du contrat unique coordonné ailleurs.")
reduction(9,
    "Condition de recours au CDD pour bénéficier de la branche salariale de l'aide au poste, supprimée afin de conserver l'aide aux futurs contrats uniques éligibles.")
effect(9, 'coordination', 'contrat-unique-aides-insertion',
       "Conserver l'aide au poste dans le nouveau support d'emploi, sans deuxième convention due au seul changement de contrat.",
       "Branche salariale de l'aide ouverte pour l'embauche en CDD, dans les limites des postes conventionnés ; branche pénitentiaire séparée.",
       "Même aide ouverte aux futurs contrats uniques éligibles et aux anciens CDD, sans réduction tenant à la durée indéterminée ; mêmes limites et branche pénitentiaire.",
       'regime', "Entreprises d'insertion, salariés en insertion éligibles et personnes détenues dans leur régime distinct.",
       "Futurs recrutements dès réforme et conventions en cours ; droits acquis préservés, durée d'aide distincte de l'emploi.",
       "Aucun nouveau conventionnement du seul fait du contrat unique ; condition d'emploi indéterminé issue du régime général, pas une nouvelle baisse comptée ici.",
       "dans la limite du nombre de postes d'insertion fixé par la convention, à une aide financière.",
       "Les conventions en cours et les droits déjà constitués restent applicables ; aucun nouveau conventionnement n'est exigé du seul fait de la substitution du contrat unique au CDD.")


article(10, sources[10]['previous_draft']['proposed_xml'],
    "Coordination de l'aide et de ses arrêtés avec le contrat unique, en maintenant leur application favorable aux futurs recrutements éligibles sans interruption de versement. La seconde passe conserve prorata, socle, maximum de modulation et revalorisation annuelle : supprimer l'un d'eux pourrait retirer un avantage, tandis qu'inventer une indexation automatique chiffrée dépasserait la source. L'arrêté conjoint est une compétence de fixation des montants, pas un agrément imposé à chaque employeur.",
    "Maintien du temps plein, du prorata d'occupation, de la part modulée plafonnée par un pourcentage du socle, et des deux branches salariés/détenus. Aucun pourcentage de modulation n'est créé. Le 1er janvier 2015 reste l'origine historique de la revalorisation annuelle selon le SMIC, sans revalorisation rétroactive nouvelle. Concordance avec R5132-7 du présent lot : même éligibilité future et absence de rupture des paiements par la substitution contractuelle. Les arrêtés extérieurs fixant les montants et versements doivent être coordonnés, mais les avantages ne sont pas suspendus dans cette attente. Les V/VI de l'article 2 du décret 2021-1128, signalés dans la note, ne sont pas fournis intégralement ; leur portée historique reste à vérifier, sans modifier le régime pénitentiaire par inférence. Aucune nouvelle cible de renvoi introduite dans le texte.",
    'coordination_only',
    "Par rapport à la source entière, seule la restriction de support CDD est coordonnée pour empêcher la perte de l'aide dans le contrat unique. Prorata, montants à fixer et revalorisation subsistent ; la même mesure d'aide est suivie sous la clé commune à R5132-7, sans seconde réduction revendiquée.",
    "La proposition ne modifie ni les montants fixés par arrêté, ni l'éligibilité du parcours, ni le contingent de postes. Aucun allègement financier net ou pourcentage de modulation n'est déduit de cette coordination.",
    "Aucune charge nouvelle n'est identifiée : mêmes règles d'occupation et de calcul, mêmes ministres compétents, aucune nouvelle demande ou condition d'accès en attendant l'actualisation des arrêtés. Le régime pénitentiaire demeure distinct.")
reduction(10,
    "Restriction de la fixation et du versement de l'aide salariale aux salariés recrutés sous CDD, retirée par coordination avec l'ouverture aux futurs contrats uniques éligibles.")
effect(10, 'coordination', 'contrat-unique-aides-insertion',
       "Assurer la continuité des montants et de leur revalorisation pour les aides au poste coordonnées à R5132-7.",
       "Les arrêtés distinguent les salariés en insertion sous CDD et les personnes détenues ; prorata d'occupation et revalorisation annuelle au SMIC.",
       "Même calcul et mêmes montants applicables aux anciens CDD et aux futurs contrats uniques de même objet sans exclusion liée à la durée indéterminée ; branche pénitentiaire préservée.",
       'regime', "Entreprises d'insertion bénéficiaires des aides et futurs salariés éligibles.",
       "Futures embauches privées à compter de la réforme ; continuité des versements et revalorisations malgré les arrêtés non encore modifiés ; origine historique de 2015 conservée.",
       "Aucune nouvelle demande ni attestation ; aucune seconde réduction comptée pour la coordination d'une même aide.",
       "pour les salariés en insertion recrutés sous contrat de travail à durée déterminée",
       "Elle n'interrompt ni les versements ni la revalorisation en l'absence de modification des arrêtés ou conventions existants.")


article(11, sources[11]['previous_draft']['proposed_xml'],
    "Abrogation entière du cadrage préalable supplémentaire des immersions dans la convention générale d'insertion, avec ses quatre rubriques. La seconde passe conserve cette suppression acquise : prescription, accord de l'employeur et convention propre à chaque période sont déjà encadrés par des fondements autonomes. Les protections ne justifient donc pas de maintenir le doublon de programmation ; aucune formalité équivalente ne le remplace.",
    "L5135-1 à L5135-6, D5135-2/3/4 et D5132-10-2/4 officiels lus en entier ; L5135-7 et L5132-5 lus dans leurs sources et propositions. Maintien des trois objets légaux, prescription et convention individuelle, statut et indemnisation antérieurs, retour au poste, santé/sécurité et interdiction du travail de substitution. D5135-3 garde son mois de date à date, son renouvellement unique et les limites de deux conventions et soixante jours sur douze mois ; aucun de ces plafonds n'est un terme d'emploi. D5132-10-2, hors lot, doit être coordonné pour que sa réserve de sous-section ne rétablisse pas le cadrage supprimé ; D5132-10-4 garde sa transmission distincte à l'ASP, non abrogée ici. Les renvois explicites L5135-1 à 6 et D5132-10-2, déjà présents dans le brouillon mais non fournis comme cibles empreintées, sont vérifiés dans le corpus local ; aucune vue empreintée n'est inventée. Arrêté du modèle de convention individuelle extérieur au lot non réputé réécrit. Contrats uniques futurs et anciens contrats éligibles gardent l'accès aux immersions.",
    'material_reduction',
    "La source entière subordonne la possibilité d'immersion à sa programmation dans la convention générale et à quatre rubriques. Cette couche préalable est entièrement supprimée pour les périodes futures ; le cadre individuel autonome et les engagements d'accompagnement déjà valables restent applicables.",
    "La convention individuelle, la prescription, l'accord patronal et la transmission ASP fondée sur D5132-10-4 subsistent. L'abrogation n'est pas une suppression de toutes les procédures d'immersion ; aucun coût total ni solde national n'est chiffré.",
    "Aucune charge nouvelle n'est identifiée : aucun avenant, agrément, dépôt ou déclaration de remplacement. Les règles individuelles maintenues existaient avant l'abrogation ; les engagements autonomes et créances antérieures restent protégés.")
answers[11].update(change_type='full_repeal',
    repeal_policy_id='editorial_direction_2026_10_19',
    repeal_scope="Suppression du cadrage préalable des immersions dans la convention générale d'insertion et de ses quatre rubriques obligatoires, pour les périodes organisées après l'entrée en vigueur, sans supprimer leur convention individuelle ni les protections autonomes.")
effect(11, 'obligation_removed', 'insertion-cadrage-general-immersions',
       "Retirer le préalable de programmation des immersions dans la convention générale, avec les quatre rubriques associées, en une seule mesure.",
       "La convention générale doit prévoir la possibilité d'immersion et préciser nombre prévisionnel, structures d'accueil, accompagnement et objets.",
       "Aucune programmation ni ces quatre rubriques exigées dans la convention générale ; prescription et convention individuelle restent régies par leurs bases autonomes.",
       'legal_duty', "Entreprises d'insertion et salariés éligibles aux périodes de mise en situation.",
       "Périodes organisées dès l'entrée en vigueur ; conventions et périodes déjà engagées, engagements autonomes, droits et créances antérieurs préservés.",
       "Aucun avenant, agrément ou dépôt remplaçant le cadrage général ; accord, convention individuelle et protection du bénéficiaire maintenus.",
       "Dans ce cas, la convention précise :",
       "Aucun avenant, agrément ou dépôt de remplacement n'est exigé sur ce fondement.")
