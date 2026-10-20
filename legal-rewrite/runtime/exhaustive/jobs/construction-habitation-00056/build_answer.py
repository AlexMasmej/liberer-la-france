import json
import re
from html import unescape
from pathlib import Path


SOURCES = json.loads(Path('source.json').read_text())
REFERENCES = json.loads(Path('reference-targets.json').read_text())
BY_NUMBER = {a['number']: a for a in SOURCES}
ANSWERS = {}


def plain(xml):
    return unescape(re.sub(r'<[^>]*>', '', xml or ''))


def base(number, reason, review, benefit):
    source = BY_NUMBER[number]
    return {
        **{k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')},
        'reason': reason,
        'review_notes': review,
        'benefit_review': benefit,
    }


def effect(kind, measure_id, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    return {
        'kind': kind, 'measure_id': measure_id, 'description': description,
        'before': before, 'after': after, 'unit': unit,
        'affected_population': population, 'conditions_and_transition': transition,
        'replacement_or_new_burdens': burdens,
        'source_quote': source_quote, 'proposed_quote': proposed_quote,
    }


def retain(number, reason, review, benefit, assessment, scope, burdens):
    a = base(number, reason, review, benefit)
    a.update(proposed_xml=None, status='retained_unchanged', classification='retained_necessary')
    a['substantive_impact'] = {
        'version': 1, 'classification': 'retained_necessary',
        'assessment': assessment, 'scope_limitations': scope,
        'new_burdens_review': burdens, 'effects': [],
    }
    ANSWERS[number] = a


def rewrite(number, xml, reason, review, benefit, classification,
            assessment, scope, burdens, effects, removed=None, repeal=None):
    a = base(number, reason, review, benefit)
    a.update(proposed_xml=xml, status='rewrite_draft')
    if removed:
        a.update(change_type='normative_reduction',
                 reform_policy_id='editorial_direction_2026_10_19',
                 removed_provisions=removed)
    if repeal:
        a.update(change_type='full_repeal',
                 repeal_policy_id='editorial_direction_2026_10_19',
                 repeal_scope=repeal)
    a['substantive_impact'] = {
        'version': 1, 'classification': classification,
        'assessment': assessment, 'scope_limitations': scope,
        'new_burdens_review': burdens, 'effects': effects,
    }
    ANSWERS[number] = a


retain(
    'L522-1',
    "Maintien intégral après examen : la prise en charge par l'Etat ou ses opérateurs de l'acquisition des terrains de bidonvilles est une garantie financière utile, non une taxe à supprimer. L'exception liée à une demande locale et l'habilitation du décret répartissant le financement des autres opérations demeurent ; aucune autorisation ou déclaration supplémentaire n'est instituée par cet article.",
    "Conserver les deux alinéas, l'exception tenant à l'auteur de la demande de prise de possession et la subvention couvrant une part du déficit prévu. La suppression du forfait de L543-2 ne modifie pas cette répartition des acquisitions. Aucune compensation budgétaire ni économie nationale n'est calculée.",
    "Le financement exclusif par l'Etat ou ses opérateurs, hors demande locale visée au premier alinéa, et la subvention de l'Etat au déficit des autres opérations sont maintenus pour les opérations futures recevables. Aucun retrait d'aide, transfert nouveau de charge ou condition supplémentaire n'est proposé.",
    "La source entière conserve son mécanisme de concours financiers et ses deux champs d'opérations ; aucun allègement nouveau ni transfert nouveau de financement n'est revendiqué.",
    "Le montant des subventions et le coût des opérations dépendent du décret et des décisions de financement ; cet article seul ne permet pas de les chiffrer.",
    "Aucune charge nouvelle n'est identifiée : le texte source est maintenu sans dossier, justificatif ou agrément ajouté."
)

retain(
    'L522-2',
    "Maintien intégral de la règle de conflit de lois dans le temps. Elle protège les effets des déclarations d'insalubrité et d'utilité publique antérieures au 10 juillet 1970 ; elle ne prescrit aucune nouvelle déclaration ni acquisition. Son ancienneté ne démontre pas l'extinction de tous ses effets patrimoniaux.",
    "Conserver la date du 10 juillet 1970, les deux anciens articles du code de la santé publique et la loi n° 64-1229 comme références historiques, non comme habilitations actuelles. La datation de version fournie (2000-06-22) ne change pas ce seuil historique. Les lois anciennes citées ne sont pas intégralement jointes ; aucun effet ancien n'est réputé éteint.",
    "Le maintien de la loi ancienne peut conserver indemnisations, droits des propriétaires et situations acquises liés aux déclarations antérieures. La règle ne ferme aucune aide future relevant d'un autre fondement et ne réactive pas une procédure abrogée pour de nouvelles déclarations.",
    "La conservation des effets historiques évite une suppression indifférenciée des droits et obligations anciens ; aucune baisse de prélèvement n'est démontrée.",
    "Seules les déclarations prises avant le 10 juillet 1970 sont visées. L'existence de contentieux ou de créances encore ouverts n'est pas quantifiée.",
    "Aucune charge nouvelle n'est identifiée : aucune déclaration nouvelle, régularisation ou preuve périodique ne résulte du maintien de cette transition."
)

retain(
    'L531-1',
    "Maintien intégral de l'habilitation d'adaptation territoriale du titre II : les modalités des concours financiers contre l'habitat indigne doivent pouvoir être fixées dans les six territoires énumérés. L'article n'impose lui-même ni agrément, ni dossier, ni taxe ; abroger l'habilitation fragiliserait l'accès aux financements plutôt que de retirer une formalité identifiée.",
    "Conserver exactement Guadeloupe, Guyane, Martinique, La Réunion, Mayotte et Saint-Martin. Le renvoi porte sur le titre II du livre V, et non sur l'ensemble des polices du livre. Ne pas ajouter Saint-Barthélemy ou Saint-Pierre-et-Miquelon par analogie avec L531-2-1.",
    "L'accès aux concours financiers et aux adaptations locales du titre II demeure ouvert aux futures opérations éligibles dans les territoires énumérés. Aucun avantage n'est retiré et aucune extension territoriale non décidée n'est présumée.",
    "L'habilitation réglementaire territoriale reste entière ; aucun dépôt ou contrôle actuellement décrit par cette source n'est supprimé.",
    "Les obligations éventuellement présentes dans les décrets d'application ne sont pas réputées allégées par le seul maintien de cet article.",
    "Aucune charge nouvelle n'est identifiée : la même habilitation, dans le même champ territorial et matériel, est conservée."
)

retain(
    'L531-2',
    "Maintien intégral de l'exception territoriale de Saint-Pierre-et-Miquelon et de sa réserve expresse en faveur de L531-2-1. Cette articulation limite l'application du livre tout en préservant la police d'insalubrité sanitaire ; ce n'est ni un quota SRU ni une formalité sans objet.",
    "L531-2-1 a été lu intégralement : il applique le chapitre unique du titre Ier pour remédier à l'insalubrité au sens du 4° de L511-2. Préserver la référence historique à l'ordonnance n° 2007-42 et la note de l'ordonnance n° 2020-1144 : effet au 1er janvier 2021 pour les arrêtés notifiés à compter de cette date. Aucune date de réforme future n'en est tirée.",
    "La non-application des autres dispositions du livre est une dérogation territoriale favorable qui reste ouverte aux situations futures. Les protections sanitaires expressément réintroduites par L531-2-1 sont conservées, sans élargir l'ensemble du livre à ce territoire.",
    "La source conserve à la fois la dérogation territoriale et l'exception sanitaire ; aucune suppression supplémentaire de contrainte n'est revendiquée.",
    "Le titre Ier dans sa rédaction historique et les arrêtés antérieurs conservent leur articulation propre ; pas de réécriture présumée du droit local complet.",
    "Aucune charge nouvelle n'est identifiée : la réserve et les limites territoriales sont maintenues sans nouveau dossier ni justificatif."
)

retain(
    'L531-2-1',
    "Maintien intégral des I et II et des 1° à 3° : ils désignent l'autorité de police sanitaire et adaptent les fonctions sanitaires dans trois collectivités. Les pouvoirs nécessaires pour remédier à l'insalubrité et la répartition des compétences protègent la santé ; aucune autorisation économique, déclaration annuelle ou prélèvement accessoire n'est créé ici.",
    "Conserver le champ limité au 4° de L511-2, les trois territoires et les trois adaptations d'autorités, notamment la réserve 's'il existe' au 3°. La source L531-2 est cohérente avec cette exception spéciale. La note limite l'application aux arrêtés notifiés à compter du 1er janvier 2021 ; les situations précédentes ne sont pas converties.",
    "Les occupants conservent la protection contre l'insalubrité et les dispositions du code citées par le chapitre rendu applicable. L'adaptation à Saint-Pierre-et-Miquelon évite d'exiger une agence régionale inexistante dans cette configuration ; les bénéfices protecteurs demeurent pour les futures situations couvertes.",
    "Les compétences sanitaires et leur champ territorial sont conservés sans modification ; aucune simplification matérielle nouvelle ne ressort de cet article.",
    "La sécurité structurelle et les autres matières non comprises dans le champ sanitaire ne sont pas étendues implicitement par ce maintien.",
    "Aucune charge nouvelle n'est identifiée : mêmes compétences et même champ, sans nouvelle transmission ou procédure de remplacement."
)

old = '5° Aux articles L. 541-2 et L. 541-3, les mots : " à la conservation des hypothèques ou " ne sont pas applicables.'
new = "5° Pour l'application des articles L. 541-2 et L. 541-3, la publicité immobilière est effectuée au livre foncier."
assert old in BY_NUMBER['L531-3']['source_xml']
xml = BY_NUMBER['L531-3']['source_xml'].replace(old, new, 1)
xml += "<p>La coordination du 5° s'applique aux formalités de publicité immobilière accomplies à compter de l'entrée en vigueur de la présente loi. Les formalités régulièrement accomplies avant cette date demeurent valables et n'ont pas à être renouvelées. Cette coordination ne crée aucune nouvelle formalité de publicité et ne modifie pas les droits de relogement ni les conditions de solidarité.</p>"
rewrite(
    'L531-3', xml,
    "Coordination nécessaire du seul 5° : il écarte encore des mots relatifs à la conservation des hypothèques qui n'existent plus dans les sources actuelles de L541-2 et L541-3. Le remplacement par la désignation expresse du livre foncier rend l'adaptation de Mayotte opérante sans nouvelle publicité. Les autres subdivisions, dont les 2° et 3° déjà abrogés et tout le régime de relogement du 4°, sont intégralement conservées.",
    "L541-2 et L541-3 ont été lus intégralement : ils mentionnent désormais le fichier immobilier ou le livre foncier, et non les mots que l'ancien 5° entend supprimer. Ces deux cibles ne sont pas fournies dans reference-targets mais sont lues dans le corpus ; aucun nouveau registre, ni déplacement de la publicité particulière des fonds de commerce n'est proposé. Lecture intégrale de L521-3-3 et des deux versions de L521-3-2 : le 4° vise expressément le I de L521-3-2 et non son II abrogé ; le changement proposé au IV ne modifie pas cette compétence. Maintenir L313-19, L313-26-2, L313-35, L321-8, L321-10, L441-1 et L441-1-3, les délais administratifs et la transition des arrêtés notifiés à compter du 1er janvier 2021. Les cibles de travail ne les remplacent pas et les dispenses de L541-5 restent distinctes.",
    "L'accès au relogement, les droits de réservation au bénéfice des salariés et demandeurs d'emploi, les offres de logements conventionnés et la substitution en cas de refus restent ouverts aux situations futures éligibles. La réforme du contrat unique ne retire pas la qualité de salarié à leurs bénéficiaires.",
    'coordination_only',
    "L'adaptation immobilière du 5° est rendue cohérente avec les mots actuels des deux articles visés, sans réduction matérielle revendiquée. Les voies de relogement sont intégralement conservées.",
    "Le délai d'attribution fixé par le représentant de l'Etat n'est pas le préavis de rupture d'emploi. Aucun régime privé de travail ou d'indemnité n'est étendu aux compétences administratives.",
    "Aucune charge nouvelle n'est identifiée : même publicité au livre foncier, sans reprise des formalités anciennes, nouveau recensement ou preuve d'emploi supplémentaire.",
    [effect(
        'coordination', 'mayotte-publicite-habitat-livre-foncier',
        "Coordination de l'adaptation foncière de Mayotte avec le libellé actuel des articles de solidarité.",
        "Le 5° exclut les mots relatifs à la conservation des hypothèques, absents des deux articles actuels qui parlent de fichier immobilier ou livre foncier.",
        "Le 5° désigne directement le livre foncier pour la publicité immobilière des deux articles à Mayotte, sans nouvelle formalité.",
        'other', "Propriétaires et exploitants, autorités de police et professionnels des publicités immobilières à Mayotte.",
        "Formalités nouvelles à compter de l'entrée en vigueur ; publicités valablement accomplies auparavant conservées sans répétition.",
        "Aucune publicité supplémentaire ni condition de solidarité nouvelle ; les registres distincts des fonds de commerce gardent leur objet.",
        old, new
    )]
)

retain(
    'L541-2-1',
    "Maintien intégral de la solidarité des indivisaires après notification ou publicité et de l'avertissement relatif à l'astreinte. Les sommes financent les mesures effectivement exécutées et l'hébergement ou le relogement ; la solidarité évite que l'indivision empêche la mise en sécurité. Les notifications conditionnant l'opposabilité et l'astreinte constituent une garantie essentielle, non un justificatif redondant.",
    "L184-1, L184-3, L511-11 et L511-15 ont été lus dans le corpus. La notification d'un arrêté de police n'est pas une notification de rupture d'emploi ; aucun préavis de quinze jours ne lui est appliqué. Conserver le point de départ distinct pour indivisaires identifiés lorsque tous n'ont pu être identifiés. Le retrait du forfait de 8 % de L543-2 laisse les frais réels et les astreintes autonomes à leur champ ; la note de 2020 n'est pas une date de réforme future.",
    "Les occupants gardent la prise en charge de la sécurité et du relogement ; les indivisaires gardent les conditions d'information et de publicité avant solidarité. Les remises et limites de l'astreinte des articles visés subsistent pour les situations futures comme pour les dossiers anciens.",
    "Les obligations de paiement et les garanties d'opposabilité restent identiques ; leur maintien n'est pas présenté comme une baisse de taxe.",
    "La dette exacte dépend des dépenses et astreintes légalement établies. Aucun chiffrage global ni réforme du partage civil entre indivisaires n'est établi.",
    "Aucune charge nouvelle n'est identifiée : les mêmes notifications, publications et conditions d'astreinte sont conservées sans attestation supplémentaire."
)

retain(
    'L541-5',
    "Maintien intégral de la dispense de solidarité pour les repreneurs lors des ventes judiciaires et par adjudication. Elle facilite la reprise et protège les acquéreurs dans les procédures de sauvegarde, redressement et liquidation ; l'abroger augmenterait leur charge alors que les obligations générales de L541-2 et L541-3 subsistent.",
    "L541-2 et L541-3 ont été lus en entier dans le corpus. La dispense vise leur solidarité, non toutes les sûretés immobilières ou toutes les obligations de sécurité. L541-4 conserve sa règle distincte de transmission de la sûreté dans un plan de cession. Aucune extension à une vente amiable ordinaire n'est présumée.",
    "L'exclusion de solidarité profite aussi aux futurs repreneurs et adjudicataires éligibles, y compris lors d'une vente autorisée ou ordonnée au cours d'une procédure collective. Elle n'est pas réduite à la protection du stock ancien et n'est pas retirée avec le forfait de L543-2.",
    "La dérogation favorable reste entière ; elle constitue un avantage préservé et non une nouvelle dette supprimée.",
    "Les charges attachées au bien sur un autre fondement et les obligations de mise en sécurité ne sont pas abolies par cette exception de solidarité.",
    "Aucune charge nouvelle n'est identifiée : maintien de la dispense sans nouvelle demande, autorisation ou condition documentaire."
)

retain(
    'L542-3',
    "Maintien intégral du contrôle du juge avant vente ou destruction des meubles, du contradictoire, de la conservation pendant deux ans des papiers personnels et du versement du produit net à l'occupant. Ces garanties protègent les biens d'une personne évacuée ; supprimer l'autorisation judiciaire permettrait une dépossession sans contrôle. Elles ne font pas double emploi avec l'inventaire initial.",
    "La suppression, à L542-2, de la convocation à date fixe dès l'inventaire ne supprime pas l'obligation, ici maintenue, d'entendre ou d'appeler les parties. Conserver les deux ans, le procès-verbal de destruction et la déduction des seuls frais engagés après l'expiration du délai de retrait de L542-1. La dénomination historique d'huissier est conservée ; la succession légale par les commissaires de justice relève des textes organiques extérieurs, non fournis intégralement.",
    "L'occupant conserve le contrôle judiciaire, le bénéfice de la conservation des papiers personnels pendant deux ans et l'intégralité du produit de vente après les seules déductions autorisées. Ces protections s'appliquent aux évacuations futures et ne sont pas réservées aux biens déjà entreposés.",
    "Aucune nouvelle réduction : la procédure protectrice et la restitution du produit de vente restent celles de la source officielle entière.",
    "Le montant des frais de vente ou de garde n'est pas chiffré ; la suppression de la convocation anticipée n'abolit pas la convocation utile devant le juge.",
    "Aucune charge nouvelle n'est identifiée : les obligations conservées existent déjà dans l'article et aucune seconde audience n'est ajoutée."
)

retain(
    'L542-4',
    "Maintien intégral de la substitution de l'autorité de police au propriétaire ou exploitant défaillant. Elle assure matériellement la sauvegarde des meubles après évacuation et permet de recouvrer les frais auprès du responsable ; le recouvrement comme en matière de contributions directes n'institue pas une taxe nouvelle.",
    "Le renvoi au présent chapitre conserve son objet après la suppression de la seule convocation anticipée de L542-2 : inventaire, entreposage, délai de retrait et contrôle judiciaire demeurent. La suppression du forfait de L543-2 ne prive pas la personne publique du principal des dépenses légalement recouvrables.",
    "Les occupants bénéficient encore de la sauvegarde de leurs biens même en cas de carence du propriétaire, pour les futures évacuations aussi. Ni avance obligatoire par l'occupant ni garantie financière nouvelle n'est introduite en échange de cette protection.",
    "La continuité de la sauvegarde des meubles et le recouvrement des frais réels restent inchangés ; aucune suppression de prélèvement distinct n'est revendiquée.",
    "Le coût public d'une substitution dépend des dossiers ; aucun transfert nouveau de financement ni montant d'économie n'est établi.",
    "Aucune charge nouvelle n'est identifiée : même intervention subsidiaire et même recouvrement, sans dossier de remplacement demandé à l'occupant."
)

retain(
    'L611-1',
    "Maintien intégral du principe exceptionnel et temporaire applicable à une crise grave du logement. Il ne constitue pas, à lui seul, une autorisation générale de contraindre sans les conditions des chapitres suivants ; il oriente les mesures vers l'installation des personnes selon leur travail et leur famille. Aucun quota SRU ou prélèvement communal n'y figure.",
    "Conserver le seuil de crise grave et les caractères exceptionnel et temporaire. Les mesures particulières doivent garder leurs propres bases légales et garanties ; ce principe ne rétablit aucun quota, rattrapage, carence ou prélèvement SRU supprimé. Le travail mentionné n'est pas un renvoi au régime de rupture des contrats privés.",
    "La prise en compte des besoins de logement liés au travail et à la famille demeure ouverte aux situations futures. Aucun dispositif d'aide ou dérogation favorable n'est supprimé au seul motif de ce principe général.",
    "Le principe de finalité des mesures de crise est conservé ; sa formulation ne démontre aucune formalité ou taxe supplémentaire retirée.",
    "L'article ne chiffre pas les besoins et n'institue pas lui-même toutes les réquisitions ou mesures du livre VI ; leurs charges ne sont pas réputées supprimées.",
    "Aucune charge nouvelle n'est identifiée : le texte reste entier, sans condition, délai ou obligation déclarative ajouté."
)

retain(
    'L613-1',
    "Maintien intégral du renvoi aux règles judiciaires de sursis à l'expulsion du code des procédures civiles d'exécution. La protection juridictionnelle contre une éviction précipitée est essentielle ; supprimer ce renvoi ne retire pas une formalité inutile et pourrait obscurcir les garanties des occupants.",
    "Conserver exactement L412-3, L412-4 et L412-6 à L412-8 du CPCE ; aucun renvoi au droit du licenciement. Les textes complets du CPCE ne figurent pas dans le corpus autorisé et ne sont pas présentés comme réécrits. La politique d'accélération des impayés nécessite un traitement propre du CPCE et de la loi n° 89-462 ; aucune réduction de leurs délais n'est opérée ici.",
    "Les délais et protections judiciaires d'expulsion restent accessibles aux futurs occupants remplissant leurs conditions. Aucun préavis de quinze jours d'emploi n'est substitué à ces garanties et aucune dispense favorable n'est fermée.",
    "Le renvoi de protection demeure sans modification ; il ne compte ni comme réécriture ni comme nouvelle réduction de délai.",
    "Le contenu détaillé des dispositions extérieures n'est pas vérifié à partir d'un texte intégral fourni ; aucune simplification de la procédure d'expulsion n'est revendiquée.",
    "Aucune charge nouvelle n'est identifiée : aucun recours préalable, pièce ou condition supplémentaire n'est créé par le maintien du renvoi."
)

retain(
    'L615-3',
    "Maintien intégral de la composition de la commission de sauvegarde et de la délégation facultative de sa présidence. La représentation du conseil syndical, la faculté pour les copropriétaires de choisir un représentant en son absence et la présence des autorités et administrateurs compétents protègent le consentement et l'utilisation des fonds. L'article n'impose ni réunion périodique minimale ni nouvelle déclaration.",
    "L615-1 et L615-2 ont été lus en entier : la commission élabore le diagnostic et le plan et doit comprendre des représentants de propriétaires et locataires. L615-3 ne remplace pas cette garantie autonome. Conserver département, EPCI compétent et délégation de présidence seulement lorsque l'autorité locale est à l'initiative du plan. Ne pas confondre cette sauvegarde des immeubles avec la carence SRU.",
    "La désignation d'un représentant par l'assemblée générale lorsqu'il n'existe pas de conseil syndical et la présidence locale facultative restent possibles pour les futurs plans. Les aides et droits des occupants ne sont pas fermés en échange d'une suppression de représentation.",
    "La gouvernance et les options existantes restent entières ; aucune fusion nouvelle de commission ni réduction matérielle de procédure n'est démontrée.",
    "Le nombre de réunions et les coûts réels de fonctionnement ne sont pas établis par cet article ; aucune économie nationale n'est extrapolée.",
    "Aucune charge nouvelle n'est identifiée : aucune périodicité, rapport ou attestation nouvelle n'est ajoutée à la commission."
)


xml = """<p>Le présent article est abrogé à compter de l'entrée en vigueur de la présente loi.</p>
<p>L'article L. 482-3 ne peut plus être rendu applicable, sur le seul fondement d'une délibération prise en application du présent article, aux logements locatifs sociaux qui ne sont pas situés dans les zones géographiques mentionnées au I de l'article L. 482-3. Les délibérations antérieures cessent de produire cet effet pour l'avenir. Aucune déchéance du titre d'occupation ne peut être prononcée ou prendre effet après l'entrée en vigueur de la présente loi sur ce seul fondement.</p>
<p>Les baux en cours se poursuivent selon leurs stipulations et les règles qui leur sont applicables, sans déchéance du titre d'occupation sur ce seul fondement. Les contrats valablement conclus et les droits favorables acquis par les locataires, notamment au relogement ou à la conclusion d'un nouveau bail, demeurent protégés. Les baux ayant pris fin avant cette entrée en vigueur ne sont pas reconstitués par la présente abrogation ; les contestations et recours relatifs aux effets antérieurs demeurent ouverts selon les règles qui leur sont applicables.</p>"""
rewrite(
    'L482-4', xml,
    "Réforme de fond : abroger la faculté d'étendre par délibération la déchéance du titre d'occupation de L482-3 aux logements SEM hors zones de déséquilibre important. Après lecture de L482-3, cette extension d'une obligation de quitter le logement n'a pas de fonction essentielle démontrée dans ces zones. La suppression vaut aussi pour les effets futurs des délibérations déjà prises ; les droits favorables et les contrats sont préservés.",
    "L482-3 a été lu en entier dans le corpus : seuil de 150 %, deux années consécutives, prorogation de dix-huit mois, notification six mois avant l'échéance, nouveau bail et exemptions. Aucun de ces nombres n'est modifié dans son champ géographique propre. L482-4 cesse seulement d'étendre ce régime hors zone ; les délais locatifs ne sont pas ceux du contrat de travail. Les déchéances déjà effectives et leurs recours ne sont pas annulés automatiquement. Les renvois réglementaires à cette extension doivent être retirés dans leur seul champ ; aucun examen complet de ces règlements n'est affirmé.",
    "La fin de l'extension supprime une contrainte de départ pour les locataires hors zone. Elle ne retire ni les exemptions liées à l'âge, au handicap ou aux quartiers de L482-3 dans son champ autonome, ni un droit favorable au nouveau bail déjà acquis ; les nouveaux locataires hors zone bénéficient également de l'absence d'extension.",
    'material_reduction',
    "L'habilitation à imposer hors zone le régime de fin d'occupation est entièrement supprimée pour l'avenir, y compris les effets futurs des délibérations anciennes ; aucun régime équivalent ne la remplace.",
    "Le régime de L482-3 dans les zones qu'il vise, les autres motifs légaux de congé et les fins de bail déjà effectives demeurent distincts. Aucun effet sur les loyers ou la disponibilité globale de logements n'est chiffré.",
    "Aucune charge nouvelle n'est identifiée : aucune déclaration de ressources, demande de maintien ou autorisation de remplacement n'est créée par l'abrogation.",
    [effect(
        'obligation_removed', 'sem-fin-extension-sortie-hors-zone',
        "Suppression de la possibilité d'imposer la fin d'occupation de L482-3 hors de ses zones, par simple délibération SEM.",
        "Hors zone : extension facultative par le conseil du régime de L482-3, comportant déchéance à l'issue de dix-huit mois et notification six mois avant l'échéance, avec ses exemptions.",
        "Hors zone : aucune nouvelle déchéance ou prise d'effet future de déchéance sur cette seule extension ; autres règles de bail inchangées.",
        'legal_duty', "Locataires de logements locatifs sociaux des SEM hors des zones du I de L482-3.",
        "Dès l'entrée en vigueur ; effets futurs des anciennes délibérations arrêtés, contrats et droits favorables acquis protégés, pas de reconstitution des baux déjà terminés.",
        "Aucun mécanisme de contrôle ou dépôt de remplacement ; pas de suppression générale des règles locatives.",
        "rendre applicable l'article L. 482-3 aux logements locatifs sociaux qui ne sont pas situés dans les zones géographiques mentionnées au I du même article.",
        "Aucune déchéance du titre d'occupation ne peut être prononcée ou prendre effet après l'entrée en vigueur de la présente loi sur ce seul fondement."
    )],
    repeal="Suppression de l'habilitation des conseils des SEM à étendre hors zone la fin du droit d'occupation de L482-3 et cessation des effets futurs des délibérations prises sur ce seul fondement."
)


xml = """<p>Si un bien grevé de l'hypothèque légale spéciale mentionnée au 7° de l'article 2402 du code civil est compris dans un plan de cession arrêté en application de l'article L. 631-22 ou des articles L. 642-1 et suivants du code de commerce, la charge de cette sûreté est transmise au cessionnaire. Celui-ci est alors tenu d'acquitter entre les mains du créancier la somme restant due à la date du transfert de propriété, ou en cas de location-gérance, de la jouissance du bien sur lequel porte la garantie.</p>
<p>Les sûretés constituées sous l'empire des dispositions antérieures demeurent régies par les dispositions transitoires qui leur sont applicables, y compris pour la transmission de leur charge. La présente rédaction ne modifie ni le montant des créances garanties ni leur rang.</p>"""
rewrite(
    'L541-4', xml,
    "Coordination nécessaire du renvoi à la sûreté immobilière : l'ancien 8° de l'article 2374 est remplacé par le 7° de l'article 2402, déjà cité dans la source officielle de L543-1. La garantie du coût des mesures contre l'habitat indigne est conservée, avec les règles transitoires des anciennes sûretés. Aucune baisse de dette ni simplification matérielle n'est revendiquée.",
    "Nouveau renvoi à une cible non fournie dans reference-targets : code civil, article 2402, 7°. La concordance est corroborée par L543-1 et sa note d'entrée en vigueur au 1er janvier 2022 de l'ordonnance n° 2021-1192. Le code civil et les dispositions transitoires complètes de cette ordonnance, ainsi que les cibles du code de commerce L631-22 et L642-1 et suivants, ne sont pas intégralement disponibles dans le corpus ; ce contrôle extérieur reste signalé et ne constitue pas une filiation SRU vérifiée. Aucun nouveau rang ni régime de sûreté n'est déduit de cette coordination. L541-5 conserve sa dispense distincte de solidarité, qui ne vaut pas extinction de toute sûreté grevant le bien.",
    "La dispense de solidarité des repreneurs prévue à L541-5 est intégralement conservée et demeure ouverte aux ventes futures éligibles. La coordination ne retire aucune remise, exonération ou recours portant sur les créances garanties et n'ajoute pas les frais supprimés de L543-2 au principal dû.",
    'coordination_only',
    "L'article conserve la transmission de la sûreté et le montant restant dû ; seul le support juridique cité est actualisé, sous réserve des transitions des anciennes sûretés.",
    "Le texte intégral du code civil et de l'ordonnance de réforme des sûretés n'étant pas joint, le contrôle externe de la concordance et des transitions reste à documenter. Aucun allègement de dette n'est compté.",
    "Aucune charge nouvelle n'est identifiée : aucune nouvelle sûreté, inscription, donnée ou formalité n'est instituée par cette coordination de référence.",
    [effect(
        'coordination', 'habitat-indigne-concordance-surete',
        "Actualisation de la référence à la sûreté immobilière sans modifier la dette garantie.",
        "Renvoi au privilège spécial immobilier du 8° de l'article 2374 du code civil.",
        "Renvoi à l'hypothèque légale spéciale du 7° de l'article 2402 ; maintien des dispositions transitoires des anciennes sûretés, sans changement de montant ou de rang.",
        'other', "Cessionnaires de biens grevés de la sûreté dans les plans de cession et créanciers concernés.",
        "Application de la référence actuelle sous réserve des règles transitoires gouvernant les anciennes sûretés ; aucune rétroactivité créatrice de dette.",
        "Aucune inscription ou formalité nouvelle ; vérification extérieure du texte civil restant explicitement signalée.",
        "privilège spécial immobilier mentionné au 8° de l'article 2374 du code civil",
        "l'hypothèque légale spéciale mentionnée au 7° de l'article 2402 du code civil"
    )]
)


xml = """<p>Lorsqu'un immeuble frappé d'un arrêté pris en application de l'article L. 184-1 ou de l'article L. 511-11 du présent code ou le fonds de commerce qui y est exploité aux fins d'hébergement font l'objet d'une mutation, le notaire qui dresse l'acte notifie sans délai cette mutation à l'auteur de l'arrêté.</p>
<p>Pour les mutations constatées à compter de l'entrée en vigueur de la présente loi, aucune notification supplémentaire au maire n'est exigée au titre du présent article lorsque celui-ci n'est pas l'auteur de l'arrêté. Cette suppression ne dispense pas de la notification à l'auteur de l'arrêté lorsqu'il est le maire. Les notifications déjà régulièrement effectuées n'ont pas à être renouvelées ; les mutations constatées avant cette entrée en vigueur demeurent régies par les dispositions antérieures.</p>"""
rewrite(
    'L541-6', xml,
    "Réforme de fond : retirer le second destinataire obligatoire, le maire lorsqu'il n'est pas l'auteur de l'arrêté, tout en conservant l'information immédiate de l'autorité chargée de l'exécution. La fonction essentielle de suivi des responsables subsiste sans double envoi. Coordination expresse du renvoi inexistant L184-1-3 vers L184-1, fondement des arrêtés de sécurité d'hébergement identifié dans les articles voisins.",
    "L184-1, L541-2 et L541-3 ont été lus dans le corpus : ils associent les arrêtés L184-1 et L511-11, alors qu'aucun article L184-1-3 n'y figure. Nouveau renvoi L184-1 non fourni comme cible de reference-targets, mais texte officiel intégral lu dans le corpus. L'exécution, les publicités foncières et la solidarité ne sont pas supprimées. Le maire auteur reste destinataire ; lorsque l'autorité est distincte, aucun envoi administratif de remplacement au maire n'est créé. Les éventuelles transmissions fondées sur d'autres textes demeurent à leur champ et ne sont pas prétendues supprimées.",
    "Les protections d'hébergement, de relogement et la connaissance de la mutation par l'autorité d'exécution demeurent. Aucune dispense d'une aide, exonération ou dérogation favorable n'est retirée ; la suppression du double envoi vaut pour toutes les mutations futures couvertes, sans demande du bénéficiaire.",
    'material_reduction',
    "Un destinataire obligatoire de notification est retiré lorsque le maire et l'auteur de l'arrêté sont distincts. Le suivi essentiel de la mutation est conservé ; la correction du renvoi n'est pas une seconde obligation supprimée.",
    "Aucun gain nouveau lorsque le maire est déjà l'auteur de l'arrêté. Les transmissions requises par des fondements autonomes et leurs coûts ne sont pas évalués.",
    "Aucune charge nouvelle n'est identifiée : la notification existante à l'auteur subsiste et aucun rapport, registre ou déclaration remplaçant l'envoi au maire n'est institué.",
    [effect(
        'obligation_removed', 'habitat-indigne-fin-double-notification-mutation',
        "Suppression de l'envoi notarial supplémentaire au maire distinct de l'auteur de l'arrêté.",
        "Mutation notifiée sans délai à l'auteur de l'arrêté ainsi qu'au maire de la commune.",
        "Mutation notifiée sans délai au seul auteur au titre de cet article ; maire destinataire s'il est lui-même cet auteur.",
        'legal_duty', "Notaires constatant la mutation d'un immeuble ou fonds d'hébergement sous arrêté, lorsque les deux autorités sont distinctes.",
        "Mutations constatées dès l'entrée en vigueur ; mutations antérieures soumises à leurs règles, pas de répétition des notifications déjà faites.",
        "Aucun nouvel envoi par une autre personne n'est prescrit ; obligations autonomes conservées.",
        "notifie sans délai cette mutation à l'auteur de l'arrêté ainsi qu'au maire de la commune.",
        "notifie sans délai cette mutation à l'auteur de l'arrêté."
    ), effect(
        'coordination', 'habitat-indigne-coordination-renvois-police',
        "Rectification explicite de la référence au fondement des arrêtés de sécurité des établissements d'hébergement.",
        "Mention L184-1-3 sans article correspondant dans le corpus fourni.",
        "Mention L184-1, fondement lu des arrêtés de sécurité d'hébergement, concordant avec L541-2 et L541-3.",
        'other', "Autorités de police, notaires et parties aux mutations visées.",
        "Correction pour les mutations futures, sans réouverture ou nouvelle notification des actes antérieurs.",
        "Aucune formalité distincte n'est créée par la correction.",
        "articles L. 184-1-3 ou l'article L. 511-11 du présent code",
        "l'article L. 184-1 ou de l'article L. 511-11 du présent code"
    )],
    removed=["Notification notariale supplémentaire de chaque mutation au maire de la commune lorsque celui-ci est distinct de l'auteur de l'arrêté de police."]
)


old = "au titre d'un arrêté de péril, d'une déclaration d'insalubrité"
new = "au titre d'un arrêté de mise en sécurité ou de traitement de l'insalubrité, d'un arrêté de péril ou d'une déclaration d'insalubrité demeurés applicables"
assert old in BY_NUMBER['L542-1']['source_xml']
xml = BY_NUMBER['L542-1']['source_xml'].replace(old, new, 1)
xml += "<p>La présente rédaction s'applique aux évacuations intervenant à compter de l'entrée en vigueur de la présente loi. Les inventaires, significations et mesures de garde régulièrement accomplis auparavant demeurent valables et n'ont pas à être renouvelés. Les droits de retrait, de conservation et de relogement des occupants résultant des évacuations antérieures demeurent régis par les dispositions qui leur sont applicables.</p>"
rewrite(
    'L542-1', xml,
    "Coordination nécessaire avec la police unifiée de mise en sécurité et de traitement de l'insalubrité : ses arrêtés sont nommés expressément, sans fermer le régime des anciens arrêtés. Les cinq alinéas et toutes les protections matérielles sont conservés ; le délai d'un an, les frais supportés par le responsable et le contrôle judiciaire ne sont pas des charges administratives superflues.",
    "L511-11 et L521-1 ont été lus intégralement dans le corpus ; L521-3-1 et L521-3-2 dans reference-targets, source et proposition. Conserver le premier alinéa de L521-1 définissant l'occupant, le délai d'un an courant de la signification, le cinquième alinéa et l'exception d'absence de relogement adapté. Le nouveau IV proposé de L521-3-2 concerne le montant recouvré auprès du propriétaire, non le droit de l'occupant à la garde de ses meubles. Les trois cibles de travail sont inapplicables à cette police et à ce délai. La mention explicite des nouveaux intitulés d'arrêtés est coordonnée au vocabulaire officiel lu ; la dénomination historique de l'huissier ne crée pas un professionnel supplémentaire.",
    "La garde aux frais du propriétaire ou exploitant pendant un an, puis au-delà si aucune offre de relogement adaptée n'a été faite, reste entière. La preuve par tout moyen et le contrôle du juge avant vente ou destruction sont conservés pour les futures évacuations ; aucun seuil d'ancienneté d'emploi ne conditionne ces droits.",
    'coordination_only',
    "La sauvegarde des meubles vise expressément les arrêtés actuels de police et reste ouverte aux anciens arrêtés applicables. Il n'est revendiqué ni délai réduit ni obligation matérielle supprimée dans cet article.",
    "Les coûts d'inventaire, déménagement et garde restent à la charge prévue par la source. La convocation anticipée supprimée dans L542-2 n'est pas comptée ici une seconde fois.",
    "Aucune charge nouvelle n'est identifiée : pas de nouvel inventaire pour les actes déjà faits, pas de nouveau dépôt ni d'allongement de la garde ; les protections existantes gardent leur objet.",
    [effect(
        'coordination', 'habitat-indigne-coordination-renvois-police',
        "Coordination du vocabulaire des arrêtés ouvrant la protection des meubles après évacuation définitive.",
        "Source nommant les arrêtés de péril, déclarations d'insalubrité et décisions urgentes de police.",
        "Mention expresse des arrêtés de mise en sécurité ou de traitement de l'insalubrité, avec maintien des anciens actes et des décisions urgentes ; mêmes garanties de garde et de retrait.",
        'other', "Occupants évacués, propriétaires et exploitants des immeubles interdits définitivement à l'habitation.",
        "Evacuations à compter de l'entrée en vigueur ; actes régulièrement accomplis auparavant valables, droits antérieurs préservés.",
        "Aucun acte à refaire et aucun nouveau délai ; pas de nouvelle obligation distincte comptée.",
        "au titre d'un arrêté de péril, d'une déclaration d'insalubrité",
        new
    )]
)


convocation = "-la convocation de la personne évacuée à comparaître devant le juge de l'exécution à une date déterminée qui ne peut être antérieure à l'expiration du délai imparti, afin qu'il soit statué sur le sort des meubles non retirés avant le jour de l'audience."
assert convocation in BY_NUMBER['L542-2']['source_xml']
xml = BY_NUMBER['L542-2']['source_xml'].replace(convocation, '-(Abrogé).', 1)
xml += "<p>La suppression de la convocation dans le procès-verbal s'applique aux procès-verbaux établis à compter de l'entrée en vigueur de la présente loi. Elle ne dispense pas d'entendre ou d'appeler les parties devant le juge de l'exécution dans les conditions de l'article L. 542-3. Les procès-verbaux et convocations régulièrement établis avant cette entrée en vigueur demeurent valables et n'ont pas à être refaits ; les droits des parties et leurs recours sont conservés.</p>"
rewrite(
    'L542-2', xml,
    "Réforme de fond : supprimer l'obligation d'insérer dès le procès-verbal d'inventaire une convocation judiciaire à date fixée au-delà du délai de retrait d'un an. L542-3 impose déjà que les parties soient entendues ou appelées avant le sort judiciaire des meubles. Conserver l'inventaire, l'accès au dépôt, la sommation, la sanction de nullité attachée aux mentions restantes et les deux ans de conservation des papiers personnels.",
    "Les quatre tirets restent localisables, le quatrième étant marqué abrogé ; aucun alinéa de L542-1 n'est déplacé. La comparution utile, l'autorisation du juge et les droits de recours demeurent : seule la programmation imposée dès l'inventaire disparaît. Le délai de retrait d'un an et la conservation de deux ans ne sont pas réduits. Les anciennes convocations restent valables, sans nouvel acte obligatoire. Les textes de procédure civile extérieurs au corpus doivent être coordonnés s'ils imposent encore cette convocation anticipée ; leur suppression n'est pas déclarée accomplie.",
    "Toutes les informations permettant de retrouver les biens et d'éviter leur abandon restent obligatoires ; les papiers personnels sont conservés deux ans. L'occupant bénéficie toujours du contradictoire devant le juge avant vente ou destruction. Les futures personnes évacuées gardent ces protections sans audience fixée artificiellement un an à l'avance.",
    'material_reduction',
    "Une mention et un acte de convocation anticipée obligatoires sont retirés du procès-verbal initial. La saisine et la convocation nécessaires à une décision effective du juge restent exigées par L542-3.",
    "Le coût de la convocation utile demeure ; le nombre d'actes évités dépend des retraits effectifs. Aucun raccourcissement du délai d'un an ou des deux ans n'est revendiqué.",
    "Aucune charge nouvelle n'est identifiée : la convocation ultérieure procède déjà de L542-3, sans nouveau rapport, registre, délai ou mention de remplacement imposé à l'inventaire.",
    [effect(
        'obligation_removed', 'meubles-evacues-fin-convocation-anticipee',
        "Suppression de la convocation judiciaire à date déterminée dans le procès-verbal initial d'inventaire.",
        "Quatrième mention obligatoire, à peine de nullité, fixant dès l'inventaire une comparution après le délai de retrait.",
        "Quatrième mention supprimée ; parties entendues ou appelées au titre de L542-3 lorsqu'une décision sur les meubles est effectivement sollicitée.",
        'legal_duty', "Professionnels dressant l'inventaire et personnes supportant les frais de procédure ; occupants évacués.",
        "Procès-verbaux établis dès l'entrée en vigueur ; actes anciens valables, contradictoire et recours conservés.",
        "Pas de mention de remplacement ; la convocation utile préexistante devant le juge demeure.",
        convocation,
        "La suppression de la convocation dans le procès-verbal s'applique aux procès-verbaux établis à compter de l'entrée en vigueur de la présente loi."
    )],
    removed=["Mention, à peine de nullité du procès-verbal initial, d'une convocation judiciaire à date déterminée après l'expiration du délai de retrait des meubles."]
)


old = "Si, à l'issue du délai fixé, le syndic de la copropriété atteste que l'inexécution des travaux prescrits résulte de la défaillance de certains copropriétaires à avoir répondu aux appels de fonds nécessaires, votés par l'assemblée générale des copropriétaires, l'autorité publique compétente notifie, par arrêté, le montant de l'astreinte due par chacun des copropriétaires défaillants."
new = "Si, à l'issue du délai fixé, il est établi que l'inexécution des travaux prescrits résulte de la défaillance de certains copropriétaires à avoir répondu aux appels de fonds nécessaires, votés par l'assemblée générale des copropriétaires, l'autorité publique compétente notifie, par arrêté, le montant de l'astreinte due par chacun des copropriétaires défaillants. Cette défaillance peut être établie par les décisions d'assemblée générale, appels de fonds et éléments de paiement légalement disponibles, sans attestation distincte obligatoire du syndic. Aucune transmission périodique nouvelle de ces pièces n'est imposée par le présent article."
assert old in BY_NUMBER['L543-1']['source_xml']
xml = BY_NUMBER['L543-1']['source_xml'].replace(old, new, 1)
old_police = "dont les parties privatives sont frappées d'un arrêté de péril ou d'insalubrité."
new_police = "dont les parties privatives sont frappées d'un arrêté de mise en sécurité ou de traitement de l'insalubrité, ou d'un arrêté de péril ou d'insalubrité demeuré applicable."
assert old_police in xml
xml = xml.replace(old_police, new_police, 1)
xml += "<p>La dispense d'attestation distincte s'applique dès l'entrée en vigueur de la présente loi, y compris aux procédures en cours. Elle ne remet pas en cause les arrêtés et notifications régulièrement pris, les preuves déjà produites et les droits de recours ; aucun dossier n'a à être déposé de nouveau.</p>"
rewrite(
    'L543-1', xml,
    "Réforme de fond ciblée : retirer l'attestation distincte du syndic comme condition formelle de l'imputation de l'astreinte aux seuls copropriétaires défaillants lorsque la défaillance résulte déjà des décisions, appels de fonds et paiements disponibles. Le fait à établir, les destinataires, la notification, le régime de liquidation et les garanties de créance restent identiques. Coordination distincte du quatrième alinéa avec les intitulés actuels des arrêtés, sans supprimer les anciens actes applicables. L'astreinte de sécurité n'est pas supprimée et aucun nouveau rapport ne remplace l'attestation.",
    "Les six alinéas sources sont conservés à leur place ; la troisième condition probatoire est allégée et le quatrième alinéa est coordonné au vocabulaire de L511-11/L511-15, textes lus intégralement. L511-15 réserve plafonds et exonérations ; les deux versions de L511-16 conservent la substitution aux seuls défaillants et le recours au tribunal administratif en cas de concours de la force publique refusé. Les trois cibles de travail ne concernent ni l'arrêté ni le délai de travaux. Le 7° de l'article 2402 est conservé, à coordonner avec L541-4 ; pas de seconde dette ajoutée pour une même astreinte. La source ne nomme encore que péril et insalubrité au quatrième alinéa : la coordination des nouveaux intitulés ne crée pas une nouvelle catégorie d'astreinte ou de cumul et laisse leurs conditions propres applicables.",
    "L'imputation aux seuls défaillants après vote des appels de fonds reste accessible dans les procédures futures, avec une preuve plus souple. Les copropriétaires ayant payé ne perdent pas cette protection ; les remises, plafonds et recours de L511-15 ainsi que les droits des occupants restent entiers.",
    'material_reduction',
    "La condition d'une attestation distincte du syndic est retirée. L'administration doit toujours établir la défaillance et notifier l'astreinte ; la modification ne réduit pas son taux ou son plafond.",
    "Gain limité aux dossiers où les faits sont établis sans attestation ; aucune dispense d'établir le fait générateur ni nouvelle baisse d'astreinte n'est revendiquée. Le solde de coût administratif n'est pas chiffré.",
    "Aucune charge nouvelle n'est identifiée : les pièces citées sont les décisions, appels et paiements existants, sans registre, transmission périodique ou accès aux données supplémentaire.",
    [effect(
        'obligation_removed', 'coproprietes-fin-attestation-syndic-astreinte',
        "Suppression d'une attestation obligatoire distincte pour établir les copropriétaires défaillants.",
        "L'imputation aux seuls défaillants est conditionnée par l'attestation du syndic sur les appels de fonds nécessaires votés et non payés.",
        "La défaillance reste à établir mais les décisions, appels de fonds et paiements disponibles peuvent suffire, sans attestation distincte obligatoire.",
        'legal_duty', "Syndics et copropriétaires dans les procédures d'astreinte relatives aux parties communes sous arrêté de sécurité ou d'insalubrité.",
        "Dès l'entrée en vigueur, procédures en cours comprises, sans nouveaux dépôts ni remise en cause des actes valables.",
        "Pas de nouveau registre ou rapport ; établissement contradictoire des faits et notifications existantes conservés.",
        "le syndic de la copropriété atteste que l'inexécution des travaux prescrits résulte de la défaillance de certains copropriétaires",
        "sans attestation distincte obligatoire du syndic."
    ), effect(
        'coordination', 'habitat-indigne-coordination-renvois-police',
        "Coordination des intitulés des arrêtés portant sur les parties privatives, avec maintien du régime d'astreintes existant.",
        "Quatrième alinéa mentionnant les arrêtés de péril ou d'insalubrité pour les parties privatives.",
        "Mention des arrêtés actuels de mise en sécurité ou de traitement de l'insalubrité et des anciens arrêtés demeurés applicables ; pas de nouveau taux ou plafond.",
        'other', "Copropriétaires dont les parties privatives et les parties communes sont sous arrêtés de police.",
        "Coordination terminologique de la police actuelle ; anciens arrêtés et recours conservés, mêmes conditions de liquidation et remises de L511-15.",
        "Aucune seconde astreinte créée et aucun cumul supplémentaire sur le même manquement institué par la coordination.",
        old_police, new_police
    )],
    removed=["Exigence d'une attestation distincte du syndic pour imputer l'astreinte aux seuls copropriétaires défaillants lorsque la défaillance est déjà établie par les pièces disponibles."]
)


xml = """<p>Le présent article est abrogé à compter de l'entrée en vigueur de la présente loi.</p>
<p>Aucun montant forfaitaire de 8 % n'est ajouté sur le fondement du présent article aux dépenses engagées à compter de cette entrée en vigueur au titre de la maîtrise d'ouvrage ou de l'accompagnement social des travaux et mesures prescrits. Aucun forfait de remplacement n'est perçu sur ce même fondement. Les dépenses effectivement recouvrables sur un autre fondement légal, les obligations de mise en sécurité et les droits des occupants demeurent régis par leurs dispositions propres.</p>
<p>Les créances légalement nées à raison de dépenses engagées avant cette entrée en vigueur restent régies par les dispositions antérieures pour leur liquidation, leur recouvrement, les restitutions, la prescription et les recours, même si leur paiement intervient ultérieurement. La présente abrogation n'ouvre pas un droit général au remboursement des sommes antérieurement dues et ne remet pas en cause les contestations ou restitutions légalement fondées.</p>"""
rewrite(
    'L543-2', xml,
    "Réforme de fond : suppression intégrale pour les dépenses nouvelles du forfait accessoire de 8 % ajouté aux dépenses recouvrables contre les propriétaires défaillants. Ce forfait automatique n'est pas la preuve de frais supplémentaires effectivement engagés. Le coût des travaux et des mesures légalement recouvrables reste dû ; aucune taxe ni déclaration ne remplace le forfait supprimé.",
    "Assiette source : dépenses recouvrables des mesures prescrites au titre de L1311-4 du code de la santé publique, L184-1 et du chapitre Ier du titre Ier du livre V du CCH. Le seuil transitoire est la date des dépenses engagées, sans date de promulgation inventée ; les créances antérieures et leurs contestations sont préservées. Ne pas confondre cette suppression avec celle de la contribution de sécurité immobilière ou avec les prélèvements pour frais de recouvrement autonomes de L511-15/L184-3, qui ne sont pas abrogés ici. Examiner les dispositions réglementaires et décomptes appliquant exclusivement ce forfait ; pas de purge complète prétendue des textes extérieurs. Le coût public de maîtrise d'ouvrage et d'accompagnement subsiste et doit être financé, sans recette compensatoire inventée.",
    "Aucune exonération favorable autonome n'est retirée. Le forfait de 8 % disparaît entièrement pour les dépenses nouvelles ; ses allègements éventuels seraient sans objet dans ce champ, sans prélèvement équivalent. Les droits des occupants, les remises et recours anciens ainsi que les aides aux opérations futures restent protégés.",
    'material_reduction',
    "Suppression réelle du supplément forfaitaire de 8 % sur les dépenses nouvelles visées par l'article, sans suppression du principal légalement dû. Il s'agit d'une surcharge de recouvrement retirée, sans qualification de baisse de cotisation sociale.",
    "Les forfaits dus sur des dépenses antérieures restent possibles ; les autres frais ayant un fondement autonome demeurent. La perte de recettes, les coûts publics maintenus et le solde public net ne sont pas chiffrés.",
    "Aucune charge nouvelle n'est identifiée : aucun forfait de remplacement, justificatif, déclaration ou nouvelle procédure de recouvrement n'est ajouté.",
    [effect(
        'obligation_removed', 'habitat-indigne-suppression-forfait-huit-pourcent',
        "Suppression du supplément financier forfaitaire de recouvrement de 8 %.",
        "Supplément de 8 % des dépenses recouvrables des travaux et mesures visés, à la charge des propriétaires défaillants, pour maîtrise d'ouvrage et accompagnement social.",
        "Supplément de 0 % sur ce fondement pour les dépenses engagées à compter de l'entrée en vigueur ; même principal légalement recouvrable, sans forfait de remplacement.",
        'percent', "Propriétaires défaillants redevables des dépenses entrant dans le champ de L543-2.",
        "Dépenses nouvelles dès l'entrée en vigueur ; créances légalement nées de dépenses antérieures et restitutions/recours préservés, pas de remboursement général.",
        "Aucun prélèvement de remplacement ; coûts réels des missions publiques maintenus et solde budgétaire non établi.",
        "un montant forfaitaire de 8 % de ces dépenses.",
        "Aucun montant forfaitaire de 8 % n'est ajouté sur le fondement du présent article aux dépenses engagées à compter de cette entrée en vigueur"
    )],
    repeal="Suppression intégrale du supplément forfaitaire de 8 % pour maîtrise d'ouvrage et accompagnement social ajouté aux dépenses nouvelles recouvrables contre les propriétaires défaillants."
)


old = "Dans ce cas, l'acte de vente et l'attestation sont notifiés à l'administration fiscale par le notaire."
new = "Aucune notification distincte de l'acte de vente ou de l'attestation à l'administration fiscale n'est exigée du notaire au titre du présent II. Les formalités fiscales et de publicité foncière légalement requises sur un autre fondement demeurent applicables."
assert old in BY_NUMBER['L551-1']['source_xml']
xml = BY_NUMBER['L551-1']['source_xml'].replace(old, new, 1)
xml += "<p>La suppression de la notification distincte prévue au II s'applique aux notifications non encore effectuées à la date d'entrée en vigueur de la présente loi, y compris lorsque l'acte de vente a été signé avant cette date. Aucune notification de rattrapage n'est exigée sur ce seul fondement. Les actes, attestations et contrôles antérieurs demeurent valables ; les condamnations, les interdictions encore applicables et les recours conservent leurs effets selon leurs règles propres.</p>"
rewrite(
    'L551-1', xml,
    "Réforme de fond : supprimer la transmission fiscale spéciale de l'acte et de l'attestation d'occupation personnelle. L'attestation reste dans l'acte authentique, lequel relève déjà des formalités fiscales ordinaires, et le contrôle notarial de la condamnation demeure. Ce retrait ne transforme pas une peine facultative dans les propositions cibles en peine automatiquement éteinte ; il supprime seulement un envoi supplémentaire.",
    "Les I et II, les personnes contrôlées, le circuit ADSN/casier, la condamnation définitive, le refus de signature, la nullité de l'avant-contrat et l'information du maire sont conservés. CGI635 et CGI647 ont été lus en entier dans le corpus pour le circuit fiscal ordinaire ; aucune dispense d'enregistrement ou de publicité n'est créée. Les sources et propositions de L184-7, L184-8 et L511-22 ont été lues intégralement : les propositions rendent certaines peines facultatives sans abolir celles effectivement prononcées, et préservent l'occupation personnelle des personnes physiques. Le contrôle de L551-1 porte sur la vente telle que définie par sa source ; le champ plus large des interdictions (usufruit, parts) n'est pas silencieusement étendu ici. Les cibles de travail sont sans application. Les modalités réglementaires de la notification fiscale spéciale restent à retirer dans leur champ ; aucun nouvel accès au casier n'est créé.",
    "La dérogation permettant au condamné d'acquérir son logement pour l'occuper personnellement demeure ouverte aux acquisitions futures, par attestation dans l'acte, sans transmission spéciale supplémentaire. Les exceptions d'occupation personnelle des cibles pénales et les garanties des victimes restent entières ; aucune taxe ni perte d'exonération n'est créée.",
    'material_reduction',
    "La notification fiscale spéciale de l'acte et de l'attestation est supprimée pour tous les envois futurs. Le contrôle des interdictions d'achat et l'attestation d'occupation personnelle sont maintenus ; aucune peine n'est supprimée par cet article.",
    "Les formalités fiscales ordinaires de l'acte et le contrôle notarial restent dus ; aucun gain d'émoluments ou de taxe n'est établi. La conformité du champ civil du contrôle avec toutes les formes d'acquisition interdites n'est pas entièrement résolue dans cet article.",
    "Aucune charge nouvelle n'est identifiée : pas de nouvelle attestation, registre ou accès aux données ; l'attestation déjà prévue reste dans l'acte et aucun envoi de remplacement n'est prescrit.",
    [effect(
        'obligation_removed', 'achat-logement-fin-notification-fiscale-speciale',
        "Suppression de la notification fiscale spéciale de l'achat pour occupation personnelle par une personne sous interdiction.",
        "Acte de vente et attestation d'occupation personnelle notifiés spécialement par le notaire à l'administration fiscale.",
        "Attestation maintenue dans l'acte ; aucune notification distincte au titre du II, formalités fiscales ordinaires conservées.",
        'legal_duty', "Notaires et acquéreurs relevant de la dérogation d'occupation personnelle du II de L551-1.",
        "Tous envois non encore effectués dès l'entrée en vigueur, même pour un acte antérieur ; pas de rattrapage sur ce seul fondement, actes et recours préservés.",
        "Aucune déclaration de remplacement ; contrôle de la peine et formalités générales de l'acte inchangés.",
        old,
        "Aucune notification distincte de l'acte de vente ou de l'attestation à l'administration fiscale n'est exigée du notaire au titre du présent II."
    )],
    removed=["Notification spéciale par le notaire à l'administration fiscale de l'acte de vente et de l'attestation d'occupation personnelle, en plus des formalités générales de l'acte."]
)


xml = """<p>Afin de faciliter la libération de locaux d'habitation affectés à un usage administratif, professionnel ou commercial, le gestionnaire légalement compétent des immeubles bâtis ou non bâtis appartenant à l'Etat et affectés au chemin de fer et à ses dépendances est habilité à passer avec les personnes publiques ou privées des conventions autorisant celles-ci à construire et exploiter des locaux à usage administratif, professionnel ou commercial sur ces immeubles lorsque cette affectation ne fait pas obstacle à un complément d'utilisation.</p>
<p>Ces conventions ne sont pas soumises à l'approbation du ministre chargé des transports au titre du présent article. La réservation d'une partie des locaux à des services publics et les modalités de leur occupation peuvent être convenues par les parties, sans pouvoir être imposées sur le seul fondement du présent article. Les règles applicables à la propriété et à la gestion des biens, à leur affectation ferroviaire, à la sécurité, à la commande publique et à l'occupation domaniale demeurent applicables.</p>
<p>La suppression de l'approbation et de la faculté d'imposer une réservation s'applique aux conventions conclues à compter de l'entrée en vigueur de la présente loi, y compris lorsque leur approbation a déjà été demandée. Aucune nouvelle demande d'approbation n'est exigée sur ce fondement. Les conventions valablement conclues avant cette entrée en vigueur, les droits de leurs parties et les réservations qu'elles prévoient restent régis par leurs stipulations et les dispositions qui leur sont applicables. La présente rédaction ne modifie pas l'identité des propriétaires ni les compétences de gestion résultant des autres textes.</p>"""
rewrite(
    'L612-1', xml,
    "Réforme de fond : retirer l'approbation ministérielle propre à ces conventions et le pouvoir d'imposer sur ce fondement une réservation de locaux. La compatibilité avec l'affectation ferroviaire et les régimes domaniaux et de sécurité restent requis ; une réservation peut être convenue librement. Coordination institutionnelle : l'ancienne dénomination SNCF Mobilités est remplacée par la qualité de gestionnaire légalement compétent, sans attribuer arbitrairement tous les biens à une société successeur.",
    "La source désigne encore SNCF Mobilités dans une version de 2015. La réorganisation ferroviaire et les dévolutions, notamment dans l'ordonnance n° 2019-552 du 3 juin 2019, sont hors corpus et leur texte intégral n'est pas fourni : vérifier cette succession institutionnelle par catégorie de bien, sans prétendre le volet achevé. La rédaction ne fait aucun transfert et laisse les compétences au titulaire désigné par les textes autonomes. Le champ matériel reste limité aux immeubles appartenant à l'Etat et affectés au chemin de fer ; il n'est pas étendu automatiquement aux biens appartenant en propre à une société. Aucun nouveau renvoi numéroté à un code extérieur n'est inventé. Les règles domaniales, de commande publique et de sécurité autonomes ne sont pas réputées supprimées ; leurs circuits restent à vérifier séparément.",
    "La faculté de construire et d'exploiter des locaux complémentaires pour libérer de l'habitation reste ouverte aux futures conventions compatibles avec l'affectation. Les conventions anciennes et leurs droits acquis restent protégés. La suppression du visa ne retire ni une aide ni une dérogation utile ; les réservations déjà contractuelles demeurent.",
    'material_reduction',
    "L'approbation spéciale du ministre et sa faculté d'imposer des réservations disparaissent pour les nouvelles conventions. La désignation fonctionnelle du gestionnaire évite une attribution non documentée à une société précise ; elle ne vaut pas transfert de propriété.",
    "Les autorisations et règles domaniales ou ferroviaires sur d'autres fondements subsistent. L'identification des titulaires après réorganisation doit être documentée hors corpus ; aucun gain de délai global ni coût net n'est établi.",
    "Aucune charge nouvelle n'est identifiée : pas de déclaration remplaçant le visa, pas d'obligation de réservation et pas de nouvelle compétence de gestion créée ; les conditions matérielles préexistantes subsistent.",
    [effect(
        'authorization_removed', 'ferroviaire-fin-approbation-conventions-complementaires',
        "Suppression de l'approbation ministérielle spéciale des conventions de complément d'utilisation et de la réservation unilatérale associée.",
        "Conventions soumises à l'approbation du ministre, pouvant imposer une réservation à des services publics et ses modalités d'occupation.",
        "Aucune approbation sur ce fondement ; réservation seulement convenue par les parties, autres règles autonomes conservées.",
        'legal_duty', "Gestionnaires légalement compétents et cocontractants de biens de l'Etat affectés au chemin de fer entrant dans le champ de l'article.",
        "Conventions conclues dès l'entrée en vigueur, demandes d'approbation pendantes comprises ; conventions anciennes et droits contractuels conservés.",
        "Aucune déclaration ni autorisation de remplacement ; règles autonomes de propriété, sécurité et domanialité maintenues.",
        "Avant d'approuver ces conventions, le ministre chargé des transports peut, dans chaque cas, imposer l'obligation de réserver une partie des locaux à des services publics et fixer les modalités de leur occupation.",
        "Ces conventions ne sont pas soumises à l'approbation du ministre chargé des transports au titre du présent article."
    )],
    removed=[
        "Approbation par le ministre chargé des transports des conventions de construction et d'exploitation complémentaires sur le seul fondement de L612-1.",
        "Faculté du ministre d'imposer sur ce seul fondement une réservation de locaux à des services publics et leurs modalités d'occupation."
    ]
)


old = "après avis du maire de la commune ou du président du groupement de communes ayant compétence en matière de logement, intéressé par la réquisition "
assert old in BY_NUMBER['L614-1']['source_xml']
xml = BY_NUMBER['L614-1']['source_xml'].replace(old, '', 1)
old_opening = "Lorsque des constructions provisoires ou des équipements annexes ne peuvent être réalisés pour permettre le relogement temporaire des personnes occupant un logement insalubre au sens des articles L. 511-1 et suivants du code de l'expropriation pour cause d'utilité publique sur des terrains expropriés en vertu des articles L 511-1 et suivants du code précité les terrains nus nécessaires à cet effet peuvent être réquisitionnés par le représentant de l'Etat dans le département, au profit"
new_opening = "Lorsque les constructions provisoires ou les équipements annexes nécessaires au relogement temporaire des personnes occupant un logement insalubre au sens des articles L. 511-1 et suivants du code de l'expropriation pour cause d'utilité publique ne peuvent être réalisés sur des terrains expropriés en vertu des mêmes articles, les terrains nus nécessaires à cet effet peuvent être réquisitionnés par le représentant de l'Etat dans le département au profit"
assert old_opening in xml
xml = xml.replace(old_opening, new_opening, 1)
old2 = "L'avis du maire ou du président du groupement de communes prévu au précédent alinéa est réputé exprimé s'il n'a pas été émis dans le mois du jour où il a été sollicité."
assert old2 in xml
xml = xml.replace(old2, "Le deuxième alinéa est abrogé.", 1)
xml += "<p>La suppression de la consultation prévue au premier alinéa s'applique aux décisions de réquisition prises à compter de l'entrée en vigueur de la présente loi, y compris dans les procédures en cours. Une consultation déjà engagée ne fait pas obstacle à la décision du seul fait de l'absence d'avis ou de l'inachèvement de l'ancien délai d'un mois. Les décisions antérieures, les droits à indemnisation, les garanties des propriétaires et les recours demeurent régis par les dispositions qui leur sont applicables.</p>"
# Le texte proposé est un corps complet, non une instruction d'amendement.
xml = xml.replace('<p>Le deuxième alinéa est abrogé.</p>', '<p>(Abrogé).</p>')
rewrite(
    'L614-1', xml,
    "Réforme de fond : retirer l'avis préalable du maire ou du groupement et son attente maximale d'un mois, sans supprimer les conditions exceptionnelles de réquisition. L'avis était réputé exprimé sans prise de position et ne constituait pas une autorisation ; l'autorité préfectorale, le besoin de relogement temporaire, la subsidiarité par rapport aux terrains expropriés et les garanties foncières sont conservés.",
    "Conserver les deux objets du renvoi au code de l'expropriation L511-1 et suivants, l'exclusion absolue des propriétés attenantes et closes, les bénéficiaires et le renvoi aux articles 2, alinéa 1er, et suivants de l'ordonnance n° 61-106. L'ouverture source manque de ponctuation avant 'les terrains nus' : elle est clarifiée sans changer la subsidiarité de la réquisition lorsqu'il est impossible de construire sur les terrains expropriés. Ces textes extérieurs ne sont pas fournis intégralement et leur procédure d'indemnisation n'est pas présentée comme réécrite. Seuls l'avis nommé dans L614-1 et l'ancien mois sont retirés ; aucune suppression du contradictoire, de l'indemnité, des recours ou d'une consultation autonome n'est déduite. Les règlements réitérant ce seul avis doivent être coordonnés. Le titre historique de l'ordonnance est conservé tel qu'il figure dans la source, sans rétablissement de son ancien champ personnel par analogie.",
    "Le relogement temporaire des personnes sortant de logements insalubres reste possible pour les situations futures. L'exemption de réquisition des propriétés attenantes aux habitations et closes demeure intégrale, ainsi que les droits à indemnisation et recours ; aucun agrément ou avis de remplacement n'est ajouté.",
    'material_reduction',
    "Une consultation obligatoire et l'attente liée à son avis tacite sont supprimées. Le mois était un délai maximal avant avis réputé exprimé, pas une durée minimale générale de réquisition ; aucun raccourcissement forfaitaire d'un mois de toute procédure n'est annoncé.",
    "Les autres conditions et délais de réquisition, les garanties extérieures et le coût des indemnités subsistent ; le solde financier et le gain de délai effectif ne sont pas chiffrés.",
    "Aucune charge nouvelle n'est identifiée : pas d'avis, de dossier, de registre ou de déclaration de remplacement ; seules les conditions foncières et garanties existantes restent applicables.",
    [effect(
        'obligation_removed', 'requisition-terrains-fin-avis-local',
        "Suppression de l'avis préalable local propre à la réquisition et de l'attente de son expression tacite.",
        "Avis du maire ou du président du groupement à solliciter, réputé exprimé après un mois sans réponse ; pas de veto local.",
        "Aucun avis préalable local sur ce fondement et aucune attente du mois, sous les mêmes conditions de nécessité et garanties foncières.",
        'legal_duty', "Autorité préfectorale et collectivités concernées par les terrains nus nécessaires au relogement temporaire des personnes de logements insalubres.",
        "Décisions prises dès l'entrée en vigueur, procédures en cours comprises ; décisions antérieures, indemnisation et recours préservés.",
        "Aucun avis ni dépôt remplaçant celui qui est supprimé ; autres procédures autonomes conservées.",
        "après avis du maire de la commune ou du président du groupement de communes ayant compétence en matière de logement",
        "La suppression de la consultation prévue au premier alinéa s'applique aux décisions de réquisition prises à compter de l'entrée en vigueur de la présente loi"
    )],
    removed=[
        "Consultation préalable obligatoire du maire ou du président du groupement de communes compétent en matière de logement avant la réquisition du terrain nu.",
        "Délai d'un mois permettant de réputer exprimé l'avis local en l'absence de réponse, retiré avec la consultation dont il était l'exécution."
    ]
)


xml = """<p>Lorsque les engagements prévus au plan de sauvegarde pour les mesures mentionnées à l'article L. 615-2 ne sont pas respectés dans le délai prévu par ce plan, après mise en demeure restée sans effet, la suppression des aides et le recouvrement des aides financières ne portent que sur les aides ou fractions d'aide correspondant aux engagements inexécutés. Les aides ou fractions d'aide correspondant à des engagements exécutés demeurent acquises. Le recouvrement, dans la limite des aides effectivement versées et ainsi rattachées aux engagements inexécutés, a lieu comme en matière de contributions directes. Aucune même somme ne peut être recouvrée deux fois au titre de ces engagements.</p>
<p>La présente limitation s'applique aux décisions de suppression ou de recouvrement prises à compter de l'entrée en vigueur de la présente loi, pour les aides accordées avant ou après cette entrée en vigueur. Elle ne remet pas en cause les décisions antérieures devenues définitives ni les droits de recours et de restitution ouverts sur un autre fondement ; elle ne crée pas de remboursement général des sommes régulièrement recouvrées avant cette date. Les conditions d'attribution des aides et les règles autonomes réprimant la fraude demeurent applicables, sans permettre de rétablir sur le seul fondement du présent article la suppression ou la récupération des fractions d'aide correspondant à des engagements exécutés.</p>"""
rewrite(
    'L615-4', xml,
    "Réforme de fond : remplacer la suppression et le recouvrement globaux des aides après inexécution d'engagements par une limitation aux seules aides ou fractions rattachées aux engagements inexécutés. La mise en demeure, le délai fixé par le plan et le recouvrement du montant effectivement versé restent requis ; l'aide rémunérant un engagement exécuté n'est plus perdue pour un autre manquement. Le contrôle des fonds et les règles autonomes contre la fraude subsistent.",
    "L615-1 et L615-2 ont été lus intégralement : engagements conventionnels, échéancier, financement, coordonnateur et facultés de modification/prolongation restent distincts. La mise en demeure conservée n'est pas le préavis d'un contrat de travail ; elle est suivie de l'échéance du plan, sans inventer quinze jours ni une nouvelle durée. La limitation s'applique aux décisions nouvelles même pour des aides anciennes, sans restitution générale ni réouverture des décisions définitives. Coordonner L615-5 et ses textes d'application s'ils prescrivent un retrait total au titre de ce seul manquement ; leurs autres contrôles et conditions d'aide ne sont pas supprimés. Aucun taux, plafond budgétaire ou nouvelle aide n'est inventé.",
    "Les aides correspondant aux engagements exécutés sont explicitement conservées et les futures situations éligibles continuent d'accéder aux dispositifs. Les engagements inexécutés restent contrôlés et leurs aides récupérables après mise en demeure ; la sauvegarde des avantages ne devient pas une dispense des conditions de fond ou une immunité pour fraude.",
    'mixed',
    "Le risque de retrait global et de recouvrement d'aides liées à des engagements pourtant exécutés est réduit. En contrepartie, l'autorité doit rattacher les fractions aux engagements inexécutés ; cette appréciation nouvelle peut accroître son travail. Aucun nouveau taux ni montant garanti d'aide n'est créé et le solde net de coût n'est pas établi.",
    "Le gain dépend de la ventilation des aides et engagements ; aucune remise chiffrée ni économie publique n'est établie. Les décisions définitives et les règles autonomes de fraude restent hors de cet allègement.",
    "Aucune nouvelle formalité n'est identifiée pour les bénéficiaires : aucune attestation périodique ni demande de maintien n'est ajoutée. Le rattachement des fractions d'aide aux engagements inexécutés exige une appréciation de l'autorité et peut ajouter du travail administratif ; aucun nouveau registre ni transmission n'est prescrit. Ce coût et le solde net ne sont pas chiffrés.",
    [effect(
        'relief_extended', 'sauvegarde-aides-retrait-limite-engagements-inexecutes',
        "Protection explicite des aides correspondant aux engagements exécutés lors d'un manquement au plan de sauvegarde.",
        "Suppression des aides et recouvrement des aides financières accordées aux personnes qui n'ont pas respecté leurs engagements après mise en demeure, sans limitation expresse aux fractions inexécutées.",
        "Suppression et recouvrement limités aux aides ou fractions correspondant aux engagements inexécutés, dans la limite des montants versés ; fractions correspondant aux engagements exécutés acquises.",
        'euro', "Bénéficiaires d'aides liées aux mesures de plans de sauvegarde des immeubles.",
        "Décisions nouvelles dès l'entrée en vigueur pour aides anciennes ou futures ; décisions antérieures définitives et recours propres préservés, sans remboursement général.",
        "Aucune nouvelle demande ni condition d'attribution ; appréciation individualisée des engagements et règles anti-fraude autonomes maintenues, coût administratif net non établi.",
        "Il est procédé à la suppression des aides correspondant aux mesures mentionnées à l'article L. 615-2 et au recouvrement, comme en matière de contributions directes, des aides financières accordées aux personnes qui, après mise en demeure, n'ont pas respecté les engagements qui leur incombent, dans le délai prévu au plan de sauvegarde.",
        "la suppression des aides et le recouvrement des aides financières ne portent que sur les aides ou fractions d'aide correspondant aux engagements inexécutés."
    ), effect(
        'complexity_added', 'sauvegarde-aides-retrait-limite-engagements-inexecutes',
        "Appréciation du rattachement de chaque fraction d'aide à l'engagement inexécuté avant retrait ou recouvrement.",
        "La source énonce un retrait des aides accordées à la personne défaillante sans ventilation expresse des fractions par engagement.",
        "L'autorité doit distinguer les fractions correspondant aux engagements exécutés et inexécutés pour respecter la nouvelle limite.",
        'legal_duty', "Autorités décidant le retrait ou le recouvrement des aides du plan de sauvegarde.",
        "Décisions prises dès l'entrée en vigueur, pour aides antérieures ou futures ; aucun retrait définitif ancien à refaire sur ce seul fondement.",
        "Travail d'appréciation supplémentaire possible, sans registre ou justificatif périodique imposé aux bénéficiaires ; solde net non établi.",
        "des aides financières accordées aux personnes qui, après mise en demeure, n'ont pas respecté les engagements qui leur incombent",
        "Les aides ou fractions d'aide correspondant à des engagements exécutés demeurent acquises."
    )],
    removed=["Suppression et récupération globales des aides au titre de L615-4 sans limitation aux aides ou fractions correspondant aux engagements inexécutés après mise en demeure."]
)


T_PREAVIS = 'LEGITEXT000006072050|LEGIARTI000006901112'
T_CONTRAT = 'LEGITEXT000006072050|LEGIARTI000019071087'
T_INDEMNITE = 'LEGITEXT000006072050|LEGIARTI000035644154'
T_EXECUTION = 'LEGITEXT000006074096|LEGIARTI000042338102'
T_RELOGEMENT_PRIVE = 'LEGITEXT000006074096|LEGIARTI000049397643'
T_RELOGEMENT_PUBLIC = 'LEGITEXT000006074096|LEGIARTI000049398947'
T_PENAL_POLICE = 'LEGITEXT000006074096|LEGIARTI000049778895'
T_PENAL_PM = 'LEGITEXT000006074096|LEGIARTI000049778903'
T_PENAL_PP = 'LEGITEXT000006074096|LEGIARTI000049778910'

CHECKS = {
    'L531-3': {
        T_PREAVIS: "L1234-1 règle le préavis du licenciement privé : un ou deux mois selon l'ancienneté dans la source, quinze jours calendaires sans condition d'ancienneté pour les nouveaux contrats dans la proposition, avec droits des anciens contrats et procédures spéciales distinctes. L531-3 ne vise pas ce préavis : le délai fixé par le représentant de l'Etat est un délai d'attribution de logement. Aucune notification de rupture ni ancienneté d'emploi ne remplace cette décision administrative.",
        T_CONTRAT: "L1221-2 oppose dans la source CDI normal et CDD autorisé ; la proposition impose l'emploi nouveau à durée indéterminée, conserve les anciens contrats et distingue durée d'une mission et durée d'emploi. Au 4° de L531-3, salarié ou demandeur d'emploi ouvre un contingent de relogement à Mayotte, sans exigence de CDI ou de CDD. Cet accès demeure donc pour les futurs contrats uniques comme pour les anciens contrats, sans preuve de terme d'emploi nouvelle.",
        T_INDEMNITE: "L1234-9 source ouvre l'indemnité de licenciement après huit mois, sauf faute grave. La proposition distingue les anciens contrats et exige pour le contrat unique un an au terme effectif préavis inclus, puis 0,20 mois par année totale, mois complets au prorata et plafond de six mois, employeur seul. Aucun renvoi de L531-3 ne soumet le relogement à ce seuil ou à cette indemnité ; les frais et droits de logement des salariés restent indépendants.",
        T_RELOGEMENT_PUBLIC: "Le 4° remplace le premier alinéa de L521-3-3 et vise expressément le I de L521-3-2, contrairement au renvoi de droit commun au II abrogé relevé dans le corpus. Le I organise la substitution publique faute d'hébergement ou relogement par le responsable ; la proposition conserve cette obligation et réforme seulement le forfait de frais au IV. Les désignations, réservations et délais administratifs de Mayotte gardent donc leur champ, sans ancienneté ni préavis d'emploi.",
    },
    'L542-1': {
        T_PREAVIS: "Le préavis de L1234-1 est celui de la rupture d'un emploi privé. Sa proposition de quinze jours pour les nouveaux contrats, distincte des procédures et protections spéciales, ne vise pas la signification de l'inventaire des meubles. L542-1 conserve un an de retrait à compter de cette signification et la garde prolongée faute d'offre adaptée ; aucune durée ni ancienneté de travail n'entre dans cette protection des occupants évacués.",
        T_CONTRAT: "L1221-2 proposé exclut les nouveaux CDD et l'expiration automatique de l'emploi lors de la fin d'une mission, tout en conservant les droits des anciens contrats. L542-1 protège l'occupant défini au premier alinéa de L521-1, non une catégorie de contrats de travail. L'accès à la garde des meubles et au relogement reste donc ouvert aux futurs salariés en contrat unique et aux autres occupants éligibles, sans terme professionnel ajouté.",
        T_INDEMNITE: "L1234-9 proposé ouvre l'indemnité ordinaire du contrat unique après un an à la fin effective préavis compris, sur toute l'ancienneté à 0,20 mois par année, fractions en mois complets, plafond six mois, à l'initiative patronale et sous l'exception de faute grave du texte fourni. Cela ne règle pas les frais de garde de L542-1 : aucune indemnité de travail, ancienneté de huit mois ou d'un an n'en conditionne le bénéfice, y compris après licenciement.",
        T_RELOGEMENT_PRIVE: "L521-3-1 I distingue l'hébergement temporaire, la suroccupation et l'éviction devenue définitive après trois ans ; le II impose relogement adapté et trois mois du nouveau loyer pour réinstallation, même dans certaines fins de bail. La proposition garde ces protections. Le dernier alinéa de L542-1 maintient donc l'exception à la vente ou destruction et la garde aux frais du responsable jusqu'au relogement sans retirer l'indemnité de réinstallation, distincte d'une indemnité de licenciement.",
        T_RELOGEMENT_PUBLIC: "L521-3-2 I et III organisent la substitution publique, et le VII une saisine du juge après trois offres refusées. La proposition plafonne au IV l'indemnité de frais réels à un an de loyer, interdit le double recouvrement et protège les créances anciennes, sans réduire l'obligation de reloger. Le renvoi final de L542-1 reste donc cohérent pour conserver les meubles jusqu'au relogement ; aucun nouveau seuil d'emploi ni changement du délai de retrait d'un an n'en résulte.",
    },
    'L543-1': {
        T_PREAVIS: "L1234-1 source et proposition concernent seulement le préavis de licenciement selon l'ancienneté ou le nouveau préavis de quinze jours. Le délai de L543-1 est fixé dans un arrêté de sécurité ou d'insalubrité pour exécuter des travaux et son expiration ouvre l'astreinte. Il n'est ni déclenché par une notification de rupture d'emploi ni limité par ce préavis individuel ; les notifications de l'astreinte restent nécessaires et distinctes.",
        T_CONTRAT: "La suppression des nouveaux CDD dans L1221-2 proposé concerne les relations privées d'emploi et laisse une mission ou une formation limitée sans terme automatique du contrat. Le syndic, les copropriétaires et l'autorité de L543-1 agissent ici dans une procédure de police immobilière, non dans une rupture d'emploi. La dispense d'attestation distincte ne crée donc aucun CDD spécial et ne retire aucun droit futur d'un salarié ou d'un ancien contrat.",
        T_INDEMNITE: "L1234-9 distingue l'indemnité source de licenciement à huit mois et, dans sa proposition, le seuil d'un an au terme effectif préavis inclus, l'ancienneté totale, 0,20 mois par année, fractions en mois complets et plafond de six mois pour la rupture patronale, avec transitions et indemnités spéciales. L'astreinte de L543-1 ne rémunère pas une rupture : aucune ancienneté, franchise de première année ou plafond d'indemnité de travail ne lui est applicable.",
        T_EXECUTION: "L511-16, source et proposition intégralement lues, autorise l'exécution d'office motivée et, sur les parties communes, la substitution aux seuls copropriétaires défaillants pour les sommes exigibles votées. Il conserve le contrôle du juge pour la démolition et le recours permettant de mettre une dette à la charge de l'Etat en cas de concours de force publique refusé. Le dernier alinéa de L543-1 reste cohérent : suppression de la seule attestation distincte, sans effacer votes, défaillance, motivation, subrogation, frais réels ni recours spécial.",
    },
    'L551-1': {
        T_PREAVIS: "L1234-1 proposé prévoit quinze jours pour le nouveau contrat de travail privé avec préservation des anciens préavis et des procédures spéciales. L551-1 vise une condamnation définitive à une interdiction d'achat, sa vérification avant signature et une information du maire ; aucune de ces étapes n'est un préavis de licenciement. Ni durée de quinze jours, ni ancienneté, ni notification patronale n'y est importée.",
        T_CONTRAT: "L1221-2 proposé impose un contrat d'emploi nouveau à durée indéterminée, sans fin automatique de mission et sous transition des contrats anciens. L'acte authentique et l'avant-contrat de vente de L551-1 sont des contrats immobiliers, non des contrats de travail. Le II maintient la possibilité future d'acquérir son habitation personnelle, quel que soit le statut d'emploi, sans créer une exception au contrat unique ni réserver l'avantage aux anciens CDD.",
        T_INDEMNITE: "La proposition L1234-9 calcule l'indemnité ordinaire patronale du contrat unique après un an au terme effectif préavis compris, sur l'ancienneté totale à 0,20 mois par année, mois complets au prorata et plafond six mois, avec droits anciens et spéciaux réservés. L551-1 ne vise aucune rupture de travail ou indemnité : condamnation pénale, nullité de l'avant-contrat et dérogation d'occupation personnelle restent à leur champ, sans appliquer huit mois ou un an d'ancienneté au droit d'acheter.",
        T_PENAL_POLICE: "L511-22 IV 3° et V portent l'interdiction d'achat ou d'usufruit, avec exception d'occupation personnelle pour la personne physique au IV. La proposition rend l'interdiction facultative et conserve les condamnations définitives, avec loi plus douce pour les affaires non définitivement jugées. Le I de L551-1 vérifie une peine effectivement prononcée, non sa seule possibilité ; il reste cohérent après cette réforme. Sa suppression d'un envoi fiscal ne lève pas la peine et n'étend pas silencieusement le contrôle de vente aux usufruits ou parts, champ plus large de la cible à coordonner séparément.",
        T_PENAL_PM: "Le deuxième alinéa de L184-8 est bien la peine d'interdiction d'achat ou d'usufruit encourue par les personnes morales. La proposition précise les infractions L184-4 à L184-6 et rend les peines concernées facultatives sans effacer les condamnations définitives. Ce caractère facultatif ne dispense pas le notaire de rechercher la peine effectivement prononcée au titre du I de L551-1. L'exception du II demeure celle de l'occupation personnelle et ne devient pas une immunité générale pour toutes les personnes morales.",
        T_PENAL_PP: "Le 3° de L184-7 vise les personnes physiques, leurs acquisitions ou usufruits directs, via SCI/SNC ou parts, en exceptant l'habitation personnelle. La proposition rend confiscation et interdiction facultatives, avec transition de loi pénale plus douce et protection des jugements définitifs. Le renvoi de L551-1 au 3° reste exact pour les ventes contrôlées : conserver la vérification de la peine et l'attestation personnelle future, supprimer seulement la notification fiscale spéciale, sans confondre faculté de prononcer et absence de peine.",
    },
}

for source in SOURCES:
    number = source['number']
    key = source['code_id'] + '|' + source['source_id']
    required = REFERENCES['requirements'][key]
    actual = CHECKS.get(number, {})
    assert set(required) == set(actual), (number, required, list(actual))
    if required:
        ANSWERS[number]['reference_checks'] = [
            {
                'target_key': target,
                'view_sha256': REFERENCES['targets'][target]['view_sha256'],
                'assessment': actual[target],
            }
            for target in required
        ]


def validate():
    assert len(SOURCES) == len(ANSWERS) == 24
    allowed_tags = {
        'p', 'br', 'table', 'thead', 'tbody', 'tfoot', 'tr', 'th', 'td',
        'b', 'strong', 'i', 'em', 'u', 'sup', 'sub', 'ul', 'ol', 'li',
        'div', 'span', 'blockquote',
    }
    from html.parser import HTMLParser

    class CheckHTML(HTMLParser):
        def handle_starttag(self, tag, attrs):
            assert tag in allowed_tags, tag
            assert all(k in ('rowspan', 'colspan') and v.isdigit() for k, v in attrs), attrs

        def handle_startendtag(self, tag, attrs):
            self.handle_starttag(tag, attrs)

        def handle_endtag(self, tag):
            assert tag in allowed_tags, tag

    for source in SOURCES:
        a = ANSWERS[source['number']]
        for key in ('code_id', 'source_id', 'source_sha256', 'number'):
            assert a[key] == source[key]
        assert len(a['benefit_review']) >= 100
        impact = a['substantive_impact']
        assert impact['version'] == 1
        for key in ('assessment', 'scope_limitations', 'new_burdens_review'):
            assert len(impact[key]) >= 40, (a['number'], key)
        if a['status'] == 'retained_unchanged':
            assert a['proposed_xml'] is None
            assert a['classification'] == impact['classification'] == 'retained_necessary'
            assert impact['effects'] == []
        else:
            assert a['status'] == 'rewrite_draft'
            assert a['proposed_xml']
            CheckHTML().feed(a['proposed_xml'])
            if a.get('change_type') == 'full_repeal':
                assert plain(a['proposed_xml']).startswith('Le présent article est abrogé')
                assert len(a['repeal_scope']) >= 30
                assert a['repeal_policy_id'] == 'editorial_direction_2026_10_19'
            if a.get('change_type') == 'normative_reduction':
                assert a['reform_policy_id'] == 'editorial_direction_2026_10_19'
                assert all(len(x) >= 30 for x in a['removed_provisions'])
            for e in impact['effects']:
                assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', e['measure_id'])
                assert 6 <= len(e['measure_id']) <= 96
                assert len(e['source_quote']) >= 12
                assert len(e['proposed_quote']) >= 12
                assert e['source_quote'] in plain(source['source_xml']), (a['number'], 'source quote', e['source_quote'])
                assert e['proposed_quote'] in plain(a['proposed_xml']), (a['number'], 'proposed quote', e['proposed_quote'])
                assert e['unit'] in ('percent', 'euro', 'legal_duty', 'regime', 'calendar_days', 'working_days', 'financing', 'other')
        required = REFERENCES['requirements'][source['code_id'] + '|' + source['source_id']]
        checks = a.get('reference_checks', [])
        assert [x['target_key'] for x in checks] == required
        for check in checks:
            assert check['view_sha256'] == REFERENCES['targets'][check['target_key']]['view_sha256']
            assert len(check['assessment']) >= 80


validate()
output = [ANSWERS[a['number']] for a in SOURCES]
Path('answer.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({
    'articles': len(output),
    'retained': sum(a['status'] == 'retained_unchanged' for a in output),
    'rewritten': sum(a['status'] == 'rewrite_draft' for a in output),
    'reference_checks': sum(len(a.get('reference_checks', [])) for a in output),
    'effects': sum(len(a['substantive_impact']['effects']) for a in output),
    'output_bytes': Path('answer.json').stat().st_size,
}, ensure_ascii=False))
