import json
import re
from html import unescape
from html.parser import HTMLParser
from pathlib import Path

S = json.loads(Path('source.json').read_text())
R = json.loads(Path('reference-targets.json').read_text())
A = []

def plain(s):
    return unescape(re.sub(r'<[^>]+>', '', s or ''))

def paragraphs(*items):
    return ''.join('<p>' + x + '</p>' for x in items)

def impact(classification, assessment, limitations, burdens, effects=None):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=limitations, new_burdens_review=burdens,
                effects=effects or [])

def effect(kind, measure, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure, description=description,
                before=before, after=after, unit=unit,
                affected_population=population,
                conditions_and_transition=transition,
                replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)

def add(i, proposed, reason, notes, si, **extra):
    s = S[i]
    a = {k:s[k] for k in ('code_id','source_id','source_sha256','number')}
    a.update(proposed_xml=proposed, reason=reason, review_notes=notes,
             status='retained_unchanged' if proposed is None else 'rewrite_draft',
             substantive_impact=si)
    if proposed is None:
        a['classification'] = 'retained_necessary'
    a.update(extra)
    A.append(a)
    return a

def repeal(i, text, reason, notes, si, scope, **extra):
    return add(i, text, reason, notes, si, change_type='full_repeal',
               repeal_policy_id='editorial_direction_2026_10_19',
               repeal_scope=scope, **extra)

# L244-4 : le fait de récidive reste défini ; les deux peines accessoires cessent.
p0 = paragraphs(
    "Il y a récidive lorsque dans les douze mois antérieurs à la date d'expiration du délai d'un mois imparti par l'avertissement ou la mise en demeure prévus à l'article L. 244-2, le contrevenant a déjà subi une condamnation pour une contravention identique.",
    "Le présent article ne permet plus de prononcer les peines complémentaires d'inéligibilité ou d'incapacité de participer à des organismes consultatifs pour les faits commis à compter de l'entrée en vigueur de la présente loi.",
    "1°) Abrogé.",
    "2°) Abrogé.",
    "Pour les faits antérieurs, les règles en vigueur à la date des faits demeurent applicables sous réserve de l'application de la loi pénale plus douce et des règles relatives à la cessation d'exécution des peines prévues aux articles 112-1 et 112-4 du code pénal. La définition de la récidive au premier alinéa et les peines principales prévues par d'autres dispositions ne sont pas modifiées."
)
add(0, p0,
    "Réforme de fond : retrait des deux peines accessoires d'exclusion professionnelle et consultative, dont le lien avec le paiement des cotisations n'est pas nécessaire au recouvrement. Le premier alinéa, qui définit la récidive sur douze mois après une condamnation pour contravention identique, est maintenu à droit constant. Les amendes principales, le principal social et les garanties de poursuite ne sont pas supprimés.",
    "Les subdivisions 1°) et 2°) restent repérables comme abrogées ; l'alinéa définissant la récidive n'est pas déplacé. L244-2, R244-4 et R244-6 ont été lus dans le corpus public : délai préalable d'un mois, amende principale et plafond de cumul demeurent distincts. Aucun nouveau délai de préavis de travail n'est créé. Les notes citent plusieurs anciennes numérotations ; notamment le L623-1 fourni est aujourd'hui un régime de prestations parentales, non une extension des sanctions. Les articles 112-1 et 112-4 du code pénal, hors corpus fourni, sont signalés pour coordination temporelle sans en inventer une rédaction ni modifier leur champ. Vérifier également les adaptations de Saint-Pierre-et-Miquelon citées par les notes, hors de ce lot.",
    impact('material_reduction',
        "La source entière autorisait, outre la récidive, deux exclusions de six mois à cinq ans. Seules ces peines accessoires sont retirées ; aucune baisse des cotisations ou des amendes principales n'est revendiquée.",
        "La qualification de récidive et les peines principales restent. L'effet sur les affaires antérieures dépend des règles pénales transitoires ; les textes territoriaux extérieurs ne sont pas réécrits ici.",
        "Aucune charge nouvelle identifiée : ni déclaration ni autorisation de remplacement. La transition conserve les garanties pénales générales et n'ajoute aucun registre ou justificatif.",
        [effect('obligation_removed','recouvrement-social-fin-exclusions-accessoires',
                "Suppression des deux peines complémentaires d'inéligibilité et d'incapacité consultative.",
                "En cas de récidive, le tribunal pouvait prononcer pour six mois à cinq ans les inéligibilités du 1°) et l'incapacité du 2°).",
                "Pour les faits nouveaux, ces deux peines ne peuvent plus être prononcées sur ce fondement ; les peines principales restent.",
                'legal_duty','Cotisants contrevenants en état de récidive visés par L244-4.',
                "Faits à compter de l'entrée en vigueur ; faits antérieurs sous réserve de la loi pénale plus douce.",
                "Aucune exclusion ni formalité de remplacement.",
                "Le tribunal peut, en outre, prononcer pour une durée de six mois à cinq ans :",
                "Le présent article ne permet plus de prononcer les peines complémentaires d'inéligibilité ou d'incapacité de participer à des organismes consultatifs pour les faits commis à compter de l'entrée en vigueur de la présente loi.")]),
    change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=[
        "Peine complémentaire d'inéligibilité aux chambres, tribunaux et conseil de prud'hommes énumérés au 1°), de six mois à cinq ans.",
        "Peine complémentaire d'incapacité à faire partie des comités et conseils consultatifs constitués auprès du Gouvernement, de six mois à cinq ans."
    ])

p1 = paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la présente loi.",
    "Pour les faits commis à compter de cette date, aucune publication dans un journal ni aucun affichage du jugement ne peut être ordonné aux frais du contrevenant sur le fondement du présent article.",
    "Les faits antérieurs et les décisions déjà rendues demeurent régis par les règles antérieures, sous réserve de l'application de la loi pénale plus douce et des règles relatives à la cessation d'exécution des peines prévues aux articles 112-1 et 112-4 du code pénal. Les frais légalement acquittés avant cette date ne donnent pas lieu à restitution du seul fait de la présente abrogation.",
    "Les peines principales, le recouvrement des cotisations, les voies de recours et les règles de publicité des décisions de justice ayant un fondement distinct demeurent applicables."
)
repeal(1,p1,
    "Réforme de fond : suppression de la faculté d'ajouter une insertion dans la presse et un affichage payants aux condamnations relevant de L244-1 à L244-4. Ce coût accessoire, même plafonné à 1 % du PASS pour l'insertion, n'est pas nécessaire au recouvrement ni au caractère public de la justice. Les sanctions principales et les recours sont conservés.",
    "L241-3 sert ici uniquement à définir le plafond annuel limitant le coût d'insertion ; sa proposition de capitalisation ne transforme pas ce coût en cotisation vieillesse. La suppression ne modifie pas le PASS ni les prestations indexées sur celui-ci. L244-4 conserve sa définition de récidive. Les notes d'extension historiques, notamment L623-1, ne sont pas des renvois normatifs contemporains au contrat unique. Les règles pénales transitoires 112-1 et 112-4, extérieures aux fichiers fournis, sont une coordination signalée ; ne pas étendre l'abrogation aux peines de publication fondées sur une autre infraction. Les textes territoriaux cités en notes restent à coordonner dans leur champ propre.",
    impact('material_reduction',
        "La faculté autonome de publication et d'affichage payants disparaît pour les faits nouveaux. Le plafond favorable de 1 % n'est pas perdu : la dépense correspondante n'est plus imposable sur ce fondement.",
        "Les autres peines de publication, la publicité ordinaire de la justice et les décisions antérieures ne sont pas abolies globalement. Aucune économie nationale n'est chiffrée.",
        "Aucune charge nouvelle identifiée : la suppression ne demande ni autorisation ni déclaration et n'institue aucune publicité alternative payante.",
        [effect('obligation_removed','recouvrement-social-fin-publication-payante',
                "Fin de la peine accessoire de publication et d'affichage à la charge du contrevenant.",
                "Publication intégrale ou par extraits et affichage décidés par le tribunal ; insertion plafonnée à 1 % du plafond annuel L241-3.",
                "Aucune publication ou affichage payant sur ce fondement pour les faits nouveaux ; sanctions principales inchangées.",
                'legal_duty','Contrevenants condamnés dans les cas de L244-1 à L244-4.',
                "Faits nouveaux dès l'entrée en vigueur, avec réserve de la loi pénale plus douce pour les faits anciens.",
                "Pas de publication ou frais de remplacement.",
                "le tout aux frais du contrevenant, sans que le coût de l'insertion puisse dépasser 1 % du plafond annuel mentionné à l'article L. 241-3.",
                "Pour les faits commis à compter de cette date, aucune publication dans un journal ni aucun affichage du jugement ne peut être ordonné aux frais du contrevenant sur le fondement du présent article.")]),
    "Publication et affichage judiciaires payants complémentaires aux condamnations des articles L244-1 à L244-4 pour les faits nouveaux.")

add(2,None,
    "Maintien intégral nécessaire après examen : l'article réprime la rétention indue par l'employeur de la part salariale déjà précomptée, en cas de récidive dans les trois ans. Ce n'est ni une cotisation accessoire ni une formalité : supprimer l'incrimination réduirait une protection contre l'appropriation des sommes des salariés. Les deux ans d'emprisonnement, 3 750 euros et la possibilité d'une seule des deux peines restent inchangés.",
    "Le délai de récidive de trois ans de L244-6 est distinct des douze mois de L244-4 ; aucune fusion silencieuse. R244-4 et L244-2, lus dans le corpus, portent respectivement la sanction contraventionnelle générale et l'avertissement préalable, non une autorisation de retenir la part salariale. Aucun renvoi au contrat unique, aucune restriction d'aide, d'exonération ou de droit salarial futur.",
    impact('retained_necessary',
        "Aucune modification de la source entière : maintien de la sanction ciblée contre une rétention indue de cotisations précomptées, protection essentielle des salariés et du financement de leurs droits.",
        "Le maintien ne démontre aucune baisse de prélèvement et n'étend pas la sanction aux simples erreurs déclaratives. Aucune réforme de la procédure pénale générale n'est proposée ici.",
        "Aucune charge nouvelle identifiée puisque le texte officiel entier reste applicable sans déclaration, registre, délai ou condition supplémentaire."))

add(3,None,
    "Maintien intégral nécessaire : le point de départ de la prescription pénale reste l'expiration du mois laissé pour régulariser après avertissement ou mise en demeure. Cette articulation évite une poursuite avant la garantie préalable et fixe une borne temporelle intelligible ; elle ne constitue pas un délai minimal d'embauche ou une formalité doublonnée. Les infractions de L244-1 à L244-4 et L244-6 ne sont pas toutes supprimées par ce lot.",
    "L244-2 et L244-3 ont été lus dans le corpus. L244-4 garde son premier alinéa malgré le retrait de ses peines accessoires ; L244-5 et L244-8 abrogés ne sont pas visés par L244-7. La source porte ABROGE_DIFF avec fin au 1er janvier 2029 : le maintien n'annule pas cette extinction programmée et ne prétend pas réécrire son texte successeur, non fourni. Les notes L623-1 sont historiquement décalées par rapport à la cible actuelle de prestations parentales. Les quinze jours du préavis privé ne remplacent pas le mois de régularisation sociale.",
    impact('retained_necessary',
        "Maintien de la totalité de la règle de prescription pénale, sans suppression artificielle d'une garantie de régularisation et sans renvoi nouveau au droit des contrats de travail.",
        "Article applicable dans sa fenêtre officielle se terminant le 1er janvier 2029 ; les modalités du régime successeur ne sont pas établies par la source de ce lot.",
        "Aucune charge nouvelle identifiée : aucune nouvelle notification ou donnée n'est exigée ; le mois préalable et son point de départ restent ceux de la source."))

p4 = paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la présente loi.",
    "Aucun remboursement de prestations ne peut être mis à la charge de l'employeur sur le seul fondement du présent article à raison d'un accident survenu ou d'un arrêt de travail débutant à compter de cette date.",
    "Pour les accidents survenus et les arrêts de travail ayant débuté avant cette date, les règles antérieures demeurent applicables, notamment la limitation aux prestations effectivement servies entre l'accident ou l'arrêt et l'acquittement des cotisations alors impayées, ainsi que le plafond égal aux cotisations dues pour l'ensemble du personnel à la date de l'accident ou de l'arrêt. Les prescriptions, restitutions et recours sont conservés, sous réserve de l'application de la loi répressive plus douce dans son champ. Il n'est créé aucun remboursement général des sommes légalement acquittées.",
    "Les droits des assurés aux prestations, l'obligation de payer les cotisations et les majorations légalement dues, ainsi que les responsabilités et recours fondés sur une disposition distincte, demeurent applicables."
)
repeal(4,p4,
    "Réforme de fond : suppression du remboursement punitif des soins de longue maladie ou d'accident du travail dû uniquement parce que l'employeur est en retard de cotisations pour son personnel. Cette charge s'ajoute au principal et aux sanctions ordinaires sans condition de causalité avec le sinistre ; le recouvrement des cotisations et les responsabilités pour faute conservent leurs fondements distincts. Les assurés ne perdent aucune prestation.",
    "La bascule porte sur la date de l'accident ou du début de l'arrêt, pas sur celle du remboursement tardif par la caisse. Pour le stock antérieur, les deux bornes favorables de la source sont expressément conservées : période entre sinistre/arrêt et paiement des impayés et plafond des cotisations dues à la date du sinistre/arrêt. Le renvoi ancien L324-1 reste dans le droit antérieur applicable au stock ; il ne crée aucune obligation nouvelle. L243-2 et les adaptations du décret 98-994 pour Saint-Pierre-et-Miquelon, mentionnés dans les notes, sont des coordinations extérieures à ce lot. L'abrogation n'éteint ni dette sociale principale ni recours pour faute inexcusable ou autre responsabilité autonome ; aucune recette de compensation n'est créée.",
    impact('material_reduction',
        "Une charge de remboursement de prestations, cumulable avec les cotisations impayées et leurs accessoires, disparaît pour les sinistres nouveaux. Le service des prestations reste entièrement distinct de cette sanction.",
        "La suppression ne réduit pas les cotisations, les sanctions autonomes ni les recours pour responsabilité ayant un autre fondement. Les créances anciennes restent plafonnées ; le coût net public n'est pas chiffré.",
        "Aucune charge nouvelle identifiée : ni régime d'autorisation, ni attestation de paiement, ni remboursement ou prélèvement de remplacement n'est institué.",
        [effect('obligation_removed','recouvrement-social-fin-remboursement-soins-sanction',
                "Fin du remboursement punitif de prestations en raison du seul impayé de cotisations patronales.",
                "Remboursement des prestations de longue maladie ou AT effectivement servies jusqu'à régularisation, au plus égal aux cotisations dues pour tout le personnel à la date du sinistre ou de l'arrêt.",
                "Aucun remboursement sur ce fondement pour un accident ou début d'arrêt nouveau, sans réduction des prestations des assurés ni effacement des cotisations.",
                'legal_duty',"Employeurs en situation d'impayé lors de l'accident ou de l'arrêt visé ; salariés et assimilés protégés.",
                "Accident ou début d'arrêt dès l'entrée en vigueur ; régime et plafonds anciens pour les événements antérieurs.",
                "Aucune charge de remplacement ; responsabilités autonomes conservées.",
                "Cette sanction est encourue lorsque, à la date de l'accident ou de l'arrêt de travail, l'employeur n'avait pas acquitté l'intégralité des cotisations de sécurité sociale dues pour son personnel.",
                "Aucun remboursement de prestations ne peut être mis à la charge de l'employeur sur le seul fondement du présent article à raison d'un accident survenu ou d'un arrêt de travail débutant à compter de cette date.")]),
    "Remboursement sanction des prestations de longue maladie et d'accident du travail pour accidents ou arrêts nouveaux en cas d'impayé social de l'employeur.")

add(5,None,
    "Maintien intégral nécessaire : la prescription triennale de l'action civile en recouvrement limite le temps pendant lequel le cotisant peut être poursuivi indépendamment de l'action publique. Supprimer cette borne favorable ne simplifierait pas le droit au bénéfice du débiteur. Le départ à l'expiration du délai des avertissements et mises en demeure est conservé.",
    "L244-2 et L244-3 ont été lus, ainsi que L244-9 dans les cibles. La prescription de l'action civile n'est ni le délai d'opposition à contrainte ni un préavis de licenciement. Les notes de la loi 2016-1827 préservent les mises en demeure notifiées dès le 1er janvier 2017 et la borne totale pour les créances plus anciennes. La source prévoit une fin d'applicabilité au 1er janvier 2029 (ABROGE_DIFF) : le maintien ne la reporte pas. La rédaction du régime successeur n'est pas fournie et n'est pas inventée.",
    impact('retained_necessary',
        "La totalité de la prescription triennale protectrice reste inchangée. Aucune nouvelle baisse de cotisation ou suppression de formalité n'est comptée pour ce maintien.",
        "Les exceptions de travail illégal et de dialogue européen restent aux articles L244-11 et L244-12. La source n'établit pas le détail du droit succédant à son extinction programmée en 2029.",
        "Aucune charge nouvelle identifiée : le maintien n'ajoute aucun acte préalable, notification ou justificatif et conserve la borne temporelle favorable existante."))

add(6,None,
    "Maintien intégral nécessaire après examen des trois alinéas : la contrainte assure le recouvrement des droits sociaux avec opposition devant un tribunal, et sa prescription définitive est bornée à trois ans. L'exécution provisoire de droit après deux jours ne concerne que les sommes redressées pour les infractions de travail illégal des 1° à 4° de L8211-1 ; l'arrêt judiciaire reste possible en cas de moyen sérieux et de conséquences manifestement excessives. Cette protection antifraude ciblée est conservée, sans généralisation aux autres cotisants.",
    "La cible fournie reprend la même source officielle, sans proposition antérieure. Ne pas confondre deux jours calendaires d'exécution provisoire, délai réglementaire d'opposition et quinze jours de préavis de travail. La note de la loi 2026-534 prévoit une application aux contraintes décernées à une date fixée par décret, au plus tard le 1er janvier 2027 : aucune date effective de décret n'est affirmée ici. L211-16 COJ et L8211-1 travail ne sont pas des renvois nouveaux et leurs corps entiers ne sont pas fournis dans les cibles ; leurs rédactions ne sont pas inventées. L244-11 conserve la prescription spéciale de cinq ans et L244-12 sa suspension européenne.",
    impact('retained_necessary',
        "Aucune modification de la source entière : conservation d'un titre de recouvrement contestable, d'une voie d'arrêt de l'exécution antifraude et de la prescription de la contrainte définitive.",
        "L'exécution provisoire ne s'étend pas hors des redressements pour le travail illégal visé. Son calendrier reste celui de la note légale et du décret applicable ; aucun bilan net de coût n'est établi.",
        "Aucune charge nouvelle identifiée : les actes, voies de contestation et délais restent ceux du texte officiel, sans nouvelle procédure ni condition d'accès au juge."))

add(7,None,
    "Maintien intégral nécessaire : le droit d'appel du ministère public et des parties intéressées constitue une garantie de contrôle des jugements du chapitre. Il ne s'agit ni d'une transmission doublonnée ni d'une autorisation administrative ; supprimer l'appel compromettrait une protection essentielle du cotisant. Les dispositions du chapitre qui subsistent et ses litiges anciens nécessitent cette voie de recours.",
    "L'abrogation prospective de certaines sanctions accessoires ne supprime pas les contentieux des cotisations, de la rétention de la part salariale ou des décisions antérieures. Les renvois des notes sont historiques ; le L623-1 actuel fourni traite de prestations parentales, non de la procédure d'appel. Aucun préavis, indemnité ou contrat privé n'est réglé par cet article. Les voies et conditions procédurales détaillées hors de cet article ne sont pas réécrites.",
    impact('retained_necessary',
        "Le droit d'appel est conservé en entier pour sa fonction de recours juridictionnel. Aucun allègement matériel nouveau n'est attribué à cet article inchangé.",
        "Ce maintien ne statue pas sur les délais d'appel fixés ailleurs et ne fait pas revivre une sanction supprimée pour les faits nouveaux. Les règles spéciales de procédure restent à leur champ.",
        "Aucune charge nouvelle identifiée : le texte inchangé n'ajoute aucune démarche obligatoire, pièce ou délai et conserve une faculté de recours."))

add(8,None,
    "Maintien intégral nécessaire : la prescription portée à cinq ans est strictement attachée à une infraction de travail illégal constatée par procès-verbal. Elle sert la détection et le recouvrement de la fraude, et ne constitue pas un délai administratif sans objet. Les trois renvois à l'assiette, à l'action civile et à la contrainte correspondent à des délais distincts, non à trois créances nouvelles.",
    "L244-3 et L244-8-1 ont été lus avec leurs transitions de 2017 ; L244-9 a été lu dans la cible complète. La prescription spéciale de cinq ans ne remplace ni les deux jours d'exécution provisoire ciblée de L244-9 ni le préavis du contrat unique. L244-8-1 porte une extinction programmée au 1er janvier 2029 ; sa coordination successorale devra être faite avec le texte successeur non fourni, sans en déduire une extinction immédiate du renvoi actuel. La transition légale de 2017 reste applicable, notamment la limitation de la durée totale pour les créances plus anciennes.",
    impact('retained_necessary',
        "La seule extension antifraude de prescription constatée par procès-verbal est maintenue sans modification. Elle n'est pas présentée comme une diminution des prélèvements ou des contraintes.",
        "Hors constat de travail illégal par procès-verbal, les délais de droit commun ne sont pas allongés. La coordination du régime civil appelé à succéder en 2029 n'est pas documentée dans le lot.",
        "Aucune charge nouvelle identifiée : aucune nouvelle catégorie d'infraction ou de donnée n'est créée ; la condition du procès-verbal et les bornes existantes sont conservées."))

add(9,None,
    "Maintien intégral nécessaire : la suspension de prescription pendant le dialogue et la conciliation prévus par les règlements européens permet la coordination des sécurités sociales sans mettre les organismes devant une prescription résultant de cette procédure. Cette contrainte européenne ne peut être effacée implicitement pour alléger un calendrier national. Aucun rapport périodique, taxe ou justificatif supplémentaire n'est prévu par cet article.",
    "L244-3, L244-8-1 et la cible L244-9 ont été lus. Le texte suspend le décompte des délais pendant la procédure européenne ; il n'interrompt pas indistinctement tous les délais judiciaires et ne règle pas l'opposition à contrainte ou le préavis d'emploi. L'extinction programmée de L244-8-1 au 1er janvier 2029 appelle une coordination avec son successeur lorsque celui-ci sera fourni, sans anticiper sa rédaction. Aucun contenu de règlement européen absent du dossier n'est reconstruit.",
    impact('retained_necessary',
        "La règle entière de suspension pendant une procédure européenne identifiée est conservée. Aucun gain matériel n'est revendiqué pour cette coordination transfrontière nécessaire.",
        "La suspension reste limitée aux trois délais expressément visés et à la durée de la procédure européenne. Le texte ne permet pas de conclure à la suspension d'un autre recours.",
        "Aucune charge nouvelle identifiée : aucune déclaration ou délai minimal supplémentaire n'est ajouté ; la suspension existante reste à son champ légal."))

p10 = paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la présente loi.",
    "Les conventions de conseil, d'assistance ou d'avance conclues à compter de cette date ne sont plus nulles du seul fait qu'un intermédiaire rémunéré offre ou accepte ses services afin d'obtenir une remise, même partielle, de sommes réclamées par un organisme de sécurité sociale. Cette activité ne peut plus être sanctionnée sur le seul fondement du présent article pour les faits commis à compter de cette date.",
    "Les conventions conclues avant cette date demeurent soumises, pour leur validité et leurs effets civils, aux règles qui leur étaient applicables. Les faits antérieurs demeurent régis par les règles pénales antérieures sous réserve de l'application de la loi pénale plus douce et des règles relatives à la cessation d'exécution des peines prévues aux articles 112-1 et 112-4 du code pénal. Aucune restitution générale des sommes légalement acquittées n'est créée.",
    "La présente abrogation ne confère aucun droit à remise et ne modifie ni les conditions légales de celle-ci, ni les compétences des organismes et du juge. Les règles relatives aux professions réglementées, à la représentation, à la protection du consentement, à la fraude et aux conflits d'intérêts, notamment celles de l'article L. 244-14, demeurent applicables dans leur champ propre."
)
repeal(10,p10,
    "Réforme de fond : retrait de la nullité générale des engagements envers les intermédiaires rémunérés cherchant une remise sociale et de l'incrimination correspondante, y compris amende, emprisonnement en récidive et publicité. Cette interdiction de principe frappe aussi l'assistance licite ; les conditions de remise, les professions réglementées et la répression des fraudes restent distinctes. La protection ciblée contre les conflits d'intérêts des agents sociaux est maintenue à L244-14.",
    "Les montants supprimés sont 1 500 euros, six mois d'emprisonnement et 3 750 euros en récidive, avec publication/affichage plafonnés ensemble à 15 euros ; les mentions historiques de 1994 ne sont pas des dates de réforme future. L244-5 ne porte pas ce plafond propre. Pour les conventions antérieures, la nullité civile n'est pas levée rétroactivement ; pour les faits pénaux anciens, réserver 112-1/112-4 code pénal, dont les corps ne sont pas fournis. Le nouveau renvoi exprès à L244-14 vise une source entière assignée et maintenue dans ce lot, hors des cibles imposées de reference-targets.json ; aucune analyse supplémentaire n'est ajoutée à reference_checks. Ni droit automatique à transaction ni remise de principal n'est créé. Les conditions autonomes des professions et de représentation ne sont pas réécrites ici ; adaptations territoriales des notes à coordonner hors lot.",
    impact('material_reduction',
        "Suppression démontrée de l'interdiction générale d'assistance rémunérée à une demande de remise et de ses sanctions propres. La dette sociale et les conditions d'octroi d'une remise restent inchangées.",
        "Aucune libéralisation des professions réglementées, de la fraude ou des conflits d'intérêts n'est décidée. Les contrats antérieurs gardent leur régime civil et le solde économique n'est pas chiffré.",
        "Aucune charge nouvelle identifiée : l'interdiction n'est remplacée par aucun agrément, déclaration, registre ou justificatif de qualification supplémentaire.",
        [effect('obligation_removed','remises-sociales-fin-interdiction-generale-intermediaires',
                "Retrait de la nullité et des sanctions propres à l'assistance rémunérée en vue d'une remise sociale.",
                "Nullité de plein droit des engagements et répression de l'offre de services ; 1 500 euros, puis six mois et 3 750 euros en récidive ; publicité plafonnée à 15 euros.",
                "Conventions nouvelles non nulles et activité nouvelle non réprimée sur ce seul fondement ; aucune remise garantie.",
                'legal_duty','Cotisants et intermédiaires sollicitant une remise sociale, sous réserve des règles professionnelles et antifraude autonomes.',
                "Conventions et faits nouveaux dès l'entrée en vigueur ; ancien droit civil conservé et loi pénale plus douce réservée.",
                "Pas d'agrément ni de déclaration de remplacement ; L244-14 et les règles autonomes demeurent.",
                "Sont nulles de plein droit et de nul effet les obligations contractées pour rémunération de leurs services ou avances envers les intermédiaires",
                "Cette activité ne peut plus être sanctionnée sur le seul fondement du présent article pour les faits commis à compter de cette date.")]),
    "Interdiction générale, nullité civile et sanctions propres de l'assistance rémunérée aux remises sociales pour conventions et faits nouveaux.")

add(11,None,
    "Maintien intégral nécessaire après examen : l'article vise les agents et anciens agents des organismes sociaux qui interviennent ou participent, contre rémunération, à une entreprise obtenant des remises, pendant l'activité ou durant les cinq années suivant la cessation. Cette règle protège l'impartialité du recouvrement et prévient les conflits d'intérêts ; elle demeure nécessaire malgré la suppression de l'interdiction générale de L244-13. Les deux ans, 4 500 euros et le plafond de publicité de 15 euros sont conservés avec le régime des complices.",
    "Le délai de cinq ans court de la cessation des fonctions de l'agent, pas de la rupture du contrat d'un cotisant ou d'un préavis privé. La nullité et l'infraction générales de L244-13 peuvent être supprimées sans effacer cette incrimination autonome. La suppression de publicité à L244-5 n'a pas pour objet la sanction ciblée autonome de L244-14 ; aucun renvoi devenu vide ne la soutient. Les conditions légales de remise ne sont pas modifiées. Aucun nouveau statut des agents publics ou privés n'est inventé.",
    impact('retained_necessary',
        "Maintien de la totalité d'une protection ciblée de probité du recouvrement, distincte de l'interdiction générale des intermédiaires supprimée à L244-13. Aucun allègement nouveau n'est revendiqué.",
        "Ce maintien n'interdit pas tout conseil social : il vise les personnes et participations expressément énumérées. La durée de cinq ans et les peines autonomes ne sont ni étendues ni réduites.",
        "Aucune charge nouvelle identifiée : l'article demeure inchangé, sans nouveau registre de déontologie, autorisation ou déclaration à créer."))

MED = 'promotion-medicaments-contribution-suppression'
DM = 'promotion-dispositifs-medicaux-contribution-suppression'
date_clause = "Le présent article est abrogé à compter de l'entrée en vigueur de la présente loi."
stock = ("Les dispositions antérieures demeurent applicables exclusivement aux contributions se rapportant à des charges comptabilisées avant cette date, même si la clôture de l'exercice, la déclaration, la liquidation, le paiement ou le contrôle intervient ultérieurement. Les abattements, exonérations, imputations, restitutions, prescriptions et recours correspondants sont conservés. Aucune restitution générale des sommes légalement dues n'est créée.")
mixed_year = ("Pour les exercices qui comprennent des charges comptabilisées avant et à compter de cette date, seules les premières restent imposables. Le chiffre d'affaires de référence et la durée des exercices sont déterminés selon les règles antérieures ; les abattements et seuils favorables ne subissent aucun prorata supplémentaire du seul fait de la présente abrogation.")
no_future_form = ("Aucune déclaration, donnée, représentation fiscale, garantie ou versement exclusivement justifié par cette contribution ne peut être exigé pour les charges comptabilisées à compter de cette date. Les obligations nécessaires à la liquidation et au contrôle des seules charges antérieures demeurent applicables ; les obligations ayant un fondement distinct ne sont pas modifiées.")
no_new_tax = ("La suppression ne crée ni contribution de remplacement ni extension de l'assiette d'un autre prélèvement. Les règles sanitaires, la réglementation de la publicité, les conditions de prise en charge des produits et les autres prélèvements ayant un fondement distinct demeurent applicables.")

med_notes = ("Mesure unique dédupliquée sous promotion-medicaments-contribution-suppression : L245-1 est le fait générateur supprimé, L245-2 à L245-5 et L245-5-1 A sont ses coordinations, non cinq taxes supplémentaires. L138-20 à L138-23 ont été lus : retirer pour les seules charges nouvelles les références et données exclusivement liées à cette contribution, conserver les garanties et les autres contributions, notamment L245-6. L138-21, bien qu'inclus dans la plage de renvoi actuelle, vise des prélèvements mobiliers et non cette contribution : discordance préexistante signalée, sans lui attribuer un contenu fictif. L241-2 IV 6° conserve l'affectation à la CNAM des seules recettes anciennes effectivement recouvrées et les autres contributions. R245-4 à R245-7 et D245-1 ont été lus : extinction des formalités pour les seules charges nouvelles, maintien des modalités et avantages pour le stock ; R245-4 reste utile au régime distinct auquel R245-18 renvoie. Ces articles hors lot ne sont pas présentés comme réécrits. R245-6 renvoie à R245-3, dont aucun corps ne figure dans le corpus consulté : cette lacune de calendrier n'est pas comblée par invention et n'éteint pas le report favorable expressément conservé pour le stock par la transition législative. Les notes de 2021 renvoient à des conditions d'application extérieures dont le texte intégral n'est pas fourni. La perte de recettes et les besoins de financement maladie restent à chiffrer, sans recette de compensation inventée ni baisse de prestations déduite de l'abrogation.")
dm_notes = ("Mesure unique dédupliquée sous promotion-dispositifs-medicaux-contribution-suppression : L245-5-1 porte la suppression, L245-5-2 à L245-5-6 la coordonnent sans compter de nouvelles taxes supprimées. L138-20 à L138-23 et L241-2 IV 6° ont été lus : les références ne valent plus que pour les charges anciennes et leurs recettes effectivement recouvrées ; les autres prélèvements et garanties subsistent. L138-21 traite de prélèvements mobiliers malgré son inclusion dans la plage de renvoi : incohérence préexistante à ne pas combler par invention. R245-16, R245-16-1 et R245-16-2 ont été lus : ne pas rétablir de déclaration future, conserver les calculs favorables anciens ; R245-4, auquel R245-16 renvoie, reste utile à des régimes distincts. Ces coordinations réglementaires et d'affectation ne sont pas rédigées dans ce lot. La réglementation sanitaire, les remboursements de produits et les contributions autonomes, dont L245-6, restent distincts. Perte de recettes CNAM et solde public net non chiffrés, sans financement ni rendement inventé.")
tax_limit = ("La suppression ne vise que cette contribution sur les dépenses de promotion ; elle n'abolit ni les impôts généraux, ni les autres contributions sanitaires, ni les règles européennes et nationales de sécurité. Les coordinations réglementaires et d'affectation indiquées ne sont pas rédigées ici ; le solde public n'est pas établi.")
tax_burdens = ("Aucune obligation nouvelle autonome identifiée : pas de déclaration, agrément, registre ou prélèvement de remplacement. La séparation des écritures antérieures et nouvelles utilise les dates comptables existantes ; son coût transitoire n'est pas chiffré et aucun solde global des codes n'est affirmé.")

p12 = paragraphs(date_clause,
    "La contribution instituée au profit de la Caisse nationale de l'assurance maladie n'est plus due à raison des charges comptabilisées à compter de cette date, quelle que soit la date de clôture de l'exercice ou d'échéance.",
    stock, mixed_year, no_future_form, no_new_tax)
repeal(12,p12,
    "Réforme de fond : suppression de la contribution sectorielle sur la promotion des spécialités pharmaceutiques. Ce prélèvement assis sur des dépenses ne constitue pas une autorisation sanitaire ni un contrôle de la qualité de l'information ; ces protections conservent leurs fondements distincts. Suppression pour toutes les entreprises du champ, y compris exploitation, importation et distribution parallèles, sans taxe de remplacement. Les dettes et avantages sur les seules charges antérieures sont préservés.",
    med_notes + " Le fait temporel choisi est la comptabilisation de la charge, pas la date de paiement de la contribution ou de clôture : une échéance future ne rétablit pas l'impôt sur les charges nouvelles. Aucun taux intermédiaire n'est institué ; le tableau 19/29/36/39 de L245-2 a été lu en entier.",
    impact('material_reduction',
        "La contribution prévue par la source entière est abolie pour les charges nouvelles, et non simplement différée. Toutes les entreprises du champ en bénéficient ; le stock ancien et ses exonérations restent liquidables.",
        tax_limit, tax_burdens,
        [effect('tax_removed',MED,
                "Abolition prospective de la contribution sur les dépenses de promotion des médicaments.",
                "Entreprises du champ : rémunérations et charges associées des personnes de L5122-11, frais de déplacement hors véhicules mis à disposition, repas/hébergement, publications, publicité et congrès, prestations externalisées HT, sous exclusions et répartition forfaitaire ; abattements 2,5 millions d'euros, 3 % des dépenses du 1° du I (rémunérations et charges liées), 75 % des congrès et 30 % des CA génériques/orphelins éligibles. Taux marginaux 19 %, 29 %, 36 %, 39 % selon R (assiette nette/CA pertinent) inférieur à 6,5 %, de 6,5 à moins de 12 %, de 12 à moins de 14 %, au moins 14 %. Exonération sous 15 millions d'euros sous conditions de groupe.",
                "Aucune contribution sur les charges comptabilisées dès l'entrée en vigueur, sans taxe de remplacement ; assiette, taux et avantages anciens pour les charges antérieures uniquement.",
                'percent',"Entreprises du champ pharmaceutique de L245-1, quelle que soit leur taille ou modalité d'exploitation.",
                "Bascule à la comptabilisation ; exercices mixtes limités aux charges antérieures, sans prorata supplémentaire des avantages.",
                "Aucune taxe ni formalité de remplacement ; obligations communes et contrôles sur le stock conservés.",
                "Il est institué au profit de la caisse nationale de l'assurance maladie une contribution des entreprises assurant l'exploitation en France",
                "La contribution instituée au profit de la Caisse nationale de l'assurance maladie n'est plus due à raison des charges comptabilisées à compter de cette date, quelle que soit la date de clôture de l'exercice ou d'échéance.")]),
    "Contribution pharmaceutique de promotion supprimée sur toutes charges comptabilisées dès l'entrée en vigueur, sans nouveau prélèvement ; ancien stock seul conservé.")

p13 = paragraphs(date_clause,
    "Aucune assiette ni aucun taux de la contribution ne s'applique aux charges comptabilisées à compter de cette date.",
    stock, mixed_year,
    "Pour les charges antérieures, les exclusions d'assiette, la répartition forfaitaire lorsque les charges ne peuvent être isolées, les abattements du II, leur report entre entreprises du même groupe et le barème du III restent applicables dans les conditions antérieures. La suppression des charges nouvelles de l'assiette ne réduit aucun de ces avantages.",
    no_future_form)
repeal(13,p13,
    "Coordination de fond de l'abolition portée par L245-1 : extinction pour les charges nouvelles de l'assiette, du rapport R, du barème et des calculs exclusivement nécessaires à la contribution. Le tableau entier, ses quatre taux et sa note de première application ont été examinés ; ils ne sont pas recopiés car ils n'ont plus de champ prospectif. Tous les allègements restent opérants pour les charges anciennes, y compris lorsque l'exercice clôture après la bascule.",
    med_notes + " Contrôle de chiffres : 2,5 millions d'euros, 3 %, 75 %, deux abattements de 30 %, seuil des médicaments orphelins de 30 millions d'euros, rapport arrondi au centième par défaut ; tranches 6,5/12/14 et taux 19/29/36/39. Les conditions des génériques, du tarif de responsabilité, des prix identiques et du report de groupe ne sont pas élargies pour le stock. Le tableau ne disparaît que parce que le prélèvement entier est supprimé pour les charges nouvelles. La note de 2005 ne fixe pas la réforme future.",
    impact('coordination_only',
        "L'assiette et le barème entiers cessent pour les charges nouvelles par coordination de l'unique suppression L245-1. Les calculs favorables anciens restent applicables ; aucune deuxième taxe supprimée n'est comptée.",
        tax_limit, tax_burdens,
        [effect('coordination',MED,
                "Extinction prospective de l'assiette et du barème, avec maintien des abattements pour le stock.",
                "Charges des 1° à 4° du I, rapport forfaitaire si nécessaire, abattements du II et barème marginal 19/29/36/39 %.",
                "Plus d'assiette ni de taux pour les charges nouvelles ; calculs antérieurs entiers pour le stock, sans prorata supplémentaire des avantages.",
                'regime','Même population pharmaceutique que la suppression portée à L245-1.',
                "Date de comptabilisation commune à L245-1 ; exercices mixtes sans réduction additionnelle d'abattement.",
                "Pas de nouveau suivi réglementaire ; dates et comptabilité existantes pour les seules liquidations anciennes.",
                "La contribution est assise sur les charges comptabilisées au cours du ou des exercices clos depuis la dernière échéance au titre :",
                "Aucune assiette ni aucun taux de la contribution ne s'applique aux charges comptabilisées à compter de cette date.")]),
    "Assiette, abattements et barème de la contribution pharmaceutique devenus sans objet pour les charges nouvelles, avec maintien entier des allègements du stock.",
    benefit_review=("Examen des avantages : exclusion des véhicules du 2°, exclusion des échantillons et des publications consacrées exclusivement à une spécialité non inscrite sur les listes visées et non prise en charge au titre des dispositifs visés au 3°, limitation des seules rémunérations pertinentes du 1°, répartition forfaitaire et arrondi au centième par défaut lorsque l'isolement comptable est impossible ; abattement forfaitaire de 2,5 millions d'euros modulé selon la durée, 3 % des dépenses du 1° du I, comprenant rémunérations et charges liées, et 75 % des frais de congrès ; abattements de 30 % du chiffre d'affaires des génériques sous leurs exceptions de prix/tarif et des médicaments orphelins dont le chiffre d'affaires hors taxes n'excède pas 30 millions d'euros, et report des excédents de ces deux derniers au sein du groupe. Tous restent applicables aux charges antérieures selon leur champ et conditions, même pour une clôture ultérieure et sans prorata supplémentaire à cause de la réforme. Pour toutes les charges nouvelles, y compris les futures situations qui auraient rempli ces conditions, la contribution est intégralement supprimée sans substitution ni extension d'assiette ; ces avantages ne sont donc pas retirés au profit d'une charge générale maintenue."))

p14 = paragraphs(date_clause,
    "Aucune déclaration, mise en recouvrement, majoration, pénalité ou taxation provisionnelle ou forfaitaire ne peut être fondée sur cet article pour les charges comptabilisées à compter de cette date.",
    stock,
    "Pour les seules charges antérieures, les règles de recouvrement, de contrôle, de sanction et les garanties antérieures demeurent applicables, sous réserve de la loi répressive plus douce dans son champ. Elles ne peuvent imposer la déclaration de charges nouvelles non soumises à cette contribution. Les contributions et obligations ayant un fondement distinct demeurent applicables.")
repeal(14,p14,
    "Coordination nécessaire : éteindre les procédures et l'habilitation réglementaire exclusivement liées à la contribution supprimée, afin qu'un renvoi à L138-20 à L138-23 ne rétablisse ni déclaration ni taxation forfaitaire sur des charges nouvelles. Les moyens de contrôle, garanties et voies de restitution pour le stock ancien sont conservés ; il ne s'agit pas d'une deuxième abolition fiscale.",
    med_notes + " L'habilitation à préciser majorations, pénalités et taxation provisoire n'a plus de champ nouveau. Une sanction autonome d'une autre contribution n'est pas supprimée par le retrait de ce renvoi ; pour le stock, réserver la loi répressive plus douce.",
    impact('coordination_only',
        "Le recouvrement et les sanctions propres ne peuvent survivre sur les charges nouvelles après l'abolition de L245-1. Ce retrait d'exécution coordonne la même mesure, sans compter une formalité générale distincte supprimée.",
        tax_limit, tax_burdens,
        [effect('coordination',MED,
                "Limitation du renvoi aux procédures communes et de l'habilitation de sanction au stock imposable.",
                "Recouvrement et contrôle par renvoi à L138-20 à L138-23, modalités réglementaires incluant majorations et taxations provisionnelles ou forfaitaires.",
                "Procédures seulement pour les charges antérieures ; aucune taxation ni déclaration de la contribution supprimée pour les charges nouvelles.",
                'legal_duty','Entreprises anciennement redevables de la contribution pharmaceutique.',
                "Bascule commune des charges ; contrôles et garanties anciens conservés.",
                "Aucune procédure de remplacement ; obligations des autres contributions inchangées.",
                "La contribution est recouvrée et contrôlée en application des dispositions prévues aux articles L. 138-20 à L. 138-23.",
                "Aucune déclaration, mise en recouvrement, majoration, pénalité ou taxation provisionnelle ou forfaitaire ne peut être fondée sur cet article pour les charges comptabilisées à compter de cette date.")]),
    "Procédure, habilitation de majorations et taxations propres à la contribution pharmaceutique pour les seules charges nouvelles.")

p15 = paragraphs(date_clause,
    "Aucune entreprise n'est redevable de la contribution pour les charges comptabilisées à compter de cette date, y compris lorsqu'elle aurait dépassé les seuils de chiffre d'affaires ou relevé des exclusions liées à la détention de capital prévues par les dispositions antérieures.",
    stock, mixed_year,
    "Pour les charges antérieures, l'exonération liée au chiffre d'affaires inférieur à 15 millions d'euros, ses règles de consolidation et de détention d'au moins 50 % ainsi que sa modulation pour les exercices de durée différente de douze mois restent applicables dans les conditions antérieures. La présente abrogation ne restreint aucun droit à exonération au titre de ces charges.")
repeal(15,p15,
    "Coordination nécessaire d'une exonération dont le prélèvement de référence est supprimé pour toutes les charges nouvelles. L'avantage des entreprises sous 15 millions d'euros n'est pas révoqué pendant que la taxe subsiste : il reste intégralement applicable au stock ancien, avec ses conditions, et les entreprises nouvelles ou nouvellement éligibles ne supportent plus cette taxe du tout. Aucune transformation de l'exonération en aide fermée aux situations futures.",
    med_notes + " Maintien pour le stock du seuil strictement inférieur à 15 millions d'euros, des participations à 50 % au moins, de la consolidation et de la modulation des exercices autres que douze mois. L'ancien renvoi aux quatre derniers alinéas couvre les exclusions de groupe et la modulation ; aucune de ces conditions n'est perdue pour les anciennes liquidations.",
    impact('coordination_only',
        "L'exonération conserve son effet sur toute charge ancienne encore taxable. Pour les charges nouvelles, l'abolition générale rend les seuils inutiles sans perte d'avantage ni taxe de remplacement.",
        tax_limit, tax_burdens,
        [effect('coordination',MED,
                "Articulation de l'exonération des petites entreprises avec l'abolition générale de la contribution.",
                "Exonération sous 15 millions d'euros, sous exclusions de groupe à 50 % au moins et modulation de durée d'exercice.",
                "Même exonération pour le stock ancien ; toutes charges nouvelles hors contribution, même pour les entreprises hors exonération.",
                'regime','Entreprises pharmaceutiques sous seuil et entreprises futures, sans restriction nouvelle.',
                "Anciennes charges selon le droit antérieur ; charges nouvelles exonérées de toute contribution du régime par abolition.",
                "Aucune demande d'exonération nouvelle pour des charges non imposables ; pas de condition ou taxe de remplacement.",
                "Sont exonérées de cette contribution, sous réserve des dispositions prévues aux quatre derniers alinéas, les entreprises",
                "La présente abrogation ne restreint aucun droit à exonération au titre de ces charges.")]),
    "Exonération et exclusions de la contribution pharmaceutique pour charges nouvelles, devenues sans objet du fait de l'abolition générale sans remplacement.",
    benefit_review=("L'avantage examiné est l'exonération lorsque le chiffre d'affaires pertinent est strictement inférieur à 15 millions d'euros, avec le champ des spécialités enregistrées, autorisées ou prises en charge, les exclusions pour filiales ou sociétés détenant au moins 50 % au sein d'un ensemble dépassant ce seuil et la modulation selon la durée des exercices. La nouvelle règle conserve toutes ces conditions pour les charges antérieures, même si l'échéance ou la clôture est future. Pour les charges comptabilisées dès l'entrée en vigueur, le prélèvement est entièrement supprimé pour toutes les entreprises, y compris celles qui deviendraient éligibles à l'exonération après la réforme ; aucun impôt équivalent ni extension d'assiette n'en réduit l'avantage."))

p16 = paragraphs(date_clause,
    "L'exclusion des charges déductibles prévue par les dispositions antérieures demeure applicable aux seules contributions se rapportant à des charges comptabilisées avant cette date, même lorsque leur paiement ou leur comptabilisation intervient ultérieurement.",
    "Aucune contribution ne peut être rétablie pour des charges comptabilisées à compter de cette date du fait de cette règle de non-déductibilité. Aucun droit à déduction d'une contribution non due n'est créé. Les rectifications, restitutions, prescriptions et recours relatifs aux impositions et contributions antérieures demeurent régis par les règles qui leur sont applicables.")
repeal(16,p16,
    "Coordination nécessaire : la non-déductibilité de la contribution ne doit pas survivre comme une charge autonome ni créer une déduction fictive après l'abolition. Les contributions liées aux charges anciennes gardent exactement leur traitement à l'IR ou à l'IS, même comptabilisées ou payées après la réforme ; aucune rétroactivité fiscale ou assimilation à un nouveau taux d'IS.",
    med_notes + " Cette coordination ne modifie pas le calendrier propre de l'IS à la distribution, les réserves déjà taxées, les crédits ni le minimum international. Les coordinations éventuelles du CGI pour les seules contributions anciennes sont à vérifier dans leurs articles, sans inventer un renvoi non fourni.",
    impact('coordination_only',
        "La non-déductibilité reste attachée au stock de contribution réellement dû ; elle cesse sans objet pour les charges nouvelles. Aucun nouveau gain d'IR ou d'IS distinct de l'abolition n'est revendiqué.",
        "L'impôt sur les bénéfices et ses régimes distincts ne sont pas réécrits par cet article. Aucun montant de déduction ou de rendement n'est calculé.",
        "Aucune charge nouvelle identifiée : pas de suivi fiscal autonome nouveau ; seule l'identification comptable de la contribution ancienne réellement due demeure.",
        [effect('coordination',MED,
                "Cantonnement de la non-déductibilité à la contribution ancienne effectivement due.",
                "Contribution exclue des charges déductibles à l'IR ou à l'IS.",
                "Même non-déductibilité pour le stock ancien ; aucune contribution ni déduction fictive pour les charges nouvelles.",
                'regime',"Entreprises relevant de la contribution pharmaceutique imposables à l'IR ou à l'IS.",
                "Qualification par date des charges sous-jacentes, même si la contribution ancienne est payée plus tard.",
                "Aucun impôt ni déclaration de remplacement.",
                "La contribution est exclue des charges déductibles pour l'assiette de l'impôt sur le revenu ou de l'impôt sur les sociétés.",
                "Aucun droit à déduction d'une contribution non due n'est créé.")]),
    "Non-déductibilité sans objet pour la contribution pharmaceutique supprimée sur charges nouvelles, avec traitement fiscal ancien conservé pour le stock.")

p17 = paragraphs(date_clause,
    "Aucun versement provisionnel ni aucune régularisation ne peut être exigé au titre de la contribution sur des charges comptabilisées à compter de cette date.",
    "Pour les seules charges comptabilisées avant cette date, le versement provisionnel au 1er juin, calculé à 75 % de la contribution due au titre de l'année précédente, et la régularisation au 1er octobre de l'année suivante demeurent applicables dans les conditions antérieures. Un versement provisionnel ne peut excéder la contribution restant légalement due pour ces charges antérieures.",
    "Les versements déjà effectués sont imputés sur les seules contributions restant dues ; leur excédent est restituable selon les règles de réclamation applicables. Une même somme ne peut être imputée ou remboursée deux fois. Les droits, prescriptions et recours relatifs aux périodes antérieures sont conservés. Aucune régularisation annuelle à néant n'est exigée pour les seules charges nouvelles.")
repeal(17,p17,
    "Coordination de l'abolition : suppression des acomptes et régularisations concernant les charges nouvelles, afin que le calendrier annuel ne recrée pas le prélèvement. Le 75 % au 1er juin et le 1er octobre de l'année suivante sont conservés pour le stock seulement, avec plafonnement au reliquat légal et restitution des indus. La disparition de l'acompte découle de la suppression définitive du principal, pas d'un simple report de cotisations.",
    med_notes + " La note de la loi 2025-1403 rend le calendrier source applicable à partir des contributions dues pour 2026 et prévoit l'entrée immédiate : ce sont des faits historiques, non la date de la présente abrogation. Aucun acompte calculé sur l'année ancienne ne doit maintenir une dette sur des charges nouvelles. Échéances résiduelles et remboursements doivent rester dédupliqués.",
    impact('coordination_only',
        "L'extinction des avances sur les charges nouvelles met en œuvre la même abolition de L245-1. Le reliquat ancien garde son calendrier, sans paiement supérieur au principal résiduel ni double remboursement.",
        tax_limit, tax_burdens,
        [effect('coordination',MED,
                "Extinction du calendrier d'acomptes pour les charges non imposables après abolition.",
                "75 % de la contribution de l'année précédente au 1er juin ; régularisation le 1er octobre de l'année suivante.",
                "Calendrier seulement pour le stock imposable, plafonné au reliquat ; aucun acompte sur les charges nouvelles, excédents restituables.",
                'legal_duty',"Entreprises redevables de versements provisionnels pharmaceutiques et détentrices d'acomptes excédentaires.",
                "Application de la bascule comptable commune ; anciennes échéances non transformées en dette nouvelle.",
                "Aucune déclaration annuelle à néant ou garantie de remplacement ; remboursement sans double emploi.",
                "La contribution est versée de manière provisionnelle le 1er juin de chaque année, pour un montant correspondant à 75 % de la contribution due au titre de l'année précédente.",
                "Aucun versement provisionnel ni aucune régularisation ne peut être exigé au titre de la contribution sur des charges comptabilisées à compter de cette date.")]),
    "Acomptes et régularisations de la contribution pharmaceutique pour charges nouvelles ; seul calendrier résiduel de l'ancien principal conservé.")

p18 = paragraphs(date_clause,
    "La contribution instituée au profit de la Caisse nationale de l'assurance maladie sur les dépenses de promotion des dispositifs médicaux, tissus, cellules, dérivés, autres produits de santé et prestations associés relevant de son champ n'est plus due à raison des charges comptabilisées à compter de cette date, quelle que soit la date de clôture de l'exercice ou d'échéance.",
    stock, mixed_year, no_future_form, no_new_tax)
repeal(18,p18,
    "Réforme de fond : suppression de la contribution sur les dépenses de promotion des produits et prestations du champ des titres Ier et III de L165-1. Ce prélèvement accessoire sur les fabricants, importateurs et distributeurs est distinct des obligations de sécurité, des évaluations et de la prise en charge médicale, qui restent applicables. Le taux de 15 % ne reçoit aucun taux intermédiaire ou substitut. Les dettes et tous les avantages sur les charges antérieures sont conservés.",
    dm_notes + " Le champ source inclut les tissus et cellules humains quel que soit leur degré de transformation et leurs dérivés, les autres produits de santé et les services/adaptations associés ; l'abrogation couvre ce champ entier, sans le limiter aux seuls dispositifs au sens étroit. Aucun changement de remboursement ou reste à charge des patients n'est décidé.",
    impact('material_reduction',
        "La contribution entière est supprimée pour les dépenses nouvelles de toute la population source. Il ne s'agit ni d'un report de paiement ni d'une suppression de prestations de santé ; les anciennes charges gardent leur régime.",
        tax_limit, tax_burdens,
        [effect('tax_removed',DM,
                "Abolition prospective de la contribution sur la promotion des dispositifs et produits de santé de ce champ.",
                "Fabricants, importateurs et distributeurs du champ : rémunérations et charges associées des personnes présentant/promouvant/vendant les produits, déplacements hors véhicules mis à disposition, repas/hébergement, publications, publicité, congrès et externalisation HT, avec répartition forfaitaire si nécessaire ; abattements de 50 000 euros modulés et 75 % des frais de congrès. Taux 15 % de cette assiette nette ; exonération sous 11 millions d'euros de CA pertinent sous conditions de groupe.",
                "Aucune contribution sur les charges comptabilisées dès l'entrée en vigueur pour tout ce champ, sans remplacement ; ancienne contribution seulement sur les charges antérieures.",
                'percent','Entreprises de fabrication, importation ou distribution des dispositifs, produits, tissus, cellules, dérivés et prestations visés à L245-5-1.',
                "Bascule à la comptabilisation ; exercices mixtes sans prorata supplémentaire des abattements ou seuils.",
                "Aucune contribution ni déclaration de remplacement ; obligations sanitaires et autres prélèvements distincts demeurent.",
                "une contribution des entreprises assurant la fabrication, l'importation ou la distribution en France de dispositifs médicaux à usage individuel",
                "La contribution instituée au profit de la Caisse nationale de l'assurance maladie sur les dépenses de promotion des dispositifs médicaux, tissus, cellules, dérivés, autres produits de santé et prestations associés relevant de son champ n'est plus due à raison des charges comptabilisées à compter de cette date, quelle que soit la date de clôture de l'exercice ou d'échéance.")]),
    "Contribution de promotion des dispositifs, produits de santé et prestations supprimée sur toutes charges nouvelles, sans prélèvement de remplacement.")

p19 = paragraphs(date_clause,
    "Aucune assiette ni aucun taux de la contribution ne s'applique aux charges comptabilisées à compter de cette date.",
    stock, mixed_year,
    "Pour les charges antérieures, les limitations et exclusions d'assiette, la répartition forfaitaire lorsque la comptabilité ne permet pas d'isoler les charges, l'arrondi du rapport au centième par défaut, l'abattement forfaitaire de 50 000 euros avec sa modulation de durée, l'abattement de 75 % des frais de congrès et le taux de 15 % restent applicables selon les dispositions antérieures. La suppression des charges nouvelles de l'assiette ne réduit aucun de ces avantages.",
    no_future_form)
repeal(19,p19,
    "Coordination nécessaire de L245-5-1 : extinction de la définition des dépenses taxables et du taux de 15 % pour les charges nouvelles. Les sept alinéas entiers, y compris les prestations externalisées, la répartition forfaitaire, les exclusions et les deux abattements, ont été examinés. Tous les mécanismes favorables restent applicables au stock ancien, sans prorata additionnel lié à l'abrogation ; aucune deuxième baisse de taxe n'est comptée.",
    dm_notes + " Contrôle des conditions : rémunérations seulement afférentes à la présentation/promotion/vente des titres Ier et III, exclusion des charges de véhicules mis à disposition, prestations externalisées au montant HT, rapport arrondi au centième par défaut, 50 000 euros modulés selon la durée différente de douze mois, 75 % des congrès et taux 15 %. La mention source 'aux titres Ier et III sur la liste' est préexistante ; elle n'est pas silencieusement réinterprétée pour les liquidations anciennes.",
    impact('coordination_only',
        "Le taux de 15 % et son assiette entière cessent pour les charges nouvelles par coordination de l'abolition unique de L245-5-1. Les abattements et modalités favorables restent pour les charges anciennes imposables.",
        tax_limit, tax_burdens,
        [effect('coordination',DM,
                "Extinction de l'assiette et du taux, avec maintien des exclusions et abattements sur le stock.",
                "Dépenses des 1° à 4°, répartition forfaitaire si nécessaire, abattements de 50 000 euros modulés et 75 % des congrès ; taux 15 %.",
                "Aucune assiette ni taux sur les charges nouvelles ; mêmes règles et avantages pour le stock antérieur.",
                'regime','Même population que la suppression portée à L245-5-1, y compris les entreprises utilisant des prestataires externalisés.',
                "Bascule comptable commune ; aucune réduction des abattements du seul fait du découpage transitoire.",
                "Pas de déclaration ou registre de substitution ; utilisation des écritures existantes pour le stock.",
                "Le taux de la contribution est fixé à 15 %.",
                "Aucune assiette ni aucun taux de la contribution ne s'applique aux charges comptabilisées à compter de cette date.")]),
    "Assiette, taux de 15 % et calculs de contribution sur la promotion des dispositifs et produits de santé pour toutes charges nouvelles.",
    benefit_review=("Les avantages possibles examinés sont la limitation des rémunérations aux activités et produits précisément visés, l'exclusion des charges relatives aux véhicules mis à disposition, la répartition forfaitaire des charges non isolables et l'arrondi au centième par défaut, l'abattement forfaitaire de 50 000 euros avec modulation pour les exercices autres que douze mois, et l'abattement de 75 % des frais de congrès. Le montant hors taxe des prestations externalisées délimite l'assiette et n'est pas une exonération autonome supprimée. Toutes ces règles restent applicables aux charges antérieures avec les mêmes conditions, même si la clôture ou le paiement est ultérieur. Les futures charges de toute entreprise, y compris nouvellement éligible à ces allègements, sont entièrement soustraites à la contribution sans remplacement ni extension d'assiette ; aucun avantage n'est fermé tandis qu'une charge générale correspondante subsisterait."))

p20 = paragraphs(date_clause,
    "Aucune entreprise n'est redevable de la contribution pour les charges comptabilisées à compter de cette date, y compris lorsqu'elle aurait dépassé les seuils de chiffre d'affaires ou relevé des exclusions liées à la détention de capital prévues par les dispositions antérieures.",
    stock, mixed_year,
    "Pour les charges antérieures, l'exonération liée au chiffre d'affaires inférieur à 11 millions d'euros, ses règles de consolidation et de détention d'au moins 50 % ainsi que sa modulation pour les exercices de durée différente de douze mois restent applicables dans les conditions antérieures. La présente abrogation ne restreint aucun droit à exonération au titre de ces charges.")
repeal(20,p20,
    "Coordination de l'abolition de L245-5-1 : l'exonération sous 11 millions d'euros n'est pas supprimée pendant que la contribution générale subsiste. Elle reste intégralement utilisable pour les seules charges anciennes, avec ses règles de groupe et de durée ; toutes les charges nouvelles sortent du prélèvement, y compris pour les entreprises qui accéderaient ultérieurement au champ de l'avantage. Aucun droit n'est limité aux seuls bénéficiaires déjà identifiés.",
    dm_notes + " Conserver sur le stock le seuil strictement inférieur à 11 millions d'euros, les deux exclusions à 50 % au moins, la consolidation et la modulation selon la durée des exercices. La source omet grammaticalement 'en' avant France métropolitaine : incohérence éditoriale signalée, sans étendre ni réduire le champ territorial de l'ancien régime. La proposition n'est pas un crédit d'impôt remboursable sans taxe.",
    impact('coordination_only',
        "L'exonération reste pleinement applicable aux charges anciennes. Sa disparition prospective de structure découle de l'abolition de toute la contribution sur les charges nouvelles, sans restriction d'avantage ni seconde taxe supprimée.",
        tax_limit, tax_burdens,
        [effect('coordination',DM,
                "Articulation de l'exonération de chiffre d'affaires avec la suppression générale de la contribution.",
                "Exonération sous 11 millions d'euros, sous exclusions de groupe à au moins 50 % et modulation de durée.",
                "Exonération conservée pour le stock imposable ; toutes charges nouvelles hors prélèvement, même au-delà des seuils.",
                'regime',"Entreprises de dispositifs et autres produits du champ, y compris futures entreprises anciennement éligibles à l'exonération.",
                "Bascule comptable commune ; conditions anciennes seulement pour le stock antérieur.",
                "Aucune nouvelle demande, attestation ou condition pour les charges nouvelles non imposables.",
                "Sont exonérées de cette contribution, sous réserve des dispositions prévues aux quatre derniers alinéas, les entreprises",
                "La présente abrogation ne restreint aucun droit à exonération au titre de ces charges.")]),
    "Régime d'exonération de la contribution sur dispositifs et produits de santé pour charges nouvelles, rendu sans objet par l'abolition de la taxe entière.",
    benefit_review=("L'avantage est l'exonération des entreprises dont le chiffre d'affaires pertinent est strictement inférieur à 11 millions d'euros dans le champ des produits et prestations de la liste L165-1. Ses limites sont les deux cas de détention d'au moins 50 % et de chiffre d'affaires consolidé dépassant ce montant, ainsi que la modulation pour une durée d'exercices autre que douze mois. La nouvelle règle préserve l'exonération et toutes ses conditions pour toute contribution résiduelle relative aux charges antérieures, y compris liquidée ultérieurement. Pour les charges nouvelles, la contribution correspondante est entièrement supprimée pour tous, sans taxation équivalente ou extension d'assiette : les futures entreprises ou situations qui auraient accédé à l'avantage ne sont donc pas exclues du bénéfice de la réforme."))

p21 = paragraphs(date_clause,
    "L'exclusion des charges déductibles prévue par les dispositions antérieures demeure applicable aux seules contributions se rapportant à des charges comptabilisées avant cette date, même lorsque leur paiement ou leur comptabilisation intervient ultérieurement.",
    "Aucune contribution ne peut être rétablie pour des charges comptabilisées à compter de cette date du fait de cette règle de non-déductibilité. Aucun droit à déduction d'une contribution non due n'est créé. Les rectifications, restitutions, prescriptions et recours relatifs aux impositions et contributions antérieures demeurent régis par les règles qui leur sont applicables.")
repeal(21,p21,
    "Coordination de l'abolition : la non-déductibilité de la contribution sur les dispositifs ne peut plus avoir d'objet sur les charges nouvelles. Elle reste applicable aux contributions résiduelles réellement dues pour le stock ancien, même payées plus tard. Aucune déduction d'impôt fictive, restitution générale ou modification implicite de l'IS à la distribution n'est créée.",
    dm_notes + " La note de 2003 fixe la première assiette d'application de l'ancien régime ; elle ne fixe aucune date de la réforme proposée. La fiscalité des bénéfices, les crédits et l'absence de double imposition des réserves ont leur champ propre. Les renvois du CGI éventuellement utiles aux anciennes contributions doivent être vérifiés dans leurs sources, non reconstruits ici.",
    impact('coordination_only',
        "La non-déductibilité du stock reste inchangée et aucun montant de contribution supprimée n'est artificiellement déduit. L'effet est une coordination de la même abolition, non une baisse autonome d'IR ou d'IS.",
        "L'article ne réforme pas la fiscalité générale des bénéfices ni les droits antérieurs de contestation. Aucun rendement fiscal global ou taux effectif n'est établi.",
        "Aucune charge nouvelle identifiée : pas de justificatif ou registre supplémentaire. L'identification des contributions anciennes relève des écritures déjà nécessaires à leur liquidation.",
        [effect('coordination',DM,
                "Maintien de la non-déductibilité sur le stock réel, extinction de son objet sur les charges nouvelles.",
                "Contribution exclue des charges déductibles à l'IR et à l'IS.",
                "Règle conservée sur les contributions anciennes dues ; aucune contribution ni déduction fictive pour les charges nouvelles.",
                'regime',"Entreprises de dispositifs et produits du champ relevant de l'IR ou de l'IS.",
                "Date des charges sous-jacentes, indépendamment du paiement ou de la comptabilisation ultérieure de la contribution.",
                "Aucune obligation de substitution et aucun impôt supplémentaire.",
                "La contribution est exclue des charges déductibles pour l'assiette de l'impôt sur le revenu ou de l'impôt sur les sociétés.",
                "Aucun droit à déduction d'une contribution non due n'est créé.")]),
    "Non-déductibilité devenue sans objet pour la contribution sur dispositifs supprimée sur charges nouvelles, avec traitement fiscal ancien conservé.")

p22 = paragraphs(date_clause,
    "Aucun versement provisionnel ni aucune régularisation ne peut être exigé au titre de la contribution sur des charges comptabilisées à compter de cette date.",
    "Pour les seules charges comptabilisées avant cette date, le versement provisionnel au 1er juin, calculé à 75 % de la contribution due au titre de l'année précédente, et la régularisation au 1er octobre de l'année suivante demeurent applicables dans les conditions antérieures. Un versement provisionnel ne peut excéder la contribution restant légalement due pour ces charges antérieures.",
    "Les versements déjà effectués sont imputés sur les seules contributions restant dues ; leur excédent est restituable selon les règles de réclamation applicables. Une même somme ne peut être imputée ou remboursée deux fois. Aucune régularisation annuelle à néant n'est exigée pour les seules charges nouvelles.",
    "Le recouvrement, le contrôle, les majorations, pénalités et taxations provisionnelles ou forfaitaires antérieurement applicables demeurent réservés aux seules contributions relatives aux charges antérieures, avec leurs garanties, prescriptions, restitutions et recours et sous réserve de la loi répressive plus douce dans son champ. Aucune donnée concernant les charges nouvelles ne peut être exigée au seul titre de cette contribution supprimée ; les obligations ayant un fondement distinct demeurent applicables.")
repeal(22,p22,
    "Coordination nécessaire : retirer les acomptes, régularisations et procédures exclusivement liés aux charges désormais non imposables ; conserver le calendrier et les garanties de recouvrement sur le stock ancien. Le plafond du reliquat dû évite qu'un acompte fondé sur l'année précédente maintienne le prélèvement aboli ; les indus restent restituables sans double emploi. L'article ne constitue pas une suppression supplémentaire de contribution ni un simple report du principal nouveau.",
    dm_notes + " Les deux alinéas source ont été examinés, y compris le calendrier de 75 % au 1er juin et régularisation le 1er octobre de l'année suivante et la désignation de l'ACOSS pour le recouvrement. Les notes d'application aux contributions dues dès 2026 ne fixent pas la présente bascule. L138-20 prévoit les organismes désignés par le directeur de l'ACOSS : articulation préexistante à respecter pour le stock, non une nouvelle compétence inventée. Le retrait n'emporte pas les garanties ou sanctions autonomes d'autres prélèvements.",
    impact('coordination_only',
        "Les échéances et la procédure ne peuvent recréer la contribution abolie sur les charges nouvelles. Le stock garde ses échéances et garanties ; les acomptes excédentaires ne sont ni conservés sans dette ni remboursés deux fois.",
        tax_limit, tax_burdens,
        [effect('coordination',DM,
                "Extinction des acomptes et procédures pour les charges nouvelles, maintien du recouvrement résiduel.",
                "Acompte de 75 % au 1er juin, régularisation au 1er octobre de l'année suivante, recouvrement et contrôle par l'ACOSS et renvoi L138-20 à L138-23.",
                "Calendrier limité à l'ancien reliquat dû, procédures réservées aux charges anciennes ; aucune obligation propre aux seules charges nouvelles.",
                'legal_duty','Entreprises redevables ou ayant versé un acompte de contribution de promotion des dispositifs et produits du champ.',
                "Bascule commune selon la comptabilisation ; remboursements et recours sur le stock préservés.",
                "Aucune déclaration annuelle à néant, garantie ou représentation de remplacement.",
                "La contribution est versée de manière provisionnelle le 1er juin de chaque année, pour un montant correspondant à 75 % de la contribution due au titre de l'année précédente.",
                "Aucun versement provisionnel ni aucune régularisation ne peut être exigé au titre de la contribution sur des charges comptabilisées à compter de cette date.")]),
    "Acomptes, régularisations, recouvrement et sanctions propres de la contribution sur dispositifs pour les charges nouvelles ; seul stock ancien contrôlable.")

p23 = paragraphs(date_clause,
    "Les dispositions réglementaires prises pour l'application de la présente section ne peuvent maintenir ni rétablir une contribution, une déclaration, un acompte ou une autre formalité se rapportant exclusivement à cette contribution pour les charges comptabilisées à compter de cette date.",
    "Ces dispositions demeurent applicables aux seules contributions se rapportant à des charges comptabilisées avant cette date, même si leur liquidation, leur paiement ou leur contrôle intervient ultérieurement, avec leurs exonérations, abattements, garanties, prescriptions, restitutions et recours. Les autres obligations sanitaires, comptables ou fiscales ayant un fondement distinct ne sont pas modifiées.")
repeal(23,p23,
    "Coordination nécessaire de l'abolition de la section : supprimer l'habilitation générale qui pourrait laisser subsister les formalités du régime pour des charges nouvelles. Les décrets d'exécution conservent leur application résiduelle pour les anciennes contributions, avec tous leurs avantages et garanties. Aucun nouveau pouvoir d'agrément ou de déclaration n'est donné au règlement.",
    dm_notes + " Les R245-16 à R245-16-2 sont les descendants réglementaires lus ; les règles de durée à 360 jours et mois complets de trente jours demeurent pour les anciens calculs. La première application à l'assiette 2003 dans la note reste historique. Les éventuels formulaires et textes extérieurs non joints doivent être coordonnés, sans prétendre leur réécriture exhaustive ni effacer leurs fondements autonomes.",
    impact('coordination_only',
        "L'habilitation réglementaire cesse pour les charges nouvelles afin de rendre l'abolition cohérente jusque dans ses modalités. Les seules règles d'exécution anciennes demeurent, sans compter une seconde réduction de taxe.",
        tax_limit, tax_burdens,
        [effect('coordination',DM,
                "Cantonnement des règlements d'application au stock antérieur de la contribution supprimée.",
                "Habilitation générale d'un décret en Conseil d'Etat pour les modalités de la section.",
                "Aucun règlement ne peut maintenir contribution ou formalité sur les charges nouvelles ; modalités anciennes pour le seul stock.",
                'regime','Entreprises et organismes appliquant la section de contribution sur les dispositifs et produits de santé.',
                "Bascule comptable commune aux articles de la section ; droits et garanties résiduels conservés.",
                "Pas d'habilitation de remplacement ni nouveau formulaire.",
                "Les modalités d'application de la présente section sont définies par décret en Conseil d'Etat.",
                "Les dispositions réglementaires prises pour l'application de la présente section ne peuvent maintenir ni rétablir une contribution, une déclaration, un acompte ou une autre formalité se rapportant exclusivement à cette contribution pour les charges comptabilisées à compter de cette date.")]),
    "Habilitation réglementaire d'application de la contribution sur dispositifs pour charges nouvelles, sans remise en cause des modalités favorables du stock ancien.")

# Les cibles de contrat unique sont examinées dans leur champ réel, sans faire
# passer les notes historiques ou une référence de contexte pour un renvoi normatif.
contexts = {
    0: "L244-4 règle la récidive contraventionnelle sociale et deux peines accessoires, non une rupture d'emploi.",
    1: "L244-5 règle la publication payante d'un jugement social, non les sommes dues lors d'une rupture d'emploi.",
    3: "L244-7 fixe le départ de prescription pénale après un mois de régularisation sociale, non après notification d'une rupture d'emploi.",
    6: "L244-9 porte un titre de recouvrement, son opposition et une exécution provisoire ciblée de travail illégal, non un licenciement.",
    7: "L244-10 protège l'appel des jugements du chapitre social et ne fixe aucune condition de rupture d'emploi.",
    8: "L244-11 allonge à cinq ans des prescriptions en cas de procès-verbal de travail illégal, sans régler la fin de l'emploi.",
    9: "L244-12 suspend des prescriptions pendant une procédure européenne, sans régler le contrat de travail ni sa notification.",
    10: "L244-13 interdit l'assistance rémunérée aux remises sociales ; son abrogation ne règle pas la rupture d'un emploi."
}

for i,a in enumerate(A):
    sk = a['code_id'] + '|' + a['source_id']
    checks = []
    for tk in R['requirements'][sk]:
        t = R['targets'][tk]
        n = t['number']
        context = contexts[i]
        if n == 'L1234-1':
            assessment = context + " La source cible organise le préavis patronal selon six mois/deux ans d'ancienneté ; sa proposition, qui n'est pas le droit en vigueur, prévoit quinze jours calendaires pour les contrats nouveaux et préserve les anciens contrats. Aucun alinéa de cet article social ne vise L1234-1 : le mois de mise en demeure, les délais de sanction ou de recours ne deviennent pas un préavis. Le point de départ de notification propre à la rupture n'est pas importé ; aucune coordination de ce corps n'est nécessaire."
        elif n == 'L1221-2':
            assessment = context + " La source cible admet encore le CDD, tandis que sa proposition interdit les nouveaux termes et réserve les nouvelles embauches au contrat à durée indéterminée, y compris à l'occasion d'un renouvellement ou d'une reconduction, avec transition des contrats antérieurs. Cet article social ne distingue ni CDI/CDD ni durée de mission ou formation : aucun nouveau CDD, ancienneté remise à zéro ou exclusion future d'aide ne résulte du maintien ou de la suppression proposés. Aucun alinéa ne requiert un renvoi au contrat unique ; les régimes publics ne sont pas assimilés au privé."
        elif n == 'L1234-9':
            assessment = context + " La source cible ouvre l'indemnité de licenciement après huit mois, hors faute grave ; la proposition distingue les anciens droits et l'indemnité nouvelle après un an mesuré au terme effectif, préavis inclus, de 0,20 mois par année totale, fractions en mois complets et plafond six mois, à la charge du seul employeur. Cet article social ne vise aucun alinéa de L1234-9 et ne calcule aucune indemnité : ni ce seuil ni la notification de rupture n'y sont importés ; salaires, congés, réparations et indemnités spéciales ne sont pas modifiés."
        elif n == 'L241-3':
            assessment = ("Le seul renvoi normatif actuel de L244-5 à L241-3 concerne le plafond annuel qui borne à 1 % le coût d'insertion du jugement, non l'assiette ou les taux des cotisations vieillesse. La proposition cible conserve le PASS et ajoute un transfert progressif conditionné vers la capitalisation, qui n'est pas une baisse de prélèvement. La suppression de la peine de publication rend ce plafond sans objet pour les faits nouveaux, tandis que le régime ancien reste applicable dans la transition pénale. Aucune condition d'ancienneté, notification d'emploi ou financement de retraite n'est créée par ce renvoi.")
        elif n == 'L623-1':
            assessment = context + " La mention de L623-1 provient des notes historiques d'extension à la vieillesse non salariée. La cible officielle actuelle traite des allocations et indemnités de maternité, paternité, adoption et deuil, avec cessation d'activité et réserve d'égalité de la QPC 2025-1155 : ce n'est plus le même fondement. Aucun renvoi normatif au L623-1 actuel n'est ajouté ; ses prestations et futures situations éligibles restent intactes. Le préavis du contrat privé et son ancienneté ne remplacent aucune durée de cessation ou condition de prestation."
        elif n == 'L244-9':
            if i == 8:
                assessment = ("L244-11 vise réellement la prescription de L244-9 et la porte à cinq ans lorsqu'un procès-verbal constate une infraction de travail illégal. La cible n'a pas de proposition : sa source officielle distingue le délai réglementaire d'opposition, l'exécution provisoire après deux jours calendaires pour les seuls redressements des 1° à 4° de L8211-1 et la prescription triennale de la contrainte définitive, qui est le délai visé ici. Le renvoi reste cohérent sans transformer l'un en l'autre ; il n'importe ni ancienneté d'emploi ni préavis de quinze jours. La note d'application des nouvelles contraintes en 2026/2027 reste à son objet.")
            else:
                assessment = ("L244-12 vise réellement le décompte de la prescription de L244-9, suspendu pendant le dialogue et la conciliation européens. La cible est une source officielle sans proposition : la prescription de trois ans de la contrainte définitive se distingue des délais réglementaires d'opposition et des deux jours d'exécution provisoire ciblée. Le renvoi ne suspend pas indistinctement toutes les voies de recours et ne crée aucun préavis d'emploi ni condition d'ancienneté. La notification ou signification reste celle du recouvrement ; le calendrier de la note 2026/2027 n'est pas remplacé par la réforme du contrat unique.")
        else:
            raise AssertionError(n)
        checks.append(dict(target_key=tk, view_sha256=t['view_sha256'], assessment=assessment))
    a['reference_checks'] = checks

# Citer des phrases ou alinéas complets pour les effets qui portent sur le
# champ entier d'une contribution ou sur la nullité d'une convention.
for i in (1, 12, 18):
    A[i]['substantive_impact']['effects'][0]['source_quote'] = plain(S[i]['source_xml']).strip()
for i in (15, 20):
    first_p = re.search(r'<p>(.*?)</p>', S[i]['source_xml'], re.S).group(1)
    A[i]['substantive_impact']['effects'][0]['source_quote'] = plain(first_p).strip()
A[10]['substantive_impact']['effects'][0]['source_quote'] = re.search(
    r'Sont nulles.*?réglementaires\.', plain(S[10]['source_xml']), re.S).group(0)

Path('answer.json').write_text(json.dumps(A, ensure_ascii=False, indent=2) + '\n')
print('answer.json:',len(A),'articles')
