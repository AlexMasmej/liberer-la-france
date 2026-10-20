import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
drafts = {}


def add(number, paragraphs, reason, review_notes):
    drafts[number] = {
        'proposed_xml': '\n'.join('<p>' + p + '</p>' for p in paragraphs),
        'reason': reason,
        'review_notes': review_notes,
        'status': 'rewrite_draft',
    }


add('L146-6', [
    "La section des assurances sociales de la chambre disciplinaire des médecins, des chirurgiens-dentistes et des sages-femmes de Nouvelle-Calédonie et de Polynésie française constitue une juridiction. Le vice-président du Conseil d'État désigne son président parmi les membres du corps des tribunaux administratifs et des cours administratives d'appel, pour une durée de six ans renouvelable. Le cas échéant, deux présidents suppléants peuvent être nommés dans les mêmes conditions.",
    "Nul ne peut exercer les fonctions de président ou de président suppléant d'une section des assurances sociales d'une chambre disciplinaire à partir de l'âge de soixante-dix-sept ans.",
    "La section comprend, en nombre égal, des assesseurs membres, selon le cas, de l'ordre des médecins, de l'ordre des chirurgiens-dentistes ou de l'ordre des sages-femmes et des assesseurs représentant l'organisme de sécurité sociale, dont un praticien conseil. Le président du tribunal administratif dans le ressort territorial duquel se trouve le siège de la section nomme les assesseurs représentant l'organisme de sécurité sociale pour une durée de six ans renouvelable. Les chambres disciplinaires désignent en leur sein les assesseurs membres de l'ordre.",
    "Lorsqu'un assesseur est remplacé, son remplaçant est nommé pour la durée du mandat restant à courir.",
    "Les fonctions d'assesseur ne peuvent être cumulées avec celles de président ou de secrétaire général de l'organe de l'ordre.",
    "Un membre de la section des assurances sociales de la chambre disciplinaire ne peut siéger s'il a eu connaissance des faits de la cause dans l'exercice d'autres fonctions ordinales.",
    "Lorsqu'un organe de l'ordre a déposé une plainte auprès de la section des assurances sociales de la chambre disciplinaire, aucun membre de cet organe ne peut siéger comme assesseur dans la formation de jugement qui statue sur cette plainte.",
    "Les ministres chargés du budget et de la santé fixent par arrêté, après consultation de l'ordre, le montant des indemnités allouées aux présidents et aux présidents suppléants des sections des assurances sociales des chambres disciplinaires.",
    "Les frais de déplacement de ces présidents et présidents suppléants sont remboursés dans les conditions prévues par la réglementation applicable aux fonctionnaires de l'État.",
    "L'organe de l'ordre prend en charge ces indemnités et ces frais.",
],
    "Réécriture à droit constant : les autorités de désignation et de paiement sont nommées comme sujets des obligations ; les deux catégories d'assesseurs et les deux interdictions de siéger sont distinguées. Les dix alinéas, les mandats, la limite d'âge et la prise en charge des frais sont conservés. Aucune réforme de fond de policy.json ne concerne cette organisation juridictionnelle.",
    "Conserver les mandats de six ans renouvelables du président et des assesseurs représentant l'organisme de sécurité sociale, les deux suppléants éventuels et la limite de soixante-dix-sept ans. Aucune durée n'est ajoutée au mandat des assesseurs ordinaux. La note source renvoie au V de l'article 15 de l'ordonnance n° 2017-644 du 27 avril 2017 pour une entrée en vigueur au 1er janvier 2018 ; cette indication historique ne fixe pas l'entrée en vigueur du projet."
)

add('L146-7', [
    "La section des assurances sociales de la chambre de discipline des pharmaciens constitue une juridiction. Le vice-président du Conseil d'État désigne son président parmi les membres du corps des tribunaux administratifs et des cours administratives d'appel, pour une durée de six ans renouvelable. Le cas échéant, deux présidents suppléants peuvent être nommés dans les mêmes conditions.",
    "Nul ne peut exercer les fonctions de président ou de président suppléant d'une section des assurances sociales d'une chambre disciplinaire à partir de l'âge de soixante-dix-sept ans.",
    "La section comprend, en nombre égal, des assesseurs membres de l'ordre des pharmaciens et des assesseurs représentant l'organisme de sécurité sociale, dont un praticien conseil. Le président du tribunal administratif dans le ressort territorial duquel se trouve le siège de la section nomme les assesseurs représentant l'organisme de sécurité sociale. Les assesseurs membres de l'ordre sont désignés au sein de la chambre de discipline.",
    "Lorsqu'un assesseur est remplacé, son remplaçant est nommé pour la durée du mandat restant à courir.",
    "Les fonctions d'assesseur ne peuvent être cumulées avec celles de président ou de secrétaire général de l'organe de l'ordre.",
    "Un membre de la section des assurances sociales de la chambre de discipline ne peut siéger s'il a eu connaissance des faits de la cause dans l'exercice d'autres fonctions ordinales.",
    "Lorsqu'un organe de l'ordre a déposé une plainte auprès de la section des assurances sociales de la chambre de discipline, aucun membre de cet organe ne peut siéger comme assesseur dans la formation de jugement qui statue sur cette plainte.",
    "Les ministres chargés du budget et de la santé fixent par arrêté, après consultation de l'ordre, le montant des indemnités allouées aux présidents et aux présidents suppléants de la section des assurances sociales de la chambre de discipline.",
    "Les frais de déplacement de ces présidents et présidents suppléants sont remboursés dans les conditions prévues par la réglementation applicable aux fonctionnaires de l'État.",
    "L'organe de l'ordre prend en charge ces indemnités et ces frais.",
],
    "Réécriture à droit constant : la désignation du président et des assesseurs représentant la sécurité sociale est formulée à la voix active, les incompatibilités sont exprimées directement et les bénéficiaires du remboursement sont explicités. Les dix alinéas et les règles propres aux pharmaciens sont conservés. Aucune réforme de fond n'est introduite.",
    "La source ne fixe pas ici la durée du mandat des assesseurs : la durée de six ans prévue à L146-6 pour certains assesseurs n'est pas transposée. Elle conserve au deuxième alinéa la désignation générique « chambre disciplinaire », alors que les autres alinéas parlent de « chambre de discipline » ; cette variation n'est pas harmonisée sans coordination. La note historique vise le V de l'article 15 de l'ordonnance n° 2017-644 du 27 avril 2017 et le 1er janvier 2018, sans incidence sur une date future de réforme."
)

add('L146-8', [
    "Devant la section des assurances sociales de la chambre disciplinaire de première instance et devant la section des assurances sociales du conseil national de discipline, la procédure respecte le principe du contradictoire.",
],
    "Réécriture à droit constant de l'alinéa unique : les deux degrés de juridiction précèdent l'énoncé explicite du principe du contradictoire, sans modifier son champ. Aucune réforme de fond n'est applicable.",
    "La source emploie « conseil national de discipline », tandis que L146-5 et L146-9 visent les conseils nationaux des ordres. Cette différence de dénomination est conservée et appelle une vérification de coordination ; aucun organe nouveau n'est créé."
)

add('L146-9', [
    "Le président de la section des assurances sociales de la chambre disciplinaire de première instance et le président de la section des assurances sociales du Conseil national de l'ordre des médecins, des chirurgiens-dentistes, des sages-femmes et des pharmaciens peuvent statuer par ordonnance pour donner acte d'un désistement, constater qu'il n'y a pas lieu de statuer sur une requête ou rejeter des conclusions entachées d'une irrecevabilité manifeste qui ne peut être couverte en cours d'instance.",
],
    "Réécriture à droit constant de l'alinéa unique : les trois pouvoirs exercés par ordonnance sont présentés comme des cas distincts et la condition de non-régularisation est rattachée à l'irrecevabilité manifeste. Aucun pouvoir juridictionnel supplémentaire n'est attribué.",
    "Maintenir cumulativement le caractère manifeste de l'irrecevabilité et l'impossibilité de la couvrir en cours d'instance. La désignation collective des conseils nationaux est conservée ; sa terminologie doit être examinée avec celle de L146-5 et L146-8, sans modifier les compétences par simple harmonisation rédactionnelle."
)

add('L151-1', [
    "L'autorité compétente de l'État contrôle les décisions des conseils ou des conseils d'administration des caisses primaires d'assurance maladie, des caisses d'assurance retraite et de la santé au travail, des caisses d'allocations familiales et des unions de recouvrement.",
    "Cette autorité peut annuler les décisions contraires à la loi. Un décret en Conseil d'État fixe les modalités de ce contrôle de légalité. Il précise notamment les règles de communication des décisions, les délais dans lesquels l'autorité compétente peut les annuler, la procédure de suspension provisoire et les modalités d'intervention des organismes nationaux.",
    "L'autorité compétente de l'État peut également suspendre, dans un délai déterminé, les décisions d'un conseil ou d'un conseil d'administration qui lui paraissent de nature à compromettre l'équilibre financier des risques. Si la caisse intéressée maintient sa décision, elle saisit la caisse nationale compétente. La décision reste suspendue jusqu'à ce que le conseil ou le conseil d'administration de la caisse nationale l'ait explicitement confirmée ou infirmée et que sa délibération soit devenue définitive conformément à l'article L. 226-4.",
    "Des décrets en Conseil d'État fixent les conditions d'application du présent article aux régimes spéciaux mentionnés à l'article L. 711-1.",
],
    "Réécriture à droit constant : l'autorité de contrôle est placée en sujet, le contenu du décret est réparti en phrases plus courtes et la caisse qui maintient sa décision est expressément désignée. Les quatre alinéas, la distinction entre annulation pour illégalité et suspension financière, ainsi que les deux conditions de fin de suspension sont maintenus. Aucune réforme de fond n'est introduite.",
    "Au troisième alinéa, « Si elle maintient sa décision » est explicité comme visant la caisse intéressée et la décision de son conseil ; le prononcé de la suspension demeure du ressort de l'État. Le renvoi à L. 226-4 est présent dans la source mais cet article n'a pas été trouvé dans le corpus public fourni : renvoi maintenu, à contrôler avant consolidation. Le renvoi à L. 711-1 et le cumul de la confirmation ou infirmation explicite avec le caractère définitif de la délibération sont conservés."
)

add('L152-1', [
    "Dans les conditions fixées au présent chapitre, l'État contrôle les décisions des conseils d'administration des organismes d'assurance vieillesse des professions libérales et des avocats, des organismes mentionnés à l'article L. 723-1 du code rural et de la pêche maritime et de l'organisme mentionné à l'article L. 382-12 du présent code.",
    "L'autorité compétente de l'État peut annuler ces décisions lorsqu'elles sont contraires à la loi ou de nature à compromettre l'équilibre financier de la caisse.",
    "Un décret en Conseil d'État fixe les modalités du contrôle prévu au premier alinéa. Il précise notamment les règles de communication des décisions, les délais dans lesquels l'autorité compétente peut prononcer leur annulation et la procédure de suspension provisoire des décisions des organismes.",
    "Pour les organismes de mutualité sociale agricole, des décrets en Conseil d'État peuvent apporter les adaptations nécessaires à ces dispositions.",
],
    "Réécriture à droit constant : la liste des organismes contrôlés est clarifiée et les modalités réglementaires sont énoncées en deux phrases dans le même alinéa. Les deux motifs alternatifs d'annulation et la faculté d'adaptation agricole sont conservés. Les réformes concernant les salariés privés ou la C3S ne sont pas étendues à ce régime de contrôle.",
    "Les quatre alinéas et le renvoi au premier alinéa restent à la même place. Les références à L. 723-1 du code rural et de la pêche maritime et à L. 382-12 du présent code sont conservées ; ce dernier vise dans le corpus une caisse de retraite complémentaire des artistes-auteurs. Contrairement à L151-1, l'atteinte à l'équilibre financier reste ici un motif d'annulation et non seulement de suspension."
)

add('L153-1', [
    "Le présent chapitre s'applique au régime général et aux régimes de protection sociale agricole. Sous réserve des adaptations prévues par décret en Conseil d'État, il s'applique également au régime de base de l'Organisation autonome d'assurance vieillesse des professions libérales et au conseil de la protection sociale des travailleurs indépendants. Il s'applique aussi au régime d'assurance vieillesse de base des avocats. Il ne s'applique ni à la Caisse d'assurance vieillesse, invalidité et maladie des cultes ni à la Caisse des Français de l'étranger. Les budgets de ces derniers organismes ou régimes demeurent soumis à l'approbation du ministre chargé de la sécurité sociale et du ministre chargé du budget. Ces ministres exercent, dans ce cas, les attributions que les articles L. 153-4 et L. 153-5 confient à l'organisme national.",
    "Le présent chapitre s'applique au régime de la sécurité sociale dans les mines. Il s'applique aussi, sous réserve des adaptations prévues par décret en Conseil d'État, aux autres régimes spéciaux de sécurité sociale mentionnés au titre Ier du livre VII. Dans ce cas, le ministre chargé de la sécurité sociale et le ministre chargé du budget exercent conjointement les attributions que les articles L. 153-2, L. 153-4 et L. 153-5 confient à l'organisme national.",
],
    "Réécriture à droit constant : les régimes inclus, les adaptations réglementaires et les deux exclusions sont énoncés en phrases distinctes, dans les deux alinéas d'origine. Les pouvoirs des ministres demeurent rattachés aux mêmes situations et aux mêmes articles. Aucune extension des réformes de retraite aux régimes distincts n'est opérée.",
    "Conserver la distinction entre, au premier alinéa, les attributions des articles L. 153-4 et L. 153-5 et, au second, celles des articles L. 153-2, L. 153-4 et L. 153-5. L'exigence d'exercice conjoint est maintenue expressément au second alinéa. Les adaptations par décret en Conseil d'État ne sont pas imposées au régime minier, au régime agricole ou au régime de base des avocats, que la source vise directement. Les deux caisses exclues restent soumises à l'approbation ministérielle de leurs budgets."
)

add('L153-2', [
    "Les budgets des organismes de base et ceux des établissements qu'ils gèrent doivent être soumis à l'approbation de l'organisme national de rattachement. Toutefois, pour les établissements qui relèvent de la compétence tarifaire de l'État, cette approbation reste du ressort de l'autorité compétente de l'État.",
],
    "Réécriture à droit constant : l'obligation de soumettre les budgets à approbation est explicite et la compétence de l'État est isolée comme une exception liée à son pouvoir tarifaire. L'alinéa unique conserve le champ des organismes et de leurs établissements, sans réforme de fond.",
    "Le régime d'approbation demeure soumis aux attributions particulières prévues par L153-1. Conserver l'exception tarifaire et les coordinations avec L153-4 et L153-5 ; l'approbation ne devient pas une compétence générale de l'État."
)

add('L153-3', [
    "L'autorité compétente de l'État approuve les budgets établis par les organismes à compétence nationale mentionnés aux articles L. 723-1 et L. 723-5 du code rural et de la pêche maritime.",
],
    "Réécriture à droit constant de l'alinéa unique : l'autorité d'approbation devient le sujet de la phrase, sans changer les organismes concernés ni les deux renvois. Aucune réforme de fond n'est introduite.",
    "Maintenir les deux références agricoles, L. 723-1 et L. 723-5, et la compétence de l'État pour les budgets de ces organismes nationaux ; ne pas leur substituer l'organisme de rattachement visé à L153-2."
)

add('L153-4', [
    "Lorsque les budgets prévus à l'article L. 153-2 n'ont pas été, selon le cas, votés, arrêtés ou délibérés par le conseil ou le conseil d'administration au 1er janvier de l'année concernée, l'organisme national compétent peut les établir d'office. Si cet organisme n'y procède pas, l'autorité compétente de l'État établit elle-même ces budgets d'office.",
],
    "Réécriture à droit constant : les deux étapes de l'établissement d'office sont formulées avec un sujet explicite, en conservant le déclenchement au 1er janvier et les trois modes d'adoption des budgets. L'alinéa unique et la faculté initiale de l'organisme national sont maintenus, sans réforme de fond.",
    "Le 1er janvier reste celui de l'année budgétaire en cause, non une date d'entrée en vigueur du projet. L'État intervient en cas de carence de l'organisme national ; les substitutions particulières de compétence de L153-1 et le renvoi à L. 153-2 doivent rester coordonnés."
)

add('L153-5', [
    "Lorsque le conseil ou le conseil d'administration d'un organisme de sécurité sociale omet ou refuse d'inscrire aux budgets prévus à l'article L. 153-2 un crédit suffisant pour payer des dépenses obligatoires, l'organisme national décide d'inscrire d'office le crédit nécessaire au budget correspondant. Sont concernées les dépenses rendues obligatoires par des dispositions législatives ou réglementaires ou par des stipulations conventionnelles prises en vertu des articles L. 123-1 et L. 123-2 et agréées par l'autorité compétente de l'État. En cas de carence de l'organisme national, l'autorité compétente de l'État procède elle-même à cette inscription d'office.",
],
    "Réécriture à droit constant : l'alinéa unique distingue le défaut d'inscription, les sources de l'obligation de dépense et l'intervention subsidiaire de l'État. Les stipulations conventionnelles demeurent soumises aux renvois et à l'agrément prévus par la source. Aucune dépense nouvelle ni réforme de fond n'est créée.",
    "Conserver les deux cas, omission et refus, ainsi que le montant suffisant du crédit et son inscription au budget correspondant. L'agrément de l'État reste une condition attachée aux stipulations conventionnelles prises en vertu de L. 123-1 et L. 123-2. Maintenir les coordinations de compétence avec L153-1 et le champ budgétaire de L. 153-2."
)

add('L153-6', [
    "L'autorité compétente de l'État peut s'opposer à l'octroi, par tout organisme de sécurité sociale, d'un avantage financier à un établissement, une œuvre ou une institution dont la gestion n'est pas assujettie aux règles de la comptabilité publique, quelle que soit sa nature juridique. Un décret fixe les cas, les conditions et les délais de cette opposition.",
],
    "Réécriture à droit constant : le pouvoir d'opposition de l'État est exprimé directement et son encadrement réglementaire fait l'objet d'une seconde phrase au sein du même alinéa. La condition de gestion hors comptabilité publique et l'indifférence à la nature juridique sont conservées, sans réforme de fond.",
    "Le décret prévu est un décret simple, sans ajout d'une exigence de Conseil d'État. Le pouvoir porte sur l'octroi d'un avantage financier par tout organisme de sécurité sociale ; il ne devient pas une interdiction générale de tels avantages."
)

add('L153-7', [
    "Des décrets en Conseil d'État peuvent rendre l'article L. 281-2 applicable à tout organisme de sécurité sociale doté de la personnalité civile et soumis au contrôle de la Cour des comptes en application des articles L. 154-1 et L. 154-2. Ils peuvent prévoir les adaptations nécessaires.",
],
    "Réécriture à droit constant : le pouvoir réglementaire d'extension et la faculté d'adaptation sont énoncés en deux phrases dans l'alinéa unique. Les conditions tenant à la personnalité civile et au contrôle de la Cour des comptes restent cumulatives. Aucune extension immédiate ni réforme de fond n'est prononcée.",
    "Maintenir la faculté, exercée par décret en Conseil d'État, et les trois renvois à L. 281-2, L. 154-1 et L. 154-2. L. 281-2, consulté dans le corpus fourni, organise une substitution en cas de carence pour l'exécution de dépenses ou le recouvrement de recettes obligatoires ; ce mécanisme n'est pas modifié ici."
)

add('L153-8', [
    "Le conseil ou les conseils d'administration des organismes nationaux des régimes mentionnés à l'article L. 153-1 peuvent encadrer l'évolution de leurs dépenses budgétaires en fixant des règles et des modalités pour une durée de trois ans. Ces délibérations doivent être soumises à l'approbation du ministre chargé de la sécurité sociale et du ministre chargé du budget.",
],
    "Réécriture à droit constant : la faculté d'encadrer l'évolution des dépenses est énoncée avant ses règles et sa durée ; l'obligation de soumettre les délibérations aux deux ministres est explicite. La faculté de programmer et l'approbation restent distinctes dans l'alinéa unique. Aucun budget ni réforme de fond n'est ajouté.",
    "La durée reste de trois ans et le champ reste celui des régimes mentionnés à L. 153-1. L'approbation des deux ministres est maintenue ; la programmation n'est pas présentée comme un financement des baisses de prélèvements ou de la transition des retraites."
)

add('L153-9', [
    "Les schémas directeurs informatiques des organismes de sécurité sociale mentionnés au deuxième alinéa du présent article doivent être soumis à l'approbation de l'autorité compétente de l'État.",
    "Dans les conditions définies par décret, cette obligation s'applique aux organismes du régime général, aux organismes de mutualité sociale agricole et aux organismes des régimes des travailleurs indépendants non agricoles relevant du livre VI.",
],
    "Réécriture à droit constant : l'autorité d'approbation et la portée du renvoi sont explicitées, en conservant les deux alinéas et les trois catégories d'organismes. Aucun nouveau partage de données ni dispositif de simplification non défini par la source n'est introduit.",
    "Le renvoi au deuxième alinéa reste exact et le décret demeure un décret simple. La désignation des régimes des travailleurs indépendants non agricoles et son rattachement au livre VI sont conservés tels que fournis ; leur adéquation à l'organisation actuelle doit être contrôlée, sans remplacement implicite des organismes visés."
)

add('L153-10', [
    "L'autorité compétente de l'État contrôle les organismes de sécurité sociale pour évaluer l'efficacité de leur action et mesurer leurs résultats au regard des objectifs qu'ils se sont fixés et de ceux que l'État leur a fixés.",
],
    "Réécriture à droit constant : la finalité du contrôle est exprimée directement et les deux origines des objectifs sont explicitées. L'alinéa unique conserve l'évaluation de l'efficacité et la mesure des résultats, sans nouvelle obligation de résultat ni réforme de fond.",
    "Les objectifs propres aux organismes et ceux de l'État demeurent tous deux des références du contrôle. L'article ne constate aucune économie et ne vaut pas financement des mesures figurant dans policy.json."
)

add('L154-1', [
    "La Cour des comptes contrôle les organismes de la sécurité sociale dans les conditions et selon les modalités fixées par décret en Conseil d'État.",
],
    "Réécriture à droit constant de l'alinéa unique : la Cour des comptes est placée en sujet et le renvoi réglementaire est allégé sans modification de sa portée. Aucune réforme de fond n'est introduite.",
    "Conserver le décret en Conseil d'État et l'articulation avec le champ personnel et territorial de L154-2. Le contrôle de la Cour des comptes demeure distinct de l'approbation administrative des budgets prévue au chapitre précédent."
)

add('L154-2', [
    "En France métropolitaine et dans les collectivités mentionnées à l'article L. 751-1, l'article L. 154-1 s'applique à tous les organismes de droit privé dotés de la personnalité civile ou de l'autonomie financière qui assurent, en tout ou partie, la gestion d'un régime légalement obligatoire d'assurance contre la maladie, la maternité, la vieillesse, l'invalidité, le décès, les accidents du travail et les maladies professionnelles ou de prestations familiales. Il s'applique également aux unions et aux fédérations de ces organismes.",
],
    "Réécriture à droit constant : le renvoi relatif à l'article précédent est remplacé par sa référence explicite, et les unions et fédérations sont visées dans une seconde phrase du même alinéa. Les critères alternatifs de personnalité civile ou d'autonomie financière, la gestion partielle et tous les risques sont conservés, sans réforme de fond.",
    "Le corpus fourni comporte L. 751-1 avec une abrogation différée au 1er janvier 2028. Le renvoi territorial est conservé pour la version assignée ; il appelle une coordination à cette échéance, sans substitution anticipée. Conserver le caractère légalement obligatoire du régime, la totalité des risques énumérés, les prestations familiales et l'alternative entre personnalité civile et autonomie financière."
)

add('L160-1', [
    "Toute personne qui travaille ou, si elle n'exerce pas d'activité professionnelle, réside en France de manière stable et régulière bénéficie, en cas de maladie ou de maternité, de la prise en charge de ses frais de santé dans les conditions fixées au présent livre.",
    "L'exercice d'une activité professionnelle est apprécié selon les règles de l'article L. 111-2-2 ; les conditions de résidence en France le sont selon celles de l'article L. 111-2-3.",
    "Un décret en Conseil d'État fixe les conditions dans lesquelles les personnes qui résident en France mais cessent de remplir les autres conditions mentionnées à l'article L. 111-2-3 conservent leurs droits pendant une durée maximale d'un an. Cette prolongation concerne la prise en charge des frais de santé mentionnée aux articles L. 160-8 et L. 160-9-1 et, le cas échéant, la protection complémentaire en matière de santé prévue à l'article L. 861-1.",
],
    "Réécriture à droit constant : les deux critères d'ouverture des droits sont exprimés directement, chaque règle d'appréciation est rattachée à son article et le champ de la prolongation est distingué de sa durée dans le même troisième alinéa. Aucune réforme des pensions ou de la CSG n'est appliquée à la couverture maladie et maternité.",
    "Conserver le caractère alternatif de l'activité et de la résidence pour une personne sans activité, ainsi que le plafond d'un an et le caractère éventuel de la protection complémentaire. Les cinq renvois sont maintenus. La note source fixe, en application du I de l'article 5 de l'ordonnance n° 2021-1554 du 1er décembre 2021 et de l'article 1 du décret n° 2022-801 du 12 mai 2022, l'entrée en vigueur au 14 mai 2022, avant la date limite du 30 juin 2022 ; aucune de ces dates ne sert de date au projet."
)

add('L160-1-1', [
    "Sous réserve des conventions internationales et des règlements européens, la prise en charge des frais de santé prévue au premier alinéa de l'article L. 160-1 est subordonnée au paiement d'une participation financière pour toute personne qui remplit les conditions suivantes : elle réside en France de manière stable et régulière ; elle n'y exerce pas d'activité professionnelle ; en vertu d'une convention internationale, elle n'est pas redevable des cotisations et contributions mentionnées aux articles L. 131-9 et L. 136-1.",
    "Lorsque cette personne ne paie pas sa participation financière pendant une durée déterminée, le directeur de l'organisme chargé de la prise en charge des frais de santé vérifie sa situation, puis lui notifie que son droit à cette prise en charge sera suspendu si elle ne paie pas le montant dû.",
    "Un décret en Conseil d'État fixe les modalités d'application du présent article. Il précise notamment le montant de la participation, les modalités de sa notification et de son recouvrement, ainsi que les modalités de suspension du droit à la prise en charge des frais de santé en cas de non-paiement.",
],
    "Réécriture à droit constant : les conditions cumulatives d'assujettissement sont rendues lisibles par une énumération dans le premier alinéa, puis la vérification et la notification sont placées dans leur ordre d'exécution. Le décret conserve la fixation du montant et des modalités. Aucun taux ni délai nouveau, ni réforme de fond, n'est ajouté.",
    "Maintenir la réserve des conventions internationales et des règlements européens et le lien entre l'absence de dette de cotisations ou contributions et une convention internationale. La suspension reste précédée de la vérification de situation et d'une notification conditionnelle ; aucune suspension automatique n'est ajoutée. La source ne chiffre ni le montant de la participation ni la durée de non-paiement. La note historique relative à l'entrée en vigueur immédiate de la rédaction issue de la loi n° 2025-1403 du 30 décembre 2025 ne fixe pas l'entrée en vigueur du projet."
)

add('L160-2', [
    "Par dérogation à l'article L. 160-1, les enfants mineurs qui n'exercent pas d'activité professionnelle et sont à la charge d'un assuré social bénéficient de la prise en charge de leurs frais de santé en qualité d'ayants droit de cet assuré. Ils doivent avoir une filiation légalement établie, y compris adoptive, ou être pupilles de la Nation ou enfants recueillis.",
    "Le statut d'ayant droit cesse à une date fixée par décret, au cours de l'année où l'enfant atteint sa majorité.",
    "Dès l'âge de seize ans, l'enfant peut demander à bénéficier à titre personnel de la prise en charge de ses frais de santé en cas de maladie ou de maternité, selon les modalités fixées par décret.",
    "Les personnes ou les établissements qui assurent l'accueil ou la garde d'enfants mineurs pris en charge par les services de l'aide sociale à l'enfance peuvent demander que ces enfants soient identifiés de façon autonome au sein du régime de l'assuré social. Ces personnes ou établissements bénéficient, pour le compte de l'assuré, de la prise en charge de ses frais de santé en cas de maladie ou de maternité.",
],
    "Réécriture à droit constant : les conditions de la qualité d'ayant droit sont séparées de son effet au sein du premier alinéa, l'âge de la demande personnelle est placé en tête et les auteurs de la demande d'identification autonome sont explicites. Les quatre alinéas et les règles des mineurs sont conservés, sans réforme de fond.",
    "L'expression « pour le compte de l'assuré » au dernier alinéa est conservée : la source rattache les frais à « ce dernier » alors que le dispositif porte sur les enfants accueillis ; l'identité du bénéficiaire désigné doit être contrôlée, sans substitution silencieuse de l'enfant à l'assuré. La note source, fondée sur le VI de l'article 11 de la loi n° 2018-166 du 8 mars 2018, fixe l'entrée en vigueur au 1er septembre 2018 et comporte des transitions extérieures au texte codifié : 1° les étudiants rattachés au 31 août 2018 aux organismes délégataires des deuxième et troisième alinéas de l'ancien L. 160-17 y demeurent, tant qu'aucun autre titre n'impose leur rattachement ailleurs, au plus tard jusqu'aux dates du 2° ; le régime général assure ensuite leur prise en charge ; 2° les conventions et contrats conclus pour servir leurs prestations en application du troisième alinéa de cet ancien article cessent au 31 août 2019, sauf accord des parties sur des dates antérieures. Les droits et obligations des délégataires visés aux deuxième et troisième alinéas, y compris les contrats de travail afférents à la gestion confiée, sont transférés de plein droit aux mêmes dates aux organismes d'assurance maladie du régime général, sans droits, impôts ni taxes de quelque nature que ce soit. L'indemnisation du préjudice des délégataires reste soumise à son caractère anormal et spécial et à un constat établi après procédure contradictoire ; ses conditions et son montant sont fixés par décret. Ces effets transitoires et droits éventuels à indemnité ne sont ni abrogés ni réinitialisés par la réécriture ; ils ne sont pas incorporés comme de nouveaux alinéas du code."
)

add('L160-3', [
    "Les personnes énumérées aux 1° à 4° qui résident à l'étranger et n'exercent pas d'activité professionnelle bénéficient, pendant leurs séjours temporaires en France, de la prise en charge de leurs frais de santé prévue à l'article L. 160-1. La prestation susceptible d'ouvrir ce droit ne doit toutefois pas être celle mentionnée à l'article L. 161-22-2.",
    "1° Les titulaires d'une pension ou d'une rente de vieillesse ou d'une pension de réversion servie par un régime de base de sécurité sociale français ;",
    "2° Les titulaires d'une rente ou d'une allocation accordée en application des dispositions législatives relatives aux accidents du travail et aux maladies professionnelles applicables aux professions non agricoles ;",
    "3° Les titulaires d'une pension de vieillesse substituée à une pension d'invalidité ou d'une pension d'invalidité, servie par un ou plusieurs régimes de base français ;",
    "4° Les personnes mentionnées à l'article L. 117-3 du code de l'action sociale et des familles.",
    "Sous réserve des règles relatives au séjour temporaire prévues par les règlements européens et les conventions internationales de sécurité sociale, ou des dispositions applicables dans l'État de résidence qui prévoient la prise en charge de soins dispensés hors de son territoire, le premier alinéa du présent article s'applique :",
    "a) Aux personnes mentionnées aux 1° à 3°, lorsque les conventions internationales de sécurité sociale donnent à la France une compétence exclusive pour la prise en charge des soins de santé dispensés dans leur État de résidence ;",
    "b) Aux personnes mentionnées aux 1° et 3° qui ne relèvent pas du a et dont la pension rémunère une durée d'assurance d'au moins quinze années au titre d'un régime français ;",
    "c) Aux enfants mineurs qui n'exercent pas d'activité professionnelle et sont à la charge des personnes mentionnées aux a et b.",
],
    "Réécriture à droit constant : les conditions de séjour, l'exclusion d'une prestation et les réserves internationales sont formulées plus directement. Les neuf alinéas, les quatre catégories et les trois lettres sont conservés, ainsi que les combinaisons propres à chaque lettre. Aucune mesure de transfert de cotisations ou de gel des pensions n'est appliquée à ces droits de santé.",
    "Conserver l'exclusion de la prestation de L. 161-22-2 et le seuil de quinze années au b, sans étendre ce b aux titulaires du 2°. Le renvoi à L. 117-3 du code de l'action sociale et des familles et la réserve internationale sont maintenus. La source énumère les personnes du 4° mais ne les reprend pas dans les lettres a et b ; cette articulation est conservée et mérite contrôle, sans ajout de catégorie. La note source, fondée sur le 3° du IX de l'article 52 de la loi n° 2018-1203 du 22 décembre 2018, fixe au 1er juillet 2019 l'entrée en vigueur des quatre derniers alinéas issus du 4° du II ; cette date historique n'est pas celle du projet."
)

add('L160-4', [
    "Les personnes énumérées ci-dessous bénéficient également de la prise en charge de leurs frais de santé si elles n'exercent pas d'activité professionnelle en France :",
    "1° Les membres de la famille qui accompagnent les travailleurs temporairement détachés depuis la France à l'étranger pour y exercer une activité professionnelle et qui sont exemptés d'affiliation au régime de sécurité sociale de l'État de détachement en application d'une convention internationale de sécurité sociale ou d'un règlement européen ;",
    "2° Les membres de la famille qui sont à la charge d'un assuré du régime de sécurité sociale français, ne résident pas en France et bénéficient de cette prise en charge en application d'une convention internationale de sécurité sociale ou d'un règlement européen ;",
    "3° Les membres du personnel diplomatique et consulaire, les fonctionnaires de la République française et les personnes assimilées en poste à l'étranger, ainsi que les membres de leur famille qui les accompagnent.",
],
    "Réécriture à droit constant : la condition commune d'absence d'activité professionnelle en France est exprimée en tête et les conditions du 2° sont coordonnées de façon plus lisible. L'alinéa introductif et les trois numéros sont maintenus, sans réforme de fond ; le rattachement ambigu d'une condition au 1° est signalé sans être tranché.",
    "Au 1°, la source ne permet pas de lever sûrement l'ambiguïté du relatif « qui sont exemptés d'affiliation » entre les membres de la famille et les travailleurs détachés ; ce rattachement est conservé et doit être contrôlé. Le caractère temporaire, le départ depuis la France et le fondement international ou européen restent exigés. Au 2°, la charge de famille, la résidence hors de France et le titre international ou européen restent cumulatifs. Au 3°, conserver les personnes assimilées et la condition d'accompagnement de la famille. L'absence d'activité professionnelle exigée en tête demeure limitée à la France."
)

add('L160-5', [
    "Toute personne qui, dans les conditions fixées par décret, déclare à une caisse primaire d'assurance maladie qu'elle ne bénéficie pas de la prise en charge des frais de santé mentionnée à l'article L. 160-1 obtient cette prise en charge auprès de cette caisse dès qu'elle justifie de son identité et de sa résidence stable et régulière.",
    "Les services sociaux, les associations et organismes à but non lucratif agréés par décision du représentant de l'État dans le département, ainsi que les établissements de santé, aident les intéressés à demander leur affiliation. Avec l'accord de l'intéressé, ils sont habilités à transmettre à l'organisme compétent les documents relatifs à cette demande.",
    "Les personnes sans domicile stable sont tenues d'élire domicile dans les conditions prévues au chapitre IV du titre VI du livre II du code de l'action sociale et des familles.",
],
    "Réécriture à droit constant : le moment où la prise en charge est obtenue est conservé, l'aide à l'affiliation et l'habilitation à transmettre les pièces sont distinguées dans le même deuxième alinéa, et l'obligation de domiciliation est exprimée directement. Aucun échange de données supplémentaire ni réforme de fond n'est créé.",
    "Conserver les justificatifs cumulatifs d'identité et de résidence stable et régulière, ainsi que l'accord de l'intéressé avant transmission. L'agrément départemental reste attaché aux associations et organismes à but non lucratif. Le renvoi au chapitre IV du titre VI du livre II du code de l'action sociale et des familles est maintenu. Coordonner la lecture du droit ouvert avec les conditions particulières de L160-1 et L160-1-1, sans créer ici une dispense nouvelle de participation financière."
)


assert len(sources) == 24
assert set(drafts) == {s['number'] for s in sources}
answer = []
for source in sources:
    item = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    item.update(drafts[source['number']])
    answer.append(item)
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
