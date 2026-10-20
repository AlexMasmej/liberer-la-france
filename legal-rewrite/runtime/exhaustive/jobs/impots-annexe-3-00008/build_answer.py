import json
from pathlib import Path


drafts = [
    (
        '41 duodecies',
        """<p>Les représentants de la personne morale émettrice certifient et signent la déclaration estimative prévue au deuxième alinéa de l’article 41 nonies.</p>""",
        "Réécriture à droit constant : les représentants de la personne morale deviennent le sujet explicite des deux obligations de certification et de signature. Le renvoi vise toujours le deuxième alinéa de l’article 41 nonies. Aucune réforme de fond.",
        "Le deuxième alinéa de l’article 41 nonies a été vérifié dans le corpus : il concerne la déclaration estimative en l’absence de stipulation d’intérêts. Les deux formalités restent cumulatives et incombent aux représentants de l’émetteur.",
    ),
    (
        '41 duodecies A',
        """<p>Les personnes, sociétés et organismes définis à l’article 75 de l’annexe II au code général des impôts sont dénommés ci-après « établissements payeurs ». Lorsqu’ils versent, à quelque titre que ce soit, des intérêts, arrérages ou autres produits visés au I de l’article 125 A du même code, ils respectent les articles 41 duodecies B à 41 duodecies G et 381 S.</p>""",
        "Réécriture à droit constant : la définition des établissements payeurs est séparée, dans le même alinéa, de l’obligation qui leur incombe lors du paiement. Les catégories de produits et les renvois sont conservés. Aucune réforme de fond.",
        "L’article 75 de l’annexe II et l’article 381 S ont été vérifiés dans le corpus. Le renvoi à l’article 381 S conserve notamment ses exclusions propres aux prélèvements relevant de l’article 125 D. La simplification administrative du projet ne justifie ici aucune dispense nouvelle ni suppression de pièce non identifiée comme doublon.",
    ),
    (
        '41 duodecies B',
        """<p>Les établissements payeurs exigent des bénéficiaires des revenus, des présentateurs ou des vendeurs de coupons qu’ils justifient de leur identité et de leur domicile réel ou de leur siège social, dans les conditions prévues à l’article 76 de l’annexe II au code général des impôts.</p>
<p>Toutefois, cette justification n’est pas requise pour les revenus soumis au prélèvement prévu à l’article 125 A du même code, à l’exception des produits d’obligations.</p>""",
        "Réécriture à droit constant : l’obligation de demander les justificatifs est formulée directement et l’exception est exprimée en distinguant les produits d’obligations. Les deux alinéas sont maintenus. Aucune réforme de fond.",
        "L’article 76 de l’annexe II a été vérifié : ses modalités et sa faculté de dispense sous la responsabilité de l’établissement restent applicables par renvoi. L’exception du second alinéa ne dispense pas les produits d’obligations de justification. Aucune autorisation nouvelle de réemploi ou d’échange de données n’est créée.",
    ),
    (
        '41 duodecies C',
        """<p>Sous réserve des conventions internationales, l’établissement payeur effectue le prélèvement prévu au III de l’article 125 A du code général des impôts lorsque le domicile réel ou le siège social du bénéficiaire des revenus se situe hors de la France métropolitaine et des départements d’outre-mer.</p>
<p>Ce prélèvement ne s’applique toutefois pas :</p>
<p>1° (Abrogé) ;</p>
<p>1° bis (Abrogé) ;</p>
<p>2° Aux intérêts des dépôts en devises effectués auprès d’établissements de crédit installés en France ;</p>
<p>3° Aux revenus des opérations de trésorerie à court terme réalisées entre, d’une part, des établissements de crédit ou des sociétés de financement installés en France et, d’autre part, des banques établies à l’étranger, des organismes internationaux ou des institutions financières publiques étrangères ;</p>
<p>4° Aux intérêts provenant d’opérations à court terme que les banques établies à l’étranger perçoivent à raison des effets représentatifs de créances hypothécaires qu’elles détiennent et qui sont susceptibles d’être acquis par le crédit foncier de France ;</p>
<p>5° Aux intérêts des comptes étrangers en euros ouverts auprès d’établissements de crédit établis en France par des personnes dont le domicile fiscal ou le siège social se situe hors de France.</p>""",
        "Réécriture à droit constant du texte fourni : la réserve conventionnelle et l’obligation de l’établissement payeur sont placées en tête ; les deux groupes de contreparties du 3° et les conditions cumulatives du 4° sont rendus plus lisibles. Les numéros, y compris les deux mentions d’abrogation, restent en place. Aucune réforme de fond.",
        "Décalage préexistant à coordonner avec le III de l’article 125 A vérifié dans le corpus : ce III vise les paiements dans certains États ou territoires non coopératifs, comporte une clause de sauvegarde et s’applique indépendamment du domicile du bénéficiaire, tandis que le présent article conserve un critère de domicile hors métropole et départements d’outre-mer. Ce décalage est signalé sans réécrire silencieusement le champ. Les numéros 1°, 1° bis et 2° à 5° sont maintenus ; les quatre exceptions actives sont les 2° à 5°.",
    ),
    (
        '41 duodecies D',
        """<p>Lorsque les revenus sont soumis au prélèvement en application du II de l’article 125 A du code général des impôts, leur débiteur effectue lui-même ce prélèvement, même s’il ne paie pas personnellement les produits concernés.</p>""",
        "Réécriture à droit constant : la condition d’application est distinguée de l’obligation personnelle du débiteur. L’absence de paiement direct ne le décharge pas du prélèvement. Aucune réforme de fond.",
        "Le II de l’article 125 A vérifié dans le corpus concerne le mécanisme solidaire de versement automatique des revenus d’épargne à un organisme bénéficiaire. Le renvoi au seul II et la responsabilité du débiteur sont conservés ; le texte n’est pas étendu aux autres prélèvements.",
    ),
    (
        '41 duodecies E',
        """<p>En dehors des cas prévus aux articles 41 duodecies C et 41 duodecies D, l’établissement payeur n’effectue le prélèvement que si le bénéficiaire des revenus a opté pour son assujettissement à ce prélèvement, dans les conditions prévues aux I et IV de l’article 125 A du code général des impôts.</p>
<p>Le bénéficiaire exerce cette option au plus tard lors de l’encaissement des revenus. L’option est irrévocable.</p>""",
        "Réécriture à droit constant du texte fourni : l’établissement payeur et le bénéficiaire sont expressément désignés pour leurs actes respectifs ; le délai et l’irrévocabilité sont énoncés en deux phrases dans le second alinéa. Aucune réforme de fond.",
        "Incohérence préexistante : les I et IV actuels de l’article 125 A, vérifiés dans le corpus, ne prévoient plus l’option décrite ici. Le I organise un prélèvement obligatoire avec possibilité de dispense sous conditions et le IV exclut certains intérêts et revenus exonérés. Une coordination du régime d’option est nécessaire avec les articles 41 duodecies H, L et M ; elle n’est pas remplacée ici par une réforme fiscale non définie dans policy.json. L’échéance à l’encaissement et l’irrévocabilité du texte source sont conservées.",
    ),
    (
        '41 duodecies F',
        """<p>Le prélèvement appliqué aux produits des bons de caisse émis par les établissements de crédit se substitue, pour ces produits, à la retenue à la source prévue au I de l’article 1678 bis du code général des impôts.</p>""",
        "Réécriture à droit constant : la substitution du prélèvement à la retenue est formulée directement, dans le seul cas des bons de caisse émis par les établissements de crédit. Aucune réforme de fond.",
        "L’article 1678 bis vérifié dans le corpus est subdivisé en 1, 2 et 3, alors que la source renvoie à un I : cette discordance de subdivision est conservée et signalée. Son 1 mentionne la retenue de l’article 119 bis et le prélèvement de l’article 125 A ; leur articulation avec la substitution propre au présent article doit être contrôlée. Aucune exonération ni substitution pour les autres émetteurs de bons de caisse n’est créée.",
    ),
    (
        '41 duodecies G',
        """<p>Les sociétés mentionnées au 4° de l’article 75 de l’annexe II au code général des impôts sont réputées verser à chaque associé la quote-part des revenus correspondant à ses droits le jour où elles encaissent ces revenus ou sont créditées de leur montant.</p>
<p>À cette même date, elles effectuent le prélèvement prévu à l’article 41 duodecies C sur la quote-part revenant aux associés dont le domicile réel ou le siège social se situe hors de la France métropolitaine et des départements d’outre-mer.</p>
<p>Le présent article ne s’applique pas aux sociétés qui exercent une activité industrielle, commerciale, artisanale ou agricole, ou une profession non commerciale.</p>""",
        "Réécriture à droit constant : la date du versement réputé et celle du prélèvement sont reliées explicitement, puis les activités exclues sont conservées dans le troisième alinéa. Aucune réforme de fond.",
        "Le 4° de l’article 75 de l’annexe II a été vérifié : il vise les sociétés de l’article 8 pour les revenus définis au 4 de l’article 79 de cette annexe. La fiction de versement reste liée à l’encaissement ou au crédit et non au paiement effectif à l’associé. La difficulté de champ signalée à l’article 41 duodecies C se répercute sur le deuxième alinéa ; les exclusions du troisième alinéa restent entières.",
    ),
    (
        '41 duodecies H',
        """<p>1. Pour l’application de l’article 125 A du code général des impôts, les obligations émises en France par des organismes étrangers ou internationaux sont assimilées à des obligations françaises.</p>
<p>2. L’article 125 A du même code ne s’applique pas aux obligations que les entreprises françaises ont été autorisées à émettre à l’étranger dans les conditions prévues à l’article 131 ter de ce code.</p>
<p>3. Pour les obligations françaises comme pour les obligations étrangères, l’option prévue au I de l’article 125 A du même code ne peut être exercée que si l’emprunt ne comporte aucune clause d’indexation.</p>""",
        "Réécriture à droit constant du texte fourni : l’article auquel se rapporte le 2 est nommé expressément et la condition d’absence d’indexation du 3 est formulée directement. Les trois subdivisions et leurs champs respectifs sont maintenus. Aucune réforme de fond.",
        "Au 2, « cet article » est explicité comme visant l’article 125 A, conformément à l’enchaînement du texte source. Deux décalages préexistants sont à coordonner : le 3 renvoie à une option absente du I actuel de l’article 125 A ; le 1 ne reprend pas l’autorisation ministérielle mentionnée au 2 de l’article 131 ter pour l’assimilation des émissions en France. Le 1 de l’article 131 ter réserve le régime des émissions françaises à l’étranger aux séries émises avant le 1er janvier 1976, pour toute leur durée ; le renvoi du 2 ne crée pas d’ouverture aux nouvelles émissions.",
    ),
    (
        '41 duodecies J',
        """<p>Le prélèvement prévu à l’article 125 A du code général des impôts et dû sur les gains mentionnés à l’article 124 B du même code est opéré sur le compte que le contribuable approvisionne à cette fin. Il est effectué par la personne auprès de laquelle les titres de créances sont inscrits en compte ou déposés en application du premier alinéa de l’article 124 D du même code, ou par la personne désignée par le contribuable pour acquitter ce prélèvement.</p>
<p>Le présent article ne s’applique pas au prélèvement dû sur les gains mentionnés au I de l’article 125 D du même code.</p>""",
        "Réécriture à droit constant : la règle relative au compte à approvisionner est séparée de la désignation des personnes qui effectuent le prélèvement, dans le même premier alinéa. L’exclusion du second alinéa et tous les renvois sont conservés. Aucune réforme de fond.",
        "Les articles 124 B, 124 D et 125 D ont été vérifiés dans le corpus. Le contribuable reste chargé d’approvisionner le compte et peut désigner une personne pour acquitter le prélèvement. L’exclusion vise seulement le I de l’article 125 D et les gains mentionnés par la source, sans alignement sur l’exclusion plus large de l’article 41 duodecies L. Les graphies fautives de « prélèvement » et d’« impôts » sont rectifiées sans changement de droit.",
    ),
    (
        '41 duodecies K',
        """<p>Pour l’application de l’article 125 A du code général des impôts aux gains mentionnés à l’article 41 duodecies J, la cession des titres produit les effets d’un paiement à la date de cette cession.</p>""",
        "Réécriture à droit constant : la fiction de paiement est exprimée par ses effets et sa date, sans modifier son fait générateur ni ses renvois. Aucune réforme de fond.",
        "Le caractère parasite « s » placé après « impôts » dans la source a été supprimé comme erreur matérielle, sans incidence normative. Le paiement est réputé intervenir au jour de la cession pour l’application de l’article 125 A aux seuls gains visés par le renvoi à l’article 41 duodecies J.",
    ),
    (
        '41 duodecies L',
        """<p>Le cédant exerce l’option pour le prélèvement auprès des personnes mentionnées à l’article 41 duodecies J lorsqu’il leur communique le montant de la cession effectuée, et au plus tard dix jours à compter de la date de cette cession. Il indique alors le montant du gain pour lequel il exerce l’option.</p>
<p>Le présent article ne s’applique pas au prélèvement dû sur les revenus, produits et gains mentionnés aux I et II de l’article 125 D du code général des impôts.</p>""",
        "Réécriture à droit constant du texte fourni : le cédant devient le sujet de l’exercice de l’option et de l’indication du gain. Le moment de la communication et le délai maximal de dix jours sont distingués, sans déplacer le second alinéa d’exclusion. Aucune réforme de fond.",
        "Le délai demeure de dix jours à compter de la cession, sans ajout d’une règle de jours ouvrés ni modification de son point de départ. L’exclusion vise les I et II de l’article 125 D, contrairement à celle du J limitée au I. Le mécanisme d’option doit être coordonné avec le régime actuel de l’article 125 A, dont le I ne prévoit plus cette option ; cette incohérence du dispositif source n’est pas corrigée silencieusement.",
    ),
    (
        '41 duodecies M',
        """<p>Par dérogation aux articles 41 duodecies J et 41 duodecies L, lorsque les gains sont réalisés par l’intermédiaire d’une société mentionnée à l’article 8 du code général des impôts, cette société effectue le prélèvement prévu à l’article 125 A du même code. L’option est exercée auprès d’elle dans les conditions prévues à l’article 41 duodecies G, sous réserve du délai mentionné à l’article 41 duodecies L.</p>""",
        "Réécriture à droit constant du texte fourni : les deux fonctions de la société, effectuer le prélèvement et recevoir l’option, sont énoncées dans deux phrases du même alinéa. La dérogation, les conditions et la réserve de délai sont intégralement conservées. Aucune réforme de fond.",
        "Le renvoi à l’article 8 du CGI et les renvois internes aux articles J, G et L sont maintenus. Difficultés préexistantes : l’article G ne décrit pas lui-même de procédure d’option et le I actuel de l’article 125 A ne prévoit plus l’option ancienne ; l’articulation de ces textes doit être coordonnée. Le renvoi au L reste limité à la réserve de délai formulée par la source ; la portée de son second alinéa doit être articulée avec ce régime dérogatoire.",
    ),
    (
        '41 duodecies N',
        """<p>Le contribuable qui demande à bénéficier du report de pertes subies au cours des cinq années antérieures joint à sa déclaration d’impôt sur le revenu une note détaillant, pour chaque année, les pertes reportées.</p>""",
        "Réécriture à droit constant : l’obligation de joindre la note est formulée directement et son contenu annuel est explicité. La période de cinq années et le support déclaratif sont conservés. Aucune réforme de fond.",
        "La note reste une annexe à la déclaration d’impôt sur le revenu ; elle n’est pas remplacée par une simple mise à disposition. Cet article fixe une obligation justificative et ne crée pas un droit autonome à reporter toute catégorie de pertes. Aucun doublon administratif précis n’étant établi par les sources, la pièce n’est pas supprimée au titre du projet de simplification.",
    ),
    (
        '41 duodecies O',
        """<p>Les personnes et les gains mentionnés aux articles 41 duodecies J et 41 duodecies M relèvent des dispositions du 1 de l’article 242 ter du code général des impôts et de l’article 41 duodecies A.</p>""",
        "Réécriture à droit constant : le champ des personnes et des gains est placé en sujet, puis les deux ensembles de dispositions applicables sont désignés. Les références exactes sont conservées. Aucune réforme de fond.",
        "Le 1 de l’article 242 ter a été vérifié dans le corpus : le renvoi maintient ses obligations déclaratives et ses exceptions. Il n’est pas étendu à l’ensemble de cet article. La chaîne de renvois via l’article 41 duodecies A, notamment vers l’article 381 S, reste applicable dans ses propres limites.",
    ),
    (
        '41 duodecies P',
        """<p>Les personnes mentionnées aux articles 41 duodecies J et 41 duodecies M tiennent à la disposition de l’administration un document qui précise, pour chaque cession :</p>
<p>La date à laquelle le gain a été réalisé et son montant ;</p>
<p>Le montant du prélèvement effectué ou, à défaut de prélèvement, l’identité et le domicile réel du bénéficiaire des gains.</p>""",
        "Réécriture à droit constant : l’obligation de tenir le document à disposition et l’alternative entre prélèvement et identification sont formulées directement. Les trois alinéas et le détail par cession sont conservés. Aucune réforme de fond.",
        "L’identité et le domicile réel sont exigés à défaut de prélèvement, sans les substituer à l’indication du gain et de sa date, qui reste requise dans tous les cas. La source prévoit une mise à disposition et non un dépôt spontané ; aucune durée de conservation supplémentaire n’est inventée.",
    ),
    (
        '41 terdecies',
        """<p>Les sociétés, compagnies ou entreprises françaises qui envisagent d’émettre à l’étranger des séries spéciales d’obligations et souhaitent bénéficier du régime fiscal prévu au 1 de l’article 131 ter du code général des impôts déposent préalablement une demande spéciale auprès de la direction générale des finances publiques.</p>
<p>La demande précise la date et les conditions de l’émission, ainsi que le nombre, le montant et les numéros des titres à émettre.</p>""",
        "Réécriture à droit constant du texte fourni : les demandeurs deviennent le sujet de l’obligation de dépôt préalable et les renseignements exigés sont énoncés dans un second alinéa conservé. Aucune réforme de fond.",
        "Décalage historique préexistant : le 1 de l’article 131 ter, vérifié dans le corpus avec ses notes, limite le régime aux séries émises à l’étranger avant le 1er janvier 1976, pour toute leur durée, alors que le présent article conserve une formulation prospective. Le renvoi ne saurait ouvrir ce régime à de nouvelles émissions ; la coordination historique est à expliciter dans le dispositif d’ensemble, sans élargissement silencieux. La demande spéciale, son destinataire et tous ses renseignements sont maintenus.",
    ),
    (
        '41 quaterdecies',
        """<p>Le directeur général des finances publiques accorde l’autorisation.</p>""",
        "Réécriture à droit constant : la phrase passive est remplacée par une phrase active qui désigne directement l’autorité compétente. Aucune condition d’octroi ni réforme de fond n’est ajoutée.",
        "Discordance terminologique préexistante à contrôler dans la chaîne d’autorisation : le présent article désigne le directeur général des finances publiques, tandis que le 1 de l’article 131 ter vise l’autorisation du ministre de l’économie et des finances et l’article 41 quindecies une autorisation ministérielle. Les compétences ou délégations correspondantes ne sont pas modifiées par cette réécriture.",
    ),
    (
        '41 quindecies',
        """<p>Les séries émises avant la publication au Journal officiel du décret n° 55-486 du 30 avril 1955 peuvent bénéficier d’une autorisation sur présentation d’une demande conforme à celle prévue à l’article 41 terdecies. Les effets de cette autorisation s’appliquent aux intérêts échus depuis la date d’entrée en vigueur de ce décret.</p>
<p>Sous réserve du premier alinéa, le régime institué par le 1 de l’article 131 ter du code général des impôts ne s’applique à une émission qu’à compter de la notification de l’autorisation ministérielle.</p>""",
        "Réécriture à droit constant : la possibilité d’autorisation et ses effets sur les intérêts échus sont séparés en deux phrases dans le premier alinéa. Le second conserve la règle générale de prise d’effet à la notification et sa réserve historique. Aucune réforme de fond.",
        "Les trois repères sont distincts : émission antérieure à la publication du décret, intérêts échus depuis son entrée en vigueur, et prise d’effet ordinaire à la notification. Le 30 avril 1955 est la date du décret, sans être présenté comme sa date de publication ou d’entrée en vigueur. La limite des émissions antérieures au 1er janvier 1976 découle du 1 de l’article 131 ter. La qualification ministérielle de l’autorisation reste à articuler avec l’autorité désignée à l’article 41 quaterdecies ; elle est conservée.",
    ),
    (
        '41 sexdecies',
        """<p>Les titres émis à l’étranger doivent tous porter la mention suivante :</p>
<p>" En application du décret français n° 55-486 du 30 avril 1955 (code général des impôts, art. 131 ter-1), la présente obligation est soumise en France au régime fiscal des valeurs mobilières étrangères (décision du directeur général des finances publiques en date du..) ".</p>""",
        "Réécriture à droit constant de l’obligation introductive : son caractère obligatoire et uniforme est exprimé au présent. Le libellé de la mention imposée aux titres est conservé intégralement, car le modifier changerait la formalité prescrite. Aucune réforme de fond.",
        "Le numéro 55-486, la date du 30 avril 1955, la référence 131 ter-1 et la désignation du directeur général des finances publiques sont maintenus dans la formule. Le blanc « en date du.. » reste un emplacement à compléter sur le titre, sans date inventée. Le régime est celui du 1 de l’article 131 ter, limité aux séries historiques antérieures au 1er janvier 1976, et non celui de futures émissions nouvelles.",
    ),
    (
        '41 sexdecies A',
        """<p>Le gérant dépose une déclaration d’existence du fonds et un exemplaire de son règlement auprès de la direction départementale ou, le cas échéant, régionale des finances publiques dans le ressort de laquelle il souscrit sa déclaration de résultats. Il effectue ce dépôt dans le mois de l’agrément délivré par l’Autorité des marchés financiers prévu à l’article L. 214-3 du code monétaire et financier ou, pour les fonds non soumis à cet agrément, dans le mois de la déclaration faite à cette autorité.</p>
<p>Le gérant d’un fonds commun de placement informe cette même direction de la transformation, de la fusion, de la scission ou de la liquidation du fonds prévues à l’article L. 214-3 du code monétaire et financier, dans le délai mentionné au premier alinéa.</p>""",
        "Réécriture à droit constant : l’obligation de dépôt, les deux pièces et le service destinataire sont énoncés avant les deux événements faisant courir le délai. Le second alinéa conserve les quatre événements à notifier et son renvoi au délai du premier. Aucune réforme de fond.",
        "Le délai d’un mois est conservé comme tel, sans le convertir en trente jours. Le service reste celui du ressort de la déclaration de résultats du gérant. Le renvoi à l’article L. 214-3 doit être contrôlé dans le code monétaire et financier, non fourni parmi les sources assignées. Le futur compte personnel investi collectivement, prévu par la coordination du CSS L. 241-3 proposé, n’est pas assimilé automatiquement à un fonds commun de placement. Son éventuel raccordement à un tel véhicule appelle des dispositions spécifiques du code monétaire et financier sur son statut, son gestionnaire et la séparation de ses actifs, ainsi que des coordinations fiscales dans le CGI ; aucun numéro de disposition nouvelle n’est inventé.",
    ),
    (
        '41 sexdecies C',
        """<p>Le gérant d’un fonds commun de placement dépose auprès de la direction départementale ou, le cas échéant, régionale des finances publiques désignée au premier alinéa de l’article 41 sexdecies A un état sur papier libre. Il le dépose dans les trente jours de la date de mise en distribution des produits des actifs compris dans le fonds, et au plus tard dans les trente jours suivant l’expiration du délai de cinq mois prévu à l’article L. 214-17-2 du code monétaire et financier. Cet état indique :</p>
<p>a. Les dates d’ouverture et de clôture de l’exercice dont les produits ont été mis en distribution ;</p>
<p>b. La date de mise en distribution ;</p>
<p>c. Le nombre de parts du fonds commun de placement à la date d’ouverture de l’exercice, à sa date de clôture et à la date de mise en distribution ;</p>
<p>d. Le montant de la répartition effectuée au titre de l’exercice considéré, déterminé conformément au 1° du I de l’article L. 214-17-2 du même code, ainsi que la part de cette répartition éligible à l’abattement de 40 % mentionné au 2° du 3 de l’article 158 du code général des impôts ;</p>
<p>e. Le cas échéant, la date de distribution et le montant de chaque acompte versé au titre du même exercice.</p>""",
        "Réécriture à droit constant : le dépôt, son destinataire et ses deux contraintes de délai sont distingués dans le même alinéa introductif. Le c explicite les trois dates à retenir et les lettres a à e sont conservées. Aucune réforme de fond.",
        "Contrôles de fidélité : trente jours à compter de la mise en distribution, limite de trente jours après le délai de cinq mois, trois dates au c, abattement de 40 % et renvois au 1° du I de l’article L. 214-17-2 et au 2° du 3 de l’article 158 maintenus. La note source a été lue : elle rattache la modification à l’article 77-34° de la loi n° 2019-486 du 22 mai 2019 ; c’est une indication historique, sans date d’entrée en vigueur d’une réforme future. Le renvoi au code monétaire et financier reste à contrôler dans ce code. Le support papier libre est conservé faute de réforme précise de ce dépôt.",
    ),
    (
        '41 sexdecies D',
        """<p>Pour chaque répartition globale unique effectuée par un fonds commun de placement au titre d’un exercice déterminé, le gérant établit un état et le produit à toute demande de l’administration. Cet état mentionne :</p>
<p>1° Le montant des sommes ou valeurs distribuées pour chaque part du fonds et la nature des produits soumis à des règles fiscales différentes qui les composent. Les produits de source étrangère sont, s’il y a lieu, ventilés par État d’origine ;</p>
<p>2° La nature et le montant des produits de l’exercice qui, le cas échéant, n’ont pas été distribués ;</p>
<p>3° Le montant global des crédits d’impôt figurant sur les certificats délivrés au fonds pendant l’exercice, calculé dans l’hypothèse où tous les propriétaires de parts ont en France leur domicile fiscal ou leur siège social.</p>
<p>Ce montant est, s’il y a lieu, ventilé selon la nature des produits encaissés à répartir et leur origine française ou étrangère ;</p>
<p>4° Le montant total des crédits d’impôt calculé dans l’hypothèse où tous les propriétaires de parts ont leur domicile ou leur siège social hors de France et sont placés hors du champ d’application d’une convention internationale en matière d’impôt sur les revenus. Ce montant est, s’il y a lieu, ventilé dans les conditions prévues au 3° ;</p>
<p>5° (Abrogé) ;</p>
<p>6° Pour les crédits d’impôt attachés aux produits encaissés par le fonds commun au cours de l’exercice, la fraction qui n’a pas pu être transférée aux propriétaires de parts.</p>
<p>Cette fraction peut être utilisée au titre des deux exercices annuels qui suivent celui au cours duquel les produits auxquels se rattachent les avoirs fiscaux et crédits d’impôt auraient normalement pu être répartis, compte tenu de leur date d’encaissement ;</p>
<p>7° Le nombre de parts existant effectivement à la date de mise en distribution des produits et donnant droit à cette répartition ainsi qu’à l’utilisation d’une quote-part de la somme imputable prévue soit au 3°, soit au 4° ;</p>
<p>8° Le montant du crédit d’impôt unitaire calculé pour chacune des deux hypothèses prévues respectivement au 3° et au 4°, selon le lieu du domicile fiscal ou du siège social du propriétaire de parts ;</p>
<p>9° La ventilation du crédit d’impôt unitaire selon la nature et l’origine des produits qui composent les sommes ou valeurs réparties.</p>""",
        "Réécriture à droit constant : les obligations d’établir et de produire l’état sont formulées séparément ; les ventilations et les deux hypothèses de calcul sont rendues explicites. Les neuf numéros, la mention d’abrogation du 5° et les alinéas complémentaires des 3° et 6° restent à leur place. Aucune réforme de fond.",
        "Contrôles de fidélité : montants par part au 1°, produits non distribués au 2°, certificats et hypothèse française au 3°, hypothèse hors de France sans convention au 4°, deux exercices annuels au 6°, parts effectivement existantes et quote-part imputable au 7°, double calcul au 8° et ventilation au 9° conservés. Le point de départ du délai du 6° reste l’exercice de répartition normalement possible selon l’encaissement, et non celui du transfert manqué. La référence historique aux avoirs fiscaux est maintenue ; son éventuel champ résiduel et celui des certificats doivent être contrôlés sans suppression automatique des droits anciens.",
    ),
    (
        '41 sexdecies E',
        """<p>I. – Lorsqu’un acompte est distribué, le gérant du fonds commun de placement produit un état dans le mois de cette distribution partielle, comme pour la distribution globale prévue à l’article 41 sexdecies C. Cet état indique le montant et la date de mise en distribution de l’acompte, l’exercice au titre duquel il est versé, le nombre de parts ayant vocation à cette répartition ainsi que la part de l’acompte éligible à l’abattement de 40 % mentionné au 2° du 3 de l’article 158 du code général des impôts.</p>
<p>II. – Pour chaque acompte, le gérant établit un état analogue à celui prévu à l’article 41 sexdecies D. Pour déterminer les différents montants à y mentionner, il ne prend en compte que les produits du fonds compris dans l’acompte et les crédits d’impôt attachés à ces produits.</p>
<p>III. – Lors de la répartition pour solde des produits d’un exercice déterminé, le gérant établit des états analogues à ceux prévus respectivement aux articles 41 sexdecies C et 41 sexdecies D. Ces états récapitulent, d’une part, les éléments afférents aux acomptes déjà versés et présentent, d’autre part, les éléments relatifs au solde.</p>""",
        "Réécriture à droit constant : les renseignements de l’état d’acompte, la limitation de l’assiette documentaire du II et le rapprochement des acomptes avec le solde au III sont explicités. Le gérant est désigné comme sujet des obligations et les trois subdivisions sont maintenues. Aucune réforme de fond.",
        "Le délai du I reste d’un mois ; il n’est pas remplacé par trente jours. Décalage rédactionnel préexistant : le I rapproche ce délai de celui de la distribution globale, alors que l’article 41 sexdecies C fixe trente jours et une limite liée au délai de cinq mois. Une harmonisation éventuelle nécessite une coordination explicite, non opérée ici. Le montant éligible à l’abattement de 40 %, le renvoi au 2° du 3 de l’article 158, le calcul limité aux produits et crédits compris dans chaque acompte, ainsi que la distinction entre récapitulatif des acomptes et solde sont conservés.",
    ),
]


sources = json.loads(Path('source.json').read_text())
assert len(sources) == len(drafts) == 24
answer = []
for source, (number, xml, reason, notes) in zip(sources, drafts):
    assert number == source['number'], (number, source['number'])
    answer.append({
        'code_id': source['code_id'],
        'source_id': source['source_id'],
        'source_sha256': source['source_sha256'],
        'number': source['number'],
        'proposed_xml': xml,
        'reason': reason,
        'review_notes': notes,
        'status': 'rewrite_draft',
    })
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
