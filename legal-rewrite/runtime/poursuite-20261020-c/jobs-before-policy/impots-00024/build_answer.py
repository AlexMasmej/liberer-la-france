import json
from pathlib import Path


SPECS = [
    (
        "151-nonies.xml",
        "Réécriture à droit constant : les conditions de chaque report, les engagements des bénéficiaires et les événements mettant fin au report sont formulés avec des sujets explicites. Les exonérations après cinq ans, les règles d'apport, de fusion et de scission et l'obligation annuelle de suivi restent distinctes. Les subdivisions et les vingt-huit alinéas sont conservés. Aucune réforme de fond du projet ne modifie ces régimes de plus-values.",
        "Les troisième et quatrième alinéas de la source énoncent deux fois l'imposition au nom du bénéficiaire à la fin du report : cette redondance préexistante est conservée pour ne supprimer ni déplacer un alinéa. Au IV bis, la formule source « prend fin à la date […] ou jusqu'à la date » est syntaxiquement discordante ; la proposition explicite la priorité de la date antérieure sans ajouter d'événement. Sont conservés les engagements d'acquitter l'impôt au II, de déclarer la plus-value aux III, IV et IV bis, les durées de cinq ans, le seuil strictement supérieur à 50 % des droits de vote et les renvois, notamment au 1° du 1 du III de l'article 975 et au seul I de l'article 151 octies B, vérifiés dans le corpus public. La note source relative aux 1 et 2 du B du IX de l'article 31 de la loi n° 2017-1837 du 30 décembre 2017 applique la rédaction issue du 7° du B du I de cet article à l'IFI dû à compter du 1er janvier 2018 et maintient, pour l'ISF dû jusqu'à 2017 inclus, les dispositions modifiées par le B dans leur rédaction au 31 décembre 2017 ; cette règle historique reste à maintenir lors de la consolidation. Aucun taux nouveau d'IS ni date d'entrée en vigueur du projet n'est introduit ici.",
    ),
    (
        "151-decies.xml",
        "Réécriture à droit constant : les bénéficiaires de l'intéressement sont identifiés dans la phrase principale ; l'affectation au plan d'épargne d'entreprise et le renvoi aux conditions et à la limite du code du travail font l'objet de propositions distinctes. L'alinéa unique et le champ des bénéfices industriels et commerciaux et non commerciaux sont conservés. Aucune réforme de fond n'est appliquée à ce régime d'intéressement.",
        "Maintien de toutes les catégories de bénéficiaires, de l'absence d'option des sociétés de personnes pour l'IS, de l'affectation au plan d'épargne d'entreprise et du renvoi à l'article L. 3315-3 du code du travail. La note source indique une coordination résultant des articles 1er, 3 et 12-I de l'ordonnance n° 2007-329 du 12 mars 2007 ; elle ne fixe aucune date de réforme future. Ce régime ne constitue pas le nouveau compte de capitalisation collective du projet.",
    ),
    (
        "153.xml",
        "Réécriture à droit constant de la phrase unique : l'interdiction de déduire l'impôt sur le revenu est énoncée directement pour le calcul des revenus nets concernés. Les simples sauts de ligne de la source sont remplacés par un paragraphe. Aucune réforme de fond ne modifie cette interdiction.",
        "Le champ du renvoi aux I à VII bis de la présente sous-section est intégralement maintenu. L'interdiction vise l'impôt sur le revenu ; elle n'étend ni ne remplace les règles propres aux cotisations sociales ou à la CSG. La coordination de la déductibilité de la CSG salariale prévue par le projet relève de l'article 154 quinquies, hors du présent lot.",
    ),
    (
        "154.xml",
        "Réécriture à droit constant : le contribuable est désigné comme auteur de la demande de déduction du salaire du conjoint. La participation effective, le paiement des cotisations et prélèvements sociaux et le classement en traitements et salaires sont explicités en phrases séparées dans le même alinéa. Le II et son champ sociétaire sont conservés. Aucune réforme de fond du projet ne concerne cette déduction.",
        "Conservation de la demande du contribuable, de la participation effective du conjoint, du versement des cotisations de sécurité sociale et d'allocations familiales ainsi que des autres prélèvements sociaux en vigueur. Le renvoi au V de la présente sous-section et l'extension aux sociétés des articles 8 et 8 ter restent inchangés. Aucun plafond ni nouveau taux n'est ajouté ; les deux alinéas et les subdivisions I et II restent à leur place.",
    ),
    (
        "154-bis.xml",
        "Réécriture à droit constant : les cotisations obligatoires, les contrats d'assurance groupe, les régimes facultatifs et les versements d'épargne retraite sont distingués par des phrases plus courtes au sein de leurs alinéas d'origine. Les exclusions de garantie, les conditions des garanties de santé et les trois plafonds de déduction restent complets. La présentation des formules est clarifiée sans modification de taux, d'assiette ou de plafond. Aucune réforme de fond n'est étendue à ces régimes de non-salariés.",
        "Contrôle des formules conservées : retraite, maximum entre 10 % du bénéfice limité à huit plafonds annuels augmenté de 15 % de la fraction entre un et huit plafonds, et 10 % d'un plafond ; prévoyance, 7 % d'un plafond plus 3,75 % du bénéfice, au maximum 3 % de huit plafonds ; perte d'emploi subie, maximum entre 1,875 % du bénéfice limité à huit plafonds et 2,5 % d'un plafond. La réduction au titre des a et a bis du 18° de l'article 81, l'option du deuxième alinéa de l'article L. 224-20, l'exclusion du 6° de l'article L. 142-3 et la prise en compte des revenus exonérés hors plus-values et moins-values professionnelles à long terme sont maintenues. Renvoi préexistant à contrôler : le I cite l'article L. 652-7 du CSS au titre des facultés de rachat ; dans le corpus public fourni, cet article décrit des cotisations obligatoires et ne mentionne pas expressément de faculté de rachat. Ce renvoi est conservé sans substitution. Les quatorze alinéas, les références aux articles L. 644-1, L. 654-1 et L. 652-1 et la mention III périmé sont maintenus. Le compte de capitalisation du projet, destiné d'abord aux salariés privés, n'est pas assimilé à ces contrats ni soumis automatiquement à ces déductions.",
    ),
    (
        "154-bis-0-a.xml",
        "Réécriture à droit constant : les chefs d'exploitation ou d'entreprise agricole sont explicitement désignés comme bénéficiaires des déductions. Les conditions des contrats et versements, les exclusions de garanties, la formule de plafond et la limite propre aux contrats familiaux sont exprimées en phrases plus lisibles. Les dix alinéas et les subdivisions sont maintenus. Aucune réforme de fond de la retraite des salariés privés n'est étendue au régime agricole.",
        "Maintien du renvoi au 2° de l'article L. 144-1, de l'option du deuxième alinéa de l'article L. 224-20, des plans et du sous-compte français mentionnés, et de l'exclusion des garanties des 4° à 6° de l'article L. 142-3. La limite demeure le maximum entre 10 % du revenu professionnel limité à huit plafonds annuels, augmenté de 15 % de la fraction entre un et huit plafonds, et 10 % d'un plafond annuel ; elle reste réduite des versements d'entreprise exonérés selon les a et a bis du 18° de l'article 81. La distinction entre revenus exonérés et abattements, l'exclusion des plus-values et moins-values professionnelles à long terme, l'affiliation familiale exigée et la limite d'un tiers par personne sont conservées. Le renvoi au « premier alinéa » dans l'alinéa relatif aux revenus exonérés demeure à sa place. Les mentions II abrogé et IV périmé ne sont pas des emplacements « Réservé. » et ne justifient pas une sortie retained_unchanged.",
    ),
    (
        "154-bis-a.xml",
        "Réécriture à droit constant : les deux alinéas opposent plus directement la prise en compte des prestations de remplacement et l'exclusion des indemnités journalières correspondant aux affections décrites par le texte. Le bénéficiaire et les organismes payeurs sont explicitement désignés. Aucune réforme de fond, notamment de CSG ou de revalorisation des pensions, n'est appliquée à ces prestations.",
        "Le renvoi reste limité aux deuxième et troisième alinéas du I de l'article 154 bis, dont les positions sont conservées dans la proposition correspondante. L'exclusion exige à la fois un traitement prolongé et une thérapeutique particulièrement coûteuse ; elle vise les indemnités journalières versées par les organismes de sécurité sociale. La note source conserve l'application aux exercices ou périodes d'imposition ouverts à compter du 1er janvier 2017 et précise, pour la réforme de l'épargne retraite, l'entrée en vigueur du I de l'article 9 de l'ordonnance n° 2019-766 du 24 juillet 2019 au 1er octobre 2019, fixée par le II de l'article 9 du décret n° 2019-807 du 30 juillet 2019, dans la limite initialement prévue du 1er janvier 2020. Ces dates historiques ne sont pas une date d'entrée en vigueur du projet.",
    ),
    (
        "155.xml",
        "Réécriture à droit constant : l'intégration des activités accessoires, les ajustements du bénéfice, les deux composantes du prix de cession et les régimes d'imposition distincts sont formulés avec des sujets et des opérations explicites. Les conditions alternatives de 5 % et 10 %, la définition de l'activité professionnelle et les deux conditions cumulatives de location meublée sont conservées. Aucun changement de fond du projet relatif au logement n'est appliqué à la qualification fiscale de cette activité.",
        "Maintien des vingt-cinq alinéas, de toutes les subdivisions, du 1° abrogé du IV et des renvois, notamment aux articles 151 septies VII, 39 duodecies à 39 novodecies, 150-0 A à 150 VH et 156 I. Les rapports de durée, la valeur d'origine et le traitement des amortissements demeurent distincts. L'option expresse du 3 du II est maintenue ; le seuil de 10 % reste conditionné au respect du seuil de 5 % à l'exercice précédent. Les recettes de location meublée doivent excéder strictement 23 000 € et les autres revenus énumérés ; pour les non-résidents, la comparaison porte sur les revenus de même nature soumis à un impôt équivalent dans l'État de résidence. L'annualisation au début de la location et à la cessation totale est conservée. La note source vise le II de l'article 49 de la loi n° 2019-1479 du 28 décembre 2019 et les revenus et profits perçus ou réalisés à compter du 1er janvier 2020, tandis que la version fournie débute le 21 février 2026. Cette note historique ne précise pas le champ temporel de chacune des évolutions ultérieures, notamment de la dérogation des non-résidents ; ce décalage préexistant doit être pris en compte lors de la consolidation historique.",
    ),
    (
        "155-a.xml",
        "Réécriture à droit constant : le bénéficiaire étranger des sommes et les personnes auxquelles elles sont fiscalement imputées sont distingués dans des phrases séparées. Les catégories de services et droits, les trois cas alternatifs d'imposition, la portée territoriale, la responsabilité solidaire et la règle de reversement restent intégralement énoncés. Aucune réforme de fond n'est apportée à ce dispositif.",
        "Les sept alinéas et les I à IV sont conservés. Les critères de contrôle direct ou indirect, de preuve de l'activité industrielle ou commerciale prépondérante et de régime fiscal privilégié au sens de l'article 238 A demeurent alternatifs. La solidarité reste plafonnée au montant des sommes perçues et le IV maintient l'impôt réputé déjà acquitté en cas de reversement total ou partiel. La note source, issue du II de l'article 10 de la loi n° 2023-1322 du 29 décembre 2023, fixe l'application aux revenus perçus à compter du 1er janvier 2024 ; aucune autre date n'est créée.",
    ),
    (
        "155-b.xml",
        "Réécriture à droit constant : les conditions personnelles et temporelles de l'exonération des impatriés sont présentées en phrases distinctes. Les règles de changement de fonctions, de rémunération de comparaison, de séjours à l'étranger et d'option entre les plafonnements sont rendues plus lisibles. Les revenus de source étrangère visés au II et la prise en compte partielle des moins-values restent complets. Aucune réforme de fond du projet n'est appliquée à ce régime particulier.",
        "Conservation des onze alinéas, du forfait optionnel de 30 %, des cinq années civiles antérieures sans domicile fiscal en France, du terme au 31 décembre de la huitième année civile suivant la prise de fonctions et de la condition des a et b du 1 de l'article 4 B. Les plafonds alternatifs restent 50 % de la rémunération totale ou 20 % de la rémunération imposable résultant du 1, avec leurs assiettes distinctes. Le caractère direct et exclusif de l'intérêt de l'employeur, le renvoi au contrôle de l'article L. 233-3 du code de commerce, l'exclusion de l'article 81 A et les conditions conventionnelles du II sont maintenus ; les moins-values du c sont toujours retenues à 50 %. La note de l'article 6 II de la loi n° 2018-1317 du 28 décembre 2018 réserve les modifications du 1 du I aux rémunérations dues à compter du 1er janvier 2019 pour les personnes ayant pris leurs fonctions en France à compter du 16 novembre 2018. Cette transition doit demeurer applicable aux situations anciennes ; les dates ne sont pas celles du projet.",
    ),
]


def main():
    sources = json.loads(Path("source.json").read_text())
    assert len(sources) == len(SPECS) == 10
    answer = []
    for source, (filename, reason, notes) in zip(sources, SPECS):
        item = {key: source[key] for key in ("code_id", "source_id", "source_sha256", "number")}
        item.update(
            proposed_xml=(Path("drafts") / filename).read_text().strip(),
            reason=reason,
            review_notes=notes,
            status="rewrite_draft",
        )
        answer.append(item)
    Path("answer.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
