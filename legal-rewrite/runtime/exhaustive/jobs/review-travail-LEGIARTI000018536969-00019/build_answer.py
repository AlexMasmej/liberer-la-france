import json
import html
import re
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
answer = []

def base(s):
    return {k: s[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}

def replace_once(text, old, new):
    assert text.count(old) == 1, (old, text.count(old))
    return text.replace(old, new, 1)

def effect(kind, measure_id, description, before, after, unit,
           affected_population, conditions_and_transition,
           replacement_or_new_burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit,
                affected_population=affected_population,
                conditions_and_transition=conditions_and_transition,
                replacement_or_new_burdens=replacement_or_new_burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)

# D1272-5 : le même document que D1272-1, sans réintroduction des données dispensées.
s = sources[0]
a = base(s)
p = s['previous_draft']['proposed_xml']
p = replace_once(p,
    "Il ne donne lieu ni à une seconde transmission ni à une nouvelle saisie des informations exactes et à jour déjà légalement disponibles.",
    "Il ne donne lieu ni à une seconde transmission ni à une nouvelle saisie des informations exactes et à jour déjà légalement disponibles auprès de l'organisme gestionnaire. Les dispenses prévues aux articles D. 1272-1 et D. 1272-4 s'appliquent à l'ensemble de ses mentions ; seuls les éléments manquants ou modifiés nécessaires sont complétés. L'employeur peut corriger les informations réutilisées, sans attestation de non-changement.")
p = replace_once(p,
    "b) La durée de la période d'essai, si un essai est stipulé ;",
    "b) La durée de la période d'essai éventuellement stipulée, uniquement lorsque la déclaration tient lieu de contrat de travail. Cette durée n'est pas déclarée lorsque les clauses d'un contrat distinct signé s'appliquent dans les conditions de l'article D. 1272-4 ;")
p = replace_once(p,
    "g) Le taux de cotisation au titre des accidents du travail et, le cas échéant, celui de prévoyance, sans nouvelle indication des taux déjà connus de l'organisme gestionnaire ;",
    "g) Le taux de cotisation au titre des accidents du travail et des maladies professionnelles, uniquement lorsque plusieurs taux s'appliquent dans l'établissement et que le taux applicable au salarié n'est pas déjà connu de l'organisme gestionnaire ; le taux de cotisation de prévoyance, uniquement s'il est spécifique au salarié et n'est pas déjà connu de cet organisme ;")
p = replace_once(p,
    "Les droits antérieurs et les avantages ouverts aux situations futures éligibles dans le contrat unique sont maintenus.",
    "Elles ne modifient ni les échéances des formalités d'embauche légalement maintenues, ni la remise au salarié prévue à l'article D. 1272-1, ni les taux des cotisations ou les garanties de prévoyance. Les droits antérieurs et les avantages ouverts aux situations futures éligibles de même objet dans le contrat unique sont maintenus sous leurs autres conditions propres.")
a.update(
    proposed_xml=p,
    reason="Réforme de fond coordonnée du document d'identification : conservation de la fusion avec D1272-1, du réemploi des données et de la dispense de seconde signature déjà retenus. La seconde passe retire aussi l'indication de l'essai lorsqu'un contrat distinct signé en contient les clauses, ainsi que l'indication des taux AT-MP uniformes et des taux de prévoyance non spécifiques au salarié. Ces dispenses reprennent celles de D1272-1 proposé : elles constituent la même mesure et ne sont pas comptées comme des suppressions indépendantes. À droit constant, demeurent l'identification utile, la distinction des affiliations générale et agricole, le salaire, le temps de travail, la qualification et l'information du salarié. Le terme du CDD n'est conservé que pour les contrats antérieurs ; aucun nouveau CDD ou renouvellement n'est autorisé.",
    review_notes="Le renvoi source au « 2° de D1272-1 » est incohérent avec le texte actuel : ce 2° contient les mentions d'emploi, non l'institution d'un volet distinct. Le rattachement est expressément rectifié à la déclaration entière, sans second document. Le 1° a) conserve les mentions de R1221-1 dans leur champ propre, avec ses dispenses proposées : pas de réintroduction du code APE, de la durée de l'essai dans la DPAE ni d'une durée d'emploi pour les contrats uniques. Les données d'employeur et les données agricoles nécessaires aux cotisations, affiliations et santé au travail ne sont pas effacées lorsqu'elles manquent. La durée de l'essai, si elle demeure une clause du document tenant lieu de contrat, reste distinguée de son indication dans la DPAE ; l'essai nouveau est de trois mois sans renouvellement selon la coordination travail. Les taux conditionnels du 2° g) sont alignés sur D1272-1 proposé, sans modification de taux ou de garantie. D1272-4 proposé préserve aussi la substitution des clauses des anciens CDD valables et du temps partiel. Les sources et propositions du fichier de cibles sont distinguées. Les sources locales D1272-2, D1272-3, CSS D133-13-1 et L133-5-6 ont été lues : les exclusions du guichet spectacle et les différents dispositifs, notamment agricoles, restent à leur champ ; l'intégration ne dispense pas des échéances préalables légalement maintenues ni de la remise au salarié. Aucun nouveau renvoi normatif à une cible absente du fichier n'est créé. Les articles de préavis et d'indemnité requis ont été examinés comme coordinations indirectes ; le présent article n'ajoute aucun barème ni aucune procédure de rupture. Aucune économie nationale ni baisse de cotisation n'est chiffrée.",
    status='rewrite_draft',
    change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=[
        "L'obligation de renseigner à nouveau les mentions exactes et à jour déjà légalement disponibles auprès de l'organisme gestionnaire est écartée.",
        "La déclaration de la durée de l'essai lorsque cette clause figure dans un contrat distinct signé valablement est supprimée.",
        "L'indication systématique du taux AT-MP uniforme dans l'établissement et du taux de prévoyance non spécifique au salarié est supprimée.",
        "La seconde signature du salarié sur la déclaration, lorsqu'il a déjà signé un contrat distinct dans les formes requises, est supprimée."
    ],
    substantive_impact=dict(
        version=1, classification='coordination_only',
        assessment="Par rapport à la source officielle entière, les mentions obligatoires deviennent conditionnelles et la double signature est écartée en présence d'un contrat signé. La seconde passe aligne expressément l'essai et les taux sociaux sur les dispenses du D1272-1 proposé. Comme il s'agit du même document et de la même réforme d'identification, aucun second gain autonome n'est attribué à ce règlement d'exécution ; aucun prélèvement n'est diminué ici.",
        scope_limitations="L'identification, les données réellement manquantes, les affiliations agricoles, l'information contractuelle et les échéances préalables utiles demeurent. Les propositions des cibles ne sont pas du droit en vigueur. L'ensemble des procédures d'embauche et des coûts des cinq codes n'est pas évalué ; le gain de temps propre à cette coordination n'est pas quantifié.",
        new_burdens_review="Aucune charge nouvelle n'est identifiée : pas de formulaire, registre, dépôt de contrat ou attestation de remplacement. La correction des données est une faculté ; compléter les seules mentions manquantes maintient une partie de l'obligation source. La signature du salarié reste requise si le document tient lieu de contrat. Ces constats ne démontrent pas un solde chiffré pour l'ensemble des codes.",
        effects=[
            effect('coordination','identification-salarie-sans-doublons',
                "Intégrer le volet dans le document unique et appliquer les dispenses communes sans compter une seconde suppression.",
                "D1272-5 énumère inconditionnellement ses mentions en visant un volet prétendument prévu au 2° de D1272-1.",
                "Le volet est celui de D1272-1 ; seules les données nécessaires manquantes ou modifiées sont complétées, sans ressaisie des données déjà disponibles.",
                'legal_duty',"Employeurs et salariés concernés par le document d'identification dans le champ de ces dispositifs.",
                "Transmissions après l'entrée en vigueur de la loi proposée, même pour un contrat antérieur ; aucun volet déjà établi n'est refait.",
                "Aucun second document ni attestation ; données d'identification et échéances maintenues dans leur champ.",
                "Le volet d'identification du salarié prévu au 2° de l'article D. 1272-1 comporte les mentions suivantes :",
                "Les dispenses prévues aux articles D. 1272-1 et D. 1272-4 s'appliquent à l'ensemble de ses mentions ; seuls les éléments manquants ou modifiés nécessaires sont complétés."),
            effect('coordination','identification-salarie-sans-doublons',
                "Empêcher D1272-5 de rétablir l'indication de l'essai dispensée dans D1272-1 lorsque le contrat distinct la contient.",
                "La durée de l'essai figure obligatoirement au 2° b), sans dispense liée au contrat déjà signé.",
                "Elle ne figure dans ce volet que lorsqu'il tient lieu de contrat ; les clauses du contrat distinct signé dispensent de la déclarer.",
                'legal_duty',"Employeurs utilisant le dispositif avec un contrat de travail distinct déjà signé.",
                "Transmissions nouvelles, contrats anciens compris ; durée substantielle de l'essai et information du salarié non supprimées.",
                "Aucun dépôt du contrat ou justificatif nouveau exigé ; même dispense que D1272-1 proposé.",
                "La durée de la période d'essai",
                "Cette durée n'est pas déclarée lorsque les clauses d'un contrat distinct signé s'appliquent dans les conditions de l'article D. 1272-4"),
            effect('coordination','identification-salarie-sans-doublons',
                "Aligner les taux à renseigner et la signature sur les conditions communes du document unique.",
                "Le taux accidents du travail, le cas échéant le taux prévoyance, et les deux signatures sont prescrits sans les dispenses proposées.",
                "Seuls les taux AT-MP multiples et de prévoyance spécifiques non connus sont indiqués ; un contrat distinct signé dispense d'une seconde signature du salarié.",
                'legal_duty',"Employeurs du dispositif, notamment avec un taux AT-MP uniforme ou un contrat distinct déjà signé.",
                "Transmissions postérieures à l'entrée en vigueur, sans réfection ; taux de prélèvement et garanties inchangés.",
                "Pas d'attestation ou déclaration substitutive ; la signature contractuelle initiale est maintenue.",
                "Le taux de cotisations accidents du travail et, le cas échéant, le taux prévoyance",
                "La signature d'un contrat distinct dans les conditions de l'article D. 1272-4 dispense le salarié d'une seconde signature."),
            effect('coordination','contrat-unique-duree-indeterminee',
                "Réserver les mentions de terme aux anciens CDD sans recréer ce régime pour les embauches nouvelles.",
                "La date de fin est prévue pour tout emploi à durée déterminée, sans transition.",
                "Seul le CDD conclu avant la réforme conserve une date de fin d'emploi ; aucun nouveau CDD ni renouvellement après réforme.",
                'regime',"Salariés et employeurs privés du dispositif ; les régimes publics ne sont pas assimilés.",
                "Distinction à la date d'entrée en vigueur de la loi instituant le contrat unique ; anciens droits conservés.",
                "Aucune formalité nouvelle ; une durée d'aide, de mission ou de formation ne devient pas un terme d'emploi.",
                "La date de fin d'emploi s'il s'agit d'un emploi à durée déterminée",
                "La présente mention ne permet aucun nouveau contrat à durée déterminée ni renouvellement d'un tel contrat après cette entrée en vigueur")
        ]))
answer.append(a)

# R2262-1 : le brouillon contient déjà la coupe justifiée ; l'accès utile reste nécessaire.
s = sources[1]
a = base(s)
a.update(
    proposed_xml=s['previous_draft']['proposed_xml'],
    reason="Conservation de la réforme de fond du brouillon : suppression du cumul obligatoire entre exemplaire sur le lieu de travail et publication intranet. L'un des supports suffit s'il assure effectivement l'accès aux textes à jour. Après examen supplémentaire, aucune autre coupe n'est retenue : l'information individuelle identifie les accords applicables au salarié, tandis que l'exemplaire accessible permet d'en connaître le contenu pendant l'emploi ; ces deux fonctions ne sont pas des doublons. La priorité des modalités conventionnelles, l'actualisation et l'accès effectif sont maintenus à droit constant. Le maintien de cette proposition ne constitue ni une nouvelle réduction par rapport au brouillon ni une validation juridique.",
    review_notes="L2262-5 entier a été lu dans le corpus local : le règlement reste supplétif aux modalités fixées par convention de branche ou accord professionnel. R1221-34 vise les accords applicables au 13°, distinct de son 10° sur la rupture ; R1221-35 place la remise de l'information du 13° au plus tard un mois après l'embauche, et non au septième jour applicable à d'autres mentions. Sa proposition dispense déjà d'un second document si l'information complète a été remise individuellement dans les formes et délais requis : le 1° du présent article ne rétablit pas cette répétition. Le support choisi doit donner accès aux accords propres à l'entreprise ; un simple renvoi à une page publique incomplète n'y satisfait pas. L'accès numérique est une faculté de substitution, sans création d'un intranet ni achat imposé au salarié. Il reste nécessaire de mettre un exemplaire à jour à disposition lorsque tous n'ont pas un accès numérique effectif. Les règles de préavis, d'indemnité et de contrat unique des cibles sont indirectes ; ce règlement d'information ne modifie aucune de leurs conditions d'ancienneté, de notification ou de transition. Il ne rétablit aucune transmission CPPNI, délai de négociation ou procédure collective supprimés ailleurs. La date du 1er novembre 2023 figurant dans les notes de R2262-1 et des cibles est historique ; elle n'est pas la date de la réforme proposée. Les exigences européennes d'information individuelle et de consultation restent à coordonner dans leurs textes propres, sans conformité générale présumée. Aucun nouveau renvoi à une cible absente du fichier n'est ajouté.",
    status='rewrite_draft', change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=["L'obligation de cumuler systématiquement un exemplaire sur le lieu de travail et une publication intranet est supprimée lorsque l'un des supports assure l'accès effectif aux textes à jour."],
    substantive_impact=dict(
        version=1, classification='material_reduction',
        assessment="La source officielle entière impose le cumul des 2° et 3° dès que l'entreprise possède un intranet. La proposition rend les supports alternatifs, ce qui supprime une duplication de publication et d'actualisation. Cette réduction était déjà acquise dans le brouillon ; la seconde passe n'en ajoute pas une autre, car l'information individuelle et la disponibilité du texte répondent à des besoins distincts.",
        scope_limitations="Le bénéfice est celui des entreprises soumises aux modalités supplétives disposant d'un intranet ; les modalités conventionnelles autonomes ne sont pas supprimées. L'obligation d'actualiser et d'assurer l'accès effectif subsiste. Aucun coût moyen ni solde de complexité de l'ensemble des codes n'est démontré.",
        new_burdens_review="Aucune charge nouvelle n'est identifiée : pas d'intranet, compte, équipement individuel, registre de lecture ou attestation créés. L'accès gratuit et effectif conditionne seulement le choix facultatif d'un support numérique à la place du support déjà requis. L'information individuelle reste celle de R1221-34 et R1221-35, avec leurs dispenses proposées de seconde remise.",
        effects=[effect('obligation_merged','information-collective-support-unique',
            "Un support accessible suffit pour les accords collectifs ; leur publication en double cesse d'être obligatoire.",
            "À défaut de modalités conventionnelles différentes, l'employeur tient un exemplaire à jour sur le lieu de travail et le publie aussi sur l'intranet lorsque celui-ci existe.",
            "Un exemplaire papier ou numérique effectivement accessible à tous sur le lieu de travail suffit, y compris dans une entreprise dotée d'un intranet ; l'information individuelle reste due.",
            'legal_duty',"Employeurs relevant des modalités réglementaires supplétives et salariés de ces entreprises.",
            "Application à compter de l'entrée en vigueur de la loi proposée ; modalités conventionnelles autonomes maintenues.",
            "Aucun second support obligatoire, équipement ou compte nouveau imposé ; maintien d'un texte à jour effectivement accessible.",
            "Met sur l'intranet, dans les entreprises dotées de ce dernier, un exemplaire à jour des textes.",
            "Lorsque la mise à disposition est assurée sur un autre support conformément au 2°, aucune publication supplémentaire sur l'intranet n'est exigée.")]))
answer.append(a)

# R2312-8 : conserver la grille complète, y appliquer les coupes et les coordinations.
s = sources[2]
a = base(s)
p = s['previous_draft']['proposed_xml']
p = replace_once(p,
    "a) Évolution des effectifs par type de contrat, âge et ancienneté :",
    "a) Évolution des effectifs par type de contrat. Une ventilation générale supplémentaire par âge ou ancienneté n'est pas exigée au titre du présent a) ; les analyses et ventilations prévues aux autres rubriques demeurent applicables :")
p = replace_once(p,
    "- pour l'année antérieure et l'année en cours, bilan agrégé des actions du plan de formation, des bilans de compétences et des validations des acquis de l'expérience réalisés, avec les effectifs concernés répartis par catégorie socioprofessionnelle et sexe. Une liste distincte action par action n'est pas exigée ;",
    "- pour l'année antérieure et l'année en cours, bilan agrégé des actions du plan de développement des compétences, des bilans de compétences et des validations des acquis de l'expérience réalisés, avec les effectifs concernés répartis par catégorie socioprofessionnelle et sexe. Pour les périodes où elle était applicable, l'ancienne dénomination de plan de formation désigne le dispositif correspondant. Une liste distincte action par action n'est pas exigée ;")
p = replace_once(p,
    "- pour les mêmes années et pour chaque type de congé, nombre de congés accordés, durée totale et coût total des congés individuels de formation, de bilan de compétences, de validation des acquis de l'expérience et pour enseignement. Le détail de leur objet, des conditions de leur octroi ou de leur report et des résultats obtenus n'est pas exigé au titre de cette rubrique ;",
    "- pour les mêmes années, informations agrégées sur la durée et le coût des congés de formation, notamment de transition professionnelle, de bilan de compétences, de validation des acquis de l'expérience et pour enseignement, ainsi que des congés individuels de formation antérieurement accordés lorsque les périodes couvertes l'exigent. Aucun décompte supplémentaire du nombre de congés par type ni relevé individuel de leur objet, des conditions de leur octroi ou de leur report et des résultats obtenus n'est exigé au titre de cette rubrique ;")
p = replace_once(p,
    "- nombre de salariés bénéficiaires de l'abondement mentionné à l'avant-dernier alinéa du II de l'article L. 6315-1 et sommes versées à ce titre ;",
    "- nombre de salariés bénéficiaires de l'abondement prévu au II de l'article L. 6315-1, dans les conditions de l'article L. 6323-13, et sommes versées à ce titre ;")
p = replace_once(p,
    "- nombre de salariés ayant bénéficié de l'entretien professionnel mentionné au I de l'article L. 6315-1 ;",
    "- nombre de salariés ayant bénéficié de l'entretien de parcours professionnel mentionné au I de l'article L. 6315-1 ou, pour les périodes soumises aux dispositions antérieures, de l'entretien professionnel correspondant ;")
p = replace_once(p,
    "iii - à l'information et à la formation prévues aux articles L. 4154-2 et L. 4154-4 pour les salariés relevant de leur champ. La protection des titulaires d'anciens CDD est maintenue ; les salariés en contrat unique affectés aux mêmes postes ou missions bénéficient des protections de même objet ;",
    "iii - à l'information et à la formation prévues aux articles L. 4154-2 et L. 4154-4, dans leur champ propre. Les titulaires d'anciens CDD conservent leurs protections ; les salariés temporaires, y compris à durée indéterminée, et les salariés en contrat unique qui relèvent de ces dispositions bénéficient des garanties qu'elles prévoient ;")
p = replace_once(p,
    "a) Identification des postes d'émissions directes de gaz à effet de serre provenant des sources fixes et mobiles nécessaires à l'activité de l'entreprise, dites « émissions du scope 1 ». Le volume de ces émissions est évalué lorsque l'entreprise dispose de cette information.",
    "a) Informations déjà disponibles sur les postes d'émissions directes de gaz à effet de serre provenant des sources fixes et mobiles nécessaires à l'activité de l'entreprise, dites « émissions du scope 1 », et sur leur volume. Aucun inventaire distinct de ces postes ni calcul de leur volume n'est à établir au seul titre du présent a). Les obligations autonomes d'établissement des bilans mentionnés au b) demeurent applicables.")
p = replace_once(p,
    "Les informations et analyses figurant déjà dans des documents exacts, à jour et légalement accessibles aux membres du comité sont mises à disposition par un accès direct et identifiable dans la base, sans transcription ni rapport distinct. Les conditions d'accès, d'actualisation, d'analyse et de confidentialité prévues aux articles L. 2312-18, L. 2312-36 et R. 2312-10 à R. 2312-14 demeurent applicables. Cette faculté ne dispense pas de fournir les informations manquantes nécessaires à l'exercice des compétences du comité.",
    "Les informations et analyses communes à plusieurs rubriques ne sont mises à disposition qu'une fois. Celles qui figurent déjà dans des documents exacts, à jour et légalement accessibles aux destinataires de la base sont mises à disposition par un accès direct et identifiable dans la base, sans transcription ni rapport distinct. Ce réemploi n'impose pas de support informatique lorsque le support papier est autorisé. Les conditions d'accès, d'actualisation, d'analyse et de confidentialité prévues aux articles L. 2312-18, L. 2312-36 et R. 2312-10 à R. 2312-14 demeurent applicables. Les bilans et informations légalement requis, notamment sur les formations entreprises à l'issue des entretiens de parcours professionnel et sur les périodes de reconversion, restent accessibles dans les conditions de ces textes et de l'article L. 2312-26. Les dispenses de relevés systématiques du présent article ne suppriment pas la communication des informations manquantes nécessaires à une consultation utile du comité ; elles ne peuvent être contournées par la reconstitution automatique des mêmes relevés sous une autre présentation.")
p = replace_once(p,
    "Les informations relatives aux aides, réductions d'impôt, exonérations ou réductions de cotisations, crédits d'impôt, droits à formation, congés et épargne salariale n'instituent aucune condition supplémentaire pour en bénéficier.",
    "Les informations relatives aux aides, réductions d'impôt, exonérations ou réductions de cotisations, crédits d'impôt, droits à formation, abondements, congés, épargne salariale et concours de mécénat n'instituent aucune condition supplémentaire pour en bénéficier. L'allègement du contenu de la base n'emporte aucune suppression de ces avantages.")
# Normaliser uniquement les balises vides, sans modifier les cellules ni les subdivisions.
p = p.replace('<br />', '<br/>')
p = re.sub(r'<td([^>]*)\s/>', r'<td\1></td>', p)
a['proposed_xml'] = p
answer.append(a)

# Métadonnées du tableau et contrôles des cibles ajoutés ci-dessous.
a.update(
    reason="Réforme de fond de la grille supplétive, sans supprimer la BDESE ni les consultations. Les coupes déjà retenues sont conservées : série mensuelle des effectifs, justification particulière du temps partiel, liste de formation action par action, relevé individuel des congés de formation, recensement des partenariats hors sous-traitance et doubles reproductions. La seconde passe retire en outre la ventilation générale des effectifs par âge et ancienneté, redondante avec les analyses ciblées qui restent exigées, et l'inventaire systématique distinct des postes d'émissions directes pour les entreprises qui ne disposent pas déjà de ces informations ; les bilans environnementaux dus sur un fondement autonome demeurent. Le décompte supplémentaire des congés par type créé par le brouillon est également retiré. Les dix rubriques et les subdivisions maintenues restent intégralement rédigées. Les informations essentielles sur les rémunérations, aides, égalité professionnelle, handicap, santé, sécurité et sous-traitance sont conservées ; les documents existants accessibles peuvent servir sans transcription. À droit constant et par coordination, les noms des dispositifs de formation sont actualisés avec leur régime historique ; les catégories de CDD ne valent que pour les contrats antérieurs et les avantages restent accessibles aux situations futures de même objet dans le contrat unique.",
    review_notes="Source officielle et précédent brouillon lus en entier, y compris les 45 lignes du tableau et sa note environnementale. La grille complète conserve les dix rubriques, lettres et i à iv ; aucune cellule maintenue n'est remplacée par un résumé. Les seuils de moins de 300 salariés, moins de 26 ans pour l'insertion et l'alternance, plus de 16 ans pour les stagiaires et les douze derniers mois pour les journées d'intérim sont maintenus. Le retrait de la ventilation générale par âge et ancienneté au 1° A a ne retire ni l'analyse par âge, qualification et ancienneté du 2° A, ni l'âge du bilan d'alternance. Les comptes agrégés de congés restent limités à la durée et au coût : aucun nouvel état nominatif, ventilation supplémentaire ou décompte du nombre de congés par type n'est créé. L2312-18, L2312-21, L2312-26 source et proposition, L2312-27, L2312-36 et R2312-10 à R2312-14 ont été lus dans le corpus fourni : les droits d'accès de tous leurs destinataires, la périodicité légale, les deux années antérieures, l'année en cours et les perspectives des trois années suivantes demeurent. Une série annuelle ne dispense pas d'une information ponctuelle nécessaire à la consultation ; aucune reconstitution générale systématique des relevés supprimés n'est permise. Les thèmes légaux de la formation, de la reconversion et de l'environnement ne sont pas abrogés. La faculté de ne pas recopier des documents accessibles coordonne surtout L2312-18 et R2312-14 déjà existants ; elle n'est pas présentée comme une suppression autonome supplémentaire de rapport. Le support papier autorisé par R2312-12 reste possible. Le 8° se limite à la sous-traitance prévue par L2312-36, sans fermer une consultation justifiée par un autre fondement. Les rubriques d'égalité et leur stratégie, avec indicateurs, coûts et calendrier, sont maintenues ; R2242-2 a été lu. Le 10° C a ne supprime que l'inventaire réglementaire automatique propre à cette grille : les informations disponibles restent communiquées, ainsi que celles nécessaires à une consultation utile ; le 10° C b et la mise en perspective au niveau de l'entreprise exigée par la note (1) sont conservés. Les renvois au code de l'environnement et à l'article 244 de la loi de finances pour 2021 ne sont pas abrogés ; leurs champs propres ne sont pas étendus et leur texte extérieur n'est pas présenté comme réécrit. Les contrôles environnementaux, la prévention et les obligations européennes d'information et de consultation restent distincts ; leur conformité globale n'est pas présumée. Incohérences de vocabulaire source identifiées : plan de formation et entretien professionnel ont été rapprochés explicitement des dénominations actuelles après lecture de L2312-26, L6315-1 et de ses transitions ; les anciens dispositifs restent renseignés pour les années couvertes. Le congé spécifique de transition professionnelle a été vérifié dans L6323-17-1 et L6323-17-5 entiers ; aucun nouveau renvoi à ces articles n'est inséré. L6361-1, L6323-13 et L6362-4 ont été lus et leurs renvois sont conservés : L6323-13 contient bien le contrôle de l'abondement correctif, ce n'est pas un renvoi à supprimer. Dans L6315-1 actuel, l'avant-dernier alinéa du II correspond bien à l'abondement ; le renvoi est stabilisé au II et à ses conditions de L6323-13, sans changer seuil, droit ni sommes. L2241-6 actuel porte sur la périodicité de renégociation des accords de branche : sa mention ne crée aucune négociation ni transmission supplémentaire. L4142-2 proposé et L4154-4 officiel ont aussi été lus pour délimiter le iii : le premier conserve les anciennes situations de CDD à risques et protège les situations de même objet dans le contrat unique ; le second concerne les seuls intérimaires qualifiés intervenant pour des travaux urgents de sécurité. Aucune formation renforcée générale pour tous les CDI n'est inventée. Les propositions L4143-1 et L4154-2 des cibles sont examinées séparément du droit en vigueur. Le 3° c décrit les impôts effectivement applicables et ne crée aucun IS annuel, CVAE ni contribution de remplacement ; les réserves conservées et les crédits ne sont pas taxés par une obligation d'information. L232-6 et L225-115 du code de commerce, déjà visés par la source mais non fournis en entier parmi les cibles, restent des coordinations extérieures à contrôler dans leur champ propre ; aucun contenu nouveau ne leur est attribué. Les compléments légaux d'égalité concernant les instances dirigeantes dans L2312-18 et L2312-36 restent applicables même si la grille source de 2024 ne les détaille pas. Renvois ajoutés par rapport à la source officielle et absents des cibles de reference-targets : L2312-36 et R2312-10 à R2312-14, déjà présents dans le brouillon, ainsi que L2312-26 désormais explicité. Tous ont été lus en entier dans le corpus local ; pour L2312-26, sa proposition et sa note d'entrée en vigueur du 1er janvier 2026 ont également été examinées. Aucun de ces renvois ne remplace le contenu maintenu du tableau. Aucun rendement, coût national, économie d'aide, réduction de crédit ou financement de l'IS n'est déduit de cette grille. Aucune des vérifications effectuées ne constitue une relecture par un juriste.",
    benefit_review="L'article est une grille d'information, non le fondement d'un impôt ou d'une condition générale d'accès aux avantages. Le 7° A conserve toutes les aides et avantages financiers de l'Union, de l'État, des collectivités, de leurs établissements et des organismes privés de service public, ainsi que leur utilisation ; les conditions de versement et d'emploi sont celles de chaque aide, sans condition nouvelle de BDESE. Les réductions d'impôt du 7° B, exonérations et réductions de cotisations du 7° C, crédits d'impôt du 7° D et concours de mécénat du 7° E demeurent intégralement dans leur champ fiscal ou social ; aucune taxe correspondante n'est abolie par le présent article et aucun avantage n'est retiré au prétexte d'une autre réforme fiscale. Le 5° conserve les activités sociales et culturelles, leur contribution et le mécénat ; le 4° c conserve intéressement et participation ; le 6° B conserve actions d'épargne salariale, part du capital et dividendes. Les congés de formation, de transition professionnelle, de bilan de compétences, de VAE et pour enseignement, les anciens CIF encore pertinents, le CPF, son abondement correctif et les droits d'entretien restent ouverts selon leurs règles propres : seul leur relevé détaillé est allégé, sans suppression de congé, rémunération, financement ni abondement. L'abondement du II de L6315-1 reste renseigné avec ses conditions de L6323-13 ; la première année, le seuil de rupture ou la fin d'une formation ne ferment aucun droit de formation. Les actions pour les travailleurs handicapés et l'exclusion des informations D5212-4 sont conservées ; cette exclusion protège la limitation de la communication et n'est pas supprimée. Les aides et exonérations d'insertion et d'alternance, comme les protections de sécurité attachées aux anciennes situations de CDD ou d'intérim, bénéficient aussi aux futures situations éligibles de même objet dans le contrat unique ; les durées de mission ou d'aide ne deviennent pas des termes d'emploi. L'accès aux données existantes, le support papier autorisé, les droits antérieurs et les dispositifs sociaux ou fiscaux sous-jacents ne sont pas fermés. Le texte interdit expressément de transformer ces informations en condition supplémentaire d'octroi : aucune justification de non-changement, attestation de remplacement ou restriction aux seuls anciens bénéficiaires n'est ajoutée.",
    status='rewrite_draft', change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=[
        "La reconstitution obligatoire de l'évolution des effectifs mois par mois est supprimée au profit de l'évolution annuelle, sous réserve des informations ponctuelles légalement nécessaires.",
        "La ventilation générale supplémentaire des effectifs par âge et ancienneté est supprimée au 1° A a ; les analyses d'égalité et ventilations ciblées des autres rubriques subsistent.",
        "L'obligation particulière de justifier le recours au temps partiel au titre du 1° A a est supprimée, sans supprimer les données sur ses conditions d'emploi.",
        "La liste distincte de chaque action de formation, bilan de compétences et validation des acquis est supprimée ; les bilans agrégés et les effectifs par catégorie et sexe demeurent.",
        "Le relevé individuel de l'objet, de l'octroi ou du report et des résultats des congés de formation est supprimé ; les informations agrégées de durée et coût demeurent sans décompte supplémentaire par type.",
        "Le recensement systématique des partenariats commerciaux qui ne sont pas de la sous-traitance est supprimé au titre du 8°, sans fermer les informations utiles requises sur un fondement distinct.",
        "L'inventaire systématique distinct des postes d'émissions directes de gaz à effet de serre au seul titre du 10° C a est supprimé ; les informations disponibles et les bilans autonomes obligatoires demeurent."
    ],
    substantive_impact=dict(
        version=1, classification='material_reduction',
        assessment="La comparaison porte sur tout le tableau officiel : plusieurs relevés systématiques et justifications disparaissent, tandis que les dix thèmes légaux restent documentés. Aux réductions du brouillon s'ajoutent le retrait de la ventilation générale par âge/ancienneté et celui de l'inventaire autonome systématique des postes d'émissions directes. Le nombre de congés par type demandé par le brouillon est également retiré, sans le présenter comme une réduction supplémentaire par rapport à la source qui ne le demandait pas explicitement. Le réemploi de rapports accessibles explicite pour partie une dispense légale déjà existante ; il n'est pas compté comme un nouveau rapport supprimé. Aucun prélèvement ni aide n'est supprimé par cet article.",
        scope_limitations="Les obligations légales de BDESE, les consultations utiles, l'accès permanent de leurs destinataires, les périodes de référence, la sous-traitance, les analyses d'égalité et les bilans environnementaux autonomes subsistent. Les informations ponctuelles réellement nécessaires à une consultation doivent encore être fournies. Les renvois extérieurs au code du travail ne font pas l'objet d'une réécriture dans ce lot. Le gain de temps, les coûts de collecte et le solde net de complexité ou de prélèvements de l'ensemble des codes ne sont pas établis.",
        new_burdens_review="Aucun registre, formulaire, dépôt, certificat, nouvelle échéance ou condition d'aide n'est créé. Les informations agrégées remplacent des relevés plus détaillés de même objet ; le décompte des congés par type ajouté au brouillon est retiré. L'identification d'un document existant est une modalité facultative de réemploi et n'exige pas de portail ni de support informatique nouveau. Les termes actuels de formation et de reconversion rappellent des obligations légales déjà applicables, sans nouveau bilan autonome. La protection des situations de même objet dans le contrat unique ne s'étend pas indistinctement à tous les CDI. Aucun solde national n'a été chiffré.",
        effects=[
            effect('obligation_removed','bdese-effectifs-sans-serie-mensuelle',
                "Supprimer la série obligatoire mois par mois des effectifs.",
                "Évolution des effectifs retracée mois par mois, pour les entreprises soumises à la grille supplétive de moins de 300 salariés.",
                "Évolution annuelle, sans reconstitution d'une série mensuelle ; informations ponctuelles nécessaires à une consultation maintenues.",
                'legal_duty',"Entreprises de moins de 300 salariés soumises au contenu supplétif de la BDESE.",
                "Mises à disposition après l'entrée en vigueur, même pour les années antérieures ; aucun document déjà établi n'est refait et les périodes légales demeurent.",
                "Pas de relevé mensuel de remplacement ; l'information annuelle relève du même thème légal existant.",
                "évolution des effectifs retracée mois par mois",
                "évolution annuelle des effectifs, sans reconstitution obligatoire d'une série mois par mois"),
            effect('obligation_removed','bdese-effectifs-ventilations-ciblees',
                "Retirer la ventilation générale par âge et ancienneté, en conservant les analyses ciblées utiles.",
                "Le 1° A a demande l'évolution des effectifs par type de contrat, âge et ancienneté, en plus des données ciblées des autres rubriques.",
                "Le 1° A a conserve les types de contrat ; la ventilation générale par âge/ancienneté disparaît, les analyses d'égalité et l'âge en alternance subsistent.",
                'legal_duty',"Entreprises de moins de 300 salariés relevant de cette grille supplétive et destinataires de la BDESE.",
                "Mises à disposition postérieures à l'entrée en vigueur, y compris périodes antérieures ; droits d'information sur l'égalité et consultations maintenus.",
                "Aucune nouvelle matrice ne remplace la ventilation retirée ; les autres analyses sont des obligations préexistantes conservées.",
                "Evolution des effectifs par type de contrat, par âge, par ancienneté",
                "Une ventilation générale supplémentaire par âge ou ancienneté n'est pas exigée au titre du présent a) ; les analyses et ventilations prévues aux autres rubriques demeurent applicables"),
            effect('obligation_removed','bdese-temps-partiel-sans-justification-generale',
                "Retirer la justification générale du recours au temps partiel, sans supprimer le bilan de ses conditions d'emploi.",
                "Les motifs du recours aux contrats à temps partiel sont systématiquement demandés avec ceux des autres formes d'emploi.",
                "Cette justification particulière n'est plus requise ; durée, horaires, nombre, sexe et qualification des salariés à temps partiel restent documentés.",
                'legal_duty',"Entreprises de moins de 300 salariés soumises à la grille supplétive ; salariés à temps partiel.",
                "Mises à disposition après entrée en vigueur, même sur les années antérieures ; garantie contractuelle et minima conventionnels non modifiés ici.",
                "Pas de justification ou d'attestation de remplacement ; maintien des données préexistantes nécessaires au contrôle des conditions d'emploi.",
                "aux contrats de travail à temps partiel",
                "La justification particulière du recours au temps partiel n'est plus requise au titre de cette rubrique."),
            effect('obligation_removed','bdese-formation-bilans-agreges',
                "Supprimer la liste de formation action par action au profit du bilan agrégé conservant les publics et catégories.",
                "Bilan des années antérieure et en cours comportant la liste des actions de formation, bilans de compétences et VAE, rapportés aux effectifs par catégorie et sexe.",
                "Bilan agrégé pour les mêmes années et catégories ; aucune liste distincte action par action.",
                'legal_duty',"Entreprises de moins de 300 salariés soumises au contenu supplétif de la BDESE et salariés bénéficiaires des dispositifs de formation.",
                "Mises à disposition postérieures à l'entrée en vigueur ; dispositifs actuels et anciennes périodes restent couverts selon leur champ propre.",
                "Un bilan agrégé de même objet remplace la liste détaillée ; aucun nouveau registre ni nouvelle condition de formation.",
                "comportant la liste des actions de formation, des bilans de compétences et des validations des acquis de l'expérience réalisés",
                "Une liste distincte action par action n'est pas exigée"),
            effect('obligation_removed','bdese-conges-formation-releve-allege',
                "Retirer les renseignements individuels détaillés sur l'objet, l'octroi, le report et les résultats des congés de formation.",
                "Pour l'année antérieure et l'année en cours, informations sur les congés incluant objet, durée, coût, conditions d'octroi ou report et résultats.",
                "Pour ces mêmes années, durée et coût agrégés des congés concernés, sans relevé individuel de l'objet, de l'octroi/report et des résultats ni décompte supplémentaire par type.",
                'legal_duty',"Entreprises relevant de la grille supplétive et bénéficiaires des congés de formation, de bilan, de VAE, d'enseignement et de transition professionnelle.",
                "Mises à disposition après entrée en vigueur, anciennes périodes comprises ; droits aux congés, rémunérations et recours préservés.",
                "Information agrégée en remplacement du détail ; le nombre par type ajouté au précédent brouillon n'est pas exigé et n'est pas compté comme une coupe dans la source officielle.",
                "notamment leur objet, leur durée et leur coût, aux conditions dans lesquelles ces congés ont été accordés ou reportés ainsi qu'aux résultats obtenus",
                "Aucun décompte supplémentaire du nombre de congés par type ni relevé individuel de leur objet, des conditions de leur octroi ou de leur report et des résultats obtenus n'est exigé au titre de cette rubrique"),
            effect('obligation_removed','bdese-partenariats-sous-traitance',
                "Retirer le recensement général des partenariats hors sous-traitance.",
                "Le 8° couvre tous les partenariats conclus pour produire ou recevoir des biens et services, sans limitation à la sous-traitance.",
                "Le 8° couvre les deux sens de la sous-traitance ; les autres partenariats commerciaux ne sont plus systématiquement recensés sur ce seul fondement.",
                'legal_duty',"Entreprises de moins de 300 salariés soumises à la grille supplétive et leurs partenaires commerciaux.",
                "Mises à disposition après entrée en vigueur ; informations nécessaires à une autre consultation et sous-traitance légale maintenues.",
                "Aucun état de remplacement des autres partenariats ; accès utile à l'information demeurant requis sur un fondement autonome.",
                "Partenariats conclus pour bénéficier des services ou des produits d'une autre entreprise",
                "Les autres partenariats commerciaux ne font pas l'objet d'un recensement obligatoire au seul titre du présent 8°."),
            effect('obligation_removed','bdese-emissions-sans-inventaire-distinct',
                "Supprimer l'inventaire systématique autonome des postes d'émissions directes imposé par la seule grille.",
                "Identification obligatoire des postes d'émissions directes des sources fixes et mobiles ; évaluation du volume seulement si l'entreprise en dispose.",
                "Communication des informations déjà disponibles sur les postes et volumes ; pas d'inventaire distinct ni de calcul à créer au seul titre du 10° C a ; bilans autonomes du b) maintenus.",
                'legal_duty',"Entreprises de moins de 300 salariés relevant du contenu supplétif de la BDESE, notamment celles non soumises à un bilan autonome d'émissions.",
                "Mises à disposition postérieures à l'entrée en vigueur ; informations nécessaires à une consultation utile et note de mise en perspective à l'échelle de l'entreprise conservées.",
                "Pas de bilan, certification ou attestation substitutive. Les bilans légaux déjà requis et les informations disponibles demeurent accessibles.",
                "Identification des postes d'émissions directes de gaz à effet de serre produites par les sources fixes et mobiles nécessaires aux activités de l'entreprise",
                "Aucun inventaire distinct de ces postes ni calcul de leur volume n'est à établir au seul titre du présent a)."),
            effect('coordination','bdese-reemploi-informations-accessibles',
                "Rendre explicite le réemploi des documents et analyses accessibles, en coordination avec la dispense légale de rapports séparés.",
                "La grille énumère des informations ; L2312-18 et R2312-14 prévoient déjà que leur mise à disposition actualisée peut valoir communication des rapports.",
                "La grille explicite l'accès direct aux documents existants et le renseignement unique des informations communes ; les analyses utiles et l'ensemble des droits d'accès demeurent.",
                'legal_duty',"Employeurs de la grille supplétive et tous les destinataires légaux de la base.",
                "Mises à disposition après entrée en vigueur ; documents déjà établis non refaits et support papier encore autorisé.",
                "Modalité de réemploi, sans nouveau portail ni dépôt ; aucune seconde suppression de rapport n'est imputée à cette coordination.",
                "les informations contenues dans le rapport relatif à l'impôt sur les bénéfices prévu par l'article L. 232-6 du code de commerce",
                "Les informations et analyses communes à plusieurs rubriques ne sont mises à disposition qu'une fois."),
            effect('coordination','contrat-unique-duree-indeterminee',
                "Distinguer les anciens CDD des missions, formations et dispositifs futurs qui se déroulent dans le contrat unique.",
                "La grille recense les CDD et l'alternance sans transition vers un contrat unique.",
                "Les CDD recensés sont antérieurs ; les nouveaux emplois, y compris intérim, portage, insertion et alternance, sont à durée indéterminée et ne prennent pas fin avec leur mission ou formation.",
                'regime',"Salariés privés entrant dans le champ de la grille ; aucun régime d'agent public assimilé.",
                "Contrats nouveaux à compter de l'entrée en vigueur de la loi instituant le contrat unique ; anciens contrats et droits préservés, aucun renouvellement futur de CDD autorisé.",
                "Aucune nouvelle déclaration d'autorisation de CDD ; la consultation et les protections de sécurité restent à leur champ propre.",
                "nombre de salariés titulaires d'un contrat de travail à durée déterminée",
                "La durée d'une mission, d'une formation, d'une convention ou d'une aide n'est pas une durée d'emploi."),
            effect('relief_preserved','bdese-avantages-sans-condition-nouvelle',
                "Préserver tous les avantages recensés sans faire du tableau une condition d'éligibilité nouvelle.",
                "La grille demande des informations sur les aides, réductions d'impôt, exonérations/réductions de cotisations, crédits d'impôt, formation et épargne ; elle n'en abolit pas les fondements.",
                "Les mêmes catégories sont documentées et une clause expresse maintient les avantages et leur accès pour les futures situations éligibles de même objet, sans condition BDESE supplémentaire.",
                'other',"Entreprises et salariés éligibles aux aides, exonérations, crédits, abondements, congés, épargne salariale et mécénat.",
                "Situations futures éligibles sous leurs autres conditions propres et droits antérieurs conservés ; aucune suppression de taxe ou extension d'assiette par cet article.",
                "Aucune attestation ni condition d'octroi substitutive ; l'allègement du relevé ne ferme pas l'avantage sous-jacent.",
                "Exonérations et réductions de cotisations sociales",
                "L'allègement du contenu de la base n'emporte aucune suppression de ces avantages.")
        ]))

checks = {
    'D1272-5': {
        'L1234-1': "Renvoi de cohérence indirect, absent de la liste de données : L1234-1 officiel module le préavis selon six mois/deux ans ; sa proposition applique quinze jours calendaires aux contrats nouveaux sans condition d'ancienneté, en maintenant les anciens préavis et procédures protégées. Le volet d'identification ne crée ni démission ni licenciement et sa date historique de CDD ne vaut pas notification de rupture.",
        'L1221-2': "Le 2° a) est coordonné avec L1221-2 proposé : tout emploi privé nouveau est à durée indéterminée ; ni tâche, mission, formation ni aide ne fixe sa fin. La date de fin ne concerne que les CDD déjà conclus et aucun renouvellement futur ne peut en résulter ; les droits et l'ancienneté des anciens contrats demeurent distincts. Le texte source autorise encore des CDD et n'est pas confondu avec cette proposition.",
        'L1234-9': "Ce texte ne calcule aucune indemnité et son identification d'emploi ne doit pas transformer la fin d'une aide en rupture. La cible officielle ouvre l'indemnité à huit mois sous exception de faute grave ; sa proposition distingue le nouveau seuil d'un an au terme effectif préavis inclus, 0,20 mois sur toute l'ancienneté, mois complets et plafond de six mois, employeur seul, avec ancien régime et indemnités spéciales préservés. Aucun montant ni seuil d'éligibilité social n'est importé dans le volet.",
        'R1221-1': "Le 1° a) vise bien la DPAE entière, donc aussi les données employeur et agricoles nécessaires, pas seulement l'identité du salarié. Sa proposition retire APE et durée de l'essai, réutilise les données disponibles et ne demande plus de durée d'emploi pour un contrat unique. Le 2° b) du présent volet est une clause contractuelle seulement lorsqu'il tient lieu de contrat ; il ne rétablit pas l'essai dans la DPAE. Les anciennes mentions de CDD restent soumises à leurs conditions et transition propres.",
        'D1272-1': "Le 2° actuel énumère les données d'emploi et n'institue pas un second volet : le renvoi introductif source est rectifié à la déclaration entière. La proposition cible dispense de durée d'essai en cas de contrat distinct, de durée d'emploi nouvelle, de taux uniformes ou non spécifiques et de seconde signature du salarié ; ces dispenses sont expressément opposables à D1272-5. Les affiliations, échéances utiles et remise au salarié ne sont pas effacées, pour les anciens comme les nouveaux contrats.",
        'D1272-4': "La substitution des clauses d'un contrat distinct signé couvre l'embauche de droit commun et le temps partiel ; la proposition maintient également les anciens CDD établis sous les articles L1242-12/13 antérieurs. Le présent 2° b) et 3° n'exigent donc ni nouvelle déclaration de l'essai ni nouvelle signature du salarié dans ce cas. Les seules informations légalement nécessaires manquantes ou modifiées restent à compléter, sans dépôt supplémentaire du contrat."
    },
    'R2262-1': {
        'L1234-1': "Aucun renvoi direct au préavis : l'accès à un accord collectif n'en rend pas toutes les anciennes durées applicables à un contrat unique nouveau. La proposition de L1234-1 substitue quinze jours calendaires indépendamment de l'ancienneté, avec protection des procédures collectives et autorisations ; les anciens contrats gardent leurs préavis source. Le support unique d'information n'est pas la notification écrite de rupture et n'en déclenche aucun délai.",
        'L1221-2': "L'information sur les accords reste due pour les contrats nouveaux comme anciens. L1221-2 officiel connaît encore les CDD ; sa proposition les ferme pour les nouvelles embauches et renouvellements, avec emploi indéterminé même si formation ou mission limitée. La mise à disposition d'accords ne rétablit pas une clause de terme interdite et ne réserve aucun avantage conventionnel aux seuls contrats antérieurs.",
        'L1234-9': "Le règlement de support ne change ni droit à indemnité ni condition d'ancienneté. La cible proposée distingue les anciens contrats du contrat unique : un an au terme effectif avec préavis, zéro avant ce seuil puis 0,20 mois sur l'ancienneté totale, prorata des mois complets et plafond de six mois à l'initiative de l'employeur ; faute grave et indemnités spéciales restent dans leur champ. La consultation d'un accord ne vaut pas notification de rupture ni renonciation à une indemnité plus favorable.",
        'R1221-35': "Le 13° de R1221-34, objet du présent 1°, relève des informations à fournir au plus tard un mois après embauche, et non du groupe dû au septième jour. La proposition cible admet déjà l'écrit exact, complet et remis individuellement dans les formes de R1221-39 sans second document ; R2262-1 ne recrée pas cette remise. Le seul accès collectif à un exemplaire ne remplace pas la communication individuelle légalement due.",
        'R1221-34': "Le renvoi porte spécifiquement sur le 13° qui identifie les conventions et accords applicables au salarié ; les 5°, 7° et 10° relatifs à durée, essai et rupture sont des informations distinctes. La proposition cible distingue anciens CDD et contrat unique, essai sans renouvellement et procédure de notification du préavis de quinze jours. L'alternative de support du présent article n'altère aucune de ces informations ni les conditions d'ancienneté de la protection complémentaire du 14°."
    },
    'R2312-8': {
        'L1234-1': "La grille d'effectifs et de conditions de travail n'est pas un régime de rupture et ne fait courir aucun préavis. L1234-1 proposé prévoit quinze jours calendaires pour les contrats nouveaux indépendamment de l'ancienneté, conserve les règles source pour les contrats anciens et distingue les procédures collectives et autorisations. Le retrait d'une ventilation générale par ancienneté n'efface ni celle du contrat individuel ni sa preuve pour ces droits et ne transforme pas la fin d'une mission en notification.",
        'L1221-2': "Le nombre de CDD au 1° A a est réservé aux contrats antérieurs. L1221-2 proposé interdit tout nouveau terme et renouvellement après entrée en vigueur, y compris par fin de tâche ou de formation ; les durées d'alternance, mission et aide restent distinctes de l'emploi. Les données sur ces dispositifs et leurs avantages restent ouvertes aux futures situations éligibles en contrat unique. Les agents publics ne sont pas assimilés artificiellement à ce régime privé.",
        'L1234-9': "Ni les rubriques de rémunération ni celles d'effectifs ne modifient l'indemnité ordinaire. La cible source exige huit mois et exclut la faute grave ; la proposition distingue les anciens droits et le nouveau seuil d'un an à la fin effective avec préavis inclus, suivi de 0,20 mois sur toute l'ancienneté, prorata des mois complets, plafond légal de six mois et employeur seul. La grille ne crée pas de franchise de première année, ne supprime pas les salaires, congés ou réparations et ne remplace aucune notification individuelle.",
        'L4143-1': "Le renvoi englobant L4141-1 à L4143-1 au 1° A f ii inclut la consultation du CSE sur les programmes de formation et leur mise en œuvre effective. Le 1° de la cible proposée renvoie au champ de L4142-2 plutôt qu'à tous les CDD nouveaux ; le 2° concernant les installations à risques et ses codes extérieurs reste inchangé. Les coupes dans les statistiques de formation ne suppriment ni ces consultations ni les protections des situations anciennes ou de même objet sous contrat unique.",
        'L4154-2': "Le iii vise la formation renforcée, l'accueil adapté et l'information aux postes à risques, avec liste après avis du médecin et du CSE conservée par la cible. Sa proposition couvre les anciens CDD, les intérimaires, les stagiaires et les contrats uniques du troisième alinéa de L4142-2 ; ce dernier a été lu dans le corpus et se rattache aux anciennes situations des L1242-2/3 uniquement pour maintenir la sécurité. La grille ne généralise pas ce régime à tout CDI et ne rétablit aucun CDD. L4154-4 reste limité aux intérimaires qualifiés des travaux urgents de sécurité."
    }
}

checks['R2312-8']['L2312-26'] = (
    "La cible source distingue le I (thèmes de la consultation annuelle) et le II "
    "(informations nécessaires), notamment les 1° et 9° pour les contrats et missions, "
    "les 3°, 4°, 4° bis et 4° ter pour compétences, CPF, entretiens et reconversion, "
    "et le 5° pour le temps de travail. Sa note fixe au 1er janvier 2026 l'entrée en "
    "vigueur historique de la rédaction issue de 2025 ; ce n'est pas la date de la "
    "réforme projetée. La proposition cible réserve les CDD aux contrats antérieurs, "
    "retire le décompte du II 5° d et la justification spécifique des recours envisagés "
    "pour l'année suivante au II 9°, sans supprimer les perspectives générales d'emploi. "
    "La présente grille ne rétablit ni ce décompte ni cette prévision détaillée ; ses "
    "motifs portent sur les recours effectués. Le paragraphe final assure l'accès aux "
    "bilans de formation et de reconversion légalement nécessaires sans état distinct. "
    "Les aides, exonérations et garanties de logement restent ouvertes aux futures "
    "situations éligibles dans le contrat unique ; la durée de formation ou d'aide "
    "ne termine pas l'emploi. Ces informations collectives ne constituent aucune "
    "notification de rupture et n'altèrent ni ancienneté ni indemnités spéciales."
)

# Un effet unique pour la mesure commune d'identification : les trois éléments
# sont des coordinations du même document, pas trois allègements indépendants.
identification = answer[0]['substantive_impact']['effects']
assert [(x['kind'], x['measure_id']) for x in identification[:3]] == [
    ('coordination', 'identification-salarie-sans-doublons')
] * 3
merged = dict(identification[0])
merged.update(
    description="Coordonner le document unique, le réemploi des données, les dispenses de mention de l'essai et des taux sociaux, et la dispense de seconde signature déjà retenus dans D1272-1/D1272-4, sans compter plusieurs fois cette même mesure.",
    before="D1272-5 énumère les mentions du volet, dont la durée d'essai, le taux accidents du travail et le cas échéant le taux prévoyance, ainsi que les deux signatures. Le renvoi au seul 2° de D1272-1 est discordant ; la substitution des clauses du contrat distinct de D1272-4 doit déjà être prise en compte.",
    after="Le même document sert à l'identification. Seules les données nécessaires manquantes ou modifiées sont complétées ; l'essai n'est renseigné que si la déclaration tient lieu de contrat. Seuls les taux AT-MP multiples ou de prévoyance spécifiques non connus sont indiqués ; le contrat distinct signé dispense de seconde signature du salarié.",
    conditions_and_transition="Transmissions après l'entrée en vigueur de la loi proposée, même pour un contrat antérieur, sans réfection. Les clauses du contrat distinct signé demeurent substituées ; données réellement manquantes, échéances préalables et information du salarié restent dues dans leur champ.",
    replacement_or_new_burdens="Aucun dépôt du contrat, formulaire, attestation de non-changement ou déclaration équivalente n'est ajouté. La signature reste nécessaire lorsque la déclaration tient lieu de contrat. Il s'agit d'une coordination des mêmes dispenses, sans gain autonome ni baisse des taux de cotisation.",
    source_quote="Les signatures de l'employeur et du salarié.",
    proposed_quote="La signature d'un contrat distinct dans les conditions de l'article D. 1272-4 dispense le salarié d'une seconde signature."
)
answer[0]['substantive_impact']['effects'] = [merged] + identification[3:]

# La source n'exige pas littéralement un exemplaire papier et un fichier
# distincts : la réduction porte précisément sur la publication intranet imposée.
r = answer[1]
r['reason'] = (
    "La réforme de fond déjà retenue est conservée : l'employeur peut assurer l'accès "
    "aux accords à jour sur un support unique de son choix, sans publication intranet "
    "supplémentaire obligatoire si l'accès est assuré autrement. La source cumulait "
    "l'accès sur le lieu de travail et la publication intranet lorsque cet outil existe, "
    "sans imposer expressément deux fichiers ou un exemplaire papier distinct. Après "
    "réexamen, aucune coupe supplémentaire n'est justifiée : l'information individuelle "
    "identifie les textes applicables et l'exemplaire accessible permet d'en consulter "
    "le contenu pendant l'emploi. Ces fonctions, l'actualisation et la priorité des "
    "modalités conventionnelles sont conservées. Aucun gain nouveau n'est attribué à "
    "la seule conservation du brouillon."
)
r['substantive_impact']['assessment'] = (
    "La source officielle entière exige la publication sur l'intranet quand il existe, "
    "en plus de l'accès sur le lieu de travail ; un même exemplaire numérique peut "
    "déjà satisfaire ces deux exigences. La proposition supprime l'obligation de "
    "publication intranet lorsque l'employeur choisit un autre support effectivement "
    "accessible. Le gain concerne alors la publication et son actualisation ; aucun "
    "double fichier imposé par la source n'est présumé. Cette réduction figurait déjà "
    "dans le brouillon et aucune coupe supplémentaire n'est retenue."
)
r['substantive_impact']['scope_limitations'] = (
    "L'allègement bénéficie aux entreprises soumises aux modalités supplétives qui "
    "disposent d'un intranet et choisissent un autre support accessible. Si l'intranet "
    "satisfait déjà aux deux exigences source, aucune seconde copie effectivement "
    "supprimée n'est démontrée. Les modalités conventionnelles autonomes, "
    "l'information individuelle, l'actualisation et l'accès effectif subsistent. "
    "Aucun coût moyen ni solde de complexité des cinq codes n'est établi."
)
r['substantive_impact']['effects'][0]['before'] = (
    "À défaut de modalités conventionnelles différentes, exemplaire à jour accessible "
    "sur le lieu de travail et publication intranet dès qu'il existe ; le même "
    "exemplaire numérique peut déjà assurer les deux fonctions."
)

# Les renseignements source sur les congés ne sont pas expressément nominatifs.
# Décrire la coupe du détail demandé, sans inventer un ancien relevé nominatif.
def precise_conges(value):
    if isinstance(value, str):
        return value.replace('relevé individuel', 'relevé détaillé').replace(
            'renseignements individuels détaillés', 'renseignements détaillés')
    if isinstance(value, list):
        return [precise_conges(x) for x in value]
    if isinstance(value, dict):
        return {k: precise_conges(v) for k, v in value.items()}
    return value
answer[2] = precise_conges(answer[2])
answer[2]['review_notes'] = replace_once(
    answer[2]['review_notes'],
    "Renvois ajoutés par rapport à la source officielle et absents des cibles de reference-targets : L2312-36 et R2312-10 à R2312-14, déjà présents dans le brouillon, ainsi que L2312-26 désormais explicité. Tous ont été lus en entier dans le corpus local ; pour L2312-26, sa proposition et sa note d'entrée en vigueur du 1er janvier 2026 ont également été examinées.",
    "Renvois ajoutés par rapport à la source officielle et absents des cibles de reference-targets : L2312-36 et R2312-10 à R2312-14, déjà présents dans le brouillon. Ils ont été lus en entier dans le corpus local. Le renvoi désormais explicité à L2312-26 fait, lui, partie des cibles fournies : son texte officiel, sa note d'entrée en vigueur du 1er janvier 2026 et sa proposition ont été lus en entier ; le contrôle dédié distingue leurs effets. Les renvois conservés au code de commerce, au code de l'environnement et à la loi de finances pour 2021 restent à contrôler sur leurs textes extérieurs entiers, non fournis ici ; aucun contenu supplémentaire ne leur est attribué."
)
answer[2]['reason'] = answer[2]['reason'].replace(
    "redondante avec les analyses ciblées qui restent exigées",
    "dont le relevé systématique supplémentaire n'est pas indispensable aux analyses ciblées maintenues ; les données nécessaires à une consultation utile restent communicables"
)
for article_checks in checks.values():
    article_checks['L1234-1'] += (
        " La notification écrite demeure distincte de ces informations ; selon L1234-3 "
        "proposé, lu dans le corpus, les quinze jours courent du lendemain de la "
        "présentation ou de la réception légalement pertinente, sans absorber les "
        "procédures collectives et autorisations distinctes."
    )

for obj in answer:
    req = refs['requirements'][obj['code_id'] + '|' + obj['source_id']]
    obj['reference_checks'] = []
    for key in req:
        target = refs['targets'][key]
        obj['reference_checks'].append(dict(
            target_key=key, view_sha256=target['view_sha256'],
            assessment=checks[obj['number']][target['number']]))

    pairs = [(e['measure_id'], e['kind']) for e in obj['substantive_impact']['effects']]
    assert len(pairs) == len(set(pairs)), ('Duplicate measure and effect in one article', obj['number'])

Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print('answer.json :', len(answer), 'articles')
