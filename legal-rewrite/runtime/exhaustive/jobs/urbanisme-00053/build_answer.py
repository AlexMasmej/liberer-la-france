import json
import re
import html
from pathlib import Path


SOURCES = json.loads(Path('source.json').read_text())
BY_NUMBER = {s['number']: s for s in SOURCES}
ANSWERS = {}


def plain(xml):
    return html.unescape(re.sub(r'<[^>]*>', '', xml or ''))


def impact(classification, assessment, limitations, burdens, effects=None):
    return {
        'version': 1,
        'classification': classification,
        'assessment': assessment,
        'scope_limitations': limitations,
        'new_burdens_review': burdens,
        'effects': effects or [],
    }


def effect(kind, measure_id, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    return {
        'kind': kind,
        'measure_id': measure_id,
        'description': description,
        'before': before,
        'after': after,
        'unit': unit,
        'affected_population': population,
        'conditions_and_transition': transition,
        'replacement_or_new_burdens': burdens,
        'source_quote': source_quote,
        'proposed_quote': proposed_quote,
    }


def base(number, status, proposed, reason, notes, substantive):
    src = BY_NUMBER[number]
    item = {k: src[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    item.update(proposed_xml=proposed, reason=reason, review_notes=notes,
                status=status, classification=substantive['classification'],
                substantive_impact=substantive)
    ANSWERS[number] = item
    return item


def retained(number, reason, notes, assessment, limitations, burdens):
    return base(number, 'retained_unchanged', None, reason, notes,
                impact('retained_necessary', assessment, limitations, burdens))


def rewritten(number, proposed, reason, notes, substantive, removed=None):
    item = base(number, 'rewrite_draft', proposed, reason, notes, substantive)
    if removed:
        item.update(change_type='normative_reduction',
                    reform_policy_id='editorial_direction_2026_10_19',
                    removed_provisions=removed)
    return item


retained(
    'R104-9',
    "Maintien intégral après examen des trois déclencheurs : risque significatif pour Natura 2000, effets d'une révision du SCoT et lacune de l'étude d'impact dans une procédure intégrée. Ils assurent une évaluation des transformations potentiellement importantes ; ce ne sont ni une taxe ni un agrément sans fonction propre. Le 3° ne constitue pas un déclencheur supplémentaire lorsque l'analyse est déjà incluse dans l'étude d'impact, sans dispenser des cas du 1° ou du 2°. Aucune réécriture de vocabulaire n'est proposée.",
    "L. 143-29 et le V de L. 300-6-1 ont été lus dans le corpus : le premier définit désormais la révision par les orientations du projet d'aménagement stratégique ; le second exige l'évaluation manquante avant l'examen conjoint. R. 104-10 garde son rôle pour les autres mises en compatibilité. La note source de l'article 26 du décret de 2021 est conservée dans son champ historique, sans en faire une date de la réforme. Les exigences Natura 2000 et de la directive 2001/42/CE ne sont pas abrogées.",
    "Les trois cas d'évaluation restent identiques à la source entière. La condition du 3° tient compte de l'analyse déjà incluse dans l'étude d'impact, sans neutraliser les deux autres déclencheurs. Aucun allègement nouveau n'est compté.",
    "Le maintien concerne les mises en compatibilité du SCoT, non les permis ni les autres documents. La compatibilité européenne de toute réduction ultérieure du champ demanderait un examen distinct ; aucun solde national n'est chiffré.",
    "Aucune charge nouvelle n'est identifiée : le texte source est conservé, sans dossier, attestation ni consultation supplémentaire. L'obligation existante répond aux incidences significatives et aux cas légalement définis.",
)

retained(
    'R104-10',
    "Maintien des deux voies de filtrage des mises en compatibilité du SCoT non couvertes par R. 104-9. L'évaluation n'est imposée qu'en présence d'incidences notables appréciées selon l'annexe II de la directive. Le partage entre examen par l'autorité environnementale et examen avec avis conforme n'est pas un double examen cumulatif du même dossier. Supprimer le filtrage ferait disparaître une garantie environnementale, sans doublon établi.",
    "Les cibles L. 143-42, L. 143-44, R. 143-12 et R. 143-13 et les procédures R. 104-28 à R. 104-37 ont été lues. Le renvoi au second alinéa de L. 143-42 demeure cohérent avec la mise en compatibilité engagée par l'Etat. Les allègements du fonctionnement de l'examen dans ce lot ne suppriment pas son champ. La note de 2021 conserve sa portée transitoire propre ; les échéances des procédures anciennes ne sont pas recréées.",
    "Le critère des incidences notables et les deux voies alternatives sont maintenus sans extension de champ. Le maintien n'est ni une fusion nouvelle ni une suppression d'autorisation.",
    "Le renvoi à l'annexe II de la directive est conservé ; son texte intégral n'est pas joint au lot. Aucune conformité européenne globale ni économie de procédure à l'échelle du corpus n'est établie.",
    "Aucune charge nouvelle n'est identifiée : maintien du seul filtrage existant et de ses garanties, sans nouvelle déclaration, donnée ou pièce justificative.",
)

retained(
    'R104-11',
    "Maintien de l'évaluation environnementale lors de l'élaboration et de la révision des PLU. Le corps ne comporte ni taxe, ni pièce accessoire, ni circuit d'agrément à retirer. La révision vise les changements d'orientations définis par L. 153-31, et non toute correction matérielle. Le principe légal de L. 104-1 et la protection des incidences des choix d'urbanisation justifient ce maintien, sans reformulation stylistique.",
    "Version assignée entrée en vigueur le 5 août 2026, sans note source complémentaire. L. 104-1, L. 104-3 et L. 153-31 ont été lus : ne pas transformer le caractère systématique du contrôle en exigence systématique d'études entièrement nouvelles lorsque l'actualisation suffit. Les dispenses de modification relèvent de R. 104-12 ; elles ne sont pas retirées ici. Pas de suppression implicite de contraintes issues de la directive 2001/42/CE.",
    "Le champ de l'évaluation des élaborations et révisions de PLU demeure exactement celui de la source. Aucune réduction n'est revendiquée pour la conservation de ce principe nécessaire.",
    "L'article ne règle ni les méthodes d'actualisation ni les délais d'avis. Une éventuelle réduction du champ légal suppose une coordination de L. 104-1 et du droit de l'Union, absente de cette proposition.",
    "Aucune charge nouvelle n'est identifiée : aucune nouvelle étude, donnée, échéance ou condition d'accès à un avantage n'est ajoutée au texte maintenu.",
)

item = retained(
    'R104-12',
    "Maintien du régime ciblé des modifications de PLU : évaluation pour Natura 2000 et, dans les autres cas, seulement après constat d'incidences notables au cas par cas. La dispense expresse des modifications ayant pour seul objet une réduction de zone urbaine ou à urbaniser ou la rectification d'une erreur matérielle reste intégrale, pour les futures procédures éligibles aussi. Les deux branches sont alternatives ; aucun double dossier n'est institué.",
    "Version du 5 août 2026. L. 104-3 et R. 104-33 à R. 104-37 ont été lus : la dispense du dernier alinéa n'est pas une clause limitée aux procédures anciennes. Le filtrage environnemental restant protège les incidences notables et Natura 2000. Les régimes transitoires de L. 104-3, notamment les procédures en cours le 26 mai 2026, gardent leur champ propre ; aucune date historique n'est transformée en date de réforme.",
    "Les deux déclencheurs et les deux objets de dispense sont conservés intégralement. Les exemptions déjà acquises dans la source ne sont pas présentées comme deux allègements créés par ce lot.",
    "La dispense porte sur les seuls objets énumérés, non sur toute modification comprenant aussi d'autres changements. Aucune réduction du champ de la directive ni baisse de coût totale n'est démontrée.",
    "Aucune charge nouvelle n'est identifiée : maintien des dispenses sans attestation, enregistrement ou condition supplémentaire et maintien du filtrage dans les autres cas.",
)
item['benefit_review'] = "La dispense d'évaluation pour les modifications ayant pour seul objet de réduire une zone urbaine ou à urbaniser, ainsi que celle relative à la seule rectification d'une erreur matérielle, sont maintenues sans changement pour les procédures futures éligibles. Le cas par cas reste un filtre permettant de ne pas imposer une évaluation sans incidences notables ; aucun avantage fiscal n'est présent."

retained(
    'R104-13',
    "Maintien intégral des trois cas de mise en compatibilité du PLU nécessitant une évaluation : atteinte significative possible à Natura 2000, effets d'une révision et procédure intégrée dont l'étude d'impact n'a pas couvert les dispositions concernées. La condition du 3° tient compte de l'analyse déjà incluse, sans dispenser des évaluations requises par les deux autres déclencheurs. Les retirer indistinctement neutraliserait la protection environnementale et le V de L. 300-6-1.",
    "L. 153-31 et L. 300-6-1 ont été lus ; le renvoi au premier conserve ses exceptions légales et le V du second impose l'évaluation manquante avant l'examen conjoint. Le point final du 2° dans la source n'est pas une nouvelle subdivision. R. 104-14 demeure applicable au champ résiduel. Version assignée du 5 août 2026, sans note transitoire jointe.",
    "Les trois déclencheurs sont inchangés, y compris la condition propre au 3° relative à l'analyse incluse dans l'étude d'impact. Cette condition ne dispense pas des cas du 1° ou du 2°. Aucun gain supplémentaire n'est attribué à cette conservation.",
    "Le maintien ne modifie ni les autorisations de projet ni les dispositions autonomes de protection du littoral. Les modalités de réutilisation des études et les exigences européennes gardent leur régime distinct.",
    "Aucune charge nouvelle n'est identifiée : maintien du contenu source sans nouvelle pièce, nouvelle donnée ni exigence de refaire une étude déjà suffisante.",
)

retained(
    'R104-14',
    "Maintien des voies alternatives de cas par cas pour les mises en compatibilité du PLU qui ne relèvent pas de R. 104-13. Le seuil d'incidences notables et les critères européens conditionnent l'évaluation, ce qui écarte l'étude systématique sans enjeu établi. Les deux voies correspondent à des autorités et procédures distinctes ; aucun doublon cumulatif n'est démontré.",
    "Lecture de L. 153-51, L. 153-54, R. 153-16, R. 153-17 et R. 104-28 à R. 104-37. La désignation du second alinéa de L. 153-51 demeure cohérente. Les formalités allégées dans R. 104-28 à R. 104-30 ne ferment ni la dispense ni le contrôle utile. La note de l'article 26 du décret de 2021 reste une règle historique, pas une échéance nouvelle.",
    "Le filtre des incidences notables et les deux voies du 1° et du 2° sont maintenus. Aucune autorisation ni obligation nouvelle n'est supprimée par le simple maintien de ces renvois.",
    "L'article ne fixe pas lui-même les délais ni les pièces du cas par cas. Le droit de l'Union et les garanties de la décision motivée restent applicables ; aucun bilan global de simplification n'est établi.",
    "Aucune charge nouvelle n'est identifiée : aucune extension du champ, aucun nouveau formulaire ni circuit d'approbation ne s'ajoute aux voies existantes.",
)

retained(
    'R104-15',
    "Maintien de l'évaluation des cartes communales lorsque les travaux qu'elles permettent peuvent affecter significativement Natura 2000. Cette condition ciblée protège les habitats et espèces ; l'article n'ajoute pas de prélèvement ou d'autorisation accessoire. Le cas général reste filtré par R. 104-16, et n'est pas absorbé dans une évaluation systématique générale.",
    "L. 104-2 et R. 104-16 articulent le régime des cartes communales. La note source de 2021 mentionne des transitions de procédures de PLU ; elle n'est pas étendue par inférence à toutes les cartes communales. Le présent maintien ne prétend ni abroger ni remplacer le régime d'incidences Natura 2000 du code de l'environnement.",
    "Le seul cas d'incidences significatives possibles sur Natura 2000 demeure inchangé. Aucun allègement matériel ni suppression de taxe ne résulte de cette conservation nécessaire.",
    "L'évaluation porte sur les cartes et non sur l'ensemble des projets pris individuellement. Le texte intégral du régime Natura 2000 extérieur au corpus n'est pas réécrit et sa conformité n'est pas certifiée.",
    "Aucune charge nouvelle n'est identifiée : pas d'extension des cartes concernées, de justificatif ou de délai nouveau dans l'article conservé.",
)

retained(
    'R104-16',
    "Maintien du filtrage des élaborations et révisions de cartes communales hors Natura 2000. L'évaluation n'est requise que pour les incidences notables établies après cas par cas, selon les critères de la directive. Ce mécanisme évite déjà une évaluation systématique de toutes les cartes tout en conservant le contrôle utile. Aucun doublon ni prélèvement n'est retiré artificiellement.",
    "L. 104-2, R. 104-15 et R. 104-33 à R. 104-37 ont été lus ; les dispenses et l'avis conforme gardent leur champ. La note de 2021 est reproduite dans la source avec son objet PLU et n'est pas transformée en transition générale des cartes. Les futurs dossiers éligibles à l'absence d'évaluation ne sont pas fermés.",
    "Le caractère conditionnel de l'évaluation hors R. 104-15 reste intégralement maintenu. La possibilité existante de ne pas réaliser d'évaluation n'est pas un gain créé par ce lot.",
    "Les critères de l'annexe II et le filtrage restent nécessaires ; aucun allègement du formulaire de R. 104-34, hors lot, n'est présenté comme réalisé.",
    "Aucune charge nouvelle n'est identifiée : aucune nouvelle démarche ni condition ne s'ajoute au filtrage maintenu et aucun second contrôle ne lui est superposé.",
)

item = retained(
    'R104-17',
    "Maintien intégral de l'évaluation des élaborations et révisions des schémas d'aménagement de plage. Cette garantie environnementale soutient le régime facultatif et favorable de L. 121-28 à L. 121-30 ; elle ne ferme pas les dérogations littorales pour de nouveaux projets éligibles. La supprimer au motif de l'origine SRU serait contraire à preserved_benefits_2026_10_19 et retirerait une garantie expressément conservée avec ces dérogations.",
    "Lecture de L. 104-2 3°, L. 121-28, L. 121-29, L. 121-30, R. 121-7 et R. 121-8 : les équipements antérieurs au 5 janvier 1986, le maintien ou la reconstruction dérogatoires, l'enquête et l'avis de la commission restent à leur champ propre. Aucune fermeture de procédure, de rubrique environnementale I 50° ou du fondement de L. 341-16 du code de l'environnement n'est opérée. Ces deux textes environnementaux extérieurs ne sont pas réécrits dans le lot.",
    "Les deux cas d'évaluation du schéma de plage sont intégralement conservés avec la possibilité d'utiliser ce schéma à l'avenir. Ce maintien ne compte pas comme nouvelle réduction de contrainte.",
    "L'article n'accorde pas à lui seul une dérogation littorale et ne modifie aucune condition des autorisations. L'examen des 209 articles SRU n'est pas déclaré achevé par ce lot.",
    "Aucune charge nouvelle n'est identifiée : maintien du contrôle existant, sans ajout d'agrément ou de déclaration, afin de laisser fonctionner les dérogations littorales dans leurs conditions actuelles.",
)
item['benefit_review'] = "Le schéma facultatif de plage permet les dérogations de maintien ou de reconstruction de L. 121-30 dans le champ des équipements et constructions de L. 121-28. L'évaluation de R. 104-17 demeure la garantie accompagnant cet avantage ; elle ne ferme ni son élaboration ni sa révision pour les futures opérations éligibles et ne réserve pas le dispositif aux droits acquis."

retained(
    'R104-17-1',
    "Maintien du contrôle environnemental des créations et extensions d'unités touristiques nouvelles soumises à autorisation qui peuvent affecter significativement Natura 2000. Cette protection vise des effets écologiques identifiés, non une formalité sans objet. L'article ne crée ni taxe ni nouvelle autorisation distincte de celles auxquelles il se réfère ; les autres unités restent au régime gradué de R. 104-17-2.",
    "R. 104-17-2, L. 104-2 et R. 122-8 ont été lus. La note de R. 122-8 rappelle l'annulation contentieuse de 2019 pour absence d'évaluation des UTN autorisées : aucune dispense générale ne peut être déduite d'une simplification nationale. La note source de 2021 garde son objet historique, sans étendre sa mention de PLU à toutes les UTN.",
    "Le cas Natura 2000 des UTN demeure identique à la source. Il n'est pas assimilé à une autorisation redondante supprimable ni à une mesure fiscale.",
    "Le maintien ne valide pas les autorisations des articles L. 122-20 et L. 122-21 et ne les réécrit pas. Les incidences de projet et le droit européen conservent leur champ distinct.",
    "Aucune charge nouvelle n'est identifiée : aucun site, document, délai ou justificatif supplémentaire n'est ajouté à la règle source conservée.",
)

retained(
    'R104-17-2',
    "Maintien de l'ensemble de la grille UTN hors R. 104-17-1 : 1° a) opérations des 1°, 5°, 7° et 8° de R. 122-8, b) filtrage des 4° et 6°, c) partage systématique/cas par cas pour les 2° et 3°, puis 2° UTN locales sous condition d'incidences notables. Ces subdivisions graduent déjà la charge selon les opérations. Une abrogation générale supprimerait la protection plutôt qu'un doublon ; aucune reformulation de remplissage n'est faite.",
    "R. 122-8 et R. 104-33 à R. 104-37 ont été lus intégralement ; ses seuils de qualification ne sont pas modifiés. Les renvois externes aux rubriques 43 a et 39 a de l'annexe de R. 122-2 environnement sont conservés exactement, sans inférer leur formule ou leur champ depuis le seul intitulé. Le tableau environnemental n'est pas fourni dans le lot et n'est pas déclaré vérifié. La note de 2021 reste historique ; aucune nouvelle exonération ni réduction de seuil n'est inventée.",
    "Tous les cas systématiques, les cas filtrés et le champ des UTN locales sont maintenus. Les filtrages existants ne sont pas comptés comme des allègements nouveaux.",
    "Les rubriques 43 a et 39 a du code de l'environnement ne sont pas réécrites ici ; leur concordance externe reste à contrôler sur leur texte officiel intégral. Ce maintien ne prétend pas achever l'audit des régimes de montagne.",
    "Aucune charge nouvelle n'est identifiée : aucune extension de catégorie, de seuil, de champ géographique ou de pièces ne résulte du maintien intégral de la source.",
)

retained(
    'R104-18',
    "Maintien intégral des sept composantes du rapport environnemental, y compris les deux branches du 3°, les incidences sanitaires, Natura 2000, les solutions raisonnables, les mesures et le suivi. Ces informations rendent effectives l'évaluation et la participation du public. La source exige un rapport, mais n'impose explicitement ni un nombre de copies ni un fichier matériel autonome : le seul regroupement sur un support commun ne suffit donc pas à démontrer une obligation supprimée. Aucun contenu nécessaire n'est retiré pour fabriquer un gain.",
    "L. 104-4 à L. 104-6 et R. 104-38 ont été lus : les informations raisonnablement exigibles et les procédures communes permettent déjà d'éviter certaines répétitions, sans effacer le rapport identifiable. Les sept rubriques et leurs renvois restent inchangés ; le rapport n'est exigé ici que pour les documents sans rapport de présentation. La note de l'article 26 du décret de 2021 conserve son champ historique. Les exigences de la directive 2001/42/CE et de Natura 2000 ne sont pas réputées abrogées ; aucune conformité européenne générale n'est certifiée.",
    "Le contenu intégral du rapport reste conservé. Aucun support distinct explicitement obligatoire n'étant établi dans la source, le maintien ne revendique ni fusion de pièces nouvelle ni diminution du coût des études.",
    "Les documents disposant déjà d'un rapport de présentation ne sont pas soumis ici à un second rapport. Les procédures communes de R. 104-38 et le droit européen restent à leur champ propre ; aucun coût net national n'est mesuré.",
    "Aucune charge nouvelle n'est identifiée : aucune des sept rubriques n'est étendue et aucun nouveau fichier, exemplaire, attestation, registre ou méthode d'étude n'est ajouté au texte maintenu.",
)

retained(
    'R104-19',
    "Maintien intégral de la proportionnalité du rapport aux effets et enjeux, de la possibilité de se référer aux études existantes et du cadrage seulement en tant que de besoin. Ce sont des garanties contre des exigences excessives, non une nouvelle démarche systématique. Le service d'appui et l'information des préfets organisent le cadrage sollicité ; aucun doublon de pièces n'est établi dans ce corps. La réutilisation déjà permise n'est pas présentée comme une invention.",
    "R. 104-18 est maintenu intégralement ; le renvoi au rapport environnemental demeure cohérent. L. 104-5 a été lu : les informations restent raisonnablement exigibles. L'avis de cadrage visé ici et l'avis final de R. 104-25 ont des objets différents. La note fixe l'entrée en vigueur ancienne au 1er septembre 2022, sans définir celle de la présente réforme. L'éventuel réemploi de données au titre du CRPA n'est pas compté en gain nouveau.",
    "La proportionnalité, le réemploi des renseignements et le caractère non systématique du cadrage restent entièrement conservés. Aucune obligation distincte n'est supprimée par ce maintien.",
    "Le texte ne dispense pas des analyses manquantes ou devenues inexactes. Le partage d'information légal et le fonctionnement des services restent à leur régime propre ; aucun solde de coût n'est estimé.",
    "Aucune charge nouvelle n'est identifiée : la consultation reste limitée au besoin et aucun justificatif de réutilisation ou nouveau registre n'est instauré.",
)

retained(
    'R104-20',
    "Maintien de l'exposé des motifs des changements, uniquement le cas échéant, dans le rapport existant lors d'une modification, mise en compatibilité ou révision. Il rend compréhensible l'évolution évaluée et son choix, sans imposer un rapport autonome ni une répétition de tout l'état initial. L'obligation ainsi ciblée sert l'information du public et le contrôle des raisons environnementales ; aucun doublon matériel obligatoire n'est démontré.",
    "Les renvois à R. 104-18 et au rapport de présentation demeurent opérants ; aucun second support n'est imposé par cet article. L. 104-3 et L. 104-4, lus, n'imposent pas par cet article une étude intégralement nouvelle si une actualisation suffit. La note de 2021 conserve son régime transitoire propre ; aucun calendrier historique n'est réutilisé comme date de réforme.",
    "L'obligation conditionnelle d'expliquer les changements dans le rapport existant reste identique. Elle ne crée pas un second rapport et aucun allègement nouveau n'est compté.",
    "Le maintien porte sur les motifs nécessaires aux évolutions du document, non sur une nouvelle évaluation systématique de toute modification. Les régimes de dispense et les transitions de champ restent distincts.",
    "Aucune charge nouvelle n'est identifiée : maintien des seuls motifs utiles, sans support supplémentaire, attestation ou obligation de refaire des analyses déjà valables.",
)

# Le changement d'autorité ne remet plus l'horloge à zéro.
src = BY_NUMBER['R104-21']['source_xml']
old = "Les délais prévus aux articles R. 104-25 et R. 104-31 courent à compter de la date de réception du dossier par la formation d'autorité environnementale de l'inspection générale de l'environnement et du développement durable. Celle-ci notifie à la personne publique responsable ce nouveau délai."
new = "Le changement d'autorité ne fait courir aucun nouveau délai. Les délais prévus aux articles R. 104-25 et R. 104-31 demeurent calculés à compter de la réception du dossier mentionné, selon le cas, à l'article R. 104-23 ou à l'article R. 104-29 par le service régional chargé de l'environnement. La formation d'autorité environnementale de l'inspection générale de l'environnement et du développement durable informe la personne publique responsable de l'échéance ainsi conservée, sans lui demander un nouveau dépôt du dossier."
assert old in src
prop = src.replace(old, new, 1).strip()
prop += "\n<p>L'absence de reprise des délais s'applique aux décisions de transfert prises à compter de l'entrée en vigueur de la présente réforme. Les transferts décidés auparavant conservent leur régime antérieur ; aucune échéance déjà acquise n'est reportée par la présente réforme.</p>"
rewritten(
    'R104-21', prop,
    "Suppression de la remise à zéro des délais lorsque le ministre confie le dossier à la formation nationale. L'autorité peut toujours être choisie selon la complexité et les enjeux, mais la circulation interne du dossier ne prolonge plus la procédure. Les deux listes de compétence, notamment les schémas de plage et les périmètres dépassant une région, le pouvoir motivé d'évocation et la transmission sans délai sont intégralement conservés.",
    "R. 104-23, R. 104-25, R. 104-29 et R. 104-31 ont été lus ; leurs dossiers et délais de trois mois pour l'avis et deux mois pour le cas par cas restent distincts. R. 104-25 est coordonné dans ce lot. Le délai du cas par cas reste assorti de l'obligation d'évaluation en l'absence de décision, non d'une dispense tacite. La transition conserve les transferts déjà décidés. La note du 1er septembre 2022 est historique ; aucun délai de réforme n'en est déduit. Les moyens de la formation nationale doivent être appréciés, sans créer de nouvelle étude ni délai additionnel.",
    impact(
        'material_reduction',
        "La source fait repartir à la réception nationale les délais d'avis et de cas par cas. Ce redémarrage est supprimé pour les transferts futurs : l'échéance demeure celle du dépôt régional initial. Les compétences et les garanties environnementales demeurent inchangées.",
        "Aucun nombre uniforme de jours gagnés n'est établi : le gain dépend du moment du transfert. Les transferts déjà décidés gardent l'ancien régime. Ni le délai de trois mois ni celui de deux mois n'est abaissé en lui-même ; aucun solde public n'est chiffré.",
        "Aucune charge nouvelle n'est identifiée : transfert et information de la personne publique existaient déjà. La formation nationale indique l'échéance conservée au lieu d'en annoncer une nouvelle ; aucun nouveau dépôt ni registre de suivi n'est imposé.",
        [effect(
            'deadline_reduced', 'urbanisme-delais-sans-reprise-apres-evocation',
            "Fin du redémarrage intégral des délais d'avis et de décision lors du transfert ministériel à la formation nationale.",
            "L'avis de R. 104-25 dispose de trois mois et la décision de R. 104-31 de deux mois à compter de la réception par la formation nationale après transfert, indépendamment du temps déjà écoulé au niveau régional.",
            "Les mêmes délais de trois mois ou deux mois restent calculés depuis la réception du dossier de R. 104-23 ou R. 104-29 au service régional ; le transfert ne les renouvelle pas.",
            'other',
            "Personnes publiques responsables dont un dossier relevant initialement de la mission régionale est transféré à la formation nationale par le ministre.",
            "Seulement pour les transferts décidés à compter de la réforme ; transferts anciens sous leur régime et aucune échéance acquise reportée.",
            "Pas de nouveau dépôt ; transmission et information existantes conservées. La disponibilité des moyens du service national n'est pas chiffrée.",
            old,
            "Le changement d'autorité ne fait courir aucun nouveau délai.",
        )],
    ),
    ["La reprise intégrale des délais de R. 104-25 et R. 104-31 à la réception du dossier par la formation nationale après évocation ministérielle est supprimée pour les décisions de transfert nouvelles."],
)

src = BY_NUMBER['R104-22']['source_xml']
old = "aux adaptations nécessaires d'un règlement ou d'une servitude mentionnés au deuxième alinéa de l'article L. 300-6"
new = "aux adaptations nécessaires d'un règlement ou d'une servitude dont l'adaptation est prévue à l'article L. 300-6"
assert old in src
prop = src.replace(old, new, 1).strip()
rewritten(
    'R104-22', prop,
    "Coordination nécessaire d'un renvoi devenu incohérent : le deuxième alinéa de L. 300-6 ne désigne plus les règlements et servitudes adaptés après l'insertion de l'énumération des projets. La référence vise directement les règlements et servitudes dont cet article prévoit l'adaptation. La compétence de droit commun et l'exception permettant une autorité commune au règlement ou à la servitude sont maintenues ; aucune suppression de contrôle n'est revendiquée.",
    "L. 300-6 a été lu intégralement dans sa version du 28 mai 2026 : la liste des documents adaptés figure après les cinq catégories de projets, et son propre renvoi ultérieur vise le huitième alinéa. Le renvoi ordinal ancien de R. 104-22 est donc une incohérence préexistante, corrigée expressément sans changer la liste matérielle. La note de l'ordonnance de 2016 distingue les projets au cas par cas au 1er janvier 2017, les projets systématiques au 16 mai 2017 et les plans/programmes selon la publication de l'enquête ou de la mise à disposition ; ces régimes ne sont pas réouverts ni supprimés par la correction du renvoi.",
    impact(
        'coordination_only',
        "La proposition répare le seul renvoi ordinal obsolète vers L. 300-6. La répartition des autorités et l'exception pour les adaptations restent identiques dans leur objet ; aucune obligation supprimée n'est comptée.",
        "Aucune réforme des documents énumérés par L. 300-6 ni de leurs procédures n'est réalisée ici. La correction ne vaut ni audit des autres renvois de ce texte ni validation de sa conformité européenne.",
        "Aucune charge nouvelle n'est identifiée : le renvoi corrigé désigne la même catégorie matérielle de règlements et servitudes, sans nouvelle autorité, information, demande ni délai.",
        [effect(
            'coordination', 'urbanisme-renvoi-adaptations-l300-6',
            "Correction du renvoi ordinal aux règlements et servitudes dont l'adaptation est prévue par L. 300-6.",
            "La compétence spéciale renvoie aux règlements ou servitudes du deuxième alinéa de L. 300-6, alinéa qui traite désormais d'une catégorie de projet.",
            "La compétence spéciale renvoie aux règlements ou servitudes dont L. 300-6 prévoit l'adaptation, sans élargir la liste.",
            'legal_duty',
            "Autorités et personnes publiques conduisant une déclaration de projet de l'Etat avec mise en compatibilité de PLU ou de SCoT et adaptation d'un règlement ou d'une servitude.",
            "Correction du renvoi applicable avec la nouvelle rédaction, sans reprise d'une procédure ni réouverture d'un délai historique de 2016 ou 2017.",
            "Aucun circuit, dossier ou contrôle de remplacement n'est instauré.",
            old, new,
        )],
    ),
)

retained(
    'R104-23',
    "Maintien intégral du dossier nécessaire à l'avis : projet de document, rapport environnemental seulement en l'absence de rapport de présentation et avis déjà rendus. Il ne prescrit ni exemplaires supplémentaires ni supports matériels distincts ; supprimer le rapport ou les avis priverait l'autorité d'éléments utiles sans doublon démontré. Le service d'appui prépare les informations et informe la mission sans délai, ce qui assure l'instruction et l'indépendance de la décision sans avis supplémentaire obligatoire dans cet article.",
    "L. 104-6, R. 104-18 et R. 104-25 ont été lus. Le dossier comprenant les pièces n'implique pas une seconde production des données déjà légalement disponibles ; les règles de réemploi applicables gardent leur effet, sans nouveau gain CRPA compté. La règle nouvelle d'évocation de R. 104-21 et R. 104-25 conserve le point de départ initial sans modifier les pièces du présent article. La note du 1er septembre 2022 reste une date historique et non celle de la réforme.",
    "Les trois catégories de pièces et le circuit d'appui restent inchangés. Aucune obligation expresse de support séparé ou d'exemplaires multiples n'étant établie, aucune fusion matérielle nouvelle n'est comptée.",
    "Les pièces nécessaires encore manquantes restent dues ; le réemploi de données déjà détenues n'est pas une nouvelle dispense créée ici. L'article ne réforme ni le délai ordinaire d'avis ni les droits de participation du public.",
    "Aucune charge nouvelle n'est identifiée : pas de pièce, bordereau, attestation de disponibilité ou registre ajouté et aucun nouvel avis distinct imposé par ce maintien.",
)

# Une consultation déjà expresse et suffisante n'est plus répétée.
src = BY_NUMBER['R104-24']['source_xml']
prop = src.strip()
dedup = "La consultation d'une autorité mentionnée au présent article n'est pas renouvelée, au titre du présent article ou de l'article R. 104-30, lorsque cette autorité a déjà rendu un avis exprès dans l'une de ces consultations sur le même projet de document et que cet avis couvre les informations du rapport ou du dossier soumis à l'autorité environnementale. Cette dispense ne s'applique pas lorsque l'évolution du projet ou des connaissances disponibles rend l'avis antérieur insuffisant pour apprécier les incidences relevant de la compétence de l'autorité consultée. Un avis tacite ne dispense pas d'une consultation ultérieure."
prop += '\n<p>' + dedup + '</p>'
prop += "\n<p>Cette dispense s'applique dès l'entrée en vigueur de la présente réforme aux consultations restant à engager, y compris dans les procédures en cours. Elle n'impose de refaire aucune consultation déjà réalisée et ne rouvre ni ne proroge aucun délai.</p>"
rewritten(
    'R104-24', prop,
    "Suppression ciblée d'une consultation répétée de la même autorité sanitaire ou du conseil des sites de Corse lorsque son avis exprès couvre déjà le même projet et les informations pertinentes. La consultation initiale et celle nécessaire à des données ou enjeux nouveaux restent obligatoires. Les catégories de documents, le ministre de la santé, l'ARS, le conseil des sites, le mois de réponse et le minimum de dix jours ouvrés en urgence sont intégralement conservés. Aucune autorisation n'est remplacée par une déclaration.",
    "R. 104-30 est coordonné dans ce lot sous la même mesure. La dispense ne repose ni sur un silence ancien ni sur la seule détention de données : il faut un avis effectivement rendu et encore suffisant sur les informations du dossier ; elle retire une seconde saisine obligatoire et ne se réduit pas au réemploi déjà permis par le CRPA. Les consultations environnementales, la participation du public et les besoins sanitaires nouveaux restent entiers. La directive 2001/42/CE ne peut être écartée ; l'adoption doit conserver l'effectivité de la consultation des autorités compétentes. La date de 2022 reste historique.",
    impact(
        'material_reduction',
        "La source impose la consultation sanitaire et, en Corse, celle du conseil des sites à réception du dossier sans exception de répétition. La proposition dispense la répétition si un avis exprès pertinent existe déjà au titre de R. 104-24 ou R. 104-30, sans supprimer la consultation initiale ni les consultations rendues nécessaires par une évolution.",
        "Le nombre de dossiers réunissant ces conditions et les jours effectivement gagnés ne sont pas connus. Un avis de simple filtrage qui ne couvre pas les informations du rapport complet ne suffit pas. Aucun gain fondé sur un simple échange de données ou solde national de complexité n'est revendiqué.",
        "Aucune charge nouvelle n'est identifiée : les conditions bornent une dispense facultative de fait, sans attestation de suffisance, nouveau registre ni avis de remplacement. Si l'avis est insuffisant ou tacite, la consultation déjà prévue par la source demeure.",
        [effect(
            'obligation_removed', 'urbanisme-consultations-environnementales-sans-doublon',
            "Retrait de la seconde consultation d'une même autorité lorsque son avis exprès couvre encore le dossier pertinent.",
            "Consultation du ministre de la santé ou de l'ARS à réception du dossier et du conseil des sites pour le PADDUC, sans dispense pour un avis exprès déjà rendu lors du cas par cas ; un mois et au moins dix jours ouvrés en urgence pour l'ARS.",
            "Même consultation et mêmes délais lorsqu'elle reste nécessaire ; pas de renouvellement si un avis exprès rendu au titre de R. 104-24 ou R. 104-30 couvre le même projet et les informations utiles, sans évolution le rendant insuffisant.",
            'legal_duty',
            "Autorité environnementale, services d'appui, autorités sanitaires et conseil des sites de Corse, ainsi que les personnes publiques responsables des documents concernés.",
            "Consultations non encore engagées dès la réforme, y compris procédures en cours ; aucun avis tacite ne suffit ; aucune réfection de consultation ni prorogation de délai.",
            "Aucune déclaration, attestation ou autre avis de substitution. L'examen de la pertinence sert uniquement à délimiter la dispense.",
            "Pour l'évaluation environnementale du plan d'aménagement et de développement durable de Corse, le conseil des sites de Corse est également consulté.",
            "La consultation d'une autorité mentionnée au présent article n'est pas renouvelée, au titre du présent article ou de l'article R. 104-30, lorsque cette autorité a déjà rendu un avis exprès dans l'une de ces consultations sur le même projet de document et que cet avis couvre les informations du rapport ou du dossier soumis à l'autorité environnementale.",
        )],
    ),
    ["La nouvelle saisine obligatoire d'une autorité déjà consultée au titre de R. 104-24 ou R. 104-30 est retirée lorsque son avis exprès couvre les informations pertinentes du même projet et demeure suffisant ; les consultations nécessaires restent dues."],
)

src = BY_NUMBER['R104-25']['source_xml']
old = "L'autorité environnementale formule un avis sur le rapport de présentation ou, à défaut, le rapport environnemental mentionné à l'article R. 104-18, et sur le projet de document dans les trois mois suivant la date de réception du dossier mentionné à l'article R. 104-23."
new = old + " Dans le cas du transfert prévu à l'article R. 104-21, cette réception s'entend de celle du dossier par le service régional chargé de l'environnement ; le transfert ne fait pas courir un nouveau délai."
assert old in src
prop = src.replace(old, new, 1).strip()
prop += "\n<p>La règle relative au transfert s'applique aux décisions de transfert prises à compter de l'entrée en vigueur de la présente réforme, dans les conditions transitoires fixées à l'article R. 104-21.</p>"
rewritten(
    'R104-25', prop,
    "Coordination nécessaire du point de départ avec R. 104-21 : la réception nationale après transfert ne peut rétablir le redémarrage supprimé. Le délai ordinaire de trois mois, la mise en ligne immédiate, toutes les transmissions, le rattachement à l'enquête ou à la participation électronique et l'absence d'observations réputée au terme du délai sont intégralement conservés. Il ne s'agit pas d'une seconde réduction autonome de délai.",
    "Version source du 5 août 2026. Les cibles R. 104-18 et R. 104-23 sont maintenues et gardent leur objet. R. 104-21 et R. 104-31 ont été lus pour distinguer l'avis sur l'évaluation de la décision de cas par cas : l'absence d'observation ici ne vaut pas dispense d'évaluation dans l'autre procédure. La règle ne s'applique qu'aux transferts nouveaux, sans déplacer les échéances déjà acquises des anciens transferts.",
    impact(
        'coordination_only',
        "Le premier alinéa identifie la réception régionale comme point de départ après un transfert nouveau. Cette précision met en œuvre la suppression de reprise dans R. 104-21 ; elle ne réduit pas une seconde fois le délai de trois mois.",
        "Aucun gain uniforme en jours n'est mesuré. Le délai ordinaire, les obligations de publicité et le régime du silence demeurent ; les transferts antérieurs restent régis par leur transition.",
        "Aucune charge nouvelle n'est identifiée : la précision du point de départ n'ajoute ni nouvelle publication, ni transmission, ni formulaire et conserve les obligations de publicité existantes.",
        [effect(
            'coordination', 'urbanisme-delais-sans-reprise-apres-evocation',
            "Coordination du délai d'avis de trois mois avec le maintien de son point de départ régional.",
            "Trois mois depuis la réception du dossier de R. 104-23, avec reprise nationale prévue par l'ancien R. 104-21.",
            "Trois mois depuis la réception régionale du dossier en cas de transfert nouveau ; publicité, transmissions et régime du silence inchangés.",
            'other',
            "Personnes publiques et autorités concernées par un transfert nouveau à la formation nationale pendant la consultation sur le rapport et le document.",
            "Même transition que R. 104-21 : décisions de transfert nouvelles seulement, sans report des échéances antérieures.",
            "Aucune formalité de remplacement ni nouveau dossier ; coordination d'une seule mesure de délai.",
            old,
            "Dans le cas du transfert prévu à l'article R. 104-21, cette réception s'entend de celle du dossier par le service régional chargé de l'environnement ; le transfert ne fait pas courir un nouveau délai.",
        )],
    ),
)

retained(
    'R104-26',
    "Maintien de la consultation transfrontalière lorsqu'un document peut avoir des incidences notables dans un autre Etat membre ou lorsque cet Etat la demande. Le même dossier que celui consulté par le public est transmis ; il n'est pas créé de rapport autonome. Le délai est un maximum de trois mois et le silence clôt déjà l'attente. L'information diplomatique et le relais préfectoral identifient les interlocuteurs internationaux : aucun doublon sans fonction établi ne justifie de les supprimer.",
    "L. 104-7 et R. 132-5 ont été lus. Le premier fonde la consultation des Etats concernés ; le second conserve les consultations facultatives de collectivités limitrophes et organismes étrangers. Le maximum de trois mois n'est ni un délai minimal ni une taxe. L'article met en œuvre les consultations transfrontières de la directive 2001/42/CE ; aucune abrogation nationale de cette exigence n'est proposée.",
    "Le déclenchement, le dossier déjà utilisé, le maximum de trois mois, l'avis réputé émis et le circuit diplomatique demeurent identiques à la source entière. Aucun nouveau gain de délai n'est compté.",
    "Ne couvre que les consultations sortantes vers un Etat membre, sans modifier les obligations internationales ni la procédure entrante de R. 104-27. Le texte européen intégral n'est pas joint et aucun coût global n'est chiffré.",
    "Aucune charge nouvelle n'est identifiée : aucun second dossier, destinataire additionnel, délai minimal ou nouvelle pièce n'est instauré dans la règle conservée.",
)

retained(
    'R104-27',
    "Maintien du circuit entrant des consultations transfrontalières : le préfet intéressé reçoit le dossier, peut consulter le public, convient du délai et transmet les résultats à l'Etat demandeur en informant les affaires étrangères. Ces étapes permettent de faire valoir les incidences en France et d'organiser une participation utile ; elles ne dupliquent pas la consultation sortante de R. 104-26. Aucun prélèvement ni délai minimal sans objet n'est présent.",
    "L. 104-8 et L. 104-7 ont été lus. La possibilité légale de consulter le public et la coordination internationale restent applicables ; le délai convenu ne devient pas un forfait de trois mois importé de l'article précédent. Le maintien ne prétend pas assurer à lui seul la conformité de toutes les consultations transfrontalières à la directive ou aux autres engagements internationaux.",
    "Les compétences, la possibilité de consulter le public, le délai convenu et la communication des résultats restent inchangés. Aucune suppression d'une prétendue double consultation n'est revendiquée.",
    "Le dispositif concerne un document provenant d'un autre Etat membre et non une demande française de permis. Aucun gain en jours ou économie nationale ne peut être déduit de son maintien.",
    "Aucune charge nouvelle n'est identifiée : aucun nouvel avis obligatoire, registre, collecte ou délai n'est ajouté aux échanges déjà prévus par la source.",
)

src = BY_NUMBER['R104-28']['source_xml']
old = "le service régional chargé de l'environnement (appui à la mission régionale d'autorité environnementale) instruit le dossier et transmet son avis à la mission régionale qui prend alors sa décision."
new = "le service régional chargé de l'environnement (appui à la mission régionale d'autorité environnementale) instruit le dossier pour la mission régionale, qui prend sa décision sans qu'un avis distinct de ce service soit requis."
assert old in src
prop = src.replace(old, new, 1).strip()
prop += "\n<p>La suppression de l'avis distinct obligatoire du service d'appui s'applique dès l'entrée en vigueur de la présente réforme aux dossiers nouveaux et aux dossiers en cours d'instruction. Un avis déjà établi peut être utilisé ; aucune pièce ni consultation déjà réalisée n'est à refaire et les délais en cours ne sont pas repris.</p>"
rewritten(
    'R104-28', prop,
    "Suppression de l'avis distinct obligatoirement émis par le service d'appui avant la décision de la mission régionale. Le service instruit toujours le même dossier pour la mission ; la mission conserve seule la décision, au regard des informations de R. 104-29 et des critères de la directive. Cette formalisation interne supplémentaire n'est pas nécessaire au maintien de l'instruction et de l'indépendance décisionnelle. Aucun avis sanitaire requis ni contrôle de la mission n'est supprimé.",
    "R. 104-3 à R. 104-5 et R. 172-1 restent les champs cités par la source, sans modification de leurs déclencheurs ; R. 172-1, R. 104-29, R. 104-31 et R. 104-32 ont été lus. Le délai de deux mois, la motivation, la publicité et l'évaluation exigible en cas de silence restent distincts et conservés. La suppression est celle d'un acte interne obligatoire, pas celle du service ou des informations d'instruction. La note du décret de 2022 ne fixe pas la date de la réforme ; les dossiers en cours ne sont pas recommencés.",
    impact(
        'material_reduction',
        "La source cumule instruction du service, avis de ce service et décision de la mission régionale. La proposition retire seulement l'avis interne distinct obligatoire ; instruction, informations du dossier et décision environnementale restent requis. C'est une formalité publique effectivement retirée, sans chiffrage de temps économisé.",
        "Le gain concerne le service régional et non un agrément privé supprimé. Les champs de R. 104-3 à R. 104-5 restent conservés sans réécriture ; les coûts et éventuelles organisations internes ne sont pas chiffrés.",
        "Aucune charge nouvelle n'est identifiée : l'instruction du même dossier reste assurée pour la mission, sans rapport d'instruction supplémentaire obligatoire ni attestation à fournir par la personne publique.",
        [effect(
            'obligation_removed', 'urbanisme-cas-par-cas-sans-avis-interne-obligatoire',
            "Retrait de l'avis distinct du service d'appui comme étape obligatoire préalable à la décision régionale de cas par cas.",
            "Le service régional instruit le dossier et doit transmettre son propre avis à la mission régionale qui décide ensuite.",
            "Le service instruit le dossier pour la mission ; un avis distinct peut exister mais n'est plus obligatoire. La mission régionale conserve sa décision et ses critères.",
            'legal_duty',
            "Services régionaux d'appui aux missions régionales d'autorité environnementale et missions régionales chargées du cas par cas relevant de R. 104-28.",
            "Application aux dossiers nouveaux et en cours dès la réforme ; avis déjà établis utilisables et aucun délai repris.",
            "Aucun rapport, attestation ou visa de substitution. Les informations et consultations déjà nécessaires demeurent dans l'instruction.",
            old, new,
        )],
    ),
    ["L'émission et la transmission obligatoires d'un avis distinct du service régional d'appui avant la décision de la mission régionale sont supprimées ; l'instruction du même dossier et la décision indépendante demeurent."],
)

src = BY_NUMBER['R104-29']['source_xml']
old = "Ce dossier est transmis à un stade précoce et avant la réunion d'examen conjoint prévue aux articles L. 123-22, L. 123-23, L. 143-44 et L. 153-54 du présent code ainsi qu'aux articles  L. 4424-15-1 ,  L. 4433-10-6  et  L. 4433-10-7  du code général des collectivités territoriales ou avant la soumission pour avis aux personnes publiques associées."
new = "Ce dossier est transmis à un stade précoce. Sous réserve des dispositions législatives imposant une évaluation environnementale avant l'examen conjoint, notamment du V de l'article L. 300-6-1, sa transmission et son examen peuvent se dérouler parallèlement à la réunion d'examen conjoint prévue aux articles L. 123-22, L. 123-23, L. 143-44 et L. 153-54 du présent code ainsi qu'aux articles L. 4424-15-1, L. 4433-10-6 et L. 4433-10-7 du code général des collectivités territoriales, ou à la consultation des personnes publiques associées. Cette conduite parallèle ne permet ni d'ouvrir une enquête publique ou une participation du public avec un dossier privé d'une pièce environnementale légalement requise, ni d'approuver le document avant l'achèvement de l'évaluation environnementale et des consultations applicables."
assert old in src
prop = src.replace(old, new, 1).strip()
prop += "\n<p>Cette faculté de conduite parallèle s'applique dès l'entrée en vigueur de la présente réforme aux procédures nouvelles et à celles en cours. Elle n'impose de refaire aucun dossier, avis ou examen conjoint et n'entraîne ni reprise des délais ni réouverture des décisions définitives.</p>"
rewritten(
    'R104-29', prop,
    "Réduction de fond du séquencement imposé : l'envoi au cas par cas reste précoce, mais n'a plus à précéder dans tous les cas la réunion d'examen conjoint ou la saisine des personnes publiques associées. Les travaux peuvent être conduits parallèlement lorsque la loi ne fixe pas une antériorité particulière. Les trois descriptions, dont vulnérabilité du territoire et incidences sanitaires, ainsi que les destinataires restent intégraux. L'obligation légale du V de L. 300-6-1 et la complétude du dossier présenté au public ne sont pas écartées.",
    "Lecture intégrale de L. 123-22, L. 123-23, L. 143-44, L. 153-54 et L. 300-6-1 : la procédure intégrée exige l'évaluation manquante avant l'examen conjoint et reste expressément réservée. Les trois références CGCT sont conservées avec réserve de leurs exigences législatives propres ; leurs textes intégraux ne sont pas fournis dans le corpus des cinq codes et leur éventuelle réforme n'est pas déclarée réalisée. R. 104-31 continue de régler le délai et le silence. La proposition ne supprime ni l'examen conjoint ni les consultations et ne rétablit aucun quota SRU. Aucun raccourcissement chiffré de la durée totale n'est avancé.",
    impact(
        'material_reduction',
        "La source impose une antériorité systématique de transmission avant examen conjoint ou saisine des personnes publiques associées. Cette contrainte réglementaire est retirée dans les cas où la loi autorise la conduite parallèle, tout en maintenant l'envoi précoce et les informations complètes. Il s'agit d'une liberté d'organisation, pas d'une suppression d'évaluation.",
        "Aucun nombre de jours gagnés n'est garanti : la source exigeait déjà une transmission, et non une décision de filtrage, avant la réunion. Les antériorités législatives, notamment la procédure intégrée, sont exclues du gain. Les textes CGCT extérieurs restent non réécrits et le solde global de coût est inconnu.",
        "Aucune charge nouvelle n'est identifiée : la conduite parallèle est permise, sans nouvelle consultation, donnée ou échéance autonome. Les réserves de complétude, d'évaluation et de participation maintiennent les exigences existantes et ne demandent aucune attestation supplémentaire.",
        [effect(
            'obligation_removed', 'urbanisme-examen-environnemental-procedures-paralleles',
            "Suppression de l'antériorité réglementaire obligatoire de la transmission au cas par cas sur l'examen conjoint ou la consultation des personnes publiques associées, hors exigences législatives.",
            "Transmission du dossier à un stade précoce et nécessairement avant la réunion d'examen conjoint ou la soumission pour avis aux personnes publiques associées, sans durée chiffrée.",
            "Transmission toujours précoce, mais transmission et examen peuvent être parallèles aux autres étapes quand aucune loi ne prescrit l'antériorité ; le dossier environnemental requis pour le public et avant approbation reste dû.",
            'legal_duty',
            "Personnes publiques responsables et services chargés des examens au cas par cas de R. 104-28 dans les procédures sans antériorité législative obligatoire.",
            "Procédures nouvelles et en cours dès la réforme, sans reprise de dossier ou de délai ; V de L. 300-6-1 et autres antériorités législatives réservés.",
            "Aucun dossier ou avis de remplacement ; les mêmes étapes peuvent seulement être organisées en parallèle. Aucun délai total de traitement n'est promis.",
            old,
            "Ce dossier est transmis à un stade précoce. Sous réserve des dispositions législatives imposant une évaluation environnementale avant l'examen conjoint, notamment du V de l'article L. 300-6-1, sa transmission et son examen peuvent se dérouler parallèlement à la réunion d'examen conjoint prévue aux articles L. 123-22, L. 123-23, L. 143-44 et L. 153-54 du présent code ainsi qu'aux articles L. 4424-15-1, L. 4433-10-6 et L. 4433-10-7 du code général des collectivités territoriales, ou à la consultation des personnes publiques associées.",
        )],
    ),
    ["L'obligation réglementaire générale de transmettre le dossier au cas par cas avant l'examen conjoint ou la saisine des personnes publiques associées est retirée lorsque la loi n'impose pas cette antériorité ; l'envoi précoce et les conditions législatives demeurent."],
)

src = BY_NUMBER['R104-30']['source_xml']
old_ref = "la décision implicite mentionnée à l'article R. 104-32"
new_ref = "la décision implicite mentionnée à l'article R. 104-31"
assert old_ref in src
prop = src.replace(old_ref, new_ref, 1).strip()
dedup_coord = "La dispense de renouvellement d'une consultation prévue à l'article R. 104-24 s'applique également aux consultations effectuées en application du présent article, dans les mêmes conditions et selon la même transition. Lorsqu'elle s'applique, aucune nouvelle saisine de l'autorité déjà consultée n'est exigée."
prop += '\n<p>' + dedup_coord + '</p>'
rewritten(
    'R104-30', prop,
    "Double coordination nécessaire : le renvoi de l'accusé de réception est corrigé vers R. 104-31, qui fait naître l'obligation implicite d'évaluation, et la dispense de consultation répétée de R. 104-24 est rendue expressément applicable. Le reçu, l'information de la mission, la consultation initiale, son mois de réponse et le minimum de dix jours ouvrés en urgence sont intégralement maintenus. Ni une deuxième réduction autonome ni une dispense tacite d'évaluation n'est créée.",
    "R. 104-31 et R. 104-32 ont été lus intégralement : la décision implicite relève du premier ; le second prévoit la publicité de la décision ou de son caractère tacite. Cette incohérence préexistante n'est pas conservée. La dispense reprend la même mesure que R. 104-24, pour avis exprès couvrant le même projet et des informations encore suffisantes, sans la présumer à partir d'un silence. Les consultations encore à engager bénéficient seules de sa transition ; aucun délai en cours n'est repris. La note d'entrée en vigueur de 2022 reste historique.",
    impact(
        'coordination_only',
        "La correction R. 104-32 vers R. 104-31 rétablit le bon fondement du silence sans en changer les effets. L'autre ajout rend applicable la dispense de consultation répétée définie dans R. 104-24 ; cette même mesure n'est pas comptée une seconde fois.",
        "La durée d'un mois, son abaissement possible en urgence et le plancher de dix jours ouvrés ne changent pas. Aucun dossier sans avis pertinent n'est dispensé par cette coordination ; le coût global n'est pas calculé.",
        "Aucune charge nouvelle n'est identifiée : mêmes reçu et consultations lorsqu'elles restent dues, sans justificatif, rapport de dispense ou nouvelle transmission. Le renvoi corrigé ne crée aucune sanction ni donnée nouvelle.",
        [
            effect(
                'coordination', 'urbanisme-consultations-environnementales-sans-doublon',
                "Application au cas par cas de la dispense bornée de renouvellement de consultation de R. 104-24.",
                "R. 104-30 prescrit de consulter sans délai les autorités de R. 104-24, sans dispense expresse pour un avis déjà rendu et toujours suffisant.",
                "La même consultation demeure, sous la dispense de R. 104-24 pour avis exprès antérieur pertinent ; aucun nouveau délai de consultation dans ce cas.",
                'legal_duty',
                "Services et autorités conduisant le cas par cas, autorités sanitaires et conseil des sites dans leur champ de compétence.",
                "Même transition que R. 104-24 : consultations restant à engager, y compris dans les procédures en cours, sans reprise ni prorogation de délai.",
                "Aucune formalité de remplacement ; renvoi à la seule dispense déjà définie dans R. 104-24.",
                "consulte sans délai les autorités mentionnées à l'article R. 104-24.",
                "Lorsqu'elle s'applique, aucune nouvelle saisine de l'autorité déjà consultée n'est exigée.",
            ),
            effect(
                'coordination', 'urbanisme-renvoi-decision-implicite-cas-par-cas',
                "Correction du fondement de la décision implicite annoncé dans l'accusé de réception.",
                "L'accusé annonce une décision implicite attribuée à R. 104-32, qui règle en réalité la publicité.",
                "L'accusé renvoie à R. 104-31, qui fixe le délai de deux mois et l'obligation d'évaluation en l'absence de décision.",
                'legal_duty',
                "Services accusant réception des dossiers et personnes publiques responsables soumises au cas par cas de R. 104-28.",
                "Correction de référence dès la nouvelle rédaction ; aucun délai expiré n'est rouvert et aucun effet de silence n'est modifié.",
                "Aucune nouvelle notification ou pièce ; seul le renvoi du reçu existant est corrigé.",
                old_ref, new_ref,
            ),
        ],
    ),
)

output = [ANSWERS[s['number']] for s in SOURCES]
assert len(output) == 24
for src, item in zip(SOURCES, output):
    if src.get('benefit_check_required'):
        assert len(item.get('benefit_review', '')) >= 100
Path('answer.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({
    'articles': len(output),
    'rewrite_draft': sum(a['status'] == 'rewrite_draft' for a in output),
    'retained_unchanged': sum(a['status'] == 'retained_unchanged' for a in output),
    'normative_reduction': sum(a.get('change_type') == 'normative_reduction' for a in output),
}, ensure_ascii=False))
