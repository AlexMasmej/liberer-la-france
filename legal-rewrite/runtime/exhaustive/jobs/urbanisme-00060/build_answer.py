import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
references = json.loads(Path('reference-targets.json').read_text())
by_number = {s['number']: s for s in sources}
answers = {}


def impact(classification, assessment, scope, burdens, effects=None):
    return {
        'version': 1,
        'classification': classification,
        'assessment': assessment,
        'scope_limitations': scope,
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


def base(number):
    s = by_number[number]
    return {k: s[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}


def retain(number, reason, notes, assessment, scope, burdens, benefit=None):
    a = base(number)
    a.update(proposed_xml=None, reason=reason, review_notes=notes,
             status='retained_unchanged', classification='retained_necessary',
             substantive_impact=impact('retained_necessary', assessment, scope, burdens))
    if benefit:
        a['benefit_review'] = benefit
    answers[number] = a


def draft(number, xml, reason, notes, assessment, scope, burdens, effects,
          removed=None, classification='material_reduction'):
    a = base(number)
    a.update(proposed_xml=xml, reason=reason, review_notes=notes, status='rewrite_draft',
             substantive_impact=impact(classification, assessment, scope, burdens, effects))
    if removed:
        a.update(change_type='normative_reduction',
                 reform_policy_id='editorial_direction_2026_10_19', removed_provisions=removed)
    answers[number] = a


retain(
    'R121-1-2',
    "Maintien intégral après examen du délai et du renvoi : les quatre mois déterminent la naissance d'un rejet implicite de la dérogation littorale pour les ouvrages du réseau public de transport d'électricité. Ils n'imposent pas d'attendre quatre mois pour délivrer une autorisation expresse. L'instruction porte sur un bilan technique, financier et environnemental, des avis et des conditions de localisation sensibles ; supprimer cette règle ne supprimerait ni la demande ni ces contrôles. Faire naître le refus plus tôt ne constituerait pas un allègement favorable démontré.",
    "R.* 121-1-1 et L. 121-5-2 officiels lus intégralement dans le corpus local, avec leurs notes vides. Le premier règle le silence des deux ministres ; le second conserve la dérogation, les avis dont l'avis local sous un mois, les possibilités d'enfouissement ou de lignes aériennes et les protections des espaces remarquables. Le délai de quatre mois n'est ni celui de participation du public ni un accord tacite. Aucun dépôt, justificatif ou prélèvement propre à R121-1-2 n'est identifié. Aucune modification des demandes en cours ni des délais de recours n'est introduite.",
    "Aucun changement normatif : maintien du délai de quatre mois avant rejet implicite, sans le compter comme une réduction de délai ou une autorisation supprimée.",
    "La durée administrative optimale n'est pas chiffrée ; aucun gain sur la délivrance des autorisations ni aucune suppression des contraintes environnementales n'est revendiqué.",
    "Aucune charge nouvelle n'est identifiée : le texte source est maintenu sans nouvelle pièce, notification, condition ou échéance."
)

retain(
    'R121-3',
    "Maintien intégral de la désignation de la Seine, de la Loire et de la Gironde. Elle détermine le champ territorial des protections et exceptions des articles L121-15 et L121-20, sans procédure individuelle de classement ni obligation déclarative pour les riverains. La supprimer rendrait ces renvois indéterminés et retirerait une protection de fond, plutôt qu'un doublon administratif.",
    "L121-15, L121-20, L121-13 et L121-16 à L121-19, sources et notes, ont été lus en entier. Les deux premiers étendent respectivement les règles des espaces proches et de la bande littorale aux grands estuaires. Les voies favorables d'extension limitée et les exceptions pour les activités nécessitant l'eau restent à leur champ propre. La liste de trois estuaires n'est pas étendue. Aucune filiation SRU n'est déduite du seul numéro de l'article.",
    "La liste géographique est conservée exactement ; aucune taxe, formalité ou autorisation supplémentaire n'est retirée par cet article.",
    "Les règles législatives auxquelles la liste donne un champ territorial restent distinctes ; aucune réduction de leur intensité ni examen des 209 articles SRU n'est affirmé.",
    "Aucune charge nouvelle n'est identifiée : maintien de trois désignations existantes, sans dossier ni décision individuelle supplémentaire."
)

retain(
    'R121-3-1',
    "Maintien intégral de l'autorité de délivrance de la dérogation solaire littorale. Cet article ne crée pas une seconde autorisation : il désigne le ministre qui délivre celle prévue par L121-12-1. Une suppression isolée ne libérerait pas le projet de l'autorisation législative et priverait la dérogation de son autorité compétente. L'examen de la biodiversité, des paysages, de la salubrité et de la sécurité justifie de conserver la décision expresse requise pour cette exception.",
    "L121-12-1 officiel et sa proposition locale ont été lus ; la source entière distingue les friches inscrites sur une liste réglementaire, les bassins de saumure saturée, les installations couplées de stockage ou d'hydrogène du II et le stockage limité à l'énergie solaire du site au III. Avis de la commission, comparaison avec la renaturation et étude du pétitionnaire ne sont pas effacés par la seule désignation du ministre. Les opérations futures éligibles conservent cette voie favorable ; aucun nouvel agrément ni dossier n'est ajouté.",
    "Désignation ministérielle maintenue, sans nouveau corps normatif ni suppression fictive d'une seconde autorisation qui n'existe pas dans la source.",
    "Aucun gain de décentralisation ou de délai n'est établi ; les conditions de L121-12-1 et les autres autorisations éventuellement nécessaires restent hors de cette seule désignation.",
    "Aucune charge nouvelle n'est identifiée : l'autorité et la voie de dérogation restent celles de la source, sans formalité de remplacement."
)

retain(
    'R*121-3-2',
    "Maintien intégral du silence valant rejet pour la dérogation de L121-12-1. Une absence de réponse ne démontre ni l'examen des conditions de biodiversité, de paysage, de sécurité et de salubrité, ni la comparaison requise avec la renaturation. Transformer ce silence en autorisation retirerait cette garantie substantielle. Le rejet implicite n'abolit pas la possibilité d'une décision expresse favorable pour les projets recevables.",
    "Renvoi L121-12-1 vérifié sur ses I, II et III officiels entiers ; R121-3-1 attribue la compétence au ministre et R121-3-3 conserve le délai de quatre mois. Il n'est pas créé d'autorisation tacite de stockage, de solaire ou d'hydrogène. Cette réserve ne prétend pas que tout projet du dispositif est nécessairement soumis à la même procédure environnementale européenne : les obligations supérieures gardent leur champ propre. Les exonérations et dérogations littorales ne sont pas fermées pour l'avenir.",
    "Le régime du silence est conservé ; aucune simplification matérielle ni délai réduit n'est compté.",
    "Le maintien porte sur le seul effet du silence ministériel. Il ne démontre ni durée réelle d'instruction ni conformité européenne de l'ensemble des projets.",
    "Aucune charge nouvelle n'est identifiée : maintien du régime existant sans déclaration, justificatif ou condition de fond supplémentaire."
)

retain(
    'R121-3-3',
    "Maintien intégral du délai de quatre mois de rejet implicite. Ce délai concerne une demande exceptionnelle sur le littoral impliquant l'étude des atteintes et, sur les friches, la comparaison avec la renaturation. Il ne constitue pas un délai minimal interdisant une réponse favorable plus rapide. Son raccourcissement isolé provoquerait un refus implicite plus tôt, sans suppression de la demande ni démonstration d'une délivrance facilitée.",
    "R.*121-3-2, R121-3-1 et L121-12-1 ont été confrontés en entier. Le délai source est quatre mois, sans nouveau délai intermédiaire ni changement de point de départ. Les situations en cours et les recours ne sont pas modifiés. Une réduction éventuelle du temps d'instruction effectif demanderait de traiter les opérations et contrôles concernés, et ne peut être déduite d'une naissance anticipée du rejet.",
    "Aucune modification par rapport à la source officielle entière : le délai de rejet implicite reste de quatre mois, sans revendication de gain administratif.",
    "Aucune évaluation empirique de la durée nécessaire n'est disponible ; le maintien protège la cohérence de la dérogation, sans garantir une décision dans un délai réel donné.",
    "Aucune charge nouvelle n'est identifiée : aucun changement de délai, pièce, notification ou condition d'accès à la dérogation."
)

retain(
    'R121-4',
    "Maintien intégral des huit catégories d'espaces et milieux et de la précision relative aux activités et équipements de gestion ou de mise en valeur. Le texte assure une protection écologique de fond, notamment pour les habitats d'oiseaux, les zones humides et les milieux littoraux fragiles. Il ne contient ni taxe, ni dossier périodique, ni agrément distinct à supprimer. Retirer une catégorie effacerait une protection essentielle et pourrait affecter les dérogations qui s'articulent à cette liste.",
    "L121-23 et L121-24 ont été lus en entier. Les huit numéros, le seuil de 1 000 hectares du 2°, la directive 2009/147/CE du 6°, les renvois aux protections d'espèces et de sites et la dernière phrase sont conservés par maintien de la source. La référence plus ancienne à la directive 79/409 CEE dans L121-23 appelle une coordination de ce texte législatif, non une suppression des habitats dans R121-4. Les articles environnementaux cités ne sont pas fournis intégralement dans le corpus des cinq codes consulté : aucun effacement de leurs contraintes n'est présumé. Les possibilités de R121-5 restent ouvertes.",
    "La liste et les conditions écologiques demeurent intégrales ; aucune baisse de prélèvement ni suppression de formalité n'est comptée.",
    "Les protections de l'environnement et des espèces extérieures au corpus n'ont pas fait l'objet d'une réécriture dans ce lot ; leur contrôle et leur articulation restent distincts.",
    "Aucune charge nouvelle n'est identifiée : les catégories, seuils, renvois et précisions des documents d'urbanisme sont ceux de la source entière."
)

retain(
    'R121-5',
    "Maintien intégral de la liste favorable des aménagements légers. Les six catégories, les trois branches a, b et c du 4° et les conditions communes permettent des équipements, activités et travaux dans des espaces normalement protégés. Leurs limitations de dimension, de localisation, de revêtement et de réversibilité ont une fonction de protection écologique identifiable. Les supprimer indistinctement ou abroger la liste priverait les opérations futures de dérogations utiles ; aucune taxe ou formalité autonome n'est imposée par cette liste.",
    "L121-24, R121-4, R121-6 et R*420-1 ont été lus intégralement, notes comprises. Le renvoi R.420-1 correspond à R*420-1 du corpus, définition de l'emprise avec exclusions des ornements et de certains débords ; cette définition n'est pas élargie. Sont conservés les cinquante mètres carrés simultanément pour plancher et emprise du 4°a et les cinq mètres carrés du 4°c, l'exclusion de l'hébergement au 4°, l'absence d'accroissement de capacité du 2° et le retour à l'état naturel pour les 1°, 2°, 4° et les réfections et extensions du 3°. La référence historique à la loi du 31 décembre 1913 au 5° reste signalée : sa concordance patrimoniale n'est pas documentée par un texte extérieur complet ici et n'est pas remplacée au hasard. R121-6 est allégé sans fermer cette liste ni modifier les quinze jours et les huit jours de L121-24. Aucun schéma de plage ni dérogation littorale n'est abrogé.",
    "Tous les aménagements recevables et leurs conditions restent ouverts, y compris pour les opérations futures. Ce maintien utile n'est pas compté comme une nouvelle réduction.",
    "Aucun élargissement des dimensions ni des catégories n'est proposé ; les autorisations et participations prévues par L121-24 restent distinctes de la liste favorable.",
    "Aucune charge nouvelle n'est identifiée : la source est maintenue intégralement, sans attestation, déclaration ou condition d'accès supplémentaire.",
    "Les avantages possibles sont les permissions de chacun des six numéros : au 1°, équipements démontables de préservation, restauration, accueil, observation, cheminements, sanitaires et secours ; au 2°, aires de stationnement de résorption ; au 3°, réfection et extension économique limitée ; au 4°a, activités agricoles, pastorales et forestières jusqu'aux deux limites de cinquante mètres carrés ; au 4°b, activités aquatiques, salicoles et ovines exigeant l'eau ; au 4°c, canalisations enfouies et aménagements jusqu'à cinq mètres carrés ; au 5°, gestion et remise en état du patrimoine bâti ; au 6°, équipements d'intérêt général de sécurité et de préservation. Tous restent applicables aux nouvelles situations éligibles comme aux situations antérieures, avec leurs conditions communes de paysage et de préservation, l'exclusion de l'hébergement au 4°, les nécessités techniques propres à b et c, les conditions de stationnement et la réversibilité expressément prévue. Aucun avantage n'est réservé au stock ancien. Il ne s'agit pas d'exonérations fiscales : aucune taxe correspondante n'est supprimée ou remplacée dans cet article."
)

xml6 = """<p>Les aménagements légers mentionnés à l'article R. 121-5 qui ne sont pas soumis à enquête publique en application du 1° du I de l'article L. 123-2 du code de l'environnement font l'objet d'une mise à disposition du public organisée par l'autorité compétente pour statuer sur la demande d'autorisation du projet. Aucun arrêté distinct n'est requis pour organiser cette mise à disposition.</p>
<p>Un avis précisant la nature des documents communiqués au public et les modalités de leur mise à disposition est affiché dans la ou les mairies des communes intéressées ainsi que sur le lieu où est projetée l'implantation de l'aménagement, dans des conditions qui garantissent le respect du site ou du paysage concerné. L'affichage de cet avis au siège de l'établissement public de coopération intercommunale n'est pas obligatoire. Les délais d'information préalable et de mise à disposition, la possibilité de formuler des observations, leur enregistrement et leur conservation ainsi que le bilan préalable à la décision prévus à l'article L. 121-24 demeurent applicables.</p>
<p>Ces dispositions s'appliquent aux mises à disposition dont les modalités sont portées à la connaissance du public à compter de l'entrée en vigueur du présent article. Les arrêtés et affichages déjà intervenus conservent leur validité ; aucune nouvelle publicité ni reprise des délais n'est exigée à raison de cette seule réforme.</p>"""
draft(
    'R121-6', xml6,
    "Réforme de fond : supprimer l'arrêté distinct obligatoire organisant la mise à disposition et l'affichage supplémentaire au siège de l'EPCI, tout en conservant l'information dans chaque mairie et sur le site. L121-24 impose déjà de porter les documents et modalités à la connaissance du public : l'avis exécute cette obligation, sans nouvel acte préalable distinct. La participation et ses garanties restent intégrales ; la dérogation d'aménagement léger demeure ouverte pour l'avenir.",
    "L121-24 entier impose au moins quinze jours de mise à disposition, une information au moins huit jours avant, les observations enregistrées et conservées et le bilan avant décision : rien de cela n'est retiré. R121-5 reste entier. La nouvelle mention de l'avis ne crée pas une seconde publicité ; elle remplace l'affichage de l'arrêté par celui des informations déjà légalement exigées. L'affichage des mairies et du site est maintenu avec le respect du paysage. L'enquête et l'avis de la commission dans leurs champs législatifs ne sont pas dispensés. Le renvoi environnemental de la source est conservé sans en inventer le contenu extérieur au corpus. Cette mesure ne ferme pas le schéma de plage et ne porte pas sur ses règles propres de R121-7 et R121-8.",
    "Deux obligations administratives précises disparaissent : prendre un arrêté distinct et afficher au siège de l'EPCI. Le contenu de l'information et la participation du public subsistent ; aucune réduction des délais de protection n'est revendiquée.",
    "L'allègement ne vaut que pour les aménagements de R121-5 hors enquête publique et pour les nouvelles mises à disposition. Le coût administratif net et l'effet sur les délais réels ne sont pas chiffrés.",
    "Aucune charge nouvelle n'est identifiée : l'avis conserve les informations et affichages déjà requis par L121-24 et R121-6, sans dépôt ni déclaration du pétitionnaire en remplacement de l'arrêté.",
    [
        effect('obligation_removed', 'littoral-mise-a-disposition-sans-arrete',
               "Suppression de l'acte administratif distinct organisant la mise à disposition.",
               "L'autorité compétente doit organiser la mise à disposition par un arrêté distinct, pour les aménagements légers non soumis à enquête publique.",
               "La même autorité organise la participation sans arrêté distinct ; l'information législativement requise est affichée par avis.", 'legal_duty',
               "Autorités compétentes et porteurs des aménagements légers de R121-5 hors enquête publique.",
               "Modalités rendues publiques après l'entrée en vigueur ; anciens arrêtés valables, aucun nouveau dépôt ni recommencement.",
               "Information, huit jours préalables, quinze jours de participation, observations et bilan conservés ; pas de déclaration de remplacement.",
               "Les aménagements légers mentionnés à l'article R. 121-5 qui ne sont pas soumis à enquête publique en application du 1° du I de l'article L. 123-2 du code de l'environnement font l'objet d'une mise à disposition du public organisée par un arrêté de l'autorité compétente pour statuer sur la demande d'autorisation du projet.",
               "Aucun arrêté distinct n'est requis pour organiser cette mise à disposition."),
        effect('obligation_removed', 'littoral-affichage-siege-epci-suppression',
               "Suppression du seul emplacement supplémentaire obligatoire d'affichage au siège de l'EPCI.",
               "L'arrêté est également affiché, le cas échéant, au siège de l'EPCI compétent en planification, en plus des mairies et du site.",
               "L'affichage au siège de l'EPCI devient facultatif ; l'avis reste affiché dans les mairies intéressées et sur le site.", 'legal_duty',
               "Autorités organisant la mise à disposition publique des aménagements légers littoraux.",
               "Nouvelles publicités à compter de l'entrée en vigueur ; les publicités déjà réalisées restent valides.",
               "Aucun affichage nouveau ajouté ailleurs ; maintien des emplacements des mairies et du projet déjà exigés.",
               "Cet arrêté est affiché dans la ou les mairies des communes intéressées et, le cas échéant, au siège de l'établissement public de coopération intercommunale compétent en matière de plan local d'urbanisme, de document en tenant lieu ou de carte communale, ainsi que sur le lieu où est projetée l'implantation de l'aménagement, dans des conditions qui garantissent le respect du site ou du paysage concerné.",
               "L'affichage de cet avis au siège de l'établissement public de coopération intercommunale n'est pas obligatoire.")
    ],
    ["Obligation de prendre un arrêté distinct pour organiser la mise à disposition du public des aménagements légers concernés.",
     "Affichage obligatoire supplémentaire au siège de l'EPCI compétent, en plus des mairies et du lieu du projet."]
)

retain(
    'R121-9',
    "Maintien intégral de l'assiette de trois mètres et des réserves des articles R121-10 à R121-18. Il s'agit de l'exécution de la servitude législative d'accès piéton, non d'une taxe ou d'un dossier supplémentaire. La largeur détermine aussi la limite de la charge foncière ; l'abroger sans traiter L121-31 retirerait la précision protectrice sans supprimer légalement la servitude.",
    "L121-31, R121-10 à R121-18 ont été lus en entier. Le point de départ est la limite du domaine public maritime, avec les possibilités de délimitation, modification, suspension et les garanties d'habitation. La ponctuation isolée finale de la source est une anomalie matérielle sans effet normatif ; elle ne justifie pas un nouveau corps stylistique. Les allègements de R121-15 et R121-18 ne rendent pas le renvoi de plage incohérent et ne suppriment pas ses protections.",
    "La largeur de trois mètres et les réserves d'application restent celles de la source ; aucun allègement matériel n'est attribué à ce maintien.",
    "Le maintien ne modifie ni le tracé effectif des servitudes existantes ni les procédures de modification ou d'indemnisation.",
    "Aucune charge nouvelle n'est identifiée : ni élargissement de la bande, ni nouvelle démarche, ni nouvelle catégorie de propriétaires assujettis."
)

retain(
    'R121-10',
    "Maintien intégral des quatre points de départ de l'assiette. La définition évite qu'une limite discrétionnaire augmente la charge des riverains et articule le passage avec les différentes composantes du domaine public maritime. Elle ne prescrit pas d'autorisation, de déclaration ou de document à remettre par les propriétaires ; aucune formalité autonome n'est donc supprimable ici.",
    "Les quatre subdivisions et les renvois aux 1°, 3° et dernier alinéa de L2111-4 et à L2111-6 du CG3P sont conservés. Le CG3P n'est pas disponible en texte intégral dans le corpus des cinq codes fourni : la concordance actuelle du dernier alinéa et les règles détaillées de domanialité restent à contrôler sur cette source publique extérieure, sans prétendre l'avoir lue ni substituer une subdivision supposée. Aucune incohérence n'est établie par les pièces locales. R121-9, R121-11 et L121-31 ont été confrontés : le droit de demander une délimitation est préservé.",
    "Aucun changement normatif : les limites et les catégories de terrains restent intégrales, sans baisse fictive d'obligation.",
    "La vérification externe des deux articles du CG3P est une limite documentaire explicite ; aucune réécriture de ce code ou modification de son domaine public n'est affirmée.",
    "Aucune charge nouvelle n'est identifiée : les limites, les renvois et les personnes concernées ne sont pas modifiés."
)

retain(
    'R121-11',
    "Maintien intégral du droit du riverain de demander la délimitation du domaine public maritime, tant en l'absence d'acte que lorsque l'évolution naturelle admissible a modifié le niveau des plus hautes eaux. Cette faculté protège contre une assiette incertaine de servitude et ne constitue pas une demande obligatoire. Supprimer la faculté retirerait un droit favorable sans alléger une charge.",
    "Les deux alinéas sont maintenus, avec le préfet comme destinataire et l'exclusion des perturbations météorologiques exceptionnelles dans le second. Les articles R121-9 et R121-10 ont été confrontés. Aucun formulaire exclusif, justificatif imposé, taxe ni délai minimal ne figure dans cette source. Aucun renvoi au contrat de travail n'existe et la demande du propriétaire n'est pas transformée en obligation périodique de délimitation.",
    "La faculté de délimitation reste intégralement ouverte aux propriétaires futurs et actuels ; ce maintien n'est pas une nouvelle mesure de réduction.",
    "Les modalités domaniales extérieures à cet article et le délai réel de traitement ne sont ni modifiés ni évalués dans ce lot.",
    "Aucune charge nouvelle n'est identifiée : la demande reste facultative et ses deux cas d'ouverture ne sont pas restreints."
)

retain(
    'R121-12',
    "Maintien intégral de la faculté de modifier le tracé et les caractéristiques de la servitude, notamment pour l'évolution prévisible du rivage. La souplesse protège la continuité du sentier tout en renvoyant aux garanties des propriétaires. Abroger ce fondement retirerait une possibilité d'adaptation favorable et ne supprimerait pas la servitude légale. L'article ne demande lui-même ni taxe ni dossier additionnel.",
    "L121-32 et R121-14 à R121-18, R121-21, R121-22 et R121-25 ont été lus en entier ; R121-23 et R121-24 ont également été consultés. La plage de renvois demeure valable malgré les allègements ciblés des autres articles du lot. R121-18 conserve les preuves scientifiques en cas d'évolution du rivage, sans imposer cette preuve pour chaque autre modification. Le texte n'autorise pas une disparition générale de l'enquête, des garanties d'habitation ou des droits de recours.",
    "Maintien sans modification de la voie d'adaptation de la servitude ; aucune nouvelle suppression d'obligation n'est attribuée au renvoi lui-même.",
    "Les réductions identifiées dans les règles de dossier ou de participation sont évaluées dans leurs articles propres et ne sont pas recomptées ici.",
    "Aucune charge nouvelle n'est identifiée : les finalités, les titulaires de la compétence et les renvois de procédure restent inchangés."
)

retain(
    'R121-13',
    "Maintien intégral des six cas non exhaustifs de suspension exceptionnelle. Ils évitent des charges inutiles lorsque le passage existe ailleurs et protègent services, activités professionnelles, ports, défense, sites fragiles et stabilité des sols. Ce sont des possibilités de dérogation à conserver pour les situations futures, non des obligations nouvelles à supprimer au seul motif de leur appartenance au chapitre littoral.",
    "Les six numéros et la dernière phrase renvoyant à R121-16 à R121-18 et R121-20 à R121-25 restent intacts. Les textes de ces plages présents au corpus ont été lus, y compris R121-23 et R121-24. Le caractère exceptionnel et la décision au titre de L121-32 demeurent ; la suspension n'est pas rendue automatique. La dispense très limitée de mise en sécurité dans R121-26 ne vaut ni suspension juridique générale ni modification durable de tracé. L'enquête et les droits des tiers continuent dans leur champ.",
    "Les six voies de suspension et leur caractère non exhaustif restent ouverts ; aucune procédure ou taxe distincte n'est retirée par cet article.",
    "L'effet des décisions individuelles de suspension et leur coût ne sont pas évalués ; les modifications des articles de procédure ne sont pas comptées une seconde fois.",
    "Aucune charge nouvelle n'est identifiée : aucun motif de suspension n'est supprimé ou soumis à une pièce nouvelle."
)

retain(
    'R121-14',
    "Maintien intégral des trois possibilités de réduire la distance de quinze mètres pour les habitations. Elles concilient le passage avec la configuration des lieux, les passages déjà ouverts et la position des murs, sans demande d'agrément distincte dans cet article. Les supprimer fermerait des dérogations favorables ; supprimer les garanties législatives de l'habitation ne constituerait pas un simple allègement de dossier.",
    "L121-32 et L121-33 entiers confirment la protection des habitations et terrains concernés au 1er janvier 1976 et les exceptions de continuité ou d'accès au rivage. R121-15 maintient la voie d'accord du propriétaire dans les autres cas en simplifiant seulement son support. Les trois numéros de R121-14, la réserve initiale du 1° de L121-32 et la distance de quinze mètres restent exactement ceux de la source. R121-17 conserve la justification particulière et le plafond de trois mètres du passage.",
    "Les trois dérogations de distance sont conservées pour les nouveaux projets recevables ; elles ne sont pas présentées comme trois allègements nouvellement créés.",
    "Aucune réduction générale de la distance protégée ni dispense de décision d'institution ou de modification de servitude n'est proposée ici.",
    "Aucune charge nouvelle n'est identifiée : les cas, les conditions physiques et les réserves législatives ne changent pas."
)

xml15 = """<p>Dans les autres cas que ceux mentionnés à l'article R. 121-14, la distance de quinze mètres peut également être réduite avec l'accord du propriétaire du bâtiment. Cet accord peut être exprimé par tout écrit signé du propriétaire et n'est pas subordonné à la conclusion d'une convention avec une collectivité publique ou un groupement de collectivités publiques. Une telle convention reste un mode valable d'expression de cet accord. Le silence du propriétaire ne vaut pas accord.</p>
<p>Ces dispositions s'appliquent aux accords donnés à compter de l'entrée en vigueur du présent article. Les conventions valablement conclues antérieurement, les actes régulièrement pris sur leur fondement et les droits et obligations qui en résultent sont conservés. L'accord ne dispense pas de la décision et des procédures requises pour instituer ou modifier la servitude.</p>"""
draft(
    'R121-15', xml15,
    "Réforme de fond : retirer la convention obligatoire avec une personne publique comme mode exclusif de consentement à la réduction des quinze mètres. Un écrit signé du propriétaire suffit désormais, sans contre-signature conventionnelle imposée. Le consentement effectif reste indispensable et la convention demeure possible, notamment pour des engagements supplémentaires librement consentis. La décision de servitude et ses garanties ne sont pas remplacées par ce seul écrit.",
    "Les cas propres de R121-14, la protection de L121-33 et les justifications et largeur maximale de R121-17 restent distincts. L'écrit signé atteste le consentement déjà requis ; aucun formulaire, notarisation, justificatif supplémentaire ou enregistrement spécial n'est créé. La précision excluant le silence protège le caractère réel de cet accord sans retirer une voie antérieure d'accord tacite, inexistante dans la convention imposée. Les conventions anciennes ne sont pas déliées de leurs engagements et la faculté nouvelle est ouverte aux opérations futures. Publicité et recours de la décision de servitude restent applicables selon leurs fondements.",
    "Suppression de l'obligation de conclure une convention publique pour utiliser la dérogation consensuelle de distance ; le propriétaire conserve la maîtrise de son accord et l'autorité prend toujours la décision requise.",
    "Aucune suppression de la servitude, de la protection des habitations ou des autres actes nécessaires n'est démontrée. L'économie de négociation et de signature n'est pas chiffrée.",
    "Aucune charge nouvelle n'est identifiée : la signature remplace l'accord conventionnel déjà obligatoire, sans donnée nouvelle ni déclaration de remplacement. La voie conventionnelle et ses avantages restent disponibles.",
    [effect('obligation_removed', 'littoral-accord-riverain-sans-convention',
            "Suppression du caractère obligatoire de la convention publique pour matérialiser le consentement du propriétaire.",
            "Le propriétaire doit consentir par une convention passée avec une collectivité publique ou un groupement pour réduire la distance hors R121-14.",
            "Tout écrit signé du propriétaire peut exprimer l'accord ; la convention publique reste facultative et la décision de servitude demeure nécessaire.", 'legal_duty',
            "Propriétaires de bâtiments et personnes publiques portant une modification de servitude hors des cas de R121-14.",
            "Accords donnés après l'entrée en vigueur ; conventions, actes et droits antérieurs préservés.",
            "Consentement écrit et effectif conservé ; ni contre-signature publique obligatoire ni formalité nouvelle de publicité de l'accord lui-même.",
            "Cet accord doit résulter d'une convention passée avec une collectivité publique ou un groupement de collectivités publiques.",
            "Cet accord peut être exprimé par tout écrit signé du propriétaire et n'est pas subordonné à la conclusion d'une convention avec une collectivité publique ou un groupement de collectivités publiques.")],
    ["Convention obligatoire avec une collectivité publique ou un groupement comme mode exclusif de l'accord du propriétaire à la réduction de distance."]
)

for number, old_phrase in [
    ('R121-16', 'renseignements délivrés par le conservateur des hypothèques au vu du fichier immobilier'),
    ('R121-19', 'renseignements délivrés par le conservateur des hypothèques au vu du fichier immobilier'),
]:
    s = by_number[number]
    new_phrase = 'renseignements délivrés au vu du fichier immobilier'
    xml = s['source_xml'].replace(old_phrase, new_phrase)
    assert xml != s['source_xml']
    xml += "<p>Les listes et pièces déjà établies restent utilisables ; cette coordination n'impose ni nouveau dossier ni nouvelle délivrance de renseignements et n'ouvre aucun accès aux données en dehors des conditions légalement applicables.</p>"
    longitudinal = number == 'R121-16'
    draft(
        number, xml,
        "Coordination nécessaire à droit constant : retirer la désignation nominative du conservateur des hypothèques comme fournisseur des renseignements, tout en maintenant le fichier immobilier comme source, le cadastre et tous autres moyens déjà admis. La liste des propriétaires reste nécessaire à leur information et à la protection des droits fonciers. Le texte ne prescrivait pas une voie exclusive d'obtention ; aucune nouvelle dispense de justificatif n'est donc revendiquée.",
        ("Les quatre subdivisions et leur ordre sont conservés : notice, plan parcellaire avec tracé et largeur, liste communale des propriétaires, zones de suspension et motifs avec les modifications antérieures. R121-17 et R121-18 conservent leur articulation avec la notice et les preuves nécessaires. " if longitudinal else
         "Les quatre subdivisions et leur ordre sont conservés : notice justifiant L121-34, plan de l'itinéraire, plan parcellaire et liste communale des propriétaires. L121-34 officiel entier conserve les chemins privés d'usage collectif, l'exclusion professionnelle et l'absence d'accès public à moins de cinq cents mètres. ") +
        "La référence fonctionnelle évite de lier le dossier à une ancienne désignation personnelle ; elle ne fixe pas un nouveau titulaire ou une nouvelle compétence de publicité foncière. Les conditions d'accès au cadastre et au fichier immobilier ne sont pas modifiées. Le régime organique de publicité foncière extérieur aux cinq codes n'est pas réécrit. Les facultés déjà ouvertes par « tous autres moyens » restent identiques, sans économie CRPA nouvelle comptée. Les pièces existantes ne sont pas refaites.",
        "Seule la désignation du fournisseur des renseignements est coordonnée ; les quatre éléments du dossier demeurent. Aucune suppression d'une liste, d'un plan ou d'une collecte obligatoire n'est imputée à cette correction.",
        "Les régimes d'accès et de publicité foncière extérieurs au corpus ne sont pas réécrits ; aucun nouveau droit d'accès ni gain chiffré de conformité n'est démontré.",
        "Aucune charge nouvelle n'est identifiée : mêmes informations, mêmes moyens ouverts, réutilisation des pièces existantes et aucun dossier ou accès de données ajouté.",
        [effect('coordination', 'littoral-reference-fichier-immobilier',
                "Référence fonctionnelle au fichier immobilier sans désignation personnelle du fournisseur de renseignements.",
                "Le fichier immobilier peut fournir les renseignements de la liste des propriétaires, avec mention du conservateur des hypothèques ; cadastre et autres moyens sont déjà possibles.",
                "Les mêmes renseignements au vu du même fichier restent utilisables sans désigner ce titulaire, aux conditions légales d'accès inchangées.", 'other',
                "Services constituant les dossiers de servitude littorale et propriétaires dont l'identification est nécessaire.",
                "Coordination des textes ; les listes et pièces déjà établies restent utilisables sans nouvelle délivrance.",
                "Aucun remplacement de dossier, aucune donnée supplémentaire et aucun accès automatique nouveau.",
                old_phrase, new_phrase)],
        classification='coordination_only'
    )

retain(
    'R121-17',
    "Maintien intégral de la justification particulière lorsque le tracé atteint les habitations ou terrains historiquement protégés, et du plafond de trois mètres. La justification démontre la nécessité de l'atteinte aux droits fonciers ; ce n'est pas une pièce redondante de simple identité. La supprimer affaiblirait le contrôle de la dérogation de L121-33. La source n'impose pas de support matériel distinct de la notice de R121-16 : aucune fusion nouvelle n'est fabriquée.",
    "Les deux numéros conservent les références au 1er janvier 1976, les murs en matériaux durables adhérant au sol, les bâtiments concernés et les quinze mètres. Les renvois L121-32, R121-13 et R121-14 ont été lus en entier. Le maximum de trois mètres s'applique aux deux cas. La simplification du consentement de R121-15 ne remplace pas cette justification et la limitation scientifique de R121-18 ne dispense pas de la démonstration foncière particulière. Aucun déplacement de subdivision n'est effectué.",
    "Les garanties renforcées des habitations et le plafond de passage restent intégraux ; aucune prétendue suppression d'une seconde notice n'est comptée.",
    "Le texte ne couvre que les deux situations historiques décrites et n'étend pas leur protection à une population nouvelle ; les règles générales de servitude restent distinctes.",
    "Aucune charge nouvelle n'est identifiée : mêmes deux cas, mêmes justifications, mêmes dates et largeur maximale, sans support ou attestation nouveau."
)

xml18 = """<p>Lorsque la modification du tracé en application de l'article R. 121-12 est motivée par l'évolution prévisible du rivage, le dossier contient les observations et informations fournies par des procédés scientifiques qui motivent le nouveau tracé.</p>
<p>Les autres modifications du tracé ne sont pas subordonnées à la production d'observations et d'informations fournies par des procédés scientifiques sur le seul fondement du présent article. Les pièces et justifications requises par les articles R. 121-16 et R. 121-17 demeurent exigibles dans leur champ respectif. Cette dispense ne s'étend pas aux études ou évaluations exigées sur un autre fondement.</p>
<p>Cette limitation de l'exigence scientifique s'applique à compter de l'entrée en vigueur du présent article, y compris aux procédures en cours, sans nouveau dossier ni recommencement des enquêtes ou de leurs délais. Les éléments déjà recueillis restent au dossier et les décisions régulièrement prises auparavant demeurent valables.</p>"""
draft(
    'R121-18', xml18,
    "Réduction de fond : réserver les observations et informations scientifiques obligatoires aux modifications motivées par l'évolution prévisible du rivage. R121-12 vise aussi la continuité face aux obstacles et l'adaptation du passage ; imposer cette catégorie de preuve à toute modification ne se justifie pas pour une simple adaptation locale sans motif d'évolution du rivage. Les justifications du tracé, les garanties d'habitation, l'enquête et les études légalement autonomes sont maintenues.",
    "L121-32 et R121-12, R121-16, R121-17 ont été lus en entier. L'évolution prévisible exige encore la base scientifique source ; une modification comportant ce motif n'est pas dispensée parce qu'elle comporte aussi un autre motif. La dispense ne vaut que pour l'exigence propre à R121-18 : sécurité, stabilité des sols, études environnementales et autres preuves nécessaires restent opposables selon leur fondement. Pas de déclaration du propriétaire certifiant l'absence d'évolution, pas de registre ni de formulaire de remplacement. Les éléments anciens restent utilisables sans réouverture des enquêtes.",
    "L'exigence scientifique générale de la source est réellement réduite : elle cesse pour les modifications non motivées par l'évolution prévisible du rivage, tout en restant entière pour ce motif et pour les études autonomes.",
    "Le nombre de dossiers dispensés et le coût des études ne sont pas connus. Aucune dispense de toute preuve de nécessité ou de toute étude environnementale n'est revendiquée.",
    "Aucune charge nouvelle n'est identifiée : le motif d'évolution délimite l'exigence conservée ; il n'impose ni attestation d'exemption, ni déclaration ni étude de remplacement.",
    [effect('obligation_removed', 'littoral-preuve-scientifique-limitee-au-rivage',
            "Retrait de l'exigence scientifique propre à R121-18 pour les modifications sans motif d'évolution prévisible du rivage.",
            "Toute modification de tracé par R121-12 doit comporter les observations et informations scientifiques motivant le nouveau tracé.",
            "Cette catégorie de preuve reste obligatoire pour l'évolution prévisible du rivage ; elle n'est plus imposée par R121-18 pour les autres modifications.", 'legal_duty',
            "Services et opérations de modification de servitude longitudinale non motivée par l'évolution prévisible du rivage.",
            "Entrée en vigueur, procédures en cours incluses sans reprise de l'enquête ; pièces et décisions antérieures conservées.",
            "Justifications foncières et études exigées sur des fondements autonomes maintenues ; aucune certification de dispense ajoutée.",
            "Lorsque le tracé est modifié en application de l'article R. 121-12, le dossier contient en outre les observations et informations fournies par des procédés scientifiques qui motivent le nouveau tracé.",
            "Les autres modifications du tracé ne sont pas subordonnées à la production d'observations et d'informations fournies par des procédés scientifiques sur le seul fondement du présent article.")],
    ["Production systématique d'observations et d'informations scientifiques au titre de R121-18 pour les modifications sans motif d'évolution prévisible du rivage."]
)

retain(
    'R121-20',
    "Maintien intégral de l'enquête publique et de l'articulation avec les garanties particulières de visite et de rectification. L'enquête permet de contester une charge foncière et de faire connaître l'incidence sur l'accès au rivage ; elle a une fonction essentielle de participation et de protection des propriétaires. Cet article de renvoi ne crée pas de dossier périodique, prélèvement ou autorisation distincte à retirer.",
    "R121-16, R121-19, R121-21 et R121-22 ont été lus en entier ; les allègements des trois derniers textes concernés n'orphelinent pas ce renvoi. Le chapitre IV du titre III du livre Ier du CRPA n'est pas reproduit dans le corpus fourni : ses articles détaillés ne sont pas réputés vérifiés par une lecture externe interdite. La proposition maintient son champ, sans inventer de délai CRPA. Les procédures de délibération communale et d'approbation ont leur coordination propre dans la proposition locale de R121-23, distincte de cette enquête.",
    "Renvoi général et réserves particulières maintenus, sans compter une nouvelle fusion ou suppression d'enquête.",
    "Les dispositions détaillées du CRPA restent une limite documentaire extérieure au lot ; aucune simplification de ce code n'est prétendue.",
    "Aucune charge nouvelle n'est identifiée : aucune nouvelle enquête, pièce, consultation ou condition n'est créée par le maintien intégral."
)

xml21 = """<p>Le commissaire enquêteur ou la commission d'enquête peut décider de procéder à une visite des lieux. Dans ce cas, le commissaire enquêteur ou le président de la commission avise le maire et convoque sur place les propriétaires intéressés ainsi que les représentants des administrations. Après les avoir entendus, il consigne le déroulement de la réunion et les observations recueillies soit dans un procès-verbal, soit dans une partie identifiable des conclusions transmises au préfet en application de l'article R. 121-22. Aucun procès-verbal distinct n'est requis lorsque ces éléments figurent dans ces conclusions.</p>
<p>Cette faculté de regroupement s'applique aux réunions tenues à compter de l'entrée en vigueur du présent article. Les procès-verbaux déjà établis restent au dossier et n'ont pas à être reproduits dans les conclusions.</p>"""
draft(
    'R121-21', xml21,
    "Réduction de fond : supprimer le caractère nécessairement distinct du procès-verbal de visite lorsque le déroulement et les observations figurent déjà dans une partie identifiable des conclusions d'enquête. Le commissaire peut conserver un procès-verbal s'il le juge utile. La visite reste facultative, mais l'avis au maire, les convocations et l'audition des propriétaires et administrations restent entiers.",
    "R121-20 et R121-22 officiels lus : la transmission des conclusions au préfet est déjà prescrite par la dernière phrase de R121-22. Aucun nouveau rapport d'enquête n'est créé ; le contenu probatoire du compte rendu est intégré à un document existant, ou reste dans un procès-verbal. L'identification de cette partie évite la perte des observations utiles au contrôle et aux recours. Aucun consentement des propriétaires à une atteinte foncière n'est présumé de leur présence ou absence. Les procès-verbaux antérieurs ne sont pas recopiés. Le renvoi ajouté à R121-22 est une cible locale lue en entier, extérieure à la liste des trois cibles de contrat unique qui ne concerne que R121-26.",
    "La visite ne requiert plus un procès-verbal séparé quand son compte rendu figure dans les conclusions déjà dues ; les mêmes acteurs restent informés et entendus.",
    "Le gain ne concerne que les visites suivies d'une intégration effective du compte rendu dans les conclusions. Aucun nombre de visites, coût ou gain global de délai n'est établi.",
    "Aucune charge nouvelle n'est identifiée : la consignation remplace le procès-verbal déjà imposé et les conclusions existent déjà ; aucune signature, donnée ou audition supplémentaire n'est ajoutée.",
    [effect('obligation_merged', 'littoral-visite-compte-rendu-integre',
            "Regroupement facultatif du compte rendu de visite dans les conclusions déjà transmises au préfet.",
            "Après la réunion de visite, un procès-verbal est obligatoire, en plus de la transmission des conclusions exigée par R121-22.",
            "Le même compte rendu peut figurer dans une partie identifiable des conclusions, sans procès-verbal séparé ; un procès-verbal reste possible.", 'legal_duty',
            "Commissaires enquêteurs et commissions réalisant une visite des lieux pour la servitude littorale.",
            "Réunions postérieures à l'entrée en vigueur ; procès-verbaux antérieurs gardés sans recopie.",
            "Avis, convocations, auditions et trace du déroulement et des observations conservés ; aucun document de remplacement supplémentaire.",
            "Après les avoir entendus, il dresse procès-verbal de la réunion.",
            "Aucun procès-verbal distinct n'est requis lorsque ces éléments figurent dans ces conclusions.")],
    ["Procès-verbal obligatoirement distinct de la réunion de visite lorsque son contenu est intégré aux conclusions d'enquête déjà transmises."]
)

xml22 = """<p>Si le commissaire enquêteur ou la commission d'enquête propose de rectifier le tracé ou les caractéristiques de la servitude qui ont été soumis à enquête, et si ces rectifications tendent à appliquer la servitude à de nouveaux terrains, les propriétaires de ces terrains en sont avisés par lettre. Un avis au public est, en outre, affiché à la mairie. Un délai de quinze jours au moins à compter de l'accomplissement de l'information des propriétaires et de l'affichage de l'avis est accordé à toute personne intéressée pour prendre connaissance à la mairie des rectifications proposées et présenter des observations. Ce délai peut courir pendant celui fixé par l'arrêté prescrivant l'ouverture de l'enquête et ne s'y ajoute pas systématiquement. Si la durée restant à courir est insuffisante, l'enquête est prolongée du temps nécessaire pour assurer ces quinze jours au moins.</p>
<p>A l'expiration du délai d'enquête, le commissaire enquêteur ou le président de la commission d'enquête transmet le dossier avec ses conclusions au préfet.</p>
<p>Ces dispositions s'appliquent aux rectifications dont l'information des propriétaires et l'affichage sont accomplis à compter de l'entrée en vigueur du présent article. Les rectifications déjà portées à la connaissance des intéressés avant cette date conservent le délai supplémentaire antérieurement applicable. Aucun délai d'observations expiré n'est rouvert et aucune décision régulièrement prise n'est remise en cause.</p>"""
draft(
    'R121-22', xml22,
    "Réduction de fond : retirer l'addition systématique d'au moins quinze jours à la durée initiale d'enquête quand les rectifications et leur publicité peuvent être utilement examinées pendant l'enquête en cours. Chaque intéressé conserve au moins quinze jours à partir de l'information des propriétaires et de l'affichage ; la prolongation reste obligatoire pour compléter cette garantie si nécessaire. Les nouveaux propriétaires reçoivent toujours leur lettre et l'avis reste affiché à la mairie.",
    "R121-20 et R121-21 sont maintenus dans leur champ ; les conclusions restent transmises après la clôture effective. La durée protectrice de quinze jours n'est pas diminuée et le point de départ exige l'accomplissement des deux informations, non une date antérieure à l'une d'elles. Aucun mode de lettre, accusé supplémentaire ou registre nouveau n'est imposé. La proposition locale de R121-23, lue, mentionne encore un délai « supplémentaire de quinze jours » : son alinéa transitoire doit être coordonné en remplaçant cette qualification par le délai minimal d'observations de R121-22, sans remettre en vigueur la délibération communale ou les deux mois supprimés. Ce compagnon, hors articles assignés, n'est pas modifié ici. Les droits déjà ouverts au délai additionnel sont préservés. Ces quinze jours d'enquête ne sont ni le préavis foncier de R121-26 ni le préavis de rupture du contrat de travail.",
    "Suppression du seul cumul automatique de la durée initiale et de quinze jours supplémentaires. Le délai utile de participation reste au moins quinze jours ; le gain dépend de la date de publicité des rectifications et peut être nul.",
    "Seules les nouvelles publicités après entrée en vigueur sont concernées ; anciens délais supplémentaires conservés. Coordination du libellé de la proposition R121-23 à réaliser hors lot ; aucune accélération forfaitaire de quinze jours n'est promise.",
    "Aucune charge nouvelle n'est identifiée : lettre, affichage, observations et transmission sont déjà requis. La garantie minimale est conservée, sans accusé, registre, pièce ni consultation de remplacement.",
    [effect('deadline_reduced', 'littoral-rectifications-delai-non-cumulatif',
            "Suppression de l'addition automatique des quinze jours d'observations à la durée initiale de l'enquête.",
            "En cas de nouveaux terrains, au moins quinze jours sont accordés en sus du délai fixé par l'arrêté initial, après information et publicité des rectifications.",
            "Au moins quinze jours utiles restent accordés après accomplissement de l'information et de l'affichage ; ils peuvent se dérouler pendant la durée initiale, prolongée seulement du reliquat nécessaire.", 'calendar_days',
            "Projets de servitude rectifiés vers de nouveaux terrains, propriétaires nouvellement concernés et autres personnes intéressées.",
            "Nouvelles informations et publicités après entrée en vigueur ; le délai supplémentaire reste acquis aux rectifications déjà rendues publiques.",
            "Les deux informations et les quinze jours minimaux restent obligatoires ; aucune formalité nouvelle ni suppression des observations.",
            "Un délai de quinze jours au moins, en sus de celui fixé par l'arrêté prescrivant l'ouverture de l'enquête, est accordé à toute personne intéressée pour prendre connaissance à la mairie des rectifications proposées et présenter des observations.",
            "Ce délai peut courir pendant celui fixé par l'arrêté prescrivant l'ouverture de l'enquête et ne s'y ajoute pas systématiquement.")],
    ["Addition systématique d'au moins quinze jours au délai initial d'enquête, même lorsque les rectifications sont publiées assez tôt pour être examinées pendant ce délai."]
)

retain(
    'R121-25',
    "Maintien intégral de la signalisation nécessaire et de la substitution préfectorale après mise en demeure infructueuse. La signalisation détermine où le public peut passer et évite les intrusions hors assiette ainsi que les risques pour les usagers. Elle sert donc aussi la protection des propriétaires. La substitution vise une carence de signalisation, sans rapport avec la carence SRU supprimée ; la retirer rendrait l'obligation de sécurité inopérante.",
    "R121-26 et R121-28 officiels ont été lus en entier : accès de l'administration pour établir les panneaux et travaux, préavis de quinze jours sauf urgence, prise en charge des dépenses par l'Etat et participation facultative des collectivités ou organismes. R121-25 ne transfère pas ces dépenses au propriétaire et ne crée ni rapport, ni taxe, ni déclaration privée. La mise en demeure reste une garantie préalable à la substitution, non un délai minimal de construction.",
    "La signalisation nécessaire et sa garantie d'exécution restent intègres ; aucune nouvelle réduction matérielle n'est attribuée à ce maintien de sécurité.",
    "Les coûts de signalisation et les modalités d'intervention ne sont pas chiffrés ; la suppression de la carence SRU ne s'étend pas à cette compétence de signalisation.",
    "Aucune charge nouvelle n'est identifiée : pas de panneau supplémentaire imposé par le projet, de contribution privée ou de procédure périodique ajoutée."
)

xml26 = """<p>La servitude entraîne pour les propriétaires des terrains et leurs ayants droit : <br />1° L'obligation de laisser aux piétons le droit de passage ; <br />2° L'obligation de n'apporter à l'état des lieux aucune modification de nature à faire, même provisoirement, obstacle au libre passage des piétons, sauf autorisation préalable accordée par le préfet, pour une durée de six mois au maximum. L'autorisation préalable n'est pas requise pour les seules mesures immédiatement nécessaires à la protection des personnes contre un danger grave et imminent. Cette dispense ne vaut que pendant le temps strictement nécessaire à la mise en sécurité, dans la limite de six mois ; elle ne permet ni de modifier durablement le tracé ni de supprimer la servitude. Le passage est rétabli dès que la mise en sécurité le permet. Aucune déclaration ne se substitue à l'autorisation ainsi écartée ; <br />3° L'obligation de laisser l'administration compétente établir la signalisation prévue à l'article R. 121-25 et effectuer les travaux nécessaires pour assurer le libre passage et la sécurité des piétons, sous réserve d'un préavis de quinze jours sauf cas d'urgence.</p>
<p>La dispense prévue au 2° s'applique aux mesures prises à compter de l'entrée en vigueur du présent article. Les autorisations antérieures conservent leurs effets dans les limites de leur durée ; la dispense ne prolonge pas ces autorisations. Elle ne vaut ni suspension juridique de la servitude ni dispense des autorisations exigées sur un autre fondement. Les actes régulièrement pris auparavant, les droits à indemnisation légalement ouverts et les voies de recours sont préservés.</p>"""
draft(
    'R121-26', xml26,
    "Réduction de fond ciblée : retirer l'autorisation préfectorale préalable pour la seule mise en sécurité immédiate contre un danger grave et imminent. Faire attendre cette autorisation avant l'intervention nécessaire ne protège pas les personnes. Aucun dépôt ou déclaration ne remplace le visa retiré. La servitude, l'interdiction ordinaire d'obstacle, l'autorisation pour les autres obstacles temporaires et son maximum de six mois, l'accès des services et le préavis foncier de quinze jours sauf urgence restent en place.",
    "Les 1°, 2° et 3° demeurent dans cet ordre ; les six mois restent le maximum de l'autorisation ordinaire et bornent aussi la dispense, laquelle cesse plus tôt dès la mise en sécurité. Le rétablissement du passage explicite la portée temporaire de l'exception, sans transformer celle-ci en suspension de L121-32 ou en modification de tracé. R121-13, R121-25, R121-27, R121-28, R121-31 et L121-31 à L121-37 ont été lus en entier : finalité piétonne, sécurité, compétence, dépenses de l'Etat, indemnisation du dommage direct, matériel et certain, exclusion de responsabilité civile propre au passage et règles de restitution gardent leur champ. Les obstacles d'urgence licites ne sont pas assimilés par R121-31 à des obstacles placés en violation de R121-26 ; les infractions autonomes restent distinctes. Les trois cibles de reference-targets ont été lues en entier, propositions et notes comprises ; elles concernent les relations de travail et non ces propriétaires. Le préavis foncier n'est pas converti en quinze jours calendaires de rupture et aucune condition d'ancienneté ou indemnité salariale n'est introduite.",
    "Une autorisation préalable est effectivement écartée dans le cas strict de la sécurité immédiate ; le contrôle ordinaire des autres obstacles et le droit de passage restent entiers. Aucune suppression générale des servitudes n'est revendiquée.",
    "La dispense ne couvre ni les travaux ordinaires, ni les modifications durables, ni les autorisations sectorielles autonomes. Le nombre d'interventions concernées et le coût net ne sont pas établis.",
    "Aucune charge nouvelle n'est identifiée : pas de déclaration, registre ou justification à déposer. Danger grave et imminent, nécessité et durée limitent une dispense nouvelle ; ils ne restreignent pas la voie d'autorisation ordinaire, et le rétablissement du passage découle de son obligation existante.",
    [effect('authorization_removed', 'littoral-securite-urgence-dispense-autorisation',
            "Suppression de l'autorisation préfectorale préalable pour l'obstacle provisoire strictement nécessaire à une mise en sécurité immédiate.",
            "Toute modification faisant même provisoirement obstacle au passage requiert une autorisation préfectorale, accordée au maximum pour six mois ; le 2° ne prévoit pas d'exception de danger imminent.",
            "Les seules mesures immédiatement nécessaires face à un danger grave et imminent sont dispensées, le temps de la mise en sécurité au plus six mois ; les autres obstacles gardent leur autorisation.", 'legal_duty',
            "Propriétaires de terrains grevés et ayants droit devant prendre immédiatement une mesure de protection des personnes.",
            "Mesures prises après entrée en vigueur ; autorisations anciennes non prolongées, droits et recours antérieurs préservés.",
            "Aucune déclaration de remplacement ; remise en libre passage dès la sécurité acquise, aucune suspension juridique ou modification durable permise.",
            "2° L'obligation de n'apporter à l'état des lieux aucune modification de nature à faire, même provisoirement, obstacle au libre passage des piétons, sauf autorisation préalable accordée par le préfet, pour une durée de six mois au maximum ;",
            "L'autorisation préalable n'est pas requise pour les seules mesures immédiatement nécessaires à la protection des personnes contre un danger grave et imminent.")],
    ["Autorisation préfectorale préalable de l'obstacle temporaire pour les seules mesures immédiatement nécessaires à la protection contre un danger grave et imminent."]
)

r26 = answers['R121-26']
ref_assessments = {
    'L1234-1': "Le préavis de R121-26 informe le propriétaire de l'accès de l'administration pour panneaux ou travaux ; il ne notifie aucun licenciement. Les conditions officielles d'ancienneté de moins de six mois, de six mois à moins de deux ans et d'au moins deux ans, comme la proposition de quinze jours calendaires des nouveaux contrats, sont donc inapplicables. Les anciens contrats gardent leur transition propre. Le préavis foncier de quinze jours sauf urgence demeure sans renvoi ajouté au droit du travail.",
    'L1221-2': "La servitude et son autorisation temporaire de six mois ne sont ni un contrat d'emploi ni un CDD. La proposition L1221-2 impose une durée indéterminée aux nouveaux emplois privés et préserve les anciens contrats ; elle ne s'étend pas aux obligations d'un propriétaire ou d'un ayant droit. La dispense foncière d'urgence n'ouvre aucun terme automatique d'emploi et ne modifie pas les aides ou droits des futurs salariés éligibles.",
    'L1234-9': "R121-26 ne rompt aucun emploi et ne prévoit aucune indemnité ordinaire de licenciement. La source L1234-9 vise huit mois d'ancienneté ; la proposition préserve cette ouverture pour les anciens contrats et prévoit, pour les nouveaux, un an à la fin effective, préavis inclus, puis 0,20 mois sur toute l'ancienneté au prorata des mois complets, avec plafond de six mois. Ces règles salariales sont hors champ. L'indemnisation foncière de L121-35 et L121-36 reste autonome, sans cette ancienneté ni ce plafond salarial, et ses droits futurs restent ouverts.",
}
required = references['requirements'][r26['code_id'] + '|' + r26['source_id']]
r26['reference_checks'] = [
    {'target_key': k, 'view_sha256': references['targets'][k]['view_sha256'],
     'assessment': ref_assessments[references['targets'][k]['number']]}
    for k in required
]

assert set(answers) == set(by_number)
output = [answers[s['number']] for s in sources]
Path('answer.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
print('answer.json:', len(output), 'articles')
