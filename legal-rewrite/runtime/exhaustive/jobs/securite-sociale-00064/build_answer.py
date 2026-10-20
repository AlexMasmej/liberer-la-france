import json
import re
from html import unescape
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
references = json.loads(Path('reference-targets.json').read_text())
by_number = {s['number']: s for s in sources}


def plain(xml):
    return re.sub(r'\s+', ' ', unescape(re.sub(r'<[^>]+>', ' ', xml or ''))).strip()


def paragraphs(*items):
    return ''.join('<p>' + item + '</p>' for item in items)


proposals = {}
proposals['L461-4'] = paragraphs(
    "Tout employeur qui utilise des procédés de travail susceptibles de provoquer les maladies professionnelles mentionnées à l'article L. 461-2 est tenu, dans les conditions prévues par décret en Conseil d'Etat, d'en faire une déclaration unique à la caisse primaire d'assurance maladie. La caisse transmet cette déclaration à l'inspecteur du travail ou au fonctionnaire qui en exerce les attributions en vertu d'une législation spéciale. La déclaration est établie en un seul exemplaire ; aucun envoi séparé à l'inspecteur du travail ou au fonctionnaire précité ni exemplaire supplémentaire ne peut être exigé de l'employeur au titre du présent article.",
    "Le défaut de déclaration peut être constaté par l'inspecteur du travail ou par le fonctionnaire susmentionnés, qui doit en informer la caisse primaire.",
    "Le dépôt unique s'applique aux déclarations à effectuer à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris lorsque les travaux ont commencé auparavant. Une déclaration déjà reçue par la caisse à cette date n'a pas à être déposée à nouveau ; la caisse en assure, si nécessaire, la transmission au destinataire mentionné au premier alinéa. Les obligations d'information de la caisse d'assurance retraite et de la santé au travail par la caisse primaire demeurent applicables. Les manquements antérieurs conservent leur régime, sous réserve de l'application des dispositions répressives plus douces aux sanctions non définitives."
)

proposals['L461-5'] = paragraphs(
    "Toute maladie professionnelle dont la réparation est demandée en vertu du présent livre doit être, par les soins de la victime, déclarée à la caisse primaire dans un délai déterminé. Lorsque la victime a expressément demandé cette réparation lors de la transmission à la caisse de l'avis prévu à l'article L. 321-2, cette demande vaut déclaration de maladie professionnelle à sa date de réception. Aucune seconde déclaration de la même demande n'est exigée ; les seules informations nécessaires qui manquent à son instruction restent à fournir. La seule transmission d'un avis d'arrêt de travail ne vaut pas demande de reconnaissance du caractère professionnel de la maladie.",
    "Dans le cas prévu au quatrième alinéa de l'article L. 461-2, il est fixé un délai plus long courant à compter de la date d'entrée en vigueur du nouveau tableau annexé au décret.",
    "Le praticien établit et remet à la victime un certificat indiquant la nature de la maladie, notamment les manifestations mentionnées aux tableaux et constatées ainsi que les suites probables. Un seul exemplaire de ce certificat complète la déclaration mentionnée au premier alinéa. Cette déclaration peut être faite au moyen du formulaire déterminé par arrêté ministériel ou sur un autre support comportant les mêmes informations nécessaires à l'instruction de la demande. La caisse réalise les copies nécessaires aux transmissions qui lui incombent ; aucun exemplaire supplémentaire du certificat initial ne peut être exigé de la victime ou du praticien à cette fin.",
    "Une copie de cette déclaration et un exemplaire du certificat médical sont transmis immédiatement par la caisse primaire à l'inspecteur du travail chargé de la surveillance de l'entreprise ou, s'il y a lieu, au fonctionnaire qui en exerce les attributions en vertu d'une législation spéciale.",
    "Sans préjudice des dispositions de l'article L. 461-1, le délai de prescription prévu à l'article L. 431-2 court à compter de la cessation du travail.",
    "Les dispenses de seconde déclaration et de pluralité d'exemplaires ainsi que la faculté d'utiliser un autre support s'appliquent aux formalités à accomplir à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris pour une demande en cours. Aucun nouveau dépôt ni remplacement des pièces déjà reçues n'est exigé. Une demande expresse de réparation déjà reçue avec l'avis mentionné à l'article L. 321-2 conserve sa date de réception pour la poursuite de son instruction. Les délais de déclaration et de prescription, leurs causes de suspension ou d'interruption et les droits résultant de l'article L. 461-1 demeurent applicables ; aucun délai expiré n'est rouvert et aucune restitution générale n'est instituée."
)

proposals['L471-1'] = paragraphs(
    "Les contraventions aux dispositions de l'article L. 441-2, de l'article L. 441-4 et du premier alinéa de l'article L. 441-5 peuvent être constatées par les inspecteurs du travail.",
    "Les manquements des employeurs ou de leurs préposés aux dispositions mentionnées au premier alinéa peuvent donner lieu à la pénalité prévue à l'article L. 114-17-1, dans les conditions de cet article. Le seul manquement à ces formalités ne permet pas à la caisse primaire d'assurance maladie de recouvrer auprès de l'employeur ou de ses préposés la totalité des dépenses faites à l'occasion de l'accident. Les droits de la victime aux prestations et indemnités du présent livre demeurent intégralement applicables.",
    "En outre, la caisse recouvre auprès de l'employeur de toute personne étrangère travaillant ou ayant travaillé pour le compte de celui-ci, sans satisfaire à la condition de régularité de séjour prévue à l'article L. 111-2-3, l'indu correspondant à la totalité des dépenses qu'elle supporte pour cette personne au titre du présent livre. Il en est de même lorsque la victime se trouvait en situation de travail dissimulé au sens des articles L. 8221-3 et L. 8221-5 du code du travail. Si, à l'occasion des faits mentionnés au présent alinéa, il est constaté l'un des faits prévus au premier alinéa du présent article, la caisse peut prononcer la pénalité prévue à l'article L. 114-17-1, sans préjudice d'autres sanctions, le cas échéant.",
    "La suppression du recouvrement fondé sur le seul manquement aux formalités mentionnées au premier alinéa s'applique dès l'entrée en vigueur de la loi portant la présente réforme, y compris aux procédures de recouvrement qui ne sont pas définitivement tranchées à cette date. Elle ne supprime ni les recouvrements fondés sur le troisième alinéa ni les recours fondés sur des dispositions autonomes. Les créances définitivement établies avant cette entrée en vigueur, leurs restitutions, prescriptions et voies de recours encore ouvertes conservent leur régime, sous réserve de l'application des dispositions répressives plus douces. Aucune restitution générale des sommes légalement recouvrées n'est instituée."
)

proposals['L481-1'] = paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant la présente réforme.",
    "A compter de cette date, les projets de création d'établissements de rééducation professionnelle ou de participation à la gestion de tels établissements créés par des oeuvres ou institutions, établis par les caisses de sécurité sociale, ne sont plus soumis à l'autorisation spéciale de l'Etat fondée sur le présent article. Aucune déclaration, demande d'agrément ou autorisation de remplacement ne peut être exigée sur ce seul fondement. Les demandes d'autorisation en cours deviennent sans objet, sans nouveau dépôt.",
    "Les autorisations déjà accordées et les engagements valablement souscrits conservent leurs effets ; aucun renouvellement n'est imposé sur le seul fondement du présent article. Les droits des bénéficiaires de la rééducation professionnelle, les droits des tiers, les créances antérieures et leurs voies de recours sont préservés. Les règles de sécurité, de qualité des soins, d'accessibilité, de contrôle des fonds et les autorisations ou agréments reposant sur un fondement légal autonome demeurent applicables."
)

assert 'au onzième alinéa' in by_number['L491-2']['source_xml']
proposals['L491-2'] = by_number['L491-2']['source_xml'].replace('au onzième alinéa', 'au douzième alinéa')

proposals['L491-4'] = paragraphs(
    "Le demandeur informe le fonds mentionné à l'article L. 723-13-3 du code rural et de la pêche maritime des autres procédures relatives à l'indemnisation des préjudices définis à l'article L. 491-1 du présent code qu'il a engagées. Si une action en justice est intentée, le fonds informe le juge ou la commission de sa saisine à partir des informations qui lui ont été communiquées. Le demandeur n'est pas tenu d'effectuer une seconde notification de la saisine du fonds au juge ou à la commission.",
    "Le fonds peut requérir de tout service de l'Etat, de toute collectivité publique, de tout organisme assurant la gestion des prestations sociales et de tout organisme assureur susceptibles de réparer tout ou partie du préjudice la communication des renseignements relatifs à l'exécution de leurs obligations éventuelles.",
    "Les renseignements ainsi recueillis ne peuvent être utilisés à d'autres fins que l'instruction de la demande faite au fonds d'indemnisation et leur divulgation est interdite. Les personnes qui ont à connaître des documents et informations fournis au fonds sont tenues au secret professionnel.",
    "Le demandeur peut obtenir la communication de son dossier, dans le respect des dispositions de l'article L. 1111-7 du code de la santé publique et sous réserve du secret des affaires.",
    "La notification par le fonds se substitue à celle du demandeur à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris pour les demandes et actions en cours. Une notification déjà effectuée au juge ou à la commission n'a pas à être renouvelée. Aucun nouveau dossier, attestation ou dépôt de remplacement n'est exigé du demandeur pour cette substitution. Elle ne modifie ni l'objet des procédures ni les règles de réparation et de subrogation ; les actes déjà accomplis, les prescriptions et les recours demeurent régis par les dispositions qui leur sont applicables."
)


# Each record contains a specific necessity/reform analysis, not a paraphrase of the source.
analyses = {
    'L461-4': (
        "Réforme de fond : le double circuit de déclaration des procédés dangereux est remplacé par un dépôt unique auprès de la caisse, en un seul exemplaire. L'information de l'inspection du travail est conservée mais sa transmission incombe à la caisse. La constatation du défaut de déclaration et l'information de la caisse par l'inspecteur restent à droit constant. Le risque professionnel justifie de conserver la déclaration de fond ; il ne justifie pas les envois privés parallèles.",
        "R461-4 a été lu en entier dans le corpus : il exige avant travaux un recommandé, deux exemplaires à la caisse et un envoi à l'inspection, puis une transmission caisse–CARSAT. Son dépôt multiple doit être coordonné au dépôt unique législatif ; le moment de déclaration avant travaux et le circuit caisse–CARSAT ne sont pas abolis ici. La proposition ne prétend pas réécrire ce règlement hors lot. L461-2 vise les risques et tableaux, non la durée de l'emploi. Les données de prévention doivent rester disponibles sans nouveau registre. Coût de transmission transféré à la caisse non chiffré.",
        "L'information sur les procédés dangereux demeure une protection pour tous les travailleurs exposés, anciens ou futurs. Aucune exonération, prestation ou dérogation favorable n'est supprimée ; l'allègement porte sur les dépôts parallèles, non sur la reconnaissance de la maladie.",
        'mixed',
        "Un dépôt privé remplace deux destinataires obligatoires et les exemplaires privés multiples sont retirés ; la caisse doit assurer le relais vers l'inspection. Le solde des coûts privés et publics n'est pas établi.",
        "La déclaration de risque, le contrôle et les destinataires de prévention subsistent. L'allègement ne modifie ni les tableaux ni les contributions AT-MP et ne démontre aucune baisse nationale de coût.",
        "Une obligation de transmission à l'inspection est mise à la charge de la caisse à la place de l'employeur. Aucun nouveau renseignement, registre ni dépôt de remplacement n'est imposé à l'employeur ; le coût public du relais reste inconnu."
    ),
    'L461-5': (
        "Réforme de fond : suppression du certificat initial établi en triple et de ses deux exemplaires à joindre, du caractère exclusif du formulaire de déclaration, et de la seconde déclaration lorsque la victime a déjà expressément demandé la réparation avec l'avis d'arrêt de travail. Le certificat médical, son contenu, l'information de l'inspection, le délai plus long lié à un nouveau tableau et les règles de prescription sont conservés. Il ne s'agit pas d'une simple reprise du droit de réemploi des pièces : l'acte initial peut désormais valoir la déclaration spéciale elle-même.",
        "Les cinq alinéas sources gardent leur place ; seule la transition forme un sixième alinéa. R461-5 lu : quinze jours depuis la cessation du travail, trois mois pour le deuxième alinéa ; ces durées ne sont pas remplacées par le préavis du contrat unique. L461-1 lu : date assimilée à l'accident, limite de deux ans et information médicale du lien possible ; le renvoi réserve expressément ces règles à la prescription de L431-2. L321-2 lu : un avis signé d'arrêt de travail n'est pas en lui-même une demande AT-MP, d'où l'exigence d'une demande expresse. R461-6 et R461-9 lus : coordonner les exemplaires initiaux et le formulaire, sans supprimer les examens, le contradictoire ni le délai de cent-vingt jours francs de R461-9. Les certificats ultérieurs de R461-6 restent distincts et leur triple établissement n'est pas déclaré supprimé par ce lot. L'arrêté de formulaire doit être rendu facultatif dans ce champ ; il n'est pas rédigé ici. Aucune date d'entrée en vigueur n'est tirée de la note historique de 2018.",
        "Le délai plus long après extension d'un tableau et les prestations de maladie professionnelle restent ouverts aux nouvelles demandes éligibles. L'allègement n'efface ni certificat médical ni droits à rente ; une simple déclaration de maladie ordinaire n'enclenche pas contre le gré de la victime une demande professionnelle.",
        'mixed',
        "La pluralité d'exemplaires et un second acte déclaratif dans le cas expressément défini sont retirés, et le formulaire devient facultatif. La caisse réalise les copies nécessaires : allègement privé avec traitement public, sans réduction des cotisations revendiquée.",
        "Les délais et conditions médicales sont conservés, le simple arrêt sans demande expresse n'est pas couvert par la fusion. La triple rédaction réglementaire des certificats ultérieurs n'est pas retirée ici ; coût net de reproduction et adaptations des formulaires non établis.",
        "La réalisation des copies nécessaires est explicitement confiée à la caisse. Aucun nouveau renseignement ou justificatif n'est créé pour la victime ou le médecin ; la demande expresse existante et les informations utiles restent nécessaires, avec un coût administratif non chiffré."
    ),
    'L461-6': (
        "Maintien intégral nécessaire après examen : le signalement médical des symptômes toxiques et maladies d'allure professionnelle alimente la prévention et la révision des tableaux. Il a un objet de veille sanitaire distinct de la demande individuelle de réparation de L461-5. La seconde catégorie permet justement de repérer les maladies non encore inscrites ; la supprimer fermerait cette protection aux risques nouveaux.",
        "Aucun taux, délai minimal, agrément ou prélèvement n'est institué par cet article. La liste ministérielle et l'avis du Conseil d'orientation des conditions de travail relèvent de l'identification des risques ; aucune transmission identique au même destinataire n'est démontrée dans la source. Les modalités réglementaires restent à leur champ et aucune réduction de déclaration n'est comptée.",
        "Les futurs malades et travailleurs exposés bénéficient de la détection des pathologies hors liste et de l'évolution des tableaux. L'obligation incombe aux médecins ; ce n'est ni une condition nouvelle de prestation ni un avantage fiscal à supprimer.",
        'retained_necessary',
        "La totalité de la déclaration de veille médicale reste applicable ; aucune réduction n'est revendiquée. Sa fonction de prévention, notamment hors tableaux, diffère d'un dossier d'indemnisation.",
        "La charge de signalement médical subsiste ; aucun doublon exact de destinataire et de finalité n'est démontré. Le lot ne mesure pas son coût et ne réécrit pas sa réglementation.",
        "Aucune charge nouvelle n'est identifiée : l'article est maintenu intégralement, sans formulaire supplémentaire, nouveau délai ou extension de la population déclarante."
    ),
    'L461-7': (
        "Maintien intégral nécessaire : l'habilitation autorise des modalités adaptées à certaines maladies professionnelles. Elle ne crée elle-même ni autorisation préalable, ni déclaration, ni contribution. Son abrogation générale ferait perdre le fondement de régimes spéciaux utiles sans démonstration de la disparition de leur objet sanitaire ou indemnitaire.",
        "La faculté réglementaire ne vaut pas maintien de chaque charge de chaque règlement : les éventuelles contraintes doivent être examinées dans leurs véritables textes. Aucune durée de contrat ou règle de rupture n'est visée et aucune nouvelle habilitation n'est ajoutée.",
        "Les adaptations spéciales, y compris celles susceptibles d'être favorables à la reconnaissance ou à la réparation, conservent leur fondement pour les situations futures recevables. Aucune fermeture aux seuls droits acquis n'est introduite.",
        'retained_necessary',
        "La faculté d'adapter l'application du livre à certaines pathologies est conservée sans création de formalité. Aucun allègement matériel autonome ne résulte du maintien.",
        "Le contenu des décrets spéciaux n'est pas présenté comme examiné ou supprimé par cette habilitation. Leur coût et leurs contraintes propres ne sont pas quantifiés ici.",
        "Aucune charge nouvelle n'est identifiée : le texte d'habilitation est reproduit par maintien de la source, sans condition ni procédure supplémentaire."
    ),
    'L461-8': (
        "Maintien intégral nécessaire de l'indemnité spéciale de changement d'emploi pour pneumoconioses siliceuses, affections liées aux poussières d'amiante et sidérose professionnelle. Elle compense une nécessité médicale lorsque les conditions d'une rente ne sont pas remplies. Aucun doublon avec l'indemnité ordinaire de rupture patronale n'est établi ; lui appliquer un an d'ancienneté ou un plafond de six mois supprimerait un avantage distinct.",
        "Les trois catégories, la nécessité de prévenir l'aggravation et l'absence des conditions ouvrant une rente restent intégrales. L'article ne fixe ni préavis, ni CDD, ni assiette fiscale. Le contrat unique ne ferme pas le droit à un salarié qui doit changer d'emploi pour les mêmes motifs médicaux.",
        "L'indemnité spéciale demeure ouverte aux futurs travailleurs atteints des trois catégories de maladies et devant changer d'emploi, même sans droit à rente. Elle n'est ni absorbée par l'indemnité ordinaire ni subordonnée à son seuil d'ancienneté.",
        'retained_necessary',
        "L'avantage médical et indemnitaire est intégralement préservé, sans modification du champ des trois catégories. Aucun prélèvement ou formalité propre n'est retiré.",
        "La nécessité médicale et l'absence de droit à rente restent requises ; le texte ne réforme pas les autres indemnités ou les montants réglementaires, qui ne sont pas chiffrés ici.",
        "Aucune charge nouvelle n'est identifiée : aucune ancienneté, notification de rupture ou pièce additionnelle n'est introduite dans ce dispositif spécial maintenu."
    ),
    'L471-1': (
        "Réforme de fond : suppression du recours automatique pour la totalité des dépenses AT-MP sur le seul manquement à une formalité des articles L441-2, L441-4 ou L441-5. Ce transfert intégral des dépenses n'est pas nécessaire pour sanctionner le manquement puisque la pénalité proportionnée de L114-17-1 et la constatation des contraventions subsistent. Les recours distincts pour travail dissimulé et défaut de régularité du séjour ainsi que les droits de la victime sont conservés intégralement.",
        "L441-2, L441-4 et L441-5 ont été lus en entier dans le corpus, sources et propositions : la dispense de seconde déclaration déjà communiquée et l'élargissement du registre bénin ne doivent pas être sanctionnés comme des obligations subsistantes. L114-17-1 II 9° demeure le fondement de pénalité pour défaut de déclaration, de feuille et manœuvres privant les victimes de leurs droits ; ses conditions et garanties ne sont pas modifiées ici. Les articles L8221-3 et L8221-5 ne sont pas un préavis ni un régime de CDD ; leur régime n'est pas abrogé. La suppression est étendue aux recouvrements non définitivement tranchés, sans restitution générale des créances définitives ; la qualification répressive éventuelle et la loi plus douce restent à apprécier dans leur champ.",
        "Les prestations et indemnités de la victime restent dues, sans condition nouvelle et y compris pour les accidents futurs. Les dispenses déclaratives favorables proposées en L441-2 et L441-4 ne recréent pas un manquement ; la diminution du recours contre l'employeur ne réduit aucune prestation.",
        'material_reduction',
        "Le paiement de la totalité des dépenses de l'accident ne peut plus être exigé pour le seul défaut de formalité. C'est une obligation pécuniaire retirée, non une baisse de taux de cotisation ; les pénalités et recours autonomes demeurent.",
        "Les dépenses liées au travail dissimulé ou au défaut de séjour régulier restent recouvrables selon le troisième alinéa. Les créances définitives ne sont pas effacées ; incidence sur les recettes et solde public non chiffrés.",
        "Aucune charge nouvelle n'est identifiée : la pénalité renvoie à un régime existant et n'est ni créée ni relevée. Aucun formulaire ou recours préalable de remplacement n'est ajouté à la suppression du recouvrement automatique."
    ),
    'L471-2': (
        "Maintien intégral nécessaire : l'amende de 12 000 euros protège les victimes contre les intermédiaires rémunérés visés à L482-4 et les salariés contre des retenues destinées à financer l'assurance accidents à la place de l'employeur. Ce ne sont pas des cotisations accessoires dues par une activité licite ; leur suppression affaiblirait des protections patrimoniales essentielles.",
        "Le 1° renvoie au second alinéa de L482-4 et non à la rupture d'un contrat de travail. Le 2° interdit le prélèvement salarial pour l'assurance accidents ; le transfert de cotisations vieillesse vers la capitalisation ne l'autorise pas. Le montant de 12 000 euros et les deux incriminations sont conservés sans extension.",
        "L'interdiction de retenues salariales et la protection contre la captation des prestations restent applicables aux futurs salariés et victimes. Aucune exonération d'impôt n'est concernée et aucun droit spécial n'est absorbé par le contrat unique.",
        'retained_necessary',
        "Les deux interdictions protectrices et l'amende de 12 000 euros sont maintenues. Leur maintien ne constitue pas une taxe supprimée ni une réduction de cotisations.",
        "Aucun changement du régime pénal ou de ses conditions n'est proposé ; la source ne démontre pas de doublon dispensable avec une autre incrimination exactement équivalente.",
        "Aucune charge nouvelle n'est identifiée : montant, personnes visées et deux faits réprimés restent ceux de la source officielle entière."
    ),
    'L471-4': (
        "Maintien intégral nécessaire des protections contre le détournement de patients par menaces ou avantages, la falsification médicale consciente et les pressions sur les témoins. Les renvois au code pénal concernent des infractions distinctes ; aucun doublon exact ne permet ici de supprimer la protection spéciale sans laisser un champ de faits sans sanction.",
        "Les trois alinéas, l'amende de 12 000 euros, l'emprisonnement de trois mois, la tentative, le libre choix du médecin et du pharmacien ainsi que les articles 441-7 et 434-13 à 434-15 du code pénal demeurent. Aucun agrément de soins ni dossier supplémentaire ne découle du maintien ; les textes pénaux hors corpus ne sont pas déclarés réécrits.",
        "Le libre choix des soignants et la sincérité de la preuve médicale et testimoniale protègent les victimes futures comme actuelles. Ces garanties ne sont pas des avantages fiscaux et ne sont pas supprimées au titre de la réduction des contraintes.",
        'retained_necessary',
        "Aucune modification normative : les sanctions ciblent la contrainte et l'altération volontaire de la vérité. Aucun allègement de prélèvement ou de procédure licite n'est revendiqué.",
        "Le maintien ne tranche pas les règles de cumul des sanctions pénales, qui gardent leurs garanties propres. Aucun coût national ou effet budgétaire n'est établi.",
        "Aucune charge nouvelle n'est identifiée : les peines, les éléments intentionnels et les comportements sanctionnés restent intégralement ceux de la source."
    ),
    'L481-1': (
        "Abrogation de fond prospective de l'autorisation spéciale de l'Etat imposée aux projets des caisses de création d'établissements de rééducation professionnelle ou de participation à leur gestion. Ce filtre organique propre à la sécurité sociale s'ajoute aux règles autonomes de fonctionnement et de sécurité, qu'il n'est pas nécessaire de remplacer par une nouvelle déclaration. L'abrogation ne retire ni les soins ni les financements valablement engagés.",
        "L'abrogation porte sur tout le corps normatif de L481-1, sans conserver une partie de son autorisation pour l'avenir. R481-1 a été lu : il traite, sur un fondement distinct, de l'équivalence favorable entre un agrément de centre et l'autorisation de dispenser des soins ; cette équivalence n'est pas abolie. Son ancien renvoi à R323-41-1 du code du travail doit faire l'objet d'une concordance propre, non inventée ici. Les éventuelles autorisations médico-sociales, les règles de soins, d'accessibilité et de contrôle des fonds reposant sur d'autres textes restent à leur champ. Leurs textes hors du corpus fourni ne sont pas prétendus réécrits ; la suppression de ce seul filtre ne vaut pas liberté de fonctionner sans protection sanitaire.",
        "Les droits aux prestations de rééducation, les prises en charge et les engagements valablement acquis restent préservés. L'équivalence favorable d'agrément et d'autorisation de soins de R481-1 n'est pas supprimée, y compris pour les futurs centres recevables sur son fondement autonome.",
        'material_reduction',
        "L'autorisation spéciale de création ou de participation à la gestion prévue par ce seul article est entièrement retirée pour l'avenir, sans déclaration de substitution. Les autorisations sanitaires autonomes ne sont pas comptées comme supprimées.",
        "Les décisions acquises et engagements valables subsistent. Le lot ne supprime pas l'ensemble des agréments médico-sociaux et ne chiffre ni le coût du filtre retiré ni le financement des établissements.",
        "Aucune charge nouvelle n'est identifiée : les demandes pendantes deviennent sans objet de plein droit, sans attestation, dépôt ni autorisation de remplacement. Les contrôles autonomes déjà applicables demeurent."
    ),
    'L481-2': (
        "Maintien intégral nécessaire de la restitution des seules sommes indûment perçues en rééducation professionnelle à la suite d'une déclaration inexacte ou incomplète. La règle assure le paiement conforme des prestations ; elle ne crée ni taxe accessoire, ni pénalité automatique sur une prestation légalement due. Supprimer la restitution ferait supporter des paiements sans droit aux régimes sans alléger une condition d'accès légitime.",
        "L'indu doit être établi ; le texte ne présume pas la fraude et ne prononce pas lui-même de peine pénale. Les sanctions pénales seulement réservées gardent leurs propres éléments et garanties. Aucune obligation nouvelle de justificatif, d'agrément ou de notification n'est ajoutée.",
        "Les prestations de rééducation réellement dues restent acquises, pour les situations présentes et futures. Le remboursement ne vise que l'excédent sans droit ; aucune exonération ou dispense favorable n'est retirée par le maintien.",
        'retained_necessary',
        "Le remboursement des indus est conservé sans extension. Aucune économie ou diminution de prélèvement n'est attribuée à une règle de restitution des paiements sans droit.",
        "Les règles de constatation de l'indu, de prescription et de recours demeurent à leurs textes propres. Aucun montant d'indu ni solde budgétaire n'est présumé.",
        "Aucune charge nouvelle n'est identifiée : la source est maintenue sans nouveaux contrôles périodiques, justificatifs ou pénalités créés par cet article."
    ),
    'L482-1': (
        "Maintien intégral nécessaire de la prolongation des rentes d'orphelin dans les régimes historiques exclus des articles L434-7 et suivants. Apprentissage, études, infirmité et maladie chronique sont des critères protecteurs distincts ; le contrat unique n'impose aucune suppression de l'avantage de l'enfant en apprentissage, dont la phase de formation peut rester limitée au sein d'un emploi indéterminé.",
        "R482-1 lu en entier : dix-huit ans pour l'apprentissage et vingt ans pour études ou impossibilité permanente de travail salarié liée aux infirmités ou maladies chroniques. Aucun âge n'est changé dans la loi. Les dates du 9 avril 1898 et du 19 juillet 1911 identifient les régimes historiques, non l'entrée en vigueur d'une nouvelle réforme. Les nouvelles situations éligibles dans ce champ historique ne sont pas fermées. L434-7 lu confirme le régime distinct des pensions de décès ordinaires.",
        "Les prolongations d'âge demeurent pour tout enfant remplissant à l'avenir les conditions du régime historique, notamment une phase d'apprentissage dans le contrat unique. L'avantage n'est limité ni aux anciens CDD ni aux seuls droits déjà liquidés.",
        'retained_necessary',
        "Les prolongations favorables des rentes historiques sont intégralement maintenues. La durée d'une formation n'est pas transformée en terme du contrat et aucune réduction fictive de cotisation n'est comptée.",
        "Le dispositif reste limité aux accidents exclus de L434-7 et suivants et à ses conditions d'âge et de situation. L'organisation actuelle de chaque organisme payeur historique n'est pas certifiée par le lot.",
        "Aucune charge nouvelle n'est identifiée : aucun préavis, seuil d'ancienneté ou justificatif supplémentaire n'est ajouté à la rente d'orphelin maintenue."
    ),
    'L482-2': (
        "Maintien intégral nécessaire de la désignation des débiteurs des prestations historiques de L482-1. Supprimer cet article ne réduirait aucun prélèvement et risquerait de priver les bénéficiaires d'un fondement explicite de paiement. La règle distingue les fonds de majoration gérés par la Caisse des dépôts des organismes d'assurance accidents d'Alsace-Moselle.",
        "Renvoi conservé à L482-1, qui garde les prolongations d'âge ; il ne vise ni un contrat de travail à terme ni une indemnité de rupture. La continuité organique actuelle des fonds historiques et d'éventuelles substitutions de payeur doivent être documentées hors de cette source ; aucune disparition du droit ou nouvelle désignation n'est déduite de cette incertitude.",
        "Les rentes d'orphelin et leurs prolongations continuent à être payables aux futurs bénéficiaires recevables dans le champ historique. Aucun organisme de substitution ou plafond nouveau n'est créé et l'avantage d'apprentissage n'est pas réservé aux anciens contrats.",
        'retained_necessary',
        "Le circuit légal de paiement des prestations de L482-1 reste intégral. Aucune fusion de régime, suppression de taxe ou économie budgétaire n'est démontrée par ce maintien.",
        "La continuité des dénominations et successions institutionnelles des payeurs n'est pas établie par les seules sources locales ; elle n'est pas affirmée comme une coordination achevée.",
        "Aucune charge nouvelle n'est identifiée : les bénéficiaires ne reçoivent aucune déclaration, attestation ou nouvelle condition de paiement dans l'article maintenu."
    ),
    'L482-3': (
        "Maintien intégral nécessaire de l'habilitation à fixer par arrêté interministériel les conditions d'application des deux articles qui préservent les rentes historiques. Cette disposition ne crée pas elle-même une déclaration, un taux ou une autorisation supplémentaire. Son retrait sans reprise des conditions d'exécution compromettrait l'effectivité d'avantages conservés.",
        "Les deux renvois restent cohérents avec L482-1 et L482-2 maintenus, notamment apprentissage, études, incapacité et organismes payeurs. Aucun arrêté non fourni n'est déclaré lu ni réécrit. Le pouvoir réglementaire ne peut être confondu avec une habilitation à rétablir des CDD.",
        "L'exécution des prolongations favorables de rentes garde son fondement pour les nouvelles situations qui relèvent de ces régimes historiques. Aucun âge, droit de paiement ou faculté d'apprentissage n'est réduit par le maintien.",
        'retained_necessary',
        "Le support d'application des rentes protégées reste inchangé ; l'article ne contient pas de charge directement supprimable démontrée. Aucun allègement n'est attribué au maintien.",
        "Les conditions détaillées des arrêtés d'application et les successions des organismes restent extérieures au lot ; leur examen exhaustif n'est pas revendiqué.",
        "Aucune charge nouvelle n'est identifiée : les mêmes deux articles restent visés et aucun contenu supplémentaire n'est imposé à leur réglementation."
    ),
    'L482-4': (
        "Maintien intégral nécessaire des nullités protégeant les droits AT-MP contre les conventions contraires au livre IV et contre la rémunération anticipée d'intermédiaires pour obtenir les prestations légales. La disposition protège le patrimoine de la victime et l'effectivité du recours ; la supprimer ne constitue pas un allègement justifié d'une formalité administrative.",
        "Les deux alinéas sont conservés, avec les émoluments convenus à l'avance et les victimes ou ayants droit. L471-2 sanctionne le service d'intermédiaire au 1°, non une rupture de travail. L'existence du contrat unique ne permet pas d'écarter ces droits sociaux d'ordre public ni de les confondre avec l'indemnité ordinaire de licenciement.",
        "La nullité des conventions de captation et des renonciations contraires au livre demeure pour les nouvelles victimes comme pour les ayants droit futurs. Aucun bénéfice de prestation ni possibilité de réparation n'est réduit au nom de la simplification.",
        'retained_necessary',
        "Les protections contractuelles restent entières ; aucune nouvelle nullité ou formalité n'est créée. Le maintien n'est pas une réduction de prélèvement ou de délai.",
        "La règle ne réforme pas l'ensemble de l'assistance juridique ou des honoraires fondés sur d'autres textes. Aucun double emploi exact permettant son retrait sans perte de protection n'est démontré.",
        "Aucune charge nouvelle n'est identifiée : les mêmes conventions demeurent nulles et aucun registre, visa ou condition d'ancienneté supplémentaire n'est institué."
    ),
    'L482-5': (
        "Maintien intégral nécessaire de la règle générale d'exécution du livre IV et du décret en Conseil d'Etat à défaut de disposition contraire. Ce cadre permet de rendre effectifs reconnaissance, indemnisation et recours ; il ne constitue pas par lui-même une autorisation demandée aux victimes ou aux employeurs. Aucun doublon opératoire dispensable n'est établi.",
        "La réserve des dispositions contraires et le caractère limité aux modalités d'application restent intacts. Les règlements ne peuvent contredire les suppressions législatives proposées dans ce lot. Le maintien de cette habilitation ne vaut pas validation ni maintien de toute formalité réglementaire existante.",
        "Les modalités nécessaires aux prestations AT-MP, dont les avantages et dispenses conservés, gardent leur base d'exécution. Aucune prestation future éligible n'est fermée et aucun agrément individuel n'est créé par le maintien de cet article.",
        'retained_necessary',
        "Le cadre réglementaire d'application est conservé à droit constant. Aucune suppression d'obligation privée ou de cotisation ne peut être déduite de cette habilitation générale.",
        "Chaque règlement conserve un examen propre et doit respecter les réformes législatives ; aucun inventaire complet de ses charges n'est prétendu effectué par cet article.",
        "Aucune charge nouvelle n'est identifiée : ni champ, ni compétence, ni procédure individuelle ne sont ajoutés à la source intégralement maintenue."
    ),
    'L491-1': (
        "Maintien intégral nécessaire du droit à réparation des victimes des pesticides, de tous ses bénéficiaires obligatoires et solidaires, du complément des non-salariés et de l'indemnité corporelle des enfants exposés avant la naissance. La demande et l'imputabilité déterminent un droit individualisé ; la référence aux autorisations de mise sur le marché définit les produits couverts et n'est pas un agrément imposé à la victime. Aucune charge dispensable interne n'est démontrée sans altérer la protection.",
        "Lecture des quatorze alinéas : le complément est au douzième, comme le dit correctement le 2° a ; le onzième définit les pesticides. L491-2 doit donc remplacer son renvoi devenu faux. Sont préservés les anciens exploitants, conjoints et membres de famille ayant cessé avant le 1er avril 2002, la rédaction antérieure à la loi du 28 février 2025 pour les pensions citées, les trois règlements européens, les ayants droit des enfants et l'action juridictionnelle malgré le forfait. La note d'entrée en vigueur au 1er janvier 2026 reste historique ; elle n'est pas la date d'une réforme future. L723-13-3 et les régimes ruraux restent hors des cinq codes et ne sont pas présentés comme réécrits.",
        "Tous les avantages indemnitaires sont conservés : régimes obligatoires, complément solidaire des non-salariés, couverture des anciens exploitants et familles dans leur champ historique, dommages corporels des enfants et ayants droit, recours de droit commun. Les demandes futures recevables restent possibles, sans clôture liée au contrat unique.",
        'retained_necessary',
        "La totalité du champ personnel, de la définition des pesticides et des droits à réparation est conservée. Aucun impôt, contribution ou déclaration n'est supprimé par ce maintien.",
        "Le champ historique des anciens exploitants et les conditions de causalité subsistent. Le financement et la réglementation du fonds hors corpus ne sont ni refondus ni chiffrés ici.",
        "Aucune charge nouvelle n'est identifiée : la demande initiale et les conditions médicales restent les mêmes, sans registre, justificatif ou ancienneté de travail supplémentaire."
    ),
    'L491-2': (
        "Coordination nécessaire de fondement : le renvoi au complément d'indemnisation passe du onzième au douzième alinéa de L491-1. Le onzième alinéa en vigueur définit les pesticides ; le douzième contient effectivement le complément et ses modalités. Les trois alinéas et toutes les compétences du fonds et des caisses sont conservés, sans reformulation de remplissage ni nouvel allègement revendiqué.",
        "L491-1 fourni en entier et sa numérotation ont été confrontés : le 2° a renvoie déjà au douzième alinéa. La correction est immédiate pour les liquidations à opérer, sans modification d'assiette, de catégorie de bénéficiaires ou de créance acquise. La centralisation au fonds évite déjà plusieurs instructions de reconnaissance ; elle n'est pas comptée comme une fusion nouvelle. Le fonds de L723-13-3 du code rural et les caisses agricoles restent à leur régime propre.",
        "La correction rétablit un renvoi exact au complément des personnes visées aux a et b du 2°, sans fermer les demandes futures et sans modifier les règles du régime général, des salariés agricoles, des non-salariés ou du régime local. Elle ne crée pas une nouvelle condition d'accès.",
        'coordination_only',
        "Seul le renvoi erroné au complément est rectifié, du onzième au douzième alinéa. Le montant des droits, l'instruction et la liquidation restent identiques ; aucune seconde réduction n'est comptée.",
        "Le lot corrige une incohérence de renvoi préexistante ; il ne fusionne pas les régimes et ne retire aucune étape d'instruction distincte. Aucun effet budgétaire n'est évalué.",
        "Aucune charge nouvelle n'est identifiée : la rectification du numéro d'alinéa ne change ni les informations demandées ni le nombre de demandes ou de décisions."
    ),
    'L491-3': (
        "Maintien intégral nécessaire de la réparation des enfants exposés avant leur naissance : éléments d'exposition et de santé, investigations utiles, offre détaillée dans les six mois, provision avant consolidation et nouvelle offre en cas d'aggravation. Les éléments médicaux sont indispensables à l'imputabilité et au montant du dommage ; aucun justificatif exactement redondant n'est imposé par la source. La faculté d'investigation protège l'accès effectif à une preuve souvent détenue par des tiers.",
        "L491-1 2° c couvre l'exposition prénatale du fait professionnel de l'un ou l'autre parent, ainsi que les ayants droit. Les six mois sont un délai maximal d'offre à compter de la réception, non une durée d'emploi ou un préavis. Le droit existant de réemploi des données ne crée pas ici de nouvelle dispense ; aucune obligation de fournir à nouveau des pièces n'est ajoutée. Les levées de secrets restent limitées aux investigations utiles et les règles de confidentialité de L491-4 subsistent.",
        "L'offre provisionnelle sans consolidation, la nouvelle offre en cas d'aggravation et l'évaluation de chaque prestation demeurent pour tous les enfants et ayants droit futurs éligibles. Ni l'exposition parentale ni la réparation ne sont limitées aux anciens CDD.",
        'retained_necessary',
        "Les garanties d'offre, de provision et d'aggravation sont intégralement conservées. La charge de preuve utile n'est pas déclarée supprimée et aucune réduction de délai n'est inventée.",
        "Le délai maximal de six mois et l'évaluation causale demeurent ; aucune mesure du coût d'expertise ou réforme du règlement du fonds n'est fournie dans ce lot.",
        "Aucune charge nouvelle n'est identifiée : le maintien n'ajoute ni pièce systématique, ni exigence d'ancienneté, ni notification supplémentaire aux enfants ou à leur représentant."
    ),
    'L491-4': (
        "Réforme de fond : suppression de la notification personnelle supplémentaire au juge ou à la commission de la saisine du fonds. Le demandeur conserve l'information du fonds sur ses autres procédures ; le fonds assure le relais judiciaire. Le pouvoir d'obtenir les renseignements utiles, leur finalité limitée, les secrets et l'accès au dossier sont intégralement maintenus. Il s'agit d'un transfert explicite de démarche vers le fonds, non d'une économie nette présumée.",
        "Les quatre alinéas sources gardent leur place et une transition est ajoutée en cinquième position. La notification par le fonds porte sur sa saisine, comme auparavant celle du demandeur ; elle ne constitue pas une autorisation générale de divulguer les renseignements protégés par le troisième alinéa. Les actes de mise en cause imposés par d'autres règles procédurales, notamment pour les recours subrogatoires, ne sont pas supprimés par cette seule dispense. L1111-7 du code de la santé publique reste un renvoi préexistant d'accès au dossier, non un renvoi au droit de la rupture ; son contenu hors corpus n'est pas inventé. Le remplacement du déclarant au juge dépasse une simple reprise du réemploi administratif CRPA.",
        "Le droit d'obtenir le dossier, le respect des secrets et la finalité d'instruction demeurent pour les futures demandes comme pour les dossiers en cours. La notification au juge est conservée via le fonds afin de coordonner les réparations sans imposer une démarche de remplacement à la victime.",
        'mixed',
        "Une notification judiciaire à la charge du demandeur est retirée et confiée au fonds, à information de fond inchangée. L'allègement privé est démontré ; le coût public du relais et le solde net ne sont pas établis.",
        "L'information du fonds sur les autres procédures reste due ; les mises en cause fondées sur d'autres textes demeurent. Cette mesure ne supprime pas les règles empêchant la double indemnisation.",
        "Une obligation de notification au juge ou à la commission est ajoutée au fonds à la place du demandeur. Aucun nouveau dossier, registre, attestation ou dépôt de remplacement n'est imposé à celui-ci ; coût administratif non chiffré."
    ),
    'L491-5': (
        "Maintien intégral nécessaire des voies de recours : droit commun du régime pour les victimes professionnelles, action directe devant la cour d'appel du domicile pour les enfants après rejet, défaut d'offre dans le délai ou refus de l'offre. Ce dernier cas permet le recours sans exiger d'accepter l'offre ; les six mois encadrent l'instruction médicale et ne constituent pas une attente minimale lorsque le fonds s'est déjà prononcé.",
        "Le renvoi au dernier alinéa de L491-3 reste cohérent : cet article conserve ses trois alinéas, le dernier comprenant le délai de six mois, la provision et l'aggravation. Les règles de prescription de L491-7 demeurent distinctes. La compétence favorable de la cour du domicile et les adaptations par décret en Conseil d'Etat sont maintenues ; aucun nouveau recours préalable ni notification n'est ajouté.",
        "Les victimes conservent l'accès au juge et les enfants la cour d'appel de leur domicile dans les trois cas alternatifs, y compris le refus d'une offre. Ces voies sont ouvertes aux futurs bénéficiaires éligibles sans lien avec l'ancienneté d'un contrat de travail.",
        'retained_necessary',
        "Les voies judiciaires et leurs trois cas alternatifs restent intacts ; aucun délai nouveau ou plus court n'est créé. Le maintien préserve le recours sans fabriquer un allègement.",
        "L'instruction du fonds demeure préalable à l'action spéciale contre lui ; sa suppression immédiate n'est pas retenue au détriment de l'expertise et de l'offre provisionnelle. Aucun gain de coût n'est établi.",
        "Aucune charge nouvelle n'est identifiée : les mêmes conditions alternatives et la même juridiction restent applicables, sans préalable ou pièce supplémentaire."
    ),
    'L491-6': (
        "Maintien intégral nécessaire de la subrogation limitée aux sommes versées et aux indemnités effectivement à la charge des responsables, des interventions juridictionnelles du fonds et de la faculté de statuer au civil sans attendre le pénal. Le dispositif préserve la réparation de la victime tout en évitant un financement public définitif à la place du responsable ; ce n'est pas une cotisation à supprimer.",
        "L376-1 et L454-1 fournis ont été lus en entier, sources et propositions. Le renvoi vise les voies de recours, non un prélèvement autonome : leurs suppressions proposées d'indemnités forfaitaires de gestion restent opérantes dans leur propre champ et ne sont pas recréées par L491-6. La subrogation reste limitée aux paiements et aux plafonds de dette ; les préjudices personnels et droits préférentiels prévus dans les cibles gardent leur régime. Les interventions civiles, pénales, administratives et pour la première fois en appel sont maintenues ; aucun dépôt périodique ou autorisation supplémentaire n'est imposé.",
        "Les droits résiduels du demandeur et la limitation de la subrogation sont préservés pour les nouvelles indemnisations. La faculté pour le juge civil de ne pas attendre la décision pénale reste favorable. Aucune indemnité spéciale n'est assimilée à l'indemnité ordinaire patronale.",
        'retained_necessary',
        "La subrogation et les voies d'intervention sont conservées avec leurs limites. Les suppressions envisagées dans les articles cibles ne constituent pas une nouvelle réduction reproduite ici.",
        "Le lot ne supprime pas le remboursement par le responsable des prestations déjà versées ni les frais judiciaires autonomes. Aucune baisse de cotisations ou économie budgétaire nationale n'est démontrée.",
        "Aucune charge nouvelle n'est identifiée : les plafonds de subrogation, personnes responsables et facultés d'intervention restent ceux de la source entière, sans procédure additionnelle."
    ),
    'L491-7': (
        "Maintien intégral nécessaire de la prescription spéciale de dix ans courant de la consolidation du dommage des enfants. Le point de départ médical évite de faire courir ce délai avant la stabilisation du dommage prénatal ; raccourcir ou rapprocher ce point de départ retirerait une protection. Aucun doublon de déclaration ou prélèvement accessoire n'est contenu dans cet article.",
        "Le renvoi au c du 2° de L491-1 couvre les enfants exposés avant la naissance et leurs ayants droit dans le champ de cette disposition. La consolidation n'est ni la date de rupture du travail d'un parent ni une fin d'apprentissage. Le fonds reste celui de L723-13-3 du code rural ; la note historique de 2020 ne fixe pas une nouvelle date de réforme.",
        "Le délai de dix ans depuis la consolidation reste ouvert aux futurs enfants et ayants droit remplissant les conditions de L491-1, sans restriction aux seuls dommages déjà déclarés. Aucun raccourcissement de recours ni déchéance nouvelle n'est ajouté.",
        'retained_necessary',
        "Le délai protecteur et son point de départ restent inchangés ; aucune réduction de délai de procédure ou de prélèvement n'est revendiquée.",
        "Le texte ne change pas les règles générales de suspension, d'interruption ou de computation applicables. La durée d'exposition et la causalité gardent leur examen médical propre.",
        "Aucune charge nouvelle n'est identifiée : le maintien n'ajoute ni déclaration périodique, ni contrôle d'ancienneté, ni justification nouvelle avant la consolidation."
    ),
    'L511-1': (
        "Maintien intégral nécessaire de la liste des neuf prestations familiales. Retirer une rubrique ne simplifierait pas un doublon administratif : cela fragiliserait le fondement d'une aide aux familles. L'allocation forfaitaire en cas de décès d'un enfant est une prestation, sans rapport avec un impôt de succession à abolir.",
        "Les 1° à 9° sont conservés avec le renvoi de l'allocation de logement au livre VIII du CCH. Les réformes SRU de quotas et carence ne suppriment pas cette aide au logement. La note de la loi du 8 juin 2020 réserve son entrée en vigueur et l'allocation transitoire ; elle n'est pas convertie en calendrier d'une réforme future. Aucun montant ou critère de prestation n'est inventé.",
        "PAJE, allocations familiales, complément familial, logement, éducation de l'enfant handicapé, soutien familial, rentrée scolaire, décès d'un enfant et présence parentale restent tous conservés pour les futurs bénéficiaires recevables selon leurs conditions propres.",
        'retained_necessary',
        "Les neuf fondements de prestations restent intégralement applicables ; le maintien ne supprime aucune taxe ou formalité et ne fusionne pas leurs conditions d'attribution.",
        "Les montants, assiettes de ressources et procédures des prestations relèvent de leurs textes propres, non modifiés par cette liste. Aucun solde de dépenses sociales n'est calculé.",
        "Aucune charge nouvelle n'est identifiée : aucune rubrique, condition, déclaration ou nouvelle pièce n'est ajoutée à la liste légale maintenue."
    ),
    'L512-1': (
        "Maintien intégral nécessaire du droit aux prestations familiales des résidents français ou étrangers ayant un enfant à charge résident, de la coordination avec les prestations personnelles de l'enfant et de l'exception des personnes détachées exemptées d'affiliation française. Les conditions déterminent le régime débiteur et préviennent les doubles attributions ; leur suppression ne se réduit pas à l'élimination d'une formalité redondante.",
        "L111-2-3 a été lu, source et proposition de réemploi : stabilité et régularité du séjour demeurent, sans demander ici de nouveaux justificatifs. Les règlements européens et conventions internationales restent réservés, avec leur stipulation particulière, et ne sont pas abolis nationalement. Aucun régime d'agent public, d'apprentissage ou de rupture du contrat privé ne peut être déduit de l'exception de détachement. L'interdiction de cumul vise les prestations personnelles énumérées, non toute ressource de l'enfant.",
        "Le droit des résidents étrangers comme français et la réserve favorable de stipulation particulière pour les personnes détachées restent préservés. Les nouvelles familles recevables conservent leur accès ; aucune exonération d'affiliation issue d'un accord ou règlement n'est supprimée.",
        'retained_necessary',
        "Le champ des bénéficiaires et la coordination internationale restent inchangés. Aucune baisse de prélèvement ni nouvelle dispense de justificatif n'est comptée à partir d'une reprise des droits de réemploi déjà existants.",
        "La résidence, la charge d'enfant, les non-cumuls ciblés et l'exemption de détachement subsistent. L'ensemble des règlements et conventions n'est pas déclaré réécrit ou audité ici.",
        "Aucune charge nouvelle n'est identifiée : le maintien ne demande ni nouvelle attestation de résidence ni déclaration de détachement supplémentaire, et n'élargit pas les non-cumuls."
    ),
}


def effect(number, kind, measure, description, before, after, unit, population,
           transition, replacement, source_quote, proposed_quote):
    assert source_quote in plain(by_number[number]['source_xml']), (number, source_quote)
    assert proposed_quote in plain(proposals[number]), (number, proposed_quote)
    assert len(source_quote) >= 12 and len(proposed_quote) >= 12
    return dict(kind=kind, measure_id=measure, description=description,
                before=before, after=after, unit=unit,
                affected_population=population, conditions_and_transition=transition,
                replacement_or_new_burdens=replacement,
                source_quote=source_quote, proposed_quote=proposed_quote)


effects = {n: [] for n in by_number}
measure = 'maladies-professionnelles-declaration-procedes-unique'
effects['L461-4'] = [
    effect('L461-4', 'obligation_merged', measure,
           "Dépôt unique de la déclaration des procédés de travail dangereux, sans envoi privé parallèle à l'inspection.",
           "L'employeur déclare les mêmes procédés à la caisse primaire et à l'inspection du travail ; R461-4 impose en outre deux exemplaires à la caisse.",
           "Une déclaration et un exemplaire sont remis par l'employeur à la caisse, qui relaie l'information à l'inspection ; aucun taux ni assiette de cotisation n'est modifié.",
           'legal_duty', "Employeurs utilisant les procédés susceptibles de provoquer les maladies de L461-2.",
           "Formalités à accomplir dès l'entrée en vigueur, y compris pour des travaux antérieurs ; aucun redépôt des déclarations déjà reçues.",
           "Transmission à l'inspection par la caisse ; circuit de prévention vers la CARSAT conservé, coût public non chiffré.",
           "d'en faire la déclaration à la caisse primaire d'assurance maladie et à l'inspecteur du travail",
           "d'en faire une déclaration unique à la caisse primaire d'assurance maladie."),
    effect('L461-4', 'obligation_added', measure,
           "Le relais vers l'inspection incombe expressément à la caisse au lieu du déclarant.",
           "La source impose l'information de l'inspection directement à l'employeur, sans ce relais obligatoire de la caisse.",
           "La caisse transmet la déclaration reçue à l'inspecteur compétent ; aucune nouvelle donnée de fond n'est demandée.",
           'legal_duty', "Caisses primaires destinataires des déclarations de procédés dangereux.",
           "Dès l'entrée en vigueur, y compris les déclarations déjà reçues non encore parvenues à l'inspection.",
           "Charge administrative de transmission transférée ; pas de nouveau délai chiffré ou de dépôt privé de remplacement.",
           "d'en faire la déclaration à la caisse primaire d'assurance maladie et à l'inspecteur du travail",
           "La caisse transmet cette déclaration à l'inspecteur du travail ou au fonctionnaire qui en exerce les attributions en vertu d'une législation spéciale.")
]

measure = 'maladies-professionnelles-certificat-exemplaire-unique'
effects['L461-5'] = [
    effect('L461-5', 'obligation_removed', measure,
           "Suppression du certificat initial en triple et des deux exemplaires joints par la victime.",
           "Le praticien établit trois exemplaires du certificat initial ; la victime en joint deux à la déclaration.",
           "Un certificat initial et un seul exemplaire joint suffisent, avec contenu médical inchangé et transmissions nécessaires par la caisse.",
           'legal_duty', "Victimes demandant la réparation d'une maladie professionnelle et praticiens établissant le certificat initial.",
           "Formalités futures, y compris demandes en cours ; pièces déjà déposées conservées et aucun remplacement exigé.",
           "Copies nécessaires réalisées par la caisse, avec coût public de reproduction non établi.",
           "Le praticien établit en triple exemplaire et remet à la victime un certificat indiquant la nature de la maladie, notamment les manifestations mentionnées aux tableaux et constatées ainsi que les suites probables.",
           "Un seul exemplaire de ce certificat complète la déclaration mentionnée au premier alinéa."),
    effect('L461-5', 'obligation_added', measure,
           "Les copies nécessaires aux transmissions sont mises explicitement à la charge de la caisse.",
           "Deux exemplaires de certificat sont fournis par la victime pour le dossier et la transmission.",
           "La caisse produit les copies nécessaires à ses transmissions existantes à partir de l'exemplaire unique.",
           'legal_duty', "Caisses primaires instruisant les demandes de maladie professionnelle.",
           "Copies nécessaires pour les formalités à accomplir après l'entrée en vigueur, sans refaire les dossiers déjà déposés.",
           "Reproduction administrative explicitée ; les destinataires de la transmission et le contenu médical ne sont pas étendus.",
           "Deux exemplaires du certificat doivent compléter la déclaration mentionnée au premier alinéa dont la forme a été déterminée par arrêté ministériel.",
           "La caisse réalise les copies nécessaires aux transmissions qui lui incombent"),
    effect('L461-5', 'obligation_merged', 'maladies-professionnelles-demande-expresse-declaration-unique',
           "La demande expresse de réparation jointe à l'avis d'arrêt vaut la déclaration professionnelle, sans acte à refaire.",
           "Déclaration professionnelle imposée même si la maladie a été portée à la connaissance de la caisse au titre de L321-2.",
           "Si la victime a expressément demandé réparation avec l'avis L321-2, cet acte vaut déclaration à réception ; les informations réellement manquantes restent dues.",
           'legal_duty', "Victimes ayant expressément demandé réparation AT-MP avec leur avis d'arrêt de travail.",
           "Formalités futures et demandes en cours ; pas de conversion du seul avis d'arrêt ni réouverture des délais expirés.",
           "Aucune seconde déclaration, confirmation ou formulaire de remplacement ; les conditions médicales et délais demeurent.",
           "même si elle a déjà été portée à la connaissance de la caisse en application de l'article L. 321-2.",
           "Aucune seconde déclaration de la même demande n'est exigée ; les seules informations nécessaires qui manquent à son instruction restent à fournir."),
    effect('L461-5', 'compliance_cost_reduced', 'maladies-professionnelles-formulaire-facultatif',
           "Le formulaire ministériel n'est plus le support exclusif de la déclaration.",
           "La déclaration est de forme déterminée par arrêté ministériel.",
           "Le formulaire reste disponible ; un autre support est recevable s'il contient les mêmes informations nécessaires, sans formulaire à recopier.",
           'legal_duty', "Victimes ou leurs représentants déposant une déclaration de maladie professionnelle.",
           "Déclarations à accomplir après l'entrée en vigueur, y compris demandes en cours, sans remplacement des pièces reçues.",
           "Aucune donnée nouvelle : contenu utile inchangé et support libre en alternative, non dépôt additionnel.",
           "la déclaration mentionnée au premier alinéa dont la forme a été déterminée par arrêté ministériel.",
           "Cette déclaration peut être faite au moyen du formulaire déterminé par arrêté ministériel ou sur un autre support comportant les mêmes informations nécessaires à l'instruction de la demande.")
]

effects['L471-1'] = [effect(
    'L471-1', 'obligation_removed', 'atmp-recouvrement-integral-seul-manquement-formel-suppression',
    "Suppression du remboursement automatique de toutes les dépenses AT-MP fondé exclusivement sur un manquement formel.",
    "Pour défaut de déclaration, de registre ou de remise de feuille visé, la caisse recouvre la totalité des dépenses de l'accident auprès de l'employeur ou du préposé ; une pénalité peut s'y ajouter.",
    "Plus de recours pour la totalité des dépenses fondé sur le seul manquement ; la pénalité L114-17-1 et les recours du troisième alinéa demeurent, sans changement de taux ou d'assiette des cotisations.",
    'legal_duty', "Employeurs et préposés auxquels est imputé le seul manquement aux formalités L441-2, L441-4 ou L441-5.",
    "Dès l'entrée en vigueur, y compris recouvrements non définitivement tranchés ; créances définitives préservées, sans restitution générale et avec réserve répressive plus douce.",
    "Aucun prélèvement ni formalité de remplacement ; sanctions existantes, réparation de la victime et recours autonomes conservés.",
    "La caisse primaire d'assurance maladie recouvre auprès des employeurs ou de leurs préposés n'ayant pas satisfait à ces dispositions l'indu correspondant à la totalité des dépenses faites à l'occasion de l'accident",
    "Le seul manquement à ces formalités ne permet pas à la caisse primaire d'assurance maladie de recouvrer auprès de l'employeur ou de ses préposés la totalité des dépenses faites à l'occasion de l'accident.")]

effects['L481-1'] = [effect(
    'L481-1', 'authorization_removed', 'reeducation-professionnelle-autorisation-speciale-caisses-suppression',
    "Retrait de l'autorisation organique spéciale de création ou de participation à la gestion par les caisses.",
    "L'Etat autorise les projets des caisses de création d'établissements de rééducation ou de participation à leur gestion.",
    "Aucune autorisation ni déclaration de substitution sur ce fondement ; règles et autorisations sanitaires autonomes maintenues.",
    'legal_duty', "Caisses de sécurité sociale portant des projets de création d'établissements de rééducation professionnelle ou de participation à leur gestion.",
    "Abrogation dès l'entrée en vigueur ; demandes pendantes sans objet ; autorisations et engagements valables, droits et créances antérieurs préservés.",
    "Aucun remplacement de l'autorisation abrogée ; contrôles des soins, sécurité et fonds conservés sur leurs bases autonomes.",
    "Les projets de création d'établissements de rééducation professionnelle ou de participation à la gestion de tels établissements créés par des oeuvres ou institutions, établis par les caisses de sécurité sociale, sont soumis à l'autorisation de l'Etat.",
    "Aucune déclaration, demande d'agrément ou autorisation de remplacement ne peut être exigée sur ce seul fondement.")]

effects['L491-2'] = [effect(
    'L491-2', 'coordination', 'pesticides-complement-indemnisation-renvoi-exact',
    "Correction de l'alinéa désignant le complément de réparation, sans modifier son régime.",
    "L491-2 renvoie au onzième alinéa de L491-1, qui définit désormais les pesticides.",
    "Le renvoi vise le douzième alinéa, qui prévoit réellement le complément des non-salariés et des anciens exploitants éligibles.",
    'other', "Personnes des a et b du 2° de L491-1, fonds et caisses chargés de leur liquidation.",
    "Coordination du renvoi pour les liquidations à opérer, sans retrait des créances acquises ni condition nouvelle pour les demandes futures.",
    "Aucune procédure nouvelle ou réduction autonome ; seuls les mots du renvoi nécessaire changent.",
    "du complément d'indemnisation mentionné au onzième alinéa du même article L. 491-1.",
    "du complément d'indemnisation mentionné au douzième alinéa du même article L. 491-1.")]

measure = 'pesticides-notification-judiciaire-par-fonds'
effects['L491-4'] = [
    effect('L491-4', 'obligation_removed', measure,
           "Retrait de la notification personnelle au juge de la saisine du fonds, après information du fonds sur les autres procédures.",
           "Le demandeur informe le fonds des procédures et doit aussi informer le juge ou la commission de la saisine du fonds.",
           "Le demandeur garde l'information du fonds et n'effectue plus la seconde notification judiciaire ; le fonds la réalise.",
           'legal_duty', "Demandeurs d'indemnisation des pesticides ayant une action en justice relative aux mêmes préjudices.",
           "Notifications à accomplir dès l'entrée en vigueur, y compris dossiers et actions en cours ; celles déjà effectuées ne sont pas renouvelées.",
           "Relais administratif par le fonds ajouté ; aucune attestation ou dépôt de remplacement exigé du demandeur.",
           "Si une action en justice est intentée, il informe le juge ou la commission de la saisine du fonds.",
           "Le demandeur n'est pas tenu d'effectuer une seconde notification de la saisine du fonds au juge ou à la commission."),
    effect('L491-4', 'obligation_added', measure,
           "Le fonds prend en charge la notification judiciaire auparavant due par la victime.",
           "La victime doit notifier la saisine du fonds au juge ou à la commission.",
           "Le fonds informe le juge ou la commission de sa saisine à partir des informations reçues, dans le respect des secrets conservés.",
           'legal_duty', "Fonds d'indemnisation saisi de demandes pesticides faisant aussi l'objet d'une procédure juridictionnelle.",
           "Substitution dès l'entrée en vigueur ; aucune répétition des notifications déjà effectuées.",
           "Charge administrative de relais nouvellement obligatoire ; coûts et solde net non établis, sans nouvelle donnée exigée du demandeur.",
           "Si une action en justice est intentée, il informe le juge ou la commission de la saisine du fonds.",
           "Si une action en justice est intentée, le fonds informe le juge ou la commission de sa saisine à partir des informations qui lui ont été communiquées.")
]


# Required references: the three labour-law targets are examined in the actual context
# of each source. An out-of-scope target is explained rather than imported into social law.
contexts = {
    'L461-4': "La déclaration concerne des procédés dangereux et non la durée d'emploi des exposés ; les obligations de prévention restent applicables au contrat unique et aux contrats antérieurs.",
    'L461-5': "La demande concerne la reconnaissance et la réparation d'une maladie, éventuellement après la cessation du travail ; aucun délai de déclaration ne se transforme en préavis de rupture.",
    'L461-8': "Le changement d'emploi médicalement nécessaire et l'indemnité spéciale faute de rente sont distincts d'une indemnité ordinaire de licenciement ; l'avantage doit rester ouvert aux futurs salariés éligibles.",
    'L471-1': "Les manquements déclaratifs d'accident et le travail dissimulé sont des objets autonomes ; la réduction du recours en dépenses ne modifie ni la durée des contrats ni les indemnités de rupture.",
    'L471-2': "L'amende frappe les intermédiaires visés en L482-4 et les retenues salariales d'assurance accidents ; elle ne sanctionne pas une rupture de contrat ni un défaut de préavis.",
    'L482-1': "La phase d'apprentissage ouvre la prolongation d'une rente historique d'orphelin ; elle reste possible dans un emploi indéterminé et sa durée pédagogique ne termine pas l'emploi.",
    'L482-2': "La désignation des payeurs exécute la prolongation des rentes historiques de L482-1, y compris lorsque la phase d'apprentissage d'un futur bénéficiaire se déroule dans le contrat unique.",
    'L482-3': "L'arrêté applique les prolongations de rentes de L482-1 et leurs payeurs ; il ne peut transformer la durée pédagogique de l'apprentissage en terme d'un contrat nouveau.",
    'L482-4': "Les nullités protègent les prestations AT-MP des victimes et ayants droit ; elles ne portent ni sur une indemnité ordinaire de licenciement ni sur la durée de l'emploi.",
    'L491-1': "Le droit aux indemnités pesticides couvre des salariés, non-salariés, anciens exploitants et enfants exposés avant la naissance ; son fait générateur médical est autonome de la rupture d'emploi.",
    'L491-2': "Le fonds statue sur l'origine professionnelle, l'imputabilité et l'incapacité avant liquidation par les caisses ; le complément solidaire renvoie désormais au douzième alinéa de L491-1.",
    'L491-3': "L'offre aux enfants vise le dommage causé par l'exposition prénatale résultant du travail parental ; les six mois d'offre ne sont ni un terme d'emploi ni un préavis individuel.",
    'L491-4': "La notification au juge coordonne des procédures de réparation pesticides ; son transfert au fonds ne vaut pas notification de rupture d'un contrat de travail ni autorisation de rupture.",
    'L491-5': "Les recours contre le fonds suivent le régime social de l'adulte ou la voie spéciale de la cour d'appel pour les enfants ; leurs délais ne sont pas ceux d'une rupture individuelle d'emploi.",
    'L491-6': "La subrogation rembourse les indemnités pesticides effectivement versées et ouvre des interventions juridictionnelles ; elle ne recouvre pas une indemnité ordinaire de licenciement.",
    'L491-7': "La prescription de dix ans part de la consolidation du dommage de l'enfant, non de la cessation de l'emploi d'un parent ou de la date d'une notification patronale."
}

special_checks = {
    ('L461-4', 'L461-2'): "Le renvoi vise les tableaux et les maladies que les procédés peuvent provoquer : catégories présumées des trois premiers alinéas, révisions du quatrième et délais de prise en charge du cinquième. Le dépôt unique conserve ce champ, l'information de prévention et les futures expositions ; aucune ancienneté ou notification de rupture n'intervient. La note de 2018 n'est pas une date future de réforme.",
    ('L461-5', 'L461-2'): "Le deuxième alinéa vise précisément le quatrième de L461-2 : révision ou extension d'un tableau, bénéfice aux maladies constatées antérieurement sans effet pécuniaire avant l'entrée en vigueur et substitution aux autres avantages pour l'avenir. Le délai déclaratif plus long reste conservé. Les présomptions et limites médicales ne sont pas remplacées par une condition d'ancienneté d'emploi.",
    ('L461-5', 'L431-2'): "Le cinquième alinéa de L461-5 conserve le renvoi au délai de deux ans de L431-2, sous réserve expresse de L461-1 et de l'information médicale du lien possible. Les régimes de rechute, décès, prestataires, indu et interruption de la demande pour faute inexcusable de la cible ne sont pas modifiés. Le délai de quinze jours de déclaration R461-5 est distinct des deux ans de prescription et du préavis individuel.",
    ('L471-1', 'L114-17-1'): "La cible I 2° vise les employeurs et son II 9° couvre fausse déclaration d'accident, non-respect déclaratif, feuille d'accident et manœuvres privant les victimes de leurs droits. La proposition maintient cette pénalité et ses conditions, plafonds et garanties ; elle retire seulement le recours automatique de L471-1 pour toutes les dépenses au seul manquement. Les obligations déjà dispensées par L441-2/4 ne peuvent redevenir sanctionnables. Aucun seuil d'ancienneté de licenciement n'est importé.",
    ('L471-2', 'L482-4'): "Le 1° de L471-2 vise les services des intermédiaires décrits au second alinéa de L482-4 : obtention des prestations contre émoluments convenus à l'avance, obligations frappées de nullité. Ce champ et l'ordre public du premier alinéa restent entiers. Il n'existe aucun renvoi à l'ancienneté ou à une notification de rupture ; le contrat unique ne peut valider la captation de prestations.",
    ('L482-2', 'L482-1'): "Le renvoi désigne les seules prestations de prolongation d'âge des orphelins des régimes historiques exclus de L434-7 et suivants : apprentissage, études et incapacité permanente de travail par infirmité ou maladie chronique. La désignation des payeurs est conservée sans fermer ces droits futurs ; une phase d'apprentissage à durée limitée n'est pas un nouveau CDD ni une condition d'ancienneté professionnelle.",
    ('L482-3', 'L482-1'): "L'arrêté doit appliquer la prolongation d'âge de L482-1, non fixer la durée d'un emploi : apprentissage, études et impossibilité permanente de travail du régime historique restent couverts. R482-1 lu maintient dix-huit et vingt ans dans leurs cas propres. Ni l'indemnité ordinaire, ni son an d'ancienneté, ni une notification de rupture ne conditionnent ces rentes.",
    ('L491-2', 'L491-1'): "Le fonds instruit les personnes du 1° et des a et b du 2° ; les caisses liquident selon le régime avec le complément de ces deux dernières catégories. La source de L491-2 vise à tort le onzième alinéa : c'est la définition des pesticides ; le complément est au douzième, également visé par le 2° a de L491-1. Le renvoi est rectifié sans réduire le champ, notamment les futurs demandeurs relevant des cohortes antérieures au 1er avril 2002.",
    ('L491-3', 'L491-1'): "Le renvoi au c du 2° couvre les enfants dont la pathologie résulte directement de l'exposition prénatale du fait de l'exposition professionnelle de l'un ou l'autre parent, ainsi que leurs ayants droit. Ce n'est pas le champ des adultes des 1° et 2° a/b. Les conditions de causalité, la provision et l'aggravation restent intégrales, sans ancienneté de travail ni notification de rupture parentale exigée.",
    ('L491-4', 'L491-1'): "Les procédures à signaler concernent les préjudices définis par tout L491-1, adultes des régimes obligatoires ou de solidarité et enfants du 2° c avec ayants droit. Le transfert de notification au fonds ne ferme aucune catégorie future et n'altère ni complément ni indemnité corporelle. La déclaration des autres procédures demeure ; aucune durée d'emploi ou indemnité ordinaire n'entre dans le champ de ce renvoi.",
    ('L491-5', 'L491-1'): "Les voies se répartissent exactement entre personnes du 1° et des a/b du 2° soumises au contentieux de leur régime, et enfants du c du 2° admis devant la cour d'appel du domicile dans les cas prévus. Les futurs demandeurs recevables et ayants droit gardent les protections de L491-1. Aucune rupture d'emploi, ancienneté ou notification du contrat unique n'est une condition de recevabilité ici.",
    ('L491-6', 'L454-1'): "Le renvoi porte sur les voies de recours AT-MP contre un tiers, avec paiement préalable des prestations, limites de responsabilité et protections des préjudices personnels. La proposition cible supprime pour l'avenir l'indemnité forfaitaire de gestion et dispense l'information déjà reçue dans les limites prévues ; L491-6 ne recrée pas cette indemnité par son renvoi procédural. Les droits de la victime et la subrogation plafonnée sont maintenus, sans condition d'ancienneté d'emploi.",
    ('L491-6', 'L376-1'): "Le renvoi permet les voies subrogatoires hors AT-MP : recours poste par poste, préférence de la victime partiellement indemnisée et règles de mise en cause des caisses. La proposition cible supprime la nouvelle indemnité forfaitaire dans son propre champ et conserve les dettes anciennes ; le renvoi de L491-6 aux voies de recours ne rétablit aucun forfait. Ni ces prescriptions ni les deux ans de nullité du jugement ne se confondent avec un préavis de quinze jours.",
    ('L491-7', 'L491-1'): "Le c du 2° définit les enfants exposés avant la naissance du fait du travail de l'un ou l'autre parent et leurs ayants droit. Le droit à indemnisation visé par L491-7 garde dix ans à compter de la consolidation, pour les futurs dossiers recevables aussi. Cette prescription n'est ni un délai de rupture d'emploi parental ni un seuil d'ancienneté et elle ne ferme pas le complément distinct des adultes."
}


def reference_assessment(number, target):
    target_number = target['number']
    if target_number == 'L1234-1':
        return (contexts[number] + " La source de L1234-1 module le préavis patronal selon moins de six mois, six mois à moins de deux ans et au moins deux ans ; sa proposition fixe quinze jours calendaires pour les nouveaux contrats, sans ancienneté, et conserve l'ancien régime pour les contrats antérieurs. Aucun de ces seuils n'est un renvoi de " + number + " ; les procédures collectives et autorisations spéciales restent distinctes. Le point de départ de notification de L1234-3 n'est pas fourni comme cible et n'est pas modifié ici.")
    if target_number == 'L1221-2':
        return (contexts[number] + " La source autorise encore des contrats à terme dans les cas légaux ; la proposition impose l'emploi indéterminé aux nouvelles embauches sans fin automatique de mission ou formation. " + number + " ne rétablit aucun CDD et ne limite pas ses protections sociales aux anciens contrats. Les contrats antérieurs gardent leur transition ; les agents publics et les statuts agricoles non salariés ne sont pas convertis par ce renvoi de contexte.")
    if target_number == 'L1234-9':
        return (contexts[number] + " La cible officielle ouvre l'indemnité ordinaire après huit mois hors faute grave ; sa proposition exige pour le contrat unique un an à la fin effective, préavis inclus, puis 0,20 mois par année totale avec mois complets au prorata et plafond de six mois, employeur seul. Ces conditions ne sont pas importées dans " + number + ". Les parts acquises des anciens contrats et les indemnités spéciales restent distinctes, sans double compte ni soustraction de la première année après le seuil.")
    return special_checks[(number, target_number)]


answer = []
for source in sources:
    number = source['number']
    reason, notes, benefit, classification, assessment, limitations, burdens = analyses[number]
    rewritten = number in proposals
    result = {field: source[field] for field in ['code_id', 'source_id', 'source_sha256', 'number']}
    result.update(proposed_xml=proposals.get(number), reason=reason, review_notes=notes,
                  status='rewrite_draft' if rewritten else 'retained_unchanged')
    if not rewritten:
        result['classification'] = 'retained_necessary'
    result['benefit_review'] = benefit
    result['substantive_impact'] = dict(version=1, classification=classification,
        assessment=assessment, scope_limitations=limitations, new_burdens_review=burdens,
        effects=effects[number])
    result['reference_checks'] = []
    key = source['code_id'] + '|' + source['source_id']
    for target_key in references['requirements'][key]:
        target = references['targets'][target_key]
        result['reference_checks'].append(dict(target_key=target_key,
            view_sha256=target['view_sha256'], assessment=reference_assessment(number, target)))
    if number == 'L481-1':
        result.update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19',
            repeal_scope="Suppression pour l'avenir de l'autorisation spéciale de l'Etat des projets des caisses de sécurité sociale de création d'établissements de rééducation professionnelle ou de participation à leur gestion ; aucune demande ou déclaration de remplacement, demandes pendantes sans objet et garanties autonomes préservées.")
    if number in ['L461-4', 'L461-5', 'L471-1', 'L491-4']:
        result.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19')
        result['removed_provisions'] = {
            'L461-4': ["Envoi séparé par l'employeur de la déclaration des mêmes procédés à l'inspection du travail en plus de son dépôt à la caisse primaire.", "Pluralité d'exemplaires de la déclaration à remettre par l'employeur pour le circuit d'information prévu par L461-4."],
            'L461-5': ["Etablissement par le praticien du certificat médical initial en triple exemplaire et obligation pour la victime d'en joindre deux à la déclaration.", "Obligation de refaire une déclaration professionnelle lorsque la demande expresse de réparation a déjà accompagné l'avis L321-2 remis à la caisse.", "Exclusivité du formulaire ministériel pour la déclaration de maladie professionnelle, avec maintien des informations nécessaires sur un support alternatif."],
            'L471-1': ["Recouvrement automatique auprès de l'employeur ou de son préposé de la totalité des dépenses de l'accident pour le seul manquement aux formalités visées au premier alinéa."],
            'L491-4': ["Notification personnelle supplémentaire du demandeur au juge ou à la commission de la saisine du fonds d'indemnisation, remplacée par le relais du fonds."]
        }[number]
    answer.append(result)

Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'articles': len(answer), 'rewrites': sum(a['status'] == 'rewrite_draft' for a in answer),
                  'retained': sum(a['status'] == 'retained_unchanged' for a in answer),
                  'reference_checks': sum(len(a['reference_checks']) for a in answer)}, ensure_ascii=False))
