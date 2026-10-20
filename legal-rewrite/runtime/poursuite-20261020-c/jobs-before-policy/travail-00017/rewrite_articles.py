import json
from pathlib import Path


drafts = {}


def add(number, proposed_xml, reason, review_notes):
    assert number not in drafts
    drafts[number] = {
        'proposed_xml': proposed_xml.strip(),
        'reason': reason,
        'review_notes': review_notes,
    }


add('L1255-8', '''
<p>L'utilisateur qui méconnaît les conditions de renouvellement du contrat fixées par la convention ou l'accord de branche conclu en application de l'article L. 1251-35 ou, le cas échéant, par l'article L. 1251-35-1 est puni d'une amende de 3 750 euros.</p>
<p>En cas de récidive, les peines sont de six mois d'emprisonnement et de 7 500 euros d'amende.</p>
''',
    "Réécriture à droit constant : l'utilisateur est directement désigné comme auteur du manquement et les deux sources des conditions de renouvellement sont rattachées au même verbe. Les peines initiale et de récidive sont conservées ; aucune réforme de fond n'est appliquée au travail temporaire.",
    "Conserver les renvois à L. 1251-35 et L. 1251-35-1, vérifiés dans le corpus public, ainsi que les montants de 3 750 et 7 500 euros et les six mois d'emprisonnement. La note source maintient l'application aux contrats de travail conclus après la publication de l'ordonnance n° 2017-1387 du 22 septembre 2017, en vertu de son article 40, VIII. Cette règle temporelle demeure attachée au texte ; elle ne constitue pas la date d'entrée en vigueur d'une réforme nouvelle.")

add('L1255-9', '''
<p>L'utilisateur qui méconnaît les règles de succession de contrats sur un même poste fixées par la convention ou l'accord de branche conclu en application de l'article L. 1251-36 ou, le cas échéant, par l'article L. 1251-36-1 est puni d'une amende de 3 750 euros.</p>
<p>En cas de récidive, les peines sont de six mois d'emprisonnement et de 7 500 euros d'amende.</p>
''',
    "Réécriture à droit constant : la phrase identifie immédiatement l'utilisateur sanctionné et présente plus directement l'articulation entre les règles conventionnelles et légales de succession des contrats. Les sanctions sont maintenues, sans réforme de fond.",
    "Les renvois à L. 1251-36 et L. 1251-36-1 ont été vérifiés dans le corpus public. Maintien de 3 750 euros, puis de six mois d'emprisonnement et de 7 500 euros en récidive. L'article 40, VIII, de l'ordonnance n° 2017-1387 du 22 septembre 2017, cité par la note source, réserve cette rédaction aux contrats de travail conclus après la publication de cette ordonnance ; cette disposition historique d'application doit être conservée avec le texte.")

add('L1255-10', '''
<p>L'utilisateur est puni d'une amende de 3 750 euros lorsqu'il recourt à un salarié temporaire dans l'une des situations suivantes :</p>
<p>1° Il n'a pas conclu avec un entrepreneur de travail temporaire un contrat écrit de mise à disposition dans le délai prévu à l'article L. 1251-42 ;</p>
<p>2° Il a omis de communiquer, dans le contrat de mise à disposition, l'ensemble des éléments de rémunération conformément au 6° de l'article L. 1251-43.</p>
<p>En cas de récidive, les peines sont de six mois d'emprisonnement et de 7 500 euros d'amende.</p>
''',
    "Réécriture à droit constant : le sujet de l'infraction est explicite et chaque branche de l'alternative comporte une proposition complète. Les deux manquements, leurs renvois et la récidive restent distincts ; aucune réforme de fond.",
    "Les 1° et 2° sont conservés dans leur ordre. Le délai reste celui de L. 1251-42 et l'obligation de communication reste celle du 6° de L. 1251-43. Aucun délai chiffré n'est ajouté. Peines conservées : 3 750 euros ; six mois d'emprisonnement et 7 500 euros en récidive.")

add('L1255-11', '''
<p>Toute personne qui méconnaît, directement ou par personne interposée, l'interdiction d'exercer l'activité d'entrepreneur de travail temporaire prononcée par la juridiction en application du dernier alinéa de l'article L. 1255-1 ou du dernier alinéa de l'article L. 1255-2 est punie de six mois d'emprisonnement et de 6 000 euros d'amende.</p>
''',
    "Réécriture à droit constant : l'auteur de l'infraction devient le sujet de la phrase et la référence au dernier alinéa est explicitée pour chacun des deux articles. Le recours à une personne interposée et les peines demeurent inchangés ; aucune réforme de fond.",
    "Les derniers alinéas de L. 1255-1 et L. 1255-2 ont été lus dans le corpus public et contiennent bien l'interdiction d'exercer. Maintien des six mois d'emprisonnement et de l'amende de 6 000 euros, distincte des amendes de récidive prévues dans les autres articles.")

add('L1255-12', '''
<p>Dans tous les cas prévus à la présente section, la juridiction peut, à titre de peine complémentaire, ordonner l'affichage du jugement dans les conditions prévues à l'article 131-35 du code pénal et son insertion, intégrale ou par extraits, dans les journaux qu'elle désigne. L'entrepreneur de travail temporaire ou l'utilisateur condamné supporte les frais de ces mesures. Ces frais ne peuvent dépasser le montant maximum de l'amende encourue.</p>
''',
    "Réécriture à droit constant : la décision de publicité, la personne qui en supporte les frais et le plafond de ces frais sont exprimés dans trois phrases successives. Le caractère facultatif de la peine complémentaire et les deux mesures de publicité sont conservés ; aucune réforme de fond.",
    "Maintien du renvoi à l'article 131-35 du code pénal, du choix des journaux par la juridiction et de l'insertion intégrale ou par extraits. Le plafond demeure celui de l'amende encourue, et non de l'amende effectivement prononcée. Le code pénal est hors des cinq codes du périmètre et n'est pas modifié.")

add('L1255-13', '''
<p>Toute personne qui méconnaît les dispositions des articles L. 1253-1 à L. 1253-10 et L. 1253-17 est punie d'une amende de 3 750 euros.</p>
<p>En cas de récidive, les peines sont de six mois d'emprisonnement et de 7 500 euros d'amende.</p>
<p>La juridiction peut également, à titre de peine complémentaire, ordonner l'affichage du jugement à la porte du siège du groupement et aux portes des entreprises utilisatrices, dans les conditions prévues à l'article 131-35 du code pénal, ainsi que son insertion, intégrale ou par extraits, dans les journaux qu'elle désigne. La personne condamnée supporte les frais de ces mesures. Ces frais ne peuvent dépasser le montant maximum de l'amende encourue.</p>
''',
    "Réécriture à droit constant : l'auteur du manquement est explicite et la longue phrase sur la publicité du jugement est séparée de la règle de prise en charge des frais. Les trois alinéas, les lieux d'affichage et les sanctions sont maintenus ; aucune réforme de fond.",
    "La plage L. 1253-1 à L. 1253-10 et le renvoi distinct à L. 1253-17 sont conservés. Contrôle des montants de 3 750 et 7 500 euros et des six mois d'emprisonnement. Maintien de l'article 131-35 du code pénal, des deux catégories de lieux d'affichage et du plafond égal au maximum de l'amende encourue.")

add('L1255-14', '''
<p>L'entrepreneur de portage salarial est puni de 3 750 € d'amende lorsqu'il commet l'un des manquements suivants :</p>
<p>1° Il conclut un contrat de travail en portage salarial pour une activité de services en méconnaissance de l'article L. 1254-5 ;</p>
<p>2° Il conclut un contrat de travail en portage salarial sans respecter l'article L. 1254-7 ;</p>
<p>3° Il conclut un contrat de travail en portage salarial à durée déterminée qui ne comporte pas de terme précis ou qui ne fixe pas de durée minimale lorsqu'il ne comporte pas de terme précis, en méconnaissance de l'article L. 1254-11 ;</p>
<p>4° Il ne respecte pas les durées maximales du contrat de travail en portage salarial à durée déterminée prévues aux articles L. 1254-12, L. 1254-13 et L. 1254-17 ;</p>
<p>5° Il conclut un contrat de travail en portage salarial sans la mention obligatoire prévue aux articles L. 1254-14 ou L. 1254-20 ;</p>
<p>6° Il conclut un contrat de travail en portage salarial qui ne comporte pas l'ensemble des clauses et mentions prévues aux articles L. 1254-15 ou L. 1254-21 ;</p>
<p>7° Il ne transmet pas au salarié porté le contrat de travail en portage salarial dans le délai prévu à l'article L. 1254-16 ;</p>
<p>8° Il ne conclut pas avec l'entreprise cliente d'une personne portée le contrat commercial de prestation de portage salarial dans le délai prévu à l'article L. 1254-22, ou il ne délivre pas au salarié porté une copie de ce contrat dans le même délai ;</p>
<p>9° Il conclut avec l'entreprise cliente d'une personne portée un contrat commercial de prestation de portage salarial qui ne comporte pas les mentions prévues à l'article L. 1254-23 ;</p>
<p>10° Il ne respecte pas les conditions d'exercice de l'activité de portage salarial prévues à l'article L. 1254-24 ;</p>
<p>11° Il ne respecte pas l'obligation de mettre en place et de gérer, pour chaque salarié porté, un compte d'activité conformément à l'article L. 1254-25 ;</p>
<p>12° Il exerce son activité sans avoir souscrit de garantie financière, en méconnaissance de l'article L. 1254-26 ;</p>
<p>13° (Abrogé) ;</p>
<p>14° Il ne respecte pas, en méconnaissance de l'article L. 1254-28, les obligations relatives à la médecine du travail définies aux articles L. 4121-1 à L. 4121-5.</p>
<p>En cas de récidive, les peines sont de six mois d'emprisonnement et de 7 500 € d'amende.</p>
<p>La juridiction peut également interdire l'exercice de l'activité d'entreprise de portage salarial pour une durée de deux à dix ans.</p>
''',
    "Réécriture à droit constant : chaque infraction a pour sujet explicite l'entrepreneur de portage salarial et les propositions relatives sont simplifiées. Les quatorze emplacements numérotés, dont le 13° abrogé, les délais par renvoi, la récidive et l'interdiction complémentaire demeurent en place. Aucune réforme de fond.",
    "Peines conservées : 3 750 €, six mois et 7 500 € en récidive, interdiction de deux à dix ans. Trois difficultés préexistantes sont signalées sans correction : le 1° parle d'une activité de services alors que L. 1254-5 vise les services à la personne ; le 3° juxtapose l'absence de terme précis et l'absence de durée minimale alors que L. 1254-11 admet, sous condition, un terme non précis ; le 14° qualifie de médecine du travail les obligations de L. 4121-1 à L. 4121-5, qui portent sur la santé et la sécurité. Les renvois qualificatifs sont conservés ; toute clarification de leur portée pénale exige une coordination expresse. Le corpus confirme L. 1254-27 dans sa rédaction depuis le 28 mai 2026 ; le 13° abrogé n'est pas rétabli.")

add('L1255-15', '''
<p>Une entreprise autre que celle mentionnée à l'article L. 1255-14 est punie de 3 750 € d'amende si elle conclut un contrat de travail en portage salarial sans remplir les conditions d'exercice de cette activité prévues aux articles L. 1254-24 à L. 1254-27.</p>
''',
    "Réécriture à droit constant : l'entreprise sanctionnée est le sujet de la phrase et la condition de l'infraction est formulée directement. Le champ des entreprises visées, la plage d'articles et l'amende sont maintenus ; aucune réforme de fond.",
    "Maintien de l'amende de 3 750 € et du renvoi à L. 1255-14. Les articles L. 1254-24 à L. 1254-27 ont été lus : dans le corpus, L. 1254-27 exige depuis le 28 mai 2026 l'obtention préalable de la garantie financière. Le renvoi existant est conservé sans ajouter de déclaration préalable ni de peine de récidive.")

add('L1255-16', '''
<p>L'entreprise cliente est punie de 3 750 € d'amende lorsqu'elle commet l'un des manquements suivants :<br />
1° Elle recourt à un salarié porté en dehors des cas prévus à l'article L. 1254-3 ;<br />
2° Elle ne respecte pas les interdictions de recours à un salarié porté prévues aux articles L. 1254-4 et L. 1254-5 ;<br />
3° Elle ne conclut pas avec l'entreprise de portage salarial le contrat commercial de prestation de portage salarial dans le délai prévu à l'article L. 1254-22 ;<br />
4° Elle conclut avec l'entreprise de portage salarial un contrat commercial de prestation de portage salarial qui ne comporte pas les mentions prévues à l'article L. 1254-23.<br />
En cas de récidive, les peines sont de six mois d'emprisonnement et de 7 500 € d'amende.</p>
''',
    "Réécriture à droit constant : chaque manquement est exprimé par une phrase dont l'entreprise cliente est le sujet. Les quatre branches de l'énumération et la récidive restent dans leur ordre ; aucune réforme de fond.",
    "Conservation des 1° à 4°, des cinq références distinctes à L. 1254-3, L. 1254-4, L. 1254-5, L. 1254-22 et L. 1254-23, et des peines de 3 750 €, puis six mois et 7 500 € en récidive. Le délai du contrat commercial demeure défini par renvoi.")

add('L1255-17', '''
<p>Toute personne qui méconnaît, directement ou par personne interposée, l'interdiction d'exercer l'activité de portage salarial prononcée par la juridiction en application du dernier alinéa de l'article L. 1255-14 est punie de six mois d'emprisonnement et de 6 000 € d'amende.</p>
''',
    "Réécriture à droit constant : la personne qui enfreint l'interdiction devient le sujet explicite de la phrase. L'interposition d'une personne, le fondement de l'interdiction et les deux peines sont intégralement conservés ; aucune réforme de fond.",
    "Le dernier alinéa de L. 1255-14 reste à sa place dans la proposition de cet article et prévoit toujours l'interdiction d'exercer. Maintien de six mois d'emprisonnement et de 6 000 € d'amende ; ce dernier montant ne doit pas être confondu avec les 7 500 € de récidive.")

add('L1255-18', '''
<p>Dans tous les cas prévus à la présente section, la juridiction peut, à titre de peine complémentaire, ordonner l'affichage ou la diffusion de tout ou partie de la décision, ou d'un communiqué informant le public des motifs et du dispositif de la décision, dans les conditions prévues à l'article 131-35 du code pénal, ainsi que son insertion, intégrale ou par extraits, dans les publications qu'elle désigne. L'entrepreneur de portage salarial ou l'entreprise cliente condamnée supporte les frais de ces mesures. La juridiction détermine, le cas échéant, les extraits de la décision et les termes du communiqué à afficher ou à diffuser.</p>
''',
    "Réécriture à droit constant : la longue phrase de publicité est allégée en isolant la prise en charge des frais et en explicitant de nouveau le sujet de la dernière phrase. Les choix du support, du contenu et des extraits, ainsi que l'insertion dans les publications désignées, sont maintenus ; aucune réforme de fond.",
    "Maintien de l'alternative affichage ou diffusion, de la décision intégrale ou partielle et du communiqué portant sur les motifs et le dispositif. Le renvoi à l'article 131-35 du code pénal est conservé. Aucun plafond autonome de frais n'est ajouté : cet article n'en énonce pas, contrairement à L. 1255-12 et L. 1255-13.")

add('L1261-1', '''
<p>Les dispositions du présent titre s'appliquent sous réserve, le cas échéant, des dispositions des traités, conventions ou accords régulièrement ratifiés ou approuvés et publiés. Cette réserve concerne notamment les traités instituant les communautés européennes et les actes pris par les autorités de ces communautés pour l'application de ces traités.</p>
''',
    "Réécriture à droit constant : la réserve de primauté des engagements internationaux est exprimée en deux phrases, la seconde précisant le cas des communautés européennes et de leurs actes. Aucune réforme de fond ni actualisation institutionnelle de portée incertaine.",
    "Les conditions cumulant ratification ou approbation régulière et publication sont conservées. La référence historique aux communautés européennes est celle de la source ; elle est maintenue et signalée comme terminologie à examiner dans une éventuelle coordination institutionnelle, sans substitution silencieuse par une référence à l'Union européenne.")

add('L1261-2', '''
<p>Les obligations et interdictions imposées aux entreprises françaises qui font appel à des prestataires de services s'appliquent dans les mêmes conditions lorsque ces prestataires sont des entreprises établies hors de France qui détachent du personnel sur le territoire national. Elles comprennent notamment les obligations et interdictions relatives au travail illégal mentionnées à l'article L. 8211-1. Un décret en Conseil d'Etat définit les modalités d'application de cette règle.</p>
''',
    "Réécriture à droit constant : la situation transfrontalière et l'entreprise française tenue aux obligations sont explicites, puis le travail illégal et le renvoi réglementaire font chacun l'objet d'une phrase. L'identité des conditions d'application est maintenue ; aucune réforme de fond.",
    "Maintien du renvoi à L. 8211-1, du détachement sur le territoire national et du décret en Conseil d'Etat. La règle porte sur les obligations et interdictions des entreprises françaises qui recourent aux prestataires ; elle ne crée pas une assimilation générale des prestataires étrangers aux entreprises établies en France.")

add('L1261-3', '''
<p>Au sens du présent titre, un salarié est détaché lorsqu'il travaille habituellement hors du territoire national pour le compte d'un employeur régulièrement établi et exerçant son activité hors de France et qu'il exécute, à la demande de cet employeur, son travail sur le territoire national pendant une durée limitée, dans les conditions définies aux articles L. 1262-1 et L. 1262-2.</p>
''',
    "Réécriture à droit constant : les conditions tenant à l'employeur, au lieu habituel de travail, à la demande de détachement et à sa durée sont présentées dans leur ordre logique. La définition conserve tous ses critères et renvois ; aucune réforme de fond.",
    "Maintien du caractère régulier de l'établissement de l'employeur, de son activité hors de France, du travail habituel pour son compte à l'étranger et de la durée limitée du travail en France. Les références à L. 1262-1 et L. 1262-2 ne sont pas remplacées par la seule notion de contrat de travail français.")

add('L1262-1', '''
<p>Un employeur établi hors de France peut détacher temporairement des salariés sur le territoire national si un contrat de travail le lie à chaque salarié détaché et si leur relation de travail se poursuit pendant toute la période de détachement.</p>
<p>Le détachement intervient dans l'un des cas suivants :</p>
<p>1° Pour le compte de l'employeur et sous sa direction, dans le cadre d'un contrat qu'il a conclu avec le destinataire de la prestation établi ou exerçant en France ;</p>
<p>2° Entre établissements d'une même entreprise ou entre entreprises d'un même groupe ;</p>
<p>3° Pour le compte de l'employeur, sans contrat entre celui-ci et un destinataire.</p>
''',
    "Réécriture à droit constant : les conditions de maintien du lien contractuel et les trois cas de détachement sont exprimés plus directement. Le nombre, l'ordre et la portée des subdivisions sont préservés ; aucune réforme de fond.",
    "Les 1°, 2° et 3° sont conservés, notamment parce que L. 1262-2-1 et L. 1262-4-4 les visent séparément. La direction de l'employeur n'est mentionnée qu'au 1°, comme dans la source. Le 1° conserve l'alternative entre un destinataire établi en France et un destinataire y exerçant son activité.")

add('L1262-2', '''
<p>Une entreprise exerçant une activité de travail temporaire et établie hors du territoire national peut détacher temporairement des salariés si un contrat de travail la lie à chaque salarié détaché et si leur relation de travail se poursuit pendant la période de détachement. Cette mise à disposition intervient :<br />
1° Auprès d'une entreprise utilisatrice établie sur le territoire national ;<br />
2° Auprès d'une entreprise utilisatrice établie hors du territoire national qui exerce temporairement une activité sur le territoire national.</p>
<p>Les dispositions relatives au travail temporaire du chapitre Ier du titre V du présent livre s'appliquent aux salariés détachés dans le cadre d'une mise à disposition au titre du travail temporaire. Toutefois, les articles L. 1251-32 et L. 1251-33 ne s'appliquent pas aux salariés titulaires d'un contrat de travail à durée indéterminée dans leur pays d'origine.</p>
''',
    "Réécriture à droit constant : les conditions communes du détachement précèdent les deux lieux d'établissement de l'entreprise utilisatrice ; l'exception propre aux titulaires d'un CDI dans leur pays d'origine est isolée dans une phrase. Les deux alinéas et les 1° et 2° restent en place, sans réforme de fond.",
    "Maintien du chapitre Ier du titre V et de l'exception limitée à L. 1251-32 et L. 1251-33 pour les CDI du pays d'origine. La note source fixe l'entrée en vigueur historique au 30 juillet 2020, selon les I et II de l'article 7 de l'ordonnance n° 2019-116 du 20 février 2019, et réserve aux salariés roulants des entreprises de transport routier visées à L. 1321-1 du code des transports la rédaction antérieure à cette ordonnance. Cette réserve reste attachée à l'article ; ne pas l'étendre ni la supprimer sans coordination avec les règles du transport routier. La réforme des nouveaux CDI français n'est pas transposée aux contrats du pays d'origine.")

add('L1262-2-1', '''
<p>I.-Avant le détachement, l'employeur qui détache un ou plusieurs salariés dans les conditions prévues aux 1° et 2° de l'article L. 1262-1 et à l'article L. 1262-2 adresse une déclaration à l'inspection du travail du lieu où débute la prestation.</p>
<p>II.-L'employeur mentionné au I désigne un représentant de l'entreprise sur le territoire national. Ce représentant assure, pendant la durée de la prestation, la liaison avec les agents mentionnés à l'article L. 8271-1-2.</p>
<p>III.-Le respect des obligations prévues aux I et II ne fait pas présumer que le détachement est régulier.</p>
<p>IV.-L'entreprise utilisatrice établie hors du territoire national mentionnée au 2° de l'article L. 1262-2 qui recourt, pour exercer son activité sur le territoire national, à des salariés détachés mis à disposition par une entreprise de travail temporaire également établie hors du territoire national informe cette dernière, qui emploie les salariés détachés, avant le détachement, du détachement de ces salariés sur le territoire national et des règles qui leur sont applicables. La liste de ces règles est arrêtée par le ministre chargé du travail.<br />
En cas de contrôle, l'entreprise utilisatrice justifie par tout moyen auprès des services de l'inspection du travail qu'elle a respecté les dispositions du premier alinéa du présent IV.</p>
<p>V.-L'entreprise utilisatrice établie sur le territoire national mentionnée au 1° de l'article L. 1262-2 qui recourt à des salariés détachés mis à disposition par une entreprise exerçant une activité de travail temporaire dans les conditions prévues à l'article L. 1262-2 informe l'employeur de ces salariés des règles de rémunération qui leur sont applicables pendant leur mise à disposition sur le territoire national.</p>
''',
    "Réécriture à droit constant : l'antériorité de la déclaration est placée en tête, les missions du représentant et la fixation de la liste des règles font l'objet de phrases autonomes, et les destinataires de l'information sont clarifiés. Les I à V et les deux alinéas du IV sont préservés ; aucune réforme de fond.",
    "Les obligations des I et II restent limitées aux 1° et 2° de L. 1262-1 et à L. 1262-2 ; le 3° de L. 1262-1 n'est pas ajouté. Les IV et V distinguent toujours l'entreprise utilisatrice étrangère de celle établie en France. Le renvoi au premier alinéa du IV est explicité sans déplacement. La note source conserve le 30 juillet 2020 comme date historique d'entrée en vigueur et, selon les I et II de l'article 7 de l'ordonnance n° 2019-116 du 20 février 2019, réserve la rédaction antérieure aux salariés roulants des entreprises de transport routier visées à L. 1321-1 du code des transports. Aucune suppression de cette réserve ni fusion avec un guichet d'embauche n'est proposée.")

add('L1262-2-2', '''
<p>Un décret en Conseil d'Etat, pris après avis de la Commission nationale de l'informatique et des libertés, fixe les conditions dans lesquelles les employeurs mentionnés aux articles L. 1262-1 et L. 1262-2 doivent transmettre par voie dématérialisée la déclaration prévue au I de l'article L. 1262-2-1 du présent code ou l'attestation prévue à l'article L. 1331-1-1 du code des transports.</p>
''',
    "Réécriture à droit constant : le décret devient le sujet de la phrase et les deux documents soumis à transmission dématérialisée sont identifiés directement. L'avis préalable de la CNIL et les champs des deux codes sont maintenus ; aucune réforme de fond.",
    "Maintien des renvois à L. 1262-1, L. 1262-2, au I de L. 1262-2-1 et à L. 1331-1-1 du code des transports. La note source rattache l'entrée en vigueur au 1er janvier 2023, en application de l'article 5 de l'ordonnance n° 2022-1293 du 5 octobre 2022 ; cette date historique ne date aucune réforme nouvelle. Le code des transports est hors du périmètre de réécriture et n'est pas modifié.")

add('L1262-3', '''
<p>Un employeur ne peut invoquer les dispositions applicables au détachement de salariés si, dans l'Etat où il est établi, il exerce uniquement des activités de gestion interne ou administrative, ou si son activité sur le territoire national présente un caractère habituel, stable et continu. Il ne peut notamment invoquer ces dispositions lorsque son activité comprend la recherche et la prospection d'une clientèle ou le recrutement de salariés sur ce territoire.</p>
<p>Dans ces situations, l'employeur est soumis aux dispositions du code du travail applicables aux entreprises établies sur le territoire national.</p>
''',
    "Réécriture à droit constant : les deux motifs alternatifs d'exclusion du détachement sont formulés plus directement et la conséquence juridique reste dans un second alinéa. Les critères et exemples de la source sont conservés ; aucune réforme de fond.",
    "Le caractère habituel, stable et continu demeure cumulatif ; il n'est pas remplacé par un critère isolé. Le cas de l'activité uniquement interne ou administrative dans l'Etat d'établissement reste alternatif. L'exemple de recherche et prospection de clientèle ou de recrutement en France est conservé sans trancher davantage son articulation avec les critères généraux.")

add('L1262-4', '''
<p>I.-L'employeur qui détache temporairement un salarié sur le territoire national lui garantit, dans les matières énumérées ci-dessous, l'égalité de traitement avec les salariés employés par les entreprises de la même branche d'activité établies sur ce territoire. A cette fin, il respecte les dispositions légales et les stipulations conventionnelles applicables à ces salariés en matière de législation du travail :<br />
1° Libertés individuelles et collectives dans la relation de travail ;<br />
2° Discriminations et égalité professionnelle entre les femmes et les hommes ;<br />
3° Protection de la maternité, congés de maternité et de paternité et d'accueil de l'enfant, congés pour événements familiaux ;<br />
4° Conditions de mise à disposition et garanties dues aux salariés par les entreprises exerçant une activité de travail temporaire ;<br />
5° Exercice du droit de grève ;<br />
6° Durée du travail, repos compensateurs, jours fériés, congés annuels payés, durée du travail et travail de nuit des jeunes travailleurs ;<br />
7° Conditions d'assujettissement aux caisses de congés et intempéries ;<br />
8° Rémunération au sens de l'article L. 3221-3, paiement du salaire, y compris les majorations pour les heures supplémentaires ;<br />
9° Règles relatives à la santé et à la sécurité au travail, âge d'admission au travail, emploi des enfants ;<br />
10° Travail illégal ;<br />
11° Remboursements des frais professionnels supportés par le salarié détaché lors de sa mission, correspondant à des charges de caractère spécial inhérentes à sa fonction ou à son emploi, en matière de transport, de repas et d'hébergement.</p>
<p>II.-Lorsque le détachement temporaire d'un salarié sur le territoire national dure plus de douze mois, l'employeur est soumis, à compter du treizième mois, aux dispositions du code du travail applicables aux entreprises établies sur ce territoire. Sont exceptées les dispositions du chapitre I, des sections 1, 2 et 5 du chapitre II, des chapitres III et IV du titre II, des titres III, IV et VII du livre II de la première partie du code du travail.</p>
<p>Lorsqu'un salarié détaché est remplacé par un autre salarié détaché sur le même poste de travail, la durée de détachement de douze mois mentionnée à l'alinéa précédent est atteinte dès que les durées cumulées de détachement des salariés qui se succèdent sur ce poste sont égales à douze mois.</p>
<p>Lorsque l'exécution de la prestation le justifie, l'employeur mentionné au premier alinéa du II bénéficie d'une prolongation de l'application des règles relevant des matières énumérées au I, pour une durée maximale de six mois supplémentaires. Pour en bénéficier, il adresse une déclaration motivée à l'autorité administrative avant l'expiration du délai de douze mois, dans les conditions fixées par décret en Conseil d'Etat.</p>
''',
    "Réécriture à droit constant : le principe d'égalité et son contenu sont séparés, les frais professionnels sont définis dans un ordre plus lisible, et les conditions de la prolongation sont exprimées en deux phrases. Les onze matières du I, les trois alinéas du II, les exclusions et les durées sont conservés ; aucune réforme de fond.",
    "Maintien de L. 3221-3, des onze matières et de tous les niveaux des exclusions du II : chapitre I, sections 1, 2 et 5 du chapitre II, chapitres III et IV du titre II, titres III, IV et VII du livre II de la première partie. Douze mois, application dès le treizième mois, cumul des remplacements sur le même poste et prorogation maximale de six mois sont inchangés. La note source fixe l'entrée en vigueur au 30 juillet 2020 et impose, pour les détachements en cours à cette date, de compter les périodes déjà accomplies, conformément aux I et II de l'article 7 de l'ordonnance n° 2019-116 du 20 février 2019. Elle renvoie aussi aux modalités du II de cet article 7 et du III de l'article 25 de la loi n° 2021-1308 du 8 octobre 2021 ; ces règles historiques d'application restent à conserver et à articuler avec les régimes concernés. Le seuil de quarante heures prévu pour les nouveaux contrats ne devient pas ici un seuil propre à tout détachement : L. 1262-4 continue de renvoyer aux règles applicables avec leurs champs et transitions.")

add('L1262-4-1', '''
<p>I.-Le donneur d'ordre ou le maître d'ouvrage qui conclut un contrat avec un prestataire de services détachant des salariés dans les conditions prévues aux articles L. 1262-1 et L. 1262-2 vérifie auprès de ce prestataire, avant le début du détachement, qu'il a rempli les obligations prévues aux I et II de l'article L. 1262-2-1.</p>
<p>Si son cocontractant ne lui a pas remis une copie de la déclaration prévue au I de l'article L. 1262-2-1, le maître d'ouvrage ou le donneur d'ordre adresse une déclaration à l'inspection du travail du lieu où débute la prestation dans les quarante-huit heures suivant le début du détachement. Un décret détermine les informations à faire figurer dans cette déclaration.</p>
<p>Un décret en Conseil d'Etat, pris après avis de la Commission nationale de l'informatique et des libertés, fixe les conditions dans lesquelles le maître d'ouvrage ou le donneur d'ordre doit transmettre par voie dématérialisée la déclaration prévue au deuxième alinéa du présent I.</p>
<p>II.-Avant le début du détachement, le maître d'ouvrage vérifie que les sous-traitants et les entreprises de travail temporaire suivants ont rempli l'obligation prévue au I de l'article L. 1262-2-1 lorsqu'ils détachent des salariés dans les conditions prévues aux articles L. 1262-1 et L. 1262-2 : les sous-traitants directs ou indirects de ses cocontractants qu'il accepte en application de l'article 3 de la loi n° 75-1334 du 31 décembre 1975 relative à la sous-traitance, ainsi que les entreprises exerçant une activité de travail temporaire avec lesquelles l'un de ces sous-traitants ou l'un de ces cocontractants a contracté. Cette vérification porte sur chacun de ces sous-traitants et chacune de ces entreprises.</p>
<p>III.-Lorsqu'il conclut un contrat avec un prestataire de services détachant des salariés dans les conditions prévues aux articles L. 1262-1 et L. 1262-2, le donneur d'ordre ou le maître d'ouvrage vérifie que son cocontractant a payé, le cas échéant, les sommes dues au titre des amendes prévues aux articles L. 1263-6, L. 1264-1, L. 1264-2 et L. 8115-1.</p>
''',
    "Réécriture à droit constant : les pronoms ambigus sont remplacés par leurs sujets, le délai de déclaration est rapproché de l'obligation correspondante et le II énonce plus clairement les deux catégories d'entreprises à vérifier. Les I à III et leurs alinéas sont maintenus ; aucune réforme de fond.",
    "Conserver les quarante-huit heures après le début du détachement, distinctes des vérifications préalables des I et II et du contrôle des amendes lors de la conclusion du contrat au III. Le II ne vise que le maître d'ouvrage et la seule obligation du I de L. 1262-2-1 ; il ne lui étend pas le II de cet article. Maintien de l'acceptation selon l'article 3 de la loi n° 75-1334 du 31 décembre 1975, du deuxième alinéa du I pour la dématérialisation et des quatre références d'amendes. L'exception personnelle de L. 1262-4-2 reste applicable.")

add('L1262-4-2', '''
<p>Le particulier qui conclut un contrat avec un prestataire de services établi hors de France pour son usage personnel, celui de son conjoint, de son partenaire lié par un pacte civil de solidarité, de son concubin ou de ses ascendants ou descendants n'est pas soumis à l'article L. 1262-4-1.</p>
''',
    "Réécriture à droit constant : le particulier bénéficiant de l'exception devient le sujet de la phrase. Le caractère étranger du prestataire, les usages couverts et la totalité des bénéficiaires sont préservés ; aucune réforme de fond.",
    "L'exception reste limitée à l'article L. 1262-4-1. Sont conservés l'usage personnel et ceux du conjoint, du partenaire de PACS, du concubin, des ascendants et des descendants. Ne pas confondre cette condition de prestataire établi hors de France avec la rédaction distincte de l'exception figurant à L. 1262-4-3.")

add('L1262-4-3', '''
<div>Lorsqu'un agent de contrôle mentionné à l'article L. 8271-1-2 l'informe par écrit du non-paiement total ou partiel du salaire minimum légal ou conventionnel dû à un salarié détaché au sens de l'article L. 1261-3 par son cocontractant, par un sous-traitant direct ou indirect ou par un cocontractant d'un sous-traitant, le maître d'ouvrage ou le donneur d'ordre enjoint aussitôt par écrit à ce sous-traitant ou à ce cocontractant, ainsi qu'au donneur d'ordre immédiat de ce dernier, de faire cesser sans délai cette situation.<br />
Si la situation signalée n'est pas régularisée dans le délai fixé par décret et si le maître d'ouvrage ou le donneur d'ordre ne dénonce pas le contrat de prestation de service, il est tenu, solidairement avec l'employeur du salarié, de payer les rémunérations, indemnités et charges dues. Un décret en Conseil d'Etat fixe les conditions de cette obligation.<br />
Le particulier qui conclut un contrat avec une entreprise pour son usage personnel, celui de son conjoint, de son partenaire auquel il est lié par un pacte civil de solidarité, de son concubin ou de ses ascendants ou descendants n'est pas soumis au présent article.</div>
''',
    "Réécriture à droit constant : le signalement déclencheur est placé en tête, les deux conditions de la solidarité sont réunies dans une proposition explicite, et le renvoi au décret en Conseil d'Etat est isolé. L'injonction immédiate, tous ses destinataires, les sommes dues et l'exception personnelle restent conservés ; aucune réforme de fond.",
    "Maintien de L. 8271-1-2 et de L. 1261-3. Le signalement et l'injonction restent tous deux écrits ; l'injonction est immédiate et exige une cessation sans délai. Le délai de régularisation est fixé par décret, sans ajout d'une durée chiffrée. La solidarité reste subordonnée à l'absence de régularisation et à l'absence de dénonciation du contrat. L'exception du dernier alinéa ne reçoit pas une condition nouvelle d'établissement de l'entreprise hors de France.")

add('L1262-4-4', '''
<p>Tout accident du travail dont est victime un salarié détaché est déclaré à l'inspection du travail du lieu de l'accident.</p>
<p>La déclaration incombe aux personnes suivantes, dans un délai et selon des modalités fixés par décret en Conseil d'Etat :</p>
<p>1° A l'employeur, si le salarié est détaché selon les modalités prévues au 3° de l'article L. 1262-1 ;</p>
<p>2° Au donneur d'ordre ou au maître d'ouvrage cocontractant du prestataire de services qui détache des salariés dans les conditions prévues aux 1° et 2° de l'article L. 1262-1 ou à l'article L. 1262-2.</p>
''',
    "Réécriture à droit constant : le destinataire de la déclaration et les personnes qui en sont responsables sont identifiés plus directement. La répartition selon les modalités de détachement, les quatre alinéas et les subdivisions sont maintenus ; aucune réforme de fond.",
    "Maintien de l'inspection du travail du lieu de l'accident, distincte de celle du lieu où commence la prestation. Le 1° renvoie au seul 3° de L. 1262-1 ; le 2° vise les 1° et 2° de L. 1262-1 ou L. 1262-2. Le délai et les modalités restent renvoyés à un décret en Conseil d'Etat, sans délai inventé.")


sources = json.loads(Path('source.json').read_text())
assert len(sources) == 24
assert set(drafts) == {s['number'] for s in sources}
answer = []
for source in sources:
    answer.append({
        **{key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')},
        **drafts[source['number']],
        'status': 'rewrite_draft',
    })
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
