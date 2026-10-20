import json
import re
from pathlib import Path
from html import unescape

ROOT = Path(__file__).resolve().parent
sources = json.loads((ROOT / 'source.json').read_text())
refs = json.loads((ROOT / 'reference-targets.json').read_text())
by_number = {s['number']: s for s in sources}
answers = {}


def paragraphs(n):
    return re.findall(r'<p>.*?</p>', by_number[n]['source_xml'], re.S)


def p(text):
    return '<p>' + text + '</p>'


def effect(kind, measure_id, description, before, after, unit,
           population, transition, replacement, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit,
                affected_population=population, conditions_and_transition=transition,
                replacement_or_new_burdens=replacement,
                source_quote=source_quote, proposed_quote=proposed_quote)


def add(n, xml, reason, notes, classification, assessment, limitations, burdens,
        effects=None, removed=None, benefit=None):
    s = by_number[n]
    a = {k: s[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    a.update(proposed_xml=xml, reason=reason, review_notes=notes,
             status='retained_unchanged' if xml is None else 'rewrite_draft')
    if xml is None:
        a['classification'] = 'retained_necessary'
    a['substantive_impact'] = dict(
        version=1, classification=classification, assessment=assessment,
        scope_limitations=limitations, new_burdens_review=burdens,
        effects=effects or [])
    if removed:
        a.update(change_type='normative_reduction',
                 reform_policy_id='editorial_direction_2026_10_19',
                 removed_provisions=removed)
    if benefit:
        a['benefit_review'] = benefit
    a['reference_checks'] = []
    answers[n] = a
    return a


def retain(n, reason, notes, assessment, limitations, benefit):
    return add(n, None, reason, notes, 'retained_necessary', assessment,
               limitations,
               "Aucune charge nouvelle n'est identifiée : la source entière est maintenue sans ajout de donnée, de registre, de délai ni de condition. Aucun solde global des codes n'est chiffré.",
               benefit=benefit)


# L432-1 : ouverture de la gestion, sans importer une clause de fonction.
n = 'L432-1'
xml = ''.join([
    p("Les communes peuvent construire des habitations pour familles nombreuses répondant aux conditions prévues par l'article L. 411-1."),
    p("Ces habitations peuvent également être construites par les offices publics ou par les sociétés anonymes d'habitations à loyer modéré pour le compte des communes."),
    p("Les habitations mentionnées aux deux alinéas précédents peuvent être gérées par tout organisme d'habitations à loyer modéré mentionné à l'article L. 411-2 habilité à exercer cette activité. Pour la construction de ces habitations, les communes bénéficient des dispositions des articles L. 431-1, L. 431-2 et L. 443-18 ainsi que des dispositions réglementaires régissant les prêts et aides légalement ouverts à ces opérations."),
    p("Les droits à prêts, aides, bonifications et garanties légalement ouverts à ces opérations demeurent applicables aux opérations futures qui en remplissent les conditions. Les contrats valablement conclus, les aides accordées, les créances et les droits des occupants antérieurs à l'entrée en vigueur de la présente loi sont préservés. L'ouverture de la gestion à d'autres organismes habilités s'applique à compter de cette entrée en vigueur, sans résiliation ni transfert d'office des contrats en cours.")])
add(n, xml,
    "Réforme de fond : supprimer l'exclusivité de gestion réservée aux offices et sociétés anonymes, en ouvrant aux autres organismes HLM déjà habilités. Coordination distincte : retirer le renvoi financier à L442-7, dont la norme actuelle concerne un bail lié à une fonction, et remplacer la plage réglementaire non retrouvée par le champ des prêts et aides effectivement applicables. Les trois alinéas d'origine restent identifiables ; une transition est ajoutée.",
    "L411-1, L411-2, L431-1, L431-2 et L443-18 lus dans le corpus public. Le renvoi à L411-2 est nouveau dans cet article ; cette cible n'est pas fournie dans reference-targets et a été lue au corpus. L442-7 lu en entier dans reference-targets : aucune clause de fonction n'est créée par cette construction communale. R431-1 à R431-6 ne figurent pas dans le corpus fourni : leur contenu historique et leur éventuelle concordance ne sont pas établis. La garantie des avantages légalement ouverts ne réactive aucun texte abrogé ; cette filiation réglementaire ne compte pas comme volet historique achevé. L431-1 conserve ses hypothèques et L443-18 son plafond d'intérêts moratoires. Aucun contrat de travail ni délai locatif n'est modifié.",
    'material_reduction',
    "La comparaison avec la source entière démontre une ouverture réelle du choix du gestionnaire HLM. Le nettoyage des renvois n'est pas compté comme une baisse de taxe ni comme une nouvelle ouverture de prêt.",
    "Les compétences de chaque catégorie d'organisme restent opposables. La portée historique des six références réglementaires absentes reste à documenter ; aucun effet budgétaire ou tarifaire n'est établi.",
    "Aucune charge nouvelle n'est identifiée : les habilitations de gestion sont celles déjà applicables aux organismes et aucune déclaration ni autorisation de remplacement n'est instaurée. Les contrats en cours ne sont pas transférés d'office.",
    [effect('obligation_removed', 'logements-communaux-ouverture-gestion-hlm',
            "Retrait de l'exclusivité légale de gestion au profit de deux seules formes d'organismes.",
            "Gestion limitée aux offices publics HLM et sociétés anonymes HLM.",
            "Choix de tout organisme HLM déjà habilité à gérer ces habitations, sans agrément supplémentaire.",
            'legal_duty', "Communes construisant pour les familles nombreuses et organismes HLM habilités.",
            "Dès l'entrée en vigueur ; les contrats et droits des occupants existants sont conservés.",
            "Aucun dépôt ni contrôle préalable nouveau ; compétences légales existantes maintenues.",
            "ne peuvent être gérées que par des offices publics d'habitations à loyer modéré ou des sociétés anonymes d'habitations à loyer modéré",
            "peuvent être gérées par tout organisme d'habitations à loyer modéré mentionné à l'article L. 411-2 habilité à exercer cette activité")],
    ["L'exclusivité de gestion des habitations communales au profit des seuls offices publics et sociétés anonymes HLM est supprimée."],
    "Les possibilités de construction pour familles nombreuses et de construction pour compte communal sont conservées. Les droits aux prêts, aides, bonifications et garanties légalement ouverts restent accessibles aux opérations futures éligibles ; les contrats et les droits des occupants existants sont sauvés. Le renvoi à L442-7 actuel ne constitue pas un avantage de financement.")

retain('L432-2',
       "Maintien intégral nécessaire du régime de financement et de protection patrimoniale des coopératives : accès aux prêts et au régime fiscal HLM, limitation des contributions de chaque associé à son lot, prise en charge des défaillances et affectation non distribuable des réserves. Ces affectations protègent les fonds sociaux et les associés ; elles ne sont pas de simples formalités ni l'IS annuel réformé.",
       "CGI1378 sexies et L261-10 lus en entier : même régime fiscal HLM et faculté de vente à terme confirmés, sans assimilation à un contrat de travail. Dans L443-1 à L443-6, les articles actifs L443-1, L443-2, L443-4 et L443-6 ont été lus ; L443-3 et L443-5 ne figurent pas au corpus. La plage vise ses dispositions encore applicables, sans reconstitution des articles absents. Les garanties des prêts, les droits fiscaux et la non-distribution des réserves restent distincts du nouvel IS à la distribution et de la suppression des droits de succession.",
       "Aucune taxe ni autorisation autonome supprimable n'est instituée ici. Retirer les plafonds de contribution, la garantie de défaillance ou la dévolution sociale fragiliserait les associés ou détournerait les prêts aidés ; aucun changement normatif n'est revendiqué.",
       "Le régime fiscal résulte aussi du CGI, dont les taux et exonérations ne sont pas réécrits par cet article ; les textes réglementaires de crédit restent à leur champ propre.",
       "L'accès aux prêts, la vente à terme, l'identité de régime fiscal avec les HLM, la contribution proportionnée au lot et la prise en charge des dettes restent ouverts aux futures coopératives et opérations éligibles. Les réserves et bénéficiaires de liquidation sont intégralement maintenus.")

for n, subject, regulation in [
    ('L432-3', "Les sociétés de bains-douches agréées dans les conditions prévues à l'article L. 422-5", ''),
    ('L432-4', "Les sociétés et unions de sociétés mutualistes et les associations reconnues d'utilité publique ayant reçu des prêts de l'Etat au titre de la législation sur les habitations à loyer modéré, dans les mêmes conditions que les sociétés de crédit immobilier", ', ainsi que des bonifications prévues à l\'article R. 431-49')
]:
    xml = p(subject + (", " if n == 'L432-4' else " ") + "bénéficient des dispositions des articles L. 431-1, L. 431-2 et L. 443-18" + regulation + ". Les dispositions réglementaires régissant les prêts et aides légalement ouverts à ces organismes s'appliquent dans leur champ propre.")
    xml += p("Les droits à prêts, aides, bonifications et garanties légalement ouverts à ces organismes demeurent accessibles aux opérations futures qui en remplissent les conditions. Les prêts, contrats, aides, garanties et créances valablement constitués avant l'entrée en vigueur de la présente loi conservent le régime qui leur est applicable, ainsi que les droits à restitution et les recours correspondants.")
    add(n, xml,
        ("Coordination nécessaire, sans nouvelle réduction revendiquée : conserver l'accès aux financements et leurs garanties, mais retirer la référence à L442-7 actuel, étrangère aux prêts. "
         + ("L'agrément initial de L422-5 est conservé comme qualification d'accès à des fonds aidés, non remplacé par une déclaration sans contrôle des conditions de fond." if n == 'L432-3' else "La bonification d'intérêts de R431-49 est expressément conservée ; aucune condition supplémentaire n'est ajoutée aux organismes ayant reçu les prêts visés.")),
        "L431-1, L431-2, L443-18 et la cible L442-7 ont été lus en entier. "
        + ("L422-5 a également été lu : agrément administratif et clauses types statutaires. R431-1 à R431-6 sont absents du corpus." if n == 'L432-3' else "R431-49 a été lu : bonifications pour toutes les opérations de L411-1, notamment foncier et grosses réparations. R431-1 à R431-6 et R431-50 à R431-56 sont absents du corpus.")
        + " Le contenu historique de ces références absentes n'est pas reconstitué : la clause de maintien couvre les avantages légalement applicables et les anciens prêts, sans rouvrir un dispositif éteint. La concordance historique reste une lacune documentaire, non un volet achevé. L442-7 ne peut plus être présenté comme un avantage financier général, et son champ locatif autonome n'est pas modifié.",
        'coordination_only',
        "L'article conserve ses bénéficiaires et les avantages financiers légalement ouverts ; seul le raccordement à des dispositions actives est corrigé. La clause de fonction actuelle de L442-7 ne devient pas une condition de financement.",
        "Aucune baisse de taux, de coût d'emprunt ou de délai n'est démontrée ; les concordances des références réglementaires absentes restent à vérifier sans les attribuer à SRU.",
        "Aucune charge nouvelle n'est identifiée : aucune déclaration, agrément de remplacement, pièce ni condition financière nouvelle n'est créée ; les qualifications d'accès maintenues sont celles de la source.",
        [effect('coordination', 'prets-hlm-renvois-financiers-anciens',
                "Suppression du raccordement impropre à la clause de fonction et maintien du champ des financements applicables.",
                "Liste financière comprenant L442-7 et des plages réglementaires non retrouvées.",
                "Renvois financiers actifs, garanties de maintien des droits applicables et des anciens prêts.",
                'other', subject + '.', "Application à l'entrée en vigueur, avec sauvegarde des créances et aides anciennes et des futures opérations éligibles.",
                "Aucune démarche de remplacement ni extension de la clause de fonction.",
                "bénéficient des dispositions des articles L. 431-1, L. 431-2, L. 442-7, L. 443-18",
                "bénéficient des dispositions des articles L. 431-1, L. 431-2 et L. 443-18")],
        benefit="Les prêts et garanties des organismes désignés, le plafonnement d'intérêts moratoires de L443-18 et les bonifications légalement ouvertes sont maintenus pour les opérations futures recevables comme pour les droits anciens. Aucune exonération fiscale n'est retirée ; la clause de fonction de L442-7 actuel n'est pas un avantage de prêt.")

retain('L432-6',
       "Maintien nécessaire du contrôle ANCOLS limité aux opérations financées par les prêts désignés. L'article n'impose aucun agrément préalable, rapport annuel ou justificatif autonome à supprimer ; le contrôle de l'emploi des fonds aidés et des garanties reste essentiel.",
       "La référence au 3° de L831-1 porte sur le champ des prêts à la construction ou amélioration ouvrant l'aide au logement, non sur les quotas de L302-5. L'article ne crée ni prélèvement ni double organisme de contrôle. La suppression des obligations de quota ou des formalités d'agrément ciblées ne vaut pas suppression de la surveillance des fonds publics.",
       "Le contrôle est conservé dans son périmètre de financement, sans nouvelle transmission périodique. Aucun gain de simplification ou de prélèvement n'est attribué à ce maintien.",
       "Les procédures et pouvoirs de contrôle sont régis par d'autres articles et ne sont pas réputés tous examinés ou allégés par ce maintien.",
       "Les prêts de la caisse de prêts HLM et de la Caisse des dépôts ne sont ni fermés ni soumis à une condition nouvelle. Le contrôle n'est pas une exonération ; son maintien protège la destination des avantages de financement, y compris pour les futures opérations éligibles.")

retain('L433-1',
       "Maintien intégral de l'assujettissement des organismes privés HLM aux règles de commande publique. Supprimer globalement ce raccordement effacerait sans coordination les garanties de concurrence, de transparence et les contraintes européennes applicables ; l'article ne crée pas de procédure supplémentaire à celles du code de la commande publique.",
       "Le code de la commande publique est extérieur aux cinq codes et son texte n'est pas joint ici. Les seuils, exclusions et procédures simplifiées qu'il prévoit ne sont ni supprimés ni durcis. Aucune exemption générale des organismes HLM ne peut être présumée compatible avec les directives marchés publics et concessions à partir de ce seul renvoi.",
       "Aucune charge autonome redondante n'est retirée : le texte fixe le raccordement nécessaire au droit des marchés, avec ses exceptions propres. Aucun effet matériel supplémentaire n'est revendiqué.",
       "La simplification éventuelle des procédures exige un examen des dispositions nationales et européennes de commande publique, qui n'est pas présenté comme réalisé dans ce lot.",
       "Le renvoi conserve le champ, les seuils et les dérogations plus favorables de la commande publique ; il ne crée aucune autorisation supplémentaire ni ne ferme une dispense existante aux futures opérations éligibles.")

n = 'L433-2'
ps = paragraphs(n)
old = "Cette vente est soumise à l'autorisation du représentant de l'Etat dans le département du lieu de l'opération et subordonnée au respect, par l'organisme d'habitations à loyer modéré, de critères prenant notamment en compte la production et la rénovation de logements locatifs sociaux, définis à l'article L. 445-1 du présent code."
new = "Cette vente n'est soumise à aucune autorisation particulière du représentant de l'Etat dans le département au titre du présent article. Elle reste subordonnée au respect, par l'organisme d'habitations à loyer modéré, de critères prenant notamment en compte la production et la rénovation de logements locatifs sociaux, définis à l'article L. 445-1 du présent code."
assert old in ps[4]
ps[4] = ps[4].replace(old, new)
xml = ''.join(ps) + p("La suppression de l'autorisation s'applique aux ventes conclues à compter de l'entrée en vigueur de la présente loi, y compris lorsque la demande d'autorisation était en cours à cette date. Aucun dépôt, déclaration ou visa ne remplace cette autorisation. Les ventes déjà conclues, les aides, les droits des acquéreurs et des tiers et les créances antérieurement constitués sont préservés. Cette suppression ne dispense ni des règles de la commande publique dans leur champ propre, ni des garanties légales de la vente d'immeubles à construire ou à rénover.")
add(n, xml,
    "Réforme de fond : suppression de l'autorisation préfectorale particulière préalable à la vente des logements privés du programme mixte. Toutes les conditions de fond, la majorité sociale du programme, la limite de 30 %, les terrains admissibles, le seuil de 50 000 habitants, les critères L445-1 et la comptabilité SIEG sont conservés, ainsi que les acquisitions des quatre premiers alinéas.",
    "L261-1, L261-12 et L261-14 lus en entier dans les cibles : vente immobilière à terme ou VEFA, protection des paiements et plafond forfaitaire de 10 % en résolution, sans lien avec une durée d'emploi ni une indemnité de licenciement. L411-2 lu pour la comptabilité des aides SIEG. Les exigences européennes de marchés et de compensation de service public subsistent. Les notes de la source relatives aux impositions 2027 et à la vacance sont conservées comme notes documentaires : elles ne datent pas l'entrée en vigueur de notre suppression d'autorisation. Aucun nouveau renvoi au droit du travail n'est introduit.",
    'material_reduction',
    "Une autorisation administrative est effectivement retirée pour les ventes futures dans le champ défini par l'article, sans déclaration de remplacement. Ni le plafond de ventes privées ni la protection des fonds sociaux ne sont réduits.",
    "La réforme ne dispense pas des permis, des règles de commande publique, des garanties VEFA ou du respect des aides SIEG. Aucun gain de délai moyen ou produit budgétaire n'est calculé.",
    "Aucune charge nouvelle n'est identifiée : les critères de fond et la séparation comptable figuraient déjà dans la source ; aucune attestation, registre ou transmission de remplacement n'est ajouté.",
    [effect('authorization_removed', 'ventes-mixtes-hlm-fin-autorisation-prefet',
            "Vente des logements privés d'un programme majoritairement social sans autorisation préfectorale spéciale.",
            "Autorisation du préfet du lieu de l'opération requise en plus des conditions de vente, à hauteur maximale de 30 % du programme.",
            "Aucune autorisation particulière au titre de L433-2 ; limite de 30 %, terrains admissibles et critères sociaux inchangés.",
            'legal_duty', "Organismes HLM vendeurs et acquéreurs privés des logements de ces programmes mixtes.",
            "Ventes conclues dès l'entrée en vigueur, demandes pendantes comprises ; contrats et créances anciens préservés.",
            "Aucune déclaration ni visa de remplacement ; contrôles autonomes maintenus.",
            "Cette vente est soumise à l'autorisation du représentant de l'Etat dans le département du lieu de l'opération",
            "Cette vente n'est soumise à aucune autorisation particulière du représentant de l'Etat dans le département au titre du présent article.")],
    ["L'autorisation préfectorale particulière préalable à la vente de logements privés dans le programme mixte défini au cinquième alinéa est supprimée."],
    "Les facultés d'acquisition de logements-foyers, résidences hôtelières sociales, ouvrages d'autres organismes et logements de programmes de tiers sont conservées. La faculté de vente mixte reste ouverte aux futurs programmes remplissant les conditions, sans retrait d'aides ni des garanties de paiement des acquéreurs.")

retain('L441',
       "Maintien intégral des principes de droit au logement, d'égalité d'accès, de prise en compte du handicap et des faibles revenus, ainsi que de la faculté d'adapter les loyers. Cet article ne fixe ni quota communal SRU, ni rattrapage, ni nouvelle taxe ou autorisation ; le supprimer retirerait des protections et une souplesse tarifaire utiles.",
       "Ne pas assimiler la diversité de la demande et l'accès à l'ensemble des secteurs à un rétablissement des quotas de L302-5. Les loyers différents demeurent une faculté, non une hausse imposée. L'interdiction du refus fondé seulement sur l'absence de lien communal est intégralement conservée. Aucun CDD, seuil d'ancienneté ou préavis n'est visé.",
       "Aucun changement normatif : les principes d'accès et la souplesse des loyers sont nécessaires. Leur maintien ne constitue ni une simplification ni une baisse de prélèvement.",
       "Les règles opérationnelles d'attribution et les plafonds de ressources se trouvent dans les articles de la section ; le maintien n'atteste pas l'examen de toutes leurs mesures réglementaires.",
       "L'accès des ménages modestes, des personnes handicapées et des ménages aux revenus les plus faibles, la faculté de loyers adaptés et la protection des demandeurs sans lien communal bénéficient aussi aux futures demandes recevables, sans condition nouvelle.")

n = 'L441-1-1'
ps = paragraphs(n)
assert len(ps) == 10
ps[0] = ps[0].replace("conclure pour trois ans un accord collectif intercommunal", "conclure un accord collectif intercommunal")
ps[3] = ps[3][:-4] + "Les signataires peuvent fixer librement la durée de l'accord et les modalités de sa modification.</p>"
ps[4] = p("L'accord collectif intercommunal n'est soumis ni à l'avis préalable du comité responsable du plan départemental d'action pour le logement et l'hébergement des personnes défavorisées ni à un agrément du représentant de l'Etat dans le département.")
ps[5] = p("L'accord collectif intercommunal n'impose pas la création d'une commission de coordination distincte des commissions d'attribution prévues à l'article L. 441-2. Ses signataires peuvent organiser une concertation sans se substituer aux décisions de ces commissions.")
ps[6] = p("Dès sa conclusion, l'accord collectif intercommunal se substitue, sur le territoire où il s'applique, à l'accord collectif départemental prévu à l'article L. 441-1-2.")
xml = ''.join(ps) + p("Ces simplifications s'appliquent aux accords conclus ou modifiés à compter de l'entrée en vigueur de la présente loi et aux projets d'accords en cours, sans nouvel avis, agrément ou dépôt de remplacement. Les accords valablement conclus, leurs engagements d'attribution et d'accompagnement, les aides accordées et les droits des demandeurs demeurent applicables. Les commissions de coordination existantes peuvent être maintenues par leurs signataires, sans obligation légale de conservation ni préjudice des conventions valablement conclues.")
add(n, xml,
    "Réforme de fond : supprimer la durée légale imposée de trois ans, l'avis du comité départemental, l'agrément préfectoral conditionnant la substitution de l'accord et la commission de coordination obligatoirement distincte, son examen préalable des dossiers, sa composition imposée et son règlement intérieur. La durée peut être librement fixée par les signataires ; les engagements annuels prioritaires, les moyens d'accompagnement et tous les mécanismes d'exécution des trois derniers alinéas sont conservés.",
    "Les dix alinéas initiaux gardent leurs positions ; transition au onzième. L441-2 lu : il conserve la commission qui attribue nominativement les logements. L441-1, L441-1-5, L441-1-6 et L441-2-3 lus : les accords prioritaires ne sont pas les quotas communaux de production SRU. L441-1-6 conserve, hors lot, sa convention et sa commission propres ; leur éventuel allègement exige une coordination distincte, non prétendue achevée. L'accord intercommunal remplace l'accord départemental dès conclusion sans agrément ni déclaration substitutive. Les droits DALO et la consultation des maires au neuvième alinéa restent inchangés.",
    'material_reduction',
    "La durée imposée de trois ans et trois étapes obligatoires propres à cet accord sont supprimées : avis, agrément et instance préalable distincte. Les décisions d'attribution, les priorités et les engagements déjà souscrits restent contrôlables et exécutoires.",
    "Les obligations autonomes des conférences et conventions d'attribution de L441-1-5 et L441-1-6 ne sont pas abrogées. Le délai de six mois avant désignations contraignantes protège le bailleur et n'est pas raccourci.",
    "Aucune charge nouvelle n'est identifiée : aucune transmission, déclaration ou commission de remplacement n'est imposée. Une concertation facultative peut subsister ; le coût net de l'ensemble du logement social n'est pas établi.",
    [effect('obligation_removed', 'accord-intercommunal-fin-duree-imposee',
            "Suppression de la durée légale de trois ans de l'accord intercommunal.",
            "Accord collectif intercommunal à conclure pour trois ans.",
            "Durée librement choisie par les signataires, sans périodicité de remplacement.",
            'legal_duty', "EPCI, établissements territoriaux et organismes signataires de l'accord intercommunal.",
            "Accords futurs ou modifiés dès l'entrée en vigueur ; durées et engagements des accords valablement conclus préservés.",
            "Aucune clause obligatoire supplémentaire ; la liberté de durée ne supprime pas les priorités légales.",
            "conclure pour trois ans un accord collectif intercommunal.",
            "Les signataires peuvent fixer librement la durée de l'accord et les modalités de sa modification."),
     effect('obligation_removed', 'accords-attribution-fin-avis-prealables',
            "Retrait de l'avis départemental préalable sur l'accord intercommunal.",
            "Transmission au comité pour avis, réputé favorable seulement après deux mois de silence.",
            "Aucun avis du comité requis pour conclure ou modifier l'accord, sans transmission substitutive.",
            'legal_duty', "EPCI ou établissements territoriaux proposant l'accord et organismes signataires.",
            "Accords nouveaux ou modifiés et projets en cours dès l'entrée en vigueur ; accords acquis préservés.",
            "Aucun visa ou dépôt de remplacement ; accompagnement et priorités maintenus.",
            "Cet accord est soumis pour avis au comité responsable du plan départemental d'action pour le logement et l'hébergement des personnes défavorisées.",
            "L'accord collectif intercommunal n'est soumis ni à l'avis préalable du comité responsable du plan départemental d'action pour le logement et l'hébergement des personnes défavorisées ni à un agrément du représentant de l'Etat dans le département."),
     effect('authorization_removed', 'accord-intercommunal-fin-agrement-substitution',
            "Substitution de l'accord intercommunal à l'accord départemental dès sa conclusion.",
            "Substitution conditionnée par l'agrément du préfet.",
            "Substitution dès conclusion sans agrément spécifique.", 'legal_duty',
            "Signataires des accords collectifs intercommunaux et organismes soumis à l'accord départemental.",
            "Accords conclus ou modifiés et projets en cours dès l'entrée en vigueur ; engagements anciens protégés.",
            "Aucune formalité de remplacement ; pouvoirs DALO autonomes inchangés.",
            "Après agrément du représentant de l'Etat dans le département, l'accord collectif intercommunal se substitue",
            "Dès sa conclusion, l'accord collectif intercommunal se substitue"),
     effect('obligation_removed', 'accord-intercommunal-fin-commission-double',
            "Retrait de la commission de coordination obligatoire distincte de la commission d'attribution.",
            "Commission distincte imposée, avec composition, avis sur les dossiers et règlement intérieur.",
            "Aucune commission de coordination à créer ; concertation laissée aux signataires.",
            'legal_duty', "Signataires des accords intercommunaux et membres imposés de la commission de coordination.",
            "Accords et projets relevant de la réforme ; possibilité de maintenir volontairement les instances existantes et respect des conventions acquises.",
            "La commission d'attribution existante demeure ; aucune instance nouvelle n'est imposée.",
            "L'accord collectif intercommunal prévoit la création d'une commission de coordination",
            "L'accord collectif intercommunal n'impose pas la création d'une commission de coordination distincte des commissions d'attribution prévues à l'article L. 441-2.")],
    ["La durée légale imposée de trois ans de l'accord collectif intercommunal est supprimée au profit d'une durée librement choisie par ses signataires.",
     "L'avis préalable obligatoire du comité départemental, sa transmission et l'attente attachée à cet avis sont supprimés pour cet accord.",
     "L'agrément préfectoral conditionnant la substitution de l'accord intercommunal à l'accord départemental est supprimé.",
     "La commission de coordination distincte obligatoire, sa composition légale, ses avis préalables sur les dossiers et son règlement intérieur imposé sont supprimés."],
    "Les engagements quantifiés de logement des personnes reconnues DALO ou prioritaires, l'accompagnement, les signataires réservataires facultatifs et la substitution évitant deux accords territoriaux sont conservés. Les futures personnes prioritaires en bénéficient aussi ; aucune priorité n'est remplacée par un quota communal SRU.")

n = 'L441-1-2'
ps = paragraphs(n)
ps[0] = ps[0].replace("conclut tous les trois ans un accord collectif", "conclut un accord collectif")
ps[3] = p("Les signataires peuvent fixer librement la durée de l'accord et les modalités de sa modification. Aucune conclusion ou reconduction triennale n'est imposée par le présent article. Sa conclusion, son renouvellement ou sa modification ne sont pas soumis à l'avis préalable du comité responsable du plan départemental d'action pour le logement et l'hébergement des personnes défavorisées.")
xml = ''.join(ps) + p("Ces dispositions s'appliquent aux accords conclus, renouvelés ou modifiés à compter de l'entrée en vigueur de la présente loi et aux projets en cours, sans transmission ni formalité de remplacement de l'avis supprimé. Les accords antérieurs conservent leur durée et leurs engagements, les aides accordées et les droits des demandeurs ; ils n'ont pas à être renouvelés du seul fait de la présente loi. Les priorités légales d'attribution demeurent applicables indépendamment de la durée de l'accord.")
add(n, xml,
    "Réforme de fond : retirer la conclusion obligatoire d'un accord tous les trois ans et permettre aux signataires de fixer sa durée ; supprimer l'avis départemental préalable et l'attente de deux mois. Maintien intégral des engagements annuels de logement des personnes défavorisées, DALO et prioritaires, des capacités d'accueil et de l'accompagnement.",
    "Les quatre alinéas source restent identifiables, avec transition finale. L441-1 et L441-2-3 lus : les priorités et recours sont autonomes et ne dépendent pas d'une reconduction triennale. L441-1-3 demeure le mécanisme d'exécution, avec ses garanties de conciliation et de mise en demeure ; seule sa consultation municipale répétée est traitée dans cet autre objet. L'avis supprimé relève de la même mesure que celui de L441-1-1, sans décompte de taxe ou de second rapport supprimé.",
    'material_reduction',
    "La périodicité triennale obligatoire de conclusion disparaît réellement ; les parties peuvent stabiliser l'accord au-delà de trois ans. Le circuit d'avis est retiré dans le prolongement de l'allègement des accords intercommunaux.",
    "Les engagements annuels prioritaires et la conclusion d'un accord départemental restent nécessaires. La durée des accords antérieurs n'est pas prolongée automatiquement et aucun gain financier national n'est établi.",
    "Aucune charge nouvelle n'est identifiée : la durée est décidée dans l'accord déjà prévu, sans document distinct, agrément, nouvelle transmission ou périodicité de remplacement.",
    [effect('obligation_removed', 'accord-departemental-fin-renouvellement-triennal',
            "Suppression de la cadence légale de conclusion triennale de l'accord départemental.",
            "Accord à conclure tous les trois ans avec les bailleurs du département.",
            "Accord dont la durée et les modifications sont librement fixées par les signataires, engagements annuels conservés.",
            'legal_duty', "Préfets, bailleurs sociaux et réservataires signataires de l'accord départemental.",
            "Accords nouveaux, renouvelés ou modifiés dès l'entrée en vigueur ; durées et droits des anciens accords conservés.",
            "Aucun document ou renouvellement périodique de remplacement.",
            "le représentant de l'Etat conclut tous les trois ans un accord collectif",
            "Les signataires peuvent fixer librement la durée de l'accord et les modalités de sa modification."),
     effect('coordination', 'accords-attribution-fin-avis-prealables',
            "Déclinaison départementale du retrait du circuit d'avis sur les accords collectifs d'attribution.",
            "Avis du comité départemental et silence de deux mois valant avis favorable.",
            "Aucun avis du comité pour conclusion, renouvellement ou modification.", 'legal_duty',
            "Signataires des accords collectifs départementaux.", "Projets en cours et accords relevant de la réforme, droits anciens préservés.",
            "Aucune transmission substitutive ; même mesure d'avis que L441-1-1.",
            "Cet accord est soumis pour avis au comité responsable du plan départemental d'action pour le logement et l'hébergement des personnes défavorisées.",
            "Sa conclusion, son renouvellement ou sa modification ne sont pas soumis à l'avis préalable du comité responsable du plan départemental d'action pour le logement et l'hébergement des personnes défavorisées.")],
    ["La conclusion obligatoire d'un nouvel accord collectif départemental tous les trois ans est supprimée pour les accords futurs.",
     "L'avis préalable du comité départemental sur cet accord, la transmission et l'attente de deux mois correspondantes sont supprimés."],
    "Les engagements annuels de logements en faveur des personnes en difficulté, DALO et autres catégories prioritaires ainsi que les moyens d'accompagnement sont conservés sans limiter leur bénéfice aux demandeurs déjà inscrits. La liberté de durée évite les renouvellements contraints sans fermer les droits futurs.")

n = 'L441-1-3'
raw = by_number[n]['source_xml']
parts = [x.strip() for x in re.split(r'<br\s*/?>', raw) if x.strip()]
assert len(parts) == 3
old_consultations = [", après consultation des maires des communes intéressées", ", après consultation des maires des communes concernées"]
for i in range(3):
    for phrase in old_consultations:
        parts[i] = parts[i].replace(phrase, '')
xml = ''.join(p(x) for x in parts) + p("La suppression des consultations préalables des maires prévues au présent article s'applique aux décisions prises à compter de l'entrée en vigueur de la présente loi, y compris dans les procédures en cours, sans nouvelle formalité de remplacement. Les décisions déjà prises, les baux, les conventions de réservation, les droits des demandeurs et les voies de recours sont préservés. La participation des maires aux autres instances légalement compétentes demeure régie par ses dispositions propres.")
add(n, xml,
    "Réforme de fond : retirer les trois consultations municipales répétées avant l'exécution des engagements de logement prioritaires ou l'intervention du délégué spécial. Les droits de réservation, le délai protecteur de six mois, l'adéquation sociale des attributions, la conciliation, la mise en demeure, la durée d'un an du délégué et les conventions régulièrement signées restent intégralement maintenus.",
    "Les trois alinéas sont conservés à leur place, transition finale. L441-2, L441-1-5 et L441-1-6 lus pour la participation autonome des maires aux instances du logement. L441-2-3 renvoie aussi à cet article en cas d'obstacle aux attributions DALO : les pouvoirs de substitution et le contradictoire ne sont pas abolis. Ce délégué spécial d'exécution des attributions n'est ni une carence communale SRU ni un administrateur de rupture d'emploi.",
    'material_reduction',
    "Trois saisines pour avis des maires sont retirées dans un même mécanisme d'exécution. La protection des personnes prioritaires et les garanties du bailleur ne sont pas réduites ; aucune suppression de délai global n'est chiffrée.",
    "Les consultations prévues par d'autres articles, y compris L441-1-1 et L441-1-6, subsistent. Le délai de six mois avant désignation contraignante et le mandat maximal d'un an restent inchangés.",
    "Aucune charge nouvelle n'est identifiée : aucune information, déclaration, instance ou avis de remplacement n'est exigé ; les maires conservent leur participation autonome et les recours demeurent.",
    [effect('obligation_removed', 'attributions-prioritaires-fin-avis-municipaux-repetes',
            "Suppression des consultations municipales préalables répétées dans les trois étapes d'exécution de L441-1-3.",
            "Consultation des maires avant attributions de substitution et avant action du délégué spécial.",
            "Décisions d'exécution sans ces trois consultations, avec droits de réservation et garanties procédurales inchangés.",
            'legal_duty', "Préfets et organismes bailleurs soumis à l'exécution des accords prioritaires.",
            "Décisions prises dès l'entrée en vigueur, procédures pendantes comprises ; baux et décisions anciens préservés.",
            "Aucune consultation de remplacement ; conciliation et mise en demeure conservées.",
            "après consultation des maires des communes intéressées",
            "La suppression des consultations préalables des maires prévues au présent article s'applique aux décisions prises à compter de l'entrée en vigueur de la présente loi")],
    ["Les consultations des maires avant les attributions de substitution des premier et deuxième alinéas et avant celles du délégué spécial au troisième alinéa sont supprimées."],
    "Le droit à l'exécution des engagements prioritaires, le respect des conventions de réservation et la prise en compte de l'occupation du patrimoine restent applicables aux futurs bénéficiaires. La conciliation, la mise en demeure et le délai préalable protègent toujours les organismes concernés.")

n = 'L441-1-7'
xml = p("Les articles L. 441-1, L. 441-1-1, L. 441-1-5, L. 441-1-6, L. 441-2, L. 441-2-1, L. 441-2-3-2, L. 441-2-7 et L. 441-2-8 sont applicables à la métropole de Lyon.")
add(n, xml,
    "Coordination nécessaire : retirer de la liste d'application à Lyon le seul compte rendu annuel de L441-2-5 abrogé dans ce lot. Toutes les autres dispositions territoriales sont intégralement conservées ; aucune réduction autonome supplémentaire n'est revendiquée.",
    "Cette coordination prend effet avec l'abrogation de L441-2-5. Les autres renvois, dont ceux aux dispositifs d'information et de gestion partagée, demeurent. La métropole ne perd ni ses droits d'accès aux données légalement disponibles ni les protections des demandeurs ; l'obligation de compte rendu n'est pas recréée par ce renvoi.",
    'coordination_only',
    "La liste territoriale cesse de viser l'obligation annuelle abrogée. Il s'agit de la même mesure que L441-2-5 et non d'un second rapport ou prélèvement supprimé.",
    "Aucun autre régime propre à Lyon n'est modifié et les obligations autonomes d'enregistrement des attributions subsistent.",
    "Aucune charge nouvelle n'est identifiée : la liste est seulement amputée du renvoi abrogé, sans nouveau destinataire, fichier ou rapport.",
    [effect('coordination', 'attributions-sociales-fin-compte-rendu-annuel',
            "Retrait de l'application territoriale du seul compte rendu annuel abrogé.",
            "Liste applicable à Lyon incluant L441-2-5.", "Même liste sans L441-2-5, autres articles inchangés.", 'other',
            "Métropole de Lyon et bailleurs présents sur son territoire.",
            "Même entrée en vigueur que la suppression de L441-2-5, sans remise en cause des données et droits anciens.",
            "Aucun rapport de remplacement ; enregistrement national inchangé.",
            "L. 441-2-3-2, L. 441-2-5, L. 441-2-7 et L. 441-2-8",
            "L. 441-2-3-2, L. 441-2-7 et L. 441-2-8")],
    benefit="L'application à Lyon des priorités d'attribution, des droits d'information, de l'enregistrement et de la gestion partagée est conservée pour les demandes futures comme antérieures. Aucun avantage de logement ou accès légal aux informations n'est fermé par le retrait du seul rapport abrogé.")

retain('L441-2-2',
       "Maintien intégral après examen : l'écrit motivé assure le recours contre un refus ; l'exception en faveur des personnes protégées contre les violences et l'obligation de proposer le premier logement adapté hors résidence fragile sont des protections à conserver. Les deux motifs de refus sont des facultés encadrées, non des formalités obligatoires supplémentaires. Retirer isolément le troisième alinéa ferait aussi disparaître son droit favorable de relogement.",
       "L441-1-6 lu en entier : les résidences à enjeu prioritaire relèvent d'un mécanisme d'attribution autonome, non du quota communal SRU supprimé. Le refus lié à la propriété ne peut être automatique ; l'adaptation du bien ou ses revenus suffisants et l'exception d'ordonnance de protection restent exigés. Le renvoi au titre XIV du livre Ier du code civil est reproduit de la source : la mention antérieure du code de procédure civile dans le contexte de L441-1 rend nécessaire une concordance documentaire extérieure ; aucun contenu de ce titre n'est inventé ici. Le contrôle juridictionnel du motif et l'offre adaptée restent nécessaires.",
       "Aucun changement de norme : maintien de la motivation et de l'accès protégé des victimes, avec garantie d'une offre alternative en cas de refus lié à la résidence. Aucune simplification ni nouvelle baisse de loyer n'est comptée.",
       "Le décret définissant les ménages concernés et les références civiles ne sont pas réécrits dans ce lot ; le maintien n'atteste pas leur conformité indépendante.",
       "L'exception au motif de propriété pour les bénéficiaires actuels ou passés d'une ordonnance de protection, et l'offre du premier logement vacant adapté hors résidence fragile, restent ouvertes aux futures demandes éligibles. La notification motivée protège tous les demandeurs et leurs recours.")

retain('L441-2-3-1',
       "Maintien intégral du recours juridictionnel DALO et hébergement : injonction, urgence, astreinte, contradictoire et modalités de versement rendent effectif le droit. Les durées de deux mois sont des délais maximaux de jugement, non des attentes minimales à supprimer. Les astreintes ne sont pas une taxe de production ; leur suppression affaiblirait le recours.",
       "Les I, II et III, les deux séries de règles d'astreinte depuis le 1er janvier 2016, les dates historiques du 1er décembre 2008 et du 1er janvier 2012 et le calendrier de liquidation sont conservés. L441-2-3 lu en entier pour la décision de priorité et ses catégories. L'expression ancienne « commissaire du Gouvernement » est celle de la source et n'est pas présentée comme une nouvelle fonction créée. L'agrément des organismes d'assistance est une qualification de protection dans ce recours, non un dépôt périodique autonome ; les réformes de leurs dossiers d'agrément restent à leur champ propre.",
       "Aucune réduction matérielle : toutes les voies de recours et les garanties financières d'exécution sont maintenues. Modifier seulement le vocabulaire ou effacer les périodes historiques encore pertinentes ne répondrait pas à la consigne.",
       "Le code de justice administrative et les délais réglementaires de réponse de l'Etat ne sont pas modifiés. Aucun effet sur la durée réelle des contentieux ni sur les finances du fonds n'est chiffré.",
       "Les recours, l'assistance qualifiée, les ordonnances dans les cas manifestes et l'injonction assortie d'astreinte restent accessibles aux futurs demandeurs DALO et d'hébergement. Les droits issus de jugements anciens, le produit acquis au fonds et les deux calendriers historiques sont préservés.")

retain('L441-2-3-2',
       "Maintien nécessaire de l'accès à l'information sur le droit au logement, les aides et la commission de médiation pour les personnes visées. La concertation n'impose ni nouveau dossier au demandeur ni rapport périodique ; retirer cette obligation d'information fermerait l'accès effectif aux avantages et recours.",
       "Les premier et deuxième alinéas du II de L441-2-3 ont été lus : demande après délai excessif et saisine sans délai dans les situations graves. Le renvoi conserve ces deux populations, sans les réduire aux seules personnes déjà reconnues prioritaires. L'application à Lyon demeure dans L441-1-7.",
       "Aucun changement normatif : l'information coordonnée des personnes concernées est une protection utile, sans autorisation préalable ou prélèvement à supprimer dans cet article.",
       "Le maintien ne crée ni guichet supplémentaire ni fichier ; les modalités pratiques d'information relèvent des services compétents.",
       "L'information sur les aides d'accès ou de maintien au logement et sur le recours de médiation reste due aux futures personnes remplissant les conditions des deux alinéas visés. La participation des collectivités ne devient pas une condition à leur droit d'information.")

n = 'L441-2-3-3'
ps = paragraphs(n)
ps[0] = ps[0].replace("l'indemnité dont le propriétaire ou l'exploitant est redevable en application des IV et VI de l'article L. 521-3-2 est versée à l'Etat.",
    "l'indemnité dont le propriétaire ou l'exploitant est redevable en application du IV de l'article L. 521-3-2 est versée à l'Etat et recouvrée dans les conditions prévues au VI du même article. Pour les relogements assurés à compter de l'entrée en vigueur de la présente loi, elle correspond aux frais effectivement engagés pour le relogement, dans la limite d'un an du loyer prévisionnel ; les mêmes frais ne peuvent être recouvrés une seconde fois. L'indemnité de réinstallation due à l'occupant reste distincte.")
ps[1] = p("Cette créance est recouvrée comme en matière de contributions directes. Elle bénéficie de la sûreté prévue au 7° de l'article 2402 du code civil, mise en œuvre selon les articles 2404 et suivants du même code, ainsi que des garanties prévues aux articles L. 541-1 et suivants du présent code.")
xml = ''.join(ps) + p("Les créances légalement nées des relogements assurés avant l'entrée en vigueur de la présente loi restent régies par les dispositions antérieures pour leur liquidation, leur recouvrement, les restitutions, la prescription et les recours, même si leur paiement est ultérieur. La présente coordination n'ouvre aucun droit général au remboursement des indemnités déjà acquittées.")
add(n, xml,
    "Coordination nécessaire avec le IV et la transition du L521-3-2 proposé : distinguer l'assiette indemnitaire du IV et le recouvrement du VI, plafonner la créance future au coût réel dans la limite annuelle déjà retenue dans la cible et interdire le double recouvrement des mêmes frais. L'affectation à l'Etat, le recouvrement et les sûretés restent inchangés dans leur champ. Le vocabulaire neutre de sûreté évite d'affirmer que l'article 2402 actuel crée encore un privilège.",
    "Cible L521-3-2 officielle et proposition lues intégralement : le IV officiel prévoit un forfait d'un an ; le IV proposé retient les frais effectifs plafonnés et le VIII protège les anciens relogements. Cette coordination ne compte pas une seconde réduction du même forfait. La réinstallation de l'occupant est distincte. Le texte civil intégral n'est pas joint : le numéro 2402 7° et les articles 2404 et suivants ne sont pas changés ; la qualification ancienne « privilège » reste un point de concordance documentaire, non une sûreté nouvelle. La note du 1er janvier 2022 ne date pas notre réforme. Aucun barème d'indemnité du travail n'est importé.",
    'coordination_only',
    "Le renvoi de recouvrement suit la seule réforme des frais de relogement de L521-3-2, avec la même transition ; aucune seconde économie ou taxe supprimée n'est revendiquée.",
    "Le forfait ancien reste applicable aux créances antérieures. Le montant effectif des économies n'est pas établi et les textes civils et de recouvrement extérieurs ne sont pas réécrits.",
    "Aucune charge nouvelle autonome n'est identifiée : la créance reste recouvrée par les voies existantes ; les frais et le bénéficiaire sont ceux du relogement déjà réalisé. Aucun registre, délai ou justificatif supplémentaire n'est imposé par cet article.",
    [effect('coordination', 'relogement-indemnite-frais-reels-plafonnee',
            "Raccordement de la créance versée à l'Etat au coût réel plafonné de la cible L521-3-2.",
            "Renvoi aux IV et VI dont le IV officiel porte une indemnité égale à un an du loyer prévisionnel.",
            "Renvoi distinguant indemnité et recouvrement ; coût réel plafonné à un an pour les nouveaux relogements, sans double recouvrement.",
            'other', "Propriétaires ou exploitants défaillants d'établissements d'hébergement et Etat ayant relogé.",
            "Relogements assurés dès l'entrée en vigueur ; créances anciennes et recours sous droit antérieur.",
            "Aucune taxe ni indemnité de remplacement ; indemnité personnelle de réinstallation conservée.",
            "l'indemnité dont le propriétaire ou l'exploitant est redevable en application des IV et VI de l'article L. 521-3-2 est versée à l'Etat.",
            "elle correspond aux frais effectivement engagés pour le relogement, dans la limite d'un an du loyer prévisionnel")],
    benefit="Le relogement des personnes exposées à l'insalubrité ou au danger et l'indemnité de réinstallation demeurent protégés. La limitation des remboursements futurs au coût réel suit la cible, sans réduire les dépenses effectivement couvertes ni effacer les anciens droits ; aucun avantage fiscal n'est supprimé.")

n = 'L441-2-3-4'
xml = p(by_number[n]['source_xml'].strip()) + p("Pour l'application du premier alinéa de l'article L. 521-3-3 à ces relogements, les prérogatives du représentant de l'Etat dans le département se rapportent aux obligations qui lui incombent en application du I ou, le cas échéant, des III ou V de l'article L. 521-3-2 ; elles ne se fondent pas sur le II abrogé de ce dernier article. Les autres conditions de l'article L. 521-3-3, les droits des occupants, les conventions de réservation et les droits de recours demeurent applicables.")
add(n, xml,
    "Coordination nécessaire d'un renvoi indirect : le L521-3-3 officiel lu vise encore au premier alinéa le II désormais abrogé de L521-3-2. Le corps initial est conservé et l'application aux obligations actuelles I, III ou V est explicitée dans le champ déjà visé par L441-2-3-4 ; aucune nouvelle police du logement ou indemnité n'est créée.",
    "L521-3-2 officiel et proposé lus intégralement dans les cibles ; L521-3-3 lu en entier dans le corpus. Ce dernier est une cible facultative non fournie dans reference-targets et demeure à coordonner dans son propre article, notamment son premier alinéa. La présente règle règle expressément son application aux relogements du présent article sans faire revivre le II abrogé. Les pouvoirs du maire et de l'EPCI sur leurs droits de réservation, les engagements d'accords prioritaires et l'hébergement transitoire de L521-3-3 ne sont pas supprimés. La limite d'indemnité suit sa transition propre ; aucun préavis de travail ne s'applique aux occupants.",
    'coordination_only',
    "La proposition traite l'incohérence préexistante du raccordement au II abrogé et maintient l'effectivité du relogement dangereux ou insalubre. Aucun prélèvement ou circuit administratif supplémentaire n'est présenté comme supprimé.",
    "La correction directe de L521-3-3 est hors lot et reste identifiée. Les attributions, réservations et conditions transitoires conservent leurs règles propres sans extension à d'autres cas de relogement.",
    "Aucune charge nouvelle n'est identifiée : mêmes autorités, mêmes occupants et mêmes obligations de relogement ; aucun registre, délai ni justificatif supplémentaire ne résulte de l'explicitation du renvoi.",
    [effect('coordination', 'relogement-renvoi-substitution-ii-abroge',
            "Explicitation des obligations actuelles auxquelles se rapporte le renvoi à L521-3-3.",
            "Application de L521-3-3 dont le premier alinéa renvoie encore à un II abrogé.",
            "Application expresse aux obligations actuelles I, III ou V, dans le champ de L441-2-3-4.", 'other',
            "Préfets ou maires assurant le relogement d'occupants de locaux frappés d'un arrêté de police.",
            "Coordination à l'entrée en vigueur sans retrait des droits des occupants ou recours en cours.",
            "Aucune procédure de remplacement ou extension à une rupture d'emploi.",
            "il est fait application de l'article L. 521-3-3.",
            "elles ne se fondent pas sur le II abrogé de ce dernier article.")],
    benefit="Le relogement des occupants de locaux insalubres ou dangereux continue de bénéficier aux situations futures entrant dans les I, III ou V applicables, sans dépendre d'un II abrogé. Les droits de réservation, les solutions temporaires et les recours restent à leur champ propre.")

retain('L441-2-4',
       "Maintien nécessaire du droit facultatif du maire d'être entendu par les organismes possédant ou gérant le parc communal. Aucune audition systématique, périodicité, dossier ou avis conforme n'est imposé ; supprimer ce droit restreindrait la participation locale sans retirer une procédure préalable générale.",
       "Le champ comprend organismes HLM, SCI majoritairement financées par la participation des employeurs et SEM locales d'aménagement et de construction. L'audition sur demande ne vaut ni droit de veto sur les logements ni pouvoir de rétablir les quotas SRU supprimés.",
       "Aucun changement de fond : conservation d'un droit d'audition ciblé, sans création d'une instance ou d'un rapport distinct.",
       "Les décisions des conseils d'administration et les commissions d'attribution restent régies par leurs dispositions propres ; aucun gain global de délai n'est démontré.",
       "La faculté d'audition reste ouverte pour toute demande future du maire ou de son représentant et pour les trois catégories d'organismes prévues. Elle ne conditionne pas l'accès des ménages aux logements ni aux aides.")

n = 'L441-2-5'
xml = p("Le présent article est abrogé à compter de l'entrée en vigueur de la présente loi. A compter de cette date, aucun compte rendu annuel, transmission ou rattrapage ne peut être exigé sur le seul fondement du présent article, y compris au titre d'une année antérieure.")
xml += p("Les comptes rendus déjà établis et les informations régulièrement enregistrées demeurent conservés et accessibles selon les règles qui leur sont applicables. L'abrogation ne dispense pas de l'enregistrement des attributions dans le système national d'enregistrement ni des obligations d'information des demandeurs, des contrôles et des comptes rendus fondés sur des dispositions légales autonomes. Aucun rapport périodique de remplacement n'est institué.")
a = add(n, xml,
    "Abrogation prospective de l'obligation annuelle générale de rendre compte des attributions à la préfecture, aux EPCI et aux maires, y compris des rattrapages futurs sur ce seul fondement. L'enregistrement individuel nécessaire à la gestion des demandes et les accès légaux aux informations sont conservés ; aucun nouveau rapport n'est créé.",
    "R441-12 lu intégralement : son I permet déjà de satisfaire le compte rendu par les enregistrements nationaux ; ne pas revendiquer la suppression d'un second dépôt aujourd'hui obligatoire. Ses II et IV portent consolidation non nominative et accès, à préserver ; son III porte une transmission annuelle préfectorale autonome, non déclarée supprimée par le seul présent article. L441-1 impose aussi un bilan annuel des désignations et R441-9 un compte rendu interne : ces bases distinctes ne sont pas abolies implicitement. L441-1-7, L441-2-8 et l'habilitation L441-2-9 sont coordonnés dans ce lot. La coordination directe de R441-12, cible facultative hors reference-targets, reste identifiée hors lot.",
    'material_reduction',
    "Le devoir annuel général de compte rendu fondé sur L441-2-5 disparaît. Le gain de charge pratique est limité : les bailleurs qui enregistrent déjà au système national le satisfaisaient sans document séparé ; l'enregistrement et les autres bilans autonomes subsistent.",
    "Aucune économie de saisie nationale n'est établie, ni suppression de toutes les statistiques ou transmissions d'autres articles. Le montant net de coût privé ou public n'est pas chiffré.",
    "Aucune charge nouvelle n'est identifiée : aucun rapport, collecte ou fichier de remplacement n'est ajouté ; les accès et enregistrements maintenus préexistaient à l'abrogation.",
    [effect('obligation_removed', 'attributions-sociales-fin-compte-rendu-annuel',
            "Fin du compte rendu annuel général fondé sur L441-2-5 sans retirer l'enregistrement des attributions.",
            "Compte rendu une fois par an aux autorités territoriales désignées, déjà satisfait par le SNE selon R441-12.",
            "Aucun compte rendu ni rattrapage exigible sur ce seul fondement ; SNE et bases autonomes maintenus.",
            'legal_duty', "Bailleurs sociaux, préfectures, EPCI compétents et communes destinataires.",
            "Transmissions futures dès l'entrée en vigueur, même pour années anciennes ; données et rapports déjà établis préservés.",
            "Aucun rapport périodique substitutif ; obligations nationales d'enregistrement inchangées.",
            "les bailleurs sociaux rendent compte, une fois par an, de l'attribution des logements locatifs sociaux",
            "aucun compte rendu annuel, transmission ou rattrapage ne peut être exigé sur le seul fondement du présent article")],
    benefit="L'information des demandeurs, la conservation des données antérieures et les droits légaux d'accès aux informations d'attribution demeurent applicables. Aucune priorité de logement, aide, exonération ou dérogation future n'est retirée ; seule la base du compte rendu annuel général est abrogée.")
a.update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19',
         repeal_scope="Obligation annuelle générale des bailleurs sociaux de rendre compte des attributions au préfet, aux EPCI et aux maires, y compris transmissions et rattrapages futurs exclusivement fondés sur L441-2-5 ; enregistrements nationaux et bases autonomes conservés.")

retain('L441-2-6',
       "Maintien intégral du droit d'information préalable et du suivi individuel de la demande : pièces admissibles, parc accessible, étapes d'instruction et transparence de la cotation. Cette information empêche les demandes de pièces arbitraires et permet le recours ; ce n'est pas un rapport administratif annuel redondant.",
       "L441-2-1, L441-2-7 et L441-2-8 lus. La suppression du compte rendu de L441-2-5 ne ferme pas ce droit ; aucune information nominative sur d'autres demandeurs n'est ouverte. La cotation reste obligatoire dans le plan maintenu par L441-2-8 et son information doit être conservée. Aucun dépôt de justificatifs supplémentaires n'est ajouté.",
       "Aucun changement normatif : l'article protège la lisibilité des démarches et des décisions et ne crée pas d'autorisation ou de taxe à retirer. Son maintien n'est pas présenté comme une nouvelle simplification.",
       "Les informations disponibles sur le parc et le niveau de satisfaction restent limitées à leur base légale ; l'article ne mesure pas les délais réels d'attribution.",
       "Les futurs candidats et demandeurs gardent les informations sur les pièces, leurs propres données, les autres territoires répondant à leurs besoins et la cotation. Aucun de ces droits n'est réservé aux personnes déjà enregistrées ou aux seuls rapports anciens.")

n = 'L441-2-7'
ps = paragraphs(n)
assert len(ps) == 4
ps[2] = p("Les parties mentionnées au premier alinéa peuvent préciser par convention les modalités de leur participation au dispositif, notamment à son financement. Le présent article ne leur impose pas de conclure une convention distincte et n'autorise pas le représentant de l'Etat à fixer par arrêté la participation d'un bailleur ou d'un réservataire au seul motif qu'il refuse de signer une convention.")
xml = ''.join(ps) + p("Cette suppression de la convention obligatoire et de la participation imposée par arrêté s'applique à compter de l'entrée en vigueur de la présente loi, y compris aux procédures en cours. Les conventions valablement conclues, les créances légalement constituées avant cette date et les droits des demandeurs sont préservés ; aucune nouvelle convention ni formalité de remplacement ne peut être exigée sur ce seul fondement. Les obligations de mise en commun, les solutions d'adhésion déjà prévues et les garanties de protection des données demeurent applicables.")
add(n, xml,
    "Réforme de fond : supprimer la convention de mise en œuvre obligatoirement distincte et le pouvoir d'imposer par arrêté une participation au seul refus de signer. Conserver le dispositif partagé, les pièces nécessaires, l'interconnexion, l'adhésion à un dispositif départemental, régional ou national valant exécution, le cahier des charges francilien et la substitution en cas d'absence effective de dispositif.",
    "Les quatre alinéas restent en place et une transition est ajoutée. L441-2-1 lu : dépôt unique et SNE existaient déjà, donc aucune seconde fusion de dossier ni nouveau gain CRPA n'est revendiqué. La carence de cet article concerne l'absence de gestion partagée, non la carence communale de L302-9-1 supprimée. Les conventions et créances anciennes restent exécutoires ; l'abolition ne rembourse pas les participations acquittées. Les prescriptions réglementaires de convention de gestion partagée restent à coordonner dans leurs articles, sans les présenter comme déjà réécrites.",
    'material_reduction',
    "Une formalisation contractuelle imposée et la participation unilatérale attachée au seul refus de signature sont retirées. La mise en commun effective et la protection des dossiers restent obligatoires ; aucun nouveau fichier n'est fusionné ni créé.",
    "L'absence de convention imposée ne rend pas facultative la participation à la gestion partagée. Le financement global et les coûts de fonctionnement du SNE ne sont pas chiffrés ni garantis par une recette nouvelle.",
    "Aucune charge nouvelle n'est identifiée : les conventions deviennent facultatives, les données et dispositifs sont ceux de la source et aucune déclaration ni donnée de remplacement n'est requise. Le coût net public reste inconnu.",
    [effect('obligation_removed', 'gestion-partagee-fin-convention-imposee',
            "Suppression de la convention distincte obligatoire et de la participation forcée en raison du refus de signature.",
            "Convention nécessaire à la mise en œuvre et participation pouvant être fixée par arrêté après refus de signer.",
            "Convention facultative ; pas d'arrêté de participation sur le seul refus, obligation de gestion partagée conservée.",
            'legal_duty', "Collectivités, bailleurs, réservataires et services participant à la gestion partagée des demandes.",
            "Dès l'entrée en vigueur, procédures en cours incluses ; conventions et créances anciennes préservées.",
            "Pas de convention ni de déclaration de remplacement ; dispositif commun et garanties de données déjà existants.",
            "La mise en œuvre du dispositif fait l'objet d'une convention qui précise notamment les conditions de participation",
            "Le présent article ne leur impose pas de conclure une convention distincte et n'autorise pas le représentant de l'Etat à fixer par arrêté la participation d'un bailleur ou d'un réservataire au seul motif qu'il refuse de signer une convention.")],
    ["La conclusion obligatoire d'une convention distincte de mise en œuvre et de financement du dispositif de gestion partagée est supprimée.",
     "Le pouvoir d'imposer par arrêté la participation d'un bailleur ou réservataire au seul motif du refus de signer la convention est supprimé pour les décisions futures."],
    "L'adhésion à un dispositif de niveau supérieur continue de valoir exécution ; le dépôt unique, la mutualisation des pièces et les garanties de données restent accessibles aux futures demandes. Les conventions acquises, les informations individuelles et les droits des demandeurs sont sauvegardés sans prélèvement de remplacement.")

n = 'L441-2-8'
ps = paragraphs(n)
assert len(ps) == 11
old_bilan = "Le bilan de l'attribution des logements locatifs sociaux établi, chaque année, par les bailleurs sociaux, en application de l'article L. 441-2-5, peut être consulté dans le cadre du service d'information et d'accueil des demandeurs de logement."
assert old_bilan in ps[1]
ps[1] = ps[1].replace(old_bilan, "Les bilans déjà établis et les informations non nominatives relatives aux attributions, légalement accessibles, peuvent être consultés dans le cadre du service d'information et d'accueil des demandeurs de logement, sans établissement d'un nouveau compte rendu annuel sur le fondement de l'article L. 441-2-5 abrogé.")
ps[6] = p("II. - L'adoption et la révision du plan ne sont subordonnées ni à un avis préalable des communes membres de l'établissement public de coopération intercommunale ou de l'établissement public territorial de la métropole du Grand Paris, ni à un accord ou un agrément du représentant de l'Etat. L'association à l'élaboration du plan des personnes mentionnées au I est maintenue.")
ps[7] = p("Le représentant de l'Etat ne peut subordonner l'adoption du plan à l'acceptation de modifications sur le fondement du présent article. Le contrôle de légalité et les voies de recours de droit commun demeurent applicables.")
ps[8] = p("Le plan est révisé dans les mêmes conditions.")
ps[9] = p("III. - La mise en œuvre du plan peut faire l'objet de conventions signées entre l'établissement public de coopération intercommunale, la commune de Paris ou l'établissement public territorial de la métropole du Grand Paris et les organismes bailleurs, l'Etat, les autres réservataires de logements sociaux et, le cas échéant, d'autres personnes morales intéressées.")
ps[10] = p("Le présent article n'impose pas de conclure une convention de mise en œuvre et n'autorise pas le représentant de l'Etat à fixer par arrêté la participation d'un bailleur social ou d'un réservataire au seul motif de son refus de signer une telle convention. Les obligations légales d'information, d'accueil, de gestion partagée et de publicité des logements restent applicables.")
xml = ''.join(ps) + p("IV. - Ces simplifications s'appliquent aux plans adoptés ou révisés et aux conventions conclues à compter de l'entrée en vigueur de la présente loi ainsi qu'aux procédures en cours, sans nouvel avis, agrément, transmission de projet ou formalité de remplacement des procédures supprimées. Les plans adoptés, les conventions valablement conclues, les créances légalement constituées et les droits des demandeurs antérieurs à cette date sont préservés. Aucun nouveau compte rendu annuel ne peut être exigé sur le seul fondement de l'article L. 441-2-5 abrogé.")
add(n, xml,
    "Réforme de fond : supprimer le second avis formel des communes, la transmission du projet au préfet comme étape d'adoption et son veto par demande de modifications, ainsi que les conventions obligatoires de mise en œuvre et la participation imposée en cas de refus de signature. Coordination du compte rendu annuel abrogé. Maintien intégral du I sauf cette phrase de coordination : participants, accueil sous un ou deux mois, cotation transparente, location voulue, publicité et faculté d'adhésion à un dispositif supérieur.",
    "Les onze alinéas sources conservent leur place, un IV transitoire étant ajouté. Les deux mois du II supprimé étaient des délais d'avis ou de demande préfectorale, pas la durée du droit à être reçu ; le plafond de deux mois des zones de plus de 50 000 habitants reste au I, ainsi que le délai ordinaire d'un mois. L441-2-6 et L441-2-7 restent cohérents ; la conférence L441-1-5 peut toujours suivre le plan. Les notes fiscales 2027/vacance ne datent pas cette réforme administrative. Les dispositions réglementaires relatives aux plans et à leurs conventions restent à coordonner hors lot avec le 7° de L441-2-9 traité ici. Les actes, conventions et créances acquis ne sont pas annulés.",
    'material_reduction',
    "Le double circuit d'adoption et le pouvoir préfectoral de blocage sont effectivement retirés, de même que la contractualisation imposée d'exécution. L'accueil, la transparence de cotation et les informations aux demandeurs restent des protections nécessaires.",
    "L'obligation d'élaborer le plan dans son champ et les services de son I demeurent. Aucun raccourcissement chiffré de l'instruction réelle, ni suppression des contrôles de légalité ou du budget du service n'est démontré.",
    "Aucune charge nouvelle n'est identifiée : les communes restent associées comme auparavant, les conventions sont facultatives et la consultation de données déjà légalement accessibles n'étend ni l'accès nominatif ni les collectes. Aucun rapport de remplacement n'est ajouté.",
    [effect('obligation_removed', 'plan-demande-logement-fin-double-avis-veto',
            "Suppression de l'avis communal formel supplémentaire et du contrôle préalable préfectoral bloquant l'adoption du plan.",
            "Avis des communes sous deux mois, transmission au préfet et modifications demandables sous deux mois conditionnant l'adoption.",
            "Adoption ou révision sans ces étapes préalables ; association initiale et contrôle de légalité conservés.",
            'legal_duty', "EPCI, Paris, établissements territoriaux, communes membres et préfectures concernés par le plan partenarial.",
            "Plans nouveaux ou révisés et procédures en cours dès l'entrée en vigueur ; plans et droits acquis préservés.",
            "Aucun nouvel avis, envoi de projet ou déclaration substitutive ; contrôle de légalité de droit commun inchangé.",
            "Le plan ne peut être adopté si ces demandes ne sont pas satisfaites.",
            "Le représentant de l'Etat ne peut subordonner l'adoption du plan à l'acceptation de modifications sur le fondement du présent article."),
     effect('coordination', 'gestion-partagee-fin-convention-imposee',
            "Application au plan partenarial du retrait de la convention d'exécution imposée et de la participation fixée pour refus de signer.",
            "Conventions signées obligatoires et participation arrêtée par le préfet en cas de refus.",
            "Conventions facultatives et absence de participation imposée sur ce seul refus, services légaux maintenus.",
            'legal_duty', "Collectivités, organismes bailleurs et réservataires mettant en œuvre le plan.",
            "Futures conventions et procédures en cours ; conventions valablement conclues et créances anciennes protégées.",
            "Même mesure que L441-2-7 ; aucune contractualisation de remplacement.",
            "le représentant de l'Etat dans le département ou, en Ile-de-France, le représentant de l'Etat dans la région fixe par arrêté les conditions de sa participation",
            "Le présent article n'impose pas de conclure une convention de mise en œuvre"),
     effect('coordination', 'attributions-sociales-fin-compte-rendu-annuel',
            "Retrait du renvoi au compte rendu annuel abrogé, sans fermeture de l'information des demandeurs.",
            "Consultation du bilan annuel fondé sur L441-2-5.",
            "Consultation des bilans déjà établis et des informations non nominatives légalement accessibles, sans compte rendu substitutif.",
            'other', "Demandeurs de logement et services d'information et d'accueil.",
            "Même entrée en vigueur que l'abrogation de L441-2-5, données et droits anciens conservés.",
            "Aucun nouveau rapport ni droit d'accès nominatif créé.",
            "Le bilan de l'attribution des logements locatifs sociaux établi, chaque année, par les bailleurs sociaux",
            "Les bilans déjà établis et les informations non nominatives relatives aux attributions, légalement accessibles, peuvent être consultés")],
    ["L'avis préalable formel des communes membres, distinct de leur association à l'élaboration du plan, est supprimé.",
     "La transmission du projet de plan comme procédure préalable et le blocage de son adoption pour refus de modifications préfectorales sont supprimés.",
     "Les conventions obligatoires de mise en œuvre du plan et la participation fixée par arrêté au seul refus de signature sont supprimées pour l'avenir.",
     "La référence à l'établissement obligatoire du compte rendu annuel de L441-2-5 est retirée sans imposer de rapport substitutif."],
    "Les futurs demandeurs conservent le droit d'être reçus sous un mois, ou deux mois dans les zones définies, les informations de cotation, la prise en compte des choix de location voulue et l'accès aux logements vacants publiés. La dispense par adhésion à un dispositif supérieur et les plans et conventions acquis restent maintenus.")

n = 'L441-2-9'
xml = ''.join(paragraphs(n)) + p("Le décret ne peut rétablir, sur le fondement de la présente section, le compte rendu annuel supprimé à l'article L. 441-2-5, les avis préalables et l'agrément supprimés pour les accords collectifs aux articles L. 441-1-1 et L. 441-1-2, les consultations supprimées à l'article L. 441-1-3, les conventions ou participations imposées supprimées aux articles L. 441-2-7 et L. 441-2-8, ni les avis et le pouvoir préfectoral de blocage du plan supprimés au II de l'article L. 441-2-8. Aucune déclaration, attestation, transmission ou procédure équivalente ne peut leur être substituée sur ces seuls fondements. Les règles autonomes d'enregistrement, d'information, de protection des données, d'attribution prioritaire et de contrôle demeurent applicables.")
add(n, xml,
    "Coordination nécessaire de l'habilitation réglementaire : conserver les huit rubriques et empêcher que les modalités d'application de la section réintroduisent les rapports, avis, agréments ou conventions supprimés. Aucun nouveau dépôt ni nouvelle catégorie de donnée n'est créé. Le 6° favorable aux ménages dont un conjoint est en EHPAD est maintenu intégralement.",
    "Les 1° à 8° et leurs numéros sont conservés mot pour mot. Les nouveaux renvois de l'alinéa de verrouillage à L441-2-5, L441-1-1, L441-1-2 et L441-1-3 concernent des sources assignées lues en entier, non des cibles fournies dans reference-targets ; L441-2-7 et L441-2-8 étaient déjà visés. Le décret général de L441-2-9 n'est pas le décret anciennement visé par L441-2-5 : aucune identité fictive des deux renvois n'est présumée. Les mesures d'exécution des accords, plans et données, notamment R441-12 et les règlements de gestion partagée, restent à coordonner dans leurs articles hors lot. L441-2-1, L441-2-6, L441-2-7 et L441-2-8 ont été lus ; les droits d'accès et de cotation restent en vigueur. La note du 21 février 2023 concerne l'entrée en vigueur passée de la source.",
    'coordination_only',
    "L'habilitation reste complète pour les obligations conservées mais ne permet plus de rétablir les procédures supprimées par la loi. Ce verrou de coordination n'est pas compté comme une nouvelle suppression distincte de chacun des renvois.",
    "Les règlements existants ne sont pas présentés comme tous réécrits ; les huit domaines maintenus nécessitent toujours leurs modalités dans le respect des droits des demandeurs.",
    "Aucune charge nouvelle n'est identifiée : les huit habilitations existaient déjà et l'alinéa final limite les formalités possibles, sans nouveau fichier, pièce, délai ou destinataire.",
    [effect('coordination', 'attributions-sociales-fin-compte-rendu-annuel',
            "Borner l'habilitation générale pour éviter de réintroduire le compte rendu annuel supprimé.",
            "Habilitation générale de mise en œuvre de la section contenant le compte rendu annuel.",
            "Habilitation conservée pour les huit domaines avec interdiction expresse de rétablir le compte rendu sur ce fondement.",
            'other', "Pouvoir réglementaire et organismes appliquant la section d'attribution des logements sociaux.",
            "A compter de l'entrée en vigueur des suppressions législatives ; bases autonomes de données et droits anciens conservés.",
            "Aucune déclaration équivalente substitutive ; aucune réduction supplémentaire décomptée.",
            "Un décret en Conseil d'Etat détermine les conditions d'application de la présente section.",
            "Le décret ne peut rétablir, sur le fondement de la présente section, le compte rendu annuel supprimé à l'article L. 441-2-5"),
     effect('coordination', 'plan-demande-logement-fin-double-avis-veto',
            "Le 7° de l'habilitation reste applicable aux plans sans recréer leurs avis et veto abrogés.",
            "Décret fixant l'élaboration, l'évaluation et la révision du plan dans son ancien circuit d'adoption.",
            "Même champ technique, sous la limite expresse des suppressions législatives du II de L441-2-8.",
            'other', "Autorités élaborant le plan partenarial et pouvoir réglementaire.",
            "Même bascule que la simplification du plan ; actes acquis et contrôle de légalité préservés.",
            "Aucune modalité équivalente de blocage ou d'avis ne peut être ajoutée.",
            "Les modalités d'élaboration, d'évaluation et de révision du plan partenarial prévu à l'article L. 441-2-8",
            "les avis et le pouvoir préfectoral de blocage du plan supprimés au II de l'article L. 441-2-8")],
    benefit="Le 6° maintient la prise en compte favorable des dépenses d'EHPAD du conjoint ou partenaire dans les ressources. Les modalités d'information, de numéro unique, d'accès sécurisé, de cotation et de protection des dossiers restent ouvertes aux futures demandes éligibles ; aucune condition d'aide n'est durcie.")

n = 'L441-3-1'
raw = by_number[n]['source_xml']
body = re.sub(r'<br\s*/?>', '', raw).strip()
body = body.replace("Après avis conforme du représentant de l'Etat dans le département, le programme local de l'habitat", "Le programme local de l'habitat", 1)
xml = p(body) + p("La détermination de ces zones ou quartiers et des orientations relatives au supplément de loyer de solidarité n'est soumise à aucun avis conforme ni accord préalable du représentant de l'Etat au titre du présent article. Cette suppression s'applique aux décisions prises à compter de l'entrée en vigueur de la présente loi, y compris dans les procédures en cours, sans demande, déclaration ou visa de remplacement. Les zones et quartiers déjà dispensés, les droits des locataires et les décisions valablement prises restent applicables. Le contrôle de légalité et les voies de recours de droit commun sont maintenus.")
add(n, xml,
    "Réforme de fond : supprimer l'avis conforme préfectoral qui conditionne les zones de dispense du supplément de loyer de solidarité. Maintien de la faculté du PLH, de l'association préalable des organismes HLM et SEM à son élaboration, des orientations de mise en œuvre et de toutes les dispenses acquises. Le supplément lui-même n'est ni augmenté ni déclaré supprimé par cet article.",
    "L'allègement porte sur un avis conforme administratif, pas sur un taux fiscal : le supplément de loyer est distinct d'un impôt. Les futures zones de non-application peuvent être déterminées sans veto préfectoral particulier, avec contrôle de légalité maintenu. Les autres exemptions légales ou réglementaires de supplément et les compétences du PLH demeurent à leur champ ; aucune commune déficitaire ou carencée SRU n'est ajoutée comme condition.",
    'material_reduction',
    "Le préfet ne dispose plus d'un avis conforme préalable dans ce mécanisme favorable de dispense territoriale du supplément de loyer. Le bénéfice existant reste accessible pour de nouvelles décisions, sans hausse de loyer imposée.",
    "Le montant d'une dispense dépend toujours du PLH et des zones qu'il retient ; aucune exonération automatique de tous les locataires ni économie nationale n'est démontrée.",
    "Aucune charge nouvelle n'est identifiée : l'association des organismes existait dans la source, aucune déclaration ou consultation de remplacement n'est introduite et le contrôle de légalité est préexistant.",
    [effect('authorization_removed', 'sls-zones-dispense-fin-avis-conforme',
            "Suppression de l'accord préfectoral préalable aux zones de non-application du supplément de loyer.",
            "Avis conforme du préfet nécessaire avant détermination des zones ou quartiers par le PLH.",
            "PLH habilité à déterminer ces zones sans cet avis conforme ; association des organismes et recours maintenus.",
            'legal_duty', "Collectivités compétentes pour le PLH, organismes HLM, SEM et locataires concernés par une dispense.",
            "Décisions futures dès l'entrée en vigueur, procédures pendantes incluses ; zones et droits acquis conservés.",
            "Aucune demande, déclaration ou visa substitutif ; pas de modification des autres plafonds et exemptions.",
            "Après avis conforme du représentant de l'Etat dans le département",
            "n'est soumise à aucun avis conforme ni accord préalable du représentant de l'Etat au titre du présent article.")],
    ["L'avis conforme préfectoral préalable à la détermination des zones ou quartiers dispensés du supplément de loyer de solidarité et des orientations correspondantes est supprimé."],
    "La faculté de dispenser du supplément de loyer dans les zones et quartiers du PLH est conservée pour les futures décisions, avec une procédure allégée ; les dispenses et droits des locataires antérieurs sont préservés. Aucune autre exonération du supplément n'est retirée et aucune taxe de remplacement n'est créée.")


# Rattacher les transitions au dernier alinéa existant : notamment le renvoi
# de L441-1-6 au dernier alinéa de L441-1-3 doit toujours viser le délégué.
for n in ['L432-1', 'L432-3', 'L432-4', 'L433-2', 'L441-1-1',
          'L441-1-2', 'L441-1-3', 'L441-2-3-3', 'L441-2-3-4',
          'L441-2-7', 'L441-2-8', 'L441-3-1']:
    a = answers[n]
    ps = re.findall(r'<p>.*?</p>', a['proposed_xml'], re.S)
    transition = ps[-1][3:-4]
    if n == 'L441-2-8':
        assert transition.startswith('IV. - ')
        transition = transition[6:]
    ps[-2] = ps[-2][:-4].rstrip() + ' ' + transition + '</p>'
    a['proposed_xml'] = ''.join(ps[:-1])

# Garder les huit rubriques de l'habilitation dans leurs alinéas d'origine.
a = answers['L441-2-9']
ps = re.findall(r'<p>.*?</p>', a['proposed_xml'], re.S)
guard = ps[-1][3:-4]
ps[0] = ps[0].replace(' Il définit ou précise notamment :',
                     ' ' + guard + ' Il définit ou précise notamment :')
a['proposed_xml'] = ''.join(ps[:-1])

answers['L441-1-1']['review_notes'] = answers['L441-1-1']['review_notes'].replace(
    'Les dix alinéas initiaux gardent leurs positions ; transition au onzième.',
    'Les dix alinéas initiaux gardent leurs positions ; la transition est rattachée au dixième, qui demeure le dernier.').replace(
    "L441-1-6 conserve, hors lot, sa convention et sa commission propres ; leur éventuel allègement exige une coordination distincte, non prétendue achevée.",
    "La source officielle de L441-1-6 conserve sa convention et sa commission propres. Sa proposition publique, lue en entier, retire déjà sa commission distincte, sans abolir la convention, et doit être conservée à l'assemblage. Notre suppression porte sur l'autre commission, celle de l'accord L441-1-1 ; aucune instance supprimée dans la convention n'est rétablie.")
answers['L441-1-3']['review_notes'] = answers['L441-1-3']['review_notes'].replace(
    'Les trois alinéas sont conservés à leur place, transition finale.',
    "Les trois alinéas sont conservés à leur place ; la transition est rattachée au troisième, qui reste le dernier. Le renvoi exprès du dernier alinéa de L441-1-6 au dernier alinéa de L441-1-3 continue ainsi de viser le délégué spécial, et non un alinéa transitoire distinct.")
answers['L441-2-8']['review_notes'] = answers['L441-2-8']['review_notes'].replace(
    'Les onze alinéas sources conservent leur place, un IV transitoire étant ajouté.',
    "Les onze alinéas sources conservent leur place ; la transition est rattachée au dernier alinéa du III. Les renvois aux troisième alinéa du I et premier alinéa du III restent donc exacts.")
answers['L441-2-9']['substantive_impact']['new_burdens_review'] = answers['L441-2-9']['substantive_impact']['new_burdens_review'].replace(
    "l'alinéa final limite", "l'encadrement ajouté à l'introduction limite")
answers['L441-2-2']['review_notes'] += " La proposition publique de L441-1, lue en entier, retire le taux minimal de 50 % en QPV ; le maintien de L441-2-2 ne permet pas de rétablir ce taux ni une restriction équivalente, et sa garantie d'offre adaptée reste distincte."
answers['L441-2-5']['review_notes'] += " Distinction source/projet : la proposition publique de L441-1, lue en entier, supprime déjà son bilan annuel distinct des désignations et les envois semestriels ; la sauvegarde des bases autonomes du présent article ne les rétablit pas. Son trente-troisième alinéa proposé vise encore les comptes rendus de L441-2-5 : ce compagnon hors lot doit viser seulement les comptes rendus déjà établis et les données légalement disponibles, sans nouveau rapport."
answers['L441-1-1']['review_notes'] += " Compagnons réglementaires lus en entier : R441-16-4 doit cesser d'imposer l'examen des dossiers DALO par la commission de cet accord, et R441-2-15 I et V 4° doit conserver les avis historiques et les accès nécessaires aux fonctions maintenues sans recréer un secrétariat ou des avis obligatoires de l'instance supprimée. Ces textes ne sont pas modifiés dans ce dossier."
for n in ['L441-2-7', 'L441-2-8', 'L441-2-9']:
    answers[n]['review_notes'] += " R441-2-10 et R441-2-15 ont été lus en entier avec leurs notes : le 3° et le dernier alinéa de R441-2-10 doivent perdre le calendrier de signature obligatoire et la contractualisation imposée, sans supprimer les fonctions du dispositif, la cotation, l'accueil et les garanties d'accès aux données. Ces coordinations réglementaires hors lot sont identifiées et non présentées comme rédigées."
answers['L441-2-3-4']['review_notes'] = answers['L441-2-3-4']['review_notes'].replace(
    "Ce dernier est une cible facultative non fournie dans reference-targets et demeure à coordonner dans son propre article, notamment son premier alinéa.",
    "Ce dernier est une cible facultative non fournie dans reference-targets. Sa proposition publique, également lue en entier, corrige déjà le premier alinéa en visant les obligations de relogement incombant effectivement à l'Etat selon L521-3-1 ou L521-3-2 ; ce projet n'est pas le droit en vigueur et doit être conservé à l'assemblage sans modification de ce fichier.").replace(
    "La correction directe de L521-3-3 est hors lot et reste identifiée.",
    "La correction directe de L521-3-3 est hors lot et reste identifiée dans sa proposition publique.")
answers['L441-2-3-4']['substantive_impact']['scope_limitations'] = answers['L441-2-3-4']['substantive_impact']['scope_limitations'].replace(
    "La correction directe de L521-3-3 est hors lot et reste identifiée.",
    "La correction directe de L521-3-3 reste hors lot ; sa proposition publique a été lue et son assemblage doit être coordonné.")

# Contrôles sémantiques des seules cibles requises, avec leurs empreintes exactes.
contexts = {
    'L432-1': "L432-1 règle la construction et le financement d'habitations communales pour familles nombreuses et le choix du gestionnaire HLM.",
    'L432-2': "L432-2 règle les prêts, les droits des associés et la dévolution des réserves d'une coopérative de construction ; l'associé n'est pas ici un salarié.",
    'L432-3': "L432-3 ouvre des dispositions financières HLM à des sociétés de bains-douches agréées ; il ne règle pas leurs contrats de personnel.",
    'L432-4': "L432-4 étend des dispositions de prêts aux mutualistes et associations ayant reçu les financements désignés ; aucun emploi n'est constitué par ce prêt.",
    'L433-2': "L433-2 porte sur l'acquisition et la vente d'immeubles à construire ou à rénover, avec limite de 30 % du programme pour les ventes privées.",
    'L441-2-3-3': "L441-2-3-3 porte sur une dette du propriétaire ou exploitant défaillant envers l'Etat ayant relogé des occupants, non sur une dette d'employeur envers un salarié.",
    'L441-2-3-4': "L441-2-3-4 porte sur le relogement public après arrêté visant des locaux dangereux ou insalubres, non sur une rupture de contrat de travail."
}
for n, a in answers.items():
    key = a['code_id'] + '|' + a['source_id']
    for target_key in refs['requirements'][key]:
        t = refs['targets'][target_key]
        tn = t['number']
        if tn == 'L1234-1':
            analysis = (contexts[n] + " L1234-1 officiel fixe le préavis de licenciement selon l'ancienneté ; sa proposition vise quinze jours calendaires pour les nouveaux contrats privés et garde les règles antérieures pour les anciens. Ce préavis suppose la notification régie par L1234-3 proposé, dont le texte n'est pas fourni ici, et ne remplace ni un délai locatif ni une procédure collective. Aucun renvoi à L1234-1 n'est à introduire dans cet article du logement.")
        elif tn == 'L1221-2':
            analysis = (contexts[n] + " L1221-2 officiel admet encore les CDD dans leur champ ; sa proposition institue le contrat unique indéterminé pour les nouvelles embauches privées et protège les anciens contrats. Une durée de prêt, de programme, de vente ou de relogement ne fixe pas un terme d'emploi. L'article examiné ne crée donc aucun CDD et ne doit pas recevoir artificiellement ce renvoi professionnel.")
        elif tn == 'L1234-9':
            analysis = (contexts[n] + " L1234-9 officiel ouvre l'indemnité de licenciement à huit mois hors faute grave ; la proposition distingue les contrats nouveaux, seuil d'un an au terme effectif préavis inclus, puis 0,20 mois par année totale au prorata des mois complets, plafond six mois, employeur seul, et protège les parts anciennes et indemnités spéciales. Ces règles d'ancienneté et de rupture notifiée sont inapplicables à cette créance ou opération de logement ; aucun de ces montants n'y est importé.")
        elif tn == 'L442-7':
            analysis = (contexts[n] + " L442-7 n'est fourni qu'en texte officiel : il vise une clause de fonction dans certains logements attribués sur proposition d'employeurs, pour agents publics ou salariés des établissements ou transports expressément désignés. L'employeur peut demander la résiliation dans l'année après fin d'emploi ; le bailleur notifie au locataire un préavis d'au moins six mois, avec prolongation exceptionnelle et maintien lié au handicap. Ce texte ne porte pas un avantage financier de construction. Son renvoi ancien est retiré sans remplacer ses six mois locatifs par quinze jours de travail ni étendre le contrat privé aux agents publics.")
        elif tn == 'L261-1':
            analysis = (contexts[n] + " L261-1 officiel reproduit la définition civile de la vente d'immeuble à construire, à terme ou en VEFA ; sa proposition ne change pas cette qualification. Le délai contractuel est celui d'édification de l'immeuble, non une durée d'emploi. Le renvoi de L433-2 au régime L261-1 à L261-22 conserve donc cet objet immobilier sans relever de l'ancienneté, de la notification ou de l'indemnité du contrat unique.")
        elif tn == 'L261-12':
            analysis = (contexts[n] + " L261-12 officiel et proposé interdisent les versements VEFA avant signature ou exigibilité et protègent les dépôts à terme sur compte spécial, incessibles, insaisissables et indisponibles sauf prix. Ces garanties restent dans la plage L261-1 à L261-22 malgré la suppression de l'autorisation préfectorale de vente. Elles ne sont ni un salaire ni une indemnité liée à l'ancienneté et ne sont pas remplacées par une règle de rupture notifiée d'emploi.")
        elif tn == 'L261-14':
            analysis = (contexts[n] + " L261-14 officiel et proposé plafonnent à 10 % du prix l'indemnité forfaitaire de résolution imputable à une partie, tout en conservant la réparation du préjudice effectivement subi. C'est la résolution d'une vente immobilière, non le licenciement d'un salarié. Le renvoi de plage de L433-2 conserve donc ce plafond et ce recours ; ni seuil d'un an, ni notification à quinze jours, ni plafond de six mois de salaire ne peuvent s'y substituer.")
        elif tn == 'L521-3-2':
            if n == 'L441-2-3-3':
                analysis = ("Le renvoi vise réellement le IV pour l'indemnité de relogement et le VI pour le recouvrement après défaillance du propriétaire ou exploitant. Le IV officiel fixe un an de loyer prévisionnel ; la proposition retient les frais effectivement engagés dans cette limite, sans double recouvrement et avec réinstallation de l'occupant distincte. Le corps de L441-2-3-3 est coordonné à cette mesure et au VIII proposé : nouveaux relogements à l'entrée en vigueur, anciens faits sous droit antérieur même payés plus tard. Ce n'est pas une indemnité patronale liée à l'ancienneté ou à la notification d'un licenciement.")
            else:
                analysis = ("Le renvoi porte sur la substitution de l'autorité publique au propriétaire défaillant après interdiction d'habiter, aux I, III ou V applicables de L521-3-2 ; le II est déjà abrogé dans la source officielle et dans la proposition. La source officielle de L521-3-3, lue au corpus, vise encore ce II en son premier alinéa ; sa proposition publique, lue en entier, corrige déjà ce point pour les obligations incombant effectivement à l'Etat. L441-2-3-4 explicite son application dans le champ du présent article, sans rétablir le II. La réforme indemnitaire du IV et la transition du VIII proposé gardent leur champ autonome ; aucune condition d'ancienneté ni notification de rupture privée n'est applicable aux occupants.")
        else:
            raise AssertionError(tn)
        a['reference_checks'].append(dict(target_key=target_key,
                                          view_sha256=t['view_sha256'], assessment=analysis))


ordered = [answers[s['number']] for s in sources]
(ROOT / 'answer.json').write_text(json.dumps(ordered, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(ordered)} articles')
