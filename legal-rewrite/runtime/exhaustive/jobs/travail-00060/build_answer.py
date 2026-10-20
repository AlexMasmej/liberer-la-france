import json
import re
from html import unescape
from pathlib import Path

sources = json.loads(Path("source.json").read_text())
by_number = {a["number"]: a for a in sources}
answers = {}


def impact(classification, assessment, scope, burdens, effects=None):
    return {
        "version": 1,
        "classification": classification,
        "assessment": assessment,
        "scope_limitations": scope,
        "new_burdens_review": burdens,
        "effects": effects or [],
    }


def base(number, reason, notes, assessment):
    a = by_number[number]
    result = {k: a[k] for k in ("code_id", "source_id", "source_sha256", "number")}
    result.update(reason=reason, review_notes=notes, substantive_impact=assessment)
    answers[number] = result
    return result


def retained(number, reason, notes, assessment, scope, burdens, benefit=None):
    r = base(number, reason, notes, impact("retained_necessary", assessment, scope, burdens))
    r.update(status="retained_unchanged", proposed_xml=None, classification="retained_necessary")
    if benefit is not None:
        r["benefit_review"] = benefit


def effect(kind, measure_id, description, before, after, unit, population,
           transition, replacement, source_quote, proposed_quote):
    return {
        "kind": kind, "measure_id": measure_id, "description": description,
        "before": before, "after": after, "unit": unit,
        "affected_population": population, "conditions_and_transition": transition,
        "replacement_or_new_burdens": replacement,
        "source_quote": source_quote, "proposed_quote": proposed_quote,
    }


def reduced(number, proposed, reason, notes, removed, assessment):
    r = base(number, reason, notes, assessment)
    r.update(
        status="rewrite_draft", proposed_xml=proposed,
        change_type="normative_reduction",
        reform_policy_id="editorial_direction_2026_10_19",
        removed_provisions=removed,
    )
    return r


retained(
    "L2316-8",
    "Maintien intégral après examen du circuit de répartition des sièges. L'accord conclu selon la double majorité de L2314-6 demeure la voie première ; aucune autorisation administrative n'est exigée lorsqu'il existe. En cas de désaccord, l'arbitrage administratif assure une répartition indépendante entre établissements et collèges. Le recours judiciaire est une garantie contre cette décision, non une seconde validation systématiquement obligatoire. La suspension du scrutin et la prorogation des mandats évitent une représentation irrégulière ou interrompue ; leur suppression n'est pas justifiée.",
    "L2314-6, L2316-4 à L2316-7 et R2316-1/2/9 lus. Maintenir les cinq alinéas, y compris l'application immédiate de la nouvelle répartition sans attendre tous les renouvellements et l'exclusivité du recours judiciaire. R2316-2 vise improprement le premier alinéa pour la compétence administrative, alors que le désaccord figure au deuxième ; ce décalage réglementaire préexistant et la désignation administrative ancienne restent à coordonner dans cet article hors lot. Le présent renvoi à L2314-6 est cohérent. La note historique d'entrée en vigueur au plus tard en 2018 n'est pas une date future de réforme.",
    "La source entière organise un accord, puis seulement en cas d'échec une décision indépendante susceptible de recours. Aucune taxe, déclaration périodique, pièce justificative supplémentaire ou double approbation générale n'y est instituée. La règle reste entière pour préserver la représentation électorale et sa continuité.",
    "Aucune réduction nouvelle n'est revendiquée. Le délai réglementaire de décision de deux mois et les recours de quinze jours ne sont pas modifiés ; leur efficacité pratique et les coordinations de R2316-2 restent hors de ce maintien.",
    "Aucune charge nouvelle n'est identifiée : le texte source demeure intégralement applicable, sans registre, dépôt, délai ou condition supplémentaire. Aucun solde global de coût ou de complexité des codes n'est établi.",
)

retained(
    "L2316-9",
    "Maintien intégral du juge compétent pour l'électorat, la régularité des élections et la désignation syndicale. La prise en charge par l'État d'une mesure d'instruction indispensable est un avantage d'accès effectif au juge, et non un prélèvement à supprimer. Aucun dossier annuel, agrément ou justificatif redondant n'est imposé par cet article ; retirer cette garantie déplacerait le coût du contrôle sur les parties.",
    "R2316-10 et R2314-24/25 lus : requête, délais distincts de trois jours pour l'électorat et de quinze jours pour les opérations ou désignations, jugement et pourvoi restent à leur champ propre. Ne pas confondre ces délais électoraux avec le préavis individuel du contrat unique. La mesure d'instruction demeure subordonnée à son caractère indispensable ; le texte ne rend pas gratuits tous les frais privés d'un procès.",
    "La source entière garantit un recours judiciaire identifiable et fait supporter à l'État les dépenses de l'instruction indispensable. Son maintien protège un avantage utile sans formalité nouvelle et sans présenter les dépenses publiques conservées comme une économie.",
    "La prise en charge ne couvre que les mesures d'instruction indispensables visées par le texte, non tous les honoraires ou frais des parties. Aucun élargissement de compétence ou de gratuité n'est proposé.",
    "Aucune charge nouvelle n'est identifiée : maintien exact des conditions de contestation et de prise en charge, sans attestation ni demande périodique ajoutée. Le coût public de cette garantie n'est pas chiffré.",
    "L'avantage possible est la prise en charge par l'État des dépenses d'une mesure d'instruction indispensable à une contestation électorale ou de désignation syndicale. Il est maintenu sans plafond ou restriction nouvelle, pour les litiges futurs éligibles comme pour ceux déjà engagés. La compétence judiciaire contribue à l'accès au recours ; elle ne constitue pas une taxe ni une dispense générale de tous frais de procédure.",
)

retained(
    "L2316-10",
    "Maintien intégral du renouvellement quadriennal du CSE central après les élections générales des CSE d'établissement. Ce scrutin désigne une représentation centrale distincte ; il ne duplique pas l'élection directe des établissements. Le rythme fixe rend les mandats prévisibles et évite des élections centrales répétées à chaque renouvellement isolé. La dérogation conventionnelle favorable de L2316-11, entre deux et quatre ans, demeure ouverte.",
    "L2316-4 et L2316-11 lus : les élus d'établissement désignent les représentants centraux, avec faculté de durée conventionnelle de deux à quatre ans. Ne pas assimiler la durée du mandat à celle du contrat de travail ni supprimer les nouveaux CDI au terme du mandat. Les mécanismes de continuité en cas de transfert de L2316-12 restent distincts.",
    "Le délai de quatre ans fixe une durée de représentation, non un délai administratif minimal avant d'embaucher. Supprimer cette règle laisserait sans calendrier le renouvellement des délégués centraux ; aucune charge accessoire dissociable n'a été identifiée dans la source entière.",
    "Aucun scrutin ni coût électoral n'est déclaré supprimé. Les durées conventionnelles de deux à quatre ans et les transferts d'établissements gardent leur propre régime.",
    "Aucune charge nouvelle n'est identifiée : le calendrier légal reste identique, sans nouvelle élection, information ou pièce exigée. Aucun solde global des coûts électoraux n'est déduit de ce maintien.",
)

retained(
    "L2316-11",
    "Maintien intégral de la faculté de fixer par accord de branche, de groupe ou d'entreprise un mandat central de deux à quatre ans. Il s'agit d'une dérogation d'organisation utile au calendrier quadriennal, non d'une autorisation administrative. La retirer fermerait une souplesse favorable sans retirer d'obligation générale ni de prélèvement.",
    "L2316-10 lu : quatre ans à défaut de dérogation. Conserver les trois niveaux d'accord, l'expression selon le cas et les bornes de deux et quatre ans. L'article ne permet ni prorogation au-delà de quatre ans ni renouvellement automatique d'un contrat à durée déterminée. Les accords futurs éligibles conservent cette possibilité.",
    "La source entière ouvre une souplesse conventionnelle sans imposer de négociation distincte à toutes les entreprises. Elle est maintenue avec ses bornes et ses bénéficiaires, sans réduction fictive du nombre d'élections.",
    "Le maintien ne modifie ni les conditions générales de validité des accords ni le renouvellement quadriennal supplétif ; aucune économie ou diminution du nombre de scrutins n'est démontrée.",
    "Aucune charge nouvelle n'est identifiée : aucun accord n'est rendu obligatoire et aucun agrément, envoi ou justificatif supplémentaire n'est créé. Les conditions de la dérogation restent celles de la source.",
    "L'avantage possible est la dérogation conventionnelle au mandat légal de quatre ans : une durée de deux à quatre ans peut être choisie, selon le cas, par accord de branche, de groupe ou d'entreprise. La proposition maintient intégralement cette faculté pour les accords futurs éligibles, sans la réserver aux accords existants ni ajouter une autorisation ou une formalité. Les bornes protectrices restent inchangées.",
)

retained(
    "L2316-12",
    "Maintien intégral des quatre alinéas assurant la continuité de la représentation lors d'un changement juridique d'employeur. La conservation du comité lorsque l'autonomie juridique subsiste, la désignation de représentants en cas d'absorption et la représentation des établissements transférés évitent une interruption des mandats. Le dépassement temporaire du plafond de représentants est une dérogation favorable à conserver ; il n'est pas justifié de supprimer cette protection au motif de simplifier une fusion.",
    "L1224-1, L2316-4 et R2316-1 lus : les contrats en cours subsistent ; le plafond réglementaire est de vingt-cinq titulaires et vingt-cinq suppléants sauf accord applicable. Maintenir la distinction autonomie juridique/établissement distinct et le délai d'un an au plus des deuxième et troisième alinéas. La formule source « deux représentants titulaires et suppléants » est conservée sans trancher silencieusement son éventuelle ambiguïté de décompte. Articulation des garanties de transfert avec le droit européen à contrôler dans son champ propre.",
    "La source entière évite une nouvelle élection générale immédiate et autorise une représentation transitoire au-delà du plafond. Ces mécanismes protègent les élus et les salariés ; aucune déclaration autonome, taxe ou agrément n'est à retirer de cet article.",
    "Aucune extension de la période d'un an ni du champ de L1224-1 n'est proposée. Le régime des salariés protégés et les contraintes européennes de continuité ne sont pas réputés supprimés.",
    "Aucune charge nouvelle n'est identifiée : les désignations et représentations transitoires existantes restent seules requises. Aucun nouveau registre de transfert ni justificatif d'ancienneté n'est institué.",
)

retained(
    "L2316-13",
    "Maintien intégral de la personnalité civile, de la présidence et du secrétariat du CSE central. La personnalité permet d'administrer les fonds et d'agir en justice. Le secrétaire et l'adjoint chargé de la santé, de la sécurité et des conditions de travail assurent des fonctions distinctes utiles ; leur désignation n'est pas une déclaration administrative. Les deux collaborateurs de l'employeur restent facultatifs et seulement consultatifs : aucune assistance imposée n'est à supprimer.",
    "R2316-3 lu : secrétaire, adjoint et trésorier désignés parmi les titulaires. Préserver le plafond de deux collaborateurs et leur absence de voix délibérative. L'assouplissement de L2316-14 ne supprime ni ces organes ni les règles de comptes de L2316-19. La durée du mandat ne termine pas le contrat de travail.",
    "La source entière attribue une capacité juridique et organise des interlocuteurs identifiés, dont un pour la prévention. Après examen, aucun poste administratif externe, agrément, dépôt ou prélèvement accessoire sans fonction essentielle n'est isolé.",
    "Ce maintien ne fusionne pas le secrétaire et son adjoint et ne supprime pas le trésorier prévu au règlement. Les coûts de fonctionnement ne sont ni estimés ni déclarés réduits.",
    "Aucune charge nouvelle n'est identifiée : les fonctions, la limite de deux assistants et leurs pouvoirs restent identiques, sans document de désignation supplémentaire ni nouvelle périodicité.",
)

reduced(
    "L2316-14",
    "<p>Le comité social et économique central détermine les modalités de son fonctionnement et de ses rapports avec les salariés de l'entreprise pour l'exercice des missions qui lui sont conférées par le présent titre. Il peut les réunir dans un règlement intérieur, sans être tenu d'y consigner celles qui ne font pas l'objet d'une prescription légale particulière.</p>"
    "<p>Les décisions du comité social et économique central portant sur ses modalités de fonctionnement et l'organisation de ses travaux ainsi que ses résolutions sont prises à la majorité des membres présents.</p>"
    "<p>L'absence d'obligation générale de consignation ne dispense pas des mentions particulières que d'autres dispositions imposent dans le règlement intérieur, dans leur champ propre.</p>"
    "<p>Cette suppression de l'obligation générale de consignation s'applique à compter de l'entrée en vigueur de la loi portant la présente rédaction. Les règlements intérieurs déjà adoptés demeurent applicables jusqu'à leur modification régulière ; les décisions et droits antérieurs ne sont pas remis en cause.</p>",
    "Réforme de fond limitée : retirer l'obligation de consigner toutes les modalités générales de fonctionnement et de relations avec les salariés dans le règlement intérieur du CSE central. Le comité continue de déterminer ses modalités et de décider à la majorité des membres présents. Les mentions particulières légalement nécessaires aux comptes, à la commission des marchés ou, selon le cas, à la santé et sécurité restent obligatoires. La coupe porte sur le contenu général imposé, et non sur la disparition de tout règlement intérieur ; elle n'est pas une reformulation à droit constant.",
    "L2315-44, L2315-44-1 à L2315-44-4, L2315-68/69 et L2316-19 lus. Les modalités d'arrêté des comptes et d'établissement du rapport de gestion restent inscrites au règlement intérieur par leurs bases propres ; les mentions de commissions restent dues lorsqu'elles sont applicables au comité central. L2315-24 régit le CSE de droit commun : le présent allègement spécial ne le réécrit pas pour les établissements. Aucune règle de majorité, de participation, de rémunération ou d'information des salariés n'est retranchée. Aucun document équivalent de remplacement n'est créé.",
    ["L'obligation générale de consigner dans un règlement intérieur toutes les modalités de fonctionnement et de rapports avec les salariés, hors mentions particulières légalement requises, est supprimée."],
    impact(
        "material_reduction",
        "Par rapport à la source entière, les modalités générales ne doivent plus toutes être consignées dans le règlement intérieur. La majorité des présents reste inchangée. Le gain est une réduction du contenu formel imposé ; les comptes imposent encore des mentions dans un règlement intérieur, si bien qu'aucune suppression complète de ce document n'est revendiquée.",
        "La coupe est limitée au CSE central et aux modalités sans prescription spéciale. L2315-68/69 et les règles propres aux commissions demeurent ; ni toute documentation interne ni tout contrôle financier n'est supprimé. Aucun gain de temps ou coût national n'est chiffré.",
        "Aucune charge nouvelle n'est identifiée : la détermination des modalités et leur adoption majoritaire existaient déjà ; aucune déclaration, registre ou décision de remplacement n'est exigé. Les mentions spéciales et la modification régulière d'un règlement existant conservent leurs fondements antérieurs.",
        [effect(
            "obligation_removed", "cse-central-fin-consignation-generale-reglement",
            "Retrait de la consignation obligatoire des modalités générales sans prescription spéciale.",
            "Le CSE central doit déterminer dans un règlement intérieur ses modalités générales de fonctionnement et de rapports avec les salariés.",
            "Le comité détermine toujours ces modalités ; leur consignation n'est obligatoire que dans les cas imposés par une disposition particulière.",
            "legal_duty", "CSE centraux et leurs membres chargés de formaliser les modalités générales.",
            "Dès l'entrée en vigueur de la loi ; règlements existants valables jusqu'à modification régulière, mentions spéciales et droits antérieurs préservés.",
            "Aucun document général équivalent ; mentions financières et autres mentions légales particulières maintenues.",
            "Le comité social et économique central détermine, dans un règlement intérieur, les modalités de son fonctionnement et de ses rapports avec les salariés de l'entreprise pour l'exercice des missions qui lui sont conférées par le présent titre.",
            "Il peut les réunir dans un règlement intérieur, sans être tenu d'y consigner celles qui ne font pas l'objet d'une prescription légale particulière.",
        )],
    ),
)

reduced(
    "L2316-15",
    "<p>Le comité social et économique central d'entreprise se réunit au moins une fois tous les six mois sur convocation de l'employeur.</p>"
    "<p>Il peut tenir des réunions exceptionnelles à la demande de la majorité de ses membres.</p>"
    "<p>Le lieu de réunion n'est pas obligatoirement le siège de l'entreprise. Les garanties de participation effective et les règles de rémunération et de prise en charge des déplacements demeurent applicables dans leur champ propre.</p>"
    "<p>La suppression du lieu légal obligatoire s'applique aux réunions convoquées à compter de l'entrée en vigueur de la loi portant la présente rédaction. Les convocations antérieures et les stipulations conventionnelles valablement applicables conservent leurs effets.</p>",
    "Réforme de fond : supprimer la tenue obligatoirement au siège de l'entreprise, qui impose un lieu uniforme même lorsque les établissements et les membres sont dispersés. La convocation patronale, la réunion au moins semestrielle et la réunion exceptionnelle demandée par la majorité sont conservées intégralement. Le choix d'un autre lieu n'emporte aucune suppression des droits de participation, de rémunération ou de déplacement. Aucun accord ou dépôt préalable de remplacement n'est institué.",
    "L2315-1 et L2315-11 lus ; la prise en compte des unités dispersées et le temps de réunion rémunéré restent à leur champ propre. Coordonner avec L2316-16 pour la visioconférence sans rendre celle-ci obligatoire. L2316-4 conserve les participants consultatifs de santé et sécurité identifiés au siège, quel que soit le lieu choisi : leur rattachement n'est pas une obligation d'y tenir la séance. Le minimum de six mois n'est pas supprimé et les accords existants ne sont pas révisés automatiquement.",
    ["L'obligation de tenir les réunions du CSE central au siège de l'entreprise est retirée, sans remplacement par une autorisation de changement de lieu."],
    impact(
        "material_reduction",
        "La source entière imposait le siège comme lieu des réunions ordinaires. Cette contrainte géographique disparaît, tandis que le rythme semestriel, la convocation et le droit de demander une réunion exceptionnelle restent identiques. Une réduction effective du déplacement ou de son coût n'est pas présumée dans chaque entreprise.",
        "Seul le lieu légal obligatoire du CSE central est supprimé. Les accords applicables, l'accessibilité effective et les droits de réunion subsistent ; aucune baisse de frais, d'heures rémunérées ou de prélèvement n'est chiffrée.",
        "Aucune charge nouvelle n'est identifiée : le lieu faisait déjà partie de l'organisation des séances et aucune déclaration, accord préalable ou équipement nouveau n'est exigé. Les garanties mentionnées ont leurs bases antérieures ; le solde des coûts de déplacement et d'organisation reste inconnu.",
        [effect(
            "obligation_removed", "cse-central-liberte-lieu-reunion",
            "Suppression du siège de l'entreprise comme lieu légal obligatoire.",
            "Réunion au moins tous les six mois au siège de l'entreprise sur convocation patronale.",
            "Même convocation et périodicité, sans lieu légal obligatoire au siège ; garanties de participation et droits de réunion conservés.",
            "legal_duty", "Employeurs et membres des CSE centraux, notamment dans les entreprises à établissements dispersés.",
            "Réunions convoquées dès entrée en vigueur ; convocations antérieures et stipulations conventionnelles applicables préservées.",
            "Aucun visa ni déclaration de changement de lieu ; aucun abaissement des garanties de participation ou des droits aux frais dans leur champ propre.",
            "Le comité social et économique central d'entreprise se réunit au moins une fois tous les six mois au siège de l'entreprise sur convocation de l'employeur.",
            "Le lieu de réunion n'est pas obligatoirement le siège de l'entreprise.",
        )],
    ),
)

reduced(
    "L2316-16",
    "<p>Le recours à la visioconférence pour réunir le comité social et économique central peut être organisé par accord entre l'employeur et les membres élus du comité. En l'absence d'accord, ce recours est possible sans limitation du nombre de réunions par année civile. Un décret détermine les conditions dans lesquelles le comité social et économique central peut, dans ce cadre, procéder à un vote à bulletin secret.</p>"
    "<p>Cette suppression de la limite légale s'applique aux réunions convoquées à compter de l'entrée en vigueur de la loi portant la présente rédaction. Elle ne rend pas la visioconférence obligatoire et ne remet pas en cause les modalités d'organisation résultant d'accords valablement conclus, tant qu'elles demeurent applicables. Les garanties d'identification des membres, de participation effective aux délibérations et de secret des votes demeurent applicables. Les réunions convoquées avant cette date restent soumises aux règles qui leur étaient applicables.</p>",
    "Coordination de fond avec la suppression déjà proposée du plafond de visioconférences à L2315-4 : retirer aussi le plafond autonome de trois réunions du CSE central et l'accord nécessaire pour le dépasser. Un accord peut toujours organiser les modalités des réunions ; les accords valables et les garanties techniques restent applicables. Cette déclinaison centrale de la même mesure ne constitue pas une seconde suppression générale d'autorisation.",
    "L2315-4 officiel et proposé, D2315-1/2 et D2316-8 lus intégralement : identification, son et image continus et simultanés, accès technique de tous, suspensions, confidentialité, anonymat du vote et durée de vote identique doivent subsister. D2316-8 porte un renvoi préexistant inexact à R2315-1 et suivants ; il reste à corriger vers D2315-1/2 dans le lot réglementaire, sans supprimer ses garanties. La présente loi conserve elle-même participation effective et secret. Rémunération des réunions de L2315-11 maintenue. Même clé de mesure que L2315-4, sans double comptage.",
    ["Le plafond autonome de trois réunions centrales en visioconférence par année civile sans accord, ainsi que l'accord requis pour dépasser ce plafond, sont supprimés."],
    impact(
        "coordination_only",
        "La source entière contenait encore un plafond autonome de trois réunions centrales sans accord. Son retrait met le CSE central en cohérence avec la mesure déjà retenue pour le CSE à L2315-4 ; l'effet concret sur la règle centrale est établi mais n'est pas une nouvelle mesure générale à additionner.",
        "Seul le plafond légal disparaît ; accords applicables, accès effectif, secret, consultations et rémunération restent opposables. D2316-8 doit encore recevoir sa correction de renvoi réglementaire. Aucun gain net de frais ou de complexité n'est chiffré.",
        "Aucune charge nouvelle n'est identifiée : la visioconférence reste une possibilité, sans matériel ou abonnement personnel rendu obligatoire, ni accord de remplacement. Les garanties techniques existaient déjà ; les coûts de réunions à distance plus fréquentes ne sont pas évalués.",
        [effect(
            "coordination", "cse-visioconference-fin-plafond-legal",
            "Application au CSE central de la levée du plafond légal déjà retenue pour le CSE.",
            "Pour le CSE central, sans accord employeur-élus, le recours est limité à trois réunions par année civile.",
            "Pour le CSE central, le nombre n'est plus plafonné légalement en l'absence d'accord ; accords et garanties techniques conservés.",
            "legal_duty", "Employeurs et membres des CSE centraux recourant à la visioconférence sans accord.",
            "Réunions convoquées dès entrée en vigueur ; convocations antérieures et modalités conventionnelles applicables préservées.",
            "Aucun accord ou dépôt de substitution ; identification, participation, rémunération et vote secret conservent leurs garanties.",
            "En l'absence d'accord, ce recours est limité à trois réunions par année civile.",
            "En l'absence d'accord, ce recours est possible sans limitation du nombre de réunions par année civile.",
        )],
    ),
)

reduced(
    "L2316-17",
    "<p>L'ordre du jour des réunions du comité social et économique central est arrêté par le président et le secrétaire.</p>"
    "<p>Les consultations rendues obligatoires par une disposition législative ou réglementaire ou par un accord collectif de travail sont inscrites de plein droit à l'ordre du jour par le président ou le secrétaire.</p>"
    "<p>L'ordre du jour est communiqué aux membres trois jours au moins avant la séance.</p>"
    "<p>Ce délai ne réduit ni le délai d'examen suffisant et le droit aux informations précises et écrites nécessaires à la consultation, ni les délais particuliers de communication des documents, ni les garanties conventionnelles plus favorables applicables.</p>"
    "<p>La réduction du délai de communication de l'ordre du jour s'applique aux réunions convoquées à compter de l'entrée en vigueur de la loi portant la présente rédaction. Les convocations antérieures et les droits et recours relatifs aux consultations déjà engagées demeurent régis par les dispositions qui leur étaient applicables.</p>",
    "Réforme de fond : ramener de huit à trois jours le délai minimal de communication du seul ordre du jour du CSE central, en cohérence avec les trois jours du CSE de droit commun. Le délai de consultation sur le fond n'est pas réduit, et les documents soumis à un délai particulier restent transmis dans ce délai. La fixation conjointe président-secrétaire et l'inscription de plein droit par l'un ou l'autre des consultations obligatoires sont conservées ; aucun accord de réduction, renoncement au recours ou déclaration de remplacement n'est exigé.",
    "L2315-30, L2312-15, R2312-6 et D2316-5 lus : distinguer les trois jours pour l'ordre du jour des délais d'avis d'un, deux ou trois mois et de la transmission des avis d'établissement sept jours avant l'échéance centrale. D2316-5 conserve huit jours pour les documents de L2315-70/71 ; la présente réduction ne les abaisse pas. Le délai d'examen suffisant, les informations écrites et le recours au juge sont conservés. Les garanties conventionnelles plus favorables restent applicables. Aucune prétention de procédure collective complète en trois jours ou de rupture individuelle achevée en quinze jours.",
    ["Le délai minimal légal de huit jours pour communiquer le seul ordre du jour au CSE central est réduit à trois jours, sans réduction des délais particuliers de documents ni du temps d'examen suffisant."],
    impact(
        "material_reduction",
        "La comparaison de la source entière démontre une réduction de cinq jours du minimum de communication de l'ordre du jour : huit deviennent trois. Le contenu et les auteurs de l'ordre du jour restent identiques ; le temps d'examen des projets et les communications spéciales ne sont pas réduits par cette mesure.",
        "La possibilité de réunir plus tôt dépend encore des documents dus, du délai d'examen suffisant et des garanties conventionnelles plus favorables. Les huit jours propres aux documents comptables de D2316-5 sont maintenus ; aucune durée totale de consultation ni économie nationale n'est déduite.",
        "Aucune charge nouvelle n'est identifiée : l'ordre du jour et sa communication étaient déjà obligatoires ; ni consentement formalisé de remplacement ni nouvel accusé de réception n'est demandé. Les réserves d'information suffisante et de délais spéciaux conservent des garanties préexistantes.",
        [effect(
            "deadline_reduced", "cse-central-delai-ordre-du-jour-trois-jours",
            "Réduction du minimum de communication du seul ordre du jour.",
            "Ordre du jour communiqué aux membres du CSE central au moins huit jours avant la séance ; délai exprimé en jours, sans qualification de jours ouvrés.",
            "Ordre du jour communiqué au moins trois jours avant la séance ; documents soumis à délais spéciaux et temps d'examen suffisant conservés.",
            "calendar_days", "Président, secrétaire et membres des CSE centraux pour les réunions relevant du délai légal.",
            "Réunions convoquées dès entrée en vigueur ; convocations antérieures, recours et garanties conventionnelles plus favorables préservés.",
            "Même ordre du jour, sans demande de dérogation ou déclaration nouvelle ; aucune réduction automatique du délai de consultation sur le fond.",
            "L'ordre du jour est communiqué aux membres huit jours au moins avant la séance.",
            "L'ordre du jour est communiqué aux membres trois jours au moins avant la séance.",
        )],
    ),
)

retained(
    "L2316-18",
    "Maintien intégral de la commission centrale de santé, sécurité et conditions de travail à partir de trois cents salariés. Elle traite la prévention à l'échelle commune de l'entreprise, tandis que les commissions d'établissement interviennent localement : ce n'est pas un rapport ou une autorisation administrative doublonnés. Les risques et conditions transversales justifient cette fonction spécialisée ; aucun motif n'établit que sa suppression préserverait une représentation de santé aussi effective.",
    "L2315-36 à L2315-39 et L2315-41 à L2315-44 lus : compétence consultative et recours à l'expert restent au comité, qui délègue des missions à la commission ; composition, majorité, formation et moyens demeurent dans leur champ. Le corpus consulté ne comporte pas de L2315-40 ; il n'est pas inventé. Conserver le seuil de trois cents salariés et les garanties applicables, en coordonnant les exigences européennes de participation en santé au travail plutôt qu'en les réputant supprimées.",
    "La source entière impose une structure de prévention pour les entreprises d'au moins trois cents salariés. Après examen des doublons avec les établissements, sa fonction centrale de santé et sécurité demeure nécessaire ; aucune taxe, pièce répétée ou déclaration autonome n'y est isolée.",
    "Aucune commission centrale ni aucun crédit d'heures n'est supprimé. Les règles de commissions dans les établissements à risques ou sous le seuil gardent leur champ propre ; leur simplification éventuelle n'est pas démontrée ici.",
    "Aucune charge nouvelle n'est identifiée : seuil et régime de la commission restent inchangés, sans rapport, registre de risques ou formation supplémentaire imposé par le présent maintien.",
)

r = base(
    "L2316-19",
    "Coordination nécessaire du renvoi à la commission des marchés, sans changement stylistique gratuit. La source vise le sous-paragraphe 5 du paragraphe 3 de la sous-section 6, emplacement qui ne correspond plus à la commission dans le corpus courant. Les quatre dispositions utiles se trouvent désormais au paragraphe 1er bis de cette sous-section. Le renvoi à la sous-section 9 sur les comptes reste entier, avec ses simplifications et dérogations ; aucun nouvel état comptable ni seconde commission n'est créé.",
    "L2315-44-1 à L2315-44-4 et L2315-64 à L2315-77 lus intégralement. Le corpus ne contient plus L2315-57 à L2315-60 ; le renvoi hiérarchique source est donc incohérent et sa correction est explicite. La nouvelle cible préserve seuils, rôle de choix des fournisseurs et règles de comptes, y compris les dérogations de L2315-64 II et L2315-65. D2316-4 vise encore L2315-57 : correction réglementaire à prévoir vers la commission actuelle, sans changer les seuils ou ressources cumulées. D2316-5/6 restent à leur champ. Vérifier la concordance historique de la recodification pour confirmer la continuité, sans présumer une extension à une commission nouvelle.",
    impact(
        "coordination_only",
        "La source entière comporte deux renvois : celui aux comptes est conservé ; celui à un emplacement disparu de la commission des marchés est remplacé par son emplacement actuel. La correction permet une application lisible au CSE central sans compter une nouvelle réduction d'obligation.",
        "Le règlement D2316-4 conserve un renvoi obsolète hors lot. La filiation exacte de la recodification doit encore être consolidée ; aucune simplification des obligations comptables ou de marchés ni extension de leurs seuils n'est revendiquée.",
        "Aucune charge nouvelle autonome n'est identifiée : aucun registre, rapport, seuil ou commission supplémentaire n'est rédigé. La clarification rend explicite l'application de règles de marchés déjà visées par la source ; leur continuité historique et l'effet pratique du renvoi défectueux restent à contrôler, sans solde net présumé.",
        [effect(
            "coordination", "cse-central-comptes-commission-marches-renvoi",
            "Correction explicite de l'emplacement de la commission des marchés dans le renvoi du CSE central.",
            "Application de la sous-section comptable et renvoi à un sous-paragraphe de commission ne correspondant plus à l'emplacement actuel.",
            "Même sous-section comptable et renvoi au paragraphe 1er bis contenant les quatre articles de commission des marchés, sans nouveau seuil.",
            "other", "CSE centraux relevant des règles de comptes et, aux seuils applicables, de commission des marchés.",
            "Coordination de la loi portant la présente rédaction ; aucune remise en cause de décisions ou comptes antérieurs n'est édictée.",
            "Aucun organe ou rapport nouveau ; renvoi réglementaire D2316-4 à coordonner séparément.",
            "le sous-paragraphe 5 du paragraphe 3 de la sous-section 6 de la même section 3",
            "le paragraphe 1er bis de la sous-section 6 de la même section 3",
        )],
    ),
)
r.update(
    status="rewrite_draft",
    proposed_xml="<p>La sous-section 9 de la section 3 du chapitre V du présent titre et le paragraphe 1er bis de la sous-section 6 de la même section 3 sont applicables au comité social et économique central dans des conditions déterminées par décret.</p>",
)

retained(
    "L2316-20",
    "Maintien intégral des attributions du CSE d'établissement dans la limite des pouvoirs de son chef, et de sa consultation sur les adaptations locales qui relèvent effectivement de celui-ci. Le premier alinéa évite de recopier tout le régime d'entreprise. Le second ne reproduit pas une consultation centrale à l'identique : il vise les mesures spécifiques à l'établissement, indispensables à la représentation des salariés directement concernés.",
    "L2316-1/2 et L2316-22 lus : compétence centrale pour la marche générale et les mesures communes, compétence locale pour les adaptations spécifiques, articulation par accord ou délais supplétifs. Ne pas lire « mêmes attributions » comme un rétablissement des obligations spéciales déjà supprimées dans leurs articles propres, notamment le bilan social. Le contrat unique ne supprime pas ces consultations collectives.",
    "La source entière délimite les compétences centrale et locale et conserve une consultation sur des décisions locales distinctes. Aucun dépôt, agrément, délai minimal ou prélèvement accessoire dissociable n'y est institué ; le maintien évite une suppression de représentation au niveau compétent.",
    "Aucune consultation entière n'est déclarée fusionnée ou supprimée. Les avis communs ou calendriers coordonnés restent possibles dans leurs règles propres, sans disparition des adaptations locales.",
    "Aucune charge nouvelle n'est identifiée : compétence et consultation locales restent identiques, sans rapport de liaison ou seconde transmission supplémentaire créée par cet article.",
)

retained(
    "L2316-21",
    "Maintien intégral de la faculté d'expertise du CSE d'établissement lorsqu'il est compétent. C'est un moyen d'exercer effectivement ses attributions, non une autorisation administrative ni une expertise automatique à chaque consultation. Le critère de compétence et la désignation centrale pour les projets centraux limitent déjà les doubles interventions sans priver les salariés d'une analyse utile.",
    "L2316-3 et la sous-section 10 du chapitre V identifiée ; L2315-80/81/85 lus pour les financements et délais. L'article maintient le seul renvoi à cette sous-section et n'en modifie ni les cas d'expertise ni la répartition 20 %/80 % ou les prises en charge intégrales dans leurs champs propres. Aucun accord ou droit plus favorable n'est fermé pour les futures expertises éligibles.",
    "La source entière ouvre une faculté conditionnée à la compétence légale de l'établissement. Son retrait supprimerait un soutien à l'information et aux recours plutôt qu'un doublon imposé ; aucun gain de prélèvement ou de démarche n'est démontré par une telle suppression.",
    "Les conditions et coûts des différentes expertises gardent leurs articles propres ; ce maintien ne valide pas chaque expertise particulière et ne prétend pas auditer toute la sous-section 10.",
    "Aucune charge nouvelle n'est identifiée : pas d'expertise automatique, de registre, de justificatif ou de délai ajouté. Les règles antérieures de financement et de contestation restent seules applicables.",
)

retained(
    "L2316-22",
    "Maintien intégral de la possibilité d'organiser par accord l'ordre et les délais des avis central et locaux. À défaut d'accord, la transmission des avis d'établissement au comité central permet de prendre en compte les adaptations spécifiques, au lieu de deux consultations sans liaison. Il n'existe ici ni envoi administratif externe ni rapport annuel supplémentaire à supprimer ; les deux niveaux ne sont consultés ensemble que lorsqu'ils sont compétents.",
    "L2316-1/20 et R2312-6 lus. À défaut d'accord : délais centraux d'un mois, deux avec expertise ou trois pour expertise aux deux niveaux dans les cas du règlement ; avis local transmis au plus tard sept jours avant l'échéance centrale, avec effet négatif à défaut. Conserver la compétence du décret en Conseil d'État et l'option d'accord. La réduction de l'ordre du jour de L2316-17 ne modifie pas ces délais d'avis.",
    "La source entière offre une coordination conventionnelle et un calendrier supplétif, sans imposer d'accord ni une seconde validation publique. Les avis locaux et leur circulation ont une fonction d'information essentielle qui ne disparaît pas avec la suppression des rapports accessoires.",
    "Aucun délai de consultation sur le fond n'est réduit dans cet article. Ni toutes les consultations d'établissement ni les consultations centrales ne sont réputées doublonnées ; leur compétence s'apprécie projet par projet.",
    "Aucune charge nouvelle n'est identifiée : avis, transmission interne et faculté d'accord sont maintenus à l'identique, sans nouveau protocole, copie, accusé ou donnée à produire.",
)

reduced(
    "L2316-23",
    "<p>Les comités sociaux et économiques d'établissement assurent et contrôlent la gestion de toutes les activités sociales et culturelles.</p>"
    "<p>Toutefois, les comités sociaux et économiques d'établissement peuvent confier au comité social et économique central la gestion d'activités communes.</p>"
    "<p>Un accord entre l'employeur et une ou plusieurs organisations syndicales de salariés représentatives dans l'entreprise, conclu dans les conditions prévues au premier alinéa de l'article L. 2232-12, peut définir les compétences respectives du comité social et économique central et des comités sociaux et économiques d'établissement.</p>"
    "<p>En cas de transfert au comité social et économique central de la gestion d'activités sociales et culturelles en application du présent article, ce transfert fait l'objet d'une convention entre les comités sociaux et économiques d'établissement et le comité social et économique central. Cette convention n'est soumise à aucune clause type obligatoire. Les parties en déterminent le contenu dans le respect des droits des bénéficiaires et des règles applicables à la gestion et au contrôle des fonds.</p>"
    "<p>La suppression des clauses types obligatoires s'applique aux conventions conclues ou révisées à compter de l'entrée en vigueur de la loi portant la présente rédaction. Les conventions antérieures et les droits des bénéficiaires conservent leurs effets ; aucune révision ni nouvelle convention n'est exigée du seul fait de cette suppression.</p>",
    "Réforme de fond : supprimer les clauses types imposées par décret à toute convention de transfert d'activités sociales et culturelles. D2316-7 exige notamment des ventilations annuelles du financement et des moyens, avec deux rubriques de financement qui se recouvrent ; aucune nécessité d'un canevas réglementaire uniforme n'est démontrée. La convention de transfert reste nécessaire pour des personnes morales et des fonds distincts, mais ses clauses sont librement convenues. Gestion locale, faculté de mutualisation, accord syndical majoritaire, avantages sociaux des salariés et contrôle des fonds sont conservés ; aucune déclaration de remplacement n'est ajoutée.",
    "L2232-12, L2315-62, L2316-19 et D2316-7 lus. Conserver le renvoi au seul premier alinéa de L2232-12 : plus de 50 % des suffrages exprimés en faveur des organisations représentatives, non substitution de la voie minoritaire avec référendum. D2316-7 doit être abrogé ou rendu facultatif pour les conventions nouvelles ou révisées afin de ne pas réimposer ses sept rubriques et ventilations annuelles. Les clauses déjà convenues restent opposables ; la coupe n'autorise ni détournement des fonds ni exclusion des bénéficiaires et ne crée aucun droit de remboursement général. L2315-62 sur le budget de fonctionnement reste distinct du transfert d'activités sociales.",
    ["L'obligation de conformer les conventions de transfert d'activités sociales et culturelles à des clauses types réglementaires, avec leurs rubriques et ventilations annuelles imposées, est supprimée."],
    impact(
        "material_reduction",
        "Par rapport à la source entière, seule l'obligation de clauses types est retirée. Les trois premiers alinéas, le transfert conventionnel volontaire et la gestion des activités sociales restent entiers. La réduction porte sur le contenu réglementaire imposé à la convention, non sur la disparition de la convention ou des droits sociaux qu'elle organise.",
        "Les clauses existantes et les règles de gestion des fonds restent opposables. D2316-7 demande une coordination réglementaire hors lot ; aucune activité, subvention, avantage social ou économie nationale n'est déclaré supprimé, et le coût de rédaction libre n'est pas mesuré.",
        "Aucune charge nouvelle n'est identifiée : la convention et le contrôle des fonds existaient déjà, sans agrément, déclaration, bilan annuel ou nouveau registre de remplacement. Le rappel des droits des bénéficiaires ne conditionne pas leur maintien à une démarche nouvelle.",
        [effect(
            "obligation_removed", "cse-activites-sociales-fin-clauses-types",
            "Suppression du contenu conventionnel imposé par clauses types pour les transferts volontaires d'activités communes.",
            "Chaque transfert entre comités doit faire l'objet d'une convention comportant des clauses conformes aux clauses types réglementaires.",
            "La convention entre comités reste requise ; son contenu est librement déterminé sous les règles des droits des bénéficiaires et de gestion des fonds, sans clause type obligatoire.",
            "legal_duty", "CSE d'établissement et CSE centraux organisant le transfert volontaire d'activités sociales et culturelles.",
            "Conventions conclues ou révisées dès entrée en vigueur ; conventions antérieures et droits des bénéficiaires maintenus, sans révision forcée.",
            "Même convention, sans canevas, autorisation ou déclaration de remplacement ; contrôles et engagements valables conservés.",
            "Cette convention comporte des clauses conformes à des clauses types déterminées par décret.",
            "Cette convention n'est soumise à aucune clause type obligatoire.",
        )],
    ),
)

retained(
    "L2316-24",
    "Maintien intégral de la composition des CSE d'établissement par renvoi à la composition de droit commun. Ce renvoi évite un second système électoral matériellement distinct et conserve les titulaires, suppléants, représentants syndicaux et intervenants de santé et sécurité. Il ne prescrit ni nouveau dépôt ni agrément ; supprimer cette règle ferait perdre des garanties de représentation sans démontrer une charge accessoire supprimable.",
    "L2314-1 à L2314-3 lus : égalité du nombre de titulaires et suppléants, présence du suppléant en l'absence du titulaire, possibilités conventionnelles, référent contre le harcèlement, représentation syndicale et participants consultatifs de santé et sécurité restent à leur champ propre. Les invitations particulières après accident ou maladie et les notes historiques de 2018/2021 des cibles ne sont pas réécrites ni effacées par ce maintien.",
    "La source entière harmonise la composition de l'établissement avec le régime général, sans créer un effectif distinct ni une instance supplémentaire. La représentation et les fonctions de prévention justifient son maintien intégral plutôt qu'une suppression des sièges.",
    "Aucun nombre de sièges ni crédit d'heures n'est réduit ici. Les options conventionnelles du régime général restent ouvertes ; leur effet dans chaque établissement n'est pas chiffré.",
    "Aucune charge nouvelle n'est identifiée : le même renvoi reste applicable, sans nomination, registre, transmission ou condition d'éligibilité supplémentaire.",
)

retained(
    "L2316-25",
    "Maintien intégral de la personnalité civile des CSE d'établissement dans les entreprises d'au moins cinquante salariés. Elle permet de détenir et gérer leurs fonds, de conclure les conventions utiles et de défendre leurs droits. Il s'agit d'une capacité attribuée par la loi, sans immatriculation ou agrément imposé par cet article ; la supprimer compromettrait les droits sociaux et les recours au lieu de retirer une formalité.",
    "Conserver le seuil de cinquante salariés apprécié au niveau de l'entreprise, et non le substituer à un seuil d'établissement. Coordination avec L2316-23 pour les conventions entre personnes morales et L2316-26 pour le fonctionnement. Le texte ne crée pas de nouveau régime fiscal ni de prélèvement sur les activités sociales.",
    "La source entière attribue une capacité juridique au seuil de cinquante salariés de l'entreprise. Aucun paiement, enregistrement ou autorisation conditionnant cette attribution n'y figure ; le maintien protège la gestion autonome et l'accès au juge.",
    "La capacité n'est ni étendue sous le seuil ni retirée aux établissements éligibles. Aucune économie de fonctionnement ou suppression de comptabilité n'est revendiquée.",
    "Aucune charge nouvelle n'est identifiée : l'attribution légale et son seuil restent identiques, sans nouveau dossier, renouvellement d'agrément ou registre.",
)

retained(
    "L2316-26",
    "Maintien intégral du renvoi aux règles de fonctionnement des CSE d'entreprise. Il évite de recopier un régime complet et assure aux élus d'établissement les mêmes garanties de réunion, rémunération, moyens et contrôle des fonds. Ce renvoi général applique les dispositions dans leur état coordonné ; il n'a pas pour effet de ressusciter leurs obligations supprimées. Aucun doublon documentaire particulier n'est institué par cet article.",
    "L2315-1, L2315-4 officiel et proposé, L2315-11, L2315-24 et les règles de comptes pertinentes lus. La suppression proposée du plafond de visioconférences à L2315-4 bénéficie dans son champ aux établissements ; ce simple renvoi n'est pas une nouvelle réduction. Le régime spécial du CSE central et les assouplissements de L2316-14/15 ne sont pas étendus aux établissements par cet article. Les procédures collectives et protections restent distinctes de la rupture individuelle.",
    "La source entière unifie par renvoi le fonctionnement de l'établissement et celui de l'entreprise. Aucun dépôt ou rapport autonome ne peut être retranché de cette phrase sans viser son véritable article d'origine ; aucun gain supplémentaire n'est donc attribué à son maintien.",
    "Ce maintien n'est pas un audit exhaustif de toutes les obligations du chapitre V. Les coordinations matérielles sont à porter dans leurs articles propres ; le renvoi ne rétablit aucune version abrogée.",
    "Aucune charge nouvelle n'est identifiée : même règle de renvoi, sans seconde instance, registre, condition ou délai créé. Les effets des réformes du régime général ne sont pas comptés une seconde fois ici.",
)

retained(
    "L2317-1",
    "Maintien intégral de la protection pénale de la constitution des CSE, de la libre désignation de leurs membres et de leur fonctionnement régulier. L'entrave à la constitution ou à la désignation demeure passible d'un an d'emprisonnement et de 7 500 euros d'amende ; l'entrave au fonctionnement, de 7 500 euros d'amende. Ces garanties protègent l'exercice effectif des libertés collectives et ne sont pas un prélèvement périodique sur l'activité. Leur suppression n'est pas justifiée par celle des formalités accessoires.",
    "L2314-1 à L2314-9 lus, avec les propositions de simplification de L2314-5/9 : le renvoi porte sur les obligations encore applicables dans leur champ temporel, non sur leurs anciennes modalités supprimées. Le délit général n'est pas une base pour rétablir le seul bilan social supprimé à L2312-28. L'abrogation spécifique de L2317-2 n'abolit pas les atteintes distinctes à une consultation toujours due. Préserver les deux niveaux de sanction et les règles générales d'application de la loi pénale plus douce sans les confondre avec des taxes.",
    "La source entière protège la liberté électorale et le fonctionnement des représentants par deux sanctions distinctes. Le maintien conserve une protection essentielle et n'introduit ni paiement automatique ni formalité indépendante ; aucune amende n'est déclarée supprimée ici.",
    "Les infractions supposent leurs éléments légaux et ne couvrent pas des obligations matériellement abrogées pour la période considérée. Le présent maintien ne valide aucune poursuite individuelle ni toutes les anciennes formalités électorales.",
    "Aucune charge nouvelle n'est identifiée : mêmes incriminations, peines et renvois aux obligations applicables, sans registre, attestation de conformité ou sanction supplémentaire.",
)

r = base(
    "L2317-2",
    "Abrogation intégrale de l'incrimination spéciale du défaut annuel de bilan social : coordination nécessaire de la suppression déjà proposée de ce bilan à L2312-28 et suivants. Le renvoi source à L2312-14 est en outre inexact, cet article régissant la consultation préalable générale et non le bilan. Le corriger vers un bilan désormais supprimé maintiendrait une contrainte incohérente. L'abrogation ne supprime ni les informations et consultations sociales autonomes, ni l'entrave distincte à des droits encore applicables, ni les droits des victimes.",
    "L2312-14/19/28, sa proposition d'abrogation et les coordinations de L2312-29 à L2312-35 identifiées dans le corpus ; L2317-1 lu. Même mesure cse-suppression-bilan-social-obligatoire : l'amende spéciale de 7 500 euros n'est ni une taxe supplémentaire supprimée ni un second bilan supprimé. La transition pénale ne maintient pas les poursuites anciennes contrairement à la loi plus douce : articles 112-1 et 112-4 du code pénal à appliquer selon leurs conditions. Leur texte intégral n'est pas joint au lot ; aucune validation de chaque condamnation ou rétroactivité générale de restitution n'est affirmée. Les consultations déjà engagées restent soumises aux obligations transitoires de leurs textes, sans maintien de cette incrimination spéciale abrogée.",
    impact(
        "coordination_only",
        "La source entière ne contient que la sanction pénale spéciale du défaut annuel de bilan social des entreprises ou établissements d'au moins trois cents salariés en l'absence d'accord. Elle est abrogée pour rendre effective la suppression du bilan déjà retenue ; il ne s'agit pas d'une nouvelle baisse de taxe ni d'une seconde obligation de bilan supprimée.",
        "Les obligations d'information et de consultation ayant un fondement autonome et leurs sanctions légalement applicables demeurent. Le traitement des faits antérieurs et peines relève de la loi pénale plus douce, sans remboursement général inventé ni renvoi erroné à L2312-14 conservé.",
        "Aucune charge nouvelle n'est identifiée : aucune déclaration, sanction, garantie, rapport ou accord de remplacement n'est institué. Les droits des victimes et les règles de droit pénal transitoire conservent leur champ propre ; aucun solde global de coût n'est chiffré.",
        [effect(
            "coordination", "cse-suppression-bilan-social-obligatoire",
            "Suppression de la sanction spéciale afin qu'elle ne rétablisse pas le bilan social obligatoire supprimé.",
            "À défaut d'accord de L2312-19, le défaut annuel d'établissement et de soumission du bilan social dans une entreprise ou un établissement d'au moins trois cents salariés est puni de 7 500 euros d'amende.",
            "L'incrimination spéciale est abrogée ; seules les obligations et sanctions autonomes encore applicables conservent leur champ, sous les règles de loi pénale plus douce.",
            "legal_duty", "Personnes susceptibles de poursuite au titre du défaut de bilan social dans les entreprises ou établissements d'au moins trois cents salariés concernés.",
            "Entrée en vigueur de la loi supprimant le bilan ; faits et condamnations antérieurs soumis aux articles 112-1/112-4 du code pénal dans leur champ propre.",
            "Aucune sanction de substitution ni nouveau bilan ; droits autonomes d'information, consultation et réparation préservés.",
            "de ne pas établir et soumettre annuellement au comité social et économique le bilan social d'entreprise ou d'établissement prévu à l'article L. 2312-14 est puni d'une amende de 7 500 €.",
            "Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant le bilan social obligatoire.",
        )],
    ),
)
r.update(
    status="rewrite_draft",
    proposed_xml="<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant le bilan social obligatoire.</p>"
    "<p>Les articles 112-1 et 112-4 du code pénal s'appliquent dans leur champ propre aux faits antérieurs et aux condamnations déjà prononcées. La présente abrogation ne remet pas en cause les droits des victimes à réparation.</p>"
    "<p>Les obligations d'information et de consultation ayant un fondement autonome demeurent applicables, ainsi que les sanctions légalement attachées à leur méconnaissance. Le seul défaut d'un bilan social dont l'établissement n'est plus exigé ne peut être sanctionné sur le fondement de ces dispositions.</p>",
    change_type="full_repeal",
    repeal_policy_id="editorial_direction_2026_10_19",
    repeal_scope="Suppression intégrale de l'incrimination spéciale et de l'amende de 7 500 euros pour défaut annuel d'établissement et de soumission du bilan social dans les entreprises ou établissements d'au moins trois cents salariés visés, avec application de la loi pénale plus douce aux faits et peines antérieurs dans son champ propre.",
)

retained(
    "L2321-1",
    "Maintien intégral du conseil d'entreprise comme instance réunissant les attributions du CSE et la compétence de négocier, conclure et réviser les accords d'entreprise ou d'établissement. Ce régime est facultatif selon L2321-2 ; il constitue déjà une possibilité de regroupement plutôt qu'une nouvelle institution imposée à toutes les entreprises. Retirer son pouvoir de négocier ferait perdre l'objet de cette option sans supprimer une formalité accessoire.",
    "L2321-2 et L2321-4 à L2321-10 lus : institution conventionnelle, heures, rémunération, frais, composition, périodicité et majorités propres restent applicables. Le renvoi au chapitre II porte sur ses règles dans leur état réformé, sans ressusciter le bilan social supprimé ; celui au chapitre V conserve les garanties de fonctionnement. Ne pas confondre la compétence exclusive du conseil avec une dispense des conditions majoritaires de L2321-9.",
    "La source entière prévoit une faculté de réunion de fonctions qui n'est pas instituée automatiquement. Son maintien conserve cette option, mais ne peut être compté comme une nouvelle fusion de régimes ou une économie de charges réalisée par le présent lot.",
    "Aucun conseil n'est imposé ou créé par ce maintien ; aucun coût net ni réduction du nombre de négociations n'est démontré. Les majorités et moyens des élus relèvent des articles distincts conservés.",
    "Aucune charge nouvelle n'est identifiée : mêmes compétences et renvois, sans négociation, réunion, rapport, registre ou approbation supplémentaire exigé par cet article.",
)

retained(
    "L2321-2",
    "Maintien intégral des voies facultatives d'institution du conseil d'entreprise : accord d'entreprise majoritaire ou accord de branche étendu pour les seules entreprises sans délégué syndical. La durée indéterminée de l'accord assure la continuité de la représentation ; ce n'est pas la durée d'un emploi ou d'une aide. La précision de la négociation au niveau des établissements prévient des conflits de compétence. Supprimer la majorité ou rendre la branche disponible malgré un délégué syndical affaiblirait le consentement sans retirer de doublon administratif démontré.",
    "Premier alinéa de L2232-12 officiel et proposé lu : plus de 50 % des suffrages exprimés en faveur des organisations représentatives, et non extension de la voie minoritaire à plus de 30 % avec consultation. L2321-9/10 lus pour les accords conclus par le conseil et l'unité économique et sociale. Conserver la durée indéterminée et les deux phrases du premier alinéa ; ni nouveau CDD ni fin automatique d'emploi n'en découle. Aucun agrément public supplémentaire n'est imposé par cet article.",
    "La source entière laisse le conseil facultatif, avec un consentement majoritaire et une voie de branche limitée aux entreprises sans délégué syndical. Ces conditions fondent la légitimité d'une instance ayant une compétence exclusive de négociation ; leur maintien ne crée pas une charge générale nouvelle.",
    "L'extension de branche reste à son régime propre et n'est pas supprimée dans ce lot. Aucun accord existant n'est annulé, aucune nouvelle possibilité de mandat à durée déterminée n'est créée et aucune économie nationale n'est établie.",
    "Aucune charge nouvelle n'est identifiée : mêmes voies d'accord et contenu sur les établissements, sans autorisation, déclaration de constitution ou pièce supplémentaire ajoutée.",
)

retained(
    "L2321-3",
    "Maintien intégral de l'accord définissant les thèmes soumis à l'avis conforme du conseil d'entreprise, avec la formation professionnelle obligatoirement incluse. Cet avis relève de la participation collective dans une instance volontairement instituée, non d'un agrément administratif ni d'un second dossier de formation. Il constitue une garantie de consentement utile face à la compétence exclusive de négociation du conseil ; aucune duplication documentaire autonome ne justifie sa suppression.",
    "L2321-1/2 et L2321-4 à L2321-9 lus. Préserver le caractère illustratif de l'égalité professionnelle et le caractère obligatoire de la formation, sans transformer toute la liste en thèmes obligatoires supplémentaires. Le texte ne limite pas l'emploi à la durée d'une formation et ne ferme ni aides, dispenses ni droits à formation pour les contrats uniques futurs éligibles. Les accords valables instituant le conseil restent à leur régime propre.",
    "La source entière impose seulement l'inclusion de la formation parmi les thèmes d'avis conforme d'un conseil institué conventionnellement ; elle laisse les autres thèmes à l'accord. Ce pouvoir protège la participation et n'est pas un dossier administratif de formation à retirer.",
    "Aucun thème d'avis conforme ni droit à formation n'est supprimé ou élargi. Les obligations de formation de l'employeur et les modalités de financement relèvent d'autres dispositions, sans chiffrage ou exonération nouvelle.",
    "Aucune charge nouvelle n'est identifiée : maintien de la liste conventionnelle et du seul thème légal obligatoire, sans rapport, justificatif, registre, calendrier ou nouvelle condition d'aide.",
)

assert set(answers) == set(by_number)
result = [answers[a["number"]] for a in sources]
Path("answer.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({
    "articles": len(result),
    "rewrite_draft": sum(a["status"] == "rewrite_draft" for a in result),
    "retained_unchanged": sum(a["status"] == "retained_unchanged" for a in result),
}, ensure_ascii=False))
