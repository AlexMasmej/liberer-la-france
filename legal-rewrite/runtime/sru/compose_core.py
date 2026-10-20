"""Complete proposed articles abolishing the municipal SRU quota system.

Every source, application note and previous draft was read in full. Unrelated
social-housing definitions and vested claims survive; quota machinery does not.
"""
from pathlib import Path
import html
import json
import re

HERE = Path(__file__).resolve().parent
sources = json.loads((HERE / 'core-source.json').read_text())
rows = []


def paragraphs(value):
    return '\n'.join('<p>' + html.escape(' '.join(p.split()), quote=False) + '</p>'
                     for p in value.strip().split('\n\n'))


def add(number, body, reason, notes, removed=None, repeal=None, raw=False):
    source = next(a for a in sources if a['number'] == number)
    row = {k: source[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}
    row.update(proposed_xml=body if raw else paragraphs(body), reason=reason,
               review_notes=notes, status='rewrite_draft')
    if removed:
        row.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19', removed_provisions=removed)
    if repeal:
        row.update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19', repeal_scope=repeal)
    rows.append(row)


previous = next(a for a in sources if a['number'] == 'L302-5')['previous_draft']['proposed_xml']
# The split consumes the opening paragraph; restore it before selecting all 13.
iv = re.findall(r'<p>.*?</p>', '<p>IV. – ' + previous.split('<p>IV. – ', 1)[1], re.S)
assert len(iv) == 13
iv[0] = paragraphs("IV. – Les catégories et assimilations du présent IV définissent les logements sociaux pour l'application des dispositions qui y renvoient. Elles n'instituent aucun quota communal, objectif de rattrapage, inventaire ou déclaration obligatoire. Sont compris dans cette définition les logements suivants :")
iv[10] = paragraphs("Lorsqu'une disposition distincte du régime de quotas abrogé renvoie au présent IV pour déterminer les résidences principales, sont retenues celles qui figurent dans les données légalement disponibles de l'administration fiscale, principalement issues de la déclaration des propriétaires prévue à l'article 1418 du code général des impôts, après déduction des logements concédés par nécessité absolue de service en application de l'article L. 4145-2 du code de la défense et de ceux concédés à des militaires des armées dans des immeubles dépendant du domaine de l'État. Cette définition n'impose aucune transmission ni collecte supplémentaire au titre du régime SRU supprimé.")
iv.append(paragraphs("Les renvois au présent article qui ont pour seul objet de désigner une catégorie de logements, sans définir un territoire ou une commune assujettie, s'entendent comme visant le présent IV. Ils ne rétablissent ni les taux ni les obligations supprimés. Les durées d'assimilation qu'il prévoit demeurent applicables aux seuls dispositifs autonomes qui utilisent ces définitions et à la liquidation des situations antérieures."))

start = paragraphs("""
I. – Les obligations de taux minimal de logements sociaux imposées aux communes par les I et II du présent article dans leur rédaction antérieure sont abrogées à l'entrée en vigueur de la loi portant la présente rédaction. Il en va de même des objectifs de rattrapage, prélèvements, majorations, procédures de carence et pouvoirs de substitution dont le seul fondement est le non-respect de ces taux ou de ces objectifs. Aucun renvoi à ces dispositions dans un autre texte ne peut en maintenir l'application pour l'avenir, sous réserve des seules situations antérieures définies au V.

II. – Abrogé.

III. – Abrogé.

III bis. – Abrogé.

III ter. – Abrogé.
""")
transition = paragraphs("""
V. – La suppression des obligations prévues aux I, II et III ter dans leur rédaction antérieure s'applique à compter de l'entrée en vigueur de la loi portant la présente rédaction, y compris aux demandes d'autorisation et aux périodes de rattrapage en cours. Aucun nouveau constat de carence, aucune nouvelle majoration ni sanction ne peut être prononcé après cette date pour le seul non-respect des obligations supprimées, même au titre d'une période antérieure. Les effets futurs des arrêtés de carence cessent à cette date. Les autorités compétentes de droit commun reprennent les instructions en cours, avec transmission des dossiers déjà constitués, sans nouveau dépôt ni recommencement des délais écoulés.

Aucun prélèvement, contribution obligatoire, reprise de déduction ou charge équivalente ne peut naître, sur le seul fondement des dispositions supprimées, d'un fait générateur survenu à compter de cette date. Les créances légalement nées de faits générateurs antérieurs restent régies par les dispositions antérieurement applicables pour leur liquidation, leur rectification, leur exigibilité, leur recouvrement, leurs déductions, leur restitution, leur prescription et leurs recours, même si une échéance ou un encaissement intervient ensuite. Une nouvelle décision de carence ou de majoration ne peut être prise pour faire naître une créance après la suppression. Les dispositions répressives plus douces s'appliquent aux sanctions qui ne sont pas devenues définitives. Aucun remboursement général ni crédit remboursable au titre d'un report de déduction inutilisable n'est institué.

Les actes régulièrement pris, les conventions valablement conclues et les engagements financiers acquis avant cette date, les droits des occupants, des cocontractants et des tiers ainsi que les aides régulièrement attribuées sont préservés. Leurs conditions d'exécution et les recours correspondants restent applicables. Les stipulations qui se bornent à rappeler les quotas ou obligations légales supprimés cessent d'en imposer le respect pour l'avenir. Aucun avenant ne peut, sur le seul fondement d'une carence abrogée, mettre à la charge d'une commune une nouvelle opération ou une contribution supplémentaire obligatoire ; les engagements librement consentis sur un fondement distinct restent possibles.

Les prescriptions d'une autorisation d'urbanisme régulièrement délivrée avant cette date ne sont pas automatiquement supprimées. Elles restent susceptibles d'être modifiées ou contestées selon les voies ordinaires, dans le respect des droits des tiers. La suppression des quotas nationaux communaux ne supprime pas les règles d'urbanisme, de sécurité, de salubrité, d'attribution, de conventionnement, de financement ou de protection des occupants qui disposent d'un fondement légal autonome.
""")
add(
    'L302-5', start + '\n' + '\n'.join(iv) + '\n' + transition,
    "Réforme de fond demandée par l'auteur : abolition des quotas communaux de 20 % et 25 %, de leurs exemptions et du quota par opération de 25 % prévu au III ter. La définition du parc social du IV est maintenue pour les régimes distincts qui l'utilisent, sans nouvel inventaire ni transmission. Un V nouveau règle les dettes antérieures, les contrats, les autorisations, la cessation des effets de carence et les compétences d'instruction.",
    "Périmètre : dispositif actuel issu de l'article 55 de la loi SRU et de ses modifications ultérieures, sans prétendre annuler toutes les modifications de la loi de 2000. Le IV conserve les six catégories et toutes les assimilations : 5 janvier 1977, 31 décembre 2016, cinq ans après convention, dix ans après vente, anciens supplétifs, cinq ans après option de location-accession et BRS depuis le 1er janvier 2019. Les sous-paragraphes du IV ne sont pas renumérotés. Le dénominateur fiscal n'est plus transmis pour un inventaire SRU : il reste une définition conditionnelle pour les seuls renvois autonomes. Les normes de risque, bruit, littoral, captage et défense citées dans les anciennes exemptions ne sont pas abrogées avec celles-ci. Les territoires autonomes encore désignés par l'ancien II nécessitent une coordination explicite ; ils ne sont pas rétablis comme communes déficitaires. La note d'entrée historique au 1er janvier 2023 ne date pas la réforme. Le V est une disposition nouvelle proposée ici, pas un paragraphe existant du droit en vigueur. Le prélèvement ancien peut conserver des échéances postérieures ; une reprise dont le fait générateur survient après réforme ne naît pas. Pas de chiffrage budgétaire inventé.",
    ["Suppression des taux communaux obligatoires de 20 % et 25 %, des classifications d'assujettissement et des listes d'exemption des I à III bis.",
     "Suppression du quota de 25 % par opération de plus de douze logements ou 800 mètres carrés du III ter et de ses dérogations devenues sans objet.",
     "Suppression du recours aux définitions du IV comme fondement d'inventaire, de collecte, de sanction ou de rétablissement indirect des quotas, sans supprimer les définitions utilisées par des régimes autonomes."],
    raw=True,
)

add(
    'L302-6',
    """
Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant abrogation des quotas communaux mentionnés à l'article L. 302-5. Les propriétaires et gestionnaires ne sont plus tenus de produire l'inventaire annuel SRU ni l'inventaire complémentaire par mode de financement. Les communications, observations et notifications de décompte imposées sur ce seul fondement cessent ; aucune attestation ou déclaration de remplacement n'est exigée.

L'amende de 1 500 euros pour absence d'inventaire ou inventaire manifestement erroné est supprimée. Les dispositions répressives plus douces s'appliquent aux sanctions qui ne sont pas devenues définitives. Les créances antérieures maintenues, les restitutions et les recours sont traités dans les conditions du V de l'article L. 302-5, sans nouvelle obligation générale de dépôt.

Les documents déjà produits conservent leur valeur pour la liquidation et le contrôle des seules situations antérieures. Les recensements, statistiques et informations nécessaires à des missions distinctes, notamment celles de l'article L. 411-10, restent régis par leur propre fondement légal, sans duplication de l'inventaire supprimé. Leur conservation et leur communication respectent les secrets protégés et les règles de protection des données applicables.
""",
    "Abrogation complète de l'inventaire et de son complément, des trois étapes préfectorales et de l'amende qui contrôlaient les quotas supprimés. Les données historiques utiles aux anciens contentieux sont conservées ; aucun nouveau reporting annuel n'est substitué à celui qui disparaît.",
    "Les échéances source du 1er juillet, 1er septembre et 31 décembre, le délai de deux mois d'observations et l'amende de 1 500 euros disparaissent avec la procédure pour l'avenir. Ils ne sont pas recyclés comme nouvelles échéances. Coordonner R302-15 et les renvois de L411-10/R411-3 sans supprimer les missions autonomes du répertoire des logements locatifs. Les faits de fraude distincts restent soumis à leur régime. Le V de L302-5 est créé dans la proposition du même lot.",
    repeal="Suppression de l'inventaire communal annuel SRU, du complément sur les financements, de la procédure préfectorale de décompte et de l'amende de 1 500 euros qui leur était propre ; conservation des pièces et recours relatifs aux situations anciennes.",
)

add(
    'L302-7',
    """
Le présent article est abrogé pour les faits générateurs survenant à compter de l'entrée en vigueur de la loi portant suppression du prélèvement SRU. Aucune créance nouvelle de ce prélèvement ne peut naître à compter de cette date, ni être remplacée sur ce seul fondement par une contribution de même objet. Les imputations sur les ressources fiscales communales et les reversements à des organismes bénéficiaires cessent pour les créances ainsi supprimées.

Les créances légalement nées de faits générateurs antérieurs restent soumises aux dispositions antérieurement applicables pour leur liquidation, leur rectification, leur calcul, leurs exonérations, leurs plafonds, leurs déductions, leurs échéances, leur recouvrement, leur affectation et leurs recours, dans les conditions du V de l'article L. 302-5. Une échéance postérieure ne constitue pas, à elle seule, un nouveau fait générateur. La seule suppression du prélèvement n'ouvre aucun remboursement des montants antérieurement dus.

Les dépenses et moins-values déductibles ainsi que les reports régulièrement constitués restent imputables sur les seules créances antérieures maintenues dans les limites qui leur étaient applicables. L'absence de prélèvement futur n'en fait pas des créances remboursables. Les sommes effectivement recouvrées au titre des anciennes créances restent affectées aux bénéficiaires et emplois prévus par leur régime antérieur, sous les contrôles transitoires de l'article L. 302-7-1.
""",
    "Abrogation de fond du prélèvement communal SRU et de sa mécanique pour les faits nouveaux, sans recréer un impôt de remplacement. La liquidation des années antérieures conserve les exonérations, plafonds et dépenses déductibles ; les reports ne sont pas transformés en subventions remboursables. Les fonds anciens restent affectés selon leurs règles propres.",
    "La formule de 25 % du potentiel fiscal par habitant, le plafond de 5 % des dépenses réelles, le minimum de 4 000 euros, l'exonération de trois ans et les circuits EPCI/métropole/EPF/FNAP/DOM cessent de produire de nouvelles créances, sans être recopiés comme un nouveau régime. Pour les créances antérieures, tous ces paramètres restent préservés par la rédaction applicable au fait générateur. R302-19 prévoit neuf échéances de mars à novembre : elles peuvent continuer pour une dette déjà née, sans prélèvement pour une nouvelle année après suppression. Coordonner CGCT L2332-2 et les ressources des fonds pour que leurs renvois ne créent aucune nouvelle créance. Aucun montant national de perte de recettes ni compensation n'est supposé.",
    repeal="Suppression du prélèvement annuel SRU sur les ressources fiscales communales, de sa formule et de ses reversements pour tout fait générateur nouveau ; maintien des créances anciennes, de leurs déductions, échéances, affectations et recours.",
)

add(
    'L302-7-1',
    """
Les établissements publics fonciers, l'office foncier de la Corse, les établissements publics de coopération intercommunale à fiscalité propre et la métropole de Lyon qui ont reçu des sommes en application des septième à neuvième alinéas de l'article L. 302-7 dans sa rédaction antérieure à l'abrogation du prélèvement restent tenus d'en justifier l'emploi. Cette obligation ne porte que sur les sommes antérieurement prélevées ou recouvrées au titre de créances antérieures maintenues par le V de l'article L. 302-5.

Pour ces seules sommes, les bénéficiaires conservent les pièces justifiant l'affectation et l'emploi des fonds, ainsi que le solde restant à employer. Aucun rapport annuel au 31 mars, ni aucun état périodique de remplacement, n'est exigé au titre du présent article, y compris pour les fonds anciens. Le représentant de l'État dans le département peut demander les seuls justificatifs nécessaires et manquants pour contrôler ces sommes. Les informations exactes et à jour déjà légalement détenues par cette autorité ou transmises dans le cadre de comptes ou rapports autonomes sont réutilisées sans nouvelle production ; le bénéficiaire peut en indiquer la référence. Ce contrôle transitoire ne peut servir à rétablir un suivi des quotas abrogés.

Si l'utilisation par un bénéficiaire désigné au septième alinéa de l'article L. 302-7 dans sa rédaction antérieure est non conforme, le représentant de l'État en informe son président dans le mois suivant la réception des justifications nécessaires et lui laisse deux mois pour présenter ses observations. Si les justifications restent insuffisantes, il peut, par arrêté motivé, suspendre les seuls versements encore dus au titre des créances antérieures, pour douze mois au plus et dans la limite des sommes dont l'emploi a été jugé non conforme. L'arrêté indique le montant et la durée. Durant cette suspension, les sommes sont versées à l'établissement public foncier correspondant aux anciens huitième ou neuvième alinéas, à l'office foncier de la Corse ou, à défaut, au fonds mentionné à l'article L. 435-1, selon le circuit applicable avant l'abrogation.

Aucune obligation permanente de bilan, de transmission ou de surveillance du respect de quotas n'est maintenue pour les faits postérieurs à l'abrogation. Un décret en Conseil d'État précise les modalités de cette liquidation transitoire sans créer de nouveau prélèvement ni de nouveau reporting SRU.
""",
    "Réduction de fond : suppression du rapport annuel spécial, y compris pour les fonds anciens. Le contrôle d'affectation devient ciblé sur les seules sommes anciennes, avec réutilisation des comptes et pièces légalement disponibles. Maintien du contradictoire et du plafonnement de suspension nécessaires pour empêcher la libre réaffectation d'anciens fonds publics, sans reporting périodique de remplacement.",
    "Les renvois ordinaux de L302-7 sont expressément figés à sa rédaction antérieure, puisque sa proposition abrogative ne conserve plus dix alinéas. L'échéance annuelle du 31 mars est supprimée ; les délais d'un mois après réception des justifications, de deux mois d'observations et de douze mois de suspension maximale restent limités aux anciens flux. Le point de départ d'un mois suit désormais la réception des pièces utiles, pas un rapport annuel aboli. Aucune nouvelle recette ne naît d'une suspension. Les bénéficiaires des anciens septième à neuvième alinéas et la règle propre au bénéficiaire du septième restent distincts. Harmonisation avec R302-20 : aucun rapport annuel distinct ne subsiste même sur des sommes anciennes. Pas de commission SRU reconstituée.",
    ["Suppression du rapport annuel spécial au 31 mars sur l'emploi des prélèvements SRU, y compris pour les fonds anciens, sans état périodique de remplacement.", "Suppression des transmissions en double lorsque les mêmes informations exactes et à jour sont déjà légalement détenues ou transmises à l'autorité compétente."],
)

add(
    'L302-8',
    """
Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant les quotas communaux SRU. Aucun objectif légal de rattrapage triennal, aucune répartition obligatoire entre prêts locatifs sociaux et prêts locatifs aidés d'intégration, aucun échéancier obligatoire ni aucune mutualisation ou adaptation de tels objectifs ne peut être imposé sur son fondement. La suppression s'applique aussi aux périodes en cours et aux arrondissements de Paris, Lyon et Marseille.

Les programmes locaux de l'habitat et les documents en tenant lieu cessent d'imposer, sur le seul fondement du présent article, ces objectifs de taux, de rattrapage et de typologie de financement. Ils peuvent conserver les diagnostics, projets, engagements librement consentis, programmes de rénovation et orientations de logement fondés sur leurs compétences légales distinctes. Leur mise en cohérence ne peut être subordonnée à une procédure de carence ou à une nouvelle obligation de rattrapage.

Les opérations déjà valablement engagées, les droits des tiers et les engagements financiers acquis demeurent soumis à leurs règles propres dans les conditions du V de l'article L. 302-5. Les engagements et aides relevant d'un autre fondement légal ne sont pas supprimés. Les bilans de documents de planification qui gardent une fonction autonome ne peuvent servir à contrôler ou sanctionner les objectifs SRU abrogés.
""",
    "Abrogation complète du rattrapage : suppression des objectifs de 33 %, 50 %, 100 %, des régimes d'entrée et adaptations, des minima de financement, de la mutualisation et de leur intégration obligatoire aux PLH et arrondissements. Les programmes, opérations et droits indépendants de ces quotas restent possibles, sans nouveau mécanisme de contrainte équivalente.",
    "Toutes les subdivisions I à X et leurs pourcentages, échéanciers et dérogations sont supprimés comme régime obligatoire pour l'avenir ; ils ne sont pas résumés en une norme partiellement conservée. La source officielle demeure intégralement consultable. Coordonner L302-1/4 et les documents en tenant lieu lorsqu'ils ne visent que l'ancien rattrapage, sans supprimer les fonctions autonomes de diagnostic et planification. L302-9 reprend sa propre cadence de bilan, afin de ne pas dépendre de la définition des périodes supprimée ici. Aucun coefficient de substitution ni quota d'arrondissement n'est réintroduit.",
    repeal="Suppression des dix subdivisions organisant objectifs communaux et d'arrondissement de rattrapage triennal, typologies de financement, échéanciers, adaptations et mutualisations SRU, ainsi que leur prise en compte obligatoire dans les PLH.",
)

add(
    'L302-8-1',
    """
Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant le rattrapage SRU. Aucun contrat de mixité sociale ne peut être exigé, proposé comme préalable obligatoire à une décision, ou utilisé pour rendre à nouveau opposables les taux, objectifs de rattrapage ou typologies supprimés. Les procédures en cours destinées exclusivement à conclure un tel contrat cessent sans nouveau dossier.

Les conventions valablement conclues avant cette date conservent leurs effets pour les engagements autonomes et financiers déjà acquis, les opérations engagées et les droits des cocontractants et des tiers. Leurs clauses qui se bornent à reprendre les obligations légales supprimées cessent d'imposer ces obligations pour l'avenir. Aucun avenant ne peut rétablir une contribution ou une opération forcée sur le seul fondement d'une carence abrogée.

Les collectivités, l'État et les autres personnes morales peuvent poursuivre ou conclure librement des conventions de logement sur leurs compétences distinctes, dans le respect des règles de financement et des droits des occupants, sans quota SRU ni sanction de carence. Les annexes des programmes locaux de l'habitat sont mises en cohérence sans recréer les procédures supprimées. Le V de l'article L. 302-5 s'applique aux situations antérieures.
""",
    "Abrogation du cadre spécial des contrats de mixité comme instruments de rattrapage, de leurs adaptations et obligations d'annexion. Les conventions autonomes et opérations déjà engagées restent protégées ; un contrat ne peut continuer à rendre obligatoires les quotas supprimés ni créer une contrainte équivalente.",
    "La durée de trois ans renouvelable, les périodes, les objectifs supplémentaires et la priorité vers les arrondissements sous 15 % disparaissent avec ce cadre obligatoire. Ne pas confondre abolition du cadre légal SRU avec annulation des marchés, subventions ou obligations financières déjà acquis. La proposition antérieure affirmait qu'aucun contrat ne dispensait des obligations légales : cette phrase devenue contraire à la décision de l'auteur est supprimée. Le droit commun des conventions reste applicable sans inventer un nouveau type de contrat.",
    repeal="Suppression du cadre légal spécial des contrats de mixité sociale, des procédures de négociation et d'annexion pour adapter ou mutualiser les objectifs SRU, avec conservation des engagements autonomes et droits antérieurs.",
)

add(
    'L302-9',
    """
La collectivité ou l'établissement public de coopération intercommunale qui a approuvé le programme local de l'habitat établit un bilan à l'issue de chaque période de trois ans, ces périodes étant décomptées à partir du 1er janvier 2002. Ce bilan porte notamment sur l'exécution des engagements de mixité sociale et des opérations de logement qui disposent d'un fondement distinct des quotas SRU supprimés. Il ne contrôle ni ne rend opposables les taux ou objectifs de rattrapage abrogés. Le bilan est communiqué au comité régional de l'habitat et de l'hébergement et rendu public par le représentant de l'État dans le département.

Le Gouvernement n'est plus tenu de remettre au Parlement le rapport triennal de conformité des communes aux obligations de réalisation de logements sociaux supprimées. Aucune remise nouvelle ne peut être exigée sur ce seul fondement à compter de l'entrée en vigueur de la loi portant la présente rédaction, y compris pour une période échue. Les rapports et bilans déjà publiés demeurent accessibles selon les règles qui leur sont applicables.
""",
    "Réduction de fond : suppression du rapport gouvernemental de contrôle des quotas et retrait du suivi obligatoire du rattrapage. Le bilan général du PLH, sa publicité et sa transmission au CRHH restent maintenus pour les projets et engagements autonomes, avec cadence inchangée explicitée indépendamment de L302-8 abrogé.",
    "La cadence de trois ans à compter du 1er janvier 2002 est reprise du deuxième alinéa du I ancien de L302-8, qui définissait les périodes pour cette section ; ce n'est pas une nouvelle date de réforme. Le rapport national est supprimé, pas renommé en bilan identique. Préserver les missions autonomes du CRHH lors de la coordination de R362-2 et les bilans distincts de L302-3. Les contrats et engagements libres ne rétablissent aucune sanction légale de quota.",
    ["Suppression du rapport triennal du Gouvernement au Parlement sur le respect de quotas communaux abrogés.", "Suppression du suivi ou de l'opposabilité des objectifs SRU par le bilan général du programme local de l'habitat, sans suppression de sa fonction autonome et de sa publicité."],
)

add(
    'L302-9-1',
    """
Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant la carence SRU. Aucune nouvelle procédure de constat de carence, majoration de prélèvement, substitution de compétence d'urbanisme, convention imposée ou contribution communale obligatoire ne peut être engagée ou décidée sur son fondement, même à raison d'objectifs non atteints pendant une période antérieure. Les procédures administratives en cours sans décision cessent sur ce seul fondement.

Les effets futurs des arrêtés de carence cessent à cette date. Les compétences précédemment substituées retournent aux autorités compétentes de droit commun, qui reprennent les dossiers en cours sans nouveau dépôt ni recommencement des délais. Les actes régulièrement accomplis, les décisions déjà prises et leurs recours demeurent régis par les règles applicables à leur date, sous réserve des dispositions répressives plus douces pour les sanctions non définitives.

Les conventions de construction, d'acquisition ou d'intermédiation locative valablement conclues avant cette date demeurent applicables pour les engagements financiers déjà acquis et les opérations engagées, ainsi que pour les droits des occupants, des organismes et des tiers. Les contributions et échéances qui correspondent à ces engagements restent régies par les conditions, limites, déductions, voies de recouvrement et recours antérieurement applicables. Aucun avenant ne peut imposer à la commune une nouvelle opération ou contribution sur le seul fondement de la carence supprimée ; un engagement volontaire sur une compétence distincte reste possible.

Les créances légalement nées de faits générateurs antérieurs et leurs échéances, liquidations, rectifications, déductions, recouvrements, restitutions, prescriptions et recours restent soumis au V de l'article L. 302-5. Aucun nouvel arrêté de majoration ne peut être pris pour constituer une dette après la réforme. La suppression de la carence ne met fin ni à un bail ni à une mesure de relogement ou de protection d'un occupant ayant un fondement autonome.
""",
    "Abrogation de la carence et de tous ses leviers : majoration, transfert de permis, conventions forcées et financement obligatoire de nouvelles opérations. La transition traite séparément la fin des effets administratifs futurs et les droits ou dettes déjà acquis, sans supprimer la sécurité des occupants ou effacer les contrats.",
    "Les plafonds de cinq fois, 5 %/7,5 %, potentiel fiscal de 150 %, durée de trois ans et limites de 50 000/30 000 euros ne servent plus à créer une charge nouvelle. Les conditions anciennes restent intégralement applicables aux seules créances et conventions antérieures maintenues. Les mises en demeure et leurs délais de deux mois demeurent utilisables uniquement pour ces créances, pas pour de nouvelles contributions. Coordonner urbanisme L111-24,L152-6,L210-1,L422-2 et leurs décrets, CCH L435-1 et DALO, CGCT et textes fonciers. La compétence de droit commun est déterminée par les règles propres à chaque autorisation ou préemption, pas attribuée uniformément au maire. L'abrogation ne valide ni n'annule rétroactivement un acte ; les voies de recours existantes restent ouvertes.",
    repeal="Suppression de la procédure de carence SRU, des majorations, des compétences préfectorales substituées et des nouvelles conventions ou contributions communales forcées, avec fin des effets futurs de carence et maintien des engagements et créances antérieurs légalement acquis.",
)

add(
    'L302-9-1-1',
    """
Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant les quotas communaux SRU. La commission nationale constituée sur son fondement est supprimée ; aucun nouvel avis, saisine, collecte de documents ou procédure d'exemption, de carence ou de contrat de rattrapage ne peut être exigé au titre de ses anciennes missions.

Les avis et pièces déjà établis demeurent conservés et communicables selon les règles applicables. Les actes et décisions antérieurs restent soumis à leurs voies de recours, sans qu'un nouvel avis de la commission supprimée puisse être requis pour apprécier leur légalité. Les dispositions relatives aux personnels et aux engagements contractuels demeurent régies par leurs règles propres ; aucune indemnité ou nouvelle dépense n'est instituée par la présente abrogation.

Les missions distinctes du comité régional de l'habitat et de l'hébergement, du Conseil national de l'habitat et des autres autorités mentionnées dans l'ancienne composition demeurent applicables lorsqu'elles disposent d'un fondement autonome.
""",
    "Abrogation complète de la commission nationale et de ses trois fonctions liées aux quotas : carence, exemptions et contrats de mixité. Il n'est créé ni commission remplaçante ni collecte de données. Les archives et les voies de recours demeurent, sans prolonger un avis obligatoire de l'organisme supprimé.",
    "Supprimer les textes de composition et procédures réglementaires propres à cette commission. La source prévoit deux députés, deux sénateurs et diverses juridictions/organisations : leurs sièges dans cet organe cessent, sans supprimer les organismes qu'ils représentent. La date historique du 1er septembre 2022 dans la note source ne date pas cette réforme. Les éventuelles mentions de la commission dans des lois ou décrets hors des cinq codes doivent être coordonnées expressément, sans prétendre que ces textes ont déjà été réécrits.",
    repeal="Suppression de la commission nationale SRU, de sa composition et de ses pouvoirs de collecte, d'avis et de recommandation pour la carence, les exemptions et les contrats de mixité devenus sans objet, sans remplacement institutionnel.",
)

add(
    'L302-9-1-2',
    """
Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant les obligations de carence SRU. Le quota de 30 % de logements familiaux locatifs sociaux, hors logements financés par un prêt locatif social, pour les opérations d'immeubles collectifs de plus de douze logements ou de plus de 800 mètres carrés n'est plus opposable aux décisions d'autorisation prises à compter de cette date, y compris pour une demande déjà déposée. La demande de dérogation et l'exception propres aux terrains affectés au ministère de la défense deviennent sans objet pour ces opérations.

Les prescriptions des autorisations régulièrement délivrées auparavant ne sont pas supprimées automatiquement ; elles peuvent être modifiées ou contestées selon les procédures ordinaires, dans le respect des droits des tiers. Les contrats, aides et engagements financiers déjà acquis et les droits des occupants restent protégés dans les conditions du V de l'article L. 302-5. Les règles de sécurité, de salubrité et les contraintes d'urbanisme qui disposent d'un fondement autonome demeurent applicables.
""",
    "Abrogation du quota par opération attaché à la carence, de sa dérogation et de l'exception défense devenues inutiles. L'allègement s'applique aux décisions nouvelles et demandes pendantes ; il ne réécrit pas automatiquement les anciens permis ou contrats et ne supprime pas les autres contrôles.",
    "Les seuils de plus de douze logements, plus de 800 mètres carrés et 30 % sont cités uniquement pour identifier la charge supprimée, pas pour maintenir une règle de construction future. Coordonner urbanisme L111-24 et R*431-16-3. La définition du parc social de L302-5 IV reste utilisable ailleurs ; sa conservation ne rétablit pas le quota. La règle du III ter de L302-5, distincte et fixée à 25 %, est également supprimée dans le même lot.",
    repeal="Suppression du quota de 30 % de logements sociaux hors PLS dans les opérations collectives des communes carencées, avec suppression de sa demande de dérogation et de son exception défense, sans annulation automatique des titres antérieurs.",
)

assert len(rows) == len(sources) == 10
assert {(a['code_id'], a['source_id']) for a in rows} == {(a['code_id'], a['source_id']) for a in sources}
(HERE / 'core-candidates.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2))
print(json.dumps({'file': str(HERE / 'core-candidates.json'), 'articles': len(rows)}, ensure_ascii=False))
