import json
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
drafts = {}


def article(number, paragraphs, reason, notes):
    assert number not in drafts
    drafts[number] = {
        'proposed_xml': '\n'.join('<p>' + p + '</p>' for p in paragraphs),
        'reason': reason,
        'review_notes': notes,
    }


article('41 B', [
    "Les versements à fonds perdus mentionnés à l'article 41 A doivent remplir les conditions suivantes :",
    "1° a Les versements effectués par des employeurs assujettis à la participation à l'effort de construction doivent constituer des investissements valables au regard de la réglementation de la participation des employeurs à l'effort de construction ;",
    "b Les versements effectués par les autres employeurs doivent être destinés à permettre la construction d'habitations respectant les caractéristiques et les prix fixés pour l'octroi des primes à la construction ;",
    "2° L'entreprise qui effectue les versements doit perdre complètement et définitivement tout droit sur les sommes versées ;",
    "3° Les dirigeants de l'entreprise qui effectue les versements, au sens du 3 de l'article 39 et de l'article 211 bis du code général des impôts, ainsi que le chef d'entreprise lorsqu'il s'agit d'un exploitant individuel, leurs conjoints et leurs enfants non émancipés, ne doivent retirer aucun avantage de ces versements ;",
    "4° (Abrogé).",
], "Réécriture à droit constant : chaque condition désigne expressément les employeurs ou l'entreprise concernés. Les deux catégories de versements du 1°, la perte définitive des droits et l'interdiction des avantages personnels sont conservées. Aucune réforme de fond n'est appliquée.",
    "Renvoi à l'article 41 A vérifié dans le corpus public. Numérotation 1° a, b, 2°, 3° et emplacement du 4° abrogé conservés. La répétition matérielle « de de » au 3° est supprimée, sans modifier les renvois aux articles 39 et 211 bis. Les références aux primes à la construction et aux catégories historiques d'employeurs sont conservées ; leur éventuelle actualisation exige une coordination distincte.")

article('41 D', [
    "La liste des sociétés et organismes prévue à l'article 39 quinquies du code général des impôts exclut les sociétés qui ne sont pas, par elles-mêmes, passibles de l'impôt sur les sociétés.",
], "Réécriture à droit constant : l'exclusion est énoncée directement à partir de la liste concernée. Le critère d'assujettissement de la société elle-même est maintenu. Aucune réforme de fond n'est appliquée.",
    "Renvoi à l'article 39 quinquies vérifié dans le corpus. L'exclusion ne dépend pas de l'imposition des associés. La modification du taux normal de l'IS prévue par la politique ne modifie pas ce critère d'assujettissement.")

article('41 DA', [
    "Les gestionnaires désignés par la convention ou l'accord agréé qui crée le fonds salarial déclarent chaque année, pour chaque salarié, la nature et la valeur des opérations inscrites au compte ouvert à son nom dans le fonds. Ils distinguent :",
    "1° (Périmé).",
    "2° Les retraits effectués par le salarié au cours de l'année, répartis selon l'origine des sommes déposées ;",
    "3° Les produits servis aux salariés au cours de l'année.",
    "Les gestionnaires portent ces renseignements sur la déclaration prévue au 1 de l'article 242 ter du code général des impôts (1).",
    "(1) Les conditions et délais de cette déclaration sont prévus aux articles 49 D à 49 I de l'annexe III au code général des impôts.",
], "Réécriture à droit constant : l'obligation annuelle et le contenu de la déclaration sont répartis en phrases plus courtes ; le déclarant est nommé dans la phrase relative au support déclaratif. Aucune réforme de fond n'est appliquée.",
    "Le 1° périmé reste à sa place. Les retraits ventilés par origine et les produits servis restent deux rubriques distinctes. Correction grammaticale de « le salariés ». Les renvois au 1 de l'article 242 ter et aux articles 49 D à 49 I sont conservés. Le fonds salarial n'est pas assimilé au compte de capitalisation collective projeté.")

article('41 DGA', [
    "I. – Le taux dérogatoire mentionné au dernier alinéa du b du 2° du 8 du II de l'article 150-0 A du code général des impôts et au dernier alinéa du b du 2° du 1 du II de l'article 163 quinquies C du même code est fixé à 0,25 % du montant total des souscriptions dans un fonds commun de placement à risques, un fonds professionnel spécialisé relevant de l'article L. 214-37 du code monétaire et financier dans sa rédaction antérieure à l'ordonnance n° 2013-676 du 25 juillet 2013 modifiant le cadre juridique de la gestion d'actifs, un fonds professionnel de capital investissement, une société de capital-risque ou une entité mentionnée au dernier alinéa du 8 du II de l'article 150-0 A précité. Ce taux s'applique lorsque le fonds, la société ou l'entité a pour objet principal d'investir, directement ou indirectement par l'intermédiaire d'autres fonds, sociétés ou entités :",
    "1° Dans des sociétés innovantes qui remplissent la condition prévue au 1° ou au 2° du I de l'article L. 214-30 du code monétaire et financier et dont les titres ne sont admis aux négociations ni sur un marché réglementé d'instruments financiers français ou étranger, ni sur un marché non réglementé d'instruments financiers d'un Etat qui n'est pas partie à l'accord sur l'Espace économique européen ;",
    "2° Dans des petites ou moyennes entreprises au sens de l'annexe I au règlement (CE) n° 800/2008 de la Commission du 6 août 2008 déclarant certaines catégories d'aides compatibles avec le marché commun en application des articles 87 et 88 du traité (règlement général d'exemption par catégorie). Les titres de ces entreprises ne doivent être admis aux négociations ni sur un marché réglementé d'instruments financiers français ou étranger, ni sur un marché non réglementé d'instruments financiers d'un Etat qui n'est pas partie à l'accord sur l'Espace économique européen. Pour apprécier la composition du capital de ces petites et moyennes entreprises, il n'est pas tenu compte des participations des sociétés de capital-risque, des fonds communs de placement à risques, des fonds professionnels spécialisés relevant de l'article L. 214-37 du code monétaire et financier dans sa rédaction antérieure à l'ordonnance n° 2013-676 du 25 juillet 2013 modifiant le cadre juridique de la gestion d'actifs, des fonds professionnels de capital investissement, des sociétés de développement régional, des sociétés financières d'innovation et des sociétés unipersonnelles d'investissement à risque. Il n'est pas non plus tenu compte des participations des structures équivalentes établies dans un autre Etat membre de la Communauté européenne ou dans un Etat ou territoire ayant conclu avec la France une convention fiscale contenant une clause d'assistance administrative en vue de lutter contre la fraude ou l'évasion fiscale.",
    "Le taux d'investissement de 0,25 % mentionné au premier alinéa du I s'applique également au montant total des souscriptions dans un fonds commun de placement dans l'innovation mentionné à l'article L. 214-30 du code monétaire et financier et dans un fonds d'investissement de proximité mentionné à l'article L. 214-31 du même code.",
    "Toutefois, le taux d'investissement de 0,25 % ne s'applique pas si les parts, actions ou droits du fonds, de la société ou de l'entité, qui donnent des droits différents sur leur actif net ou leurs produits et sont attribués en fonction de la qualité de la personne, donnent droit à plus de 20 % des plus-values et produits réalisés par le fonds, la société ou l'entité au-delà des souscriptions reçues.",
    "II. – Lorsque les parts, actions ou droits du fonds, de la société ou de l'entité, qui donnent des droits différents sur leur actif net ou leurs produits et sont attribués en fonction de la qualité de la personne, donnent droit à moins de 20 % des plus-values et produits réalisés par le fonds, la société ou l'entité au-delà des souscriptions reçues, les taux d'investissement sont diminués dans la proportion existant entre le pourcentage auquel donnent droit ces parts, actions ou droits et le pourcentage de 20 %. Cette diminution concerne les taux prévus aux deuxième et troisième alinéas du b du 2° du 8 du II de l'article 150-0 A du code général des impôts et aux deuxième et troisième alinéas du b du 2° du 1 du II de l'article 163 quinquies C du même code, ainsi que le taux de 0,25 % prévu au I.",
    "III. – Le ministre chargé de l'économie peut autoriser l'application d'un taux inférieur à celui de 1 % prévu au deuxième alinéa du b du 2° du 8 du II de l'article 150-0 A du code général des impôts et au deuxième alinéa du b du 2° du 1 du II de l'article 163 quinquies C du même code. Cette autorisation peut être accordée lorsque le fonds commun de placement à risques, le fonds professionnel spécialisé relevant de l'article L. 214-37 du code monétaire et financier dans sa rédaction antérieure à l'ordonnance n° 2013-676 du 25 juillet 2013 modifiant le cadre juridique de la gestion d'actifs, le fonds professionnel de capital investissement, la société de capital-risque ou l'entité mentionnée au dernier alinéa du 8 du II de l'article 150-0 A précité a pour objet principal d'investir dans des conditions particulières au regard des pratiques courantes de marché, compte tenu des types d'investissement pratiqués et du niveau de risque qui en résulte.",
    "L'autorisation fixe le taux d'investissement applicable au fonds, à la société ou à l'entité ainsi que les conditions d'application de la dérogation. Ce taux ne peut être inférieur à 0,5 %.",
    "IV. – Les demandes de dérogation au taux d'investissement de 1 % prévu au deuxième alinéa du b du 2° du 8 du II de l'article 150-0 A du code général des impôts et au deuxième alinéa du b du 2° du 1 du II de l'article 163 quinquies C du même code sont présentées au directeur de la législation fiscale. Elles sont instruites au vu des éléments transmis par le fonds, la société ou l'entité sur son orientation de gestion et sa stratégie d'investissement.",
    "La décision de dérogation précise le taux d'investissement retenu pour le fonds, la société ou l'entité concerné, la durée de la dérogation et les modalités de sa mise en œuvre.",
], "Réécriture à droit constant : les conditions d'accès au taux dérogatoire, les règles de proportionnalité et la procédure d'autorisation sont énoncées par des phrases plus courtes au sein des mêmes alinéas. Les catégories de structures et leurs qualifications historiques sont intégralement maintenues. Aucune réforme de fond ni aucun nouveau taux n'est introduit.",
    "Subdivisions I à IV, 1° et 2° et ordre des dix alinéas conservés. Contrôle des taux : 0,25 %, seuil de 20 % strictement supérieur au I et strictement inférieur au II, taux de référence de 1 %, minimum de 0,5 %. Le rapport de réduction du II n'est pas remplacé par une formule qui en changerait la lecture. Les renvois à la rédaction de L. 214-37 antérieure à l'ordonnance du 25 juillet 2013, au règlement n° 800/2008 et à la Communauté européenne restent historiques ; leur actualisation éventuelle relève d'une coordination expresse. Les taux d'investissement ne sont pas des taux d'IS et ne sont pas concernés par le taux national projeté de 20 %.")

article('41 DG ter', [
    "I. – Le contribuable exerce l'option pour le versement forfaitaire libératoire prévue au I de l'article 151-0 du code général des impôts selon les modalités fixées à l'article R. 613-7 du code de la sécurité sociale.",
    "II. – Le contribuable déclare son chiffre d'affaires ou ses recettes et verse l'impôt dû selon les règles fixées aux articles R. 613-8 à R. 613-13 du code de la sécurité sociale.",
    "III. – En cas de cessation d'activité, d'abandon ou de perte du régime mentionné au IV de l'article 151-0 du code général des impôts, le contribuable accomplit les obligations prévues à l'article R. 613-14 du code de la sécurité sociale.",
    "IV. – Si les sommes dues ne sont pas payées, ou ne le sont que partiellement, aux dates mentionnées à l'article R. 613-8 du code de la sécurité sociale, leur recouvrement suit les dispositions mentionnées aux articles R. 243-18 et R. 243-19 à R. 243-21 du même code.",
], "Réécriture à droit constant : le contribuable est explicitement désigné comme auteur de l'option, des déclarations et des versements ; le fait déclenchant le recouvrement est formulé directement. Les quatre subdivisions et leurs renvois sont conservés. Aucune réforme de fond n'est appliquée.",
    "La note source rattache les modifications aux articles 2-I-6° et II-7° du décret n° 2019-718 du 5 juillet 2019 ; elle n'est pas une date d'entrée en vigueur de la réforme projetée. Les échéances restent définies par R. 613-8 ; aucun délai autonome n'est créé. Ce versement libératoire n'est pas affecté par la réforme du taux normal de l'IS.")

article('41 DN bis', [
    "Pour déterminer les limites de déduction des cotisations ou primes mentionnées au II de l'article 154 bis et au I de l'article 154 bis-0 A du code général des impôts, le bénéfice imposable est calculé avant déduction de ces cotisations ou primes.",
], "Réécriture à droit constant : la règle de calcul est placée immédiatement après son objet et précise que le bénéfice s'apprécie avant la déduction concernée. Aucune réforme de fond n'est appliquée.",
    "Les deux renvois fiscaux et la neutralisation des seules cotisations ou primes visées sont conservés. Les régimes des indépendants et des exploitants agricoles ne sont pas assimilés à la capitalisation collective projetée pour les salariés privés ; aucun transfert de cotisations n'est ajouté.")

article('41 DN ter', [
    "Les organismes qui reçoivent, au titre du risque vieillesse, des cotisations ou primes mentionnées au deuxième alinéa du I de l'article 154 bis du code général des impôts ou au I de l'article 154 bis-0 A du même code délivrent chaque année aux cotisants, avant le 1er mars, une attestation indiquant le montant des cotisations ou primes versées au cours de l'année civile précédente ou du dernier exercice clos. Ils produisent un double de cette attestation à l'administration fiscale dans le même délai.",
], "Réécriture à droit constant : les organismes sont nommés comme responsables des deux transmissions, et la phrase précise séparément la remise au cotisant et la production du double à l'administration. Aucune réforme de fond n'est appliquée.",
    "L'échéance est avant le 1er mars, et non au plus tard le 1er mars. Les deux périodes alternatives, année civile précédente ou dernier exercice clos, sont conservées. La suppression des demandes en double visée par la politique nécessiterait des modalités légales de réemploi et de correction des données : elle ne justifie pas de supprimer ici l'attestation ou son double. Aucune extension du projet de retraite aux indépendants ou aux régimes agricoles.")

article('41 DO', [
    "La limite d'imputation des déficits fonciers sur le revenu global est rehaussée en application du quatrième alinéa du 3° du I de l'article 156 du code général des impôts si les conditions suivantes sont remplies :",
    "1. Les dépenses déductibles de travaux de rénovation énergétique sont celles énumérées à l'article D. 319-17 du code de la construction et de l'habitation, dans sa rédaction applicable au jour de l'acceptation d'un devis accompagnée du versement d'un acompte ou, à défaut, au jour de leur paiement. Elles doivent se rapporter aux travaux et audits justifiant du respect des dispositions de l'article D. 319-16 du même code. Sont comprises les dépenses éligibles à la prime de transition énergétique mentionnée au 1° ter du I de ce dernier article. Sont exclus les travaux mentionnés au 3° de ce I ainsi que les travaux de pose d'une chaudière à très haute performance énergétique réalisés en application du d du 1° du même I ;",
    "2. Le contribuable mentionne le déficit foncier pour lequel il demande le rehaussement de la limite d'imputation sur son revenu global dans la déclaration de revenus de l'année au titre de laquelle ce déficit est constaté ;",
    "3. A la demande de l'administration, le contribuable fournit les devis et factures justifiant du respect des dispositions de l'article D. 319-16 du code de la construction et de l'habitation. Il fournit également un diagnostic de performance énergétique au sens de l'article L. 126-26 du même code établissant que le bien concerné par les dépenses mentionnées au 1 présente un niveau de performance énergétique, au sens de l'article L. 173-1-1 du même code, correspondant aux classes suivantes :",
    "– E, F ou G, selon un diagnostic en cours de validité à une date comprise entre le 1er janvier 2023 et la veille de la réalisation des travaux et audits mentionnés au 1 ;",
    "– A, B, C ou D, selon un diagnostic en cours de validité à l'issue des travaux et audits mentionnés au 1, réalisés au plus tard le 31 décembre 2025.",
    "Conformément à l'article 2 du décret n° 2023-297 du 21 avril 2023, ces dispositions s'appliquent aux dépenses de rénovation énergétique pour lesquelles le contribuable justifie de l'acceptation d'un devis à compter du 5 novembre 2022 et qui sont payées entre le 1er janvier 2023 et le 31 décembre 2025.",
], "Réécriture à droit constant : les dépenses admises, les exclusions et les pièces justificatives sont distinguées en phrases plus courtes dans les mêmes subdivisions. La règle temporelle figurant dans la note source est reproduite à la fin du texte proposé afin de conserver l'intégralité des conditions d'application. Aucune réforme de fond ni prolongation du dispositif n'est introduite.",
    "Les renvois à D. 319-16 et D. 319-17 ont été vérifiés dans le corpus public. Dates maintenues : devis acceptés à compter du 5 novembre 2022 ; paiements du 1er janvier 2023 au 31 décembre 2025 ; travaux et audits réalisés au plus tard le 31 décembre 2025. Classes initiales E/F/G et finales A/B/C/D conservées. L'alinéa final reprend la note d'application du décret, sans déplacer les six alinéas de la source ; son maintien comme note éditoriale plutôt que dans la codification devra être arrêté lors de la coordination formelle. La voie de rénovation locative de vingt-quatre mois projetée relève notamment de la loi n° 89-462 et ne prolonge pas cette mesure fiscale.")

article('41 E', [
    "Les charges foncières des immeubles classés ou inscrits au titre des monuments historiques dont le propriétaire se réserve la jouissance peuvent être déduites du revenu global servant de base à l'impôt sur le revenu, dans les conditions et limites prévues aux articles 41 F à 41 I. Cette déduction n'est admise que dans la mesure où ces charges ne sont pas déduites des revenus mentionnés au deuxième alinéa de l'article 29 du code général des impôts.",
], "Réécriture à droit constant : le champ des immeubles et la déduction sont exposés avant la réserve qui interdit une double déduction. Le caractère conditionnel de l'admission et les limites réglementaires sont maintenus. Aucune réforme de fond n'est appliquée.",
    "Le deuxième alinéa de l'article 29 a été vérifié dans le corpus : il vise notamment des recettes issues des droits attachés à la propriété ou à l'usufruit. Ce renvoi et la plage 41 F à 41 I sont conservés tels quels, sans réintroduire un article abrogé ni étendre le texte aux immeubles seulement labellisés, traités par 41 I bis.")

article('41 F', [
    "I. – Les charges mentionnées à l'article 41 E comprennent tout ou partie des dépenses de réparation et d'entretien et des autres charges foncières énumérées aux a à e du 1° et au a du 2° du I de l'article 31 du code général des impôts.",
    "Le propriétaire peut déduire la totalité de ces charges si le public est admis à visiter l'immeuble. Dans le cas contraire, la déduction est limitée à 50 % de leur montant.",
    "II. – Toutefois, les participations aux travaux de réparation ou d'entretien exécutés ou subventionnés par l'administration des affaires culturelles sont intégralement déductibles.",
], "Réécriture à droit constant : la différence entre ouverture au public et absence d'ouverture est exprimée en deux phrases, et la déduction intégrale du II est formulée directement. Les catégories de charges et l'exception du II sont conservées. Aucune réforme de fond n'est appliquée.",
    "Subdivisions I et II et trois alinéas conservés. Contrôle du taux de 50 % et de la déduction intégrale, qui reste applicable aux participations aux travaux exécutés ou subventionnés par l'administration des affaires culturelles. A coordonner avec 41 G pour la fraction restant à la charge du propriétaire et 41 I pour les conditions d'ouverture au public ; aucune réforme des taux n'est prévue ici.")

article('41 G', [
    "Lorsque des subventions sont attribuées pour des travaux de réparation ou d'entretien, les dépenses correspondantes ne sont retenues, chaque année, que pour la part qui doit rester définitivement à la charge du propriétaire. Cette part est déterminée après déduction de la quote-part des subventions afférente à ces dépenses, quelle que soit la date de versement des subventions.",
], "Réécriture à droit constant : la limitation aux dépenses définitivement supportées par le propriétaire est dissociée de la règle de prise en compte des subventions. La règle annuelle et l'indifférence de la date de versement sont maintenues. Aucune réforme de fond n'est appliquée.",
    "La subvention doit être prise en compte même si son versement intervient à une autre date ; le texte ne se limite pas aux subventions déjà encaissées. Coordination conservée avec la déduction des charges prévue à 41 F.")

article('41 I', [
    "Pour l'application de l'article 41 F, un arrêté fixe les conditions dans lesquelles un immeuble est considéré comme ouvert au public (1).",
    "(1) Ces conditions sont prévues aux articles 17 ter à 17 quinquies de l'annexe IV au code général des impôts.",
], "Réécriture à droit constant : l'objet de l'arrêté est formulé directement, sans la tournure impersonnelle « il doit être satisfait ». La note de renvoi est intégralement conservée. Aucune réforme de fond n'est appliquée.",
    "Articles 17 ter à 17 quinquies de l'annexe IV vérifiés dans le corpus : ils traitent de l'ouverture, de la déclaration et du récépissé. Les durées et formalités ne sont pas réécrites ici. La note source relative à l'article 26-I [l] et XI-3 de la loi n° 2013-1278 du 29 décembre 2013 est une indication historique de coordination, sans nouvelle date d'application.")

article('41 I bis', [
    "I. – A. – Pour les immeubles qui ne sont ni classés ni inscrits au titre des monuments historiques, mais qui appartiennent au patrimoine national en raison du label délivré par la « Fondation du patrimoine », seules les charges correspondant aux travaux de réparation et d'entretien sont déductibles.",
    "Pour les immeubles bâtis, seuls les travaux de réparation et d'entretien portant sur les murs, les façades et les toitures ouvrent droit à déduction.",
    "Pour les immeubles bâtis non habitables, les travaux intérieurs de réparation et d'entretien ouvrent également droit à déduction lorsqu'ils sont reconnus comme indissociables de l'intérêt historique, artistique ou culturel du bien par l'unité départementale de l'architecture et du patrimoine territorialement compétente.",
    "Pour les immeubles non bâtis, seuls les travaux de réparation et d'entretien pérenne qui ne nécessitent aucun renouvellement pendant la durée de validité du label ouvrent droit à déduction.",
    "B. – Pour les immeubles mentionnés au A, les travaux de destruction, de reconstruction, de restauration et de remise en état destinés à restaurer l'immeuble dans sa situation d'origine ouvrent également droit à déduction s'ils sont prescrits par l'unité départementale de l'architecture et du patrimoine.",
    "II. – Pour satisfaire à l'engagement prévu au sixième alinéa de l'article L. 143-2 du code du patrimoine, l'immeuble doit être accessible au public, chaque année pendant la durée de validité du label, dans les conditions déterminées par l'arrêté prévu à l'article 41 I.",
    "Pour les immeubles mentionnés au troisième ou au quatrième alinéa du A du I, l'engagement est satisfait si les travaux réalisés sont eux-mêmes visibles ou accessibles au public dans les conditions prévues à l'alinéa précédent.",
    "III. – Les charges sont déductibles à hauteur de 50 % de leur montant. La déduction est toutefois portée à 100 % lorsque la « Fondation du patrimoine » subventionne les travaux à hauteur d'au moins 20 % de leur montant. Ces pourcentages de déduction s'appliquent uniquement à la fraction des travaux qui n'est pas couverte par une subvention.",
], "Réécriture à droit constant : les travaux déductibles sont nommés dans chaque catégorie d'immeubles ; les conditions de reconnaissance, de prescription et d'accès au public sont formulées directement. Les subdivisions et alinéas sont conservés, ainsi que les règles de subvention. Aucune réforme de fond n'est appliquée.",
    "Les quatre alinéas du A du I restent dans le même ordre : le renvoi du II à ses troisième et quatrième alinéas continue de viser les immeubles bâtis non habitables et non bâtis. Contrôle des taux de 50 % et 100 %, du seuil d'au moins 20 % et de l'exclusion de toute fraction subventionnée de l'assiette déductible. Les travaux du B restent une extension expresse au champ du A, conditionnée par leur prescription ; la règle annuelle d'accès au public pendant tout le label est maintenue.")

article('41 J', [
    "Pour obtenir la déduction des charges énumérées aux articles 41 F et 41 I bis, les propriétaires d'immeubles classés ou inscrits au titre des monuments historiques, ou bénéficiant du label de la « Fondation du patrimoine » mentionné à l'article 41 I bis, joignent à leur déclaration annuelle de revenus une note indiquant :",
    "Le détail des sommes dont ils demandent la déduction ;",
    "La date du décret, de l'arrêté ou de la décision ayant classé ou inscrit l'immeuble, ou certaines de ses parties, au titre des monuments historiques.",
    "Pour les monuments classés, les propriétaires joignent à cette note une attestation de l'administration des affaires culturelles. Cette attestation certifie que les travaux exécutés ont effectivement le caractère de travaux d'entretien et de réparation. Elle indique le montant du devis correspondant établi par l'architecte en chef des monuments historiques et, le cas échéant, le taux de la subvention accordée.",
    "Pour les immeubles bénéficiant du label de la « Fondation du patrimoine », les propriétaires joignent à la note une copie de la décision d'octroi du label.",
], "Réécriture à droit constant : le propriétaire est explicitement responsable des pièces à joindre ; le contenu de l'attestation est réparti en phrases plus lisibles. Les cinq alinéas et les pièces propres à chaque catégorie sont conservés. Aucune réforme de fond n'est appliquée.",
    "La source demande une date de classement ou d'inscription dans la liste générale, alors que son premier alinéa vise aussi les immeubles seulement labellisés : cette formulation préexistante est conservée et appelle une clarification de champ, sans inventer de date de classement pour ces immeubles. L'attestation des affaires culturelles reste exigée pour les seuls monuments classés. Aucune dispense de pièces n'est créée au titre du réemploi des données sans modalités de coordination précises.")

article('41 JA', [
    "L'ouverture d'un plan d'épargne avenir climat s'effectue selon les modalités prévues aux articles R. 221-118 et R. 221-119-1 du code monétaire et financier.",
], "Réécriture à droit constant : la phrase exprime directement la règle applicable à l'ouverture du plan et conserve ses deux renvois. Aucune réforme de fond n'est appliquée.",
    "Les références R. 221-118 et R. 221-119-1 sont maintenues sans ajout de condition d'âge ou de procédure non présente dans cet article. Le plan d'épargne avenir climat demeure distinct du compte de retraite projeté.")

article('41 JB', [
    "L'organisme gestionnaire auprès duquel est ouvert un plan d'épargne avenir climat déclare, avant le 16 février de chaque année, les renseignements suivants concernant l'année précédente, sur la déclaration prévue au 1 de l'article 242 ter du code général des impôts :",
    "a) Les nom, prénom et adresse du titulaire du plan ;",
    "b) La date d'ouverture du plan ;",
    "c) Les références du plan.",
    "Il indique également, de manière distincte, la date du premier retrait de sommes ou de valeurs figurant sur le plan ou celle du premier rachat du contrat de capitalisation.",
    "En cas de clôture du plan ou, sans clôture, de retrait ou de rachat effectué dans les conditions prévues aux I et II de l'article L. 221-34-4 du code monétaire et financier, l'organisme gestionnaire indique :",
    "a) La valeur liquidative du plan ou la valeur de rachat du contrat de capitalisation à la date de la clôture, du retrait ou du rachat ;",
    "b) Le montant cumulé des versements effectués depuis l'ouverture du plan, diminué du montant des versements correspondant aux retraits ou rachats précédents ;",
    "c) Le montant du retrait ou du rachat effectué dans les conditions prévues aux I et II de l'article L. 221-34-4 du même code.",
], "Réécriture à droit constant : l'obligation annuelle et les informations propres au premier retrait et aux opérations ultérieures sont formulées directement. Les deux séries de lettres a) à c) et les neuf alinéas sont conservés. Aucune réforme de fond n'est appliquée.",
    "L'échéance reste avant le 16 février. La date du premier retrait ou rachat est une information distincte ; elle n'est pas confondue avec la date d'ouverture. Le montant cumulé est diminué des versements correspondant aux retraits ou rachats précédents, et non de la totalité de ces retraits ou rachats. Renvois aux I et II de L. 221-34-4 conservés. Aucune application des paramètres de retraite au plan d'épargne avenir climat.")

article('41 JC', [
    "Sur la déclaration prévue au 1 de l'article 170 du code général des impôts, le titulaire d'un plan d'épargne avenir climat indique le montant du gain net exonéré en application du 4 ter du III de l'article 150-0 A du même code ou, le cas échéant, le montant du gain net imposable en application du 10 du II de ce même article 150-0 A.",
], "Réécriture à droit constant : le support de déclaration est placé en tête et les deux qualifications du gain net sont énoncées de manière parallèle. Aucune réforme de fond n'est appliquée.",
    "Les références distinctes au 4 ter du III et au 10 du II de l'article 150-0 A sont conservées. L'exonération ne supprime pas l'obligation de déclarer le gain net ; aucune modification du régime fiscal du plan n'est introduite.")

article('41 JD', [
    "Le transfert d'un plan d'épargne avenir climat entre organismes gestionnaires ne constitue pas un retrait si le titulaire remet à l'organisme d'origine un certificat d'identification du plan destinataire. L'organisme auprès duquel le plan est transféré établit ce certificat.",
    "Dans ce cas, l'organisme d'origine communique au nouvel organisme gestionnaire les informations suivantes :",
    "a) La date d'ouverture du plan ;",
    "b) Le montant cumulé des versements effectués sur le plan, diminué du montant des versements correspondant aux retraits ou rachats effectués avant le transfert et n'ayant pas entraîné la clôture du plan.",
], "Réécriture à droit constant : les organismes d'origine et de destination sont désignés sans ambiguïté dans les phrases relatives au certificat et à la transmission des données. La condition de neutralité du transfert et les quatre alinéas sont conservés. Aucune réforme de fond n'est appliquée.",
    "La neutralité du transfert reste subordonnée à la remise du certificat par le titulaire à l'organisme d'origine. La correction du cumul porte sur les versements correspondant aux retraits ou rachats antérieurs sans clôture, et non sur le montant total de ces opérations. Le texte ne crée pas de plafond de frais de transfert : le plafond projeté pour la retraite ne s'applique pas à ce plan distinct.")

article('41 JE', [
    "Pour bénéficier du premier alinéa du II de l'article L. 221-34-4 du code monétaire et financier, le titulaire d'un plan d'épargne avenir climat adresse à l'organisme gestionnaire, avant tout retrait ou rachat concerné, un document dans lequel il atteste sur l'honneur que les retraits ou rachats résultent de l'un des événements mentionnés à cet alinéa.",
], "Réécriture à droit constant : l'antériorité de l'attestation et son auteur sont formulés directement. Le renvoi aux seuls événements du premier alinéa du II est maintenu. Aucune réforme de fond n'est appliquée.",
    "Le document doit précéder le retrait ou le rachat ; une déclaration fiscale ultérieure ne le remplace pas. Le texte n'ajoute ni événement de déblocage ni pièce justificative à l'attestation sur l'honneur prévue par la source.")

article('41 V bis', [
    "1° La société mentionnée au 2° délivre aux bénéficiaires des bons de souscription de parts de créateur d'entreprise mentionnés à l'article 163 bis G du code général des impôts un état individuel, au plus tard le 1er mars de l'année de dépôt de leur déclaration de revenus au titre de l'année d'exercice des bons. Les bénéficiaires conservent cet état jusqu'à l'expiration du délai de reprise et le présentent à la demande de l'administration fiscale.",
    "Cet état indique :",
    "a) Son objet : l'application de l'article 163 bis G du code général des impôts ;",
    "b) La raison sociale et le siège social de la société émettrice des titres ;",
    "c) L'identité et l'adresse du bénéficiaire ;",
    "d) Les date, nombre et prix d'acquisition des titres ;",
    "e) La fraction de source française du gain constaté lors de l'exercice des bons ;",
    "f) A la date d'exercice des bons, la date depuis laquelle le bénéficiaire exerce son activité dans la société ou, s'il n'y exerce plus son activité, la date de son départ et son ancienneté dans la société à cette date.",
    "La société atteste également sur cet état que les bons ont été émis et attribués conformément à l'article 163 bis G précité et, en particulier, qu'elle remplissait, à la date de leur émission, l'ensemble des conditions prévues à cet article.",
    "2° La société émettrice des bons dans laquelle le titulaire exerce son activité transmet à l'administration fiscale les informations mentionnées au k du 2° de l'article 39, dans la déclaration prévue à l'article 87 du code général des impôts.",
    "Si, au moment de l'exercice des bons, le titulaire exerce son activité dans une entreprise différente de la société ou de l'entreprise mentionnée à l'alinéa précédent, cette entreprise transmet cette information selon les mêmes modalités lorsqu'elle dispose des informations nécessaires.",
    "Dans les autres cas, la société émettrice adresse au service des impôts dont elle relève un duplicata de l'état individuel mentionné au 1°, au plus tard le 1er mars de l'année suivant celle de l'exercice des bons.",
    "3° Si les titres issus de l'exercice des bons sont inscrits sur un compte titres qui n'est pas tenu par l'entreprise ou la société mentionnée au 2°, cette entreprise ou société communique une copie de l'état prévu au 1° à l'établissement teneur du compte titres redevable de la retenue à la source prévue à l'article 182 A ter du code général des impôts. Elle transmet cette copie au plus tard le 1er mars de l'année suivant celle de l'exercice des bons ou lors de la cession des titres si celle-ci intervient avant cette date.",
    "Si les titres sont transférés sur un autre compte, l'établissement mentionné à l'alinéa précédent transmet une copie du duplicata au nouveau redevable de la retenue à la source.",
], "Réécriture à droit constant : les obligations de remise, de conservation et de transmission sont exprimées au présent, et les échéances sont séparées de la désignation des destinataires. Les subdivisions 1° à 3°, les lettres a) à f) et les quatorze alinéas sont conservés. Aucune réforme de fond n'est appliquée.",
    "Les échéances du 1° restent rattachées à l'année de dépôt de la déclaration, celles des 2° et 3° à l'année suivant l'exercice des bons ; en cas de cession antérieure, la copie est transmise lors de la cession. La condition de disponibilité des informations par l'autre entreprise est conservée. La source emploie « cette information » au deuxième alinéa du 2° et vise une « entreprise » à l'alinéa précédent qui nomme seulement la société émettrice ; ces ambiguïtés préexistantes sont signalées et non corrigées par une extension du champ. Au dernier alinéa, « copie du duplicata » est maintenu malgré la mention d'une copie de l'état à l'alinéa précédent. Le renvoi au k du 2° de l'article 39 est celui de la présente annexe. La réutilisation des données souhaitée par la politique appelle une coordination précise de cet article avec les obligations déclaratives de l'article 87 du CGI, sans supprimer les transmissions nécessaires à la retenue de l'article 182 A ter.")

article('41 W', [
    "A chaque souscription, un acte constate l'engagement prévu au I de l'article 163 quinquies B du code général des impôts.",
    "Cet acte indique le nombre et la catégorie des parts, ainsi que la date et le montant total de la souscription réalisée.",
], "Réécriture à droit constant : l'établissement de l'acte est rattaché directement à chaque souscription et son contenu est exprimé sans pronom ambigu. Les deux alinéas sont conservés. Aucune réforme de fond n'est appliquée.",
    "Le nombre de parts, leur catégorie, la date et le montant total de la souscription restent tous requis. L'acte demeure propre à chaque souscription ; il n'est pas remplacé par un engagement global annuel.")

article('41 X', [
    "Le gérant d'un fonds commun de placement à risques ou d'un fonds professionnel de capital investissement, ou le dépositaire des actifs du fonds agissant pour le compte du gérant, adresse chaque année, avant le 16 février, les documents suivants à la direction départementale ou, le cas échéant, régionale des finances publiques désignée à l'article 41 duovicies G :",
    "a) Une copie de l'engagement prévu au I de l'article 163 quinquies B du code général des impôts ;",
    "b) Un état individuel indiquant la date, le nombre, la catégorie et le montant des parts cédées ou rachetées.",
    "Les documents relatifs aux opérations réalisées dans le cadre du fonds sont conservés jusqu'à la fin de la sixième année suivant celle de l'expiration de l'engagement.",
], "Réécriture à droit constant : le destinataire et la liste des documents sont séparés plus clairement ; l'obligation de conservation est formulée directement. Les quatre alinéas et les deux catégories de fonds sont conservés. Aucune réforme de fond n'est appliquée.",
    "Le destinataire prévu par 41 duovicies G a été vérifié dans le corpus : il s'agit de la direction auprès de laquelle est souscrite la déclaration de résultats. L'échéance reste avant le 16 février. La conservation court jusqu'à la fin de la sixième année suivant l'année d'expiration de l'engagement, et non à compter de la cession. Aucun fonds supplémentaire n'est ajouté par alignement sur le champ plus large de 41 duovicies G.")

article('41 Y', [
    "Lorsque l'engagement prévu au I de l'article 163 quinquies B du code général des impôts est rompu, le gérant ou le dépositaire des actifs du fonds porte les informations suivantes sur les relevés concernés :",
    "1° Sur le relevé mentionné à l'article 41 sexdecies F, le montant global des sommes ou valeurs auxquelles donnent droit les parts initialement souscrites et qui ont bénéficié de l'exonération instituée par le I de l'article 163 quinquies B précité ;",
    "2° Sur le relevé prévu à l'article 41 duovicies G, les renseignements prévus à cet article concernant les rachats ou les cessions de parts.",
], "Réécriture à droit constant : l'événement déclenchant les déclarations et leurs deux supports sont formulés directement. Les informations propres à chaque relevé et les subdivisions 1° et 2° sont conservées. Aucune réforme de fond n'est appliquée.",
    "Les articles 41 sexdecies F et 41 duovicies G ont été vérifiés dans le corpus. Le 1° conserve le montant global des sommes ou valeurs liées aux parts initialement souscrites ayant bénéficié de l'exonération ; il n'est pas limité à un seul prix de cession. Le 2° maintient les informations sur les rachats comme sur les cessions.")

article('41 ZZ bis', [
    "Pour l'application du a du 2 du I de l'article 163 quatervicies du code général des impôts, le plafond mentionné à l'article L. 241-3 du code de la sécurité sociale est celui de l'année civile qui précède l'année du versement des cotisations ou primes mentionnées au 1 du I de l'article 163 quatervicies précité.",
], "Réécriture à droit constant : la référence temporelle du plafond est exprimée avec des années explicitement rattachées au versement des cotisations ou primes. Les deux renvois internes à l'article 163 quatervicies sont conservés. Aucune réforme de fond n'est appliquée.",
    "La référence demeure le plafond de l'année civile précédente, sans chiffrage nouveau du PASS. La coordination de L. 241-3 figurant dans coordination.json ne justifie pas de remplacer ce plafond ni d'appliquer à l'épargne retraite existante les taux de transfert ou le plafond de frais du compte collectif projeté. Le traitement fiscal de ce nouveau compte nécessitera des dispositions expresses du CGI et les règles déclaratives correspondantes ; aucun renvoi à un article nouveau non créé n'est ajouté.")

assert len(sources) == len(drafts) == 24
answer = []
for source in sources:
    answer.append({
        **{k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')},
        **drafts[source['number']],
        'status': 'rewrite_draft',
    })
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
