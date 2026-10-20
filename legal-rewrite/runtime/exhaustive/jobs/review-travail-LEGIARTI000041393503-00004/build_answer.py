import json
from html import escape
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())

def paragraphs(*parts):
    return '\n'.join('<p>' + escape(p, quote=False) + '</p>' for p in parts)

answer = []
for s in sources:
    a = {k: s[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    a.update(status='rewrite_draft', proposed_xml=s['previous_draft']['proposed_xml'],
             reason=s['previous_draft']['reason'], review_notes=s['previous_draft']['review_notes'])
    answer.append(a)

answer[0]['proposed_xml'] = paragraphs(
    "I.-Le salarié demande par écrit à son employeur un congé de transition professionnelle avant le début de l'action de formation. Aucun délai minimal de présentation de la demande avant ce début n'est exigé.",
    "1° Abrogé.",
    "2° Abrogé.",
    "II.-La demande précise la date de début, la désignation et la durée de l'action de formation ainsi que le nom de l'organisme responsable. L'intitulé et la date de l'examen ne constituent pas des mentions obligatoires distinctes. Les informations exactes et à jour déjà communiquées à l'employeur n'ont pas à lui être transmises une seconde fois.",
    "III.-L'employeur répond par écrit dans les trente jours suivant la réception de la demande. À défaut de réponse dans ce délai, le congé est réputé accordé.",
    "IV.-L'employeur ne peut refuser le congé que si le salarié ne respecte pas les conditions du I ou du II ou les conditions d'ancienneté prévues au paragraphe 1, compte tenu des dispenses applicables. Tout refus est motivé.",
    "Le salarié employé par une entreprise de travail temporaire mentionnée à l'article L. 1251-2 adresse sa demande à cette entreprise.",
    "Ces allègements s'appliquent aux demandes présentées ou encore en cours d'examen à compter de l'entrée en vigueur de la loi portant la présente réforme. Les anciens délais de cent vingt et soixante jours et l'absence des mentions distinctes d'examen ne peuvent, à eux seuls, justifier un refus intervenant après cette date. Les décisions devenues définitives ne sont pas rouvertes. Les règles distinctes de report et de priorité des articles R. 6323-10-1 et R. 6323-10-2 demeurent applicables. La durée de la formation ou du congé ne fixe pas de terme au contrat unique à durée indéterminée."
)
answer[0]['reason'] = "Réforme de fond : les prévenances de 120 et 60 jours déjà retirées dans le brouillon restent supprimées. La seconde passe retire en outre les mentions obligatoires distinctes de l'intitulé et de la date d'examen : la formation et l'absence sont identifiées par leur désignation, leur début, leur durée et leur organisme. La dispense de retransmettre des informations déjà reçues par l'employeur privé est conservée. Restent nécessaires l'écrit, la décision sous trente jours, l'accord tacite, la motivation et la détermination du bon employeur ; ce n'est pas une simple reformulation."
answer[0]['review_notes'] = "I à IV et emplacements 1°/2° conservés. Le seuil de six mois ne répartit plus les prévenances supprimées. Le délai de réponse de trente jours ne vaut pas autorisation immédiate d'absence ; R. 6323-10-1 conserve les reports de neuf mois, les seuils d'effectif et les exceptions intérimaires, et R. 6323-10-2 les priorités. Ces deux articles ont été lus dans le corpus public, comme R. 6323-14 : son contrôle doit porter sur les nouvelles mentions et non sur celles supprimées. La dispense de mentions d'examen ne supprime ni l'examen ni le congé correspondant. Renvois complémentaires non fournis comme cibles : R. 6323-10-1/10-2 et R. 6323-14 sont vérifiés au corpus, sans modification de leurs fichiers. Aucune nouvelle règle de rupture ni condition d'un an n'est appliquée au congé."

answer[1]['proposed_xml'] = paragraphs(
    "Tout salarié peut demander à la commission paritaire interprofessionnelle régionale compétente la prise en charge d'un projet de transition professionnelle pendant l'exécution de son contrat de travail, quelle que soit la nature de ce contrat. Cette faculté demeure ouverte dans le contrat unique à durée indéterminée et pour les contrats antérieurs à la réforme.",
    "Par dérogation à la condition d'accord préalable prévue à l'article R. 6323-11, la demande de prise en charge peut être déposée avant la réponse de l'employeur à la demande de congé. La prise en charge ne dispense pas d'obtenir le congé prévu à l'article R. 6323-10 lorsque la formation se déroule, même en partie, sur le temps de travail. L'autorisation expresse ou tacite de ce congé suffit ; aucun second accord de l'employeur sur la prise en charge n'est requis.",
    "Pour ces demandes, les quatre mois mentionnés au 2° du I de l'article D. 6323-9 sont comptés quelle que soit la nature du contrat de travail, y compris pour les périodes antérieures à la réforme. Aucune des exclusions des 1° à 5° du II de cet article n'est opposable. Les autres conditions d'ancienneté, leur date d'appréciation au départ en formation et les dispenses applicables demeurent.",
    "Ces dispositions s'appliquent aux demandes en cours et aux demandes nouvelles à compter de l'entrée en vigueur de la loi instituant le contrat unique. Les ouvertures de droits et décisions favorables antérieures sont conservées. Elles n'autorisent ni la conclusion ni le renouvellement d'un contrat à durée déterminée après cette date et ne subordonnent pas les droits de formation au paiement d'une contribution CPF-CDD."
)
answer[1]['reason'] = "Réforme de fond : maintien du dépôt financier sans attendre l'autorisation du congé et de l'accès dans le contrat unique. La seconde passe aligne réellement le texte sur la proposition actuelle de D. 6323-9 : tous les contrats et toutes les périodes auparavant exclues peuvent concourir aux quatre mois, y compris les périodes anciennes dans les demandes futures. Le brouillon antérieur maintenait à tort les exclusions 1° à 4°. L'autorisation d'absence, l'ancienneté restante et le contrôle du financement ont une fonction nécessaire ; aucun agrément financier patronal de remplacement n'est créé."
answer[1]['review_notes'] = "D. 6323-9, dans la vue fournie, propose vingt-quatre mois de salariat sur cinq ans, dont quatre mois sur douze, sans les cinq exclusions ; la voie de vingt-quatre mois dont douze dans l'entreprise et les dispenses demeurent. La source officielle de cette cible comporte encore ces exclusions : la proposition n'est pas le droit en vigueur. R. 6323-11, lu au corpus, conserve le choix territorial résidence/travail et l'interdiction de demandes simultanées ; seule sa chronologie d'accord patronal est écartée ici. Ce renvoi complémentaire n'est pas une cible fournie. Les conditions de R. 6323-14, lu au corpus, restent contrôlées sans rétablir l'attente avant dépôt. D. 6323-18-3 du lot coordonne les quatre mois de salaire et la protection du calcul ancien plus favorable. Aucun seuil d'indemnité de rupture ne conditionne l'accès à la formation."

answer[2]['proposed_xml'] = paragraphs(
    "Le salarié mentionné à l'article R. 6323-9-1 qui remplit l'une des conditions d'ancienneté prévues à cet article peut demander à la commission paritaire interprofessionnelle régionale compétente la prise en charge d'un projet de transition professionnelle après la fin de son dernier contrat de travail ou de son dernier contrat de mission.",
    "Lorsque l'emploi se poursuit dans le cadre d'un contrat unique à durée indéterminée, la demande peut également être présentée après la fin de la dernière mission. Cette fin de mission ne rompt pas le contrat de travail et ne dispense pas du congé requis pour une formation sur le temps de travail.",
    "Aucun délai maximal de dépôt de la demande ou de commencement de la formation après cette fin n'est imposé par le présent article. Les conditions d'ancienneté et leurs dispenses restent applicables ; l'ancienneté est appréciée à la date du départ en formation conformément au III de l'article R. 6323-9-1.",
    "La suppression du délai de quatre mois pour la demande et du délai de six mois pour le début de la formation s'applique aux demandes présentées ou encore en cours d'examen à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris pour les fins de contrat ou de mission antérieures. Les décisions favorables et droits déjà ouverts sont conservés ; les décisions devenues définitives ne sont pas rouvertes. Les périodes d'activité sous contrat antérieur restent prises en compte."
)
answer[2]['reason'] = "Réforme de fond : à la suppression déjà acquise de la forclusion de dépôt à quatre mois s'ajoute celle du commencement de formation imposé dans les six mois. Cette seconde coupure temporelle n'est pas nécessaire au contrôle du projet : les fenêtres d'activité et l'ancienneté restent appréciées au départ en formation, ainsi que l'éligibilité et le financement. La fin de mission conserve sa fonction d'accès, sans rompre l'emploi nouveau. Aucune déclaration ni échéance de remplacement n'est créée."
answer[2]['review_notes'] = "La source vise quatre mois pour déposer et six mois pour commencer, non un préavis de rupture. Les deux limites sont retirées, y compris pour une demande encore examinable portant sur un terme antérieur ; absence de réouverture des décisions définitives. R. 6323-9-1 distingue le I spectacle, le II intérim et le III date d'appréciation. Sa proposition actuelle retire les 600 heures dans l'entreprise mais conserve les 1 600 heures de branche sur dix-huit mois et les intermissions. Ces fenêtres maintenues peuvent encore limiter l'accès : il n'est pas promis un droit inconditionnel sans limite temporelle. R. 6323-14-1 du lot est coordonné pour la limite de six mois. La demande financière n'autorise pas à elle seule une absence pendant un emploi maintenu ; la fin de mission n'est pas une notification de rupture."

answer[3]['proposed_xml'] = paragraphs(
    "I.-Lorsque le salarié mentionné à l'article R. 6323-11-1 demande une prise en charge, la commission paritaire interprofessionnelle régionale peut financer le projet même si l'action de formation commence après la fin effective du contrat de travail. Aucun délai maximal entre cette fin et le début de la formation n'est imposé par le présent article. Les conditions d'accès et de financement, ainsi que les dispenses applicables, demeurent.",
    "II.-Pendant toute la durée de son projet de transition professionnelle, le travailleur mentionné au I a le statut de stagiaire de la formation professionnelle. Ce statut ne met pas, par lui-même, fin à un contrat de travail qui se poursuit.",
    "Il perçoit la rémunération prévue à l'article L. 6323-17-5. Le régime de protection sociale dont il bénéficie au titre de son contrat de travail ou dont il bénéficiait au titre de son dernier contrat est maintenu en matière de sécurité sociale, d'assurance chômage et de retraite complémentaire. La commission paritaire interprofessionnelle régionale verse aux régimes concernés les cotisations correspondant à ces garanties, selon les modalités de financement applicables à la période du projet.",
    "Ces droits demeurent ouverts après un contrat antérieur à la réforme et après un contrat unique à durée indéterminée, pour les projets présents et futurs éligibles. La fin d'une mission ou d'une phase de formation ne vaut pas fin du contrat unique. Lorsque l'emploi se poursuit, la formation et sa rémunération relèvent des règles applicables pendant cet emploi, sans double versement de la même rémunération.",
    "La suppression du délai de six mois s'applique aux demandes en cours et nouvelles à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris après une fin de contrat antérieure. Les décisions favorables, rémunérations, garanties et créances acquises sont conservées ; les décisions devenues définitives ne sont pas rouvertes."
)
answer[3]['reason'] = "Coordination de fond du contrat unique et de la suppression des délais après l'emploi opérée dans R. 6323-11-2 : la limite de six mois est également retirée ici pour ne pas subsister dans une autre voie d'accès. La rémunération, le statut de stagiaire, les trois branches de protection sociale et les cotisations versées par la commission sont nécessaires et entièrement maintenus. Aucun prélèvement social supplémentaire n'est supprimé, et cette coordination n'est pas comptée comme une seconde suppression du même délai."
answer[3]['review_notes'] = "I/II conservés. R. 6323-11-1 est désormais ouvert à tout salarié, sans exclusions de périodes par nature de contrat ; les anciens CDI ne sont pas exclus. L. 6323-17-5, lu au corpus mais non fourni comme cible, garantit une rémunération minimale et définit les modalités de payeur, distinctes de l'indemnité de rupture. La protection chômage ne crée pas automatiquement une allocation sans ses conditions. Le maintien des cotisations de garantie n'est pas la contribution patronale CPF-CDD de 1 % supprimée ailleurs. D. 6323-18-2 et R. 6323-18-2-1 du lot conservent la distinction après cessation effective/emploi maintenu/intermittents. Aucun droit de résiliation automatique à la fin du projet n'est introduit."

answer[4]['proposed_xml'] = paragraphs(
    "I.-La commission paritaire interprofessionnelle régionale prend en charge :",
    "1° Les frais pédagogiques et les frais de validation des compétences et des connaissances liés à l'action de formation ;",
    "2° Les frais annexes de transport, de repas et d'hébergement occasionnés par la formation suivie dans le cadre du projet de transition professionnelle ;",
    "3° La rémunération du salarié prévue à l'article L. 6323-17-5 ;",
    "4° Les cotisations de sécurité sociale correspondant à cette rémunération ;",
    "5° Les charges légales et conventionnelles assises sur cette rémunération.",
    "II.-Lorsque la décision de rompre le contrat de travail intervient après l'accord de prise en charge donné par la commission, cette prise en charge est maintenue en cas de rupture à l'initiative :",
    "1° De l'employeur ;",
    "2° Du bénéficiaire, sans condition de conclusion d'un nouveau contrat de travail ni de délai de réemploi.",
    "Si le bénéficiaire occupe un nouvel emploi et suit la formation, même en partie, pendant le temps de travail correspondant, le congé associé reste soumis à l'autorisation expresse ou tacite prévue à l'article R. 6323-10. Aucun accord de cet employeur sur le maintien du financement n'est exigé.",
    "La rupture et la date de sa décision sont établies par tout moyen probant. Le bénéficiaire n'est pas tenu de transmettre un justificatif distinct de rupture. La commission utilise les informations et pièces dont elle dispose légalement et peut demander les seules informations manquantes nécessaires à cette vérification, sans imposer une attestation ou un document particulier.",
    "Les allègements du II s'appliquent aux maintiens de prise en charge restant à décider à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris pour les contrats antérieurs. Les décisions favorables et créances acquises sont conservées. Les décisions devenues définitives ne sont pas rouvertes. Le maintien du financement ne dispense pas des règles distinctes de rupture du contrat ou d'assiduité à la formation."
)
answer[4]['reason'] = "Réforme de fond : la seconde passe supprime entièrement la condition de réemploi après une rupture décidée par le bénéficiaire, et non seulement son délai d'un mois. Une prise en charge déjà accordée n'a pas à disparaître selon l'auteur de la rupture alors que le projet demeure exécuté. L'autorisation d'absence chez un nouvel employeur garde sa seule fonction d'organisation du travail. Le justificatif distinct obligatoire de rupture est retiré au profit de la preuve libre des faits nécessaires ; pas de formulaire équivalent imposé. Les cinq postes financés, l'assiduité et la décision de rupture postérieure à l'accord initial sont maintenus."
answer[4]['review_notes'] = "Le II compare la décision de rupture à l'accord initial, non la seule fin effective du contrat. Suppression du délai d'un mois ET de l'exigence d'un nouveau contrat ; un emploi nouveau reste soumis au congé lorsqu'il est affecté par la formation. Les cotisations et charges des 4°/5° sont des postes financés au bénéfice du salarié, pas des taxes accessoires abolies ici. R. 6323-14-1 du lot conserve protection sociale et rémunération après l'emploi ; L. 6323-17-5 a été lu au corpus, hors des cibles fournies. Une demande d'information résiduelle sert à vérifier un fait précis et ne peut exiger de nouveau justificatif particulier de rupture. Les anciens préavis, les quinze jours du contrat unique et les procédures collectives restent distincts de l'ancien délai de réemploi. Aucun montant national de financement n'est présumé."

answer[5]['reason'] = "Coordination de fond déjà contenue dans le brouillon, conservée après nouvel examen : le payeur de la rémunération après la fin effective de l'emploi demeure la commission, y compris après le contrat unique. Supprimer ce versement fermerait un droit de formation ; le remplacer par le payeur d'un emploi encore actif créerait une confusion de régime. L'article ne contient ni formalité, ni agrément, ni délai ou prélèvement autonome à retirer davantage. La référence exclusive au terme du CDD doit néanmoins être corrigée : le texte officiel ne peut être conservé tel quel."
answer[5]['review_notes'] = "R. 6323-14-1 du lot supprime également la limite de six mois : le renvoi du présent article ne la rétablit pas. La fin de mission ne déclenche pas le versement après emploi si le CDI continue. D. 6323-18-1, lu au corpus avec ses notes, distingue versement patronal remboursé, avances aux entreprises de moins de cinquante salariés et versement direct pour particuliers employeurs ; R. 6323-18-2-1 a son champ spectacle/intérim. L. 6323-17-5 a aussi été lu. Ces renvois complémentaires D. 6323-18-1 et L. 6323-17-5 ne sont pas fournis comme cibles. Aucun ancien droit ni aucune aide future éligible n'est fermé, et le changement de contrat n'est pas un changement artificiel de financeur."

answer[6]['proposed_xml'] = paragraphs(
    "I.-Lorsqu'un projet de transition professionnelle est accordé à un artiste ou technicien intermittent du spectacle mentionné à l'article R. 6323-9-1 qui remplit la condition d'ancienneté du 1°, du 2° ou du 3° du I de cet article, la commission paritaire interprofessionnelle régionale verse chaque mois sa rémunération et les cotisations sociales légales et conventionnelles assises sur celle-ci. Ces versements comprennent les cotisations dues au titre des règles spécifiques d'indemnisation du régime d'assurance chômage prévues à l'article L. 5424-22.",
    "II.-Lorsqu'un projet est accordé à un salarié employé par une entreprise de travail temporaire qui remplit les conditions d'ancienneté du II de l'article R. 6323-9-1, l'entreprise formalise son affectation à la période de formation par une lettre de mission, dans le cadre des articles L. 1251-57 et L. 1251-58-1. Cette affectation n'exige pas de nouveau contrat de mission à durée déterminée ; elle n'interrompt pas le contrat unique et ne crée ni terme de l'emploi ni nouvelle période d'essai.",
    "III.-Pour le salarié mentionné au II, l'employeur verse la rémunération et les cotisations sociales légales et conventionnelles assises sur celle-ci.",
    "La commission rembourse l'employeur dans un délai maximal d'un mois à compter de la réception des éléments nécessaires suivants ou, s'ils sont déjà légalement disponibles pour elle, de la demande de remboursement :",
    "1° Les éléments établissant la rémunération versée ;",
    "2° Les éléments établissant l'assiduité du bénéficiaire à l'action de formation ou au stage en entreprise ;",
    "3° Le cas échéant, les éléments relatifs aux cotisations sociales légales et conventionnelles à la charge de l'employeur assises sur les rémunérations dans l'entreprise concernée.",
    "La copie intégrale du bulletin de paie n'est pas exigée. Les éléments nécessaires peuvent être établis par tout document probant. La commission réutilise les pièces exactes et à jour dont elle dispose légalement ; elle ne peut imposer leur nouvelle production ni une attestation distincte reproduisant les mêmes informations. Seuls les éléments nécessaires manquants sont transmis.",
    "IV.-Dans les entreprises de moins de cinquante salariés, l'employeur bénéficie, sur sa demande, du remboursement par avances de la rémunération et des cotisations sociales légales et conventionnelles assises sur celle-ci.",
    "Le total des avances ne peut dépasser 90 % du montant total des rémunérations mensuelles et des cotisations sociales légales et conventionnelles correspondantes dues par l'employeur pendant le projet.",
    "La commission verse la première avance au plus tard trente jours après réception de la demande d'avance indiquant le montant total de ces rémunérations et cotisations dues pendant le projet. Aucune facture distincte n'est exigée. Elle verse le solde à la fin du projet, une fois les éléments nécessaires reçus ou légalement disponibles selon le III.",
    "Si le salarié abandonne le projet ou s'absente pendant plus d'un mois, le paiement est calculé au prorata temporis de la durée du projet.",
    "La commission et l'employeur déterminent conjointement le taux et les conditions des avances. Ils peuvent retenir ces modalités pour l'ensemble des salariés bénéficiaires d'un projet pendant une période qu'ils définissent ensemble. À défaut d'accord avant le début du projet, le taux et les conditions de versement sont déterminés par arrêté du ministre chargé de la formation professionnelle.",
    "L'employeur informe la commission de tout événement susceptible de modifier le suivi de la formation, le montant de la rémunération ou celui des cotisations sociales légales et conventionnelles. Il lui transmet, avant l'avance suivante ou le solde, les seuls éléments nouveaux ou modifiés nécessaires qui ne sont pas déjà légalement disponibles.",
    "Le versement des avances est suspendu si l'employeur ne fournit pas les éléments nécessaires manquants. Il ne peut être suspendu au seul motif qu'une pièce exacte et à jour, déjà légalement disponible pour la commission, n'a pas été transmise à nouveau.",
    "Les contrats de mission valablement conclus avant l'entrée en vigueur de la loi instituant le contrat unique conservent leur régime et les droits qui y sont attachés jusqu'à leur terme. Aucun nouveau contrat de mission à durée déterminée ni renouvellement ne peut être imposé ou conclu après cette entrée en vigueur au titre du II. Les garanties de rémunération et d'ancienneté pendant les intermissions demeurent applicables dans leur champ.",
    "Les allègements de pièces et de facture s'appliquent aux demandes et versements en cours et futurs à compter de l'entrée en vigueur de la loi portant la présente réforme. Une demande d'avance déjà reçue contenant les montants requis suffit, sans nouveau dépôt ; les délais déjà courus ne sont pas repris. Les rémunérations, remboursements et avances acquis restent dus selon leurs conditions de fond ; aucun versement antérieur n'est remis en cause pour la seule modification de la forme du contrat."
)
answer[6]['reason'] = "Réforme de fond supplémentaire : la demande d'avance comportant déjà le total des rémunérations et cotisations suffit, sans facture distincte ; le remboursement n'exige plus une copie intégrale du bulletin de paie lorsque des éléments probants ciblés établissent la dépense. La simple réutilisation de pièces déjà légalement disponibles n'est pas comptée comme un gain nouveau du CRPA. Sont conservés les versements mensuels spectacle, le payeur intérimaire, le mois de remboursement, le seuil de moins de cinquante salariés, le plafond de 90 %, les trente jours de première avance, le solde, le prorata et le contrôle des changements. La formation dans le contrat unique n'impose plus un nouveau CDD de mission."
answer[6]['review_notes'] = "Corrections expresses des deux anomalies sources : l'ancienneté intérimaire relève du II de R. 6323-9-1, son III ne fixe que la date de départ ; « L. 125158-1 » est rectifié en L. 1251-58-1. La proposition actuelle de R. 6323-9-1 retire les 600 heures d'entreprise : ce seuil n'est pas réintroduit ici. Le III désigne expressément l'intérimaire du II, le I conservant le versement direct aux intermittents. La transition II est placée à la fin pour conserver l'enchaînement I à IV. L. 5424-22, D. 6323-18-1, L. 1251-58-2/58-3 et R. 1234-1 ont été lus au corpus ; ils ne sont pas des cibles supplémentaires à joindre. La formule source « prorata temporis de la durée du projet » est conservée : le brouillon ne peut en déduire silencieusement une nouvelle formule d'assiduité. Coordonner l'arrêté d'avances pour retirer la facture distincte ; son texte n'est pas fourni et n'est pas prétendu réécrit. Les règles de trop-perçu autonomes demeurent."

answer[7]['proposed_xml'] = paragraphs(
    "I.-La rémunération du bénéficiaire d'un projet de transition professionnelle correspond à un pourcentage de son salaire moyen de référence, établi à partir des salaires perçus pendant la période de référence applicable.",
    "II.-Pour le salarié qui remplit les conditions d'ancienneté du 1° du I de l'article D. 6323-9, le salaire moyen de référence est calculé sur les salaires perçus au cours des douze mois précédant la formation.",
    "III.-Pour le salarié qui remplit les conditions d'ancienneté du 2° du I de l'article D. 6323-9, le salaire moyen de référence est calculé sur les salaires perçus au cours des quatre derniers mois de travail retenus au titre de cette voie d'accès, quelle que soit la nature du contrat de travail. Aucune période n'est exclue de ce calcul sur le fondement des 1° à 5° du II de cet article.",
    "Pour le salarié qui satisfait également aux anciennes conditions de cette voie d'accès, le salaire moyen de référence ne peut être inférieur à celui calculé sur les quatre derniers mois en contrat à durée déterminée, en excluant les contrats mentionnés au II de l'article D. 6323-9 dans sa rédaction antérieure à la réforme.",
    "Ces règles s'appliquent aux demandes en cours et futures à compter de l'entrée en vigueur de la loi portant réforme du contrat de travail, y compris pour les périodes d'emploi antérieures. Les décisions favorables, rémunérations et créances déjà acquises sont conservées. La conversion convenue d'un contrat antérieur conserve les périodes et l'ancienneté correspondantes, sans double compte. Le calcul ne requiert ni nouveau contrat à durée déterminée ni rupture de l'emploi ; il ne limite pas la durée du contrat unique."
)
answer[7]['reason'] = "Coordination de fond avec l'ouverture actuelle de D. 6323-9, qui retire toutes les exclusions et la condition de CDD, y compris pour les services anciens. Le précédent brouillon conservait des exclusions incompatibles : elles sont retirées. Les références de douze et quatre mois restent distinctes et aucun taux de rémunération n'est modifié. Une sauvegarde explicite du calcul ancien plus favorable évite de diminuer une rémunération en intégrant désormais des périodes exclues, par exemple d'alternance. Cette sauvegarde ajoute une comparaison de calcul : le résultat est mixte, sans baisse nette de complexité revendiquée."
answer[7]['review_notes'] = "Les renvois aux 1° et 2° sont précisés comme appartenant au I de D. 6323-9. La proposition actuelle de cette cible ne conserve plus aucune exclusion du II et vaut pour les demandes en cours et futures avec services antérieurs. Les quatre mois ne sont pas une option universelle offerte à toute personne relevant du II : ils restent attachés à la voie du 2° du I. Le plancher favorable s'applique aux salariés satisfaisant aussi à l'ancienne voie, non à une moyenne fictive de CDD jamais exercés. Il requiert potentiellement un calcul supplémentaire, sans nouveau taux ni baisse des rémunérations déjà accordées. Les pourcentages de rémunération relèvent des articles suivants ; ils ne sont pas extrapolés ici. R. 6323-11-1 du lot suit le même champ, sans référence à un an d'ancienneté de rupture."

answer[8]['proposed_xml'] = paragraphs(
    "I.-Pour l'artiste ou le technicien intermittent du spectacle mentionné à l'article R. 6323-9-1 qui bénéficie d'un projet de transition professionnelle, le salaire moyen de référence est calculé à partir des salaires perçus pendant les périodes travaillées mentionnées au 1°, au 2° ou au 3° du I de cet article, de l'allocation d'assurance perçue et des indemnités versées par la caisse des congés spectacles.",
    "II.-Pour le salarié employé par une entreprise de travail temporaire qui remplit les conditions d'ancienneté du II de l'article R. 6323-9-1, le salaire moyen de référence est établi à partir des salaires moyens perçus pendant les 600 dernières heures de mission effectuées pour l'entreprise de travail temporaire auprès de laquelle la demande est déposée.",
    "Cette moyenne comprend le salaire de base, les heures complémentaires ou supplémentaires et les primes de toute nature versées pendant la période de référence. Elle exclut l'indemnité de fin de mission, l'indemnité compensatrice de congés payés et les remboursements de frais professionnels.",
    "Lorsque le salarié n'a pas effectué 600 heures de mission pour cette entreprise, le salaire moyen de référence est calculé sur les salaires perçus au cours des 600 dernières heures de mission effectuées dans la branche du travail temporaire, avec les mêmes éléments de salaire et exclusions. S'il a effectué moins de 600 heures de mission dans la branche, la moyenne porte sur les heures de mission effectivement accomplies. En l'absence de toute heure de mission, la rémunération mensuelle minimale garantie par son contrat et applicable à la date du départ en formation sert de salaire mensuel de référence. Ces calculs subsidiaires ne constituent pas une condition d'ancienneté supplémentaire dans l'entreprise, le groupe ou la branche et ne réduisent pas la rémunération minimale due au titre du projet. Les données et pièces exactes déjà légalement disponibles sont réutilisées ; aucune attestation distincte reproduisant les mêmes informations n'est exigée.",
    "Ces règles restent applicables aux situations éligibles dans le contrat unique, sans subordonner leur bénéfice à un terme de l'emploi. Les périodes sans mission demeurent prises en compte pour l'ancienneté dans les conditions de l'article R. 6323-9-1 ; elles ne sont pas assimilées à des heures de mission dans la référence salariale des 600 heures. La garantie mensuelle propre à l'emploi intérimaire demeure distincte.",
    "Le calcul subsidiaire s'applique aux demandes en cours et futures à compter de l'entrée en vigueur de la loi portant réforme du contrat de travail. Les décisions favorables, rémunérations et créances déjà acquises au titre de contrats antérieurs sont conservées."
)
answer[8]['reason'] = "Coordination supplémentaire nécessaire : le retrait des 600 heures d'ancienneté dans l'entreprise prévu par la proposition actuelle de R. 6323-9-1 ne peut être neutralisé par une base de salaire impossible à établir chez un nouvel employeur. La référence existante de 600 heures dans l'entreprise est conservée lorsqu'elle existe ; à défaut, une base subsidiaire de missions dans la branche est expressément instituée, limitée aux heures disponibles si elles sont inférieures à 600. Le cas sans aucune mission utilise la garantie mensuelle contractuelle, afin que des intermissions admises pour l'ancienneté n'aboutissent pas à une base introuvable. Ces règles sont des propositions normatives supplémentaires, pas des formules attribuées à la source. Les composantes spectacle et les éléments et exclusions de salaire intérimaire sont maintenus. Les calculs subsidiaires ajoutent une complexité et des besoins documentaires possibles, sans gain net fictif."
answer[8]['review_notes'] = "La source juxtapose déjà une ancienneté de 600 heures d'entreprise OU de groupe dans R. 6323-9-1 et une base salariale limitée à l'entreprise dans le présent II : l'absence de base chez l'entreprise dépositaire est une lacune préexistante pour certains membres du groupe. La nouvelle proposition de la cible retire entièrement le seuil d'entreprise/groupe ; le calcul subsidiaire résout explicitement cette difficulté et n'exige pas de nouvelles missions avant la formation. Les 1 600 heures de branche sur dix-huit mois restent une condition d'accès dans la cible, les 600 heures du présent texte une référence salariale, sans confusion. Ne pas incorporer les intermissions à cette base horaire. Le I inclut les indemnités de congés spectacles, le II exclut l'indemnité compensatrice de congés payés intérimaire. Le recours aux salaires d'autres entreprises peut nécessiter des éléments supplémentaires et ne crée aucun accès nouveau aux données. Aucun minimum légal de rémunération ni garantie intérimaire autonome n'est supprimé."

answer[9]['proposed_xml'] = paragraphs(
    "L'employeur adresse à l'opérateur de compétences, par voie dématérialisée, les éléments nécessaires à sa décision de prise en charge de la période de reconversion :",
    "1° L'accord écrit qui fixe la durée de la reconversion interne mentionnée au I de l'article L. 6324-3 ou les modalités de suspension du contrat pendant la reconversion externe mentionnée au II de cet article ;",
    "2° La convention mentionnée à l'article L. 6353-1. Elle peut figurer dans le même document que l'accord du 1°, dès lors que ce document contient les éléments requis pour chacun. Aucune annexe distincte ni nouvelle signature reproduisant le même engagement n'est exigée ;",
    "3° Abrogé ;",
    "4° Les seules pièces complémentaires nécessaires pour vérifier les critères du 1° bis du I de l'article L. 6332-1 qui ne résultent pas des éléments déjà légalement disponibles pour l'opérateur. Toute demande complémentaire précise le critère à vérifier et les informations manquantes correspondantes. Elle ne peut rétablir une transmission systématique du contrat de travail complet avec l'entreprise d'accueil ; seuls les éléments de ce contrat nécessaires à une vérification identifiée peuvent être demandés.",
    "L'opérateur réutilise les accords, conventions et autres pièces exactes et à jour dont il dispose légalement. Leur dépôt antérieur vaut transmission au titre du présent article ; aucune copie supplémentaire ni attestation reproduisant les mêmes informations n'est exigée.",
    "Le dépôt n'est pas limité aux trente jours précédant le début de la reconversion. Il peut intervenir avant ou pendant cette période. Son seul caractère extérieur à cette ancienne fenêtre ne justifie ni refus de prise en charge ni perte des droits correspondants. Le délai de décision prévu à l'article R. 6324-2 et les conditions de fond du financement demeurent applicables.",
    "Pour les emplois conclus à compter de l'entrée en vigueur de la loi instituant le contrat unique, le contrat avec l'entreprise d'accueil est à durée indéterminée. La durée de reconversion et celle de la suspension du contrat d'origine ne fixent pas un terme à cet emploi. Les contrats antérieurs et les droits attachés aux avenants de reconversion ou de promotion par l'alternance conclus avant le 1er janvier 2026 sont conservés dans leur champ transitoire.",
    "Les simplifications de dépôt s'appliquent aux demandes en cours et aux demandes nouvelles à compter de l'entrée en vigueur de la loi portant la présente réforme, sans nouveau dépôt des dossiers déjà transmis et sans reprise des délais d'instruction."
)
answer[9]['reason'] = "Réforme de fond : suppression déjà acquise de la fenêtre de trente jours, puis retrait supplémentaire du dépôt systématique du contrat d'accueil complet et de l'annexe distincte pour une convention pouvant être réunie à l'accord. La vérification ciblée ne doit pas reconstituer ce dépôt général. Les compléments sont limités aux critères légaux et doivent être explicités : cette obligation de précision pour l'opérateur est recensée comme une charge ajoutée, dans un résultat mixte. Restent nécessaires le consentement écrit, la convention de formation, les conditions de prise en charge et les garanties du contrat suspendu. L'emploi d'accueil nouveau reste indéterminé."
answer[9]['review_notes'] = "La fenêtre source est celle des trente jours précédant le début, pas un préavis minimal de trente jours. R. 6324-2, lu au corpus, conserve vingt jours pour décider ; R. 6324-3 conserve refus motivé, notification et contrôles. L. 6353-1 et D. 6353-1, lus au corpus hors des cibles fournies, conservent leurs exigences de convention ; le document commun doit les satisfaire sans nouveau support. L. 6332-1, également lu hors cibles, garde au 1° bis du I les critères de financement et la dotation. L. 6324-3 proposé retire le CDD d'au moins six mois et l'essai obligatoire, au profit d'un essai seulement stipulé dans le régime commun : aucun dépôt ne peut les rétablir. La note source du décret 2026-39 attribue de façon ambiguë la survivance aux avenants antérieurs au 1er janvier 2026 ; la note législative de L. 6324-3 distingue l'ancienne rédaction. L'article 4 de ce décret extérieur doit être clarifié dans la transition générale, sans prétendre le réécrire ici."

answer[10]['reason'] = "Abrogation intégrale déjà proposée et confirmée après seconde passe : retrait du dépôt central de l'accord et de la transmission des refus et motifs au ministère. Le financement reste instruit par l'opérateur et le refus reste motivé et notifié aux parties ; ce second circuit n'a pas de fonction essentielle démontrée dans le lot. Aucun dépôt, registre ou déclaration équivalente ne le remplace. Les données légalement conservées, contrôles et recours restent à leur fondement autonome ; aucune coupe supplémentaire fictive n'est ajoutée à une obligation déjà entièrement retirée par le brouillon."
answer[10]['review_notes'] = "R. 6324-1 à R. 6324-3 et R. 6323-32 ont été lus au corpus ; ces renvois complémentaires ne sont pas des cibles fournies supplémentaires. L'abrogation n'abolit ni la convention de L. 6324-3 ni le SI-CPF, y compris sa fonction distincte relative aux élus locaux et ses responsables de traitement. Coordonner les spécifications du traitement et les instructions aux opérateurs pour ne plus exiger ce dépôt, sans effacer illégalement les archives. La note transitoire du décret 2026-39 présente l'ambiguïté exposée pour R. 6324-1 ; aucun futur rattrapage n'est exigé sur le fondement abrogé, même pour les dossiers anciens. Aucun accord individuel ni aide éligible future n'est annulé."

answer[11]['proposed_xml'] = paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant la présente réforme. L'obligation spéciale de conclure et de signer une convention de professionnalisation sur le fondement du présent article est supprimée, sans document ni signature de remplacement.",
    "Les actions d'accompagnement et les enseignements mentionnés à l'article L. 6325-13 demeurent soumis aux obligations de formation, d'évaluation et de qualification qui leur sont applicables et à la convention de droit commun prévue à l'article L. 6353-1, dans les conditions de cet article. Aucune convention supplémentaire n'est requise sur le fondement du présent article abrogé.",
    "Cette suppression s'applique aux conventions restant à conclure et aux signatures restant à recueillir à cette date, y compris dans les dossiers en cours. Les conventions déjà valablement conclues, les prestations convenues, les rémunérations, les financements et les créances acquis restent régis par leurs stipulations et leurs règles applicables. Aucune convention antérieure n'est annulée et aucun remboursement n'est exigé du seul fait de cette abrogation.",
    "Les aides, exonérations et droits de formation demeurent ouverts aux situations éligibles futures. Pour les emplois conclus à compter de l'entrée en vigueur de la loi instituant le contrat unique, la phase de professionnalisation se déroule dans un contrat unique à durée indéterminée ; sa durée pédagogique et celle de la convention de formation ne fixent pas de terme à l'emploi. Les contrats de travail antérieurs conservent leur régime transitoire."
)
answer[11]['reason'] = "Abrogation de fond supplémentaire par rapport au brouillon : retrait complet du fondement réglementaire spécial imposant une convention signée de professionnalisation. La convention générale de L. 6353-1 et ses modalités D. 6353-1, qui admettent déjà certains devis ou bons de commande, conservent la contractualisation utile ; L. 6325-13 maintient la formation et l'évaluation. La source n'imposait pas nécessairement deux documents : aucun double dépôt universel n'est donc inventé. L'allègement est le retrait d'une obligation spéciale autonome, avec ses signatures et mentions propres, sans document de substitution ni atteinte aux prestations convenues. Le contrat unique, les anciens contrats et les aides futures restent coordonnés."
answer[11]['review_notes'] = "L. 6353-1 et D. 6353-1, lus intégralement au corpus, ne sont pas fournis comme cibles ; ils sont expressément identifiés comme fondements autonomes maintenus, et non présentés comme nouvellement créés. D. 6353-1 prévoit déjà la convention des actions financées, ses contenus et les équivalences de devis/commandes dans leur champ, ainsi que le régime CPF. La suppression de D. 6325-12 ne supprime aucune de ces règles générales. L. 6325-13 conserve positionnement, évaluation, accompagnement et enseignements ; sa proposition applique les 15 % à 25 % et le minimum de 150 heures à la phase pédagogique, pas à une durée d'emploi. Les contrats, prestations et consentements déjà acquis ne sont pas libérés rétroactivement. Les modèles et circuits exigeant une convention supplémentaire sur ce seul fondement doivent être retirés ; ils ne sont pas prétendus tous réécrits ici. Aucun gain nouveau n'est revendiqué pour un dossier où un document unique satisfaisait déjà les deux textes."

reductions = {
    0: ["Suppression des prévenances obligatoires de cent vingt et soixante jours avant le début de la formation.", "Suppression des mentions distinctes obligatoires de l'intitulé et de la date de l'examen dans la demande de congé.", "Suppression de la retransmission à l'employeur des informations exactes et à jour déjà communiquées."],
    1: ["Suppression de l'accord de congé comme condition préalable au dépôt de la demande de financement.", "Retrait de la restriction d'accès liée au CDD et des cinq exclusions de périodes pour la voie des quatre mois, en coordination avec D. 6323-9."],
    2: ["Suppression du dépôt obligatoire de la demande dans les quatre mois suivant la fin du contrat ou de la mission.", "Suppression de l'obligation de commencer la formation dans les six mois suivant cette fin."],
    3: ["Suppression coordonnée de la limite de six mois après la fin du contrat pour commencer la formation financée."],
    4: ["Suppression de la condition de réemploi, du délai d'un mois et de l'accord d'un nouvel employeur comme conditions de maintien du financement après rupture par le bénéficiaire.", "Suppression du justificatif distinct obligatoire de rupture à transmettre par le bénéficiaire, sans formulaire équivalent."],
    6: ["Suppression du recours obligatoire à un nouveau contrat de mission à durée déterminée pour l'affectation en formation dans l'emploi nouveau.", "Suppression de la copie intégrale imposée du bulletin de paie au profit des seuls éléments probants nécessaires au remboursement.", "Suppression de la facture distincte exigée pour la première avance, réunie avec la demande déjà nécessaire.", "Suppression des nouvelles transmissions de pièces exactes et à jour déjà légalement disponibles, sans gain CRPA supplémentaire revendiqué."],
    7: ["Retrait coordonné de la restriction aux salaires de CDD et des exclusions de périodes pour les ouvertures élargies par D. 6323-9, sous maintien du calcul ancien plus favorable."],
    9: ["Suppression de la fenêtre de dépôt limitée aux trente jours précédant le début de la reconversion.", "Suppression de l'annexe distincte obligatoire lorsque l'accord et la convention figurent dans un document commun complet.", "Suppression du dépôt systématique du contrat de travail complet avec l'entreprise d'accueil.", "Retrait du pouvoir de demander indistinctement tout autre document sans nécessité rattachée à un critère de financement."],
}
for i, removed in reductions.items():
    answer[i].update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19', removed_provisions=removed)
for i, scope in {
    10: "Suppression de tout dépôt ministériel de l'accord de reconversion et de toute transmission ministérielle des refus et de leurs motifs sur le fondement de R. 6324-4, y compris les transmissions restant à effectuer pour dossiers anciens.",
    11: "Suppression intégrale de l'obligation réglementaire spéciale de convention signée de professionnalisation prévue à D. 6325-12, de ses mentions et signatures propres pour les actes restant à accomplir, avec maintien des conventions de droit commun et des engagements antérieurs."
}.items():
    answer[i].update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19', repeal_scope=scope)

# Each item below is an analysis of the required view, not an assertion that its
# proposed text is current law. The mapping is deliberately exact per referrer.
core = [
    (
        "R. 6323-10 organise un congé, pas une rupture : les prévenances de 120/60 jours supprimées ne sont pas les préavis de L. 1234-1. La vue proposée réserve quinze jours calendaires aux nouveaux contrats et conserve pour les anciens les durées selon six mois/deux ans et les règles plus favorables. La notification de rupture, comptée du lendemain selon L. 1234-3 lu au corpus, reste distincte de la demande de congé.",
        "L. 1221-2 proposé interdit le terme automatique des nouveaux emplois, y compris intérimaires. La durée de l'absence et de l'action de formation de R. 6323-10 ne devient donc pas une durée d'emploi. Les contrats antérieurs restent au régime transitoire, sans nouveau CDD ni renouvellement autorisé par cette procédure de congé.",
        "L. 1234-9 ne règle pas l'ancienneté d'accès au congé. Sa proposition ouvre l'indemnité ordinaire patronale à un an au terme effectif, préavis inclus, puis calcule 0,20 mois sur toute l'ancienneté avec fractions en mois complets et plafond de six mois. Aucun de ces seuils ne remplace les conditions et dispenses de formation du IV ; les salaires et garanties spéciales restent distincts."
    ),
    (
        "L'autorisation patronale de congé visée ici ne constitue pas une notification de rupture. L. 1234-1 proposé fixe quinze jours calendaires pour les emplois nouveaux mais maintient les anciens préavis ; ce délai ne conditionne ni le dépôt à la commission ni l'accord tacite sous trente jours de R. 6323-10.",
        "L. 1221-2 proposé ouvre uniquement des emplois nouveaux à durée indéterminée. R. 6323-11-1 retire donc la restriction au CDD et conserve la faculté de demande pendant le contrat unique, y compris pour les activités futures. Les anciens contrats demeurent recevables, et l'accès financier n'autorise ni nouveau CDD ni renouvellement.",
        "L'ancienneté de formation reste celle de D. 6323-9, appréciée au départ, avec ses dispenses ; elle n'est pas l'année d'ouverture de l'indemnité ordinaire de L. 1234-9 proposé. Cette dernière ne concerne que la rupture patronale, avec préavis inclus au terme et calcul sur l'ancienneté totale. Le dépôt financier ne déclenche aucune indemnité ni renonciation aux anciens droits."
    ),
    (
        "La fin d'une mission utilisée par R. 6323-11-2 n'est pas le licenciement régi par L. 1234-1. Si l'emploi nouveau est réellement rompu, les quinze jours calendaires et la notification restent requis dans leur champ ; les anciens préavis subsistent pour les contrats antérieurs. La suppression des quatre/six mois ne raccourcit aucune procédure collective.",
        "L. 1221-2 proposé exclut qu'une dernière mission rompe automatiquement le nouveau contrat. R. 6323-11-2 distingue par conséquent fin de mission et fin effective d'emploi pour ouvrir la demande, sans rouvrir le CDD. L'ancienneté de formation et les périodes issues de contrats antérieurs demeurent utilisables.",
        "Les quatre et six mois source sont des délais de formation, sans rapport avec l'indemnité de L. 1234-9. Pour le contrat unique rompu par l'employeur, la vue impose un an au terme effectif préavis inclus, puis 0,20 mois par année totale, prorata de mois complets et plafond de six mois ; aucune fin de mission ou demande de financement ne suffit à ouvrir cette créance."
    ),
    (
        "R. 6323-14-1 finance la période postérieure à la fin effective du contrat ; il ne fixe pas le point de départ de cette rupture. L. 1234-1 proposé conserve les préavis anciens et prévoit quinze jours calendaires pour l'emploi nouveau. Leur notification et leur exécution éventuelle doivent être distinguées du début de formation désormais sans délai de six mois dans le lot.",
        "Le renvoi à R. 6323-11-1 ne peut rester réservé à un terme de CDD puisque L. 1221-2 proposé impose l'emploi indéterminé nouveau. Le I vise donc toute fin effective admissible ; le II maintient le statut de stagiaire sans rupture automatique d'un contrat continué. Les droits des contrats antérieurs et des futures situations éligibles sont conservés.",
        "La rémunération de stagiaire et les cotisations du II ne sont pas l'indemnité ordinaire de L. 1234-9 proposé. Le zéro avant un an, le seuil au terme préavis inclus et le calcul sur toute l'ancienneté avec plafond de six mois ne permettent de supprimer aucune rémunération de projet ni protection sociale. Les anciennes composantes et indemnités spéciales restent à leur régime."
    ),
    (
        "L'ancien délai d'un mois après la fin du préavis au 2° du II est une condition de réemploi, pas le préavis de L. 1234-1. Le retrait entier de cette condition ne modifie ni les quinze jours calendaires du nouvel emploi, comptés selon notification, ni les préavis anciens, ni les autorisations et procédures collectives distinctes.",
        "L. 1221-2 proposé interdit tout nouveau terme d'emploi. Le II de R. 6323-14-3 ne subordonne plus le maintien de la prise en charge à un réemploi ; si le bénéficiaire retrouve un emploi nouveau, ce sera un contrat unique indéterminé, avec congé pour la formation sur temps de travail. Ni la poursuite du projet ni son achèvement ne rompent cet emploi.",
        "Le financement maintenu après rupture par le bénéficiaire ne crée pas l'indemnité patronale de L. 1234-9 proposé. Une démission ordinaire n'ouvre pas cette indemnité ; le seuil d'un an à la fin effective préavis inclus et les 0,20 mois par année totale plafonnés à six mois ne conditionnent pas les cinq postes de financement du I, tous conservés."
    ),
    (
        "D. 6323-18-2 change le payeur après cessation effective, sans raccourcir la rupture. La vue de L. 1234-1 maintient les anciens préavis et fixe quinze jours calendaires dans le contrat nouveau. Un salarié encore en préavis ou simplement sans mission peut rester employé : il ne doit pas être traité comme déjà sorti pour le seul circuit de versement.",
        "L. 1221-2 proposé supprime le terme automatique des nouveaux contrats. Le renvoi au terme du CDD est donc remplacé par la fin effective de l'emploi, tandis que la seule fin de mission ne déclenche pas le versement post-emploi. Les anciens CDD gardent leur régime et les nouveaux bénéficiaires en contrat unique conservent l'accès à la rémunération.",
        "La commission verse ici la rémunération de formation, non l'indemnité de rupture de L. 1234-9. Le défaut d'un an d'ancienneté au terme effectif préavis inclus n'efface pas cette rémunération. Le barème proposé de 0,20 mois par année totale, fractions en mois complets et plafond de six mois reste limité à l'indemnité patronale ordinaire et ne change pas le payeur du projet."
    ),
    (
        "La lettre de mission pédagogique du II ne notifie pas une rupture au sens de L. 1234-1. La fin de formation ne dispense pas du préavis nouveau de quinze jours calendaires ni de sa notification, et les préavis des anciens contrats restent distincts. Le mois de remboursement du III et les trente jours d'avance du IV sont des délais de financement, non de séparation.",
        "L. 1221-2 proposé interdit tout nouveau CDD de mission : le II ne peut conserver l'obligation d'en établir un pour la formation. Il retient l'affectation par lettre dans l'emploi indéterminé, sans nouvel essai, tandis que les missions antérieures gardent leur terme et leurs droits jusqu'à leur échéance sans nouveau renouvellement après réforme.",
        "Les avances, rémunérations et cotisations du présent article ne sont pas plafonnées par L. 1234-9. Sa proposition exige pour l'indemnité patronale ordinaire un an au terme effectif préavis inclus, puis compte toute l'ancienneté à 0,20 mois avec fractions en mois complets et plafond de six mois. Aucune ancienneté n'est remise à zéro lors de l'affectation ou de la conversion, et les droits anciens restent séparés."
    ),
    (
        "Les périodes de douze et quatre mois de D. 6323-18-3 servent à calculer une rémunération de formation ; elles ne remplacent ni les préavis anciens ni les quinze jours calendaires de L. 1234-1 proposé. Une demande ou une fin de phase pédagogique ne constitue pas la notification écrite de rupture dont le délai se compte du lendemain dans le contrat unique.",
        "L. 1221-2 proposé ne permet plus de produire de nouveaux mois en CDD. Le III doit donc ouvrir la moyenne de quatre mois aux services éligibles du contrat unique et aux périodes désormais admises par D. 6323-9. L'emploi ne prend pas fin avec cette période de référence, et la conversion conserve les périodes acquises sans double compte.",
        "Le salaire moyen de référence du projet n'est pas le salaire de référence de l'indemnité de L. 1234-9. Les douze/quatre mois et les conditions d'accès à formation restent distincts de l'année d'ancienneté au terme effectif préavis inclus, du taux de 0,20 mois sur toute l'ancienneté et du plafond de six mois. La sauvegarde du calcul ancien favorable ne plafonne aucun dommage ou indemnité spéciale."
    ),
    (
        "Les 600 heures de mission de R. 6323-18-3-1 constituent une base salariale ; elles ne sont pas une durée de préavis. L. 1234-1 proposé fixe quinze jours calendaires pour le contrat nouveau après notification et conserve les anciens préavis. La fin de mission ou l'entrée en formation ne suffit donc pas à mettre fin à l'emploi ou à ouvrir son préavis.",
        "L. 1221-2 proposé permet des missions limitées dans un emploi indéterminé, pas un nouveau CDD. Les règles de salaire du I et du II demeurent donc accessibles aux futures situations éligibles dans le contrat unique ; la prise en compte des intermissions pour l'ancienneté ne transforme pas celles-ci en heures de mission ni en terme d'emploi.",
        "L. 1234-9 proposé régit une indemnité patronale ordinaire, distincte de la moyenne de salaire du présent article. Son année d'ancienneté s'apprécie au terme effectif avec préavis inclus, puis le calcul porte sur toute l'ancienneté à 0,20 mois, fractions de mois complets, plafond de six mois. Le calcul subsidiaire de formation ne déclenche pas cette indemnité et n'efface aucune garantie spéciale ou ancienne."
    ),
    (
        "La fenêtre source de trente jours pour déposer les pièces de reconversion n'est pas le préavis de L. 1234-1. Sa suppression ne permet pas de rompre le contrat d'origine suspendu sans notification et préavis applicables ; le contrat nouveau relève des quinze jours calendaires et les anciens gardent leur régime, avec protections collectives distinctes.",
        "Le 3° source demandait un contrat d'accueil pouvant être CDD selon l'ancien L. 6324-3 ; L. 1221-2 proposé impose désormais un emploi nouveau indéterminé. La suppression de son dépôt systématique ne change pas cette condition de fond. La durée de reconversion et la suspension du contrat d'origine ne sont jamais un terme de l'emploi d'accueil.",
        "L. 1234-9 proposé ne s'applique pas du seul fait de la suspension pour reconversion ou d'un retour anticipé. Son indemnité ordinaire patronale suppose une rupture et un an au terme effectif avec préavis inclus ; le calcul de 0,20 mois par année totale, prorata des mois complets et plafond de six mois reste distinct des financements, rémunérations et anciens droits conservés par R. 6324-1."
    ),
    (
        "L'abrogation du dépôt ministériel de R. 6324-4 ne supprime aucune notification de rupture. L. 1234-1 proposé maintient les anciens préavis et les quinze jours calendaires nouveaux ; le refus de financement doit encore être motivé et notifié aux parties selon R. 6324-3, procédure distincte de la rupture individuelle et de ses protections.",
        "L. 1221-2 proposé continue d'imposer le contrat unique indéterminé pour les nouveaux emplois d'accueil. Supprimer le dépôt central de l'accord ne supprime ni son consentement ni cette condition, et ne rétablit pas le CDD de L. 6324-3 officiel. Les anciens accords et contrats conservent leurs droits ; la fin de la période de reconversion ne rompt pas l'emploi nouveau.",
        "Le retrait d'une transmission au ministère n'affecte pas L. 1234-9 proposé : l'indemnité ordinaire reste patronale, sans ouverture avant un an au terme effectif préavis inclus, puis à 0,20 mois par année totale avec prorata des mois complets et plafond de six mois. Les anciennes composantes, les rémunérations de reconversion et les indemnités spéciales ne sont pas supprimées par l'abrogation documentaire."
    ),
    (
        "L'abrogation de la convention spéciale de D. 6325-12 n'abroge pas le préavis du contrat de travail. L. 1234-1 proposé maintient les anciens préavis et prévoit quinze jours calendaires dans le contrat nouveau, avec notification et procédures distinctes. L'échéance d'une convention pédagogique ne constitue ni licenciement ni notification de rupture.",
        "L. 1221-2 proposé exclut le CDD de professionnalisation nouveau : la convention générale de formation maintenue porte sur une phase pédagogique dans l'emploi indéterminé. L'abrogation ne permet pas de fixer le terme de cet emploi. Les anciens contrats restent au régime transitoire, et les aides futures éligibles ne sont pas réservées aux anciens CDD.",
        "L. 1234-9 proposé ne limite aucune dépense de formation du fait de l'abrogation. Son zéro avant un an, apprécié au terme effectif préavis inclus, puis 0,20 mois sur l'ancienneté totale avec prorata des mois complets et plafond de six mois ne concernent que l'indemnité ordinaire patronale. Les rémunérations, conventions acquises et indemnités spéciales restent à leur champ propre."
    ),
]

extra = {
    0: {
        'LEGIARTI000006901251': "Le dernier alinéa de R. 6323-10 désigne comme destinataire l'entreprise de travail temporaire définie par L. 1251-2, qui recrute et rémunère le salarié, et non l'entreprise utilisatrice. La proposition cible étend le contrat unique aux nouveaux recrutements et réserve les garanties d'intermission et de rémunération. Le congé et sa notification n'exigent aucun nouveau CDD de mission."
    },
    1: {
        'LEGIARTI000041393503': "R. 6323-10 proposé distingue le congé sur temps de travail du dépôt de financement : demande écrite sans prévenance minimale, réponse sous trente jours, accord tacite et refus motivé. R. 6323-11-1 permet le dépôt avant cette réponse sans autoriser l'absence d'office. La présente version de R. 6323-10 retire en plus les mentions distinctes d'examen ; ni cette coupe ni les anciennes prévenances ne peuvent être réintroduites par le dossier financier.",
        'LEGIARTI000045369571': "D. 6323-9 officiel conserve deux voies et cinq exclusions ; sa proposition actuelle retire la condition de CDD pour les quatre mois et toutes les exclusions 1° à 5°, y compris pour les périodes anciennes dans les demandes en cours ou futures. Le présent troisième alinéa est rectifié en conséquence : le brouillon ne pouvait conserver 1° à 4°. Restent vingt-quatre mois sur cinq ans dont quatre sur douze, la voie vingt-quatre/douze, les dispenses et l'appréciation au départ en formation."
    },
    2: {
        'LEGIARTI000040340619': "R. 6323-9-1 distingue l'ancienneté spectacle au I, l'intérim au II et la date de départ en formation au III. Sa proposition retire les 600 heures dans l'entreprise/groupe mais conserve 1 600 heures de branche sur dix-huit mois avec intermissions et les seuils spectacle 220 puis 130/65, 88/44 ou 60/30 selon l'activité. Retirer les délais de quatre/six mois ne supprime aucune de ces fenêtres ni dispense ; aucune mission ne termine l'emploi unique."
    },
    3: {
        'LEGIARTI000038007569': "R. 6323-11-1 officiel visait le CDD ; la vue proposée ouvre le contrat unique et le dépôt avant la réponse au congé. Dans ce lot, le texte est de plus aligné sur D. 6323-9 actuel, sans exclusions 1° à 5°. Le renvoi du I maintient donc le financement post-emploi pour toutes les situations éligibles, pas seulement les anciens CDD, sans considérer une mission terminée comme une rupture du contrat ni imposer un accord financier patronal supplémentaire."
    },
    4: {
        'LEGIARTI000038007617': "R. 6323-14-1 maintient la rémunération et la protection sociale du stagiaire après la cessation effective de l'emploi ; sa vue fournie conservait six mois mais la présente proposition de lot retire cette limite en coordination avec R. 6323-11-2. Le II de R. 6323-14-3 peut dès lors maintenir un financement après rupture par le bénéficiaire sans exiger un réemploi. Ce maintien n'est pas une nouvelle indemnité de rupture et ne crée pas de double rémunération.",
        'LEGIARTI000041393503': "Le nouvel employeur reste compétent pour le seul congé sur son temps de travail selon R. 6323-10 : écrit, trente jours de réponse et autorisation tacite à défaut. La suppression de la condition de réemploi et de son délai dans R. 6323-14-3 ne supprime pas ce congé lorsqu'un nouvel emploi existe. La notification de la rupture précédente et l'accord initial de financement restent des faits distincts à dater."
    },
    5: {
        'LEGIARTI000038007617': "D. 6323-18-2 renvoie à la prise en charge après fin effective d'emploi organisée par le I de R. 6323-14-1 et à la rémunération garantie de son II. La vue cible conservait six mois ; cette limite est retirée dans le lot et ne peut survivre dans le renvoi. Le statut de stagiaire et les garanties sociales ne cessent pas avec le CDD et restent ouverts après le contrat unique, sans double versement pour la même période.",
        'LEGIARTI000040340741': "R. 6323-18-2-1 réserve le versement mensuel direct par la commission au spectacle du I ; l'intérim du II/III passe par l'employeur remboursé, avec les avances de moins de cinquante salariés plafonnées à 90 %. Ces modalités d'emploi maintenu restent distinctes du versement post-emploi de D. 6323-18-2. La lettre de formation ne rompt pas le contrat ; la copie intégrale de paie et la facture distincte sont retirées dans la présente version du lot."
    },
    6: {
        'LEGIARTI000037379970': "La source cite erronément « L. 125158-1 » ; la cible L. 1251-58-1 confirme la lettre de mission au 2° et le contrat de mise à disposition au 1°. Sa proposition impose le CDI nouveau et conserve ancienneté et garanties des CDI antérieurs. Le II rectifie le numéro et utilise la lettre pour l'affectation pédagogique, sans nouveau terme, nouvel essai ou contrat de mise à disposition commercial fictif pendant la formation.",
        'LEGIARTI000038952026': "L. 1251-57 assimile à des missions les stages, bilans, VAE et certaines formations conventionnelles, sans imposer par lui-même un CDD. Le II conserve cette assimilation pour la formation du salarié temporaire et la formalise dans l'emploi indéterminé selon L. 1251-58-1. La proposition cible préserve les activités futures et les anciens contrats ; leur fin pédagogique n'est pas une rupture notifiée du contrat unique.",
        'LEGIARTI000040340619': "Le II source renvoie au III de R. 6323-9-1 pour l'ancienneté intérimaire, alors que ce III fixe seulement la date d'appréciation. Le renvoi est expressément corrigé vers le II, puis lu avec le III : 1 600 heures de branche sur dix-huit mois, intermissions pour le CDI, appréciation au départ. La proposition cible retire les 600 heures d'entreprise/groupe ; aucune exigence de ce type ne doit être reconstituée par la lettre de mission ou le remboursement."
    },
    7: {
        'LEGIARTI000038007569': "Le renvoi ajouté à R. 6323-11-1 dans le brouillon ne pouvait maintenir indirectement les exclusions 1° à 4°. La présente version de ce dernier suit toutes les périodes admises par D. 6323-9 et permet le dépôt avant réponse au congé. D. 6323-18-3 rattache directement le salaire à la voie de quatre mois du 2° du I, sans nouveau CDD ni condition de rupture ou d'accord patronal financier.",
        'LEGIARTI000045369571': "Les 1° et 2° source de D. 6323-18-3 sont précisés comme les 1° et 2° du I de D. 6323-9. La proposition cible supprime toutes les exclusions du II et ouvre les quatre mois indépendamment de la nature du contrat, avec services anciens et futurs ; le calcul doit suivre. Les douze mois et quatre mois restent deux voies, pas une libre option. Le calcul ancien plus favorable est garanti aux salariés également éligibles selon les anciennes conditions, avec une comparaison supplémentaire signalée."
    },
    8: {
        'LEGIARTI000040340619': "La proposition cible de R. 6323-9-1 supprime les 600 heures chez l'entreprise ou le groupe pour l'accès, tout en conservant 1 600 heures de branche sur dix-huit mois et les intermissions. Garder seulement une moyenne de 600 heures chez l'employeur pourrait refermer cet accès. Le II reçoit donc une base subsidiaire explicite dans la branche, puis sur les heures disponibles ou la garantie mensuelle sans mission. Ces nouvelles règles de calcul sont signalées, et les seuils et composantes propres au spectacle restent ceux du I."
    },
    9: {
        'LEGIARTI000052437338': "L. 6324-3 officiel prévoit au II un CDI ou un CDD d'au moins six mois avec essai ; sa proposition remplace le nouveau CDD par le contrat unique et rend l'essai seulement stipulé selon le régime commun. R. 6324-1 conserve l'accord interne du I et la suspension écrite du II sans nouveau terme d'emploi. Le contrat d'accueil complet n'est plus déposé systématiquement, mais les conditions de fond demeurent contrôlables. Les avenants antérieurs au 1er janvier 2026 gardent la rédaction antérieure selon la note législative, contrairement à la note réglementaire ambiguë."
    },
    10: {
        'LEGIARTI000052437338': "L'accord écrit de L. 6324-3 protège l'organisation et la rémunération de la reconversion interne, puis la suspension et le retour en reconversion externe. Son dépôt ministériel de R. 6324-4 n'est pas l'accord lui-même : seul le circuit est abrogé. Le contrat d'accueil nouveau reste indéterminé et l'essai facultativement stipulé selon la proposition cible. Les accords anciens, le régime des avenants d'avant le 1er janvier 2026 et les droits de financement demeurent, sans transmission de rattrapage."
    },
    11: {
        'LEGIARTI000033024376': "L. 6325-13 conserve positionnement, évaluation, accompagnement et enseignements, par prestataire ou service de formation de l'entreprise. Sa proposition rapporte les 15 % à 25 % et le minimum de 150 heures à la phase de professionnalisation, sans terme d'emploi. L'abrogation de la convention spéciale de D. 6325-12 ne supprime ni ces prestations ni leurs durées ni la convention générale de formation ; les anciens contrats et les aides futures éligibles demeurent protégés."
    },
}

core_ids = ['LEGIARTI000006901112', 'LEGIARTI000019071087', 'LEGIARTI000035644154']
for i, a in enumerate(answer):
    by_id = dict(zip(core_ids, core[i]))
    by_id.update(extra[i])
    key = a['code_id'] + '|' + a['source_id']
    checks = []
    for target_key in refs['requirements'][key]:
        target = refs['targets'][target_key]
        assessment = by_id.pop(target['source_id'])
        checks.append(dict(target_key=target_key, view_sha256=target['view_sha256'], assessment=assessment))
    assert not by_id, (i, by_id)
    a['reference_checks'] = checks

impacts = [
    (
        'material_reduction',
        "Par rapport à la source officielle entière, les deux prévenances de 120/60 jours et les mentions distinctes d'examen disparaissent ; la retransmission d'informations déjà reçues par l'employeur privé est écartée. La décision de congé, ses motifs et les reports autonomes subsistent. Le retrait des mentions d'examen est supplémentaire par rapport au brouillon.",
        "La suppression de prévenance ne garantit pas une autorisation avant le début souhaité : trente jours de réponse et les reports distincts demeurent. Les conditions d'ancienneté et de financement ne sont pas abolies ; aucun effet national sur l'emploi ou les coûts n'est chiffré.",
        "Aucune charge nouvelle n'est identifiée : la demande écrite et ses informations restantes existent déjà, aucun formulaire, délai minimal ou autorisation de remplacement n'est créé. La phrase relative au contrat unique coordonne la durée d'emploi sans ajouter une démarche."
    ),
    (
        'material_reduction',
        "La source officielle entière subordonne l'action sur temps de travail à l'accord préalable et réserve cette voie au CDD. Le dépôt financier est désolidarisé de la réponse au congé et l'accès suit les périodes admises par D. 6323-9 proposé. La suppression des exclusions est une coordination de cette même mesure d'accès, pas cinq réductions indépendantes.",
        "L'absence sur temps de travail doit encore être autorisée expressément ou tacitement ; financement, vingt-quatre mois et fenêtres d'activité restent à leur champ, avec dispenses. L'impact budgétaire de l'accès élargi et l'ensemble des formulaires ne sont pas chiffrés ni prétendus coordonnés.",
        "Aucune charge nouvelle n'est identifiée dans cet article : pas de second accord financier, pas de nouvelle attestation, pas de taxe CPF-CDD de remplacement. Les justificatifs d'ancienneté demeurent ceux de la voie légale applicable ; l'emploi indéterminé découle de L. 1221-2 proposé."
    ),
    (
        'material_reduction',
        "La source officielle entière impose un dépôt dans les quatre mois et un début de formation dans les six mois après le terme. Les deux limites disparaissent pour les demandes en cours et futures ; seule la première était retirée par le brouillon. La demande après mission reste possible sans rupture du contrat unique.",
        "Les périodes de référence d'ancienneté appréciées au départ peuvent encore rendre un projet inéligible ; leur suppression n'est pas revendiquée. Les décisions définitives ne sont pas rouvertes. L'extension du nombre de projets finançables et son coût public restent inconnus.",
        "Aucune charge nouvelle n'est identifiée : aucun nouveau délai, justificatif, déclaration ou contrat ne remplace les deux limites. Le rappel de la date de départ en formation reprend le III existant de R. 6323-9-1, avec ses dispenses."
    ),
    (
        'coordination_only',
        "La comparaison avec toute la source montre la disparition du délai de début de six mois et de la restriction exclusive au CDD, tout en maintenant intégralement statut, rémunération, protection sociale et cotisations de garantie. Le délai est coordonné sous la même mesure que R. 6323-11-2 et ne représente pas un second gain autonome.",
        "Les conditions d'accès, le contrôle du financement et les règles de rémunération pendant un emploi maintenu subsistent. Aucun droit automatique à allocation chômage ni indemnité de rupture n'est créé. Le coût des projets supplémentaires n'est pas mesuré.",
        "Aucune charge nouvelle n'est identifiée : les cotisations versées par la commission existent dans la source et sont maintenues, pas transférées vers un nouveau financeur. Aucun dépôt ou délai de remplacement n'est ajouté à la suppression coordonnée des six mois."
    ),
    (
        'material_reduction',
        "Le maintien après rupture à l'initiative du bénéficiaire n'exige plus un nouveau contrat dans le mois ni l'accord d'un nouvel employeur comme condition financière. La pièce spéciale de rupture obligatoire est supprimée ; les faits nécessaires restent prouvables librement. Les cinq dépenses financées de la source entière restent dues dans leur champ.",
        "L'accord initial doit toujours précéder la décision de rupture, l'assiduité reste contrôlée et un nouvel emploi affecté exige le congé. Les décisions définitives ne sont pas rouvertes. Le supplément éventuel de dépenses de formation n'est ni mesuré ni compensé par une recette supposée.",
        "Aucune charge nouvelle n'est identifiée : la vérification de rupture remplace un justificatif spécial par des informations probantes libres, sans attestation imposée. L'autorisation de congé chez un nouvel employeur garde une obligation existante d'organisation du travail et n'est pas une déclaration financière de remplacement."
    ),
    (
        'coordination_only',
        "Par rapport à toute la source officielle, le versement post-emploi par la commission est conservé et son accès suit le contrat unique ; la référence exclusive au terme du CDD est retirée. Le même payeur et la même rémunération demeurent : il n'y a ni prélèvement supprimé ni transfert de financement démontré.",
        "La distinction entre emploi maintenu, intermittents, intérim et particuliers employeurs relève d'autres articles lus. Le présent texte ne diminue ni assiduité ni conditions de financement et ne chiffre aucun coût ou solde national. Aucun allègement autonome supplémentaire n'a été trouvé lors de la seconde passe.",
        "Aucune charge nouvelle n'est identifiée : l'article ne crée ni déclaration, ni registre, ni condition d'ancienneté, ni délai ; il conserve le payeur nécessaire et coordonne seulement les bénéficiaires avec le contrat unique et les droits antérieurs."
    ),
    (
        'mixed',
        "La copie intégrale de paie et la facture d'avance distincte sont réellement retirées par rapport à la source entière ; la demande existante comporte déjà le montant utile. Les autres preuves demeurent ciblées. Le nouveau CDI et la lettre d'affectation coordonnent le contrat unique, qui impose un emploi continu plutôt qu'une nouvelle mission à terme ; cette contrainte de régime est signalée sans solde net prétendu.",
        "Les cotisations, la mensualité spectacle, les seuils moins de cinquante salariés/90 %, le mois de remboursement et les trente jours d'avance subsistent. La dispense de pièces déjà disponibles reprend un droit de réemploi, sans gain CRPA nouveau. L'arrêté d'avances reste à coordonner et les coûts documentaires nets et d'emploi ne sont pas mesurés.",
        "La lettre remplace le contrat de mission dans l'emploi nouveau ; elle n'est pas supprimée et le CDI obligatoire est une contrainte de régime déjà décidée dans L. 1221-2/L. 1251-58-1 proposés. Les pièces manquantes restent nécessaires, mais aucun formulaire, donnée supplémentaire, registre ou attestation de remplacement n'est créé ici. Les demandes d'avance sont fusionnées avec la facture retirée, sans nouvelle échéance."
    ),
    (
        'mixed',
        "La restriction aux seuls salaires de CDD et les exclusions sont retirées pour suivre l'accès élargi de D. 6323-9, sans nouvelle réduction autonome comptée. Les douze/quatre mois sont conservés. La protection du calcul ancien plus favorable ajoute une comparaison pour certains dossiers ; cette complexité est recensée au lieu de prétendre à un allègement net établi.",
        "Le texte ne modifie pas les pourcentages de rémunération ni n'offre universellement le choix de la meilleure des moyennes de douze et quatre mois. Les comparaisons ne concernent que les salariés satisfaisant également aux anciennes conditions. Les coûts supplémentaires et le bilan national restent inconnus.",
        "Une charge de calcul supplémentaire est identifiée : vérifier le plancher ancien favorable lorsque les deux voies d'éligibilité sont satisfaites. Aucun nouveau dépôt ou registre n'est prescrit, mais des salaires historiques peuvent être nécessaires ; le réemploi n'ouvre aucun accès nouveau aux données. Le solde documentaire et financier net n'est pas établi."
    ),
    (
        'mixed',
        "Les composantes de salaire et exclusions de toute la source sont conservées. Un calcul subsidiaire explicite évite que la référence de 600 heures chez l'employeur fasse échec à l'accès élargi de R. 6323-9-1. Cette coordination ajoute des variantes de calcul et peut demander des salaires d'autres entreprises ; ce n'est pas présenté comme une suppression autonome de seuil ou un gain net de complexité.",
        "Les 600 heures restent la référence principale de salaire, pas un seuil d'accès recréé. La source ne contenait pas les variantes subsidiaires, dont la mise en œuvre comptable reste à coordonner ; aucun taux de rémunération nouveau n'est inventé. Les coûts, variations individuelles pour les nouveaux accès et effets publics ne sont pas chiffrés.",
        "Des charges nouvelles de calcul sont identifiées pour les dossiers sans 600 heures chez l'employeur : branche, heures disponibles puis garantie mensuelle sans mission. Des données salariales auparavant non nécessaires à cette entreprise peuvent être requises par la commission. Aucun registre ou formulaire nouveau n'est imposé et les pièces déjà disponibles sont réutilisées ; le solde net n'est pas établi."
    ),
    (
        'mixed',
        "Par rapport à la source entière, la fenêtre de trente jours est retirée, l'annexe obligatoire peut disparaître dans un document commun et le contrat d'accueil complet n'est plus déposé systématiquement. Le 4° ne permet plus des demandes indifférenciées. En contrepartie, l'opérateur doit préciser le critère et l'information manquante, obligation ajoutée recensée.",
        "Le délai de vingt jours pour décider, les conditions de financement, le consentement écrit et la convention de formation restent exigés. Des extraits du contrat peuvent être demandés pour un contrôle identifié. Les coûts pour opérateurs et employeurs, l'arrêté ou les formulaires et la transition du décret 2026-39 ne sont pas globalement soldés.",
        "L'obligation pour l'opérateur d'expliciter chaque complément constitue une charge nouvelle limitée, justifiée par le contrôle de nécessité. La fusion des supports ne crée pas une nouvelle convention ; le CDI d'accueil et l'essai commun suivent la réforme législative distincte. Aucun formulaire, registre ou transmission de remplacement du contrat complet n'est imposé. Le solde net national n'est pas établi."
    ),
    (
        'material_reduction',
        "L'intégralité de la source officielle instituant le dépôt ministériel de l'accord et l'information sur les refus est abrogée pour les transmissions à venir. Cette obligation de second circuit disparaît effectivement, sans dépôt équivalent. La coupe était déjà complète dans le brouillon et n'est pas annoncée comme une seconde économie supplémentaire.",
        "Les accords, l'instruction par l'opérateur, les refus notifiés aux parties, les contrôles et le SI-CPF à fondement autonome subsistent. L'inventaire des spécifications techniques n'est pas achevé par cette abrogation et aucune économie publique ou privée chiffrée n'est démontrée.",
        "Aucune charge nouvelle n'est identifiée : il n'y a ni déclaration centrale ni registre ni délai de remplacement, pas même pour rattraper un dossier ancien. La conservation légale des données existantes et la notification du refus aux parties reprennent des obligations autonomes maintenues."
    ),
    (
        'material_reduction',
        "Le fondement autonome de la convention spéciale signée et de ses mentions propres est intégralement retiré. La contractualisation générale de L. 6353-1 et les prestations de L. 6325-13 subsistent sur leurs fondements indépendants. La source ne prouvait pas deux documents dans tous les dossiers : seul le régime spécial est supprimé, sans gain fictif pour les supports déjà communs.",
        "Les obligations générales de convention, les exigences pédagogiques, les prestations et financements acquis restent applicables. Aucun coût chiffré ou double signature universel n'est affirmé. Les formulaires et modèles hors de l'article doivent cesser d'imposer ce seul fondement, sans être prétendus tous réécrits.",
        "Aucune charge nouvelle n'est identifiée : la convention générale existait déjà et ne constitue pas une nouvelle formalité de remplacement ; aucun registre, agrément ou déclaration n'est créé. Les contrats antérieurs restent exécutés et les avantages futurs éligibles restent ouverts."
    ),
]
for a, (classification, assessment, limitations, burdens) in zip(answer, impacts):
    a['substantive_impact'] = dict(version=1, classification=classification, assessment=assessment,
        scope_limitations=limitations, new_burdens_review=burdens, effects=[])

def effect(i, kind, measure, description, before, after, unit, population, transition, burdens, sq, pq):
    answer[i]['substantive_impact']['effects'].append(dict(
        kind=kind, measure_id=measure, description=description, before=before, after=after,
        unit=unit, affected_population=population, conditions_and_transition=transition,
        replacement_or_new_burdens=burdens, source_quote=sq, proposed_quote=pq))

effect(0, 'deadline_reduced', 'ptp-conge-suppression-prevenances',
    "Retrait des deux délais minimaux de présentation du congé.",
    "Demande écrite au moins 120 jours avant une interruption continue d'au moins six mois, ou 60 jours pour une interruption plus courte ou à temps partiel.",
    "Aucun délai minimal avant le début ; demande écrite préalable au début toujours nécessaire.", 'calendar_days',
    "Salariés demandant un congé de transition professionnelle, y compris les salariés temporaires.",
    "Demandes nouvelles ou en cours à l'entrée en vigueur ; pas de réouverture des décisions définitives, reports autonomes maintenus.",
    "Aucune échéance de remplacement ; réponse sous trente jours et autorisation expresse ou tacite maintenues.",
    "Cent vingt jours avant le début de l'action de formation lorsque la réalisation de celle-ci entraîne une interruption continue de travail d'au moins six mois",
    "Aucun délai minimal de présentation de la demande avant ce début n'est exigé.")
effect(0, 'obligation_removed', 'ptp-conge-mentions-examen-supprimees',
    "Retrait des deux mentions distinctes obligatoires d'examen.",
    "Intitulé et date d'examen exigés distinctement en plus de l'identification de la formation et de sa durée.",
    "La formation est identifiée par son début, sa désignation, sa durée et son organisme ; aucun intitulé ou date d'examen distinct obligatoire.", 'legal_duty',
    "Demandeurs du congé, quel que soit leur contrat.",
    "Demandes nouvelles et non définitivement décidées à l'entrée en vigueur ; le droit à l'examen n'est pas retiré.",
    "Aucune mention ou attestation équivalente de remplacement.",
    "l'intitulé et la date de l'examen concerné.",
    "L'intitulé et la date de l'examen ne constituent pas des mentions obligatoires distinctes.")
effect(0, 'compliance_cost_reduced', 'ptp-conge-retransmission-employeur-supprimee',
    "Dispense de retransmettre au destinataire privé des informations exactes déjà reçues.",
    "Le II exige le contenu complet dans la demande sans dispense expresse des informations déjà communiquées à l'employeur.",
    "Pas de seconde transmission des mêmes informations exactes et à jour à l'employeur.", 'legal_duty',
    "Salariés et employeurs destinataires d'une demande de congé.",
    "Demandes en cours et nouvelles à l'entrée en vigueur ; les informations manquantes nécessaires restent à fournir.",
    "Aucun accès nouveau aux données, ni formulaire ou attestation de réemploi ; coût monétaire non chiffré.",
    "La demande de congé indique la date du début de l'action de formation, la désignation et la durée de celle-ci ainsi que le nom de l'organisme qui en est responsable",
    "Les informations exactes et à jour déjà communiquées à l'employeur n'ont pas à lui être transmises une seconde fois.")

effect(1, 'obligation_removed', 'ptp-depot-financement-sans-attente-conge',
    "Dépôt du dossier financier sans attendre l'autorisation d'absence.",
    "Pour une formation sur temps de travail, accord préalable de l'employeur dans la source et dépôt après accord selon R. 6323-11.",
    "La commission peut recevoir la demande avant la réponse au congé ; l'absence reste autorisée expressément ou tacitement.", 'legal_duty',
    "Salariés déposant une demande pendant l'emploi, anciens contrats et contrat unique.",
    "Demandes en cours et nouvelles à l'entrée en vigueur du contrat unique ; décision de financement non automatique.",
    "Pas de deuxième accord financier ; le congé existant n'est pas supprimé.",
    "L'accord préalable de l'employeur est requis lorsque le salarié souhaite suivre l'action de formation correspondante pour tout ou partie pendant son temps de travail.",
    "la demande de prise en charge peut être déposée avant la réponse de l'employeur à la demande de congé.")
effect(1, 'coordination', 'ptp-anciennete-acces-elargi',
    "Application de l'ouverture des périodes éligibles déjà proposée dans D. 6323-9.",
    "Voie du présent article attachée au CDD, avec les exclusions officielles de périodes pour les quatre mois.",
    "Tout salarié, toutes natures de contrats et aucune des exclusions 1° à 5°, sans retirer les autres conditions et dispenses.", 'regime',
    "Demandeurs remplissant la voie vingt-quatre mois sur cinq ans dont quatre mois sur douze, ou une dispense.",
    "Demandes en cours et futures, services anciens compris ; droits favorables acquis conservés.",
    "Coordination d'une mesure unique, pas cinq nouvelles suppressions ; emploi nouveau indéterminé selon la réforme distincte.",
    "Lorsque le salarié est titulaire d'un contrat à durée déterminée, il peut adresser une demande de prise en charge d'un projet de transition professionnelle",
    "Aucune des exclusions des 1° à 5° du II de cet article n'est opposable.")

effect(2, 'obligation_removed', 'ptp-suppression-delais-apres-emploi',
    "Suppression des deux forclusions temporelles après le terme ou la mission.",
    "Dépôt au plus tard quatre mois après le terme et début de formation au plus tard six mois après ce terme.",
    "Aucun délai maximal de dépôt ou de commencement imposé par l'article ; ancienneté toujours appréciée au départ en formation.", 'other',
    "Intermittents et intérimaires mentionnés à R. 6323-9-1, avec leurs dispenses.",
    "Demandes nouvelles et en cours après entrée en vigueur, fins antérieures comprises ; décisions définitives non rouvertes.",
    "Aucun calendrier de remplacement ; les fenêtres d'ancienneté et l'autorisation de congé sur temps de travail restent distinctes.",
    "au plus tard quatre mois après le terme de son dernier contrat de travail ou contrat de mission, à la condition que l'action de formation débute au plus tard six mois après ce terme.",
    "Aucun délai maximal de dépôt de la demande ou de commencement de la formation après cette fin n'est imposé par le présent article.")
effect(3, 'coordination', 'ptp-suppression-delais-apres-emploi',
    "Retrait dans la voie post-emploi de la même limite de commencement de six mois.",
    "Le I exige que la formation débute au plus tard six mois après le terme du contrat.",
    "Le I ne rétablit plus de limite maximale entre fin effective et commencement ; rémunération et garanties du II maintenues.", 'other',
    "Salariés de R. 6323-11-1 dont la formation commence après la fin effective de l'emploi.",
    "Demandes en cours et nouvelles, fins de contrat antérieures comprises ; pas de réouverture des décisions définitives.",
    "Aucune condition temporelle de remplacement ; coordination non comptée comme deuxième délai supprimé.",
    "à la condition toutefois qu'elle débute au plus tard six mois après celui-ci.",
    "Aucun délai maximal entre cette fin et le début de la formation n'est imposé par le présent article.")
effect(3, 'coordination', 'contrat-unique-duree-indeterminee',
    "Maintien du financement, de la rémunération et de la protection sociale au-delà de l'ancien CDD.",
    "Le maintien du régime social est explicitement attaché au précédent contrat à durée déterminée.",
    "Le maintien s'applique au contrat ou dernier contrat éligible, dont le contrat unique ; mêmes trois garanties et mêmes cotisations.", 'regime',
    "Bénéficiaires éligibles après emploi ou pendant un emploi poursuivi, dans leurs circuits respectifs.",
    "Anciens droits et situations futures conservés ; aucun double versement de rémunération.",
    "Pas de transfert de financeur ni de taxe de remplacement ; emploi unique imposé par la mesure législative distincte.",
    "du maintien du régime de protection sociale dont il bénéficiait lorsqu'il était titulaire d'un contrat de travail à durée déterminée",
    "Ces droits demeurent ouverts après un contrat antérieur à la réforme et après un contrat unique à durée indéterminée, pour les projets présents et futurs éligibles.")

effect(4, 'relief_extended', 'ptp-maintien-financement-sans-reemploi',
    "Le maintien d'une prise en charge accordée ne dépend plus d'un nouvel emploi après départ volontaire.",
    "Rupture par le bénéficiaire : nouveau contrat dans un mois après fin du préavis et accord du nouvel employeur sur le congé requis pour conserver la prise en charge.",
    "Aucun réemploi ni délai de réemploi imposé pour le maintien ; congé requis seulement si un nouvel emploi est effectivement affecté.", 'legal_duty',
    "Bénéficiaires dont la décision de rupture intervient après l'accord de financement.",
    "Maintiens restant à décider après entrée en vigueur, y compris anciens contrats ; assiduité et droits acquis conservés.",
    "Aucune déclaration de réemploi de remplacement ; contrôle du projet et autorisation d'absence dans un éventuel nouvel emploi maintenus.",
    "sous réserve de la conclusion d'un nouveau contrat de travail succédant au précédent dans un délai d'un mois à compter de la date de fin de préavis et de l'accord donné par le nouvel employeur à la demande de congé associé.",
    "Du bénéficiaire, sans condition de conclusion d'un nouveau contrat de travail ni de délai de réemploi.")
effect(4, 'obligation_removed', 'ptp-rupture-sans-justificatif-special',
    "Retrait de la transmission obligatoire d'une pièce distincte de rupture par le bénéficiaire.",
    "Transmission par le bénéficiaire du justificatif matérialisant la décision de rupture comme condition du maintien.",
    "Vérification des faits et de leur date par tout moyen probant ; aucune pièce distincte de rupture ou attestation particulière imposée.", 'legal_duty',
    "Bénéficiaires du maintien et commission qui vérifie l'accord antérieur à la décision de rupture.",
    "Demandes de maintien en cours ou futures à l'entrée en vigueur ; informations nécessaires encore vérifiables.",
    "Demande résiduelle des seules informations manquantes, sans modèle ni pièce de substitution obligatoire ; pas de nouveau droit d'accès aux données.",
    "Sous réserve de la transmission, par le bénéficiaire, du justificatif matérialisant la décision de rompre le contrat de travail",
    "Le bénéficiaire n'est pas tenu de transmettre un justificatif distinct de rupture.")

effect(5, 'coordination', 'contrat-unique-duree-indeterminee',
    "Continuité du payeur de la rémunération après la cessation effective du nouvel emploi indéterminé.",
    "Versement par la commission après terme du contrat à durée déterminée dans la voie R. 6323-14-1.",
    "Versement par la même commission après fin effective de l'emploi éligible, contrat unique ou ancien contrat.", 'regime',
    "Bénéficiaires de projets post-emploi financés selon R. 6323-14-1.",
    "Droits anciens et futurs conservés ; la simple fin de mission ne suffit pas si l'emploi continue.",
    "Aucun changement de financeur, prélèvement, formulaire ou délai de remplacement.",
    "Lorsque le projet de transition professionnelle est réalisé après le terme du contrat de travail à durée déterminée",
    "Cette règle vaut après un contrat à durée déterminée conclu avant la réforme comme après un contrat unique à durée indéterminée, sans fermeture du droit aux situations éligibles futures.")

effect(6, 'obligation_merged', 'ptp-avance-demande-sans-facture-distincte',
    "La demande d'avance et sa facture sont réunies, sans nouveau support.",
    "Employeur de moins de cinquante salariés : demande au IV puis facture indiquant le total des rémunérations et cotisations pour déclencher la première avance sous trente jours.",
    "Demande indiquant le même total ; aucune facture distincte, trente jours et plafond de 90 % conservés.", 'legal_duty',
    "Entreprises de travail temporaire de moins de cinquante salariés relevant du IV.",
    "Demandes et versements en cours et futurs ; une demande complète déjà reçue suffit et les délais courus ne sont pas repris.",
    "Le montant total figurait déjà dans la facture ; aucune donnée, déclaration ou échéance nouvelle.",
    "La première avance est versée à l'employeur par la commission paritaire interprofessionnelle régionale au plus tard trente jours après la réception de la facture émise par l'employeur",
    "Aucune facture distincte n'est exigée.")
effect(6, 'compliance_cost_reduced', 'ptp-remboursement-sans-copie-integrale-paie',
    "Le bulletin de paie intégral cesse d'être un support imposé au remboursement.",
    "Le 1° du III impose une copie du bulletin de paie.",
    "Seuls les éléments probants établissant la rémunération versée sont requis, avec preuve libre et réemploi.", 'legal_duty',
    "Employeurs de salariés intérimaires en projet financé et commission régionale.",
    "Demandes et versements en cours et futurs à l'entrée en vigueur ; sommes, assiduité et cotisations restent vérifiées.",
    "Pas de nouvelle attestation ni nouveau relevé équivalent ; pas de gain CRPA supplémentaire compté pour le simple réemploi.",
    "La copie du bulletin de paie ;",
    "La copie intégrale du bulletin de paie n'est pas exigée.")
effect(6, 'coordination', 'contrat-unique-duree-indeterminee',
    "L'affectation pédagogique nouvelle est portée par lettre dans le CDI, sans contrat de mission à terme.",
    "Contrat de mission pour le salarié temporaire ou lettre pour le titulaire d'un CDI intérimaire.",
    "Pour l'emploi nouveau, lettre de mission dans le contrat unique ; aucun nouveau CDD ni nouvel essai pour la formation.", 'regime',
    "Salariés des entreprises de travail temporaire bénéficiant du projet.",
    "Anciens contrats conservés jusqu'à leur terme ; aucun renouvellement à terme après réforme, ancienneté et intermissions préservées.",
    "Le CDI obligatoire remplace une option de CDD et maintient l'emploi au-delà de la phase : contrainte de régime coordonnée, non gain net démontré ; lettre déjà prévue pour le CDI.",
    "l'entreprise de travail temporaire établit un contrat de mission en application de l'article L. 1251-57 ou une lettre de mission",
    "Cette affectation n'exige pas de nouveau contrat de mission à durée déterminée ; elle n'interrompt pas le contrat unique et ne crée ni terme de l'emploi ni nouvelle période d'essai.")

effect(7, 'coordination', 'ptp-anciennete-acces-elargi',
    "Le calcul à quatre mois suit l'accès élargi aux périodes de tous contrats.",
    "Salaires des quatre derniers mois de CDD, hors contrats exclus par le II de D. 6323-9.",
    "Quatre derniers mois de travail de cette voie, sans exclusions par nature de contrat, avec protection du calcul ancien plus favorable.", 'regime',
    "Salariés relevant du 2° du I de D. 6323-9, dont nouvelles périodes et situations admises.",
    "Demandes en cours et futures, périodes anciennes comprises ; rémunérations et décisions favorables acquises conservées.",
    "Comparaison du plancher ancien pour les salariés également éligibles selon les anciennes règles, recensée comme complexité ajoutée.",
    "sur la base des salaires perçus au cours des quatre derniers mois en contrat de travail à durée déterminée, à l'exclusion des contrats mentionnés au II de l'article D. 6323-9.",
    "Aucune période n'est exclue de ce calcul sur le fondement des 1° à 5° du II de cet article.")
effect(7, 'complexity_added', 'ptp-anciennete-acces-elargi',
    "Comparaison supplémentaire pour conserver une moyenne ancienne plus favorable.",
    "Une moyenne à quatre mois selon la voie CDD et ses exclusions, sans comparaison avec des périodes désormais admises.",
    "Pour le salarié remplissant aussi les anciennes conditions, calcul ancien servant de minimum à la nouvelle moyenne.", 'regime',
    "Commission et salariés satisfaisant aux anciennes comme aux nouvelles conditions du 2° du I.",
    "Demandes en cours et futures ; pas de moyenne fictive lorsque la voie ancienne n'était pas satisfaite.",
    "Calcul supplémentaire possible et besoin de salaires historiques ; aucun dépôt distinct prescrit, solde de complexité non établi.",
    "Le salaire moyen de référence du salarié qui remplit les conditions d'ancienneté mentionnées au 2° de l'article D. 6323-9 est calculé",
    "le salaire moyen de référence ne peut être inférieur à celui calculé sur les quatre derniers mois en contrat à durée déterminée")

effect(8, 'coordination', 'ptp-acces-sans-seuil-entreprise',
    "La base salariale n'empêche pas l'accès sans 600 heures chez l'employeur prévu dans R. 6323-9-1 proposé.",
    "Seule base exprimée : 600 dernières heures de mission pour l'entreprise dépositaire, même lorsque l'accès pouvait déjà résulter de 600 heures dans le groupe.",
    "Base entreprise conservée si disponible ; sinon branche, heures effectivement accomplies, puis garantie mensuelle sans mission.", 'regime',
    "Intérimaires éligibles ne disposant pas de 600 heures de mission chez l'entreprise où la demande est déposée.",
    "Demandes en cours et futures à l'entrée en vigueur ; les droits déjà accordés restent conservés, les 1 600 heures de branche d'accès ne sont pas supprimées ici.",
    "Variantes de calcul et salaires d'autres entreprises potentiellement nécessaires, pas de nouveau seuil ou période de mission à accomplir.",
    "sur la base des salaires moyens perçus au cours des 600 dernières heures de mission effectuées pour le compte de l'entreprise de travail temporaire dans laquelle cette demande est déposée.",
    "Ces calculs subsidiaires ne constituent pas une condition d'ancienneté supplémentaire dans l'entreprise, le groupe ou la branche et ne réduisent pas la rémunération minimale due au titre du projet.")
effect(8, 'complexity_added', 'ptp-acces-sans-seuil-entreprise',
    "Création explicite de calculs subsidiaires de référence de salaire.",
    "La source ne décrit aucun calcul sans 600 heures de mission dans l'entreprise.",
    "La commission calcule à défaut sur la branche, sur les heures disponibles si moins de 600, ou sur la garantie mensuelle contractuelle s'il n'existe aucune mission.", 'regime',
    "Commission et intérimaires admis avec des périodes insuffisantes ou nulles de mission chez l'entreprise dépositaire.",
    "Demandes en cours et nouvelles ; règles de salaire et exclusions conservées, droits acquis protégés.",
    "Données et calculs supplémentaires possibles, sans formulaire nouveau ni accès nouveau aux données ; coût net inconnu.",
    "Le salaire moyen tient compte du salaire de base, des heures complémentaires ou supplémentaires et des primes de toute nature versées au cours de la période de référence",
    "S'il a effectué moins de 600 heures de mission dans la branche, la moyenne porte sur les heures de mission effectivement accomplies.")

effect(9, 'obligation_removed', 'reconversion-depot-sans-fenetre-trente-jours',
    "Retrait de la fenêtre de dépôt, conservant le délai distinct de décision.",
    "Dépôt dématérialisé dans les trente jours précédant le début de la reconversion.",
    "Dépôt avant ou pendant la reconversion, non limité à cette fenêtre ; décision sous vingt jours selon R. 6324-2 maintenue.", 'legal_duty',
    "Employeurs sollicitant la prise en charge d'une période de reconversion par l'opérateur.",
    "Demandes en cours et nouvelles ; pas de nouveau dépôt ni reprise du délai d'instruction.",
    "Aucun calendrier ou formulaire de remplacement ; pas de droit automatique à financement.",
    "dans les trente jours précédant le début de l'exécution de la période de reconversion :",
    "Le dépôt n'est pas limité aux trente jours précédant le début de la reconversion.")
effect(9, 'obligation_merged', 'reconversion-accord-convention-support-commun',
    "Document commun possible, sans annexe et signature répétée pour le même engagement.",
    "Accord écrit au 1° et convention annexée à cet accord au 2°.",
    "Un document peut satisfaire les deux contenus nécessaires ; aucune annexe distincte si les exigences de chaque acte sont remplies.", 'legal_duty',
    "Employeurs, salariés et organismes de formation présentant une période de reconversion.",
    "Dossiers en cours et futurs ; conventions et consentements acquis préservés.",
    "La convention de droit commun existait déjà ; aucun contenu, engagement ou signature nouvelle n'est créé.",
    "La convention annexée à cet accord, mentionnée à l'article L. 6353-1 ;",
    "Aucune annexe distincte ni nouvelle signature reproduisant le même engagement n'est exigée ;")
effect(9, 'obligation_removed', 'reconversion-sans-depot-contrat-complet',
    "Retrait du dépôt systématique du contrat d'accueil complet.",
    "Au 3°, transmission du contrat conclu avec une autre entreprise lorsqu'il existe.",
    "3° abrogé ; seuls éléments nécessaires à une vérification identifiée peuvent encore être demandés, sans transmission générale reconstituée.", 'legal_duty',
    "Employeurs et salariés en reconversion externe avec un emploi d'accueil.",
    "Demandes en cours et futures ; condition de fond d'un emploi d'accueil régulier maintenue, contrat unique pour emplois nouveaux.",
    "Demande ciblée possible, pas d'attestation standard ou de copie complète de remplacement.",
    "Le cas échéant, le contrat de travail conclu avec une autre entreprise pour la période de reconversion mentionné au II de l'article L. 6324-3 ;",
    "Elle ne peut rétablir une transmission systématique du contrat de travail complet avec l'entreprise d'accueil ; seuls les éléments de ce contrat nécessaires à une vérification identifiée peuvent être demandés.")
effect(9, 'obligation_added', 'reconversion-complements-necessite-explicite',
    "Obligation pour l'opérateur de préciser le critère et l'information manquante dans chaque complément.",
    "Le 4° permet tout autre document visant à s'assurer du respect des critères, sans imposer cette précision individualisée dans le texte.",
    "L'opérateur motive le besoin documentaire par le critère à vérifier et les informations manquantes, en utilisant d'abord les éléments disponibles.", 'legal_duty',
    "Opérateurs de compétences instruisant la prise en charge de reconversion.",
    "Demandes complémentaires des dossiers en cours et futurs à l'entrée en vigueur.",
    "Charge de rédaction ajoutée à l'opérateur ; elle ne doit pas transférer au demandeur un nouveau formulaire. Coût net inconnu.",
    "Tout autre document demandé par l'opérateur de compétences visant à s'assurer du respect des critères mentionnés au 1° bis du I de l'article L. 6332-1.",
    "Toute demande complémentaire précise le critère à vérifier et les informations manquantes correspondantes.")

effect(10, 'obligation_removed', 'reconversion-suppression-depot-ministeriel',
    "Suppression du second circuit central de dépôt et de transmission des refus.",
    "L'opérateur dépose l'accord auprès du ministre par le traitement CPF et transmet par le même circuit refus et motifs.",
    "Aucun de ces dépôts/transmissions à effectuer, y compris pour dossiers anciens ; notification du refus aux parties maintenue.", 'legal_duty',
    "Opérateurs de compétences et service ministériel recevant les accords de reconversion.",
    "Toutes transmissions restant à effectuer à l'entrée en vigueur, aucun rattrapage ; accords, droits, décisions et données déjà déposés conservés selon leur régime.",
    "Aucune déclaration ou registre équivalent, SI-CPF et contrôles autonomes maintenus.",
    "L'opérateur de compétences dépose l'accord écrit mentionné à l'article L. 6324-3 auprès du ministre chargé de la formation professionnelle",
    "L'opérateur de compétences n'est plus tenu de déposer auprès du ministre chargé de la formation professionnelle l'accord écrit de reconversion, ni de lui transmettre par ce circuit les refus de prise en charge et leurs motifs.")
effect(11, 'obligation_removed', 'professionnalisation-convention-speciale-abrogee',
    "Retrait complet du fondement spécial de convention signée, sans supprimer la convention générale existante.",
    "Obligation réglementaire spéciale de signature d'une convention de professionnalisation avec cinq catégories de mentions pédagogiques ; un support commun pouvait déjà remplir plusieurs fonctions.",
    "Aucune convention ou signature fondée sur D. 6325-12 ; convention de droit commun et obligations pédagogiques autonomes maintenues.", 'legal_duty',
    "Entreprises et organismes ou établissements dispensant l'accompagnement et les enseignements de professionnalisation.",
    "Conventions et signatures restant à établir à l'entrée en vigueur, dossiers en cours inclus ; contrats et prestations déjà convenus restent exécutés et aides futures ouvertes.",
    "Aucun document de substitution ; le droit commun préexistant n'est pas une formalité nouvelle et le gain est nul pour un support déjà suffisant sous les deux textes.",
    "donnent lieu à la signature, entre l'entreprise et l'organisme de formation ou l'établissement d'enseignement, d'une convention précisant les objectifs, le programme et les modalités d'organisation, d'évaluation et de sanction de la formation.",
    "L'obligation spéciale de conclure et de signer une convention de professionnalisation sur le fondement du présent article est supprimée, sans document ni signature de remplacement.")

Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles, {sum(len(a["reference_checks"]) for a in answer)} analyses de renvois, {sum(len(a["substantive_impact"]["effects"]) for a in answer)} effets documentés')
