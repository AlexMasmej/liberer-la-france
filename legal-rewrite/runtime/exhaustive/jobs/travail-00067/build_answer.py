import json
import re
import html
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
references = json.loads(Path('reference-targets.json').read_text())
answers = []


def plain(xml):
    return html.unescape(re.sub(r'<[^>]+>', '', xml or ''))


def keep(number, reason, notes, assessment, limits, burden, benefit=None):
    source = next(a for a in sources if a['number'] == number)
    answer = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    answer.update(
        proposed_xml=None,
        reason=reason,
        review_notes=notes,
        status='retained_unchanged',
        classification='retained_necessary',
        substantive_impact={
            'version': 1,
            'classification': 'retained_necessary',
            'assessment': assessment,
            'scope_limitations': limits,
            'new_burdens_review': burden,
            'effects': [],
        },
    )
    if benefit:
        answer['benefit_review'] = benefit
    answers.append(answer)
    return answer


def draft(number, xml, reason, notes, assessment, limits, burden, effects,
          removed=None):
    source = next(a for a in sources if a['number'] == number)
    answer = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    answer.update(
        proposed_xml=xml,
        reason=reason,
        review_notes=notes,
        status='rewrite_draft',
        substantive_impact={
            'version': 1,
            'classification': 'material_reduction' if removed else 'coordination_only',
            'assessment': assessment,
            'scope_limitations': limits,
            'new_burdens_review': burden,
            'effects': effects,
        },
    )
    if removed:
        answer.update(change_type='normative_reduction',
                      reform_policy_id='editorial_direction_2026_10_19',
                      removed_provisions=removed)
    answers.append(answer)
    return answer


keep(
    'L2354-2',
    "Maintien intégral après examen du rendez-vous de quatre ans, de la convocation dans les six mois et du maintien en fonction du comité. L'examen ne contraint pas à conclure un accord ni même à ouvrir une négociation. Le comité tient lui-même lieu de groupe spécial de négociation : la source évite déjà la constitution d'un second organe. La convocation rend effectif le droit de réexamen et la continuité du comité empêche un vide de représentation. Aucune taxe, déclaration périodique supplémentaire ou autorisation indépendante à supprimer n'est identifiée.",
    "Le chapitre II fixe la procédure de négociation ; il n'est pas une procédure de rupture des contrats de travail. L2353-4, lu dans le corpus, impose déjà une réunion annuelle : L2354-2 n'exige pas expressément une réunion matériellement distincte, et une prétendue fusion des réunions ne serait donc pas un gain démontré. Le réexamen quadriennal s'inscrit dans les dispositions de référence de la directive 2001/86/CE ; le texte européen intégral n'est pas joint au lot, sa confrontation primaire reste à effectuer avant adoption, sans présumer sa suppression nationale possible. Les quatre ans et les six mois ne sont ni un préavis individuel ni une ancienneté ouvrant une indemnité.",
    "La source entière demeure applicable : examen quadriennal, délai maximal de convocation, comité négociateur et continuité des mandats. Aucune réduction de charge n'est revendiquée.",
    "Sociétés européennes et comité déjà institué seulement ; aucune réforme du CSE national, des contrats individuels ou du cadre européen n'est opérée.",
    "Aucune charge nouvelle n'est identifiée : le texte source est maintenu sans rapport, justificatif, organe ni rendez-vous supplémentaire.",
)

keep(
    'L2354-3',
    "Maintien intégral du droit de réouverture à la demande écrite d'au moins 10 % des salariés ou de leurs représentants. Le seuil, les deux ans et la possibilité d'un accord de réouverture plus rapide organisent la remise en cause d'une décision collective de ne pas négocier, sans rendre cette décision irrévocable. L'écrit prouve la demande et son soutien ; ce n'est pas un agrément administratif. Le non-déclenchement du chapitre III après échec protège le choix initial. Supprimer cette dernière réserve imposerait un régime plus contraignant.",
    "L2352-13 a été lu en entier : la décision initiale relève de son deuxième alinéa, avec deux tiers des membres, au moins deux Etats et deux tiers des salariés, et exception de transformation avec participation existante. L2364-3, lu dans le corpus, rend L2354-3 applicable aux coopératives européennes. Le délai de deux ans et la réouverture anticipée conventionnelle relèvent du cadre de la directive 2001/86/CE, avec cadre analogue pour les coopératives ; les textes européens intégraux ne sont pas joints et leur modification n'est pas réputée acquise. Le délai ne concerne pas la notification ou le préavis d'une rupture individuelle.",
    "Aucun délai n'est raccourci artificiellement : la réouverture anticipée par accord est déjà permise dans la source. Le droit de demande et l'absence de régime subsidiaire imposé après échec sont préservés.",
    "Seule la réouverture après la décision de L2352-13 est concernée ; ni les négociations initiales ni les procédures de licenciement ne sont modifiées.",
    "Aucune charge nouvelle n'est identifiée : maintien du seul écrit existant, sans nouvelle collecte de signatures, autorisation ou déclaration de remplacement.",
)

keep(
    'L2354-4',
    "Maintien intégral de la négociation déclenchée par un changement susceptible d'affecter substantiellement la représentation ou les modalités d'implication. La source ne vise pas toute variation d'effectif ni tout déplacement : le critère d'atteinte substantielle limite déjà l'obligation. La négociation et son régime de repli évitent qu'une restructuration vide de leur portée les droits collectifs acquis. Une simple suppression du groupe ou du repli laisserait les salariés des nouvelles composantes sans garantie équivalente démontrée.",
    "L2352-3 à L2352-8, L2353-2 et L2353-28 à L2353-30 ont été lus : répartition transnationale, adaptation des sièges et maintien du niveau de participation expliquent les renvois au chapitre II et à L2353-28 et suivants. Le renvoi final à L2353-2 et suivants désigne le régime de référence après échec ; il ne recrée pas un CDD. R2354-1 et R2364-1, lus, donnent au juge le pouvoir d'ordonner la constitution du groupe ; L2364-3 étend la règle aux coopératives. Le cadre européen anti-contournement doit être confronté aux textes intégraux non joints avant tout allègement de ces garanties.",
    "Le déclencheur substantiel et la protection de la représentation demeurent entiers. Aucun nouveau motif de négociation ni aucune baisse de coût ne sont annoncés.",
    "La seule réorganisation de l'implication collective après immatriculation est traitée ; les effets économiques, le coût d'une négociation et les contraintes européennes ne sont pas chiffrés.",
    "Aucune charge nouvelle n'est identifiée : la négociation reste conditionnée au même risque d'atteinte substantielle, sans rapport ni autorisation additionnels.",
)

keep(
    'L2355-1',
    "Maintien intégral des deux incriminations d'entrave. La constitution du groupe ou du comité et la libre désignation de leurs membres protègent l'exercice effectif de la représentation ; leur fonctionnement régulier fait l'objet d'une peine distincte, sans emprisonnement dans le second alinéa. Les supprimer priverait les droits collectifs de leur garantie pénale sans mécanisme équivalent démontré. L'amende réprime une infraction : elle n'est ni un prélèvement sur l'emploi ni une cotisation accessoire.",
    "Contrôle des montants et peines : un an d'emprisonnement et 7 500 € pour les entraves du premier alinéa ; 7 500 € seuls pour le fonctionnement au second. Aucune extension aux procédures ou délais individuels du contrat unique. Le cadre européen exige l'effectivité de la protection, mais cette exigence n'est pas présentée comme imposant précisément ces peines nationales ; aucun texte européen intégral n'est joint. Les garanties pénales générales et les règles d'application dans le temps ne sont pas modifiées.",
    "Les deux infractions et leur différenciation restent inchangées. Aucune suppression de taxe ni économie sur les sanctions n'est comptée.",
    "Le présent maintien n'évalue ni la politique pénale générale ni les sanctions d'autres institutions représentatives ou d'autres Etats.",
    "Aucune charge nouvelle n'est identifiée : aucun fait incriminé, peine, obligation documentaire ou pouvoir de contrôle n'est ajouté.",
)

keep(
    'L2361-1',
    "Maintien intégral des trois catégories du champ d'application. Le siège et l'administration centrale en France, les participants personnes morales ou physiques établis ou résidant en France et les filiales ou établissements français de coopératives d'un autre Etat constituent les rattachements qui évitent une application indifférenciée du titre. La référence au règlement définit la forme sociale ; ce n'est pas un agrément national supplémentaire. Aucun dépôt autonome ni taxe n'est créé par cet article de champ.",
    "Les 1°, 2° et 3° restent dans leur ordre, avec le règlement (CE) n° 1435/2003 du 22 juillet 2003 et la distinction Communauté européenne/Espace économique européen de la source. Ne pas attribuer le statut de coopérative européenne à un contrat de travail privé, ni modifier ici celui d'un agent public. Le règlement et la directive 2003/72/CE constituent le cadre supérieur à coordonner ; leurs textes intégraux ne sont pas joints et aucune conformité globale n'est attestée.",
    "Le périmètre territorial et personnel entier est conservé ; supprimer les distinctions pourrait élargir les obligations au lieu de les réduire.",
    "Aucun changement de droit des sociétés, d'immatriculation ou de statut des agents publics n'est démontré par le maintien de cette définition de champ.",
    "Aucune charge nouvelle n'est identifiée : aucun rattachement, seuil, dossier ou condition de création n'est ajouté aux trois cas existants.",
)

keep(
    'L2361-2',
    "Maintien intégral du non-cumul entre le régime propre à la coopérative européenne et le titre IV sur le comité d'entreprise européen ou la procédure transnationale d'information-consultation. Il évite déjà deux dispositifs concurrents pour la coopérative et ses filiales. La réapplication du titre IV après décision du groupe de ne pas négocier ou de clore les négociations préserve une voie de représentation. Supprimer l'exclusion générale augmenterait les contraintes ; supprimer l'exception laisserait un défaut de protection.",
    "L2341-1 et L2341-2 ont été lus intégralement dans le corpus : le premier définit l'entreprise de dimension communautaire (mille salariés et établissements de cent cinquante dans au moins deux Etats), le second le groupe avec ses rattachements à L2331-1 et L2341-1. Dans L2361-2, le renvoi à L2341-2 vise la définition du groupe ; il ne remplace pas celle de l'entreprise. L2362-7, deuxième alinéa, fixe la décision qualifiée de retrait de la négociation. L'exclusion ne concerne pas les institutions nationales autonomes et ne dépend pas de l'ancienneté d'un contrat individuel.",
    "L'allègement de non-cumul est déjà dans la source et reste ouvert aux futures coopératives éligibles ; aucune seconde obligation supprimée n'est revendiquée.",
    "La dispense vise seulement le titre IV et ses destinataires définis. Elle ne supprime ni le titre VI ni les garanties nationales indépendantes de représentation.",
    "Aucune charge nouvelle n'est identifiée : les conditions de non-cumul et le retour au titre IV restent exactement ceux de la source, sans nouvelle attestation.",
    "L'avantage possible est la dispense d'appliquer le titre IV à la coopérative européenne et à ses filiales, évitant le cumul de deux dispositifs transnationaux. Il est maintenu intégralement pour les structures futures qui satisfont au champ, sans être limité aux structures déjà constituées. Le second alinéa conserve la voie protectrice du titre IV lorsque le groupe décide de ne pas engager ou de clore la négociation ; cette exception n'est ni une taxe ni une suppression de la dispense en dehors de son cas légal.",
)

keep(
    'L2361-3',
    "Maintien intégral des trois formes d'implication, de la priorité à l'accord et du régime subsidiaire du chapitre III. La participation n'est imposée que le cas échéant, et la source laisse les modalités à la négociation. Il ne s'agit ni d'une autorisation de l'emploi ni d'un rapport à produire. La suppression du repli ferait disparaître l'information et la consultation faute d'accord ; celle de la voie négociée imposerait au contraire un régime unique plus rigide.",
    "L2362-2 et L2362-10 précisent l'accord écrit et son contenu ; L2363-1 fixe l'entrée dans le régime subsidiaire, sous réserve de la décision qualifiée de L2362-7. La nouvelle rédaction de L2363-2 retire seulement l'engagement distinct d'application de ce régime, non son contenu. Les modalités d'implication ne constituent ni une durée d'emploi ni une condition de rupture individuelle. Cadre de la directive 2003/72/CE à confronter à son texte intégral non joint avant une réforme des droits de participation.",
    "Les droits d'information, consultation et participation éventuelle restent entiers ; la source contient déjà la possibilité de les organiser par accord.",
    "Aucun régime de participation supplémentaire n'est créé et aucun chiffrage des coûts des instances nationales ou transnationales n'est effectué.",
    "Aucune charge nouvelle n'est identifiée : l'accord et le régime de repli restent ceux de la source, sans dépôt, registre ou réunion additionnels.",
)

keep(
    'L2361-4',
    "Maintien intégral du renvoi commun aux définitions de l'information, de la consultation et de la participation. Une définition commune évite trois corps de règles parallèles ; elle n'oblige à aucune déclaration autonome. La supprimer rendrait indéterminés les droits négociés et le régime de repli. Aucun agrément, justificatif redondant ou prélèvement ne figure dans la source à retirer.",
    "L2351-4, L2351-5 et L2351-6 ont été lus en entier : information transnationale permettant d'apprécier les incidences, dialogue et avis susceptible d'être pris en compte, puis élection/désignation ou recommandation/opposition pour les organes sociaux. L2361-4 en étend les définitions aux coopératives et aux participants personnes physiques comme morales, filiales et établissements du titre. Cette adaptation de champ n'étend pas un préavis de rupture ou une autorisation de licenciement.",
    "Les trois définitions communes et leur champ d'application sont conservés, sans prétendre que le renvoi existant constitue une nouvelle fusion de régimes.",
    "Le contenu des accords particuliers et l'appréciation d'une information ou d'une consultation effective ne sont pas validés par ce maintien.",
    "Aucune charge nouvelle n'est identifiée : maintien du renvoi existant, sans ajouter de données, de consultation ni de condition de participation.",
)

effectif = keep(
    'L2361-5',
    "Maintien intégral du décompte par L1111-2. Le renvoi donne une règle commune aux seuls participants, filiales et établissements situés en France et évite un second calcul spécialement créé pour les coopératives européennes. La proposition cible de L1111-2 prévoit déjà les nouveaux contrats uniques, la proratisation des affectations temporaires et l'exclusion pendant un remplacement réel ; elle ne rend pas ce renvoi incohérent. Ajouter un nouveau texte stylistique ne démontrerait aucune simplification.",
    "Lecture entière des quatre cibles requises dans reference-targets.json, sources, notes et propositions distinguées. Seul L1111-2 est directement visé : son décompte n'est pas une condition d'ancienneté de rupture. Les trois autres cibles fournissent le contexte du contrat unique et de ses effets, sans être introduites dans le présent article. Les exclusions et proratisations favorables de la proposition cible doivent rester ouvertes aux futures affectations éligibles et aux anciens contrats dans leur champ. Aucun nouveau renvoi n'est ajouté. La validité européenne du calcul national pour la représentation transnationale n'est pas attestée par ces contrôles.",
    "Le renvoi source à la règle commune de décompte est conservé. Les modifications de L1111-2 appartiennent à la mesure du contrat unique et ne sont pas une nouvelle réduction produite par L2361-5.",
    "France seulement pour ce calcul ; les règles des autres Etats et le coût global des seuils sociaux ne sont pas modifiés ni chiffrés dans ce lot.",
    "Aucune charge nouvelle n'est identifiée dans cet article : aucun relevé distinct, preuve de notification ou fichier spécial d'effectifs n'est ajouté au renvoi existant.",
)

checks = {
    'L1234-1': "L2361-5 ne renvoie pas au préavis : cette cible n'est qu'un contexte associé au décompte de L1111-2. La source prévoit notamment un ou deux mois selon l'ancienneté ; la proposition distingue les nouveaux contrats, avec quinze jours calendaires indépendamment de l'ancienneté, des anciens contrats conservant leurs règles. Le décompte des effectifs ne modifie ni la notification déclenchant ce préavis ni les autorisations ou procédures collectives distinctes.",
    'L1221-2': "La source admet un terme par renvoi au titre IV ; la proposition impose le contrat unique indéterminé pour les contrats nouveaux et empêche sa fin automatique avec une mission, une formation ou un remplacement. L2361-5 conserve un renvoi de calcul, pas une faculté de nouveau CDD. Les anciens contrats et les droits futurs liés à une affectation temporaire restent distingués par la proposition de L1111-2 ; leur prise en compte n'implique aucune rupture automatique ni notification de fin de mission valant fin d'emploi.",
    'L1111-2': "Cible directe : la source distingue prise en compte intégrale au 1°, proratisation sur douze mois et exclusion des remplaçants au 2°, puis prorata des horaires au 3°. La proposition conserve ces règles et précise leur application au contrat unique : prorata pendant une affectation réellement temporaire, exclusion pendant le seul remplacement, puis retour à la règle de l'emploi permanent ; l'intérim n'est pas compté deux fois chez l'utilisateur. Le renvoi reste opérant et n'instaure aucune ancienneté individuelle d'indemnisation ni notification supplémentaire.",
    'L1234-9': "Aucun renvoi direct de L2361-5 à cette indemnité : la cible ne détermine pas l'effectif. La source ouvre le droit à huit mois sous réserve de faute grave ; la proposition ouvre l'indemnité ordinaire des nouveaux contrats à un an atteint à la fin effective, préavis inclus, puis 0,20 mois sur toute l'ancienneté, mois complets au prorata et plafond de six mois, employeur seul, avec exception de faute grave. Elle conserve une transition des anciens contrats et les droits spéciaux. Le nombre de salariés n'altère ni ce seuil ni la date de notification du préavis et ne supprime aucune protection collective.",
}
effectif['reference_checks'] = [
    {'target_key': key, 'view_sha256': references['targets'][key]['view_sha256'],
     'assessment': checks[references['targets'][key]['number']]}
    for key in references['requirements'][effectif['code_id'] + '|' + effectif['source_id']]
]

fusion_xml = (
    "<p>Les dispositions d'application du présent titre relatives à la procédure applicable aux litiges sont déterminées par décret en Conseil d'Etat.</p>"
    "<p>La constitution d'une société coopérative européenne par fusion ne donne lieu à aucune transmission systématique à l'inspection du travail des éléments établis pour attester la conformité des modalités d'implication des salariés aux dispositions du présent titre. Aucune déclaration ni aucun dépôt de substitution ne peut être exigé sur ce fondement.</p>"
    "<p>Cette dispense ne supprime ni les informations dues aux salariés et à leurs représentants, ni la vérification du respect de leurs droits dans les procédures de constitution et d'immatriculation de la société. Les pouvoirs de contrôle et de demande de communication de l'inspection du travail résultant des autres dispositions légales demeurent applicables dans leurs conditions propres.</p>"
    "<p>La dispense s'applique à compter de l'entrée en vigueur de la loi portant cette suppression, y compris aux transmissions qui n'ont pas encore été effectuées pour une fusion antérieure. Les documents déjà régulièrement transmis demeurent soumis aux règles de conservation, d'utilisation et de protection des données qui leur sont applicables. La suppression de la transmission systématique ne remet pas en cause les droits et recours nés antérieurement.</p>"
)
draft(
    'L2361-6', fusion_xml,
    "Réforme de fond : suppression de la transmission systématique à l'inspection du travail des éléments attestant l'implication des salariés lors d'une constitution par fusion. L'habilitation réglementaire relative aux litiges est maintenue. R2362-17 et R2363-5, lus intégralement, prescrivent l'envoi des éléments déjà fournis pour le contrôle de la fusion : la copie automatique ne constitue pas le contrôle lui-même. Les informations des salariés, le contrôle de constitution et d'immatriculation, les pouvoirs légaux autonomes de l'inspection et les recours demeurent. Aucun envoi, déclaration ou agrément ne remplace la formalité retirée.",
    "Coordonner R2362-17 et R2363-5 : retirer pour les transmissions non effectuées leurs envois systématiques, qui reprennent les mêmes éléments ; une seule mesure est comptée, non deux dépôts supposés pour chaque fusion. Ces règlements ne sont pas modifiés dans ce dossier de travail. Ils citent le quatrième alinéa de L229-3 du code de commerce : ce texte extérieur n'est pas fourni et son rattachement exact à la fusion de coopératives doit être confronté avant adaptation, sans le corriger silencieusement ni supprimer le contrôle de légalité. Le règlement 1435/2003 et la directive 2003/72/CE ne sont pas joints en entier ; la dispense ne vise aucun contrôle ou information qu'ils imposent. Aucun accès nouveau aux données n'est autorisé. Les litiges et informations aux représentants restent à leur régime propre.",
    "Par rapport à l'article source entier, l'envoi systématique de pièces de fusion à l'inspection, dont l'exécution figure dans les deux règlements lus, est effectivement retiré. Seule la procédure de litige reste habilitée. Le contrôle de fond ne disparaît pas ; aucun gain fiscal n'est revendiqué.",
    "La réduction porte sur cet envoi spécifique, y compris restant à effectuer, non sur les pièces nécessaires au registre, les communications aux salariés ou les demandes légales de contrôle. Le coût administratif et le solde public net ne sont pas chiffrés.",
    "Aucune charge nouvelle n'est identifiée : pas de déclaration de remplacement, de registre, de consentement supplémentaire ou de nouvel accès aux données. Les demandes de contrôle restent exclusivement celles permises par les autres lois ; le coût net de leur éventuelle mobilisation reste inconnu.",
    [{
        'kind': 'obligation_removed',
        'measure_id': 'sce-fusion-fin-transmission-systematique-inspection',
        'description': "Retrait de l'envoi systématique à l'inspection des éléments attestant l'implication des salariés lors d'une fusion ; une seule formalité dédupliquée avec ses deux textes d'exécution.",
        'before': "Les sociétés, filiales ou établissements concernés par une fusion transmettent à l'inspection les éléments déjà fournis pour attester la conformité de l'implication, suivant R2362-17 et R2363-5 ; ni taux ni assiette fiscale ne sont en cause.",
        'after': "Aucun envoi systématique de ces éléments à l'inspection, sans dépôt de substitution ; subsistent les informations des salariés et les contrôles légalement autonomes.",
        'unit': 'legal_duty',
        'affected_population': "Personnes participantes, filiales et établissements concernés par la constitution d'une société coopérative européenne par fusion.",
        'conditions_and_transition': "Dispense dès l'entrée en vigueur, y compris pour un envoi non effectué relatif à une fusion antérieure ; documents déjà transmis, droits et recours antérieurs protégés.",
        'replacement_or_new_burdens': "Aucun dépôt de remplacement et aucun nouveau pouvoir de collecte ; maintien des demandes de communication ayant un fondement légal autonome.",
        'source_quote': "Les dispositions d'application du présent titre relatives à la procédure applicable aux litiges et aux informations transmises à l'inspection du travail en cas de constitution de la société coopérative européenne par fusion sont déterminées par décret en Conseil d'Etat.",
        'proposed_quote': "La constitution d'une société coopérative européenne par fusion ne donne lieu à aucune transmission systématique à l'inspection du travail des éléments établis pour attester la conformité des modalités d'implication des salariés aux dispositions du présent titre.",
    }],
    ["Transmission systématique à l'inspection du travail des éléments d'attestation de l'implication des salariés lors d'une constitution par fusion, y compris les envois correspondants encore à effectuer."],
)

keep(
    'L2362-1',
    "Maintien intégral de l'institution du groupe spécial de négociation dès que possible après le projet de fusion, transformation ou autre constitution, et de sa personnalité juridique. Le groupe garantit une représentation transnationale des salariés avant la création ; la personnalité lui permet d'agir et de défendre ses droits. Il ne s'agit pas d'un agrément préalable d'embauche. Aucun délai minimal d'attente, prélèvement ou rapport distinct ne figure dans cet article à retirer.",
    "Les trois déclencheurs et la différence entre publication et adoption du projet sont conservés. L2362-3 organise les représentants, L2362-4 leur négociation et L2362-7 leur faculté qualifiée de ne pas négocier. Ne pas confondre ce groupe avec un nouveau contrat de travail ou avec la durée d'une mission. La directive 2003/72/CE encadre cette représentation initiale ; sa confrontation primaire intégrale reste à faire, aucun document européen complet n'étant joint.",
    "L'organe de négociation et sa capacité juridique sont maintenus pour garantir des droits effectifs avant constitution ; aucun allègement déjà existant n'est compté comme nouveau.",
    "Ce maintien ne valide ni le calendrier réel d'un projet particulier ni la composition d'un groupe dans un autre Etat.",
    "Aucune charge nouvelle n'est identifiée : pas d'instance parallèle, de délai minimum ou de dossier supplémentaire au-delà du groupe prévu par la source.",
)

keep(
    'L2362-2',
    "Maintien intégral de l'accord écrit entre le groupe spécial de négociation et les dirigeants ou personnes physiques participants, ou leurs représentants. L'écrit établit les modalités et les titulaires des droits et permet leur contrôle ; il n'est ni une seconde transmission ni une autorisation administrative. La faculté de représentation et la négociation des modalités sont conservées. Retirer l'accord ou son support probatoire fragiliserait l'opposabilité des droits sans formalité redondante identifiée.",
    "L2361-3 vise information, consultation et participation éventuelle. L2362-10 et les cibles L2352-16 à L2352-20, lues, en fixent le contenu, et L2362-7 réserve le choix qualifié de ne pas négocier. Cet accord d'implication des salariés n'est pas un contrat d'embauche à durée limitée et n'emporte aucune fin automatique d'emploi. L'allègement de L2363-2 ne supprime pas cet accord lorsqu'il a été conclu.",
    "La négociation et la preuve écrite du contenu convenu sont conservées sans en faire une nouvelle exigence de dépôt ou d'agrément.",
    "Seul l'accord d'implication dans une coopérative ayant siège et administration centrale en France est visé ; aucune validation des accords particuliers n'est effectuée.",
    "Aucune charge nouvelle n'est identifiée : même écrit, mêmes parties et même faculté de représentation, sans certification ou transmission ajoutée.",
)

keep(
    'L2362-3',
    "Maintien intégral du renvoi commun aux règles de désignation, d'élection et de statut du groupe spécial. Les dispositions cibles répartissent les sièges entre Etats et collèges, préservent les entités absorbées, organisent la représentation en l'absence de syndicat et ouvrent le recours judiciaire. Les remplacer par une désignation unilatérale supprimerait des protections collectives essentielles. La source procède déjà par mutualisation des règles ; aucun second régime autonome n'est créé à simplifier.",
    "L2352-3 à L2352-8 ont été lus intégralement : répartition proportionnelle et salariés représentés, sièges supplémentaires plafonnés à 20 %, désignation syndicale et élection directe, adaptation aux changements substantiels, juge judiciaire. Leur application à la coopérative s'articule avec les majorités propres de L2362-7 et les règlements D2362-1 à D2362-16. D2362-7 impose la lettre recommandée pour la notification : cet allègement potentiel doit viser ce règlement, non être prétendu accompli par le maintien du présent renvoi. Le contenu de cette notification et les délais de recours distincts restent nécessaires.",
    "Les garanties de composition et de recours sont maintenues ; le renvoi existant n'est pas présenté comme une nouvelle fusion ou une suppression de formalité.",
    "Les canaux réglementaires de notification ne sont pas réécrits dans cet article ; leur coût et les procédures électorales des autres Etats restent hors mesure.",
    "Aucune charge nouvelle n'est identifiée : aucune attestation, nouvelle élection ou nouvelle notification ne résulte du maintien intégral de la source.",
)

keep(
    'L2362-4',
    "Maintien intégral de l'invitation, de l'information sur les participants et les effectifs, du calendrier et du paiement du temps de réunion. Les données rendent possibles la désignation, les majorités et la négociation ; l'information directe des salariés sans représentant évite leur exclusion. Les six mois sont une durée maximale de négociation, non une attente minimale avant de conclure ; la prolongation jusqu'à un an suppose l'accord des parties. Le salaire à l'échéance normale protège l'indépendance des représentants.",
    "Les quatre alinéas sont maintenus, sans les confondre avec le préavis individuel de quinze jours. D2362-14, lu en entier, impose une convocation recommandée avec avis de réception et fait partir les six mois de la première réunion, tandis que le texte législatif rattache le début à la constitution du groupe : articulation réglementaire préexistante à coordonner expressément sur le point de départ, sans retarder artificiellement la négociation. Le canal postal est une contrainte de ce règlement, non une charge supprimée ici. D2362-1, D2362-2, D2362-4 et D2362-15, lus, détaillent les destinataires et informations. Aucune seconde communication des mêmes données n'est inventée dans la proposition, puisqu'aucun nouveau corps n'est produit.",
    "Information indispensable, faculté de conclure avant six mois, prolongation consensuelle et rémunération demeurent. Aucune réduction fictive d'un délai minimal ou d'un double dépôt n'est annoncée.",
    "Le règlement de convocation et son articulation chronologique ne sont pas modifiés dans ce lot législatif ; les accords existants et les droits salariaux restent entiers.",
    "Aucune charge nouvelle n'est identifiée : la source entière demeure sans nouvelle réunion, collecte périodique, justificatif ou délai de réponse.",
)

keep(
    'L2362-5',
    "Maintien intégral de la prise en charge par les personnes participantes des dépenses nécessaires à la bonne exécution de la mission du groupe. Ce financement empêche de faire supporter aux représentants le coût de l'exercice de leurs droits. La nécessité borne la dépense ; l'article n'impose ni taxe, taux forfaitaire, dossier de subvention ni autorisation administrative. Transférer ce coût aux salariés ne serait pas une suppression de charge collective démontrée.",
    "L2362-6 distingue l'assistance des experts et la prise en charge d'un seul expert. L2362-4 conserve le salaire du temps de réunion : la suppression d'un financement dans L2362-5 ne doit pas neutraliser cette garantie. Le cadre européen d'implication des salariés exige des moyens effectifs ; sa version intégrale n'est pas jointe et aucun montant national d'économie ou de coût n'est calculé.",
    "L'obligation de financement nécessaire est conservée, sans déplacement de financeur présenté comme une économie.",
    "Aucun barème, budget ou coût total des négociations n'est déduit de la seule notion de dépense nécessaire.",
    "Aucune charge nouvelle n'est identifiée : maintien du même payeur et du même critère de nécessité, sans justificatif standard ou prélèvement additionnel.",
)

keep(
    'L2362-6',
    "Maintien intégral du libre choix des experts, de leur rôle consultatif et de la prise en charge des frais de négociation et d'un seul expert. L'assistance est une faculté du groupe permettant une négociation éclairée ; elle n'est pas un agrément obligatoire de l'activité. La limitation à un expert financé borne déjà la charge des participants sans interdire une autre assistance. Réduire encore le droit d'expertise ou en faire payer systématiquement les salariés dégraderait la garantie de négociation.",
    "Ne pas confondre le nombre d'experts pouvant assister le groupe et le nombre d'experts dont les frais sont à la charge des personnes participantes. Les dépenses nécessaires générales restent à L2362-5. La coordination de L2362-9 conserve le secret et la discrétion des experts. Les règles européennes d'assistance et de financement doivent être confrontées à la directive intégrale non jointe ; aucune extension de prise en charge n'est créée.",
    "Faculté d'assistance et limitation du financement à un expert sont conservées ; aucune obligation nouvelle de recourir à un expert n'est introduite.",
    "Ni les honoraires convenus ni l'utilité d'une expertise particulière ne sont évalués ; aucun gain budgétaire n'est établi.",
    "Aucune charge nouvelle n'est identifiée : mêmes droits de choix, même rôle consultatif et même limite de prise en charge, sans registre ni agrément.",
)

keep(
    'L2362-7',
    "Maintien intégral des trois alinéas et de leurs majorités. La double majorité absolue donne une assise représentative aux décisions ; la majorité des deux tiers, issue d'au moins deux Etats et représentant deux tiers des salariés, protège les décisions de renoncer au régime négocié ou de réduire la participation existante. L'exception de transformation conserve la participation acquise. Les seuils de 25 % et 50 % déclenchent la majorité renforcée, non un prélèvement ou une obligation de négociation supplémentaire. Supprimer ces garanties ne serait pas une simplification acceptable du consentement collectif.",
    "Contrôle précis : majorité absolue des membres ET des salariés au premier alinéa, une voix par membre ; deux tiers des membres, deux Etats au moins ET deux tiers des salariés au deuxième ; 25 % en fusion et 50 % par autre moyen au troisième, avec exception du premier alinéa de L2362-12. Le renvoi à la majorité du deuxième alinéa au troisième n'emporte pas son exclusion du chapitre III pour toute décision : il vise la règle de majorité. D2362-16, lu, fixe la pondération des salariés représentés. L2361-2 et L2363-1 préservent les effets spécifiques de la décision de ne pas négocier. Le cadre de la directive 2003/72/CE reste à confronter au texte primaire intégral non joint.",
    "Les facultés de renoncer au circuit négocié et de choisir des modalités de participation demeurent sous les mêmes garanties. Aucune modification de seuil ou baisse de charge n'est revendiquée.",
    "L'article ne régit ni le vote d'un accord ordinaire d'entreprise de L2232 ni l'ancienneté ou la notification d'une rupture individuelle.",
    "Aucune charge nouvelle n'est identifiée : majorités, pondérations et exceptions sont conservées sans nouveau quorum, certificat ou scrutin ajouté.",
    "Les avantages possibles sont la faculté de ne pas engager ou de clore la négociation, l'application des règles nationales d'information-consultation et l'exclusion corrélative du chapitre III, ainsi que la latitude de convenir d'une participation inférieure sous majorité renforcée. Ils restent accessibles pour les futures constitutions éligibles comme pour les décisions actuelles, sans condition nouvelle. La transformation avec participation existante demeure exclue de la renonciation, et le plancher d'équivalence de L2362-12 est préservé : ce sont des garanties de droits, non des charges fiscales à abolir.",
)

keep(
    'L2362-8',
    "Maintien intégral de la version française des documents remis aux représentants des salariés. Dans cette négociation transnationale, le droit d'obtenir au moins cette version permet l'intelligibilité, l'examen des droits et l'exercice du consentement. Il n'impose pas de traduire les documents en toutes langues ni de recourir à un traducteur agréé. Aucun autre document, enregistrement ou certification n'est exigé. Supprimer ce droit sans garantie équivalente de compréhension ferait peser la charge linguistique sur les représentants.",
    "La source exige au moins une version en français des documents communiqués, sans procédure d'approbation, certification linguistique ou délai minimal. La gratuité de la mission et la rémunération du temps de réunion restent aux articles L2362-4 à L2362-6. Ce maintien est justifié par l'effectivité de la négociation, sans affirmer que la directive européenne impose précisément la langue française.",
    "La garantie d'intelligibilité est conservée avec son champ limité ; aucune prétendue suppression d'agrément linguistique absent de la source n'est comptée.",
    "Aucune évaluation du volume de traduction ou des langues effectivement comprises dans un groupe particulier n'est disponible.",
    "Aucune charge nouvelle n'est identifiée : maintien de la seule version française déjà requise, sans traducteur certifié, traduction supplémentaire ou formulaire imposé.",
)

secret_xml = (
    "<p>Aucun salarié ne peut être sanctionné ou licencié en raison de l'exercice du droit prévu à l'article L. 2362-7. Toute décision ou tout acte contraire est nul de plein droit.</p>"
    "<p>Les membres du groupe spécial de négociation ainsi que les experts qui les assistent sont tenus au secret professionnel pour toutes les questions relatives aux procédés de fabrication. Ils sont tenus à une obligation de discrétion à l'égard des informations revêtant un caractère confidentiel et présentées comme telles par l'employeur.</p>"
    "<p>Les droits, obligations et recours nés de faits antérieurs à l'entrée en vigueur de la loi portant cette coordination demeurent régis par les dispositions qui leur étaient applicables.</p>"
)
draft(
    'L2362-9', secret_xml,
    "Coordination nécessaire, sans réduction de protection ni simple changement de vocabulaire : le renvoi de la source à L2352-15 conduit lui-même à l'ancien article L2325-5. Les garanties sont rendues directement opératoires dans le titre des coopératives, en distinguant le secret sur les procédés de fabrication de la discrétion sur les informations réellement confidentielles et présentées comme telles. La protection contre les sanctions et licenciements reproduit celle de L2352-14 en rattachant expressément son exercice aux décisions de L2362-7 propres à la coopérative, au lieu du renvoi indirect aux décisions de la société européenne.",
    "L2352-14 et L2352-15 ont été lus entièrement dans le corpus. Le second vise L2325-5, absent comme article actif du corpus ; la source actuelle L2315-3 et sa note de transition de 2017 ont également été lues. La rédaction autonome reprend les deux objets et les deux conditions de confidentialité de cette règle, sans renvoi nouveau à L2315-3, ni pouvoir de classer arbitrairement toute information confidentielle. Nouveau renvoi explicite à L2362-7 : cette cible ne figure pas parmi les targets de reference-targets.json mais son texte entier est fourni et examiné dans source.json. L2352-15 reste à coordonner hors du présent lot ; la portée historique de son ancien renvoi ne vaut pas création rétroactive d'une infraction. Les autorisations de licenciement des représentants fondées sur d'autres textes et les procédures collectives ne sont pas supprimées par le préavis individuel de quinze jours.",
    "Le texte entier remplace deux renvois indirects par une protection et une obligation de confidentialité explicites. C'est une coordination, sans réduction démontrée de coût, de taxe ou de devoir de secret.",
    "La coordination ne réécrit pas L2352-15 ni le statut protecteur général des représentants. La portée de l'ancien renvoi et les faits antérieurs restent soumis à leur droit propre ; aucune validation indépendante n'est affirmée.",
    "Aucune charge administrative nouvelle n'est identifiée : les devoirs de secret et de discrétion déjà annoncés par la source sont précisés sans registre, donnée, délai ou procédure de classification ajoutés. Leur clarification n'est pas comptée comme une diminution de charges.",
    [{
        'kind': 'coordination',
        'measure_id': 'sce-secret-professionnel-renvois',
        'description': "Rendre explicites la protection liée aux décisions de la coopérative et les deux devoirs de confidentialité, en supprimant le renvoi indirect à un ancien article du comité d'entreprise.",
        'before': "L2362-9 renvoie à L2352-14 et L2352-15 ; ce dernier renvoie encore à L2325-5 pour le secret professionnel et la discrétion.",
        'after': "Protection directement rattachée à L2362-7 ; secret des procédés et discrétion sur les informations confidentielles présentées comme telles directement définis.",
        'unit': 'legal_duty',
        'affected_population': "Salariés exerçant les droits de L2362-7, membres du groupe spécial de négociation de la coopérative européenne et experts les assistant.",
        'conditions_and_transition': "Coordination applicable à l'entrée en vigueur ; les droits, obligations et recours relatifs aux faits antérieurs restent sous leurs règles antérieures.",
        'replacement_or_new_burdens': "Pas de nouveau devoir documentaire ni de réduction revendiquée ; précision du contenu de devoirs déjà visés par la source et maintien des protections autonomes.",
        'source_quote': "Les dispositions des articles L. 2352-14 et L. 2352-15 relatives à la protection contre le licenciement et au secret professionnel des membres du groupe spécial de négociation de la société européenne s'appliquent à la société coopérative européenne.",
        'proposed_quote': "Les membres du groupe spécial de négociation ainsi que les experts qui les assistent sont tenus au secret professionnel pour toutes les questions relatives aux procédés de fabrication.",
    }],
)

keep(
    'L2362-10',
    "Maintien intégral de la négociation avec toutes les personnes participantes et de son contenu commun avec celui de la société européenne. La réserve du deuxième alinéa de L2362-7 préserve le choix collectif de ne pas négocier ou de clore la négociation. Les règles de contenu précisent le périmètre, les moyens et les modalités de représentation ; leur suppression ne retirerait pas seulement des formalités mais rendrait les droits incertains. Aucun nouveau dépôt ou agrément ne figure ici.",
    "L2352-16 à L2352-20 ont été lus en entier : périmètre, composition, attributions, fréquence, moyens, procédure alternative, durée et renégociation ; modalités de participation ; équivalence en transformation ; choix entre formes existantes ; option d'appliquer le régime de référence. L2362-11 et L2362-12 précisent les garanties propres aux coopératives, sans contredire ces renvois. Le renvoi à L2352-18 ne supprime pas la nullité et le repli de L2362-12. Ni le contenu d'une convention d'aide ni sa durée ne constituent ici le terme d'un emploi.",
    "La liberté encadrée de négocier et l'option du régime de référence demeurent ; aucune nouvelle simplification n'est attribuée à cette mutualisation déjà en vigueur.",
    "La validité de chaque accord et la compatibilité européenne de ses clauses ne sont pas établies par le seul maintien du renvoi.",
    "Aucune charge nouvelle n'est identifiée : aucune clause, formalité de dépôt ou autorisation ne s'ajoute au contenu déjà demandé par les articles cibles.",
)

keep(
    'L2362-11',
    "Maintien intégral de la clause de renégociation relative aux changements de structure de la coopérative, de ses filiales et établissements. Elle évite que la représentation négociée à la création reste figée après une restructuration et serve à contourner les droits des nouvelles composantes. La source impose de prévoir ce cas dans l'accord, non un rapport périodique, une autorisation administrative ou une renégociation à chaque variation mineure. Retirer la clause priverait la protection d'une adaptation convenue.",
    "Le 7° de L2352-16, lu, demande déjà les cas et la procédure de renégociation ; L2362-11 précise un cas structurel pour les coopératives. L2364-3 rend également applicable L2354-4 après immatriculation pour les changements susceptibles d'affecter substantiellement les droits. Les deux règles n'imposent pas deux groupes ou deux négociations successives pour un même changement. Le cadre européen des clauses d'adaptation reste à confronter à la directive intégrale non jointe avant une suppression de cette garantie.",
    "La clause d'adaptation demeure ; aucun double circuit non établi n'est artificiellement supprimé ou compté.",
    "La portée des clauses de chaque accord et la qualification d'un changement de structure restent à apprécier dans leur cas particulier.",
    "Aucune charge nouvelle n'est identifiée : même clause de renégociation, sans périodicité, inventaire des changements ou procédure d'autorisation ajoutés.",
)

keep(
    'L2362-12',
    "Maintien intégral du plancher d'équivalence de l'information, de la consultation et de la participation en cas de transformation d'une coopérative. La nullité d'un accord inférieur et le régime de repli empêchent que le changement de forme juridique fasse perdre les droits collectifs existants. Il ne s'agit ni d'une durée minimale d'emploi ni d'une taxe. Le maintien des niveaux est une protection essentielle, et le second alinéa donne un effet concret au premier.",
    "L2352-18, lu via L2362-10, exprime le principe d'équivalence ; L2362-12 en organise aussi la nullité et l'application du chapitre III. L2362-7 interdit dans ce cas la renonciation lorsque la participation existe et réserve ce premier alinéa dans sa règle de majorité renforcée. La nouvelle rédaction de L2363-2 dispense d'un engagement distinct, sans retirer le régime de repli ni la sanction de l'accord inférieur. La garantie de transformation relève également du cadre européen non joint intégralement.",
    "L'équivalence de niveau et son mécanisme de sauvegarde restent entiers pour les transformations futures ; aucune restriction favorable supprimée n'est présentée comme un gain.",
    "L'appréciation de l'équivalence concrète de trois droits et la validité des accords individuels ne sont pas vérifiées dans ce lot.",
    "Aucune charge nouvelle n'est identifiée : aucun contrôle préalable, justificatif ou seuil supplémentaire n'est ajouté au plancher et au recours existants.",
)

keep(
    'L2363-1',
    "Maintien intégral du comité subsidiaire en l'absence d'accord à l'issue de la période de négociation et en l'absence de décision qualifiée de ne pas négocier. Les deux conditions évitent un cumul avec l'accord et respectent le choix du groupe. Supprimer le comité dans ce seul cas laisserait les salariés sans organe transnational de référence. L'article ne crée ni déclaration distincte ni durée d'emploi limitée.",
    "L2362-4 conserve les six mois de négociation et la prolongation consensuelle dans la limite d'un an ; L2362-7, deuxième alinéa, fixe la décision qui exclut le chapitre III. Le renvoi à cette seule décision est exact, sans assimilation de toute décision prise à la majorité renforcée à une renonciation. L2363-2 est coordonné dans le présent lot pour supprimer seulement l'acte distinct de choix ou d'engagement ; le comité ici institué demeure. L2363-3 à L2363-6, lus dans le corpus, déterminent attributions, composition, désignation et fonctionnement.",
    "Le mécanisme subsidiaire et ses deux exclusions demeurent ; il n'est pas compté comme une nouvelle création ou fusion de régime.",
    "Les modalités concrètes de composition et fonctionnement et le cadre européen non joint ne sont pas entièrement réécrits par cet article de déclenchement.",
    "Aucune charge nouvelle n'est identifiée : maintien du même comité dans les mêmes hypothèses, sans nouveau dépôt ou nouvelle période d'attente.",
)

registration_xml = (
    "<p>Dans le cas prévu à l'article L. 2363-1, les dispositions du présent chapitre et du chapitre IV du présent titre s'appliquent de plein droit, dans leurs conditions propres. Sur le fondement du présent article, l'immatriculation de la société coopérative européenne n'est subordonnée ni à une décision distincte des parties de mettre en œuvre ces dispositions ni à un engagement distinct des dirigeants des personnes morales participantes ou des personnes physiques participantes de les appliquer.</p>"
    "<p>La dispense de cette décision ou de cet engagement ne dispense pas de respecter les droits d'implication des salariés ni les autres conditions légales de constitution et d'immatriculation. Elle ne peut donner lieu à une déclaration, une attestation ou un dépôt de remplacement ayant le même objet.</p>"
    "<p>Le présent article s'applique aux demandes d'immatriculation présentées à compter de l'entrée en vigueur de la loi portant cette suppression ainsi qu'aux demandes en cours à cette date, sans nouveau dépôt de la demande ni remise à zéro des délais. Les accords et engagements valablement souscrits avant cette date demeurent opposables dans leur champ ; les droits et recours qui en sont nés sont préservés.</p>"
)
draft(
    'L2363-2', registration_xml,
    "Réforme de fond : les règles subsidiaires du chapitre III et du chapitre IV s'appliquent directement dans le cas de L2363-1, sans décision spéciale des parties ni engagement distinct des dirigeants à respecter ces règles légales. La condition formelle d'immatriculation est effectivement retirée, sans supprimer les droits de représentation, le respect du régime de référence ou les autres contrôles de constitution. L'acte d'adhésion préalable ne démontre pas une fonction protectrice supplémentaire à l'application directe et opposable de la loi. Aucun certificat ou dépôt équivalent ne le remplace.",
    "L2363-1 et L2362-4 sont lus dans le lot : absence d'accord au terme de la négociation, sans décision de L2362-7 excluant le chapitre III. L2364-1 à L2364-3 ont été lus en entier dans le corpus : aménagement conventionnel des anciennes institutions, réexamen après quatre ans et adaptation après immatriculation restent applicables. D2363-1, lu, doit être coordonné : supprimer l'exigence de joindre la décision spéciale ou, au 2°, l'engagement écrit ; ne pas le remplacer par une attestation identique. Les accords existants et les pièces de contrôle ayant un objet autonome restent à leur régime propre. Les références de ce règlement à L2363-2 pour un système de participation et à L2361-2/L2361-5 dans la liste sont des articulations préexistantes à confronter, non une description du contenu littéral de ces articles. Le règlement (CE) 1435/2003 et la directive 2003/72/CE ne sont pas fournis intégralement : les conditions européennes de constitution et d'immatriculation doivent être confrontées avant adoption, sans présumer que cette suppression d'acte national dispense du contrôle de l'implication.",
    "La source entière imposait comme préalable une décision des parties ou un engagement des dirigeants à appliquer les chapitres III et IV. La proposition retire cet acte distinct et donne force légale directe au même régime de référence, sans abandonner les conditions de fond ni compter une deuxième suppression au titre de D2363-1.",
    "La dispense ne concerne que l'acte distinct d'application du régime subsidiaire, non le dossier général d'immatriculation, les vérifications européennes, les obligations d'information ou les accords librement conclus. Les coûts évités et le solde global de complexité restent inconnus.",
    "Aucune charge nouvelle n'est identifiée : l'application de plein droit remplace l'adhésion formelle au même régime, sans droit de représentation supplémentaire, nouvelle donnée, attestation ni délai. Les autres conditions légales ne sont ni étendues ni tenues pour satisfaites.",
    [{
        'kind': 'obligation_removed',
        'measure_id': 'sce-immatriculation-sans-engagement-distinct',
        'description': "Supprimer l'acte distinct de décision ou d'engagement d'appliquer le régime légal d'implication avant immatriculation, le régime s'appliquant directement.",
        'before': "Dans le cas de L2363-1, immatriculation subordonnée à une décision des parties d'appliquer les chapitres III et IV ou à un engagement des dirigeants ; D2363-1 prévoit la pièce correspondante, dont l'engagement écrit au 2°.",
        'after': "Même régime d'implication applicable de plein droit, sans cet acte distinct ni document de remplacement ; les autres conditions de constitution et d'immatriculation demeurent.",
        'unit': 'legal_duty',
        'affected_population': "Parties, dirigeants des personnes morales et personnes physiques participants à une coopérative européenne relevant de L2363-1.",
        'conditions_and_transition': "Demandes nouvelles ou en cours à l'entrée en vigueur ; pas de nouveau dépôt ni de redémarrage des délais ; engagements et accords valables antérieurs et leurs droits préservés.",
        'replacement_or_new_burdens': "Aucun engagement, certificat, attestation ou dépôt de substitution ; application directe de devoirs de représentation déjà attachés au régime, sans nouveau taux ou financement.",
        'source_quote': "Dans le cas prévu à l'article L. 2363-1, l'immatriculation de la société coopérative européenne ne peut intervenir que si les parties décident de mettre en œuvre les dispositions du présent chapitre et du chapitre IV du présent titre, ou que si les dirigeants des personnes morales participantes ou les personnes physiques participantes s'engagent à en faire application.",
        'proposed_quote': "Dans le cas prévu à l'article L. 2363-1, les dispositions du présent chapitre et du chapitre IV du présent titre s'appliquent de plein droit, dans leurs conditions propres.",
    }],
    ["Décision distincte des parties ou engagement distinct des dirigeants d'appliquer les chapitres III et IV, exigé comme préalable spécifique à l'immatriculation dans le cas de L2363-1, et sa pièce justificative de même objet."],
)

# L'ordre et les identifiants du lot restent exactement ceux des sources assignées.
by_number = {a['number']: a for a in answers}
answers = [by_number[s['number']] for s in sources]
Path('answer.json').write_text(json.dumps(answers, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answers)} articles')
