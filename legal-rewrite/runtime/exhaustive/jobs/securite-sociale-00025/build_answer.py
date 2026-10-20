import json
from pathlib import Path


EDITORIAL_NOTES = {
    "L162-16-5": (
        "Réécriture à droit constant : le premier alinéa distingue la convention, la décision du comité, l'opposition ministérielle et la fixation de la marge. Les phrases relatives à la prise en charge avant publication du prix et au partage de l'écart entre prix d'achat et prix de cession sont décomposées dans leurs alinéas d'origine. Le tarif unifié et ses modulations sont conservés. Aucune réforme de fond de policy.json ne concerne ce dispositif.",
        "Les neuf alinéas et les subdivisions I à IV sont conservés. Le III maintient le calcul : prix d'achat, augmenté de la fraction réglementaire de l'écart avec le prix de cession diminué de la marge, puis de la marge. Aucun montant ni aucune fraction ne sont inventés. La rédaction du tarif unifié au IV est coordonnée avec celle du IV de L. 162-16-6 dans ce lot. Les réserves relatives à L. 162-16-5-1 et L. 162-16-5-2 restent dans le quatrième alinéa du I."
    ),
    "L162-16-5-1": (
        "Réécriture à droit constant : l'assurance maladie et les ministres sont explicitement désignés comme acteurs. Les conditions de fin de prise en charge sont exprimées séparément pour l'inscription au remboursement, le retrait ou la suspension, le refus d'inscription et le retrait des demandes. Le délai de demande d'inscription et les compétences réglementaires sont maintenus. Aucune réforme de fond du projet ne s'applique à l'accès précoce aux médicaments.",
        "Les neuf alinéas, les subdivisions et le délai de deux semaines sont conservés. Le renvoi du I à L. 162-22-6 ne correspond à aucune entrée dans le corpus public fourni ; L. 162-22-7 y renvoie désormais aux établissements de L. 162-22. Le renvoi de la source est maintenu, sans substitution silencieuse : sa coordination doit être vérifiée. La note source relative au A du IV de l'article 78 de la loi n° 2020-1576 du 14 décembre 2020 prévoit une entrée en vigueur fixée par décret, au plus tard le 1er juillet 2021 ; cette donnée historique ne fixe aucune date nouvelle."
    ),
    "L162-16-5-1-1": (
        "Réécriture à droit constant : les déclarations annuelles, l'assiette des remises et leurs cinq motifs de majoration sont rendus plus lisibles. Le calcul comparatif du chiffre d'affaires au prix net de référence, le sens du versement ou de la restitution et les modalités conventionnelles de paiement sont explicités sans changer leur ordre ni leurs limites. Aucune réforme de fond de policy.json ne vise ces remises pharmaceutiques.",
        "Les vingt-six alinéas et les subdivisions I à VI sont conservés, notamment le second alinéa du I auquel renvoient L. 162-16-5-1-2 et L. 162-16-5-4. Sont maintenus le 15 février, les cent quatre-vingts jours, la signature avant le 1er mai, les deux années successives au maximum, la décote maximale de 3 % et le délai de deux mois. Le plafond de restitution reste limité à la remise du II pour l'indication et la période d'accès précoce concernées. Le III, A, 2° conserve la référence simultanée à l'année civile pour laquelle la remise a été versée et à l'ensemble de la période de prise en charge : cette articulation temporelle, déjà présente dans la source, mérite un contrôle d'application et n'est pas corrigée implicitement. Le V continue à reporter le calcul jusqu'à la fin du régime de L. 162-16-5-1-2 en intégrant toutes les périodes."
    ),
    "L162-16-5-1-2": (
        "Réécriture à droit constant : les conditions d'accès au régime temporaire, les trois bases tarifaires possibles, les majorations des remises et les quatre cas de cessation sont présentés par des phrases plus directes. Le rôle de l'entreprise dans le recueil des données et celui des ministres dans l'octroi de la prise en charge sont explicites. Aucune réforme de fond du projet ne concerne ce régime.",
        "Les vingt-sept alinéas et les subdivisions I à IX sont conservés. Sont maintenus le premier montant non nul de l'indemnité, les alternatives liées au prix maximal ou à une autre prise en charge, la deuxième année de l'autorisation, les cent quatre-vingts jours et la durée réglementaire maximale de trois ans. La source désigne une autorisation prévue ou délivrée au présent article au IV, A et au IV, B, 1°, alors que le V décrit un arrêté accordant la prise en charge : cette articulation terminologique est conservée et doit être contrôlée. La reconduction annuelle des majorations figure toujours dans les deux alinéas où la source la mentionne. Les renvois financiers à L. 162-16-5-1-1 restent coordonnés avec les alinéas correspondants de cet article dans ce lot."
    ),
    "L162-16-5-2": (
        "Réécriture à droit constant : les régimes tarifaires selon l'existence d'une autre indication remboursée, les exceptions à la déclaration et aux remises, les obligations de l'entreprise et la procédure de pénalité sont distingués dans leurs alinéas d'origine. Les cas de cessation et de poursuite de la prise en charge compassionnelle sont reformulés sans extension de leur champ. Aucune réforme de fond de policy.json ne porte sur ce dispositif.",
        "Les vingt-neuf alinéas et les subdivisions I à VIII sont conservés. L'exclusion des remises annuelles pour l'indication financée forfaitairement reste au III, A. Le 15 février, la pénalité annuelle maximale de 10 % du chiffre d'affaires réalisé en France pour le produit au dernier exercice clos, les sept mois pour la décision d'inscription et le mois pour le dépôt de la demande sont maintenus ; la source ne qualifie pas l'assiette de cette pénalité de hors taxes et cette qualification n'est pas ajoutée. Le VI reste soumis aux cas de fin du V et permet la poursuite dès la date de cessation des effets de l'autorisation ou du cadre. La poursuite d'un traitement individuel reste exclue en cas d'évaluation défavorable de l'indication au sens de L. 5121-9 du code de la santé publique."
    ),
    "L162-16-5-3": (
        "Réécriture à droit constant : la longue phrase définissant le champ de l'obligation de mentionner l'indication est scindée en deux phrases dans le même alinéa. L'obligation lors de la prescription, la transmission lors de la facturation et le recouvrement de l'indu restent distincts. L'attribut de présentation de la source est supprimé. Aucune réforme de fond du projet ne modifie ces obligations.",
        "Les deux alinéas et tous les renvois sont maintenus. Une articulation préexistante appelle un contrôle : le régime temporaire de L. 162-16-5-1-2 est explicitement inclus dans le champ de l'obligation de prescription, mais la phrase relative à la condition de prise en charge lors de la facturation n'énumère que l'autorisation, le cadre compassionnel et la continuité de traitement. La proposition n'ajoute pas implicitement ce régime à cette seconde énumération. Une extension expresse de cette condition, si elle est souhaitée, nécessiterait une coordination de ce même premier alinéa."
    ),
    "L162-16-5-4": (
        "Réécriture à droit constant : les engagements du laboratoire, les conditions applicables après l'accès précoce et le calcul du reversement sont exprimés en phrases plus courtes. Le régime du prix d'achat après la fin du maintien de la prise en charge et les garanties procédurales de la pénalité sont conservés. Aucune réforme de fond de policy.json ne concerne la continuité de ces traitements.",
        "Les onze paragraphes de la source et les subdivisions I, I bis, I ter et II sont conservés ; les conteneurs div sont supprimés sans déplacement des alinéas. La durée minimale est fixée par décret dans la limite d'une année : cette limite n'est pas transformée en plafond de toute période supplémentaire. L'exception liée à la sécurité des patients demeure. La pénalité du II reste limitée aux manquements au I, sans extension aux I bis et I ter ; elle reste plafonnée à 30 % du chiffre d'affaires hors taxes réalisé en France pour la spécialité pendant les vingt-quatre mois précédant la constatation. Le reversement du second alinéa du 2° du I bis conserve la déduction des remises du II de L. 162-16-5-1-1 et la comparaison avec le prix de référence."
    ),
    "L162-16-5-4-1": (
        "Réécriture à droit constant : le cas d'acquisition par l'Agence nationale de santé publique est placé en tête de phrase, puis la formule de chiffre d'affaires est exprimée directement. Une seconde phrase, dans le même alinéa, conserve l'ensemble des dispositions auxquelles ce calcul s'applique. Aucune réforme de fond du projet ne modifie ce calcul.",
        "L'alinéa unique conserve le produit du prix d'achat par l'agence et du nombre d'unités administrées ou dispensées pendant la période, ainsi que les trois renvois au présent code et celui à l'article 62 de la loi n° 2021-1754 du 23 décembre 2021 de financement de la sécurité sociale pour 2022. Les métadonnées de la source annoncent une fin de validité au 1er janvier 2028 et l'état ABROGE_DIFF ; la réécriture ne supprime ni ne reporte cette échéance et ne la présente pas comme la date d'une réforme nouvelle."
    ),
    "L162-16-5-5": (
        "Réécriture à droit constant : l'assurance maladie devient le sujet explicite de la prise en charge. La définition ministérielle du forfait annuel par patient et la compétence du décret en Conseil d'État sont distinguées en phrases successives dans l'alinéa unique. Aucune réforme de fond du projet ne concerne ce financement.",
        "Le champ reste celui des médicaments autorisés comme médicaments de thérapie innovante préparés ponctuellement, visés au 17° de L. 5121-1 du code de la santé publique. Le forfait annuel par patient est conservé sans montant nouveau. Ce régime demeure distinct du dispositif de traitement par médicaments de thérapie innovante prévu au V de L. 162-16-6 ; aucune assimilation tarifaire n'est introduite."
    ),
    "L162-16-6": (
        "Réécriture à droit constant : les étapes de convention, de publication, de décision du comité et d'opposition ministérielle sont décomposées dans le premier alinéa. Le remboursement sur facture, le tarif unifié et le financement des thérapies innovantes sont reformulés en conservant les calculs, les conditions d'arrêt des versements et le recueil des données à la charge de l'entreprise. Aucune réforme de fond de policy.json ne vise ces tarifs et versements.",
        "Les dix-sept alinéas et les subdivisions I à V, A à C, 1° et 2° sont conservés. Les délais de cent quatre-vingts jours, de quatre-vingt-dix jours et les deux délais distincts de quinze jours restent liés aux mêmes événements. Le produit du nombre d'unités par le tarif demeure strictement inférieur au forfait ; le prix limite reste égal au tarif. L'interdiction de facturer l'écart aux patients, l'arrêt des versements et le plafond fondé sur le coût net des traitements à même visée sont maintenus. Le V, B vise les établissements de santé mentionnés au I, alors que le I ne les énumère pas directement : cette imprécision de la source est conservée ; les articles L. 162-22-7 et L. 162-23-6 du corpus renvoient aux établissements de L. 162-22 et doivent être pris en compte pour vérifier cette articulation. Le IV est coordonné avec celui de L. 162-16-5. La note source rattachée au VII de l'article 49 de la loi n° 2023-1250 du 26 décembre 2023 fixe l'entrée en vigueur au 1er janvier 2024 ; elle reste une donnée historique."
    ),
}


def main():
    sources = json.loads(Path("source.json").read_text(encoding="utf-8"))
    result = []
    assert len(sources) == len(EDITORIAL_NOTES) == 10
    for source in sources:
        number = source["number"]
        reason, review_notes = EDITORIAL_NOTES[number]
        item = {
            key: source[key]
            for key in ("code_id", "source_id", "source_sha256", "number")
        }
        item.update(
            proposed_xml=Path("drafts", number + ".xml").read_text(encoding="utf-8").strip(),
            reason=reason,
            review_notes=review_notes,
            status="rewrite_draft",
        )
        result.append(item)
    Path("answer.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
