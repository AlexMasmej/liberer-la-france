import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
drafts = {}


def add(number, paragraphs, reason, notes):
    assert number not in drafts
    drafts[number] = {
        'proposed_xml': '\n'.join('<p>' + p + '</p>' for p in paragraphs),
        'reason': reason,
        'review_notes': notes,
    }


reuse = (
    " Pour les déclarations prévues au présent article, l'administration réutilise les informations "
    "qu'elle détient déjà légalement et qu'elle est autorisée à utiliser pour l'obligation concernée, "
    "lorsqu'elles se rapportent au même contribuable et à la même période. Elle les met à la disposition "
    "du déclarant et n'en exige pas une nouvelle saisie lorsqu'elles sont exactes et complètes. "
    "Le déclarant peut les vérifier, les compléter et les corriger, ainsi qu'en demander la rectification "
    "au service qui les détient. Cette réutilisation respecte les secrets protégés par la loi et ne dispense "
    "pas du dépôt de la déclaration dans le délai applicable. Ces modalités de réutilisation s'appliquent "
    "aux déclarations déposées à compter de l'entrée en vigueur de la présente rédaction."
)

reuse_note = (
    " Réforme déclarative du volet entreprise de policy.json : réemploi limité aux données déjà détenues "
    "légalement et utilisables pour l'obligation, concernant le même contribuable et la même période ; "
    "aucune habilitation nouvelle à échanger des données couvertes par un secret. Coordonner les formulaires "
    "et téléprocédures correspondants pour permettre la mise à disposition et la rectification auprès du "
    "service détenteur. Les dépôts restent obligatoires et les délais sont conservés. La règle nouvelle "
    "vise les dépôts à compter de l'entrée en vigueur de la présente rédaction, sans modifier les droits "
    "fiscaux attachés aux dépenses ou aux contrats antérieurs. Si une transmission entre administrations "
    "requiert une dérogation au secret fiscal, elle appelle une disposition législative distincte dans le "
    "livre des procédures fiscales, notamment au regard de son article L. 103, hors des cinq codes ; "
    "aucune dérogation ni aucun renvoi nouveau n'est créé ici."
)

add('49 septies WG', [
    "Lorsqu'un des événements mentionnés au III de l'article 244 quater E du code général des impôts n'affecte qu'une partie des investissements ayant ouvert droit au crédit d'impôt au titre d'une année ou d'un exercice, la part du crédit d'impôt de cette année ou de cet exercice déjà utilisée pour payer l'impôt est réputée provenir des investissements réalisés au titre de la même année ou du même exercice qui ne sont pas affectés par ces événements."
],
    "Réécriture à droit constant : la condition tenant à l'atteinte d'une partie seulement des investissements est placée en tête et la règle d'affectation du crédit déjà utilisé est formulée directement. Aucune modification de fond du crédit d'impôt pour investissement n'est introduite.",
    "Maintien du renvoi au III de l'article 244 quater E et du rattachement à la même année ou au même exercice pour les investissements et le crédit déjà utilisé. La présomption porte seulement sur la part déjà imputée, sans modifier le montant à reprendre ni les événements de reprise."
)

add('49 septies WH', [
    "Lorsqu'un événement mentionné au III de l'article 244 quater E du code général des impôts entraîne la remise en cause de tout ou partie du crédit d'impôt, l'entreprise propriétaire des investissements ayant ouvert droit à ce crédit délivre au contribuable ou à l'entreprise concerné un relevé d'information dans les deux mois suivant cet événement. Ce relevé comprend :",
    "a. L'identité et l'adresse du bénéficiaire du crédit d'impôt ;",
    "b. L'année du crédit d'impôt à reprendre ;",
    "c. La date de cession ou de changement d'affectation des immobilisations ou de cessation d'activité ;",
    "d. Le montant du crédit d'impôt à reprendre.",
    "Le relevé est établi selon un modèle fixé par l'administration.",
    "L'entreprise propriétaire des biens adresse une copie de ce relevé, dans le même délai de deux mois, au service chargé de l'assiette de l'impôt dont elle dépend."
],
    "Réécriture à droit constant : l'entreprise tenue de délivrer le relevé et d'en adresser la copie est désignée explicitement ; le délai est rattaché à l'événement déclenchant la reprise. Les quatre informations exigées et le modèle administratif sont conservés. Aucune réforme de fond.",
    "Lettres a à d et ordre des informations conservés. Le délai de deux mois s'applique à la délivrance et à la copie ; son point de départ reste l'événement visé au III de l'article 244 quater E. Le bénéficiaire du relevé et le service destinataire de la copie ont des fonctions distinctes : leur envoi respectif n'est pas supprimé comme un doublon."
)

add('49 septies X', [
    "Pour l'application de l'article 238 bis du code général des impôts, les entreprises déclarent les réductions d'impôt et les informations prévues au premier alinéa du 6 du même article 238 bis, selon le format établi par l'administration. Elles déposent cette déclaration dans les mêmes délais que la déclaration annuelle de résultat qu'elles sont tenues de souscrire en application des articles 53 A et 223 du même code." + reuse,
    "La société mère d'un groupe au sens de l'article 223 A du code général des impôts déclare, pour le compte des sociétés du groupe, les réductions d'impôt et les informations prévues au premier alinéa du 6 de l'article 238 bis du même code, y compris celles qui la concernent. Elle effectue cette déclaration lors du dépôt de la déclaration relative au résultat d'ensemble du groupe."
],
    "À droit constant, la réécriture distingue le contenu, le format et le délai de déclaration, puis rend explicite la déclaration centralisée par la société mère. Réforme de fond limitée à la procédure : application de la mesure déclarer une fois par réutilisation des données légalement détenues, sans nouvelle saisie des données exactes, avec faculté de correction et maintien du dépôt.",
    "Deux alinéas conservés ; la règle nouvelle est intégrée au premier sans déplacer le second. Maintien des renvois au premier alinéa du 6 de l'article 238 bis, aux articles 53 A, 223 et 223 A et de la déclaration de la société mère pour elle-même. La fiche de l'article 238 bis du corpus porte l'état ABROGE_DIFF et une borne au 1er janvier 2027 : contrôler la coordination temporelle sans en déduire ici la suppression de la réduction ni modifier ses conditions." + reuse_note
)

add('49 septies XA', [
    "1. Pour l'application de l'article 200 bis du code général des impôts, les personnes physiques qui bénéficient de la réduction d'impôt joignent un état de suivi conforme à un modèle établi par l'administration à leur déclaration de revenus ou, s'il s'agit d'un exploitant individuel, à leur déclaration de résultat de l'exercice.",
    "2. Abrogé."
],
    "Réécriture à droit constant : l'obligation de joindre l'état de suivi est exprimée directement, et l'alternative entre les supports déclaratifs est rendue plus lisible en rapprochant la condition d'exploitant individuel de la déclaration de résultat. Le 2 abrogé est conservé ; aucune réforme de fond.",
    "Numérotation 1 et 2 maintenue. Le renvoi à l'article 200 bis est présent dans le corpus et renvoie à la réduction de l'article 238 bis. Les deux supports déclaratifs ne sont pas cumulés pour l'exploitant individuel. Le suivi des réductions antérieures est conservé ; aucun changement du report ni de son ordre d'imputation."
)

add('49 septies XB', [
    "La réduction d'impôt correspondant aux dons versés aux œuvres et organismes d'intérêt général au cours de l'année ou de l'exercice au titre duquel l'impôt est calculé est imputée sur cet impôt avant les réductions d'impôt de même nature calculées au titre d'années ou d'exercices antérieurs. Lorsque le redevable dispose de réductions d'impôt reportables, il les impute par ordre d'ancienneté."
],
    "Réécriture à droit constant : les deux règles successives d'imputation sont exprimées avec les verbes imputer et disposer, en désignant le redevable pour l'utilisation des reports. La priorité de la réduction de l'année et l'ordre des reports restent identiques ; aucune réforme de fond.",
    "Un alinéa conservé. Priorité de la réduction de l'année ou de l'exercice courant sur celles des périodes antérieures, puis ordre d'ancienneté des reports. Aucun changement de durée, de plafond, de taux ou de nature des organismes bénéficiaires."
)

add('49 septies XC', [
    "Les prestations et produits mentionnés au 2 de l'article 238 bis du code général des impôts sont les suivants :<br /><br />1° La fourniture gratuite de repas à des personnes en difficulté ;<br /><br />2° Le logement de personnes en difficulté ;<br /><br />3° La fourniture gratuite, lorsqu'elle est exercée à titre principal, à des personnes en difficulté :<br /><br />a. De soins mentionnés au 1° du 4 de l'article 261 du même code ;<br /><br />b. Des matériels mentionnés à l'article 2 du décret n° 2015-981 du 31 juillet 2015 fixant la liste des éléments de mobilier d'un logement meublé, ainsi que de meubles de rangement, de linge de maison, d'équipements de salle de bain et de puériculture, de biberons et de matériels pour nourrissons et enfants en bas âge, et de petits et gros appareils électroménagers ;<br /><br />c. De matériels et équipements spécialement conçus pour les personnes handicapées ou à mobilité réduite, à savoir les appareillages, équipements et matériels mentionnés aux a à c et f du 2° du A de l'article 278-0 bis du même code ;<br /><br />d. De fournitures scolaires, y compris les jouets et jeux d'éveil et éducatifs ;<br /><br />e. De vêtements, y compris les chaussures ;<br /><br />f. De produits sanitaires, y compris les produits d'entretien ménager, et de produits d'hygiène bucco-dentaire et corporelle ;<br /><br />g. De produits de protection hygiénique féminine ;<br /><br />h. De couches pour nourrissons ;<br /><br />i. De produits et matériels utilisés pour l'incontinence ;<br /><br />j. De produits contraceptifs."
],
    "Réécriture à droit constant : la phrase introductive et le 3° sont simplifiés, et les articles et prépositions rendent chaque catégorie de produits grammaticalement explicite. Toutes les catégories et leurs renvois sont reproduits intégralement ; aucune réforme de fond.",
    "Maintien du paragraphe avec les subdivisions 1°, 2°, 3° et a à j dans leur ordre. La gratuité reste exigée aux 1° et 3°, sans être ajoutée au 2°. La condition d'exercice à titre principal reste limitée au 3°. Décret n° 2015-981 du 31 juillet 2015, article 2, et renvois au 1° du 4 de l'article 261 et aux a à c et f du 2° du A de l'article 278-0 bis maintenus. La fiche de l'article 238 bis porte dans le corpus l'état ABROGE_DIFF avec une borne au 1er janvier 2027 ; contrôler la coordination temporelle sans supprimer la liste sur ce seul fondement."
)

add('49 septies Y', [
    "Pour l'application du 1 du I de l'article 244 quater F du code général des impôts, les dépenses et versements retenus sont les suivants :",
    "a) Les dépenses engagées par l'entreprise pour financer la création ou le fonctionnement d'un établissement mentionné au premier alinéa de l'article L. 2324-1 du code de la santé publique, géré par une personne physique ou morale de droit privé, exploité directement par l'entreprise et accueillant les enfants de moins de trois ans de ses salariés ;",
    "b) Les versements effectués directement par l'entreprise à des organismes publics ou privés exploitant un établissement mentionné au premier alinéa de l'article L. 2324-1 du code de la santé publique, en contrepartie de prestations d'accueil des enfants de moins de trois ans de ses salariés. À la demande de l'administration, l'entreprise fournit tous les justificatifs relatifs à l'affectation effective de ces versements à l'activité d'accueil des enfants de moins de trois ans de ses salariés."
],
    "Réécriture à droit constant : les deux catégories de dépenses sont formulées autour de l'entreprise qui finance ou verse, et les conditions de gestion, d'exploitation et d'accueil sont rendues successives. L'obligation de justifier l'affectation effective est exprimée au présent ; aucune réforme de fond.",
    "Trois alinéas et lettres a) et b) conservés. Le a) reste limité à la gestion par une personne de droit privé et à l'exploitation directe par l'entreprise ; le b) conserve les organismes publics ou privés et la contrepartie d'accueil. Âge strictement inférieur à trois ans, qualité d'enfant de salarié, versement direct et contrôle sur demande maintenus. Aucune extension aux autres dépenses familiales de l'article 244 quater F."
)

add('49 septies YA', [
    "Lorsque l'exercice est clos en cours d'année, le crédit d'impôt prévu à l'article 244 quater F du code général des impôts et son plafond sont calculés à partir des dépenses éligibles engagées au titre de la dernière année civile écoulée."
],
    "Réécriture à droit constant : le crédit d'impôt et son plafond sont désignés directement, et la période des dépenses est formulée sans périphrase. La règle applicable à la clôture en cours d'année est intégralement conservée ; aucune réforme de fond.",
    "Maintien de la dernière année civile écoulée comme période de référence commune au crédit et au plafond. Ni proratisation nouvelle du plafond ni substitution de l'exercice comptable à l'année civile. Renvoi à l'article 244 quater F inchangé."
)

add('49 septies YB', [
    "Le crédit d'impôt prévu à l'article 244 quater F du code général des impôts s'impute sur l'impôt dû après l'imputation des prélèvements non libératoires et des autres crédits d'impôt."
],
    "Réécriture à droit constant : l'ordre d'imputation est explicité en rattachant les prélèvements et les autres crédits à leur imputation préalable. Aucune réforme de fond ni règle nouvelle de restitution.",
    "Le crédit famille conserve son rang après les prélèvements non libératoires et les autres crédits. Le renvoi à l'article 244 quater F est maintenu ; les modalités de restitution des articles 199 ter E et 220 G ne sont pas modifiées."
)

add('49 septies YC', [
    "Pour l'application des articles 199 ter E, 220 G et 244 quater F du code général des impôts, les entreprises annexent une déclaration spéciale à la déclaration de résultat qu'elles sont tenues de déposer auprès du service des impôts dont elles dépendent." + reuse,
    "Les personnes morales passibles de l'impôt sur les sociétés déposent cette déclaration spéciale auprès du comptable de la direction générale des finances publiques du lieu d'imposition défini à l'article 218 A du code général des impôts, avec le relevé de solde de l'exercice concerné mentionné à l'article 360. Pour les sociétés relevant du régime des groupes prévu à l'article 223 A du code général des impôts, la société mère joint les déclarations spéciales du groupe au relevé de solde relatif au résultat d'ensemble. Les sociétés du groupe sont dispensées d'annexer leur déclaration spéciale à la déclaration de résultat qu'elles sont tenues de déposer en application du 1 de l'article 223 du même code.",
    "Une copie de la déclaration spéciale est adressée, dans le même délai, au ministre chargé de la famille."
],
    "À droit constant, les obligations de dépôt sont formulées au présent et les modalités propres à l'impôt sur les sociétés et aux groupes sont rendues plus lisibles. Réforme de fond procédurale : les données légalement détenues et réutilisables sont mises à disposition sans ressaisie, avec correction possible. Les destinataires et le dépôt restent ceux de la source.",
    "Trois alinéas conservés, sans déplacer le régime des personnes morales ni la copie ministérielle. Renvois aux articles 199 ter E, 220 G, 244 quater F, 218 A, 223 A, au 1 de l'article 223 et à l'article 360 de la présente annexe maintenus. La source distingue le dépôt avec le relevé de solde et la dispense d'annexe à la déclaration de résultat pour les sociétés du groupe. La copie au ministre chargé de la famille est maintenue : un accès légal de ce ministre aux données fiscales ne peut être présumé." + reuse_note
)

add('49 septies YP', [
    "Lorsque l'exercice est clos en cours d'année, le crédit d'impôt prévu à l'article 244 quater J du code général des impôts est calculé à partir des avances remboursables sans intérêt versées au titre de la dernière année civile écoulée."
],
    "Réécriture à droit constant : la clôture de l'exercice est énoncée comme condition et les avances prises en compte sont rattachées directement à la dernière année civile écoulée. Aucune réforme de fond du crédit ni des prêts.",
    "Maintien des avances versées, de leur caractère remboursable sans intérêt et de la référence à la dernière année civile écoulée. L'article 244 quater J reste la cible du renvoi ; les nouveaux dispositifs de prêts ne lui sont pas substitués."
)

add('49 septies YQ', [
    "Pour calculer le crédit d'impôt prévu à l'article 244 quater J du code général des impôts au titre d'une année, les avances remboursables sont prises en compte pour leur montant total dès le premier déblocage des fonds.",
    "Les éléments susceptibles de modifier le montant et les conditions de remboursement de l'avance remboursable sans intérêt sont pris en compte pour établir l'attestation portant calcul du crédit d'impôt. Cette attestation est délivrée à l'établissement de crédit ou à la société de financement par l'organisme mentionné au cinquième alinéa de l'article L. 312-1 du code de la construction et de l'habitation.",
    "Par exception, les éléments ayant modifié le montant et les conditions de remboursement de l'avance peuvent être pris en compte sur l'attestation délivrée par l'organisme mentionné au deuxième alinéa, au plus tard la deuxième année suivant celle de l'émission de l'offre, lorsque les deux conditions suivantes sont réunies : le ou les avis d'imposition des emprunteurs font apparaître, par rapport aux revenus fiscaux de référence déclarés, un écart justifiant une baisse de l'avantage dont ils ont bénéficié ; les emprunteurs ont régularisé cette situation auprès de l'établissement de crédit ou de la société de financement entre le 1er janvier et le 31 mars de l'année suivant celle de l'offre."
],
    "Réécriture à droit constant : l'assiette intégrale dès le premier déblocage est énoncée directement ; la production et la délivrance de l'attestation sont distinguées. Le troisième alinéa présente séparément les deux conditions cumulatives de la régularisation et le délai de prise en compte, sans modifier leur portée. Aucune réforme de fond.",
    "Trois alinéas conservés : le renvoi interne au deuxième alinéa vise toujours l'organisme qui délivre l'attestation. Le cinquième alinéa de L. 312-1 du CCH désigne bien une société de gestion dans le corpus. Fenêtre du 1er janvier au 31 mars de l'année suivant l'offre et limite de la deuxième année suivant son émission maintenues. Le report de prise en compte reste facultatif et réservé à un écart de ressources justifiant une baisse de l'avantage ; aucune extension à une hausse ni modification des anciens prêts."
)

add('49 septies YR', [
    "Le crédit d'impôt prévu à l'article 244 quater J du code général des impôts s'impute sur l'impôt dû après l'imputation des prélèvements non libératoires et des autres crédits d'impôt."
],
    "Réécriture à droit constant : la priorité des prélèvements non libératoires et des autres crédits est rendue explicite par la répétition du terme imputation. Aucune réforme de fond du crédit attaché aux avances sans intérêt.",
    "Ordre d'imputation et renvoi à l'article 244 quater J maintenus. Les fractions, restitutions et reprises des articles 199 ter I et 220 K restent régies par ces articles ; aucune anticipation de leur utilisation n'est introduite."
)

add('49 septies YS', [
    "Pour l'application des articles 199 ter I, 220 K et 244 quater J du code général des impôts, les établissements de crédit et les sociétés de financement mentionnés au I de l'article 244 quater J annexent une déclaration spéciale à leur déclaration de résultat déposée auprès du service des impôts dont ils dépendent." + reuse,
    "Toutefois, les personnes morales passibles de l'impôt sur les sociétés déposent cette déclaration spéciale auprès du comptable de la direction générale des finances publiques du lieu d'imposition défini à l'article 218 A du code général des impôts, avec le relevé de solde de l'exercice mentionné à l'article 360. Pour les sociétés relevant du régime des groupes prévu à l'article 223 A du code général des impôts, la société mère joint les déclarations spéciales des sociétés membres du groupe au relevé de solde relatif au résultat d'ensemble du groupe. Les sociétés du groupe sont dispensées d'annexer leur déclaration spéciale à la déclaration de résultats qu'elles sont tenues de déposer en application du 1 de l'article 223 du même code."
],
    "À droit constant, le débiteur de l'obligation déclarative est désigné sans ambiguïté et les règles de dépôt propres à l'impôt sur les sociétés et aux groupes sont simplifiées. Réforme de fond limitée à la déclaration : réutilisation des informations légalement détenues, suppression de leur ressaisie et droit de correction, sans changement du crédit ou des prêts.",
    "Deux alinéas maintenus ; l'exception de dépôt des personnes morales reste au second. Renvois aux articles 199 ter I, 220 K, 244 quater J, à son I, aux articles 218 A, 223 A, au 1 de l'article 223 et à l'article 360 de la présente annexe conservés. Les états produits par l'organisme gestionnaire à l'article 49 septies YT ne sont pas assimilés à une déclaration souscrite par la banque : réemploi seulement si l'utilisation des mêmes informations est légalement autorisée." + reuse_note
)

add('49 septies YT', [
    "L'organisme mentionné au troisième alinéa de l'article L. 312-1 du code de la construction et de l'habitation transmet au service chargé des grandes entreprises un état relatif au crédit d'impôt en faveur de la première accession à la propriété. Il établit cet état pour chaque établissement de crédit ou société de financement qui est tenu de déposer une déclaration spéciale et qui lui a déclaré des avances remboursables sans intérêt. Il le transmet dans les quatre mois suivant la clôture de l'exercice de cet établissement ou de cette société.",
    "Cet état fait apparaître les éléments suivants :",
    "a) Le montant global des avances remboursables sans intérêt ainsi que des crédits d'impôt dégagés au cours des années antérieures et de l'année concernée ;",
    "b) Le suivi des crédits d'impôt ;",
    "c) Les crédits d'impôt ou fractions de crédit d'impôt reversés ou non imputés en raison du non-respect des conditions d'octroi des avances remboursables mentionnées au I de l'article 244 quater J du code général des impôts, du non-respect des conditions relatives à l'affectation du logement et à ses caractéristiques mentionnées au I du même article, ou des remboursements totaux ou partiels d'avances remboursables sans intérêt intervenant pendant la durée de remboursement de l'avance, ainsi que l'origine du reversement ou de l'arrêt d'imputation du crédit d'impôt."
],
    "Réécriture à droit constant : l'auteur, le destinataire, le périmètre par établissement et le délai de transmission sont exposés en phrases distinctes dans le premier alinéa. Les trois catégories d'informations et toutes les causes de reversement ou de non-imputation restent intégrales ; aucune réforme de fond.",
    "Cinq alinéas et lettres a) à c) conservés. Délai de quatre mois suivant la clôture propre à chaque établissement ou société ; montants des années antérieures et de l'année courante, remboursements totaux ou partiels pendant la durée de remboursement et origine du reversement ou de l'arrêt maintenus. Incohérence préexistante : le troisième alinéa de L. 312-1 du CCH porte, dans le corpus, sur la garantie de l'État ; la société de gestion figure au cinquième alinéa, également visé par 49 septies YQ. Le V de 244 quater J confirme la fonction de l'organisme gestionnaire. Le renvoi au troisième alinéa est conservé et sa correction exige une coordination explicite."
)

add('49 septies Z', [
    "Pour vérifier si l'entreprise respecte le seuil de 40 % prévu au I de l'article 244 quater L du code général des impôts, le rapport est calculé entre :",
    "a. Au numérateur, les recettes provenant des activités mentionnées à l'article 63 du code général des impôts qui ont fait l'objet d'une certification en agriculture biologique au sens du règlement (UE) 2018/848 du Parlement européen et du Conseil du 30 mai 2018 relatif à la production biologique et à l'étiquetage des produits biologiques, et abrogeant le règlement (CE) n° 834/2007 du Conseil ;",
    "b. Au dénominateur, les recettes provenant des activités mentionnées à l'article 63 du même code."
],
    "Réécriture à droit constant : les deux termes du rapport sont identifiés comme numérateur et dénominateur, et la finalité du calcul est exprimée directement. Le seuil, les recettes et la certification biologique restent identiques ; aucune réforme de fond.",
    "Trois alinéas et lettres a. et b. maintenus. Seuil de 40 %, I de l'article 244 quater L, article 63, règlement (UE) 2018/848 du 30 mai 2018 et règlement (CE) n° 834/2007 conservés. Le dénominateur reste limité aux activités de l'article 63, sans extension à toutes les recettes de l'entreprise. Note source lue : coordination de l'article 132-III de la loi n° 2010-1657 du 29 décembre 2010. Cette note historique est conservée comme contexte documentaire, sans être transformée en date de la présente rédaction."
)

add('49 septies ZB', [
    "Le crédit d'impôt prévu à l'article 244 quater L du code général des impôts s'impute sur l'impôt dû après l'imputation des prélèvements non libératoires et des autres crédits d'impôt. La part de ce crédit qui n'a pas pu être imputée est restituée."
],
    "Réécriture à droit constant : l'ordre des imputations est rendu explicite et le droit à restitution est exprimé en désignant la part non imputée. Aucune réforme de fond.",
    "Un alinéa et les deux règles d'imputation puis de restitution conservés. Renvoi à l'article 244 quater L inchangé ; aucune transformation de l'excédent restituable en simple report."
)

add('49 septies ZB bis', [
    "Pour l'application des articles 199 ter K, 220 M et 244 quater L du code général des impôts, les entreprises souscrivent une déclaration spéciale conforme à un modèle établi par l'administration." + reuse,
    "Les personnes morales passibles de l'impôt sur les sociétés déposent cette déclaration spéciale auprès du comptable de la direction générale des finances publiques du lieu d'imposition défini à l'article 218 A du code général des impôts, avec le relevé de solde mentionné à l'article 360. Pour les sociétés relevant du régime des groupes prévu à l'article 223 A du code général des impôts, la société mère dépose les déclarations spéciales pour le compte des sociétés du groupe. Elle les joint au relevé de solde relatif au résultat d'ensemble du groupe, y compris la déclaration qui la concerne.",
    "Les autres entreprises joignent la déclaration spéciale à la déclaration annuelle de résultat qu'elles sont tenues de déposer en application de l'article 53 A du code général des impôts.",
    "Les sociétés de personnes et les groupements assimilés, y compris les groupements agricoles d'exploitation en commun, qui ne sont pas tenus de déposer la déclaration annuelle de résultat prévue à l'article 53 A du code général des impôts adressent la déclaration spéciale mentionnée au premier alinéa au service des impôts des entreprises dont ils relèvent. Ils l'adressent dans le même délai que la déclaration de revenus des associés lorsque ceux-ci sont des personnes physiques, ou que la déclaration annuelle de résultat lorsque les associés sont des personnes morales tenues de la déposer en application de l'article 53 A du même code.",
    "Les associés personnes physiques joignent à leur déclaration de revenus une déclaration spéciale indiquant les quotes-parts de crédit d'impôt issues de leur participation dans les groupements mentionnés au quatrième alinéa.",
    "Les associés personnes morales joignent cette même déclaration spéciale à leur déclaration annuelle de résultat lorsqu'ils sont tenus de la déposer en application de l'article 53 A du code général des impôts.",
    "Les exploitants individuels qui ne sont pas tenus de déposer la déclaration annuelle de résultat prévue à l'article 53 A du code général des impôts joignent la déclaration spéciale mentionnée au premier alinéa à leur déclaration de revenus."
],
    "À droit constant, les obligations sont réparties plus clairement entre sociétés à l'impôt sur les sociétés, groupes, autres entreprises et associés, sans déplacer les sept alinéas. Les délais conditionnés par la qualité des associés sont explicités. Réforme de fond procédurale : réemploi des données légalement détenues sans nouvelle saisie des informations exactes, avec correction possible et maintien des dépôts.",
    "Sept alinéas conservés, notamment les renvois au premier alinéa et les déclarations distinctes des associés aux cinquième et sixième. La mention des groupements susvisés est explicitée par le quatrième alinéa, sans en élargir le champ. Maintien des groupements agricoles d'exploitation en commun, des quotes-parts, des cas sans déclaration annuelle de résultat et des délais liés aux déclarations des associés. La source ne tranche pas le cas d'associés soumis à des échéances différentes : cette difficulté préexistante doit être contrôlée, sans créer ici une nouvelle échéance. Renvois aux articles 199 ter K, 220 M, 244 quater L, 218 A, 223 A, 53 A et 360 conservés." + reuse_note
)

training_note = (
    " Les articles 199 ter L, 220 N et 244 quater M ne figurent pas dans le fichier impots.json du corpus fourni, "
    "alors que les dispositions réglementaires du lot les visent encore. Contrôler leur état et le champ temporel "
    "du crédit, notamment pour les créances et obligations antérieures ; cette absence ne fonde ni une "
    "abrogation implicite des dispositions du lot ni une réouverture de droits."
)

add('49 septies ZC', [
    "Pour l'application de l'article 244 quater M du code général des impôts, sont des chefs d'entreprise les exploitants individuels, les gérants, les présidents, les administrateurs, les directeurs généraux et les membres du directoire."
],
    "Réécriture à droit constant : la définition est formulée directement, en conservant chacune des six catégories de dirigeants. Aucune réforme de fond ni extension du crédit d'impôt formation.",
    "Liste intégrale et renvoi à l'article 244 quater M conservés ; aucune condition de fonction principale ou de rémunération ajoutée." + training_note
)

add('49 septies ZD', [
    "Les formations ouvrent droit au crédit d'impôt lorsqu'elles relèvent des dispositions relatives à la formation professionnelle continue mentionnées à l'article L. 6313-1 du code du travail, sont réalisées dans les conditions prévues à l'article L. 6353-1 du même code et donnent lieu à des dépenses admises en déduction du bénéfice imposable."
],
    "Réécriture à droit constant : les trois conditions cumulatives d'éligibilité sont coordonnées dans une phrase directe, en distinguant le champ de la formation, ses conditions de réalisation et la déductibilité des dépenses. Aucune réforme de fond.",
    "Un alinéa et renvois à L. 6313-1 et L. 6353-1 du code du travail maintenus. Le corpus confirme l'énumération des actions de développement des compétences à L. 6313-1 et l'exigence de convention à L. 6353-1. La formulation historique formation professionnelle continue reste conservée sans élargir les formations éligibles. Note source lue : article 24-VII-13° de la loi n° 2018-771 du 5 septembre 2018 ; il s'agit d'une coordination historique, sans date nouvelle d'entrée en vigueur." + training_note
)

add('49 septies ZE', [
    "Pour l'application du I de l'article 244 quater M du code général des impôts, le taux horaire du salaire minimum de croissance retenu est celui en vigueur au 31 décembre de l'année au titre de laquelle le crédit d'impôt est calculé."
],
    "Réécriture à droit constant : le taux de référence est introduit comme la donnée à retenir pour le calcul, en conservant sa date d'appréciation. Aucun montant de SMIC ni changement de fond n'est ajouté.",
    "Date du 31 décembre et année au titre de laquelle le crédit est calculé maintenues ; le taux n'est ni celui du jour de formation ni une moyenne annuelle. Renvoi au I de l'article 244 quater M inchangé." + training_note
)

add('49 septies ZF', [
    "Le plafond du crédit d'impôt prévu à l'article 244 quater M du code général des impôts s'apprécie par entreprise et par année civile, y compris pour les sociétés de personnes. Lorsque l'exercice est clos en cours d'année, le crédit d'impôt est calculé à partir des heures que le ou les dirigeants ont consacrées à la formation au cours de la dernière année civile écoulée."
],
    "Réécriture à droit constant : l'unité d'application du plafond et la période de calcul sont énoncées directement. La règle conserve les sociétés de personnes et le cumul des heures du ou des dirigeants ; aucune réforme de fond.",
    "Un alinéa conservé. Plafond par entreprise, et non par dirigeant ou associé, apprécié par année civile ; dernière année civile écoulée maintenue en cas de clôture en cours d'année. Aucun montant ni nouveau plafond n'est introduit." + training_note
)

add('49 septies ZG', [
    "Le crédit d'impôt prévu à l'article 244 quater M du code général des impôts s'impute sur l'impôt dû après l'imputation des prélèvements non libératoires et des autres crédits d'impôt."
],
    "Réécriture à droit constant : la succession des imputations est exprimée explicitement. Le crédit formation conserve son rang ; aucune réforme de fond ni règle supplémentaire de restitution.",
    "Renvoi à l'article 244 quater M et ordre d'imputation conservés ; aucun report ni remboursement nouveau n'est créé." + training_note
)

add('49 septies ZH', [
    "Pour l'application des articles 199 ter L, 220 N et 244 quater M du code général des impôts, les entreprises déclarent les réductions et crédits d'impôt selon le format établi par l'administration. Elles effectuent cette déclaration dans les mêmes délais que la déclaration annuelle de résultat qu'elles sont tenues de souscrire en application des articles 53 A et 223 du même code." + reuse,
    "La société mère d'un groupe au sens de l'article 223 A du code général des impôts déclare les réductions et crédits d'impôt pour le compte des sociétés du groupe, y compris ceux qui la concernent. Elle effectue cette déclaration lors du dépôt de la déclaration relative au résultat d'ensemble du groupe."
],
    "À droit constant, le format et le délai sont exposés séparément et l'obligation de la société mère est rendue directe. Réforme de fond strictement procédurale : réutilisation des données légalement détenues et correction possible, sans nouvelle saisie des informations exactes. Cette mesure ne rétablit pas un crédit dont le champ temporel aurait pris fin.",
    "Deux alinéas conservés. La source vise les réductions et crédits d'impôt au pluriel malgré l'intitulé propre au crédit formation : cette portée n'est pas réduite silencieusement. Maintien des renvois aux articles 199 ter L, 220 N, 244 quater M, 53 A, 223 et 223 A et de la déclaration de la société mère pour elle-même." + training_note + reuse_note
)

assert len(drafts) == len(sources) == 24
answer = []
for source in sources:
    entry = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    entry.update(drafts[source['number']])
    entry['status'] = 'rewrite_draft'
    answer.append(entry)

Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles, {sum(len(a["proposed_xml"]) for a in answer)} caractères de texte proposé')
