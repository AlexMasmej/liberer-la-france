import json
import re
import html
from pathlib import Path

SOURCES = json.loads(Path('source.json').read_text())
REFS = json.loads(Path('reference-targets.json').read_text())
BY_NUMBER = {a['number']: a for a in SOURCES}
ANSWER = {}


def plain(s):
    return html.unescape(re.sub(r'<[^>]*>', '', s))


def replace(s, old, new):
    assert s.count(old) == 1, old
    return s.replace(old, new)


def effect(kind, measure_id, description, before, after, unit, population,
           transition, source_quote, proposed_quote,
           burdens='Aucune obligation, donnée, autorisation ou déclaration de remplacement n’est créée.'):
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit,
                affected_population=population,
                conditions_and_transition=transition,
                replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


def base(number, reason, notes, classification, assessment, limitations,
         burdens, proposed=None, effects=None, removed=None, repeal_scope=None,
         benefit=None):
    a = BY_NUMBER[number]
    row = {k: a[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    row.update(proposed_xml=proposed, reason=reason, review_notes=notes,
               status='retained_unchanged' if proposed is None else 'rewrite_draft')
    if proposed is None:
        row['classification'] = 'retained_necessary'
    row['substantive_impact'] = dict(
        version=1, classification=classification, assessment=assessment,
        scope_limitations=limitations, new_burdens_review=burdens,
        effects=effects or [])
    if removed:
        row.update(change_type='normative_reduction',
                   reform_policy_id='editorial_direction_2026_10_19',
                   removed_provisions=removed)
    if repeal_scope:
        row.update(change_type='full_repeal',
                   repeal_policy_id='editorial_direction_2026_10_19',
                   repeal_scope=repeal_scope)
    if benefit:
        row['benefit_review'] = benefit
    ANSWER[number] = row
    return row


base('L615-4-1',
     "Maintien intégral de la définition des occupants et des propriétaires occupants. Après examen des charges et doublons, ce texte n’impose ni collecte, ni prélèvement, ni agrément : il délimite les personnes protégées par les mesures de sauvegarde, y compris les occupants de bonne foi et les preneurs professionnels ou commerciaux. Une modification de vocabulaire n’apporterait aucun allègement.",
     "Les deux alinéas sont conservés : copropriétaires, associés de sociétés d’attribution et de coopératives de construction donnant vocation à l’attribution d’un lot, propriété ou jouissance et occupation effective. L. 615-1 à L. 615-4, lus dans le corpus, conservent leur champ autonome ; la carence d’immeuble de L. 615-6 n’est pas la carence communale SRU. Aucun nouveau renvoi ni transition nécessaire.",
     'retained_necessary',
     "Aucun changement normatif : les catégories d’occupants restent définies sans formalité supplémentaire, pour les sauvegardes futures également.",
     "Ce maintien ne tranche pas les conditions propres des aides et ne constitue pas un allègement des autres procédures du chapitre.",
     "Aucune charge nouvelle n’est identifiée : aucun texte de remplacement, registre, délai ou justificatif n’est introduit.")

base('L615-4-2',
     "Maintien intégral de la mise à disposition des seuls documents nécessaires au plan de sauvegarde. Le texte ne commande pas des exemplaires multiples ni un dossier annuel. La gratuité au regard des honoraires du syndic protège les copropriétaires ; la mise en demeure et le mois laissé avant engagement de responsabilité garantissent une demande établie et une possibilité de régularisation. Aucune suppression de fond suffisamment justifiée ne résulte de la seule pluralité des destinataires.",
     "Trois alinéas conservés, avec les quatre destinataires et le renvoi à la commission de L. 615-1. L’information sert au diagnostic, à l’exécution et à l’évaluation, non à un inventaire communal SRU. Le régime général de réemploi légal des données ne justifie pas de compter ici une nouvelle dispense. La mention du recommandé ne vaut pas exclusion des équivalences électroniques légalement applicables ; aucune nouvelle facilité de notification n’est revendiquée.",
     'retained_necessary',
     "L’accès ciblé aux pièces de la copropriété et l’interdiction d’honoraires spécifiques restent entiers ; aucune réduction de coût nouvelle n’est comptée.",
     "Les éventuels doublons d’une demande concrète ne sont pas établis par la source ; le coût national des plans de sauvegarde n’est pas évalué.",
     "Aucune charge nouvelle n’est identifiée, puisque la règle utile est conservée avec sa nécessité et ses garanties de mise en demeure.")

base('L615-5',
     "Maintien intégral de l’habilitation réglementaire limitée aux articles L. 615-1 à L. 615-4-2. Elle rend possible l’application des plans de sauvegarde nécessaires à la sécurité et au redressement des immeubles et n’impose, par elle-même, aucun agrément, déclaration ou prélèvement à supprimer.",
     "La plage de renvoi demeure cohérente : elle ne comprend ni la procédure judiciaire de carence de L. 615-6, ni une obligation communale de quota SRU. Le maintien de cette habilitation ne valide pas indistinctement les contraintes de tous ses décrets d’application et ne compte pas comme leur réécriture.",
     'retained_necessary',
     "Aucun changement matériel : le renvoi au décret en Conseil d’État conserve son seul champ d’application des plans de sauvegarde.",
     "Les décrets non assignés ne sont pas réputés allégés par ce maintien ; aucune économie de procédure ou de prélèvement n’est chiffrée.",
     "Aucune charge nouvelle n’est identifiée : aucune extension de l’habilitation ni condition d’accès à une aide n’est ajoutée.")


n = 'L615-6'
p = BY_NUMBER[n]['source_xml']
p = replace(p,
    "La saisine peut être également effectuée, après accord du maire ou du président de l'établissement public de coopération intercommunale compétent en matière d'habitat, par le représentant de l'Etat dans le département, le syndic,",
    "La saisine peut être également effectuée, sans accord préalable du maire ou du président de l'établissement public de coopération intercommunale compétent en matière d'habitat, par le représentant de l'Etat dans le département, le syndic,")
p = replace(p, "au chapitre Ier du titre Ier du livre V du présent code",
            "au chapitre unique du titre Ier du livre V du présent code")
p = replace(p,
    "à l'organisme payeur des allocations de logement mentionnées aux articles L. 542-1 et L. 831-1 du code de la sécurité sociale",
    "à l'organisme payeur des allocations de logement mentionnées au 2° de l'article L. 821-1 du présent code")
p = replace(p, "les parties ayant été dûment entendues ou appelées convoquées",
            "les parties ayant été dûment entendues ou convoquées")
p += "<p>La dispense d'accord préalable prévue au I s'applique aux saisines introduites à compter de l'entrée en vigueur de la loi qui l'institue ainsi qu'aux instances en cours. Aucune confirmation de saisine ni formalité de remplacement n'est exigée. Les actes de procédure régulièrement accomplis et les décisions juridictionnelles irrévocables antérieures ne sont pas remis en cause.</p>"
base(n,
     "Réforme de fond : suppression de l’accord municipal ou intercommunal préalable permettant au préfet, au syndic, à l’administrateur provisoire ou aux copropriétaires réunissant au moins 15 % des voix de saisir le juge. Le juge reste seul compétent pour l’expertise et la déclaration de carence ; l’accord local ne démontre donc pas une garantie essentielle distincte du contrôle juridictionnel. Maintien intégral des autres conditions, délais et protections. Coordination nécessaire, sans gain supplémentaire revendiqué, des renvois à la police unifiée de l’habitat indigne et aux allocations de logement désormais définies dans le CCH.",
     "Huit subdivisions conservées, avec trois mois renouvelables une fois pour l’expertise, l’annexe privative non dirimante, le seuil de 15 %, le projet et son coût, le relogement selon le chapitre IV du titre Ier du livre III de l’urbanisme, toutes les notifications, la présomption après deux mois sans comptes, le contradictoire, le mois de participation publique, la liquidation et le recours de deux mois, ainsi que les syndicats secondaires. Le nouveau dernier alinéa règle les instances en cours sans recommencer les actes. La source cumule les mots « appelées convoquées » : cette anomalie rédactionnelle est expressément ramenée à « convoquées », sans retrait du contradictoire ni gain de fond compté. L’articulation préexistante du II, réservé à la saisine locale, et du V sur le projet d’acquisition demeure : la dispense d’accord n’impose pas un nouvel engagement d’acquisition ou de financement aux autres auteurs de saisine. Renvois rectifiés expressément : L. 511-1, L. 511-2 et L. 821-1 ont été lus dans le corpus ; le livre V comporte un chapitre unique et les anciennes cibles CSS L. 542-1/L. 831-1 ne figurent plus dans le corpus courant. Le nouveau renvoi à L. 821-1 n’était pas fourni comme cible de reference-targets.json ; il est vérifié séparément en lecture seule. Les articles L. 143-3 et L. 184-1 ont également été lus et restent pertinents. La loi de copropriété et le code de l’expropriation restent hors lot ; leur contrôle n’est pas présenté comme exhaustif. Aucune suppression de la carence communale SRU n’est transposée à la sécurité des immeubles.",
     'mixed',
     "Un accord administratif préalable à l’accès au juge est effectivement supprimé, sans déclaration équivalente. En contrepartie, les obligations de traitement et de notification peuvent désormais être déclenchées par une saisine sans accord local ; ce champ supplémentaire justifie mixed. Les mises à jour de renvois ne sont pas deux réductions supplémentaires.",
     "Le coût et le nombre de saisines supplémentaires ne sont pas chiffrés et aucun solde net de coût ou de complexité n’est établi. L’expertise, la participation publique, le projet local, l’expropriation et les dépenses de relogement demeurent dans leurs régimes propres.",
     "Aucune déclaration, donnée, registre, délai ou autorisation de remplacement n’est ajouté au demandeur. Toutefois, l’ouverture sans accord local étend les cas dans lesquels doivent être assurés le traitement juridictionnel, les notifications et, si la carence est déclarée, les suites prévues au V. Ces charges publiques et procédurales supplémentaires possibles sont recensées ; leur coût net reste inconnu.",
     proposed=p,
     removed=["Accord préalable du maire ou du président de l’EPCI conditionnant la saisine du juge par les quatre autres catégories de demandeurs habilités."],
     effects=[
       effect('authorization_removed', 'coproprietes-carence-saisine-sans-accord',
              "Suppression du filtre local préalable à la saisine du président du tribunal judiciaire.",
              "Préfet, syndic, administrateur provisoire et copropriétaires disposant d’au moins 15 % des voix : accord préalable du maire ou du président de l’EPCI.",
              "Ces mêmes personnes saisissent directement le juge ; le seuil de 15 % et le contrôle juridictionnel demeurent.",
              'legal_duty', 'Demandeurs habilités et copropriétés en graves difficultés relevant du I.',
              "Saisines nouvelles et instances en cours dès l’entrée en vigueur ; décisions irrévocables et actes réguliers préservés.",
              "après accord du maire ou du président de l'établissement public de coopération intercommunale compétent en matière d'habitat",
              "sans accord préalable du maire ou du président de l'établissement public de coopération intercommunale compétent en matière d'habitat",
              burdens="Aucune formalité de remplacement pour le demandeur. Le traitement de nouvelles instances et leurs notifications s'étendent aux saisines auparavant empêchées par le refus d'accord ; les suites du V restent applicables si la carence est déclarée, sans coût net établi."),
       effect('obligation_added', 'coproprietes-carence-saisine-sans-accord',
              "Extension du champ de déclenchement du traitement juridictionnel et des notifications obligatoires aux saisines sans accord local ; aucune nouvelle catégorie de document n’est créée.",
              "Pour le préfet, le syndic, l’administrateur provisoire et les copropriétaires réunissant au moins 15 % des voix, le refus d’accord local empêche la saisine et donc les obligations procédurales qui en résultent.",
              "Ces obligations procédurales peuvent être déclenchées sans cet accord ; les conclusions sont notifiées aux mêmes destinataires et les suites du V demeurent si la carence est déclarée.",
              'legal_duty', 'Juridiction, autorités publiques et parties aux saisines auparavant subordonnées à un accord local.',
              "Saisines nouvelles et instances en cours dès l’entrée en vigueur ; les conditions de danger, de difficulté et de contrôle juridictionnel demeurent, sans engagement automatique d’acquisition du seul fait de la saisine.",
              "La saisine peut être également effectuée, après accord du maire ou du président de l'établissement public de coopération intercommunale compétent en matière d'habitat, par le représentant de l'Etat dans le département, le syndic,",
              "La saisine peut être également effectuée, sans accord préalable du maire ou du président de l'établissement public de coopération intercommunale compétent en matière d'habitat, par le représentant de l'Etat dans le département, le syndic,",
              burdens="Champ procédural étendu : traitement des saisines, expertise ordonnée et notifications dans les nouveaux cas, puis suites du V après déclaration de carence. Les tâches restent de même nature ; volume, dépense et solde net ne sont pas établis."),
       effect('coordination', 'sauvegarde-renvois-polices-et-allocations',
              "Actualisation du destinataire de notification des allocations et du chapitre de police de l’habitat indigne.",
              "Renvois CSS L. 542-1/L. 831-1 et chapitre Ier du titre Ier du livre V, antérieurs à la recodification.",
              "Même organisme payeur, identifié par CCH L. 821-1, 2°, et chapitre unique du livre V ; aucun nouveau contrôle.",
              'other', 'Parties à la procédure de carence et organisme payeur des allocations.',
              "Coordination de textes, sans nouvelle aide ni changement des droits à allocation.",
              "à l'organisme payeur des allocations de logement mentionnées aux articles L. 542-1 et L. 831-1 du code de la sécurité sociale",
              "à l'organisme payeur des allocations de logement mentionnées au 2° de l'article L. 821-1 du présent code")])


base('L615-7',
     "Maintien intégral d’une procédure d’expropriation déjà dérogatoire au droit commun, réservée à une carence judiciairement déclarée. Les désignations, la publicité, le plan de relogement, l’indemnité provisionnelle et le délai de deux mois avant possession protègent le droit de propriété et les occupants face à une dépossession forcée. Leur fonction essentielle est établie ; aucune taxe, double dossier ou autorisation inutile n’est ici démontré.",
     "Tous les alinéas et les 1° à 5° sont conservés. Le renvoi au V de L. 615-6 reste exact dans le nouveau corps : projet approuvé et observations du public maintenus. L. 615-10 conserve l’expérimentation et l’opérateur bénéficiaire ; sa suppression de périodicité du plan de travaux n’affecte pas l’expropriation. Indemnité au moins égale à l’évaluation des domaines, paiement ou consignation avant possession, deux mois à compter de la publication et poursuite de procédure dans le mois restent distincts. La note du 1er janvier 2020 est historique et ne date pas la présente réforme.",
     'retained_necessary',
     "Aucun nouvel allègement : la dérogation procédurale existante reste ouverte et ses garanties de paiement, relogement et publicité sont entièrement conservées.",
     "Ce maintien ne modifie ni le code de l’expropriation, ni les procédures d’attribution de logements ; aucun rendement budgétaire n’est établi.",
     "Aucune charge nouvelle n’est identifiée : mêmes cinq mentions de l’arrêté, mêmes destinataires et mêmes délais protecteurs.",
     benefit="La dérogation au code de l’expropriation et la diversité des bénéficiaires publics ou opérateurs restent applicables aux opérations futures recevables. Le projet de relogement, le plancher d’indemnité égal à l’évaluation des domaines pour propriétaires, copropriétaires, porteurs de parts et titulaires de baux commerciaux ou professionnels, le paiement ou la consignation préalable et les deux mois avant possession demeurent entiers. La poursuite judiciaire dans le mois est aussi conservée. Il s’agit de facilités d’intervention et de garanties patrimoniales, sans exonération fiscale à fermer ni privilège réservé aux seuls dossiers anciens.")


n = 'L615-8'
p = BY_NUMBER[n]['source_xml']
p = replace(p,
    "du coût des travaux prescrits sur les logements par des arrêtés pris sur le fondement des articles L. 1331-26 et suivants du code de la santé publique et de l'article L. 511-2 du présent code.",
    "du coût des travaux prescrits sur les logements par des arrêtés de mise en sécurité ou de traitement de l'insalubrité pris sur le fondement du chapitre unique du titre Ier du livre V du présent code. Sont également pris en compte, lorsqu'ils demeurent applicables, les travaux prescrits par des arrêtés pris sur le fondement des articles L. 1331-26 et suivants du code de la santé publique ou de l'article L. 511-2 du présent code dans leur rédaction antérieure au 1er janvier 2021.")
p += "<p>La présente rédaction s'applique aux évaluations qui ne sont pas définitivement fixées à l'entrée en vigueur de la loi qui l'institue. Elle ne rouvre ni les transferts de propriété ni les indemnités définitivement fixées.</p>"
base(n,
     "Coordination nécessaire, sans réduction normative nouvelle : le renvoi de 2015 aux anciens arrêtés de péril et d’insalubrité est complété par le régime unifié du livre V applicable aux arrêtés notifiés depuis le 1er janvier 2021. L’ancien L. 511-2 ne décrit plus la même procédure. Les arrêtés anciens encore applicables restent pris en compte ; les règles de transfert et tous les renvois de fixation et de calcul de l’indemnité sont intégralement maintenus. Aucun simple changement de style n’est ajouté.",
     "Quatre alinéas sources lus en entier. L. 511-1 et sa note transitoire, L. 511-2, L. 511-9 à L. 511-11 et L. 511-19 ont été lus dans le corpus : les arrêtés actuels de mise en sécurité et de traitement de l’insalubrité justifient le renvoi au chapitre unique. Ce nouveau renvoi n’est pas une cible fournie par reference-targets.json et sa vérification est distincte. Le texte intégral des anciens articles CSP et du code de l’expropriation n’est pas dans les cinq codes fournis ; aucune formule d’indemnisation extérieure n’est inventée et leur confrontation exhaustive reste nécessaire. L. 615-7 est maintenu ; l’indemnité d’expropriation ne devient pas une indemnité salariale. La transition empêche la réouverture des indemnités et transferts définitifs ; elle ne crée pas une nouvelle déduction forfaitaire de travaux.",
     'coordination_only',
     "Les bases légales des travaux prescrits sont coordonnées avec la police unifiée ; aucune diminution d’indemnité, taxe supprimée ou économie supplémentaire n’est revendiquée.",
     "La vérification intégrale des articles externes d’expropriation et des anciennes versions CSP reste hors corpus. Le montant de chaque indemnité relève du juge et de ses règles propres.",
     "Aucune charge nouvelle n’est identifiée : aucun rapport supplémentaire ni justificatif distinct n’est exigé, et les indemnités définitivement fixées ne sont pas rouvertes.",
     proposed=p,
     effects=[effect('coordination', 'sauvegarde-renvois-polices-et-allocations',
              "Coordination temporelle des fondements des travaux pris en compte dans l’évaluation.",
              "L’alinéa vise les anciens articles CSP L. 1331-26 et suivants et CCH L. 511-2 sans distinguer leurs versions.",
              "Le chapitre unique actuel de police est identifié ; les arrêtés anciens encore applicables conservent leur prise en compte.",
              'other', 'Propriétaires et titulaires de droits indemnisés dans la procédure de carence.',
              "Évaluations non définitivement fixées ; aucune réouverture des indemnités ou transferts définitifs.",
              "du coût des travaux prescrits sur les logements par des arrêtés pris sur le fondement des articles L. 1331-26 et suivants du code de la santé publique et de l'article L. 511-2 du présent code.",
              "du coût des travaux prescrits sur les logements par des arrêtés de mise en sécurité ou de traitement de l'insalubrité pris sur le fondement du chapitre unique du titre Ier du livre V du présent code.")])


base('L615-9',
     "Maintien intégral du droit des propriétaires occupants aux allocations de logement à raison de l’indemnité d’occupation versée à l’expropriant. Il s’agit d’un avantage utile pour éviter qu’une expropriation de sauvegarde ne prive les occupants d’aide ; il demeure ouvert aux futures situations éligibles. Le texte ne crée ni prélèvement accessoire ni justificatif redondant à retirer.",
     "L. 821-1 a été lu dans le corpus : son 2° couvre l’allocation de logement familiale et l’allocation de logement sociale, distinctes de l’APL du 1°. Ce renvoi est exact et n’est ni étendu à une autre aide ni fermé. Les conditions d’attribution propres au livre VIII demeurent ; aucun seuil d’ancienneté professionnelle n’est importé.",
     'retained_necessary',
     "L’ouverture existante des allocations familiales ou sociales de logement sur l’indemnité d’occupation est entièrement conservée, sans nouveau gain compté.",
     "Ce texte ne dispense pas des conditions autonomes d’allocation et ne garantit pas à lui seul le montant de l’aide d’un ménage.",
     "Aucune charge nouvelle n’est identifiée : maintien du même droit et du même renvoi, sans attestation ou ancienneté supplémentaire.")


n = 'L615-10'
p = replace(BY_NUMBER[n]['source_xml'],
            "établit un plan pluriannuel de travaux actualisé tous les trois ans et provisionne",
            "établit un plan pluriannuel de travaux et provisionne")
p += "<p>À compter de l'entrée en vigueur de la loi supprimant l'actualisation triennale obligatoire du plan pluriannuel de travaux, aucune actualisation périodique n'est exigée sur ce seul fondement, y compris pour les plans déjà établis et les échéances antérieures non exécutées. Les obligations d'entretien, de conservation et de sécurité, les travaux prescrits ainsi que les engagements contractuels valablement souscrits demeurent applicables. Cette suppression ne proroge pas l'expérimentation prévue au I et ne remet pas en cause les responsabilités et les droits nés de faits antérieurs.</p>"
base(n,
     "Réforme de fond ciblée : suppression de l’actualisation automatique tous les trois ans du plan pluriannuel de travaux, sans rapport ni déclaration de remplacement. L’obligation d’établir le plan, le diagnostic technique, les provisions, l’entretien, la conservation et la responsabilité de l’opérateur demeurent. La répétition calendaire ne démontre pas une utilité essentielle indépendante de ces obligations de sécurité. Tous les autres éléments de l’expérimentation, y compris son évaluation parlementaire, sont intégralement conservés.",
     "Sept subdivisions conservées dans leur ordre : vingt ans à compter de la loi du 24 mars 2014, expropriation des parties communes, état descriptif et servitude, redevance mensuelle proportionnelle aux superficies, révision par décret, hypothèque et priorités année courante/deux dernières années, allocations de logement, responsabilité et recours, préemption, expropriation totale, avis favorables pour remise en copropriété et formule complète d’indemnité nette de toutes redevances. Le rapport reste dû six mois avant le terme. La transition retire les rattrapages d’actualisation sur ce seul fondement sans libérer des travaux, de la sécurité ou des contrats. La note historique du 1er janvier 2022 est lue ; elle ne change ni le point de départ de 2014 ni la durée portée à vingt ans en 2024. Les textes d’application de l’expérimentation et les contrats doivent être coordonnés sans réintroduire un calendrier réglementaire obligatoire sur le seul fondement retiré.",
     'material_reduction',
     "La mise à jour triennale imposée disparaît ; le plan initial, ses provisions et l’exécution des obligations de conservation restent dus. La redevance de service n’est pas supprimée ni présentée comme une taxe abolie.",
     "Le coût de mise à jour évité n’est pas évalué. Les engagements contractuels, travaux prescrits et contrôles de sécurité peuvent toujours nécessiter des interventions documentées.",
     "Aucune charge nouvelle n’est identifiée : aucune échéance de substitution, nouveau registre ou nouveau déclencheur déclaratif ne remplace les trois ans supprimés.",
     proposed=p,
     removed=["Actualisation obligatoire tous les trois ans du plan pluriannuel de travaux établi par l’opérateur des parties communes expropriées."],
     effects=[effect('obligation_removed', 'coproprietes-plan-travaux-fin-triennalite',
              "Suppression de la seule réactualisation calendaire triennale du plan.",
              "L’opérateur établit un plan pluriannuel de travaux et doit l’actualiser tous les trois ans.",
              "Le plan reste obligatoire ; aucune actualisation périodique n’est due sur le seul fondement de L. 615-10.",
              'legal_duty', 'Opérateurs de l’expérimentation d’expropriation des parties communes.',
              "Dès l’entrée en vigueur, plans anciens compris et sans rattrapage sur ce seul fondement ; obligations de sécurité et contrats préservés.",
              "établit un plan pluriannuel de travaux actualisé tous les trois ans et provisionne, dans sa comptabilité, des sommes en prévision de la réalisation des travaux.",
              "établit un plan pluriannuel de travaux et provisionne, dans sa comptabilité, des sommes en prévision de la réalisation des travaux.")],
     benefit="La dérogation permettant l’expropriation des seules parties communes reste ouverte pendant les vingt ans prévus au I, sans prolongation inventée. Les facultés de confier l’entretien à un opérateur, de lui déléguer la préemption et, si nécessaire, de demander l’expropriation totale demeurent dans leurs conditions. La redevance conserve son affectation aux dépenses nécessaires, sa proportion à la superficie, son ouverture aux allocations de logement pour les propriétaires occupants et la garantie hypothécaire de l’opérateur. La responsabilité pour dommages et les recours restent entiers. La nouvelle mise en copropriété demeure possible après les avis favorables requis ; la valeur initiale majorée des travaux reste diminuée de la totalité des redevances, évitant un double paiement. Seule la périodicité triennale est retirée, sans fermeture de ces droits pour les opérations futures recevables.")


base('L616',
     "Maintien intégral du droit communal de préemption destiné au maintien dans les lieux d’un débiteur saisi satisfaisant aux plafonds de ressources HLM. La préemption constitue ici une protection ciblée du logement principal, non une autorisation supplémentaire de construire ou de louer. Sa suppression retirerait une possibilité favorable de maintien ; la délégation facultative à un office public de l’habitat ne crée pas de procédure doublonnée.",
     "Les deux alinéas conservent la résidence principale, la condition de ressources, le maintien dans les lieux et le cas des adjudications obligatoires. Le renvoi à L. 213-3 de l’urbanisme et les modalités d’adjudication sont à distinguer de la préemption partielle de L. 213-2-1 supprimée dans la coordination SRU : aucune dépendance textuelle à cet article abrogé n’apparaît ici. L. 213-3 et les articles réglementaires d’adjudication ont été lus séparément dans le corpus. La préemption ne crée ni taxe ni droit de succession.",
     'retained_necessary',
     "Aucune réduction nouvelle ; la faculté favorable d’éviter le départ du saisi demeure disponible pour les futures adjudications recevables.",
     "Le texte ne garantit ni l’exercice effectif de la préemption par une commune ni le financement de toutes les acquisitions ; aucun coût global n’est mesuré.",
     "Aucune charge nouvelle n’est identifiée : les conditions et modalités existantes sont maintenues sans dossier ou délai ajouté.")


n = 'L621-1'
p = replace(BY_NUMBER[n]['source_xml'],
            "Le service municipal du logement a notamment pour tâche de dresser un fichier général des locaux à usage d'habitation, en vue de déterminer les locaux vacants, inoccupés ou insuffisamment occupés.",
            "Le service municipal du logement n'est pas tenu de dresser un fichier général des locaux à usage d'habitation. Aucune obligation de déclaration, de collecte ou de mise à jour d'un tel fichier ne peut être imposée aux propriétaires, aux gérants ou aux occupants sur le fondement du présent chapitre.")
p += "<p>La suppression de cette obligation s'applique dès l'entrée en vigueur de la loi qui l'institue, y compris aux fichiers existants et aux opérations de collecte ou de mise à jour en cours. Aucune collecte, mise à jour ou transmission de rattrapage n'est exigée sur ce fondement. Les données déjà recueillies restent soumises aux règles applicables à la protection des données à caractère personnel et aux archives publiques ; la présente disposition n'autorise aucun nouvel accès à ces données.</p>"
base(n,
     "Réforme de fond : suppression de la mission obligatoire de constitution du fichier général de tous les locaux d’habitation et de ses collectes et mises à jour imposées aux particuliers. L’exhaustivité d’un fichier municipal ne démontre pas une nécessité essentielle au regard des missions ciblées de logement et des informations légalement disponibles. Le service temporaire et la possibilité d’un service intercommunal demeurent ; aucune base de données ou transmission équivalente n’est créée.",
     "Trois alinéas conservés à leur place : désignation administrative sur proposition des maires et caractère temporaire, retrait de la tâche de fichier, association de communes. La rédaction supprime une obligation autonome, au-delà du simple réemploi de pièces déjà prévu par le CRPA, sans attribuer de nouveau droit d’accès aux données fiscales ou sociales. L. 621-2 est coordonné dans ce lot ; les déclarations de L. 621-5/L. 621-6 sont abolies séparément. Les missions de contrôle légalement autonomes et leurs limites de L. 651-6/L. 651-7 ne deviennent pas des collectes générales de remplacement. Les archives ne sont ni détruites d’office ni régularisées par un nouveau fichier. Les règles de logement social ou de réquisition ne sont pas abolies par cette mesure bornée.",
     'material_reduction',
     "Le fichier municipal général et la charge de collecte qui lui est propre cessent d’être obligatoires ; ce retrait est distinct d’une simple reformulation du droit existant de réemploi.",
     "Les recensements ou contrôles fondés sur d’autres textes subsistent dans leur champ ; aucun nombre de fichiers actifs ni coût public net évité n’est établi.",
     "Aucune charge nouvelle n’est identifiée : pas de fichier alternatif, de déclaration de substitution, de mise à jour résiduelle obligatoire ou d’ouverture nouvelle de données.",
     proposed=p,
     removed=["Constitution obligatoire d’un fichier général des locaux d’habitation destiné à repérer les locaux vacants, inoccupés ou insuffisamment occupés et collectes imposées à cette seule fin."],
     effects=[effect('obligation_removed', 'logement-fichier-general-suppression',
              "Suppression de la tâche obligatoire de fichier général municipal et de ses obligations de collecte.",
              "Tout service institué doit dresser un fichier général des locaux à usage d’habitation.",
              "Aucun fichier général obligatoire ni collecte, déclaration ou mise à jour imposée aux propriétaires, gérants et occupants sur ce fondement.",
              'legal_duty', 'Services municipaux ou intercommunaux concernés, propriétaires, gérants et occupants.',
              "Entrée en vigueur immédiate, fichiers existants et collectes en cours compris ; protection des données et archives maintenue.",
              "Le service municipal du logement a notamment pour tâche de dresser un fichier général des locaux à usage d'habitation, en vue de déterminer les locaux vacants, inoccupés ou insuffisamment occupés.",
              "Le service municipal du logement n'est pas tenu de dresser un fichier général des locaux à usage d'habitation.")])


n = 'L621-2'
p = replace(BY_NUMBER[n]['source_xml'],
            "Ce décret fixe les obligations incombant aux propriétaires, aux gérants et aux occupants des lieux en ce qui concerne la tenue du fichier général, ainsi que les déclarations prévues aux articles L. 621-5 et L. 621-6.",
            "Ce décret ne peut imposer aux propriétaires, aux gérants ou aux occupants la tenue d'un fichier général des locaux à usage d'habitation, ni rétablir les déclarations supprimées aux articles L. 621-5 et L. 621-6.")
base(n,
     "Coordination nécessaire des suppressions du fichier général et des déclarations de location : retrait effectif de l’habilitation réglementaire correspondante pour empêcher leur rétablissement par décret. Maintien intégral et autonome des définitions de vacance, d’inoccupation et de sous-occupation, de toutes les catégories d’occupants comptées et des exclusions favorables. Ces définitions servent notamment au relogement social et à ses aides ; elles ne doivent pas disparaître avec le fichier.",
     "L’alinéa premier conserve la définition réglementaire des locaux vacants et inoccupés ; l’alinéa deuxième conserve le seuil supérieur de plus d’une pièce, le renvoi à l’article 28 de la loi de 1948, l’exclusion des cuisines et des pièces indispensables à une fonction publique élective ou une profession. Les 1° à 5° et les enfants en droit de visite et d’hébergement restent inchangés. L. 442-3-1, L. 442-5-1, L. 442-5-2 et L. 482-1, lus dans le corpus, justifient cette base autonome ; L. 641-3 conserve son renvoi au décret de définition des conditions d’occupation suffisantes. Les définitions n’emportent plus les obligations abrogées de L. 621-5/L. 621-6. La loi de 1948 demeure extérieure au lot et n’est pas présentée comme réécrite.",
     'coordination_only',
     "L’habilitation de recréer le fichier et les déclarations est neutralisée ; les réductions principales sont comptées à L. 621-1 et L. 621-5, sans nouvelle suppression de taxe.",
     "Le régime autonome des réquisitions et les règles de sous-occupation du parc social demeurent ; aucune réduction de leurs contraintes n’est revendiquée ici.",
     "Aucune charge nouvelle n’est identifiée : définitions, seuil, exceptions et personnes comptées inchangés ; aucune déclaration de remplacement n’est autorisée.",
     proposed=p,
     removed=["Habilitation du décret à imposer la tenue du fichier général et les déclarations des articles L. 621-5 et L. 621-6, désormais supprimées."],
     effects=[
       effect('coordination', 'logement-fichier-general-suppression',
              "Retrait du fondement réglementaire de la tenue obligatoire du fichier, coordonné à L. 621-1.",
              "Le décret fixe des obligations des propriétaires, gérants et occupants pour tenir le fichier général.",
              "Le décret ne peut imposer la tenue d’un fichier général ; les définitions restent utilisables et les archives déjà constituées ne sont pas supprimées.",
              'legal_duty', 'Propriétaires, gérants, occupants et autorité réglementaire.',
              "Même suppression prospective que L. 621-1, sans fermeture des droits de relogement futurs.",
              "Ce décret fixe les obligations incombant aux propriétaires, aux gérants et aux occupants des lieux en ce qui concerne la tenue du fichier général, ainsi que les déclarations prévues aux articles L. 621-5 et L. 621-6.",
              "Ce décret ne peut imposer aux propriétaires, aux gérants ou aux occupants la tenue d'un fichier général des locaux à usage d'habitation, ni rétablir les déclarations supprimées aux articles L. 621-5 et L. 621-6."),
       effect('coordination', 'locations-fin-condition-occupation-suffisante',
              "Neutralisation de l’habilitation aux déclarations de location retirées dans L. 621-5 et L. 621-6.",
              "Le décret prévoit les déclarations du preneur puis leur transmission par le bailleur.",
              "Le décret ne peut rétablir ces déclarations ; les conditions d’occupation servant aux autres dispositifs ne sont pas effacées.",
              'legal_duty', 'Preneurs et bailleurs des communes dotées d’un service du logement.',
              "Application coordonnée à la disparition des formalités, sans nouveau formulaire.",
              "ainsi que les déclarations prévues aux articles L. 621-5 et L. 621-6.",
              "ni rétablir les déclarations supprimées aux articles L. 621-5 et L. 621-6.")],
     benefit="Le seuil de sous-occupation reste strictement supérieur de plus d’une pièce au nombre de résidents, sans compter les cuisines. Les pièces indispensables à une profession ou une fonction publique élective restent exclues. Le conjoint, parents et alliés, personnes à charge, personnes au service de l’occupant et affiliées aux caisses visées, sous-locataires et enfants soumis à un droit de visite et d’hébergement restent tous comptés. Ces règles favorables continuent de protéger les situations futures dans les dispositifs sociaux qui utilisent la définition, notamment les offres de relogement à loyer inférieur et aides à la mobilité ; elles ne sont pas cantonnées aux anciens contrats. La définition réglementaire de la vacance et de l’inoccupation est conservée. Le retrait de l’habilitation au fichier et aux déclarations supprime une contrainte, sans supprimer une exonération fiscale ni une dérogation favorable.")


base('L621-3',
     "Maintien intégral des règles de prise en charge et de fonctionnement des services municipaux ou intercommunaux du logement. La faculté de remboursement et l’avis des maires avant sa suppression protègent les collectivités. La désignation administrative de L. 621-1 ne constitue pas ici une autorisation privée redondante : elle délimite un service doté de prérogatives légales de contrôle et susceptible de financement d’État. Aucune suppression financière ou ouverture nouvelle de pouvoirs n’est justifiée.",
     "Les trois alinéas et les deux hypothèses de fonctionnement communal demeurent. R. 621-1 et R. 621-2 ont été lus : création par arrêté interministériel et fin du remboursement après avis des maires, sans justificatif doublonné identifié par le texte législatif. La suppression du fichier général n’abolit pas le service ni ses autres missions légales. Aucune faculté de remboursement n’est réservée aux seuls services déjà constitués ; aucun transfert budgétaire supplémentaire n’est inventé.",
     'retained_necessary',
     "Aucune baisse de prélèvement ni transfert nouveau : les possibilités de financement et d’organisation demeurent dans leurs conditions existantes.",
     "Le nombre de services et les remboursements effectivement pratiqués ne sont pas établis ; la dépense publique ne devient pas une économie par maintien de cette règle.",
     "Aucune charge nouvelle n’est identifiée : même décision, même avis et mêmes modalités d’organisation, sans dossier supplémentaire.")


n = 'L621-4'
p = replace(BY_NUMBER[n]['source_xml'],
            "Il est institué à Paris et dans chacune des communes mentionnées ci-dessus un comité consultatif municipal du logement dont la composition est fixée par décision administrative.",
            "À Paris et dans chacune des communes mentionnées ci-dessus, la création d'un comité consultatif municipal du logement est facultative. Lorsqu'un tel comité est institué, sa composition est fixée par décision administrative. L'absence d'un tel comité ou de son avis ne fait pas obstacle à l'exercice des missions légales du service du logement.")
p += "<p>La suppression de l'obligation d'instituer ce comité s'applique à compter de l'entrée en vigueur de la loi qui l'institue. Elle n'affecte ni les actes régulièrement pris ni les créances antérieurement nées. Les communes peuvent conserver les comités existants ; aucune consultation de remplacement n'est imposée.</p>"
base(n,
     "Réforme de fond : le comité consultatif municipal du logement cesse d’être obligatoire à Paris et dans les communes visées de l’ancien département de la Seine. Il peut être conservé ou créé volontairement, sans instance ou consultation équivalente imposée. Les autorités compétentes et les agents assermentés conservent leurs missions légales ; aucune fonction essentielle de sécurité n’exige cette instance consultative distincte.",
     "Le premier alinéa est intégralement maintenu : service départemental et prérogatives des agents selon L. 651-6/L. 651-7, lus en entier. Ces dispositions de contrôle ne sont ni élargies ni validées au-delà de leurs garanties applicables. R. 621-3, lu en entier, doit être coordonné pour ne pas rétablir un comité obligatoire dans les communes couvertes par le présent article ; la situation des autres services n’est pas réputée réécrite. Les compositions administratives doivent suivre la facultativité, sans mandat ou indemnité nouvelle. Les comités volontaires et les créances antérieures sont protégés.",
     'material_reduction',
     "Une instance consultative obligatoire devient facultative dans le périmètre géographique exact de la source ; les services et leurs contrôles autonomes demeurent.",
     "Le nombre de comités effectivement actifs et leurs coûts ne sont pas connus ; aucune économie nationale ou suppression de tous les comités locaux n’est avancée.",
     "Aucune charge nouvelle n’est identifiée : aucune instance, consultation, donnée ou transmission ne remplace le comité devenu facultatif.",
     proposed=p,
     removed=["Institution obligatoire d’un comité consultatif municipal du logement à Paris et dans les communes visées des trois départements de l’ancien département de la Seine."],
     effects=[effect('obligation_removed', 'logement-comite-consultatif-facultatif',
              "Fin de l’instance consultative obligatoirement distincte dans les communes désignées.",
              "Paris et chacune des communes visées doivent être dotées d’un comité consultatif municipal du logement.",
              "Création ou maintien facultatifs ; l’absence de comité ou d’avis ne bloque pas les missions légales du service.",
              'legal_duty', 'Paris et communes visées des Hauts-de-Seine, de Seine-Saint-Denis et du Val-de-Marne.',
              "À l’entrée en vigueur ; actes et créances antérieurs préservés, comités existants conservables volontairement.",
              "Il est institué à Paris et dans chacune des communes mentionnées ci-dessus un comité consultatif municipal du logement dont la composition est fixée par décision administrative.",
              "À Paris et dans chacune des communes mentionnées ci-dessus, la création d'un comité consultatif municipal du logement est facultative.")])


n = 'L621-5'
p = "<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi qui prononce son abrogation.</p><p>À compter de cette date, aucune location ou sous-location de locaux à usage d'habitation ou professionnel ne peut être interdite sur le seul fondement d'une occupation insuffisante au sens du présent chapitre. Aucune déclaration du preneur au bailleur ni justification équivalente n'est exigée sur ce fondement.</p><p>Cette suppression s'applique aux contrats conclus à compter de cette date ainsi qu'aux effets futurs des contrats en cours. Les droits attachés aux locations ou sous-locations antérieures, notamment celles ayant acquis date certaine ou donné lieu à une occupation effective à la date de la décision instituant le service municipal du logement, ne sont pas remis en cause. Les obligations de décence, de sécurité et de salubrité, les droits des occupants et les régimes de relogement légalement autonomes demeurent applicables.</p>"
base(n,
     "Abrogation de fond : suppression de la condition générale d’occupation suffisante pour conclure une location ou sous-location et de la déclaration du preneur au bailleur. La restriction empêche la location de locaux pourtant habitables sans démonstration d’un risque de sécurité ; elle n’est pas nécessaire au maintien des règles autonomes du parc social. Aucun contrôle d’occupation ou formulaire équivalent ne la remplace. La protection des locations déjà dispensées est conservée et la liberté vaut aussi pour les contrats futurs.",
     "Deux alinéas sources lus, y compris l’exception de date certaine et d’occupation effective au jour de publication de la décision instituant le service. L. 621-2 conserve ses définitions et ses avantages de décompte pour les autres régimes. L. 621-6 est abrogé avec les formalités et conséquences spécifiques ; L. 651-3/L. 651-4, lus dans le corpus, ne peuvent plus sanctionner une déclaration supprimée pour l’avenir et doivent être coordonnés sans effacer les infractions autonomes. La procédure de relogement du parc social de L. 442-3-1 et L. 482-1 demeure distincte. Le régime d’ordre public de L. 651-9 doit être purgé de ce renvoi devenu sans objet ; il ne fait pas renaître la condition abrogée. Aucun décret ne peut la recréer par L. 621-2.",
     'material_reduction',
     "La restriction d’accès au bail fondée sur la sous-occupation et sa déclaration disparaissent réellement pour l’avenir ; les contrats anciennement exemptés ne perdent aucun droit.",
     "Les règles du parc social, les réquisitions, la décence et les changements d’usage restent autonomes ; ce texte ne supprime pas toutes les conditions légales de location.",
     "Aucune charge nouvelle n’est identifiée : pas de déclaration de substitution, d’autorisation, d’attestation ou de registre ; la condition générale est retirée.",
     proposed=p,
     repeal_scope="Condition d’occupation suffisante imposée aux nouvelles locations ou sous-locations d’habitation ou professionnelles et déclaration du preneur au bailleur ; suppression pour l’avenir sans atteinte aux contrats antérieurement dispensés.",
     effects=[effect('obligation_removed', 'locations-fin-condition-occupation-suffisante',
              "Suppression de la condition de location et de la justification déclarative du preneur.",
              "Dans les localités dotées d’un service municipal, nouvelles locations ou sous-locations réservées aux personnes justifiant une occupation suffisante, avec déclaration au bailleur.",
              "Aucune interdiction ni déclaration sur ce seul fondement ; sécurité, décence et régimes autonomes préservés.",
              'legal_duty', 'Preneurs et bailleurs de locaux d’habitation ou professionnels dans les localités concernées.',
              "Contrats nouveaux et effets futurs des contrats en cours dès l’entrée en vigueur ; anciennes dispenses préservées.",
              "Cette justification fait l'objet d'une déclaration du preneur au bailleur.",
              "Aucune déclaration du preneur au bailleur ni justification équivalente n'est exigée sur ce fondement.")])


n = 'L621-6'
p = "<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi qui prononce son abrogation.</p><p>À compter de cette date, aucune transmission des déclarations du preneur au service municipal du logement n'est exigée sur le fondement du présent article, même pour une location ou sous-location conclue antérieurement. Aucune transmission de rattrapage ni formalité équivalente n'est due.</p><p>Aucune nouvelle décision de résiliation ou d'expulsion ne peut être prononcée sur le seul fondement de la condition d'occupation suffisante supprimée à l'article L. 621-5 ou de l'absence des déclarations et transmissions supprimées. Les procédures en cours ne peuvent être poursuivies sur ces seuls fondements. Les décisions juridictionnelles irrévocables rendues avant l'entrée en vigueur ne sont pas remises en cause, sous réserve de l'application de la loi répressive plus douce aux sanctions dans les conditions prévues par le code pénal.</p><p>Les contrats, les droits des occupants et les créances légalement nées antérieurement demeurent protégés, sans restitution générale des sommes légalement dues. Les recours et restitutions d'indus ainsi que les causes de résiliation ou d'expulsion légalement autonomes conservent leur régime et leurs garanties.</p>"
base(n,
     "Abrogation de fond et exécution de la même mesure que L. 621-5 : disparition de l’envoi au service municipal avant l’entrée et au plus tard dans les huit jours, ainsi que du mécanisme spécial de résiliation et d’expulsion pour occupation insuffisante. Ni un défaut de déclaration désormais supprimée ni la sous-occupation du présent chapitre ne fondent une nouvelle expulsion. Les décisions irrévocables et droits antérieurs ont une transition expresse ; les sanctions non définitives bénéficient de la loi plus douce dans son champ.",
     "Trois alinéas intégralement lus. Le statut source ABROGE_DIFF et la fin de validité annoncée au 1er janvier 2029 sont identifiés : la proposition anticipe la suppression si la loi entre en vigueur auparavant, sans inventer cette date d’entrée en vigueur ni présenter une suppression déjà effective. La note du 1er janvier 2020 concerne seulement la terminologie judiciaire. Les coordinations L. 621-2/L. 621-5 sont effectuées dans ce lot ; les renvois généraux de L. 651-3, L. 651-4 et L. 651-9 restent à coordonner dans leur propre article sans rétablir les anciennes déclarations. L’effet est rattaché à la même mesure que L. 621-5 : ni seconde restriction générale de louer supprimée ni seconde taxe. Les expulsions pour impayé, insalubrité ou causes autonomes et la procédure sociale après offres de relogement ne sont pas supprimées implicitement.",
     'coordination_only',
     "Les transmissions et les effets coercitifs propres au régime de L. 621-5 cessent ; ce volet d’exécution est une coordination de la même mesure, sans seconde réduction autonome comptée.",
     "Décisions irrévocables antérieures et autres causes légales de résiliation restent à leur champ. L’abrogation différée déjà annoncée pour 2029 limite la durée du gain anticipé éventuel.",
     "Aucune charge nouvelle n’est identifiée : suppression sans dossier, déclaration, garantie ni autorisation de remplacement, y compris pour les transmissions tardives.",
     proposed=p,
     repeal_scope="Transmission municipale des déclarations d’occupation avant entrée et au plus tard huit jours après location, résiliation et expulsion spécifiques pour occupation insuffisante ; fin des obligations futures et transition des instances et décisions anciennes.",
     effects=[effect('coordination', 'locations-fin-condition-occupation-suffisante',
              "Retrait des transmissions et des résiliations/expulsions servant à exécuter la condition supprimée à L. 621-5.",
              "Bailleur : transmission avant entrée et au plus tard huit jours après location ; résiliation et expulsion possibles sur le fondement du défaut d’occupation suffisante.",
              "Aucune transmission, même tardive ; aucune nouvelle décision de résiliation ou d’expulsion sur les seuls fondements retirés.",
              'legal_duty', 'Bailleurs et locataires des communes dotées du service municipal concerné.',
              "Dès l’entrée en vigueur si antérieure à l’extinction annoncée pour 2029 ; procédures en cours couvertes, décisions irrévocables et loi répressive plus douce réservées.",
              "Les bailleurs sont tenus de transmettre avant l'entrée du preneur dans les lieux et au plus tard dans les huit jours de la location ou de la sous-location, au service municipal du logement, les déclarations produites par les preneurs en application de l'article précédent.",
              "À compter de cette date, aucune transmission des déclarations du preneur au service municipal du logement n'est exigée sur le fondement du présent article, même pour une location ou sous-location conclue antérieurement.")])


base('L622-1',
     "Maintien intégral d’une transition historique : l’État reste titulaire des droits et obligations de la bourse supprimée le 1er avril 1975, sous les exceptions contractuelles précisément prévues. Abroger ce texte sans preuve d’extinction de tous les droits risquerait d’effacer une créance ou de déplacer une dette ; il n’impose aucune démarche actuelle ni nouvel organisme. Aucun allègement réel n’est démontré par une réécriture stylistique.",
     "La date de 1975 et les deux catégories de contrats et conventions ayant cessé d’avoir effet restent intégralement maintenues. L’habilitation au décret d’application n’est pas la création d’une nouvelle bourse ni d’une obligation de déclaration. Aucun élément ne démontre localement la clôture juridique de tous les droits transférés ; le texte n’est donc ni déclaré caduc ni abrogé pour masquer ce point.",
     'retained_necessary',
     "Aucun changement normatif : la continuité des droits et dettes historiques de la bourse supprimée reste juridiquement assurée.",
     "L’existence de créances encore actives n’est pas établie ; le maintien ne chiffre ni dépense future ni économie administrative.",
     "Aucune charge nouvelle n’est identifiée : aucune déclaration de créance, registre, délai de forclusion ou structure nouvelle n’est institué.")


base('L631-1',
     "Maintien intégral de l’aide de déménagement et de réinstallation sous condition de ressources, dans toutes les communes de la source et pour propriétaires, locataires et occupants de bonne foi. Le seuil territorial de plus de 10 000 habitants et l’attribution unique bornent un avantage financé publiquement ; les supprimer ou modifier sans paramètres ni financement ne constitue pas une coupe de prélèvement. Aucun dossier redondant n’est prescrit par cet article.",
     "Les deux alinéas sont conservés : Paris, communes de l’ancien département de la Seine dans les trois départements cités et communes de plus de 10 000 habitants ; ressources annuelles fixées par décret ; une seule attribution au même bénéficiaire. R. 631-1 à R. 631-3, lus dans le corpus, confirment le cadre et les cas favorables de réinstallation ou d’échange ; l’aide ne se limite pas à une sortie définitive de toute grande commune. La suppression de la reprise de L. 631-6 n’abolit aucune aide ni ne remet le compteur d’attribution unique à zéro.",
     'retained_necessary',
     "Le droit d’accès existant à l’aide reste ouvert aux demandes futures éligibles ; aucun nouveau taux, montant ou gain fiscal n’est prétendu.",
     "L’existence et le contenu de l’arrêté ministériel applicable ne sont pas intégralement fournis ; aucun montant concret d’aide n’est inventé.",
     "Aucune charge nouvelle n’est identifiée : mêmes catégories, seuil territorial et condition de ressources, sans pièce ajoutée.")

base('L631-2',
     "Maintien intégral de la faculté d’accorder l’aide de L. 631-1 aux personnes déjà propriétaires du local de réinstallation. Cette extension favorable est nécessaire pour que la propriété du nouveau logement ne ferme pas l’aide. Aucune autorisation, collecte ni prélèvement propre à cet article ne justifie une nouvelle rédaction.",
     "Renvoi exact à L. 631-1, maintenu dans ce lot ; aucune condition nouvelle d’achat, de délai ou d’ancienneté n’est introduite. La possibilité reste ouverte aux futurs propriétaires éligibles, sans restriction aux anciens bénéficiaires. L’attribution unique et les conditions générales demeurent à leur champ.",
     'retained_necessary',
     "Aucun changement : l’aide reste accessible au propriétaire du logement de réinstallation selon les conditions générales conservées.",
     "Le maintien ne crée pas un droit inconditionnel à un montant donné et ne prétend pas chiffrer la dépense publique correspondante.",
     "Aucune charge nouvelle n’est identifiée : aucune attestation ou ancienneté de propriété n’est ajoutée au texte maintenu.")

base('L631-3',
     "Maintien intégral de la faculté pour départements et communes de compléter l’aide de l’État sur leurs ressources. Ce financement volontaire supplémentaire est un avantage et non un prélèvement privé ou une dépense imposée à abolir. Le supprimer fermerait une aide encore utile aux futures demandes éligibles.",
     "L. 631-1, L. 631-4 et L. 631-5 sont maintenus ; la suppression de L. 631-6 retire la reprise spécifique mais ne supprime ni le complément ni ses conditions d’attribution autonomes. Aucun montant, transfert de financeur ou compensation obligatoire n’est créé.",
     'retained_necessary',
     "Aucun nouvel allègement compté : le complément local facultatif demeure disponible, sans dépense obligatoire ajoutée.",
     "Les délibérations locales et les montants effectivement accordés ne sont pas établis ; aucun solde public consolidé n’est démontré.",
     "Aucune charge nouvelle n’est identifiée : la seule faculté existante est conservée, sans rapport ou demande supplémentaire.")

base('L631-4',
     "Maintien intégral de la fixation par arrêté des montants et conditions de versement des primes locales. Ce cadre détermine un avantage public, sans soumettre chaque bénéficiaire ou chaque commune à un agrément individuel. Le supprimer sans texte intégral des montants et conditions pourrait faire disparaître des règles favorables ou rendre l’aide inexécutable ; aucune coupe autonome justifiée n’est donc retenue.",
     "La source, son habilitation et R. 631-1 ont été lus. La référence de L. 651-5, également lue, à cet arrêté confirme qu’une suppression mécanique affecterait la définition de la perception indue, régime distinct du simple retour dans une grande commune. L’arrêté lui-même n’est pas joint ; aucun barème ni condition nouvelle n’est reconstitué. Les articles précédents L. 631-1 à L. 631-3 sont maintenus, leur renvoi n’est pas orphelin.",
     'retained_necessary',
     "Aucun changement normatif : le fondement des montants et conditions de paiement est conservé pour éviter de fermer l’avantage.",
     "L’arrêté ministériel externe n’est pas intégralement disponible ; son éventuel allègement ne peut être déclaré accompli à partir de l’habilitation seule.",
     "Aucune charge nouvelle n’est identifiée : aucune procédure de visa, attestation ou décision individuelle supplémentaire n’est créée.")

base('L631-5',
     "Maintien intégral de l’affectation des ressources générales de l’Agence nationale de l’habitat au financement des primes de déménagement et de réinstallation. Il ne s’agit pas d’un prélèvement accessoire imposé au bénéficiaire. Le supprimer sans solution décidée retirerait le financement juridique d’un avantage préservé.",
     "Aucun taux de prélèvement ni montant de budget n’est fixé par la source. La fin de la reprise de L. 631-6 peut réduire des recouvrements, mais elle ne vaut ni économie nationale ni transfert fictif vers un autre financeur. Les engagements et l’exécution budgétaire de l’ANAH restent dans leur régime propre.",
     'retained_necessary',
     "Le financement existant de l’avantage est maintenu sans baisse de prélèvement, nouvelle affectation ou ressource de compensation inventée.",
     "Les disponibilités réelles de l’ANAH et l’effet budgétaire de l’abrogation de L. 631-6 ne sont pas chiffrés dans ce lot.",
     "Aucune charge nouvelle n’est identifiée : la même source de financement demeure et aucun taux, registre ou déclaration n’est ajouté.")


n = 'L631-6'
p = "<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi qui prononce son abrogation.</p><p>Aucun remboursement des primes prévues aux articles L. 631-1 et L. 631-3 ne peut être exigé sur le seul fondement de l'établissement de la résidence principale de leur bénéficiaire, à compter de cette entrée en vigueur, dans une des communes mentionnées à l'article L. 631-1, même si la prime a été accordée antérieurement et si cet établissement intervient dans les trois ans du déménagement.</p><p>Les créances légalement nées d'un établissement de résidence principale intervenu avant cette entrée en vigueur restent soumises aux règles antérieures, y compris la dispense de remboursement pour motif reconnu légitime, le mode de recouvrement et les autorités et juridictions compétentes pour en apprécier la légitimité. Leurs prescriptions, restitutions et recours sont préservés ; aucune restitution générale des remboursements légalement effectués n'est instituée.</p><p>Les conditions d'attribution des primes et les règles autonomes de récupération des sommes indûment perçues, notamment par fraude, demeurent applicables. Aucune déclaration, garantie ou obligation de résidence de remplacement n'est instituée.</p>"
base(n,
     "Abrogation de fond : suppression de la reprise des primes en raison du seul retour ou établissement dans une commune de L. 631-1 pendant les trois ans suivant le déménagement. Ce mécanisme contraint la mobilité personnelle ou professionnelle sans être une condition essentielle de validité de la dépense initialement éligible ; les règles de fraude et d’indu demeurent. La liberté nouvelle bénéficie aussi aux titulaires de primes anciennes pour leurs déménagements futurs. Les dettes déjà nées conservent expressément le motif légitime et leurs recours.",
     "Les deux alinéas, le délai de trois ans et la dispense pour motif reconnu légitime ont été intégralement lus. Le fait transitoire est l’établissement effectif de la résidence, non la date de recouvrement ou du titre de recette. Le recouvrement comme en matière d’impôts directs ne fait pas de la prime un impôt et n’est conservé que pour les créances anciennes légalement nées. Les aides L. 631-1 à L. 631-5 et les cas favorables de R. 631-3 restent ouverts. L. 651-5 garde son champ de fraude, distinct du retour régulier, avec coordination nécessaire de sa plage de déchéance ; aucune immunité de fraude ni nouvelle créance de remboursement n’est créée. La perte de recouvrements et le coût public net restent à mesurer, sans taxe compensatoire.",
     'material_reduction',
     "L’obligation de restituer une prime régulièrement attribuée en raison du seul lieu de résidence dans les trois ans est effectivement supprimée pour les faits nouveaux.",
     "Créances nées de retours antérieurs et récupération des indus demeurent. Le coût budgétaire de la suppression et le nombre de ménages concernés ne sont pas établis.",
     "Aucune charge nouvelle n’est identifiée : pas de résidence imposée, déclaration de retour, garantie ou nouvelle condition de prime en remplacement.",
     proposed=p,
     repeal_scope="Obligation de rembourser les primes de déménagement ou de réinstallation pour établissement de résidence dans une commune visée à L. 631-1 pendant les trois ans, pour les faits futurs ; anciennes créances avec dispense pour motif légitime et recours protégées.",
     effects=[effect('obligation_removed', 'demenagement-prime-fin-reprise-residence',
              "Suppression de la dette de restitution résultant du seul retour géographique dans les trois ans.",
              "Bénéficiaire d’une prime L. 631-1 ou L. 631-3 : remboursement intégral si résidence dans une commune visée dans les trois ans, sauf motif légitime.",
              "Pour tout établissement de résidence à compter de l’entrée en vigueur, aucune reprise sur ce seul motif, même après une prime ancienne ; fraude et indus distincts.",
              'legal_duty', 'Bénéficiaires des primes de déménagement et de réinstallation de L. 631-1 et L. 631-3.',
              "Faits de résidence futurs ; créances des faits antérieurs, motif légitime, prescriptions et recours préservés, sans remboursement général.",
              "Sauf motif reconnu légitime, le bénéficiaire des primes prévues aux articles L. 631-1 et L. 631-3 est tenu d'en rembourser le montant si, dans le délai de trois ans à compter de son déménagement, ce bénéficiaire établit sa résidence principale dans une des communes mentionnées à l'article L. 631-1.",
              "Aucun remboursement des primes prévues aux articles L. 631-1 et L. 631-3 ne peut être exigé sur le seul fondement de l'établissement de la résidence principale de leur bénéficiaire, à compter de cette entrée en vigueur, dans une des communes mentionnées à l'article L. 631-1, même si la prime a été accordée antérieurement et si cet établissement intervient dans les trois ans du déménagement.")])


n = 'L631-7'
p = replace(BY_NUMBER[n]['source_xml'],
            "Une autorisation d'urbanisme ayant pour conséquence de changer la destination de locaux à usage d'habitation ne constitue un mode de preuve valable que si elle est accompagnée d'une autorisation de changement d'usage.",
            "Lorsqu'une autorisation de changement d'usage est requise, une autorisation d'urbanisme ayant pour conséquence de changer la destination de locaux à usage d'habitation ne constitue un mode de preuve valable que si elle est accompagnée d'une autorisation de changement d'usage ou si elle tient lieu de cette autorisation dans les conditions prévues à l'article L. 425-9 du code de l'urbanisme.")
p += "<p>La reconnaissance de la décision commune prévue au cinquième alinéa s'applique aux demandes déposées à compter de l'expiration du délai de six mois suivant l'entrée en vigueur de la loi qui l'institue. À compter de cette même date, elle peut aussi être demandée pour les dossiers en cours, sans nouvelle production des pièces déjà disponibles ni reprise des délais écoulés. Les autorisations déjà délivrées conservent leur champ et leurs conditions ; une autorisation d'urbanisme antérieure ne vaut pas, par elle-même, autorisation de changement d'usage.</p>"
base(n,
     "Coordination nécessaire de la décision commune facultative retenue à L. 425-9 de l’urbanisme : la preuve du changement d’usage peut résulter du titre d’urbanisme qui en tient valablement lieu, sans exiger un second acte déjà supprimé par cette réforme. Aucune seconde réduction n’est comptée. Maintien intégral du champ communal, des logements et annexes, des périodes de référence, de la charge de preuve, des usages résultant d’autorisations, de la nullité des conventions illicites et du traitement des meublés de tourisme. L’autorisation sectorielle et ses garanties restent nécessaires à la protection du parc de logements et conformément à la coordination adoptée.",
     "Huit alinéas sources conservés dans leur ordre ; le cinquième est coordonné, puis une transition est ajoutée. La règle de preuve y est expressément bornée aux cas où une autorisation d’usage est requise, conformément au caractère facultatif prévu au premier alinéa et aux dispenses voisines : elle ne crée pas un titre obligatoire là où la réglementation n’en exige pas. Cette clarification ne compte pas comme un allègement nouveau démontré. Sont conservés 1er janvier 1970/31 décembre 1976 inclus, trente dernières années, travaux postérieurs à 1970 et preuve à la charge de celui qui invoque l’usage illicite. L. 425-9 officiel et sa proposition courante ont été lus intégralement dans le corpus : accord sectoriel, conditions, avis requis, compensation, publicité, effets personnels ou réels, absence de transfert automatique avec le permis et transition de six mois. Ce nouveau renvoi n’est pas une cible fournie par reference-targets.json ; son examen est signalé ici. L. 631-7-1 a aussi été lu, sans prétendre le réécrire. Le B du I de CGI 1406 bis a été vérifié dans l’article entier : il contient la liste communale, sans application ici de ses taux fiscaux. La note source rattache la rédaction de 2026 aux impositions de 2027 alors que le présent article est une police d’usage : articulation temporelle préexistante à vérifier dans l’article 108 de la loi 2026-103, non fourni intégralement. Elle n’est pas silencieusement corrigée ni employée pour dater la décision commune. Les dérogations futures des articles voisins, dont la résidence principale, ne sont pas fermées.",
     'coordination_only',
     "Le titre commun déjà prévu par la réforme de L. 425-9 est reconnu comme preuve des deux autorisations ; cet article ne supprime pas une seconde procédure indépendante.",
     "L’intégration dépend de l’accord sectoriel et des conditions conservées. La coordination temporelle de la loi fiscale de 2026 reste à vérifier hors de la source complète fournie.",
     "Aucune charge nouvelle n’est identifiée : pas d’acte séparé rétabli, pas de nouvelle pièce et pas de reprise des délais ; les conditions sectorielles existantes restent distinctes.",
     proposed=p,
     effects=[effect('coordination', 'changement-usage-decision-commune',
              "Reconnaissance probatoire du titre commun d’urbanisme et de changement d’usage.",
              "La preuve par autorisation d’urbanisme doit être accompagnée d’une autorisation de changement d’usage.",
              "L’autorisation d’urbanisme peut aussi faire preuve lorsqu’elle tient valablement lieu du titre d’usage selon L. 425-9.",
              'legal_duty', 'Demandeurs de travaux soumis à urbanisme et changement d’usage dans le champ du dispositif commun.',
              "Six mois après entrée en vigueur ; option pour dossiers en cours sans reprise des délais ; aucun permis ancien converti automatiquement.",
              "Une autorisation d'urbanisme ayant pour conséquence de changer la destination de locaux à usage d'habitation ne constitue un mode de preuve valable que si elle est accompagnée d'une autorisation de changement d'usage.",
              "Lorsqu'une autorisation de changement d'usage est requise, une autorisation d'urbanisme ayant pour conséquence de changer la destination de locaux à usage d'habitation ne constitue un mode de preuve valable que si elle est accompagnée d'une autorisation de changement d'usage ou si elle tient lieu de cette autorisation dans les conditions prévues à l'article L. 425-9 du code de l'urbanisme.")])


n = 'L631-7-1 A'
p = replace(BY_NUMBER[n]['source_xml'],
            "Le demandeur en atteste par la production d'une déclaration sur l'honneur.",
            "Aucune déclaration sur l'honneur ni pièce équivalente n'est exigée du demandeur pour attester cette conformité.")
p += "<p>La suppression de la déclaration sur l'honneur relative au règlement de copropriété s'applique dès l'entrée en vigueur de la loi qui l'institue aux demandes nouvelles et aux demandes en cours, sans régularisation au titre de cette seule pièce. Elle ne modifie ni les stipulations du règlement de copropriété ni les droits et recours des copropriétaires. Les autorisations déjà délivrées conservent leur champ, leur durée et les conditions légalement applicables, sous réserve de la suppression de cette seule formalité.</p>"
base(n,
     "Réforme de fond ciblée : suppression de la déclaration sur l’honneur de conformité au règlement de copropriété, sans justificatif équivalent. Cette auto-attestation ajoute une formalité sans vérifier matériellement les droits civils ; la conformité et les recours de copropriété demeurent. Maintien intégral du régime temporaire, des compétences, critères, garanties de sélection, plafonds municipaux distincts des quotas SRU et des dérogations favorables, notamment la résidence principale. Aucune reformulation stylistique des autres dispositions.",
     "Tous les alinéas et sous-alinéas du troisième paragraphe sont lus : durée des contrats, caractéristiques et localisation, modulation selon le nombre de titres, choix communal ou intercommunal, plafonds par zone, interdiction des titres permanents dans ces zones sauf compensation, durée identique inférieure à cinq ans et transparence y compris renouvellement sont conservés. L’exclusion des résidences-services utilisées comme résidence principale hors des périodes touristiques reste intégrale et ouverte aux situations futures ; L. 631-13 a été lu dans reference-targets.json. La dispense d’autorisation de courte location de la résidence principale et l’absence de changement de destination au sens de L. 151-9 sont maintenues. L. 651-2, lu dans le corpus, doit être coordonné pour que l’absence de l’ancienne déclaration ne fonde plus une sanction dans le champ transitoire, sans supprimer les infractions autonomes de changement d’usage. L’avis d’arrondissement demeure conformément à la coordination de L. 425-9 ; cette coupe ne concerne pas l’autorisation sectorielle elle-même ni les formalités autonomes du code du tourisme. Aucun nombre de nuitées, durée maximale ou déclaration nouvelle n’est inventé.",
     'material_reduction',
     "Une auto-attestation obligatoire est effectivement retirée pour les demandes nouvelles et en cours ; la conformité civile et les régimes d’autorisation et de dispense restent intacts.",
     "Les formalités autonomes de tourisme et les décisions locales de contingentement subsistent. Le coût de cette pièce évitée n’est pas chiffré et ne vaut pas abolition de l’autorisation.",
     "Aucune charge nouvelle n’est identifiée : ni attestation, ni déclaration, ni pièce équivalente de remplacement ; aucune condition nouvelle de dérogation ou de renouvellement.",
     proposed=p,
     removed=["Production par le demandeur d’une déclaration sur l’honneur attestant la conformité du changement d’usage au règlement de copropriété."],
     effects=[effect('obligation_removed', 'meubles-tourisme-fin-attestation-copropriete',
              "Suppression de l’auto-attestation jointe à la demande d’autorisation temporaire.",
              "Le demandeur doit produire une déclaration sur l’honneur de conformité au règlement de copropriété.",
              "Aucune auto-attestation ni pièce équivalente ; conformité, droits et recours civils conservés.",
              'legal_duty', 'Personnes physiques ou morales sollicitant l’autorisation temporaire visée par cet article.',
              "Dès l’entrée en vigueur, demandes en cours comprises ; pas de régularisation de cette pièce ni remise en cause des titres acquis.",
              "Le demandeur en atteste par la production d'une déclaration sur l'honneur.",
              "Aucune déclaration sur l'honneur ni pièce équivalente n'est exigée du demandeur pour attester cette conformité.")])


# Contrôles des cibles imposées : les trois articles du travail sont bien lus,
# mais aucun ne régit une indemnité d'expropriation ou un contrat de services.
LABOR_CONTEXT = {
    'L615-6': "La procédure de carence porte sur l’immeuble, l’expertise et la saisine du tribunal, non sur la rupture de l’emploi d’un syndic ou d’un occupant. Les deux mois de recours et le mois de participation publique gardent leur fonction propre.",
    'L615-7': "Le délai d’au moins deux mois après publication protège la prise de possession d’un bien exproprié ; il ne s’agit pas du préavis de licenciement. Les titulaires de baux commerciaux ou professionnels sont indemnisés au titre de leurs droits immobiliers.",
    'L615-8': "L’indemnité est celle d’une expropriation et ses modalités sont celles du code de l’expropriation. La conservation de l’immeuble et les travaux affectent l’évaluation du bien, non la rémunération ou l’ancienneté d’un salarié.",
    'L615-9': "L’indemnité d’occupation versée par le propriétaire occupant ouvre droit aux allocations de logement du 2° de L. 821-1. Le bénéficiaire n’est pas défini comme salarié et le texte ne fixe aucune indemnité de rupture.",
    'L615-10': "La concession à un opérateur, la redevance mensuelle et l’indemnité de remise en copropriété relèvent de la gestion immobilière. La durée expérimentale de vingt ans et le plan de travaux ne fixent pas la durée de l’emploi des salariés de l’opérateur.",
    'L631-7-1 A': "L’autorisation temporaire règle la location touristique et les contrats de location sont des baux, non des contrats d’embauche. Le maintien de la durée des titres inférieure à cinq ans dans les zones contingentées ne crée aucun CDD de travail."
}

LABOR_RULES = {
    'L1234-1': "La source prévoit un préavis de licenciement variable selon l’ancienneté, avec règles plus favorables ; la proposition prévoit quinze jours calendaires pour les contrats nouveaux et conserve les règles anciennes dans leur champ. Ce préavis individuel et sa notification ne sont pas applicables à la règle immobilière examinée.",
    'L1221-2': "La source distingue CDI de droit commun et CDD autorisés ; la proposition impose un contrat d’emploi indéterminé pour les nouvelles embauches, sans terme tiré d’une mission ou formation, et préserve les contrats antérieurs. Cette réforme ne transforme ni un bail, ni une concession immobilière, ni une procédure publique en contrat privé de travail.",
    'L1234-9': "La source ouvre l’indemnité ordinaire après huit mois sous ses exceptions ; la proposition retient un an à la fin effective, préavis inclus, puis 0,20 mois par année totale au prorata des mois complets et plafond de six mois, à l’initiative de l’employeur, avec transition des anciens droits. Ni ce seuil ni ce calcul salarial ne peuvent être importés dans le dispositif immobilier."
}

SPECIAL_CHECKS = {
    ('L615-6', 'L615-8'): "Le renvoi du VI à L. 615-7 à L. 615-10 comprend les règles de transfert et d’indemnisation de L. 615-8. La vue fournie est la source officielle seule : la proposition de ce lot coordonne expressément les arrêtés actuels et anciens sans modifier les renvois de calcul au code de l’expropriation. La subsistance du syndicat pour liquider ses dettes n’écarte ni l’indemnisation ni ces règles ; aucune ancienneté salariale n’intervient.",
    ('L615-6', 'L615-9'): "L. 615-9, fourni en source officielle seule, ouvre les allocations de logement sur l’indemnité d’occupation versée à l’expropriant par les propriétaires occupants. Le renvoi global du VI ne suspend pas cette aide et la proposition la maintient intégralement pour les bénéficiaires futurs. Ni notification d’un licenciement ni seuil d’un an ne conditionnent cette ouverture.",
    ('L615-6', 'L615-7'): "Le II vise L. 615-10 pour l’expropriation partielle et le VI réserve L. 615-7 à L. 615-10 ; le V reste bien le projet approuvé que L. 615-7 vise pour la déclaration d’utilité publique. La vue de L. 615-7 est une source officielle, maintenue dans ce lot. Indemnité provisionnelle, publication, deux mois avant possession et continuation judiciaire dans le mois ne sont pas remplacés par les quinze jours d’emploi.",
    ('L615-6', 'L615-10'): "L. 615-10 est visé au II pour l’expropriation des parties communes et au VI pour les suites de la carence. Sa source officielle prévoit vingt ans depuis la loi du 24 mars 2014 ; la proposition de ce lot ne supprime que la mise à jour triennale du plan, en maintenant la servitude, les redevances, aides, responsabilités et la référence au V de L. 615-6. Les deux renvois restent cohérents et ne bornent aucun contrat de travail.",
    ('L615-7', 'L615-10'): "La mention de l’opérateur au premier alinéa et des parties communes aux 1°, 2° et 5° correspond à l’expérimentation de L. 615-10. La vue cible est la source officielle seule et non un ancien brouillon. Le nouveau corps conserve l’expropriation, la possibilité de désigner l’opérateur et tous les droits attachés, sans prolonger les vingt ans. La périodicité documentaire supprimée ne modifie pas le bénéficiaire de l’expropriation.",
    ('L615-8', 'L615-7'): "Le premier alinéa vise exactement l’arrêté de L. 615-7, qu’il s’agisse de l’ordonnance d’expropriation ou d’une cession amiable postérieure. La vue officielle de L. 615-7 et son maintien dans ce lot préservent les cinq mentions, la provision au moins égale à l’évaluation des domaines et les notifications. La coordination de police à L. 615-8 ne modifie pas la date de l’arrêté ni le délai de possession ; aucune notification salariale n’est pertinente.",
    ('L615-10', 'L615-7'): "Le V de L. 615-10 renvoie à L. 615-7 pour une expropriation totale consécutive à un déséquilibre important. Cette cible, fournie en source officielle seule et maintenue, conserve utilité publique, cessibilité, indemnité provisionnelle, publication et notifications. Le nouveau projet reste approuvé selon le V de L. 615-6 ; le délai immobilier d’au moins deux mois et le mois de poursuite ne sont pas un préavis d’emploi de quinze jours.",
    ('L631-7-1 A', 'L631-13'): "Le sous-alinéa des résidences-services renvoie à la définition de L. 631-13 : logements autonomes avec services non individualisables, services individualisables souscrits séparément. Son préavis de résiliation plafonné à un mois protège le contrat de prestations de services et ne relève pas de L. 1234-1. La dérogation de comptage touristique reste intégrale lorsque le logement est une résidence principale hors périodes touristiques ; aucune ancienneté d’emploi n’est ajoutée. La vue ne comporte aucune proposition nouvelle."
}

for number, row in ANSWER.items():
    source = BY_NUMBER[number]
    source_key = source['code_id'] + '|' + source['source_id']
    row['reference_checks'] = []
    for key in REFS['requirements'][source_key]:
        target = REFS['targets'][key]
        tn = target['number']
        if target['code_id'] == 'LEGITEXT000006072050':
            assessment = LABOR_CONTEXT[number] + ' ' + LABOR_RULES[tn]
        else:
            assessment = SPECIAL_CHECKS[(number, tn)]
        row['reference_checks'].append(dict(target_key=key,
                                            view_sha256=target['view_sha256'],
                                            assessment=assessment))

ANSWER['L615-6']['reason'] += " L’ouverture de la saisine étend aussi le champ des procédures et notifications obligatoires, voire des suites locales du V : cette contrepartie est recensée sous mixed, sans prétendre à une économie nette démontrée."
ANSWER['L615-10']['review_notes'] += " Vérification facultative du renvoi existant du IV : L. 211-4 de l’urbanisme est lu intégralement, source et proposition distinctes. La délibération communale motivée de préemption renforcée garde son fondement autonome ; la proposition cible retire le seul pouvoir préfectoral fondé sur la carence SRU. La délégation à l’opérateur ne fait pas renaître ce pouvoir retiré."
ANSWER['L631-7-1 A']['review_notes'] += " Le troisième alinéa de L. 151-9 de l’urbanisme a été lu : il vise les règles de destination et de nature des constructions ; le renvoi maintenu est cohérent. Les baux meublés de L. 632-1, également lus en entier pour L. 631-7, restent des contrats de logement et ne deviennent pas des CDD d’emploi."


def validate():
    from html.parser import HTMLParser
    allowed = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())

    class Validator(HTMLParser):
        def handle_starttag(self, tag, attrs):
            assert tag in allowed, tag
            for key, value in attrs:
                assert key in ('rowspan', 'colspan') and value.isdigit(), (key, value)

    assert len(SOURCES) == len(ANSWER) == 24
    for a in SOURCES:
        n = a['number']
        r = ANSWER[n]
        for key in ('code_id', 'source_id', 'source_sha256', 'number'):
            assert r[key] == a[key], (n, key)
        assert r['reason'] and r['review_notes']
        si = r['substantive_impact']
        assert si['version'] == 1
        cut_kinds = {'tax_removed', 'tax_reduced', 'obligation_removed',
                     'obligation_merged', 'authorization_removed', 'regime_merged',
                     'deadline_reduced', 'compliance_cost_reduced', 'relief_extended'}
        added_kinds = {'tax_increased', 'obligation_added', 'deadline_increased',
                       'complexity_added'}
        kinds = {e['kind'] for e in si['effects']}
        if si['classification'] == 'material_reduction':
            assert kinds & cut_kinds, (n, 'Une réduction requiert une coupe concrète')
            assert not kinds & added_kinds, (n, 'Les ajouts imposent la classe mixed')
        if kinds & cut_kinds and kinds & added_kinds:
            assert si['classification'] == 'mixed', (n, 'Coupes et ajouts doivent être recensés ensemble')
        if kinds and kinds <= {'coordination', 'relief_preserved'}:
            assert si['classification'] == 'coordination_only', (n, 'Ne pas recompter une coordination')
        for key in ('assessment', 'scope_limitations', 'new_burdens_review'):
            assert len(si[key]) >= 40, (n, key)
        if r['status'] == 'retained_unchanged':
            assert r['proposed_xml'] is None
            assert r['classification'] == si['classification'] == 'retained_necessary'
            assert si['effects'] == []
        else:
            assert r['status'] == 'rewrite_draft'
            assert r['proposed_xml'] != a['source_xml']
            Validator().feed(r['proposed_xml'])
        if a.get('benefit_check_required'):
            assert len(r['benefit_review']) >= 100
        if r.get('change_type') == 'full_repeal':
            assert plain(r['proposed_xml']).startswith(('Le présent article est abrogé', 'Abrogé'))
            assert r['repeal_policy_id'] == 'editorial_direction_2026_10_19'
            assert len(r['repeal_scope']) >= 30
        if r.get('change_type') == 'normative_reduction':
            assert r['reform_policy_id'] == 'editorial_direction_2026_10_19'
            assert all(len(s) >= 30 for s in r['removed_provisions'])
        for e in si['effects']:
            assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)+', e['measure_id'])
            assert 6 <= len(e['measure_id']) <= 96
            assert e['kind'] in ('tax_removed', 'tax_reduced', 'obligation_removed', 'obligation_merged',
                                 'authorization_removed', 'regime_merged', 'deadline_reduced',
                                 'compliance_cost_reduced', 'tax_increased', 'obligation_added',
                                 'deadline_increased', 'complexity_added', 'financing_transfer',
                                 'payment_deferred', 'relief_extended', 'relief_preserved', 'coordination')
            assert e['unit'] in ('percent', 'euro', 'legal_duty', 'regime', 'calendar_days',
                                 'working_days', 'financing', 'other')
            for k, v in e.items():
                assert isinstance(v, str) and v, (n, k)
            for q, body in [('source_quote', a['source_xml']), ('proposed_quote', r['proposed_xml'])]:
                assert len(e[q]) >= 12
                assert e[q] in plain(body), (n, q, e[q])
        source_key = a['code_id'] + '|' + a['source_id']
        checks = r['reference_checks']
        assert [c['target_key'] for c in checks] == REFS['requirements'][source_key]
        for c in checks:
            assert c['view_sha256'] == REFS['targets'][c['target_key']]['view_sha256']
            assert len(c['assessment']) >= 80


if __name__ == '__main__':
    validate()
    rows = [ANSWER[a['number']] for a in SOURCES]
    Path('answer.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'articles': len(rows), 'statuses': {
        s: sum(r['status'] == s for r in rows)
        for s in ('rewrite_draft', 'retained_unchanged')},
        'full_repeals': [r['number'] for r in rows if r.get('change_type') == 'full_repeal'],
        'reference_checks': sum(len(r['reference_checks']) for r in rows)}, ensure_ascii=False))
