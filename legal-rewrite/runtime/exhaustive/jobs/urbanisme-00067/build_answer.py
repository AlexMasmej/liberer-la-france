import html
import json
import re
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
answers = {}


def plain(xml):
    return html.unescape(re.sub(r'<[^>]*>', '', xml or '')).strip()


def impact(classification, assessment, limitations, burdens, effects=None):
    return {
        'version': 1,
        'classification': classification,
        'assessment': assessment,
        'scope_limitations': limitations,
        'new_burdens_review': burdens,
        'effects': effects or [],
    }


def effect(kind, measure, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    return {
        'kind': kind, 'measure_id': measure, 'description': description,
        'before': before, 'after': after, 'unit': unit,
        'affected_population': population,
        'conditions_and_transition': transition,
        'replacement_or_new_burdens': burdens,
        'source_quote': source_quote, 'proposed_quote': proposed_quote,
    }


def put(i, xml, reason, notes, assessment, benefit=None, removed=None, repeal=None):
    s = sources[i]
    a = {k: s[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    a.update(proposed_xml=xml, reason=reason, review_notes=notes,
             status='retained_unchanged' if xml is None else 'rewrite_draft',
             substantive_impact=assessment)
    if xml is None:
        a['classification'] = 'retained_necessary'
    if benefit:
        a['benefit_review'] = benefit
    if removed:
        a.update(change_type='normative_reduction',
                 reform_policy_id='editorial_direction_2026_10_19',
                 removed_provisions=removed)
    if repeal:
        a.update(change_type='full_repeal',
                 repeal_policy_id='editorial_direction_2026_10_19',
                 repeal_scope=repeal)
    answers[i] = a


def keep(i, reason, notes, assessment, limitations, benefit=None):
    put(i, None, reason, notes,
        impact('retained_necessary', assessment, limitations,
               "Aucune charge nouvelle n'est identifiée : le texte source est maintenu intégralement, sans donnée, registre, justificatif, dépôt, condition ou délai supplémentaire. Ce maintien ne démontre aucune baisse nette de coût ou de complexité de l'ensemble des codes."),
        benefit=benefit)


keep(0,
     "Maintien nécessaire, sans réécriture stylistique. Le document graphique rend repérables les emplacements réservés aux ouvrages publics et leurs bénéficiaires, ainsi que les secteurs soumis à une qualité renforcée des communications électroniques. Tant que les règles de fond de L. 151-41, 1°, et L. 151-40 subsistent, supprimer leur représentation rendrait les contraintes moins accessibles aux propriétaires sans les supprimer. L'article ne crée ni taxe, ni agrément, ni déclaration du constructeur, ni série d'exemplaires à déposer.",
     "Source intégrale lue, notes vides, aucun tableau. Les quatre zones U, AU, A et N, la réserve « s'il y a lieu », les deux numéros, la destination et l'identité des bénéficiaires demeurent. L. 151-40 et L. 151-41 ont été lus en entier dans le corpus public : leurs facultés de fond sont distinctes de cette publicité graphique. Le 1° vise les ouvrages publics, sans étendre ici son champ à tous les emplacements réservés. Aucun quota SRU n'est réintroduit par le maintien de ce renvoi ciblé.",
     "Les deux informations cartographiques sont conservées pour rendre opposables et intelligibles des contraintes de fond distinctes. Aucun prélèvement, formalité privée ou contrôle supplémentaire n'est retiré ; ce maintien n'est compté ni comme réécriture ni comme simplification.",
     "Une éventuelle suppression des critères renforcés de réseaux ou d'une catégorie d'emplacements appelle une décision sur L. 151-40 ou L. 151-41, hors du lot. Le présent examen ne chiffre ni coût de cartographie ni gain national.")

keep(1,
     "Maintien nécessaire de la règle de composition des annexes. Elle permet une lecture commune des servitudes et des éléments d'information issus du code de l'urbanisme et des autres codes, sans exiger par elle-même un second dossier. Retirer cette articulation ne supprimerait aucune servitude et ferait perdre un point d'accès utile aux propriétaires. Le renvoi à R. 151-52 conserve notamment l'annexion des schémas de plage, utile à la mise en œuvre des dérogations littorales pour les opérations futures.",
     "L. 151-43 et R. 151-52 lus intégralement ; R. 151-53 appartient au présent lot. Le 5° de R. 151-52, relatif à L. 121-28, reste entier. Le 11° abrogé de cette liste n'est pas rétabli. La liste des catégories de servitudes annexée au livre n'est pas elle-même assignée ni déclarée réécrite. Notes source vides. Aucun nouveau formulaire, circuit de transmission ou support distinct n'est imposé.",
     "L'article est une articulation des annexes existantes, conservée pour l'information foncière et l'accès aux régimes favorables. Il ne prescrit pas de doublon documentaire identifiable à retirer indépendamment des listes qu'il relie.",
     "Le maintien ne vaut pas validation de chaque servitude de la liste extérieure au lot. Il ne ferme pas les schémas de plage et n'établit ni achèvement du volet SRU ni réduction de coûts.")

keep(2,
     "Maintien intégral nécessaire des quinze rubriques d'information territoriale. Ont été examinés les réseaux de chaleur, plantations, mines et carrières, bruit, plomb, forêts, eau-assainissement-déchets, risques naturels, sols, publicité, patrimoine mondial, débroussaillement, SAGE et diagnostic structurel. Ces annexes rendent visibles des règles autonomes, notamment de santé, de sécurité et de desserte, sans créer leurs autorisations ou prélèvements. Leur suppression déplacerait la recherche vers quinze régimes sans alléger les obligations de fond ; aucune production systématique d'une pièce inexistante n'est imposée puisque la liste ne joue que s'il y a lieu.",
     "Les quinze numéros et toutes leurs références, le contenu détaillé des 5° et 8°, les projets de PPR déjà rendus opposables au 9° et les documents existants ou en cours de réalisation au 8° sont conservés. Source intégrale et notes vides lues ; aucun tableau. Les sources complètes des codes de l'énergie, rural, minier, de l'environnement et du patrimoine ne sont pas fournies dans les cinq fichiers de codes : leur droit autonome n'est pas déclaré réécrit. Pour le 6°, l'articulation historique des plans de zones à risque d'exposition au plomb avec le droit sanitaire actuel reste à contrôler ; la formule « s'il y a lieu » ne crée pas un nouveau plan. L. 126-6-1 du CCH a été lu intégralement : ses secteurs de risque structurel sont précisément annexés au PLU ; son équivalence favorable entre diagnostic et projet de plan pluriannuel de travaux des copropriétés demeure. Les diagnostics ne sont pas abolis par leur simple mention en annexe.",
     "La proposition maintient les quinze catégories de renseignements, sans nouveau dépôt privé ni disparition de leur fondement. Aucun allègement de taxes ou d'autorisations n'est déduit de cette seule liste ; l'accès consolidé à l'information sur les risques et les règles reste utile.",
     "Le lot n'a pas pour effet de valider les délimitations ou obligations sectorielles individuelles. L'ancienneté éventuelle d'une rubrique ne suffit pas à abroger un document encore applicable ; aucune économie nationale ou réduction de complexité n'est chiffrée.")


xml = sources[3]['source_xml'].strip() + "\n" + (
    "<p>Les renvois du présent article ne rendent pas applicables les quotas communaux de logements sociaux, les objectifs de rattrapage et les obligations par opération supprimés par la loi portant la présente réforme. Ils ne peuvent fonder un inventaire, une transmission, un prélèvement ou un constat de carence destiné à rétablir ces obligations. La définition des logements sociaux figurant au IV de l'article L. 302-5 du code de la construction et de l'habitation reste applicable dans son champ propre. Les missions autonomes de diagnostic, d'observation, d'hébergement et d'action pour le logement demeurent.</p>\n"
    "<p>Cette exclusion s'applique à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris aux procédures en cours, sans nouveau dépôt ni reprise des délais. Les clauses qui imposent seulement les obligations ainsi supprimées cessent de produire cet effet pour l'avenir. Les contrats, conventions, aides, engagements financiers et droits des occupants et des tiers valablement acquis sont préservés. Les créances légalement nées de faits générateurs antérieurs, leurs déductions, liquidations, recouvrements, restitutions, prescriptions et recours demeurent régis par les dispositions antérieures, sous réserve de la loi répressive plus douce pour les sanctions non définitives.</p>"
)
quote = "Les renvois du présent article ne rendent pas applicables les quotas communaux de logements sociaux, les objectifs de rattrapage et les obligations par opération supprimés par la loi portant la présente réforme."
put(3, xml,
    "Coordination de fond avec l'abolition des quotas SRU : l'incorporation des règles du PLH dans le PLU ne doit pas importer les obligations supprimées par le renvoi à R. 302-1-3 ou aux objectifs du PLH. Les trois subdivisions et leur contenu autonome sont repris intégralement ; une exclusion expresse et la transition empêchent le rétablissement du quota, du rattrapage, de l'inventaire ou de la carence. Le diagnostic, les besoins de logement et d'hébergement et l'observatoire ne sont pas abolis. Cette coordination n'est pas une seconde suppression de quotas.",
    "L. 302-1 et R. 302-1-1 à R. 302-1-4 ont été lus intégralement dans le corpus public. Le projet de R. 302-1-3 y retire déjà la seule phrase de son b relative à L. 302-5 et L. 302-8, tout en conservant objectifs généraux, typologies, rénovation et moyens ; le présent article suit cette distinction. Les lettres a à c, f et h de R. 302-1-2 sont inchangées, sans importer d, e ou g. La note fiscale de L. 302-1 relative à 2027 ne fixe pas la date de la réforme. Le IV de L. 302-5 est la définition autonome conservée par coordination.json ; l'ancienne part de quota ne doit pas y être réincorporée. L'exclusion des quotas vaut aussi pour les plans existants, sans réécrire automatiquement les prescriptions des permis. La transition commune de L. 302-5 et les textes financiers hors lot doivent rester concordants. Aucune filiation exhaustive des 209 articles SRU n'est affirmée.",
    impact('coordination_only',
           "Le renvoi général au programme d'actions est borné pour ne pas rétablir les obligations SRU supprimées dans les articles porteurs. Les trois composantes autonomes du PLU-H restent entières. L'effet est une coordination d'une seule mesure, sans seconde baisse de prélèvement ni suppression de l'observatoire.",
           "L'abolition opératoire des quotas et prélèvements relève des articles L. 302-5 et suivants coordonnés hors de ce lot. Les objectifs généraux du PLH et les engagements valablement acquis subsistent ; aucun rendement financier ni achèvement documentaire SRU n'est démontré.",
           "Aucune charge nouvelle n'est identifiée : l'exclusion n'impose ni donnée, inventaire, attestation, dépôt ou contrôle de remplacement. Les missions de diagnostic et d'observation sont préexistantes. Aucun solde net de coût à l'échelle des codes n'est établi.",
           [effect('coordination', 'sru-suppression-quotas-logements-sociaux',
                   "Neutralisation des renvois susceptibles de réimporter le quota ou le rattrapage dans un PLU tenant lieu de PLH.",
                   "Le 3° incorpore le programme d'actions de L. 302-1 IV et de R. 302-1-3, dont la source comprend une obligation de rattrapage fondée sur L. 302-8.",
                   "Les missions autonomes subsistent ; les renvois ne peuvent rétablir quota, rattrapage, obligations par opération ou leurs instruments supprimés.",
                   'legal_duty', 'EPCI compétents et communes couverts par un PLU tenant lieu de programme local de l’habitat.',
                   "Entrée en vigueur de la loi, procédures en cours et effets futurs des plans anciens inclus ; contrats, aides et créances anciennes protégés.",
                   "Aucun inventaire, transmission ou prélèvement de substitution ; pas de nouveau quota local.",
                   "3° Le programme d'orientations et d'actions comprend notamment les moyens à mettre en œuvre pour satisfaire les besoins en logements et en places d'hébergement, ainsi que le programme d'actions défini au IV de l'article L. 302-1 et à l'article R. 302-1-3 du code de la construction et de l'habitation.",
                   quote)]),
    removed=["Application par les renvois du PLU-H des quotas communaux, objectifs de rattrapage et obligations par opération supprimés, ainsi que de leurs instruments exclusivement destinés à les rétablir."])


keep(4,
     "Maintien nécessaire du contenu du PLU tenant lieu de plan de mobilité. L'intégration du transport au rapport, au PADD et au programme d'actions évite des politiques contradictoires et rattache la sécurité des déplacements à un document public commun. L'article ne prescrit pas plusieurs plans ou plusieurs organes distincts. L'observation des accidents a une fonction de sécurité identifiable ; elle n'est pas assimilée à un reporting fiscal ou à un quota de logement supprimé. Aucune simple reformulation n'est produite.",
     "Les trois numéros et les renvois aux articles L. 1214-1, L. 1214-2 et R. 1214-1 à R. 1214-3 du code des transports restent entiers. R. 152-2 et R. 152-3 du présent lot précisent respectivement le suivi des accidents et le rapport de compatibilité ; le premier parle d'un dispositif d'observation, non d'une personne morale obligatoire. Le corps complet du code des transports n'est pas dans le corpus des cinq codes fourni : ni ses missions ni une réforme extérieure ne sont déclarées rédigées. Les deux notes source d'entrée en vigueur au 1er janvier 2021 ont été lues ; elles sont historiques et ne datent pas la réforme future.",
     "Le contenu intégré du plan de mobilité est conservé pour la cohérence des déplacements et la sécurité. La source ne démontre pas un doublon de structures ou un second dossier à supprimer ; aucune économie nouvelle ne lui est attribuée.",
     "La suppression éventuelle d'une mission du plan de mobilité exige l'examen complet du code des transports, hors du lot. Le présent maintien ne valide ni tous ses dispositifs ni leur coût et ne compte pas comme volet SRU achevé.")

keep(5,
     "Maintien nécessaire de l'application de l'observation habitat-foncier aux PLU tenant lieu de PLH. La mission sert le diagnostic des disponibilités, de la vacance, de l'habitat indigne et des besoins, indépendamment des quotas SRU. L. 302-1 III impose déjà cet observatoire et R. 302-1-4 définit ses missions ; supprimer le seul renvoi n'abolirait pas cette obligation législative. La source n'exige ni nouvelle personne morale ni deuxième observatoire à côté d'un dispositif satisfaisant déjà ces missions.",
     "L. 302-1 III et R. 302-1-4 lus en entier : analyses, suivis et concours des services et partenaires sont distincts de l'inventaire de L. 302-6 abrogé dans le projet. R. 151-54 maintient cette observation autonome en excluant expressément les outils des quotas. La formule source « dans les conditions définies » ne peut être interprétée comme rétablissant l'inventaire SRU supprimé. Notes vides et source sans tableau. Aucun compte rendu ou collecte privée de remplacement n'est ajouté.",
     "Le renvoi au dispositif habitat-foncier conserve une mission législative autonome utile à la construction et au repérage de l'habitat indigne. Aucune seconde structure obligatoire n'étant établie par cette source, aucun gain de fusion fictif n'est annoncé.",
     "Le délai et les missions fixés par L. 302-1 III ne sont pas supprimés dans le présent article. Les données des observatoires ne recréent ni décompte obligatoire de quota communal ni constat de carence ; aucun chiffrage des coûts n'est disponible.")

keep(6,
     "Maintien nécessaire du suivi des accidents impliquant les usagers vulnérables dans le PLU tenant lieu de plan de mobilité. Le champ est précisément limité aux accidents impliquant au moins un piéton, cycliste ou utilisateur d'engin de déplacement personnel. Ce suivi répond à une fonction essentielle de prévention des accidents ; la source n'impose ni déclaration nouvelle aux victimes ni création d'une structure juridique distincte. L'effacer seul laisserait subsister le fondement législatif de sécurité cité sans organiser sa mise en œuvre.",
     "Corps et deux notes source lus intégralement. Conserver la compétence de l'EPCI, l'expression « au moins un », les trois catégories d'usagers et les renvois à R. 1214-3 et L. 1214-2, 3°, du code des transports. Les notes fixent l'entrée en vigueur historique au 1er janvier 2021. Les données et transmissions éventuellement organisées par le code des transports restent à leur champ propre, sans prétendre avoir lu ou réécrit ce code extérieur à la collection fournie.",
     "Le dispositif existant d'observation des accidents est conservé pour les usagers vulnérables. Aucun régime parallèle ni donnée privée supplémentaire ne ressort de la source ; ce maintien n'est pas une nouvelle fusion ni une obligation supprimée.",
     "La couverture des autres accidents et le coût du suivi ne sont pas évalués. Les modalités sectorielles du code des transports restent hors du lot ; la seule suppression d'un renvoi ne prouverait pas leur abolition.")

keep(7,
     "Maintien nécessaire du seul rapport de compatibilité entre le programme d'orientations et d'actions du PLU-mobilité et les décisions de stationnement, de voirie et de circulation qui affectent les déplacements. Cette cohérence prévient la contradiction entre le plan intégré et son exécution, sans transformer la compatibilité en conformité ni ajouter un agrément ou un avis préalable. Aucune formalité répétée ni prélèvement à retirer n'est identifié dans cet article.",
     "Alinéa intégral et note historique du 1er janvier 2021 relus. Conserver les trois catégories d'actes, les compétences de domaine public routier et la limite tenant aux effets sur les déplacements pour les décisions des autorités de voirie et de circulation. Aucun effet d'opposabilité générale à tous les projets privés n'est ajouté. Les pouvoirs de police et règles de sécurité restent autonomes ; le maintien de cette compatibilité ne rétablit aucun quota SRU.",
     "Le niveau de compatibilité, plus souple qu'une conformité détaillée, reste inchangé. Il organise la cohérence des décisions publiques sans délai minimal, dépôt ni autorisation privée identifiable à supprimer.",
     "Aucune baisse des contraintes de stationnement imposées aux constructeurs ne résulte de ce maintien. Une réforme de ces contraintes exige les articles matériels concernés, sans être attribuée au simple lien de compatibilité.")


xml = (
    "<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant la présente réforme.</p>\n"
    "<p>Pour les décisions prises à compter de cette date, y compris sur les demandes en cours, les dérogations prévues au 5° de l'article L. 152-6 ne sont plus soumises aux distances minimales auparavant fixées par l'article R. 111-17. Elles demeurent ouvertes dans les conditions de l'article L. 152-6, sans nouvelle demande ni reprise des délais d'instruction.</p>\n"
    "<p>Les prescriptions des autorisations délivrées avant cette date conservent leurs effets tant qu'elles n'ont pas été modifiées selon les procédures applicables. Les refus devenus définitifs ne sont pas rouverts ; les droits et recours relatifs aux décisions antérieures sont préservés. L'abrogation ne supprime ni les servitudes civiles ni les règles distinctes de sécurité, de salubrité ou de protection du patrimoine.</p>"
)
quote = "Pour les décisions prises à compter de cette date, y compris sur les demandes en cours, les dérogations prévues au 5° de l'article L. 152-6 ne sont plus soumises aux distances minimales auparavant fixées par l'article R. 111-17."
put(8, xml,
    "Abrogation de coordination nécessaire : le projet de R. 111-17 a déjà supprimé le recul national H/2, avec plancher de trois mètres hors implantation en limite. R. 152-4 ne doit pas maintenir ce plafond par incorporation dans les dérogations au PLU. La dérogation favorable de L. 152-6, 5°, conserve son fondement légal et reste ouverte pour les décisions futures ; seuls les plafonds importés sont retirés. Ce n'est pas une seconde suppression autonome du recul national.",
    "R. 111-1, R. 111-17 et L. 152-6 lus intégralement dans le corpus public, ainsi que le projet d'abrogation de R. 111-17. Ce dernier n'était généralement pas directement applicable dans les territoires dotés d'un PLU ; R. 152-4 en importait néanmoins les limites dans la dérogation. L'objectif de mixité et l'insertion harmonieuse de L. 152-6, 5°, ne sont pas abrogés ici, et les servitudes civiles sont distinctes. R*431-31-2, lu en entier, doit cesser de demander la justification du respect du R. 152-4 abrogé dans sa plage R. 152-4 à R. 152-9 ; conserver les justifications des seules conditions subsistantes. Cet article extérieur au lot n'est pas déclaré réécrit. Les anciens permis ne sont pas automatiquement modifiés.",
    impact('coordination_only',
           "La limite nationale importée dans les dérogations de retrait est retirée pour suivre l'abrogation de R. 111-17. Le fondement favorable de L. 152-6 reste utilisable. L'article est coordonné sous la même mesure que les retraits du RNU, sans comptage d'une seconde règle nationale abolie.",
           "Les conditions légales de L. 152-6, les règles civiles et les protections autonomes subsistent. La coordination du dossier R*431-31-2 demeure à exécuter hors lot ; aucune surface supplémentaire ou réduction de coût n'est chiffrée.",
           "Aucune charge nouvelle n'est identifiée : ni distance forfaitaire, agrément, déclaration ni note de remplacement n'est ajouté. Les demandes en cours ne sont pas redéposées ; la validité des anciens titres est préservée sans nouvelle formalité. Le solde global des codes reste inconnu.",
           [effect('coordination', 'urbanisme-retraits-geometriques-rnu-suppression',
                   "Retrait du renvoi qui maintiendrait le recul national comme plafond des dérogations au PLU.",
                   "L'autorité doit limiter la dérogation de L. 152-6, 5°, aux distances de R. 111-17 : H/2, au minimum trois mètres hors implantation en limite.",
                   "Aucun plafond de distance n'est imposé par R. 152-4 ou par son ancien renvoi ; les conditions propres de L. 152-6 demeurent.",
                   'legal_duty', 'Porteurs de projets d’habitation sollicitant la dérogation de retrait de L. 152-6, 5°.',
                   "Décisions prises après entrée en vigueur, demandes en cours incluses ; anciens titres conservés jusqu'à modification régulière et refus définitifs non rouverts.",
                   "Aucune règle de recul ou déclaration substitutive ; maintien des seules protections autonomes.",
                   plain(sources[8]['source_xml']), quote)]),
    benefit="L'avantage est la possibilité de déroger aux retraits du PLU pour une construction principalement d'habitation. Il reste ouvert aux opérations futures comme aux demandes en cours sur le fondement du 5° de L. 152-6 ; seules les limites supplémentaires importées de R. 111-17 sont retirées. Les autorisations déjà accordées, leur modification et les recours restent protégés. Aucun quota supprimé n'est recréé.",
    repeal="Suppression du plafond de recul imposé aux dérogations de L. 152-6, 5°, par incorporation des distances de R. 111-17 ; le fondement légal favorable de la dérogation demeure applicable.")


xml = (
    "<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant la présente réforme.</p>\n"
    "<p>Pour les décisions prises à compter de cette date, les dérogations prévues aux 1° et 2° de l'article L. 152-5 peuvent être accordées aux constructions existantes sans durée minimale écoulée depuis leur achèvement. Cette règle s'applique aux demandes en cours, sans nouveau dépôt ni reprise des délais d'instruction. Les autres conditions de ces dérogations demeurent applicables.</p>\n"
    "<p>Les autorisations régulièrement délivrées avant cette date et les droits qui en résultent sont préservés. Les refus devenus définitifs ne sont pas rouverts ; les droits et recours relatifs aux décisions antérieures demeurent régis par les règles qui leur sont applicables.</p>"
)
quote = "Pour les décisions prises à compter de cette date, les dérogations prévues aux 1° et 2° de l'article L. 152-5 peuvent être accordées aux constructions existantes sans durée minimale écoulée depuis leur achèvement."
put(9, xml,
    "Réforme de fond : suppression de la condition d'achèvement depuis plus de deux ans pour l'isolation des façades et des toitures dérogeant au PLU. La qualité de construction existante, exigée par L. 152-5, reste requise ; une attente forfaitaire après achèvement n'apporte pas de protection propre contre un risque que les règles de sécurité, de patrimoine et les conditions techniques applicables ne traitent déjà. La suppression ne transforme pas les dérogations en dispense de permis et ne les réserve pas aux seuls travaux anciens.",
    "L. 152-5, R. 152-6 et R. 152-7 lus en entier. Les dépassements de 30 centimètres et les exclusions patrimoniales légales demeurent dans leur champ ; aucune modification de L. 152-6, 2°, qui conserve une condition distincte de deux ans pour la surélévation créant du logement, n'est faite ici. La suppression porte sur la durée, non sur l'existence de la construction ni sur l'obligation de demander une dérogation dans le dossier du titre. R*431-31-2 n'a plus à faire justifier une condition d'âge supprimée ; sa plage réglementaire est à coordonner hors du lot. Source sans notes ni tableau ; l'attribut de présentation align n'est pas repris. Aucune taxe ou aide n'est créée ni retirée.",
    impact('material_reduction',
           "La source entière ne contenait que le seuil d'ancienneté de plus de deux ans pour deux dérogations d'isolation. Cette condition est effectivement supprimée pour les décisions futures : un bâtiment déjà existant peut en bénéficier immédiatement après achèvement, sous les autres règles inchangées.",
           "L'abrogation ne vise ni les projets de bâtiments non encore existants ni la surélévation de logements de L. 152-6, 2°. Les plafonds de saillie et hauteur et les protections légales restent applicables ; les refus définitifs ne sont pas rouverts. Aucun gain financier n'est chiffré.",
           "Aucune charge nouvelle n'est identifiée : aucun agrément, certificat d'âge, délai alternatif ou déclaration compensatoire n'est créé. Les conditions préexistantes de la dérogation restent seules opposables et les demandes en cours ne sont pas redéposées. Aucun solde global des codes n'est présumé.",
           [effect('deadline_reduced', 'urbanisme-isolation-fin-attente-deux-ans',
                   "Suppression de l'ancienneté minimale après achèvement pour accéder aux dérogations d'isolation de façade et toiture.",
                   "Constructions achevées depuis plus de deux ans à la date du dépôt de la demande, pour les 1° et 2° de L. 152-5.",
                   "Toute construction existante, sans durée minimale après achèvement pour ces deux dérogations ; autres conditions inchangées.",
                   'other', 'Propriétaires et maîtres d’ouvrage isolant des constructions existantes éligibles aux 1° et 2° de L. 152-5.',
                   "Décisions prises après entrée en vigueur, y compris demandes en cours ; anciens titres et recours préservés, refus définitifs non rouverts.",
                   "Aucune condition d'âge ou pièce de substitution ; les autorisations d'urbanisme et exclusions patrimoniales subsistent.",
                   plain(sources[9]['source_xml']), quote)]),
    benefit="Les avantages possibles sont les dérogations d'emprise, d'implantation, de hauteur et d'aspect extérieur permettant l'isolation en saillie des façades ou par surélévation des toitures. Ils sont préservés pour toutes les constructions existantes éligibles futures, y compris celles achevées depuis deux ans ou moins, et pour les demandes en cours. La seule règle abrogée est une restriction d'ancienneté, non une exonération ou une dérogation favorable ; les titres antérieurs sont conservés.",
    repeal="Suppression de l'exigence d'achèvement depuis plus de deux ans pour les dérogations d'isolation des 1° et 2° de L. 152-5, sans suppression de ces dérogations ni des autres règles applicables.")


xml = sources[10]['source_xml'].replace("<p>Le présent article s'applique sans préjudice des dispositions de l'article R. 152-9.</p>", '').strip()
xml += "\n<p>La présente rédaction s'applique aux décisions prises à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris sur les demandes en cours, sans nouveau dépôt ni reprise des délais d'instruction. Les prescriptions des autorisations antérieures restent applicables tant qu'elles n'ont pas été régulièrement modifiées ; les refus définitifs ne sont pas rouverts et les droits et recours relatifs aux décisions antérieures sont préservés.</p>"
quote = "La présente rédaction s'applique aux décisions prises à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris sur les demandes en cours, sans nouveau dépôt ni reprise des délais d'instruction."
put(10, xml,
    "Coordination nécessaire avec l'abrogation de R. 152-9 : retrait du dernier alinéa qui réimporterait son contrôle architectural spécifique dans la végétalisation. Les deux premiers alinéas sont intégralement conservés : dépassement d'un mètre hors végétation et faculté de déroger aux caractéristiques des façades et toitures. L'accès reste ouvert aux nouvelles opérations. La suppression du critère matériel est évaluée à R. 152-9, non comptée une seconde fois ici.",
    "L. 152-5-1 et R. 151-41 ont été lus intégralement dans le corpus : le 2° du second fournit le champ des caractéristiques architecturales des façades et toitures auxquelles la dérogation peut s'appliquer. La hauteur supplémentaire reste mesurée en tout point et hors végétation. La dérogation ne devient pas de plein droit : la décision motivée et les zones urbaines et à urbaniser de L. 152-5-1 subsistent. R. 111-2, R. 111-27 et R. 111-1 lus en entier : sécurité et protection des lieux gardent leurs champs autonomes. R*431-31-2, lu intégralement, doit retirer le test de R. 152-9 de la note justificative sans supprimer les justifications des conditions maintenues. Aucune autre partie du corps source ni tableau omis ; note vide.",
    impact('coordination_only',
           "Seul le renvoi au contrôle architectural abrogé de R. 152-9 est retiré. Les deux possibilités favorables de végétalisation sont intégralement conservées ; le présent article ne compte pas comme une seconde suppression de contrôle.",
           "Le mètre de dépassement hors végétation, le champ légal des zones et la décision motivée subsistent. Les prescriptions anciennes ne sont pas automatiquement effacées et la coordination de R*431-31-2 reste à réaliser hors lot ; aucun chiffrage n'est établi.",
           "Aucune charge nouvelle n'est identifiée : aucun visa, nouvelle note ou évaluation de remplacement n'est introduit. Les paramètres de hauteur et d'aspect existaient déjà et les demandes en cours conservent leurs délais ; aucun solde global de coût n'est démontré.",
           [effect('coordination', 'urbanisme-isolation-vegetalisation-fin-controle-specifique',
                   "Retrait du renvoi à R. 152-9 dans le dispositif favorable de végétalisation.",
                   "La végétalisation est soumise, outre ses paramètres propres, au renvoi exprès à R. 152-9.",
                   "Les paramètres favorables restent entiers et le renvoi au contrôle abrogé disparaît, pour les nouvelles décisions.",
                   'legal_duty', 'Maîtres d’ouvrage installant des dispositifs de végétalisation éligibles à L. 152-5-1.',
                   "Décisions futures, demandes en cours incluses ; titres antérieurs conservés jusqu'à modification régulière.",
                   "Aucun contrôle de substitution ; protections autonomes et décision motivée légale maintenues.",
                   "Le présent article s'applique sans préjudice des dispositions de l'article R. 152-9.", quote)]),
    benefit="Les deux avantages sont conservés en entier : dépassement d'un mètre de la hauteur autorisée, hors végétation, et dérogation possible aux caractéristiques architecturales des façades et toitures fixées au PLU. Ils restent ouverts aux installations futures éligibles à L. 152-5-1 et aux demandes en cours. Le retrait du renvoi à R. 152-9 supprime une contrainte supplémentaire sans diminuer ces facultés ; les droits issus des titres antérieurs sont protégés.",
    removed=["Renvoi exprès au contrôle spécifique d'adaptation technique et de qualité architecturale de R. 152-9, abrogé dans la même proposition, sans retrait des deux dérogations de végétalisation."])


keep(11,
     "Maintien intégral nécessaire du régime favorable de hauteur pour les modes constructifs exemplaires sur le plan environnemental. Le supplément de 25 centimètres par niveau, limité à 2,5 mètres, neutralise une épaisseur technique accrue sans permettre un étage supplémentaire. L. 152-5-2 fixe précisément cette finalité de comparaison entre modes constructifs ; supprimer le lien technique ou l'interdiction d'étage supplémentaire changerait son objet plutôt que retirer un justificatif redondant. Aucun document autonome n'est exigé par cet article.",
     "L. 152-5-2 lu intégralement : la nature du projet, sa zone et la comparaison du nombre d'étages restent à prendre en compte. Les deux limites, leur mesure en tout point et l'interdiction d'ajout d'étage sont toutes conservées, sans convertir 25 centimètres en 25 % ni 2,5 mètres en un étage autorisé. Les exigences d'exemplarité définies dans le CCH ne sont pas supprimées par coordination implicite ; leur contrôle matériel reste dans leur champ. Notes source vides, aucun tableau. Ce maintien vaut pour les situations futures éligibles et ne crée ni taxe ni agrément nouveau.",
     "Le supplément de hauteur environnemental demeure disponible avec ses deux plafonds et sa finalité technique. La source n'établit aucun second dépôt ou délai à retirer ; aucune hausse de constructibilité ni réduction supplémentaire n'est revendiquée.",
     "Le régime est limité aux constructions répondant à l'exemplarité environnementale et au besoin technique prévu par la loi. Les modalités complètes de qualification ne sont pas réécrites ici ; aucun gain de surface ou coût de construction n'est chiffré.",
     benefit="L'avantage est le dépassement des règles de hauteur du PLU pour compenser une épaisseur par niveau plus importante d'un mode constructif exemplaire : 25 centimètres par niveau et 2,5 mètres au total. Il reste intégralement ouvert aux constructions futures éligibles, avec la comparaison technique et sans étage supplémentaire. Aucune échéance, condition fiscale, restriction de bénéficiaires ou extinction de ce bénéfice n'est ajoutée.")

keep(12,
     "Maintien intégral nécessaire des deux avantages de l'isolation extérieure et des protections solaires : saillie de 30 centimètres au-delà des règles d'implantation et emprise au sol pouvant dépasser celle du PLU. Supprimer ce corps ferait disparaître la base réglementaire de ces dérogations. Les 30 centimètres sont le paramètre de l'avantage autorisé, non une formalité doublonnée ; aucune nouvelle tolérance chiffrée n'est décidée sans besoin technique documenté. La condition d'âge supprimée à R. 152-5 ne s'applique plus par ailleurs.",
     "Conserver les 1° et 3° de L. 152-5, les façades, le règlement en vigueur, les 30 centimètres et l'emprise favorable du second alinéa. La réécriture de R. 152-8 retire seulement la limite commune redondante, sans supprimer ces limites propres. Source complète lue, notes vides ; aucun tableau. Le maintien avec proposed_xml nul reproduit la source, y compris sa présentation initiale ; aucun nouveau corps à droit constant n'est fabriqué. Les exclusions patrimoniales et la décision de L. 152-5 demeurent autonomes.",
     "Les dérogations d'implantation et d'emprise restent entières pour les travaux futurs éligibles. Aucune obligation nouvelle ou réduction additionnelle n'est attribuée à leur maintien ; les suppressions d'âge et de contrôle architectural sont évaluées dans leurs articles porteurs.",
     "La règle n'autorise pas une saillie civile chez le voisin ni sur le domaine public sans son fondement propre. Le gain de surface ou de performance énergétique n'est pas chiffré et aucune hausse de plafond n'est proposée.",
     benefit="Sont maintenus le dépassement d'implantation de 30 centimètres pour l'isolation ou la protection solaire en façade et la possibilité corrélative de dépasser l'emprise au sol du PLU. Ces avantages restent disponibles pour les futures demandes et ne sont pas limités aux bâtiments anciens de plus de deux ans, cette restriction étant supprimée à R. 152-5. Leurs autres conditions légales demeurent.")

keep(13,
     "Maintien intégral nécessaire de la tolérance de 30 centimètres de surélévation pour isoler les toitures des constructions existantes. Elle donne un contenu opératoire à l'avantage du 2° de L. 152-5, sans délai ni pièce autonome. La supprimer rendrait l'avantage moins certain alors que les règles générales de hauteur subsistent. Aucun besoin technique documenté n'appelle une nouvelle valeur arbitraire ; l'ancienneté minimale et le contrôle spécifique supplémentaires sont retirés dans les articles concernés.",
     "L. 152-5 lu en entier. Le dépassement est au-dessus de la hauteur maximale du PLU, non la hauteur totale de la toiture et non un droit à ajouter un étage. Le champ des constructions existantes demeure. Les réformes de R. 152-5, R. 152-8 et R. 152-9 restent distinctes ; les prescriptions antérieures d'un titre ne sont pas réécrites automatiquement. Source intégrale sans notes ni tableau. La conservation avec texte proposé nul n'utilise pas un nouveau corps stylistique.",
     "Le dépassement favorable de hauteur pour l'isolation des toitures est intégralement conservé, y compris pour les opérations futures. Le maintien du chiffre de 30 centimètres ne démontre aucune nouvelle baisse de contrainte.",
     "Les règles légales de patrimoine et les droits des tiers conservent leur champ. Aucune équivalence générale entre cette isolation et les surélévations de logements n'est créée ; aucun coût évité n'est chiffré.",
     benefit="L'avantage conservé est la possibilité de dépasser de 30 centimètres la hauteur maximale autorisée au PLU pour isoler la toiture d'une construction existante. Il reste applicable à toute situation future éligible et aux titres existants selon leur régime, avec suppression distincte de l'attente de deux ans. Il n'est ni fermé ni subordonné à un agrément, une taxe ou une attestation nouvelle.")


xml = (
    "<p>Les dérogations prévues aux articles R. 152-6 et R. 152-7 peuvent être mises en œuvre cumulativement, dans les limites propres à chacune d'elles. Leur cumul ne crée pas de plafond supplémentaire aux dépassements de hauteur ou d'implantation autorisés séparément par ces articles.</p>\n"
    "<p>La présente rédaction s'applique aux décisions prises à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris sur les demandes en cours, sans nouveau dépôt ni reprise des délais d'instruction. Les autorisations antérieures et leurs prescriptions demeurent applicables tant qu'elles n'ont pas été régulièrement modifiées ; les refus définitifs ne sont pas rouverts et les droits et recours relatifs aux décisions antérieures sont préservés.</p>"
)
quote = "Leur cumul ne crée pas de plafond supplémentaire aux dépassements de hauteur ou d'implantation autorisés séparément par ces articles."
put(14, xml,
    "Réduction normative par retrait d'un plafond commun redondant, et maintien explicite de la possibilité de cumuler les dérogations d'isolation. Les articles R. 152-6 et R. 152-7 fixent chacun 30 centimètres, respectivement pour l'implantation et pour la hauteur ; le présent article ne réimpose plus une seconde limite de même montant à leur cumul. Aucun dépassement de 60 centimètres, cumul de deux hauteurs ou fusion des deux axes n'est autorisé. L'effet est classé en coordination, sans prétendre une extension matérielle de constructibilité que ces deux plafonds propres empêchent de démontrer.",
    "Les trois sources R. 152-6, R. 152-7 et R. 152-8 ont été lues intégralement. Le cumul favorable ne disparaît pas ; les limites distinctes de 30 centimètres restent dans les deux articles porteurs. Le texte ne transforme pas une règle de hauteur en implantation ni inversement. R*431-31-2, lu intégralement, ne doit pas exiger une justification séparée du plafond commun supprimé ; les conditions matérielles de chaque dérogation restent justifiées. Cette coordination documentaire extérieure au lot reste à exécuter. Aucun nouveau chiffre, tableau, délai minimal ou régime de preuve n'est créé.",
    impact('coordination_only',
           "Le plafond commun de 30 centimètres est retiré comme doublon des limites propres conservées à R. 152-6 et R. 152-7. La possibilité de cumul est maintenue expressément. La proposition ne démontre pas de nouveau volume constructible ni de seconde réduction des limites propres : l'effet reste une coordination de plafonds.",
           "Les deux plafonds de 30 centimètres subsistent séparément, sur des dimensions différentes. Aucun cumul à 60 centimètres n'est institué ; aucune baisse de coût ou de surface réglementaire n'est chiffrée. La note justificative hors lot doit être coordonnée.",
           "Aucune charge nouvelle n'est identifiée : pas de test, note, déclaration ou délai substitutif au plafond commun. Les deux dérogations gardent leurs conditions préexistantes et les titres antérieurs ne sont pas automatiquement modifiés ; le bilan net global demeure inconnu.",
           [effect('coordination', 'urbanisme-isolation-cumul-plafonds-propres',
                   "Suppression de la réitération d'un plafond de cumul, sous maintien des deux limites propres et de la faculté de cumul.",
                   "R. 152-8 réimpose au cumul un maximum de 30 centimètres de hauteur ou d'implantation, en plus des 30 centimètres des articles R. 152-6 et R. 152-7.",
                   "Seules les limites propres de chaque dérogation s'appliquent ; la possibilité de les cumuler est conservée, sans nouveau dépassement chiffré.",
                   'legal_duty', 'Propriétaires combinant isolation extérieure des façades ou protection solaire et isolation des toitures.',
                   "Décisions futures et demandes en cours ; anciens titres, prescriptions et recours protégés.",
                   "Aucun plafond, formulaire ou justification de remplacement ; pas de cumul arithmétique des deux tolérances sur le même axe.",
                   plain(sources[14]['source_xml']), quote)]),
    benefit="L'avantage possible est la mise en œuvre cumulée des dérogations d'implantation ou d'emprise et de hauteur pour les mêmes travaux. Cette faculté est maintenue explicitement pour les opérations futures et demandes en cours. Seul le plafond commun qui réitère les limites propres est supprimé ; les 30 centimètres de chaque article restent applicables et les anciens titres demeurent protégés. Il n'est promis aucune nouvelle hauteur de 60 centimètres.",
    removed=["Plafond commun de cumul de 30 centimètres réitérant les limites propres de hauteur et d'implantation de R. 152-6 et R. 152-7, sans suppression de la faculté favorable de les cumuler."])


xml = (
    "<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant la présente réforme.</p>\n"
    "<p>Aucune obligation d'adaptation au mode constructif et aux caractéristiques de la façade ou de la toiture, ni aucun contrôle de la qualité architecturale et de l'insertion du bâtiment ne peut être imposé sur le seul fondement du présent article pour les décisions prises à compter de cette date. Cette règle s'applique aux demandes en cours, sans nouveau dépôt ni reprise des délais d'instruction.</p>\n"
    "<p>Les dérogations d'isolation, de protection solaire et de végétalisation demeurent ouvertes dans leur champ et leurs limites propres. Les exclusions et prescriptions prévues à l'article L. 152-5, les règles de sécurité et de salubrité, notamment l'article R. 111-2, ainsi que les protections du patrimoine et des lieux, notamment l'article R. 111-27 dans son champ, restent applicables sur leurs fondements distincts. Aucune autorisation, déclaration ou attestation de remplacement n'est instituée.</p>\n"
    "<p>Les prescriptions des autorisations antérieures restent applicables tant qu'elles n'ont pas été régulièrement modifiées. Les refus devenus définitifs ne sont pas rouverts ; les droits et recours relatifs aux décisions antérieures demeurent régis par les règles applicables à ces décisions.</p>"
)
quote = "Aucune obligation d'adaptation au mode constructif et aux caractéristiques de la façade ou de la toiture, ni aucun contrôle de la qualité architecturale et de l'insertion du bâtiment ne peut être imposé sur le seul fondement du présent article pour les décisions prises à compter de cette date."
put(15, xml,
    "Réforme de fond : retrait du test supplémentaire et général d'adaptation technique et de qualité architecturale propre aux surépaisseurs et surélévations. Le maintien de ce test indéterminé n'a pas de fonction essentielle distincte démontrée alors que L. 152-5 conserve exclusions patrimoniales et prescriptions d'intégration, R. 111-2 la sécurité et la salubrité et R. 111-27 les atteintes aux lieux et perspectives. La coupe porte sur ce fondement autonome, pas sur toutes les protections architecturales. Elle ne substitue ni déclaration ni attestation au contrôle supprimé.",
    "Source complète lue, notes vides ; les doubles espaces du texte source sont conservés dans sa citation exacte. L. 152-5, L. 152-5-1, R. 111-1, R. 111-2 et R. 111-27 lus intégralement. Le RNU n'exclut pas R. 111-2 et R. 111-27 du seul fait de l'existence d'un PLU ; leurs champs et éventuelles règles sectorielles restent distincts. Le dernier alinéa de R. 152-5-1 est retiré dans le présent lot. R*431-31-2, lu en entier, doit remplacer sa plage générale de références par les conditions encore applicables à chaque dérogation et cesser d'exiger la démonstration du test supprimé. Ne pas rétablir cette exigence par le formulaire de demande. Ce texte de dossier, hors lot, n'est pas déclaré modifié. Les règles constructives de sécurité ne sont pas abrogées et les anciens permis ne sont pas réécrits automatiquement.",
    impact('material_reduction',
           "Le contrôle propre de l'adaptation de la surépaisseur ou surélévation et de la qualité architecturale du bâtiment cesse d'être opposable sur ce fondement. C'est une suppression normative réelle, même si certains projets restent soumis à des protections générales ou patrimoniales sur d'autres fondements.",
           "La coupe n'abolit ni les prescriptions légales d'intégration de L. 152-5, ni R. 111-27, ni les règles de sécurité ou du patrimoine. L'étendue pratique du gain dépend de ces autres règles ; les coûts, surfaces gagnées et le solde national ne sont pas chiffrés. R*431-31-2 reste à coordonner hors lot.",
           "Aucune charge nouvelle n'est identifiée : aucun avis, certificat d'intégration, enregistrement ou déclaration ne remplace le test retiré. Le rappel des règles autonomes ne leur donne pas un champ nouveau ; les demandes en cours gardent leurs délais. Aucun solde global des codes n'est démontré.",
           [effect('obligation_removed', 'urbanisme-isolation-vegetalisation-fin-controle-specifique',
                   "Suppression du test réglementaire spécifique d'adaptation technique et de qualité architecturale de R. 152-9.",
                   "La surépaisseur ou surélévation doit satisfaire au test propre de R. 152-9, en plus des autres conditions légales et réglementaires.",
                   "Ce test ne peut plus être imposé sur ce fondement pour les décisions futures ; les autres protections restent à leur champ propre.",
                   'legal_duty', 'Maîtres d’ouvrage dont les surépaisseurs ou surélévations et dispositifs de végétalisation relevaient de R. 152-9.',
                   "Décisions futures, demandes en cours incluses sans redépôt ; anciennes prescriptions maintenues jusqu'à modification régulière, refus définitifs non rouverts.",
                   "Aucune procédure ou attestation substitutive ; exigences légales de sécurité et patrimoine conservées sans extension.",
                   plain(sources[15]['source_xml']), quote)]),
    repeal="Suppression du contrôle spécifique d'adaptation au mode constructif et aux caractéristiques de la façade ou toiture, de qualité architecturale du bâtiment et d'insertion, sans abroger les protections autonomes.")


keep(16,
     "Maintien nécessaire de l'identification de l'autorité conduisant l'élaboration du PLU : président de l'EPCI compétent ou maire selon la compétence détenue. Cette attribution évite une responsabilité diffuse sans imposer une formalité, un agrément, une taxe ou un délai supplémentaire au porteur de projet. La supprimer n'allégerait aucune procédure et laisserait moins claire l'autorité responsable ; aucune reformulation de remplissage n'est produite.",
     "Source intégrale d'un alinéa, sans note ni tableau. La compétence de l'EPCI reste une condition, non une compétence générale attribuée à tous les EPCI. Le maire n'est pas ajouté comme codécideur lorsque le président compétent conduit la procédure. Les délibérations, consultations et participations publiques gardent leurs fondements propres ; cet article ne permet pas de les effacer implicitement.",
     "L'attribution de la conduite de la procédure est conservée, sans acte privé ou étape additionnelle. Aucun changement matériel par rapport à la source n'est revendiqué ni compté en simplification.",
     "Les transferts de compétence et les règles de délibération ne sont pas réécrits par ce maintien. Aucune économie de personnel ou de délai n'est démontrée.")


xml = (
    "<p>L'avis prévu à l'article L. 153-13 est rendu dans un délai d'un mois à compter de la saisine. A défaut de réponse dans ce délai, l'avis est réputé favorable.</p>\n"
    "<p>Ce délai s'applique aux saisines intervenant à compter de l'entrée en vigueur de la loi portant la présente réforme. Les saisines antérieures conservent le délai et les effets du silence prévus par les dispositions antérieurement applicables ; aucun avis acquis ni délai expiré n'est remis en cause.</p>"
)
quote = "L'avis prévu à l'article L. 153-13 est rendu dans un délai d'un mois à compter de la saisine."
put(17, xml,
    "Réforme de fond : le plafond de réponse de l'autorité organisatrice consultée sur les orientations du PADD passe de deux mois à un mois, avec avis favorable tacite maintenu. Il s'agit d'une consultation ciblée en amont, non de l'examen complet du projet arrêté ; un mois permet l'avis tout en réduisant l'attente maximale créée par le silence. La consultation légale, les compétences et les exclusions territoriales ne sont pas supprimées ou remplacées par une déclaration.",
    "L. 153-13 lu intégralement : communes ni membres d'un EPCI compétent en PLU ni d'une autorité organisatrice, à moins de quinze kilomètres de la périphérie d'une agglomération de plus de 50 000 habitants ; Île-de-France exclue. Ce champ n'est pas élargi. Le délai reste calculé en mois, sans conversion approximative en jours. Il ne s'agit pas d'un mois d'attente obligatoire si l'avis est rendu avant. Les saisines anciennes restent à deux mois : aucune consultation en cours n'est raccourcie rétroactivement. Note source vide, aucun tableau. La modification réglementaire et son entrée en vigueur doivent être coordonnées dans le texte de réforme, sans nouvelle date calendaire inventée.",
    impact('material_reduction',
           "Le plafond de consultation passe de deux mois à un mois et le silence favorable est conservé. Le gain démontré est un mois de moins avant acquisition tacite pour les nouvelles saisines sans réponse, non une suppression de la consultation ni un délai total de PLU garanti.",
           "Le délai reste en mois et le gain peut être nul si l'autorité répond déjà rapidement ou si une autre étape détermine le calendrier. Le champ étroit de L. 153-13 et les saisines anciennes sont inchangés ; aucun coût ou nombre de jours n'est extrapolé.",
           "Aucune charge nouvelle n'est identifiée : même autorité, même objet et même saisine, sans document, donnée, registre ou déclaration supplémentaire. Le délai de réponse est raccourci mais aucune nouvelle échéance de dépôt n'est imposée à un demandeur ; le solde net global reste inconnu.",
           [effect('deadline_reduced', 'urbanisme-plu-delais-avis-reduction',
                   "Réduction à un mois du plafond de l'avis de l'autorité organisatrice sur les orientations du PADD.",
                   "Deux mois à compter de la saisine, puis avis réputé favorable, dans le champ de L. 153-13.",
                   "Un mois à compter de la même saisine, puis même avis réputé favorable ; aucune durée minimale de consultation nouvelle.",
                   'other', 'Communes et autorités organisatrices entrant dans les conditions de L. 153-13, hors Île-de-France.',
                   "Saisines nouvelles après entrée en vigueur ; anciennes saisines, avis et échéances conservés.",
                   "Aucun dépôt de remplacement ; la consultation existante subsiste avec un délai maximal réduit.",
                   "L'avis prévu à l'article L. 153-13 est rendu dans un délai de deux mois à compter de la saisine.", quote)]),
    removed=["Mois supplémentaire du délai maximal de réponse à la consultation ciblée de l'autorité organisatrice sur les orientations du PADD, sans suppression de son droit de rendre un avis."])


xml = (
    "<p>Le bilan de la concertation établi en application de l'article L. 103-6 peut être présenté à l'organe délibérant lors de la délibération qui arrête le projet de plan local d'urbanisme, sans décision ni délibération d'adoption de ce bilan.</p>\n"
    "<p>La présente rédaction s'applique aux bilans établis à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris dans les procédures en cours. Les bilans régulièrement établis auparavant restent utilisables sans nouvelle adoption ni établissement d'un second bilan ; aucune procédure achevée n'est rouverte.</p>"
)
quote = "Le bilan de la concertation établi en application de l'article L. 103-6 peut être présenté à l'organe délibérant lors de la délibération qui arrête le projet de plan local d'urbanisme, sans décision ni délibération d'adoption de ce bilan."
put(18, xml,
    "Coordination nécessaire avec le projet de L. 103-6, qui retire l'acte d'adoption du bilan tout en conservant son établissement. La possibilité actuelle de le traiter simultanément à l'arrêt du projet est conservée comme présentation facultative, sans réintroduire une adoption obligatoire. L'arrêt du projet de PLU, le bilan lui-même, son insertion dans l'enquête et les présentations requises sur d'autres fondements demeurent ; aucune nouvelle fusion n'est comptée ici, la simultanéité étant déjà possible dans la source.",
    "Source en vigueur depuis le 29 juillet 2026 lue intégralement ; note vide. L. 103-6 source et proposition lues en entier dans le corpus, et mesure existante urbanisme-concertation-bilan-sans-adoption reprise pour déduplication. La transition suit celle du projet législatif : elle ne rouvre ni concertation ni procédure achevée. R. 153-8 et L. 153-19 lus intégralement : les pièces du dossier et les garanties de participation restent autonomes. La dispense d'adoption n'efface pas les délibérations relatives au fond du PLU ni une présentation imposée par un autre texte. La filiation historique SRU de la concertation reste non close dans les notes de L. 103-6 ; aucun achèvement des 209 articles n'est déclaré.",
    impact('coordination_only',
           "Le vocabulaire de R. 153-3 suit la suppression de l'adoption formelle décidée à L. 103-6. La source permettait déjà la simultanéité avec l'arrêt du PLU : aucune réunion évitée ni nouvelle fusion n'est attribuée au présent article.",
           "Le bilan, sa communication utile et l'arrêt du projet subsistent. L'effet matériel d'abolition de l'adoption est porté par L. 103-6, hors lot ; aucune économie nationale ni clôture de filiation SRU n'est démontrée.",
           "Aucune charge nouvelle n'est identifiée : la présentation reste facultative sur ce seul fondement et aucun support, vote, visa ou rapport supplémentaire n'est ajouté. Les bilans anciens sont réutilisables ; le solde global de coût et complexité n'est pas établi.",
           [effect('coordination', 'urbanisme-concertation-bilan-sans-adoption',
                   "Coordination du bilan de concertation du PLU avec la suppression de son acte d'adoption obligatoire.",
                   "La délibération arrêtant le projet peut simultanément tirer le bilan de la concertation selon L. 103-6.",
                   "Le bilan établi peut être présenté lors de l'arrêt du PLU sans acte d'adoption du bilan ; l'arrêt du PLU reste requis.",
                   'legal_duty', 'Organes délibérants communaux et intercommunaux arrêtant un projet de PLU.',
                   "Bilans établis après entrée en vigueur, procédures en cours incluses ; anciens bilans utilisables sans nouvelle adoption.",
                   "Aucun vote ni rapport substitutif ; présentation seulement facultative sur ce fondement.",
                   plain(sources[18]['source_xml']), quote)]),
    removed=["Portée du renvoi au bilan de L. 103-6 en tant qu'acte d'adoption formelle, déjà supprimé dans l'article législatif porteur de la mesure ; la présentation facultative et l'arrêt du PLU subsistent."])


xml = (
    "<p>L'avis sur le projet de plan arrêté, prévu à l'article L. 153-15, est rendu dans un délai de deux mois à compter de l'arrêt du projet. En l'absence de réponse à l'issue de ce délai, l'avis est réputé favorable.</p>\n"
    "<p>Ce délai s'applique aux projets arrêtés à compter de l'entrée en vigueur de la loi portant la présente réforme. Les projets arrêtés antérieurement restent soumis au délai et aux effets du silence antérieurement applicables. Les règles de nouvelle délibération, de consultation sur le projet modifié et de majorité prévues à l'article L. 153-15 demeurent applicables, sans remise en cause d'un avis acquis ni réouverture d'un délai expiré.</p>"
)
quote = "L'avis sur le projet de plan arrêté, prévu à l'article L. 153-15, est rendu dans un délai de deux mois à compter de l'arrêt du projet."
put(19, xml,
    "Réforme de fond : réduction de trois à deux mois du plafond d'avis de la commune membre sur le projet arrêté. Le délai est aligné sur les deux mois déjà accordés par L. 153-15 pour l'avis sur la modification répondant à un désaccord, sans supprimer le droit de la commune d'émettre ce désaccord, la nouvelle délibération ni les majorités protectrices. Le silence favorable subsiste. Il ne s'agit pas d'une suppression des procédures collectives de PLU ni d'un raccourcissement des autres consultations.",
    "L. 153-15 source et proposition lues intégralement. Conserver le départ à l'arrêt du projet, et non le remplacer par la transmission ; trois mois demeurent pour les projets arrêtés avant la réforme. Les deux tiers des suffrages exprimés restent exigés dans les autres cas définis par L. 153-15 ; la majorité des suffrages exprimés ne s'applique qu'au cas qu'il prévoit. R. 153-4, lu intégralement, conserve son délai distinct de trois mois pour les personnes publiques de L. 153-16 et L. 153-17 : aucune réduction implicite de cette consultation. Le délai légal de deux mois sur le projet modifié n'est pas un deuxième gain. Notes source vides ; aucun tableau ou conversion en jours.",
    impact('material_reduction',
           "La commune membre dispose désormais de deux mois, au lieu de trois, avant que son silence sur le projet arrêté vaille avis favorable. La réduction d'un mois de l'attente maximale est réelle pour ce cas, sans disparition de l'examen communal ni affaiblissement textuel des majorités de L. 153-15.",
           "Les avis expressément défavorables gardent leurs conséquences légales et les anciennes procédures conservent trois mois. Le délai déjà fixé à deux mois pour le projet modifié n'est pas réduit ; les autres consultations et le calendrier total du PLU ne sont pas garantis plus courts.",
           "Aucune charge nouvelle n'est identifiée : aucun dossier, attestation ou accord substitutif n'est ajouté et les mêmes règles de décision subsistent. Les communes doivent organiser leur avis dans le plafond réduit ; ce changement de calendrier n'est pas présenté comme une économie nette chiffrée des services ou des codes.",
           [effect('deadline_reduced', 'urbanisme-plu-delais-avis-reduction',
                   "Réduction du plafond de l'avis communal initial sur le PLU arrêté, sans modifier les majorités de désaccord.",
                   "Trois mois à compter de l'arrêt du projet, puis avis favorable en l'absence de réponse.",
                   "Deux mois à compter du même arrêt, puis avis favorable ; désaccord exprès et mécanismes de L. 153-15 conservés.",
                   'other', 'Communes membres et EPCI compétents dans la procédure de L. 153-15.',
                   "Projets arrêtés après entrée en vigueur ; projets antérieurs à trois mois, avis acquis et délais expirés protégés.",
                   "Aucun dépôt ou accord nouveau ; maintien du droit de désaccord et des délibérations légales.",
                   "L'avis sur le projet de plan arrêté, prévu à l'article L. 153-15, est rendu dans un délai de trois mois à compter de l'arrêt du projet.", quote)]),
    removed=["Troisième mois du plafond d'avis communal initial sur le projet de PLU arrêté, sans suppression de l'avis, du droit de désaccord ni des majorités de L. 153-15."])


keep(20,
     "Maintien nécessaire des avis sectoriels lors d'une réduction d'espaces agricoles ou forestiers. La chambre d'agriculture, l'INAO en zone d'appellation d'origine contrôlée et, le cas échéant, le CNPF apportent des expertises distinctes sur des ressources et activités difficilement reconstituables ; la seule qualité d'avis administratifs ne démontre pas leur inutilité. L'avis reste simple et le silence favorable au bout de trois mois évite un veto par inertie. Aucun dossier, agrément ou taxe supplémentaire n'est ajouté.",
     "Source et notes vides lues en entier. Conserver le caractère préalable à l'approbation, les trois organismes, la condition propre aux zones AOC, la réserve « le cas échéant », la réduction d'espaces agricoles ou forestiers, le départ à la saisine et les trois mois. L. 112-3 du code rural, expressément porteur de l'obligation, n'est pas présent dans la collection des cinq codes fournie : une abrogation de la seule répétition réglementaire ne peut être annoncée comme suppression légale de ces avis. R. 153-4 et L. 153-16 ont été lus : leurs consultations et compétences propres ne prouvent pas que les trois avis soient déjà intégralement obtenus dans tous les cas. Aucun délai minimum d'attente après un avis exprès n'est créé.",
     "Les avis ciblés sur la consommation des espaces agricoles ou forestiers sont conservés avec leur silence favorable. La source ne prouve pas une identité d'objet et de compétence qui permettrait d'abolir un avis comme doublon ; aucune réduction fictive n'est comptée.",
     "Le fondement rural et les règles sectorielles externes n'ont pas été réécrits dans ce lot. Une fusion ultérieure exige la comparaison de leurs textes complets ; ni coût net, ni économie de terres ou d'argent n'est chiffré.")


xml = sources[21]['source_xml'].replace(
    "Toutefois, le silence de l'établissement public de coopération intercommunale à l'origine de la zone d'aménagement concerté vaut rejet du projet.",
    "Toutefois, le silence de l'établissement public de coopération intercommunale à l'origine de la zone d'aménagement concerté vaut avis favorable au projet."
).strip()
xml += "\n<p>La présente rédaction s'applique aux saisines intervenant à compter de l'entrée en vigueur de la loi portant la présente réforme. Les saisines antérieures conservent leurs délais et les effets du silence antérieurement applicables. Les avis exprès, les décisions devenues définitives et les droits et recours relatifs aux procédures antérieures ne sont pas remis en cause.</p>"
quote = "Toutefois, le silence de l'établissement public de coopération intercommunale à l'origine de la zone d'aménagement concerté vaut avis favorable au projet."
put(21, xml,
    "Réforme de fond : le silence de l'EPCI initiateur de la ZAC pendant trois mois vaut avis favorable au lieu de rejet du projet. La consultation et la nécessité légale d'un avis favorable dans ce cas sont conservées, mais l'inertie ne bloque plus indéfiniment l'élaboration, la révision ou la modification du PLU. Le reste de l'alinéa est maintenu intégralement, notamment la saisine, le délai de trois mois et le régime des autres personnes publiques. Aucun accord tacite n'efface un avis exprès défavorable.",
    "L. 153-18 et L. 153-39, sources et propositions, lus intégralement : ils exigent un avis favorable de l'EPCI initiateur mais n'y ajoutent pas le mot « exprès ». Le nouveau règlement précise le sens favorable du silence sans transformer l'avis des autres personnes publiques ni supprimer cette exigence légale. Les renvois restent nécessaires et cohérents. R. 153-8 lu en entier : les avis recueillis restent au dossier de participation dans leur champ. Le texte n'impose pas d'obtenir un certificat nouveau pour l'avis tacite et ne remplace pas le délai par un préavis de travail. Saisines antérieures inchangées, aucun rejet définitif rouvert. L'articulation avec les règles générales de silence du CRPA et l'habilitation réglementaire devra être contrôlée lors de l'adoption du décret, sans prétendre ce code extérieur réécrit.",
    impact('material_reduction',
           "La seule exception de silence défavorable de R. 153-7 devient un avis favorable tacite après trois mois. Le blocage par absence d'accord exprès disparaît pour les nouvelles saisines de l'EPCI initiateur, sans supprimer la consultation ni la faculté d'un désaccord motivant le refus d'approuver dans le cadre légal.",
           "Le délai de trois mois n'est pas réduit. Un avis exprès défavorable reste efficace et les conditions des articles L. 153-18 et L. 153-39 subsistent. Les anciennes saisines et décisions ne sont pas rouvertes ; aucun nombre de projets ou gain financier n'est établi.",
           "Aucune charge nouvelle n'est identifiée : aucun agrément, confirmation de saisine, attestation de silence ou nouvelle donnée n'est ajouté. L'avis favorable peut naître du silence sans acte substitutif ; les recours et compétences restent à leur champ propre. Aucun solde net global n'est chiffré.",
           [effect('relief_extended', 'urbanisme-zac-silence-avis-favorable',
                   "Remplacement du rejet tacite propre à l'EPCI initiateur d'une ZAC par un avis favorable tacite.",
                   "Après trois mois de silence suivant la saisine, l'EPCI à l'origine de la ZAC est réputé rejeter le projet de PLU concerné.",
                   "Après les mêmes trois mois, son avis est réputé favorable ; les désaccords exprès et la consultation restent régis par les articles légaux cités.",
                   'legal_duty', 'Collectivités élaborant, révisant ou modifiant un PLU concernant une ZAC créée à l’initiative d’un EPCI.',
                   "Saisines nouvelles après entrée en vigueur ; anciennes saisines, avis exprès et décisions définitives conservés.",
                   "Aucun certificat ou nouvelle procédure ; l'exigence légale d'avis favorable est satisfaite tacitement à défaut de réponse.",
                   "Toutefois, le silence de l'établissement public de coopération intercommunale à l'origine de la zone d'aménagement concerté vaut rejet du projet.", quote)]),
    removed=["Effet de rejet du projet attaché au seul silence de trois mois de l'EPCI initiateur de la ZAC, remplacé par un avis favorable tacite sans nouvelle formalité."])


keep(22,
     "Maintien intégral nécessaire d'une fusion favorable de procédures : l'enquête du PLU peut déjà valoir enquête préalable à la DUP des opérations, acquisitions ou expropriations prévues dans la ZAC. Cette économie existante reste ouverte aux opérations futures, avec les pièces indispensables à l'information des personnes susceptibles d'être expropriées. Supprimer ces pièces ou les garanties environnementales ne serait pas retirer un simple double dépôt ; aucun second dossier matériel n'est exigé par le présent article.",
     "L. 153-19, sa note de transition du 26 mai 2026, L. 153-20 et R. 153-8 lus intégralement. Le choix de participation électronique introduit dans L. 153-19 ne remplace pas automatiquement une enquête préalable à la DUP : le présent article reste limité à l'enquête publique. Conserver les opérations, acquisitions et expropriations, le périmètre intérieur à la ZAC, l'alternative R. 112-4 ou R. 112-5 du code de l'expropriation et les formes du chapitre III du titre II du livre Ier du code de l'environnement. Ces deux codes extérieurs ne sont pas présentés comme réécrits. Notes source vides, aucun tableau. Aucun élargissement d'expropriation ni nouvelle preuve privée n'est ajouté.",
     "La fusion de l'enquête PLU et de l'enquête préalable à la DUP existe déjà dans la source. Elle est conservée avec l'information utile aux propriétaires, sans lui attribuer une seconde enquête supprimée ou un allègement nouveau.",
     "Le régime ne vaut ni pour une simple participation électronique ni pour toute opération hors ZAC. Les exigences d'expropriation gardent leur champ et leur corpus complet n'est pas réécrit ; aucune économie nationale n'est calculée.")

keep(23,
     "Maintien intégral nécessaire de la dispense d'enquête préalable aux classements et déclassements de voies et places prévus au PLU. L'enquête du plan doit déjà couvrir ces opérations et en préciser la catégorie ; la dispense évite une seconde consultation sans priver le public d'information. Pour les voiries nationale et départementale, l'avis conforme et son rattachement à l'acte protègent la compétence du gestionnaire de la voie. Aucun allègement supplémentaire ne peut être déduit du seul réemploi de cet avis déjà requis et aucune nouvelle formalité n'est produite.",
     "Source intégrale lue, notes vides. Les voies et places communales, les deux conditions du premier alinéa et l'extension aux voiries nationale et départementale avec avis conforme du préfet ou du président du conseil départemental demeurent. L. 153-19 lu en entier : la faculté de participation électronique ne doit pas être assimilée silencieusement à l'enquête publique ici requise pour la dispense. Le renvoi à L. 123-2 du code de l'environnement n'est ni remplacé ni étendu ; le texte complet de ce code extérieur n'est pas déclaré réécrit. L'avis conforme ne devient pas un avis simple et les opérations futures éligibles conservent la dispense.",
     "Les deux dispenses existantes, communale et conditionnellement nationale ou départementale, sont maintenues pour les futurs classements et déclassements prévus par le plan. Il ne s'agit pas d'une nouvelle enquête supprimée, et aucune réduction de taxe ou de délai n'est revendiquée.",
     "Les opérations doivent rester couvertes par une enquête publique répondant au texte et les voiries externes exigent l'accord conforme du gestionnaire compétent. Aucun élargissement à la seule participation électronique ni chiffrage de coût n'est démontré.",
     benefit="L'avantage est la dispense d'une enquête distincte pour les classements et déclassements de voies et places publiques prévus au PLU, puis son extension conditionnelle aux voiries nationale et départementale. Les deux branches restent intégralement applicables aux opérations futures éligibles, sans date de fermeture ni restriction nouvelle. Les conditions d'information du public et d'avis conforme du gestionnaire demeurent, de même que les droits déjà acquis.")


output = [answers[i] for i in range(len(sources))]
Path('answer.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')

# Vérifications de structure et de fidélité textuelle, sans validation juridique.
assert len(output) == 24
for s, a in zip(sources, output):
    for k in ('code_id', 'source_id', 'source_sha256', 'number'):
        assert s[k] == a[k], (s['number'], k)
    si = a['substantive_impact']
    assert si['version'] == 1
    for k in ('assessment', 'scope_limitations', 'new_burdens_review'):
        assert len(si[k]) >= 40, (s['number'], k)
    if s.get('benefit_check_required'):
        assert len(a.get('benefit_review', '')) >= 100, s['number']
    if a['status'] == 'retained_unchanged':
        assert a['proposed_xml'] is None
        assert a['classification'] == si['classification'] == 'retained_necessary'
        assert si['effects'] == []
    else:
        assert a['proposed_xml']
    if a.get('change_type') == 'full_repeal':
        assert len(a['repeal_scope']) >= 30
        assert plain(a['proposed_xml']).startswith('Le présent article est abrogé')
    if a.get('change_type') == 'normative_reduction':
        assert all(len(x) >= 30 for x in a['removed_provisions'])
    for e in si['effects']:
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', e['measure_id'])
        assert 6 <= len(e['measure_id']) <= 96
        for q, text in [('source_quote', plain(s['source_xml'])), ('proposed_quote', plain(a['proposed_xml']))]:
            assert len(e[q]) >= 12 and e[q] in text, (s['number'], q)

print(json.dumps({'articles': len(output), 'drafts': sum(a['status'] == 'rewrite_draft' for a in output),
                  'retained': sum(a['status'] == 'retained_unchanged' for a in output),
                  'full_repeals': sum(a.get('change_type') == 'full_repeal' for a in output)}, ensure_ascii=False))
