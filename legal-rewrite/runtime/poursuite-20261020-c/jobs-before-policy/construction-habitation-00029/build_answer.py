import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sources = json.loads((ROOT / "source.json").read_text())

editorial = {
    "L411-9": (
        "Réécriture à droit constant du plan stratégique de patrimoine : une phrase distincte précise sa fonction, puis l'analyse du parc, son évolution, les choix d'investissement et de gestion et les perspectives de développement. Le lien avec la demande locale et les programmes locaux de l'habitat est conservé. Aucune réforme de fond n'est introduite dans cet article de programmation patrimoniale.",
        "L'alinéa unique est conservé. Le plan continue de tenir compte des orientations des programmes locaux de l'habitat ; il ne se substitue ni aux autorisations d'urbanisme ni aux obligations de logement social. Les coordinations d'urbanisme déjà retenues pour les articles L151-4, L151-26, L410-1 et L423-1 n'appellent ici aucune extension des compétences des organismes."
    ),
    "L411-10": (
        "Réécriture à droit constant : les responsabilités du ministère, des bailleurs, des gestionnaires et du groupement d'intérêt public sont explicitées. Les phrases distinguent les transmissions annuelles, les communications sur demande, les données publiables et les résultats ne permettant pas l'identification des personnes. Les cinq catégories de bailleurs, les deux équivalences d'inventaire et la sanction restent intégrales. Aucune réforme de fond du répertoire n'est prévue par policy.json.",
        "Les treize alinéas utiles et les subdivisions 1° à 5° sont conservés. Contrôle effectué sur le seuil de 99 %, l'amende de 1 000 € par logement après mise en demeure infructueuse, son bénéficiaire et les restrictions concernant le numéro d'immatriculation des occupants majeurs. Le renvoi au vingt-troisième alinéa de L. 441-1 correspond, dans le corpus fourni, à l'alinéa désignant notamment les EPCI concernés. La portée du membre « ayant conclu la convention » dans la liste des destinataires du huitième alinéa reste à contrôler : la construction de la source ne permet pas de lever sans interprétation son rattachement aux différentes catégories qui le précèdent. Les notes historiques sont conservées comme contexte d'application : article 26 II de la loi n° 2015-925 du 29 juillet 2015, entrée en vigueur le 1er janvier 2018 pour les bailleurs propriétaires de plus de 10 000 logements-foyers ou logements de centres concernés au 1er janvier 2017, et le 1er janvier 2019 pour les autres ; article 90 de la loi n° 2015-1776 du 28 décembre 2015 pour le 2° de l'article 13 de cette même loi selon les mêmes termes. Ces dates ne constituent pas une transition de réforme nouvelle."
    ),
    "L421-1": (
        "Réécriture à droit constant de l'ensemble des missions et du régime des filiales : les phrases séparent les activités autorisées, leurs bénéficiaires et leurs conditions, puis les plafonds, les modalités des apports, les contrôles de l'Etat et les concours financiers. Toutes les subdivisions, les interventions subsidiaires, les exclusions et les règles relatives aux logements intermédiaires sont reprises. Aucune réforme de fond des missions des offices ou de leur financement n'est ajoutée ; les possibilités de transformation de locaux déjà prévues restent soumises aux conditions de la source.",
        "Les 41 alinéas sont conservés dans le même ordre, notamment les a et b du 12° et ceux relatifs au capital. Contrôle des seuils de 99 %, 50 000 et 15 000 habitants, 25 %, dix ans, 30 %, 10 %, des délais de trois mois, du capital d'un euro et du permis demandé avant le 1er mars 2014. Incohérence préexistante maintenue et signalée : le renvoi de l'avant-dernier alinéa aux vingt-cinquième à vingt-septième alinéas ne couvre pas les trois conditions des logements intermédiaires, qui figurent aux vingt-septième à vingt-neuvième alinéas du source_xml ; une correction expresse et le contrôle des autres renvois seraient nécessaires. L'accord pronominal au 17° est harmonisé avec le sujet « offices », sans modifier ses compétences ni la limite de 30 %. La note de source relative au A du IX de l'article 108 de la loi n° 2026-103 du 19 février 2026 indique une application de la rédaction résultant du II aux impositions établies à compter de 2027, avec prise en compte, pour 2027, de la vacance antérieure au 1er janvier 2027. Le renvoi au 1° du B du I de l'article 1406 bis du CGI existe dans le corpus ; l'articulation temporelle de cette coordination fiscale avec l'article du CCH doit être contrôlée sans transformer cette note fiscale en nouvelle date de compétence des offices. Les obligations de logement social et les règles du service d'intérêt général sont maintenues."
    ),
    "L421-2": (
        "Réécriture à droit constant des participations autorisées : la liste est maintenue et le 8° distingue plus clairement l'autorisation préalable, la date unique d'acquisition, la dissolution, les limites de compétence, le conventionnement des logements et la nullité. L'accord des autorités au 4° et le délai d'avis tacite ne sont pas modifiés. Aucune réforme de fond des participations des offices n'est introduite.",
        "Les neuf alinéas et les 1° à 8° sont conservés. Délais inchangés : deux mois au 4°, un an pour la dissolution et un an à compter de la transmission effective du patrimoine pour les conventions au 8°. Renvoi ancien maintenu et signalé : le 8° vise L. 351-2, absent du corpus courant fourni. La note de source indique que l'article 2 de l'ordonnance n° 2019-770 du 17 juillet 2019 remplace cette référence par L. 353-1, L. 821-2, L. 831-1 et L. 831-2 ; ces quatre articles figurent dans le corpus. Une coordination expresse de ce renvoi reste à effectuer, sans substitution silencieuse dans le présent lot. La nullité d'ordre public conserve le champ littéral de la source, qui vise la souscription. La seconde note, simple invitation à consulter des tables de concordance du code général de la fonction publique sans contenu normatif précis, n'est pas intégrée au dispositif."
    ),
    "L421-3": (
        "Réécriture à droit constant des prestations subsidiaires : l'objet de chaque prestation, son donneur d'ordre et les conditions d'intervention sont rendus plus explicites. Le 5° sépare les accords préalables, l'avis tacite et les opérations sur les lots des copropriétés en difficulté. La qualité de prestataire de services, le caractère subsidiaire et toutes les catégories de bénéficiaires sont conservés. Aucune réforme de fond n'étend ces habilitations.",
        "Numérotation et alinéas conservés, y compris le 2° ter après les sauts de ligne au sein du paragraphe du 2° bis. Maintien du seuil de 99 %, du délai de deux mois et des modalités réglementaires pouvant déroger aux règles HLM au 5°. La rénovation énergétique du 4° bis reste réservée au syndicat des copropriétaires dont l'office est membre et soumise au dernier alinéa de L. 411-2. Pour la voie locative de rénovation de vingt-quatre mois prévue par policy.json, une disposition législative distincte doit être articulée avec les articles 6 et 20-1 de la loi n° 89-462 du 6 juillet 1989, notamment pour les conditions d'accès, le contrôle des travaux et la compensation des surcoûts énergétiques ; les prescriptions réglementaires de décence du décret n° 2002-120 du 30 janvier 2002 doivent aussi être coordonnées. Pour le traitement des impayés, la coordination porte notamment sur l'article 24 de cette loi et les règles procédurales applicables ; le présent article ne les modifie pas. Aucun numéro de disposition nouvelle n'est créé."
    ),
    "L421-4": (
        "Réécriture à droit constant des facultés complémentaires des offices : les opérations, bénéficiaires, agréments et conditions sont présentés plus directement, sans supprimer de catégorie ni de réserve. L'usufruit temporaire, la sous-location, les services sociaux et les baux réels solidaires d'activité restent distincts. Le caractère historique de l'expérimentation du 3° b est préservé. Aucune réforme de fond n'est introduite.",
        "Alinéas et subdivisions conservés, notamment l'alinéa d'exclusion qui suit le 3° b et le paragraphe regroupant les 9°, 10° et 11°. Contrôle des deux seuils de détention de 99 %, des 50 000 et 15 000 habitants et de l'expérimentation de cinq ans à compter de la promulgation de la loi n° 2014-366 du 24 mars 2014 : cette durée historique n'est ni relancée ni prolongée ; les effets d'opérations anciennes restent à apprécier selon leurs textes applicables. La source rattache cette expérimentation ancienne à la nouvelle référence au 1° du B du I de l'article 1406 bis du CGI ; ce renvoi est maintenu, sans résoudre silencieusement son articulation temporelle. La note relative au A du IX de l'article 108 de la loi n° 2026-103 du 19 février 2026 vise la rédaction issue du II applicable aux impositions établies à compter de 2027 et la vacance antérieure au 1er janvier 2027 pour les impositions de 2027 ; cette note fiscale n'est pas utilisée comme date de réouverture de l'expérimentation ou d'une réforme future. Les limitations du service d'intérêt général et les conditions normales du marché au 11° sont conservées."
    ),
    "L421-4-1": (
        "Réécriture à droit constant : la faculté de constituer une sûreté, les conditions de saisie des biens grevés et l'interdiction des sûretés générales sont énoncées séparément et avec un sujet explicite. Les sûretés demeurent exclusivement réelles mobilières et liées à l'action des offices dans le cadre de la réglementation HLM. Aucune réforme de fond des garanties n'est ajoutée.",
        "Les trois énoncés restent dans leur ordre initial, séparés par des sauts de ligne comme dans la source. Les références aux articles L. 211-1 à L. 211-5 et L. 511-1 à L. 512-2 du code des procédures civiles d'exécution ainsi que l'interdiction des sûretés réelles mobilières générales sont intégralement conservées. Les orientations de logement de policy.json ne prévoient pas d'assouplissement de ces garanties."
    ),
    "L421-5": (
        "Réécriture à droit constant des deux règles territoriales : la région de rattachement est le champ ordinaire d'activité ; l'intervention dans les départements limitrophes de cette région exige l'accord préalable de la commune d'implantation. Les deux alinéas sont rendus plus directs. Aucune réforme de fond de la compétence géographique n'est introduite.",
        "Les deux alinéas sont conservés. Le territoire limitrophe reste celui des départements bordant la région, et non celui des seuls départements bordant la collectivité de rattachement. L'accord communal reste préalable à l'intervention, sans ajout de délai ni d'accord tacite."
    ),
    "L421-6": (
        "Réécriture à droit constant du rattachement des offices : les catégories d'organismes de rattachement, les interdictions, le changement obligatoire de rattachement et la fusion sont énoncés plus directement. Les exceptions concernant Paris et la métropole du Grand Paris, les mises en demeure, le délai et les seuils sont maintenus. Aucune réforme de fond de l'organisation territoriale des offices n'est ajoutée.",
        "Les quinze alinéas et toutes les subdivisions, y compris le 2° bis abrogé, sont conservés. Contrôle du délai de quatre ans et de ses deux points de départ, de l'arrêté de fusion après mise en demeure et du seuil strictement inférieur à 12 000 logements sociaux pour chacun des organismes concernés. Le 1° quater autorise le rattachement à un syndicat mixte constitué par plusieurs départements, tandis que l'avant-dernier alinéa interdit le rattachement direct à plusieurs départements : ces deux règles distinctes sont conservées. L'exception de la commune de Paris dans l'interdiction de rattachement communal n'est pas étendue au-delà de son alinéa ; l'articulation de cette exception avec l'alinéa suivant sur l'adhésion à un EPCI reste celle de la source."
    ),
}

answers = []
for source in sources:
    number = source["number"]
    fragment_names = (
        ["L421-1.1.xml", "L421-1.2.xml", "L421-1.3.xml"]
        if number == "L421-1"
        else [number + ".xml"]
    )
    proposed = "\n".join(
        (ROOT / "fragments" / name).read_text().strip()
        for name in fragment_names
    )
    reason, review_notes = editorial[number]
    answers.append({
        **{key: source[key] for key in ("code_id", "source_id", "source_sha256", "number")},
        "proposed_xml": proposed,
        "reason": reason,
        "review_notes": review_notes,
        "status": "rewrite_draft",
    })

(ROOT / "answer.json").write_text(json.dumps(answers, ensure_ascii=False, indent=2) + "\n")
print(f"answer.json : {len(answers)} articles")
