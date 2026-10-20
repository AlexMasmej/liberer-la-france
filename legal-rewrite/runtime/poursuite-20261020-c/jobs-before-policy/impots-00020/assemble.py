import json
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
sources = json.loads((ROOT / 'source.json').read_text())
drafts = [
    ['150-0-D-01.xml', '150-0-D-02.xml', '150-0-D-03.xml'],
    ['150-0-D-ter.xml'],
    ['150-0-E.xml'],
    ['150-0-F.xml'],
    ['150-A-bis.xml'],
]
reasons = [
    "Réécriture intégrale à droit constant : distinction entre le prix de cession et le prix d'acquisition pour le calcul du gain net ; clarification du champ et des conditions des abattements ordinaires et renforcés, des points de départ de la durée de détention, des valeurs d'acquisition particulières, de l'ordre d'imputation des moins-values et des reprises de pertes. Les longues phrases sont fractionnées à l'intérieur de leur alinéa. Les subdivisions et les emplacements des alinéas sont conservés. Aucune réforme de fond de policy.json ne vise ces plus-values ; les mesures de CSG salariale, d'IS et de capitalisation des retraites ne sont donc pas étendues à ce régime.",
    "Réécriture intégrale à droit constant : présentation explicite des conditions à remplir par le cédant et la société, des modalités de l'abattement global, du complément de prix, des cessions échelonnées au profit de jeunes agriculteurs et des événements entraînant une remise en cause. Les conditions et les échéances sont réparties en phrases plus courtes sans changer les alinéas ni les subdivisions. Aucune réforme de fond : les orientations sur la retraite ne modifient pas les conditions fiscales du départ à la retraite des dirigeants ni le régime agricole distinct.",
    "Réécriture à droit constant de l'obligation déclarative : les contribuables sont expressément désignés comme les personnes tenues de déclarer les gains nets et distributions, dans les conditions du renvoi conservé au 1 de l'article 170. Aucune modification du champ, des modalités de déclaration ou du régime fiscal et aucune réforme de fond.",
    "Réécriture à droit constant : la phrase identifie directement les plus-values distribuées par le fonds de placement immobilier et conserve dans le même alinéa le régime d'imposition ainsi que la réserve relative au 4 ter du II de l'article 150-0 A. Aucune réforme de fond ; les orientations de CSG salariale et de retraite ne sont pas appliquées à ces distributions.",
    "Réécriture intégrale à droit constant : précision de la méthode d'appréciation de l'actif immobilier, séparation en phrases des règles relatives aux titres des sociétés immobilières pour le commerce et l'industrie et clarification des échanges antérieurs puis postérieurs au 1er janvier 2000. Les reports historiques, le traitement de la soulte et les événements mettant fin au report sont conservés dans leurs alinéas d'origine. Aucune réforme de fond ni transposition des orientations concernant les autres régimes fiscaux.",
]
reviews = [
    "Conserver les renvois entre les articles 150-0 A, 150-0 B, 150-0 D ter, 150-0 F, 150 UB, 163 quinquies C et D, 163 bis H, 210 E bis et 1655 sexies. Aucun alinéa n'a été ajouté ou déplacé : les renvois aux quatrième et cinquième alinéas du A du 1 ter, aux quatrième à avant-dernier alinéas du 2° du B du 1 quater et à l'avant-dernier alinéa du 1 quinquies gardent leur cible. Contrôler la formulation préexistante du quota : les quatrième et cinquième alinéas du A du 1 ter exigent plus de 75 %, tandis que son dernier alinéa vise un quota de 75 % ; cette différence est conservée, sans harmonisation silencieuse. Préserver les taux de 50 %, 65 % et 85 %, le seuil de 25 %, toutes les durées de détention, les reports jusqu'à la dixième année incluse et les valeurs historiques de 1949, 1972 et 1978 pour les acquisitions antérieures au 1er janvier 1979. Le renvoi du 9 à l'ancien quatrième alinéa de l'article 150 A bis et celui du 9 bis à l'article L. 214-37 dans sa rédaction antérieure à l'ordonnance du 25 juillet 2013 restent historiques. Les trois notes source sont prises en compte comme règles d'application de la loi existante : article 16 de la loi n° 2026-103 du 19 février 2026, pour les apports réalisés à compter du 1er janvier 2026 et pour les exercices clos à compter de cette date ; article 24 de cette loi pour les retraits des titres de l'article 163 bis H à compter du 15 février 2025. Ces dates ne constituent pas l'entrée en vigueur d'une réforme proposée. Les notes ne sont pas insérées dans le corps afin de ne pas modifier les cibles d'alinéas. Aucune disposition nouvelle n'est nécessaire pour ce seul lot.",
    "Conserver la coordination avec les 1 ter, 1 quater et 1 quinquies de l'article 150-0 D, le complément de prix du 2 du I de l'article 150-0 A, les aides du I de l'article 73 B et la résiliation au sens de l'article 1229 du code civil. Les 41 alinéas sont conservés à leur emplacement, notamment les deuxième et troisième alinéas du IV. Vérifier ensemble les montants de 500 000 € et de 600 000 €, les seuils stricts de plus de 50 %, de plus de la moitié des revenus et d'au moins 25 %, les cinq années continues, les deux derniers exercices, la détention d'au moins un an, les fenêtres de deux ans, le délai de six ans et la surveillance de trois ans. Le B du II bis conserve ses règles propres de cessions échelonnées ; il n'est pas confondu avec le II. La note source du B du III de l'article 11 de la loi n° 2026-103 du 19 février 2026 prévoit l'application de sa modification aux cessions réalisées à compter du lendemain de la publication de cette loi ; aucune date de publication n'est déduite de sa seule date de signature. Pas de coordination nouvelle avec le transfert de cotisations vieillesse prévu par le projet.",
    "Renvois aux I et II de l'article 150-0 A et au 1 de l'article 170 conservés. Le 1 de l'article 170 a été consulté dans le corpus public pour vérifier le sujet de l'obligation déclarative. La note source de l'article 17, III, de la loi n° 2013-1278 du 29 décembre 2013 prévoit l'application aux gains réalisés et aux distributions perçues à compter du 1er janvier 2013 ; cette règle historique n'est pas remplacée par une date nouvelle. Aucune coordination de fond supplémentaire.",
    "Les quatre cibles de renvoi sont conservées : 4 ter du II de l'article 150-0 A ; 3° du II de l'article L. 214-81 du code monétaire et financier ; article 239 nonies ; 1 ou 2 de l'article 200 A. Ne pas supprimer la réserve ni choisir entre les modalités d'imposition des 1 et 2. Aucune note source d'application temporelle n'est fournie et aucune date nouvelle n'est introduite.",
    "Les cinq alinéas restent à leur place : les troisième et quatrième alinéas demeurent les cibles du dernier alinéa. Conserver le caractère historique du renvoi au I ter de l'article 160, absent du corpus courant consulté, et vérifier sa version applicable aux échanges antérieurs au 1er janvier 2000. Le III de l'article 150 UB, consulté dans le corpus public, vise expressément les anciennes rédactions de l'article 150 A bis et de l'article 160 ; ne pas substituer silencieusement le régime actuel de l'article 150 UB au régime résiduel du présent article. La note source limite l'application aux plus-values en report d'imposition au 1er janvier 2004. Elle cite la loi n° 200-1311 du 30 décembre 2003 : ce numéro semble comporter une coquille, car la référence à la loi de finances pour 2004 figurant au 9 de l'article 150-0 D est n° 2003-1311 ; anomalie signalée sans correction de la source. Préserver le seuil de 10 % de la valeur nominale, l'imposition immédiate de la fraction correspondant à la soulte pour les échanges du troisième alinéa, et les quatre événements de fin du report : cession, rachat, remboursement, annulation.",
]

allowed = {'p', 'br', 'table', 'thead', 'tbody', 'tfoot', 'tr', 'th', 'td',
           'b', 'strong', 'i', 'em', 'u', 'sup', 'sub', 'ul', 'ol', 'li',
           'div', 'span', 'blockquote'}
answers = []
assert len(sources) == len(drafts) == len(reasons) == len(reviews) == 5
for source, files, reason, review in zip(sources, drafts, reasons, reviews):
    xml = '\n'.join((ROOT / 'fragments' / name).read_text().strip() for name in files)
    doc = ET.fromstring('<root>' + xml + '</root>')
    original = ET.fromstring('<root>' + source['source_xml'] + '</root>')
    assert [e.tag for e in doc] == [e.tag for e in original], source['number']
    for element in doc.iter():
        if element is doc:
            continue
        assert element.tag in allowed
        assert all(k in {'rowspan', 'colspan'} and v.isdigit() for k, v in element.attrib.items())
    answer = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    answer.update(proposed_xml=xml, reason=reason, review_notes=review, status='rewrite_draft')
    answers.append(answer)
(ROOT / 'answer.json').write_text(json.dumps(answers, ensure_ascii=False, indent=2) + '\n')
for answer in answers:
    print(answer['number'], len(answer['proposed_xml']), answer['status'])
