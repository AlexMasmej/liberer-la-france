import json
from pathlib import Path


drafts = {}


def add(number, xml, reason, notes):
    if number in drafts:
        raise ValueError(f"Article rédigé deux fois : {number}")
    drafts[number] = {
        "proposed_xml": xml.strip(),
        "reason": reason,
        "review_notes": notes,
        "status": "rewrite_draft",
    }


add(
    "L1242-17",
    """<p>L'employeur doit informer le salarié titulaire d'un contrat de travail à durée déterminée des postes en contrat à durée indéterminée à pourvoir dans l'entreprise lorsque ce salarié en fait la demande et justifie d'au moins six mois d'ancienneté continue dans l'entreprise.<br /><br />Un décret fixe les modalités d'application du présent article.</p>""",
    "Réécriture à droit constant : l'obligation d'information est placée à la charge de l'employeur et ses deux conditions, demande du salarié et ancienneté continue minimale de six mois, sont explicitées. Le renvoi au décret est conservé. Aucune réforme de fond n'est appliquée à ce droit d'information.",
    "Renvoi réglementaire vérifié dans le corpus : D1242-8 précise les modalités de demande et de réponse. Les délais, limites de demandes et modalités propres aux petits employeurs restent dans cet article réglementaire ; ils ne sont pas ajoutés à la disposition législative.",
)

add(
    "L1243-1",
    """<p>Les parties peuvent convenir de rompre le contrat de travail à durée déterminée avant l'échéance de son terme. À défaut d'accord, cette rupture n'est possible qu'en cas de faute grave, de force majeure ou d'inaptitude constatée par le médecin du travail.</p>
<p>Pour le contrat de travail à durée déterminée conclu en application du 6° de l'article L. 1242-2, chacune des parties peut également prendre l'initiative d'une rupture pour un motif réel et sérieux. Cette rupture peut intervenir dix-huit mois après la conclusion du contrat, puis à la date anniversaire de sa conclusion.</p>""",
    "Réécriture à droit constant : l'accord des parties est distingué des trois autres causes de rupture anticipée, puis la faculté spéciale de rupture du CDD à objet défini est présentée séparément. Le motif réel et sérieux et les échéances sont conservés. Le nouveau motif d'adaptation économique prévu pour le licenciement n'est pas étendu aux CDD.",
    "Le 6° de L1242-2 vise les ingénieurs et cadres recrutés pour un objet défini, sous les conditions collectives de ce texte. Conserver les échéances de dix-huit mois puis de la date anniversaire, sans les transformer en faculté permanente de rupture. La dérogation de L1243-2 pour la conclusion d'un CDI reste applicable ; articulation avec L1243-4 signalée dans la note de cet article.",
)

add(
    "L1243-2",
    """<p>Par dérogation à l'article L. 1243-1, le salarié peut rompre son contrat de travail à durée déterminée avant son terme s'il justifie avoir conclu un contrat à durée indéterminée.</p>
<p>Sauf accord des parties, il doit alors respecter un préavis calculé à raison d'un jour par semaine, en fonction :</p>
<p>1° De la durée totale du contrat, y compris, le cas échéant, son renouvellement ou ses deux renouvellements, si le contrat comporte un terme précis ;</p>
<p>2° De la durée effectuée, si le contrat ne comporte pas de terme précis.</p>
<p>La durée du préavis est limitée à deux semaines.</p>""",
    "Réécriture à droit constant : le salarié est désigné comme titulaire de la faculté de rupture et débiteur du préavis. Les deux bases de calcul sont distinguées selon que le terme est précis ou non, avec maintien d'un jour par semaine, de l'accord dérogatoire et du maximum de deux semaines. Aucune modification de fond du régime des CDD.",
    "La note source précise que ces dispositions sont applicables aux contrats en cours ; cette portée historique est conservée. Incohérence préexistante à coordonner : le 1° vise un ou deux renouvellements, alors que L1243-13 permet à la branche de fixer leur nombre maximal. La mention de deux renouvellements n'est pas supprimée silencieusement ; une modification de ce calcul exigerait une coordination expresse.",
)

add(
    "L1243-3",
    """<p>L'employeur a droit à des dommages et intérêts lorsque le salarié rompt le contrat de travail à durée déterminée avant son terme en dehors des cas prévus aux articles L. 1243-1 et L. 1243-2. Le montant de ces dommages et intérêts correspond au préjudice subi par l'employeur.</p>""",
    "Réécriture à droit constant : le bénéficiaire de la réparation et le salarié à l'initiative de la rupture sont explicitement désignés. Une seconde phrase précise que le montant répare le préjudice subi. Les deux renvois qui délimitent les ruptures autorisées sont maintenus ; aucune réforme de fond n'est introduite.",
    "Le préjudice reste la mesure de la réparation : aucun forfait ni plafond n'est ajouté. Conserver ensemble les exceptions de L1243-1 et la rupture pour conclusion d'un CDI prévue par L1243-2.",
)

add(
    "L1243-4",
    """<p>Lorsque l'employeur rompt le contrat de travail à durée déterminée avant son terme en dehors des cas de faute grave, de force majeure ou d'inaptitude constatée par le médecin du travail, le salarié a droit à des dommages et intérêts. Leur montant doit être au moins égal aux rémunérations que le salarié aurait perçues jusqu'au terme du contrat, sans préjudice de l'indemnité de fin de contrat prévue à l'article L. 1243-8.</p>
<p>Toutefois, si la rupture anticipée résulte d'un sinistre constituant un cas de force majeure, le salarié a également droit à une indemnité compensatrice égale aux rémunérations qu'il aurait perçues jusqu'au terme du contrat. L'employeur doit verser cette indemnité.</p>""",
    "Réécriture à droit constant : les conditions du droit à réparation sont séparées du montant minimal des dommages et intérêts. Le régime distinct du sinistre de force majeure et la charge de son indemnité sont explicités dans le second alinéa. Le barème proposé pour l'indemnité légale de licenciement des CDI n'est pas transposé à cette réparation de la rupture d'un CDD.",
    "Le minimum des rémunérations restant jusqu'au terme et le montant égal à ces rémunérations pour le sinistre de force majeure sont conservés. Articulation préexistante à contrôler avec L1243-1 : le premier alinéa ne mentionne expressément ni l'accord des parties ni la faculté spéciale de rupture pour motif réel et sérieux du CDD à objet défini. Ces exceptions ne sont pas ajoutées silencieusement. Le renvoi à L1243-8 demeure soumis aux règles propres à l'indemnité de fin de contrat.",
)

add(
    "L1243-5",
    """<p>Le contrat de travail à durée déterminée prend fin de plein droit à son terme. Lorsqu'il est conclu en application du 6° de l'article L. 1242-2, il prend fin à la réalisation de l'objet pour lequel il a été conclu, après un délai de prévenance d'au moins deux mois.</p>
<p>Ces règles s'appliquent sous réserve des dispositions relatives à la rupture du contrat de travail à durée déterminée :</p>
<p>1° Applicables aux salariés victimes d'un accident du travail ou d'une maladie professionnelle et prévues à l'article L. 1226-19 ;</p>
<p>2° Applicables aux salariés titulaires d'un mandat de représentation mentionnés à l'article L. 2412-1.</p>""",
    "Réécriture à droit constant : la fin de plein droit au terme et la fin du CDD à objet défini sont formulées directement. Les deux catégories de dispositions protectrices demeurent dans leurs subdivisions 1° et 2°, ainsi que le délai de prévenance minimal de deux mois. Aucune réforme de fond des échéances de CDD.",
    "Renvois vérifiés : L1226-19 maintient l'échéance malgré la suspension et encadre le refus de renouvellement ; L2412-1 énumère les mandats protégés. Ne pas confondre le délai de prévenance de deux mois du CDD à objet défini avec le préavis de L1243-2 ou avec la prévenance de l'essai en CDI.",
)

add(
    "L1243-6",
    """<p>La suspension du contrat de travail à durée déterminée n'empêche pas ce contrat de prendre fin au terme prévu.</p>""",
    "Réécriture à droit constant : la conséquence de la suspension est exprimée par une phrase directe indiquant que le terme prévu continue de produire effet. Aucun report automatique ni nouvelle cause de rupture n'est créé.",
    "Lire cette règle avec les protections réservées par L1243-5, notamment L1226-19 en cas d'accident du travail ou de maladie professionnelle, et avec le report spécialement autorisé par L1243-7. Ces régimes distincts ne sont pas supprimés par la reformulation.",
)

add(
    "L1243-7",
    """<p>Le terme initialement fixé d'un contrat de travail à durée déterminée peut être reporté jusqu'au surlendemain du jour où la personne remplacée reprend son emploi. Cette faculté s'applique lorsque le contrat est conclu pour remplacer un salarié temporairement absent ou dont le contrat de travail est suspendu, ou pour effectuer un remplacement au titre des 4° et 5° de l'article L. 1242-2.</p>""",
    "Réécriture à droit constant : la faculté de report et sa limite sont exposées avant les catégories de remplacement auxquelles elle s'applique, dans le même alinéa. Le surlendemain de la reprise et les deux renvois sont maintenus. Aucune extension de fond à d'autres motifs de CDD.",
    "Les 4° et 5° de L1242-2 visent les remplacements de personnes dirigeant ou participant à certaines activités professionnelles et agricoles. La limite reste le surlendemain de la reprise de l'emploi, sans conversion en jours ouvrés ni application aux CDD conclus pour un autre besoin temporaire.",
)

add(
    "L1243-8",
    """<p>À l'issue d'un contrat de travail à durée déterminée, le salarié a droit à une indemnité de fin de contrat si la relation contractuelle de travail ne se poursuit pas par un contrat à durée indéterminée. Cette indemnité constitue un complément de salaire destiné à compenser la précarité de sa situation.</p>
<p>Le montant de cette indemnité est fixé à 10 % de la rémunération totale brute versée au salarié.</p>
<p>Cette indemnité s'ajoute à la rémunération totale brute due au salarié. L'employeur la verse à la fin du contrat, en même temps que le dernier salaire, et la fait figurer sur le bulletin de salaire correspondant.</p>""",
    "Réécriture à droit constant : la condition de non-poursuite en CDI est détachée de la nature et de la finalité de l'indemnité. L'assiette brute, le taux de 10 %, le versement avec le dernier salaire et la mention au bulletin sont maintenus. La réforme de l'indemnité légale de licenciement ne modifie pas l'indemnité de précarité du CDD.",
    "Conserver le taux de 10 % sur la rémunération totale brute versée, distinct de la rémunération brute due à laquelle l'indemnité s'ajoute. Coordination avec le taux conventionnel de 6 % sous conditions de L1243-9 et les exclusions de L1243-10 ; aucun plafond de six mois ni taux de 0,20 mois n'est appliqué ici.",
)

add(
    "L1243-9",
    """<p>Pour améliorer la formation professionnelle des salariés titulaires d'un contrat de travail à durée déterminée, une convention ou un accord collectif de branche étendu, ou une convention ou un accord d'entreprise ou d'établissement, peut également ramener à 6 % le montant de l'indemnité de fin de contrat. Cette réduction suppose que des contreparties soient offertes à ces salariés, notamment un accès privilégié à la formation professionnelle. Dans ce cas, la convention ou l'accord peut fixer les conditions dans lesquelles les salariés peuvent suivre un bilan de compétences en dehors du temps de travail effectif. Ce bilan est réalisé dans le cadre du plan de formation.</p>""",
    "Réécriture à droit constant : les instruments collectifs habilités, le taux réduit de 6 % et l'exigence de contreparties sont présentés dans des phrases distinctes. Le bilan de compétences hors temps de travail effectif et son rattachement au plan de formation sont conservés. Aucune réforme de fond du taux ou des garanties de formation.",
    "Le taux de 6 % reste subordonné aux contreparties et à l'instrument collectif prévu, en coordination avec l'assiette de L1243-8. Point terminologique préexistant à contrôler : la source emploie encore « plan de formation ». Cette dénomination est conservée, sans substitution silencieuse par « plan de développement des compétences » ni modification du régime du bilan de compétences.",
)

add(
    "L1243-10",
    """<p>L'indemnité de fin de contrat n'est pas due dans les cas suivants :</p>
<p>1° Le contrat a été conclu au titre du 3° de l'article L. 1242-2 ou de l'article L. 1242-3, sous réserve de dispositions conventionnelles plus favorables ;</p>
<p>2° Le contrat a été conclu avec un jeune pour une période comprise dans ses vacances scolaires ou universitaires ;</p>
<p>3° Le salarié refuse de conclure un contrat de travail à durée indéterminée portant sur le même emploi ou un emploi similaire et assorti d'une rémunération au moins équivalente ;</p>
<p>4° Le contrat est rompu avant son terme soit à l'initiative du salarié, soit en raison de sa faute grave, soit en raison d'un cas de force majeure.</p>""",
    "Réécriture à droit constant : chaque exclusion est énoncée comme une situation complète, en conservant les quatre subdivisions et la réserve conventionnelle du seul 1°. Les critères du refus de CDI et les trois causes de rupture du 4° sont maintenus. Aucune réforme de fond de l'indemnité de fin de CDD.",
    "Les renvois aux 3° de L1242-2 et à L1242-3 sont vérifiés et conservés dans tout leur champ. Les critères du 3° diffèrent de ceux de L1243-11-1 : le présent texte ne mentionne ni durée de travail équivalente, ni classification identique, ni maintien du lieu de travail. Cette différence préexistante est maintenue ; les critères ne sont pas fusionnés. Les nouvelles règles de durée du travail ne modifient pas silencieusement l'équivalence de rémunération exigée ici.",
)

add(
    "L1243-11",
    """<p>La poursuite de la relation contractuelle de travail au-delà du terme d'un contrat de travail à durée déterminée transforme ce contrat en contrat à durée indéterminée.</p>
<p>Le salarié garde l'ancienneté acquise à l'échéance de son contrat de travail à durée déterminée.</p>
<p>Si le nouveau contrat de travail prévoit une période d'essai, la durée du contrat de travail à durée déterminée est déduite de cette période.</p>""",
    "Réécriture à droit constant : la transformation du contrat, la conservation de l'ancienneté et la déduction sur l'éventuelle période d'essai restent dans trois alinéas distincts. La condition relative à l'existence d'un essai est placée en tête du dernier alinéa. La réforme de l'essai en CDI ne supprime pas cette déduction protectrice.",
    "Coordination avec L1221-19 et L1221-21 visés par coordination.json : appliquer au CDI les règles d'essai et la transition qui le concernent, en conservant intégralement la déduction de la durée du CDD. Aucun nouvel essai automatique de trois mois n'est institué par cet article ; ancienneté acquise et ordre des trois alinéas sont préservés.",
)

add(
    "L1243-11-1",
    """<p>Lorsque l'employeur propose de poursuivre la relation contractuelle de travail après le terme du contrat à durée déterminée sous la forme d'un contrat à durée indéterminée pour occuper le même emploi ou un emploi similaire, il notifie sa proposition par écrit au salarié si l'emploi proposé offre une rémunération au moins équivalente pour une durée de travail équivalente, relève de la même classification et n'implique aucun changement du lieu de travail. Si le salarié refuse cette proposition, l'employeur en informe l'opérateur France Travail et justifie du caractère similaire de l'emploi proposé.<br /><br />Un décret en Conseil d'État fixe les modalités d'application du présent article.</p>""",
    "Réécriture à droit constant : les conditions cumulatives de l'offre de CDI sont formulées avec des verbes explicites et le refus fait l'objet d'une phrase distincte. L'écrit, l'information de France Travail, la justification du caractère similaire et le décret en Conseil d'État sont maintenus. Aucune réforme de fond des conséquences du refus.",
    "La note source fixe l'entrée en vigueur au 1er janvier 2024, conformément au V de l'article 6 de la loi n° 2023-1196 du 18 décembre 2023 ; cette date historique est conservée sans valoir date d'une réforme future. R1243-2, vérifié dans le corpus, règle la notification, le délai de réponse et l'information de France Travail. Conserver l'équivalence de la durée de travail malgré la réforme du seuil des heures supplémentaires ; ne pas réduire les critères à ceux, plus restreints, de L1243-10.",
)

add(
    "L1243-12",
    """<p>Par dérogation aux articles L. 1242-8 et L. 1242-8-1 relatifs à la durée du contrat, l'employeur propose au salarié une prorogation de son contrat de travail à durée déterminée lorsque le salarié est exposé à des rayonnements ionisants et qu'au terme de son contrat, cette exposition dépasse la valeur limite annuelle rapportée à la durée du contrat. La durée de la prorogation doit permettre que l'exposition constatée à l'expiration de cette prorogation soit au plus égale à la valeur limite annuelle rapportée à la durée totale du contrat.</p>
<p>La prorogation ne modifie pas la qualification de contrat à durée déterminée.</p>""",
    "Réécriture à droit constant : le déclenchement de l'obligation de proposer la prorogation et le résultat que sa durée doit permettre sont exposés dans deux phrases. Les deux références de durée maximale, la comparaison proportionnelle de l'exposition et la qualification du contrat sont maintenues. Aucune réforme de fond du régime de radioprotection.",
    "La note source réserve l'application aux contrats de travail conclus postérieurement à la publication de l'ordonnance n° 2017-1387 du 22 septembre 2017, conformément à son article 40-VIII. Cette portée historique reste applicable. Ne pas remplacer la valeur limite annuelle rapportée à la durée totale du contrat par une nouvelle limite d'exposition ni assimiler cette prorogation protectrice à un renouvellement ordinaire. L1242-8 et L1242-8-1 ont été vérifiés dans le corpus.",
)

add(
    "L1243-13",
    """<p>Une convention ou un accord de branche étendu peut déterminer le nombre maximal de fois qu'un contrat de travail à durée déterminée peut être renouvelé. Ce nombre ne peut avoir ni pour objet ni pour effet de pourvoir durablement un emploi lié à l'activité normale et permanente de l'entreprise.<br /><br />Le contrat fixe les conditions de renouvellement ou celles-ci figurent dans un avenant soumis au salarié avant le terme initialement prévu.<br /><br />Le présent article ne s'applique pas au contrat de travail à durée déterminée conclu en application de l'article L. 1242-3.</p>""",
    "Réécriture à droit constant : le pouvoir de la branche est exprimé comme la fixation du nombre maximal de renouvellements. L'interdiction de pourvoir durablement un emploi permanent, les deux supports possibles des conditions de renouvellement et l'exclusion des contrats de L1242-3 sont conservés dans le même ordre. Aucune réforme de fond ni transfert de cette compétence à l'entreprise.",
    "La note source prévoit l'application aux contrats de travail conclus postérieurement à la publication de l'ordonnance n° 2017-1387 du 22 septembre 2017, conformément à son article 40-VIII ; ce champ temporel est maintenu. L'avenant reste soumis au salarié avant le terme initialement prévu. Coordonner avec les deux renouvellements supplétifs de L1243-13-1 et avec la discordance déjà signalée au 1° de L1243-2 ; aucun maximum conventionnel nouveau n'est inventé.",
)

add(
    "L1243-13-1",
    """<p>En l'absence de stipulation dans la convention ou l'accord de branche conclu en application de l'article L. 1243-13, le contrat de travail à durée déterminée peut être renouvelé deux fois, chaque renouvellement ayant une durée déterminée.</p>
<p>La durée du contrat initial, cumulée avec celle de son renouvellement ou de ses deux renouvellements, ne peut dépasser la durée maximale fixée par la convention ou l'accord de branche conclu en application de l'article L. 1242-8 ou, à défaut, par l'article L. 1242-8-1.</p>
<p>Le contrat fixe les conditions de renouvellement ou celles-ci figurent dans un avenant soumis au salarié avant le terme initialement prévu.</p>
<p>Ces règles ne s'appliquent pas au contrat de travail à durée déterminée conclu en application de l'article L. 1242-3.</p>""",
    "Réécriture à droit constant : le caractère supplétif des deux renouvellements est explicité, puis la durée cumulée est formulée comme la somme du contrat initial et des renouvellements. Les quatre alinéas, la hiérarchie des plafonds de durée, l'avenant préalable et l'exclusion sont préservés. Aucune réforme de fond du nombre ou de la durée des renouvellements.",
    "La note source maintient l'application aux contrats de travail conclus postérieurement à la publication de l'ordonnance n° 2017-1387 du 22 septembre 2017, conformément à l'article 40-VIII de celle-ci. Les renvois L1243-13, L1242-8, L1242-8-1 et L1242-3 sont conservés. Le maximum de deux renouvellements est supplétif ; le plafond total reste celui du régime de durée applicable, sans ajout automatique de deux périodes au plafond.",
)

add(
    "L1244-1",
    """<p>La conclusion de contrats de travail à durée déterminée successifs avec le même salarié reste possible, sans que l'article L. 1243-11 y fasse obstacle, lorsque le contrat relève de l'un des cas suivants :</p>
<p>1° Le remplacement d'un salarié absent ;</p>
<p>2° Le remplacement d'un salarié dont le contrat de travail est suspendu ;</p>
<p>3° Un emploi à caractère saisonnier défini au 3° de l'article L. 1242-2, ou un emploi pour lequel, dans certains secteurs d'activité définis par décret ou par convention ou accord collectif étendu, il est d'usage constant de ne pas recourir au contrat de travail à durée indéterminée en raison de la nature de l'activité exercée et du caractère par nature temporaire de cet emploi ;</p>
<p>4° Le remplacement de l'une des personnes mentionnées aux 4° et 5° de l'article L. 1242-2.</p>""",
    "Réécriture à droit constant : l'autorisation de contrats successifs avec le même salarié est énoncée directement, avec maintien de sa relation à la transformation prévue par L1243-11. Les quatre cas, les secteurs habilités et les justifications des emplois d'usage sont intégralement conservés. Aucune extension de fond des motifs de recours aux CDD.",
    "Le 3° conserve distinctement les emplois saisonniers et les emplois d'usage, avec leurs critères propres ; le renvoi aux 4° et 5° de L1242-2 reste limité aux personnes concernées. Cette disposition concerne les contrats successifs avec le même salarié ; elle ne supprime pas globalement les règles de carence sur un même poste des articles L1244-3 et suivants.",
)

add(
    "L1244-2",
    """<p>Une clause prévoyant la reconduction pour la saison suivante peut être insérée dans les contrats de travail à caractère saisonnier définis au 3° de l'article L. 1242-2.</p>
<p>Une convention ou un accord collectif de travail peut imposer à tout employeur ayant employé un salarié dans un emploi à caractère saisonnier de lui proposer, sauf motif réel et sérieux, un emploi de même nature pour la même saison de l'année suivante. La convention ou l'accord précise les conditions applicables, notamment la période d'essai. Il fixe en particulier le délai dans lequel la proposition doit être faite au salarié avant le début de la saison et le montant minimum de l'indemnité que le salarié perçoit s'il n'a pas reçu de proposition de réemploi.</p>
<p>L'ancienneté du salarié est calculée en additionnant les durées des contrats de travail à caractère saisonnier successifs dans une même entreprise.</p>""",
    "Réécriture à droit constant : la clause individuelle de reconduction est distinguée de l'obligation de proposition que peut instituer un texte collectif. Les éléments que celui-ci doit fixer sont répartis entre plusieurs phrases, tandis que le cumul d'ancienneté reste dans le troisième alinéa. Le motif réel et sérieux, l'indemnité minimale et la référence à l'essai sont conservés ; aucune réforme de fond des CDD saisonniers.",
    "Conserver la même nature d'emploi et la même saison de l'année suivante, le délai avant le début de saison et l'indemnité en l'absence de proposition. Les articles L1244-2-1 et L1244-2-2 complètent le régime dans certaines branches à défaut de stipulations collectives. L'essai évoqué ici relève de l'emploi saisonnier ; l'essai de trois mois sans renouvellement proposé pour les nouveaux CDI n'y est pas transposé.",
)

add(
    "L1244-2-1",
    """<p>Dans les branches où l'emploi saisonnier est particulièrement développé, définies par arrêté du ministre chargé du travail, et à défaut de stipulations conventionnelles de branche ou d'entreprise, les contrats de travail à caractère saisonnier conclus dans une même entreprise sur une ou plusieurs saisons sont considérés comme successifs pour l'application de l'article L. 1244-2. Les périodes sans activité dans cette entreprise qui interrompent la succession de ces contrats ne font pas obstacle à cette qualification.</p>""",
    "Réécriture à droit constant : le champ des branches et le caractère supplétif de la règle sont explicités avant son effet sur les contrats successifs. Une seconde phrase isole le maintien de cette qualification malgré les périodes sans activité. Le renvoi au calcul d'ancienneté de L1244-2 et le champ d'une même entreprise sont conservés, sans réforme de fond.",
    "La définition des branches demeure renvoyée à l'arrêté du ministre chargé du travail ; aucune liste de branches n'est inventée. Le défaut de stipulations s'apprécie au niveau de la branche ou de l'entreprise. Le texte qualifie la succession des contrats pour L1244-2 ; il n'institue pas à lui seul une reconduction automatique, régie séparément par L1244-2-2.",
)

add(
    "L1244-2-2",
    """<p>I. – Dans les branches mentionnées à l'article L. 1244-2-1, à défaut de stipulations conventionnelles de branche ou d'entreprise, l'employeur informe le salarié sous contrat de travail à caractère saisonnier des conditions de reconduction de son contrat avant l'échéance de celui-ci. Il utilise tout moyen permettant de donner date certaine à cette information.</p>
<p>II. – Dans les branches mentionnées à l'article L. 1244-2-1, à défaut de stipulations conventionnelles de branche ou d'entreprise, tout salarié qui a été embauché sous contrat de travail à caractère saisonnier dans la même entreprise a droit à la reconduction de son contrat lorsque les deux conditions suivantes sont réunies :</p>
<p>1° Le salarié a accompli au moins deux mêmes saisons dans cette entreprise sur deux années consécutives ;</p>
<p>2° Un emploi saisonnier défini au 3° de l'article L. 1242-2, compatible avec la qualification du salarié, est à pourvoir chez l'employeur.</p>
<p>Dès que les conditions des 1° et 2° sont réunies, l'employeur informe le salarié de son droit à la reconduction de son contrat, sauf motif dûment fondé. Il lui communique cette information par tout moyen permettant de lui donner date certaine.</p>""",
    "Réécriture à droit constant : les deux obligations d'information sont dissociées de leurs modalités de preuve, sans changer leurs alinéas. Le droit à reconduction est clairement subordonné aux deux conditions cumulatives du II. Les branches concernées, la subsidiarité conventionnelle, les saisons sur deux années consécutives et le motif dûment fondé sont maintenus ; aucune réforme de fond.",
    "Les subdivisions I, II, 1° et 2° et le dernier alinéa sont conservés dans l'ordre. L'information du I doit précéder l'échéance ; celle du dernier alinéa intervient dès la réunion des deux conditions, avec la réserve du motif dûment fondé. Ne pas transformer les « deux mêmes saisons » en deux saisons quelconques ni supprimer la compatibilité de qualification. Les deux informations doivent chacune avoir date certaine.",
)

add(
    "L1244-3",
    """<p>À l'expiration d'un contrat de travail à durée déterminée, l'employeur ne peut pourvoir le poste du salarié dont le contrat a pris fin par un nouveau contrat à durée déterminée ou par un contrat de travail temporaire qu'après l'expiration d'un délai de carence. Ce délai est calculé en fonction de la durée du contrat achevé, y compris, le cas échéant, son ou ses renouvellements. Le délai séparant les deux contrats se décompte en jours d'ouverture de l'entreprise ou de l'établissement concerné.<br /><br />Une convention ou un accord de branche étendu peut fixer les modalités de calcul de ce délai de carence, sans préjudice de l'article L. 1242-1.</p>""",
    "Réécriture à droit constant : l'interdiction de pourvoir immédiatement le même poste est formulée comme une obligation de l'employeur. La base de calcul et les jours de décompte font l'objet de phrases distinctes. La compétence de la branche et la réserve de L1242-1 restent dans le second alinéa. Aucune réforme de fond de la carence ni extension de la négociation d'entreprise à ce dispositif.",
    "La note source prévoit l'application aux contrats de travail conclus postérieurement à la publication de l'ordonnance n° 2017-1387 du 22 septembre 2017, conformément à son article 40-VIII ; cette portée temporelle est conservée. L1242-1, vérifié, interdit de pourvoir durablement un emploi lié à l'activité normale et permanente. Coordonner les calculs supplétifs de L1244-3-1 et les dispenses de L1244-4 et L1244-4-1. Les jours d'ouverture ne sont pas remplacés par des jours calendaires ou travaillés par le salarié.",
)

add(
    "L1244-3-1",
    """<p>En l'absence de stipulation dans la convention ou l'accord de branche conclu en application de l'article L. 1244-3, la durée du délai de carence est fixée comme suit :<br /><br />1° À un tiers de la durée du contrat venu à expiration lorsque sa durée, y compris, le cas échéant, son ou ses renouvellements, est d'au moins quatorze jours ;<br /><br />2° À la moitié de la durée du contrat venu à expiration lorsque sa durée, y compris, le cas échéant, son ou ses renouvellements, est inférieure à quatorze jours.<br /><br />Le délai séparant les deux contrats se décompte en jours d'ouverture de l'entreprise ou de l'établissement concerné.</p>""",
    "Réécriture à droit constant : la règle supplétive est annoncée explicitement et les deux branches sont formulées de manière parallèle. Les fractions d'un tiers et d'une moitié, le seuil de quatorze jours, les renouvellements et le décompte en jours d'ouverture sont conservés. Aucune réforme de fond du calcul de carence.",
    "La note source réserve l'application aux contrats de travail conclus postérieurement à la publication de l'ordonnance n° 2017-1387 du 22 septembre 2017, conformément à son article 40-VIII. Le cas de quatorze jours exactement relève du 1° ; les durées inférieures relèvent du 2°. Les 1° et 2° restent dans le même ordre et le dernier alinéa conserve l'unité de décompte de L1244-3. Aucune règle d'arrondi nouvelle n'est ajoutée.",
)

add(
    "L1244-4",
    """<p>Une convention ou un accord de branche étendu peut définir les cas de dispense du délai de carence prévu à l'article L. 1244-3, sans préjudice de l'article L. 1242-1.</p>""",
    "Réécriture à droit constant : la compétence de la branche est exprimée comme une faculté de prévoir des dispenses de carence. Les deux renvois et la réserve de l'interdiction de pourvoir durablement un emploi permanent sont conservés. Aucune réforme de fond ni dispense générale ou pouvoir nouveau donné à l'accord d'entreprise.",
    "La note source maintient l'application aux contrats de travail conclus postérieurement à la publication de l'ordonnance n° 2017-1387 du 22 septembre 2017, conformément à son article 40-VIII. Articuler avec les seuls cas supplétifs de L1244-4-1 en l'absence de stipulation de branche. La dispense de carence ne vaut pas dérogation à L1242-1.",
)

add(
    "L1244-4-1",
    """<p>En l'absence de stipulation dans la convention ou l'accord de branche conclu en application de l'article L. 1244-4, le délai de carence ne s'applique pas dans les cas suivants :</p>
<p>1° Le contrat de travail à durée déterminée assure le remplacement d'un salarié temporairement absent ou dont le contrat de travail est suspendu, en cas de nouvelle absence du salarié remplacé ;</p>
<p>2° Le contrat de travail à durée déterminée a pour objet des travaux urgents rendus nécessaires par des mesures de sécurité ;</p>
<p>3° Le contrat de travail à durée déterminée pourvoit un emploi à caractère saisonnier défini au 3° de l'article L. 1242-2, ou un emploi pour lequel, dans certains secteurs d'activité définis par décret ou par convention ou accord collectif étendu, il est d'usage constant de ne pas recourir au contrat de travail à durée indéterminée en raison de la nature de l'activité exercée et du caractère par nature temporaire de cet emploi ;</p>
<p>4° Le contrat a pour objet le remplacement de l'une des personnes mentionnées aux 4° et 5° de l'article L. 1242-2 ;</p>
<p>5° Le contrat est conclu sur le fondement de l'article L. 1242-3 ;</p>
<p>6° Le salarié prend l'initiative de rompre le contrat avant son terme ;</p>
<p>7° Le salarié refuse le renouvellement de son contrat, pour la durée du contrat non renouvelé.</p>""",
    "Réécriture à droit constant : le caractère supplétif des dispenses est annoncé et les sept situations sont formulées avec des sujets et des verbes explicites. Toutes les qualifications des remplacements, des travaux urgents et des emplois d'usage sont conservées, de même que la portée temporelle du refus de renouvellement. Aucune réforme de fond des exceptions à la carence.",
    "La note source réserve l'application aux contrats de travail conclus postérieurement à la publication de l'ordonnance n° 2017-1387 du 22 septembre 2017, conformément à son article 40-VIII. Conserver spécialement la nouvelle absence du salarié remplacé au 1°, les mesures de sécurité au 2°, les deux critères des emplois d'usage au 3° et la durée du contrat non renouvelé au 7°. Les sept subdivisions, les renvois et la réserve de L1242-1 portée par L1244-4 sont maintenus ; aucune dispense supplémentaire n'est créée.",
)


if __name__ == "__main__":
    sources = json.loads(Path("source.json").read_text())
    assert len(sources) == 24
    assert len(drafts) == len(sources)
    assert set(drafts) == {s["number"] for s in sources}
    output = []
    for source in sources:
        item = {key: source[key] for key in ("code_id", "source_id", "source_sha256", "number")}
        item.update(drafts[source["number"]])
        output.append(item)
    Path("answer.json").write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
