import json
from pathlib import Path


metadata = [
    (
        "Réécriture à droit constant : le calendrier de dépôt et l'auteur des obligations sont explicités ; les listes de pièces sont reformulées et les phrases longues sur les travaux, les prorogations et les changements de locataire sont scindées. Les trois périodes d'investissement et leurs exclusions propres restent distinctes. Aucune réforme de fond de la réduction d'impôt n'est introduite.",
        "Conserver l'articulation avec l'article 199 novovicies du CGI et les articles 46 AZA duodecies à quaterdecies. Les bornes du 1er septembre 2014, du 31 décembre 2014 et du 1er janvier 2015, les engagements de neuf ans ou de six ou neuf ans, les deux prorogations triennales et l'avis fiscal de l'avant-dernière année sont préservés. Les pièces propres à chacun des a à g du 4° sont maintenues, notamment la réception en mairie qui reste exigée au e malgré l'exception portant sur la copie de la déclaration. Le corpus indique une abrogation différée de l'article 199 novovicies : les obligations attachées aux investissements et engagements antérieurs ne sont pas supprimées. Les renvois au code de la santé publique sont conservés sans vérification externe, conformément au périmètre de lecture autorisé."
    ),
    (
        "Réécriture à droit constant : les deux loyers à prendre en compte sont identifiés et les conditions cumulatives d'exclusion de la redevance sont rendues plus lisibles. Le dépôt initial, les prorogations, le dépôt différé et le changement de locataire ou de sous-locataire sont exprimés avec un contribuable explicitement tenu de produire les pièces. Aucun plafond ni régime fiscal n'est modifié.",
        "Les renvois aux 1 et 2 du I bis de l'article 46 AZA undecies restent utilisables. Sont conservés le minimum de dix logements, l'indépendance de l'organisme bénéficiaire de la redevance, l'ensemble des frais concernés et le plafond annuel égal aux loyers du sous-locataire. Le d du 3° du I vise un avis d'impôt sur le revenu, tandis que le c final vise expressément l'imposition ou la non-imposition : cette différence de la source n'est pas uniformisée. La prorogation reste réservée aux investissements réalisés à compter du 1er septembre 2014."
    ),
    (
        "Réécriture à droit constant : la société propriétaire est désignée comme responsable du dépôt et de l'envoi aux associés ; le contenu du relevé et les opérations d'inscription des parts sont présentés en phrases plus courtes. Les obligations de la société, de chaque associé et du conjoint survivant restent séparées, sans modification du régime fiscal.",
        "Le champ exclut toujours les sociétés civiles de placement immobilier. Les trois périodes d'investissement, les exclusions de locataires et les durées de neuf ans ou de six ou neuf ans sont maintenues. Contrôler conjointement les articles 46 AZA undecies, duodecies et 199 novovicies : échéance au deuxième jour ouvré après le 1er mai, situation des parts au 1er janvier et au 31 décembre, inscription dans les trente jours, conservation jusqu'à la fin de la troisième année suivant l'expiration de l'engagement. Le double exemplaire destiné aux associés et l'exemplaire joint au résultat sont maintenus ; ces obligations ont des destinataires distincts de la double remise administrative supprimée aux articles 46 B et 46 C."
    ),
    (
        "Réécriture à droit constant : l'inscription des parts et son délai sont distingués au sein du même alinéa ; la société civile de placement immobilier est le sujet explicite des obligations d'envoi et de dépôt. Les huit rubriques du relevé sont conservées et la base d'appréciation des 95 % est exprimée hors frais de collecte. Aucune réforme de fond n'est apportée.",
        "Conserver les renvois au C et au A du VIII de l'article 199 novovicies et aux articles 2 terdecies D et 2 terdecies F. Le délai de trente jours, la fin de la troisième année de conservation documentaire, le deuxième jour ouvré suivant le 1er mai, les 95 % et l'investissement intégral dans les dix-huit mois sont maintenus. L'avis fiscal demeure celui de l'avant-dernière année précédant la signature du contrat. Les parts ou actions, les modalités de calcul et la prorogation éventuelle de l'engagement restent expressément couvertes."
    ),
    (
        "Réécriture à droit constant : le premier dépôt, la location par un organisme, les obligations des associés personnes physiques et les dépôts ultérieurs sont formulés avec des sujets explicites. Le report de production est isolé du renouvellement du bail. Aucun avantage ni condition de location n'est modifié ; le renvoi défectueux du III est maintenu et signalé.",
        "Incohérence préexistante : le III vise les documents « aux 2° et 3° du I et du 1 du II », alors que le 1 du II est subdivisé en a, b et c. Le libellé de ce renvoi est conservé ; une correction expresse devra préciser s'il vise les b et c de ce 1. La répartition des obligations entre société et associés doit rester coordonnée avec les articles 46 AZA sexdecies et septdecies et le B du I de l'article 199 tricies. L'année de référence de l'avis fiscal au c du 1 du II reste liée à la première année ouvrant droit à la réduction, et non à la signature de la sous-location. La note relative à l'article 2-2° du décret n° 2022-465 du 31 mars 2022 est historique et ne fixe aucune entrée en vigueur future."
    ),
    (
        "Réécriture à droit constant : les blocs séparés par des sauts de ligne sont présentés en alinéas, sans changer les subdivisions I et II ni la numérotation 1° à 8°. Les actions de joindre la convention, d'adresser le relevé et de déclarer une reprise sont attribuées explicitement à la société ou à l'associé. Le régime de réduction d'impôt n'est pas réformé.",
        "Maintenir la coordination avec les articles 46 AZA quindecies et septdecies et le B du I de l'article 199 tricies. La convention signée par les deux parties reste jointe au résultat de l'année de prise d'effet de la location ; le relevé porte sur l'année précédente et parvient aux associés au plus tard le deuxième jour ouvré suivant le 1er mai. Les revenus bruts du 3°, le revenu net et les frais et charges du 6° ne sont pas confondus. Les renvois aux articles 2 terdecies H et 2 terdecies I, la sous-location et l'occupation sont conservés."
    ),
    (
        "Réécriture à droit constant : le délai d'inscription des parts est exprimé dans une phrase distincte, au sein du II, et l'obligation annuelle de chaque associé est formulée directement. Les subdivisions et le moment où l'engagement de conservation est constaté sont maintenus. Aucune réforme de fond n'est introduite.",
        "Le renvoi au 1° du B du I de l'article 199 tricies et celui au II de l'article 46 AZA sexdecies sont conservés. L'inscription intervient dans les trente jours suivant la date limite de dépôt de la déclaration de la première année ouvrant droit à la réduction. L'alternative entre compte nominatif dans la comptabilité et registre spécial et la conservation documentaire jusqu'à la fin de la troisième année suivant l'expiration de l'engagement demeurent."
    ),
    (
        "Réécriture à droit constant : les trois cas permettant de satisfaire la condition d'exposition sont exprimés directement, et les conditions de dépôt et de convention sont clarifiées. Les dérogations à l'exposition continue restent attachées à chacun de leurs cas propres. Aucune réforme de fond du régime des monuments historiques n'est introduite.",
        "Les subdivisions 1° à 3° et a à c sont conservées, de même que la période minimale de cinq années. Au 1°, les restrictions à l'exposition doivent être prescrites par les services de l'Etat ; au 2°, l'objet doit rester confié à l'organisme ; au 3°, la convention peut autoriser une exposition discontinue si le dépôt dure jusqu'au terme requis. Les quatre domaines publics et les catégories de musées, bibliothèques et archives sont intégralement conservés. Les renvois au 2° du II de l'article 199 duovicies et à l'article 41 I sont maintenus ; le renvoi au code du patrimoine n'a pas fait l'objet d'une recherche externe."
    ),
    (
        "Réécriture à droit constant : les listes de mentions et de justificatifs sont allégées sur le plan syntaxique, et les obligations du propriétaire, de la société, des associés et du conjoint survivant sont exprimées séparément. Toutes les subdivisions I à V, les exceptions de production antérieure et les attestations chiffrées sont maintenues. Aucune réforme de fond ni actualisation silencieuse du champ patrimonial n'est effectuée.",
        "Incohérences préexistantes à coordonner expressément avec l'article 199 tervicies : le b du 1 du I de cet article réglementaire conserve les anciennes catégories de secteurs sauvegardés, ZPPAUP et AVAP, alors que le I législatif du corpus vise notamment les sites patrimoniaux remarquables ; le 5° du IV réglementaire vise les dépenses au I législatif, tandis que le IV bis législatif renvoie aux dépenses du II. Ces références de la source sont conservées pour ne pas modifier sans transition les opérations anciennes. Contrôler la coordination en fonction de la date de chaque opération. Les engagements de neuf ans, la reprise par le conjoint pour la seule période restante, le délai de trente jours, la conservation jusqu'à la fin de la troisième année, les dix-huit mois et les seuils minimaux de 65 % et 30 % calculés hors frais de collecte restent inchangés. Le 4° du IV conserve sa précision propre sur l'année précédente ; elle n'est pas ajoutée ailleurs."
    ),
    (
        "Réécriture à droit constant : le calcul de l'avantage et la détermination de sa base sont énoncés en deux phrases, puis la limitation en présence d'un déficit foncier est formulée directement. L'ordre des termes de la différence et les renvois de calcul restent ceux de la source ; aucune réforme de fond du plafonnement n'est appliquée.",
        "Point de contrôle préexistant : la source définit une différence entre le résultat net foncier déclaré et le résultat reconstitué sans amortissement, sans préciser ici son sens arithmétique ou sa valeur positive. Aucun ordre inverse ni valeur absolue n'a été introduit. Conserver les h et l du 1° du I de l'article 31, l'article 31 bis, le 1 du I de l'article 197 et l'alternative entre les deuxième et troisième alinéas du 3° du I de l'article 156. La note sur l'article 118-I-3° a et III de la loi n° 2015-1785 du 29 décembre 2015 reste une indication historique."
    ),
    (
        "Réécriture à droit constant : l'option du contribuable pour une base moyenne ou fractionnée et le montant à retenir sont explicités. Pour les revenus au quotient, la prise en compte avant multiplication de la cotisation supplémentaire est formulée dans une phrase distincte du même 2°. Aucune limite ni méthode d'imposition n'est modifiée.",
        "Maintenir les deux branches et tous les renvois : 1 de l'article 200-0 A, articles 75-0 B, 84 A, 100 bis, 75-0 A, 163-0 A et 163-0 A bis, et I de l'article 197 du CGI. Les exemples introduits par « notamment » restent non limitatifs. La multiplication visée au 2° intervient après la prise en compte prescrite. La note sur l'article 29-III-2° et IV B de la loi n° 2019-1479 du 28 décembre 2019 ne constitue pas une date d'entrée en vigueur de la réforme."
    ),
    (
        "Réécriture à droit constant : l'obligation de déclarer est formulée avec un sujet actif et les deux montants à porter séparément sur la déclaration sont maintenus. La seconde rubrique reste le montant des sommes ouvrant droit aux avantages et non le montant des réductions ou crédits eux-mêmes. Aucune réforme de fond n'est introduite.",
        "Coordonner avec les articles 46-0 B et 46-0 B bis et conserver les renvois aux articles 170, 31, 31 bis et 200-0 A du CGI. Les h et l du 1° du I de l'article 31 sont maintenus pour les amortissements relevant des régimes concernés ; la simplification déclarative des sociétés immobilières aux articles 46 B et 46 C ne dispense pas de cette déclaration des montants entrant dans le plafonnement."
    ),
    (
        "À droit constant, la société, le service destinataire, les renseignements et les deux délais de trois mois sont exprimés directement. Réforme de fond, en application de la mesure « déclarer une fois » de policy.json : suppression de la remise en double exemplaire de la déclaration et des statuts, puis ajout d'un IV organisant le réemploi des données et documents à jour légalement accessibles, leur identification et leur rectification à la source. Aucun champ d'imposition n'est modifié.",
        "Les subdivisions I à III et leurs positions sont conservées ; le IV est ajouté à la fin. La déclaration de constitution et son renouvellement demeurent dus, avec les renseignements nouveaux ou modifiés. Le champ demeure celui de l'article 172 bis du CGI, qui exclut les sociétés visées à l'article 1655 ter. Coordonner les formulaires et les modalités de dépôt avec l'article 46 C et conserver les pouvoirs de justification de l'article 46 D. Le réemploi est subordonné à un accès déjà légal, à l'actualité des données et au respect des secrets ; cette disposition n'autorise aucun échange nouveau. Si de nouveaux échanges soumis au secret fiscal sont nécessaires à sa mise en œuvre, ils appellent une disposition législative d'habilitation dans le livre des procédures fiscales, hors des cinq codes, à créer sans numéro présumé."
    ),
    (
        "À droit constant, les données d'identification des associés sont réparties entre personnes physiques et morales au sein du a, et les règles de calcul des revenus, de vérification et de valeur ajoutée sont rendues plus lisibles. Réforme de fond issue de policy.json : suppression du double exemplaire administratif et ajout d'un IV de réemploi des données et documents à jour légalement accessibles, avec identification et rectification à la source. L'obligation annuelle et son contenu fiscal demeurent.",
        "Les I à III, les lettres a à e et l'échéance au deuxième jour ouvré après le premier mai sont préservés ; le IV est ajouté après le III. Coordonner les modalités de réemploi et les formulaires avec l'article 46 B proposé, sans ouvrir d'accès nouveau aux données protégées. Les articles 234 nonies, 1586 octies et 1586 sexies ne visent pas la C3S et ne sont pas supprimés au titre de son extinction. Le corpus comporte des abrogations différées pour les deux derniers articles : contrôler la coordination temporelle du tableau de valeur ajoutée sans anticiper la disparition des obligations historiques. La procédure de vérification directe avec la société et les justifications de l'article 46 D demeurent. Une extension des échanges couverts par le secret fiscal nécessiterait, le cas échéant, une habilitation législative dans le livre des procédures fiscales, hors des cinq codes, sans renvoi nouveau inventé."
    ),
    (
        "Réécriture à droit constant : les sociétés sont le sujet explicite de l'obligation de présentation, et le lien entre les pièces requises et l'exactitude des déclarations est formulé plus directement. Toutes les catégories de pièces et le pouvoir de réquisition du service des impôts sont conservés ; aucune réforme de fond du contrôle n'est introduite.",
        "La présentation sur réquisition reste distincte des formalités de dépôt simplifiées aux articles 46 B et 46 C proposés. Les documents comptables ou sociaux, inventaires, copies de lettres et pièces de recettes et de dépenses demeurent couverts. La disposition ne crée ni délai de conservation nouveau ni suppression du pouvoir de contrôler les renseignements déclarés."
    ),
    (
        "Réécriture à droit constant : les règles de rattachement des produits et dépenses sont exprimées en phrases plus directes, et la condition de déduction des provisions reste dans le deuxième alinéa du I. Le II explicite les produits et charges à exclure de la dernière période d'impôt sur le revenu. Aucune réforme de fond ni modification du taux d'impôt sur les sociétés n'est introduite.",
        "Maintenir les deux alinéas du I, le II et les renvois au premier alinéa du II et au III de l'article 202 ter ainsi qu'au 5° du 1 de l'article 39 du CGI. La perte totale ou partielle d'assujettissement, la condition de reprise des provisions au bilan d'ouverture et le rattachement postérieur des créances ou dettes au II sont conservés. La coquille « code général de impôts » est corrigée en « code général des impôts », sans changement de référence. La mesure de policy.json relative au taux normal d'IS relève de l'article 219, pas de ces règles de changement de régime."
    ),
    (
        "Réécriture à droit constant : la périodicité mensuelle est placée en tête, le compte rendu est décrit directement et la détection des anomalies est attribuée explicitement à l'administration fiscale. Les subdivisions, les identifiants et l'exception de transmission du taux restent inchangés. Aucune réforme de fond du prélèvement à la source ou de la CSG n'est introduite.",
        "Le renvoi aux e et g du 3° du V de l'article R. 133-14 du code de la sécurité sociale a été vérifié dans le corpus : il vise les identifiants du salarié, y compris ceux d'attente ou provisoires dans les conditions de cet article. Conserver le III de l'article 204 H et l'article 87-0 A du CGI. La note de l'article 2 du décret n° 2017-1676 du 7 décembre 2017 fixe l'application aux revenus perçus ou réalisés à compter du 1er janvier 2019 ; cette borne historique est conservée et n'est pas transformée en date de réforme future. Le taux de prélèvement à la source ne doit pas être confondu avec le taux de CSG salariale visé par policy.json."
    ),
]


def build():
    sources = json.loads(Path('source.json').read_text())
    assert len(sources) == len(metadata) == 17
    answer = []
    for i, (source, (reason, review_notes)) in enumerate(zip(sources, metadata)):
        row = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
        row.update(
            proposed_xml=Path(f'drafts/{i:02d}.xml').read_text().strip(),
            reason=reason,
            review_notes=review_notes,
            status='rewrite_draft',
        )
        answer.append(row)
    Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    build()
