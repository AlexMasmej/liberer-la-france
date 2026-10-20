import json
from html.parser import HTMLParser
from pathlib import Path

class PlainText(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]
    def handle_data(self,data): self.parts.append(data)
    def handle_endtag(self,tag):
        if tag in {'p','div'}: self.parts.append(' ')
    def handle_starttag(self,tag,attrs):
        if tag=='br': self.parts.append(' ')

def plain(xml):
    p=PlainText(); p.feed(xml or ''); return ' '.join(''.join(p.parts).split())

D={}
def add(number,xml,reason,notes):
    assert number not in D
    D[number]=(xml.strip(),reason,notes)

add('L1237-16', '''
<p>Les dispositions de la présente section ne s'appliquent pas aux ruptures de contrats de travail qui résultent :</p>
<p>1° Des accords issus de la négociation mentionnée aux articles L. 2242-20 et L. 2242-21 ;</p>
<p>2° Des plans de sauvegarde de l'emploi, dans les conditions définies à l'article L. 1233-61 ;</p>
<p>3° Des accords collectifs mentionnés à l'article L. 1237-17.</p>
''', "Réécriture à droit constant : la portée de l'exclusion est exprimée directement, puis les trois catégories de ruptures sont présentées dans leur ordre initial. Aucune réforme de fond.",
"Les 1°, 2° et 3° et leurs renvois sont conservés. L'exclusion vise la section 3 relative à la rupture conventionnelle ; elle ne soustrait pas les accords de L. 1237-17 aux règles propres de la section 4. La réforme du motif économique ne modifie pas cette délimitation.")

add('L1237-17', '''
<p>Un accord collectif portant sur la gestion prévisionnelle des emplois et des compétences ou sur la rupture conventionnelle collective peut fixer les conditions et les modalités dans lesquelles l'employeur et le salarié rompent d'un commun accord le contrat de travail qui les lie.<br /><br />Ces ruptures sont exclusives du licenciement et de la démission. Ni l'employeur ni le salarié ne peut les imposer à l'autre. Les dispositions de la présente section leur sont applicables.</p>
''', "Réécriture à droit constant : les deux objets possibles de l'accord sont distingués et l'interdiction d'imposer la rupture est formulée en nommant les deux parties. Le caractère commun du consentement et l'application de la section sont maintenus. Aucune réforme de fond.",
"Conserver le champ des accords de gestion prévisionnelle des emplois et des compétences et de rupture conventionnelle collective. Les réformes de l'embauche et du licenciement économique n'autorisent pas à imposer ces ruptures. Le renvoi depuis L. 1237-16, 3°, reste opérant.")

add('L1237-18', '''
<p>L'employeur peut proposer un congé de mobilité soit dans le cadre d'un accord portant rupture conventionnelle collective conclu dans les conditions prévues aux articles L. 1237-19 à L. 1237-19-8, soit dans une entreprise ayant conclu un accord collectif portant sur la gestion des emplois et des compétences.</p>
<p>Ce congé vise à favoriser le retour à un emploi stable au moyen de mesures d'accompagnement, d'actions de formation et de périodes de travail.</p>
''', "Réécriture à droit constant : l'employeur est placé en sujet de la faculté de proposition et les deux cadres collectifs sont explicités. L'objectif de stabilité de l'emploi et les trois moyens d'action sont conservés. Aucune réforme de fond.",
"Maintien des deux alinéas et de l'ensemble du renvoi aux articles L. 1237-19 à L. 1237-19-8. Le congé de mobilité reste distinct de la période de reconversion mentionnée au 4° ter de L. 1237-19-1 et du congé de reclassement.")

add('L1237-18-1', '''
<p>Le salarié peut accomplir les périodes de travail prévues pendant le congé de mobilité dans l'entreprise qui lui a proposé ce congé ou en dehors de celle-ci.</p>
<p>Ces périodes peuvent s'effectuer dans le cadre d'un contrat de travail à durée indéterminée ou d'un contrat de travail à durée déterminée conclu en application du 1° de l'article L. 1242-3, dans la limite fixée par l'accord collectif. Lorsqu'un tel contrat à durée déterminée est conclu, le congé de mobilité est suspendu. Il reprend à l'issue de ce contrat pour la durée restant à courir.</p>
''', "Réécriture à droit constant : le salarié est désigné comme l'auteur des périodes de travail et le cas du contrat à durée déterminée est repris explicitement avant d'exposer la suspension puis la reprise du congé. Aucune réforme de fond.",
"Les deux lieux possibles, le CDI, le CDD fondé sur le 1° de L. 1242-3 et sa limite conventionnelle sont préservés. La suspension et la reprise pour la durée restante concernent le cas du CDD ; elles ne sont pas étendues au CDI. Le régime d'essai des nouveaux CDI se traite dans ses articles propres.")

add('L1237-18-2', '''
<p>L'accord collectif fixe :</p>
<p>1° La durée du congé de mobilité ;</p>
<p>2° Les conditions que le salarié doit remplir pour bénéficier de ce congé ;</p>
<p>3° Les modalités selon lesquelles le salarié adhère à la proposition de l'employeur, y compris les conditions dans lesquelles il exprime son consentement écrit, ainsi que les engagements de chaque partie ;</p>
<p>4° L'organisation des périodes de travail, les conditions dans lesquelles le congé prend fin et les modalités d'accompagnement des actions de formation envisagées ;</p>
<p>5° Le montant de la rémunération versée pendant le congé de mobilité ;</p>
<p>6° Les conditions dans lesquelles les institutions représentatives du personnel sont informées ;</p>
<p>7° Les indemnités de rupture garanties au salarié. Leur montant ne peut être inférieur à celui des indemnités légales dues en cas de licenciement pour motif économique. Pour l'indemnité prévue à l'article L. 1234-9, ce minimum est calculé selon les règles de cet article, y compris celles qui protègent la part correspondant à l'ancienneté acquise avant l'entrée en vigueur de sa nouvelle rédaction.</p>
''', "Réécriture des sept clauses obligatoires : le consentement écrit, les engagements et les modalités du congé sont rendus plus explicites. Coordination de fond au 7° avec la réforme de L. 1234-9 : le minimum de rupture intègre la protection de l'ancienneté antérieure, sans plafonnement global de l'indemnité ni modification des autres clauses.",
"Les sept numéros restent en place. Coordonner l'entrée en vigueur du 7° avec L. 1234-9 et R. 1234-1, R. 1234-2 et R. 1234-4 : 0,20 mois par année et plafond de six mois pour la seule part d'ancienneté postérieure ; la part antérieure s'ajoute et conserve son barème, avec salaire de référence déterminé à la rupture. Aucun taux nouveau n'est fixé ici et aucune date future n'est inventée. La diminution du minimum légal ne réécrit pas les garanties des accords déjà conclus. Le plancher reste celui du licenciement pour motif économique ; le besoin d'adaptation de L. 1233-3 ne devient pas une condition de ce départ amiable.")

add('L1237-18-3', '''
<p>Pendant le congé de mobilité, le salarié reçoit une rémunération au moins égale au montant de l'allocation prévue au 3° de l'article L. 5123-2.</p>
<p>Dans la limite des douze premiers mois du congé, cette rémunération relève du même régime social que l'allocation versée au bénéficiaire du congé de reclassement prévue au dernier alinéa de l'article L. 1233-72. Cette limite peut être portée à vingt-quatre mois en cas de formation de reconversion professionnelle.</p>
''', "Réécriture à droit constant : le salarié bénéficiaire est nommé et la limite d'application du régime social est séparée de sa possible extension pour reconversion. Le minimum de rémunération est toujours défini par renvoi. Aucune réforme de fond.",
"Conservation du 3° de L. 5123-2 et du dernier alinéa de L. 1233-72, vérifiés dans le corpus public. Les douze mois, pouvant être portés à vingt-quatre mois en cas de formation de reconversion professionnelle, limitent le régime social mentionné, non le montant minimal de rémunération ni la durée générale du congé. L'extension reste une possibilité. Ne pas appliquer à cette rémunération le plafond de six mois de l'indemnité de licenciement.")

add('L1237-18-4', '''
<p>Lorsque le salarié accepte la proposition de congé de mobilité, son contrat de travail est rompu d'un commun accord des parties à l'issue du congé.<br /><br />Les salariés qui bénéficient d'une protection mentionnée au chapitre Ier du titre Ier du livre IV de la deuxième partie peuvent bénéficier d'un congé de mobilité. Pour ces salariés, par dérogation au premier alinéa du présent article, la rupture amiable dans le cadre de ce congé nécessite l'autorisation de l'inspecteur du travail, dans les conditions prévues au chapitre Ier du titre II du livre IV de la deuxième partie. Le contrat de travail ne peut alors être rompu que le lendemain du jour de l'autorisation.<br /><br />Pour les médecins du travail, la rupture du contrat nécessite l'autorisation de l'inspecteur du travail, qui se prononce après avis du médecin inspecteur du travail.</p>
''', "Réécriture à droit constant : les effets de l'acceptation, la dérogation pour les salariés protégés et l'autorisation propre aux médecins du travail sont exprimés dans des phrases plus courtes. Les trois alinéas matérialisés par les sauts de ligne sont maintenus. Aucune réforme de fond.",
"Maintien du terme à l'issue du congé, des deux références à la deuxième partie du code, de l'autorisation administrative et de l'avis du médecin inspecteur du travail. Le renvoi au premier alinéa reste à la même place. La source dit « que le lendemain du jour de l'autorisation » ; cette formulation est conservée sans la transformer en une faculté générale de rupture à toute date ultérieure. Coordination avec le renvoi de L. 1237-19-2.")

add('L1237-18-5', '''
<p>L'employeur informe l'autorité administrative des ruptures prononcées dans le cadre du congé de mobilité. L'autorité compétente est celle du lieu où est établie l'entreprise concernée par l'accord de gestion prévisionnelle des emplois et des compétences. Un décret fixe les conditions de cette information.</p>
''', "Réécriture à droit constant : l'employeur est désigné comme débiteur de l'information et le rôle du décret est présenté dans une phrase distincte. La compétence territoriale et le cadre de l'accord sont maintenus. Aucune réforme de fond.",
"L'information demeure adressée à l'autorité du lieu d'établissement de l'entreprise concernée par l'accord de gestion prévisionnelle des emplois et des compétences. Aucun délai ni formulaire supplémentaire n'est créé ; les conditions restent définies par décret. Ne pas confondre cette information sur les ruptures avec la validation de l'accord de rupture conventionnelle collective.")

add('L1237-19', '''
<p>Un accord collectif peut fixer le contenu d'une rupture conventionnelle collective. Pour atteindre les objectifs de suppression d'emplois assignés à ce dispositif, tout licenciement est exclu.<br /><br />L'administration est informée sans délai de l'ouverture de la négociation de cet accord.</p>
''', "Réécriture à droit constant : le contenu de l'accord et l'exclusion du licenciement pour atteindre ses objectifs sont exprimés dans deux phrases. L'information immédiate de l'administration reste dans le second alinéa. Aucune réforme de fond.",
"L'interdiction du licenciement est rattachée aux objectifs de suppression d'emplois du dispositif, sans en faire une interdiction générale de tout licenciement dans l'entreprise. Le délai reste « sans délai ». La source ne désigne pas expressément l'auteur de cette information ; aucun auteur supplémentaire n'est imposé par cette réécriture.")

add('L1237-19-1', '''
<p>L'accord portant rupture conventionnelle collective fixe :</p>
<p>1° Les modalités et les conditions dans lesquelles le comité social et économique est informé, s'il existe ;</p>
<p>2° Le nombre maximal de départs envisagés et de suppressions d'emplois associées, ainsi que la durée pendant laquelle des ruptures de contrat de travail peuvent être engagées sur le fondement de cet accord ;</p>
<p>3° Les conditions que le salarié doit remplir pour bénéficier du dispositif ;</p>
<p>4° Les modalités de présentation et d'examen des candidatures des salariés au départ, y compris les conditions de transmission du consentement écrit du salarié à participer au dispositif prévu par l'accord collectif ;</p>
<p>4° bis Les modalités selon lesquelles l'employeur et le salarié concluent une convention individuelle de rupture et les parties exercent leur droit de rétractation ;</p>
<p>4° ter Le cas échéant, les modalités selon lesquelles l'employeur et le salarié concluent une convention individuelle de rupture dans le cadre de la période de reconversion mentionnée à l'article L. 6324-1 ;</p>
<p>5° Les modalités de calcul des indemnités de rupture garanties au salarié. Leur montant ne peut être inférieur à celui des indemnités légales dues en cas de licenciement. Pour l'indemnité prévue à l'article L. 1234-9, ce minimum est calculé selon les règles de cet article, y compris celles qui protègent la part correspondant à l'ancienneté acquise avant l'entrée en vigueur de sa nouvelle rédaction ;</p>
<p>6° Les critères permettant de départager les candidats potentiels au départ ;</p>
<p>7° Les mesures destinées à faciliter l'accompagnement et le reclassement externe des salariés sur des emplois équivalents. Ces mesures peuvent notamment prendre la forme d'un congé de mobilité dans les conditions prévues aux articles L. 1237-18-1 à L. 1237-18-5, d'actions de formation, de validation des acquis de l'expérience ou de reconversion, ou d'actions soutenant la création d'activités nouvelles ou la reprise d'activités existantes par les salariés ;</p>
<p>7° bis Le cas échéant, les mesures mentionnées au II de l'article L. 6324-9 ;</p>
<p>8° Les modalités de suivi de la mise en œuvre effective de l'accord portant rupture conventionnelle collective.</p>
<p>En application du X de l'article 40 et du III de l'article 10 de l'ordonnance n° 2017-1387 du 22 septembre 2017, les dispositions issues de l'article 10 de cette ordonnance qui nécessitent des mesures d'application entrent en vigueur à la date de publication des décrets d'application et, au plus tard, le 1er janvier 2018.</p>
''', "Réécriture de chaque clause obligatoire, avec des sujets explicites pour l'information, la convention individuelle et la rétractation. Les 4° bis, 4° ter et 7° bis sont conservés, comme les exemples d'accompagnement et l'alinéa historique final. Coordination de fond au seul 5° avec la réforme de L. 1234-9, en préservant expressément sa part d'ancienneté antérieure.",
"Numérotation et ordre de tous les alinéas conservés : les renvois au 7° depuis L. 1237-19-3 demeurent exacts. Le minimum du 5° intègre le calcul en deux parts de L. 1234-9 et R. 1234-1, R. 1234-2 et R. 1234-4 : 0,20 mois par année et plafond de six mois pour la seule ancienneté nouvelle ; part antérieure protégée et ajoutée, salaire de référence à la rupture. La baisse du minimum ne diminue pas les montants déjà garantis par un accord. La date commune de la réforme doit être fixée dans ses dispositions d'entrée en vigueur, sans utiliser les dates historiques de 2018 ou de 2026. L'alinéa relatif à l'ordonnance de 2017 figure déjà dans source_xml, alors que d'autres articles le portent en note : son emplacement est maintenu et cette particularité éditoriale est signalée. Les renvois à L. 6324-1 et au II de L. 6324-9 ont été vérifiés ; leurs règles transitoires propres aux actions déjà engagées ne sont pas remplacées par celles de l'indemnité légale.")

add('L1237-19-2', '''
<p>Lorsque l'employeur accepte la candidature du salarié à la rupture conventionnelle collective, le contrat de travail est rompu d'un commun accord des parties, le cas échéant dans les conditions prévues à l'article L. 1237-18-4.<br /><br />Les salariés qui bénéficient d'une protection mentionnée au chapitre Ier du titre Ier du livre IV de la deuxième partie peuvent bénéficier de l'accord portant rupture conventionnelle collective. Pour ces salariés, par dérogation au premier alinéa du présent article, la rupture d'un commun accord dans le cadre de ce dispositif nécessite l'autorisation de l'inspecteur du travail, dans les conditions prévues au chapitre Ier du titre II du livre IV de la deuxième partie. Le contrat de travail ne peut alors être rompu que le lendemain du jour de l'autorisation.<br /><br />Pour les médecins du travail, la rupture du contrat nécessite l'autorisation de l'inspecteur du travail, qui se prononce après avis du médecin inspecteur du travail.</p>
''', "Réécriture à droit constant : l'effet de l'acceptation est formulé directement, puis les autorisations applicables aux salariés protégés et aux médecins du travail sont exposées séparément. Les trois alinéas matérialisés par des sauts de ligne sont maintenus. Aucune réforme de fond.",
"Conserver le renvoi éventuel à L. 1237-18-4, les deux références à la deuxième partie et la dérogation au premier alinéa. L'acceptation patronale ne supprime ni les modalités de convention individuelle ni le droit de rétractation du 4° bis de L. 1237-19-1. La formule source « que le lendemain du jour de l'autorisation » est conservée sans élargissement ; l'avis du médecin inspecteur du travail reste préalable à l'autorisation concernant un médecin du travail.")

add('L1237-19-3', '''
<p>L'accord collectif mentionné à l'article L. 1237-19 est transmis à l'autorité administrative afin qu'elle le valide.</p>
<p>L'autorité administrative valide cet accord lorsqu'elle a vérifié :<br /><br />1° Qu'il est conforme à l'article L. 1237-19 ;<br /><br />2° Qu'il contient les clauses prévues à l'article L. 1237-19-1 ;<br /><br />3° Que les mesures prévues au 7° de l'article L. 1237-19-1 sont précises et concrètes ;<br /><br />4° Le cas échéant, que la procédure d'information du comité social et économique est régulière.</p>
''', "Réécriture à droit constant : chacun des quatre contrôles est formulé comme une vérification explicite de l'autorité administrative. La transmission préalable et les deux alinéas de la source sont conservés. Aucune réforme de fond.",
"Le contrôle de présence porte sur toutes les clauses de L. 1237-19-1, notamment les 4° ter et 7° bis. Le contrôle du caractère précis et concret reste expressément rattaché au 7°, sans extension silencieuse au 7° bis. Si le législateur souhaite ce contrôle spécifique supplémentaire, L. 1237-19-3, 3°, devra être modifié expressément. Le contrôle de régularité de l'information du comité reste conditionnel.")

add('L1237-19-4', '''
<p>L'autorité administrative dispose de quinze jours à compter de la réception de l'accord collectif mentionné à l'article L. 1237-19 pour notifier sa décision de validation à l'employeur.</p>
<p>Dans ce même délai, elle notifie sa décision au comité social et économique, s'il existe, et aux signataires de l'accord. Elle motive sa décision.</p>
<p>Si l'autorité administrative garde le silence jusqu'à l'expiration du délai prévu au premier alinéa, l'accord est réputé validé. Dans ce cas, l'employeur transmet au comité social et économique, s'il existe, et aux signataires de l'accord une copie de la demande de validation accompagnée de l'accusé de réception délivré par l'administration.</p>
<p>Les salariés sont informés de la décision de validation ou, à défaut, des documents mentionnés au troisième alinéa, ainsi que des voies et délais de recours. Cette information est donnée par affichage sur leurs lieux de travail ou par tout autre moyen lui conférant une date certaine.</p>
''', "Réécriture à droit constant : le délai de notification, la validation tacite et les documents à transmettre dans ce cas sont exprimés directement. L'information des salariés et l'exigence de date certaine sont regroupées dans le quatrième alinéa, sans déplacement des alinéas ciblés. Aucune réforme de fond.",
"Les quatre alinéas restent dans le même ordre. Maintien des quinze jours à compter de la réception de l'accord, du même délai pour le comité et les signataires, de la motivation et de l'effet positif du silence. Les renvois au premier et au troisième alinéa sont conservés. La copie de la demande et son accusé de réception restent tous deux requis en cas de validation tacite ; les voies et délais de recours sont portés à la connaissance des salariés dans les deux cas.")

add('L1237-19-5', '''
<p>La validation relève de l'autorité administrative du lieu où l'entreprise ou l'établissement concerné par le projet d'accord portant rupture conventionnelle collective est établi. Lorsque le projet concerne des établissements relevant d'autorités différentes, un décret en Conseil d'Etat fixe les conditions de désignation de l'autorité administrative compétente.</p>
''', "Réécriture à droit constant : la règle de compétence territoriale est exprimée directement et la désignation en présence de plusieurs autorités est isolée dans une seconde phrase. Aucune réforme de fond.",
"L'alternative entre entreprise et établissement est conservée. Le cas d'établissements relevant d'autorités différentes reste soumis à un décret en Conseil d'Etat, sans désignation automatique d'une autorité ni création d'un délai.")

add('L1237-19-6', '''
<p>Si l'autorité administrative refuse de valider l'accord, les parties peuvent négocier un nouvel accord en tenant compte des motifs de ce refus. Le comité social et économique, s'il existe, est informé de la reprise de la négociation. Une fois conclu, le nouvel accord est transmis à l'autorité administrative, qui se prononce dans les conditions prévues aux articles L. 1237-19-3 et L. 1237-19-4.</p>
''', "Réécriture à droit constant : la faculté de reprendre la négociation est attribuée aux parties et les étapes qui suivent le refus sont formulées dans leur ordre. L'information du comité et le nouveau contrôle administratif sont maintenus. Aucune réforme de fond.",
"La négociation d'un nouvel accord reste facultative et doit tenir compte de la motivation du refus. Les renvois à L. 1237-19-3 et L. 1237-19-4 préservent les contrôles et le régime de notification, de délai et de silence applicables à la nouvelle transmission.")

add('L1237-19-7', '''
<p>Lorsqu'un comité social et économique existe, il est consulté régulièrement et de manière détaillée sur le suivi de la mise en œuvre de l'accord portant rupture conventionnelle collective. Ses avis sont transmis à l'autorité administrative.<br /><br />L'autorité administrative est associée au suivi de ces mesures. L'employeur établit un bilan de la mise en œuvre de l'accord portant rupture conventionnelle collective et le lui transmet.</p>
''', "Réécriture à droit constant : la condition d'existence du comité lui est rattachée explicitement et l'employeur est nommé pour l'établissement et la transmission du bilan. Les deux alinéas matérialisés par les sauts de ligne sont conservés. Aucune réforme de fond.",
"Dans la source, « s'il existe » est placé après le suivi de la mise en œuvre ; la proposition explicite qu'il vise le comité social et économique. La consultation reste régulière et détaillée, les avis sont transmis et l'administration participe au suivi en plus de recevoir le bilan. Aucun rythme chiffré supplémentaire n'est imposé.")

add('L1237-19-8', '''
<p>L'accord collectif mentionné à l'article L. 1237-19, le contenu de l'accord portant rupture conventionnelle collective et la régularité de la procédure qui précède la décision de l'autorité administrative ne peuvent être contestés dans un litige distinct de celui portant sur la décision de validation mentionnée à l'article L. 1237-19-3.</p>
<p>Les recours contre la décision de validation sont formés, instruits et jugés selon les conditions définies à l'article L. 1235-7-1.</p>
<p>Toute autre contestation relative à la rupture du contrat doit être formée avant l'expiration d'un délai de douze mois à compter de la date de cette rupture. A défaut, elle est irrecevable.</p>
''', "Réécriture à droit constant : la concentration du contentieux est formulée avec le verbe contester et l'irrecevabilité de la contestation tardive est exprimée dans une phrase distincte. Les trois alinéas et leurs domaines respectifs sont maintenus. Aucune réforme de fond.",
"Conserver les renvois à L. 1237-19-3 et L. 1235-7-1, vérifié dans le corpus public, ainsi que le délai de douze mois et son point de départ à la date de rupture pour les autres contestations. Ne pas appliquer ces douze mois au recours contre la validation, qui conserve le régime de L. 1235-7-1. La source distingue l'accord collectif de son contenu, malgré leur proximité : les deux objets restent mentionnés.")

add('L1237-19-9', '''
<p>Lorsque, par leur ampleur, les suppressions d'emplois résultant de l'accord collectif prévu à l'article L. 1237-19 affectent l'équilibre du ou des bassins d'emploi dans lesquels ils sont implantés, les entreprises ou les établissements d'au moins mille salariés, ainsi que les entreprises mentionnées à l'article L. 2331-1 et celles qui remplissent les conditions prévues aux articles L. 2341-1 et L. 2341-2, dès lors qu'elles emploient au total au moins mille salariés, doivent contribuer à la création d'activités et au développement des emplois. Ils doivent également atténuer les effets de l'accord portant rupture conventionnelle collective envisagé sur les autres entreprises du ou des bassins d'emploi.</p>
<p>Ces obligations ne s'appliquent pas aux entreprises en redressement ou en liquidation judiciaire.</p>
''', "Réécriture à droit constant : les obligations de contribution et d'atténuation sont formulées dans deux phrases au sein du premier alinéa. Le champ des entreprises et établissements, les seuils et l'exclusion du second alinéa sont maintenus. Aucune réforme de fond.",
"Maintien des seuils d'au moins mille salariés, y compris le total requis pour les entreprises visées par les renvois à L. 2331-1 et L. 2341-1/L. 2341-2, et de l'exclusion en redressement ou liquidation judiciaire. Ambiguïté préexistante : le pronom « ils » de « dans lesquels ils sont implantés » a un antécédent incertain dans la source (emplois ou entreprises/établissements). La formulation est conservée pour ne pas trancher silencieusement le périmètre territorial ; à clarifier expressément lors de la coordination avec L. 1233-84, qui vise l'implantation des entreprises. Les obligations de revitalisation ne sont pas réduites par la réforme de l'indemnité de licenciement.")

add('L1237-19-10', '''
<p>Dans les six mois qui suivent la validation prévue à l'article L. 1237-19-3, l'entreprise et l'autorité administrative concluent une convention fixant la nature des actions prévues à l'article L. 1237-19-9, ainsi que leurs modalités de financement et de mise en œuvre. Le cas échéant, cette convention est établie sur la base d'une étude d'impact social et territorial prescrite par l'autorité administrative.<br /><br />La convention tient compte des actions de même nature qui ont éventuellement été mises en œuvre par anticipation dans le cadre d'un accord collectif relatif à la gestion prévisionnelle des emplois et des compétences. Elle tient également compte des actions prévues dans un accord collectif portant rupture conventionnelle collective établi par l'entreprise ou dans une démarche volontaire de celle-ci faisant l'objet d'un document-cadre conclu entre l'Etat et l'entreprise. Un décret définit le contenu et les modalités d'adoption de ce document-cadre. Lorsqu'un accord collectif de groupe, d'entreprise ou d'établissement prévoit des actions de même nature assorties d'engagements financiers de l'entreprise au moins égaux au montant de la contribution prévue à l'article L. 1237-19-11, cet accord tient lieu, à la demande de l'entreprise, de la convention entre l'entreprise et l'autorité administrative prévue au présent article. L'autorité administrative peut toutefois s'y opposer par une décision motivée exprimée dans les deux mois suivant la demande.</p>
''', "Réécriture à droit constant : le délai de conclusion et l'objet de la convention sont formulés directement. Les trois cadres d'actions à prendre en compte, les conditions de substitution d'un accord collectif et l'opposition administrative sont répartis en phrases plus courtes, sans modifier les deux alinéas. Aucune réforme de fond.",
"Conserver les six mois à compter de la validation, l'étude d'impact social et territorial seulement lorsqu'elle est prescrite, les renvois à L. 1237-19-9 et L. 1237-19-11, et le délai d'opposition de deux mois à compter de la demande. La substitution exige la demande de l'entreprise, un accord de groupe, d'entreprise ou d'établissement et des engagements financiers au moins égaux à la contribution. Les trois cadres d'actions pris en compte restent distincts ; le document-cadre est conclu avec l'Etat et régi par décret. Le régime de convention-cadre nationale de L. 1237-19-14 reste à articuler sans effacer ses propres délais.")

add('L1237-19-11', '''
<p>Pour chaque emploi supprimé, l'entreprise verse une contribution au moins égale à deux fois la valeur mensuelle du salaire minimum de croissance. L'autorité administrative peut toutefois fixer un montant inférieur si l'entreprise n'est pas en mesure d'en supporter la charge financière.<br /><br />Si aucune convention n'est signée et qu'aucun accord collectif n'en tient lieu, les entreprises versent au Trésor public une contribution égale au double du montant prévu au premier alinéa.</p>
''', "Réécriture à droit constant : le minimum est présenté par emploi supprimé et la dérogation financière est exprimée directement. Le second alinéa explicite l'absence des deux instruments possibles avant le versement au Trésor public. Aucune réforme de fond.",
"Maintien du minimum de deux valeurs mensuelles du SMIC par emploi supprimé, de la faculté de minoration pour incapacité financière et du double du montant prévu au premier alinéa en l'absence de convention ou d'accord en tenant lieu. Le renvoi au premier alinéa est conservé sans le remplacer par un forfait de quatre SMIC qui effacerait la question de la minoration. Coordination avec L. 1237-19-10 et L. 1237-19-14. Contribution de revitalisation distincte de l'indemnité de rupture et de son plafond proposé de six mois.")

add('L1237-19-12', '''
<p>Les collectivités territoriales intéressées, les organismes consulaires et les partenaires sociaux membres de la commission paritaire interprofessionnelle régionale sont consultés avant que soient déterminées les actions prévues à l'article L. 1237-19-9.<br /><br />L'exécution de ces actions est suivie et évaluée sous le contrôle de l'autorité administrative, selon des modalités définies par décret. Ce décret fixe aussi les conditions dans lesquelles les entreprises dont le siège est situé hors du bassin d'emploi affecté par l'accord portant rupture conventionnelle collective contribuent à ces actions.</p>
''', "Réécriture à droit constant : les organismes consultés sont placés en sujet, en conservant l'antériorité de la consultation. Le suivi, l'évaluation et le cas des entreprises dont le siège est extérieur au bassin sont exprimés dans des phrases distinctes. Aucune réforme de fond.",
"Les trois catégories consultées et la qualité de membres de la commission paritaire interprofessionnelle régionale des partenaires sociaux sont préservées. La source vise bien cette commission ; aucune autre institution ne lui est substituée. Maintien du renvoi à L. 1237-19-9, du contrôle administratif et de la compétence du même décret pour les modalités de suivi et la contribution des entreprises dont le siège est hors du bassin.")

add('L1237-19-13', '''
<p>Les maisons de l'emploi peuvent participer à la mise en œuvre des mesures de revitalisation des bassins d'emploi. Une convention avec les entreprises intéressées fixe les conditions de cette participation.</p>
''', "Réécriture à droit constant : la faculté de participation et la fixation conventionnelle de ses conditions sont exposées dans deux phrases, au sein du même alinéa. Aucune réforme de fond.",
"Le concours des maisons de l'emploi reste facultatif. Les conditions de leur participation sont fixées par convention avec les entreprises intéressées ; aucune compétence de substitution à celle de l'autorité administrative ni aucun financement automatique ne sont créés.")

add('L1237-19-14', '''
<p>Lorsque les suppressions d'emplois concernent au moins trois départements, le ministre chargé de l'emploi et l'entreprise concluent une convention-cadre nationale de revitalisation.</p>
<p>Le montant de la contribution mentionnée à l'article L. 1237-19-11 est déterminé en tenant compte du nombre total d'emplois supprimés.</p>
<p>La convention-cadre est signée dans les six mois qui suivent la décision de validation prévue à l'article L. 1237-19-3.</p>
<p>Dans les quatre mois qui suivent cette signature, le représentant de l'Etat et l'entreprise concluent une ou plusieurs conventions locales. Celles-ci respectent le contenu de la convention-cadre nationale.</p>
''', "Réécriture à droit constant : les parties à la convention nationale et aux conventions locales sont nommées directement. Les deux délais et leurs points de départ sont formulés séparément, dans les quatre alinéas initiaux. Aucune réforme de fond.",
"Maintien du seuil d'au moins trois départements, du nombre total d'emplois supprimés pour la contribution de L. 1237-19-11, des six mois à compter de la décision de validation de L. 1237-19-3 et des quatre mois à compter de la signature nationale pour les conventions locales. Celles-ci doivent respecter le contenu national. Articuler avec la convention et le délai de L. 1237-19-10, sans fusionner les points de départ ni créer un nouveau montant de contribution.")

add('L1238-1', '''
<p>Le fait de porter atteinte ou de tenter de porter atteinte à l'exercice régulier des fonctions de conseiller du salarié est puni d'un an d'emprisonnement et de 3 750 euros d'amende. Sont notamment visées les atteintes ou tentatives d'atteinte résultant de la méconnaissance des articles L. 1232-8 à L. 1232-12 et L. 1232-14.</p>
''', "Réécriture à droit constant : la peine est énoncée dans une première phrase et les manquements expressément cités sont présentés dans une seconde. L'atteinte consommée et sa tentative demeurent toutes deux réprimées. Aucune réforme de fond.",
"Maintien de l'exercice régulier des fonctions comme objet de la protection, d'un an d'emprisonnement et de 3 750 euros d'amende, ainsi que des renvois à L. 1232-8 à L. 1232-12 et à L. 1232-14. La liste demeure illustrative (« notamment ») et L. 1232-13 n'y est pas ajouté. La réécriture ne crée ni nouvelle infraction ni nouvelle peine.")

sources=json.loads(Path('source.json').read_text())
assert len(sources)==24 and set(D)=={a['number'] for a in sources}
answer=[]
for a in sources:
    xml,reason,review=D[a['number']]
    note=plain(a['source_notes_xml'])
    if note:
        review+=' Note source historique conservée pour le contrôle de l\'application dans le temps : '+note
    answer.append({**{k:a[k] for k in ('code_id','source_id','source_sha256','number')},
                   'proposed_xml':xml,'reason':reason,'review_notes':review,'status':'rewrite_draft'})
Path('answer.json').write_text(json.dumps(answer,ensure_ascii=False,indent=2)+'\n')
print('answer.json :',len(answer),'articles ;',sum(len(a['proposed_xml']) for a in answer),'caractères de texte proposé XML')
