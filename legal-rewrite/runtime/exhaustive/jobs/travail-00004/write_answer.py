import json
from pathlib import Path


drafts = {
    "L1233-76": (
        """<p>Les modalités d'application des articles L. 1233-71 à L. 1233-73 sont fixées par un décret en Conseil d'État.</p>""",
        "Réécriture à droit constant : les modalités d'application deviennent le sujet de la phrase et la forme du texte réglementaire est conservée. Aucune réforme de fond.",
        "Renvoi à l'ensemble des articles L. 1233-71 à L. 1233-73 et exigence d'un décret en Conseil d'État conservés. Le renvoi ne permet pas de modifier les droits au congé de reclassement. L. 1233-71 comporte déjà un renvoi interne à la période du premier alinéa alors que les durées figurent au deuxième ; cette incohérence, hors du présent article, reste à coordonner expressément.",
    ),
    "L1233-84": (
        """<p>Les entreprises mentionnées à l'article L. 1233-71 qui procèdent à un licenciement collectif dont l'ampleur affecte l'équilibre d'un ou de plusieurs bassins d'emploi où elles sont implantées doivent contribuer à la création d'activités et au développement des emplois. Elles doivent également atténuer les effets du licenciement envisagé sur les autres entreprises de ces bassins d'emploi.</p>
<p>Ces obligations ne s'appliquent pas aux entreprises en redressement ou en liquidation judiciaire.</p>""",
        "Réécriture à droit constant : les entreprises débitrices sont placées en tête de phrase et les obligations de contribution et d'atténuation sont distinguées. Le champ territorial et l'exclusion du deuxième alinéa sont maintenus. Aucune réforme de fond.",
        "Le champ demeure celui des entreprises mentionnées à L. 1233-71 ; aucun seuil nouveau n'est créé. L'ampleur du licenciement doit affecter l'équilibre du ou des bassins où l'entreprise est implantée. L'exclusion du redressement et de la liquidation judiciaires couvre les deux obligations. La réforme du motif économique ne supprime pas ces mesures de revitalisation.",
    ),
    "L1233-85": (
        """<p>L'entreprise et l'autorité administrative concluent une convention dans les six mois suivant la notification prévue à l'article L. 1233-46. Cette convention définit la nature des actions prévues à l'article L. 1233-84, ainsi que les modalités de leur financement et de leur mise en œuvre. Le cas échéant, elle est établie sur la base d'une étude d'impact social et territorial prescrite par l'autorité administrative.</p>
<p>La convention tient compte des actions de même nature éventuellement mises en œuvre par anticipation dans le cadre d'un accord collectif relatif à la gestion prévisionnelle des emplois et des compétences. Elle tient également compte de celles prévues dans le cadre du plan de sauvegarde de l'emploi établi par l'entreprise ou dans le cadre d'une démarche volontaire de l'entreprise faisant l'objet d'un document-cadre conclu entre l'État et l'entreprise. Un décret définit le contenu de ce document et ses modalités d'adoption. À la demande de l'entreprise, un accord collectif de groupe, d'entreprise ou d'établissement tient lieu de la convention prévue au présent article s'il prévoit des actions de même nature assorties d'engagements financiers de l'entreprise au moins égaux au montant de la contribution prévue à l'article L. 1233-86. L'autorité administrative peut toutefois s'y opposer ; son opposition doit être motivée et exprimée dans les deux mois suivant la demande.</p>""",
        "Réécriture à droit constant : la conclusion de la convention, son contenu et l'étude éventuelle sont exposés dans des phrases distinctes. Le second alinéa distingue les actions à prendre en compte et les conditions cumulatives permettant à un accord collectif de tenir lieu de convention. Les deux alinéas sont conservés. Aucune réforme de fond.",
        "Maintien du délai de six mois à compter de la notification de L. 1233-46, du caractère éventuel de l'étude et des trois cadres d'actions antérieures ou prévues. La substitution exige une demande de l'entreprise, des engagements financiers au moins égaux à L. 1233-86 et l'absence d'opposition administrative motivée exprimée dans les deux mois suivant cette demande. Le décret porte sur le document-cadre, sans extension de son objet.",
    ),
    "L1233-86": (
        """<p>Pour chaque emploi supprimé, la contribution versée par l'entreprise est au moins égale à deux fois la valeur mensuelle du salaire minimum de croissance. L'autorité administrative peut toutefois fixer un montant inférieur si l'entreprise ne peut pas en supporter la charge financière.</p>
<p>Si aucune convention n'est signée et qu'aucun accord collectif n'en tient lieu, les entreprises versent au Trésor public une contribution égale au double du montant prévu au premier alinéa.</p>""",
        "Réécriture à droit constant : le minimum est présenté par emploi supprimé et la dérogation financière est formulée directement. L'absence des deux instruments possibles est explicitée au deuxième alinéa. Aucune réforme de fond.",
        "Conservation du minimum de deux fois la valeur mensuelle du SMIC par emploi supprimé, de la faculté administrative d'un montant inférieur en cas d'incapacité financière et du doublement au bénéfice du Trésor public en l'absence de convention ou d'accord en tenant lieu. Le renvoi au premier alinéa est conservé sans recalcul forfaitaire qui effacerait sa dérogation. Cette contribution de revitalisation est distincte de l'indemnité de licenciement réformée à L. 1234-9.",
    ),
    "L1233-87": (
        """<p>Lorsqu'une entreprise d'au moins cinquante salariés qui n'est pas soumise à l'obligation de proposer un congé de reclassement procède à un licenciement collectif dont l'ampleur affecte l'équilibre d'un ou de plusieurs bassins d'emploi où elle est implantée, l'autorité administrative intervient pour faciliter la mise en œuvre d'actions propres à développer des activités nouvelles et à atténuer les effets de la restructuration envisagée sur les autres entreprises de ces bassins. Elle peut, au préalable, prescrire une étude d'impact social et territorial qui prend en compte les observations de l'entreprise concernée. L'autorité administrative agit en concertation avec les organismes participant ou concourant au service public de l'emploi mentionnés aux articles L. 5311-2 et suivants et, le cas échéant, avec la ou les maisons de l'emploi.</p>
<p>L'entreprise et l'autorité administrative conviennent des modalités de la participation éventuelle de l'entreprise à ces actions. Elles tiennent notamment compte de sa situation financière et du nombre d'emplois supprimés.</p>
<p>Le deuxième alinéa ne s'applique pas aux entreprises en redressement ou en liquidation judiciaire.</p>""",
        "Réécriture à droit constant : le champ des entreprises et les conditions de l'intervention administrative sont regroupés au début du premier alinéa. L'étude préalable éventuelle et la concertation font l'objet de phrases distinctes. La participation convenue et son exclusion sont maintenues aux deuxième et troisième alinéas. Aucune réforme de fond.",
        "Seuil d'au moins cinquante salariés et absence d'obligation de congé de reclassement conservés cumulativement. L'étude, lorsqu'elle est prescrite, précède l'intervention et prend en compte les observations de l'entreprise. La participation de l'entreprise demeure éventuelle et convenue d'un commun accord. Le redressement et la liquidation excluent seulement le deuxième alinéa, sans supprimer l'intervention administrative du premier. Renvoi à L. 5311-2 et suivants inchangé.",
    ),
    "L1233-88": (
        """<p>Les collectivités territoriales intéressées, les organismes consulaires et les partenaires sociaux membres de la commission paritaire interprofessionnelle régionale sont consultés avant la détermination des actions prévues aux articles L. 1233-84 et L. 1233-87.</p>
<p>L'exécution de ces actions doit être suivie et évaluée sous le contrôle de l'autorité administrative. Un décret en fixe les modalités. Ce décret détermine également les conditions dans lesquelles les entreprises dont le siège n'est pas implanté dans le bassin d'emploi affecté par le licenciement collectif contribuent à ces actions.</p>""",
        "Réécriture à droit constant : les catégories consultées sont nommées avant l'objet de la consultation et l'obligation de suivi et d'évaluation est formulée directement. L'objet du décret est exposé dans des phrases distinctes. Les deux alinéas et le contrôle administratif sont conservés. Aucune réforme de fond.",
        "Conservation des deux renvois, du caractère préalable de la consultation et de chacune des catégories consultées. La dénomination de la commission figurant dans la source est conservée sans substitution institutionnelle. Le décret règle aussi la contribution des entreprises dont le siège est extérieur au bassin affecté ; il n'est pas limité aux seules entreprises ayant leur siège dans ce bassin.",
    ),
    "L1233-89": (
        """<p>Les procédures de la présente sous-section s'appliquent indépendamment des autres procédures du présent chapitre.</p>""",
        "Réécriture à droit constant : la formule « sont applicables » est remplacée par un verbe direct et les références structurelles sont allégées. L'indépendance des procédures est conservée. Aucune réforme de fond.",
        "L'indépendance concerne toutes les autres procédures du chapitre relatif au licenciement pour motif économique. Elle ne constitue pas une dispense de ces procédures, notamment après la réforme du motif économique de L. 1233-3.",
    ),
    "L1233-90": (
        """<p>Les maisons de l'emploi peuvent participer à la mise en œuvre des mesures de revitalisation des bassins d'emploi. Une convention conclue avec les entreprises intéressées fixe les conditions de cette participation.</p>""",
        "Réécriture à droit constant : la faculté de participation et l'exigence de conditions conventionnelles sont exprimées dans deux phrases au sein du même alinéa. Aucune réforme de fond.",
        "La participation des maisons de l'emploi reste facultative et ses conditions doivent être fixées par convention avec les entreprises intéressées. Aucun financement obligatoire ni nouvelle compétence n'est ajouté.",
    ),
    "L1233-90-1": (
        """<p>Lorsque les suppressions d'emplois concernent au moins trois départements, le ministre chargé de l'emploi et l'entreprise concluent une convention-cadre nationale de revitalisation.</p>
<p>Le montant de la contribution mentionnée à l'article L. 1233-86 est déterminé en tenant compte du nombre total des emplois supprimés.</p>
<p>Les parties signent la convention-cadre dans les six mois suivant la notification du projet de licenciement mentionnée à l'article L. 1233-46.</p>
<p>Dans les quatre mois suivant la signature de la convention-cadre nationale, le représentant de l'État et l'entreprise concluent une ou plusieurs conventions locales conformes à son contenu.</p>""",
        "Réécriture à droit constant : le fait déclencheur est placé en tête du premier alinéa, les signataires sont sujets des obligations et les deux délais sont formulés directement. Les quatre alinéas sont conservés. Aucune réforme de fond.",
        "Seuil d'au moins trois départements, nombre total d'emplois supprimés et renvoi à L. 1233-86 conservés. Les six mois courent à compter de la notification du projet visée à L. 1233-46 ; les quatre mois courent à compter de la signature de la convention-cadre. La ou les conventions locales doivent respecter son contenu. Aucun des deux délais n'est fusionné avec l'autre.",
    ),
    "L1233-91": (
        """<p>Dans les entreprises tenues de constituer un comité social et économique ou des organismes en tenant lieu en application de dispositions légales autres que celles du code du travail ou de stipulations conventionnelles, des décrets en Conseil d'État peuvent fixer les adaptations nécessaires à l'application des dispositions relatives au licenciement pour motif économique.</p>""",
        "Réécriture à droit constant : le champ des entreprises concernées précède l'habilitation réglementaire et les deux fondements possibles de l'obligation de représentation sont exprimés plus directement. Le caractère facultatif de l'adaptation est conservé. Aucune réforme de fond.",
        "L'habilitation vise les entreprises tenues de constituer un CSE ou un organisme en tenant lieu sur un fondement légal extérieur au code du travail ou sur un fondement conventionnel. Maintien de décrets en Conseil d'État et de la seule finalité d'adaptation ; aucune suppression de représentation ou de procédure n'est prévue.",
    ),
    "L1234-1": (
        """<p>Sauf lorsque le licenciement est motivé par une faute grave, le salarié a droit au préavis suivant :</p>
<p>1° S'il justifie de moins de six mois de services continus chez le même employeur, un préavis dont la durée est fixée par la loi, la convention ou l'accord collectif de travail ou, à défaut, par les usages de la localité et de la profession ;</p>
<p>2° S'il justifie d'au moins six mois et de moins de deux ans de services continus chez le même employeur, un préavis d'un mois ;</p>
<p>3° S'il justifie d'au moins deux ans de services continus chez le même employeur, un préavis de deux mois.</p>
<p>Les 2° et 3° s'appliquent seulement si la loi, la convention ou l'accord collectif de travail, le contrat de travail ou les usages ne prévoient pas une durée de préavis ou une condition d'ancienneté de services plus favorable au salarié.</p>""",
        "Réécriture à droit constant : les tranches d'ancienneté sont formulées de manière parallèle et la réserve des règles plus favorables est rendue plus directe. Les cinq alinéas et les 1° à 3° restent à leur place. Aucune réforme de fond du préavis.",
        "Vérification des bornes : moins de six mois ; de six mois inclus à moins de deux ans ; au moins deux ans. Les préavis des 2° et 3° restent respectivement d'un mois et de deux mois. Ancienneté continue chez le même employeur, exception de faute grave et priorité aux durées ou conditions plus favorables conservées. L'allongement ou la réduction de l'essai ne modifie pas ce régime du préavis de licenciement.",
    ),
    "L1234-2": (
        """<p>Est nulle toute clause d'un contrat de travail qui prévoit un préavis plus court que celui résultant de l'article L. 1234-1 ou qui exige une ancienneté de services plus longue que celle prévue par cet article.</p>""",
        "Réécriture à droit constant : la sanction de nullité figure en tête de phrase et les deux clauses interdites sont formulées séparément dans la même phrase. Aucune réforme de fond.",
        "Maintien du renvoi à L. 1234-1 pour la durée du préavis comme pour la condition d'ancienneté. Les deux causes de nullité sont alternatives ; aucune durée ou ancienneté nouvelle n'est créée.",
    ),
    "L1234-3": (
        """<p>Le préavis commence à la date de présentation au salarié de la lettre recommandée lui notifiant son licenciement.</p>""",
        "Réécriture à droit constant : le préavis devient le sujet de la phrase et son commencement est exprimé par un verbe direct. Aucune réforme de fond.",
        "Le point de départ reste la présentation de la lettre recommandée au salarié, sans substitution de la date d'envoi, de retrait ou de lecture. La forme recommandée de la notification demeure mentionnée.",
    ),
    "L1234-4": (
        """<p>Le fait de ne pas exécuter le préavis de licenciement n'avance pas la date de fin du contrat de travail.</p>""",
        "Réécriture à droit constant : la périphrase relative à la conséquence de l'inexécution est remplacée par une formulation directe. Aucune réforme de fond.",
        "Seule l'absence d'avancement du terme est énoncée, comme dans la source. La disposition ne supprime pas les règles particulières de report du préavis, notamment celle de L. 1233-72 en cas de congé de reclassement plus long que le préavis.",
    ),
    "L1234-5": (
        """<p>Le salarié qui n'exécute pas son préavis a droit à une indemnité compensatrice, sauf s'il a commis une faute grave.</p>
<p>Lorsque le préavis n'est pas exécuté, notamment parce que l'employeur en dispense le salarié, les salaires et avantages que celui-ci aurait perçus en travaillant jusqu'au terme du préavis ne peuvent être diminués. Cette règle inclut l'indemnité de congés payés.</p>
<p>L'indemnité compensatrice de préavis s'ajoute à l'indemnité de licenciement ainsi qu'à l'indemnité prévue à l'article L. 1235-2.</p>""",
        "Réécriture à droit constant : le bénéficiaire et l'exception de faute grave sont explicités dans une phrase directe. Le maintien de l'ensemble des salaires et avantages, y compris les congés payés, et le cumul des indemnités restent dans leurs alinéas respectifs. Aucune réforme de fond.",
        "Conservation des trois alinéas, de l'exception de faute grave et du caractère non exhaustif de l'exemple de dispense par l'employeur. Le renvoi à L. 1235-2 est conservé avec les conditions propres à cet article, sans créer d'indemnité automatique. Le plafond proposé pour la seule composante nouvelle de l'indemnité légale de licenciement ne plafonne ni le préavis ni les congés payés ni l'indemnité de L. 1235-2. Le premier alinéa reprend la portée générale de la source ; il n'ajoute pas de règle sur une dispense demandée par le salarié.",
    ),
    "L1234-6": (
        """<p>Lorsque le préavis n'est pas exécuté, en tout ou en partie, en raison de la fermeture temporaire ou définitive de l'établissement ou d'une réduction de son horaire habituel en deçà de la durée légale du travail applicable au salarié, le salaire à prendre en considération est calculé selon la durée de travail suivante. Pour le salarié qui travaillait à temps plein, cette durée est la durée légale ou conventionnelle de travail qui lui est applicable dans l'entreprise. Pour le salarié qui travaillait à temps partiel, elle est celle fixée par son contrat de travail.</p>""",
        "Réécriture de la phrase unique en trois phrases au sein du même alinéa pour distinguer les causes d'inexécution et les bases de calcul à temps plein et à temps partiel. Coordination de fond avec la réforme de L. 3121-27 : la durée légale est celle applicable au salarié, afin de respecter les références distinctes des contrats antérieurs et nouveaux. Les autres règles de calcul sont maintenues à droit constant.",
        "Coordination avec L. 3121-27 : trente-cinq heures pour les contrats antérieurs et quarante heures pour les nouveaux contrats à temps complet, à la même entrée en vigueur, sans date inventée. La durée conventionnelle applicable et la durée contractuelle du temps partiel demeurent les bases prévues par la source. Aucune réduction du salaire contractuel n'est autorisée. Les seuils annuels ou plurihebdomadaires de L. 3121-41 et L. 3121-44 ne sont pas relevés par cet article. Fermeture temporaire ou définitive, réduction sous la durée légale et inexécution totale ou partielle sont conservées.",
    ),
    "L1234-7": (
        """<p>L'employeur reste tenu de respecter le préavis même si l'entreprise cesse son activité.</p>""",
        "Réécriture à droit constant : l'employeur est placé en sujet de l'obligation et la cessation d'activité est exprimée directement. Aucune réforme de fond.",
        "L'obligation de préavis subsiste en cas de cessation de l'entreprise. L'exception de force majeure reste régie par L. 1234-12 et le droit particulier en cas de sinistre par L. 1234-13 ; ces régimes ne sont ni supprimés ni étendus.",
    ),
    "L1234-8": (
        """<p>Les suspensions du contrat de travail prévues par des dispositions légales, une convention ou un accord collectif de travail, des stipulations contractuelles ou des usages n'interrompent pas l'ancienneté retenue pour déterminer la durée du préavis prévue aux 2° et 3° de l'article L. 1234-1.</p>
<p>Toutefois, la durée de ces suspensions n'est pas prise en compte dans le calcul de l'ancienneté exigée pour bénéficier de ces dispositions. Cette exclusion ne s'applique pas à la période de suspension du contrat de travail des élus locaux mentionnés au premier alinéa de l'article L. 3142-88.</p>""",
        "Réécriture à droit constant : la distinction entre continuité de l'ancienneté et décompte de la durée de suspension est formulée directement. L'exception applicable aux élus locaux reste au deuxième alinéa. Aucune réforme de fond.",
        "Les quatre fondements de suspension, le renvoi aux seuls 2° et 3° de L. 1234-1 et l'exception visant le premier alinéa de L. 3142-88 sont conservés. L. 3142-88, vérifié dans le corpus, limite à deux mandats consécutifs la prise en compte qu'il prévoit ; la présente réécriture ne supprime pas cette limite. Ne pas confondre absence de rupture de l'ancienneté et assimilation de toute suspension à du service effectif.",
    ),
    "L1234-10": (
        """<p>Lorsque l'indemnité de licenciement prévue à l'article L. 1234-9 est due, l'employeur reste tenu de la verser même si l'entreprise cesse son activité.</p>""",
        "Réécriture à droit constant : la réserve tenant à l'existence du droit à indemnité est placée en début de phrase et l'employeur est sujet de l'obligation de paiement. Aucune réforme de fond propre à cet article.",
        "Maintien du renvoi à L. 1234-9 et de la réserve « s'il y a lieu », sans création d'un droit indépendant de ses conditions. La coordination avec L. 1234-9 et R. 1234-1, R. 1234-2 et R. 1234-4 conserve la composante d'ancienneté antérieure protégée et le plafond de six mois de la seule composante nouvelle. L'exception de force majeure demeure à L. 1234-12, sous réserve du sinistre visé à L. 1234-13.",
    ),
    "L1234-11": (
        """<p>Les suspensions du contrat de travail prévues par des dispositions légales, une convention ou un accord collectif de travail, des stipulations contractuelles ou des usages n'interrompent pas l'ancienneté retenue pour déterminer le droit à l'indemnité de licenciement.</p>
<p>Toutefois, la durée de ces suspensions n'est pas prise en compte dans le calcul de l'ancienneté exigée pour bénéficier de ce droit. Cette exclusion ne s'applique pas à la période de suspension du contrat de travail des élus locaux mentionnés au premier alinéa de l'article L. 3142-88.</p>""",
        "Réécriture à droit constant : la continuité de l'ancienneté est distinguée du décompte des périodes de suspension pour l'ouverture du droit à indemnité. La rédaction est harmonisée avec L. 1234-8 tout en conservant son objet distinct. Les deux alinéas et l'exception des élus locaux sont maintenus. Aucune réforme de fond.",
        "Le texte porte sur l'ancienneté exigée pour le droit à indemnité, sans créer d'assimilation générale de toutes les suspensions. L'exception des élus locaux se lit avec la limite de deux mandats consécutifs prévue à L. 3142-88. Pour la transition de L. 1234-9, coordonner l'affectation des périodes prises en compte entre ancienneté antérieure et postérieure, sans double compte ni suppression de l'exception. Aucun seuil ni nouveau taux n'est introduit ici.",
    ),
    "L1234-12": (
        """<p>Si l'entreprise cesse son activité en raison d'un cas de force majeure, l'employeur n'est tenu ni de respecter le préavis ni de verser l'indemnité de licenciement prévue à l'article L. 1234-9.</p>""",
        "Réécriture à droit constant : la force majeure est présentée comme la cause de la cessation et les deux obligations dont l'employeur est libéré sont exprimées parallèlement. Aucune réforme de fond.",
        "La libération exige une cessation de l'entreprise pour force majeure ; une simple cessation d'activité ou une difficulté économique ne suffit pas. Maintien du renvoi à L. 1234-9 et de l'articulation avec l'indemnité compensatrice de L. 1234-13 lorsque la rupture résulte d'un sinistre relevant de la force majeure.",
    ),
    "L1234-13": (
        """<p>Le salarié dont le contrat de travail à durée indéterminée est rompu en raison d'un sinistre relevant d'un cas de force majeure a droit à une indemnité compensatrice. Son montant est égal à la somme des montants qui auraient résulté de l'application de l'article L. 1234-5 pour l'indemnité compensatrice de préavis et de l'article L. 1234-9 pour l'indemnité de licenciement.</p>
<p>L'employeur doit verser cette indemnité.</p>""",
        "Réécriture à droit constant : le salarié bénéficiaire, le fait générateur et les deux éléments du montant compensateur sont explicités. La charge de l'employeur reste au deuxième alinéa. Les règles de calcul continuent de résulter des deux articles cités ; aucune réforme de fond autonome n'est ajoutée.",
        "Le champ reste la rupture d'un CDI résultant d'un sinistre relevant de la force majeure, et non toute force majeure. Les deux renvois sont conservés. La référence à L. 1234-9 doit suivre sa transition : composante antérieure protégée, taux de 0,20 mois par année pour la composante nouvelle et plafond de six mois pour cette seule composante. Le plafond ne s'applique pas à la composante de préavis ni au total de l'indemnité compensatrice. Entrée en vigueur à coordonner avec L. 1234-9 et ses textes de calcul.",
    ),
    "L1234-14": (
        """<p>Les articles L. 1234-1, L. 1234-8, L. 1234-9 et L. 1234-11 s'appliquent aux catégories suivantes, sous réserve que les intéressés remplissent les conditions prévues par ces articles :</p>
<p>1° Les agents et salariés mentionnés à l'article L. 5424-1, à l'exclusion des fonctionnaires et des militaires ;</p>
<p>2° Les salariés dont le statut légal est le même que celui applicable dans des entreprises publiques.</p>""",
        "Réécriture à droit constant : le champ personnel est annoncé directement et les catégories sont énumérées sous une forme parallèle. Les trois alinéas, les quatre articles applicables et la réserve de leurs conditions sont conservés. Aucune réforme autonome des régimes du secteur public.",
        "L'exclusion des fonctionnaires et des militaires reste rattachée au 1°. Les conditions propres à chacun des articles L. 1234-1, L. 1234-8, L. 1234-9 et L. 1234-11 restent exigées. Le renvoi existant à L. 1234-9 doit être coordonné expressément avec sa réforme et sa transition pour les agents et salariés effectivement couverts par cet article ; ne pas appliquer le nouveau barème à d'autres indemnités statutaires ou à des régimes publics distincts. Aucune extension nouvelle de champ n'est rédigée ici.",
    ),
    "L1234-15": (
        """<p>La durée du préavis auquel le salarié a droit est fixée comme suit, selon la période pour laquelle sa rémunération est fixée :</p>
<p>1° Un jour si sa rémunération est fixée par jour ;</p>
<p>2° Une semaine si sa rémunération est fixée par semaine ;</p>
<p>3° Quinze jours si sa rémunération est fixée par mois ;</p>
<p>4° Six semaines si sa rémunération est fixée par trimestre ou pour une période plus longue.</p>""",
        "Réécriture à droit constant : le critère de détermination du préavis est explicité dans la phrase introductive et chaque branche associe directement une durée à sa condition. Les cinq alinéas et les 1° à 4° sont conservés. Aucune réforme de fond.",
        "Maintien des quatre correspondances : jour/un jour, semaine/une semaine, mois/quinze jours, trimestre ou période plus longue/six semaines. Le critère reste la période pour laquelle la rémunération est fixée, et non sa date effective de versement. Le champ territorial de la sous-section demeure la Moselle, le Bas-Rhin et le Haut-Rhin ; les catégories particulières à préavis de six semaines de L. 1234-16 ne sont pas absorbées par cet article.",
    ),
}


sources = json.loads(Path("source.json").read_text())
assert len(sources) == len(drafts) == 24
assert set(drafts) == {article["number"] for article in sources}
answer = []
for article in sources:
    proposed_xml, reason, review_notes = drafts[article["number"]]
    answer.append({
        key: article[key]
        for key in ("code_id", "source_id", "source_sha256", "number")
    } | {
        "proposed_xml": proposed_xml,
        "reason": reason,
        "review_notes": review_notes,
        "status": "rewrite_draft",
    })
Path("answer.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")
print(f"answer.json : {len(answer)} articles")
