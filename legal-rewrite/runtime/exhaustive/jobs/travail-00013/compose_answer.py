import json
from pathlib import Path


drafts = {}


def add(number, proposed_xml, reason, review_notes):
    assert number not in drafts
    drafts[number] = (proposed_xml, reason, review_notes)


add(
    "L1251-53",
    """<p>Un décret en Conseil d'État fixe les conditions d'application du présent paragraphe.</p>""",
    "Réécriture à droit constant : le décret en Conseil d'État devient le sujet de la phrase, qui énonce directement sa fonction. Aucune réforme de fond.",
    "Le renvoi reste limité au présent paragraphe relatif à la garantie financière et à la défaillance de l'entreprise de travail temporaire. Le recours à un décret en Conseil d'État est conservé.",
)

add(
    "L1251-54",
    """<p>L'effectif d'une entreprise de travail temporaire est calculé en prenant en compte :</p>
<p>1° Les salariés permanents de cette entreprise, décomptés selon l'article L. 1111-2 ;</p>
<p>2° Les salariés temporaires liés à cette entreprise par des contrats de mission pendant au moins trois mois au total au cours de la dernière année civile.</p>""",
    "Réécriture à droit constant : la règle de calcul est formulée directement et la durée cumulée des missions est explicitée. Les deux catégories de salariés restent séparées et numérotées. Aucune réforme de fond.",
    "Trois alinéas et les 1° et 2° conservés. Le seuil est d'au moins trois mois cumulés, sans exigence nouvelle de continuité, sur la dernière année civile et non sur douze mois glissants. Le renvoi à L. 1111-2 reste attaché aux salariés permanents.",
)

add(
    "L1251-55",
    """<p>Lorsqu'une disposition légale subordonne son application à un salarié temporaire à une condition d'ancienneté dans l'entreprise de travail temporaire, cette ancienneté est calculée en additionnant les périodes pendant lesquelles le salarié a été lié à cette entreprise par des contrats de mission.</p>""",
    "Réécriture à droit constant : la condition d'application est exposée avant la méthode de calcul et le lien entre chaque période et les contrats de mission est explicite. Aucune réforme de fond.",
    "Le cumul porte sur les périodes de contrats de mission, sans période de référence ni condition de continuité ajoutée. Le décompte particulier des périodes avec ou sans mission sous CDI intérimaire demeure régi, dans les cas qu'ils visent, par L. 1251-58-7 et L. 1251-58-8.",
)

add(
    "L1251-56",
    """<p>Pour l'application du 1° de l'article L. 6322-63, la durée minimale de présence d'un salarié temporaire dans l'entreprise de travail temporaire est calculée en additionnant les périodes pendant lesquelles des contrats de mission l'ont lié à son employeur.</p>""",
    "Réécriture à droit constant : le salarié concerné et le calcul par addition des périodes de contrats sont énoncés directement. Le renvoi source est conservé ; aucune réforme de fond.",
    "Anomalie de renvoi à contrôler : L. 6322-63 est absent du corpus public travail.json fourni. Le 1° de cet article est néanmoins conservé à l'identique dans son identification ; aucun article de remplacement n'est inventé. Coordonner toute correction ultérieure avec L. 1251-58-7, qui vise le même 1° mais retient les périodes avec ou sans mission sous CDI.",
)

add(
    "L1251-57",
    """<p>Le principe d'exclusivité prévu à l'article L. 1251-2 demeure applicable. Sont assimilées à des missions les périodes que les salariés temporaires consacrent :</p>
<p>1° À des stages de formation, à des bilans de compétences ou à des actions de validation des acquis de l'expérience. Ces périodes sont accomplies soit à l'initiative de l'employeur, dans le cadre du plan de formation de l'entreprise, du contrat d'apprentissage ou du contrat de professionnalisation, soit à l'initiative du salarié, dans le cadre d'un congé spécifique mentionné à l'article L. 6323-17-1 ou d'un congé de bilan de compétences ;</p>
<p>2° À des actions de formation liées à leur activité professionnelle, dans les conditions fixées par une convention ou un accord collectif étendu, ou par une convention ou un accord d'entreprise ou d'établissement.</p>""",
    "Réécriture à droit constant : le maintien du principe d'exclusivité est isolé dans une phrase ; les activités assimilées et les deux initiatives possibles sont présentées dans leurs subdivisions d'origine. Aucune réforme de fond des formations ni des accords habilités.",
    "Les trois alinéas et les 1° et 2° sont maintenus. L. 6323-17-1 a été vérifié dans le corpus : il prévoit un congé spécifique pour le projet de transition professionnelle. Les mentions sources du plan de formation et du congé de bilan de compétences sont conservées ; leur articulation avec les dispositifs actuels de formation appelle un contrôle de coordination, sans remplacement silencieux. Le caractère étendu reste exigé pour la convention ou l'accord collectif du premier membre du 2°, sans ajout de cette exigence aux accords d'entreprise ou d'établissement.",
)

add(
    "L1251-58",
    """<p>Le livre III de la deuxième partie fixe les règles de représentation du personnel propres au travail temporaire.</p>
<p>Le livre III de la troisième partie fixe les règles de participation des salariés aux fruits de l'expansion des entreprises propres au travail temporaire.</p>""",
    "Réécriture à droit constant : chaque livre devient le sujet de la phrase qui indique la matière qu'il régit. Les deux renvois restent dans deux alinéas distincts. Aucune réforme de fond.",
    "Conserver la distinction entre le livre III de la deuxième partie, pour la représentation du personnel, et le livre III de la troisième partie, pour la participation. Aucun régime nouveau n'est créé par ces renvois.",
)

add(
    "L1251-58-1",
    """<p>Pour l'exécution de missions successives, une entreprise de travail temporaire peut conclure avec un salarié un contrat de travail à durée indéterminée. Chaque mission exige :<br /><br />1° La conclusion d'un contrat de mise à disposition entre l'entreprise de travail temporaire et le client utilisateur, dénommé « entreprise utilisatrice » ;<br /><br />2° L'établissement d'une lettre de mission par l'entreprise de travail temporaire.</p>""",
    "Réécriture à droit constant : l'objet du CDI est placé en tête et les deux formalités propres à chaque mission sont énoncées comme des exigences distinctes. Aucune réforme de fond du CDI intérimaire.",
    "La conclusion du CDI demeure facultative ; le contrat de mise à disposition et l'établissement d'une lettre sont exigés pour chaque mission. Les 1° et 2° et leur ordre sont maintenus. La remise de la lettre au salarié est traitée au 8° de L. 1251-58-2. Les conditions générales d'essai du CDI se lisent avec cet article et L. 1221-19 à L. 1221-23, selon leur transition.",
)

add(
    "L1251-58-2",
    """<p>Les dispositions du code du travail relatives au contrat à durée indéterminée s'appliquent au contrat mentionné à l'article L. 1251-58-1, sous réserve des dispositions de la présente section.<br /><br />Ce contrat peut prévoir des périodes sans exécution de mission. Pour le calcul des droits à congés payés et de l'ancienneté, ces périodes sont assimilées à du temps de travail effectif.<br /><br />Le contrat doit être écrit et comporter notamment les mentions suivantes :<br /><br />1° L'identité des parties ;<br /><br />2° Le cas échéant, les conditions relatives à la durée du travail, notamment au travail de nuit ;<br /><br />3° Les horaires pendant lesquels le salarié doit être joignable au cours des périodes sans exécution de mission ;<br /><br />4° Le périmètre de mobilité dans lequel les missions sont effectuées. Ce périmètre tient compte de la spécificité des emplois et de la nature des tâches à accomplir, dans le respect de la vie personnelle et familiale du salarié ;<br /><br />5° La description des emplois correspondant aux qualifications du salarié ;<br /><br />6° Le cas échéant, la durée de la période d'essai ;<br /><br />7° Le montant de la rémunération mensuelle minimale garantie ;<br /><br />8° L'obligation de remettre au salarié une lettre de mission pour chacune des missions qu'il effectue.</p>""",
    "Réécriture à droit constant : les règles du CDI applicables, la portée de l'assimilation des périodes sans mission et l'obligation d'écrit sont formulées directement. La clause de mobilité est décomposée en deux phrases dans le même 4°. Aucune modification autonome du régime spécial.",
    "Les huit mentions, leur numérotation et les réserves « le cas échéant » des 2° et 6° sont maintenues. La liste reste non exhaustive. L'assimilation des périodes sans mission reste limitée ici aux congés payés et à l'ancienneté. Le 6° ne fixe pas de durée d'essai : par le renvoi général au CDI, coordonner avec L. 1221-19, L. 1221-21 à L. 1221-23 et L. 1221-25 pour les nouveaux CDI (trois mois au plus, sans renouvellement, sous réserve des durées plus courtes) et préserver les contrats antérieurs et la prévenance. Ne pas appliquer l'essai de trois mois aux contrats de mission ordinaires ; L. 1251-58-4 écarte leurs articles L. 1251-14 et L. 1251-15 pour ce CDI.",
)

add(
    "L1251-58-3",
    """<p>Le contrat mentionné à l'article L. 1251-58-1, qui lie l'entreprise de travail temporaire au salarié, doit garantir le versement d'une rémunération mensuelle minimale. Son montant est au moins égal au produit du montant du salaire minimum de croissance fixé en application des articles L. 3231-2 à L. 3231-12 par le nombre d'heures correspondant, pour le mois considéré, à la durée légale hebdomadaire applicable au contrat. Pour apprécier cette garantie, il est tenu compte, le cas échéant, des rémunérations des missions versées au cours de ce même mois.</p>""",
    "La formule de garantie est réécrite en trois phrases dans le même alinéa : obligation contractuelle, calcul du minimum et prise en compte des rémunérations de mission. Coordination de fond avec la réforme de L. 3121-27 : la durée légale utilisée est celle applicable au contrat, sans généraliser la référence nouvelle aux contrats antérieurs. Aucun taux de SMIC n'est modifié.",
    "Le produit SMIC × nombre d'heures du mois et l'imputation éventuelle des rémunérations des missions sont conservés. La rédaction proposée de L. 3121-27 consultée dans le corpus retient quarante heures pour les nouveaux contrats à temps complet et trente-cinq pour les contrats antérieurs : la même transition doit régir cette garantie, sans minorer une garantie contractuelle ou conventionnelle plus favorable. Le calcul de la garantie ne relève pas, à lui seul, les seuils de décompte des heures supplémentaires sur une période supérieure à la semaine de L. 3121-41 et L. 3121-44. Arrêter une entrée en vigueur commune dans la loi de réforme, sans inventer de date ni de montant mensuel.",
)

add(
    "L1251-58-4",
    """<p>Les articles L. 1251-5 à L. 1251-63 s'appliquent aux missions du salarié lié à l'entreprise de travail temporaire par un contrat de travail à durée indéterminée, sous réserve des adaptations de la présente section. Toutefois, les articles L. 1251-14, L. 1251-15, L. 1251-19, L. 1251-26 à L. 1251-28, L. 1251-32, L. 1251-33 et L. 1251-36 ne s'appliquent pas à ces missions.</p>""",
    "Réécriture à droit constant : le champ des règles applicables est exposé avant la liste complète des exclusions, placée dans une seconde phrase du même alinéa. Aucune réforme de fond ni nouvelle exclusion.",
    "Plage L. 1251-5 à L. 1251-63 et toutes les exclusions conservées, y compris l'intégralité de L. 1251-26 à L. 1251-28. Lire ces règles avec L. 1251-58-5 pour la lettre de mission et L. 1251-58-6 pour la durée prévue à L. 1251-12-1 ; l'exclusion de cet article n'est pas ajoutée à la liste. L. 1251-60 reste dans la plage applicable aux utilisateurs publics.",
)

add(
    "L1251-58-5",
    """<p>Lorsque les articles L. 1251-5, L. 1251-9, L. 1251-11, L. 1251-13, L. 1251-16, L. 1251-17, L. 1251-29, L. 1251-30, L. 1251-31, L. 1251-34, L. 1251-35, L. 1251-41 et L. 1251-60 s'appliquent au contrat à durée indéterminée conclu entre une entreprise de travail temporaire et un salarié, leurs références au « contrat de mission » s'entendent comme des références à la « lettre de mission ».</p>""",
    "Réécriture à droit constant : la règle de substitution de termes devient une règle d'interprétation directement applicable au CDI intérimaire. Le texte constitue la disposition intégrale, sans instruction d'amendement. Aucune réforme de fond.",
    "Les treize articles visés sont conservés dans leur ordre, notamment L. 1251-41 et L. 1251-60. L'adaptation du vocabulaire est limitée à cette liste et à l'application au CDI intérimaire ; elle ne transforme pas les lettres de mission en contrats de travail distincts et n'étend pas les exclusions de L. 1251-58-4.",
)

add(
    "L1251-58-6",
    """<p>La limite de durée totale du contrat de mission prévue à l'article L. 1251-12-1 ne s'applique pas aux missions du salarié lié à l'entreprise de travail temporaire par un contrat à durée indéterminée.</p>""",
    "Réécriture à droit constant : l'objet de l'inapplicabilité est désigné comme la limite de durée et rattaché explicitement aux missions du salarié en CDI intérimaire. Aucune réforme de fond.",
    "Le renvoi reste exclusivement L. 1251-12-1. Ne pas en déduire une exclusion de L. 1251-12, des conditions de recours aux missions ou des règles propres aux personnes publiques de L. 1251-60, qui demeure visé par L. 1251-58-4 et L. 1251-58-5. Aucun ancien plafond n'est réintroduit.",
)

add(
    "L1251-58-7",
    """<p>Lorsqu'un salarié est lié à une entreprise de travail temporaire par un contrat à durée indéterminée, sa durée minimale de présence dans l'entreprise, pour l'application du 1° de l'article L. 6322-63, est calculée en additionnant les périodes avec ou sans exécution d'une mission.</p>""",
    "Réécriture à droit constant : le CDI est présenté comme la condition du calcul qui inclut tant les périodes de mission que celles sans mission. Aucune réforme de fond.",
    "Le renvoi au 1° de L. 6322-63 est conservé bien que cet article soit absent du corpus public travail.json fourni : anomalie de renvoi à contrôler, sans substitution inventée. Toute correction devra être coordonnée avec L. 1251-56. La différence entre le cumul des missions de ce dernier et le cumul avec ou sans mission sous CDI est maintenue.",
)

add(
    "L1251-58-8",
    """<p>Pour le salarié lié à une entreprise de travail temporaire par un contrat à durée indéterminée, la durée passée dans l'entreprise au sens de l'article L. 2314-20 est calculée en additionnant les périodes avec ou sans exécution d'une mission.</p>""",
    "Réécriture à droit constant : le bénéficiaire de la règle est identifié en tête et les deux types de périodes compris dans le calcul sont explicités. Aucune réforme de fond des conditions électorales.",
    "Renvoi à L. 2314-20 vérifié dans le corpus : cet article porte sur l'ancienneté pour l'électorat et l'éligibilité des salariés temporaires. Le présent texte adapte les périodes comptabilisées sous CDI sans modifier les seuils, les périodes de référence ni la règle particulière de création d'entreprise ou d'ouverture d'établissement de L. 2314-20.",
)

add(
    "L1251-59",
    """<p>Les organisations syndicales représentatives peuvent, en faveur d'un salarié, exercer en justice toutes les actions qui résultent de l'application du présent chapitre. Elles n'ont pas à justifier d'un mandat de ce salarié.</p>
<p>Le salarié est averti dans les conditions fixées par voie réglementaire. L'exercice de l'action est subordonné à l'absence d'opposition du salarié dans un délai de quinze jours à compter de la date à laquelle l'organisation syndicale lui a notifié son intention.</p>
<p>Le salarié peut, à tout moment, intervenir dans l'instance engagée par l'organisation syndicale et y mettre un terme.</p>""",
    "Réécriture à droit constant : la dispense de mandat est isolée, puis la condition d'absence d'opposition est rattachée à l'exercice de l'action. Les pouvoirs conservés par le salarié restent dans le troisième alinéa. Aucune réforme de fond du recours au juge.",
    "Trois alinéas conservés. Le délai reste de quinze jours à compter de la notification de l'intention syndicale, et non de la saisine de la juridiction. Le champ demeure l'ensemble du présent chapitre et les seules organisations représentatives ; le salarié conserve le droit d'intervenir et de mettre fin à l'instance à tout moment.",
)

add(
    "L1251-60",
    """<p>Une personne morale de droit public ne peut faire appel aux salariés d'une entreprise de travail temporaire que pour exécuter des tâches non durables, appelées missions, dans l'un des cas suivants :</p>
<p>1° Remplacement momentané d'un agent en raison d'un congé de maladie, de maternité, parental ou de présence parentale ; d'un passage provisoire à temps partiel ; de sa participation à des activités dans le cadre d'une réserve opérationnelle, sanitaire, civile ou autre ; de l'accomplissement du service civil ou national ; du rappel ou du maintien sous les drapeaux ;</p>
<p>2° Vacance temporaire d'un emploi qui ne peut pas être pourvu immédiatement dans les conditions prévues par la loi n° 84-16 du 11 janvier 1984 portant dispositions statutaires relatives à la fonction publique de l'État, la loi n° 84-53 du 26 janvier 1984 portant dispositions statutaires relatives à la fonction publique territoriale et la loi n° 86-33 du 9 janvier 1986 portant dispositions statutaires relatives à la fonction publique hospitalière et par le chapitre II du titre V du livre Ier de la sixième partie du code de la santé publique ;</p>
<p>3° Accroissement temporaire de l'activité ;</p>
<p>4° Besoin occasionnel ou saisonnier au sens du 3° de l'article L. 1242-2.</p>
<p>Pour les contrats conclus au titre des 1°, 3° et 4°, la durée totale du contrat de mission est limitée à dix-huit mois. Ce plafond est ramené à neuf mois lorsque le contrat a pour objet la réalisation de travaux urgents nécessités par des mesures de sécurité. Il est porté à vingt-quatre mois lorsque la mission est exécutée à l'étranger.</p>
<p>Pour les contrats conclus au titre du 2°, la durée totale du contrat de mission est limitée à douze mois. Ce plafond est ramené à neuf mois lorsque le contrat est conclu dans l'attente de la prise de fonctions d'un agent.</p>
<p>Le contrat de mission peut être renouvelé une seule fois, pour une durée déterminée. La durée de ce renouvellement, ajoutée à celle du contrat initial, ne peut dépasser les durées prévues à l'alinéa précédent.</p>""",
    "Réécriture à droit constant : le recours par l'utilisateur public est énoncé comme une faculté strictement limitée ; les causes de remplacement sont séparées par des points-virgules et les plafonds sont formulés directement. Les huit alinéas, les quatre cas et le renvoi final restent à leur place. Aucune réforme de fond des missions publiques.",
    "Plafonds conservés : dix-huit mois pour les 1°, 3° et 4°, neuf mois pour les travaux urgents de sécurité, vingt-quatre mois à l'étranger ; douze mois pour le 2°, ramenés à neuf mois dans l'attente d'un agent. Un seul renouvellement. Ambiguïté préexistante conservée : le dernier alinéa renvoie à « l'alinéa précédent », qui ne traite que des plafonds de douze et neuf mois du 2°, alors que la phrase de renouvellement vise le contrat de mission sans autre restriction. Une clarification exige une coordination expresse ; aucune extension silencieuse du renvoi aux deux alinéas n'est faite. Les références aux trois lois statutaires historiques sont conservées ; contrôler leur articulation avec le code général de la fonction publique, hors des cinq codes, sans inventer d'articles de substitution. L. 1251-58-5 adapte le contrat en lettre de mission pour les CDI intérimaires sans écarter le présent régime public.",
)

add(
    "L1251-61",
    """<p>Les salariés qu'une entreprise de travail temporaire met à la disposition d'une personne morale de droit public sont tenus de respecter les règles d'organisation et de fonctionnement du service où ils servent, ainsi que les obligations qui s'imposent à tout agent public. La protection prévue à l'article 11 de la loi n° 83-634 du 13 juillet 1983 portant droits et obligations des fonctionnaires leur est applicable.</p>
<p>Aucune fonction susceptible de les exposer aux sanctions prévues aux articles 432-12 et 432-13 du code pénal ne peut leur être confiée.</p>""",
    "Réécriture à droit constant : les obligations des salariés sont formulées directement, la protection est identifiée dans une phrase distincte et l'interdiction d'attribution de fonctions reste dans le second alinéa. Aucune réforme de fond.",
    "Le bénéfice de la protection et l'interdiction liée aux deux articles pénaux sont conservés. Le renvoi historique à l'article 11 de la loi n° 83-634 du 13 juillet 1983 demeure celui de la source : contrôler sa coordination avec les dispositions de protection fonctionnelle du code général de la fonction publique, extérieur aux cinq codes. Aucun renvoi de substitution non vérifié n'est introduit. Cette mise à disposition ne vaut pas acquisition du statut de fonctionnaire.",
)

add(
    "L1251-62",
    """<p>Lorsqu'une personne morale de droit public continue d'employer un salarié d'une entreprise de travail temporaire après la fin de sa mission, sans avoir conclu avec lui un contrat ou sans avoir conclu un nouveau contrat de mise à disposition, le salarié est réputé lié à cette personne morale par un contrat à durée déterminée de trois ans. Son ancienneté est alors calculée à partir du premier jour de sa mission. La durée d'ancienneté ainsi acquise est déduite de la période d'essai éventuellement prévue.</p>""",
    "Réécriture à droit constant : la poursuite d'emploi et les deux absences de contrat sont exposées avant leur conséquence ; le calcul et l'imputation de l'ancienneté sont formulés dans deux phrases autonomes du même alinéa. Aucune réforme de fond du CDD de droit public.",
    "Durée de trois ans, prise d'effet du calcul d'ancienneté au premier jour de la mission et déduction de cette ancienneté de l'essai conservées. Le « ou » entre les deux absences de contrat est repris tel qu'il figure dans la source ; sa portée alternative appelle contrôle et n'est pas remplacée silencieusement par une condition cumulative. Le plafond d'essai de trois mois des nouveaux CDI prévu par la réforme ne s'étend pas à ce CDD de droit public.",
)

add(
    "L1251-63",
    """<p>La juridiction administrative connaît des litiges relatifs à une mission d'intérim entre le salarié et la personne publique utilisatrice qui gère un service public administratif.</p>""",
    "Réécriture à droit constant : la juridiction compétente est le sujet de la phrase et les parties ainsi que la nature du service restent explicites. Aucune réforme de fond de la compétence juridictionnelle.",
    "La compétence vise les litiges entre le salarié et la personne publique utilisatrice gérant un service public administratif. Elle n'est pas étendue aux litiges avec l'entreprise de travail temporaire ni, par cette seule disposition, aux utilisateurs gérant un service public industriel et commercial.",
)

add(
    "L1252-1",
    """<p>Dans le cadre du travail à temps partagé, une entreprise de travail à temps partagé met un salarié à la disposition d'un client utilisateur pour l'exécution d'une mission.</p>
<p>Pour chaque mission, les contrats suivants sont conclus :</p>
<p>1° Un contrat de mise à disposition entre l'entreprise de travail à temps partagé et le client utilisateur, dénommé « entreprise utilisatrice » ;</p>
<p>2° Un contrat de travail, dénommé « contrat de travail à temps partagé », entre le salarié et son employeur, l'entreprise de travail à temps partagé.</p>""",
    "Réécriture à droit constant : la définition décrit directement l'action de l'entreprise, puis les deux contrats exigés pour chaque mission et leurs parties sont présentés dans leurs subdivisions d'origine. Aucune réforme de fond.",
    "Quatre alinéas et les 1° et 2° maintenus. L'entreprise de travail à temps partagé demeure l'employeur ; le client demeure l'utilisateur. Lire l'exigence de contrat pour chaque mission avec la qualification à durée indéterminée de L. 1252-4, sans transformer les missions en CDD ni importer le régime des lettres de mission du CDI intérimaire.",
)

add(
    "L1252-2",
    """<p>Est entrepreneur de travail à temps partagé toute personne physique ou morale qui a pour activité exclusive, par dérogation aux dispositions de l'article L. 8241-1, de mettre du personnel qualifié à la disposition d'entreprises utilisatrices qui ne peuvent le recruter elles-mêmes en raison de leur taille ou de leurs moyens.</p>
<p>Les missions des salariés ainsi mis à disposition peuvent être réalisées à temps plein ou à temps partiel.</p>""",
    "Réécriture à droit constant : l'activité qui définit l'entrepreneur est formulée directement ; la dérogation au prêt de main-d'œuvre et les motifs empêchant le recrutement par l'utilisateur sont conservés. Aucune réforme de fond.",
    "Personnes physiques et morales, exclusivité, qualification du personnel et impossibilité de recrutement liée à la taille ou aux moyens sont conservées. Le renvoi à L. 8241-1 a été vérifié dans le corpus : cet article comporte l'exception relative aux entreprises de travail à temps partagé. Lire l'exclusivité avec L. 1252-3 et L. 1251-4 pour l'activité autorisée des entreprises de travail temporaire. La possibilité de missions à temps partiel ne supprime par elle-même aucun minimum spécial ; la réforme des règles générales du temps partiel doit rester dans son champ propre.",
)

add(
    "L1252-3",
    """<p>Une entreprise de travail temporaire peut également exercer l'activité d'entreprise de travail à temps partagé.</p>""",
    "Réécriture à droit constant : la faculté est énoncée pour une entreprise prise individuellement et son caractère complémentaire est explicité. La disposition courte conserve exactement son objet ; aucune réforme de fond.",
    "Faculté, sans obligation, conservée. Coordination vérifiée avec le 2° de L. 1251-4, qui autorise cette activité par dérogation à l'exclusivité du travail temporaire, et avec la définition de L. 1252-2. Aucune autorisation supplémentaire ni fusion des deux régimes n'est créée.",
)

add(
    "L1252-4",
    """<p>Le contrat de travail à temps partagé est réputé conclu pour une durée indéterminée.</p>""",
    "Réécriture à droit constant, limitée à la formulation de la conclusion du contrat : le terme « réputé », qui porte la qualification légale, est conservé. Aucune réforme de fond ni transformation de cette qualification en simple faculté.",
    "Alinéa unique et qualification à durée indéterminée maintenus. Les règles générales du CDI, notamment celles de l'essai, doivent être appliquées selon leur propre champ et leur transition pour les contrats antérieurs ; le présent article ne fixe ni nouvelle durée d'essai ni durée de mission.",
)

add(
    "L1252-5",
    """<p>Si la mise à disposition du salarié a lieu hors du territoire métropolitain, le contrat de travail à temps partagé doit prévoir une clause qui met le rapatriement du salarié à la charge de l'entreprise de travail à temps partagé.</p>
<p>Cette clause devient caduque lorsque le salarié prend l'initiative de rompre son contrat de travail.</p>""",
    "Réécriture à droit constant : l'obligation d'insérer la clause et l'entreprise qui supporte le rapatriement sont explicites ; la cause de caducité est formulée directement dans le second alinéa. Aucune réforme de fond.",
    "Le champ demeure toute mise à disposition hors du territoire métropolitain, sans le restreindre à l'étranger. La charge incombe à l'entreprise de travail à temps partagé. La caducité reste limitée à la rupture à l'initiative du salarié et n'est pas étendue aux autres ruptures.",
)


sources = json.loads(Path("source.json").read_text())
assert len(sources) == len(drafts) == 24
assert {s["number"] for s in sources} == set(drafts)
answer = []
for source in sources:
    proposed_xml, reason, review_notes = drafts[source["number"]]
    item = {key: source[key] for key in ("code_id", "source_id", "source_sha256", "number")}
    item.update(
        proposed_xml=proposed_xml,
        reason=reason,
        review_notes=review_notes,
        status="rewrite_draft",
    )
    answer.append(item)
Path("answer.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")
