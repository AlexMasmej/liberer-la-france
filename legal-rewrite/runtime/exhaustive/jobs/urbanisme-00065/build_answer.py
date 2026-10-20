import json
import re
from html import unescape


sources = json.load(open('source.json'))
answers = []


def plain(xml):
    return re.sub(r'\s+', ' ', unescape(re.sub(r'<[^>]+>', ' ', xml or ''))).strip()


def impact(classification, assessment, limitations, burdens, effects=None):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=limitations, new_burdens_review=burdens,
                effects=effects or [])


def retained(index, reason, notes, assessment, limitations, burdens, benefit=None):
    src = sources[index]
    a = {k: src[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    a.update(proposed_xml=None, reason=reason, review_notes=notes,
             status='retained_unchanged', classification='retained_necessary',
             substantive_impact=impact('retained_necessary', assessment, limitations, burdens))
    if benefit:
        a['benefit_review'] = benefit
    answers.append(a)


def changed(index, xml, reason, notes, assessment, limitations, burdens,
            removed=None, repeal_scope=None, benefit=None):
    src = sources[index]
    a = {k: src[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    a.update(proposed_xml=xml, reason=reason, review_notes=notes, status='rewrite_draft',
             substantive_impact=impact('material_reduction', assessment, limitations, burdens))
    if repeal_scope:
        a.update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19',
                 repeal_scope=repeal_scope)
    else:
        a.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19',
                 removed_provisions=removed)
    if benefit:
        a['benefit_review'] = benefit
    answers.append(a)
    return a


def effect(a, kind, measure, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    a['substantive_impact']['effects'].append(dict(
        kind=kind, measure_id=measure, description=description, before=before,
        after=after, unit=unit, affected_population=population,
        conditions_and_transition=transition, replacement_or_new_burdens=burdens,
        source_quote=source_quote, proposed_quote=proposed_quote))


retained(0,
    "Maintien intégral après examen : cet article permet de créer une ZAC par la délibération approuvant le PLU, au lieu d'imposer deux actes. La description du site et de son environnement et les raisons de ce choix sont les conditions utiles de cette faculté, nécessaires à son intelligibilité et à l'examen des incidences. Le texte ne demande ni agrément ni déclaration supplémentaire. Aucune réécriture de pure forme n'est proposée.",
    "L. 151-7-2, R. 151-2 et R. 151-3 ont été consultés dans le corpus : double compétence de la collectivité, contenu des orientations et évaluation commune restent distincts. R. 151-8-1 conserve les trois éléments propres à la ZAC. L'article n'impose pas une étude séparée de la description déjà incluse dans le rapport ; aucun doublon documentaire autonome n'est donc démontré. Les règles de création de ZAC hors de ce mécanisme ne sont pas abrogées. Aucune taxe ni formalité fiscale nouvelle n'est créée, ni aucun achèvement de l'examen SRU revendiqué.",
    "La faculté de réunir approbation du PLU et création de ZAC est conservée avec ses conditions ; aucune suppression supplémentaire n'est démontrée par rapport à la source entière.",
    "Le maintien ne vaut ni création automatique de toute ZAC ni dispense d'évaluation environnementale, de participation ou de compétence ; aucun gain budgétaire n'est calculé.",
    "Aucune charge nouvelle n'est identifiée : texte source conservé sans ajout de dossier, de justificatif ou de délai.",
    "L'effet favorable est la possibilité d'un acte unique PLU/ZAC. Elle reste ouverte aux nouvelles opérations remplissant les conditions de L. 151-7-2 et du présent article, sans réservation aux seules ZAC anciennes ; les conditions de description et de justification ne sont pas renforcées.")

xml4 = """<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant la présente réforme.</p>
<p>À compter de cette date, y compris dans les procédures en cours, l'identification préalable d'indicateurs dans le rapport de présentation ne peut être exigée sur le seul fondement du présent article. Aucun nouveau document ni aucune collecte de données de remplacement ne sont imposés sur ce fondement. Les indicateurs déjà établis peuvent être utilisés sans devoir être refaits.</p>
<p>Les analyses et bilans prévus aux articles L. 153-27 et L. 153-29 restent exigibles dans leur champ et selon leurs échéances propres. Les critères, indicateurs et modalités de suivi exigés au titre de l'évaluation environnementale, notamment par le 6° de l'article R. 151-3, demeurent applicables dans leur champ propre.</p>
<p>Cette abrogation n'impose pas de modifier les plans approuvés ou les dossiers déjà constitués. Elle ne remet pas en cause les actes antérieurs, les obligations de suivi disposant d'un autre fondement, ni les recours ouverts à leur égard ; elle ne rouvre aucun délai expiré.</p>"""
a = changed(1, xml4,
    "Réforme de fond : suppression de l'obligation réglementaire générale de prédéfinir dans le rapport les indicateurs des bilans du PLU. Hors du suivi environnemental, cette prescription de méthode ne se confond pas avec l'obligation législative d'analyser les résultats ; sa nécessité comme document initial imposé n'est pas démontrée. Les collectivités peuvent choisir leurs éléments d'évaluation au moment utile. Les analyses législatives et le suivi environnemental sont expressément conservés, sans collecte ou rapport de substitution.",
    "L. 153-27 et L. 153-29 ont été lus : analyse à six ans au plus et bilan habitat à trois ans, transmission et renouvellement de ce dernier conservent leur régime. R. 151-3, lu avec sa note du décret 2021-1345, impose déjà au 6° des critères, indicateurs et modalités de suivi environnemental : aucune dispense de cette obligation ni des exigences européennes de suivi n'est décidée. R. 151-1 conserve l'exposé des analyses existantes. L'abrogation est donc limitée à l'obligation autonome de R. 151-4 ; elle n'économise pas tous les indicateurs de tous les PLU. Les ambiguïtés d'avis et d'alinéas de L. 153-27 signalées dans le corpus ne sont pas corrigées ici. Adaptation réglementaire à coordonner avec la loi de réforme, sans date de promulgation inventée.",
    "Une obligation initiale de contenu du rapport disparaît, uniquement lorsqu'elle procède de R. 151-4 ; les bilans eux-mêmes et les indicateurs environnementaux ne sont pas supprimés. La réduction est normative, sans chiffrage de son coût.",
    "Les procédures soumises à R. 151-3 ou à une obligation autonome de suivi gardent leurs indicateurs ; aucune réduction nationale nette de complexité ou de dépense n'est établie.",
    "Aucune charge nouvelle n'est identifiée : ni déclaration, ni collecte, ni attestation ne remplace l'obligation retirée ; les travaux déjà réalisés restent utilisables.",
    repeal_scope="Obligation générale d'identifier à l'avance dans le rapport de présentation les indicateurs des analyses et bilans du PLU, à l'exclusion des exigences autonomes de suivi environnemental et des bilans législatifs eux-mêmes.")
effect(a, 'obligation_removed', 'plu-indicateurs-generaux-prealables-suppression',
    "Suppression de la prescription autonome d'indicateurs préalables dans le rapport du PLU.",
    "L'auteur du PLU doit identifier dans le rapport les indicateurs nécessaires aux analyses L153-27 et, le cas échéant, au bilan habitat L153-29, même hors suivi environnemental autonome.",
    "Aucune identification préalable exigible sur ce seul fondement ; analyses et bilan habitat, ainsi que le suivi environnemental obligatoire, conservés.",
    'legal_duty', "Collectivités compétentes pour le PLU dans le champ où R151-4 constitue le fondement autonome de l'obligation.",
    "Entrée en vigueur de la loi de réforme, procédures en cours incluses ; éléments existants réutilisables, aucun plan à refaire.",
    "Aucun rapport, registre ou collecte de remplacement ; autres suivis légalement dus inchangés.",
    "Le rapport de présentation identifie les indicateurs nécessaires à l'analyse des résultats de l'application du plan mentionnée à l'article L. 153-27 et, le cas échéant, pour le bilan de l'application des dispositions relatives à l'habitat prévue à l'article L. 153-29.",
    "À compter de cette date, y compris dans les procédures en cours, l'identification préalable d'indicateurs dans le rapport de présentation ne peut être exigée sur le seul fondement du présent article.")

retained(2,
    "Maintien intégral de l'exposé des motifs en cas de modification ou de mise en compatibilité du PLU. Il permet au public, aux propriétaires et au juge de comprendre le changement des règles opposables. La source n'impose ni un second rapport ni une seconde enquête : la suppression d'un doublon n'est pas démontrée. Réduire les contraintes du PLU ne justifie pas de rendre leurs changements inexpliqués ; aucune reformulation stylistique n'est produite.",
    "Les 1° et 2° restent dans leur ordre. L. 151-4 et R. 151-2, lus dans le corpus, maintiennent l'explication et les justifications des choix du plan dans le rapport : supprimer ici la motivation des évolutions laisserait ces obligations et fragiliserait la transparence sans suppression nette prouvée. Les procédures de participation et d'évaluation ont leurs fondements propres ; aucun délai minimal ni exemplaire supplémentaire n'est imposé par cet article. La mise en compatibilité mentionnée n'est pas assimilée à un quota SRU ou à une taxe.",
    "L'obligation de motiver les deux types de changements demeure, sans second document ajouté ni suppression démontrée par rapport à l'article officiel entier.",
    "Les formalités des procédures d'évolution du PLU ne sont pas toutes examinées dans ce seul article ; aucun gain de coût ou de délai n'est revendiqué.",
    "Aucune charge nouvelle n'est identifiée : maintien des seules justifications déjà exigées, avec les deux cas source et sans formalité supplémentaire.")

retained(3,
    "Maintien intégral : les conditions d'aménagement et leur périmètre graphique assurent l'insertion des opérations dans les espaces existants et l'identification des orientations applicables. Leur suppression ne serait pas une simple coupe de formalité mais retirerait la protection architecturale et paysagère et la lisibilité territoriale du plan. Aucun agrément, prélèvement, délai minimal ou justificatif séparé ne figure dans cet article.",
    "Renvoi à R. 151-10 conservé : il définit la partie graphique du règlement, distincte de la portée de compatibilité des OAP sous L. 152-1. R. 151-14 demeure la règle générale de visibilité des limites ; il ne constitue pas une deuxième remise de plans exigée par R. 151-6. Les dispositions ne commandent ni un quota de logements sociaux ni une autorisation supplémentaire. Les capacités de densification de L. 151-4 et L. 151-26 restent à leur champ propre, sans neutralisation des protections du site.",
    "Les conditions d'insertion et la délimitation demeurent nécessaires à la protection des lieux et à l'identification de la règle ; aucune simplification nouvelle n'est comptée.",
    "Le maintien ne valide pas chaque prescription locale concrète ni son coût ; les OAP restent soumises à leur fondement et au contrôle de légalité.",
    "Aucune charge nouvelle n'est identifiée : aucune pièce, autorisation ou échéance n'est ajoutée aux deux exigences sources.")

retained(4,
    "Maintien intégral des deux facultés : conservation, mise en valeur ou requalification du patrimoine et des paysages ; identification de zones préférentielles de renaturation. La source utilise 'peuvent', sans obliger toute collectivité à créer une zone, un projet, un tableau ou un rapport supplémentaire. Ces outils facultatifs servent les protections environnementales et patrimoniales et peuvent faciliter la requalification ; leur suppression retirerait une possibilité utile sans charge générale démontrée.",
    "R. 151-19 et R. 151-10 sont vérifiés dans le corpus. Le premier fait l'objet d'une coordination dans ce lot ; le renvoi de R. 151-7 reste pertinent pour les zones utilisant le régime national simplifié. La faculté graphique du second alinéa n'est pas transformée en obligation. L. 151-7 conserve les possibilités de renaturation et de densification. Aucune dérogation littorale ni franchise fiscale ne dépend ici d'une suppression ; aucun quota SRU n'est recréé.",
    "Les deux habilitations facultatives restent entières ; ni une obligation nationale nouvelle ni une obligation nationale supprimable n'est identifiée dans leur seule formulation.",
    "Les contraintes concrètes d'une OAP effectivement adoptée ne sont pas chiffrées ni toutes appréciées par ce maintien du cadre facultatif.",
    "Aucune charge nouvelle n'est identifiée : facultés, motifs de protection, conditions de localisation et représentation graphique restent ceux de la source.")

xml8 = """<p>Les orientations d'aménagement et de programmation des secteurs de zones urbaines ou de zones à urbaniser mentionnées au deuxième alinéa du R. 151-20 dont les conditions d'aménagement et d'équipement ne sont pas définies par des dispositions réglementaires garantissent la cohérence des projets d'aménagement et de construction avec le projet d'aménagement et de développement durables.</p>
<p>Elles portent au moins sur :</p>
<p>1° La qualité de l'insertion architecturale, urbaine et paysagère ;</p>
<p>2° Abrogé ;</p>
<p>3° La qualité environnementale et la prévention des risques ;</p>
<p>4° Abrogé ;</p>
<p>5° La desserte par les transports en commun ;</p>
<p>6° La desserte des terrains par les voies et réseaux.</p>
<p>Ces orientations d'aménagement et de programmation comportent un schéma d'aménagement qui précise les principales caractéristiques d'organisation spatiale du secteur.</p>
<p>La suppression des exigences de contenu des 2° et 4° s'applique aux orientations approuvées ou modifiées à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris dans les procédures en cours, sans imposer de nouvelle procédure ni le renouvellement des consultations déjà régulièrement accomplies. Elle ne retire pas aux orientations les facultés que leur confèrent les dispositions législatives applicables et ne supprime aucun plafonnement, dispense ou dérogation favorable en matière de stationnement. Les dispositions des plans déjà en vigueur et les prescriptions des autorisations déjà délivrées conservent leur régime et leurs voies de modification et de recours, sous réserve des suppressions de quotas et de contraintes disposant d'un fondement abrogé par cette loi. Aucune obligation de quota, de rattrapage ou de carence supprimée par cette loi ne peut être rétablie sur le fondement du présent article.</p>"""
a = changed(5, xml8,
    "Réforme de fond ciblée : suppression de deux thèmes imposés dans toutes les OAP de secteurs sans règlement détaillé, la mixité fonctionnelle et sociale et les besoins de stationnement. L'obligation nationale de traiter ces thèmes, même lorsqu'ils n'appellent aucune prescription utile, disparaît ; elle n'est remplacée ni par une déclaration ni par une étude obligatoire équivalente. Les facultés législatives pertinentes demeurent, ainsi que les garanties d'insertion, d'environnement, de risques et de desserte qui assurent une fonction essentielle en l'absence de règlement détaillé. Les numéros 2° et 4° sont laissés abrogés, sans renumérotation.",
    "Comparaison effectuée avec les six rubriques et le schéma de la source entière. L. 151-6 et L. 151-7 ont été lus : transports et déplacements restent couverts, les outils facultatifs de mixité fonctionnelle ne sont pas abrogés par cette coupe réglementaire. L. 151-15 est une habilitation législative locale distincte, non supprimée dans ce lot ; sa présence ne vaut pas rétablissement des quotas communaux ou par opération SRU supprimés. R. 151-20 conserve son deuxième alinéa et son objet dans la proposition de ce lot. La suppression de la rubrique stationnement n'abolit pas les obligations légalement applicables ni leurs plafonds, dispenses et dérogations favorables. Aucun quantum de stationnement n'est ajouté. Les modifications des plans suivent leurs procédures ordinaires ; aucune révision générale immédiate n'est imposée. L'origine historique de tout le dispositif n'est pas attribuée mécaniquement à SRU.",
    "Deux rubriques nationales obligatoires de contenu disparaissent dans les OAP sectorielles sans règlement détaillé. Cela allège le cadre de rédaction du plan, sans prouver l'abolition de quotas locaux autonomes ni de toutes les prescriptions de stationnement.",
    "Les habilitations législatives, prescriptions locales encore valides, conditions de desserte et protections essentielles subsistent ; le coût net de cette suppression de thèmes n'est pas chiffré.",
    "Aucune charge nouvelle n'est identifiée : quatre thèmes et le schéma déjà exigés sont conservés ; aucune pièce, donnée ou procédure ne remplace les deux rubriques retirées.",
    removed=["Obligation de traiter au minimum la mixité fonctionnelle et sociale dans chaque OAP sectorielle dépourvue de règlement détaillé.",
             "Obligation de traiter au minimum les besoins en matière de stationnement dans chaque OAP sectorielle dépourvue de règlement détaillé."],
    benefit="Les possibilités d'aménager un secteur sans règlement détaillé restent ouvertes pour les opérations futures. Les dispenses, plafonnements et dérogations favorables de stationnement ne sont pas supprimés avec le thème obligatoire ; les facultés législatives utiles des OAP restent accessibles sans nouveau justificatif.")
effect(a, 'obligation_removed', 'plu-oap-themes-minimaux-suppression',
    "Retrait, dans une mesure unique, des deux thèmes minimaux imposés de mixité fonctionnelle et sociale et de besoins de stationnement.",
    "Les OAP sectorielles sans règlement détaillé doivent toutes traiter au minimum la mixité fonctionnelle et sociale au 2° et les besoins de stationnement au 4°, parmi les six thèmes obligatoires.",
    "Les 2° et 4° sont abrogés : ces deux thèmes ne sont plus imposés sur ce fondement. Les quatre autres thèmes, le schéma, les habilitations législatives distinctes et les plafonnements, dispenses et dérogations favorables de stationnement demeurent.",
    'legal_duty', "Collectivités élaborant les OAP sectorielles visées au premier alinéa de R151-8.",
    "OAP approuvées ou modifiées après l'entrée en vigueur, procédures en cours incluses ; plans existants selon leurs règles d'évolution, sans survie des seuls quotas abrogés et sans réécriture automatique des autorisations antérieures.",
    "Aucune étude, rubrique, déclaration équivalente ou minimum de places de remplacement ; facultés législatives et régimes favorables maintenus.",
    "2° La mixité fonctionnelle et sociale ; 3° La qualité environnementale et la prévention des risques ; 4° Les besoins en matière de stationnement ;",
    "2° Abrogé ; 3° La qualité environnementale et la prévention des risques ; 4° Abrogé ;")
a['review_notes'] += " Incohérence préexistante relevée dans la cible législative consultée L. 151-6 : le renvoi commercial aux 1° et 2° de L. 141-5 y est signalé comme discordant avec son contenu actuel. La présente suppression de thèmes réglementaires ne corrige pas silencieusement ce renvoi législatif extérieur au lot."

retained(6,
    "Maintien intégral des trois informations de l'OAP permettant à l'approbation du PLU de créer la ZAC : schéma spatial, programme global prévisionnel et régime de la part communale ou intercommunale de la taxe d'aménagement. Elles rendent l'acte unique utilisable et fiscalement intelligible ; la mention du régime n'est ni une taxe supplémentaire ni une déclaration fiscale privée. Aucun second acte ou dossier n'est imposé par ce seul article.",
    "L. 151-7-2 et R. 151-2-1 ont été lus et conservent le mécanisme d'acte unique. Le 3° ne fixe ni taux ni assiette et ne justifie pas de retirer une exonération de taxe d'aménagement ; il permet au contraire d'identifier le régime applicable, y compris favorable. Aucune suppression générale de cette taxe n'est décidée dans la coordination fournie. Les 1°, 2° et 3° restent identiques, sans confondre programme prévisionnel et autorisation de chaque construction. Les évaluations communes de R. 151-3 demeurent distinctes.",
    "Les trois éléments utiles à la faculté PLU/ZAC sont maintenus, sans baisse fiscale ni suppression documentaire supplémentaire revendiquée.",
    "Le coût des études de ZAC et le droit fiscal de la taxe d'aménagement ne sont pas réécrits ici ; aucune exonération autonome n'est restreinte.",
    "Aucune charge nouvelle n'est identifiée : les trois rubriques restent celles de la source, sans relevé fiscal ou justificatif ajouté.",
    "La procédure commune d'approbation du PLU et de création de la ZAC demeure ouverte aux projets futurs. La mention du régime de taxe d'aménagement conserve la visibilité des exonérations et régimes applicables ; elle ne supprime ni ne resserre un avantage fiscal.")

retained(7,
    "Maintien intégral : le mot 'exclusivement' limite le règlement aux règles et servitudes nécessaires à la mise en œuvre du PADD et à la délimitation prévue par la loi. Il borne le pouvoir réglementaire local plutôt qu'il n'ajoute une autorisation ou un rapport. Supprimer cette limite pourrait élargir les contraintes opposables ; aucun doublon de dépôt ni charge accessoire retirable n'est établi.",
    "Renvois L. 151-8 et L. 151-9 lus et conservés : fondement des règles et délimitation des zones. Le diagnostic et les enveloppes de densification retenus à L. 151-4 et L. 151-26 ne sont pas transformés ici en une nouvelle pièce du règlement. L'article ne rétablit pas les obligations SRU supprimées ; les fondements autonomes environnementaux, patrimoniaux et de sécurité restent à leur champ propre.",
    "Le champ limitatif du règlement demeure ; aucune réduction supplémentaire de prélèvement ou d'obligation n'est démontrée par une modification de cet article.",
    "La nécessité de chaque règle locale doit être appréciée séparément ; le maintien ne prouve pas que tous les PLU sont déjà simplifiés.",
    "Aucune charge nouvelle n'est identifiée : même limite du contenu réglementaire, mêmes renvois et aucune pièce supplémentaire.")

retained(8,
    "Maintien intégral des deux composantes du règlement et de la limitation de leur opposabilité. Le second alinéa protège le demandeur contre l'opposition d'autres documents au titre de la conformité ; l'abroger pourrait rendre les obligations moins prévisibles. Les documents écrits et graphiques remplissent des fonctions complémentaires, sans exigence source de copies multiples ni de dossier parallèle.",
    "L. 152-1 a été lu : conformité au règlement et à ses documents graphiques, compatibilité distincte avec les OAP. Les R. 151-6, R. 151-7, R. 151-11 et R. 151-14 utilisent ce support graphique ; leur maintien ou leur modification dans ce lot ne change pas les deux degrés d'opposabilité. La suppression de la mention écrite redondante proposée à R. 151-11 ne confère aucune opposabilité à un simple document illustratif du rapport.",
    "La protection limitant les supports opposables est conservée ; aucune nouvelle simplification ni fusion de documents existants n'est comptée.",
    "L'article n'allège pas à lui seul les pièces d'une demande de permis et ne fixe aucun délai d'instruction ; ces régimes restent distincts.",
    "Aucune charge nouvelle n'est identifiée : mêmes composantes et même protection d'opposabilité que dans la source.")

xml11 = """<p>Les règles peuvent être écrites et graphiques.</p>
<p>Lorsqu'une règle fait exclusivement l'objet d'une représentation dans un document graphique, sa mention dans la partie écrite du règlement n'est pas exigée.</p>
<p>Tout autre élément graphique ou figuratif compris dans la partie écrite du document est réputé constituer une illustration dépourvue de caractère contraignant, à moins qu'il en soit disposé autrement par une mention expresse.</p>
<p>La dispense de mention écrite s'applique aux dispositions réglementaires du plan approuvées ou modifiées à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris dans les procédures en cours. Elle ne dispense pas d'inclure la règle dans la partie graphique opposable et publiée du règlement. Elle ne rend pas opposable une illustration ni une règle antérieurement dépourvue d'opposabilité. Les dispositions des plans et les autorisations antérieurs conservent leur régime et leurs voies de modification et de recours ; aucune modification du plan n'est imposée du seul fait de cette dispense.</p>"""
a = changed(9, xml11,
    "Réforme de fond limitée : suppression de l'obligation de doubler toute règle exclusivement graphique par une mention expresse dans la partie écrite. La règle publiée dans la partie graphique suffit, sans texte de signalement supplémentaire. Le choix entre écrit et graphique et la présomption non contraignante des illustrations sont maintenus mot pour mot. La dispense ne transforme pas rétroactivement une illustration ou une ancienne règle inopposable en nouvelle contrainte.",
    "R. 151-10, R. 151-14 et L. 152-1 ont été lus : la règle doit toujours appartenir au règlement graphique, dont les limites sont visibles et dont l'opposabilité reste celle de la conformité. Les exigences légales de publication et d'accès ne sont pas supprimées ; aucune règle cachée n'est créée. La dispense porte uniquement sur la seconde mention écrite, non sur le contenu graphique, sa publication ou la mention expresse encore nécessaire pour conférer une portée contraignante à une illustration de la partie écrite. Transition limitée aux dispositions approuvées ou modifiées après réforme pour ne pas rétablir une contrainte auparavant inopposable. Aucun dépôt, système numérique ou lexique de remplacement.",
    "Une obligation de signalement écrit d'une règle déjà graphique et publiée disparaît pour les dispositions nouvelles ou modifiées. Le contenu de la règle et la protection des illustrations demeurent ; l'allègement porte sur la rédaction du règlement.",
    "Aucun coût net ni nombre de mentions évitées n'est chiffré ; les règles anciennes inopposables ne deviennent pas opposables par cette dispense.",
    "Aucune charge nouvelle n'est identifiée : publication graphique et statut des illustrations étaient déjà applicables ; aucune nouvelle légende, attestation ou table de correspondance n'est imposée.",
    removed=["Obligation de mentionner expressément dans la partie écrite du règlement toute règle faisant exclusivement l'objet d'une représentation graphique."])
effect(a, 'obligation_removed', 'plu-regle-graphique-fin-mention-ecrite',
    "Suppression du signalement écrit obligatoire d'une règle exclusivement graphique.",
    "Pour chaque règle exclusivement graphique, le règlement écrit doit en porter une mention expresse, en plus de la représentation graphique.",
    "La représentation dans la partie graphique opposable et publiée suffit ; la mention écrite de signalement n'est plus imposée pour les dispositions nouvelles ou modifiées.",
    'legal_duty', "Collectivités compétentes rédigeant ou faisant évoluer les règles graphiques du PLU.",
    "Approbations ou modifications après entrée en vigueur, procédures en cours incluses ; absence de validation rétroactive de règles inopposables.",
    "Aucun tableau, légende, déclaration ou double support de remplacement ; accès et publication conservés.",
    "Lorsqu'une règle fait exclusivement l'objet d'une représentation dans un document graphique, la partie écrite du règlement le mentionne expressément.",
    "Lorsqu'une règle fait exclusivement l'objet d'une représentation dans un document graphique, sa mention dans la partie écrite du règlement n'est pas exigée.")

retained(10,
    "Maintien intégral de la faculté de définir une règle par un résultat qualitatif précis et vérifiable. Elle permet d'éviter des prescriptions techniques détaillées sans abandonner la possibilité de vérifier le respect de la règle. Précision et vérifiabilité sont des garanties de prévisibilité et de contrôle ; les enlever rendrait l'obligation plus discrétionnaire. Aucun agrément, justificatif distinct ou délai n'est demandé par cet article.",
    "Le caractère facultatif ('peuvent') reste entier. L'article ne crée pas un dossier de preuve universel du résultat : toute demande de pièce relève des règles de procédure qui lui sont propres. Les mesures de densification de L. 151-26 et les dérogations de L. 152-3 et suivants conservent leurs fondements. Aucune substitution stylistique ni réduction prétendue d'une prescription locale non identifiée.",
    "La souplesse du résultat qualitatif reste disponible, avec les mêmes garanties ; il s'agit d'un maintien utile et non d'une nouvelle suppression de contrainte.",
    "L'article ne démontre pas que toutes les prescriptions de moyens locales sont retirées ni qu'une économie de conformité est quantifiée.",
    "Aucune charge nouvelle n'est identifiée : aucune certification, attestation ou méthode de preuve obligatoire n'est ajoutée.",
    "La possibilité de règles de résultat, plus souples que des prescriptions de moyens, reste ouverte à tous les futurs PLU et à leurs évolutions. La précision et la vérifiabilité ne sont pas renforcées et ne deviennent pas une certification nouvelle.")

retained(11,
    "Maintien intégral des règles alternatives tenant compte des conditions locales et de leur non-substitution aux adaptations mineures et aux dérogations légales. Ces dispositions protègent des possibilités de construire ; les abroger supprimerait des allègements alors que les règles générales du PLU subsistent. Les deux phrases ne créent ni taxe ni nouvelle autorisation distincte des procédures légales existantes.",
    "L. 152-3, L. 152-4, L. 152-5 et L. 152-6 ont été lus intégralement dans le corpus. La coordination déjà proposée de L. 152-6 retire la condition liée à la carence pour le 3° ; le présent maintien ne rétablit pas cette condition. Les renvois restent pertinents pour les adaptations et les dérogations de leur champ ; les autres dérogations légales, y compris littorales, ne sont ni fermées ni remplacées par les règles alternatives locales. Aucun renvoi à une norme abrogée n'a été identifié dans cette plage. Les dispositifs plus récents disposant d'un fondement autonome ne sont pas réputés abrogés par le caractère non exhaustif de la phrase.",
    "Les trois voies favorables, règles alternatives, adaptations mineures et dérogations légales, sont conservées sans gain nouveau attribué à leur simple maintien.",
    "Les conditions et décisions propres aux dérogations légales restent applicables ; aucun droit automatique général de déroger ni solde global de contraintes n'est affirmé.",
    "Aucune charge nouvelle n'est identifiée : même faculté locale et même protection contre la substitution aux allègements légaux, sans justificatif ajouté.",
    "Chaque voie favorable est conservée pour les futures opérations éligibles, avec ses conditions propres, sans limitation aux droits acquis : règles alternatives locales du premier alinéa ; adaptations mineures de L. 152-3 ; reconstruction après catastrophe, restauration ou reconstruction patrimoniale et accessibilité de L. 152-4 ; isolation des façades et toitures, protection solaire, ombrières, production renouvelable, réseaux de chaleur ou de froid efficaces et revêtements réflectifs de L. 152-5. Le renvoi de plage protège aussi les dérogations intermédiaires de hauteur et d'aspect pour la végétalisation de L. 152-5-1, de hauteur pour l'exemplarité environnementale de L. 152-5-2 et de hauteur pour les projets d'intérêt national majeur de L. 152-5-3. À L. 152-6 demeurent le dépassement de hauteur jusqu'au faîtage contigu, la surélévation, la transformation en logements avec majoration de gabarit, les dispenses de stationnement près des transports ou lors de travaux sur logements existants, la dérogation de retrait, le supplément de gabarit pour espaces extérieurs, la dispense de stationnement en réhabilitation de centre-ville et la dérogation supplémentaire d'intérêt architectural. Le maintien de R. 151-13 ne rétablit pas l'ancienne exclusion pour carence retirée du 3° de L. 152-6. Aucune de ces voies n'est remplacée par la seule règle alternative locale, et aucun nouveau dossier n'est exigé.")

answers[-1]['review_notes'] += " Les articles intermédiaires L. 152-5-1, L. 152-5-2 et L. 152-5-3 ont également été lus entièrement : végétalisation, exemplarité environnementale et intérêt national majeur restent couverts par la plage maintenue. Incohérence structurelle préexistante signalée à L. 152-3 : la 'présente sous-section' de son 2° n'est pas identifiée comme telle dans le classement du corpus ; sa clarification relève d'une coordination de ce texte, sans changer le renvoi actif de R. 151-13 ni réduire les dérogations."

retained(12,
    "Maintien intégral de l'obligation de faire apparaître les limites des zones et des autres espaces identifiés par le PLU. Elle permet au propriétaire et au service instructeur de savoir quelle règle s'applique et protège contre des périmètres indéterminés. Ce n'est pas une demande de second plan au pétitionnaire ; la source ne prévoit aucune collecte, déclaration ou pièce justificative séparée retirable.",
    "Articulation vérifiée avec R. 151-10, R. 151-17 et L. 151-9 : les zones ont leur fondement légal, les graphiques leur support et la présente règle leur visibilité. Les périmètres favorables ou dérogatoires ne sont pas supprimés. La dispense de mention écrite à R. 151-11 conserve cette délimitation graphique, sans multiplication des documents ni modification implicite de l'opposabilité.",
    "La délimitation visible des espaces reste nécessaire à l'application prévisible du PLU ; aucune seconde obligation graphique supprimée n'est démontrée.",
    "Le maintien ne justifie pas chaque périmètre de fond ; il ne calcule ni coût cartographique ni économie globale.",
    "Aucune charge nouvelle n'est identifiée : les limites déjà requises restent sur les documents existants, sans nouvelle carte ni donnée supplémentaire.")

retained(13,
    "Maintien intégral de l'emploi des définitions nationales existantes à la date de prescription du PLU ou de sa révision. La règle évite des sens divergents pour un même terme et fige une référence temporelle prévisible ; elle n'oblige pas à produire un lexique local ni à suivre rétroactivement chaque changement national. Aucun dépôt ou agrément ne peut être retiré de cette seule disposition.",
    "R. 111-1 a été lu : son dernier alinéa prévoit le lexique national par arrêté ; la réforme distincte des règles de distance n'affecte pas cette habilitation. L. 153-31 demeure la référence de la révision. L'arrêté portant lexique et son contenu intégral ne sont pas joints à ce lot : aucune définition nationale absente n'est inventée ou prétendue réécrite. R. 151-16 maintient la faculté de préciser et compléter sans contredire les définitions requises. La date de prescription, et non la date d'approbation ou la date de la réforme future, reste le repère.",
    "L'unification terminologique et sa référence temporelle demeurent ; aucune charge supprimée ni nouvelle simplification n'est revendiquée.",
    "La pertinence de chaque définition de l'arrêté national n'est pas évaluée faute de son texte joint ; cela ne supprime aucun article du lot ni ne modifie ses renvois.",
    "Aucune charge nouvelle n'est identifiée : même usage des définitions existantes, aucun inventaire ou lexique local obligatoire ajouté.")

retained(14,
    "Maintien intégral de la simple faculté de préciser ou compléter les définitions nationales utiles au règlement. Elle peut réduire les ambiguïtés locales sans imposer un glossaire à chaque plan. La supprimer fermerait une souplesse et pourrait augmenter l'incertitude des demandeurs ; aucun document annuel, pièce autonome ou autorisation ne résulte de la source.",
    "Le renvoi contextuel 'ces définitions' vise celles de R. 151-15, qui reste intégralement maintenu. La faculté de complément n'autorise pas à détourner les définitions nationales applicables ni à créer des formalités hors du champ du règlement. R. 111-1 conserve l'habilitation du lexique national. Aucune nouvelle définition n'est rédigée dans ce lot et aucun régime favorable n'est fermé pour l'avenir.",
    "La faculté de clarification reste intacte, sans obligation supplémentaire ou réduction nouvelle démontrée par rapport à la source.",
    "Les définitions locales concrètement adoptées ne font pas l'objet d'un audit individuel par ce maintien ; aucun gain national n'est calculé.",
    "Aucune charge nouvelle n'est identifiée : le complément demeure facultatif et n'est assorti d'aucun registre, visa ou délai ajouté.")

retained(15,
    "Maintien intégral du zonage graphique U, AU, agricole, naturel et forestier et de la détermination des règles par zone. Cette structure sert l'identification des droits à construire et la protection des terres et milieux ; la supprimer ne serait pas retirer un doublon documentaire mais rendre incertain le champ du règlement. Aucun plan distinct ou exemplaire supplémentaire n'est exigé.",
    "L. 151-9 a été lu : fondement légal de la délimitation et des destinations. R. 151-14 assure la visibilité des limites, et R. 151-18 à R. 151-24 définissent les catégories examinées dans ce lot. Les règles alternatives de R. 151-13, le régime simplifié de R. 151-19 et les possibilités de R. 151-23 restent utilisables ; la présente règle ne les écrase pas. Aucun quota SRU n'est créé et aucune interdiction générale nouvelle de construire n'est ajoutée.",
    "La structure de zonage nécessaire à la lecture des droits demeure, sans requalification en simplification ni abolition de règle de fond.",
    "Ce maintien ne démontre pas que le classement de chaque parcelle est nécessaire ni qu'une baisse globale des contraintes locales est acquise.",
    "Aucune charge nouvelle n'est identifiée : mêmes catégories et mêmes supports graphiques, sans formalité de classement individuelle supplémentaire.")

retained(16,
    "Maintien intégral des deux voies de classement en zone urbaine : secteurs déjà urbanisés et secteurs pouvant être suffisamment desservis par des équipements existants ou en cours de réalisation. Le texte ouvre le classement sans exiger que tous les équipements soient déjà achevés. La capacité de desserte protège l'eau, l'accès et la salubrité ; aucun agrément ou justificatif séparé n'est imposé ici.",
    "La qualification 'peuvent' reste une habilitation, non un reclassement automatique de toute parcelle. Les deux catégories de secteurs ne sont pas transformées en conditions cumulatives. Articulation maintenue avec R. 151-17 et le diagnostic de L. 151-4 ; aucune certification de réseau ou étude supplémentaire n'est créée dans le présent article. Les enveloppes de densification de L. 151-26 conservent leur transition propre.",
    "Les deux possibilités de classement favorable sont conservées, y compris en présence d'équipements en cours ; aucune extension ou réduction supplémentaire n'est comptée.",
    "La capacité des réseaux n'est pas présumée partout suffisante et aucun droit individuel automatique au reclassement n'est annoncé.",
    "Aucune charge nouvelle n'est identifiée : mêmes critères alternatifs, aucun document de preuve ou délai supplémentaire ajouté.",
    "Le classement U peut toujours bénéficier aux secteurs déjà urbanisés et aux secteurs suffisamment desservis par des équipements en cours de réalisation, pour les futures décisions de planification aussi. Aucune exigence d'achèvement préalable ni nouvelle condition cumulative n'est introduite.")

xml19 = """<p>Une ou plusieurs zones urbaines d'un plan local d'urbanisme peuvent être réglementées en y appliquant l'ensemble des articles R. 111-3 et R. 111-5 à R. 111-13, sans y ajouter d'autres règles.</p>
<p>Il est alors fait renvoi à l'ensemble de ces articles en mentionnant leurs références dans le règlement de la ou des zones concernées.</p>
<p>Cette faculté est ouverte aux plans locaux d'urbanisme communaux comme intercommunaux pour les délibérations approuvant leur élaboration ou leur évolution à compter de l'entrée en vigueur de la loi portant la présente réforme. Elle n'impose pas de modifier un plan en vigueur.</p>
<p>Les renvois des plans en vigueur aux articles R. 111-15 à R. 111-18 et R. 111-28 à R. 111-30 ne peuvent maintenir ni rétablir les règles abrogées pour les décisions nouvelles, dans le champ et selon les dispositions transitoires de leurs abrogations. Les prescriptions locales distinctes disposant d'un fondement autonome, les autorisations antérieures et leurs voies de modification et de recours conservent leur régime.</p>"""
a = changed(17, xml19,
    "Réforme de fond favorable : ouverture aux PLU communaux, et non plus seulement intercommunaux, de l'option consistant à appliquer un ensemble de règles nationales sans règles locales supplémentaires dans les zones urbaines choisies. Aucune fonction essentielle ne justifie que cette option soit interdite à la seule échelle communale. Coordination distincte : retrait des renvois à R. 111-15 à R. 111-18 et R. 111-28 à R. 111-30 dont les propositions d'abrogation figurent déjà au corpus ; ces retraits ne sont pas comptés comme de nouvelles suppressions de distance ou d'aspect. Les règles nationales restantes et la désignation des références restent entières.",
    "Lecture intégrale dans le corpus de R. 111-3, R. 111-5 à R. 111-13, R. 111-15 à R. 111-18 et R. 111-28 à R. 111-30, avec leurs propositions. Les protections contre nuisances graves, les accès et l'incendie, l'eau et l'assainissement subsistent dans les cibles restantes, sous leurs coordinations propres. Les suppressions déjà proposées de distance interne, retraits géométriques et prescriptions esthétiques sont dédupliquées sous leurs measure_id existantes. R. 111-1 conserve au corpus des plages partiellement dépassées par les dernières abrogations ; sa coordination complète est nécessaire hors du présent lot, sans modifier le lexique national ni prétendre cette coordination déjà réalisée. R. 151-2 5° et R. 151-7 continuent à viser un mécanisme actif. L. 151-9 ne réserve pas le zonage aux PLUi. Les procédures ordinaires d'évolution du plan et les règles nationales applicables indépendamment de cette option subsistent. Les anciennes prescriptions locales autonomes ne sont pas automatiquement effacées ; aucun renvoi ne fait revivre les normes nationales abrogées.",
    "L'interdiction d'utiliser le régime national simplifié dans un PLU communal disparaît. Le reste est une coordination de trois mesures déjà proposées, sans second gain de distance ou d'aspect attribué au seul retrait des références.",
    "L'option reste un choix du plan, sans droit individuel de remplacer son règlement ; les abrogations et leurs transitions doivent entrer en vigueur de façon coordonnée, notamment avec R111-1. Coût net global non établi.",
    "Aucune charge nouvelle n'est identifiée : mêmes règles nationales restantes et même mention des références ; aucun dossier, agrément ou déclaration ne conditionne l'extension aux communes.",
    removed=["Restriction de l'option de règlement national simplifié aux seuls plans locaux d'urbanisme intercommunaux, à l'exclusion des plans communaux.",
             "Renvois aux règles abrogées de distance et de retrait de R. 111-15 à R. 111-18, sans maintien de leurs effets pour les décisions nouvelles.",
             "Renvois aux prescriptions esthétiques abrogées de R. 111-28 à R. 111-30, sans rétablissement par les plans qui les citent."],
    benefit="L'option favorable d'un régime national sans règles locales supplémentaires est conservée pour les PLUi et étendue aux PLU communaux pour leurs évolutions futures. Les dérogations sanitaires des règles nationales restantes demeurent dans leur champ propre ; aucun ancien bénéficiaire ne perd l'option et aucun renvoi ne rétablit les prescriptions nationales abrogées.")
effect(a, 'relief_extended', 'plu-communal-option-reglement-national',
    "Extension aux PLU communaux de l'option nationale simplifiée de zonage urbain.",
    "Option réservée aux zones urbaines d'un PLU intercommunal, sans ajout d'autres règles dans les zones choisies ; PLU communal exclu.",
    "Même option pour PLU communal ou intercommunal ; application des seules références nationales encore actives énumérées au premier alinéa.",
    'regime', "Communes compétentes pour un PLU communal et porteurs de projets dans les zones U où cette option est adoptée.",
    "Délibérations approuvant l'élaboration ou l'évolution après entrée en vigueur ; aucune évolution immédiate d'un plan existant imposée.",
    "Pas de déclaration ou d'autorisation de remplacement ; procédure ordinaire d'évolution du plan inchangée.",
    "Une ou plusieurs zones urbaines d'un plan local d'urbanisme intercommunal peuvent être réglementées en y appliquant l'ensemble des articles R. 111-3, R. 111-5 à R. 111-13, R. 111-15 à R. 111-18 et R. 111-28 à R. 111-30, sans y ajouter d'autres règles.",
    "Cette faculté est ouverte aux plans locaux d'urbanisme communaux comme intercommunaux pour les délibérations approuvant leur élaboration ou leur évolution à compter de l'entrée en vigueur de la loi portant la présente réforme.")
for measure, description, before in [
    ('urbanisme-distance-interne-trois-metres-suppression', "Coordination du renvoi à la distance interne abrogée de R111-15.", "L'option fait référence à R111-15 dans la plage R111-15 à R111-18."),
    ('urbanisme-retraits-geometriques-rnu-suppression', "Coordination des renvois aux retraits géométriques abrogés R111-16 à R111-18.", "L'option fait référence à R111-16, R111-17 et R111-18 dans la même plage."),
    ('rnu-prescriptions-esthetiques-redondantes', "Coordination des renvois aux prescriptions esthétiques abrogées R111-28 à R111-30.", "L'option impose aussi les références R111-28 à R111-30.")]:
    effect(a, 'coordination', measure, description, before,
        "Les références abrogées sont retirées et les renvois existants ne peuvent rétablir leur contrainte ; ce retrait n'est pas une seconde abolition.",
        'other', "Zones urbaines utilisant le mécanisme de R151-19 et projets soumis aux seules références concernées.",
        "Coordination avec les abrogations du corpus, sous leurs transitions propres et avec maintien des anciens titres.",
        "Aucune charge ni formalité ajoutée par la coordination ; prescriptions locales autonomes distinctes réservées.",
        "R. 111-15 à R. 111-18 et R. 111-28 à R. 111-30",
        "Les renvois des plans en vigueur aux articles R. 111-15 à R. 111-18 et R. 111-28 à R. 111-30 ne peuvent maintenir ni rétablir les règles abrogées pour les décisions nouvelles, dans le champ et selon les dispositions transitoires de leurs abrogations.")

xml20 = """<p>Les zones à urbaniser sont dites " zones AU ". Peuvent être classés en zone à urbaniser les secteurs destinés à être ouverts à l'urbanisation.</p>
<p>Lorsque les voies ouvertes au public et les réseaux d'eau, d'électricité et, le cas échéant, d'assainissement existant à la périphérie immédiate d'une zone AU ont une capacité suffisante pour desservir les constructions à implanter dans l'ensemble de cette zone ou dans une partie de celle-ci délimitée par les orientations d'aménagement et de programmation et que ces orientations et, le cas échéant, le règlement en ont défini les conditions d'aménagement et d'équipement, les constructions sont autorisées dans la zone ou dans la partie ainsi desservie soit lors de la réalisation d'une opération d'aménagement d'ensemble, soit au fur et à mesure de la réalisation des équipements internes à la zone ou à cette partie prévus par les orientations d'aménagement et de programmation et, le cas échéant, le règlement.</p>
<p>Pour les parties de la zone AU dans lesquelles les voies ouvertes au public et les réseaux d'eau, d'électricité et, le cas échéant, d'assainissement existant à la périphérie immédiate de la zone n'ont pas une capacité suffisante pour desservir les constructions à implanter, l'ouverture à l'urbanisation reste subordonnée à une modification ou à une révision du plan local d'urbanisme comportant notamment les orientations d'aménagement et de programmation de ces parties.</p>
<p>La possibilité d'ouvrir à l'urbanisation une partie suffisamment desservie s'applique aux décisions prises à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris sur les demandes en cours, sans nouveau dépôt ni reprise des délais. Elle ne dispense pas de l'évolution du plan nécessaire pour délimiter cette partie et définir ses conditions d'aménagement et d'équipement lorsque le plan en vigueur ne le fait pas déjà ; elle n'impose pas de faire évoluer un plan existant. L'insuffisance de desserte d'une autre partie de la zone ne peut, à elle seule, imposer l'équipement préalable de l'ensemble de la zone ou une nouvelle évolution du plan pour la partie remplissant les conditions du deuxième alinéa. Les conditions de sécurité, de salubrité, d'environnement et de patrimoine demeurent applicables, ainsi que la dérogation de l'article R. 151-20-1 dans son champ propre. Les autorisations antérieures et leurs voies de modification et de recours sont préservées ; aucun refus définitif ni délai de recours expiré n'est rouvert.</p>"""
a = changed(18, xml20,
    "Réforme de fond : l'ouverture d'une partie cohérente de zone AU déjà délimitée par les OAP et suffisamment desservie n'est plus subordonnée à la capacité des voies et réseaux pour toute la zone. L'obstacle d'équipement préalable à l'échelle entière est retiré ; les parties non desservies restent soumises à l'évolution du plan. Les deux modalités d'opération d'ensemble ou de réalisation progressive des équipements internes sont conservées. La définition AU, les voies et les réseaux d'eau, d'électricité et, le cas échéant, d'assainissement, le rôle des OAP et du règlement et les protections essentielles ne sont pas abandonnés. Aucun permis autonome ou déclaration de remplacement n'est créé.",
    "Les trois premiers alinéas gardent leur objet et leur ordre. R. 151-8 continue de viser le deuxième alinéa ; R. 151-20-1 conserve son exception nucléaire, plus large que l'option de desserte partielle, sans condition nouvelle. L. 151-6-1 et L. 151-7, lus dans le corpus, conservent la planification et les facultés de schéma ; L. 151-4 et L. 151-26 gardent diagnostic des capacités et transition des secteurs desservis. Le plan doit déjà permettre la partie d'opération ; une zone entièrement fermée n'est pas rendue automatiquement constructible sans la procédure d'évolution nécessaire. La délimitation dans les OAP sert à rattacher la capacité des réseaux à un périmètre identifiable, et non à imposer un dossier technique supplémentaire. Les choix de révision ou modification et les évaluations/participations de leur régime restent à coordonner selon le contenu concret de l'évolution ; aucune dispense supérieure présumée. Aucun coût public de réseaux ni solde national n'est chiffré.",
    "La condition de capacité périphérique à l'échelle de toute la zone AU est réduite à la partie autorisée et planifiée lorsque celle-ci suffit. Il s'agit d'une extension des possibilités d'urbaniser, non d'une suppression de l'exigence de desserte réelle ni d'une abolition générale de l'évolution des PLU.",
    "Les parties sans capacité suffisante et celles que le plan n'a pas encore ouvertes ne bénéficient pas d'une ouverture automatique ; les coûts de réseaux et les effets publics nets ne sont pas établis.",
    "Aucune charge nouvelle obligatoire n'est identifiée : la voie entière existante reste utilisable ; l'option partielle s'appuie sur les OAP et règles de desserte existantes, sans nouvelle étude, attestation, autorisation ou déclaration autonome. La délimitation de la seule partie bénéficiaire ne remplace pas une exigence moins coûteuse déjà acquise.",
    removed=["Condition de capacité des voies et réseaux pour l'ensemble de la zone AU lorsque seule une partie planifiée et suffisamment desservie est ouverte à l'urbanisation.",
             "Obligation de faire à nouveau évoluer le PLU pour une partie déjà planifiée et suffisamment desservie au seul motif de l'insuffisance des réseaux d'une autre partie de la zone."],
    benefit="Les deux voies favorables déjà prévues, opération d'aménagement d'ensemble et construction au fur et à mesure des équipements internes, demeurent pour les zones entières comme pour leurs parties éligibles. La dérogation nucléaire de R. 151-20-1 reste distincte et applicable aux futures opérations de son champ, sans restriction ni preuve supplémentaire issue de la nouvelle option.")
effect(a, 'relief_extended', 'urbanisme-au-ouverture-parties-desservies',
    "Possibilité d'ouvrir une partie AU planifiée sans disposer d'une capacité périphérique suffisante pour toute la zone.",
    "Dans la règle générale, les voies et réseaux périphériques doivent pouvoir desservir les constructions de l'ensemble de la zone AU ; à défaut, l'ouverture relève d'une modification ou révision du plan.",
    "Capacité suffisante pour la partie délimitée et planifiée par les OAP : cette partie peut être autorisée, sans attendre la capacité pour le reste ; parties non desservies sous le régime d'évolution du plan.",
    'regime', "Collectivités et porteurs de projets dans les parties de zones AU suffisamment desservies et déjà couvertes par des conditions d'aménagement et d'équipement adéquates.",
    "Décisions après entrée en vigueur, demandes en cours incluses ; adaptation préalable du plan seulement si son contenu actuel ne permet pas la partie ; anciens titres préservés.",
    "Aucun dépôt autonome ajouté ; la desserte, les OAP et leurs procédures restent nécessaires dans leur champ, sans obligation d'équiper toute la zone avant la partie bénéficiaire.",
    "ont une capacité suffisante pour desservir les constructions à implanter dans l'ensemble de cette zone",
    "ont une capacité suffisante pour desservir les constructions à implanter dans l'ensemble de cette zone ou dans une partie de celle-ci délimitée par les orientations d'aménagement et de programmation")

retained(19,
    "Maintien intégral de la dérogation aux conditions de voies et réseaux suffisants en périphérie immédiate des zones AU dans les OIN destinées à une installation nucléaire de base. Elle est expressément favorable et doit rester ouverte aux constructions, travaux, installations et aménagements futurs nécessaires à sa mise en œuvre. La réforme partielle de R. 151-20 ne remplace pas ni ne réduit cette dérogation par une simple possibilité de desserte par partie.",
    "Source et note du décret 2021-851 du 29 juin 2021 lues entièrement. La note distingue les documents déjà approuvés et les procédures d'élaboration/révision non arrêtées, puis les mises en compatibilité dont l'examen conjoint n'a pas eu lieu avant le premier jour du mois suivant la publication : ces champs historiques restent appliqués sans inventer une date d'entrée en vigueur nouvelle. Renvoi R. 151-20 cohérent avec la proposition du lot ; L. 593-2 du code de l'environnement reste le renvoi de définition fourni, dont le texte intégral extérieur n'est pas dans le corpus des cinq codes consulté. Aucune dérogation aux autorisations nucléaires, à la sûreté ou aux évaluations environnementales n'est déduite de la seule dispense de réseaux périphériques.",
    "L'avantage nucléaire de desserte AU est conservé à l'identique avec son champ territorial et matériel, sans réduction nouvelle ni fermeture des opérations futures.",
    "La dérogation ne dispense pas du droit de la sûreté nucléaire ou des autres autorisations ; la définition externe L593-2 n'est pas présentée comme réécrite ou vérifiée intégralement ici.",
    "Aucune charge nouvelle n'est identifiée : aucun réseau préalable, agrément, certificat ou restriction de date ne s'ajoute aux conditions de la source.",
    "L'avantage possible est précisément la non-application des conditions de capacité suffisante des voies et réseaux en périphérie immédiate des zones AU pour les constructions, travaux, installations et aménagements nécessaires à une installation nucléaire de base dans l'OIN visée. Il est maintenu intégralement, pour les nouvelles opérations éligibles aussi, dans les champs temporels de la note de 2021 ; la nouvelle option partielle de R. 151-20 ne le conditionne pas et ne le remplace pas.")

xml21 = """<p>Dans les zones U et AU, le règlement peut, à l'intérieur d'une même zone, délimiter des secteurs dans lesquels les projets de constructions situés sur plusieurs unités foncières contiguës qui font l'objet d'une demande de permis de construire ou d'aménager conjointe sont appréciés comme un projet d'ensemble et auxquels il est fait application de règles alternatives édictées à leur bénéfice par le plan local d'urbanisme.</p>
<p>Ces règles alternatives définissent notamment les obligations faites à ces projets lorsque le règlement prévoit sur ces secteurs, en application de l'article L. 151-15, qu'un pourcentage des programmes de logements doit être affecté à des catégories de logement en précisant ce pourcentage et les catégories prévues.</p>
<p>Dans le cas d'un lotissement ou dans celui de la construction, sur une unité foncière ou sur plusieurs unités foncières contiguës, de plusieurs bâtiments dont le terrain d'assiette doit faire l'objet d'une division en propriété ou en jouissance, l'ensemble du projet est apprécié au regard de la totalité des règles édictées par le plan local d'urbanisme. Le règlement de ce plan ne peut s'opposer à cette appréciation d'ensemble.</p>
<p>La suppression de la faculté d'opposition prévue au troisième alinéa s'applique aux décisions prises à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris sur les demandes en cours, sans nouveau dépôt ni reprise des délais. Les clauses d'opposition des plans en vigueur ne peuvent plus être opposées à ces décisions. Les prescriptions des autorisations régulièrement délivrées avant cette date conservent leur régime et leurs voies de modification et de recours ; aucun refus définitif ni délai de recours expiré n'est rouvert.</p>
<p>Les règles distinctes de sécurité, de salubrité, de protection de l'environnement et du patrimoine ainsi que les droits des tiers demeurent applicables dans leur champ propre. Le deuxième alinéa ne peut rétablir aucun quota, rattrapage, prélèvement ou régime de carence supprimé par la loi portant la présente réforme ; il ne concerne que les règles locales conservant un fondement légal autonome.</p>"""
a = changed(20, xml21,
    "Réforme de fond : suppression du pouvoir du règlement du PLU de s'opposer à l'appréciation globale des lotissements et ensembles de bâtiments destinés à une division. Le bénéfice existant de l'examen du projet dans son ensemble devient garanti dans le cas prévu au troisième alinéa, au lieu de pouvoir être écarté par une clause locale. Les deux premiers alinéas sont maintenus intégralement : ils règlent un mécanisme différent de demande conjointe et de règles alternatives favorables. Les conditions d'unités contiguës, de division et la totalité des règles du PLU restent préservées ; aucune autorisation ou déclaration de substitution n'est créée.",
    "L. 151-15 et L. 152-1 ont été lus : le premier conserve au corpus une habilitation locale autonome de catégories de logements, le second distingue conformité et compatibilité. Le renvoi du deuxième alinéa n'est donc pas orphelin et n'est pas supprimé par simple assimilation à SRU ; la réserve finale interdit de rétablir par ce renvoi un quota, rattrapage ou régime de carence supprimé. L'allègement est limité au veto contre l'appréciation d'ensemble du troisième alinéa, et non à une dispense de toutes les règles de fond ni à un nouveau droit de déroger parcelle par parcelle. Les règles de sécurité, salubrité, environnement, patrimoine et droits des tiers restent dans leur champ propre. Aucune autorisation ancienne n'est réécrite automatiquement. Les éventuelles règles d'exécution des permis valant division doivent rester cohérentes avec l'appréciation d'ensemble, sans être présentées comme toutes modifiées ici.",
    "Le veto local contre l'appréciation globale disparaît pour les opérations définies au troisième alinéa. C'est un élargissement réel d'un mécanisme favorable existant ; aucune suppression de quota local autonome ni de permis n'est comptée.",
    "Le bénéfice concerne les seuls lotissements et ensembles avec division décrits ; les deux premiers alinéas ont leur champ distinct et la totalité des règles pertinentes demeure. Aucun coût net national n'est établi.",
    "Aucune charge nouvelle n'est identifiée : les mêmes opérations sont appréciées globalement sans clause locale d'opposition ; ni dossier conjoint nouveau pour le troisième alinéa, ni attestation ou donnée supplémentaire n'est ajouté.",
    removed=["Faculté du règlement du PLU de s'opposer à l'appréciation d'ensemble d'un lotissement ou d'un ensemble de bâtiments dont le terrain doit être divisé."],
    benefit="Les règles alternatives favorables aux demandes conjointes sur unités contiguës du premier alinéa restent entières. Le bénéfice de l'appréciation globale des lotissements et ensembles avec division du troisième alinéa est étendu en supprimant le veto du règlement, pour les futures décisions et demandes en cours aussi. Le maintien du renvoi à L. 151-15 ne rétablit aucun quota SRU supprimé ; aucun allègement fiscal, aide au logement ou dérogation indépendante n'est supprimé.")
effect(a, 'relief_extended', 'urbanisme-projets-divises-appreciation-ensemble',
    "Suppression du veto du PLU contre l'appréciation d'ensemble des opérations avec division visées au troisième alinéa.",
    "Le lotissement ou l'ensemble de plusieurs bâtiments avec division bénéficie d'une appréciation globale, sauf opposition du règlement du PLU.",
    "La même appréciation globale est garantie pour ces opérations ; le règlement ne peut plus s'y opposer, sans suppression de la totalité des règles applicables.",
    'regime', "Aménageurs et constructeurs de lotissements ou de plusieurs bâtiments sur une ou plusieurs unités foncières contiguës avec division en propriété ou jouissance.",
    "Décisions après entrée en vigueur, demandes en cours incluses ; clauses locales d'opposition inopposables à ces décisions ; titres anciens et recours préservés.",
    "Aucune formalité ou autorisation de remplacement, aucune demande conjointe nouvelle imposée au troisième alinéa.",
    "l'ensemble du projet est apprécié au regard de la totalité des règles édictées par le plan local d'urbanisme, sauf si le règlement de ce plan s'y oppose.",
    "l'ensemble du projet est apprécié au regard de la totalité des règles édictées par le plan local d'urbanisme. Le règlement de ce plan ne peut s'opposer à cette appréciation d'ensemble.")

retained(21,
    "Maintien intégral de la définition des zones A par le potentiel agronomique, biologique ou économique des terres, équipées ou non. La qualification sert une protection essentielle de l'activité et des sols agricoles et n'est pas une autorisation individuelle nouvelle. La présence d'équipements n'est ni rendue obligatoire ni utilisée pour supprimer les possibilités de construire prévues au régime agricole.",
    "R. 151-17 et R. 151-23 conservent respectivement le support de zonage et les constructions admissibles. L. 151-11, L. 151-12 et L. 151-13 ont été lus : équipements collectifs, changements de destination, extensions et annexes, secteurs de taille et capacité limitées restent accessibles sous leurs conditions. Aucun classement automatique de toute terre équipée ni restriction des dérogations futures n'est ajouté. Une coupe générale de cette définition retirerait la protection du sol sans identifier une formalité redondante.",
    "La protection des terres agricoles conserve la même définition et les mêmes critères alternatifs ; aucune nouvelle réduction ou contrainte n'est démontrée.",
    "Le maintien ne certifie pas le bien-fondé du classement de chaque parcelle ni les coûts des règles locales ; les possibilités de construire restent régies par leurs textes.",
    "Aucune charge nouvelle n'est identifiée : pas de dossier agronomique individuel, registre, déclaration ou nouvelle condition d'équipement ajouté.")

retained(22,
    "Maintien intégral des deux catégories de possibilités de construire en zone A : besoins agricoles et matériel des CUMA, puis constructions, transformations et extensions autorisées par les textes législatifs cités. L'article n'institue pas un nouvel agrément d'urbanisme pour les coopératives : il reconnaît une qualité relevant du code rural. Retirer ces possibilités pendant que la protection de la zone A subsiste serait contraire à la préservation des dérogations favorables.",
    "L. 151-11, L. 151-12 et L. 151-13 lus en entier dans le corpus : toutes leurs possibilités et conditions propres demeurent, y compris équipements collectifs, transformations agricoles, méthanisation, changements de destination, extensions/annexes et secteurs limités. Le renvoi L. 525-1 rural n'est pas une demande d'agrément créée par cet article et son texte intégral n'est pas joint au corpus des cinq codes consulté ; la réforme de l'agrément rural lui-même serait extérieure au lot et n'est pas réputée réalisée. Le 1° et le 2° restent dans leur ordre, sans transfert de conditions ni limitation aux opérations antérieures. Le verbe 'peuvent' ne devient pas un permis de plein droit.",
    "Les ouvertures utiles de constructibilité en zone A restent identiques pour les opérations futures éligibles ; aucune nouvelle suppression d'autorisation n'est annoncée.",
    "Les avis, autorisations et conditions des textes de fond ne sont pas supprimés ici ; l'agrément rural externe n'est pas audité intégralement par ce maintien.",
    "Aucune charge nouvelle n'est identifiée : aucune pièce justifiant la qualité de CUMA, aucune procédure ou condition complémentaire n'est ajoutée à la source.",
    "Tous les avantages possibles sont préservés pour l'avenir : constructions nécessaires à l'exploitation, stockage et entretien du matériel des CUMA éligibles, ainsi que constructions, installations, extensions, annexes, changements de destination et aménagements des trois articles législatifs visés. Leurs conditions restent les mêmes ; aucune voie n'est réduite aux seuls droits antérieurs et aucun nouvel agrément d'urbanisme ne se substitue à une dispense.")

retained(23,
    "Maintien intégral des cinq fondements alternatifs de classement N : sites et milieux, exploitation forestière, caractère naturel, ressources et prévention des risques dont expansion des crues. Ces critères assurent des protections environnementales, patrimoniales et de sécurité distinctes d'une formalité administrative inutile. La règle est une faculté de classement, sans dossier individuel ni prélèvement ; une suppression indifférenciée effacerait ces protections sans gain ciblé justifié.",
    "Les 1° à 5°, le 'soit' alternatif, les qualifications esthétique, historique et écologique et la réserve 'notamment' pour les crues sont intégralement conservés. R. 151-17 définit le support graphique et les articles L. 151-11 à L. 151-13, lus au corpus, conservent leurs possibilités utiles dans les zones naturelles ou forestières selon leurs champs. Aucune dérogation littorale, schéma de plage, exonération ou droit de construire autonome n'est fermé par la définition. Les contraintes locales concrètes et leur proportionnalité restent soumises à leurs fondements et recours.",
    "La définition de protection naturelle et forestière reste entière ; aucun allègement supplémentaire ni économie nationale n'est attribué à ce maintien.",
    "Aucun audit parcellaire ou chiffrage du coût des cinq motifs n'est réalisé ; les autorisations et dérogations d'autres articles ne sont pas réécrites par cette définition.",
    "Aucune charge nouvelle n'est identifiée : mêmes cinq critères alternatifs et aucune collecte, attestation, taxe ou procédure ajoutée.")

assert len(answers) == len(sources) == 24
assert [a['number'] for a in answers] == [s['number'] for s in sources]
with open('answer.json', 'w') as f:
    json.dump(answers, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(f'{len(answers)} articles écrits dans answer.json')
