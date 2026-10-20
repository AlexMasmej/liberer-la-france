import json
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
drafts = {}


def add(number, paragraphs, reason, review_notes, removed=None):
    item = {
        'proposed_xml': '\n'.join('<p>' + p + '</p>' for p in paragraphs),
        'reason': reason,
        'review_notes': review_notes,
    }
    if removed:
        item.update(
            change_type='normative_reduction',
            reform_policy_id='editorial_direction_2026_10_19',
            removed_provisions=removed,
        )
    drafts[number] = item


add('L2241-1', [
    "Les organisations liées par une convention de branche ou, à défaut, par des accords professionnels se réunissent pour négocier sur les thèmes énumérés ci-dessous. Elles négocient au moins une fois tous les quatre ans sur les thèmes mentionnés aux 1° à 5° bis et au moins une fois tous les cinq ans sur ceux mentionnés aux 6° et 7° :",
    "1° Les salaires ;",
    "2° Les mesures visant à assurer l'égalité professionnelle entre les femmes et les hommes, les mesures de rattrapage des inégalités constatées et la mise à disposition d'outils aux entreprises pour prévenir le harcèlement sexuel et les agissements sexistes et agir contre ces faits ;",
    "2° bis Les mesures facilitant la conciliation de la vie professionnelle et de la vie personnelle des salariés proches aidants ;",
    "3° Les conditions de travail, la gestion prévisionnelle des emplois et des compétences et la prise en compte des effets de l'exposition aux facteurs de risques professionnels énumérés à l'article L. 4161-1 ;",
    "4° Les mesures favorisant l'insertion professionnelle et le maintien dans l'emploi des travailleurs handicapés ;",
    "5° Les priorités, les objectifs et les moyens de la formation professionnelle des salariés ;",
    "5° bis L'emploi et le travail des salariés expérimentés, en considération de leur âge ;",
    "6° La nécessité de réviser les classifications, compte tenu de l'objectif d'égalité professionnelle entre les femmes et les hommes et de mixité des emplois ;",
    "7° L'institution d'un ou plusieurs plans d'épargne interentreprises ou plans d'épargne pour la retraite d'entreprise collectifs interentreprises, lorsqu'aucun accord n'a été conclu à ce niveau en la matière.",
],
    "Réécriture à droit constant du socle de négociation obligatoire : les sujets et leurs deux périodicités sont rendus explicites. Le maintien des salaires, de la prévention des discriminations et des risques, de l'insertion et de l'accès à la formation répond à une fonction essentielle. L'allègement des périodicités supplétives est porté par les articles qui les fixent, sans supprimer ces négociations ni les dispositifs favorables.",
    "Contrôle : quatre ans pour les 1° à 5° bis, cinq ans pour les 6° et 7° ; le 2° bis relatif aux proches aidants et la condition d'absence d'accord du 7° demeurent. Le renvoi à L4161-1 a été lu, y compris sa transition historique. Aucun nouveau rapport, minimum de réunions CPPNI ni transmission supprimée par la coordination L2232 n'est ajouté. Les aides, aménagements et dispositifs d'épargne restent ouverts aux futures situations éligibles ; aucune réforme fiscale ou de retraite n'est déduite de ces seuls thèmes."
)

add('L2241-2', [
    "Lorsqu'au moins un tiers de l'effectif de la branche professionnelle occupe un emploi à temps partiel, les organisations liées par une convention de branche ou, à défaut, par des accords professionnels ouvrent une négociation sur l'organisation du temps partiel. Cette négociation porte notamment sur le volume de travail garanti par le contrat, le nombre et la durée des interruptions d'activité, le délai de prévenance préalable aux modifications des horaires et la rémunération des heures complémentaires.",
    "La négociation peut fixer une durée minimale conventionnelle hebdomadaire ou mensuelle plus favorable aux salariés. Les minima conventionnels plus favorables demeurent applicables. Le présent article n'institue aucun plancher légal général de vingt-quatre heures et ne déroge ni au minimum spécial de seize heures hebdomadaires prévu au 2° de l'article L. 1225-47 ni aux priorités d'accès à l'emploi prévues à l'article L. 3123-3.",
    "Ces dispositions s'appliquent aux négociations ouvertes à compter de l'entrée en vigueur de la loi. Elles n'abaissent ni les volumes contractuels déjà garantis ni les droits résultant des accords en vigueur.",
],
    "Réforme de coordination du temps partiel : l'obligation de négocier une durée minimale hebdomadaire ou mensuelle est retirée au profit du volume contractuel garanti. La fixation d'un minimum conventionnel favorable reste possible. À droit constant, le seuil d'un tiers, les interruptions d'activité, la prévenance et la rémunération des heures complémentaires sont conservés.",
    "Discordance explicite avec coordination.travail : elle rattache le minimum parental de seize heures à L3123-3. Or les sources publiques intégralement lues placent ce minimum au 2° de L1225-47 ; L3123-3 organise des priorités d'accès à un emploi et ne comporte pas ce chiffre. La proposition préserve séparément les deux protections sur leurs fondements vérifiés ; l'attribution faite dans coordination.json reste à rectifier, sans modifier ici ces articles hors lot. La source assignée ne fixe pas elle-même vingt-quatre heures : leur suppression générale relève des L3123-6, L3123-7, L3123-19 et L3123-27 coordonnés dans travail, dont les sources ont été lues. L2241-5 c) et L2241-7 conservent le déclenchement d'un tiers. Aucun minimum conventionnel favorable ni volume acquis n'est supprimé, pour les contrats existants comme pour les futurs salariés éligibles ; aucune créance ou obligation antérieure n'est effacée.",
    ["L'obligation de négocier une durée minimale d'activité hebdomadaire ou mensuelle est supprimée ; une durée minimale conventionnelle favorable reste librement négociable, avec maintien des minima applicables."]
)

add('L2241-2-1', [
    "L'accord de branche conclu lors de la négociation prévue au 5° bis de l'article L. 2241-1 peut prévoir un plan d'action type destiné aux entreprises de moins de trois cents salariés.",
    "Lorsqu'une négociation sur l'emploi et le travail des salariés expérimentés, en considération de leur âge, menée avec les organisations syndicales de salariés représentatives dans l'entreprise n'aboutit pas à un accord collectif, l'employeur peut appliquer ce plan par un document unilatéral. Il informe et consulte préalablement, par tous moyens, les salariés ainsi que le comité social et économique, lorsqu'il existe dans l'entreprise.",
],
    "Réécriture à droit constant d'une faculté de simplification favorable aux entreprises de moins de trois cents salariés. Le recours au plan type reste possible après l'échec de la négociation, sans nouvelle homologation, formulaire ou transmission. L'information et la consultation sont conservées pour assurer la participation effective des intéressés.",
    "Le seuil est strictement inférieur à trois cents salariés. L'échec préalable concerne la négociation avec les syndicats représentatifs de l'entreprise ; le document unilatéral ne vaut pas accord collectif. Le plan type de branche reste facultatif et accessible aux futures entreprises éligibles. L'information et la consultation portent à la fois sur les salariés et sur le CSE s'il existe, conformément à la source. Le renvoi au 5° bis de L2241-1 est conservé ; la nouvelle périodicité supplétive de branche ne supprime pas ce dispositif."
)

add('L2241-3', [
    "Lorsque les négociations ne sont pas engagées sérieusement et loyalement, une commission mixte est réunie dans les conditions prévues à l'article L. 2261-20.",
    "La partie patronale doit communiquer aux organisations syndicales les informations nécessaires pour négocier en toute connaissance de cause. Elle répond de manière motivée à leurs propositions éventuelles. Ces obligations conditionnent le caractère sérieux et loyal de l'engagement des négociations.",
    "Une information exacte, à jour et déjà effectivement accessible à tous les négociateurs destinataires n'a pas à être transmise de nouveau. Une référence précise à cette information et à son emplacement suffit, à condition d'en garantir l'accès effectif pendant la négociation. Les informations manquantes ou modifiées sont communiquées ; les délais nécessaires à leur examen, notamment les délais réglementaires applicables, restent respectés.",
    "La dispense de transmission répétée s'applique dès l'entrée en vigueur de la loi, y compris aux négociations en cours. Elle ne supprime aucune information nécessaire, aucune réponse motivée ni aucun recours relatif à un manquement antérieur.",
],
    "Réforme de fond limitée aux doubles transmissions : les informations déjà exactes, à jour et réellement accessibles peuvent être désignées par un renvoi précis au lieu d'être remises à nouveau. À droit constant, la loyauté, les réponses motivées et l'intervention de la commission mixte en cas de défaillance restent exigées.",
    "L2261-20 a été lu : l'administration peut réunir la commission à la demande d'une organisation représentative ou de sa propre initiative et doit la convoquer lorsque deux organisations la demandent. Ces voies ne sont pas restreintes. Le renvoi documentaire ne peut couvrir une information inaccessible ou périmée. D2241-1, lu, prévoit quinze jours avant la négociation salariale : ce délai de préparation n'est pas retiré. Coordonner la rédaction réglementaire pour admettre l'accès déjà assuré sans rapport ou envoi répété, sans recréer une transmission CPPNI ou une attestation de remplacement.",
    ["La remise répétée des informations nécessaires déjà exactes, à jour et effectivement accessibles à tous leurs destinataires est supprimée ; un renvoi précis suffit sans nouvelle attestation."]
)

add('L2241-4', [
    "À la demande de l'une d'entre elles, les organisations liées par une convention de branche ou, à défaut, par des accords professionnels peuvent ouvrir une négociation sur le calendrier, la périodicité, les thèmes et les modalités des négociations dans la branche ou le secteur professionnel concerné.",
],
    "Réécriture à droit constant : l'initiative d'une seule organisation et le caractère facultatif de la négociation d'organisation sont explicités. Cette faculté permet d'adapter les négociations sans autorisation préalable ; sa suppression retirerait un instrument de simplification plutôt qu'une charge.",
    "Conserver le choix d'engager cette négociation, le champ branche ou secteur professionnel et les quatre objets énumérés. La demande ne vaut pas conclusion d'un accord ni modification unilatérale des périodicités. L'accord éventuel relève de L2241-5 et des règles générales de validité ; aucune majorité, opposition ou garantie de participation n'est modifiée ici."
)

add('L2241-5', [
    "L'accord conclu à l'issue de la négociation prévue à l'article L. 2241-4 précise :",
    "1° Les thèmes et la périodicité des négociations, dans les conditions suivantes :",
    "a) Les thèmes mentionnés aux 1° à 5° bis de l'article L. 2241-1 sont négociés au moins tous les quatre ans ;",
    "b) Les thèmes mentionnés aux 6° et 7° de l'article L. 2241-1 sont négociés au moins tous les cinq ans ;",
    "c) Le thème mentionné à l'article L. 2241-2 est négocié lorsque les conditions prévues par cet article sont réunies ;",
    "2° Le contenu de chaque thème ;",
    "3° Le calendrier des réunions ou les modalités permettant de le fixer au cours de l'exécution de l'accord ; les lieux des réunions n'ont pas à être fixés dans cet accord ;",
    "4° Les informations que les organisations professionnelles d'employeurs communiquent aux négociateurs sur les thèmes de la négociation à ouvrir, ainsi que la date de cette communication, sous réserve de la dispense de transmission répétée prévue à l'article L. 2241-3 ;",
    "5° Les modalités de suivi des engagements pris par les parties.",
    "L'accord peut être conclu pour une durée déterminée ou indéterminée dans les conditions de l'article L. 2222-4. Sa durée ne dispense pas de respecter les périodicités prévues au 1°.",
    "Ces dispositions s'appliquent aux accords conclus à compter de l'entrée en vigueur de la loi. Les accords antérieurs conservent leur durée et leurs engagements ; leur prolongation ou leur modification suppose l'accord des parties dans les conditions de droit commun.",
],
    "Réforme de fond : suppression de l'obligation de prédéterminer les lieux et de fixer immédiatement tout le calendrier, ainsi que de la limite spéciale de cinq ans imposant de renouveler l'accord d'organisation. Une durée indéterminée est permise sans allonger les intervalles obligatoires entre négociations. Les thèmes, informations utiles, dates de communication et modalités de suivi sont intégralement conservés.",
    "Les numéros 1° à 5° et lettres a), b), c) restent à leur place. Quatre ans et cinq ans sont les plafonds de périodicité existants, non des délais minimaux. L2222-4 a été lu : en l'absence de stipulation de durée, la durée de droit commun demeure cinq ans ; l'option indéterminée doit donc être stipulée. Aucun accord ancien n'est prolongé automatiquement. L2231-6 et les règles de validité restent applicables. Le 4° conserve la date de mise à disposition et les délais utiles ; le renvoi à L2241-3 évite les doubles remises sans retirer le droit d'information.",
    [
        "L'obligation de fixer les lieux des réunions dans l'accord d'organisation est supprimée, ainsi que l'exigence d'un calendrier entièrement prédéterminé lorsque l'accord en définit les modalités de fixation.",
        "La durée maximale spéciale de cinq ans de l'accord d'organisation est supprimée ; le droit commun permet une durée indéterminée sans dispenser des négociations périodiques.",
    ]
)

add('L2241-6', [
    "Un accord portant sur l'un des domaines énumérés à l'article L. 2241-1 peut fixer la périodicité de sa renégociation. Cette périodicité ne peut dépasser quatre ans pour les domaines mentionnés aux 1° à 5° bis de cet article, ni cinq ans pour ceux mentionnés aux 6° et 7°.",
],
    "Réécriture à droit constant de la faculté de fixer une périodicité par accord thématique. Les deux plafonds sont séparés pour en clarifier l'application. Cette faculté évite un accord d'organisation distinct et doit rester disponible ; elle n'ajoute ni formalité ni négociation supplémentaire.",
    "Les plafonds de quatre et cinq ans et les groupes de subdivisions de L2241-1 sont exactement conservés. Le 2° bis et le 5° bis sont compris dans le premier groupe. La suppression de la durée maximale spéciale de l'accord d'organisation à L2241-5 ne supprime aucun plafond de renégociation ni les engagements plus fréquents valablement convenus."
)

add('L2241-7', [
    "En l'absence d'accord prévu à l'article L. 2241-5 ou si ses stipulations ne sont pas respectées, les organisations liées par une convention de branche ou, à défaut, par des accords professionnels engagent les négociations prévues aux articles L. 2241-1 et L. 2241-2 selon les modalités des sous-sections 2 à 6 de la présente section.",
    "Les périodicités supplétives résultant de la loi s'appliquent, dès son entrée en vigueur, aux échéances légales qui ne sont pas encore échues. Elles se calculent à partir de l'ouverture de la précédente négociation sur le même thème, sans nouveau point de départ à l'entrée en vigueur de la loi. Une négociation en cours se poursuit sans nouvelle ouverture. Les obligations déjà échues et les recours qui s'y rapportent conservent leur régime, sous réserve de l'application de la loi répressive plus douce aux sanctions non définitives.",
    "Les accords en vigueur conservent leurs engagements, notamment une périodicité plus fréquente. L'application des dispositions supplétives en cas de non-respect d'un accord n'éteint ni ces engagements ni les recours auxquels leur méconnaissance ouvre droit.",
],
    "Réécriture du mécanisme supplétif et coordination de sa transition. Les négociations obligatoires subsistent ; les allègements des articles L2241-8, L2241-11 à L2241-14 et L2241-14-1 profitent aux échéances légales futures sans remettre les compteurs à zéro ni effacer une obligation déjà échue. Les droits conventionnels plus favorables et les recours sont réservés.",
    "Le renvoi global aux sous-sections 2 à 6 est conservé tel qu'il figure dans la source ; il n'est pas réduit aux seuls articles du lot. Cette disposition ne modifie pas la périodicité supplétive propre à l'entreprise de L2242-13, L2242-20 ou L2242-22. Aucun manquement antérieur n'est amnistié ; l'application de la loi répressive plus douce aux sanctions non définitives reste réservée. La règle de calcul à partir de la précédente ouverture évite qu'une entrée en vigueur ne crée quatre années supplémentaires après une période déjà écoulée."
)

add('L2241-8', [
    "Les organisations liées par une convention de branche ou, à défaut, par des accords professionnels se réunissent au moins une fois tous les quatre ans pour négocier sur les salaires, sans préjudice d'une périodicité plus fréquente prévue par un accord en vigueur et du déclenchement prévu à l'article L. 2241-10.",
    "La négociation prend en compte l'objectif d'égalité professionnelle entre les femmes et les hommes et les mesures permettant de l'atteindre.",
    "Par dérogation au premier alinéa de l'article L. 2241-9, l'examen des données prévu par cet article a lieu à l'occasion de la négociation sur les salaires, sans examen annuel distinct imposé sur ce seul fondement. Toutes les catégories de données et les informations nécessaires prévues par cet article demeurent examinées et accessibles aux négociateurs.",
    "La transition prévue à l'article L. 2241-7 s'applique à cette périodicité. Le présent article ne réduit ni les salaires dus, ni les minima applicables, ni les droits à l'égalité de rémunération.",
],
    "Réforme de fond : l'annualité supplétive de branche est supprimée au profit de la périodicité de quatre ans déjà admise par L2241-1 et L2241-6. La coordination expresse de L2241-9 empêche que l'examen annuel des données ne rétablisse une réunion annuelle. Les sujets, l'information et l'égalité salariale sont maintenus, ainsi que les calendriers conventionnels plus fréquents et la négociation déclenchée par un minimum professionnel inférieur au SMIC.",
    "L2241-9 a été lu intégralement : les trois catégories de données, les actions de prévention, la ventilation des salaires par sexe et catégories et la détermination réglementaire des informations demeurent. La dérogation ne porte que sur leur annualité légale distincte. Coordonner sa rédaction et les intitulés de sous-sections, ainsi que D2241-1 ; le délai de préparation de quinze jours n'est pas supprimé. L7113-4 a été lu : les salaires des journalistes professionnels permanents ou occasionnels restent inclus. Les articles L2241-11, L2241-17 et L2241-18 du lot cessent de rétablir l'annualité par leur formulation. L'égalité de rémunération reste immédiatement opposable sans attendre quatre ans ; aucune conformité au droit supérieur n'est présumée par un seul contrôle rédactionnel.",
    [
        "L'obligation supplétive de se réunir chaque année en branche pour négocier les salaires est supprimée ; une négociation au moins quadriennale demeure exigée.",
        "L'examen annuel distinct des données de L2241-9 est supprimé par dérogation expresse ; l'intégralité de ces données reste examinée lors de la négociation salariale.",
    ]
)

add('L2241-10', [
    "Lorsque le salaire minimum national professionnel des salariés sans qualification, au sens du 4° du II de l'article L. 2261-22, est inférieur au salaire minimum interprofessionnel de croissance, les organisations liées par une convention de branche ou, à défaut, par des accords professionnels se réunissent pour négocier sur les salaires.",
    "Si la partie patronale n'a pas pris l'initiative de cette négociation, une organisation syndicale de salariés représentative au sens de l'article L. 2231-1 peut en demander l'ouverture dès que cette situation est constatée. La négociation s'engage dans les quinze jours suivant cette demande, sans délai préalable de quarante-cinq jours réservé à l'initiative patronale.",
    "Ces dispositions s'appliquent dès l'entrée en vigueur de la loi, y compris lorsque le salaire minimum professionnel est déjà inférieur au salaire minimum interprofessionnel de croissance. Une demande déjà présentée conserve sa date et ne doit pas être renouvelée ; aucun délai antérieurement commencé n'est prolongé.",
],
    "Réforme de fond : retrait du délai de quarante-cinq jours qui retarde le droit syndical de déclencher la négociation lorsque le minimum professionnel passe sous le SMIC. Le délai maximal de quinze jours après la demande est conservé. Le déclenchement correcteur subsiste indépendamment de l'allègement de la périodicité ordinaire de branche.",
    "L2261-22 II 4° et L2231-1 ont été lus ; la qualification des salariés sans qualification et la représentativité syndicale ne sont pas modifiées. Le délai de quinze jours est un maximum d'ouverture après demande, non le préavis individuel de rupture de quinze jours du contrat unique. Ni le niveau du SMIC, ni l'application immédiate des minima, ni les rappels de salaire ne sont modifiés. Le traitement des demandes déjà formées évite une reprise des délais au détriment des salariés.",
    ["Le délai préalable de quarante-cinq jours durant lequel l'absence d'initiative patronale empêchait le déclenchement syndical obligatoire est supprimé."]
)

add('L2241-11', [
    "Les organisations liées par une convention de branche ou, à défaut, par des accords professionnels se réunissent au moins une fois tous les quatre ans pour négocier sur les mesures visant à assurer l'égalité professionnelle entre les femmes et les hommes et sur les mesures de rattrapage des inégalités constatées. Lorsque le rattrapage porte sur des mesures salariales, sa mise en œuvre est suivie dans le cadre de la négociation obligatoire sur les salaires prévue à l'article L. 2241-8.",
    "La négociation porte notamment sur :",
    "1° Les conditions d'accès à l'emploi, à la formation et à la promotion professionnelle ;",
    "2° Les conditions de travail et d'emploi, notamment celles des salariés à temps partiel.",
    "Les informations nécessaires à la négociation sont déterminées par voie réglementaire. Elles peuvent être réunies dans des documents existants, qui tiennent lieu du rapport spécifique dès lors qu'ils présentent une situation comparée complète et à jour des femmes et des hommes dans les domaines des 1° et 2°, avec les indicateurs chiffrés pertinents pour chaque secteur d'activité. L'analyse permettant d'identifier les écarts de rémunération reste nécessaire ; elle n'exige pas un document distinct lorsque ces éléments la contiennent déjà. Les informations manquantes ou modifiées sont communiquées conformément à l'article L. 2241-3.",
    "La périodicité suit la transition prévue à l'article L. 2241-7. La dispense de document distinct s'applique dès l'entrée en vigueur de la loi, y compris aux négociations en cours, sans retirer les informations nécessaires ni les droits des négociateurs. Les mesures de rattrapage déjà convenues continuent de s'appliquer selon leurs engagements et leurs échéances.",
],
    "Réforme de fond : suppression de la périodicité supplétive triennale, remplacée par les quatre ans du socle d'ordre public, et suppression des rapports et diagnostics matériellement distincts lorsque des documents existants fournissent déjà tous leurs éléments. L'égalité, le rattrapage, les deux domaines de négociation et l'information comparée demeurent. La référence à une négociation salariale nécessairement annuelle est coordonnée avec L2241-8.",
    "D2241-2 a été lu intégralement : les données comparées dans les domaines 1° et 2°, les indicateurs chiffrés par secteur et l'identification des écarts de rémunération restent exigibles. Sa rédaction doit admettre le support existant et cesser d'imposer un rapport séparé ou une périodicité triennale. La dispense n'est pas une dispense d'analyse, de communication utile ou de rattrapage, et ne crée pas une nouvelle déclaration. Les calendriers conventionnels plus fréquents et les créances de rémunération subsistent. Les obligations d'égalité de rémunération et les protections de droit supérieur demeurent distinctes du rythme légal de négociation.",
    [
        "La périodicité supplétive de trois ans pour la négociation de branche sur l'égalité professionnelle est supprimée au profit de quatre ans, sans réduire les engagements conventionnels en vigueur.",
        "Le rapport spécifique et le support distinct de diagnostic des écarts ne sont plus requis lorsque les documents existants fournissent déjà intégralement les données comparées et l'analyse nécessaires.",
    ]
)

add('L2241-12', [
    "Les organisations liées par une convention de branche ou, à défaut, par des accords professionnels se réunissent au moins une fois tous les quatre ans pour négocier sur les conditions de travail, sur la gestion prévisionnelle des emplois et des compétences, notamment pour répondre aux enjeux de la transition écologique, et sur la prise en compte des effets de l'exposition aux facteurs de risques professionnels énumérés à l'article L. 4161-1.",
    "La gestion prévisionnelle des emplois et des compétences peut être négociée à l'échelle du territoire. La négociation veille à l'objectif de mixité des métiers et s'appuie sur les données pertinentes disponibles, notamment, lorsqu'ils sont disponibles, les travaux de l'observatoire prospectif des métiers et des qualifications mis en place par la commission paritaire nationale de l'emploi de la branche. Le recours à cet observatoire n'est pas une condition de la négociation ; le présent article n'impose pas la création ou le maintien d'un organisme distinct. L'analyse porte une attention particulière aux mutations professionnelles liées aux filières et aux métiers de la transition écologique et énergétique.",
    "Les mêmes organisations négocient également, au moins une fois tous les quatre ans, sur les matières définies aux articles L. 2242-15 et L. 2242-16. Ces matières peuvent être traitées au cours de la négociation prévue au premier alinéa ou d'une autre négociation de branche couvrant la même période ; celles déjà effectivement traitées n'ont pas à faire l'objet d'une seconde négociation pour satisfaire au présent alinéa.",
    "La transition prévue à l'article L. 2241-7 s'applique aux périodicités. Les dispenses de recours à un organisme distinct et de seconde négociation s'appliquent dès l'entrée en vigueur de la loi, sans faire obstacle à la poursuite des négociations en cours ni aux engagements conventionnels en vigueur. Les observatoires et les obligations d'information disposant d'un fondement autonome conservent leur régime.",
],
    "Réforme de fond : les deux rythmes supplétifs de trois ans sont alignés sur quatre ans ; le recours obligé aux travaux d'un observatoire déterminé est retiré et les mêmes matières déjà négociées ne déclenchent plus une seconde négociation. Le champ complet des conditions de travail, de la prévention, de la transition écologique et énergétique et des renvois est conservé. L'analyse utile est maintenue sans imposer une structure ou une procédure dédiée.",
    "L4161-1, L2242-15 et L2242-16 ont été lus intégralement. Les deux derniers renvois, bien qu'ils décrivent des matières de négociation en entreprise, figurent déjà dans la source de branche : ils sont conservés et cette articulation préexistante doit être explicitée lors de la coordination, non effacée. L2242-15 couvre salaires, temps de travail, intéressement, participation, épargne et suivi des écarts ; L2242-16 traite des mises à disposition syndicales. Leur renvoi ici n'importe pas leur annualité d'entreprise dans la branche et ne dispense pas les entreprises de leurs propres obligations. Aucun dispositif d'épargne, abondement, aide ou droit au congé n'est supprimé. Les références aux anciens CDD et à la précarité dans les données de L2241-9 et L2242-20 nécessitent leur coordination au contrat unique, sans ouvrir de nouveaux CDD. Le présent article ne supprime aucun observatoire institué par un autre fondement.",
    [
        "Les deux obligations supplétives de négocier tous les trois ans sont supprimées au profit d'un rythme de quatre ans, dans les limites de L2241-1 et sans effacer les calendriers conventionnels.",
        "Le recours obligatoire aux travaux d'un observatoire prospectif déterminé cesse d'être une condition de la négociation ; aucune création ou structure distincte n'est exigée sur ce seul fondement.",
        "Une seconde négociation des matières visées par les renvois à L2242-15 et L2242-16 n'est plus exigée lorsqu'elles ont été effectivement traitées dans la même période au niveau de la branche.",
    ]
)

add('L2241-13', [
    "Les organisations liées par une convention de branche ou, à défaut, par des accords professionnels se réunissent au moins une fois tous les quatre ans pour négocier sur les mesures favorisant l'insertion professionnelle et le maintien dans l'emploi des travailleurs handicapés.",
    "La négociation porte notamment sur les conditions d'accès à l'emploi, à la formation et à la promotion professionnelle, ainsi que sur les conditions de travail, d'emploi et de maintien dans l'emploi.",
    "Les informations nécessaires à la négociation sont déterminées par voie réglementaire. Les données et documents existants tiennent lieu du rapport spécifique lorsqu'ils présentent, pour chaque secteur d'activité, une situation complète et à jour au regard de l'obligation d'emploi des travailleurs handicapés prévue aux articles L. 5212-1 et suivants. Les informations manquantes ou modifiées sont communiquées conformément à l'article L. 2241-3, sans nouvelle collecte ou transmission des mêmes données déjà effectivement accessibles.",
    "La périodicité suit la transition prévue à l'article L. 2241-7. La dispense de rapport distinct s'applique dès l'entrée en vigueur de la loi, y compris aux négociations en cours. Les droits et mesures d'insertion, d'aménagement, de formation et de maintien dans l'emploi demeurent applicables dans leur champ propre.",
],
    "Réforme de fond : retrait du rythme supplétif triennal au profit des quatre ans du socle commun et suppression du rapport distinct lorsqu'il répète une information complète déjà disponible. À droit constant, l'insertion, le maintien dans l'emploi, tous les domaines d'accès et de conditions de travail et le droit aux informations nécessaires sont conservés.",
    "D2241-3 a été lu : le contenu sectoriel relatif à l'obligation d'emploi reste requis, seul le document spécifique redondant est dispensé. Coordonner sa périodicité et son support sans créer une déclaration de remplacement. Le présent article ne modifie ni l'obligation d'emploi des articles L5212-1 et suivants ni leurs règles de contribution, qui ne sont pas les prélèvements du présent lot. Les aménagements, aides, dispenses et avantages restent ouverts aux situations futures éligibles ; les accords en vigueur et les échéances déjà échues bénéficient de la transition de L2241-7.",
    [
        "La périodicité supplétive triennale de la négociation de branche relative aux travailleurs handicapés est supprimée au profit d'une périodicité de quatre ans.",
        "L'établissement d'un rapport spécifique répétant des données sectorielles complètes, exactes et à jour déjà effectivement disponibles est supprimé, sans réduction de l'information nécessaire.",
    ]
)

add('L2241-14', [
    "Les organisations liées par une convention de branche ou, à défaut, par un accord professionnel se réunissent au moins une fois tous les quatre ans pour négocier sur les priorités, les objectifs et les moyens de la formation professionnelle des salariés.",
    "La négociation porte notamment sur l'égal accès à la formation selon la catégorie professionnelle des salariés et la taille de leur entreprise, sur les abondements supplémentaires du compte personnel de formation, sur la validation des acquis de l'expérience, sur l'accès aux certifications et sur le développement du tutorat. Elle porte aussi sur la valorisation de la fonction de tuteur ou de maître d'apprentissage, en particulier sur les actions facilitant l'exercice de cette fonction et sur ses conditions d'exercice par les salariés âgés de plus de cinquante-cinq ans.",
    "La négociation sur la validation des acquis de l'expérience mentionnée à l'alinéa précédent porte sur :",
    "1° Les modalités d'information des entreprises et des salariés sur les actions de validation des acquis de l'expérience mises en œuvre pour obtenir une qualification mentionnée à l'article L. 6314-1 ;",
    "2° Les conditions favorisant l'accès des salariés à la validation des acquis de l'expérience, dans un cadre collectif ou individuel ;",
    "3° Les modalités de prise en charge, par les opérateurs de compétences, des dépenses liées à la participation d'un salarié à un jury d'examen ou de validation des acquis de l'expérience.",
    "La périodicité prévue au premier alinéa suit la transition de l'article L. 2241-7. Les abondements, prises en charge, aides et droits à la formation continuent de s'appliquer dans leur champ propre, y compris aux futures situations éligibles ; leur maintien ne dépend pas de l'ouverture d'une nouvelle négociation.",
],
    "Réforme de fond limitée au rythme supplétif : la négociation tous les trois ans est remplacée par une négociation au moins tous les quatre ans. La réécriture conserve tous les thèmes et les trois composantes de la validation des acquis. Elle protège explicitement les abondements et prises en charge, qui ne sont pas des formalités supprimées.",
    "Le seuil d'âge reste strictement supérieur à cinquante-cinq ans ; les opérateurs de compétences, les jurys d'examen et de VAE, les catégories professionnelles et la taille des entreprises restent mentionnés. L6314-1 a été lu : les trois voies de qualification demeurent couvertes par le renvoi inchangé. La note historique du PER figurant à L2241-16 n'est pas importée ici comme date de réforme. La durée d'une formation ou d'une mission de tutorat n'est pas une durée d'emploi ; apprentissage et professionnalisation nouveaux restent à coordonner au contrat unique sans fermer les aides ou exonérations futures. Aucun droit de formation, abondement CPF ou financement favorable n'est supprimé pour financer la réforme.",
    ["La réunion supplétive obligatoire au moins tous les trois ans sur la formation professionnelle est supprimée au profit d'une réunion au moins tous les quatre ans, sans réduction des droits financés."]
)

add('L2241-14-1', [
    "Les organisations liées par une convention de branche ou, à défaut, par des accords professionnels se réunissent au moins une fois tous les quatre ans pour engager une négociation sur l'emploi et le travail des salariés expérimentés, en considération de leur âge. La négociation analyse la situation de ces salariés à partir des informations nécessaires ; elle n'est pas subordonnée à l'établissement préalable d'un diagnostic dans un document distinct.",
    "La négociation porte sur :",
    "1° Le recrutement de ces salariés ;",
    "2° Leur maintien dans l'emploi ;",
    "3° L'aménagement des fins de carrière, en particulier l'accompagnement à la retraite progressive ou au temps partiel ;",
    "4° La transmission de leurs savoirs et de leurs compétences, en particulier les missions de mentorat, de tutorat et de mécénat de compétences.",
    "Les informations nécessaires à la négociation sont déterminées par voie réglementaire. L'analyse de la situation repose sur des indicateurs pertinents et chiffrés pour chacun des domaines mentionnés aux 1° à 4°. Les informations exactes et à jour déjà effectivement accessibles sont réutilisées dans les conditions de l'article L. 2241-3 ; seuls les éléments nécessaires manquants ou modifiés sont communiqués en complément.",
    "La périodicité suit la transition prévue à l'article L. 2241-7. La suppression du préalable documentaire s'applique dès l'entrée en vigueur de la loi, y compris aux négociations en cours, sans imposer de refaire un diagnostic déjà réalisé. Les droits à l'aménagement de fin de carrière, au temps partiel et à la retraite progressive restent ouverts selon leurs conditions propres.",
],
    "Réforme de fond : remplacement du rythme supplétif de trois ans par quatre ans et suppression du diagnostic documentaire préalable obligatoire. L'analyse de la situation et les indicateurs utiles demeurent dans la négociation ; elle peut utiliser directement les éléments existants. À droit constant, les quatre thèmes, notamment les dispositifs favorables de fin de carrière et la transmission des compétences, sont maintenus.",
    "D2241-5 a été lu : les indicateurs pertinents et chiffrés pour chaque domaine sont repris, sans maintenir un rapport autonome préalable. Coordonner ce règlement pour retirer sa qualification triennale et toute condition de diagnostic séparé. Le renvoi de L2242-22 aux matières des 1° à 4° reste opérant ; la suppression du préalable propre à la branche ne supprime pas par elle-même le diagnostic d'entreprise de L2242-22 et D2242-17, lus. La retraite progressive et le temps partiel conservent leur champ ; aucune baisse des pensions, durée d'emploi limitée ou nouvelle condition d'aide n'est créée ici. Le plan type de L2241-2-1 reste disponible pour les futures entreprises éligibles.",
    [
        "La périodicité supplétive de trois ans de la négociation de branche relative aux salariés expérimentés est supprimée au profit de quatre ans.",
        "L'établissement préalable d'un diagnostic dans un document distinct n'est plus une condition d'ouverture ; l'analyse et ses indicateurs sont intégrés à la négociation à partir des informations utiles.",
    ]
)

add('L2241-14-2', [
    "La négociation prévue à l'article L. 2241-14-1 peut également porter, pour les mêmes salariés, notamment sur :",
    "1° Le développement des compétences et l'accès à la formation ;",
    "2° Les effets des transformations technologiques et environnementales sur les métiers ;",
    "3° Les modalités de management du personnel ;",
    "4° Les modalités d'écoute, d'accompagnement et d'encadrement des salariés concernés ;",
    "5° La santé au travail et la prévention des risques professionnels ;",
    "6° L'organisation et les conditions de travail.",
],
    "Réécriture à droit constant d'une liste facultative : le rattachement de chaque thème à la négociation sur les salariés expérimentés est clarifié. Aucun de ces thèmes n'est transformé en obligation supplémentaire. Supprimer ces facultés fermerait des possibilités d'accompagnement, de formation et de prévention sans retirer une charge imposée par cet article.",
    "Les six subdivisions, le caractère non exhaustif de la liste et le mot peut sont conservés. Les thèmes de santé et de prévention restent à leur champ propre ; cet article ne modifie pas les obligations de sécurité. Le renvoi de L2242-22 à cette liste facultative reste valide pour l'entreprise, sans transposer à celle-ci la périodicité supplétive de branche."
)

add('L2241-15', [
    "Les organisations liées par une convention de branche ou, à défaut, par des accords professionnels se réunissent au moins une fois tous les cinq ans pour examiner s'il est nécessaire de réviser les classifications.",
    "La négociation prend en compte l'objectif d'égalité professionnelle entre les femmes et les hommes et de mixité des emplois.",
    "Lorsqu'un écart moyen de rémunération entre les femmes et les hommes est constaté, les organisations font de sa réduction une priorité.",
    "Lors de cet examen, les critères d'évaluation utilisés pour définir les différents postes de travail sont analysés. Cette analyse vise à identifier et à corriger les critères susceptibles d'entraîner des discriminations entre les femmes et les hommes et à garantir la prise en compte de l'ensemble des compétences des salariés.",
],
    "Réécriture à droit constant : l'examen quinquennal, qui ne commande pas une révision systématique, est distingué de l'analyse des critères. La répétition de la désignation des organisations est retirée sans modifier leur obligation. Le contrôle des critères potentiellement discriminatoires et de la prise en compte de toutes les compétences est maintenu pour sa fonction essentielle.",
    "Cinq ans demeure la périodicité légale maximale, conforme au 6° de L2241-1 et au b) de L2241-5. Il ne s'agit ni d'une obligation de reclasser tous les postes ni d'un délai pour demander réparation d'une discrimination. Les quatre alinéas et la priorité de réduction de l'écart moyen sont conservés. Aucun classement favorable, salaire acquis ou recours n'est supprimé."
)

add('L2241-16', [
    "En l'absence d'accord conclu en la matière au niveau de négociation concerné, les organisations liées par une convention de branche ou, à défaut, par des accords professionnels se réunissent une fois tous les cinq ans pour engager une négociation sur l'institution d'un ou plusieurs plans d'épargne interentreprises ou plans d'épargne pour la retraite d'entreprise collectifs interentreprises.",
],
    "Réécriture à droit constant : la condition d'absence d'accord est placée en tête afin de rendre immédiatement visible la dispense de négociation lorsqu'un accord existe déjà. La négociation sur les plans reste obligatoire dans les autres cas, sans devenir une obligation de créer un plan ou de souscrire. Cette faculté d'accès à l'épargne collective et sa dispense sont conservées.",
    "Cinq ans, les deux catégories exactes de plans et la condition d'absence d'accord au niveau concerné sont maintenus ; aucun seuil nouveau n'est ajouté. Les deux notes sources ont été lues : ordonnance 2019-766, article 9 I, échéance au plus tard le 1er janvier 2020, et décret 2019-807, article 9 II, fixant l'entrée en vigueur au 1er octobre 2019. Elles décrivent l'entrée en vigueur historique, pas celle de la réforme proposée. Les anciens plans et les avantages des futurs plans éligibles demeurent régis par leurs dispositions propres ; la réforme de retraite ne les absorbe pas implicitement."
)

add('L2241-17', [
    "Les négociations sur les salaires et sur les classifications prévues respectivement aux articles L. 2241-8 et L. 2241-15 visent aussi à définir et à programmer les mesures permettant de supprimer les écarts de rémunération entre les femmes et les hommes. Elles suivent les périodicités applicables à chacun de ces articles, sans annualité supplémentaire sur le fondement du présent article.",
],
    "Réforme de coordination : retrait de la qualification annuelle de la négociation salariale pour rendre effectif l'allègement de L2241-8. À droit constant, la définition et la programmation des mesures de suppression des écarts restent intégrées aux négociations salariales et de classifications ; elles ne déclenchent pas une procédure autonome.",
    "Les renvois à L2241-8 et L2241-15 sont conservés. Le premier prévoit désormais quatre ans en supplétif avec réserves conventionnelles et déclenchement L2241-10 ; le second conserve cinq ans. R2271-1, repéré dans le corpus, vise le présent article pour le suivi de l'égalité : ce rattachement reste opérant, sans rétablir un rapport annuel CPPNI supprimé dans L2232. Aucun droit à un salaire égal ni aucune mesure déjà programmée ne doit attendre l'échéance d'une négociation pour s'appliquer.",
    ["Le renvoi imposant une négociation salariale nécessairement annuelle est supprimé ; les mesures d'égalité sont définies et programmées aux périodicités propres à L2241-8 et L2241-15."]
)

add('L2241-18', [
    "L'accord visant à supprimer les écarts de rémunération, conclu à l'issue des négociations prévues aux articles L. 2241-8 et L. 2241-15, est déposé auprès de l'autorité administrative dans les conditions prévues à l'article L. 2231-6. Le dépôt effectué au titre de cet article satisfait à la présente obligation ; aucun second dépôt du même accord n'est exigé.",
    "L'absence de dépôt d'un accord ne rend pas obligatoire la transmission d'un procès-verbal de désaccord sur le fondement du présent article. Ni cette absence de dépôt ni l'absence d'une telle transmission ne déclenche, à elle seule, la réunion d'une commission mixte. Les articles L. 2241-3 et L. 2261-20 demeurent applicables aux négociations prévues à l'article L. 2241-17, notamment lorsqu'elles n'ont pas été engagées sérieusement et loyalement.",
    "Ces dispositions s'appliquent dès l'entrée en vigueur de la loi, y compris aux négociations en cours et aux procès-verbaux qui n'ont pas encore été transmis. Aucune transmission tardive de ces procès-verbaux n'est exigée après cette date sur le seul fondement du présent article. Les dépôts d'accords déjà effectués restent valables et ne sont pas renouvelés. Les réunions régulièrement convoquées peuvent se poursuivre et les recours fondés sur un manquement à une obligation maintenue sont conservés.",
],
    "Réforme de fond partielle : suppression de la transmission du procès-verbal comme alternative imposée au dépôt d'un accord et suppression du déclenchement automatique d'une commission pour la seule absence de dépôt ou transmission. Le dépôt légal de l'accord reste unique et la commission peut toujours intervenir selon les garanties de loyauté et le droit commun. La référence à l'annualité est coordonnée avec L2241-8.",
    "Une abrogation intégrale serait inexacte : le dépôt de l'accord demeure et relève aussi du fondement autonome L2231-6, lu. L2261-20 et L2241-3 conservent les voies de convocation, notamment la demande de deux organisations représentatives et le défaut de négociation sérieuse. La dispense concerne seulement le procès-verbal de branche visé ici ; elle ne supprime pas le procès-verbal d'entreprise de L2242-5 ni ses utilisations distinctes dans L2242-8. Les données nécessaires à la négociation restent accessibles et les mesures de suppression des écarts demeurent exigibles. Coordonner les éventuels circuits administratifs propres à ce procès-verbal sans nouvelle déclaration de remplacement.",
    [
        "La transmission à l'administration d'un procès-verbal de désaccord contenant les dernières propositions, imposée comme alternative à l'absence de dépôt d'accord, est supprimée sur ce fondement.",
        "La réunion automatique d'une commission mixte sur le seul constat d'absence de dépôt ou de transmission est supprimée, sans retirer les voies de convocation pour défaut de négociation loyale ou à la demande des organisations.",
    ]
)

add('L2242-1', [
    "Dans les entreprises où une ou plusieurs sections syndicales d'organisations représentatives sont constituées, l'employeur engage au moins une fois tous les quatre ans les négociations suivantes :",
    "1° Une négociation sur la rémunération, notamment les salaires effectifs, sur le temps de travail et sur le partage de la valeur ajoutée dans l'entreprise ;",
    "2° Une négociation sur l'égalité professionnelle entre les femmes et les hommes, notamment sur les mesures permettant de supprimer les écarts de rémunération, ainsi que sur la qualité de vie et des conditions de travail.",
],
    "Réécriture à droit constant : les objets de la négociation et leur rattachement aux deux subdivisions sont clarifiés. L'obligation demeure limitée aux entreprises dotées de sections syndicales représentatives. La négociation sur les salaires et l'égalité remplit une fonction essentielle ; aucune procédure ou transmission supplémentaire n'est ajoutée.",
    "Le plafond d'ordre public de quatre ans et les deux subdivisions sont maintenus ; le présent article n'efface pas l'annualité supplétive d'entreprise de L2242-13, contrairement à la réforme propre à la branche. La note source de la loi 2021-1018, article 40 I et II, a été lue : entrée en vigueur historique le 31 mars 2022 et conditions d'application à conserver ; aucune date future n'en est tirée. Les articles d'entreprise L2242-4 et L2242-5, lus, conservent le régime des décisions unilatérales et du procès-verbal de désaccord. Les seuils de durée du travail, les contrats uniques et le préavis de rupture ne sont pas fixés par le présent article."
)

add('L2242-2', [
    "Dans les entreprises et les groupes d'entreprises au sens de l'article L. 2331-1 qui comptent au moins trois cents salariés, l'employeur engage au moins une fois tous les quatre ans, en plus des négociations prévues à l'article L. 2242-1, une négociation sur la gestion des emplois et des parcours professionnels. Cette obligation s'applique aussi aux entreprises et aux groupes d'entreprises de dimension communautaire au sens des articles L. 2341-1 et L. 2341-2 qui comportent en France au moins un établissement ou une entreprise d'au moins cent cinquante salariés.",
    "Lorsque cette négociation et celle prévue à l'article L. 2242-2-1 sont dues au même niveau et pour la même échéance, les parties peuvent convenir d'une négociation commune. Celle-ci satisfait aux deux obligations si tous les thèmes requis pour chacune sont traités avec les interlocuteurs habilités, selon les règles de validité et les délais applicables à chacune. Les matières communes effectivement négociées ne donnent alors pas lieu à une seconde ouverture ou à une seconde discussion obligatoire. Les informations nécessaires à chaque thème et les garanties de participation demeurent exigées.",
    "Cette dispense de double négociation s'applique dès l'entrée en vigueur de la loi, y compris aux négociations en cours, sans recommencer une procédure déjà engagée. Elle ne modifie ni les périodicités supplétives propres à l'entreprise ni les engagements conventionnels plus fréquents, ni les droits et recours relatifs aux périodes antérieures.",
],
    "Réforme de fond ciblée sur les doublons : une négociation commune peut satisfaire à la gestion des emplois et à l'emploi des salariés expérimentés sans seconde ouverture ni nouvelle discussion des mêmes matières. Les conditions empêchent de compter une négociation qui n'aurait pas traité tous les sujets. Les quatre ans d'ordre public et les champs exacts, dont les entreprises communautaires avec cent cinquante salariés en France, sont maintenus.",
    "Les références L2331-1, L2341-1 et L2341-2 ont été lues. Trois cents salariés concernent le premier champ ; cent cinquante salariés dans au moins un établissement ou une entreprise en France concernent le second, sans soumettre celui-ci au seuil de trois cents salariés ni à une condition nouvelle de section syndicale. Les deux champs demeurent réunis dans le premier alinéa, sans subdivisions nouvelles. Le regroupement suppose l'accord des parties, sans consentement déduit de leur silence. L2242-13 et L2242-20, lus, conservent leurs périodicités supplétives de trois ans ; la fusion ne les porte pas à quatre ans. L2242-20 conserve en source un renvoi ancien à L2323-10 : incohérence préexistante à coordonner dans cet autre article, non corrigée implicitement. Aucune autorisation de licenciement, procédure collective ou aide éligible n'est supprimée par ce regroupement.",
    ["La seconde ouverture et la répétition obligatoire des matières communes aux négociations de gestion des emplois et d'emploi des salariés expérimentés sont supprimées quand une négociation commune satisfait intégralement aux deux régimes."]
)

add('L2242-2-1', [
    "Dans les entreprises et les groupes d'entreprises au sens de l'article L. 2331-1 qui comptent au moins trois cents salariés et où une ou plusieurs sections syndicales d'organisations représentatives sont constituées, l'employeur engage au moins une fois tous les quatre ans, en plus des négociations prévues à l'article L. 2242-1, une négociation sur l'emploi, le travail et l'amélioration des conditions de travail des salariés expérimentés, en considération de leur âge.",
    "Cette obligation peut être satisfaite par la négociation commune prévue à l'article L. 2242-2, dans les conditions fixées par cet article. Les matières communes effectivement traitées n'imposent pas une seconde ouverture ou une seconde discussion pour satisfaire au présent article. Les thèmes spécifiques aux salariés expérimentés, les informations nécessaires et les garanties de participation demeurent exigés.",
    "La dispense de double négociation s'applique dès l'entrée en vigueur de la loi, y compris aux négociations en cours. Elle ne modifie ni les périodicités supplétives propres à l'entreprise ni les engagements conventionnels plus fréquents, ni les droits et recours relatifs aux périodes antérieures.",
],
    "Réforme de coordination : la négociation concernant les salariés expérimentés peut être intégrée à celle sur les emplois et parcours professionnels sans procédure répétée pour les matières communes. Le seuil de trois cents salariés, la présence de sections syndicales représentatives, la périodicité maximale de quatre ans et les trois objets de négociation sont conservés.",
    "Ne pas importer le champ communautaire de cent cinquante salariés de L2242-2 dans le présent article : la source exige ici trois cents salariés et des sections syndicales représentatives. L2242-22 et D2242-17 ont été lus : la périodicité supplétive de trois ans, le diagnostic d'entreprise, les sujets obligatoires et facultatifs ainsi que l'examen du fonds de prévention de l'usure professionnelle demeurent. La dispense de diagnostic séparé décidée pour la branche à L2241-14-1 ne les abroge pas. L2242-4 continue de viser le présent article pour les décisions unilatérales pendant la négociation. Aucun calendrier d'aide ou de formation n'est converti en terme de l'emploi.",
    ["L'ouverture d'une seconde négociation et la répétition des mêmes discussions sur les salariés expérimentés ne sont plus exigées lorsque la négociation commune satisfait à tous les thèmes, délais et garanties applicables."]
)

add('L2242-3', [
    "Si la négociation prévue au 2° de l'article L. 2242-1 n'aboutit pas à un accord sur l'égalité professionnelle entre les femmes et les hommes, l'employeur établit un plan d'action annuel pour assurer cette égalité. Après évaluation des objectifs et des mesures de l'année écoulée, le plan, fondé sur des critères clairs, précis et opérationnels, fixe les objectifs de progression de l'année à venir, définit les actions qualitatives et quantitatives permettant de les atteindre et en évalue le coût. Le plan peut être actualisé dans le document existant : aucun nouveau document complet n'est exigé si ce document contient l'évaluation et tous les éléments requis pour l'année à venir. Le plan et ses mises à jour ne sont pas soumis à un dépôt obligatoire auprès de l'autorité administrative.",
    "En l'absence d'accord prévoyant les mesures de suppression des écarts de rémunération entre les femmes et les hommes, la négociation sur les salaires effectifs prévue au 1° de l'article L. 2242-1 porte aussi sur la programmation des mesures permettant de supprimer ces écarts et les différences de déroulement de carrière entre les femmes et les hommes.",
    "La dispense de dépôt ne dispense ni d'établir et de mettre en œuvre le plan annuel, ni de le mettre à la disposition du comité social et économique dans les conditions de l'article L. 2312-26, ni de satisfaire aux obligations de publication et de correction prévues par les articles L. 1142-8, L. 1142-9, L. 1142-9-1 et L. 1142-13 dans leur champ propre. Les décisions correctrices dont les articles L. 1142-9 et L. 1142-13 imposent le dépôt restent déposées selon les modalités réglementaires du dépôt des plans ; ce dépôt ne rend pas obligatoire celui du plan ou de ses autres mises à jour. Le plan est tenu à la disposition des agents de contrôle ; l'absence de dépôt du seul plan ne constitue pas un manquement au sens de l'article L. 2242-8.",
    "L'employeur peut déposer volontairement le plan dans les conditions réglementaires applicables à ce dépôt pour bénéficier de l'appréciation prévue à l'article L. 2242-9. Ce dépôt conserve les effets que cet article lui attache, notamment pour le calcul de la période pendant laquelle la réponse de conformité lie l'autorité administrative. Les droits attachés aux dépôts et aux réponses de conformité antérieurs demeurent.",
    "La dispense de nouveau document complet et la suppression du dépôt obligatoire s'appliquent dès l'entrée en vigueur de la loi, y compris aux plans déjà établis et aux mises à jour en cours. Aucun dépôt tardif ni nouveau dépôt d'un plan déjà transmis n'est exigé sur ce seul fondement après cette date. Les obligations annuelles de fond, les créances, les droits des salariés et les recours demeurent ; la règle répressive plus douce s'applique aux sanctions non définitives dans son champ propre.",
],
    "Réforme de fond : suppression du dépôt administratif obligatoire du plan annuel d'égalité et du besoin de produire chaque année un nouveau document complet lorsque l'actualisation du document existant suffit. L'évaluation annuelle, les objectifs de progression, les actions, leur coût et les mesures salariales demeurent. Le dépôt reste libre pour préserver le rescrit favorable et son effet de sécurité juridique. Les décisions correctrices légalement distinctes, les publications, le CSE et le contrôle ne sont pas fermés.",
    "Les deux premiers alinéas gardent leurs objets et leur place, notamment pour le renvoi de L1142-13 au premier alinéa. R2242-2 a été lu : au moins trois domaines pour moins de 300 salariés, quatre pour 300 et plus, indicateurs chiffrés et rémunération effective obligatoire sont inchangés. Coordonner R2242-2-1, lu, pour rendre le seul dépôt du plan facultatif ; ses modalités restent utilisables pour le dépôt volontaire et pour les décisions correctrices dont L1142-9 et L1142-13 imposent expressément le dépôt. L2242-9, lu intégralement, conserve la demande d'appréciation, son régime, le rejet implicite, l'irrecevabilité après contrôle engagé et l'effet favorable jusqu'au terme de la première année suivant le dépôt du plan : aucun avantage n'est fermé aux futurs employeurs éligibles. L2242-8 et R2242-3 à R2242-6, lus, conservent les obligations de fond, la mise en demeure et les garanties de contrôle ; l'absence du dépôt désormais facultatif ne peut les rétablir indirectement. L2312-26 conserve l'accès du CSE ; L1142-9-1 conserve les objectifs publiés. L1142-13 et sa date historique d'application restent à leur champ distinct. Les protections d'égalité et les exigences supérieures de transparence et de non-discrimination ne sont pas abrogées ni réputées vérifiées par le seul présent travail. Aucun crédit, aide, dispense ou réduction de cotisation n'est retiré.",
    [
        "Le dépôt administratif obligatoire du plan annuel d'égalité professionnelle et de ses mises à jour est supprimé, sans attestation ni déclaration de remplacement et sans supprimer le dépôt volontaire ouvrant le rescrit.",
        "La production d'un nouveau document complet chaque année n'est pas exigée lorsque l'actualisation du document existant contient déjà l'évaluation, les objectifs, les actions et leurs coûts pour l'année suivante.",
    ]
)


answer = []
assert len(sources) == 24
assert set(drafts) == {s['number'] for s in sources}
for source in sources:
    obj = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    obj.update(drafts[source['number']])
    obj['status'] = 'rewrite_draft'
    answer.append(obj)

Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
