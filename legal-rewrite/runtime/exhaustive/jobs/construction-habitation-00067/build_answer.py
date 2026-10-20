import json
import re
from html import unescape
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
by_number = {a['number']: a for a in sources}
answers = {}


def plain(xml):
    return re.sub(r'\s+', ' ', unescape(re.sub(r'<[^>]+>', ' ', xml))).strip()


def substitute(number, old, new, xml=None):
    xml = by_number[number]['source_xml'] if xml is None else xml
    assert xml.count(old) == 1, (number, old)
    return xml.replace(old, new)


def append(xml, text):
    return xml.rstrip() + '\n<p>' + text + '</p>'


def effect(kind, measure_id, description, before, after, unit, population,
           transition, replacement, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit,
                affected_population=population, conditions_and_transition=transition,
                replacement_or_new_burdens=replacement,
                source_quote=source_quote, proposed_quote=proposed_quote)


def record(number, reason, notes, assessment, limitations, burdens,
           xml=None, classification='retained_necessary', effects=None,
           removed=None, benefit=None):
    a = by_number[number]
    result = {k: a[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}
    result.update(proposed_xml=xml, reason=reason, review_notes=notes,
                  status='retained_unchanged' if xml is None else 'rewrite_draft',
                  substantive_impact=dict(version=1, classification=classification,
                      assessment=assessment, scope_limitations=limitations,
                      new_burdens_review=burdens, effects=effects or []))
    if xml is None:
        result['classification'] = 'retained_necessary'
    if removed:
        result.update(change_type='normative_reduction',
                      reform_policy_id='editorial_direction_2026_10_19',
                      removed_provisions=removed)
    if benefit:
        result['benefit_review'] = benefit
    key = a['code_id'] + '|' + a['source_id']
    result['reference_checks'] = []
    # Les deux listes requises non vides sont renseignées et contrôlées à la fin.
    answers[number] = result
    return result


# Les paragraphes maintenus sont repris de la source, sans réécriture de style.
n = 'R112-7'
old = ", ainsi que par l'établissement, par l'organisme désigné pour le traitement de ces données, d'un rapport annuel sur les solutions d'effet équivalent"
xml = substitute(n, old, '')
xml = append(xml, "À compter de l'entrée en vigueur de la loi de simplification, aucun rapport annuel n'est exigé sur le fondement du présent article, y compris au titre d'une période antérieure. Les rapports déjà établis ne sont pas à refaire ; les règles de protection des données qu'ils contiennent demeurent applicables.")
record(n,
    "Réduction de fond : suppression du rapport annuel obligatoire sur les solutions d'effet équivalent. Le traitement des données déjà collectées, le suivi, les statistiques et la diffusion des expériences sont conservés ; aucune nouvelle collecte ni déclaration ne remplace le rapport.",
    "Coordonner R112-8 dans le présent lot pour conserver les secrets et l'anonymisation des rapports anciens sans renvoi à un rapport futur. Les procédures des sections 1 à 3 ne sont pas abolies par cette suppression. Le coût du traitement existant et l'économie de rédaction ne sont pas chiffrés.",
    "L'organisme désigné n'a plus à produire un document annuel obligatoire, alors que la source entière le lui impose en plus des usages statistiques et de diffusion. Ce retrait est distinct de la conservation du traitement existant.",
    "La collecte prévue dans les sections 1 à 3 et les contrôles techniques restent à leur champ propre ; aucune baisse de prélèvement ni économie nationale n'est établie.",
    "Aucune charge nouvelle identifiée : les mêmes données et usages demeurent, sans rapport, dépôt, confirmation négative ou calendrier de remplacement.",
    xml, 'material_reduction', [effect('obligation_removed', 'solutions-equivalentes-fin-rapport-annuel',
        "Suppression de la production annuelle d'un rapport administratif distinct.",
        "Un rapport annuel obligatoire établi par l'organisme chargé du traitement, en plus du suivi et de la diffusion des données.",
        "Aucun rapport annuel obligatoire ; statistiques, suivi et diffusion demeurent possibles.", 'legal_duty',
        "Organisme désigné pour traiter les données des solutions d'effet équivalent.",
        "À l'entrée en vigueur ; les rapports encore non établis pour une période ancienne ne sont plus exigés, les rapports établis demeurent protégés.",
        "Aucun document ni collecte de remplacement.",
        "par l'établissement, par l'organisme désigné pour le traitement de ces données, d'un rapport annuel sur les solutions d'effet équivalent",
        "aucun rapport annuel n'est exigé sur le fondement du présent article, y compris au titre d'une période antérieure.")],
    ["Obligation faite à l'organisme désigné d'établir un rapport annuel spécifique sur les solutions d'effet équivalent, sans rapport périodique de remplacement."])

n = 'R112-8'
xml = substitute(n,
    "Les données utilisées pour l'établissement du rapport annuel prévu par l'article R.112-7 sont anonymisées.",
    "Les données utilisées pour les rapports annuels établis avant l'entrée en vigueur de la loi de simplification demeurent anonymisées.")
record(n,
    "Coordination nécessaire de la suppression du rapport annuel de R112-7 : le renvoi prospectif est retiré, l'anonymisation des rapports établis et l'interdiction absolue de transmettre les données personnelles à un tiers sont maintenues. Les secrets d'affaires, de propriété intellectuelle et de défense restent intégralement protégés.",
    "Aucune seconde obligation de rapport n'est supprimée ici. Les utilisations statistiques et la diffusion conservées à R112-7 restent soumises à la première phrase et à l'interdiction de transmission de données personnelles. La suppression du rapport ne rend pas publiques les données individuelles.",
    "La référence au rapport obligatoire est mise en cohérence avec R112-7 ; les protections de fond ne sont pas diminuées et aucune réduction autonome n'est comptée.",
    "Le régime général des données personnelles et les secrets légalement protégés ne sont pas réécrits ; aucune économie propre à cet article n'est quantifiée.",
    "Aucune charge nouvelle identifiée : l'anonymisation déjà prescrite demeure pour les rapports anciens et aucune nouvelle donnée ou vérification périodique n'est demandée.",
    xml, 'coordination_only', [effect('coordination', 'solutions-equivalentes-fin-rapport-annuel',
        "Retrait du renvoi à un rapport annuel futur tout en protégeant les documents déjà établis.",
        "Anonymisation des données utilisées pour le rapport annuel obligatoire de R112-7.",
        "Anonymisation conservée pour les rapports antérieurement établis ; aucune obligation de produire un nouveau rapport.", 'legal_duty',
        "Organisme de traitement, personnes concernées et détenteurs des secrets protégés.",
        "Coordination à la même entrée en vigueur que R112-7 ; données anciennes toujours protégées.",
        "Aucun rapport de remplacement ni nouvelle transmission.",
        "Les données utilisées pour l'établissement du rapport annuel prévu par l'article R.112-7 sont anonymisées.",
        "Les données utilisées pour les rapports annuels établis avant l'entrée en vigueur de la loi de simplification demeurent anonymisées.")])

n = 'R112-9'
old = " En outre, le pétitionnaire justifie dans quelle mesure le projet sera de nature, au regard des objectifs poursuivis par la réglementation en cause, à atteindre le meilleur niveau de performance possible, que ce soit par sa conception ou par la mise en œuvre de matériaux et équipements performants."
xml = substitute(n, old, '')
xml = append(xml, "La suppression de la justification du meilleur niveau de performance possible s'applique aux demandes déposées ou en cours d'instruction à compter de l'entrée en vigueur de la loi de simplification, sans nouveau dépôt ni reprise des délais. Elle ne dispense pas du respect des conditions de l'article L. 112-13, notamment de l'absence de dégradation de la partie existante, ni des prescriptions et mesures compensatoires légalement imposées.")
record(n,
    "Réduction de fond : retrait de la justification supplémentaire d'une optimisation au meilleur niveau de performance possible. La demande doit toujours identifier les règles, ses raisons et, s'il y a lieu, les compensations. Les avis de sécurité incendie et d'accessibilité, la consultation éventuelle du CEREMA, les délais de deux et trois mois et la décision préfectorale sont intégralement conservés.",
    "L112-13 a été lu dans le corpus : surélévation d'un bâtiment achevé depuis plus de deux ans, impossibilité liée aux caractéristiques du bâtiment, non-dégradation de l'existant et acceptation tacite après trois mois demeurent. La suppression ne crée pas une dérogation générale à la sécurité. Le R*423-13-1 du code de l'urbanisme, lu intégralement, vise encore L111-4-1 au lieu de L112-13 : coordination de recodification nécessaire dans cet article hors lot, sans modifier sa transmission sous une semaine ni rétablir des exemplaires supprimés par les autres coordinations. Le renvoi source à L161-1 dans le b reste celui de l'objectif d'accessibilité ; il n'est pas remplacé par une règle du contrat de travail.",
    "La source impose une démonstration distincte du meilleur niveau techniquement possible ; elle disparaît effectivement. Les conditions légales de la dérogation, les compensations éventuelles et l'expertise de sécurité ne sont pas retirées.",
    "Le gain concerne la justification d'optimisation, pas la totalité du dossier ni les performances obligatoires. Le compagnon urbanisme R*423-13-1 est identifié mais non modifié dans ce lot.",
    "Aucune charge nouvelle identifiée : aucune attestation, déclaration ou expertise ne remplace la justification supprimée ; les pièces nécessaires aux motifs et compensations restent celles de la source.",
    xml, 'material_reduction', [effect('obligation_removed', 'derogation-surelevation-fin-preuve-optimum',
        "Suppression de la démonstration supplémentaire du meilleur niveau de performance possible.",
        "Le pétitionnaire doit justifier une optimisation maximale, en plus des motifs et compensations de la dérogation.",
        "Seuls les motifs, règles concernées et compensations éventuelles sont décrits selon les conditions légales conservées.", 'legal_duty',
        "Pétitionnaires de dérogations pour surélévation relevant de L112-13.",
        "Demandes nouvelles et en cours à l'entrée en vigueur ; ni redépôt ni remise à zéro des délais ; décisions déjà prises non annulées.",
        "Aucune pièce ou contrôle d'optimisation de remplacement ; contrôles incendie et accessibilité maintenus.",
        old.strip(),
        "La suppression de la justification du meilleur niveau de performance possible s'applique aux demandes déposées ou en cours d'instruction")],
    ["Justification supplémentaire imposant au pétitionnaire de démontrer l'atteinte du meilleur niveau de performance possible par la conception, les matériaux ou les équipements."],
    "La faculté de déroger pour les surélévations futures reste ouverte, avec les avis tacitement rendus au bout de deux mois et le délai de trois mois. Les compensations demeurent éventuelles. La coupe supprime une justification supplémentaire ; elle ne réduit ni le champ de la dérogation légale ni l'acceptation tacite prévue par L112-13.")

record('R112-10',
    "Maintien intégral utile : l'article habilite des règles spéciales plus adaptées aux logements temporaires ou saisonniers. Il ne crée ni taxe, ni dossier individuel, ni agrément supplémentaire ; supprimer l'habilitation fermerait une dérogation favorable pour les opérations futures.",
    "Le caractère temporaire ou saisonnier qualifie l'occupation du logement, non un contrat de travail à durée déterminée. L'arrêté conjoint et ses exigences sanitaires demeurent à leur champ ; aucun quota SRU n'est réintroduit.",
    "Aucun changement normatif : la possibilité réglementaire de déroger au livre est conservée pour éviter une rigidification des règles de construction.",
    "Les arrêtés particuliers ne sont pas intégralement fournis dans ce lot ; leur contenu n'est ni déclaré supprimé ni audité. Aucun allègement nouveau n'est compté.",
    "Aucune charge nouvelle identifiée : aucun nouveau corps n'est proposé et l'habilitation existante n'est assortie d'aucune condition supplémentaire.",
    benefit="La dérogation pour certaines catégories de logements à occupation temporaire ou saisonnière est un avantage de souplesse conservé intégralement. Elle reste utilisable par de futures opérations éligibles, sans condition d'antériorité ajoutée ni extinction de l'habilitation ministérielle.")

record('R112-11',
    "Maintien intégral : la décision conjointe construction-santé ouvre des dérogations pour des habitations expérimentales. Cette autorisation porte sur un écart aux règles du livre, qui peut concerner la salubrité ou la sécurité ; son retrait sans critères matériels de substitution ne garantirait pas ces fonctions essentielles.",
    "Articuler avec R*112-17, maintenu : le silence ne suffit pas à autoriser une expérimentation dérogatoire. Le dispositif des solutions d'effet équivalent reste distinct. Aucune déclaration équivalente à l'autorisation n'est créée.",
    "La faculté de dérogation expérimentale et son examen conjoint sont conservés, sans réécriture stylistique ni réduction déclarée.",
    "L'évaluation des catégories précises d'expérimentation et des dérogations déjà accordées n'est pas fournie ; aucune généralisation automatique de l'expérimentation n'est établie.",
    "Aucune charge nouvelle identifiée : conditions, autorités et procédure de la source sont conservées sans dossier, registre ou délai supplémentaire.",
    benefit="Le pouvoir d'accorder des dérogations aux habitations expérimentales demeure entier pour les projets futurs comme pour les décisions acquises. Le contrôle conjoint de santé et de construction ne constitue pas un prélèvement ; il n'est pas supprimé au prix d'une fermeture de cette possibilité favorable.")

record('R112-12',
    "Maintien intégral de la dérogation ministérielle pour les bâtiments collectifs expérimentaux lorsque R162-3 est momentanément inapplicable. R162-3, lu intégralement, protège le transport sur brancard et la desserte par ascenseur : un examen de la dérogation garde une fonction d'accessibilité et de secours essentielle.",
    "Le renvoi vise les exigences matérielles de R162-3, pas une durée d'emploi. R*112-17 conserve le rejet implicite. Ni la compétence ministérielle ni le caractère momentanément impossible ne sont remplacés par une attestation privée.",
    "Aucune suppression : la dérogation expérimentale utile et le contrôle d'un écart aux règles de secours et d'accès sont maintenus ensemble.",
    "Aucune démonstration disponible ne permet d'ouvrir une dispense générale de brancard ou d'ascenseur sans critères équivalents. Aucun gain de conformité n'est attribué à ce maintien.",
    "Aucune charge nouvelle identifiée : le texte source reste entier, avec la même dérogation et sans condition ou formalité supplémentaire.",
    benefit="La faculté de déroger à R162-3 pour un collectif nouveau expérimental est intégralement préservée, y compris pour de futurs projets remplissant le critère d'impossibilité momentanée. Elle n'est ni réservée aux permis anciens ni abrogée par coordination avec les obligations ordinaires d'accessibilité.")

n = 'R112-13'
old = "la commission consultative départementale de la protection civile, de la sécurité et de l'accessibilité prévue par le décret n° 85-988 du 16 septembre 1985"
new = "la commission consultative départementale de sécurité et d'accessibilité ou, à Paris, dans les Hauts-de-Seine, la Seine-Saint-Denis et le Val-de-Marne, de la commission départementale de sécurité"
xml = substitute(n, old, new)
record(n,
    "Coordination de l'organe consulté : remplacement de la référence ancienne à la commission de 1985 par les commissions actuelles identifiées dans R122-6 du corpus. Le préfet, son arrêté et la dérogation liée au terrain ou aux constructions existantes restent inchangés ; aucune autorisation supprimée n'est revendiquée.",
    "R162-3 et R122-6 ont été lus intégralement dans le corpus en lecture seule. R122-6 nomme expressément la commission de sécurité et d'accessibilité et les quatre territoires à commission départementale de sécurité. Ce texte vérifié n'est pas ajouté comme cible dans reference_checks, dont la liste requise est vide. Le décret de 1985 n'est pas présenté comme vérifié intégralement ni son abrogation datée par inférence. Les consultations antérieures régulièrement accomplies ne sont pas à recommencer du seul fait de cette mise à jour de dénomination.",
    "Seule la désignation de l'organe est coordonnée ; la possibilité favorable de déroger aux règles de brancard et d'ascenseur ainsi que son examen essentiel demeurent.",
    "Aucune autorisation ou consultation distincte n'est abolie. Les textes organiques extérieurs des commissions ne sont pas réécrits ; aucun gain matériel n'est compté.",
    "Aucune charge nouvelle identifiée : la consultation déjà exigée reste unique, avec le même objet et sans nouvelle pièce ni délai légal ajouté.",
    xml, 'coordination_only', [effect('coordination', 'construction-commission-accessibilite-coordination',
        "Mise à jour de l'identification de la commission consultée, sans modifier l'accès à la dérogation.",
        "Consultation d'une commission désignée par une référence réglementaire de 1985.",
        "Consultation de la commission actuelle de sécurité et d'accessibilité ou de sécurité dans les quatre territoires particuliers.", 'legal_duty',
        "Préfets et pétitionnaires dont le terrain ou les constructions existantes font obstacle à R162-3.",
        "Application organique de droit commun ; les actes de consultation déjà régulièrement accomplis restent utilisables.",
        "Aucune seconde consultation ni nouvelle formalité.", old, new)],
    benefit="La dérogation préfectorale lorsque le terrain ou les constructions existantes empêchent d'appliquer R162-3 est conservée pour toutes les demandes futures éligibles. Seule l'identification de la commission est actualisée ; le champ de la dispense, ses deux causes et la compétence du préfet ne sont pas resserrés.")

record('R112-14',
    "Maintien intégral de la faculté de dérogation sur aménagements assurant les mêmes garanties de confort, d'hygiène ou de sécurité. Les cibles R151-1 c, R155-1, R134-61 premier alinéa et R142-1 ont été lues : cuisine, ouvertures, installations à risque et incendie justifient le contrôle de l'équivalence.",
    "La référence au premier alinéa de R134-61 ne vise pas les alinéas autonomes sur conduits de fumée et vide-ordures. La source de R142-1 contient aussi entretien, vérification et registre : l'article ne les abroge pas implicitement. R112-16 conserve publicité et accès aux décisions. Aucun avis additionnel n'est introduit.",
    "Aucune réforme matérielle : conserver cette voie alternative évite d'imposer exclusivement les moyens techniques ordinaires, tout en maintenant l'équivalence de sécurité.",
    "L'article ne permet pas de supprimer tous les contrôles d'incendie ni de conclure que les prescriptions des arrêtés seraient toutes redondantes ; aucun gain nouveau n'est compté.",
    "Aucune charge nouvelle identifiée : les mêmes critères d'équivalence et la décision préfectorale subsistent sans dossier ou justification supplémentaire.",
    benefit="L'avantage consiste dans la faculté de déroger aux quatre groupes de prescriptions grâce à des aménagements équivalents. Il reste ouvert aux futures constructions avec les mêmes garanties alternatives de confort, d'hygiène ou de sécurité, sans limitation aux décisions déjà accordées et sans ajout d'autorisation.")

record('R112-15',
    "Maintien intégral de la dérogation pour caractéristiques techniques et économiques concernant la seule première phrase du premier alinéa de R113-4. La proposition de R113-4 conserve cette phrase sur les lignes téléphoniques en élargissant sa dispense aux logements fibrés ; le renvoi reste donc matériellement cohérent.",
    "Le préfet peut toujours dispenser les opérations non déjà dispensées par R113-4. Le renvoi n'englobe ni l'alinéa sur la radiodiffusion ni les prescriptions de fibre et d'installation intérieure. La dérogation ne devient pas un ancien droit fermé aux opérations futures.",
    "La faculté existante est maintenue ; l'élargissement de la dispense générale est porté et évalué dans R113-4, sans second gain attribué au présent article.",
    "Les dérogations individuelles restent nécessaires seulement dans leur champ résiduel. Aucun constat de baisse chiffrée des coûts de raccordement n'est fourni.",
    "Aucune charge nouvelle identifiée : aucun nouveau corps, aucune nouvelle demande et aucune nouvelle condition technique ou économique ne sont ajoutés.",
    benefit="La faculté préfectorale favorable fondée sur les caractéristiques techniques et économiques des opérations est intégralement maintenue pour les demandes futures. La dispense générale élargie de R113-4 ne la remplace pas : les opérations qui ne sont pas déjà dispensées conservent cette voie individuelle.")

record('R112-16',
    "Maintien intégral : la publication des dérogations R112-14 et R112-15 et l'accès au dossier assurent la connaissance de décisions qui peuvent écarter des règles de sécurité ou affecter les tiers. Ce n'est ni une seconde demande du constructeur ni une autorisation additionnelle à supprimer.",
    "R112-14 et R112-15 demeurent en vigueur dans la proposition : aucun renvoi orphelin. Le livre III du CRPA encadre la communication, y compris les secrets et restrictions applicables ; aucun accès illimité ou registre supplémentaire n'est créé.",
    "Aucune réduction revendiquée : publicité et accès constituent les garanties procédurales des dérogations favorables maintenues.",
    "Les modalités générales de publicité et le CRPA restent hors réécriture du présent lot. Aucun coût public ni économie privée n'est chiffré.",
    "Aucune charge nouvelle identifiée : le régime de publication existant et la communication sur demande sont conservés à l'identique, sans dépôt supplémentaire.",
    benefit="L'article ne crée pas d'exonération fiscale. Il rend opposables et contrôlables les dérogations favorables de R112-14 et R112-15, qui restent ouvertes à l'avenir ; conserver cette garantie ne ferme aucun bénéficiaire futur ni n'ajoute de préalable à l'octroi de ces dérogations.")

record('R*112-17',
    "Maintien intégral du rejet implicite des seules dérogations expérimentales R112-11 et R112-12. L'expérimentation peut écarter la salubrité, la sécurité ou les règles de secours et d'ascenseur : une autorisation tacite générale sans critères de substitution démontrés ne préserverait pas ces fonctions essentielles.",
    "Le rejet implicite n'abroge pas le pouvoir de décision expresse favorable. Il ne s'étend pas à la surélévation L112-13, dont le silence de trois mois vaut acceptation. Aucun délai d'attente nouveau n'est fixé et aucune décision expresse ancienne n'est retirée.",
    "Aucun changement normatif ; le texte empêche qu'une absence d'examen suffise à autoriser une expérimentation touchant potentiellement des règles de sécurité.",
    "Les régimes généraux de décision implicite et leurs délais ne sont pas reconstitués à partir de cet article. Aucun rejet devenu favorable ou raccourcissement de délai n'est revendiqué.",
    "Aucune charge nouvelle identifiée : le même champ limité du rejet implicite subsiste sans nouvelle justification, notification ou durée minimale.",
    benefit="Le rejet implicite n'est pas une exonération ni une dérogation favorable autonome. Les avantages sont les décisions expresses de R112-11 et R112-12, toutes deux conservées pour les opérations futures. La présente règle ne transforme pas leur silence en refus définitif d'examiner un projet ni ne supprime une dérogation acquise.")

n = 'R112-18'
xml = substitute(n, ", évaluée par un professionnel dans le domaine de l'immobilier", '')
xml = substitute(n,
    "du règlement du plan d'occupation des sols applicable prises sur le fondement des articles L. 151-18 et L. 151-19 du code de l'urbanisme",
    "du règlement du plan local d'urbanisme applicable prises sur le fondement des articles L. 151-18 et L. 151-19 du code de l'urbanisme",
    xml)
xml = substitute(n,
    "sous réserve du droit de surplomb pour une isolation thermique par l'extérieur prévu à l'article L. 113-5-1 du code de la construction et de l'habitation ;",
    "sous réserve du droit de surplomb pour une isolation thermique par l'extérieur prévu à l'article L. 113-5-1 du code de la construction et de l'habitation. La même exception demeure applicable aux prescriptions correspondantes d'un plan d'occupation des sols légalement applicable ;",
    xml)
xml = append(xml, "La suppression de l'évaluation obligatoire par un professionnel s'applique à l'appréciation de l'exception à compter de l'entrée en vigueur de la loi de simplification, y compris aux demandes en cours, sans renouvellement des évaluations déjà produites. La valeur vénale et le coût des travaux peuvent être établis par tout moyen ; aucune expertise nouvelle n'est exigée sur le seul fondement du 2°. Les droits et avantages valablement acquis avant cette entrée en vigueur sont préservés, sous les conditions qui leur sont propres.")
record(n,
    "Réduction de fond : suppression de l'évaluation immobilière professionnelle obligatoire au 2°, sans modifier le seuil strict de 50 % ni l'exception pour coûts disproportionnés. Coordination expresse au d du 1° : L151-18 et L151-19 régissent le règlement du PLU, alors que la source nomme le POS ; les prescriptions correspondantes des POS légalement applicables restent couvertes. Les quatre catégories d'exception, les protections patrimoniales, le risque pathologique et sa note d'homme de l'art demeurent.",
    "Sources de renvoi lues intégralement : L111-1, L151-18 et L151-19 urbanisme ; aucune modification de ces cibles hors lot. Les six postes, le gain de deux classes et les autres conditions légales de L111-1 restent requis dans leur champ. Le d conserve expressément L113-5-1 : droit de surplomb de 35 cm, hauteur de deux mètres sauf accord, indemnités, publicité, accès temporaire et délai d'opposition de six mois ne sont pas supprimés. Le titre de rénovation globale et ses durées relèvent de R112-19. Les trois cibles du travail imposées par reference-targets n'ont aucun lien matériel avec cette exception de construction : analyses individuelles jointes, sans nouveau renvoi au contrat unique.",
    "La source entière exige un professionnel pour valoriser le bien ; cette dépense imposée disparaît et la preuve devient libre. Le seuil de coût, la protection du bâti, les quatre exceptions et la note technique de sécurité du 3° restent applicables. La correction POS/PLU ne compte pas comme une seconde suppression.",
    "L'économie d'honoraires dépend des évaluations déjà disponibles et n'est pas chiffrée. Les aides ont leurs autres conditions propres ; aucun droit à une aide ni dispense de sécurité n'est créé automatiquement.",
    "Aucune charge nouvelle identifiée : la valeur et le coût étaient déjà nécessaires au seuil de 50 %, aucune expertise ou attestation de remplacement n'est créée ; les moyens de preuve deviennent libres.",
    xml, 'material_reduction', [
        effect('compliance_cost_reduced', 'renovation-exception-fin-expertise-venale',
            "Suppression du recours obligatoire à un professionnel pour apprécier la valeur vénale au 2°.",
            "Coût des travaux supérieur à 50 % de la valeur vénale du bien obligatoirement évaluée par un professionnel de l'immobilier.",
            "Même seuil strict de 50 %, coût et valeur établis par tout moyen, sans expertise professionnelle obligatoire.", 'legal_duty',
            "Propriétaires et demandeurs se prévalant de l'exception de coût de la rénovation performante.",
            "Appréciations nouvelles et dossiers en cours à l'entrée en vigueur ; évaluations déjà établies utilisables, avantages acquis préservés.",
            "Aucune expertise ni déclaration de remplacement ; la note technique du 3° reste nécessaire pour le risque pathologique distinct.",
            "2° Excéderaient 50 % de la valeur vénale du bien, évaluée par un professionnel dans le domaine de l'immobilier ;",
            "La valeur vénale et le coût des travaux peuvent être établis par tout moyen ; aucune expertise nouvelle n'est exigée sur le seul fondement du 2°."),
        effect('coordination', 'renovation-exception-documents-urbanisme',
            "Correction explicite du document auquel se rattachent L151-18 et L151-19, avec conservation de l'exception des POS encore applicables.",
            "La source désigne le règlement du POS en le rattachant aux dispositions actuelles de PLU.",
            "Référence au PLU sous L151-18 et L151-19, avec maintien des prescriptions correspondantes d'un POS légalement applicable.", 'other',
            "Constructions bénéficiant de l'exception pour prescriptions architecturales ou d'urbanisme.",
            "Dossiers futurs et en cours, sans retrait des droits antérieurement accordés ni du droit de surplomb.",
            "Aucun nouveau document d'urbanisme ou justificatif à établir.",
            "du règlement du plan d'occupation des sols applicable prises sur le fondement des articles L. 151-18 et L. 151-19 du code de l'urbanisme",
            "La même exception demeure applicable aux prescriptions correspondantes d'un plan d'occupation des sols légalement applicable ;")],
    ["Évaluation obligatoire de la valeur vénale du bien par un professionnel de l'immobilier pour invoquer le dépassement du seuil de coût de 50 %."],
    "Les quatre exceptions sont préservées pour les futurs bâtiments éligibles : patrimoine et prescriptions architecturales du 1° a à d, coût supérieur à 50 % au 2°, pathologie du bâti au 3°, et autres obligations au 4°. Les labels, sites, droit de surplomb et POS encore légalement applicables ne sont pas fermés. La preuve de valeur vénale est allégée, sans retirer les conditions énergétiques légales ni la note de sécurité du 3°.")

record('R112-19',
    "Maintien intégral justifié : cet article définit les délais maximaux ouvrant la qualification de rénovation performante globale, et non une attente minimale avant travaux. Dix-huit mois pour un logement, vingt-quatre mois jusqu'à cinquante logements et trente-six mois au-delà restent distingués ; le point de départ et la réception finale protègent la lisibilité des droits.",
    "L111-1 a été lu : il exige une durée maximale et le traitement des six postes. Supprimer toute durée ici sans coordination législative laisserait sa qualification incomplète. Ne pas confondre ces durées avec le projet locatif de vingt-quatre mois relevant de la loi de 1989 hors lot, ni avec le préavis individuel de quinze jours. Le renvoi au septième alinéa du 17° bis vise le délai de rénovation globale.",
    "Aucun changement : les seuils de dix-huit, vingt-quatre et trente-six mois et la catégorie favorable des bâtiments de plus de cinquante logements sont conservés intégralement.",
    "L'opportunité de modifier la qualification législative ou les calendriers particuliers d'aides n'est pas démontrée par ces seules sources ; aucun allongement ni réduction de délai n'est compté.",
    "Aucune charge nouvelle identifiée : les événements de premier ordre de service et de dernière réception restent les mêmes, sans attestation, dépôt ou calendrier additionnel.",
    benefit="Le délai plus long de trente-six mois pour les bâtiments de plus de cinquante logements, ainsi que les délais adaptés d'un ou plusieurs logements, restent accessibles aux futurs travaux éligibles. Le maintien ne limite pas les avantages aux rénovations engagées avant la réforme et ne réduit aucun délai existant.")

record('R113-1',
    "Maintien intégral de la règle de localisation des prescriptions techniques des bâtiments professionnels : le titre Ier du livre II de la quatrième partie du code du travail complète le CCH. Ce renvoi évite de recopier les mêmes normes et concerne la conception des lieux de travail, non le régime des contrats individuels.",
    "L112-2 impose que l'ouvrage permette les obligations de l'employeur du titre II ; L112-3 habilite les règles de construction. R113-1 localise, sans confusion, les prescriptions de conception du titre Ier. Les cinq cibles requises sont analysées individuellement. La version source est applicable depuis le 21 novembre 2025 ; cette date n'est pas une entrée en vigueur de la réforme proposée.",
    "Aucune suppression à revendiquer : un renvoi fonctionnel évite un doublon normatif tout en maintenant les exigences de sécurité et de santé des bâtiments professionnels.",
    "Les titres techniques et les obligations des agents publics ne sont pas supprimés ou réattribués au contrat privé. Aucun coût de conformité nouveau ou gain fiscal n'est établi.",
    "Aucune charge nouvelle identifiée : le texte source est maintenu, sans nouveau renvoi à un contrat unique, pièce, autorisation ou délai d'ancienneté.")

n = 'R113-2'
xml = substitute(n, "ces boîtes doivent être regroupées en ensembles homogènes.", "ces boîtes doivent être regroupées ; aucune homogénéité de modèle ou d'aspect n'est imposée sur le fondement du présent article.")
xml = append(xml, "La suppression de l'exigence d'homogénéité s'applique aux installations réalisées à compter de l'entrée en vigueur de la loi de simplification. Elle n'impose aucune modification des installations existantes et ne modifie pas les engagements contractuels valablement conclus.")
record(n,
    "Réduction de fond ciblée : suppression de l'homogénéité obligatoire des ensembles de boîtes aux lettres, sans retirer une boîte par logement ni leur regroupement utile à la desserte. L'arrêté d'application ne peut rétablir cette exigence sur le fondement de l'article ; dimensions fonctionnelles, identification et accès légal restent à leur régime propre.",
    "La suppression ne remet pas en cause le service postal ni les normes autonomes d'accessibilité et de distribution. Les arrêtés et spécifications postales hors lot devront être confrontés à cette coupe, sans prétendre les avoir tous supprimés. Les contrats de fourniture et installations anciennes ne sont pas défaits.",
    "Le constructeur conserve le nombre de boîtes et leur regroupement mais n'est plus obligé de choisir un ensemble homogène. Cette liberté retire une prescription matérielle d'aspect au-delà d'un simple changement de vocabulaire.",
    "Le gain dépend des choix d'équipement et des normes postales autonomes qui restent à vérifier ; aucune économie monétaire nationale n'est avancée.",
    "Aucune charge nouvelle identifiée : même nombre de boîtes et même regroupement, sans contrôle, justification d'hétérogénéité ou déclaration de remplacement.",
    xml, 'material_reduction', [effect('obligation_removed', 'boites-postales-fin-homogeneite',
        "Suppression de l'homogénéité obligatoire des ensembles de boîtes aux lettres.",
        "Une boîte par logement, avec regroupement obligatoire en ensembles homogènes dans les bâtiments comportant plusieurs logements.",
        "Une boîte par logement et regroupement maintenus ; aucun modèle ou aspect homogène imposé par cet article.", 'legal_duty',
        "Maîtres d'ouvrage de bâtiments d'habitation comportant plusieurs logements.",
        "Installations nouvelles après entrée en vigueur ; aucune modification imposée à l'existant et contrats antérieurs préservés.",
        "Aucun critère d'aspect ni justificatif de remplacement ; obligations postales autonomes conservées.",
        "S'il existe plusieurs logements, ces boîtes doivent être regroupées en ensembles homogènes.",
        "aucune homogénéité de modèle ou d'aspect n'est imposée sur le fondement du présent article.")],
    ["Exigence de regroupement des boîtes aux lettres en ensembles homogènes quant à leur modèle ou leur aspect, sans retrait du regroupement lui-même."])

record('R113-3',
    "Maintien intégral : l'équipement fibre des locaux professionnels, le point accessible et l'adduction multiopérateur évitent des reprises lourdes du bâti et protègent l'accès concurrentiel aux réseaux. Une fibre au moins par local et les passages réservés ne sont pas une formalité administrative redondante ; les dérogations par nature, affectation ou situation sont conservées.",
    "L113-10, lu intégralement, impose une infrastructure fixe à très haut débit et à potentiel fibre. Les modalités européennes de préparation numérique des bâtiments et les arrêtés techniques extérieurs doivent rester coordonnés ; leur conformité globale n'est pas présumée. Cet article ne vise pas la durée des emplois exercés dans ces locaux.",
    "Aucun changement ni simplification comptée : l'infrastructure et l'accès à plusieurs opérateurs sont conservés avec les possibilités de dérogation technique déjà prévues.",
    "Le contenu intégral des arrêtés et des règles européennes n'est pas fourni dans le lot ; une suppression générale de la fibre ou des passages n'est pas justifiée par la seule recherche de coupes.",
    "Aucune charge nouvelle identifiée : aucun câble, registre, agrément ou justificatif supplémentaire n'est ajouté au texte source maintenu.",
    benefit="Le dernier alinéa conserve intégralement le pouvoir de prévoir des dérogations pour certaines catégories de bâtiments selon leur nature, leur affectation ou leur situation. Ces possibilités restent ouvertes aux opérations futures ; ni le minimum d'une fibre ni l'accès multiopérateur ne sont durcis sous couvert de simplification.")

n = 'R113-4'
xml = substitute(n,
    "à l'exception des bâtiments situés en \" zone fibrée \", au sens de l'article L. 33-11 du code des postes et des communications électroniques, et sous réserve qu'ils soient pourvus de lignes de communications électroniques à très haut débit en fibre optique desservant chacun des logements.",
    "à l'exception des bâtiments pourvus de lignes de communications électroniques à très haut débit en fibre optique desservant chacun des logements, sans condition de classement en zone fibrée.")
xml = substitute(n,
    "Chaque logement est équipé d'une installation intérieure raccordée aux lignes téléphoniques et aux dispositifs individuels ou collectifs nécessaires à la distribution des services de radiodiffusion",
    "Chaque logement est équipé d'une installation intérieure raccordée aux lignes téléphoniques lorsque celles-ci sont requises au premier alinéa, ainsi qu'aux dispositifs individuels ou collectifs nécessaires à la distribution des services de radiodiffusion",
    xml)
xml = append(xml, "La dispense de lignes téléphoniques distinctes et de leur raccordement intérieur s'applique aux équipements réalisés à compter de l'entrée en vigueur de la loi de simplification, y compris au titre d'une autorisation antérieure. Elle n'impose aucune dépose d'installation existante et ne porte pas atteinte aux contrats de service ni aux dérogations déjà accordées. Les dérogations prévues au septième alinéa demeurent ouvertes aux opérations futures dans les conditions qu'il prévoit.")
record(n,
    "Réduction de fond : la présence de fibre desservant chaque logement dispense des lignes téléphoniques distinctes sans attendre un classement administratif en zone fibrée. Le sixième alinéa est expressément coordonné pour ne pas rétablir le raccordement téléphonique supprimé. Les sept alinéas initiaux, l'ensemble de la radiodiffusion, la fibre de un à quatre brins selon le cas, l'adduction multiopérateur, la desserte des locaux mixtes et les dérogations finales restent conservés.",
    "R112-15 continue de viser la première phrase du premier alinéa : le fondement résiduel de dérogation technique et économique reste cohérent. Le retrait du renvoi à L33-11 n'abroge pas le statut des zones fibrées du CPCE, mais retire seulement sa fonction de condition à la dispense du présent article. L113-10 a été lu : gaines, très haut débit, confidentialité et réseaux ne sont pas supprimés. Coordonner les arrêtés d'application pour qu'ils n'imposent pas un raccordement téléphonique distinct dans le champ dispensé ; aucun arrêté extérieur n'est déclaré réécrit. La desserte téléphonique reste exigée lorsque la condition matérielle de fibre n'est pas satisfaite.",
    "La source dispense les seuls bâtiments à la fois classés en zone fibrée et équipés de fibre. La proposition retire le classement géographique : un bâtiment effectivement fibré peut éviter le second réseau et son raccordement intérieur même hors de cette zone. Les autres équipements ne sont pas allégés fictivement.",
    "Le gain ne couvre pas les bâtiments sans fibre desservant tous les logements ni les obligations autonomes des opérateurs ; le coût et le nombre d'immeubles concernés ne sont pas chiffrés. La conformité européenne globale reste à coordonner.",
    "Aucune charge nouvelle identifiée : le raccordement fibre de tous les logements était déjà imposé au troisième alinéa ; aucun certificat de zonage, abonnement ou déclaration ne le remplace.",
    xml, 'material_reduction', [effect('relief_extended', 'logements-fibres-fin-doublon-telephonique',
        "Extension de la dispense de lignes téléphoniques distinctes à tous les bâtiments matériellement fibrés.",
        "Dispense seulement si le bâtiment est situé en zone fibrée au sens du CPCE et si la fibre dessert chacun des logements ; raccordement téléphonique intérieur encore formulé sans réserve au sixième alinéa.",
        "Dispense dès que la fibre dessert chaque logement, sans classement de zone ; le raccordement intérieur téléphonique n'est requis que lorsque les lignes le sont encore.", 'legal_duty',
        "Maîtres d'ouvrage de bâtiments d'habitation fibrés, notamment ceux situés hors zone officiellement fibrée.",
        "Équipements réalisés après l'entrée en vigueur, même avec autorisation ancienne ; pas de dépose imposée, contrats et dérogations acquis préservés.",
        "Aucun dossier ou certificat de remplacement ; fibre, radiodiffusion et droits des opérateurs maintenus.",
        "à l'exception des bâtiments situés en \" zone fibrée \", au sens de l'article L. 33-11 du code des postes et des communications électroniques, et sous réserve qu'ils soient pourvus de lignes de communications électroniques à très haut débit en fibre optique desservant chacun des logements.",
        "à l'exception des bâtiments pourvus de lignes de communications électroniques à très haut débit en fibre optique desservant chacun des logements, sans condition de classement en zone fibrée.")],
    ["Condition de classement administratif en zone fibrée pour dispenser les bâtiments déjà matériellement fibrés des lignes téléphoniques distinctes.",
     "Raccordement intérieur aux lignes téléphoniques distinctes dans les logements dispensés de ces lignes, par coordination du sixième alinéa avec le premier."],
    "La dispense existante des bâtiments en zone fibrée équipés de fibre est conservée et élargie aux autres bâtiments équipés dans les mêmes conditions. Les dérogations selon la nature, l'affectation ou la situation des bâtiments restent ouvertes pour les opérations futures. La faculté individuelle de R112-15, l'adaptation multi-fibre et les dispositions des usages mixtes ne sont pas supprimées.")

record('R113-5',
    "Maintien intégral de la dispense lorsque l'équipement fibre, travaux induits compris, dépasse 5 % du coût des travaux sous permis. Elle applique la proportionnalité de L113-10 : supprimer le seuil ou l'exclusion rétablirait une obligation plus lourde pour les propriétaires et fermerait un avantage futur.",
    "L113-10 a été lu dans le corpus. Le seuil porte sur un coût de travaux d'équipement, pas sur une taxe ni sur une baisse de taux. La comparaison inclut les travaux induits et conserve l'inégalité stricte supérieur à 5 %. L'arrêté de raccordement reste à sa fonction technique, sans dossier additionnel créé ici.",
    "Aucun changement normatif : le champ des immeubles sous permis et la dispense favorable au-delà de 5 % sont conservés, sans revendiquer une nouvelle exemption.",
    "Les prescriptions techniques détaillées des arrêtés ne sont pas examinées intégralement dans ce lot. Aucun coût net de raccordement ni économie publique n'est calculé.",
    "Aucune charge nouvelle identifiée : même assiette de comparaison, même seuil et mêmes modalités techniques ; aucune attestation professionnelle ou autorisation supplémentaire.",
    benefit="La dispense de fibre en rénovation lorsque son coût, y compris les travaux induits, est strictement supérieur à 5 % du coût des travaux du permis reste intégrale et ouverte aux futures rénovations. Elle n'est ni remplacée par un simple report ni réservée aux propriétaires ayant déjà engagé leur chantier.")

n = 'R113-6'
old = "Les conduits mis en place pour le passage des câbles électriques sont dimensionnés pour autoriser un passage carré d'au moins 100 mm de côté."
new = "Les conduits permettent le passage des câbles nécessaires au pré-équipement défini au premier alinéa ; aucun gabarit minimal de passage carré n'est imposé sur le fondement du présent article."
xml = substitute(n, old, new)
xml = append(xml, "La suppression du gabarit minimal de passage carré s'applique aux conduits installés à compter de l'entrée en vigueur de la loi de simplification, y compris pour les projets déjà autorisés. Elle n'impose aucune modification des installations existantes et ne dispense pas des règles de sécurité électrique et de protection contre l'incendie.")
record(n,
    "Réduction de fond : retrait du gabarit imposant le passage d'un carré de 100 mm de côté dans les conduits, au profit de leur capacité fonctionnelle de passage des câbles déjà requise par le pré-équipement. Les cinq alinéas d'origine sont conservés dans leur ordre ; dimensionnement pour 20 % des emplacements au moins, minimum d'un emplacement, deux voies d'alimentation et compatibilité avec le pilotage sont maintenus.",
    "L113-11 a été lu intégralement : il exige conduits et dispositifs d'alimentation et de sécurité pour une recharge ultérieure, sans imposer lui-même ce gabarit de 100 mm. La suppression ne diminue ni la proportion de places ni la sécurité. Coordonner les arrêtés d'application pour ne pas rétablir le seul gabarit supprimé ; ils ne sont pas déclarés réécrits. Les exigences européennes de pré-équipement et leurs transpositions conservent leur champ : aucune suppression de ces exigences ni conformité globale présumée. Le gabarit source n'impose pas nécessairement un conduit lui-même carré, mais un passage carré : cette distinction est conservée dans l'analyse.",
    "Un dimensionnement géométrique uniforme de passage disparaît effectivement ; la capacité d'accueillir les câbles et d'alimenter au moins 20 % des places reste obligatoire. Aucun gain fiscal ou baisse du nombre de places équipables n'est allégué.",
    "Le coût évité dépend du chantier et n'est pas chiffré. Les capacités électriques, le minimum d'une place et les règles de sécurité sont hors de la coupe ; les arrêtés techniques demandent coordination.",
    "Aucune charge nouvelle identifiée : le dimensionnement fonctionnel était déjà exigé au premier alinéa, aucun calcul certifié, nouveau registre ou agrément ne remplace le gabarit retiré.",
    xml, 'material_reduction', [effect('obligation_removed', 'recharge-fin-gabarit-carre-conduits',
        "Suppression du passage carré minimal de 100 mm de côté, sans diminuer la capacité électrique requise.",
        "Conduits autorisant obligatoirement le passage d'un carré d'au moins 100 mm de côté, en plus du dimensionnement de l'alimentation pour au moins 20 % des places, minimum une.",
        "Conduits adaptés au passage des câbles nécessaires, sans gabarit carré minimal ; alimentation pour au moins 20 % des places, minimum une, inchangée.", 'legal_duty',
        "Maîtres d'ouvrage soumis aux obligations de pré-équipement de stationnement électrique.",
        "Conduits installés après entrée en vigueur, y compris projets autorisés ; aucune reprise obligatoire de l'existant et sécurité électrique conservée.",
        "Aucune attestation ou étude autonome nouvelle ; aptitude fonctionnelle déjà exigée et sécurité maintenues.", old, new)],
    ["Gabarit géométrique uniforme imposant aux conduits le passage d'un carré d'au moins 100 mm de côté, indépendamment des câbles effectivement nécessaires."])

technical_new = "Un descriptif détaillé des travaux à entreprendre, précisant leur implantation, les modalités d'intervention et le raccordement électrique, est joint à la notification. Ces informations peuvent figurer sur un support commun ; aucun plan technique d'intervention ni schéma de raccordement électrique n'est exigé lorsque le descriptif contient ces informations."
technical_old = "Un descriptif détaillé des travaux à entreprendre, assorti d'un plan technique d'intervention et d'un schéma de raccordement électrique, est joint à la notification."
notification_transition = "Ces dispositions s'appliquent aux notifications adressées à compter de l'entrée en vigueur de la loi de simplification. Les notifications antérieures, leurs délais, les procédures engagées et les droits qui en résultent demeurent régis par les dispositions antérieures."

n = 'R113-7'
xml = substitute(n, technical_old, technical_new)
xml = substitute(n,
    "Si l'établissement du plan et du schéma a été rendu impossible du fait du propriétaire ou de ses préposés, ces documents ne sont pas exigés à l'appui de la notification.",
    "Si le propriétaire ou ses préposés ont rendu impossible l'établissement des informations qui auraient figuré sur le plan et le schéma, ces seules informations ne sont pas exigées à l'appui de la notification.",
    xml)
xml = append(xml, notification_transition)
record(n,
    "Réduction de fond : le descriptif détaillé peut porter lui-même les informations d'implantation, d'intervention et de raccordement, sans exiger les deux productions graphiques spécifiques. La dispense en cas d'obstruction du propriétaire reste effective. Notification du propriétaire, information des indivisaires, recours pour motif sérieux et légitime, trois mois pour saisir, quinze jours pour notifier, trois et six mois pour les travaux sont maintenus.",
    "L113-16 et L113-17 ont été lus : le droit à la prise, le comptage individuel, l'accès à l'étude et au devis et la convention d'intervention restent distincts du descriptif. La notification est un instrument d'information et de recours, pas un agrément du propriétaire. Les six alinéas initiaux sont gardés dans le même ordre, notamment le renvoi au cinquième alinéa. Les délais de trois mois sont propres au droit à la prise, sans lien avec les quinze jours du préavis de travail. Les prescriptions de sécurité électrique et les documents imposés sur un fondement autonome ne sont pas supprimés.",
    "La source réclame un descriptif assorti d'un plan technique et d'un schéma ; la proposition admet un descriptif suffisant sans ces deux livrables graphiques obligatoires. Le contenu utile et les recours du propriétaire restent disponibles ; aucune seconde suppression du droit d'information n'est comptée.",
    "Aucun coût moyen ni gain de délai de recours n'est chiffré. Les notifications antérieures, la convention L113-17 et les exigences autonomes de sécurité ne sont pas couvertes par la dispense documentaire nouvelle.",
    "Aucune charge nouvelle identifiée : l'information d'implantation, d'intervention et de raccordement remplace les représentations déjà dues, sans expertise, attestation ou donnée supplémentaire.",
    xml, 'material_reduction', [effect('obligation_merged', 'recharge-dossier-technique-support-commun',
        "Intégration des informations techniques dans le descriptif, avec suppression des deux livrables graphiques obligatoires.",
        "Descriptif détaillé obligatoirement assorti d'un plan technique d'intervention et d'un schéma de raccordement électrique.",
        "Descriptif contenant les informations utiles, sur un support commun et sans plan ou schéma distincts obligatoires.", 'legal_duty',
        "Locataires et occupants de bonne foi installant une recharge dans un bâtiment hors copropriété.",
        "Notifications nouvelles après entrée en vigueur ; anciens délais et procédures conservés, obstruction du propriétaire ne bloquant pas le dossier.",
        "Même information technique ; aucune nouvelle formalité de validation ni réduction du droit au juge.", technical_old,
        "Ces informations peuvent figurer sur un support commun ; aucun plan technique d'intervention ni schéma de raccordement électrique n'est exigé lorsque le descriptif contient ces informations.")],
    ["Production systématique d'un plan technique d'intervention et d'un schéma de raccordement électrique en plus du descriptif détaillé lorsque celui-ci fournit les informations nécessaires."],
    "Le droit à la prise du locataire ou occupant de bonne foi reste ouvert aux futurs travaux. La dispense de pièces rendues impossibles par le propriétaire est conservée sous forme d'une dispense des seules informations techniques empêchées. La forclusion de l'opposition, les délais de réalisation promis par le propriétaire et la faculté de réaliser les travaux en cas de carence restent intacts.")

n = 'R113-8'
xml = substitute(n, technical_old, technical_new)
xml = substitute(n,
    "Si l'établissement du plan et du schéma a été rendu impossible du fait du syndic ou de ses préposés, ces documents ne sont pas exigés à l'appui de la notification.",
    "Si le syndic ou ses préposés ont rendu impossible l'établissement des informations qui auraient figuré sur le plan et le schéma, ces seules informations ne sont pas exigées à l'appui de la notification.",
    xml)
xml = substitute(n,
    "avec copie au syndic de la copropriété.",
    "avec copie de la notification et de ses pièces au syndic de la copropriété.",
    xml)
relay_old = "Dans le délai d'un mois suivant la réception de cette notification, le copropriétaire bailleur notifie au syndic les documents qui lui ont été notifiés par le locataire ou l'occupant de bonne foi."
relay_new = "La réception par le syndic de la copie de la notification et de ses pièces prévue au premier alinéa vaut notification au syndic ; aucune nouvelle transmission de ces documents par le copropriétaire bailleur n'est exigée."
xml = substitute(n, relay_old, relay_new, xml)
xml = append(xml, notification_transition)
record(n,
    "Réduction de fond : suppression de la seconde notification obligatoire par le bailleur au syndic sous un mois, la copie intégrale déjà adressée au syndic valant notification. Coordination du dossier technique avec R113-7 pour permettre un descriptif commun sans deux livrables graphiques imposés. Les onze alinéas initiaux, dont 1° et 2°, et les garanties judiciaires et d'information de l'assemblée sont maintenus dans leur ordre.",
    "Le quatrième alinéa conserve son emplacement et définit le fait de réception valant notification ; les renvois aux quatrième ou cinquième alinéas, au sixième et au septième restent donc opératoires sans renumérotation. Le délai de saisine reste de trois mois à compter de la réception complète par le syndic, et non de la future retransmission supprimée. Pour les notifications antérieures, la transition maintient les délais anciens : aucun recours n'est raccourci rétroactivement. Les délais de quinze jours, trois et six mois, le motif sérieux et légitime, la date de décision d'assemblée le cas échéant et son information subsistent. R113-10 proposé ouvre des supports de notification avec réception prouvable. La pièce technique et le circuit direct constituent deux mesures distinctes, chacune dédupliquée.",
    "Le doublon certain est la retransmission par le bailleur de pièces déjà copiées au syndic ; elle disparaît, ainsi que le décalage possible de son envoi sous un mois. Les trois mois d'opposition du syndic ne sont pas réduits. La simplification du dossier technique coordonne la même mesure que R113-7.",
    "Le coût net et la rapidité pratique de la copie initiale ne sont pas chiffrés. La notification du projet aux deux destinataires, les litiges, la convention d'accès et les notifications antérieures restent couverts par leurs règles conservées.",
    "Aucune charge nouvelle identifiée : la copie au syndic existait déjà et inclut les pièces du même dossier ; aucune donnée, signature ou transmission supplémentaire ne remplace l'envoi du bailleur.",
    xml, 'material_reduction', [
        effect('obligation_removed', 'recharge-copropriete-notification-directe',
            "Suppression de la retransmission du dossier par le bailleur au syndic qui en reçoit déjà copie.",
            "Le locataire notifie le bailleur avec copie au syndic, puis le bailleur doit notifier à nouveau les documents au syndic sous un mois.",
            "La réception de la copie complète par le syndic vaut notification ; le bailleur n'envoie plus les mêmes documents une seconde fois.", 'legal_duty',
            "Copropriétaires bailleurs et demandeurs de recharge électrique en copropriété.",
            "Notifications postérieures à l'entrée en vigueur ; délai de trois mois du syndic à compter de sa réception complète ; anciennes notifications conservant leurs délais.",
            "Copie déjà obligatoire simplement reconnue comme notification ; aucun dépôt ni délai de remplacement.", relay_old, relay_new),
        effect('coordination', 'recharge-dossier-technique-support-commun',
            "Application en copropriété du dossier technique simplifié de la même mesure que R113-7.",
            "Descriptif détaillé assorti obligatoirement d'un plan technique et d'un schéma électrique.",
            "Informations techniques du descriptif pouvant figurer sur un support commun sans livrables graphiques distincts.", 'legal_duty',
            "Locataires, occupants et copropriétaires installant une recharge dans un immeuble en copropriété.",
            "Notifications nouvelles ; dispense pour obstruction du syndic et recours des notifications anciennes conservés.",
            "Aucune nouvelle donnée ni autorisation ; mêmes informations nécessaires au raccordement.", technical_old,
            "Ces informations peuvent figurer sur un support commun ; aucun plan technique d'intervention ni schéma de raccordement électrique n'est exigé lorsque le descriptif contient ces informations.")],
    ["Seconde notification obligatoire par le copropriétaire bailleur au syndic sous un mois des documents déjà reçus en copie de la notification initiale.",
     "Production systématique d'un plan technique d'intervention et d'un schéma électrique distincts du descriptif lorsque les mêmes informations peuvent être décrites sur le support commun."],
    "Les droits futurs du locataire, occupant et copropriétaire à installer la recharge restent ouverts. L'exemption en cas de documents empêchés par le syndic, la forclusion faute de saisine, les trois et six mois pour les travaux collectifs et le contrôle judiciaire subsistent. La suppression du relais du bailleur ne retranche pas le délai de trois mois dont dispose le syndic à compter de sa réception.")

n = 'R113-9'
old = "En cas de copropriété, cette notification est faite au copropriétaire bailleur, qui transmet ces informations au syndic représentant le syndicat des copropriétaires, dans les mêmes formes et dans un délai de quinze jours à compter de la date de la notification qui lui a été faite."
new = "En cas de copropriété, le locataire ou l'occupant de bonne foi peut adresser cette notification directement au syndic représentant le syndicat des copropriétaires, avec copie au copropriétaire bailleur ; celui-ci n'a pas à transmettre de nouveau ces informations. À défaut de cette notification directe, la notification est faite au copropriétaire bailleur, qui transmet ces informations au syndic représentant le syndicat des copropriétaires, dans les mêmes formes et dans un délai de quinze jours à compter de la date de la notification qui lui a été faite."
xml = substitute(n, old, new)
xml = append(xml, notification_transition)
record(n,
    "Réduction de fond dans le même circuit direct que R113-8 : option de notification des coordonnées du prestataire au syndic, avec copie au bailleur, qui est dispensé du relais. La voie ancienne par le bailleur reste disponible avec ses quinze jours. Ni les données du prestataire ni la convention préalable et son délai de deux mois ne sont supprimés ; l'absence d'autorisation de l'assemblée générale et le recours au juge restent intacts.",
    "Les cinq alinéas initiaux restent à leur place, dont le renvoi à l'alinéa précédent pour le délai de convention. L113-17, lu, exige la convention avant travaux pour l'accès, l'intervention, la gestion et l'entretien : aucune autorisation tacite du chantier ne la remplace. En voie directe, les deux mois courent à la réception du syndic ; en voie ancienne, à la notification qu'il reçoit du bailleur. Aucun renvoi nouveau à une cible extérieure n'est ajouté. La voie directe coordonne la même mesure recharge-copropriete-notification-directe, sans compter une seconde procédure générale supprimée.",
    "La source impose un relais par le bailleur même lorsque le syndic pourrait recevoir les coordonnées directement ; cette obligation cesse lorsqu'est choisie la voie directe. Le canal antérieur et les deux mois pour conclure la convention demeurent, sans prétendre que ce délai maximal était une attente obligatoire.",
    "Les usagers peuvent conserver la voie ancienne : aucune économie universelle de quinze jours n'est garantie. Les données nécessaires, le contrat du prestataire et la convention d'accès restent requis ; aucun coût net n'est chiffré.",
    "Aucune charge nouvelle obligatoire identifiée : l'option conserve les deux destinataires déjà existants ; la copie au bailleur remplace la notification initiale qu'il recevait, et le relais au syndic disparaît. L'ancienne voie reste librement utilisable.",
    xml, 'material_reduction', [effect('obligation_removed', 'recharge-copropriete-notification-directe',
        "Dispense du relais des coordonnées du prestataire par le bailleur lorsque l'usager notifie directement le syndic.",
        "Notification des nom, adresse et téléphone du prestataire au bailleur, puis retransmission obligatoire par celui-ci au syndic sous quinze jours.",
        "Option de notification directe au syndic avec copie au bailleur, sans retransmission ; ancienne voie et son délai maximal de quinze jours conservés si l'option n'est pas utilisée.", 'legal_duty',
        "Locataires, occupants de bonne foi et copropriétaires bailleurs concernés par l'installation d'une recharge.",
        "Notifications nouvelles après entrée en vigueur ; deux mois pour conclure la convention à compter de la réception par le syndic ; procédures et délais antérieurs préservés.",
        "Option sans nouvelle donnée ni destinataire : copie au bailleur à la place de sa notification initiale et de son relais.", old,
        "le locataire ou l'occupant de bonne foi peut adresser cette notification directement au syndic représentant le syndicat des copropriétaires, avec copie au copropriétaire bailleur ; celui-ci n'a pas à transmettre de nouveau ces informations.")],
    ["Retransmission obligatoire par le copropriétaire bailleur sous quinze jours des coordonnées du prestataire lorsque l'usager choisit de notifier directement le syndic avec copie au bailleur."],
    "La dispense d'autorisation de l'assemblée générale pour signer la convention demeure entière pour les futures installations. Le droit de saisir le juge si la convention n'est pas signée dans les deux mois est maintenu ; l'option directe ne supprime ni la voie ancienne ni les garanties d'accès aux parties communes.")

n = 'R113-10'
xml = "<p>Les notifications prévues aux articles R. 113-7 à R. 113-9 sont faites par lettre recommandée avec demande d'avis de réception ou par tout autre moyen permettant d'établir leur contenu et donnant date certaine à leur réception. La remise contre récépissé ou émargement est admise. Les notifications électroniques respectent les conditions légales qui leur sont applicables, notamment le consentement du destinataire lorsqu'il est requis ; un simple envoi de courriel ne vaut pas preuve de réception.</p><p>Ces dispositions s'appliquent aux notifications effectuées à compter de l'entrée en vigueur de la loi de simplification. Elles ne remettent pas en cause la validité des notifications antérieures, les délais déjà commencés ni les actes régulièrement accomplis dans les procédures en cours.</p>"
record(n,
    "Réduction de fond : suppression de l'exclusivité de la lettre recommandée avec avis de réception pour les notifications du droit à la prise. La remise contre récépissé et les autres moyens prouvant contenu et réception datée deviennent utilisables ; les conditions légales de l'électronique et les délais de recours demeurent.",
    "Les destinataires sont privés, à la différence d'une simple reprise du CRPA pour une administration. L'équivalence légale déjà existante de la lettre recommandée électronique n'est pas comptée comme un nouvel avantage ; le gain est l'ouverture aux autres supports probants, dont la remise. Aucun courriel ordinaire n'est réputé reçu. Vérifier les règles de notification des lois et décrets extérieurs applicables : le présent texte ne les abroge pas et n'ouvre pas de nouveaux délais pour les procédures anciennes.",
    "L'article source exige une forme recommandée pour toutes les notifications de R113-7 à R113-9. La proposition permet d'éviter cet achat et cet acheminement en choisissant un autre support probant, sans réduire le délai du destinataire ni le droit au juge.",
    "Aucun tarif d'envoi ni coût moyen n'est avancé ; certains usagers conserveront le recommandé. Les règles légales électroniques autonomes et les notifications déjà faites restent hors de la coupe.",
    "Aucune charge nouvelle identifiée : la preuve du contenu et de la date de réception correspond à la fonction déjà remplie par le recommandé ; les supports alternatifs sont facultatifs et aucun abonnement ni équipement n'est imposé.",
    xml, 'material_reduction', [effect('compliance_cost_reduced', 'recharge-notification-support-probant-libre',
        "Libre choix d'un support prouvant contenu et réception à la place du recommandé obligatoire.",
        "Lettre recommandée avec demande d'avis de réception imposée pour les notifications du droit à la prise, sous les équivalences électroniques légales déjà existantes.",
        "Recommandé ou autre moyen probant, notamment remise contre récépissé ; aucune dépense postale obligatoire si une alternative valable est choisie.", 'legal_duty',
        "Locataires, occupants, propriétaires, bailleurs et syndics effectuant les notifications de R113-7 à R113-9.",
        "Notifications nouvelles après entrée en vigueur ; anciennes notifications, délais et procédures non modifiés ; consentement électronique légalement requis conservé.",
        "Aucune plateforme ni confirmation supplémentaire ; preuve de réception et contenu conservée sans présomption de réception d'un simple courriel.",
        "Les notifications prévues aux articles R. 113-7 à R. 113-9 sont faites par lettre recommandée avec demande d'avis de réception.",
        "La remise contre récépissé ou émargement est admise.")],
    ["Exclusivité de la lettre recommandée avec avis de réception pour les notifications relatives au droit à la prise, remplacée par un choix facultatif de moyens probants."])

record('R113-11',
    "Maintien intégral utile des trois définitions : vélo incluant l'assistance électrique, infrastructures de stationnement sécurisé, et ensemble d'habitations à partir de deux logements. Ces définitions n'imposent par elles-mêmes aucun quota, autorisation ni nouveau chantier et évitent les divergences de champ des articles suivants.",
    "La note source sur l'entrée en vigueur six mois après publication du décret de juin 2022 est une transition historique, non un nouveau délai de la réforme. Ne pas confondre ensemble d'habitations d'au moins deux logements et définition générale du bâtiment collectif de L111-1. R311-1 du code de la route est un renvoi de définition technique, non une règle du contrat de travail ; aucun nouveau renvoi à cette cible non fournie n'est créé.",
    "Aucun changement ni gain matériel compté : les champs techniques du stationnement sécurisé des vélos et des cycles assistés sont conservés sans reformulation de remplissage.",
    "Les nombres de places et conditions des articles suivants ne sont pas traités par cette définition seule ; aucune réduction de leurs exigences n'est présumée ni chiffrée.",
    "Aucune charge nouvelle identifiée : le texte source et sa portée définitionnelle sont intégralement maintenus, sans données, contrôle ou équipement supplémentaire.")


# Vérifications spécifiques, exactement limitées aux cibles requises par source.
checks = {
    'R112-18': {
        'L1234-1': "R112-18 ne renvoie pas à L1234-1 : il définit les exceptions d'une rénovation énergétique. Les contraintes de propriété du 4° ne sont pas un préavis de licenciement. Le préavis proposé de quinze jours pour les contrats nouveaux, sa notification et la conservation des durées anciennes selon l'ancienneté n'affectent donc aucun alinéa de cet article ; aucune durée de rénovation n'est ramenée à quinze jours.",
        'L1221-2': "L1221-2 porte sur les contrats de travail privés et la fin automatique d'un emploi ; R112-18 porte exclusivement sur les bâtiments et travaux. La mission d'un professionnel immobilier ou de l'homme de l'art du 3° n'est pas un cas de CDD créé par le CCH. Le contrat unique futur, les anciens contrats et leur transition ne modifient pas les exceptions énergétiques ; aucun renvoi artificiel n'est ajouté.",
        'L1234-9': "Aucune indemnité de rupture ni condition d'ancienneté n'est visée par R112-18. Le coût de travaux supérieur à 50 % d'une valeur vénale ne représente ni une indemnité ni un salaire de référence. Le seuil proposé d'un an à la fin effective, préavis inclus, le calcul de 0,20 mois sur toute l'ancienneté et le plafond de six mois restent étrangers à cet article ; les droits anciens et indemnités spéciales ne sont pas affectés.",
        'L113-5-1': "Le d du 1° réserve expressément le droit de surplomb de L113-5-1 : 35 cm au plus, hauteur de deux mètres sauf accord, indemnité préalable, acte authentique ou décision publiée, accès temporaire indemnisé et convention restent opératoires. Les six mois d'opposition et de saisine du juge sont ceux du voisin après notification, sans rapport avec le préavis du travail. La correction POS/PLU et la preuve libre de la valeur vénale ne retirent ni ces garanties ni les frais de dépose du IV ; le droit reste ouvert aux futures isolations éligibles."
    },
    'R113-1': {
        'L1234-1': "Le titre Ier du livre II de la quatrième partie du code du travail visé par R113-1 traite des lieux de travail ; L1234-1 relève du livre II de la première partie et du licenciement. Il n'est donc pas une norme technique appelée ici. Les quinze jours proposés, la notification et les anciens préavis modulés par ancienneté ne s'appliquent à aucun délai de construction par ce renvoi.",
        'L1221-2': "Le renvoi de R113-1 n'atteint pas L1221-2 : la règle du contrat unique est dans la première partie du code du travail, tandis que le CCH désigne la quatrième partie, livre II, titre Ier, pour la conception des bâtiments professionnels. Une durée de travaux ou mission de conception ne fixe pas un terme d'emploi. La proposition de contrat unique et ses contrats antérieurs ne commandent aucune modification du présent renvoi.",
        'L1234-9': "L1234-9 n'est pas compris dans les prescriptions de construction de la quatrième partie visées par R113-1. Son indemnité ordinaire proposée, nulle avant un an puis de 0,20 mois sur l'ancienneté totale avec préavis inclus et plafond de six mois, ne définit ni un coût de chantier ni un seuil d'autorisation. Les droits antérieurs et indemnités spéciales restent hors de ce renvoi ; aucune coordination du barème n'est requise ici.",
        'L112-3': "R113-1 vise effectivement L112-3, qui réserve à un décret en Conseil d'État les principales règles de construction sauf disposition contraire. La proposition fournie est une formulation équivalente, pas le droit déjà modifié. La localisation de certaines prescriptions techniques dans le code du travail reste cohérente avec cette habilitation ; aucune ancienneté ou notification de rupture n'y figure et aucun nouveau pouvoir d'agrément n'est créé.",
        'L112-2': "R113-1 vise effectivement L112-2 : la conception du bâtiment professionnel doit permettre les obligations de l'employeur figurant au titre II du livre II de la quatrième partie du code du travail. R113-1 localise quant à lui les règles de conception au titre Ier : ces titres ont des fonctions complémentaires et ne doivent pas être fusionnés. La proposition de L112-2 maintient cette distinction, sans importer le contrat unique, les préavis ou les conditions d'ancienneté."
    }
}

for number, result in answers.items():
    key = result['code_id'] + '|' + result['source_id']
    for target_key in refs['requirements'][key]:
        target = refs['targets'][target_key]
        result['reference_checks'].append(dict(target_key=target_key,
            view_sha256=target['view_sha256'],
            assessment=checks[number][target['number']]))

ordered = [answers[a['number']] for a in sources]
assert len(ordered) == 24
Path('answer.json').write_text(json.dumps(ordered, ensure_ascii=False, indent=2) + '\n')
print('answer.json :', len(ordered), 'articles')
