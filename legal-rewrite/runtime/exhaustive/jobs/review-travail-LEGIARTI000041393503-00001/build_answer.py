import json
from html import unescape
from html.parser import HTMLParser

sources = json.load(open('source.json'))
refs = json.load(open('reference-targets.json'))
by_number = {a['number']: a for a in sources}
out = {}

def body(*paragraphs):
    return '\n'.join('<p>' + p + '</p>' for p in paragraphs)

def article(n, xml, reason, notes, removed=None, repeal=None):
    src = by_number[n]
    a = {k: src[k] for k in ['code_id','source_id','source_sha256','number']}
    a.update(proposed_xml=xml, reason=reason, review_notes=notes, status='rewrite_draft')
    if removed:
        a.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19', removed_provisions=removed)
    if repeal:
        a.update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19', repeal_scope=repeal)
    out[n] = a
    return a

article('R6323-10', body(
    "I.-Le salarié demande par écrit à son employeur un congé de transition professionnelle avant le début de l'action de formation. Aucun délai minimal de présentation de la demande avant ce début n'est exigé.",
    "1° Abrogé.", "2° Abrogé.",
    "II.-La demande de congé indique la date du début de l'action de formation, la désignation et la durée de celle-ci ainsi que le nom de l'organisme qui en est responsable. L'intitulé et la date de l'examen ne font pas l'objet de mentions distinctes obligatoires. Les informations exactes et à jour déjà communiquées à l'employeur n'ont pas à lui être transmises une seconde fois.",
    "III.-L'employeur informe l'intéressé de sa réponse, par écrit, dans le délai de trente jours suivant la réception de la demande de congé. En l'absence de réponse dans ce délai, l'autorisation est réputée accordée.",
    "IV.-L'employeur ne peut refuser d'accorder le congé demandé qu'en cas de non-respect, par le salarié, des conditions prévues au I ou au II ou des conditions d'ancienneté prévues au paragraphe 1. La décision par laquelle l'employeur rejette la demande est motivée.",
    "Le salarié titulaire d'un contrat de travail conclu avec une entreprise de travail temporaire mentionnée à l'article L. 1251-2 adresse sa demande de congé de transition professionnelle à cette entreprise.",
    "Les suppressions des délais de présentation de cent vingt et soixante jours et des mentions distinctes relatives à l'examen s'appliquent aux demandes présentées ou encore en cours d'examen à compter de l'entrée en vigueur de la loi portant la présente réforme. Ces anciens délais ou l'absence de ces mentions ne peuvent, à eux seuls, justifier un refus intervenant après cette date. Les décisions devenues définitives ne sont pas rouvertes. Les règles distinctes de report et de priorité des articles R. 6323-10-1 et R. 6323-10-2 demeurent applicables."
),
    "Réforme de fond : les prévenances de 120 et 60 jours déjà retirées dans le brouillon restent supprimées. La seconde passe retire aussi les mentions distinctes d'intitulé et de date d'examen : l'employeur organise l'absence à partir des dates et de la durée de formation, sans instruire la certification. Le contenu restant, la réponse sous trente jours, l'accord tacite, la motivation et le destinataire intérimaire sont maintenus à droit constant. Le réemploi des informations déjà fournies ne constitue pas un gain CRPA supplémentaire revendiqué.",
    "I à IV et 1°/2° conservés. Les six mois de la source distinguaient seulement les deux prévenances supprimées. R. 6323-10-1 et R. 6323-10-2, lus intégralement dans le corpus, gardent leurs reports, exceptions favorables et priorités ; aucune autorisation immédiate d'absence n'est créée. R. 6323-14 doit appliquer ces nouvelles conditions d'accès et ne pas rétablir les anciennes mentions. L'autorisation de congé reste nécessaire à la coordination de l'absence ; ce n'est ni une autorisation de rupture ni une condition d'indemnité. Les dispenses légales d'ancienneté restent applicables.",
    ["Prévenance obligatoire de cent vingt jours pour une interruption continue d'au moins six mois.",
     "Prévenance obligatoire de soixante jours pour les autres formations ou celles à temps partiel.",
     "Mentions distinctes obligatoires de l'intitulé et de la date de l'examen dans la demande de congé."])

article('R6323-11-1', body(
    "Tout salarié peut adresser une demande de prise en charge d'un projet de transition professionnelle à la commission paritaire interprofessionnelle régionale compétente au cours de l'exécution de son contrat de travail, dans les conditions d'ancienneté ou de dispense qui lui sont applicables. Cette faculté demeure ouverte pour les contrats antérieurs à la réforme et pour les futurs contrats uniques à durée indéterminée.",
    "Par dérogation à la condition d'accord préalable prévue à l'article R. 6323-11, la demande de prise en charge peut être déposée avant la réponse de l'employeur à la demande de congé. La prise en charge ne dispense pas d'obtenir le congé prévu à l'article R. 6323-10 lorsque la formation se déroule, même en partie, sur le temps de travail. L'autorisation expresse ou tacite de ce congé suffit ; aucun second accord de l'employeur sur la prise en charge n'est requis.",
    "Pour l'application de l'article D. 6323-9, la nature à durée déterminée ou indéterminée des contrats successifs ne fait pas obstacle à la prise en compte des périodes d'emploi. Aucune condition propre de quatre mois en contrat à durée déterminée n'est ajoutée par le présent article. Les dispenses d'ancienneté restent applicables et une conversion convenue conserve l'ancienneté acquise.",
    "Ces dispositions s'appliquent aux demandes en cours et aux demandes nouvelles à compter de l'entrée en vigueur de la loi instituant le contrat unique. Elles n'autorisent ni la conclusion ni le renouvellement d'un contrat à durée déterminée après cette date et ne subordonnent pas les droits de formation au paiement d'une contribution CPF-CDD."
),
    "La faculté de demande pendant l'emploi est coordonnée au contrat unique, sans fermer les droits des contrats antérieurs. Le préalable patronal au seul dépôt financier reste supprimé ; l'autorisation d'absence suffit ensuite. La seconde passe retire du brouillon le renvoi au 2° du I et aux exclusions du II de D. 6323-9 : sa proposition actuelle supprime précisément cette voie séparée et ces exclusions. Ni quatre mois de CDD ni ancienneté dans l'entreprise ne sont ainsi réintroduits. La commission conserve l'examen du financement ; aucun second agrément n'est instauré.",
    "D. 6323-9 officiel prévoit deux voies (24 mois dont 12 dans l'entreprise ; ou 24 mois sur cinq ans dont quatre de CDD sur douze) ; sa proposition fournie conserve 24 mois globaux, supprime les restrictions et préserve les dispenses. La présente coordination vise cette proposition, qui n'est pas le droit en vigueur. R. 6323-11, lu, conserve la compétence résidence/travail et l'interdiction de demandes simultanées ; seule l'antériorité de l'accord est écartée ici. R. 6323-14 doit permettre le dépôt avant réponse, sans financer une absence non autorisée. Maintien de la rémunération et des protections de R. 6323-14-1 ; aucun seuil d'indemnité de rupture ne conditionne la formation.",
    ["Accord de l'employeur préalable au dépôt financier, distinct de l'autorisation du congé sur temps de travail.",
     "Restriction de la faculté de demande pendant l'emploi aux seuls titulaires d'un contrat à durée déterminée."])

article('R6323-11-2', body(
    "Le salarié mentionné à l'article R. 6323-9-1 et réunissant l'une des conditions d'ancienneté prévues à cet article peut adresser une demande de prise en charge d'un projet de transition professionnelle à la commission paritaire interprofessionnelle régionale compétente après la fin de son dernier contrat de travail ou de son dernier contrat de mission. Aucun délai maximal après cette fin n'est imposé pour présenter la demande ou commencer l'action de formation.",
    "Lorsque l'emploi se poursuit dans le cadre d'un contrat unique à durée indéterminée, la demande peut également être présentée après la fin de la dernière mission. Celle-ci n'entraîne pas la rupture du contrat de travail et ne dispense pas du congé requis pour une formation sur le temps de travail. Les conditions d'ancienneté restent appréciées à la date du départ en formation selon l'article R. 6323-9-1, sans condition supplémentaire propre à l'entreprise ou au groupe où la demande est présentée.",
    "La suppression des délais de quatre mois pour la demande et de six mois pour le début de formation s'applique aux demandes présentées ou encore en cours d'examen à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris pour les contrats antérieurs. Les droits ouverts et les décisions favorables antérieurs demeurent acquis ; les décisions de refus devenues définitives ne sont pas rouvertes. Les voies générales et les dispenses légales d'ancienneté demeurent ouvertes."
),
    "Réforme de fond supplémentaire : à la suppression déjà acquise de la forclusion de dépôt à quatre mois s'ajoute celle du début de formation dans les six mois. Le calendrier des sessions ne justifie pas de perdre l'accès au financement ; l'activité récente exigée par R. 6323-9-1 et l'examen du projet continuent de borner l'éligibilité. La fin de mission permet la demande dans le contrat unique sans terminer l'emploi. Le brouillon est aussi coordonné au retrait, dans la cible proposée, des 220 jours cumulés et des 600 heures dans l'entreprise ; aucune de ces conditions n'est rétablie ici.",
    "Les I, II et III de R. 6323-9-1 fourni ont été confrontés : les seuils professionnels demeurent dans les 1° à 3°, 1 600 heures de branche sur dix-huit mois et intermissions au II, appréciation au départ au III ; la proposition allège deux conditions supplémentaires. L'absence de délai maximal après emploi n'efface donc pas les périodes de référence d'activité. Coordination nécessaire des interfaces de dépôt et des instructions de financement ; aucune prolongation automatique de droits à allocation chômage n'est créée. La fin effective et la notification d'une rupture restent régies par leurs textes distincts.",
    ["Forclusion de présentation de la demande quatre mois après le dernier contrat ou la dernière mission.",
     "Condition de commencement de la formation dans les six mois suivant le dernier contrat ou la dernière mission."])

article('R6323-14-1', body(
    "I.-Lorsque la demande de prise en charge est présentée par le salarié mentionné à l'article R. 6323-11-1, la commission paritaire interprofessionnelle régionale peut décider de prendre en charge le projet même quand l'action de formation associée débute après la fin effective du contrat de travail. Aucun délai maximal entre cette fin et le début de l'action de formation n'est exigé. Les conditions d'ancienneté ou de dispense et l'examen du projet demeurent applicables dans leur champ.",
    "II.-Pendant la durée de son projet de transition professionnelle, le travailleur mentionné au I a la qualité de stagiaire de la formation professionnelle. Cette qualité ne met pas fin à un contrat de travail qui se poursuit.",
    "Il bénéficie de la rémunération prévue à l'article L. 6323-17-5 ainsi que du maintien du régime de protection sociale dont il bénéficie au titre de son contrat de travail ou dont il bénéficiait au titre de son dernier contrat, en matière de sécurité sociale, d'assurance chômage et de retraite complémentaire. La commission paritaire interprofessionnelle régionale verse aux régimes concernés les cotisations sociales afférentes à ces garanties.",
    "Ces droits demeurent ouverts après un contrat à durée déterminée antérieur à la réforme et après un contrat unique à durée indéterminée, pour les situations futures éligibles. La fin d'une mission ou d'une phase de formation ne vaut pas fin du contrat unique. Lorsque l'emploi se poursuit, le versement de la rémunération et des cotisations suit les modalités applicables pendant cet emploi, sans double versement au titre de la même période.",
    "La suppression du délai de six mois s'applique aux demandes nouvelles et aux demandes encore en cours d'examen à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris après un contrat antérieur. Les droits ouverts et les décisions favorables antérieurs sont conservés ; les décisions de refus devenues définitives ne sont pas rouvertes."
),
    "Coordination de la suppression commune des échéances après emploi : le délai de six mois, encore maintenu dans le brouillon, cesse de fermer le financement. La rémunération, le statut de stagiaire et les trois protections sociales restent intégralement garantis, avec leur payeur. La continuité dans le contrat unique reste acquise. Ce renvoi d'exécution ne représente pas une seconde mesure de suppression de délai ni une suppression des cotisations prises en charge au profit du bénéficiaire.",
    "R. 6323-11-1 est rédigé dans ce lot en cohérence avec le nouveau D. 6323-9 proposé ; aucune ancienne condition de CDD n'est reconduite. L. 6323-17-5, lu dans le corpus, conserve la rémunération minimale, le versement patronal remboursé à partir de cinquante salariés et l'habilitation pour les autres cas. D. 6323-18-2 et R. 6323-18-2-1 distinguent après-emploi et emploi poursuivi. Le maintien du régime chômage n'est pas une allocation automatique sans ses conditions ; la contribution CPF-CDD supprimée est distincte des cotisations couvrant ici les garanties.",
    ["Condition de commencement de la formation au plus tard six mois après la cessation du contrat de travail.",
     "Réservation du maintien des garanties sociales au seul régime d'un ancien contrat à durée déterminée."])

article('R6323-14-3', body(
    "I.-La commission paritaire interprofessionnelle régionale prend en charge :",
    "1° Les frais pédagogiques et les frais de validation des compétences et des connaissances liés à la réalisation de l'action de formation ;",
    "2° Les frais annexes, composés des frais de transport, de repas et d'hébergement occasionnés par la formation suivie par le salarié qui exécute un projet de transition professionnelle ;",
    "3° La rémunération du salarié mentionnée à l'article L. 6323-17-5 ;",
    "4° Les cotisations de sécurité sociale afférentes à cette rémunération ;",
    "5° Les charges légales et conventionnelles assises sur cette rémunération.",
    "II.-La prise en charge est maintenue lorsque la décision de rompre le contrat de travail intervient après l'accord de prise en charge de la commission paritaire interprofessionnelle régionale et que la rupture est à l'initiative :",
    "1° De l'employeur ;",
    "2° Du bénéficiaire, sans obligation de conclure un nouveau contrat de travail ni délai de reprise d'emploi. S'il occupe un nouvel emploi et que la formation se déroule en tout ou partie sur le temps de travail correspondant, le congé associé doit être autorisé par le nouvel employeur. L'autorisation expresse ou tacite obtenue selon l'article R. 6323-10 suffit ; aucun second accord sur le financement n'est requis.",
    "La commission établit la décision de rupture et sa date au moyen des informations et pièces exactes dont elle dispose légalement. Elle ne demande au bénéficiaire une pièce complémentaire que si ces éléments ne permettent pas cette vérification. Tout document probant suffit ; aucune attestation particulière ni seconde transmission d'une pièce déjà disponible n'est exigée.",
    "Le maintien du financement ne dispense pas de l'assiduité à la formation et ne donne lieu à aucun double versement de rémunération pour la même période. Il ne supprime aucun salaire, congé acquis ou droit résultant de la rupture du contrat.",
    "Les allègements du II s'appliquent aux maintiens de prise en charge restant à décider à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris pour les contrats antérieurs. Les décisions favorables et les droits acquis restent conservés ; les décisions de refus devenues définitives ne sont pas rouvertes. Ces règles demeurent applicables aux situations futures éligibles dans le contrat unique, dont aucune phase de formation ne fixe le terme."
),
    "Réforme de fond supplémentaire : le bénéficiaire qui rompt son contrat ne doit plus retrouver un emploi pour conserver un projet déjà accepté. La condition de nouveau contrat est retirée en plus du délai d'un mois déjà supprimé. Le congé chez un nouvel employeur ne subsiste que si un nouvel emploi existe et si la formation empiète sur son temps de travail. Les cinq postes financés restent mot pour mot ceux de la source ; la décision de rupture postérieure à l'accord initial protège la continuité de cet accord. Le réemploi des justificatifs est maintenu sans être compté comme une nouvelle dispense CRPA.",
    "La date à vérifier reste celle de la décision de rupture, distincte de la cessation effective. Le délai d'un mois supprimé était une condition de reprise d'emploi après préavis, pas la durée du préavis. Les quinze jours du nouveau contrat unique, leur notification et les procédures collectives ou autorisations spéciales restent à leurs textes. L. 6323-17-5 et D. 6323-18-1, lus, conservent rémunération minimale et assiduité ; la présente règle spéciale maintient le financement après rupture. Les 4°/5° sont des dépenses de formation couvertes, non une abolition des prélèvements sociaux. Adaptation des décisions de maintien et interfaces nécessaire ; aucun droit à allocation chômage n'est créé par cette continuité.",
    ["Obligation de conclure un nouveau contrat de travail après une rupture à l'initiative du bénéficiaire.",
     "Condition de reprise d'emploi dans le mois suivant la fin du préavis pour conserver le financement accepté.",
     "Transmission systématique par le bénéficiaire du justificatif de rupture, même lorsque la commission le détient déjà légalement."])

article('D6323-18-2', body(
    "Lorsque le projet de transition professionnelle se déroule après la fin effective du contrat de travail dans les conditions de l'article R. 6323-14-1, la commission paritaire interprofessionnelle régionale verse la rémunération au bénéficiaire.",
    "Cette règle vaut après un contrat à durée déterminée conclu avant l'entrée en vigueur de la loi instituant le contrat unique comme après un contrat unique à durée indéterminée, pour les demandes en cours et les futures situations éligibles. Aucun délai maximal entre la cessation de l'emploi et le début de la formation n'est ajouté par le présent article.",
    "La seule fin d'une mission ne déclenche pas ce versement si le contrat de travail se poursuit ; les modalités de rémunération applicables pendant l'emploi restent alors régies par les articles D. 6323-18-1 et R. 6323-18-2-1, dans leurs champs respectifs. Les rémunérations et créances antérieures restent dues selon leur régime, sans double versement."
),
    "Coordination nécessaire du payeur après cessation effective de l'emploi : la rémunération n'est plus réservée au terme d'un CDD. Le renvoi suit aussi la suppression du délai de six mois dans R. 6323-14-1. Aucune coupe supplémentaire du paiement ne se justifie : il rend effectif le droit à formation lorsque l'employeur ne verse plus la rémunération. Ni taux, ni cotisation, ni montant ne sont réduits ; aucun allègement autonome supplémentaire n'est compté.",
    "R. 6323-14-1 et R. 6323-18-2-1 sont rédigés dans ce lot ; leurs vues fournies restent des brouillons datés, non le droit en vigueur. D. 6323-18-1 et L. 6323-17-5, lus intégralement dans le corpus, distinguent salaire versé par l'employeur puis remboursé, avances des moins de cinquante salariés et versement direct pour particuliers employeurs. Les intermittents gardent le versement direct de leur régime. Une fin de mission sous CDI ne constitue pas une rupture. Le versement postérieur à l'emploi n'est ni une indemnité de licenciement ni un transfert de financement nouveau.")

src = by_number['R6323-18-2-1']
xml = src['previous_draft']['proposed_xml']
xml = xml.replace("La commission verse la première avance au plus tard trente jours après réception de la facture de l'employeur indiquant le montant total de ces rémunérations et cotisations dues pendant le projet. Elle verse le solde à la fin du projet, une fois les justificatifs nécessaires reçus ou légalement disponibles selon le III.",
    "La commission verse la première avance au plus tard trente jours après réception de la demande d'avances de l'employeur lorsque le montant total des rémunérations et des cotisations dues pendant le projet est établi. Aucune facture distincte n'est exigée. Si ce montant ne résulte pas des éléments déjà légalement disponibles pour la commission, l'employeur le précise dans sa demande, sans document supplémentaire imposé. La commission verse le solde à la fin du projet, une fois les justificatifs nécessaires reçus ou légalement disponibles selon le III.")
xml = xml.replace("Les allègements de pièces s'appliquent", "La suppression de la facture distincte et les allègements de pièces s'appliquent")
article('R6323-18-2-1', xml,
    "La seconde passe supprime la facture séparée conditionnant la première avance : la demande d'avances et le montant déjà établi suffisent ; un montant manquant est indiqué dans cette même demande. Sont conservés les acquis du brouillon : lettre de mission dans le CDI plutôt que nouveau CDD de formation, correction explicite des deux renvois inexacts et absence de nouvelles productions de pièces déjà disponibles. La rémunération mensuelle du spectacle, les cotisations spécifiques, le remboursement sous un mois et l'avance des moins de cinquante salariés plafonnée à 90 % restent entiers, sans nouveau taux.",
    "Anomalies de la source signalées et corrigées : le II de R. 6323-9-1 porte les heures intérimaires, le III leur date d'appréciation ; « L. 125158-1 » est corrigé en L. 1251-58-1. La cible proposée retire les 600 heures dans l'entreprise mais conserve 1 600 heures de branche et les intermissions. Le III du présent article est explicité pour l'intérim, le I imposant le paiement direct au spectacle. Le contrat de mission antérieur garde son régime ; aucun CDD nouveau ou renouvellement après réforme. Le premier paiement garde trente jours, le solde la fin du projet, le prorata l'abandon ou l'absence supérieure à un mois ; taux négociés ou arrêté supplétif et signalements d'événements restent. L. 1251-58-2/3 et D. 6323-18-1 ont été lus : garantie mensuelle, congés, intermissions et répétition des trop-perçus restent autonomes. Le réemploi de données n'est pas un nouvel allègement CRPA. L'arrêté des avances doit suivre la suppression de la facture, sans être présenté comme réécrit ici.",
    ["Facture distincte imposée à l'employeur pour obtenir la première avance de financement du projet.",
     "Création d'un contrat de mission à durée déterminée pour une période de formation des salariés nouvellement recrutés.",
     "Nouvelle production systématique de pièces de remboursement ou d'avance déjà légalement disponibles à la commission."])

article('D6323-18-3', body(
    "I.-La rémunération due au titre du projet de transition professionnelle est égale à un pourcentage du salaire moyen de référence du bénéficiaire du projet, déterminé en fonction des salaires perçus au cours d'une période de référence.",
    "II.-Le salaire moyen de référence du salarié qui remplit les conditions d'ancienneté mentionnées au 1° du I de l'article D. 6323-9 ou bénéficie d'une dispense de ces conditions est calculé sur la base des salaires perçus au cours des douze mois précédant la formation, sous réserve de la référence plus favorable prévue au III et des règles spéciales applicables aux intermittents du spectacle et aux salariés des entreprises de travail temporaire.",
    "III.-Pour le bénéficiaire qui compte quatre mois d'activité salariée, consécutifs ou non, au cours des douze mois précédant la formation, le salaire moyen de référence est calculé sur les salaires perçus au cours des quatre derniers mois d'activité salariée lorsque ce calcul est plus favorable que celui du II. La nature à durée déterminée ou indéterminée des contrats correspondants n'exclut aucun de ces mois ; les périodes mentionnées au II de l'article D. 6323-9 sont prises en compte dans les mêmes conditions. Le calcul le plus favorable est retenu sans demande particulière du bénéficiaire.",
    "Les quatre mois du III constituent uniquement une période de calcul de la rémunération ; ils ne sont pas une condition supplémentaire d'ouverture du droit au projet. Les droits ouverts, rémunérations et créances acquis selon les règles antérieures sont conservés. Ces dispositions s'appliquent aux demandes en cours et futures à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris pour les périodes d'emploi antérieures et pour les futurs contrats uniques. La conversion convenue d'un contrat n'interrompt pas la prise en compte des périodes et salaires correspondants."
),
    "Coordination de fond supplémentaire indispensable : le brouillon renvoyait au 2° du I de D. 6323-9 que la vue actuelle abroge et conservait ses exclusions désormais levées. La référence de douze mois demeure ; la référence de quatre mois, possible avantage pour un salarié récemment mieux rémunéré, reste ouverte aux situations futures de même objet sans exiger un nouveau CDD ni la voie abrogée. Elle est retenue si plus favorable, sans démarche d'option. Il s'agit d'une extension favorable du calcul et d'une charge de comparaison pour la commission, non d'une baisse de cotisation ou d'un taux nouveau.",
    "Les 24 mois globaux ou dispenses restent régis par D. 6323-9 proposé et L. 6323-17-2 lu ; aucune période de cinq ans, ancienneté de douze mois dans l'entreprise ou exclusion de contrats n'est rétablie. Le III conserve quatre mois d'activité sur douze comme critère de référence salariale seulement, ouvert aussi à ceux éligibles par dispense. Le choix favorable évite qu'une fusion des voies fasse perdre la base de quatre mois. Les règles spéciales de R. 6323-18-3-1 demeurent distinctes. D. 6323-18-4, lu, garde ses pourcentages 100/90/60 %, son seuil de deux SMIC et ses durées ; aucun de ces paramètres n'est modifié ici. Le double calcul administratif et l'extension possible de dépense restent à évaluer, sans solde net inventé.",
    ["Restriction du calcul de référence sur quatre mois aux seuls salaires de CDD et aux catégories non exclues par l'ancien II de D. 6323-9."])

article('R6323-18-3-1', body(
    "I.-Le salaire moyen de référence de l'artiste ou technicien intermittent du spectacle mentionné à l'article R. 6323-9-1 qui bénéficie d'un projet de transition professionnelle est calculé sur la base des salaires perçus au cours des périodes travaillées mentionnées au 1°, au 2° ou au 3° du I de l'article R. 6323-9-1, du montant de l'allocation d'assurance perçu par le salarié et des indemnités versées par la caisse des congés spectacles.",
    "II.-Le salaire moyen de référence du salarié titulaire d'un contrat de travail conclu avec une entreprise de travail temporaire, qui remplit les conditions d'ancienneté mentionnées au II de l'article R. 6323-9-1, est calculé sur la base des salaires moyens perçus au cours des 600 dernières heures de mission effectuées pour le compte de l'entreprise de travail temporaire dans laquelle cette demande est déposée.",
    "Le salaire moyen tient compte du salaire de base, des heures complémentaires ou supplémentaires et des primes de toute nature versées au cours de la période de référence, à l'exception de l'indemnité de fin de mission, de l'indemnité compensatrice de congés payés et des remboursements de frais professionnels.",
    "Lorsque le salarié ne compte pas 600 heures de mission dans cette entreprise, la moyenne est calculée sur les salaires des heures de mission effectivement accomplies dans la branche, dans la limite des 600 dernières heures, toutes entreprises de travail temporaire confondues. Les mêmes éléments de rémunération et exclusions s'appliquent. L'absence de 600 heures dans l'entreprise ou le groupe où la demande est présentée ne fait pas obstacle au droit à rémunération. Les données et pièces exactes déjà légalement disponibles sont réutilisées, sans attestation supplémentaire des mêmes heures.",
    "Lorsqu'aucune heure de mission ne peut être retenue, le salaire moyen de référence est calculé sur les rémunérations versées pendant les douze mois précédant la formation, y compris celles des périodes sans mission. Le calcul plus favorable du III de l'article D. 6323-18-3 s'applique lorsque sa période de référence est constituée. Ce renvoi ne soumet pas le bénéficiaire à une condition d'ancienneté supplémentaire de l'article D. 6323-9.",
    "Ces règles s'appliquent aux demandes en cours et futures à compter de l'entrée en vigueur de la loi portant la présente réforme. Elles restent ouvertes dans le contrat unique, sans terme automatique de l'emploi. Les intermissions prises en compte pour l'ancienneté ne deviennent pas des heures de mission pour la référence salariale. Les droits ouverts, décisions favorables, rémunérations et créances antérieurs sont conservés."
),
    "Le I et les deux premiers alinéas du II sont maintenus intégralement : allocation d'assurance et congés spectacles ne doivent pas disparaître, et les exclusions propres à l'intérim ont un autre champ. La seconde passe coordonne la suppression des 600 heures dans l'entreprise par R. 6323-9-1 proposé : le bénéficiaire nouvellement éligible ne doit pas perdre toute base salariale. La formule dans l'entreprise reste inchangée lorsqu'elle est utilisable ; à défaut la même moyenne porte sur les dernières heures de branche, plafonnées à 600. Ce calcul de secours est une coordination avec complexité supplémentaire identifiée, sans prétendre à une réduction autonome de charges.",
    "La source distingue déjà l'ancienneté dans l'entreprise OU le groupe (R. 6323-9-1) et une référence salariale dans la seule entreprise : l'éventuelle insuffisance d'heures dans cette entreprise est une difficulté préexistante, désormais traitée explicitement. La vue proposée retire l'obligation locale de 600 heures ; elle ne retire ni les 1 600 heures de branche sur dix-huit mois ni les intermissions d'ancienneté. La nouvelle moyenne n'intègre pas les intermissions comme heures rémunérées de mission et ne diminue pas la garantie mensuelle du CDI intérimaire. En l'absence totale de mission utilisable, le calcul utilise les rémunérations réellement versées, notamment la garantie d'intermission, sur douze mois avec la possibilité favorable de quatre mois. Ce nouveau renvoi à D. 6323-18-3, source assignée et rédigée dans le lot mais non cible requise de cet article, ne réintroduit pas l'ancienneté générale de D. 6323-9. Les dispenses et la voie générale conservent leur champ ; aucun nouveau seuil d'accès de 600 heures n'est créé. L'utilisation de rémunérations de plusieurs entreprises pour le seul calcul de secours élargit les données utiles : accès légal à respecter, coût de traitement non chiffré. Les droits déjà ouverts sont protégés.")

src = by_number['R6324-1']
xml = src['previous_draft']['proposed_xml']
xml = xml.replace("Il peut intervenir avant ou pendant cette période.", "Il peut intervenir avant ou pendant la période de reconversion.")
xml = xml.replace("Les contrats antérieurs et les droits attachés aux avenants de reconversion ou de promotion par l'alternance conclus avant le 1er janvier 2026 sont conservés dans leur champ transitoire.",
    "Un essai n'est pas rendu obligatoire par ce dépôt ; s'il est stipulé pour un contrat unique, il relève du régime commun de trois mois sans renouvellement. Les contrats antérieurs et les droits attachés aux avenants de reconversion ou de promotion par l'alternance conclus avant le 1er janvier 2026 sont conservés dans leur champ transitoire. Les aides et financements restent ouverts aux futures périodes de reconversion éligibles dans le contrat unique.")
article('R6324-1', xml,
    "Après nouvel examen, les coupes du brouillon sont conservées : suppression de la fenêtre de dépôt des trente jours précédant la reconversion, des copies supplémentaires et des demandes de pièces sans lien avec les critères légaux. Une coupe supplémentaire des trois documents de base ne se justifie pas : accord et suspension attestent le consentement et le retour possible, convention décrit la prestation financée, contrat d'accueil établit l'emploi extérieur. Les compléments restent strictement nécessaires aux critères L. 6332-1. La coordination est précisée avec L. 6324-3 proposé : CDI d'accueil, essai facultatif du régime commun et financements futurs maintenus.",
    "L. 6324-3 fourni conserve contrat d'origine et rémunération en interne, suspension et retour en externe ; le nouveau contrat d'accueil n'a pas de terme ni d'essai obligatoire. Le plafond de trois mois sans renouvellement provient de la section travail, sans nouvelle date de promulgation. R. 6324-2/3 lus conservent vingt jours de décision, motivation, notification et contrôles. La fenêtre source est une période de dépôt, non un préavis minimal de trente jours. Le réemploi CRPA est distinct de la suppression de cette fenêtre et n'est pas compté comme allègement nouveau. La note source du décret 2026-39 attribue de façon ambiguë la survivance à la rédaction nouvelle pour les avenants antérieurs au 1er janvier 2026 ; la note législative de L. 6324-3 vise au contraire l'ancienne rédaction. Le III de l'article 11 de la loi 2025-989 et l'article 4 du décret 2026-39, hors code, doivent être coordonnés ; leur texte intégral n'est pas fourni ici. Aucun essai de CDD de six mois n'est rétabli par formulaire.",
    ["Fenêtre obligatoire de dépôt dans les trente jours précédant le début de la période de reconversion.",
     "Pouvoir indifférencié de réclamer tout autre document sans identifier le critère de financement et la pièce réellement manquante."])

src = by_number['R6324-4']
article('R6324-4', src['previous_draft']['proposed_xml'],
    "Abrogation intégrale pour les transmissions futures du second circuit de dépôt de l'accord et des refus au ministre. La seconde passe confirme cette suppression réelle sans déclaration de remplacement : l'opérateur détient déjà l'accord, décide du financement et notifie son refus motivé aux parties. Aucun reliquat utile propre à cet article ne justifie un nouveau corps. Les contrôles, le système d'information et les droits antérieurs ont leurs fondements autonomes et demeurent.",
    "R. 6324-1 à R. 6324-3 et R. 6323-32 lus intégralement : le SI-CPF, ses responsables, les garanties de données et la décision motivée ne sont pas abrogés. L. 6324-3 fourni maintient les accords de consentement et le CDI d'accueil proposé. Coordonner les spécifications de traitement et les instructions aux opérateurs ; ne pas rétablir ce dépôt sous forme de nouvelle déclaration. La note transitoire ambiguë du décret 2026-39 est signalée dans R. 6324-1 ; l'abrogation vise aussi les transmissions encore à effectuer des anciens avenants, sans annuler leurs aides. Ni les aides futures ni le financement ne sont subordonnés à ce dépôt ministériel supprimé.",
    repeal="Dépôt ministériel obligatoire de l'accord de reconversion et transmission au ministre des refus de prise en charge et de leurs motifs, pour toutes transmissions encore à effectuer après l'entrée en vigueur.")

article('D6325-12', body(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant la présente réforme. Aucune convention ni signature particulière n'est exigée sur son seul fondement pour les actions d'accompagnement et les enseignements de professionnalisation dispensés par un organisme de formation ou un établissement d'enseignement.",
    "Cette suppression s'applique aux conventions restant à conclure et aux dossiers en cours à cette date, sans nouvelle signature ni régularisation sur ce seul fondement. Les conventions valablement conclues, les prestations exécutées, les droits de formation, les aides et les créances antérieurs demeurent régis par leurs règles et engagements.",
    "La convention entre l'acheteur et l'organisme de formation prévue à l'article L. 6353-1 et les modalités de l'article D. 6353-1 demeurent applicables dans leur champ propre. Le document pédagogique annexé au contrat prévu à l'article D. 6325-11 demeure exigé, avec les objectifs, le programme et les modalités d'organisation, d'évaluation et de sanction de la formation. L'abrogation ne supprime ni la formation effective ni les obligations de qualité et de financement qui ont un autre fondement.",
    "Les actions de professionnalisation, les aides et les exonérations restent ouvertes aux futures situations éligibles dans le contrat unique à durée indéterminée. La durée de l'action, de la convention ou d'une aide ne fixe pas le terme de l'emploi ; les anciens contrats conservent leur régime et leurs droits acquis."
),
    "Coupe supplémentaire par rapport au brouillon : abrogation de l'exigence spéciale de convention signée au lieu de simplement permettre son regroupement sur un autre support. L. 6353-1 et D. 6353-1 encadrent déjà l'engagement entre acheteur et prestataire ; D. 6325-11 exige déjà l'ensemble des cinq éléments pédagogiques en annexe au contrat. Ces textes lus rendent la couche particulière de D. 6325-12 dispensable, sans enlever le contenu pédagogique ni le consentement contractuel. L'abrogation ne prétend pas que deux conventions étaient effectivement établies dans chaque dossier ; elle retire une base spéciale de signature et de régularisation.",
    "L. 6325-13 fourni passe de la durée du contrat à celle de l'action pour les nouveaux contrats uniques et conserve 15 %/25 % et 150 heures ; ces minima de formation ne sont pas un terme d'emploi. L. 6353-1, D. 6353-1 et D. 6325-11 ont été lus dans le corpus : les devis ou bons approuvés peuvent déjà, dans le champ du II de D. 6353-1, tenir lieu de convention. Les deux renvois réglementaires D. 6353-1 et D. 6325-11 sont nouveaux dans le texte proposé, non fournis comme cibles obligatoires, mais vérifiés dans le corpus. Les conventions existantes ne sont ni annulées ni privées de force obligatoire. Coordonner les modèles administratifs de professionnalisation ; le nombre de doubles signatures réellement évitées et le solde net de coût ne sont pas établis.",
    repeal="Exigence spéciale de signature d'une convention entreprise-prestataire pour l'accompagnement et les enseignements de professionnalisation, distincte des engagements généraux et du document pédagogique déjà obligatoires.")

class Plain(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts=[]
    def handle_data(self, data):
        self.parts.append(data)
    def handle_starttag(self, tag, attrs):
        if tag in ['p','br','div','li','tr']:
            self.parts.append(' ')
    def handle_endtag(self, tag):
        if tag in ['p','div','li','tr']:
            self.parts.append(' ')

def plain(s):
    p=Plain();p.feed(s or '')
    return ' '.join(''.join(p.parts).split())

def effect(n,kind,measure_id,description,before,after,unit,population,transition,replacement,squote,pquote):
    s=plain(by_number[n]['source_xml']);p=plain(out[n]['proposed_xml'])
    assert len(squote)>=12 and squote in s,(n,'source quote',squote)
    assert len(pquote)>=12 and pquote in p,(n,'proposed quote',pquote)
    return dict(kind=kind,measure_id=measure_id,description=description,before=before,after=after,unit=unit,
                affected_population=population,conditions_and_transition=transition,
                replacement_or_new_burdens=replacement,source_quote=squote,proposed_quote=pquote)

def impact(n,classification,assessment,limits,burdens,effects):
    out[n]['substantive_impact']=dict(version=1,classification=classification,assessment=assessment,
        scope_limitations=limits,new_burdens_review=burdens,effects=effects)

impact('R6323-10','material_reduction',
    "Par rapport à l'article officiel entier, les prévenances de 120/60 jours disparaissent et les deux mentions distinctes relatives à l'examen cessent d'être obligatoires. Le délai patronal de trente jours et l'accord tacite restent entiers. La seconde coupe est supplémentaire au brouillon ; aucune baisse de prélèvement n'est en cause.",
    "Les reports et priorités de R. 6323-10-1/2 demeurent ; l'absence n'est pas autorisée par le seul dépôt. Le réemploi des informations ne prouve pas un gain supplémentaire par rapport au droit existant. Aucun coût national n'est chiffré.",
    "Aucune charge nouvelle n'est identifiée : l'écrit, le contenu utile, la réponse et la motivation existaient déjà. Aucun formulaire, attestation ou délai minimal de remplacement n'est instauré.",[
    effect('R6323-10','obligation_removed','ptp-prevenances-depot-suppression',
        "Suppression des deux prévenances de dépôt de la demande de congé.",
        "Dépôt au moins 120 jours avant une interruption continue d'au moins six mois, ou 60 jours avant les autres formations et le temps partiel.",
        "Demande avant le début de formation, sans nombre minimal de jours d'anticipation ; autorisation expresse ou tacite toujours nécessaire.",'legal_duty',
        "Salariés demandant un congé de transition professionnelle à leur employeur, y compris entreprise de travail temporaire.",
        "Demandes nouvelles et en examen dès l'entrée en vigueur ; pas de réouverture des refus définitifs ; reports distincts maintenus.",
        "Aucun délai de dépôt de remplacement ; réponse patronale de trente jours inchangée.",
        "1° Cent vingt jours avant le début de l'action de formation lorsque la réalisation de celle-ci entraîne une interruption continue de travail d'au moins six mois ;",
        "Aucun délai minimal de présentation de la demande avant ce début n'est exigé."),
    effect('R6323-10','obligation_removed','ptp-mentions-examen-suppression',
        "Suppression des mentions séparées de l'examen dans le dossier adressé à l'employeur.",
        "L'intitulé et la date de l'examen doivent figurer en plus des dates, désignation, durée et organisme de formation.",
        "Dates, désignation, durée et organisme de formation conservés ; les mentions distinctes d'examen ne conditionnent plus le congé.",'legal_duty',
        "Demandeurs du congé de transition professionnelle.","Demandes nouvelles ou encore examinées après l'entrée en vigueur ; refus définitifs préservés.",
        "Aucune donnée de remplacement ; l'employeur conserve les informations de calendrier nécessaires à l'absence.",
        "l'intitulé et la date de l'examen concerné.",
        "L'intitulé et la date de l'examen ne font pas l'objet de mentions distinctes obligatoires.")])

impact('R6323-11-1','material_reduction',
    "Le préalable patronal au dépôt de financement est expressément dissocié de l'autorisation d'absence, et la faculté est ouverte aux contrats uniques futurs et aux contrats antérieurs. Le brouillon est rectifié pour ne plus reconstituer la voie de quatre mois et les exclusions que D. 6323-9 proposé supprime. Aucun deuxième agrément ancien n'est supposé avoir existé.",
    "Financement décidé par la commission et congé sur temps de travail restent requis. Les simplifications d'ancienneté proviennent de la cible D. 6323-9 proposée, non d'une nouvelle suppression comptée ici. L'absence de dépôt simultané multiple et la compétence territoriale subsistent dans R. 6323-11.",
    "Aucune charge nouvelle n'est identifiée : même demande, même commission, mêmes garanties du congé. Il n'est créé ni déclaration de remplacement, ni nouvelle preuve d'ancienneté, ni condition de contribution CPF-CDD.",[
    effect('R6323-11-1','obligation_removed','ptp-depot-financier-sans-accord-prealable',
        "Dépôt financier possible avant la réponse de l'employeur sur le congé.",
        "Le texte exige l'accord préalable de l'employeur lorsque la formation est prévue, même en partie, pendant le temps de travail.",
        "Le dépôt précède éventuellement la réponse ; l'autorisation expresse ou tacite est requise pour l'absence effective seulement.",'legal_duty',
        "Salariés éligibles, contrats antérieurs et contrats uniques futurs.","Demandes en cours et nouvelles dès l'entrée en vigueur du contrat unique.",
        "L'autorisation du congé subsiste ; aucun second accord sur le financement n'est exigé.",
        "L'accord préalable de l'employeur est requis lorsque le salarié souhaite suivre l'action de formation correspondante pour tout ou partie pendant son temps de travail.",
        "Par dérogation à la condition d'accord préalable prévue à l'article R. 6323-11, la demande de prise en charge peut être déposée avant la réponse de l'employeur à la demande de congé."),
    effect('R6323-11-1','coordination','contrat-unique-duree-indeterminee',
        "Continuité de la demande de financement dans le nouveau régime d'emploi.",
        "Faculté expressément prévue pour le salarié titulaire d'un CDD.",
        "Faculté ouverte pour les futurs contrats uniques comme pour les contrats antérieurs ; aucune réouverture des nouveaux CDD.",'regime',
        "Salariés demandant un projet de transition professionnelle pendant l'emploi.","Ancienneté générale et dispenses maintenues selon leurs textes coordonnés.",
        "Pas de document ni d'accord supplémentaire ; coordination d'une mesure commune, non seconde réduction.",
        "Lorsque le salarié est titulaire d'un contrat à durée déterminée,",
        "Cette faculté demeure ouverte pour les contrats antérieurs à la réforme et pour les futurs contrats uniques à durée indéterminée.")])

impact('R6323-11-2','material_reduction',
    "Les deux échéances après emploi sont réellement retirées : dépôt dans les quatre mois et début dans les six mois. La seconde suppression dépasse le brouillon. L'accès reste subordonné aux conditions d'activité pertinentes au départ, à l'examen du projet et au congé si le contrat se poursuit ; il ne s'agit pas d'un report de paiement.",
    "La suppression de forclusion n'est pas un droit illimité à financement sans activité éligible : les périodes de référence de R. 6323-9-1 subsistent dans leur champ. Les refus définitifs ne sont pas rouverts ; aucun montant de dépenses supplémentaires n'est établi.",
    "Aucune charge nouvelle n'est identifiée : aucun nouveau dossier, accord, justificatif ou délai ne remplace les deux échéances. Le champ des conditions d'ancienneté est celui de la cible proposée, sans seuil local réintroduit.",[
    effect('R6323-11-2','relief_extended','ptp-suppression-delais-apres-emploi',
        "Suppression des échéances de dépôt et de commencement après le dernier contrat ou la dernière mission.",
        "Demande au plus tard quatre mois après le terme et début de formation au plus tard six mois après ce terme.",
        "Aucune échéance maximale liée à cette fin pour la demande ou le début ; les conditions d'activité et de financement restent applicables.",'other',
        "Intermittents du spectacle et salariés des entreprises de travail temporaire visés par R. 6323-9-1, sans fermer les autres voies éligibles.",
        "Demandes nouvelles et en examen dès l'entrée en vigueur, y compris emplois antérieurs ; décisions favorables et droits ouverts conservés.",
        "Pas de délai ni formalité de substitution ; une fin de mission n'est pas une rupture du contrat unique.",
        "au plus tard quatre mois après le terme de son dernier contrat de travail ou contrat de mission, à la condition que l'action de formation débute au plus tard six mois après ce terme.",
        "Aucun délai maximal après cette fin n'est imposé pour présenter la demande ou commencer l'action de formation.")])

impact('R6323-14-1','coordination_only',
    "Cet article met en cohérence le financement et les garanties sociales après emploi avec la suppression commune du délai de six mois et avec le contrat unique. La rémunération, les cotisations, le statut de stagiaire et les trois protections sociales restent entiers. Ni taxe ni seconde mesure de délai supprimée ne sont comptées.",
    "Les conditions générales d'accès et de décision financière subsistent ; maintien du régime chômage ne vaut pas allocation automatique. Les refus définitifs ne sont pas rouverts. Aucun coût consolidé de l'extension des possibilités de formation n'est estimé.",
    "Aucune charge nouvelle n'est identifiée dans cette coordination : mêmes garanties et même financement, sans registre ni déclaration. Le non-double versement précise l'articulation des payeurs et n'introduit pas une nouvelle condition d'accès.",[
    effect('R6323-14-1','coordination','ptp-suppression-delais-apres-emploi',
        "Retrait coordonné de la condition de six mois du financement après l'emploi.",
        "La commission ne peut financer ce début postérieur que dans les six mois après le terme.",
        "Aucune échéance maximale de début après fin effective, sous les autres conditions d'accès et d'examen.",'other',
        "Bénéficiaires visés par R. 6323-11-1 après CDD antérieur ou contrat unique.",
        "Demandes en cours et futures dès l'entrée en vigueur ; refus définitifs non rouverts.",
        "Aucun remplacement ; coordination de la même mesure que R. 6323-11-2.",
        "à la condition toutefois qu'elle débute au plus tard six mois après celui-ci.",
        "Aucun délai maximal entre cette fin et le début de l'action de formation n'est exigé."),
    effect('R6323-14-1','coordination','contrat-unique-duree-indeterminee',
        "Maintien du régime de protection sociale après les futurs contrats uniques.",
        "Maintien du régime dont le bénéficiaire disposait lorsqu'il était titulaire d'un CDD.",
        "Maintien du régime du contrat en cours ou du dernier contrat, avec sécurité sociale, chômage et retraite complémentaire.",'regime',
        "Bénéficiaires présents et futurs du projet, sans disparition des anciens droits.",
        "Emploi poursuivi soumis à ses modalités de versement ; fin de formation sans effet automatique sur le contrat.",
        "Aucune contribution de remplacement ni suppression des cotisations afférentes aux garanties.",
        "du maintien du régime de protection sociale dont il bénéficiait lorsqu'il était titulaire d'un contrat de travail à durée déterminée,",
        "du maintien du régime de protection sociale dont il bénéficie au titre de son contrat de travail ou dont il bénéficiait au titre de son dernier contrat,")])

impact('R6323-14-3','material_reduction',
    "Les cinq dépenses prises en charge sont conservées. Après une rupture décidée par le bénéficiaire postérieurement à l'accord financier, l'obligation de nouvel emploi disparaît entièrement, ainsi que le délai d'un mois déjà retiré au brouillon. Le contrôle des faits de rupture subsiste sans justificatif systématiquement redemandé.",
    "Pas de suppression de l'assiduité, du consentement à une absence dans un emploi effectivement repris ni des conditions initiales du financement. Le réemploi des pièces ne compte pas comme nouvelle réduction CRPA ; coût du maintien sans nouvel emploi non chiffré.",
    "Aucune charge nouvelle n'est identifiée : le consentement du nouvel employeur existait déjà et n'est requis que si la formation empiète sur l'emploi. Aucun engagement de réemploi, formulaire ou attestation de remplacement n'est institué.",[
    effect('R6323-14-3','relief_extended','ptp-maintien-financement-apres-rupture',
        "Maintien du financement sans obligation de retrouver un emploi après rupture par le bénéficiaire.",
        "Nouveau contrat exigé dans le mois après la fin du préavis avec accord du nouvel employeur au congé.",
        "Pas de nouveau contrat ni de délai de reprise imposé ; congé autorisé seulement si un emploi repris est concerné par l'absence.",'legal_duty',
        "Bénéficiaires rompant leur contrat après l'accord de financement du projet.",
        "Décisions de maintien restant à prendre dès l'entrée en vigueur, contrats anciens compris ; refus définitifs non rouverts.",
        "Les cinq postes financés et l'assiduité restent ; pas de double rémunération de la même période.",
        "2° Par le bénéficiaire, sous réserve de la conclusion d'un nouveau contrat de travail succédant au précédent dans un délai d'un mois à compter de la date de fin de préavis et de l'accord donné par le nouvel employeur à la demande de congé associé.",
        "2° Du bénéficiaire, sans obligation de conclure un nouveau contrat de travail ni délai de reprise d'emploi.")])

impact('D6323-18-2','coordination_only',
    "Le paiement direct après emploi est conservé et étendu par coordination au contrat unique ; la référence exclusivement au CDD disparaît. Le renvoi au financement après emploi n'en rétablit pas la limite de six mois. Il n'est démontré aucune réduction de cotisation, de rémunération ou de formalité autonome dans cet article.",
    "La seule fin de mission n'ouvre pas un second circuit si l'emploi demeure. Les règles du spectacle, des particuliers employeurs et des avances pendant emploi restent distinctes. Aucun gain de trésorerie nouveau ni solde budgétaire n'est avancé.",
    "Aucune charge nouvelle n'est identifiée : la commission payait déjà après le contrat ; le texte conserve ce payeur et ne crée aucun justificatif ou déclaration. Les créances antérieures et l'absence de double versement demeurent.",[
    effect('D6323-18-2','coordination','contrat-unique-duree-indeterminee',
        "Continuité du paiement direct de la rémunération après les futurs contrats uniques.",
        "Versement direct après le terme du contrat de travail à durée déterminée.",
        "Versement direct après la fin effective du CDD antérieur ou du contrat unique ; emploi poursuivi soumis au régime pendant emploi.",'regime',
        "Bénéficiaires d'un projet après cessation effective de l'emploi.",
        "Demandes en cours et futures, créances antérieures conservées ; pas de délai maximal ajouté au renvoi R. 6323-14-1.",
        "Pas de nouveau financeur ni de nouvelle cotisation ; même commission payeuse.",
        "Lorsque le projet de transition professionnelle est réalisé après le terme du contrat de travail à durée déterminée en application de l'article R. 6323-14-1, la rémunération est versée par la commission paritaire interprofessionnelle régionale.",
        "Lorsque le projet de transition professionnelle se déroule après la fin effective du contrat de travail dans les conditions de l'article R. 6323-14-1, la commission paritaire interprofessionnelle régionale verse la rémunération au bénéficiaire.")])

impact('R6323-18-2-1','material_reduction',
    "La facture séparée de première avance disparaît réellement, en plus du maintien des corrections du brouillon sur le CDD de formation et les renvois. Le même plafond de 90 %, le même paiement à trente jours et les mêmes postes sociaux subsistent. Le réemploi des pièces déjà disponibles ne compte pas comme une nouvelle suppression de droit commun.",
    "La demande volontaire d'avance, l'établissement de son montant, les accords de taux ou l'arrêté supplétif, l'assiduité et les informations sur les changements restent. Il n'est pas démontré combien de factures distinctes étaient effectivement produites, ni une économie nationale ou un solde global de complexité.",
    "Aucune charge nouvelle indépendante n'est identifiée : le montant total figurait déjà sur la facture, il peut désormais figurer dans la même demande. La lettre de mission existe pour le CDI intérimaire et remplace le contrat de mission pour le contrat unique ; aucun registre ou justificatif nouveau ne s'y ajoute.",[
    effect('R6323-18-2-1','obligation_removed','ptp-avances-sans-facture-distincte',
        "Suppression de la facture spéciale de première avance, demande et montant établi suffisant.",
        "Première avance sous trente jours de la réception d'une facture de l'employeur portant le total des rémunérations et cotisations du projet.",
        "Première avance sous trente jours de la demande avec montant établi ; facture distincte non exigée ; plafond 90 % de la même assiette inchangé.",'legal_duty',
        "Employeurs intérimaires de moins de cinquante salariés demandant des avances de rémunération et cotisations de projet.",
        "Demandes et versements en cours ou futurs dès l'entrée en vigueur ; sommes déjà acquises et conditions de fond conservées.",
        "Le total manquant est indiqué dans la demande existante, sans attestation ou document de substitution imposé.",
        "La première avance est versée à l'employeur par la commission paritaire interprofessionnelle régionale au plus tard trente jours après la réception de la facture émise par l'employeur comprenant le montant total des rémunérations et des cotisations sociales légales et conventionnelles dues par l'employeur pendant le projet de transition professionnelle.",
        "Aucune facture distincte n'est exigée."),
    effect('R6323-18-2-1','coordination','contrat-unique-duree-indeterminee',
        "Coordination de la formation intérimaire avec l'emploi à durée indéterminée.",
        "Contrat de mission pour la formation, ou lettre de mission pour le CDI intérimaire.",
        "Lettre de mission dans l'emploi nouveau à durée indéterminée ; aucun nouveau CDD de formation ni essai supplémentaire.",'regime',
        "Salariés intérimaires bénéficiant d'un projet de transition professionnelle.",
        "Anciens contrats de mission préservés jusqu'au terme selon leurs règles ; aucun renouvellement de CDD après réforme.",
        "Lettre de mission en remplacement d'un contrat, selon la mesure commune du contrat unique ; garanties de rémunération conservées.",
        "l'entreprise de travail temporaire établit un contrat de mission en application de l'article L. 1251-57 ou une lettre de mission",
        "Cette affectation n'exige pas de nouveau contrat de mission à durée déterminée ; elle n'interrompt pas le contrat unique et ne crée ni terme de l'emploi ni nouvelle période d'essai.")])

impact('D6323-18-3','mixed',
    "La référence de quatre mois est préservée et étendue sans CDD requis, avec priorité au calcul plus favorable face aux douze mois. Cela évite qu'une fusion des voies d'ancienneté efface un avantage salarial. Une comparaison administrative supplémentaire est créée ; ni baisse de taux social ni réduction nette de complexité ne sont démontrées.",
    "L'accès au projet reste soumis à D. 6323-9 ou à ses dispenses ; les quatre mois ne conditionnent que ce calcul de référence. Les formules spéciales spectacle/intérim et les pourcentages de D. 6323-18-4 restent autonomes. Coût de dépense et coût du double calcul non chiffrés.",
    "La commission doit comparer les deux références lorsque quatre mois récents existent, charge de calcul nouvelle recensée. Aucune demande d'option, nouvelle attestation ou déclaration salariale n'est imposée au bénéficiaire ; le calcul utilise les rémunérations des périodes de référence déjà nécessaires.",[
    effect('D6323-18-3','relief_extended','ptp-reference-salariale-quatre-mois-preservee',
        "Préservation et extension de la référence sur quatre mois si plus favorable.",
        "Douze mois pour la voie du 1° ; quatre derniers mois de CDD non exclus pour la voie du 2° de D. 6323-9.",
        "Douze mois conservés ; quatre derniers mois d'activité pour le bénéficiaire ayant quatre mois sur les douze précédant la formation si plus favorable, sans exclusion liée au type de contrat.",'other',
        "Bénéficiaires relevant de la voie générale ou d'une dispense, hors calculs spéciaux spectacle et intérim.",
        "Demandes en cours et futures dès l'entrée en vigueur ; rémunérations et créances antérieures conservées ; périodes antérieures et contrats uniques pris en compte.",
        "Comparaison automatique ajoutée à la commission, sans option privée ni nouvelle pièce imposée.",
        "III.-Le salaire moyen de référence du salarié qui remplit les conditions d'ancienneté mentionnées au 2° de l'article D. 6323-9 est calculé sur la base des salaires perçus au cours des quatre derniers mois en contrat de travail à durée déterminée, à l'exclusion des contrats mentionnés au II de l'article D. 6323-9.",
        "III.-Pour le bénéficiaire qui compte quatre mois d'activité salariée, consécutifs ou non, au cours des douze mois précédant la formation, le salaire moyen de référence est calculé sur les salaires perçus au cours des quatre derniers mois d'activité salariée lorsque ce calcul est plus favorable que celui du II."),
    effect('D6323-18-3','obligation_added','ptp-reference-salariale-quatre-mois-preservee',
        "Charge de comparaison d'office des deux références pour préserver la plus favorable.",
        "Calcul attaché à chacune des deux voies de la source, sans obligation explicite de retenir systématiquement la meilleure moyenne.",
        "Commission tenue de retenir le calcul le plus favorable, sans demande du bénéficiaire.",'legal_duty',
        "Commissions paritaires interprofessionnelles régionales pour les bénéficiaires entrant dans le III.",
        "Même champ temporel que l'extension de la référence ; droits acquis protégés.",
        "Traitement supplémentaire à partir des salaires utiles ; son coût net n'est pas établi.",
        "I.-La rémunération due au titre du projet de transition professionnelle est égale à un pourcentage du salaire moyen de référence du bénéficiaire du projet, déterminé en fonction des salaires perçus au cours d'une période de référence.",
        "Le calcul le plus favorable est retenu sans demande particulière du bénéficiaire.")])

impact('R6323-18-3-1','mixed',
    "Les bases spectacle et intérim officielles restent intégrales dans les cas déjà calculables. Un calcul de secours de branche évite de recréer les 600 heures dans l'entreprise supprimées dans R. 6323-9-1 proposé ; sans mission utilisable, les rémunérations réelles sur douze mois et la référence de quatre mois plus favorable évitent une base vide. Cette coordination étend les données utiles et la complexité de certains calculs ; elle n'est pas une nouvelle obligation supprimée.",
    "La moyenne de secours s'applique seulement si les 600 heures dans l'entreprise manquent ; les intermissions demeurent du temps d'ancienneté, non des missions salariales fictives. Les voies générales et dispenses gardent leur régime. Aucun effet salarial individuel ou solde net administratif global n'est chiffré.",
    "Calcul subsidiaire sur plusieurs employeurs et données salariales correspondantes nouveaux dans ce cas, avec accès légal exigé. Aucune attestation supplémentaire des mêmes heures n'est créée ; l'accès multi-employeurs n'est pas présumé acquis hors des bases légales existantes. Cette complexité est recensée.",[
    effect('R6323-18-3-1','coordination','ptp-anciennete-interim-branche',
        "Empêcher la formule salariale de reconstituer la condition locale de 600 heures supprimée par la cible proposée.",
        "Seule base écrite : 600 dernières heures de mission dans l'entreprise de dépôt, alors que l'ancienneté source permet aussi les heures du groupe.",
        "Même base si disponible ; sinon dernières heures effectives de branche dans la limite de 600, toutes entreprises confondues ; sans heure utilisable, rémunérations réelles sur douze mois et référence plus favorable de quatre mois si constituée.",'other',
        "Salariés intérimaires éligibles ne disposant pas de 600 heures dans l'entreprise de dépôt.",
        "Demandes en cours et futures dès l'entrée en vigueur, décisions favorables et créances anciennes préservées.",
        "Calcul subsidiaire et données multi-employeurs ; pas de nouveau seuil d'accès, pas de salaire d'intermission fictif.",
        "est calculé sur la base des salaires moyens perçus au cours des 600 dernières heures de mission effectuées pour le compte de l'entreprise de travail temporaire dans laquelle cette demande est déposée.",
        "L'absence de 600 heures dans l'entreprise ou le groupe où la demande est présentée ne fait pas obstacle au droit à rémunération."),
    effect('R6323-18-3-1','complexity_added','ptp-anciennete-interim-branche',
        "Calcul de secours interentreprises pour rendre la nouvelle éligibilité opératoire.",
        "Référence aux salaires des heures de mission de la seule entreprise de dépôt.",
        "Si cette référence est incomplète, calcul sur les heures de plusieurs entreprises ; sans aucune mission utilisable, calcul sur douze mois de rémunérations réelles avec comparaison favorable de quatre mois si possible.",'other',
        "Commissions régionales traitant les cas de référence locale insuffisante.",
        "Même transition ; données exactes et légalement disponibles réutilisées, droits déjà ouverts préservés.",
        "Complexité de calcul et traitement de données plus larges ; coût net inconnu, aucun nouveau pouvoir général d'accès aux données.",
        "des 600 dernières heures de mission effectuées pour le compte de l'entreprise de travail temporaire dans laquelle cette demande est déposée.",
        "Lorsque le salarié ne compte pas 600 heures de mission dans cette entreprise, la moyenne est calculée sur les salaires des heures de mission effectivement accomplies dans la branche, dans la limite des 600 dernières heures, toutes entreprises de travail temporaire confondues.")])

impact('R6324-1','mixed',
    "La fenêtre de dépôt des trente jours précédant la reconversion est supprimée, et le pouvoir de complément est borné aux pièces nécessaires à des critères identifiés. L'opérateur doit désormais préciser le critère et la pièce manquante, charge de motivation ajoutée. Le contrat d'accueil est coordonné au CDI sans terme pédagogique. Le réemploi seul n'est pas compté comme nouveau gain CRPA.",
    "Accords, convention, emploi d'accueil et critères de financement restent vérifiables ; vingt jours de décision de R. 6324-2 conservés. Le coût net public et privé de la motivation supplémentaire n'est pas établi. La clarification de la note transitoire extérieure au code reste à effectuer.",
    "Charge nouvelle explicite pour l'opérateur : identifier le critère et la pièce manquante dans chaque demande de complément. Aucun registre ni donnée supplémentaire n'est exigé de l'employeur ; l'essai reste facultatif et la durée de reconversion ne termine pas l'emploi.",[
    effect('R6324-1','obligation_removed','reconversion-depot-sans-fenetre-trente-jours',
        "Suppression de la fenêtre exclusive de dépôt préalable à la période de reconversion.",
        "Envoi dématérialisé dans les trente jours précédant le début de la reconversion.",
        "Dépôt avant ou pendant la période, sans refus lié à cette ancienne fenêtre ; même examen de financement.",'legal_duty',
        "Employeurs demandant la prise en charge d'une période de reconversion.",
        "Demandes en cours ou nouvelles dès l'entrée en vigueur ; pas de redépôt ni de remise à zéro des délais d'instruction.",
        "Les documents nécessaires demeurent ; pas de déclaration de remplacement ni délai minimal nouveau.",
        "L'employeur adresse à l'opérateur de compétences, par voie dématérialisée, dans les trente jours précédant le début de l'exécution de la période de reconversion :",
        "Le dépôt n'est pas limité aux trente jours précédant le début de la reconversion. Il peut intervenir avant ou pendant la période de reconversion."),
    effect('R6324-1','compliance_cost_reduced','reconversion-complements-documents-limites',
        "Limitation des demandes de documents aux critères et aux éléments manquants nécessaires.",
        "Tout autre document demandé pour vérifier les critères, sans exigence expresse d'identifier la pièce manquante et sa nécessité.",
        "Seules pièces complémentaires nécessaires non déjà disponibles, avec critère et pièce identifiés.",'legal_duty',
        "Employeurs et opérateurs de compétences instruisant les dossiers de reconversion.",
        "Demandes en cours et futures dès l'entrée en vigueur, sans reprise de l'instruction.",
        "Motivation spécifique imposée à l'opérateur ; gain net non chiffré ; le droit existant au réemploi n'est pas recompté.",
        "4° Tout autre document demandé par l'opérateur de compétences visant à s'assurer du respect des critères mentionnés au 1° bis du I de l'article L. 6332-1.",
        "4° Les seules pièces complémentaires nécessaires pour vérifier les critères du 1° bis du I de l'article L. 6332-1 qui ne résultent pas des éléments déjà légalement disponibles pour l'opérateur."),
    effect('R6324-1','obligation_added','reconversion-complements-documents-limites',
        "Motivation précise des demandes complémentaires par l'opérateur.",
        "La source habilite la demande d'autres documents sans cette précision obligatoire.",
        "Chaque demande indique le critère à vérifier et la pièce manquante correspondante.",'legal_duty',
        "Opérateurs de compétences demandant un complément.","Demandes en cours et futures dès l'entrée en vigueur.",
        "Charge d'explication ajoutée au service pour limiter les pièces demandées ; solde net inconnu.",
        "Tout autre document demandé par l'opérateur de compétences visant à s'assurer du respect des critères",
        "Toute demande complémentaire précise le critère à vérifier et la pièce manquante correspondante.")])

impact('R6324-4','material_reduction',
    "Le dépôt au ministre de l'accord de reconversion et l'envoi des refus motivés par le même circuit sont entièrement supprimés pour les transmissions futures. L'opérateur garde la décision et l'information des parties. La suppression acquise au brouillon est confirmée après lecture entière, sans déclarer autant de réductions que de pièces concernées.",
    "Les contrôles autonomes, le SI-CPF et la conservation légale des données subsistent ; les accords et financements antérieurs restent valables. Les paramètres du traitement et les textes transitoires extérieurs doivent être coordonnés. Aucun coût public global n'est établi.",
    "Aucune charge nouvelle n'est identifiée : ni dépôt, ni rapport, ni déclaration de remplacement. La motivation du refus et la notification aux parties existaient déjà dans R. 6324-3 et ne sont pas une nouvelle formalité créée ici.",[
    effect('R6324-4','obligation_removed','reconversion-suppression-depot-ministeriel',
        "Suppression du circuit supplémentaire de dépôt de l'accord et des refus au ministre.",
        "L'opérateur dépose l'accord au ministre via SI-CPF et lui transmet les refus et leurs motifs.",
        "Aucun de ces dépôts ministériels sur le seul fondement abrogé ; décision, motivation et notification aux parties maintenues.",'legal_duty',
        "Opérateurs de compétences traitant les périodes de reconversion, y compris anciens avenants dans leur régime transitoire.",
        "Toute transmission encore à effectuer dès l'entrée en vigueur ; aucun rattrapage, dépôts et droits existants conservés.",
        "Aucun circuit substitué ; SI-CPF et contrôles légaux gardent leurs autres finalités.",
        "L'opérateur de compétences dépose l'accord écrit mentionné à l'article L. 6324-3 auprès du ministre chargé de la formation professionnelle, au moyen du traitement automatisé mentionné à l'article R. 6323-32.",
        "L'opérateur de compétences n'est plus tenu de déposer auprès du ministre chargé de la formation professionnelle l'accord écrit de reconversion, ni de lui transmettre par ce circuit les refus de prise en charge et leurs motifs.")])

impact('D6325-12','coordination_only',
    "Le fondement spécial de convention signée est abrogé mais le contenu pédagogique reste imposé par D. 6325-11 et l'engagement acheteur-prestataire par L. 6353-1/D. 6353-1, lus. Ces obligations générales pouvaient déjà être satisfaites par le même document : aucune baisse distincte de documents ou signatures n'est démontrée. L'abrogation coordonne ces fondements sans être comptée comme réduction matérielle autonome.",
    "La source n'établit pas que deux conventions distinctes étaient produites dans chaque cas ; aucun gain de conformité indépendant n'est avancé. Les conventions existantes, la formation effective et les financements restent régis par leurs textes autonomes. Le nombre de documents effectivement évités et le solde global de complexité restent inconnus.",
    "Aucune charge nouvelle n'est identifiée : les obligations pédagogiques et contractuelles rappelées préexistent dans les articles lus. Aucun agrément, déclaration ou attestation ne remplace la convention spéciale supprimée ; les avantages restent ouverts aux futurs contrats uniques.",[
    effect('D6325-12','coordination','professionnalisation-convention-speciale-supprimee',
        "Abrogation du fondement spécial redondant, sans obligation distincte de signature démontrée.",
        "Signature d'une convention entreprise-organisme ou établissement pour les actions et enseignements visés, avec cinq rubriques pédagogiques.",
        "Pas de convention ou signature particulière sur ce fondement ; convention générale de formation et document pédagogique conservent leurs fondements autonomes.",'legal_duty',
        "Entreprises, organismes de formation et établissements d'enseignement intervenant en professionnalisation.",
        "Conventions restant à conclure et dossiers en cours dès l'entrée en vigueur ; contrats, aides et créances anciens conservés et avantages futurs ouverts.",
        "Pas de remplacement ; obligations générales déjà applicables conservées ; aucun double document réputé systématique.",
        "donnent lieu à la signature, entre l'entreprise et l'organisme de formation ou l'établissement d'enseignement, d'une convention précisant les objectifs, le programme et les modalités d'organisation, d'évaluation et de sanction de la formation.",
        "Aucune convention ni signature particulière n'est exigée sur son seul fondement pour les actions d'accompagnement et les enseignements de professionnalisation dispensés par un organisme de formation ou un établissement d'enseignement.")])

contexts = {
 'R6323-10': "Le délai de demande de congé et celui de réponse de l'employeur concernent la formation, pas la rupture.",
 'R6323-11-1': "Le dépôt à la commission pendant l'emploi et l'ancienneté de formation ne sont pas des actes de rupture.",
 'R6323-11-2': "La fin du dernier contrat ou d'une mission sert ici à l'accès à la formation après activité.",
 'R6323-14-1': "Le financement postérieur à la fin effective du contrat et le statut de stagiaire ne constituent pas un licenciement.",
 'R6323-14-3': "Le maintien d'un financement après décision de rupture est distinct des effets de la notification et de la fin du préavis.",
 'D6323-18-2': "Le paiement direct débute après la cessation effective de l'emploi, et non à la seule notification d'une rupture.",
 'R6323-18-2-1': "L'affectation à la formation intérimaire par lettre de mission ne constitue pas une rupture de l'emploi.",
 'D6323-18-3': "Les quatre et douze mois servent au salaire de référence de formation, pas à une indemnité de rupture.",
 'R6323-18-3-1': "Les 600 heures de référence salariale ne sont ni un seuil d'indemnité ni un délai de rupture.",
 'R6324-1': "Le dépôt financier et l'accord de reconversion organisent une formation ou une suspension, sans décider d'une rupture.",
 'R6324-4': "La disparition du dépôt ministériel n'affecte ni la notification du refus aux parties ni une procédure de rupture.",
 'D6325-12': "La convention pédagogique entre entreprise et prestataire ne fixe ni durée ni coût de rupture de l'emploi."
}

def core_check(n, number):
    prefix=contexts[n]+' '
    if number=='L1234-1':
        return prefix+"La source L. 1234-1 règle les anciens préavis selon six mois/deux ans d'ancienneté ; la proposition fournie fixe quinze jours calendaires pour les nouveaux contrats, même en faute grave avec paiement si non exécutés. Ce délai individuel n'est pas importé dans les délais de formation. Les anciens contrats, les procédures collectives et les autorisations spéciales gardent leur régime. Le point de départ après notification relève de la coordination L. 1234-3, non fournie comme cible ici ; il n'est pas fixé par cet article de formation."
    if number=='L1221-2':
        return prefix+"La source admet encore un terme dans les cas du titre IV ; la proposition fournie, non droit en vigueur, interdit tout nouveau CDD ou renouvellement après la bascule et tout terme automatique de mission, de formation ou d'aide. Le présent texte suit ce champ privé, préserve les contrats antérieurs et ouvre les avantages de formation aux situations futures éligibles. Ni une durée pédagogique ni une fin d'affectation ne peut rompre le contrat unique ; les agents publics ne sont pas absorbés par cette coordination."
    if number=='L1234-9':
        return prefix+"La source ouvre l'indemnité à huit mois hors faute grave ; la proposition vise, pour les nouveaux contrats, zéro avant un an mesuré à la fin effective préavis inclus, puis 0,20 mois par année totale avec mois complets au prorata et plafond de six mois, employeur seul, avec sa réserve de faute grave. Aucune première année n'est retranchée une fois le seuil atteint. Ces conditions ne sont pas importées dans l'accès, le maintien ou le salaire de formation. La composante ancienne, les réparations d'illégalité, congés et indemnités spéciales gardent leur champ."
    raise ValueError(number)

specific_checks = {
 ('R6323-10','L1251-2'): "L. 1251-2 définit l'entreprise qui recrute et rémunère les salariés mis à disposition. Elle reste donc la destinataire du congé, non l'utilisateur. Sa proposition impose le contrat unique pour les recrutements nouveaux et renvoie aux garanties mensuelles et intermissions ; ces garanties ne sont ni un délai de réponse ni un terme de formation. Le renvoi est maintenu dans son champ exact, avec les anciens contrats préservés.",
 ('R6323-11-1','R6323-10'): "La vue fournie supprime 120/60 jours et maintient réponse écrite sous trente jours, accord tacite et refus motivé. Notre version du même lot retire en outre les mentions distinctes d'examen. L'autorisation expresse ou tacite suffit pour l'absence ; son attente n'empêche plus le dépôt financier. Ni le préavis de quinze jours ni le seuil d'un an d'indemnité n'y sont substitués.",
 ('R6323-11-1','D6323-9'): "La source prévoit 24 mois dont 12 dans l'entreprise ou 24 mois sur cinq ans dont quatre de CDD sur douze, avec exclusions et dispenses. La proposition fournie fusionne au 1° en 24 mois sans ancienneté locale, abroge le 2° et réintègre les périodes du II ; le III apprécie au départ. Le troisième paragraphe du brouillon R. 6323-11-1 rétablissait à tort les quatre mois et exclusions : il est remplacé, sans perte des dispenses ni de l'ancienneté de conversion.",
 ('R6323-11-2','R6323-9-1'): "Le I vise spectacle enregistré/vivant avec seuils spécifiques 130/65, 88/44 et 60/30 jours ou cachets ; le II vise 1 600 heures de branche sur dix-huit mois et les intermissions, le III apprécie au départ. La proposition retire les 220 jours cumulés et les 600 heures d'entreprise/groupe ; le présent article ne les ressuscite pas. La fin de mission sous contrat unique reste distincte de la rupture et le départ garde ses conditions d'activité, même sans délai post-emploi de quatre ou six mois.",
 ('R6323-14-1','R6323-11-1'): "La vue fournie ouvre la faculté pendant contrat unique mais conserve dans son troisième paragraphe la voie de quatre mois et les exclusions de D. 6323-9, contredites par la proposition actuelle de cette cible. Notre version dans ce lot retire ces références et maintient congé autorisé pour l'absence effective, sans accord préalable au seul dépôt. Le financement post-emploi de R. 6323-14-1 suit cette continuité, sans réserver le régime aux anciens CDD ni imposer un délai de six mois.",
 ('R6323-14-3','R6323-10'): "Le renvoi porte sur l'autorisation du congé chez le nouvel employeur : réponse sous trente jours et accord tacite restent valables, sans nouveau préavis de 120/60 jours. Le présent II n'exige plus de nouvel emploi ; cette autorisation ne vaut donc que si un emploi est effectivement repris et si l'action empiète sur son temps de travail. Notre R. 6323-10 du lot retire aussi les mentions d'examen, sans modifier la notification d'une rupture ni l'ancienneté de formation.",
 ('D6323-18-2','R6323-14-1'): "La vue fournie conserve un début de formation dans les six mois après la fin effective et maintient les trois protections sociales. Notre version de ce lot supprime cette échéance, en coordination avec R. 6323-11-2, tout en conservant statut, rémunération et cotisations. Le paiement direct ici suit la fin effective, non la seule notification ni la fin d'une mission dont l'emploi se poursuit ; les futurs contrats uniques restent couverts.",
 ('D6323-18-2','R6323-18-2-1'): "Le I organise le versement direct mensuel aux artistes et techniciens ; les II à IV concernent la formation intérimaire, le paiement patronal remboursé et les avances des moins de cinquante salariés. La version du lot conserve ces champs et retire seulement la facture distincte de première avance. Le renvoi ne remet pas à l'employeur le paiement d'un après-emploi déjà relevant de D. 6323-18-2, et la fin d'une lettre de mission n'est pas une cessation de CDI.",
 ('R6323-18-2-1','L1251-58-1'): "La source prévoit déjà une lettre de mission pour chaque mission en CDI intérimaire ; la proposition l'étend aux recrutements nouveaux en contrat unique et préserve ancienneté et garanties des CDI antérieurs. La lettre du II organise l'affectation à la formation, sans nouveau contrat à terme ni nouvel essai. Le contrat commercial de mise à disposition pour un utilisateur garde son champ propre ; il n'est pas exigé pour inventer une entreprise utilisatrice pendant le congé.",
 ('R6323-18-2-1','L1251-57'): "Les stages, bilans et VAE du 1°, dont le congé L. 6323-17-1, et les formations liées à l'activité du 2° sont assimilés à des missions. Le renvoi justifie l'affectation à la formation, non une embauche à durée déterminée. La proposition fournie maintient cette assimilation pour le contrat unique et les droits des anciens contrats ; ni fin pédagogique ni fin de mission ne rompt automatiquement l'emploi. Le préavis et l'indemnité restent leurs règles de rupture distinctes.",
 ('R6323-18-2-1','R6323-9-1'): "Le renvoi source au III pour l'ancienneté intérimaire est impropre : les heures de branche et intermissions figurent au II, le III ne fixe que la date d'appréciation au départ. Il est corrigé en II. La proposition cible retire les 600 heures dans l'entreprise/groupe et les 220 jours supplémentaires du spectacle ; aucun de ces seuils ne devient une condition de paiement. Le I du présent article garde les artistes/techniciens des 1° à 3° et leurs cotisations chômage propres.",
 ('D6323-18-3','R6323-11-1'): "La vue fournie continuait à viser l'ancien 2° du I et les exclusions du II de D. 6323-9 ; la version finale du présent lot les retire conformément à la cible proposée. Le droit au salaire de formation ne dépend donc plus d'une nouvelle période de CDD. Le maintien d'une moyenne favorable de quatre mois est organisé directement au III, comme règle de rémunération et non comme voie d'accès ou condition de notification de rupture.",
 ('D6323-18-3','D6323-9'): "La proposition de D. 6323-9 fournie abroge le 2° du I, l'ancienneté locale et les exclusions de périodes du II ; son III garde l'appréciation au départ et les dispenses restent ouvertes. Le brouillon de D. 6323-18-3 serait incohérent en maintenant une référence exclusive à ce 2°. La nouvelle rédaction conserve douze mois et permet quatre mois plus favorables pour quatre mois d'activité sur douze, sans condition de CDD, de cinq ans d'activité ou de contrat exclu. Les quatre mois ne restreignent pas l'ouverture du projet.",
 ('R6323-18-3-1','R6323-9-1'): "Le I sert aux périodes travaillées du spectacle et conserve allocations d'assurance et congés spectacles dans la moyenne ; le II concerne l'intérim. La vue proposée retire les 600 heures dans l'entreprise/groupe, sans retirer les 1 600 heures de branche sur dix-huit mois et les intermissions d'ancienneté. La source de calcul dans la seule entreprise pouvait déjà échouer lorsque les 600 heures étaient dans le groupe : le calcul subsidiaire de branche traite cette difficulté et la nouvelle éligibilité sans réintroduire un seuil local ni confondre intermissions et heures de mission.",
 ('R6324-1','L6324-3'): "Le I maintient le contrat et la rémunération en reconversion interne ; le II organise suspension, accord écrit et retour en externe. La source admet CDI ou CDD d'au moins six mois avec essai obligatoire ; la proposition fournie impose l'emploi nouveau à durée indéterminée et rend l'essai facultatif dans son régime commun. Les pièces de dépôt ne réintroduisent ni terme d'emploi ni essai obligatoire. La note protège l'ancienne rédaction pour les avenants conclus avant le 1er janvier 2026 ; cette date n'est pas celle de la réforme future du contrat unique.",
 ('R6324-4','L6324-3'): "L. 6324-3 conserve l'accord écrit protégeant l'organisation interne ou la suspension et le retour externe. La proposition cible prévoit un CDI d'accueil, une durée de phase sans terme d'emploi et un essai facultatif ; elle préserve les contrats antérieurs. Supprimer le dépôt au ministre ne supprime aucun de ces accords ni le financement futur éligible. Les avenants antérieurs au 1er janvier 2026 gardent leur régime de fond, mais leurs transmissions ministérielles encore à effectuer sont retirées expressément.",
 ('D6325-12','L6325-13'): "La cible officielle vise les contrats de professionnalisation CDD et les actions dans un CDI, avec 15 % à 25 % et au moins 150 heures. Sa proposition transfère la référence à la durée de l'action dans le contrat unique, sans terme d'emploi, et préserve les anciens droits. L'abrogation de D. 6325-12 porte uniquement sur une convention spéciale et ne retire ni ces heures, ni le prestataire/service de formation, ni les aides futures ; D. 6325-11 maintient les cinq rubriques pédagogiques sur son fondement propre."
}

for n,a in out.items():
    key=a['code_id']+'|'+a['source_id']
    checks=[]
    for target_key in refs['requirements'][key]:
        target=refs['targets'][target_key]
        number=target['number']
        assessment=core_check(n,number) if number in ['L1234-1','L1221-2','L1234-9'] else specific_checks[(n,number)]
        checks.append(dict(target_key=target_key,view_sha256=target['view_sha256'],assessment=assessment))
    a['reference_checks']=checks

benefits = {
 'R6323-10': "L'accord tacite à trente jours, la motivation du refus et les exceptions de report favorables du régime intérimaire restent ouverts. La suppression des prévenances et des mentions d'examen élargit l'accès au congé ; aucun salaire, dispense d'ancienneté ou droit de formation n'est retiré.",
 'R6323-11-1': "L'accès à la demande pendant l'emploi demeure pour les contrats antérieurs et futurs contrats uniques. Les dispenses d'ancienneté et périodes favorables de D. 6323-9 proposé ne sont pas fermées par l'ancien 2° ou ses exclusions. La suppression de la contribution CPF-CDD ne conditionne pas le bénéfice du projet.",
 'R6323-11-2': "L'accès postérieur à une mission ou à l'emploi reste ouvert aux artistes, techniciens et intérimaires éligibles, avec les voies générales et dispenses. Les délais de quatre et six mois cessent de faire perdre ce bénéfice ; décisions favorables, périodes anciennes et intermissions d'ancienneté sont préservées.",
 'R6323-14-1': "Statut de stagiaire, rémunération minimale, maintien de sécurité sociale, d'assurance chômage et de retraite complémentaire, ainsi que paiement des cotisations par la commission sont maintenus. Leur accès reste ouvert après les futurs contrats uniques sans forclusion de six mois, sans créer une allocation chômage inconditionnelle.",
 'R6323-14-3': "Les cinq avantages financés demeurent : frais pédagogiques et de validation, transport/repas/hébergement, rémunération, cotisations de sécurité sociale et charges légales et conventionnelles. Leur maintien après rupture par le bénéficiaire est élargi sans nouvel emploi imposé ; anciens droits et situations futures éligibles restent couverts.",
 'D6323-18-2': "Le paiement direct par la commission après la fin effective de l'emploi est maintenu et couvre les futurs contrats uniques. Les droits antérieurs sont conservés ; les garanties propres au spectacle et aux particuliers employeurs restent distinctes, sans transfert indu vers un ancien employeur ni double rémunération.",
 'R6323-18-2-1': "Les versements mensuels du spectacle avec cotisations chômage spécifiques, le remboursement sous un mois et les avances des moins de cinquante salariés jusqu'à 90 % demeurent. Le délai de trente jours de première avance, le solde et les conditions collectivement fixées restent applicables ; supprimer la facture ne ferme aucun de ces avantages futurs.",
 'D6323-18-3': "Les bases salariales de douze mois et de quatre mois peuvent chacune constituer un avantage ; le calcul plus favorable est retenu pour les bénéficiaires ayant quatre mois d'activité sur douze. Les contrats auparavant exclus sont réintégrés conformément à D. 6323-9 proposé, les créances anciennes conservées et les taux de rémunération non diminués.",
 'R6323-18-3-1': "Allocations d'assurance et congés spectacles restent dans la moyenne du spectacle. L'intérim garde salaire de base, heures complémentaires/supplémentaires et primes ; les indemnités et frais exclus gardent leur exclusion propre. Le calcul subsidiaire préserve le paiement des nouveaux éligibles sans 600 heures locales, et les droits antérieurs restent acquis.",
 'R6324-1': "Le financement de la reconversion, la rémunération interne, le consentement à la suspension et les possibilités de retour externe restent protégés. Aides futures et régimes des avenants antérieurs au 1er janvier 2026 demeurent dans leur champ. La suppression de fenêtre et les pièces limitées facilitent l'accès sans imposer un CDD ou un essai obligatoire.",
 'R6324-4': "Les accords, financements acquis, aides et droits des anciens avenants restent valables. La suppression du dépôt ministériel ne ferme pas les aides aux nouvelles reconversions éligibles dans le contrat unique ; elle conserve décision motivée, information des parties et recours sur leurs fondements propres.",
 'D6325-12': "Les enseignements, accompagnements et cinq rubriques pédagogiques restent protégés par L. 6325-13 et D. 6325-11 ; la convention générale de formation conserve son régime. Les aides, exonérations et droits de formation demeurent accessibles aux futures situations éligibles dans le contrat unique, ainsi qu'aux contrats et créances antérieurs."
}

for n,a in out.items():
    a['benefit_review']=benefits[n]

answer=[out[s['number']] for s in sources]
with open('answer.json','w') as f:
    json.dump(answer,f,ensure_ascii=False,indent=2)
    f.write('\n')
print('answer.json :',len(answer),'articles')
