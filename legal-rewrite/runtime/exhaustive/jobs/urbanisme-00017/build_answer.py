import json
from pathlib import Path


drafts = {}


def add(number, xml, reason, notes):
    assert number not in drafts
    drafts[number] = {
        "proposed_xml": xml.strip(),
        "reason": reason,
        "review_notes": notes,
    }


add(
    "L211-2-1",
    """
<p>Dans les départements et régions d'outre-mer, le titulaire du droit de préemption peut aussi en déléguer l'exercice à un organisme d'habitations à loyer modéré mentionné à l'article L. 411-2 du code de la construction et de l'habitation. Il ne peut accorder cette délégation qu'à l'occasion de l'aliénation d'un bien nécessaire à l'accomplissement des missions prévues au même article L. 411-2.</p>
""",
    "Réécriture à droit constant : le titulaire qui accorde la délégation et la condition tenant aux missions de l'organisme sont exprimés directement. Aucune réforme de fond de la délégation ultramarine n'est prévue par policy.json.",
    "Champ limité aux départements et régions d'outre-mer ; nécessité du bien pour les missions de l'article L. 411-2 et délégation à l'occasion d'une aliénation conservées. L'articulation avec les autres délégations prévues à L. 211-2 reste inchangée.",
)

add(
    "L211-2-2",
    """
<p>En Guadeloupe et en Martinique, le titulaire du droit de préemption peut aussi en déléguer l'exercice aux agences pour la mise en valeur des espaces urbains de la zone dite des cinquante pas géométriques, mentionnées à l'article 4 de la loi n° 96-1241 du 30 décembre 1996 relative à l'aménagement, la protection et la mise en valeur de la zone dite des cinquante pas géométriques dans les départements d'outre-mer. Cette délégation est limitée aux espaces urbains et aux secteurs occupés par une urbanisation diffuse délimités conformément aux articles L. 5112-1 et L. 5112-2 du code général de la propriété des personnes publiques.</p>
""",
    "Réécriture à droit constant : la faculté de délégation et son périmètre géographique sont présentés dans deux phrases distinctes. Les orientations de réforme n'appellent aucune modification de fond de ce régime.",
    "Guadeloupe et Martinique, catégories d'espaces concernées, article 4 de la loi n° 96-1241 du 30 décembre 1996 et renvois à L. 5112-1 et L. 5112-2 conservés. Aucune extension à l'ensemble des territoires ultramarins.",
)

add(
    "L211-2-3",
    """
<p>Le titulaire du droit de préemption urbain peut déléguer ce droit à une personne y ayant vocation à laquelle a été confiée, en application de l'article L. 300-9, la réalisation d'actions ou d'opérations relevant de l'une des catégories suivantes : celles prévues aux 6°, 8° et 9° du III de l'article L. 303-2 du code de la construction et de l'habitation, dans les secteurs d'intervention délimités d'une opération de revitalisation de territoire mentionnée au même article L. 303-2 ; ou celles destinées à favoriser la diversité, le maintien ou le développement d'activités artisanales et commerciales de proximité dans des espaces urbains, à l'intérieur du périmètre délimité en application de l'article L. 214-1 du présent code.</p>
<p>Le droit ainsi délégué peut aussi, le cas échéant, s'exercer sur les aliénations et cessions mentionnées à l'article L. 211-4, dans les conditions prévues aux deux derniers alinéas du même article L. 211-4.</p>
<p>Les biens acquis par l'exercice de ce droit sont intégrés au patrimoine du délégataire.</p>
""",
    "Réécriture à droit constant : les deux catégories d'opérations justifiant la délégation sont distinguées dans le premier alinéa et les effets de la délégation sont formulés directement. Aucune modification de fond n'est issue de policy.json pour cet article.",
    "Les trois alinéas de fond sont conservés. Renvois à L. 300-9, aux 6°, 8° et 9° du III de L. 303-2, à L. 214-1 et aux deux derniers alinéas de L. 211-4 maintenus. La réécriture de L. 211-4 conserve ces deux alinéas à leur place ; aucune délégation autonome en dehors des opérations confiées n'est créée.",
)

add(
    "L211-2-4",
    """
<p>I. - Le droit de préemption institué dans les conditions du présent chapitre peut être exercé pour réaliser une opération programmée d'amélioration de l'habitat prévue à l'article L. 303-1 du code de la construction et de l'habitation, un plan de sauvegarde prévu à l'article L. 615-1 du même code ou une opération de requalification de copropriétés dégradées prévue à l'article L. 741-1 de ce code.</p>
<p>II. - Pour réaliser les actions ou opérations mentionnées au I, le titulaire du droit de préemption urbain peut déléguer ce droit au concessionnaire d'une opération d'aménagement mentionnée à l'article L. 300-4 ou d'actions mentionnées à l'article L. 300-10.</p>
<p>Le droit ainsi délégué peut également, le cas échéant, s'exercer sur les aliénations et cessions mentionnées à l'article L. 211-4.</p>
<p>Les biens acquis par l'exercice de ce droit sont intégrés au patrimoine du délégataire.</p>
""",
    "Réécriture à droit constant : les finalités d'exercice du droit et les délégations au concessionnaire sont formulées avec des verbes directs. Les subdivisions I et II et les quatre alinéas sont conservés ; aucune réforme de fond de ce dispositif n'est prévue.",
    "Les trois dispositifs du CCH et les deux fondements de concession restent distincts. Le renvoi à L. 211-4 est conservé sans lui ajouter la condition des deux derniers alinéas propre à la rédaction de L. 211-2-3. Aucune suppression d'obligations de logement social n'est introduite.",
)

add(
    "L211-3",
    """
<p>Les aliénations de biens et de droits immobiliers ayant fait l'objet de la notification prévue à l'article L. 240-3 du présent code sont exclues du droit de préemption urbain. Cette exclusion s'applique également à l'aliénation d'un terrain au profit du preneur d'un bail à construction conclu dans le cadre de l'opération d'accession sociale à la propriété prévue au dernier alinéa de l'article L. 251-1 du code de la construction et de l'habitation.</p>
""",
    "Réécriture à droit constant : les deux exclusions sont exposées successivement dans le même alinéa pour rendre leur champ plus lisible. Aucune mesure de policy.json ne modifie ces exclusions.",
    "Les renvois à L. 240-3 et au dernier alinéa de L. 251-1 sont conservés. Ce dernier alinéa a été vérifié dans le corpus public : il concerne l'achat du terrain par le preneur dans une opération d'accession sociale. L'exclusion ne devient pas générale pour tous les baux à construction.",
)

add(
    "L211-4",
    """
<p>Le droit de préemption urbain ne s'applique pas :</p>
<p>a) À l'aliénation d'un ou plusieurs lots constitués soit d'un seul local à usage d'habitation, à usage professionnel ou à usage professionnel et d'habitation, soit d'un tel local et de ses locaux accessoires, soit d'un ou plusieurs locaux accessoires d'un tel local. Ces lots doivent être compris dans un bâtiment effectivement soumis, à la date du projet d'aliénation, au régime de la copropriété : soit à la suite du partage total ou partiel d'une société d'attribution ; soit, lorsque la mise en copropriété ne résulte pas d'un tel partage, depuis au moins dix ans. Dans ce dernier cas, le délai court à compter de la publication du règlement de copropriété au fichier immobilier ;</p>
<p>b) À la cession de parts ou d'actions des sociétés visées aux titres II et III de la loi n° 71-579 du 16 juillet 1971, lorsque ces parts ou actions donnent vocation à l'attribution d'un local d'habitation, d'un local professionnel ou d'un local mixte et de ses locaux accessoires ;</p>
<p>c) À l'aliénation d'un immeuble bâti pendant les quatre ans qui suivent son achèvement.</p>
<p>Toutefois, la commune peut, par une délibération motivée, soumettre à ce droit de préemption les aliénations et cessions mentionnées au présent article, sur tout ou partie du territoire soumis à ce droit.</p>
<p>Pour mettre en œuvre le deuxième alinéa de l'article L. 210-1, le représentant de l'Etat dans le département peut également, par un arrêté motivé, soumettre à ce droit de préemption les aliénations et cessions mentionnées au présent article, sur tout ou partie du territoire soumis à ce droit.</p>
""",
    "Réécriture à droit constant : la longue condition de copropriété du a) est décomposée en phrases, sans créer d'alinéa supplémentaire. Les exclusions b) et c) et les deux possibilités d'extension motivée sont clarifiées, sans réforme de fond.",
    "Les six alinéas, les lettres a), b), c), les titres II et III et la loi n° 71-579 du 16 juillet 1971 sont maintenus. Le délai de dix ans du a), son point de départ et celui de quatre ans du c) sont conservés. Les deux derniers alinéas demeurent les cibles du renvoi de L. 211-2-3. Incohérence préexistante signalée dans L. 213-1 : celui-ci évoque un délai de dix ans au c), alors que le présent c) prévoit quatre ans ; aucun des deux délais n'est corrigé silencieusement.",
)

add(
    "L211-5",
    """
<p>Le propriétaire d'un bien soumis au droit de préemption peut proposer au titulaire de ce droit d'acquérir le bien, au prix qu'il indique. Le titulaire doit se prononcer dans les deux mois suivant cette proposition. Le maire en transmet une copie au directeur départemental des finances publiques.</p>
<p>Si aucun accord amiable n'est trouvé, la juridiction compétente en matière d'expropriation fixe le prix selon les règles mentionnées à l'article L. 213-4.</p>
<p>Si le bien est acquis, les dispositions de l'article L. 213-14 s'appliquent.</p>
<p>Si le titulaire du droit de préemption refuse l'acquisition ou ne répond pas dans le délai de deux mois prévu au premier alinéa, le propriétaire bénéficie des dispositions de l'article L. 213-8.</p>
<p>Les articles L. 213-11 et L. 213-12 ne s'appliquent pas aux biens acquis dans les conditions du présent article.</p>
""",
    "Réécriture à droit constant : les obligations du titulaire et du maire sont explicitées et les suites de l'offre sont présentées dans les cinq alinéas existants. Les orientations de réforme ne modifient ni ce droit de délaissement ni ses délais.",
    "Délai de deux mois à compter de la proposition maintenu. Renvois à L. 213-4, L. 213-14 et L. 213-8 et exclusions de L. 213-11 et L. 213-12 conservés. Le refus ou le silence n'est pas assimilé à la disparition du droit prévue, dans un autre régime, à L. 212-3.",
)

add(
    "L211-7",
    """
<p>Les conditions d'application du présent chapitre sont précisées, si nécessaire, par décret en Conseil d'Etat.</p>
""",
    "Réécriture à droit constant : la formule de renvoi réglementaire est rendue plus directe, en conservant son caractère conditionnel. Aucune modification de fond.",
    "Maintien du décret en Conseil d'Etat et de la réserve de nécessité ; aucune habilitation réglementaire nouvelle ni date d'application ajoutée.",
)

add(
    "L212-1",
    """
<p>Le représentant de l'Etat dans le département peut créer une zone d'aménagement différé par une décision motivée, sur proposition de la commune ou après avoir recueilli son avis, et après avis de l'établissement public de coopération intercommunale ayant les compétences visées au deuxième alinéa de l'article L. 211-2. Les zones urbaines ou d'urbanisation future délimitées par un plan d'occupation des sols rendu public ou par un plan local d'urbanisme approuvé cessent d'être soumises au droit de préemption urbain institué sur ces territoires dès lors qu'elles sont comprises dans une zone d'aménagement différé ou dans son périmètre provisoire.</p>
<p>Si la commune ou l'établissement public compétent émet un avis défavorable, la zone d'aménagement différé ne peut être créée que par décret en Conseil d'Etat.</p>
<p>L'organe délibérant de l'établissement public de coopération intercommunale à fiscalité propre ayant les compétences mentionnées au deuxième alinéa de l'article L. 211-2 peut également créer une zone d'aménagement différé par une délibération motivée, après avis des communes comprises dans le périmètre de la zone.</p>
<p>Si l'une de ces communes émet un avis défavorable, la zone ne peut être créée que par arrêté du représentant de l'Etat dans le département. Lorsqu'elle s'étend sur plusieurs départements, sa création exige un arrêté conjoint des représentants de l'Etat dans les départements concernés.</p>
<p>L'organe délibérant d'un établissement public territorial créé en application de l'article L. 5219-2 du code général des collectivités territoriales peut également créer une zone d'aménagement différé par une délibération motivée. Il recueille au préalable l'avis des communes dont le territoire est compris en tout ou partie dans le périmètre de la zone. Cette création n'est possible qu'en dehors des périmètres fixés par le conseil de la métropole du Grand Paris pour mettre en œuvre les opérations d'aménagement d'intérêt métropolitain mentionnées à l'article L. 5219-1 du même code.</p>
<p>Si une commune émet un avis défavorable, la zone ne peut être créée que par arrêté du représentant de l'Etat dans le département. Lorsqu'elle s'étend sur plusieurs départements, sa création exige un arrêté conjoint des représentants de l'Etat dans les départements concernés.</p>
""",
    "Réécriture à droit constant : les trois voies de création et les effets des avis défavorables sont exprimés avec leur autorité compétente. Les règles de substitution au droit de préemption urbain et les périmètres métropolitains sont conservés ; aucune réforme de fond.",
    "Les six alinéas de fond, y compris les deux séparés par des br dans le dernier p source, sont conservés. L'avis défavorable ne produit pas la même procédure selon la voie initiale : décret en Conseil d'Etat pour la première, arrêté préfectoral ou conjoint pour les deux autres. Les références historiques aux plans d'occupation des sols restent présentes. Renvois au deuxième alinéa de L. 211-2 et à L. 5219-1 et L. 5219-2 maintenus.",
)

add(
    "L212-2",
    """
<p>Dans une zone d'aménagement différé, une collectivité publique, un établissement public y ayant vocation ou le concessionnaire d'une opération d'aménagement peut être titulaire d'un droit de préemption. Ce droit peut être exercé pendant une période renouvelable de six ans à compter de la publication de l'acte créant la zone, sous réserve de l'article L. 212-2-1.</p>
<p>L'acte qui crée la zone désigne le titulaire de ce droit.</p>
<p>La période mentionnée au premier alinéa est renouvelée selon les modalités de l'article L. 212-1. L'acte renouvelant le droit de préemption peut être pris selon une modalité différente de celle retenue pour créer la zone.</p>
""",
    "Réécriture à droit constant : les titulaires possibles, la durée du droit et la procédure de renouvellement sont séparés en phrases plus courtes, dans les trois alinéas existants. Aucune réforme de fond du régime des zones d'aménagement différé.",
    "Période de six ans renouvelable et point de départ à la publication conservés, avec la réserve de L. 212-2-1 pour le périmètre provisoire. Le renouvellement reste soumis à L. 212-1 sans identité obligatoire de modalité avec la création.",
)

add(
    "L212-2-1",
    """
<p>Le représentant de l'Etat dans le département peut, par arrêté, délimiter le périmètre provisoire d'une zone d'aménagement différé lorsqu'il est saisi d'une proposition de création par la commune ou l'établissement public de coopération intercommunale compétent, ou lorsqu'il demande à la commune ou à cet établissement un avis sur un tel projet.</p>
<p>De la publication de cet arrêté à celle de l'acte créant la zone d'aménagement différé, l'Etat dispose d'un droit de préemption dans le périmètre provisoire. Dans ce périmètre, les zones urbaines ou d'urbanisation future délimitées par un plan d'occupation des sols rendu public ou par un plan local d'urbanisme approuvé cessent d'être soumises au droit de préemption urbain institué sur ces territoires.</p>
<p>L'arrêté qui délimite le périmètre provisoire peut attribuer ce droit de préemption à un autre titulaire.</p>
<p>Si l'acte créant la zone d'aménagement différé n'est pas publié dans les deux ans suivant la publication de l'arrêté délimitant le périmètre provisoire, cet arrêté devient caduc à l'expiration de ce délai.</p>
<p>Par dérogation à l'article L. 212-2, la période renouvelable de six ans pendant laquelle le droit de préemption peut être exercé court à compter de la publication de l'acte délimitant le périmètre provisoire, et non de celle de l'acte créant la zone d'aménagement différé.</p>
""",
    "Réécriture à droit constant : les circonstances de délimitation, les effets provisoires et les deux délais sont formulés directement dans les cinq alinéas existants. Aucun nouveau régime ni allongement de délai n'est introduit.",
    "Caducité après deux ans sans publication de l'acte de création et calcul de la période de six ans depuis l'acte provisoire conservés. La désignation possible d'un autre titulaire demeure facultative. Les plans d'occupation des sols restent mentionnés ; coordination maintenue avec L. 212-1, L. 212-2 et L. 212-2-2.",
)

add(
    "L212-2-2",
    """
<p>À la publication de l'acte créant la zone d'aménagement différé, les biens immobiliers acquis par décision de préemption et qui n'ont pas été utilisés pour l'un des objets mentionnés à l'article L. 210-1 sont cédés au titulaire du droit de préemption s'ils sont compris dans le périmètre définitif. S'ils sont situés hors de ce périmètre, ils sont rétrocédés à leurs anciens propriétaires ou à leurs ayants cause universels ou à titre universel dans l'année suivant la publication de l'acte créant la zone. Dans ce dernier cas, les quatrième, cinquième, sixième et septième alinéas de l'article L. 213-11 s'appliquent.</p>
<p>Les règles de rétrocession prévues au premier alinéa s'appliquent également lorsque l'arrêté délimitant le périmètre provisoire devient caduc dans les conditions prévues à l'article L. 212-2-1.</p>
""",
    "Réécriture à droit constant : les sorts respectifs des biens compris dans le périmètre définitif et de ceux qui en sont exclus sont distingués en phrases, sans déplacer les deux alinéas. Aucune réforme de fond.",
    "Le délai d'un an reste rattaché à la rétrocession des biens hors périmètre ; il n'est pas étendu à la cession au titulaire. Le second alinéa ne précise pas le point de départ de ce délai en cas de caducité de l'arrêté provisoire ; aucune date n'est suppléée. Le renvoi aux quatrième à septième alinéas de L. 213-11 est conservé. Point de coordination préexistant à contrôler : dans le corpus public, le quatrième alinéa de L. 213-11 vise un changement d'affectation et son huitième conditionne la procédure au nom de l'acquéreur dans la déclaration ; le renvoi existant ne couvre donc pas tout cet ensemble procédural. Aucune renumérotation ou extension de renvoi n'est effectuée ici.",
)

add(
    "L212-3",
    """
<p>La personne qui est propriétaire d'un bien soumis au droit de préemption à la date de publication de l'acte instituant la zone d'aménagement différé ou délimitant son périmètre provisoire peut proposer au titulaire de ce droit d'acquérir le bien, au prix qu'elle indique. Ses ayants cause universels ou à titre universel disposent de la même faculté. Le titulaire doit se prononcer dans les deux mois suivant cette proposition. Le maire en transmet une copie au directeur départemental des finances publiques.</p>
<p>Si aucun accord amiable n'est trouvé, la juridiction compétente en matière d'expropriation fixe le prix selon les règles mentionnées à l'article L. 213-4.</p>
<p>Si le bien est acquis, les dispositions de l'article L. 213-14 s'appliquent.</p>
<p>Si le titulaire refuse l'acquisition ou ne répond pas dans les deux mois, le bien concerné cesse d'être soumis au droit de préemption.</p>
<p>Les articles L. 213-11 et L. 213-12 ne s'appliquent pas aux biens acquis dans les conditions du présent article.</p>
""",
    "Réécriture à droit constant : la qualité de propriétaire à la date requise et la faculté des ayants cause sont explicitées ; les obligations de réponse et de transmission sont formulées séparément. Les effets propres à ce droit de délaissement sont maintenus, sans réforme de fond.",
    "Les cinq alinéas de fond sont conservés. La faculté n'est pas étendue aux acquéreurs à titre particulier postérieurs à la publication. Délai de deux mois et cessation de l'assujettissement au droit en cas de refus ou de silence maintenus ; renvois à L. 213-4 et L. 213-14 et exclusions de L. 213-11 et L. 213-12 conservés.",
)

add(
    "L212-4",
    """
<p>Une commune membre d'un établissement public de coopération intercommunale ayant vocation à exercer les compétences prévues au présent chapitre peut lui déléguer tout ou partie de celles qui lui sont attribuées par ce chapitre. Cette délégation exige l'accord de l'établissement.</p>
""",
    "Réécriture à droit constant : la faculté de délégation et l'accord nécessaire de l'établissement sont exprimés dans deux phrases du même alinéa. Aucune modification de fond.",
    "La qualité de membre de l'établissement, sa vocation à exercer les compétences et son accord demeurent requis. La délégation peut toujours être totale ou partielle et reste limitée au présent chapitre.",
)

add(
    "L212-5",
    """
<p>Les conditions d'application du présent chapitre sont précisées, si nécessaire, par décret en Conseil d'Etat.</p>
""",
    "Réécriture à droit constant : le renvoi aux mesures réglementaires d'application est reformulé sans changer l'autorité ni le caractère conditionnel de ces mesures. Aucune réforme de fond.",
    "Le renvoi reste limité au présent chapitre et à un décret en Conseil d'Etat pris en tant que de besoin. Aucune date nouvelle n'est fixée.",
)

add(
    "L213-1",
    """
<p>Le droit de préemption institué par l'un ou l'autre des deux chapitres précédents s'applique :</p>
<p>1° À tout immeuble, bâti ou non bâti, ainsi qu'à tout ensemble de droits sociaux donnant vocation à l'attribution en propriété ou en jouissance d'un immeuble ou d'une partie d'immeuble, bâti ou non bâti, lorsqu'ils font l'objet d'une aliénation à titre onéreux, quelle qu'en soit la forme. Sont toutefois exclus les immeubles et droits compris dans un plan de cession arrêté en application de l'article L. 631-22 ou des articles L. 642-1 et suivants du code de commerce ;</p>
<p>2° Aux cessions de droits indivis sur un immeuble ou une partie d'immeuble, bâti ou non bâti, sauf si la cession est consentie à un coïndivisaire, ainsi qu'aux cessions de tantièmes contre remise de locaux à construire ;</p>
<p>3° Aux cessions de la majorité des parts d'une société civile immobilière et aux cessions qui conduisent un acquéreur à détenir la majorité de ses parts, lorsque le patrimoine de la société est constitué d'une unité foncière, bâtie ou non, dont la cession serait soumise au droit de préemption. Ce 3° ne s'applique pas aux sociétés civiles immobilières constituées exclusivement entre parents et alliés jusqu'au quatrième degré inclus ;</p>
<p>4° Aux immeubles construits ou acquis par les organismes mentionnés à l'article L. 411-2 du code de la construction et de l'habitation et dont ces organismes sont propriétaires, sous réserve des droits reconnus aux locataires par l'article L. 443-11 du même code. Sont toutefois exclus les immeubles ayant fait l'objet d'une décision d'agrément du représentant de l'Etat dans le département pour la construction ou l'acquisition de logements neufs faisant l'objet d'un contrat de location-accession régi par la loi n° 84-595 du 12 juillet 1984 définissant la location-accession à la propriété immobilière.</p>
<p>Lorsqu'il acquiert un bien faisant l'objet d'une adjudication autorisée ou ordonnée par un juge, le titulaire du droit de préemption se substitue à l'adjudicataire au prix de la dernière enchère. Cette règle ne s'applique pas à une vente mettant fin à une indivision créée volontairement, sauf si cette indivision résulte d'une donation-partage.</p>
<p>Pour un contrat de location-accession régi par la loi n° 84-595 du 12 juillet 1984 définissant la location-accession à la propriété immobilière, le droit de préemption s'exerce avant la signature du contrat, et non lors de la levée de l'option par l'accédant. Le délai de dix ans mentionné au a) et au c) de l'article L. 211-4 s'apprécie à la date de signature du contrat.</p>
<p>Le droit de préemption ne s'applique pas :</p>
<p>a) Aux immeubles construits par les sociétés coopératives d'habitations à loyer modéré de location-attribution, ni aux immeubles construits ou acquis par les organismes mentionnés à l'article L. 411-2 du code de la construction et de l'habitation, dont ces organismes sont propriétaires, et qui ont fait l'objet d'une décision d'agrément du représentant de l'Etat dans le département pour la construction ou l'acquisition de logements neufs faisant l'objet d'un contrat de location-accession régi par la loi n° 84-595 du 12 juillet 1984 précitée ;</p>
<p>b) Aux immeubles faisant l'objet d'un contrat de vente d'immeuble à construire dans les conditions prévues aux articles 1601-1 et suivants du code civil, sauf lorsque ces dispositions sont appliquées à des bâtiments existants ;</p>
<p>c) Aux parts ou actions des sociétés d'attribution visées aux chapitres II et III du titre Ier du livre II du code de la construction et de l'habitation, lorsque leur cession intervient avant l'achèvement de l'immeuble ou dans les dix ans qui suivent cet achèvement ;</p>
<p>d) Aux immeubles cédés au locataire en exécution de la promesse de vente figurant dans un contrat de crédit-bail immobilier conclu en application du 2 de l'article L. 313-7 du code monétaire et financier ;</p>
<p>e) Aux immeubles faisant l'objet d'une mise en demeure d'acquérir en application des articles L. 152-2, L. 311-2 ou L. 424-1, ou des articles L. 241-1 et L. 241-2 du code de l'expropriation pour cause d'utilité publique ;</p>
<p>f) (Abrogé) ;</p>
<p>g) Aux aliénations de terrains, bâtis ou non bâtis, par l'Etat, ses établissements publics ou les sociétés dont il détient la majorité du capital, lorsque ces aliénations ont pour objet soit de réaliser des logements situés dans les périmètres mentionnés au deuxième alinéa du I de l'article 1er de la loi n° 2006-872 du 13 juillet 2006 portant engagement national pour le logement, tant que les décrets prévus à ce même alinéa ne sont pas caducs, soit de réaliser les opérations d'intérêt national mentionnées à l'article L. 132-1 ;</p>
<p>h) Aux transferts en pleine propriété d'immeubles appartenant à l'Etat ou à ses établissements publics, lorsqu'ils sont réalisés conformément à l'article 141 de la loi n° 2006-1771 du 30 décembre 2006 de finances rectificative pour 2006 ;</p>
<p>i) Aux biens acquis par un organisme visé aux articles L. 321-4 et L. 324-1, lorsqu'il agit à la demande expresse de la collectivité titulaire du droit de préemption urbain ;</p>
<p>j) Aux cessions entre la société nationale SNCF mentionnée à l'article L. 2101-1 du code des transports, la société SNCF Réseau et sa filiale respectivement mentionnées à l'article L. 2111-9 du même code et au 5° de cet article, la société SNCF Voyageurs mentionnée à l'article L. 2141-1 de ce code et la société chargée des activités relatives à la fourniture des services de transport ferroviaire de marchandises mentionnée au c du 2° du I de l'article 18 de l'ordonnance n° 2019-552 du 3 juin 2019 portant diverses dispositions relatives au groupe SNCF. Cette exclusion s'applique lorsque les biens concernés sont nécessaires aux missions de service public confiées à ces sociétés par les dispositions mentionnées au présent alinéa ;</p>
<p>k) Aux cessions à la Société des grands projets, créée par l'article 7 de la loi n° 2010-597 du 3 juin 2010 relative au Grand Paris, de biens nécessaires à la réalisation et à l'exploitation de projets d'infrastructures déclarés d'utilité publique, lorsque ces projets mettent en œuvre le schéma d'ensemble du réseau de transport public du Grand Paris en application de l'article 2 de la même loi ou lorsque leur maîtrise d'ouvrage est confiée à cette société en application des articles 20-2 et 20-3 de cette loi.</p>
""",
    "Réécriture à droit constant : les quatre catégories soumises au droit et les onze lettres d'exclusion sont conservées intégralement. Les conditions relatives aux sociétés, à l'adjudication, à la location-accession et aux opérateurs publics sont exprimées en phrases plus courtes, sans déplacement d'alinéa ni réforme de fond.",
    "Les dix-neuf alinéas, les 1° à 4°, les a) à k) et la mention f) (Abrogé) sont conservés. Incohérence préexistante maintenue et signalée : l'alinéa relatif à la location-accession vise un délai de dix ans au a) et au c) de L. 211-4, tandis que le c) de cet article prévoit quatre ans. Aucun délai n'est corrigé sans coordination expresse. Les conditions relatives aux agréments de location-accession, aux sociétés familiales jusqu'au quatrième degré, aux décrets non caducs et aux missions de service public ferroviaire sont maintenues. L'exclusion des ventes d'immeubles à construire conserve son exception pour l'application de ces dispositions à des bâtiments existants. Les dates des lois citées restent des références historiques, sans date future de réforme.",
)

add(
    "L213-1-1",
    """
<p>Les immeubles et ensembles de droits sociaux mentionnés au 1° de l'article L. 213-1 sont également soumis au droit de préemption lorsqu'ils font l'objet d'une donation entre vifs. En sont toutefois exclues les donations consenties :</p>
<p>1° Entre ascendants et descendants ;</p>
<p>2° Entre collatéraux jusqu'au sixième degré ;</p>
<p>3° Entre époux ou entre partenaires d'un pacte civil de solidarité ;</p>
<p>4° Entre une personne et les descendants de son conjoint ou de son partenaire de pacte civil de solidarité, ou entre ces descendants.</p>
<p>Les aliénations mentionnées au premier alinéa relèvent du présent chapitre. Toutefois, par dérogation au premier alinéa de l'article L. 213-2, la déclaration adressée à la mairie ne comporte pas de prix. Si le titulaire du droit de préemption décide d'acquérir le bien, sa décision indique l'estimation du bien faite par les services fiscaux.</p>
""",
    "Réécriture à droit constant : le principe d'assujettissement des donations et ses quatre exceptions sont exposés directement ; la règle spéciale de déclaration et le contenu de la décision sont clarifiés. Aucune réforme de fond des donations.",
    "Les six alinéas de fond et les 1° à 4° sont conservés ; seuls les espacements et le paragraphe vide de la source sont retirés. Le sixième degré des collatéraux, les descendants du conjoint ou du partenaire et les donations entre ces descendants sont maintenus. L'absence de prix déclaré n'efface pas l'obligation de faire figurer l'estimation fiscale dans la décision d'acquérir.",
)

add(
    "L213-1-2",
    """
<p>Le droit de préemption s'applique également aux immeubles et ensembles de droits sociaux mentionnés au 1° de l'article L. 213-1 lorsqu'ils sont apportés en nature à une société civile immobilière. Dans ce cas, le déclarant joint à la déclaration d'intention d'aliéner un état de la situation sociale, financière et patrimoniale de cette société.</p>
""",
    "Réécriture à droit constant : l'apport en nature et l'obligation documentaire qui l'accompagne sont exprimés par des verbes directs, avec un sujet explicite pour la transmission. Aucune modification de fond.",
    "Champ limité aux biens et droits visés au 1° de L. 213-1 et aux apports en nature à une société civile immobilière. Les trois composantes de l'état joint, sociale, financière et patrimoniale, sont conservées ; aucune pièce supplémentaire n'est ajoutée.",
)

add(
    "L213-2",
    """
<p>Avant toute aliénation visée à l'article L. 213-1, le propriétaire doit adresser une déclaration à la mairie de la commune où se situe le bien, à peine de nullité de l'aliénation. Cette déclaration indique obligatoirement le prix et les conditions de l'aliénation projetée ou, en cas d'adjudication, l'estimation du bien ou sa mise à prix. Elle comprend aussi les informations dues au titre de l'article L. 514-20 du code de l'environnement. Dans le délai de deux mois prévu au troisième alinéa du présent article, le titulaire du droit de préemption peut adresser au propriétaire une seule demande de communication de documents permettant d'apprécier la consistance et l'état de l'immeuble et, le cas échéant, la situation sociale, financière et patrimoniale de la société civile immobilière. Un décret en Conseil d'Etat fixe la liste limitative des documents pouvant être demandés. La déclaration d'intention d'aliéner peut être dématérialisée. Le cas échéant, elle comprend également les informations dues au titre des articles L. 303-2 et L. 741-1 du code de la construction et de l'habitation.</p>
<p>Si la contrepartie de l'aliénation est payée en nature, la déclaration indique le prix auquel cette contrepartie est estimée.</p>
<p>Lorsque le représentant de l'Etat dans le département exerce le droit de préemption dans les conditions prévues au deuxième alinéa de l'article L. 210-1, le maire lui transmet la déclaration dans les sept jours ouvrés suivant sa réception. À défaut de transmission, le représentant de l'Etat dans le département peut informer le maire, par lettre recommandée avec demande d'avis de réception, de son intention de faire dresser procès-verbal de ce manquement. Le maire dispose de sept jours à compter de la réception de cette lettre pour présenter ses observations. À l'expiration de ce délai et au vu de ces observations, le représentant de l'Etat dans le département peut décider de constater par procès-verbal l'absence de transmission de la déclaration. Une amende forfaitaire de 1 000 € est alors mise en recouvrement. La commune en est redevable sur le fondement d'un titre de perception émis par le représentant de l'Etat dans le département. Le produit de l'amende est versé au Fonds national des aides à la pierre mentionné à l'article L. 435-1 du code de la construction et de l'habitation si la commune se situe en métropole, ou au fonds régional d'aménagement foncier et urbain mentionné à l'article L. 340-2 du présent code si elle se situe dans un département d'outre-mer. L'avis de mise en recouvrement du titre de perception de l'amende forfaitaire reçu par le maire peut être contesté par un recours de pleine juridiction.</p>
<p>Le titulaire du droit de préemption qui garde le silence pendant deux mois à compter de la réception de la déclaration mentionnée au premier alinéa est réputé renoncer à exercer ce droit.</p>
<p>Ce délai est suspendu à compter de la réception de la demande de documents mentionnée au premier alinéa ou de la demande de visite du bien. Il reprend son cours lorsque le titulaire du droit de préemption reçoit les documents, lorsque le propriétaire refuse la visite ou lorsque le titulaire effectue cette visite. Si le délai restant à courir est inférieur à un mois, le titulaire dispose d'un mois pour décider. Son silence à l'expiration de ces délais vaut renonciation à l'exercice du droit de préemption.</p>
<p>Le titulaire du droit de préemption qui envisage d'acquérir le bien transmet sans délai une copie de la déclaration d'intention d'aliéner au responsable départemental des services fiscaux. Il publie sa décision et la notifie au vendeur, au notaire et, le cas échéant, à la personne désignée dans la déclaration comme ayant l'intention d'acquérir le bien. Le notaire transmet cette décision aux titulaires de droits d'emphytéose, d'habitation ou d'usage, aux bénéficiaires de servitudes, aux fermiers et aux locataires mentionnés dans la déclaration d'intention d'aliéner.</p>
<p>Le titulaire du droit de préemption peut demander à visiter le bien selon les conditions fixées par décret.</p>
<p>L'action en nullité prévue au premier alinéa se prescrit par cinq ans à compter de la publication de l'acte transférant la propriété.</p>
""",
    "Réécriture à droit constant : les obligations déclaratives, la procédure de sanction de la commune, le calcul des délais et les destinataires des notifications sont explicités, en conservant les huit alinéas. Le dossier coordonné d'autorisation prévu pour L. 423-1 par les orientations de réforme n'est pas étendu à cette procédure distincte de préemption.",
    "Incohérence préexistante conservée : le premier alinéa renvoie au troisième pour le délai de deux mois, alors que ce délai figure au quatrième ; le troisième organise la transmission préfectorale et l'amende. Aucune renumérotation silencieuse. Contrôles maintenus : sept jours ouvrés pour transmettre, sept jours pour les observations, amende de 1 000 €, délai de deux mois, minimum résiduel d'un mois après suspension et prescription de cinq ans. Tous les destinataires et les deux fonds bénéficiaires sont conservés. Note source prise en compte : selon l'article 157, VI de la loi n° 2018-1021 du 23 novembre 2018, les conventions de mise en œuvre des opérations de requalification des quartiers anciens dégradés conclues sur le fondement de l'ancien L. 304-1 du CCH demeurent en vigueur. Ces opérations peuvent être transformées en opérations de revitalisation de territoire par avenant à la convention initiale. Cette règle historique n'est pas présentée comme l'entrée en vigueur d'une réforme future.",
)

add(
    "L213-2-1",
    """
<p>Si la réalisation d'une opération d'aménagement le justifie, le titulaire du droit de préemption peut exercer ce droit pour acquérir la fraction d'une unité foncière située dans une partie de commune soumise à l'un des droits de préemption institués par le présent titre.</p>
<p>Le propriétaire peut alors exiger que le titulaire de ce droit acquière la totalité de l'unité foncière.</p>
""",
    "Réécriture à droit constant : la condition de préemption partielle et le droit du propriétaire d'imposer l'acquisition totale sont exprimés directement dans les deux alinéas existants. Aucune réforme de fond.",
    "La justification par une opération d'aménagement et la localisation de la fraction dans un secteur soumis au droit sont conservées. La faculté du propriétaire d'exiger l'acquisition de l'ensemble n'est pas limitée ; articulation maintenue avec la dépréciation de la fraction restante prévue à L. 213-4.",
)

add(
    "L213-3",
    """
<p>Le titulaire du droit de préemption peut en déléguer l'exercice à l'Etat, à une collectivité locale, à un établissement public y ayant vocation ou au concessionnaire d'une opération d'aménagement. Il peut accorder cette délégation pour une ou plusieurs parties des zones concernées ou à l'occasion de l'aliénation d'un bien. Les biens acquis dans ce cadre entrent dans le patrimoine du délégataire.</p>
<p>Pour l'application des articles L. 211-1 et suivants, L. 212-1 et suivants, L. 213-1 à L. 213-18 et L. 219-1 à L. 219-13, le délégataire désigné en application du présent article est également compris, s'il y a lieu, dans l'expression « titulaire du droit de préemption ».</p>
""",
    "Réécriture à droit constant : les bénéficiaires possibles et les portées territoriale ou ponctuelle de la délégation sont énoncés avec un sujet explicite. L'assimilation du délégataire au titulaire est clarifiée sans changer les séries d'articles concernées ni introduire de réforme de fond.",
    "Les deux alinéas sont conservés. Bénéficiaires, entrée des biens dans le patrimoine du délégataire et réserve « s'il y a lieu » maintenus. Renvois conservés exactement dans leur étendue : L. 211-1 et suivants, L. 212-1 et suivants, L. 213-1 à L. 213-18 et L. 219-1 à L. 219-13.",
)

add(
    "L213-4",
    """
<p>Si aucun accord amiable n'est trouvé, la juridiction compétente en matière d'expropriation fixe le prix d'acquisition. Ce prix n'inclut aucune indemnité accessoire, notamment aucune indemnité de réemploi.</p>
<p>Dans le cas prévu à l'article L. 213-2-1, la juridiction compétente en matière d'expropriation tient compte, pour fixer le prix d'acquisition, de la dépréciation éventuelle de la fraction restante de l'unité foncière due à la préemption partielle.</p>
<p>Les règles applicables en matière d'expropriation régissent la fixation du prix ainsi que son paiement ou, le cas échéant, sa consignation, sous les réserves suivantes :</p>
<p>a) La date de référence prévue à l'article L. 322-2 du code de l'expropriation pour cause d'utilité publique est déterminée comme suit :</p>
<p>- Pour les biens compris dans le périmètre d'une zone d'aménagement différé :</p>
<p>i) La date de publication de l'acte délimitant le périmètre provisoire de la zone, lorsque le bien se trouve dans un tel périmètre ou lorsque l'acte créant la zone est publié pendant la durée de validité d'un périmètre provisoire ;</p>
<p>ii) La date de publication de l'acte créant la zone, lorsqu'aucun périmètre provisoire n'a été délimité ;</p>
<p>iii) Dans tous les cas, la date du dernier renouvellement de l'acte créant la zone ;</p>
<p>- Pour les biens situés hors d'une telle zone, la date d'opposabilité aux tiers du plus récent des actes rendant public, approuvant, révisant ou modifiant le plan d'occupation des sols, ou approuvant, révisant ou modifiant le plan local d'urbanisme et délimitant la zone où se situe le bien ;</p>
<p>b) Les améliorations, transformations ou changements d'affectation réalisés par le propriétaire après la date mentionnée au a) ne sont pas présumés spéculatifs ;</p>
<p>c) Si les transactions amiables réalisées dans la même zone ne fournissent pas de références suffisantes pour évaluer le bien, il peut être tenu compte des mutations et accords amiables concernant des biens de même qualification situés dans des zones comparables.</p>
<p>Lorsque la juridiction compétente en matière d'expropriation fixe le prix d'un bien dont la vente est envisagée avec constitution d'une rente viagère, elle respecte les conditions de paiement proposées par le vendeur. Elle peut toutefois réviser le montant de la rente et celui du capital éventuel.</p>
""",
    "Réécriture à droit constant : les règles de fixation du prix et les dates de référence sont présentées avec des phrases plus courtes, tout en conservant les douze alinéas et les subdivisions a), b), c), i), ii), iii). La rente viagère et la préemption partielle gardent leurs règles propres ; aucune réforme de fond.",
    "L'exclusion des indemnités accessoires, la dépréciation de la fraction restante, les hypothèses de périmètre provisoire et de renouvellement, les actes relatifs aux POS et PLU et l'opposabilité aux tiers sont conservés. Le iii) demeure prioritaire « dans tous les cas » sans déplacer les dates i) et ii). L'absence de présomption spéculative ne vaut pas reconnaissance automatique d'une amélioration indemnisable. Les références à des zones comparables restent subsidiaires. Le renvoi à L. 322-2 est maintenu.",
)

add(
    "L213-4-1",
    """
<p>Lorsque la juridiction compétente en matière d'expropriation est saisie dans l'un des cas prévus aux articles L. 211-5, L. 211-6, L. 212-3 et L. 213-4, le titulaire du droit de préemption doit consigner 15 % du montant de l'évaluation établie par le directeur départemental des finances publiques.</p>
<p>Seuls l'acte de saisine de la juridiction et l'évaluation du directeur départemental des finances publiques sont nécessaires pour effectuer cette consignation.</p>
<p>Le titulaire du droit de préemption doit notifier une copie du récépissé de consignation à la juridiction et au propriétaire dans les trois mois suivant la saisine de la juridiction. S'il ne le fait pas dans ce délai, il est réputé avoir renoncé à l'acquisition ou à l'exercice du droit de préemption.</p>
""",
    "Réécriture à droit constant : le montant à consigner, les seules pièces nécessaires et l'obligation de notification sont formulés directement, en maintenant les trois alinéas. Aucun changement de taux, de délai ou de sanction n'est proposé.",
    "Consignation de 15 % de l'évaluation fiscale et notification aux deux destinataires dans les trois mois de la saisine conservées. Renvois à L. 211-5, L. 211-6, L. 212-3 et L. 213-4 maintenus. Point préexistant à vérifier : L. 211-6 est absent du corpus public urbanisme.json fourni ; cette absence ne permet pas à elle seule d'affirmer son abrogation et le renvoi n'est pas supprimé. Libération des fonds coordonnée avec L. 213-4-2.",
)

add(
    "L213-4-2",
    """
<p>Les fonds consignés sur le fondement de l'article L. 213-4-1 ne peuvent être libérés qu'après le transfert de propriété ou lorsque le titulaire du droit de préemption a renoncé à l'acquisition ou à l'exercice de ce droit.</p>
""",
    "Réécriture à droit constant : les deux événements permettant de libérer les fonds sont énoncés dans une phrase plus directe. Aucune modification de fond des conditions de restitution.",
    "Renvoi à L. 213-4-1 maintenu. La renonciation à l'acquisition ou à l'exercice du droit et le transfert de propriété demeurent les seuls événements prévus ; la fixation du prix ou la décision d'acquérir ne sont pas ajoutées comme causes de libération.",
)


def main():
    sources = json.loads(Path("source.json").read_text())
    assert len(sources) == 24
    assert set(drafts) == {source["number"] for source in sources}
    answer = []
    for source in sources:
        row = {
            key: source[key]
            for key in ("code_id", "source_id", "source_sha256", "number")
        }
        row.update(drafts[source["number"]])
        row["status"] = "rewrite_draft"
        answer.append(row)
    Path("answer.json").write_text(
        json.dumps(answer, ensure_ascii=False, indent=2) + "\n"
    )


if __name__ == "__main__":
    main()
