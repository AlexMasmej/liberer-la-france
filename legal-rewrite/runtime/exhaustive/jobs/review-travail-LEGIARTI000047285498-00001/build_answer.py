import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
drafts = {}


def add(number, proposed_xml, reason, review_notes, removed=None):
    row = {
        'proposed_xml': proposed_xml,
        'reason': reason,
        'review_notes': review_notes,
        'status': 'rewrite_draft',
    }
    if removed is not None:
        row.update(
            change_type='normative_reduction',
            reform_policy_id='editorial_direction_2026_10_19',
            removed_provisions=removed,
        )
    drafts[number] = row


add(
    'L1225-35-2',
    '<p>La durée du congé de paternité et d’accueil de l’enfant compte comme une période de travail effectif pour déterminer les droits du salarié liés à son ancienneté.</p>'
    '<p>Le salarié conserve tous les avantages acquis avant le début du congé.</p>',
    'Droit constant après examen de seconde passe : la première phrase précise la portée de l’assimilation au travail effectif ; la seconde conserve expressément tous les avantages acquis. Aucune suppression de fond supplémentaire n’est justifiée : le calcul de l’ancienneté et la conservation des avantages répondent à deux risques distincts de perte de droits du fait du congé. Ils ne constituent ni une déclaration ni un contrôle administratif en double. Retirer l’une de ces garanties pénaliserait l’exercice du congé de paternité.',
    'Contrôle : toute la durée du congé est prise en compte, mais l’assimilation prévue ici reste limitée aux droits liés à l’ancienneté ; tous les avantages antérieurs sont conservés, pas seulement le salaire de base. Coordonner avec les garanties de droits liés à l’emploi de la directive (UE) 2019/1158, notamment son article 10. Pour l’indemnité de licenciement, maintenir cette ancienneté dans chacune des composantes antérieure et postérieure à la réforme de L. 1234-9, sans modifier ici leur taux ni leur transition. Les décisions fiscales, successorales, de logement et de retraite ne modifient pas cet article. La source et la proposition antérieure ont été lues intégralement ; la note source est vide.',
)

add(
    'L1225-36',
    '<p>À la fin du congé de paternité et d’accueil de l’enfant, l’employeur réintègre le salarié dans son emploi précédent ou dans un emploi similaire assorti d’une rémunération au moins équivalente.</p>',
    'Droit constant : l’employeur devient le sujet explicite de l’obligation de réintégration ; les deux possibilités de retour et le niveau minimal de rémunération sont conservés. La seconde passe ne justifie aucune coupe : le droit au congé serait fragilisé sans garantie de retour au travail. Cet article ne fait pas double emploi avec L. 1225-35-2, qui traite de l’ancienneté et des avantages acquis, et ne crée aucune formalité autonome.',
    'Contrôle : emploi précédent ou emploi similaire ; rémunération au moins équivalente, sans la limiter au salaire de base. La réintégration n’ouvre pas une nouvelle période d’essai. Maintenir la coordination avec les garanties de retour et de protection contre les traitements défavorables de la directive (UE) 2019/1158 ; aucune conformité globale n’est présumée. Le champ reste le congé de paternité et d’accueil de l’enfant. Source, note source vide et proposition antérieure relues intégralement.',
)

add(
    'L1225-37',
    '<p>Le salarié auquel l’autorité administrative ou un organisme désigné par voie réglementaire confie un enfant en vue de son adoption a droit à un congé d’adoption de seize semaines au plus. Un décret fixe le délai dans lequel ce congé doit être pris et les modalités de son fractionnement.</p>'
    '<p>La durée du congé d’adoption est portée à :</p>'
    '<p>1° Dix-huit semaines lorsque l’adoption porte à trois ou plus le nombre d’enfants à la charge du salarié ou du foyer ;</p>'
    '<p>2° Vingt-deux semaines en cas d’adoptions multiples.</p>',
    'Droit constant : le droit au congé, sa durée de base et le renvoi au décret sont exprimés en deux phrases dans le premier alinéa ; les deux majorations conservent leurs subdivisions. Aucune coupe de fond n’est retenue après seconde passe : le placement vérifié protège l’enfant et établit l’événement ouvrant le droit ; les durées différenciées permettent son accueil. Le renvoi au décret règle le calendrier et le fractionnement, sans créer d’autorisation individuelle supplémentaire. Sa suppression isolée désorganiserait également l’indemnisation qui reprend ces modalités.',
    'Contrôle : seize semaines au plus ; dix-huit semaines lorsque le nombre d’enfants à charge du salarié ou du foyer atteint au moins trois du fait de l’adoption ; vingt-deux semaines en cas d’adoptions multiples. Les 1° et 2° restent à leur place. R. 1225-9 et D. 1225-11-1 ont été lus dans le corpus : organismes habilités ; début au plus tôt sept jours avant l’arrivée ; fin au plus tard huit mois après ; deux fractions d’au moins vingt-cinq jours, y compris pour chaque parent en cas de partage. Ces paramètres réglementaires ne sont pas supprimés par le présent article. La note de D. 1225-11-1 vise les placements à compter du 15 septembre 2023 et reste une transition historique distincte. CSS L. 331-7 a été lu : conserver la coordination du calendrier et des durées d’indemnisation, ainsi que les jours supplémentaires de L. 1225-40. Le congé supplémentaire de naissance de L. 1225-46-2 demeure distinct. Source et proposition antérieure lues intégralement ; aucune note source dans le présent article.',
)

add(
    'L1225-38',
    '<p>Le congé d’adoption suspend le contrat de travail.</p>'
    '<p>Pendant cette suspension, les parents salariés bénéficient de la protection contre le licenciement prévue aux articles L. 1225-4 et L. 1225-5. Cette protection ne fait pas obstacle à l’arrivée à son terme d’un contrat de travail à durée déterminée.</p>',
    'Droit constant après seconde passe : les deux alinéas distinguent la suspension du contrat et la protection qui l’accompagne, avec maintien de l’échéance normale du CDD. Aucune suppression supplémentaire n’est justifiée. La suspension évite de confondre le congé avec une rupture ; la protection empêche de licencier en raison de son exercice. Le renvoi réutilise des garanties existantes plutôt que de créer une procédure supplémentaire. L’exception relative au CDD délimite déjà cette protection.',
    'L. 1225-4 et L. 1225-5 ont été lus intégralement dans le corpus : conserver leurs protections, exceptions et modalités propres ; leur application à l’adoption reste articulée avec la règle spéciale de L. 1225-39. La proposition consultée de L. 1225-5 admet déjà une transmission datable sans mode imposé : ne pas réintroduire indirectement une lettre recommandée obligatoire. L’échéance du CDD reste distincte d’une rupture anticipée. L’article 16 de la directive 2006/54/CE appelle une coordination pour la protection liée au congé d’adoption ; le renvoi national n’efface aucune contrainte européenne. Aucun déplacement des deux alinéas ; source, note vide et proposition antérieure relues.',
)

add(
    'L1225-39',
    '<p>Le licenciement est annulé si, dans les quinze jours à compter de sa notification, le salarié envoie à l’employeur une attestation justifiant l’arrivée à son foyer, dans un délai de quinze jours, d’un enfant placé en vue de son adoption. L’autorité administrative ou l’organisme autorisé pour l’adoption qui procède au placement délivre cette attestation. Une décision ou un document de placement émanant de cette même autorité ou de cet organisme et justifiant les mêmes faits tient lieu d’attestation. L’envoi peut être effectué par tout moyen permettant d’en établir la date ; aucune forme particulière de transmission n’est exigée. Lorsque l’employeur détient déjà l’un de ces documents, le salarié peut, dans le même délai, lui indiquer par tout moyen permettant d’en établir la date qu’il se prévaut de ce document ; aucune nouvelle transmission de celui-ci n’est exigée.</p>'
    '<p>L’annulation ne s’applique pas lorsque le licenciement est fondé sur une faute grave sans lien avec l’adoption ou sur l’impossibilité de maintenir le contrat de travail pour un motif étranger à l’adoption.</p>'
    '<p>Les nouvelles modalités de justification et de transmission s’appliquent aux démarches accomplies à compter de l’entrée en vigueur de la loi portant la présente rédaction, y compris lorsqu’un délai de quinze jours est en cours à cette date. Elles ne rouvrent pas les délais déjà expirés et ne remettent pas en cause la validité des transmissions antérieures.</p>',
    'Réforme de fond de seconde passe : suppression de la soumission de l’envoi à des formes réglementaires imposées, dont la lettre recommandée avec avis de réception ou la remise contre récépissé de R. 1225-11. Suppression aussi de l’obtention d’une attestation distincte lorsque le document officiel de placement justifie déjà les mêmes faits, puis de sa retransmission lorsque l’employeur le détient déjà. La preuve du placement reste issue de l’autorité ou de l’organisme compétent, et une démarche datable du salarié reste nécessaire dans les quinze jours : la simplification n’ouvre pas une annulation sans justification. À droit constant sont conservés les deux délais de quinze jours et les deux exceptions. La transition bénéficie aux délais en cours sans rouvrir les délais expirés.',
    'Coordonner R. 1225-10 pour conserver la compétence du président du conseil départemental pour l’attestation qu’il délivre, sans rendre cette attestation obligatoire lorsqu’un document équivalent satisfait à la loi ; conserver aussi le champ des organismes autorisés de L. 1225-39. R. 1225-11 doit cesser d’imposer ses deux modes de transmission. R. 1225-3 doit reconnaître la date d’envoi pour les nouveaux moyens et la date de la démarche se référant à un document déjà détenu. Ces trois articles réglementaires ont été lus. La date d’envoi, et non celle de réception, reste déterminante pour l’envoi du document. La source ne précise pas expressément le point de départ du second délai de quinze jours, relatif à l’arrivée de l’enfant : cette ambiguïté préexistante est conservée et signalée, sans fusion des délais ni point de départ inventé. La dispense ne vaut que si le document émane de l’émetteur compétent et prouve les mêmes faits ; elle ne remplace pas cette preuve par une simple déclaration du salarié. Maintenir L. 1225-38, les exceptions et le recours au juge ; coordonner R. 1227-5 pour qu’aucune sanction ne repose sur le seul défaut des formes ou du doublon supprimés, sous réserve de l’application de la loi pénale plus douce aux faits antérieurs. Les obligations substantielles de protection restent sanctionnées. Source et proposition antérieure relues ; note source vide.',
    [
        'Suppression de l’obligation de transmettre la justification du placement par un mode réglementaire imposé, notamment par lettre recommandée avec avis de réception ou remise contre récépissé.',
        'Suppression de l’obtention d’une attestation distincte lorsque la décision ou le document émanant de l’autorité ou de l’organisme de placement justifie déjà les mêmes faits.',
        'Suppression de la retransmission d’une attestation ou d’un document de placement déjà détenu par l’employeur, avec maintien d’une démarche datable du salarié dans le délai légal.',
    ],
)

add(
    'L1225-40',
    '<p>Le partage du congé d’adoption entre les deux parents salariés d’un couple ouvre droit à vingt-cinq jours supplémentaires de congé d’adoption, ou à trente-deux jours en cas d’adoptions multiples.</p>'
    '<p>Pour chaque parent, la durée du congé ainsi réparti ne peut dépasser les seize semaines ou, selon le cas, les dix-huit ou vingt-deux semaines prévues à l’article L. 1225-37.</p>'
    '<p>Les deux parents peuvent prendre leurs périodes de congé simultanément.</p>',
    'Droit constant : la rédaction distingue la majoration liée au partage, le plafond individuel et la possibilité de simultanéité, en conservant les trois alinéas. Après seconde passe, aucune coupe supplémentaire n’est justifiée. Les jours supplémentaires facilitent le partage effectif de l’accueil ; le plafond individuel délimite l’avantage de durée accordé au couple et évite d’attribuer à chacun la totalité du congé majoré. La simultanéité permet l’accueil commun sans formalité d’autorisation supplémentaire. Ces trois règles ne sont donc pas des obligations administratives doublonnées.',
    'Contrôle : couple de deux parents salariés ; partage effectif ; vingt-cinq ou trente-deux jours supplémentaires pour le congé partagé, et non pour chaque parent ; plafonds individuels de seize, dix-huit ou vingt-deux semaines selon L. 1225-37 ; simultanéité facultative. La source ne qualifie pas ici l’unité des jours : aucune qualification nouvelle n’est ajoutée. D. 1225-11-1 a été lu et conserve les règles propres au fractionnement de chaque part ; les majorations ne sont pas confondues avec la durée minimale de vingt-cinq jours d’une fraction. Maintenir la coordination avec l’indemnisation d’adoption du code de la sécurité sociale sans promettre un cumul d’indemnités nouveau. Source, note vide et proposition antérieure relues intégralement.',
)

add(
    'L1225-41',
    '<p>Le salarié titulaire de l’agrément mentionné aux articles L. 225-2 et L. 225-17 du code de l’action sociale et des familles bénéficie du congé d’adoption s’il adopte un enfant ou l’accueille en vue de son adoption, sur décision de l’autorité étrangère compétente. L’enfant doit avoir été autorisé, à ce titre, à entrer sur le territoire national.</p>',
    'Droit constant après seconde passe : les conditions liées à l’agrément et à la décision étrangère sont distinguées de l’autorisation d’entrée de l’enfant, au sein de l’unique alinéa. La qualité de salarié, omise dans la rédaction antérieure, est rétablie explicitement. Aucune coupe de fond supplémentaire n’est justifiée : ces conditions rattachent le congé à un placement international régulier et protègent l’enfant contre un déplacement irrégulier. Le présent article ne crée ni nouvel agrément ni nouvelle autorisation ; en supprimer les références ferait disparaître un contrôle substantiel, non une répétition documentaire.',
    'Contrôle : qualité de salarié ; agrément des articles L. 225-2 et L. 225-17 du code de l’action sociale et des familles ; adoption ou accueil en vue de l’adoption ; décision de l’autorité étrangère compétente ; entrée autorisée à ce titre sur le territoire national. Les deux branches de la décision étrangère sont maintenues, sans réserver le congé aux seules adoptions déjà achevées. Les dispositions du code de l’action sociale et des familles sont hors des cinq codes fournis : leur référence est conservée, sans prétendre les avoir réécrites ni supprimer les contraintes internationales de protection de l’enfant. Le droit au congé ne vaut pas autorisation d’entrée. Source entière, note vide et proposition antérieure relues.',
)

add(
    'L1225-42',
    '<p>Le salarié informe l’employeur du motif de son absence et de la date à laquelle il entend mettre fin à la suspension de son contrat de travail. Les informations déjà communiquées à l’employeur, notamment à l’occasion de la démarche prévue à l’article L. 1225-39, valent information au titre du présent alinéa et ne peuvent être demandées de nouveau. Le salarié fournit seulement les informations manquantes ou celles qui ont changé. Cette dispense de nouvelle communication s’applique à compter de l’entrée en vigueur de la loi portant la présente rédaction, y compris pour les congés déjà annoncés ou en cours et pour les informations transmises avant cette date. Les conséquences des manquements antérieurs restent régies par les dispositions alors applicables, sous réserve des règles d’application de la loi pénale dans le temps.</p>'
    '<p>La durée du congé d’adoption compte comme une période de travail effectif pour déterminer les droits du salarié liés à son ancienneté.</p>',
    'Réforme de fond de seconde passe : la communication déjà effectuée du motif de l’absence ou de sa date de fin remplit l’obligation, sans démarche distincte ni répétition à la demande de l’employeur. Le salarié n’a plus qu’à compléter les informations manquantes ou modifiées ; une justification déjà remise pour L. 1225-39 n’entraîne pas une seconde annonce du même motif. À droit constant, le motif et la date de fin restent dus lorsqu’ils ne sont pas connus, car ils permettent d’organiser l’absence et le retour. L’assimilation de toute la durée du congé à du travail effectif pour l’ancienneté est conservée : sa suppression pénaliserait l’exercice du congé. La transition réutilise aussi les communications antérieures pour les congés en cours.',
    'Les deux alinéas restent consacrés respectivement à l’information et à l’ancienneté. Le nouveau renvoi à L. 1225-39 vise un article existant du présent lot : son attestation n’indique pas nécessairement la date de fin du congé ; celle-ci reste à communiquer si elle manque. Aucune recherche d’informations dans un compte ou un fichier tiers n’est imposée à l’employeur : seules les informations qui lui ont déjà été communiquées sont réutilisées. Ne pas présenter R. 1225-11 comme créant un recommandé pour L. 1225-42 : son texte lu vise L. 1225-39. Coordonner la portée de R. 1227-5, également lu, pour qu’une seule absence de répétition d’une information déjà communiquée ne soit pas sanctionnée ; tenir compte de la loi pénale plus douce pour les faits antérieurs concernés. L’ancienneté reste prise en compte dans les composantes antérieure et postérieure de l’indemnité de L. 1234-9 selon leurs règles propres. Le régime d’indemnisation sociale et les durées de congé ne sont pas modifiés. Source, note source vide et proposition antérieure lues intégralement.',
    [
        'Suppression d’une communication distincte ou répétée du motif de l’absence et de la date de fin déjà communiqués à l’employeur, notamment lors de la justification du placement prévue à L. 1225-39.',
    ],
)

add(
    'L1225-43',
    '<p>À la fin du congé d’adoption, l’employeur réintègre le salarié dans son emploi précédent ou dans un emploi similaire assorti d’une rémunération au moins équivalente.</p>',
    'Droit constant : le débiteur de la garantie de retour est explicite et les deux possibilités d’emploi sont conservées. Aucune coupe supplémentaire n’est justifiée après seconde passe : la suspension du contrat prévue à L. 1225-38 ne précise pas à elle seule les caractéristiques du poste et la rémunération au retour. Supprimer cet article retirerait donc une garantie concrète d’emploi plutôt qu’un doublon. Il ne contient aucune déclaration ni autorisation administrative.',
    'Contrôle : retour dans l’emploi précédent ou un emploi similaire ; rémunération au moins équivalente appréciée sans réduction au seul salaire de base. L. 1225-44 garde son rôle distinct de rattrapage des évolutions de rémunération. Maintenir la coordination avec les garanties de retour de l’article 16 de la directive 2006/54/CE ; ne pas prétendre qu’un simple changement national écarte cette contrainte. Aucun nouvel essai ni nouvelle embauche au retour. Source, note source vide et proposition antérieure relues intégralement.',
)

add(
    'L1225-44',
    '<p>À la fin du congé d’adoption, l’employeur majore la rémunération du salarié, au sens de l’article L. 3221-3, des augmentations générales et de la moyenne des augmentations individuelles perçues pendant ce congé par les salariés de la même catégorie professionnelle ou, à défaut, de la moyenne des augmentations individuelles dans l’entreprise. Cette règle s’applique en l’absence d’accord collectif de branche ou d’entreprise prévoyant, pendant et après le congé, des garanties d’évolution de la rémunération au moins aussi favorables.</p>'
    '<p>Cette règle ne s’applique pas aux accords collectifs de branche ou d’entreprise conclus avant l’entrée en vigueur de la loi n° 2006-340 du 23 mars 2006 relative à l’égalité salariale entre les femmes et les hommes.</p>',
    'Droit constant : calcul et articulation avec les accords au moins aussi favorables sont réunis dans le premier alinéa ; l’exception historique demeure au deuxième et dernier alinéa. Cette organisation corrige la proposition antérieure en trois alinéas sans déplacer la cible du renvoi territorial. Aucune coupe de fond supplémentaire n’est justifiée : les augmentations générales et la moyenne des augmentations individuelles compensent deux effets distincts de l’absence sur la progression salariale ; le seul maintien d’une rémunération équivalente ne les couvre pas. L’accord au moins aussi favorable évite déjà de cumuler deux mécanismes équivalents. L’exception ancienne est conservée pour ne pas modifier rétroactivement le régime des accords antérieurs.',
    'L. 3221-3 a été lu : sa définition comprend le salaire de base et tous les avantages et accessoires, directs ou indirects, en espèces ou en nature, dus en raison de l’emploi. Contrôle du cumul des augmentations générales avec la moyenne individuelle, de la priorité donnée à la même catégorie professionnelle puis, à défaut, à l’entreprise, et des garanties conventionnelles pendant et après le congé. L. 1524-3 a été lu : il vise le dernier alinéa et substitue, à Mayotte, le 1er janvier 2018 à la référence d’entrée en vigueur de la loi de 2006 ; cette exception reste donc au dernier alinéa. Ne pas remplacer la date d’entrée en vigueur de cette loi par sa date de signature du 23 mars 2006, ni par celle de la future réforme. L. 1225-26, lu pour coordination, conserve le mécanisme correspondant en maternité. L’article 16 de la directive 2006/54/CE appelle le maintien d’une coordination sur les améliorations des conditions de travail pendant le congé ; la compatibilité de la dérogation historique n’est pas présumée. Source, note vide et proposition antérieure relues intégralement.',
)

add(
    'L1225-45',
    '<p>Les salariés en congé d’adoption bénéficient de plein droit de tout avantage lié à la naissance qu’une convention ou un accord collectif de travail accorde aux salariées en congé de maternité.</p>',
    'Droit constant : la rédaction antérieure est conservée en précisant qu’il s’agit d’une convention ou d’un accord collectif de travail. Après seconde passe, aucune suppression de fond supplémentaire n’est justifiée. L’extension de plein droit évite un traitement défavorable de l’adoption et dispense déjà le salarié d’obtenir une modification conventionnelle ou une autorisation pour chaque avantage. L’article ne fait pas double emploi avec le retour à l’emploi ou le rattrapage salarial, qui ont d’autres objets. Supprimer cette extension réduirait une garantie d’égalité sans retirer une démarche administrative.',
    'Contrôle : tous les salariés en congé d’adoption ; application de plein droit ; tout avantage conventionnel lié à la naissance accordé aux salariées en congé de maternité. La qualification « lié à la naissance » reste déterminante ; aucune extension indistincte à une mesure exclusivement liée à l’état biologique de grossesse n’est ajoutée. La garantie ne dépend ni du sexe du parent adoptant ni d’un nouvel accord. L. 1142-3, lu dans le corpus, conserve son articulation avec les dispositions d’adoption de L. 1225-37 à L. 1225-45. Source entière, note vide et proposition antérieure relues.',
)

add(
    'L1225-46',
    '<p>Le salarié titulaire de l’agrément mentionné aux articles L. 225-2 et L. 225-17 du code de l’action sociale et des familles a droit à un congé d’adoption internationale et extra-métropolitaine non rémunéré pour se rendre, en vue de l’adoption d’un enfant, à l’étranger, dans une collectivité régie par l’article 73 ou l’article 74 de la Constitution ou en Nouvelle-Calédonie. Ce droit s’exerce au départ d’un département métropolitain, d’une autre collectivité régie par l’article 73 de la Constitution, de Saint-Barthélemy, de Saint-Martin ou de Saint-Pierre-et-Miquelon.</p>'
    '<p>La durée maximale du congé est de six semaines par agrément.</p>'
    '<p>Le salarié informe l’employeur du début et de la durée envisagés du congé avant son départ, par tout moyen et sans délai minimal de prévenance. Cette règle s’applique aux départs intervenant à compter de l’entrée en vigueur de la loi portant la présente rédaction, y compris lorsque le congé a déjà été annoncé ; aucune nouvelle notification n’est alors exigée si ces informations ont déjà été communiquées et n’ont pas changé. Le non-respect de l’ancien délai de deux semaines ne peut être opposé pour ces départs. Les départs antérieurs restent régis par les dispositions alors applicables.</p>'
    '<p>Le salarié peut interrompre son congé avant la date prévue et reprendre son activité initiale.</p>'
    '<p>À la fin du congé, l’employeur réintègre le salarié dans son emploi précédent ou dans un emploi similaire assorti d’une rémunération au moins équivalente.</p>',
    'Réforme de fond de seconde passe : suppression du délai impératif de prévenance de deux semaines, qui peut empêcher un départ lié au calendrier des autorités de placement. L’employeur reçoit toujours avant le départ les informations nécessaires sur le début et la durée envisagée ; aucun délai minimal supplémentaire n’est imposé. Les informations déjà données n’ont pas à être répétées. La transition s’applique aux départs futurs, même déjà annoncés, et conserve le régime des départs antérieurs. À droit constant, sont maintenus l’agrément, le but d’adoption, le champ territorial, le caractère non rémunéré, les six semaines par agrément, la reprise anticipée et les garanties de retour. Ces éléments établissent et bornent un droit utile à la réalisation du placement ; leur suppression ne serait pas un simple retrait de formalités.',
    'Les cinq alinéas conservent leurs objets : bénéficiaire et trajets, durée, information, reprise anticipée, retour. Contrôle exhaustif des lieux de départ et destinations : départ d’un département métropolitain, d’une autre collectivité de l’article 73, de Saint-Barthélemy, de Saint-Martin ou de Saint-Pierre-et-Miquelon ; destination à l’étranger, dans une collectivité des articles 73 ou 74 ou en Nouvelle-Calédonie. La source juxtapose « à l’étranger » et « dans une collectivité » sans séparateur net : l’ambiguïté préexistante est signalée ; la lecture en destinations distinctes déjà retenue dans la proposition antérieure est explicitée sans ajouter de territoire. Six semaines par agrément, et non par déplacement ; aucune rémunération nouvelle. La dispense de préavis minimal ne modifie ni l’agrément ni les autorisations de déplacement ou d’entrée de l’enfant relevant d’autres textes. Aucun délai nouveau de reprise anticipée n’est inventé. Le congé supplémentaire de naissance des articles L. 1225-46-2 et suivants reste un régime distinct : ses préavis ne sont pas supprimés ; R. 1225-11-6, lu, vise ainsi la reprise anticipée de cet autre congé. Les articles du code de l’action sociale et des familles sont hors des cinq codes et ne sont pas présentés comme réécrits. Source entière, note source vide et proposition antérieure relues.',
    [
        'Suppression du délai minimal obligatoire de deux semaines entre l’information de l’employeur et le départ en congé d’adoption internationale et extra-métropolitaine, avec maintien de l’information avant le départ.',
    ],
)


answer = []
for source in sources:
    row = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    row.update(drafts[source['number']])
    answer.append(row)

assert len(answer) == len(drafts) == len(sources) == 12
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
