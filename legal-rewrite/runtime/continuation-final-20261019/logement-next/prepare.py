import json,pathlib,html,hashlib
P=pathlib.Path(__file__).parent
S=json.loads((P/'source.json').read_text());D={}
def add(n,paras,reason,benefit,removed=None,notes=''):
 a={'proposed_xml':''.join('<p>'+html.escape(t,quote=False)+'</p>' for t in paras),'reason':reason,'benefit_review':benefit,'review_notes':notes}
 if removed:a.update(change_type='normative_reduction',reform_policy_id='editorial_direction_2026_10_19',removed_provisions=removed)
 D[n]=a
def repeal(n,scope,kept,reason,benefit,notes=''):
 add(n,["Le présent article est abrogé à compter de l'entrée en vigueur de la présente rédaction.",scope,kept],reason,benefit,[scope],notes)
 D[n].update(change_type='full_repeal',repeal_policy_id='editorial_direction_2026_10_19',repeal_scope=scope)

repeal('R423-2',
"La déclaration d'intention de changer de régime comptable, sa transmission pour avis et les délais de douze mois, de six mois et du 31 juillet propres à ce changement cessent d'être exigibles. Ils ne peuvent servir à instaurer un choix nouveau entre comptabilité publique et comptabilité commerciale, l'article L. 421-17 imposant cette dernière depuis le 1er janvier 2021.",
"Les décisions de changement de régime valablement prises sous la législation antérieure et les effets qu'elles ont déjà produits demeurent acquis. Aucun changement de date d'effet, nouvelle délibération, avis ou déclaration de remplacement n'est demandé pour les régulariser. Les pièces nécessaires à la clôture et au contrôle des anciens exercices sont conservées selon les règles qui leur sont applicables.",
"Abrogation des préparatifs d'un choix supprimé par l'article 88 I 15° de la loi ELAN à compter de 2021. Il serait contraire à L421-17 de simplifier le délai tout en restaurant ce choix. Aucun gain actuel lié à la suppression d'un régime déjà fermé n'est chiffré.",
"Les changements anciens restent valables et aucune formalité ne doit être refaite. La faculté ancienne de choisir le régime public ne peut être présentée comme un avantage futur légalement ouvert depuis 2021 ; les droits issus des décisions prises avant sa fermeture subsistent.",
"Source entière lue ; L421-17 actuel et sa précédente version contrôlés, ainsi que l'article 88 I 15° à 19° de la loi n°2018-1021. R423-3 et R423-4 sont coordonnés dans le même paquet.")

repeal('R423-3',
"Aucune entrée nouvelle en comptabilité publique ne peut être préparée sur le fondement du présent article. Le dernier rapport du commissaire aux comptes n'a plus à être joint à une déclaration d'intention supprimée par l'abrogation de l'article R. 423-2.",
"Pour les seuls passages légalement intervenus sous la législation antérieure, les comptes, états de trésorerie, fonds disponibles, balances, bilans, comptes de résultat et états de développement des soldes des comptes de tiers restent conservés et accessibles au comptable compétent. Les documents nécessaires à l'approbation des anciens comptes et les réserves régulièrement émises restent attachés à ces comptes. Le droit d'accès aux documents des exercices précédents subsiste ; l'abrogation ne rouvre ni ne recommence le délai de six mois de formulation des réserves. Aucune pièce déjà disponible n'a à être transmise une seconde fois.",
"Suppression du dossier d'entrée dans un régime qui n'est plus ouvert. Conservation explicite de l'accès aux archives et des réserves anciennes, sans nouveau dossier ni remise répétée pour achever une opération passée.",
"Les droits d'accès et les réserves des comptables sur les anciens exercices sont conservés. Aucun office n'a à recréer un dossier ou une attestation pour bénéficier de la validité de son ancien changement de régime.")

repeal('R423-4',
"Les délais et transmissions préparatoires à un changement futur de comptabilité publique vers la comptabilité commerciale ne sont plus imposés par le présent article, le régime commercial étant obligatoire depuis le 1er janvier 2021.",
"Cette abrogation ne dispense pas d'achever et de contrôler les derniers comptes publics légalement ouverts. Les informations de trésorerie et de fonds disponibles, balances, bilans, comptes de résultat, états des comptes de tiers et pièces justificatives antérieurs au changement restent conservés. Le directeur général garde accès à tout document relatif aux exercices précédents. Les opérations anciennes déjà accomplies n'ont pas à être répétées ; les documents déjà détenus sont réutilisés, sans réouverture des délais d'un mois avant clôture ou de quatre mois après clôture.",
"Retrait des formalités de migration futures devenues sans objet depuis 2021, avec conservation de la clôture, des preuves et du droit d'accès utile à la reprise des comptes. Aucun changement comptable nouveau n'est créé.",
"Le directeur général conserve son droit d'accès aux anciens comptes et les opérations de clôture ne sont pas abandonnées. Le réemploi des pièces évite d'imposer aux offices une seconde migration ou des copies nouvelles pour conserver les effets de celle déjà réalisée.")

add('R423-5',[
"L'exercice budgétaire et comptable de l'office commence le 1er janvier et s'achève le 31 décembre de la même année. Cette durée ne s'impose pas au premier exercice d'un office nouvellement mis en exploitation ni à l'exercice de cessation définitive de son activité."
],"Maintien du cadre annuel nécessaire à la comparabilité et à l'approbation des comptes. Les deux exceptions évitent des clôtures fictives à la création ou à la cessation ; aucune procédure d'autorisation pour les utiliser n'est ajoutée.",
"Les offices nouvellement exploités ou cessant définitivement leur activité conservent l'exception à l'année civile. Aucun exercice complet, justificatif particulier ou accord ministériel n'est imposé pour exercer cette faculté.")

add('R423-6',[
"Le conseil d'administration délibère sur les orientations générales du budget avant de le voter. Il peut le faire au cours de la même séance que celle de l'examen du budget, dès lors que les administrateurs disposent en temps utile d'informations à jour permettant de débattre des orientations avant le vote.",
"Aucun délai distinct de deux mois, réunion séparée ou rapport supplémentaire n'est exigé à cette fin. Les documents déjà établis pour le budget et le rapport prévu à l'article R. 421-17 peuvent être utilisés."
],"Suppression de la fenêtre obligatoire de deux mois avant l'examen et faculté explicite d'utiliser une même séance et un même dossier. Il ne s'agissait pas d'une attente minimale de deux mois ; aucune économie provenant d'une telle attente fictive n'est revendiquée. Le débat préalable, l'information à jour et le rapport présidentiel dû subsistent.",
"Les administrateurs, dont les représentants des locataires, conservent le débat, la délibération et les informations avant leur vote. La faculté d'une séance commune réduit les démarches sans transformer l'approbation du budget en décision du seul directeur.",
["Fenêtre obligatoire des deux mois précédant l'examen du budget ; la réunion et le dossier peuvent explicitement être communs sans acte documentaire supplémentaire."],
"R421-16 et R421-17 lus en entier. Le rapport sur la politique de l'office dû par le président n'est pas abrogé et sert au débat ; aucune obligation équivalente supplémentaire n'est créée.")

add('R423-7',[
"Le budget de l'office est présenté selon la nomenclature budgétaire et comptable applicable à la comptabilité commerciale et les instructions homologuées conjointement par les ministres chargés du logement, des finances et des collectivités territoriales, dans le respect des règles fixées par l'Autorité des normes comptables.",
"Le tableau de financement prévisionnel indique, pour l'exercice, les variations prévues des emplois stables et des ressources stables.",
"Chaque activité exercée pour le compte d'un tiers est identifiée dans un état prévisionnel annexe comportant un compte de résultat prévisionnel en équilibre et, s'il y a lieu, un tableau de financement prévisionnel. Un excédent du compte de résultat ne constitue pas un déséquilibre de cet état. Les fonds et résultats de chaque tiers restent identifiables.",
"Ces états peuvent être constitués directement à partir des données et tableaux déjà établis, sans nouvelle saisie ou reproduction d'informations identiques. Les prescriptions propres à l'ancien régime de comptabilité publique ne fondent aucune obligation de présentation supplémentaire pour les exercices relevant de la comptabilité commerciale."
],"Retrait du double circuit d'instructions selon un choix de régime fermé depuis 2021. Le budget, le financement prévisionnel et la séparation des activités de tiers restent complets. Réemploi des données plutôt qu'une annexe ressaisie ; la tolérance des états excédentaires de l'ancien R423-14 est expressément conservée pour l'avenir.",
"L'excédent d'un état prévisionnel annexe reste autorisé, et les activités exercées pour autrui restent possibles. Leurs résultats ne sont pas confondus avec ceux de l'office ; le réemploi n'impose ni autorisation nouvelle ni état fictivement équilibré par écrêtement d'un excédent.",
["Circuit futur de présentation propre à un office en comptabilité publique, régime fermé par L421-17.","Nouvelle saisie ou reproduction des mêmes informations pour constituer les états prévisionnels annexes."],
"Note DILA de 2014 lue. Coordination avec R423-12-1, R423-14 abrogé et R423-29 maintenu : l'exception d'excédent des états annexes est reprise ici, pas perdue par l'abrogation du paragraphe public.")

add('R423-9',[
"A l'arrêté des comptes annuels, l'office qui possède un patrimoine locatif calcule le rapport entre l'autofinancement net défini à l'article R. 423-1-4 et la somme des produits financiers et des produits d'activité, à l'exclusion de la récupération des charges locatives. Le résultat figure dans les informations présentées au conseil d'administration avec les comptes selon l'article R. 423-28, sans rapport d'activité distinct imposé à cette seule fin.",
"Un arrêté conjoint des ministres chargés du logement, du budget, des finances et des collectivités territoriales précise le calcul et fixe les taux de référence en pourcentage.",
"Lorsque le ratio de l'exercice est inférieur à l'un de ces taux, le directeur général en explique les causes au conseil d'administration et propose, s'il y a lieu, des mesures internes de redressement durable. Les mêmes obligations s'appliquent lorsque la moyenne du ratio sur trois années consécutives est inférieure à l'un de ces taux.",
"Les explications et propositions peuvent être intégrées au dossier d'approbation des comptes et examinées dans la même délibération. Aucune délibération spécifique ni rapport séparé ne sont exigés ; les chiffres déjà issus des comptes sont réutilisés."
],"Suppression de la délibération spécifique et du rapport distinct consacrés au ratio, sans supprimer l'alerte sur la solvabilité. Calcul, exclusion des charges récupérées, taux réglementaires et moyenne de trois ans demeurent ; aucun seuil n'est inventé.",
"L'exclusion de la récupération des charges locatives de l'assiette du ratio et la possibilité de proposer des mesures seulement si elles sont nécessaires restent conservées. La mutualisation du dossier évite des démarches nouvelles sans diminuer l'information du conseil ou les aides financières autonomes.",
["Délibération spécifique séparée pour l'alerte liée au ratio.","Rapport d'activité autonome et nouvelle saisie de chiffres déjà compris dans les comptes pour cette seule alerte."],
"R423-1-4, L452-1 et R423-70 lus : aucune modification du calcul de l'autofinancement net, des aides CGLLS, des cotisations ou du régime distinct des sociétés HLM. Les taux fixés par arrêté restent à leur valeur applicable ; le présent projet n'en propose aucun nouveau.")

add('R423-11',[
"Les ajustements de valeur des immobilisations corporelles et financières d'un office, dans le cadre d'une réévaluation de ses comptes, sont réalisés conformément aux règles comptables applicables. Ils ne sont pas soumis à une autorisation ministérielle préalable propre au présent article.",
"Les immeubles donnés en location-attribution ou en location-vente ne peuvent pas être réévalués.",
"L'absence d'autorisation préalable ne dispense ni de la sincérité des comptes, ni de la certification et des contrôles applicables. Elle n'autorise pas à modifier les droits des occupants ou des acquéreurs. Aucune déclaration de remplacement n'est instituée."
],"Suppression de l'autorisation préalable par trois ministres pour une réévaluation qui reste régie et contrôlée par les normes comptables. L'interdiction concernant location-attribution et location-vente, protectrice des bénéficiaires, demeure intégralement.",
"Les personnes en location-attribution ou location-vente gardent l'interdiction de réévaluation de leur immeuble. Les offices peuvent utiliser la réévaluation admise par les normes comptables sans agrément nouveau, sans modification des droits des occupants et sans déclaration de substitution.",
["Autorisation ministérielle préalable des ajustements de valeur de réévaluation, pour les offices à comptabilité commerciale comme pour l'ancien régime public."],
"L421-17 rend le régime commercial obligatoire depuis 2021. La suppression porte sur l'agrément, pas sur les normes comptables, la certification ou les pouvoirs autonomes de contrôle.")

add('R423-12',[
"Le conseil d'administration décide de l'affectation du résultat de l'exercice clos.",
"Avant cette affectation, les plus-values ou moins-values nettes résultant des cessions immobilières sont retraitées selon les instructions mentionnées au premier alinéa de l'article R. 423-7.",
"L'excédent est affecté dans l'ordre suivant :",
"– A l'apurement du report à nouveau déficitaire, sans dépasser le solde débiteur de ce compte ;",
"– Aux réserves, notamment pour la part destinée au financement des investissements ;",
"– Au report à nouveau créditeur.",
"Le déficit est porté au compte de report à nouveau."
],"Maintien de l'affectation qui couvre les pertes antérieures et réserve les moyens d'investissement. Ces règles empêchent de présenter une cession patrimoniale comme une ressource d'exploitation librement distribuable ; leur suppression ne serait pas une simple réduction documentaire.",
"La possibilité de constituer des réserves pour investir et de reporter le solde créditeur demeure. Le retraitement des cessions et l'apurement des déficits ne suppriment aucune aide, exonération ou faculté d'investissement existante.",notes="Note DILA de 2014 lue ; les trois subdivisions en tirets et leur ordre de priorité sont conservés. L'exception pour les activités de tiers demeure à R423-12-1.")

add('R423-12-1',[
"L'article R. 423-12 ne s'applique pas aux activités que l'office exerce pour le compte d'un tiers.",
"Le conseil d'administration arrête le résultat de clôture de chacune de ces activités ; ce résultat est repris dans le compte de résultat prévisionnel de l'état annexe correspondant de l'exercice suivant. Il peut statuer dans la délibération d'approbation des comptes, dès lors que le résultat de chaque activité est identifié, sans délibération matériellement distincte."
],"Conservation de la dérogation soustrayant les activités de tiers à l'affectation du résultat propre de l'office. Possibilité explicite d'une même délibération plutôt que plusieurs actes, sans confusion des résultats ni captation des fonds de tiers.",
"L'exception à l'ordre d'affectation de R423-12 et la reprise du résultat propre à chaque activité restent disponibles pour les activités futures. Le tiers ne perd ni l'identification de ses fonds ni le bénéfice de la dérogation lorsque le conseil utilise un acte commun.",
["Exigence d'une délibération matériellement distincte écartée expressément lorsque chaque résultat de tiers est identifié dans l'acte commun."],
"La source n'exigeait pas expressément des délibérations matériellement distinctes : cette faculté est clarifiée pour empêcher une interprétation formaliste, sans présenter la suppression d'une obligation séparée certaine comme un gain établi.")

repeal('R423-13',
"Le format budgétaire propre à l'ancien régime de comptabilité publique ne peut plus être imposé aux nouveaux exercices sur le fondement du présent article. Le budget relevant de la comptabilité commerciale demeure régi par l'article L. 421-21 et les dispositions réglementaires applicables à ce régime.",
"Les comptes de résultat, tableaux de financement et de capacité d'autofinancement ainsi que les annexes de dette, de personnel, d'investissement et de fonds de roulement des anciens exercices publics restent conservés et utilisables pour leur clôture et leur contrôle. Aucun budget passé n'a à être reconstitué dans un format nouveau.",
"Abrogation du cadre public dont L421-19 a été abrogé au 1er janvier 2021. Pas de suppression du budget commercial ou des informations financières essentielles : la mesure retire un second cadre obsolète.",
"L'office reste dispensé d'un second format public pour les exercices commerciaux et conserve les documents utiles aux droits anciens. Aucune annexe ou attestation de remplacement n'est créée pour obtenir cette dispense.")

repeal('R423-14',
"Les conditions de vote chapitre par chapitre et d'équilibre réel propres au régime public supprimé ne s'appliquent plus à un exercice nouveau. Le vote et l'équilibre du budget commercial relèvent de l'article L. 421-21.",
"L'exception permettant un état prévisionnel annexe excédentaire demeure applicable aux activités futures dans les conditions de l'article R. 423-7 réécrit. L'abrogation ne modifie pas l'appréciation des anciens budgets publics, la protection des dépôts de garantie des locataires ni les droits nés des opérations correspondantes.",
"Retrait d'un contrôle budgétaire assis sur L421-19 abrogé, sans restaurer une exigence d'équilibre public au régime commercial. La dérogation favorable des états annexes excédentaires reçoit un fondement exprès dans R423-7.",
"La faculté d'avoir un état annexe excédentaire est expressément maintenue pour l'avenir. La protection ancienne des dépôts de garantie des locataires et des opérations déjà réalisées subsiste ; aucune utilisation de ces dépôts pour équilibrer de nouveaux budgets n'est autorisée par l'abrogation.")

repeal('R423-15',
"Les autorisations de programme, délibérations particulières et états selon un modèle public ne sont plus exigés pour les exercices nouveaux sur le seul fondement du présent article. La programmation pluriannuelle des investissements reste possible dans le cadre du budget commercial et des compétences du conseil d'administration.",
"Les autorisations de programme valablement votées demeurent valables sans limite de durée jusqu'à leur annulation et restent révisables. Les crédits de paiement, engagements et contrats antérieurs continuent d'être exécutés et suivis selon leurs règles applicables ; aucun plafond de dépense ancien n'est relevé par l'abrogation. Les états déjà établis sont réutilisés sans nouvelle délibération ni copie requise pour leur seule conservation.",
"Suppression des formalités propres aux chapitres limitatifs de l'ancien régime public, sans annuler des programmes d'investissement, ni rendre exigible un nouveau modèle pour les contrats déjà engagés.",
"Les autorisations anciennes conservent leur durée non limitée et leur faculté de révision. L'investissement pluriannuel reste possible pour l'avenir ; l'abrogation ne raccourcit pas une autorisation favorable et n'annule pas les engagements envers les tiers.")

repeal('R423-16',
"Les décisions modificatives et seuils d'alerte propres au budget public prévus par le présent article ne peuvent plus être imposés aux nouveaux exercices commerciaux. Les modifications de ces derniers restent régies par l'article L. 421-21 et l'article R. 423-25.",
"Les décisions et mouvements de crédits légalement intervenus pour un ancien exercice public conservent leurs effets. Les règles alors applicables aux chapitres limitatifs, à l'économie générale du budget et à la disponibilité du fonds de roulement restent prises en compte pour achever ou contrôler ces opérations ; aucun nouveau rapport périodique ou décision modificative ne doit être produit pour un exercice définitivement clos.",
"Abrogation des procédures publiques concurrentes de la procédure commerciale de R423-25. Les contrôles actuels et les engagements passés subsistent ; aucune alerte de sécurité financière ne disparaît dans le régime effectivement applicable.",
"Les financements et prélèvements sur fonds de roulement valablement autorisés dans le passé ne sont pas annulés. Le budget commercial reste évaluatif hors les cas légaux où le préfet le règle ; l'ancien régime limitatif n'est pas étendu aux offices actuels.")

repeal('R423-17',
"La communication des virements et les états de suivi propres à l'ancien régime public cessent d'être exigés pour les nouveaux exercices. Le suivi du budget commercial et l'information du conseil d'administration restent assurés selon l'article R. 423-25.",
"Les virements anciens valablement décidés et leurs effets sont conservés. Les documents existants restent accessibles pour vérifier les crédits limitatifs et l'exécution des anciens budgets, sans nouvelle saisie ou répétition d'une transmission déjà réalisée. La présente abrogation ne remet pas en cause les délégations ou compétences que le conseil tient d'autres dispositions applicables.",
"Suppression du second circuit de suivi et de transmission au comptable public pour les exercices actuels, sans retirer l'information annuelle et l'alerte financière conservées à R423-25.",
"Les virements effectués régulièrement gardent leurs effets et les facultés de gestion du budget commercial ne sont pas réduites. Aucun nouveau contrôle préalable du comptable public n'est créé pour des virements relevant d'un régime qui ne lui est plus soumis.")

repeal('R423-17-1',
"L'approbation de règles, plans de comptes et états propres aux offices en comptabilité publique ne fonde plus d'obligation pour les exercices nouveaux soumis à la comptabilité commerciale. Les règles et le plan applicables à ces exercices relèvent notamment de l'article R. 423-29.",
"Les règles publiques applicables aux anciens exercices restent utilisables pour les clore, les conserver et les contrôler. Les documents anciens ne sont pas convertis dans un plan nouveau pour le seul effet de l'abrogation. Aucun nouvel avis, homologation ou état de remplacement n'est institué.",
"Abrogation du circuit de normalisation exclusivement public fermé depuis 2021, sans modifier l'autorité des normes comptables pour les offices commerciaux ni imposer une conversion rétrospective.",
"Les offices n'ont pas à refaire leurs anciens comptes dans un plan nouveau et gardent les règles nécessaires à leur contrôle. Le régime commercial commun n'est pas doublé d'une nouvelle homologation propre à chaque office.")

repeal('R423-18',
"Le dispositif de saisine pour déficit propre à l'ancien régime public, avec ses seuils de 10 % et de 5 %, ne s'applique pas à un exercice nouveau. Pour les offices soumis au régime commercial, les pouvoirs définis par l'article L. 421-21 demeurent applicables, sans contrôle de remplacement créé par la présente abrogation.",
"Les mesures prises régulièrement pour les anciens exercices publics et les droits résultant des protocoles de prévention, de consolidation ou d'aide au rétablissement de l'équilibre restent préservés. L'abrogation ne ferme aucune aide prévue par l'article L. 452-1, y compris pour les organismes et situations futurs éligibles.",
"Retrait d'une procédure publique sans champ nouveau depuis 2021. Le seuil réduit lié à une aide n'est pas transformé en condition d'accès à cette aide et le contrôle légal du régime actuel subsiste.",
"Les concours et protocoles de la CGLLS restent ouverts aux bénéficiaires futurs et leurs droits antérieurs sont conservés. La disparition d'un seuil d'alerte propre à un régime fermé ne supprime ni une exonération de cotisation ni une aide financière.")

repeal('R423-23',
"Aucune contribution nouvelle au fonctionnement du service comptable public ne peut être mise à la charge d'un office sur le fondement du présent article. Aucune rémunération de substitution n'est exigible pour le seul exercice des missions comptables obligatoires. Aucun conventionnement ou justificatif d'exonération nouveau n'est requis pour constater cette suppression.",
"Les créances légalement nées de prestations et exercices antérieurs, leurs exonérations totales ou partielles, les conventions valablement conclues et les rémunérations ou indemnités de gestion déjà acquises restent régis par les règles qui leur étaient applicables, avec leurs recours et prescriptions. Les exonérations attachées à la mise à disposition gratuite de personnels restent prises en compte lors de la liquidation de ces seules créances anciennes. Les indemnités légalement dues aux personnels demeurent à la charge de l'Etat ; leur montant n'est pas recalculé ni supprimé par cette abrogation. Les prestations facultatives distinctes valablement convenues demeurent exécutées dans leur champ ; aucun contrat de substitution n'est imposé.",
"Abrogation du prélèvement et du dispositif exclusivement rattachés à la comptabilité publique, fermée depuis 2021. Aucune recette de compensation ni règle nouvelle de rémunération des agents n'est inventée. Les sommes anciennes et leurs exonérations restent liquidables sans reconstituer une contribution future.",
"La suppression du prélèvement entier rend inutile une exonération pour l'avenir sans taxe équivalente de remplacement. Toutes les exonérations totales ou partielles des créances antérieures subsistent, comme les indemnités déjà acquises et les conventions de prestations facultatives valables ; aucune reprise des avantages anciens n'est autorisée.",
"L421-17 et l'article 88 ELAN ferment la comptabilité publique des OPH à compter de 2021. Les arrêtés tarifaires et indemnitaires ne sont pas réputés réécrits ; ils restent pertinents uniquement pour les droits anciens dans ce champ. Aucun montant d'économie actuelle n'est revendiqué.")

repeal('R423-24',
"Le rapport, l'approbation et la transmission propres au régime public ne sont plus imposés aux exercices nouveaux. Les comptes de ces exercices sont approuvés et transmis selon l'article L. 421-21 et l'article R. 423-28, sans rapport ou envoi supplémentaire fondé sur le présent article.",
"Les comptes publics anciens qui doivent encore être clôturés ou contrôlés, les documents valablement approuvés et les preuves des transmissions effectuées restent conservés. Aucun rapport d'activité ancien définitivement clos n'est refait. Le renvoi à l'article L. 421-14, abrogé depuis le 1er janvier 2015, ne peut fonder ni une sanction nouvelle ni la restauration d'un pouvoir de sanction supprimé ; les contrôles et recours disposant d'un fondement autonome demeurent.",
"Suppression du circuit public concurrent, de son rapport propre et de son renvoi à une sanction législative abrogée. L'approbation des comptes et la transmission légale du régime actuel ne sont pas supprimées.",
"Les actes et transmissions déjà valables restent acquis, sans répétition d'un rapport pour les conserver. La suppression du renvoi à une sanction abrogée ne retire aucune protection des locataires ou aucun contrôle disposant d'une base légale actuelle.")

add('R423-25',[
"Le conseil d'administration vote le budget de l'office.",
"I. – Lorsque les crédits d'un chapitre limitatif dans les conditions du 4° de l'article L. 421-21 sont insuffisants pour les dépenses à engager, le conseil vote une décision modificative. Celle-ci respecte la procédure d'adoption applicable au budget, mais ne reproduit que les tableaux modifiés et les éléments nécessaires pour en apprécier les effets. Les documents inchangés du budget initial sont réutilisés.",
"Les crédits supplémentaires sont financés par des recettes nouvelles, une diminution de crédits disponibles d'un autre chapitre ou un prélèvement sur le fonds de roulement disponible.",
"II. – L'exécution du budget est suivie régulièrement en comparant les recettes et dépenses aux prévisions. Les données et états comptables existants peuvent tenir lieu d'états comparatifs lorsqu'ils permettent cette lecture ; aucune saisie ou présentation distincte n'est exigée. Le conseil reçoit au moins une fois par an une information sur l'exécution, qui peut être intégrée à une séance et à un dossier budgétaires déjà prévus.",
"Si le suivi fait apparaître un bouleversement de l'économie générale du budget, une décision modificative rétablissant l'équilibre est présentée au conseil dans le mois.",
"L'économie générale est notamment bouleversée dans les cas suivants :",
"a) La prévision actualisée de capacité d'autofinancement est inférieure à la dernière prévision approuvée dans les proportions fixées par arrêté conjoint des ministres chargés du logement, des finances et des collectivités territoriales ;",
"b) La prévision actualisée du prélèvement sur le fonds de roulement dépasse le fonds de roulement disponible défini par les instructions mentionnées au premier alinéa de l'article R. 423-7, ou dépasse la dernière prévision approuvée dans la proportion fixée par le même arrêté.",
"Les règles légales de compétence, de transmission au préfet et d'intervention de la chambre régionale des comptes sont inchangées. Aucun dossier budgétaire complet de remplacement ne peut être exigé du seul fait de la modification d'un élément."
],"Suppression de la reproduction du budget primitif entier pour chaque décision modificative et des états comparatifs ressaisis. Maintien du vote, des sources de financement, de l'alerte dans le mois, des critères de bouleversement et du caractère limitatif seulement dans les cas légaux.",
"L'office conserve toutes les sources de financement admises et le caractère évaluatif du budget hors règlement préfectoral. Les données existantes et les réunions déjà prévues servent à l'information ; aucun contrôle de remplacement ou accord ministériel nouveau n'est introduit.",
["Reconstitution de la forme intégrale du budget primitif pour une décision ne modifiant que certains éléments.","Etats comparatifs distincts et nouvelle saisie lorsque les données existantes permettent déjà le suivi et l'information annuelle."],
"L421-21 courant et sa proposition existante lus en entier ; CGCT L1612-2, L1612-5 et L1612-8 actuels lus dans le fonds officiel consolidé externe. Aucune modification des taux d'alerte fixés par arrêté ni des délais légaux n'est proposée.")

repeal('R423-26',
"Le dispositif réglementaire redondant de saisine pour déficit et les seuils de 10 % et de 5 % figurant au présent article cessent d'être applicables. La constatation et le traitement d'un déficit demeurent soumis au 8° de l'article L. 421-21 : la présente abrogation ne crée ni nouveau seuil, ni dispense contraire à cette disposition législative, ni contrôle de remplacement.",
"Les protocoles de prévention, de consolidation et d'aide au rétablissement de l'équilibre et les aides de l'article L. 452-1 demeurent accessibles aux situations futures éligibles. Les droits issus des protocoles valablement conclus, les actes régulièrement accomplis et les recours sur les exercices antérieurs sont préservés.",
"Suppression d'un doublon qui assortissait encore la saisine de seuils alors que L421-21 8° actuel vise le déficit après vérification de sincérité sans ces seuils. La norme législative n'est pas modifiée ni présentée comme créée ici ; aucune économie tirée d'une prétendue suppression du contrôle légal n'est revendiquée.",
"Les aides et protocoles CGLLS ne sont ni supprimés ni conditionnés à un nouveau ratio. Les seuils réglementaires ne peuvent être présentés comme une dispense légale opposable à L421-21 8° ; la suppression du doublon laisse les compétences et garanties légales dans leur champ propre.",
"Discordance source expressément traitée : L421-21 8° en vigueur depuis 2021 dit « un déficit », avec délai d'un mois après saisine. Le paquet ne prétend pas étendre lui-même le contrôle à tout déficit ; c'est la règle supérieure déjà applicable. R423-18 traite séparément l'ancien régime public.")

repeal('R423-27',
"Le défaut de désignation d'un commissaire aux comptes ne peut plus être qualifié ni sanctionné sur le fondement du renvoi du présent article à l'article L. 421-14, abrogé depuis le 1er janvier 2015.",
"L'obligation de désigner un commissaire aux comptes, la certification et les pouvoirs de contrôle ou de sanction disposant d'un fondement légal autonome restent applicables. Aucun régime de sanction de remplacement n'est créé. Les droits de recours et l'application des règles plus favorables aux sanctions non définitivement prononcées sont préservés, sans remise en cause des décisions définitives par la seule présente abrogation.",
"Abrogation d'une qualification réglementaire renvoyant à un pouvoir législatif supprimé. Le contrôle des comptes reste dû ; le projet n'invente ni nouveau manquement ni nouvelle sanction pour remplacer le renvoi obsolète.",
"Les personnes contrôlées conservent leurs recours et le bénéfice des règles répressives plus douces lorsqu'elles sont applicables. La suppression du renvoi obsolète n'autorise pas l'office à priver les locataires ou créanciers de la certification légalement requise.",
"L421-14 dernier texte et statut ABROGE au 1er janvier 2015 lus intégralement. Ne pas substituer sans examen un renvoi automatique à une autre sanction du contrôle ANCOLS ; aucun tel remplacement n'est opéré.")

add('R423-28',[
"Pour chaque exercice, le directeur général établit le compte financier et le transmet au commissaire aux comptes au plus tard le 15 mai de l'année suivante.",
"Le compte certifié est présenté au conseil d'administration avec les informations nécessaires à son approbation, notamment celles prévues à l'article R. 423-9. Ces informations sont reprises des documents disponibles et peuvent être intégrées au dossier des comptes. Aucun rapport d'activité matériellement distinct du directeur général n'est exigé sur le seul fondement du présent article ; les rapports dus sur un fondement autonome ne sont pas supprimés et peuvent être réutilisés.",
"Après avoir approuvé les documents au plus tard le 30 juin, le conseil décide de l'affectation du résultat.",
"Le compte financier et les informations qui l'accompagnent sont déposés une seule fois sur la plate-forme sécurisée désignée par arrêté du ministre chargé du logement. Ce dépôt les rend accessibles au préfet et au ministre chargé du logement ; aucun second envoi identique à ces destinataires n'est demandé. Il intervient dans les quinze jours de l'approbation, conformément à l'article L. 421-21, et au plus tard le 15 juillet de l'année suivant l'exercice.",
"Le renvoi antérieur à l'article L. 421-14, abrogé depuis le 1er janvier 2015, ne fonde aucune sanction nouvelle. L'obligation légale de transmission et les contrôles et recours autonomes subsistent ; aucun état ou déclaration de remplacement n'est ajouté."
],"Suppression du rapport d'activité autonome du directeur général, des doubles envois identiques et du renvoi à une sanction abrogée. Compte certifié, information substantielle du conseil, affectation et calendrier restent dus. Le délai légal de quinze jours après approbation est coordonné avec la borne réglementaire du 15 juillet.",
"Le dossier existant suffit sans rapport ou copie supplémentaires ; les rapports autonomes peuvent servir sans être refaits. Les droits des locataires et des tiers à des comptes sincères et certifiés, ainsi que les délais légaux, ne sont ni supprimés ni remplacés par une déclaration nouvelle.",
["Rapport d'activité du directeur général matériellement distinct sur le seul fondement de cet article.","Double transmission identique du même dossier au préfet et au ministre après dépôt sécurisé unique.","Renvoi de sanction à L421-14 abrogé depuis 2015."],
"R421-17 conserve le rapport du président sur la politique de l'office : il peut être réutilisé, pas abrogé implicitement. L421-21 6° dit avant le 30 juin tandis que 7° dit au plus tard le 30 juin : discordance préexistante signalée, le texte réglementaire ne proroge aucun délai légal plus court.")

add('R423-29',[
"Le plan de comptes applicable aux offices publics de l'habitat à comptabilité commerciale est fixé par des instructions homologuées par arrêté conjoint des ministres chargés du logement, des finances et des collectivités territoriales, après avis de l'Autorité des normes comptables.",
"Ces instructions respectent les règles relatives au cadre comptable et à la tenue des comptes fixées par l'Autorité des normes comptables. Elles n'imposent ni un second jeu de comptes de même objet ni la reproduction des informations déjà présentes dans les comptes et annexes réglementairement requis."
],"Maintien du plan commun qui rend comparables les comptes des offices et permet leur contrôle, tout en interdisant un second jeu identique. La réforme n'ajoute pas de modèle individuel à homologuer et n'efface pas les normes de sincérité.",
"Les offices conservent un cadre commun plutôt que des autorisations individuelles de plan comptable. La dispense de seconde copie et de second jeu de comptes bénéficie aux exercices futurs sans retirer une aide ou faculté financière existante.",
["Second jeu de comptes ou reproduction d'informations de même objet déjà présentes dans les comptes et annexes réglementairement requis."],
"Note DILA de 2014 lue. Les instructions et leur contenu ne sont pas réputés réécrits dans ce paquet ; leurs prescriptions de doublons devront être alignées sur la dispense nouvelle, sans changement des règles ANC.")

add('R423-30',[
"Le compte financier mentionné à l'article R. 423-28 comprend le bilan, le compte de résultat et les annexes déterminées par les instructions homologuées mentionnées à l'article R. 423-29, dans le respect des normes comptables applicables.",
"Ces instructions précisent la nature, le format et le contenu des documents transmis par voie dématérialisée. Le dépôt reprend les documents et données déjà établis : aucune annexe de même objet, nouvelle saisie ou version supplémentaire n'est exigée lorsqu'ils satisfont déjà aux prescriptions applicables. Les données doivent rester lisibles, complètes et contrôlables ; cette dispense ne permet d'omettre aucune annexe comptable obligatoire."
],"Suppression des versions, saisies et annexes redondantes de la transmission dématérialisée, sans remplacer le compte complet par un résumé. Bilan, résultat et annexes obligatoires restent présents et contrôlables.",
"Les offices peuvent réutiliser directement leurs comptes réglementaires pour le dépôt et ne produisent pas un nouveau dossier pour le même objet. Cette faculté demeure ouverte aux exercices futurs sans supprimer les informations nécessaires aux locataires, tiers et organismes d'aide.",
["Annexe de même objet, nouvelle saisie ou version supplémentaire lorsque les documents déjà établis satisfont aux prescriptions du dépôt."],
"Coordination avec R423-28 : dépôt unique, pas de second rapport d'activité. Aucun tableau source ni contenu comptable obligatoire n'est supprimé au prétexte de l'allègement du format.")

A=[]
for s in S:
 n=s['number'];a={k:s[k] for k in ('code_id','source_id','number','source_sha256')};a.update(status='rewrite_draft',**D[n]);a['review_notes']+=(' Note DILA entière conservée dans la source ; son application historique n’est pas réactivée.' if s['source_notes_xml'].strip() else ' Note DILA de la source vide.');a['review_notes']+=' Avant-projet sans validation juridique revendiquée ; aucune modification de la source canonique.';A.append(a)
t=P/'answer.tmp';t.write_text(json.dumps(A,ensure_ascii=False,indent=2)+'\n');t.replace(P/'answer.json')
print(len(A),hashlib.sha256((P/'answer.json').read_bytes()).hexdigest())
