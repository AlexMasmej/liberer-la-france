import json
import re
from html import unescape, escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCES = json.loads((ROOT / 'source.json').read_text())
S = {a['number']: a for a in SOURCES}
RESULT = {}


def p(text):
    return '<p>' + escape(text, quote=False) + '</p>'


def plain(xml):
    return unescape(re.sub(r'<[^>]+>', '', xml or ''))


def effect(kind, measure_id, description, before, after, unit,
           affected_population, conditions_and_transition,
           replacement_or_new_burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit,
                affected_population=affected_population,
                conditions_and_transition=conditions_and_transition,
                replacement_or_new_burdens=replacement_or_new_burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


def put(number, proposed, reason, notes, impact_class, assessment, limitations,
        burdens, effects=None, removed=None, benefit=None, repeal=None):
    a = S[number]
    obj = {key: a[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    obj.update(proposed_xml=proposed, reason=reason, review_notes=notes,
               status='retained_unchanged' if proposed is None else 'rewrite_draft')
    if proposed is None:
        obj['classification'] = 'retained_necessary'
    if removed:
        obj.update(change_type='normative_reduction',
                   reform_policy_id='editorial_direction_2026_10_19',
                   removed_provisions=removed)
    if repeal:
        obj.update(change_type='full_repeal',
                   repeal_policy_id='editorial_direction_2026_10_19',
                   repeal_scope=repeal)
    if benefit:
        obj['benefit_review'] = benefit
    obj['substantive_impact'] = dict(
        version=1, classification=impact_class, assessment=assessment,
        scope_limitations=limitations, new_burdens_review=burdens,
        effects=effects or [])
    RESULT[number] = obj


# Les corps maintenus dans les articles modifiés sont repris intégralement de
# la source. Chaque remplacement ci-dessous est limité à une réforme identifiée.
n = 'R111-25-14'
x = S[n]['source_xml'].replace(
    "l'absence de réponse ou le caractère infructueux de la procédure, attestée par lui, permet",
    "l'absence de réponse ou le caractère infructueux de la procédure permet")
assert x != S[n]['source_xml']
x += p("Pour l'application du III, l'absence de réponse ou le caractère infructueux de la procédure peut être établi par tout moyen, sans attestation distincte du propriétaire ou du gestionnaire. Cette règle s'applique aux justifications examinées à compter de l'entrée en vigueur de la réforme, y compris dans les demandes en cours, sans nouveau dépôt ni reprise des délais d'instruction. Les éléments déjà produits restent utilisables.")
put(n, x,
    "Coordination de fond de la liberté de preuve retenue à R. 111-25-19 : retrait de l'attestation particulière du propriétaire ou du gestionnaire au III. Les critères de coût excessif, les deux dénominateurs alternatifs du rapport, l'actualisation sur vingt ans, le reste à charge du tiers-investisseur et les trois procédures donnant accès à la présomption restent intégralement conservés. Il ne s'agit ni d'une suppression de l'exemption ni d'une seconde mesure générale de simplification.",
    "Renvois lus : L. 111-19-1, R. 111-25-7, R. 111-25-9 à R. 111-25-15, R. 111-25-18 et R. 111-25-19. Le taux d'actualisation et le seuil du rapport restent ceux des arrêtés auxquels renvoient les textes ; aucune valeur n'est inventée. Les références CG3P L. 2122-1-1 et L. 2122-1-3-1 ne sont pas modifiées ; leur régime n'est pas réécrit ici. La note d'application du décret du 13 novembre 2024 reste l'historique de la source, pas la date de la réforme. Dédupliquer avec la mesure principale de R. 111-25-19.",
    'coordination_only',
    "La présomption de coût excessif subsiste dans son entier ; son accès n'exige plus une attestation autonome. Cette coordination du régime de preuve des exemptions ne constitue pas une nouvelle taxe supprimée ni une seconde suppression générale d'étude.",
    "Les obligations législatives d'ombrage et leurs autres exemptions subsistent. Aucun coût national, seuil d'arrêté ou montant d'économie n'est établi ; les règles de passation des trois procédures citées restent autonomes.",
    "Aucune charge nouvelle identifiée : les résultats d'une procédure déjà conduite peuvent être invoqués sans nouvelle attestation, nouveau registre ou dépôt de remplacement ; l'appréciation des faits reste nécessaire.",
    [effect('coordination', 'parkings-preuve-libre-exemptions',
            "Retrait coordonné de l'attestation spéciale de procédure infructueuse, au sein de la même mesure de preuve libre que R. 111-25-19.",
            "Présomption accessible après absence de réponse ou procédure infructueuse attestée par le propriétaire ou le gestionnaire ; mêmes procédures et même lot concerné.",
            "Même présomption et mêmes procédures ; preuve par tout moyen sans attestation distincte, sans modification des rapports de coûts ni de l'actualisation sur vingt ans.",
            'legal_duty', "Propriétaires et gestionnaires des parcs relevant du III.",
            "Justifications examinées après l'entrée en vigueur, y compris dossiers en cours, sans nouveau dépôt ni remise à zéro des délais.",
            "Aucune déclaration ni étude de remplacement ; les faits doivent toujours être établis.",
            "l'absence de réponse ou le caractère infructueux de la procédure, attestée par lui, permet de présumer le caractère excessif du coût des travaux.",
            "l'absence de réponse ou le caractère infructueux de la procédure peut être établi par tout moyen, sans attestation distincte du propriétaire ou du gestionnaire.")],
    ["Attestation autonome du propriétaire ou du gestionnaire pour établir l'absence de réponse ou le caractère infructueux de la procédure mentionnée au III."],
    "L'exemption d'ombrières renouvelables pour coût excessif, les deux bases de comparaison, la déduction des revenus actualisés sur vingt ans et le traitement du tiers-investisseur restent applicables. La présomption du III demeure ouverte pour les trois procédures, obligatoires ou volontaires, et pour leur lot spécifique ; seule sa preuve est allégée. Aucune fermeture aux futurs parcs éligibles.")

put('R111-25-15', None,
    "Maintien nécessaire après examen : les II et III permettent de compter tous les coûts réels, y compris adaptation du parc, contraintes réglementaires et remplacement provisionné des onduleurs, dans les exemptions de R. 111-25-13 et R. 111-25-14. Retirer ces postes rendrait les exemptions moins favorables. Le I règle le seuil de comparaison sans imposer ici une nouvelle demande ou déclaration ; aucun changement stylistique n'est proposé.",
    "R. 111-25-13 et R. 111-25-14 lus intégralement : les rapports restent utiles et ne deviennent pas orphelins. La provision pour onduleurs est facultative, non un provisionnement obligatoire ajouté. La note source fixe le champ historique au 1er janvier 2024 ; aucune nouvelle date ni valeur de rapport n'est déduite de cette note. Les arrêtés chiffrant les rapports ne sont pas fournis dans ce lot.",
    'retained_necessary',
    "Aucun changement par rapport à la source entière : conservation de l'assiette complète des coûts servant aux exemptions économiques, sans créer ni supprimer de prélèvement. Cet article n'est compté ni comme réécrit ni comme simplifié.",
    "Le maintien ne valide pas les valeurs des rapports fixées par arrêtés non joints et ne mesure pas le coût des équipements ; il concerne seulement la méthode et les postes de coût de cet article.",
    "Aucune charge nouvelle identifiée : le texte est intégralement maintenu et la provision facultative n'est pas convertie en obligation de comptabilité ou de justificatif supplémentaire.",
    benefit="Le périmètre large des coûts et la faculté d'intégrer le remplacement des onduleurs favorisent l'accès aux exemptions pour coût excessif. Ils restent intégralement applicables aux parcs futurs éligibles ; aucun poste de coût, dénominateur ou exonération n'est supprimé.")

n = 'R111-25-16'
x = S[n]['source_xml'].replace(' a été délivrée avant le 1er juillet 2023.', ' a été délivrée.')
assert x != S[n]['source_xml']
x += p("Le présent article s'applique, à compter de l'entrée en vigueur de la réforme, aux obligations restant à exécuter, quelle que soit la date de délivrance de la première autorisation d'urbanisme relative à la suppression ou à la transformation du parc. Il s'applique aux demandes en cours sans nouveau dépôt ni reprise des délais d'instruction. Les exemptions antérieurement acquises sont conservées. Il n'emporte ni remboursement des travaux déjà exécutés ni remise en cause automatique des décisions antérieures ; les voies de recours demeurent ouvertes dans leurs conditions propres.")
put(n, x,
    "Réduction de fond : suppression de la date butoir du 1er juillet 2023 pour bénéficier de l'exonération liée à une suppression ou transformation du parc déjà autorisée. L'investissement destiné à un équipement appelé à disparaître n'est plus imposé du seul fait de la date du premier titre. Le motif matériel, la nécessité d'une autorisation délivrée, la caducité faute d'engagement des travaux pendant sa validité, les deux ans de mise en conformité et l'obligation sur la partie restante sont maintenus en entier.",
    "L. 111-19-1, R. 111-25-1 et R. 111-25-17 lus ; cette extension de l'exemption réglementaire doit être articulée avec l'habilitation législative de L. 111-19-1, sans supprimer implicitement les obligations générales de perméabilité ou d'ombrage. Ne pas confondre le délai de deux ans après caducité avec la durée de l'autorisation d'urbanisme. La note du décret du 18 décembre 2023 décrit le régime applicable à partir de 2024, sans fixer la date de notre réforme.",
    'material_reduction',
    "Les parcs destinés à être supprimés ou transformés peuvent désormais obtenir l'exonération même lorsque leur première autorisation a été délivrée à compter du 1er juillet 2023. La réduction porte sur l'équipement temporairement inutile, sans abandon de l'obligation sur la partie restante.",
    "L'exonération reste conditionnée à une suppression ou transformation autorisée et à l'engagement des travaux pendant la validité du titre. Aucun remboursement d'équipement ancien, coût global ou effet européen n'est démontré ; l'articulation législative est à contrôler.",
    "Aucune charge nouvelle identifiée : retrait d'une condition de date, sans nouvelle autorisation, attestation ou déclaration ; la première autorisation et la caducité existaient déjà dans la source.",
    [effect('relief_extended', 'parkings-exemption-transformation-sans-date-butoir',
            "Ouverture de l'exemption aux suppressions ou transformations autorisées après l'ancienne date butoir.",
            "Exemption des équipements visés à L. 111-19-1 seulement si la première autorisation de suppression ou transformation était délivrée avant le 1er juillet 2023.",
            "Même exemption sans date butoir ; partie restante toujours équipée, et délai inchangé de deux ans après caducité faute de commencement des travaux.",
            'legal_duty', "Propriétaires de parcs dont la suppression ou transformation totale ou partielle a été autorisée.",
            "Obligations restant à exécuter après la réforme, dossiers en cours inclus ; droits anciens conservés et travaux déjà réalisés non remboursés.",
            "Aucune formalité de remplacement ; les conditions matérielles et la validité du titre restent exigées.",
            "pour laquelle une première autorisation d'urbanisme a été délivrée avant le 1er juillet 2023.",
            "pour laquelle une première autorisation d'urbanisme a été délivrée.")],
    ["Condition imposant une première autorisation de suppression ou de transformation délivrée avant le 1er juillet 2023 pour accéder à l'exonération."],
    "L'exonération des revêtements, aménagements hydrauliques, dispositifs végétalisés et d'ombrage est conservée et ouverte aux autorisations futures. La caducité et les deux ans suivant celle-ci restent inchangés, de même que l'équipement de la partie non transformée. Les situations antérieures éligibles ne perdent aucun droit du fait du retrait de la date butoir.")

n = 'R111-25-17'
x = S[n]['source_xml'].replace(
    'Une exemption temporaire peut être accordée par le préfet de département',
    'Une exemption temporaire s’applique de plein droit')
x = x.replace('Cette exemption temporaire peut également être accordée',
              'Cette exemption temporaire s’applique également de plein droit')
old = "Cette exemption ne peut excéder une durée de cinq ans. Elle ne peut être prorogée qu'une fois, pour une durée maximale de deux ans. A défaut d'engagement des travaux dans la durée de validité de l'autorisation octroyant le report, cette dernière est caduque. Les obligations prévues à l'article L. 111-19-1 devront alors être satisfaites dans un délai de deux ans à compter de la caducité de l'autorisation de report."
new = "Cette exemption s'applique pendant cinq ans. Elle court à compter de la date à laquelle les conditions du présent article sont réunies, sans pouvoir commencer avant l'entrée en vigueur de la réforme. Elle est prorogée de plein droit une seule fois, pour deux ans, si ces conditions demeurent réunies à l'expiration de la période initiale. A défaut d'engagement des travaux pendant la durée de l'exemption, y compris sa prorogation, l'exemption est caduque. Les obligations prévues à l'article L. 111-19-1 doivent alors être satisfaites dans un délai de deux ans à compter de cette caducité."
assert old in x
x = x.replace(old, new)
x += p("L'exemption et sa prorogation ne sont subordonnées à aucune demande, autorisation ou déclaration distincte. Les actes programmant l'opération ou la construction et les autres éléments légalement disponibles permettent d'en apprécier les conditions.")
x += p("Les présentes dispositions s'appliquent aux situations répondant à leurs conditions à compter de l'entrée en vigueur de la réforme et aux demandes en cours, sans nouveau dépôt ni reprise des délais. Les exemptions déjà accordées conservent leur date de départ et leur durée, sans réduction des droits résultant de la décision antérieure ; elles bénéficient de la prorogation de plein droit dans la limite d'une seule prorogation et de deux ans de prorogation au total. Une prorogation déjà accordée est prise en compte dans cette limite.")
put(n, x,
    "Réduction de fond : l'exemption temporaire et sa prorogation deviennent de droit lorsque les conditions matérielles sont réunies, sans autorisation préfectorale ni déclaration de remplacement. Les quatre catégories d'aménagement, les parcs voisins d'une construction faisant obstacle aux équipements, les références techniques, les cinq ans puis l'unique prorogation de deux ans et les deux ans de mise en conformité après caducité sont conservés. Le point de départ est défini pour permettre l'effet de plein droit ; les décisions antérieures gardent leur durée.",
    "Renvois L. 300-1, L. 312-1, L. 102-12, L. 303-2 CCH et R. 111-25-4/-9 : maintien de leurs champs, sans abroger les actes d'aménagement ni le PLU. Les dispositions techniques R. 111-25-4/-9 et le fondement L. 111-19-1 ont été lus. La possibilité d'exemption déjà réglementaire est transformée en droit : contrôle de l'habilitation de L. 111-19-1 et coordination des instructions préfectorales/formulaires à prévoir, sans les présenter comme réécrits. Ne pas additionner cinq ans nouveaux aux durées déjà accordées ; une prorogation ancienne consomme la limite unique.",
    'material_reduction',
    "L'obtention d'une décision préfectorale discrétionnaire et d'une décision de prorogation disparaît. L'avantage reste ouvert pour les opérations futures et devient automatique, avec les mêmes catégories matérielles et sans remplacement par une déclaration.",
    "Les opérations et documents d'aménagement nécessaires restent requis sur leurs fondements propres. Les installations dues après caducité ne sont pas abolies ; leur exécution reste soumise au délai de deux ans. Le gain de délai réel et le coût ne sont pas chiffrés.",
    "Aucune charge nouvelle identifiée : aucun dossier, registre, attestation ou autorisation de remplacement. Les conditions sont celles de la source et s'apprécient au moyen des actes de programmation et éléments légalement disponibles ; le nouveau départ ne requiert pas d'enregistrement particulier.",
    [effect('authorization_removed', 'parkings-exemption-temporaire-de-plein-droit',
            "Remplacement de l'octroi préfectoral par une exemption et une prorogation de plein droit.",
            "Exemption préfectorale facultative d'au plus cinq ans, avec une seule prorogation d'au plus deux ans ; obligations à remplir sous deux ans après caducité.",
            "Exemption de plein droit pendant cinq ans et unique prorogation de deux ans si les conditions persistent ; même délai de deux ans après caducité, sans demande distincte.",
            'legal_duty', "Propriétaires et gestionnaires des parcs répondant aux catégories d'aménagement ou de voisinage prévues par l'article.",
            "Conditions réunies après entrée en vigueur, y compris programmes antérieurs et demandes en cours ; date et durée des exemptions déjà accordées préservées, prorogation ancienne décomptée.",
            "Aucune déclaration équivalente ; actes d'aménagement et autres autorisations sectorielles restent distincts.",
            "Une exemption temporaire peut être accordée par le préfet de département",
            "L'exemption et sa prorogation ne sont subordonnées à aucune demande, autorisation ou déclaration distincte.")],
    ["Décision préfectorale préalable et caractère discrétionnaire de l'accès à l'exemption temporaire pour les situations matériellement éligibles.",
     "Autorisation distincte de prorogation de l'exemption temporaire, remplacée par une unique prorogation de plein droit sans déclaration."],
    "L'exemption temporaire, même non signalée automatiquement comme avantage, est maintenue pour les quatre catégories d'opérations et le voisinage visé par l'article. Elle reste accessible aux situations futures, devient de droit et conserve les durées favorables déjà accordées. L'unique prorogation reste possible sans nouvelle décision ; aucune obligation d'équipement n'est rétablie pendant sa validité.")

put('R111-25-18', None,
    "Maintien nécessaire : l'appréciation cumulée des coûts de toutes les obligations empêche de refuser artificiellement une exemption en fractionnant les dépenses d'un même parc existant. Ce texte favorise les exemptions économiques et ne crée ni pièce autonome ni procédure supplémentaire ; l'abroger laisserait subsister les travaux généraux en rendant leurs exceptions moins protectrices.",
    "R. 111-25-1, R. 111-25-6, R. 111-25-12, R. 111-25-13 et R. 111-25-14 lus intégralement. Le cumul porte sur les coûts et non sur des rapports à additionner ou des taux nouveaux. Ces cinq renvois restent opérants pour cette méthode ; la simplification des preuves de R. 111-25-19 ne la modifie pas. Discordance préexistante relevée dans la cible R. 111-25-1 I : elle vise le deuxième alinéa du I de L. 174-1 CCH comme base de perméabilité, tandis que la source de L. 174-1 du corpus fourni traite de consommation énergétique tertiaire et que cet alinéa vise la stratégie bas carbone. Concordance historique à vérifier et renvoi de R. 111-25-1 à corriger hors lot ; aucun renvoi de substitution n'est inventé. L. 111-19-1 fournit directement le fondement de perméabilité des parcs qui relèvent de son champ, sans couvrir fictivement tout autre champ. Note d'application au 1er janvier 2024 conservée dans la source.",
    'retained_necessary',
    "Aucun changement normatif : la prise en compte globale des coûts pour les exemptions des parcs existants est conservée. Ce maintien favorable n'est pas une nouvelle obligation supprimée.",
    "Les coûts effectivement retenus et les seuils des arrêtés ne sont pas chiffrés ici. La discordance du renvoi R. 111-25-1 I vers L. 174-1 CCH reste à résoudre hors lot, sans prétendre achevé le contrôle de tout son champ. La disposition ne supprime pas les équipements légalement dus pour les parcs ne remplissant aucune exemption.",
    "Aucune charge nouvelle identifiée : maintien exact d'une règle de calcul commune, sans nouveau document, calendrier, registre ou justification distincte.",
    benefit="La prise en compte de l'ensemble des coûts protège les exemptions pour viabilité, financement ou coût excessif des parcs existants. Elle est maintenue pour toute situation future remplissant les conditions, sans plafonnement nouveau et sans disparition de l'une des quatre exceptions visées.")

n = 'R111-25-19'
x = ''.join(map(p, [
    "Les conditions des exceptions prévues aux articles R. 111-25-4, R. 111-25-6 et R. 111-25-9 à R. 111-25-14 peuvent être établies par tout moyen. Le propriétaire du parc de stationnement peut se prévaloir des pièces du dossier d'autorisation d'urbanisme et des éléments exacts et à jour dont l'autorité compétente dispose légalement.",
    "Aucune attestation distincte, aucun résumé non technique et aucune étude technico-économique réalisée par une entreprise disposant d'une qualification particulière ne sont exigés au seul titre de la justification de ces exceptions. Les renvois du présent code à l'attestation mentionnée au présent article n'imposent pas la production d'une telle pièce.",
    "Les critères d'exonération fixés par les arrêtés mentionnés au II de l'article R. 111-25-9, l'exonération tenant à la sécurité nationale prévue au 2° du I du même article et la présomption prévue au III de l'article R. 111-25-14 demeurent applicables sans étude ni résumé non technique. Les autres conditions de fond des exceptions et leur contrôle demeurent applicables. Les études imposées sur un fondement distinct pour la sécurité ou l'évaluation environnementale restent régies par leurs dispositions propres.",
    "Le présent article s'applique aux justifications examinées à compter de l'entrée en vigueur de la réforme, y compris pour les demandes en cours, sans nouveau dépôt ni reprise des délais d'instruction. Les éléments déjà produits restent utilisables et leur présentation sous l'ancienne forme n'est pas exigée à nouveau. Les décisions antérieures et les droits qui en résultent ne sont pas remis en cause du seul fait de cette réforme."
]))
put(n, x,
    "Réduction de fond : suppression de l'attestation jointe systématique, du résumé non technique et de l'étude technico-économique obligatoirement confiée à une entreprise qualifiée pour les ombrières photovoltaïques. La preuve reste nécessaire mais devient libre, sans pièce ou déclaration équivalente. Les exceptions techniques, économiques, patrimoniales et de sécurité, ainsi que les dispenses documentaires déjà favorables, sont préservées ; la réutilisation des données déjà détenues n'est pas présentée comme un gain nouveau distinct du droit existant.",
    "Lecture intégrale des critères R. 111-25-4/-6/-9 à -14 et du fondement L. 111-19-1. Coordinations identifiées et lues : R. 431-16 r) et R. 441-8-4 continuent à viser cette attestation ; la clause expresse du nouveau corps rend ces renvois inopérants pour imposer la pièce, mais leur rédaction doit être nettoyée hors lot. Ne pas supprimer l'attestation distincte R. 171-35 CCH par cette coordination ; elle a son champ propre. R. 111-25-14 III est coordonné dans ce lot sous la même measure_id. Les arrêtés de qualification et les formulaires sont à mettre en cohérence, sans prétendre leur réécriture accomplie ni vérifier ici une conformité européenne complète.",
    'material_reduction',
    "Trois exigences documentaires expresses de la source entière sont retirées : attestation séparée, résumé non technique, étude technico-économique par entreprise qualifiée. Les conditions matérielles d'exemption sont maintenues, et les dispenses antérieures restent couvertes. Une seule mesure de preuve libre est comptée avec sa coordination R. 111-25-14.",
    "L'exploitant doit encore pouvoir établir les faits permettant l'exemption ; l'ombrage et la perméabilité ne sont pas abolis. Les exigences indépendantes de sécurité et d'évaluation environnementale subsistent. Les coûts privés évités et le solde global de complexité ne sont pas chiffrés.",
    "Aucune charge nouvelle identifiée : pas de déclaration, registre, expertise obligatoire ni formulaire de remplacement. La preuve par tout moyen n'ajoute pas de condition de fond ; la réutilisation légalement possible de pièces n'ouvre aucun nouvel accès aux données.",
    [effect('obligation_removed', 'parkings-preuve-libre-exemptions',
            "Suppression de la forme obligatoire des preuves d'exemption, dont l'expertise qualifiée et le résumé séparé.",
            "Attestation jointe à la demande avec résumé non technique ; pour les ombrières photovoltaïques, étude technico-économique par entreprise qualifiée, sous les dispenses déjà prévues.",
            "Preuve des mêmes critères par tout moyen, sans attestation distincte, résumé non technique ni étude par entreprise qualifiée obligatoires au seul titre de ces exceptions ; dispenses antérieures conservées.",
            'legal_duty', "Propriétaires des parcs invoquant les exceptions R. 111-25-4, -6, -9 à -14 ; aucune économie nouvelle imputée à ceux déjà totalement dispensés des pièces concernées.",
            "Justifications examinées dès l'entrée en vigueur, dossiers en cours inclus, sans nouveau dépôt ou délai recommencé ; décisions et droits antérieurs préservés.",
            "Pas de pièce ni déclaration équivalente ; preuve des faits et études requises par des fondements distincts maintenues.",
            "cette attestation comprend une étude technico-économique réalisée par une entreprise disposant d'une qualification définie par un arrêté conjoint des ministres chargés de l'énergie et de l'urbanisme.",
            "Aucune attestation distincte, aucun résumé non technique et aucune étude technico-économique réalisée par une entreprise disposant d'une qualification particulière ne sont exigés au seul titre de la justification de ces exceptions.")],
    ["Attestation distincte obligatoirement jointe à la demande d'autorisation pour justifier les exceptions aux équipements de stationnement.",
     "Résumé non technique systématiquement exigé en plus des éléments justifiant l'exemption, hors dispenses existantes.",
     "Étude technico-économique obligatoirement réalisée par une entreprise spécialement qualifiée pour justifier une exception d'ombrières photovoltaïques."],
    "Toutes les exceptions visées aux articles R. 111-25-4, -6, -9 à -14 restent ouvertes aux futures situations éligibles. Les dispenses d'étude et de résumé liées aux critères des arrêtés de R. 111-25-9 II, la dispense d'étude pour sécurité nationale et celle attachée à la présomption de R. 111-25-14 III ne sont pas retirées : la dispense documentaire est généralisée sans condition nouvelle. Les conditions de fond favorables ne sont ni durcies ni limitées aux droits anciens.")

put('R111-26', None,
    "Maintien nécessaire : cette règle donne au permis et à la décision sur déclaration un fondement de prescriptions répondant à des conséquences dommageables pour l'environnement, en tenant compte des mesures de l'autorisation environnementale. Ce n'est ni un agrément supplémentaire ni une déclaration générale. Supprimer cette articulation créerait un défaut de protection et de coordination plutôt qu'un doublon démontré ; aucune reformulation à droit constant n'est produite.",
    "Renvois maintenus à L. 110-1, L. 110-2 et R. 181-43 du code de l'environnement. Ils ne sont pas remplacés par une évaluation fictivement plus simple et leurs textes ne sont pas réécrits dans ce lot. La note source renvoie au 1° de l'article 17 du décret du 26 janvier 2017 : ses réserves historiques ne sont pas déclarées levées. Les obligations européennes d'évaluation éventuelles ne sont pas réputées abrogées.",
    'retained_necessary',
    "La source entière reste applicable : protection environnementale et prise en compte des prescriptions environnementales déjà décidées. Aucune simplification matérielle ou baisse de prélèvement n'est revendiquée.",
    "La proportionnalité d'une prescription et les régimes européens applicables à un projet déterminé demeurent à apprécier au cas par cas ; aucune expertise de projet ni réécriture du code de l'environnement n'est effectuée ici.",
    "Aucune charge nouvelle identifiée puisque le texte et ses conditions sont maintenus à l'identique ; aucune étude, déclaration ou autorisation supplémentaire n'est ajoutée.")

put('R111-27', None,
    "Maintien nécessaire : protection transversale du caractère des lieux, des sites, des paysages et des perspectives monumentales contre une atteinte imputable au projet. Ce fondement conditionné à une atteinte réelle est distinct des trois prescriptions nationales redondantes supprimées à R. 111-28 à R. 111-30. Il assure la protection patrimoniale sans instaurer ici un nouveau titre, une consultation ou une pièce obligatoire.",
    "R. 111-1 lu : R. 111-27 reste applicable y compris en présence d'un PLU, contrairement aux trois articles suivants sauf mécanisme particulier de R. 151-19. La suppression des règles de hauteur moyenne, d'harmonisation générale et des prescriptions industrielles ne supprime donc pas la conservation des paysages. Les régimes autonomes de monuments, sites, littoral et recours ne sont pas modifiés.",
    'retained_necessary',
    "Aucun changement du corps : le contrôle d'une atteinte aux lieux ou au patrimoine reste possible. Il ne se confond pas avec le maintien des trois contraintes esthétiques nationales supprimées dans les articles voisins.",
    "La décision sur un projet reste motivée selon son régime propre et contrôlable ; aucun gain financier ou de délai n'est établi par ce maintien. Les protections sectorielles ne sont pas réécrites ici.",
    "Aucune charge nouvelle identifiée : conservation exacte d'un contrôle existant sans nouvelle consultation, nouvelle étude ou condition formelle supplémentaire.")

repeal_common = (
    "Cette abrogation s'applique aux décisions prises à compter de l'entrée en vigueur de la réforme, y compris sur les demandes en cours, sans nouveau dépôt ni reprise des délais d'instruction. "
    "Les renvois au présent article ne maintiennent ni ne rétablissent la contrainte abrogée. "
    "Les autorisations délivrées et les prescriptions prises avant cette entrée en vigueur conservent leurs effets, sous réserve de leurs procédures ordinaires de modification, de retrait et de recours. "
    "Les règles distinctes de sécurité, de salubrité, d'environnement, de protection du patrimoine et des paysages demeurent applicables."
)
repeals = {
    'R111-28': (
        "Le présent article est abrogé. La hauteur supérieure à la hauteur moyenne des constructions avoisinantes ne peut plus, sur son seul fondement, justifier un refus d'autorisation ou des prescriptions particulières.",
        "Suppression de fond de la restriction autonome tirée du seul dépassement de la hauteur moyenne dans les secteurs partiellement bâtis d'aspect unitaire hors rénovation. Elle fait obstacle aux extensions et surélévations sans exiger une atteinte paysagère distincte. R. 111-27, les règles de sécurité et les prescriptions locales valablement fondées restent applicables ; l'abrogation ne donne donc pas un droit général de construire à toute hauteur.",
        "Pouvoir national de refus ou de prescriptions pour dépassement de la hauteur moyenne dans les secteurs déjà partiellement bâtis d'aspect unitaire hors programmes de rénovation.",
        "l'autorisation de construire à une hauteur supérieure à la hauteur moyenne des constructions avoisinantes peut être refusée ou subordonnée à des prescriptions particulières.",
        "Dans les secteurs partiellement bâtis d'aspect unitaire hors rénovation, dépassement de la hauteur moyenne pouvant suffire au refus ou à une prescription nationale particulière.",
        "Suppression de ce seul motif national ; contrôle de l'atteinte aux paysages par R. 111-27 et autres règles de hauteur autonomes conservés.",
        "La hauteur supérieure à la hauteur moyenne des constructions avoisinantes ne peut plus, sur son seul fondement, justifier un refus d'autorisation ou des prescriptions particulières.",
        "Porteurs de constructions, extensions et surélévations dans le champ territorial effectif de R. 111-28."
    ),
    'R111-29': (
        "Le présent article est abrogé. L'emploi de matériaux différents de ceux des façades principales pour les murs séparatifs ou aveugles ne peut plus, sur son seul fondement, imposer une harmonisation de leur aspect avec celui des façades.",
        "Suppression de fond de l'obligation nationale autonome d'harmonisation des murs séparatifs et aveugles lorsque leurs matériaux diffèrent des façades principales. La protection d'un paysage ou d'un ensemble patrimonial reste assurée par R. 111-27 et les régimes locaux ou sectoriels autonomes ; l'uniformité d'aspect imposée sans atteinte identifiée n'a pas de fonction essentielle distincte démontrée.",
        "Obligation générale d'harmonisation de l'aspect des murs séparatifs et aveugles construits dans des matériaux différents des façades principales.",
        "avoir un aspect qui s'harmonise avec celui des façades.",
        "Obligation d'harmoniser l'aspect des murs séparatifs et aveugles si leurs matériaux diffèrent des façades principales.",
        "Fin de cette obligation nationale autonome, sans suppression des protections paysagères ou prescriptions locales ayant leur propre fondement.",
        "L'emploi de matériaux différents de ceux des façades principales pour les murs séparatifs ou aveugles ne peut plus, sur son seul fondement, imposer une harmonisation de leur aspect avec celui des façades.",
        "Constructeurs et propriétaires des murs concernés dans le champ territorial effectif de R. 111-29."
    ),
    'R111-30': (
        "Le présent article est abrogé. La seule nature industrielle, légère ou provisoire d'une installation ou d'une construction ne peut plus, sur son fondement, justifier des prescriptions particulières, notamment un écran de verdure ou une marge de reculement.",
        "Suppression de fond du fondement autonome de prescriptions lié à la seule catégorie industrielle, légère ou provisoire de l'ouvrage. Les atteintes concrètes à la sécurité, à la salubrité, à l'environnement ou aux paysages continuent de relever notamment de R. 111-2, R. 111-26 et R. 111-27, et les marges ou écrans imposés par une règle autonome restent distincts. Le doublon national est retiré plutôt que réécrit.",
        "Pouvoir national de prescriptions particulières pour installations ou bâtiments industriels et constructions légères ou provisoires, dont écrans de verdure et marges de reculement.",
        "peut être subordonnée à des prescriptions particulières, notamment à l'aménagement d'écrans de verdure ou à l'observation d'une marge de reculement.",
        "La catégorie industrielle, légère ou provisoire permet des prescriptions nationales particulières, sans condition expresse d'atteinte dans cet article.",
        "Suppression de ce seul fondement ; prescriptions requises par la sécurité, l'environnement, le patrimoine, les paysages ou un texte local autonome conservées.",
        "La seule nature industrielle, légère ou provisoire d'une installation ou d'une construction ne peut plus, sur son fondement, justifier des prescriptions particulières, notamment un écran de verdure ou une marge de reculement.",
        "Porteurs d'installations ou bâtiments industriels et de constructions légères ou provisoires dans le champ territorial effectif de R. 111-30."
    ),
}
for n, (opening, reason, scope, quote, before, after, prop_quote, population) in repeals.items():
    put(n, p(opening) + p(repeal_common), reason,
        "R. 111-1 et R. 151-19 lus en entier : hors PLU, application directe du RNU ; certaines zones de PLUi peuvent aussi incorporer ces articles. Nettoyer leur plage R. 111-28 à R. 111-30 dans ces deux articles hors lot ; la clause opératoire interdit déjà qu'un renvoi fasse survivre le fondement abrogé. R. 111-2, R. 111-26, R. 111-27, L. 151-18 et L. 421-6/-8 lus pour distinguer les protections autonomes. Les règles locales reposant sur leur propre base légale ne sont pas abrogées par assimilation. Les prescriptions individuelles antérieures ne sont pas effacées automatiquement. Aucune filiation SRU n'est affirmée pour justifier cette coupe.",
        'material_reduction',
        "Abrogation réelle de la contrainte décrite dans la source entière, pour les décisions futures et les dossiers en cours. Cette composante relève de la mesure commune de suppression des prescriptions esthétiques nationales redondantes ; les autorisations d'urbanisme elles-mêmes subsistent.",
        "Le gain concerne le seul fondement national abrogé. Un projet peut encore rencontrer une règle locale autonome, un risque ou une atteinte patrimoniale ; aucune économie moyenne, augmentation de capacité automatique ou baisse générale du délai de permis n'est démontrée.",
        "Aucune charge nouvelle identifiée : le pouvoir et l'obligation correspondants sont retirés sans demande, déclaration ou contrôle de remplacement. Les garanties et procédures indépendantes ne sont pas étendues.",
        [effect('obligation_removed', 'rnu-prescriptions-esthetiques-redondantes',
                scope, before, after, 'legal_duty', population,
                "Décisions à compter de l'entrée en vigueur, demandes en cours incluses, sans nouveau dépôt ; titres et prescriptions antérieurs gardent leurs effets et leurs procédures de modification et de recours.",
                "Aucune procédure de remplacement ; les contraintes autonomes distinctes restent dans leur propre champ.",
                quote, prop_quote)], repeal=scope)

put('R111-31', None,
    "Maintien intégral nécessaire : la section camping n'est pas applicable aux foires, marchés, voies et places publiques ni aux aires d'accueil des gens du voyage visées par la loi du 5 juillet 2000. Il s'agit d'une exclusion favorable et d'une séparation de régimes, non d'un nouveau contrôle. L'abroger étendrait des contraintes de loisirs à des usages distincts ; aucune simplification supplémentaire utile n'est obtenue par un changement de mots.",
    "La portée de l'exclusion concerne la présente section, non l'ensemble du code ni les pouvoirs de police de la voirie. R. 111-32 à R. 111-43 lus, ainsi que R. 443-1 pour la séparation des aires de gens du voyage. La loi n° 2000-614 reste un fondement autonome, sans assimilation de l'habitat permanent à une activité de camping.",
    'retained_necessary',
    "L'exclusion entière est préservée : aucune extension des contraintes de camping aux usages publics ou aux aires d'accueil visées. Ce maintien favorable ne constitue pas une nouvelle réduction.",
    "Les obligations propres à la voirie, à la sécurité et aux aires d'accueil ne sont pas modifiées ni réputées abolies. Aucun effet de coût ou de couverture nationale n'est calculé.",
    "Aucune charge nouvelle identifiée : aucune donnée, pièce ou autorisation supplémentaire n'est ajoutée, et l'exclusion existante conserve exactement son périmètre.",
    benefit="L'exclusion de toute la section pour les foires, marchés, voies et places publiques et les aires de la loi du 5 juillet 2000 est maintenue sans réserve nouvelle, y compris pour les futurs usages et aires entrant dans le champ légal. Les protections propres aux gens du voyage ne sont pas ramenées au régime des loisirs.")

put('R111-32', None,
    "Maintien nécessaire : principe de liberté du camping hors routes et voies publiques, avec accord du titulaire de la jouissance du sol et réserve de l'opposition du propriétaire. Ce consentement protège des droits privés distincts ; le supprimer ne serait pas un simple retrait d'agrément administratif. Aucun dépôt ou autorisation de remplacement n'est créé, et les limites sectorielles sont examinées séparément.",
    "La réserve des conditions de la sous-section reste cohérente avec le maintien de R. 111-33 et l'allègement de R. 111-34. Ne pas confondre accord de la personne ayant la jouissance et droit du propriétaire d'opposition, ni étendre le camping aux routes et voies publiques par omission.",
    'retained_necessary',
    "Le principe favorable de libre pratique et les consentements privés sont intégralement conservés. Aucun changement réel de régime ni allègement nouveau n'est revendiqué pour cet article.",
    "La liberté reste encadrée par les interdictions et protections propres aux sites et usages du sol ; elle ne vaut ni titre d'occupation publique ni droit d'imposer une présence au propriétaire.",
    "Aucune charge nouvelle identifiée : maintien des seuls consentements privés existants et des limites déjà présentes, sans dossier, registre ou déclaration nouvelle.",
    benefit="La liberté de camping reste ouverte à toute future pratique recevable hors voies publiques ; l'accord de la personne ayant la jouissance et l'opposition éventuelle du propriétaire gardent leur portée exacte. Aucun agrément administratif général n'est ajouté sous couvert de conservation de ces consentements.")

put('R111-33', None,
    "Maintien nécessaire après examen des quatre interdictions et de leurs dérogations : rivages et sites inscrits, sites classés ou en instance, patrimoine remarquable et abords des monuments, captages d'eau potable. Les contrôles de paysage, de patrimoine et d'eau potable ont ici une fonction essentielle identifiable ; la compétence de décision et les avis ne sont pas démontrés redondants. Les dérogations favorables sont toutes conservées pour l'avenir, sans réduction aux seuls droits acquis.",
    "L. 422-1 à L. 422-3 lus intégralement : leur plage reste utile pour identifier l'autorité compétente. Le d) de la source de L. 422-2 contient toutefois la substitution liée à la carence SRU : cette composante appelle sa propre suppression hors lot conformément à sru_abrogation ; le renvoi de compétence du présent article ne vaut ni maintien de cette carence ni rétablissement d'un quota. L. 341-1/-2 environnement, L. 631-1 et L. 621-30 patrimoine, L. 1321-2 santé publique restent dans leurs champs autonomes. Le rayon de 200 mètres, le seul avis expressément favorable du 4°, la double consultation des 1° et 3° et la consultation du 2° sont conservés sans permutation. R. 111-48 lu : son renvoi reste opérant. Ces dérogations au camping ne remplacent pas le schéma de plage des articles L. 121-28 à L. 121-30 et ne le ferment pas. Aucune filiation SRU incertaine n'est comptée comme achevée.",
    'retained_necessary',
    "Les quatre protections territoriales et leurs quatre voies de dérogation restent inchangées. Aucun supplément d'interdiction ni suppression d'une possibilité littorale n'est introduit ; le maintien ne compte pas comme simplification.",
    "L'octroi d'une dérogation reste soumis à son avis et à son autorité propres, sans dispense fictive des normes supérieures. La coordination autonome du d) de L. 422-2 avec la suppression de carence SRU reste hors de ce lot ; le présent renvoi de compétence ne la rétablit pas. Les codes environnement, patrimoine et santé ne sont pas réécrits ni audités intégralement ici.",
    "Aucune charge nouvelle identifiée : le texte entier, ses consultations et les mêmes conditions de dérogation sont maintenus sans nouvelle pièce, nouveau taux ou nouveau délai.",
    benefit="Les quatre avantages possibles sont conservés : dérogation sur rivages et sites inscrits après ABF et commission, dérogation dans les sites classés ou en instance après commission, dérogation dans les sites patrimoniaux remarquables et les abords dans les conditions du 1°, dérogation dans les 200 mètres d'un captage après avis favorable sanitaire. Chaque voie reste ouverte aux demandes futures éligibles ; aucune n'est limitée aux situations antérieures ni confondue avec le schéma de plage littoral.")

n = 'R111-34'
x = ''.join(map(p, [
    "La pratique du camping en dehors des terrains aménagés à cet effet ne peut être interdite dans certaines zones par le plan local d'urbanisme ou le document d'urbanisme en tenant lieu que lorsqu'elle est de nature à porter atteinte à la salubrité, à la sécurité ou à la tranquillité publiques, aux paysages naturels ou urbains, à la conservation des perspectives monumentales, à la conservation des milieux naturels ou à l'exercice des activités agricoles et forestières. Pour ces mêmes motifs, l'interdiction peut également être prononcée par arrêté du maire.",
    "Ces interdictions ne sont opposables que si elles ont été portées à la connaissance du public par affichage en mairie et par apposition de panneaux aux points d'accès habituels aux zones visées par ces interdictions. Un arrêté conjoint des ministres chargés de l'urbanisme et du tourisme fixe les conditions dans lesquelles est établie cette signalisation.",
    "A compter de l'entrée en vigueur de la réforme, une interdiction fondée sur le présent article, y compris lorsqu'elle figure dans un document ou un arrêté antérieur, n'est opposable que pour l'un des motifs mentionnés au premier alinéa. Les mesures de publicité régulièrement accomplies ne sont pas à renouveler du seul fait de la réforme. Les mêmes règles s'appliquent aux interdictions opposées par renvoi au présent article. Les interdictions fondées sur une disposition distincte conservent leur régime propre."
]))
put(n, x,
    "Réduction de fond : le PLU ne peut plus interdire le camping hors terrains aménagés sans rattachement à l'un des motifs essentiels déjà énumérés pour le maire. La source offrait au document d'urbanisme un pouvoir d'interdiction autonome sans ce rattachement exprès. Les sept groupes de motifs, la faculté du maire et la double publicité d'opposabilité sont conservés ; les interdictions anciennes sans motif relevant de cette liste cessent d'être opposables pour l'avenir sur ce seul fondement.",
    "R. 111-32, R. 111-33 et R. 111-49 lus. Le renvoi des caravanes à R. 111-34 reste valable et suit la limitation nouvelle, sans retirer l'exception des caravanes professionnelles ni l'autorisation municipale jusqu'à quinze jours prévues dans R. 111-49. Les motifs d'ordre public, paysages, perspectives monumentales, milieux naturels, agriculture et forêt sont tous maintenus. Aucune révision obligatoire de tous les PLU, recensement d'interdictions ou nouvelle signalisation n'est imposé ; les interdictions issues d'autres fondements restent distinctes.",
    'material_reduction',
    "Le pouvoir d'interdiction autonome du PLU est réduit aux motifs matériels déjà prévus pour la police municipale du camping. La liberté s'accroît uniquement dans les zones où une interdiction de ce seul fondement ne répond à aucun de ces motifs, sans enlever les protections essentielles.",
    "Aucun nombre de zones libérées ni coût économisé n'est établi. Les interdictions pour risques, salubrité, tranquillité, paysage, patrimoine, nature ou activités agricoles et forestières subsistent, ainsi que les autres régimes légaux de protection.",
    "Aucune charge nouvelle identifiée : aucune nouvelle procédure de motivation formalisée, liste, donnée, publication ou révision documentaire obligatoire. La liste de motifs déjà existante borne désormais les deux voies d'interdiction ; les publicités accomplies restent valables.",
    [effect('obligation_removed', 'camping-interdictions-locales-motifs-essentiels',
            "Retrait des interdictions de PLU sans rattachement à un motif essentiel prévu par l'article.",
            "Camping hors terrains aménagés pouvant être interdit par le PLU sans condition expresse de motif dans la première phrase ; arrêté du maire déjà lié aux motifs énumérés.",
            "PLU et arrêté du maire limités à la même liste de motifs ; interdictions anciennes sans l'un de ces motifs inopposables pour l'avenir sur ce fondement, publicité inchangée.",
            'legal_duty', "Campeurs et propriétaires des zones interdites sur le seul fondement de R. 111-34 ; caravanes dans le champ du renvoi R. 111-49.",
            "Opposabilité appréciée dès l'entrée en vigueur, y compris pour les textes anciens ; aucune publicité régulière à refaire et autres fondements d'interdiction conservés.",
            "Aucun permis, déclaration ou signalement nouveau en contrepartie de la limitation.",
            "La pratique du camping en dehors des terrains aménagés à cet effet peut en outre être interdite dans certaines zones par le plan local d'urbanisme ou le document d'urbanisme en tenant lieu.",
            "La pratique du camping en dehors des terrains aménagés à cet effet ne peut être interdite dans certaines zones par le plan local d'urbanisme ou le document d'urbanisme en tenant lieu que lorsqu'elle est de nature à porter atteinte à la salubrité, à la sécurité ou à la tranquillité publiques, aux paysages naturels ou urbains, à la conservation des perspectives monumentales, à la conservation des milieux naturels ou à l'exercice des activités agricoles et forestières.")],
    ["Pouvoir d'interdire le camping par PLU ou document en tenant lieu sans rattachement exprès aux motifs essentiels déjà énumérés pour l'arrêté du maire."],
    "La garantie d'inopposabilité sans affichage en mairie et panneaux d'accès reste entière pour les usagers futurs. Les exceptions aux interdictions de caravanes prévues par R. 111-49 restent distinctes et applicables ; l'allègement ne remplace aucune dérogation existante par une autorisation nouvelle.")

put('R111-35', None,
    "Maintien nécessaire : les normes d'aménagement, d'équipement et de fonctionnement des terrains de camping assurent notamment des fonctions de salubrité et de sécurité et n'ont pas ici la forme d'un agrément supplémentaire. La faculté de règles adaptées à l'exploitation saisonnière est favorable et préservée. Sans les arrêtés d'exécution dans le lot, supprimer en bloc cette base ferait aussi tomber des protections essentielles non isolées ; aucune reformulation de remplissage n'est proposée.",
    "R. 443-2, R*443-6 et R*443-7 lus en entier : notice d'insertion, capacité du permis et régime d'exploitation saisonnière restent coordonnés. L. 443-2/-3 maintiennent distinctement information, alerte et évacuation dans les zones à risque. Les arrêtés conjoints ne sont pas joints ; aucune suppression de leurs normes particulières n'est prétendue accomplie. La durée saisonnière règle l'exploitation du terrain, pas la durée d'un contrat de travail.",
    'retained_necessary',
    "Aucune modification de la source entière : maintien de la base des normes des campings et de leur adaptation saisonnière. Ce maintien ne constitue ni une nouvelle procédure supprimée ni une réforme des emplois saisonniers.",
    "L'utilité de chaque prescription détaillée des arrêtés n'est pas établie ici ; leur examen reste extérieur à cet article. Le maintien ne prouve pas l'absence de tout doublon dans l'ensemble de la réglementation du tourisme.",
    "Aucune charge nouvelle identifiée : ni titre, donnée, fréquence de transmission ou norme technique ne sont ajoutés ; la possibilité de règles saisonnières adaptées reste facultative dans les mêmes conditions.",
    benefit="La faculté de prévoir des règles particulières pour l'exploitation saisonnière de R. 443-7 reste intégralement ouverte aux futurs terrains éligibles. Elle n'est pas limitée aux autorisations anciennes et n'est pas transformée en obligation générale d'exploitation ou en CDD de personnel.")

put('R111-36', None,
    "Maintien nécessaire : base des normes d'aménagement, d'équipement et de fonctionnement des parcs résidentiels de loisirs. Les fonctions de sécurité et de salubrité ne peuvent être effacées par l'abrogation globale de cette habilitation ; aucune autorisation ou transmission périodique distincte n'est prévue par cet article. Les prescriptions détaillées d'insertion ne sont pas isolables sur le seul texte fourni ; aucune réécriture stylistique n'est fabriquée.",
    "R. 443-1 et R*443-6 lus : la première disposition comporte une exception pour certains PRL exploités par cession ou location supérieure à un an renouvelable ; ce lot n'en supprime pas le bénéfice et ne prétend pas étendre automatiquement toutes les règles du chapitre à ces PRL. L. 443-1 et R*421-19 d) maintiennent leur champ propre d'aménagement. Les arrêtés conjoints ne sont pas réécrits ici.",
    'retained_necessary',
    "Aucune différence avec la source entière : conservation du socle réglementaire des PRL, sous les champs et exclusions autonomes applicables. Aucun gain de coût ou baisse de contrainte n'est imputé à ce maintien.",
    "L'examen des arrêtés techniques n'est pas réalisé dans ce lot ; il ne permet pas de déclarer chaque détail nécessaire. La nouvelle ouverture de R. 111-42 ne vaut pas suppression générale des règles d'aménagement des PRL.",
    "Aucune charge nouvelle identifiée : texte maintenu exactement, sans extension de la compétence ministérielle, nouvelle autorisation ou nouvelles données à fournir.")

put('R111-37', None,
    "Maintien nécessaire : définition autonome des habitations légères de loisirs par leur caractère démontable ou transportable et leur usage temporaire ou saisonnier de loisirs. Elle permet d'appliquer un régime favorable adapté sans assimiler toute construction permanente à un hébergement léger. Elle ne prescrit ici ni démarche, ni durée de bail, ni emploi saisonnier.",
    "R. 111-38 à R. 111-40 et R*421-2 b), R. 421-9 b), R. 421-11 II a) lus : les seuils de formalités et les protections de sites utilisent toujours cette catégorie. Le plafond supprimé à R. 111-38 ne change pas la définition ni le seuil distinct de trente-cinq mètres carrés de surface de plancher.",
    'retained_necessary',
    "Aucun changement par rapport à la source entière : maintien d'une définition utile aux dispenses et aux régimes d'implantation. Ce n'est ni une autorisation ni une obligation autonome supprimée.",
    "L'article ne régit pas le logement permanent, les caravanes ou les résidences mobiles ; aucune extension à ces populations ni garantie de dispense universelle de permis n'est avancée.",
    "Aucune charge nouvelle identifiée : aucun certificat, délai, contrôle additionnel ou justificatif n'est ajouté à la définition existante.",
    benefit="La catégorie démontable ou transportable reste le support des possibilités et dispenses applicables aux futurs hébergements éligibles. Le caractère temporaire ou saisonnier de l'occupation reste distinct de la durée d'un bail ou d'un emploi ; aucune nouvelle restriction de ces durées n'est créée.")

n = 'R111-38'
old = " Dans ce cas, le nombre d'habitations légères de loisirs doit demeurer inférieur soit à trente-cinq lorsque le terrain comprend moins de 175 emplacements, soit à 20 % du nombre total d'emplacements dans les autres cas."
assert old in S[n]['source_xml']
x = S[n]['source_xml'].replace(old, '')
x += p("Le présent article n'impose pas de plafond national du nombre d'habitations légères de loisirs, ni de proportion maximale de ces habitations parmi les emplacements. La capacité d'accueil et la répartition des emplacements légalement fixées par l'autorisation d'aménager, lorsqu'une telle autorisation est requise, demeurent applicables, ainsi que les règles de sécurité, de salubrité et de protection de l'environnement et des sites.")
x += p("Ces dispositions s'appliquent aux implantations réalisées et aux décisions prises à compter de l'entrée en vigueur de la réforme, y compris sur les demandes en cours, sans nouveau dépôt ni reprise des délais. Les prescriptions des autorisations délivrées antérieurement conservent leurs effets et peuvent être modifiées selon les procédures ordinaires ; les contrats valablement conclus et les droits des tiers sont préservés.")
put(n, x,
    "Réduction de fond : suppression du plafond national inférieur à trente-cinq HLL sous 175 emplacements et inférieur à 20 % dans les autres campings éligibles. Le nombre et la répartition autorisés par le permis d'aménager assurent déjà un contrôle propre de la capacité ; un second plafond national de typologie n'a pas de fonction essentielle distincte démontrée. Les quatre catégories de lieux, toutes les exclusions du 4° et la référence au 1er octobre 2007 sont conservées.",
    "R*443-6 lu : le permis fixe le nombre maximal d'emplacements et délimite les emplacements HLL ; il n'est pas automatiquement modifié. R*421-19 c), e), f), R. 443-2, R*421-2 b), R. 421-9 b), R. 421-11 II a) et R*421-8-2 lus. Le seuil distinct de 35 m² de surface de plancher n'est pas supprimé avec le seuil de 35 unités. La création d'une aire naturelle, les petits campings déclarés et les catégories exclues ne sont pas ouverts aux HLL par ce texte. R. 111-39/-40 restent coordonnés à la liste inchangée.",
    'material_reduction',
    "Le contingent national de HLL dans les campings éligibles disparaît ; le permis et les règles de sécurité restent opérants. Il s'agit d'une réduction de la restriction de composition des emplacements, sans création de capacité globale automatique.",
    "Un permis existant peut encore limiter le nombre et la localisation des HLL ; sa modification éventuelle suit la procédure ordinaire. Les campings exclus du 4° et les protections patrimoniales restent hors du gain. Aucune quantité d'hébergements supplémentaire n'est calculée.",
    "Aucune charge nouvelle identifiée : retrait du second plafond national sans nouveau registre, quota, déclaration ou autorisation de remplacement ; capacité et formalités d'aménagement préexistantes seulement réservées.",
    [effect('obligation_removed', 'hll-suppression-contingent-national-campings',
            "Suppression du contingent de typologie HLL dans les campings admissibles.",
            "Campings éligibles : nombre de HLL strictement inférieur à 35 si moins de 175 emplacements, sinon strictement inférieur à 20 % des emplacements, en plus du permis.",
            "Aucun plafond national en unités ou pourcentage par cet article ; capacité et répartition légalement fixées par le permis toujours applicables, ainsi que les exclusions de lieux.",
            'other', "Exploitants et usagers des terrains de camping admis au 4° ; pas les terrains explicitement exclus.",
            "Implantations et décisions futures, demandes en cours incluses ; anciens permis non modifiés automatiquement et contrats valides préservés.",
            "Aucun contingent ni reporting de remplacement ; autorisations ordinaires d'aménagement et de construction dans leurs champs existants.",
            "le nombre d'habitations légères de loisirs doit demeurer inférieur soit à trente-cinq lorsque le terrain comprend moins de 175 emplacements, soit à 20 % du nombre total d'emplacements dans les autres cas.",
            "Le présent article n'impose pas de plafond national du nombre d'habitations légères de loisirs, ni de proportion maximale de ces habitations parmi les emplacements.")],
    ["Plafond national de HLL strictement inférieur à trente-cinq unités pour un camping de moins de 175 emplacements ou à 20 % du total des emplacements dans les autres cas."],
    "Les possibilités d'implantation dans les PRL, villages classés, maisons familiales agréées et campings éligibles sont conservées et, pour ces derniers, libérées du contingent national. Les dispenses liées à la catégorie HLL et aux accessoires amovibles restent ouvertes aux situations futures, sous leurs propres conditions ; le seuil distinct de 35 m² n'est pas altéré.")

put('R111-39', None,
    "Maintien nécessaire de l'autorisation d'accoler auvents, rampes et terrasses amovibles aux HLL dans les lieux admissibles. L'absence de scellement ou fixation définitive et le démontage facile et rapide déterminent le caractère accessoire qui justifie la dispense de formalité ; les enlever sans coordination élargirait cette dispense à des ouvrages fixes. Aucun dossier particulier n'est ajouté.",
    "R. 111-38 et R*421-8-2 lus : la liste des lieux du premier est conservée et la dispense d'accessoires amovibles du second reste utilisable. R. 111-40 ne modifie pas ces critères de mobilité. Ne pas transformer l'accessibilité d'une rampe en obligation de démontage nouvelle ou généraliser ce régime aux terrasses fixes.",
    'retained_necessary',
    "La possibilité d'accessoires amovibles et ses conditions techniques sont conservées sans changement. Cette disposition favorable n'est pas comptée comme une nouvelle suppression de formalité.",
    "Les accessoires fixes ou situés hors des lieux autorisés conservent leur régime propre ; aucun chiffrage ni dispense de toutes les règles de construction n'est établi.",
    "Aucune charge nouvelle identifiée : conditions inchangées de mobilité, sans attestation, délai de démontage chiffré ni nouvelle procédure.",
    benefit="Les auvents, rampes et terrasses amovibles restent admis pour toute HLL future éligible dans les lieux de R. 111-38, avec leur dispense autonome de formalité de R*421-8-2. Les trois catégories d'accessoires et leurs conditions ne sont pas restreintes aux installations anciennes.")

n = 'R111-40'
paras = re.findall(r'<p>(.*?)</p>', S[n]['source_xml'], re.S)
assert len(paras) == 1
text_source = plain(S[n]['source_xml'])
first = "En dehors des emplacements prévus à l'article R. 111-38, l'implantation des habitations légères de loisirs est soumise au droit commun des constructions."
old_second = "Il en est de même en cas d'implantation d'une habitation légère de loisirs sur un emplacement situé à l'intérieur du périmètre d'un terrain de camping, village de vacances ou dépendance de maison familiale mentionné aux 2° à 4° de l'article R. 111-38 qui a fait l'objet d'une cession en pleine propriété, de la cession de droits sociaux donnant vocation à son attribution en propriété ou en jouissance ou d'une location pour une durée supérieure à deux ans."
assert first in text_source and old_second in text_source
new_second = "Dans les emplacements des terrains de camping, villages de vacances et dépendances de maisons familiales mentionnés aux 2° à 4° de l'article R. 111-38, une cession en pleine propriété, une cession de droits sociaux donnant vocation à l'attribution de l'emplacement en propriété ou en jouissance ou la durée d'une location ne soumettent pas, à elles seules, l'implantation d'une habitation légère de loisirs au droit commun des constructions. Le régime des habitations légères de loisirs demeure applicable tant que la construction répond à la définition de l'article R. 111-37 et que les autres conditions d'implantation sont remplies."
x = S[n]['source_xml'].replace(old_second, new_second).replace(
    'Les dispositions du précédent alinéa ne sont pas applicables :',
    "Ce régime reste notamment applicable dans les situations suivantes, sans que leur énumération limite la règle de l'alinéa précédent :")
x += p("Les présentes dispositions s'appliquent aux implantations réalisées à compter de l'entrée en vigueur de la réforme et aux demandes en cours, sans nouveau dépôt ni reprise des délais d'instruction. Les autorisations antérieurement délivrées, les contrats valablement conclus et les droits des tiers sont préservés ; les procédures ordinaires de modification et de recours demeurent applicables.")
put(n, x,
    "Réduction de fond : retrait du basculement vers le droit commun fondé uniquement sur la propriété, la cession de droits sociaux ou une location supérieure à deux ans. Ces modalités civiles ne modifient pas à elles seules le caractère démontable, l'usage de loisirs ou l'impact de l'hébergement. Le droit commun hors emplacements de R. 111-38 reste entier. Les 1° à 3° antérieurs à octobre 2011 sont intégralement conservés à titre de situations bénéficiant du régime, sans limiter l'ouverture nouvelle aux opérations futures.",
    "R. 111-37/-38, R*421-2 b), R. 421-9 b) et R. 421-11 II a) lus : définition, liste des lieux, seuil de 35 m² et protections patrimoniales demeurent. Le renvoi aux 2° à 4° et les trois subdivisions sont conservés. R. 111-44, lu, concerne les résidences mobiles et non les HLL : sa restriction autonome n'est pas abrogée par ce texte ; R*421-23 d) reste propre aux caravanes. Les dates du 1er octobre 2011 et la protection jusqu'au terme du bail ancien au 3° sont conservées sans fermer les nouveaux bénéficiaires.",
    'material_reduction',
    "Le régime adapté des HLL reste accessible après cession ou location longue, sans dépendre d'une situation antérieure au 1er octobre 2011. Il s'agit d'une extension réelle du régime favorable ; les dispenses anciennes des trois subdivisions ne sont pas retirées.",
    "Le gain ne concerne que les HLL au sens de R. 111-37 dans les lieux admissibles. Les résidences mobiles, caravanes, résidences permanentes et constructions hors de ces emplacements restent à leur régime ; aucun nombre de permis évités ou coût national n'est calculé.",
    "Aucune charge nouvelle identifiée : retrait d'un critère de basculement, sans agrément, option, attestation ou déclaration de substitution. La définition de HLL et les autres conditions d'implantation sont préexistantes, sans nouvelle durée de bail imposée.",
    [effect('relief_extended', 'hll-regime-independant-cession-location',
            "Maintien du régime HLL indépendamment de la cession de l'emplacement ou de la longueur du bail.",
            "Dans les lieux des 2° à 4°, basculement au droit commun si cession en pleine propriété, cession de droits sociaux ou location supérieure à deux ans, sauf trois exceptions historiques de 2011.",
            "Même régime HLL malgré ces cessions et quelle que soit la durée de location ; trois garanties historiques conservées, droit commun hors lieux admissibles inchangé.",
            'regime', "Propriétaires, détenteurs de droits sociaux et locataires d'emplacements HLL dans les lieux des 2° à 4° de R. 111-38, y compris futurs bénéficiaires.",
            "Implantations futures et demandes en cours dès entrée en vigueur ; anciens titres, baux valables et droits des tiers maintenus ; aucune régularisation automatique d'infractions passées.",
            "Pas de formalité de remplacement ; conditions matérielles HLL, règles des sites et formalités de surface préexistantes demeurent.",
            old_second,
            "une cession en pleine propriété, une cession de droits sociaux donnant vocation à l'attribution de l'emplacement en propriété ou en jouissance ou la durée d'une location ne soumettent pas, à elles seules, l'implantation d'une habitation légère de loisirs au droit commun des constructions.")],
    ["Basculement obligatoire au droit commun des constructions du seul fait d'une cession en pleine propriété ou de droits sociaux sur l'emplacement HLL.",
     "Basculement obligatoire au droit commun des constructions du seul fait d'une location d'emplacement HLL supérieure à deux ans."],
    "Les trois exceptions historiques sont préservées mot pour mot dans leurs catégories : sociétés enregistrées avant le 1er octobre 2011, cessions antérieures à cette date et locations longues antérieures jusqu'à leur terme. L'avantage est en outre ouvert aux implantations futures après cession ou location longue, sans nouvelle date butoir. Les bénéficiaires anciens ne sont pas privés de leur fondement et aucune exigence nouvelle de propriété ou de durée ne les défavorise.")

put('R111-41', None,
    "Maintien nécessaire : la résidence mobile de loisirs est un véhicule habitable pour occupation temporaire ou saisonnière de loisirs, conservant la traction mais interdit à la circulation par le code de la route. Cette définition sépare les régimes des HLL, caravanes et logements permanents ; son abrogation laisserait les possibilités favorables d'installation sans catégorie précise. Aucune formalité particulière n'est créée ici.",
    "R. 111-37, R. 111-42 à R. 111-47 lus pour vérifier la distinction entre construction démontable, véhicule tractable non circulant et caravane circulante. Les possibilités d'entreposage et de relogement de catastrophe restent autonomes. La durée de l'occupation de loisirs n'est ni un bail maximal ni un contrat de travail temporaire.",
    'retained_necessary',
    "Aucun changement : maintien d'une qualification utile aux possibilités et aux limites propres aux résidences mobiles. Aucun prélèvement ou procédure n'est supprimé par cette conservation.",
    "La définition ne permet pas la circulation routière ni l'installation de toute résidence permanente ; les règles distinctes de sécurité et d'occupation du sol restent à leur champ.",
    "Aucune charge nouvelle identifiée : pas de titre, certificat, donnée, registre ou durée nouvelle ; la mobilité exigée et l'usage restent ceux de la source entière.")

n = 'R111-42'
old = ", autres que ceux créés après le 1er octobre 2007 et exploités par cession d'emplacements ou par location d'emplacements d'une durée supérieure à un an"
assert old in S[n]['source_xml']
x = S[n]['source_xml'].replace(old, '')
x += p("Ces dispositions s'appliquent aux installations réalisées et aux décisions prises à compter de l'entrée en vigueur de la réforme, y compris sur les demandes en cours, sans nouveau dépôt ni reprise des délais d'instruction. Les autorisations antérieurement délivrées, les contrats valablement conclus et les droits des tiers sont préservés. Les restrictions propres aux terrains de camping et aux villages de vacances prévues à l'article R. 111-44 conservent leur champ distinct ; elles ne sont pas étendues aux parcs résidentiels de loisirs par le présent article.")
put(n, x,
    "Réduction de fond : les PRL spécialement aménagés deviennent admissibles aux résidences mobiles de loisirs indépendamment de leur création après le 1er octobre 2007 et d'une exploitation par cession ou location supérieure à un an. La date et le mode contractuel ne démontrent pas à eux seuls un besoin de prohibition. Les villages classés, la catégorie des campings régulièrement créés et toutes les exclusions du 3° sont intégralement conservés, avec les autres régimes d'aménagement.",
    "L. 111-25 et L. 443-1, R*421-19 d), R. 443-1, R. 111-41/-43/-44 et R*421-8-2 lus. L. 111-25 confie bien au décret les catégories admissibles. Ne pas confondre la limite d'un an de l'ancien 1° avec les deux ans de R. 111-44, qui concerne seulement camping et village et reste distinct. L'exception favorable de R. 443-1 pour certains PRL à cession/location longue n'est pas retirée ; aucune extension implicite de toutes les normes de R*443-6 n'est affirmée. Le 3° conserve le repère du 1er octobre 2007 propre aux anciens campings.",
    'material_reduction',
    "La prohibition particulière des résidences mobiles dans certains PRL récents à cession ou location longue est retirée. L'ouverture porte sur cette seule catégorie, sans généraliser l'installation hors des trois types de lieux ou enlever les conditions des terrains de camping.",
    "Les installations restent des résidences mobiles de loisirs ; les autorisations d'aménagement, la sécurité, les sites et les conditions propres aux campings/villages continuent selon leur champ. Aucun volume de places nouvelles, recette ou coût global n'est établi.",
    "Aucune charge nouvelle identifiée : retrait d'une exclusion de lieux sans agrément, déclaration, registre ou contrôle de substitution. Les titres d'aménagement déjà nécessaires et les exceptions favorables autonomes ne sont pas étendus ni supprimés.",
    [effect('obligation_removed', 'rml-prl-sans-exclusion-cession-location',
            "Suppression de l'interdiction d'installation liée à la date de création et au mode d'exploitation de certains PRL.",
            "PRL spécialement aménagés exclus s'ils sont créés après le 1er octobre 2007 et exploités par cession ou location d'emplacements supérieure à un an.",
            "Tous les PRL spécialement aménagés entrent au 1°, sans ce filtre de date ou de contrat ; villages, campings, exclusions du 3° et régimes autonomes restent inchangés.",
            'legal_duty', "Exploitants et usagers de résidences mobiles dans les PRL spécialement aménagés visés par l'ancienne exclusion.",
            "Installations et décisions futures, demandes en cours incluses ; titres, contrats valables et droits des tiers antérieurs préservés, sans régularisation automatique des installations passées.",
            "Aucune formalité de remplacement ; restrictions de R. 111-44 pour camping/village conservées et non étendues aux PRL.",
            "autres que ceux créés après le 1er octobre 2007 et exploités par cession d'emplacements ou par location d'emplacements d'une durée supérieure à un an",
            "1° Dans les parcs résidentiels de loisirs spécialement aménagés à cet effet ;")],
    ["Exclusion des résidences mobiles dans les PRL créés après le 1er octobre 2007 lorsqu'ils sont exploités par cession ou location d'emplacements supérieure à un an."],
    "Les possibilités d'installation dans les trois catégories restent ouvertes aux situations futures recevables ; la première est élargie. Les accessoires amovibles restent admis avec la dispense de R*421-8-2, et l'exception de champ de R. 443-1 pour certains PRL n'est pas supprimée. Aucune dérogation d'entreposage ou de relogement après catastrophe n'est fermée.")

put('R111-43', None,
    "Maintien nécessaire de la possibilité d'accoler auvents, rampes d'accès et terrasses amovibles aux résidences mobiles de loisirs. Le démontage facile et rapide, l'absence de scellement et de fixation définitive conservent la nature accessoire qui fonde la dispense ; les supprimer isolément permettrait des ouvrages fixes sous cette dispense sans examen. Aucun justificatif distinct n'est prescrit.",
    "R. 111-42 et R*421-8-2 lus : le renvoi reste cohérent après l'élargissement des PRL au 1° de R. 111-42, et la dispense d'accessoires amovibles continue à s'appliquer aux futurs bénéficiaires éligibles. Le texte n'étend pas les résidences mobiles aux routes ni l'habitat de loisirs au logement permanent.",
    'retained_necessary',
    "Aucune modification propre : conservation de l'avantage des accessoires amovibles et de ses critères. L'élargissement des lieux résulte de R. 111-42 et n'est pas recompté comme une deuxième procédure supprimée.",
    "Les accessoires fixes et les installations hors des lieux admis gardent leur régime. Aucun gain supplémentaire de coût ou de délai n'est démontré dans cet article maintenu.",
    "Aucune charge nouvelle identifiée : maintien exact des critères d'amovibilité, sans nouveau certificat, déclaration, registre ou délai ajouté.",
    benefit="Auvents, rampes d'accès et terrasses restent permis pour les futures résidences mobiles admissibles, avec la dispense de formalité de R*421-8-2. Le renvoi à R. 111-42 bénéficie également des PRL nouvellement ouverts sans restriction supplémentaire ; les conditions techniques favorables et protectrices restent identiques.")


def validate():
    assert len(RESULT) == len(SOURCES) == 24
    assert set(RESULT) == set(S)
    kinds = {'tax_removed', 'tax_reduced', 'obligation_removed', 'obligation_merged',
             'authorization_removed', 'regime_merged', 'deadline_reduced',
             'compliance_cost_reduced', 'tax_increased', 'obligation_added',
             'deadline_increased', 'complexity_added', 'financing_transfer',
             'payment_deferred', 'relief_extended', 'relief_preserved', 'coordination'}
    units = {'percent', 'euro', 'legal_duty', 'regime', 'calendar_days',
             'working_days', 'financing', 'other'}
    for a in SOURCES:
        n = a['number']
        o = RESULT[n]
        for key in ('code_id', 'source_id', 'source_sha256', 'number'):
            assert o[key] == a[key], (n, key)
        assert len(o['reason']) >= 40 and len(o['review_notes']) >= 40
        si = o['substantive_impact']
        for key in ('assessment', 'scope_limitations', 'new_burdens_review'):
            assert len(si[key]) >= 40, (n, key)
        assert si['version'] == 1
        if a.get('benefit_check_required'):
            assert len(o.get('benefit_review', '')) >= 100, n
        if o['status'] == 'retained_unchanged':
            assert o['proposed_xml'] is None and si['effects'] == []
            assert o['classification'] == si['classification'] == 'retained_necessary'
        else:
            assert o['proposed_xml'] and o['proposed_xml'] != a['source_xml'], n
        if o.get('change_type') == 'normative_reduction':
            assert o['reform_policy_id'] == 'editorial_direction_2026_10_19'
            assert all(len(x) >= 30 for x in o['removed_provisions'])
        if o.get('change_type') == 'full_repeal':
            assert len(o['repeal_scope']) >= 30
            assert plain(o['proposed_xml']).startswith('Le présent article est abrogé')
        for e in si['effects']:
            assert e['kind'] in kinds and e['unit'] in units
            assert re.fullmatch('[a-z0-9][a-z0-9-]{5,95}', e['measure_id'])
            for key in ('description', 'before', 'after', 'affected_population',
                        'conditions_and_transition', 'replacement_or_new_burdens'):
                assert isinstance(e[key], str) and e[key]
            for key, xml in [('source_quote', a['source_xml']), ('proposed_quote', o['proposed_xml'])]:
                assert len(e[key]) >= 12 and e[key] in plain(xml), (n, key, e[key])
    return [RESULT[a['number']] for a in SOURCES]


if __name__ == '__main__':
    out = validate()
    (ROOT / 'answer.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    from collections import Counter
    print('Articles:', len(out))
    print('Statuts:', dict(Counter(a['status'] for a in out)))
    print('Impacts:', dict(Counter(a['substantive_impact']['classification'] for a in out)))
    print('Mesures distinctes:', len({e['measure_id'] for a in out for e in a['substantive_impact']['effects']}))
