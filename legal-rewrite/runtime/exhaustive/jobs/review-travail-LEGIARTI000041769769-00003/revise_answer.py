import copy
import hashlib
import json
from pathlib import Path


REFERENCE_DIGEST = "b8ba12e9f2b73d67f159bafa13722517bbf402052ae846cc64017523df0f1cbb"
reference_bytes = Path("reference-targets.json").read_bytes()
assert hashlib.sha256(reference_bytes).hexdigest() == REFERENCE_DIGEST
refs = json.loads(reference_bytes)
sources = json.loads(Path("source.json").read_text())
previous = json.loads(Path("previous-answer.json").read_text())
answer = copy.deepcopy(previous)
by_number = {a["number"]: a for a in answer}

# Le brouillon complet est conservé, sauf la coordination rendue nécessaire
# par la nouvelle rédaction fournie de R6222-6.
a = by_number["D6224-1"]
old = (
    "La convention de formation peut également tenir lieu de convention d'aménagement de durée "
    "lorsqu'elle en contient les éléments et recueille l'accord écrit de toutes les parties dont "
    "la signature est requise. Elle demeure annexée au contrat dans les conditions prévues au "
    "troisième alinéa de l'article L. 6222-7-1, sans document ou signature en double."
)
new = (
    "Dans les conditions prévues à l'article R. 6222-6, l'accord sur l'aménagement de durée peut "
    "figurer dans la convention de formation ou dans un document de formation commun, signé par "
    "le centre de formation, l'employeur et l'apprenti ou son représentant légal, sous réserve "
    "de la règle de signature propre au centre de formation d'apprentis interne à l'entreprise. "
    "La partie de ce document qui fixe l'aménagement constitue la convention et est annexée au "
    "contrat conformément au troisième alinéa de l'article L. 6222-7-1. Aucun acte autonome ni "
    "aucune répétition des signatures déjà apposées pour cet accord ne sont exigés."
)
assert a["proposed_xml"].count(old) == 1
a["proposed_xml"] = a["proposed_xml"].replace(old, new)
a["reason"] = (
    "Les suppressions de supports et de dépôt répétés du précédent essai sont conservées après "
    "comparaison avec la source entière. La correction de renvoi suit la vue actuelle de R. 6222-6 : "
    "l'aménagement peut figurer dans un document de formation commun, avec les signatures requises "
    "et la règle propre au CFA interne ; seule la partie constituant la convention d'aménagement "
    "doit être annexée au contrat. Cette coordination ne supprime pas l'annexion législative et "
    "n'impose pas celle de l'ensemble du document commun. Le délai de cinq jours ouvrables et "
    "toutes les données pédagogiques et financières restent nécessaires à la prise en charge "
    "contrôlable. Aucune autre coupe n'est retenue dans ces informations et garanties."
)
a["review_notes"] = (
    "La nouvelle vue fournie de R. 6222-6 a été relue intégralement avec sa source : évaluation "
    "des compétences, bornes de six mois à trois ans sous leurs exceptions, dispense de convention "
    "de R. 6222-9, signatures propres au CFA interne, document de formation commun et annexion de "
    "sa seule partie d'aménagement. Le texte de D. 6224-1 et son contrôle de cible sont corrigés "
    "sur cette base ; aucune ancienne empreinte de cette cible n'est reprise. L. 6222-7-1 maintient "
    "au troisième alinéa la convention signée et annexée : le document commun ne dispense pas "
    "d'obtenir les accords requis. L. 6224-1, D. 6224-2, R. 6224-3 et D. 6224-4 à D. 6224-7 ont été "
    "lus dans le corpus pour leurs textes officiels complets et leurs notes. Le dépôt et la décision "
    "de financement demeurent ; aucun financement automatique n'est créé. Les cinq jours du dépôt "
    "sont ouvrables, distincts du préavis individuel. R. 6224-3 fait courir vingt jours à réception "
    "de l'ensemble des documents requis, avec refus implicite : l'absence d'un support séparé "
    "supprimé ne doit pas retarder la complétude. D. 6224-5 conserve l'avenant en cas de modification "
    "essentielle ; seuls les éléments nouveaux sont transmis sans refaire le contrat initial. "
    "D. 6224-7 préserve la gratuité du dépôt. Le réemploi des pièces déjà accessibles coordonne le "
    "droit existant et ne compte pas comme une réduction autonome. Le renvoi explicite à R. 6222-6 "
    "est une cible fournie et contrôlée ; aucun renvoi nouveau à une cible non fournie n'est ajouté."
)
a["substantive_impact"]["assessment"] = (
    "La source exige une annexe pédagogique et financière et une convention tripartite lorsqu'elle "
    "est requise. Le texte retire le support séparé de l'annexe et permet de réunir les conventions "
    "dans un document commun. La correction à la vue actuelle de R. 6222-6 préserve les signatures "
    "et l'annexion de la partie d'aménagement, sans exiger l'annexion du reste du document. Elle "
    "ne constitue pas une seconde réduction. Le dépôt et toutes les informations sources subsistent."
)
a["substantive_impact"]["scope_limitations"] = (
    "Les accords requis, l'annexion de la convention et les contrôles de prise en charge subsistent. "
    "Les décisions de financement et l'avenant pour modification essentielle ne sont pas supprimés. "
    "La réunion de supports est dédupliquée sous apprentissage-documents-communs ; le réemploi CRPA "
    "ne compte pas comme un gain nouveau. Les coûts et le solde global de complexité ne sont pas mesurés."
)
a["substantive_impact"]["new_burdens_review"] = (
    "Aucune charge nouvelle n'est identifiée : le document commun reste facultatif, conserve les "
    "signatures déjà requises et ne crée ni registre ni attestation. Le contenu pédagogique et le "
    "délai de cinq jours ouvrables sont inchangés. La correction limite l'annexion à la partie qui "
    "constitue la convention, conformément à la cible fournie, sans réimposer une signature en double."
)
a["substantive_impact"]["effects"][0]["after"] = (
    "Même contenu utile ; informations pédagogiques et financières dans les documents du dossier, "
    "conventions réunissables avec les signatures requises et annexion de la partie d'aménagement."
)

# Même précision nécessaire dans le dépôt public : annexer l'ensemble du
# document de prise en charge rétablirait indirectement son envoi financier.
a = by_number["D6275-1"]
old = (
    "Ce document demeure annexé au contrat dans les conditions prévues au troisième alinéa "
    "de l'article L. 6222-7-1 ; aucun second document ni aucune signature en double n'est exigé."
)
new = (
    "La partie de ce document qui fixe l'aménagement constitue la convention et demeure annexée "
    "au contrat dans les conditions prévues au troisième alinéa de l'article L. 6222-7-1 ; aucun "
    "second document ni aucune signature en double n'est exigé. L'intégration ne rend pas "
    "obligatoire la transmission des autres éléments de la convention de prise en charge."
)
assert a["proposed_xml"].count(old) == 1
a["proposed_xml"] = a["proposed_xml"].replace(old, new)
a["reason"] += (
    " La relecture corrige également la portée de l'annexion : seule la partie constituant "
    "l'aménagement est annexée, afin que l'intégration à un document commun ne rétablisse pas "
    "l'envoi de l'ensemble de la convention financière supprimé."
)
a["review_notes"] += (
    " Coordination d'annexion rectifiée avec L. 6222-7-1 : le document commun ne doit pas entraîner "
    "le retour indirect de la convention financière entière au dépôt ; sa seule partie "
    "d'aménagement constitue la convention à annexer. Aucune dispense d'accord requis ni de "
    "contrôle autonome n'en résulte, et aucune nouvelle cible n'est ajoutée à reference_checks."
)
a["removed_provisions"][0] = (
    "Suppression du document d'aménagement de durée séparé lorsque le document commun contient "
    "l'aménagement et les signatures requises ; sa seule partie valant convention reste annexée au contrat."
)
a["substantive_impact"]["assessment"] += (
    " La correction limite l'annexion à la partie d'aménagement pour ne pas rétablir "
    "indirectement le dépôt financier ; elle n'est pas comptée comme une seconde réduction."
)
a["substantive_impact"]["effects"][0]["after"] = (
    "Réunion facultative des fonctions dans un document commun signé ; sa partie valant "
    "convention d'aménagement reste annexée. Le contrat et l'aménagement requis sont déposés, "
    "sans dépôt financier systématique ni envoi obligatoire des autres éléments du document commun."
)

# Les trois coordinations protectrices sont décrites par leurs propres effets,
# et non par un simple changement de vocabulaire de la garantie maintenue.
coord_effects = {
    "R6222-23-1": {
        "description": "Maintien des deux dérogations et de la dispense pour reprendre l'apprentissage au sein d'un emploi sans terme.",
        "before": "Reprise d'apprentissage après rupture : dérogation aux minima de durée du contrat ou de formation en centre, sans convention de réduction obligatoire.",
        "after": "Mêmes dérogations et dispense pour les reprises futures ; la durée réduite est celle de la période pédagogique du nouvel emploi sans terme.",
        "affected_population": "Apprentis reprenant leur cycle dans le champ de L. 6222-18-2 et de ses exceptions territoriales ou transfrontalières.",
        "source_quote": "il peut être dérogé à la durée minimale du contrat d'apprentissage mentionnée au premier alinéa de l'article L. 6222-7-1",
        "proposed_quote": "la durée réduite est celle de la période d'apprentissage ; elle n'est pas celle de l'emploi et son expiration ne le rompt pas.",
    },
    "D6222-28-1": {
        "description": "Coordination de l'assimilation salariale du cycle entier avec les périodes réduites du contrat unique.",
        "before": "Lors d'une réduction relevant des trois fondements cités, durée du cycle réputée accomplie pour la rémunération seulement.",
        "after": "Même assimilation pour les futures périodes réduites du contrat unique ; aucun terme d'emploi ni ancienneté générale fictive n'en résulte.",
        "affected_population": "Apprentis relevant d'une réduction selon L. 6222-7-1, L. 6222-12-1 ou R. 6222-23-1.",
        "source_quote": "l'apprenti est considéré, en ce qui concerne sa rémunération, comme ayant accompli une durée d'apprentissage égale à ce cycle de formation.",
        "proposed_quote": "Elle reste applicable aux futures périodes d'apprentissage des contrats uniques à durée indéterminée conclus à compter de l'entrée en vigueur de la loi portant réforme du contrat de travail.",
    },
    "D6222-28-2": {
        "description": "Coordination du minimum salarial pendant une prolongation pédagogique avec l'emploi sans terme.",
        "before": "En cas de prolongation par L. 6222-7-1, minimum correspondant à la dernière année précédant la prolongation selon D. 6222-26.",
        "after": "Même minimum pour les futures prolongations de la période d'apprentissage, sans transformer sa fin en rupture de l'emploi.",
        "affected_population": "Apprentis dont la période de formation dépasse le cycle dans le cas de L. 6222-7-1, troisième alinéa.",
        "source_quote": "le salaire minimum applicable pendant la prolongation est celui correspondant à la dernière année d'exécution du contrat précédant cette prolongation selon les modalités prévues à l'article D. 6222-26.",
        "proposed_quote": "La prolongation concerne la phase pédagogique et ne fixe pas un terme à l'emploi.",
    },
}
for number, changes in coord_effects.items():
    by_number[number]["substantive_impact"]["effects"][0].update(changes)

# Analyses nouvelles après lecture des vues sources et proposées fournies.
# La clé courte est résolue ci-dessous vers l'identifiant EXACT demandé.
checks = {
    "R6222-23-1": {
        "L1234-1": "La cible proposée remplace pour les nouveaux contrats les préavis de licenciement liés à l'ancienneté par quinze jours calendaires ; elle garde les anciens régimes et les procédures protégées. Ici, la reprise d'apprentissage et la dispense de convention ne sont pas des actes de rupture : elles ne notifient rien et ne font courir aucun préavis. Le départ du préavis reste à coordonner selon la notification écrite prévue par la politique, non selon la signature d'une convention pédagogique.",
        "L1221-2": "La source cible autorise encore le CDD dans ses cas légaux ; sa proposition réserve aux nouveaux emplois une durée indéterminée et interdit le terme automatique lié à une formation. Le nouvel engagement du présent article doit donc ouvrir une période d'apprentissage dans cet emploi. La dérogation aux minima et la dispense restent utilisables pour les reprises futures ; les droits des contrats antérieurs ne sont ni convertis de force ni supprimés.",
        "L1234-9": "L'indemnité de la cible proposée est patronale, hors faute grave : un an au terme effectif, préavis inclus, puis 0,20 mois par année totale, mois complets au prorata, plafond légal de six mois. Les droits des anciens contrats suivent leurs composantes sans double compte. La reprise et les six mois de formation théorique ne créent pas une ancienneté fictive chez le nouvel employeur ; la dispense de convention ne retranche aucune créance de salaire ou indemnité spéciale.",
        "L6222-7-1": "Le renvoi au premier alinéa vise le minimum de six mois, dans une plage ordinaire allant jusqu'à trois ans ; le troisième alinéa prévoit l'aménagement et sa convention signée, annexée. R. 6222-23-1 maintient expressément la dérogation au minimum et la dispense de cette convention dans son cas de reprise. La proposition cible limite ces durées à la pédagogie du contrat unique et préserve les anciens contrats ; elle ne rétablit ni convention dispensée ni terme d'emploi.",
        "L6222-18-2": "La cible source comporte trois garanties après rupture : poursuite théorique pendant six mois, aide à retrouver un employeur, statut de stagiaire pendant cette période. Sa proposition les étend expressément à la rupture du contrat unique pendant l'apprentissage, sous ses champs et exceptions territoriales et transfrontalières. La reprise facilitée par R. 6222-23-1 garde ces avantages ouverts et ne transforme pas les six mois en durée de l'emploi suivant.",
    },
    "D6222-28-1": {
        "L1234-1": "Les quinze jours calendaires de la proposition cible concernent le préavis patronal des nouveaux contrats, indépendamment de l'ancienneté ; les anciens contrats gardent leurs règles. L'assimilation d'un cycle pour le salaire de l'apprenti ne vaut ni notification de rupture ni durée de préavis. Elle n'autorise pas à soustraire des salaires dus pendant le préavis et ne modifie aucune procédure collective ou autorisation spéciale.",
        "L1221-2": "La proposition cible interdit un terme automatique de l'emploi nouveau, même à la fin de la formation. D. 6222-28-1 rattache donc correctement la réduction au contrat antérieur ou à la période pédagogique du contrat unique. Les trois cas de réduction restent admis pour l'avenir ; le bénéfice salarial n'est pas réservé aux anciens CDD et ne nécessite pas d'en conclure ou renouveler un.",
        "L1234-9": "La durée réputée accomplie par le présent article sert exclusivement à la rémunération d'apprentissage. Elle ne remplace pas l'année d'ancienneté ininterrompue réellement atteinte au terme effectif, préavis inclus, que la cible proposée exige pour l'indemnité patronale de 0,20 mois par année totale avec prorata en mois complets et plafond de six mois. Le salaire reste dû même sans indemnité ordinaire ; anciens droits et indemnités spéciales restent distincts.",
        "L6222-7-1": "Le troisième alinéa de la cible permet une durée de période inférieure au cycle d'après les compétences initiales ou acquises, et conserve une convention signée annexée. Le renvoi de D. 6222-28-1 vise exactement cette réduction pour en neutraliser l'effet défavorable sur la rémunération. Il n'assimile pas le cycle à de l'ancienneté de rupture et ne transforme pas la période pédagogique de la proposition cible en durée d'emploi.",
        "R6222-23-1": "La vue fournie de R. 6222-23-1 et le texte final conservé dans ce lot accordent les deux dérogations de durée et dispensent de convention dans le cas de reprise après rupture. D. 6222-28-1 attache à cette réduction le salaire correspondant au cycle réputé accompli. La dispense de convention n'est pas annulée par ce renvoi salarial ; les reprises futures en contrat unique restent couvertes, sans ancienneté générale fictive.",
    },
    "D6222-28-2": {
        "L1234-1": "Le préavis de quinze jours calendaires de la cible proposée est distinct de la prolongation de formation. Une prolongation pédagogique ne vaut pas notification et n'ajoute aucun jour au préavis ; le minimum salarial du présent article continue de jouer dans sa propre période. Les contrats antérieurs restent soumis à leurs préavis et garanties, sans suppression des procédures ou autorisations de rupture distinctes.",
        "L1221-2": "La source cible permet le CDD, tandis que sa proposition exclut tout terme automatique pour les nouveaux emplois. Prolonger la période d'apprentissage selon D. 6222-28-2 n'est donc ni renouveler un CDD ni prolonger un emploi qui devrait s'éteindre au terme du cycle. Le minimum de dernière année est conservé aussi pour les prolongations futures du contrat unique ; les contrats antérieurs et rémunérations acquises restent protégés.",
        "L1234-9": "La cible proposée calcule l'indemnité ordinaire patronale hors faute grave après un an effectif, préavis inclus : 0,20 mois par année totale, fractions en mois complets, plafond de six mois, avec transition des anciens contrats. Une prolongation réellement exécutée peut compter dans l'ancienneté applicable ; aucune durée fictive n'est créée. Le salaire minimum de prolongation n'est ni absorbé ni plafonné par l'indemnité ordinaire.",
        "L6222-7-1": "Le troisième alinéa de la cible permet aussi l'allongement de la période par rapport au cycle selon les compétences ; c'est ce cas précis que vise D. 6222-28-2. Le renvoi salarial à D. 6222-26 garde les âges, pourcentages et minima conventionnels correspondants. La proposition cible ne fait pas de cet allongement un terme de l'emploi et n'ôte pas la garantie aux situations futures ; les anciens contrats gardent leurs règles.",
    },
    "R6223-1": {
        "L1234-1": "Abroger le fondement spécial des demandes de pièces ne modifie pas le préavis de la cible : quinze jours calendaires pour les nouveaux contrats dans la proposition, régimes antérieurs conservés pour les anciens. Cela ne dispense ni de notifier la rupture selon ses propres règles ni de respecter les autorisations ou procédures collectives. Les pièces exigibles sur les fondements autonomes de contrôle restent accessibles dans leurs champs.",
        "L1221-2": "La cible proposée impose une durée indéterminée aux nouveaux emplois et ne permet aucun renouvellement ou reconduction en CDD après la réforme. L'abrogation de R. 6223-1 retire un devoir spécial de justification, pas l'écrit d'apprentissage ni la validité des accords pédagogiques. Elle s'applique aux demandes nouvelles, même sur d'anciens contrats, sans permettre de recruter à terme ou d'effacer leurs droits acquis.",
        "L1234-9": "La preuve spéciale supprimée ne modifie pas la condition d'un an à la fin effective, préavis inclus, ni le barème proposé de 0,20 mois par année totale, mois complets au prorata et plafond légal de six mois pour la rupture patronale hors faute grave. Les composantes des anciens contrats, salaires et indemnités spéciales demeurent. Les contrôles autonomes de documents ne sont ni étendus ni neutralisés par l'abrogation.",
        "L6222-7-1": "La source de R. 6223-1 permettait de demander les pièces attestant la convention d'aménagement. Le troisième alinéa de L. 6222-7-1 conserve dans la vue proposée cette convention, ses signataires et son annexion. Retirer le fondement spécial de demande n'abroge pas ces exigences de fond ni les contrôles autonomes ; la période pédagogique de la cible ne devient pas un terme d'emploi et les accords antérieurs restent valables.",
    },
    "D6224-1": {
        "L1234-1": "Le délai de dépôt de D. 6224-1 demeure cinq jours ouvrables après le début d'exécution ; il n'est pas le préavis de quinze jours calendaires prévu par la proposition cible pour les nouveaux contrats. Un dépôt auprès de l'OPCO ne notifie pas une rupture au salarié et ne fait pas courir son préavis. Les anciens préavis, autorisations de salariés protégés et procédures collectives restent hors de cette simplification documentaire.",
        "L1221-2": "Le contrat unique de la proposition cible exclut une fin automatique à l'achèvement de la formation ou d'une mission et interdit les nouveaux CDD, y compris par renouvellement postérieur à la réforme. Le dépôt unique et la mise à jour d'une nouvelle période d'apprentissage dans D. 6224-1 ne créent donc pas un nouvel emploi à terme et ne remettent pas l'ancienneté à zéro. Un avenant reste requis si un élément essentiel du contrat est modifié.",
        "L1234-9": "La convention et le dépôt pédagogique ne déterminent pas l'ancienneté de rupture de la cible proposée : un an au terme effectif, préavis inclus, puis 0,20 mois par année totale avec mois complets au prorata et plafond légal de six mois, pour la rupture patronale hors faute grave. Les anciennes composantes et indemnités spéciales subsistent. Une mise à jour du financement n'interrompt pas l'ancienneté et n'ouvre pas une indemnité fictive.",
        "L6222-7-1": "La vue cible maintient au troisième alinéa la convention tripartite signée et annexée, malgré la substitution de la période pédagogique à la durée du nouvel emploi. Le document commun de D. 6224-1 doit contenir l'accord d'aménagement avec toutes les signatures requises, sous la règle spéciale du CFA interne ; sa partie valant convention reste annexée au contrat. L'intégration matérielle ne dispense ni de cet accord ni des conditions de fond, sauf dispenses applicables.",
        "R6222-6": "La nouvelle vue fournie précise que la partie du document de formation commun fixant l'aménagement constitue la convention et est annexée au contrat conformément à L. 6222-7-1. D. 6224-1 est rectifié en ce sens, sans imposer d'annexer le document commun entier. Les signatures du centre, de l'employeur et de l'apprenti ou représentant sont requises sous l'exception du CFA interne ; pas d'acte autonome ni de signature répétée. Les évaluations pertinentes restent réutilisables, les conventions antérieures valables et les dispenses de R. 6222-9 ou R. 6222-23-1 préservées ; l'aménagement n'est pas un terme d'emploi.",
    },
    "R6226-3": {
        "L1234-1": "La transmission d'informations d'affectation au CFA n'est pas la notification de rupture à l'apprenti. Le préavis patronal de la cible proposée reste quinze jours calendaires pour les nouveaux contrats, avec les régimes antérieurs pour les anciens et les procédures protégées distinctes. Le délai administratif de quinze jours pour décider la reprise après risque sérieux, réservé par le III, a une fonction de sécurité différente et n'est pas absorbé par ce préavis.",
        "L1251-16": "La cible source exige un contrat de mission écrit avec sept catégories de mentions ; la proposition actuelle utilise une lettre de mission pour les nouveaux emplois et dispense les informations déjà remises sur support conservable. R. 6226-3 y ajoute les six informations pédagogiques de R. 6226-2 sans recopie ni attestation supplémentaire. La lettre n'instaure pas un nouvel essai ; la rémunération, le rapatriement et les indemnités et recours des missions anciennes ne sont pas supprimés par ce règlement.",
        "L1221-2": "La proposition cible interdit de terminer automatiquement le nouvel emploi avec sa mission ou sa formation ; les anciens contrats gardent leur transition, sans nouveau renouvellement en CDD. R. 6226-3 distingue la lettre d'affectation du contrat unique et préserve les mesures spéciales de suspension ou rupture de sécurité. La simple fin d'une affectation ne rompt pas l'emploi et ne crée pas de nouvel essai, même si la période pédagogique est limitée.",
        "L1234-9": "Le seuil proposé d'un an à la fin effective, préavis inclus, et le barème patronal hors faute grave de 0,20 mois par année totale, mois complets au prorata, plafond de six mois, concernent la seule indemnité ordinaire. Le III préserve les sommes spéciales de sécurité de L. 6225-5 sans leur appliquer ce seuil ni ce plafond. Une fin de mission n'interrompt pas l'ancienneté ; les intermissions légalement assimilées restent reconnues et les anciens contrats conservent leurs droits.",
    },
    "D6235-7": {
        "L1234-1": "L'envoi unique des conventions à l'OPCO n'est pas une notification de rupture à l'apprenti ; sa date ne déclenche donc pas le préavis patronal de quinze jours calendaires de la cible proposée. Les contrats antérieurs conservent leurs règles de préavis. La simplification de circuit ne supprime aucune autorisation spéciale ou procédure collective et ne déroge pas aux communications directement requises par la convention internationale applicable.",
        "L1221-2": "Pour un nouvel emploi français soumis à la réforme, la proposition cible interdit le terme lié à l'accueil, la mission ou la formation ; l'affectation est donc décrite à partir des documents de l'emploi indéfini existant. Le guichet unique n'autorise pas un nouveau CDD ou renouvellement et conserve les envois valables des anciens contrats. Il ne décide pas la loi applicable à un emploi étranger ni l'extension du contrat unique à un régime public distinct.",
        "L1234-9": "La durée de l'accueil transfrontalier et la date d'envoi des conventions ne fixent pas l'ancienneté chez l'employeur qui rompt. La cible proposée réserve l'indemnité ordinaire patronale hors faute grave à un an au terme effectif, préavis inclus : 0,20 mois par année totale, mois complets au prorata, plafond de six mois, avec transition ancienne. Salaires, frais d'accueil et garanties spéciales ne sont pas absorbés dans ce barème et ne sont pas supprimés par le circuit unique.",
    },
    "D6235-13": {
        "L1234-1": "Le champ du présent article est la formation française d'un apprenti employé dans le pays frontalier. Il ne suffit pas à appliquer le préavis français de quinze jours calendaires de la cible proposée : la loi de l'emploi et la convention internationale doivent être déterminées. Ni l'admission en troisième formation ni la réduction de sa durée ne vaut notification de rupture ; les anciens contrats et procédures spéciales ne sont pas effacés par cette simplification pédagogique.",
        "L1221-2": "La cible proposée supprime le terme automatique des nouveaux emplois soumis au contrat unique français, même à la fin d'une formation ; les anciens contrats gardent leur transition. D. 6235-13 ne peut imposer cette réforme à l'employeur frontalier par le seul choix d'un enseignement français. La réserve finale l'explicite et, si le contrat unique est effectivement applicable, aucune durée de cycle, de temps partiel ou de réorientation ne termine automatiquement l'emploi.",
        "L1234-9": "L'ancienneté pédagogique, la première année de formation au 10° et la durée d'un cycle ne sont pas l'année ininterrompue au terme effectif, préavis inclus, de l'indemnité ordinaire proposée. Le barème de 0,20 mois par année totale, prorata en mois complets et plafond légal de six mois pour une rupture patronale hors faute grave ne s'applique pas automatiquement à un emploi étranger. Les anciens droits, salaires et garanties de formation restent dans leurs champs propres.",
        "L6222-7-1": "Le 2° renvoie aux compétences initiales ou acquises mentionnées par la cible, pas à l'ensemble de son régime de contrat ni à sa durée d'emploi. L. 6235-4 II 2° exclut l'essentiel du titre II lorsque la pratique se déroule dans le pays frontalier ; le minimum de durée aménagée supprimé ici est celui du 2° de D. 6235-13. Le cycle ordinaire de six mois à trois ans demeure au 1°, ainsi que les prolongations et conditions de certification ; le renvoi ne rétablit pas le minimum individuel supprimé.",
        "L6222-18-2": "La cible maintient les six mois de poursuite théorique, l'aide à rechercher un nouvel employeur et le statut de stagiaire après rupture dans son champ. L. 6235-4 II 2° maintient expressément son application pour la pratique dans le pays frontalier ; son exception distincte lorsque la théorie est à l'étranger ne doit pas être confondue avec ce cas. Le 9° de D. 6235-13 conserve la dérogation de reprise pour les futurs bénéficiaires ; supprimer le plancher aménagé ne ferme aucun de ces droits.",
    },
    "D6274-1": {
        "L1234-1": "La dispense de désigner un médiateur distinct concerne l'organisation des employeurs publics de L. 6227-1. Elle n'étend pas à elle seule le préavis patronal proposé de quinze jours calendaires aux contrats publics concernés et ne fixe aucune date de notification. La cible garde les régimes anciens et les protections distinctes ; la fonction de médiation et l'accès au juge restent ouverts, sans réduire un délai de protection par ce changement d'intervenant.",
        "L1221-2": "La proposition cible emploie une formule large, tout contrat relevant du code, alors que la politique réserve la réforme aux relations privées nouvelles et ne supprime pas implicitement le régime des agents publics. L'articulation avec L. 6227-12 doit donc être expresse pour les apprentis publics ; D. 6274-1 ne la décide pas. Sa dispense d'organisation peut bénéficier aux contrats anciens sans les convertir ni modifier leurs règles de durée ou de rupture.",
        "L1234-9": "Le choix d'un service de médiation ne fixe aucune indemnité et ne convertit pas les apprentis publics au barème privé proposé : un an au terme effectif avec préavis, puis 0,20 mois par année totale, mois complets au prorata et plafond légal de six mois pour la rupture patronale hors faute grave. Les anciens régimes et indemnités spéciales restent distincts. Le temps de médiation n'est ni une ancienneté fictive ni un motif de retrancher une créance acquise.",
        "L6222-18": "La cible source distingue les quarante-cinq jours pratiques, les voies de rupture, la médiation préalable et la cosignature du mineur, avec exclusion historique des contrats antérieurs à 2019. La proposition ouvre ensuite le régime du contrat unique avec médiation accessible et protection du mineur. D. 6274-1 ne retire aucune saisine encore obligatoire pour un contrat ancien ou public resté sous son régime ; il remplace seulement l'intervenant possible, sans décider l'extension législative au public.",
        "D6222-21-1": "La source impose cinq jours calendaires après saisine du médiateur puis sept jours après information de l'employeur dans son champ à partir du 1er janvier 2019. Sa proposition réserve aux nouveaux contrats uniques un préavis de quinze jours dès le lendemain de réception de l'écrit et retire la saisine préalable obligatoire du majeur. Le renvoi de D. 6274-1 doit appliquer un seul régime effectivement applicable au contrat public, sans cumuler cinq, sept et quinze jours ; la protection du mineur et les règles des contrats plus anciens subsistent.",
    },
    "D6275-1": {
        "L1234-1": "Les cinq jours ouvrables de D. 6275-1 concernent le dépôt public après début d'exécution, pas le préavis de licenciement de la cible proposée. Retirer la convention financière du dépôt ne vaut ni notification à l'apprenti ni réduction d'un délai de rupture. Les préavis anciens, les protections et l'éventuelle application future du régime privé doivent être déterminés par leurs propres textes ; cette simplification documentaire n'y supplée pas.",
        "L1221-2": "La proposition cible interdit les nouveaux emplois à terme relevant du contrat unique ; le présent article conserve le dépôt public fondé sur L. 6227-11 et ne décide aucune conversion des apprentis ou agents publics. Son renvoi à l'aménagement de formation n'étend pas implicitement la durée indéterminée à un régime distinct : l'articulation avec L. 6227-12 demeure à coordonner par la loi. Les contrats antérieurs et décisions de prise en charge valables restent protégés.",
        "L1234-9": "La dispense d'envoi de la convention financière ne modifie ni l'ancienneté ni une indemnité de rupture. Le seuil et le barème privés de la cible proposée, un an au terme effectif préavis inclus, puis 0,20 mois par année totale avec mois complets au prorata et plafond légal de six mois pour la rupture patronale hors faute grave, ne sont pas étendus au secteur public par D. 6275-1. Les salaires, anciennes composantes et indemnités spéciales restent réservés.",
        "L6222-7-1": "La cible conserve au troisième alinéa la convention tripartite signée annexée. Le document de prise en charge ou de formation ne tient lieu d'aménagement que s'il en contient les éléments et les accords écrits requis ; seule sa partie constituant cette convention reste annexée et déposée. Cette précision évite de rétablir indirectement l'envoi financier supprimé. Le renvoi ne décide pas l'extension du contrat unique privé au secteur public et préserve les conventions anciennes, sans dispenser du dépôt de l'aménagement requis.",
    },
    "D6323-9": {
        "L1234-1": "Les vingt-quatre mois de salariat portable de D. 6323-9 s'apprécient au départ en formation, tandis que les quinze jours calendaires de la cible proposée sont un préavis patronal pour les nouveaux contrats sans seuil d'ancienneté. Une demande de formation n'est pas une notification de rupture et ne déclenche aucun préavis. La fusion des voies d'accès n'affecte ni les préavis des anciens contrats ni les autorisations ou procédures collectives distinctes.",
        "L1221-2": "La cible proposée supprime les nouveaux CDD et les fins automatiques d'emploi liées à une formation ; ses droits transitoires restent protégés. D. 6323-9 supprime en conséquence toute nécessité de détenir quatre mois récents de CDD : vingt-quatre mois de salariat de toute nature ouvrent la voie générale, sans récence ou rattachement à l'entreprise. Les périodes d'anciens CDD restent admises sans permettre leur renouvellement ni limiter la durée du contrat unique.",
        "L1234-9": "L'ancienneté portable auprès de plusieurs employeurs pour une formation ne se confond pas avec l'année ininterrompue chez celui qui rompt, appréciée au terme effectif avec préavis, pour l'indemnité ordinaire proposée. Le montant patronal hors faute grave demeure 0,20 mois par année totale, prorata en mois complets et plafond légal de six mois, sous transition ancienne. La fusion de D. 6323-9 ne crée pas d'indemnité fictive et ne retranche ni salaires ni dispenses et garanties spéciales.",
    },
    "R6323-9-1": {
        "L1234-1": "Les jours, cachets et heures de R. 6323-9-1 sont des conditions de formation, sans effet sur le préavis patronal de la cible proposée : quinze jours calendaires pour les nouveaux contrats et régimes antérieurs pour les anciens. Leur allègement ne vaut pas notification de rupture, ne fait courir aucun délai et ne supprime aucune autorisation ou procédure spéciale. La date de départ en formation demeure distincte de la réception de l'écrit de rupture.",
        "L1251-2": "La source définit l'entrepreneur de travail temporaire par le recrutement rémunéré pour une mise à disposition temporaire. Sa proposition soumet les recrutements nouveaux au contrat unique et réserve les garanties mensuelles et d'intermission. Le II de R. 6323-9-1 reste compatible avec cette définition : les 1 600 heures de branche demeurent, le sous-seuil de 600 heures disparaît et les intermissions du CDI restent admises sans nouveau contrat à terme ni suppression de rémunération garantie.",
        "L1221-2": "Les voies du spectacle et de l'intérim continuent de s'appliquer aux futurs salariés en contrat unique. La proposition cible interdit de faire de la fin d'une représentation, d'une mission ou d'une formation un terme automatique de l'emploi et conserve les anciens contrats sous transition. Supprimer les seuils cumulatifs de formation n'autorise donc aucun nouveau CDD d'usage, ni renouvellement postérieur de CDD, et ne réduit pas les droits déjà ouverts.",
        "L1234-9": "Les heures de branche et les cachets ne valent pas ancienneté ininterrompue chez l'employeur qui rompt. La cible proposée exige un an au terme effectif, préavis inclus, puis 0,20 mois par année totale avec mois complets au prorata et plafond légal de six mois pour une rupture patronale hors faute grave, sous transition ancienne. Les intermissions assimilées légalement restent reconnues pour l'ancienneté applicable, sans conversion horaire inventée ; salaires et indemnités spéciales restent distincts.",
        "D6323-9": "La source cible prévoit deux voies, 24 mois dont 12 dans l'entreprise ou 24 mois sur cinq ans dont quatre de CDD récents, avec cinq exclusions. La vue proposée fournie étend les quatre mois à tous contrats mais conserve les deux voies ; elle n'est pas le droit en vigueur. Le texte final de ce lot conserve la fusion plus favorable du précédent essai : 24 mois portables sans récence ni rattachement. Le renvoi de R. 6323-9-1 ouvre la voie générale en alternative aux seuils spéciaux, sans cumul ; date d'appréciation et dispenses sont conservées.",
    },
}

targets_by_number = {v["number"]: (k, v) for k, v in refs["targets"].items()}
for article in answer:
    number = article["number"]
    key = article["code_id"] + "|" + article["source_id"]
    required = refs["requirements"][key]
    expected_numbers = [refs["targets"][k]["number"] for k in required]
    assert set(checks[number]) == set(expected_numbers), number
    article["reference_checks"] = [
        {
            "target_key": target_key,
            "view_sha256": refs["targets"][target_key]["view_sha256"],
            "assessment": checks[number][refs["targets"][target_key]["number"]],
        }
        for target_key in required
    ]
    assert article["status"] == "rewrite_draft"

assert hashlib.sha256(Path("reference-targets.json").read_bytes()).hexdigest() == REFERENCE_DIGEST
Path("answer.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")
print(f"answer.json : {len(answer)} articles, {sum(len(a['reference_checks']) for a in answer)} contrôles de cibles actuelles")
