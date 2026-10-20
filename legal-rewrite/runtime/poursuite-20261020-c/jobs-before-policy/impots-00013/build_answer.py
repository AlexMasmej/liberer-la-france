import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
proposals = {}


def add(number, xml, reason, review):
    proposals[number] = (xml.strip(), reason, review)


add('80 sexdecies', '''
<p>Les sommes mentionnées au 2° de l'article L. 3332-11 du code du travail sont soumises à l'impôt sur le revenu selon les règles des traitements et salaires. Toutefois, celles qui n'excèdent pas le plafond prévu à ce même 2° sont exonérées dans les conditions du a du 18° de l'article 81 du présent code.</p>
''',
    "À droit constant, séparation de la règle d'imposition et de l'exception liée au plafond de l'abondement. Les deux renvois qui déterminent le champ de l'exonération sont conservés. Aucune réforme de fond n'est introduite dans ce régime d'épargne salariale.",
    "Renvoi vérifié dans le corpus public : le 2° de l'article L. 3332-11 du code du travail comporte le plafond de 30 % du plafond annuel de la sécurité sociale et prévoit l'imposition des sommes excédentaires par renvoi au présent article. Le montant n'est pas dupliqué dans le texte proposé ; coordination conservée avec le a du 18° de l'article 81. Ce dispositif n'est pas assimilé au nouveau compte de retraite.")

add('81', Path('fragments/81-a.xml').read_text() + Path('fragments/81-b.xml').read_text(),
    "Réécriture à droit constant de l'ensemble des 97 alinéas : décomposition des conditions des allocations pour frais, explicitation des fractions exonérées des capitaux de retraite, clarification des plafonds et cumuls de transport, des affectations d'épargne et de l'option des étudiants. Les numéros, lettres, emplacements abrogés ou périmés, renvois et régimes historiques sont conservés. Aucune exonération n'est ajoutée pour le nouveau compte de retraite et aucune baisse de CSG n'est appliquée aux prestations énumérées.",
    "Les 97 alinéas restent dans l'ordre source. Le renvoi du 18° a ter au troisième alinéa du 2° de l'article 83 est conservé, de même que les autres limites d'épargne. Contrôles particuliers : 7 650 €, seuil de revenu de 93 510 €, 17 %, une fois et demie ce montant, 38,75 %, communes de moins de 3 500 habitants ; exonération de 50 % des seules indemnités temporaires au 8° ; dix jours au 18° b bis ; 7,32 € et indexation des titres-restaurant ; plafonds de 600 €, 300 €, maximum de 900 € ou de l'avantage du a, et 310 € au 19° ter. Les dates de 1991, 2018 et du 31 décembre 2022 sont maintenues dans leurs régimes historiques. Les notes source rattachent la rédaction issue de l'article 9 de la loi n° 2026-103 au 1er janvier 2026 et la modification du c du 19° ter issue de la loi n° 2021-1900 aux revenus de 2022 : elles ne datent aucune réforme future. La source porte un état ABROGE_DIFF avec échéance au 1er janvier 2029 ; la présente proposition reprend intégralement la version assignée sans anticiper sa succession. Le repère (1) du 31° bis n'a pas de note explicative correspondante dans les notes fournies : anomalie conservée et signalée. Pour la capitalisation nouvelle, une disposition fiscale propre devra déterminer le traitement des contributions patronales, des produits et des sorties, en coordination avec les articles 79, 81, 83 et 158 du CGI ; les exonérations actuelles des PER et contrats de retraite ne lui sont pas étendues automatiquement.")

add('81 bis', '''
<p>Dans la limite du montant annuel du salaire minimum de croissance, sont exonérés de l'impôt sur le revenu les salaires versés aux apprentis dont le contrat remplit les conditions du code du travail, ainsi que la gratification prévue à l'article L. 124-6 du code de l'éducation, versée aux stagiaires au titre d'un stage ou d'une période de formation en milieu professionnel. Cette exonération s'applique que l'apprenti ou le stagiaire soit imposable personnellement ou qu'il soit à la charge d'un autre contribuable.</p>
''',
    "À droit constant, placement de la limite annuelle en tête de phrase et clarification des deux catégories de rémunération ainsi que des modalités d'imposition du bénéficiaire. Le seuil reste le SMIC annuel sans montant chiffré ajouté.",
    "Le renvoi à l'article L. 124-6 du code de l'éducation et l'exigence d'un contrat d'apprentissage conforme au code du travail sont conservés. Ne pas confondre cette exonération avec celle, optionnelle et plafonnée à trois SMIC mensuels, prévue au 36° de l'article 81 pour certains étudiants.")

add('81 ter', '''
<p>Sont exonérés de l'impôt, dans une limite annuelle de 460 € :</p>
<p>1. (Sans objet) ;</p>
<p>2. Les montants prélevés sur les salaires pour souscrire des parts sociales que les sociétés coopératives de production émettent exclusivement à destination de leurs salariés, dans les conditions des articles 35 à 44 de la loi n° 78-763 du 19 juillet 1978 portant statut de ces sociétés.</p>
''',
    "À droit constant, formulation directe de l'exonération et de l'objet des prélèvements sur salaire. Conservation des subdivisions 1 et 2 et du plafond annuel de 460 € ; seuls les sauts de ligne de présentation superflus sont supprimés.",
    "Les références aux articles 35 à 44 de la loi n° 78-763 sont maintenues. Les notes source relatent des modifications de coordination issues des lois du 19 février 2001 et du 31 juillet 2014 ; aucune entrée en vigueur nouvelle n'en est déduite. Ne pas assimiler ces souscriptions au versement complémentaire exonéré au 17° ter de l'article 81.")

add('81 quater', '''
<p>I. – Les rémunérations, majorations et éléments de rémunération mentionnés aux I et III de l'article L. 241-17 du code de la sécurité sociale sont exonérés de l'impôt sur le revenu, dans les conditions et limites prévues à ce même article et dans la limite de 7 500 € par an.</p>
<p>II. – (Abrogé).<br/><br/>III. – Pour bénéficier de cette exonération, la condition prévue au V de l'article L. 241-17 du code de la sécurité sociale doit être respectée.</p>
''',
    "À droit constant, mise en évidence du plafond annuel et formulation directe de la condition anti-substitution. Les I, II et III, ainsi que les deux paragraphes et les renvois à l'article L. 241-17, sont conservés. La réforme de la durée du travail produit ses effets par la définition des heures éligibles dans les textes auxquels cet article renvoie ; aucun seuil fiscal autonome n'est créé.",
    "L'article L. 241-17 du CSS a été consulté : son I renvoie notamment aux articles L. 3121-28 à L. 3121-39, son V prévoit la condition de non-substitution et le délai de douze mois. Coordonner son application avec les nouveaux contrats soumis au seuil hebdomadaire de quarante heures et les contrats antérieurs conservant trente-cinq heures, conformément à coordination.json. Les heures de la 36e à la 40e des seuls nouveaux contrats soumis au nouveau seuil ne deviennent pas fiscalement exonérées au seul motif de leur paiement. Conserver les régimes annuels ou plurihebdomadaires à 1 607 heures et les régimes particuliers, dont les heures complémentaires ; aucune extension aux agents publics ou aux contrats anciens ne résulte de cette réécriture. La note source maintient l'application aux heures supplémentaires et complémentaires réalisées à compter du 1er janvier 2022. Plafond inchangé de 7 500 €.")

add('81 A', '''
<p>I. – Les personnes domiciliées en France au sens de l'article 4 B qui exercent une activité salariée peuvent être exonérées d'impôt sur le revenu sur les salaires rémunérant leur activité dans l'État où leur employeur les envoie. Cet État doit être distinct de la France et de l'État d'établissement de l'employeur.</p>
<p>L'employeur doit être établi en France, dans un autre État membre de l'Union européenne ou dans un autre État partie à l'accord sur l'Espace économique européen ayant conclu avec la France une convention d'assistance administrative destinée à lutter contre la fraude et l'évasion fiscales.</p>
<p>Pour bénéficier de l'exonération prévue au premier alinéa, les personnes concernées doivent justifier qu'elles remplissent l'une des conditions suivantes :</p>
<p>1° Les rémunérations concernées ont été effectivement soumises à un impôt sur le revenu dans l'État d'exercice de l'activité. Cet impôt doit être au moins égal aux deux tiers de l'impôt qui aurait été dû en France sur la même base d'imposition ;</p>
<p>2° L'activité salariée a été exercée dans les conditions des premier et deuxième alinéas :</p>
<p>– soit pendant plus de cent quatre-vingt-trois jours au cours d'une période de douze mois consécutifs, dans l'un des domaines suivants :</p>
<p>a) Chantiers de construction ou de montage, installation d'ensembles industriels, mise en route et exploitation de ces ensembles, ainsi que l'ingénierie qui s'y rapporte ;</p>
<p>b) Recherche ou extraction de ressources naturelles ;</p>
<p>c) Navigation à bord de navires armés au commerce et immatriculés au registre international français ;</p>
<p>d) Navigation à bord de navires armés au commerce et immatriculés à Wallis-et-Futuna ;</p>
<p>– soit pendant plus de cent vingt jours au cours d'une période de douze mois consécutifs, pour une activité de prospection commerciale.</p>
<p>Le 2° ne s'applique ni aux travailleurs frontaliers ni aux agents de la fonction publique.</p>
<p>II. – Lorsque les personnes mentionnées au premier alinéa du I ne remplissent aucune des conditions prévues aux 1° et 2° de ce I, les suppléments de rémunération qui leur sont éventuellement versés pour leur séjour dans un autre État sont exonérés d'impôt sur le revenu en France s'ils remplissent toutes les conditions suivantes :</p>
<p>1° Ils sont versés en contrepartie de séjours effectués dans l'intérêt direct et exclusif de l'employeur ;</p>
<p>2° Ils sont justifiés par un déplacement nécessitant une résidence effective d'au moins vingt-quatre heures dans un autre État ;</p>
<p>3° Leur montant est fixé avant les séjours dans un autre État, en fonction, d'une part, du nombre, de la durée et du lieu des séjours et, d'autre part, de la rémunération du salarié, hors suppléments mentionnés au premier alinéa. Le total de ces suppléments ne peut dépasser 40 % de cette rémunération hors suppléments.</p>
''',
    "Réécriture à droit constant en séparant la destination du détachement, l'établissement de l'employeur, les deux voies alternatives d'exonération et les trois conditions cumulatives des suppléments de rémunération. Maintien des seize alinéas, des domaines d'activité et des exclusions du seul 2°.",
    "Conservation des seuils stricts de plus de cent quatre-vingt-trois jours et de plus de cent vingt jours sur douze mois consécutifs, du minimum de vingt-quatre heures, de l'impôt étranger au moins égal aux deux tiers et du plafond de 40 % calculé hors suppléments. L'exigence de convention d'assistance administrative reste attachée aux autres États de l'EEE visés par la source. Le d) relatif à Wallis-et-Futuna est conservé. La note source fixe au 1er janvier 2026 l'application de la rédaction résultant de l'article 3 de la loi n° 2026-103 ; elle n'est pas transformée en date de réforme du projet.")

add('81 D', '''
<p>Les salariés et dirigeants appelés de l'étranger pour occuper un emploi auprès de la Chambre de commerce internationale en France sont exonérés d'impôt sur le revenu sur les traitements et salaires versés au titre de cet emploi.</p>
<p>Cette exonération est subordonnée à l'absence de domicile fiscal en France pendant les cinq années civiles précédant l'année de la prise de fonctions. Elle s'applique jusqu'au 31 décembre de la cinquième année civile suivant celle de cette prise de fonctions, pour les années au titre desquelles les personnes concernées sont fiscalement domiciliées en France au sens des a et b du 1 de l'article 4 B.</p>
<p>Les salariés et les personnes mentionnés au premier alinéa ne peuvent bénéficier de l'article 155 B.</p>
''',
    "À droit constant, séparation de la condition de résidence antérieure et de la durée d'exonération. Le champ propre aux emplois de la Chambre de commerce internationale et l'exclusion du régime de l'article 155 B restent explicites, dans les trois alinéas d'origine.",
    "Conserver cinq années civiles antérieures et l'échéance du 31 décembre de la cinquième année civile suivant la prise de fonctions, ainsi que les a et b du 1 de l'article 4 B. Ce régime spécial ne reçoit ni les paramètres du compte de retraite ni ceux d'un autre régime d'impatriation.")

add('82', '''
<p>Les bases d'imposition comprennent le montant net des traitements, indemnités, émoluments, salaires, pensions et rentes viagères, ainsi que tous les avantages en argent ou en nature accordés aux bénéficiaires en complément de ces revenus. Toutefois, les logements mis à la disposition des personnels de la gendarmerie dans les conditions de l'article D. 14 du code du domaine de l'État ou de l'article D. 2124-75 du code général de la propriété des personnes publiques ne constituent pas un avantage en nature.</p>
<p>Les rémunérations versées sous forme d'avantages en nature sont évaluées selon les règles de calcul des cotisations de sécurité sociale prévues à l'article L. 242-1 du code de la sécurité sociale ou à l'article L. 741-10 du code rural et de la pêche maritime.</p>
''',
    "À droit constant, suppression de la répétition de la liste des revenus et identification directe des éléments de la base d'imposition. Les deux alinéas, l'exception pour les logements de la gendarmerie et les deux règles de renvoi pour l'évaluation des avantages en nature sont maintenus.",
    "Le renvoi à l'article D. 14 du code du domaine de l'État, ancien code, figure encore dans la source à côté du renvoi au code général de la propriété des personnes publiques : il est conservé et son maintien formel appelle un contrôle de coordination. La note source rattache cette rédaction aux articles 2 et 3-I [2°] du décret n° 2011-1612 du 22 novembre 2011. Aucun changement d'assiette n'est déduit de la baisse proposée de CSG ou du transfert de cotisations vieillesse.")

add('83', Path('fragments/83.xml').read_text(),
    "À droit constant, clarification du calcul des plafonds de prévoyance et de retraite supplémentaire, des dépenses professionnelles, du barème kilométrique et des exclusions de déduction des intérêts. Les 33 alinéas et leurs subdivisions sont maintenus. Coordination de fond de la réforme des retraites au 1° : la fraction salariale de cotisations vieillesse transférée vers le compte personnel de capitalisation collective reste déductible une seule fois, dans le seul champ des salariés du régime général employés par une personne de droit privé et lors de la mise en œuvre prévue à l'article L. 241-3 du CSS. Les PER et les contrats antérieurs gardent leurs régimes propres.",
    "La précision nouvelle du 1° doit entrer en application en même temps que le transfert prévu par la rédaction coordonnée de l'article L. 241-3 du CSS, après satisfaction de ses préalables de financement et de gouvernance, sans supposer ces conditions déjà remplies. Elle ne crée aucune déduction pour les parts patronales, les produits ou les sorties du nouveau compte. Ce régime de capitalisation nécessite encore des dispositions législatives propres sur le véhicule de placement, la séparation des actifs, la gouvernance, la diversification et les frais dans le code monétaire et financier et, selon le véhicule retenu, les codes des assurances ou de la mutualité ; aucun numéro d'article nouveau n'est inventé. Le traitement fiscal des contributions patronales, des produits et des sorties doit être arrêté dans les articles pertinents du CGI, notamment 81, 83 et 158, sans appliquer automatiquement les régimes d'épargne existants. Déductibilité de la CSG à coordonner exclusivement avec l'article 154 quinquies selon coordination.json : montant effectivement acquitté sur l'assiette après abattements, sans déduction supérieure à la contribution payée ; aucun calcul sur le brut n'est ajouté ici. Les renvois au quatrième alinéa du 1° quater, aux troisième et dernier alinéas du 2° et au huitième alinéa du 3° gardent leurs cibles. Le sixième alinéa de l'article L. 242-1 du CSS, visé au 1° quater, correspond dans la version consultée du corpus au 4° du II sur la protection sociale complémentaire collective et obligatoire : renvoi conservé, à maintenir sur cette cible lors des autres réécritures. Le règlement CEE n° 1408/71 reste cité au 1° 0 bis comme dans la source ; ce renvoi historique ne fait pas l'objet d'une actualisation silencieuse. Montants et formules conservés : 5 % du PASS plus 2 % du brut, plafond de 2 % de huit PASS ; 8 % du brut limité à huit PASS ; huitième année d'impatriation ; premiers 1 000 € de rente ; 10 %, 14 555 € pour les revenus de 2025 et minimum de 509 €, avec les indexations d'origine. La formulation source laisse le cas d'une distance exactement égale à quarante kilomètres sans mention expresse entre « moins de » et « supérieure » : rédaction préservée sur ce point et ambiguïté signalée. Le renvoi du calcul forfaitaire aux 1° à 2° ter mentionne encore des intérêts et une subdivision abrogée : il est maintenu, sans extension implicite. Dates du 1er janvier 1993 et du 1er janvier 2026 conservées pour les régimes sportifs ; note source de coordination avec l'article 4-I B 1° a de la loi n° 2026-103 prise en compte.")

add('83 A', '''
<p>Le montant brut des pensions versées par un débiteur établi ou domicilié en France métropolitaine bénéficie d'un abattement de 40 % lorsque leurs bénéficiaires ont leur domicile fiscal en Polynésie française, aux îles Wallis et Futuna, dans les Terres australes et antarctiques françaises ou en Nouvelle-Calédonie.</p>
''',
    "À droit constant, identification du montant auquel s'applique l'abattement puis de la condition de domicile fiscal du bénéficiaire. Le taux de 40 % et tous les territoires sont conservés.",
    "L'abattement porte sur le montant brut des pensions ; le débiteur doit être établi ou domicilié en France métropolitaine. Ce régime fiscal territorial ne met pas en œuvre le gel temporaire de revalorisation des pensions prévu par le projet, lequel relève de la coordination sociale et non d'une modification de cet abattement.")

add('84 A', '''
<p>Les règles de l'article 100 bis du présent code s'appliquent, dans les mêmes conditions, à la détermination des salaires imposables des artistes du spectacle titulaires d'un contrat relevant des articles L. 7121-3 à L. 7121-7 du code du travail, ainsi qu'à celle des salaires imposables perçus par les sportifs au titre de la pratique d'un sport.</p>
''',
    "À droit constant, formulation directe du renvoi à l'article 100 bis et distinction lisible des salaires des artistes et de ceux des sportifs. Les conditions du régime de référence et les articles du code du travail restent inchangés.",
    "L'article 100 bis a été consulté dans le corpus : il prévoit notamment les périodes de moyenne et les règles d'option. Le renvoi global est maintenu afin de ne pas isoler le calcul de ses conditions. La note source renvoie à la recodification opérée par les articles 1er, 3 et 12-I de l'ordonnance n° 2007-329 du 12 mars 2007 ; aucune réforme de fond nouvelle n'en résulte.")

add('86', '''
<p>Pour chaque bénéficiaire d'un paiement imposable, la personne physique ou morale qui verse la somme doit inscrire les informations suivantes dans le livre, fichier ou autre document d'enregistrement de la paye ou, à défaut, dans un livre spécial (1) :</p>
<p>– la date, la nature et le montant du paiement ;</p>
<p>– le nombre de personnes que le bénéficiaire déclare à sa charge.</p>
''',
    "À droit constant, identification du débiteur de l'obligation et présentation directe des informations à enregistrer pour chaque bénéficiaire. Les trois alinéas et le caractère déclaratif des personnes à charge sont conservés.",
    "La note (1) vise les articles L82 B et L102 B du livre des procédures fiscales : leurs obligations de communication et de conservation restent à coordonner. La réutilisation administrative prévue à l'article 87 proposé ne supprime pas cette obligation de tenue des documents de paye et n'autorise aucun échange de données couvertes par un secret.")

add('87', '''
<p>Toute personne physique ou morale qui verse des traitements, émoluments, salaires ou rétributions imposables doit souscrire, dans les conditions de l'article 87 A, une déclaration dont un décret fixe le contenu (1). Pour établir cette déclaration, l'organisme ou l'administration destinataire réutilise les informations nécessaires qu'il détient déjà légalement, lorsqu'elles sont à jour et répondent aux mêmes exigences déclaratives. Ces informations ne peuvent alors faire l'objet d'une nouvelle demande de transmission au déclarant. Leur réutilisation respecte les finalités pour lesquelles elles peuvent être légalement traitées et les secrets protégés par la loi. Le déclarant et chaque bénéficiaire peuvent accéder aux informations qui les concernent et en demander la rectification, sans accéder aux informations protégées relatives à des tiers.</p>
<p>Pour chaque bénéficiaire appartenant au personnel dirigeant ou aux cadres, la déclaration doit en outre indiquer distinctement les indemnités pour frais d'emploi perçues et les montants alloués ou remboursés au cours de l'année précédente au titre des frais de représentation, de déplacement, de mission et des autres frais professionnels.</p>
''',
    "À droit constant, clarification du débiteur de la déclaration et des montants à distinguer pour les dirigeants et cadres. Réforme de fond de simplification conforme à policy.json : réutilisation par le destinataire des données déjà légalement détenues, à jour et répondant aux mêmes exigences, suppression de leur nouvelle demande de transmission, maintien des finalités légales et des secrets, et accès aux données propres avec demande de rectification. Le support et les échéances restent ceux de l'article 87 A ; aucun nouveau portail n'est créé.",
    "Les deux alinéas et la déclaration distincte des frais de l'année précédente sont conservés. L'article 87 A a été consulté : il organise la transmission mensuelle, notamment via la déclaration sociale nominative, et les déclarations hors de ce champ ; aucune échéance n'est modifiée ici. Coordonner sa mise en œuvre ainsi que le contenu réglementaire de l'article 39 de l'annexe III du CGI avec la réutilisation des données, leur actualisation, l'information des personnes et la rectification auprès de leur source. Le renvoi de la note (1) aux obligations de l'article 240 reste pertinent et n'est pas supprimé par la règle de réemploi. Les secrets fiscaux et sociaux, notamment l'article L. 103 du livre des procédures fiscales, et les règles de protection des données demeurent applicables ; aucune habilitation générale à échanger des données entre administrations n'est créée. Les modalités pratiques de rectification doivent être coordonnées avec les régimes déclaratifs du CSS et le règlement (UE) 2016/679. L'article 86 continue d'imposer la tenue du document de paye.")

assert len(sources) == len(proposals) == 13
answer = []
for source in sources:
    xml, reason, review = proposals[source['number']]
    answer.append({
        **{key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')},
        'proposed_xml': xml,
        'reason': reason,
        'review_notes': review,
        'status': 'rewrite_draft',
    })
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
