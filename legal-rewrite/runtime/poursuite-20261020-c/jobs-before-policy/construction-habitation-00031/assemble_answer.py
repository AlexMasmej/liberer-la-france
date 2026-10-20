import json
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
fragments = {
    'L422-2': ['L422-2_01.xml', 'L422-2_02.xml', 'L422-2_03.xml'],
    'L422-2-1': ['L422-2-1.xml'],
}
reasons = {
    'L422-2': (
        "Réécriture à droit constant de l'ensemble des compétences des sociétés anonymes d'HLM : "
        "les longues énumérations sont rendues plus lisibles par des phrases distinctes à l'intérieur "
        "des mêmes alinéas ; les bénéficiaires, autorisations, conditions territoriales et financières "
        "et exclusions sont explicités. Les règles propres aux filiales de logement intermédiaire, "
        "à leur capital, aux concours financiers et au contrôle administratif sont intégralement "
        "reprises. Les soixante-huit alinéas conservent leur ordre et les subdivisions demeurent en "
        "place. Aucune réforme de fond : les orientations de policy.json sur les autorisations "
        "d'urbanisme, l'équivalence technique et la rénovation locative ne modifient pas, par "
        "elles-mêmes, cet article relatif à l'objet et aux compétences des sociétés d'HLM."
    ),
    'L422-2-1': (
        "Réécriture intégrale à droit constant des règles d'actionnariat et de gouvernance : "
        "les conditions imposées aux associations présentant les candidats locataires, le contenu "
        "et la communication du pacte, la répartition des droits de vote et les nominations aux "
        "conseils sont exprimés dans des phrases plus directes. Les quatre parties I à IV et les "
        "dix-neuf alinéas restent à leur place. Les catégories d'actionnaires, seuils, exclusions "
        "et règles de représentation sont préservés. Aucune réforme de fond : policy.json ne "
        "prévoit pas de modifier cette gouvernance."
    ),
}
notes = {
    'L422-2': (
        "Contrôle source/proposition effectué sur les 68 alinéas, sans tableau dans la source. "
        "Sont notamment conservés : les détentions d'au moins 99 %, la vacance de plus d'un an, "
        "les seuils de plus de 50 000 et de plus de 15 000 habitants, les limites de 30 % et "
        "10 %, le minimum de 25 %, les délais de deux mois et trois mois, les deux délais "
        "d'un an, le capital d'un euro, la durée maximale de dix ans et le dépôt du permis "
        "avant le 1er mars 2014. Les accords du maire et des représentants de l'État, "
        "l'autorisation ministérielle préalable, la nullité d'ordre public des souscriptions "
        "irrégulières, l'interdiction d'être tiers-financeur, les plafonds de ressources et de "
        "prix, les conventions réglementées et les limites du service d'intérêt général demeurent. "
        "Les renvois aux trois alinéas précédents et à l'alinéa précédent conservent leurs cibles ; "
        "le renvoi aux deuxième à quatrième alinéas de L. 411-2 reste inchangé. "
        "Incohérence préexistante conservée : le 62e alinéa vise les quarante-septième à "
        "cinquantième alinéas pour définir l'objet des filiales, alors que, dans le découpage "
        "fourni, l'alinéa introductif des filiales et leurs 1° à 3° occupent les alinéas 48 à 51. "
        "Une correction de ce renvoi doit faire l'objet d'une coordination expresse. Le renvoi "
        "à L. 351-2 au 28e alinéa est conservé ; cet article n'a pas été retrouvé dans le corpus "
        "public fourni et sa portée doit être contrôlée au regard du conventionnement, également "
        "visé par le renvoi à L. 831-1 ailleurs dans cet article. La référence à l'article 232 "
        "du CGI au b est conservée, distincte de celle à l'article 1406 bis au sixième alinéa. "
        "L'expérimentation de cinq ans courant depuis la promulgation de la loi n° 2014-366 "
        "du 24 mars 2014 est reproduite sans prorogation ; ses éventuels effets sur les "
        "opérations historiques restent à examiner. Les renvois historiques à l'ordonnance "
        "n° 2004-559 du 17 juin 2004 et aux articles L. 6148-2 à L. 6148-5-3 du code de la "
        "santé publique sont maintenus et appellent un contrôle de leur portée temporelle. "
        "L'absence de tiret en tête du 28e alinéa de la source est conservée ; l'accord "
        "grammatical « elles sont membres » est rétabli au 12e alinéa. "
        "La note source prévoit, selon le A du IX de l'article 108 de la loi n° 2026-103 "
        "du 19 février 2026, l'application de la rédaction résultant du II du même article "
        "aux impositions établies au titre de 2027 et des années suivantes ; pour 2027, la "
        "durée de vacance antérieure au 1er janvier 2027 est prise en compte. La portée de "
        "cette note fiscale associée à un article de compétences, notamment pour le renvoi à "
        "1406 bis, nécessite vérification : elle ne fixe pas l'entrée en vigueur d'une réforme "
        "future ni un report global des compétences des sociétés d'HLM. "
        "Coordinations de réforme hors du présent article : le dossier coordonné et la fiche "
        "de parcelle relèvent de L. 423-1 et L. 410-1 du code de l'urbanisme selon "
        "coordination.json ; les solutions techniques équivalentes relèvent du régime de "
        "construction, notamment de L. 112-4 et suivants du CCH. La voie locative de "
        "vingt-quatre mois avec travaux contrôlés et compensation des surcoûts énergétiques "
        "appelle des dispositions dans la loi n° 89-462 du 6 juillet 1989, notamment son "
        "article 6, et une coordination de son décret de décence n° 2002-120 du 30 janvier "
        "2002. Le traitement des impayés appelle notamment l'article 24 de cette loi et les "
        "textes de procédure judiciaire et d'exécution. Ces dispositions doivent être rédigées "
        "dans leur champ propre, avec leur transition, sans créer ici de renvoi nouveau ni "
        "autoriser une location contraire aux protections contre l'habitat indigne."
    ),
    'L422-2-1': (
        "Contrôle source/proposition effectué sur les 19 alinéas ; aucun tableau ni note "
        "source. Les seuils de plus de 50 000 habitants et d'au moins une commune de plus "
        "de 15 000 habitants, le groupe de deux ou trois actionnaires, les deux minima de "
        "10 % des droits de vote, le tiers des voix plus une, le plafond global de 5 % du "
        "capital détenu par les personnes physiques et les deux représentations de trois "
        "membres sont conservés. La majorité des droits de vote de l'actionnaire de référence "
        "reste plafonnée par sa part de capital ; l'alternance des sexes sur les listes, le "
        "prix symbolique des cessions, la communication du pacte dès sa conclusion "
        "et le renouvellement de l'agrément en cas de rupture ou de modification pertinente "
        "du capital sont maintenus. Le calcul géographique propre aux départements et "
        "l'exclusion des personnes physiques et des placements collectifs salariés du rôle "
        "d'actionnaire de référence sont préservés. Les subdivisions du code monétaire et "
        "financier sont reprises sans raccourci. Les articles L. 411 et L. 441 existent sous "
        "ces numéros dans le corpus public fourni ; aucun suffixe ne leur est ajouté. "
        "Le renvoi à l'article 1134 du code civil et la dénomination « Union des entreprises "
        "et des salariés pour le logement » sont conservés tels que fournis ; leur actualité "
        "et leur portée temporelle, notamment pour les pactes anciens, nécessitent contrôle "
        "avant toute coordination. Au IV, la source vise le conseil d'administration ou le "
        "conseil de surveillance pour les nominations, mais seulement le conseil "
        "d'administration pour les trois représentants des locataires : cette différence "
        "préexistante est conservée et doit être examinée sans étendre silencieusement "
        "la seconde règle au conseil de surveillance."
    ),
}

answer = []
for source in sources:
    number = source['number']
    article = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    article.update(
        proposed_xml='\n'.join((Path('fragments') / name).read_text().strip() for name in fragments[number]),
        reason=reasons[number],
        review_notes=notes[number],
        status='rewrite_draft',
    )
    answer.append(article)

Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print('answer.json :', len(answer), 'articles')
