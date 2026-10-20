import json
from pathlib import Path


comments = {
    "L302-5": (
        "Réécriture à droit constant : les conditions cumulatives d'assujettissement sont séparées dans la phrase, les compétences de l'Etat et les conditions d'exemption sont explicitées, et les catégories de logements décomptés sont présentées avec leurs réserves propres. Les taux, seuils, dérogations, périodes de décompte et dispositions historiques sont conservés. Aucune réforme de fond des obligations de logement social n'est introduite ; leur maintien est conforme à policy.json.",
        "Les trente paragraphes et les subdivisions I, II, III, III bis, III ter et IV restent en place pour les renvois de L. 302-6 à L. 302-9-1. Le renvoi au 5° de L. 831-1 a été vérifié dans le corpus public. La note source fixe l'entrée en vigueur des dispositions concernées au 1er janvier 2023, sans dater une réforme future. La borne historique du 31 décembre 2016, la condition de signature après publication de la loi du 23 novembre 2018 et le point de départ du 1er janvier 2019 sont conservés. Le II comprend déjà une dérogation à 25 % dans un ensemble normalement soumis à 20 % : l'articulation avec la formule de L. 302-7 nécessite contrôle et n'est pas corrigée implicitement. Au 6° du IV, la source vise un organisme agréé puis un loyer pratiqué par l'association ; cette différence de terminologie est conservée."
    ),
    "L302-6": (
        "Réécriture à droit constant : le champ territorial de l'inventaire est distingué de l'obligation des propriétaires et gestionnaires, puis les étapes d'inventaire, de communication, d'observations et de notification sont exprimées dans des phrases plus directes. L'inventaire complémentaire, l'amende et les modalités de recouvrement sont maintenus. Aucune réforme de fond n'est appliquée à cette procédure de décompte.",
        "Les six paragraphes et les renvois au premier alinéa sont conservés. L'obligation d'inventaire n'est pas limitée aux seules communes déficitaires : la condition de taux concerne la communication prévue au quatrième alinéa. Contrôle effectué sur les seuils de 1 500, 3 500 et plus de 15 000 habitants, les échéances avant les 1er juillet, 1er septembre et 31 décembre, le délai de deux mois, la date du 1er janvier 2002 et l'amende de 1 500 euros. Le dernier alinéa du II et le IV de L. 302-5 restent à leur emplacement."
    ),
    "L302-7": (
        "Réécriture à droit constant : la règle de prélèvement, les exemptions et la formule de calcul sont dissociées ; la longue liste des dépenses déductibles est organisée en phrases au sein du quatrième alinéa ; les bénéficiaires successifs du produit sont identifiés explicitement. Toutes les catégories de dépenses, les plafonds, les reports et l'exception historique de 2012 sont conservés. Aucune baisse fiscale ni suppression de contribution n'est créée par la réforme du logement.",
        "Les dix paragraphes sont conservés, notamment le quatrième pour les dépenses et les septième à neuvième pour les bénéficiaires, visés par L. 302-7-1 et L. 302-9-1. Sont maintenus : facteur de 25 %, objectifs de 25 % ou 20 %, plafond de 5 %, seuil de 4 000 €, plafond de 10 000 € par logement et par an, exonération initiale de trois ans à compter de 2015 et report sur deux années. La note historique relative aux impositions de 2025 et à son exception n'est pas transformée en date d'une réforme projetée. Ambiguïtés préexistantes conservées : la formule rattache 20 % au II de L. 302-5 alors que son deuxième alinéa rétablit 25 % ; les dépenses du quatrième alinéa sont de nouveau évoquées en déduction au septième, ce qui appelle un contrôle de l'absence de double déduction."
    ),
    "L302-7-1": (
        "Réécriture à droit constant : la transmission du rapport, l'ouverture du contradictoire, la suspension motivée et le versement à un bénéficiaire de substitution sont exposés dans leur ordre procédural. Le caractère facultatif de la suspension, sa durée et son plafond financier sont conservés. Aucune réforme de fond de l'affectation des prélèvements n'est introduite.",
        "Le paragraphe unique et ses quatre blocs séparés par des doubles sauts de ligne sont maintenus. Le 31 mars, le délai d'un mois après réception, les deux mois d'observations, le maximum de douze mois et la limite des sommes employées irrégulièrement sont préservés. Les renvois aux septième, huitième et neuvième alinéas de L. 302-7 concordent avec les emplacements conservés. Deux difficultés de la source sont signalées sans correction : le constat vise une utilisation non conforme au présent article alors que les règles d'affectation figurent à L. 302-7 ; la métropole de Lyon est expressément visée dans la procédure contradictoire mais pas dans l'énumération initiale des auteurs du rapport."
    ),
    "L302-8": (
        "Réécriture à droit constant : les règles d'objectif triennal sont formulées en distinguant règle générale, montée en charge des communes nouvelles dans le dispositif, adaptation par contrat et mutualisation intercommunale. Les exigences de typologie, les conditions d'accord, tous les taux et toutes les limites de durée restent inchangés. Aucune liberté conventionnelle de supprimer les obligations de logement social n'est instaurée ; les mécanismes légaux existants sont préservés conformément à policy.json.",
        "Les vingt-sept paragraphes et les subdivisions I à X restent en place. Le renvoi du II au septième alinéa du IV de L. 302-1 a été vérifié dans le corpus. Sont conservés les objectifs de 33 %, 50 % et 100 %, la montée en charge de 15 %, 25 % et 10 %, les planchers contractuels de 25 %, 40 % et 80 %, le plancher de moitié en mutualisation et le maintien de l'objectif total intercommunal. Les trois périodes consécutives du IX, les deux du X et la dérogation pour moins de 5 000 habitants ou une inconstructibilité de 30 % à 50 % sont maintenues. Ambiguïté préexistante : le IX limite d'abord la durée de fixation de l'objectif puis qualifie cette limite de durée du contrat, tandis que L. 302-8-1 prévoit trois ans renouvelables ; cette articulation n'est pas réinterprétée."
    ),
    "L302-8-1": (
        "Réécriture à droit constant des parties au contrat, de ses périmètres, des engagements et de la procédure d'adaptation. En application de l'orientation de policy.json sur le maintien du logement social, une précision normative expresse interdit aux stipulations du contrat de dispenser une commune de ses obligations légales et rappelle les conditions des adaptations des IX et X de L. 302-8. Cet ajout consolide la limite légale du contrat ; il ne modifie ni les taux ni les dérogations existantes et n'institue pas un nouveau régime de fond.",
        "Le paragraphe unique, les subdivisions I et II et les huit blocs séparés par des doubles sauts de ligne sont conservés. La précision est ajoutée dans le bloc qui définit le contenu du contrat, sans déplacer d'alinéa cible. La durée de trois ans renouvelable et la priorité donnée aux arrondissements comptant moins de 15 % de logements sociaux restent inchangées. Coordination avec les IX et X de L. 302-8, sans les confondre avec la demande du II, qui relève du seul IX ; les prélèvements et constats de carence de L. 302-7 et L. 302-9-1 restent applicables selon leurs conditions propres. Le rôle de la commission nationale a été vérifié à L. 302-9-1-1. Le rappel des limites légales ne crée ni extinction ni renégociation obligatoire des contrats antérieurs."
    ),
    "L302-9": (
        "Réécriture à droit constant : les phrases identifient séparément l'auteur du bilan triennal, sa communication au comité régional et sa publicité par le représentant de l'Etat. L'obligation distincte du Gouvernement de rendre compte au Parlement est formulée directement. Le contenu et la périodicité des deux bilans sont maintenus, sans réforme de fond ni nouvel indicateur imposé.",
        "Les deux paragraphes et leurs sauts de ligne sont conservés. Le bilan local reste établi à l'issue de chaque période triennale par la collectivité ou l'établissement ayant approuvé le programme, et le rapport gouvernemental reste transmis tous les trois ans. Coordination inchangée avec les communes visées à L. 302-5 et les périodes de L. 302-8 ; aucune obligation de résultat supplémentaire n'est ajoutée."
    ),
    "L302-9-1": (
        "Réécriture à droit constant : les conditions du constat de carence, les garanties contradictoires et les critères de décision sont exprimés avec leurs sujets explicites. Les phrases séparent les limites de majoration, puis les deux voies de conventionnement et leurs recouvrements propres. Tous les plafonds, délais, recours et conditions de contribution volontaire sont conservés. Aucune sanction nouvelle ni suppression des obligations par convention n'est créée.",
        "Les onze paragraphes sont conservés, notamment les sixième à dixième auxquels renvoient les conventions et recouvrements. Contrôle effectué sur le délai maximal de deux mois d'observations, la majoration pour trois ans au plus à compter du 1er janvier suivant la signature, le maximum de cinq fois le prélèvement, les plafonds de 5 % et 7,5 % et le critère de 150 %. Les limites de 50 000 € en Ile-de-France et Provence-Alpes-Côte d'Azur et de 30 000 € ailleurs, ainsi que les deux délais de mise en demeure de deux mois, sont maintenus. Le plafond d'intermédiation renvoie toujours au quatrième alinéa de L. 302-7. Les déductions ordinaires restent distinctes des sommes recouvrées d'office, non déductibles. La formule préexistante du taux minimal repose sur le déficit quantitatif alors que la carence peut aussi résulter du seul non-respect de la typologie ; aucun taux supplémentaire n'est inventé pour ce cas."
    ),
}


sources = json.loads(Path("source.json").read_text())
answer = []
for source in sources:
    number = source["number"]
    reason, notes = comments[number]
    answer.append({
        **{key: source[key] for key in ("code_id", "source_id", "source_sha256", "number")},
        "proposed_xml": Path(f"draft-{number}.xml").read_text().strip(),
        "reason": reason,
        "review_notes": notes,
        "status": "rewrite_draft",
    })

Path("answer.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")
