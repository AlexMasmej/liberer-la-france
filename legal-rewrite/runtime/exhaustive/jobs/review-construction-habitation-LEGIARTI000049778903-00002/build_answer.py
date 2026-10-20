import json
import re
from html import unescape


with open('source.json', encoding='utf-8') as f:
    sources = json.load(f)
with open('reference-targets.json', encoding='utf-8') as f:
    references = json.load(f)


def paragraphs(xml):
    return re.findall(r'<p>(.*?)</p>', xml, flags=re.S)


def xml(paras):
    return '\n'.join('<p>' + p + '</p>' for p in paras)


def impact(classification, assessment, scope, burdens, effects):
    return {
        'version': 1,
        'classification': classification,
        'assessment': assessment,
        'scope_limitations': scope,
        'new_burdens_review': burdens,
        'effects': effects,
    }


def effect(kind, measure, description, before, after, unit, population,
           transition, replacement, source_quote, proposed_quote):
    return {
        'kind': kind,
        'measure_id': measure,
        'description': description,
        'before': before,
        'after': after,
        'unit': unit,
        'affected_population': population,
        'conditions_and_transition': transition,
        'replacement_or_new_burdens': replacement,
        'source_quote': source_quote,
        'proposed_quote': proposed_quote,
    }


def base(source):
    return {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}


answers = []

# L184-8 : même ensemble de peines, individualisation et renvoi pénal explicite.
s = sources[0]
p = paragraphs(s['source_xml'])
p[0] = (
    "Pour les infractions prévues aux articles L. 184-4 à L. 184-6, les personnes morales "
    "encourent, outre l'amende prévue à l'article 131-38 du code pénal, les peines "
    "complémentaires prévues aux 2°, 4°, 8° et 9° de l'article 131-39 du même code."
)
p[3] = (
    "La juridiction peut prononcer la peine de confiscation mentionnée au même 8° et la "
    "peine d'interdiction d'acheter ou d'être usufruitier mentionnée au deuxième alinéa "
    "à l'encontre des personnes morales coupables des infractions prévues aux articles "
    "L. 184-4 à L. 184-6, en tenant compte des circonstances de l'infraction et de la "
    "personnalité de son auteur. Leur prononcé n'est pas obligatoire et la décision de "
    "ne pas les prononcer n'exige pas de motivation spéciale au titre du présent article, "
    "sans préjudice des règles générales de motivation des décisions juridictionnelles."
)
p.append(
    "Le caractère facultatif de la confiscation et de l'interdiction mentionnées au "
    "quatrième alinéa s'applique aux infractions commises à compter de l'entrée en "
    "vigueur de la loi portant la présente réforme et, dans les conditions d'application "
    "de la loi pénale plus douce, aux infractions antérieures n'ayant pas donné lieu à "
    "une condamnation passée en force de chose jugée. Il n'entraîne pas la remise en "
    "cause des condamnations passées en force de chose jugée ni l'extinction des droits "
    "des victimes. La précision du champ des infractions au présent article ne permet "
    "de prononcer aucune peine qui n'était pas légalement encourue à la date des faits."
)
a = base(s)
a.update(
    proposed_xml=xml(p),
    status='rewrite_draft',
    change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=[
        "Suppression du prononcé obligatoire de la confiscation et de l'interdiction d'achat ou d'usufruit pour les personnes morales ; ces peines deviennent facultatives.",
        "Suppression de la motivation spéciale imposée pour ne pas prononcer ces deux peines, sans supprimer la motivation judiciaire de droit commun.",
    ],
    reason=(
        "Réforme de fond conservée du brouillon : retirer le prononcé obligatoire des deux "
        "peines patrimoniales et sa dérogation spécialement motivée, tout en laissant au juge "
        "le pouvoir de les prononcer. La seconde passe corrige aussi expressément le renvoi "
        "à une « infraction prévue au présent article », inexploitable dans un article qui "
        "énumère seulement des peines : le champ est rattaché aux délits de L. 184-4 à "
        "L. 184-6, lus dans le corpus. Ce n'est pas une incrimination nouvelle. Les autres "
        "peines, les dix ans au plus, l'objet de la confiscation et la règle d'expropriation "
        "restent à droit constant. Aucune autre coupe n'est justifiée : ces moyens judiciaires "
        "protègent les occupants contre l'hébergement dangereux, la suroccupation et "
        "l'éviction par dégradation. Les supprimer entièrement retirerait une protection "
        "essentielle. Il n'est revendiqué ni suppression d'un impôt ni économie chiffrée."
    ),
    review_notes=(
        "Les cinq alinéas sources, la note vide, le brouillon entier et le texte initial de "
        "SRU 178 ont été lus. Le dispositif initial de travaux d'office et de relogement "
        "ne contient pas les peines actuelles : l'origine détaillée de ces ajouts reste "
        "non établie, sans clôture du volet historique ni de l'examen des 209 articles. "
        "L. 184-1 à L. 184-7 et L. 551-1 ont été lus en entier dans le corpus public, "
        "sources et propositions distinguées. La nouvelle référence à L. 184-4 à "
        "L. 184-6, absente des cibles contractuelles de reference-targets.json, est une "
        "coordination expresse et bornée aux délits existants de sécurité : refus délibéré "
        "de travaux après mise en demeure, suroccupation manifeste et faits de L. 184-6. "
        "La syntaxe défectueuse du 1° de L. 184-6 reste un point autonome à authentifier ; "
        "elle n'est pas réécrite dans ce lot. La transition interdit tout élargissement "
        "rétroactif de peine. L. 184-7 proposé retient déjà la facultativité pour les "
        "personnes physiques ; la présente mesure en coordonne le volet personnes morales. "
        "Les alinéas 2, 3 et 5 sont repris mot pour mot ; aucune exception d'occupation "
        "personnelle n'est créée pour les personnes morales. Les renvois 131-38, 131-39 "
        "(2°, 4°, 8°, 9°) et le dixième alinéa de 131-21 sont conservés dans leur objet "
        "source ; leur texte pénal externe, non fourni dans le corpus autorisé, et notamment "
        "la concordance ordinale de 131-21 restent à contrôler hors de ce lot. L. 551-1 "
        "vise toujours le deuxième alinéa, maintenu à sa place, et contrôle les interdictions "
        "effectivement prononcées. La date de version de 2024 n'est pas la date de la réforme. "
        "Les trois cibles de droit du travail requises sont sans application matérielle ici, "
        "comme détaillé dans reference_checks."
    ),
    benefit_review=(
        "La possibilité judiciaire de ne pas prononcer les deux peines devient la règle "
        "de leur individualisation et reste ouverte aux affaires futures. Le plafond de dix "
        "ans, la limitation de la confiscation au bien ou fonds ayant servi à l'infraction "
        "et la valeur liée à l'indemnité d'expropriation sont conservés. Les droits des "
        "victimes et les règles de la loi pénale plus douce subsistent ; aucune exonération "
        "fiscale ni aide n'est supprimée."
    ),
)
a['substantive_impact'] = impact(
    'material_reduction',
    "Par rapport à la source officielle entière, deux peines restent disponibles mais "
    "cessent d'être obligatoires, et le non-prononcé ne requiert plus la motivation spéciale "
    "de cet article. Cette réduction était déjà dans le brouillon ; la correction explicite "
    "de son champ pénal n'est pas une seconde coupe. Les peines principales et les autres "
    "peines complémentaires ne baissent pas.",
    "Champ limité aux personnes morales et aux délits de sécurité visés ; ni abrogation "
    "des incriminations, ni annulation des condamnations définitives. L'alinéa externe de "
    "131-21 et la filiation historique complète restent à vérifier. Aucun montant de "
    "sanctions évitées ni solde global des codes n'est établi.",
    "Aucune charge nouvelle identifiée : ni autorisation, ni déclaration, ni donnée ou "
    "registre ajouté. La motivation générale demeure ; la nouvelle précision des délits "
    "ne crée aucune infraction et la transition interdit une peine rétroactivement nouvelle.",
    [effect(
        'obligation_removed',
        'securite-hebergement-peines-complementaires-facultatives',
        "Retrait de l'automatisme des deux peines patrimoniales et de la motivation "
        "spéciale de leur non-prononcé, dans le volet personnes morales.",
        "Personnes morales : confiscation du fonds ou bâtiment ayant servi à l'infraction "
        "et interdiction d'achat ou d'usufruit jusqu'à dix ans obligatoires, sauf "
        "non-prononcé spécialement motivé ; aucun taux fiscal concerné.",
        "Mêmes personnes, mêmes objets et maximum de dix ans : prononcé facultatif "
        "selon les circonstances et l'auteur ; seule la motivation judiciaire générale subsiste.",
        'legal_duty',
        "Personnes morales pénalement responsables des délits de L. 184-4 à L. 184-6 ; "
        "volet distinct mais coordonné aux personnes physiques de L. 184-7.",
        "Faits futurs et faits antérieurs non définitivement jugés dans le champ de la "
        "loi pénale plus douce ; condamnations définitives et droits des victimes préservés.",
        "Pas de formalité ou de sanction de remplacement ; autres peines maintenues. "
        "La même mesure ne doit pas être additionnée une seconde fois avec L. 184-7.",
        "Le prononcé de la peine de confiscation mentionnée au même 8° et de la peine "
        "d'interdiction d'acheter ou d'être usufruitier mentionnée au deuxième alinéa "
        "est obligatoire à l'encontre de toute personne coupable d'une infraction prévue au présent article.",
        "Leur prononcé n'est pas obligatoire et la décision de ne pas les prononcer "
        "n'exige pas de motivation spéciale au titre du présent article, sans préjudice "
        "des règles générales de motivation des décisions juridictionnelles.",
    )],
)
checks = {
    'L1234-1': (
        "Cette cible concerne le préavis du salarié licencié, avec ancienneté et règles "
        "plus favorables dans la source, puis quinze jours calendaires pour les contrats "
        "nouveaux dans la proposition et maintien des anciennes durées. L. 184-8 ne vise "
        "aucun salarié, aucune notification de rupture ni aucune ancienneté : il sanctionne "
        "des personnes morales en matière de sécurité de l'hébergement. Il ne comporte "
        "pas de renvoi à L. 1234-1. Aucun préavis de travail n'est transposé à une peine pénale."
    ),
    'L1221-2': (
        "La source admet encore les CDD dans leurs cas légaux ; la proposition réserve "
        "les embauches nouvelles au contrat unique indéterminé et maintient les contrats "
        "antérieurs, sans nouveau CDD par renouvellement. L. 184-8 ne régit ni embauche, "
        "ni mission, ni formation : sa personne morale poursuivie n'est pas un contrat "
        "de travail. Aucun renvoi à cette cible n'existe et aucune condition d'ancienneté "
        "ou de notification d'une rupture n'est applicable à ses sanctions."
    ),
    'L1234-9': (
        "La source ouvre l'indemnité de licenciement après huit mois hors faute grave. "
        "La proposition distingue anciens contrats et nouveaux contrats : pour ces "
        "derniers, seuil d'un an au terme effectif, préavis inclus, puis 0,20 mois par "
        "année totale, fractions en mois complets, plafond de six mois et employeur seul ; "
        "les réparations et indemnités spéciales demeurent distinctes. Ni cette ancienneté "
        "ni une notification patronale n'ont de champ dans L. 184-8 : confiscation et "
        "interdiction pénales ne sont pas des indemnités de rupture et aucun renvoi n'est à modifier."
    ),
}
a['reference_checks'] = [
    {'target_key': key, 'view_sha256': references['targets'][key]['view_sha256'],
     'assessment': checks[references['targets'][key]['number']]}
    for key in references['requirements'][s['code_id'] + '|' + s['source_id']]
]
answers.append(a)

# L184-9 : correction opératoire, sans présenter la protection judiciaire comme une coupe.
s = sources[1]
p = [
    "Lorsque les poursuites sont effectuées à l'encontre d'exploitants de fonds de "
    "commerce aux fins d'hébergement, il est fait application de l'article L. 651-10.",
    "Pour l'application de l'article L. 651-10 aux poursuites exercées pour les "
    "infractions prévues aux articles L. 184-4 à L. 184-6, la référence à "
    "l'article L. 184-1 figurant au I de cet article désigne ces infractions. "
    "Les conditions relatives à la continuation de "
    "l'exploitation et les garanties prévues à l'article L. 651-10 demeurent applicables.",
    "Cette coordination s'applique aux actes de procédure accomplis à compter de "
    "l'entrée en vigueur de la loi portant la présente réforme, y compris dans les "
    "procédures en cours. Elle ne remet pas en cause les actes régulièrement accomplis "
    "ni les décisions passées en force de chose jugée. Elle ne crée aucune infraction "
    "ni aucune peine et ne permet pas de prononcer une peine qui n'était pas légalement "
    "encourue à la date des faits.",
]
a = base(s)
a.update(
    proposed_xml=xml(p),
    status='rewrite_draft',
    reason=(
        "Coordination nécessaire, et non reformulation stylistique du brouillon : rendre "
        "opératoire le renvoi de sécurité à L. 651-10 en précisant expressément, pour ces "
        "poursuites seulement, les délits derrière sa référence à L. 184-1, article de "
        "police administrative sans incrimination. Le régime judiciaire déjà rendu "
        "applicable est maintenu : administration provisoire décidée par le juge en cas "
        "de danger ou d'atteinte à la dignité, information des propriétaires et défense "
        "des tiers. Aucune taxe, déclaration périodique, autorisation préalable "
        "d'exploitation ou pièce redondante n'est créée par l'article source. Les "
        "retirer ici reviendrait à supprimer des garanties de sécurité et de recours ; "
        "aucune coupe supplémentaire n'est justifiée. Les actes antérieurs et les "
        "limites pénales sont protégés par une transition expresse."
    ),
    review_notes=(
        "Source, note historique, brouillon et SRU 178 lus intégralement ; L. 184-1 à "
        "L. 184-7 et L. 651-10 ont également été lus en entier. Le I de L. 651-10 "
        "vise actuellement des poursuites sur L. 184-1, alors que les délits de ce "
        "chapitre sont L. 184-4 à L. 184-6. Au lieu de laisser cette incohérence intacte "
        "comme le brouillon, le deuxième alinéa la coordonne expressément dans le champ "
        "du présent article. Ces nouveaux renvois précis ne sont pas fournis dans "
        "reference-targets.json mais leurs sources entières ont été contrôlées dans "
        "construction-habitation.json. Le premier alinéa demeure celui de l'applicabilité "
        "à l'exploitant d'un fonds d'hébergement ; les précisions et la transition sont "
        "ajoutées après lui. Aucun contournement des conditions sanitaires, de dignité, "
        "de sécurité ou de santé du I de L. 651-10, ni de ses II à IV. La décision "
        "judiciaire, la citation, les observations par avocat et l'appel des tiers "
        "demeurent dans leur champ. Une modification concordante du I de L. 651-10 "
        "reste à intégrer hors lot pour remplacer directement son ancienne référence ; "
        "ses autres renvois, notamment L. 511-6, demandent un examen autonome et "
        "ne sont pas réputés purgés. La présente correction ne fournit pas une rédaction "
        "authentifiée du 1° de L. 184-6. Le texte initial de SRU 178 correspond à "
        "l'ancienne police L. 123-3, retrouvée dans L. 184-1, et ne démontre pas à "
        "lui seul l'origine du renvoi pénal actuel : filiation complète non soldée. "
        "Le 1er juillet 2021 de la note est une date historique, pas celle du projet."
    ),
    benefit_review=(
        "Le renvoi conserve l'information des propriétaires, leur défense et leurs "
        "recours dans L. 651-10 ainsi que la protection des occupants en cas de "
        "poursuite future. L'administration provisoire reste conditionnée au danger "
        "ou aux autres atteintes légalement définies et décidée par le juge. Aucune "
        "dispense favorable ou aide n'est fermée aux nouvelles situations éligibles."
    ),
    reference_checks=[],
)
a['substantive_impact'] = impact(
    'coordination_only',
    "La source entière est une règle de renvoi judiciaire. Le texte proposé clarifie "
    "l'articulation avec le I de L. 651-10 sans supprimer de prélèvement ou de "
    "formalité autonome. Cette correction dépasse le précédent changement de mots, "
    "mais ne constitue pas une réduction matérielle supplémentaire.",
    "Coordination limitée aux poursuites contre les exploitants d'hébergement pour "
    "les trois articles pénaux du chapitre. Les autres fondements de L. 651-10 et "
    "son histoire complète ne sont pas réécrits ; aucun gain financier ni solde global "
    "de complexité n'est démontré.",
    "Aucune charge nouvelle autonome identifiée : aucun dépôt, agrément, délai, "
    "registre ou donnée supplémentaire. Les procédures judiciaires déjà visées "
    "conservent leurs conditions et garanties ; aucune peine nouvelle ne peut être "
    "appliquée rétroactivement du fait de la précision des renvois.",
    [effect(
        'coordination',
        'securite-hebergement-renvoi-administration-provisoire',
        "Précision des délits de sécurité visés par le renvoi judiciaire existant.",
        "L. 184-9 renvoie à L. 651-10, dont le I vise des poursuites sur L. 184-1 "
        "alors que ce dernier est un article de police administrative.",
        "Pour les poursuites du présent article, la référence du I de L. 651-10 "
        "désigne explicitement L. 184-4 à L. 184-6 ; ses autres conditions restent opposables.",
        'legal_duty',
        "Exploitants de fonds de commerce aux fins d'hébergement poursuivis pour "
        "les infractions de sécurité de ce chapitre, propriétaires et tiers concernés.",
        "Actes de procédure futurs, même dans les procédures en cours ; actes "
        "réguliers, décisions définitives et légalité des peines à la date des faits préservés.",
        "Aucun nouveau dossier, contrôle périodique ou autorisation : coordination "
        "d'un régime déjà rendu applicable, sans réduction comptée.",
        "Lorsque les poursuites sont effectuées à l'encontre d'exploitants de fonds "
        "de commerce aux fins d'hébergement, il est fait application de l'article L. 651-10.",
        p[1],
    )],
)
answers.append(a)

# L222-2 : le reste de la source est intégralement conservé, sans réécriture stylistique.
s = sources[2]
p = paragraphs(s['source_xml'])
p[0] = p[0].replace(
    "est une société d'économie mixte",
    "est un organisme d'habitations à loyer modéré ou une société d'économie mixte",
)
p.append(
    "L'exemption prévue au premier alinéa pour les organismes d'habitations à "
    "loyer modéré s'applique aux contrats conclus à compter de l'entrée en vigueur "
    "de la loi portant la présente réforme. Elle n'éteint ni ne modifie les obligations "
    "résultant des contrats antérieurs ni les garanties valablement constituées pour "
    "leur exécution. Les dispositions impératives fondées sur un autre texte restent applicables."
)
a = base(s)
a.update(
    proposed_xml=xml(p),
    status='rewrite_draft',
    change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=[
        "Suppression, pour les nouveaux contrats des organismes HLM, de l'application obligatoire du régime de promotion immobilière par le premier alinéa de L. 222-1, rétablie à leur charge par SRU 164 III.",
    ],
    reason=(
        "Réduction de fond déjà acquise au brouillon, conservée après la seconde passe : "
        "rétablir expressément la dispense HLM que SRU 164 III avait retirée, pour tous "
        "leurs contrats futurs éligibles. Ce n'est pas l'abrogation de l'ensemble du "
        "régime de promotion ni une restauration automatique du droit antérieur. À "
        "droit constant, les dispenses SEM, d'opérations administratives seules et "
        "de construction sur le terrain conservé par le vendeur sont reprises dans "
        "leurs termes sources. Aucune coupe supplémentaire n'est retenue : la garantie "
        "du vendeur au quatrième alinéa est la contrepartie essentielle de sa dispense "
        "de contrat de promotion et protège l'exécution de la construction payée par "
        "la société ; elle n'est pas une déclaration doublonnée. Supprimer les "
        "conditions des autres exceptions ouvrirait une dispense différente, sans "
        "fondement démontré dans la présente décision."
    ),
    review_notes=(
        "Source entière, note vide, brouillon entier et texte initial de SRU 164 "
        "lus ; son III retire exactement « un organisme d'habitations à loyer modéré "
        "ou ». Ce constat documentaire suffit à identifier la restriction réécrite, "
        "sans affirmer avoir consulté une version ancienne non jointe. L. 222-1 à "
        "L. 222-5, L. 221-1 à L. 221-5, L. 212-10 et L. 213-6 ont été lus dans "
        "le corpus. Le premier alinéa de L. 222-1 rend obligatoires le régime civil "
        "de promotion et ce chapitre ; ses autres exceptions demeurent. Les alinéas "
        "2 à 4 sont reproduits intégralement, avec le « 3. » de 1779, les opérations "
        "administratives seules, les trois chapitres, le surplus conservé et le "
        "garant du vendeur. Capital SEM strictement supérieur à la moitié, sans "
        "extension à toutes les sociétés. La nouvelle transition est au cinquième "
        "alinéa ; les alinéas visés restent en place. La garantie de bonne exécution "
        "du h de L. 222-3 est traitée dans L. 222-6 pour ses supports propres : les "
        "deux volets appartiennent à la même mesure, sans double compte des garanties "
        "sur un même contrat. Les garanties de vente et d'assurance ayant un "
        "fondement distinct ne sont pas supprimées. Ni ancien contrat modifié "
        "d'office, ni garantie constituée libérée. Le reste du dispositif SRU 164, "
        "notamment sa filiation réglementaire, ne devient pas achevé par ce seul texte."
    ),
    benefit_review=(
        "Sont maintenues pour les situations futures les dispenses existantes des "
        "SEM à majorité publique, des opérateurs administratifs seuls et des sociétés "
        "construisant pour le vendeur sur le surplus du terrain, avec leurs conditions "
        "et la garantie de ce vendeur. La dispense est étendue explicitement aux "
        "organismes HLM pour les contrats futurs, sans révoquer les protections "
        "contractuelles antérieures ni les garanties issues d'un autre fondement."
    ),
    reference_checks=[],
)
a['substantive_impact'] = impact(
    'material_reduction',
    "La source officielle réserve la première dispense aux SEM à majorité publique ; "
    "la proposition y ajoute les organismes HLM, retirant pour leurs contrats futurs "
    "l'assujettissement obligatoire découlant de L. 222-1. Le gain de fond existait "
    "dans le brouillon et n'est pas présenté comme une seconde suppression. Toutes "
    "les autres exceptions et la garantie finale sont conservées.",
    "Dispense limitée aux règles rendues obligatoires par le premier alinéa de "
    "L. 222-1 et au rôle contractuel de l'organisme HLM, sans exonération générale "
    "de responsabilité ou des garanties distinctes. Contrats antérieurs exclus de "
    "la réforme ; aucun coût de garantie, économie nationale ou solde global n'est chiffré.",
    "Aucune charge nouvelle identifiée : pas d'agrément, de déclaration, de preuve "
    "spéciale ou de registre en remplacement. La qualité HLM désigne le bénéficiaire "
    "de la dispense et les garanties anciennes continuent de plein droit, sans "
    "avenant obligatoire.",
    [effect(
        'relief_extended',
        'hlm-promotion-immobiliere-dispenses',
        "Extension aux organismes HLM de la dispense d'application obligatoire du "
        "régime de promotion pour le rôle visé au premier alinéa.",
        "La dispense fondée sur la qualité de la personne qui s'oblige à faire "
        "construire vise les seules SEM dont plus de la moitié du capital appartient "
        "à des personnes morales de droit public ; les organismes HLM n'y figurent pas.",
        "Les organismes HLM bénéficient de la même dispense pour leurs nouveaux "
        "contrats, quel que soit le maître de l'ouvrage ; majorité publique SEM et "
        "autres exceptions inchangées.",
        'legal_duty',
        "Organismes d'habitations à loyer modéré s'obligeant à faire procéder à "
        "la construction dans le champ du premier alinéa de L. 222-1.",
        "Contrats conclus dès l'entrée en vigueur de la réforme ; contrats "
        "antérieurs, garanties constituées et règles impératives distinctes conservés.",
        "Aucune formalité de remplacement. Les deux articles L. 222-2 et L. 222-6 "
        "forment des volets complémentaires de la même mesure, sans cumul fictif "
        "d'économie pour une même garantie.",
        "Les dispositions du premier alinéa de l'article L. 222-1 ne sont pas non "
        "plus obligatoires, quel que soit le maître de l'ouvrage, lorsque la personne "
        "qui s'oblige à faire procéder à la construction est une société d'économie "
        "mixte dont le capital appartient pour plus de la moitié à des personnes "
        "morales de droit public.",
        p[0].strip(),
    )],
)
answers.append(a)

# L222-6 : dispense de la seule garantie propre à la mission de promotion.
s = sources[3]
p = [
    "Les organismes d'habitations à loyer modéré et les sociétés d'économie mixte "
    "dont le capital appartient pour plus de moitié à des personnes de droit public "
    "ne sont pas tenus de fournir la garantie prévue au h de l'article L. 222-3 "
    "quand ils agissent comme promoteurs liés par un contrat de promotion immobilière, "
    "ou par l'écrit prévu aux articles L. 212-10 et L. 213-6.",
    "La dispense applicable aux organismes d'habitations à loyer modéré vaut pour "
    "les contrats conclus à compter de l'entrée en vigueur de la loi portant la "
    "présente réforme. Elle n'éteint ni ne modifie les garanties valablement constituées "
    "pour les contrats antérieurs et ne prive pas leur bénéficiaire d'une mise en "
    "jeu ultérieure. Les autres garanties imposées par un fondement distinct ne sont pas supprimées.",
]
a = base(s)
a.update(
    proposed_xml=xml(p),
    status='rewrite_draft',
    change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=[
        "Suppression pour les nouveaux contrats des organismes HLM de l'obligation de fournir la garantie de bonne exécution de la mission du promoteur prévue au h de L. 222-3, retirée de la dispense par SRU 164 IV.",
    ],
    reason=(
        "Réforme de fond du brouillon conservée : réintroduire expressément les "
        "organismes HLM dans la dispense de garantie dont SRU 164 IV les avait "
        "exclus. L'allègement porte sur la bonne exécution de la mission du promoteur, "
        "dans les deux supports visés, et reste ouvert aux contrats futurs. Le "
        "bénéfice existant des SEM à majorité publique est maintenu à droit constant. "
        "L'examen supplémentaire ne justifie pas d'effacer les conditions de qualité "
        "et de rôle, qui bornent cette dispense sectorielle, ni de libérer les "
        "garanties anciennes qui protègent les cocontractants. Aucune assurance, "
        "responsabilité, garantie de vente ou garantie du vendeur prévue par un "
        "fondement autonome n'est retirée par généralisation de cette coupe."
    ),
    review_notes=(
        "Source entière avec ses br, note vide, brouillon et texte initial de SRU "
        "164 lus. Son IV retire exactement les organismes HLM de cette dispense ; "
        "la réintroduction est une nouvelle règle expresse, sans renaissance "
        "automatique d'une version abrogée. Le texte authentique antérieur non joint "
        "n'est pas présenté comme relu. L. 222-3 h, L. 212-10 et L. 213-6 ont été "
        "lus en entier dans le corpus, ainsi que L. 222-1 à L. 222-5 : les écrits "
        "portent les énonciations de L. 222-3 et la garantie concerne la mission "
        "du promoteur. Le renvoi au h reste exact ; le contrat et l'écrit restent "
        "distincts. Les mots « plus de moitié », les personnes de droit public et "
        "la qualité SEM sont conservés ; « ils » assure l'accord grammatical après "
        "réintroduction des organismes HLM. Le premier alinéa reste celui de la "
        "dispense ; seule la transition est ajoutée après lui. Les garanties "
        "anciennes restent mobilisables même après la réforme. Même measure_id "
        "que L. 222-2 pour cette mesure de dispenses HLM : aucun double compte "
        "d'une garantie déjà exclue dans une autre configuration contractuelle. "
        "L'article ne prétend pas réécrire les régimes VEFA ou toutes les "
        "coordinations SGA de SRU 164."
    ),
    benefit_review=(
        "La dispense actuelle des SEM dont le capital est majoritairement public "
        "reste intégrale, pour les futures opérations éligibles aussi. La dispense "
        "est étendue aux organismes HLM pour leurs nouveaux contrats de promotion "
        "ou écrits visés. Les bénéficiaires des garanties antérieures gardent leur "
        "mise en jeu ; aucune garantie autonome ni autre exception favorable "
        "n'est supprimée par ce texte."
    ),
    reference_checks=[],
)
a['substantive_impact'] = impact(
    'material_reduction',
    "Comparée à l'intégralité de la source officielle, la dispense de la garantie "
    "du h de L. 222-3 s'applique aussi aux organismes HLM pour l'avenir. Cette "
    "extension, déjà acquise au brouillon, complète L. 222-2 pour les supports "
    "expressément visés ; elle ne démontre ni une nouvelle exonération fiscale "
    "ni la suppression de toutes les garanties de construction.",
    "Seuls les organismes HLM agissant comme promoteurs dans les supports "
    "énumérés sont ajoutés. Garanties anciennes et garanties autonomes hors champ. "
    "Les frais effectivement évités dépendent des contrats et ne sont pas "
    "chiffrés ; pas d'addition des mêmes frais avec L. 222-2 ni de solde global établi.",
    "Aucune charge nouvelle identifiée : la dispense est légale sans dossier, "
    "visa, déclaration ou registre supplémentaire. Les garanties anciennes "
    "restent soumises à leurs règles sans formalité nouvelle ; la réforme "
    "n'instaure ni garantie publique de remplacement ni prélèvement compensatoire.",
    [effect(
        'relief_extended',
        'hlm-promotion-immobiliere-dispenses',
        "Extension HLM de la dispense spécifique de garantie de bonne exécution "
        "dans le contrat de promotion ou l'écrit des sociétés concernées.",
        "Seules les SEM à capital public supérieur à la moitié sont dispensées "
        "par L. 222-6 de la garantie du h de L. 222-3 lorsqu'elles agissent comme "
        "promoteurs dans un contrat de promotion ou un écrit de L. 212-10 ou L. 213-6.",
        "Même dispense pour les organismes HLM dans ces rôles et supports, pour "
        "leurs contrats futurs ; dispense SEM intacte. Aucune suppression générale "
        "des autres garanties et aucun taux fiscal concerné.",
        'legal_duty',
        "Organismes HLM promoteurs liés par contrat de promotion immobilière "
        "ou par l'écrit prévu à L. 212-10 et L. 213-6.",
        "Nouveaux contrats dès l'entrée en vigueur de la réforme ; garanties "
        "valablement constituées pour les anciens contrats conservées et mobilisables.",
        "Aucune garantie, déclaration ou autorisation de remplacement. Même "
        "mesure que L. 222-2, avec un champ complémentaire et sans double "
        "valorisation d'une même garantie.",
        "Les sociétés d'économie mixte dont le capital appartient pour plus de "
        "moitié à des personnes de droit public ne sont pas tenus de fournir la "
        "garantie prévue au h de l'article L. 222-3 quand elles agissent comme "
        "promoteurs liés par un contrat de promotion immobilière, ou par l'écrit "
        "prévu aux articles L. 212-10 et L. 213-6.",
        p[0],
    )],
)
answers.append(a)

# L271-1 : maintien des droits ; retrait supplémentaire de la copie légale intégrale.
s = sources[4]
p = paragraphs(s['source_xml'])
# La dernière balise source contient deux alinéas matériels séparés par des br.
p = p[:5] + re.split(r'<br\s*/?>\s*<br\s*/?>\s*', p[5])
assert len(p) == 7
p[2] = (
    "Lorsque l'acte est conclu par l'intermédiaire d'un professionnel ayant reçu "
    "mandat pour prêter son concours à la vente, cet acte peut être remis directement "
    "au bénéficiaire du droit de rétractation. Dans ce cas, le délai de rétractation "
    "court à compter du lendemain de la remise de l'acte. La preuve de la remise "
    "et de sa date peut être apportée par tout moyen présentant les garanties prévues "
    "au deuxième alinéa, sans mention manuscrite ni attestation distincte obligatoire. "
    "L'acte ou le projet remis indique les règles applicables aux versements, à la "
    "garantie des fonds déposés et à leur restitution prévues à l'article L. 271-2. "
    "La reproduction intégrale de cet article n'est pas exigée."
)
p[6] = p[6].replace("mentionnée à l'avant-dernier alinéa", "mentionnée au sixième alinéa")
p.append(
    "Les modalités de preuve et d'information prévues au troisième alinéa "
    "s'appliquent aux actes et aux projets d'acte remis à compter de l'entrée en "
    "vigueur de la loi portant la présente réforme. Les remises antérieures restent "
    "soumises aux dispositions alors applicables ; leurs effets, les droits des "
    "parties et les délais de rétractation ou de réflexion correspondants sont "
    "conservés. Aucun délai expiré n'est rouvert et aucune remise antérieure "
    "irrégulière n'est régularisée de plein droit."
)
p = [part.strip() for part in p]
a = base(s)
a.update(
    proposed_xml=xml(p),
    status='rewrite_draft',
    change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=[
        "Suppression de l'attestation de remise selon des formes réglementaires obligatoires, dont les mentions à recopier de la main de l'acquéreur, au profit d'une preuve de date et de remise aux garanties équivalentes.",
        "Suppression supplémentaire de la reproduction intégrale obligatoire de L. 271-2 sur l'acte ou le projet remis directement, prescrite par D. 271-6 et D. 271-7 ; les informations utiles sur les versements et leur restitution restent dues.",
    ],
    reason=(
        "Réduction de fond de la procédure de remise directe : conserver la "
        "suppression déjà proposée des mentions manuscrites et du formalisme "
        "réglementaire d'attestation, et retirer en plus la reproduction intégrale de "
        "L. 271-2 encore maintenue par le brouillon. La lecture entière de D. 271-6 "
        "et D. 271-7 révèle cette copie légale obligatoire ; l'information utile "
        "sur les paiements, la garantie et la restitution reste dans l'acte ou le "
        "projet, sans texte légal à reproduire mot pour mot. La preuve probante de "
        "remise demeure, sans nouveau dossier ni déclaration. À droit constant sont "
        "conservés le champ d'actes et d'acquéreurs, les formes de notification et "
        "de rétractation, le mandat du professionnel, l'articulation avec l'avant-contrat, "
        "les deux délais de dix jours, l'information sur ces droits et ses sanctions. "
        "Ces droits favorables et l'interdiction de signer pendant la réflexion "
        "rendent le consentement effectif ; ils ne sont pas des attentes administratives "
        "inutiles à supprimer. Le renvoi de la sanction est coordonné au sixième "
        "alinéa après ajout de la transition."
    ),
    review_notes=(
        "Source entière, note vide, brouillon entier et SRU 72 lus. Le texte de "
        "2000 concernait notamment l'acte sous seing privé, sept jours et un ordre "
        "différent : ni le délai historique ni sa portée ne sont substitués à "
        "la version actuelle. D. 271-6 et D. 271-7 ont été lus intégralement : "
        "ils imposent tant les inscriptions manuscrites que la reproduction de "
        "L. 271-2. Le troisième alinéa écarte expressément ces formes pour les "
        "remises futures, tout en gardant les informations de versement déjà "
        "transmises par cette copie. Les deux décrets doivent être coordonnés "
        "sur leurs deux exigences ; ils ne sont pas modifiés dans ce lot. Le "
        "rappel informatif peut être commun et n'exige pas d'attestation signée "
        "distincte. Le cinquième alinéa étend les modalités du troisième au projet "
        "authentique. L'ordre des sept alinéas matériels est conservé ; la source "
        "regroupait information et sanction dans une balise avec br. Au septième "
        "alinéa, « avant-dernier » devient explicitement « sixième » pour ne pas "
        "viser la sanction elle-même après ajout de la transition. Les alinéas "
        "1, 2, 4, 5 et 6 sont repris dans leurs termes sources. Contrôles dans "
        "le corpus de L. 271-3, L. 231-4, R. 231-8 et L. 721-3, lus en entier : "
        "adjudication authentique exclue, dépôts spéciaux garantis et report du "
        "départ du délai en cas de documents de copropriété manquants non supprimés. "
        "L'articulation du cinquième alinéa entre notification ou remise et ses "
        "modalités demeure ; aucune nouvelle règle de calcul du point de départ. "
        "Les dix jours et les plafonds de 3 000 et 15 000 euros restent exacts. "
        "Le chapitre II du titre II du livre V du code de la consommation est "
        "maintenu dans son objet procédural ; son texte externe n'est pas fourni "
        "et n'est pas présenté comme relu. Les remises anciennes ne sont ni "
        "régularisées ni réitérées de plein droit. Aucun achèvement des autres "
        "descendants de SRU 72, notamment l'article 1589-1 du code civil, n'est affirmé."
    ),
    benefit_review=(
        "Les futurs acquéreurs non professionnels conservent rétractation et "
        "réflexion de dix jours, remise directe par professionnel mandaté, "
        "application à l'avant-contrat seul lorsqu'il existe et information "
        "compréhensible. Les formes alternatives probantes restent ouvertes. "
        "Les restrictions aux versements, exceptions législatives, garantie et "
        "restitution de L. 271-2 sont intégralement conservées dans cet article ; "
        "seule leur copie mot à mot sur l'acte cesse d'être obligatoire. La "
        "protection des remises antérieures et le report prévu par L. 721-3 demeurent."
    ),
    reference_checks=[],
)
a['substantive_impact'] = impact(
    'material_reduction',
    "Par rapport à la source officielle entière et à ses modalités de remise "
    "réglementaires lues, l'attestation formalisée, les mentions manuscrites et "
    "la reproduction intégrale de L. 271-2 cessent d'être imposées. La dernière "
    "suppression est supplémentaire au brouillon. Les informations utiles et "
    "la preuve de la remise demeurent ; aucun délai favorable de dix jours "
    "n'est diminué, aucune sanction n'est accrue.",
    "Allègement limité à la remise directe par professionnel mandaté et au "
    "projet authentique auquel ces modalités s'appliquent. Les autres notifications, "
    "la remise des documents de copropriété et les anciens actes gardent leurs "
    "règles. D. 271-6 et D. 271-7 sont à coordonner ; aucun coût net de rédaction "
    "ni solde de complexité de l'ensemble des codes n'est établi.",
    "Aucune nouvelle catégorie de données, aucun registre, délai ou dépôt "
    "identifié. Les informations sur les versements remplacent leur reproduction "
    "légale intégrale, déjà obligatoire dans les deux cas de remise : ce n'est "
    "pas une nouvelle information exigée des autres actes. Une adaptation "
    "rédactionnelle des actes peut être nécessaire et son coût n'est pas chiffré ; "
    "la preuve existante reste nécessaire, sans attestation distincte imposée.",
    [effect(
        'obligation_removed',
        'acquereur-remise-directe-formalisme-reduit',
        "Retrait des formes obligatoires d'attestation de la remise et de la "
        "copie intégrale de L. 271-2, sans retrait de l'information utile.",
        "Remise directe par professionnel mandaté : attestation selon décret ; "
        "D. 271-6 et D. 271-7 imposent les mentions manuscrites et la reproduction "
        "de L. 271-2 sur l'acte ou le projet authentique remis. Les droits de "
        "rétractation et de réflexion durent dix jours.",
        "Même remise et mêmes droits de dix jours : preuve présentant les "
        "garanties du deuxième alinéa, sans manuscrit ou attestation distincte "
        "obligatoire et sans copie intégrale de L. 271-2. Les informations de "
        "versement, garantie et restitution restent dans le document remis.",
        'legal_duty',
        "Acquéreurs non professionnels et professionnels mandatés procédant "
        "à une remise directe de l'acte ou du projet authentique visé au cinquième alinéa.",
        "Remises effectuées dès l'entrée en vigueur ; règles et effets des "
        "remises antérieures conservés, sans réouverture d'un délai expiré "
        "ni validation d'une remise irrégulière.",
        "Preuve datée toujours nécessaire et information sur les fonds "
        "maintenue, à la place de sa copie légale intégrale ; pas de "
        "certification ou de déclaration de remplacement. Coût net non chiffré.",
        paragraphs(s['source_xml'])[2],
        p[2],
    )],
)
answers.append(a)

# L271-2 : maintien de la source, pas de nouvelle version stylistique.
s = sources[5]
a = base(s)
a.update(
    proposed_xml=None,
    status='retained_unchanged',
    classification='retained_necessary',
    reason=(
        "Maintien intégral de la source après examen du brouillon et de chaque "
        "charge, sans conserver son simple changement de mots. L'interdiction "
        "des versements pendant la rétractation protège effectivement les fonds "
        "et le consentement de l'acquéreur. Les exceptions législatives et la "
        "réception par un professionnel mandaté et financièrement garanti "
        "permettent déjà les opérations recevables ; supprimer leur condition "
        "de garantie exposerait les fonds plutôt qu'un doublon administratif. "
        "La condition suspensive du versement différé est une protection "
        "contractuelle utile. Les vingt et un jours sont une borne maximale "
        "de restitution, pas un délai minimal d'attente : l'allonger ou le "
        "supprimer sans restitution exigible retirerait un avantage, et le "
        "raccourcir créerait une charge nouvelle non nécessaire à la coupe "
        "demandée. La réflexion authentique et l'amende rendent les interdictions "
        "effectives. Aucune taxe, autorisation, déclaration ou pièce redondante "
        "n'a été identifiée dans cet article. Aucune réécriture ou simplification "
        "matérielle n'est comptée pour ce maintien."
    ),
    review_notes=(
        "Les quatre alinéas de la source, ses br, la note vide, le brouillon "
        "intégral et le texte initial de SRU 72 ont été lus. Le délai historique "
        "de sept jours et l'amende de 200 000 F ne remplacent pas les dix jours "
        "et 30 000 euros de la source actuelle. Le renvoi à L. 271-1 a été "
        "confronté à sa source et à la proposition du présent lot : champ des "
        "actes, acquéreur non professionnel, délai de rétractation et réflexion "
        "restent cohérents. La suppression de la copie obligatoire de L. 271-2 "
        "dans L. 271-1 ne supprime aucune règle de L. 271-2. L. 271-3, L. 231-4 "
        "et R. 231-8 ont été lus entièrement dans le corpus : adjudication "
        "authentique hors section, dépôts spéciaux et garantie de remboursement "
        "de la construction gardent leur champ. La restitution immédiate du "
        "dépôt de garantie dans le cas propre de L. 231-4 n'est pas remplacée "
        "par vingt et un jours. Le premier alinéa conserve sa liste non "
        "exhaustive de dérogations, le deuxième le mandat et l'affectation de "
        "la garantie aux fonds déposés. Le lendemain de la rétractation reste "
        "le départ des vingt et un jours ; dix jours authentiques et engagement "
        "de versement dans l'infraction sont maintenus. Pas de transition "
        "nouvelle pour une disposition inchangée, pas de fermeture des "
        "avantages aux contrats futurs. Le volet civil 1589-1 cité par "
        "SRU 72 n'est pas réécrit ni réputé vérifié dans le corpus fourni."
    ),
    benefit_review=(
        "Sont conservés pour les futures situations éligibles les exceptions "
        "législatives de versement du neuf, des parts, de la vente à construire "
        "et de la location-accession, la possibilité de dépôt chez un "
        "professionnel garanti et la condition suspensive du versement différé. "
        "L'acquéreur garde le remboursement dans les vingt et un jours, ainsi "
        "que toute restitution spéciale plus favorable, et l'absence de "
        "versement pendant la réflexion authentique. Aucun avantage n'est "
        "restreint au stock antérieur."
    ),
    reference_checks=[],
)
a['substantive_impact'] = impact(
    'retained_necessary',
    "L'intégralité de la source officielle est maintenue, avec ses exceptions "
    "et garanties. La révision stylistique antérieure est écartée : aucune "
    "obligation supprimée ni baisse de prélèvement n'est revendiquée. Chaque "
    "contrainte assure la disponibilité du droit de rétractation ou la "
    "sécurité des fonds de l'acquéreur.",
    "Ce maintien ne vaut pas examen de tous les régimes spéciaux de dépôt "
    "ni des autres articles de SRU 72 ; les textes de construction et "
    "l'exception des adjudications conservent leur champ propre. Aucun "
    "allègement nouveau, gain chiffré ou solde global de complexité n'est démontré.",
    "Aucune charge nouvelle identifiée, puisque la source est conservée "
    "sans modification : ni donnée, registre, attestation, autorisation "
    "ou délai ajouté. Les conditions du professionnel garanti et de "
    "la restitution sont des protections existantes, sans procédure "
    "nouvelle de remplacement.",
    [],
)
answers.append(a)

with open('answer.json', 'w', encoding='utf-8') as f:
    json.dump(answers, f, ensure_ascii=False, indent=2)
    f.write('\n')

print('answer.json :', len(answers), 'articles')
