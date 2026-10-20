import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
FRAGMENTS = ROOT / "fragments"

# L'article long est composé puis assemblé sans remplacer les sources.
(FRAGMENTS / "167_bis.xml").write_text(
    "\n".join(
        fragment.read_text().rstrip()
        for fragment in sorted(FRAGMENTS.glob("167_bis_*.xml"))
    ) + "\n"
)

EDITORIAL = {
    "167 bis": {
        "file": "167_bis.xml",
        "reason": "Réécriture à droit constant de l'intégralité du régime d'imposition au transfert du domicile fiscal : séparation des étapes de calcul dans les mêmes alinéas, désignation du contribuable comme sujet des obligations, explicitation des conditions cumulatives du sursis, des événements qui y mettent fin, des dégrèvements, restitutions et imputations. Les 76 alinéas, subdivisions, abrogations, régimes historiques et exceptions sont conservés. Aucune réforme de taux ou de retraite n'est appliquée à ce régime distinct ; notamment, la CSG salariale proposée ne concerne pas les prélèvements sur les plus-values de capitaux mentionnés au VIII.",
        "review_notes": "Contrôle effectué sur les seuils de six années sur dix, 50 %, 800 000 €, 12,8 %, 2,57 millions d'euros, les délais de deux et cinq ans, d'un mois et de deux mois, ainsi que les références historiques antérieures aux 1er janvier 2000 et 1er janvier 2006 et la directive 2010/24/UE du 16 mars 2010. Le taux spécial du 1 bis du II bis, les soultes, l'exclusion d'imputation des moins-values latentes, les exceptions aux donations et l'ordre d'imputation de l'impôt étranger sont maintenus. Incohérence préexistante conservée : au second alinéa du 2 du IX, les renvois au « premier alinéa du présent IX » et au « formulaire mentionné au même premier alinéa » ne désignent pas clairement le même support, le formulaire étant introduit au premier alinéa du 2 et non au 1. Une correction de ces renvois nécessiterait une coordination expresse. Le VIII, 4 et le IX, 3 visent un paiement l'année suivant le transfert, tandis que d'autres restitutions visent un paiement immédiat lors du transfert : ces formulations distinctes sont préservées. Aucun alinéa cible n'est déplacé.",
    },
    "168": {
        "file": "168.xml",
        "reason": "Réécriture à droit constant du mécanisme d'évaluation forfaitaire et de l'intégralité du tableau : phrases distinctes pour le seuil et son indexation, formulation directe des exclusions et réductions, explicitation de la preuve ouverte au contribuable. Les douze catégories du barème, les trente lignes et leurs deux cellules, tous les montants, unités, âges, coefficients et conditions restent présents dans le même ordre. Aucune réforme de fond définie par policy.json ne modifie ce régime.",
        "review_notes": "Seuil de 54 299 € et indexation annuelle conservés sans recalcul ; disproportion d'au moins un tiers, revenus exonérés ou soumis à un régime proportionnel et droit à la preuve maintenus. Les cellules chiffrées du tableau ont été comparées ligne par ligne : valeurs locatives multipliées par cinq, demi-bases, abattements de 25 %, 50 % et 75 %, majorations par cinq, seuils et arrondis sont conservés. Ambiguïté préexistante non corrigée : les tranches de tonnage du 6 sont libellées « de 4 à 10 » et « de 10 à 25 », avec une borne de 10 commune. La note source rattache la modification à l'article 4-I B 1° a de la loi n° 2026-103 du 19 février 2026 ; elle ne fixe aucune date pour une réforme proposée. Les attributs de présentation du tableau sont retirés, sans suppression de ligne, de cellule ni de condition.",
    },
    "170": {
        "file": "170.xml",
        "reason": "Réécriture à droit constant des 1, 1 bis, 2, 3 et 4 : obligations déclaratives et calculs administratifs exprimés directement, maintien de toutes les plus-values, fractions de gain, revenus étrangers, exonérations, données familiales et mentions de l'avis d'imposition. Réforme de fond procédurale au nouveau 5 : application de la mesure « déclarer une fois, corriger à la source » par réemploi des informations légalement détenues et utilisables, mise à disposition pour vérification, correction ou complément, et suppression des nouvelles demandes de données déjà exactes, actuelles et suffisantes. L'obligation de souscrire, le dispositif de l'article 171, les secrets protégés et le contrôle fiscal sont préservés ; aucun barème, taux ou avantage fiscal n'est modifié.",
        "review_notes": "Les subdivisions et dix alinéas normatifs préexistants restent à leur place ; le nouveau 5 est ajouté après le 4. Coordination explicite avec le premier alinéa de l'article 171 et le nouveau 4° de l'article 172. La désignation du « premier alinéa » à la fin du 3 est explicitée comme visant le premier alinéa de ce même 3, où figure le calcul du revenu imposable. Pour la mise en œuvre du nouveau 5, coordonner les formulaires et textes réglementaires des déclarations, ainsi que les règles du livre des procédures fiscales relatives au secret, à la communication et au contrôle ; ce 5 ne crée pas une autorisation générale d'échange de données entre administrations. La note source renvoie au A du IV de l'article 24 de la loi n° 2026-103 du 19 février 2026 : application de la rédaction issue du I aux opérations qu'elle énumère à compter du 15 février 2025, avec l'exception du b du 1° du D pour les donations et dons manuels intervenus à compter du lendemain de la promulgation de cette loi. Ce régime temporel historique n'est pas étendu au nouveau 5 ; aucune date d'entrée en vigueur de la réforme n'est inventée.",
    },
    "170 bis": {
        "file": "170_bis.xml",
        "reason": "Réécriture à droit constant de l'obligation de déclaration indépendante du montant du revenu : sujet et obligation explicites, énumération plus lisible des biens détenus et formulation directe du dépassement de valeur locative. Les 1° à 4°, les qualifications des véhicules et résidences et les critères géographiques sont conservés. Aucune réforme de fond n'est appliquée à ces critères d'assujettissement.",
        "review_notes": "Seuils stricts de plus de 150 € à Paris et dans le rayon de 30 kilomètres, et de plus de 114 € ailleurs, conservés tels qu'ils figurent dans la source ; aucune actualisation monétaire implicite. Le renvoi à l'article L. 421-2 du code des impositions sur les biens et services et la destination exclusive au transport des personnes restent attachés au véhicule de tourisme. La note source rappelle l'entrée en vigueur au 1er janvier 2022 en application de l'article 40 de l'ordonnance n° 2021-1843 du 22 décembre 2021 : cette date historique n'est pas réutilisée pour les ajouts proposés aux autres articles. La coordination procédurale des articles 170 et 171 ne supprime aucun des cas d'assujettissement du présent article.",
    },
    "170 ter": {
        "file": "170_ter.xml",
        "reason": "Réécriture à droit constant de la mission de tiers de confiance : opérations confiées au professionnel formulées par des verbes directs, condition de présence des avantages sur la liste réglementaire rendue explicite, obligations de conservation et de transmission individualisées. Toutes les subdivisions I à VI et les cinq opérations numérotées sont maintenues. Les professions habilitées, le consentement contractuel du client, les conventions et leur résiliation sont préservés. La simplification administrative ne supprime pas les obligations de conservation propres à ce régime.",
        "review_notes": "Convention individuelle de trois ans, information des clients dans les trois mois suivant la résiliation et conservation jusqu'à l'extinction du délai de reprise conservées ; l'expression « expiration du délai de reprise » désigne ce même terme sans fixer de nouvelle durée. Maintien du renvoi à l'article 1649 quater B ter, de la convention nationale applicable jusqu'à dénonciation et de l'accord du client dans le contrat du I. Le réemploi de données proposé à l'article 170 ne vaut ni nouveau mandat du professionnel ni suppression de l'exemplaire de justificatifs conservé par le contribuable ; les contrats et conventions en cours ne sont pas révisés par cette réécriture. Aucun changement des pouvoirs de contrôle de l'administration.",
    },
    "171": {
        "file": "171.xml",
        "reason": "Réécriture du mécanisme de déclaration réputée souscrite en présentant directement les conditions auxquelles le contribuable doit satisfaire : mise à disposition du document dans le délai requis et absence de complément ou rectification avant la date limite. A droit constant, le délai, les prorogations et les cas d'exclusion définis par décret sont conservés. Réforme de fond par coordination avec le nouveau 5 de l'article 170 : le document est établi au moyen des informations légalement réutilisables et permet leur vérification, correction ou complément.",
        "review_notes": "Les deux alinéas sont maintenus dans leur ordre ; la coordination est ajoutée à la fin du premier et ne décale pas le second. Le délai demeure au plus tard un mois avant la date du premier alinéa de l'article 175, éventuellement prorogée selon ce même alinéa ; aucune date annuelle fixe n'est substituée à ce renvoi. L'absence de complément ou rectification demeure appréciée à la date limite de déclaration, et non à la date de mise à disposition du document. L'article 175 a été consulté dans le corpus public local pour vérifier le mécanisme de prorogation. Adapter le décret relatif aux cas d'exclusion et les modalités de correction à la coordination avec le 5 de l'article 170, sans présumer que tous les contribuables remplissent les conditions de la déclaration réputée souscrite.",
    },
    "172": {
        "file": "172.xml",
        "reason": "Réécriture à droit constant des obligations complémentaires de déclaration professionnelle : finalité du contrôle, catégories de bénéfices et époux tenu de souscrire exprimés directement ; 2° abrogé conservé. Réforme de fond procédurale au nouveau 4° : application aux renseignements et déclarations professionnelles de la règle de réemploi instituée au nouveau 5 de l'article 170. Les déclarations elles-mêmes et leurs champs fiscaux ne sont pas supprimés ni étendus.",
        "review_notes": "Les 1°, 2° et 3° restent dans le même ordre ; les sauts de ligne du XML source sont convertis en paragraphes sans fusion de subdivision. Nouveau 4° ajouté après le 3°. Renvois aux articles 53 A, 97 et 38 sexdecies Q de l'annexe III conservés et vérifiés dans le corpus public local : leurs champs propres, notamment les régimes réels et la déclaration contrôlée, demeurent applicables. L'article 53 A renvoie aussi aux délais de l'article 175, et l'article 38 sexdecies Q rattache les exploitants sous régime réel aux obligations de l'article 53 A ; aucun de ces renvois n'est remplacé par le nouveau dispositif. Le 3° conserve le renvoi rédigé « au 1 » dans la source, malgré la numérotation « 1° ». Coordonner les modèles et pièces prévus par les textes réglementaires d'application de ces déclarations avec le nouveau 5 de l'article 170 ; le nouveau 4° ne dispense ni de déclarer le résultat ni de répondre aux demandes de contrôle légalement nécessaires.",
    },
}

sources = json.loads((ROOT / "source.json").read_text())
answer = []
for source in sources:
    editorial = EDITORIAL[source["number"]]
    answer.append({
        **{
            key: source[key]
            for key in ("code_id", "source_id", "source_sha256", "number")
        },
        "proposed_xml": (FRAGMENTS / editorial["file"]).read_text().strip(),
        "reason": editorial["reason"],
        "review_notes": editorial["review_notes"],
        "status": "rewrite_draft",
    })

(ROOT / "answer.json").write_text(
    json.dumps(answer, ensure_ascii=False, indent=2) + "\n"
)
