import json
from pathlib import Path


drafts = {}


def add(number, xml, reason, notes):
    assert number not in drafts
    drafts[number] = {
        "proposed_xml": xml.strip(),
        "reason": reason,
        "review_notes": notes,
        "status": "rewrite_draft",
    }


add(
    "L342-10",
    """<p>L'Agence nationale de contrôle du logement social adresse chaque année au ministre chargé du logement un rapport public présentant les principales conclusions de ses contrôles. Avant cet envoi, elle communique les observations qu'elle envisage d'insérer dans le rapport à l'Union sociale pour l'habitat regroupant les fédérations d'organismes d'habitations à loyer modéré, aux fédérations d'organismes d'habitations à loyer modéré et aux organismes contrôlés. Elle les invite à lui transmettre leurs réponses, qu'elle joint au rapport.</p>""",
    "Réécriture à droit constant : la remise annuelle du rapport, la communication préalable des observations et l'annexion des réponses sont exprimées dans leur ordre de réalisation. Les trois catégories de destinataires de la consultation sont maintenues. Aucune réforme de fond.",
    "Le caractère public du rapport et le contradictoire préalable sont conservés ; aucune nouvelle faculté de diffusion des pièces de contrôle n'est créée. L'alinéa unique est maintenu.",
)

add(
    "L342-11",
    """<p>L'organisme ou la personne contrôlée qui fait obstacle aux contrôles de l'agence ou aux demandes qu'elle formule en application de l'article L. 342-5 s'expose, après une mise en demeure restée sans effet, à une sanction pécuniaire d'un montant maximal de 15 000 €. Le ministre chargé du logement prononce cette sanction. Elle est recouvrée comme en matière d'impôts directs et son produit est versé à la Caisse de garantie du logement locatif social.</p>
<p>Lorsqu'une personne ou un organisme ne respecte pas une obligation de déclaration ou de transmission d'états, de documents ou de données demandés par l'agence, celle-ci peut le mettre en demeure de respecter ses obligations, après lui avoir permis de présenter ses observations.</p>""",
    "Réécriture à droit constant : le premier alinéa identifie l'auteur de l'obstacle, le plafond et l'autorité de sanction ; le second précise la procédure préalable à la mise en demeure pour défaut de déclaration ou de transmission. Aucune réforme de fond.",
    "Plafond de 15 000 €, mise en demeure infructueuse, recouvrement et affectataire conservés. Les deux alinéas substantiels restent à leur place, notamment pour le renvoi au second alinéa figurant à L. 342-13 ; le paragraphe vide de la source n'est pas reproduit.",
)

add(
    "L342-12",
    """<p>Lorsque l'agence constate des manquements aux dispositions législatives et réglementaires applicables à l'organisme ou à la personne contrôlée, une irrégularité dans l'emploi des fonds de la participation à l'effort de construction ou des subventions, prêts ou avantages consentis par l'Etat ou par ses établissements publics et par les collectivités territoriales ou leurs établissements publics, une faute grave de gestion, une carence dans la réalisation de l'objet social ou un non-respect des conditions d'agrément, elle demande à cet organisme ou à cette personne de présenter ses observations. Le cas échéant, elle le met en demeure de rectifier les irrégularités dans un délai déterminé.</p>""",
    "Réécriture à droit constant : la constatation des différents manquements est distinguée de la demande d'observations, puis de l'éventuelle mise en demeure. Tous les motifs et toutes les origines de fonds mentionnés par la source sont conservés. Aucune réforme de fond.",
    "L'alinéa unique est conservé pour les renvois de L. 342-13 et L. 342-14. Le délai reste déterminé au cas par cas, sans durée nouvelle ; les qualifications de faute grave, de carence et de non-respect de l'agrément restent distinctes.",
)

add(
    "L342-13",
    """<p>L'agence peut assortir la mise en demeure mentionnée au second alinéa de l'article L. 342-11 d'une astreinte. Elle en fixe la date d'effet et le montant, dans la limite de 70 € par jour de retard et d'un plafond total de 10 000 €.</p>
<p>L'agence peut assortir la mise en demeure mentionnée au premier alinéa de l'article L. 342-12 d'une astreinte. Elle en fixe la date d'effet et le montant, dans la limite de 500 € par jour de retard et d'un plafond total de 100 000 €.</p>
<p>Les astreintes sont recouvrées selon les règles applicables aux impôts directs. Leur produit est versé à la Caisse de garantie du logement locatif social.</p>""",
    "Réécriture à droit constant : chaque astreinte est rattachée à sa mise en demeure et ses deux plafonds sont présentés ensemble. La compétence de l'agence, la date d'effet, le recouvrement et l'affectation sont maintenus. Aucune réforme de fond.",
    "Contrôle des couples 70 €/10 000 € et 500 €/100 000 € et des renvois aux alinéas de L. 342-11 et L. 342-12. Les trois alinéas substantiels sont maintenus ; seuls les paragraphes vides sont retirés.",
)

add(
    "L342-14",
    """<p>I. ― L'agence peut proposer au ministre chargé du logement de prononcer les sanctions suivantes après que la personne ou l'organisme a été mis en mesure de présenter ses observations en application de l'article L. 342-12 ou, lorsqu'une mise en demeure a été adressée, à l'expiration du délai mentionné à cet article :</p>
<p>1° Une sanction pécuniaire d'un montant maximal de deux millions d'euros, sous réserve des règles suivantes :</p>
<p>a) Lorsque les règles d'attribution et d'affectation des logements prévues par le présent code ne sont pas respectées pour un ou plusieurs logements, la sanction ne peut excéder dix-huit mois du loyer en principal du ou des logements concernés. Cette sanction est sans préjudice de la restitution de l'aide publique, lorsqu'elle est due ;</p>
<p>b) Lorsque les règles d'application du supplément de loyer de solidarité prévu à l'article L. 441-3 ne sont pas respectées, la sanction est prononcée dans les limites prévues par la convention conclue avec l'Etat et des montants mentionnés à l'article L. 441-11 ;</p>
<p>c) Lorsque les dispositions législatives et réglementaires applicables aux organismes mentionnés à l'article L. 313-17-1 ne sont pas respectées, la sanction est prononcée dans la limite de 1 % du montant des participations mentionnées au 1° du I de l'article L. 313-19-1 pour l'année civile précédant la décision de sanction. Cette décision précise les modalités d'imputation sur le fonds mentionné à l'article L. 313-19-2.</p>
<p>2° Pour un organisme d'habitations à loyer modéré mentionné à l'article L. 411-2, un groupement d'intérêt économique ou toute autre structure de mutualisation comprenant un organisme d'habitations à loyer modéré mentionné au même article L. 411-2 :</p>
<p>a) La suspension d'un ou plusieurs dirigeants ou membres du conseil d'administration, du conseil de surveillance ou du directoire de l'organisme jusqu'à la prochaine assemblée générale, pour une durée maximale d'un an. Toutefois, si l'intéressé a été déféré devant un tribunal répressif pour le même motif, la suspension ne prend fin qu'après la décision définitive de la juridiction compétente ;</p>
<p>b) La suspension de la gérance, du conseil d'administration, du conseil de surveillance ou du directoire d'un organisme et la nomination d'un administrateur provisoire. Celui-ci reçoit l'ensemble des pouvoirs d'administration, de direction et de représentation du conseil d'administration, de son président et des administrateurs, à l'exception des pouvoirs que la loi attribue expressément aux assemblées d'actionnaires.</p>
<p>La mission de l'administrateur provisoire prend fin dans les mêmes conditions. L'administration provisoire ne peut durer plus de deux ans à compter de la décision ministérielle. A son terme, il est procédé soit à la désignation d'une nouvelle gérance, d'un nouveau conseil d'administration ou d'un nouveau conseil de surveillance et d'un nouveau directoire, soit à la dissolution de l'organisme ;</p>
<p>c) L'interdiction faite à un ou plusieurs membres ou anciens membres du conseil d'administration, du conseil de surveillance ou du directoire de participer au conseil d'administration, au conseil de surveillance ou au directoire d'un organisme mentionné au II de l'article L. 342-2, pour une durée maximale de dix ans ;</p>
<p>d) La révocation d'un ou plusieurs dirigeants ou membres du conseil d'administration, du conseil de surveillance ou du directoire ;</p>
<p>e) Le retrait de la possibilité, pour l'organisme, d'exercer une ou plusieurs de ses compétences, pour une durée maximale de cinq ans ;</p>
<p>f) La dissolution de l'organisme et la nomination d'un liquidateur. Le boni de liquidation ne peut alors être attribué qu'à un organisme de même nature désigné par le ministre chargé du logement ;</p>
<p>3° a) Pour une société d'économie mixte exerçant une activité de construction et de gestion de logements sociaux, un organisme bénéficiant de l'agrément prévu à l'article L. 365-2, un groupement d'intérêt économique ou toute autre structure de mutualisation comprenant une telle société ou un tel organisme :</p>
<p>― la suspension d'un ou plusieurs dirigeants ou membres du conseil d'administration, du conseil de surveillance ou du directoire jusqu'à la prochaine assemblée générale, pour une durée maximale d'un an. Toutefois, si l'intéressé a été déféré à un tribunal répressif pour le même motif, la suspension ne prend fin qu'après la décision définitive de la juridiction compétente ;</p>
<p>― le retrait de l'agrément dont bénéficie l'entité concernée ;</p>
<p>― l'interdiction faite à un ou plusieurs membres ou anciens membres du conseil d'administration, du conseil de surveillance ou du directoire de participer au conseil d'administration, au conseil de surveillance ou au directoire d'un organisme mentionné au II de l'article L. 342-2 ;</p>
<p>― la révocation d'un ou plusieurs dirigeants ou membres du conseil d'administration, du conseil de surveillance ou du directoire ;</p>
<p>b) Pour une société d'économie mixte exerçant une activité de construction et de gestion de logements sociaux, la nomination d'un administrateur chargé de céder les logements à usage locatif et les logements-foyers conventionnés dans les conditions définies à l'article L. 831-1 ou, dans les départements d'outre-mer, construits, acquis ou améliorés avec le concours financier de l'Etat ;</p>
<p>c) Pour un organisme bénéficiant de l'agrément prévu à l'article L. 365-2, la nomination d'un administrateur chargé de céder les logements à usage locatif sociaux mentionnés à l'article L. 302-5 ;</p>
<p>4° Pour une autre personne morale ou une personne physique mentionnée au 4° du II de l'article L. 342-2, l'interdiction de bénéficier de tout concours ou aide de l'Etat ou d'un établissement public de l'Etat, d'une collectivité territoriale ou d'un établissement public local pour la construction, l'acquisition ou la réhabilitation de logements à usage locatif ;</p>
<p>5° Pour un organisme collecteur agréé à collecter la participation des employeurs à l'effort de construction, autre que la société mentionnée à l'article L. 313-19 :</p>
<p>a) Le retrait de l'agrément permettant de collecter la participation des employeurs à l'effort de construction ;</p>
<p>b) La suspension des organes dirigeants jusqu'à la prochaine assemblée générale, pour une durée maximale d'un an, ou le prononcé de la démission d'office de leurs membres.</p>
<p>6° (Abrogé)</p>
<p>7° Pour un organisme mentionné à l'article L. 313-17-1, un groupement d'intérêt économique ou toute autre structure de mutualisation comprenant un tel organisme :</p>
<p>a) La suspension d'un ou plusieurs dirigeants ou membres du conseil d'administration jusqu'à la prochaine assemblée générale, pour une durée maximale d'un an ;</p>
<p>b) La suspension du conseil d'administration jusqu'à la prochaine assemblée générale, pour une durée maximale d'un an. Dans ce cas, le ministre chargé du logement peut nommer un administrateur provisoire ;</p>
<p>c) La révocation d'un ou plusieurs dirigeants ou membres du conseil d'administration ;</p>
<p>d) L'interdiction faite à un ou plusieurs dirigeants, membres ou anciens membres des organes dirigeants d'être dirigeants ou de participer aux organes dirigeants d'un organisme mentionné au II de l'article L. 342-2, pour une durée maximale de dix ans.</p>
<p>8° (Abrogé)</p>
<p>9° Pour un organisme bénéficiant de concours financiers provenant de ressources issues de la participation des employeurs à l'effort de construction, l'interdiction de bénéficier de ces concours pour une durée maximale de dix ans ;</p>
<p>10° Le remboursement des aides d'Etat versées pour l'accomplissement de leur mission de service d'intérêt économique général.</p>
<p>II. ― Les décisions de sanction que le ministre chargé du logement prononce sur proposition de l'agence sont publiées au bulletin officiel.</p>""",
    "Réécriture à droit constant : chaque sanction est rattachée explicitement à la catégorie d'organisme concernée ; les conditions préalables, plafonds, durées, pouvoirs de l'administrateur et publicité sont conservés. Les I et II, les 1° à 10°, les lettres, les tirets et les alinéas sont maintenus, y compris les emplacements abrogés. Aucune réforme de fond.",
    "Plafonds de deux millions d'euros, dix-huit mois de loyer et 1 % maintenus, avec l'année civile de référence et l'imputation sur le fonds. Durées d'un an, deux ans, cinq ans et dix ans conservées selon chaque cas ; aucune durée maximale n'est ajoutée à l'interdiction du troisième tiret du a du 3°. Les prolongations liées au procès pénal et la réserve des pouvoirs des assemblées d'actionnaires sont maintenues. Incohérence préexistante : L. 342-15 vise encore les a et b du 6° et le 8° du I, alors que ces emplacements sont abrogés ici ; une coordination législative distincte est nécessaire. Le renvoi de L. 342-15 au deuxième alinéa du a du 3° reste également à préciser, sans déplacement des tirets dans la présente proposition.",
)

add(
    "L342-15",
    """<p>En cas d'urgence, le ministre chargé du logement peut prononcer les sanctions mentionnées aux a et b des 1° et 2°, au deuxième alinéa du a du 3°, au 4°, aux a et b du 6° et au 8° du I de l'article L. 342-14. Il doit au préalable recueillir l'avis de l'agence, rendu dans un délai maximal de huit jours, et mettre en demeure l'organisme ou la personne concernée de présenter ses observations.</p>""",
    "Réécriture à droit constant : la faculté de sanction en urgence est distinguée des deux formalités préalables. Le délai d'avis de huit jours et l'intégralité des renvois de la source sont conservés. Aucune réforme de fond ni extension des sanctions d'urgence.",
    "Incohérences préexistantes conservées expressément : les 6° et 8° du I de L. 342-14 sont abrogés dans la source assignée, mais restent visés ici. La référence aux a et b du 1° renvoie à des cas de sanction pécuniaire, et celle au deuxième alinéa du a du 3° mérite une clarification de son décompte, car l'énumération comporte une introduction puis des tirets. Une intervention législative doit définir les sanctions d'urgence effectivement visées ; aucune substitution au 7° ni renumérotation n'est inventée.",
)

add(
    "L342-16",
    """<p>Les sanctions mentionnées au I de l'article L. 342-14 sont déterminées en tenant compte de la gravité des faits reprochés, de la situation financière et de la taille de l'organisme. Les sanctions pécuniaires sont recouvrées selon les règles applicables aux impôts directs. Leur produit est versé à la Caisse de garantie du logement locatif social.</p>
<p>Les décisions de sanction prises en application des articles L. 342-14 et L. 342-15 sont communiquées, dès la plus proche réunion, au conseil d'administration ou au conseil de surveillance et au directoire de l'organisme, ou à son organe dirigeant.</p>
<p>Les décisions de sanction prononcées en application des articles L. 342-14 et L. 342-15 peuvent faire l'objet d'un recours de pleine juridiction devant le Conseil d'Etat.</p>""",
    "Réécriture à droit constant : les critères de détermination des sanctions, leur recouvrement, leur communication interne et le recours sont exprimés séparément. Les trois alinéas substantiels et la compétence du Conseil d'Etat sont maintenus. Aucune réforme de fond.",
    "Les trois critères restent cumulatifs dans l'appréciation. Le destinataire composé du conseil de surveillance et du directoire est conservé, ainsi que la communication à la plus proche réunion et le recours de pleine juridiction. Aucun délai de recours nouveau n'est introduit.",
)

add(
    "L342-17",
    """<p>Un décret en Conseil d'Etat précise les modalités de réalisation des contrôles et de gestion de leurs suites.</p>""",
    "Réécriture à droit constant : le texte réglementaire compétent devient le sujet de la phrase, et les modalités des contrôles sont distinguées de la gestion de leurs suites. Aucune réforme de fond.",
    "Le renvoi à un décret en Conseil d'Etat est maintenu pour les deux objets ; aucun pouvoir de sanction supplémentaire n'est créé.",
)

add(
    "L342-18",
    """<p>Un conseil d'administration administre l'agence. Il comprend quatre représentants de l'Etat et trois personnalités qualifiées, désignées pour leurs compétences en matière de logement, d'audit ou d'évaluation des politiques publiques.<br/><br/>La composition de ce conseil favorise la parité entre les femmes et les hommes. Un décret fixe les conditions dans lesquelles cette parité est assurée.<br/><br/>Le président du conseil d'administration est nommé par décret.<br/><br/>Un directeur général, nommé par arrêté du ministre chargé du logement, dirige l'agence.</p>""",
    "Réécriture à droit constant : les fonctions du conseil d'administration et du directeur général sont formulées avec des sujets explicites ; la composition, les compétences justifiant les désignations et les actes de nomination sont conservés. Aucune réforme de fond.",
    "Quatre représentants de l'Etat et trois personnalités qualifiées maintenus. La règle de parité reste formulée comme dans la source, avec son décret d'application, sans ajout de quota. Les quatre blocs de texte gardent leur ordre et leurs séparations.",
)

add(
    "L342-19",
    """<p>I. ― Le personnel de l'Agence nationale de contrôle du logement social se compose des catégories suivantes :</p>
<p>1° Des fonctionnaires de l'Etat ;</p>
<p>2° Des agents non titulaires de droit public ;</p>
<p>3° Des salariés régis par le code du travail.</p>
<p>II. ― Les personnels qui réalisent les contrôles nécessaires à l'accomplissement des missions de l'agence doivent être habilités par le ministre compétent.</p>
<p>Les personnels chargés des contrôles sont soumis au secret professionnel dans les conditions prévues aux articles 226-13 et 226-14 du code pénal. Seuls les auxiliaires de justice peuvent leur opposer ce secret.</p>
<p>III. ― A. - Un comité social d'administration est institué. Il est compétent pour l'ensemble des personnels de l'Agence nationale de contrôle du logement social. Il exerce les compétences des comités sociaux d'administration prévues au II de l'article 15 de la loi n° 84-16 du 11 janvier 1984 portant dispositions statutaires relatives à la fonction publique de l'Etat et celles prévues au chapitre II du titre Ier du livre III de la deuxième partie du code du travail, sous réserve des adaptations prévues par décret en Conseil d'Etat. Son président peut faire appel à un expert habilité dans les conditions fixées par décret en Conseil d'Etat.</p>
<p>B. - Le comité social d'administration comprend le directeur général de l'établissement ou son représentant, qui le préside, et les représentants du personnel. Lorsque le comité est consulté, seuls les représentants du personnel prennent part aux votes.</p>
<p>Les représentants du personnel au comité social d'administration sont élus par collège, au scrutin de liste à la représentation proportionnelle, selon les modalités fixées par décret en Conseil d'Etat.</p>
<p>Les candidatures sont présentées par les organisations syndicales qui satisfont aux conditions suivantes :</p>
<p>1° Pour le collège des personnels mentionnés aux 1° et 2° du I du présent article, les conditions prévues à l'article 9 bis de la loi n° 83-634 du 13 juillet 1983 portant droits et obligations des fonctionnaires ;</p>
<p>2° Pour le collège des personnels mentionnés au 3° du I du présent article, les conditions prévues à l'article L. 2314-5 du code du travail.</p>
<p>Un décret en Conseil d'Etat fixe la composition de la représentation du personnel au comité social d'administration. Ce décret doit permettre la représentation de chaque collège en tenant compte des effectifs des personnels mentionnés, d'une part, aux 1° et 2° du I du présent article et, d'autre part, au 3° du même I.</p>
<p>C. - Le comité social d'administration dispose de la personnalité civile et gère son patrimoine.</p>
<p>Le comité dispose des mêmes règles de fonctionnement et des mêmes moyens que le comité social d'administration prévu à l'article 15 de la loi n° 84-16 du 11 janvier 1984 précitée.</p>
<p>D. - Une commission des agents de droit public est instituée au sein du comité. Elle est compétente pour les personnels mentionnés aux 1° et 2° du I du présent article et exerce les compétences prévues au 3° du II de l'article 15 de la loi n° 84-16 du 11 janvier 1984 précitée.</p>
<p>Un décret en Conseil d'Etat définit la composition de cette commission, les modalités de désignation des représentants du personnel qui y participent, son fonctionnement et les moyens qui lui sont attribués.</p>
<p>E. - Une commission des droits des salariés est instituée au sein du comité. Elle exerce les compétences prévues à l'article L. 2312-5, à l'exception de ses troisième et avant-dernier alinéas, et aux articles L. 2312-6, L. 2312-7 et L. 2312-59 du code du travail. Elle remplit les missions des commissions prévues aux articles L. 2315-51 et L. 2315-55 du même code. Elle est compétente pour gérer le budget des activités sociales et culturelles des salariés de droit privé et son budget de fonctionnement, dans les conditions définies par décret en Conseil d'Etat. A cette fin, elle dispose de la personnalité civile et gère son patrimoine ainsi que les budgets qui lui sont attribués.</p>
<p>Un décret en Conseil d'Etat définit la composition de cette commission, les modalités de désignation des représentants du personnel qui y siègent, son fonctionnement et ses moyens.</p>""",
    "Réécriture à droit constant : les règles relatives aux trois catégories de personnel, à l'habilitation et au secret professionnel, puis au comité et à ses deux commissions, sont clarifiées. Les subdivisions I à III et A à E, les collèges électoraux, les compétences, les exceptions et les budgets restent distincts. Aucune réforme de fond.",
    "Notes source prises en compte : le B du II de l'article 94 de la loi n° 2019-828 du 6 août 2019 rattache l'entrée en vigueur au prochain renouvellement général des instances dans la fonction publique ; le II de l'article 6 de cette loi prévoit la substitution de la commission des droits des salariés à la formation représentant les salariés de droit privé du comité d'entreprise de l'agence. Ces règles historiques ne sont pas transformées en date future. Les renvois aux lois n° 84-16 et n° 83-634 nécessitent un contrôle de concordance avec le code général de la fonction publique, hors du corpus fourni ; ils ne sont pas remplacés silencieusement. Les exclusions des troisième et avant-dernier alinéas de L. 2312-5 et tous les autres renvois au code du travail sont conservés. Aucun régime d'emploi nouveau n'est appliqué à ces personnels.",
)

add(
    "L342-20",
    """<p>Un décret en Conseil d'Etat précise les modalités selon lesquelles l'agence est organisée et fonctionne.</p>""",
    "Réécriture à droit constant : le décret compétent est placé en sujet et les deux objets, organisation et fonctionnement, sont explicités. Aucune réforme de fond.",
    "La compétence d'un décret en Conseil d'Etat et l'alinéa unique sont maintenus, sans ajout d'habilitation législative.",
)

add(
    "L342-21",
    """<p>Pour accomplir ses missions, l'Agence nationale de contrôle du logement social dispose des ressources suivantes :</p>
<p>1° Un prélèvement annuel effectué à son bénéfice sur les ressources de la participation des employeurs à l'effort de construction mentionnées à l'article L. 313-3, dans la limite d'un plafond annuel ;</p>
<p>2° Une cotisation versée par les organismes d'habitations à loyer modéré, les organismes bénéficiant de l'agrément relatif à la maîtrise d'ouvrage prévu à l'article L. 365-2 et les sociétés d'économie mixte exerçant une activité locative sociale ;</p>
<p>3° (Abrogé)</p>
<p>4° (Abrogé)</p>
<p>5° Les contributions et subventions de l'Etat ;</p>
<p>6° Le produit des placements financiers réalisés par l'agence.</p>
<p>La cotisation mentionnée au 2° du présent article a pour assiettes celles mentionnées aux deuxième et troisième alinéas de l'article L. 452-4. La Caisse de garantie du logement locatif social la prélève dans les conditions prévues aux articles L. 452-5 et L. 452-6, puis en reverse le montant à l'Agence nationale de contrôle du logement social dans la limite d'un plafond annuel.</p>
<p>Un arrêté conjoint des ministres chargés du logement, de l'économie et du budget fixe le montant du prélèvement prévu au 1° du présent article, dans la limite de 10 millions d'euros, et le taux de la cotisation mentionnée au 2° du présent article, dans la limite de 0,1 %.</p>""",
    "Réécriture à droit constant : la liste des ressources, le prélèvement de la cotisation par la caisse et la fixation ministérielle des paramètres sont explicités. Les numéros, y compris les 3° et 4° abrogés, et les deux plafonds annuels restent en place. Aucune réforme de fond.",
    "Limites de 10 millions d'euros et 0,1 % conservées sans les présenter comme des montants effectivement arrêtés. Les assiettes des deuxième et troisième alinéas de L. 452-4 ont été vérifiées dans le corpus local. Le corpus indique pour L. 452-5 une fin de validité au 1er janvier 2027 : le renvoi et les modalités de recouvrement devront être coordonnés avec sa succession, sans anticiper ici un régime non fourni. Cette cotisation de financement de l'agence est distincte de la C3S et n'est pas supprimée par la réforme fiscale.",
)

add(
    "L352-1",
    """<p>Lorsque les deux tiers des locataires ou occupants d'un immeuble mentionné au troisième alinéa du présent article ont donné leur accord pour que cet immeuble fasse l'objet d'une convention régie par le chapitre III du présent titre, le représentant de l'Etat dans le département peut proposer cette convention au propriétaire ou aux copropriétaires. Cette proposition intervient avant l'engagement des procédures prévues respectivement aux articles L. 1331-28 ou L. 1331-19 du code de la santé publique et à l'article L. 313-4 du code de l'urbanisme.</p>
<p>Si le propriétaire ou les copropriétaires n'acceptent pas la convention dans un délai de trois mois à compter de la proposition, ou ne réalisent pas les travaux qu'elle prévoit dans les délais impartis, les procédures définies respectivement aux articles L. 1331-28 à L. 1331-31 ou L. 1331-19 à L. 1331-24 du code de la santé publique et à l'article L. 313-4 du code de l'urbanisme sont appliquées.</p>
<p>Les deux alinéas précédents s'appliquent aux immeubles qui nécessitent des travaux de remise en état au titre de l'article L. 1331-28 ou de l'article L. 1331-19 du code de la santé publique, ou au titre de l'article L. 313-4 du code de l'urbanisme.</p>""",
    "Réécriture à droit constant : la proposition de convention est distinguée de ses conditions et des conséquences d'un refus ou d'une inexécution des travaux. Le seuil des deux tiers, le délai de trois mois, les délais impartis pour les travaux et les trois alinéas sont conservés. Aucune réforme de fond.",
    "Les références anciennes aux articles L. 1331-19 et L. 1331-28 à L. 1331-31 du code de la santé publique appellent une vérification de concordance avec les procédures actuelles de sécurité et de salubrité, notamment le titre Ier du livre V du CCH ; elles restent intégralement reproduites faute de coordination expresse dans la source. Aucun assouplissement des protections contre l'habitat indigne n'est déduit de policy.json. La voie locative de rénovation de vingt-quatre mois nécessiterait notamment des dispositions spécifiques aux articles 6 et 20-1 de la loi n° 89-462 du 6 juillet 1989, avec champ, travaux contrôlés et compensation des surcoûts énergétiques ; elle ne résulte pas de cette convention et n'est pas créée ici.",
)

add(
    "L353-1",
    """<p>Pour les logements qui ont fait l'objet d'une convention en application de l'article L. 831-1, le présent chapitre régit les rapports entre les propriétaires et les locataires ou occupants dans la mesure où ses dispositions dérogent à la législation en vigueur.</p>
<p>Des dispositions réglementaires fixent les obligations des bailleurs des logements à usage locatif mentionnés aux 2°, 3° et 4° de l'article L. 831-1 qui donnent lieu au versement de l'aide personnalisée au logement.</p>
<p>Les conventions régies par le présent chapitre et celles régies par la section 3 du chapitre Ier du titre II du livre III du présent code doivent respecter les conventions types fixées par voie réglementaire en application de l'alinéa précédent ou du 5° de l'article L. 831-1.</p>""",
    "Réécriture à droit constant : le champ dérogatoire du chapitre, les obligations réglementaires des bailleurs et la conformité aux conventions types sont formulés avec des sujets explicites. Les catégories de logements et les trois alinéas sont maintenus. Aucune réforme de fond.",
    "Renvoi à L. 831-1 vérifié dans le corpus local, notamment ses 2° à 5°. La seconde famille de conventions demeure celle de la section 3 du chapitre Ier du titre II du livre III. La convention ne reçoit aucun pouvoir de déroger aux obligations de logement social au titre de policy.json.",
)

add(
    "L353-2",
    """<p>Les conventions mentionnées à l'article L. 831-1 ont pour parties l'Etat et les bailleurs des logements précisés à cet article.</p>
<p>Dans le cadre des conventions types mentionnées au même article, ces conventions déterminent les obligations des parties. Elles fixent notamment :</p>
<p>― les travaux d'amélioration à la charge des bailleurs ;</p>
<p>― les caractéristiques techniques que les logements doivent présenter après leur construction ou leur amélioration ;</p>
<p>― le cas échéant, les conditions et les modalités du relogement provisoire pendant les travaux ;</p>
<p>― les conditions d'occupation et de peuplement des logements ;</p>
<p>― le nombre de logements réservés à des familles ou à des occupants quittant des habitats insalubres ou des immeubles menaçant ruine ;</p>
<p>― la durée minimale des baux et les modalités de leur résiliation ou de leur reconduction à la volonté du locataire pendant la durée de la convention ;</p>
<p>― le montant maximal des loyers, des cautionnements et des avances, les modalités de leur évolution et les charges dont le remboursement incombe aux locataires ;</p>
<p>― les obligations des bailleurs envers les organismes chargés de la liquidation et du paiement de l'aide personnalisée au logement ;</p>
<p>― les conditions de révision des conventions et leur durée, qui ne peut être inférieure à neuf ans ;</p>
<p>― les sanctions applicables en cas de non-respect des engagements conventionnels, y compris la résiliation de la convention aux torts du bailleur après mise en demeure.</p>""",
    "Réécriture à droit constant : les parties à la convention et les dix éléments de son contenu sont explicités. Les tirets restent dans l'ordre de la source, et la durée minimale de neuf ans ainsi que la mise en demeure préalable à la résiliation sont conservées. Aucune réforme de fond.",
    "Les alinéas séparés par des sauts de ligne dans la source sont présentés en paragraphes, sans déplacement ni numérotation nouvelle. Le relogement reste prévu le cas échéant ; la résiliation ou reconduction à la volonté du locataire, les réservations et les plafonds conventionnels sont maintenus. Les solutions techniques équivalentes prévues par policy.json relèvent des dispositions techniques de construction et de leurs contrôles, sans faculté générale de dérogation créée ici. Les obligations légales de logement social ne peuvent être supprimées par la convention.",
)

add(
    "L353-3",
    """<p>La publication des conventions au fichier immobilier ou leur inscription au livre foncier conditionne leur entrée en vigueur.</p>""",
    "Réécriture à droit constant : la publicité foncière est exprimée comme une condition préalable d'entrée en vigueur, avec maintien des deux formalités alternatives. Aucune réforme de fond.",
    "La publication au fichier immobilier et l'inscription au livre foncier restent alternatives ; aucune formalité supplémentaire ni date d'effet distincte n'est ajoutée.",
)

add(
    "L353-4",
    """<p>Lorsqu'un bien faisant l'objet d'une convention mentionnée à l'article L. 831-1 est transmis à titre gratuit ou onéreux, cette convention s'impose de plein droit au nouveau propriétaire.</p>""",
    "Réécriture à droit constant : la transmission du bien est placée en tête de phrase et l'opposabilité automatique de la convention est explicitée. Les mutations gratuites et onéreuses restent toutes deux couvertes. Aucune réforme de fond.",
    "Le renvoi à L. 831-1 et l'effet de plein droit sont maintenus ; aucune acceptation du nouveau propriétaire n'est exigée et les conventions en cours ne sont pas modifiées.",
)

add(
    "L353-5",
    """<p>Les logements faisant l'objet d'une convention conclue en application de l'article L. 831-1 doivent être loués conformément à cette convention jusqu'à la date prévue pour son expiration.</p>
<p>Toutefois, dans les conditions fixées par la convention, un logement vacant peut être occupé à titre de résidence principale par le propriétaire, son conjoint, les ascendants ou descendants du propriétaire ou ceux de son conjoint.</p>""",
    "Réécriture à droit constant : l'obligation de location est formulée directement et l'exception pour l'occupation familiale d'un logement vacant est rendue plus lisible. Le terme conventionnel, la résidence principale et tous les liens familiaux sont conservés. Aucune réforme de fond.",
    "L'exception demeure subordonnée à la vacance et aux conditions de la convention. Elle n'est pas étendue à d'autres proches, aux résidences secondaires ou aux logements occupés. Les deux alinéas substantiels sont maintenus.",
)

add(
    "L353-6",
    """<p>Lorsque la convention mentionnée à l'article L. 831-1 est résiliée aux torts du bailleur, les locataires et occupants des logements bénéficient de plein droit, sans formalité, soit de la prorogation de leur bail, soit du maintien dans les lieux, jusqu'à la date initialement prévue pour le terme de la convention. Ce droit est subordonné au respect des obligations prévues aux articles 1728 et suivants du code civil et ne bénéficie pas à ceux dont l'expulsion a été prononcée par une décision judiciaire devenue définitive. La prorogation ou le maintien dans les lieux s'exerce aux clauses et conditions du contrat initial ou, en cas d'échange, du contrat du coéchangiste.</p>
<p>A compter de la date à laquelle la résiliation devient définitive, les logements concernés ne donnent plus droit à l'aide personnalisée au logement. Le loyer exigible ne peut dépasser celui déterminé par la convention et il est diminué du montant de l'aide qui aurait été due pour l'occupation de ces logements.</p>
<p>Cette règle ne fait toutefois pas obstacle à la signature d'une nouvelle convention.</p>""",
    "Réécriture à droit constant : les bénéficiaires, la durée et les conditions de prorogation du bail ou de maintien dans les lieux sont distingués dans le même alinéa. La disparition de l'aide et la diminution corrélative du loyer restent dans le deuxième alinéa. Aucune réforme de fond.",
    "La décision d'expulsion doit rester judiciaire et définitive ; la réserve des articles 1728 et suivants et la situation du coéchangiste sont maintenues. Le terme de la protection reste celui initialement prévu pour la convention. L'accélération des impayés envisagée par policy.json nécessiterait une coordination de l'article 24 de la loi n° 89-462 du 6 juillet 1989, des règles de procédure civile et, pour l'expulsion, du code des procédures civiles d'exécution, notamment L. 411-1. Elle n'est pas introduite dans ce régime de résiliation aux torts du bailleur et ne crée aucun droit d'expulsion privée.",
)

add(
    "L353-7",
    """<p>Si, à la date d'entrée en vigueur de la convention, le logement fait l'objet d'un bail valide ou est occupé par un occupant de bonne foi pouvant bénéficier de la loi n° 48-1360 du 1er septembre 1948 modifiée, le propriétaire doit proposer au locataire ou à l'occupant un bail conforme à la convention. Ce bail entre en vigueur après l'exécution des travaux prévus par la convention ou, si celle-ci ne prévoit pas de travaux, à la date à laquelle le locataire ou l'occupant l'accepte. Une copie de la convention et du barème de l'aide personnalisée doit être annexée au projet de bail, dans les conditions définies par décret.</p>
<p>Le locataire dispose de six mois pour accepter le bail. En cas de refus, les stipulations du bail en cours restent inchangées, sous réserve de la loi n° 67-561 du 12 juillet 1967. Le locataire n'a alors pas droit à l'aide personnalisée au logement. Le propriétaire peut demander la révision de ses engagements conventionnels ou le report de leurs effets jusqu'à l'expiration du bail.</p>
<p>L'occupant mentionné au premier alinéa dispose de six mois pour accepter le bail proposé. A l'expiration de ce délai ou à la date de signature du bail, la loi du 1er septembre 1948 précitée cesse de s'appliquer au logement, sous réserve de l'article L. 353-9.</p>
<p>Le locataire ou l'occupant de bonne foi mentionné aux deuxième et troisième alinéas du présent article qui accepte un nouveau bail dans le délai de six mois continue à occuper les lieux, jusqu'à l'entrée en vigueur de ce bail, aux conditions conventionnelles ou légales applicables à la date de son acceptation.</p>""",
    "Réécriture à droit constant : la proposition de bail, sa prise d'effet, les conséquences du refus du locataire et la situation propre à l'occupant de bonne foi sont distinguées. Les quatre alinéas, les délais de six mois et les régimes historiques de 1948 et 1967 sont maintenus. Aucune réforme de fond.",
    "La date de signature demeure distincte de la date d'entrée en vigueur du nouveau bail lorsque des travaux sont prévus. La fin d'application de la loi de 1948 reste assortie du renvoi à L. 353-9 ; les conditions applicables pendant l'attente sont celles de la date d'acceptation. Le renvoi interne aux deuxième et troisième alinéas est conservé. Aucun bail ancien n'est soumis par cette réécriture à une réforme de fond des rapports locatifs.",
)

add(
    "L353-8",
    """<p>Par dérogation à l'article L. 353-7, la convention s'applique de plein droit à tous les locataires et occupants d'un immeuble financé dans les conditions prévues au présent livre et au livre IV du présent code, à compter de l'achèvement des travaux, lorsque les travaux d'amélioration à la charge du bailleur en application de l'article L. 353-2 sont justifiés par la salubrité, la sécurité ou la mise aux normes minimales d'habitabilité. Cette application reste subordonnée au respect de l'article 2 modifié de la loi n° 67-561 du 12 juillet 1967 sur l'amélioration de l'habitat ou de l'article 14 modifié de la loi n° 48-1360 du 1er septembre 1948 précitée.</p>""",
    "Réécriture à droit constant : l'effet automatique de la convention, sa date de départ et les conditions tenant au financement et aux travaux sont présentés directement. Les réserves des lois de 1967 et de 1948 et l'alinéa unique sont conservés. Aucune réforme de fond.",
    "La dérogation reste limitée à L. 353-7 et aux travaux justifiés par la salubrité, la sécurité ou les normes minimales d'habitabilité. Le financement visé par les livres III et IV, la charge des travaux définie à L. 353-2 et les deux réserves légales restent inchangés ; aucune dérogation générale pour la transformation de bureaux n'est ajoutée.",
)

add(
    "L353-9",
    """<p>Le locataire ou l'occupant de bonne foi qui bénéficiait de la loi n° 48-1360 du 1er septembre 1948 précitée lors de la signature de la convention peut bénéficier à nouveau des chapitres Ier, II, IV, V et VI de cette loi à l'expiration de la convention ou, si celle-ci est résiliée, à la date prévue pour son expiration. Ce bénéfice est soumis aux conditions suivantes :</p>
<p>― qu'il soit âgé d'au moins soixante-cinq ans ou d'au moins soixante ans en cas d'inaptitude au travail ou lorsqu'il bénéficie à cet âge d'une retraite et que ses ressources annuelles ne dépassent pas le montant prévu à l'article 22 bis de cette loi ;</p>
<p>― qu'à la date d'expiration ou de résiliation de la convention, cette loi reste applicable au logement et au locataire ou à l'occupant.</p>
<p>Dans ce cas, le locataire ou l'occupant conserve sa vocation au bénéfice de l'aide personnalisée au logement.</p>
<p>Le loyer exigible est celui fixé par la convention.</p>
<p>Ce loyer est ensuite révisé chaque année selon les conditions prévues à cette fin par la convention.</p>""",
    "Réécriture à droit constant : le retour possible aux chapitres désignés de la loi de 1948 et ses dates sont explicités, puis les effets sur l'aide et le loyer sont formulés directement. Les six alinéas, les deux conditions et les seuils d'âge sont conservés. Aucune réforme de fond.",
    "Soixante-cinq ans, soixante ans, inaptitude au travail, retraite et plafond de l'article 22 bis sont maintenus sans actualisation ni transfert d'un seuil de la réforme des retraites. L'articulation grammaticale de la condition de ressources avec les différentes branches d'âge dans le premier tiret est ambiguë dans la source ; elle est conservée sans en élargir ou restreindre silencieusement la portée. La source distingue le retour au régime à la date prévue pour l'expiration, même après résiliation, et le contrôle d'applicabilité à la date d'expiration ou de résiliation : ces deux repères sont préservés. La vocation à l'aide n'est pas transformée en droit automatique au versement.",
)

add(
    "L353-9-1",
    """<p>Lorsqu'un organisme d'habitations à loyer modéré prend à bail, dans les conditions prévues aux articles L. 444-1 et suivants, un logement que son propriétaire a conventionné en application du 4° de l'article L. 831-1, le sous-locataire est assimilé à un locataire pour bénéficier de l'aide personnalisée au logement. Pour le versement de cette aide, l'organisme d'habitations à loyer modéré est assimilé au bailleur du logement.</p>""",
    "Réécriture à droit constant : les conditions de prise à bail précèdent les deux assimilations, dont les finalités respectives sont distinguées. Le conventionnement au titre du 4° de L. 831-1 et le renvoi à L. 444-1 et suivants sont conservés. Aucune réforme de fond.",
    "L'assimilation du sous-locataire reste limitée au bénéfice de l'aide et celle de l'organisme au versement de cette aide ; aucun statut général de bailleur ou de locataire n'est créé. L'alinéa unique est maintenu.",
)

add(
    "L353-9-2",
    """<p>Les loyers et redevances maximaux prévus par les conventions conclues en application de l'article L. 831-1 sont révisés chaque année au 1er janvier selon l'indice de référence des loyers prévu au I de l'article 17-1 de la loi n° 89-462 du 6 juillet 1989 tendant à améliorer les rapports locatifs et portant modification de la loi n° 86-1290 du 23 décembre 1986. L'indice retenu est celui du deuxième trimestre de l'année précédente.</p>
<p>Le premier alinéa du présent article s'applique depuis le 1er janvier 2010 à toutes les conventions, y compris celles en cours.</p>
<p>Les loyers et redevances maximaux des conventions conclues en application de l'article L. 831-1 du présent code peuvent être augmentés par avenant pour tenir compte de l'amélioration de la performance énergétique et environnementale des logements après des travaux réalisés dans les conditions prévues à l'article 1384 C bis du code général des impôts. Un décret définit les conditions de cette augmentation et fixe notamment son taux maximal.</p>""",
    "Réécriture à droit constant : la révision annuelle, son indice de référence et son application depuis 2010 sont explicités ; la faculté distincte d'augmentation par avenant est formulée séparément. Les trois alinéas et tous les renvois sont maintenus. Aucune réforme de fond ni taux nouveau.",
    "Le 1er janvier, le deuxième trimestre de l'année précédente et le 1er janvier 2010 sont conservés. Le renvoi à l'article 1384 C bis du CGI a été vérifié dans le corpus local : il concerne les logements locatifs soumis aux conditions de rénovation lourde, sans généralisation à tout travail énergétique. Incohérence apparente des métadonnées à contrôler : la note source cite le B du X de l'article 71 de la loi n° 2023-1322 du 29 décembre 2023 et vise les offres de prêts avance mutation ne portant pas intérêt émises du 1er septembre 2024 au 31 décembre 2027, alors que le texte de l'article traite des plafonds conventionnels de loyers et redevances. Cette note est signalée avec ses dates sans être appliquée silencieusement à ces plafonds ni présentée comme une transition de la réforme future. Le taux maximal reste à fixer par décret. La voie de rénovation locative de vingt-quatre mois envisagée par policy.json ne résulte pas de cette faculté d'avenant.",
)


if __name__ == "__main__":
    sources = json.loads(Path("source.json").read_text())
    assert len(sources) == 24
    assert set(drafts) == {source["number"] for source in sources}
    result = []
    for source in sources:
        result.append({
            **{key: source[key] for key in ("code_id", "source_id", "source_sha256", "number")},
            **drafts[source["number"]],
        })
    Path("answer.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"answer.json : {len(result)} articles")
