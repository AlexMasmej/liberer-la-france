import hashlib
import html
import json
import re
from pathlib import Path


source = json.loads(Path('source.json').read_text())[0]
references = json.loads(Path('reference-targets.json').read_text())
official = json.loads(Path('fragments/source-paragraphs.json').read_text())
previous = json.loads(Path('fragments/previous-paragraphs.json').read_text())
assert len(official) == 71 and len(previous) == 72

# Chaque emplacement source demeure un alinéa à la même position.
paragraphs = official.copy()
for position in (9, 13, 14, 21, 26, 31, 32, 33, 54, 55, 60, 62, 68, 70, 71):
    paragraphs[position - 1] = previous[position - 1]


def set_paragraph(position, text):
    paragraphs[position - 1] = '<p>' + html.escape(text, quote=False) + '</p>'


# La conjonction manque dans la source actuelle ; l'initial SRU 149 la fournit.
paragraphs[1] = official[1].replace(
    'des personnes physiques des sociétés de construction',
    'des personnes physiques et des sociétés de construction',
).replace(
    "en accession à la propriété, des sociétés d'habitat participatif",
    "en accession à la propriété, ainsi que des sociétés d'habitat participatif",
)

set_paragraph(12, "6° quater. A titre subsidiaire, de donner en location des logements conventionnés en application de l'article L. 831-1 du présent code, en vue de proposer des places d'hébergement d'urgence et d'hébergement relais ou d'insertion, centres d'hébergement et de réinsertion sociale, au sein de structures spécifiques et sécurisées, destinées aux personnes mariées, liées par un pacte civil de solidarité ou vivant maritalement qui se trouvent dans une situation d'urgence ou sont victimes de violences au sein du couple. La situation d'urgence ou les violences peuvent être établies par tout moyen, notamment par une ordonnance de protection délivrée par le juge aux affaires familiales en application du titre XIV du livre Ier du code civil ou par le récépissé du dépôt d'une plainte par la victime ; aucune de ces deux pièces n'est obligatoire. Les besoins doivent être identifiés dans le plan départemental d'action pour le logement et l'hébergement des personnes défavorisées. Aucun avis préalable de la commune ou de l'établissement public de coopération intercommunale compétent en matière d'habitat n'est requis au titre du présent 6° quater ;")

set_paragraph(15, "7° De réaliser, dans les conditions fixées par leurs statuts, toutes les actions ou opérations d'aménagement définies par le code de l'urbanisme, soit pour leur compte, soit pour le compte de tiers. Aucun accord préalable de la ou des collectivités locales concernées n'est requis au titre du présent 7° pour les opérations réalisées pour leur compte. Cette dispense ne vaut ni autorisation d'urbanisme, ni décision d'engagement financier d'une collectivité, ni autorisation d'occuper ou de disposer de ses biens ; les règles de compétence, de commande publique et les autres autorisations légalement applicables demeurent. Dans le cas où elles interviennent pour le compte de tiers, les dispositions des articles L. 443-14 et L. 451-5 ne sont pas applicables aux cessions d'immeubles rendues nécessaires par la réalisation de ces actions ou opérations. Lorsqu'elles se voient confier par convention la réalisation d'une opération de restructuration urbaine ou de revitalisation de centre-ville, celle-ci comprend toutes opérations ou actions ou tous aménagements ou équipements de nature à favoriser une politique de développement social urbain. Dans ce cas, la convention peut inclure des actions d'insertion professionnelle et sociale en faveur des habitants ;")

# Conventionnement : concordance vérifiée sur les articles L353-1 et L831-1.
paragraphs[25] = paragraphs[25].replace("l'article L. 351-2", "l'article L. 831-1")

# Le zonage ancien n'est utilisé que pour l'expérimentation de 2014 déjà close.
set_paragraph(47, "b) A titre expérimental pendant une durée de cinq ans à compter de la promulgation de la loi n° 2014-366 du 24 mars 2014 pour l'accès au logement et un urbanisme rénové, au sein d'immeubles bâtis occupés ou non, dans les communes appartenant à une zone d'urbanisation continue de plus de 50 000 habitants telle que définie à l'article 232 du code général des impôts ainsi que dans les communes de plus de 15 000 habitants en forte croissance démographique définies par décret pris en application du dernier alinéa du II de l'article L. 302-5 du présent code, ces dispositions et décrets étant retenus dans leur rédaction applicable aux opérations régulièrement engagées pendant cette expérimentation ;")

# Conserver les critères protecteurs de la source sans faire du contrôle a priori
# supprimé une nouvelle procédure ou une obligation de justification spontanée.
set_paragraph(62, "La création de telles filiales ne requiert ni transmission préalable de la décision au ministre chargé du logement ni délai d'opposition de celui-ci, sans dossier ni déclaration spéciale de création au titre du présent article. Cette dispense ne soustrait pas l'organisme mère aux obligations légales qui régissent ses missions en matière de logement social, notamment de construction et de rénovation de logements locatifs sociaux, ni aux contrôles de l'Agence nationale de contrôle du logement social.")
set_paragraph(68, "Une augmentation de capital de la filiale réalisée par l'organisme mère demeure soumise aux conditions fixées aux a et b ci-dessus. Elle ne requiert ni transmission préalable de la décision au représentant de l'État dans la région ni délai d'opposition de celui-ci, sans dossier ni déclaration spéciale d'augmentation de capital au titre du présent article. Cette dispense ne soustrait pas l'organisme mère aux obligations légales qui régissent ses missions en matière de logement social, notamment de construction et de rénovation de logements locatifs sociaux, ni aux contrôles de l'Agence nationale de contrôle du logement social.")

transition = "Les suppressions d'avis, d'accords, d'autorisations, de transmissions préalables et de délais d'opposition ainsi que la dispense de révision coopérative obligatoire prévues par le présent article s'appliquent à compter de l'entrée en vigueur de la loi portant sa réécriture, y compris aux demandes en cours sur lesquelles aucune décision définitive n'est intervenue. Ces demandes ne sont plus nécessaires à la réalisation de l'opération et aucune déclaration de remplacement n'est exigée. L'assouplissement des modes de preuve prévu au 6° quater et la suppression du zonage géographique applicable aux ventes complémentaires de logements à des personnes morales s'appliquent également aux opérations nouvelles et aux procédures en cours à cette date. Les oppositions et refus antérieurs ne sont pas annulés ; les nouvelles opérations restent soumises aux conditions de fond du présent article. Les actes antérieurement accomplis, les droits des tiers, les obligations contractuelles déjà souscrites et les recours relatifs aux opérations antérieures demeurent régis par les règles qui leur sont applicables. Les nouvelles dispositions ne rouvrent pas la période expérimentale de cinq ans prévue au b relatif à l'usufruit temporaire et ne modifient pas les droits nés des opérations régulièrement engagées pendant cette période. Elles sont sans incidence sur l'application des dispositions fiscales de l'article 108 de la loi n° 2026-103 du 19 février 2026 aux impositions établies au titre de 2027, notamment sur la prise en compte, pour ces impositions, de la durée de vacance antérieure au 1er janvier 2027. Ces dispositions fiscales ne conditionnent pas la suppression du zonage prévue au présent article."
paragraphs.append('<p>' + html.escape(transition, quote=False) + '</p>')

for index, fragment in enumerate(paragraphs, 1):
    Path(f'fragments/proposed-{index:02d}.xml').write_text(fragment + '\n')
proposed_xml = '\n'.join(paragraphs)
Path('proposed.xml').write_text(proposed_xml + '\n')


def plain(xml):
    return html.unescape(re.sub(r'<[^>]*>', '', xml))


source_plain = plain(source['source_xml'])
proposed_plain = plain(proposed_xml)


def effect(kind, measure_id, description, before, after, unit,
           affected_population, conditions_and_transition,
           replacement_or_new_burdens, source_quote, proposed_quote):
    assert len(source_quote) >= 12 and source_quote in source_plain, source_quote
    assert len(proposed_quote) >= 12 and proposed_quote in proposed_plain, proposed_quote
    assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', measure_id)
    assert 6 <= len(measure_id) <= 96
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit,
                affected_population=affected_population,
                conditions_and_transition=conditions_and_transition,
                replacement_or_new_burdens=replacement_or_new_burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


effects = [
    effect(
        'obligation_removed', 'cooperatives-hlm-hebergement-fin-avis-locaux',
        'Suppression des quatre avis locaux spéciaux des 6° ter à 6° sexies, déjà retenue dans le brouillon ; une seule famille de formalités, sans suppression des plans ou schémas.',
        "Avis communal ou intercommunal à recueillir pour chacune des quatre catégories d'activité subsidiaire, même lorsque les besoins figurent au plan ou schéma départemental.",
        "Aucun de ces avis préalables n'est requis ; besoins inscrits au plan ou schéma, conventionnement, destinataires et agréments des organismes demeurent.",
        'legal_duty', "Coopératives HLM intervenant dans l'hébergement et les terrains familiaux locatifs, et leurs bénéficiaires.",
        "Dès l'entrée en vigueur, demandes nouvelles et demandes pendantes sans décision définitive ; actes et droits antérieurs protégés.",
        "Aucune déclaration ni consultation de remplacement ; les règles autonomes de planification, d'urbanisme et de sécurité restent applicables.",
        "et que l'avis de la commune ou de l'établissement public de coopération intercommunale compétent en matière d'habitat a été recueilli",
        "Aucun avis préalable de la commune ou de l'établissement public de coopération intercommunale compétent en matière d'habitat n'est requis au titre du présent 6° ter.",
    ),
    effect(
        'authorization_removed', 'cooperatives-hlm-amenagement-fin-accord-local',
        "Coupe supplémentaire par rapport au brouillon : suppression du consentement local spécial aux opérations d'aménagement pour compte propre.",
        "Accord de la ou des collectivités locales concernées requis par le 7° pour une opération d'aménagement réalisée pour compte propre.",
        "Pas d'accord au titre du 7° ; les compétences publiques, autorisations d'urbanisme, biens et engagements financiers des collectivités restent régis par leurs fondements propres.",
        'legal_duty', "Coopératives HLM réalisant pour leur propre compte des actions ou opérations d'aménagement.",
        "Entrée en vigueur de la loi ; demandes en cours sans décision définitive comprises, sans annulation automatique des décisions antérieures.",
        "Aucune déclaration de remplacement. Le rappel des règles de compétence, de commande publique et de propriété ne crée aucun nouveau dossier.",
        "soit pour leur compte avec l'accord de la ou des collectivités locales concernées, soit pour le compte de tiers.",
        "Aucun accord préalable de la ou des collectivités locales concernées n'est requis au titre du présent 7° pour les opérations réalisées pour leur compte.",
    ),
    effect(
        'compliance_cost_reduced', 'hebergement-violences-preuve-non-exclusive',
        "Coupe supplémentaire : les deux justificatifs judiciaires ou policiers cessent d'être des voies de preuve exclusives d'accès à l'hébergement sécurisé du 6° quater.",
        "Situation d'urgence attestée par une ordonnance de protection ou violences attestées par un récépissé de plainte ; autre preuve non prévue par ce texte.",
        "Urgence ou violences établies par tout moyen ; ordonnance et récépissé restent recevables mais aucun des deux n'est imposé.",
        'legal_duty', "Personnes mariées, liées par un PACS ou vivant maritalement ayant besoin de l'hébergement sécurisé du 6° quater.",
        "Pour les nouvelles opérations et les procédures en cours à l'entrée en vigueur ; conventionnement, besoins identifiés et structures spécifiques et sécurisées conservés.",
        "Pas d'attestation, de formulaire ni de démarche de remplacement ; la réalité de la situation reste à établir, sans nouvel accès à des données.",
        "attestées par le récépissé du dépôt d'une plainte par la victime",
        "La situation d'urgence ou les violences peuvent être établies par tout moyen, notamment par une ordonnance de protection délivrée par le juge aux affaires familiales en application du titre XIV du livre Ier du code civil ou par le récépissé du dépôt d'une plainte par la victime ; aucune de ces deux pièces n'est obligatoire.",
    ),
    effect(
        'authorization_removed', 'cooperatives-hlm-participations-fin-accord-prefectoral',
        "Maintien de la suppression de l'accord préfectoral et de son circuit de demande au 11°.",
        "Participation soumise à accord préfectoral ; absence d'opposition dans les deux mois de la réception de la demande valant avis favorable.",
        "Participation sans accord préalable, demande correspondante ni délai d'opposition ; objet et règles de participation demeurent.",
        'legal_duty', "Coopératives HLM souscrivant ou acquérant des parts ou actions de sociétés d'aménagement ou de projet urbain partenarial.",
        "Bascule à l'entrée en vigueur, demandes pendantes non définitivement décidées comprises ; droits des tiers et contrats conservés.",
        "Aucun agrément ni dépôt déclaratif de substitution ; pas de nouvelle taxe.",
        "cette participation est soumise à l'accord du représentant de l'Etat dans le département du lieu de l'opération ou du projet.",
        "Cette participation ne requiert ni accord préalable du représentant de l'État dans le département du lieu de l'opération ou du projet, ni dépôt d'une demande à cette fin, ni délai d'opposition ;",
    ),
    effect(
        'authorization_removed', 'cooperatives-hlm-sci-fin-autorisation-ministerielle',
        "Maintien du retrait de l'autorisation ministérielle préalable pour l'acquisition intégrale d'une SCI ; les garanties de fond ne sont pas supprimées.",
        "Souscription ou acquisition intégrale des parts d'une SCI soumise à autorisation préalable du ministre chargé du logement.",
        "Pas d'autorisation ministérielle ; acquisition à date unique, dissolution en un an, objet et compétence géographique, conventionnement en un an et nullité des souscriptions irrégulières conservés.",
        'legal_duty', "Coopératives HLM acquérant ou souscrivant la totalité des parts d'une SCI.",
        "Opérations nouvelles et demandes en cours sans décision définitive à l'entrée en vigueur ; actes antérieurs, conventions et droits des tiers préservés.",
        "Aucune déclaration ou autorisation équivalente créée ; le renvoi au conventionnement est corrigé séparément, sans assouplir ses garanties.",
        "L'opération fait l'objet d'une autorisation préalable du ministre chargé du logement.",
        "16° Souscrire ou acquérir la totalité des parts d'une société civile immobilière, sans autorisation préalable du ministre chargé du logement.",
    ),
    effect(
        'coordination', 'hlm-coproprietes-fin-accords-prealables',
        "Coordination organique de la suppression des accords municipaux et préfectoraux en copropriété déjà portée par L411-2 ; la dérogation expresse empêche leur retour par renvoi, sans compter une seconde autorisation générale supprimée.",
        "Accords du maire et du préfet pour la gestion des copropriétés en difficulté ; accord municipal pour les autres logements du trente-troisième alinéa ; délai préfectoral de deux mois.",
        "Plus de ces accords, demandes ou délai d'opposition pour ces activités ; les autres critères du service d'intérêt général, le mandat et les conditions de L442-11 restent applicables.",
        'legal_duty', "Coopératives HLM syndics, administrateurs de biens ou acquéreurs de lots dans les copropriétés et périmètres visés ; propriétaires et occupants.",
        "Entrée en vigueur et procédures pendantes sans décision définitive ; conventions, aides valables, droits des tiers et recours historiques maintenus.",
        "Aucune déclaration de substitution ; maintien des contrôles légaux et des conditions matérielles d'aide, pas de droit automatique à une aide nouvelle.",
        "avec l'accord du maire de la commune d'implantation et du représentant de l'Etat dans le département",
        "Pour les sociétés régies par le présent article, les activités prévues au présent alinéa sont exercées sans accord préalable du maire de la commune d'implantation ou du représentant de l'État dans le département, sans demande à cette fin et sans délai d'opposition.",
    ),
    effect(
        'obligation_removed', 'cooperatives-hlm-fin-revision-periodique-obligatoire',
        "Maintien de la dispense de révision coopérative périodique imposée quelle que soit l'activité ; l'audit volontaire reste possible.",
        "Examen périodique obligatoire de l'organisation et du fonctionnement par révision coopérative, quelle que soit l'importance de l'activité.",
        "Révision périodique facultative ; contrôles ANCOLS, comptes, droits des associés et exceptions de L422-12 conservés.",
        'legal_duty', "Sociétés anonymes coopératives de production d'HLM et extension aux SCIC-HLM selon les textes qui les régissent, à coordonner séparément.",
        "Dispense à compter de l'entrée en vigueur ; obligations contractuelles déjà souscrites et droits et recours antérieurs protégés.",
        "Aucun rapport, certificat périodique ni nouvel examen de remplacement ; le réviseur volontaire ne devient pas obligatoire.",
        "font procéder périodiquement, quelle que soit l'importance de leur activité, à l'examen de leur organisation et de leur fonctionnement dans le cadre d'une procédure de révision coopérative.",
        "les sociétés anonymes coopératives de production d'habitations à loyer modéré ne sont pas tenues de faire procéder à une révision coopérative périodique de leur organisation et de leur fonctionnement.",
    ),
    effect(
        'authorization_removed', 'cooperatives-hlm-filiales-fin-controle-prealable',
        "Retrait maintenu des contrôles préalables de création, participation et augmentation de capital dans les filiales et sociétés de logement intermédiaire ; les exécutions réglementaires relèvent de la même mesure.",
        "Opposition ministérielle à la création ou préfectorale à l'augmentation de capital ; décision exécutoire après trois mois sans opposition motivée suivant transmission ; mêmes règles pour les sociétés conjointement contrôlées.",
        "Ni transmission, dossier spécial, déclaration ni attente d'opposition ; objet exclusif, aides, plafonds, contrôle conjoint, règles d'apports et protection légale des missions sociales restent applicables.",
        'legal_duty', "Coopératives HLM et leurs filiales ou sociétés conjointement contrôlées de logement locatif intermédiaire.",
        "À l'entrée en vigueur, y compris demandes pendantes sans décision définitive ; actes antérieurs et engagements de financement préservés.",
        "Aucune procédure préalable de substitution. Les contrôles ANCOLS et obligations légales autonomes demeurent ; le critère discrétionnaire d'opposition n'est pas converti en nouveau dossier ni en interdiction générale supplémentaire.",
        "A défaut d'opposition motivée du ministre dans un délai de trois mois à compter de la transmission de la décision de création, cette dernière est exécutoire.",
        "La création de telles filiales ne requiert ni transmission préalable de la décision au ministre chargé du logement ni délai d'opposition de celui-ci, sans dossier ni déclaration spéciale de création au titre du présent article.",
    ),
    effect(
        'relief_extended', 'cooperatives-hlm-ventes-complementaires-fin-zonage',
        "Maintien de l'extension territoriale des ventes complémentaires à personnes morales, sans quota communal ni suppression des conditions sociales.",
        "Faculté limitée aux communes d'une zone d'urbanisation continue de plus de 50 000 habitants et à certaines communes de plus de 15 000 habitants en forte croissance démographique.",
        "Faculté ouverte sur l'ensemble du territoire relevant de la compétence géographique de l'organisme, sans condition de taux communal ; caractère complémentaire, besoin ou demande locale, plafonds de ressources et prix conservés.",
        'regime', "Coopératives HLM, personnes morales acquéreuses et personnes respectant les plafonds de ressources des logements concernés.",
        "Opérations nouvelles et procédures pendantes à l'entrée en vigueur ; pas de réouverture de l'expérimentation d'usufruit de 2014.",
        "Aucun quota, justification ou agrément de substitution ; la compétence géographique générale de l'organisme n'est pas étendue au-delà de son régime propre.",
        "Exclusivement dans les communes appartenant à une zone d'urbanisation continue de plus de 50 000 habitants définie au 1° du B du I de l'article 1406 bis du code général des impôts",
        "sur l'ensemble du territoire relevant de leur compétence géographique, sans condition tenant au taux communal de logements sociaux.",
    ),
    effect(
        'coordination', 'conventionnement-hlm-renvois-recodification',
        "Correction nécessaire du renvoi périmé du 16° : le conventionnement locatif est désormais visé par L831-1, avec L353-1 comme texte du régime des conventions.",
        "L351-2 encore cité dans le corps source, malgré la note de recodification de 2019 ; délai de conventionnement d'un an.",
        "L831-1 expressément cité pour les conventions des logements transmis ; délai d'un an conservé, sans nouvelle condition d'aide.",
        'other', "Coopératives HLM reprenant une SCI et occupants des logements transmis.",
        "Coordination du corps proposé ; conventions et droits antérieurs conservent leur régime propre.",
        "Aucune formalité supprimée supplémentaire revendiquée, aucun nouvel agrément ou justificatif.",
        "Les logements transmis font l'objet de conventions conclues en application de l'article L. 351-2 dans un délai d'un an à compter de la transmission effective du patrimoine.",
        "Les logements transmis font l'objet, dans l'année qui suit la transmission effective du patrimoine, des conventions conclues en application de l'article L. 831-1.",
    ),
    effect(
        'coordination', 'sru-suppression-quotas-logements-sociaux',
        "Les renvois de définition sont limités au IV autonome de L302-5 ; le zonage de l'ancienne expérimentation demeure figé au droit de ses opérations, sans recréer un quota courant.",
        "Renvois généraux à L302-5 pour le plafond de 10 % et l'exclusion de logements sociaux des transformations ; renvoi au II pour une expérimentation historique de cinq ans.",
        "Renvois au IV pour les définitions ; rédaction historique de L302-5 II, de CGI232 et de leurs décrets seulement pour les opérations régulièrement engagées pendant l'expérimentation.",
        'other', "Coopératives HLM, filiales et titulaires de droits issus des opérations historiques d'usufruit.",
        "La période expérimentale n'est pas rouverte ; 10 % et exclusion des logements sociaux des transformations maintenus.",
        "Pas de nouvel inventaire, liste communale, taux communal ou obligation de production ; ce renvoi ne compte pas comme une nouvelle suppression de quota.",
        "dans la limite de 10 % des logements locatifs sociaux mentionnés à l'article L. 302-5 détenus par l'organisme",
        "dans la limite de 10 % des logements locatifs sociaux mentionnés au IV de l'article L. 302-5 qu'elles détiennent.",
    ),
]

assessments = {
    'L1234-1': "Absence de renvoi de L422-3 à cet article de travail : les contrats des 10° et cinquante-troisième alinéa sont des ventes immobilières, non des contrats salariés. Les fonctionnaires du 9° sont des bénéficiaires du logement, non des salariés privés requalifiés. Le préavis de quinze jours des nouveaux contrats privés et la transition des anciens préavis restent à leur champ ; aucun délai d'accord local ou d'opposition administrative supprimé ici n'en est une application.",
    'L1221-2': "L422-3 définit des capacités d'organismes et des opérations immobilières ; une convention d'aménagement, une expérimentation ou une mission d'insertion ne fixe pas le terme d'un emploi. La proposition de L1221-2 écarte les nouveaux CDD et conserve les contrats anciens. Le renvoi à L631-12 permet l'accueil des personnes en apprentissage ou professionnalisation au sein du contrat unique selon cette cible, sans créer dans L422-3 un contrat spécial dérogatoire ou une nouvelle obligation d'embauche.",
    'L1234-9': "Aucun renvoi direct ou indemnité de licenciement dans L422-3 : ses garanties de rachat et ses conventions de vente ne sont pas la rupture d'un emploi. Le seuil d'un an mesuré à la fin effective avec préavis, les 0,20 mois sur toute l'ancienneté, le prorata par mois complets, le plafond de six mois et la transition des services anciens de la cible proposée ne sont donc pas transposés. Les droits spéciaux et les indemnisations de ventes immobilières restent distincts.",
    'L261-1': "Le 10° vise les ventes d'immeubles à construire par L261-1 et suivants ; le cinquante-troisième alinéa vise expressément L261-1 pour l'acquisition auprès d'une SCI, avec 25 % de logements sociaux et dix ans au plus pour la SCI. Le délai de construction et la distinction vente à terme/VEFA de la source sont civils et immobiliers. Ils demeurent et ne constituent aucun CDD, préavis ou seuil d'ancienneté salarié ; la proposition de cible n'est pas du droit en vigueur.",
    'L261-12': "La plage L261-1 à L261-22 du trente-neuvième alinéa inclut L261-12 ; le 10° vise également les articles suivants L261-1. L'interdiction d'encaisser avant contrat ou exigibilité, et les dépôts de garantie progressifs sur compte spécial protégés en vente à terme, restent applicables dans leur champ. La suppression d'autorisations corporatives ne les écarte pas ; ni calendrier de paiement immobilier ni terme de vente ne devient une durée d'emploi ou un délai de notification de rupture.",
    'L261-14': "La plage L261-1 à L261-22 et le renvoi L261-1 et suivants gardent L261-14 dans son champ propre : plafond de 10 % du prix pour l'indemnité forfaitaire de résolution, avec réparation possible du préjudice réellement subi. Il protège les parties à une vente immobilière, non un salarié ; aucun remplacement par 0,20 mois, zéro avant un an ou plafond de six mois de salaire. La présente dispense d'accords administratifs laisse cette protection des opérations futures et les droits anciens ouverts.",
    'L631-12': "Le cinquante-deuxième alinéa maintient la faculté subsidiaire de construire, acquérir et gérer des résidences universitaires dans les conditions de L631-12. La cible distingue son bail d'un an renouvelable des contrats d'apprentissage ou professionnalisation et ouvre expressément ces places lorsque la formation s'inscrit dans le contrat unique. Les anciens baux, conventions et emplois gardent leurs transitions ; ni fin de formation ni fin de bail ne rompt l'emploi. Les dispenses d'autorisation et d'agrément de la proposition cible ne sont pas comptées ici comme de nouvelles suppressions.",
    'L615-10': "Le trente-quatrième alinéa maintient l'intervention comme opérateur, sans faculté d'être tiers-financeur, dans les procédures de L615-10. L'expérimentation de vingt ans ouverte en 2014, les pouvoirs d'expropriation, redevances, droits APL, entretien, responsabilités et consentements de remise en copropriété ont leur fondement propre. La proposition cible retire seule l'actualisation triennale du plan, y compris les échéances non exécutées, sans prorogation ; L422-3 ne la réintroduit pas et ne supprime pas ces protections par sa dispense distincte d'accords de gestion. Aucun préavis salarié ne s'applique à cette mission immobilière.",
}

required = references['requirements'][source['code_id'] + '|' + source['source_id']]
reference_checks = []
for key in required:
    target = references['targets'][key]
    assessment = assessments[target['number']]
    assert len(assessment) >= 80
    reference_checks.append(dict(target_key=key, view_sha256=target['view_sha256'], assessment=assessment))

answer = {
    'code_id': source['code_id'],
    'source_id': source['source_id'],
    'source_sha256': source['source_sha256'],
    'number': source['number'],
    'proposed_xml': proposed_xml,
    'reason': "Réforme de fond du périmètre et des démarches des coopératives HLM, et non réécriture à droit constant. Les suppressions déjà acquises sont conservées : avis locaux des 6° ter à sexies, accord préfectoral du 11°, autorisation ministérielle du 16°, accords en copropriété, révision coopérative périodique, contrôles préalables des filiales et sociétés conjointement contrôlées, et zonage des ventes complémentaires. La seconde passe retire en plus l'accord local spécial du 7° pour l'aménagement pour compte propre et l'exclusivité de l'ordonnance de protection ou du récépissé de plainte au 6° quater : une preuve libre permet l'accès au même hébergement sécurisé sans démarche policière ou judiciaire obligatoire. Les délais d'un an du 16°, conventions, plafonds, aides, objets sociaux, règles d'apports, comptes et contrôles autonomes restent ; aucune taxe n'est supprimée par cet article. Les renvois périmés sont coordonnés, le zonage de l'expérimentation close est figé historiquement et les alinéas non concernés sont reproduits sans nouvelle reformulation. Les garanties utiles des opérations immobilières et les transitions sont conservées.",
    'review_notes': "Lecture intégrale des 71 alinéas officiels, des notes, des 72 alinéas du previous_draft, des quatre textes initiaux SRU joints (82, 149, 152, 164), de toutes les coordinations et des huit cibles avec leurs sources, notes et propositions. Le proposed_xml de premier niveau est identique au previous_draft après décodage des entités. Les 71 positions sont conservées, avec un seul alinéa transitoire ajouté ; les cinquante-sixième à cinquante-neuvième alinéas et les trois alinéas précédant les exclusions sont donc aux mêmes places. Aucun tableau ni pièce de formule n'est présent dans cette source.\n\nRenvois : le 16° remplace effectivement L351-2 par L831-1 ; la note de l'ordonnance 2019-770 et les sources entières du corpus local L353-1, L821-2, L831-1 et L831-2 ont été lues. L831-1 est la cible du conventionnement locatif ; L821-2 est la règle de résidence principale et L831-2 concerne l'accession, non des conventions de location à cumuler. Aucun nouveau renvoi normatif extérieur aux cibles et à la source n'est ajouté. L302-5 IV demeure la définition autonome pour le plafond de 10 % et l'exclusion des transformations de logements sociaux. Les textes actuels et notes de L411-2, L422-12 et L442-11 ont été lus ; leur comptabilité séparée, affectation des fonds, réserves non distribuables, décence, plafonds de loyers et ressources ne disparaissent pas. La dérogation expresse de L422-3 aux accords de L411-2 est conservée pour éviter une autorisation réintroduite à travers le service d'intérêt général. Les conditions matérielles de compensation de service public et d'aides européennes restent à respecter ; aucune conformité globale au droit de l'Union n'est affirmée.\n\nDeux nouvelles coupes : le consentement local propre au 7° n'est pas une autorisation d'urbanisme, une commande publique, une décision budgétaire, un droit d'occupation du domaine ni une disposition du patrimoine public ; ces fondements distincts sont réservés sans nouveau dossier. Le plan départemental, le conventionnement et les structures sécurisées du 6° quater subsistent ; supprimer l'exclusivité de la plainte ou de l'ordonnance permet d'établir des violences sans avoir engagé ces procédures, sans imposer un certificat de remplacement. Les bénéficiaires mariés, pacsés ou vivant maritalement ne sont pas restreints.\n\nAutres charges examinées : agréments des opérateurs d'intermédiation et des organismes de foncier solidaire, objet/compétence géographique, conventions de services sociaux avec l'État, affectation aux publics et plafonds de prix/loyers/ressources restent nécessaires à la protection des occupants et des actifs ou aides affectés. Les 25 % de logements sociaux d'une SCI et sa durée de dix ans, les 10 % de logements intermédiaires, les 30 % de chiffre d'affaires de syndic, les 99 % de détention associative, les deux délais d'un an du 16°, le rapport du commissaire aux apports, le capital d'un euro, le contrôle conjoint, le remboursement et les prix de revient sont conservés pour protéger patrimoines, bénéficiaires et fonds sociaux. La suppression des oppositions n'est pas transformée, comme pouvait le suggérer la rédaction antérieure, en nouvelle interdiction générale autonome de porter atteinte à la capacité de l'organisme : les obligations légales déjà applicables à ses missions et les contrôles ANCOLS sont réservés, sans nouvel examen systématique.\n\nCoordinations non réalisées dans ce lot : les sources intégrales de R422-9-2, R422-17-1 à R422-17-4 et R442-23 ont été lues. Retirer leurs obligations correspondantes pour les seuls organismes concernés ; R442-23 cite en outre un septième alinéa de L422-3 qui ne désigne plus la gestion des copropriétés en difficulté. R422-9-2 doit traiter la révision volontaire sans reconstituer de périodicité obligatoire. Les listes de pièces des arrêtés d'application de R422-17-1 à 4, les clauses types des annexes R422-6/37, ainsi que les effets éventuels des articles 25-1 et 25-5 de la loi de 1947 et du décret 2015-706 restent à vérifier/coordonner hors de cet article ; leurs contenus non joints ne sont pas inventés. R422-8, R422-9, R422-17 et R422-33 ont aussi été lus : leurs procédures distinctes de transfert de réserves, transformation et liquidation ne sont pas de nouvelles coupes de L422-3. Les textes de commande publique, la loi de 1965, le code civil et le code monétaire et financier gardent leur champ ; ils ne sont pas déclarés réécrits ici.\n\nHistorique : SRU 82 ouvrait une faculté favorable d'acquisition, travaux et location provisoire de lots en sauvegarde ; elle est conservée avec ses extensions autonomes. SRU 149 et 152 fondaient notamment les habilitations d'accession, location-accession, services, aménagement et location ainsi que les dérogations L443-14/L451-5 ; aucun de ces avantages n'est supprimé pour son origine. Le 1° de la source omet la conjonction entre personnes physiques et sociétés de construction : l'initial SRU 149 la contient ; la coordination la rétablit explicitement et articule la catégorie participative, sans exclure de prestataire ni bénéficiaire. SRU 152 avait supprimé l'ancien L422-3-2 : cette suppression ne vaut pas origine du L422-3-2 actuel. SRU 164 V supprimait un douzième alinéa ancien dont le contenu n'est pas joint ; cette filiation n'est pas considérée soldée par la lecture du douzième alinéa actuel. Aucune réintroduction du régime SGA n'est opérée. L'examen des 209 articles SRU n'est pas déclaré achevé.\n\nLe b d'usufruit reste l'expérimentation de cinq ans ouverte en 2014, sans réouverture ; les deux zonages et décrets sont retenus dans leur rédaction applicable aux opérations historiques, notamment l'ancien CGI232 malgré la référence nouvelle à 1406 bis ailleurs dans la source. Les notes fiscales 2027 conservent leur objet et la durée de vacance antérieure au 1er janvier 2027, sans reporter l'extension territoriale des ventes. Aucun taux, montant de recette, date de promulgation future ou compensation n'est créé. Aucun chiffrage de baisse nette de complexité ou de finances publiques n'est établi. La vérification locale des empreintes, citations et renvois ne constitue pas une validation juridique indépendante.",
    'status': 'rewrite_draft',
    'change_type': 'normative_reduction',
    'reform_policy_id': 'editorial_direction_2026_10_19',
    'removed_provisions': [
        "Les quatre avis communaux ou intercommunaux préalables des activités subsidiaires mentionnées aux 6° ter à 6° sexies sont supprimés.",
        "L'accord préalable spécial des collectivités locales sur les opérations d'aménagement réalisées pour compte propre au 7° est supprimé, sans remplacement déclaratif.",
        "L'exclusivité de l'ordonnance de protection ou du récépissé de plainte comme justificatifs au 6° quater est supprimée ; la preuve de la situation peut être apportée par tout moyen.",
        "L'accord préfectoral, la demande correspondante et le délai d'opposition de deux mois pour les participations du 11° sont supprimés.",
        "L'autorisation ministérielle préalable du 16° pour la souscription ou l'acquisition de la totalité des parts d'une SCI est supprimée.",
        "Les accords municipaux et préfectoraux, leurs demandes et le délai d'opposition pour les interventions de gestion en copropriété des trente-deuxième et trente-troisième alinéas sont supprimés dans ce champ.",
        "La révision coopérative périodique obligatoire, quelle que soit l'importance de l'activité, est supprimée ; le recours volontaire et les contrôles légaux distincts subsistent.",
        "La transmission et le contrôle préalable avec opposition ministérielle et délai de trois mois pour créer une filiale de logement intermédiaire sont supprimés.",
        "La transmission et le contrôle préalable avec opposition préfectorale et délai de trois mois pour augmenter le capital de ces filiales sont supprimés, avec coordination des sociétés conjointement contrôlées.",
        "Le filtre limitant les ventes complémentaires à des personnes morales aux communes des deux zonages est supprimé, sans supprimer les conditions de ressources, de prix et d'offre insuffisante ou de demande locale.",
    ],
    'benefit_review': "Aucun prélèvement fiscal n'est institué par L422-3 et aucune baisse fiscale autonome n'est revendiquée. Les avantages possibles sont ses habilitations à agir, ses dispenses et l'accès des publics à des opérations sociales : ils restent ouverts aux futures situations éligibles. Les 1°, 2°, 2° bis, 4° et 5° conservent assistance à l'accession, vente à prix plafonné, location-accession, lotissement et hébergement de loisir social. Les 6° à 6° sexies gardent hôtels pour personnes en difficulté, résidences hôtelières sociales, hébergement conventionné par opérateurs agréés ou sociaux, protection des victimes, établissements d'hébergement et terrains familiaux ; les plans et schémas et les structures sécurisées demeurent. La preuve libre du 6° quater et la fin des avis locaux élargissent l'accès sans fermer les voies de preuve existantes. Les 7°, 7° bis, 8° et 8° bis maintiennent aménagement, missions pour collectivités et tiers, prestations de logement et d'économie sociale, rénovation énergétique et insertion. La dérogation aux cessions L443-14/L451-5 pour compte de tiers reste expresse ; la dispense d'accord local spécial pour compte propre n'oblige aucune collectivité à financer, commander ou céder. Les 9° à 15° conservent les logements pour les publics de sécurité et secours, ventes entre organismes, participations, habitat participatif, garantie de rachat à destination de personnes modestes, organismes de foncier solidaire et adhésions sociales. Le 16° conserve l'acquisition intégrale d'une SCI sans autorisation préalable mais avec les deux délais d'un an, les conventions désormais rattachées à L831-1, l'objet et la compétence géographique ; il ne retire pas les aides des occupants.\n\nLes équipements d'intérêt général, locaux commerciaux/professionnels, études urbaines, services aux personnes âgées, handicapées ou victimes de violences restent autorisés. Les ventes complémentaires aux personnes morales sont ouvertes sur toute la compétence géographique, avec leur caractère complémentaire, les hypothèses d'offre insuffisante ou de demande de la collectivité et les plafonds ; aucune commune n'est soumise à un quota. Gestion, acquisition/revente de lots, travaux et location provisoire dans les copropriétés en difficulté, mandats et prestations en périmètres dégradés sont maintenus, y compris les dérogations réglementaires possibles aux règles HLM. L'absence des accords supprimés ne prive pas ces activités du service d'intérêt général par L411-2 ; ses autres conditions, exonérations et aides restent à leur champ pour les opérations futures. La qualité d'opérateur sans tiers-financement reste : ce n'est pas une exonération fiscale à abolir. La cible L615-10 conserve dans son champ les allocations de logement attachées à la redevance des propriétaires occupants ; cette référence ne les ferme pas.\n\nLes opérations d'intermédiation bancaire pour membres, prestations entre organismes, activité locative, syndic et administration de biens conservent leurs facultés et limites, dont 99 % de détention par l'association et 30 % du chiffre d'affaires pour le champ complémentaire. Les ventes et prestations à l'association ou à ses SCI, les services aux organismes de foncier solidaire, l'agrément pour exercer comme tel, les baux réels solidaires d'activité, les services sociaux conventionnés avec l'État et les mandats des logements de l'association demeurent. Nue-propriété et usufruit temporaire restent autorisés, avec la dispense de la sous-section 1 de la section 2 du chapitre III du titre IV pour les opérations des trois alinéas précédents. L'expérimentation de cinq ans de 2014 était déjà temporaire dans la source ; son absence de réouverture n'est pas la suppression d'un droit futur encore ouvert, et les droits des opérations régulièrement engagées sont protégés. Les locations/sous-locations conventionnées pour les publics fragiles ou en transition, la gestion de logements vacants, la gérance des SCI sociales et les résidences universitaires restent possibles. Pour ces dernières, la cible fournie garde étudiants, moins de trente ans en formation/stage, apprentis et personnes en professionnalisation, et sa proposition préserve ces publics dans le contrat unique ; aucun terme d'emploi n'est créé ici.\n\nLes acquisitions auprès d'une SCI avec 25 % de logements sociaux, durée de dix ans et limite des apports sont conservées. La dispense de révision périodique n'efface ni contrôle ANCOLS ni droits des associés, et L422-12 protège les réserves. Le plafond de 10 % de logements intermédiaires se calcule sur la même définition sociale désormais explicitement au IV de L302-5. Filiales et sociétés conjointement contrôlées conservent l'accès aux aides directes ou indirectes, leurs plafonds de ressources et loyers et les planchers de ces plafonds, leurs mandats, locaux accessoires, apports et prêts ; aucun seuil favorable n'est relevé ou supprimé. L'assimilation des logements et prêts dont le permis a été demandé avant le 1er mars 2014 reste intégrale, de même que le capital d'un euro dans le cas du b. La séparation des fonds, la non-distribution des réserves, les conditions de marché et remboursement et les prix de revient empêchent un détournement des avantages publics sans nouvelle procédure. Les agréments distincts de qualification des opérateurs, conventions et conditions sociales ne sont pas supprimés : ils fondent ces protections, plutôt que des doublons d'autorisation d'opération. Franchise TASCOM et dérogations littorales n'apparaissent pas dans cet article et ne sont pas affectées. Aucun avantage n'est réservé aux seules situations antérieures, hormis les dispositifs dont la source fixe elle-même un champ historique fermé.",
    'substantive_impact': {
        'version': 1,
        'classification': 'material_reduction',
        'assessment': "Par rapport à l'intégralité de la source officielle, la proposition retire plusieurs catégories déterminées d'avis, accords, autorisation, révision périodique et contrôles préalables de filiales, ainsi qu'un filtre géographique ; les deux coupes nouvelles concernent l'accord local du 7° et la preuve exclusive du 6° quater. Les réductions antérieures sont conservées, sans compter chaque renvoi comme une seconde mesure. Le conventionnement et les renvois SRU sont coordonnés, sans gain fiscal propre. Les alinéas maintenus ne sont pas comptés comme simplifiés et aucun résultat national chiffré n'est établi.",
        'scope_limitations': "Lot limité au seul L422-3, dans son champ de coopératives HLM ; les dispositions des autres articles et codes ne sont pas réécrites. Les règlements, clauses types et arrêtés identifiés requièrent leurs coordinations distinctes. Pas d'abolition des agréments d'opérateurs, du conventionnement, des protections immobilières, des aides ou des exigences européennes. Les décisions définitives et engagements antérieurs ont leur transition, l'expérimentation historique n'est pas rouverte. Le coût net des contrôles et le solde des finances publiques restent non établis.",
        'new_burdens_review': "Aucune charge nouvelle identifiée : aucun registre, donnée, attestation, déclaration, consultation, délai minimal ni examen périodique ne remplace les démarches supprimées. Les modes de preuve sont élargis, sans pièce de substitution. Les obligations de comptabilité, plafonds, remboursement, conventionnement et contrôles rappelés existaient dans la source ou les fondements autonomes lus ; le contrôle a priori retiré n'est pas converti en nouveau test général de capacité sociale. Les transitions protègent les contrats et droits antérieurs sans dossier de bascule. Les effets sur les coûts publics et privés de contrôle ne sont pas chiffrés ; aucune réduction nette de charge de l'ensemble des codes n'est affirmée.",
        'effects': effects,
    },
    'reference_checks': reference_checks,
}

Path('answer.json').write_text(json.dumps([answer], ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'output_file': 'answer.json', 'article_count': 1,
                  'paragraphs': len(paragraphs), 'effects': len(effects),
                  'reference_checks': len(reference_checks),
                  'proposed_characters': len(proposed_xml)}, ensure_ascii=False))
