import json, re, html
from html.parser import HTMLParser
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
by_num = {x['number']:x for x in sources}
answer = {}

class Text(HTMLParser):
    def __init__(self): super().__init__(); self.parts=[]
    def handle_data(self,s): self.parts.append(s)
    def handle_starttag(self,t,a):
        if t in ['p','br','div','li','tr']: self.parts.append(' ')
    def handle_endtag(self,t):
        if t in ['p','div','li','tr']: self.parts.append(' ')
def plain(s):
    p=Text();p.feed(s or '');return re.sub(r'\s+',' ',''.join(p.parts)).strip()
def paras(s): return re.findall(r'<p(?:\s[^>]*)?>.*?</p>', s, re.S)
def ptext(s): return plain(s)
def replace_once(s, old, new):
    assert s.count(old)==1, (old,s.count(old))
    return s.replace(old,new,1)
def add_end(s, text): return s.rstrip()+'\n<p>'+text+'</p>\n'
def effect(kind, mid, description, before, after, unit, pop, transition, burdens, sq, pq):
    return dict(kind=kind,measure_id=mid,description=description,before=before,after=after,unit=unit,affected_population=pop,conditions_and_transition=transition,replacement_or_new_burdens=burdens,source_quote=sq,proposed_quote=pq)
def record(n, proposed, reason, review, impact_class, assessment, scope, new, effects=None, removed=None, repeal=None, benefit=None):
    a=by_num[n]
    r={k:a[k] for k in ['code_id','source_id','source_sha256','number']}
    r.update(proposed_xml=proposed,reason=reason,review_notes=review,status='retained_unchanged' if proposed is None else 'rewrite_draft')
    if proposed is None: r['classification']='retained_necessary'
    if removed:
        r.update(change_type='normative_reduction',reform_policy_id='editorial_direction_2026_10_19',removed_provisions=removed)
    if repeal:
        r.update(change_type='full_repeal',repeal_policy_id='editorial_direction_2026_10_19',repeal_scope=repeal)
    if benefit: r['benefit_review']=benefit
    r['substantive_impact']=dict(version=1,classification=impact_class,assessment=assessment,scope_limitations=scope,new_burdens_review=new,effects=effects or [])
    r['reference_checks']=[]
    answer[n]=r

record('L480-1',None,
"Maintien intégral nécessaire après examen des charges : la constatation par des agents habilités et assermentés, le procès-verbal lorsqu'une infraction est connue et sa transmission au parquet fondent la preuve contradictoire et le contrôle du juge. La force probante reste réfragable. Les règles spéciales protègent le patrimoine et l'archéologie ; les actions des associations, communes et EPCI protègent des intérêts lésés. Aucune déclaration du constructeur, taxe ou autorisation supplémentaire n'est instituée ici ; retirer le constat ou la saisine du parquet affaiblirait ces protections sans supprimer une formalité privée redondante.",
"Six alinéas examinés entièrement, notes sources vides. Renvois L480-4 et L610-1 lus avec les sources entières ; les obligations réprimées sont celles qui restent applicables après réforme, sans renaissance d'une charge abrogée. L480-4 conserve son deuxième alinéa, visé par L480-3. Les habilitations spéciales et L522-1 à L522-4 patrimoine, ainsi que l'agrément environnemental L141-1, ont une fonction autonome ; leurs textes extérieurs ne sont pas joints au corpus fourni et ne sont pas présentés comme réécrits. Pas de rétablissement de quotas ou de carence SRU par les pouvoirs de constatation.",
'retained_necessary',
"Le texte officiel entier est maintenu : aucun prélèvement, dépôt ou délai n'est supprimé. Les charges publiques de constatation sont nécessaires à la preuve, et les droits de partie civile sont conservés.",
"Le maintien porte sur les six alinéas de cette source ; les compétences patrimoniales et environnementales extérieures ne font pas l'objet d'une réécriture dans ce lot.",
"Aucune charge nouvelle n'est identifiée : absence de nouveau corps, de nouvelle donnée ou de nouveau circuit ; les garanties et obligations existantes restent identiques.")

record('L480-2',None,
"Maintien intégral nécessaire : l'interruption de travaux irréguliers évite leur poursuite pendant le contrôle et préserve l'utilité des décisions judiciaires. L'audition ou la convocation sous quarante-huit heures, la motivation, la mainlevée, la fin des mesures en cas de non-lieu, relaxe ou absence de poursuites et le contrôle du juge sont indissociables de ce pouvoir. Les transmissions au parquet concernent des actes distincts, pas une double déclaration imposée au constructeur. La saisie, les scellés et la substitution après carence n'ajoutent pas une procédure d'autorisation de construire à supprimer.",
"Onze alinéas, y compris les renvois positionnels aux alinéas 5, 6, 9 et 10, lus et maintenus dans l'ordre. Quarante-huit heures, deux délais de vingt-quatre heures et arrêtés sans délai inchangés. L480-1 et L480-4 lus ; la réduction de certaines sanctions ne retire pas les infractions ni l'interruption. Les prescriptions archéologiques et le code de procédure pénale restent autonomes. La source est signalée ABROGE_DIFF avec fin de validité au 1er janvier 2029, sans note explicative jointe : ce maintien ne décide ni un report de cette échéance ni une date pour la réforme proposée ; la coordination avec le texte différé reste à vérifier.",
'retained_necessary',
"Aucune simplification matérielle revendiquée : l'ensemble du dispositif de suspension et de ses garanties reste nécessaire pour empêcher la poursuite de travaux illégaux et assurer un recours effectif.",
"La proportionnalité des mesures demeure contrôlable ; l'abrogation différée indiquée pour 2029 et les procédures extérieures ne sont pas réécrites par ce maintien.",
"Aucune charge nouvelle n'est identifiée : le texte n'est pas modifié, aucun justificatif, délai supplémentaire ou procédure de remplacement n'est créé.")

record('L480-3',None,
"Maintien intégral nécessaire de la sanction du refus d'interrompre les travaux : elle assure l'effectivité d'un ordre judiciaire ou administratif déjà pris et des décisions de suspension du juge administratif. Elle ne sanctionne pas un simple défaut de justificatif et ne constitue ni une taxe ni une cotisation accessoire. Supprimer cette incrimination autonome permettrait de neutraliser la protection assurée par l'arrêt des travaux.",
"Les deux alinéas et les peines de 75 000 € et trois mois ont été examinés. Le deuxième alinéa de L480-4 est intégralement conservé dans la proposition de ce lot : le renvoi continue d'identifier les responsables, sans viser un barème de rupture de contrat de travail. L480-2 reste entier ; aucune assimilation d'une sanction pénale à une recette fiscale supprimée.",
'retained_necessary',
"Aucune réduction n'est déclarée : les sanctions visent la continuation de travaux malgré un ordre d'interruption ou une suspension juridictionnelle, garantie essentielle de l'autorité des décisions.",
"La source ne fixe aucune nouvelle formalité de permis ; les procédures et garanties pénales extérieures restent à leur champ propre, sans chiffrage national.",
"Aucune charge nouvelle n'est identifiée : les personnes visées, comportements incriminés et peines sont maintenus sans élargissement.")

# Suppression du minimum d'amende, maintien des plafonds et de tous les cas spéciaux.
s=by_num['L480-4']['source_xml']
q=replace_once(s,"une amende comprise entre 1 200 euros et un montant qui ne peut excéder", "une amende dont le montant ne peut excéder")
q=replace_once(q,"au sens de l'article L. 430-2", "du fait des travaux de démolition")
q=add_end(q,"La suppression du montant minimal de l'amende prévue au premier alinéa s'applique à compter de l'entrée en vigueur de la loi, y compris aux infractions commises antérieurement qui n'ont pas donné lieu à une condamnation passée en force de chose jugée. Elle ne remet pas en cause les condamnations devenues définitives avant cette entrée en vigueur.")
record('L480-4',q,
"Réforme de fond : suppression du minimum d'amende de 1 200 euros, pour permettre une sanction individualisée sans plancher automatique, tout en conservant les plafonds de 6 000 euros par mètre carré et 300 000 euros et les six mois d'emprisonnement en récidive. Les responsables, les trois cas complémentaires, la plaque commémorative et l'action des associations ou fondations demeurent. L'exclusion favorable des infractions d'affichage reste entière. Coordination nécessaire : retrait du renvoi obsolète à L430-2, absent du corpus actuel, avec maintien des surfaces rendues inutilisables par démolition dans la règle de plafond ; aucun taux nouveau ni nouvelle déclaration. Application de la suppression du plancher aux condamnations non définitives pour faits anciens.",
"Neuf alinéas sources relus, plus l'alinéa transitoire ajouté en fin ; deuxième alinéa inchangé pour L480-3. L421-1 à L421-5-3, L451-3 et L121-22-5 lus avec leurs notes. Les dispenses de formalité ne deviennent pas des obligations par le seul renvoi pénal ; la durée d'une installation temporaire ou d'un bail n'est pas celle d'un emploi. R*421-27 et R*421-28, lus en entier, emploient déjà les notions de démolition et de construction rendue inutilisable ; aucun renvoi nouveau à ces règlements n'est créé. La version historique de L430-2 n'est pas fournie : la concordance historique complète du calcul des surfaces reste à contrôler ; aucune extension d'assiette punitive n'est revendiquée. Les articles 2-4 procédure pénale et L522 patrimoine ne sont pas réécrits. Source ABROGE_DIFF jusqu'au 1er janvier 2029 : la proposition ne reporte pas cette échéance documentaire. Le projet joint de L121-22-5 conserve encore l'envoi personnel du récépissé, alors que la coordination actuelle demande son retrait après six mois ; cette discordance doit être corrigée dans cet autre article et ne modifie pas les obligations de sécurité visées au 3.",
'material_reduction',
"Par rapport à la source officielle entière, seul le plancher obligatoire de 1 200 euros est retiré du barème pénal. Les plafonds et les protections restent, et la coordination du renvoi ancien ne compte pas comme une seconde baisse.",
"Aucune baisse uniforme du montant des condamnations ni de recette fiscale n'est démontrée : le juge conserve ses plafonds. Le champ historique de L430-2 et le calendrier de l'abrogation différée exigent une coordination documentaire.",
"Aucune charge nouvelle n'est identifiée : le minimum est supprimé sans autre amende, formalité, donnée ou taux de remplacement ; la précision sur la démolition n'étend pas les travaux incriminés.",
[effect('obligation_removed','urbanisme-amende-fin-plancher',
"Retrait du minimum obligatoire de l'amende pénale générale d'urbanisme ; ce n'est pas une suppression de taxe.",
"Pour les personnes responsables de travaux irréguliers, amende d'au moins 1 200 euros ; plafond de 6 000 euros/m² de surface construite, démolie ou rendue inutilisable, ou 300 000 euros dans les autres cas.",
"Aucun minimum spécial de 1 200 euros ; mêmes personnes, surfaces et plafonds de 6 000 euros/m² ou 300 000 euros ; récidive et autres obligations maintenues.",
'euro',"Utilisateurs du sol, bénéficiaires, architectes, entrepreneurs et autres responsables des travaux visés.",
"Entrée en vigueur de la loi ; bénéfice également aux faits anciens sans condamnation passée en force de chose jugée, sans réouverture des condamnations définitives.",
"Aucune peine ou obligation de remplacement ; les contrôles, la régularisation et les plafonds existants demeurent.",
plain(paras(s)[0]).split(' En cas de récidive,')[0],plain(paras(q)[0]).split(' En cas de récidive,')[0])],
removed=["Le minimum obligatoire de 1 200 euros applicable à l'amende générale d'urbanisme du premier alinéa est supprimé."])

record('L480-4-1',None,
"Maintien intégral nécessaire : la sanction de la vente ou de la location de lots sans le titre ou les prescriptions requis protège les acquéreurs et locataires contre une opération irrégulière. Le tribunal peut privilégier une mise en conformité avec délai plutôt qu'une remise en cause immédiate, et l'exécution d'office n'intervient qu'après inexécution du jugement. Aucun dossier supplémentaire, taxe ni agrément distinct n'est créé ici. Le caractère facultatif des mesures permet une réponse proportionnée ; la protection des tiers ne justifie pas une abrogation globale.",
"Trois alinéas examinés, amende de 15 000 euros maintenue. L442-3 lu : il conserve la déclaration des lotissements non soumis à permis, sans généraliser un régime de permis. L480-7 et L480-8 sont présents dans ce lot ; le renvoi au premier bénéficiera de la suppression proposée des relèvements d'astreinte, sans nouvelle diminution à comptabiliser ici. L'exécution d'office reste subordonnée au délai fixé par le jugement ; aucun remplacement par une déclaration équivalente n'est créé.",
'retained_necessary',
"Le texte entier protège la régularité des ventes et locations de lots et permet leur régularisation judiciaire. Il n'est pas compté comme réécrit ou simplifié.",
"La proportionnalité des sanctions demeure une appréciation judiciaire ; les autres conditions de commercialisation des lots restent à leur champ propre.",
"Aucune charge nouvelle n'est identifiée : maintien du texte entier, sans nouvelle pièce ni nouvelle condition de mise en conformité.")

s=by_num['L480-4-2']['source_xml']
q=replace_once(s,"L. 480-12, L. 510-2 et L. 610-1", "L. 480-12 et L. 610-1")
record('L480-4-2',q,
"Coordination nécessaire avec l'abrogation de L510-2 : retrait de cette seule référence dans la liste applicable aux personnes morales, sans supprimer les autres infractions, le régime de responsabilité de l'article 121-2 du code pénal, l'amende ni les peines complémentaires énumérées. L510-2 ne définit pas à lui seul un délit autonome mais des mesures obligatoires de remise en état et d'expulsion ; son renvoi serait désormais orphelin. Il ne s'agit pas d'une seconde suppression de sanction distincte de celle portée par L510-2.",
"Cinq alinéas lus et conservés dans leur ordre ; 1°, 2° et limitation de l'interdiction d'activité inchangés. L480-3, L480-4, L480-4-1, L480-12 et L610-1 ont été lus. L510-1 conserve, dans le corpus et la coordination antérieure, l'agrément et son renvoi pénal à L480-4 : l'abolition de cet agrément ou de la responsabilité pénale de ses auteurs n'est pas déduite du retrait de L510-2. Les textes 121-2, 131-38 et 131-39 du code pénal ne sont pas joints et restent à vérifier hors des cinq codes ; aucune nouvelle peine ni disposition transitoire punitive n'est créée par cette suppression de renvoi.",
'coordination_only',
"Seul le renvoi au dispositif L510-2 abrogé est retiré. Aucun nouveau montant de sanction, aucune nouvelle infraction et aucune réduction supplémentaire de prélèvement ne sont revendiqués.",
"La coordination ne résout pas les règles pénales extérieures ; les sanctions encore applicables sur le fondement de L510-1 conservent leur champ propre.",
"Aucune charge nouvelle n'est identifiée : la liste est raccourcie sans élargir l'imputation aux personnes morales ni les peines existantes.",
[effect('coordination','urbanisme-agrement-fin-mesures-automatiques',
"Retrait du renvoi aux mesures de L510-2, sans compter une nouvelle abolition de l'agrément.",
"La liste de responsabilité des personnes morales mentionne L510-2 en plus des autres articles pénaux.",
"L510-2 n'est plus cité ; les autres infractions, l'amende et les peines complémentaires subsistent.",
'legal_duty',"Personnes morales susceptibles d'être poursuivies pour des infractions d'urbanisme.",
"Coordination à la même entrée en vigueur que l'abrogation de L510-2 ; pas de suppression des créances ou décisions anciennes par cette seule liste.",
"Aucune obligation de remplacement et aucune nouvelle peine.",plain(paras(s)[0]),plain(paras(q)[0]))])

s=by_num['L480-5']['source_xml']; ps=paras(s)
new_pub="La publication et l'affichage du jugement de condamnation aux frais de la personne condamnée ne peuvent être ordonnés sur le seul fondement du présent article."
q=replace_once(s,ps[2],'<p>'+new_pub+'</p>')
q=add_end(q,"La suppression de la peine de publication et d'affichage s'applique aux condamnations prononcées à compter de l'entrée en vigueur de la loi, y compris pour des faits antérieurs. Elle s'applique également aux condamnations antérieures qui ne sont pas devenues définitives. Les condamnations devenues définitives avant cette date et les créances qui en résultent restent soumises à leur régime antérieur.")
record('L480-5',q,
"Réforme de fond : suppression de la peine complémentaire facultative de publication dans deux journaux régionaux ou locaux et d'affichage aux frais du condamné. Cette publicité payante supplémentaire n'est pas indispensable à la remise en conformité, à la démolition ou à la réaffectation ordonnées par le juge ; elle ne remplace ni leur exécution ni l'information procédurale des parties. Les deux premiers alinéas sont maintenus intégralement, y compris les observations du maire, la décision même sans avis et les deux procédures pénales simplifiées. La transition bénéficie aux condamnations non définitives sans effacer les dettes issues des condamnations définitives.",
"Trois alinéas sources lus en entier ; le troisième porte désormais l'interdiction de prononcer cette seule peine sur ce fondement, afin de conserver la position des deux premiers, puis vient la transition. Les renvois L480-4 et L610-1 restent opérants. Les articles 495 à 495-6 et 495-7 à 495-16 procédure pénale ne sont pas joints au corpus fourni : contrôle de coordination hors des cinq codes nécessaire, sans suppression implicite des droits de défense, de motivation ou de recours. Les pouvoirs de publicité sur des fondements légalement autonomes ne sont pas déclarés abrogés. Source ABROGE_DIFF avec échéance au 1er janvier 2029 : aucun report de cette échéance n'est décidé ici.",
'material_reduction',
"La source autorisait une peine payante de publication dans deux journaux et d'affichage ; cette faculté pénale est retirée, sans retirer les mesures matérielles de réparation ni leurs garanties judiciaires.",
"Le coût évité dépend du prononcé de la peine et des frais réels, inconnus. Aucune suppression de toutes les publicités légales ni des autres fondements de peine n'est démontrée.",
"Aucune charge nouvelle n'est identifiée : la publicité payante disparaît sans avis, déclaration ou support de remplacement ; les procédures judiciaires existantes sont conservées.",
[effect('obligation_removed','urbanisme-fin-publication-penale-payante',
"Suppression de la peine facultative de publication et d'affichage aux frais du condamné.",
"Le tribunal peut imposer la publication de tout ou partie de la condamnation dans deux journaux départementaux régionaux ou locaux et son affichage, aux frais du délinquant.",
"Aucune peine de publication ni d'affichage ne peut être imposée sur le seul fondement de cet article ; conformité, démolition et réaffectation subsistent.",
'legal_duty',"Personnes physiques et morales condamnées pour les infractions visées par L480-4 ou L610-1.",
"Condamnations nouvelles et anciennes non définitives ; condamnations déjà définitives et créances correspondantes préservées.",
"Aucun support de publication ou circuit d'information de remplacement.",plain(ps[2]),new_pub)],
removed=["La peine complémentaire de publication aux frais du délinquant dans deux journaux régionaux ou locaux et d'affichage du jugement est supprimée."])

record('L480-6',None,
"Maintien intégral nécessaire : l'extinction de l'action publique ne doit pas laisser sans traitement matériel des travaux irréguliers après décès, dissolution ou amnistie. Le texte protège simultanément les intéressés et ayants droit par leur mise en cause et limite la recevabilité à la durée qu'aurait eue l'action publique. Il ne taxe pas une succession et n'impose aucune déclaration fiscale : supprimer les droits de succession ne justifie pas d'effacer une obligation réelle de remise en état. La saisine par le ministère public et les observations techniques servent le contrôle du juge, sans dossier privé de remplacement.",
"Les quatre alinéas séparés par br ont été lus, ainsi que la note d'entrée en vigueur au 1er janvier 2020 de l'ordonnance du 18 septembre 2019. Cette date historique n'est pas celle du projet. L480-5 demeure applicable pour les mesures de remise en état, mais la proposition du lot en retire la publicité payante : ce renvoi n'en rétablit pas le pouvoir pour les décisions futures. La source indique une fin de validité au 1er janvier 2029 et ABROGE_DIFF ; cette échéance reste à coordonner avec le texte différé non joint, sans prorogation décidée ici.",
'retained_necessary',
"Aucun nouvel allègement n'est revendiqué : l'action de réparation survit dans un cadre contradictoire et prescrit, distinct d'une sanction successorale ou d'un impôt sur le décès.",
"Le maintien ne préjuge pas l'imputabilité civile aux ayants droit ni les droits réels régis par d'autres textes ; le calendrier différé de 2029 reste à vérifier.",
"Aucune charge nouvelle n'est identifiée : la saisine, la mise en cause des parties et la borne de prescription sont maintenues, sans nouveau certificat fiscal.")

s=by_num['L480-7']['source_xml']; ps=paras(s)
q=replace_once(s,", qui ne peut être révisée que dans le cas prévu au troisième alinéa du présent article,", "")
no_raise="Le montant journalier de l'astreinte ne peut être augmenté après son prononcé."
q=replace_once(q,ps[2],'<p>'+no_raise+'</p>')
q=add_end(q,"L'interdiction d'augmenter le montant journalier de l'astreinte s'applique à compter de l'entrée en vigueur de la loi, y compris aux astreintes déjà prononcées. Les astreintes et les augmentations légalement prononcées avant cette date conservent leur montant, sans nouvelle augmentation. Les créances antérieures, les recours et les possibilités de reversement ou de dispense prévues au quatrième alinéa restent préservés.")
record('L480-7',q,
"Réforme de fond : suppression du pouvoir de relever à une ou plusieurs reprises l'astreinte judiciaire après une année d'inexécution, y compris au-delà de 500 euros par jour. La contrainte initiale, le délai fixé par le tribunal, l'exécution provisoire et la durée de course jusqu'à exécution complète restent suffisants pour assurer l'exécution avec les voies d'exécution d'office distinctes. Le troisième alinéa conserve sa place et interdit les augmentations ; la restriction de révision du deuxième est coordonnée. Le quatrième alinéa est intégralement maintenu : reversement et dispense partielle restent possibles pour les difficultés et le comportement de l'intéressé, dans les dossiers futurs aussi. Les montants déjà légalement prononcés restent dus mais ne peuvent être augmentés après la réforme.",
"Quatre alinéas sources lus, plafond initial de 500 € par jour inchangé. L480-4-1 renvoie aux conditions de cet article : la réduction lui bénéficie sans nouvelle mesure distincte. L480-8 conserve la liquidation au moins annuelle ; L480-9 conserve l'exécution d'office après décision et la protection des tiers. Il ne faut pas confondre cette astreinte judiciaire avec les 1 000 €/jour et 100 000 € administratifs de L481-1. La suppression de la révision à la hausse ne ferme ni le reversement ni la dispense du quatrième alinéa, y compris sur les sommes anciennes. Aucun délai de quinze jours du contrat de travail n'est applicable.",
'material_reduction',
"Par comparaison avec les quatre alinéas officiels, le risque de relèvements répétés et sans plafond légal spécial est retiré pour l'avenir. L'astreinte initiale et la faculté favorable de reversement ou dispense sont conservées.",
"Les astreintes déjà prononcées, y compris les relèvements antérieurs au-delà de 500 €/jour, ne sont pas rétroactivement ramenées à ce plafond. Aucun gain forfaitaire ni coût national n'est calculé.",
"Aucune charge nouvelle n'est identifiée : la hausse facultative est supprimée sans déclaration ou pénalité de remplacement ; les conditions favorables du quatrième alinéa restent identiques.",
[effect('obligation_removed','urbanisme-astreinte-fin-relevements',
"Retrait des augmentations judiciaires répétées de l'astreinte, même au-delà du maximum initial.",
"Astreinte initiale plafonnée à 500 €/jour ; après une année sans exécution, relèvements judiciaires possibles à plusieurs reprises, même au-delà de ce plafond.",
"Astreinte nouvelle au plus de 500 €/jour, sans augmentation après prononcé ; anciens montants légalement fixés conservés sans nouvelle hausse ; reversement et dispense possibles.",
'euro',"Bénéficiaires de travaux ou d'utilisations du sol irréguliers soumis à une injonction judiciaire et lotisseurs renvoyés par L480-4-1.",
"Aucune augmentation décidée après l'entrée en vigueur, même pour les astreintes existantes ; montants antérieurs et recours préservés.",
"Aucune sanction de remplacement ; l'exécution d'office et l'astreinte initiale sont des dispositifs existants.",plain(ps[2]),no_raise)],
removed=["Le pouvoir du tribunal de relever à plusieurs reprises l'astreinte après un an, y compris au-delà du plafond initial de 500 euros par jour, est supprimé."],
benefit="L'article offre un délai judiciaire d'exécution et un plafond initial de 500 € par jour : ils sont conservés pour les nouvelles décisions. Son quatrième alinéa permet le reversement ou la dispense d'une partie des astreintes selon le comportement et les difficultés rencontrées ; il est repris intégralement et reste accessible aux situations futures ainsi qu'aux créances anciennes. L'exécution provisoire n'est pas un avantage du débiteur mais un pouvoir du tribunal, maintenu. Le seuil d'un an limitait temporellement un pouvoir de hausse désormais supprimé : son retrait ne retire aucun allègement, puisque aucune augmentation nouvelle n'est permise, même après un an.")

record('L480-8',None,
"Maintien intégral nécessaire : la liquidation au moins annuelle rend l'astreinte exécutable et évite que son suivi soit abandonné ; le recouvrement public et le reversement aux communes organisent une créance déjà prononcée, sans déclaration privée supplémentaire. Le prélèvement de 4 % est retranché des sommes déjà perçues au bénéfice des communes, et n'est pas un supplément de 4 % facturé au redevable. Le supprimer seul transférerait une recette entre administrations sans réduire son astreinte ; cette opération ne répond pas à une baisse démontrée de prélèvement privé.",
"Alinéa entier et absence de notes vérifiés. 4 % est conservé comme frais d'assiette et de recouvrement sur les sommes perçues, pas comme taux de la sanction. R480-5 lu en entier avec notes vides : il renvoie aux articles 112 à 124 du décret 2012-1246 pour l'état de recouvrement. Ce décret extérieur n'est pas joint et n'est pas présenté comme réécrit. Le renvoi L480-4-1 et la réforme de L480-7 restent cohérents ; aucun relèvement d'astreinte supprimé ne peut être recréé par liquidation.",
'retained_necessary',
"Aucun montant dû par le redevable n'est réduit. Le mécanisme de recouvrement est maintenu ; supprimer le seul prélèvement interne de 4 % ne démontrerait pas une baisse de sa charge.",
"Le coût réel du recouvrement et le partage optimal État/communes ne sont pas chiffrés. Aucune économie nationale ou baisse de taxe n'est imputée à ce maintien.",
"Aucune charge nouvelle n'est identifiée : la fréquence minimale et le circuit existants demeurent, sans pièce, nouvelle majoration ou nouveau taux pour le débiteur.")

record('L480-9',None,
"Maintien intégral nécessaire de l'exécution d'une décision de justice non exécutée à l'issue du délai. Les frais ne sont pas une taxe générale mais ceux des travaux nécessaires à la décision ; leur suppression reporterait la charge sur la collectivité sans supprimer les travaux. Le deuxième alinéa est indispensable : aucune atteinte aux droits des tiers ni expulsion d'occupants sur ce fondement sans intervention préalable du tribunal judiciaire. Cette protection ne doit pas être retirée au nom d'une simplification.",
"Les deux alinéas br et la note historique du 1er janvier 2020 ont été lus. Ni délai du jugement ni condition d'exécution incomplète ni frais et risques ni protection des tiers ne sont déplacés. Le maintien complète L480-5 et L480-7 ; il ne ressuscite ni la publication payante ni le relèvement d'astreinte retirés. La compétence du tribunal judiciaire et les procédures d'expulsion extérieures ne sont pas remplacées par un préavis privé de quinze jours.",
'retained_necessary',
"Le maintien entier garantit l'effectivité de la remise en état ordonnée par le juge et protège les tiers contre une exécution administrative sans décision judiciaire préalable.",
"Aucune estimation des frais d'exécution ni transfert de leur financement n'est proposée ; les garanties procédurales d'autres codes ne sont pas réécrites.",
"Aucune charge nouvelle n'est identifiée : les travaux nécessaires et leur régime financier demeurent identiques, avec la même protection des droits acquis.")

record('L480-10',None,
"Maintien intégral nécessaire de la validation favorable des autorisations de lotir, permis et certificats : la retirer pourrait fragiliser des possibilités de construire et la sécurité des titres. L'article n'impose ni taxe, ni nouvelle autorisation, ni dépôt, ni contrôle supplémentaire. Le coefficient d'occupation des sols et la surface hors œuvre nette décrivent le champ de la validation historique ; leur vocabulaire ancien ne justifie pas d'effacer les effets favorables encore opposables.",
"Introduction, 1° a), b), c), 2° et 3° lus entièrement ; date du 1er janvier 1978 et référence à la surface totale du terrain maintenues. La validation ne crée pas de nouveau coefficient d'occupation des sols ni une procédure moderne de répartition obligatoire. Les effets attachés aux titres qui entrent dans le champ du texte restent ouverts, même lorsqu'ils sont invoqués dans un litige futur ; aucune date de réforme n'est tirée de la date historique.",
'retained_necessary',
"Aucune réduction nouvelle n'est comptée : le texte officialise déjà des validations qui sécurisent la constructibilité et les titres, sans charge administrative à retirer.",
"Le maintien ne valide pas un titre pour un autre motif d'illégalité et ne rétablit pas les anciens coefficients dans les documents actuels ; la portée contentieuse individuelle reste à apprécier.",
"Aucune charge nouvelle n'est identifiée : les validations et leur périmètre sont conservés sans justificatif, dépôt ou taux nouveau.")

record('L480-12',None,
"Maintien intégral nécessaire de l'incrimination d'obstacle aux contrôles légalement habilités. Elle garantit l'effectivité de la recherche d'infractions et de la prévention des travaux dangereux ou contraires aux protections environnementales ; elle n'est pas une obligation déclarative générale ou une autorisation préalable. La suppression des contraintes injustifiées ne dispense pas de laisser exercer des contrôles dans leurs conditions légales, notamment celles protégeant le domicile.",
"Alinéa entier, six mois d'emprisonnement et 7 500 € lus et maintenus. L461-1 à L461-4 et L480-17 ont été lus entièrement avec notes : les visites administratives et judiciaires ont des fondements et garanties distincts. La simple absence d'assentiment à une entrée domiciliaire ne devient pas une infraction par elle-même lorsque la loi exige cet assentiment ou une autorisation judiciaire. L480-4-2 conserve ce renvoi pour les personnes morales ; aucune extension de peine n'est rédigée.",
'retained_necessary',
"Le contrôle demeure protégé par une incrimination d'obstruction, avec les habilitations et limites légales ; aucune charge ou peine nouvelle et aucune baisse de prélèvement ne sont annoncées.",
"Les modalités de poursuite et d'appréciation de l'obstacle relèvent du droit pénal et des garanties des visites, qui ne sont pas intégralement réécrits dans cet article.",
"Aucune charge nouvelle n'est identifiée : même comportement incriminé, mêmes personnes habilitées, mêmes peines et absence de nouveau registre ou document obligatoire.")

s=by_num['L480-13']['source_xml']
q=replace_once(s,"mentionnés à l'article L. 146-6", "mentionnés aux articles L. 121-23, L. 121-50, L. 121-26, L. 121-27, L. 121-24 et L. 121-25")
record('L480-13',q,
"Coordination nécessaire à droit constant : remplacement, au b du 1°, du renvoi ancien L146-6 par les six références expressément indiquées dans la note de concordance officielle jointe. La liste a) à n), les conditions d'annulation préalable du permis, la saisine particulière du préfet, les délais de deux ans et la prescription historique des travaux achevés avant la publication de la loi du 13 juillet 2006 sont intégralement maintenus. L'exception favorable à certaines constructions agricoles biologiques en bois n'est pas supprimée. Aucun nouveau corps stylistique ni aucune suppression de protection littorale n'est revendiqué.",
"Les dix-neuf paragraphes de texte et les deux notes ont été lus intégralement. L121-23, L121-50, L121-26, L121-27, L121-24 et L121-25 ont été lus en entier dans le corpus, notes comprises ; la substitution suit exactement la concordance fournie par l'article 3 de l'ordonnance 2015-1174, sans présumer que toute la norme vient de SRU. Ces six renvois actualisés ne figurent pas dans les cibles imposées de reference-targets.json : leur fondement est la note jointe et les sources locales, pas une empreinte cible inventée. L600-6 a été lu, ses deux alinéas justifiant l'exception hors zones pour le préfet. Tous les seuils restent : trois cents mètres, mille hectares, cent mètres, avant le 1er janvier 2010, moins de mille mètres carrés et deux ans aux deux points de départ distincts. Les renvois ruraux, miniers, patrimoniaux et environnementaux extérieurs restent inchangés mais ne sont pas intégralement disponibles ici ; leur validité actuelle reste à contrôler. Aucun schéma de plage, dérogation littorale ou avantage futur n'est fermé. La correction du renvoi ne prétend pas solder l'examen des 209 articles SRU.",
'coordination_only',
"Le seul changement est l'actualisation nécessaire d'un renvoi obsolète selon la note officielle jointe. La source entière, ses quatorze catégories de zones, son exception agricole et ses limites de recours restent matériellement identiques.",
"Les textes extérieurs des zones et les qualifications agricoles ne sont pas tous joints ; aucune réduction de taxe, de délai de recours ou de protection environnementale n'est établie.",
"Aucune charge nouvelle n'est identifiée : la concordance ne crée ni zone supplémentaire, ni titre, ni procédure, ni preuve agricole nouvelle et conserve les conditions favorables.",
[effect('coordination','urbanisme-demolition-concordance-littorale',
"Actualisation de la référence à l'ancien article L146-6 selon les six descendants de la note officielle.",
"Le b du 1° vise l'ancien L146-6, avec identification réglementaire des espaces et exception agricole biologique en bois.",
"Le même b vise les six articles de concordance ; identification réglementaire, exception agricole, dates, surfaces et délais identiques.",
'other',"Propriétaires de constructions conformes à un permis et parties aux actions civiles en démolition.",
"Concordance à droit constant, sans réouverture de délai et avec maintien de la prescription historique du dernier alinéa.",
"Aucun zonage nouveau ni nouvelle formalité ; conditions des régimes littoraux autonomes préservées.",plain(paras(s)[3]),plain(paras(q)[3]))])

record('L480-14',None,
"Maintien intégral nécessaire de l'action civile autonome permettant à la commune ou à l'EPCI de demander au tribunal la conformité ou la démolition d'un ouvrage irrégulier. Elle ne fait pas double emploi avec une condamnation pénale : elle protège l'intérêt urbanistique dans des conditions et un délai distincts. Le juge reste nécessaire pour ordonner la mesure. Le renvoi à L421-8 conserve les dispenses de formalité et leurs exceptions de fond ; le délai de dix ans limite l'exposition du constructeur et ne doit pas être supprimé en conservant l'action.",
"Alinéa normatif et note historique du 1er janvier 2020 lus entièrement ; dix ans courent de l'achèvement des travaux, pas de la publication du transfert comme à L480-16. L421-8 et L421-5 à L421-5-3 lus : le renvoi n'étend pas la conformité aux constructions exclues par L421-8 et ne recrée pas de demande d'autorisation pour les travaux dispensés. La note de 2019-964 ne fixe pas la date d'une réforme future. Les recours et autres délais civils ne sont pas modifiés.",
'retained_necessary',
"L'action judiciaire et sa prescription restent intégralement maintenues ; aucune nouvelle démarche ni réduction normative n'est comptée. L'intervention du juge et les exceptions du renvoi protègent le constructeur et les tiers.",
"L'article ne réforme pas les procédures civiles ni les règles de conformité de fond ; aucune réduction des délais ou des frais de justice n'est démontrée.",
"Aucune charge nouvelle n'est identifiée : même action, mêmes autorités, même délai de dix ans et mêmes exceptions, sans nouvelle attestation.",
benefit="Les avantages possibles sont la dispense de formalité pour certains travaux, les exclusions de conformité résultant de L421-8 et la prescription de dix ans à compter de l'achèvement. Ils restent intégralement applicables aux opérations futures éligibles : l'article vise seulement une violation effective de L421-8 pour les travaux dispensés, et n'impose pas un titre supprimé ou une conformité dont cet article les dispense. L'action en démolition ou conformité n'est pas une exonération fiscale mais un recours judiciaire protecteur de l'intérêt urbanistique ; le maintenir avec sa borne temporelle ne retire aucun avantage au seul motif de son origine législative.")

record('L480-15',None,
"Maintien intégral nécessaire du recours en annulation des ventes ou locations de terrains irrégulières, aux frais et dommages du lotisseur : il protège l'acquéreur et l'intérêt public sans imposer de déclaration supplémentaire. Le second alinéa est un allègement autonome, empêchant l'annulation lorsque le permis de construire a été accordé pour la parcelle. Le retirer aggraverait la situation contractuelle alors que les obligations générales subsistent ; il est donc conservé sans restriction aux seuls actes antérieurs.",
"Les deux alinéas sont lus et maintenus. Le renvoi au titre IV du livre IV couvre le régime des lotissements ; L442-3 et L480-4-1 ont été lus. Le bénéfice du permis accordé s'applique dans le champ de l'article même aux ventes et locations futures recevables. Il ne s'agit pas de l'inopposabilité administrative de L510-3, abrogée séparément : aucune confusion de domaine ou d'effets contractuels.",
'retained_necessary',
"Aucune simplification nouvelle : recours protecteur et exception favorable interdisant l'annulation des parcelles dotées d'un permis sont maintenus en entier.",
"Les autres causes de nullité, responsabilités civiles et conditions de délivrance d'un permis ne sont pas modifiées et restent à leur champ propre.",
"Aucune charge nouvelle n'est identifiée : absence de nouveau corps et maintien de l'exception favorable sans attestation ou condition ajoutée.")

record('L480-16',None,
"Maintien intégral nécessaire de la prescription de dix ans et de l'impossibilité d'opposer ensuite la violation de la réglementation des lotissements. Il s'agit d'une limite favorable aux actions et à l'instabilité des titres, pas d'un délai minimal imposé pour entreprendre une opération. L'abroger tout en laissant subsister les obligations et les actions pourrait retirer cette sécurité ; aucune taxe ou formalité supplémentaire n'est attachée à cette disposition.",
"Alinéa entier et absence de notes vérifiés. Le point de départ est la publication des actes portant transfert de propriété à la publicité foncière, et non l'achèvement des travaux. Le maintien ne crée pas de nouvelle publicité et ne rétablit pas la contribution de sécurité immobilière supprimée par une autre coordination. La publication civile et la sécurité des droits des tiers restent distinctes de son financement fiscal.",
'retained_necessary',
"Le texte entier est maintenu pour préserver la borne de dix ans et l'inopposabilité ultérieure de l'irrégularité de lotissement ; aucune réduction nouvelle n'est déclarée.",
"La portée de cette prescription dans chaque action et son articulation avec les autres délais civils ne sont pas élargies par le maintien.",
"Aucune charge nouvelle n'est identifiée : le texte ne crée ni publication additionnelle, ni taxe, ni justificatif ; le délai et son point de départ sont inchangés.")

record('L480-17',None,
"Maintien intégral nécessaire des règles d'accès pour la recherche d'infractions : le contrôle des établissements est encadré par l'information préalable du procureur et son droit d'opposition ; les horaires et les garanties renforcées du domicile protègent la vie privée. L'assentiment manuscrit est une preuve d'un consentement essentiel, avec une alternative explicite pour la personne qui ne sait pas écrire ; ce n'est pas un justificatif générique redondant à supprimer. Retirer ces conditions accroîtrait la contrainte policière au lieu de l'alléger.",
"I et II lus entièrement, dont la distinction entre établissements ouverts au public hors horaires et domiciles visitables seulement entre 6 heures et 21 heures. L480-1, L480-12 et L461-1 à L461-4 ont été lus : ne pas fusionner l'enquête judiciaire avec le droit administratif de visite ni confondre l'assentiment et une autorisation privée de construire. Les dispositions du code de procédure pénale relatives aux visites, perquisitions et saisies ne sont pas jointes et ne sont pas présentées comme réécrites. Le préavis individuel du contrat unique n'est pas applicable à ces visites.",
'retained_necessary',
"Aucune réduction nouvelle n'est comptée : les conditions d'accès, horaires, opposition du procureur et consentement domiciliaire limitent nécessairement les pouvoirs de contrôle.",
"Les garanties du code de procédure pénale et leur application aux enquêtes restent extérieures au lot ; le consentement ne peut être remplacé par une présomption de silence.",
"Aucune charge nouvelle n'est identifiée : maintien du texte entier, y compris l'alternative favorable pour les personnes ne sachant pas écrire, sans nouveau formulaire.")

# L481-1 : fin des amendes administratives doubles et de l'exécution d'office fondée sur le seul zonage.
s=by_num['L481-1']['source_xml']; ps=paras(s)
q=replace_once(s,ps[1],'<p>1° Abrogé.</p>')
q=replace_once(q,"pris en application de l'amende ou de l'astreinte ordonnée", "pris en application de l'astreinte ordonnée")
q=replace_once(q,ps[10],'<p>III quater. - Abrogé.</p>')
assert q.count('ou qui se situent hors zones urbaines')==2
q=q.replace(' ou qui se situent hors zones urbaines','')
q=add_end(q,"V. - La suppression des amendes prévues au 1° du I et au III quater s'applique à compter de l'entrée en vigueur de la loi, y compris aux faits antérieurs n'ayant pas donné lieu à une décision de sanction devenue définitive. Les amendes devenues définitives avant cette date, leur recouvrement et les recours qui leur restent ouverts demeurent régis par les dispositions antérieures.")
q=add_end(q,"A compter de cette même date, aucune mesure d'exécution d'office ou de démolition ne peut être décidée ou entreprise sur le seul fondement de la situation des installations hors zones urbaines, y compris à la suite d'une mise en demeure ou d'une décision administrative antérieure. Les travaux déjà exécutés et les créances légalement nées à ce titre avant cette date restent régis par les dispositions antérieures, sans restitution générale. Les décisions de justice devenues définitives avant cette même date conservent leurs effets, sous réserve des règles d'application de la loi répressive plus douce lorsqu'elles sont applicables ; les pouvoirs fondés sur d'autres dispositions légales conservent leur régime propre.")
record('L481-1',q,
"Réforme de fond : supprimer les deux amendes administratives facultatives, chacune plafonnée à 30 000 euros, qui s'ajoutent aux poursuites pénales et au mécanisme coercitif de mise en conformité. La mise en demeure, sa prolongation favorable, le contradictoire, l'astreinte modulée de 1 000 €/jour au plus et 100 000 € au total ainsi que la substitution préfectorale restent. Retirer aussi la situation hors zones urbaines comme fondement autonome de travaux ou démolition d'office : le seul zonage ne démontre pas le risque essentiel justifiant ce pouvoir. Le IV conserve intégralement ce pouvoir pour un risque certain de santé ou sécurité, la protection des occupants et le jugement préalable en cas de démolition complète faute de régularisation technique. Il reste possible de saisir le juge sur les autres fondements applicables. Les 1° et III quater demeurent à leur place comme abrogés ; le III bis ne vise plus que l'astreinte. Transitions expresses pour sanctions non définitives et décisions d'exécution non encore mises en œuvre.",
"Quatorze paragraphes sources lus intégralement, puis comparés au nouveau corps. Renvois L421-1 à L421-5-3, L422-1 à L422-3-1, L480-1, L610-1 et L480-14 lus dans le corpus. Le d de L422-2 source vise encore la carence SRU : le renvoi de compétence s'applique dans sa version coordonnée, sans restaurer cette exception supprimée ; la correction de L422-2 reste hors lot. L481-2 retire les renvois aux deux amendes et garde les exonérations d'astreinte ; L481-3 est abrogé avec traitement des fonds consignés. Une astreinte n'est pas assimilée à une taxe, ni les deux amendes à deux taxes de production. L521-1, L521-2, L521-3-1 à L521-3-3 et L521-4 CCH ont été lus intégralement, notes comprises : maintien des protections de loyer, bail, hébergement, relogement, indemnisation et répression des pressions sur les occupants. La source locale de L521-1 présente un membre conditionnel isolé relatif à L184-1, et L521-3-3 renvoie encore au II abrogé de L521-3-2 : incohérences préexistantes à vérifier hors lot, sans correction silencieuse ni réduction de droits. Les règles européennes et constitutionnelles d'environnement et de participation ne sont pas dispensées, et les infractions de fond subsistent. Aucun défaut de permis sur une opération légalement dispensée ne peut être créé par les renvois. Aucun taux de remplacement ni économie publique chiffrée.",
'material_reduction',
"Deux amendes administratives superposées sont effectivement retirées et le champ de l'exécution d'office est réduit aux installations présentant un risque certain pour la santé ou la sécurité. Le levier d'astreinte est inchangé et les protections des occupants sont expressément maintenues sur tout leur champ source, y compris les installations non dangereuses hors zones urbaines.",
"La réduction n'abolit ni les poursuites pénales, ni l'astreinte, ni les obligations d'urbanisme, ni les actions judiciaires distinctes. Les dépenses publiques et le montant effectif des sanctions évitées ne sont pas chiffrés.",
"Aucune charge nouvelle n'est identifiée : aucun dépôt ou sanction de remplacement n'est ajouté. Le contradictoire, la protection des occupants et le contrôle judiciaire conservés sont déjà exigés par la source.",
[effect('obligation_removed','urbanisme-fin-amendes-administratives-doublees',
"Suppression des deux amendes administratives du 1° du I et du III quater, sans suppression des infractions pénales ni de l'astreinte.",
"Responsables de travaux irréguliers exposés à une amende administrative initiale d'au plus 30 000 euros et à une autre d'au plus 30 000 euros pour inexécution de la mise en demeure, en plus des autres voies.",
"Aucune de ces deux amendes administratives ne peut être prononcée ; astreinte existante modulée à 1 000 €/jour maximum, total 100 000 €, et sanctions pénales dans leur champ propre.",
'euro',"Personnes responsables des travaux et installations visés au I, soumises aux pouvoirs de l'autorité d'urbanisme.",
"Entrée en vigueur ; faits anciens bénéficient de la suppression pour sanctions non définitives, amendes définitives et droits de recours anciens préservés.",
"Aucune amende ou taxe de remplacement ; le mécanisme d'astreinte conservé préexistait.",plain(ps[10]),plain(paras(q)[14])) ,
 effect('obligation_removed','urbanisme-execution-office-risque-certain',
"Retrait de la seule implantation hors zone urbaine comme condition suffisante d'exécution ou de démolition administrative d'office.",
"Après mise en demeure infructueuse, exécution d'office possible pour risque certain de santé/sécurité ou seule situation hors zones urbaines ; démolition complète après jugement en l'absence de moyen technique de régulariser.",
"Ces pouvoirs du IV exigent un risque certain de santé ou sécurité, sans condition alternative de seul zonage ; protection des occupants et jugement préalable à la démolition complète conservés.",
'legal_duty',"Responsables et occupants d'installations irrégulières hors zones urbaines ne présentant pas un risque certain de santé ou de sécurité.",
"Aucune nouvelle décision ni mise à exécution sur le seul motif de zonage après l'entrée en vigueur, même sur ancienne mise en demeure ; travaux et créances antérieurs conservés.",
"Aucune autorisation de remplacement ; les voies judiciaires et les pouvoirs de sécurité autonomes demeurent dans leur champ antérieur.",plain(ps[11]),plain(paras(q)[11]))],
removed=["L'amende administrative initiale facultative d'un montant maximal de 30 000 euros prévue au 1° du I est supprimée.","L'amende administrative supplémentaire d'au plus 30 000 euros pour inexécution de la mise en demeure prévue au III quater est supprimée.","La possibilité de réaliser d'office des mesures ou une démolition sur le seul motif d'une implantation hors zones urbaines, sans risque certain de santé ou sécurité, est supprimée."])

s=by_num['L481-2']['source_xml'];ps=paras(s)
new_i="I. - L'astreinte prévue à l'article L. 481-1 court à compter de la date de la notification de l'arrêté la prononçant et jusqu'à la date d'exécution des opérations nécessaires à la mise en conformité ou des formalités permettant la régularisation. La date d'exécution peut être établie par tout moyen. Aucune astreinte n'est due pour la période postérieure à cette date au seul motif que la preuve de l'exécution a été fournie ultérieurement. Le recouvrement de l'astreinte est engagé par trimestre échu."
q=replace_once(s,ps[0],'<p>'+new_i+'</p>')
q=replace_once(q,"Les sommes dues au titre de l'astreinte ou de l'amende prévue aux I ou III quater de l'article L. 481-1", "Les sommes dues au titre de l'astreinte prévue à l'article L. 481-1")
q=replace_once(q,"l'arrêté a été pris ou l'amende prononcée", "l'arrêté a été pris")
q=replace_once(q,"l'astreinte ou l'amende est recouvrée", "l'astreinte est recouvrée")
q=add_end(q,"IV. - La règle d'arrêt de l'astreinte à la date d'exécution s'applique aux liquidations effectuées à compter de l'entrée en vigueur de la loi, y compris pour des astreintes antérieurement prononcées, sans remettre en cause les décisions de liquidation devenues définitives avant cette date. Les exonérations prévues au III restent applicables aux liquidations anciennes et nouvelles dans leurs conditions propres.")
q=add_end(q,"Les amendes devenues définitives avant l'entrée en vigueur de la loi et conservées par les dispositions transitoires de l'article L. 481-1 continuent d'être recouvrées selon le II du présent article dans sa rédaction antérieure, sans préjudice des recours qui leur restent ouverts.")
record('L481-2',q,
"Réforme de fond : l'astreinte s'arrête à l'exécution effective des opérations ou formalités permettant la régularisation, au lieu de dépendre de la date à laquelle il en est justifié ; une preuve produite plus tard ne doit pas créer des jours supplémentaires de contrainte après exécution. La preuve est libre, sans formulaire de remplacement. Coordination nécessaire de la suppression des deux amendes de L481-1 : seuls leurs renvois de recouvrement disparaissent pour l'avenir, pas de deuxième réduction de sanction comptée. Le recouvrement trimestriel, les bénéficiaires commune/EPCI/État et la faculté d'exonération partielle ou totale sont conservés ; transition pour liquidations non définitives, amendes définitives et recours anciens.",
"Trois alinéas sources lus en entier et maintenus dans leurs subdivisions I, II et III, avec IV transitoire ajouté. L481-1 est coordonné dans ce lot : 1 000 €/jour et plafond total 100 000 € n'augmentent pas. L'arrêt à l'exécution ne signifie pas qu'un dépôt incomplet vaut régularisation ; les formalités utiles doivent être réellement exécutées dans le champ de l'injonction. La charge de preuve des circonstances indépendantes du redevable au III n'est pas supprimée, mais aucune attestation nouvelle n'est ajoutée. Recouvrement trimestriel et destination des sommes strictement inchangés. Aucun effet rétroactif sur liquidation définitive et aucun droit à double restitution ; les amendes anciennes ne subsistent que selon la transition de L481-1.",
'material_reduction',
"Le nouveau texte écarte les jours d'astreinte postérieurs à l'exécution qui résulteraient du seul retard de justification. La suppression des renvois aux amendes est une coordination de la mesure portée par L481-1, sans deuxième amende supprimée ici.",
"Le nombre de jours et les montants évités dépendent de la date réelle d'exécution et de sa preuve ; aucun gain n'est démontré lorsque la liquidation retient déjà cette date. Les liquidations définitives antérieures ne sont pas rouvertes.",
"Aucune charge nouvelle n'est identifiée : aucune attestation ou dépôt daté nouveau n'est imposé ; la liberté de preuve allège la justification existante et les règles de recouvrement restent inchangées.",
[effect('obligation_removed','urbanisme-astreinte-arret-date-execution',
"Suppression de la continuation d'astreinte due au seul décalage entre l'exécution et la production de sa preuve.",
"Course de l'astreinte de la notification jusqu'à ce qu'il ait été justifié de l'exécution ; montant modulé de L481-1 au plus 1 000 €/jour et 100 000 € au total, exonération possible.",
"Arrêt à la date d'exécution des opérations ou formalités permettant la régularisation, prouvable par tout moyen ; aucun jour postérieur pour preuve tardive seule, mêmes plafonds et exonérations.",
'calendar_days',"Redevables d'une astreinte administrative L481-1 qui ont exécuté les mesures mais en apportent la preuve ultérieurement.",
"Liquidations nouvelles, y compris d'astreintes anciennes ; liquidations déjà définitives préservées et exonérations toujours accessibles.",
"Aucun justificatif de remplacement ; la preuve de la date réelle reste nécessaire si elle est contestée.",plain(ps[0]).split(' Le recouvrement')[0],new_i.split(' Le recouvrement')[0]),
 effect('coordination','urbanisme-fin-amendes-administratives-doublees',
"Retrait des renvois de recouvrement aux deux amendes supprimées à L481-1.",
"Le II règle ensemble le recouvrement des astreintes et des amendes des I et III quater de L481-1.",
"Le II vise les astreintes seules ; la transition conserve le recouvrement des amendes devenues définitives avant la bascule.",
'legal_duty',"Communes, EPCI, État et redevables concernés par le recouvrement des sanctions administratives d'urbanisme.",
"Même bascule que L481-1, sans effacer les amendes anciennes définitives ni créer de remboursement général.",
"Aucun nouveau circuit ou taux de recouvrement.",plain(ps[1]),plain(paras(q)[1]))],
removed=["La course de l'astreinte après l'exécution effective, lorsqu'elle résulterait seulement d'une justification produite ultérieurement, est expressément exclue."],
benefit="Le III permet une exonération partielle ou totale de l'astreinte lorsque le redevable établit que l'inexécution n'est pas de son fait : ce pouvoir et sa condition sont repris intégralement et restent ouverts pour toutes liquidations futures éligibles, pas seulement pour les anciens dossiers. Le recouvrement par trimestre échu est conservé. L'arrêt à l'exécution avec preuve libre améliore la situation sans restreindre l'exonération. Les amendes supprimées n'avaient pas d'exonération dans cet article ; leurs anciennes créances définitives restent soumises aux droits de recours applicables. Les bénéficiaires publics du produit ne sont pas des exonérations du redevable.")

q="""<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi.</p>
<p>Aucune consignation ne peut être ordonnée ou recouvrée sur son seul fondement à compter de cette date, y compris en exécution d'une décision antérieure. Le privilège attaché à cette seule consignation ne peut plus être exercé.</p>
<p>Les sommes encore consignées sur ce fondement sont restituées à leur déposant. Les sommes régulièrement imputées avant cette date ne donnent pas lieu à restitution du seul fait de l'abrogation ; les demandes de restitution d'un indu et les recours restent ouverts dans les conditions qui leur sont applicables.</p>
<p>Les créances distinctes légalement nées au titre de travaux déjà exécutés, leurs garanties légalement constituées et leur recouvrement demeurent soumis à leurs règles propres, sans double paiement. Les obligations de mise en conformité, les astreintes et les pouvoirs d'exécution fondés sur d'autres dispositions légales ne sont pas supprimés par le présent article.</p>"""
s=by_num['L481-3']['source_xml']
record('L481-3',q,
"Abrogation intégrale pour l'avenir de la consignation administrative générale du coût des travaux après mise en demeure, de son privilège spécial et de la règle de recours non suspensif propre à cette consignation. Cette immobilisation financière peut se cumuler avec l'astreinte et les voies d'exécution déjà prévues ; aucune fonction de sécurité additionnelle indispensable n'est démontrée pour la maintenir indistinctement dans tous les cas. Le risque certain de santé ou de sécurité conserve les pouvoirs de L481-1 et les voies judiciaires restent distinctes. Aucun cautionnement ou dépôt ne remplace la consignation. Les fonds encore immobilisés sont libérés, sans restitution générale des sommes régulièrement déjà imputées ni extinction des frais de travaux distincts.",
"I et II lus intégralement, y compris restitution progressive, privilège au rang de l'article 1920 CGI et opposition non suspensive. Le III ter de L481-1 retire expressément son renvoi à L481-3 dans ce lot : la substitution préfectorale ne peut plus ordonner cette consignation générale. La consignation littorale de L121-22-5 II et L425-16 répond à un régime de démolition pour recul du trait de côte distinct : elle n'est pas abrogée. Aucune baisse de taxe ou de dette de travaux n'est déduite de la libération d'une garantie ; l'avantage est la suppression d'une immobilisation obligatoire et de son privilège. Les frais de recouvrement et le coût de restitution des fonds ne sont pas chiffrés.",
'mixed',
"La consignation obligatoire facultativement ordonnée par l'administration et son privilège sont supprimés, sans garantie équivalente. La restitution des fonds encore déposés libère une immobilisation et impose leur clôture aux comptables ; ce traitement public est recensé, sans annulation d'un impôt ni du coût des travaux dus sur un fondement distinct, et sans solde net établi.",
"La mesure ne supprime pas les consignations littorales, les astreintes ni les frais de travaux d'office légalement exigibles. La restitution immédiate de tous les fonds encore consignés ajoute un traitement public par rapport à la restitution au fil des travaux ; le montant et le coût net sont inconnus.",
"Aucune charge nouvelle n'est identifiée pour les personnes contrôlées : pas de caution, registre ou déclaration substitutive. La restitution des fonds impose un traitement de clôture aux comptables, sans nouvelle obligation périodique ; son coût net reste inconnu.",
[effect('obligation_removed','urbanisme-fin-consignation-administrative-generale',
"Suppression de la consignation du coût des travaux et du privilège de recouvrement qui lui est propre.",
"Après mise en demeure inexécutée, possibilité d'imposer une consignation égale au montant des travaux, restituée à mesure de leur exécution, avec privilège et recours non suspensif.",
"Aucune nouvelle consignation ni recouvrement d'une consignation antérieure sur ce seul fondement ; restitution des fonds encore consignés, sans suppression des dettes de travaux autonomes.",
'financing',"Personnes mises en demeure de régulariser des travaux sur le fondement de L481-1, hors autres consignations légalement autonomes.",
"Entrée en vigueur ; consignations anciennes non recouvrées écartées et fonds encore déposés restitués ; imputations régulières antérieures et recours conservés.",
"Aucune garantie de remplacement. Traitement public de restitution ponctuel nécessaire, sans solde budgétaire global établi.",plain(s).split(' Pour le recouvrement')[0],plain(q).split(' Aucune consignation')[1].split(' Le privilège')[0].join(['Aucune consignation','']))],
repeal="Suppression de la consignation générale du coût des travaux après mise en demeure, de son privilège et de sa procédure propre de recouvrement ; libération des fonds encore consignés, sans abolition des garanties littorales autonomes.")

q="""<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi.</p>
<p>Aucune nouvelle mise en demeure ni astreinte ne peut être prononcée sur son fondement. Les mises en demeure antérieures cessent de produire leurs effets pour l'avenir et les astreintes prononcées sur ce fondement cessent de courir à compter de cette date.</p>
<p>Les créances légalement nées à raison des jours de retard antérieurs à cette date, leur liquidation, leur recouvrement, les prescriptions et les recours demeurent régis par les dispositions antérieures et les garanties qui leur sont applicables. Il n'est créé ni restitution générale de sommes légalement dues ni réouverture d'un délai de recours expiré.</p>
<p>Les règles d'usage des logements prévues à l'article L. 151-14-1, leurs exceptions et les droits contractuels des occupants ne sont pas modifiés par cette abrogation. Les autres actions et pouvoirs légalement autonomes restent soumis à leurs conditions propres.</p>"""
s=by_num['L481-4']['source_xml']
record('L481-4',q,
"Abrogation intégrale du dispositif spécial de mise en demeure et d'astreinte administrative lié à l'usage exclusif de résidence principale. La seule occupation différente, sans danger caractérisé pour la santé ou la sécurité, ne justifie pas ce levier administratif supplémentaire de 1 000 €/jour et 100 000 € total. La règle matérielle de L151-14-1 et ses exceptions ne sont pas supprimées ou transformées en autorisation nouvelle ; les voies légalement autonomes, y compris les recours relatifs au PLU lorsqu'ils en remplissent les conditions, restent distinctes. Les mises en demeure cessent pour l'avenir et les astreintes cessent de courir ; les droits et contestations des périodes antérieures restent préservés.",
"Cinq paragraphes sources lus, y compris le délai d'un an et sa prorogation d'un an, le contradictoire et les deux plafonds. Ces garanties n'ont plus à conditionner une procédure entièrement supprimée ; elles restent pertinentes pour l'examen des créances antérieures selon leur régime. L151-14-1 source entière et notes lues : ses six alinéas ont leur fondement autonome de 2024 et des modifications ultérieures, sans assimilation aux quotas SRU ; location temporaire de la résidence principale, cessation de l'obligation après suppression du secteur et conditions territoriales demeurent. La note fiscale 2027 jointe à L151-14-1 ne fixe pas la bascule de cette abrogation. L610-1 lu : il réprime certaines infractions au PLU, mais n'est pas présenté comme un dispositif automatiquement identique couvrant toute occupation sans travaux. Aucune nouvelle sanction de remplacement n'est instituée, ni extension de L481-1 à l'occupation sans travaux.",
'material_reduction',
"Le levier spécial de contrainte administrative sur l'occupation est effectivement supprimé, avec arrêt des astreintes futures. Il ne s'agit pas d'une suppression de la règle d'usage, d'une taxe ou d'une simple modification de délai.",
"Les règles de résidence principale du PLU et leurs effets contractuels restent applicables ; les cas relevant réellement de poursuites ou actions autonomes ne sont pas abolis. Montants et nombre de dossiers concernés inconnus.",
"Aucune charge nouvelle n'est identifiée : aucun agrément, déclaration d'occupation, amende ou registre ne remplace cette mise en demeure et cette astreinte ; le régime matériel distinct n'est pas étendu.",
[effect('obligation_removed','urbanisme-fin-astreinte-speciale-residence-principale',
"Suppression de la mise en demeure et de l'astreinte administratives spéciales de L481-4.",
"Propriétaire ou locataire d'un logement soumis à L151-14-1 : mise en demeure jusqu'à un an, prorogeable un an, et astreinte possible jusqu'à 1 000 €/jour, total 100 000 €.",
"Aucune mise en demeure ou astreinte sur ce fondement ; course des astreintes existantes arrêtée à l'entrée en vigueur, créances antérieures et règle d'usage distincte conservées.",
'legal_duty',"Propriétaires ou locataires de logements concernés par l'usage exclusif de résidence principale de L151-14-1.",
"Bascule à l'entrée en vigueur ; droits et créances pour retards antérieurs restent soumis aux garanties anciennes, sans remboursement général.",
"Aucun dispositif de sanction ou de déclaration substitutif ; pas d'extension des procédures de travaux aux seules occupations.",plain(paras(s)[2]),plain(paras(q)[1]))],
repeal="Suppression de la procédure spéciale de mise en demeure et de l'astreinte administrative d'occupation des logements de L151-14-1 ; arrêt des effets futurs des mesures antérieures, sans suppression des exceptions ni des garanties et créances relatives aux retards anciens.")

q="""<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi.</p>
<p>Aucune évacuation de locaux, remise en état, démolition ou expulsion ne peut plus être ordonnée sur son seul fondement à compter de cette date, y compris dans une instance en cours. L'administration ne peut entreprendre sur ce seul fondement l'exécution d'une mesure qui n'a pas été définitivement ordonnée avant cette date.</p>
<p>Les décisions juridictionnelles devenues définitives avant cette date conservent leurs effets, sous réserve des règles d'application de la loi répressive plus douce lorsqu'elles sont applicables et des voies de recours restant ouvertes. Les mesures déjà exécutées, les droits des tiers et les créances légalement nées des frais d'exécution antérieurs demeurent régis par les dispositions antérieures, sans restitution générale ni réouverture d'un délai de recours expiré.</p>
<p>Les agréments prévus à l'article L. 510-1 et les sanctions qui demeurent applicables sur ce fondement ne sont pas supprimés. Les mesures de sécurité, de protection de la santé, de l'environnement ou du patrimoine et les actions judiciaires reposant sur d'autres fondements légaux restent soumises à leurs conditions propres.</p>"""
s=by_num['L510-2']['source_xml']
record('L510-2',q,
"Abrogation intégrale des mesures automatiques d'évacuation, remise en état et démolition dans un délai d'au plus un an, ainsi que de leur exécution administrative aux frais du délinquant. Le seul défaut d'agrément économique ne démontre pas la nécessité d'une démolition ou d'une expulsion obligatoire indépendamment du danger ou des atteintes réelles. L'agrément préexistant et les sanctions de L510-1 restent distincts, conformément à la coordination qui en a déjà retiré le critère social ajouté par SRU ; ils ne sont pas déclarés abrogés. Aucune nouvelle déclaration ne remplace les mesures supprimées. Les instances en cours bénéficient de la disparition de ce fondement automatique, les décisions définitives et droits anciens étant traités expressément.",
"Deux alinéas lus intégralement, y compris délai d'au plus un an et exécution par les services du ministère. L510-1 source et proposition locale lues entièrement, note fiscale 2026 comprise : le projet actuel ne supprime que le critère social, pas l'agrément de fond ni son VI pénal ; ne pas les abolir implicitement par cette sanction. L480-4-2 retire dans ce lot le renvoi à L510-2 et L510-3 est abrogé en coordination. Les pouvoirs de sécurité et les voies judiciaires autonomes restent sans extension ; la liste de mesures distinctes n'invente aucun renvoi à une disposition non fournie. Le contrôle de la qualification répressive ou réparatrice des décisions antérieures reste nécessaire pour appliquer la réserve de loi plus douce ; aucune prétendue approbation juridique.",
'material_reduction',
"La source imposait au tribunal des mesures matérielles puis leur exécution administrative ; leur caractère obligatoire et leur fondement spécial disparaissent pour les décisions nouvelles et instances pendantes. L'agrément économique lui-même n'est pas supprimé.",
"Les décisions juridictionnelles déjà définitives et les pouvoirs autonomes ne sont pas effacés ; aucune économie de travaux, indemnisation générale ou suppression de toutes les sanctions d'agrément n'est chiffrée.",
"Aucune charge nouvelle n'est identifiée : pas de déclaration d'activité, de garantie, de registre ou de nouveau permis en échange de la suppression des mesures automatiques.",
[effect('obligation_removed','urbanisme-agrement-fin-mesures-automatiques',
"Suppression des évacuations, remises en état et démolitions obligatoires attachées à L510-2 et de leur exécution administrative spéciale.",
"En application de L510-1, évacuation et remise en état ordonnées par le tribunal dans un délai d'au plus un an, démolition des constructions irrégulières dans les mêmes conditions, puis exécution aux frais du délinquant.",
"Aucune mesure nouvelle sur le seul fondement de L510-2, y compris en instance pendante ; agrément et sanctions autonomes maintenus, décisions définitives antérieures préservées selon la transition.",
'legal_duty',"Occupants et responsables de locaux ou installations entrant dans le champ de l'agrément de L510-1.",
"Entrée en vigueur de la loi ; mesures et frais déjà exécutés, décisions définitives et recours protégés, sous réserve de la loi plus douce lorsqu'elle s'applique.",
"Aucune autorisation ou formalité de remplacement ; les pouvoirs autonomes restent dans leur champ.",plain(s).split(' Passé le délai')[0],plain(paras(q)[1]).split(" L'administration")[0])],
repeal="Suppression des évacuations, remises en état et démolitions judiciaires obligatoires pour défaut d'agrément ainsi que de leur exécution administrative spéciale ; décisions définitives et frais antérieurs préservés, agrément et protections autonomes distincts.")

q="""<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi.</p>
<p>Sous réserve des décisions devenues définitives avant cette date, les contrats et conventions ne peuvent plus être déclarés inopposables à l'administration sur son seul fondement à compter de cette date, quelle que soit leur date de conclusion. Leur opposabilité reste soumise aux autres règles qui leur sont légalement applicables ; elle ne vaut ni agrément ni régularisation d'une installation ou d'une construction.</p>
<p>Les décisions devenues définitives, les mesures déjà exécutées et les droits des tiers antérieurement constitués conservent leurs effets. Les créances, prescriptions et recours relatifs aux situations antérieures restent soumis aux règles applicables, sans remise en cause automatique d'une décision définitive ni réouverture d'un délai de recours expiré.</p>"""
s=by_num['L510-3']['source_xml']
record('L510-3',q,
"Abrogation intégrale en coordination avec la suppression de L510-2 : l'inopposabilité spéciale des contrats lors des expulsions, remises en état ou démolitions fondées sur cet article perd son objet pour l'avenir. Elle ne doit pas être conservée comme une éviction autonome des droits contractuels. La transition protège les contrats futurs et anciens invoqués après la bascule, sous réserve des décisions définitives et des droits déjà constitués. Aucun contrat ne devient pour autant un agrément, ni une régularisation d'urbanisme ; les autres causes légales d'inopposabilité demeurent dans leur champ.",
"Alinéa entier lu, couvrant création et extension industrielles, annexes, établissements scientifiques ou techniques, occupation de locaux vacants et construction de bureaux. L510-1 et L510-2 ont été lus, ainsi que la proposition locale de L510-1 : aucune nouvelle autorisation économique n'est supprimée ici. Le renvoi à L510-2 est retiré avec la règle spéciale qui en dépend, sans prétendre effacer des expulsions définitives passées. Il s'agit de contrats et conventions immobiliers ou d'implantation, pas d'un renvoi au contrat de travail privé ou à son indemnité ; aucune condition d'ancienneté ni préavis individuel de quinze jours ne s'applique.",
'coordination_only',
"L'abrogation retire la règle d'inopposabilité liée exclusivement aux mesures spéciales supprimées de L510-2. Elle appartient à la même mesure et ne constitue ni un second agrément aboli ni une baisse fiscale supplémentaire.",
"Les effets des contrats selon le droit commun et les autres décisions d'expulsion demeurent distincts ; les décisions définitives et droits des tiers ne sont pas annulés par cette coordination.",
"Aucune charge nouvelle n'est identifiée : aucun agrément de substitution ou justificatif contractuel nouveau ; le droit commun de l'opposabilité reste seul applicable dans son champ.",
[effect('coordination','urbanisme-agrement-fin-mesures-automatiques',
"Retrait de l'inopposabilité contractuelle spéciale attachée aux mesures abrogées de L510-2.",
"Contrats et conventions conclus en violation des exigences d'agrément inopposables à l'administration lors des mesures de L510-2.",
"Aucune inopposabilité fondée sur cet article après la bascule, même pour contrats anciens ; autres règles d'opposabilité et agrément conservés.",
'legal_duty',"Parties aux contrats et conventions d'implantation industrielle, scientifique, technique ou de bureaux entrant dans le champ du texte.",
"Entrée en vigueur ; invocation future de contrats anciens incluse, décisions définitives, mesures exécutées et droits des tiers préservés.",
"Aucune formalité de remplacement ; l'opposabilité ne constitue pas une autorisation d'urbanisme.",plain(s),plain(paras(q)[1]).split(' Leur opposabilité')[0])],
repeal="Suppression de l'inopposabilité spéciale des contrats et conventions lors des mesures d'expulsion, de remise en état et de démolition de L510-2, en coordination avec leur abrogation ; décisions définitives et droits des tiers antérieurs préservés.")

# Maintien autonome de la protection des occupants malgré le retrait du seul fondement hors zone urbaine.
r=answer['L481-1']
old="Lorsque ces installations sont occupées, l'occupant défini au premier alinéa de l'article L. 521-1 du code de la construction et de l'habitation bénéficie du régime de protection des occupants défini aux articles L. 521-1 à L. 521-4 du même code."
new="Lorsque les installations mentionnées au premier alinéa du présent IV sont occupées, l'occupant défini au premier alinéa de l'article L. 521-1 du code de la construction et de l'habitation bénéficie du régime de protection des occupants défini aux articles L. 521-1 à L. 521-4 du même code. Cette protection s'applique également, dans les mêmes conditions, aux occupants des installations situées hors zones urbaines issues des travaux entrepris et exécutés mentionnés au I pour lesquelles la mise en demeure est restée sans effet, même en l'absence de risque certain pour la sécurité ou pour la santé. Elle bénéficie aux installations existantes comme aux installations nouvelles et n'autorise pas, à elle seule, une exécution d'office ou une démolition."
r['proposed_xml']=replace_once(r['proposed_xml'],old,new)
r['reason'] += " La protection des occupants des installations non dangereuses hors zones urbaines est conservée sur un fondement autonome exprès, pour les installations futures aussi, malgré le retrait de ce motif d'exécution d'office."
r['review_notes'] += " Le deuxième alinéa du IV précise le champ des protections sans le réduire à celui des pouvoirs de démolition désormais restreints ; aucune exonération de loyer, continuité de bail, indemnité de relogement ou droit d'occupation applicable n'est retiré par le changement d'antécédent."
r['substantive_impact']['effects'].append(effect('relief_preserved','urbanisme-execution-office-risque-certain',
"Maintien du régime de protection des occupants pour les installations hors zones urbaines, même sans risque certain et même futures.",
"Le IV protège les occupants des installations présentant un risque certain ou situées hors zones urbaines, après mise en demeure infructueuse.",
"Même champ de protection des occupants conservé expressément ; le retrait du seul zonage comme motif de travaux d'office ne ferme pas les droits du CCH.",
'legal_duty',"Occupants au sens de L521-1 CCH des installations concernées, notamment hors zones urbaines sans risque certain.",
"Maintien pour les installations existantes et nouvelles ; les règles propres du régime CCH restent applicables.",
"Aucune condition nouvelle de bénéfice ni extension d'une contrainte à une population nouvelle.",
old,new))

# La libération anticipée du stock ajoute une tâche publique, recensée séparément de la coupe privée.
r=answer['L481-3']
r['substantive_impact']['effects'].append(effect('obligation_added','urbanisme-fin-consignation-administrative-generale',
"Traitement de restitution de tous les fonds encore consignés, en remplacement de leur restitution progressive selon les travaux.",
"Restitution aux intéressés au fur et à mesure de l'exécution des mesures prescrites ; les fonds restent immobilisés avant cette exécution.",
"Les comptables doivent restituer les fonds encore consignés dès l'abrogation, sans attendre l'exécution des travaux ; coût de traitement non chiffré.",
'legal_duty',"Comptables publics détenant les fonds et déposants auxquels les fonds doivent revenir.",
"Stock de fonds encore consignés à l'entrée en vigueur ; aucune restitution des imputations antérieures régulières ni double paiement.",
"Traitement public ponctuel ajouté à la bascule, sans nouveau dépôt privé ou reporting périodique ; solde net inconnu.",
plain(by_num['L481-3']['source_xml']).split(' Pour le recouvrement')[0],
"Les sommes encore consignées sur ce fondement sont restituées à leur déposant."))

# Coordination interne : ne pas laisser subsister le renvoi à la consignation supprimée.
r=answer['L481-1']
r['proposed_xml']=replace_once(r['proposed_xml'],"au présent article et aux articles L. 481-2 et L. 481-3", "au présent article et à l'article L. 481-2")
r['reason'] += " Le III ter est coordonné pour retirer aussi le renvoi à la consignation de L481-3 abrogée."
r['substantive_impact']['effects'].append(effect('coordination','urbanisme-fin-consignation-administrative-generale',
"Retrait de la substitution préfectorale pour ordonner la consignation générale supprimée à L481-3.",
"Le III ter permet au préfet de se substituer pour les pouvoirs de L481-1, L481-2 et L481-3 après un mois sans réponse.",
"La substitution ne vise plus que L481-1 et L481-2 ; le mois, la motivation et les pouvoirs de mise en conformité et d'astreinte sont conservés.",
'legal_duty',"Préfets, autorités d'urbanisme et personnes concernées par une mise en demeure de travaux.",
"Même entrée en vigueur que l'abrogation de L481-3 ; les consignations anciennes sont traitées par sa transition.",
"Aucun pouvoir de garantie ou dépôt de remplacement.",plain(paras(by_num['L481-1']['source_xml'])[9]),plain(paras(r['proposed_xml'])[9])))

checks = {
'LEGITEXT000006072050|LEGIARTI000006901112': "L1234-1 concerne le préavis de licenciement privé : source d'un ou deux mois selon ancienneté et exceptions, proposition de quinze jours calendaires pour les seuls contrats nouveaux avec anciens préavis préservés. L480-4 ne le vise pas : ses L421-1 à L421-5-3 et autorisations temporaires concernent des travaux, non une rupture d'emploi. Aucun préavis de quinze jours n'est introduit dans les délais d'urbanisme, et les protections ou procédures collectives du travail ne sont pas supprimées.",
'LEGITEXT000006072050|LEGIARTI000019071087': "L1221-2 source autorise certains CDD ; sa proposition réserve toute nouvelle relation privée au contrat unique indéterminé, les missions ou formations limitées ne fixant pas le terme de l'emploi. Aucun renvoi de L480-4 ne vise ce texte : le 2 porte sur des autorisations d'urbanisme limitées ou précaires et le délai de remise en état du sol. Leur maintien ne recrée ni CDD, ni terme d'emploi, et ne restreint aucune aide future attachée à une situation éligible dans le contrat unique.",
'LEGITEXT000006072050|LEGIARTI000035644154': "L1234-9 source vise l'indemnité de licenciement à partir de huit mois ; sa proposition applique aux nouveaux contrats un seuil d'un an à la fin effective, préavis inclus, puis 0,20 mois par année totale, prorata de mois complets et plafond de six mois, employeur seul, avec faute grave et régimes anciens ou spéciaux distincts. L480-4 ne renvoie pas à cette indemnité : l'amende et les travaux ne sont pas une rupture de contrat. Aucun seuil d'ancienneté ni plafond indemnitaire n'est transposé aux sanctions ou à la démolition.",
'LEGITEXT000006074075|LEGIARTI000045525738': "Le 3 de L480-4 vise réellement la mise en demeure du III de L121-22-5 pour démolition et remise en état lorsque le recul du trait de côte menace la sécurité au-delà de trois ans. Source et proposition prévoient au moins six mois pour le premier arrêté puis au moins un mois de mise en demeure ; ces délais ne deviennent pas quinze jours de préavis privé. Le VIII exclut les constructions ou extensions sous bail réel L321-18 environnement : cette exception et la dispense de formalité L421-5-1 restent applicables aux situations futures. Le projet cible conserve encore l'envoi personnel du récépissé, incompatible avec la coordination actuelle après six mois ; cette correction hors lot est signalée, sans affaiblir la consignation ni l'obligation de sécurité."
}
r=answer['L480-4']
for key in refs['requirements'][r['code_id']+'|'+r['source_id']]:
    r['reference_checks'].append(dict(target_key=key, view_sha256=refs['targets'][key]['view_sha256'], assessment=checks[key]))

out=[answer[a['number']] for a in sources]
Path('answer.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('answer.json',len(out),'articles')
