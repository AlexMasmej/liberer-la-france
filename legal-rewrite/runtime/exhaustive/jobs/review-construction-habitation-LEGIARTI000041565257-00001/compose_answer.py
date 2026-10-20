import copy
import html
import json
import re
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
references = json.loads(Path('reference-targets.json').read_text())
answers = []


def impact(classification, assessment, limitations, burdens, effects=None):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=limitations, new_burdens_review=burdens,
                effects=effects or [])


def effect(kind, measure_id, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit,
                affected_population=population, conditions_and_transition=transition,
                replacement_or_new_burdens=burdens, source_quote=source_quote,
                proposed_quote=proposed_quote)


def base(a):
    return {k: a[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}


def retained(a, reason, notes, assessment, limitations, burdens):
    r = base(a)
    r.update(status='retained_unchanged', proposed_xml=None,
             classification='retained_necessary', reason=reason, review_notes=notes,
             substantive_impact=impact('retained_necessary', assessment, limitations, burdens),
             reference_checks=[])
    return r


# L. 126-17 : l'allègement acquis est conservé ; les seuils sanitaires ne sont pas modifiés.
a = sources[0]
r = base(a)
r.update(status='rewrite_draft', proposed_xml=a['previous_draft']['proposed_xml'],
         change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19',
         removed_provisions=["Interdiction de diviser l'ensemble d'un immeuble au seul motif que des logements de catégorie IV loués ou occupés représentent au moins un quart de sa superficie totale."],
         reason="Réduction de fond conservée après comparaison avec la source officielle entière : retrait du critère collectif de catégorie IV au 1°, qui peut bloquer la division de locaux non dangereux en raison du classement d'autres logements. La seconde passe n'ajoute pas de coupe aux 2° et 3° : les dimensions, l'exclusion des parties communes du calcul, l'eau potable, les eaux usées, l'électricité et les diagnostics plomb/amiante protègent directement l'habitabilité et la santé ; la source n'impose pas ici de renouvellement systématique des diagnostics à supprimer. Les interdictions d'habiter, de péril et d'insalubrité sont maintenues, ainsi que la dérogation de restauration déclarée d'utilité publique, ouverte aux opérations futures. Les autres modifications de rédaction du brouillon antérieur sont à droit constant et ne sont pas comptées comme des réductions supplémentaires.",
         review_notes="Source, note de recodification, proposition précédente et texte initial de SRU 74 lus entièrement. Le critère du quart de superficie figure dans l'ancien L. 111-6-1 reproduit ; la filiation de chaque ajout ultérieur, notamment les diagnostics actuels, n'est pas pour autant établie. Les subdivisions 1° à 3°, 14 m2, 33 m3, la conjonction « et », l'exclusion des parties communes et « le cas échéant » sont conservés. L. 313-4 urbanisme, lu intégralement dans le corpus, définit la restauration et son articulation avec la déclaration d'utilité publique ; l'exception source n'est pas restreinte. L. 126-18 à L. 126-20 et L. 183-15 ont été lus : l'autorisation locale et son mois de réponse ne sont pas supprimés ; seul le motif tiré du classement de catégorie IV cesse de fonder le refus. Le bail de l'occupant de bonne foi reste protégé. L. 183-15 incrimine directement les divisions interdites par L. 126-17 et L. 126-21 ; son champ suit la réduction, avec réserve de la loi pénale plus douce. Les renvois existants au code de la santé publique L. 1334-5 et L. 1334-12-1 sont maintenus, mais leurs textes ne sont pas dans les pièces locales autorisées et leur concordance extérieure reste à vérifier ; aucune nouvelle dispense sanitaire n'en est inférée. La transition ne rouvre pas un refus définitif et n'efface pas les droits des occupants. Le 1er juillet 2021 est historique. Aucun achèvement des 209 articles SRU ni de leur filiation exhaustive n'est affirmé.",
         benefit_review="La dérogation permettant la division en lots privatifs et quotes-parts communes pour une restauration immobilière déclarée d'utilité publique demeure au cinquième alinéa, pour les futures opérations recevables aussi. La suppression du seul motif de catégorie IV élargit les divisions possibles ; elle n'abolit ni les droits des occupants ni les règles sanitaires autonomes. Aucun avantage fiscal n'est supprimé.",
         reference_checks=[])
r['substantive_impact'] = impact(
    'material_reduction',
    "Par rapport à toute la source officielle, une interdiction de division fondée sur le classement collectif de catégorie IV est effectivement retirée. Les autres motifs de sécurité et d'habitabilité demeurent ; aucune autorisation locale entière ni taxe n'est supprimée. Cette réduction figurait déjà dans le brouillon et n'est pas revendiquée comme une seconde mesure nouvelle.",
    "Ne couvre ni les locaux dangereux ou dépourvus des équipements maintenus, ni les autorisations autonomes de division ou d'urbanisme. Les effets sur les coûts, les logements produits et l'historique complet des recodifications ne sont pas chiffrés ni démontrés.",
    "Aucune charge nouvelle n'est identifiée : ni dépôt, déclaration, diagnostic supplémentaire ni délai minimal ne remplace le motif retiré. L'application aux demandes en cours ne requiert pas de nouveau dossier et ne recommence pas les délais.",
    [effect('obligation_removed', 'division-fin-interdiction-categorie-iv',
            "Suppression du motif d'interdiction de division tiré du seul classement collectif de catégorie IV.",
            "Division par appartements interdite lorsque les logements loués ou occupés de catégorie IV représentent au moins un quart de la superficie totale de l'immeuble, même sans autre motif établi.",
            "Le classement en catégorie IV ne suffit plus à interdire la division, quelle que soit sa proportion ; les autres interdictions et autorisations autonomes demeurent.",
            'legal_duty', "Propriétaires et opérateurs divisant ces immeubles ; locataires et occupants dont les droits sont conservés.",
            "Divisions réalisées après l'entrée en vigueur et demandes en cours sans nouveau dépôt ; pas de régularisation générale des divisions antérieures, réserve de la loi pénale plus douce.",
            "Aucune déclaration de remplacement ; maintien des équipements, diagnostics et règles autonomes de sécurité.",
            "1° Toute division par appartements d'immeubles qui sont frappés d'une interdiction d'habiter, ou d'un arrêté de péril, ou sont déclarés insalubres, ou comportent pour le quart au moins de leur superficie totale des logements loués ou occupés classés dans la catégorie IV mentionnée par la loi n° 48-1360 du 1er septembre 1948 portant modification et codification de la législation relative aux rapports des bailleurs et locataires ou occupants de locaux d'habitation ou à usage professionnel et instituant des allocations de logement ;",
            "À compter de l'entrée en vigueur de la loi portant la présente réforme, le classement dans la catégorie IV mentionnée par la loi n° 48-1360 du 1er septembre 1948 ne constitue plus, à lui seul, un motif d'interdiction de division, quelle que soit la proportion de la superficie totale de l'immeuble occupée par les logements ainsi classés.")])
answers.append(r)


# L. 126-21 : retour explicite à la source, sans réécriture stylistique comptabilisée.
a = sources[1]
answers.append(retained(a,
    "Maintien intégral de la source après examen de chaque condition et du brouillon antérieur. L'interdiction concerne les immeubles de grande hauteur d'habitation ou mixtes dont la sécurité a fait l'objet d'un avis défavorable ou de prescriptions inexécutées. La division ne doit pas disperser les responsabilités avant la levée de ces risques graves. L'article n'impose ni déclaration périodique, ni taxe, ni nouvelle autorisation autonome ; les deux conditions alternatives restent nécessaires. La reformulation stylistique antérieure n'est pas retenue comme une simplification.",
    "SRU 74, source, note et proposition antérieure lus entièrement : le dernier tiret de l'ancien L. 111-6-1 contient cette interdiction de sécurité, mais ne documente pas toutes les étapes de recodification. Conserver le champ habitation et usages mixtes professionnel ou commercial avec habitation, le contrôle par la commission, l'avis de l'autorité compétente et les prescriptions inexécutées. L. 183-15, lu intégralement, porte directement la sanction ; l'abrogation de L. 126-22 ne la retire pas. Aucun renvoi au contrat de travail. Date historique du 1er juillet 2021 sans portée pour l'entrée en vigueur du projet. Filiation intermédiaire non soldée.",
    "Aucune réduction matérielle : la source entière demeure nécessaire à la sécurité des occupants d'immeubles de grande hauteur. Le contrôle et les prescriptions ne sont pas un doublon documentaire supprimable sur les éléments locaux.",
    "Pas de suppression du contrôle de sécurité, des prescriptions ni de la sanction directe de L. 183-15. L'historique intermédiaire et les effets économiques n'ont pas été établis par ce maintien.",
    "Aucune charge nouvelle n'est identifiée puisque la source est intégralement conservée, sans ajout de pièces, de contrôle, de délai ou de procédure de remplacement."))


# L. 126-22 : retrait d'un renvoi ; aucune dépénalisation prétendue.
a = sources[2]
r = base(a)
r.update(status='rewrite_draft', proposed_xml=a['previous_draft']['proposed_xml'],
         change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19',
         repeal_scope="Suppression du seul renvoi législatif redondant aux peines de L. 183-15 ; ni les interdictions de division maintenues ni l'incrimination et les sanctions directement portées par L. 183-15 ne sont abrogées.",
         reason="Abrogation opératoire du renvoi répétitif, conservée après seconde passe. La lecture entière de L. 183-15 confirme qu'il énonce lui-même les actes, les personnes, les interdictions visées et les sanctions : L. 126-22 n'ajoute aucune condition ou garantie. Cette suppression réduit une répétition normative, mais ne supprime aucune obligation de sécurité ni aucune peine autonome. Il s'agit d'une coordination, distincte de l'allègement matériel de L. 126-17 ; aucune seconde réduction de charge n'est comptée.",
         review_notes="Lecture intégrale des deux versions, de la note et de SRU 74. L. 183-15, source LEGIARTI000041570627 lue dans le corpus autorisé, prévoit directement deux ans d'emprisonnement, 75 000 € et les peines complémentaires dans le même champ. Il demeure opérant sans le présent renvoi. La réduction du motif de catégorie IV de L. 126-17 doit être prise en compte dans les procédures pénales selon la loi plus douce ; l'abrogation du seul renvoi ne constitue pas une abolition d'infraction. Le texte SRU initial ne démontre pas la création de ce renvoi autonome : filiation non soldée. Le contrôle local des mentions de L. 126-22 dans les fichiers du corpus n'a relevé aucun autre article source le visant ; les textes extérieurs ne sont pas réputés exhaustivement contrôlés. Aucun droit des victimes ni condamnation définitive n'est effacé. La note du 1er juillet 2021 est historique.",
         reference_checks=[])
r['substantive_impact'] = impact(
    'coordination_only',
    "L'article entier est abrogé mais ne portait qu'un renvoi. L'incrimination et toutes les peines sont directement maintenues dans L. 183-15 : aucune obligation ni peine supplémentaire supprimée n'est dénombrée.",
    "Cette coordination ne diminue pas les exigences sanitaires et ne dépénalise pas les divisions encore interdites. Le contrôle des textes extérieurs au corpus et l'historique de création du renvoi restent incomplets.",
    "Aucune charge nouvelle n'est identifiée : le renvoi disparaît sans déclaration, registre, autorisation ou contrôle substitué. La sanction continue de reposer sur son article autonome.",
    [effect('coordination', 'division-sanctions-renvoi-unique',
            "Retrait de la répétition des sanctions directement prévues par L. 183-15, sans diminution propre de leur champ.",
            "L. 126-22 renvoie à L. 183-15, qui définit déjà directement la même infraction.",
            "L. 126-22 est abrogé ; l'incrimination et les peines directes de L. 183-15 restent applicables dans le champ des interdictions maintenues.",
            'other', "Personnes mettant les locaux issus d'une division interdite en vente, en location ou à disposition ; autorités de poursuite et victimes.",
            "Abrogation à l'entrée en vigueur ; sanctions directes antérieures et futures conservées, avec la loi pénale plus douce applicable aux changements matériels des interdictions.",
            "Aucun dispositif de remplacement ni nouvelle obligation ; pas de seconde suppression de sanction.",
            "Les personnes qui mettent en vente, en location ou à la disposition d'autrui des locaux destinés à l'habitation et provenant d'une division réalisée en méconnaissance des interdictions définies aux articles L. 126-17 et L. 126-21 encourent les peines prévues par l'article L. 183-15.",
            "Elle ne supprime ni l'incrimination ni les peines directement prévues par cet article, qui demeurent applicables aux faits antérieurs et postérieurs à cette entrée en vigueur dans le champ des interdictions des articles L. 126-17 et L. 126-21.")])
answers.append(r)


# L. 184-1 : police essentielle, source entière.
a = sources[3]
answers.append(retained(a,
    "Maintien intégral après réexamen réel de l'arrêté, de la mise en demeure, des travaux d'office, de la provision et du recouvrement. L'arrêté précise les mesures pour faire cesser l'insécurité constatée ; la mise en demeure, après défaut d'exécution volontaire, est une garantie avant une intervention forcée aux frais des propriétaires, et non une seconde déclaration à leur charge. Aucun délai minimal général ni dossier renouvelé n'est imposé ici. Les travaux d'office empêchent la persistance d'un risque manifeste ; la provision et le recouvrement protègent les fonds publics ; le juge règle l'accès contesté. Interdiction temporaire, hébergement et relogement sont essentiels pour les occupants. La différence entre provision de l'exploitant et dépenses aux frais des propriétaires est maintenue sans réécriture stylistique.",
    "Source, note, précédent brouillon et SRU 178 lus entièrement. Le texte initial de l'ancien L. 123-3 contient une partie des pouvoirs ; les ajouts relatifs notamment au propriétaire, à l'interdiction temporaire et à Paris ne peuvent lui être attribués sans historique complémentaire. Les cinq alinéas source restent intacts, spécialement le troisième visé au 2° de L. 184-6. L. 521-1, L. 521-2, L. 521-3-1 et L. 521-3-2, lus intégralement, préservent les occupants futurs, la suspension des loyers dans son champ, l'hébergement, le relogement et la substitution publique. R. 321-15 et R. 523-1 ont été lus : les aides ne sont pas fermées. R. 523-1 conserve un ancien renvoi à L. 123-3 alors que le L. 123-3 actuel lu concerne les responsabilités de construction ; coordination hors lot à effectuer vers la police recodifiée, après contrôle historique, sans supprimer l'aide. Cet article extérieur au lot n'est pas modifié. Le maintien ne recrée ni quotas SRU ni nouvelles sanctions. Le 1er juillet 2021 est une date historique.",
    "Aucune réduction comptée : prescription des mesures, étape préalable à l'exécution forcée, contrôle de l'accès, recouvrement et protection des occupants remplissent chacun une fonction de sécurité ou de garantie distincte.",
    "Les coûts des travaux et du relogement restent à la charge déterminée par les textes. Le renvoi ancien du règlement d'aide R. 523-1 et la filiation complète des ajouts ne sont pas soldés dans ce lot.",
    "Aucune charge nouvelle n'est identifiée : la source entière reste applicable, sans nouvelle notification, pièce, condition d'aide ou formalité. Aucune recette de compensation n'est créée."))


# L. 184-2 : notifications protectrices et indivision.
a = sources[4]
answers.append(retained(a,
    "Maintien intégral de l'information sur l'astreinte et de la notification à chacun des deux débiteurs avant solidarité. Ces actes portent respectivement sur la prescription et sur l'application effective de l'astreinte ; leur objet n'est pas identique. En supprimer un affaiblirait l'information préalable ou l'opposabilité personnelle de la dette. Le renvoi spécial à l'indivision permet une application cohérente sans dossier distinct. Ni taxe autonome ni déclaration périodique ne sont créées par cet article. L'allègement pécuniaire est porté par L. 184-3 et bénéficie aussi aux cas d'indivision visés, sans modification stylistique du présent article.",
    "Les deux alinéas, la source, sa note, le brouillon et SRU 178 ont été lus. Le régime d'astreinte ne figure pas dans le texte SRU initial fourni : filiation ultérieure à documenter. L. 541-2-1, lu intégralement, renvoie au troisième alinéa à L. 184-3 pour l'astreinte, sa liquidation et son recouvrement ; l'exonération obligatoire nouvelle s'y applique dans le même champ. Il ne faut pas l'étendre au régime autonome de L. 511-15. Le premier arrêté avertit ; le second applique l'astreinte et doit être notifié à chacun : aucun renouvellement de notification n'est imposé par la révision de L. 184-3. L'exclusion nouvelle de sûreté spéciale de l'astreinte n'efface pas cette solidarité ni les dettes de travaux ou de relogement. Date de 2021 historique, non date de réforme.",
    "Aucun allègement autonome : conservation des garanties d'information et de notification qui conditionnent la solidarité, et du renvoi utile à l'indivision. L'article reste cohérent avec les réductions de L. 184-3.",
    "Ne supprime ni solidarité, ni arrêté d'application de l'astreinte, ni notification personnelle. L'histoire détaillée de l'introduction de ce mécanisme n'est pas fournie ; aucune réduction globale de coût n'est démontrée.",
    "Aucune charge nouvelle n'est identifiée car aucune formalité n'est ajoutée à la source, notamment aucune nouvelle notification pour bénéficier des dispositions plus favorables de L. 184-3."))


# L. 184-3 : avantages acquis, transfert financier correctement qualifié,
# et suppression supplémentaire de la sûreté spéciale de la seule astreinte.
a = sources[5]
r = base(a)
proposed = a['previous_draft']['proposed_xml']
old = "Dans ce cas, son montant s'ajoute au coût des mesures et travaux exécutés d'office et bénéficie de la garantie prévue au 8° de l'article 2374 du code civil. Les articles L. 541-1 et suivants du présent code s'appliquent."
new = "Dans ce cas, son montant s'ajoute au coût des mesures et travaux exécutés d'office. Aucune sûreté immobilière spéciale ne garantit le montant de l'astreinte prononcée en application du présent article. Cette exclusion ne supprime pas les sûretés garantissant le coût des mesures et travaux exécutés d'office ou les frais d'hébergement et de relogement. Les articles L. 541-1 et suivants du présent code s'appliquent sous réserve de cette exclusion pour l'astreinte."
assert old in proposed
proposed = proposed.replace(old, new)
old = "L'exonération obligatoire prévue au quatrième alinéa et la suppression du prélèvement pour frais de recouvrement prévue au sixième alinéa s'appliquent aux sommes correspondant aux jours de retard à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris lorsque l'arrêté est antérieur. Les sommes correspondant aux jours de retard antérieurs, leur liquidation, leur recouvrement, leur affectation et les recours les concernant restent régis par les dispositions antérieures. La présente réforme n'institue aucun remboursement général de sommes antérieurement acquittées et ne supprime ni les travaux prescrits ni leur exécution d'office."
new = "L'exonération obligatoire prévue au quatrième alinéa, la suppression du prélèvement pour frais de recouvrement prévue au sixième alinéa et l'exclusion de sûreté immobilière spéciale prévue au septième alinéa s'appliquent aux sommes correspondant aux jours de retard à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris lorsque l'arrêté est antérieur. Les sommes correspondant aux jours de retard antérieurs, leur liquidation, leur recouvrement, leur affectation, les sûretés les garantissant et les recours les concernant restent régis par les dispositions antérieures. Les sûretés de ces sommes antérieures ne s'étendent pas aux sommes correspondant aux jours de retard à compter de cette entrée en vigueur. La présente réforme n'institue aucun remboursement général de sommes antérieurement acquittées et ne supprime ni les travaux prescrits ni leur exécution d'office."
assert old in proposed
proposed = proposed.replace(old, new)
r.update(status='rewrite_draft', proposed_xml=proposed,
         change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19',
         removed_provisions=[
             "Faculté de maintenir l'astreinte pour les retards dont le redevable établit qu'ils ne sont pas de son fait : cette part est désormais obligatoirement exonérée, avec maintien des remises plus étendues.",
             "Prélèvement de 4 % pour frais de recouvrement sur les sommes recouvrées par l'État et affectées à l'ANAH ; ce retrait modifie une répartition publique sans diminuer le montant dû par le redevable.",
             "Garantie immobilière spéciale du montant de l'astreinte ajouté au coût des travaux d'office, pour les jours de retard nouveaux ; les sûretés des dépenses réelles de travaux, d'hébergement ou de relogement ne sont pas supprimées."],
         reason="Réduction de fond complétée lors de la seconde passe : suppression de la sûreté immobilière spéciale de la seule astreinte. Elle ajoute une garantie patrimoniale au titre exécutoire, à la solidarité des débiteurs, à la possibilité de travaux d'office et à la sanction pénale du refus délibéré ; elle n'est pas nécessaire pour garantir le remboursement des dépenses réelles, dont les sûretés sont expressément préservées. Cette suppression évite de reconduire le renvoi civil source non coordonné, sans inventer son numéro successeur. Les deux réformes antérieures sont conservées : droit à l'exonération pour les retards non imputables au redevable, avec possibilité de remise plus étendue jusqu'à la totalité ; retrait des 4 % de frais prélevés par l'État sur le produit revenant à l'ANAH. Ce dernier retrait constitue une réaffectation entre organismes publics, non une baisse de la dette privée ni une économie nationale. Les plafonds, la modulation selon la gravité, les garanties de notification, le rythme trimestriel et la cessation lors de la notification d'exécution d'office restent nécessaires. Les autres changements de formulation n'ont pas d'effet de réduction démontré.",
         review_notes="Source entière, note, ancien projet et SRU 178 lus : le régime d'astreinte n'est pas dans ce texte initial et sa filiation n'est pas réputée démontrée. Les sept alinéas matériels restent dans l'ordre ; transition au huitième. Maintien de 1 000 € par jour, de la modulation, du plafond total par L. 184-4 maintenu à 50 000 €, du trimestre échu et du mois suivant la demande du préfet avant substitution de l'État. Les 4 % disparaissent seulement pour les jours de retard nouveaux : versement de 100 % du produit correspondant à l'ANAH au lieu de 96 %, sans changement de la dette privée par ce seul effet. L'exonération minimale devient obligatoire sur preuve déjà requise ; la remise partielle ou totale plus large demeure possible. Les retards anciens restent sous le droit antérieur, y compris leurs exonérations et sûretés ; pas de restitution générale. L. 541-1 à L. 541-6 ont été lus intégralement. Leurs solidarités et règles de recouvrement restent, mais ne peuvent recréer une sûreté spéciale pour la nouvelle astreinte ; L. 541-4 ne peut en transférer la charge sur un repreneur pour ces sommes. Les créances de dépenses réelles et leurs garanties ne sont pas supprimées. Le renvoi source au 8° de l'article 2374 civil, également présent dans L. 541-4, n'est pas reconduit : le rattachement spécial de l'astreinte est expressément retiré. Des articles CCH lus dans le corpus citent déjà 2402 dans d'autres champs ; ils ne prouvent pas le contenu exact du texte civil ni sa portée pour cette astreinte. Aucun numéro ni contenu civil de remplacement n'est inventé. Coordination extérieure à prévoir dans le code civil et les textes de publicité des sûretés, afin d'exclure explicitement les créances d'astreinte de L. 184-3 nouvelles tout en conservant les dettes anciennes et les garanties des travaux et du relogement ; ces textes absents ne sont pas présentés comme réécrits. Le 1° de L. 541-1 vise L. 184-1 plutôt que L. 184-3 : renvoi imprécis préexistant, n'élargissant pas le régime à L. 511-15. Le CGCT L. 5211-9-2 reste un renvoi existant hors corpus à contrôler, sans nouvelle compétence créée. Coût du recouvrement restant public et perte éventuelle de priorité de l'astreinte à évaluer ; aucun rendement net ni compensation présumés. La date de 2021 dans la note est historique.",
         benefit_review="L'exonération partielle ou totale pour circonstances non imputables est conservée et renforcée pour les jours de retard futurs : la part justifiée doit être exonérée, et la remise peut toujours aller jusqu'à la totalité. Elle reste ouverte aux futurs redevables et aux arrêtés antérieurs pour leurs nouveaux jours de retard. Les anciennes sommes gardent leur faculté d'exonération et leurs recours. La modulation selon l'ampleur et les conséquences, le plafond journalier de 1 000 €, le plafond total égal à l'amende de L. 184-4, le recouvrement par trimestre échu et la fin de l'astreinte lors de la notification de l'exécution d'office demeurent. Le retrait des 4 % améliore l'affectation à l'ANAH mais n'est pas une exonération du débiteur. L'exclusion de sûreté spéciale allège seulement la garantie patrimoniale de l'astreinte ; elle n'enlève ni sûretés des dépenses réelles, ni aides au logement, ni obligations de mise en sécurité.",
         reference_checks=[])
relief_source = "Le maire peut, lors de la liquidation trimestrielle de l'astreinte, consentir une exonération partielle ou totale de son produit si le redevable établit que la non-exécution de l'intégralité de ses obligations est due à des circonstances qui ne sont pas de son fait."
relief_proposed = "L'exonération couvre au moins les sommes correspondant aux retards ainsi justifiés."
r['substantive_impact'] = impact(
    'mixed',
    "La comparaison à la source entière établit un droit à remise pour les retards non imputables, le retrait d'une sûreté immobilière spéciale de l'astreinte et un transfert de 4 % de recettes de l'État à l'ANAH. La décision d'exonération minimale lie désormais le maire ; cette obligation administrative réciproque est recensée. Seule la sûreté est une coupe supplémentaire au brouillon. Le solde net de coût public et privé n'est pas établi.",
    "L'astreinte demeure pour les retards imputables, dans les limites de 1 000 € par jour et du total de 50 000 €. Les sûretés des travaux et du relogement restent ; les jours anciens gardent leur droit et leurs garanties. Le code civil, les textes de publicité et les règles financières extérieures doivent encore être coordonnés ; ni effets de recouvrement ni coût budgétaire net ne sont chiffrés.",
    "Le maire doit accorder la remise minimale lorsque la preuve déjà exigée est apportée : obligation juridique nouvelle pour l'autorité, sans nouvelle déclaration ou pièce imposée au redevable. Aucun registre, délai minimal ou sûreté de remplacement n'est créé. Les 4 % retirés ne suppriment pas le travail de recouvrement de l'État ; son financement n'est pas présumé résolu.",
    [effect('relief_extended', 'astreinte-erp-exoneration-retards-non-imputables',
            "La remise devient un droit pour la fraction des retards non imputables, avec maintien d'une remise plus large.",
            "Remise partielle ou totale seulement facultative lors de la liquidation trimestrielle, même lorsque la non-exécution n'est pas du fait du redevable ; astreinte maximale 1 000 € par jour, total plafonné à l'amende de 50 000 €.",
            "Remise obligatoire au moins pour les retards ainsi justifiés ; remise jusqu'à la totalité toujours possible. Aucun changement des plafonds de 1 000 € par jour et 50 000 € au total.",
            'legal_duty', "Exploitants et propriétaires redevables, y compris indivisaires relevant du renvoi à L. 184-3.",
            "Jours de retard à compter de l'entrée en vigueur, même pour un arrêté antérieur ; preuve de circonstances non imputables maintenue. Anciennes sommes sous droit antérieur.",
            "Pas de nouvelle pièce légalement définie ; le maire est désormais tenu d'accorder la remise minimale, effet réciproque recensé sous la même mesure.",
            relief_source, relief_proposed),
     effect('obligation_added', 'astreinte-erp-exoneration-retards-non-imputables',
            "Conséquence administrative de la même extension de droit : l'autorité ne peut plus refuser la remise minimale établie.",
            "Le maire disposait d'une faculté de remise, même si les circonstances non imputables étaient prouvées.",
            "Il doit accorder au minimum l'exonération correspondant aux retards non imputables ; la faculté plus favorable demeure.",
            'legal_duty', "Maire ou autorité compétente liquidant l'astreinte de L. 184-3.",
            "Même champ et transition que le droit à exonération ; ce n'est pas une seconde réduction indépendante.",
            "Décision liée sur le minimum de remise ; pas de nouveau rapport, registre ou circuit d'autorisation.",
            relief_source,
            "Lors de la liquidation trimestrielle de l'astreinte, le maire accorde une exonération partielle ou totale de son produit lorsque le redevable établit que la non-exécution de l'intégralité de ses obligations est due à des circonstances qui ne sont pas de son fait."),
     effect('financing_transfer', 'astreinte-erp-suppression-frais-recouvrement',
            "Suppression de la retenue de recouvrement entre administrations ; pas de baisse de la dette du redevable.",
            "Sur le produit d'astreinte effectivement recouvré par l'État en substitution, 4 % sont prélevés pour frais et 96 % reviennent à l'ANAH.",
            "Aucune retenue : 100 % du même produit revient à l'ANAH ; le débiteur paie la même astreinte hors effet distinct des exonérations.",
            'financing', "État chargé du recouvrement et ANAH bénéficiaire ; redevables sans réduction de dette par cette seule répartition.",
            "Part correspondant aux jours de retard futurs ; affectation des jours anciens préservée même si le recouvrement intervient ensuite.",
            "Le recouvrement demeure à effectuer par l'État sans ces 4 % ; aucune ressource de remplacement n'est instituée et le solde public consolidé n'est pas chiffré.",
            "Après prélèvement de 4 % pour frais de recouvrement, les sommes perçues sont versées au budget de l'Agence nationale de l'habitat.",
            "Les sommes perçues sont intégralement versées au budget de l'Agence nationale de l'habitat, sans prélèvement pour frais de recouvrement."),
     effect('obligation_removed', 'astreinte-erp-fin-surete-immobiliere-speciale',
            "Retrait de la garantie immobilière spéciale de l'astreinte ; les garanties des dépenses réelles demeurent.",
            "En cas d'exécution d'office, le montant de l'astreinte ajouté aux travaux bénéficie de la garantie spéciale désignée par le renvoi civil source.",
            "L'astreinte de L. 184-3 n'est plus garantie par une sûreté immobilière spéciale pour ses jours nouveaux ; dette, solidarité et recouvrement subsistent. Les garanties des travaux et du relogement sont conservées.",
            'legal_duty', "Propriétaires redevables et personnes exposées aux effets immobiliers de la sûreté spéciale ; créanciers publics pour la seule astreinte.",
            "Jours de retard à compter de l'entrée en vigueur, même avec un arrêté ancien ; sûretés des sommes relatives aux jours antérieurs préservées sans extension aux sommes nouvelles.",
            "Aucune sûreté ou formalité de remplacement créée ; coordination civile et de publicité à effectuer hors lot, effet net sur le recouvrement non mesuré.",
            "Dans ce cas, le montant de l'astreinte, qui s'ajoute à celui du coût des mesures et des travaux exécutés d'office, est garanti par les dispositions prévues au 8° de l'article 2374 du code civil.",
            "Aucune sûreté immobilière spéciale ne garantit le montant de l'astreinte prononcée en application du présent article.")])
answers.append(r)


# L. 184-4 : l'amende garde également sa fonction de plafond.
a = sources[6]
answers.append(retained(a,
    "Maintien intégral après examen de l'incrimination et du projet antérieur. Elle vise un refus délibéré, sans motif légitime, constaté après mise en demeure, d'exécuter des travaux nécessaires à la sécurité. Ces conditions cumulatives écartent la simple difficulté d'exécution et protègent la défense ; l'infraction ne double pas une déclaration administrative mais sanctionne une obstruction dangereuse. Les peines principales restent nécessaires ; le montant de l'amende borne également l'astreinte de L. 184-3. Aucune reformulation stylistique n'est comptée comme réécriture ni comme réduction.",
    "Source, note et brouillon lus entièrement, ainsi que SRU 178 : cette peine n'est pas dans le texte initial fourni, et son origine détaillée reste à documenter. Conserver un an d'emprisonnement, 50 000 €, refus délibéré, absence de motif légitime et constat après mise en demeure. Le renvoi à L. 184-1 demeure cohérent, son corps étant maintenu intégralement. La remise plus favorable de l'astreinte et l'exclusion de sa sûreté n'abolissent pas les éléments de cette infraction autonome. L. 184-7 rend facultatives certaines peines complémentaires des personnes physiques ; la proposition de L. 184-8 lue dans le corpus traite séparément les personnes morales, sans être réécrite ici. Aucune rétroactivité nouvelle ni changement du plafond total d'astreinte. Date de 2021 historique.",
    "Aucune réduction comptée : le refus délibéré de travaux de sécurité demeure pénalement sanctionné avec ses garanties cumulatives. Le plafond de 50 000 € conserve son rôle favorable de limite totale de l'astreinte.",
    "Ne supprime ni la peine principale ni les travaux. Les conséquences budgétaires et l'historique complet de l'incrimination ne sont pas établis ; la réforme des peines complémentaires a son champ propre.",
    "Aucune charge nouvelle n'est identifiée : texte source entièrement maintenu, sans pièce justificative, notification supplémentaire, délai nouveau ni extension d'infraction."))


# L. 184-5 : suroccupation manifeste.
a = sources[7]
answers.append(retained(a,
    "Maintien intégral de la protection contre la location conduisant manifestement à la suroccupation. Ce comportement présente un risque sanitaire et de sécurité propre, distinct du refus de travaux et du classement historique de catégorie IV. La source n'impose aucun formulaire, agrément, rapport périodique ou prélèvement dont la fonction serait à retirer. Le caractère manifeste limite déjà l'incrimination ; supprimer celle-ci au titre de l'allègement général supprimerait une protection essentielle des occupants. La reformulation antérieure n'apporte pas de réduction et n'est pas reconduite comme nouveau corps.",
    "Lecture intégrale de la source, de la note, du brouillon et de SRU 178. Le texte initial fourni ne comporte pas cette infraction : sa filiation ne peut être déclarée achevée. Deux ans d'emprisonnement, 75 000 € et « manifestement » sont conservés, sans seuil de surface ou nombre d'occupants inventé. Aucun renvoi incohérent dans cet alinéa unique. Le retrait du motif collectif de catégorie IV à L. 126-17 ne vaut pas autorisation de suroccuper. Les peines complémentaires des personnes physiques sont régies par L. 184-7 ; la proposition distincte de L. 184-8 ne doit pas être tenue pour du droit en vigueur. Le 1er juillet 2021 reste une date historique.",
    "Aucun allègement matériel : maintien d'une incrimination ciblée sur les conditions conduisant manifestement à la suroccupation, sans inventer un nouveau seuil ni un coût de conformité supprimé.",
    "Aucune dépénalisation de la suroccupation ni modification de peine principale. La filiation historique intégrale et les effets quantifiés sur les occupants et bailleurs ne sont pas établis.",
    "Aucune charge nouvelle n'est identifiée : la source reste entière, sans nouveau contrôle, registre, justificatif, seuil ou délai ajouté au comportement déjà interdit."))


# L. 184-6 : conservation sans changement du brouillon, réparation syntaxique signalée.
a = sources[8]
r = base(a)
r.update(status='rewrite_draft', proposed_xml=a['previous_draft']['proposed_xml'],
         classification='editorial_only',
         reason="Conservation sans nouvelle modification du brouillon antérieur ; aucune réduction de fond n'est revendiquée. Les dégradations destinées à faire partir les occupants et le non-respect de mauvaise foi d'une interdiction de sécurité doivent rester sanctionnés. Le texte ne porte ni taxe ni formalité administrative à supprimer. Le brouillon clarifie la syntaxe et corrige expressément la séquence matériellement défectueuse du 1° ; cela ne constitue ni une simplification de charge ni une preuve que le champ pénal authentique a été vérifié.",
         review_notes="Source, note, proposition antérieure et SRU 178 intégralement lus. Le texte source porte « lorsque ces locaux sont mentionnés les lieux par un arrêté ». Le brouillon maintenu retient « lorsque ces locaux sont mentionnés dans un arrêté » : correction explicite proposée, dont la portée reste à confronter au texte authentique absent des pièces ; aucune authentification ni validation juridique n'est affirmée. Au 2°, conserver « et » entre habiter et utiliser, bien que le troisième alinéa de L. 184-1 porte « ou » : incohérence source signalée, sans extension pénale implicite. Le troisième alinéa de L. 184-1 est intact et le renvoi ordinal demeure exact. Trois ans d'emprisonnement, 100 000 €, finalité d'éviction, mauvaise foi, 1° et 2° restent. Ces incriminations ne figurent pas dans SRU 178 initial : filiation non soldée. Aucun nouveau renvoi, régime de travail ou délai n'est ajouté. La note de 2021 est historique.",
         substantive_impact=impact(
             'editorial_only',
             "Aucun changement normatif de réduction démontré par rapport à la source entière. Le brouillon antérieur est reproduit sans modification nouvelle ; sa correction syntaxique signalée ne supprime ni infraction, ni obligation, ni peine.",
             "Le passage défectueux du 1° requiert une confrontation documentaire extérieure ; le « et » du 2° et le « ou » du texte visé ne sont pas harmonisés. Aucune filiation historique complète ni baisse de complexité n'est démontrée.",
             "Aucune charge nouvelle n'est identifiée dans la proposition conservée : aucune pièce, autorisation, donnée, condition ou durée n'est ajoutée. La correction syntaxique ne doit pas être interprétée comme un élargissement tacite de l'infraction."),
         reference_checks=[])
answers.append(r)


# L. 184-7 : suppression acquise de l'automatisme, contrôles des trois cibles exactes.
a = sources[9]
r = base(a)
r.update(status='rewrite_draft', proposed_xml=a['previous_draft']['proposed_xml'],
         change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19',
         removed_provisions=[
             "Prononcé obligatoire des peines complémentaires de confiscation du 1° et d'interdiction d'achat ou d'usufruit du 3°, remplacé par la faculté d'individualisation de la juridiction.",
             "Exigence d'une motivation spécialement renforcée pour décider de ne pas prononcer les peines des 1° et 3°, sans suppression de la motivation juridictionnelle de droit commun."],
         reason="Réduction de fond acquise conservée : fin de l'obligation de prononcer confiscation et interdiction d'achat ou d'usufruit, ainsi que de la motivation spéciale de leur non-prononcé. Le juge garde ces sanctions pour répondre à la gravité et à la personnalité de l'auteur ; les retirer entièrement affaiblirait la réponse aux infractions de sécurité et d'éviction forcée. La seconde passe maintient donc les objets, durées maximales, conditions et exceptions protectrices, notamment occupation personnelle et mandats électifs ou responsabilités syndicales. Elle n'ajoute pas de coupe arbitraire aux peines individualisables. Les phrases simplifiées restent à droit constant sur ces points et ne sont pas dénombrées comme des réductions distinctes.",
         review_notes="Source entière et précédent brouillon lus, absence de note source constatée ; SRU 178 lu, sans preuve de filiation de cette liste ou de son automatisme. Le champ final du « présent chapitre » est conservé, sans le réduire silencieusement aux articles d'ouverture. Maintien des cinq alinéas matériels et transition au sixième ; cinq ans et dix ans au plus, facilités sciemment utilisées, exception élective/syndicale, SCI ou société en nom collectif, parts immobilières, occupation personnelle, propriété au moment des faits et égalité avec l'indemnité d'expropriation restent intacts. L. 551-1, lu intégralement, contrôle les condamnations effectivement prononcées et définitives ; il ne rend pas à nouveau obligatoire la peine et conserve son exception d'occupation personnelle. L. 184-8 et sa proposition ont été lus : la coordination des personnes morales reste distincte et aucun droit proposé n'est présenté comme en vigueur. Le renvoi existant au dixième alinéa de l'article 131-21 pénal demeure à contrôler sur texte extérieur non fourni, notamment son ordinal selon les versions ; aucune concordance extérieure ni contenu substitué ne sont inventés. Il n'est pas démontré localement incohérent. Application plus douce aux faits antérieurs non définitivement jugés, sans annuler les condamnations définitives ni les droits des victimes. Les trois cibles obligatoires du travail sont examinées ci-dessous malgré l'absence de renvoi à ces articles dans la source : l'activité professionnelle du 2° désigne une peine, non la durée d'emploi ou une rupture de contrat. Aucune condition d'ancienneté, indemnité ordinaire, notification de rupture ou suppression de CDD n'est importée dans cette peine. La date de version du 26 juin 2024 ne fixe pas la réforme. Filiation SRU non soldée.",
         benefit_review="Les exceptions favorables à l'exercice d'un mandat électif et de responsabilités syndicales restent au 2°. L'exclusion de l'achat ou de l'usufruit pour occupation personnelle reste au 3°, pour les situations futures aussi. La possibilité de ne pas prononcer les peines des 1° et 3° est élargie, et non supprimée avec l'ancien automatisme. La limitation de la confiscation en valeur à l'indemnité d'expropriation dans le cas prévu, les durées maximales de cinq et dix ans, les circonstances et la personnalité restent prises en compte. Aucun avantage fiscal ou droit de contrat de travail n'est supprimé.")
r['substantive_impact'] = impact(
    'material_reduction',
    "La source officielle entière imposait par principe deux peines complémentaires avec une motivation spéciale pour y déroger. La proposition les rend facultatives et retire ce surcroît de motivation, sans abolir les sanctions disponibles ni les infractions. Cet allègement figurait déjà dans le brouillon ; aucun nouveau gain n'est attribué à la seconde passe.",
    "Personnes physiques seulement ; les personnes morales relèvent de L. 184-8. Les peines principales, condamnations définitives et contrôles notariaux des peines effectivement prononcées restent. L'ordinal du renvoi pénal extérieur et la filiation historique complète ne sont pas authentifiés localement.",
    "Aucune charge nouvelle n'est identifiée : pas de registre, autorisation, déclaration ni demande de dispense substituée. Les règles générales de motivation et les contrôles des peines prononcées existaient déjà et ne deviennent pas une procédure de remplacement.",
    [effect('obligation_removed', 'habitat-sanctions-complementaires-facultatives',
            "Fin du prononcé obligatoire de la confiscation et de l'interdiction d'achat ou d'usufruit pour les personnes physiques.",
            "Peines des 1° et 3° obligatoires pour les personnes coupables dans le champ du chapitre, sauf décision spécialement motivée ; interdiction du 3° limitée à dix ans avec exception d'occupation personnelle.",
            "Peines des 1° et 3° facultatives selon circonstances et personnalité, sans motivation spéciale pour leur non-prononcé ; objets, maxima et exceptions identiques, dont dix ans et occupation personnelle.",
            'legal_duty', "Personnes physiques poursuivies pour les infractions visées par le chapitre et juridictions pénales.",
            "Infractions futures et infractions antérieures non définitivement jugées dans les conditions de la loi pénale plus douce ; droits des victimes et condamnations définitives préservés.",
            "Aucune demande de dispense nouvelle ; motivation générale des décisions maintenue. La même mesure inclut le retrait de la motivation spéciale, sans compter une seconde peine supprimée.",
            "Le prononcé des peines complémentaires mentionnées aux 1° et 3° est obligatoire à l'encontre de toute personne coupable d'une infraction prévue par le présent chapitre.",
            "Leur prononcé n'est pas obligatoire et la décision de ne pas les prononcer n'exige pas de motivation spéciale au titre du présent article, sans préjudice des règles générales de motivation des décisions juridictionnelles.")])
checks = [
    "L. 1234-1 fixe le préavis de licenciement : la source distingue moins de six mois, six mois à moins de deux ans et au moins deux ans ; la proposition ouvre quinze jours calendaires aux nouveaux contrats sans condition d'ancienneté et conserve les anciens préavis. L. 184-7 n'y renvoie pas : les cinq ans du 2° sont une durée maximale de peine d'interdiction professionnelle, pas un préavis. Aucune notification de rupture ni dispense pour faute grave n'est transposée ; les autorisations et procédures collectives distinctes ne sont pas affectées.",
    "L. 1221-2 proposé impose l'emploi nouveau à durée indéterminée, sans fin automatique de mission ou de formation, et protège les contrats antérieurs sans nouveau renouvellement de CDD. L. 184-7 n'a aucun renvoi à cette cible et son 2° ne crée pas de contrat d'emploi : il décrit une peine professionnelle, avec exceptions électives et syndicales. Le contrat unique n'est donc pas une coordination à insérer ici ; aucune ancienneté ni notification d'embauche ou de rupture n'est ajoutée et aucun CDD spécial n'est rétabli.",
    "L. 1234-9 actuel ouvre l'indemnité du CDI à huit mois sous réserve de faute grave ; sa proposition vise l'employeur rompant un contrat unique après un an mesuré au terme effectif, préavis compris, puis 0,20 mois par année totale avec mois complets au prorata et plafond de six mois, en préservant les anciennes composantes et indemnités spéciales. L. 184-7 ne renvoie à aucune de ces règles : confiscation et interdiction d'acquérir sont des peines, non une indemnité de rupture. Aucun seuil d'ancienneté ou condition de notification de licenciement n'est applicable à leur prononcé ; droits des victimes et règles d'emploi restent distincts."
]
required = references['requirements'][a['code_id'] + '|' + a['source_id']]
r['reference_checks'] = [dict(target_key=k, view_sha256=references['targets'][k]['view_sha256'],
                              assessment=checks[i]) for i, k in enumerate(required)]
answers.append(r)

Path('answer.json').write_text(json.dumps(answers, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json: {len(answers)} articles')
