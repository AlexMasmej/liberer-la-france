import json
import re
import html
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
by_number = {a['number']: a for a in sources}
answers = {}

def plain(value):
    return html.unescape(re.sub(r'<[^>]*>', '', value or ''))

def article(number, reason, notes, classification, assessment, limitations, burdens,
            proposed=None, retained=False):
    s = by_number[number]
    a = {k: s[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}
    a.update(proposed_xml=None if retained else (proposed or s['previous_draft']['proposed_xml']),
             reason=reason, review_notes=notes,
             status='retained_unchanged' if retained else 'rewrite_draft',
             substantive_impact=dict(version=1, classification=classification,
                                     assessment=assessment, scope_limitations=limitations,
                                     new_burdens_review=burdens, effects=[]))
    answers[number] = a
    return a

def repeal(number, scope):
    answers[number].update(change_type='full_repeal',
                           repeal_policy_id='editorial_direction_2026_10_19',
                           repeal_scope=scope)

def reduction(number, provisions):
    answers[number].update(change_type='normative_reduction',
                           reform_policy_id='editorial_direction_2026_10_19',
                           removed_provisions=provisions)

def effect(number, kind, measure_id, description, before, after, unit, population,
           transition, replacements, source_quote, proposed_quote):
    answers[number]['substantive_impact']['effects'].append(dict(
        kind=kind, measure_id=measure_id, description=description, before=before,
        after=after, unit=unit, affected_population=population,
        conditions_and_transition=transition,
        replacement_or_new_burdens=replacements,
        source_quote=source_quote, proposed_quote=proposed_quote))

article('L1251-33',
    "Coordination de fond du contrat unique : abrogation prospective du catalogue de dispenses d'indemnité de fin de mission, dont le 3° est déjà abrogé. Les dispenses restent applicables aux contrats anciens et à leurs échéances futures. Le brouillon antérieur avait déjà réalisé cette abrogation ; aucune coupe supplémentaire n'est justifiée dans ses garanties transitoires. La source ne crée pas l'indemnité : sa disparition pour les nouveaux emplois relève de L1251-32 et de l'exclusion déjà applicable au CDI intérimaire, non d'une seconde baisse ici.",
    "Lecture complète des 1°, 2°, 3° et 4°. Le 1° exige un accord étendu de branche ou un texte d'entreprise ou d'établissement pour la mission du 3° de L1251-6 ; le 2° vise les activités assimilées de L1251-57 ; le 4° vise initiative du salarié, faute grave ou force majeure. Ces dispenses continuent dans leur champ ancien même si la créance est exigible après la réforme. Pour l'avenir, L1251-32 exclut l'indemnité à la seule fin de mission sous contrat unique, et L1251-58-4 exclut déjà L1251-33 pour les missions en CDI : aucune dispense favorable n'est retirée pendant que la même indemnité subsiste. Les formations et assimilations de L1251-57 restent accessibles aux futurs salariés. Coordonner L1251-58-5 en retirant les substitutions devenues inutiles dans les articles abrogés, sans toucher aux autres lettres de mission. Les indemnités ordinaires et spéciales restent distinctes ; aucune faute grave n'efface automatiquement les autres créances.",
    'coordination_only',
    "La source officielle entière énumère des dispenses et non une charge autonome. L'abrogation pour l'avenir accompagne l'absence d'indemnité de fin de mission dans l'emploi indéterminé ; elle ne supprime ici ni une taxe ni une seconde indemnité. Les quatre subdivisions historiques sont conservées par le droit transitoire, sans nouveau contrat à terme.",
    "La suppression de l'indemnité générale est portée par L1251-32, lu dans le corpus, et n'est pas comptée une seconde fois. Aucun montant net de coût d'emploi ou effet national n'est établi. Les contrats antérieurs, indemnités plus favorables et recours restent hors de la suppression prospective.",
    "Aucune charge nouvelle propre à cet article n'est identifiée : pas d'attestation, déclaration ou condition de remplacement. Le contrat unique coordonné implique la continuité de l'emploi et ses garanties d'intermission ; cette contrepartie ne constitue pas une baisse démontrée du coût total de l'intérim.")
repeal('L1251-33', "Suppression prospective du catalogue spécial de dispenses d'indemnité de fin de mission devenu sans objet pour les nouveaux emplois à durée indéterminée ; maintien des dispenses, créances et recours des contrats antérieurs.")
effect('L1251-33', 'coordination', 'contrat-unique-sans-nouveau-cdd',
       "Coordonner les exceptions de fin de mission avec la continuité de l'emploi, sans compter une suppression d'indemnité supplémentaire.",
       "Dispenses de l'indemnité de fin de mission pour les cas des 1°, 2° et 4° ; le CDI intérimaire est déjà exclu de cet article par L1251-58-4.",
       "Catalogue abrogé pour l'avenir ; exceptions anciennes maintenues pour les anciens contrats, y compris à échéance ultérieure. La seule fin de mission n'est pas la fin de l'emploi nouveau.",
       'regime', 'Salariés temporaires et entreprises de travail temporaire.',
       "À l'entrée en vigueur de la loi instituant le contrat unique ; aucun nouveau CDD ni renouvellement à durée déterminée. Droits conventionnels et contractuels plus favorables conservés.",
       "Aucune formalité de remplacement ; garanties mensuelles, congés et ancienneté de l'emploi indéterminé restent à leur champ propre.",
       "L'indemnité de fin de mission n'est pas due :",
       "Pour les contrats de mission conclus avant cette date, les dispenses d'indemnité de fin de mission demeurent celles prévues par les dispositions antérieurement applicables, y compris lorsque l'indemnité devient exigible après cette date.")

article('L1251-34',
    "Coordination de fond, sans suppression de la protection radiologique : l'offre porte sur des affectations au sein d'un emploi indéterminé, et non sur de nouveaux contrats à terme. Le CDI intérimaire bénéficie déjà de la substitution de la lettre de mission par L1251-58-5 ; cette coordination n'est donc pas une nouvelle réduction pour cette population. Après réexamen du brouillon, aucune coupe supplémentaire ne se justifie dans le délai maximal, les quatre garanties matérielles ou la dérogation de durée : ils assurent la continuité protectrice après une exposition dépassant la valeur rapportée à la mission. Aucun seuil dosimétrique n'est inventé.",
    "Le renvoi au deuxième alinéa de L1251-26 porte exactement sur qualification professionnelle, rémunération, horaire de travail et temps de transport ; il ne fait pas dépendre L1251-34 de la rupture anticipée ou de la faute visées au premier alinéa de cette cible. Les trois jours sont ouvrables et constituent un maximum après la fin de mission, non un préavis de rupture. L1251-12 concerne désormais l'affectation ; L1251-12-1, proposé à l'abrogation, reste mentionné dans son seul champ historique. La comparaison reste l'exposition constatée rapportée à la durée totale mission initiale et affectations suivantes, non à une durée indéterminée d'emploi. La note de 2017 vise les contrats conclus après la publication de l'ordonnance et reste distincte de la réforme proposée. Coordonner L1251-58-5 et les dispositions autonomes de radioprotection ; aucune conformité européenne n'est présumée. Les valeurs limites, restrictions médicales et responsabilités pour une exposition déjà subie ne sont pas effacées.",
    'coordination_only',
    "La source entière exige une proposition protectrice après dépassement de la limite rapportée à la durée du contrat. Le texte conserve délai de trois jours ouvrables, durée correctrice, dérogation aux plafonds et éléments essentiels du poste. Il remplace le support d'emploi à terme pour les nouveaux recrutements ; le CDI intérimaire utilisait déjà des lettres de mission. Aucun allègement de radioprotection n'est revendiqué.",
    "Les normes autonomes de radioprotection et le droit de l'Union doivent rester coordonnés ; aucune dose nouvelle ni dilution d'une exposition passée n'est admise. Le gain administratif supplémentaire n'est pas établi pour les salariés déjà en CDI. Le solde des coûts de l'emploi et de prévention n'est pas chiffré.",
    "Aucune nouvelle collecte dosimétrique, autorisation ou attestation n'est créée : la règle utilise le constat d'exposition déjà prévu. La continuité en CDI et l'affectation protectrice sont les contreparties coordonnées ; les trois jours et les quatre garanties ne sont pas nouveaux.")
reduction('L1251-34', ["Suppression, pour les propositions faites après l'entrée en vigueur du contrat unique, du recours à une succession de nouveaux contrats de travail à terme pour assurer la protection dosimétrique ; les affectations et garanties matérielles demeurent."])
answers['L1251-34']['benefit_review'] = (
    "La dérogation aux durées maximales de L1251-12 et L1251-12-1 est un avantage protecteur : elle reste ouverte pour les futures affectations éligibles et dans le champ historique des anciens plafonds. L'offre d'une ou plusieurs affectations au plus tard trois jours ouvrables après la mission précédente est conservée. Les quatre garanties du deuxième alinéa de L1251-26, qualification, rémunération, horaire et temps de transport, restent entières. La durée doit toujours ramener la comparaison à la valeur limite annuelle rapportée à la durée totale ; elle ne rend pas licite une exposition déjà excessive. Les anciens contrats gardent leurs droits et recours, même si la proposition intervient après la réforme, mais tout nouvel emploi est indéterminé. Le CDI intérimaire conserve rémunération mensuelle garantie, congés et ancienneté des intermissions. Il n'existe dans cette source ni exonération fiscale ni prélèvement supprimé.")
effect('L1251-34','coordination','contrat-unique-sans-nouveau-cdd',
       "Maintenir l'offre protectrice par des affectations sans nouveaux emplois à terme.",
       "En cas d'exposition dépassant la valeur annuelle rapportée à la durée du contrat de mission : un ou plusieurs contrats dans les trois jours ouvrables, avec la durée correctrice et les garanties de L1251-26, alinéa 2 ; lettre de mission déjà substituée pour le CDI intérimaire.",
       "Même déclencheur, délai maximal et garanties, au moyen d'affectations dans un emploi à durée indéterminée ; droits des contrats antérieurs préservés.",
       'regime','Salariés temporaires exposés aux rayonnements ionisants et entreprises de travail temporaire.',
       "Les contrats anciens gardent leur protection ; après l'entrée en vigueur, aucune proposition d'emploi ne peut être un nouveau CDD ou renouvellement à terme.",
       "Pas de formalité de remplacement ni réduction du suivi médical ; continuité de l'emploi et garanties d'intermission maintenues.",
       "un ou plusieurs contrats prenant effet dans un délai maximum de trois jours ouvrables après l'expiration du contrat précédent",
       "Ces propositions ne nécessitent pas la conclusion d'un nouveau contrat de travail lorsque le salarié est déjà employé à durée indéterminée.")
effect('L1251-34','relief_preserved','interim-protection-rayonnements',
       "Conserver la dérogation favorable de durée nécessaire à la proposition protectrice, y compris pour les futures missions éligibles.",
       "Dérogation aux limites de durée de L1251-12 et L1251-12-1 afin de rapporter l'exposition à la durée totale des contrats concernés.",
       "Dérogation aux limites de mission conservées, avec L1251-12-1 limité à son champ historique ; rapport à la durée totale des missions, jamais à la durée indéterminée de l'emploi.",
       'legal_duty','Salariés temporaires remplissant le critère dosimétrique, anciens et futurs.',
       "Maintien pour les futures situations recevables, sans nouveau contrat à terme et sans effacer une exposition déjà subie.",
       "Aucune autorisation, attestation ou nouvelle valeur limite ; garanties de santé et garanties matérielles inchangées.",
       "Par dérogation aux dispositions des articles L. 1251-12 et L. 1251-12-1 relatives à la durée maximale du contrat de mission",
       "Par dérogation aux limites de durée de mission prévues à l'article L. 1251-12 et, dans son champ historique, à l'article L. 1251-12-1")

article('L1251-35',
    "Réforme de fond déjà engagée par le brouillon et conservée après nouvel examen : supprimer le plafond de renouvellements sur ce fondement et l'obligation de les stipuler ou de soumettre un avenant avant le terme. La poursuite d'un emploi indéterminé ne nécessite aucun renouvellement. La suppression n'atteint ni l'information sur l'affectation, ni le consentement à une modification essentielle, ni les limites autonomes de durée ou de recours temporaire. Aucun allègement supplémentaire n'est justifié dans ces garanties. L'interdiction coordonnée des nouveaux CDD est une restriction nouvelle de choix contractuel, non une économie nette démontrée.",
    "L1251-12 permet encore une durée conventionnelle de l'affectation et L1251-5 interdit une occupation durable de l'emploi permanent de l'utilisateur. Ces règles ne rétablissent pas le plafond de nombre de renouvellements du présent article. L1251-35-1 et L1251-40 sont coordonnés dans ce lot ; L1251-58-5 doit retirer la substitution devenue sans objet pour L1251-35. Vérifier aussi les renvois répressifs au nombre de renouvellements avant adoption, sans les présenter comme réécrits ici. Les conditions anciennes restent invocables pour le terme en cours, mais ne permettent pas un renouvellement à terme prenant effet après la réforme. La note de 2017 conserve son champ historique. Aucun préavis ne court du seul fait du non-renouvellement d'une mission.",
    'mixed',
    "Par rapport à la source officielle entière, disparition du dispositif de plafonnement par branche et du support contractuel obligatoire de renouvellement pour les nouvelles missions en emploi indéterminé. En contrepartie coordonnée, les nouveaux emplois à terme et leurs renouvellements sont interdits. Les règles autonomes protégeant l'affectation temporaire demeurent ; aucun solde net de coût n'est établi.",
    "Pas d'effet sur les droits, créances et recours du terme en cours des contrats antérieurs. Les durées conventionnelles de mission restent opposables dans leur champ. Le coût économique de la continuité en CDI et les coordinations répressives restantes ne sont pas chiffrés.",
    "Pas de nouveau registre, déclaration ou avenant de remplacement. La continuation obligatoire de l'emploi indéterminé et l'interdiction des nouveaux CDD restreignent le choix contractuel dans la réforme commune ; cette contrepartie est recensée et exclut de prétendre à une réduction nette de toutes les charges.")
repeal('L1251-35', "Suppression pour les nouvelles missions du plafonnement du nombre de renouvellements sur ce fondement et de leur stipulation ou avenant obligatoire avant le terme ; conservation du régime du terme en cours des anciens contrats.")
effect('L1251-35','obligation_removed','interim-suppression-renouvellements',
       "Supprimer le plafonnement et la formalisation préalable des renouvellements fondés sur L1251-35, sans second décompte au titre de son texte supplétif.",
       "Nombre maximal fixé par accord de branche étendu ; conditions stipulées ou avenant soumis au salarié avant le terme, y compris pour les lettres de mission via L1251-58-5.",
       "Pour les missions nouvelles en emploi indéterminé, ni plafond du nombre ni stipulation ou avenant de renouvellement sur ce fondement ; information et accord sur les modifications essentielles subsistent.",
       'legal_duty','Entreprises de travail temporaire, entreprises utilisatrices et salariés en nouvelles missions.',
       "Missions convenues à compter de l'entrée en vigueur du contrat unique ; terme en cours des contrats anciens et droits correspondants préservés, sans nouveau renouvellement à terme.",
       "Aucune formalité équivalente créée ; les garanties autonomes de mission et la continuité de l'emploi demeurent.",
       "Les conditions de renouvellement sont stipulées dans le contrat ou font l'objet d'un avenant soumis au salarié avant le terme initialement prévu.",
       "Pour les missions convenues à compter de cette date dans le cadre d'un emploi à durée indéterminée, les limitations du nombre de renouvellements et l'obligation d'un avenant de renouvellement fondées sur le seul présent article cessent de s'appliquer.")
effect('L1251-35','coordination','contrat-unique-sans-nouveau-cdd',
       "Recenser la restriction coordonnée des nouveaux emplois à terme et la continuation de l'emploi, sans compter une seconde mesure de fusion.",
       "Le renouvellement d'un contrat de mission à terme est possible dans les conditions légales ou conventionnelles.",
       "Tout nouvel emploi est indéterminé ; aucun nouveau contrat de mission à durée déterminée ni renouvellement à durée déterminée.",
       'regime','Nouveaux recrutements privés par les entreprises de travail temporaire.',
       "À compter de l'entrée en vigueur ; terme en cours des contrats antérieurs et conversion convenue avec ancienneté conservée.",
       "Obligation coordonnée de poursuivre l'emploi après la mission avec garanties d'intermission ; pas de gain net chiffré.",
       "La convention ou l'accord de branche étendu de l'entreprise utilisatrice peut fixer le nombre maximal de renouvellements possibles pour un contrat de mission.",
       "À compter de cette date, aucun nouveau contrat de mission à durée déterminée ni renouvellement à durée déterminée ne peut être conclu.")

article('L1251-35-1',
    "Abrogation prospective du régime supplétif de deux renouvellements et de sa formalisation, en exécution de la suppression du même dispositif dans L1251-35. Le brouillon réalisait déjà cette coupe et est conservé sur le fond. Aucun motif essentiel ne justifie de recréer un plafond de nombre dans un emploi qui se poursuit ; à l'inverse les limites autonomes de durée d'affectation et le consentement du salarié ne peuvent être retirés comme de simples doublons. La conservation du calcul historique ne permet aucun nouveau renouvellement d'emploi à terme.",
    "Le plafond supplétif est bien de deux renouvellements, avec cumul de la durée initiale et des renouvellements sous L1251-12 ou L1251-12-1 ; ce cumul reste applicable au terme en cours des contrats anciens lorsqu'il les régissait. L1251-35 est abrogé dans le même lot et L1251-12-1 est proposé à l'abrogation dans la vue fournie ; L1251-12 ne conserve qu'une limite conventionnelle de mission. L1251-40 est rectifié ici pour ne pas rétablir le plafond comme cause de requalification future. Les renvois répressifs ou réglementaires non assignés restent à coordonner. La note de 2017 n'est pas une date d'entrée en vigueur de la loi proposée.",
    'coordination_only',
    "La source entière est le régime supplétif du dispositif de renouvellement : deux fois, durée cumulée plafonnée et stipulation ou avenant avant terme. Son abrogation met en œuvre la même suppression que L1251-35, sous la même clé de mesure ; elle n'est pas comptée comme une seconde formalité supprimée.",
    "Les règles des anciens contrats restent invocables pour le terme en cours et leurs litiges. L'abrogation n'établit pas de baisse supplémentaire pour une mission ne nécessitant déjà aucun renouvellement. Les plafonds conventionnels autonomes de durée ne disparaissent pas.",
    "Aucun délai de remplacement ni nouveau support n'est imposé. L'information sur l'affectation et le consentement en cas de modification essentielle préexistent ; le choix obligatoire du CDI est coordonné avec la mesure commune et n'est pas présenté comme sans coût.")
repeal('L1251-35-1', "Suppression prospective du plafond supplétif de deux renouvellements et de sa stipulation ou de son avenant avant terme, sans maintien d'un emploi à terme nouveau ; protection du terme en cours des contrats antérieurs.")
effect('L1251-35-1','coordination','interim-suppression-renouvellements',
       "Retirer la branche supplétive de la même règle de renouvellement supprimée par L1251-35.",
       "À défaut d'accord, deux renouvellements au plus, durée totale initiale et renouvellements comprise sous les limites applicables ; stipulation ou avenant avant terme.",
       "Ni plafond supplétif de deux renouvellements ni formalité de renouvellement pour les nouvelles missions en emploi indéterminé ; limites autonomes d'affectation maintenues.",
       'legal_duty',"Salariés et entreprises relevant de l'ancien régime supplétif de renouvellement.",
       "Missions nouvelles après entrée en vigueur ; protection du terme en cours, droits et recours anciens, sans nouveau renouvellement à durée déterminée.",
       "Pas de formalité équivalente ; contrat unique et garanties matérielles à leur champ propre. Pas de seconde réduction comptée.",
       "le contrat de mission est renouvelable deux fois pour une durée déterminée",
       "Pour les missions convenues à compter de cette date dans le cadre d'un emploi à durée indéterminée, le plafond supplétif de deux renouvellements et l'obligation de stipulation ou d'avenant de renouvellement prévue par le présent article cessent de s'appliquer.")

article('L1251-36',
    "Réforme de fond : retirer le fondement du délai de carence sur le même poste et de son calcul par la branche, sans délai ni formalité de remplacement. Le brouillon avait déjà supprimé ce régime ; aucune coupe supplémentaire n'est nécessaire dans la transition protectrice des faits anciens. L1251-58-4 exclut déjà L1251-36 pour le CDI intérimaire : la coupe ne doit donc pas être comptée comme un nouveau gain pour ces missions. L'interdiction autonome de pourvoir durablement un poste permanent de l'utilisateur reste nécessaire et ne limite pas la durée de l'emploi auprès de l'agence.",
    "Les jours d'ouverture et la durée incluant les renouvellements ne restent utiles que pour les faits anciens. L1251-36-1 est abrogé avec la même transition. L1251-37 et L1251-37-1, lus en entier dans le corpus, doivent être coordonnés : leurs dispenses restent utilisables pour l'appréciation des faits anciens, et la suppression générale pour l'avenir ne doit pas devenir une permission de nouveau CDD. L1255-9, également lu, punit encore le manquement à ces règles de 3 750 euros et, en récidive, six mois et 7 500 euros ; son fondement doit être retiré pour les faits futurs et la loi répressive plus douce respectée pour les sanctions non définitives. Ces textes non assignés ne sont pas déclarés réécrits. La note de 2017 reste historique.",
    'material_reduction',
    "La source officielle impose une carence entre contrats sur le même poste, calculée en jours d'ouverture et susceptible de modalités de branche. Ce fondement et les effets futurs des délais en cours disparaissent. Le champ ancien à terme est fermé, tandis que le CDI intérimaire était déjà exclu par L1251-58-4 : aucun gain additionnel n'est attribué à cette population déjà dispensée.",
    "Les dommages et actions attachés aux faits anciens sont conservés sous réserve de la loi répressive plus douce. Les coordinations de L1251-37, L1251-37-1 et L1255-9 ne sont pas réalisées dans ce lot. Aucun nombre de journées ou coût total effectivement épargné n'est établi.",
    "Aucun nouveau délai, formulaire, agrément ou relevé ne remplace la carence. Le contrôle préexistant du caractère temporaire de l'affectation et les garanties d'intermission restent applicables ; ils ne constituent pas une carence reconstituée.")
repeal('L1251-36', "Suppression de tout effet futur du délai de carence sur le même poste et de l'habilitation de branche à le calculer sur ce fondement, y compris des délais en cours ; droits et recours sur faits antérieurs réservés.")
effect('L1251-36','obligation_removed','interim-suppression-carence',
       "Supprimer le fondement légal de la carence, sans l'attribuer comme nouveau gain aux CDI intérimaires déjà exclus.",
       "Pour les successions entrant dans L1251-36, attente sur le même poste calculée d'après la durée de mission et ses renouvellements en jours d'ouverture, selon les modalités de branche ou supplétives. L1251-58-4 exclut déjà le CDI intérimaire.",
       "Aucun délai sur ce fondement pour une embauche ou affectation en emploi indéterminé après la réforme ; fin des effets correspondants des délais en cours.",
       'legal_duty','Entreprises utilisatrices et entreprises de travail temporaire, dans le champ de la carence supprimée.',
       "À compter de l'entrée en vigueur du contrat unique, y compris pour les délais en cours ; faits anciens, dispenses et recours conservés avec réserve des sanctions plus douces.",
       "Aucun délai ou déclaration substitutif ; le CDI et l'interdiction autonome d'affectation permanente restent distincts.",
       "avant l'expiration d'un délai de carence calculé en fonction de la durée du contrat de mission incluant, le cas échéant, son ou ses renouvellements.",
       "À compter de cette date, aucun délai de carence fondé sur le présent article ou sur les stipulations prises pour son application ne fait obstacle à une embauche à durée indéterminée ou à une affectation temporaire dans le cadre d'un emploi à durée indéterminée.")

article('L1251-36-1',
    "Abrogation du barème supplétif de carence en coordination avec la suppression du fondement dans L1251-36 : tiers de la durée à partir de quatorze jours, moitié en dessous et décompte en jours d'ouverture. Le brouillon réalisait déjà la suppression ; les fractions ne sont pas réduites ni remplacées. Les calculs incluant les renouvellements et dispenses ne survivent que pour l'examen des faits anciens. Aucune coupe supplémentaire ne se justifie dans les droits et recours transitoires ou les garanties autonomes d'emploi.",
    "Les seuils source sont quatorze jours ou plus pour un tiers et moins de quatorze pour la moitié, avec renouvellements compris dans la durée de référence. Ce ne sont ni des jours calendaires de préavis ni des durées minimales d'emploi. Le délai en cours cesse d'empêcher les nouvelles affectations en CDI. L1251-36 est abrogé dans le même lot ; L1251-37, L1251-37-1 et L1255-9 lus dans le corpus nécessitent leur propre coordination. Le CDI intérimaire est déjà dispensé du fondement de carence par L1251-58-4, de sorte que la suppression supplétive n'est pas une seconde baisse. La note de 2017 garde son seul champ historique.",
    'coordination_only',
    "Le barème de la source entière cesse de s'appliquer avec le délai principal de L1251-36. Le retrait du tiers, de la moitié, du seuil de quatorze jours et du décompte d'ouverture constitue l'exécution de la même mesure, sans réduction supplémentaire comptée séparément.",
    "Pas de gain additionnel démontré pour les missions déjà en CDI ; les droits sur faits anciens restent réservés. Les sanctions et dispenses des articles non assignés nécessitent coordination, sans chiffrage du nombre réel de jours évités.",
    "Aucune condition ou donnée nouvelle n'est demandée : le calcul disparaît sans barème substitutif. La continuité de l'emploi et la licéité de l'affectation restent régies par leurs règles propres, sans recréer un intervalle minimal entre missions.")
repeal('L1251-36-1', "Suppression du barème supplétif de carence d'un tiers ou d'une moitié, du seuil de quatorze jours et du décompte en jours d'ouverture pour l'avenir, y compris les délais en cours ; réserve des faits antérieurs.")
effect('L1251-36-1','coordination','interim-suppression-carence',
       "Retirer le calcul supplétif de la carence déjà supprimée dans L1251-36, sans compter une seconde suppression de délai.",
       "À défaut d'accord : un tiers de la durée initiale et renouvellements si cette durée est de quatorze jours ou plus ; moitié en dessous ; délai apprécié en jours d'ouverture.",
       "Aucun tiers, moitié, seuil de quatorze jours ou décompte d'ouverture sur ce fondement pour les embauches et affectations futures en emploi indéterminé.",
       'legal_duty','Entreprises et salariés relevant du barème supplétif de succession de missions.',
       "Entrée en vigueur du contrat unique, y compris les délais restant à courir ; calcul ancien conservé uniquement pour l'examen des faits antérieurs et leurs recours.",
       "Aucun délai substitutif, aucun nouveau CDD ; la même mesure est enregistrée sous la clé commune de la carence.",
       "Au tiers de la durée du contrat de mission venu à expiration si la durée du contrat incluant, le cas échéant, son ou ses renouvellements, est de quatorze jours ou plus",
       "Le délai supplétif de carence d'un tiers ou de la moitié de la durée du contrat de mission, le seuil de quatorze jours qui en détermine la fraction et leur décompte en jours d'ouverture ne s'appliquent plus à compter de cette date.")

article('L1251-38',
    "Maintien intégral nécessaire après lecture de la source et du brouillon. Les deux alinéas attribuent des avantages et non une formalité : reprise des missions des trois derniers mois pour l'ancienneté et déduction de cette durée de l'essai. Le terme « mission » couvre déjà les missions en CDI intérimaire et le contrat de recrutement n'est pas limité au CDD. Les précisions ajoutées par le brouillon ne justifient donc pas une nouvelle réécriture à droit constant. La règle source reste applicable aux recrutements futurs en contrat unique sans fermer aucun droit.",
    "Fenêtre exacte : trois mois précédant le recrutement, non trois mois d'ancienneté minimale et non toute l'ancienneté auprès de l'agence. La durée retenue est également déduite de l'essai, sans créer ni renouveler un essai. L1221-19 lu dans le corpus prévoit trois mois sans renouvellement pour le nouveau contrat ; cette déduction reste opposable. L1251-58-4 soumet déjà les missions en CDI à L1251-38. Le seuil de L1234-9 doit intégrer l'ancienneté reconnue ici et s'apprécier au terme effectif, préavis inclus, sans double compte ; le salaire de référence conserve sa fenêtre propre. Aucun renvoi numéroté de la source n'est rendu orphelin. Ni enregistrement, agrément, déclaration ni justificatif périodique n'est imposé par cet article. La non-reprise du texte stylistique du brouillon ne retire pas un avantage nouveau : ses deux droits matériels figurent intégralement dans la source conservée.",
    'retained_necessary',
    "La source entière conserve l'ancienneté correspondant aux missions des trois mois précédant le recrutement et réduit d'autant l'essai. Elle s'applique déjà aux missions exécutées dans un emploi indéterminé : aucune coupe ni extension nouvelle n'est démontrée ou revendiquée. Retirer l'un des deux alinéas supprimerait un avantage utile pour les futurs recrutements.",
    "Le maintien ne reprend pas toute l'ancienneté antérieure à la fenêtre de trois mois et ne règle pas les autres garanties de transfert d'emploi. Aucune réduction de prélèvement ou économie nette nationale n'est attribuée à cet article ; les paramètres de rupture relèvent de leurs textes propres.",
    "Aucune charge nouvelle n'est identifiée : le texte intégral reste celui de la source, sans dossier, collecte, délai d'attente ou condition supplémentaire. Le calcul d'ancienneté et la déduction d'essai sont maintenus pour préserver les droits des salariés.",
    retained=True)

article('L1251-39',
    "Maintien intégral nécessaire. La reconnaissance du CDI auprès de l'utilisateur en cas de poursuite irrégulière de mission, le départ de l'ancienneté au premier jour et la déduction d'essai protègent l'identification de l'employeur et les droits du salarié. Ces règles s'appliquent déjà aux missions en CDI intérimaire par L1251-58-4 et ne requièrent pas un nouvel emploi à terme. Le brouillon ajoutait surtout leur explicitation pour le contrat unique ; aucune nouvelle reformulation à droit constant ni suppression de ce recours n'est justifiée.",
    "La source est reproduite intégralement depuis sa version officielle, sans modification de sa conjonction « ou ». L'articulation préexistante des absences de contrat direct et de nouveau contrat de mise à disposition peut prêter à discussion : contrat direct et mise à disposition sont des supports différents ; le lot ne tranche pas silencieusement cette lecture ni n'ajoute une cause de requalification. Le point de départ est le premier jour de la mission, distinct de la fenêtre de trois mois de L1251-38. Une fin régulière d'affectation ne rompt pas le CDI auprès de l'agence. La reconnaissance d'un lien avec l'utilisateur n'efface pas les responsabilités propres de l'agence ni les créances antérieures. La règle n'impose aucun agrément, déclaration ou pièce spéciale en double. Le préavis individuel et l'indemnité ordinaire ne sont déclenchés que par une rupture dans leur champ propre ; les recours et réparations restent distincts.",
    'retained_necessary',
    "La source entière maintient une protection contre la poursuite de travail sans support régulier, avec ancienneté au premier jour et réduction de l'essai. Elle couvre déjà les missions exécutées dans un emploi à durée indéterminée ; aucun allègement supplémentaire n'est démontré. Abroger cette protection ouvrirait une perte de droits sans supprimer un doublon administratif identifié.",
    "La difficulté préexistante de formulation avec « ou » est signalée et reste à examiner ; les responsabilités réciproques des deux entreprises ne sont pas refondues. Le maintien ne constitue ni une validation de jurisprudence ni une estimation du solde économique des recours.",
    "Aucune charge nouvelle n'est identifiée puisque la norme source reste entière : pas de nouveau contrat, registre ou déclaration imposé par ce maintien. La présomption de CDI et les droits correspondants sont des garanties existantes et non des formalités de remplacement.",
    retained=True)

xml40 = """<p>Lorsqu'une entreprise utilisatrice a recours à un salarié d'une entreprise de travail temporaire en méconnaissance des articles L. 1251-5 à L. 1251-7, L. 1251-10, L. 1251-11 et L. 1251-30, et des stipulations des conventions ou accords de branche conclus en application de l'article L. 1251-12, le salarié peut faire valoir auprès de cette entreprise les droits d'un contrat de travail à durée indéterminée prenant effet au premier jour de sa mission. Ces renvois s'appliquent aux règles d'affectation qui demeurent en vigueur dans leur champ temporel propre.</p>
<p>La méconnaissance de l'obligation de transmission au salarié, dans le délai fixé par l'article L. 1251-17, du contrat de mission ou, pour un emploi à durée indéterminée, de la lettre de mission, ne peut, à elle seule, entraîner la requalification de l'emploi en contrat à durée indéterminée ni la reconnaissance de ces droits auprès de l'entreprise utilisatrice. Elle ouvre droit, pour le salarié, à une indemnité à la charge de son employeur, dont le montant ne peut dépasser un mois de salaire. Un écrit déjà régulièrement transmis n'a pas à être envoyé une seconde fois ; une nouvelle affectation n'exige pas un nouveau contrat de travail.</p>
<p>Pour les missions convenues à compter de l'entrée en vigueur de la loi instituant le contrat de travail unique dans le cadre d'un emploi à durée indéterminée, les plafonds légaux de durée ou de renouvellement supprimés des articles L. 1251-12-1, L. 1251-35 et L. 1251-35-1 ne peuvent fonder une requalification ni une demande de reconnaissance de droits contre l'entreprise utilisatrice. Les règles maintenues d'affectation ne fixent pas de terme à l'emploi et ne rétablissent pas ces plafonds.</p>
<p>Le salarié employé sous contrat unique conserve le droit de faire valoir les droits du premier alinéa auprès de l'entreprise utilisatrice lorsque les règles d'affectation applicables sont méconnues. Un terme illicitement stipulé dans son emploi auprès de l'entreprise de travail temporaire ne le prive pas des droits du contrat unique auprès de celle-ci et ne décharge pas l'entreprise utilisatrice de ses propres manquements. La seule fin de mission ne rompt pas cet emploi.</p>
<p>Pour les contrats et les faits auxquels demeurent applicables les dispositions antérieures, le salarié conserve les droits d'un contrat à durée indéterminée prenant effet au premier jour de la mission en cas de méconnaissance des articles L. 1251-5 à L. 1251-7, L. 1251-10, L. 1251-11, L. 1251-12-1, L. 1251-30 et L. 1251-35-1, et des stipulations des conventions ou accords de branche conclus en application des articles L. 1251-12 et L. 1251-35, dans leur champ temporel propre. Les règles maintenues pour le terme en cours d'un contrat antérieur restent invocables, même si leur violation intervient après l'entrée en vigueur précitée. Les renouvellements à durée déterminée valablement conclus avant cette entrée en vigueur conservent leurs effets ; aucun nouveau contrat ni renouvellement à durée déterminée ne peut être conclu ou décidé à compter de cette date. Une simple faculté de renouvellement non encore exercée ne vaut pas renouvellement déjà conclu.</p>
<p>Les droits, créances et recours antérieurs, y compris ceux relatifs à la transmission du contrat, sont conservés. Le champ historique des dispositions issues de l'ordonnance n° 2017-1387 du 22 septembre 2017, applicables aux licenciements prononcés et aux contrats conclus après sa publication, reste distinct de l'entrée en vigueur de la présente réforme. L'indemnité du deuxième alinéa et les réparations d'une illégalité sont indépendantes de l'indemnité ordinaire de rupture et ne sont pas subordonnées à un an d'ancienneté.</p>"""
article('L1251-40',
    "Coordination normative des suppressions de durée et de renouvellement, sans nouvelle réduction autonome : les fondements devenus historiques sont retirés de l'énumération générale et conservés explicitement pour les anciens contrats concernés. Le brouillon maintenait encore toute l'énumération en tête avec une réserve temporelle ; la présente rédaction distingue la règle maintenue et son champ historique sans rétablir les plafonds supprimés. Le plafond indemnitaire d'un mois pour retard de transmission et le recours contre l'utilisateur sont maintenus : ils protègent l'information et sanctionnent une illégalité. La dispense de double envoi coordonne L1251-17, sans prétendre que la source L1251-40 exigeait déjà deux transmissions.",
    "Les alinéas source de recours et d'indemnité restent en première et deuxième positions. Vérification des cibles entières, notamment L1251-7 : ses cinq cas et ses avantages restent ouverts aux situations futures, sans rétablir son ancien minimum d'un mois ni l'habilitation supprimée au 1° dans sa proposition. L1251-10 lu dans le corpus conserve conflit collectif, travaux dangereux avec dérogation exceptionnelle, et médecin du travail ; leur autorisation sectorielle ne devient pas une dispense de procédure de rupture. L1251-11 maintient ses cas de terme imprécis et la durée minimale de l'affectation. L1251-12 conserve la durée conventionnelle ; L1251-12-1, L1251-35 et L1251-35-1 ne sont gardés que pour leurs faits et contrats historiques. L1251-30 ne rétablit pas les anciens plafonds d'un jour pour cinq, deux jours ou dix jours pour les missions nouvelles. L1251-17 conserve deux jours ouvrables, lettre de mission et dispense de nouvel envoi ; son indemnité maximale n'est pas le minimum d'un mois de L1251-41. L1251-58-4 rend déjà les recours d'affectation applicables au CDI intérimaire. La transition précise les renouvellements définitivement conclus avant la réforme, à distinguer d'une simple clause de faculté : la source ne tranche pas cette réforme temporelle, qui doit être uniformisée avec les autres lots. Aucun nouveau renvoi numéroté n'est ajouté.",
    'coordination_only',
    "La source officielle entière protège les droits contre l'utilisateur et indemnise le seul retard de transmission dans la limite d'un mois. La proposition retire les renvois prospectifs aux plafonds abrogés et coordonne la lettre de mission sans doublon ; ces effets exécutent des mesures portées ailleurs et ne sont pas comptés comme de nouvelles obligations supprimées. Les garanties de fond et réparations sont maintenues.",
    "Les anciens fondements restent invocables dans leur champ, même si la violation du terme en cours survient après la réforme. Les responsabilités respectives ne sont pas fusionnées. La dispense de doublon n'est pas un gain indépendant démontré par le texte source de cet article ; les sanctions hors lot restent à coordonner.",
    "Aucune charge nouvelle propre à l'article n'est identifiée : pas de dossier, registre ou notification additionnelle. La transmission initiale sous deux jours et les conséquences du retard existaient déjà ; le contrat unique et les règles matérielles d'affectation gardent leur champ sans nouvelle cause autonome de requalification.",
    proposed=xml40)
reduction('L1251-40', ["Retrait, pour les missions futures en emploi indéterminé, des fondements de requalification tirés des plafonds légaux de durée et de renouvellement supprimés ; maintien explicite des anciens fondements dans leur seul champ temporel."])
effect('L1251-40','coordination','interim-suppression-renouvellements',
       "Empêcher le recours de requalification de rétablir les plafonds de renouvellement supprimés, sans seconde réduction comptée.",
       "Le premier alinéa vise L1251-35-1 et les stipulations prises en application de L1251-35 comme fondements de droits contre l'utilisateur.",
       "Ces fondements n'opèrent plus pour les nouvelles missions en emploi indéterminé ; ils restent invocables pour les contrats et faits historiques concernés.",
       'legal_duty','Salariés temporaires et entreprises utilisatrices en cas de demande de reconnaissance de droits.',
       "Missions convenues après l'entrée en vigueur du contrat unique ; protection du terme en cours et des recours des contrats anciens, sans nouvel emploi à terme.",
       "Aucune nouvelle cause de requalification, condition de saisine ou pièce ; les autres fondements demeurent.",
       "et des stipulations des conventions ou des accords de branche conclus en application des articles L. 1251-12 et L. 1251-35",
       "Pour les missions convenues à compter de l'entrée en vigueur de la loi instituant le contrat de travail unique dans le cadre d'un emploi à durée indéterminée, les plafonds légaux de durée ou de renouvellement supprimés des articles L. 1251-12-1, L. 1251-35 et L. 1251-35-1 ne peuvent fonder une requalification ni une demande de reconnaissance de droits contre l'entreprise utilisatrice.")
effect('L1251-40','coordination','interim-information-sans-double-envoi',
       "Coordonner le régime du retard avec la lettre de mission et la dispense de second envoi de L1251-17.",
       "Retard du contrat de mission transmis selon L1251-17 : pas de requalification à lui seul ; indemnité à la charge de l'employeur plafonnée à un mois de salaire.",
       "Même règle et plafond pour l'écrit de mission applicable ; pas de sanction pour l'absence d'un second envoi d'un écrit régulièrement transmis.",
       'legal_duty',"Entreprises de travail temporaire et salariés destinataires de l'écrit de mission.",
       "Application selon le champ temporel de L1251-17 ; créances et recours de transmission des contrats anciens conservés.",
       "Pas de nouvel envoi ou justificatif ; transmission initiale et indemnisation effective restent dues dans leur champ.",
       "Elle ouvre droit, pour le salarié, à une indemnité, à la charge de l'employeur, qui ne peut être supérieure à un mois de salaire.",
       "Un écrit déjà régulièrement transmis n'a pas à être envoyé une seconde fois ; une nouvelle affectation n'exige pas un nouveau contrat de travail.")

article('L1251-41',
    "Maintien intégral nécessaire de la saisine directe, du jugement dans le mois et du minimum d'indemnité d'un mois à la charge de l'utilisateur. Ils rendent effectif un recours contre une illégalité et ne constituent pas le coût ordinaire de rupture. Le CDI intérimaire est déjà visé par L1251-58-4 et la substitution de lettre de mission de L1251-58-5 inclut expressément L1251-41. La coordination protectrice ajoutée par le brouillon est donc déjà assurée par ces règles ; aucune nouvelle réécriture à droit constant n'est retenue. Retirer le minimum ou la voie directe supprimerait une protection essentielle.",
    "Les deux mois cités par la source ont des fonctions différentes : délai maximal d'un mois pour statuer après saisine du bureau de jugement, et minimum d'un mois de salaire pour l'indemnité si la demande est accueillie. Il n'existe pas de délai minimal pour agir ni de seuil d'ancienneté dans cet article. Le titre III du présent livre garde son champ temporel et ses protections distinctes ; son renvoi général ne transforme pas l'indemnité de requalification en indemnité ordinaire de rupture. Le recours ne peut rétablir un fondement de durée ou de renouvellement supprimé : L1251-40 est coordonné dans ce lot. L1251-58-5 et son adaptation au contrat unique doivent continuer de viser L1251-41 ; le texte entier de cette cible a été lu dans le corpus. Les procédures collectives et autorisations pour salariés protégés restent distinctes du préavis. Aucun renvoi source n'est incohérent ou nouvellement créé par le maintien.",
    'retained_necessary',
    "La source entière maintient l'accès direct au bureau de jugement, un délai de jugement d'un mois et un minimum indemnitaire d'un mois. Ces garanties demeurent nécessaires pour les contrats anciens et les futures missions en CDI, déjà couvertes par les adaptations de la section. Aucun allègement nouveau ni réduction du coût ordinaire de rupture n'est revendiqué.",
    "La procédure ne crée pas elle-même un fondement de requalification et ne garantit pas un résultat au fond. Le respect effectif du délai de jugement et le coût des contentieux ne sont pas évalués. Les règles de rupture et les fondements coordonnés de L1251-40 conservent leur portée propre.",
    "Aucune charge nouvelle n'est identifiée : maintien exact des deux alinéas sources sans étape de conciliation supplémentaire, dossier spécifique, délai minimal ou condition d'ancienneté. Le minimum indemnitaire existant sanctionne une illégalité et ne remplace aucune formalité supprimée.",
    retained=True)

# Le 1° de la source exige des justifications dans le contrat, non un dossier
# administratif autonome : ne pas amplifier la description de la coupe.
xml43 = by_number['L1251-43']['previous_draft']['proposed_xml'].replace(
    "Aucun dossier de justifications précises ni mention du nom et de la qualification de la personne remplacée ou à remplacer n'est imposé dans ce contrat sur le seul fondement du présent article.",
    "Les justifications précises du motif ainsi que le nom et la qualification de la personne remplacée ou à remplacer n'ont pas à figurer dans ce contrat sur le fondement du présent article. Aucun document distinct de remplacement n'est exigé à ce titre."
).replace("Les suppressions du dossier justificatif, des mentions nominatives de remplacement et de la clause spéciale",
          "Les suppressions des justifications précises à insérer au contrat, des mentions nominatives de remplacement et de la clause spéciale")
article('L1251-43',
    "Réforme de fond conservant les coupes du brouillon : retirer les justifications précises à inscrire dans chaque contrat de mise à disposition, le nom et la qualification de la personne remplacée, ainsi que la clause préalable spéciale de variation du terme et sa répétition lors d'un renouvellement. La source n'impose pas un dossier administratif autonome : cette présentation du brouillon est rectifiée. Les données contractuelles déjà exactes et accessibles sont réutilisables par référence, sans recopie. Aucune coupe supplémentaire n'est justifiée dans les mentions de sécurité, qualification du poste, lieu, horaire, équipements et comparateur salarial complet : elles protègent la santé et l'égalité de rémunération et restent nécessaires aux missions futures.",
    "Les six numéros sont conservés, le 3° portant l'abrogation dans le nouveau champ. Le 1° conserve un motif réel et contrôlable ; supprimer les mentions sur la personne remplacée ne supprime pas la qualification requise pour le poste au 4°. Le 6° maintient toutes les composantes, primes et accessoires du salaire du salarié de qualification équivalente après essai au même poste. L4154-2 conserve formation renforcée, accueil, information, liste des postes et avis du médecin/CSE, y compris les futurs salariés temporaires. L1251-30 et L1251-31 concernent la fin de l'affectation, avec leurs garanties et le report jusqu'au surlendemain du retour ; aucune nouvelle rupture d'emploi à terme. L1251-11, lu dans la vue fournie, permet déjà terme imprécis et durée minimale dans ses cas propres : leur mention au 2° n'ajoute pas une condition nouvelle. L1251-42 et L1251-58-1, lus dans le corpus, maintiennent l'écrit par salarié et par mission ; la référence documentaire ne les abroge pas. L1251-16 autorise déjà la communication sans recopie dans la lettre de mission, tout en garantissant un support accessible au salarié. L1255-10 conserve l'infraction d'absence d'écrit et l'omission du comparateur salarial, non les mentions supprimées. Vérifier les formulaires et règlements non assignés ; aucun nouveau renvoi numéroté n'est créé.",
    'material_reduction',
    "Comparée à la source officielle entière, la proposition supprime réellement des mentions et une clause obligatoire du contrat commercial, et autorise le réemploi des données contractuelles sans répétition. Elle ne supprime pas le motif, l'écrit de mise à disposition, la sécurité ni l'égalité salariale. Elle rectifie la prétention du brouillon à un « dossier » distinct que la source n'imposait pas. Aucun montant d'économie ni solde national n'est établi.",
    "Les contrats et mises à disposition déjà convenus gardent leurs mentions et leur terme en cours ; les autres obligations d'information et contrôles restent applicables. Les règles de forme de L1251-42 et les garanties de L4154-2 subsistent. Le coût de réemploi des pièces et le gain effectif ne sont pas chiffrés.",
    "Aucune charge nouvelle n'est identifiée dans l'article : le renvoi à un écrit accessible est une faculté remplaçant la recopie, sans nouveau registre ni dépôt ; le motif, la durée applicable, les données de sécurité et le comparateur préexistaient. Le contrat unique est coordonné sans être présenté comme une baisse nette du coût de l'emploi.",
    proposed=xml43)
reduction('L1251-43', [
    "Suppression de l'obligation d'assortir le motif, dans chaque contrat de mise à disposition nouveau, de justifications précises et du nom et de la qualification de la personne remplacée ou à remplacer.",
    "Suppression du 3° imposant la clause préalable spéciale d'aménagement du terme et son insertion dans l'avenant de renouvellement, pour les mises à disposition nouvelles.",
    "Suppression de la recopie des informations contractuelles exactes et à jour déjà accessibles aux parties lorsqu'elles sont incorporées par une référence écrite identifiable, sans nouveau dossier de substitution."
])
effect('L1251-43','obligation_removed','interim-mentions-contrat-allegees',
       "Retirer les justifications précises et les mentions identifiant la personne remplacée du contrat de mise à disposition.",
       "Le motif doit être assorti de justifications précises, notamment nom et qualification de la personne remplacée dans les cas de remplacement des 1°, 4° et 5° de L1251-6.",
       "Le motif demeure dans le contrat ; ses justifications précises et le nom et la qualification de la personne remplacée ne sont plus exigés sur ce fondement, sans document distinct de remplacement.",
       'legal_duty','Entreprises de travail temporaire et utilisatrices concluant de nouvelles mises à disposition.',
       "Mises à disposition convenues à compter de l'entrée en vigueur ; mentions des conventions et anciens contrats déjà conclus, créances et recours conservés.",
       "Aucun dossier ou attestation de substitution ; réalité du motif contrôlable par les voies légales existantes.",
       "Cette mention est assortie de justifications précises dont, notamment, dans les cas de remplacement prévus aux 1°, 4° et 5° de l'article L. 1251-6, le nom et la qualification de la personne remplacée ou à remplacer",
       "Les justifications précises du motif ainsi que le nom et la qualification de la personne remplacée ou à remplacer n'ont pas à figurer dans ce contrat sur le fondement du présent article. Aucun document distinct de remplacement n'est exigé à ce titre.")
effect('L1251-43','obligation_removed','interim-clause-variation-terme',
       "Supprimer la clause préalable spéciale autorisant les aménagements de terme et sa répétition dans l'avenant commercial de renouvellement.",
       "Le 3° exige, le cas échéant, une clause spéciale pour L1251-30 et L1251-31, également dans l'avenant de renouvellement du contrat de mise à disposition.",
       "Le 3° est abrogé pour les nouvelles mises à disposition ; les facultés de L1251-30 et L1251-31 restent applicables avec leurs garanties propres sans clause spéciale sur ce fondement.",
       'legal_duty','Entreprises parties aux nouvelles mises à disposition et salariés affectés.',
       "Mises à disposition nouvelles à l'entrée en vigueur ; règles antérieures maintenues pour les engagements déjà conclus et leur terme en cours.",
       "Pas de clause ni formulaire substitutif ; accord entre entreprises, information du salarié et consentement à une modification essentielle dans leur champ existant.",
       "Cette disposition s'applique également à l'avenant prévoyant le renouvellement du contrat de mise à disposition",
       "la modification de la date de fin d'affectation dans les conditions de l'article L. 1251-30 ne nécessite pas une clause spéciale préalable de variation du terme ni sa répétition dans un avenant de renouvellement sur le fondement du présent article.")
effect('L1251-43','compliance_cost_reduced','interim-reemploi-mentions-contractuelles',
       "Permettre l'incorporation des mentions déjà exactes par référence accessible au lieu de leur recopie.",
       "Le contrat établi pour chaque salarié doit comporter les mentions énumérées, sans faculté expresse d'incorporation des informations communes déjà contractualisées.",
       "Informations exactes et à jour incorporables par référence identifiant l'écrit accessible ; seules l'affectation et ses données propres ou modifiées sont individualisées.",
       'legal_duty',"Entreprises de travail temporaire et entreprises utilisatrices disposant d'informations contractuelles communes.",
       "Faculté pour les nouveaux contrats ; aucune réfection des anciens documents ni dispense d'information du salarié ou de contrôle légal.",
       "Une référence écrite est requise uniquement pour utiliser cette faculté, pas comme dépôt ou registre supplémentaire ; les parties conservent l'option d'insérer les mentions.",
       "Le contrat de mise à disposition établi pour chaque salarié comporte :",
       "Les informations exactes et à jour déjà consignées dans un écrit contractuel entre les deux entreprises peuvent être incorporées par une référence écrite qui identifie cet écrit et le rend accessible aux parties.")

article('L1251-46',
    "Réforme de fond déjà opérée dans le brouillon et maintenue après réexamen : supprimer entièrement le relevé spécial des contrats de mission et le circuit automatique de retransmission qui en dépend. Le remplacement par une transmission périodique résiduelle des seules données manquantes conserverait l'obligation supprimée et n'est pas retenu. La fonction essentielle d'établissement des droits et de contrôle demeure sur ses fondements propres, sans présumer que toutes les données de mission existent dans la DSN. Aucun allègement supplémentaire ne justifie de retirer les droits sociaux, la protection des données anciennes ou les recours.",
    "L1251-48, R1251-7, R1251-8 et R1251-9 ont été lus intégralement dans le corpus, avec leurs notes. Le 2° de L1251-48 et le relevé résiduel encore prévu dans sa proposition doivent être retirés. R1251-7 impose actuellement un relevé avant le 20 de chaque mois et par établissement utilisateur, puis sa retransmission ; sa proposition conserve encore une collecte résiduelle incompatible avec cette abrogation. R1251-8 impose modèle et rubriques : raison sociale, adresses, activité, identifiants facultatifs de l'utilisateur, identité du salarié, NIR, code postal, nationalité, qualification, dates et salaire brut ; cette collecte spéciale est supprimée, non les obligations autonomes légalement fondées. R1251-9 doit préserver information et droits sur les traitements déjà effectués, sans présenter les anciens articles 39 et 40 de la loi de 1978 comme une nouvelle habilitation : concordance de protection des données à vérifier. L5312-1 définit les missions publiques de France Travail et L5421-2 les allocations d'assurance, de solidarité et des régimes particuliers ; leur texte entier ne justifie ni fermeture de droits futurs ni extension du contrat privé au régime de l'opérateur public. L'arrêté ministériel fixant le modèle de R1251-8, non fourni et non identifié par une date dans la source, reste une coordination extérieure précise à retrouver ; aucune annexe prétendument lue ou réécrite. Aucun nouveau renvoi numéroté n'est ajouté au texte normatif.",
    'material_reduction',
    "La source officielle entière impose un relevé des contrats de mission à l'institution de l'emploi puis sa communication à l'autorité administrative. Les deux obligations spécifiques sont supprimées pour toutes transmissions restant à faire, sans relevé résiduel ni déclaration équivalente. Le bénéfice des revenus de remplacement et les contrôles sur d'autres bases restent ouverts ; aucun gain monétaire total n'est chiffré.",
    "La disponibilité de toutes les données de mission dans d'autres déclarations n'est pas démontrée ; les contrôles et droits utilisent seulement les accès et preuves légalement admissibles. L1251-48 et les règlements cités doivent être alignés, et le modèle extérieur reste à identifier. Le gain net à l'échelle des codes est inconnu.",
    "Aucune charge nouvelle n'est identifiée : ni relevé résiduel, attestation, collecte, accès administratif supplémentaire ou déclaration de remplacement. La preuve des droits et les contrôles subsistent selon les moyens légaux existants, sans conditionner les prestations à la production d'un relevé supprimé.")
repeal('L1251-46', "Suppression de l'établissement et de la transmission du relevé spécial des contrats de mission, ainsi que du circuit automatique de retransmission à l'administration, pour toutes transmissions futures même relatives à des périodes anciennes.")
effect('L1251-46','obligation_removed','interim-suppression-releve-missions',
       "Supprimer le relevé spécial et sa retransmission automatique, sans collecte périodique résiduelle.",
       "Toute entreprise de travail temporaire fournit le relevé des contrats de mission à l'institution de l'emploi ; celle-ci le communique à l'autorité administrative. Le règlement lu organise une transmission mensuelle avant le 20, par établissement.",
       "Aucun relevé spécial, complément périodique ni rattrapage exigé sur ce fondement après l'entrée en vigueur, même pour une période antérieure ; aucune déclaration de remplacement.",
       'legal_duty','Entreprises de travail temporaire et institutions destinataires du relevé spécial.',
       "Toutes transmissions restant à effectuer à l'entrée en vigueur ; relevés déjà reçus soumis aux règles de conservation et de confidentialité, droits sociaux et recours anciens et futurs protégés.",
       "Aucune habilitation de collecte nouvelle ; contrôle par d'autres fondements légaux et preuve des droits par les moyens légalement admissibles, sans exclusion pour absence du relevé supprimé.",
       "L'entreprise de travail temporaire fournit le relevé des contrats de mission à l'institution mentionnée à l'article L. 5312-1, notamment pour la vérification des droits des salariés au revenu de remplacement prévu à l'article L. 5421-2.",
       "À compter de cette date, l'entreprise de travail temporaire n'est plus tenue d'établir ni de transmettre le relevé spécial des contrats de mission prévu par le présent article.")

# Préserver un renouvellement définitivement conclu avant la réforme ne permet
# pas d'en décider un nouveau après elle. Uniformiser les articles du présent lot.
for n in ['L1251-35', 'L1251-35-1']:
    a = answers[n]
    a['proposed_xml'] = a['proposed_xml'].replace(
        "Cette conservation n'autorise pas un renouvellement prenant effet après cette date.",
        "Les renouvellements à durée déterminée valablement conclus avant cette date conservent leurs effets ; une simple faculté de renouvellement non encore exercée ne vaut pas renouvellement déjà conclu. Aucun renouvellement à durée déterminée ne peut être conclu ou décidé à compter de cette date."
    ).replace(
        "Aucun nouveau contrat de travail à durée déterminée ni renouvellement prenant effet à compter de cette date ne peut être conclu sur ce fondement.",
        "Les renouvellements à durée déterminée valablement conclus avant cette date conservent leurs effets ; une simple faculté de renouvellement non encore exercée ne vaut pas renouvellement déjà conclu. Aucun nouveau contrat de travail à durée déterminée ni renouvellement à durée déterminée ne peut être conclu ou décidé à compter de cette date."
    )
    a['reason'] = a['reason'].replace(
        "ni un renouvellement d'emploi à terme prenant effet après la réforme", 
        "ni un renouvellement d'emploi à terme conclu ou décidé après la réforme")
    a['review_notes'] = a['review_notes'].replace(
        "mais ne permettent pas un renouvellement à terme prenant effet après la réforme",
        "et pour un renouvellement définitivement conclu avant la réforme, mais ne permettent pas un renouvellement à terme conclu ou décidé après celle-ci")
    a['review_notes'] += (
        " La transition distingue une faculté contractuelle de renouvellement, qui n'autorise aucun exercice après la réforme, d'un renouvellement définitivement conclu avant celle-ci dont les effets contractuels acquis sont préservés ; uniformiser cette précision avec les autres lots."
    )

old35 = "les limitations du nombre de renouvellements et l'obligation d'un avenant de renouvellement fondées sur le seul présent article cessent de s'appliquer."
new35 = "les limitations du nombre de renouvellements et l'obligation de stipulation ou d'avenant de renouvellement fondées sur le seul présent article cessent de s'appliquer."
answers['L1251-35']['proposed_xml'] = answers['L1251-35']['proposed_xml'].replace(old35, new35)
for e in answers['L1251-35']['substantive_impact']['effects']:
    e['proposed_quote'] = e['proposed_quote'].replace(old35, new35)

contexts = {
    'L1251-33': "L'indemnité de fin de mission et ses dispenses ne sont pas le préavis ou l'indemnité ordinaire de rupture ; l'échéance d'affectation ne les déclenche pas.",
    'L1251-34': "Les trois jours ouvrables de l'offre de protection radiologique ne sont pas un préavis de rupture et n'ouvrent pas une indemnité ordinaire par fin d'affectation.",
    'L1251-35': "La fin ou le non-renouvellement d'une affectation ne rompt pas l'emploi ; supprimer le nombre de renouvellements ne supprime pas les règles de rupture de l'agence employeur.",
    'L1251-35-1': "La suppression du plafond supplétif de deux renouvellements ne fait pas de la fin d'affectation une notification de rupture ou une fin d'emploi.",
    'L1251-36': "La carence entre affectations est distincte du préavis de rupture de l'emploi ; son abrogation ne permet pas de supprimer la notification ou les garanties de rupture.",
    'L1251-36-1': "Le tiers, la moitié et le seuil de quatorze jours appartiennent à la carence, pas au préavis ni à l'ancienneté de l'indemnité ordinaire.",
    'L1251-38': "La reprise des missions des trois mois précédant l'embauche contribue à l'ancienneté reconnue du nouvel employeur ; elle ne déclenche aucune rupture de l'emploi.",
    'L1251-39': "La reconnaissance des droits chez l'utilisateur part du premier jour de la mission ; la seule poursuite ou fin de mission n'est pas une notification de rupture.",
    'L1251-40': "Le recours contre l'utilisateur et l'indemnité de retard plafonnée à un mois sont distincts de la rupture ordinaire et ne disparaissent pas avant un an d'ancienneté.",
    'L1251-41': "L'indemnité de requalification d'au moins un mois et le délai judiciaire d'un mois restent distincts de la rupture ordinaire ; aucune condition d'un an n'est ajoutée à ce recours.",
    'L1251-43': "Le terme de la mise à disposition règle l'affectation commerciale, sans valoir notification de rupture ni déclencheur de l'indemnité ordinaire.",
    'L1251-46': "La suppression du relevé n'emporte ni rupture d'emploi à la fin d'une mission ni dispense des règles d'une véritable rupture, et ne ferme aucun revenu de remplacement éligible."
}

extra_checks = {
    ('L1251-33','L1251-6'): "Le 1° source renvoie exactement au 3° de L1251-6 : saison et usage sectoriel. La dispense d'indemnité exige son texte collectif propre pour les anciens contrats. La proposition de la cible conserve ces catégories comme affectations temporaires, sans nouveau CDD ; leur durée ne rompt pas l'emploi et les autres cas de remplacement restent distincts.",
    ('L1251-33','L1251-57'): "Le 2° source vise les deux assimilations : stages, bilans et VAE à l'initiative de l'employeur ou du salarié, puis formations professionnelles selon texte collectif. La cible les maintient pour les futures situations en contrat unique ; seule la dispense liée à l'ancienne indemnité reste historique, sans fermer formation ni droits sociaux futurs.",
    ('L1251-34','L1251-26'): "Le renvoi porte au deuxième alinéa, exactement sur qualification professionnelle, rémunération, horaire de travail et temps de transport : ces quatre garanties sont reprises. Ni l'exception de faute grave du premier alinéa, ni les quatre semaines/trois affectations du quatrième ne sont importées dans la protection radiologique. Le délai propre est trois jours ouvrables après fin de mission, distinct des quinze jours de rupture de l'emploi.",
    ('L1251-34','L1251-12-1'): "La source vise ses plafonds de dix-huit, neuf, vingt-quatre et trente-six mois, ainsi que le minimum de six mois de l'exportation exceptionnelle ; la proposition les abroge prospectivement et préserve les anciens contrats. Le renvoi dérogatoire du présent article n'est donc conservé que dans ce champ historique, sans reconstituer un plafond pour les futures affectations ou un emploi à terme.",
    ('L1251-34','L1251-12'): "Le renvoi concerne la durée conventionnelle de la mission auprès de l'utilisateur. La proposition de la cible distingue cette affectation de l'emploi indéterminé ; la dérogation protectrice de L1251-34 reste applicable à cette limite pour les futures situations dosimétriques éligibles, sans fin automatique de l'emploi ni suppression du contrôle de l'affectation permanente.",
    ('L1251-35-1','L1251-12-1'): "La durée cumulée du contrat initial et de ses renouvellements était plafonnée selon cette cible à défaut de durée conventionnelle. Sa proposition abroge les plafonds pour l'avenir en gardant les anciens contrats ; le présent article n'en conserve le calcul que pour les contrats historiques concernés et ne les rétablit pas dans les lettres de mission futures.",
    ('L1251-35-1','L1251-12'): "La durée totale conventionnelle est une limite d'affectation autonome, conservée par la proposition de la cible malgré la disparition du nombre légal de renouvellements. L'abrogation du plafond supplétif de deux fois ne supprime pas cette durée et ne permet pas de limiter l'emploi indéterminé à la fin de la mission.",
    ('L1251-35-1','L1251-35'): "Cette cible est le fondement de branche dont L1251-35-1 est le supplétif. La vue proposée l'abroge déjà et sa version finale du présent lot conserve cette suppression ; aucun plafond ni avenant sur ce fondement ne renaît pour les missions nouvelles. Les anciens renouvellements définitivement conclus sont distincts d'une simple faculté non exercée après la réforme.",
    ('L1251-36','L1251-5'): "La réserve source conserve l'interdiction de pourvoir durablement un poste permanent de l'utilisateur. La proposition de la cible porte bien sur la mission et non sur la durée de l'emploi dans l'agence ; supprimer la carence n'efface pas ce contrôle ni les garanties mensuelles et d'intermission des nouveaux contrats uniques.",
    ('L1251-36-1','L1251-36'): "La cible est le fondement du délai et de son calcul par branche, tandis que L1251-36-1 fixe le barème supplétif. Les deux textes sont abrogés dans le même lot avec extinction des effets futurs des délais en cours ; les droits sur faits anciens et leurs dispenses subsistent, sans compter une seconde suppression ni permettre un nouveau CDD.",
    ('L1251-40','L1251-5'): "Le premier alinéa conserve le fondement du caractère temporaire de l'affectation : ni objet ni effet de pourvoir durablement un poste permanent de l'utilisateur. La proposition de la cible maintient cette règle dans le contrat unique sans borner l'emploi ; sa violation peut encore fonder les droits contre l'utilisateur au premier jour de mission.",
    ('L1251-40','L1251-17'): "Le deuxième alinéa vise la transmission sous deux jours ouvrables, non un délai de notification de rupture. La proposition de la cible substitue la lettre de mission, dispense d'un nouveau contrat par affectation et du second envoi d'un écrit déjà transmis. Le retard réellement constitué conserve son indemnité maximale d'un mois sans requalification à lui seul ni seuil d'ancienneté.",
    ('L1251-40','L1251-11'): "La cible impose le terme précis avec cinq exceptions de terme imprécis et une durée minimale dans ces exceptions ; sa proposition applique ces règles à la lettre de mission du contrat unique. Le renvoi conservé n'abroge pas ce minimum d'affectation, ne recrée pas un terme d'emploi et ne restaure pas le minimum d'un mois supprimé dans la cible distincte L1251-7.",
    ('L1251-40','L1251-12-1'): "Les plafonds légaux de durée et leurs cas spéciaux sont proposés à l'abrogation par cette cible ; le CDI intérimaire était déjà dispensé par L1251-58-6. Le premier alinéa proposé ne les vise plus comme règle générale ; l'énumération historique les conserve pour les anciens contrats dans leur champ et non comme fondement d'une requalification future sur un plafond supprimé.",
    ('L1251-40','L1251-35-1'): "Le plafond supplétif de deux renouvellements et l'avenant avant terme sont abrogés dans la proposition de cette cible et dans le présent lot. Le renvoi passe dans la seule disposition historique ; les nouvelles lettres de mission ne peuvent être requalifiées à cause d'un dépassement d'un nombre désormais supprimé. Les droits de contestation du terme ancien demeurent.",
    ('L1251-40','L1251-12'): "La durée de mission fixée par convention ou accord de branche étendu reste un fondement matériel de recours contre l'utilisateur. La proposition de la cible la limite à l'affectation et maintient la dispense de plafond légal du CDI ; le présent article ne confond ni durée de mission et durée d'emploi ni plafond conventionnel conservé et nombre de renouvellements supprimé.",
    ('L1251-40','L1251-35'): "La source vise les stipulations de renouvellement prises sur ce fondement. La cible et sa version finale de ce lot abrogent ce dispositif pour les missions futures ; le présent article garde la référence dans le seul champ des faits et contrats historiques, sans reconstituer la clause ou l'avenant de renouvellement supprimé.",
    ('L1251-40','L1251-30'): "La cible permet l'aménagement du terme. Sa proposition conserve pour les anciennes missions un jour pour cinq jours de travail, deux jours pour les missions de moins de dix jours, la réduction maximale de dix jours et les durées applicables ; elle les retire pour les nouvelles affectations en CDI avec information, consentement si élément essentiel, et salaires garantis. Le renvoi n'applique donc pas ces plafonds historiques aux nouvelles missions et ne vaut pas rupture d'emploi.",
    ('L1251-40','L1251-6'): "Le renvoi L1251-5 à L1251-7 inclut tous les remplacements du 1° a à e, l'accroissement temporaire, la saison/l'usage du 3°, puis les remplacements professionnels et agricoles des 4° et 5°. La proposition de la cible conserve ces catégories pour les affectations futures et leur contrôle, sans rendre licite un nouvel emploi à terme ni importer un statut public dans le contrat privé.",
    ('L1251-40','L1251-7'): "Les cinq cas ont été lus : insertion, complément de formation, apprentissage, personnes de L5212-13 sauf son 5°, et insertion de L5132-6. La proposition retire l'habilitation préalable du 1° et le minimum d'un mois du 5°, maintient la formation et les avantages futurs sous contrat unique. Le recours de L1251-40 ne doit rétablir ni cette habilitation ni ce minimum supprimés, tout en protégeant les autres conditions et engagements antérieurs.",
    ('L1251-43','L1251-31'): "Le 3° source exigeait une clause spéciale pour le report de remplacement jusqu'au surlendemain de la reprise d'emploi. La proposition de la cible maintient cette faculté pour les futures affectations et pour les contrats anciens. Supprimer la clause préalable n'abroge pas cette dérogation favorable et le surlendemain ne devient pas une fin automatique de l'emploi indéterminé.",
    ('L1251-43','L1251-30'): "Le 3° source imposait une clause préalable de variation, répétée à l'avenant commercial. Sa suppression ne rétablit pas les proportions d'un jour pour cinq, deux jours et dix jours que la proposition de la cible retire des nouvelles missions en CDI. L'accord entre entreprises, l'information de date, le consentement si élément essentiel et la rémunération garantie demeurent ; l'emploi se poursuit.",
    ('L1251-43','L1251-6'): "Les 1°, 4° et 5° fondaient la mention du nom et de la qualification de la personne remplacée. Ces mentions sont retirées du contrat commercial, mais les situations réelles de remplacement et les autres catégories de la cible demeurent contrôlables. La qualification du poste au 4° de L1251-43 et le comparateur salarial au 6° restent distincts ; aucune mission saisonnière n'autorise un nouveau CDD.",
    ('L1251-43','L4154-2'): "Le 4° vise exactement la liste des postes à risques particuliers, pas une liste de durée d'emploi. La cible conserve formation renforcée, accueil et information adaptés, liste établie après avis du médecin du travail et du CSE s'il existe et accès de l'inspection. Sa proposition couvre les futurs salariés temporaires et contrats uniques concernés : aucune de ces garanties n'est retirée par l'allègement des mentions de remplacement.",
}

def global_check(number, target_number):
    context = contexts[number]
    if target_number == 'L1234-1':
        return context + (
            " La source de la cible fixe les anciens seuils de six mois et deux ans ; sa proposition prévoit quinze jours calendaires pour les contrats nouveaux, sans seuil d'ancienneté, y compris en faute grave avec paiement si non-exécution. Le calcul commence le lendemain de présentation ou réception de la notification écrite selon L1234-3 lu dans le corpus. Les anciens contrats, procédures collectives et autorisations des salariés protégés gardent leur régime propre."
        )
    if target_number == 'L1221-2':
        note = (
            " L5312-1 désigne l'opérateur public destinataire du relevé : le contrat unique privé ne régit pas de ce seul fait ses agents ou ses missions publiques."
            if number == 'L1251-46' else ''
        )
        return context + (
            " La cible proposée interdit les nouveaux emplois à terme, y compris terme d'événement, saison, formation ou mission, mais permet une affectation limitée au sein du CDI. Les droits des contrats antérieurs et renouvellements définitivement conclus avant l'entrée en vigueur restent à préserver ; une faculté non exercée ne permet aucun renouvellement décidé après. Les situations futures éligibles gardent leurs avantages, sans recréer de CDD spécial."
        ) + note
    if target_number == 'L1234-9':
        return context + (
            " La cible officielle ouvre l'indemnité ordinaire à huit mois sauf faute grave ; sa proposition fixe pour les nouveaux contrats un an apprécié à la fin effective, préavis inclus, puis 0,20 mois par année totale, première année comprise, prorata des mois complets et plafond légal de six mois, employeur seul, avec exception de faute grave maintenue. Les composantes anciennes, avantages plus favorables, salaires, congés, dommages et indemnités spéciales restent distincts ; le présent article n'importe pas ce seuil dans un autre droit."
        )
    raise ValueError((number,target_number))

for s in sources:
    n = s['number']
    a = answers[n]
    key = s['code_id'] + '|' + s['source_id']
    checks = []
    for target_key in refs['requirements'][key]:
        t = refs['targets'][target_key]
        tn = t['number']
        assessment = (global_check(n, tn) if tn in ['L1234-1','L1221-2','L1234-9']
                      else extra_checks[(n,tn)])
        checks.append(dict(target_key=target_key, view_sha256=t['view_sha256'],
                           assessment=assessment))
    a['reference_checks'] = checks

out = [answers[s['number']] for s in sources]
Path('answer.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')

if __name__ == '__main__':
    print(f"answer.json : {len(out)} articles, {sum(len(a['reference_checks']) for a in out)} vérifications de renvois")
