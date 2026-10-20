import json
import re
from html import unescape
from html.parser import HTMLParser
from pathlib import Path


class TextOnly(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def plain(xml):
    parser = TextOnly()
    parser.feed(xml or "")
    return "".join(parser.parts)


def paras(*texts):
    return "\n".join("<p>" + text + "</p>" for text in texts)


sources = json.loads(Path("source.json").read_text())
refs = json.loads(Path("reference-targets.json").read_text())
answer = []
for source in sources:
    answer.append({key: source[key] for key in ("code_id", "source_id", "source_sha256", "number")})


def complete(index, xml, reason, review_notes, removed, assessment, limitations, burdens, classification="material_reduction"):
    item = answer[index]
    item.update(
        proposed_xml=xml,
        reason=reason,
        review_notes=review_notes,
        status="rewrite_draft",
        change_type="normative_reduction",
        reform_policy_id="editorial_direction_2026_10_19",
        removed_provisions=removed,
        reference_checks=[],
        substantive_impact={
            "version": 1,
            "classification": classification,
            "assessment": assessment,
            "scope_limitations": limitations,
            "new_burdens_review": burdens,
            "effects": [],
        },
    )


def effect(index, kind, measure_id, description, before, after, unit, population, transition, burdens, source_quote, proposed_quote):
    assert len(source_quote) >= 12 and source_quote in plain(sources[index]["source_xml"]), (index, source_quote)
    assert len(proposed_quote) >= 12 and proposed_quote in plain(answer[index]["proposed_xml"]), (index, proposed_quote)
    answer[index]["substantive_impact"]["effects"].append({
        "kind": kind,
        "measure_id": measure_id,
        "description": description,
        "before": before,
        "after": after,
        "unit": unit,
        "affected_population": population,
        "conditions_and_transition": transition,
        "replacement_or_new_burdens": burdens,
        "source_quote": source_quote,
        "proposed_quote": proposed_quote,
    })


# L353-15 : conserver littéralement les parties utiles de la source officielle.
xml = sources[0]["source_xml"].strip()
xml = xml.replace(
    "après accord du maire et des garants des prêts ayant servi à construire ces logements, à les acquérir ou à les améliorer.",
    "après accord des garants des prêts ayant servi à construire ces logements, à les acquérir ou à les améliorer. Aucun accord distinct du maire n'est requis au titre du présent VI.",
)
xml = xml.replace(
    "les logements faisant l'objet de l'autorisation sont exclus de la convention par avenant.",
    "les logements faisant l'objet de l'autorisation en sont exclus de plein droit à la date de départ du dernier locataire, sans avenant ni demande de résiliation ou d'exclusion. Cette exclusion laisse subsister les effets de la convention pour les autres logements.",
)
xml = xml.replace(
    "à l'exception des conditions d'ancienneté, d'habitabilité et de performance énergétique prévues à l'article L. 443-7 lorsque le logement conserve un usage d'habitation.",
    "à l'exception des conditions d'habitabilité et de performance énergétique prévues à l'article L. 443-7 lorsque le logement conserve un usage d'habitation. Aucune condition d'ancienneté de construction ou d'acquisition n'est exigée pour cette aliénation.",
)
xml = xml.replace(
    "VII.-Le VI du présent article ne s'applique pas aux immeubles situés dans une commune mentionnée aux I ou II de l'article L. 302-5.",
    "VII.-Le VI s'applique sans condition tenant au taux communal de logements sociaux. Les dispositions transitoires du V de l'article L. 302-5 s'appliquent.",
)
xml += "\n" + paras(
    "VIII.-La suppression de l'accord distinct du maire, de l'avenant d'exclusion et de la condition d'ancienneté prévue au VI s'applique aux autorisations de vente ou de changement d'usage résultant de conventions pluriannuelles conclues ou modifiées à compter de l'entrée en vigueur de la présente loi. Elle bénéficie aux demandes en cours, sans nouveau dépôt ni reprise des délais déjà courus. Les conventions et autorisations antérieures conservent leurs effets ; leur modification reste possible selon les règles qui leur sont applicables. Les contrats de prêt, les sûretés, les garanties, les créances légalement nées et les engagements financiers valablement souscrits sont préservés, ainsi que leurs règles de remboursement et leurs recours. Aucun remboursement d'aide ou de prêt n'est écarté par la seule suppression de la condition d'ancienneté. Les droits des occupants et des tiers demeurent protégés ; aucune libération des lieux ni résiliation de bail ne résulte de ces seules suppressions. Les règles d'urbanisme, de sécurité et de salubrité légalement applicables restent distinctes."
)
complete(
    0, xml,
    "Réforme de fond : l'ouverture du VI aux communes anciennement soumises aux quotas SRU est conservée. La présente passe retire en outre l'accord distinct du maire pour une opération déjà définie par convention ANRU, l'avenant obligatoire qui ne faisait que constater l'exclusion des logements après le départ du dernier locataire, et le délai d'ancienneté de construction ou d'acquisition repris de L443-7. Le financement et la protection des occupants ne reposent pas sur ces trois répétitions : l'accord des garants, les prêts et remboursements, le conventionnement jusqu'au dernier départ, les conditions d'habitabilité et d'énergie et le relogement subsistent. Les I à V sont maintenus dans leur texte officiel ; les autres éléments du VI restent à droit constant. Il n'est supprimé aucun impôt ni aucune aide par cet article.",
    "Lecture intégrale de la source, du brouillon et de SRU180 : ce dernier modifiait notamment l'exclusion de l'article11 de la loi1948 et la démolition-relogement, sans établir l'origine SRU de tous les ajouts actuels, notamment du VI. Les I à V sont reproduits sans déplacement. Trois offres, six mois après notification de la troisième offre, logement spécialement conçu, plus de cinq logements, date du13novembre1982, bonne foi et besoins/possibilités sont conservés. L'ambiguïté préexistante du III subsiste entre la dispense de trois offres pour un logement spécialement conçu et le point de départ du délai attaché à la troisième offre ; aucune nouvelle procédure de notification n'est inventée. Le VI garde la dérogation à L443-7 à L443-12-1, le prix fixé par le propriétaire et les conditions d'habitabilité et d'énergie. L443-7, lu en entier avec ses notes, exige normalement une construction ou acquisition depuis plus de dix ans ; cette seule ancienneté est écartée dans le VI. L443-8, lu, conserve sa dérogation autonome pour les autres ventes ; elle n'est pas fermée. L443-15-1, lu, et ses accords propres à la démolition ne sont pas modifiés : la suppression du maire au VI ne les atteint pas. L353-14 et L831-1 ont été lus pour le champ des logements. Le V proposé de L302-5 a été lu comme proposition, sans l'assimiler au droit en vigueur ; la transition SRU et ses droits anciens sont conservés. Coordonner les conventions types et actes ANRU qui exigeraient encore un accord du maire, un avenant ou l'ancienneté sur le seul fondement du VI ; ces documents hors lot ne sont pas réécrits ici. Les stipulations financières autonomes demeurent. Pas d'achèvement affirmé du volet SRU180 ni des209articles.",
    [
        "Accord distinct du maire pour la vente ou le changement d'usage déjà défini dans une convention pluriannuelle ANRU.",
        "Avenant obligatoire excluant de la convention APL les logements concernés après le départ du dernier locataire.",
        "Condition minimale d'ancienneté de construction ou d'acquisition issue de L443-7 pour les seules aliénations relevant du VI.",
        "Exclusion des immeubles des communes visées aux anciens I ou II de L302-5, en coordination de la fin des quotas SRU.",
    ],
    "Par rapport à la source officielle entière, trois contraintes propres aux opérations ANRU sont retirées et l'exclusion territoriale du VII cesse. Cette dernière coordonne la mesure SRU générale ; elle n'est pas une nouvelle taxe supprimée. L'ancienneté normalement supérieure à dix ans ne bloque plus ces ventes, sans suppression des exigences de qualité ni des engagements financiers. Aucune économie nationale ou baisse de loyer n'est chiffrée.",
    "Le régime reste limité aux opérations, ensembles de plus de cinq logements et conventions du VI. Les autorisations de démolition, l'urbanisme, les garanties de prêts et les financements autonomes subsistent. Les conventions types hors lot restent à coordonner ; l'ambiguïté du III n'est pas résolue et la filiation de tous les ajouts n'est pas démontrée.",
    "Aucune charge nouvelle n'est identifiée : aucun avis, dépôt, déclaration ou attestation ne remplace les actes supprimés. L'exclusion de plein droit conserve le même événement de départ du dernier locataire ; la transition préserve les contrats et protections existants sans créer de nouvelle collecte de données.",
)
answer[0]["benefit_review"] = (
    "Les avantages possibles sont examinés séparément. Le I conserve le régime dérogatoire de la loi1948 applicable aux occupants de bonne foi et son exclusion de l'article11. Le III conserve la faculté de réaliser l'opération après trois offres conformes, la dispense lorsque le logement est spécialement conçu, le délai protecteur de six mois et l'interdiction de réoccupation avant travaux. Le IV maintient les seules charges récupérables dans les conditions de L442-3 ; le V conserve le régime de réintégration ou d'offre adaptée lié à l'hébergement. Le VI maintient la convention ANRU valant autorisation, le conventionnement et les droits associés jusqu'au départ du dernier locataire, la dérogation aux règles ordinaires de vente L443-7 à L443-12-1 et la fixation du prix par le propriétaire ; l'habitabilité, l'énergie et les garanties financières demeurent. L'autorisation n'est plus subordonnée à l'accord distinct du maire ni à l'ancienneté minimale ; l'exclusion partielle n'exige plus d'avenant. Le VII ouvre ce régime aux futures opérations recevables dans toutes les communes sans quota SRU. Les aides, garanties, droits des occupants, prêts et conventions antérieurs restent protégés par le VIII et la transition SRU. Aucune exonération ni dérogation favorable n'est retirée, aucun impôt de remplacement ni extension fiscale n'est instauré."
)
effect(0, "coordination", "sru-fin-quotas-communaux", "Retrait de l'exclusion territoriale du régime ANRU, en coordination de la mesure SRU commune.",
       "VI inapplicable aux immeubles des communes des I ou II de L302-5, sans taux ni assiette fiscale propres à cet article.",
       "VI ouvert sans condition de taux communal de logements sociaux ; autres conditions du VI maintenues.", "regime", "Organismes propriétaires et occupants des ensembles conventionnés concernés.",
       "Entrée en vigueur de la réforme et transition commune du V proposé de L302-5 ; droits et conventions valables protégés.",
       "Aucun quota, inventaire ni prélèvement de remplacement ; ne pas compter une seconde abolition des quotas.",
       "Le VI du présent article ne s'applique pas aux immeubles situés dans une commune mentionnée aux I ou II de l'article L. 302-5.",
       "Le VI s'applique sans condition tenant au taux communal de logements sociaux.")
effect(0, "authorization_removed", "anru-fin-accord-distinct-maire", "Suppression du veto municipal distinct dans le seul circuit conventionnel du VI.",
       "La convention ANRU ne vaut autorisation qu'après accord du maire et des garants des prêts.",
       "L'accord des garants reste nécessaire ; aucun accord distinct du maire au titre du VI.", "legal_duty", "Bailleurs et opérations ANRU de vente ou changement d'usage d'un ensemble de plus de cinq logements.",
       "Conventions conclues ou modifiées après entrée en vigueur, demandes en cours sans redépôt ; autorisations antérieures préservées.",
       "Aucun avis ou déclaration substitutif ; urbanisme et accords de démolition de L443-15-1 distincts.",
       "La convention vaut autorisation de vente ou de changement d'usage de cet ensemble de logements, après accord du maire et des garants des prêts ayant servi à construire ces logements, à les acquérir ou à les améliorer.",
       "Aucun accord distinct du maire n'est requis au titre du présent VI.")
effect(0, "obligation_removed", "anru-fin-avenant-deconventionnement", "Suppression de l'avenant purement consécutif à la sortie partielle de convention APL.",
       "Pour un ensemble conventionné plus important, exclusion des logements autorisés par avenant après départ du dernier locataire.",
       "Exclusion de plein droit au même événement, sans avenant ni demande ; convention maintenue pour les autres logements.", "legal_duty", "Organismes propriétaires et parties aux conventions APL partiellement concernées.",
       "Champ temporel du VIII ; aucun départ forcé ni fin anticipée des droits APL des occupants.", "Aucun formulaire, notification spéciale ou acte de confirmation de remplacement.",
       "les logements faisant l'objet de l'autorisation sont exclus de la convention par avenant.",
       "les logements faisant l'objet de l'autorisation en sont exclus de plein droit à la date de départ du dernier locataire, sans avenant ni demande de résiliation ou d'exclusion.")
effect(0, "deadline_reduced", "anru-fin-anciennete-minimale", "Suppression du délai minimal d'ancienneté immobilière dans les seules aliénations ANRU du VI.",
       "Renvoi aux conditions d'ancienneté de L443-7 : logements construits ou acquis depuis plus de dix ans, à distinguer de l'ancienneté d'un salarié.",
       "Aucune durée minimale de construction ou d'acquisition pour ces aliénations ; qualité du logement et obligations financières conservées.", "other", "Organismes propriétaires des logements entrant dans une opération du VI.",
       "Conventions conclues ou modifiées à compter de l'entrée en vigueur ; contrats, créances et remboursements antérieurs préservés.",
       "Ni agrément de remplacement ni nouvelle condition d'investissement ; autorisation conventionnelle et garants demeurent.",
       "à l'exception des conditions d'ancienneté, d'habitabilité et de performance énergétique prévues à l'article L. 443-7 lorsque le logement conserve un usage d'habitation.",
       "Aucune condition d'ancienneté de construction ou d'acquisition n'est exigée pour cette aliénation.")


# L353-19-2 : conserver les acquis normatifs du brouillon et lever le plafond de séjour.
xml = sources[1]["previous_draft"]["proposed_xml"]
xml = xml.replace(
    "Ces logements peuvent être sous-loués meublés ou non, pour une durée n'excédant pas six mois.",
    "Ces logements peuvent être sous-loués meublés ou non, à titre temporaire. La durée de la sous-location n'est pas limitée à six mois par le présent article.",
)
xml = xml.replace(
    "les dispositions de la section 2 du chapitre Ier du livre IV et de l'article L. 442-5,",
    "les dispositions de la section 2 du chapitre Ier du titre IV du livre IV et de l'article L. 442-5,",
)
xml = xml.replace(
    "La faculté de sous-louer un logement non meublé s'applique aux contrats de location et de sous-location conclus à compter de l'entrée en vigueur de la loi. Les contrats antérieurs conservent leurs effets ; leurs parties peuvent convenir d'appliquer cette faculté sans remise en cause des droits déjà acquis. Cette faculté ne prolonge ni le contrat principal ni le contrat de sous-location et ne permet pas de dépasser la durée maximale de six mois.",
    "La faculté de sous-louer un logement non meublé et la suppression de la durée maximale légale de six mois s'appliquent aux contrats de location et de sous-location conclus à compter de l'entrée en vigueur de la présente loi. Les contrats antérieurs conservent leurs effets ; leurs parties peuvent convenir d'appliquer ces dispositions, notamment par une prolongation de la sous-location, sans remise en cause des droits déjà acquis et dans les conditions de la loi n° 89-462 du 6 juillet 1989 précitée. Ces dispositions ne prorogent automatiquement ni le contrat principal ni le contrat de sous-location et n'autorisent pas la sous-location au-delà du terme du contrat principal.",
)
xml = xml.replace(
    "Les contrats de travail à durée déterminée valablement conclus avant l'entrée en vigueur de la loi instituant le contrat unique à durée indéterminée, les rémunérations, dépenses et périodes qui s'y rattachent ainsi que les droits et créances nés à leur titre restent soumis aux dispositions antérieures qui leur sont applicables. Le présent article n'autorise pas la conclusion d'un nouveau contrat à durée déterminée.",
    "Les contrats de travail à durée déterminée valablement conclus avant l'entrée en vigueur de la loi instituant le contrat unique à durée indéterminée demeurent soumis, pour leur exécution et leur rupture, aux dispositions transitoires qui leur sont applicables. Leurs rémunérations, droits et créances acquis sont préservés. Cette réserve ne rétablit aucune enquête ni formalité de logement supprimée par le présent article. Le présent article n'autorise ni la conclusion d'un nouveau contrat à durée déterminée ni un nouveau renouvellement de ce contrat à compter de cette entrée en vigueur.",
)
xml = xml.replace(
    "La durée maximale de six mois prévue au présent article est celle de la sous-location ; elle ne fixe aucun terme au contrat de travail.",
    "Le caractère temporaire et la durée du contrat de sous-location ne fixent aucun terme au contrat de travail. La fin de la saison, de la mission ou de la sous-location ne rompt pas automatiquement ce contrat. Le présent article ne modifie ni les règles de notification et de préavis, ni les indemnités, ni les procédures collectives et les protections spéciales applicables à sa rupture.",
)
complete(
    1, xml,
    "Réforme de fond et coordination : les acquis du brouillon sont conservés, à savoir les logements non meublés, la dispense de l'enquête statistique L442-5 et de ses pénalités, le maintien de l'APL et l'accès au logement des salariés sous contrat unique. La coupe supplémentaire retire le maximum légal de six mois de sous-location : il excluait les besoins saisonniers plus longs sans garantir à lui seul la décence ou l'éligibilité. Le caractère temporaire, le bail principal, les ressources, les règles locatives et les protections de la loi1989 restent applicables. Les baux anciens ne sont pas prolongés d'office. Le renvoi au CDD saisonnier est remplacé par sa définition matérielle, sans rouvrir les CDD. Le renvoi APL et l'intitulé incomplet de la section relative au supplément de loyer sont coordonnés ; ces corrections ne sont pas des prélèvements supprimés.",
    "Source, brouillon et texte complet de SRU154 lus. L'avantage de sous-location temporaire provient bien du V de SRU154, alors réservé aux SEM ; la source actuelle vise plus largement les bailleurs autres que les organismes de L353-14 et ajoute le prix du mobilier. Ces fondements actuels ne sont pas éliminés au motif de leur origine. La définition saisonnière reprend uniquement la première branche du3° de L1242-2, pas les emplois d'usage ni son bulletin unique, qui ne conditionnent pas ce logement. Les autres cas des1°,2°,4°,5°,6° ne sont pas importés. L821-1, lu en entier, identifie l'APL en son1° ; la référence source à L351-1 est remplacée, sans nouvelle condition d'aide. La structure et les textes de L441-3 et L441-15, lus avec leurs notes, situent la section2 au chapitreIer du titreIV du livreIV : le titre manquant est ajouté expressément. Le supplément de loyer et ses exonérations restent à leur champ ; aucune suppression générale n'est revendiquée. L442-5, lu en entier, vise une enquête statistique, une réponse sous un mois et 7,62euros puis7,62euros par mois entier de retard, avec exception pour difficultés particulières. La dispense spécifique ne ferme aucune aide et n'efface pas les contrôles de ressources autonomes ; aucune enquête équivalente n'est créée. La loi89-462, article40III, demeure un renvoi externe conservé : son texte intégral n'est pas joint au corpus fourni et sa coordination des durées et des baux temporaires doit être vérifiée hors de ce lot ; aucun contenu supplémentaire ne lui est attribué. La suppression du plafond légal n'efface ni les durées contractuelles ni les préavis locatifs de ce régime. Les dispositions CASF des CCAS restent également à leur champ. Aucune modification des codes extérieurs ni de l'ensemble de SRU154 n'est déclarée achevée.",
    [
        "Obligation de sous-louer exclusivement des logements meublés aux travailleurs saisonniers éligibles.",
        "Enquête et collecte de justificatifs statistiques L442-5 auprès de ces sous-locataires, avec pénalités pour défaut de réponse.",
        "Durée maximale légale de six mois pour ces seules sous-locations de logements conventionnés à des travailleurs saisonniers.",
    ],
    "La comparaison avec la source officielle démontre une extension aux logements non meublés, le retrait de l'enquête L442-5 et de ses accessoires et la levée du plafond légal de six mois. Le contrat unique et les références APL et de structure sont des coordinations. La levée du plafond n'est ni une prolongation forcée du bail ni une abolition de loyers ou de toutes les vérifications de ressources.",
    "Le champ reste celui des logements conventionnés des bailleurs visés, des CCAS ou associations déclarées et des tâches saisonnières définies. Les loyers, le supplément de loyer dans son champ, les ressources et le financement APL restent distincts. La loi1989 et ses règlements nécessitent une vérification externe de concordance ; aucun solde national de coût ou de complexité n'est établi.",
    "Aucune charge nouvelle n'est identifiée pour le locataire ou l'employeur : la définition des tâches reprend le critère saisonnier officiel et n'impose pas de nouvelle attestation. Aucun délai minimal de séjour ou d'emploi, aucune déclaration et aucun financement de remplacement ne sont introduits. L'accord pour modifier un bail existant protège les droits contractuels au lieu d'imposer un nouvel avenant à tous.",
)
effect(1, "coordination", "logement-saisonnier-contrat-unique", "Autonomisation de la définition saisonnière pour conserver l'accès au logement lors de la disparition des nouveaux CDD.",
       "Emploi saisonnier identifié par renvoi au3° de L1242-2 ; le texte source ne pose pas expressément une exigence de CDD.",
       "Tâches répétées selon saisons ou modes de vie collectifs définies dans l'article ; contrat unique explicitement admis sans terme automatique.", "regime", "Travailleurs saisonniers éligibles, y compris nouvelles embauches sous contrat unique et anciens CDD valables.",
       "Anciennes créances et contrats préservés ; aucune conclusion ou reconduction nouvelle de CDD autorisée.",
       "Aucun certificat saisonnier ajouté ; préavis et indemnités du contrat de travail restent hors de la durée du logement.",
       "des travailleurs dont l'emploi présente un caractère saisonnier tel que mentionné au 3° de l'article L. 1242-2 du code du travail.",
       "les tâches de cet emploi étant appelées à se répéter chaque année selon une périodicité à peu près fixe, en fonction du rythme des saisons ou des modes de vie collectifs, y compris lorsque le travailleur est employé sous contrat unique à durée indéterminée.")
effect(1, "relief_extended", "logement-saisonnier-sans-meubles", "Ouverture de la dérogation de sous-location aux logements non meublés.",
       "Sous-location meublée seulement dans le premier alinéa officiel ; majoration de mobilier possible selon L442-8-3-1.",
       "Choix meublé ou non ; majoration de mobilier réservée au logement effectivement meublé, selon les mêmes règles.", "regime", "Bailleurs, CCAS, associations et travailleurs saisonniers des logements conventionnés visés.",
       "Contrats nouveaux à l'entrée en vigueur ; option conventionnelle pour les contrats antérieurs sans perte de droits acquis.",
       "Aucun équipement obligatoire, certificat de mobilier ni dépôt supplémentaire en remplacement.",
       "ayant pour objet de les sous-louer meublés pour une durée n'excédant pas six mois",
       "Ces logements peuvent être sous-loués meublés ou non, à titre temporaire.")
effect(1, "obligation_removed", "logement-saisonnier-fin-enquete-statistique", "Dispense de l'enquête statistique et des pénalités de non-réponse de L442-5 pour ces sous-locataires.",
       "Renvoi source à L442-5 : enquête, justificatifs, un mois pour répondre et pénalité de7,62euros augmentée de7,62euros par mois entier, sous son exception favorable.",
       "Aucune enquête ou collecte sur ce fondement ni pénalité de défaut de réponse ; contrôles autonomes de ressources et d'APL maintenus.", "legal_duty", "Sous-locataires saisonniers visés au premier alinéa et organismes chargés de l'enquête.",
       "Dispense immédiate, y compris enquêtes en cours et anciens baux, sans rattrapage ; sommes antérieures et loi répressive plus douce réservées.",
       "Aucune enquête ou déclaration équivalente ; les seules vérifications autonomes demeurent.",
       "et de l'article L. 442-5 ainsi que celles relatives au niveau de ressources prévues à l'article L. 441-1",
       "aucune enquête ni collecte de pièces ou de données auprès de ces sous-locataires ne peut être exigée sur le fondement de l'article L. 442-5, et les pénalités prévues par cet article pour défaut de réponse ne leur sont pas applicables.")
effect(1, "relief_extended", "logement-saisonnier-fin-plafond-six-mois", "Suppression du maximum légal de séjour qui interdisait une sous-location saisonnière supérieure à six mois.",
       "Durée de la sous-location au plus six mois, sans lien nécessaire avec un préavis d'emploi.",
       "Pas de maximum légal spécial ; sous-location temporaire limitée par son contrat et le terme du bail principal.", "other", "Travailleurs saisonniers dont le besoin de logement dépasse six mois et leurs bailleurs intermédiaires.",
       "Nouveaux baux après entrée en vigueur ; accord des parties pour appliquer la réforme aux baux antérieurs, sans prorogation automatique.",
       "Pas de justification de dépassement, d'autorisation ou de déclaration de prolongation ; règles locatives autonomes conservées.",
       "pour une durée n'excédant pas six mois",
       "La durée de la sous-location n'est pas limitée à six mois par le présent article.")
effect(1, "coordination", "apl-concordance-l821-1", "Correction du renvoi identifiant l'aide personnalisée au logement, sans nouvelle condition d'accès.",
       "Assimilation des sous-locataires aux locataires pour l'APL avec renvoi à L351-1 dans la source.",
       "Même assimilation pour l'APL identifiée au1° de L821-1, lu dans le corpus ; droits et conditions propres conservés.", "regime", "Sous-locataires éligibles à l'APL dans le présent régime.",
       "Droits anciens et futurs éligibles préservés ; pas de nouvelle demande liée à la seule concordance.", "Aucune charge nouvelle ni seconde aide créée.",
       "pour bénéficier de l'aide personnalisée au logement prévue par l'article L. 351-1 du présent code.",
       "pour bénéficier de l'aide personnalisée au logement mentionnée au 1° de l'article L. 821-1 du présent code.")


# L365-1 : la source utile est conservée, sans nouvel habillage stylistique.
answer[2].update(
    proposed_xml=None,
    reason="Maintien intégral nécessaire après examen des charges, avantages, renvois et du brouillon : cet article ne prélève rien et n'impose directement ni agrément, déclaration, justificatif, délai ou renouvellement. Il qualifie les services sociaux de logement pour les personnes et familles en difficulté, locataires ou propriétaires occupants, et conserve leurs trois activités et modes de financement. Le reste à charge strictement inférieur à50% délimite ce régime favorable, sans fixer un nouveau tarif. Les renvois européens encadrent la qualification et les compensations publiques et ne peuvent être effacés par simplification nationale. Le brouillon antérieur n'apportait qu'une reformulation à droit constant ; il n'est pas présenté comme une réduction ou une réécriture de fond.",
    review_notes="Source entière et brouillon lus : maintien des1°,2°,3°, des opérations d'acquisition, construction et réhabilitation, des logements et hébergements, de la qualité de propriétaire et des trois baux, des collectivités publiques, établissements publics et institutions sociales, des décisions, subventions et marchés, ainsi que du seuil inférieur à50%. Le II de L301-1 a été lu : personnes et familles ayant des difficultés particulières d'accès ou de maintien dans un logement décent. Le j du2 de l'article2 de la directive2006/123/CE, la décision2012/21/UE et l'article106§2 du traité demeurent les références de la source ; leurs textes européens ne sont pas joints et aucune vérification externe ou nouvelle conformité n'est affirmée. Agréments nationaux indéfinis des autres articles ne prolongent ni mandat ni financement SIEG. SRU141, lu en entier, portait sur une qualification d'utilité sociale et des agréments ; il ne prouve pas que la rédaction actuelle, donnée en vigueur depuis2014, en découle intégralement. L365-7, lu, conserve le fondement distinct des conventions facultatives des fédérations. Aucune filiation incertaine ni aucun ensemble de209articles n'est déclaré achevé. Aucun renvoi du présent article n'est rendu orphelin par les modifications du lot.",
    status="retained_unchanged",
    classification="retained_necessary",
    reference_checks=[],
    substantive_impact={
        "version": 1,
        "classification": "retained_necessary",
        "assessment": "Aucun changement par rapport à la source officielle entière : la qualification favorable des services, les bénéficiaires, les financements et le cadre européen restent intégraux. Cette disposition ne fournit aucun gain compté au titre de la couverture ou de la simplification.",
        "scope_limitations": "Le maintien ne valide ni la conformité européenne de chaque financement ni le contenu des actes SIEG autonomes. Les agréments et dossiers sont traités par les articles suivants et leurs règlements, sans assimilation à une suppression de prélèvement.",
        "new_burdens_review": "Aucune charge nouvelle n'est identifiée puisque le texte officiel est intégralement maintenu, sans nouveau corps, obligation, registre ou donnée. Le seuil et les références européennes sont existants ; aucune nouvelle attestation n'est ajoutée pour en bénéficier.",
        "effects": [],
    },
)


# L365-2 : garder l'agrément et ses critères, supprimer le circuit régional et sa répétition territoriale.
xml = paras(
    sources[3]["source_xml"],
    "La délivrance ou la modification de cet agrément ne requiert aucun avis du comité régional de l'habitat et de l'hébergement. L'organisme n'a pas à saisir ce comité ni à produire son avis.",
    "Pour les demandes prévues au présent article et aux articles L. 365-3 et L. 365-4, les pièces et renseignements communs sont fournis une seule fois. L'autorité saisie les transmet aux autres autorités compétentes dans le respect des règles de protection et d'accès aux données. Les pièces et renseignements exacts et à jour que l'administration détient déjà légalement ou auxquels elle a légalement accès ne peuvent être exigés à nouveau.",
    "L'agrément est délivré sans limitation de durée et vaut sur l'ensemble du territoire national pour les activités qu'il couvre. L'extension territoriale de ces activités n'est soumise ni à une nouvelle demande d'agrément ni à une autorisation ou à une déclaration d'extension. Aucun renouvellement ni aucune confirmation périodique ne peuvent être exigés à ce titre. Les capacités financières, la compétence et le caractère désintéressé de la gestion prévus au premier alinéa restent exigés ; les contrôles légaux demeurent applicables. Les actes confiant une mission de service public ou accordant son financement conservent leurs propres champs, durées et conditions.",
    "Les deuxième à quatrième alinéas s'appliquent dès l'entrée en vigueur de la présente loi. Les agréments en cours de validité deviennent de plein droit nationaux pour les activités qu'ils couvrent, sans demande ni formalité ; les demandes d'extension territoriale deviennent sans objet. Les demandes initiales en cours sont poursuivies sans nouveau dépôt ni reprise des délais déjà courus. Les agréments retirés ou déjà caducs ne sont pas rétablis. Les aides accordées, les conventions valablement conclues, les droits des bénéficiaires et les engagements financiers antérieurs conservent leurs effets."
)
complete(
    3, xml,
    "Réforme de fond : conservation de la suppression de l'avis régional et du dépôt unique des pièces communes déjà proposés ; ajout de la portée nationale du seul agrément de maîtrise d'ouvrage, sans demande d'extension, autorisation ou déclaration de remplacement. Le territoire ne constitue pas une capacité autonome alors que chaque opération financée garde ses conditions et que les contrôles des fonds demeurent. L'agrément initial et ses trois critères officiels sont conservés : la maîtrise durable d'un patrimoine social et l'accès aux concours de la CGLLS exigent un contrôle des capacités financières, de la compétence et de la gestion désintéressée. Le premier alinéa reste le texte officiel ; la durée sans limitation existait déjà au règlement et n'est pas comptée comme une nouvelle suppression de renouvellement. Le réemploi des données légalement détenues reprend aussi un droit existant, sans gain CRPA fictif.",
    "Source et brouillon entiers lus. R365-1 à R365-8 ont été lus intégralement avec leurs notes et leurs propositions distinguées du droit officiel. R365-2 prévoit déjà la durée illimitée et trois mois pour décider, mais fixe le territoire ; R365-6-1 exige la demande d'extension au préfet de région du siège. Retirer cette limitation et cette demande dans ces deux articles, puis les références territoriales de R365-5, sans rétablir d'avis régional. R362-2,8°, et R365-5,10°c, restent à coordonner pour supprimer le circuit consultatif ; les coordinations déjà signalées dans coordination.json ne deviennent pas de nouveaux gains. R365-5 prévoit aussi des pièces organiques déjà allégées dans sa proposition : aucun rétablissement ici, aucune seconde coupe comptée. R365-6 et R365-6-1 doivent organiser le dossier commun et son acheminement légal ; la charge du service est explicitée dans le bilan. Les conditions d'aides, les obligations de comptes et le contrôle ANCOLS gardent leur fondement autonome ; les articles L342-2 et L342-14 ne sont pas modifiés par ce lot. L365-5, L411-4 et L452-1 ont été lus entièrement : l'agrément maintient l'accès futur aux concours et aides sans les attribuer automatiquement et conserve les protections locatives autonomes. Les avantages fiscaux liés à la qualité agréée ne sont pas retirés ; leurs articles CGI particuliers ne sont pas réécrits ni réputés contrôlés ici. Les actes de mandat et de compensation gardent leur territoire et leur durée propres malgré l'agrément national. L371-4 et sa note ont été lus : son9° reste une transition de Mayotte au1erjanvier2014/2015 et n'est pas réinitialisé. SRU141 n'établit pas la filiation de chaque condition actuelle. Les fichiers publics hors lot restent inchangés.",
    [
        "Consultation du comité régional, saisine par le demandeur et production de son avis pour délivrer ou modifier l'agrément de maîtrise d'ouvrage.",
        "Limitation territoriale de l'agrément de maîtrise d'ouvrage et nouvelle demande administrative pour l'étendre à un autre territoire.",
        "Dépôts répétés de pièces communes aux trois agréments, dans les limites du droit de réemploi légal déjà applicable.",
    ],
    "L'article conserve l'agrément initial mais retire le circuit régional consultatif et la demande d'extension territoriale de la maîtrise d'ouvrage. Les modalités supprimées sont identifiées dans R365-2, R365-5 et R365-6-1 lus, en application de l'habilitation de la source. La durée illimitée et une partie du réemploi existaient déjà : aucun gain nouveau n'en est compté. Le dossier commun met aussi la circulation des pièces à la charge des autorités ; son solde net reste inconnu, d'où le classement mixed.",
    "Seuls l'agrément du présent article et les dépôts communs des trois agréments sont concernés ; aucune cotisation, carte professionnelle, attribution de financement ou obligation SIEG autonome n'est supprimée. Les coordinations réglementaires territoriales et les conventions de financement hors lot restent nécessaires. Les économies et coûts de service ne sont pas chiffrés.",
    "Le troisième alinéa impose explicitement aux autorités la transmission légale des pièces communes, sans nouveau dépôt privé ; cette organisation peut entraîner un coût de service et est recensée comme charge publique du projet. Son supplément exact au regard des devoirs déjà issus du CRPA n'est pas établi. Aucun registre, agrément, déclaration ou donnée supplémentaire n'est imposé aux organismes en remplacement ; le solde net n'est pas démontré.",
    "mixed",
)
source_initial = plain(sources[3]["source_xml"]).split(" Les critères")[0]
effect(3, "obligation_removed", "agrement-logement-fin-avis-regional", "Retrait de la consultation régionale et de la saisine avec copie d'avis exigées par les modalités réglementaires de l'agrément.",
       "Agrément légal avec modalités par décret ; R365-2 impose l'avis du comité régional et R365-5,10°c, sa saisine et sa copie.",
       "Aucun avis du comité, saisine ni pièce correspondante ; l'autorité décide sur les capacités conservées.", "legal_duty", "Organismes demandant l'agrément de maîtrise d'ouvrage et autorités instructrices.",
       "Demandes nouvelles et en cours à l'entrée en vigueur sans nouveau dépôt ni reprise des délais.", "Ni déclaration ni avis équivalent ; décision initiale et contrôles demeurent.",
       source_initial,
       "La délivrance ou la modification de cet agrément ne requiert aucun avis du comité régional de l'habitat et de l'hébergement.")
effect(3, "authorization_removed", "agrement-maitrise-ouvrage-national", "Suppression des demandes d'extension de l'agrément de maîtrise d'ouvrage par portée nationale de la qualification.",
       "R365-2 fixe le territoire de l'agrément prévu par la source ; R365-6-1 impose une demande pour l'étendre, durée déjà illimitée.",
       "Qualification nationale et durable sans demande, autorisation ni déclaration d'extension ; aucune prolongation automatique de financement.", "legal_duty", "Organismes de maîtrise d'ouvrage agréés ou futurs éligibles, dans les activités de leur agrément.",
       "Conversion automatique des agréments valides ; demandes d'extension sans objet ; agréments caducs ou retirés non rétablis.",
       "Pas de confirmation périodique, registre ou condition de financement nouvelle.",
       source_initial,
       "L'extension territoriale de ces activités n'est soumise ni à une nouvelle demande d'agrément ni à une autorisation ou à une déclaration d'extension.")
effect(3, "coordination", "agrement-logement-pieces-communes", "Inscription du dossier commun et du réemploi des informations légalement disponibles ; gain au-delà du CRPA non établi.",
       "Pièces d'agrément fixées par décret ; R365-5 prévoit leur liste, sous les droits de réemploi déjà applicables.",
       "Pièces communes fournies une fois, réemploi des éléments exacts accessibles et circulation par les autorités compétentes.", "legal_duty", "Organismes présentant des demandes des articles L365-2 à L365-4 et administrations saisies.",
       "Dossiers nouveaux et en cours, sans redépôt ou remise à zéro ; protection légale des données conservée.",
       "Aucune autorisation d'accès aux données créée ; charge d'acheminement du service décrite séparément.",
       source_initial,
       "Pour les demandes prévues au présent article et aux articles L. 365-3 et L. 365-4, les pièces et renseignements communs sont fournis une seule fois.")
effect(3, "obligation_added", "agrement-logement-pieces-communes", "Obligation expresse de circulation interadministrative des pièces, corrélative au dossier commun, sans prétendre établir son supplément au droit général.",
       "L'article officiel prévoit l'agrément et ses critères, sans organiser expressément une transmission entre autorités ; obligations CRPA distinctes réservées.",
       "L'autorité saisie transmet les pièces communes aux autres autorités compétentes dans les limites légales d'accès et de protection.", "legal_duty", "Autorités administratives saisies des demandes d'agrément communes, pas les bénéficiaires des logements.",
       "Demandes nouvelles et en cours dès entrée en vigueur ; aucun accès à une donnée protégée n'est créé.",
       "Coût public possible de circulation ; caractère additionnel exact et solde net non établis, aucun chiffrage de réduction globale.",
       source_initial,
       "L'autorité saisie les transmet aux autres autorités compétentes dans le respect des règles de protection et d'accès aux données.")


# L365-3 et L365-4 : une même simplification de qualification, dans deux champs distincts.
for index, numeral, activity in [
    (4, "2°", "d'ingénierie sociale, financière et technique"),
    (5, "3°", "d'intermédiation locative et de gestion locative sociale"),
]:
    xml = sources[index]["previous_draft"]["proposed_xml"]
    xml = xml.replace(
        "Aucun renouvellement ni aucune confirmation ou déclaration périodique tenant lieu de renouvellement ne sont exigés.",
        "Aucun renouvellement ni aucune confirmation ou déclaration périodique tenant lieu de renouvellement ne sont exigés. La délivrance initiale de l'agrément n'est subordonnée à aucune consultation des préfets de département. L'autorité compétente statue sur les capacités de l'organisme à exercer les activités demandées ; aucune autorisation territoriale supplémentaire ne peut être exigée.",
    )
    number = sources[index]["number"]
    specific = (
        "L'ingénierie comprend l'accueil, les conseils, l'accompagnement social, les démarches DALO, la recherche de logements et la participation aux commissions : les compétences sociales, financières, techniques et juridiques doivent rester contrôlables pour les publics défavorisés."
        if index == 4 else
        "L'intermédiation et la gestion impliquent la prise à bail, la sous-location, la gérance et les résidences sociales, avec des fonds et des droits d'occupants à protéger : la capacité de l'opérateur doit rester contrôlable. La carte professionnelle de la loi70-9 pour la gérance demeure distincte."
    )
    review_specific = (
        "R365-1,2°b, maintient l'assimilation des organismes sociaux qu'il cite ; le2°c conserve l'agrément de plein droit des organismes collecteurs pour l'assistance DALO. Ces dispenses restent ouvertes dans leur champ et ne deviennent pas des dossiers initiaux supplémentaires."
        if index == 4 else
        "Le dernier alinéa de R365-1 maintient l'assimilation des maîtres d'ouvrage pour la gestion de leur propre parc. La carte professionnelle de gérance visée au dernier alinéa de R365-5 et fondée sur la loi70-9, hors des cinq codes, n'est ni assimilée à cet agrément ni supprimée. Les avantages locatifs et fiscaux attachés à la qualité agréée restent ouverts aux futures situations éligibles selon leurs autres conditions, sans financement automatique."
    )
    complete(
        index, xml,
        "Réforme de fond : conservation de la suppression des cinq ans renouvelables et des demandes d'extension territoriale, sans confirmation ou déclaration équivalente. La coupe supplémentaire retire la consultation systématique des préfets départementaux lors de l'instruction initiale régionale : le même examen des capacités aboutit à une qualification nationale, tandis que chaque mission ou financement garde son territoire et ses conditions. L'agrément initial demeure une vérification de compétence distincte de ces circuits répétitifs. " + specific + " Le renvoi au" + numeral + " de L365-1 et les dispenses sont maintenus ; aucun droit à aide ni garantie des personnes n'est retiré. Les parties simplement explicatives du brouillon ne sont pas comptées comme des réductions supplémentaires.",
        "Source, note historique, brouillon et texte complet de SRU141 lus. Le renvoi au" + numeral + " de L365-1 est préservé ; l'origine de toutes les règles actuelles de2009 ne se déduit pas du numéro créé en2000. R365-1 à R365-8, leurs notes et leurs propositions ont été lus en distinguant droit et projet. Coordonner R365-3 et R365-4 sur la durée, R365-5 sur l'absence de dossier de renouvellement et R365-6 sur la portée nationale, la disparition des demandes d'extension et, désormais, des consultations départementales initiales. Une seule mesure de nationalisation du circuit R365-6 s'applique aux deux agréments ; ses deux coordinations ne constituent pas deux suppressions du même circuit. Les autorités compétentes et les trois mois pour statuer sur un dossier complet restent ceux des règles non incompatibles ; les délais déjà courus sont préservés. R365-7 proposé supprime déjà l'envoi annuel : ne pas le rétablir par le suivi de l'agrément, ne pas le compter comme nouvelle coupe ici. Ses contrôles et la notification des modifications statutaires autonomes restent à leur champ. R365-8 conserve les motifs de retrait et le contradictoire. " + review_specific + " Les obligations SIEG demeurent celles de L365-1 et des actes de mandat ; la nationalisation et la durée indéterminée de l'agrément ne les étendent pas. Les demandes initiales utilisent les pièces communes de L365-2 sans nouveau dépôt. Les notes de la loi2009-323, article2IV, conservent leurs dates historiques du1erjanvier2010 et du1erjanvier2011 ; L371-4,9°, lu en entier avec sa note, conserve celles de Mayotte au1erjanvier2014 et au1erjanvier2015. Aucun agrément retiré ou caduc avant réforme n'est rétabli, aucune créance ou convention valable n'est effacée. Les coordinations réglementaires hors lot restent identifiées, pas déclarées réalisées par ce fichier.",
        [
            "Durée de cinq ans de l'agrément et demande de renouvellement périodique, sans confirmation ou déclaration périodique de remplacement.",
            "Demandes et consultations territoriales répétées pour étendre les mêmes activités déjà agréées à d'autres territoires.",
            "Consultation préalable systématique des préfets départementaux dans l'instruction initiale d'une qualification désormais nationale.",
        ],
        "Par rapport à la source entière, l'échéance de cinq ans et le renouvellement sont supprimés. La portée nationale et la fin des circuits territoriaux sont rattachées aux modalités de R365-6, lu ; la consultation départementale initiale disparaît en plus du brouillon. L'agrément initial, les contrôles, les dispenses et les conditions de financement sont conservés. Les mesures communes à L365-3 et L365-4 sont dédupliquées ; aucun montant national d'économie n'est établi.",
        "La réforme vise seulement les activités " + activity + " du" + numeral + " de L365-1 et la portée de leur agrément, pas la durée des contrats, missions, financements ou mandats. Les règlements de procédure restent à coordonner. Les agréments déjà caducs ou retirés ne revivent pas, les engagements financiers antérieurs restent propres.",
        "Aucune charge nouvelle n'est identifiée : l'examen initial des capacités, le contrôle et le retrait sont existants, et aucune déclaration annuelle ou territoriale ne remplace le renouvellement. La conversion des agréments valides est automatique, sans dossier ou notification supplémentaire ; aucune donnée nouvelle n'est demandée au public accompagné.",
    )
    effect(index, "obligation_removed", "agrement-social-fin-renouvellement",
           "Suppression de l'échéance et du renouvellement quinquennal, appliquée aux deux champs d'agrément sans doubler leur économie présumée.",
           "Agrément de cinq ans renouvelable pour les organismes des activités " + activity + ".",
           "Agrément de durée indéterminée, sans renouvellement, confirmation ou déclaration périodique ; retrait et contrôles conservés.", "legal_duty", "Organismes titulaires ou demandeurs de l'agrément " + number + ".",
           "Agrément nouveau ou valide à la bascule ; conversion sans formalité, renouvellements en cours sans objet ; aides et droits anciens protégés.",
           "Aucune attestation de maintien ni nouvelle condition de financement ; qualification et mission financée restent distinctes.",
           "pour une période de cinq ans renouvelable selon des modalités définies par décret en Conseil d'Etat.",
           "Aucun renouvellement ni aucune confirmation ou déclaration périodique tenant lieu de renouvellement ne sont exigés.")
    effect(index, "authorization_removed" if index == 4 else "coordination", "agrement-social-national",
           "Portée nationale de la qualification et retrait du circuit commun d'extension de R365-6 ; application au champ de " + number + ".",
           "Modalités réglementaires de l'agrément : compétence départementale ou régionale, nouvelle demande au préfet de région pour extension avec consultations et caducité de l'ancien titre.",
           "Qualification nationale pour les activités agréées, sans nouvelle demande, consultation d'extension ni déclaration ; financements territoriaux non étendus automatiquement.", "legal_duty", "Organismes " + number + " opérant sur plusieurs territoires.",
           "Conversion des agréments encore valides et extinction des demandes d'extension ; aucun rétablissement d'un titre caduc.",
           "Aucune nouvelle autorisation territoriale ; même mesure R365-6 pour L365-3 et L365-4, pas une seconde suppression du circuit.",
           "selon des modalités définies par décret en Conseil d'Etat.",
           "L'extension territoriale de ces activités n'est soumise ni à une nouvelle demande d'agrément ni à une autorisation ou à une déclaration d'extension.")
    effect(index, "obligation_removed" if index == 4 else "coordination", "agrement-social-fin-avis-prefectoraux",
           "Retrait de la consultation des préfets départementaux lors de la demande initiale ; même circuit partagé par les deux agréments.",
           "La source renvoie aux modalités par décret ; R365-6, deuxième alinéa, impose de consulter chaque préfet départemental pour une demande initiale pluridépartementale régionale.",
           "L'autorité compétente décide directement sur les capacités, sans consultation départementale obligatoire.", "legal_duty", "Services instructeurs et organismes des activités de " + number + ".",
           "Demandes nouvelles et initiales en cours dès la bascule, sans recommencement des délais ni nouveau dossier.",
           "Aucun avis ou visa de remplacement ; contrôles et conditions propres des opérations conservés.",
           "selon des modalités définies par décret en Conseil d'Etat.",
           "La délivrance initiale de l'agrément n'est subordonnée à aucune consultation des préfets de département.")


# L366-1 : maintenir la coupe acquise, sans effacer les protections du réseau.
xml = sources[6]["previous_draft"]["proposed_xml"]
complete(
    6, xml,
    "Réforme de fond acquise conservée après nouvel examen : suppression de l'agrément territorial et de l'avis national préalable, sans nouvelle déclaration, avec assimilation légale des associations au régime agréé. Le second circuit ministériel doublonnait une création déjà à l'initiative conjointe de l'État et des collectivités. Aucune coupe supplémentaire de cet article n'est justifiée : la gratuité, la neutralité et la compétence de l'information, l'absence d'actes administratifs, commerciaux ou contentieux, les statuts types et le contrôle protègent les usagers ; la composition et l'agrément propres de l'association nationale assurent la qualification de l'organisme de coordination, distincte de l'avis territorial déjà retiré. Les variantes territoriales et la dérogation corse restent nécessaires aux futures créations. La conservation des phrases à droit constant du brouillon ne compte pas comme une nouvelle simplification.",
    "Source, brouillon et SRU201 lus entièrement. SRU a créé le socle départemental, mais non toutes les variantes actuelles ; les initiatives conjointe, interdépartementale, métropolitaine, Rhône/Lyon et corse sont intégralement conservées. Les six alinéas de fond restent dans leur ordre et la transition demeure au septième. R366-1 à R366-7 et les deux annexes à R366-1/R366-5 ont été lus en entier avec leurs notes. Coordonner R366-5 pour conserver les clauses statutaires indépendamment du titre territorial, et R366-6/7 pour retirer arrêté, demande, recommandé, dossier, transmission et délai d'un mois attachés au seul avis territorial. L'annexe nationale doit perdre les mentions de cet avis, de sa commission et de l'agrément territorial comme condition d'accès au réseau, sans rétablissement sous un autre nom ; son soutien technique reste possible. L'annexe territoriale garde compétence juridique et financière, neutralité, gratuité, prévention des conflits et contrôle ; aucune suppression de ses autres clauses n'est opérée implicitement par ce lot. R366-1 à R366-4 gardent l'agrément national, sa mise en demeure de quatre mois et le contradictoire : ce contrôle du réseau n'est pas une seconde autorisation des associations territoriales. L452-1, lu en entier, conserve la possibilité d'aide aux organismes de L366-1 ; l'assimilation de plein droit maintient l'accès des associations futures éligibles sans accorder automatiquement une aide. R411-4, lu, conserve l'accès légal aux informations sans nouvelle collecte ni ouverture de données. Les conventions, aides et droits des usagers sont protégés ; aucune prétention de réécriture des annexes ou d'achèvement de tous les descendants de SRU201.",
    [
        "Agrément ministériel individuel des associations territoriales d'information sur le logement créées selon le premier alinéa.",
        "Avis préalable de l'association nationale et circuit de demande, de dossier et d'attente attaché à cet agrément territorial.",
    ],
    "Par rapport à la source officielle entière, l'agrément des associations territoriales et son avis préalable sont retirés, sans formalité substitutive ; l'assimilation de plein droit conserve l'accès aux régimes favorables. Ces coupes figuraient déjà au brouillon et ne sont pas présentées comme un gain nouveau de cette passe. Les missions gratuites, statuts, contrôles et agrément national demeurent essentiels.",
    "Le dispositif concerne seulement les associations territoriales constituées conformément à l'article. Il ne dispense pas l'association nationale de son agrément, n'attribue pas automatiquement une aide et n'efface pas les règles de création des associations. Les annexes et règlements hors lot restent à coordonner ; coût et solde global non mesurés.",
    "Aucune charge nouvelle n'est identifiée : l'assimilation est automatique sans demande, confirmation, registre ou déclaration. Les statuts, la composition, l'initiative publique conjointe et le contrôle existaient dans la source ; aucun nouveau délai ni condition de financement n'est créé en échange de la suppression de l'agrément territorial.",
)
effect(6, "authorization_removed", "adil-fin-agrement-territorial", "Suppression du circuit d'agrément territorial et de l'avis national préalable, avec maintien légal de la qualité donnant accès au réseau et aux aides.",
       "Associations du premier alinéa agréées après avis national ; demande, dossier et délai d'avis organisés par R366-5 à R366-7.",
       "Exercice sans agrément ni avis préalable ; assimilation de plein droit sans demande, sous les missions, statuts et contrôles maintenus.", "legal_duty", "Associations territoriales d'information sur le logement existantes et futures conformes au présent article.",
       "Suppression immédiate à l'entrée en vigueur ; demandes en cours sans objet ; aides, conventions et droits des usagers non interrompus.",
       "Ni déclaration ni confirmation de remplacement ; agrément national et autres conditions propres des aides demeurent distincts.",
       "Les associations mentionnées au premier alinéa sont agréées après avis d'une association nationale",
       "Les associations mentionnées au premier alinéa exercent leur mission sans agrément ni avis préalable d'une association nationale.")


# Contrôle des cibles imposées : aucune cible facultative dans reference_checks.
answer[0]["review_notes"] += " Le renvoi nouveau au V proposé de L302-5 ne figure pas dans les cibles de reference-targets.json : sa proposition entière a été vérifiée en lecture seule dans le corpus public, et son statut de projet est expressément conservé."
answer[1]["review_notes"] += " Le renvoi nouveau au1° de L821-1 n'est pas une cible fournie par reference-targets.json ; son texte officiel entier a été vérifié en lecture seule dans construction-habitation.json. La transition des anciens CDD est limitée à leur régime de travail et ne rétablit aucune enquête de logement supprimée."
answer[3]["review_notes"] += " Les renvois nouveaux à L365-3 et L365-4 ne sont pas des cibles fournies dans reference-targets.json ; leurs textes officiels entiers et leurs brouillons sont assignés dans source.json et leurs propositions finales sont coordonnées dans le présent fichier."
assessments = {
    0: [
        "L1234-1 règle le préavis de licenciement privé : un ou deux mois selon l'ancienneté officielle, puis quinze jours calendaires pour les nouveaux contrats dans sa proposition, avec anciens contrats et procédures spéciales préservés. Aucun renvoi de L353-15 ne vise cette règle : ses six mois suivent une troisième offre de relogement et ne sont pas un préavis d'emploi. Ils ne sont donc pas ramenés à quinze jours ; aucune nouvelle notification patronale n'est créée ici.",
        "L1221-2 proposé impose la durée indéterminée aux nouveaux emplois privés et préserve les contrats antérieurs, sans terme automatique de mission. L353-15 concerne des conventions et occupations immobilières ; ses conditions d'ancienneté renvoient à la construction ou acquisition des logements de L443-7, jamais à l'ancienneté d'un salarié. La suppression ciblée de cette ancienneté immobilière n'importe ni CDD ni contrat unique dans le bail et ne modifie aucun contrat de travail ancien.",
        "L1234-9 officiel ouvre une indemnité de licenciement à huit mois, sous exception de faute grave. Sa proposition prévoit un an au terme effectif, préavis inclus, puis0,20mois par année totale et mois complets au prorata, plafond six mois et employeur seul, avec transition des droits anciens et garanties spéciales. L353-15 ne vise ni cette indemnité ni une rupture d'emploi : relogement, prêts et perte du titre d'occupation restent à leur régime, sans condition d'ancienneté salariale ajoutée.",
        "Le V de L353-15 vise l'hébergement de L521-3-1, non un contrat privé de travail. Le I de la cible impose l'hébergement décent en cas d'inhabitabilité temporaire, et le II le relogement avec indemnité de trois mois du nouveau loyer ; au-delà de trois ans d'éviction, le II s'applique. Source et proposition de cible conservent ces protections. Le V maintenu n'abolit ni ces prestations ni cette indemnité ; son refus de réintégrer ou d'une offre adaptée reste distinct d'un préavis de quinze jours.",
        "Le V de L353-15 renvoie à la substitution pour hébergement ou relogement de L521-3-2. Les I et III de la cible déterminent l'intervention publique ; son VII permet au juge de statuer après trois refus. Son IV proposé limite les frais réels à un an de loyer, évite leur double recouvrement avec le VI et conserve l'indemnité du II de L521-3-1 ; le VIII protège les créances de relogements antérieurs. Le maintien du V n'annule aucune de ces règles ni leur transition et n'assimile aucune indemnité de relogement à une rupture salariale.",
    ],
    1: [
        "L1234-1 concerne le licenciement privé et non la durée du logement saisonnier. Son projet prévoit quinze jours calendaires pour les contrats nouveaux, indépendamment de l'ancienneté, tout en gardant l'ancien régime et les procédures collectives ou protections distinctes. L353-19-2 ne fixe aucun préavis d'emploi : le plafond locatif de six mois supprimé n'est pas un délai de licenciement. Les notifications locatives et salariales conservent leurs objets, sans nouvelle formalité ni extension à un régime public.",
        "L1221-2 proposé ferme les nouveaux CDD et n'autorise pas la fin automatique de l'emploi au terme d'une saison, mission ou formation, avec transition des contrats antérieurs. Le premier alinéa de L353-19-2 admet explicitement le contrat unique et son dernier alinéa sépare durée du logement et emploi. La dispense d'enquête et la possibilité non meublée restent ouvertes aux futures situations éligibles ; ni la sous-location temporaire ni sa prolongation ne créent un CDD spécial ou un renouvellement dérogatoire.",
        "L1234-9 proposé mesure le seuil d'un an au terme effectif avec préavis inclus, puis calcule0,20mois sur toute l'ancienneté et les mois complets, plafond six mois, pour la rupture patronale seulement, sous ses exceptions et transition. Aucune indemnité de cette nature n'est fixée par L353-19-2 ; l'accès au logement n'est subordonné ni à cet anniversaire ni à l'existence d'une indemnité. Les anciens droits, salaires, congés et réparations d'illégalité ne sont pas affectés par la durée de sous-location ou par la suppression de son maximum.",
        "Le premier alinéa officiel de L353-19-2 vise uniquement la branche saisonnière du3° de L1242-2 : tâches se répétant chaque année selon une périodicité à peu près fixe liée aux saisons ou modes de vie collectifs. La définition est reprise intégralement dans le nouveau corps ; ni emplois d'usage, ni1°,2°,4°,5°,6°, ni bulletin unique de moins d'un mois ne sont importés dans les conditions du logement. L'abrogation prospective proposée de la cible reste celle des nouveaux CDD : anciens contrats et créances sont préservés, l'APL et le logement saisonnier futur restent ouverts sous contrat unique sans autoriser de nouveau CDD.",
    ],
}
for index, item in enumerate(answer):
    key = item["code_id"] + "|" + item["source_id"]
    required = refs["requirements"][key]
    texts = assessments.get(index, [])
    assert len(required) == len(texts)
    item["reference_checks"] = [
        {"target_key": target_key, "view_sha256": refs["targets"][target_key]["view_sha256"], "assessment": assessment}
        for target_key, assessment in zip(required, texts)
    ]


def prose_spacing(value):
    """Rendre les notes lisibles sans toucher aux textes normatifs ni aux citations."""
    value = re.sub(r"\b([LRD])(?=\d{3}-)", r"\1. ", value)
    value = re.sub(r"(?<=[A-Za-zÀ-ÿ])(?=\d)", " ", value)
    value = value.replace("1erjanvier", "1er janvier")
    value = re.sub(r"\b(chapitre|titre|livre)(?=[IVX])", r"\1 ", value)
    value = re.sub(r"(?<=\d)(?=(?:euros|mois|ans)\b)", " ", value)
    value = re.sub(r"(?<=\d)(?=[IVX]+\b)", " ", value)
    value = re.sub(r"(?<=\d)(?=%)", " ", value)
    value = re.sub(r"\s*§\s*", " § ", value)
    return value


for item in answer:
    for key in ("reason", "review_notes", "benefit_review"):
        if key in item:
            item[key] = prose_spacing(item[key])
    if "removed_provisions" in item:
        item["removed_provisions"] = [prose_spacing(value) for value in item["removed_provisions"]]
    for key in ("assessment", "scope_limitations", "new_burdens_review"):
        item["substantive_impact"][key] = prose_spacing(item["substantive_impact"][key])
    for change in item["substantive_impact"]["effects"]:
        for key in ("description", "before", "after", "affected_population", "conditions_and_transition", "replacement_or_new_burdens"):
            change[key] = prose_spacing(change[key])
    for check in item["reference_checks"]:
        check["assessment"] = prose_spacing(check["assessment"])


# Contrôles structurels et citations, sans prétention de validation du fond juridique.
assert len(answer) == len(sources) == 7
for index, (source, item) in enumerate(zip(sources, answer)):
    for key in ("code_id", "source_id", "source_sha256", "number"):
        assert item[key] == source[key]
    impact = item["substantive_impact"]
    assert impact["version"] == 1
    for key in ("assessment", "scope_limitations", "new_burdens_review"):
        assert len(impact[key]) >= 40
    assert all(len(check["assessment"]) >= 80 for check in item["reference_checks"])
    if source.get("benefit_check_required"):
        assert len(item["benefit_review"]) >= 100
    if item["status"] == "rewrite_draft":
        assert item["proposed_xml"] and all(len(provision) >= 30 for provision in item["removed_provisions"])
    else:
        assert item["proposed_xml"] is None and impact["effects"] == []
    for change in impact["effects"]:
        assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)+", change["measure_id"])
        assert 6 <= len(change["measure_id"]) <= 96

Path("answer.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"written": "answer.json", "article_count": len(answer), "status_counts": {status: sum(a["status"] == status for a in answer) for status in {a["status"] for a in answer}}}, ensure_ascii=False))
