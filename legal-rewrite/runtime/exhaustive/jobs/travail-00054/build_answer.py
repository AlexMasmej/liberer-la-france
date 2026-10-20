import json
import re
from html import unescape
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
by_number = {s['number']: s for s in sources}
answers = {}


def plain(xml):
    return unescape(re.sub(r'<[^>]+>', '', xml or ''))


def retained(number, reason, notes, assessment, limits, burdens, benefit=None):
    s = by_number[number]
    a = {k: s[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    a.update(proposed_xml=None, reason=reason, review_notes=notes,
             status='retained_unchanged', classification='retained_necessary',
             substantive_impact=dict(version=1, classification='retained_necessary',
                                     assessment=assessment, scope_limitations=limits,
                                     new_burdens_review=burdens, effects=[]),
             reference_checks=[])
    if benefit:
        a['benefit_review'] = benefit
    answers[number] = a
    return a


def rewritten(number, xml, reason, notes, assessment, limits, burdens,
              effects, classification='material_reduction', removed=None, benefit=None):
    s = by_number[number]
    a = {k: s[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    a.update(proposed_xml=xml, reason=reason, review_notes=notes, status='rewrite_draft',
             substantive_impact=dict(version=1, classification=classification,
                                     assessment=assessment, scope_limitations=limits,
                                     new_burdens_review=burdens, effects=effects),
             reference_checks=[])
    if removed:
        a.update(change_type='normative_reduction',
                 reform_policy_id='editorial_direction_2026_10_19',
                 removed_provisions=removed)
    if benefit:
        a['benefit_review'] = benefit
    answers[number] = a
    return a


def effect(kind, measure, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure, description=description,
                before=before, after=after, unit=unit,
                affected_population=population,
                conditions_and_transition=transition,
                replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


retained('L2313-6',
    "Maintien intégral après examen : la cessation des mandats accompagne la disparition réelle de l'établissement distinct, sans imposer une instance devenue sans objet. La faculté d'achever les mandats par accord est une dérogation favorable à conserver, non une autorisation administrative. Aucun doublon déclaratif ou prélèvement n'est institué ici.",
    "Les cibles L2313-2 à L2313-5 ont été lues dans le corpus : accord majoritaire, accord subsidiaire avec les élus, décision unilatérale puis traitement du litige. Le premier alinéa de L2232-12 exige plus de 50 % des suffrages exprimés en faveur des organisations représentatives ; les autres voies de validation ne sont pas importées dans ce renvoi limité. La note d'entrée en vigueur de 2017-2018 n'est pas une transition de la réforme future. La fin du mandat ne vaut pas rupture du contrat de travail.",
    "La source entière comporte déjà une extinction de fonctions et une faculté conventionnelle de maintien. Ces deux règles sont nécessaires à la continuité ou à la clôture de la représentation ; aucune réduction normative supplémentaire n'est revendiquée.",
    "Ce maintien ne traite ni la détermination initiale des établissements ni les procédures de rupture des contrats ou les protections postérieures au mandat. Aucun solde global de charges n'est établi.",
    "Aucune charge nouvelle n'est identifiée : aucun texte de remplacement, déclaration ou accord obligatoire n'est ajouté et l'accord de maintien demeure facultatif.")

retained('L2313-7',
    "Maintien de l'article entier : les représentants de proximité sont une option de l'accord d'entreprise, non une strate imposée. Les quatre rubriques organisent leurs moyens, leur désignation et leurs responsabilités de santé et de sécurité sans rapport, autorisation ou renouvellement administratif supplémentaire à supprimer.",
    "L2313-2, lu intégralement, renvoie au seul premier alinéa de L2232-12 : conserver sa majorité et son assiette. Les représentants peuvent être membres du CSE ou désignés par lui ; aucune obligation de les élire séparément n'est ajoutée. La durée du mandat ne constitue pas une durée de l'emploi. Les heures de délégation restent une garantie négociée pour les futurs accords également.",
    "L'examen des conditions de l'accord et de la fin commune des mandats ne révèle aucune obligation autonome sans utilité démontrée. L'option de représentation locale et ses moyens restent intégralement ouverts.",
    "La faculté ne remplace pas le CSE ni ses missions légales ; aucun gain financier ou de délai n'est démontré par ce maintien.",
    "Aucune charge nouvelle n'est identifiée : ni représentants imposés, ni quota d'heures nouveau, ni pièce ou transmission de remplacement.")

retained('L2313-8',
    "Maintien intégral du cadre commun de représentation des unités économiques et sociales : le CSE commun évite la fragmentation entre personnes morales ; les accords puis la décision de l'employeur mandaté offrent déjà des voies graduées. L'arbitrage administratif ne se déclenche qu'en cas de litige et son contrôle judiciaire protège contre un découpage privant des salariés de représentation. Il ne s'agit pas d'un agrément préalable général.",
    "Vérifiés : seuil de onze salariés, au moins deux établissements pour l'organisation à deux niveaux, majorité des titulaires élus pour l'accord subsidiaire, absence de délégué syndical au niveau de l'UES et autonomie de gestion. Ne pas confondre cette majorité avec celle du premier alinéa de L2232-12. R2313-5 lu : décision administrative sous deux mois et recours judiciaire sous quinze jours, avec voie ouverte après rejet implicite. La suspension et la prorogation évitent un vide de représentation ; elles ne relèvent pas du préavis individuel. Le recours judiciaire n'est pas un second dépôt systématiquement obligatoire.",
    "La source entière organise une instance commune, des voies négociées et une solution subsidiaire contrôlable. Supprimer ici l'arbitrage amiable administratif imposerait d'emblée le juge aux différends, sans réduction nette établie ; les garanties sont conservées.",
    "Les coûts des deux niveaux d'instance et du contentieux ne sont pas chiffrés. Aucune suppression des protections électorales, des recours ou du champ des unités économiques et sociales n'est décidée.",
    "Aucune charge nouvelle n'est identifiée : maintien des seules obligations existantes, sans dossier périodique, enregistrement ou autorisation générale supplémentaire.")

retained('L2313-9',
    "Maintien intégral : le comité interentreprises et la participation d'un représentant de chaque CSE aux réunions mensuelles reposent déjà sur un choix conventionnel. Les quatre mentions donnent un contenu opératoire à ce choix ; leur suppression fragiliserait l'instance sans retirer une obligation de création générale, inexistante dans la source.",
    "Conserver le champ du même site ou de la même zone, les organisations représentatives au niveau interprofessionnel ou départemental et le seuil de onze salariés pour la participation facultative. Le rythme mensuel de la dernière phrase ne devient pas une réunion imposée à toutes les entreprises. Les fonctions ne constituent pas un contrat à terme et la réforme du contrat unique ne requiert pas de changement ici.",
    "La lecture de l'ensemble de l'article confirme un dispositif volontaire de coopération entre entreprises ; aucune nouvelle réduction n'est attribuée à la conservation de cette souplesse.",
    "Les accords peuvent créer leurs propres engagements ; leur coût n'est pas évalué et aucun démantèlement des droits conventionnels acquis n'est proposé.",
    "Aucune charge nouvelle n'est identifiée : l'instance et les participations demeurent facultatives, sans agrément ni dépôt supplémentaire créé.")

retained('L2313-10',
    "Maintien intégral de la dispense de renouvellement lorsque l'effectif est resté inférieur à onze salariés pendant douze mois consécutifs. Cette règle retire déjà une charge à l'échéance du mandat, tout en empêchant la suppression immédiate d'une représentation pour une fluctuation passagère. Aucun justificatif spécial ou déclaration supplémentaire n'est prévu.",
    "Les onze salariés, les douze mois consécutifs et l'expiration du mandat sont trois conditions distinctes, toutes conservées pour les situations futures. Le mandat en cours n'est pas interrompu par une simple baisse d'effectif. Cette dispense ne supprime pas les règles de nouvelle mise en place lorsque les conditions légales sont à nouveau remplies.",
    "La source officielle contient un allègement conditionnel utile déjà acquis ; le conserver entier ne constitue pas une nouvelle suppression d'élections ni une baisse de prélèvement.",
    "Le maintien ne dispense pas d'examiner le franchissement ultérieur du seuil et ne quantifie ni le nombre d'entreprises bénéficiaires ni un coût national.",
    "Aucune charge nouvelle n'est identifiée : mêmes seuil, période d'observation et échéance, sans attestation ou contrôle administratif créé.")

retained('L2314-1',
    "Maintien intégral de la composition du CSE, de l'égalité entre titulaires et suppléants et du référent contre le harcèlement sexuel et les agissements sexistes. La présence du suppléant seulement en l'absence du titulaire limite déjà la charge des réunions. L'aménagement négocié des sièges et des heures est conservé ; supprimer le référent retirerait une protection essentielle sans doublon démontré.",
    "L2314-7 est lu dans le présent lot : le volume global des heures dans chaque collège reste garanti. L2315-32 lu : majorité des membres présents et non-participation du président lorsqu'il consulte les élus comme délégation du personnel. Conserver la résolution, le choix parmi les membres et la fin du mandat du référent avec celui des élus. La note relative au 1er janvier 2019 ne fixe aucune date future.",
    "La source entière combine représentation effective, remplacement et prévention du harcèlement avec une souplesse conventionnelle. Aucun prélèvement, formulaire ou autorisation sans fonction essentielle n'y est isolé.",
    "Le barème réglementaire des sièges n'est pas réécrit dans ce lot et aucune économie sur les heures ou la prévention n'est présumée.",
    "Aucune charge nouvelle n'est identifiée : la désignation du référent et les règles de composition restent exactement celles de la source.")

retained('L2314-2',
    "Maintien intégral d'une faculté syndicale de désignation avec voix consultative. La réserve des entreprises de moins de trois cents salariés évite déjà une désignation distincte lorsque le délégué syndical exerce cette fonction de droit. Le renvoi aux conditions d'éligibilité demeure opérant après leur allègement proposé à L2314-19.",
    "L2143-22 lu intégralement : le délégué syndical est représentant de droit dans les entreprises de moins de trois cents salariés et leurs établissements, et reçoit les informations du CSE. L2314-19 du lot conserve l'âge de dix-huit ans, les exclusions d'indépendance et la qualité d'électeur ; la suppression proposée de ses restrictions supplémentaires se répercute ici par le renvoi, sans seconde mesure à compter. La désignation reste interne au personnel.",
    "La source entière ne crée pas de représentant obligatoire supplémentaire pour chaque syndicat. Le maintien de la faculté et de son articulation avec le délégué syndical ne reçoit aucun effet de réduction distinct.",
    "Les effets indirects du renvoi à l'éligibilité sont rattachés à la mesure de L2314-19 ; ils ne prouvent ni économie nationale ni suppression d'un représentant existant.",
    "Aucune charge autonome nouvelle n'est identifiée : pas de nouvelle désignation imposée, de voix délibérative ou de formalité ajoutée dans cet article.")

retained('L2314-3',
    "Maintien intégral : la participation consultative des professionnels de santé et de sécurité et l'invitation des services de contrôle ont une fonction essentielle de prévention. La délégation par le médecin à un membre compétent de l'équipe constitue déjà une souplesse utile ; les invitations ne sont pas des autorisations de réunion à supprimer.",
    "L2315-27 lu : les deux premiers alinéas concernent les réunions de prévention et celles consécutives à des événements graves ou à une demande motivée. Conserver les I et II, leurs 1° à 3°, la compétence du délégataire médical, les réunions de commission, l'initiative patronale ou la majorité de la délégation, et le seuil propre d'arrêt de travail d'au moins huit jours au II 3°. Le point-virgule source après « sont invités » n'est pas une condition manquante. La note d'application de 2021-2022 reste historique.",
    "L'article complet cible les participants et événements utiles à la prévention, sans rapport général ou agrément redondant. Aucune simplification matérielle nouvelle n'est revendiquée pour ce maintien.",
    "Les obligations d'information du calendrier de L2315-27 sont distinctes et ne sont ni supprimées ni réputées réécrites ici. Aucun bilan de coût de prévention n'est établi.",
    "Aucune charge nouvelle n'est identifiée : mêmes réunions, événements, participants et possibilités de délégation, sans déclaration sanitaire de remplacement.")

retained('L2314-4',
    "Maintien intégral de l'information électorale datée, de la périodicité de quatre ans et du délai maximal de quatre-vingt-dix jours pour le premier tour. Ce plafond ne constitue pas un délai minimal d'attente et permet déjà un scrutin plus rapide ; l'information préalable rend les candidatures et contestations effectives.",
    "Le renvoi au deuxième alinéa de L2311-2 est un renvoi existant, non remplacé par le régime du contrat unique ; le seuil de onze salariés est conservé. Le délai de quatre-vingt-dix jours n'est pas le préavis de rupture de quinze jours. Les invitations de L2314-5 conservent leurs propres garanties de réception et de calendrier, après suppression proposée de l'anticipation fixe de deux mois.",
    "La source entière autorise déjà tout moyen donnant date certaine et impose seulement un délai butoir de scrutin. La conserver ne démontre aucune obligation supprimée ni nouvelle réduction de délai.",
    "Les règles de franchissement du seuil, non assignées ici, ne sont pas modifiées. Aucun taux de participation ou gain de temps effectif n'est estimé.",
    "Aucune charge nouvelle n'est identifiée : pas de support exclusif, accusé supplémentaire ou nouvelle échéance ; l'information existante demeure nécessaire.")

s = by_number['L2314-5']['source_xml']
xml = s.replace('y sont également invités par courrier.', 'y sont également invités par tout moyen.')
xml = xml.replace("Dans le cas d'un renouvellement de l'institution, cette invitation est effectuée deux mois avant l'expiration du mandat des délégués en exercice. Le premier tour des élections a lieu dans la quinzaine précédant l'expiration de ce mandat.",
                  "Dans le cas d'un renouvellement de l'institution, le premier tour des élections a lieu dans la quinzaine précédant l'expiration du mandat des délégués en exercice.")
xml += "<p>Les nouvelles modalités d'invitation s'appliquent aux invitations effectuées à compter de l'entrée en vigueur de la présente rédaction. Les invitations antérieures régulièrement effectuées restent valables sans réitération ; les délais déjà échus et les recours relatifs aux opérations antérieures restent régis par les dispositions antérieures, sans préjudice de l'application de la loi pénale plus douce.</p>"
a = rewritten('L2314-5', xml,
    "Réduction de fond : supprimer le courrier imposé au deuxième alinéa et l'invitation obligatoirement anticipée de deux mois lors d'un renouvellement. Les mêmes syndicats sont invités par tout moyen, sans déclaration de remplacement. Maintien intégral des critères syndicaux, du premier tour dans la quinzaine précédant l'expiration, de la réception de l'invitation au moins quinze jours avant la négociation, de la dispense conditionnelle des entreprises de onze à vingt salariés et de la protection dès connaissance de l'imminence de la candidature.",
    "Les six alinéas matériels sources restent dans le même ordre, notamment les deux premiers visés par L2314-29 et le cinquième portant la dérogation onze-vingt salariés. Retirer l'anticipation fixe n'autorise pas une invitation tardive : réception quinze jours avant la réunion et calendrier du scrutin restent impératifs. Le nouveau support n'est pas un simple envoi présumé reçu. Les preuves de réception nécessaires à l'application du quatrième alinéa restent à la charge de celui qui s'en prévaut, sans certificat nouveau. L2411-7 et L2413-1 lus dans le corpus : l'autorisation protectrice demeure distincte du préavis individuel. L2412-3 est conservé dans son champ transitoire et dans la garantie saisonnière future de sa proposition, sans autoriser un nouveau CDD. Les contrôles des quatre vues requises sont détaillés dans reference_checks ; les deux cibles indemnitaires/de préavis ne sont pas des renvois présents dans cet article. Aucun renvoi nouveau n'est créé.",
    "Par rapport à toute la source, deux contraintes patronales précises disparaissent : support courrier pour certains syndicats et anticipation uniforme de deux mois. Il ne s'agit pas de supprimer la négociation ni de compter les quinze jours comme un nouveau gain ; les garanties et la petite entreprise éligible restent couvertes.",
    "L'allègement vise seulement les invitations nouvelles. Les temps réellement nécessaires à la négociation peuvent limiter le gain de calendrier ; aucune économie d'affranchissement nationale ou procédure complète en quinze jours n'est démontrée.",
    "Aucune charge nouvelle autonome n'est identifiée : mêmes destinataires, même contenu et réception déjà requise, aucun registre ni déclaration remplaçante. Les moyens utilisés doivent permettre d'établir la réception en cas de contestation, comme l'exige déjà le délai source.",
    [effect('obligation_removed', 'cse-invitations-sans-courrier-ni-anticipation-fixe',
            "Retrait du support courrier imposé aux syndicats du deuxième alinéa, sans retirer leur invitation.",
            "Invitation par courrier des syndicats représentatifs, ayant une section ou affiliés au niveau national et interprofessionnel ; autres syndicats déjà invités par tout moyen.",
            "Invitation des mêmes syndicats par tout moyen ; réception au moins quinze jours avant la réunion toujours requise.",
            'legal_duty', "Employeurs organisant les élections et syndicats du deuxième alinéa.",
            "Invitations effectuées à compter de l'entrée en vigueur ; invitations antérieures valables et recours conservés.",
            "Aucun dépôt de remplacement ; maintien des seules exigences existantes d'invitation et de réception.",
            'y sont également invités par courrier.', 'y sont également invités par tout moyen.'),
     effect('deadline_reduced', 'cse-invitations-sans-courrier-ni-anticipation-fixe',
            "Suppression de l'anticipation minimale fixe de deux mois au renouvellement, sans suppression du délai protecteur de réception.",
            "Invitation deux mois avant l'expiration du mandat et réception au plus tard quinze jours avant la première réunion ; premier tour dans la quinzaine avant expiration.",
            "Plus d'anticipation uniforme de deux mois ; quinze jours de réception préalable à la réunion et quinzaine du premier tour inchangés. Les deux mois ne sont pas convertis fictivement en soixante jours.",
            'other', "Employeurs et syndicats négociant lors du renouvellement du CSE.",
            "Invitations nouvelles seulement ; les échéances échues et les recours antérieurs ne sont pas effacés.",
            "Pas de nouvelle formalité ; l'organisation doit toujours respecter la négociation effective et le calendrier conservé.",
            "cette invitation est effectuée deux mois avant l'expiration du mandat des délégués en exercice.",
            "Dans le cas d'un renouvellement de l'institution, le premier tour des élections a lieu dans la quinzaine précédant l'expiration du mandat des délégués en exercice.")],
    removed=["Obligation d'utiliser un courrier pour inviter les organisations syndicales énumérées au deuxième alinéa.",
             "Obligation d'effectuer l'invitation au renouvellement avec une anticipation de deux mois avant l'expiration du mandat, indépendamment des autres délais utiles conservés."],
    benefit="La dispense conditionnelle d'invitation des syndicats pour les entreprises de onze à vingt salariés est intégralement conservée, y compris pour les prochaines élections : elle dépend toujours de l'absence de candidat dans les trente jours de l'information. Les droits des syndicats à être informés et invités, le délai de réception de quinze jours, le premier tour avant expiration et la protection du candidat dès connaissance de l'imminence restent applicables. Les renvois L2411-7, L2412-3 et L2413-1 ne retirent aucune autorisation protectrice, ni la prolongation saisonnière destinée aux futurs contrats uniques par la proposition cible. Les critères de deux ans des syndicats sont distincts des délais patronaux supprimés.")

checks = {
    'L1234-1': "Cette cible règle le préavis de licenciement : la proposition prévoit quinze jours calendaires sans ancienneté pour les contrats nouveaux, avec maintien des règles des contrats antérieurs. L2314-5 ne la cite pas et ses quinze jours concernent la réception d'une invitation syndicale, jamais une rupture. Aucune autorisation de licenciement d'un candidat n'est supprimée par ce calendrier électoral.",
    'L1221-2': "La source admet le CDI et les cas de CDD ; la proposition réserve aux nouvelles relations le contrat unique sans terme et protège les contrats antérieurs. L2314-5 n'y renvoie pas directement et vise tout candidat éligible, quel que soit l'ancien support du contrat. Le renvoi à L2412-3 ne permet donc ni nouvelle embauche à terme ni renouvellement de CDD ; la durée d'un mandat ou d'une saison ne termine pas l'emploi.",
    'L1234-9': "Cette cible porte sur l'indemnité de rupture, non sur la candidature électorale : la proposition distingue le seuil d'un an au terme effectif avec préavis inclus, le taux de 0,20 mois sur toute l'ancienneté, les fractions en mois complets et le plafond de six mois, avec transition des contrats anciens. L2314-5 ne la cite pas ; la protection du candidat n'exige aucune ancienneté indemnitaire et préserve les recours contre une illégalité dès son déclenchement.",
    'L2412-3': "Le renvoi final est réel. La source exige l'autorisation de l'inspecteur pour certaines ruptures et échéances de CDD protégés et prolonge les protections saisonnières. La proposition réserve les anciens CDD, sans renouvellement à terme, et conserve expressément la prolongation pour les futurs salariés saisonniers ou d'usage en contrat unique ; les nouveaux contrats relèvent aussi du chapitre Ier. Maintenir ce renvoi protège ces champs distincts sans transformer le préavis de quinze jours en dispense d'autorisation ; L2314-5 fixe le départ de la protection dès connaissance de l'imminence, sans attendre la notification formelle de candidature."
}
key = a['code_id'] + '|' + a['source_id']
for target_key in refs['requirements'][key]:
    t = refs['targets'][target_key]
    a['reference_checks'].append(dict(target_key=target_key, view_sha256=t['view_sha256'], assessment=checks[t['number']]))

retained('L2314-6',
    "Maintien intégral de la double majorité du protocole préélectoral. Elle garantit un consentement syndical effectif et une audience représentative ; l'alternative lorsque les résultats ne sont pas disponibles évite déjà un blocage. La retirer supprimerait une garantie de validité, sans éliminer de rapport ou autorisation redondante.",
    "Conserver la majorité des organisations ayant participé, puis, parmi les signataires, les organisations représentatives ayant recueilli la majorité des suffrages exprimés aux dernières élections ; à défaut de résultats, majorité des organisations représentatives. Ce n'est ni la majorité de 50 % des inscrits ni le mécanisme de consultation de L2232-12. Les exceptions législatives, dont l'unanimité propre de L2314-12, restent réservées.",
    "Aucune réduction matérielle n'est attribuée au maintien de la règle complète : les majorités et leurs assiettes exactes servent la légitimité du scrutin.",
    "La conservation ne vaut pas validation des protocoles particuliers ni mesure du coût de négociation ; les autres articles fixent leurs dérogations propres.",
    "Aucune charge nouvelle n'est identifiée : mêmes signatures et même appréciation des résultats, sans attestation ou protocole supplémentaire.")

retained('L2314-7',
    "Maintien intégral d'une faculté d'aménagement des sièges et des heures dans le protocole. La garantie du volume global, vérifiée collège par collège, empêche qu'une simplification retire les moyens de représentation ; aucune création d'heures ou de sièges nouveaux n'est imposée ici.",
    "Conserver le caractère alternatif du nombre de sièges ou du volume individuel et le plancher global dans chaque collège, apprécié au regard de l'effectif. Le renvoi de L2314-1 à cette souplesse demeure cohérent. Un volume global identique à l'échelle de l'entreprise ne suffit pas s'il réduit celui d'un collège.",
    "La source entière est déjà une dérogation favorable à l'organisation conventionnelle assortie d'un plancher utile. Son maintien ne constitue ni une fusion nouvelle ni une baisse d'heures revendiquée.",
    "Le barème légal ou réglementaire de référence et les accords particuliers ne sont pas modifiés ; aucun solde financier n'est établi.",
    "Aucune charge nouvelle n'est identifiée : la négociation demeure facultative dans ce champ et aucun contrôle, dépôt ou calcul de remplacement n'est ajouté.")

retained('L2314-8',
    "Maintien intégral du droit de demander les élections et de l'engagement de la procédure dans le mois. Le délai de six mois ne bloque que la répétition après une procédure effectivement engagée et un procès-verbal de carence ; il évite des cycles électoraux immédiatement répétés sans priver durablement les salariés d'une voie de mise en place. Sa suppression créerait une obligation patronale récurrente sans borne, sans baisse nette démontrée.",
    "Les deux conditions cumulatives du second alinéa sont maintenues ; une simple absence de CSE ou une absence d'initiative de l'employeur ne suffit pas à faire courir six mois. Le premier alinéa exige d'engager la procédure, non d'avoir élu le comité dans le mois. Le renvoi à L2314-5 demeure opérant avec l'assouplissement des invitations et sans perte des candidatures protégées.",
    "L'article entier protège l'initiative d'un salarié ou d'un syndicat et limite un renouvellement répétitif de procédure. Les délais sont conservés pour leur fonction propre ; aucune simplification nouvelle n'est comptée.",
    "Aucune estimation de la fréquence des carences ne permet de chiffrer le coût d'une nouvelle procédure. La règle ne prive pas des recours contre une carence irrégulière.",
    "Aucune charge nouvelle n'est identifiée : ni demande périodique ni relance imposée, et aucune déclaration n'est ajoutée aux deux voies existantes.")

xml = """<p>Lorsque le comité social et économique n'a pas été mis en place ou renouvelé, un procès-verbal de carence est établi par l'employeur. L'employeur porte à la connaissance des salariés par tout moyen permettant de donner date certaine à cette information, le procès-verbal dans l'entreprise et le transmet dans les quinze jours, par tout moyen permettant de conférer date certaine, au destinataire chargé, pour le compte du ministre chargé du travail, de la collecte des résultats des élections professionnelles. Cette transmission unique, effectuée selon les modalités applicables à cette collecte, vaut transmission à l'agent de contrôle de l'inspection du travail mentionné à l'article L. 8112-1. Le destinataire chargé de la collecte communique le procès-verbal à cet agent sans nouvel envoi de l'employeur. L'agent de contrôle communique une copie du procès-verbal de carence aux organisations syndicales de salariés du département concerné.</p><p>Ces dispositions s'appliquent aux transmissions dont le délai n'est pas expiré à la date d'entrée en vigueur de la présente rédaction et aux transmissions dues à compter de cette date. Pour ces seules transmissions, le procès-verbal déjà reçu par le destinataire chargé de la collecte est communiqué à l'agent de contrôle sans nouvel envoi de l'employeur. Les obligations dont le délai avait expiré avant cette date et les recours relatifs aux opérations antérieures restent régis par les dispositions antérieures, sans préjudice de l'application de la loi pénale plus douce.</p>"""
rewritten('L2314-9', xml,
    "Réduction de fond avec transfert de traitement : fusionner l'envoi du procès-verbal de carence à l'inspection avec celui déjà imposé au collecteur ministériel par R2314-22. L'employeur n'effectue qu'une transmission administrative ; le collecteur l'achemine à l'agent de contrôle. Le procès-verbal, sa diffusion datée aux salariés, le délai de quinze jours et l'information des syndicats du département sont maintenus. Il ne s'agit pas d'une suppression de l'information ni d'une simple reprise des droits de réemploi existants.",
    "R2314-22, lu intégralement dans le corpus public, exige déjà un exemplaire du procès-verbal d'élections ou de carence au prestataire ministériel, dans les quinze jours suivant la tenue des élections, avec formulaire homologué et garanties du téléservice. Sa coordination doit rendre explicites l'envoi unique et l'acheminement vers l'inspection ; elle n'est pas prétendue rédigée ici. Aucun nouveau renvoi numéroté n'est inséré : la collecte décrite est celle de ce texte vérifié. Le point de départ de la phrase source « dans les quinze jours » n'est pas précisé dans L2314-9 ; la difficulté d'articulation avec la tenue des élections, notamment en cas de carence sans vote, est préexistante et reste à expliciter dans le règlement, sans allongement d'une échéance acquise. La liste nominative affichée, propre aux comités élus, et les autres procès-verbaux de R2314-22 ne sont pas supprimés. Aucune mise en ligne publique de données personnelles n'est créée.",
    "La comparaison complète avec la source et le dépôt réglementaire existant démontre la suppression d'un envoi administratif patronal, remplacé par l'acheminement du même document par le collecteur. Le classement est mixte : une charge privée disparaît et une tâche de transmission est ajoutée au destinataire ministériel ; le coût net n'est pas établi.",
    "Le gain ne concerne que les procès-verbaux de carence, pas toutes les transmissions électorales. Le circuit réglementaire et son organisation technique restent à coordonner ; aucune économie publique ou nationale n'est chiffrée.",
    "Une tâche nouvelle d'acheminement vers l'inspection incombe au collecteur, avec coût non évalué. Aucun contenu, formulaire, donnée ou registre nouveau n'est demandé à l'employeur ; le dépôt homologué existant et la diffusion aux salariés restent dus.",
    [effect('obligation_merged', 'cse-carence-transmission-administrative-unique',
            "Fusion des deux envois administratifs patronaux du même procès-verbal de carence.",
            "Un envoi à l'inspection au titre de L2314-9 et un exemplaire au collecteur au titre de R2314-22, outre la diffusion interne aux salariés.",
            "Un seul envoi au collecteur valant transmission à l'inspection ; diffusion aux salariés et communication syndicale conservées, délai de quinze jours maintenu.",
            'legal_duty', "Employeurs établissant un procès-verbal de carence du CSE.",
            "Transmissions non échues à l'entrée en vigueur et futures ; pas de nouvel envoi d'un document déjà reçu par le collecteur ; obligations antérieurement échues préservées.",
            "Acheminement ajouté au collecteur ; aucun document de remplacement demandé à l'employeur.",
            "le transmet dans les quinze jours, par tout moyen permettant de conférer date certaine à l'agent de contrôle de l'inspection du travail",
            "Cette transmission unique, effectuée selon les modalités applicables à cette collecte, vaut transmission à l'agent de contrôle de l'inspection du travail"),
     effect('obligation_added', 'cse-carence-transmission-administrative-unique',
            "Acheminement par le collecteur du document déjà reçu vers l'inspection, contrepartie du dépôt patronal unique.",
            "Le texte législatif reçoit directement le document de l'employeur à l'inspection et ne charge pas le collecteur de cet acheminement.",
            "Le collecteur communique le même procès-verbal à l'agent, sans nouvel envoi patronal ; copie syndicale toujours effectuée par l'agent.",
            'legal_duty', "Destinataire chargé de la collecte pour le compte du ministre du travail et inspection du travail.",
            "Même bascule que le dépôt unique ; documents déjà reçus acheminés sans redépôt, droits et recours historiques conservés.",
            "Tâche de transmission et coût de fonctionnement supplémentaires possibles pour le collecteur ; aucun montant net démontré.",
            "Ce dernier communique une copie du procès-verbal de carence aux organisations syndicales de salariés du département concerné.",
            "Le destinataire chargé de la collecte communique le procès-verbal à cet agent sans nouvel envoi de l'employeur.")],
    classification='mixed',
    removed=["Transmission administrative séparée du procès-verbal de carence par l'employeur à l'agent de contrôle, en plus du dépôt ministériel déjà obligatoire."])

retained('L2314-10',
    "Maintien intégral des élections partielles lorsque la représentation disparaît dans un collège ou que les titulaires sont réduits d'au moins moitié. La dispense lorsque ces événements interviennent moins de six mois avant le terme et le réemploi des dispositions électorales précédentes allègent déjà la procédure ; les supprimer réduirait un avantage ou laisserait une représentation gravement incomplète.",
    "L2314-29 lu : scrutin de liste à deux tours, proportionnelle, règles du second tour et transmission aux syndicats. Conserver tous les sièges vacants des collèges intéressés, le seuil moitié ou plus, l'exception strictement « moins de six mois » et la durée restante du mandat. Le texte ne commande pas un renouvellement général ni un mandat plein. Les règles nouvelles de L2314-18 et L2314-19 n'annulent pas les opérations antérieures ; leur application doit se lire avec la base électorale conservée par le présent article pour les partielles.",
    "La source entière dose déjà le rétablissement nécessaire des élus et la dispense proche du terme. Aucun nouveau nombre d'élections supprimées n'est attribué au maintien de cette dispense.",
    "Les vacances et suppléances concrètes doivent être appréciées selon leurs règles propres ; aucune économie ou durée effective de procédure n'est calculée.",
    "Aucune charge nouvelle n'est identifiée : mêmes événements déclencheurs et même base de procédure, sans nouvelle déclaration ou nouvelle durée de mandat.")

retained('L2314-11',
    "Maintien intégral des collèges, de la représentation minimale des cadres à partir de cinq cent un salariés et du troisième collège à partir de vingt-cinq cadres assimilés. Ces garanties empêchent l'éviction d'une catégorie ; le collège unique pour un seul titulaire et un suppléant constitue une simplification favorable, à préserver pour les élections futures.",
    "Les deux collèges ordinaires, les catégories professionnelles exactes, le seuil de cinq cent un salariés et celui de vingt-cinq au moment de la constitution ou du renouvellement sont conservés. L2314-12 présente dans la source un renvoi au dernier alinéa alors que celui-ci porte sur le collège unique : correction explicite dans cet autre article du lot, sans déplacement d'alinéa ici. La règle du troisième collège demeure autonome et non neutralisable par accord.",
    "La source entière contient une organisation protectrice et une exception simplificatrice déjà existante ; son maintien n'est pas compté comme une fusion nouvelle de régimes ou un allègement créé.",
    "La composition des collèges détermine les assiettes de représentation ; aucune suppression de catégorie ni modification des seuils n'est proposée, et aucun coût national n'est établi.",
    "Aucune charge nouvelle n'est identifiée : mêmes collèges et mêmes seuils, sans siège ou fichier obligatoire ajouté par le maintien.",
    benefit="La dérogation du collège unique pour les entreprises ou établissements n'élisant qu'un titulaire et un suppléant est conservée entière pour les élections futures et les situations existantes. La représentation minimale d'un titulaire cadre dans le second collège à partir de cinq cent un salariés et le troisième collège dès vingt-cinq cadres assimilés restent applicables avec leurs catégories et dates d'appréciation. Les deux collèges ordinaires demeurent le cadre général ; aucune exemption ou garantie de représentation n'est supprimée sous couvert de simplification. La correction du renvoi dans L2314-12 rend ce maintien opérant sans modifier les seuils.")

xml = by_number['L2314-12']['source_xml'].replace("au dernier alinéa de l'article L. 2314-11", "à l'article L. 2314-11")
rewritten('L2314-12', xml,
    "Coordination nécessaire, sans réduction de fond : corriger le renvoi matériellement incohérent au dernier alinéa de L2314-11. Cet alinéa règle le collège unique, tandis que l'article contient auparavant le troisième collège. Le renvoi à l'article entier conserve exactement les conditions du troisième collège sans dépendre d'un décompte incertain des alinéas. L'unanimité syndicale et la communication à l'inspection sur demande restent intégrales.",
    "L2314-11 est une source du lot lue entièrement : troisième collège à vingt-cinq cadres assimilés, quel que soit l'effectif ; le dernier alinéa vise un titulaire et un suppléant dans un collège unique. L'erreur préexistante est expressément identifiée, non corrigée en silence. Aucun nouveau renvoi ou nouvelle catégorie n'est ajouté. L8112-1 demeure le renvoi existant à l'agent de contrôle ; le contrôle ponctuel sur demande n'est pas une transmission périodique redondante.",
    "La seule différence avec la source entière est la suppression de la localisation ordinale erronée du renvoi. Elle sécurise une garantie existante sans créer de collège, retirer une formalité ou diminuer un prélèvement.",
    "Aucun gain de coût ou de délai n'est démontré ; les conditions d'unanimité et le champ de l'accord restent inchangés et la correction ne rouvre pas des scrutins définitivement jugés.",
    "Aucune charge nouvelle n'est identifiée : mêmes signataires, conditions du troisième collège inchangées, et même communication seulement sur demande.",
    [effect('coordination', 'cse-renvoi-troisieme-college',
            "Retrait de l'indication d'alinéa erronée, sans modification des conditions légales du troisième collège.",
            "Le renvoi vise le dernier alinéa de L2314-11, consacré au collège unique et non au troisième collège.",
            "Le renvoi vise L2314-11, qui contient les conditions déjà existantes de constitution du troisième collège.",
            'other', "Parties à un accord modifiant les collèges électoraux et salariés concernés.",
            "Correction du renvoi sans rétroactivité ni réouverture des décisions définitives ; aucune nouvelle condition d'effectif.",
            "Aucune formalité ou condition nouvelle ; contrôle ponctuel existant conservé.",
            "L'accord conclu ne fait pas obstacle à la création du troisième collège dans les conditions prévues au dernier alinéa de l'article L. 2314-11.",
            "L'accord conclu ne fait pas obstacle à la création du troisième collège dans les conditions prévues à l'article L. 2314-11.")],
    classification='coordination_only')

retained('L2314-13',
    "Maintien intégral de la répartition négociée, de la mention de la proportion de femmes et d'hommes et de l'arbitrage en cas d'échec d'une négociation à laquelle au moins un syndicat a répondu. La donnée de proportion rend possible la représentation équilibrée des listes ; elle n'est pas un rapport annuel autonome. L'arbitrage et son recours protègent contre une répartition unilatérale litigieuse.",
    "L2314-6, L2314-11 et L2314-12 lus : doubles majorités, catégories et troisième collège sont conservés. R2314-3 lu intégralement : compétence territoriale, décision sous deux mois, notification avec recours, saisine du tribunal sous quinze jours et voie après silence. Le conflit préexistant avec la formule de L2314-14, qui ne vise que l'absence des syndicats représentatifs, est traité explicitement dans L2314-14 ; la présence d'un syndicat non représentatif ne doit pas neutraliser la règle du présent troisième alinéa. La suspension et la prorogation protègent la représentation pendant le différend.",
    "La source entière organise un accord ou un arbitrage utile, avec une donnée nécessaire aux listes équilibrées. Aucune procédure générale d'autorisation ni collecte redondante n'est supprimée, et aucune réduction n'est revendiquée.",
    "Le coût des différends et de l'arbitrage n'est pas chiffré. Le maintien ne vaut ni réécriture du règlement ni contrôle d'un accord ou d'une liste particulière.",
    "Aucune charge nouvelle n'est identifiée : même donnée par collège, même échec préalable de négociation et mêmes garanties de recours, sans déclaration annuelle ajoutée.")

xml = "<p>Lorsque aucune organisation syndicale n'a répondu à l'invitation à négocier de l'employeur, celui-ci répartit le personnel et les sièges entre les différents collèges électoraux.</p><p>La présente rédaction s'applique aux décisions de répartition prises à compter de son entrée en vigueur. Les décisions antérieures et les recours qui s'y rapportent demeurent régis par les dispositions qui leur étaient applicables.</p>"
rewritten('L2314-14', xml,
    "Coordination explicite d'une incohérence préexistante avec L2314-13 : réserver la répartition unilatérale à l'absence de réponse de toute organisation syndicale à l'invitation à négocier. L2314-13 impose déjà l'accord ou, en cas d'échec après réponse d'au moins un syndicat, la décision administrative. La rédaction source permettait simultanément une compétence patronale quand seul un syndicat non représentatif participait. La correction reprend le critère de réponse du troisième alinéa de L2314-13, sans supprimer une autorisation ou obligation et sans être présentée comme un allègement.",
    "Les invitations régulières restent celles de L2314-5 ; la double majorité de L2314-6 et les collèges de L2314-11/12 ne sont pas modifiés. La correction ne valide ni n'annule automatiquement les répartitions antérieures ou les décisions définitives. Pas de renvoi nouveau. Le critère de réponse correspond exactement au déclenchement prévu au troisième alinéa de L2314-13 : un désaccord après réponse ne peut être traité comme l'absence de réponse ; les faits doivent être établis, sans présumer un accord du silence ni supprimer les recours.",
    "La comparaison avec la source entière révèle une correction de compétence, non une simplification : le seul syndicat non représentatif participant ne peut plus être ignoré au titre de cet article alors que L2314-13 prévoyait déjà la voie négociée ou administrative.",
    "Aucune baisse de charge n'est démontrée. La lecture isolée de l'ancienne rédaction donnait un champ unilatéral plus large ; sa réduction est expressément reconnue, sans prétendre trancher rétroactivement les litiges antérieurs.",
    "Aucun dossier, délai ou arbitrage nouveau autonome n'est ajouté : la voie de L2314-13 existe déjà pour au moins un syndicat répondant. La correction restreint cependant la faculté patronale que pouvait suggérer la lecture isolée de la source ; son coût éventuel n'est pas chiffré.",
    [effect('coordination', 'cse-repartition-competences-syndicats',
            "Alignement du domaine de la répartition patronale sur le traitement déjà prévu de la participation syndicale.",
            "Répartition patronale prévue si aucun syndicat représentatif ne participe, malgré la compétence prévue à L2314-13 dès la réponse d'au moins un syndicat.",
            "Répartition patronale prévue si aucun syndicat n'a répondu à l'invitation ; dès réponse d'un syndicat, accord ou arbitrage selon L2314-13.",
            'other', "Employeurs et syndicats participant à la négociation de la répartition, notamment syndicats non représentatifs.",
            "Pas d'annulation automatique des décisions antérieures ; droits de recours et cas d'échec de négociation de L2314-13 préservés.",
            "Pas de procédure supplémentaire créée, mais limitation explicite de la lecture isolée de la compétence patronale antérieure.",
            "Lorsque aucune organisation syndicale représentative dans l'entreprise n'a pris part à la négociation, l'employeur répartit le personnel et les sièges entre les différents collèges électoraux.",
            "Lorsque aucune organisation syndicale n'a répondu à l'invitation à négocier de l'employeur, celui-ci répartit le personnel et les sièges entre les différents collèges électoraux.")],
    classification='coordination_only')

retained('L2314-15',
    "Maintien intégral de l'adaptation du protocole aux équipes successives et aux salariés isolés. La formule « s'il y a lieu » limite déjà l'obligation aux situations pertinentes ; elle garantit une possibilité effective de représentation, plutôt qu'un rapport ou agrément de convenance à supprimer.",
    "La conclusion demeure soumise à L2314-6 et à ses assiettes exactes. Les modalités concrètes ne sont pas imposées uniformément par la loi : aucune nouvelle plateforme, permanence ou consultation distincte n'est prescrite. L2232-12 proposé, lu dans le corpus, conserve expressément l'utilité de ces mesures pour la consultation des salariés ; leur suppression affaiblirait ce renvoi.",
    "Toute la source a une fonction ciblée d'égalité d'accès à la représentation et de négociation adaptée. Son maintien ne constitue pas une nouvelle obligation fusionnée ni une réduction de coût démontrée.",
    "Les situations de travail isolé et le contenu des protocoles restent à apprécier concrètement ; aucun effet chiffré sur la participation n'est établi.",
    "Aucune charge nouvelle n'est identifiée : les adaptations ne sont requises que s'il y a lieu, selon le protocole existant, sans formalité de remplacement.")

retained('L2314-16',
    "Maintien intégral de la faculté d'assurer une représentation équitable entre le personnel permanent et les salariés affectés aux missions de travail temporaire. Le texte ne prescrit aucun contrat de travail à terme : le personnel temporaire peut déjà relever d'un CDI et les missions peuvent rester limitées sous le contrat unique. Une reformulation de ces seuls mots ne serait pas une suppression de régime.",
    "L2314-11, L2314-12 et L2314-6 sont lus dans le lot : collèges, unanimité requise pour leur modification et majorité du protocole restent réservés. L2314-20, lu dans le corpus avec sa proposition, coordonne les périodes d'emploi des salariés temporaires au contrat unique et inclut les intermissions. Aucune nouvelle embauche à terme, rupture de fin de mission ou ancienneté remise à zéro ne découle de la présente faculté. Les droits des anciens contrats ne sont pas affectés.",
    "La source entière ouvre déjà une répartition adaptée sans imposer de comité ou siège supplémentaire. La conserver n'est pas une fusion nouvelle ; son vocabulaire professionnel n'autorise pas le retour des CDD.",
    "Les conditions électorales spéciales des salariés temporaires relèvent notamment de L2314-20 et ne sont pas abolies par les changements du régime général de L2314-18/19. Aucun gain financier n'est démontré ici.",
    "Aucune charge nouvelle n'est identifiée : même faculté de négocier la répartition, mêmes réserves de collèges et aucun registre de missions nouveau.")

retained('L2314-17',
    "Maintien intégral du contrôle électoral ordonné par le juge et de ses frais à la charge de l'employeur. Ce coût est lié à une mesure judiciaire ciblée de liberté et de sincérité du scrutin, non à un agrément systématique. Le supprimer ou le faire payer aux salariés affaiblirait le recours ou transférerait la charge sans réduction démontrée.",
    "La saisine est préalable aux élections et le juge décide de l'opportunité du dispositif ; aucun audit permanent n'est imposé. Les frais concernent les mesures effectivement ordonnées. Le renvoi de L2232-12 proposé à ce contrôle pour les consultations reste utile. Ne pas classer un changement de financeur comme une baisse de prélèvement.",
    "La source entière assure l'effectivité du contrôle judiciaire et son financement, sans formalité périodique identifiable à supprimer. Aucun allègement nouveau n'est attribué à son maintien.",
    "Le montant des frais dépend de la décision et n'est pas chiffré ; les voies procédurales hors de cet article restent à leur champ propre.",
    "Aucune charge nouvelle n'est identifiée : pas de contrôle systématique, frais additionnels ou obligation de certification ajoutés.")

xml = by_number['L2314-18']['source_xml'].replace(
    "âgés de seize ans révolus, travaillant depuis trois mois au moins dans l'entreprise et", "âgés de seize ans révolus et")
xml = xml.replace("l'ensemble des salariés âgés de seize ans", "l'ensemble des salariés de l'entreprise âgés de seize ans")
xml += "<p>La suppression de la condition générale d'ancienneté ne modifie pas les conditions spéciales applicables aux salariés temporaires, aux salariés en portage salarial ou aux salariés mis à disposition. Elle s'applique aux processus électoraux engagés à compter de l'entrée en vigueur de la présente rédaction. Les élections partielles destinées à compléter un mandat issu d'un scrutin engagé avant cette entrée en vigueur demeurent régies par les règles applicables à ce scrutin. Les opérations déjà engagées et les recours qui s'y rapportent demeurent régis par les dispositions antérieures.</p>"
rewritten('L2314-18', xml,
    "Réduction de fond de la condition d'accès au vote : supprimer les trois mois d'attente du régime général. L'existence d'une relation salariée dans l'entreprise établit déjà l'appartenance au corps électoral ; aucune utilité essentielle d'un délai supplémentaire uniforme n'est démontrée. Conserver intégralement l'âge de seize ans et les exclusions civiques ; ne pas supprimer les règles spéciales par incidence implicite.",
    "L2314-20, L2314-23 et L2314-24 ont été lus : ancienneté spéciale des temporaires, présence et choix de vote des salariés mis à disposition, conditions propres du portage. Leur régime demeure distinct ; aucun renvoi numéroté nouveau n'est créé. L2314-25 reste utile pour les conditions spéciales et n'est pas abrogé implicitement. Le renvoi de L2232-12 proposé à la qualité d'électeur produit une extension du groupe pouvant voter dans les futures consultations, sans changer ses pourcentages ni leur assiette de suffrages exprimés ; cette incidence est intentionnelle et n'est pas comptée comme une deuxième suppression. Les listes et scrutins déjà engagés ne sont pas refaits. L'âge d'éligibilité de dix-huit ans et les exclusions d'indépendance de L2314-19 demeurent distincts.",
    "Par rapport à la source entière, les salariés du régime général peuvent voter sans attendre trois mois d'emploi. Il s'agit d'une condition restrictive effectivement retirée et d'un droit élargi, non d'une baisse de taxe ou d'un simple changement de mots.",
    "La mesure ne couvre pas les anciennetés et présences des régimes spéciaux, ni les scrutins déjà engagés. L'augmentation possible de la taille des listes et le coût net de l'organisation du vote ne sont pas chiffrés.",
    "Aucune formalité autonome nouvelle n'est créée : l'employeur utilise les listes électorales existantes sans nouvelle attestation d'ancienneté. Leur champ s'élargit aux salariés récents ; cela peut augmenter le traitement des listes et les moyens de vote, avec solde de coût inconnu.",
    [effect('relief_extended', 'cse-droits-electoraux-sans-anciennete-generale',
            "Ouverture du vote aux salariés récents du régime général sans condition d'ancienneté de trois mois.",
            "Salariés de seize ans révolus avec au moins trois mois de travail dans l'entreprise et sans incapacité civique ; conditions spéciales distinctes.",
            "Salariés de seize ans révolus sans condition générale de durée d'emploi, avec mêmes exclusions civiques et mêmes réserves des régimes spéciaux.",
            'legal_duty', "Salariés du régime électoral général, notamment embauchés depuis moins de trois mois.",
            "Processus électoraux engagés après l'entrée en vigueur ; opérations et recours antérieurs conservés ; régimes temporaires, portage et mise à disposition non modifiés.",
            "Pas de dossier nouveau ; élargissement des listes et du nombre de votants possible, avec coûts non mesurés.",
            "travaillant depuis trois mois au moins dans l'entreprise",
            "Sont électeurs l'ensemble des salariés de l'entreprise âgés de seize ans révolus et n'ayant fait l'objet d'aucune interdiction, déchéance ou incapacité relative à leurs droits civiques.")],
    removed=["Condition générale de trois mois de travail dans l'entreprise pour accéder à l'électorat, sans suppression des conditions spéciales autonomes."])

xml = by_number['L2314-19']['source_xml'].replace(
    "âgés de dix-huit ans révolus, et travaillant dans l'entreprise depuis un an au moins,", "âgés de dix-huit ans révolus,")
xml = xml.replace("Les salariés travaillant à temps partiel simultanément dans plusieurs entreprises ne sont éligibles que dans l'une de ces entreprises. Ils choisissent celle dans laquelle ils font acte de candidature.",
                  "Les salariés travaillant à temps partiel simultanément dans plusieurs entreprises peuvent être candidats et élus dans chacune d'elles dès lors qu'ils y remplissent les conditions d'éligibilité.")
xml += "<p>La suppression de la condition générale d'ancienneté ne modifie pas les conditions spéciales applicables aux salariés temporaires, aux salariés en portage salarial ou aux salariés mis à disposition. La possibilité de candidatures dans plusieurs entreprises concerne les salariés qui sont liés à chacune d'elles par un contrat de travail et ne supprime aucune incompatibilité fondée sur une autre disposition. Ces dispositions s'appliquent aux processus électoraux engagés à compter de l'entrée en vigueur de la présente rédaction. Les élections partielles destinées à compléter un mandat issu d'un scrutin engagé avant cette entrée en vigueur demeurent régies par les règles applicables à ce scrutin. Les opérations déjà engagées, les mandats en cours et les recours qui s'y rapportent demeurent régis par les dispositions antérieures.</p>"
rewritten('L2314-19', xml,
    "Réduction de fond de deux restrictions sans fonction essentielle démontrée : retirer l'année d'ancienneté supplémentaire pour être candidat dans le régime général et l'obligation du salarié à temps partiel multiemployeur de choisir une seule entreprise. Les électeurs choisissent leurs représentants ; l'âge de dix-huit ans, les exclusions familiales et les exclusions liées à l'autorité patronale protègent déjà l'indépendance. La qualité d'électeur, les régimes spéciaux et les incompatibilités autonomes demeurent.",
    "L2314-18 du lot supprime l'attente électorale générale sans modifier les exclusions civiques ; L2314-2, lu dans le lot, reprend les conditions d'éligibilité pour la désignation syndicale, incidence à dédupliquer. L2314-20/23/24/25 lus dans le corpus : les règles spéciales et leurs dérogations favorables restent ouvertes aux futurs intéressés. La candidature multiple concerne plusieurs contrats directs ; elle ne rend pas éligible le salarié seulement mis à disposition dans l'entreprise utilisatrice et ne supprime pas le choix de vote prévu par L2314-23. Le représentant de l'employeur et ses proches énumérés restent inéligibles. Aucune proratisation de l'ancienneté liée à l'indemnité de rupture n'est importée ici. Les sièges, heures de délégation et protections demeurent ceux de chaque mandat légalement obtenu ; pas de cumul artificiel d'une même heure de travail rémunérée sur le seul fondement de cet article.",
    "Toute la source est comparée : suppression de l'année d'attente générale et de l'exclusivité de candidature multiemployeur, avec maintien de toutes les exclusions d'indépendance. Ce sont des accès aux fonctions élargis, sans baisse de prélèvement ni suppression d'un moyen de représentation.",
    "Les conditions spéciales et les processus électoraux antérieurs ne sont pas couverts. Davantage de candidatures ou de mandats peuvent augmenter les coûts de vote et de représentation ; aucune réduction nette de coût ni effet sur l'emploi n'est chiffré.",
    "Aucun formulaire, registre ou quota nouveau n'est créé et aucun mandat supplémentaire n'est imposé. Les mandats que des salariés supplémentaires peuvent obtenir entraînent les obligations de protection et de moyens déjà attachées à ces mandats ; cette extension possible de champ est identifiée, sans solde de coût présumé.",
    [effect('relief_extended', 'cse-droits-electoraux-sans-anciennete-generale',
            "Suppression de l'année d'ancienneté générale pour l'éligibilité, composante distincte de l'ouverture de l'électorat à L2314-18.",
            "Électeurs de dix-huit ans révolus, avec au moins un an de travail dans l'entreprise, sous exclusions familiales et d'autorité patronale.",
            "Électeurs de dix-huit ans révolus sans année générale d'attente, sous les mêmes exclusions et conditions spéciales autonomes.",
            'legal_duty', "Salariés du régime général souhaitant être candidats avant un an d'emploi.",
            "Processus électoraux nouveaux ; mandats, opérations et recours antérieurs préservés ; régimes spéciaux non supprimés.",
            "Pas de formalité remplaçante ; possible extension du nombre de candidats et de bénéficiaires des protections de mandat, coût non chiffré.",
            "travaillant dans l'entreprise depuis un an au moins",
            "Sont éligibles les électeurs âgés de dix-huit ans révolus, à l'exception des conjoint, partenaire d'un pacte civil de solidarité, concubin, ascendants, descendants, frères, sœurs et alliés au même degré de l'employeur"),
     effect('obligation_removed', 'cse-multiemploi-fin-candidature-exclusive',
            "Retrait du choix obligatoire d'une seule entreprise de candidature pour le salarié à temps partiel multiemployeur.",
            "Salarié à temps partiel simultanément dans plusieurs entreprises éligible dans une seule, qu'il doit choisir pour candidater.",
            "Candidature et élection possibles dans chaque entreprise où le salarié dispose d'un contrat et satisfait aux conditions applicables, sous incompatibilités autonomes.",
            'legal_duty', "Salariés à temps partiel liés simultanément par des contrats de travail à plusieurs entreprises.",
            "Processus électoraux nouveaux ; pas de modification automatique des mandats en cours ou des décisions antérieures ; mise à disposition distincte.",
            "Aucun enregistrement de choix de remplacement ; les protections et moyens de mandats effectivement obtenus restent dus et leur coût éventuel n'est pas établi.",
            "Les salariés travaillant à temps partiel simultanément dans plusieurs entreprises ne sont éligibles que dans l'une de ces entreprises. Ils choisissent celle dans laquelle ils font acte de candidature.",
            "Les salariés travaillant à temps partiel simultanément dans plusieurs entreprises peuvent être candidats et élus dans chacune d'elles dès lors qu'ils y remplissent les conditions d'éligibilité.")],
    removed=["Condition générale d'un an de travail dans l'entreprise pour être éligible, sans effacement des régimes spéciaux ni des exclusions d'indépendance.",
             "Exclusivité de l'éligibilité dans une seule entreprise et obligation correspondante de choix pour le salarié à temps partiel multiemployeur."])

answers['L2314-5']['review_notes'] += " D2314-1-1 a été lu entier : les trois rubriques de contenu et son renvoi à la première réunion du quatrième alinéa restent opérants. L2314-29 conserve le champ des syndicats des deux premiers alinéas. L2317-1 a été lu ; la transition réserve expressément l'application de la loi pénale plus douce pour les contraintes retirées."
answers['L2314-9']['review_notes'] += " L2317-1, D1233-10 et D1237-9 ont été lus entièrement : les sanctions distinctes et les pièces des procédures collectives gardent leur champ, sans compter leur réemploi éventuel comme une seconde suppression. Le pluriel « ces articles » de D1233-10, malgré le seul L2314-9 cité, est une anomalie source signalée, sans correction implicite de ce règlement. La nouvelle tâche du collecteur sur les documents déjà reçus est limitée aux transmissions non échues et futures visées par la transition, sans reprise générale des archives."
answers['L2314-19']['review_notes'] += " L2232-28, lu entier, renvoie au premier alinéa pour les apparentés à l'employeur : ce premier alinéa et toute son énumération sont conservés à leur emplacement, sans élargir les personnes pouvant recevoir ce mandat syndical."

# Les cibles requises ne sont pas toutes des renvois exprès du texte source.
# Leur analyse reste individuelle ; aucune cible n'est ajoutée par analogie.
eligibility_checks = {
    'L1234-1': "La source de L1234-1 réserve les préavis de licenciement, hors faute grave, selon une ancienneté inférieure à six mois, de six mois à moins de deux ans, ou d'au moins deux ans, avec règles plus favorables. Sa proposition applique quinze jours calendaires aux contrats nouveaux sans condition d'ancienneté et conserve le régime des anciens contrats ; la coordination prévoit une notification écrite dont le lendemain de la présentation ou de la réception ouvre le décompte. L2314-19 n'y renvoie pas : retirer l'ancienneté électorale d'un an ne modifie ni cette notification ni le préavis, et une rupture notifiée ne fait pas, à elle seule, disparaître une relation de travail avant sa fin effective. Les autorisations protectrices restent distinctes.",
    'L1221-2': "La source de L1221-2 admet des contrats à terme à côté du CDI ; sa proposition, qui n'est pas le droit en vigueur, impose le contrat unique sans terme aux nouvelles embauches et conserve les droits des contrats antérieurs. L2314-19 ne renvoie pas à cette cible : l'éligibilité générale reste ouverte aux électeurs employés dans l'entreprise, qu'ils relèvent d'un ancien contrat encore en cours ou du futur contrat unique. La suppression de l'année d'attente et du choix d'une seule entreprise ne transforme pas une durée de mission, de formation ou de mandat en terme de l'emploi. Les conditions spéciales de l'intérim, du portage et de la mise à disposition restent expressément réservées et ne sont pas attribuées au contrat privé ordinaire.",
    'L1234-9': "La source de L1234-9 ouvre l'indemnité de licenciement du CDI après huit mois, sauf faute grave ; sa proposition distingue nouveaux et anciens contrats et ne régit aucune condition d'éligibilité au CSE. Pour un contrat unique nouveau rompu par l'employeur, son seuil d'un an se mesure au terme effectif, préavis exécuté ou non inclus ; une fois atteint, le calcul porte sur toute l'ancienneté, à 0,20 mois par année, fractions au prorata des mois complets et plafond de six mois, sous l'exception de faute grave prévue par cette cible. La démission n'ouvre pas cette indemnité. L2314-19 ne cite pas cette règle : supprimer son année électorale ne supprime ni seuil indemnitaire ni notification de rupture. La composante antérieure, les indemnités plus favorables, les congés, salaires, réparations d'une illégalité et indemnités spéciales restent dans leur champ, sans compter deux fois une même période."
}
a = answers['L2314-19']
key = a['code_id'] + '|' + a['source_id']
for target_key in refs['requirements'][key]:
    t = refs['targets'][target_key]
    a['reference_checks'].append(dict(target_key=target_key,
                                    view_sha256=t['view_sha256'],
                                    assessment=eligibility_checks[t['number']]))

answers['L2314-19']['review_notes'] += " Les trois cibles requises sont examinées individuellement dans reference_checks, même si aucun de ces trois numéros n'est cité dans le texte source. Leur vue proposée est distinguée du droit officiel ; aucune condition électorale n'est déduite du seuil indemnitaire et aucune fin automatique d'emploi n'est créée. Le point de départ du préavis est repris de la décision travail de coordination.json, sans introduire de renvoi nouveau à une cible non fournie."

# Le retrait d'une attente ou d'une exclusivité élargit des droits collectifs.
# En présenter aussi l'incidence sur le champ des obligations de l'employeur.
for number in ('L2314-18', 'L2314-19'):
    answers[number]['substantive_impact']['classification'] = 'mixed'
    answers[number]['substantive_impact']['assessment'] += " L'élargissement des bénéficiaires étend corrélativement le champ des obligations électorales et, pour les mandats obtenus, des moyens et protections existants : classement mixte, sans réduction nette de coût démontrée."

answers['L2314-18']['substantive_impact']['new_burdens_review'] = "Aucun formulaire, registre, justificatif ou délai nouveau n'est créé. Le retrait des trois mois étend toutefois aux salariés récents le champ des obligations existantes d'établissement des listes et d'organisation du vote. Cette extension de traitement constitue une charge possible pour l'employeur ; elle accompagne l'ouverture du droit et ne permet pas d'affirmer une réduction nette de coût."
answers['L2314-19']['substantive_impact']['new_burdens_review'] = "Aucun formulaire, registre ou quota nouveau n'est créé et aucun mandat supplémentaire n'est imposé. Le retrait de l'attente et de l'exclusivité ouvre cependant les candidatures à de nouveaux salariés et permet plusieurs mandats directs. Chaque mandat effectivement obtenu entraîne les moyens, rémunérations et protections déjà prévus pour celui-ci ; le champ potentiel des obligations patronales s'élargit, sans solde net de coût établi."

answers['L2314-18']['substantive_impact']['effects'].append(effect(
    'obligation_added', 'cse-droits-electoraux-sans-anciennete-generale',
    "Extension du champ des obligations électorales existantes aux salariés récents ; contrepartie de l'ouverture du vote, non formalité autonome supplémentaire.",
    "Le régime général limite le corps électoral aux salariés ayant au moins trois mois d'emploi dans l'entreprise, sous âge et capacité civique.",
    "Le corps électoral général inclut aussi les salariés de moins de trois mois d'emploi remplissant les autres conditions ; listes et moyens de vote doivent les inclure.",
    'legal_duty', "Employeurs soumis aux élections du CSE et salariés récents du régime général.",
    "Même transition que l'ouverture du droit : nouveaux processus électoraux, sous réserves expresses des régimes spéciaux et des élections partielles des mandats anciens.",
    "Extension du traitement des listes et du vote, sans document, donnée, registre ou procédure distincte ; coût net non établi.",
    "travaillant depuis trois mois au moins dans l'entreprise",
    "Sont électeurs l'ensemble des salariés de l'entreprise âgés de seize ans révolus"))

answers['L2314-19']['substantive_impact']['effects'].append(effect(
    'obligation_added', 'cse-multiemploi-fin-candidature-exclusive',
    "Extension possible des obligations attachées aux mandats auprès de plusieurs employeurs directs, contrepartie de la fin du choix exclusif de candidature.",
    "Un salarié à temps partiel multiemployeur ne peut être élu que dans une seule entreprise choisie pour sa candidature.",
    "Il peut être candidat et élu chez chacun de ses employeurs directs où il satisfait aux conditions ; chaque mandat effectivement obtenu garde ses moyens et protections propres.",
    'legal_duty', "Employeurs directs d'un salarié à temps partiel élu auprès de plusieurs d'entre eux ; salariés titulaires de ces mandats.",
    "Nouveaux processus électoraux ; incompatibilités autonomes et règles spéciales maintenues, sans cumul artificiel d'une même heure rémunérée créé par cet article.",
    "Pas de déclaration de remplacement ; extension potentielle des bénéficiaires des obligations de mandat existantes, sans réduction nette de coût affirmée.",
    "Les salariés travaillant à temps partiel simultanément dans plusieurs entreprises ne sont éligibles que dans l'une de ces entreprises.",
    "Les salariés travaillant à temps partiel simultanément dans plusieurs entreprises peuvent être candidats et élus dans chacune d'elles dès lors qu'ils y remplissent les conditions d'éligibilité."))

for number in ('L2314-18', 'L2314-19'):
    answers[number]['review_notes'] += " L2314-21 a aussi été lu en entier : les trois et six mois propres au portage et les périodes de référence ne sont pas modifiés ici. La transition réserve expressément les élections partielles d'un mandat provenant d'un scrutin antérieur, pour rendre cohérente la base conservée par L2314-10 ; elle ne rétablit pas l'attente pour les nouveaux cycles électoraux."
    answers[number]['substantive_impact']['scope_limitations'] += " Les élections partielles complétant un mandat issu d'un scrutin antérieur gardent également leur base antérieure."
    for e in answers[number]['substantive_impact']['effects']:
        e['conditions_and_transition'] += " Les partielles complétant un mandat issu d'un scrutin antérieur gardent les règles de ce scrutin."

output = [answers[s['number']] for s in sources]
Path('answer.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
print('Écriture :', len(output), 'articles,', Path('answer.json').stat().st_size, 'octets')
