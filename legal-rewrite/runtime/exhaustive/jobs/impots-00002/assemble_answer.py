import json
from pathlib import Path
import xml.etree.ElementTree as ET


sources = json.loads(Path('source.json').read_text())
assert len(sources) == 1
source = sources[0]
proposed = '\n'.join(
    Path(f'fragment_{i:02}.xml').read_text().strip() for i in range(1, 5)
)
assert len(ET.fromstring('<root>' + proposed + '</root>')) == 135
Path('proposed.xml').write_text(proposed + '\n')

answer = {
    key: source[key]
    for key in ('code_id', 'source_id', 'source_sha256', 'number')
}
answer.update(
    proposed_xml=proposed,
    reason=(
        "Réécriture intégrale de l'article 39 en conservant ses 135 alinéas, "
        "ses subdivisions et ses dispositions historiques. A droit constant, "
        "les conditions de déduction sont formulées avec des sujets explicites ; "
        "les longues phrases relatives aux emprunts, provisions, véhicules, "
        "crédits-bails et redevances sont décomposées au sein des mêmes alinéas. "
        "Les calculs de plafonnement, de reprise des provisions et du montant "
        "des redevances exclu de la déduction sont explicités sans modifier leurs paramètres. "
        "La coordination liée à la réforme de fond supprimant la C3S dans une tranche "
        "financée consiste à maintenir expressément, au 6° du 1, la déduction "
        "du principal restant dû pour les faits générateurs antérieurs à cette "
        "suppression. La taxe d'aide au commerce et à l'artisanat conserve son "
        "régime. Cette coordination ne fixe ni la date de suppression ni son "
        "financement. Le seuil autonome de 25 % du 12 ter est conservé : "
        "la proposition de taux national normal d'IS à 20 % ne le modifie pas."
    ),
    review_notes=(
        "C3S : articulation vérifiée avec la proposition de l'article L137-30 "
        "du CSS dans le corpus public et avec coordination.json. La suppression "
        "concerne les faits générateurs à compter du 1er janvier d'une année "
        "à fixer par une LFSS financée, avec compensation durable de l'assurance "
        "vieillesse. Coordonner avec L137-30 à L137-38 et D137-30 à D137-36, "
        "en conservant les règles relatives aux périodes antérieures. La déduction "
        "maintenue au 6° du 1 ne rend pas déductibles les sanctions ou pénalités "
        "exclues au 2. Aucun calendrier fiscal nouveau n'est déduit des dates "
        "historiques. Le renvoi au huitième alinéa de l'article 1679 quinquies "
        "a été vérifié dans le corpus public. Incohérence préexistante à contrôler : "
        "au 2° du 4, la source renvoie aux limites déterminées « conformément au a », "
        "alors que le 1° comporte des régimes a et b ; ce renvoi est conservé sans "
        "élargissement silencieux. Au 5° du 1, le quatorzième alinéa continue de "
        "viser la provision pour fluctuation des cours du troisième alinéa, "
        "alors que le cinquième en arrête l'application pour les exercices clos "
        "à compter du 31 décembre 1997 ; cette articulation historique est "
        "conservée et appelle un contrôle de portée résiduelle. Les anciens "
        "régimes de congés payés, d'intérêts, de provisions et de crédit-bail, "
        "ainsi que les mentions d'abrogation, de péremption et d'alinéa disjoint, "
        "sont maintenus. Les renvois ordinaux internes du 5° restent à leur "
        "emplacement d'origine. Notes source prises en compte : le II de "
        "l'article 7 de la loi n° 2026-103 du 19 février 2026 vise la taxe due "
        "au titre des exercices clos à compter du 31 décembre 2026 ; son III "
        "prévoit la compensation à due concurrence de la restriction des critères et de l'assiette "
        "de la taxe de l'article 235 ter C par une taxe additionnelle à l'accise "
        "sur les tabacs du chapitre IV du titre Ier du livre III du code des "
        "impositions sur les biens et services. Ce mécanisme existant n'est pas "
        "affecté au financement des réformes du projet. Le II de l'article 13 "
        "de cette loi prévoit un rapport du Gouvernement au Parlement avant le "
        "1er juillet 2029 sur le coût pour l'Etat et l'efficacité du dispositif "
        "du troisième alinéa du 2° du 1 ; son III rend la rédaction issue de "
        "son I applicable aux exercices clos à compter du 1er janvier 2026. "
        "Ces notes d'application ne sont pas transformées en nouveaux alinéas "
        "codifiés. La période d'acquisition des fonds commerciaux du "
        "1er janvier 2022 au 31 décembre 2029 est conservée. La source est "
        "signalée ABROGE_DIFF et sa validité est bornée au 1er janvier 2027 ; "
        "cette borne de version n'est pas une date de promulgation ou d'entrée "
        "en vigueur de la réforme proposée."
    ),
    status='rewrite_draft',
)
Path('answer.json').write_text(
    json.dumps([answer], ensure_ascii=False, indent=2) + '\n'
)
print('answer.json : 1 article, 135 alinéas,', len(proposed), 'caractères XML.')
