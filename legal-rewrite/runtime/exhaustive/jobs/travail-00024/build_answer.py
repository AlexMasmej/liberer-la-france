import json
from pathlib import Path


drafts = {
    "L1442-15": {
        "paragraphs": [
            "Lorsqu'un conseiller prud'homme fait l'objet d'une interdiction, d'une déchéance ou d'une incapacité relative à ses droits civiques, il est déchu de plein droit de ses fonctions à la date à laquelle sa condamnation devient définitive."
        ],
        "reason": "Réécriture à droit constant : la condition tenant aux droits civiques précède désormais sa conséquence, et la date de prise d'effet de la déchéance est exprimée directement. Aucune réforme de fond n'est appliquée.",
        "review_notes": "Les trois causes de déchéance, son caractère automatique et l'exigence d'une condamnation devenue définitive sont conservés. Aucune date nouvelle n'est introduite."
    },
    "L1442-16": {
        "paragraphs": [
            "Le président de la Commission nationale de discipline peut suspendre un conseiller prud'homme sur proposition du ministre de la justice ou du premier président de la cour d'appel dans le ressort de laquelle ce conseiller siège. Cette suspension suppose que des faits de nature à entraîner une sanction disciplinaire existent contre le conseiller et que le premier président l'ait préalablement entendu. Sa durée ne peut excéder six mois. La Commission nationale de discipline peut la renouveler une seule fois, pour une durée ne dépassant pas six mois. Lorsque le conseiller fait l'objet de poursuites pénales, le président de la Commission nationale de discipline peut ordonner sa suspension jusqu'à l'intervention de la décision pénale définitive."
        ],
        "reason": "Réécriture à droit constant : la phrase initiale est scindée pour distinguer les autorités de proposition et de décision, les conditions de suspension, sa durée et son renouvellement. Le régime propre aux poursuites pénales est conservé sans réforme de fond.",
        "review_notes": "Contrôles : audition préalable par le premier président ; suspension initiale de six mois au plus ; un seul renouvellement, de six mois au plus, décidé par la commission ; suspension pénale décidée par son président jusqu'à la décision pénale définitive. Le ressort de la cour d'appel reste celui du siège du conseiller."
    },
    "L1442-16-1": {
        "paragraphs": [
            "La Commission nationale de discipline ne peut délibérer que si au moins quatre de ses membres sont présents, dont son président. En cas de partage égal des voix, la voix du président est prépondérante."
        ],
        "reason": "Réécriture à droit constant : le quorum est formulé en réunissant le nombre minimal de membres et la présence obligatoire du président. La règle de départage est maintenue ; aucune réforme de fond n'est introduite.",
        "review_notes": "Le quorum demeure de quatre membres au moins, président compris. La prépondérance de sa voix reste limitée au partage égal des voix."
    },
    "L1442-16-2": {
        "paragraphs": [
            "La Commission nationale de discipline et son président doivent motiver leurs décisions."
        ],
        "reason": "Réécriture à droit constant : la formulation passive devient une obligation explicite de motivation pesant sur la commission et sur son président. Aucune réforme de fond.",
        "review_notes": "L'obligation s'applique aux décisions de chacune des deux autorités, sans exception ni catégorie de décision ajoutée."
    },
    "L1442-17": {
        "paragraphs": [
            "Le conseiller prud'homme peut être relevé, d'office ou à sa demande, de la mesure d'incapacité prononcée à son encontre sur le fondement de l'article L. 1441-10."
        ],
        "reason": "Réécriture à droit constant : le bénéficiaire, les deux voies de relèvement et la mesure concernée sont présentés dans une phrase directe. Aucune réforme de fond n'est prévue pour cette disposition.",
        "review_notes": "Le renvoi à L. 1441-10 a été vérifié dans le corpus public et est conservé. Le relèvement reste possible d'office ou sur demande ; ses modalités demeurent régies par L. 1442-18. Le délai d'un an de recevabilité de la demande ne remplace pas la durée d'incapacité prévue à L. 1441-10."
    },
    "L1442-18": {
        "paragraphs": [
            "Les demandes de relèvement d'incapacité sont adressées au ministre de la justice. Elles sont recevables seulement après l'écoulement d'un délai d'un an depuis le refus d'installation ou la démission.",
            "Lorsqu'une demande a été rejetée après un examen au fond, elle ne peut être renouvelée qu'après un nouveau délai d'un an à compter de ce rejet.",
            "Le ministre de la justice prononce le relèvement par arrêté."
        ],
        "reason": "Réécriture à droit constant : les deux délais de recevabilité sont distingués, et l'autorité qui prononce le relèvement est nommée comme sujet de la phrase. Les trois alinéas sont conservés, sans réforme de fond.",
        "review_notes": "Le premier délai d'un an court depuis le refus d'installation ou la démission. Le nouveau délai d'un an ne concerne que le renouvellement d'une demande rejetée après examen au fond. La compétence du ministre et la forme de l'arrêté sont maintenues."
    },
    "L1442-19": {
        "paragraphs": [
            "Aucune sanction ni aucune rupture du contrat de travail ne peut être fondée sur l'exercice des fonctions de conseiller prud'homme ou sur la participation aux activités mentionnées aux articles L. 1442-2 et L. 1442-5.",
            "Le licenciement d'un conseiller prud'homme doit suivre la procédure d'autorisation administrative prévue par le livre IV de la deuxième partie."
        ],
        "reason": "Réécriture à droit constant : la protection est exprimée comme une interdiction explicite de sanction ou de rupture fondée sur les fonctions ou les activités protégées. L'exigence d'autorisation administrative est maintenue dans son alinéa, sans réforme de fond.",
        "review_notes": "Les deux activités visées par renvoi et le renvoi au livre IV de la deuxième partie sont conservés. La protection n'est pas limitée aux sanctions disciplinaires. Les orientations sur les ruptures du CDI ne suppriment pas ce régime protecteur."
    },
    "L1443-1": {
        "paragraphs": [
            "Le fait de porter atteinte ou de tenter de porter atteinte à la libre désignation des candidats à la nomination des conseillers prud'hommes, à l'indépendance des conseillers prud'hommes ou à l'exercice régulier de leurs fonctions est puni d'un an d'emprisonnement et de 3 750 euros d'amende. L'atteinte peut notamment résulter de la méconnaissance des articles L. 1442-2, L. 1442-5 à L. 1442-7 et L. 1442-10."
        ],
        "reason": "Réécriture à droit constant : les intérêts protégés et la peine sont exposés dans une première phrase ; les manquements cités à titre d'exemple figurent dans une seconde. L'atteinte et sa tentative restent incriminées, sans réforme de fond.",
        "review_notes": "Peines inchangées : un an d'emprisonnement et 3 750 euros d'amende. Sont conservés la désignation des candidats à la nomination, l'indépendance, l'exercice régulier des fonctions et tous les renvois, dont l'intervalle L. 1442-5 à L. 1442-7. Le caractère illustratif de ces renvois est maintenu par « notamment »."
    },
    "L1451-1": {
        "paragraphs": [
            "Lorsque le conseil de prud'hommes est saisi d'une demande tendant à qualifier la rupture du contrat de travail intervenue à l'initiative du salarié en raison de faits que celui-ci reproche à son employeur, l'affaire est portée directement devant le bureau de jugement. Ce bureau statue au fond dans un délai d'un mois suivant sa saisine."
        ],
        "reason": "Réécriture à droit constant : la saisine directe du bureau de jugement et son délai pour statuer font l'objet de deux phrases distinctes. Le champ de la rupture à l'initiative du salarié pour des faits reprochés à l'employeur est conservé, sans réforme de fond.",
        "review_notes": "Le délai reste d'un mois à compter de la saisine du bureau de jugement et concerne une décision au fond. Cette voie directe n'est pas étendue aux autres litiges relatifs à une rupture."
    },
    "L1453-1 A": {
        "paragraphs": [
            "Par dérogation au premier alinéa de l'article 4 de la loi n° 71-1130 du 31 décembre 1971 portant réforme de certaines professions judiciaires et juridiques, les parties peuvent assurer elles-mêmes leur défense devant le conseil de prud'hommes. Elles peuvent aussi être assistées ou représentées par un avocat ou par l'une des personnes suivantes :",
            "1° Les salariés ou les employeurs appartenant à la même branche d'activité ;",
            "2° Les défenseurs syndicaux ;",
            "3° Leur conjoint, leur partenaire lié par un pacte civil de solidarité ou leur concubin.",
            "L'employeur peut également être assisté ou représenté par un membre de l'entreprise ou de l'établissement qui est fondé de pouvoir ou habilité à cet effet.",
            "Tout représentant qui n'est pas avocat doit justifier d'un pouvoir spécial. Devant le bureau de conciliation et d'orientation, ce pouvoir écrit doit l'autoriser à concilier au nom et pour le compte du mandant ainsi qu'à prendre part aux mesures d'orientation."
        ],
        "reason": "Réécriture à droit constant : la défense personnelle est distinguée de l'assistance et de la représentation, puis les exigences du pouvoir spécial sont exprimées directement. Les six alinéas et les trois catégories numérotées sont conservés, sans réforme de fond.",
        "review_notes": "La dérogation vise toujours le premier alinéa de l'article 4 de la loi n° 71-1130 du 31 décembre 1971. Les catégories habilitées, la faculté supplémentaire de l'employeur et les deux habilitations écrites devant le bureau de conciliation et d'orientation sont maintenues. Application temporelle issue de la note source : l'article 109 II de la loi n° 2019-222 du 23 mars 2019 réserve ces dispositions aux instances introduites à compter du lendemain de la publication de cette loi ; cette règle demeure à prendre en compte pour les instances antérieures."
    },
    "L1453-1": {
        "paragraphs": [
            "Le conseil de prud'hommes peut autoriser les mineurs qui ne peuvent être assistés de leur père, de leur mère ou de leur tuteur à agir devant lui."
        ],
        "reason": "Réécriture à droit constant : le conseil de prud'hommes devient le sujet explicite du pouvoir d'autorisation. La condition d'absence d'assistance demeure identique ; aucune réforme de fond.",
        "review_notes": "La faculté d'autorisation est conservée, sans automatisme. Les trois personnes susceptibles d'assister le mineur restent le père, la mère ou le tuteur."
    },
    "L1453-2": {
        "paragraphs": [
            "Lorsqu'une personne habilitée à assister ou à représenter les parties en matière prud'homale est également conseiller prud'homme, elle ne peut exercer une mission d'assistance ou un mandat de représentation devant le conseil de prud'hommes auquel elle appartient."
        ],
        "reason": "Réécriture à droit constant : la double qualité déclenchant l'incompatibilité est placée en tête de phrase, avant l'interdiction. Le périmètre du conseil d'appartenance reste identique, sans réforme de fond.",
        "review_notes": "L'interdiction porte sur l'assistance comme sur la représentation devant le seul conseil auquel la personne appartient. Note historique : le V de l'article 259 de la loi n° 2015-990 du 6 août 2015 prévoit une entrée en vigueur au plus tard le premier jour du douzième mois suivant la publication de cette loi ; il ne fixe pas la date d'une réforme future."
    },
    "L1453-3": {
        "paragraphs": [
            "Il est interdit au président et au vice-président d'un conseil de prud'hommes d'assister ou de représenter une partie devant les formations de ce conseil."
        ],
        "reason": "Réécriture à droit constant : l'incompatibilité est formulée comme une interdiction directe dont les titulaires et le champ sont explicites. Aucune réforme de fond.",
        "review_notes": "L'interdiction continue de viser le président et le vice-président, l'assistance et la représentation, devant toutes les formations de leur conseil. Elle n'est pas étendue aux autres conseils."
    },
    "L1453-4": {
        "paragraphs": [
            "Le défenseur syndical assiste ou représente les parties devant les conseils de prud'hommes et, en matière prud'homale, devant les cours d'appel.",
            "Le défenseur syndical est inscrit, dans les conditions définies par décret, sur une liste arrêtée par l'autorité administrative sur proposition des organisations d'employeurs et de salariés.",
            "Le défenseur syndical intervient dans le périmètre d'une région administrative. La partie qui a choisi de se faire assister par lui devant le conseil de prud'hommes peut, dans tous les cas, continuer à être représentée par ce même défenseur devant la cour d'appel compétente."
        ],
        "reason": "Réécriture à droit constant : les fonctions et l'inscription sur la liste sont exprimées directement. Le troisième alinéa explicite la réserve d'interprétation constitutionnelle déjà applicable à la limite régionale ; il ne s'agit pas d'une réforme de fond.",
        "review_notes": "Les trois alinéas sont conservés. La seconde phrase du troisième alinéa reprend la portée de la réserve énoncée au paragraphe 8 de la décision n° 2019-831 QPC du 12 mars 2020, relative à la rédaction issue de l'ordonnance n° 2017-1718 du 20 décembre 2017 : la limite régionale ne doit pas empêcher la poursuite de la représentation en appel par le défenseur choisi devant le conseil. Cette précision ne crée pas de compétence territoriale générale hors région pour les autres affaires."
    },
    "L1453-5": {
        "paragraphs": [
            "Dans un établissement qui compte au moins onze salariés, le défenseur syndical bénéficie du temps nécessaire pour exercer ses fonctions, dans la limite de dix heures par mois."
        ],
        "reason": "Réécriture à droit constant : le seuil d'effectif est formulé comme une condition explicite, suivie du droit au temps nécessaire et de sa limite. Aucune réforme de fond.",
        "review_notes": "Le seuil demeure de onze salariés au moins, apprécié dans l'établissement, et la limite de dix heures par mois. Note historique : le V de l'article 259 de la loi n° 2015-990 du 6 août 2015 prévoit l'entrée en vigueur au plus tard le premier jour du douzième mois suivant la publication de cette loi. Ce délai historique n'est pas réouvert."
    },
    "L1453-6": {
        "paragraphs": [
            "Le temps que le défenseur syndical consacre à sa mission hors de l'entreprise pendant ses heures de travail est assimilé à une durée de travail effectif pour déterminer la durée de ses congés payés, ses droits aux prestations d'assurances sociales et aux prestations familiales, ainsi que tous les droits qu'il tient de son ancienneté dans l'entreprise.",
            "L'employeur rémunère ces absences, qui n'entraînent aucune diminution des rémunérations ni des avantages correspondants.",
            "L'Etat rembourse aux employeurs les salaires maintenus pendant les absences du défenseur syndical pour l'exercice de sa mission, ainsi que les avantages et les charges sociales correspondants.",
            "Un décret fixe les modalités d'indemnisation du défenseur syndical qui exerce son activité professionnelle en dehors de tout établissement ou qui dépend de plusieurs employeurs."
        ],
        "reason": "Réécriture à droit constant : les quatre alinéas substantiels sont rendus lisibles et conservés dans leur ordre, avec des sujets explicites pour la rémunération et le remboursement. Tous les droits assimilés au travail effectif et les deux situations particulières d'indemnisation sont maintenus, sans réforme de fond.",
        "review_notes": "L'assimilation reste limitée au temps consacré à la mission hors de l'entreprise pendant les heures de travail et couvre congés payés, assurances sociales, prestations familiales et droits d'ancienneté. Le remboursement par l'Etat comprend salaires, avantages et charges sociales. Note historique : entrée en vigueur au plus tard le premier jour du douzième mois suivant la publication de la loi n° 2015-990 du 6 août 2015, conformément au V de son article 259. Les sauts de ligne purement matériels et le paragraphe final vide ne portent aucune règle omise."
    },
    "L1453-7": {
        "paragraphs": [
            "A la demande du défenseur syndical, l'employeur lui accorde les autorisations d'absence nécessaires à sa formation. Leur durée est limitée à deux semaines par période de quatre ans suivant la publication de la liste des défenseurs syndicaux sur laquelle il est inscrit.",
            "Ces autorisations d'absence sont soumises à l'article L. 3142-12. L'employeur rémunère les absences correspondantes."
        ],
        "reason": "Réécriture à droit constant : la demande du défenseur, l'obligation de l'employeur, le plafond de formation et la rémunération sont formulés directement. Le renvoi de la source est conservé avec signalement de son incohérence ; aucune réforme de fond n'est appliquée.",
        "review_notes": "Incohérence préexistante : le second alinéa vise L. 3142-12, alors que la note source indique que, conformément à l'article 33 de la loi n° 2016-1088 du 8 août 2016, cet article est devenu L. 2145-10. Le corpus public confirme que L. 2145-10 porte les règles de formation concernées et que l'actuel L. 3142-12 a un contenu distinct. Le renvoi de la source n'est pas corrigé silencieusement : une coordination explicite doit substituer L. 2145-10 à L. 3142-12 au second alinéa. Sont maintenus deux semaines par période de quatre ans et le point de départ lié à la publication de la liste d'inscription."
    },
    "L1453-8": {
        "paragraphs": [
            "Le défenseur syndical doit respecter le secret professionnel pour toutes les questions relatives aux procédés de fabrication.",
            "Il est également soumis à une obligation de discrétion pour les informations qui présentent un caractère confidentiel et sont données comme telles par la personne qu'il assiste ou représente ou par la partie adverse dans le cadre d'une négociation.",
            "En cas de manquement à l'une de ces obligations, l'autorité administrative peut le radier de la liste des défenseurs syndicaux."
        ],
        "reason": "Réécriture à droit constant : les obligations de secret et de discrétion puis la conséquence possible de leur méconnaissance sont présentées dans trois alinéas lisibles, dans l'ordre de la source. L'autorité compétente pour la radiation est le sujet explicite de la dernière phrase ; aucune réforme de fond.",
        "review_notes": "Le secret professionnel reste propre aux procédés de fabrication. La discrétion conserve les conditions cumulatives du caractère confidentiel et de l'information donnée comme telle, ainsi que les personnes et le cadre de négociation mentionnés dans la source. La radiation reste facultative. Note historique : entrée en vigueur au plus tard le premier jour du douzième mois suivant la publication de la loi n° 2015-990 du 6 août 2015, en application du V de son article 259."
    },
    "L1453-9": {
        "paragraphs": [
            "Aucune sanction disciplinaire ni aucune rupture du contrat de travail ne peut être fondée sur l'exercice de la mission de défenseur syndical.",
            "Le licenciement d'un défenseur syndical doit suivre la procédure d'autorisation administrative prévue au livre IV de la deuxième partie."
        ],
        "reason": "Réécriture à droit constant : la protection est formulée comme une interdiction explicite de fonder une sanction disciplinaire ou une rupture sur la mission. La procédure d'autorisation administrative reste dans son alinéa, sans réforme de fond.",
        "review_notes": "La protection concerne la mission de défenseur syndical et ne supprime pas l'autorisation administrative de licenciement. Le renvoi au livre IV de la deuxième partie est conservé. Note historique : le V de l'article 259 de la loi n° 2015-990 du 6 août 2015 prévoit une entrée en vigueur au plus tard le premier jour du douzième mois suivant la publication de cette loi. Les réformes des ruptures du CDI ne sont pas étendues à ce régime protecteur."
    },
    "L1454-1": {
        "paragraphs": [
            "Le bureau de conciliation et d'orientation a pour mission de concilier les parties.",
            "Pour accomplir cette mission, il peut entendre chaque partie séparément et de manière confidentielle."
        ],
        "reason": "Réécriture à droit constant : la mission et la faculté d'audition séparée sont distinguées en deux alinéas, conformément aux séparations du texte source. La confidentialité est maintenue, sans réforme de fond.",
        "review_notes": "L'audition séparée demeure une faculté liée à la mission de conciliation. Application temporelle à conserver selon la note source : ces dispositions concernent les instances introduites devant les conseils de prud'hommes à compter de la publication de la loi n° 2015-990 du 6 août 2015. Cette borne ne devient pas une date d'entrée en vigueur de la présente réécriture."
    },
    "L1454-1-1": {
        "paragraphs": [
            "Lorsque la conciliation échoue, le bureau de conciliation et d'orientation peut, par simple mesure d'administration judiciaire, procéder à l'un des renvois suivants :",
            "1° Si le litige porte sur un licenciement ou sur une demande de résiliation judiciaire du contrat de travail, renvoyer les parties, avec leur accord, devant le bureau de jugement dans sa composition restreinte mentionnée à l'article L. 1423-13. Cette formation doit statuer dans un délai de trois mois ;",
            "2° Si les parties le demandent ou si la nature du litige le justifie, renvoyer les parties devant le bureau de jugement mentionné à l'article L. 1423-12, présidé par le juge mentionné à l'article L. 1454-2. Dans ce cas, l'article L. 1454-4 ne s'applique pas.",
            "A défaut d'un tel renvoi, l'affaire est renvoyée devant le bureau de jugement mentionné à l'article L. 1423-12.",
            "La formation saisie est compétente pour examiner l'ensemble des demandes des parties, y compris leurs demandes additionnelles ou reconventionnelles."
        ],
        "reason": "Réécriture à droit constant : les conditions des deux orientations sont placées avant chacune des décisions possibles, puis le renvoi par défaut est distingué de la compétence sur toutes les demandes. Les cinq alinéas substantiels et les numéros 1° et 2° sont conservés, sans réforme de fond.",
        "review_notes": "Sont conservés l'accord des parties au 1°, son champ limité au licenciement ou à la résiliation judiciaire et le délai de trois mois, sans point de départ ajouté. Le 2° reste possible sur demande des parties ou en raison de la nature du litige ; L. 1454-4 y reste exclu. Renvois L. 1423-12, L. 1423-13, L. 1454-2 et L. 1454-4 vérifiés dans le corpus ou le lot. Application temporelle issue de la note : instances introduites devant les conseils de prud'hommes à compter de la publication de la loi n° 2015-990 du 6 août 2015."
    },
    "L1454-1-2": {
        "paragraphs": [
            "Le bureau de conciliation et d'orientation est chargé de la mise en état des affaires.",
            "Si une affaire portée devant le bureau de jugement n'est pas en état d'être jugée, ce bureau peut en assurer la mise en état.",
            "Un ou deux conseillers rapporteurs peuvent être désignés pour mettre l'affaire en état d'être jugée. Ils prescrivent toutes les mesures nécessaires à cette fin.",
            "A la demande des conseillers rapporteurs, les agents de contrôle mentionnés à l'article L. 8271-1-2 leur communiquent les renseignements et les documents dont ils disposent concernant le travail dissimulé, le marchandage ou le prêt illicite de main-d'œuvre. Ils ne peuvent opposer le secret professionnel à cette communication.",
            "Le bureau de conciliation et d'orientation, les conseillers rapporteurs désignés par le bureau de conciliation et d'orientation ou le bureau de jugement peuvent prononcer, par ordonnance, la clôture de l'instruction. Une copie de cette ordonnance est remise aux parties ou à leur conseil. L'ordonnance constitue une mesure d'administration judiciaire."
        ],
        "reason": "Réécriture à droit constant : les responsabilités de mise en état restent réparties dans les cinq alinéas, et les obligations de communication ainsi que les effets de l'ordonnance de clôture sont exposés en phrases distinctes. Aucune réforme de fond.",
        "review_notes": "Le nombre de conseillers rapporteurs reste d'un ou deux. Les trois domaines de communication et l'inopposabilité du secret professionnel sont conservés ; le renvoi à L. 8271-1-2 a été vérifié. La formulation de la source désignant les autorités de clôture est conservée pour ne pas en modifier le périmètre. Les articles R. 1454-3, R. 1454-4 et R. 1454-19-1 du corpus confirment les mécanismes de désignation et les pouvoirs des rapporteurs. La remise d'une copie aux parties ou à leur conseil et la qualification de mesure d'administration judiciaire sont maintenues."
    },
    "L1454-1-3": {
        "paragraphs": [
            "Si une partie, sans motif légitime, ne comparaît ni personnellement ni par représentation selon les modalités prévues par décret en Conseil d'Etat, le bureau de conciliation et d'orientation peut juger l'affaire en l'état des pièces et moyens communiqués contradictoirement par la partie comparante.",
            "Il statue alors en tant que bureau de jugement, dans sa composition restreinte mentionnée à l'article L. 1423-13."
        ],
        "reason": "Réécriture à droit constant : l'absence de comparution personnelle comme de représentation est formulée explicitement, avec maintien du motif légitime et du contradictoire. Les deux alinéas sont conservés ; aucune réforme de fond.",
        "review_notes": "Le pouvoir de juger demeure facultatif et suppose une absence sans motif légitime. Les modalités de représentation restent renvoyées à un décret en Conseil d'Etat, et seules sont visées les pièces et moyens communiqués contradictoirement. Le renvoi à la composition restreinte de L. 1423-13 est conservé et vérifié. La note source réserve ces dispositions aux instances introduites devant les conseils de prud'hommes à compter de la publication de la loi n° 2015-990 du 6 août 2015 ; cette règle temporelle est maintenue."
    },
    "L1454-2": {
        "paragraphs": [
            "En cas de partage des voix, l'affaire est renvoyée devant le même bureau de jugement ou la même formation de référé. Le bureau ou la formation siège alors sous la présidence d'un juge du tribunal judiciaire dans le ressort duquel se trouve le siège du conseil de prud'hommes. L'affaire est reprise dans le délai d'un mois.",
            "En cas de partage des voix devant le bureau de conciliation et d'orientation, ce bureau renvoie l'affaire devant le bureau de jugement, sous la présidence d'un juge du tribunal judiciaire dans le ressort duquel se trouve le siège du conseil de prud'hommes.",
            "Le président du tribunal judiciaire désigne chaque année les juges chargés de ces fonctions, en tenant compte notamment de leurs aptitudes et de leurs connaissances particulières."
        ],
        "reason": "Réécriture à droit constant : le renvoi, la présidence et le délai sont séparés dans le premier alinéa ; l'auteur du renvoi et celui des désignations annuelles sont nommés explicitement. Les trois alinéas et leurs champs respectifs sont conservés, sans réforme de fond.",
        "review_notes": "Le renvoi se fait devant le même bureau de jugement ou la même formation de référé au premier alinéa, mais devant le bureau de jugement en cas de partage au bureau de conciliation et d'orientation. Le délai d'un mois reste au seul premier alinéa. Le ressort du tribunal judiciaire et la désignation annuelle par son président, notamment selon aptitudes et connaissances particulières, sont maintenus. Note historique : entrée en vigueur au 1er janvier 2020 en application de l'article 36 de l'ordonnance n° 2019-964 du 18 septembre 2019 ; aucune date nouvelle n'est déduite de cette note."
    }
}


sources = json.loads(Path("source.json").read_text())
assert len(sources) == 24
assert set(drafts) == {source["number"] for source in sources}
answer = []
for source in sources:
    draft = drafts[source["number"]]
    record = {key: source[key] for key in ("code_id", "source_id", "source_sha256", "number")}
    record.update(
        proposed_xml="".join(f"<p>{text}</p>" for text in draft["paragraphs"]),
        reason=draft["reason"],
        review_notes=draft["review_notes"],
        status="rewrite_draft",
    )
    answer.append(record)

Path("answer.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")
print(f"answer.json : {len(answer)} articles")
