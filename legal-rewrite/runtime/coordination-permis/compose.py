"""Complete regulatory coordination of the new L424-6 and L424-7."""
from pathlib import Path
import html
import json

HERE = Path(__file__).resolve().parent
sources = json.loads((HERE / "source.json").read_text())
rows = []


def add(number, body, reason, notes, removed=None, repeal=None):
    source = next(a for a in sources if a["number"] == number)
    row = {k: source[k] for k in ("code_id", "source_id", "source_sha256", "number")}
    row.update(
        proposed_xml="\n".join(
            "<p>" + html.escape(" ".join(p.split()), quote=False) + "</p>"
            for p in body.strip().split("\n\n")
        ),
        reason=reason, review_notes=notes, status="rewrite_draft",
    )
    if removed:
        row.update(change_type="normative_reduction", reform_policy_id="editorial_direction_2026_10_19", removed_provisions=removed)
    if repeal:
        row.update(change_type="full_repeal", repeal_policy_id="editorial_direction_2026_10_19", repeal_scope=repeal)
    rows.append(row)


add(
    "R*424-8",
    """
Le présent article est abrogé pour les permis tacites et les décisions de non-opposition à déclaration préalable intervenus à compter de l'entrée en vigueur de l'abrogation de l'article L. 424-6. Aucun arrêté ne peut fixer ultérieurement des participations sur le seul fondement de ces dispositions pour ces titres.

Pour les permis tacites et les décisions de non-opposition antérieurs, l'autorité compétente conserve, dans les deux mois suivant l'intervention de ces titres, le pouvoir de fixer les participations selon l'ancienne rédaction de l'article L. 424-6. L'arrêté les fixe dans les conditions de l'article R. 424-7 et est notifié dans les conditions de l'article R. 424-10. Les participations régulièrement établies demeurent soumises aux règles de recouvrement, de restitution, de prescription et de recours qui leur sont applicables.

La présente abrogation ne supprime pas les taxes directement exigibles sur leur fondement propre, les engagements conventionnels régulièrement conclus ni les participations régulièrement prescrites par une décision expresse sur un autre fondement légal.
""",
    "Abrogation réglementaire coordonnée avec L424-6 : le pouvoir de prescrire des participations après un titre tacite disparaît pour les titres futurs. Le texte complet règle les anciens titres, leur fenêtre exacte de deux mois, leurs notifications et leurs créances sans supprimer les autres bases fiscales ou conventionnelles.",
    "Le renvoi source à l'article précédent devient explicitement R424-7. Préserver le champ des deux titres tacites/non-opposition et le délai légal transitoire de deux mois. Coordonner le deuxième alinéa de R*424-10 dans le même lot ; ne pas abroger R*424-7 ni L332-28 pour les décisions expresses ou anciennes qui conservent un fondement. Aucun remboursement général, aucune taxe nouvelle ni compensation budgétaire n'est décidé.",
    repeal="Suppression du dispositif réglementaire permettant de fixer les participations par arrêté après un permis tacite ou une non-opposition futurs ; conservation du délai et des créances propres aux titres antérieurs selon L424-6.",
)

add(
    "R*424-10",
    """
L'autorité compétente notifie au demandeur la décision qui accorde ou refuse le permis ou qui s'oppose au projet faisant l'objet d'une déclaration préalable, par tout moyen donnant date certaine à sa réception. La lettre recommandée avec demande d'avis de réception postal reste utilisable. Une notification électronique respecte les conditions légales qui lui sont applicables ; le seul envoi d'un message sans preuve de réception ne suffit pas.

La même règle s'applique aux arrêtés fixant les participations encore exigibles sur le fondement de l'ancienne rédaction de l'article L. 424-6 pour les permis tacites et non-oppositions antérieurs à son abrogation. Aucun arrêté de cette nature ne peut être établi pour les titres postérieurs sur le seul fondement supprimé.

Lorsque la décision accorde le permis sans participation ni prescription, la notification par pli non recommandé demeure possible.

Si le président de l'établissement public de coopération intercommunale prend la décision, il en adresse une copie au maire de la commune.

La faculté d'utiliser un moyen donnant date certaine à la réception s'applique aux notifications effectuées à compter de l'entrée en vigueur du décret portant la présente rédaction, y compris pour les demandes déjà en cours. Les notifications antérieures et les délais qu'elles ont fait courir ne sont pas remis en cause. Le deuxième alinéa suit la transition de l'abrogation de l'article L. 424-6.
""",
    "Réforme de fond : la notification recommandée postale n'est plus le seul moyen admissible lorsqu'une réception certaine peut être prouvée, notamment dans un circuit électronique légalement valable. Conservation de l'exception de pli simple pour les permis sans charge, de la copie au maire et des notifications financières encore utiles aux titres antérieurs. Suppression de la procédure financière pour les nouveaux titres relevant de l'abrogation de L424-6.",
    "Les quatre premiers alinéas conservent leurs objets : décision, participations transitoires, pli simple, copie au maire. Ne pas transformer une simple adresse électronique en acceptation ou preuve de réception ; les conditions du code des relations entre le public et l'administration, hors des cinq codes, demeurent applicables. Les délais d'instruction et de recours ne sont pas changés. La note source du décret 2014-253 fixe le champ historique au 1er avril 2014 ; le nouveau régime de notifications futures ne requalifie pas les actes déjà notifiés sous les anciens régimes.",
    ["Suppression du monopole de la lettre recommandée postale pour les notifications pouvant être effectuées par un autre moyen légal donnant date certaine à leur réception.", "Suppression des notifications d'arrêtés de participations pour les nouveaux titres tacites et non-oppositions privés de ce fondement par l'abrogation de L424-6."],
)

add(
    "R*424-11",
    """
La décision accordant un permis indique les conditions de sa prise d'effet. Pour les permis relevant de la nouvelle rédaction de l'article L. 424-7, elle précise que le permis est exécutoire dès sa notification au demandeur et que l'attente de sa transmission au préfet ne reporte pas cette date. Elle mentionne, lorsqu'elle s'applique, la dérogation prévue à l'article L. 424-9.

Les permis notifiés avant l'entrée en vigueur de cette nouvelle rédaction restent soumis aux conditions de prise d'effet qui leur étaient applicables. Les mentions de la décision ne peuvent ni dispenser de la transmission légalement requise au préfet ni réduire ses pouvoirs de contrôle.
""",
    "Réécriture complète de la mention des conditions de prise d'effet et coordination expresse avec L424-7. La décision ne peut plus présenter l'attente de transmission au préfet comme un préalable pour le nouveau champ, tout en annonçant les délais spéciaux encore applicables.",
    "Source sans numéro interne conservée en deux paragraphes complets. Renvois L424-7 et L424-9 ajoutés pour identifier le fondement et la réserve ; L424-9 protège les démolitions et les décisions qu'il vise. Les anciens permis ne sont pas réputés exécutoires à une date nouvelle. Les règles de transmission et de contrôle de légalité du CGCT et de leurs extensions aux EPCI demandent leur coordination législative propre, expressément signalée dans L424-7 ; le présent article réglementaire ne prétend pas les abroger.",
    ["Suppression de la mention d'une transmission préalable au préfet comme condition de prise d'effet des nouveaux permis déjà notifiés dans le champ de L424-7."],
)

add(
    "R*424-12",
    """
Lorsque la décision relève du maire ou du président de l'établissement public de coopération intercommunale, cette autorité informe le demandeur de la date à laquelle la décision et le dossier ont été transmis au préfet ou à son délégué, dans les conditions des articles L. 2131-1 et L. 2131-2 du code général des collectivités territoriales. Si cette date lui a déjà été régulièrement communiquée, aucun nouvel envoi de la même information n'est requis.

Pour les permis soumis à la nouvelle rédaction de l'article L. 424-7, cette information constate la transmission et ne constitue pas une condition de prise d'effet. Le retard de transmission ou de communication de sa date ne reporte pas la prise d'effet résultant de la notification, sous réserve de l'article L. 424-9. Les obligations de transmission de l'autorité et les pouvoirs de contrôle du préfet sont maintenus.

La dispense de nouvel envoi s'applique aux communications effectuées à compter de l'entrée en vigueur du décret portant la présente rédaction. La règle relative à la prise d'effet suit la transition de l'article L. 424-7 ; les décisions antérieures restent régies par les conditions qui leur étaient applicables.
""",
    "Réécriture complète de l'information sur la transmission et coordination avec la prise d'effet dès notification prévue au nouveau L424-7. Réduction limitée : pas de second envoi d'une date déjà régulièrement communiquée. L'information utile au contrôle reste due lorsqu'elle n'a pas été fournie et ne peut devenir une nouvelle autorisation d'exécuter.",
    "Conserver maire et président de l'EPCI, préfet ou délégué, décision et dossier ainsi que les deux références L2131-1 et L2131-2 du CGCT. La transmission demeure obligatoire : il ne s'agit pas d'un régime sans contrôle préfectoral. La réserve de L424-9 ne neutralise pas les délais des opérations irréversibles. La dispense porte uniquement sur la répétition de la même information, sans présomption d'accès du demandeur à un système administratif auquel il n'aurait pas légalement accès.",
    ["Suppression du second envoi de la date de transmission déjà régulièrement communiquée au demandeur et de tout effet suspensif de cette information dans le nouveau champ de L424-7."],
)

assert {(a['code_id'], a['source_id']) for a in rows} == {(a['code_id'], a['source_id']) for a in sources}
dest = HERE.parents[1] / "batches" / "coordination-permis" / "001.json"
dest.parent.mkdir(exist_ok=True)
tmp = dest.with_suffix('.json.tmp')
tmp.write_text(json.dumps(rows, ensure_ascii=False, indent=2))
tmp.replace(dest)
print(json.dumps({"articles": len(rows), "file": str(dest)}, ensure_ascii=False))
