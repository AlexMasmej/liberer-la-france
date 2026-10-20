import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
by_number = {s['number']: s for s in sources}


def impact(classification, assessment, scope, burdens, effects=None):
    return {
        'version': 1,
        'classification': classification,
        'assessment': assessment,
        'scope_limitations': scope,
        'new_burdens_review': burdens,
        'effects': effects or [],
    }


def retained(number, reason, notes, assessment, scope, burdens, benefits):
    s = by_number[number]
    return {
        **{k: s[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')},
        'proposed_xml': None,
        'reason': reason,
        'review_notes': notes,
        'status': 'retained_unchanged',
        'classification': 'retained_necessary',
        'benefit_review': benefits,
        'substantive_impact': impact('retained_necessary', assessment, scope, burdens),
    }


vk = by_number['223 VK']
old1 = "dans les conditions prévues à l'avant-dernier alinéa du présent a"
new1 = "dans les conditions prévues par les dispositions du présent a définissant les entités transparentes"
old2 = "conformément à l'avant-dernier alinéa du a du 14°"
new2 = "conformément aux dispositions du a du 14° définissant les entités transparentes"
assert vk['source_xml'].count(old1) == 1
assert vk['source_xml'].count(old2) == 1
proposed = vk['source_xml'].replace(old1, new1).replace(old2, new2)
src_nodes = list(ET.fromstring('<root>' + vk['source_xml'] + '</root>'))
new_nodes = list(ET.fromstring('<root>' + proposed + '</root>'))


def text(node):
    return ''.join(node.itertext())


def passage(nodes, start, stop):
    return ''.join(text(node) + (node.tail or '') for node in nodes[start:stop]).strip()


effects = [{
    'kind': 'coordination',
    'measure_id': 'pilier-deux-renvois-transparence',
    'description': "Coordination unique des deux renvois à la transparence, dans la définition de l'entité hybride inversée au a du 14° et dans la présomption d'imposabilité de l'entité hybride au a du 14° bis : les deux applications de la même correction ne sont pas comptées comme deux effets.",
    'before': "Les deux renvois visent l'avant-dernier alinéa du a du 14°, lequel énonce désormais seulement l'assimilation de l'entité du b à une entité transparente ; la définition générale figure immédiatement avant cet alinéa.",
    'after': "Les deux renvois visent les dispositions du a du 14° définissant les entités transparentes, comprenant la définition générale et l'assimilation particulière ; les critères de transparence, les législations concernées, les produits, charges, participations et conditions d'imposabilité restent intégralement conservés.",
    'unit': 'other',
    'affected_population': "Entités interposées et détenteurs examinés pour la qualification d'entité hybride inversée, et entités constitutives examinées pour la qualification d'entité hybride, notamment dans un Etat ou territoire sans impôt équivalent à l'IS.",
    'conditions_and_transition': "Coordination des références internes seulement : maintien des critères, des périodes d'application de la source et des situations régies par celles-ci ; aucune nouvelle période d'option ni rétroactivité fiscale n'est instituée par ces renvois.",
    'replacement_or_new_burdens': "Aucune déclaration, autorisation, pièce, donnée, condition de fond ni échéance n'est ajoutée ; cette coordination commune aux deux renvois n'est pas une réduction de prélèvement.",
    'source_quote': passage(src_nodes, 48, 56),
    'proposed_quote': passage(new_nodes, 48, 56),
}]

answers = [{
    **{k: vk[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')},
    'proposed_xml': proposed,
    'reason': (
        "Coordination nécessaire, sans réforme de taux ni d'assiette du minimum international. Le corps intégral des définitions est conservé, sauf deux références internes au a du 14°. Dans la source entière, l'avant-dernier alinéa de ce a est désormais la phrase assimilant l'entité du b à une entité transparente ; il n'énonce pas la définition générale, placée immédiatement avant. Les renvois figurant dans la définition de l'entité hybride inversée et dans la présomption d'imposabilité de l'entité hybride sont donc explicités pour viser les dispositions définissant les entités transparentes. Aucun critère de ces définitions n'est réécrit ni ajouté. "
        "L'examen des charges porte aussi sur l'audit des états consolidés sans réserve sur la non-significativité de l'entité concernée, les données comptables, le rapport annuel conditionnant la qualification d'entité publique, les exigences réglementaires des fonds, l'agrément collectif préexistant des réseaux bancaires et les conditions des régimes fiscaux étrangers. Ces éléments délimitent le calcul, les exclusions et les garanties du minimum international expressément maintenu par is_distribution ; les retirer isolément modifierait ce régime ou ses avantages, sans suppression autorisée du minimum lui-même. Les définitions de normes agréées ne créent pas une demande individuelle d'agrément. Les mentions des déclarations désignent les acteurs du circuit de l'article 223 WW, sans imposer ici un dépôt supplémentaire. Aucune taxe accessoire, cotisation additionnelle à l'IS ordinaire ou pièce redondante autonome n'est supprimée dans cet article. Ce nouveau corps est une coordination de renvois, pas une simplification matérielle ni une réécriture stylistique revendiquée comme réforme."
    ),
    'review_notes': (
        "Lecture intégrale des 160 paragraphes et des trois notes source. Les seules différences normatives de rédaction sont les deux renvois aux dispositions définissant les entités transparentes ; aucun alinéa n'est déplacé. Le défaut ordinal préexistant est signalé, et non corrigé silencieusement. Les renvois internes numérotés restent utilisables. Contrôle local des textes cibles complets : 223 VL bis, 223 VN, 223 VN bis, 223 VO et 223 VO bis, 223 VS et 223 VS bis, 223 WF, 223 WG, 223 WW, 223 WS et 223 WS bis ; le 8° de CCH L423-1-2 conserve les comptes combinés, dans la source comme dans son brouillon public. "
        "Chiffres conservés : quatre ans pour le crédit qualifié, 80 % et quinze mois pour le crédit transférable négociable, 75 millions d'euros pour l'écart significatif, 50 millions pour l'entité non significative, 95 % et 85 % pour les entités d'investissement, plus de 20 % pour la mère partiellement détenue, 15 % pour le minimum et le régime agrégé, moins de 10 % pour les titres de portefeuille, un an au maximum pour le report du véhicule immobilier, ainsi que la périodicité annuelle et les deux réserves de liquidités des véhicules de titrisation. "
        "Le c du 39° conserve impérativement le 1er juillet 2021. Le nouvel IS français à la distribution ne devient pas, par analogie, un régime éligible à 223 WS ; le taux normal français proposé de 20 % ne remplace pas le minimum de 15 %. Le brouillon public de 223 VJ distingue déjà ces deux champs ; cela ne constitue pas une validation de ce brouillon. Le traitement concret de l'IS effectivement acquitté, des impôts différés, des pertes et crédits au regard des articles 223 VS à 223 VV quater reste à coordonner dans leurs lots ; aucun impôt fictif de distribution n'est créé ici et aucune absence de double impôt n'est présumée pour l'ensemble du chapitre. "
        "Les notes des articles 104 et 105 de la loi n° 2026-103 conservent leurs distinctions entre exercices clos à compter du lendemain de sa publication et exercices ouverts à compter du 31 décembre 2023 ; elles ne datent pas l'entrée en vigueur de la réforme proposée. Les textes complets CMF L511-30/L512-55, assurances L345-2, rural L524-6-2, les modèles conventionnels et la directive (UE) 2022/2523 ne sont pas joints à ce lot et ne sont pas déclarés vérifiés intégralement ; aucune conformité internationale nouvelle n'est attestée. Aucun chiffrage net, retrait de crédit ou économie publique n'est déduit du présent article."
    ),
    'status': 'rewrite_draft',
    'classification': 'coordination_only',
    'benefit_review': (
        "Les 2°, 3°, 3° bis et 3° ter sont intégralement conservés : crédit non qualifié, part remboursable qualifiée versée sous quatre ans, priorité du 3°, transfert négociable à au moins 80 % sous quinze mois, assimilation au crédit qualifié et traitement du transfert non négociable. Ces définitions ne créent ni ne suppriment le droit national au crédit lui-même, et restent ouvertes aux avantages futurs éligibles. Le seuil de 75 millions du 4° continue de limiter les retraitements pour écarts significatifs ; la qualification non significative du 8° bis demeure utilisable pour l'option simplifiée de 223 VN, avec l'audit des comptes consolidés et, au-delà de 50 millions d'euros de chiffre d'affaires de l'entité, l'emploi d'une norme qualifiée ou agréée pour les états servant à la déclaration. "
        "Les 9°, 10° et 11° gardent les catégories d'investissement, d'assurance et de services de fonds de pension, y compris 95 %/85 % et les dividendes ou plus-values exclus ; ces qualifications demeurent disponibles pour les exclusions ou règles particulières auxquelles elles donnent effectivement accès. Le 12° conserve la désignation d'une entité pour accomplir les déclarations du groupe ; ce n'est pas un nouveau dépôt. Les qualifications d'entités interposées, transparentes et hybrides des 14° et 14° bis gardent leurs critères et leur application aux situations futures : les deux renvois sont rendus explicites pour ne pas perdre la définition générale de transparence ni son assimilation particulière. Les exclusions d'entités mères, établissements stables et entités d'investissement des 15° à 18° restent exactement à leur champ, ainsi que la reconnaissance de l'agrément collectif au c du 18°. "
        "Les définitions d'entité publique (19°), fonds d'investissement (24°), fonds de pension et services associés (25°), organisme sans but lucratif (35°) et organisation internationale (36°) conservent les fondements des exclusions de 223 VL bis, pour les futures entités éligibles aussi. Le 35° maintient expressément le prolongement commercial de l'objet principal et les exceptions autorisant rémunérations adaptées, usages liés à l'activité et achats au prix du marché. Retirer leurs conditions de compte rendu, de contrôle ou de non-distribution ne serait pas une suppression autonome de formalité, mais changerait leur qualification ; aucune telle restriction ou substitution n'est opérée. "
        "Le 20° conserve les quatre catégories d'établissements stables et leurs liens conventionnels ; les 22°, 23°, 33° et 34° gardent les voies comptables alternatives, comptes combinés, normes nationales admises et période subsidiaire de l'année civile, sans nouvelle autorisation. Les 26° à 28° délimitent le groupe et sa territorialité ; ils ne constituent pas par eux-mêmes une exonération supplémentaire. Les 30° et 31° préservent les distinctions d'impôts remboursables et qualifiés, les bénéficiaires publics, internationaux, non lucratifs, de pension, d'investissement et d'assurance-vie, ainsi que les règles de résidence qui conditionnent leur traitement. "
        "Le 39° garde le régime favorable des distributions éligibles avec ses trois conditions, dont l'antériorité au 1er juillet 2021 ; il reste ouvert aux situations futures relevant d'un régime déjà admissible, mais pas automatiquement à un régime français nouvellement institué. Les 40° à 43° maintiennent les qualifications et calculs nécessaires aux règles de sociétés étrangères contrôlées, d'inclusion, d'allocation et de résultat qualifié, sans créer un nouveau prélèvement. Les 1°, 29°, 32°, 37°, 38° et 44° sont des définitions de calcul ou de détention, non des avantages fiscaux autonomes. "
        "Les 45° à 48° conservent le minimum de 15 %, le seuil de portefeuille inférieur à 10 %, la valeur nette comptable moyenne et l'imposition unique du véhicule immobilier avec report d'un an au maximum, sans les assimiler à une nouvelle baisse. Enfin, le 1°-0 et le 49° conservent le véhicule de titrisation, ses conditions et ses deux exceptions au reversement annuel : bénéfice fixé pour distributions ultérieures et réserves pour paiements futurs ou solvabilité. Leur rôle dans la désignation d'un autre redevable et l'exonération particulière de 223 WF IV bis reste opérant pour les véhicules futurs admissibles. Aucun de ces avantages n'est limité aux droits déjà acquis et aucune taxe générale correspondante n'est abolie dans ce lot."
    ),
    'substantive_impact': impact(
        'coordination_only',
        "Par rapport aux 160 paragraphes officiels entiers, seuls deux renvois ordinaux sont rendus explicites au bénéfice de la cohérence des définitions de transparence. Aucun taux, assiette, exclusion, option, délai ou rapport n'est supprimé. Les deux corrections sont regroupées dans une seule mesure et un seul effet de coordination, sans réduction matérielle revendiquée.",
        "Le minimum international et ses contraintes subsistent dans leur champ. Les conséquences de l'IS français à la distribution sur les impôts couverts et différés doivent être traitées dans les articles correspondants. Les sources externes non jointes ne sont pas validées ; aucun solde national de recettes ou de complexité n'est établi.",
        "Aucune charge nouvelle identifiée : les deux changements désignent des dispositions déjà présentes, sans nouvelle donnée, déclaration, preuve, autorisation, registre, délai ou condition de fond. Les conditions et obligations préexistantes restent recensées, sans en prétendre chiffrer le coût net pour l'ensemble des codes.",
        effects,
    ),
}]

answers.append(retained(
    '223 VL',
    "Maintien utile intégral, à droit constant : cet article borne le minimum international aux entités françaises de groupes multinationaux ou nationaux atteignant 750 millions d'euros de chiffre d'affaires consolidé au cours d'au moins deux des quatre exercices précédents. Il évite l'assujettissement général des entreprises plus petites et ajuste le seuil aux exercices de durée différente. La prise en compte du chiffre d'affaires des entités exclues est distincte de leur assujettissement. Supprimer le fait générateur ou élargir la franchise ici reviendrait à modifier le minimum international que is_distribution maintient expressément, sans coordination supérieure établie. Aucun agrément, justificatif, dépôt autonome ou prélèvement accessoire supprimable n'est énoncé. Il n'est pas produit de nouveau texte stylistique.",
    "Contrôle des deux paragraphes et de la note entière. Conserver exactement : seuil inclusif de 750 millions, deux exercices sur les quatre précédents, chiffre d'affaires consolidé incluant les entités de 223 VL bis, ajustement proportionnel propre à chacun des exercices supérieurs ou inférieurs à douze mois. Renvois croisés contrôlés dans 223 VK, 223 VL bis, 223 VJ et 223 WF ; la règle spéciale de scission de 223 WL quater n'est pas effacée. La note vise les exercices ouverts à compter du 31 décembre 2023, pas une date d'entrée en vigueur de la réforme future. Le calcul annuel du minimum ne recrée pas un IS ordinaire annuel sur les bénéfices conservés. La déclaration de résultat mentionnée par 223 WW I et son articulation avec le nouvel IS relèvent de ce dernier article, hors lot ; aucune suppression de ses formalités n'est réputée réalisée ici. Pas de chiffrage ni de conformité européenne nouvelle présumés.",
    "Aucun changement par rapport à la source officielle entière : champ, seuil et règle de proportionnalité sont maintenus. Leur nécessité tient au maintien décidé du minimum international et à sa limitation aux grands groupes ; aucune baisse de prélèvement ni simplification n'est comptée.",
    "Concerne seulement l'impôt complémentaire et les entités visées, avec les exclusions et règles spéciales du chapitre. Aucun zéro d'impôt total des grands groupes ni coordination achevée du nouvel IS n'est démontré ; les autres entreprises ne sont pas rendues imposables par ce maintien.",
    "Aucune charge nouvelle identifiée : le texte source est maintenu sans nouveau dépôt, donnée, autorisation, condition ni échéance. Le calcul de champ déjà applicable demeure ; aucun bilan global de coût des codes n'est déduit de ce maintien.",
    "Le seuil de 750 millions et le test de deux exercices sur quatre continuent d'écarter du champ ordinaire du chapitre les groupes qui ne les atteignent pas, sous réserve de ses règles spéciales. L'ajustement proportionnel des exercices atypiques et les exclusions personnelles de 223 VL bis restent applicables aux situations futures ; inclure leur chiffre d'affaires ne supprime pas ces exclusions."
))

answers.append(retained(
    '223 VL bis',
    "Maintien intégral d'exclusions favorables nécessaires alors que l'impôt complémentaire subsiste. Le 1° protège les six catégories désignées ; les 2° et 3° étendent l'exclusion aux entités détenues répondant respectivement aux seuils de 95 % et 85 %, avec leurs chaînes de détention et critères propres. Retrancher ces catégories ou leurs branches alternatives serait une hausse de charge pour des situations futures éligibles, contraire à cuts_and_reliefs_2026_10_19. Les conditions de détention, d'activité et de composition du résultat délimitent ces avantages ; elles ne constituent ni un agrément fiscal ni une déclaration redondante à supprimer. Aucune reformulation ni nouvelle obligation de preuve n'est ajoutée.",
    "Lecture des six paragraphes et de la note entière. Vérification des définitions de 223 VK : 9°, 11°, 18°, 19°, 24°, 25°, 35°, 36° et 48°. Le fonds d'investissement et le véhicule immobilier du 1° doivent être mères ultimes ; cette qualification n'est pas étendue aux autres catégories. Les 2° et 3° gardent mot pour mot leurs réserves relatives aux entités de services de fonds de pension. Le 2° conserve l'alternative a/b, l'objet exclusif ou presque exclusif du a et les activités exclusivement accessoires du b ; le 3° garde la quasi-totalité du résultat et les dividendes ou plus ou moins-values exclus. Le renvoi aux 2° et 3° de 223 VO a été vérifié : ces dispositions définissent précisément les dividendes et gains ou pertes sur participation exclus, dont 223 VO bis tire les corrections. 223 VL conserve le chiffre d'affaires des entités exclues pour le seuil, sans les soumettre elles-mêmes à l'impôt. L'option contraire de 223 VL ter reste volontaire. La note du 31 décembre 2023 est préservée.",
    "Aucun changement par rapport à la source entière : les exclusions demeurent intégralement, y compris leurs extensions et conditions. Le maintien évite de retirer un avantage pendant que la charge générale subsiste ; il n'est pas présenté comme une nouvelle exonération ou baisse.",
    "Les exclusions sont celles du minimum international, et non une exemption générale de tout impôt pour les organismes concernés. Les seuils de détention, conditions d'activité et options du chapitre subsistent ; aucune réduction nette des charges nationales n'est évaluée.",
    "Aucune charge nouvelle identifiée : les exclusions restent de plein droit dans leurs conditions existantes, sans dossier, agrément, certificat, registre ou déclaration supplémentaire créé par la proposition de maintien.",
    "Maintien pour les futures situations éligibles des entités publiques, organisations internationales, organismes non lucratifs, fonds de pension, fonds d'investissement mères ultimes et véhicules immobiliers mères ultimes. Maintien également des branches à 95 % et 85 %, des détentions indirectes admissibles, des activités accessoires et de l'exclusion fondée sur les dividendes ou plus ou moins-values exclus. Les réserves concernant les services de fonds de pension ne sont ni étendues ni supprimées ; aucun avantage n'est limité aux seules entités déjà existantes."
))

answers.append(retained(
    '223 VL ter',
    "Maintien utile intégral de l'option volontaire et de sa stabilité pluriannuelle dans le minimum international. L'exclusion de 223 VL bis reste la règle par défaut ; seule l'entité déclarante peut choisir de ne pas l'appliquer aux entités de ses 2° et 3°. L'option utilise déjà la déclaration commune, sa reconduction tacite évite un renouvellement exprès et la renonciation ne demande aucun dossier séparé. Les deux périodes de cinq exercices stabilisent la qualification fiscale et évitent des alternances annuelles opportunistes de périmètre. Leur suppression isolée changerait le régime du minimum expressément conservé, sans coordination de son cadre supérieur démontrée. Aucun droit d'option ni avantage futur n'est fermé et aucun agrément n'est substitué au mécanisme.",
    "Vérification des quatre paragraphes et de la note. Garder deux durées distinctes de cinq exercices : durée de validité à compter du premier exercice d'option, puis interdiction de nouvelle option au titre des cinq exercices suivant le dernier exercice d'application en cas de renonciation. La formulation initiale figure sur la déclaration du premier exercice ; la renonciation sur celle du dernier, sans préavis nouveau. 223 WW II, lu en entier avec les autres divisions de l'article, prévoit la déclaration d'informations de l'impôt complémentaire ; le renvoi reste opérant malgré le nouvel IS. Les délais déclaratifs propres à 223 WW ne sont pas réécrits ici. Une réforme du cycle de l'option devrait vérifier le cadre de la directive (UE) 2022/2523 et ses coordinations ; le texte intégral de cette directive n'est pas disponible dans le lot et aucune validation européenne n'est revendiquée. La date source des exercices ouverts à compter du 31 décembre 2023 reste à son champ propre.",
    "Aucune suppression réelle par rapport à la source complète. L'option, la reconduction tacite, la renonciation et les périodes de stabilité sont conservées comme éléments du minimum international. Ce maintien n'est compté ni comme formalité fusionnée ni comme baisse fiscale.",
    "Seules les entités des 2° et 3° de 223 VL bis sont concernées par cette faculté, pas celles du 1°. L'avantage économique d'une option dépend de la situation du groupe ; il n'est pas garanti. La possibilité de réduire les cycles au regard du droit supérieur n'est pas démontrée dans le contexte documentaire local.",
    "Aucune charge nouvelle identifiée : option et renonciation restent portées par la déclaration existante, avec reconduction tacite. Aucune confirmation annuelle, pièce, autorisation ou nouvelle période de blocage n'est introduite.",
    "La faculté de choisir un traitement non exclu est conservée pour toutes les entités futures éligibles des 2° et 3° ; ce choix peut être utile au groupe sans être systématiquement fiscalement favorable. L'exclusion par défaut, la renonciation et la reconduction tacite restent intactes. Les périodes de cinq exercices ne constituent pas des avantages fiscaux autonomes mais les conditions existantes de stabilité du choix ; elles ne sont ni allongées ni converties en délais de déclaration supplémentaires."
))

answers.append(retained(
    '223 VM',
    "Maintien intégral des critères de localisation nécessaires au calcul territorial du minimum international. Le I utilise l'assujettissement légal à raison du siège, de la création ou de critères similaires, puis subsidiairement le lieu de création. Le II règle les entités interposées avec les exceptions propres aux mères ultimes et aux entités devant appliquer l'inclusion du revenu. Ces règles évitent une localisation discrétionnaire ou multiple ; les supprimer ne retirerait pas une formalité mais désorganiserait l'affectation du minimum maintenu. Aucun agrément, paiement accessoire, justificatif répétitif, durée minimale ni déclaration autonome ne figure dans cet article. Aucun nouveau corps à droit constant n'est fabriqué.",
    "Lecture intégrale des trois paragraphes I/II et de la note. Le mot passible n'impose pas le paiement effectif d'un IS chaque année : l'absence de distribution dans le nouvel IS ne fait pas automatiquement perdre la localisation française. 223 VK 14° et 14° bis conservent les qualifications, avec coordination explicite des renvois à la transparence dans ce lot. 223 WG, lu intégralement, définit bien les redevables de la règle d'inclusion ; son renvoi n'est pas orphelin. Articulation vérifiée avec 223 VM bis/ter/quater, ainsi qu'avec 223 VM quinquies (règle de l'autre Etat sous réserve conventionnelle) et 223 VM sexies (appréciation au premier jour de l'exercice). La règle ne fixe pas à elle seule la résidence pour les autres impôts ou conventions. La note d'application aux exercices ouverts à compter du 31 décembre 2023 n'est pas une transition de la réforme future.",
    "Aucun changement réel par rapport à la source entière : les critères d'attribution territoriale et les exceptions aux entités apatrides sont conservés. Leur fonction est nécessaire au minimum maintenu, sans nouvelle réduction de prélèvement ou de formalité.",
    "L'effet est limité au présent chapitre ; ni résidence conventionnelle générale ni impôt personnel des associés ne sont modifiés. Les conséquences chiffrées de la localisation dépendent des autres articles et ne sont pas établies pour chaque groupe.",
    "Aucune charge nouvelle identifiée : les critères légaux et exceptions existants restent identiques, sans demande, certificat de résidence nouveau, registre, donnée supplémentaire ou échéance ajoutée.",
    "Le critère subsidiaire du lieu de création et les exceptions du II pour les mères ultimes ou entités soumises à l'inclusion restent accessibles aux situations futures. Ils sont des règles d'affectation, non des exonérations générales. Aucun traitement protecteur contre une mauvaise qualification d'entité apatride n'est retiré et aucune imposition n'est ajoutée en raison de la seule rétention des bénéfices."
))

answers.append(retained(
    '223 VM bis',
    "Maintien utile intégral des quatre règles de localisation des établissements stables. Les branches correspondent exactement aux quatre catégories du 20° de 223 VK : convention fiscale, imposition comparable des résidents sans convention, implantation dans un territoire sans impôt sur les bénéfices, enfin établissement considéré comme apatride. Fusionner ces branches en une règle unique effacerait des qualifications différentes et pourrait déplacer le minimum international. Aucune charge administrative, autorisation, pièce redondante, délai minimal ou taxe accessoire autonome n'est institué ici ; il n'est donc pas produit de reformulation présentée comme une coupe.",
    "Contrôle de l'introduction, des quatre paragraphes numérotés et de la note. Chaque lettre a/b/c/d du 20° de 223 VK a été lue et confrontée à son 1°/2°/3°/4° correspondant ; les renvois restent cohérents. Au 1°, conserver la double condition de reconnaissance et d'imposition conventionnelles ; au 2°, le lien à l'installation d'affaires et au mode d'imposition des résidents ; au 3°, le lieu de l'installation ; au 4°, la qualification apatride. La temporalité reste complétée par 223 VM sexies, lu dans le corpus. Ces règles ne rétablissent aucun IS annuel ordinaire, mais gardent leur rôle dans 223 WF. Les conventions effectivement applicables à chaque groupe ne sont pas jointes : aucun contrôle individuel conventionnel n'est déclaré achevé. La note vise les exercices ouverts à compter du 31 décembre 2023.",
    "Aucun changement par rapport à la source officielle entière : quatre critères territoriaux différenciés sont maintenus, pour éviter un vide de localisation du minimum international. Aucun gain fiscal ou administratif nouveau n'est attribué à ce maintien.",
    "Ne concerne que les établissements stables définis au 20° de 223 VK et le chapitre du minimum. La résidence du siège, les autres impôts et les conventions individuelles restent à leur champ ; le coût fiscal de chaque localisation n'est pas chiffré.",
    "Aucune charge nouvelle identifiée : les quatre rattachements légaux subsistent sans procédure d'autorisation, déclaration de remplacement, certificat, délai ou information additionnelle imposé par cet article.",
    "Les rattachements conventionnels et l'implantation dans un Etat sans impôt sur les bénéfices restent reconnus pour les futurs établissements répondant aux conditions. Ils ne valent pas exonération universelle du minimum. Aucun droit conventionnel ni exception de qualification n'est supprimé sous couvert de simplifier les quatre branches."
))

answers.append(retained(
    '223 VM ter',
    "Maintien intégral de la priorité conventionnelle et des deux cas limités de recours à la règle subsidiaire. Pour une entité située dans deux Etats liés par convention, le rattachement conventionnel doit demeurer ; il peut protéger contre une localisation cumulative. L'absence d'accord amiable requis ou l'absence d'élimination de la double imposition justifient la solution subsidiaire de 223 VM quater. Le texte n'impose ni demande d'agrément, ni autorisation, ni justificatif supplémentaire, ni délai minimal : la mention d'un accord entre autorités est un critère d'application d'une convention existante. Aucun tel accord n'est remplacé par une déclaration et aucune procédure étrangère n'est réputée abrogée.",
    "Lecture des quatre paragraphes et de la note. Le premier alinéa conserve l'application de la convention fiscale ; le 1° exige cumulativement qu'elle prévoie un accord amiable et qu'aucun accord ne soit conclu ; le 2° est une autre hypothèse, sans exigence d'accord ajoutée. 223 VM quater a été confronté intégralement : sa règle subsidiaire est aussi applicable par le présent renvoi lorsque la convention n'apporte pas la solution requise. Les textes 223 VM quinquies et sexies du corpus gardent respectivement la réserve conventionnelle de l'inclusion et la date de localisation. Aucune convention particulière, ni procédure amiable correspondante, n'est jointe ; elles ne sont pas présentées comme modifiées ou vérifiées individuellement. La note conserve les exercices ouverts à compter du 31 décembre 2023.",
    "Aucun changement de la source complète : priorité de la convention et cas subsidiaires restent entiers. Ce maintien protège la cohérence du rattachement territorial ; il n'est pas une nouvelle exonération ni la suppression d'une démarche conventionnelle.",
    "Concerne les doubles localisations dans le seul minimum international, sous conventions existantes. L'élimination effective de chaque double imposition dépend de la convention et du reste du chapitre ; elle n'est pas démontrée pour tous les groupes.",
    "Aucune charge nouvelle identifiée : aucun dépôt, accord privé, demande d'autorisation, justificatif, donnée, registre ou délai n'est créé. Les accords entre autorités éventuellement exigés par les conventions conservent leur fondement distinct.",
    "Le bénéfice du rattachement résidentiel prévu par une convention est conservé pour les situations futures comme pour les situations déjà couvertes. Les deux renvois subsidiaires n'effacent ni le contenu des conventions ni les voies amiables disponibles. L'article n'institue pas en lui-même un crédit remboursable ou une exonération d'impôt supplémentaire."
))

answers.append(retained(
    '223 VM quater',
    "Maintien utile intégral de la cascade de rattachement subsidiaire. Le montant des impôts couverts, hors impôts sur sociétés étrangères contrôlées, départage d'abord les deux Etats ; l'égalité ou la nullité conduit à comparer la déduction fondée sur la substance, puis à la qualification apatride, avec exception pour la mère ultime située au lieu de création. Cette hiérarchie évite un choix libre de localisation et préserve le rôle de la substance. Elle ne crée aucune déclaration, autorisation ou pièce autonome que l'on pourrait supprimer. Retirer une étape modifierait la territorialité du minimum maintenu et non un simple doublon administratif. Aucun nouveau corps stylistique n'est proposé.",
    "Relecture des quatre paragraphes et de la note. Le premier critère est un montant d'impôts couverts de l'exercice, non un taux nominal ni la totalité des impôts payés. Le paragraphe 1 de la sous-section 2 de la section III comprend 223 VS et 223 VS bis, lus intégralement ; les définitions de 223 VK 30° à 32° restent coordonnées. L'exclusion des impôts de sociétés étrangères contrôlées est conservée au deuxième alinéa. La déduction fondée sur la substance du troisième alinéa est calculée pour chaque entité selon la sous-section 1 de la section IV : ce critère de rattachement ne supprime ni ne modifie la déduction elle-même. Maintien des deux tests identique ou nul et de l'exception finale de la mère ultime. Le renvoi de 223 VM ter étend l'emploi de cette règle à ses deux cas conventionnels ; 223 VM quinquies et sexies gardent leur application distincte. Le calcul détaillé de la déduction et les montants propres à chaque groupe ne sont pas audités ici. La note du 31 décembre 2023 demeure applicable.",
    "Aucun changement matériel par rapport à la source entière : la hiérarchie de localisation, l'exclusion des impôts de sociétés étrangères contrôlées et l'exception des mères ultimes demeurent. Ce n'est ni une taxe supprimée ni un nouvel allègement de la déduction fondée sur la substance.",
    "S'applique aux doubles localisations sans convention et aux cas renvoyés par 223 VM ter. Les effets individuels dépendent des impôts couverts et de la déduction de chaque entité ; aucun avantage fiscal systématique, solde budgétaire ou baisse générale de complexité n'est établi.",
    "Aucune charge nouvelle identifiée : la règle source est maintenue sans nouveau registre, justificatif, relevé, autorisation ou délai. La comparaison utilise les éléments du minimum déjà requis ; aucun nouveau reporting n'est institué par ce maintien.",
    "La déduction fondée sur la substance reste entière dans son régime propre ; sa comparaison ici n'en est pas une nouvelle attribution ni une réduction. L'exclusion des impôts de sociétés étrangères contrôlées pour le premier départage et le rattachement au lieu de création de la mère ultime à égalité finale restent ouverts aux situations futures. Aucun avantage de rattachement n'est limité aux situations anciennes et aucune imputation ou exonération du chapitre n'est supprimée."
))

assert len(answers) == len(sources) == 8
for a, s in zip(answers, sources):
    assert all(a[k] == s[k] for k in ('code_id', 'source_id', 'source_sha256', 'number'))
Path('answer.json').write_text(json.dumps(answers, ensure_ascii=False, indent=2) + '\n')
