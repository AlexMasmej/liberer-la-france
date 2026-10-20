import json
import re
from html import unescape
from pathlib import Path

SOURCES = json.loads(Path('source.json').read_text())
REFS = json.loads(Path('reference-targets.json').read_text())
BY_NUMBER = {s['number']: s for s in SOURCES}
TARGETS = REFS['targets']
TARGET_NUMBER = {v['number']: k for k, v in TARGETS.items()}
POLICY = 'editorial_direction_2026_10_19'

def plain(xml):
    return unescape(re.sub(r'<[^>]*>', '', xml or ''))

def previous(number):
    return BY_NUMBER[number]['previous_draft']['proposed_xml']

def paras(*parts):
    return '\n'.join('<p>' + x + '</p>' for x in parts)

def effect(kind, measure, description, before, after, unit, population, transition, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure, description=description, before=before,
                after=after, unit=unit, affected_population=population,
                conditions_and_transition=transition, replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)

def impact(classification, assessment, limitations, burdens, effects):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=limitations, new_burdens_review=burdens, effects=effects)

ANSWER = []

def add(number, proposed, reason, notes, substantive, removed=None, repeal_scope=None, benefit=None):
    source = BY_NUMBER[number]
    obj = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    obj.update(proposed_xml=proposed, reason=reason, review_notes=notes,
               status='retained_unchanged' if proposed is None else 'rewrite_draft',
               substantive_impact=substantive)
    if removed:
        obj.update(change_type='normative_reduction', reform_policy_id=POLICY, removed_provisions=removed)
    if repeal_scope:
        obj.update(change_type='full_repeal', repeal_policy_id=POLICY, repeal_scope=repeal_scope)
    if benefit:
        obj['benefit_review'] = benefit
    ANSWER.append(obj)
    return obj

add('R4625-1', previous('R4625-1'),
    "Coordination de fond avec la disparition des nouveaux CDD privés : maintien du suivi équivalent pour les anciens contrats et des dispenses pour les futurs contrats uniques. Après réexamen, le brouillon est conservé : supprimer la périodicité équivalente ou les dispenses affaiblirait la santé au travail ou recréerait des visites. Cet article ne crée ni cotisation, ni dossier, ni visite distincte à retirer. Aucune coupe supplémentaire autonome n'est revendiquée.",
    "R. 4624-15 et R. 4624-27 ont été lus en entier dans le corpus : conditions cumulatives d'emploi identique, risques équivalents, attestation ou avis détenu et absence de mesure ou d'inaptitude sur cinq ans, trois ans dans le champ de R. 4624-17, ou deux ans pour l'aptitude. Ces périodes et conditions ne sont pas réduites. Les renvois demeurent ceux de la source. Une conversion ne crée pas à elle seule un nouveau risque ni une nouvelle visite ; elle ne dispense pas du suivi requis pour une autre raison. La réserve de droit public est limitée aux seuls contrats entrant déjà dans le champ de l'article, sans leur étendre le contrat privé. Le titre de la section devra être coordonné avec les anciens CDD et le contrat unique. Aucun taux d'indemnité de rupture n'est fixé ici.",
    impact('coordination_only',
        "Par rapport à la source entière, la garantie de suivi et les deux dispenses sont conservées ; seule leur articulation avec les anciens CDD et les nouveaux contrats uniques est explicitée. Il n'est démontré aucune visite supprimée supplémentaire.",
        "Le suivi périodique, les risques nouveaux et les régimes publics hors du champ initial ne sont pas modifiés ; les chapitres Ier à IV ne sont pas réécrits par ce lot.",
        "Aucune charge nouvelle n'est identifiée : la proposition n'exige ni visite de conversion, ni attestation nouvelle, ni collecte supplémentaire et maintient les conditions des dispenses existantes.",
        [effect('coordination', 'contrat-unique-suivi-medical',
            "Maintien du suivi et des dispenses lors du changement de support contractuel, sans compter une nouvelle suppression de visite.",
            "CDD : chapitres Ier à IV et périodicité équivalente à celle des CDI, avec les dispenses visées.",
            "Anciens CDD : mêmes garanties ; futurs contrats uniques : mêmes chapitres et dispenses aux conditions existantes.", 'regime',
            "Travailleurs relevant de ces règles de santé au travail.",
            "Nouveaux contrats privés à compter de l'entrée en vigueur ; contrats antérieurs préservés et droit public à son champ propre.",
            "Aucune visite ni déclaration de remplacement ; les protections médicales demeurent.",
            "Ces travailleurs bénéficient d'un suivi individuel de leur état de santé d'une périodicité équivalente à celui des salariés en contrat à durée indéterminée",
            "Les travailleurs recrutés sous contrat unique relèvent des mêmes chapitres et conservent, lorsque leurs conditions sont remplies, les dispenses de nouvelle visite ou de nouvel examen prévues aux articles R. 4624-15 et R. 4624-27.")]))

add('R4626-12', previous('R4626-12'),
    "Réforme de fond conservée après seconde passe : suppression de l'information administrative distincte de nomination ou de recrutement au directeur régional, sans formalité de remplacement. La représentation du personnel reste informée et l'avis conforme de rupture demeure : il protège l'indépendance du médecin contre son employeur. Aucune suppression supplémentaire des consultations protectrices n'est justifiée ; leur pluralité ne suffit pas à établir un doublon entre instances de champs différents.",
    "R. 4626-9, R. 4626-10 et R. 4626-11 lus intégralement : qualification, dérogation pour les médecins en fonction au 8 septembre 1985 et modèle contractuel restent autonomes. L. 952-21 du code de l'éducation et L. 6152-1, 1°, du code de la santé publique, renvois déjà présents, ne sont pas fournis dans les cibles : leur contenu n'est pas réécrit ni attribué au contrat privé. Les dénominations comité technique d'établissement/CSE et direction régionale sont celles de la source ; leur succession institutionnelle nécessite une coordination extérieure explicite selon l'établissement. Avis conforme de l'inspecteur, consultation du CSE et avis du médecin inspecteur ne sont pas supprimés par le préavis individuel. La transition met fin aussi aux informations non encore envoyées ; les informations déjà données restent valables.",
    impact('material_reduction',
        "La source entière imposait une information supplémentaire de l'administration à chaque nomination ou recrutement. La proposition retire ce destinataire et ce seul envoi, tout en maintenant les informations représentatives et le contrôle protecteur de la rupture. Cette coupe était déjà dans le brouillon.",
        "Ni les règles disciplinaires extérieures ni les avis protecteurs ne sont abrogés. Le coût de l'envoi retiré et le solde de complexité de l'ensemble des codes ne sont pas chiffrés.",
        "Aucune charge nouvelle n'est identifiée : pas de déclaration substitutive, pas de registre et pas de modification des avis conformes ou consultations déjà imposés par la source.",
        [effect('obligation_removed', 'medecin-travail-fin-information-regionale',
            "Suppression de l'envoi distinct de l'information de nomination ou de recrutement à l'autorité régionale.",
            "Information du comité technique, du CSE et du directeur régional à la nomination ou au recrutement.",
            "Information du comité technique et du CSE ; aucun envoi distinct à la direction régionale sur ce fondement.", 'legal_duty',
            "Établissements recrutant ou nommant un médecin du travail dans le champ de l'article.",
            "Suppression dès l'entrée en vigueur, y compris pour les informations encore non transmises ; actes et informations antérieurs valables.",
            "Aucun destinataire ou dépôt administratif de remplacement ; protection de rupture conservée.",
            "L'établissement informe le comité technique d'établissement, le           comité social et économique et le directeur régional des entreprises, de la concurrence, de la consommation, du travail et de l'emploi de la nomination ou du recrutement du médecin du travail.",
            "l'information distincte du directeur régional des entreprises, de la concurrence, de la consommation, du travail et de l'emploi sur la nomination ou le recrutement n'est plus requise")]),
    removed=["L'information distincte du directeur régional lors de la nomination ou du recrutement du médecin du travail, sans dépôt ni déclaration de remplacement."])

add('R5122-18', previous('R5122-18'),
    "Réforme favorable déjà acquise : retrait de l'exclusion des intérimaires en CDI du plancher horaire spécifique d'activité partielle, ouvert aussi aux futures embauches en contrat unique. La seconde passe ne retire ni la majoration de formation à 100 %, ni les salaires de référence variables, ni les protections du temps partiel. Les plafonds d'allocation et de rémunération nette évitent une indemnisation excédant la perte ou la prestation payée. Leur suppression n'est pas justifiée. L'extension crée corrélativement un minimum à verser par l'employeur : elle n'est pas présentée comme une baisse de son coût.",
    "Les sept alinéas sources sont couverts : 60 % du brut, plafond de référence de 4,5 SMIC horaire, moyenne sur douze mois civils ou tous les mois travaillés si moins de douze, 100 % du net durant les formations de L. 5122-2, limite d'allocation apprentissage/professionnalisation, plafond du net et exception des salaires horaires inférieurs au SMIC. L. 1251-58-1 fourni et L. 1251-58-2/3 lus dans le corpus distinguent mission et emploi, garantie mensuelle et intermissions ; aucune double indemnisation n'est créée. L. 3121-27/28 et L. 3123-1 lus : 40 heures pour les nouveaux contrats, 35 pour les anciens selon les propositions, sans relèvement implicite des 1 607 heures ou des régimes annuels. Les renvois sont ceux de la source ; le dispositif de calcul doit être coordonné avec les textes de durée du travail. La note du 1er janvier 2023 reste une application historique, distincte de l'extension aux heures futures. La dépense publique et le coût patronal net restent à établir.",
    impact('mixed',
        "Par rapport à la source officielle entière, une exclusion du plancher est supprimée au bénéfice des CDI intérimaires, y compris futurs ; le même changement étend l'obligation minimale de versement patronal. Les paramètres généraux de l'indemnité et ses autres garanties demeurent. Ce n'est pas une suppression de prélèvement.",
        "L'effet sur l'allocation remboursée à l'employeur, les autres planchers autonomes et le coût budgétaire global ne sont pas chiffrés. Seules les heures futures bénéficient de l'extension.",
        "Charge nouvelle identifiée : les employeurs de CDI intérimaires entrent dans le plancher spécifique de cet article, sous sa réserve du salaire inférieur au SMIC. Aucun nouveau formulaire ou registre ; le solde patronal net n'est pas établi.",
        [effect('relief_extended', 'activite-partielle-plancher-interim',
            "Extension de la garantie horaire aux intérimaires déjà ou nouvellement employés à durée indéterminée.",
            "Les salariés de L. 1251-58-1 sont exclus du plancher spécifique ; règle générale de 60 % du brut, référence plafonnée à 4,5 SMIC.",
            "Le plancher SMIC horaire inclut ces salariés, avec indemnité égale au salaire horaire si celui-ci est inférieur au SMIC ; autres paramètres maintenus.", 'euro',
            "Intérimaires relevant de L. 1251-58-1, anciens CDI et futurs contrats uniques.",
            "Heures chômées à compter de l'entrée en vigueur ; les heures antérieures restent régies par leur droit ; pas de cumul fictif avec les intermissions.",
            "Le minimum patronal est étendu : effet corrélatif décrit sous obligation_added, sans deuxième avantage distinct.",
            "à l'exception de ceux mentionnés à l'article L. 1251-58-1",
            "y compris ceux mentionnés à l'article L. 1251-58-1"),
         effect('obligation_added', 'activite-partielle-plancher-interim',
            "Contrepartie patronale du même plancher étendu ; il ne s'agit pas d'une seconde mesure.",
            "Les employeurs de ces CDI ne sont pas assujettis au plancher spécifique prévu par cet alinéa.",
            "Ils versent au moins le SMIC horaire, ou le salaire horaire s'il est inférieur, dans les conditions de cet article.", 'legal_duty',
            "Entreprises de travail temporaire employant les salariés de L. 1251-58-1 en activité partielle.",
            "Application aux seules heures futures à compter de l'entrée en vigueur, y compris sous CDI existant.",
            "Minimum de versement élargi ; couverture par l'allocation et solde net à vérifier, sans reporting ajouté.",
            "le taux horaire de l'indemnité d'activité partielle ne peut être inférieur au taux horaire du salaire minimum interprofessionnel de croissance, sous réserve des dispositions du dernier alinéa.",
            "Pour tous les salariés des entreprises de travail temporaire régis par le chapitre Ier du titre V du livre II de la première partie du présent code, y compris ceux mentionnés à l'article L. 1251-58-1")]),
    removed=["L'exclusion des salariés intérimaires mentionnés à L. 1251-58-1 du plancher horaire spécifique d'indemnisation de l'activité partielle."])

add('R5131-21', None,
    "Maintien intégral nécessaire, après lecture de la source et du précédent brouillon. La déduction est une imputation sur l'allocation du contrat d'engagement jeune, non une déduction fiscale : les trois catégories de ressources financent déjà le remplacement du revenu ou la formation. Le texte n'impose aucun envoi, agrément, justificatif autonome ou délai minimal. Retirer la liste changerait le financement de l'allocation et les cumuls sans supprimer un doublon administratif démontré. La reformulation stylistique antérieure n'est donc pas reprise ni comptée comme réécriture.",
    "R. 5131-20, R. 5131-22, D. 5131-23, R. 5131-25 et L. 5131-6 lus intégralement dans le corpus : distinction entre ressources intégralement imputées, revenus partiellement déductibles et autres ressources cumulables. Le renvoi au 1° de R. 5131-20 est préexistant ; le corpus actuel porte ce 1° au I, sans changement de règle. Le 8° de L. 1233-68 fourni règle l'allocation du CSP ; ses 1° et 2° sur ancienneté/adhésion ne sont pas les règles ordinaires de rupture. Les références au code de l'éducation demeurent à leur champ et ne sont pas vérifiées comme contenu d'un contrat privé. La date du 1er mars 2022 est historique. Les pièces et délais de R. 5131-25 sont hors lot et ne sont pas présentés comme supprimés.",
    impact('retained_necessary',
        "La liste officielle est maintenue en entier : aucune nouvelle coupe ni économie n'est revendiquée. Elle délimite l'imputation des allocations chômage/CSP, stages et écoles de la deuxième chance sur une allocation sous condition de ressources, sans formalité autonome.",
        "Le maintien n'approuve pas les justificatifs ou forclusions d'autres articles ; les montants d'allocation et le financement global ne sont pas recalculés. La coordination des salaires d'insertion relève de R. 5131-24 dans ce lot.",
        "Aucune charge nouvelle n'est identifiée puisque le texte source est reproduit sans modification ; aucune déclaration, condition, pièce ou période de référence supplémentaire n'est créée.", []),
    benefit="Les trois catégories ne sont pas des avantages fiscaux : leur déduction intégrale réduit le montant du CEJ, sans réduire les allocations de chômage et de CSP, les revenus de stages ni la rémunération des écoles de la deuxième chance elles-mêmes. Leur éligibilité et leurs droits propres restent applicables aux situations futures. Le renvoi à L. 1233-68 inclut son allocation du 8°, non l'indemnité ordinaire de L. 1234-9 ni le préavis. Les exonérations d'IR, de CSG et de CRDS, l'incessibilité et l'insaisissabilité du CEJ prévues par L. 5131-6 restent intactes ; les cumuls favorables des autres ressources de R. 5131-20, II, et de R. 5131-24 ne sont pas restreints par ce maintien. Aucune taxe correspondante n'est supprimée ici.")

add('R5131-24', previous('R5131-24'),
    "Suppression de fond maintenue : le salaire des cinq catégories d'emplois d'insertion/CUI du 6° ne déclenche plus à lui seul une suspension intégrale du CEJ ; il suit la dégressivité ordinaire des revenus d'activité. La seconde passe conserve les coordinations RSA, prime d'activité et cinq prestations de volontariat, qui organisent des soutiens distincts plutôt que des démarches doublonnées. Leurs exceptions favorables restent intégrales. Aucun nouveau taux ni cumul intégral universel n'est créé.",
    "R. 5131-20, R. 5131-22, D. 5131-23 et L. 5131-6 lus : seuil existant de 300 euros et coefficient égal au forfait de D. 5131-19 divisé par la différence entre 80 % du SMIC mensuel brut et 300 euros, sans changer ces paramètres dans cet article. Les renvois nouveaux à R. 5131-22, 1°, et R. 5131-20, I, 2°, ne figurent pas parmi les cibles jointes ; ils ont été lus en entier dans le corpus. Le renvoi aux emplois de L. 5132-5/11-1/15-1 et L. 5132-6 demeure une identification du salaire, non une autorisation de nouveau CDD ou une limite de durée d'emploi. L. 5134-19-3 est le renvoi CUI déjà présent ; aucun contenu non fourni n'est inventé. Le III, 1° à 5°, concerne des régimes de volontariat et non la rupture privée ; les références extérieures sont conservées, pas déclarées réécrites. Les cumuls des personnes à charge et de la prime pour activité antérieure restent ouverts aux situations futures. Coordonner les circuits de paiement et R. 5131-25, hors lot, sans nouveau justificatif. Les années 2019 à 2025 identifient une loi et le 1er mars 2022 la note historique, sans échéance nouvelle.",
    impact('material_reduction',
        "La source entière excluait le CEJ pendant la perception de ces salaires d'insertion. La proposition retire cette exclusion et applique les règles ordinaires de ressources salariées. Elle n'enlève pas toute prise en compte du revenu et n'abolit pas les autres non-cumuls.",
        "Le droit reste limité à la durée et aux conditions du CEJ ; la réforme n'ouvre pas de rappel général pour les périodes antérieures, sans éteindre les créances déjà nées. Le coût public de l'ouverture du cumul dégressif n'est pas établi.",
        "Aucune charge nouvelle n'est identifiée : les salaires sont traités par le calcul ordinaire déjà existant, sans nouvelle demande de cumul, agrément, attestation ou collecte distincte ajoutée par cet article.",
        [effect('relief_extended', 'cej-cumul-degressif-salaires-insertion',
            "Fin de la suspension automatique du CEJ fondée sur la seule catégorie du salaire d'insertion.",
            "Salaires du III, 6° : non-cumul et suspension de l'allocation pendant leur perception.",
            "Ces salaires relèvent du cumul ordinaire des revenus d'activité : franchise existante puis dégressivité, sous les autres conditions du CEJ.", 'regime',
            "Jeunes éligibles au CEJ employés en insertion ou en contrat unique d'insertion, anciens et futurs contrats.",
            "Ressources à compter de l'entrée en vigueur ; périodes antérieures à leur régime ; pas de droit au-delà de la fin du CEJ.",
            "Réemploi du calcul de ressources existant ; aucune démarche distincte de remplacement.",
            "6° La rémunération perçue dans le cadre d'un contrat à durée déterminée conclu en application des dispositions des articles L. 5132-5, L. 5132-11-1 et L. 5132-15-1 du présent code, d'un contrat de mission mentionné à l'article L. 5132-6 ou d'un contrat unique d'insertion mentionné à l'article L. 5134-19-3.",
            "Elles ne justifient plus, à elles seules, la suspension automatique de l'allocation, que l'emploi relève d'un ancien contrat ou du nouveau contrat unique à durée indéterminée.")]),
    removed=["Le non-cumul et la suspension automatique du CEJ attachés aux rémunérations des emplois d'insertion et du contrat unique d'insertion énumérés au III, 6°."])

add('R5132-7', previous('R5132-7'),
    "Coordination du contrat unique : la référence au CDD ne ferme plus l'aide aux futurs emplois d'insertion à durée indéterminée. Le bénéfice n'est pas réservé aux anciens contrats. Après seconde passe, les postes conventionnés et les trois critères de modulation restent nécessaires au ciblage et à la bonne utilisation de l'aide ; supprimer la part modulée pourrait supprimer un avantage. Aucun taux, prélèvement, déclaration ou autorisation distincte n'est créé ici. La mesure de contrat unique n'est pas comptée une seconde fois comme une baisse de prélèvement.",
    "L. 5132-1/2/3 et les deux versions de R. 5132-8 ont été lus ; L. 5132-5 fourni distingue les périodes d'accompagnement de quatre et vingt-quatre mois et leurs prolongations de la durée indéterminée de l'emploi. La période d'aide reste soumise à ses conditions, sans promesse d'aide pendant toute la vie du contrat. Les trois critères de modulation annuelle et le contingent de postes sont conservés, de même que l'emploi pénitentiaire distinct. La revalorisation et le prorata de R. 5132-8 sont coordonnés dans ce lot. Les V et VI de l'article 2 du décret 2021-1128 sont signalés par la note source ; leur texte extérieur non joint n'est pas déclaré vérifié ni réécrit. Les arrêtés de montants et de versement restent à coordonner, sans nouveau conventionnement au seul changement de support.",
    impact('coordination_only',
        "La source entière limitait le support salarial de l'aide au CDD ; la proposition en maintient le bénéfice pour les nouvelles embauches sous contrat unique et pour les anciens CDD, sans changer le montant socle, la modulation ou le nombre de postes. C'est une coordination de la même mesure d'emploi et d'aides.",
        "Ni le montant ministériel ni la durée d'éligibilité au parcours ne sont élargis automatiquement. Le régime pénitentiaire et les conditions extérieures de versement restent distincts et le coût des aides n'est pas chiffré.",
        "Aucune charge nouvelle n'est identifiée : les conventions en cours servent sans redépôt imposé du seul fait du contrat unique ; l'éligibilité, les critères et les postes étaient déjà nécessaires à l'aide.",
        [effect('coordination', 'contrat-unique-aides-insertion',
            "Coordination de l'aide au poste avec le contrat unique, en préservant les futurs bénéficiaires.",
            "Embauche des personnes de L. 5132-1 en CDD ou emploi pénitentiaire, dans la limite des postes conventionnés.",
            "Embauche éligible en contrat unique, maintien des anciens CDD et de la branche pénitentiaire, mêmes limites et modulation.", 'regime',
            "Entreprises d'insertion et personnes éligibles à leur aide au poste.",
            "Nouveaux emplois privés à compter de la réforme ; aides et conventions anciennes conservées, sans aide viagère déduite du CDI.",
            "Aucun nouveau conventionnement au seul motif du CDI ; pas de taxe ou de taux ajouté.",
            "L'embauche des personnes mentionnées à l'article L. 5132-1 en contrat à durée déterminée",
            "la durée indéterminée de l'emploi ne peut, à elle seule, exclure l'aide ou en réduire le montant.")]))

add('R5132-8', previous('R5132-8'),
    "Coordination de fond, sans nouvelle coupe autonome : les paramètres de l'aide salariale sont utilisables pour les futurs contrats uniques sans attendre un nouvel arrêté. Le temps plein et le prorata mesurent les postes financés ; les compétences ministérielles fixent des montants qui ne sont pas dans cet article. La revalorisation annuelle liée au SMIC est un avantage à conserver et ne peut être transformée par inférence en une formule d'indexation différente. Les deux branches salariale et pénitentiaire restent séparées.",
    "Concordance avec R. 5132-7 dans le lot et lecture de sa source entière. Temps plein, réduction proportionnelle, montant socle, maximum de part modulée exprimé en pourcentage du socle et compétence conjointe emploi/budget sont maintenus. Aucun pourcentage ni formule de revalorisation n'est inventé. Le 1er janvier 2015 est l'origine historique de la revalorisation ; il n'est ni une date de promulgation ni une rétroactivité nouvelle. La note aux V et VI du décret 2021-1128 est conservée comme réserve d'application extérieure non fournie. Les anciens arrêtés servent aux emplois futurs de même objet ; leur coordination reste à effectuer sans fermeture transitoire des aides. La durée de l'aide ne vaut pas terme d'emploi ni ancienneté remise à zéro.",
    impact('coordination_only',
        "Par rapport à la source complète, les montants, leur prorata, leurs deux branches et la revalorisation demeurent ; la restriction terminologique aux CDD est coordonnée avec les contrats uniques futurs. Aucune baisse supplémentaire d'impôt, de montant ou de délai n'est démontrée.",
        "Le contenu des arrêtés de montants et le décret extérieur d'application ne sont pas réécrits ici. Le CDI ne garantit pas une aide pour toute la relation d'emploi.",
        "Aucune charge nouvelle n'est identifiée : la proposition évite de nouveaux arrêtés ou conventions préalables à la continuité du versement et n'ajoute aucun justificatif, taux ou déclaration.",
        [effect('coordination', 'contrat-unique-aides-insertion',
            "Maintien des paramètres et revalorisations pour les emplois devenus à durée indéterminée.",
            "Arrêté distinctement applicable aux salariés d'insertion en CDD et aux personnes détenues ; prorata et revalorisation annuelle.",
            "Branche salariale applicable aux nouveaux contrats uniques et anciens CDD, sans interruption ; branche pénitentiaire, prorata et revalorisation conservés.", 'regime',
            "Entreprises d'insertion et personnes éligibles aux postes aidés.",
            "Embauches futures à compter de la réforme, avec continuité des conventions et arrêtés existants ; droits antérieurs préservés.",
            "Aucun nouveau dépôt et aucune formule de taux nouvelle ; maintien des conditions propres de l'aide.",
            "respectivement pour les salariés en insertion recrutés sous contrat de travail à durée déterminée",
            "s'appliquent aux nouveaux contrats uniques de même objet, sans exclusion ni réduction tenant à leur durée indéterminée.")]))

add('D5132-10-1', previous('D5132-10-1'),
    "Abrogation de fond conservée après seconde passe : suppression entière de l'inscription préalable des immersions dans la convention générale et de ses quatre rubriques. L. 5135-4 et D. 5135-2 encadrent déjà chaque immersion, son objet, ses tâches et son accueil ; la prescription et l'accord patronal demeurent. Aucun volet autonome de l'article source ne reste à supprimer. Les droits et engagements d'accompagnement ne sont pas effacés et l'accès futur sous contrat unique reste possible.",
    "L. 5135-1 à L. 5135-7, D. 5135-2/3/4 et D. 5132-10-2/4 lus intégralement dans le corpus ; L. 5135-7 est également fourni comme cible. Les renvois nouveaux de l'abrogation aux articles L. 5135-1 à L. 5135-7 et D. 5132-10-2 réservent le régime autonome ; les autres articles ne sont pas fournis parmi les cibles. L. 5135-5 conserve les règles de durée et de financement de l'organisme ; L. 5135-6 conserve les durées de présence, nuit, repos, jours fériés, santé et sécurité. Statut, indemnisation et retour au poste restent protégés ; la convention ne peut pourvoir un emploi permanent, saisonnier, temporairement accru ou remplacer un salarié. D. 5132-10-2 vise la sous-section, dont les dispositions abrogées ne devront plus être rétablies par formulaire. D. 5132-10-4, hors lot, impose encore une copie à l'ASP et n'est pas prétendu supprimé. L. 5132-5 maintient l'accès aux immersions sans en faire un terme de contrat unique.",
    impact('material_reduction',
        "L'ensemble de la norme source est retiré : plus d'habilitation préalable ni de quatre mentions d'immersion dans la convention générale d'insertion. Le dispositif individuel déjà existant reste applicable et n'est pas une formalité créée en remplacement. L'abrogation était déjà acquise dans le brouillon.",
        "La prescription, la convention individuelle, l'accord de l'employeur et la transmission autonome à l'ASP ne sont pas abrogés. Aucun total d'heures administratives économisées n'est calculé.",
        "Aucune charge nouvelle n'est identifiée : aucune déclaration, attestation ou autorisation de remplacement ; les protections et conventions individuelles réservées existaient déjà dans le corpus.",
        [effect('obligation_removed', 'immersion-fin-cadrage-convention-generale',
            "Fin du cadrage préalable des immersions et des quatre mentions dans la convention générale d'insertion.",
            "Possibilité prévue dans la convention générale, avec prévisions de salariés, structures d'accueil, accompagnement et objets des immersions.",
            "Aucune prévision ni ces mentions requises dans la convention générale ; régime individuel d'immersion maintenu.", 'legal_duty',
            "Entreprises d'insertion organisant des PMSMP pour leurs salariés éligibles.",
            "Organisation après l'entrée en vigueur ; clauses purement reproductives sans nouvelle formalité future, engagements autonomes et droits antérieurs conservés.",
            "Prescription et convention individuelle préexistantes maintenues ; aucun avenant ou dépôt substitutif.",
            "La convention mentionnée à l'article L. 5132-2 peut prévoir la possibilité pour l'entreprise d'insertion signataire de mettre en place des périodes de mise en situation en milieu professionnel",
            "l'organisation de périodes de mise en situation en milieu professionnel par l'entreprise d'insertion n'est plus subordonnée à leur prévision dans la convention mentionnée à l'article L. 5132-2")]),
    repeal_scope="Suppression entière du cadrage préalable des PMSMP dans la convention générale d'insertion, de ses quatre mentions et de toute formalité future sur ce seul fondement ; droits antérieurs et régime individuel autonome préservés.")

add('D5132-10-3', previous('D5132-10-3'),
    "Abrogation effective maintenue : le plafond cumulé de 25 % de la durée totale du contrat disparaît, sans plafond fictif de parcours ou d'aide substitué au contrat indéterminé. La seconde passe ne peut davantage réduire cet article, qui ne contient aucune autre règle. Les durées individuelles et la prohibition de remplacer un emploi par une immersion assurent la protection maintenue sans reconduire le ratio.",
    "D. 5135-3 lu en entier : convention d'un mois de date à date au maximum, renouvellement unique si objectifs non atteints, au plus deux conventions d'objets ou objectifs différents dans la même structure en douze mois, total de soixante jours renouvellements compris. L. 5135-3 et L. 5135-7 ainsi que D. 5132-10-2 lus pour statut, retour au poste, prescription et accord de l'employeur. Les renvois nouveaux à D. 5135-3 et à L. 5135-7 explicitent ces protections ; le premier n'est pas fourni dans reference-targets mais sa source entière a été lue dans le corpus. La suppression concerne périodes nouvelles et exécution future des périodes en cours, sans effacement des effets antérieurs. Le renvoi à la durée du contrat de L. 5132-5 n'est pas remplacé par la durée de l'accompagnement ; les formulaires doivent être coordonnés.",
    impact('material_reduction',
        "Par rapport à l'unique règle de la source entière, le plafond global de 25 % des immersions rapporté à la durée du contrat est entièrement supprimé, pour l'avenir et la partie future des périodes en cours. Les plafonds individuels ne sont pas supprimés.",
        "Ce n'est pas une suppression de la durée maximale propre à chaque immersion, des soixante jours ni de la protection contre le travail de substitution ; les effets antérieurs restent soumis à leurs règles.",
        "Aucune charge nouvelle n'est identifiée : aucun ratio de parcours, agrément ou suivi de durée présumée du CDI ne remplace le plafond ; les conditions individuelles étaient déjà applicables.",
        [effect('obligation_removed', 'immersion-fin-plafond-global-25',
            "Suppression du calcul et du respect du plafond global de 25 % de la durée totale du contrat.",
            "Immersions cumulées limitées à 25 % de la durée totale du contrat de L. 5132-5.",
            "Aucun plafond global rapporté au contrat, à une mission, au parcours ou à l'aide ; limites individuelles maintenues.", 'percent',
            "Salariés en insertion et entreprises d'insertion organisant leurs PMSMP.",
            "Périodes commençant après l'entrée en vigueur et fraction future des périodes en cours ; droits et créances antérieurs réservés.",
            "Aucun plafond ou autorisation substitutif ; les règles individuelles préexistantes demeurent.",
            "La durée cumulée de l'ensemble des périodes de mise en situation en milieu professionnel effectuées au cours du contrat conclu en application de l'article L. 5132-5 ne peut représenter plus de 25 % de la durée totale du contrat.",
            "Le plafond fixant la durée cumulée des périodes de mise en situation en milieu professionnel à 25 % de la durée totale du contrat d'insertion cesse de s'appliquer")]),
    repeal_scope="Suppression complète du plafond cumulé de 25 % rapporté à la durée totale du contrat d'insertion, sans plafond de remplacement ; limites individuelles des immersions, droits et effets antérieurs préservés.")

TEXT_10_7 = paras(
    "La convention conclue avec une entreprise de travail temporaire d'insertion comporte :",
    "1° Une présentation du projet d'insertion de la structure précisant :",
    "a) Les caractéristiques générales de la structure ;",
    "b) Les principales caractéristiques des personnes en difficulté embauchées ;",
    "c) Les modalités d'accompagnement des salariés en insertion et de collaboration avec l'opérateur France Travail et avec les organismes chargés de leur insertion sociale et professionnelle. La structure peut faire état d'un label délivré par un tiers certificateur attestant de la qualité de son projet ; aucun label n'est exigé au titre du présent article ;",
    "d) Abrogé ;",
    "e) Abrogé ;",
    "f) Abrogé ;",
    "g) Le cas échéant, le champ territorial d'intervention de l'entreprise lorsque celui-ci dépasse le ressort départemental ;",
    "2° Les moyens en personnel, matériels et financiers mobilisés pour mettre en œuvre le projet d'insertion de la structure ;",
    "3° Le nombre de postes d'insertion ouvrant droit à l'aide financière prévue à l'article R. 5132-10-12 ;",
    "4° Les engagements d'insertion de la structure et les indicateurs rendant compte des actions et des résultats ;",
    "5° Abrogé ;",
    "6° La nature et le montant des autres aides publiques directes ou privées dont la structure a bénéficié les années antérieures, uniquement dans la mesure où ces informations sont nécessaires au contrôle des règles de cumul ou des plafonds d'aide applicables ;",
    "7° Les modalités de suivi, de contrôle et d'évaluation de la convention.",
    "Les informations et pièces exactes et à jour déjà légalement détenues par l'autorité de conventionnement sont réutilisées sans nouvelle production par la structure. Aucune déclaration, autorisation, certification ou pièce équivalente ne remplace les mentions supprimées aux d), e) et f) du 1° et au 5°. Les moyens prévus au 2° ne sont pas soumis à une justification distincte de capacité à accomplir les tâches administratives ou comptables. Les obligations comptables légalement autonomes demeurent applicables.",
    "Ces simplifications s'appliquent dès l'entrée en vigueur de la loi les prévoyant aux conventions nouvelles et aux procédures en cours, sans nouveau dépôt ni reprise des délais. Les conventions déjà conclues restent valables ; leurs clauses qui imposent seulement les formalités supprimées cessent de les imposer pour l'avenir, sans affecter les engagements autonomes, les aides accordées ni les créances antérieures. La condition d'activité exclusive et l'obligation d'y affecter l'intégralité des moyens humains et matériels ne peuvent être maintenues par la convention sur le fondement du f) abrogé ; les aides restent affectées aux personnes et actions éligibles conformément à l'article L. 5132-6. Les emplois de droit privé conclus après l'entrée en vigueur du contrat unique sont à durée indéterminée ; la durée de la convention, de l'aide ou d'une mission ne met pas fin à ces emplois.")

add('R5132-10-7', TEXT_10_7,
    "Coupes de fond du précédent brouillon conservées : suppression des mentions d'autre convention, de l'adéquation à l'offre locale et du dépôt des offres ; historique des aides limité aux informations nécessaires et réemploi des pièces détenues. Coupes supplémentaires : retrait du f) relatif à l'activité exclusive, devenu contraire à L. 5132-6 proposé, et de la justification distincte des moyens administratifs/comptables du 2°. Le projet d'insertion, ses moyens effectifs, le nombre de postes, les engagements, les indicateurs et les contrôles suffisent à rendre l'aide contrôlable. Le label reste facultatif. La limitation du 6° est rectifiée pour préserver aussi le contrôle des plafonds d'aide, qui peut porter sur des dépenses différentes : la version antérieure ne réservait que les mêmes postes ou dépenses. Aucun plafond supérieur n'est implicitement effacé.",
    "L. 5132-6 fourni supprime expressément l'activité exclusive et l'affectation de l'intégralité des moyens : le maintien du f) par le brouillon était incohérent. R. 5132-10-8/9/13/14 lus intégralement : viabilité, comptes annuels, bilan, contrôle d'exécution et non-cumul des aides d'État au même poste restent autonomes. La suppression du détail des moyens pour tâches administratives/comptables ne supprime ni les moyens d'insertion ni les comptes. Les 1° a), b), c), g), 2°, 3°, 4°, 6° et 7° sont conservés ; d), e), f) et 5° restent à leur emplacement comme abrogés. La liste n'est plus ouverte par « notamment ». Le 6° couvre les aides antérieures utiles aux règles de cumul et plafonds, y compris lorsqu'un plafond s'apprécie à un autre niveau que le poste ; il n'invente pas de collecte des aides actuelles et ne supprime aucune contrainte européenne applicable. Pièces et informations seulement si légalement détenues, exactes et à jour. R. 5132-10-12 est coordonné dans ce lot ; sa vue fournie demeure distincte du présent texte final. La note au 1er juillet 2024 est historique. Formulaires et modèles restent à adapter, sans les déclarer réécrits.",
    impact('material_reduction',
        "La comparaison avec la source entière retire des mentions conventionnelles, l'ouverture illimitée de la liste, l'historique sans pertinence juridique et les productions répétées. Elle retire en plus le f) et le détail de capacité administrative encore présents au brouillon. La suppression d'activité exclusive est une coordination de la mesure législative, pas une nouvelle réduction comptée deux fois.",
        "Les moyens d'insertion, l'affectation des aides, les comptes, les plafonds d'aide applicables et les contrôles autonomes demeurent. Aucun coût global, nombre de pièces effectivement détenues ou solde national de complexité n'est établi.",
        "Aucune charge nouvelle par rapport à la source n'est identifiée : les aides antérieures exigibles sont un sous-ensemble de l'historique existant ; ni activité exclusive, ni attestation, ni label obligatoire, ni déclaration équivalente ne remplacent les mentions retirées.",
        [effect('obligation_removed', 'etti-convention-mentions-supprimees',
            "Retrait des mentions obligatoires d'autre convention, d'adéquation à l'offre locale et du circuit de dépôt des offres ; mention du label détenu rendue facultative et liste fermée au titre de cet article. Ces volets constituent un seul allègement des mentions conventionnelles.",
            "Le c) impose la mention du label détenu le cas échéant ; le 1° d) et e) et le 5° imposent trois autres mentions dans une liste ouverte par « notamment ».",
            "Label utilisable volontairement comme preuve favorable ; d), e) et 5° abrogés ; liste fermée au titre de cet article, accompagnement, collaboration et contrôles autonomes conservés.", 'legal_duty',
            "Entreprises de travail temporaire d'insertion et autorités de conventionnement.",
            "Conventions nouvelles, procédures en cours et formalités futures des conventions conclues dès l'entrée en vigueur ; engagements autonomes et créances préservés.",
            "Aucune déclaration, attestation de non-détention, certification ou autorisation de remplacement ; le label favorable reste utilisable.",
            plain(BY_NUMBER['R5132-10-7']['source_xml']).strip(),
            plain(TEXT_10_7).strip()),
         effect('coordination', 'insertion-fin-activite-exclusive',
            "Suppression du f) pour ne pas rétablir par convention l'exclusivité déjà supprimée dans L. 5132-6 proposé.",
            "Le f) exige les modalités de respect de l'activité exclusive et l'intégralité des moyens humains et matériels.",
            "Le f) est abrogé ; affectation des aides à l'insertion et moyens nécessaires conservés, sans exclusivité conventionnelle sur ce fondement.", 'legal_duty',
            "Entreprises de travail temporaire d'insertion.",
            "À coordonner avec l'entrée en vigueur de L. 5132-6 proposé ; conventions et formalités futures visées.",
            "Pas de déclaration de répartition des activités substitutive ; contrôle des moyens et de l'aide préexistant maintenu.",
            "f) Les modalités selon lesquelles la condition d'activité exclusive définie à l'article L. 5132-6 est respectée, notamment l'intégralité des moyens humains et matériels ;",
            "La condition d'activité exclusive et l'obligation d'y affecter l'intégralité des moyens humains et matériels ne peuvent être maintenues par la convention sur le fondement du f) abrogé"),
         effect('compliance_cost_reduced', 'etti-convention-justificatifs-proportionnes',
            "Réduction des demandes d'historique d'aides et retrait du détail administratif/comptable, sans nouvelle production des pièces détenues.",
            "Historique général des aides publiques directes ou privées des années antérieures, plus présentation des moyens pour accomplir les tâches administratives et comptables.",
            "Historique limité aux données utiles aux cumuls ou plafonds ; seuls moyens du projet exigés, pièces exactes déjà détenues réutilisées.", 'legal_duty',
            "Entreprises de travail temporaire d'insertion lors du conventionnement et de son exécution.",
            "Entrée en vigueur, procédures en cours sans redépôt, obligations futures des anciennes conventions également allégées.",
            "Pas d'autorisation substitutive ; comptabilité et contrôles autonomes demeurent ; économie monétaire non chiffrée.",
            "6° La nature et le montant des autres aides publiques directes ou privées dont la structure a bénéficié les années antérieures ;",
            "6° La nature et le montant des autres aides publiques directes ou privées dont la structure a bénéficié les années antérieures, uniquement dans la mesure où ces informations sont nécessaires au contrôle des règles de cumul ou des plafonds d'aide applicables ;")]),
    removed=[
        "La mention systématique du label détenu au 1° c) devient une faculté de preuve favorable, sans retirer le label ni imposer une certification de remplacement.",
        "La mention obligatoire de l'autre convention d'insertion au 1° d), déjà susceptible d'être connue de l'autorité de conventionnement.",
        "La justification conventionnelle de l'adéquation du projet à l'offre locale existante, prévue au 1° e), sans supprimer les critères légaux autonomes d'aide.",
        "Les modalités de justification de l'activité exclusive et de l'affectation de l'intégralité des moyens prévues au 1° f), en coordination avec L. 5132-6 proposé.",
        "Le détail des moyens affectés aux tâches administratives et obligations comptables du 2°, sans retirer la comptabilité autonome ni les moyens du projet d'insertion.",
        "La mention conventionnelle des modalités de dépôt des offres d'emploi auprès de France Travail exigée au 5°.",
        "L'historique général indifférencié des aides antérieures au 6°, pour les données inutiles au contrôle des cumuls et plafonds applicables.",
        "La nouvelle production des pièces exactes et à jour déjà légalement détenues, et le caractère ouvert de la liste par le mot « notamment »."])

TEXT_10_12 = previous('R5132-10-12').replace(
    "L'aide particulière prévue à l'article R. 5132-10-13-1 demeure ouverte aux personnes qui remplissent ses conditions, y compris pour les situations futures. Lorsqu'un même poste et une même période sont éligibles aux deux dispositifs, l'entreprise peut demander le dispositif le plus favorable, sans cumul des deux aides pour ce poste et cette période.",
    "L'aide particulière prévue à l'article R. 5132-10-13-1 demeure ouverte aux personnes définies à l'article D. 5132-10-15 qui remplissent ses autres conditions, y compris pour les situations futures. Lorsqu'un même poste et une même période sont éligibles aux deux dispositifs, l'entreprise peut demander le dispositif le plus favorable. Les interdictions de cumul prévues à l'article R. 5132-10-14 demeurent applicables.")

add('R5132-10-12', TEXT_10_12,
    "Coordination de fond du support contractuel de l'aide ordinaire, en conservant le socle, la modulation et ses trois critères. Le choix favorable entre aide ordinaire et aide d'inclusion du brouillon est maintenu, sans double financement. Rectification du renvoi : D. 5132-10-15 définit désormais de façon autonome les bénéficiaires de l'inclusion, car L. 5132-6-1 est proposé à l'abrogation ; l'aide reste ouverte aux futurs bénéficiaires. Aucun retrait supplémentaire de critère ou de part d'aide ne se justifie sans diminuer l'avantage ou affaiblir le contrôle des fonds.",
    "L. 5132-6 et L. 5132-6-1 fournis distinguent emploi indéterminé, missions et abrogation prospective de la dérogation d'inclusion. R. 5132-10-13/13-1/13-2/14 lus en entier : temps plein et prorata, socle et modulation ; inclusion à 100 % du socle la première année puis 70 %, sous ses autres conditions ; versement ASP et non-cumul d'une autre aide d'État au même poste. La proposition ne change aucun de ces paramètres. Les renvois nouveaux à R. 5132-10-13-1 et R. 5132-10-14, absents des cibles, ont été lus dans le corpus ; D. 5132-10-15 est une cible jointe dont la proposition antérieure est rectifiée dans ce lot. Coordonner R. 5132-10-13-1 pour remplacer son renvoi aux personnes de L. 5132-6-1 par le fondement autonome, ainsi que les arrêtés de versement, sans fermeture dans l'attente. La garantie mensuelle et l'ancienneté des intermissions de L. 1251-58-2/3 restent applicables selon L. 5132-6 proposé. Ni aide pendant toute la vie du CDI ni double aide ne sont promises.",
    impact('coordination_only',
        "La source complète réservait l'aide ordinaire à l'embauche en contrat de mission. La proposition la coordonne avec le contrat unique, maintient ses paramètres et évite que l'abrogation de L. 5132-6-1 ferme l'aide d'inclusion. Le choix le plus favorable n'ouvre aucun cumul et n'est pas compté comme une autre suppression de charge.",
        "Le montant et la durée d'aide restent soumis aux autres conditions, aux postes conventionnés et aux arrêtés. Le renvoi de R. 5132-10-13-1 doit encore être coordonné hors lot ; aucun rendement ou coût global n'est établi.",
        "Aucune charge nouvelle n'est identifiée : aucun nouveau conventionnement au seul changement de contrat, pas de dossier ou choix obligatoire imposé ; les interdictions préexistantes de cumul demeurent.",
        [effect('coordination', 'contrat-unique-aides-insertion',
            "Maintien de l'aide ordinaire et de l'accès favorable à l'inclusion sous le contrat unique.",
            "Aide ordinaire sur embauche en contrat de mission, dans la limite des postes conventionnés, avec socle et part modulée.",
            "Même aide sur contrat unique, maintien des anciens contrats et de l'aide d'inclusion selon son fondement autonome, choix favorable sans cumul.", 'regime',
            "Entreprises de travail temporaire d'insertion et personnes éligibles, dont les futurs bénéficiaires de l'inclusion.",
            "Nouvelles embauches privées à compter de la réforme ; anciennes aides et conventions préservées ; pas de renouvellement d'un emploi à terme.",
            "Conventions utilisables sans nouvel agrément ; garanties intérimaires et non-cumul existants maintenus.",
            "L'embauche des personnes mentionnées à l'article L. 5132-1 en contrat de mission",
            "La durée indéterminée du nouvel emploi ne peut, à elle seule, exclure l'aide ou en réduire le montant.")]))

TEXT_10_15 = paras(
    "Pour l'accès au régime d'inclusion et aux aides prévues aux articles R. 5132-10-13-1 et R. 5132-10-13-2, sont éligibles les personnes âgées d'au moins cinquante-sept ans qui rencontrent des difficultés sociales et professionnelles particulières. Elles peuvent bénéficier de ce régime dès le début de leur parcours d'insertion par l'activité économique, dans le cadre de l'emploi à durée indéterminée prévu à l'article L. 5132-6 et dans les conditions de l'article L. 1251-58-1. L'âge prévu au présent alinéa délimite ce régime favorable ; il ne subordonne pas l'accès des autres personnes éligibles à l'emploi d'insertion à durée indéterminée.",
    "L'éligibilité au parcours d'insertion reste appréciée dans les conditions de l'article L. 5132-3. Aucun contrat à durée déterminée préalable, examen distinct avant l'accès au régime d'inclusion, bilan spécifique ni justificatif de remplacement n'est exigé au titre du présent article. L'absence d'actions d'accompagnement ou de formation antérieures au début du parcours ne fait pas obstacle à cet accès. Les actions d'accompagnement et de formation restent adaptées aux besoins du bénéficiaire.",
    "La suppression de l'attente minimale de douze mois, du préalable d'un CDD et de l'examen distinct s'applique dès l'entrée en vigueur de la loi la prévoyant, y compris aux personnes dont le parcours a commencé avant cette date. Les aides et garanties du régime d'inclusion restent ouvertes aux futures personnes éligibles selon leurs autres conditions ; l'abrogation de l'article L. 5132-6-1 ne peut à elle seule en fermer le bénéfice. Les contrats d'inclusion déjà conclus, leurs aides, les droits acquis et l'ancienneté sont préservés. La suppression des conditions n'ouvre pas de droit à un versement rétroactif pour les périodes antérieures ; les créances déjà nées et les voies de recours restent applicables. Une conversion convenue conserve toute l'ancienneté et les créances acquises, sans double compte. Les nouveaux emplois de droit privé relèvent du contrat unique à durée indéterminée ; ni la durée d'une mission ni celle de l'accompagnement ou de l'aide ne met fin à l'emploi. Le présent article n'autorise ni nouveau CDD ni renouvellement d'un ancien CDD après l'entrée en vigueur du contrat unique.")

add('D5132-10-15', TEXT_10_15,
    "Coupes de fond maintenues : suppression des douze mois d'attente et du CDD préalable. Coupe supplémentaire : suppression de l'examen individuel distinct avant l'inclusion, doublonnant l'appréciation d'éligibilité au parcours de L. 5132-3 ; aucun bilan ni justificatif ne le remplace. Le renvoi actif à L. 5132-6-1, proposé à l'abrogation, est remplacé par un fondement autonome pour le régime favorable d'inclusion et ses aides. Le seuil de cinquante-sept ans et les difficultés particulières délimitent cet avantage, non le droit commun d'embauche désormais indéterminée. Les garanties d'accompagnement restent nécessaires et ne sont pas supprimées.",
    "L. 5132-6-1 fourni abroge la dérogation tout en préservant les aides futures et retire le plafond de trente-six mois pour les missions futures ; le précédent brouillon se référait encore à ce fondement et à son ancien plafond. L. 5132-6 fourni ouvre l'emploi indéterminé sans exclusivité et conserve garantie mensuelle/intermissions ; ces points ne sont pas rétablis à rebours. Le présent article donne un fondement autonome à la catégorie favorable de personnes d'au moins 57 ans rencontrant les difficultés particulières de L. 5132-6-1 officiel, sans ajouter une condition de preuve. Renvois nouveaux à L. 5132-6 et L. 1251-58-1 : cibles fournies ; L. 5132-3 et R. 5132-10-13-1/2, non fournis comme cibles, lus intégralement dans le corpus. Coordonner le renvoi de R. 5132-10-13-1 à L. 5132-6-1, les modèles et arrêtés, sans retarder l'accès futur. Les taux d'aide de 100 % du socle la première année et de 70 % ensuite et le prorata de poste restent à leur champ ; aucune nouvelle date de départ de l'aide ni rétroactivité générale n'est inventée. La suppression de l'examen distinct ne supprime pas l'appréciation d'éligibilité, l'accompagnement ou les contrôles préexistants de L. 5132-3.",
    impact('material_reduction',
        "Par rapport à la source entière, sont retirés le délai minimal de douze mois, le passage préalable par un CDD et l'examen distinct de la situation avant l'inclusion. Ce dernier retrait va au-delà du brouillon. La définition autonome maintient le régime favorable malgré l'abrogation législative proposée.",
        "Le seuil de 57 ans pour le régime favorable, les difficultés particulières et l'éligibilité au parcours demeurent ; ils ne limitent pas l'embauche ordinaire. Les paramètres financiers et le coût public ne sont pas modifiés ni chiffrés ; les textes de versement restent à coordonner.",
        "Aucune charge nouvelle n'est identifiée par rapport à la source : l'examen de parcours préexistait dans L. 5132-3, le bilan distinct disparaît et aucun agrément, formulaire, attestation ou nouveau délai ne le remplace. Le fondement autonome ne durcit pas l'éligibilité légale de la population.",
        [effect('deadline_reduced', 'inclusion-acces-immediat-sans-cdd',
            "Accès au régime favorable dès le début du parcours, sans douze mois d'attente ni emploi à terme préalable.",
            "Personnes d'au moins 57 ans : attente d'au moins douze mois depuis le début du parcours et référence à un CDD précédent.",
            "Accès dès le début du parcours sous emploi indéterminé ; pas de CDD préalable ni d'attente minimale, sous les autres conditions de l'aide.", 'other',
            "Personnes d'au moins 57 ans rencontrant des difficultés sociales et professionnelles particulières et ETTI les employant.",
            "À compter de l'entrée en vigueur pour parcours nouveaux ou déjà commencés ; anciens contrats et aides préservés, sans rappel général.",
            "Aucune autorisation ou déclaration de remplacement ; l'appréciation d'éligibilité au parcours reste existante.",
            "à l'issue d'un délai minimal de douze mois après le début de leur parcours d'insertion par l'activité économique.",
            "Elles peuvent bénéficier de ce régime dès le début de leur parcours d'insertion par l'activité économique"),
         effect('obligation_removed', 'inclusion-fin-examen-distinct',
            "Suppression de l'examen distinct avant l'inclusion, sans retirer l'appréciation préexistante d'éligibilité au parcours.",
            "Conclusion après examen par l'ETTI de la situation au regard de l'emploi et des actions du CDD précédent.",
            "Aucun examen distinct, bilan spécifique ou justificatif de remplacement au titre de cet article ; appréciation du parcours de L. 5132-3 conservée.", 'legal_duty',
            "ETTI et personnes éligibles au régime favorable d'inclusion.",
            "Entrée en vigueur, y compris parcours en cours ; droits acquis et anciennes aides préservés.",
            "Aucun bilan, agrément ou nouvelle formalité ; l'accompagnement adapté reste applicable.",
            "Ce contrat est conclu après examen par l'entreprise de travail temporaire d'insertion de la situation de la personne au regard de l'emploi et des actions d'accompagnement et de formation effectuées dans le cadre du contrat à durée déterminée précédent conclu en application du premier alinéa de l'article L. 5132-6.",
            "Aucun contrat à durée déterminée préalable, examen distinct avant l'accès au régime d'inclusion, bilan spécifique ni justificatif de remplacement n'est exigé au titre du présent article."),
         effect('coordination', 'inclusion-avantages-fondement-autonome',
            "Fondement autonome des avantages d'inclusion, pour ne pas fermer les situations futures après l'abrogation de L. 5132-6-1.",
            "Accès au contrat d'inclusion défini par L. 5132-6-1, catégorie de personnes renvoyée par l'aide de R. 5132-10-13-1.",
            "Catégorie favorable définie ici ; emplois de L. 5132-6 et garanties de L. 1251-58-1, aides conservées aux autres conditions.", 'regime',
            "Personnes âgées d'au moins 57 ans éligibles à l'inclusion, y compris les futures situations.",
            "Coordination avec l'abrogation prospective de L. 5132-6-1 ; anciennes aides préservées sans fermeture aux nouveaux parcours.",
            "Aucun nouveau seuil d'embauche ou justificatif ; il s'agit du maintien de l'avantage ciblé et de son accès simplifié.",
            "un contrat à durée indéterminée d'inclusion prévu à l'article L. 5132-6-1",
            "Les aides et garanties du régime d'inclusion restent ouvertes aux futures personnes éligibles selon leurs autres conditions ; l'abrogation de l'article L. 5132-6-1 ne peut à elle seule en fermer le bénéfice.")]),
    removed=[
        "Le délai minimal de douze mois après le début du parcours d'insertion pour accéder au régime favorable d'inclusion.",
        "L'exigence d'un précédent contrat à durée déterminée comme support de l'examen et préalable à l'accès au régime d'inclusion.",
        "L'examen distinct préalable par l'entreprise de la situation d'emploi et des actions du CDD précédent, doublonnant l'appréciation d'éligibilité au parcours."])

# Analyses des cibles : chaque contexte est attaché à l'article examiné ; les
# empreintes décrivent les vues livrées, et non les propositions finales du lot.
CONTEXT = {
    'R4625-1': "La garantie médicale et ses dispenses ne constituent pas une règle de rupture.",
    'R4626-12': "La rupture du médecin reste soumise à l'avis conforme et aux consultations protectrices ; le recrutement public n'est pas transformé en relation privée.",
    'R5122-18': "L'indemnité horaire d'activité partielle est un revenu de remplacement pendant la relation d'emploi, pas une indemnité de rupture.",
    'R5131-21': "Les allocations chômage/CSP et revenus de formation sont des ressources du calcul CEJ, pas une indemnité patronale de rupture.",
    'R5131-24': "Le non-cumul ou le cumul dégressif du CEJ porte sur des ressources ; les prestations militaires et civiques restent des régimes distincts.",
    'R5132-7': "Le poste aidé est distinct de la rupture de l'emploi et de la durée d'aide ; le contrat pénitentiaire garde son régime propre.",
    'R5132-8': "Prorata de poste, revalorisation et conditions de versement d'aide ne fixent ni terme ni indemnité de l'emploi ; le régime pénitentiaire reste distinct.",
    'D5132-10-1': "La fin ou l'absence de prévision conventionnelle d'une immersion ne constitue pas la rupture du contrat de travail.",
    'D5132-10-3': "Le retrait du ratio de durée des immersions ne rompt pas l'emploi et ne change pas l'ancienneté acquise.",
    'R5132-10-7': "La fin d'une convention, d'une aide ou d'une mission n'est pas une rupture automatique de l'emploi d'insertion.",
    'R5132-10-12': "L'aide au poste et l'aide d'inclusion sont distinctes de la rémunération garantie, du préavis et de l'indemnité de rupture.",
    'D5132-10-15': "L'accès immédiat au régime favorable d'inclusion n'autorise pas un terme d'emploi ; un parcours antérieur n'est pas effacé par la conversion.",
}

UNIQUE_CONTEXT = {
    'R4625-1': "Les anciens CDD gardent le suivi équivalent ; les nouveaux contrats uniques et les conversions conservent les dispenses aux conditions médicales. La réserve publique ne vise que le champ public initial.",
    'R4626-12': "Les seuls CDD privés encore visés sont ceux déjà conclus ; aucun renouvellement n'est autorisé. Les contrats publics et références éducation/santé ne sont pas rattachés artificiellement à L. 1221-2.",
    'R5122-18': "Apprentissage, professionnalisation et intérim gardent leurs droits propres sous emploi indéterminé ; l'extension du plancher vise aussi les CDI existants, sans réduire garantie mensuelle ou intermissions.",
    'R5131-21': "La liste maintenue ne dépend d'aucun CDD ; la période de formation et le dispositif CSP ne sont pas des emplois à terme. Aucun salaire de contrat unique n'est ajouté à cette liste par analogie.",
    'R5131-24': "La suppression du III, 6°, s'applique aux salaires d'anciens contrats et de futurs contrats uniques, sans que les renvois d'insertion autorisent un nouveau CDD, un terme ou un renouvellement.",
    'R5132-7': "La condition de CDD de la source est remplacée par le contrat unique avec aide ouverte aux futurs emplois éligibles ; ancien CDD, convention et droits restent protégés, sans fin d'emploi à échéance d'aide.",
    'R5132-8': "Les arrêtés de la branche CDD sont rendus applicables aux futurs contrats uniques de même objet, sans interruption de l'aide ni nouveau conventionnement. L'emploi pénitentiaire n'est pas converti.",
    'D5132-10-1': "L'abrogation de la prévision générale n'enlève pas la convention individuelle d'immersion ; l'accès reste ouvert aux anciens contrats et aux futurs contrats uniques sans terme lié à l'immersion.",
    'D5132-10-3': "Le ratio n'est pas calculé sur une durée fictive du CDI, de la mission ou du parcours. Les périodes anciennes et leurs droits sont réservés, sans nouveau terme d'emploi.",
    'R5132-10-7': "La convention ne peut rétablir un CDD par sa durée ou celle d'une mission ; clauses de formalités supprimées cessent pour l'avenir et engagements autonomes antérieurs restent protégés.",
    'R5132-10-12': "L'aide ordinaire suit le nouveau support indéterminé sans nouveau conventionnement ; anciens contrats de mission protégés, mais aucun renouvellement d'emploi à terme après la réforme.",
    'D5132-10-15': "Le régime favorable est défini indépendamment de l'ancienne dérogation CDD/CDI ; ni son âge ni la durée d'aide ne limitent le droit commun d'emploi indéterminé. Pas de nouveau CDD préalable.",
}

SPECIAL = {
 ('R5132-10-12', 'D5132-10-15'): "La source de D. 5132-10-15 réserve l'inclusion aux personnes d'au moins 57 ans après douze mois et un examen lié au CDD précédent. Sa vue proposée retire l'attente et le CDD mais conserve l'examen et un renvoi actif à L. 5132-6-1 proposé à l'abrogation. Le texte final du lot retire aussi l'examen distinct et définit la catégorie favorable de façon autonome ; R. 5132-10-12 s'y rattache pour garder les aides ouvertes aux futurs bénéficiaires sans limiter à 57 ans l'emploi d'insertion ordinaire ni remettre l'ancienneté à zéro.",
 ('R5122-18', 'L1251-58-1'): "L. 1251-58-1 officiel distingue le CDI et ses missions successives, avec contrat de mise à disposition au 1° et lettre de mission au 2°. Sa proposition généralise l'emploi unique, conserve ces actes et l'ancienneté. R. 5122-18 retire expressément l'exclusion du plancher visant ces salariés, pour les heures futures des contrats anciens et nouveaux, sans confondre mission et rupture ni écarter garantie mensuelle/intermissions.",
 ('R5131-21', 'L1233-68'): "Le renvoi conservé au 1° vise les allocations CSP du 8° de L. 1233-68. Les conditions d'ancienneté du 1° et les formalités/délais d'adhésion du 2° sont propres au dispositif, pas celles de L. 1234-1/9. Le 3° proposé transforme les périodes de travail en contrats uniques sans terme d'emploi et le 10° b) retire un financement patronal pour adhésions nouvelles, sans supprimer l'allocation visée ici ni imposer de la déduire comme indemnité de rupture.",
 ('R5131-24', 'L5132-15-1'): "Le III, 6°, officiel vise le salaire des ateliers et chantiers de L. 5132-15-1. Sa proposition distingue les périodes d'accompagnement de quatre/vingt-quatre mois, leurs prolongations et l'emploi indéterminé ; le 1° et le 2° de suspension servent l'immersion ou un essai, avec départ favorable sans préavis dans leur champ. Leur salaire entre ici dans le cumul dégressif ordinaire, anciens contrats et futurs contrats uniques, sans fermeture des aides ni nouveau CDD.",
 ('R5131-24', 'L5132-11-1'): "Le III, 6°, source identifie le salaire des associations intermédiaires de L. 5132-11-1. La proposition de cette cible maintient le parcours et ses prolongations, le minimum spécial de vingt heures et sa dispense favorable, distincts du contrat unique. Le cumul CEJ proposé ne crée aucun terme ni nouveau CDD et ne supprime ni les droits d'anciens contrats ni le départ sans préavis après immersion, action ou essai prévu par la cible.",
 ('R5131-24', 'L5132-5'): "L. 5132-5 est la branche entreprises d'insertion du III, 6°. La proposition cible emploie à durée indéterminée mais garde la durée du parcours et les possibilités de prolongation, les immersions et les départs favorables. La suppression du non-cumul automatique ne remplace aucun délai de parcours ni de notification ; elle applique les règles salariées CEJ aux ressources futures des contrats anciens et nouveaux sans autoriser un CDD.",
 ('R5131-24', 'L5132-6'): "La cible officielle vise des contrats de mission ; sa proposition les sépare de l'emploi indéterminé, supprime exclusivité et plafonds légaux de mission, ouvre les garanties de la section 4 bis et maintient les anciennes missions sous transition. Le renvoi salarial conservé après abrogation du III, 6°, identifie les bénéficiaires du cumul dégressif, non une autorisation d'emploi à terme ni un nouveau minimum hebdomadaire.",
 ('R5132-7', 'R5132-8'): "Le renvoi du deuxième alinéa porte sur le montant et le versement : poste à temps plein, prorata, arrêté conjoint emploi/budget, maximum de modulation et revalorisation annuelle depuis 2015. La vue proposée de R. 5132-8 et le texte de ce lot maintiennent ces avantages pour les futurs contrats uniques et les anciens CDD, sans nouvelle convention ni terme d'emploi lié à la durée d'aide ; branche pénitentiaire distincte.",
 ('R5132-7', 'L5132-5'): "L. 5132-5 proposé distingue emploi indéterminé, parcours initial d'au moins quatre mois, durée de vingt-quatre mois et prolongations favorables. L'aide de R. 5132-7 n'est donc ni réservée aux anciens CDD ni promise pour toute la vie du CDI. Les immersions et possibilités de départ du salarié sans préavis dans le champ spécial restent intactes ; aucune durée d'aide ne termine automatiquement l'emploi.",
 ('D5132-10-1', 'L5135-7'): "L. 5135-7 interdit les immersions pour un poste permanent, un surcroît temporaire, un remplacement ou un emploi saisonnier. Sa proposition autonomise la définition saisonnière au lieu du renvoi à L. 1242-2, sans relâcher l'interdiction. L'abrogation du cadrage dans la convention générale laisse cette protection entière, pour anciens comme nouveaux contrats ; aucune immersion n'est un nouvel emploi à terme ni un essai renouvelé.",
 ('D5132-10-1', 'L5132-5'): "Le deuxième alinéa de L. 5132-5 officiel et proposé autorise la convention d'immersion de L. 5135-4 pendant l'emploi d'insertion. L'abrogation de D. 5132-10-1 retire seulement sa prévision dans la convention générale de L. 5132-2 et les quatre rubriques ; elle ne touche pas cette possibilité, sa convention individuelle ou les départs spéciaux du salarié après immersion/essai. Durée du parcours distincte du CDI et anciens droits réservés.",
 ('D5132-10-3', 'L5135-7'): "La suppression du plafond global de 25 % n'autorise aucune immersion sur un poste permanent, pour un surcroît temporaire, un emploi saisonnier ou un remplacement : L. 5135-7 et sa définition saisonnière autonome proposée demeurent. Les limites individuelles de D. 5135-3 restent également préservées ; l'immersion ne devient ni un CDD, ni une rupture sans notification de l'emploi.",
 ('D5132-10-3', 'L5132-5'): "Le renvoi source portait sur la durée totale du contrat de L. 5132-5. La cible proposée remplace ce contrat par un emploi indéterminé et distingue le parcours d'au moins quatre mois, vingt-quatre mois et prolongations : ces durées ne peuvent servir de dénominateur implicite au ratio abrogé. Les immersions, leur accord patronal et leurs départs spéciaux sans préavis restent possibles ; droits anciens préservés pour leurs effets antérieurs.",
 ('R5132-10-7', 'R5132-10-12'): "Le 3° renvoie seulement au nombre de postes ouvrant l'aide. La vue fournie de R. 5132-10-12 ouvre les contrats uniques et préserve anciens contrats, modulation et inclusion ; le texte final du lot précise le fondement D. 5132-10-15 pour ne pas fermer l'aide future. La convention ne garantit pas un financement pendant toute la vie du CDI ; ses indicateurs et limites de postes restent applicables, sans nouveau conventionnement dû au changement de support.",
 ('R5132-10-7', 'L5132-6'): "Le f) source et le précédent brouillon exigeaient encore activité exclusive et intégralité des moyens. La cible proposée les supprime expressément : f) est donc abrogé, sans déclaration équivalente. Les moyens nécessaires à l'insertion et l'affectation des aides restent contrôlables. Contrat unique, garantie mensuelle, intermissions et absence de terme automatique à la fin d'une mission sont maintenus ; la durée conventionnelle ne rétablit pas une exclusivité supprimée.",
 ('R5132-10-12', 'L5132-6'): "La cible proposée ouvre le contrat unique avec garantie mensuelle et intermissions de la section 4 bis, sans exclusivité ni plafond légal de mission et avec transition pour les anciens contrats de mission. R. 5132-10-12 coordonne le support de l'aide, sans renouvellement d'emploi à terme ni condition de durée indéterminée défavorable ; l'aide n'est pas une rémunération perpétuelle ou une indemnité de rupture.",
 ('R5132-10-12', 'L1251-58-1'): "La cible distingue le contrat d'emploi, devenu unique dans la proposition, de la mise à disposition du 1° et de la lettre de mission du 2°. L'aide ordinaire peut donc suivre les nouveaux emplois sans créer un CDD par la durée des missions ; ancienneté, CDI intérimaires antérieurs et garanties restent préservés. Ce n'est pas une dispense de notification de rupture ni une suppression du préavis individuel.",
 ('R5132-10-12', 'L5132-6-1'): "La proposition cible abroge la dérogation spéciale et le plafond futur de trente-six mois, mais réserve les anciens contrats/missions et maintient expressément les aides futures. Le texte final évite donc de laisser l'aide particulière dépendre uniquement du renvoi ancien de R. 5132-10-13-1 : D. 5132-10-15 définit sa population favorable et les autres conditions financières sont conservées, sans âge minimal général pour l'emploi unique.",
 ('D5132-10-15', 'L5132-6-1'): "La source de cette cible visait les personnes de 57 ans ou plus aux difficultés particulières et des missions de trente-six mois. Sa proposition abroge la dérogation et le plafond pour les nouvelles missions, en préservant les aides futures. Le renvoi actif du brouillon est donc retiré : D. 5132-10-15 définit désormais la catégorie favorable de façon autonome, sans attente de douze mois ni CDD/examen distinct, et ne rétablit pas le plafond futur ou un âge minimal d'embauche.",
 ('D5132-10-15', 'L5132-6'): "La cible proposée permet l'emploi unique sans exclusivité, supprime les plafonds légaux de missions et maintient garantie mensuelle, intermissions, aides et transitions. D. 5132-10-15 s'y rattache pour l'emploi, sans rétablir la durée de trente-six mois ou un CDD préalable. Son âge de 57 ans vise seulement le régime d'inclusion favorable ; les autres personnes éligibles gardent accès au contrat indéterminé, et la fin d'une aide ne rompt pas celui-ci.",
 ('D5132-10-15', 'L1251-58-1'): "Renvoi d'emploi ajouté pour remplacer le fondement dérogatoire abrogé : les 1° et 2° maintiennent mise à disposition et lettre de mission, tandis que le contrat unique demeure distinct et sans terme lié à la mission. Le régime favorable d'inclusion reste accessible après suppression de l'attente ; ancienneté et CDI antérieurs ne sont ni remis à zéro ni terminés par l'échéance d'une mission ou d'une aide.",
}

EXTRA = {
    'R5132-7': ['L5132-5'],
    'R5132-10-12': ['L5132-6', 'L1251-58-1', 'L5132-6-1'],
    'D5132-10-15': ['L1251-58-1'],
}

for obj in ANSWER:
    n = obj['number']
    if n == 'R5122-18':
        obj['substantive_impact']['scope_limitations'] += " La référence hebdomadaire de quarante heures des nouveaux contrats, au lieu de trente-cinq, peut affecter le montant horaire à rémunération mensuelle donnée ; aucun gain uniforme de montant n'est affirmé. Les références annuelles ne sont pas relevées par cet article."
        obj['substantive_impact']['effects'].append(effect(
            'coordination', 'contrat-unique-duree-legale-40-heures',
            "Coordination du dénominateur horaire avec la durée légale applicable à la cohorte du salarié, sans présenter le relèvement de référence comme une baisse de prélèvement.",
            "Indemnité de 60 % calculée par référence à la durée légale applicable dans l'entreprise, soit trente-cinq heures hebdomadaires en droit source, ou à la durée collective/contractuelle inférieure.",
            "Durée légale de quarante heures pour les nouveaux contrats et trente-cinq pour les anciens selon la réforme, sous la référence collective/contractuelle inférieure ; références annuelles non relevées automatiquement.",
            'other', "Salariés indemnisés en activité partielle, selon la date et le régime de leur contrat.",
            "Transition de la réforme de durée du travail ; salaire contractuel non réduit, pas d'application du nouveau seuil aux anciens contrats.",
            "Pas de déclaration ajoutée ; effet sur le montant horaire à salaire donné distinct de l'extension du plancher et non chiffré globalement.",
            "sur la base de la durée légale du travail applicable dans l'entreprise ou, lorsqu'elle est inférieure, la durée collective du travail ou la durée stipulée au contrat de travail.",
            "La durée légale retenue est celle applicable au salarié concerné : le passage du seuil hebdomadaire à quarante heures pour les nouveaux contrats ne relève pas celui des contrats antérieurs, fixé à trente-cinq heures, et ne réduit pas le salaire contractuel."))
    key = obj['code_id'] + '|' + obj['source_id']
    required = list(REFS['requirements'][key])
    for extra in EXTRA.get(n, []):
        k = TARGET_NUMBER[extra]
        if k not in required:
            required.append(k)
    checks = []
    for k in required:
        target = TARGETS[k]
        tn = target['number']
        if tn == 'L1234-1':
            assessment = CONTEXT[n] + " L. 1234-1 officiel prévoit les paliers de moins de six mois, six mois à moins de deux ans et deux ans ; sa proposition leur substitue quinze jours calendaires pour les nouveaux contrats, avec maintien des règles anciennes et des protections/procédures distinctes. Ce n'est pas un renvoi opératoire de cet article ; le délai nouveau part du lendemain de la notification selon L. 1234-3 proposé, pas de l'événement traité ici."
        elif tn == 'L1221-2':
            assessment = "L. 1221-2 proposé écarte les nouveaux CDD et leurs renouvellements, mais ne transforme ni les anciens contrats ni les régimes publics. " + UNIQUE_CONTEXT[n]
        elif tn == 'L1234-9':
            assessment = CONTEXT[n] + " L. 1234-9 proposé concerne l'indemnité ordinaire à l'initiative patronale, hors faute grave : zéro avant un an apprécié à la fin effective, préavis inclus ; ensuite 0,20 mois par année totale, sans retrancher la première année, fractions en mois complets, plafond légal six mois. Aucun calcul de cette indemnité ne figure ici : salaires, congés, réparations et indemnités spéciales restent distincts. Anciens contrats : seuil de huit mois et composante antérieure aux taux anciens préservés sans double compte ; dispositions conventionnelles plus favorables non plafonnées."
        else:
            assessment = SPECIAL[(n, tn)]
        checks.append(dict(target_key=k, view_sha256=target['view_sha256'], assessment=assessment))
    obj['reference_checks'] = checks

Path('answer.json').write_text(json.dumps(ANSWER, ensure_ascii=False, indent=2) + '\n')
print('answer.json :', len(ANSWER), 'articles')
