import json
from pathlib import Path


METADATA = {
    "199 decies E": {
        "files": ["proposed-199-decies-E.xml"],
        "reason": (
            "Réécriture à droit constant : les conditions d'acquisition et de localisation, "
            "le calcul puis l'imputation de la réduction, les engagements du propriétaire et "
            "de l'exploitant, les reprises et l'exception au décès sont exprimés en phrases "
            "distinctes avec des sujets explicites. Les huit alinéas restent à leur place. "
            "Aucune réforme de fond : policy.json prévoit un réexamen des niches sans définir "
            "de suppression ni de nouveaux paramètres pour ce régime historique."
        ),
        "review_notes": (
            "Coordination conservée avec 199 decies EA, qui vise les premier et troisième "
            "alinéas et le délai de location, et 199 decies G, qui vise le cinquième alinéa : "
            "aucun de ces alinéas n'est déplacé. Sont maintenus les acquisitions du 1er janvier "
            "1999 au 31 décembre 2010, l'achèvement au plus tard le 1er juillet 2025, les bases "
            "de 50 000 et 100 000 €, le taux de 25 %, les limites de 12 500 et 25 000 €, "
            "le seuil d'agglomération strictement supérieur à 5 000 habitants et les références "
            "européenne et législative historiques. Au cinquième alinéa : engagement d'au moins "
            "neuf ans, prise d'effet dans le mois, rupture supérieure à douze mois dans les cas "
            "énumérés, reprise par tiers pendant trois années, remplacement du gestionnaire "
            "après un an et avec au moins 50 % des appartements, occupation personnelle "
            "n'excédant pas huit semaines et déclaration du loyer annuel sans cette occupation. "
            "Deux ambiguïtés préexistantes sont conservées et nécessitent une clarification "
            "normative : la répartition sur six années au maximum coexiste avec l'option "
            "d'imputer le solde par sixième durant les six années suivantes ; une proportion "
            "du parc immobilier est comparée à un nombre de salariés, sans unité commune. "
            "Le renvoi au 5 du I de 197 a été vérifié dans le corpus : imputation avant crédits "
            "et prélèvements non libératoires, sans remboursement. L'exception au décès reste "
            "réservée au conjoint survivant d'époux imposés en commun."
        ),
    },
    "199 decies EA": {
        "files": ["proposed-199-decies-EA.xml"],
        "reason": (
            "Réécriture à droit constant : la condition d'ancienneté du logement, la dérogation "
            "géographique, la composition et le plafonnement de la base, les exclusions de "
            "déduction, les étapes de l'imputation et l'obligation de réservation aux saisonniers "
            "sont explicitées dans les cinq alinéas d'origine. Aucune réforme de fond n'est "
            "définie pour ce régime par policy.json ; ses droits et conditions historiques "
            "sont conservés."
        ),
        "review_notes": (
            "Renvois aux premier et troisième alinéas de 199 decies E et à son délai de "
            "location maintenus sans déplacement de leurs cibles. L'articulation de ce délai, "
            "qui vise l'achèvement de l'immeuble ou son acquisition postérieure, avec les "
            "travaux de réhabilitation n'est pas réinterprétée. Conditions et chiffres "
            "conservés : logement achevé depuis au moins quinze ans, prix de revient augmenté "
            "des travaux définis par décret, bases de 50 000 et 100 000 €, taux de 20 %, "
            "imputation initiale au sixième des limites de 10 000 ou 20 000 €, solde sur les "
            "cinq années suivantes ou, sur demande, par sixième durant les six années "
            "suivantes, travaux achevés dans les deux années suivant l'acquisition et au moins "
            "15 % de logements réservés aux salariés saisonniers. L'option d'étalement du "
            "solde appelle la même clarification que le deuxième alinéa de 199 decies E "
            "sur la durée maximale. La renonciation à la déduction des dépenses, y compris "
            "sous forme d'amortissement, et l'exclusion de l'article 32 restent distinctes. "
            "Le renvoi au code du tourisme est conservé ; ce code n'est pas présent dans "
            "le corpus fourni pour vérification. Le taux de 20 % demeure celui de cette "
            "réduction, indépendamment de la réforme du taux normal de l'IS."
        ),
    },
    "199 decies G": {
        "files": ["proposed-199-decies-G.xml"],
        "reason": (
            "Réécriture à droit constant : le cas de la société non soumise à l'impôt sur "
            "les sociétés est posé en tête, l'engagement du porteur de parts est explicite "
            "et l'exception au décès est présentée en deux phrases. Le texte forme toujours "
            "un seul alinéa, désormais balisé par p au lieu de sauts de ligne. Aucune réforme "
            "de fond : les réductions historiques et leur régime de conservation des titres "
            "ne sont pas modifiés par les orientations fournies."
        ),
        "review_notes": (
            "Renvois aux articles 199 decies E et 199 decies EA conservés. Le cinquième "
            "alinéa de 199 decies E contient toujours le délai de neuf ans : aucun déplacement "
            "de la cible ni changement du point d'expiration. Le porteur doit conserver "
            "la totalité de ses titres, non une fraction de ceux-ci. La rédaction de la "
            "source exclut les revenus des titres dont la propriété est démembrée, alors "
            "que l'avantage porte sur l'investissement : cette formulation est conservée "
            "sans la remplacer silencieusement par une exclusion des titres eux-mêmes ; "
            "sa portée mérite clarification. Le conjoint survivant attributaire ou "
            "usufruitier ne peut reprendre le bénéfice que pour la période restant à courir "
            "au décès et dans les mêmes conditions et modalités. Aucun assujettissement "
            "nouveau de ces sociétés à l'IS n'est introduit."
        ),
    },
    "199 decies I": {
        "files": ["proposed-199-decies-I.xml"],
        "reason": (
            "Réécriture à droit constant : les bénéficiaires et les opérations éligibles "
            "sont formulés directement, puis la base, le calendrier d'imputation, "
            "l'engagement locatif, les reprises et le non-cumul sont clarifiés. Les "
            "subdivisions I à VIII, leurs 1° et 2° et les treize alinéas sont maintenus. "
            "Aucune réforme de fond : ni la réduction propre aux résidences hôtelières "
            "à vocation sociale ni ses engagements anciens ne sont modifiés par policy.json."
        ),
        "review_notes": (
            "Conservation des acquisitions du 1er janvier 2007 au 31 décembre 2010, "
            "du domicile fiscal au sens de 4 B, des logements neufs ou en l'état futur "
            "d'achèvement et des logements à rénover, des bases de 50 000 et 100 000 €, "
            "du taux de 25 % et des limites de 12 500 ou 25 000 € imputées par sixième "
            "sur six années au maximum. Le plafond de 100 000 € conserve la mention "
            "des époux et partenaires de PACS soumis à une imposition commune, sans "
            "modifier les catégories propres à 199 decies E ou EA. Le III distingue "
            "toujours l'achèvement ou l'acquisition postérieure de la réception des travaux. "
            "Sont maintenus le bail nu d'au moins neuf ans, sa prise d'effet dans les "
            "six mois, la reprise l'année de la rupture ou de la cession, l'exclusion "
            "du démembrement et l'exception au décès d'un époux, le non-cumul pour un "
            "même contribuable et l'échéance du 1er juillet 2025. Les renvois aux articles "
            "L. 631-11 et L. 262-1 du CCH et au 5 du I de 197 ont été vérifiés dans "
            "le corpus. Le délai locatif de six mois est celui de ce régime distinct ; "
            "le délai d'un mois de 199 decies E ne lui est pas substitué."
        ),
    },
    "199 undecies A": {
        "files": ["proposed-199-undecies-A-part1.xml", "proposed-199-undecies-A-part2.xml"],
        "reason": (
            "Réécriture à droit constant de l'intégralité de l'article : le champ territorial "
            "et les deux périodes d'investissement sont distingués, les conditions des a "
            "à g du 2 ont des sujets explicites et les longues énumérations des engagements "
            "et reprises sont ponctuées en propositions plus lisibles. Les trente-neuf "
            "alinéas, le h abrogé, les subdivisions 1 à 9, 3 bis et 6 bis et les rangs "
            "d'alinéas du 6 sont conservés. Aucune réforme de fond : le réexamen des niches "
            "prévu dans policy.json ne définit pas de modification chiffrée ou de suppression "
            "de ces avantages. Les régimes transitoires de 2011 et 2012 restent intégralement "
            "rédigés, sans application rétroactive d'une réforme générale de l'IS."
        ),
        "review_notes": (
            "Tous les territoires et les périodes du 1 sont conservés : début à la date "
            "de promulgation de la loi n° 2003-660 du 21 juillet 2003, fin au 31 décembre "
            "2017 pour les a à d, f et g du 2 et au 31 décembre 2029 pour le e. La note "
            "source relative à l'article 58-I-1 de la loi n° 2004-1485 du 30 décembre 2004 "
            "est historique et n'est pas transformée en date d'entrée en vigueur future. "
            "Sont maintenus les 50 à 150 mètres carrés, les 90 % de superficie, les "
            "engagements et délais de cinq ans, six mois, deux ans et douze mois propres "
            "aux différentes opérations, les logements de plus de vingt ans au e, "
            "la durée normale d'utilisation plus courte au f, les souscriptions agréées "
            "du g, la rétrocession équivalente à 60 %, l'agrément préalable au-delà "
            "de deux millions d'euros et le plafond de 3 295 € HT par mètre carré "
            "avec sa formule d'indexation et ses dates du 1er janvier et du 1er novembre. "
            "La base annuelle reste de 10 % sur dix années au a et de 20 % sur cinq "
            "années pour les autres opérations, calculée sur les sommes payées au "
            "31 décembre de l'année de naissance du droit. Taux du 6 conservés : "
            "18 %, 30 %, 38 % ; majorations de quartier prioritaire à 26 %, 38 %, "
            "45 % ; d'énergie renouvelable à 22 %, 33 %, 40 % ; cumul à 29 %, "
            "40 %, 48 %. Les quatrième, septième et huitième alinéas du 6 gardent "
            "leurs places et leurs cibles ; les six ans de location et de conservation "
            "et les plafonds de loyer et de ressources demeurent cumulatifs. Le 6 bis "
            "maintient l'exclusion après le 31 décembre 2010 et ses exceptions : en "
            "2011, taux de 22 % ou 34 %, puis 30 %/41 %, 25 %/37 % ou 33 %/45 % "
            "selon les conditions ; en 2012, 26 % avec les deux conditions du 6. "
            "La délivrance du permis définit toujours l'engagement et le délai de "
            "location de trente-six mois, prorogeable pour force majeure ou contentieux "
            "de légalité. Reprises, exceptions d'apport partiel d'actif ou de fusion "
            "sous 210 B ou 210 A avec engagements pour le reliquat du délai, décès, "
            "location à un organisme pour son personnel, remboursement dans les cinq "
            "ans, exception de sinistre et non-cumul des déductions sont maintenus. "
            "Points préexistants nécessitant coordination ou clarification : le 3 bis "
            "vise le chapitre Ier du titre Ier du livre V du CCH, alors que L. 511-2 "
            "est classé dans un chapitre unique dans le corpus ; ce renvoi est conservé "
            "sans correction silencieuse. Le troisième alinéa du I de 244 quater J "
            "contient bien la condition de première propriété. La juxtaposition des "
            "travaux de réhabilitation et des travaux de confortation au e ne précise "
            "pas expressément l'articulation de toutes leurs conditions : aucune "
            "condition nouvelle propre à la confortation n'est ajoutée. Les échéances "
            "historiques et les conditions survivantes ne sont pas supprimées du seul "
            "fait qu'elles sont antérieures à la rédaction."
        ),
    },
}


def main():
    sources = json.loads(Path("source.json").read_text(encoding="utf-8"))
    assert len(sources) == 5
    assert {s["number"] for s in sources} == set(METADATA)
    answers = []
    for source in sources:
        metadata = METADATA[source["number"]]
        answer = {key: source[key] for key in ("code_id", "source_id", "source_sha256", "number")}
        answer.update(
            proposed_xml="\n".join(Path(p).read_text(encoding="utf-8").strip() for p in metadata["files"]),
            reason=metadata["reason"],
            review_notes=metadata["review_notes"],
            status="rewrite_draft",
        )
        answers.append(answer)
    Path("answer.json").write_text(json.dumps(answers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
