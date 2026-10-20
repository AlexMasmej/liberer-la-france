import json
import re
from pathlib import Path

s = json.loads(Path('source.json').read_text())[0]
paragraphs = re.findall(r'<p>(.*?)</p>', s['source_xml'], re.S)
assert len(paragraphs) == 68
original = list(paragraphs)


def replace(n, old, new):
    assert paragraphs[n - 1].count(old) == 1, (n, old)
    paragraphs[n - 1] = paragraphs[n - 1].replace(old, new)


replace(1,
        "après accord du maire de la commune d'implantation et dans les conditions fixées par l'article L. 442-11",
        "sans accord préalable du maire de la commune d'implantation et dans les conditions fixées par l'article L. 442-11")
replace(1,
        "ainsi que les logements appartenant à des personnes privées et vacants depuis plus d'un an.",
        "ainsi que les logements appartenant à des personnes privées et vacants, sans durée minimale de vacance. Pour l'exercice de cette faculté de gestion, les conditions de décence, de loyer et de ressources prévues à l'article L. 442-11 s'appliquent aussi aux logements vacants depuis un an ou moins. Cette extension ne restreint pas les autres facultés de gestion déjà ouvertes par le présent article.")

replace(4,
        "avec l'accord de la ou des collectivités ou communautés intéressées",
        "sans accord administratif préalable de la ou des collectivités ou communautés intéressées")

replace(6,
        "Exclusivement dans les communes appartenant à une zone d'urbanisation continue de plus de 50 000 habitants définie au 1° du B du I de l'article 1406 bis du code général des impôts ainsi que dans les communes de plus de 15 000 habitants en forte croissance démographique définies par décret pris en application du dernier alinéa du II de l'article L. 302-5 du présent code, elles peuvent de même",
        "Sur l'ensemble du territoire relevant de leur compétence géographique, sans condition tenant au taux communal de logements sociaux, elles peuvent de même")

for n in (12, 65):
    replace(n,
            "dans le respect du dernier alinéa du même article L. 411-2" if n == 12 else "dans le respect des dispositions du dernier alinéa du même article L. 411-2",
            "dans le respect des règles d'affectation des résultats de l'activité relevant de la gestion de services d'intérêt économique général prévues à l'article L. 411-2")

for n in (17, 18, 19):
    replace(n,
            "et que l'avis de la commune ou de l'établissement public de coopération intercommunale compétent en matière d'habitat a été recueilli",
            "; aucun avis de la commune ou de l'établissement public de coopération intercommunale compétent en matière d'habitat n'est requis au titre du présent alinéa")
replace(20,
        "et que l'avis de la commune ou de l'établissement public de coopération intercommunale compétent a été recueilli",
        "; aucun avis de la commune ou de l'établissement public de coopération intercommunale compétent n'est requis au titre du présent alinéa.")

replace(27,
        "cette participation est soumise à l'accord du représentant de l'Etat dans le département du lieu de l'opération ou du projet. A défaut d'opposition de sa part notifiée dans le délai de deux mois à compter de la date de la réception de la demande, son avis est réputé favorable.",
        "cette participation n'est soumise à aucun accord préalable du représentant de l'Etat, à aucune demande à ce titre ni à aucun délai d'opposition.")

replace(28,
        "L'opération fait l'objet d'une autorisation préalable du ministre chargé du logement.",
        "L'opération n'est soumise à aucune autorisation préalable du ministre chargé du logement.")
replace(28,
        "conventions conclues en application de l'article L. 351-2 du présent code",
        "conventions conclues en application de l'article L. 831-1 du présent code")

replace(30,
        "lorsqu'elles ont été agréées à cet effet",
        "sans agrément spécifique à cet effet")

replace(31,
        "-avec l'accord du maire de la commune d'implantation et du représentant de l'Etat dans le département, gérer,",
        "-gérer,")
replace(31,
        "A défaut d'opposition de la part du représentant de l'Etat notifiée dans le délai de deux mois à compter de la date de la réception de la demande, son avis est réputé favorable ;",
        "Aucun accord préalable du maire de la commune d'implantation ni du représentant de l'Etat dans le département, aucune demande à ce titre et aucun délai d'opposition ne sont requis pour les activités prévues au présent alinéa, y compris au titre de l'article L. 411-2 ;")

replace(39,
        "définies par décret pris en application du dernier alinéa du II de l'article L. 302-5 du présent code ;",
        "définies par le dernier alinéa du II de l'article L. 302-5 et les décrets pris pour son application, dans leur rédaction applicable aux opérations régulièrement engagées pendant cette expérimentation ;")

replace(47,
        "logements locatifs sociaux mentionnés à l'article L. 302-5",
        "logements locatifs sociaux mentionnés au IV de l'article L. 302-5")
replace(52,
        "logements locatifs sociaux définis à l'article L. 302-5",
        "logements locatifs sociaux définis au IV de l'article L. 302-5")

paragraphs[53] = (
    "La création de telles filiales n'est soumise à aucune transmission spécifique au ministre chargé du logement ni à son accord ou à son opposition préalables. La décision de création peut être exécutée sans délai d'attente sur ce fondement. "
    "Les règles d'affectation des actifs et de financement public qui protègent les missions de logement social de l'organisme mère demeurent applicables."
)
paragraphs[59] = (
    "Une augmentation de capital de la filiale réalisée par l'organisme mère n'est soumise à aucune transmission spécifique au représentant de l'Etat dans la région ni à son accord ou à son opposition préalables. La décision d'augmentation de capital peut être exécutée sans délai d'attente sur ce fondement. "
    "Elle reste soumise aux conditions fixées aux a et b ci-dessus ainsi qu'aux règles d'affectation des actifs et de financement public qui protègent les missions de logement social de cet organisme."
)
replace(62,
        "ayant le même objet que les filiales de logement locatif intermédiaire défini aux quarante-septième à cinquantième alinéas du présent article",
        "ayant pour objet la construction, l'acquisition et la gestion de logements locatifs intermédiaires définis aux 1° à 3° du présent article")
paragraphs[61] += (
    " Les prises de participation dans ces sociétés et les augmentations de capital correspondantes ne donnent lieu à aucune transmission spécifique ni à aucune procédure d'accord ou d'opposition préalables. Les décisions correspondantes peuvent être exécutées sans délai d'attente sur ce fondement."
)

paragraphs.extend([
    "Les suppressions d'accords, d'avis, d'agrément, d'autorisation, de demandes, de transmissions spécifiques et de délais d'opposition prévues au présent article, l'extension territoriale des ventes à des personnes morales et la suppression de la durée minimale de vacance prennent effet à l'entrée en vigueur de la loi portant la présente rédaction. Elles s'appliquent également aux opérations, décisions et procédures en cours, sans nouveau dossier, confirmation, déclaration ni justificatif de remplacement et sans recommencement des délais des procédures qui subsistent. Aucun texte réglementaire pris pour l'application du présent article ne peut rétablir ces formalités ou ces délais pour les activités qui en sont dispensées.",
    "Les décisions régulièrement prises, les contrats et conventions valablement conclus, les aides, exonérations et garanties régulièrement accordées ainsi que les droits et créances antérieurs des organismes, des occupants et des tiers sont préservés. Les stipulations qui se bornent à rappeler les accords, avis, agréments, autorisations, demandes, transmissions ou délais d'opposition supprimés cessent de les imposer pour l'avenir. La suppression des filtres administratifs ne dispense ni des accords des propriétaires et des cocontractants requis par leur titre ou le droit commun, ni du respect des conditions d'urbanisme, de sécurité, de salubrité, de ressources, de loyers, de prix, d'affectation des actifs et de financement public qui restent applicables. Les contrôles légaux des organismes et des aides, les règles de comptabilité distincte et les voies de recours demeurent. Les aides, exonérations, garanties, dispenses et dérogations maintenues restent ouvertes aux opérations et situations futures qui en remplissent les conditions propres. Les responsabilités et recours relatifs aux faits antérieurs sont conservés ; aucune restitution générale ni réouverture d'un délai expiré n'est instituée. L'expérimentation d'usufruit temporaire prévue au trente-neuvième alinéa n'est pas prorogée."
])

assert len(paragraphs) == 70
Path('proposed.xml').write_text('\n'.join('<p>' + x + '</p>' for x in paragraphs) + '\n')
changes = [{'paragraph': i + 1, 'before': a, 'after': b}
           for i, (a, b) in enumerate(zip(original, paragraphs)) if a != b]
Path('paragraph-review.json').write_text(json.dumps(changes, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'source_paragraphs': len(original), 'proposed_paragraphs': len(paragraphs),
                  'modified_positions': [c['paragraph'] for c in changes],
                  'source_characters': len(s['source_xml']),
                  'proposed_characters': Path('proposed.xml').stat().st_size}, ensure_ascii=False))
