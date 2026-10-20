import json
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
by_number = {a['number']: a for a in sources}
answers = {}


def base(number):
    a = by_number[number]
    return {k: a[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}


def retain(number, reason, notes, assessment, limitations, burden_review, benefit=None):
    a = base(number)
    a.update(proposed_xml=None, reason=reason, review_notes=notes,
             status='retained_unchanged', classification='retained_necessary',
             substantive_impact={
                 'version': 1, 'classification': 'retained_necessary',
                 'assessment': assessment, 'scope_limitations': limitations,
                 'new_burdens_review': burden_review, 'effects': []})
    if benefit:
        a['benefit_review'] = benefit
    answers[number] = a


def effect(kind, measure_id, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit,
                affected_population=population, conditions_and_transition=transition,
                replacement_or_new_burdens=burdens, source_quote=source_quote,
                proposed_quote=proposed_quote)


def rewrite(number, xml, reason, notes, assessment, limitations, burdens,
            effects, removed=None, classification='material_reduction', benefit=None):
    a = base(number)
    a.update(proposed_xml=xml, reason=reason, review_notes=notes,
             status='rewrite_draft', substantive_impact={
                 'version': 1, 'classification': classification,
                 'assessment': assessment, 'scope_limitations': limitations,
                 'new_burdens_review': burdens, 'effects': effects})
    if removed:
        a.update(change_type='normative_reduction',
                 reform_policy_id='editorial_direction_2026_10_19',
                 removed_provisions=removed)
    if benefit:
        a['benefit_review'] = benefit
    answers[number] = a


retain('R132-2',
    "Maintien intégral après examen des deux transmissions. La proposition de périmètre des abords permet une élaboration conjointe avec le document d'urbanisme ; la notification du schéma social et médico-social assure la prise en compte des besoins d'équipement. Leur publication générale n'assure pas à elle seule cette information ciblée. Aucun rapport, agrément ni prélèvement autonome ne peut être retiré ici sans affaiblir cette coordination utile.",
    "Conserver le délai maximal de trois mois après publication du schéma et sa prise en compte à la plus prochaine révision, sans obligation de révision anticipée. Les renvois au code du patrimoine L621-30/L621-31 et au CASF L312-4 sont extérieurs aux cinq codes disponibles ; leur concordance n'est pas certifiée par ce lot. R132-1 et L132-2 ont été lus dans le corpus public.",
    "Aucune modification par rapport aux deux alinéas officiels : maintien de l'information patrimoniale et médico-sociale, sans revendiquer une simplification.",
    "Ne réforme ni les périmètres patrimoniaux ni les schémas médico-sociaux ; aucun coût administratif ou solde global des codes n'est chiffré.",
    "Aucune charge nouvelle identifiée : les mêmes destinataires, transmissions et échéances sont conservés intégralement.")

retain('R132-3',
    "Maintien intégral de l'information territorialisée donnée par le préfet en Ile-de-France. Le schéma directeur régional et ses éléments pertinents doivent être accessibles à l'auteur du SCOT ou, sans SCOT approuvé, à celui du PLU. Cette communication évite aux collectivités de reconstituer ces données ; elle ne crée ni demande de pièces privée ni nouvel agrément.",
    "R132-1 et L132-2 lus : la disposition précise territorialement le porter à connaissance général. Conserver les deux branches SCOT et PLU sans SCOT approuvé et leurs destinataires distincts. La coquille source « éléments mentionnées » ne justifie pas une réécriture stylistique.",
    "Aucune coupe démontrée : la transmission ciblée des éléments franciliens demeure utile pour préparer un document conforme au cadre régional.",
    "La compatibilité avec le schéma directeur régional et les modalités générales de transmission ne sont pas réformées par cet article.",
    "Aucune charge nouvelle identifiée : texte source intégralement conservé, sans attestation ni inventaire supplémentaire.")

xml = """<p>Les associations locales d'usagers mentionnées au 1° de l'article L. 132-12 et au 1° de l'article L. 132-13 peuvent être agréées dès lors qu'elles exercent des activités statutaires désintéressées en rapport avec l'urbanisme. L'agrément ne peut être demandé que pour le territoire de la commune où l'association a son siège social et des communes limitrophes.</p>
<p>Les présentes dispositions s'appliquent aux demandes déposées à compter de l'entrée en vigueur de la loi portant la présente réforme ainsi qu'aux demandes en cours d'instruction à cette date. Les agréments déjà régulièrement acquis demeurent valables.</p>"""
rewrite('R132-6', xml,
    "Réforme de fond : suppression de l'ancienneté minimale de trois ans et de l'exigence de fonctionnement continu préalable. Les associations nouvellement créées peuvent donc obtenir l'agrément. Maintien des activités statutaires désintéressées liées à l'urbanisme et du périmètre communal et limitrophe, qui caractérisent les associations locales concernées ; maintien de l'agrément prévu par les L132-12 et L132-13, avec procédure substantiellement allégée en R132-7.",
    "L132-12 et L132-13 lus intégralement : ils réservent cette consultation particulière aux associations agréées ; leur régime n'est pas abrogé implicitement. R132-7 est coordonné dans ce lot pour retirer le bilan triennal d'activité. R132-16 et R132-17 restent applicables aux associations agréées selon ces conditions simplifiées. Aucun agrément environnemental L141-1 n'est modifié. Application aux demandes en cours sans rouvrir les refus définitifs ni retirer les agréments acquis. Mise en œuvre réglementaire en Conseil d'Etat à coordonner avec la loi proposée.",
    "La source exige trois années de fonctionnement continu ; la proposition retire effectivement cette attente pour l'accès à l'agrément, sans créer une déclaration de remplacement.",
    "L'agrément et son périmètre géographique subsistent ; ni la procédure d'agrément environnemental ni les décisions antérieures définitives ne sont réformées. Aucun solde national de complexité n'est établi.",
    "Aucune charge nouvelle identifiée : seules les conditions d'ancienneté sont retirées ; les critères statutaires et territoriaux sont repris de la source et aucun justificatif nouveau n'est créé.",
    [effect('deadline_reduced', 'urbanisme-agrement-usagers-fin-anciennete',
            "Suppression de l'attente de trois ans de fonctionnement continu pour demander l'agrément local d'usagers.",
            "Associations locales : au moins trois ans de fonctionnement continu, outre les activités désintéressées d'urbanisme.",
            "Associations locales : aucune ancienneté minimale ni continuité préalable exigée ; activités désintéressées d'urbanisme et territoire inchangés.",
            'other', "Associations locales d'usagers relevant des L132-12 et L132-13.",
            "Demandes nouvelles et en cours à l'entrée en vigueur ; agréments acquis conservés.",
            "Aucune déclaration, pièce ou autorisation de remplacement ; l'agrément existant demeure avec la procédure allégée de R132-7.",
            "un fonctionnement continu depuis trois ans au moins",
            "peuvent être agréées dès lors qu'elles exercent des activités statutaires désintéressées en rapport avec l'urbanisme.")],
    ["Condition de fonctionnement continu pendant au moins trois ans avant l'accès à l'agrément des associations locales d'usagers."])

xml = """<p>La demande d'agrément comporte :</p>
<p>1° Une note de présentation de l'association retraçant ses activités en rapport avec l'urbanisme ;</p>
<p>2° Un exemplaire, à jour, des statuts ;</p>
<p>3° Abrogé.</p>
<p>L'agrément est délivré par arrêté préfectoral.</p>
<p>La décision d'agrément est publiée au Recueil des actes administratifs de l'Etat dans le département.</p>
<p>L'agrément est réputé accordé si l'association n'a pas reçu notification de la décision du préfet dans les deux mois qui suivent le dépôt de la demande comportant les pièces mentionnées aux 1° et 2°. Aucune autre pièce ne peut être exigée pour cet agrément. Dans ce cas, le préfet délivre, sur simple demande du président de l'association intéressée, une attestation constatant l'existence d'un agrément.</p>
<p>Les présentes dispositions s'appliquent aux demandes déposées à compter de l'entrée en vigueur de la loi portant la présente réforme. Pour les demandes en cours à cette date, le délai de deux mois est calculé depuis le dépôt des pièces mentionnées aux 1° et 2° ; lorsqu'il est déjà expiré, l'agrément tacite est acquis à cette date. Ces dispositions ne reportent aucune échéance antérieurement applicable et ne remettent en cause aucun agrément déjà acquis. Les pièces déjà remises ne sont pas demandées à nouveau.</p>"""
rewrite('R132-7', xml,
    "Réduction de fond du dossier et du circuit d'agrément : retrait du nombre d'adhérents cotisants, des rapports moral et financier, du tableau des ressources et charges et des informations sur les cotisations ; suppression des avis préalables des maires et de l'EPCI. La note d'activité et les statuts suffisent pour les conditions utiles de R132-6. Délai d'agrément tacite ramené de quatre à deux mois, sans nouveau départ fondé sur d'autres pièces. Coordination de la fin de l'ancienneté triennale en R132-6. L'arrêté, sa publicité et l'attestation facultative d'agrément tacite demeurent.",
    "L132-12/13 et R132-6 lus ; l'agrément légal subsiste, sans visa local de remplacement. Les mentions 1°, 2° et 3° sont conservées, le 3° étant abrogé. Les deux mois sont des mois, sans conversion fictive en soixante jours. Pour les demandes pendantes, le nouveau délai est calculé sur les seules pièces restantes ; aucun agrément n'est réputé né avant l'entrée en vigueur et aucune échéance plus favorable n'est retardée. Articuler le nouveau régime complet de pièces avec les règles générales du CRPA sans réintroduire les rapports supprimés. Les contrôles autonomes de fraude et recours gardent leur champ. Aucun agrément environnemental n'est touché.",
    "Le dossier triennal, les données financières et les avis locaux obligatoires disparaissent effectivement ; le délai de décision tacite est réduit. La suppression de la preuve triennale coordonne la même mesure que R132-6 et n'est pas une deuxième suppression du seuil.",
    "La note d'activité, les statuts, l'arrêté et sa publication restent requis. L'administration doit toujours examiner les critères légaux ; le coût net de ce traitement et les effets sur les consultations ne sont pas chiffrés.",
    "Aucune charge nouvelle identifiée : deux pièces déjà présentes restent seules exigibles, les avis sont retirés sans remplaçant et le délai se raccourcit. La publication et la délivrance facultative d'une attestation existaient déjà.",
    [effect('coordination', 'urbanisme-agrement-usagers-fin-anciennete',
            "Coordination documentaire de la suppression du seuil triennal en R132-6.",
            "La note d'activité doit retracer les trois années antérieures.",
            "La note retrace les activités d'urbanisme, sans période minimale de trois ans.",
            'other', "Associations locales demandant l'agrément, notamment nouvelles associations.",
            "Demandes nouvelles et pendantes ; les pièces remises ne sont pas exigées une seconde fois.",
            "Aucune nouvelle période de référence, attestation ou déclaration.",
            "retraçant ses principales activités au cours des trois années antérieures",
            "Une note de présentation de l'association retraçant ses activités en rapport avec l'urbanisme"),
     effect('obligation_removed', 'urbanisme-agrement-usagers-dossier-allege',
            "Retrait des données d'adhésion et du dossier financier, sans demande complémentaire équivalente.",
            "Nombre d'adhérents à jour, rapports moral et financier approuvés, tableau des ressources et charges, montants et produit des cotisations ; pièces complémentaires susceptibles de relancer le délai.",
            "Note d'activité et statuts à jour seulement ; aucun rapport moral ou financier, tableau, chiffre de cotisations ou pièce supplémentaire.",
            'legal_duty', "Associations locales d'usagers sollicitant l'agrément préfectoral.",
            "Demandes nouvelles et en cours à l'entrée en vigueur ; réutilisation des pièces déjà remises.",
            "Pas de déclaration ni d'attestation de remplacement ; note et statuts existaient dans le dossier source.",
            "3° Le rapport moral et le rapport financier approuvés lors de la dernière assemblée générale. Le rapport financier doit comprendre un tableau retraçant les ressources et les charges financières de l'association et indique expressément le ou les montants des cotisations demandées aux membres de l'association ainsi que le produit de ces cotisations.",
            "Aucune autre pièce ne peut être exigée pour cet agrément."),
     effect('obligation_removed', 'urbanisme-agrement-usagers-fin-avis-locaux',
            "Suppression du circuit obligatoire d'avis locaux avant agrément préfectoral.",
            "Avis du ou des maires et, s'il y a lieu, du président de l'EPCI ; silence favorable après deux mois.",
            "Arrêté préfectoral sans consultation locale obligatoire au titre de cet agrément.",
            'legal_duty', "Préfectures, maires, EPCI consultés et associations locales candidates.",
            "Demandes nouvelles et en cours ; les agréments antérieurs demeurent valables.",
            "Aucun autre avis, visa ou déclaration ne remplace les avis retirés.",
            "L'agrément est délivré par arrêté préfectoral après avis du maire ou des maires intéressés et, s'il y a lieu, du président de l'établissement public de coopération intercommunale compétent pour l'élaboration des schémas de cohérence territoriale et des plans locaux d'urbanisme.",
            "L'agrément est délivré par arrêté préfectoral."),
     effect('deadline_reduced', 'urbanisme-agrement-usagers-delai-deux-mois',
            "Réduction du délai de naissance de l'agrément tacite.",
            "Quatre mois après dépôt de la demande ou des pièces complémentaires demandées, en l'absence de notification d'une décision.",
            "Deux mois après dépôt de la note d'activité et des statuts, sans autre pièce exigible, en l'absence de notification d'une décision.",
            'other', "Associations locales demandant un agrément ; préfectures chargées de statuer.",
            "Demandes nouvelles ; pour les demandes en cours, calcul depuis les pièces restantes et effet au plus tôt à l'entrée en vigueur, sans retard d'une échéance acquise.",
            "Aucun nouveau dossier ou formulaire ; maintien de l'attestation facultative et du contrôle des conditions de fond.",
            "L'agrément est réputé accordé si l'association n'a pas reçu notification de la décision du préfet dans les quatre mois qui suivent le dépôt de la demande ou des pièces complémentaires demandées.",
            "L'agrément est réputé accordé si l'association n'a pas reçu notification de la décision du préfet dans les deux mois qui suivent le dépôt de la demande comportant les pièces mentionnées aux 1° et 2°.")],
    ["Indication obligatoire du nombre d'adhérents à jour de leur cotisation et pièces financières du 3°, comprenant rapports, tableau et données de cotisations.",
     "Consultation préalable obligatoire des maires et, le cas échéant, du président de l'EPCI avant délivrance de l'agrément.",
     "Attente de quatre mois et possibilité de recommencer ce délai sur la base de pièces complémentaires autres que les deux pièces restant exigibles.",
     "Présentation obligatoire des activités sur les trois années antérieures, coordonnée avec la suppression de l'ancienneté minimale de R132-6."])

xml = """<p>Lorsque, lors de l'élaboration, de la révision ou de la modification du plan local d'urbanisme, il y a lieu, en application des dispositions du code général des collectivités territoriales relatives aux communes nouvelles, de procéder à la consultation des conseils de communes déléguées, il est procédé à cette consultation dans les conditions prévues à l'article R. 134-1 pour les conseils d'arrondissement.</p>"""
rewrite('R132-8', xml,
    "Coordination du renvoi législatif : le numéro CGCT L2111-5 donné par la source n'a pas de concordance établie dans les pièces disponibles. Pour ne pas conserver un renvoi numéroté incertain ni en inventer un autre, le texte vise directement les dispositions du CGCT relatives aux communes nouvelles qui requièrent cette consultation. La condition législative de consultation et le régime commun de R134-1 restent identiques ; aucune suppression de consultation n'est revendiquée.",
    "Le défaut de concordance du numéro source est expressément signalé, non corrigé silencieusement par un numéro supposé. Le renvoi fonctionnel ne rend pas obligatoires les consultations que la loi n'exige pas. La concordance législative numérotée du CGCT reste à documenter hors des cinq codes. R134-1 est lu et réécrit dans le lot : quinze jours, avis tacite et information publique conservés ; son allègement d'annexion s'applique par renvoi, sans seconde réduction comptée ici.",
    "Coordination du renvoi aux règles des communes nouvelles ; le champ conditionnel de la consultation et son régime procédural restent ceux de la source.",
    "La concordance numérotée du CGCT n'est pas démontrée ; aucune modification des conditions législatives de consultation ni réduction supplémentaire de formalités n'est comptée.",
    "Aucune charge nouvelle identifiée : la consultation reste exigible seulement lorsqu'elle l'est par le CGCT ; aucun avis, délai, destinataire ou document supplémentaire n'est institué.",
    [effect('coordination', 'urbanisme-consultation-communes-deleguees',
            "Remplacement d'un renvoi numéroté non corroboré par la désignation fonctionnelle du même cadre législatif de consultation.",
            "Condition d'application renvoyant à CGCT L2111-5 pour la consultation des conseils de communes déléguées des communes nouvelles.",
            "Condition d'application renvoyant aux dispositions du CGCT relatives aux communes nouvelles qui imposent cette consultation ; régime R134-1 conservé.",
            'other', "Communes nouvelles et conseils de communes déléguées concernés par une consultation légale sur le PLU.",
            "Coordination du renvoi dès l'entrée en vigueur, sans nouvelle saisine ni reprise des consultations en cours.",
            "Aucune procédure ou pièce nouvelle ; aucune réduction autonome attribuée à ce renvoi.",
            "par application des dispositions de l'article L. 2111-5 du code général des collectivités territoriales",
            "en application des dispositions du code général des collectivités territoriales relatives aux communes nouvelles")],
    classification='coordination_only')

retain('R132-11',
    "Maintien intégral des règles de représentation des élus communaux à la commission. Le scrutin proportionnel assure leur pluralisme ; le vote par correspondance et surtout la nomination sans élection en cas de liste unique sont déjà des allègements à préserver. La désignation parisienne et la cessation en cas de perte de qualité organisent la représentativité, sans rapport ou autorisation économique supprimable.",
    "R132-10 et L132-14 lus : conserver la conformité de la liste unique à la composition de la commission, la plus forte moyenne, les titulaires et suppléants, les deux particularités du scrutin et de Paris. Aucun nouveau scrutin n'est créé ; la version source du 22 février 2026 sert de référence, sans confondre cette date avec celle de la réforme proposée.",
    "Aucune réduction nouvelle : la nomination sans scrutin sur liste unique et l'option du vote par correspondance restent entièrement applicables.",
    "Le coût des élections et la pratique préfectorale du vote par correspondance ne sont pas évalués ; la composition de R132-10 n'est pas modifiée.",
    "Aucune charge nouvelle identifiée : maintien exact des élections, dispenses et nominations existantes, sans nouveau formulaire.",
    "La nomination par arrêté en présence d'une liste unique conforme à R132-10 dispense déjà d'organiser une élection : elle est conservée pour tous les renouvellements futurs recevables. Le vote par correspondance reste possible et la désignation des élus par le conseil de Paris demeure. La fin du mandat en cas de perte de qualité n'est pas un avantage fiscal ou une dispense ; elle assure la représentativité de la commission. Aucun de ces aménagements favorables n'est limité aux situations antérieures.")

retain('R132-12',
    "Maintien de la nomination des personnalités qualifiées et de leurs suppléants pour le cycle municipal. Il faut pourvoir ces sièges pour rendre la conciliation opérationnelle et assurer la continuité des remplacements. Un acte unique de nomination à chaque renouvellement n'est pas un agrément imposé à une activité privée ; aucune déclaration ou renouvellement intermédiaire n'est exigé.",
    "R132-10 et L132-14 lus : l'effectif et les domaines de qualification restent ceux de la composition légale et réglementaire ; le terme du mandat demeure le renouvellement général suivant, sans mandat perpétuel ou révocation nouvelle.",
    "Aucune modification de fond : maintien de la constitution régulière de la moitié qualifiée de la commission et de sa suppléance.",
    "Ni le choix des personnalités ni les dépenses de fonctionnement de la commission ne sont évalués ; le texte ne réglemente pas une profession.",
    "Aucune charge nouvelle identifiée : maintien de la nomination préfectorale et du terme de mandat déjà prévus, sans pièce supplémentaire.")

retain('R132-13',
    "Maintien intégral du remplacement en cas de vacance : les mêmes modalités de désignation préservent l'équilibre entre élus et personnalités qualifiées et la durée limitée du mandat de remplacement. La disposition évite de renouveler la commission entière. Le titulaire et le suppléant sont nécessaires à son fonctionnement ; aucun dossier autonome redondant n'est institué ici.",
    "Lire avec R132-10 à R132-12 et R135-1 pour Mayotte. Ne pas assimiler une vacance à un renouvellement général ni prolonger le mandat au-delà du prochain renouvellement municipal. Le texte ne précise pas distinctement l'hypothèse de vacance du seul suppléant ; aucune interprétation créant une réélection systématique des deux personnes n'est ajoutée.",
    "Aucune suppression nouvelle démontrée : le remplacement limité à la durée restant à courir est conservé pour assurer la continuité de la conciliation.",
    "Le traitement des seules vacances de suppléants reste celui du droit applicable ; aucune extension du pouvoir préfectoral n'est créée dans ce lot.",
    "Aucune charge nouvelle identifiée : mêmes désignations et même terme de mandat, sans registre ni notification supplémentaires.")

xml = """<p>Dès que ses membres ont été désignés, la commission de conciliation est convoquée par le préfet et procède à l'élection d'un président et d'un vice-président choisis parmi les élus communaux.</p>
<p>La liste des membres de la commission est publiée au Recueil des actes administratifs de l'Etat dans le département à la diligence du préfet.</p>
<p>Le siège de la commission de conciliation est la préfecture du département.</p>
<p>Les présentes dispositions s'appliquent aux formalités de publication restant à accomplir à la date d'entrée en vigueur de la loi portant la présente réforme. Les publications déjà régulièrement effectuées ne sont pas renouvelées.</p>"""
rewrite('R132-14', xml,
    "Réforme de fond ciblée : suppression de l'insertion obligatoire de la liste des membres dans un journal départemental, doublon de sa publication au Recueil des actes administratifs. Maintien intégral de la convocation préfectorale, de l'élection du président et du vice-président parmi les élus communaux et du siège de la commission. Aucune publicité de remplacement.",
    "L132-14 et R132-10/11 lus : la commission et sa représentativité ne sont pas supprimées. La réduction porte sur la seconde publication, non sur l'accès du public à la composition. Elle vaut aussi pour une insertion encore à faire au jour de la réforme, sans restitution de frais déjà engagés ni republication imposée. Les annonces de saisine de R132-18 demeurent distinctes.",
    "La source impose Recueil et journal ; la proposition retire le journal tout en gardant la publication officielle de la composition. Réduction d'une formalité publique, sans montant d'économie présumé.",
    "Les coûts déjà contractés, les autres publicités de la conciliation et le financement de la presse ne sont pas évalués ; aucun gain national n'est extrapolé.",
    "Aucune charge nouvelle identifiée : aucune plateforme ni annonce nouvelle ; le Recueil et les règles de constitution restent ceux de la source.",
    [effect('obligation_removed', 'urbanisme-conciliation-fin-insertion-journal',
            "Suppression de la seconde publication obligatoire de la composition dans un journal départemental.",
            "Publication au Recueil des actes administratifs et insertion de la même liste dans un journal diffusé dans le département.",
            "Publication au seul Recueil au titre de R132-14 ; constitution et siège de la commission inchangés.",
            'legal_duty', "Préfectures chargées de publier la composition des commissions de conciliation.",
            "Formalités restant à accomplir à l'entrée en vigueur ; les publications accomplies ne sont pas répétées.",
            "Aucune annonce ou donnée de remplacement ; maintien de la publication officielle préexistante.",
            "La liste des membres de la commission est publiée au Recueil des actes administratifs de l'Etat dans le département à la diligence du préfet et insérée dans un journal diffusé dans le département.",
            "La liste des membres de la commission est publiée au Recueil des actes administratifs de l'Etat dans le département à la diligence du préfet.")],
    ["Insertion obligatoire dans un journal diffusé dans le département de la liste déjà publiée au Recueil des actes administratifs."])

retain('R132-15',
    "Maintien intégral du fonctionnement minimal de la commission : convocation par son président, règlement intérieur et secrétariat assuré par le service d'urbanisme de l'Etat. Aucune fréquence obligatoire, rapport périodique ou structure supplémentaire n'est exigé. Supprimer ces trois règles affaiblirait la continuité et l'impartialité de la conciliation sans retirer une démarche aux usagers.",
    "L132-14 et R132-14 lus : distinguer convocation constitutive par le préfet et réunions ultérieures par le président. Le règlement intérieur ne vaut pas habilitation à rétablir les pièces et publicités supprimées dans les autres articles du lot.",
    "Aucune réduction nouvelle : maintien du support de fonctionnement nécessaire à la commission légale, sans quota de réunions.",
    "La teneur des règlements intérieurs et les moyens humains du secrétariat ne sont pas disponibles ; leur coût net n'est pas présumé nul.",
    "Aucune charge nouvelle identifiée : aucune périodicité ni formalité supplémentaire n'est ajoutée au règlement intérieur existant.")

retain('R132-16',
    "Maintien intégral de l'accès à la conciliation pour les personnes publiques associées, les associations locales agréées et les associations environnementales agréées. Les deux stades du document, arrêté ou approuvé, et les trois catégories de saisissants sont utiles au règlement amiable. L'agrément des associations locales bénéficie des allègements de R132-6/7 ; le répéter sous un nouveau texte ne créerait aucune réduction supplémentaire.",
    "L132-14, L132-7/8/9 et L132-12/13 lus dans le corpus. Le renvoi aux conditions définies par décret en Conseil d'Etat reste cohérent avec les R132-6/7 réécrits ; aucun second agrément n'est exigé. L141-1 environnement reste autonome. R132-19 comporte une asymétrie préexistante de notification aux seules personnes publiques, expressément signalée dans ses notes.",
    "Les trois voies de saisine et les deux états du document sont conservés ; cet article ne compte pas une deuxième suppression de délai ou de pièces d'agrément.",
    "La conciliation ne remplace pas les recours juridictionnels ; aucun effet interruptif de délai ni droit nouveau d'une association non agréée n'est inventé.",
    "Aucune charge nouvelle identifiée : mêmes catégories de saisissants, sans dossier ni agrément supplémentaire de conciliation.")

retain('R132-17',
    "Maintien intégral de l'audition à leur demande des parties intéressées et des représentants des associations locales et environnementales agréées. C'est une garantie d'accès effectif à la conciliation et non une audition imposée à tous. Aucun formulaire, délai d'attente ou pièce spéciale ne figure dans le texte et ne peut être supprimé artificiellement.",
    "R132-16 et L132-14 lus. Les conditions de l'agrément local demeurent celles de R132-6/7, allégées dans le lot ; l'agrément environnemental L141-1 reste distinct. La rédaction n'institue ni délai de forclusion pour demander à être entendu ni représentation obligatoire par avocat.",
    "Aucune modification par rapport à la source : maintien du droit d'être entendu, y compris pour les associations agréées à l'avenir.",
    "La conduite matérielle des séances et les agréments environnementaux ne sont pas réformés ; aucun gain administratif supplémentaire n'est compté.",
    "Aucune charge nouvelle identifiée : le droit d'audition reste exercé sur demande, sans nouvelle pièce ou comparution obligatoire.")

retain('R132-18',
    "Maintien intégral de l'annonce de l'objet, de la date et du lieu de la première séance. L'affichage en préfecture et dans les communes ou à l'EPCI permet aux intéressés d'exercer leur droit de demander une audition, y compris sans accès numérique. Les lieux multiples correspondent à des publics territoriaux distincts ; le texte n'exige ni journal ni nouvelle pièce du saisissant.",
    "Lire avec R132-17 et R132-19. L'annonce de première séance est conservée même lorsque l'affichage intégral ultérieur des propositions est retiré dans R132-19 ; la mise à disposition matérielle de ces propositions et leur jonction au dossier public restent exigées. Aucun avis électronique exclusif n'est substitué.",
    "Aucune coupe nouvelle : les trois informations nécessaires à l'accès à la séance restent affichées dans les lieux de proximité prévus.",
    "Le coût de l'affichage et le nombre de communes concernées ne sont pas chiffrés ; cette publicité ne vaut pas convocation personnelle générale.",
    "Aucune charge nouvelle identifiée : les informations, les lieux d'affichage et le déclenchement par la saisine sont inchangés.")

xml = """<p>Les propositions de la commission, formulées dans le délai de deux mois à compter de sa saisine, sont notifiées, à la diligence de son président, à la personne publique chargée de l'élaboration du document d'urbanisme faisant l'objet de la procédure de conciliation, ainsi qu'à la personne publique qui a saisi la commission.</p>
<p>Elles sont tenues à la disposition du public à la préfecture, à la ou aux mairies ou au siège de l'établissement public chargé de l'élaboration du document et, dans ce cas, aux mairies des communes membres concernées.</p>
<p>Ces propositions sont également jointes au document d'urbanisme soumis à l'enquête publique ou à la procédure de participation du public par voie électronique.</p>
<p>Les présentes dispositions s'appliquent aux propositions formulées à compter de l'entrée en vigueur de la loi portant la présente réforme ainsi qu'aux formalités de publicité restant à accomplir à cette date. Les formalités déjà régulièrement accomplies ne sont pas renouvelées.</p>"""
rewrite('R132-19', xml,
    "Réduction de fond limitée à l'affichage du texte intégral des propositions, cumulatif avec leur mise à disposition dans les mêmes lieux et leur jonction au dossier de participation publique. Ces deux derniers accès restent complets ; l'annonce de la première séance demeure en R132-18. Le délai maximal de deux mois et les notifications prévues par la source sont intégralement maintenus. Aucun résumé ne remplace les propositions.",
    "La source notifie les propositions à la personne publique saisissante, alors que R132-16 permet aussi une saisine associative : asymétrie préexistante signalée, sans prétendre qu'une notification individuelle aux associations figure déjà dans le texte. L'accès public intégral et l'audition sur demande restent assurés ; aucune règle de recours n'est retirée. Les deux mois ne constituent pas une attente minimale. Conserver les deux voies d'enquête publique et de participation électronique ainsi que tous les lieux de consultation de la source. Une réforme distincte des destinataires individuels devrait être explicite ; elle n'est pas présentée comme accomplie ici.",
    "La seule obligation retirée est l'affichage intégral des propositions ; leur formulation sous deux mois, leurs notifications et leur consultation intégrale physique et dans le dossier public restent identiques.",
    "La visibilité spontanée procurée par l'affichage intégral cesse ; l'annonce préalable de séance et la consultation des propositions demeurent. Le coût net et l'asymétrie des notifications ne sont pas résolus par cette coupe.",
    "Aucune charge nouvelle identifiée : pas de registre, résumé affiché, portail ou notification de remplacement ; les deux canaux de consultation maintenus existaient dans la source.",
    [effect('obligation_removed', 'urbanisme-conciliation-fin-affichage-propositions',
            "Retrait de l'affichage intégral des propositions en plus de leur mise à disposition dans les mêmes lieux.",
            "Affichage et mise à disposition des propositions à la préfecture et aux lieux communaux ou intercommunaux prévus, plus jonction au dossier public.",
            "Mise à disposition intégrale dans tous ces lieux et jonction au dossier public ; pas d'affichage intégral imposé par R132-19.",
            'legal_duty', "Préfectures, communes et établissements publics chargés de la publicité des propositions de conciliation.",
            "Propositions nouvelles et formalités restant à accomplir à l'entrée en vigueur ; pas de répétition des formalités acquises.",
            "Aucune formalité nouvelle ; l'annonce de la première séance en R132-18, les notifications existantes et les accès publics sont conservés.",
            "Elles sont affichées et tenues à la disposition du public à la préfecture, à la ou aux mairies ou au siège de l'établissement public chargé de l'élaboration du document et, dans ce cas, aux mairies des communes membres concernées.",
            "Elles sont tenues à la disposition du public à la préfecture, à la ou aux mairies ou au siège de l'établissement public chargé de l'élaboration du document et, dans ce cas, aux mairies des communes membres concernées.")],
    ["Affichage intégral obligatoire des propositions de conciliation, en supplément de leur consultation complète dans les mêmes lieux et au dossier public."])

retain('R133-1',
    "Maintien intégral de l'habilitation ministérielle à préciser les modalités techniques des transmissions légales. L'article ne crée ni une déclaration supplémentaire ni une approbation du document transmis ; il permet la cohérence du point d'accès national. Abroger cette seule habilitation laisserait inchangées les obligations de L133-2/3 et désorganiserait leur exécution sans gain démontré.",
    "L133-1 à L133-5 lus intégralement. Les transmissions légales des documents et des servitudes restent distinctes de la transmission facultativement électronique de L133-5. Le contenu de l'arrêté d'application n'est pas joint ; son éventuel allègement n'est pas présenté comme réalisé.",
    "Aucune réduction nouvelle : maintien d'une base de modalités techniques, sans compter sa conservation comme une fusion des transmissions.",
    "Les prescriptions de l'arrêté extérieur et leur coût ne sont pas audités ici ; les obligations législatives restent dans leur champ propre.",
    "Aucune charge nouvelle identifiée : la compétence ministérielle existante est maintenue sans nouvelle donnée ni nouveau calendrier.")

retain('R133-2',
    "Maintien intégral des standards de numérisation et, à défaut de standard validé, du recours à un format de fichiers largement disponible. L'interopérabilité permet l'accès commun aux documents opposables sans ressaisie ; l'exception de format empêche un blocage en l'absence de standard. Le dispositif se rattache à la directive 2007/2/CE, qu'une coupe nationale ne peut effacer implicitement.",
    "L133-4 et L133-2/3 lus. Conserver les deux branches, le renvoi aux articles 18 et 19, paragraphe 2, de la directive du 14 mars 2007 et l'absence d'exigence de format propriétaire. Le corpus ne fournit ni les standards validés ni le texte européen complet : aucune conformité technique indépendante n'est certifiée.",
    "Aucune baisse d'obligation démontrée ; maintien de la standardisation nécessaire et de l'assouplissement en l'absence de standard validé.",
    "Les coûts de conversion, les standards actuels et les contraintes européennes détaillées ne sont pas évalués ; aucun gain national n'est annoncé.",
    "Aucune charge nouvelle identifiée : mêmes standards et même solution subsidiaire de fichiers largement disponibles ; aucun nouveau registre.")

retain('R133-3',
    "Maintien intégral des deux modes de transmission électronique facultative : plateforme conforme aux référentiels de sécurité et d'interopérabilité ou supports physiques électroniques. Il n'existe pas d'obligation exclusive de plateforme à supprimer. Les exigences de sécurité protègent l'intégrité et la réception des actes ; retirer la possibilité matérielle serait moins favorable aux collectivités.",
    "L133-5 lu : le choix initial de l'échange électronique demeure facultatif. Conserver la transmission de tout ou partie des actes et les deux référentiels de l'ordonnance 2005-1516 du 8 décembre 2005. Les modalités légales autonomes de transmission et cette ordonnance extérieure ne sont pas réécrites.",
    "Aucune réduction nouvelle : maintien d'une option électronique déjà ouverte, de son alternative matérielle et de ses garanties techniques.",
    "Le coût comparé des plateformes et supports, ainsi que le contenu actuel des référentiels extérieurs, ne sont pas établis dans le lot.",
    "Aucune charge nouvelle identifiée : pas de plateforme exclusive, d'abonnement, de copie papier ou d'échange électronique obligatoire ajouté.")

xml = """<p>Lors de l'élaboration, de la révision ou de la modification du plan local d'urbanisme de la Ville de Paris, le maire consulte le conseil d'arrondissement préalablement à toute délibération du conseil municipal.</p>
<p>La demande d'avis est accompagnée des documents au vu desquels le conseil municipal sera appelé à délibérer.<br />Le conseil d'arrondissement émet son avis dans le délai fixé par le maire de la commune. Ce délai ne peut être inférieur à quinze jours, à compter de la saisine du conseil d'arrondissement. Il est réputé favorable s'il n'intervient pas dans le délai prévu.</p>
<p>L'avis du conseil d'arrondissement ou à défaut le document justifiant qu'il a été saisi dans les délais nécessaires est joint au projet de délibération. Il est également joint au plan local d'urbanisme soumis à l'enquête publique, à la procédure de participation du public par voie électronique ou à une mise à disposition du public.</p>
<p>Les présentes dispositions s'appliquent aux délibérations adoptées à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris lorsque la consultation a été engagée avant cette date. Les saisines, avis et délibérations antérieurement régulièrement intervenus demeurent valables ; aucune consultation n'est recommencée du seul fait de la présente réforme.</p>"""
rewrite('R134-1', xml,
    "Réduction de fond documentaire : retrait de l'annexion supplémentaire de l'avis, ou de la preuve de saisine, à la délibération municipale définitive. La pièce reste jointe au projet soumis aux élus et au PLU soumis au public ; son contenu n'est pas supprimé. La consultation préalable à toute délibération, les documents de préparation, le minimum de quinze jours et l'avis tacite favorable sont conservés pour garantir une participation locale effective.",
    "R132-8 lu et coordonné : son renvoi applique le même régime aux consultations légales des communes déléguées, sans compter une seconde suppression. Le minimum de quinze jours est un délai de préparation d'un organe élu, distinct du préavis individuel de travail. Les trois modes de participation du public restent énumérés. La réforme ne dispense ni de consulter ni de conserver légalement les avis ; elle ne retire que leur annexion répétée à la délibération définitive. Le numéro CGCT non corroboré de R132-8 est remplacé par une référence fonctionnelle explicite, sans numéro de substitution inventé.",
    "Une destination documentaire obligatoire est supprimée, sans retrait de l'information préalable des élus ni de l'accès au dossier du public. Aucun raccourcissement du délai de préparation n'est revendiqué.",
    "Les effets sont limités à l'annexion prévue par cet article, y compris via R132-8 ; les obligations d'archives et de publicité autonomes subsistent. Aucun coût net global n'est établi.",
    "Aucune charge nouvelle identifiée : la consultation et ses deux transmissions documentaires restantes existaient déjà ; aucun registre, attestation nouvelle ou procédure de remplacement n'est créé.",
    [effect('obligation_removed', 'urbanisme-consultation-locale-fin-annexe-deliberation',
            "Retrait de la seconde annexion de l'avis ou de la preuve de saisine après la jonction au projet de délibération.",
            "Pièce jointe au projet de délibération, annexée à la délibération définitive et jointe au PLU soumis au public.",
            "Pièce jointe au projet de délibération et au PLU soumis au public ; aucune annexion supplémentaire à la délibération définitive exigée par R134-1.",
            'legal_duty', "Ville de Paris ; consultations de conseils de communes déléguées dans le champ du renvoi R132-8.",
            "Délibérations adoptées après l'entrée en vigueur, consultations en cours comprises ; aucune nouvelle saisine des conseils.",
            "Aucun document de remplacement ; quinze jours, dossier préparatoire, consentement par avis et accès du public maintenus dans leur régime source.",
            "L'avis du conseil d'arrondissement ou à défaut le document justifiant qu'il a été saisi dans les délais nécessaires est joint au projet de délibération et est annexé à la délibération du conseil municipal.",
            "L'avis du conseil d'arrondissement ou à défaut le document justifiant qu'il a été saisi dans les délais nécessaires est joint au projet de délibération.")],
    ["Annexion obligatoire à la délibération municipale définitive de l'avis ou de la preuve de saisine déjà joint au projet et au PLU soumis au public."])

retain('R135-1',
    "Maintien intégral de la composition adaptée de la commission de conciliation à Mayotte : trois élus de trois communes différentes et trois personnalités qualifiées. Cette parité assure une instance praticable localement ; abroger la dérogation pourrait rétablir le format général plus lourd de R132-10 et serait moins favorable. Aucune obligation déclarative ou publication supplémentaire n'est ajoutée.",
    "L132-14 et R132-10 lus : conserver le régime spécial de Mayotte, les deux effectifs de trois et les quatre domaines de qualification. Les règles générales de fonctionnement subsistent dans leur champ ; la composition spéciale n'est pas une exemption fiscale ou un quota de logements.",
    "Aucune réduction nouvelle : préservation du format territorial adapté de six membres, sans le compter comme une nouvelle fusion d'organismes.",
    "Aucun effet sur les autres territoires ultramarins ni coût de fonctionnement de la commission n'est établi par cet article.",
    "Aucune charge nouvelle identifiée : composition et modalités de qualification inchangées, sans nouveau siège ni rapport à produire.")

xml = """<p>Le schéma de cohérence territoriale comporte en zone de montagne, s'il y a lieu, les études prévues au premier alinéa du I de l'article L. 122-7 et au 1° de l'article L. 122-14.</p>"""
rewrite('R141-1', xml,
    "Coordination nécessaire du renvoi : le premier alinéa visé appartient désormais au I de L122-7. La précision rejoint le renvoi expressément utilisé par L122-14 1°. Les deux études et leur caractère conditionnel « s'il y a lieu » sont conservés en entier : elles permettent l'urbanisation en discontinuité ou les dérogations de construction près des plans d'eau. Aucune étude ne peut être supprimée ici au prix de fermer ces avantages futurs.",
    "L122-7 et L122-14 lus en entier dans le corpus : L122-7 comprend désormais I, II et III ; L122-14 1° vise expressément le premier alinéa du I. La précision n'étend pas R141-1 aux études des autres branches. Conserver les conditions de fond, accords et avis attachés aux dérogations législatives. Aucun nouveau dossier ni reprise d'une étude valablement réalisée n'est nécessaire du seul fait de la précision du renvoi.",
    "Coordination du seul repérage de l'étude au sein de L122-7, sans suppression ni ajout d'étude ; aucune réduction de charge n'est comptée.",
    "Les conditions législatives d'urbanisation en montagne et leurs procédures autonomes restent applicables ; l'article ne donne pas une dispense générale d'étude.",
    "Aucune charge nouvelle identifiée : mêmes deux études éventuelles, même champ montagne ; seule la subdivision I du renvoi est explicitée.",
    [effect('coordination', 'urbanisme-etudes-derogatoires-montagne',
            "Précision de la subdivision contenant l'étude législative déjà visée.",
            "Renvoi au premier alinéa de L122-7, sans mention du I désormais présent dans la source législative.",
            "Renvoi au premier alinéa du I de L122-7 ; étude de L122-14 1° inchangée.",
            'other', "Etablissements chargés d'un SCOT en zone de montagne et opérations utilisant les dérogations concernées.",
            "Précision du renvoi dès l'entrée en vigueur ; études antérieures valables conservées, sans nouveau dépôt.",
            "Aucune nouvelle étude ni pièce ; les conditions des dérogations restent celles de la loi.",
            "les études prévues au premier alinéa de l'article L. 122-7 et au 1° de l'article L. 122-14.",
            "les études prévues au premier alinéa du I de l'article L. 122-7 et au 1° de l'article L. 122-14.")],
    classification='coordination_only',
    benefit="Les études servent de fondement aux dérogations de L122-7 I, autorisant sous conditions une urbanisation en discontinuité, et de L122-14 1°, permettant des constructions et aménagements près de plans d'eau normalement protégés. Les deux voies restent ouvertes aux futures opérations éligibles avec leurs conditions, avis et accords. La précision du I ne retire aucune étude recevable ni n'étend l'obligation à une branche distincte ; aucune dérogation n'est cantonnée aux droits antérieurs.")

retain('R141-6',
    "Maintien intégral de la localisation graphique des protections et des éventuelles zones préférentielles de renaturation, ainsi que de l'identification des biens du patrimoine mondial et de leur zone tampon. Sans localisation, les orientations de L141-10 seraient incertaines pour les propriétaires et instructeurs. Aucun plan autonome supplémentaire, expertise privée ou inventaire fiscal n'est prescrit ici ; les mentions conditionnelles évitent une obligation hors champ.",
    "L141-10 lu en entier : ses 2° et 3° correspondent aux espaces protégés et aux continuités écologiques. Conserver la faculté des zones préférentielles et le « le cas échéant » des biens inscrits ; ne pas transformer ces cartographies en nouvelles interdictions générales. Les engagements patrimoniaux supérieurs ne sont pas abrogés implicitement.",
    "Aucune réduction nouvelle : maintien d'une cartographie nécessaire à la lisibilité des protections existantes et de leurs limites territoriales.",
    "Les règles matérielles de protection, les normes cartographiques et le coût de mise à jour ne sont pas réformés ou chiffrés dans ce lot.",
    "Aucune charge nouvelle identifiée : les mêmes objets cartographiques conditionnels sont conservés, sans couche ou expertise nouvelle.")

retain('R141-6-1',
    "Maintien intégral de la prise en compte de la surface minimale communale de consommation d'espaces et des spécificités littorales ou montagnardes. Ces tempéraments rendent la déclinaison géographique des objectifs d'artificialisation moins restrictive et ne constituent pas un nouvel objectif communal. Les supprimer au titre de la simplification pourrait réduire les possibilités de construire, contrairement à la préservation des avantages.",
    "L141-8 lu : il permet une déclinaison géographique, sans la rendre obligatoire. Conserver le renvoi précis au premier alinéa du 3° bis du III de l'article 194 de la loi 2021-1104 du 22 août 2021, à L121-1 et à l'article 3 de la loi 85-30 du 9 janvier 1985 ; aucune superficie chiffrée non donnée dans la source n'est ajoutée. La source L141-8 1° mentionne les obligations de logement social : sa coordination SRU extérieure au lot reste nécessaire, sans réintroduire ces quotas par R141-6-1.",
    "Aucune nouvelle baisse comptée : maintien des aménagements territoriaux favorables, applicables aux futures déclinaisons sectorielles.",
    "Le régime législatif complet de l'artificialisation et des garanties communales reste autonome ; aucune suppression de quota SRU supplémentaire n'est opérée ici.",
    "Aucune charge nouvelle identifiée : les deux prises en compte restent celles de la source, sans nouveau justificatif ou condition de surface.",
    "La prise en compte de la surface minimale communale peut préserver une capacité d'urbanisation ; celle des spécificités du littoral et de la montagne tempère la territorialisation. Elles sont conservées sans fermeture aux futurs documents ou opérations éligibles. Le texte ne crée pas de franchise fiscale ni ne dispense des protections littorales ; aucune dérogation côtière existante n'est supprimée.")

retain('R141-7',
    "Maintien intégral de la désignation éventuelle des plans d'eau de faible importance. Cette désignation rend effective l'exclusion favorable prévue par L122-12 2° du régime de protection des rives ; la supprimer laisserait la dérogation sans identification praticable. Le caractère facultatif et le critère de faible importance sont conservés, sans inventaire général de tous les plans d'eau.",
    "L122-12 lu intégralement : protection de trois cents mètres autour des plans d'eau de moins de mille hectares, avec exclusions distinctes aux 1° et 2°. R141-7 met en œuvre le seul 2°, sans enlever la voie d'arrêté du 1° ni les possibilités PLU ou carte communale. Aucun seuil de faible importance non fixé dans la source n'est inventé.",
    "Aucune réduction nouvelle : préservation du mécanisme cartographique qui permet de lever la protection riveraine dans les cas légalement recevables.",
    "La décision d'exclure un plan d'eau reste facultative et dépend de sa faible importance ; aucune exclusion automatique ou nouvelle franchise de construction n'est créée.",
    "Aucune charge nouvelle identifiée : désignation éventuelle inchangée, sans nouvelle étude, autorisation ou liste exhaustive imposée.",
    "L'identification des plans d'eau de faible importance ouvre la dérogation de L122-12 2° à l'interdiction riveraine de principe. Elle demeure possible pour les futurs SCOT et les nouvelles situations éligibles, avec le critère légal de faible importance. L'article ne réduit ni l'exclusion par PLU ou carte communale ni celle du 1° sur arrêté ; il ne réserve pas l'avantage aux seuls plans d'eau déjà désignés.")

retain('R141-8',
    "Maintien intégral du diagnostic des usages marins et terrestres du littoral, de leurs perspectives et des orientations de développement, protection et équipement. L141-15 impose un diagnostic général, mais ne décrit pas aussi précisément l'articulation mer-terre ; ce contenu ciblé éclaire les risques, la desserte et les choix côtiers. Il n'exige pas une étude ou un rapport distinct : aucune nouvelle formalité n'est substituée au diagnostic existant.",
    "L141-15 lu en entier : diagnostic et justification des choix figurent déjà aux annexes, sans imposer ici un support supplémentaire. Conserver les trois dimensions développement, protection et équipement. La note source renvoie à l'article 7 du décret 2021-639 et aux deuxième à cinquième alinéas de l'article 7 de l'ordonnance 2020-744 : leur transition historique demeure, sans devenir une date de réforme nouvelle. Aucun schéma de plage, exemption littorale ou rubrique environnementale I50° n'est fermé.",
    "Aucune réduction nouvelle : le contenu littoral utile du diagnostic demeure intégralement, sans rapport additionnel et sans modification des dérogations côtières.",
    "Les documents extérieurs de transition et les prescriptions littorales autonomes ne sont pas réécrits ; aucun achèvement des 209 articles SRU n'est revendiqué.",
    "Aucune charge nouvelle identifiée : même diagnostic intégré aux annexes, sans étude séparée, nouvelle donnée imposée ou nouvelle condition d'autorisation.")

result = [answers[a['number']] for a in sources]
assert len(result) == len(sources) == 24
Path('answer.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
