import json
from pathlib import Path


drafts = {}


def add(number, paragraphs, reason, review_notes):
    assert number not in drafts
    drafts[number] = {
        "proposed_xml": "\n".join(f"<p>{paragraph}</p>" for paragraph in paragraphs),
        "reason": reason,
        "review_notes": review_notes,
    }


add(
    "L151-2",
    [
        "Les règles de construction relatives à la qualité sanitaire des bâtiments, définies en application du présent titre, doivent être cohérentes avec les règles générales d'hygiène et les autres mesures de protection de la santé humaine mentionnées à l'article L. 1311-1 du code de la santé publique. Elles se substituent de plein droit aux dispositions contraires ou divergentes des règlements départementaux et communaux pris en application des articles L. 1311-2 et L. 1311-3 du même code pour assurer la protection de la santé publique."
    ],
    "Réécriture à droit constant : l'exigence de cohérence est formulée directement et la phrase relative aux règlements locaux est réordonnée. La substitution de plein droit et ses deux cas, contrariété et divergence, sont maintenus. Aucune réforme de fond n'est introduite dans cet article de coordination sanitaire.",
    "Les trois renvois au code de la santé publique sont conservés. La note de l'article 8 de l'ordonnance du 29 janvier 2020 concerne l'entrée en vigueur historique, au plus tard le 1er juillet 2021 ; elle ne fixe aucune date pour le projet de réforme. Les solutions techniques équivalentes ne peuvent écarter les objectifs sanitaires du titre V.",
)

add(
    "L152-1",
    [
        "Chaque logement doit disposer d'une alimentation en eau potable et d'une installation assurant l'évacuation continue des eaux usées domestiques."
    ],
    "Réécriture à droit constant : les deux équipements obligatoires de chaque logement sont énoncés sous la forme d'une obligation explicite. Le caractère continu de l'évacuation et la nature domestique des eaux usées sont maintenus. Aucune réforme de fond.",
    "L'obligation reste applicable à tout logement. La politique de transformation des locaux en logements n'autorise aucune dispense d'eau potable ou d'évacuation continue des eaux usées domestiques.",
)

add(
    "L152-2",
    [
        "Le réseau d'eau d'un bâtiment d'habitation doit distribuer l'eau sans en altérer la qualité."
    ],
    "Réécriture à droit constant : l'interdiction d'altérer la qualité de l'eau est exprimée comme une obligation du réseau de distribution. Le champ des bâtiments d'habitation est conservé. Aucune réforme de fond.",
    "L'article porte sur l'altération imputable au réseau du bâtiment ; il ne remplace pas les règles relatives à la qualité de l'eau fournie. Aucun seuil ni équipement supplémentaire n'est créé.",
)

add(
    "L152-3",
    [
        "Toute nouvelle construction d'un bâtiment à usage principal d'habitation doit comprendre une installation permettant de déterminer la quantité d'eau froide fournie à chaque local occupé à titre privatif ou à chaque partie privative d'un lot de copropriété ainsi que, le cas échéant, aux parties communes.",
        "Les logements-foyers sont exemptés de l'obligation prévue au précédent alinéa.",
        "Un décret précise les conditions d'application du présent article.",
    ],
    "Réécriture à droit constant : l'installation est présentée comme une obligation de la nouvelle construction et l'exemption des logements-foyers est rattachée explicitement à cette obligation. Les points de détermination des quantités d'eau froide et le renvoi au décret sont conservés. Aucune réforme de fond.",
    "Les trois alinéas restent dans le même ordre. L'usage principal d'habitation, l'alternative entre local privatif et partie privative d'un lot, les parties communes lorsqu'il y en a et l'exemption des logements-foyers sont maintenus. Aucune obligation autonome de facturation individuelle n'est ajoutée.",
)

add(
    "L153-1",
    [
        "La conception, la construction et l'entretien des bâtiments doivent préserver la qualité de l'air intérieur. Les exigences applicables à cette qualité sont spécifiques à chaque typologie de bâtiment."
    ],
    "Réécriture à droit constant : la préservation de l'air intérieur et la différenciation des exigences selon la typologie de bâtiment sont distinguées en deux phrases. Les trois étapes concernées sont maintenues. Aucune réforme de fond.",
    "Les exigences demeurent différenciées par typologie, sans création de seuil uniforme ni extension de cet article à une nouvelle catégorie de travaux.",
)

add(
    "L153-2",
    [
        "Dans des conditions normales d'occupation et d'usage et, le cas échéant, compte tenu de l'environnement des bâtiments, le renouvellement de l'air et l'évacuation des émanations doivent être assurés de manière que la pollution de l'air intérieur des locaux ne mette pas en danger la santé et la sécurité des personnes. Ils doivent aussi permettre d'éviter les condensations, sauf lorsqu'elles sont passagères."
    ],
    "Réécriture à droit constant : les conditions d'appréciation sont placées en tête et les deux résultats attendus sont séparés en deux phrases dans le même alinéa. La protection de la santé et de la sécurité et l'exception des condensations passagères sont conservées. Aucune réforme de fond.",
    "Le renouvellement de l'air et l'évacuation des émanations restent tous deux requis. L'exception ne concerne que les condensations passagères, jamais la mise en danger des personnes par la pollution intérieure.",
)

add(
    "L153-3",
    [
        "Les travaux portant sur les parois opaques ou vitrées donnant sur l'extérieur des bâtiments, ainsi que ceux portant sur les installations de ventilation et de chauffage, doivent être complétés, si nécessaire, par des travaux garantissant un renouvellement de l'air suffisant et maîtrisé."
    ],
    "Réécriture à droit constant : la nécessité des travaux complémentaires est exprimée directement, tout en conservant les parois et installations visées. Le renouvellement de l'air doit rester à la fois suffisant et maîtrisé. Aucune réforme de fond.",
    "La condition « si nécessaire » est conservée ; elle ne devient pas une obligation systématique de travaux complémentaires. Les parois opaques et vitrées ainsi que la ventilation et le chauffage restent expressément visés.",
)

add(
    "L153-4",
    [
        "La conception, la construction, la rénovation et l'équipement des bâtiments doivent prévenir les intoxications par le monoxyde de carbone."
    ],
    "Réécriture à droit constant : les quatre opérations concernées deviennent les sujets explicites de l'obligation de prévention. Le risque visé reste l'intoxication par le monoxyde de carbone. Aucune réforme de fond.",
    "Les quatre opérations de la source sont maintenues. Aucun remplacement de cette obligation par une simple obligation d'information ou de détection n'est introduit.",
)

add(
    "L153-5",
    [
        "Un décret en Conseil d'Etat fixe les modalités d'application du présent chapitre, notamment les résultats minimaux à atteindre et les catégories de bâtiments qui y sont soumis. Ce décret entre en vigueur au plus tard le 1er janvier 2025."
    ],
    "Réécriture à droit constant : le contenu du décret et sa date limite d'entrée en vigueur sont séparés en deux phrases. La liste indicative des matières réglementaires reste ouverte. Aucune réforme de fond et aucun nouveau calendrier ne sont créés.",
    "La date du 1er janvier 2025 est conservée comme échéance déjà inscrite dans la source. Elle est passée à la date du travail et ne constitue ni une date de promulgation ni une échéance nouvelle. Le présent lot ne permet pas de vérifier l'exécution de cette prescription réglementaire.",
)

add(
    "L154-1",
    [
        "La conception, la construction, la rénovation et l'équipement des bâtiments doivent limiter les niveaux de bruit à l'intérieur des locaux et leur assurer une qualité acoustique adaptée à leur usage. Ces exigences s'apprécient dans des conditions normales d'utilisation des bâtiments et des locaux, compte tenu des nuisances sonores habituelles provenant des lieux avoisinants."
    ],
    "Réécriture à droit constant : les résultats acoustiques et leurs conditions d'appréciation sont répartis en deux phrases. Les quatre opérations, l'usage des locaux et les nuisances habituelles du voisinage sont conservés. Aucune réforme de fond.",
    "L'appréciation reste liée à l'utilisation normale des bâtiments et locaux et aux nuisances habituelles des lieux avoisinants. Aucun seuil acoustique chiffré n'est inventé.",
)

add(
    "L154-2",
    [
        "Dans les bâtiments existants situés dans une zone de bruit routier ou ferroviaire important ou dans une zone de bruit d'un plan de gêne sonore, et faisant l'objet des travaux de rénovation énergétique ou d'isolation thermique mentionnés aux articles L. 171-1 et L. 173-1, les nouveaux équipements, ouvrages ou installations mis en place doivent atteindre des résultats minimaux en matière d'acoustique."
    ],
    "Réécriture à droit constant : les conditions tenant à la localisation et aux travaux sur le bâtiment sont placées avant l'obligation des nouveaux équipements, ouvrages ou installations. Le cumul de ces conditions et les renvois énergétiques sont conservés. Aucune réforme de fond.",
    "Les articles L. 171-1 et L. 173-1 ont été consultés dans le corpus public. La nouvelle rédaction rattache explicitement aux bâtiments existants les conditions de localisation et de travaux exprimées par les relatives de la source. Elle n'étend pas l'obligation acoustique à tous les bâtiments existants ni à tous leurs équipements.",
)

add(
    "L154-3",
    [
        "Des prescriptions relatives aux caractéristiques acoustiques peuvent être imposées aux travaux exécutés dans des ouvrages ou locaux existants qui ne sont pas à usage d'habitation, lorsque ces travaux sont soumis à autorisation ou à déclaration préalable ou qu'ils sont réalisés avec l'aide de l'Etat, d'une collectivité publique ou d'un organisme assurant une mission de service public."
    ],
    "Réécriture à droit constant : le champ des ouvrages et locaux est indiqué avant les conditions alternatives d'assujettissement des travaux. Le caractère facultatif des prescriptions et les trois catégories d'aide sont préservés. Aucune réforme de fond.",
    "L'autorisation, la déclaration préalable et l'aide publique ou d'un organisme assurant une mission de service public demeurent des voies alternatives. Les ouvrages ou locaux d'habitation restent hors du champ de cet article.",
)

add(
    "L154-4",
    [
        "Les modalités d'application du présent chapitre sont fixées par décret en Conseil d'Etat. Ce décret détermine notamment les résultats minimaux à atteindre ainsi que les catégories de bâtiments et de locaux qui y sont soumis."
    ],
    "Réécriture à droit constant : l'habilitation réglementaire générale et ses objets expressément mentionnés sont séparés en deux phrases. Les catégories de bâtiments comme celles de locaux restent visées. Aucune réforme de fond.",
    "Le décret en Conseil d'Etat et le caractère non exhaustif de la liste introduite par « notamment » sont maintenus. Aucun résultat minimal n'est fixé directement par la réécriture.",
)

add(
    "L155-1",
    [
        "La conception et la construction des bâtiments d'habitation doivent permettre aux occupants de bénéficier, dans les pièces principales des logements, d'un apport de lumière naturelle, d'une vue sur l'extérieur, d'un contact avec l'extérieur et d'un renouvellement ponctuel de l'air. Ce renouvellement doit permettre de traiter les pollutions occasionnelles de l'air intérieur et contribuer au traitement de l'inconfort thermique ponctuel.",
        "Le présent article s'applique aux constructions et aux extensions de bâtiments à usage d'habitation mentionnées à l'article L. 111-1.",
    ],
    "Réécriture à droit constant : les quatre fonctions des pièces principales sont énumérées dans une première phrase, puis les finalités du renouvellement ponctuel de l'air sont précisées. Le champ du second alinéa est maintenu. Aucune réforme de fond.",
    "Les deux alinéas restent à leur place. La définition de la construction et de l'extension à l'article L. 111-1 a été consultée. Vue et contact avec l'extérieur demeurent deux exigences distinctes ; la contribution au confort thermique ne devient pas une garantie générale de température. Le champ n'est pas étendu silencieusement à tout changement de destination.",
)

add(
    "L155-2",
    [
        "La conception et la disposition des bâtiments à usage professionnel doivent permettre d'utiliser la lumière naturelle pour éclairer les locaux destinés au travail, sauf lorsque la nature technique des activités y fait obstacle."
    ],
    "Réécriture à droit constant : l'obligation de permettre l'utilisation de la lumière naturelle est énoncée directement. Les locaux destinés au travail et l'exception fondée sur la nature technique des activités sont conservés. Aucune réforme de fond.",
    "L'exception reste liée à la nature technique des activités ; aucun motif économique ou de convenance n'est ajouté. Cet article conserve son champ professionnel propre.",
)

add(
    "L156-1",
    [
        "La construction des logements doit respecter des dimensions minimales de hauteur sous plafond, de surface habitable et de volume habitable."
    ],
    "Réécriture à droit constant : le respect des dimensions minimales est formulé comme une obligation de construction. Les trois dimensions sont reprises sans modification. Aucune réforme de fond.",
    "La source ne chiffre pas ces minima : aucun chiffre n'est ajouté. Le respect de la surface habitable ne remplace ni celui du volume habitable ni celui de la hauteur sous plafond.",
)

add(
    "L157-1",
    [
        "Lors de leur construction, les bâtiments d'habitation doivent être dotés d'installations permettant de stocker les déchets ménagers avant leur évacuation. Ces installations doivent garantir l'hygiène et la salubrité des bâtiments."
    ],
    "Réécriture à droit constant : l'obligation d'installation et l'exigence d'hygiène et de salubrité sont séparées en deux phrases. Le stockage reste limité à la période précédant l'évacuation des déchets ménagers. Aucune réforme de fond.",
    "Les bâtiments d'habitation et les déchets ménagers demeurent le champ de l'article. La réécriture ne crée ni mode de collecte particulier ni obligation de traitement des déchets sur place.",
)

add(
    "L157-2",
    [
        "En fonction de leur type ou de leur catégorie, les établissements recevant du public doivent disposer d'un défibrillateur automatisé externe visible et facile d'accès. Un même défibrillateur peut être commun à plusieurs établissements recevant du public accueillis sur un même site. Les propriétaires des établissements veillent à ce que la maintenance du défibrillateur et de ses accessoires soit assurée dans les conditions prévues à l'article L. 5212-1 du code de la santé publique."
    ],
    "Réécriture à droit constant : l'équipement obligatoire, sa mutualisation possible et la responsabilité de sa maintenance sont distingués en trois phrases au sein du même alinéa. La visibilité, l'accès et les accessoires sont expressément conservés. Aucune réforme de fond.",
    "L'assujettissement reste fonction du type ou de la catégorie d'établissement. La mutualisation reste limitée aux établissements accueillis sur un même site. Le renvoi à l'article L. 5212-1 du code de la santé publique est repris à l'identique ; son contenu n'a pas été vérifié, ce code ne figurant pas dans le corpus fourni.",
)

add(
    "L161-1",
    [
        "Les dispositions architecturales ainsi que les aménagements et équipements intérieurs et extérieurs doivent assurer l'accessibilité à tous, au sens de l'article L. 111-1, des locaux à usage d'habitation, des établissements recevant du public, des installations ouvertes au public et des bâtiments à usage professionnel, dans les cas et selon les conditions prévus aux articles L. 162-1 à L. 164-3.",
        "Ces obligations ne s'imposent pas aux propriétaires qui construisent ou améliorent un logement pour leur propre usage.",
    ],
    "Réécriture à droit constant : le lien entre les choix architecturaux, les aménagements, les équipements et l'accessibilité est explicité. Les quatre catégories de biens, les renvois et l'exception d'usage propre sont maintenus. Aucune réforme de fond.",
    "Les deux alinéas et leur ordre sont conservés. La définition de l'accessibilité de l'article L. 111-1 et les limites de la plage L. 162-1 à L. 164-3 ont été consultées. L'exception ne vise que le propriétaire construisant ou améliorant un logement pour son propre usage.",
)

add(
    "L161-2",
    [
        "Pour les bâtiments relevant de son autorité, le ministre de la défense désigne l'autorité administrative compétente pour prendre les décisions relatives à l'accessibilité."
    ],
    "Réécriture à droit constant : le champ de compétence est placé en tête, avant le pouvoir de désignation du ministre. La compétence porte toujours sur les décisions relatives à l'accessibilité. Aucune réforme de fond.",
    "La compétence de désignation reste réservée au ministre de la défense pour les bâtiments relevant de son autorité. Aucune autorité nouvelle n'est désignée par la réécriture.",
)

add(
    "L161-3",
    [
        "Les modalités d'application du présent titre sont fixées par décret en Conseil d'Etat, pris après avis du conseil mentionné à l'article L. 146-1 du code de l'action sociale et des familles."
    ],
    "Réécriture à droit constant : la portée du décret est présentée avant ses conditions d'adoption. L'avis préalable du conseil et le renvoi qui l'identifie sont maintenus. Aucune réforme de fond.",
    "La consultation demeure préalable au décret en Conseil d'Etat. Le renvoi à l'article L. 146-1 du code de l'action sociale et des familles est conservé, sans le remplacer par une dénomination d'organisme non vérifiée dans le corpus.",
)

add(
    "L162-1",
    [
        "Lors de leur construction, les bâtiments nouveaux et les parties nouvelles de bâtiments doivent respecter des dispositions d'accessibilité propres à chacun des types de bâtiments relevant de l'article L. 161-1.",
        "Ces dispositions précisent notamment :",
        "1° Les conditions dans lesquelles, lors de la construction de bâtiments d'habitation collectifs et en fonction de leurs caractéristiques, 20 % de leurs logements, avec un minimum d'un logement, doivent être accessibles, les autres logements devant être évolutifs ;",
        "2° Les conditions dans lesquelles des travaux modificatifs de l'acquéreur peuvent être réalisés lors de la construction de logements vendus en l'état futur d'achèvement ;",
        "3° Les conditions dans lesquelles, lors de la construction de logements locatifs sociaux édifiés et gérés par les organismes et sociétés mentionnés aux articles L. 365-2, L. 411-2 et L. 481-1, ces organismes et sociétés garantissent la mise en accessibilité des logements évolutifs et imposent la réalisation de ces travaux dans un délai raisonnable. Le coût des travaux incombe aux bailleurs, sans préjudice des aides qu'ils peuvent recevoir à ce titre ;",
        "4° Les prestations d'accessibilité que doivent fournir les logements destinés à une occupation temporaire ou saisonnière dont la gestion et l'entretien sont organisés et assurés de façon permanente. Cette qualification nécessite l'accord de l'autorité administrative, après avis de la commission compétente en matière d'accessibilité.",
    ],
    "Réécriture à droit constant : l'obligation applicable aux constructions est énoncée directement et chaque élément de la liste est allégé. Le 3° distingue l'exécution des travaux et leur financement, sans changer les organismes responsables, les bailleurs débiteurs ni la possibilité d'aides. Aucune réforme de fond.",
    "Les six alinéas, dont les 1° à 4°, restent dans leur ordre. Le taux de 20 %, le minimum d'un logement, le caractère évolutif des autres logements et les trois renvois du 3° sont conservés. Aucun délai chiffré ne remplace le délai raisonnable. Au 4°, l'occupation temporaire ou saisonnière, la permanence de la gestion et de l'entretien, l'accord administratif et l'avis préalable restent requis. Le mécanisme d'accessibilité du bâti neuf n'est pas appliqué indistinctement aux transformations de bâtiments existants.",
)

add(
    "L163-1",
    [
        "Les bâtiments à usage d'habitation et les bâtiments à usage professionnel situés dans un cadre bâti existant doivent être rendus accessibles lorsqu'ils font l'objet de travaux. Les modalités de cette mise en accessibilité tiennent notamment compte de la nature des bâtiments et parties de bâtiments concernés, du type de travaux entrepris et du rapport entre le coût de ces travaux et la valeur des bâtiments au-delà duquel ces modalités s'appliquent.",
        "Pour les travaux de transformation de bureaux ou de locaux vacants en logements, le maître d'ouvrage peut satisfaire aux exigences d'accessibilité applicables au moyen des solutions techniques admises dans les conditions prévues à l'article L. 112-4. Lorsqu'il recourt à une solution d'effet équivalent au sens de l'article L. 112-6, il justifie du respect des objectifs généraux et de résultats au moins équivalents à ceux de la solution de référence, selon les procédures d'attestation et de contrôle prévues aux articles L. 112-9 et L. 112-10. Pour ces travaux, il justifie également du respect des exigences de sécurité et de qualité sanitaire applicables aux logements dans les conditions prévues à l'article L. 112-4.",
    ],
    "Le premier alinéa est réécrit à droit constant en séparant l'obligation de mise en accessibilité des critères de ses modalités. Un second alinéa coordonne l'article avec l'orientation de transformation des bureaux et locaux vacants en logements : il explicite le recours aux solutions techniques, y compris d'effet équivalent, dans le cadre existant des articles L. 112-4, L. 112-6, L. 112-9 et L. 112-10. Cet ajout ne crée pas de nouvelle dérogation de fond et ne réduit pas les garanties d'accessibilité, de sécurité ou de salubrité.",
    "L'alinéa source reste le premier ; l'ajout ne déplace aucune cible existante. Les articles L. 112-4 à L. 112-12 ont été consultés : les résultats minimaux restent exigibles lorsqu'ils sont fixés ; une solution d'effet équivalent conserve l'attestation préalable d'un tiers compétent, indépendant et assuré ainsi que le contrôle distinct de sa mise en œuvre. Le premier alinéa de L. 163-2 est coordonné pour limiter ses dérogations aux obligations d'accessibilité du premier alinéa du présent article. Les renvois de L. 122-10, L. 181-11 et L. 183-4 ont été consultés : l'ajout rappelle le régime existant, sans définir une nouvelle infraction ni supprimer l'attestation d'accessibilité de fin de travaux applicable. Coordination à vérifier avec R. 163-1 et R. 163-2 et leurs arrêtés ; le dispositif ne soumet pas rétroactivement des travaux achevés à une nouvelle attestation. Ecart préexistant conservé et signalé : L. 163-1 emploie « au-delà » pour le rapport coût/valeur, tandis que R. 163-2 prévoit « supérieur ou égal à 80 % ». Le dossier coordonné relève de l'article L. 423-1 du code de l'urbanisme ; le nouvel alinéa ne modifie pas à lui seul les procédures d'autorisation. La voie locative de rénovation limitée à vingt-quatre mois nécessite des dispositions hors lot, notamment à l'article 6 de la loi n° 89-462 du 6 juillet 1989 et dans ses textes d'application, définissant les biens éligibles, les travaux contrôlés et la compensation des surcoûts énergétiques. Elle ne peut neutraliser les garanties sanitaires ou être réputée créée ici. Le traitement judiciaire des impayés appelle notamment une coordination de l'article 24 de cette loi et des textes procéduraux applicables, sans autoriser d'expulsion privée.",
)

add(
    "L163-2",
    [
        "Des dérogations aux obligations d'accessibilité prévues au premier alinéa de l'article L. 163-1 peuvent être autorisées par une décision motivée dans les cas suivants :",
        "1° En cas d'impossibilité technique ;",
        "2° En cas de disproportion manifeste entre, d'une part, les améliorations apportées par l'application des prescriptions techniques d'accessibilité et, d'autre part, leurs coûts ainsi que leurs effets sur l'usage du bâtiment et de ses abords ;",
        "3° En cas de contraintes liées à la préservation du patrimoine architectural.",
        "Les personnes handicapées affectées par l'une de ces dérogations ont droit à être relogées dans un bâtiment accessible à tous au sens de l'article L. 111-1, lorsque le propriétaire du bâtiment possède un parc de logements dont le nombre est supérieur à un seuil fixé par décret en Conseil d'Etat.",
    ],
    "Réécriture à droit constant : l'exigence de motivation est rattachée à la décision autorisant la dérogation et les deux termes de la comparaison du 2° sont rendus plus lisibles. Une coordination du renvoi à L. 163-1 limite expressément les dérogations à ses obligations d'accessibilité initiales, désormais situées dans son premier alinéa. Les trois motifs et le droit conditionnel au relogement sont conservés. Aucune nouvelle dérogation de fond n'est créée par la réforme du logement.",
    "Les cinq alinéas et les 1° à 3° restent en place ; les renvois L. 163-1 et L. 111-1 sont maintenus. La précision du premier alinéa de L. 163-1 évite d'étendre les dérogations à son nouvel alinéa relatif aux solutions équivalentes et au maintien des garanties sanitaires et de sécurité. Le seuil du parc de logements reste strictement dépassé, sans inscrire un chiffre réglementaire dans la loi. La faculté de solution d'effet équivalent explicitée à L. 163-1 ne supprime ni ces dérogations ni le droit au relogement lorsqu'elles sont accordées. Ecart préexistant relevé dans le corpus : R. 163-4 prévoit, à défaut d'une offre respectant les articles R. 162-1 à R. 162-4, une offre améliorant significativement l'accessibilité, alors que le présent article énonce un droit au relogement dans un bâtiment accessible à tous. Cette articulation nécessite contrôle ; elle n'est pas corrigée silencieusement par la réécriture.",
)


sources = json.loads(Path("source.json").read_text())
assert len(sources) == 24
assert set(drafts) == {source["number"] for source in sources}
answer = []
for source in sources:
    item = {key: source[key] for key in ("code_id", "source_id", "source_sha256", "number")}
    item.update(drafts[source["number"]])
    item["status"] = "rewrite_draft"
    answer.append(item)
Path("answer.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")
print(f"answer.json : {len(answer)} articles")
