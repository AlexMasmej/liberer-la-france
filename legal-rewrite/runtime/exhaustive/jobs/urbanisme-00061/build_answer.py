import json
from pathlib import Path

S = json.loads(Path('source.json').read_text())
R = json.loads(Path('reference-targets.json').read_text())
OUT = []

def impact(assessment, limitations, burdens, effects=None, classification='retained_necessary'):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=limitations, new_burdens_review=burdens, effects=effects or [])

def effect(kind, measure_id, description, before, after, unit, population, transition, burdens, sq, pq):
    return dict(kind=kind, measure_id=measure_id, description=description, before=before,
                after=after, unit=unit, affected_population=population,
                conditions_and_transition=transition, replacement_or_new_burdens=burdens,
                source_quote=sq, proposed_quote=pq)

def add(n, reason, notes, benefits, assessment, limits, burdens, xml=None, effects=None, removed=None):
    a = next(x for x in S if x['number'] == n)
    o = {k: a[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}
    o.update(proposed_xml=xml, reason=reason, review_notes=notes,
             status='retained_unchanged' if xml is None else 'rewrite_draft',
             benefit_review=benefits,
             substantive_impact=impact(assessment, limits, burdens, effects,
                                      'retained_necessary' if xml is None else 'material_reduction'))
    if xml is None:
        o['classification'] = 'retained_necessary'
    if removed:
        o.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19', removed_provisions=removed)
    o['reference_checks'] = []
    OUT.append(o)
    return o

add('R121-27',
    "Maintien intégral après examen : limiter l'usage de la servitude à sa finalité piétonne protège les propriétaires et les usagers contre un usage étranger au passage. Cette règle n'impose ni autorisation, ni déclaration, ni dossier et ne fait pas double emploi avec l'obligation distincte du propriétaire de laisser passer.",
    "L121-31 et L121-34, lus dans le corpus, concernent respectivement le passage longitudinal de trois mètres et l'accès transversal. La règle vise celui qui emprunte le passage, non un salarié. Les possibilités de modification et de suspension de la servitude restent distinctes ; aucune fermeture des dérogations littorales ni coordination SRU n'est introduite.",
    "Le passage public reste ouvert dans les conditions légales et la limitation de son usage protège les terrains grevés. Aucun avantage fiscal n'est en cause ; aucune faculté de suspension, d'adaptation ou de construction n'est retirée aux opérations futures éligibles.",
    "La destination exclusive du passage est maintenue ; aucune obligation administrative ou somme due n'est supprimée par cet article conservé.",
    "Le maintien ne constitue ni une simplification mesurée ni un examen achevé des autres dispositions littorales ou des 209 articles SRU.",
    "Aucune charge nouvelle n'est identifiée : aucun texte nouveau, aucune pièce ni procédure ne sont ajoutés à la limitation existante.")

add('R121-28',
    "Maintien intégral de la prise en charge par l'Etat des travaux nécessaires au passage et à la sécurité. La participation des collectivités et organismes est facultative. Supprimer cette garantie ferait peser un risque de financement sur les propriétaires grevés ; aucune contribution accessoire obligatoire n'est instituée ici.",
    "Le renvoi au seul 3° de R121-26 demeure exact dans la source et dans la proposition fournie : signalisation et travaux, avec préavis foncier de quinze jours sauf urgence. La dispense d'autorisation de mise en sécurité du 2° n'élargit pas par elle-même les dépenses financées par cet article.",
    "Le financement étatique des travaux du 3° est intégralement conservé pour les travaux futurs aussi ; la faculté de concours volontaire des collectivités et organismes demeure. Aucun coût n'est transféré au propriétaire et aucun avantage n'est réservé aux seuls travaux anciens.",
    "L'obligation de financement public et les concours facultatifs restent identiques ; il n'y a ni réduction de prélèvement ni nouveau transfert de financement.",
    "Les montants, la dépense publique future et le solde consolidé ne sont pas chiffrés ; le financement n'est pas assimilé à une économie nationale.",
    "Aucune charge nouvelle n'est identifiée : les financeurs obligatoires et facultatifs restent ceux du texte officiel, sans formalité supplémentaire.")

xml30 = """<p>Le préfet statue sur la demande sans avis préalable obligatoire du directeur départemental ou, le cas échéant, régional des finances publiques.<br />L'indemnité allouée est à la charge de l'Etat.</p>
<p>La suppression de cet avis obligatoire s'applique aux décisions prises à compter de l'entrée en vigueur du présent article, y compris sur les demandes en cours, sans nouveau dépôt. Les avis déjà recueillis demeurent utilisables. Les décisions antérieures, les droits à indemnisation et les voies de recours sont préservés.</p>"""
add('R121-30',
    "Réforme de fond : suppression de la consultation préalable obligatoire de la direction des finances publiques, circuit supplémentaire qui ne fixe ni le droit au dommage ni le juge compétent. Le préfet conserve sa décision et l'Etat sa dette d'indemnité ; aucune déclaration ni attestation ne remplace l'avis.",
    "R121-29 et sa proposition, L121-35, L121-36 et L105-1 ont été lus : propriété, dommage direct, matériel et certain, accord amiable et fixation juridictionnelle demeurent à leur champ. Le retrait de l'avis ne vaut ni indemnisation automatique ni suppression des contrôles budgétaires autonomes. La suppression de la forclusion spéciale déjà proposée à R121-29 n'est pas recomptée ici. Aucun renvoi au droit du travail n'est applicable.",
    "L'indemnité à la charge de l'Etat reste accessible aux dommages futurs remplissant les conditions légales, ainsi qu'aux demandes anciennes recevables. La suppression de l'avis n'en réduit ni le montant dû ni le droit au recours ; aucune indemnité de licenciement n'est concernée.",
    "Un avis administratif préalable obligatoire est effectivement retiré par rapport à la source entière, sans modifier l'assiette juridique ni le débiteur de l'indemnisation.",
    "Aucun délai de décision garanti ni gain financier chiffré n'est annoncé. Les conditions légales du dommage et les contrôles autonomes restent applicables.",
    "Aucune charge nouvelle n'est identifiée : la décision préfectorale existait déjà et ni le propriétaire ni le préfet ne doivent produire un document de remplacement.",
    xml30,
    [effect('obligation_removed', 'littoral-indemnisation-fin-avis-finances',
            "Suppression de l'avis financier obligatoire avant la décision préfectorale d'indemnisation.",
            "Avis préalable du directeur départemental ou régional des finances publiques obligatoire avant décision sur la demande d'indemnité.",
            "Décision du préfet sans cet avis obligatoire ; indemnité toujours supportée par l'Etat.",
            'legal_duty', "Préfet, services des finances publiques et propriétaires demandant l'indemnité de servitude littorale.",
            "Décisions prises dès l'entrée en vigueur, demandes en cours comprises ; avis déjà reçus utilisables et droits antérieurs préservés.",
            "Aucun avis, dépôt ou attestation de remplacement ; contrôles budgétaires ayant un autre fondement inchangés.",
            "Le préfet statue sur la demande après avoir recueilli l'avis du directeur départemental ou, le cas échéant, régional des finances publiques.",
            "Le préfet statue sur la demande sans avis préalable obligatoire du directeur départemental ou, le cas échéant, régional des finances publiques.")],
    ["Suppression de l'avis préalable obligatoire du directeur départemental ou régional des finances publiques avant la décision préfectorale d'indemnisation."])

add('R121-31',
    "Maintien intégral : l'absence d'indemnité pour des obstacles irréguliers et la répétition limitée à la disparition ou à l'atténuation du dommage évitent une indemnisation sans préjudice. Ce ne sont ni une taxe ni une formalité générale ; retirer la répétition autoriserait un double bénéfice financé sur fonds publics sans dommage correspondant.",
    "Le renvoi à R121-26 tient compte de sa proposition : les seules mesures de sécurité dispensées par le 2° ne sont pas, pour ce seul motif, des obstacles placés en violation de cet article. Les infractions d'urbanisme et d'occupation du domaine public restent des fondements distincts. La suspension ou modification du tracé n'entraîne une répétition que si elle atténue ou supprime effectivement le préjudice.",
    "L'indemnité pour un dommage légalement indemnisable est conservée pour toute situation éligible, ancienne ou future. La répétition n'est pas un retrait général de cet avantage : elle reste proportionnée à la diminution ou disparition du préjudice ; aucun avantage fiscal n'est concerné.",
    "Les deux règles de liquidation et de restitution demeurent intégralement ; aucun prélèvement ni nouvelle obligation de production n'est supprimé ou créé.",
    "Les montants de préjudice ne sont pas évalués ; aucune restitution automatique indépendante de son atténuation n'est déduite du maintien.",
    "Aucune charge nouvelle n'est identifiée : les causes et limites de restitution restent exactement celles du texte officiel, sans contrôle périodique ajouté.")

add('R121-32',
    "Maintien intégral des contraventions distinctes pour obstruction à la servitude et usage contraire à sa destination. Ces sanctions protègent l'accès piéton effectif et les propriétaires grevés ; elles ne constituent pas un prélèvement de financement. Aucun agrément ni justificatif redondant n'est imposé par cet article.",
    "Cinquième classe pour R121-26 ou l'obstacle à son application, quatrième classe pour R121-27 : les deux champs et classes sont conservés. La dispense de sécurité du 2° de R121-26 proposé ne constitue pas une infraction à cette obligation ainsi limitée ; les autorisations exigibles sur un autre fondement demeurent distinctes. Aucun montant d'amende ni récidive nouvelle n'est inventé.",
    "La dispense future de mise en sécurité prévue dans la proposition de R121-26 reste opposable dans son champ : une mesure licite n'est pas sanctionnée comme violation de cet article. Les autorisations valides et les dérogations littorales ne sont pas supprimées ; le texte ne contient pas d'exonération fiscale.",
    "Maintien des garanties pénales de l'accès et du bon usage du passage, sans suppression ni augmentation d'amende et sans réduction revendiquée.",
    "La proposition de R121-26 n'est pas le droit positif. Son adoption doit rester coordonnée ; aucune assimilation au préavis d'un contrat de travail n'est possible.",
    "Aucune charge nouvelle n'est identifiée : ni infraction supplémentaire, ni classe relevée, ni autorisation ou document nouveau ne sont introduits.")

add('R121-35',
    "Maintien intégral de l'ajout ultramarin des récifs coralliens, lagons et mangroves à la liste des milieux préservés. Il met en œuvre la protection écologique de L121-50 et ne crée pas un dossier ou un agrément autonome pouvant être supprimé isolément.",
    "L121-23, L121-50 et R121-4 ont été lus ; le 9° complète les huit catégories existantes et reste soumis au champ et aux critères écologiques de ces dispositions. Les cinq territoires sont conservés. Les règles ne ferment pas le schéma de plage ni les dérogations maintenues ; le présent article ne les abroge pas.",
    "Cet ajout protège des milieux ultramarins sans supprimer les possibilités d'aménagement recevables selon les autres dispositions. Aucune exonération fiscale ni dérogation littorale n'est retirée ; la protection écologique n'est pas assimilée à un avantage fiscal abrogeable.",
    "La catégorie écologique ultramarine demeure identique ; aucune réduction des obligations d'urbanisme ou des prélèvements n'est démontrée ici.",
    "La conformité de chaque opération aux protections nationales, européennes ou conventionnelles ne peut être déduite de ce maintien général.",
    "Aucune charge nouvelle n'est identifiée : la liste, ses territoires et ses critères restent ceux de la source, sans dossier supplémentaire.")

add('R121-37',
    "Maintien intégral de la règle de mesure ultramarine : elle détermine l'assiette de la servitude à partir de la limite haute du rivage, hors marées cycloniques, avec les adaptations et protections réservées. Sa suppression rendrait l'emprise incertaine et pourrait accroître la charge des propriétaires.",
    "Les cinq territoires, les deux références domaniales et les réserves relatives à la modification, à la suspension et à R121-39/R121-40 sont conservés. L121-45 et L121-51 ont été lus dans le corpus. Le texte entier du CG3P L5111-2 et L5331-4 n'est pas fourni dans ce lot ni vérifié ici ; aucune nouvelle définition de la zone des cinquante pas n'est inventée.",
    "Les possibilités de modification et de suspension ainsi que les distances et exceptions de R121-39/R121-40 restent applicables aux procédures futures recevables. Exclure les marées cycloniques de la mesure évite une extension exceptionnelle de l'emprise ; cette limite est conservée.",
    "La mesure de l'emprise et ses exceptions demeurent ; aucune réduction autonome de servitude ni création de prélèvement n'est revendiquée.",
    "Les renvois domaniaux extérieurs restent à confronter à leurs textes complets ; ce maintien n'établit ni superficies ni effets financiers individuels.",
    "Aucune charge nouvelle n'est identifiée : ni nouvelle largeur, ni déclaration, ni mesure à produire par le propriétaire ne sont ajoutées.")

add('R121-38',
    "Maintien intégral d'une voie facultative d'utilisation de cheminements publics existants sur domaine privé, par arrêté constatant leur ouverture. La convention protège l'accord du propriétaire ou gestionnaire ; elle ne fait pas double emploi avec l'arrêté qui détermine le tracé de la servitude opposable.",
    "L121-32 et sa proposition conservent l'enquête et la décision de tracé. Le présent texte vise seulement les cinq territoires, les zones naturelles ou forestières et espaces naturels des cinquante pas, avec domaine privé limitrophe du domaine public maritime. Le segment relatif à la convention nomme les collectivités ou établissements, alors que le segment domanial nomme aussi l'Etat : cette différence préexistante n'est pas étendue silencieusement. Les textes extérieurs L5112-1 et L5331-6-1 ne sont pas fournis intégralement.",
    "La possibilité de reprendre des cheminements déjà ouverts reste disponible pour les nouvelles opérations éligibles, sans imposer un nouveau chemin à travers d'autres terrains. L'accord de la collectivité ou de l'établissement propriétaire ou gestionnaire reste protégé ; aucune fermeture prospective de cette faculté n'est opérée.",
    "La procédure facultative et ses conditions sont maintenues ; aucun doublon établi ne permet de revendiquer ici une autorisation supprimée.",
    "Les définitions domaniales extérieures ne sont pas contrôlées intégralement. Le maintien ne dispense pas d'une procédure autonome légalement requise.",
    "Aucune charge nouvelle n'est identifiée : l'arrêté et la convention restent dans leur champ existant, sans envoi, avis ni registre ajouté.")

add('R121-39',
    "Maintien intégral des exemptions protectrices de certaines habitations et parcelles closes, avec exception de continuité ou d'accès. Les dates et conditions domaniales bornent un avantage existant ; les effacer supprimerait une protection favorable ou modifierait silencieusement le régime légal de passage.",
    "Dix mètres, bâtiments antérieurs au 1er août 2010, clôture à cette date, acquisition de l'Etat ou demande antérieure et exception de seul moyen de continuité ou d'accès sont conservés. L121-51 et R121-37/R121-40/R121-41 ont été confrontés. Les renvois CG3P L5111-2 et L5331-4 restent inchangés, leurs textes extérieurs complets n'étant pas fournis ici.",
    "La protection des terrains à moins de dix mètres des habitations et des terrains attenants clos demeure pour toute nouvelle décision concernant des biens remplissant les conditions historiques. L'avantage n'est pas limité aux seules servitudes déjà décidées ; la condition du seul moyen d'assurer le passage reste intacte.",
    "Maintien intégral d'exemptions et de leurs limites, sans réduction nouvelle revendiquée ni extension de l'emprise de la servitude.",
    "Les conditions historiques ne sont pas déplacées à la date de réforme ; l'éligibilité individuelle et les définitions domaniales restent à vérifier selon les cas.",
    "Aucune charge nouvelle n'est identifiée : aucune pièce, date supplémentaire, déclaration ou restriction d'accès à l'exemption n'est ajoutée.")

base40 = next(a['source_xml'] for a in S if a['number']=='R121-40')
xml40 = base40.replace("Cet accord doit résulter d'une convention passée avec une collectivité publique ou un groupement de collectivités publiques.",
    "Cet accord peut être constaté par tout écrit signé par le propriétaire du bâtiment et identifiant le tracé ainsi que la réduction de distance auxquels il consent. Aucune convention distincte avec une collectivité publique ou un groupement de collectivités publiques n'est requise sur le seul fondement du présent article.")
xml40 += "<p>Cette dispense de convention distincte s'applique aux décisions prises à compter de l'entrée en vigueur du présent article, y compris aux procédures en cours, sans nouveau dépôt. Un écrit déjà établi qui constate cet accord n'a pas à être renouvelé. Les conventions antérieures et les droits qui en résultent demeurent applicables. Le présent article ne vaut ni transfert de propriété ni dispense des autres conditions d'établissement de la servitude.</p>"
add('R121-40',
    "Réforme de fond ciblée : hors des quatre hypothèses de réduction déjà prévues, l'accord exprès du propriétaire peut être prouvé par un écrit signé, y compris préexistant, sans convention distincte avec une personne publique. Les quatre cas, la distance de référence et le consentement du propriétaire du bâtiment restent intégralement protégés.",
    "Le 1° de L121-32, R121-39 et R121-41 ont été lus : décision de tracé, enquête, justification et plafond de largeur de trois mètres dans les cas de R121-41 demeurent. L'écrit identifie l'accord et ne vaut pas autorisation tacite ni cession de terrain. Cette dispense ne retire aucune clause protectrice d'une convention déjà conclue. Le 4° reste au même emplacement et aucune distance nouvelle n'est créée.",
    "Les quatre possibilités existantes de réduire les dix mètres et la voie supplémentaire avec accord du propriétaire demeurent ouvertes aux opérations futures. La simplification du support de l'accord ne vaut pas renonciation générale aux droits du propriétaire ni disparition des protections de R121-39 et R121-41.",
    "Une convention bilatérale distincte imposée pour constater l'accord est retirée ; le consentement signé et les conditions de fond de la servitude subsistent.",
    "La dispense concerne uniquement la forme spéciale de l'accord du dernier alinéa, sans suppression de l'arrêté, de l'enquête ni des formalités foncières autonomes. Aucun coût net n'est chiffré.",
    "Aucune charge nouvelle n'est identifiée : l'écrit signé prouve le consentement auparavant contenu dans la convention obligatoire et peut être un acte existant ; aucun dépôt autonome n'est ajouté.",
    xml40,
    [effect('obligation_removed', 'littoral-accord-proprietaire-sans-convention-distincte',
            "Retrait de la convention spéciale avec une collectivité pour constater l'accord de réduction de la distance aux habitations.",
            "Dans les autres cas que les 1° à 4°, accord du propriétaire du bâtiment obligatoirement contenu dans une convention avec une collectivité publique ou son groupement.",
            "Même accord du propriétaire, constaté par un écrit signé identifiant le tracé et la réduction ; aucune convention distincte requise sur ce fondement.",
            'legal_duty', "Propriétaires de bâtiments et personnes publiques établissant une servitude longitudinale dans les cinq territoires ultramarins concernés.",
            "Décisions nouvelles et procédures en cours dès l'entrée en vigueur ; écrits existants réutilisables et conventions antérieures préservées.",
            "Consentement exprès prouvé, comme dans la convention antérieure ; aucune nouvelle déclaration, aucun registre et aucune cession de propriété.",
            "Cet accord doit résulter d'une convention passée avec une collectivité publique ou un groupement de collectivités publiques.",
            "Aucune convention distincte avec une collectivité publique ou un groupement de collectivités publiques n'est requise sur le seul fondement du présent article.")],
    ["Suppression de la convention distincte obligatoire avec une collectivité publique ou son groupement pour constater l'accord du propriétaire à la réduction de distance, hors des quatre cas existants."])

add('R121-41',
    "Maintien intégral : la justification du tracé lors de l'enquête protège les habitations et terrains clos soumis à une dérogation et le plafond de trois mètres limite l'emprise. Le texte n'exige pas un second dossier distinct : supprimer la justification retirerait le contrôle d'une atteinte particulière au droit de propriété.",
    "R121-16, R121-13, L121-32 et R121-39/R121-40 ont été lus. L'explication spécifique complète les plans et la notice sans imposer une attestation autonome. Les 1° et 2°, les matériaux durables adhérant au sol, dix mètres, trois mètres et les trois occurrences du 1er août 2010 sont conservés. La formule 'édifiés au' du 2°, différente du 'avant' de R121-39, est une discordance préexistante signalée, sans modification silencieuse de l'éligibilité. Renvois domaniaux extérieurs conservés, non vérifiés intégralement.",
    "Le plafond de trois mètres et la justification des atteintes aux terrains et habitations protégés subsistent pour les nouvelles procédures recevables. L'accord simplifié de R121-40 ne dispense pas de ces garanties ; aucune dérogation littorale n'est fermée par ce maintien.",
    "Les garanties de l'enquête et la largeur maximale sont maintenues ; aucun nouveau gain de fusion de pièces n'est attribué à une notice déjà intégrée au dossier.",
    "La discordance 'édifiés au'/'avant le' et les références domaniales extérieures appellent un contrôle ciblé ; aucune résolution implicite n'est présentée comme acquise.",
    "Aucune charge nouvelle n'est identifiée : le dossier existant et la justification spécifique demeurent, sans exemplaire, attestation ou contrôle supplémentaire.")

add('R121-42',
    "Maintien intégral de la méthode de mesure du seuil légal de cinq cents mètres. Elle évite que le seuil soit modifié par le choix d'un itinéraire et protège les propriétés contre la création d'un accès transversal lorsqu'un accès public est assez proche. Aucune formalité autonome n'est prescrite.",
    "L121-51 a été lu en entier : cinq cents mètres au moins, trois mètres de largeur maximum et distance protectrice aux habitations. Le présent article mesure en ligne droite depuis le débouché du chemin ou de ses sentiers de prolongement jusqu'à tout accès public ou rural au rivage ; il ne remplace pas ces conditions.",
    "Le seuil de distance évite des servitudes supplémentaires inutiles et sa méthode de calcul reste applicable aux projets futurs. Les autres limites et exemptions de L121-51 ne sont ni réduites ni réservées aux décisions antérieures.",
    "La règle de mesure existante est conservée sans élargissement de l'emprise, suppression de prélèvement ou nouveau délai.",
    "La distance réelle et l'existence d'un accès effectif doivent être établies pour chaque projet ; aucun résultat cartographique n'est présumé.",
    "Aucune charge nouvelle n'est identifiée : la même mesure en ligne droite demeure, sans étude supplémentaire ni justificatif nouveau.")

add('R121-43',
    "Maintien intégral de la justification, dans la notice déjà requise, du respect des conditions ultramarines d'accès transversal. Il s'agit d'une information intégrée, non d'un rapport distinct ; elle garantit le seuil et les protections des habitations sans imposer un second circuit administratif.",
    "R121-19 1°, L121-51 et R121-42 ont été lus. La notice reste celle du dossier d'enquête déjà prévu, avec conditions de distance, d'emprise et de champ territorial. La suppression de l'avis communal distinct proposée à L121-34 ne retire pas cette justification de fond et n'est pas comptée une seconde fois.",
    "Les conditions protégeant les habitations et limitant la création de chemins restent contrôlées dans une notice unique pour les projets futurs. Aucune exception favorable ni accès à une procédure recevable n'est fermé ; il n'existe pas ici d'exonération fiscale.",
    "La notice comportait déjà la justification : le maintien ne démontre ni fusion nouvelle de documents ni charge supplémentaire supprimée.",
    "Le contenu individuel d'un dossier et sa conformité ne sont pas présumés ; les autorisations ou enquêtes sur d'autres fondements conservent leur régime.",
    "Aucune charge nouvelle n'est identifiée : la justification reste insérée dans la notice existante, sans document ou transmission additionnels.")

add('R122-2',
    "Maintien intégral de la désignation des petits plans d'eau exclus du régime de protection de L122-12. Elle donne une portée concrète à une dérogation favorable, sans nouvelle autorisation individuelle ; supprimer cet outil pourrait rendre l'exclusion inopérante dans le PLU.",
    "L122-12 2° a été lu : exclusion possible par SCOT, PLU ou carte communale en raison de la faible importance du plan d'eau. Le présent texte ne vise que le règlement du PLU et ne ferme pas les deux autres voies. Il ne crée ni seuil de superficie nouveau ni exemption automatique de toutes les autres protections.",
    "La faculté d'exclure des plans d'eau de faible importance reste ouverte aux nouveaux documents et aux évolutions futures recevables. Aucune nouvelle condition n'est ajoutée, et les exclusions déjà légalement décidées ne sont pas supprimées.",
    "La voie réglementaire donnant effet à une exclusion favorable est intégralement conservée, sans réduction nouvelle de contrainte revendiquée.",
    "La faible importance s'apprécie selon le cadre légal, sans seuil inventé ; ce maintien ne démontre pas l'éligibilité de chaque plan d'eau.",
    "Aucune charge nouvelle n'est identifiée : la désignation existante demeure dans le PLU, sans attestation ou procédure individuelle supplémentaire.")

xml3 = """<p>L'arrêté du préfet coordonnateur de massif prévu au 1° de l'article L. 122-12 est affiché pendant un mois en mairie dans la ou les communes intéressées. Aucune insertion dans un journal n'est requise au titre du présent article.</p>
<p>Il fait l'objet d'une publication au recueil des actes administratifs de l'Etat dans le département.</p>
<p>Il est annexé, le cas échéant, au plan local d'urbanisme, et tenu à disposition du public en mairie et en préfecture.</p>
<p>La dispense d'insertion dans un journal s'applique aux arrêtés pris à compter de l'entrée en vigueur du présent article. Les arrêtés antérieurs demeurent soumis aux formalités de publicité applicables à la date à laquelle ils ont été pris ; les publicités déjà régulièrement accomplies n'ont pas à être renouvelées. Les arrêtés et les droits qui en résultent ainsi que les voies de recours sont préservés.</p>"""
add('R122-3',
    "Réforme de fond : retrait de l'annonce dans un journal départemental, cumulée dans la source avec l'affichage municipal, le recueil administratif, l'annexion éventuelle au PLU et la consultation en mairie et préfecture. Ces quatre moyens demeurent, ainsi que le mois d'affichage ; aucune publicité de remplacement n'est créée.",
    "L122-12 1° a été lu : l'arrêté permet l'exclusion des plans d'eau dont moins du quart des rives est en zone de montagne. La suppression ne retire ni cet avantage ni les conditions de son octroi. Elle ne vaut que pour les arrêtés nouveaux ; les anciennes formalités et recours restent protégés. Les dispositions relatives à la publication administrative et au déclenchement des délais de recours doivent être confrontées dans leur champ, sans assimiler la dispense à une réduction des délais de recours.",
    "L'exclusion favorable de L122-12 1° reste ouverte aux nouvelles demandes éligibles sans délai d'entrée en vigueur propre supplémentaire. La publicité utile et l'accès des tiers sont conservés ; ni la limite du quart des rives ni les exclusions déjà acquises ne sont modifiées.",
    "Une insertion obligatoire dans un journal est supprimée pour les nouveaux arrêtés ; les autres publicités et leur durée restent inchangées.",
    "Le prix des annonces et l'économie publique ne sont pas connus. Les règles autonomes de recours ne sont pas chiffrées ni réputées abrogées.",
    "Aucune charge nouvelle n'est identifiée : affichage, recueil, annexion et mise à disposition existaient déjà, sans publication numérique ou rapport de remplacement imposé.",
    xml3,
    [effect('obligation_removed', 'montagne-arrete-plans-eau-fin-annonce-journal',
            "Suppression de la mention payante en journal de l'affichage de l'arrêté d'exclusion d'un plan d'eau.",
            "Mention de l'affichage obligatoirement insérée en caractères apparents dans un journal diffusé dans le département, en plus des autres publicités.",
            "Aucune insertion en journal requise ; un mois d'affichage, publication au recueil, annexion éventuelle au PLU et consultation du public conservés.",
            'legal_duty', "Préfecture et collectivités assurant la publicité des arrêtés du préfet coordonnateur de massif prévus au 1° de L122-12.",
            "Arrêtés pris dès l'entrée en vigueur ; formalités antérieures et recours conservés, sans renouvellement des publicités déjà accomplies.",
            "Aucun support de publicité nouveau ; maintien des supports officiels déjà obligatoires. Coût net non chiffré.",
            "Mention de cet affichage est insérée en caractères apparents dans un journal diffusé dans le département.",
            "Aucune insertion dans un journal n'est requise au titre du présent article.")],
    ["Suppression de l'insertion obligatoire dans un journal départemental de la mention de l'affichage de l'arrêté, en maintenant les autres publicités et leur durée."])

xml31 = """<p>Le préfet territorialement compétent dispose d'un délai de deux mois, à compter de la date de réception de la demande, pour notifier au demandeur l'autorisation expresse prévue au cinquième alinéa de l'article L. 122-11.</p>
<p>Faute de délivrance de l'autorisation dans ce même délai, cette dernière est réputée rejetée.</p>
<p>Le délai de deux mois s'applique aux demandes reçues à compter de l'entrée en vigueur du présent article. Pour les demandes reçues avant cette date et sur lesquelles il n'a pas encore été statué, le délai expire à la première des deux dates suivantes : l'échéance du délai de quatre mois antérieurement applicable ou l'expiration de deux mois à compter de cette entrée en vigueur. Aucun nouveau dépôt n'est requis. Les décisions, y compris implicites, déjà intervenues ne sont pas remises en cause et leurs délais de recours ne sont pas rouverts.</p>"""
add('R122-3-1',
    "Réforme de fond : le délai laissé au préfet pour notifier l'autorisation expresse passe de quatre à deux mois. L'autorisation expresse et le rejet implicite sont maintenus pour protéger les terres, le patrimoine et la sécurité ; la réduction n'est donc pas présentée comme une autorisation supprimée ni comme une acceptation automatique.",
    "L122-11 entier a été lu : dans la version actuelle, le cinquième alinéa correspond au 3° sur restauration, reconstruction et extensions limitées de chalets ou bâtiments d'estive. Le dernier alinéa ajoute notamment la servitude d'usage hivernal ou liée aux réseaux. Les avis des commissions, destinations, ruines, absence de changement de destination et servitudes demeurent ; le texte ne concerne ni le délai général des permis ni le contrat d'emploi saisonnier. Deux mois est un nouveau choix de délai du projet, fondé sur l'orientation de réduction des délais et non une donnée du droit existant.",
    "La voie favorable de restauration ou reconstruction des anciens chalets et d'extension limitée demeure ouverte aux futures situations remplissant les conditions de L122-11. Le délai réduit ne supprime ni les avis ni les conditions de sécurité ou d'usage, et aucune autorisation acquise n'est retirée.",
    "Réduction démontrée du délai administratif de quatre à deux mois, à point de départ inchangé pour les demandes nouvelles ; le silence reste un rejet, sans gain de constructibilité présumé.",
    "Il s'agit de mois calendaires, non d'un nombre fixe de jours. Le délai ne garantit pas une autorisation favorable ni l'achèvement des procédures distinctes. Le rejet implicite intervient aussi plus tôt et peut avancer le point de départ du recours, dont la durée propre n'est pas réduite. Les moyens administratifs, le coût net et le bilan pratique pour le demandeur ne sont pas établis.",
    "Aucune charge documentaire ou procédure nouvelle n'est identifiée : la même demande est instruite sans nouveau dépôt. La notification et le recours existaient déjà, mais le préfet doit agir plus vite et le demandeur peut devoir exercer plus tôt son recours contre un rejet implicite. Cet effet de calendrier est signalé, sans prétendre établir un solde net de simplification.",
    xml31,
    [effect('deadline_reduced', 'montagne-chalets-autorisation-delai-deux-mois',
            "Réduction de moitié du délai de notification de l'autorisation expresse relative aux chalets d'alpage et bâtiments d'estive.",
            "Quatre mois à compter de la réception de la demande ; absence de délivrance dans le délai valant rejet implicite.",
            "Deux mois à compter de la même réception pour les nouvelles demandes ; absence de délivrance valant toujours rejet implicite.",
            'other', "Demandeurs d'autorisation expresse et préfet territorialement compétent au titre du cinquième alinéa de L122-11.",
            "Demandes nouvelles dès l'entrée en vigueur ; demandes pendantes à l'échéance la plus proche entre ancien délai et deux mois après la réforme. Décisions acquises et délais de recours non rouverts.",
            "Aucune déclaration de remplacement ; mêmes avis et garanties, échéance administrative raccourcie avec coût d'organisation non chiffré.",
            "dispose d'un délai de quatre mois, à compter de la date de réception de la demande",
            "dispose d'un délai de deux mois, à compter de la date de réception de la demande")],
    ["Suppression de deux des quatre mois du délai administratif de notification de l'autorisation expresse, avec une règle transitoire qui ne prolonge pas les demandes pendantes."])

NOTE2019 = "La note source a été lue intégralement : annulation partielle par le Conseil d'Etat, décision n°414931 du 26 juin 2019, du décret n°2017-1039 en tant qu'il omettait l'évaluation environnementale des créations ou extensions autorisées en application des seconds alinéas de L122-20/L122-21. Elle ne vaut ni abrogation de toute la procédure UTN ni dispense environnementale. "

add('R122-5',
    "Maintien intégral : les extensions inférieures aux seuils sont expressément réputées limitées et échappent au régime UTN dans les conditions légales. Le premier alinéa définit le champ des créations et extensions plus importantes ; supprimer l'article retirerait notamment une présomption favorable utile sans supprimer les obligations législatives.",
    NOTE2019 + "L122-5, L122-16 et L122-19 ont été lus en entier. La dérogation UTN à L122-5 à L122-7 et le régime des petites extensions restent distincts. Le chapitre du code du tourisme, extérieur aux cinq codes fournis, n'est pas réputé réécrit ni entièrement vérifié.",
    "La qualification favorable d'extension limitée pour les extensions sous les seuils demeure ouverte aux projets futurs. L'exception UTN aux règles de continuité conserve son fondement législatif ; aucune réduction de l'avantage ni restriction aux seuls projets anciens n'est introduite.",
    "Maintien du champ et de la présomption favorable existants ; aucune formalité ni autorisation nouvelle n'est supprimée par simple conservation de cet article.",
    "Les obligations du code du tourisme et le droit européen ne sont pas intégralement examinés ici ; le coût administratif et les effets de chaque projet restent inconnus.",
    "Aucune charge nouvelle n'est identifiée : les seuils et les deux régimes existants restent identiques, sans dossier ou évaluation ajouté par le présent maintien.")

add('R122-6',
    "Maintien intégral des règles de calcul des seuils : le programme général empêche le fractionnement artificiel, tandis que la reconstruction se mesure à la seule augmentation de surface. Supprimer cette seconde règle retirerait un allègement ; supprimer la première affaiblirait le contrôle des grands projets sans réduire explicitement les obligations correspondantes.",
    NOTE2019 + "R122-8 et R122-9 ont été lus entièrement. Les 1° et 2° gardent leurs champs distincts ; la reconstruction vise hébergements, équipements et refuges après démolition, sans imposer la surface totale reconstruite comme augmentation.",
    "La prise en compte de la seule augmentation de surface lors d'une reconstruction après démolition demeure applicable aux opérations futures, y compris refuges. Le programme général reste la référence en cas de réalisation fractionnée, sans nouveau seuil ni cumul de surface inventé.",
    "Les règles anti-fractionnement et de calcul favorable de la reconstruction sont maintenues ; aucune réduction nouvelle n'est revendiquée.",
    "La surface et le caractère unique du programme doivent être appréciés concrètement. Le maintien ne modifie aucun seuil de R122-8 ou R122-9.",
    "Aucune charge nouvelle n'est identifiée : pas de document ni registre nouveau, et les surfaces continuent d'être calculées selon les deux règles officielles.")

add('R122-7',
    "Maintien intégral après examen des trois facultés locales de qualification. Ces facultés peuvent accroître l'encadrement UTN, mais permettent aussi de relever du régime dérogatoire à la continuité de L122-19 : une abrogation isolée peut donc fermer une possibilité de construire. Leur suppression sans fondement favorable de remplacement n'est pas retenue.",
    NOTE2019 + "L122-16 à L122-21 ont été lus. Les 2° de L122-17/L122-18 autorisent les qualifications locales ; L122-19 écarte L122-5 à L122-7 pour les UTN. Une suppression éventuelle exigerait une coordination de ces fondements et de leurs effets favorables, non réalisée dans ce lot. Les 1°, 2° et le dernier alinéa restent complets, sans extension de compétence ni baisse de seuil nouvelle.",
    "Les qualifications locales facultatives restent ouvertes pour les futures opérations recevables. Leur accès au régime UTN et à ses dérogations n'est pas réservé aux anciens documents ; la protection des avantages interdit ici de traiter toute qualification locale comme une charge purement supprimable.",
    "Aucune suppression de régime n'est revendiquée : les facultés territoriales sont maintenues pour éviter la disparition concomitante d'un effet favorable de constructibilité.",
    "L'effet net de chaque qualification dépend du projet et des documents. Ni une réduction de contraintes ni une purge globale des règles locales n'est démontrée.",
    "Aucune charge nouvelle n'est identifiée : les seules facultés déjà prévues demeurent, sans rendre obligatoire leur usage ni créer un suivi supplémentaire.")

add('R122-8',
    "Maintien intégral des huit catégories et seuils UTN structurantes : ils déclenchent l'encadrement des opérations importantes mais délimitent aussi les projets qui restent en dehors. L'exclusion des logements de personnels doit subsister. Aucun dossier supplémentaire n'est prescrit ici ; enlever la liste isolément déstabiliserait le régime favorable et son contrôle.",
    NOTE2019 + "R122-6/R122-7/R122-9/R122-10 et L122-17/L122-19/L122-20 ont été confrontés. Contrôle : 100 hectares inclus ; hébergements strictement au-delà de 12 000 m², golf au-delà de 15 ha, camping au-delà de 5 ha, sports motorisés et pistes en site vierge au-delà de 4 ha ; plus de dix mille voyageurs par jour et dénivelé supérieur à 300 mètres cumulés au 8°. Le deux-points final du 6° est conservé sans correction de fond. Le tableau du code de l'environnement définissant le site vierge n'est pas fourni intégralement ; son contenu n'est pas inventé.",
    "L'exclusion des logements destinés aux personnels saisonniers ou permanents est conservée pour les futures opérations éligibles. Les seuils et leurs bornes strictes préservent les projets qui n'y entrent pas ; 'saisonnier' qualifie ici un besoin de logement et ne crée aucun nouveau CDD.",
    "Liste, seuils et exclusion favorable demeurent intégraux ; aucune autorisation supplémentaire supprimée ni baisse de prélèvement n'est attribuée à ce maintien.",
    "Le renvoi au tableau environnemental extérieur reste à vérifier sur son texte complet ; aucun abaissement de seuil ni chiffrage de projets dispensés n'est présumé.",
    "Aucune charge nouvelle n'est identifiée : les huit catégories, conditions cumulatives et exclusions demeurent celles de la source officielle.")

add('R122-9',
    "Maintien intégral des catégories UTN locales et de leurs limites : les seuils, le caractère non urbanisé de certaines implantations et les conditions de refuges délimitent l'assujettissement tout en permettant le régime UTN. Une abrogation isolée ne supprimerait pas les fondements législatifs et pourrait fermer des possibilités favorables de projet.",
    NOTE2019 + "Contrôle des bornes : domaine skiable strictement plus de 10 et moins de 100 ha ; golf jusqu'à 15 ha inclus ; 3° seulement hors secteur urbanisé ou constructible en continuité ; hébergement/équipement strictement plus de 500 m² ; camping entre 1 et 5 ha ; création de refuges sans seuil propre et extension strictement au-delà de 200 m². Le renvoi extérieur à tourisme L326-1 n'est pas fourni intégralement ; aucune redéfinition du refuge n'est inventée.",
    "Les exclusions liées à l'implantation du 3° et les bornes des seuils demeurent pour les opérations futures. L'accès des refuges au régime UTN n'est pas retiré, et aucune création de refuge n'est silencieusement soumise au seuil de 200 m² réservé à l'extension.",
    "Les trois catégories, leurs sous-catégories et leurs limites restent inchangées ; aucun allègement nouveau n'est déduit de ce maintien.",
    "Le contenu complet de la définition touristique extérieure reste à vérifier. Les valeurs limites sont conservées sans étendre les catégories pour combler une éventuelle lacune.",
    "Aucune charge nouvelle n'est identifiée : aucun seuil nouveau, aucune pièce et aucune condition d'emploi ou de logement supplémentaire ne sont ajoutés.")

add('R122-10',
    "Maintien intégral de la compétence et de la procédure d'autorisation des UTN structurantes hors SCOT. Cette autorisation permet l'examen d'un projet sans imposer d'abord l'adoption d'un SCOT ; l'enlever isolément retirerait une voie de projet sans abroger l'exigence législative de L122-20.",
    NOTE2019 + "L122-20 entier et ses notes ont été lus, ainsi que R122-8 et R122-12 à R122-18, dont les dispositions actuelles relatives à l'évaluation et à la participation. La dérogation historique à L142-4 mentionnée dans L122-20 est limitée au 1er janvier 2019 par sa note : le maintien de R122-10 ne la réactive pas. La compétence du préfet coordonnateur de massif reste distincte de celle du préfet départemental au titre des UTN locales.",
    "La voie d'autorisation hors SCOT demeure ouverte aux opérations futures recevables. Les petites extensions et les autres exclusions conservées ne sont pas réassujetties par ce renvoi ; aucune dérogation historique expirée n'est présentée comme un avantage actuel.",
    "Maintien d'une procédure législativement requise et de sa compétence ; aucune suppression d'autorisation ou réduction de délai n'est revendiquée ici.",
    "Les autres formalités de R122-13 à R122-18 sont seulement lues pour le renvoi, non réécrites par ce lot. L'évaluation environnementale demeure requise selon son champ propre.",
    "Aucune charge nouvelle n'est identifiée : le renvoi procédural existant reste identique, sans dossier additionnel, extension aux communes couvertes ou nouvel avis.")

add('R122-11',
    "Maintien intégral de la voie d'autorisation des UTN locales en l'absence de PLU et de la compétence départementale. Elle permet l'examen du projet sans exiger préalablement un PLU ; sa suppression réglementaire seule ne supprimerait pas L122-21 et ferait perdre un accès favorable à la procédure.",
    NOTE2019 + "L122-21 et ses notes ainsi que R122-9 et R122-12 à R122-18 ont été lus en entier. Les avis et participations légaux demeurent ; la dérogation historique à L142-4 limitée au 1er janvier 2019 dans la note de L122-21 n'est pas réactivée. L'exigence porte sur les communes dépourvues de PLU, distinctement du critère de SCOT des UTN structurantes.",
    "La procédure hors PLU reste accessible pour de nouvelles UTN locales admissibles ; les catégories et exclusions de R122-9 ne sont pas modifiées. Aucune faculté favorable n'est réservée au stock d'anciens projets, et l'avantage historique expiré n'est pas recréé.",
    "Le renvoi et la compétence nécessaires à une voie de projet sans PLU sont maintenus ; aucune baisse de taxe ni formalité supprimée n'est annoncée.",
    "Les modalités de R122-13 à R122-18 ne sont pas modifiées dans ce lot ; les règles environnementales supérieures demeurent à leur champ propre.",
    "Aucune charge nouvelle n'est identifiée : ni élargissement territorial, ni second dossier, ni autorisation nouvelle n'est introduit par ce maintien.")

add('R122-12',
    "Maintien intégral de la faculté de demander une autorisation pour plusieurs opérations simultanément. La source organise déjà le regroupement ; la réécrire pour annoncer une nouvelle fusion serait artificiel. Aucun délai minimal, agrément, copie ou déclaration supplémentaires ne sont prescrits par cet article.",
    NOTE2019 + "R122-10/R122-11 et les modalités de R122-13 à R122-18 ont été lus. La pluralité d'opérations dans une demande ne dispense ni du calcul global anti-fractionnement de R122-6 ni des évaluations et participations requises ; elle n'impose pas non plus de regrouper tous les projets d'un demandeur.",
    "La faculté de regrouper plusieurs opérations reste ouverte aux demandes futures recevables et aux dossiers qui peuvent en bénéficier selon leur procédure. Elle n'est ni rendue obligatoire ni limitée aux autorisations anciennes ; aucune condition nouvelle de bénéfice n'est ajoutée.",
    "Le regroupement déjà autorisé est conservé sans lui attribuer un nouveau gain de fusion ou une réduction supplémentaire de pièces.",
    "Aucun effet chiffré de regroupement n'est établi ; les seuils globaux et les protections environnementales ne sont pas écartés par cette faculté.",
    "Aucune charge nouvelle n'est identifiée : le regroupement demeure facultatif et aucun registre, délai ou document de coordination n'est ajouté.")

# Analyses des seules cibles requises, y compris les rapprochements lexicaux
# avec le droit du travail qui ne constituent pas des renvois juridiques.
contexts = {
    'R121-28': "L'article finance des travaux publics de passage et de sécurité sur les terrains grevés ; il ne règle aucune relation d'emploi.",
    'R121-30': "L'article statue sur l'indemnisation d'un dommage foncier dû à la servitude ; le versement n'est pas une indemnité de rupture d'emploi.",
    'R121-31': "L'article exclut ou répète une indemnité de servitude selon le dommage foncier ; il ne concerne aucune rupture de contrat d'emploi.",
    'R121-32': "L'article sanctionne les entraves ou usages illicites du passage littoral ; aucun salarié ni employeur n'est visé en cette qualité.",
}
for o in OUT:
    k = o['code_id']+'|'+o['source_id']
    for target_key in R['requirements'][k]:
        t = R['targets'][target_key]
        ctx = contexts[o['number']]
        if t['number'] == 'L1234-1':
            assessment = ctx + " L1234-1 distingue le préavis de licenciement ancien selon l'ancienneté et le nouveau préavis de quinze jours. Il est inapplicable ici : le préavis de R121-26 3° est une information foncière avant travaux, sauf urgence, non une notification de rupture de travail. Aucun seuil de services ni régime d'ancien contrat n'est importé."
        elif t['number'] == 'L1221-2':
            assessment = ctx + " L1221-2 proposé impose l'emploi privé nouveau à durée indéterminée et protège les contrats antérieurs ; il ne transforme ni une servitude ni une opération matérielle en contrat de travail. Durée des travaux et mission de service ne fixent aucun terme d'emploi dans cet article ; aucun CDD n'y est créé ou rétabli."
        elif t['number'] == 'L1234-9':
            assessment = ctx + " L1234-9 proposé porte sur l'indemnité patronale après un an au terme effectif, préavis compris, à 0,20 mois par année totale et fractions par mois complets, plafond de six mois. Ce calcul et la transition des anciens contrats sont inapplicables à l'indemnisation foncière et ne restreignent aucun droit de propriétaire dans cet article."
        elif t['number'] == 'R121-26':
            if o['number'] == 'R121-28':
                assessment = "Le renvoi vise exactement le 3° de R121-26 : signalisation et travaux nécessaires à la liberté et à la sécurité du passage, avec préavis de quinze jours sauf urgence. La proposition fournie modifie seulement le 2° pour les mesures immédiates de mise en sécurité ; elle ne modifie pas le financeur du 3°. L'Etat reste débiteur des dépenses visées, sans appliquer un préavis salarié ni une condition d'ancienneté."
            elif o['number'] == 'R121-31':
                assessment = "Le renvoi écarte l'indemnisation de la suppression d'obstacles placés en violation de R121-26, sans viser sa seule procédure de préavis. La dispense nouvelle du 2° pour danger grave et imminent n'est pas une violation de cette règle dans son champ et sa durée ; elle n'exonère pas d'une infraction sur un autre fondement. La répétition liée au dommage atténué ou supprimé reste distincte de toute indemnité salariale."
            else:
                assessment = "La cinquième classe frappe la violation ou l'obstacle à l'application des obligations de R121-26 ; la quatrième classe vise séparément R121-27. Les mesures immédiatement nécessaires de sécurité dispensées par le 2° proposé ne sont pas une violation de ce 2° lorsqu'elles en respectent les limites. Aucune sanction autonome ne rétablit l'autorisation écartée et aucun préavis de contrat privé ni seuil d'ancienneté ne s'applique."
        else:
            raise ValueError(t['number'])
        o['reference_checks'].append(dict(target_key=target_key, view_sha256=t['view_sha256'], assessment=assessment))

assert [o['number'] for o in OUT] == [a['number'] for a in S]
Path('answer.json').write_text(json.dumps(OUT, ensure_ascii=False, indent=2)+'\n')
