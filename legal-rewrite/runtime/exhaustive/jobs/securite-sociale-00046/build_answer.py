import json
import re
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sources = json.loads((ROOT / 'source.json').read_text())
refs = json.loads((ROOT / 'reference-targets.json').read_text())
by_number = {s['number']: s for s in sources}
answers = {}


def plain(xml):
    return unescape(re.sub(r'<[^>]+>', '', xml or ''))


def impact(classification, assessment, limits, burdens, effects=None):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=limits, new_burdens_review=burdens, effects=effects or [])


def entry(number, reason, notes, assessment, limits):
    s = by_number[number]
    a = {k: s[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    a.update(proposed_xml=None, reason=reason, review_notes=notes,
             status='retained_unchanged', classification='retained_necessary',
             substantive_impact=impact('retained_necessary', assessment, limits,
                 'Aucune charge nouvelle identifiée : le texte officiel est maintenu intégralement, sans nouvelle formalité, donnée, condition ni délai.'))
    answers[number] = a
    return a


def effect(kind, measure, description, before, after, unit, population, transition, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure, description=description, before=before,
                after=after, unit=unit, affected_population=population,
                conditions_and_transition=transition, replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


entry('L243-6-7',
      "Réforme de fond : suppression de l'approbation ministérielle de la convention de contrôle commun et de son renouvellement légal quinquennal. La convention demeure nécessaire pour coordonner les organismes, empêcher les vérifications concomitantes d'une même donnée et organiser les corrections contradictoires. Les autres dispositions sont intégralement conservées ; aucune déclaration ne remplace le visa supprimé.",
      "Conserver les cinq alinéas et les 1° et 2° à leur place. Les conventions en cours continuent sans renouvellement imposé et leurs opérations antérieures ne sont pas remises en cause. L'assiette, le plafond et les allègements visés conservent leurs champs et transitions propres ; le calcul annuel d'un allègement social ne rétablit pas l'annualité de l'IS. L'arrêté d'approbation et les stipulations d'exécution imposant son renouvellement devront être coordonnés, sans rétablir de visa. Aucun coût public ou rendement n'est chiffré.",
      'La durée de cinq ans et le visa ministériel sont les deux contraintes effectivement retirées ; les traitements communs et garanties de correction ne sont pas abrogés.',
      'Les obligations déclaratives de DSN, les contributions principales et les décisions individuelles ne sont pas supprimées. La suppression du visa ne vaut pas examen des autres conventions du corpus.')
a = answers['L243-6-7']
old = by_number['L243-6-7']['source_xml']
new = old.replace('Une convention conclue pour cinq ans entre', 'Une convention conclue pour une durée indéterminée entre', 1)
new = new.replace(" et approuvée par arrêté des ministres chargés de la sécurité sociale et de l'agriculture", '', 1)
new += "<p>La conclusion, la modification et le remplacement de cette convention ne sont soumis à aucune approbation ministérielle. Les conventions en vigueur à la date d'entrée en vigueur de la loi demeurent applicables sans renouvellement obligatoire à leur échéance, jusqu'à leur modification ou leur remplacement par les parties. Les opérations déjà accomplies et les garanties des cotisants sont préservées. Aucune déclaration de remplacement n'est exigée.</p>"
a.update(proposed_xml=new, status='rewrite_draft', change_type='normative_reduction',
         reform_policy_id='editorial_direction_2026_10_19',
         removed_provisions=["L'approbation par arrêté ministériel de la convention de contrôle commun et de ses modifications.",
                             'La limitation légale de la convention à cinq ans et le renouvellement obligatoire qui en résulte.'])
a.pop('classification')
a['substantive_impact']['classification'] = 'material_reduction'
a['substantive_impact']['new_burdens_review'] = "Aucune charge nouvelle identifiée : la convention existe déjà, son champ et ses participants sont conservés, sans déclaration, registre ni visa de remplacement. Les parties conservent la possibilité de la modifier ou de la remplacer."
first_old = re.findall(r'<p>(.*?)</p>', old, re.S)[0]
first_new = re.findall(r'<p>(.*?)</p>', new, re.S)[0]
a['substantive_impact']['effects'] = [
    effect('authorization_removed', 'controle-commun-convention-sans-visa-renouvellement',
           "Suppression du visa ministériel de la convention commune, sans dépôt de remplacement.",
           "Convention entre les fédérations mandatées, l'Acoss et la caisse centrale de MSA soumise à approbation par arrêté ministériel.",
           "Même convention organisant les contrôles communs, sans approbation ministérielle pour sa conclusion, sa modification ou son remplacement.",
           'legal_duty', 'Organismes et représentants parties à la convention ; employeurs concernés par les vérifications communes.',
           "Dès l'entrée en vigueur ; continuité des conventions en cours et des opérations antérieures.",
           'Aucune déclaration, autorisation ou donnée supplémentaire ; coordination contradictoire et absence de vérification concomitante maintenues.',
           plain(first_old), "La conclusion, la modification et le remplacement de cette convention ne sont soumis à aucune approbation ministérielle."),
    effect('obligation_removed', 'controle-commun-convention-sans-visa-renouvellement',
           "Suppression du renouvellement légal tous les cinq ans de la même convention.",
           'Convention légalement conclue pour cinq ans, imposant son renouvellement pour poursuivre ce cadre commun.',
           'Convention à durée indéterminée ; anciennes conventions continuées sans renouvellement obligatoire à leur échéance.',
           'legal_duty', 'Les mêmes parties à la convention de contrôle commun.',
           "Conventions nouvelles et conventions en vigueur à l'entrée en vigueur, sans remise en cause des opérations accomplies.",
           "Aucune périodicité ou procédure de renouvellement de remplacement ; modification ou remplacement par les parties restent possibles.",
           plain(first_old), plain(first_new))]

entry('L243-6-8',
      "Maintien intégral utile : la faculté de faire accomplir toute démarche de cette section par un tiers évite une comparution ou une intervention personnelle obligatoire du cotisant, y compris futur. Aucun agrément ni justificatif supplémentaire n'est créé par cet article ; retirer cette faculté alourdirait les démarches. Aucune reformulation à droit constant n'est proposée.",
      "La note d'entrée en application au 1er janvier 2019 est historique ; elle ne fixe pas la date de la réforme future. Le mandat porte sur les démarches de cette section et ne remplace ni les droits de défense ni les conditions propres aux actes. Aucun lien avec le terme du contrat de travail.",
      "La représentation par un tiers est un allègement déjà présent dans la source entière ; son maintien ne constitue pas une nouvelle obligation supprimée.",
      "Le texte n'ouvre pas un accès général aux données du cotisant et ne modifie pas les régimes de cotisations ou les conditions autonomes de représentation.")

entry('L243-7',
      "Maintien intégral nécessaire des compétences et garanties de contrôle. Les éléments motivés exigés pour contrôler une personne morale tierce, l'assermentation et l'agrément des agents, la preuve contraire et la séparation du contrôle de la Cour des comptes protègent contre les contrôles arbitraires et la fraude. L'agrément concerne l'habilitation des agents investis de pouvoirs de contrôle, non une autorisation d'activité du cotisant ; sa suppression n'est pas justifiée. Aucun prélèvement accessoire autonome n'est institué ici.",
      "Le champ inclut les employeurs publics et privés, les indépendants et les déclarants du III 3° de L133-8-4 ; il ne se réduit pas aux salariés privés du contrat unique. Le deuxième alinéa conserve les règles, garanties et sanctions du régime général pour les régimes du titre Ier du livre VII sous les réserves réglementaires. Les montants effectivement contrôlables suivent les réformes d'assiette et de cotisation dans leurs articles propres, sans recréer une dette supprimée.",
      "La source entière organise le contrôle et ses garanties, sans taxe ni déclaration périodique propre à retirer. Le maintien ne compte pas comme simplification ou baisse de prélèvements.",
      "Les compétences de contrôle ne prouvent pas la légalité de chaque redressement ; les exonérations, prescriptions, procédures contradictoires et recours de leurs régimes restent à appliquer.")
answers['L243-7']['benefit_review'] = "L'article n'accorde ni taux réduit ni exonération fiscale ou sociale autonome. Ses avantages procéduraux possibles sont la nécessité d'éléments motivés pour étendre le contrôle à une personne morale non inscrite, la qualification et l'assermentation des agents, la faculté de rapporter la preuve contraire, les garanties du régime général au deuxième alinéa et la séparation du contrôle des cotisations de la Cour des comptes. Tous sont intégralement maintenus, pour les contrôles futurs aussi. Le renvoi au III 3° de L133-8-4 ne ferme pas l'accès au dispositif de paiement des services ; les exclusions d'assiette et allègements de L242-1 demeurent opposables au calcul contrôlé."

entry('L243-7-1 A',
      "Maintien intégral nécessaire de la lettre d'observations et de la période contradictoire avant recouvrement. La lettre vaut déjà notification et invitation dans le régime particulier de L133-8-7 : cette fusion favorable ne doit pas disparaître. La prolongation demandée avant l'expiration du délai protège la défense ; les exclusions ciblent les indus de ce dispositif et quatre infractions de travail illégal. Leur retrait n'est pas nécessaire à une simplification des pièces et modifierait les délais de recouvrement et de prescription sans coordination de fond décidée.",
      "Maintenir l'ordre des deux alinéas et les renvois à L244-2 et L133-8-7. Les 1° à 4° de L8211-1 visent travail dissimulé, marchandage, prêt illicite et emploi d'étranger non autorisé, non les règles de préavis. L244-3 suspend la prescription pendant cette période ; aucune extension automatique de son délai n'est introduite. La note du 1er janvier 2024 reste historique.",
      "Les garanties contradictoires et la notification déjà fusionnée sont maintenues telles qu'elles existent ; aucun nouveau gain de délai ou suppression de notification n'est revendiqué.",
      "L'article ne fixe pas le préavis individuel de rupture ni sa notification. Les durées réglementaires du contradictoire et les voies de recours ne sont pas modifiées.")

entry('L243-7-1',
      "Maintien intégral utile de l'échange réciproque de renseignements nécessaires entre agents de contrôle français et étrangers. Ce pouvoir évite de nouvelles collectes lorsque l'information existe, mais n'établit pas à lui seul une dispense nouvelle de justificatif. La nécessité des données et la réciprocité bornent ce mécanisme antifraude et de détermination des droits ; aucune déclaration ou autorisation privée n'est imposée par cette disposition.",
      "La réciprocité et la nécessité des renseignements restent cumulatives. Ce texte ne permet pas de méconnaître les secrets protégés, les règles européennes de protection des données ou les conventions applicables. Aucun nouveau destinataire ni flux de données n'est ajouté.",
      "Le mécanisme d'échange existe déjà dans la source ; sa conservation ne démontre ni une nouvelle suppression de collecte ni une baisse de cotisations.",
      "La disponibilité et la licéité de chaque échange restent à établir dans son contexte ; aucun accès international général ou économie de contrôle n'est présumé.")

entry('L243-7-2',
      "Maintien intégral nécessaire du dispositif d'abus de droit : actes fictifs ou objectif exclusivement éludant à l'encontre de la finalité des textes. La pénalité de 20 % sanctionne cet abus caractérisé et n'est pas une cotisation accessoire ordinaire ; sa fonction antifraude est identifiée. La charge de la preuve sur l'organisme et l'exclusion liée à une saisine préalable utile restée sans réponse dans les délais protègent le cotisant. Supprimer cette exclusion au nom de la simplification retirerait un avantage futur.",
      "Préserver les quatre alinéas utiles et leur ordre ; l'alinéa vide ne porte pas de règle. Le renvoi à L752-1 désigne les organismes ultramarins, dont les fonctions de recouvrement sont précisées par L752-4 6° ; il n'est pas transformé en régime de contrat privé. L243-6-3 II conserve les effets du silence et III l'opposabilité ; la suppression projetée de son seul rapport IV ne les affecte pas. Contrôle de la portée de L243-6-1 sur les interprétations contradictoires, sans le confondre avec un nouveau rescrit.",
      "Le maintien protège contre la fraude tout en conservant les garanties de preuve et de saisine préalable déjà inscrites. Aucun nouvel allègement matériel n'est compté.",
      "Une optimisation réellement conforme à l'objet des textes ne devient pas un abus par cette rédaction inchangée ; la qualification et le montant de chaque sanction restent contestables.")

entry('L243-7-3',
      "Maintien intégral nécessaire de la responsabilité subsidiaire et solidaire de la société mère ou holding après constat de travail dissimulé par procès-verbal. Elle empêche que l'organisation d'un groupe rende irrécouvrables les cotisations et sanctions de la fraude. Ce n'est ni une responsabilité générale de tous les groupes ni un nouveau prélèvement. Les liens de dépendance ou contrôle et le constat formalisé demeurent requis.",
      "Les articles L233-1 et L233-3 du code de commerce définissent le lien de groupe ; ils ne sont pas réécrits dans ce lot. La solidarité ne doit porter que sur les cotisations, contributions, majorations et pénalités légalement dues après les suppressions et transitions applicables, notamment l'abrogation proposée de L243-7-6.",
      "La garantie de recouvrement en cas de travail dissimulé est conservée, sans élargissement de population ni prétendue réduction de prélèvement.",
      "Aucune solidarité nouvelle pour une simple erreur ou pour tous les contrats d'un groupe n'est créée ; les droits de contestation et les limites de la dette principale subsistent.")

entry('L243-7-4',
      "Maintien intégral utile du réemploi de documents recueillis lors du contrôle d'une autre personne du groupe, avec information sur leur teneur et origine et copie sur demande après indication de cette faculté. Supprimer l'information ou la copie ferait perdre une garantie de défense ; imposer une copie systématique créerait une obligation administrative supplémentaire sans utilité démontrée ici. L'article n'impose aucun registre de groupe ni nouveau dépôt privé.",
      "Préserver la définition du groupe par L233-1 et L233-3 du code de commerce, les deux garanties d'information et de communication et l'habilitation réglementaire. Le réemploi de données dans un contrôle ne vaut pas droit illimité d'échange ou de collecte. La source vise les renseignements effectivement obtenus, non une présomption d'identité de situation des sociétés.",
      "La faculté de réemploi et ses garanties sont déjà dans la source officielle ; aucune seconde suppression de pièces n'est attribuée à leur maintien.",
      "Le respect des secrets, des droits des tiers et du contradictoire doit être apprécié pour chaque document utilisé ; les frais ou gains nets de contrôle ne sont pas mesurés.")

entry('L243-7-5',
      "Maintien intégral nécessaire de la faculté de redresser et recouvrer les cotisations dues sur les informations des procès-verbaux de travail dissimulé établis par les agents compétents. Ce réemploi évite de recommencer la constatation de l'infraction et ne crée pas une déclaration supplémentaire du cotisant. La fonction antifraude est essentielle ; ni le principal ni les garanties de procédure ne sont écartés.",
      "Le renvoi à L8271-1-2 du code du travail porte sur les agents compétents en matière de travail illégal, non sur les conditions de rupture des contrats. Les informations du procès-verbal ne dispensent pas d'appliquer la procédure contradictoire du redressement et les prescriptions. Ne recouvrer que les sommes restant légalement dues.",
      "Le redressement fondé sur des procès-verbaux déjà transmis est une faculté existante maintenue, sans nouvelle obligation ou taxe supprimée.",
      "Le maintien ne valide pas le montant d'un procès-verbal ni l'assiette d'une indemnité de rupture ; les exonérations et recours restent à leur champ propre.")

entry('L243-7-6',
      "Réforme de fond : suppression intégrale de la majoration automatique de 10 % du redressement pour absence de mise en conformité, applicable même lorsque les observations antérieures n'avaient donné lieu à aucun redressement. Cette sanction accessoire de répétition est retirée sans diminuer le principal, supprimer le contrôle ni effacer les sanctions autonomes de fraude, de travail dissimulé ou les majorations ordinaires de retard. Une simple reformulation n'aurait pas retiré ce coût.",
      "Coordonner R243-18, lu dans le corpus, qui exécute cette majoration avec une fenêtre de six ans, et le 2° de R243-19 qui la vise parmi les sanctions liquidables ; aucune nouvelle sanction ne doit remplacer la même majoration. Ces règlements sont hors du présent lot et ne sont pas déclarés réécrits. Conserver le traitement des décisions antérieures définitives et l'application de la loi répressive plus douce aux sanctions non définitives selon sa portée. Perte de recettes de sanctions non chiffrée, sans compensation inventée.",
      "Le coût accessoire de 10 % du montant redressé au titre de la non-conformité réitérée est effectivement supprimé pour l'avenir ; ce n'est pas une baisse du taux des cotisations sociales.",
      "Le principal, les sanctions reposant sur un fondement autonome et les majorations ordinaires de paiement restent dus dans leur champ. Aucun remboursement général des sanctions définitives n'est décidé.")
a = answers['L243-7-6']
a.update(proposed_xml="<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi.</p><p>Aucune majoration de 10 % pour absence de mise en conformité ne peut être prononcée sur son fondement à compter de cette date, même lorsque les observations antérieures ou le contrôle sont antérieurs à celle-ci. Aucune mise en conformité ni déclaration de remplacement n'est exigée sur ce seul fondement.</p><p>Les majorations devenues définitives avant cette date demeurent soumises aux règles de recouvrement, de restitution, de prescription et de recours qui leur sont applicables. Les sanctions non définitives bénéficient de la loi répressive plus douce dans les conditions prévues par la loi. Aucune restitution générale des majorations légalement devenues définitives n'est créée.</p><p>Cette abrogation ne modifie ni les cotisations et contributions principales légalement dues, ni les pouvoirs de contrôle et de rectification, ni les majorations ordinaires de retard ou les sanctions reposant sur un fondement légal autonome. Elle ne permet pas de rétablir sous un autre nom la majoration supprimée.</p>",
         status='rewrite_draft', change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19',
         repeal_scope="Suppression de la majoration de 10 % pour absence de mise en conformité et de son dispositif d'application pour les sanctions futures, avec traitement distinct des décisions antérieures définitives.")
a.pop('classification')
a['substantive_impact']['classification'] = 'material_reduction'
a['substantive_impact']['new_burdens_review'] = "Aucune charge nouvelle identifiée : la majoration est retirée sans taxe, déclaration, registre ou procédure d'autorisation de remplacement. La conservation des dettes principales et sanctions autonomes n'en crée pas de nouvelles."
a['substantive_impact']['effects'] = [effect(
    'obligation_removed', 'urssaf-majoration-non-conformite-suppression',
    "Suppression de l'obligation de payer la majoration accessoire pour défaut de mise en conformité réitéré.",
    "10 % du montant du redressement concerné par la réitération d'observations d'un précédent contrôle, y compris sans redressement antérieur ; R243-18 en précise l'assiette et la fenêtre de six ans.",
    "Aucune majoration sur ce fondement ne peut être prononcée après la bascule ; cotisations principales, majorations ordinaires et sanctions autonomes conservent leurs assiettes et taux propres.",
    'percent', 'Cotisants faisant l’objet d’un constat de non-conformité à des observations antérieures.',
    "À compter de l'entrée en vigueur ; décisions antérieures définitives préservées, sous le régime légal applicable, et loi répressive plus douce pour les sanctions non définitives.",
    "Aucun prélèvement ni formalité de remplacement ; aucune baisse du principal revendiquée.",
    "Le montant du redressement des cotisations et contributions sociales mis en recouvrement à l'issue d'un contrôle réalisé en application de l'article L. 243-7 est majoré de 10 % en cas de constat d'absence de mise en conformité.",
    "Aucune majoration de 10 % pour absence de mise en conformité ne peut être prononcée sur son fondement à compter de cette date, même lorsque les observations antérieures ou le contrôle sont antérieurs à celle-ci.")]

entry('L243-7-7',
      "Maintien intégral nécessaire des sanctions du travail dissimulé et de leurs réductions favorables. La gravité et la récidive justifient une protection antifraude distincte d'une erreur réitérée de conformité. Les taux de 35 %, 50 % et 60 %, puis 45 %, 60 % et 70 % en récidive, sont conservés avec la réduction de vingt points, les trente jours, le plan accepté et le bénéfice des donneurs d'ordres. Supprimer la réduction retirerait un avantage pour les futurs redevables éligibles.",
      "Source assignée dans la rédaction issue de la loi du 25 juin 2026 : application aux procédures engagées à compter d'une date fixée par décret, au plus tard le 1er janvier 2027. Ne pas confondre cette borne avec une date de promulgation du projet ni avancer la rédaction. La réduction du II reste exclue dans les cas du III ; sa notification intervient après paiement intégral. La période de récidive de cinq ans part de la notification de la première constatation ayant donné lieu à redressement. La suppression de L243-7-6 ne supprime pas cet article autonome.",
      "Les sanctions de fraude et leurs allègements conditionnels sont maintenus intégralement par rapport à la source entière, sans nouvelle baisse comptée.",
      "L'applicabilité temporelle de la rédaction assignée dépend du décret mentionné en note. Aucun taux d'une autre version ni cumul de sanctions non prévu n'est ajouté.")

entry('L243-7-8',
      "Maintien intégral utile du pouvoir de corriger les anomalies de DSN après la période contradictoire. L'article ne demande pas un second dépôt au cotisant et conserve l'intervention contradictoire avant correction ; le supprimer pourrait empêcher une correction favorable des droits sociaux. Les dispensations de réitération déjà coordonnées dans L213-1 ne constituent pas un nouveau gain à reproduire ici.",
      "Le renvoi à L243-7-1 A vise la période contradictoire entière et non le préavis de rupture d'emploi. Les corrections doivent conserver les exclusions d'assiette, exonérations et périodes correctes. La note d'entrée en vigueur immédiate de la loi de 2025 n'est pas une nouvelle transition de notre projet.",
      "La correction administrative après contradictoire est déjà prévue sans nouvelle obligation déclarative propre ; le maintien ne compte pas comme suppression de double DSN.",
      "L'article ne règle pas à lui seul la norme technique, les délais réglementaires ou la correction des autres organismes ; il n'autorise aucun nouvel accès aux données.")

entry('L243-8',
      "Maintien intégral nécessaire de la surveillance étatique des objectifs et méthodes de contrôle et des injonctions en cas de carence. Elle encadre les organismes et le traitement des infractions pénales ; aucun rapport périodique distinct ou justificatif du cotisant n'est imposé par cet article. La demande de procès-verbaux est liée à ce contrôle de tutelle et non à une collecte doublonnée à la charge des assurés.",
      "Notes lues en entier : renvois historiques à L612-10, L243-2 et R642-10, application à Saint-Pierre-et-Miquelon avec substitution par la caisse de prévoyance sociale. Ces indications ne sont pas converties en dispositions nouvelles ni en extension du contrat privé ; la portée actuelle de chaque texte d'extension doit être vérifiée lors de sa coordination, sans présenter tous les renvois historiques comme encore actifs.",
      "Le contrôle des organismes et la transmission des infractions pénales sont maintenus, sans nouveau dépôt ni gain de conformité revendiqué.",
      "Les notes historiques ne suffisent pas à établir la consolidation actuelle de tous les régimes d'extension ; aucune réécriture de ces régimes extérieurs à l'article n'est affirmée.")

entry('L243-9',
      "Maintien intégral nécessaire du serment de confidentialité des agents avant leur entrée en fonctions et de sa sanction pénale. L'accès à des secrets de fabrication et résultats d'exploitation justifie cette garantie spécifique. L'assermentation mentionnée à L243-7 et l'objet du serment de L243-9 sont complémentaires ; aucun second serment matériel distinct n'est démontré par les sources, donc aucune fusion fictive n'est comptée.",
      "Préserver le tribunal judiciaire ou sa chambre de proximité et le renvoi à l'article 226-13 du code pénal. La note de 2019 concerne l'entrée en vigueur au 1er janvier 2020, non celle du projet. La confidentialité continue à protéger les entreprises et futurs cotisants contrôlés.",
      "La protection des secrets d'exploitation est intégralement conservée ; aucune suppression de démarche redondante n'a été démontrée dans cet article.",
      "Le contenu des modalités d'assermentation n'établit pas ici deux cérémonies obligatoires. Aucune dispense de secret, de sanction ou d'habilitation n'est créée.")

entry('L243-10',
      "Maintien intégral nécessaire de l'identification administrative numérotée des agents exposés à une menace physique. L'autorisation nominative du directeur vérifie cette menace ; elle n'est pas un agrément économique supprimable sans retirer une protection contre la violence. L'accès du juge à l'identité, la balance des droits de défense et l'examen des nullités évitent une immunité de contrôle. Aucune donnée nouvelle n'est demandée aux cotisants.",
      "Conserver I à III et les six alinéas : menace pour l'agent ou ses proches, qualité et service, communication au juge sans versement au dossier, requête motivée de partie, procureur dans le champ de CPP77-2 et sanction du IV de CPP15-4. Le renvoi à L8221-1 vise la recherche de travail dissimulé, non une dispense de notification de rupture. Les sources de procédure pénale hors lot ne sont pas déclarées réécrites.",
      "La protection de l'intégrité physique et son contrôle judiciaire sont maintenus sans élargissement du pouvoir d'anonymisation ni baisse de prélèvement.",
      "L'autorisation ne vaut que pour la menace caractérisée et le champ légal de contrôle ; les garanties de défense et les procédures de nullité restent applicables.")

entry('L243-11',
      "Maintien intégral nécessaire de l'accueil des agents de contrôle régulièrement compétents et des ingénieurs conseils et contrôleurs de sécurité accrédités. L'obligation permet les vérifications et la prévention des risques professionnels ; elle n'institue ni autorisation de l'activité du cotisant ni transmission annuelle. Sa suppression compromettrait les contrôles de fraude et de sécurité identifiés comme essentiels.",
      "L'Etat n'est visé que pour l'application de L243-7 ; conserver cette qualification et les autres personnes publiques et travailleurs indépendants. L114-10 porte un fondement de contrôle distinct. L'accréditation vise les intervenants, non une nouvelle formalité privée. Les modalités d'accès et la nécessité des demandes demeurent contrôlables.",
      "L'obligation essentielle d'accueil et les limites de compétence sont conservées sans nouveau contrôle périodique ni formalité ajoutée.",
      "Le maintien n'élargit pas le droit d'accès aux lieux ou données au-delà des pouvoirs légaux des agents et ne neutralise pas les garanties du cotisant.")

entry('L243-12',
      "Coordination nécessaire, sans réforme du droit de contrôle : le renvoi à l'ancien dernier alinéa de L143-3 du code du travail est remplacé par L3243-4, dont la source intégrale impose la conservation des doubles ou bulletins électroniques pendant cinq ans. Le pouvoir de communication et la durée de cinq ans inscrite dans cet article sont conservés. Aucune baisse fictive des durées d'archives n'est revendiquée.",
      "Nouveau renvoi à L3243-4, cible non fournie dans reference-targets.json : lecture facultative intégrale dans travail.json du corpus public, source LEGIARTI000020625846. Cet article vise expressément les doubles et les bulletins électroniques ; il ne s'agit ni de L1234-1 ni d'un régime d'ancienneté. La durée de cinq ans n'est pas un droit à détruire une pièce encore nécessaire sous le régime autonome de six ans de L243-16 ; les deux minima s'appliquent selon leur champ. Ce cumul préexistant n'est pas corrigé silencieusement par une réduction de conservation. La fidélité des copies électroniques et les modalités techniques restent soumises à leurs règles propres.",
      "Seul le renvoi devenu obsolète est corrigé. La communication et les obligations de conservation existantes subsistent ; aucune obligation matérielle supprimée n'est démontrée.",
      "Les archives nécessaires à l'assiette et au contrôle peuvent relever de L243-16 ; cette coordination n'en réduit pas la durée et ne remplace pas les autres prescriptions de conservation.")
a = answers['L243-12']
a.update(proposed_xml="<p>Les agents des organismes de sécurité sociale mentionnés aux articles L. 114-10 et L. 243-7 peuvent, à tout moment, exiger des employeurs soumis à leur contrôle la communication des doubles des bulletins de paie mentionnés à l'article L. 3243-4 du code du travail. Ces doubles sont conservés par l'employeur pendant cinq ans.</p>", status='rewrite_draft')
a.pop('classification')
a['substantive_impact']['classification'] = 'coordination_only'
a['substantive_impact']['new_burdens_review'] = "Aucune charge nouvelle identifiée : le renvoi est actualisé vers l'obligation existante de conservation des mêmes bulletins. Ni durée, ni support obligatoire, ni dépôt, ni nouveau destinataire ne sont ajoutés."
a['substantive_impact']['effects'] = [effect(
    'coordination', 'bulletins-paie-renvoi-conservation-actualise',
    "Actualisation du renvoi au code du travail relatif à la conservation des bulletins de paie.",
    "Renvoi au dernier alinéa de l'ancien article L143-3 ; communication des doubles et durée de cinq ans.",
    "Renvoi à L3243-4 ; même pouvoir de communication des doubles et même durée de cinq ans, sous les obligations autonomes de conservation.",
    'legal_duty', 'Employeurs soumis au contrôle et agents habilités à demander les bulletins.',
    "Coordination applicable dès l'entrée en vigueur, sans reprise des délais de conservation ni nouveau dépôt d'archives.",
    'Aucune charge de remplacement et aucune réduction matérielle comptée.',
    "la communication des doubles des bulletins de paie mentionnés au dernier alinéa de l'article L. 143-3 du code du travail.",
    "la communication des doubles des bulletins de paie mentionnés à l'article L. 3243-4 du code du travail.")]

entry('L243-12-1',
      "Maintien intégral nécessaire de la sanction de l'obstacle au contrôle, limitée aux sollicitations nécessaires. Les plafonds distincts de 3 750 €, 7 500 € et 750 000 €, le délai de cinq ans de récidive, la prise en compte des circonstances et de la gravité, le contradictoire et les voies de recours assurent la proportionnalité. Cette sanction d'entrave protège l'effectivité des contrôles ; elle ne doit pas servir à rétablir une obligation supprimée ailleurs.",
      "Les 3°, 4° et 6° de L133-5-6 désignent trois catégories de particuliers employeurs, non des seuils d'ancienneté. Maintenir la condition de nécessité pour chaque demande, la réponse aux observations et les renvois à L244-2 et L244-8-1 pour notification et prescription. Une pièce ou déclaration légalement supprimée ne devient pas exigible par le seul article de sanction.",
      "La sanction d'entrave et ses plafonds favorables restent ceux de la source entière, sans nouvelle sanction, formalité ou réduction présentée comme acquise.",
      "La nécessité d'une demande et la gravité de l'entrave restent à établir au cas par cas ; les montants sont des maxima et non un tarif automatique.")

entry('L243-12-3',
      "Maintien intégral nécessaire des protections pénales des agents de contrôle contre les résistances, outrages et violences. Cette extension est liée aux fonctions exposées et répond à la protection essentielle contre les violences ; elle ne constitue ni une cotisation accessoire ni une formalité économique à retirer. Aucune réécriture stylistique n'est proposée.",
      "Le renvoi à L243-11 délimite les agents protégés ; il ne confère pas de nouveaux pouvoirs de police judiciaire. Les éléments constitutifs, garanties et peines du code pénal demeurent ceux de ce code, hors du présent lot. Ne pas assimiler une contestation juridique à une violence ou à un outrage.",
      "La protection pénale des agents est conservée intégralement ; aucun nouveau gain matériel ou transfert financier n'est revendiqué.",
      "L'article n'invente pas une infraction autonome pour un désaccord sur un redressement et n'écarte pas les droits de défense ou recours du cotisant.")

entry('L243-12-4',
      "Maintien intégral nécessaire d'une dispense de second contrôle sur les mêmes points et la même période. Cette protection existante allège les contrôles futurs aussi ; la supprimer retirerait une dérogation favorable. Les exceptions de réponse incomplète ou inexacte, fraude, travail dissimulé et demande judiciaire gardent une fonction essentielle pour ne pas couvrir les faits non loyalement vérifiés.",
      "Conserver ensemble les conditions même période et mêmes points déjà vérifiés ; ne pas transformer cette garantie en immunité d'établissement sur tous sujets. La faculté d'utiliser des pièces de groupe de L243-7-4 ne supprime pas l'interdiction de répéter un contrôle hors exceptions. Aucun nouveau dossier de preuve n'est ajouté.",
      "L'interdiction du second contrôle est déjà dans la source ; son maintien protège l'allègement existant sans constituer une nouvelle réduction dénombrable.",
      "Les exceptions restent applicables et l'identité de période et de points doit être établie ; aucun délai nouveau ni extension aux vérifications non couvertes n'est décidé.")

entry('L243-15',
      "Réforme de fond limitée : l'attestation provisoire du travailleur indépendant débutant dépend de la déclaration régulière de l'activité et de l'absence de première échéance, sans condition générale d'accomplissement de toutes les formalités et procédures de création. Cette condition indifférenciée peut bloquer l'accès à un contrat pour une formalité sans lien avec une dette sociale encore inexistante ; elle est retirée. Les obligations de création légalement autonomes, la vigilance initiale et périodique contre le travail dissimulé, la garantie du travail temporaire et tous les cas favorables de délivrance sont conservés intégralement.",
      "L8222-1 et D8222-5 du code du travail ont été lus dans le corpus : vigilance contractuelle et remise semestrielle d'attestation authentifiée ne sont pas supprimées ni comptées comme nouveau gain. L1251-49 a été lu intégralement : sa garantie protège salaires, accessoires, indemnités, cotisations et remboursements même sous un emploi à durée indéterminée. Le plafond de validité provisoire reste la première échéance déclarative ou de paiement. Ne pas supprimer le plan d'apurement respecté, le recours contentieux admis sauf verbalisation pour travail dissimulé, ou la dispense des particuliers pour leur usage familial. Examiner le décret et le formulaire d'attestation pour supprimer la seule condition générique de création sans réintroduire une attestation de remplacement ; ils ne sont pas réécrits ici.",
      "Une condition d'accès à l'attestation provisoire est effectivement retirée pour les débutants régulièrement déclarés, sans réduire les cotisations ni retirer la vigilance sur la situation sociale du cocontractant.",
      "Les formalités de création ayant une base autonome restent dues, et aucun gain n'est revendiqué sur la vérification semestrielle ou la garantie des entreprises de travail temporaire. L'ampleur des refus évités et le solde financier restent inconnus.")
a = answers['L243-15']
old = by_number['L243-15']['source_xml']
cut = " et que l'ensemble des formalités et procédures afférentes à la création d'activité ont été respectées"
assert cut in old
new = old.replace(cut, '', 1)
new += "<p>Le troisième alinéa s'applique aux attestations provisoires délivrées à compter de l'entrée en vigueur de la loi, y compris pour une activité commencée auparavant. La délivrance de l'attestation ne dispense pas des obligations de création d'activité imposées par d'autres dispositions légales ; leur accomplissement intégral ne conditionne pas cette délivrance. Les attestations antérieurement délivrées et les droits, créances et recours afférents aux périodes antérieures conservent leur régime.</p>"
a.update(proposed_xml=new, status='rewrite_draft', change_type='normative_reduction',
         reform_policy_id='editorial_direction_2026_10_19',
         removed_provisions=["La condition générale d'accomplissement de l'ensemble des formalités et procédures de création d'activité pour délivrer l'attestation sociale provisoire au débutant régulièrement déclaré."])
a.pop('classification')
a['substantive_impact']['classification'] = 'material_reduction'
a['substantive_impact']['new_burdens_review'] = "Aucune charge nouvelle identifiée : la même attestation provisoire reste délivrée, sans formulaire, contrôle préalable ou déclaration de substitution. Déclaration d'activité, première échéance et autres obligations autonomes sont des conditions préexistantes conservées."
old_third = re.findall(r'<p>(.*?)</p>', old, re.S)[2]
new_third = re.findall(r'<p>(.*?)</p>', new, re.S)[2]
a['substantive_impact']['effects'] = [effect(
    'relief_extended', 'attestation-provisoire-debutant-condition-creation-retiree',
    "Ouverture de l'attestation provisoire sans justification générale de toutes les formalités de création.",
    "Débutant non encore tenu de déclarer ou payer : activité régulièrement déclarée et ensemble des formalités et procédures de création accompli pour obtenir l'attestation provisoire.",
    "Même débutant : activité régulièrement déclarée suffisante pour cette condition d'accès ; attestation valable jusqu'à la première échéance, sans dispense des obligations autonomes de création.",
    'legal_duty', "Travailleurs indépendants débutant leur activité et cocontractants soumis à la vigilance sociale.",
    "Attestations délivrées dès l'entrée en vigueur, y compris pour activités commencées auparavant ; attestations et droits antérieurs préservés.",
    "Aucune pièce de remplacement ; cotisations, déclaration d'activité et vigilance existantes maintenues. Ce retrait ne supprime pas les formalités de création elles-mêmes.",
    plain(old_third), plain(new_third))]

entry('L243-16',
      "Maintien intégral nécessaire de la conservation des pièces utiles à l'assiette ou au contrôle pendant au moins six ans et de la faculté de conserver sur support informatique les pièces papier. Les délais de travail illégal de L244-11 atteignent cinq ans à partir des points de départ de L244-3, dont la fin de l'année civile : une simple réduction à cinq ans depuis la date de la pièce pourrait détruire la preuve avant prescription. Aucune obligation de doubles physiques n'est imposée ici et la conversion informatique favorable doit rester ouverte.",
      "L244-11 et L244-8-1 ont été lus dans le corpus : prescription de fraude, prescription d'assiette et action de recouvrement sont distinctes, avec possibilités de suspension ou interruption. La durée de six ans n'est pas réduite par le maintien du minimum de cinq ans de L243-12/L3243-4 pour les bulletins. Les obligations comptables autonomes peuvent avoir d'autres durées. L'arrêté de numérisation n'est pas réécrit ; aucun format ou registre nouveau n'est imposé.",
      "Le minimum de conservation et l'alternative informatique sont intégralement maintenus après examen de leur articulation avec les prescriptions ; aucun gain fictif d'archives n'est compté.",
      "Aucun chiffrage des coûts de stockage ni démonstration d'un doublon matériel imposé par cet article n'est disponible. Le maintien ne justifie pas de collecter des pièces inutiles au contrôle.")

entry('L244-1',
      "Maintien intégral nécessaire de la voie de poursuite contraventionnelle des manquements à la législation de sécurité sociale et de la faculté d'action du ministère public et des parties intéressées. Ce texte n'ajoute pas de déclaration ni ne fixe à lui seul un taux, une assiette ou un montant de peine. La poursuite des infractions subsistantes garde une fonction de protection des droits et de lutte contre la fraude.",
      "Le tribunal de police et les catégories de requérants restent ceux de la source. Une obligation abrogée ne peut servir de fondement à une poursuite future par ce seul renvoi général ; les règles de légalité et de loi répressive plus douce conservent leur portée. Aucun pouvoir de poursuite n'est transféré à un service privé.",
      "La voie judiciaire existante est conservée sans nouvelle infraction, formalité ou réduction de prélèvement revendiquée.",
      "L'article ne dispense pas d'identifier l'incrimination, la période et les éléments du manquement. Le régime pénal complet et ses garanties ne sont pas réécrits dans ce lot.")

entry('L244-3',
      "Maintien intégral utile des prescriptions triennales, de leurs points de départ distincts pour les indépendants, cotisations, majorations et défauts déclaratifs et de la suspension liée au contradictoire. Ces limites protègent les cotisants futurs et antérieurs dans les conditions des notes de 2016. Les retirer allongerait ou rendrait incertaine l'exposition à recouvrement ; la suspension est une coordination de la défense, non un délai de préavis d'emploi à raccourcir à quinze jours.",
      "Conserver les quatre alinéas et les notes : 30 juin de l'année suivante pour les indépendants ; fin d'année civile pour cotisations ; paiement ou exigibilité pour majorations ; production ou, à défaut, avertissement/mise en demeure pour pénalités déclaratives. Les règles transitoires de 2017 et leur borne de durée totale ne sont pas réinitialisées. L244-11 porte à cinq ans les délais en cas de procès-verbal de travail illégal ; la suppression de L243-7-6 ne crée aucune majoration nouvelle par le renvoi générique aux pénalités.",
      "Les limites existantes du droit de reprise et la suspension contradictoire sont conservées sans report nouveau de paiement ni réduction supplémentaire de dette.",
      "Les causes autonomes d'interruption, les délais spéciaux de fraude et l'action civile en recouvrement conservent leur champ ; aucun délai déjà acquis ou expiré n'est rouvert.")


# Analyses des trois cibles de travail : leur présence dans le fichier de contexte
# n'est pas un renvoi normatif de chaque article source à ces dispositions.
contexts = {
    'L243-6-7': "La convention coordonne les contrôles de DSN et leurs corrections ; elle ne règle aucune rupture d'emploi.",
    'L243-7': "Le pouvoir de contrôle vise aussi indépendants et employeurs publics ; il ne transforme pas leur régime en contrat privé.",
    'L243-7-1 A': "La lettre d'observations ouvre le contradictoire du contrôle, pas la notification d'une rupture d'emploi.",
    'L243-7-2': "Le dispositif qualifie un abus de droit social et protège la saisine préalable ; il ne fixe pas une indemnité de rupture.",
    'L243-7-5': "Les procès-verbaux de travail dissimulé fondent le redressement des cotisations dues, sans déterminer le terme des contrats.",
    'L243-7-7': "Les pourcentages sanctionnent le travail dissimulé et leurs réductions ont leurs propres trente jours ; aucun préavis de rupture n'est visé.",
    'L243-7-8': "La correction des données déclarées suit le contradictoire social ; elle ne constitue pas une nouvelle rupture de contrat.",
    'L243-10': "L'identification numérotée protège un agent menacé lors d'un contrôle ; elle n'est pas une notification de licenciement.",
    'L243-12': "Le renvoi actualisé concerne la conservation des bulletins de paie, non le préavis ou les conditions de rupture.",
    'L243-12-1': "L'entrave au contrôle et ses plafonds se distinguent de la rupture de l'emploi et de ses indemnités.",
    'L243-15': "Le contrat contrôlé est un contrat de travaux, services ou commerce avec un cocontractant ; ce n'est pas nécessairement un contrat d'emploi."
}
common = {
    'L1234-1': "L1234-1 officiel prévoit les préavis selon l'ancienneté et la faute grave ; sa proposition prévoit quinze jours calendaires pour les nouveaux contrats, avec procédures collectives et protections distinctes, et garde l'ancien régime des contrats antérieurs. Le point de départ par notification relève de L1234-3, pas du délai de contrôle ici. Aucun renvoi direct à L1234-1 n'est présent ni ajouté.",
    'L1221-2': "L1221-2 proposé impose une durée indéterminée à toute nouvelle embauche privée ; une affectation, mission ou formation limitée ne termine pas l'emploi. Les anciens contrats gardent leur transition et les régimes publics ne sont pas absorbés. L'article source n'autorise aucun nouveau CDD ni renouvellement, et les avantages sociaux de situations futures éligibles restent à leur champ propre.",
    'L1234-9': "L1234-9 officiel ouvre l'indemnité après huit mois sauf faute grave ; la proposition nouvelle retient un an à la fin effective, préavis compris, puis 0,20 mois par année totale avec mois complets au prorata et plafond de six mois, employeur seul. Ni cette ancienneté ni le préavis ne deviennent ici des conditions de contrôle, d'attestation ou d'allègement ; anciens droits, indemnités spéciales et réparations restent distincts. Aucun renvoi direct n'est créé."
}

specific = {
    ('L243-6-7', 'L213-1'): "Le I 8° de L213-1 confie aux unions la vérification, la correction contradictoire des anomalies de DSN et le contrôle sauf attribution légale contraire. La convention de L243-6-7 coordonne ces missions avec la retraite complémentaire, sans les étendre. La suppression du visa et du terme de cinq ans n'affecte ni les exclusions des 1° à 6° ni les transitions C3S/CPF-CDD de la proposition cible ; aucun seuil d'ancienneté ou délai de notification de rupture ne s'y substitue.",
    ('L243-6-7', 'L241-10'): "Le troisième alinéa de L243-6-7 inclut les anomalies des exonérations d'aide à domicile : L241-10 I et II, déductions de 2 € et 3,70 € du I bis et exonérations du III demeurent dans leur champ. La proposition cible garde les anciens CDD de remplacement et ouvre les futurs contrats uniques de même objet, avec régime public distinct. Aucun visa de convention, seuil d'un an ou préavis de quinze jours ne conditionne ces avantages.",
    ('L243-6-7', 'L241-3'): "Le renvoi du troisième alinéa vise le calcul du plafond de cotisations, dans la source au premier alinéa et dans la proposition au I, non la totalité des nouveaux comptes de retraite des II à VII. Le transfert de 0,5 à 4 % reste un financement distinct soumis à des préalables non réputés remplis, sans baisse de cotisation comptée ici. Le renouvellement de la convention ne conditionne ni le plafond ni les droits acquis ; aucun déplacement d'alinéa source n'est opéré dans ce lot.",
    ('L243-6-7', 'L241-13'): "Le troisième alinéa et les 1°/2° coordonnent les corrections de la réduction dégressive, non sa suppression. Les calculs annuels du III et facteurs du IV, ainsi que les calculs distincts plus favorables par affectation et mission de la proposition, restent utilisables pour les futurs contrats uniques sans terme d'emploi ni double compte. Les renvois internes de la cible à un montant prévu au I, alors que le seuil figure au II, présentent une discordance préexistante à coordonner hors de cet article ; la convention ne la corrige pas silencieusement.",
    ('L243-6-7', 'L242-1'): "Le renvoi vise l'assiette des cotisations du I, avec les exclusions du II de L242-1 qui doivent toutes être appliquées dans les corrections. La proposition cible conserve l'exclusion de rupture dans la limite de deux plafonds et retire les seuils d'assujettissement intégral pour les faits nouveaux selon son III ; elle n'est pas le droit officiel. Ni le préavis nouveau ni l'indemnité de 0,20 mois ne suppriment cette exclusion, les anciens régimes ou les garanties contradictoires.",
    ('L243-6-7', 'L752-3-2'): "Le troisième alinéa vise les exonérations ultramarines, avec leurs territoires, effectifs, secteurs et seuils propres. Le IV bis proposé de L752-3-2 garde un calcul distinct plus favorable par mission pour le travail temporaire nouveau sans fin automatique d'emploi ; les droits antérieurs et intermissions restent comptés. La convention sans visa ne ferme ni cette option ni les exonérations futures ; elle ne relève aucun taux ni ne transfère le régime agricole ou public au contrat privé.",
    ('L243-7', 'L133-8-4'): "Le premier alinéa de L243-7 vise précisément le 3° du III de L133-8-4 : les prestataires percevant de l'organisme les sommes des services réellement facturés, sous l'exception L133-8-6. Il ne vise pas un droit de rompre l'emploi. Déclarations, paiements directs en numéraire, deux jours francs du II, pièces et prescription du III 2° gardent leur régime, sans nouvelle attestation ou condition d'ancienneté. Le contrôle ne ferme pas le dispositif futur de services à domicile ou de garde d'enfants.",
    ('L243-7', 'L242-1'): "L'extension du contrôle à une personne morale non inscrite suppose des éléments motivés de revenus versés aux salariés de l'employeur initial ; l'assiette est celle de L242-1 I, corrigée de toutes les exclusions du II. Les indemnités de rupture ne sont pas assimilées automatiquement au salaire brut taxable. La proposition de la cible retire certains assujettissements intégraux mais garde leurs transitions ; aucun seuil d'ancienneté, préavis ou nouveau CDD n'est ajouté par la compétence de contrôle maintenue.",
    ('L243-7-2', 'L243-6-3'): "Le dernier alinéa exclut les actes préalablement exposés de façon complète par saisine restée sans réponse dans les délais requis. L243-6-3 II protège la période entre expiration du délai et réponse, et III l'opposabilité selon la situation et le droit applicables ; la suppression projetée de son seul rapport IV n'y change rien. L'exigence de tous éléments utiles et l'antériorité de la saisine sont maintenues, sans créer une acceptation tacite générale ou une condition d'ancienneté du salarié.",
    ('L243-7-2', 'L213-1'): "L213-1 identifie les unions de recouvrement ; le I 8° organise vérification et correction, sans présumer la fictivité d'un acte. L243-7-2 conserve la preuve à la charge des organismes et sa garantie de saisine préalable. La compétence de recouvrement ne rétablit aucune contribution supprimée dans ses transitions, notamment CPF-CDD ou C3S. Les nouveaux contrats uniques et les anciens droits ne changent pas le critère d'abus exclusivement éludant.",
    ('L243-7-5', 'L213-1'): "Les unions de L213-1 recouvrent les sommes relevant de leurs attributions ; L243-7-5 autorise l'utilisation des procès-verbaux transmis par les agents de travail illégal. Il ne délègue pas à ces agents le calcul des indemnités de rupture. Les exclusions et transitions de la cible, dont la fin du CPF-CDD sur rémunérations futures, bornent les sommes recouvrables ; le contrat unique ne crée pas une contribution équivalente.",
    ('L243-7-7', 'L243-7-5'): "Le I de L243-7-7 vise aussi les redressements fondés sur les informations de procès-verbaux transmis selon L243-7-5. Cette cible officielle sans proposition n'établit aucun taux de majoration : ces taux restent au I et au III de L243-7-7. Son maintien conserve le recouvrement du principal et les garanties applicables ; il n'ajoute ni notification de rupture, ni seuil d'ancienneté, ni suppression de la réduction de vingt points du II.",
    ('L243-7-8', 'L243-7-1 A'): "L243-7-8 intervient à l'issue de la période contradictoire ouverte par la lettre d'observations de L243-7-1 A. La cible garde la notification préalable, la lettre valant notification/invitation dans le cas L133-8-7 et la prolongation sur demande sous ses exclusions. Aucun délai de quinze jours de rupture n'y est importé ; le renvoi est cohérent et ne permet pas une correction anticipée avant la clôture de cette période.",
    ('L243-7-8', 'L213-1'): "Le I 8° de L213-1 organise les missions de vérification/correction des unions avec renvoi à L133-5-3-1. L243-7-8 traite leur correction après le contradictoire de contrôle ; les deux champs ne sont pas fusionnés artificiellement. La dispense de répétition des mêmes données de la proposition cible ne devient pas une nouvelle déclaration et n'est pas comptée une deuxième fois. Les exonérations connues et les anciennes situations de contrats restent traitées selon leur législation.",
    ('L243-12-1', 'L133-5-6'): "Le premier alinéa renvoie exactement aux 3°, 4° et 6° de L133-5-6 : particuliers employeurs de salariés, garde d'enfants et stagiaires aides familiaux au pair, pour le plafond de 3 750 €. Les autres plafonds ne doivent pas être étendus à ces catégories par le contrat unique. Le dispositif déclaratif reste facultatif ; la rémunération d'un salarié, la qualification publique ou privée et les anciens contrats ne se déduisent pas d'une ancienneté d'un an ou d'un préavis.",
    ('L243-15', 'L213-1'): "Le premier alinéa de L243-15 vise les organismes qui connaissent l'état des déclarations et paiements des cocontractants. L213-1 définit les missions des unions, dont vérification et corrections au I 8°, et conserve les exclusions de recouvrement. La suppression de la condition générique de création pour l'attestation provisoire n'annule aucune dette effectivement due, ne crée aucun nouveau destinataire de données et reste ouverte aux futurs indépendants régulièrement déclarés sans lien avec l'ancienneté d'un salarié.",
    ('L244-3', 'L243-7-1 A'): "Le deuxième alinéa de L244-3 suspend la prescription pendant la période contradictoire de L243-7-1 A ; ce n'est ni le délai de mise en demeure ni le préavis individuel. La cible conservée comprend la prolongation demandée avant expiration et ses exclusions, qui demeurent inchangées. Le maintien ne suspend pas tous les recours judiciaires et ne réinitialise ni le point de départ particulier des indépendants ni les prescriptions acquises selon les transitions de 2017."
}

for s in sources:
    a = answers[s['number']]
    key = s['code_id'] + '|' + s['source_id']
    checks = []
    for target_key in refs['requirements'][key]:
        target = refs['targets'][target_key]
        number = target['number']
        if number in common:
            text = contexts[s['number']] + ' ' + common[number]
        else:
            text = specific[(s['number'], number)]
        checks.append(dict(target_key=target_key, view_sha256=target['view_sha256'], assessment=text))
    a['reference_checks'] = checks

output = [answers[s['number']] for s in sources]
(ROOT / 'answer.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json: {len(output)} articles')
