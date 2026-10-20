import json
import re
from html import unescape
from pathlib import Path

ROOT = Path(__file__).parent
sources = json.loads((ROOT / 'source.json').read_text())
references = json.loads((ROOT / 'reference-targets.json').read_text())
by_number = {a['number']: a for a in sources}
proposals = {}


def paras(number):
    return re.findall(r'<p>(.*?)</p>', by_number[number]['source_xml'], re.S)


def body(items):
    return '\n'.join('<p>' + p + '</p>' for p in items)


def replace_once(text, old, new):
    assert text.count(old) == 1, (old, text.count(old))
    return text.replace(old, new, 1)


# Les paragraphes non touchés proviennent intégralement de la source lue.
p = paras('212 bis')
q = p.copy()
q[10] = replace_once(p[10], "En cas d'exercice de l'option mentionnée au V", "En cas d'application du 3 du III et du IV dans les conditions du V")
q[33] = replace_once(p[33], 'Par exception aux I, VI et VII', 'Par exception aux I et VI')
q[45] = "Le 3 du III et le IV s'appliquent au choix de l'entreprise mentionnée au I, pour chaque exercice, sans notification distincte, irrévocabilité ni engagement de durée. Le choix résulte de l'application de ces dispositions dans les calculs fiscaux de l'entreprise ; il ne requiert ni agrément, ni déclaration de remplacement."
q[52] = "VI bis. – 1. Par exception au I, les charges financières nettes mentionnées au 1 du III supportées par l'entreprise définie au 2 du présent VI bis sont intégralement déductibles au titre de l'exercice."
q[55:71] = ['VII. – Abrogé.']
# Les indices ci-dessous suivent la suppression des seize paragraphes du VII.
q[56] = "VIII. – 1. Les charges financières nettes non admises en déduction en application des I et VI, ainsi que les charges reportables des exercices antérieurs dans leur montant légalement constitué, peuvent être déduites à hauteur d'un montant égal à la différence positive entre la limite mentionnée au I appliquée au titre de l'exercice et les charges financières nettes de cet exercice. Les charges financières nettes non admises en déduction après application du présent 1 peuvent être déduites dans les mêmes conditions au titre des exercices suivants. Une même charge n'est déduite qu'une fois."
q[58] = "IX. – Aucune déclaration distincte n'est exigée pour l'application du présent article. Les éléments nécessaires à son application sont justifiés au moyen de la comptabilité, des pièces de financement et des déclarations fiscales par ailleurs légalement requises. Cette disposition ne dispense pas de fournir, lors d'un contrôle et selon les garanties et délais légaux, les éléments nécessaires à la vérification des déductions."
q += [
    "X. – Pour les exercices relevant du régime d'imposition à la distribution des V et VI de l'article 219, les résultats, charges déductibles, charges reportables et capacités de déduction prévus au présent article sont déterminés pour le suivi des assiettes et des déficits prévu au XI de l'article 209. Leur constatation ou leur rectification ne rend pas exigible l'impôt sur les bénéfices conservés, y compris en trésorerie. Les intérêts et remboursements de dettes professionnelles réels ne sont pas, par eux-mêmes, des distributions. Les réintégrations et déductions corrigent les assiettes suivies et, s'il y a lieu, l'imposition des distributions déjà intervenues, sans double imposition ni double déduction.",
    "XI. – La présente rédaction s'applique aux exercices ouverts à compter de l'entrée en vigueur de la présente loi. Les exercices antérieurs, leurs dettes, déductions, exonérations, restitutions, prescriptions et recours restent régis par les règles qui leur étaient applicables. Les charges reportables et les capacités de déduction inemployées antérieurement constituées sont conservées pour leur montant encore utilisable ; elles suivent les conditions du VIII, sans double emploi et, pour les capacités, sans recommencer le délai de cinq exercices. La fraction reportable constituée sous l'ancien VII n'est ni annulée ni recomptée comme une charge nouvelle. Les choix relatifs aux infrastructures déjà effectués restent utilisables mais cessent d'être irrévocables pour les exercices nouveaux. Les contrôles des opérations simulées, des intérêts non professionnels et des prix de transfert ainsi que les impositions minimales des articles 223 VJ et suivants conservent leur champ propre."
]
proposals['212 bis'] = body(q)

proposals['213'] = body([
    "L'impôt sur les sociétés et l'impôt sur le revenu ne sont pas admis dans les charges déductibles pour l'établissement de l'impôt.",
    "La contribution sociale mentionnée à l'article 235 ter ZC reste non déductible lorsqu'elle demeure légalement due au titre d'un fait générateur antérieur ou d'un régime distinct expressément maintenu. Cette règle de non-déductibilité ne constitue aucun fait générateur et ne rétablit aucune contribution sur l'impôt ordinaire dû à la distribution dans le régime des V et VI de l'article 219.",
    "La présente rédaction s'applique à compter de l'entrée en vigueur de la présente loi, sans modifier les dettes, déductions légalement acquises, restitutions, prescriptions et recours relatifs aux périodes antérieures."
])

p = paras('214')
q = p.copy()
q[7] = '6° Abrogé pour les exercices définis au 5 ;'
q[11] = replace_once(p[11], "l'engagement mentionné au deuxième alinéa", "l'engagement mentionné au deuxième alinéa du présent 7°")
q[13] = "Cette déduction n'est subordonnée ni à l'ouverture d'un compte bancaire d'affectation spéciale ni au dépôt des sommes sur un tel compte. À la clôture de l'exercice, une épargne provenant des recettes de cet exercice et au moins égale au montant de la déduction est inscrite à l'actif du bilan et affectée à la couverture de la responsabilité solidaire mentionnée à l'article L. 1253-8 du code du travail. Cette affectation et son utilisation sont retracées dans les écritures comptables ordinaires du groupement, sans registre ni état déclaratif distinct."
q[14] = "Les sommes ainsi affectées peuvent être utilisées pour la mise en œuvre de cette responsabilité solidaire sans délai maximal d'utilisation."
q[15] = "Lorsque les sommes affectées sont utilisées pour l'emploi prévu à l'alinéa précédent, la déduction correspondante est rapportée au résultat de l'exercice au cours duquel cette utilisation est intervenue."
q[16] = "La seule absence d'utilisation des sommes au cours des cinq exercices suivant celui de la déduction n'entraîne aucune réintégration."
q[17] = "Lorsque les sommes affectées sont utilisées à d'autres emplois, les déductions correspondant aux sommes ainsi utilisées sont rapportées au résultat de l'exercice au cours duquel cette utilisation est intervenue. Les déductions correspondant aux sommes qui demeurent affectées à la responsabilité solidaire ne sont pas réintégrées de ce seul fait."
q[18] = "1 bis. Les dispositions du 1 restent applicables lorsqu'une société exerce l'option pour le régime de groupe mentionné à l'article 223 A ou à l'article 223 A bis. Aucune suspension de cinq exercices des déductions n'est attachée à cette option."
q[19] = "Les sommes mentionnées aux 1°, 2° et 5° du 1 qui n'ont pas été déduites en application du 1 bis dans sa rédaction antérieure à l'entrée en vigueur de la présente loi conservent le caractère de ristournes pour les personnes qui les reçoivent."
q += [
    "4. Pour les exercices relevant du régime des V et VI de l'article 219, les bonis, ristournes et parts de bénéfices déductibles en application des 1°, 2° et 5° du 1 sont exclus de l'assiette de l'impôt sur les sociétés à la distribution, sous les conditions des 5° et 7° lorsqu'elles sont applicables. Leur attribution ne leur fait pas perdre cette exclusion. Les autres déductions et les reprises du présent article sont prises en compte dans les résultats de référence et les assiettes suivies conformément au XI de l'article 209. Les reprises ne rendent pas exigible l'impôt sur les bénéfices demeurés dans l'entreprise. Une somme ne peut être à la fois déduite, protégée comme déjà imposée et déduite à nouveau lors de sa distribution. L'imposition personnelle des bénéficiaires reste régie par ses règles propres.",
    "5. La présente rédaction s'applique aux exercices ouverts à compter de l'entrée en vigueur de la présente loi. La suspension prévue à l'ancien 1 bis cesse pour ces exercices, y compris pour les options de groupe en cours. Les exercices antérieurs conservent leur régime, leurs droits, créances, restitutions, prescriptions et recours. Les sommes régulièrement affectées au titre du 8° et non encore réintégrées à l'ouverture du premier exercice nouveau peuvent être conservées sans compte bancaire spécial et sans réintégration à la seule échéance du cinquième exercice ; elles restent affectées à la responsabilité solidaire et sont rapportées au résultat en cas d'utilisation dans les conditions du 8°. La suppression du 6° ne remet pas en cause les réintégrations légalement attachées aux distributions des exercices antérieurs. Les garanties des salariés et organismes créanciers ainsi que la responsabilité solidaire du groupement et de ses membres demeurent applicables."
]
proposals['214'] = body(q)

proposals['216 A'] = body([
    "Lorsqu'ils ne sont pas déductibles des résultats imposables d'une société créancière, les abandons de créances consentis par celle-ci à une autre société dans laquelle elle détient une participation au sens de l'article 145 ne sont pas pris en compte pour la détermination des résultats imposables de la société débitrice.",
    "Cette exclusion n'est subordonnée ni à un engagement joint à une déclaration de résultats, ni à une augmentation de capital au profit de la société créancière, ni à la réalisation d'une telle augmentation avant la clôture du second exercice suivant. L'absence d'engagement ou d'augmentation de capital ne donne lieu à aucune réintégration sur le fondement du présent article.",
    "Pour les exercices relevant du régime d'imposition à la distribution des V et VI de l'article 219, le bénéfice correspondant à un abandon exclu en application du premier alinéa demeure exonéré lors de sa distribution. Il est identifié dans les comptes de suivi prévus au XI de l'article 209, sans double inscription, double déduction ni crédit d'impôt nouveau. La réalité de la créance, de son abandon et de sa non-déductibilité chez la société créancière reste soumise aux règles de preuve et de contrôle de droit commun.",
    "La présente rédaction s'applique aux abandons consentis à compter de l'entrée en vigueur de la présente loi. Pour les abandons antérieurs, les engagements dont le délai d'exécution n'est pas expiré à cette date cessent d'être exigibles et leur seule inexécution ne remet pas en cause l'exclusion du premier alinéa. Les manquements dont le délai d'exécution avait expiré avant cette date, les impositions correspondantes, les autres conditions d'exclusion, restitutions, prescriptions et recours conservent leur régime antérieur."
])

p = paras('217 quinquies')
q = p.copy()
q[-1] = "Un décret fixe les modalités d'application de ces dispositions sans imposer de déclaration ni d'état distinct propres aux déductions du présent article. Les éléments de calcul et les modalités juridiques de l'émission peuvent être justifiés par tout moyen de droit commun, notamment les écritures comptables, les décisions sociales et les documents du dispositif d'actionnariat salarié déjà requis. Aucun modèle administratif ni nouvelle attestation ne conditionne le bénéfice de la déduction. Les déclarations fiscales communes et les contrôles légalement prévus demeurent applicables."
q += [
    "III. – Pour les exercices relevant des V et VI de l'article 219, les déductions des I et II sont prises en compte dans les résultats de référence et les assiettes suivies conformément au XI de l'article 209, y compris pour les salariés recrutés sous le contrat de travail unique. Leur bénéfice n'est pas réservé aux salariés dont le contrat est antérieur à la réforme. Les charges correspondant à une rémunération pour un travail effectif ne deviennent pas des distributions par la seule qualité d'actionnaire du salarié. Aucun impôt ordinaire n'est rendu exigible sur les bénéfices conservés du seul fait de l'application du présent article ; une même déduction n'est utilisée qu'une fois.",
    "La dispense de déclaration et d'état distinct s'applique aux dépôts dont l'échéance intervient à compter de l'entrée en vigueur de la présente loi, y compris lorsqu'ils concernent un exercice antérieur. Les états déjà déposés n'ont pas à être renouvelés. Les conditions de fond des déductions, les créances, restitutions, prescriptions et recours relatifs aux périodes antérieures sont préservés."
]
proposals['217 quinquies'] = body(q)

p = paras('217 octies')
q = p.copy()
q[4] = replace_once(
    p[4],
    "L'engagement du fonds ou de la société de procéder au niveau requis de souscriptions est formalisé par une déclaration remise à l'administration fiscale lors du rachat.",
    "L'engagement du fonds ou de la société de procéder au niveau requis de souscriptions est établi par les documents de l'opération déjà requis, sans déclaration distincte lors du rachat. Aucune décision sociale spéciale, attestation ni aucun registre supplémentaire n'est exigé à ce seul titre. Les pièces existantes sont accessibles dans les conditions des contrôles fiscaux de droit commun."
)
q[26] = replace_once(p[26], "la plus-value de cession est imposée au taux normal de l'impôt sur les sociétés prévu au deuxième alinéa du I de l'article 219", "la plus-value de cession relève du taux normal de l'impôt sur les sociétés, déterminé selon le régime applicable à l'entreprise à l'article 219")
q += [
    "VIII. – Pour les exercices relevant des V et VI de l'article 219, l'amortissement du I et les reprises des V et VI sont pris en compte dans les résultats de référence et les compartiments prévus au XI de l'article 209. Les montants relevant du taux normal en application du VI ne supportent l'impôt ordinaire qu'à la distribution du bénéfice par l'entreprise souscriptrice. La cession des titres, les sommes réparties par un fonds ou une société et les distributions mentionnées aux 1° et 2° du VI ne constituent pas, par leur seule réception, une distribution par cette entreprise à ses propres associés. Les reprises du V corrigent les bases suivies sans impôt ordinaire immédiat sur les bénéfices conservés ; une même fraction d'amortissement n'est reprise qu'une fois. Les restitutions d'aides d'Etat imposées par une décision de l'Union européenne, avec les intérêts de récupération légalement dus, restent distinctes de ce calendrier d'impôt ordinaire.",
    "La dispense de déclaration lors du rachat s'applique aux rachats intervenant à compter de l'entrée en vigueur de la présente loi. Les déclarations antérieures n'ont pas à être renouvelées. Cette dispense ne modifie ni les obligations de souscription, ni les conditions des I à IV, ni les délais des V et VII, ni les engagements et droits antérieurs, ni les règles de cumul et de récupération des aides d'Etat. Les sommes versées dans la période du VII continuent de bénéficier des déductions auxquelles elles ouvrent droit, y compris au cours d'exercices ultérieurs. La présente rédaction ne rouvre aucune période de versement expirée. Les exercices antérieurs conservent leur régime d'imposition, de restitution, de prescription et de recours."
]
proposals['217 octies'] = body(q)


def plain(xml):
    return unescape(re.sub('<[^>]+>', '', xml or ''))


def effect(number, kind, measure_id, description, before, after, unit,
           population, transition, burdens, source_quote, proposed_quote):
    assert len(source_quote) >= 12 and source_quote in plain(by_number[number]['source_xml']), (number, source_quote)
    assert len(proposed_quote) >= 12 and proposed_quote in plain(proposals[number]), (number, proposed_quote)
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit, affected_population=population,
                conditions_and_transition=transition,
                replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


if __name__ == '__main__':
    # Les analyses et preuves sont assemblées seulement après les textes intégraux.
    from answer_reviews import reviews, effects_for, reference_assessments
    answer = []
    for a in sources:
        n = a['number']
        item = {k: a[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
        item['proposed_xml'] = proposals.get(n)
        item.update(reviews[n])
        item['status'] = 'rewrite_draft' if n in proposals else 'retained_unchanged'
        if n not in proposals:
            item['classification'] = 'retained_necessary'
        item['substantive_impact']['effects'] = effects_for(n, effect)
        key = a['code_id'] + '|' + a['source_id']
        item['reference_checks'] = [dict(
            target_key=target,
            view_sha256=references['targets'][target]['view_sha256'],
            assessment=reference_assessments[n][references['targets'][target]['number']]
        ) for target in references['requirements'][key]]
        answer.append(item)
    (ROOT / 'answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
    print('answer.json', len(answer), 'articles')
