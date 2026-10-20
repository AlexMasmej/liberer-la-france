import json
import re
from pathlib import Path
import xml.etree.ElementTree as ET


SOURCES = json.loads(Path('source.json').read_text())
DRAFTS = {}


def draft(number, xml, reason, notes):
    assert number not in DRAFTS
    DRAFTS[number] = {
        'proposed_xml': xml.strip(),
        'reason': reason,
        'review_notes': notes,
        'status': 'rewrite_draft',
    }


HISTORY_2017 = (
    'La note source réserve l’application de ces dispositions aux licenciements '
    'prononcés après la publication de l’ordonnance n° 2017-1387 du 22 septembre '
    '2017, conformément à son article 40-I. Cette transition historique est '
    'conservée ; elle ne détermine pas la date d’une réforme future.'
)


draft('L1234-16', '''
<p>Les salariés suivants ont droit à un préavis de six semaines :</p>
<p>1° Les professeurs et les personnes employées chez des particuliers ;</p>
<p>2° Les commis commerciaux mentionnés à l’article L. 1226-24 ;</p>
<p>3° Les salariés dont la rémunération est fixe et qui assurent de manière permanente la direction ou la surveillance d’une activité ou d’une partie de celle-ci, ou les salariés auxquels sont confiés des services techniques nécessitant une certaine qualification.</p>
''',
    'Réécriture à droit constant : le bénéficiaire du préavis est annoncé dès le premier alinéa et les fonctions du 3° sont formulées directement. Les trois catégories et la durée de six semaines sont conservées. Aucune réforme de fond n’est appliquée à ce préavis spécial.',
    'Conserver le champ territorial de la sous-section relative à la Moselle, au Bas-Rhin et au Haut-Rhin et son articulation avec L. 1234-17-1. Le renvoi à L. 1226-24 vise la définition du commis commercial, vérifiée dans le corpus public. La formulation du 3° conserve les deux branches de la source sans étendre silencieusement la condition de rémunération fixe à la seconde.')

draft('L1234-17', '''
<p>Pendant le préavis, le salarié peut demander un délai raisonnable pour rechercher un nouvel emploi. L’employeur doit lui accorder ce délai.</p>
''',
    'Réécriture à droit constant : deux phrases distinguent la demande du salarié et l’obligation corrélative de l’employeur, en identifiant le sujet de chaque action. Le caractère raisonnable du délai et son objet restent inchangés ; aucune réforme de fond.',
    'Le bénéfice reste subordonné à une demande pendant le préavis. Aucun nombre d’heures ni régime de rémunération de ce délai n’est ajouté. Maintenir l’application de L. 1234-17-1 au sein du régime local.')

draft('L1234-17-1', '''
<p>Les règles de la présente sous-section s’appliquent lorsqu’aucune disposition légale ou conventionnelle ni aucun usage ne prévoit un préavis plus long. Elles s’appliquent aussi lorsque le salarié prend l’initiative de rompre son contrat de travail à durée indéterminée.</p>
''',
    'Réécriture à droit constant : la priorité donnée aux préavis plus longs est exprimée sous forme de condition explicite ; l’initiative du salarié est formulée avec un sujet actif. Les deux règles demeurent dans le même alinéa. Aucune réforme de fond.',
    'La priorité couvre les dispositions légales, les dispositions conventionnelles et les usages. La seconde phrase reste limitée au contrat à durée indéterminée ; elle maintient l’application de la sous-section aux ruptures à l’initiative du salarié sans modifier les délais.')

draft('L1234-18', '''
<p>Les modalités d’application des articles L. 1234-1 à L. 1234-14 sont fixées par décret en Conseil d’État.</p>
''',
    'Réécriture à droit constant : la phrase place les modalités d’application en tête et conserve la compétence réglementaire ainsi que l’exigence d’un décret en Conseil d’État. Aucune réforme de fond.',
    'L’intervalle L. 1234-1 à L. 1234-14 est conservé intégralement. Coordonner les textes réglementaires de calcul de l’indemnité avec la rédaction réformée de L. 1234-9 et de R. 1234-1, R. 1234-2 et R. 1234-4, notamment la protection de l’ancienneté antérieure ; cette habilitation ne fixe elle-même ni taux ni date d’entrée en vigueur.')

draft('L1234-19', '''
<p>À l’expiration du contrat de travail, l’employeur doit remettre au salarié un certificat de travail. Le contenu de ce certificat est fixé par voie réglementaire.</p>
''',
    'Réécriture à droit constant : l’obligation de remise et la détermination réglementaire du contenu sont exposées en deux phrases dans le même alinéa. Le certificat est désigné explicitement comme certificat de travail. Aucune réforme de fond.',
    'Conserver le fait déclencheur, à savoir l’expiration du contrat, et la détermination réglementaire du contenu. Aucun délai supplémentaire, aucune formalité de demande et aucune liste nouvelle de mentions ne sont créés.')

draft('L1234-20', '''
<p>L’employeur établit le solde de tout compte, qui inventorie les sommes versées au salarié lors de la rupture du contrat de travail. Le salarié en donne reçu à l’employeur.</p>
<p>Le salarié peut dénoncer le reçu pour solde de tout compte dans les six mois suivant sa signature. Passé ce délai, le reçu libère l’employeur pour les seules sommes qui y sont mentionnées.</p>
''',
    'Réécriture à droit constant : les rôles de l’employeur et du salarié sont explicités et le délai de dénonciation est séparé de son effet libératoire. Les deux alinéas sont maintenus. Aucune réforme de fond.',
    'Le délai de six mois court à compter de la signature du reçu ; l’effet libératoire ne couvre que les sommes qui y figurent. Ne pas étendre cet effet à toutes les créances de rupture ni confondre ces six mois avec le plafond proposé pour une composante de l’indemnité légale de licenciement.')

draft('L1235-1', '''
<p>En cas de litige, lors de la conciliation prévue à l’article L. 1411-1, l’employeur et le salarié peuvent convenir d’un accord mettant fin au litige. Le bureau de conciliation et d’orientation peut également proposer un tel accord. Celui-ci prévoit que l’employeur verse au salarié une indemnité forfaitaire, sans préjudice des indemnités légales, conventionnelles ou contractuelles. Son montant est déterminé en référence à un barème fixé par décret en fonction de l’ancienneté du salarié.</p>
<p>Le procès-verbal qui constate cet accord emporte renonciation des parties à toutes les réclamations et indemnités relatives à la rupture du contrat de travail prévues au présent chapitre.</p>
<p>À défaut d’accord, le juge apprécie la régularité de la procédure et le caractère réel et sérieux des motifs invoqués par l’employeur. Il forme sa conviction au vu des éléments fournis par les parties, après avoir ordonné, si nécessaire, les mesures d’instruction qu’il estime utiles.</p>
<p>Le juge justifie, dans son jugement, le montant des indemnités qu’il accorde.</p>
<p>Le doute qui subsiste profite au salarié.</p>
''',
    'Réécriture à droit constant : le premier alinéa distingue l’initiative des parties, la proposition du bureau et le calcul de l’indemnité. Le contrôle du juge est présenté en phrases courtes, en conservant les cinq alinéas, la motivation du montant et le bénéfice du doute. Aucune réforme de fond n’est introduite ici.',
    'Le barème de conciliation reste distinct de l’indemnité légale réformée de L. 1234-9. Le contrôle de la cause réelle et sérieuse et les pouvoirs d’instruction s’appliquent aussi au besoin d’adaptation proposé à L. 1233-3, sans présomption de validité. La renonciation reste limitée aux réclamations et indemnités relatives à la rupture prévues au présent chapitre. ' + HISTORY_2017)

draft('L1235-2', '''
<p>Après la notification de la lettre de licenciement prévue aux articles L. 1232-6, L. 1233-16 et L. 1233-42, l’employeur peut préciser les motifs qui y sont énoncés, de sa propre initiative ou à la demande du salarié. Un décret en Conseil d’État fixe les délais et les conditions de ces précisions.</p>
<p>La lettre de licenciement, complétée le cas échéant par les précisions de l’employeur, fixe les limites du litige quant aux motifs du licenciement.</p>
<p>Si le salarié n’a pas demandé de précisions à l’employeur en application du premier alinéa, l’insuffisance de motivation de la lettre constitue une irrégularité qui, à elle seule, ne prive pas le licenciement de cause réelle et sérieuse. Elle ouvre droit à une indemnité d’au plus un mois de salaire.</p>
<p>Lorsque le licenciement est dépourvu de cause réelle et sérieuse, l’indemnité accordée conformément à l’article L. 1235-3 répare le préjudice résultant du vice de motivation de la lettre de rupture.</p>
<p>Lorsqu’une irrégularité affecte la procédure mais que le licenciement repose sur une cause réelle et sérieuse, le juge accorde au salarié une indemnité, à la charge de l’employeur, d’au plus un mois de salaire. Il en va notamment ainsi lorsque la procédure prévue aux articles L. 1232-2, L. 1232-3, L. 1232-4, L. 1233-11, L. 1233-12 et L. 1233-13 n’a pas été observée, ou lorsque la procédure conventionnelle ou statutaire de consultation préalable au licenciement n’a pas été respectée.</p>
''',
    'Réécriture à droit constant : les conditions de précision des motifs et les différents cas d’indemnisation sont formulés séparément, sans déplacer les cinq alinéas. Les deux plafonds d’un mois et la réparation par L. 1235-3 sont conservés. Aucune réforme de fond.',
    'Le renvoi du troisième alinéa au premier alinéa reste opérant. Les précisions ne deviennent pas un pouvoir de substituer librement un motif à celui de la lettre. Conserver tous les renvois procéduraux et l’alternative entre procédures légale, conventionnelle et statutaire. La note source, fondée sur l’article 40-X de l’ordonnance n° 2017-1387 du 22 septembre 2017, prévoit l’entrée en vigueur à la publication du décret d’application et au plus tard le 1er janvier 2018 ; cette date historique n’est pas une date de réforme future.')

draft('L1235-2-1', '''
<p>Lorsque le licenciement repose sur plusieurs motifs et que l’un des griefs reprochés au salarié porte atteinte à une liberté fondamentale, la nullité encourue de la rupture ne dispense pas le juge d’examiner tous les griefs énoncés. Le juge en tient compte, le cas échéant, pour évaluer l’indemnité due au salarié, sans préjudice de l’article L. 1235-3-1.</p>
''',
    'Réécriture à droit constant : la condition tenant à la pluralité des motifs et l’obligation d’examiner les griefs sont réparties en deux phrases au sein du même alinéa. La nullité et la réserve de L. 1235-3-1 sont maintenues ; aucune réforme de fond.',
    'L’examen des autres griefs ne purge pas la nullité résultant de l’atteinte à une liberté fondamentale et ne supprime pas les garanties de L. 1235-3-1. Le nouveau motif économique d’adaptation ne déroge pas à ces garanties. ' + HISTORY_2017)


def complete_tables(source_xml):
    root = ET.fromstring('<root>' + source_xml + '</root>')
    tables = []
    for table in root.findall('table'):
        rows = []
        for row in table.findall('.//tr'):
            cells = []
            for cell in row:
                assert cell.tag in ('th', 'td')
                content = ' '.join(' '.join(cell.itertext()).split())
                cells.append(f'<{cell.tag}>{content}</{cell.tag}>')
            rows.append('<tr>' + ''.join(cells) + '</tr>')
        tables.append('<table><tbody>\n' + '\n'.join(rows) + '\n</tbody></table>')
    return tables


TABLES_1235_3 = complete_tables(next(s['source_xml'] for s in SOURCES if s['number'] == 'L1235-3'))
assert len(TABLES_1235_3) == 2
draft('L1235-3', '''
<p>Lorsqu’un licenciement est dépourvu de cause réelle et sérieuse, le juge peut proposer la réintégration du salarié dans l’entreprise avec maintien de ses avantages acquis.</p>
<p>Si l’employeur ou le salarié refuse cette réintégration, le juge accorde au salarié une indemnité à la charge de l’employeur. Son montant est compris entre les minimums et les maximums du tableau suivant.</p>
''' + TABLES_1235_3[0] + '''
<p>Lorsque l’entreprise emploie habituellement moins de onze salariés, les minimums du tableau suivant s’appliquent par dérogation aux minimums fixés à l’alinéa précédent :</p>
''' + TABLES_1235_3[1] + '''
<p>Pour fixer le montant de l’indemnité, le juge peut tenir compte, le cas échéant, des indemnités de licenciement versées lors de la rupture, à l’exception de l’indemnité de licenciement mentionnée à l’article L. 1234-9.</p>
<p>Cette indemnité peut se cumuler, le cas échéant, avec celles prévues aux articles L. 1235-12, L. 1235-13 et L. 1235-15, dans la limite des maximums prévus au présent article.</p>
''',
    'Réécriture à droit constant des conditions de réintégration, de fixation et de cumul de l’indemnité, avec des sujets explicites et des phrases plus courtes. Les deux tableaux sont intégralement conservés, cellule par cellule, y compris leurs intitulés, minimums et maximums ; leur contenu chiffré n’est pas présenté comme réformé. Aucune réforme de fond du barème judiciaire.',
    'Conserver les 31 lignes d’ancienneté du premier tableau, de 0 à 30 ans et au-delà, et les 11 lignes du second, de 0 à 10 ans ; « Sans objet », les demi-mois, le maximum de vingt mois et le seuil de moins de onze salariés sont maintenus. Le renvoi à l’alinéa précédent et l’ordre des cinq alinéas et des deux tableaux sont conservés. L’exclusion de L. 1234-9 couvre l’indemnité légale avec ses composantes antérieure et postérieure protégées par la coordination ; le plafond de six mois de la nouvelle composante ne plafonne ni ce barème ni les dommages et intérêts. Le cumul visé au dernier alinéa reste soumis aux maximums du présent article. ' + HISTORY_2017)

draft('L1235-3-1', '''
<p>L’article L. 1235-3 ne s’applique pas lorsque le juge constate que le licenciement est frappé de l’une des nullités prévues au deuxième alinéa du présent article. Si le salarié ne demande pas la poursuite de l’exécution de son contrat de travail ou si sa réintégration est impossible, le juge lui accorde, à la charge de l’employeur, une indemnité au moins égale aux salaires des six derniers mois.</p>
<p>Les nullités mentionnées au premier alinéa concernent :<br />1° La violation d’une liberté fondamentale ;<br />2° Des faits de harcèlement moral ou sexuel, dans les conditions prévues aux articles L. 1152-3 et L. 1153-4 ;<br />3° Un licenciement discriminatoire, dans les conditions prévues aux articles L. 1132-4 et L. 1134-4 ;<br />4° Un licenciement consécutif à une action en justice en matière d’égalité professionnelle entre les femmes et les hommes, dans les conditions prévues à l’article L. 1144-3, ou à une dénonciation de crimes et délits ;<br />5° Un licenciement d’un salarié protégé mentionné aux articles L. 2411-1 et L. 2412-1 en raison de l’exercice de son mandat ;<br />6° Un licenciement d’un salarié en méconnaissance des protections prévues aux articles L. 1225-71 et L. 1226-13.</p>
<p>L’indemnité est due sans préjudice du salaire que le salarié aurait perçu pendant la période couverte par la nullité, lorsque ce salaire est dû en application de l’article L. 1225-71 et du statut protecteur dont bénéficient certains salariés en application du chapitre Ier du titre Ier du livre IV de la deuxième partie du code du travail. Elle est également due, le cas échéant, sans préjudice de l’indemnité de licenciement légale, conventionnelle ou contractuelle.</p>
''',
    'Réécriture à droit constant : l’exclusion du barème, le minimum d’indemnisation et le maintien éventuel du salaire sont exprimés plus directement. Les trois alinéas et les six subdivisions du deuxième alinéa sont conservés. Aucune réforme de fond ; les protections contre les licenciements nuls demeurent intégrales.',
    'Le minimum correspond aux salaires des six derniers mois et ne constitue pas un plafond. Le deuxième alinéa reste une seule unité contenant les 1° à 6°, pour préserver les renvois internes et celui de L. 1235-3-2. La condition légale du rappel de salaire, son champ protecteur et les trois sources possibles d’indemnité de licenciement sont conservés. Ne pas étendre à cette réparation le plafond proposé à L. 1234-9. ' + HISTORY_2017)

draft('L1235-3-2', '''
<p>Lorsque le juge prononce la rupture du contrat de travail aux torts de l’employeur, ou lorsque la rupture fait suite à une demande du salarié dans la procédure prévue à l’article L. 1451-1, le montant de l’indemnité accordée est fixé selon les règles de l’article L. 1235-3. Toutefois, si la rupture produit les effets d’un licenciement nul dans l’un des cas prévus aux 1° à 6° de l’article L. 1235-3-1, le premier alinéa de l’article L. 1235-3-1 s’applique.</p>
''',
    'Réécriture à droit constant : la règle de calcul et son exception pour licenciement nul sont séparées en deux phrases dans le même alinéa. Les deux modalités de rupture et les renvois sont conservés. Aucune réforme de fond.',
    'Maintenir le renvoi à la procédure de L. 1451-1, l’ensemble des 1° à 6° de L. 1235-3-1 et son premier alinéa. Le barème ordinaire et le régime des nullités ne sont pas remplacés par le plafond de l’indemnité légale réformée. ' + HISTORY_2017)

draft('L1235-4', '''
<p>Dans les cas prévus aux articles L. 1132-4, L. 1134-4, L. 1144-3, L. 1152-3, L. 1153-4, L. 1235-3 et L. 1235-11, le juge ordonne à l’employeur fautif de rembourser aux organismes intéressés tout ou partie des indemnités de chômage versées au salarié licencié entre le jour de son licenciement et celui du jugement. Le remboursement est limité à six mois d’indemnités de chômage par salarié intéressé.</p>
<p>Le juge ordonne ce remboursement d’office lorsque les organismes intéressés ne sont pas intervenus à l’instance ou n’ont pas indiqué le montant des indemnités versées.</p>
<p>Pour obtenir le remboursement prévu au premier alinéa, le directeur général de l’opérateur France Travail, ou la personne qu’il désigne au sein de cet opérateur, peut délivrer une contrainte après mise en demeure, dans les délais et conditions fixés par décret en Conseil d’État. Il agit pour le compte de l’opérateur France Travail, de l’organisme chargé de gérer le régime d’assurance chômage mentionné à l’article L. 5427-1, de l’État ou des employeurs mentionnés à l’article L. 5424-1. Si le débiteur ne forme pas opposition devant la juridiction compétente, la contrainte produit tous les effets d’un jugement et confère le bénéfice de l’hypothèque judiciaire.</p>
''',
    'Réécriture à droit constant : la période remboursable et son plafond sont distingués, puis le mécanisme de contrainte est décomposé en trois phrases dans le troisième alinéa. Les sept cas de renvoi, les bénéficiaires et les garanties procédurales sont conservés. Aucune réforme de fond.',
    'Le maximum de six mois porte sur les indemnités de chômage remboursées aux organismes ; il est distinct de l’indemnité de licenciement et des minima pour licenciement nul. Maintenir les exceptions prévues à L. 1235-5, la mise en demeure préalable, le droit d’opposition et l’effet hypothécaire. La note source fixe l’entrée en vigueur au 1er janvier 2024 selon le V de l’article 6 de la loi n° 2023-1196 du 18 décembre 2023 ; aucune nouvelle date n’en est déduite.')

draft('L1235-5', '''
<p>En cas de méconnaissance des articles L. 1235-3 et L. 1235-11, le remboursement des indemnités de chômage prévu à l’article L. 1235-4 ne s’applique ni au licenciement d’un salarié ayant moins de deux ans d’ancienneté dans l’entreprise, ni au licenciement effectué dans une entreprise qui emploie habituellement moins de onze salariés.</p>
''',
    'Réécriture à droit constant : l’exclusion du remboursement est énoncée directement et les deux catégories de licenciement sont présentées avec « ni… ni… ». Les seuils et les cas concernés restent identiques ; aucune réforme de fond.',
    'Les deux exclusions sont alternatives, non cumulatives : moins de deux ans d’ancienneté ou entreprise employant habituellement moins de onze salariés. Elles restent limitées aux cas de méconnaissance de L. 1235-3 et L. 1235-11, sans être étendues aux autres cas de L. 1235-4. ' + HISTORY_2017)

draft('L1235-6', '''
<p>Les modalités d’application de la présente section sont fixées par décret en Conseil d’État.</p>
''',
    'Réécriture à droit constant : la phrase est réorganisée autour des modalités d’application tout en maintenant le niveau du décret et le périmètre de la section. Aucune réforme de fond.',
    'Le renvoi couvre la présente section seulement ; il ne crée pas d’habilitation à modifier les seuils légaux, les barèmes ou les protections contre les nullités.')

draft('L1235-7', '''
<p>Toute contestation d’un licenciement pour motif économique se prescrit par douze mois à compter de la dernière réunion du comité social et économique. Toutefois, lorsque le salarié exerce son droit individuel de contester ce licenciement, ce délai court à compter de la notification du licenciement.</p>
''',
    'Réécriture à droit constant : les deux points de départ du même délai de douze mois sont exposés en deux phrases dans l’alinéa d’origine, en distinguant expressément le recours individuel du salarié. Aucune réforme de fond.',
    'Articuler ce délai avec le recours administratif spécial de L. 1235-7-1 sans les confondre. La note source fondée sur l’article 40-II de l’ordonnance n° 2017-1387 du 22 septembre 2017 maintient les règles suivantes : application aux prescriptions en cours à compter de la publication de l’ordonnance, sans que la durée totale puisse dépasser celle prévue par la loi antérieure ; pour une instance introduite avant cette publication, poursuite et jugement selon la loi ancienne, y compris en appel et en cassation. Ces transitions historiques sont conservées et ne fixent pas l’entrée en vigueur d’une réforme future.')

draft('L1235-7-1', '''
<p>L’accord collectif mentionné à l’article L. 1233-24-1, le document élaboré par l’employeur mentionné à l’article L. 1233-24-4, le contenu du plan de sauvegarde de l’emploi, les décisions prises par l’administration au titre de l’article L. 1233-57-5 et la régularité de la procédure de licenciement collectif ne peuvent être contestés dans un litige distinct de celui portant sur la décision de validation ou d’homologation mentionnée à l’article L. 1233-57-4.</p>
<p>Ces litiges relèvent en premier ressort du tribunal administratif, à l’exclusion de tout autre recours administratif ou contentieux.</p>
<p>L’employeur dispose de deux mois à compter de la notification de la décision de validation ou d’homologation pour présenter son recours. Les organisations syndicales et les salariés disposent du même délai à compter de la date à laquelle cette décision est portée à leur connaissance conformément à l’article L. 1233-57-4.</p>
<p>Le tribunal administratif statue dans les trois mois. S’il ne s’est pas prononcé à l’expiration de ce délai, ou en cas d’appel, le litige est porté devant la cour administrative d’appel. Celle-ci statue dans les trois mois. Si elle ne s’est pas prononcée à l’expiration de ce délai, ou en cas de pourvoi en cassation, le litige est porté devant le Conseil d’État.</p>
<p>Le livre V du code de justice administrative s’applique.</p>
''',
    'Réécriture à droit constant : le recours unique est exprimé par le verbe contester ; les délais propres aux auteurs du recours puis à chaque degré de juridiction sont formulés dans des phrases distinctes. Les cinq alinéas, objets du contrôle et voies de recours sont conservés. Aucune réforme de fond.',
    'Maintenir le délai de recours de deux mois, ses points de départ distincts, les deux délais juridictionnels de trois mois et les saisines en cas de dépassement ou de recours. Le livre V du code de justice administrative demeure applicable. La compétence relative à la décision de validation ou d’homologation ne doit pas être étendue à tout litige individuel sur la cause du licenciement, y compris au titre du nouveau besoin d’adaptation de L. 1233-3.')

draft('L1235-8', '''
<p>Les organisations syndicales de salariés représentatives peuvent exercer en justice toutes les actions qui résultent des dispositions légales ou conventionnelles régissant le licenciement pour motif économique d’un salarié. Elles n’ont pas à justifier d’un mandat de ce salarié.</p>
<p>L’organisation syndicale avertit le salarié de son intention d’agir dans les conditions fixées par voie réglementaire. Elle ne peut exercer l’action que si le salarié ne s’y est pas opposé dans un délai de quinze jours à compter de la notification de cette intention par l’organisation syndicale.</p>
<p>À l’issue de ce délai, l’organisation syndicale avertit l’employeur de son intention d’agir en justice.</p>
<p>Le salarié peut intervenir à tout moment dans l’instance engagée par le syndicat.</p>
''',
    'Réécriture à droit constant : les actes du syndicat, le droit d’opposition du salarié et l’absence de mandat sont formulés explicitement, en conservant les quatre alinéas. Le délai de quinze jours et le droit permanent d’intervention demeurent ; aucune réforme de fond.',
    'L’action appartient aux organisations syndicales de salariés représentatives. Le délai d’opposition court à compter de la notification au salarié de l’intention du syndicat ; l’information de l’employeur reste postérieure à l’expiration de ce délai. Aucun accord exprès du salarié ni mandat nouveau n’est exigé.')

draft('L1235-9', '''
<p>Lorsqu’un recours porte sur un licenciement pour motif économique, l’employeur communique au juge tous les éléments transmis aux représentants du personnel en application du chapitre III. Si l’entreprise n’a pas de représentants du personnel, il communique tous les éléments transmis à l’autorité administrative en application de ce même chapitre.</p>
<p>Les modalités d’application du présent article sont fixées par décret en Conseil d’État.</p>
''',
    'Réécriture à droit constant : la communication des éléments au juge est présentée en deux phrases selon la présence ou l’absence de représentants du personnel. Les deux alinéas, l’exhaustivité des éléments à transmettre et le décret en Conseil d’État sont maintenus. Aucune réforme de fond.',
    'Le chapitre III reste la référence pour les deux circuits de transmission. Le nouveau motif d’adaptation proposé à L. 1233-3 demeure soumis aux obligations de documentation de cet article, au présent dispositif de communication et au contrôle de L. 1235-1 ; aucune dispense de preuve ou d’information n’est créée.')

draft('L1235-10', '''
<p>Dans une entreprise d’au moins cinquante salariés, lorsque le projet de licenciement concerne au moins dix salariés au cours d’une même période de trente jours, le licenciement est nul s’il intervient sans aucune décision de validation ou d’homologation, ou alors qu’une décision négative a été rendue.</p>
<p>La procédure de licenciement est nulle lorsque la décision de validation mentionnée à l’article L. 1233-57-2 ou la décision d’homologation mentionnée à l’article L. 1233-57-3 est annulée en raison de l’absence ou de l’insuffisance du plan de sauvegarde de l’emploi mentionné à l’article L. 1233-61.</p>
<p>Les deux premiers alinéas ne s’appliquent pas aux entreprises en redressement ou en liquidation judiciaires.</p>
''',
    'Réécriture à droit constant : les conditions et conséquences de chaque cas de nullité sont exprimées directement. L’exclusion concernant les procédures collectives est matérialisée comme troisième alinéa, conformément à son emplacement et au renvoi aux deux premiers alinéas dans la source. Aucune réforme de fond.',
    'Conserver les trois seuils : au moins cinquante salariés, au moins dix licenciements projetés et même période de trente jours. Les renvois de validation et d’homologation sont vérifiés dans le corpus. La distinction préexistante entre nullité du licenciement au premier alinéa et nullité de la procédure au deuxième est conservée : son articulation avec L. 1235-11, qui vise la nullité de la procédure au titre des deux premiers alinéas, doit être contrôlée sans harmonisation silencieuse. L’exception des entreprises en redressement ou liquidation judiciaires vise les deux premiers alinéas seulement.')

draft('L1235-11', '''
<p>Lorsque le juge constate que le licenciement est intervenu dans le cadre d’une procédure nulle en application des deux premiers alinéas de l’article L. 1235-10, il peut ordonner la poursuite du contrat de travail ou prononcer la nullité du licenciement et ordonner, à la demande du salarié, sa réintégration. Cette réintégration ne peut toutefois être ordonnée si elle est devenue impossible, notamment en raison de la fermeture de l’établissement ou du site ou de l’absence d’emploi disponible.</p>
<p>Si le salarié ne demande pas la poursuite de son contrat de travail, ou si sa réintégration est impossible, le juge lui accorde, à la charge de l’employeur, une indemnité au moins égale aux salaires des six derniers mois.</p>
''',
    'Réécriture à droit constant : les pouvoirs du juge et les obstacles à la réintégration sont exposés en phrases distinctes dans le premier alinéa. Le second conserve l’alternative ouvrant droit à l’indemnité et le minimum de six derniers mois de salaire. Aucune réforme de fond.',
    'Conserver le caractère non exhaustif des exemples d’impossibilité, la demande du salarié pour la réintégration et la faculté du juge. L. 1235-14 comporte des exclusions à articuler avec cet article. Le renvoi aux deux premiers alinéas de L. 1235-10 est maintenu malgré leur différence de formulation sur l’objet de la nullité, signalée dans la note de cet article. Le minimum de six derniers mois n’est pas le plafond de la nouvelle composante d’indemnité légale de L. 1234-9. ' + HISTORY_2017)

draft('L1235-12', '''
<p>Lorsque l’employeur ne respecte pas les procédures de consultation des représentants du personnel ou d’information de l’autorité administrative, le juge accorde au salarié concerné par un licenciement collectif pour motif économique une indemnité à la charge de l’employeur. Il en calcule le montant en fonction du préjudice subi.</p>
''',
    'Réécriture à droit constant : le manquement, le bénéficiaire de l’indemnité et son mode d’évaluation sont exposés dans deux phrases du même alinéa. Les deux procédures et le champ du licenciement collectif économique sont conservés. Aucune réforme de fond.',
    'Aucun minimum ni plafond autonome n’est ajouté à l’indemnité calculée selon le préjudice. Le cumul avec l’indemnité de L. 1235-3 reste soumis aux maximums prévus par cet article. Les obligations de consultation et d’information ne disparaissent pas pour un licenciement reposant sur le motif d’adaptation proposé.')

draft('L1235-13', '''
<p>Si la priorité de réembauche prévue à l’article L. 1233-45 n’est pas respectée, le juge accorde au salarié une indemnité d’au moins un mois de salaire.</p>
''',
    'Réécriture à droit constant : la condition de sanction est formulée directement et le montant minimal est exprimé par « au moins ». Le renvoi et le mois de salaire sont conservés. Aucune réforme de fond.',
    'Conserver l’articulation avec les exclusions de L. 1235-14 et la limite de cumul prévue à L. 1235-3. Le minimum est exprimé en mois de salaire, sans ajout d’une qualification brute ou nette absente de la source. ' + HISTORY_2017)

draft('L1235-14', '''
<p>Les sanctions suivantes ne s’appliquent ni au licenciement d’un salarié ayant moins de deux ans d’ancienneté dans l’entreprise, ni au licenciement effectué par un employeur qui emploie habituellement moins de onze salariés :</p>
<p>1° Les sanctions de la nullité du licenciement prévues à l’article L. 1235-11 ;</p>
<p>2° (supprimé) ;</p>
<p>3° Les sanctions du non-respect de la priorité de réembauche prévues à l’article L. 1235-13.</p>
<p>En cas de licenciement abusif, le salarié peut obtenir une indemnité correspondant au préjudice qu’il a subi.</p>
''',
    'Réécriture à droit constant : les deux catégories exclues sont formulées avec « ni… ni… » et les sanctions sont désignées explicitement dans les subdivisions. Les cinq alinéas, la place du 2° supprimé et la réparation du préjudice sont conservés. Aucune réforme de fond.',
    'Les seuils de moins de deux ans et de moins de onze salariés constituent deux exclusions alternatives. Ne pas renuméroter le 3° ni effacer la subdivision 2° supprimée. Tension préexistante à contrôler : la réserve finale d’une réparation du licenciement abusif selon le préjudice doit être articulée avec le barème de L. 1235-3, qui comporte déjà des minimums propres aux entreprises de moins de onze salariés ; aucune dérogation nouvelle au barème n’est créée ni supprimée ici. ' + HISTORY_2017)


assert len(SOURCES) == 24
assert len(DRAFTS) == 24
assert {s['number'] for s in SOURCES} == set(DRAFTS)
Path('fragments').mkdir(exist_ok=True)
answer = []
for source in SOURCES:
    proposed = DRAFTS[source['number']]
    Path('fragments', source['number'] + '.xml').write_text(proposed['proposed_xml'] + '\n')
    answer.append({
        **{k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')},
        **proposed,
    })
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles rédigés')
