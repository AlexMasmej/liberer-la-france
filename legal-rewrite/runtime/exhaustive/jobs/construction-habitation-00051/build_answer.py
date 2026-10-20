import json
import re
import html
from pathlib import Path

SOURCES = json.loads(Path('source.json').read_text())
REFS = json.loads(Path('reference-targets.json').read_text())
BY_NUMBER = {a['number']: a for a in SOURCES}
ANSWERS = {}


def plain(xml):
    return html.unescape(re.sub(r'<[^>]+>', '', xml or ''))


def paragraphs(*texts):
    return ''.join('<p>' + html.escape(t, quote=False) + '</p>' for t in texts)


def base(number, reason, review):
    a = BY_NUMBER[number]
    return {k: a[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')} | {
        'proposed_xml': None, 'reason': reason, 'review_notes': review,
        'status': 'rewrite_draft', 'reference_checks': []}


def impact(classification, assessment, limitations, burdens, effects=None):
    return {'version': 1, 'classification': classification, 'assessment': assessment,
            'scope_limitations': limitations, 'new_burdens_review': burdens,
            'effects': effects or []}


def effect(kind, measure, description, before, after, unit, population, transition,
           burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure, description=description,
                before=before, after=after, unit=unit, affected_population=population,
                conditions_and_transition=transition,
                replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


def retain(number, reason, review, assessment, limitations, burdens, benefit=None):
    a = base(number, reason, review)
    a.update(status='retained_unchanged', classification='retained_necessary')
    a['substantive_impact'] = impact('retained_necessary', assessment, limitations, burdens)
    if benefit:
        a['benefit_review'] = benefit
    ANSWERS[number] = a


def rewrite(number, xml, reason, review, classification, assessment, limitations,
            burdens, effects, removed=None, repeal_scope=None, benefit=None):
    a = base(number, reason, review)
    a['proposed_xml'] = xml
    a['substantive_impact'] = impact(classification, assessment, limitations, burdens, effects)
    if removed:
        a.update(change_type='normative_reduction',
                 reform_policy_id='editorial_direction_2026_10_19',
                 removed_provisions=removed)
    if repeal_scope:
        a.update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19',
                 repeal_scope=repeal_scope)
    if benefit:
        a['benefit_review'] = benefit
    ANSWERS[number] = a


SLS = 'supplement-loyer-solidarite-suppression'
NO_NEW_SLS = "Aucune charge nouvelle identifiée : aucune taxe, déclaration ou garantie de remplacement ; les droits anciens et les finalités locatives autonomes sont seuls conservés."
SLS_CONTEXT = "Coordination de la proposition actuelle de L. 441-3 lue dans le corpus public : abolition du supplément pour les périodes d'occupation à compter de l'entrée en vigueur, tous bailleurs et baux concernés. Cette proposition n'est pas le droit positif. Les renvois de calcul historiques ne peuvent fonder une perception future. Une seule mesure de suppression du SLS est suivie, sans addition de gains par article d'exécution."

retain('L441-3-2',
       "Maintien intégral, sans réécriture de style, de la faculté de financer des remises de loyer pour les locataires en difficulté. L'abolition proposée du supplément ne justifie pas de supprimer cette faculté favorable : les produits antérieurs peuvent encore financer des remises nouvelles. La mention sur la quittance permet au locataire de constater son avantage et de contrôler sa dette.",
       SLS_CONTEXT + " Le deuxième alinéa de L. 441, lu en entier, vise l'égalité d'accès et les besoins des ménages ; il ne rétablit pas les quotas communaux abrogés. Aucun nouveau produit de SLS ni crédit budgétaire n'est créé. La faculté de remise ne devient pas une obligation de financement illimité ; les autres remises ayant un fondement autonome restent possibles.",
       "La source entière est conservée : affectation facultative favorable et traçabilité de la remise sur la quittance, sans nouveau prélèvement ni gain compté.",
       "Le financement par les anciens produits dépend des sommes disponibles ; son renouvellement et le coût des remises ne sont pas chiffrés. Aucun examen des 209 articles SRU n'est déclaré achevé.",
       "Aucune charge nouvelle identifiée : maintien des deux alinéas officiels, sans fichier, démarche ni condition d'emploi nouvelle.",
       "La remise au bénéfice des locataires en difficulté économique et sociale est maintenue pour les attributions futures aussi, sur les produits antérieurs disponibles. Sa mention expresse sur la quittance protège la preuve de la réduction et ne conditionne pas la suppression générale du SLS.")

xml = paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant la présente réforme.",
    "Aucun supplément de loyer de solidarité n'est dû au titre des périodes d'occupation à compter de cette entrée en vigueur, y compris en exécution d'un bail antérieur. Le loyer principal et les charges locatives conservent leur régime ; la suppression du supplément ne constitue pas un fondement de leur augmentation.",
    "Les seules périodes d'occupation antérieures restent soumises aux règles de calcul et de plafonnement qui leur étaient applicables. Sont notamment conservés le calcul par application du coefficient de dépassement au supplément de loyer de référence, le plafond de 30 % des ressources de l'ensemble des personnes vivant au foyer pour le cumul du loyer principal et du supplément, ainsi que le plafond par mètre carré de surface habitable tenant compte des loyers moyens de la zone, applicable aux locataires qui, lors de la conclusion d'un bail conforme à la convention en application de l'article L. 353-7, avaient des ressources supérieures aux plafonds en vigueur pour l'attribution de leur logement.",
    "Ces règles demeurent applicables aux liquidations et régularisations ultérieures des sommes anciennes, à leur recouvrement, aux restitutions, prescriptions et recours. Pour une période d'occupation en cours lors de l'entrée en vigueur, seule sa fraction antérieure peut donner lieu au supplément. Aucun remboursement général des sommes antérieurement dues n'est institué.")
rewrite('L441-4', xml,
        "Abrogation prospective du calcul du SLS, en coordination avec son abolition dans L. 441-3. Les plafonds favorables de 30 % et par mètre carré ne sont pas retirés des dettes anciennes ; pour les périodes nouvelles, l'absence de tout supplément est plus favorable que leur application. Il s'agit d'une coordination de la même suppression, non d'une deuxième taxe supprimée.",
        SLS_CONTEXT + " Les trois alinéas sont lus. Le plafond particulier reste réservé aux personnes et au moment du conventionnement définis par la source ; L. 353-7 a été lu en entier, source et projet distincts. Ni la fixation du loyer principal ni les avantages liés au refus du nouveau bail ne sont modifiés. Coordonner les règles de calcul de R. 441-19 à R. 441-21 et les arrêtés hors lot ; ils ne sont pas déclarés réécrits ici.",
        'coordination_only',
        "L'article de calcul ne peut plus rétablir le SLS futur supprimé par la réforme ; ses deux plafonnements demeurent opposables sur l'ancien stock. Aucun gain supplémentaire n'est ajouté à l'abolition principale.",
        "Ne supprime ni loyer principal ni charges ordinaires. La perte de recettes du SLS et l'incidence sur les remises restent à évaluer au niveau de la mesure, sans montant national présumé.",
        NO_NEW_SLS,
        [effect('coordination', SLS, "Neutralisation prospective de la formule et maintien des plafonds historiques.",
                "SLS calculé par coefficient de dépassement et référence du logement, sous plafond de 30 % des ressources ou plafond particulier par mètre carré ; aucun taux fiscal unique.",
                "Aucun SLS pour les périodes nouvelles ; formules et plafonds antérieurs pour les seules périodes anciennes.",
                'legal_duty', "Locataires soumis au SLS, y compris ceux devenus conventionnés avec ressources supérieures aux plafonds.",
                "Périodes d'occupation à compter de l'entrée en vigueur ; fraction ancienne, restitutions et recours protégés.",
                "Aucun prélèvement ni formalité de remplacement.",
                "Ce montant est plafonné lorsque, cumulé avec le montant du loyer principal, il excède 30 % des ressources de l'ensemble des personnes vivant au foyer.",
                "Aucun supplément de loyer de solidarité n'est dû au titre des périodes d'occupation à compter de cette entrée en vigueur, y compris en exécution d'un bail antérieur.")],
        repeal_scope="Calcul du supplément de loyer de solidarité pour toutes les périodes d'occupation nouvelles ; plafonds et règles de liquidation conservés uniquement pour les périodes anciennes.")

xml = paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant la présente réforme.",
    "Aucun coefficient de dépassement du plafond de ressources ni supplément de loyer de référence ne peut fonder un supplément de loyer de solidarité au titre d'une période d'occupation à compter de cette entrée en vigueur.",
    "Pour les seules périodes d'occupation antérieures, le supplément reste calculé par le bailleur selon les valeurs du coefficient de dépassement du plafond de ressources déterminées par décret en Conseil d'Etat et le montant par mètre carré habitable du supplément de loyer de référence fixé par décret en Conseil d'Etat selon les zones géographiques tenant compte du marché locatif. Les dispositions favorables de l'article L. 441-3-1, les autres exemptions et les plafonnements applicables à ces périodes sont conservés.",
    "Les liquidations, régularisations, créances, restitutions, prescriptions et recours relatifs à ces périodes restent régis par leurs règles antérieures, même lorsqu'ils interviennent après l'entrée en vigueur. Seule la fraction antérieure d'une période d'occupation en cours à cette date peut donner lieu au supplément. Aucun remboursement général des sommes antérieurement dues n'est institué.")
rewrite('L441-8', xml,
        "Retrait prospectif de la formule réglementaire du SLS devenu supprimé. Les paramètres de marché, la surface et la dérogation favorable de L. 441-3-1 restent utilisables pour régler les seules dettes anciennes. Coordination de fond, sans taux nouveau ni deuxième réduction comptabilisée.",
        SLS_CONTEXT + " Les deux facteurs et la réserve initiale ont été lus. L. 441-3-1, lu intégralement, conserve notamment la faculté d'exclusion géographique pour les anciennes périodes concernées ; l'abolition générale n'enferme pas les futurs locataires dans une exemption plus étroite. R. 441-26 conserve encore un coefficient de liquidation provisoire et une indemnité : son champ doit être borné aux anciennes périodes avec L. 441-9, sans coefficient futur de substitution.",
        'coordination_only',
        "La formule d'exécution est neutralisée pour l'avenir dans la même mesure SLS, sans suppression d'un second prélèvement. Le calcul historique complet reste disponible pour les créances et restitutions anciennes.",
        "Les règles de loyer principal, les obligations locatives indépendantes et leurs contrôles ne sont pas supprimés. Les décrets d'application hors lot restent à coordonner.",
        NO_NEW_SLS,
        [effect('coordination', SLS, "Retrait de la formule réglementaire pour les seules périodes nouvelles.",
                "Coefficient de dépassement multiplié par le supplément de référence au mètre carré, selon les zones et sous réserve de L. 441-3-1.",
                "Formule cantonnée au stock ancien ; aucune assiette de SLS pour l'occupation future.",
                'regime', "Bailleurs calculant le SLS et locataires auparavant redevables.",
                "Bascule à l'entrée en vigueur, avec calcul des fractions anciennes et maintien de leurs avantages.",
                "Aucun barème ni déclaration de remplacement.",
                "Sous réserve des dispositions de l'article L. 441-3-1, le supplément de loyer de solidarité appliqué par l'organisme d'habitations à loyer modéré est calculé par lui en fonction :",
                "Aucun coefficient de dépassement du plafond de ressources ni supplément de loyer de référence ne peut fonder un supplément de loyer de solidarité au titre d'une période d'occupation à compter de cette entrée en vigueur.")],
        repeal_scope="Calcul réglementaire obligatoire du SLS pour les périodes d'occupation futures, avec maintien de la formule et des exemptions sur les seules périodes antérieures.")

a = BY_NUMBER['L441-9']
parts = re.findall(r'<p>(.*?)</p>', a['source_xml'], re.S)
first = plain('<p>'+parts[0]+'</p>')
first = first.replace(
    "L'organisme d'habitations à loyer modéré demande annuellement à chaque locataire communication des avis d'imposition ou de non-imposition à l'impôt sur le revenu et des renseignements concernant l'ensemble des personnes vivant au foyer permettant de calculer l'importance du dépassement éventuel du plafond de ressources et de déterminer si le locataire est redevable du supplément de loyer.",
    "Pour déterminer les droits à la réduction de loyer de solidarité prévue à l'article L. 442-2-1 et apprécier les ressources dans le champ de l'article L. 442-3-3, l'organisme d'habitations à loyer modéré demande annuellement aux seuls locataires relevant de ces dispositions communication des avis d'imposition ou de non-imposition à l'impôt sur le revenu et des renseignements concernant l'ensemble des personnes vivant au foyer strictement nécessaires à ces seules finalités. Il ne demande pas à nouveau les informations et pièces exactes et à jour dont il dispose déjà ou qu'il peut légalement obtenir sans les demander au locataire. Le présent article n'ouvre aucun accès nouveau à des données.")
old_second = plain('<p>'+parts[1]+'</p>')
old_second = "Pour les seules périodes d'occupation antérieures à l'entrée en vigueur de la loi portant la présente réforme, l'organisme peut encore demander les avis et renseignements nécessaires à la liquidation du supplément, dans les conditions de délai, de dispense et de réemploi du premier alinéa. " + old_second
old_third = "Pour ces périodes, " + plain('<p>'+parts[2]+'</p>')[:1].lower() + plain('<p>'+parts[2]+'</p>')[1:]
xml = paragraphs(first, old_second, old_third,
                 "La mise en demeure relative à ces périodes comporte la reproduction du présent article.",
                 "Pour les périodes d'occupation à compter de cette entrée en vigueur, aucune demande ayant pour seul objet le supplément de loyer supprimé, aucune liquidation provisoire de ce supplément et aucune indemnité pour frais de dossier à ce titre ne peuvent être imposées. Les demandes nécessaires aux finalités autonomes du premier alinéa ne peuvent donner lieu à cette liquidation provisoire ni à cette indemnité. Les données sont recueillies sans enquête supplémentaire lorsque celles d'une enquête légalement effectuée permettent déjà de statuer, notamment dans les conditions de l'article L. 442-5.",
                 "Les créances légalement nées pour les périodes anciennes, leurs plafonnements, régularisations, restitutions, prescriptions et recours restent régis par leurs règles antérieures. Aucun supplément ne porte sur la fraction d'occupation postérieure à l'entrée en vigueur. Aucune enquête annuelle exclusivement consacrée au supplément n'est maintenue pour les périodes nouvelles.")
rewrite('L441-9', xml,
        "Coordination effective de l'abolition du SLS : fin de ses demandes exclusives, liquidations provisoires au coefficient maximal et frais de dossier sur les périodes nouvelles. La demande déjà utilisée par L. 442-2-1 et L. 442-3-3 demeure pour leurs finalités autonomes, sans nouvelle enquête de remplacement. Réemploi des informations légalement disponibles : coordination du droit existant, sans gain CRPA nouveau revendiqué. Les dispenses APL et allocations, le mois pour répondre, les quinze jours de mise en demeure historique et le remboursement sous deux mois sont conservés.",
        SLS_CONTEXT + " Les quatre alinéas sont lus et la portée du premier est conservée pour la réduction de loyer et la gestion des ressources, non pour percevoir un SLS futur. L. 442-2-1, L. 442-3-3 et L. 442-5 sont lus en entier ; ce dernier donne déjà valeur commune à son enquête et contient ses sanctions autonomes. Le nouveau renvoi exprès à L. 442-5, non fourni comme cible dans reference-targets.json, est vérifié dans le corpus public. Les renvois exprès ajoutés à L. 442-2-1 et L. 442-3-3 ne figurent pas non plus parmi les cibles fournies dans ce fichier ; leurs corps entiers sont vérifiés dans le lot. Aucun numéro d'identification supplémentaire n'est importé. Coordonner R. 441-26 et les arrêtés d'enquête pour ne pas recréer coefficient maximal ou frais futurs ; L. 442-5-1 doit perdre son seul déclencheur SLS, sans fermeture de l'accompagnement. La déchéance sur simple défaut de réponse est retirée séparément à L. 442-3-4. Le délai locatif de quinze jours n'est pas le préavis du contrat unique.",
        'coordination_only',
        "La source entière comportait une enquête à plusieurs usages, une liquidation provisoire maximale et des frais. Les seuls mécanismes liés au SLS nouveau cessent ; l'enquête utile aux droits et aux ressources conserve son champ et ses dispenses. Pas de seconde réduction ajoutée à l'abolition du SLS ni de gain nouveau pour le réemploi déjà légal.",
        "Les obligations autonomes de L. 442-5 et le contrôle de ressources de L. 442-3-3 ne sont pas supprimés. Les anciennes liquidations et indemnités restent possibles sur leur seule période d'origine ; coût net de gestion non chiffré.",
        "Aucune charge nouvelle identifiée : mêmes types de données, mêmes dispenses et même délai, finalités autonomes déjà expressément utilisatrices de l'enquête ; aucun nouveau registre, accès fiscal ou contrôle d'emploi. Le réemploi est borné aux informations légalement disponibles.",
        [effect('coordination', SLS, "Fin des calculs provisoires et frais liés au seul supplément futur.",
                "A défaut de réponse après un mois puis mise en demeure de quinze jours, SLS provisoire au coefficient maximal réglementaire, plus indemnité de dossier plafonnée par décret.",
                "Aucun SLS provisoire ni frais de ce chef pour les périodes nouvelles ; demande commune maintenue pour RLS et contrôle de ressources existants.",
                'legal_duty', "Locataires et organismes HLM soumis à la demande, avec dispenses APL et allocations maintenues.",
                "Périodes nouvelles à compter de l'entrée en vigueur ; anciennes dettes, indemnités, plafonds, remboursement sous deux mois et recours préservés.",
                "Pas d'enquête supplémentaire ni sanction de remplacement ; les sanctions autonomes d'autres enquêtes restent distinctes.",
                "L'organisme d'habitations à loyer modéré perçoit en outre une indemnité pour frais de dossier dont le montant maximum est fixé par décret en Conseil d'Etat.",
                "Pour les périodes d'occupation à compter de cette entrée en vigueur, aucune demande ayant pour seul objet le supplément de loyer supprimé, aucune liquidation provisoire de ce supplément et aucune indemnité pour frais de dossier à ce titre ne peuvent être imposées.")],
        removed=["Demandes annuelles exclusivement destinées à établir le SLS pour les périodes d'occupation nouvelles.",
                 "Liquidation provisoire au coefficient maximal et indemnité de dossier liées au SLS des périodes nouvelles, sans sanction de remplacement."])

xml = paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant la présente réforme.",
    "La transmission des renseignements statistiques et financiers aux fins du rapport annuel départemental sur le supplément de loyer et la soumission de ce rapport pour avis au comité régional de l'habitat et de l'hébergement cessent à cette date. Aucun envoi, rapport ou avis restant à accomplir sur ce seul fondement n'est exigé après cette date, même s'il porte sur une période antérieure.",
    "Les rapports et renseignements déjà régulièrement transmis n'ont pas à être refaits. Les obligations de conservation légalement autonomes, les contrôles et les communications nécessaires aux créances anciennes conservent leur régime, sans rapport périodique de remplacement. Les actes accomplis, droits, prescriptions et recours relatifs aux périodes antérieures sont préservés, sous réserve de l'application de la loi répressive plus douce aux sanctions non définitives dans son champ.")
rewrite('L441-10', xml,
        "Abrogation du circuit annuel exclusivement consacré au SLS : données à transmettre, rapport départemental et avis régional. Suppression également des envois futurs portant sur l'ancien stock, sans retirer les contrôles autonomes des fonds ni les données utiles aux créances. Coordination de l'abolition principale et non seconde suppression d'enquête comptée à part.",
        SLS_CONTEXT + " R. 441-27, lu en entier, prévoit un arrêté et l'envoi au 1er juin : ce calendrier ne doit pas ressusciter le dépôt. R. 362-2 14°, lu dans l'article entier, doit perdre son avis annuel SLS ; ses autres consultations demeurent. Les arrêtés statistiques extérieurs au lot restent à coordonner. L. 442-5 conserve des finalités autonomes d'occupation sociale, non abrogées par le présent texte.",
        'coordination_only',
        "La totalité du circuit spécifique est retirée pour les transmissions futures, y compris anciennes années. Ce prolongement d'exécution reste rattaché à l'unique mesure SLS, sans chiffrer une seconde baisse.",
        "Ne dispense ni des comptes ni des contrôles autonomes et ne supprime pas l'enquête d'occupation sociale. La charge évitée et la perte de recettes du SLS ne sont pas chiffrées.",
        NO_NEW_SLS,
        [effect('coordination', SLS, "Suppression du rapport et de son circuit spécifique après abolition du SLS.",
                "Transmission des données, établissement d'un rapport chaque année et avis du CRHH sur le supplément.",
                "Plus aucun envoi, rapport ni avis restant dû sur ce seul fondement, même pour une année ancienne.",
                'legal_duty', "Organismes HLM, préfets départementaux et CRHH.",
                "Obligations restant à accomplir dès l'entrée en vigueur ; documents déjà déposés et contrôles indépendants préservés.",
                "Aucun rapport regroupé ou déclaration de remplacement.",
                "Ce rapport est soumis pour avis au comité régional de l'habitat et de l'hébergement.",
                "Aucun envoi, rapport ou avis restant à accomplir sur ce seul fondement n'est exigé après cette date, même s'il porte sur une période antérieure.")],
        repeal_scope="Transmission statistique SLS, rapport annuel départemental et consultation régionale correspondante pour toute formalité restant à accomplir après l'entrée en vigueur.")

xml = paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant la présente réforme.",
    "Aucune pénalité fondée sur l'absence d'exigence ou de diligences de recouvrement d'un supplément de loyer de solidarité ne peut sanctionner un manquement postérieur à cette entrée en vigueur. Aucun renvoi au présent article ne peut rétablir cette pénalité pour ces manquements.",
    "Pour les manquements antérieurs, les sanctions non définitives demeurent soumises aux règles de la loi répressive plus douce dans leur champ d'application. Les sanctions devenues définitives avant l'entrée en vigueur, les créances qui en résultent, leur recouvrement, les restitutions, prescriptions et recours restent régis par les dispositions qui leur sont applicables ; aucune restitution générale des pénalités antérieurement dues n'est instituée.",
    "Le recouvrement des suppléments légalement dus au titre des périodes d'occupation antérieures et les contrôles, responsabilités et sanctions ayant un fondement légal autonome conservent leur régime. Ils ne peuvent servir à rétablir le supplément supprimé ni la pénalité abrogée pour un manquement postérieur à l'entrée en vigueur.")
rewrite('L441-11', xml,
        "Abrogation prospective de la pénalité de 100 % liée au non-recouvrement du SLS, cohérente avec l'abolition du supplément et de ses seules formalités. Le recouvrement des anciennes créances ne recrée pas une pénalité nouvelle par renvoi. La transition distingue sanctions définitives et loi répressive plus douce ; aucune immunité pour des fautes autonomes n'est créée.",
        SLS_CONTEXT + " L. 342-14 I 1° b et R. 441-28 sont lus en entier : leur sanction renvoie au montant de L. 441-11 ; ils doivent être coordonnés pour les faits nouveaux sans substituer le plafond général de deux millions d'euros à la pénalité supprimée. La réserve des obligations du comptable public reste attachée aux manquements anciens. Le délai contradictoire d'un mois de R. 441-28 et les recours restent utiles aux seuls dossiers anciens dans leur champ ; ces articles hors lot ne sont pas réécrits ici.",
        'coordination_only',
        "La pénalité spécifique de 100 % cesse pour les manquements futurs ; elle n'est ni remplacée par une sanction générale sur le même fait ni comptée comme une deuxième taxe supprimée. Les droits anciens et le régime plus doux des sanctions sont distingués.",
        "Aucune suppression des contrôles ANCOLS ni des responsabilités autonomes. Le sort des décisions anciennes dépend de leur caractère définitif et des règles répressives applicables ; aucun rendement n'est estimé.",
        NO_NEW_SLS,
        [effect('coordination', SLS, "Neutralisation de la pénalité spécifique d'exécution du SLS.",
                "Pénalité égale à 100 % des sommes de supplément exigibles et non mises en recouvrement, hors responsabilité propre du comptable public.",
                "Pas de pénalité de ce chef pour les manquements postérieurs ; décisions anciennes définitives et loi plus douce traitées séparément.",
                'percent', "Organismes HLM qui devaient exiger et recouvrer le supplément.",
                "Manquements futurs dès l'entrée en vigueur ; pas de restitution générale des sanctions définitives anciennes.",
                "Aucun plafond général ou sanction équivalente appliqué au seul manquement supprimé.",
                "est passible d'une pénalité dont le montant est égal à 100 % des sommes exigibles et non mises en recouvrement.",
                "Aucune pénalité fondée sur l'absence d'exigence ou de diligences de recouvrement d'un supplément de loyer de solidarité ne peut sanctionner un manquement postérieur à cette entrée en vigueur.")],
        repeal_scope="Pénalité de 100 % pour les manquements futurs à l'exigence et au recouvrement du SLS ; droits anciens définitifs et loi répressive plus douce expressément réservés.")

xml = paragraphs(
    "Pour les seules périodes d'occupation antérieures à l'entrée en vigueur de la loi portant la présente réforme, les dispositions de la présente section restent applicables aux personnes morales autres que les organismes d'habitations à loyer modéré et les sociétés d'économie mixte, pour les logements à usage locatif leur appartenant et ouvrant droit à l'aide personnalisée au logement en application des 2° et 3° de l'article L. 831-1. Les exemptions, plafonnements, régularisations, restitutions, prescriptions et recours applicables à ces périodes sont conservés.",
    "Pour les périodes d'occupation à compter de cette entrée en vigueur, aucun supplément de loyer de solidarité ni aucune formalité exclusivement destinée à son établissement, à son recouvrement ou à son suivi ne peuvent être imposés à ces bailleurs ou à leurs locataires sur le fondement de la présente section ou d'un renvoi à celle-ci. Seule la fraction antérieure d'une période en cours peut donner lieu au supplément selon les règles anciennes.",
    "Les produits antérieurs du supplément peuvent encore financer des remises sur loyer pour les locataires connaissant des difficultés économiques et sociales, y compris lorsque la remise est accordée après l'entrée en vigueur. Ces remises font l'objet d'une mention expresse sur la quittance mensuelle. Les aides au logement et les autres obligations disposant d'un fondement légal autonome conservent leur régime.")
rewrite('L441-13', xml,
        "Limitation temporelle de l'extension du SLS aux autres personnes morales : la section ne peut plus recréer un supplément futur pour les bailleurs non HLM et non SEM visés. Les règles et avantages anciens demeurent pour les anciennes périodes et la faculté favorable de remise reste ouverte après la réforme sur les produits antérieurs. Pas d'enquête nouvelle étendue à ces bailleurs.",
        SLS_CONTEXT + " Les 2° et 3° de L. 831-1 sont lus dans cet article entier et visent les logements locatifs conventionnés ou aidés correspondants, pas les propriétaires du 1° ni les foyers du 5°. R. 441-29, R. 441-30, R. 441-31 et L. 442-10, lus en entier, doivent être coordonnés pour ne pas rouvrir un prélèvement futur ; le plafond ancien majoré de 50 % de L. 442-10 reste un avantage historique distinct à protéger. L. 441-14 conserve intégralement ses exemptions. La remise reproduit ici la faculté existante de la section, sans étendre un financement public ni promettre des recettes nouvelles.",
        'coordination_only',
        "L'extension personnelle du SLS ne fonctionne plus pour les périodes nouvelles. La même suppression générale s'applique aux autres bailleurs visés, sans deuxième taxe supprimée ni réduction d'aides au logement.",
        "Les catégories de L. 831-1 ne sont pas étendues ; les ressources disponibles pour les remises futures ne sont pas garanties. Réglementation et conventions extérieures restent à coordonner.",
        NO_NEW_SLS,
        [effect('coordination', SLS, "Suppression de l'extension du supplément pour les périodes nouvelles.",
                "Application de la section aux autres personnes morales pour leurs logements locatifs relevant de L. 831-1 2° et 3°.",
                "Application aux seules anciennes périodes ; aucun SLS ou circuit exclusif futur pour ces bailleurs, remises favorables conservées.",
                'regime', "Personnes morales autres que HLM et SEM et locataires des logements relevant des 2° et 3° de L. 831-1.",
                "Occupation future dès l'entrée en vigueur, y compris baux antérieurs ; droits, plafonds et recours anciens maintenus.",
                "Aucun prélèvement ni déclaration de remplacement.",
                "Les dispositions de la présente section sont applicables aux personnes morales autres que les organismes d'habitations à loyer modéré et les sociétés d'économie mixte,",
                "Pour les périodes d'occupation à compter de cette entrée en vigueur, aucun supplément de loyer de solidarité ni aucune formalité exclusivement destinée à son établissement, à son recouvrement ou à son suivi ne peuvent être imposés à ces bailleurs ou à leurs locataires sur le fondement de la présente section ou d'un renvoi à celle-ci.")],
        removed=["Extension du SLS et de ses formalités exclusives aux personnes morales non HLM et non SEM pour toute période d'occupation future."])

retain('L441-14',
       "Maintien intégral des exclusions favorables : prêts conventionnés des banques et établissements financiers pour les bailleurs non HLM, immeubles à loyer moyen outre-mer et logements subventionnés par l'ANAH. Elles restent nécessaires à la liquidation et aux litiges anciens ; l'abolition générale du SLS pour l'avenir ne doit pas supprimer leurs avantages historiques.",
       SLS_CONTEXT + " R. 441-31 3° et 5°, lu en entier, reprend ces exclusions. Le maintien de la source n'autorise aucun SLS futur ni aucune collecte supprimée ; L. 441-13 est expressément limité en conséquence. Les aides et conventionnements autonomes restent ouverts aux opérations futures éligibles.",
       "La source entière, exclusivement protectrice, est conservée ; aucune baisse nouvelle n'est attribuée au simple maintien des trois catégories d'exclusion.",
       "L'abolition future est portée par L. 441-3 et ses coordinations, non par une extension silencieuse de ces seules exemptions. Les régimes d'aides indépendants ne sont pas réécrits.",
       "Aucune charge nouvelle identifiée : pas de pièce, délai, agrément ni assiette ajoutés ; les exclusions existantes ne deviennent pas une condition de l'abolition générale.",
       "Les trois exclusions sont conservées dans leur champ exact, y compris l'ANAH sans restriction à une date de subvention inventée. Les périodes anciennes restent exonérées ; pour les futures périodes éligibles, aucun SLS ne renaît, puisque son abolition est générale et sans remplacement.")

xml = paragraphs(
    "Un décret en Conseil d'Etat détermine en tant que de besoin les conditions d'application de la présente section.",
    "Cette habilitation ne permet, pour les périodes d'occupation à compter de l'entrée en vigueur de la loi portant la présente réforme, de rétablir ni supplément de loyer de solidarité, ni coefficient destiné à sa liquidation, ni frais de dossier, enquête, transmission ou rapport exclusivement destiné à son établissement, à son recouvrement ou à son suivi. Les règles d'application nécessaires aux seules périodes anciennes, aux remises favorables et aux finalités autonomes de la demande prévue à l'article L. 441-9 restent possibles dans leur champ légal, sans obligation supplémentaire de remplacement.")
rewrite('L441-15', xml,
        "Coordination de l'habilitation réglementaire afin qu'elle ne rétablisse pas le SLS et ses formalités pour l'avenir. La compétence utile aux anciennes dettes, aux remises et aux finalités autonomes de l'enquête est conservée ; aucune nouvelle démarche ne remplace celles supprimées.",
        SLS_CONTEXT + " Le renvoi exprès ajouté à L. 441-9 n'est pas une cible nouvelle inconnue : il est lu et rédigé dans ce lot, et également fourni en vue officielle dans reference-targets.json. Les règlements R. 441-26 à R. 441-31 et les arrêtés statistiques restent à borner ; ne pas supprimer les exemptions de R. 441-31. La phrase d'habilitation initiale est conservée en entier, suivie de sa limite opératoire.",
        'coordination_only',
        "L'habilitation générale ne peut servir de voie de retour au SLS. Cette borne accompagne la suppression principale et n'est pas une obligation ou autorisation supplémentaire supprimée.",
        "Les décrets et arrêtés ne sont pas tous réécrits dans le présent lot. Les collectes et contrôles disposant d'un fondement autonome ne sont pas abolis par cette seule borne.",
        NO_NEW_SLS,
        [effect('coordination', SLS, "Borne de l'habilitation réglementaire après abolition du supplément.",
                "Habilitation générale d'application de la section, incluant calcul, enquête et suivi du SLS.",
                "Habilitation conservée pour les effets utiles ; aucun rétablissement réglementaire du SLS ou de son circuit exclusif futur.",
                'regime', "Pouvoir réglementaire, bailleurs et locataires du champ de la section.",
                "Périodes nouvelles dès l'entrée en vigueur ; anciens droits et remises futurs sur produits antérieurs maintenus.",
                "Aucune habilitation à créer une formalité équivalente.",
                "Un décret en Conseil d'Etat détermine en tant que de besoin les conditions d'application de la présente section.",
                "Cette habilitation ne permet, pour les périodes d'occupation à compter de l'entrée en vigueur de la loi portant la présente réforme, de rétablir ni supplément de loyer de solidarité, ni coefficient destiné à sa liquidation, ni frais de dossier, enquête, transmission ou rapport exclusivement destiné à son établissement, à son recouvrement ou à son suivi.")],
        removed=["Faculté d'utiliser l'habilitation générale pour reconstituer le supplément et ses formalités exclusives sur les périodes d'occupation nouvelles."])

MIN_RENT = 'hlm-suppression-loyer-minimum-administratif'
a = BY_NUMBER['L442-1']
parts = re.findall(r'<p>(.*?)</p>', a['source_xml'], re.S)
old = plain('<p>'+parts[1]+'</p>')
new = ("Pour les loyers exigibles à compter de l'entrée en vigueur de la loi portant la présente réforme, "
       "en vue d'assurer l'équilibre de la situation financière de ces organismes, elle fixe un montant maximum établi en tenant compte notamment des prix de revient de la construction à la charge desdits organismes et des frais de gestion, de contrôle et d'entretien. "
       "Aucun montant minimum de loyer ne peut être imposé sur le fondement du présent alinéa. "
       "Les plafonds conventionnels et les autres règles protégeant les locataires demeurent applicables. "
       "Les loyers exigibles avant cette entrée en vigueur restent régis par les dispositions antérieures, avec leurs prescriptions, restitutions et recours.")
xml = a['source_xml'].replace('<p>'+parts[1]+'</p>', paragraphs(new))
rewrite('L442-1', xml,
        "Réduction de fond : suppression du minimum administratif général de loyer pour les échéances nouvelles, sans relever le maximum ni le plafond conventionnel. Les quatre autres alinéas sont conservés mot pour mot : prix de base, intervention en difficulté financière, révision annuelle à l'IRL et dérogations encadrées. L'autorisation de dépassement de l'IRL reste nécessaire pour protéger le locataire et ne devient pas une liberté de hausse générale.",
        "Les cinq alinéas sont lus intégralement et restent cinq alinéas : les deux renvois à l'avant-dernier alinéa continuent de viser la révision du quatrième, sans déplacement par une transition finale. Le 3 septembre 1947, le 1er janvier, le deuxième trimestre de l'année précédente, le plafond de 5 % en sus de l'IRL, les deux cas de dérogation et l'accord des associations et locataires de l'article 42 restent inchangés. La suppression du minimum général n'abolit pas l'intervention spéciale de redressement du troisième alinéa, ni les conventions, aides et contrôles financiers autonomes. L. 442-1-1 est coordonné dans ce lot. Les dispositions réglementaires fixant les minima doivent être bornées aux anciennes échéances ; aucune réduction de loyer automatique ou dépense publique chiffrée n'est présumée.",
        'material_reduction',
        "Le plancher général imposable administrativement disparaît pour les nouvelles échéances ; la latitude de baisse augmente réellement. Le maximum, l'IRL, ses dérogations et le pouvoir spécial de redressement subsistent : aucun gel ni baisse de tous les loyers n'est promis.",
        "Ne supprime pas les loyers contractuellement dus, les engagements financiers ni le loyer spécial susceptible d'être imposé en difficulté financière. L'incidence sur recettes des organismes et financement public reste inconnue.",
        "Aucune charge nouvelle identifiée : aucun formulaire, agrément, registre ni justificatif de baisse n'est ajouté ; les bornes et procédures protectrices déjà existantes sont maintenues.",
        [effect('obligation_removed', MIN_RENT, "Fin du montant minimum administratif général, avec plafonds inchangés.",
                "Minimum et maximum administratifs tenant compte des coûts de construction et de gestion ; aucun taux de loyer unique fixé dans l'article.",
                "Seul maximum général maintenu ; aucun minimum imposable au titre du deuxième alinéa pour les loyers nouveaux, sous réserve du redressement spécial et des règles autonomes.",
                'legal_duty', "Organismes HLM et locataires soumis à ce régime de loyer.",
                "Loyers exigibles à compter de l'entrée en vigueur ; anciennes échéances, prescriptions et recours préservés.",
                "Aucune procédure d'autorisation ou déclaration de baisse ajoutée ; plafond et garanties existants inchangés.",
                "elle fixe, pour les loyers, un montant minimum et un montant maximum établis en tenant compte notamment des prix de revient de la construction à la charge desdits organismes et des frais de gestion, de contrôle et d'entretien.",
                "Aucun montant minimum de loyer ne peut être imposé sur le fondement du présent alinéa.")],
        removed=["Montant minimum administratif général des loyers HLM au deuxième alinéa pour les échéances exigibles à compter de l'entrée en vigueur."],
        benefit="Les avantages possibles sont tous conservés : plafonnement maximum des loyers, révision annuelle limitée à l'IRL et date de référence du deuxième trimestre ; pouvoir particulier de rétablissement de l'équilibre pour les organismes en difficulté ; dérogations autorisées pour plan CGLLS ou réhabilitation, plafond de 5 % en sus de l'IRL et possibilité de dépassement avec l'accord des représentants et locataires. Leur accès futur reste ouvert dans les mêmes cas. Le minimum supprimé est une contrainte de prix, non une exonération ou une aide ; sa disparition n'impose aucune hausse et ne prive pas l'organisme du droit de percevoir un loyer contractuel licite.")

a = BY_NUMBER['L442-1-1']
xml = a['source_xml'].replace("dans les limites prévues au deuxième alinéa de l'article L. 442-1",
                             "dans la limite du montant maximum prévu au deuxième alinéa de l'article L. 442-1")
rewrite('L442-1-1', xml,
        "Coordination nécessaire du renvoi à L. 442-1 : la nouvelle location reste libre sous plafond, sans renvoi à un plancher administratif désormais supprimé. Le reste du corps est conservé, notamment loyers conventionnels et plafonds des financements spéciaux. Aucun changement stylistique autonome ni deuxième allègement compté.",
        "L'article entier et le deuxième alinéa de L. 442-1 sont lus. Les trois branches alternatives sont conservées : maximum administratif, maximum de la convention de L. 831-1, plafonds des logements financés à l'aide de primes ou prêts spéciaux du Crédit foncier de France ou de la Caisse centrale de coopération économique. L. 831-1 est lu en entier dans le corpus. La transition est celle des échéances de L. 442-1, et non une remise en cause des loyers déjà dus.",
        'coordination_only',
        "Le renvoi est limité au maximum subsistant. La mesure matérielle est la suppression du plancher dans L. 442-1 ; ce texte n'en constitue pas une seconde et ne supprime aucun plafond favorable.",
        "Les conventions et les financements spéciaux gardent leurs plafonds ; aucune baisse de loyer effective par organisme ni économie nationale n'est démontrée.",
        "Aucune charge nouvelle identifiée : seul l'objet du renvoi est rectifié, sans nouvelle décision, pièce ou condition d'accès au logement.",
        [effect('coordination', MIN_RENT, "Alignement des nouvelles locations sur le seul maximum général subsistant.",
                "Renvoi aux limites du deuxième alinéa de L. 442-1, comprenant un minimum et un maximum.",
                "Renvoi au seul montant maximum, avec les deux autres plafonds spéciaux conservés.",
                'regime', "Organismes HLM concluant de nouvelles locations et leurs locataires.",
                "Coordination avec L. 442-1 pour les loyers exigibles après entrée en vigueur ; stock des anciennes dettes préservé.",
                "Aucun contrôle ou dépôt de remplacement.",
                "dans les limites prévues au deuxième alinéa de l'article L. 442-1",
                "dans la limite du montant maximum prévu au deuxième alinéa de l'article L. 442-1")])

xml = paragraphs(
    "Le présent article est abrogé pour les délibérations relatives aux loyers adoptées à compter de l'entrée en vigueur de la loi portant la présente réforme.",
    "Ces délibérations ne sont soumises ni à la transmission préalable de deux mois aux représentants de l'Etat du département du siège et du département de situation des logements, ni à la demande de nouvelle délibération prévue par le présent article. Aucune déclaration, approbation ni délai d'attente de remplacement n'est exigé sur ce fondement.",
    "Les délibérations adoptées avant cette entrée en vigueur restent régies par les dispositions antérieures, y compris les transmissions, délais et demandes de nouvelle délibération qui leur sont applicables. Les actes régulièrement accomplis, loyers légalement dus, prescriptions, restitutions et recours sont préservés.",
    "Les plafonds légaux et conventionnels, les règles d'information des locataires et les contrôles de légalité et financiers disposant d'un fondement autonome demeurent applicables.")
rewrite('L442-1-2', xml,
        "Abrogation de fond du double envoi préfectoral deux mois avant l'entrée en vigueur des délibérations et du pouvoir spécial de demander une nouvelle délibération dans le mois. Les plafonds substantiels, l'information des locataires et les contrôles autonomes subsistent : la double transmission n'est pas remplacée par une déclaration équivalente. Les délibérations antérieures gardent leur procédure.",
        "Lecture intégrale de la source. Le repère du 1er juillet 1987 décrit le champ historique, pas une date future de réforme. L. 472-3 7°, lu dans l'article entier, transpose ce repère au 1er janvier 2013 pour Mayotte ; il doit être coordonné pour empêcher la survie d'une formalité future par substitution de date. Cette coordination hors lot est identifiée, non présentée comme rédigée. Les plafonds de L. 442-1, les conventions de L. 442-1-1 et la notification de L. 442-2 sont conservés ; le contrôle général ne vaut pas nouvelle approbation particulière.",
        'material_reduction',
        "Deux destinataires obligatoires, une anticipation de deux mois et la procédure particulière de redélibération disparaissent pour les délibérations nouvelles. La portée du contrôle général et la légalité des loyers restent inchangées ; aucun gain monétaire n'est avancé.",
        "Ne dispense pas des transmissions ou contrôles qui ont un fondement autonome, ni de notifier le loyer au locataire. Les délibérations déjà adoptées conservent leur régime antérieur, même si leur prise d'effet est ultérieure.",
        "Aucune charge nouvelle identifiée : suppression sans déclaration, visa, copie ou délai de remplacement ; les obligations autonomes sont seulement réservées.",
        [effect('obligation_removed', 'hlm-fin-transmission-prealable-deliberations-loyers',
                "Fin du double circuit préfectoral préalable et de la redélibération spéciale.",
                "Transmission aux deux préfets deux mois avant prise d'effet ; nouvelle délibération demandable dans le mois de la dernière transmission.",
                "Aucun envoi préalable ni procédure spéciale de redélibération sur ce fondement pour les nouvelles délibérations.",
                'legal_duty', "Organismes HLM fixant leurs loyers et préfectures du siège et des logements.",
                "Délibérations adoptées dès l'entrée en vigueur ; procédures et droits des délibérations antérieures conservés.",
                "Aucune déclaration équivalente ; information des locataires et plafonds existants conservés.",
                "est transmise deux mois avant son entrée en vigueur au représentant de l'Etat dans le département du siège de l'organisme et à celui du département du lieu de situation des logements.",
                "Aucune déclaration, approbation ni délai d'attente de remplacement n'est exigé sur ce fondement.")],
        repeal_scope="Transmission préalable des délibérations de loyers aux deux préfectures, anticipation de deux mois et demande particulière de nouvelle délibération, pour les actes adoptés après entrée en vigueur.")

retain('L442-2',
       "Maintien intégral de la dispense de congé pour appliquer les loyers légaux et de la garantie d'information avant le terme d'usage. La première évite une démarche et protège la continuité de l'occupation ; la seconde empêche l'application d'un nouveau prix avant notification. Aucune formalité redondante ni nouveau prélèvement n'est établi dans cet article.",
       "Les deux alinéas et leur repère historique de 1978 sont lus. La notification de l'article 32 de la loi du 1er septembre 1948 est une garantie locative, distincte des transmissions préfectorales de L. 442-1-2 abrogées pour les délibérations nouvelles. Le renvoi à L. 442-1 reste opérant après suppression de son seul minimum général. Le texte externe de notification n'est pas réécrit et aucun délai numérique qui ne figure pas ici n'est inventé.",
       "La source entière demeure nécessaire : pas de congé obligatoire et effet du loyer seulement après le terme suivant la notification. Aucun allègement nouveau n'est compté.",
       "Ne modifie ni conventions de location ni contenu externe de la notification. Les anciens loyers, recours et règles de prescription restent à leur champ propre.",
       "Aucune charge nouvelle identifiée : maintien strict de la dispense et de sa garantie d'information, sans préavis d'emploi ni justificatif nouveau.")

retain('L442-2-1',
       "Maintien intégral de la réduction de loyer de solidarité, de ses deux tableaux, des revalorisations et de son information sur quittance. La charge du bailleur est la contrepartie directe de la protection des ménages modestes, et non un rapport sans fonction utile. Le renvoi à la demande de L. 441-9 reste cohérent : cette demande conserve expressément sa finalité RLS, indépendamment du SLS supprimé. Aucun nouveau corps à droit constant n'est fabriqué.",
       "Lecture complète des quatorze paragraphes, des deux tableaux et des deux notes : plafonds mensuels 2018 de RLS par zones I/II/III, successivement 50/44/41, 61/54/50, 69/60/56 et 10/9/8 ; plafonds de ressources 1294/1209/1171, 1559/1474/1426, 1984/1880/1823, 2361/2239/2173, 2890/2749/2654, 3334/3173/3069, 3712/3532/3410, 4109/3910/3778, puis 400/375/350 par personne supplémentaire. Ce sont des plafonds historiques indexés, pas les montants actuels de l'arrêté ni un barème nouvellement fixé. Les renvois aux troisième et neuvième alinéas, l'indexation IRL de la RLS, le minimum annuel de revalorisation, l'indexation IPC hors tabac des ressources avec repères du 1er octobre, le zonage APL, la faculté colocation, l'exclusion des logements-foyers du 5° de L. 831-1 et les ressources de L. 823-1 sont conservés sans déplacement. Les notes imposent l'application aux contrats en cours et rappellent le 1er février 2018 ; ce n'est pas la date de la présente réforme. Les montants d'arrêté et la coordination APL/RLS extérieure à cet article ne sont pas recalculés.",
       "La source entière est maintenue pour protéger une réduction de loyer et ses actualisations futures. La demande existante reste disponible ; ni nouveau seuil d'emploi ni baisse nouvelle de prélèvement ne résulte de ce maintien.",
       "Les arrêtés fixant les montants effectifs ne sont pas remplacés par les tableaux de 2018. L'effet global sur bailleurs, APL et finances publiques n'est pas chiffré.",
       "Aucune charge nouvelle identifiée : même réduction, mêmes données nécessaires, mêmes tableaux, indexations et mention sur quittance. Pas de demande supplémentaire ni de lien avec l'ancienneté professionnelle.",
       "La RLS et les majorations par personnes à charge restent ouvertes à tous les futurs foyers éligibles ; les indexations des montants et des plafonds, le zonage, les modalités favorables possibles en colocation et l'application aux baux en cours sont conservés. La suppression du SLS ne peut supprimer cet avantage distinct ni sa voie de détermination par la demande commune.")

a = BY_NUMBER['L442-3']
old_ii = "II.-Lorsque des travaux d'économie d'énergie sont réalisés par le bailleur dans les parties privatives d'un logement ou dans les parties communes de l'immeuble, une contribution pour le partage des économies de charge peut être demandée au locataire du logement loué, à partir de la date d'achèvement des travaux, sous réserve que ces derniers lui bénéficient directement et qu'ils lui soient justifiés. Elle ne peut toutefois être exigible qu'à la condition qu'un ensemble de travaux ait été réalisé ou que le logement atteigne un niveau minimal de performance énergétique."
new_ii = ("II.-Aucune contribution pour le partage des économies de charge ne peut être instituée pour les travaux dont l'exécution commence à compter de l'entrée en vigueur de la loi portant la présente réforme. "
          "Les contributions valablement convenues avant cette entrée en vigueur ainsi que les contributions relatives aux travaux dont l'exécution a commencé avant cette date restent soumises aux règles suivantes : "
          + old_ii[len('II.-'):][:1].lower() + old_ii[len('II.-')+1:])
xml = a['source_xml'].replace(old_ii, html.escape(new_ii, quote=False))
xml += paragraphs("La suppression de la contribution pour les travaux nouveaux ne permet ni de récupérer leur coût au titre des charges du I en dehors de la liste et des dérogations légales, ni d'augmenter le loyer en dehors de son régime propre. Elle ne modifie ni les aides à la rénovation ni les exonérations et dérogations disposant d'un fondement autonome. Les créances légalement nées pour les travaux antérieurs ou les contributions valablement convenues avant l'entrée en vigueur, leurs plafonds, durées, justifications, contrôles, prescriptions, restitutions et recours sont conservés ; aucune restitution générale des sommes antérieurement dues n'est instituée.")
assert xml != a['source_xml']
rewrite('L442-3', xml,
        "Réduction de fond de la contribution locative au partage des économies d'énergie : aucune contribution instituable pour les travaux commencés après l'entrée en vigueur, sous protection des conventions antérieures valables. Le I reste intégralement conservé avec les exclusions de malfaçon, les dépenses récupérables, les accords locaux, les coûts TTC et l'information sur l'eau. Les conditions et plafonds complets du II restent écrits pour les travaux anciens et les conventions acquises. Le locataire est libéré d'une charge privée, mais le coût des travaux n'est pas réduit : le financement restant au bailleur conduit au classement financing_transfer, sans baisse fiscale ni économie nationale revendiquée.",
        "Lecture entière des dix paragraphes et de la note de l'ordonnance 2020-71, dont le 1er juillet 2021 est un repère d'entrée en vigueur historique. Le I, ses renvois à L. 134-3, à l'article 42 de la loi de 1986 et à CGCT L. 2224-12-1 sont conservés mot pour mot. Le II conserve pour son champ transitoire bénéfice direct, justification, ensemble de travaux ou performance minimale, achèvement, quinze ans maximum, montant fixe non révisable, moitié de l'économie estimée, mentions sur avis et quittance, avis de la Commission nationale de concertation et contrôle après travaux. R. 442-24 à R. 442-30 ont été lus en entier : concertation, premier mois suivant achèvement, nouveau locataire, travaux éligibles, calcul et forfaits, attestations restent à borner aux mêmes travaux et conventions ; leur formule et leurs niveaux ne sont pas inventés. Ces règlements et les arrêtés correspondants ne sont pas déclarés réécrits. Le 8° de L. 472-3 adapte l'ancien repère de 1982 pour Mayotte sans modifier ce nouveau périmètre. Financement des travaux futurs, aides, charges des bailleurs et incidence énergétique restent à chiffrer ; aucune compensation ni retrait d'aide décidé ici.",
        'financing_transfer',
        "La contribution financière spécifique disparaît pour les travaux nouveaux non couverts par une convention antérieure valable. La part que le bailleur pouvait récupérer reste à financer par lui : transfert de financement privé, sans réduction démontrée du coût réel des travaux ou d'un prélèvement public. Les charges récupérables du I et les garanties anciennes restent écrites.",
        "Les travaux déjà commencés et les conventions antérieures valables peuvent encore donner lieu à contribution dans les limites existantes. Le coût supporté par les bailleurs, les décisions d'investissement et le solde public net ne sont pas établis.",
        "Aucune obligation documentaire nouvelle identifiée : pas de déclaration de chantier, registre ou accès aux données créé ; dates et conventions s'apprécient sur les pièces existantes. Une charge économique de remplacement est identifiée : le financement propre du bailleur augmente de la part auparavant récupérable, à travaux et aides inchangés. Son montant et le solde net restent inconnus ; aucune économie nationale n'est revendiquée.",
        [effect('financing_transfer', 'hlm-fin-contribution-economies-energie-travaux-nouveaux',
                "Fin de la contribution locative spécifique pour les travaux futurs, hors conventions anciennes valables.",
                "Contribution demandable après travaux bénéficiant au locataire, fixe et non révisable, au plus moitié de l'économie d'énergie estimée et quinze ans ; aucun taux fiscal.",
                "Aucune contribution instituable pour les travaux commencés après entrée en vigueur, sauf convention antérieure valable ; la part non récupérable reste financée par le bailleur, avec aides autonomes inchangées. Anciennes opérations et plafonds conservés.",
                'financing', "Locataires HLM et bailleurs réalisant des travaux d'économie d'énergie.",
                "Commencement d'exécution après entrée en vigueur ; travaux antérieurs, conventions valables, créances et recours anciens protégés.",
                "Pas de nouvelle contribution ni récupération déguisée ; financement propre du bailleur potentiellement accru, non chiffré.",
                "une contribution pour le partage des économies de charge peut être demandée au locataire du logement loué, à partir de la date d'achèvement des travaux, sous réserve que ces derniers lui bénéficient directement et qu'ils lui soient justifiés.",
                "Aucune contribution pour le partage des économies de charge ne peut être instituée pour les travaux dont l'exécution commence à compter de l'entrée en vigueur de la loi portant la présente réforme.")],
        removed=["Contribution spécifique du locataire au partage des économies d'énergie pour les travaux commencés après l'entrée en vigueur, hors conventions antérieures valables."],
        benefit="Les avantages des locataires restent entiers : exclusion des charges causées par erreur de conception ou vice de réalisation, liste limitative des charges, information sur eau et qualité, bénéfice direct et justification des anciens travaux, montant non révisable limité à la moitié des économies estimées et quinze ans. La dérogation favorable par accord collectif local sur sécurité ou développement durable reste disponible pour les accords futurs. Le mode TTC et la définition des prestations d'ascenseur restent inchangés. La faculté du bailleur de demander la contribution est un financement prélevé sur le locataire, non une exonération fiscale : elle est supprimée seulement pour les travaux nouveaux non couverts par convention antérieure valable ; les aides et exonérations autonomes de rénovation ne sont pas retirées.")

a = BY_NUMBER['L442-3-1']
xml = a['source_xml'].replace("l'article 13 bis de la même loi", "l'article 13 bis de la loi n° 48-1360 du 1er septembre 1948")
rewrite('L442-3-1', xml,
        "Coordination du renvoi préexistant à une « même loi » sans antécédent identifié dans l'article : la loi du 1er septembre 1948 est nommée, comme dans L. 442-3-2. Le relogement à loyer principal inférieur, l'aide à la mobilité et toutes les protections contre une déchéance injustifiée sont conservés. Pas de réécriture de vocabulaire ni d'allègement fictif de procédure revendiqué.",
        "Les six alinéas sont lus et conservés dans leur ordre. La concordance de l'article 13 bis est étayée par L. 442-3-2, lu en entier : pas de nouvelle cible matérielle créée, seulement identification explicite de la loi déjà visée ; le texte externe n'est pas réécrit. Trois offres conformes, zones tendues, six mois, plus de soixante-cinq ans, handicap du locataire ou à charge, perte d'autonomie du locataire ou à charge, ainsi que QPV actuel ou à l'emménagement sont conservés. R. 442-3-1 et R. 442-3-2 sont lus en entier : notifications de situation et aide à la mobilité ne sont pas supprimées ; l'accès au logement adapté et les droits futurs sont utiles. L. 442-5-2 conserve son examen triennal autonome ; aucune suppression de quota SRU ne justifie de fermer ces aides.",
        'coordination_only',
        "La seule modification identifie la loi qui fournit les conditions de l'offre de relogement. La règle de sous-occupation et ses garanties demeurent ; aucune obligation ou délai nouveau n'est supprimé.",
        "Ne modifie ni la définition externe de sous-occupation ni le contenu de l'article 13 bis de 1948. Aucune réduction de coût ou de délais de relogement n'est démontrée.",
        "Aucune charge nouvelle identifiée : même nombre d'offres, même délai, mêmes catégories protégées et aide ; la référence explicite ne crée aucun document à produire.",
        [effect('coordination', 'hlm-relogement-reference-loi-1948',
                "Identification explicite du fondement des conditions des offres.",
                "Référence à l'article 13 bis de la même loi sans loi nommée dans cet article.",
                "Référence à l'article 13 bis de la loi n° 48-1360 du 1er septembre 1948, sans changement des offres ou garanties.",
                'regime', "Bailleurs et locataires HLM en situation de sous-occupation.",
                "Correction du renvoi, sans remise en cause des offres ou droits déjà valables.",
                "Aucun dépôt ni condition supplémentaire.",
                "l'article 13 bis de la même loi",
                "l'article 13 bis de la loi n° 48-1360 du 1er septembre 1948")])

retain('L442-3-2',
       "Maintien intégral d'un dispositif assurant la disponibilité de logements adaptés lorsque leur occupant handicapé les a quittés, tout en garantissant une offre sans plafond de ressources, un loyer principal inférieur et une aide à la mobilité. La procédure de trois offres conformes et les protections temporelles et d'âge ont une fonction concrète pour les deux catégories de ménages ; aucune autorisation ou collecte doublonnée n'est imposée ici.",
       "Les cinq alinéas sont lus. Conserver les trois offres de l'article 13 bis de la loi de 1948, les six mois ordinaires, les dix-huit mois après décès d'une personne handicapée à charge et l'exemption des plus de soixante-cinq ans. L'allongement lié au décès est une protection locative, pas une taxe de succession ni une indemnité de rupture d'emploi. R. 442-3-2, lu entièrement, maintient l'aide au déménagement, les forfaits, branchements, dépôt, travaux et accompagnement dans leur champ ; aucune aide n'est réservée aux situations antérieures. Le renvoi au code de l'action sociale porte sur le handicap et non sur le contrat de travail.",
       "La source complète est maintenue pour concilier attribution de logements adaptés et protections du relogement ; aucune nouvelle baisse n'est imputée au maintien des dérogations.",
       "Le besoin de logements adaptés et le coût des aides ne sont pas chiffrés. Le mécanisme ne vaut pas expulsion privée et ne supprime pas les recours et procédures judiciaires autonomes.",
       "Aucune charge nouvelle identifiée : mêmes trois offres, délais de six ou dix-huit mois, aide et protections ; aucun nouveau dossier, agrément ni condition d'ancienneté ajouté.")

retain('L442-3-3',
       "Maintien intégral du contrôle des ressources durablement très supérieures aux plafonds dans les seules zones tendues, avec son délai de dix-huit mois et toutes ses protections. Cette règle d'affectation du parc aidé a une finalité autonome ; elle ne rétablit pas le SLS supprimé. Le renvoi à l'enquête de L. 441-9 reste opérant, car sa finalité de contrôle de ressources est explicitement conservée dans le présent lot.",
       "Lecture de tous les I à III et de leurs six alinéas. Les deux années consécutives au-dessus de 150 % des plafonds PLS, le point de départ au 1er janvier suivant la seconde enquête, l'information sans délai, la notification six mois avant terme, le délai de dix-huit mois, le retour au maintien si les ressources passent sous les plafonds PLS, l'anniversaire de soixante-cinq ans dans l'année suivante, le handicap et QPV actuel ou à l'emménagement sont conservés. Le seuil de retour n'est pas 150 % mais le plafond PLS lui-même. La faculté d'extension hors zones de L. 442-4 est abrogée séparément et R*442-3-3 reste à coordonner pour le seul renvoi à L. 442-3-4 supprimé ; les zonages autonomes restent. Aucun minimum d'ancienneté professionnelle ni délai de licenciement n'est introduit.",
       "La source officielle entière est conservée pour l'affectation des logements en forte tension, avec protections et retour au maintien. La suppression du SLS n'est pas assimilée à une suppression de ce régime distinct.",
       "La perte du droit au maintien reste possible dans les seules conditions légales, indépendamment de toute rupture d'emploi. Aucune économie de gestion ou baisse globale de contrainte n'est attribuée à cet article conservé.",
       "Aucune charge nouvelle identifiée : mêmes seuils de ressources, deux constatations annuelles, notifications et délais ; réemploi de l'enquête existante sans données ni formalité supplémentaires.")

xml = paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant la présente réforme.",
    "L'absence de réponse à l'enquête prévue à l'article L. 441-9 ne peut, à elle seule, entraîner la perte du droit au maintien dans les lieux ou la déchéance du titre d'occupation. Aucune notification ni procédure ayant ce seul objet ne peut être engagée ou poursuivie après cette entrée en vigueur.",
    "Les locataires encore dans les lieux qui ont perdu leur droit au maintien sur ce seul fondement le retrouvent à cette date, sauf si une décision de résiliation du bail était passée en force de chose jugée avant l'entrée en vigueur. Les décisions ainsi devenues définitives et les libérations de logements déjà effectuées ne sont pas remises en cause par le présent article.",
    "Les obligations de renseignement et les sanctions disposant d'un fondement légal autonome, ainsi que les règles relatives au dépassement effectivement établi des ressources, conservent leur régime. Aucune obligation ni sanction de remplacement ne résulte de la présente abrogation. Les droits, créances, prescriptions et recours relatifs aux périodes antérieures demeurent régis par leurs règles applicables, sous réserve de la cessation des effets futurs expressément prévue ci-dessus et de la loi répressive plus douce dans son champ.")
rewrite('L442-3-4', xml,
        "Abrogation de fond de la déchéance automatique après deux défauts annuels de réponse : la seule omission documentaire ne suffit plus à perdre son logement. Les ressources effectivement excessives restent contrôlées par L. 442-3-3 et les enquêtes autonomes ne sont pas supprimées. Les personnes encore dans les lieux retrouvent le maintien hors résiliation judiciaire ancienne définitive ; les protections d'âge, handicap et QPV ne sont pas remplacées par des restrictions nouvelles, puisque l'absence de déchéance sur ce seul fondement devient générale.",
        "Lecture entière des quatre alinéas et des deux notes. Les anciens dix-huit mois, l'avis six mois avant terme, la régularisation par documents et ressources inférieures aux plafonds PLS, les exemptions soixante-cinq ans/handicap/à charge/QPV ainsi que la protection transitoire des anciennes ZUS jusqu'au 31 décembre 2020 sont utiles aux litiges historiques et restent dans leurs règles applicables. Leur abrogation prospective ne supprime aucune dispense d'une déchéance qui subsisterait sur le même fondement. Coordonner le renvoi du I de R*442-3-3, lu entièrement : retirer seulement ce renvoi sans altérer le zonage des autres dispositifs. Le présent texte ne supprime pas la pénalité autonome d'enquête d'occupation sociale de L. 442-5, lu en entier. Les notifications et délais locatifs ne sont pas le préavis individuel de travail.",
        'material_reduction',
        "La perte du logement sur le seul défaut documentaire est effectivement supprimée, sans nouvelle sanction équivalente. Le maintien est rétabli aux occupants encore présents dans les limites judiciaires précisées ; le contrôle des ressources réelles reste distinct.",
        "Ne rouvre ni jugement ancien définitif de résiliation ni logement déjà libéré ; ne supprime pas les obligations et sanctions d'autres enquêtes, ni L. 442-3-3. Le nombre de bénéficiaires et le solde de gestion restent inconnus.",
        "Aucune charge nouvelle identifiée : aucune déclaration de remplacement, aucune nouvelle preuve de ressources pour bénéficier de la fin de déchéance ; les autres obligations ont un fondement préexistant.",
        [effect('obligation_removed', 'hlm-fin-decheance-defaut-reponse-enquete',
                "Suppression de la perte du maintien pour le seul défaut de réponse pendant deux années.",
                "Deux années de non-réponse dans les zones tendues pouvaient conduire à perte du maintien après dix-huit mois, sous exemptions et possibilité de régularisation.",
                "Aucune perte du maintien ni procédure pour ce seul défaut ; rétablissement des occupants présents hors résiliation judiciaire ancienne définitive.",
                'legal_duty', "Locataires des logements sociaux HLM ou gérés par eux dans les zones visées, défaillants à l'enquête.",
                "Dès l'entrée en vigueur, procédures en cours arrêtées sur ce seul fondement ; décisions anciennes définitives, départs exécutés et droits historiques réservés.",
                "Aucune sanction de remplacement ; contrôles de ressources réellement constatées et enquêtes autonomes maintenus.",
                "les locataires qui, au cours de deux années consécutives, ne répondent pas à l'enquête prévue à l'article L. 441-9 n'ont plus le droit au maintien dans les lieux",
                "L'absence de réponse à l'enquête prévue à l'article L. 441-9 ne peut, à elle seule, entraîner la perte du droit au maintien dans les lieux ou la déchéance du titre d'occupation.")],
        repeal_scope="Déchéance du maintien et du titre d'occupation fondée sur deux non-réponses annuelles à l'enquête, avec cessation des procédures futures et réserve des décisions judiciaires anciennes définitives.")

retain('L442-3-5',
       "Maintien intégral de la résidence principale, de l'interdiction de céder ou sous-louer hors dérogations et du recours préalable au juge. Ces règles empêchent le détournement du logement social tout en préservant la sous-location sociale et les échanges permis. L'article n'impose ni déclaration nouvelle ni contrat de travail temporaire et ne doit pas être réécrit seulement pour changer ses mots.",
       "Les trois alinéas sont lus. Le seuil de huit mois renvoie aux conditions de l'article 2 de la loi de 1989, sans effacer par paraphrase les exceptions professionnelles, de santé ou de force majeure attachées à ce régime externe ; ce texte externe n'est pas réécrit ici. Le renvoi à L. 442-8-1 vise la sous-location et non un CDD : sa source et son projet fournis sont lus en entier. Le projet maintient l'accès des personnes âgées, handicapées, étudiants, accueillants et travailleurs mobiles, enlève l'information préalable du II et conserve le caractère saisonnier dans le contrat unique. Les six mois de sous-location saisonnière ne fixent pas un terme à l'emploi ; les anciens contrats et futurs emplois éligibles restent distincts. L'échange autorisé par l'article 9 de la loi de 1989 et le juge sont préservés.",
       "La source complète est conservée comme protection contre l'usage spéculatif d'un logement aidé et contre la résiliation privée, avec ses dérogations favorables. Aucun gain matériel nouveau n'est compté.",
       "La proposition de L. 442-8-1 n'est pas le droit positif ; ses coordinations relatives aux travailleurs saisonniers sont extérieures à cet article. Aucune extension automatique des exceptions n'est inventée.",
       "Aucune charge nouvelle identifiée : même occupation, mêmes exceptions et juge ; aucun justificatif d'ancienneté, de notification de rupture ou de type de contrat ajouté.")

xml = paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant la présente réforme.",
    "Aucune délibération ne peut étendre le régime de l'article L. 442-3-3 aux logements qui ne sont pas situés dans les zones géographiques qu'il vise. Les délibérations antérieures prises sur le fondement du présent article cessent de produire cet effet pour l'avenir.",
    "Aucune perte nouvelle du droit au maintien ni procédure de libération fondée uniquement sur cette extension territoriale ne peut être engagée ou poursuivie après l'entrée en vigueur. Les locataires encore dans les lieux qui ont perdu leur maintien sur ce seul fondement le retrouvent, sauf si la résiliation du bail avait été prononcée par une décision passée en force de chose jugée avant cette date. Les décisions ainsi devenues définitives et les libérations déjà effectuées ne sont pas remises en cause.",
    "L'article L. 442-3-3 reste applicable dans son propre champ géographique, avec ses garanties et exceptions. Les autres fondements de résiliation, les droits, créances, prescriptions et recours relatifs aux périodes antérieures conservent leur régime, sous réserve de la cessation des effets futurs expressément prévue au présent article.")
rewrite('L442-4', xml,
        "Abrogation de fond de la faculté d'étendre par simple délibération la perte du maintien pour ressources élevées hors des zones de forte tension. L'objectif d'allocation en pénurie reste traité par L. 442-3-3 dans son champ propre ; la faculté d'aggraver localement cette contrainte hors de ce champ n'est pas conservée. Les effets futurs des délibérations anciennes cessent sans refaire les jugements définitifs ni les départs exécutés.",
        "Lecture entière de la source et de L. 442-3-3. L'abrogation ne modifie pas les 150 %, deux années, dix-huit mois, retour sous plafond PLS et catégories protégées qui subsistent en zone tendue. Les conseils ne reçoivent aucun pouvoir de fixer un nouveau seuil ou une contribution compensatrice. Le rétablissement du maintien ne vaut ni remise de loyer ancien ni réouverture générale d'une décision judiciaire définitive. Le zonage réglementaire de R*442-3-3 reste celui des dispositifs autonomes ; aucune abrogation générale des contrôles de ressources n'est revendiquée.",
        'material_reduction',
        "L'extension territoriale facultative d'une déchéance est retirée, y compris ses effets futurs issus de décisions anciennes. Le régime légal en zone tendue reste entier ; il ne s'agit pas d'un abandon général des conditions du logement social.",
        "Les occupants déjà partis et les résiliations judiciaires anciennes définitives ne sont pas rétablis. Aucun nombre de ménages ni effet de financement n'est démontré.",
        "Aucune charge nouvelle identifiée : aucun dossier, vote, seuil ou sanction en remplacement ; l'abrogation borne le pouvoir du bailleur et conserve les règles autonomes.",
        [effect('obligation_removed', 'hlm-fin-decheance-ressources-hors-zone-tendue',
                "Fin de l'extension locale de la déchéance pour ressources hors zone tendue.",
                "Le conseil d'administration ou de surveillance pouvait rendre L. 442-3-3 applicable hors des zones légales de forte tension.",
                "Plus d'extension nouvelle ni d'effets futurs des extensions anciennes ; régime de L. 442-3-3 conservé dans ses zones propres.",
                'regime', "Locataires de logements sociaux hors des zones de L. 442-3-3 et organismes bailleurs.",
                "Entrée en vigueur, y compris procédures en cours sur ce seul fondement ; décisions judiciaires anciennes définitives et départs exécutés réservés.",
                "Aucune contribution ou procédure équivalente de remplacement.",
                "rendre applicable l'article L. 442-3-3 aux logements locatifs sociaux qui ne sont pas situés dans les zones géographiques mentionnées au même article.",
                "Aucune délibération ne peut étendre le régime de l'article L. 442-3-3 aux logements qui ne sont pas situés dans les zones géographiques qu'il vise.")],
        repeal_scope="Faculté d'étendre par délibération la déchéance pour ressources élevées aux logements hors zones tendues, avec fin des effets futurs des extensions anciennes et protection des jugements définitifs.")

retain('L442-4-1',
       "Maintien intégral de l'offre de relogement facultative après méconnaissance de l'usage paisible, avec mise en demeure, offre correspondant aux besoins et possibilités, délai et recours au juge. La notification et le mois de réponse protègent un occupant menacé de résiliation ; ils ne constituent pas une autorisation administrative ou un rapport redondant.",
       "L'article entier est lu avec L. 442-4-2 et L. 442-4-3 : le premier n'impose pas le relogement avant toute action, le second ouvre une saisine directe, le troisième vise les troubles graves ou répétés avec substitution préfectorale. Le b de l'article 7 de la loi de 1989 porte sur l'usage paisible ; le repérage « troisième alinéa (b) » ne vise ni rupture de contrat de travail ni conditions de ressources. Le refus et l'absence de réponse pendant un mois à compter de l'envoi sont distingués. Les compétences du juge et les autres voies judiciaires autonomes restent entières ; le texte de la loi de 1989 n'est pas réécrit.",
       "La faculté souple de relogement et ses garanties sont intégralement conservées. La sécurité des voisins et le contrôle judiciaire justifient les étapes qui subsistent ; aucune baisse nouvelle n'est comptée.",
       "Ne crée pas un relogement dû dans tous les cas ; L. 442-4-2 reste explicite sur ce point. Aucune accélération du procès ou réduction de l'ensemble des délais d'expulsion n'est démontrée.",
       "Aucune charge nouvelle identifiée : même mise en demeure, même faculté d'offre, même mois de réponse et même juge ; aucun dossier ni délai de quinze jours d'emploi ajouté.")

retain('L442-4-2',
       "Maintien intégral de la faculté de saisir directement le juge pour manquement à l'usage paisible, sans obligation générale d'offrir un relogement. L'article évite déjà une contrainte et conserve l'intervention du juge : l'abroger ou réécrire ses mots ne démontrerait pas un allègement supplémentaire.",
       "Lecture entière de la source et des deux articles voisins du lot. Le renvoi à L. 442-4-1 demeure valide, distinct de L. 442-4 abrogé, et vise sa seule offre facultative. Le b de l'article 7 de la loi de 1989 ne doit pas être lu comme une obligation de notification de licenciement. La saisine par substitution de L. 442-4-3 conserve les conditions de fond du trouble et la décision du juge, pas un pouvoir préfectoral d'expulsion privée. Aucune nouvelle saisine obligatoire ni aide retirée.",
       "La règle favorable de saisine directe existe déjà dans la source complète et reste entière. Son maintien ne vaut pas nouvelle obligation supprimée ni nouveau délai réduit.",
       "Les garanties du procès et les protections indépendantes de l'expulsion restent applicables. Le contenu des textes de procédure extérieurs n'est pas prétendu réécrit.",
       "Aucune charge nouvelle identifiée : même faculté de recours, sans offre préalable obligatoire, sans agrément ni transmission administrative nouvelle.")

a = BY_NUMBER['L442-4-3']
xml = a['source_xml'].replace(
    "Le bailleur fait connaître au représentant de l'Etat, dans un délai de quinze jours, la suite qu'il entend réserver à l'injonction.",
    "Le bailleur peut faire connaître au représentant de l'Etat, dans un délai de quinze jours, la suite qu'il entend réserver à l'injonction. Cette réponse ne constitue pas une obligation distincte et son absence n'est pas, par elle-même, un manquement du bailleur.")
xml += paragraphs("Le caractère facultatif de la réponse s'applique à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris aux injonctions en cours. Il ne modifie ni les conditions de l'injonction, ni les délais et pouvoirs de substitution, ni les obligations autonomes du bailleur envers les occupants et les tiers. Aucun délai en cours n'est recommencé. Les actes régulièrement accomplis, les décisions judiciaires, les droits, créances, prescriptions et recours antérieurs sont préservés, sous réserve de l'application de la loi répressive plus douce dans son champ.")
rewrite('L442-4-3', xml,
        "Suppression de l'obligation particulière de faire une réponse au préfet dans les quinze jours : le bailleur peut répondre mais le silence n'est plus, à lui seul, un manquement autonome. L'injonction liée aux troubles graves ou répétés, sa motivation, la possibilité de substitution dès le silence et la saisine du juge restent entières. La protection de l'ordre public ne dépend donc pas de la conservation d'un compte rendu obligatoire supplémentaire.",
        "Les deux alinéas sont lus intégralement. La date du 20 août 2026 est celle de la version source, non une promulgation future. Restent inchangés l'occupant habituel, la gravité ou répétition du trouble, l'exemple du trafic de stupéfiants, le lien avec le b de l'article 7 de la loi de 1989, les faits motivant l'injonction, la substitution en cas de refus ou de silence après quinze jours et, après acceptation, après un mois sans saisine. Les renvois à L. 442-4-2 restent exacts et ne visent pas L. 442-4 abrogé. Les délais ne sont pas ceux du préavis individuel du contrat unique et ne promettent pas une décision judiciaire en quinze jours. Aucun rapport, copie de recours ou information de remplacement n'est ajouté ; l'évaluation de la charge nette reste qualitative et non nationale.",
        'material_reduction',
        "La réponse administrative particulière devient facultative, ce qui retire une obligation formelle identifiable. La substitution du préfet et ses mêmes échéances demeurent : la réduction porte sur le compte rendu, sans affaiblir le pouvoir de saisir le juge pour les troubles graves.",
        "L'injonction et les obligations autonomes envers les voisins subsistent ; le silence peut toujours entraîner la substitution après quinze jours. Aucun raccourcissement de procès ni économie globale de contrôle n'est démontré.",
        "Aucune charge nouvelle identifiée : réponse facultative sans formulaire imposé, mêmes faits, mêmes échéances de substitution et même juge ; la transition ne remet aucun délai à zéro.",
        [effect('obligation_removed', 'hlm-reponse-prefectorale-troubles-facultative',
                "Suppression du compte rendu impératif au préfet après injonction.",
                "Bailleur tenu de faire connaître dans quinze jours la suite à donner ; substitution déjà possible en cas de refus ou de silence.",
                "Réponse facultative, absence non fautive par elle-même ; substitution toujours possible aux mêmes échéances de quinze jours ou d'un mois selon le cas.",
                'legal_duty', "Bailleurs destinataires d'une injonction préfectorale pour troubles graves ou répétés causés par l'occupant habituel.",
                "Entrée en vigueur y compris injonctions en cours, sans recommencer les délais ni rouvrir les jugements.",
                "Aucun compte rendu de remplacement ; injonction, motivation, substitution et contrôle judiciaire existants maintenus.",
                "Le bailleur fait connaître au représentant de l'Etat, dans un délai de quinze jours, la suite qu'il entend réserver à l'injonction.",
                "Cette réponse ne constitue pas une obligation distincte et son absence n'est pas, par elle-même, un manquement du bailleur.")],
        removed=["Obligation distincte pour le bailleur de répondre au préfet sous quinze jours après injonction, sans modifier les pouvoirs de substitution ni le contrôle du juge."])

CHECKS = {
    'L441-15': {
        'L1234-1': "Cette cible règle le préavis de licenciement privé : dans la source, durées liées aux six mois et deux ans de services ; dans le projet, quinze jours calendaires pour les nouveaux contrats, avec transition des anciens. L'habilitation de L. 441-15 concerne uniquement le logement et ne renvoie matériellement à aucun de ces seuils. Elle ne peut réduire les délais locatifs au préavis d'emploi, ni remplacer les procédures collectives ou autorisations distinctes de rupture. Aucun renvoi au code du travail n'est ajouté.",
        'L1221-2': "La source autorise le terme dans les cas du titre IV ; la proposition impose le contrat unique indéterminé pour les nouvelles embauches, en protégeant les contrats antérieurs et en distinguant durée de mission et durée d'emploi. L. 441-15 n'habilite pas à régler la forme du contrat de travail. Les remises favorables et finalités autonomes de l'enquête locative restent accessibles aux futurs foyers éligibles, y compris sous contrat unique, sans exiger de CDD ni créer d'enquête d'emploi ou de terme de contrat.",
        'L1234-9': "La source et sa note concernent l'indemnité de licenciement ouverte après huit mois, sauf faute grave. Le projet prévoit pour le nouveau contrat un an au terme effectif, préavis inclus, puis 0,20 mois par année totale, fractions en mois complets et plafond de six mois ; droits anciens et indemnités spéciales gardent leur champ. L'habilitation locative ne fixe aucune indemnité d'emploi et ne transpose ni ce seuil ni ce plafond aux remises de loyer. Les frais de dossier SLS visés par sa borne sont distincts de l'indemnité patronale.",
        'L441-9': "La vue fournie est la source officielle entière, sans proposition : enquête annuelle, dispenses APL et allocations, réponse sous un mois, mise en demeure de quinze jours, liquidation provisoire maximale, frais et remboursement sous deux mois. Le renvoi nouveau de L. 441-15 vise le premier alinéa dans les finalités RLS et ressources maintenues par la proposition du présent lot ; il n'habilite pas à rétablir les liquidations ou frais du SLS futur. L'ancien délai de quinze jours reste une mise en demeure locative pour le stock antérieur, sans rapport avec la notification de rupture d'emploi. Les avantages futurs éligibles restent ouverts sans dossier de remplacement.",
    },
    'L441-9': {
        'L1234-1': "La cible porte sur le préavis de licenciement : ancien droit modulé par l'ancienneté, proposition de quinze jours pour le contrat unique avec anciens contrats protégés. Les quinze jours de L. 441-9 sont une mise en demeure locative de l'ancien SLS, pas une rupture d'emploi ; aucun seuil de six mois ou deux ans n'est importé dans l'enquête.",
        'L1221-2': "La cible proposée interdit les nouveaux CDD et distingue durée de mission et durée d'emploi, en conservant les contrats antérieurs. L. 441-9 recueille ressources et composition du foyer ; la demande n'est conditionnée ni à un CDI ancien ni à un CDD et demeure utilisable pour les futurs salariés sous contrat unique sans enquête d'emploi nouvelle.",
        'L1234-9': "La cible et sa note de 2017 concernent l'indemnité patronale de licenciement ; le projet distingue un an au terme effectif préavis inclus, 0,20 mois par année totale, mois complets et plafond de six mois, anciens droits et indemnités spéciales. L'indemnité de dossier du SLS est d'une autre nature : elle cesse pour les périodes nouvelles, sans supprimer aucun salaire ou droit à rupture.",
    },
    'L442-2-1': {
        'L1234-1': "Le préavis de licenciement de la cible, ancien ou proposé à quinze jours calendaires, ne fixe ni l'ouverture de la RLS ni sa revalorisation. L'article locatif garde composition du foyer, zones, ressources et baux en cours ; aucune ancienneté de travail ou notification de rupture n'est exigée pour un foyer futur éligible.",
        'L1221-2': "Le contrat unique futur remplace les nouveaux CDD sans limiter l'emploi à la durée d'une aide. La RLS est un avantage locatif défini par ressources et composition du foyer, non par la forme du contrat : elle reste ouverte aux anciens contrats, aux nouveaux salariés sous contrat unique et aux autres foyers éligibles, sans coordination de taux ou de durée d'emploi.",
        'L1234-9': "Le seuil d'un an et le barème de 0,20 mois par année totale plafonné à six mois du projet concernent exclusivement l'indemnité ordinaire due par l'employeur, avec droits anciens et spéciaux préservés. Ils ne sont ni un délai d'accès à la RLS ni un plafond de ses tableaux ; l'article locatif est intégralement maintenu sans référence à la rupture.",
        'L441-9': "La vue fournie est exclusivement la source officielle, avec demande annuelle, dispenses APL/allocations et délai d'un mois, et non une proposition adoptée. Sa demande sert déjà expressément à la RLS pour les non-bénéficiaires APL. Dans ce lot, sa finalité RLS est maintenue après abolition du SLS, sans frais ni calcul provisoire du SLS futur ; le renvoi du deuxième alinéa reste opérant, les tableaux et indexations ne bougent pas.",
    },
    'L442-3-3': {
        'L1234-1': "La cible traite le licenciement, ses anciennes durées selon services et son futur préavis de quinze jours. Ici, dix-huit mois de maintien et notification six mois avant terme sont des garanties locatives contre la déchéance pour ressources durablement élevées ; elles ne sont pas réduites au préavis de travail ni soumises à l'ancienneté chez un employeur.",
        'L1221-2': "L'interdiction des nouveaux CDD et la durée indéterminée du contrat unique ne modifient pas le test locatif des deux années au-dessus de 150 % des plafonds PLS. Les anciens contrats et les futurs emplois sont traités selon les ressources réellement pertinentes et les mêmes exceptions ; aucun terme de mission ni fin d'aide ne fait perdre le maintien dans les lieux.",
        'L1234-9': "L'indemnité patronale proposée, avec seuil d'un an préavis inclus et barème de 0,20 mois sur toute l'ancienneté, n'est pas l'objet de ce renvoi contextuel. L. 442-3-3 conserve son retour au maintien si les ressources deviennent inférieures aux plafonds PLS ; aucun seuil d'ancienneté, plafond de six mois de salaire ou démission n'est ajouté à ce droit locatif.",
        'L441-9': "La cible fournie est la demande officielle utilisée pour constater les ressources, pas un projet de suppression de tous ses usages. Le corps rédigé dans ce lot conserve expressément l'enquête pour L. 442-3-3 et ses dispenses existantes, tout en supprimant le SLS futur. Les deux enquêtes consécutives, 150 %, le calendrier de dix-huit mois et le retour sous plafond PLS restent donc cohérents sans enquête de remplacement.",
    },
    'L442-3-4': {
        'L1234-1': "Les délais de la source sont ceux de la perte du maintien après défaut d'enquête, non ceux d'un licenciement. L'abrogation supprime cette cause de déchéance sans appliquer le préavis de quinze jours ni les anciennes conditions de six mois ou deux ans de la cible ; les décisions locatives anciennes définitives restent réservées.",
        'L1221-2': "La cible proposée conserve les contrats anciens et impose la durée indéterminée aux nouvelles embauches. La suppression de la déchéance documentaire de L. 442-3-4 vaut indépendamment du type d'emploi, sans rouvrir de CDD et sans exiger un contrat unique pour retrouver le maintien ; les occupants éligibles futurs ne sont pas exclus.",
        'L1234-9': "Le projet de cible règle l'indemnité ordinaire de rupture et son seuil d'un an au terme effectif, puis 0,20 mois par année totale avec fractions en mois complets et plafond de six mois. Aucune de ces conditions n'est transposée au rétablissement du maintien locatif ; l'abrogation ne touche ni créance salariale, ni indemnité spéciale, ni réparation d'une illégalité.",
        'L441-9': "La cible officielle contient l'enquête dont deux défauts déclenchent la déchéance de la source. La proposition locale conserve les usages RLS et contrôle réel de ressources de cette enquête ; elle ne peut cependant plus alimenter une déchéance sur le seul silence, retirée ici. Les dettes et données anciennes restent à leur champ, sans frais SLS ou perte de logement de remplacement pour une période nouvelle.",
    },
    'L442-3-5': {
        'L1234-1': "La cible vise le préavis de rupture d'emploi et sa transition, non l'occupation de la résidence principale huit mois par an. La règle locative et ses exceptions externes demeurent ; aucun préavis de quinze jours ni ancienneté professionnelle de six mois ou deux ans n'est imposé à la sous-location légalement permise.",
        'L1221-2': "Le contrat unique est indéterminé malgré une mission ou saison limitée ; les CDD antérieurs gardent leurs droits. L. 442-3-5 n'interdit pas les emplois saisonniers sous ce contrat : son renvoi à L. 442-8-1 préserve l'accès futur à la sous-location éligible, et la durée du logement ne devient pas une durée d'emploi ou un nouveau CDD.",
        'L1234-9': "La cible et sa note concernent la rupture par l'employeur, le seuil futur d'un an calculé préavis inclus, l'indemnité de 0,20 mois et les droits anciens. La sanction locative reste une saisine du juge pour détournement de l'usage du logement ; elle n'efface aucune indemnité ni n'ajoute un minimum d'ancienneté à la résidence ou aux dérogations de sous-location.",
        'L442-8-1': "La source et le projet de cette cible sont lus entièrement : exceptions de sous-location à personnes morales et accueil de personnes âgées ou handicapées, prix proratisé, saisonniers et limite de six mois. Le projet enlève l'information préalable du II et maintient le caractère saisonnier réel y compris sous contrat unique, avec contrats anciens protégés. Le renvoi conservé n'exige pas cette information par une autre voie et ne ferme pas l'avantage aux emplois futurs ; les six mois portent sur la sous-location, jamais sur le terme de l'emploi. Ce projet reste distinct du droit positif.",
    },
}

for source in SOURCES:
    number = source['number']
    answer = ANSWERS[number]
    source_key = source['code_id'] + '|' + source['source_id']
    required = REFS['requirements'][source_key]
    for target_key in required:
        target = REFS['targets'][target_key]
        assessment = CHECKS[number][target['number']]
        answer['reference_checks'].append(dict(target_key=target_key,
                                               view_sha256=target['view_sha256'],
                                               assessment=assessment))

ordered_answers = [ANSWERS[a['number']] for a in SOURCES]
assert len(ordered_answers) == 24
Path('answer.json').write_text(json.dumps(ordered_answers, ensure_ascii=False, indent=2) + '\n')
print('answer.json :', len(ordered_answers), 'articles')
