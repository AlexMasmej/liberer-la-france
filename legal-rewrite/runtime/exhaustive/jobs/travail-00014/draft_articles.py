import json
from pathlib import Path


HISTORICAL_NOTE = (
    "La note source rappelle que l'article 30 de la loi n° 2011-893 du 28 juillet 2011 "
    "fixe au 1er novembre 2011 l'entrée en vigueur des articles 31 à 39 de cette loi "
    "et permet à un accord collectif national conclu avant cette date de déroger à ces articles. "
    "Cette disposition extérieure au texte codifié est conservée dans son champ historique ; "
    "elle n'est pas transformée en alinéa de l'article. Les accords antérieurs susceptibles "
    "d'en relever restent à identifier. Cette date n'est pas celle de la réforme proposée."
)


def paragraphs(*items):
    return "".join(f"<p>{item}</p>" for item in items)


drafts = {
    "L1252-6": (
        paragraphs(
            "Le salarié mis à disposition reçoit une rémunération au moins égale à celle d'un salarié qui, dans l'entreprise utilisatrice, possède un niveau de qualification professionnelle identique ou équivalent et occupe le même poste ou exerce les mêmes fonctions."
        ),
        "Réécriture à droit constant : la rémunération minimale est formulée comme un droit du salarié et les deux critères de comparaison sont explicités. Aucune réforme de fond ne vise cette garantie.",
        "Maintien du niveau de qualification identique ou équivalent et de l'alternative entre même poste et mêmes fonctions, dans l'entreprise utilisatrice. Aucun montant ni taux nouveau."
    ),
    "L1252-7": (
        paragraphs(
            "Pendant la mise à disposition, l'entreprise utilisatrice est responsable des conditions dans lesquelles le travail est exécuté. Ces conditions sont déterminées par les dispositions légales et conventionnelles applicables au lieu de travail."
        ),
        "Réécriture à droit constant : deux phrases distinguent la responsabilité de l'entreprise utilisatrice et les règles qui déterminent les conditions d'exécution du travail. Aucune modification de fond.",
        "Responsabilité maintenue pendant toute la mise à disposition, avec le double rattachement aux dispositions légales et conventionnelles du lieu de travail. Ne pas importer ici la liste limitative propre à L. 1253-12."
    ),
    "L1252-8": (
        paragraphs(
            "Dans l'entreprise utilisatrice, le salarié mis à disposition a accès aux moyens de transport collectifs et aux installations collectives, notamment de restauration, dont les salariés de cette entreprise peuvent bénéficier. Il y accède dans les mêmes conditions que ces salariés.",
            "Lorsque le comité social et économique supporte des dépenses supplémentaires, ces dépenses lui sont remboursées selon les modalités définies dans le contrat de mise à disposition."
        ),
        "Réécriture à droit constant : l'accès aux équipements et l'égalité de ses conditions sont énoncés séparément dans le premier alinéa ; le second précise l'objet du remboursement au comité social et économique. Aucune réforme de fond.",
        "Les transports, les installations collectives et l'exemple de la restauration sont maintenus. Le texte source ne désigne pas expressément le débiteur du remboursement : la proposition conserve cette limite et le renvoi aux modalités contractuelles, sans en inventer un."
    ),
    "L1252-9": (
        paragraphs(
            "Le contrat de travail à temps partagé est rompu selon les règles de rupture du contrat de travail à durée indéterminée prévues au titre III du présent livre."
        ),
        "Réécriture à droit constant : la phrase rattache directement la rupture au régime du contrat à durée indéterminée et précise le livre auquel appartient le titre III. Aucune réforme autonome de ce régime.",
        "Le caractère à durée indéterminée est confirmé par L. 1252-4 dans le corpus. Le renvoi au titre III est maintenu. Les réformes de L. 1233-3 et de L. 1234-9 et leurs coordinations s'appliquent selon leurs propres conditions et transitions ; cet article ne les étend pas aux contrats ou droits antérieurs."
    ),
    "L1252-10": (
        paragraphs(
            "Le contrat de mise à disposition établi pour chaque salarié indique les éléments suivants :",
            "1° Le contenu de la mission ;",
            "2° La durée estimée de la mission ;",
            "3° La qualification professionnelle du salarié ;",
            "4° Les caractéristiques particulières du poste de travail ou des fonctions occupées ;",
            "5° Le montant de la rémunération et ses différentes composantes."
        ),
        "Réécriture à droit constant du chapeau pour présenter directement les mentions que doit indiquer chaque contrat. Les cinq mentions, déjà précises, restent intégralement énumérées. Aucune réforme de fond.",
        "Numérotation 1° à 5° et ordre des alinéas conservés. La durée reste estimée ; le montant de la rémunération et chacune de ses composantes demeurent exigés. Aucun ajout de formalité."
    ),
    "L1252-11": (
        paragraphs(
            "Est réputée non écrite toute clause tendant à interdire à l'entreprise utilisatrice de recruter le salarié mis à disposition à l'issue de sa mission."
        ),
        "Réécriture à droit constant : la sanction est placée en tête et l'entreprise autorisée à recruter devient le sujet explicite du recrutement. Aucune modification de fond.",
        "Maintien de la sanction de clause réputée non écrite, de la formule couvrant toute clause tendant à interdire le recrutement et de la condition tenant à l'issue de la mission."
    ),
    "L1252-12": (
        paragraphs(
            "En matière de gestion des compétences et de la formation, l'entreprise de travail à temps partagé ne peut apporter des conseils qu'à ses entreprises utilisatrices."
        ),
        "Réécriture à droit constant : la phrase présente d'abord le domaine du conseil, puis exprime directement la limitation de ses bénéficiaires. Le conseil demeure une faculté ; aucune réforme de fond.",
        "Les conseils demeurent réservés aux seules entreprises utilisatrices de l'entreprise de travail à temps partagé et portent toujours sur la gestion des compétences et de la formation. Aucune ouverture à d'autres bénéficiaires."
    ),
    "L1252-13": (
        paragraphs(
            "L'entrepreneur de travail à temps partagé doit, à tout moment, justifier d'une garantie financière. En cas de défaillance de sa part, cette garantie assure le paiement :",
            "1° Des salaires et de leurs accessoires ;",
            "2° Des cotisations obligatoires dues à des organismes de sécurité sociale ou à des institutions sociales."
        ),
        "Réécriture à droit constant : le chapeau distingue l'obligation permanente de justification et la fonction de la garantie en cas de défaillance. Les deux catégories de paiements garantis restent identiques. Aucune réforme de fond.",
        "Maintien de l'exigence à tout moment, de la défaillance de l'entrepreneur, des accessoires du salaire et de l'alternative entre organismes de sécurité sociale et institutions sociales. Numérotation et alinéas conservés."
    ),
    "L1252-14": (
        paragraphs(
            "Si, à l'issue d'une mission, l'entreprise utilisatrice embauche un salarié qu'un entrepreneur de travail à temps partagé a mis à sa disposition, l'ancienneté de ce salarié tient compte de la durée des missions qu'il a accomplies dans cette entreprise au cours des trois mois précédant son recrutement.",
            "La période d'essai éventuellement prévue dans le nouveau contrat de travail est réduite de cette même durée."
        ),
        "Réécriture à droit constant : le premier alinéa rattache directement l'ancienneté du salarié à la durée des missions accomplies chez l'entreprise qui le recrute ; le second rattache expressément la réduction de l'essai à cette même durée. Aucune réforme de fond.",
        "La période rétrospective de trois mois et la prise en compte des seules missions dans l'entreprise qui recrute sont conservées. Ces trois mois ne constituent pas une durée d'essai. La réduction continue de s'appliquer à l'essai éventuellement prévu, avec les règles et transitions propres au nouveau contrat, notamment celles de L. 1221-19 à L. 1221-23 pour un CDI."
    ),
    "L1252-15": (
        paragraphs(
            "Par dérogation à l'article L. 1237-1, le salarié n'a pas à exécuter de préavis lorsqu'il prend l'initiative de rompre son contrat de travail à temps partagé en raison de son embauche par l'entreprise utilisatrice à l'issue d'une mission.",
            "Aucune indemnité compensatrice n'est due au titre de cette dispense de préavis."
        ),
        "Réécriture à droit constant : le salarié est le sujet de la rupture et la dispense de préavis est exprimée directement. Le second alinéa précise le lien entre cette dispense et l'absence d'indemnité compensatrice. Aucune réforme de fond.",
        "Renvoi à L. 1237-1 vérifié dans le corpus et conservé. La rupture doit rester à l'initiative du salarié et motivée par son embauche par l'entreprise utilisatrice à l'issue d'une mission. L'absence d'indemnité vise cette dispense et ne supprime pas d'autres créances."
    ),
    "L1253-1": (
        paragraphs(
            "Des personnes entrant dans le champ d'application d'une même convention collective peuvent constituer un groupement afin de mettre des salariés à la disposition de ses membres. Ces salariés sont liés au groupement par un contrat de travail. Leur mise à disposition peut avoir pour objet le remplacement de salariés suivant une action de formation prévue par le présent code.",
            "Le groupement peut également aider ou conseiller ses membres en matière d'emploi ou de gestion des ressources humaines.",
            "Un groupement peut être reconnu comme groupement d'employeurs pour l'insertion et la qualification lorsqu'il organise des parcours d'insertion et de qualification pour les salariés rencontrant des difficultés d'insertion qu'il met à la disposition de ses membres. Un décret fixe les conditions de cette reconnaissance.",
            "Les groupements visés au présent article ne peuvent effectuer que des opérations à but non lucratif."
        ),
        "Réécriture à droit constant : les phrases distinguent la constitution, le lien salarial et l'objet de la mise à disposition ; elles rendent explicites l'aide aux membres et la reconnaissance pour l'insertion et la qualification. Les quatre alinéas sont maintenus. Aucune réforme de fond.",
        "Maintien du champ d'une même convention collective, de la faculté de remplacement pour formation prévue par le code, des bénéficiaires et du décret de reconnaissance, ainsi que du caractère exclusivement non lucratif. L. 1253-17 conserve séparément le régime des personnes relevant de conventions différentes."
    ),
    "L1253-2": (
        paragraphs(
            "Un groupement d'employeurs doit être constitué sous l'une des formes suivantes :",
            "1° Association régie par la loi du 1er juillet 1901 relative au contrat d'association ;",
            "2° Société coopérative au sens de la loi n° 47-1775 du 10 septembre 1947 portant statut de la coopération et de la loi n° 83-657 du 20 juillet 1983 relative au développement de certaines activités d'économie sociale ;",
            "3° Association régie par le code civil local ou coopérative artisanale dans les départements de la Moselle, du Bas-Rhin et du Haut-Rhin."
        ),
        "Réécriture à droit constant du chapeau : l'obligation de choisir une forme autorisée est rendue explicite. Les dénominations légales et les trois formes sont conservées sans paraphrase susceptible d'en modifier le champ. Aucune réforme de fond.",
        "Contrôle des références conservées : 1er juillet 1901 ; loi n° 47-1775 du 10 septembre 1947 ; loi n° 83-657 du 20 juillet 1983. Les deux formes locales et les trois départements restent au 3°. Ces références extérieures au corpus des cinq codes ne sont pas actualisées."
    ),
    "L1253-3": (
        paragraphs(
            "Sont également considérées comme des groupements d'employeurs les structures suivantes :",
            "1° Les sociétés coopératives existantes qui développent, au bénéfice exclusif de leurs membres, les activités mentionnées à l'article L. 1253-1 ;",
            "2° Les sociétés interprofessionnelles de soins ambulatoires mentionnées à l'article L. 4041-1 du code de la santé publique qui emploient des salariés dans les conditions prévues au a du 3° de l'article L. 4041-2 du même code et développent les activités mentionnées à l'article L. 1253-1 du présent code au bénéfice exclusif de tout ou partie de leurs associés.",
            "Un décret en Conseil d'Etat détermine les conditions dans lesquelles le présent chapitre s'applique à ces structures."
        ),
        "Réécriture à droit constant : le 2° rattache clairement à ces sociétés les conditions cumulatives d'emploi de salariés et d'activité au bénéfice de leurs associés. Le renvoi réglementaire est formulé avec un sujet explicite. Aucune réforme de fond.",
        "Les 1° et 2° et les alinéas logiques matérialisés par les sauts de ligne de la source sont préservés. Maintien du bénéfice exclusif des membres au 1°, de tout ou partie des associés au 2° et du décret en Conseil d'Etat. Renvois externes à L. 4041-1 et au a du 3° de L. 4041-2 du code de la santé publique conservés, à contrôler dans ce code hors corpus fourni."
    ),
    "L1253-6": (
        paragraphs(
            "Le groupement tient en permanence, à son siège, la liste de ses membres à la disposition de l'agent de contrôle de l'inspection du travail mentionné à l'article L. 8112-1."
        ),
        "Réécriture à droit constant : le groupement devient le sujet explicite de l'obligation de mise à disposition de la liste. Aucune réforme de fond.",
        "Le caractère permanent, le siège du groupement et le renvoi à l'agent de contrôle de L. 8112-1 sont conservés ; ce renvoi a été vérifié dans le corpus. Aucun délai nouveau ni formalité d'envoi n'est ajouté."
    ),
    "L1253-7": (
        paragraphs(
            "Tout employeur qui adhère à un groupement d'employeurs informe les institutions représentatives du personnel existant dans son entreprise de la constitution du groupement et de sa nature."
        ),
        "Réécriture à droit constant : l'obligation est énoncée pour chaque employeur adhérent et les deux objets de l'information sont rattachés au même groupement. Aucune réforme de fond.",
        "La formulation générique de la source sur les institutions représentatives du personnel est maintenue. Aucun nouvel organe, délai, avis préalable ou condition d'adhésion n'est introduit."
    ),
    "L1253-8": (
        paragraphs(
            "Les membres du groupement sont solidairement responsables des dettes de celui-ci envers les salariés et les organismes créanciers de cotisations obligatoires. Par dérogation à cette solidarité, les statuts d'un groupement d'employeurs peuvent fixer, à partir de critères objectifs, des règles de répartition de ces dettes entre ses membres ; ces règles sont opposables aux créanciers. Les statuts peuvent également prévoir des modalités particulières de responsabilité pour les collectivités territoriales membres du groupement."
        ),
        "Réécriture à droit constant : les dettes sont rattachées explicitement au groupement, le principe de solidarité est distingué de la dérogation statutaire et l'opposabilité aux créanciers est énoncée directement. L'alinéa unique est conservé. Aucune réforme de fond.",
        "La solidarité, les critères objectifs, l'opposabilité et la faculté particulière relative aux collectivités territoriales sont maintenus. " + HISTORICAL_NOTE
    ),
    "L1253-8-1": (
        paragraphs(
            "Pour calculer l'effectif d'un groupement d'employeurs en application du présent code, les salariés que ce groupement met, en tout ou partie, à la disposition d'un ou de plusieurs de ses membres ne sont pas comptabilisés. Cette exclusion ne s'applique pas à la deuxième partie du présent code."
        ),
        "Réécriture à droit constant : la règle de calcul de l'effectif est énoncée avant son exception, rendue explicite dans une seconde phrase du même alinéa. Aucune réforme de fond.",
        "Maintien des mises à disposition totales ou partielles et auprès d'un ou de plusieurs membres. L'exception relative à la deuxième partie réserve ses règles propres sans créer une règle nouvelle de décompte. Aucun changement de seuil d'effectif."
    ),
    "L1253-8-2": (
        paragraphs(
            "En cas d'ouverture d'une procédure de sauvegarde, de redressement ou de liquidation judiciaire à l'égard d'une entreprise membre d'un groupement d'employeurs mentionné aux articles L. 1253-1 et L. 1253-17, les créances de ce groupement sur cette entreprise bénéficient des garanties suivantes :",
            "1° La part des créances correspondant à la facturation des sommes dues aux salariés mis à la disposition de l'entreprise bénéficie de privilèges identiques à ceux qui garantissent les créances des salariés, dans les conditions prévues au 3° de l'article 2331 et au 2° de l'article 2377 du code civil et aux articles L. 3253-2 et L. 3253-4 du présent code ;",
            "2° La part des créances correspondant à la facturation des charges sociales dues au titre des salariés mis à la disposition de l'entreprise bénéficie d'un privilège identique à celui qui garantit les créances des organismes de sécurité sociale, dans les conditions prévues à l'article L. 243-4 du code de la sécurité sociale."
        ),
        "Réécriture à droit constant : le chapeau expose d'abord l'ouverture de la procédure, puis chaque subdivision désigne la fraction de créance et le privilège qui la garantit. Les deux assiettes et tous les renvois restent distincts. Aucune réforme de fond.",
        "Les trois procédures et les subdivisions 1° et 2° sont conservées. L. 1253-1, L. 1253-17, L. 3253-2, L. 3253-4 et L. 243-4 du code de la sécurité sociale ont été lus dans le corpus. Les renvois au 3° de l'article 2331 et au 2° de l'article 2377 du code civil restent à contrôler hors corpus fourni ; ils ne sont ni remplacés ni complétés. Les conditions, rangs et plafonds résultant des textes visés ne sont pas rendus inconditionnels."
    ),
    "L1253-9": (
        paragraphs(
            "Le groupement établit par écrit les contrats de travail qu'il conclut. Ces contrats mentionnent notamment :",
            "1° Les conditions d'emploi et de rémunération ;",
            "2° La qualification professionnelle du salarié ;",
            "3° La liste des utilisateurs potentiels ;",
            "4° Les lieux d'exécution du travail.",
            "Ces contrats garantissent au salarié du groupement, par rapport aux salariés des entreprises auprès desquelles il est mis à disposition, l'égalité de traitement en matière de rémunération, d'intéressement, de participation et d'épargne salariale."
        ),
        "Réécriture à droit constant : le groupement est désigné comme responsable de l'écrit et le dernier alinéa rend explicites le bénéficiaire et les salariés de comparaison pour l'égalité de traitement. Les quatre mentions contractuelles restent intactes. Aucune réforme de fond.",
        "Numérotation, ordre des mentions, caractère non exhaustif introduit par « notamment » et quatre domaines d'égalité conservés. Aucun plancher de temps partiel ou nouveau volume de travail n'est ajouté à ce régime. " + HISTORICAL_NOTE
    ),
    "L1253-10": (
        paragraphs(
            "Le groupement fait bénéficier ses salariés de la convention collective dans le champ d'application de laquelle il a été constitué."
        ),
        "Réécriture à droit constant : le groupement devient le sujet de l'obligation correspondant au bénéfice reconnu à ses salariés. Le critère de rattachement conventionnel reste identique. Aucune réforme de fond.",
        "La convention reste celle dans le champ de laquelle le groupement a été constitué ; la proposition ne lui substitue ni la convention de chaque utilisateur ni un accord d'entreprise."
    ),
    "L1253-11": (
        paragraphs(
            "Les organisations professionnelles représentant les groupements d'employeurs peuvent conclure des accords collectifs de travail avec les organisations syndicales de salariés représentatives. Ces accords sont conclus sans préjudice des conventions de branche ou des accords professionnels applicables aux groupements d'employeurs."
        ),
        "Réécriture à droit constant : une première phrase identifie les parties habilitées à négocier et une seconde maintient la réserve des conventions de branche et accords professionnels. Les deux phrases restent dans le même alinéa. Aucune réforme de fond.",
        "La représentativité exigée des organisations syndicales de salariés est conservée, sans ajouter de condition aux organisations professionnelles autre que la représentation des groupements. La place accrue des accords d'entreprise prévue par le programme ne modifie pas ici les accords propres aux groupements. " + HISTORICAL_NOTE
    ),
    "L1253-12": (
        paragraphs(
            "Pendant la mise à disposition, l'utilisateur est responsable des conditions dans lesquelles le travail est exécuté, telles que les fixent les dispositions légales et conventionnelles applicables au lieu de travail.",
            "Pour l'application de ces dispositions, seules les matières suivantes relèvent des conditions d'exécution du travail :",
            "1° La durée du travail ;",
            "2° Le travail de nuit ;",
            "3° Le repos hebdomadaire et les jours fériés ;",
            "4° La santé et la sécurité au travail ;",
            "5° Le travail des femmes, des enfants et des jeunes travailleurs ;",
            "6° L'exercice de la fonction de maître d'apprentissage, définie à la section 3 du chapitre III du titre II du livre II de la sixième partie."
        ),
        "Réécriture à droit constant : le premier alinéa relie directement les conditions d'exécution aux règles du lieu de travail ; le deuxième exprime clairement le caractère limitatif des six matières. Les subdivisions sont intégralement conservées. Aucune réforme de fond.",
        "Les six matières et le renvoi structurel du 6° sont maintenus. L. 6223-5 confirme dans le corpus la fonction de maître d'apprentissage et son appréciation au niveau de l'entreprise utilisatrice pour les apprentis des groupements. La mention de la durée du travail ne modifie ni les seuils ni les transitions propres aux nouveaux contrats. " + HISTORICAL_NOTE
    ),
    "L1253-13": (
        paragraphs(
            "Le groupement assume les obligations relatives à la médecine du travail.",
            "L'utilisateur assume toutefois les obligations correspondant à la surveillance médicale renforcée lorsque l'activité du salarié mis à disposition nécessite une telle surveillance au sens de la réglementation relative à la médecine du travail."
        ),
        "Réécriture à droit constant : les deux responsables sont placés au début de leur alinéa et la seconde phrase présente expressément l'exception au principe. Le critère réglementaire demeure inchangé. Aucune réforme de fond.",
        "Décalage terminologique préexistant : la source emploie « surveillance médicale renforcée », tandis que L. 4624-2 du corpus organise un « suivi individuel renforcé » ; R. 4624-23 en précise les postes à risques. La proposition conserve la qualification de la source et le partage des obligations. Une coordination expresse de ces régimes nécessiterait de vérifier leur champ respectif ; aucune équivalence automatique ni correction silencieuse n'est opérée."
    ),
    "L1253-14": (
        paragraphs(
            "Dans l'entreprise utilisatrice, les salariés du groupement bénéficient du même accès que les salariés de cette entreprise aux moyens collectifs de transport et aux installations collectives, notamment de restauration."
        ),
        "Réécriture à droit constant : le lieu d'accès est indiqué d'abord et la garantie est formulée directement comme une égalité d'accès aux équipements collectifs. Aucune réforme de fond.",
        "Les salariés du groupement, les salariés de comparaison, les transports collectifs et les installations collectives, notamment de restauration, restent couverts dans les mêmes conditions. Ne pas ajouter ici le remboursement au comité social et économique prévu par le régime distinct de L. 1252-8."
    ),
}


def main():
    sources = json.loads(Path("source.json").read_text())
    assert len(sources) == 24
    assert set(drafts) == {source["number"] for source in sources}
    answer = []
    for source in sources:
        proposed, reason, notes = drafts[source["number"]]
        row = {
            key: source[key]
            for key in ("code_id", "source_id", "source_sha256", "number")
        }
        row.update(
            proposed_xml=proposed,
            reason=reason,
            review_notes=notes,
            status="rewrite_draft",
        )
        answer.append(row)
    Path("answer.json").write_text(
        json.dumps(answer, ensure_ascii=False, indent=2) + "\n"
    )


if __name__ == "__main__":
    main()
