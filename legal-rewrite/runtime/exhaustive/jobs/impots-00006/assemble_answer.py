import collections
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path


METADATA = [
    {
        "reason": "Réécriture à droit constant des déductions pour les équipements des navires. Les conditions techniques, l'affectation à l'activité et les dates de conclusion des contrats sont exprimées en phrases distinctes dans leurs alinéas d'origine. Les comparateurs de coûts, plafonds, règles d'étalement, événements mettant fin à la déduction, conditions propres au bailleur et reprise des sommes déduites sont explicités sans changement de régime. Aucune réforme de fond : le réexamen général des aides annoncé dans policy.json ne définit aucune suppression ni modification de ce dispositif.",
        "review_notes": "Les treize alinéas du I restent dans leur ordre : le dixième porte toujours la condition de pavillon visée au IV ; les trois derniers portent toujours les comparateurs et plafonds visés au III. Taux conservés : 125 %, 105 %, 85 % et 20 %, avec 85 % pour le second alinéa du 4°. Plafonds conservés : 15 millions d'euros par navire pour le 2°, et rédaction commune à 10 millions pour le 3° et le second alinéa du 4°, sans créer de plafonds séparés. La date initiale reste celle du décret visé au V de l'article 42 de la loi n° 2023-1322 ; aucune date n'est suppléée ; échéance au 31 décembre 2027. Points préexistants conservés à contrôler : le III vise d'abord le 4° globalement au taux de 20 %, puis son second alinéa au taux de 85 % ; le V parle de la durée d'utilisation du navire alors que les II et III visent celle des biens ; le comparateur du I emploie marchandises et passagers, tandis que les catégories éligibles emploient marchandises ou passagers. Ces articulations ne sont pas corrigées par une modification silencieuse de leur champ. Renvois aux articles L. 313-7, 209-0 B et 39 decies C maintenus."
    },
    {
        "reason": "Réécriture à droit constant : les caractéristiques des équipements frigorifiques et de traitement de l'air sont distinguées des conditions d'affectation et d'inscription à l'actif, sans déplacement d'alinéa. L'étalement, la limitation des déductions à la sortie de l'actif, la poursuite après acquisition du bien loué et la cessation lors d'une cession ou de la fin du contrat sont formulés avec un sujet explicite. L'exclusion du bailleur et du nouvel exploitant est maintenue. Aucune réforme de fond définie par policy.json ne vise cette déduction.",
        "review_notes": "Taux de 40 %, valeur d'origine hors frais financiers et période du 1er janvier 2019 au 31 décembre 2022 conservés pour les acquisitions ou contrats concernés. Cette période close n'est ni supprimée ni rouverte : les déductions peuvent encore produire des effets pendant la durée normale d'utilisation. La référence précise à la section 1 de l'annexe I du règlement (UE) n° 517/2014, y compris son intitulé et le règlement qu'il abroge, est maintenue pour ce régime historique. Renvoi au 1 de l'article L. 313-7 conservé. Aucun point de départ supplémentaire de l'étalement n'est introduit aux II et III, qui ne le précisent pas comme le fait l'article 39 decies C bis."
    },
    {
        "reason": "Réécriture à droit constant des conditions ouvertes aux établissements d'enseignement de la conduite et aux associations agréées. La condition d'imposition selon un régime réel est rendue explicite pour les deux catégories de bénéficiaires ; les simulateurs doivent toujours être dotés d'un poste de conduite. Les modalités d'étalement et de location sont exprimées en phrases plus courtes, à subdivisions et alinéas conservés. Les exclusions du bailleur et du nouvel exploitant et la condition de minimis sont conservées. Aucune réforme de fond de policy.json n'est applicable à ce régime.",
        "review_notes": "Taux de 40 %, valeur d'origine hors frais financiers et période du 9 mai 2019 au 8 mai 2021 conservés, sans réouverture de l'éligibilité. Agréments des articles L. 213-1 et L. 213-7 du code de la route et renvoi au 1 de l'article L. 313-7 du code monétaire et financier maintenus. La source comporte au II une discordance entre le fait déclencheur, sortie du bien de l'actif, et la date de calcul, date de la cession : elle reste signalée sans assimilation silencieuse de ces événements. Le IV conserve le règlement (UE) 2023/2831. La note source renvoie au VII de l'article 77 de la loi n° 2025-127 du 14 février 2025, qui rend les I à VI de cet article de loi applicables aux aides octroyées à compter du 1er janvier 2024 : cette règle temporelle accompagne le changement de référence européenne et ne prolonge pas la période d'acquisition des simulateurs."
    },
    {
        "reason": "Réécriture à droit constant : les bénéficiaires, la condition d'imposition et les caractéristiques des engins sont rendus plus lisibles ; les trois catégories numérotées sont conservées. Le II distingue expressément le régime réservé aux entreprises de bâtiment et de travaux publics remplaçant un matériel ancien par un engin conforme à la phase V. L'étalement et les conséquences d'une cession ou de la fin du contrat sont explicités dans leurs alinéas existants. Les taux de droit commun et des PME et les conditions européennes restent distincts. Aucune réforme de fond de policy.json ne fixe de nouveau paramètre pour ce régime.",
        "review_notes": "Taux de 40 % et de 60 % conservés. Les périodes du 1er janvier 2020 au 31 décembre 2022 et du 1er janvier 2024 au 31 décembre 2026 restent séparées ; aucune éligibilité n'est créée pour 2023. Le II demeure limité au bâtiment et aux travaux publics, à la phase V de l'annexe II du règlement (UE) 2016/1628 et au remplacement de matériels de plus de cinq ans pour le même usage. Points de rédaction préexistants conservés : rattachement de la condition d'émissions à la fin de l'énumération des motorisations au I ; emploi de la seule valeur des biens au VI, alors que les I et IV précisent valeur d'origine hors frais financiers. Le VI n'est pas réécrit pour trancher cette articulation d'assiette. Définition des PME par l'annexe I du règlement (UE) n° 651/2014 et condition du règlement (UE) 2023/2831 maintenues. La note source, VII de l'article 77 de la loi n° 2025-127 du 14 février 2025, fixe l'application des I à VI de cet article de loi aux aides octroyées à compter du 1er janvier 2024 : ne pas traiter cette note comme une réforme future ni comme une extension de la référence de minimis aux aides antérieures."
    },
    {
        "reason": "Réécriture à droit constant : les conditions relatives à l'entreprise, à son régime d'imposition et à l'absence d'installations au 1er janvier 2020 sont formulées séparément, au sein du même alinéa. La nature du gazole et des équipements éligibles est conservée intégralement. Les règles de calcul, d'étalement, de poursuite après acquisition et de cessation du droit en location sont clarifiées sans élargissement du champ. Aucune réforme de fond de policy.json ne modifie cette déduction sectorielle.",
        "review_notes": "Taux de 40 %, valeur d'origine hors frais financiers, inscription à l'actif immobilisé, acquisitions et contrats du 1er janvier 2020 au 31 décembre 2022 conservés. La condition d'absence d'installations au 1er janvier 2020 reste distincte de cette période. Le dispositif demeure réservé aux PME de commerce de détail de gazole non routier ; gazole non coloré et tracé, définition des PME à l'annexe I du règlement (UE) n° 651/2014 et respect de son article 17 maintenus. L'interdiction faite au bailleur et au nouvel exploitant est conservée. La note source fixe l'entrée en vigueur au 1er janvier 2022 en application de l'article 40 de l'ordonnance n° 2021-1843 du 22 décembre 2021 ; elle ne remplace pas les bornes d'acquisition et de conclusion des contrats inscrites dans l'article."
    },
    {
        "reason": "Réécriture à droit constant des qualifications à court et à long terme, avec des sujets explicites pour les plus-values et moins-values. Les règles de priorité des titres, les fonds de placement immobilier, les deux régimes historiques de location, les annulations de vente et les changements de régime fiscal sont conservés dans leurs subdivisions et alinéas. Au 12, la formule de ventilation est expliquée en plusieurs phrases dans le même alinéa, en conservant le rapport de valeurs vénales et la soustraction du prix de revient. Aucune réforme de fond de policy.json ne modifie ces qualifications ; aucune exonération générale des bénéfices réinvestis n'est créée.",
        "review_notes": "Les trente-cinq alinéas et les subdivisions 1 à 12, dont 6 bis et 6 ter, restent dans leur ordre. Seuil de plus de 50 % au 6 ter, qualité professionnelle du porteur et majoration des seuls amortissements non réintégrés maintenus. Régimes des contrats conclus jusqu'au 31 décembre 1995 et à compter du 1er janvier 1996 distincts ; date du 31 décembre 1992 conservée au 9. Le 12 garde moins de deux ans au deuxième alinéa et plus de deux ans au troisième, sans remplacer ce dernier seuil par au moins deux ans. Point de coordination préexistant : le troisième alinéa du 6 renvoie au délai de trois ans de l'article 210 B sans distinguer ses régimes ; dans la version publique fournie de l'article 210 B, l'engagement de conservation figure au a du 3 pour le régime sur agrément. Ce renvoi général est maintenu, sans étendre ni supprimer silencieusement l'obligation pour les opérations de plein droit ou anciennes. Les autres renvois, notamment 39 B, les six dispositions du code des assurances, 239 nonies, 155, 202 ter et L. 236-3 du code de commerce, sont conservés. Pour le 12, la note source impose de tenir compte du II de l'article 65 de la loi n° 2025-127 du 14 février 2025 et des conditions de l'article 13 de l'ordonnance n° 2023-393 du 24 mai 2023 ; aucune date supplémentaire ni disposition transitoire inventée ne s'y substitue."
    },
    {
        "reason": "Réécriture à droit constant des cessions de droits de crédit-bail et des cessions ultérieures du bien. Les phrases relatives aux amortissements théoriques sont découpées sans déplacement des alinéas. Les régimes des contrats conclus jusqu'au 31 décembre 1995 et à compter du 1er janvier 1996 restent séparés aux 1, 4 et 6. La minoration du prix amortissable des droits, leur prise en compte dans le prix de revient, les réintégrations et l'extension aux éléments incorporels amortissables sont conservées. Aucune mesure de fond de policy.json ne modifie ces contrats ni leurs droits historiques.",
        "review_notes": "Les dix-neuf alinéas logiques, y compris les intitulés historiques, sont conservés dans leur ordre. Date d'application du 1er octobre 1989 maintenue au 5 pour les seules cessions qu'il vise. Les références aux 1 et 2 de l'article L. 313-7 et aux articles 239 sexies, 239 sexies B et 239 sexies C restent en place ; la version publique de 239 sexies C distingue elle aussi les contrats antérieurs et postérieurs au 1er janvier 1996. Ambiguïté préexistante au 4, pour les contrats conclus à compter du 1er janvier 1996 : la source rattache augmenté au prix de revient, puis enchaîne selon le cas, des amortissements ... soit de la fraction. Ce rattachement et cette alternative restent conservés ; ils ne sont pas remplacés silencieusement par une addition aux amortissements pratiqués. La formule du 6 reste différente selon la période : rapport de valeurs pour les anciens contrats ; somme de la valeur réelle du terrain et des loyers non déduits à la date du transfert, diminuée de la valeur du terrain à la signature, pour les contrats postérieurs. Les renvois au premier alinéa du 4 sont maintenus sans déplacer les intitulés ni leurs alinéas cibles."
    },
    {
        "reason": "Réécriture à droit constant : le champ des sommes exclues du régime à long terme et le régime applicable au décès de l'exploitant sont exprimés directement. Au 5, la qualité d'entreprise de l'actionnaire apparaît dès le début ; les conditions relatives aux entités distributrices, à leur Etat d'établissement et à l'origine des distributions sont séparées en phrases dans le même alinéa. La clause de preuve concernant les Etats et territoires non coopératifs conserve ses critères propres. Les mentions abrogées ou périmées et toute la numérotation restent en place. Aucune réforme de fond de policy.json n'est appliquée à ces régimes.",
        "review_notes": "Mentions 1, 1 bis, 3 et 4 conservées, notamment l'abrogation pour les redevances prises en compte à compter du 1er janvier 2002. Au 5 : exercices clos à compter du 31 décembre 2001, détention d'au moins deux ans et perception au cours de l'exercice précédent maintenus. Les exclusions des trois catégories de fonds au b du 2°, le renvoi à la rédaction de L. 214-37 antérieure à l'ordonnance n° 2013-676 du 25 juillet 2013, la convention fiscale et la clause d'assistance administrative demeurent cumulatifs. La réserve de l'article 41 et les renvois à la loi n° 85-695 et à L. 214-28 sont conservés. Le dernier alinéa maintient la référence au 2° du 2 bis de l'article 238-0 A et le critère principalement un objet et un effet autres : il n'est pas aligné sur le critère distinct ni pour objet ni pour effet, dans un but de fraude fiscale de l'article 39 duodecies, 2, c. Les subdivisions abrogées ne justifient pas un statut retained_unchanged pour l'article, dont les dispositions opérantes sont réécrites."
    },
]


def plain(xml):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]*>", " ", xml)).strip()


def paragraphs(xml, index):
    if index in (5, 7):
        return [plain(p) for p in re.findall(r"<p>(.*?)</p>", xml, re.S)]
    return [plain(p) for p in re.split(r"(?:<br\s*/?>\s*){2,}", xml) if plain(p)]


def digits(text):
    return collections.Counter(re.findall(r"\d+(?:[.,/-]\d+)*", plain(text)))


sources = json.loads(Path("source.json").read_text())
assert len(sources) == len(METADATA) == 8
answer = []
report = []
allowed = set("p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote".split())
for i, (source, metadata) in enumerate(zip(sources, METADATA)):
    proposed = Path(f"drafts/{i:02}.xml").read_text().strip()
    root = ET.fromstring("<root>" + proposed + "</root>")
    for element in list(root.iter())[1:]:
        assert element.tag in allowed
        for key, value in element.attrib.items():
            assert key in ("rowspan", "colspan") and re.fullmatch(r"[0-9]+", value)
    before = paragraphs(source["source_xml"], i)
    after = [plain(p) for p in re.findall(r"<p>(.*?)</p>", proposed, re.S)]
    assert len(before) == len(after), source["number"]
    for j, (old, new) in enumerate(zip(before, after)):
        assert digits(old) == digits(new), (source["number"], j + 1, digits(old) - digits(new), digits(new) - digits(old))
    assert source["source_xml"].count("<table") == proposed.count("<table")
    assert plain(source["source_xml"]) != plain(proposed)
    obj = {key: source[key] for key in ("code_id", "source_id", "source_sha256", "number")}
    obj.update(proposed_xml=proposed, **metadata, status="rewrite_draft")
    answer.append(obj)
    report.append({"number": source["number"], "paragraphs": len(after), "proposed_characters": len(proposed), "numeric_tokens_by_paragraph": "identical", "xml": "valid"})

assert len({a["source_id"] for a in answer}) == 8
assert all(set(a) == set("code_id source_id source_sha256 number proposed_xml reason review_notes status".split()) for a in answer)
Path("answer.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"output_file": "answer.json", "article_count": len(answer), "checks": report}, ensure_ascii=False, indent=2))
