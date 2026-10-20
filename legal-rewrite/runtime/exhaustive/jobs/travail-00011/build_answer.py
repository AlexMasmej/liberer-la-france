import json
from pathlib import Path


SOURCES = json.loads(Path('source.json').read_text())
DRAFTS = {}


def add(number, xml, reason, notes):
    assert number not in DRAFTS
    DRAFTS[number] = {
        'proposed_xml': xml.strip(),
        'reason': reason,
        'review_notes': notes,
        'status': 'rewrite_draft',
    }


add('L1251-10', '''
<p>Le recours au travail temporaire est interdit, en plus des cas prévus à l'article L. 1251-9 :</p>
<p>1° Pour remplacer un salarié dont le contrat de travail est suspendu à la suite d'un conflit collectif de travail ;</p>
<p>2° Pour exécuter certains travaux particulièrement dangereux inscrits sur une liste établie par voie réglementaire, dans les conditions prévues à l'article L. 4154-1. Une dérogation à cette interdiction peut être exceptionnellement autorisée par l'autorité administrative, dans les conditions fixées par voie réglementaire ;</p>
<p>3° Pour remplacer un médecin du travail.</p>
''',
    "Réécriture à droit constant : l'interdiction de recourir au travail temporaire est énoncée directement et la dérogation administrative reste rattachée au seul 2°. Aucune réforme de fond du projet ne modifie ces interdictions.",
    "Les 1° à 3°, les renvois à L. 1251-9 et L. 4154-1 et le caractère exceptionnel de la dérogation sont conservés. Les deux articles de renvoi ont été vérifiés dans le corpus public ; les interdictions et exceptions propres à L. 1251-9 demeurent distinctes.")

add('L1251-11', '''
<p>Le terme du contrat de mission doit être fixé avec précision dès la conclusion du contrat de mise à disposition.</p>
<p>Par exception, le contrat de mission peut être conclu sans terme précis dans les cas suivants :</p>
<p>1° Pour remplacer un salarié absent ;</p>
<p>2° Pour remplacer un salarié dont le contrat de travail est suspendu ;</p>
<p>3° Dans l'attente de l'entrée en service effective d'un salarié recruté par contrat à durée indéterminée ;</p>
<p>4° Pour occuper un emploi à caractère saisonnier défini au 3° de l'article L. 1242-2, ou un emploi pour lequel il est d'usage constant de ne pas recourir au contrat de travail à durée indéterminée. Dans ce dernier cas, le secteur d'activité doit être défini par décret ou par une convention ou un accord collectif étendu, et cet usage doit tenir à la nature de l'activité exercée et au caractère par nature temporaire de l'emploi ;</p>
<p>5° Pour remplacer l'une des personnes mentionnées aux 4° et 5° de l'article L. 1251-6.</p>
<p>Dans ces cas, le contrat de mission est conclu pour une durée minimale. Il prend fin lorsque cesse l'absence de la personne remplacée ou lorsque se réalise l'objet pour lequel il a été conclu.</p>
''',
    "Réécriture à droit constant : distinction explicite entre le principe du terme précis et ses cinq exceptions. Le 4° est divisé en deux phrases dans la même subdivision pour rendre lisibles les conditions des emplois d'usage. Aucune réforme de fond n'est introduite.",
    "Les huit alinéas, les cinq cas, la durée minimale et les deux événements déterminant le terme sont maintenus. Au 4°, la définition du secteur et les justifications de l'usage concernent la seconde catégorie d'emplois. Les renvois au 3° de L. 1242-2 et aux 4° et 5° de L. 1251-6 sont conservés ; les deux derniers ont été vérifiés dans le corpus.")

add('L1251-12', '''
<p>Une convention ou un accord de branche étendu applicable à l'entreprise utilisatrice peut déterminer la durée totale du contrat de mission. La durée ainsi fixée ne doit avoir ni pour objet ni pour effet de pourvoir durablement un emploi lié à l'activité normale et permanente de l'entreprise.</p>
''',
    "Réécriture à droit constant : identification de l'accord applicable à l'entreprise utilisatrice et rattachement explicite de l'interdiction de pourvoir un emploi permanent à la durée ainsi fixée. Aucune réforme de fond n'est appliquée.",
    "La compétence reste celle d'une convention ou d'un accord de branche étendu. La note source réserve l'application aux contrats de travail conclus postérieurement à la publication de l'ordonnance n° 2017-1387 du 22 septembre 2017, en vertu de son article 40-VIII ; cette portée temporelle demeure à respecter. Coordination avec L. 1251-12-1, L. 1251-30 et les règles de renouvellement.")

add('L1251-12-1', '''
<p>Lorsqu'aucune stipulation de la convention ou de l'accord de branche conclu en application de l'article L. 1251-12 ne fixe cette durée, la durée totale du contrat de mission est limitée à dix-huit mois. Elle inclut, le cas échéant, le ou les renouvellements effectués dans les conditions prévues à l'article L. 1251-35 ou, lorsqu'il s'applique, à l'article L. 1251-35-1.</p>
<p>Ce plafond est ramené à neuf mois si le contrat est conclu dans l'attente de l'entrée en service effective d'un salarié recruté par contrat à durée indéterminée, ou s'il a pour objet la réalisation de travaux urgents nécessités par des mesures de sécurité.</p>
<p>Ce plafond est fixé à vingt-quatre mois dans les cas suivants :</p>
<p>1° Lorsque la mission est exécutée à l'étranger ;</p>
<p>2° Lorsque le contrat est conclu dans le cas où le départ définitif d'un salarié précède la suppression de son poste de travail ;</p>
<p>3° Lorsqu'une commande exceptionnelle à l'exportation survient dans l'entreprise de l'entrepreneur principal ou dans celle d'un sous-traitant et que son importance nécessite la mise en œuvre de moyens quantitativement ou qualitativement exorbitants par rapport à ceux que l'entreprise utilise ordinairement. Dans ce cas, le contrat initial doit avoir une durée d'au moins six mois.</p>
<p>Le plafond est porté à trente-six mois pour être égal à la durée du cycle de formation suivi en apprentissage conformément à l'article L. 6222-7-1.</p>
''',
    "Réécriture à droit constant : les plafonds supplétifs et leurs cas d'application sont présentés dans des alinéas distincts correspondant aux blocs du texte source. Les conditions de la commande exceptionnelle sont réordonnées dans le même 3°. Aucune nouvelle durée ni réforme de fond n'est créée.",
    "Contrôle des durées : dix-huit mois avec renouvellements, neuf mois dans les deux cas prévus, vingt-quatre mois dans les trois cas numérotés, minimum initial de six mois au seul 3°, et trente-six mois pour l'apprentissage. Renvois vérifiés à L. 1251-35, L. 1251-35-1 et L. 6222-7-1. La formulation source portant le plafond à trente-six mois pour l'égaler au cycle est conservée ; son articulation avec les durées variables et dérogations de L. 6222-7-1 appelle contrôle. La note source maintient l'application aux contrats conclus postérieurement à la publication de l'ordonnance n° 2017-1387 du 22 septembre 2017, article 40-VIII. La dérogation de L. 1251-34 demeure extérieure au présent article.")

add('L1251-13', '''
<p>Le contrat de mission peut prendre effet avant le début de l'absence de la personne à remplacer lorsqu'il est conclu pour remplacer un salarié temporairement absent, un salarié dont le contrat de travail est suspendu ou une personne au titre des 4° et 5° de l'article L. 1251-6.</p>
''',
    "Réécriture à droit constant : la possibilité d'anticiper la prise d'effet du contrat est placée en tête, puis les trois catégories de remplacement sont précisées. Aucune réforme de fond n'est introduite.",
    "La prise d'effet anticipée reste facultative et n'est assortie d'aucun nouveau délai. Les catégories de remplacement et le renvoi aux 4° et 5° de L. 1251-6 sont conservés. La possibilité distincte de reporter le terme demeure à L. 1251-31.")

add('L1251-14', '''
<p>Une période d'essai peut être prévue par le contrat de mission. Sa durée est fixée par une convention ou un accord professionnel de branche étendu, ou par une convention ou un accord d'entreprise ou d'établissement.</p>
<p>En l'absence d'une telle convention ou d'un tel accord, la période d'essai ne peut dépasser :</p>
<p>1° Deux jours pour un contrat d'une durée inférieure ou égale à un mois ;</p>
<p>2° Trois jours pour un contrat d'une durée supérieure à un mois et inférieure ou égale à deux mois ;</p>
<p>3° Cinq jours pour un contrat d'une durée supérieure à deux mois.</p>
''',
    "Réécriture à droit constant : séparation, dans le premier alinéa, de la faculté de prévoir un essai et des sources conventionnelles fixant sa durée ; présentation parallèle des trois plafonds supplétifs. L'essai de trois mois proposé pour les nouveaux CDI n'est pas étendu au contrat de mission.",
    "Les limites restent de deux, trois et cinq jours, selon les seuils d'un mois et de deux mois, avec les mêmes bornes inclusives ou exclusives. La nature professionnelle et le caractère étendu de l'accord de branche sont maintenus, ainsi que les accords d'entreprise ou d'établissement. Régime distinct de L. 1221-19 et suivants : aucune durée de trois mois ni interdiction nouvelle de renouvellement n'est ajoutée ici.")

add('L1251-15', '''
<p>Pendant la période d'essai, le salarié perçoit la rémunération prévue par le contrat de mission.</p>
''',
    "Réécriture à droit constant : l'interdiction d'une rémunération différente pendant l'essai est exprimée comme un droit direct du salarié à la rémunération contractuelle. Aucune réforme de fond n'est appliquée.",
    "L'identité avec la rémunération prévue par le contrat est maintenue : aucun abattement ni montant particulier pour l'essai n'est créé. Coordination avec la période d'essai propre aux missions, prévue à L. 1251-14.")

add('L1251-16', '''
<p>Le contrat de mission doit être rédigé par écrit.</p>
<p>Il doit notamment comporter :</p>
<p>1° La reproduction des clauses et des mentions du contrat de mise à disposition que l'article L. 1251-43 énumère ;</p>
<p>2° La qualification professionnelle du salarié ;</p>
<p>3° Les modalités de la rémunération due au salarié, y compris celles de l'indemnité de fin de mission prévue à l'article L. 1251-32 ;</p>
<p>4° La durée de la période d'essai, si le contrat en prévoit une ;</p>
<p>5° Pour une mission réalisée hors du territoire métropolitain, une clause prévoyant le rapatriement du salarié aux frais de l'entrepreneur de travail temporaire. Cette clause devient caduque lorsque la rupture du contrat intervient à l'initiative du salarié ;</p>
<p>6° Le nom et l'adresse de la caisse de retraite complémentaire et de l'organisme de prévoyance dont relève l'entreprise de travail temporaire ;</p>
<p>7° La mention précisant que l'embauche du salarié par l'entreprise utilisatrice n'est pas interdite à l'issue de la mission.</p>
''',
    "Réécriture à droit constant : les obligations de forme et de contenu sont formulées explicitement. La condition territoriale du rapatriement est placée au début du 5°, sans modifier la charge des frais ni la caducité. Aucune réforme de fond n'est introduite.",
    "Les neuf alinéas et les sept mentions sont maintenus, avec le caractère non exhaustif de la liste. Le 1° impose toujours la reproduction, et non une simple référence, des clauses de L. 1251-43, vérifié dans le corpus. Le champ hors territoire métropolitain et l'initiative du salarié au 5° sont conservés. L'indemnité de fin de mission de L. 1251-32 reste distincte de l'indemnité de licenciement réformée par le projet.")

add('L1251-17', '''
<p>La transmission du contrat de mission au salarié doit intervenir au plus tard dans les deux jours ouvrables suivant sa mise à disposition.</p>
''',
    "Réécriture à droit constant : la phrase énonce directement l'obligation de transmission et son échéance. Aucune réforme de fond n'est introduite.",
    "Le délai reste de deux jours ouvrables suivant la mise à disposition ; il n'est converti ni en jours calendaires ni en délai de réception. Aucune sanction ou modalité de transmission nouvelle n'est ajoutée.")

add('L1251-18', '''
<p>Le salarié temporaire perçoit une rémunération, au sens de l'article L. 3221-3, au moins égale à celle prévue par le contrat de mise à disposition et définie au 6° de l'article L. 1251-43.</p>
<p>Lorsque les salariés de l'entreprise utilisatrice bénéficient du paiement des jours fériés, le salarié temporaire y a également droit, quelle que soit son ancienneté.</p>
''',
    "Réécriture à droit constant : le plancher de rémunération est exprimé positivement et la condition de paiement des jours fériés est placée avant le droit du salarié temporaire. Aucune réforme de fond ne modifie ce mécanisme.",
    "Les deux alinéas et les renvois à L. 3221-3 et au 6° de L. 1251-43 sont conservés et ont été vérifiés dans le corpus. La rémunération de référence inclut les composantes définies par ces articles. L'absence de condition d'ancienneté pour les jours fériés est maintenue ; le salaire contractuel n'est pas réduit.")

add('L1251-19', '''
<p>Chaque mission ouvre au salarié temporaire un droit à une indemnité compensatrice de congé payé, quelle que soit sa durée.</p>
<p>Cette indemnité est calculée en fonction de la durée de la mission. Elle doit représenter au moins le dixième de la rémunération totale brute perçue par le salarié pendant la mission. Elle est versée à la fin de la mission.</p>
<p>Pour déterminer les droits du salarié, les périodes suivantes sont assimilées à du temps de mission :</p>
<p>1° Les périodes de congé légal de maternité, de paternité et d'accueil de l'enfant et d'adoption ;</p>
<p>2° Les périodes mentionnées aux 5° et 7° de l'article L. 3141-5 ;</p>
<p>3° Les périodes de rappel sous les drapeaux, si elles commencent au cours d'une mission.</p>
''',
    "Réécriture à droit constant : le droit par mission est énoncé directement et le calcul, le minimum et le versement sont distingués dans le deuxième alinéa. La condition temporelle du rappel sous les drapeaux est simplifiée sans être supprimée. Aucune réforme de fond n'est appliquée.",
    "Les six alinéas sont conservés. Minimum inchangé : un dixième de la rémunération totale brute perçue pendant la mission, avec versement en fin de mission. Le renvoi aux 5° et 7° de L. 3141-5, vérifié dans le corpus, couvre les suspensions pour accident du travail ou maladie professionnelle et celles pour accident ou maladie non professionnels. L'assimilation au 3° exige toujours un début pendant une mission. Ne pas confondre cette indemnité avec celle de fin de mission de L. 1251-32.")

add('L1251-20', '''
<p>En cas d'arrêt de travail provoqué par les intempéries, le salarié temporaire mis à la disposition d'une entreprise du bâtiment ou des travaux publics mentionnée à l'article L. 5424-6 bénéficie d'une indemnité lorsque les salariés de l'entreprise utilisatrice employés sur le même chantier en bénéficient.</p>
<p>L'entreprise de travail temporaire verse cette indemnité. Celle-ci est calculée selon les modalités prévues aux articles L. 5424-6 à L. 5424-19 et est due sans condition d'ancienneté du salarié.</p>
''',
    "Réécriture à droit constant : l'événement ouvrant le droit précède ses conditions et l'entreprise chargée du versement devient le sujet de la seconde phrase. Aucune réforme de fond n'est introduite.",
    "Les conditions cumulatives de secteur, d'intempéries et d'indemnisation des salariés du même chantier sont maintenues. Les bornes du renvoi L. 5424-6 à L. 5424-19 ont été vérifiées dans le corpus. Le versement reste à la charge de l'entreprise de travail temporaire, sans condition d'ancienneté.")

add('L1251-21', '''
<p>Pendant la mission, l'entreprise utilisatrice est responsable des conditions d'exécution du travail définies par les dispositions légales et conventionnelles applicables au lieu de travail.</p>
<p>Pour l'application de ces dispositions, seules les matières suivantes relèvent des conditions d'exécution du travail :</p>
<p>1° La durée du travail ;</p>
<p>2° Le travail de nuit ;</p>
<p>3° Le repos hebdomadaire et les jours fériés ;</p>
<p>4° La santé et la sécurité au travail ;</p>
<p>5° Le travail des femmes, des enfants et des jeunes travailleurs.</p>
''',
    "Réécriture à droit constant : suppression de la tournure « comprennent limitativement ce qui a trait » au profit d'une liste expressément limitative, avec maintien des cinq matières. Aucune réforme de fond propre au travail temporaire n'est ajoutée.",
    "Les sept alinéas, la responsabilité de l'entreprise utilisatrice et le rattachement aux règles du lieu de travail sont maintenus. La réforme du seuil hebdomadaire relève de L. 3121-27 à L. 3121-29 et de leur transition ; cet article ne fixe pas de seuil distinct et ne transforme pas les règles annuelles ou plurihebdomadaires. Les catégories du 5° sont conservées sans généralisation silencieuse.")

add('L1251-22', '''
<p>L'entreprise de travail temporaire assume les obligations relatives à la médecine du travail.</p>
<p>Des services de prévention et de santé au travail disposant d'un agrément spécifique assurent le suivi médical des salariés. Cette règle ne s'applique pas lorsque l'entreprise de travail temporaire relève du régime agricole.</p>
<p>Si l'entreprise utilisatrice dispose de son propre service de prévention et de santé au travail, ce service peut assurer le suivi des salariés dans le cadre d'une convention conclue avec l'entreprise de travail temporaire.</p>
<p>Si l'activité exercée par le salarié temporaire exige une surveillance médicale renforcée au sens de la réglementation relative à la santé au travail, l'entreprise utilisatrice assume les obligations liées à cette surveillance.</p>
''',
    "Réécriture à droit constant : chaque obligation ou faculté est rattachée explicitement à l'entreprise ou au service concerné. L'exception agricole reste limitée à la règle du deuxième alinéa. Aucune réforme de fond n'est introduite.",
    "Les quatre alinéas conservent l'agrément spécifique, la convention permettant le suivi par le service de l'entreprise utilisatrice et la charge particulière de la surveillance renforcée. Décalage terminologique préexistant : la source législative parle de « surveillance médicale renforcée », tandis que R. 4625-9 vise le « suivi individuel renforcé » et répartit les examens ; cette terminologie n'est pas harmonisée silencieusement. Selon la note source, l'entrée en vigueur est le 31 mars 2022, conformément au I de l'article 40 de la loi n° 2021-1018 du 2 août 2021, sous les conditions d'application de son II. Ces références historiques ne fixent aucune date de réforme future.")

add('L1251-23', '''
<p>L'entreprise utilisatrice fournit les équipements de protection individuelle.</p>
<p>Une convention ou un accord collectif de travail peut toutefois définir certains équipements de protection individuelle personnalisés que l'entreprise de travail temporaire peut fournir.</p>
<p>Le coût des équipements de protection individuelle ne peut être mis à la charge des salariés temporaires.</p>
''',
    "Réécriture à droit constant : les fournisseurs des équipements sont identifiés par des phrases actives, et l'interdiction d'en faire supporter le coût au salarié est formulée directement. Aucune réforme de fond n'est introduite.",
    "Les trois alinéas sont maintenus. La possibilité de fourniture par l'entreprise de travail temporaire reste limitée à certains équipements personnalisés définis par convention ou accord collectif de travail. Aucune participation financière du salarié n'est créée.")

add('L1251-24', '''
<p>Dans l'entreprise utilisatrice, les salariés temporaires ont accès aux moyens de transport collectifs et aux installations collectives, notamment de restauration, dont les salariés de cette entreprise peuvent bénéficier. Cet accès leur est accordé dans les mêmes conditions qu'à ces salariés.</p>
<p>Si des dépenses supplémentaires incombent au comité social et économique, elles lui sont remboursées selon les modalités fixées par le contrat de mise à disposition.</p>
''',
    "Réécriture à droit constant : le premier alinéa distingue l'accès aux équipements collectifs de l'égalité de ses conditions. Le remboursement au comité social et économique est reformulé sans désigner un débiteur absent de la source. Aucune réforme de fond n'est introduite.",
    "Les deux alinéas sont conservés, avec les transports collectifs, les installations collectives dont la restauration et les mêmes conditions d'accès. Les dépenses supplémentaires du comité social et économique restent remboursées suivant le contrat de mise à disposition ; aucune nouvelle règle de financement n'est ajoutée.")

add('L1251-25', '''
<p>L'entreprise utilisatrice doit informer le salarié temporaire, à la demande de celui-ci, des postes à pourvoir en contrat à durée indéterminée dans l'entreprise, dès lors que ce salarié justifie d'une ancienneté continue d'au moins six mois en son sein.<br/><br/>Les modalités d'application du présent article sont fixées par décret.</p>
''',
    "Réécriture à droit constant : l'entreprise tenue d'informer est placée en tête, avec maintien du déclenchement à la demande du salarié et de la condition d'ancienneté. Aucune réforme de fond n'est introduite.",
    "Le seuil d'au moins six mois d'ancienneté continue est apprécié dans l'entreprise utilisatrice. L'information reste limitée aux postes à pourvoir en CDI dans cette entreprise et ne devient pas une obligation d'embauche. Le bloc réglementaire final reste à sa place, séparé par des sauts de ligne comme dans la source.")

add('L1251-26', '''
<p>Sauf faute grave du salarié ou cas de force majeure, l'entreprise de travail temporaire qui rompt un contrat de mission avant le terme prévu doit proposer au salarié un nouveau contrat de mission. Celui-ci doit prendre effet dans un délai maximal de trois jours ouvrables.</p>
<p>Le nouveau contrat de mission ne doit modifier aucun élément essentiel concernant la qualification professionnelle, la rémunération, l'horaire de travail et le temps de transport.</p>
<p>À défaut d'un nouveau contrat conforme à ces conditions, ou si sa durée est inférieure à celle qui restait à courir au titre du contrat précédent, l'entrepreneur de travail temporaire assure au salarié une rémunération équivalente à celle qu'il aurait perçue jusqu'au terme du contrat rompu, indemnité de fin de mission comprise.</p>
<p>Si plus de quatre semaines restaient à courir au titre du contrat de mission rompu, les obligations prévues au présent article peuvent être remplies au moyen d'au plus trois contrats successifs.</p>
''',
    "Réécriture à droit constant : l'exception et les obligations de proposition et de prise d'effet sont distinguées dans le premier alinéa ; l'exigence de maintien des éléments essentiels est exprimée directement. La garantie de rémunération et la faculté de contrats successifs restent dans leurs alinéas respectifs. Aucune réforme de fond n'est appliquée.",
    "Les quatre alinéas sont maintenus : le deuxième, relatif aux éléments essentiels, reste expressément la cible du renvoi de L. 1251-34, vérifié dans le corpus. Contrôle des paramètres : trois jours ouvrables, durée restante strictement supérieure à quatre semaines, trois contrats successifs au plus. La faute grave doit être celle du salarié ; la garantie inclut l'indemnité de fin de mission. L. 1251-27 exclut toujours la rupture du contrat de mise à disposition de la force majeure. Le nouveau motif économique et l'indemnité de licenciement du projet ne sont pas substitués à ce régime.")

add('L1251-27', '''
<p>La rupture du contrat de mise à disposition ne peut être qualifiée de cas de force majeure.</p>
''',
    "Réécriture à droit constant : l'exclusion de la force majeure est formulée comme une interdiction de qualifier ainsi la rupture du contrat de mise à disposition. Aucune réforme de fond n'est introduite.",
    "L'exclusion reste limitée à la rupture du contrat de mise à disposition ; elle ne supprime pas tous les autres cas de force majeure. Coordination avec l'exception figurant au premier alinéa de L. 1251-26.")

add('L1251-28', '''
<p>Lorsque le salarié rompt le contrat de mission avant son terme, l'entreprise de travail temporaire a droit à des dommages et intérêts à hauteur du préjudice qu'elle subit.</p>
<p>L'entreprise ne peut toutefois réclamer ces dommages et intérêts si le salarié justifie avoir conclu un contrat de travail à durée indéterminée.</p>
<p>Dans ce cas, sauf accord des parties, le salarié doit respecter un préavis calculé à raison d'un jour par semaine, sur la base :</p>
<p>1° De la durée totale du contrat, en incluant, le cas échéant, son ou ses deux renouvellements, si le contrat prévoit un terme précis ;</p>
<p>2° De la durée déjà accomplie, si le contrat ne prévoit pas de terme précis.</p>
<p>Dans l'un comme dans l'autre cas, le préavis ne peut durer moins d'un jour ni plus de deux semaines.</p>
''',
    "Réécriture à droit constant : identification de l'entreprise bénéficiaire de la réparation, formulation directe de l'exception liée au CDI et clarification des bases de calcul du préavis. Les six blocs du texte source restent dans leur ordre. Aucune réforme de fond n'est introduite.",
    "Un jour de préavis par semaine, minimum d'un jour et maximum de deux semaines, avec dispense ou aménagement par accord des parties : paramètres conservés. Incohérence préexistante à coordonner : le 1° vise encore « son ou ses deux renouvellements », alors que L. 1251-35 autorise la branche à fixer le nombre maximal de renouvellements et que la limite supplétive de deux figure à L. 1251-35-1 ; ces deux articles ont été vérifiés dans le corpus. La mention de deux renouvellements est conservée plutôt que corrigée sans disposition expresse. La note source indique l'application aux contrats en cours sans préciser de référence ni de date ; sa portée temporelle doit être contrôlée et ne sert pas de transition à une réforme future.")

add('L1251-29', '''
<p>La suspension du contrat de mission du salarié n'en empêche pas l'arrivée à échéance.</p>
''',
    "Réécriture à droit constant : la formule « ne fait pas obstacle à l'échéance » est remplacée par une formulation plus directe, sans modifier l'effet de la suspension. Aucune réforme de fond n'est introduite.",
    "La suspension n'entraîne pas, par elle-même, le report du terme. Aucune nouvelle exception ni règle de rupture anticipée n'est ajoutée ; les possibilités distinctes d'aménagement du terme restent régies par les articles voisins.")

add('L1251-30', '''
<p>Le terme de la mission, prévu par le contrat de mise à disposition ou fixé par un avenant à ce contrat, peut être avancé ou reporté à raison d'un jour pour cinq jours de travail. Pour une mission de moins de dix jours de travail, ce terme peut être avancé ou reporté de deux jours.</p>
<p>Cette modification du terme ne doit ni réduire de plus de dix jours de travail la durée de mission initialement prévue, ni porter la durée du contrat de mission au-delà du maximum fixé par les articles L. 1251-12 et L. 1251-12-1.</p>
''',
    "Réécriture à droit constant : identification explicite de l'avenant au contrat de mise à disposition, puis formulation parallèle des deux limites à l'aménagement du terme. Aucune réforme de fond n'est introduite.",
    "Les deux alinéas sont maintenus. Contrôle des quantités : un jour pour cinq jours de travail ; régime de deux jours pour les missions strictement inférieures à dix jours de travail ; réduction limitée à dix jours de travail ; maintien des plafonds de L. 1251-12 et L. 1251-12-1. Le 3° de L. 1251-43, vérifié dans le corpus, vise toujours la clause d'aménagement. La note source limite l'application aux contrats conclus postérieurement à la publication de l'ordonnance n° 2017-1387 du 22 septembre 2017, article 40-VIII ; cette portée historique est conservée.")

add('L1251-31', '''
<p>Le terme initial de la mission peut être reporté jusqu'au surlendemain du jour où la personne remplacée reprend son emploi, lorsque le contrat de mission est conclu pour remplacer un salarié temporairement absent, un salarié dont le contrat de travail est suspendu ou une personne au titre des 4° et 5° de l'article L. 1251-6.</p>
''',
    "Réécriture à droit constant : la faculté de report et sa limite sont placées avant les catégories de remplacement qui l'autorisent. Aucune réforme de fond n'est introduite.",
    "La limite demeure le surlendemain du jour de reprise, sans conversion en jours ouvrables. Les trois catégories de remplacement et le renvoi aux 4° et 5° de L. 1251-6 sont maintenus. Coordination avec L. 1251-13 pour la prise d'effet anticipée et avec la clause prévue au 3° de L. 1251-43.")

add('L1251-32', '''
<p>À l'issue d'une mission, si le salarié ne bénéficie pas immédiatement d'un contrat de travail à durée indéterminée avec l'entreprise utilisatrice, il a droit à une indemnité de fin de mission. Ce complément de salaire est destiné à compenser la précarité de sa situation.</p>
<p>Le montant de cette indemnité est fixé à 10 % de la rémunération totale brute due au salarié.</p>
<p>L'entreprise de travail temporaire verse cette indemnité en plus de la rémunération totale brute due au salarié. Le versement intervient à l'issue de chaque mission effectivement accomplie, en même temps que le dernier salaire dû pour cette mission. L'indemnité doit figurer sur le bulletin de salaire correspondant.</p>
''',
    "Réécriture à droit constant : distinction du fait générateur, de la nature salariale et de la finalité de l'indemnité dans le premier alinéa ; identification de l'entreprise débitrice et séparation des obligations de versement et de mention au bulletin dans le troisième. Aucune réforme de fond n'est appliquée.",
    "Le taux de 10 %, l'assiette de rémunération totale brute due, le CDI immédiat avec l'entreprise utilisatrice, le versement à chaque mission effectivement accomplie et sa simultanéité avec le dernier salaire sont conservés. Les exceptions prévues par L. 1251-33, vérifié dans le corpus, restent applicables et ne sont pas déplacées ici. Cette indemnité est distincte de l'indemnité compensatrice de congé payé de L. 1251-19 et de l'indemnité de licenciement de L. 1234-9 : ni le taux de 0,20 mois ni le plafond de six mois du projet ne lui sont appliqués.")


assert len(SOURCES) == 24
assert set(DRAFTS) == {s['number'] for s in SOURCES}
answer = []
for source in SOURCES:
    item = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    item.update(DRAFTS[source['number']])
    answer.append(item)

Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
