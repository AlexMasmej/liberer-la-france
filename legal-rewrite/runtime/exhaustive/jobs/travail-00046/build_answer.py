import json
import re
import html
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
by_number = {s['number']: s for s in sources}
answers = {}


def plain(xml):
    return html.unescape(re.sub(r'<[^>]*>', '', xml or ''))


def paragraphs(*items):
    return ''.join('<p>' + p + '</p>' for p in items)


def source_paragraphs(number):
    return re.findall(r'<p(?:\s[^>]*)?>(.*?)</p>', by_number[number]['source_xml'], re.S)


def base(number, proposed, reason, notes, classification, assessment, limits, burdens, effects=None):
    s = by_number[number]
    result = {k: s[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    result.update(
        proposed_xml=proposed,
        reason=reason,
        review_notes=notes,
        status='retained_unchanged' if proposed is None else 'rewrite_draft',
        substantive_impact={
            'version': 1,
            'classification': classification,
            'assessment': assessment,
            'scope_limitations': limits,
            'new_burdens_review': burdens,
            'effects': effects or [],
        },
    )
    answers[number] = result
    return result


def retain(number, reason, notes, assessment, limits, burdens):
    return base(number, None, reason, notes, 'retained_necessary', assessment, limits, burdens)


def reduce(number, proposed, reason, notes, removed, assessment, limits, burdens, effects,
           classification='material_reduction'):
    a = base(number, proposed, reason, notes, classification, assessment, limits, burdens, effects)
    a.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19',
             removed_provisions=removed)
    return a


def repeal(number, proposed, reason, notes, scope, assessment, limits, burdens, effects,
           classification='material_reduction'):
    a = base(number, proposed, reason, notes, classification, assessment, limits, burdens, effects)
    a.update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19', repeal_scope=scope)
    return a


def effect(kind, measure, description, before, after, unit, population, transition, burdens, sq, pq):
    return dict(kind=kind, measure_id=measure, description=description, before=before, after=after,
                unit=unit, affected_population=population, conditions_and_transition=transition,
                replacement_or_new_burdens=burdens, source_quote=sq, proposed_quote=pq)


retain('L2242-4',
       "Maintien intégral après examen : l'interdiction temporaire de décisions unilatérales collectives dans les matières effectivement négociées garantit une négociation utile. L'exception d'urgence permet déjà l'action indispensable. Aucun dépôt, agrément ou délai supplémentaire à supprimer n'est institué ici.",
       "Les trois renvois, L. 2242-1, L. 2242-2 et L. 2242-2-1, ont été lus dans le corpus : rémunération/égalité, GEPP et salariés expérimentés. L'interdiction est limitée à la négociation en cours et à ses matières ; elle ne crée pas un veto syndical permanent. Les ruptures individuelles et leurs préavis ne relèvent pas de cet article. Aucun renvoi aux anciennes transmissions de L2232 n'est ajouté.",
       "La source entière est conservée : protection de la loyauté collective avec exception d'urgence, sans allègement matériel revendiqué.",
       "Ni la durée des négociations ni l'ensemble des décisions urgentes ne sont chiffrés ; la règle ne modifie pas les procédures de rupture.",
       "Aucune charge nouvelle n'est identifiée : le texte source est maintenu sans registre, pièce, notification ou délai ajouté.")

p = source_paragraphs('L2242-5')
p[1] = "Ce procès-verbal n'est soumis à aucun dépôt auprès de l'autorité administrative ou du greffe. Aucun envoi ni déclaration ne remplace ce dépôt."
p.append("La dispense de dépôt s'applique à compter de l'entrée en vigueur de la loi, y compris aux procès-verbaux établis antérieurement dont le dépôt n'a pas encore été effectué. Aucun dépôt tardif ou de régularisation n'est exigé après cette date sur le seul fondement du présent article. Les dépôts déjà effectués, les mesures prises et les droits et recours qui s'y rattachent conservent leurs effets ; aucun procès-verbal n'est à refaire.")
reduce('L2242-5', paragraphs(*p),
       "Réforme de fond : suppression du dépôt administratif du procès-verbal de désaccord et de tout envoi de remplacement. Le procès-verbal lui-même, les dernières propositions de chaque partie et les mesures unilatérales envisagées restent nécessaires à la preuve de la négociation et au contrôle de sa loyauté ; ils sont conservés sans reformulation de pure forme.",
       "R. 2242-1 a été lu : son obligation de dépôt par renvoi à D. 2231-2 doit être retirée pour les dépôts futurs. Il n'est pas modifié dans ce lot. L. 4162-2, également lu, continue à renvoyer au contenu du procès-verbal, sans rétablir son dépôt. La proposition fournie de L. 6324-9 A dispense déjà de procès-verbal distinct dans son champ propre : cette dérogation reste plus favorable. Aucun dépôt d'accord collectif ni de plan d'action autonome, notamment L. 2242-3 ou L. 4162-3, n'est supprimé par assimilation.",
       ["Dépôt obligatoire du procès-verbal de désaccord à l'initiative de la partie la plus diligente, sans transmission de remplacement."],
       "Une formalité de dépôt disparaît réellement par rapport à la source entière ; la constitution du procès-verbal et son contenu sont maintenus. Aucun coût national n'est estimé.",
       "Le règlement R. 2242-1 reste à coordonner ; les dépôts d'accords et de plans ayant un fondement autonome sont hors de cette suppression.",
       "Aucune charge nouvelle n'est identifiée : le procès-verbal existait déjà, et la suppression du dépôt ne crée ni déclaration, ni destinataire, ni délai de remplacement.",
       [effect('obligation_removed', 'negociation-depot-pv-desaccord-supprime',
               "Suppression du dépôt du procès-verbal général de désaccord.",
               "Procès-verbal à déposer par la partie la plus diligente selon la procédure réglementaire, sans taux ni assiette fiscale.",
               "Procès-verbal conservé comme pièce de négociation, sans aucun dépôt ni envoi de remplacement.",
               'legal_duty', "Parties aux négociations obligatoires se terminant sans accord.",
               "Tous dépôts restant à effectuer à l'entrée en vigueur, même pour un procès-verbal antérieur ; dépôts accomplis conservés.",
               "Aucune procédure de remplacement ; les obligations autonomes de dépôt d'accords et de plans subsistent.",
               "Ce procès-verbal donne lieu à dépôt, à l'initiative de la partie la plus diligente, dans des conditions prévues par voie réglementaire.",
               "Ce procès-verbal n'est soumis à aucun dépôt auprès de l'autorité administrative ou du greffe.")])

proposed = paragraphs(
    "Le dépôt des accords collectifs d'entreprise sur les salaires effectifs auprès de l'autorité administrative, dans les conditions de l'article L. 2231-6, n'est pas subordonné à la production d'un procès-verbal d'ouverture des négociations sur les écarts de rémunération entre les femmes et les hommes. Aucun procès-verbal ni attestation de remplacement n'est exigé à cette fin. L'employeur reste tenu d'engager sérieusement et loyalement ces négociations. Dans les entreprises où sont constituées une ou plusieurs sections syndicales d'organisations représentatives, il convoque les organisations syndicales représentatives dans l'entreprise, fixe le lieu et le calendrier des réunions, leur communique les informations nécessaires pour négocier en toute connaissance de cause et répond de manière motivée à leurs éventuelles propositions.",
    "Cette dispense de pièce s'applique aux dépôts effectués à compter de l'entrée en vigueur de la loi, y compris aux dépôts en cours ou concernant des accords antérieurs. Les dépôts déjà accomplis restent valables et ne sont pas à renouveler. Elle ne régularise pas un défaut de négociation sérieuse et loyale et ne supprime aucun droit ou recours relatif aux négociations antérieures.")
reduce('L2242-6', proposed,
       "Réforme de fond : retrait du procès-verbal d'ouverture et de son attestation de loyauté comme conditions du dépôt salarial. Le contrôle porte sur la négociation réelle, non sur une pièce supplémentaire. Les convocations de tous les syndicats représentatifs, le lieu, le calendrier, les informations et les réponses motivées sont intégralement maintenus.",
       "L. 2231-6 a été lu : le dépôt de l'accord subsiste, avec sa proposition de dépôt unique ; la présente suppression concerne une pièce additionnelle différente, sans recompter le dépôt unique comme un gain du lot. Le procès-verbal de désaccord de L. 2242-5 reste dû lorsqu'il est applicable, sans dépôt. Aucune transmission CPPNI ni ancien délai L2232 n'est rétabli. Les prescriptions réglementaires de pièces de dépôt devront être alignées ; elles ne peuvent maintenir cette condition par une autre dénomination.",
       ["Procès-verbal d'ouverture des négociations sur les écarts de rémunération et attestation de loyauté imposés pour déposer l'accord salarial."],
       "La condition documentaire bloquant le dépôt est supprimée. Le contenu essentiel de la négociation sur l'égalité et sa preuve en justice ne sont pas allégés.",
       "Les autres pièces de dépôt et les recours pour négociation déloyale subsistent ; leur coût global et les formulaires non fournis ne sont pas évalués.",
       "Aucune charge nouvelle n'est identifiée : les actions de négociation énumérées étaient toutes exigées par la source ; aucune attestation ne remplace le procès-verbal supprimé.",
       [effect('obligation_removed', 'negociation-depot-salarial-sans-pv',
               "Retrait de la pièce d'ouverture obligatoire au dépôt des accords salariaux.",
               "Dépôt de l'accord salarial subordonné à un procès-verbal d'ouverture consignant les propositions et attestant la loyauté.",
               "Dépôt de l'accord sans ce procès-verbal ni attestation de remplacement ; loyauté et négociation sur les écarts maintenues.",
               'legal_duty', "Entreprises déposant un accord collectif sur les salaires effectifs.",
               "Dépôts futurs et en cours dès l'entrée en vigueur, sans refaire les dépôts valides ni effacer les manquements de fond.",
               "Aucune pièce de remplacement ; convocations, informations et réponses motivées déjà obligatoires demeurent.",
               "Le procès-verbal atteste que l'employeur a engagé sérieusement et loyalement les négociations.",
               "Aucun procès-verbal ni attestation de remplacement n'est exigé à cette fin.")])

proposed = paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant cette abrogation.",
    "Aucune pénalité administrative fondée sur le présent article n'est due pour les manquements commis à compter de cette date à l'obligation de négocier sur les salaires effectifs. Pour un manquement se poursuivant après cette date, aucune période postérieure à celle-ci n'entre dans le calcul de cette pénalité. Aucune réduction ou suppression des exonérations de cotisations sociales ne la remplace.",
    "Pour les manquements antérieurs, la suppression de la pénalité s'applique aux sanctions qui ne sont pas devenues définitives, dans les conditions de la loi répressive plus douce. Les pénalités devenues définitives avant l'entrée en vigueur conservent leurs règles de liquidation, d'affectation et de recouvrement, ainsi que les garanties et recours applicables ; aucun remboursement général des sommes légalement acquittées n'est institué. Les plafonds, périodes de référence, dispenses liées à la périodicité négociée et règles de modulation antérieurement plus favorables restent opposables dans les procédures anciennes auxquelles ils demeurent applicables.",
    "Les réductions et exonérations de cotisations sociales, notamment celle de l'article L. 241-13 du code de la sécurité sociale, restent ouvertes aux situations antérieures et futures qui en remplissent les conditions. Leur montant n'est pas diminué au titre de la pénalité supprimée. L'obligation de négocier sur les salaires effectifs et les sanctions et recours ayant un autre fondement légal demeurent applicables.")
repeal('L2242-7', proposed,
       "Réforme de fond : suppression de toute la pénalité administrative attachée au défaut de négociation salariale, ainsi que de son circuit propre pour les faits nouveaux. Son assiette, indexée sur les allègements d'emploi, pénalise ces allègements ; le délit de soustraction à la négociation et les recours judiciaires fournissent un fondement autonome d'effectivité. L'obligation de négocier n'est pas supprimée, et les réductions sociales ne deviennent pas la recette de remplacement.",
       "La source comporte deux plafonds, 10 % ou 100 % des exonérations L. 241-13, selon l'existence d'un contrôle avec manquement au cours des six années civiles précédentes ; elle limite les périodes à trois années, selon deux fenêtres différentes. La dispense pendant la durée de l'accord portant la négociation au-delà d'un an et la modulation administrative ne sont pas supprimées au détriment d'une procédure ancienne. D. 2242-12 à D. 2242-16 ont été lus dans le corpus : rapport, notifications, échanges d'assiettes, déclaration et versement exclusivement liés à cette pénalité devront être neutralisés pour le nouveau champ ; les procédures des pénalités définitives anciennes restent nécessaires. L. 241-13 est examiné dans reference_checks ; l'affectation sociale des recettes anciennes subsiste sans recette compensatoire nouvelle. L. 2243-1 et L. 2243-2 sont coordonnés dans le présent lot.",
       "Pénalité administrative pour manquement à la négociation salariale, plafonds de 10 % et 100 % des exonérations, liquidation et circuit déclaratif propres pour les faits nouveaux.",
       "Une sanction pécuniaire administrative entière disparaît pour les faits nouveaux, sans disparition des cotisations ordinaires ni de la négociation. Ce n'est pas une baisse du taux des cotisations.",
       "Les condamnations ou pénalités définitives anciennes, les infractions autonomes et les procédures réglementaires résiduelles ne sont pas abolies. Perte de recettes non chiffrée.",
       "Aucune charge nouvelle n'est identifiée : aucune taxe, réduction d'allègement, déclaration ou autorisation ne remplace la sanction administrative supprimée ; les recours et l'amende pénale ont déjà un fondement autonome.",
       [effect('obligation_removed', 'negociation-salaires-penalite-admin-supprimee',
               "Suppression de la dette punitive administrative liée au défaut de négociation salariale.",
               "Pénalité plafonnée à 10 % des exonérations L. 241-13, ou 100 % en cas de précédent manquement constaté dans les six années civiles précédentes, sur au plus trois années selon les fenêtres légales.",
               "Aucune pénalité administrative de ce fondement pour les nouveaux manquements ; aucune reprise d'exonération de remplacement ; cotisations de droit commun inchangées.",
               'legal_duty', "Employeurs ayant une ou plusieurs sections syndicales représentatives et tenus à la négociation salariale.",
               "Entrée en vigueur de la loi ; périodes nouvelles exclues ; loi plus douce pour les sanctions non définitives et régime antérieur des pénalités définitives.",
               "Pas de prélèvement de remplacement ; négociation, recours et sanction pénale autonome subsistent.",
               "Dans les entreprises où sont constituées une ou plusieurs sections syndicales d'organisations représentatives, l'employeur qui n'a pas rempli l'obligation de négociation sur les salaires effectifs mentionnée au 1° de l'article L. 2242-1 est soumis à une pénalité.",
               "Aucune pénalité administrative fondée sur le présent article n'est due pour les manquements commis à compter de cette date à l'obligation de négocier sur les salaires effectifs.")])
answers['L2242-7']['benefit_review'] = (
    "La réduction générale L. 241-13 est l'avantage social principal : elle demeure accessible pour les futurs salariés éligibles, y compris dans le contrat unique selon la coordination fournie, sans reprise fondée sur la pénalité abolie. La source offre aussi un plafond de 10 % plutôt que 100 % en l'absence de précédent manquement en six ans, deux limites de trois années avec fenêtres propres, une inapplication temporaire pendant la périodicité négociée supérieure à un an et une modulation selon efforts, situation économique, gravité et circonstances. Pour les faits nouveaux, la disparition totale de la sanction rend ces limites sans objet sans taxe de remplacement ; pour les procédures anciennes encore applicables, ces garanties restent opposables, sous réserve de la suppression plus douce des sanctions non définitives. Ni les autres exonérations ni les droits à restitution de cotisations ne sont fermés.")

p = source_paragraphs('L2242-8')
p[0] = ("Les entreprises d'au moins cinquante salariés sont soumises à une pénalité à la charge de l'employeur lorsqu'elles ne sont couvertes ni par un accord relatif à l'égalité professionnelle entre les femmes et les hommes à l'issue de la négociation mentionnée au 2° de l'article L. 2242-1 ni, à défaut d'accord, par un plan d'action mentionné à l'article L. 2242-3. Les modalités de suivi de la réalisation des objectifs et des mesures de l'accord et du plan d'action sont fixées par décret. L'absence d'accord peut être établie par tout moyen, sans attestation particulière imposée par le présent article. L'obligation générale d'établir un procès-verbal de désaccord, lorsqu'elle est applicable en vertu de l'article L. 2242-5, demeure distincte.")
p.append("La suppression de l'attestation particulière s'applique aux contrôles et procédures en cours à compter de l'entrée en vigueur de la loi, sans qu'un document déjà établi soit à refaire. Elle ne dispense ni de l'accord ou du plan d'action requis ni des obligations mentionnées au deuxième alinéa. Les pénalités et recours relatifs aux périodes antérieures restent soumis aux règles qui leur sont applicables, sous réserve de la loi répressive plus douce.")
reduce('L2242-8', paragraphs(*p),
       "Coordination de fond limitée : suppression du mode de preuve spécialement imposé aux entreprises d'au moins 300 salariés pour attester le défaut d'accord. Le procès-verbal général L. 2242-5 demeure ; aucune économie d'un second procès-verbal n'est revendiquée. Maintien nécessaire de la pénalité d'égalité, du plafond de 1 %, des publications, mesures correctrices et règles de modulation. La première phrase est rendue explicite au regard du défaut simultané d'accord et de plan.",
       "Incohérence rédactionnelle préexistante signalée : la source dit « en l'absence d'accord ... ou, à défaut d'accord, par un plan d'action », sans verbe gouvernant le plan. R. 2242-3, lu en entier avec R. 2242-2 et R. 2242-4, confirme le manquement de défaut de couverture par accord ou plan ; la proposition explicite cette lecture, sans créer un cas de pénalité en présence d'un plan valable. Conserver seuil de 50 salariés, maximum de 1 % et assiette du premier alinéa de L. 242-1 et de L. 741-10 rural, périodes de non-respect, appréciation des efforts et motifs, et affectation à L. 200-2 3°. L. 242-1 I est vérifié dans reference_checks ; les exclusions du II ne deviennent pas l'assiette de la sanction. Aucun préavis de rupture n'intervient. Les règlements doivent cesser d'exiger l'attestation spéciale ; le contrôle d'égalité reste entier. La note de 2025 fixe une entrée en vigueur au 1er janvier 2026, pas celle de la présente réforme.",
       ["Attestation du défaut d'accord par un procès-verbal imposée spécialement par L2242-8 aux entreprises d'au moins 300 salariés."],
       "Coordination probatoire : le support spécialement prescrit au seuil de 300 salariés est retiré, mais le procès-verbal général reste exigible. Aucune baisse du plafond de 1 % ni économie certaine d'un document entier n'est revendiquée.",
       "Le dépôt du plan, les indicateurs d'égalité, leurs mesures correctrices et les garanties réglementaires demeurent ; l'effet de coût marginal de cette déduplication n'est pas établi.",
       "Aucune charge nouvelle n'est identifiée : preuve libre à la place d'un support imposé, sans nouveau registre ni notification ; le plan, les publications et la pénalité existaient déjà.",
       [effect('coordination', 'negociation-attestation-egalite-simplifiee',
               "Retrait de la prescription probatoire spéciale, sans compter un second procès-verbal supprimé.",
               "Défaut d'accord attesté par procès-verbal dans les entreprises d'au moins 300 salariés, en plus du régime général de désaccord.",
               "Preuve libre pour L2242-8, avec maintien du procès-verbal général lorsqu'il est requis ; sanction et plafond de 1 % inchangés.",
               'legal_duty', "Entreprises d'au moins 300 salariés pour l'attestation ; seuil général de sanction maintenu à 50 salariés.",
               "Contrôles et procédures en cours à l'entrée en vigueur ; anciens actes conservés et règle répressive plus douce réservée.",
               "Pas d'attestation de remplacement et pas de dispense de fond en matière d'égalité.",
               "Dans les entreprises d'au moins 300 salariés, ce défaut d'accord est attesté par un procès-verbal de désaccord.",
               "L'absence d'accord peut être établie par tout moyen, sans attestation particulière imposée par le présent article.")],
       classification='coordination_only')

retain('L2242-9',
       "Maintien intégral nécessaire d'un rescrit facultatif protecteur : l'employeur peut demander une appréciation de conformité et opposer la réponse favorable à l'administration. Le silence-rejet, la clôture d'accès après ouverture d'un contrôle et les deux périodes de garantie encadrent ce bénéfice ; la source n'impose aucune demande préalable à l'emploi ni à la négociation.",
       "Les cinq alinéas sont maintenus : demande de l'employeur, silence-rejet selon délai réglementaire, irrecevabilité après début du contrôle avec information par tout moyen, opposabilité jusqu'au terme de renégociation pour l'accord, et jusqu'au terme de la première année après dépôt pour le plan. L. 2242-8 reste opérant après sa seule coordination probatoire ; son rescrit n'est donc pas orphelin. Les renvois L. 2242-3, L. 2242-11, L. 2242-12 et L. 2242-13 restent dans leur champ. Aucune conversion du silence en conformité de fond ni suppression d'une voie de sécurisation favorable.",
       "Aucune réduction nouvelle : conservation d'une voie facultative de sécurité juridique et de ses deux protections temporelles contre la pénalité d'égalité.",
       "Le délai du décret n'est pas chiffré dans la source et n'est pas inventé. Aucun bénéfice de rescrit après ouverture d'un contrôle n'est créé.",
       "Aucune charge nouvelle n'est identifiée : le rescrit reste une faculté sans dépôt obligatoire, données nouvelles ni procédure de remplacement.")

retain('L2242-10',
       "Maintien intégral : la négociation d'organisation est une faculté ouverte à l'employeur et aux syndicats représentatifs. Elle permet d'adapter calendrier, périodicité, thèmes et modalités au groupe, à l'entreprise ou à l'établissement ; elle n'est ni un agrément ni une négociation préalable imposée.",
       "Le champ est celui des entreprises L. 2242-1, lu dans le corpus. La proposition L. 2242-11 retire une mention formelle obligatoire de l'accord sans supprimer cette faculté de négocier. Les majorités de validité et le consentement ne sont pas modifiés par ce texte ; aucune transmission supprimée en L2232 n'est recréée.",
       "La source entière autorise une adaptation négociée utile ; aucune suppression autonome ni économie n'est revendiquée.",
       "Les règles de validité des accords et les négociations de fond obligatoires subsistent ; aucune extension hors du champ L. 2242-1 n'est décidée.",
       "Aucune charge nouvelle n'est identifiée : aucune obligation de conclure ou de demander une autorisation ne s'ajoute à la faculté source.")

p = source_paragraphs('L2242-11')
p[3] = "3° Abrogé ;"
p.append("La suppression de la mention obligatoire du calendrier et des lieux des réunions dans l'accord s'applique aux accords conclus à compter de l'entrée en vigueur de la loi. Les parties peuvent toujours convenir de ces éléments dans l'accord. Les modalités supplétives de l'article L. 2242-14 demeurent applicables dans leur champ propre. Les stipulations valablement convenues avant cette date conservent leur portée ; aucun accord antérieur n'est à refaire du seul fait de cette suppression.")
reduce('L2242-11', paragraphs(*p),
       "Réforme de fond : retrait du 3° qui impose de contractualiser lieux et calendrier des réunions dans l'accord d'organisation. La négociation peut organiser concrètement ses réunions sans en faire une rubrique obligatoire de cet accord ; L. 2242-14 conserve sa fonction dans le seul champ supplétif. Les numéros des autres rubriques, les thèmes et leur contenu, les informations et leur date de remise, le suivi des engagements et le plafond de quatre ans sont conservés.",
       "Le 3° demeure à son emplacement comme abrogé : aucun décalage des 4° et 5°. Le 1° vise toujours les 1° et 2° de L. 2242-1 ainsi que L. 2242-2 et L. 2242-2-1. La périodicité et la durée maximale de quatre ans ne sont ni allongées ni supprimées. L. 2242-14 relève de la section des dispositions supplétives : il règle la première réunion dans son champ propre et n'est pas rendu universel par la suppression du 3°. L. 2242-6 garde également le calendrier utile à la négociation sérieuse et loyale dans son champ. La présente mesure retire la contractualisation imposée, sans affirmer qu'il existait nécessairement deux formalités cumulatives dans chaque entreprise. Le calendrier reste librement contractualisable ; la réforme ne retire pas les clauses existantes sans accord des parties et n'exige pas de nouvel avenant.",
       ["Contractualisation obligatoire du calendrier et des lieux des réunions dans l'accord organisant les négociations, supprimée sans nouvelle formalité de fixation en remplacement."],
       "L'accord n'a plus à contenir la rubrique légale de calendrier et lieux ; les parties restent libres d'organiser leurs réunions, et les modalités supplétives demeurent dans leur propre champ. Allègement de contenu obligatoire, sans baisse de fréquence de négociation.",
       "Les accords ayant volontairement ou antérieurement fixé un calendrier restent opposables ; aucun gain de temps ni coût global n'est chiffré.",
       "Aucune charge nouvelle n'est identifiée : aucun calendrier séparé, avenant ou déclaration ne remplace le 3° ; le rappel de L2242-14 ne l'étend pas aux cas où l'accord écarte les règles supplétives.",
       [effect('obligation_removed', 'negociation-accord-sans-calendrier-impose',
               "Suppression de la rubrique de calendrier et lieux imposée au contenu de l'accord d'organisation.",
               "Calendrier et lieux obligatoirement stipulés dans l'accord L2242-11 ; L2242-14 traite séparément le cas des modalités supplétives.",
               "Rubrique 3° abrogée ; stipulation conventionnelle facultative, règles de première réunion conservées dans leur seul champ supplétif.",
               'legal_duty', "Parties concluant l'accord d'organisation des négociations L2242-10.",
               "Accords conclus après entrée en vigueur ; clauses antérieures et plafond de quatre ans préservés.",
               "Aucune pièce, déclaration ni avenant obligatoire de remplacement.",
               "3° Le calendrier et les lieux des réunions ;", "La suppression de la mention obligatoire du calendrier et des lieux des réunions dans l'accord s'applique aux accords conclus à compter de l'entrée en vigueur de la loi.")])

retain('L2242-12',
       "Maintien intégral d'une faculté favorable d'aménager la périodicité de renégociation par accord dans chaque domaine. Le plafond de quatre ans assure la régularité minimale des négociations sans imposer l'annualité quand un accord valable y déroge.",
       "Les renvois couvrent exactement les 1° et 2° de L. 2242-1, L. 2242-2 et L. 2242-2-1, tous lus. La limite de quatre ans est cohérente avec L. 2242-11 et avec les obligations d'ordre public de ces articles. La suppression du calendrier obligatoire au 3° de L. 2242-11 ne remet pas en cause les dates et périodicités effectivement convenues.",
       "Faculté d'espacement conventionnel conservée pour les accords futurs comme en vigueur ; aucune réduction supplémentaire revendiquée.",
       "L'article ne dispense pas de négociation au-delà de quatre ans et ne traite pas de la durée du contrat de travail ou du préavis.",
       "Aucune charge nouvelle n'est identifiée : la faculté, ses domaines et son plafond de quatre ans sont conservés sans pièce ou procédure ajoutée.")

retain('L2242-13',
       "Maintien intégral des règles supplétives de négociation et de saisine syndicale. Les négociations rémunération/égalité et GEPP/salariés expérimentés, les délais d'information de tous les syndicats et de convocation garantissent une participation effective. Les accords L. 2242-11 et L. 2242-12 permettent déjà une autre périodicité ; une suppression des règles supplétives laisserait sans calendrier les entreprises sans accord.",
       "Conserver les quatre numéros : deux négociations annuelles, deux thèmes triennaux aux seuils et champs propres, relance après douze ou trente-six mois, information des autres syndicats dans huit jours et convocation dans quinze jours. La source emploie le singulier « la négociation triennale » après avoir ajouté un second thème triennal au 4° : ambiguïté préexistante signalée, sans effacer le 4° ni prétendre qu'il n'aurait pas de relance. L'information sous huit jours n'est pas assimilée aux transmissions CPPNI supprimées par negociation_collective. Sa fusion dans la convocation à quinze jours retarderait l'information des autres syndicats ; ce gain n'est pas revendiqué.",
       "La source entière demeure le calendrier supplétif et la garantie de saisine ; aucune économie issue d'une simple reformulation n'est annoncée.",
       "L'ambiguïté du singulier dans l'alinéa de relance est signalée ; les délais de huit et quinze jours et les champs d'effectif restent ceux de la source.",
       "Aucune charge nouvelle n'est identifiée : obligations, délais et destinataires sont intégralement ceux de la source, sans nouveau rapport.")

retain('L2242-14',
       "Maintien intégral de l'information d'organisation à la première réunion : lieu, calendrier et informations à remettre avec leur date. Cette garantie rend la négociation praticable dans le champ des dispositions supplétives ; la suppression du 3° obligatoire de l'accord L. 2242-11 ne rend pas L. 2242-14 applicable à toutes les négociations sous accord.",
       "Conserver les deux numéros et les destinataires, délégués syndicaux et salariés de la délégation. La source n'exige ni procès-verbal propre à cette première réunion ni dépôt de ces précisions ; aucun support supplémentaire n'est créé. Les parties peuvent encore inscrire le calendrier dans leur accord sans obligation légale de le faire.",
       "Organisation supplétive effective conservée ; le retrait de la rubrique obligatoire de l'accord est porté uniquement par L. 2242-11, sans le compter une seconde fois ici.",
       "L'article ne fixe pas la périodicité ni les délais de convocation ; la suppression d'un lieu ou d'un calendrier effectif n'est pas proposée.",
       "Aucune charge nouvelle n'est identifiée : les mêmes informations doivent être précisées à la même réunion, sans écrit ou dépôt additionnel.")

retain('L2242-15',
       "Maintien intégral des quatre thèmes de la négociation salariale : salaires, durée du travail, partage de la valeur en l'absence des dispositifs déjà prévus et suivi de l'égalité de rémunération et de carrière. La réserve liée aux accords existants évite déjà une négociation doublonnée sur l'épargne salariale ; aucun prélèvement, agrément ou rapport distinct n'est créé ici.",
       "Toutes les exceptions du 3° sont conservées : intéressement, participation, PEE, plan de mise à la retraite collectif et accord de branche couvrant au moins un dispositif. Les deux voies d'affectation retraite/entreprises solidaires et les renvois L. 3334-1, L. 3334-13, CMF L. 224-14 et L. 224-3 restent dans leur champ ; les groupements d'employeurs demeurent visés. Ces renvois extérieurs ne figurent pas parmi les cibles de reference-targets et ne sont pas présentés comme réécrits. Le seuil hebdomadaire de quarante heures du contrat unique n'impose ici aucun relèvement des seuils annuels. Les notes de 2019 mentionnent le 1er octobre 2019 comme date effective de la réforme d'épargne, sans fixer celle du projet.",
       "La norme de négociation et ses dispenses en présence d'accords d'épargne sont conservées ; aucune baisse de cotisations ni modification des produits d'épargne n'est démontrée.",
       "Les codes monétaire et financier et les régimes d'épargne restent distincts ; la portée fiscale de leurs avantages n'est pas recalibrée par cet article.",
       "Aucune charge nouvelle n'est identifiée : quatre thèmes, exceptions et groupements concernés restent exactement ceux de la source intégrale.")

retain('L2242-16',
       "Maintien intégral de la transparence sur les mises à disposition auprès des organisations de salariés ou d'employeurs. L'information accompagne la négociation existante ou répond, hors obligation annuelle, à une demande du salarié. Elle protège l'indépendance et la connaissance du financement de la représentation sans exiger de déclaration administrative ou de modèle distinct.",
       "Conserver la distinction entre entreprises soumises à la négociation L. 2242-15 et information sur demande dans les autres entreprises, ainsi que les deux catégories d'organisations visées à L. 2231-1. Il ne s'agit pas du rapport annuel CPPNI supprimé en L2232. Le texte source n'impose pas de copie de rapport, de périodicité additionnelle ni de dépôt qui pourrait être retiré ici.",
       "Information ciblée conservée pour l'indépendance de la négociation ; aucune suppression de charge autonome revendiquée.",
       "Le contenu des conventions de mise à disposition et leur financement ne sont pas modifiés ; aucun inventaire administratif nouveau n'est créé.",
       "Aucune charge nouvelle n'est identifiée : maintien des mêmes informations et des mêmes bénéficiaires, sans modèle ni transmission nouvelle.")

p = source_paragraphs('L2242-17')
old = p[9]
assert old.startswith('7° ')
p[9] = ("7° Les modalités du plein exercice par le salarié de son droit à la déconnexion et la mise en place par l'entreprise de dispositifs de régulation de l'utilisation des outils numériques, en vue d'assurer le respect des temps de repos et de congé ainsi que de la vie personnelle et familiale. A défaut d'accord, l'employeur, après avis du comité social et économique, définit ces modalités et prévoit la mise en œuvre d'actions de formation et de sensibilisation destinées aux salariés et au personnel d'encadrement et de direction pour un usage raisonnable des outils numériques. Ces modalités et actions peuvent être intégrées aux documents d'organisation déjà utilisés ; aucune charte ni document distinct n'est obligatoire à ce titre ;")
p.append("La dispense de charte ou de document distinct s'applique à compter de l'entrée en vigueur de la loi, y compris lorsque les modalités de déconnexion doivent être définies ou actualisées dans une procédure en cours. Les chartes et accords antérieurs conservent leurs effets ; aucun document existant n'est à refaire. Le droit à la déconnexion, les temps de repos et de congé, la consultation du comité social et économique et les actions de formation et de sensibilisation demeurent garantis.")
reduce('L2242-17', paragraphs(*p),
       "Réforme de fond ciblée au 7° : suppression de la charte obligatoire de déconnexion en l'absence d'accord, avec faculté d'intégrer les mêmes modalités et actions aux documents d'organisation existants. Le droit, les dispositifs de régulation, l'avis du CSE et la formation de tous les publics visés restent dus. Les huit thèmes et tous les avantages de protection complémentaire et de retraite sont conservés.",
       "Lecture intégrale, y compris les deux alinéas distincts rattachés aux 2° et 5° : maintien du supplément de cotisations vieillesse et de sa prise en charge patronale, du régime forestier, de la couverture au moins aussi favorable que L. 911-7 et de l'ensemble des garanties L. 911-2. Ces trois cibles sont vérifiées dans reference_checks. Au 3°, L. 6315-1 a également été lu dans le corpus, dans sa version comportant entretiens à quatre ans et état récapitulatif à huit ans : les II et III restent bien des dispositions de parcours/abondement, sans droit à la formation effacé. Le 8° garde le champ L. 2143-3 avec cinquante salariés au même site et les deux références de frais de mobilité. La dispense de charte ne supprime aucun reporting de solidarité ni garantie et ne rétablit aucun état annuel déjà retiré. La note du 31 mars 2022 reste historique. Les règles de santé, repos et non-discrimination ainsi que les obligations supérieures d'information/consultation ne sont pas supprimées.",
       ["Charte obligatoire distincte de déconnexion en l'absence d'accord, sans suppression des modalités, des actions de formation ou de l'avis du CSE."],
       "La formalisation en charte imposée est retirée ; les dispositifs, consultations et informations utiles subsistent. Ce gain de support ne vaut ni suppression du droit à la déconnexion ni baisse de prélèvements.",
       "Les huit thèmes restent négociables dans leurs champs et périodicités ; aucune économie de temps de formation ou de consultation n'est revendiquée. Coût net non chiffré.",
       "Aucune charge nouvelle n'est identifiée : modalités, régulation, avis du CSE, formation et sensibilisation étaient déjà exigés par la source ; aucun registre, déclaration ou document substitutif n'est ajouté.",
       [effect('obligation_removed', 'deconnexion-charte-distincte-supprimee',
               "Suppression de la charte imposée comme support de la déconnexion en l'absence d'accord.",
               "Employeur tenu d'élaborer une charte après avis du CSE, comportant modalités de déconnexion et actions de formation/sensibilisation.",
               "Modalités, avis du CSE et actions maintenus, avec intégration possible dans les documents existants et sans charte ni document distinct obligatoire.",
               'legal_duty', "Entreprises relevant de la négociation égalité/QVCT et dépourvues d'accord de déconnexion.",
               "Entrée en vigueur, y compris procédures en cours ; chartes et accords valables antérieurs conservés, sans réfection obligatoire.",
               "Même contenu protecteur et consultation ; aucune attestation ou déclaration de remplacement.",
               "A défaut d'accord, l'employeur élabore une charte, après avis du comité social et économique.",
               "Ces modalités et actions peuvent être intégrées aux documents d'organisation déjà utilisés ; aucune charte ni document distinct n'est obligatoire à ce titre ;")])
answers['L2242-17']['benefit_review'] = (
    "Le 2° conserve la possibilité de cotiser à la vieillesse sur le salaire à temps plein et la prise en charge patronale du supplément, avec l'exclusion de CSG prévue par L. 241-3-1 dans son champ. Le 5° conserve les régimes au moins aussi favorables que L. 911-7, dont le financement patronal minimal de moitié et les dispenses d'adhésion dans leur champ propre, ainsi que l'accès forestier aux garanties L. 911-2. Les futurs salariés éligibles du contrat unique ne sont pas exclus par la négociation, qui ne fixe aucun terme d'emploi. Le 8° maintient les mesures de coût de mobilité et les prises en charge de frais ; la suppression de la charte au 7° ne réduit ni repos, ni congé, ni formation, ni droit à la déconnexion.")

proposed = paragraphs(
    "La négociation sur l'insertion professionnelle et le maintien dans l'emploi des travailleurs handicapés s'appuie sur les informations relatives à la situation de l'entreprise au regard de l'obligation d'emploi des travailleurs handicapés prévue aux articles L. 5212-1 et suivants. L'employeur met ces informations à la disposition des négociateurs à partir des données et documents utilisés pour cette obligation ; il n'est pas tenu d'établir un rapport distinct pour la négociation. Les informations nécessaires qui ne figurent pas dans ces documents restent communiquées aux négociateurs, sans format de rapport imposé.",
    "La dispense de rapport s'applique aux négociations en cours ou ouvertes à compter de l'entrée en vigueur de la loi. Les informations ou rapports déjà communiqués ne sont pas à établir de nouveau. Elle ne supprime ni l'obligation d'emploi, ni ses déclarations autonomes, ni les mesures d'insertion ou de maintien dans l'emploi, ni les droits et recours relatifs aux périodes antérieures.")
reduce('L2242-18', proposed,
       "Réforme de fond : suppression du rapport patronal imposé comme support de négociation sur le handicap. La situation au regard de l'obligation d'emploi reste présentée aux négociateurs au moyen des données et pièces de son suivi, avec les seuls compléments nécessaires. Il s'agit du retrait d'un rapport dédié, non d'une affirmation que toutes les informations existent déjà ou d'une suppression de l'obligation d'emploi.",
       "Le renvoi L. 5212-1 et suivants conserve son objet : obligation d'emploi des travailleurs handicapés. Les formalités déclaratives autonomes de ce chapitre ne sont pas abrogées dans ce lot ; la dispense porte seulement sur le support exigé par L. 2242-18. Le 4° de L. 2242-17 conserve accès à l'emploi, formation, promotion, conditions de travail et sensibilisation de tout le personnel. Aucun accès nouveau à des données de santé ou registre nominatif n'est autorisé ; droits des négociateurs et règles de confidentialité restent applicables.",
       ["Rapport distinct établi par l'employeur et imposé comme base de la négociation sur l'obligation d'emploi des travailleurs handicapés."],
       "Le support de rapport spécialement exigé est supprimé ; la présentation de la situation et les informations utiles demeurent. Le gain est documentaire et ne diminue aucun droit d'insertion.",
       "Le volume des compléments dépend des données effectivement disponibles ; aucune suppression de la déclaration d'emploi ni baisse de contribution handicap n'est démontrée.",
       "Aucune charge nouvelle n'est identifiée : les informations de situation étaient déjà nécessaires au rapport ; leur communication sans format imposé ne crée ni nouveau fichier, ni dépôt, ni collecte de données de santé.",
       [effect('obligation_removed', 'handicap-negociation-rapport-distinct-supprime',
               "Retrait du rapport spécialement établi pour la négociation handicap.",
               "Rapport de l'employeur présentant la situation au regard de l'obligation d'emploi imposé comme base de négociation.",
               "Informations de situation accessibles à partir des données et documents de suivi, sans rapport distinct ; compléments utiles maintenus.",
               'legal_duty', "Employeurs et négociateurs de l'insertion et du maintien dans l'emploi des travailleurs handicapés.",
               "Négociations en cours ou futures dès l'entrée en vigueur ; pas de réfection des informations déjà remises.",
               "Communication du même contenu utile, sans nouveau modèle, registre ou accès aux données sensibles.",
               "La négociation sur l'insertion professionnelle et le maintien dans l'emploi des travailleurs handicapés se déroule sur la base d'un rapport établi par l'employeur présentant la situation par rapport à l'obligation d'emploi des travailleurs handicapés prévue par les articles L. 5212-1 et suivants.",
               "L'employeur met ces informations à la disposition des négociateurs à partir des données et documents utilisés pour cette obligation ; il n'est pas tenu d'établir un rapport distinct pour la négociation.")])

proposed = paragraphs(
    "La négociation prévue à l'article L. 2242-17 peut également porter sur la prévention des effets de l'exposition aux facteurs de risques professionnels prévue à l'article L. 4161-1. L'accord conclu sur ce thème dans le cadre du présent article vaut conclusion de l'accord mentionné à l'article L. 4162-1, sous réserve du respect des autres dispositions du chapitre II du titre VI du livre Ier de la quatrième partie du présent code.",
    "Cette coordination s'applique aux accords conclus à compter de l'entrée en vigueur de la loi. Aucun accord antérieur n'est à renégocier ou à déposer de nouveau du seul fait de la rectification des références. Les obligations de prévention, les conditions de fond et les droits et recours relatifs aux accords et aux expositions antérieurs demeurent soumis aux dispositions qui leur sont applicables.")
base('L2242-19', proposed,
     "Coordination nécessaire, sans réforme de taux ni nouvelle fusion comptée : rectification d'un renvoi devenu incohérent. L. 4163-3 ne régit plus un accord de prévention ; l'accord est aujourd'hui celui de L. 4162-1, encadré au chapitre II. La faculté de traiter ce thème dans la négociation L. 2242-17 et l'effet d'accord unique sont maintenus avec leurs conditions, non simplement reformulés.",
     "Incohérence préexistante constatée par lecture intégrale des sources locales L. 4163-3, L. 4162-1, L. 4162-2 et L. 4162-3 : L. 4163-3 écarte une présomption de manquement de sécurité tirée de la déclaration d'exposition ; il ne définit aucun accord. Le chapitre II fixe négociation, plan subsidiaire, thèmes, durée maximale de trois ans et dépôt ; ces conditions sont maintenues par le renvoi corrigé. Nouveaux renvois L. 4162-1 et chapitre II non fournis comme cibles dans reference-targets.json : leur contenu a été lu dans travail.json et leur ajout est signalé ici. Les notes historiques des textes L. 4162-2/3 et L. 4163-3 réservent notamment les expositions 2015-2017 et l'ancien chapitre III jusqu'au 31 décembre 2018 ; la rectification prospective ne réécrit pas leur régime. Les dépôts autonomes des accords de prévention ne sont pas confondus avec le dépôt du procès-verbal de désaccord supprimé en L. 2242-5.",
     'coordination_only',
     "Renvoi rectifié vers le régime actuel d'accord de prévention ; aucune obligation supprimée de nouveau et aucune diminution des garanties de santé démontrée.",
     "Les accords et expositions anciens conservent leur régime historique ; le lot ne réécrit pas le chapitre de prévention ni les règles européennes de santé au travail.",
     "Aucune charge nouvelle n'est identifiée : le même accord peut satisfaire les deux négociations, sous les conditions autonomes déjà existantes, sans nouveau dépôt ni renégociation automatique.",
     [effect('coordination', 'negociation-prevention-accord-unique',
             "Mise en cohérence du renvoi définissant l'accord de prévention bénéficiant de l'équivalence.",
             "Renvoi à L4163-3 et au chapitre III, alors que L4163-3 actuel ne définit pas d'accord.",
             "Renvoi à l'accord L4162-1 et aux conditions du chapitre II, sans nouvelle dispense de protection.",
             'regime', "Entreprises concluant un accord de prévention dans la négociation égalité/QVCT.",
             "Accords futurs après entrée en vigueur ; aucun ancien accord à refaire et régimes historiques préservés.",
             "Aucune formalité créée ; les conditions actuelles de prévention restent requises.",
             "L'accord conclu sur ce thème dans le cadre du présent article vaut conclusion de l'accord mentionné à l'article L. 4163-3, sous réserve du respect des autres dispositions prévues au chapitre III du titre VI du livre Ier de la quatrième partie du présent code.",
             "L'accord conclu sur ce thème dans le cadre du présent article vaut conclusion de l'accord mentionné à l'article L. 4162-1, sous réserve du respect des autres dispositions du chapitre II du titre VI du livre Ier de la quatrième partie du présent code.")])

retain('L2242-19-1',
       "Maintien intégral : faculté de négocier sur la qualité des conditions de travail, la santé, la sécurité et la prévention, avec appui possible des acteurs locaux et régionaux. Aucune consultation de ces acteurs, aucun agrément, délai ou rapport n'est imposé ; supprimer la faculté réduirait l'accès à un appui de prévention utile.",
       "Le renvoi à L. 2242-17 reste la négociation égalité/QVCT. Le texte complète L. 2242-19, dont le renvoi de prévention est rectifié, sans transformer son appui facultatif en étape obligatoire. La note de la loi du 2 août 2021 fixe le 31 mars 2022 et renvoie à son II pour les conditions d'application ; elle n'est pas utilisée comme date de la réforme future.",
       "Champ facultatif de négociation et d'assistance conservé ; aucune diminution de prélèvement ni formalité retirée n'est démontrée.",
       "Les obligations autonomes de prévention et de consultation ne sont pas supprimées ; l'article ne règle pas le financement des acteurs d'appui.",
       "Aucune charge nouvelle n'est identifiée : ni négociation supplémentaire obligatoire, ni recours obligatoire à un prestataire ne sont ajoutés.")

p = source_paragraphs('L2242-20')
p[0] = p[0].replace('L. 2323-10', 'L. 2312-24')
p[2] = "2° Le cas échéant, les conditions de la mobilité professionnelle ou géographique interne à l'entreprise prévue à l'article L. 2254-2, sans obligation de les présenter dans un chapitre spécifique de l'accord ;"
p[4] = ("4° Les perspectives de recours par l'employeur au contrat de travail unique à durée indéterminée pour les nouvelles embauches, au travail à temps partiel et aux stages, ainsi que les moyens mis en œuvre pour diminuer la précarité de l'emploi dans l'entreprise. Pour les contrats conclus avant l'entrée en vigueur de la loi instituant le contrat unique, la négociation prend en compte leur poursuite et les droits qui leur sont attachés ; elle ne permet ni nouveau contrat à durée déterminée ni renouvellement décidé après cette date. La durée limitée d'une affectation, d'une mission, d'un chantier, d'une formation ou d'une aide ne détermine pas le terme de l'emploi nouveau ;")
p[7] = "Aucun bilan à l'échéance de l'accord n'est imposé par le présent article. Les engagements de suivi ou de bilan librement souscrits par les parties restent applicables."
p.append("La suppression du chapitre spécifique obligatoire et du bilan légal d'échéance s'applique aux accords conclus à compter de l'entrée en vigueur de la loi. Les stipulations et droits attachés aux accords antérieurs demeurent applicables ; aucun bilan déjà réalisé n'est à refaire. La rectification du renvoi aux orientations stratégiques n'impose aucune nouvelle consultation ni reprise d'une procédure déjà accomplie. Les règles de formation, de mobilité et de protection des salariés ainsi que les aides et avantages ouverts aux situations futures éligibles gardent leur champ propre ; la fin d'une période de formation, d'affectation ou d'aide ne vaut pas rupture du contrat unique.")
reduce('L2242-20', paragraphs(*p),
       "Réforme de fond : suppression du chapitre séparé obligatoire pour la mobilité et du bilan légal à l'échéance de l'accord, sans supprimer les engagements conventionnels de suivi. Coordination substantielle du 4° avec l'absence de nouveaux CDD et la distinction entre durée de mission/formation et durée d'emploi. Rectification explicite de l'ancien renvoi L. 2323-10 vers L. 2312-24. Les six thèmes, les champs d'effectif et les droits de formation, de carrière syndicale et de sous-traitance sont maintenus.",
       "Maintien des seuils : entreprises/groupes d'au moins 300 salariés et dimension communautaire avec établissement ou entreprise d'au moins 150 salariés en France ; négociation tous les trois ans sous réserve des aménagements L. 2242-11/12. Le 3° garde les orientations de formation à trois ans, toutes priorités, compétences, qualifications et abondements CPF. La source cite L. 2323-10, absent du corpus en vigueur ; L. 2312-24 a été lu en entier et traite expressément des orientations stratégiques, de leurs conséquences et de la GEPP. Ce nouveau renvoi n'est pas une cible fournie dans reference-targets.json ; il est signalé et ne crée aucune consultation supplémentaire. La source de L. 2312-24 mentionne encore intérim et contrats temporaires : ce thème de consultation n'autorise aucun nouveau CDD contre L. 1221-2 proposé ; sa terminologie devra être coordonnée pour les anciennes situations et les affectations temporaires, sans prétendre la cible déjà réécrite. La suppression du chapitre au 2° ne supprime ni l'accord de performance collective ni les refus et garanties de L. 2254-2, vérifiés avec les cibles de rupture. Le bilan source n'était pas nécessairement un rapport distinct : sa suppression est celle de l'obligation d'évaluation finale, pas la preuve d'un document entier économisé. Les clauses de bilan des anciens accords ne sont pas annulées. Aucun terme nouveau d'emploi ni régime spécial de CDD n'est rétabli.",
       ["Présentation obligatoire des conditions de mobilité interne dans un chapitre spécifique de l'accord collectif.",
        "Réalisation obligatoire d'un bilan à l'échéance de l'accord, indépendamment des engagements conventionnels de suivi."],
       "Deux contraintes légales sont retirées : séparation formelle du chapitre mobilité et bilan final imposé. La source autorisait la négociation de différentes formes d'emploi ; le texte coordonne désormais l'interdiction des nouveaux CDD, qui est une contrainte substantielle sur le choix contractuel. Le solde net n'est pas établi. Cette coordination et celle du CSE ne sont pas comptées comme de nouvelles réductions d'emploi ou de préavis.",
       "L'emploi nouveau à durée indéterminée peut avoir des effets propres non chiffrés sur l'organisation ; anciens contrats, suivi convenu, formation et procédures de rupture restent dans leur régime.",
       "La coordination du contrat unique inscrit dans cet article une contrainte absente de sa source : les nouvelles embauches ne peuvent plus être conclues à terme ni renouvelées en CDD. Cette limitation vient de la mesure générale, sans être comptée comme réduction supplémentaire. Aucune autre charge nouvelle n'est identifiée : thèmes déjà obligatoires, aucun registre, donnée, déclaration ou délai ajouté. Les deux contraintes de forme et de bilan sont retirées ; le solde net de coûts n'est pas établi.",
       [effect('obligation_removed', 'gepp-chapitre-mobilite-distinct-supprime',
               "Suppression de la séparation formelle obligatoire du chapitre de mobilité.",
               "Conditions de mobilité L2254-2 obligatoirement présentées dans un chapitre spécifique en cas d'accord.",
               "Même thème et garanties L2254-2, sans chapitre spécifique obligatoire.",
               'legal_duty', "Entreprises et groupes dans le champ de la négociation GEPP L2242-20.",
               "Accords conclus à compter de l'entrée en vigueur ; clauses antérieures et droits des salariés conservés.",
               "Aucun document ou déclaration de remplacement ; droit au refus dans l'accord de performance maintenu.",
               "2° Le cas échéant, les conditions de la mobilité professionnelle ou géographique interne à l'entreprise prévue à l'article L. 2254-2, qui doivent, en cas d'accord, faire l'objet d'un chapitre spécifique ;",
               "2° Le cas échéant, les conditions de la mobilité professionnelle ou géographique interne à l'entreprise prévue à l'article L. 2254-2, sans obligation de les présenter dans un chapitre spécifique de l'accord ;"),
        effect('obligation_removed', 'gepp-bilan-terminal-obligatoire-supprime',
               "Suppression du bilan légal de fin d'accord, sans suppression du suivi conventionnel.",
               "Bilan obligatoire à l'échéance de chaque accord du champ de l'article, sans support distinct expressément exigé par la source.",
               "Aucun bilan légal imposé par cet article pour les nouveaux accords ; engagements conventionnels de bilan ou suivi applicables.",
               'legal_duty', "Parties aux accords GEPP du champ L2242-20.",
               "Nouveaux accords après entrée en vigueur ; bilans et clauses des accords antérieurs conservés.",
               "Aucune attestation finale substitutive ; pas de diminution des droits conventionnels acquis.",
               "Un bilan est réalisé à l'échéance de l'accord.",
               "Aucun bilan à l'échéance de l'accord n'est imposé par le présent article."),
        effect('coordination', 'contrat-unique-nouvelles-embauches',
               "Alignement du thème des formes d'emploi sur le contrat unique, sans suppression supplémentaire de CDD comptée ici.",
               "Négociation sur différents contrats et diminution des emplois précaires au profit des CDI, dans un système autorisant de nouveaux CDD.",
               "Négociation sur le contrat unique, le temps partiel, les stages et la réduction de la précarité ; pas de nouveau CDD ni de terme d'emploi lié à la mission.",
               'regime', "Nouvelles embauches privées des entreprises concernées ; contrats anciens distincts.",
               "Bascule de L1221-2 ; contrats anciens, ancienneté et droits attachés préservés, aucun renouvellement nouveau de CDD.",
               "Interdiction du terme pour l'emploi nouveau et du renouvellement de CDD : contrainte de choix contractuel coordonnée avec la mesure générale, sans gain autonome ni coût net présumé. Aucun nouveau dossier de formation ou d'aide.",
               "4° Les perspectives de recours par l'employeur aux différents contrats de travail, au travail à temps partiel et aux stages, ainsi que les moyens mis en œuvre pour diminuer le recours aux emplois précaires dans l'entreprise au profit des contrats à durée indéterminée ;",
               "La durée limitée d'une affectation, d'une mission, d'un chantier, d'une formation ou d'une aide ne détermine pas le terme de l'emploi nouveau ;")], classification='mixed')

retain('L2242-21',
       "Maintien intégral après contrôle des sept facultés complémentaires : négocier les procédures collectives dans leur cadre propre, les emplois menacés, les sous-traitants et territoires, les congés de mobilité, l'alternance/stages et la reconversion externe. L'équivalence de l'accord de reconversion évite déjà une négociation distincte ; supprimer cette faculté retirerait un avantage sans retirer de charge obligatoire.",
       "Les 1° à 7° et l'alinéa d'équivalence sont conservés. L. 1233-21/22 et L. 1237-18 ont été lus : procédures collectives, réponses motivées, expertise et congés ne sont pas absorbés par un préavis individuel. Les quatre cibles requises sont examinées dans reference_checks. L. 6324-9 proposé retire son attente de trois mois et son procès-verbal distinct dans son propre A ; L. 2242-21 n'en rétablit aucun par son simple renvoi. Les durées pédagogiques, de mission et de reconversion ne deviennent pas des termes de l'emploi. La note de source fixe le 1er janvier 2026 pour cette version ; la note de la cible maintient séparément les anciens avenants conclus avant cette date. Aucune source officielle n'est confondue avec une proposition.",
       "Facultés et effet d'accord unique conservés, sans réduction supplémentaire comptée. Le renvoi n'impose ni attente ni second dépôt supprimés dans la proposition cible.",
       "L'article ne décide aucune rupture : seuils, consentements, indemnisations et transitions relèvent des régimes cibles ; leurs effets financiers ne sont pas chiffrés ici.",
       "Aucune charge nouvelle n'est identifiée : sept sujets restent facultatifs, aucun nouveau procès-verbal, délai, registre ni condition d'aide n'est introduit.")
answers['L2242-21']['benefit_review'] = (
    "Sont conservés pour les futurs salariés éligibles les congés de mobilité et leur accompagnement, l'insertion/alternance et les modalités de reconversion externe. L'effet de l'accord GEPP valant accord L. 6324-9 reste entier. La cible de reconversion conserve prise en charge d'écart de rémunération, possibilité d'allonger formation/reconversion, plancher des indemnités selon le régime légal applicable et CPF mobilisé avec accord du salarié ; aucun de ces avantages n'est limité aux anciens CDD. Le contrat unique n'a pas de terme de formation et les garanties ou indemnités spéciales ne sont pas ramenées au seul barème ordinaire. Les anciens avenants et droits acquis conservent leur transition propre.")

p = source_paragraphs('L2242-22')
p[1] = "Cette négociation porte sur les matières mentionnées à l'article L. 2241-14-1, sans obligation de diagnostic préalable."
p.append("La suppression du diagnostic préalable obligatoire s'applique aux négociations ouvertes ou en cours à compter de l'entrée en vigueur de la loi. Les informations nécessaires à une négociation effective restent mises à la disposition des négociateurs ; aucun diagnostic, rapport ou attestation de remplacement n'est exigé. Les diagnostics déjà établis restent utilisables, sans réfection obligatoire. Les accords, aides et droits antérieurement acquis conservent leur régime ; les financements de prévention restent accessibles aux futures situations éligibles selon leurs conditions propres.")
reduce('L2242-22', paragraphs(*p),
       "Réforme de fond : suppression de l'étape de diagnostic devant obligatoirement précéder la négociation sur les salariés expérimentés. Les informations nécessaires, tous les thèmes obligatoires et facultatifs, l'examen du fonds de prévention, le seuil de 300 salariés et la périodicité de trois ans sont maintenus. Le diagnostic peut toujours être réalisé volontairement, sans support substitutif imposé.",
       "L. 2241-14-1 et L. 2241-14-2 ont été lus en entier dans le corpus : recrutement, maintien, fins de carrière et transmission restent obligatoires ; compétences, transformations, management, accompagnement, santé et organisation restent facultatifs. Le renvoi aux matières n'importe pas l'obligation distincte de diagnostic de branche de L. 2241-14-1 : l'entreprise en est expressément dispensée au présent article. L. 221-1-5 CSS est vérifié dans reference_checks ; le devoir d'examiner les possibilités de mobilisation ne vaut ni droit automatique à subvention ni suppression des contrôles d'attribution. Les informations réglementaires demeurent nécessaires à une négociation réelle, mais ne doivent pas réintroduire un rapport de diagnostic obligatoire. Aucun transfert des règles de retraite des salariés privés aux agents publics.",
       ["Établissement d'un diagnostic préalable obligatoire comme étape conditionnant la négociation d'entreprise sur les salariés expérimentés."],
       "La négociation peut commencer sans achever préalablement un diagnostic imposé. Les informations utiles, thèmes et fonds demeurent ; pas de baisse de cotisations ou d'âge de retraite revendiquée.",
       "La source ne fixait ni format ni durée du diagnostic : aucune quantité de pages ou de jours économisés n'est inventée. L'obligation de branche et les diagnostics autonomes de prévention restent distincts.",
       "Aucune charge nouvelle n'est identifiée : les informations de négociation étaient déjà exigées, la condition préalable est retirée et aucun rapport, registre ou attestation ne la remplace.",
       [effect('obligation_removed', 'seniors-negociation-diagnostic-prealable-supprime',
               "Retrait du diagnostic obligatoire préalable à la négociation d'entreprise sur les salariés expérimentés.",
               "Négociation triennale des entreprises d'au moins 300 salariés précédée d'un diagnostic obligatoire, sans durée ni format source.",
               "Négociation sans condition de diagnostic préalable ; informations nécessaires et mêmes matières conservées.",
               'legal_duty', "Entreprises d'au moins 300 salariés dans le champ de L2242-2-1.",
               "Négociations nouvelles ou en cours à l'entrée en vigueur ; diagnostics existants réutilisables et accords anciens protégés.",
               "Pas de rapport substitutif ; examen des aides et données utiles déjà exigés maintenus.",
               "Cette négociation est précédée d'un diagnostic et porte sur les matières mentionnées à l'article L. 2241-14-1.",
               "Cette négociation porte sur les matières mentionnées à l'article L. 2241-14-1, sans obligation de diagnostic préalable.")])
answers['L2242-22']['benefit_review'] = (
    "Les matières favorables de recrutement et maintien en emploi, de retraite progressive ou de temps partiel de fin de carrière, et de transmission des savoirs demeurent négociées. L'examen des possibilités de financement du fonds L. 221-1-5 reste obligatoire dans le cadre prévu ; ses aides restent accessibles aux futurs bénéficiaires selon leur exposition et leurs conditions propres, sans condition de maintien du diagnostic supprimé ici. Aucune dotation ni garantie d'attribution n'est créée ; les financements, conventions et engagements acquis sont protégés.")

proposed = paragraphs(
    "Le fait de se soustraire aux obligations prévues à l'article L. 2242-1, relatives à la convocation des parties à la négociation et à l'obligation périodique de négocier, ou aux obligations prévues à l'article L. 2242-20 est puni d'une amende de 3 750 euros. Aucune peine d'emprisonnement n'est encourue sur le fondement du présent article.",
    "Le présent article réunit les incriminations antérieurement prévues aux articles L. 2243-1 et L. 2243-2, sans créer d'infraction pour un comportement qui n'était pas réprimé. Les mêmes faits ne peuvent être sanctionnés deux fois au titre de ces deux anciennes incriminations.",
    "Ces dispositions s'appliquent à compter de l'entrée en vigueur de la loi. La suppression de l'emprisonnement et toute disposition pénale plus douce s'appliquent aux faits antérieurs qui n'ont pas donné lieu à une condamnation définitive. La régularité des actes antérieurs, les droits des victimes et les réparations civiles ne sont pas remis en cause. Les infractions autonomes de discrimination, d'atteinte aux libertés syndicales ou de santé et sécurité restent soumises à leurs règles propres.")
reduce('L2243-1', proposed,
       "Réforme de fond : suppression de l'emprisonnement d'un an et réunion dans une incrimination unique des champs déjà réprimés par L. 2243-1 et L. 2243-2. L'amende de 3 750 euros, les obligations de négociation et les réparations restent maintenues pour garantir leur effectivité. Le champ L. 2242-20 n'est pas une infraction nouvelle, car il figure dans la source entière de L. 2243-2 abrogé parallèlement.",
       "Coordination indivisible avec l'abrogation de L. 2243-2 dans ce lot ; ne pas additionner deux suppressions de peine pour une même soustraction à la négociation. L. 2242-1 et L. 2242-20 restent les seuls fondements d'obligations réprimés ici ; aucune extension à tous les articles L2242 ni à un préavis individuel n'est créée. Le bilan et le chapitre séparé retirés de L. 2242-20 ne peuvent être rétablis par la sanction. La loi pénale plus douce est expressément réservée ; aucune réouverture générale des condamnations définitives ni suppression des droits des victimes n'est annoncée. L'exigence de sanctions effectives des droits collectifs demeure un point de contrôle supérieur ; la conservation de l'amende et des recours ne constitue pas à elle seule une validation de conformité internationale.",
       ["Peine d'emprisonnement d'un an pour soustraction aux obligations de négociation collective, remplacée par le maintien de la seule amende existante.",
        "Dédoublement des incriminations L2243-1 et L2243-2 pour le champ commun de soustraction à la négociation L2242-1."],
       "L'emprisonnement est supprimé et les deux incriminations sont réunies ; le plafond pécuniaire de 3 750 euros est inchangé. La fusion ne prouve pas l'existence antérieure de deux condamnations cumulables pour les mêmes faits.",
       "Les infractions de discrimination et d'entrave ayant un autre fondement subsistent. Aucune baisse de cotisations ni conformité supérieure présumée ne découle de cette dépénalisation partielle.",
       "Aucune charge nouvelle n'est identifiée au regard des deux sources réunies : les obligations L2242-20 étaient déjà pénalement couvertes par L2243-2 ; aucune déclaration ou sanction nouvelle n'est créée.",
       [effect('obligation_removed', 'negociation-sanction-unique-sans-prison',
               "Suppression de l'exposition à l'emprisonnement pour la soustraction à la négociation, avec maintien de l'amende.",
               "Un an d'emprisonnement et 3 750 euros d'amende pour les obligations L2242-1 ; champ L2242-20 déjà réprimé aux mêmes peines par L2243-2.",
               "Aucun emprisonnement de ce fondement ; amende de 3 750 euros pour les deux champs réunis, sans double sanction des mêmes faits.",
               'legal_duty', "Auteurs de soustractions aux obligations de négociation L2242-1 et L2242-20.",
               "Entrée en vigueur ; dispositions plus douces pour faits antérieurs non définitivement jugés ; réparations civiles conservées.",
               "Amende préexistante conservée, sans nouvelle infraction ni formalité substitutive.",
               "Le fait de se soustraire aux obligations prévues à l'article L. 2242-1, relatives à la convocation des parties à la négociation et à l'obligation périodique de négocier, est puni d'un emprisonnement d'un an et d'une amende de 3 750 euros.",
               "Aucune peine d'emprisonnement n'est encourue sur le fondement du présent article.")])

proposed = paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant cette abrogation.",
    "A compter de cette date, les faits de soustraction aux obligations des articles L. 2242-1 et L. 2242-20 relèvent de la seule incrimination de l'article L. 2243-1, dans son champ et selon les peines qu'il prévoit. Aucune peine d'emprisonnement ni seconde amende ne peut être prononcée sur le fondement du présent article abrogé pour des faits commis à compter de cette date.",
    "Pour les faits antérieurs non définitivement jugés, la suppression de l'emprisonnement et les autres dispositions pénales plus douces s'appliquent dans les conditions légales. Les actes de procédure régulièrement accomplis et les droits à réparation des victimes conservent leur portée ; les condamnations définitives ne font pas l'objet d'une remise en cause générale par la présente abrogation. Les obligations de négociation maintenues, les infractions autonomes et les recours fondés sur d'autres dispositions demeurent applicables.")
repeal('L2243-2', proposed,
       "Fusion de fond coordonnée : abrogation de la seconde incrimination, dont le champ est réuni à L. 2243-1 avec maintien de l'amende existante et retrait de l'emprisonnement. Les obligations de négociation ne sont pas abrogées. Il ne s'agit ni d'une deuxième suppression de la même peine ni d'une abolition de toutes sanctions de négociation.",
       "L. 2243-1 proposé reprend exactement les deux fondements L. 2242-1 et L. 2242-20 déjà présents ici, sans étendre la sanction à d'autres obligations. Les deux articles doivent entrer en vigueur ensemble. La source ne comporte pas d'exonération fiscale ou d'aide supprimée. Les sanctions définitives et réparations antérieures ne sont pas effacées par une transition de convenance ; la loi pénale plus douce reste applicable dans son champ.",
       "Seconde incrimination de soustraction à la négociation collective, avec son emprisonnement et son amende propres, réunie dans L2243-1 sans double sanction.",
       "La disposition pénale distincte est supprimée, mais son champ utile et l'amende sont maintenus dans L2243-1 ; il s'agit de la coordination de la mesure unique de fusion sans emprisonnement.",
       "Aucune seconde baisse d'amende n'est comptée : la sanction pécuniaire subsiste dans l'article fusionné. Les infractions autonomes et les condamnations définitives restent distinctes.",
       "Aucune charge nouvelle n'est identifiée : aucune infraction, formalité ou peine de remplacement n'est créée ; la seule amende maintenue existait déjà dans les deux articles.",
       [effect('coordination', 'negociation-sanction-unique-sans-prison',
               "Abrogation de l'article pénal doublonné, avec transfert de son champ dans l'incrimination unique.",
               "Article distinct punissant la soustraction à L2242-1 et L2242-20 d'un an d'emprisonnement et de 3 750 euros d'amende.",
               "Article abrogé ; même champ poursuivi selon L2243-1 proposé, amende de 3 750 euros et aucun emprisonnement de ce fondement.",
               'regime', "Auteurs de manquements entrant dans l'ancien L2243-2.",
               "Entrée en vigueur simultanée à L2243-1 ; loi plus douce et droits à réparation réservés.",
               "Pas de nouvelle infraction ; mesure déjà portée par L2243-1, sans comptage d'une réduction supplémentaire.",
               "Le fait de se soustraire aux obligations prévues aux articles L. 2242-1 et L. 2242-20 est puni d'un emprisonnement d'un an et d'une amende de 3 750 euros.",
               "A compter de cette date, les faits de soustraction aux obligations des articles L. 2242-1 et L. 2242-20 relèvent de la seule incrimination de l'article L. 2243-1, dans son champ et selon les peines qu'il prévoit.")],
       classification='coordination_only')

retain('L2251-1',
       "Maintien intégral nécessaire du principe de faveur conventionnelle et de la limite d'ordre public. Il protège les avantages collectifs futurs et antérieurs tout en empêchant une convention d'écarter une protection impérative ; aucune formalité, autorisation ou prélèvement autonome n'est institué.",
       "Les deux phrases restent entières : faculté de stipulations plus favorables et interdiction de déroger à l'ordre public. Les lois spéciales peuvent déterminer les matières négociables ou les règles impératives. Ainsi, la substitution expressément prévue par L. 1234-1 proposé pour le préavis des nouveaux contrats n'est pas annulée par cette clause générale ; les indemnités plus favorables préservées par L. 1234-9 proposé restent à leur champ. Aucun renvoi supplémentaire n'est introduit dans le texte maintenu.",
       "Principe protecteur et autonomie conventionnelle conservés après examen, sans simple réécriture stylistique ni baisse de charge revendiquée.",
       "L'article ne tranche pas à lui seul toutes les règles spéciales de hiérarchie des normes ; les anciens contrats et garanties spéciales gardent leurs textes propres.",
       "Aucune charge nouvelle n'est identifiée : le texte intégral reste inchangé, sans dépôt, justificatif, délai ou condition de bénéfice ajouté.")
answers['L2251-1']['benefit_review'] = (
    "La faculté de négocier des stipulations plus favorables est un avantage collectif général : elle reste ouverte aux accords futurs et aux salariés futurs éligibles, sans être cantonnée aux droits acquis. La réserve d'ordre public protège les garanties impératives, tout en laissant les règles spéciales décider de leur articulation. Aucun avantage fiscal n'est institué ici et aucun avantage conventionnel n'est supprimé par cette conservation ; le barème ordinaire de rupture ne plafonne pas les réparations ou indemnités spéciales et les avantages plus favorables expressément préservés dans leur champ.")

retain('L2252-1',
       "Maintien intégral de la faculté d'adaptation entre niveaux de branche, professionnelle et interprofessionnelle, ainsi que de la clause expresse interdisant les dérogations et de l'adaptation aux accords supérieurs lorsque ceux-ci la prévoient expressément. La source n'exige ni agrément ni transmission administrative ; elle encadre une autonomie négociée, sans nouvelle réforme matérielle nécessaire dans ce lot.",
       "Conserver les deux alinéas et les conditions expresses : champ territorial ou professionnel plus large, interdiction possible en tout ou partie, puis adaptation uniquement si le nouvel accord supérieur l'exige expressément. L'article ne régit pas à lui seul la priorité des accords d'entreprise et ne permet pas de déroger à l'ordre public protégé par L. 2251-1. Il ne peut donc recréer un CDD, un terme d'emploi ou une procédure supprimée par une règle impérative. Aucune obligation d'adapter systématiquement tous les accords anciens n'est ajoutée.",
       "Souplesse conventionnelle et mécanismes de sauvegarde conservés à l'identique ; aucune réduction nette nouvelle n'est démontrée.",
       "L'avantage de souplesse pour les négociateurs peut permettre des clauses moins favorables aux salariés dans les limites légales ; il n'est pas présenté comme une hausse automatique de droits ou une économie chiffrée.",
       "Aucune charge nouvelle n'est identifiée : l'adaptation demeure subordonnée à une stipulation expresse du niveau supérieur, sans nouveau dépôt ou dossier de conformité.")
answers['L2252-1']['benefit_review'] = (
    "La faculté de déroger dans un champ plus étroit est une souplesse offerte aux négociateurs, non une exonération fiscale ni nécessairement un avantage pour chaque salarié. Elle reste ouverte aux accords futurs dans les limites d'ordre public. Pour les salariés, les avantages possibles sont la clause supérieure interdisant expressément la dérogation en tout ou partie et l'obligation d'adapter l'accord antérieur moins favorable lorsque le nouvel accord supérieur le prévoit expressément. Les deux sauvegardes demeurent intégrales pour les conventions en vigueur et à venir ; aucune fermeture aux futurs bénéficiaires ni adaptation générale non prévue n'est ajoutée.")


checks = {
    'L2242-7': {
        'L241-13': "Le renvoi source sert à calculer les plafonds punitifs de 10 %/100 % et l'affectation de la pénalité, non à définir une indemnité de rupture. La réduction L241-13 garde cotisations éligibles, calcul annuel, corrections, cumuls et adaptations de Mayotte. Sa proposition ajoute un calcul distinct plus favorable pour certaines affectations réelles dans le contrat unique, sans terme d'emploi ni double compte ; l'abrogation de la pénalité ne ferme pas ce bénéfice futur. Aucun seuil d'ancienneté ni notification de rupture ne conditionne ce renvoi social. Les éventuels anciens dossiers de sanction conservent leurs plafonds et garanties sous réserve de la loi plus douce, sans réécrire les erreurs de renvoi internes à L241-13.",
    },
    'L2242-8': {
        'L242-1': "Le troisième alinéa de L2242-8 vise le premier alinéa de L242-1, c'est-à-dire l'assiette des revenus d'activité et leur rattachement aux périodes, pour plafonner à 1 % la pénalité d'égalité. Il ne renvoie pas au II 7° relatif aux indemnités de rupture. La proposition cible supprime certains assujettissements intégraux au-delà de cinq/dix PASS sans modifier ce I : elle n'appelle donc aucune application artificielle du préavis, du seuil d'un an ou du barème 0,20 mois à la pénalité. Les exclusions sociales et les anciens droits de rupture de la cible ne sont pas supprimés par le renvoi ; le régime agricole L741-10 demeure distinct.",
    },
    'L2242-17': {
        'L911-2': "Le renvoi du second alinéa du 5° concerne les entreprises de travaux forestiers et l'accès aux garanties collectives : décès, intégrité physique, maternité, incapacité/invalidité, inaptitude, chômage et retraite/fin de carrière. La cible n'a ici qu'une source officielle, sans proposition ; aucun contenu de réforme n'est inventé. Ces couvertures profitent aussi aux anciens salariés et ayants droit et ne sont pas l'indemnité ordinaire de licenciement : ni seuil d'un an ni préavis individuel de quinze jours ne les effacent. Le terme d'une mission ne ferme pas ces garanties pour les emplois nouveaux éligibles.",
        'L911-7': "Le premier alinéa du 5° impose une négociation au moins aussi favorable que L911-7, qui prévoit couverture santé minimale, garanties du II, financement patronal d'au moins moitié, dispenses à l'initiative du salarié et adaptations du régime local Alsace-Moselle. La proposition cible conserve les dispenses des anciens CDD et les ouvre à des affectations temporaires réelles du contrat unique selon leur période, sans terme d'emploi et avec couverture ordinaire à sa fin sauf autre dispense. La suppression de charte au 7° ne modifie aucun de ces bénéfices, pour les salariés futurs aussi ; ancienneté de rupture et préavis sont étrangers au panier de soins.",
        'L241-3-1': "Le renvoi rattaché au 2° vise la faculté de maintenir l'assiette vieillesse au salaire à temps plein pour un temps partiel ou certaines rémunérations sans heures, et la prise en charge patronale du supplément avec exclusion de CSG de la part salariale ainsi prise en charge. Source et proposition cible conservent cette faculté et les habilitations réglementaires. Elle reste négociable pour les futurs salariés du contrat unique ; la suppression du minimum général de temps partiel ne la ferme pas. Aucun seuil d'un an, plafond d'indemnité ou notification de rupture ne régit ce supplément volontaire de cotisation.",
    },
    'L2242-20': {
        'L1234-1': "Il s'agit d'une cible indirecte par L2254-2 V, non d'une règle de durée de GEPP. La source distingue moins de six mois, six mois à moins de deux ans et au moins deux ans ; la proposition fixe quinze jours calendaires pour les nouveaux contrats, même en cas de faute grave payée, et garde les préavis anciens. Ce délai individuel n'abolit pas les consultations collectives ou autorisations. Son départ relève de la notification écrite dans L1234-3 proposé, non fourni comme cible autonome ici ; la durée de mobilité ou de formation ne vaut jamais notification ni terme d'emploi.",
        'L1221-2': "Le 4° de L2242-20 doit être coordonné : la source L1221-2 admet le terme de CDD tandis que la proposition interdit, pour les nouvelles embauches, tout terme lié à une date, tâche, chantier, formation ou mission. Le 4° proposé vise donc le contrat unique et prend séparément en compte les contrats anciens, sans autoriser un renouvellement de CDD nouveau. Une aide ou un parcours temporaire ne termine pas l'emploi et ne remplace pas une notification de rupture. Leurs droits acquis et les futurs avantages éligibles ne sont pas fermés par le thème de négociation ; aucun seuil indemnitaire n'est fixé ici.",
        'L1234-9': "Cible indirecte de L2254-2 V : le régime officiel ouvre l'indemnité à huit mois sauf faute grave ; le projet nouveau mesure un an à la fin effective, préavis inclus, puis calcule 0,20 mois sur toute l'ancienneté, fractions en mois complets, plafond légal six mois, à l'initiative patronale seulement. Le projet conserve la faute grave et les avantages plus favorables, salaires, congés, dommages et indemnités spéciales. Les anciens contrats gardent seuil de huit mois, composante ancienne et composante nouvelle sans double compte. Le retrait du chapitre séparé et du bilan GEPP ne modifie aucun de ces calculs ni la notification exigée pour la rupture.",
        'L2254-2': "Les 1° et 2° de L2242-20 distinguent mobilité ordinaire et accord de performance collective. La suppression du chapitre spécifique ne supprime ni l'accord, ni le droit au refus écrit pendant un mois après information à date certaine, ni les deux mois pour engager le licenciement après notification du refus, ni l'abondement CPF et l'accompagnement du VI. La proposition cible conserve ces délais et ajoute les coordinations privées : préavis de quinze jours dès le lendemain de la notification selon L1234-3 proposé, seuil indemnitaire d'un an au terme avec préavis, toute ancienneté à 0,20 mois et plafond six mois. Les procédures et autorisations distinctes, les anciens droits et les avantages futurs éligibles subsistent ; le bilan GEPP supprimé ne les remplace pas.",
    },
    'L2242-21': {
        'L1234-1': "Cible de contexte des modes de rupture, sans renvoi direct de L2242-21 au préavis. Les congés de mobilité, procédures économiques et reconversions ne sont pas tous des licenciements individuels ordinaires. La proposition cible de quinze jours pour les nouveaux contrats ne remplace ni les consultations, consentements, délais de dispositifs ni les autorisations de salariés protégés ; les préavis des anciens contrats gardent leur régime. Le départ par notification écrite relève de L1234-3 proposé dans son champ, non du seul achèvement d'une mission ou d'une formation. L'absence de seuil d'ancienneté de ce préavis ne supprime pas les seuils propres des aides.",
        'L1221-2': "La source cible autorise CDI et cas de CDD ; la proposition impose l'emploi nouveau à durée indéterminée avec maintien des contrats anciens et interdiction de nouveaux renouvellements de CDD. Les 6° et 7° de L2242-21 ne font que permettre la négociation d'alternance et de reconversion : ni la période pédagogique ni le stage, qui n'est pas un contrat de travail, ne permettent de rétablir un CDD de salarié. Les droits et aides des futurs apprentis, alternants ou salariés en reconversion restent dans leur champ coordonné. Une durée de parcours n'est ni terme d'emploi ni notification de rupture, et cet article ne fixe aucune indemnité ordinaire.",
        'L1234-9': "Cible de contexte pour les minima légaux renvoyés par L6324-9 II 3°, sans assimilation de toutes ruptures de mobilité à un licenciement ordinaire. La proposition nouvelle prévoit zéro avant un an mesuré au terme effectif avec préavis, puis 0,20 mois par année totale, première année incluse, prorata des mois complets et plafond légal six mois, employeur seul et sous ses autres conditions. Les indemnités spéciales, dommages, congés et garanties plus favorables ne sont pas écrasés. Pour les contrats anciens, le seuil antérieur et les deux composantes d'ancienneté sans double compte sont conservés. L2242-21 ne transforme pas ce seuil en condition de formation ou d'accès au congé.",
        'L6324-9': "Le 7° et l'alinéa final font valoir l'accord GEPP comme accord d'organisation de la reconversion externe. La source distingue A : 50 à moins de 300 salariés avec délégué et seuil 10 % sur douze mois, B : grands groupes/entreprises, C : petites entreprises ou absence de délégué ; les indemnités et l'accord du salarié pour le CPF demeurent. La proposition cible retire au A l'attente minimale de trois mois et le PV distinct, sans permettre d'imputer un échec au seul silence. Le renvoi conservé n'en rétablit aucun. Les durées de formation ne terminent pas le contrat ; procédures de rupture et indemnités spéciales restent propres. Les anciens avenants conclus avant le 1er janvier 2026 ont la transition expresse fournie dans les notes.",
    },
    'L2242-22': {
        'L221-1-5': "Le troisième alinéa vise seulement l'examen des possibilités de mobiliser le fonds de prévention de l'usure professionnelle. La source cible conserve ses missions, dotation annuelle, critères d'exposition, cartographie et trois catégories de financement, dont entreprises et transitions professionnelles. Sa proposition retire un avis préalable et une convention supplémentaire, sans supprimer aides ou conditions de fond, pour les demandes et bénéficiaires futurs aussi. La dispense de diagnostic préalable de L2242-22 ne crée ni attribution automatique ni nouvelle attestation d'éligibilité. La prévention du régime général et ses financements ne sont pas le barème privé de rupture ; ancienneté d'un an et préavis n'y sont pas importés.",
    },
}

for s in sources:
    number = s['number']
    a = answers[number]
    key = s['code_id'] + '|' + s['source_id']
    a['reference_checks'] = []
    for target_key in refs['requirements'][key]:
        t = refs['targets'][target_key]
        assessment = checks[number][t['number']]
        assert len(assessment) >= 80
        a['reference_checks'].append(dict(target_key=target_key, view_sha256=t['view_sha256'], assessment=assessment))

output = [answers[s['number']] for s in sources]
assert len(output) == 24
for s, a in zip(sources, output):
    assert all(a[k] == s[k] for k in ('code_id', 'source_id', 'source_sha256', 'number'))
    impact = a['substantive_impact']
    for k in ('assessment', 'scope_limitations', 'new_burdens_review'):
        assert len(impact[k]) >= 40, (a['number'], k)
    if s['benefit_check_required']:
        assert len(a['benefit_review']) >= 100
    for e in impact['effects']:
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)+', e['measure_id'])
        assert 6 <= len(e['measure_id']) <= 96
        assert len(e['source_quote']) >= 12 and e['source_quote'] in plain(s['source_xml']), (a['number'], 'source quote', e['source_quote'])
        assert len(e['proposed_quote']) >= 12 and e['proposed_quote'] in plain(a['proposed_xml']), (a['number'], 'proposed quote')
    if a.get('change_type') == 'full_repeal':
        assert plain(a['proposed_xml']).startswith(('Le présent article est abrogé', 'Abrogé'))
        assert len(a['repeal_scope']) >= 30
    if a.get('change_type') == 'normative_reduction':
        assert all(len(x) >= 30 for x in a['removed_provisions'])

Path('answer.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'article_count': len(output), 'drafts': sum(a['status'] == 'rewrite_draft' for a in output),
                  'retained_necessary': sum(a['status'] == 'retained_unchanged' for a in output),
                  'reference_checks': sum(len(a['reference_checks']) for a in output)}, ensure_ascii=False))
