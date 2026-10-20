import json, re, html
from pathlib import Path
src=json.loads(Path('source.json').read_text())
refs=json.loads(Path('reference-targets.json').read_text())
rows=[]
for s in src:
 p=s['previous_draft']
 rows.append({**{k:s[k] for k in ['code_id','source_id','source_sha256','number']},'proposed_xml':p['proposed_xml'],'reason':p['reason'],'review_notes':p['review_notes'],'status':'rewrite_draft'})
by={r['number']:r for r in rows}
def paras(*texts): return ''.join('<p>'+html.escape(t,quote=False)+'</p>' for t in texts)
def reduction(n,items):
 by[n].update(change_type='normative_reduction',reform_policy_id='editorial_direction_2026_10_19',removed_provisions=items)
def plain(xml):
 return re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',xml))).strip()
def effect(n,kind,mid,description,before,after,unit,pop,transition,replacement,sq,pq):
 assert len(sq)>=12 and sq in plain(next(s['source_xml'] for s in src if s['number']==n)),(n,'SOURCE QUOTE',sq)
 assert len(pq)>=12 and pq in plain(by[n]['proposed_xml']),(n,'PROPOSED QUOTE',pq)
 return dict(kind=kind,measure_id=mid,description=description,before=before,after=after,unit=unit,affected_population=pop,conditions_and_transition=transition,replacement_or_new_burdens=replacement,source_quote=sq,proposed_quote=pq)
def impact(n,classification,assessment,limits,burdens,effects):
 by[n]['substantive_impact']=dict(version=1,classification=classification,assessment=assessment,scope_limitations=limits,new_burdens_review=burdens,effects=effects)

# Garanties existantes : les réformes de coordination du premier brouillon sont conservées.
by['R6222-23-1']['reason']="Après seconde lecture intégrale, maintien des deux dérogations de durée et de la dispense de convention déjà prévues par la source. La modification de fond est une coordination avec le contrat unique : la reprise d'apprentissage aménage une période pédagogique, sans créer un nouvel emploi à terme. Aucune suppression supplémentaire n'est justifiée dans cet article qui accorde déjà exclusivement des allègements ; la dispense de convention ne constitue pas un gain nouveau."
by['R6222-23-1']['benefit_review']="Les avantages identifiés sont la dérogation au minimum de six mois de L. 6222-7-1, celle au minimum de formation en centre du cinquième alinéa de L. 6211-2 (25 %, sous les réserves du certificateur), et la dispense de signature de la convention de réduction. Ils restent ouverts aux reprises futures éligibles et aux anciens contrats, sans déclaration de remplacement. La poursuite de formation théorique de six mois et le statut de stagiaire de L. 6222-18-2 demeurent dans leur champ, notamment ses exceptions transfrontalières ; les six mois ne deviennent pas un terme de l'emploi."
by['D6222-28-1']['reason']="La seconde passe conserve l'assimilation salariale du cycle complet dans chacun des trois cas de réduction de formation. Retirer cette obligation de salaire supprimerait un avantage de l'apprenti, sans retirer un doublon administratif. La coordination avec le contrat unique et la séparation entre période pédagogique et durée de l'emploi restent nécessaires ; aucun allègement supplémentaire ni nouveau taux de salaire n'est décidé."
by['D6222-28-2']['reason']="La seconde passe conserve le minimum salarial de la dernière année pendant la prolongation pédagogique et son renvoi dynamique à D. 6222-26. Il protège la rémunération et ne double pas la garantie de cycle réputé accompli de D. 6222-28-1, qui vise le cas inverse. La seule réforme est la coordination de la durée pédagogique avec l'emploi sans terme ; aucune réduction supplémentaire de salaire ou de droit n'est justifiée."

# Abrogation de l'obligation spéciale de preuve, sans suppression des compétences autonomes.
n='R6223-1'
by[n]['proposed_xml']=paras(
"Le présent article est abrogé pour les demandes de pièces présentées à compter de l'entrée en vigueur de la loi portant réforme du contrat de travail, y compris lorsqu'elles concernent un contrat conclu antérieurement. L'obligation spéciale imposant à l'employeur de produire les pièces attestant le respect des déclarations du contrat d'apprentissage et des conventions de formation et d'aménagement de durée cesse de s'appliquer à ces demandes. Aucun dossier justificatif, attestation ni déclaration de remplacement n'est exigé sur ce fondement.",
"Cette abrogation ne porte atteinte ni aux pouvoirs de présentation et de communication de documents que l'inspection du travail tient d'autres dispositions, ni au contrôle pédagogique des formations, ni aux vérifications nécessaires à la prise en charge financière et au dépôt du contrat dans les conditions qui leur sont propres. Elle ne dispense pas de respecter les obligations de santé, de sécurité, de rémunération et de formation.",
"Les demandes régulièrement présentées avant cette entrée en vigueur et les recours qui s'y rapportent demeurent régis par les dispositions antérieures, sous réserve de l'application de la loi répressive plus douce aux sanctions non définitives. Aucun document déjà régulièrement communiqué n'est à transmettre de nouveau au seul motif de la présente abrogation.")
by[n].update(change_type='full_repeal',repeal_policy_id='editorial_direction_2026_10_19',repeal_scope="Suppression prospective de l'obligation spéciale de justification de toutes les déclarations du contrat et des conventions d'apprentissage sur le fondement de R6223-1 ; maintien des pouvoirs de contrôle légalement autonomes.")
by[n]['reason']="Au lieu de répéter le droit au réemploi des pièces du précédent brouillon, abrogation de l'obligation spéciale de produire des preuves de l'ensemble des déclarations contractuelles. L'inspection dispose déjà de pouvoirs légaux de présentation et communication, la mission pédagogique d'un pouvoir de communication des pièces utiles et l'opérateur d'une vérification propre au financement. La suppression retire ce fondement cumulatif de demandes, sans promettre la disparition de toute preuve utile ni neutraliser un contrôle essentiel."
by[n]['review_notes']="Fondements autonomes lus en entier dans le corpus public : L. 8113-4 (documents obligatoires présentés en visite), L. 8113-5 (communication utile dans ses domaines limitativement visés, dont santé, discrimination et harcèlement), R. 6251-2 (documents utiles au contrôle pédagogique) et D. 6224-2 (contrôle pour prise en charge et refus motivé). Ces références, absentes des cibles imposées, sont documentées ici sans ajout à reference_checks. Leurs champs ne sont pas étendus. L. 6222-4, L. 6353-1 et L. 6222-7-1 continuent d'imposer les écrits et accords requis. D. 6235-6, lu, garde un régime transfrontalier autonome : il n'est pas abrogé par cet article. L'abrogation du devoir spécial ne constitue donc pas une dispense générale de pièces ni une baisse de coût chiffrée."

# Dossier privé : document commun satisfaisant toutes les signatures existantes.
n='D6224-1'
by[n]['proposed_xml']=paras(
"Au plus tard dans les cinq jours ouvrables qui suivent le début de l'exécution du contrat d'apprentissage, l'employeur transmet ce contrat à l'opérateur de compétences, accompagné de la convention mentionnée à l'article L. 6353-1 et, le cas échéant, de la convention tripartite prévue au troisième alinéa de l'article L. 6222-7-1, sous réserve des dispenses applicables.",
"Lorsque la formation de l'apprenti est confiée à un centre de formation d'apprentis constituant un service interne de l'entreprise, mentionné à l'article D. 6241-30, l'employeur transmet le contrat, la convention tripartite lorsqu'elle est requise et les informations pédagogiques et financières suivantes : l'intitulé, l'objectif et le contenu de l'action de formation, les moyens prévus, la durée et la période de réalisation, les modalités de déroulement, de suivi et de sanction de l'action ainsi que son prix.",
"Les transmissions prévues au présent article peuvent être effectuées par voie dématérialisée.",
"À compter de l'entrée en vigueur de la loi portant réforme du contrat de travail, les pièces et informations exactes et à jour déjà légalement accessibles à l'opérateur ne lui sont pas transmises à nouveau. Les informations pédagogiques et financières peuvent figurer dans un ou plusieurs documents du dossier ; aucune annexe séparée n'est exigée. La convention de formation peut également tenir lieu de convention d'aménagement de durée lorsqu'elle en contient les éléments et recueille l'accord écrit de toutes les parties dont la signature est requise. Elle demeure annexée au contrat dans les conditions prévues au troisième alinéa de l'article L. 6222-7-1, sans document ou signature en double. Ces règles s'appliquent aux dépôts restant à accomplir et aux dossiers en cours, sans nouveau dépôt ni reprise des délais.",
"Pour les contrats uniques à durée indéterminée conclus à compter de cette entrée en vigueur, les durées indiquées pour l'apprentissage concernent la période pédagogique et ne fixent pas un terme à l'emploi. Lorsqu'une mise à jour est requise pour la prise en charge d'une nouvelle période d'apprentissage dans un emploi dont le contrat a déjà été déposé, seuls les éléments nouveaux sont transmis ; le contrat n'est pas déposé à nouveau. Les contrats antérieurs et les décisions de financement valables conservent leurs effets, sans permettre la conclusion ni le renouvellement d'un contrat à durée déterminée après cette entrée en vigueur.")
reduction(n,["Suppression de l'annexe pédagogique et financière matériellement distincte lorsque les informations figurent dans les documents du dossier.","Suppression du support séparé de convention d'aménagement lorsque la convention commune comporte les mêmes éléments et toutes les signatures requises.","Suppression du nouveau dépôt intégral du contrat déjà déposé pour la seule prise en charge d'une autre période pédagogique dans le même emploi."])
by[n]['reason']="Les suppressions de supports et de dépôt répétés du précédent brouillon sont conservées. Le texte exige désormais explicitement que le document commun vaille convention tripartite, avec les parties requises et l'annexion légale : il ne prétend plus que le seul règlement R. 6222-6 aurait effacé cette exigence législative. Le délai de cinq jours ouvrables et toutes les données pédagogiques et financières sont maintenus pour permettre une prise en charge rapide et contrôlable ; leur suppression supplémentaire priverait l'apprenti de garanties de financement sans doublon démontré."
by[n]['review_notes']="L. 6224-1 et D. 6224-2 lus intégralement : maintien du dépôt, des critères d'âge, de formation, de maître d'apprentissage, de rémunération, de sécurité et de certification ainsi que du refus motivé. Le délai de cinq jours est ouvrable, distinct du préavis individuel. L. 6222-7-1 conserve dans la cible fournie la convention tripartite annexée : le document commun doit satisfaire cette règle, et non seulement l'accord de l'acheteur et du centre prévu à L. 6353-1. La proposition de R. 6222-6 permet l'intégration, mais n'est pas du droit en vigueur. Réemploi des pièces déjà accessibles : coordination du droit existant, sans gain autonome compté. La mise à jour de période et l'absence de second dépôt doivent être raccordées à D. 6224-2 à D. 6224-7 ; aucun financement automatique n'est institué."

# Intérim : moins de reproduction et transmission de seuls éléments pédagogiques.
n='R6226-3'
by[n]['proposed_xml']=paras(
"I.-Pour les contrats de mission conclus avant l'entrée en vigueur de la loi portant réforme du contrat de travail, les mentions prévues à l'article L. 1251-16 sont complétées par celles du contrat de mise à disposition de l'apprenti prévues à l'article R. 6226-2. Pour les emplois conclus à compter de cette entrée en vigueur, ces informations sont communiquées à l'apprenti dans le cadre du contrat unique à durée indéterminée et de la lettre de mission relative à son affectation. Les informations exactes et applicables à l'affectation qui figurent déjà dans un écrit régulièrement remis à l'apprenti sur un support qu'il peut conserver ne sont pas reproduites ; seules les informations manquantes ou modifiées lui sont communiquées. Aucun renvoi écrit supplémentaire ni attestation de remise propre au présent article n'est exigé lorsque cette communication est déjà établie.",
"II.-L'entreprise de travail temporaire adresse au directeur du centre de formation d'apprentis, dès la conclusion du contrat de mission antérieur à la réforme ou de la lettre de mission du contrat unique, les informations relatives à l'affectation nécessaires au suivi de la formation, notamment les mentions prévues à l'article R. 6226-2. À compter de cette entrée en vigueur, l'envoi intégral du contrat de mission n'est plus exigé sur le fondement du présent article. Les documents et informations exacts et à jour déjà légalement accessibles au directeur ne sont pas envoyés de nouveau. L'entreprise l'informe de tout changement du maître d'apprentissage désigné au sein de l'entreprise utilisatrice.",
"III.-La suspension du contrat d'apprentissage en application de l'article L. 6225-4 suspend également le contrat de mission antérieur ou, pour le contrat unique, l'affectation de l'apprenti. Le maintien de rémunération prévu par cet article demeure applicable. La rupture prononcée en application de l'article L. 6225-5 met également fin au contrat de mission antérieur ou à l'affectation, sans supprimer les garanties et sommes dues à l'apprenti sur ce fondement. La seule suspension ou fin d'une affectation ou d'une période pédagogique ne rompt pas le contrat unique à durée indéterminée ; elle ne se confond pas avec la rupture de sécurité expressément prévue par l'article L. 6225-5.",
"Les dispenses de reproduction et les modalités de communication du présent article s'appliquent aux écrits et envois restant à établir ou à accomplir à compter de cette entrée en vigueur, y compris pour les contrats antérieurs, sans refaire les écrits ou envois déjà valables. Ces contrats conservent leurs règles de durée et leurs droits acquis. Aucune nouvelle affectation ne permet de conclure ou renouveler un contrat de travail à durée déterminée ni de stipuler un nouvel essai du seul fait de la mission. La garantie mensuelle de rémunération et la prise en compte des intermissions du contrat intérimaire à durée indéterminée demeurent applicables dans leur champ.")
reduction(n,["Suppression de la recopie des mentions d'apprentissage déjà régulièrement communiquées par écrit et applicables à l'affectation.","Suppression de la transmission intégrale du contrat de mission au centre, remplacée par les seuls éléments nécessaires au suivi pédagogique.","Suppression du renvoi écrit supplémentaire imposé par le précédent brouillon lorsque la communication des informations à l'apprenti est déjà établie."])
by[n]['reason']="Le texte conserve les six informations pédagogiques de R. 6226-2, mais retire leur recopie et, au-delà du précédent brouillon, l'envoi intégral du contrat de mission au centre. Il retire aussi le renvoi écrit supplémentaire créé par ce brouillon lorsque les informations sont déjà communiquées. La fusion de l'emploi dans le contrat unique reste une coordination avec L. 1251-16 ; les mesures de sécurité et leurs sommes spéciales sont maintenues, sans appliquer le zéro d'indemnité ordinaire à ces garanties."
by[n]['review_notes']="R. 6226-2 lu : diplôme, travaux liés à la qualification, maître de chaque entreprise, informations de compétence, échanges sur le déroulement et liaison avec le centre sont tous couverts par le renvoi. L. 6225-4 et L. 6225-5 lus : risque sérieux, maintien de salaire, décision administrative sur reprise sous quinze jours et sommes jusqu'au terme du contrat ancien ou de la période pédagogique ; ce délai n'est pas le préavis individuel. Le contrat unique et la lettre de mission relèvent de la proposition législative L. 1251-16, sans nouveau contrat ni nouvel essai par affectation. Les garanties d'intermission et de rémunération minimale de L. 1251-58-2 et L. 1251-58-3 ont été lues dans le corpus ; leur extension aux nouveaux emplois peut accroître les obligations de l'entreprise et n'est pas une baisse de coût nette démontrée. Les procédures collectives et autorisations spéciales subsistent."

# Envoi transfrontalier unique : charge d'acheminement explicitement transférée.
n='D6235-7'
by[n]['proposed_xml']=paras(
"À compter de l'entrée en vigueur de la loi portant réforme du contrat de travail, dès leur conclusion, les conventions prévues aux articles R. 6223-11 et D. 6271-2 sont adressées à l'opérateur de compétences unique mentionné au IV de l'article L. 6235-5. Celui-ci les transmet sans délai à l'organisme de formation et aux autorités compétentes dans le pays frontalier. L'envoi à l'opérateur accomplit l'obligation d'envoi prévue au présent article à l'égard de ces destinataires ; aucun nouvel envoi du même document exact et à jour déjà légalement détenu par un destinataire n'est exigé de l'employeur.",
"Lorsque l'employeur est une entreprise de travail temporaire, le contrat de mission conclu avant cette entrée en vigueur est adressé une seule fois à l'organisme chargé du dépôt, qui le transmet sans délai aux autorités compétentes dans le pays frontalier. Pour un nouvel emploi relevant du contrat unique français à durée indéterminée, les informations nécessaires relatives à l'affectation sont reprises des documents existants du contrat unique et de la mise à disposition ; elles suivent le même circuit, sans contrat de travail à durée déterminée ni déclaration équivalente. Chaque destinataire reçoit les seules données nécessaires à ses compétences et légalement transmissibles.",
"Ces règles s'appliquent aux envois restant à accomplir à compter de cette entrée en vigueur, y compris pour les conventions et contrats antérieurs. Les envois déjà valablement effectués ne sont pas refaits. Les transmissions antérieures conservent leurs effets. Les communications directement requises par une convention internationale applicable demeurent régies par celle-ci. La durée de l'accueil, de la formation ou de l'affectation ne met pas, à elle seule, fin à l'emploi à durée indéterminée.")
reduction(n,["Suppression des envois parallèles des mêmes conventions par l'employeur à l'organisme de formation et aux autorités étrangères, sous réserve des obligations conventionnelles internationales distinctes.","Suppression de l'envoi parallèle du contrat de mission par l'entreprise aux autorités étrangères après son dépôt auprès de l'organisme compétent."])
by[n]['reason']="La seconde passe maintient le guichet d'envoi unique du précédent brouillon, en rendant explicites son application prospective et la continuité d'acheminement. Elle retire plusieurs envois privés, mais en transfère l'exécution à l'opérateur et à l'organisme de dépôt : le bilan est mixte, sans économie nette présumée. Supprimer les destinataires ou les conventions elles-mêmes compromettrait le suivi transfrontalier, la répartition de rémunération, de frais et de responsabilité ; aucune coupe supplémentaire n'est justifiée sur ces éléments."
by[n]['review_notes']="R. 6223-11 et D. 6271-2 lus entièrement : responsabilités d'accueil, durée, diplôme, tâches, horaires, maîtres, salaires, transport, hébergement et responsabilité civile restent définis. D. 6271-2 prévoit déjà l'envoi au centre puis au représentant de l'État : coordonner ce circuit pour que le guichet unique dispense réellement l'employeur d'un envoi cumulé. L. 6235-5 IV conserve l'opérateur unique et son agrément propre ; le présent texte ne supprime pas cet agrément institutionnel par inadvertance. L. 6235-2 réserve les obligations bilatérales : leur texte n'est pas joint et aucune dispense étrangère n'est acquise. La réception des informations nécessaires demeure exigée, avec acheminement à la charge des organismes ; coût public et éventuelles obligations internationales résiduelles non chiffrés."

# Allègement de la durée individuelle de formation et suppression d'autorisation.
n='D6235-13'
p=by[n]['proposed_xml']
p=p.replace("La durée aménagée ne peut être inférieure à six mois ni supérieure à trois ans, sous réserve des dérogations et prolongations prévues par la présente section.","L'aménagement n'est soumis à aucune durée minimale de six mois ; sa durée est déterminée au regard des compétences ainsi évaluées et des exigences de la certification préparée. Il ne peut conduire à une durée supérieure à trois ans, sous réserve des prolongations prévues par la présente section. Les évaluations déjà réalisées et toujours pertinentes sont réutilisées, sans nouvelle évaluation imposée du seul fait de l'aménagement.")
p=p.replace("La suppression d'autorisation prévue au 8° s'applique aux admissions examinées", "La suppression du minimum de durée aménagée au 2° s'applique aux aménagements examinés et la suppression d'autorisation prévue au 8° s'applique aux admissions examinées")
by[n]['proposed_xml']=p
reduction(n,["Suppression du minimum de six mois pour une durée effective de formation individuellement aménagée après évaluation des compétences, sans supprimer les exigences de certification.","Suppression de l'autorisation du directeur du dernier centre pour une troisième formation par apprentissage de même niveau après deux contrats successifs, sans déclaration de remplacement."])
by[n]['reason']="Les onze subdivisions et les avantages de prolongation ou de réduction sont conservés. Outre l'autorisation de troisième formation déjà supprimée au précédent brouillon, la seconde passe retire le plancher de six mois pour la durée effectivement aménagée après évaluation des compétences. La durée ordinaire du cycle de six mois à trois ans, le plafond aménagé de trois ans sous réserve des prolongations et les exigences de certification subsistent : un temps de formation artificiellement prolongé n'est plus imposé à un apprenti déjà compétent. L'emploi étranger reste soumis à son régime applicable."
by[n]['review_notes']="Contrôle des onze rubriques : cycle ordinaire de six mois à trois ans au 1°, compétences évaluées au 2°, cycle suivant au 3°, un an maximal après échec au 4°, prolongation du temps partiel au 5°, début en centre sous trois mois au 6°, déduction des mois de stage au 7°, autorisation supprimée au 8°, dérogation de reprise au 9°, trois diplômes de réorientation et réduction d'une année au 10°, coopération au 11°. Rectification du précédent brouillon : L. 6235-4 II 2°, lu intégralement, exclut le titre II du livre II pour la partie pratique effectuée dans le pays frontalier, sauf L. 6222-18-2, L. 6222-34 et L. 6222-36-1. L. 6222-15 n'impose donc pas directement son autorisation dans ce champ ; le fondement actuel est le 8° ici supprimé. Le renvoi du 2° à L. 6222-7-1 désigne les compétences, sans importer un terme d'emploi ni rétablir le minimum aménagé supprimé. D. 6235-12 exclut de même l'essentiel du titre II réglementaire. Les règles du certificateur et la convention internationale L. 6235-2 doivent être respectées ; aucun texte bilatéral joint ne démontre l'absence de toute contrainte étrangère. Les demandes de l'employeur au 10° ne dispensent pas des accords nécessaires à une modification de formation."
by[n]['benefit_review']="Les avantages possibles sont l'adaptation à la baisse ou à la hausse selon les compétences (2°), la prolongation après suspension indépendante de l'apprenti (3°), l'année supplémentaire après échec (4°), l'allongement adapté au temps partiel et son calendrier (5°), la réduction des mois de stage antérieurs (7°), la dérogation de reprise après rupture (9°) et la réorientation vers CAP, CAP agricole ou brevet professionnel agricole avec réduction d'une année dans le même domaine (10°). Tous restent ouverts aux futures situations éligibles et aux aménagements acquis. S'y ajoutent la suppression d'autorisation au 8° et celle du plancher de six mois de la durée individuellement aménagée au 2°. Le cycle ordinaire du 1°, le délai d'accès à la formation au 6° et la coopération au 11° ont une fonction pédagogique ou protectrice, et ne sont pas des prélèvements supprimables. La garantie de six mois de poursuite et le statut de stagiaire de L. 6222-18-2 gardent leur champ légal transfrontalier ; ils ne sont ni une durée d'emploi ni supprimés."

# Secteur public : supprimer la désignation parallèle lorsque le service existant assure la médiation.
n='D6274-1'
by[n]['proposed_xml']=paras(
"Pour les employeurs publics mentionnés à l'article L. 6227-1, un médiateur est désigné pour résoudre les différends avec l'apprenti ou son représentant légal relatifs à l'exécution ou à la rupture du contrat d'apprentissage. À compter de l'entrée en vigueur de la loi portant réforme du contrat de travail, la médiation de ces différends peut être assurée par le service de ressources humaines de proximité dont relève l'apprenti ; la désignation d'un médiateur distinct n'est pas exigée lorsque ce service assure la médiation.",
"La médiation prévue à l'article L. 6222-18 est assurée par l'un ou l'autre de ces intervenants. Elle est mise en œuvre dans les conditions de l'article D. 6222-21-1 applicables au contrat concerné, sans cumuler le régime antérieur et celui du contrat unique.",
"Les médiations déjà engagées et les désignations valablement intervenues avant cette entrée en vigueur conservent leurs effets. La dispense de désignation distincte s'applique également pour les contrats antérieurs. Elle ne modifie pas le régime de durée et de rupture applicable aux apprentis du secteur public ; le régime du contrat unique ne s'applique qu'aux emplois que la loi y soumet expressément. L'accès à la médiation, la protection du mineur et le recours au juge demeurent ouverts.")
reduction(n,["Suppression de l'obligation de désigner un médiateur distinct lorsque le service de ressources humaines de proximité assure déjà la médiation des apprentis publics."])
by[n]['reason']="Le précédent brouillon ne faisait qu'une réécriture à droit constant. La seconde passe supprime la désignation obligatoire d'un médiateur parallèle lorsque le service de proximité, déjà habilité par le deuxième alinéa source, assure la médiation. La fonction de médiation, le choix d'un médiateur, la protection du représentant légal et les recours sont conservés. La réforme administrative ne sert pas à imposer implicitement le régime de rupture privé aux employeurs publics."
by[n]['review_notes']="L. 6227-1 et L. 6227-12 lus : champ des personnes et organismes publics et application de l'apprentissage sous exceptions propres. La source impose un médiateur au premier alinéa tout en permettant au second que le service RH assure la médiation de rupture : seule cette duplication de désignation est retirée, sans fermer les différends d'exécution. L. 6222-18 et D. 6222-21-1 proposés mentionnent le service du secteur public dans le régime du contrat unique mais ne constituent pas le droit en vigueur ; vérifier expressément leur périmètre législatif public avant tout raccordement. Les anciens contrats soumis au régime de 2019 gardent cinq jours après saisine puis sept jours après information, les contrats plus anciens leurs propres dispositions ; aucun cumul avec quinze jours n'est créé. Les agents publics ne deviennent pas titulaires de contrats privés par ce règlement."

# Dépôt public, sans actualisation administrative non documentée.
n='D6275-1'
p=by[n]['proposed_xml']
p=p.replace("L'aménagement de durée peut être intégré au document de formation ou de prise en charge, sous réserve de l'accord écrit des parties dont la signature est requise ; aucun second document contenant les mêmes éléments n'est exigé.","Le document de formation ou de prise en charge peut également tenir lieu de convention d'aménagement de durée lorsqu'il contient les éléments de cet aménagement et recueille l'accord écrit de toutes les parties dont la signature est requise. Ce document demeure annexé au contrat dans les conditions prévues au troisième alinéa de l'article L. 6222-7-1 ; aucun second document ni aucune signature en double n'est exigé.")
by[n]['proposed_xml']=p
reduction(n,["Suppression du document d'aménagement de durée séparé lorsque le document commun contient l'aménagement, toutes les signatures requises et reste annexé au contrat."])
by[n]['reason']="Les suppressions de supports redondants du précédent brouillon sont maintenues ; le document commun doit expressément satisfaire les signatures et l'annexion requises par la loi. La seule reprise du droit au réemploi des pièces déjà accessibles n'est pas comptée comme une réduction nouvelle. Le dépôt public, le délai de cinq jours ouvrables et la convention de prise en charge sont nécessaires au contrôle et au financement de la formation ; aucune suppression supplémentaire de leur fonction n'est justifiée."
by[n]['review_notes']="L. 6227-6, lu, maintient la prise en charge des coûts par les personnes publiques et son exception pour les personnes redevables de la taxe d'apprentissage, ainsi que la convention avec le centre. L. 6227-11, lu, fonde le dépôt départemental ; il n'est pas remplacé par un dépôt privé auprès d'un OPCO, sauf régime transfrontalier autonome de L. 6235-4 III. La convention tripartite et son annexion de L. 6222-7-1 ne sont pas effacées par une simple intégration matérielle. La DIRECCTE et son unité départementale correspondent à la dénomination de la source, antérieure aux réorganisations ; l'autorité successeur doit être coordonnée dans les textes organiques non joints, sans concordance inventée. Le délai reste de cinq jours ouvrables. L'emploi public n'est pas soumis par cet article au régime de rupture du contrat unique."

# CPF : une ancienneté générale portable, sans conditions de rattachement ou de récence.
n='D6323-9'
by[n]['proposed_xml']=paras(
"I.-Pour bénéficier d'un projet de transition professionnelle, le salarié justifie de l'ancienneté suivante :",
"1° Au moins vingt-quatre mois, consécutifs ou non, en qualité de salarié, quelle qu'ait été la nature des contrats de travail successifs. Aucune durée minimale dans l'entreprise où la demande est déposée ni aucune période de référence limitant la prise en compte des emplois antérieurs n'est exigée ;",
"2° Abrogé à compter de l'entrée en vigueur de la loi portant réforme du contrat de travail. La condition spécifique de quatre mois en contrat à durée déterminée au cours des douze derniers mois et la période de référence de cinq ans cessent d'être exigées ; les périodes correspondantes sont prises en compte au titre du 1°.",
"Ces conditions d'ancienneté ne s'appliquent pas au salarié qui, dans les vingt-quatre mois précédant sa demande, a connu une absence résultant d'une maladie professionnelle ou une absence d'au moins six mois, consécutifs ou non, résultant d'un accident du travail, d'une maladie ou d'un accident non professionnel, quelle qu'ait été la nature de son contrat de travail. Les autres dispenses prévues à l'article L. 6323-17-2 demeurent applicables.",
"II.-Aucune des périodes suivantes n'est exclue du calcul de l'ancienneté mentionnée au I :",
"1° Périodes d'un contrat d'accompagnement dans l'emploi mentionné à l'article L. 5134-20 ;",
"2° Périodes d'un contrat d'apprentissage mentionné à l'article L. 6221-1 ;",
"3° Périodes d'un contrat de professionnalisation mentionné à l'article L. 6325-1 ;",
"4° Périodes d'un contrat conclu avec un jeune au cours de son cursus scolaire ou universitaire ;",
"5° Périodes d'un contrat à durée déterminée poursuivi par un contrat à durée indéterminée.",
"III.-L'ancienneté est appréciée à la date du départ en formation du salarié.",
"Les présentes règles s'appliquent aux demandes en cours et futures à compter de l'entrée en vigueur de la loi portant réforme du contrat de travail, y compris pour les périodes d'emploi antérieures et pour les contrats uniques à durée indéterminée. Les ouvertures de droits et les décisions favorables antérieures demeurent acquises. Les données et pièces déjà légalement disponibles sont réutilisées sans nouvelle attestation des mêmes périodes. Les dispenses légales et les voies spéciales plus favorables demeurent ouvertes. Aucun nouveau contrat à durée déterminée n'est nécessaire pour exercer ce droit ; la formation ne limite pas la durée de l'emploi.")
reduction(n,["Suppression des douze mois d'ancienneté dans l'entreprise de demande, avec conservation du minimum portable de vingt-quatre mois de salariat.","Suppression de la voie distincte réservée aux CDD, de ses quatre mois récents sur douze et de sa fenêtre de cinq ans ; toutes les périodes de salariat concourent à la voie générale.","Suppression des cinq exclusions de périodes d'emploi pour l'accès à la voie auparavant réservée aux CDD, sans condition de nature du contrat."])
by[n]['reason']="Au-delà de l'élargissement de la voie CDD du précédent brouillon, la seconde passe fusionne les deux voies ordinaires en un minimum unique de vingt-quatre mois de salariat, sans rattachement de douze mois à l'entreprise et sans condition de récence. Les cinq exclusions sont retirées et leurs numéros conservés comme catégories expressément admises. Le minimum salarial total prévu par l'habilitation législative est maintenu, ainsi que les dispenses médicales et légales ; aucune condition de contrat à terme ne ferme le droit après sa suppression."
by[n]['review_notes']="L. 6323-17-2, lu intégralement, impose une ancienneté minimale à fixer par décret mais pas douze mois dans l'entreprise ni une récence de quatre mois : le minimum général de vingt-quatre mois est conservé. Les dispenses pour bénéficiaires de l'obligation d'emploi, réemploi après licenciement économique ou inaptitude sans formation intermédiaire, maladie professionnelle et autres absences restent applicables. La règle du fonds de prévention (durée d'activité dans un métier exposé, dispense propre et cofinancement) demeure distincte, de même que positionnement certifiant, commission, financement et congé de L. 6323-17-1 et L. 6323-17-2. La note du 31 mars 2022 est historique. Les anciens refus définitifs ne sont pas annulés ; une nouvelle demande peut utiliser les règles nouvelles. Coordonner les règlements et formulaires réservés aux anciens CDD sans recréer la contribution CPF-CDD de 1 %. L'élargissement peut accroître les demandes et financements publics, dont le coût n'est pas mesuré."

# CPF spécial : suppression du double seuil cumulatif des intermittents.
n='R6323-9-1'
p=by[n]['proposed_xml']
p=p.replace("justifie de deux cent vingt jours de travail ou cachets répartis sur les deux à cinq dernières années et remplit la condition correspondant à son activité:","remplit la condition correspondant à son activité:") if False else p
p=p.replace("justifie de deux cent vingt jours de travail ou cachets répartis sur les deux à cinq dernières années et remplit la condition correspondant à son activité :", "remplit la condition correspondant à son activité. À compter de l'entrée en vigueur de la loi portant réforme du contrat de travail, il n'est plus exigé qu'il justifie en outre de deux cent vingt jours de travail ou cachets répartis sur les deux à cinq dernières années :")
p=p.replace("La suppression de la condition de 600 heures s'applique", "Les suppressions du seuil cumulatif de deux cent vingt jours ou cachets et de la condition de 600 heures s'appliquent")
p=p.replace("Les règles du présent article ne ferment pas les dispenses légales d'ancienneté.","Les voies spéciales du présent article demeurent ouvertes sans fermer l'accès à la voie générale de l'article D. 6323-9 ni aux dispenses légales d'ancienneté.")
by[n]['proposed_xml']=p
reduction(n,["Suppression du seuil cumulatif de 220 jours de travail ou cachets sur les deux à cinq dernières années, en plus des seuils récents propres à chaque métier du spectacle.","Suppression du sous-seuil de 600 heures dans l'entreprise ou le groupe où est demandée la formation pour les salariés du travail temporaire."])
by[n]['reason']="La seconde passe conserve la suppression des 600 heures dans l'entreprise prévue au brouillon et supprime en outre le cumul de 220 jours ou cachets pour les intermittents. Les seuils d'activité récents propres aux techniciens et artistes suffisent à caractériser leur activité sans double condition. Les 1 600 heures dans la branche sur dix-huit mois, les intermissions, la date d'appréciation et les dispenses restent applicables ; les voies spéciales n'écartent pas l'accès désormais plus portable à la voie générale."
by[n]['review_notes']="Seuils maintenus exactement : spectacle enregistré 130 jours sur vingt-quatre mois ou 65 sur douze ; spectacle vivant 88/44 ; artistes 60 jours ou cachets sur vingt-quatre mois ou 30 sur douze ; intérim 1 600 heures toutes missions sur dix-huit mois. Seuls le cumul supplémentaire de 220 jours/cachets et les 600 heures dans l'entreprise sont supprimés. L. 1251-58-2, lu, assimile les intermissions à du travail effectif pour l'ancienneté ; aucune conversion horaire nouvelle n'est inventée. Le renvoi à D. 6323-9, ajouté et fourni comme source du lot mais non comme cible imposée, ouvre explicitement la voie générale sans remplacer les seuils spéciaux plus favorables. L. 6323-17-1 et L. 6323-17-2 lus : congé, positionnement, décision de prise en charge, règles du fonds de prévention et dispenses sont conservés. Aucun nouveau CDD d'usage n'est autorisé. La dépense de formation induite par l'ouverture n'est pas chiffrée."

Path('answer.partial.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')

# Bilans comparés à la source officielle, sans compter les réemplois CRPA comme gains.
for n,context in {
 'R6222-23-1':("La source accorde déjà les deux dérogations et la dispense de convention. Le texte les conserve pour les reprises futures et précise que la durée réduite porte sur la pédagogie du contrat unique ; aucune obligation existante supplémentaire n'est supprimée.","Les minima de six mois et de formation en centre gardent leurs autres champs ; les exigences autonomes du certificateur et les exceptions transfrontalières demeurent. Aucun gain budgétaire ou administratif global n'est établi.","Aucune charge nouvelle n'est identifiée : ni demande supplémentaire, ni attestation, ni déclaration ne remplace la convention dispensée ; les conditions d'éligibilité existantes sont conservées."),
 'D6222-28-1':("L'assimilation à la durée du cycle pour le salaire existe intégralement dans la source. Son maintien dans le contrat unique est une coordination protectrice et ne démontre ni baisse de prélèvement ni suppression d'une obligation de rémunérer.","L'assimilation concerne la rémunération pendant la période réduite, pas l'ancienneté générale ni une rémunération d'apprenti après formation. Les trois fondements de réduction et la transition de 2020 gardent leur champ.","Aucune charge nouvelle n'est identifiée : la garantie salariale est déjà due ; aucun formulaire, décompte ou taux supplémentaire n'est imposé par sa coordination avec le contrat unique."),
 'D6222-28-2':("Le minimum de salaire de la dernière année pendant une prolongation est déjà dans la source. Le projet conserve ce droit et son calcul par D. 6222-26, en le rattachant à la période pédagogique du contrat unique ; aucun allègement salarial n'est revendiqué.","Les pourcentages, âges et minima conventionnels de D. 6222-26 ne sont pas modifiés. Le champ reste la prolongation d'apprentissage, avec droits antérieurs et transition historique de 2020 conservés.","Aucune charge nouvelle n'est identifiée : le texte maintient le salaire dû et n'ajoute ni justificatif ni démarche pour son bénéfice. Le solde financier de l'ensemble des réformes n'est pas chiffré.")
}.items():
 sq={
 'R6222-23-1':"La signature de la convention de réduction de durée prévue à l'article L. 6222-7-1 n'est pas nécessaire.",
 'D6222-28-1':"l'apprenti est considéré, en ce qui concerne sa rémunération, comme ayant accompli une durée d'apprentissage égale à ce cycle de formation.",
 'D6222-28-2':"le salaire minimum applicable pendant la prolongation est celui correspondant à la dernière année d'exécution du contrat précédant cette prolongation selon les modalités prévues à l'article D. 6222-26."
 }[n]
 pq={
 'R6222-23-1':"La convention de réduction de durée prévue à l'article L. 6222-7-1 n'est pas exigée.",
 'D6222-28-1':"l'apprenti est réputé, pour sa rémunération, avoir accompli une durée d'apprentissage égale à celle de ce cycle.",
 'D6222-28-2':"le salaire minimum applicable pendant la prolongation est celui de la dernière année d'exécution précédant cette prolongation, déterminé selon les modalités prévues à l'article D. 6222-26."
 }[n]
 e=effect(n,'coordination','contrat-unique-duree-indeterminee','Coordination pédagogique du contrat unique avec maintien de la garantie favorable existante.',
 'Garantie déjà applicable aux contrats ou périodes d’apprentissage dans les cas de la source, sans réduction nouvelle.',
 'Même garantie pour les périodes pédagogiques des emplois uniques sans terme et préservation des contrats antérieurs.',
 'regime','Apprentis relevant du cas de reprise, réduction ou prolongation visé par cet article.',
 'Nouveaux contrats uniques à compter de l’entrée en vigueur de la réforme ; contrats antérieurs et droits acquis préservés.',
 'Aucun support, contrôle ou seuil nouveau créé par cette coordination.',sq,pq)
 impact(n,'coordination_only',*context,[e])

n='R6223-1'
impact(n,'material_reduction',
"L'obligation spéciale et cumulative de justifier les déclarations contractuelles à la demande de trois catégories de contrôleurs est abrogée pour les demandes nouvelles. La réduction est celle d'un fondement spécial de production de preuves ; elle ne représente pas la suppression de tous les contrôles ni une seconde réduction CRPA.",
"Les documents obligatoires restent présentables et les pièces utiles au contrôle pédagogique ou financier restent demandables sur leurs fondements autonomes. Les demandes déjà présentées, les règles transfrontalières distinctes et les recours ne sont pas effacés. Le volume de demandes effectivement évitées est inconnu.",
"Aucune charge nouvelle n'est identifiée : aucun registre ni déclaration ne remplace le devoir spécial abrogé. Les pouvoirs autonomes sont réservés dans leurs seuls champs existants, sans procédure de contrôle supplémentaire ni bilan national chiffré.",[
 effect(n,'obligation_removed','apprentissage-justification-speciale-abrogation','Retrait du devoir spécial cumulatif de justification des déclarations du contrat et des conventions.',
 'Obligation de fournir sur demande les pièces attestant les déclarations au titre de R. 6223-1, en plus des pouvoirs autonomes de contrôle.',
 'Aucune obligation de production sur le fondement de R. 6223-1 pour les demandes nouvelles ; preuves utiles toujours accessibles selon les autres textes applicables.',
 'legal_duty','Employeurs d’apprentis, y compris pour un contrat antérieur faisant l’objet d’une demande nouvelle.',
 'Demandes présentées dès l’entrée en vigueur de la loi ; anciennes demandes et recours conservés, sous réserve répressive plus douce.',
 'Aucun dossier de remplacement ; contrôles autonomes de santé, sécurité, pédagogie et financement maintenus.',
 "l'employeur fournit, à la demande de l'inspection du travail, de la mission chargée du contrôle pédagogique mentionnée à l'article R. 6251-1 ou des organismes en charge du dépôt du contrat d'apprentissage, les pièces permettant d'attester du respect des déclarations",
 "Aucun dossier justificatif, attestation ni déclaration de remplacement n'est exigé sur ce fondement.")])

n='D6224-1'
# Le second dépôt lié au changement de forme d'emploi n'est pas une troisième coupe autonome.
by[n]['removed_provisions']=by[n]['removed_provisions'][:2]
impact(n,'material_reduction',
"La source exige une annexe pédagogique et financière et la convention tripartite lorsqu'elle est requise. La proposition retire le support séparé de l'annexe et permet un document commun de conventions. Le dépôt et chaque information de la source restent exigibles ; le réemploi de données déjà accessibles est seulement une coordination du droit existant.",
"Aucun gain nouveau n'est attribué aux informations déjà couvertes par le CRPA ni au seul passage au contrat unique. Le document commun conserve tous les accords et l'annexion légale ; la mise à jour de prise en charge appelle ses coordinations. Les coûts de financement et le solde de complexité des codes ne sont pas mesurés.",
"Aucune charge nouvelle n'est identifiée : document commun facultatif, signatures déjà légalement requises, contenu pédagogique identique, délai de cinq jours ouvrables inchangé et absence de nouvelle attestation. La transmission des seuls éléments nouveaux ne crée pas un nouveau registre.",[
 effect(n,'obligation_merged','apprentissage-documents-communs','Suppression de supports séparés tout en gardant informations, signatures et dépôt.',
 'Dossier avec convention de formation, convention tripartite éventuelle et, pour le CFA interne, annexe pédagogique et financière distincte.',
 'Même contenu utile ; informations de l’annexe dans les documents du dossier et conventions réunissables avec toutes les signatures requises et annexion au contrat.',
 'legal_duty','Employeurs déposant un contrat d’apprentissage, notamment avec CFA interne.',
 'Dépôts restant à accomplir et dossiers en cours dès l’entrée en vigueur ; décisions financières antérieures conservées, sans remise à zéro des délais.',
 'Aucun contenu ou signature supplémentaire ; document commun au choix et signatures des parties déjà requises.',
 "une annexe pédagogique et financière précisant l'intitulé, l'objectif et le contenu de l'action de formation, les moyens prévus, la durée et la période de réalisation, les modalités de déroulement, de suivi et de sanction de l'action et le prix.",
 "Les informations pédagogiques et financières peuvent figurer dans un ou plusieurs documents du dossier ; aucune annexe séparée n'est exigée.")])

n='R6226-3'
# L'élimination du renvoi écrit du brouillon est réelle face au brouillon, pas une troisième réduction de la source.
by[n]['removed_provisions']=by[n]['removed_provisions'][:2]
impact(n,'mixed',
"Par rapport à la source, la recopie des mentions déjà remises est supprimée et l'envoi du contrat de mission intégral au centre est remplacé par les informations pédagogiques utiles. L'affectation relève du contrat unique pour les nouveaux emplois ; la continuité d'emploi et ses garanties peuvent accroître les engagements de l'employeur. Le solde net n'est pas établi.",
"Les six rubriques de R. 6226-2, la sécurité et les indemnités spéciales restent couvertes. Les transmissions au centre demeurent pour le contenu utile. Les obligations de rémunération entre missions et le régime de rupture sont coordonnés avec les cibles législatives, sans nouvelle mesure financière autonome comptée ici.",
"Le contrat unique peut prolonger des obligations d'emploi et de rémunération au-delà d'une mission : cette contrepartie est recensée. Aucun registre, attestation de remise ou renvoi écrit supplémentaire n'est créé ; les informations nouvelles restent communiquées et le maintien de salaire de sécurité existe déjà.",[
 effect(n,'obligation_removed','apprentissage-interim-mentions-sans-recopie','Dispense de recopie des informations déjà effectivement remises à l’apprenti.',
 'Les mentions du contrat de mission sont complétées par celles du contrat de mise à disposition, sans dispense textuelle de répétition.',
 'Les informations exactes et applicables déjà remises sur support conservable ne sont pas reproduites ; seules les lacunes ou modifications sont communiquées.',
 'legal_duty','Entreprises de travail temporaire employant des apprentis et apprentis destinataires.',
 'Écrits restant à établir dès l’entrée en vigueur, y compris contrats antérieurs ; aucun écrit valable à refaire.',
 'L’apprenti reçoit toujours les informations ; aucun renvoi écrit supplémentaire ni attestation spéciale de remise.',
 "les mentions du contrat de mise à disposition de l'apprenti prévues à l'article R. 6226-2.",
 "Les informations exactes et applicables à l'affectation qui figurent déjà dans un écrit régulièrement remis à l'apprenti sur un support qu'il peut conserver ne sont pas reproduites ; seules les informations manquantes ou modifiées lui sont communiquées."),
 effect(n,'compliance_cost_reduced','apprentissage-interim-transmission-pedagogique','Remplacement de l’envoi intégral du contrat au centre par son seul contenu pédagogique nécessaire.',
 'Envoi dès conclusion du contrat de mission intégral au directeur du centre, puis information du changement de maître.',
 'Envoi dès conclusion des informations d’affectation utiles, dont les six rubriques pédagogiques ; le contrat intégral n’est plus exigé par cet article.',
 'legal_duty','Entreprises de travail temporaire et directeurs de CFA.',
 'Envois restant à accomplir dès l’entrée en vigueur, anciens contrats compris ; envois valables non refaits.',
 'Communication utile et mises à jour conservées, sans nouveau formulaire ; coût monétaire non chiffré.',
 "L'entreprise de travail temporaire adresse le contrat de mission de l'apprenti, dès sa conclusion, au directeur du centre de formation d'apprentis.",
 "À compter de cette entrée en vigueur, l'envoi intégral du contrat de mission n'est plus exigé sur le fondement du présent article."),
 effect(n,'coordination','contrat-unique-duree-indeterminee','Affectation temporaire dans un emploi sans terme, avec continuité de rémunération dans le champ intérimaire.',
 'Contrat de mission d’apprentissage pouvant être limité ; la source coordonne sa suspension et sa rupture avec celles du contrat d’apprentissage.',
 'Pour les nouveaux emplois, affectation au sein du contrat unique ; seule sa fin ne rompt pas l’emploi et les garanties d’intermission restent applicables.',
 'regime','Apprentis nouvellement recrutés par une entreprise de travail temporaire.',
 'Emplois conclus après entrée en vigueur ; contrats de mission antérieurs et mesures spéciales de sécurité conservés.',
 'La continuité d’emploi peut accroître les engagements salariaux ; pas de nouvel essai par mission ni de réduction de salaire de sécurité.',
 "La suspension du contrat d'apprentissage, en application des dispositions de l'article L. 6225-4, emporte la suspension du contrat de mission de l'apprenti.",
 "La garantie mensuelle de rémunération et la prise en compte des intermissions du contrat intérimaire à durée indéterminée demeurent applicables dans leur champ.")])

n='D6235-7'
impact(n,'mixed',
"La source met des envois parallèles à la charge de l'employeur. La proposition les regroupe auprès de l'opérateur ou de l'organisme de dépôt, qui doit ensuite les acheminer. Elle réduit les démarches privées mais ajoute une charge de transmission aux organismes : ce transfert administratif ne démontre pas une diminution nette du coût global.",
"Les obligations directement issues d'une convention internationale demeurent ; leur texte manque pour mesurer les dispenses réelles. Le circuit public de D. 6271-2 reste à coordonner. Aucune économie nationale, baisse de cotisation ou suppression de destinataire essentiel n'est établie.",
"Une charge de remplacement est expressément créée : l'opérateur et l'organisme de dépôt assurent le relais sans délai. Aucun registre, formulaire, nouvel agrément ou échéance chiffrée n'est ajouté ; l'information utile déjà requise reste transmise et son coût public est inconnu.",[
 effect(n,'obligation_merged','apprentissage-transfrontalier-envoi-unique','Regroupement des envois privés de conventions et de mission vers un guichet déjà destinataire.',
 'Conventions envoyées à l’opérateur, à l’organisme de formation et aux autorités étrangères ; contrat de mission envoyé au dépôt et aux autorités étrangères.',
 'Un envoi privé au guichet compétent ; relais par les organismes, sous réserve des communications directement imposées par la convention internationale.',
 'legal_duty','Employeurs d’apprentis transfrontaliers dont la partie pratique est réalisée en France.',
 'Envois restant à accomplir dès l’entrée en vigueur, anciens contrats compris ; envois déjà accomplis non refaits.',
 'Acheminement transféré aux organismes ; éventuelles communications internationales directes demeurent.',
 "les conventions prévues à l'article R. 6223-11 et D. 6271-2 sont adressées à l'opérateur de compétences unique mentionné au IV de l'article L. 6235-5 ainsi qu'à l'organisme de formation et aux autorités compétentes dans le pays frontalier.",
 "L'envoi à l'opérateur accomplit l'obligation d'envoi prévue au présent article à l'égard de ces destinataires ; aucun nouvel envoi du même document exact et à jour déjà légalement détenu par un destinataire n'est exigé de l'employeur."),
 effect(n,'obligation_added','apprentissage-transfrontalier-envoi-unique','Relais de transmission imposé à l’opérateur et à l’organisme de dépôt en remplacement des envois privés.',
 'Le présent article fait supporter les envois aux employeurs sans imposer ce relais général à l’opérateur et à l’organisme de dépôt.',
 'L’opérateur transmet sans délai les conventions, et l’organisme de dépôt transmet sans délai le document de mission aux autorités compétentes.',
 'legal_duty','Opérateur de compétences unique et organisme chargé du dépôt.',
 'Envois restant à accomplir après entrée en vigueur ; mêmes destinataires et limites des données nécessaires.',
 'Charge administrative nouvelle pour ces organismes ; absence de chiffrage du coût ou du solde net.',
 "le contrat de mission est également adressé à l'organisme en charge du dépôt ainsi qu'aux autorités compétentes dans le pays frontalier.",
 "Celui-ci les transmet sans délai à l'organisme de formation et aux autorités compétentes dans le pays frontalier.")])

n='D6235-13'
impact(n,'material_reduction',
"Deux contraintes de la source sont retirées : le minimum de six mois pour une formation effectivement aménagée et l'autorisation de troisième formation au même niveau. Le cycle ordinaire, l'évaluation des compétences, la certification et toutes les prolongations et dérogations favorables restent applicables. Aucune suppression du droit étranger n'est revendiquée.",
"La dispense du minimum concerne l'aménagement individuel, pas le cycle ordinaire de six mois à trois ans. La convention internationale peut conserver des contraintes à coordonner ; les exigences du certificateur, le plafond sous réserve de prolongations et l'accès en centre dans les trois mois restent applicables. Aucun rendement public n'est calculé.",
"Aucune charge nouvelle n'est identifiée : pas de déclaration remplaçant l'autorisation, évaluation des compétences déjà requise et réutilisable, convention de formation existante. La certification n'est pas une condition nouvellement créée ; l'élargissement éventuel du financement n'est pas chiffré.",[
 effect(n,'deadline_reduced','apprentissage-transfrontalier-duree-adaptee','Suppression du minimum de six mois pour la formation individuellement aménagée selon les compétences.',
 'Durée effective aménagée entre six mois et trois ans, avec les dérogations spécifiques de la section.',
 'Aucun minimum de six mois pour l’aménagement individuel ; durée adaptée aux compétences et à la certification, plafond de trois ans sous réserve des prolongations.',
 'other','Apprentis dont l’employeur est établi dans le pays frontalier et dont la formation est délivrée en France selon le droit français.',
 'Aménagements examinés dès entrée en vigueur, situations anciennes éligibles comprises ; aménagements valables et avantages conservés.',
 'Évaluation déjà prévue et exigences de certification maintenues ; aucune autorisation ou déclaration nouvelle.',
 "Elle ne peut pas conduire à une durée de la formation inférieure à six mois ou supérieure à trois ans.",
 "L'aménagement n'est soumis à aucune durée minimale de six mois ; sa durée est déterminée au regard des compétences ainsi évaluées et des exigences de la certification préparée."),
 effect(n,'authorization_removed','apprentissage-troisieme-formation-sans-autorisation','Suppression du visa du dernier directeur pour la troisième formation de même niveau.',
 'Après deux contrats successifs de même niveau, autorisation du directeur du dernier CFA pour une troisième formation de même niveau.',
 'Aucune autorisation de ce directeur ni déclaration équivalente ; conditions ordinaires de formation et de financement conservées.',
 'legal_duty','Apprentis transfrontaliers relevant du 8° de D. 6235-13.',
 'Admissions examinées dès entrée en vigueur, y compris après anciens contrats ; admissions déjà accordées conservées.',
 'Aucune déclaration, visa de substitution ou registre nouveau.',
 "Lorsque l'apprenti a déjà conclu deux contrats successifs de même niveau, le suivi d'une troisième formation par apprentissage du même niveau est subordonné à l'autorisation du directeur du dernier centre de formation d'apprentis qu'il a fréquenté ;",
 "le suivi d'une troisième formation par apprentissage du même niveau, après deux contrats successifs de ce niveau, n'est pas subordonné à l'autorisation du directeur du dernier centre de formation d'apprentis fréquenté. Aucune déclaration équivalente n'est exigée ;")])

n='D6274-1'
impact(n,'mixed',
"La source impose la désignation d'un médiateur tout en permettant au service RH de proximité d'assurer la médiation de rupture. La proposition dispense de cette désignation distincte si le service assure la médiation ; la tâche de médiation des différends est conservée et peut être réaffectée au service. La baisse nette de travail n'est pas démontrée.",
"Le champ reste celui des apprentis des employeurs publics de L. 6227-1. Les règles de rupture et délais ne changent pas par cette dispense d'organisation. Les désignations valables et médiations en cours subsistent, ainsi que le recours au juge ; le coût net de cette réorganisation est inconnu.",
"Le remplacement est explicite : le service existant assure la fonction de médiation s'il est choisi, y compris pour les différends d'exécution. Cette réaffectation de tâche est recensée ; aucun registre, dossier, délai d'attente ou procédure de recours nouveau n'est créé.",[
 effect(n,'obligation_removed','apprentissage-public-mediation-service-existant','Dispense de désignation d’un médiateur distinct quand le service de proximité assure la fonction.',
 'Un médiateur doit être désigné ; la médiation de rupture peut pourtant être assurée par le service RH de proximité.',
 'Pas de désignation distincte exigée si ce service assure la médiation ; la fonction et l’accès du mineur ou représentant sont maintenus.',
 'legal_duty','Employeurs publics de L. 6227-1 et apprentis ou représentants légaux concernés.',
 'Dispense dès l’entrée en vigueur, anciens contrats compris ; médiations et désignations antérieures conservent leurs effets.',
 'Fonction réaffectée au service existant si choisi, sans disparition de la tâche ni formalité de remplacement.',
 "un médiateur est désigné pour résoudre les différends entre l'employeur et l'apprenti ou son représentant légal au sujet de l'exécution ou de la rupture du contrat d'apprentissage.",
 "la désignation d'un médiateur distinct n'est pas exigée lorsque ce service assure la médiation."),
 effect(n,'coordination','apprentissage-public-mediation-service-existant','Maintien et réaffectation de la médiation au service existant lorsque la dispense est utilisée.',
 'Le médiateur désigné règle les différends d’exécution et de rupture ; le service RH peut déjà assurer la médiation de rupture.',
 'Le service RH peut assurer la fonction de médiation des différends sans médiateur distinct, avec les conditions de rupture applicables au contrat concerné.',
 'legal_duty','Services RH de proximité des employeurs publics utilisant la dispense.',
 'Après entrée en vigueur ; les délais anciens ou nouveaux ne sont pas cumulés et le régime public doit être expressément coordonné par la loi.',
 'La mission du service choisi peut s’étendre aux différends d’exécution ; coût et charge résiduels non chiffrés.',
 "La médiation prévue par l'article L. 6222-18 est assurée soit par le médiateur soit par le service de ressources humaines de proximité dont relève l'apprenti.",
 "la médiation de ces différends peut être assurée par le service de ressources humaines de proximité dont relève l'apprenti")])

n='D6275-1'
impact(n,'material_reduction',
"La proposition retire le support séparé de l'aménagement en autorisant une convention commune complète et signée. Le dépôt, les cinq jours ouvrables et les coûts de formation couverts par la convention restent inchangés. La dispense de retransmettre des pièces déjà accessibles reprend le droit existant, sans être comptée comme une seconde coupe.",
"La convention commune demeure annexée au contrat et respecte toutes les signatures légales ; la dénomination administrative ancienne appelle une coordination organique documentée. L'emploi public, les obligations de financement et les exceptions transfrontalières gardent leur champ ; aucun gain national n'est établi.",
"Aucune charge nouvelle n'est identifiée : le document commun est facultatif et reprend des accords déjà requis. Aucun formulaire, registre, attestation ou délai supplémentaire n'est institué ; l'exception favorable de taxe d'apprentissage demeure dans L. 6227-6.",[
 effect(n,'obligation_merged','apprentissage-documents-communs','Même mesure de supports communs appliquée au dépôt public, sans seconde réduction autonome de formalités privées.',
 'Contrat déposé avec convention de prise en charge et convention tripartite d’aménagement éventuelle.',
 'Une convention commune peut satisfaire les deux fonctions avec tous les éléments et signatures et annexion au contrat ; le dépôt reste dû.',
 'legal_duty','Employeurs publics de L. 6227-1 déposant un contrat d’apprentissage.',
 'Transmissions restant à accomplir dès l’entrée en vigueur, anciens contrats compris ; actes et délais en cours conservés.',
 'Aucune signature supplémentaire obligatoire : l’intégration est une option qui garde les accords déjà requis.',
 "accompagné de la convention mentionnée à l'article L. 6227-6 et, le cas échéant, de la convention tripartite mentionnée au troisième alinéa de l'article L. 6222-7-1",
 "aucun second document ni aucune signature en double n'est exigé.")])

n='D6323-9'
impact(n,'material_reduction',
"La source impose deux voies ordinaires conditionnées par l'entreprise ou les CDD récents et exclut cinq catégories de périodes de la seconde voie. La proposition fusionne ces voies en vingt-quatre mois de salariat portable, sans douze mois dans l'entreprise ni récence, et admet les cinq catégories. Les dispenses légales ne sont pas resserrées.",
"Le minimum total de vingt-quatre mois reste une condition d'accès, non un financement automatique. Congé, positionnement, décision de financement et conditions propres au fonds de prévention subsistent ; les voies spéciales plus favorables restent ouvertes. Le coût d'éligibilités nouvelles et le solde public ne sont pas établis.",
"Aucune charge nouvelle de dossier, registre, donnée ou délai n'est identifiée : même ancienneté minimale totale, avec moins de sous-conditions et réemploi des preuves disponibles. L'élargissement peut augmenter les demandes de financement, sans obligation générale nouvelle de les financer automatiquement.",[
 effect(n,'regime_merged','cpf-transition-anciennete-portable','Fusion des deux voies ordinaires en une ancienneté générale portable.',
 '24 mois de salariat dont 12 dans l’entreprise, ou 24 mois sur 5 ans dont 4 mois de CDD sur les 12 derniers mois, sous exclusions.',
 '24 mois de salariat consécutifs ou non, tous contrats et toutes périodes de carrière, sans sous-seuil dans l’entreprise ni condition de récence.',
 'regime','Salariés demandant un projet de transition professionnelle sous les conditions générales.',
 'Demandes en cours et futures dès entrée en vigueur, périodes anciennes admises ; ancienneté mesurée au départ en formation et droits favorables acquis préservés.',
 'Aucun nouveau dossier ; maintien de l’examen du projet et du financement, coût des ouvertures nouvelles non chiffré.',
 "1° Soit d'une ancienneté d'au moins vingt-quatre mois, consécutifs ou non, en qualité de salarié, dont douze mois dans l'entreprise, quelle qu'ait été la nature des contrats de travail successifs ;",
 "1° Au moins vingt-quatre mois, consécutifs ou non, en qualité de salarié, quelle qu'ait été la nature des contrats de travail successifs. Aucune durée minimale dans l'entreprise où la demande est déposée ni aucune période de référence limitant la prise en compte des emplois antérieurs n'est exigée ;"),
 effect(n,'relief_extended','cpf-transition-anciennete-portable','Admission des cinq catégories d’emploi auparavant exclues du calcul spécial.',
 'Les périodes de CAE, apprentissage, professionnalisation, cursus scolaire ou universitaire et CDD poursuivi en CDI sont exclues du calcul des quatre mois de la seconde voie.',
 'Ces cinq catégories sont explicitement comptabilisables dans le minimum général de vingt-quatre mois ; aucune ancienneté dans un CDD nouveau n’est requise.',
 'legal_duty','Salariés possédant des périodes relevant des cinq catégories du II.',
 'Demandes en cours et futures, périodes anciennes incluses ; pas d’annulation automatique d’un ancien refus définitif.',
 'Suppression de filtres d’éligibilité ; les autres règles financières et la preuve des périodes réellement salariées demeurent.',
 "II.-Ne peut être prise en compte au titre du calcul des quatre mois en contrat de travail à durée déterminée mentionnée au I l'ancienneté acquise au titre :",
 "II.-Aucune des périodes suivantes n'est exclue du calcul de l'ancienneté mentionnée au I :")])

n='R6323-9-1'
impact(n,'material_reduction',
"La source cumule pour les intermittents 220 jours ou cachets avec les seuils récents par métier, et pour l'intérim 1 600 heures dans la branche avec 600 dans l'entreprise. Le projet retire le premier seuil cumulatif et le sous-seuil d'entreprise. Les seuils professionnels récents, les 1 600 heures et l'assimilation des intermissions restent applicables.",
"L'élargissement d'accès n'est pas une garantie de financement de toute demande. L'équivalence des intermissions n'est pas inventée ; la date de départ en formation, les dispenses et la voie générale plus favorable restent ouvertes. Coût de formation et effet global sur finances et emploi non chiffrés.",
"Aucune charge nouvelle n'est identifiée : aucun justificatif ou registre supplémentaire, seuils existants restants et réemploi des données disponibles. L'ouverture accrue peut engendrer des demandes et dépenses de financement, sans nouveau prélèvement ni financement automatique institué.",[
 effect(n,'obligation_removed','cpf-transition-spectacle-seuil-cumulatif','Retrait du double seuil de 220 jours ou cachets, avec maintien de l’activité récente propre au métier.',
 '220 jours de travail ou cachets sur 2 à 5 ans, plus 130/65 jours pour technicien enregistré, 88/44 vivant ou 60/30 jours ou cachets pour artiste sur 24/12 mois.',
 'Seuls les seuils récents par métier demeurent : 130/65, 88/44 et 60/30 sur 24/12 mois ; pas de cumul supplémentaire de 220 jours ou cachets.',
 'legal_duty','Salariés intermittents du spectacle vivant ou enregistré relevant du I.',
 'Demandes en cours et futures dès entrée en vigueur, périodes antérieures admises ; droits et décisions favorables acquis préservés.',
 'Aucune condition professionnelle ou attestation supplémentaire ; décision de financement indépendante maintenue.',
 "doit justifier de deux-cent-vingt jours de travail ou cachets répartis sur les deux à cinq dernières années",
 "il n'est plus exigé qu'il justifie en outre de deux cent vingt jours de travail ou cachets répartis sur les deux à cinq dernières années :"),
 effect(n,'obligation_removed','cpf-transition-interim-anciennete-branche','Retrait de l’ancienneté minimale dans l’entreprise où la demande est déposée.',
 '1 600 heures dans la branche sur 18 mois dont 600 dans l’entreprise de travail temporaire ou le groupe où est demandé le congé.',
 '1 600 heures dans la branche sur 18 mois, toutes missions confondues, sans 600 heures propres à cette entreprise ou ce groupe ; intermissions du CDI conservées.',
 'legal_duty','Salariés des entreprises de travail temporaire relevant du II.',
 'Demandes en cours et futures dès entrée en vigueur ; périodes d’emploi antérieures et décisions favorables conservées.',
 'Aucun seuil horaire nouveau ni conversion fictive des intermissions ; pas de contribution CPF-CDD de remplacement.',
 "dont 600 heures dans l'entreprise de travail temporaire, ou le groupe d'entreprises de travail temporaire, dans lequel est déposée la demande du congé spécifique mentionné à l'article L. 6323-17-1.",
 "il n'est plus exigé que 600 de ces heures aient été accomplies dans l'entreprise ou le groupe d'entreprises de travail temporaire où est déposée la demande de congé spécifique prévu à l'article L. 6323-17-1.")])

# Compléments issus de la relecture des pouvoirs de financement et du dépôt public.
by['R6223-1']['review_notes'] += " R. 6332-26, lu intégralement lors de la relecture finale, conserve le contrôle de service fait et de qualité, les pièces complémentaires nécessaires, les contrôles sur place, le contradictoire d'au moins sept jours et les signalements en cas de manquement : le contrôle d'exécution financée n'est pas supprimé."
n='D6275-1'
p=by[n]['proposed_xml']
p=p.replace("Il joint la convention prévue à l'article L. 6227-6 et, le cas échéant, l'aménagement convenu au troisième alinéa de l'article L. 6222-7-1, sous réserve des dispenses applicables.", "Il joint, le cas échéant, la convention tripartite prévue au troisième alinéa de l'article L. 6222-7-1, sous réserve des dispenses applicables.")
p=p.replace("À compter de l'entrée en vigueur de la loi portant réforme du contrat de travail, les conventions ou informations exactes et à jour", "À compter de l'entrée en vigueur de la loi portant réforme du contrat de travail, la convention de prise en charge prévue à l'article L. 6227-6 n'est plus jointe au dépôt sur le fondement du présent article. Sa conclusion, la prise en charge des coûts et l'exception applicable aux personnes redevables de la taxe d'apprentissage demeurent régies par cet article ; les contrôles légalement autonomes sont conservés. Les conventions ou informations exactes et à jour")
by[n]['proposed_xml']=p
by[n]['removed_provisions'].append("Suppression de l'envoi systématique au service de dépôt de la convention financière conclue entre l'employeur public et le centre, sans supprimer sa conclusion ni la prise en charge de la formation.")
by[n]['reason']="Au-delà du précédent brouillon, la seconde passe retire du dépôt public la convention financière de L. 6227-6. D. 6275-2 contrôle le contrat, l'âge, la formation, le salaire et la certification ; il ne décide pas le financement, qui reste dû par l'employeur public selon sa convention avec le centre. La transmission systématique de cette convention au service de dépôt n'a donc pas de fonction essentielle démontrée. Le contrat, la convention tripartite éventuelle et les contrôles autonomes demeurent ; la réunion facultative de documents garde ses signatures et annexion légales."
by[n]['review_notes'] += " Coupe supplémentaire après lecture entière de D. 6275-2 : ses cinq contrôles et son refus motivé du dépôt restent inchangés ; le financement par convention de L. 6227-6 n'est pas une décision de ce service. La convention demeure entre employeur et CFA, et peut rester demandable sur un fondement de contrôle autonome ; aucune demande ou attestation de remplacement n'est créée ici. D. 6275-4, lu, conserve l'avenant aux modifications essentielles du contrat, sans imposer par ce seul renvoi le nouvel envoi systématique de la convention financière supprimé."
im=by[n]['substantive_impact']
im['assessment']="La coupe supplémentaire démontrée est la suppression de l'envoi systématique de la convention financière au service de dépôt public. La convention et le financement de la formation demeurent entre l'employeur et le CFA. Le document commun conserve ses fonctions sans supports répétés ; le réemploi CRPA et la simple réunion de conventions ne sont pas comptés comme une nouvelle suppression indépendante."
im['scope_limitations']="Le contrat et la convention tripartite éventuelle restent déposés sous cinq jours ouvrables. Les contrôles de D. 6275-2, les contrôles financiers autonomes et la prise en charge de L. 6227-6 demeurent ; l'ancienne dénomination administrative appelle coordination organique. Aucun effet budgétaire national n'est établi."
im['new_burdens_review']="Aucune charge nouvelle n'est identifiée : aucun relevé ni attestation ne remplace la convention retirée du dépôt. La convention continue d'être conclue pour financer la formation ; sa réunion à un document commun reste facultative et conserve les signatures déjà requises, sans nouveau délai ou registre."
im['effects'][0]['kind']='coordination'
im['effects'][0]['description']="Coordination du support commun avec les signatures et l'annexion légales ; aucune seconde suppression autonome comptée."
im['effects'][0]['before']="Convention de prise en charge conclue avec le centre et convention tripartite éventuelle : leurs fonctions et accords de fond restent nécessaires."
im['effects'][0]['after']="Réunion facultative des fonctions dans un document commun signé et annexé ; seul le contrat et l'aménagement requis sont déposés, sans dépôt financier systématique."
im['effects'].append(effect(n,'obligation_removed','apprentissage-public-depot-sans-convention-financiere',
"Suppression du dépôt systématique de la convention financière auprès du service de dépôt du contrat.",
"L'employeur public transmet le contrat accompagné de la convention de prise en charge de L. 6227-6 et de la convention tripartite éventuelle.",
"La convention financière n'est plus jointe au dépôt ; sa conclusion et le financement restent obligatoires dans leur champ, avec l'exception favorable de taxe d'apprentissage.",
'legal_duty',"Employeurs publics relevant de L. 6227-1 et services de dépôt du contrat d'apprentissage.",
"Transmissions restant à accomplir dès entrée en vigueur, anciens contrats compris ; dépôts et conventions valables non refaits.",
"Aucun formulaire ou justificatif de remplacement ; contrôles contractuels et financiers autonomes conservés.",
"accompagné de la convention mentionnée à l'article L. 6227-6",
"la convention de prise en charge prévue à l'article L. 6227-6 n'est plus jointe au dépôt sur le fondement du présent article."))

# Analyses limitées exactement aux cibles requises, avec les empreintes de la vue fournie.
common_context={
'R6222-23-1':(
"La reprise d'apprentissage et ses minima pédagogiques ne constituent pas une notification de rupture ; la dispense de convention ne dispense d'aucune procédure patronale ni autorisation de salarié protégé.",
"La signature du nouvel engagement de reprise désigne désormais une phase pédagogique d'emploi sans terme ; aucun minimum ou maximum de formation ne rétablit un CDD, tandis que les anciens contrats gardent leurs droits.",
"La réduction de durée de formation et sa dispense ne déterminent ni l'ancienneté générale ni l'indemnité de rupture ; la garantie de poursuite de formation de six mois ne se déduit pas d'une indemnité ordinaire."),
'D6222-28-1':(
"L'assimilation de cycle pour le salaire n'est pas une durée de préavis ; elle ne reporte pas le départ du préavis ni n'en modifie la notification lorsque la rupture d'un contrat unique intervient pendant la formation.",
"L'assimilation doit suivre la période pédagogique des nouveaux emplois indéfinis et rester applicable aux anciens contrats réduits ; le cycle réputé accompli pour le salaire ne crée pas un terme d'emploi.",
"La durée réputée accomplie vaut exclusivement pour la rémunération d'apprentissage. Elle ne permet pas de franchir fictivement le seuil d'un an d'ancienneté effective ni de calculer l'indemnité sur une ancienneté de formation reconstituée."),
'D6222-28-2':(
"La prolongation pédagogique n'allonge pas le préavis et ne crée pas une nouvelle notification. Le maintien du minimum de dernière année s'applique pendant cette prolongation, sans promettre une rupture complète en quinze jours.",
"La durée supérieure au cycle concerne la phase pédagogique du contrat unique. Le minimum salarial ne devient pas un droit de poursuivre un contrat à terme nouveau ni une dérogation à l'emploi indéfini.",
"La prolongation ne transforme pas le salaire minimum pédagogique en indemnité ordinaire. Seule l'ancienneté réelle de l'emploi entre dans le seuil et le barème ; les salaires de la prolongation effectivement exécutée restent dus."),
'R6223-1':(
"L'abrogation du fondement spécial de justificatifs ne dispense pas de notifier une rupture ni de ses procédures ; les pièces obligatoires de rupture restent contrôlables dans les pouvoirs autonomes de l'inspection.",
"L'abrogation vise les demandes futures, même relatives à un ancien contrat, sans supprimer l'écrit d'apprentissage ni permettre un nouvel emploi à terme. Les règles de formation et le contrat unique conservent leurs fondements autonomes.",
"Aucun justificatif salarial ou de rupture légalement obligatoire n'est rendu inexigible dans les pouvoirs autonomes. Retirer le devoir spécial de preuve ne modifie ni l'ancienneté ni la créance ordinaire ou spéciale de rupture."),
'D6224-1':(
"Le délai de dépôt reste cinq jours ouvrables après le début du contrat : il ne s'agit ni d'un préavis de quinze jours calendaires ni de son point de départ. La réunion de documents ne vaut pas notification d'une rupture.",
"Le dépôt d'un contrat unique et la mise à jour de sa période pédagogique ne constituent pas un nouveau CDD ; aucune durée de convention de financement ne termine l'emploi. Les anciens contrats et financements valables sont préservés.",
"Le dépôt, son document commun et les périodes de prise en charge ne remettent pas l'ancienneté à zéro. Ils ne conditionnent pas l'indemnité ordinaire et ne neutralisent pas les salaires, congés ou créances déjà acquis."),
'R6226-3':(
"Le délai de quinze jours de décision de sécurité de L. 6225-5 est administratif, distinct du préavis individuel et de sa notification. Les salariés protégés et les procédures collectives ne sont pas dispensés par la fin d'affectation.",
"La nouvelle lettre de mission s'insère dans un emploi indéfini ; la mission temporaire ne termine pas ce contrat. Les anciens contrats de mission gardent leur régime sans nouveau renouvellement à durée déterminée après la réforme.",
"Les sommes dues pour refus de reprise après risque sérieux en L. 6225-5 sont spéciales : le zéro ordinaire avant un an et le plafond de six mois ne les suppriment pas. L'affectation n'interrompt pas l'ancienneté de l'emploi unique."),
'D6235-7':(
"Les envois de conventions et d'affectation sont des transmissions pédagogiques, pas la notification d'une rupture. Leur regroupement ne réduit aucune autorisation spéciale ni ne fait courir un préavis par la réception de l'OPCO.",
"La pratique en France peut relever d'un nouvel emploi français sans terme, avec affectation limitée. Les documents de mission existants alimentent le circuit unique, sans instaurer un CDD ni modifier le régime propre d'un employeur public.",
"Le circuit d'envoi ne fixe ni ancienneté ni indemnité ; sa durée d'accueil n'est pas une durée d'emploi. Les rémunérations, frais et droits acquis définis dans les conventions demeurent indépendants du barème ordinaire de rupture."),
'D6235-13':(
"L'employeur étant établi dans le pays frontalier, l'organisation de formation française n'impose pas, à elle seule, le préavis privé français. La loi de l'emploi et la convention bilatérale doivent déterminer toute notification de rupture.",
"La suppression du minimum de durée aménagée et de l'autorisation de troisième formation concerne la formation. Le droit étranger d'emploi n'est pas transformé en contrat unique par ce règlement ; si l'emploi relève de la loi française réformée, aucun terme pédagogique ne le rompt.",
"Les durées de cycle, de formation adaptée et de réorientation ne sont pas l'ancienneté d'emploi d'un salarié étranger. Le barème français ne s'applique pas automatiquement ; aucun avantage de formation n'est absorbé dans une indemnité ordinaire."),
'D6274-1':(
"La dispense de médiateur distinct est organisationnelle. Elle ne soumet pas implicitement l'apprenti public au préavis patronal du nouveau contrat privé : le régime applicable exige une coordination législative expresse, et les procédures restent distinctes.",
"Le texte vise expressément les employeurs publics de L. 6227-1 ; l'apprentissage public a ses règles propres. Le libellé large de la proposition L. 1221-2 doit être coordonné avec ce champ sans convertir les agents publics ni tous les anciens contrats.",
"La médiation ne fixe aucune indemnité. Le régime privé à un an et sa composante d'ancienneté antérieure ne sont pas appliqués mécaniquement aux apprentis publics ; l'accès au juge et les indemnités spéciales restent indépendants."),
'D6275-1':(
"Le dépôt public sous cinq jours ouvrables ne constitue pas une notification de rupture ni le préavis privé de quinze jours. La dispense de documents répétés n'autorise aucune anticipation des délais de protection applicables au contrat public concerné.",
"La convention commune simplifie un dépôt d'apprentissage public, sans appliquer implicitement un nouveau régime de durée. Les anciens contrats gardent leur champ ; l'extension du contrat unique aux emplois publics concernés doit résulter de la loi.",
"Le document de prise en charge et l'aménagement pédagogique ne modifient pas l'ancienneté et n'ouvrent ni ne suppriment une indemnité. Le champ public doit être raccordé expressément avant toute application du barème ordinaire privé."),
'D6323-9':(
"L'ouverture du projet de transition dépend d'une ancienneté de formation appréciée au départ ; elle ne change ni le préavis, ni la notification écrite de rupture, ni les autorisations et procédures collectives éventuelles.",
"La fusion des voies retire toute dépendance à quatre mois de CDD, y compris pour les nouveaux contrats uniques. Les périodes d'anciens CDD sont conservées dans le calcul sans autoriser de nouveau contrat à terme pour obtenir le droit.",
"Les vingt-quatre mois de salariat sur une carrière, tous employeurs confondus, ne valent pas un an ininterrompu chez l'employeur qui rompt. Ils ne déclenchent pas l'indemnité ordinaire et ne remplacent pas ses règles d'ancienneté propre."),
'R6323-9-1':(
"Les périodes de travail, cachets et intermissions servent l'accès au congé de formation, pas la notification d'une rupture. Le projet ne modifie ni préavis privé, ni procédure collective, ni autorisation liée à une protection spéciale.",
"Les voies d'accès des intermittents et intérimaires demeurent utilisables dans l'emploi unique. La fin d'une représentation ou d'une mission n'autorise pas un nouveau CDD d'usage ni ne termine automatiquement l'emploi indéfini.",
"Les 1 600 heures de branche et les seuils de jours ou cachets ne sont pas l'ancienneté de rupture chez un employeur. Les intermissions comptabilisables pour la formation ne créent aucune indemnité de rupture fictive ou remise à zéro d'ancienneté.")}
extra={
'R6222-23-1':{
'L6222-7-1':"Le renvoi au premier alinéa vise le minimum pédagogique de six mois, dont la dérogation demeure ; le troisième alinéa porte la convention tripartite dont cet article dispense déjà la signature. Le projet cible conserve six mois à trois ans pour la période et les anciens contrats : ni ces bornes ni la convention dispensée ne doivent rétablir un terme d'emploi.",
'L6222-18-2':"Le renvoi vise la reprise après rupture, avec poursuite théorique de six mois, aide à retrouver un employeur et statut de stagiaire. Ces garanties sont conservées pour les futures reprises éligibles et les anciens droits, dans les exceptions transfrontalières de L. 6235-4 ; elles ne constituent pas une durée minimale d'emploi ni une indemnité ordinaire."},
'D6222-28-1':{
'L6222-7-1':"Le troisième alinéa vise l'écart au cycle selon le niveau initial ou les compétences acquises, non l'ancienneté de rupture. La cible proposée réserve la durée à la période d'apprentissage et conserve la convention tripartite ; la garantie salariale de cycle réputé accompli demeure pour les réductions admises et les contrats antérieurs.",
'R6222-23-1':"La cible officielle et sa proposition dispensent de convention pour la reprise après rupture et permettent de déroger aux minima. D. 6222-28-1 lui attache l'assimilation salariale du cycle : cette garantie n'est pas perdue si la phase reprise est brève, et la dispense n'est pas remplacée par une attestation. La proposition du présent lot reste cohérente avec la vue fournie."},
'D6222-28-2':{
'L6222-7-1':"Le troisième alinéa concerne l'allongement pédagogique selon les compétences, pas le prolongement d'un CDD nouveau. Le salaire de dernière année est maintenu pour cette phase ; la cible conserve six mois à trois ans sous les exceptions de prolongation et les règles des anciens contrats, sans nouvelle notification de rupture à la fin de formation."},
'R6223-1':{
'L6222-7-1':"L'article abrogé désignait la convention tripartite lorsqu'un aménagement était requis. Son abrogation ne supprime ni la convention ni ses signatures et annexion conservées par la cible proposée ; les écrits restent accessibles dans les contrôles autonomes. La durée pédagogique du contrat unique n'est pas une durée maximale d'emploi."},
'D6224-1':{
'L6222-7-1':"La cible source et sa proposition exigent au troisième alinéa une convention tripartite signée et annexée. Le document commun de dépôt satisfait ces mêmes accords et cette annexion ; il ne se contente pas d'une dispense réglementaire incompatible. Les bornes concernent la pédagogie du nouveau contrat, et les anciens accords valables restent acquis.",
'R6222-6':"La proposition de cette cible autorise l'intégration de l'aménagement à la convention de formation, les signatures déjà acceptées et les dispenses. D. 6224-1 en reprend la fonction avec une précision nécessaire : le document commun vaut convention tripartite et reste annexé selon L. 6222-7-1. La cible réglementaire ne supprime pas, à elle seule, une exigence législative ni les évaluations nécessaires."},
'R6226-3':{
'L1251-16':"Le 1° source exige la reproduction des mentions de mise à disposition ; la proposition permet l'information déjà remise et institue une lettre d'affectation dans le contrat unique, sans nouvel essai. R. 6226-3 ajoute les six informations pédagogiques mais dispense leur recopie déjà communiquée sur support conservable. La dispense ne prive pas l'apprenti de sa rémunération, de la garantie de rapatriement ou des droits des contrats antérieurs."},
'D6235-13':{
'L6222-7-1':"Le renvoi du 2° porte sur les compétences pouvant justifier l'aménagement, non sur l'application générale de la durée d'un contrat français à l'employeur étranger. L. 6235-4 II 2° exclut le titre II sauf trois articles, dont L. 6222-18-2 : le minimum aménagé de six mois est ici retiré sur son fondement réglementaire propre, sans prétendre abroger une condition de droit étranger.",
'L6222-18-2':"Cette cible fait partie des exceptions expressément applicables quand la pratique a lieu dans le pays frontalier selon L. 6235-4 II 2°. Le 9° conserve la dérogation favorable pour une reprise de formation après rupture, avec le champ légal de poursuite théorique pendant six mois et de statut de stagiaire. Ce délai ne devient pas le terme de l'emploi étranger ou du contrat unique français."},
'D6274-1':{
'L6222-18':"Le renvoi concerne la médiation de rupture de l'apprenti, dont la protection du mineur et la saisine du service public compétent. La proposition distingue nouveaux contrats uniques et contrats antérieurs ; la dispense de désignation distincte ne rend pas facultative une saisine encore imposée à un ancien contrat ni ne supprime les signatures du représentant légal. Le champ du nouvel apprentissage public reste à coordonner expressément par la loi.",
'D6222-21-1':"La source prévoit cinq jours calendaires au moins après saisine, puis sept après information de l'employeur, avec transition historique au 1er janvier 2019. La proposition prévoit quinze jours à compter du lendemain de réception de l'écrit pour les contrats uniques et retire la saisine obligatoire du majeur. D. 6274-1 réserve le régime réellement applicable au contrat public ; il ne cumule pas cinq, sept et quinze jours ni ne transforme cette médiation en préavis patronal."},
'D6275-1':{
'L6222-7-1':"La convention du troisième alinéa conserve dans la cible les trois accords requis et son annexion au contrat. Le document de prise en charge peut avoir les deux fonctions s'il satisfait ces mêmes exigences, sans nouvelle signature en double. La convention financière de L. 6227-6 n'est plus déposée systématiquement, mais cette dispense ne supprime pas la convention tripartite requise ni son annexion. Ce support commun n'applique pas implicitement un terme de formation ou le régime du contrat unique privé à l'emploi public."},
'R6323-9-1':{
'L1251-2':"La définition vise l'entreprise qui recrute et rémunère les salariés pour les mettre temporairement à disposition. La proposition lui impose l'emploi nouveau sans terme et réserve les garanties mensuelles et d'intermission ; le seuil CPF de branche et les intermissions restent compatibles. La suppression des 600 heures chez un seul employeur ne supprime pas ces garanties et ne rétablit pas de contrat de mission à terme."}}

for r in rows:
 n=r['number']; contexts=common_context[n]
 common={
 'L1234-1':"La cible proposée, distincte du droit officiel, fixe le préavis patronal des nouveaux contrats à quinze jours calendaires sans seuil d'ancienneté, y compris paiement en cas de faute grave ; les anciens contrats gardent leurs durées. "+contexts[0]+" Le point de départ et la preuve de notification restent ceux de la coordination de L. 1234-3, dont la proposition n'est pas fournie comme cible ici.",
 'L1221-2':"La cible proposée interdit tout nouveau terme automatique, y compris renouvellement ou reconduction après la réforme, en préservant les contrats antérieurs et leurs droits. "+contexts[1],
 'L1234-9':"La cible proposée réserve l'indemnité ordinaire à la rupture patronale hors faute grave : zéro avant un an à la fin effective, préavis inclus ; ensuite 0,20 mois par année totale, fractions en mois complets et plafond légal de six mois. Les anciens contrats gardent leur seuil de huit mois et la part acquise selon le régime antérieur, sans double compte. "+contexts[2]
 }
 key=r['code_id']+'|'+r['source_id']
 checks=[]
 for tk in refs['requirements'][key]:
  t=refs['targets'][tk]; tn=t['number']
  assessment=common.get(tn) or extra[n][tn]
  assert len(assessment)>=80,(n,tn)
  checks.append(dict(target_key=tk,view_sha256=t['view_sha256'],assessment=assessment))
 r['reference_checks']=checks

# Relectures de traçabilité et de structure ; aucun contrôle n'est une validation juridique.
allowed={'p','br','table','thead','tbody','tfoot','tr','th','td','b','strong','i','em','u','sup','sub','ul','ol','li','div','span','blockquote'}
from html.parser import HTMLParser
class XMLCheck(HTMLParser):
 def handle_starttag(self,tag,attrs):
  assert tag in allowed,tag
  assert all(k in {'rowspan','colspan'} and v and v.isdecimal() for k,v in attrs),(tag,attrs)
for s,r in zip(src,rows):
 assert all(s[k]==r[k] for k in ['code_id','source_id','source_sha256','number'])
 assert r['status']=='rewrite_draft'
 assert r['proposed_xml'] and r['proposed_xml']!='texte inchangé'
 XMLCheck().feed(r['proposed_xml'])
 if s['benefit_check_required']: assert len(r.get('benefit_review',''))>=100
 im=r['substantive_impact']
 for k in ['assessment','scope_limitations','new_burdens_review']: assert len(im[k])>=40
 for e in im['effects']:
  assert e['source_quote'] in plain(s['source_xml'])
  assert e['proposed_quote'] in plain(r['proposed_xml'])
  assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',e['measure_id']) and 6<=len(e['measure_id'])<=96
 if r.get('change_type')=='normative_reduction': assert all(len(v)>=30 for v in r['removed_provisions'])
 if r.get('change_type')=='full_repeal':
  assert plain(r['proposed_xml']).startswith('Le présent article est abrogé')
  assert len(r['repeal_scope'])>=30
 assert [c['target_key'] for c in r['reference_checks']]==refs['requirements'][r['code_id']+'|'+r['source_id']]
assert len(rows)==12
Path('answer.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
Path('answer.partial.json').unlink(missing_ok=True)
print(json.dumps({'articles':len(rows),'reference_checks':sum(len(r['reference_checks']) for r in rows),'effects':sum(len(r['substantive_impact']['effects']) for r in rows),'output_bytes':Path('answer.json').stat().st_size},ensure_ascii=False))
