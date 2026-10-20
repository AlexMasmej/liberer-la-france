import json
from pathlib import Path


METADATA = {
    '158': (
        ['158_1.xml', '158_2.xml', '158_3.xml'],
        "Réécriture à droit constant des règles de composition du revenu global : phrases scindées dans leurs alinéas, conditions de l'abattement sur distributions explicitées, calculs et traitements des pensions, capitaux et rentes clarifiés. Toutes les subdivisions, exclusions, dispositions historiques, valeurs et références sont conservées. Aucune réforme de fond : la baisse de CSG salariale relève de l'article 154 quinquies et ne modifie pas ces règles ; le gel partiel de revalorisation des pensions ne modifie ni leur abattement fiscal ni son indexation.",
        "Renvoi préexistant ambigu au 3, 3°, a : « 3° septies du même article » n'a pas d'antécédent clair ; conservé. L'article 208 du corpus contient bien un 3° septies relatif aux sociétés de capital-risque, mais la correction expresse du renvoi reste à coordonner. Au 6, le renvoi au dernier alinéa de l'article 163 quinvicies est conservé : dans le corpus, cet alinéa exclut certains avantages fiscaux pour les versements à compter du soixante-dixième anniversaire ; contrôler l'articulation de ce renvoi avec la qualification des versements et des rentes. Contrôler les montants annuellement révisables de 4 439 € et 454 € pour l'année d'imposition visée ; les valeurs de la source sont maintenues, sans actualisation inventée. La note source rattache la modification à l'article 4-I B 1° a de la loi n° 2026-103 du 19 février 2026 ; ce n'est pas la date de la réforme projetée. Le nouveau compte de capitalisation collective visé au L. 241-3 proposé du CSS nécessite une disposition fiscale nouvelle au CGI définissant séparément le traitement des cotisations transférées, abondements, produits et prestations ; coordonner ensuite, selon les choix législatifs, les articles 83, 154 bis, 158 et 163 quatervicies. La définition et le régime du véhicule nécessitent également des dispositions du code monétaire et financier, hors des cinq codes du périmètre. Aucun numéro nouveau ni régime d'exonération n'est présumé acquis."
    ),
    '159 quinquies': (
        ['159_quinquies.xml'],
        "Réécriture à droit constant : les deux catégories de sociétés, leurs bénéficiaires et les conditions de distribution sont exposés dans des phrases distinctes au sein du I. L'exonération reste limitée aux primes à la construction encaissées par ces sociétés. Le II périmé et le renvoi réglementaire sont maintenus. Aucune réforme de fond de ce régime n'est définie par policy.json.",
        "Conserver le champ propre aux sociétés immobilières d'investissement et de gestion, le renvoi à l'article R. 311-1 du CCH et aux articles 83 et 84 de l'annexe II. La note source indique une modification de conséquence de l'article 4-IV-3° du décret n° 2019-873 du 21 août 2019 ; elle ne fixe aucune entrée en vigueur du projet. Le II demeure indiqué comme périmé, sans suppression ni renumérotation."
    ),
    '160 bis': (
        ['160_bis.xml'],
        "Réécriture à droit constant : la règle de non-qualification en revenus distribués est présentée avec son fait générateur, le rachat des actions, et ses deux catégories de sociétés. L'habillage en sauts de ligne est remplacé par un paragraphe. Aucune réforme de fond.",
        "La règle concerne uniquement la qualification des sommes pour l'impôt sur le revenu ; elle ne crée pas une exonération de plus-value. Maintien du renvoi au 3° nonies de l'article 208 pour les sociétés de placement à prépondérance immobilière à capital variable."
    ),
    '160 quater': (
        ['160_quater.xml'],
        "Réécriture à droit constant : le fait générateur, l'annulation des titres lors des opérations visées, et la condition de détention sont reliés explicitement à la qualification de cession taxable. Les renvois et le champ sont conservés. Aucune réforme de fond.",
        "La note source réserve l'application aux rachats effectués à compter du 1er janvier 2015, conformément à l'article 88 II de la loi n° 2014-1655 du 29 décembre 2014 ; conserver cette transition dans les textes d'application. L'autre note vise les modifications de conséquence de l'article 30-I de la loi n° 2014-856 du 31 juillet 2014. Maintenir les articles 48 et 49 de la loi de 1978 et le f du I de l'article 164 B, sans extension aux autres détentions."
    ),
    '161': (
        ['161.xml'],
        "Réécriture à droit constant : la limitation du boni imposable lorsque le prix d'acquisition dépasse l'apport est isolée, puis les modalités de calcul après échange sont décrites en phrases plus courtes. Les trois régimes d'échange et le traitement distinct des soultes reçues et versées restent dans l'alinéa d'origine. Aucune réforme de fond.",
        "Maintenir le point de départ du 1er janvier 2000, la référence historique au quatrième alinéa de l'article 150 A bis dans sa rédaction antérieure à la promulgation de la loi de finances pour 2004, et la condition de non-imposition de la soulte reçue au titre de l'année de l'échange. La loi n° 2003-1311 du 30 décembre 2003 reste une référence historique, sans actualisation."
    ),
    '162': (
        ['162.xml'],
        "Réécriture à droit constant : le moment de disponibilité de la quote-part mise en réserve est formulé directement et l'extension aux autres associés et membres est maintenue dans le deuxième alinéa. La note intégrée au texte est réécrite et sa balise de présentation non autorisée est retirée. Aucune réforme de fond.",
        "Conserver toute l'énumération, la mention des noms et adresses indiqués à l'administration et l'option pour le régime fiscal des sociétés de capitaux. La note (1), incluse dans source_xml, reste au troisième paragraphe et maintient l'application aux résultats des exercices ouverts à compter du 1er janvier 1996 pour les associés visés à l'article 8 ter."
    ),
    '163-0 A': (
        ['163-0_A.xml'],
        "Réécriture à droit constant : les conditions et étapes des deux calculs par quotient sont explicitées dans leurs subdivisions et alinéas d'origine. Les cas dispensés de la condition de montant sont énumérés plus lisiblement. Les imputations de déficits et la limitation au barème progressif restent expresses. Aucune réforme de fond.",
        "Contrôle : revenu exceptionnel comparé à la moyenne de trois années, ajout d'un quart puis multiplication par quatre ; revenu différé divisé par le nombre d'années civiles d'échéances augmenté de un, puis multiplication par le même coefficient. Préserver les trois cas dérogatoires du deuxième alinéa du I et les renvois au premier alinéa et à l'article 197."
    ),
    '163-0 A bis': (
        ['163-0_A_bis.xml'],
        "Réécriture à droit constant : la détermination du quotient et de l'impôt supplémentaire est exposée étape par étape dans le premier alinéa. Le champ historique du rachat mutualiste et le plafonnement du diviseur à dix années restent au deuxième alinéa. Aucune réforme de fond.",
        "Le régime mutualiste demeure lié à la conversion au 8 décembre 2001 et aux facultés statutaires alors en vigueur ; ne pas l'étendre au nouveau compte de capitalisation. La note source relative à l'article 19 V de la loi n° 2009-1673 du 30 décembre 2009 indique l'application à compter de l'imposition des revenus de 2009. Le diviseur ordinaire correspond aux années de déduction des cotisations, sans plafond de dix ans hors du cas particulier du deuxième alinéa."
    ),
    '163-0 A ter': (
        ['163-0_A_ter.xml'],
        "Réécriture à droit constant : le bénéficiaire, les primes concernées et l'étalement sont explicités ; le caractère exprès et irrévocable de la demande est isolé dans la dernière phrase du premier alinéa. L'incompatibilité avec le quotient de l'article 163-0 A reste au deuxième alinéa. Aucune réforme de fond.",
        "L'étalement couvre l'année de disposition et les trois années suivantes, par parts égales. Conserver les sportifs médaillés olympiques et paralympiques, leurs guides le cas échéant, et les primes des fédérations délégataires destinées à l'encadrement. Le caractère irrévocable ne vaut pas option automatique."
    ),
    '163 bis': (
        ['163_bis.xml'],
        "Réécriture à droit constant : l'option pour le prélèvement libératoire, son assiette et ses conditions sont exposées plus directement sans déplacer les alinéas. Le I périmé, les règles de recouvrement et toutes les exclusions sont maintenus. Aucune réforme de fond, notamment aucune extension aux nouveaux comptes de retraite.",
        "Maintien du taux de 7,5 %, de l'abattement de 10 %, du versement non fractionné et de la justification des cotisations déductibles ou liées à un revenu exonéré dans l'État compétent pour l'imposer. Les prestations de l'article 80 decies, des PER de l'article L. 224-1 et des sous-comptes français de l'article L. 225-1 du CMF restent exclues. Ne pas transposer ce prélèvement aux prestations du futur compte collectif sans disposition législative expresse."
    ),
    '163 bis AA': (
        ['163_bis_AA.xml'],
        "Réécriture à droit constant : les deux affectations ouvrant droit à exonération, la règle de demi-exonération à trois ans et ses exceptions sont exposées plus lisiblement. Les conditions relatives aux revenus, crédits d'impôt, maintien après indisponibilité et dépôt restent dans leurs alinéas. Aucune réforme de fond ; la participation et l'épargne retraite existantes restent distinctes du compte collectif proposé.",
        "Conserver la demi-exonération pour l'indisponibilité de trois ans et l'exonération totale sous les conditions de réaffectation du deuxième alinéa. La dénomination administrative « direction départementale du travail et de l'emploi » est celle de la source et doit faire l'objet d'un contrôle de coordination avec les textes sur le dépôt des accords ; elle n'est pas remplacée silencieusement. Les notes source fixent l'entrée en vigueur au 1er octobre 2019 par le II de l'article 9 du décret n° 2019-807 du 30 juillet 2019, dans le cadre du I de l'article 9 de l'ordonnance n° 2019-766 du 24 juillet 2019 qui prévoyait au plus tard le 1er janvier 2020. Aucun effet fiscal du nouveau compte collectif n'est déduit de cette ancienne transition."
    ),
    '163 bis B': (
        ['163_bis_B.xml'],
        "Réécriture à droit constant : le salarié est explicitement désigné comme bénéficiaire de l'exonération des versements de l'entreprise ; les conditions de remploi et d'indisponibilité des revenus sont reformulées directement. Les I, II, II bis, II ter et III ainsi que l'emplacement du II ter dans le bloc d'origine sont conservés. Aucune réforme de fond.",
        "Ne pas confondre les conditions du II, qui mentionne l'exonération définitive et les salariés ou anciens salariés, avec le II bis applicable aux PER et sous-comptes français paneuropéens. Les crédits d'impôt restent restituables par dérogation à l'article 199 ter. L'exonération du futur compte de capitalisation nécessite une disposition fiscale nouvelle ; elle n'est pas ajoutée par assimilation aux plans existants."
    ),
    '163 bis D': (
        ['163_bis_D.xml'],
        "Réécriture à droit constant : les trois avantages exonérés sont présentés avec les textes de privatisation dont ils relèvent ; la réserve propre aux opérations de 1993 reste dans un second alinéa. Les retours de ligne de présentation deviennent deux paragraphes. Aucune réforme de fond.",
        "Conserver les articles 11, 12 et 13 modifiés de la loi n° 86-912 du 6 août 1986 et les deux lois décidant les privatisations, n° 86-793 du 2 juillet 1986 et n° 93-923 du 19 juillet 1993. La réserve de l'article 150-0 D au deuxième alinéa reste limitée aux opérations décidées par la loi de 1993."
    ),
    '163 bis E': (
        ['163_bis_E.xml'],
        "Réécriture à droit constant de la phrase unique : les exonérations visées et la réserve tenant à l'article 150-0 D sont reliées explicitement, sans ajout de condition ni modification du champ. Les sauts de ligne de présentation sont remplacés par un paragraphe. Aucune réforme de fond.",
        "Maintien des deux renvois aux 25° et 26° de l'article 81 et de la réserve de l'article 150-0 D. La disposition n'accorde aucune exonération générale au-delà de ces deux cas."
    ),
    '163 bis F': (
        ['163_bis_F.xml'],
        "Réécriture à droit constant : les débitants bénéficiaires, les avantages et leur fondement sont présentés avant la réserve de l'article 150-0 D, dans le même alinéa normatif. Aucun avantage ni bénéficiaire nouveau ; aucune réforme de fond.",
        "Conserver la désignation des débitants par l'article 568, les trois avantages et l'article 3 de la loi n° 94-1135 du 27 décembre 1994 propre à la privatisation de la Société nationale d'exploitation industrielle des tabacs et allumettes. Le déplacement interne de la réserve au sein du même alinéa n'en change pas la portée."
    ),
    '163 bis G': (
        ['163_bis_G_1.xml', '163_bis_G_2.xml', '163_bis_G_3.xml'],
        "Réécriture à droit constant : la distinction entre avantage salarial et gain de cession, les dates d'imposition, les durées d'activité, les conditions d'attribution et les règles de prix sont exposées en phrases plus courtes. Toutes les subdivisions et tous les alinéas sont conservés, notamment les trois premiers alinéas du II auxquels renvoie le I. Les dérogations, structures étrangères et délégations restent intégrales. Aucune réforme de fond : le taux normal d'IS proposé n'est pas substitué aux taux propres à ces revenus.",
        "Maintien du taux spécial de 30 %, du seuil de trois ans et des périodes d'activité ou de mandat prises en compte selon la société bénéficiaire ; maintien de l'échange sans soulte et de son événement d'imposition reporté. Contrôler les seuils distincts : 75 % pour filiales et produit des détentions des sous-filiales, 15 % de détention continue et 75 % de détention des personnes morales, capitalisation strictement inférieure à 150 millions d'euros, moyenne sur soixante jours de bourse, immatriculation depuis moins de quinze ans. Maintien des trois ans après dépassement, des six mois pour les héritiers et l'augmentation de capital, des douze mois pour l'agrégation des capitalisations, et des deux motifs de décote. Les cinq premiers alinéas du II et les numéros de phrases du 2 restent stables. Incohérence de seuil préexistante à contrôler : le II, 4 impose une capitalisation strictement inférieure à 150 millions, tandis que le II bis, 1° prévoit une dérogation en cas de dépassement ; le cas d'égalité au seuil n'est pas expressément traité et n'est pas corrigé. La note source applique la rédaction issue du I de l'article 25 de la loi n° 2026-103 du 19 février 2026 aux bons attribués à compter du 1er janvier 2026 ; préserver ce champ temporel sans étendre cette rédaction aux bons antérieurs."
    ),
}


def main():
    sources = json.loads(Path('source.json').read_text())
    assert len(sources) == len(METADATA) == 16
    result = []
    for source in sources:
        files, reason, notes = METADATA[source['number']]
        proposed = '\n'.join((Path('drafts') / name).read_text().strip() for name in files)
        result.append({
            **{key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')},
            'proposed_xml': proposed,
            'reason': reason,
            'review_notes': notes,
            'status': 'rewrite_draft',
        })
    Path('answer.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    main()
