from pathlib import Path
import json,hashlib,re,sys
H=Path(__file__).resolve().parent;B=H.parents[3];sys.path.insert(0,str(B));from run_exhaustive import validate_answer
sha=lambda v:hashlib.sha256(v.encode()).hexdigest();sources=json.loads((H/'source.json').read_text());draft={}
def put(n,s):draft[n]=s.strip()
put('D133-12-1','''<p>Pour l’application de la présente sous-section, sauf disposition contraire :</p>
<p>1° Le terme « salarié » désigne les salariés, les stagiaires aides familiaux placés au pair, les accueillants familiaux mentionnés à l’article L. 441-1 du code de l’action sociale et des familles et les particuliers qui effectuent les prestations ponctuelles prévues au 8° de l’article L. 133-5-6 ;</p>
<p>2° Le terme « employeur » désigne les employeurs, les personnes recourant à un stagiaire aide familial placé au pair, les personnes accueillies par un accueillant familial en application de l’article L. 441-1 du code de l’action sociale et des familles et les particuliers faisant appel à un autre particulier pour les prestations ponctuelles prévues au même 8°.</p>
<p>Ces équivalences permettent l’accès aux formalités simplifiées sans modifier, à elles seules, la qualification de la relation entre les personnes concernées ni les protections et avantages propres à chacune de ces situations.</p>''')
put('D133-13','''<p>L’employeur qui choisit un dispositif simplifié prévu à l’article L. 133-5-6 y adhère par voie dématérialisée, sous réserve de la faculté de recourir au papier prévue à l’article L. 133-5-8. Une seule démarche permet de renseigner son profil et de transmettre la première déclaration ; aucun formulaire d’adhésion distinct n’est exigé lorsque cette déclaration contient les éléments nécessaires à l’adhésion.</p>
<p>Le profil comporte :</p>
<p>1° L’identification de l’entreprise, de l’association ou du particulier :</p>
<p>a) Pour une entreprise ou une association, la raison ou dénomination sociale, l’adresse du siège et le numéro d’identité de l’établissement employeur mentionné à l’article R. 123-221 du code de commerce ;</p>
<p>b) Pour un particulier, les nom, prénoms et adresse ;</p>
<p>2° Lorsqu’il y a lieu, l’autorisation de prélèvement automatique sur le compte désigné.</p>
<p>L’organisme réutilise les données à jour qu’il détient légalement ou auxquelles il a légalement accès pour cette démarche. Elles ne sont ni ressaisies ni justifiées une nouvelle fois ; l’employeur ne communique que les éléments manquants ou modifiés. Une nouvelle autorisation bancaire n’est requise qu’en cas de modification qui la rend nécessaire.</p>
<p>L’organisme mentionné à l’article L. 133-5-10 oriente lui-même la demande de l’entreprise mentionnée au 1° de l’article L. 133-5-6 vers l’organisme compétent pour son secteur professionnel. Une erreur d’orientation n’impose pas une seconde adhésion.</p>
<p>Les particuliers mentionnés au 4° de l’article L. 133-5-6 accomplissent cette démarche dans les conditions de l’article D. 133-13-16.</p>
<p>Les simplifications de la présente sous-section s’appliquent, dès l’entrée en vigueur de leur nouvelle rédaction, aux démarches en cours et futures. Elles ne réduisent ni les prestations, ni les exonérations, abattements, crédits d’impôt et prises en charge ouverts dans leurs conditions propres aux bénéficiaires actuels ou futurs. Elles n’annulent pas les rémunérations ou dettes déjà dues et ne rétablissent aucune imposition ou formalité supprimée par une autre disposition.</p>''')
put('D133-13-1','''<p>Les employeurs mentionnés aux 1°, 2° et 5° de l’article L. 133-5-6 identifient le salarié auprès de l’organisme mentionné à l’article L. 133-5-10 au moyen des données de la déclaration prévue à l’article D. 1272-1 du code du travail.</p>
<p>Cette identification peut être intégrée à la première déclaration prévue à l’article D. 133-13-2 lorsque la transmission unique respecte les échéances des formalités d’embauche légalement maintenues. Lorsqu’une déclaration préalable à l’embauche reste requise avant cette première déclaration, les données nécessaires sont transmises à cette échéance et réutilisées ensuite, sans seconde identification. L’organisme réutilise les données à jour déjà légalement reçues ; seules les données manquantes ou modifiées sont communiquées.</p>
<p>L’employeur conserve l’obligation de remettre au salarié la déclaration d’identification prévue à l’article D. 1272-1 du code du travail. La transmission unique ne dispense pas de cette remise.</p>
<p>La pénalité prévue par renvoi à l’article L. 1221-11 du code du travail est supprimée dans les mêmes conditions que celle de cet article : aucun fait postérieur à sa suppression et aucun fait antérieur dont la pénalité n’est pas définitive à cette date ne peut donner lieu à son prononcé. Les pénalités devenues définitives avant cette date restent régies par les dispositions antérieures, sans restitution du seul fait de la suppression et sans préjudice des recours et restitutions légalement ouverts. Les autres sanctions légalement maintenues conservent leur champ propre ; aucune ne résulte du seul regroupement régulier de deux transmissions.</p>''')
put('D133-13-2','''<p>Les employeurs utilisant un dispositif simplifié mentionné aux 1° à 8° de l’article L. 133-5-6 transmettent les données nécessaires au salarié et à sa période d’activité, sous réserve des règles propres à chaque situation.</p>
<p>La déclaration comprend :</p>
<p>1° Pour l’identification du salarié :</p>
<p>a) Les nom de famille, nom d’usage et prénoms ;</p>
<p>b) Le numéro d’inscription au répertoire des personnes physiques lorsqu’il en dispose ;</p>
<p>c) Les date et lieu de naissance ;</p>
<p>d) Le sexe ;</p>
<p>e) L’adresse ;</p>
<p>2° La période d’activité, qui ne peut excéder le mois civil.</p>
<p>Les données d’identité sont renseignées une seule fois dans le profil du salarié puis réutilisées pour les déclarations suivantes. Elles ne sont demandées de nouveau que si elles sont manquantes, modifiées ou rendues incertaines par une anomalie précise. Lorsqu’un numéro d’identification vérifié permet de les obtenir légalement, leur nouvelle saisie n’est pas exigée.</p>
<p>L’employeur transmet pour chaque période les données d’activité et de rémunération qui lui sont propres ainsi que les changements affectant le profil. Il conserve la faculté de rectifier une donnée inexacte sans refaire l’adhésion ou l’identification entière.</p>''')
put('D133-13-3','''<p>Dans le respect des règles de chaque dispositif, l’organisme mentionné à l’article L. 133-5-10 établit, pour le compte des employeurs mentionnés aux 1° à 8° de l’article L. 133-5-6, au plus tard quatre jours après réception de la déclaration :</p>
<p>1° Le bulletin de paie prévu à l’article L. 133-5-8, comportant les mentions de l’article R. 3243-1 du code du travail et le récapitulatif prévu par l’article L. 133-5-8. Il est mis à la disposition de l’employeur et du salarié pour les situations des 1° à 6° de l’article L. 133-5-6 ; l’employeur reçoit également un relevé global des sommes dues ;</p>
<p>2° Le relevé mensuel des rémunérations et indemnités prévues aux 1° à 4° de l’article L. 442-1 du code de l’action sociale et des familles, délivré au particulier mentionné au 7° de l’article L. 133-5-6 et à son accueillant ;</p>
<p>3° Pour les situations du 8° du même article, un décompte des rémunérations versées et des cotisations et contributions sociales et fiscales dues, mis à la disposition des particuliers mentionnés aux 1° et 2° de l’article D. 133-12-1.</p>
<p>Ces documents sont établis automatiquement à partir de la déclaration et des données à jour déjà légalement détenues. Aucun formulaire ou demande de délivrance supplémentaire n’est exigé. Leur mise à disposition ne supprime ni les mentions nécessaires aux droits du salarié ou de l’accueillant ni les modalités de remise qui leur sont légalement applicables.</p>''')
put('D133-13-4','''<p>I. – Les employeurs mentionnés aux 1° à 9° de l’article L. 133-5-6 soumis aux obligations du II déclarent à l’organisme mentionné à l’article L. 133-5-10 :</p>
<p>1° Le début et la fin d’un arrêt de travail pour accident ou maladie, d’origine professionnelle ou non professionnelle, d’un congé de maternité, d’adoption, de paternité et d’accueil de l’enfant ou d’un congé supplémentaire de naissance ;</p>
<p>2° La fin du contrat de travail.</p>
<p>Ils transmettent par voie dématérialisée :</p>
<p>a) Les nom et prénoms du salarié concerné, ou son identification déjà vérifiée dans le service ;</p>
<p>b) Les données relatives à l’arrêt de travail ou à la fin du contrat mentionnées aux k et l du 3° du V de l’article R. 133-14.</p>
<p>II. – Cette transmission satisfait aux obligations suivantes, sans seconde attestation portant sur les données déjà transmises :</p>
<p>1° Les attestations prévues aux articles R. 323-10 et R. 441-4 permettant de déterminer les revenus d’activité antérieurs pour les prestations en espèces des assurances maladie, maternité et paternité ou le salaire journalier de calcul des indemnités journalières d’accident du travail et de maladie professionnelle ;</p>
<p>2° La fourniture des éléments couverts par l’attestation prévue au premier alinéa de l’article R. 1234-9 du code du travail.</p>
<p>L’organisme assure la transmission aux destinataires compétents. Seuls les éléments nécessaires qui sont manquants ou inexacts peuvent faire l’objet d’une demande complémentaire motivée. Les droits aux prestations, les exceptions et délais applicables aux signalements ainsi que les dispositions transitoires favorables du congé supplémentaire de naissance demeurent applicables. Les documents de fin de contrat qui doivent être remis au salarié continuent de lui être délivrés ; la transmission de leurs données à un organisme ne dispense pas de cette remise.</p>''')
put('D133-13-5','''<p>L’employeur mentionné au 1° ou au 2° de l’article L. 133-5-6 qui utilise un dispositif simplifié transmet par voie dématérialisée la déclaration de l’article D. 133-13-2, complétée par :</p>
<p>1° Les données relatives à l’activité et à la rémunération :</p>
<p>a) Le nombre de jours ou d’heures rémunérés ;</p>
<p>b) Les éléments de rémunération et le choix d’une déclaration en montant brut ou net des cotisations et contributions à la charge du salarié. Sont précisés la nature et le montant des accessoires de salaire soumis à cotisations, ainsi que, le cas échéant, ceux des éléments non soumis, notamment les remboursements de transport et autres frais professionnels ;</p>
<p>c) La base forfaitaire retenue, lorsqu’elle s’applique ;</p>
<p>d) Les dates de congés et, s’il y a lieu, l’indemnité de congés payés ;</p>
<p>e) Le total des jours d’absence et leur détail par nature, lorsqu’il y en a ;</p>
<p>2° La date de paiement de la rémunération ;</p>
<p>3° Le cas échéant, la qualité de bénéficiaire de l’obligation d’emploi prévue à l’article L. 5212-2 du code du travail.</p>
<p>Le choix entre brut et net et les autres paramètres stables sont conservés dans le profil jusqu’à leur modification. Les données d’un congé ou d’une absence déjà signalés ne sont pas saisies une seconde fois ; le déclarant ne complète que leurs conséquences de paie non encore connues. La réutilisation des données ne réduit aucune exonération, déduction de frais ou base forfaitaire légalement applicable.</p>''')
put('D133-13-6','''<p>La déclaration prévue à l’article D. 133-13-2 est transmise au plus tard le cinquième jour suivant la période d’activité.</p>
<p>Les employeurs paient à l’organisme mentionné à l’article L. 133-5-10 les cotisations et contributions sociales prévues à l’article L. 133-5-7 ainsi que la retenue à la source prévue à l’article 204 A du code général des impôts au cours du deuxième mois suivant celui de la période déclarée.</p>
<p>Le seul retard de transmission de la déclaration n’avance pas cette échéance. Lorsque celle-ci est déjà dépassée lors de la déclaration, les sommes restant dues sont acquittées sans délai, après prise en compte des paiements déjà reçus et des réductions ou prises en charge applicables.</p>
<p>L’article R. 243-16 s’applique au défaut de paiement à l’échéance ainsi déterminée. Aucun paiement déjà effectué ne peut être exigé une seconde fois du fait d’une déclaration tardive ou rectificative.</p>''')
put('D133-13-7','''<p>L’organisme mentionné à l’article L. 133-5-10 recouvre simultanément aux prélèvements du 1° de l’article L. 133-5-7 les autres cotisations et contributions sociales relevant de ce 1°, dans le champ des conventions qui les prévoient. L’utilisation d’un dispositif simplifié ne rend pas à elle seule obligatoire une contribution qui ne l’est pas.</p>
<p>Les sommes sont versées à leur attributaire à hauteur des montants dus par les employeurs, après application du taux forfaitaire pour frais de non-recouvrement fixé par arrêté des ministres chargés de la sécurité sociale et du budget. Le présent article ne crée ni nouveau taux ni frais supplémentaires à la charge de l’employeur.</p>
<p>Les conventions prévues à l’article L. 133-5-11 fixent les dates de versement aux attributaires dans les limites de l’arrêté et la durée de conservation des informations et formulaires. L’arrêté mentionné au deuxième alinéa fixe aussi les règles applicables en l’absence de convention.</p>
<p>Les organismes utilisent une transmission unique des données nécessaires ; leurs conventions de répartition ne peuvent imposer à l’employeur une seconde déclaration des mêmes rémunérations.</p>''')
put('D133-13-8','''<p>Les particuliers employeurs qui rémunèrent leurs salariés au moyen des titres spéciaux de paiement prévus au B de l’article L. 1271-1 du code du travail les déclarent auprès de l’organisme mentionné à l’article L. 133-5-10.</p>
<p>La déclaration simplifiée prévue à l’article D. 133-13-2 remplit cette obligation. Le paiement par titre spécial ne donne lieu ni à une nouvelle identification ni à une seconde déclaration des mêmes salariés et périodes.</p>''')
put('D133-13-9','''<p>Le particulier transmet la déclaration prévue à l’article D. 133-13-2 au plus tard le cinquième jour du mois suivant la période d’activité. Il utilise le profil déjà renseigné et ne transmet que les données de la période et les modifications nécessaires.</p>
<p>L’article R. 243-16 s’applique lorsque le paiement n’est pas effectué aux dates prévues aux articles D. 133-13-13 et D. 133-13-18, sans modification de ces dates par le présent article. Une déclaration rectificative ne rend pas à nouveau exigibles des sommes déjà payées.</p>''')
put('D133-13-10','''<p>Au cours du mois de mars, l’organisme mentionné à l’article L. 133-5-10 met automatiquement à la disposition de l’employeur l’attestation annuelle permettant de justifier, pour l’année précédente, de son droit aux crédits d’impôt des articles 199 sexdecies et 200 quater B du code général des impôts.</p>
<p>Au cours du même mois, il délivre automatiquement à l’assistant maternel l’attestation permettant de justifier, pour l’année précédente, de son droit à l’abattement de l’article 80 sexies du même code.</p>
<p>Aucune demande annuelle distincte n’est nécessaire. Les attestations sont établies à partir des données déclarées et des rectifications connues ; leurs destinataires peuvent en demander la correction. Elles restent accessibles selon les modalités applicables aux personnes autorisées à utiliser le papier. La réutilisation de données fiscales déjà transmises ne prive aucun bénéficiaire de son attestation ni de son avantage.</p>''')
put('D133-13-11','''<p>Les particuliers mentionnés aux 3°, 4° et 6° à 9° de l’article L. 133-5-6 peuvent adhérer au dispositif d’intermédiation du versement des rémunérations prévu à l’article L. 133-5-12, sous réserve de l’accord écrit et préalable du salarié. Cet accord peut être recueilli par voie électronique dans des conditions permettant d’en établir l’auteur et le contenu, sans formulaire supplémentaire portant sur les mêmes éléments.</p>
<p>La déclaration prévue à l’article D. 133-13-2 vaut demande de versement de la rémunération. Sa réception après le quinzième jour du mois suivant l’activité ne constitue pas, à elle seule, un motif de refus de l’intermédiation. Elle ne reporte pas l’échéance de paiement du salaire à la charge de l’employeur. Le dispositif ne peut être utilisé pour verser une seconde fois une rémunération déjà entièrement payée ; les paiements partiels sont pris en compte dans les conditions et limites du III de l’article L. 133-5-12.</p>
<p>Le prélèvement prévu au troisième alinéa du I de l’article L. 133-5-12 intervient dans les deux jours ouvrés suivant la réception de la déclaration sur le compte désigné par le particulier. Pour les employeurs mentionnés au 3° de l’article L. 133-5-6, la rémunération est prélevée dans les mêmes deux jours ouvrés ; les cotisations, contributions et retenue à la source de l’article 204 A du code général des impôts le sont dans le délai du premier alinéa de l’article D. 133-13-13.</p>
<p>Sous réserve des exclusions et suspensions légalement applicables, notamment du V de l’article L. 133-5-12, l’organisme verse la rémunération au salarié, sur le compte qu’il a désigné, au plus tard le quatrième jour ouvré suivant la réception de la déclaration. Il avertit le salarié de cette déclaration et de la date du versement.</p>
<p>Les comptes bancaires et la qualité de leur titulaire restent soumis aux conditions de l’article L. 133-5-12. La suppression du refus lié au seul dépassement du quinzième jour ne supprime ni les contrôles des prestations fictives ni les règles applicables aux impayés et au surendettement.</p>''')
put('D133-13-11-1','''<p>I. – Le plafond annuel, par foyer fiscal au sens de l’article 6 du code général des impôts, de l’aide prévue au 5° du II de l’article L. 133-5-12 est fixé :</p>
<p>a) À 10 000 euros pour les personnes mentionnées au 3° de l’article L. 341-4, celles qui ont à leur charge une telle personne vivant sous leur toit et celles qui ont à leur charge un enfant ouvrant droit au complément d’allocation d’éducation de l’enfant handicapé prévu au deuxième alinéa de l’article L. 541-1 ;</p>
<p>b) À 6 000 euros dans les autres cas.</p>
<p>II. – Le plafond annuel, par foyer fiscal au même sens, de l’aide prévue au 6° du II de l’article L. 133-5-12 est fixé à 1 150 euros par enfant à charge âgé de moins de six ans.</p>
<p>L’organisme applique le plafond correspondant à la situation du foyer à partir des données à jour qu’il détient légalement ou peut légalement réutiliser pour cette aide. Il ne demande pas chaque mois de nouvelles pièces relatives à une situation inchangée. Les bénéficiaires actuels et futurs conservent le plafond majoré et les autres conditions favorables qui leur sont applicables.</p>''')
# Preserve all fraud, solvency and appeal conditions; remove only duplicate requests and restoration delay.
s=next(s['source_xml']for s in sources if s['number']=='D133-13-11-2');s=re.sub(r'<br\s+clear="none"\s*/?>','<br />',s)
s=s.replace('à compter de la période d\'activité correspondant au mois suivant le constat par l\'organisme mentionné à l\'article L. 133-5-10 de la régularisation de la situation.','dès que l’organisme mentionné à l’article L. 133-5-10 constate que les conditions de rétablissement sont remplies, sans attendre le mois suivant.')
s=s.replace('à compter de la période d\'activité correspondant au mois suivant le constat par l\'organisme mentionné à l\'article L. 133-5-10 de la régularisation de la situation.','dès le constat de la régularisation par l’organisme, sans attendre le mois suivant.')
s=s.replace('sur demande de ces personnes,','sans nouvelle demande lorsque l’organisme dispose déjà des éléments établissant la régularisation, ou sur demande de ces personnes,')
s=s.replace("sur demande de l'utilisateur,","sans nouvelle demande lorsque l’organisme dispose déjà des éléments établissant la régularisation, ou sur demande de l’utilisateur,")
s=s.replace("dans un délai de trente jours à compter de l'envoi de la notification prévues au I du présent article.","dans un délai de trente jours à compter de la réception de la notification prévue au I du présent article.")
s+='''<p>L’organisme réutilise les pièces déjà légalement reçues pour le même contrôle lorsque leur contenu est à jour et permet de vérifier la condition concernée. Une nouvelle demande précise les éléments manquants, inexacts ou devenus inadaptés. La suppression des demandes répétées et de l’attente jusqu’au mois suivant ne réduit ni les droits de recours, ni les durées maximales de cinq ans et de six mois, ni les conditions légales de remboursement et de réalité de la prestation. L’organisme informe sans délai l’utilisateur et le salarié du rétablissement du service. Les durées d’exclusion décidées restent à accomplir avant ce rétablissement.</p>'''
put('D133-13-11-2',s)
put('D133-13-12','''<p>Les employeurs mentionnés aux 3° et 6° à 9° de l’article L. 133-5-6 complètent la déclaration de l’article D. 133-13-2 avec les données suivantes, dans la mesure où elles ne figurent pas déjà, à jour, dans les profils ou les données légalement reçues par l’organisme mentionné à l’article L. 133-5-10 :</p>
<p>1° Pour le particulier employeur :</p>
<p>a) Les nom et prénoms ;</p>
<p>b) L’adresse ;</p>
<p>c) Les données bancaires nécessaires au prélèvement des sommes dues à l’organisme ;</p>
<p>2° En cas d’emploi salarié :</p>
<p>a) Le nombre d’heures de travail effectuées ;</p>
<p>b) Le salaire horaire et le salaire total versés, nets des cotisations et contributions à la charge du salarié ;</p>
<p>c) Le cas échéant, la nature et le montant des accessoires de salaire soumis à cotisations et contributions ;</p>
<p>d) Le cas échéant, la nature et le montant des autres versements et retenues de la période, notamment au titre des frais de transport et autres frais professionnels ;</p>
<p>e) La date de versement du salaire lorsqu’elle diffère de celle du 7° ;</p>
<p>f) Pour une déclaration dématérialisée et un nombre d’heures contractuelles excédant trente-deux heures par mois pour un même employeur, l’option annuelle de versement des indemnités de congés payés : indemnité égale au dixième de la rémunération brute versée mensuellement ou indemnité calculée selon l’article L. 3141-24 du code du travail ;</p>
<p>g) Si l’employeur a choisi cette dernière modalité, les dates de congés et l’indemnité correspondante calculée selon l’article L. 3141-24 du code du travail ;</p>
<p>h) L’activité exercée ;</p>
<p>3° En cas de recours à un stagiaire aide familial au pair, la base forfaitaire retenue ;</p>
<p>4° En cas d’accueil par un accueillant familial :</p>
<p>a) Les références de l’agrément ;</p>
<p>b) Les contreparties financières prévues à l’article L. 442-1 du code de l’action sociale et des familles, avant la retenue à la source de l’article 204 A du code général des impôts ;</p>
<p>c) Le nombre de jours d’accueil à temps plein ou partiel de la période ;</p>
<p>5° Pour les employeurs du 3° de l’article L. 133-5-6 utilisant l’intermédiation de l’article L. 133-5-12, le cas échéant, le choix de l’option de paiement du deuxième alinéa de l’article D. 133-13-13 ;</p>
<p>6° Dans les situations du 8° de l’article L. 133-5-6 :</p>
<p>a) La durée de la prestation ;</p>
<p>b) La rémunération totale nette des cotisations et contributions à la charge du salarié ;</p>
<p>c) L’activité exercée ;</p>
<p>7° La date de déclaration, enregistrée automatiquement pour la déclaration dématérialisée ;</p>
<p>8° La signature de l’employeur lorsque la déclaration est effectuée sur papier.</p>
<p>Les coordonnées, références d’agrément et options annuelles sont conservées jusqu’à leur modification ou expiration ; elles ne sont pas ressaisies à chaque période. L’agrément lui-même demeure requis dans les conditions qui lui sont propres. Les choix et garanties relatifs aux congés payés, indemnités et frais professionnels ne sont pas réduits par la transmission unique.</p>''')
put('D133-13-13','''<p>Les cotisations et contributions, la retenue à la source prévue à l’article 204 A du code général des impôts et les autres prélèvements légalement dus sur les rémunérations déclarées selon l’article D. 133-13-2 sont acquittés par prélèvement automatique sur le compte désigné par le particulier, au cours du deuxième mois suivant la période d’activité.</p>
<p>Les employeurs mentionnés aux 3° et 6° à 9° de l’article L. 133-5-6 qui utilisent l’intermédiation prévue à l’article L. 133-5-12 peuvent choisir un prélèvement à la même date que celle du troisième alinéa de l’article D. 133-13-11. Ce choix reste facultatif et est conservé jusqu’à sa modification.</p>
<p>Le mandat bancaire déjà valablement enregistré est réutilisé ; aucune nouvelle autorisation n’est demandée pour une échéance inchangée. Le montant prélevé tient compte des paiements, exonérations, allègements et prises en charge applicables. Le présent article ne rétablit aucun prélèvement supprimé dans son champ légal.</p>''')
put('D133-13-14','''<p>Lorsque le particulier bénéficie d’une prise en charge de tout ou partie de ses cotisations et contributions dans les conditions de l’article L. 133-8-3, l’organisme de recouvrement calcule la part prise en charge dès réception de la déclaration prévue à l’article D. 133-13-2. Il en reçoit paiement du conseil départemental qui sert l’allocation.</p>
<p>Une convention entre l’organisme de recouvrement et chaque conseil départemental, conforme à la convention type approuvée par arrêté des ministres chargés de la sécurité sociale et des collectivités territoriales, précise les modalités de mise en œuvre.</p>
<p>Par dérogation à l’article D. 133-13-13, le particulier et le conseil départemental paient chacun la part qui leur incombe au cours du troisième mois suivant la période d’activité.</p>
<p>Les données du plan d’aide ou de compensation déjà légalement reçues sont utilisées pour ce calcul. Il n’est demandé au particulier ni une seconde déclaration des mêmes rémunérations ni, pour chaque mois, une nouvelle preuve d’une prise en charge inchangée. La dispense d’avance et la répartition des sommes à la charge de chacun restent celles de l’article L. 133-8-3.</p>''')
put('D133-13-15','''<p>Les émetteurs des titres spéciaux de paiement mentionnés à l’article R. 1271-8 du code du travail transmettent à l’Agence centrale des organismes de sécurité sociale les seules informations nécessaires à la vérification de la déclaration régulière des salariés mentionnés au 1° du A de l’article L. 1271-1 du même code.</p>
<p>Cette transmission permet le rapprochement avec les déclarations déjà reçues. Le recours à un titre spécial ne donne pas lieu à une seconde déclaration de la même période par le particulier ; les demandes complémentaires restent limitées aux anomalies précises et données nécessaires au contrôle.</p>''')
put('D133-13-16','''<p>Le particulier mentionné au 4° de l’article L. 133-5-6 identifie un nouveau salarié par voie dématérialisée auprès de l’organisme mentionné à l’article L. 133-5-10. L’identification peut être réalisée dans la même démarche que la première déclaration prévue à l’article D. 133-13-2, sans formulaire préalable distinct contenant les mêmes données.</p>
<p>Elle comporte :</p>
<p>1° Pour l’employeur :</p>
<p>a) Les nom et prénom ;</p>
<p>b) L’adresse ;</p>
<p>c) Le numéro d’employeur ;</p>
<p>d) Les données bancaires nécessaires au prélèvement des sommes dues ;</p>
<p>2° Pour le salarié :</p>
<p>a) Les nom de famille, nom d’usage et prénoms ;</p>
<p>b) Le numéro d’inscription au répertoire des personnes physiques s’il en dispose ;</p>
<p>c) Les date et lieu de naissance ;</p>
<p>d) Le sexe ;</p>
<p>e) L’adresse ;</p>
<p>f) L’activité de garde d’enfant à domicile ou d’assistant maternel ;</p>
<p>g) Pour un assistant maternel, la date d’agrément ou de son renouvellement.</p>
<p>L’organisme préremplit les données à jour qu’il détient légalement ou peut légalement obtenir pour cette démarche. Le particulier ne complète que les données manquantes ou modifiées ; les données bancaires de son profil ne sont pas ressaisies pour chaque nouveau salarié. Les conditions d’agrément et d’identification nécessaires aux droits de l’enfant, du salarié et de l’employeur sont conservées.</p>''')
put('D133-13-17','''<p>Le particulier mentionné au 4° de l’article L. 133-5-6 transmet par voie dématérialisée à l’organisme mentionné à l’article L. 133-5-10 la déclaration prévue à l’article D. 133-13-2, complétée par :</p>
<p>1° Les données d’employeur :</p>
<p>a) Les nom et prénoms ;</p>
<p>b) L’adresse ;</p>
<p>c) Le numéro d’employeur ;</p>
<p>2° Les données de travail rémunéré de la période :</p>
<p>a) Le nombre de jours de congés payés ;</p>
<p>b) Le nombre d’heures de travail, y compris supplémentaires ou complémentaires ;</p>
<p>c) Le salaire horaire et le salaire total nets des cotisations et contributions à la charge du salarié ;</p>
<p>d) Pour un assistant maternel agréé :</p>
<p>– le total des indemnités d’entretien ;</p>
<p>– le nombre de jours d’activité rémunérée ou d’absence indemnisée ;</p>
<p>– s’il y a lieu, le nombre de jours où l’enfant a été accueilli vingt-quatre heures consécutives ;</p>
<p>– le cas échéant, l’accueil d’un enfant ayant donné lieu à une majoration de salaire dans les conditions de l’article L. 423-13 du code de l’action sociale et des familles ;</p>
<p>3° La date de naissance de chacun des enfants gardés ;</p>
<p>4° Le cas échéant, la nature et le montant des autres accessoires de salaire soumis à cotisations et contributions ;</p>
<p>5° Le cas échéant, la nature et le montant des autres versements et retenues de la période, notamment les frais de transport, de repas et autres frais professionnels ;</p>
<p>6° Le nombre d’heures de garde en horaires spécifiques comprises dans les heures déjà déclarées ;</p>
<p>7° La date de paiement du salaire ;</p>
<p>8° En cas d’utilisation du paiement de l’article L. 133-5-12, les données bancaires nécessaires au versement et l’adresse électronique du salarié, lorsqu’elles ne sont pas déjà valablement enregistrées.</p>
<p>Les données de profil de l’employeur, des enfants et du salarié sont réutilisées tant qu’elles sont à jour. Le salarié peut renseigner directement ses coordonnées de paiement dans le service sécurisé ; l’employeur n’a pas à les retransmettre chaque mois. Un moyen sécurisé d’information déjà disponible pour le salarié peut remplacer la demande répétée de son adresse électronique. Les montants, indemnités, majorations et droits à prise en charge ne sont pas modifiés.</p>''')
put('D133-13-18','''<p>Les cotisations, contributions sociales et retenue à la source de l’article 204 A du code général des impôts légalement dues sont prélevées sur le compte désigné par le particulier le deuxième jour ouvré suivant la transmission de la déclaration prévue à l’article D. 133-13-2.</p>
<p>Le mandat valablement enregistré est réutilisé sans nouvelle démarche à chaque déclaration. Le prélèvement porte sur le solde effectivement dû après prise en compte des paiements, aides, exonérations, allègements et prises en charge applicables ; une rectification ne peut entraîner le second paiement de la même dette.</p>''')
put('D133-13-19','''<p>Le dispositif prévu au 8° de l’article L. 133-5-6 s’applique aux services ponctuels de conseil, d’enseignement, de formation et d’accompagnement, notamment sportifs et culturels, qu’un particulier demande pour son usage personnel à un autre particulier.</p>
<p>La prestation a un objet identifié et une durée déterminée convenue entre les parties, déclarée avec sa rémunération. Elle peut comporter plusieurs séances nécessaires à cet objet. Le plafond de trois heures hebdomadaires auprès d’un même particulier est supprimé ; le seul dépassement de cette durée ne fait pas perdre l’accès au dispositif simplifié.</p>
<p>Cette ouverture ne transforme pas une activité professionnelle permanente ou une relation de travail en prestation ponctuelle. Les qualifications, protections et obligations propres à la relation effectivement exercée restent applicables. Elle ne réduit aucune prestation, exonération ou protection attachée à l’utilisation régulière du dispositif.</p>''')
put('D133-13-20','''<p>Les particuliers mentionnés au 8° de l’article L. 133-5-6 bénéficient des règles des articles D. 133-13, D. 133-13-2 à D. 133-13-4 et D. 133-13-8 à D. 133-13-15, dans le champ propre à leur situation.</p>
<p>Ils utilisent une seule adhésion et une seule déclaration pour les données communes à ces formalités. Le renvoi à plusieurs articles n’autorise pas une répétition de la même démarche. Les décomptes, attestations, aides et garanties auxquels ils ont droit demeurent délivrés ou appliqués selon ces articles.</p>''')
# Keep the complete enumerations and event protections of the DSN regulation; change only the operative redundancies.
s=next(s['source_xml']for s in sources if s['number']=='R133-14');s=s.strip()
old="La déclaration sociale nominative est accomplie chaque mois même si aucune rémunération n'a été versée au cours de celui-ci tant que l'employeur n'a pas demandé la radiation de son compte auprès de l'organisme de recouvrement des cotisations de sécurité sociale dont il relève, ou obtenu de ce dernier l'autorisation de ne plus l'adresser en l'absence d'emploi salarié."
new="La déclaration sociale nominative reste accomplie chaque mois lorsqu’un emploi salarié ou assimilé est maintenu, même sans rémunération, ou lorsqu’un versement ou une régularisation relevant de l’article L. 133-5-3 doit être déclaré. Après la fin déclarée du dernier contrat et en l’absence de tout salarié ou assimilé, de rémunération, de revenu de remplacement et de régularisation à déclarer, aucune déclaration mensuelle à néant n’est requise. Cette dispense ne nécessite ni radiation du compte ni autorisation préalable. La déclaration reprend, aux échéances du présent article, dès une nouvelle embauche ou dès qu’un versement ou une régularisation déclarable intervient."
assert old in s;s=s.replace(old,new)
old="8° La déclaration prévue au 1 du II de l'article 1586 octies du code général des impôts ;"
new="8° Pour les seules anciennes années demeurant soumises à la CVAE, la déclaration prévue au 1 du II de l’article 1586 octies du code général des impôts. Aucune donnée propre à une déclaration de CVAE n’est exigée pour les années supprimées par l’article 1586 ter du même code ; les données nécessaires aux droits sociaux, à la CFE ou aux autres finalités maintenues restent déclarées dans leur champ propre ;"
assert old in s;s=s.replace(old,new)
s+='''<p>VII. – Les données stables légalement détenues et réutilisables pour cette déclaration sont préremplies ou reprises automatiquement ; le déclarant n’en effectue pas une nouvelle saisie manuelle à chaque période. Les organismes destinataires disposent néanmoins des données complètes et à jour nécessaires aux finalités maintenues. Les données variables de paie et d’activité et les rectifications requises restent déclarées. La transmission unique ne supprime aucune ouverture de droit, exonération, déduction, garantie ou exception prévue au présent article.</p>'''
put('R133-14',s)
reasons={
'D133-12-1':'Clarifie les personnes assimilées pour les seules formalités simplifiées, sans requalification du service ni perte des régimes favorables.',
'D133-13':'Fusionne adhésion et première déclaration et supprime les ressaisies de coordonnées déjà accessibles, sans imposer un nouveau mandat bancaire périodique.',
'D133-13-1':'Supprime la transmission d’identification séparée lorsqu’elle accompagne la première déclaration ; maintient la remise au salarié et les échéances légales d’embauche, et préserve la suppression déjà retenue de la pénalité L1221-11.',
'D133-13-2':'Remplace la répétition mensuelle d’état civil par un profil réutilisable et ses seuls changements, en gardant les données variables nécessaires aux droits.',
'D133-13-3':'Automatise les documents dus dans le délai de quatre jours et reprend le récapitulatif brut/net déjà retenu à L133-5-8, sans retirer de mentions protectrices.',
'D133-13-4':'La transmission unique des arrêts et fins de contrat remplace les attestations portant sur les mêmes données ; aucun droit maladie, chômage ou naissance n’est supprimé.',
'D133-13-5':'Conserve le choix brut/net et les paramètres stables ; supprime la seconde saisie des congés ou absences déjà signalés et garde les effets de paie.',
'D133-13-6':'Supprime l’exigibilité anticipée due au seul retard déclaratif avant l’échéance normale du deuxième mois ; conserve les obligations déjà échues et les droits à réduction.',
'D133-13-7':'Empêche les conventions internes de recouvrement de créer des déclarations supplémentaires ou une contribution nouvelle ; maintient l’affectation et les règles de frais existantes.',
'D133-13-8':'La déclaration simplifiée vaut déclaration des salariés payés par titres, sans formalité parallèle du seul fait du moyen de paiement.',
'D133-13-9':'La déclaration mensuelle réutilise le profil sans toucher au cinquième jour ni aux échéances et protections de paiement.',
'D133-13-10':'Les attestations de crédits d’impôt et d’abattement sont délivrées automatiquement en mars, sans demande annuelle additionnelle.',
'D133-13-11':'Supprime le refus automatique de l’intermédiation après le quinzième jour ; conserve consentement écrit, délais de versement, limites de paiement partiel et exclusions prudentielles.',
'D133-13-11-1':'Conserve intégralement les plafonds et les catégories majorées, avec réutilisation des pièces d’une situation inchangée.',
'D133-13-11-2':'Supprime les demandes répétées et l’attente systématique du mois suivant après régularisation ; les exclusions pour fraude, durées maximales et recours sont conservés.',
'D133-13-12':'Supprime la ressaisie de coordonnées, agréments et choix annuels, automatise la date électronique et répare le renvoi devenu inexact du calcul des congés vers L3141-24.',
'D133-13-13':'Réutilise mandat et option de prélèvement et protège le solde après allègements, sans changer le mois d’exigibilité ni rendre obligatoire l’option avancée.',
'D133-13-14':'Conserve le paiement direct départemental et le troisième mois, en retirant les nouvelles preuves mensuelles d’une aide déjà connue.',
'D133-13-15':'Le contrôle par rapprochement des titres reçus remplace la seconde déclaration des mêmes salariés ; les vérifications d’anomalies restent possibles.',
'D133-13-16':'Fusionne l’identification initiale avec la première déclaration et supprime les coordonnées déjà vérifiées ; l’agrément protecteur de l’enfant est maintenu.',
'D133-13-17':'Réutilise les profils de l’employeur, des enfants et du salarié, avec saisie sécurisée directe du compte par le salarié et maintien de toutes indemnités.',
'D133-13-18':'Réutilise le mandat et prélève le seul solde après droits et paiements ; garde le délai de deux jours ouvrés et les aides futures.',
'D133-13-19':'Supprime le plafond réglementaire de trois heures hebdomadaires pour un service ponctuel à durée convenue, sans permettre une fausse qualification d’activité permanente.',
'D133-13-20':'Rend explicite la démarche commune unique pour les particuliers prestataires et conserve tous décomptes, aides et garanties du renvoi.',
'R133-14':'Supprime l’autorisation de cesser les DSN à néant après la fin de tout emploi, préserve les contrats sans salaire, et retire les données CVAE des années supprimées.'}
benefits={
'D133-12-1':'Les salariés, personnes au pair, accueillants et prestataires ponctuels conservent chacun leur accès au dispositif et leurs droits propres. Les assimilations de vocabulaire ne servent pas à supprimer une prestation ou à créer une requalification automatique.',
'D133-13':'L’adhésion simplifiée reste ouverte aux entreprises, associations et particuliers éligibles. L’exception papier prévue par la loi demeure applicable ; aucun nouveau tarif, retrait d’aide ou remplacement d’agrément par déclaration n’est créé. Les avantages présents et futurs sont expressément protégés.',
'D133-13-1':'La remise des données d’identification au salarié reste obligatoire et protège sa preuve d’emploi. Le regroupement administratif ne retire ni les formalités déjà accomplies à son bénéfice ni son accès à la protection sociale et au dispositif simplifié. La suppression déjà retenue de la pénalité L1221-11 est conservée ; la DPAE légalement maintenue reste à son échéance propre.',
'D133-13-2':'Les données variables nécessaires aux cotisations et droits sont toujours transmises. L’absence de NIR n’exclut pas la personne : elle est identifiée par les autres données. La suppression de ressaisie d’un état civil inchangé ne supprime aucun droit ni exonération.',
'D133-13-3':'Bulletin complet, relevé global, relevé d’accueil et décompte du prestataire sont conservés, ainsi que le délai de quatre jours. Le récapitulatif brut/net déjà retenu législativement est coordonné et n’efface ni les exonérations ni les protections de salaire.',
'D133-13-4':'Toutes les causes d’arrêt et de congé, dont le congé supplémentaire de naissance de 2026, restent couvertes ; les revenus de référence des IJ et les données chômage sont conservés. Les dispositions transitoires favorables ne sont pas écrasées par la simplification.',
'D133-13-5':'Choix brut/net, base forfaitaire, frais de transport et frais professionnels non soumis, congés payés et qualité BOETH sont conservés. Seule leur communication répétée sans changement est supprimée ; aucune base fiscale nouvelle ne remplace une réduction.',
'D133-13-6':'Le deuxième mois normal demeure favorable par rapport à l’exigibilité immédiate déclenchée par un simple retard déclaratif. Les cotisations déjà dues ne sont pas effacées, mais les exonérations, prises en charge et paiements antérieurs sont déduits, sans double paiement.',
'D133-13-7':'Le recouvrement mutualisé demeure accessible et les cotisations facultatives ne deviennent pas obligatoires par l’utilisation du service. Le taux forfaitaire historique de non-recouvrement n’est ni inventé ni augmenté ; aucune charge de remplacement n’est créée.',
'D133-13-8':'Le bénéfice des titres spéciaux et du dispositif simplifié demeure disponible aux futurs utilisateurs ; le contrôle n’exige pas un second formulaire identique et aucune aide attachée au paiement par titre n’est supprimée.',
'D133-13-9':'Le cinquième jour et les dates des deux régimes de paiement sont maintenus. Les règles ne font pas perdre exonérations et prises en charge ; une rectification ne transforme pas une dette acquittée en nouveau prélèvement.',
'D133-13-10':'Les crédits 199 sexdecies et 200 quater B et l’abattement 80 sexies restent justifiables pour les bénéficiaires actuels et futurs. Les attestations de mars, leur correction et l’accès papier légal sont maintenus ; aucune suppression d’avantage sous prétexte de dématérialisation.',
'D133-13-11':'Le service est ouvert aux déclarations tardives sans réduire le salaire dû ni reporter son échéance. Accord écrit préalable, compte du titulaire, délais de deux/quatre jours et exclusions de fraude ou impayé sont maintenus. Aucun financement garanti d’une prestation fictive n’est créé.',
'D133-13-11-1':'Les plafonds 10 000 euros pour invalidité/charge d’une personne invalide ou enfant ouvrant droit au complément AEEH, 6 000 euros autrement et 1 150 euros par enfant de moins de six ans restent intacts. La majoration demeure ouverte aux futurs foyers éligibles.',
'D133-13-11-2':'Le contrôle de réalité, les exclusions légales d’impayé/surendettement et les durées maximales cinq ans/six mois restent. La dérogation favorable de garde d’enfants et les recours sont maintenus. Réception plutôt qu’envoi déclenche les trente jours de justificatifs, et le rétablissement après conditions remplies ne dépend plus d’un mois d’attente.',
'D133-13-12':'Les indemnités de congés, option du dixième et calcul avec maintien du salaire, indemnités d’accueil, base au pair et frais professionnels subsistent. Le renvoi de calcul vers L3141-24 est actualisé après lecture de L3141-22 et -24, sans changer les seuils trente-deux heures ni les options.',
'D133-13-13':'L’échéance du deuxième mois et l’option volontaire de prélèvement lors du paiement salarial sont préservées. Les aides et réductions sont imputées avant recouvrement ; aucun nouveau mandat mensuel ni nouveau prélèvement n’est imposé.',
'D133-13-14':'Le paiement direct du département évite l’avance de la fraction aidée ; le troisième mois et le reste à charge individualisé sont conservés. Les plans d’aide APA/PCH restent à leurs plafonds propres et ouverts aux nouveaux allocataires.',
'D133-13-15':'Les titres spéciaux conservent leur mode d’emploi et les contrôles restent possibles sur anomalies. La suppression de déclarations répétées ne supprime ni aide, ni crédit d’impôt, ni droit social afférent à une période déclarée.',
'D133-13-16':'La garde d’enfant et les assistants maternels agréés restent identifiés correctement, avec prise en compte de l’agrément et de son renouvellement. L’adhésion groupée facilite l’accès aux aides sans supprimer une garantie liée à l’enfant.',
'D133-13-17':'Indemnités d’entretien, jours d’absence indemnisés, accueil vingt-quatre heures, majoration de salaire, frais et horaires spécifiques demeurent déclarés et pris en compte. Les dates de naissance connues sont réutilisées sans supprimer l’accès au CMG et aux avantages correspondants.',
'D133-13-18':'Les exonérations et prises en charge restent déduites pour les bénéficiaires présents et futurs. Les deux jours ouvrés source sont conservés ; aucune avance supplémentaire ni deuxième recouvrement n’est créé lors d’une correction.',
'D133-13-19':'L’ouverture au-delà de trois heures élargit un dispositif administratif favorable sans changer taux ou prestations. Le caractère ponctuel, l’usage personnel et la rémunération déclarée restent requis ; droits attachés à une relation de travail effective et autres avantages sont conservés.',
'D133-13-20':'Les règles de décomptes, attestations et aides incluses dans les renvois restent applicables aux prestataires ponctuels, y compris futurs. La suppression du doublon de démarche ne supprime aucune catégorie favorable ni condition protectrice.',
'R133-14':'La dispense de DSN à néant est strictement bornée à aucun salarié, revenu de remplacement, rémunération ou correction à déclarer. Les droits du salarié sans salaire et toutes exceptions favorables de signalement sont préservés. Seules les données exclusivement CVAE disparaissent pour les années dont la taxe est supprimée, sans retirer les données de CFE et de droits sociaux.'}
rows=[]
for s in sources:
 n=s['number'];p=draft[n]
 note='Lecture entière du corps source, de ses notes et des renvois utiles conservés dans references.json, direct-links.json et dsn-law-links.json, ainsi que des propositions législatives déjà retenues. Les 24 D133 et R133-14 ne possédaient aucune proposition au relevé initial ; contrôle de concurrence final requis. La suppression vise les répétitions et contraintes identifiées, sans taux nouveau ni réduction de prestation. Les dispositions favorables restent applicables aux bénéficiaires futurs. Aucun enregistrement par cet auteur.'
 if n=='D133-13-19':note+=' Réforme de fond explicite : la durée de chaque service reste déterminée par son objet et l’accord des parties, en application du 8° de L133-5-6 qui délègue au décret la précision de la durée ; le plafond hebdomadaire de trois heures est supprimé. Le champ ponctuel légal ne devient pas un statut d’activité permanente.'
 if n=='D133-13-12':note+=' Anomalie source explicitement corrigée : L3141-22 traite aujourd’hui du report des congés ; L3141-24 porte le calcul de l’indemnité du dixième et le minimum de maintien de salaire. Les deux sources actuelles entières et notes ont été lues, sans prétendre que l’ancien renvoi est la règle actuelle de calcul.'
 if n in ['D133-13-4','R133-14']:note+=' Le congé supplémentaire de naissance et ses notes transitoires de juillet 2026 sont conservés ; les notes historiques ne deviennent pas une nouvelle date de réforme.'
 row={k:s[k]for k in['code_id','source_id','source_sha256','number']}|{'status':'rewrite_draft','proposed_xml':p,'proposed_sha256':sha(p),'reason':reasons[n],'review_notes':note,'source_body_sha256':s['source_body_sha256'],'source_notes_sha256':s['source_notes_sha256'],'current_beforeimage_sha256':None,'benefit_review':benefits[n]}
 rows.append(row)
validate_answer(rows,sources)
(H/'answer.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');print('VALID',len(rows),sha((H/'answer.json').read_text()))
