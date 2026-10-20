import json
import re
from html import unescape
from pathlib import Path

SOURCES = json.loads(Path('source.json').read_text())
REFS = json.loads(Path('reference-targets.json').read_text())
BY_NUMBER = {a['number']: a for a in SOURCES}
RESULTS = {}


def plain(xml):
    return unescape(re.sub(r'<[^>]*>', '', xml or ''))


def paragraphs(number):
    xml = BY_NUMBER[number]['source_xml']
    return [re.sub(r'<p\b[^>]*>', '<p>', p) for p in re.findall(r'<p\b[^>]*>.*?</p>', xml, re.S)]


def impact(classification, assessment, limitations, burdens, effects=None):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=limitations, new_burdens_review=burdens,
                effects=effects or [])


def record(number, proposed, reason, notes, assessment, limitations, burdens,
           effects=None, removed=None, benefit=None):
    source = BY_NUMBER[number]
    obj = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    obj.update(proposed_xml=proposed, reason=reason, review_notes=notes,
               status='retained_unchanged' if proposed is None else 'rewrite_draft')
    if proposed is None:
        obj['classification'] = 'retained_necessary'
        classification = 'retained_necessary'
    else:
        classification = 'material_reduction' if removed else 'coordination_only'
    if removed:
        obj.update(change_type='normative_reduction',
                   reform_policy_id='editorial_direction_2026_10_19',
                   removed_provisions=removed)
    if benefit:
        obj['benefit_review'] = benefit
    obj['substantive_impact'] = impact(classification, assessment, limitations, burdens, effects)
    RESULTS[number] = obj
    return obj


def effect(kind, measure, description, before, after, unit, population,
           transition, replacement, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure, description=description,
                before=before, after=after, unit=unit,
                affected_population=population, conditions_and_transition=transition,
                replacement_or_new_burdens=replacement,
                source_quote=source_quote, proposed_quote=proposed_quote)


record('L661-2', None,
       "Maintien intégral nécessaire de la dérogation mahoraise : elle dispense de la publication au fichier immobilier tout en laissant opérer l'inscription au livre foncier prévue par L631-7-1. L'article n'établit ni taxe, ni agrément, ni déclaration supplémentaire ; le supprimer retirerait une adaptation favorable, sans supprimer l'autorisation de changement d'usage elle-même.",
       "L631-7-1 a été lu dans le corpus : la publication concerne les locaux de compensation lorsque l'autorisation est attachée au local. La dérogation reste utile aussi aux autorisations futures à Mayotte et compatible avec la décision commune facultative de L425-9 ; elle ne transforme pas une autorisation personnelle en droit réel. Aucun quota SRU n'est introduit. Le régime général du changement d'usage reste distinct de cet article territorial.",
       "Aucune réduction nouvelle : maintien de l'exception à la publicité au fichier immobilier pour Mayotte, sans disparition de la publicité foncière locale utile aux tiers.",
       "La suppression éventuelle du régime général d'autorisation ne résulte pas de cette adaptation ; les effets des textes extérieurs de publicité foncière ne sont pas réécrits ici.",
       "Aucune charge nouvelle identifiée : le corps source est conservé intégralement, sans pièce, délai, donnée ou procédure de remplacement.",
       benefit="La seule règle de cet article est une dispense territoriale de publication au fichier immobilier. Elle reste entière pour les situations futures comme anciennes ; l'inscription au livre foncier et l'opposabilité relevant de L631-7-1 ne sont pas supprimées.")

P662 = (
    '<p>Les articles L. 261-9 à L. 261-16 et L. 261-22 et L. 263-1 à L. 263-3 du présent code sont applicables en Polynésie française, à l\'exception :</p>'
    '<p>- au deuxième alinéa de l\'article L. 261-10, des mots : " sauf si le terrain " aux mots : " prestataire de service " ;</p>'
    '<p>- de la première phrase de l\'avant-dernier alinéa de l\'article L. 261-11 ;</p>'
    '<p>- et, à l\'article L. 263-3, de l\'interdiction visant les personnes auxquelles, en application de l\'article L. 241-7, il est interdit de procéder aux opérations mentionnées aux articles L. 214-6 à L. 214-9.</p>'
    '<p>La précision de cette dernière exception s\'applique à compter de l\'entrée en vigueur de la loi qui la prévoit. Elle ne remet en cause ni les contrats valablement conclus ni les droits acquis antérieurement et ne modifie pas les interdictions résultant des condamnations prononcées en application des articles L. 263-1 et L. 263-2. Les dispositions pénales plus douces s\'appliquent dans les conditions du code pénal.</p>'
)
record('L662-1', P662,
       "Coordination nécessaire du champ polynésien, sans nouvelle réduction quantifiée : les mots terminaux « conseil de surveillance » de la dernière exception n'existent plus dans L263-3. La proposition désigne expressément la catégorie actuellement introduite par « ainsi que celles », liée à L241-7, afin de ne pas étendre par ce défaut de concordance une interdiction professionnelle. Les deux autres exceptions et toutes les dispositions étendues sont conservées ; aucune règle de rupture d'emploi n'est importée dans les ventes immobilières.",
       "Lecture des articles L261-9 à L261-16, y compris L261-10-1 et L261-11-1, de L261-22, L263-1 à L263-3, L241-7 et L214-6 à L214-9 dans le corpus. L263-3 vise désormais les opérations L214-6 à L214-9 ; « conseil de surveillance » figure dans L241-7, non dans L263-3. La filiation textuelle exacte de l'ancienne borne n'est pas reconstituée : la clarification favorable est un choix explicite de rédaction et non la preuve d'une portée historique identique. La première phrase de l'avant-dernier alinéa de L261-11 actuel concerne la remise et la communication préalable du règlement de copropriété ; cette exception source est conservée sans la réattribuer à une autre phrase. Ni la garantie financière ni les interdictions autonomes de fraude de L263-1/2 ne sont abrogées. Compétences et mise en œuvre territoriales demeurent à coordonner hors corpus, sans prétendre réécrire le droit polynésien.",
       "Rectification d'une borne de citation devenue introuvable ; aucune seconde baisse d'indemnité, de préavis ou de taxe n'est démontrée. L'exception professionnelle est rendue opératoire sans élargir une interdiction.",
       "Le périmètre historique exact de l'ancienne exception n'est pas prouvé par les seules versions actuelles ; ce point de filiation reste signalé. La règle ne concerne aucun contrat de travail.",
       "Aucune charge nouvelle identifiée : aucune formalité ou interdiction supplémentaire n'est créée ; les protections des acquéreurs et les interdictions fondées sur L263-1/2 subsistent.",
       effects=[effect('coordination', 'polynesie-vente-immeubles-exception-interdiction',
                       "Précision de la catégorie exclue de l'extension territoriale de L263-3.",
                       "Exception repérée entre « ainsi que celles » et une borne « conseil de surveillance » absente de L263-3 actuel ; portée historique non entièrement établie.",
                       "Exception visant expressément la catégorie des interdictions rattachées à L241-7 ; maintien des condamnations L263-1 et L263-2.",
                       'regime', "Personnes participant aux opérations immobilières relevant du champ étendu en Polynésie française.",
                       "Précision prospective ; contrats et droits antérieurs sauvegardés ; loi pénale plus douce dans son champ.",
                       "Pas de déclaration ni d'autorisation nouvelle ; pas de réduction matérielle supplémentaire tenue pour établie.",
                       '-et à l\'article L. 263-3, des mots : " ainsi que celles " aux mots : " conseil de surveillance ".',
                       "- et, à l'article L. 263-3, de l'interdiction visant les personnes auxquelles, en application de l'article L. 241-7, il est interdit de procéder aux opérations mentionnées aux articles L. 214-6 à L. 214-9.")],
       benefit="Les exceptions polynésiennes de L261-10 et L261-11 sont conservées pour les opérations futures. La troisième exception est précisée favorablement sans ajouter une interdiction ; les garanties des versements et le plafond immobilier d'indemnité de L261-12/14 subsistent. L'identité exacte de sa portée historique reste à établir.")

record('L662-2', None,
       "Maintien intégral de l'adaptation de l'indice de révision des ventes immobilières en Polynésie française. L'index local BTP 01 et la répartition des compétences pour le définir et en limiter l'usage encadrent une clause facultative de révision ; ils ne constituent pas une nouvelle autorisation de vendre ni un prélèvement à supprimer.",
       "Lecture de L261-11-1 : la révision reste facultative, porte sur chaque paiement ou dépôt et compare les indices publiés aux dates prévues. La substitution expresse de son troisième alinéa conserve la compétence de l'assemblée de la Polynésie française et du haut-commissaire ; on ne réimporte pas silencieusement la fourchette nationale 60/80 % dans le texte territorial. L'existence actuelle de l'intitulé institutionnel et des actes locaux d'application n'est pas vérifiée par un service externe, interdit dans cette tâche.",
       "Aucun allègement nouveau : la règle rend utilisable un indice local pour une révision conventionnellement prévue et en organise la limitation ; sa suppression ne supprimerait pas la clause de révision.",
       "Les actes locaux définissant effectivement l'index et la limite ne sont pas fournis ; aucun nouveau pourcentage ni effet chiffré n'en est inféré.",
       "Aucune charge nouvelle identifiée : maintien intégral du texte officiel et de son mécanisme territorial, sans justificatif ou déclaration ajouté.",
       benefit="L'adaptation à l'index BTP 01 et la fixation locale de la limite demeurent disponibles pour les futurs contrats prévoyant une révision. La révision n'est pas rendue obligatoire et aucun taux national n'est substitué à l'encadrement territorial.")

record('L711-1', None,
       "Maintien du registre d'identification des seuls syndicats administrant un immeuble à destination partielle ou totale d'habitation. L'identité du responsable et les alertes d'insalubrité ont une fonction de prévention et d'information distincte des remontées financières et techniques générales supprimées dans L711-2. La finalité du registre ne suffit pas à rétablir ces remontées.",
       "Articulation avec L711-2 à L711-7 : champ légal inchangé, obligations déclaratives réduites dans L711-2, suppression des frais d'immatriculation d'office à la vente dans L711-5 et de l'astreinte et du verrou d'aides dans L711-6. La définition des syndicats par l'article 14 de la loi de 1965 reste une référence externe, sans nouveau texte de cette loi rédigé ici. Il ne s'agit pas d'un descendant SRU documenté dans ce lot.",
       "Le registre subsiste comme infrastructure d'identification et de prévention. Ce maintien ne constitue pas une simplification nouvelle et ne préjuge pas du coût net des réductions apportées aux articles suivants.",
       "Aucune suppression intégrale du registre n'est décidée ; ses coûts publics résiduels et la perte éventuelle de données d'observation ne sont pas chiffrés.",
       "Aucune charge nouvelle identifiée : la finalité et le champ source demeurent entiers, sans étendre le registre aux immeubles exclusivement non résidentiels.")

p = paragraphs('L711-2')
P7112 = (
    '<p>I. ― Les syndicats de copropriétaires sont tenus de déclarer les données mentionnées au II et au 4° du III du présent article ainsi que toute modification les concernant. Aucune déclaration annuelle de ces données n\'est exigée en l\'absence de modification. Les données financières et techniques ainsi que les données générales de repérage et d\'accompagnement qui relevaient des 1° à 3° du III ne font plus l\'objet d\'une déclaration au registre, lors de l\'immatriculation ou de ses mises à jour.</p>'
    + ''.join(p[1:5])
    + p[5]
    + '<p>1° Abrogé ;</p><p>2° Abrogé ;</p><p>3° Abrogé ;</p>'
    + p[9] + p[10]
    + '<p>Ces dispositions s\'appliquent aux déclarations effectuées à compter de l\'entrée en vigueur de la loi qui les prévoit, y compris lorsqu\'elles se rapportent à des exercices antérieurs. Aucune transmission tardive ni régularisation des seules données supprimées n\'est exigée. Les données déjà régulièrement recueillies restent soumises aux règles de conservation, de consultation et de protection qui leur sont applicables. Les obligations autonomes de tenue des comptes, de diagnostic, d\'information des copropriétaires et acquéreurs ainsi que les pouvoirs de police et de contrôle demeurent applicables dans leur champ propre.</p>'
)
record('L711-2', P7112,
       "Réduction de fond : suppression des trois catégories générales de remontées financières, techniques et de repérage au registre, à l'immatriculation comme en mise à jour, y compris la déclaration financière annuelle. L'absence de confirmation annuelle des seules données maintenues sans changement est précisée sans revendiquer un gain supplémentaire : R711-10 n'exigeait déjà leur actualisation qu'en cas de modification. Les comptes, diagnostics et informations de vente restent établis dans leur régime propre ; leur ressaisie générale au registre n'est plus imposée. Sont intégralement conservés le II, l'alerte du 4° du III connue du syndic et le IV relatif à la publicité et à la CNIL. Les subdivisions sont maintenues.",
       "R711-9 II/III et R711-10 lus : exercice comptable, budget, provisions, dettes, impayés, copropriétaires débiteurs, employés, bâtiments, étiquettes énergétiques, ascenseurs, période et chauffage alimentaient les collectes retirées. À coordonner expressément : R711-4/5, R711-9/10/11/13/14/15/21 et l'arrêté prévu à R711-21 ; ces textes non assignés ne sont pas réputés réécrits. Les demandes futures et les régularisations exclusivement fondées sur les catégories supprimées sont écartées par la disposition législative elle-même. Les exceptions réglementaires pour petites copropriétés et premiers exercices ne sont pas remplacées par une obligation plus large. Les données relatives aux plaintes restent limitées à celles connues du syndic ; aucun accès pénal ou transmission nouvelle par une autre autorité n'est créé. Renvois L615-6 et livre V : procédures d'habitat dangereux, distinctes de la carence SRU abrogée.",
       "Suppression effective d'une alimentation générale du registre et de ses mises à jour financières annuelles ; les informations d'identité, de procédure et de danger restent déclarables. Le gain ne consiste pas dans le simple réemploi d'informations déjà détenues par l'administration.",
       "Comptabilité, diagnostics, fiche synthétique, documents de vente, contrôles et demandes ciblées sur fondement autonome subsistent ; l'effet sur le repérage précoce et les coûts publics n'est pas mesuré.",
       "Aucune charge nouvelle identifiée : aucun registre, déclaration, preuve ou transmission de remplacement n'est créé. Les données déjà déclarées conservent leur régime de protection et de conservation, sans remise à jour forcée des catégories supprimées.",
       effects=[effect('obligation_removed', 'copropriete-registre-fin-collectes-generales',
                       "Fin de la déclaration générale financière et technique et des données générales de repérage au registre.",
                       "Tous les syndicats du champ devaient déclarer les principales données des III 1° à 3° et leurs modifications ; R711-10 imposait en outre une mise à jour financière annuelle sous deux mois après l'assemblée d'approbation des comptes.",
                       "Aucune de ces trois catégories à déclarer à l'immatriculation ou en mise à jour. Le II et l'alerte connue du III 4° demeurent ; l'absence de confirmation annuelle des seules données maintenues sans changement est une précision, sans gain supplémentaire compté.",
                       'legal_duty', "Syndicats de copropriétaires d'immeubles à destination partielle ou totale d'habitation et leurs déclarants.",
                       "Déclarations postérieures à l'entrée en vigueur, même pour exercices anciens ; aucune régularisation des seules données supprimées ; conservation légale des données déjà recueillies.",
                       "Aucun dépôt de remplacement ; les comptes, diagnostics et protections autonomes ne sont pas retirés.",
                       '1° De connaître la situation financière de la copropriété ;',
                       "Les données financières et techniques ainsi que les données générales de repérage et d'accompagnement qui relevaient des 1° à 3° du III ne font plus l'objet d'une déclaration au registre, lors de l'immatriculation ou de ses mises à jour.")],
       removed=["Déclaration à l'immatriculation et en actualisation des données financières générales du III 1°, y compris la déclaration annuelle des informations financières prévue par R711-10.",
                "Déclaration des caractéristiques techniques générales du III 2° et des données générales de repérage et d'accompagnement du III 3° au registre."],
       benefit="Les dispenses réglementaires de certaines données pour petites copropriétés ou premier exercice ne sont pas refermées : toute la collecte correspondante disparaît pour les déclarations futures. Les aides restent ouvertes sans verrou de registre selon L711-6 proposé. Les alertes de danger connues et les droits d'information ne sont pas remplacés par une nouvelle condition d'aide.")

record('L711-3', None,
       "Maintien intégral de l'accès territorial des personnes publiques aux informations du registre pour les politiques de l'habitat et de l'accès des notaires pour informer les acquéreurs et accomplir leur mission de L711-5. Il s'agit d'accès aux informations existantes, non d'une collecte nouvelle ; l'article ne contraint pas les syndicats à fournir un second dossier.",
       "Le renvoi à L711-5 reste opérant après réduction de sa mission à la mention du numéro attribué et à la faculté de signaler des erreurs. La référence générale aux données du registre ne rétablit pas les III 1° à 3° supprimés de L711-2 ; les données historiques restent sous leurs règles de conservation. La note source comporte un renvoi au II de « présent article » alors que L711-3 n'a pas de II : incohérence historique de la note, non reproduite comme condition normative ; les dates 2016/2017/2018 ne deviennent pas celles de la réforme.",
       "Aucun allègement nouveau démontré : le droit d'accès utile demeure, dans le territoire et pour les finalités prévues, sans nouvelle obligation de remonter des données.",
       "Les modalités de consultation et leurs coûts restent régis notamment par R711-16 ; aucune extension d'accès à des données non légalement disponibles n'est décidée.",
       "Aucune charge nouvelle identifiée : conservation exacte de la source ; la réduction du contenu alimenté au registre découle de L711-2 et n'est pas comptée une seconde fois.")

record('L711-4', None,
       "Maintien de la répartition des responsabilités : immatriculation initiale par le notaire lors de la mise en copropriété, par le syndic dans les autres cas, et actualisation par le syndic. Elle identifie le responsable du registre minimal conservé et évite un double déposant ; le renvoi à L711-2 ne porte désormais que sur ses données maintenues. Aucun nouveau corps n'est nécessaire.",
       "Le renvoi est dynamique vers le seul contenu maintenu de L711-2 ; il ne maintient ni sa collecte financière et technique générale ni une confirmation annuelle sans changement. La dématérialisation est maintenue comme mode du registre existant, sans exigence supplémentaire d'abonnement ou de plateforme. Les contraintes de compte et de rattachement R711-2 à R711-8 ainsi que les transitions 2016/2017/2018 ont été lues ; elles ne sont pas déclarées abolies par cet article. La note historique au II de « présent article » est une anomalie de rédaction des anciennes notes d'échelonnement, sans créer de nouvel assujettissement.",
       "Aucune réduction propre : une attribution claire de l'immatriculation et de l'actualisation reste nécessaire au registre d'identité. La réduction du contenu déclaré est portée par L711-2, sans seconde obligation comptée ici.",
       "La charge initiale d'immatriculation et le canal dématérialisé demeurent. Les règlements de comptes et rattachements ne sont pas réécrits dans ce lot.",
       "Aucune charge nouvelle identifiée : le texte entier reste celui de la source, avec un renvoi dont la portée se réduit par la réforme de son article cible.")

P7115 = (
    '<p>Tout acte authentique de vente devant notaire relatif à un lot de copropriété comporte la mention du numéro d\'immatriculation de la copropriété lorsqu\'un tel numéro lui a été attribué.</p>'
    '<p>L\'absence d\'immatriculation du syndicat de copropriétaires n\'impose pas au notaire chargé de l\'établissement de l\'acte de vente de procéder d\'office à cette immatriculation et ne fait pas obstacle à la vente. Elle ne dispense pas de l\'immatriculation prévue à l\'article L. 711-4.</p>'
    '<p>Aucuns frais d\'immatriculation d\'office ne sont mis à la charge du syndic ou du syndicat sur le fondement du présent article pour les ventes conclues à compter de l\'entrée en vigueur de la loi qui prévoit cette suppression.</p>'
    '<p>Le notaire peut informer l\'établissement public chargé de la tenue du registre de toute erreur qu\'il y constate.</p>'
    '<p>Ces dispositions s\'appliquent aux ventes conclues à compter de cette entrée en vigueur, y compris si elles ont été précédées d\'une promesse. Les frais légalement engagés au titre d\'une immatriculation d\'office accomplie avant cette date ainsi que les droits, restitutions et recours qui s\'y rapportent demeurent régis par les dispositions antérieures. Aucun rattrapage d\'immatriculation d\'office au titre d\'une vente antérieure n\'est exigé sur le seul fondement du présent article après cette date.</p>'
)
# Conserver une séparation textuelle entre les alinéas : la preuve extraite
# sans balises doit aussi correspondre au texte HTML rendu.
P7115 = P7115.replace('</p><p>', '</p> <p>')
record('L711-5', P7115,
       "Réduction de fond des formalités notariales de vente : fin de l'immatriculation d'office imposée en l'absence de syndic ou après mise en demeure, et de sa refacturation légale ; le numéro n'est mentionné que s'il existe et son absence ne bloque pas la vente. Le signalement systématique de toute erreur devient facultatif. L'immatriculation normale de L711-4 et les informations matérielles à donner à l'acquéreur subsistent.",
       "À coordonner dans R711-1 6°, R711-11 II, R711-14 et R711-15 ; R711-11 II renvoie déjà à tort à l'immatriculation « d'office prévue à L711-4 », alors que son fondement actuel est L711-5. La référence générale d'accès notarial de L711-3 reste utile pour obtenir le numéro et informer l'acquéreur ; elle n'impose plus une immatriculation d'office. R711-20 concerne la déclaration de disparition d'un syndicat et reste distinct. Les notes de 2014 échelonnent l'entrée en vigueur historique et ne conditionnent pas l'allègement futur. Les devoirs autonomes de conseil, de vérification du titre et d'information de vente ne sont pas supprimés.",
       "Suppression réelle de l'immatriculation notariale d'office liée à la vente, de sa charge financière spécifique et du signalement obligatoire de toute erreur ; le registre minimal et l'identification d'un numéro existant restent en place.",
       "Ni l'immatriculation initiale à la création de la copropriété ni les autres frais notariaux ne sont abolis. Le montant moyen économisé n'est pas établi et n'est pas assimilé à une taxe supprimée.",
       "Aucune charge nouvelle identifiée : aucune déclaration ni attestation d'absence de numéro ne remplace l'immatriculation d'office ; le signalement facultatif n'ajoute pas de devoir au notaire.",
       effects=[effect('obligation_removed', 'copropriete-vente-formalites-registre',
                       "Suppression de l'immatriculation d'office et des frais mis à la charge du syndic ou du syndicat à l'occasion de la vente.",
                       "Le notaire devait immatriculer d'office en l'absence de syndic ou après un mois de mise en demeure infructueuse ; le syndic, ou le syndicat si le syndic n'est pas rémunéré, supportait les frais.",
                       "La vente n'impose plus cette immatriculation d'office ni ces frais ; mention du numéro seulement s'il est attribué. L711-4 reste applicable à l'immatriculation normale.",
                       'legal_duty', "Notaires, syndics et syndicats concernés par des ventes de lots non immatriculés.",
                       "Ventes conclues à compter de l'entrée en vigueur, même avec promesse antérieure ; frais des formalités déjà accomplies protégés ; pas de rattrapage d'office pour anciennes ventes.",
                       "Aucune attestation négative ou autre formalité de vente de remplacement.",
                       "En l'absence de syndic désigné ou lorsque la mise en demeure mentionnée à l'article L. 711-6 est restée sans effet au terme d'un délai d'un mois, le notaire chargé de l'établissement de l'acte de vente procède d'office à l'immatriculation du syndicat de copropriétaires.",
                       "L'absence d'immatriculation du syndicat de copropriétaires n'impose pas au notaire chargé de l'établissement de l'acte de vente de procéder d'office à cette immatriculation et ne fait pas obstacle à la vente."),
                effect('obligation_removed', 'copropriete-vente-formalites-registre',
                       "Le signalement au registre de toute erreur constatée par le notaire devient facultatif.",
                       "Chaque erreur constatée devait être signalée à l'établissement public tenant le registre.",
                       "Le signalement demeure possible mais n'est plus une obligation propre à cet article.",
                       'legal_duty', "Notaires intervenant dans les ventes de lots de copropriété.",
                       "Ventes relevant du nouveau régime, sans effet sur les responsabilités nées antérieurement ni sur les devoirs autonomes de conseil.",
                       "Pas de déclaration annuelle ou de registre d'erreurs de remplacement.",
                       "Le notaire informe l'établissement public chargé de la tenue du registre de toute erreur qu'il y constate.",
                       "Le notaire peut informer l'établissement public chargé de la tenue du registre de toute erreur qu'il y constate.")],
       removed=["Immatriculation d'office obligatoire par le notaire lors d'une vente en l'absence de syndic ou après mise en demeure infructueuse d'un mois.",
                "Imputation obligatoire au syndic, ou au syndicat en cas de syndic non rémunéré, des frais de cette immatriculation d'office pour les nouvelles ventes.",
                "Obligation spéciale faite au notaire de signaler au teneur du registre toute erreur qu'il constate, désormais simple faculté."],
       benefit="La vente reste possible malgré l'absence de numéro et aucune attestation négative n'est exigée. Les droits de l'acquéreur à l'information et les recours sur les frais antérieurs subsistent. La non-imputation des frais d'astreinte aux copropriétaires, régie par L711-6, n'est pas utilisée pour créer ici une nouvelle charge.")

P7116 = (
    '<p>I. ― Lorsque le syndic n\'a pas procédé à l\'immatriculation du syndicat de copropriétaires ou lorsqu\'il n\'a pas transmis à l\'établissement public chargé de la tenue du registre les informations prévues à l\'article L. 711-2, l\'établissement public, un copropriétaire ou toute personne qui y a un intérêt peut mettre en demeure, par lettre recommandée avec demande d\'avis de réception, le syndic d\'y procéder.</p>'
    '<p>II. ― L\'astreinte prévue par le présent article dans sa rédaction antérieure est supprimée à compter de l\'entrée en vigueur de la loi qui prévoit cette suppression. Aucune astreinte ne peut être prononcée après cette date sur ce fondement ; les astreintes déjà prononcées cessent de courir à cette date. Les sommes légalement nées de périodes antérieures ainsi que leur recouvrement, les restitutions et les recours demeurent régis par les dispositions antérieures, y compris l\'interdiction de les facturer aux copropriétaires lorsque le syndic est rémunéré, sous réserve de l\'application de la loi répressive plus douce dans son champ.</p>'
    '<p>III. ― L\'immatriculation au registre et l\'actualisation de ses données ne sont plus des conditions d\'attribution ou de versement des subventions de l\'Etat, de ses établissements publics, des collectivités territoriales, de leurs groupements ou de leurs établissements publics aux syndicats de copropriétaires. Aucune immatriculation ni actualisation n\'est exigée en remplacement sur le seul fondement du présent chapitre pour l\'accès à ces subventions. Les autres conditions légales propres aux aides et leurs contrôles restent applicables.</p>'
    '<p>Le III s\'applique aux demandes en cours et aux décisions d\'attribution ou de versement prises à compter de cette entrée en vigueur. Il ne rouvre pas les décisions de refus devenues définitives, ne crée aucun droit automatique à une subvention et préserve les aides valablement attribuées ainsi que les créances, restitutions et recours antérieurs. Le défaut d\'immatriculation ou d\'actualisation ne peut, après cette date, justifier à lui seul de suspendre un versement restant à effectuer.</p>'
)
record('L711-6', P7116,
       "Réduction de fond : suppression de l'astreinte hebdomadaire propre au registre et du verrou d'attribution et de versement des subventions tenant à l'immatriculation et à l'actualisation. La mise en demeure du I, les informations utiles conservées dans L711-2 et les contrôles des conditions de fond des aides demeurent. La protection contre la refacturation des anciennes astreintes aux copropriétaires est expressément conservée.",
       "Le maximum source de 20 € par lot et par semaine disparaît pour l'avenir, sans remboursement général des créances nées antérieurement ; les astreintes déjà prononcées cessent pour les périodes futures. Le III ne fait pas renaître une aide refusée définitivement mais ouvre les demandes et versements futurs, y compris sur engagements anciens, sans condition de rattrapage du registre. Les règlements et formulaires d'aides ANAH et des autres financeurs doivent être coordonnés pour ne pas rétablir ce verrou au seul titre de ce chapitre ; leurs bases, budgets et contrôles autonomes ne sont pas réputés supprimés. La responsabilité civile du syndic et les recours de droit commun ne sont pas effacés. La note historique 2016/2017/2018 ne devient pas une transition future.",
       "L'astreinte du registre cesse pour les périodes nouvelles et l'aide n'est plus bloquée par l'état administratif du registre. Il s'agit de deux contraintes retirées, non d'une suppression de la comptabilité, d'une taxe de droit commun ou des conditions matérielles des aides.",
       "Les créances anciennes restent contrôlables et recouvrables avec leurs protections, sauf droit répressif plus doux applicable. Aucun montant de subvention supplémentaire ni économie globale de conformité n'est chiffré.",
       "Aucune charge nouvelle identifiée : l'astreinte n'est remplacée par aucune pénalité et l'accès aux aides par aucune attestation de registre ; les contrôles autonomes de l'usage des fonds restent inchangés.",
       effects=[effect('obligation_removed', 'copropriete-registre-fin-astreinte',
                       "Extinction prospective de l'astreinte spéciale liée au registre.",
                       "Après un mois de mise en demeure, astreinte possible jusqu'à 20 euros par lot et par semaine jusqu'à transmission ou actualisation complète, sans facturation aux copropriétaires si le syndic est rémunéré.",
                       "Aucune nouvelle astreinte sur ce fondement ; fin des périodes futures des astreintes déjà prononcées ; dettes anciennes et protection de non-refacturation conservées.",
                       'euro', "Syndics et syndicats avec syndic non rémunéré relevant du registre des copropriétés.",
                       "Dès l'entrée en vigueur ; périodes antérieures, restitutions et recours préservés sous réserve de la loi répressive plus douce.",
                       "Aucune amende ni astreinte de remplacement créée ; responsabilité civile autonome inchangée.",
                       'Le montant de l\'astreinte ne peut être supérieur à 20 € par lot et par semaine.',
                       "Aucune astreinte ne peut être prononcée après cette date sur ce fondement ; les astreintes déjà prononcées cessent de courir à cette date."),
                effect('relief_extended', 'copropriete-aides-sans-verrou-registre',
                       "Fin de la condition d'immatriculation et d'actualisation pour attribuer et verser les subventions.",
                       "Les syndicats ne pouvaient bénéficier des subventions publiques énumérées qu'après immatriculation et actualisation des données.",
                       "Ces seules conditions ne peuvent plus fonder un refus ou suspendre un versement ; les conditions matérielles et budgets propres aux aides subsistent.",
                       'legal_duty', "Syndicats demandant ou percevant des subventions de l'Etat, de ses établissements publics ou des collectivités, groupements et établissements publics locaux.",
                       "Demandes en cours et attributions ou versements futurs, y compris reliquats d'aides anciennes ; pas de réouverture automatique des refus définitifs.",
                       "Aucune attestation de substitution ; aucun droit automatique à une aide.",
                       "III. ― Les syndicats de copropriétaires ne peuvent bénéficier de subventions de l'Etat, de ses établissements publics, des collectivités territoriales, de leurs groupements ou de leurs établissements publics qu'à la condition d'être immatriculés au registre et que leurs données soient actualisées.",
                       "L'immatriculation au registre et l'actualisation de ses données ne sont plus des conditions d'attribution ou de versement des subventions de l'Etat, de ses établissements publics, des collectivités territoriales, de leurs groupements ou de leurs établissements publics aux syndicats de copropriétaires.")],
       removed=["Astreinte spécifique du teneur du registre, plafonnée à 20 euros par lot et par semaine après mise en demeure infructueuse d'un mois, pour les périodes futures.",
                "Condition d'immatriculation et d'actualisation des données du registre pour attribuer et verser les subventions publiques aux syndicats de copropriétaires."],
       benefit="La non-refacturation aux copropriétaires des anciennes astreintes du syndic rémunéré reste expresse. Pour l'avenir l'astreinte entière disparaît, sans prélèvement équivalent. Les subventions restent accessibles aux futures copropriétés éligibles sans verrou de registre ; les aides acquises et recours sont conservés, sans promettre un financement automatique.")

record('L711-7', None,
       "Maintien de l'habilitation réglementaire nécessaire à la tenue du registre, à la sécurité des accès et aux modalités techniques. Elle s'exerce sous les nouvelles limites législatives de L711-2, L711-5 et L711-6 et n'autorise pas à rétablir les données, immatriculations d'office, astreintes ou conditions d'aide supprimées.",
       "Le décret en Conseil d'Etat n'est pas un agrément demandé à chaque copropriété. La coordination des R711-1 à R711-21 et de l'arrêté technique est signalée aux articles réformés ; le maintien de cette habilitation ne vaut pas approbation de toutes leurs formalités actuelles ni constat de leur réécriture.",
       "Aucun gain autonome : conservation de la base d'application technique d'un registre maintenu, dont les charges législatives sont réduites par d'autres articles du lot.",
       "La portée et le coût des règlements d'exécution restent à coordonner dans les lots qui leur sont assignés ; ils ne peuvent excéder les obligations législatives subsistantes.",
       "Aucune charge nouvelle identifiée : le texte entier est maintenu ; il ne crée ni une nouvelle collecte ni une condition d'accès aux aides.")

record('L721-1', None,
       "Maintien intégral des informations immédiatement utiles dans les annonces : statut de copropriété, nombre de lots, charges courantes annuelles, dépenses énergétiques théoriques pour l'habitation et procédures de difficulté. Leur remise seulement après engagement ne remplit pas la fonction précontractuelle de comparaison du coût et du risque ; supprimer ces mentions retirerait une protection de consentement plutôt qu'un doublon de dépôt administratif.",
       "Les montants restent ceux de la quote-part du vendeur au budget prévisionnel, non l'ensemble des charges futures ou une garantie de consommation. Le 4° est limité aux lots d'habitation et à une indication théorique. Les procédures 29-1 A/29-1 de la loi de 1965 et L615-6 sont distinctes de la carence SRU de L302-9-1 : leur mention ne rétablit aucun quota communal. Les obligations énergétiques parallèles d'autres textes ne sont pas réputées supprimées par une simple suppression de ce renvoi.",
       "Aucune réduction nouvelle : les cinq catégories d'information de l'annonce restent utiles à l'évaluation du coût et des difficultés de la copropriété avant de s'engager.",
       "Les coûts de préparation et les éventuels recoupements avec les règles générales d'annonce ne sont pas quantifiés ; aucun nouveau dossier diagnostic n'est créé par cet article.",
       "Aucune charge nouvelle identifiée : toutes les mentions et leurs limites sont celles de la source entière, sans nouveau contenu obligatoire ni calendrier.",
       benefit="Les futurs acquéreurs conservent les mêmes informations avant engagement. La limitation du renseignement énergétique aux lots d'habitation et son caractère théorique restent entiers ; aucune extension aux lots annexes ou garantie de dépenses réelles n'est ajoutée.")

record('L721-3', None,
       "Maintien intégral du point de départ protecteur des délais de rétractation et de réflexion après communication des informations légalement exigibles. Ce mécanisme garantit un consentement informé et ne crée pas un second délai cumulatif après une remise complète. Il ne rend pas exigibles les pièces dont L721-2 dispense déjà la vente.",
       "L721-2 et L271-1 lus en entier : premier alinéa, les 1° et 2° du II exigibles ; deuxième alinéa, le 1° et le c du 2° pour le projet authentique sans promesse. Les exceptions pour acquéreur déjà copropriétaire, lot annexe et certaines petites copropriétés conservent leur portée propre. Les autres documents du II ne deviennent pas tous des causes de report par extension de cet article. Les dix jours de L271-1 ne sont pas le préavis de quinze jours de rupture du contrat unique. La graphie source « L. 721 2 » désigne sans ambiguïté L721-2, sans erreur de cible à corriger par nouveau corps.",
       "Aucun allègement nouveau : le délai légal ne commence qu'après les seules communications qui le déclenchent dans chaque voie. La protection contre une signature non éclairée demeure entière.",
       "Aucune réduction des dix jours ni suppression de document non assigné n'est décidée ici ; les modalités de notification restent celles de L271-1.",
       "Aucune charge nouvelle identifiée : aucun accusé, attestation ou délai de remplacement n'est ajouté au mécanisme officiel maintenu.",
       benefit="Le droit de rétractation ou de réflexion reste effectif pour les futurs acquéreurs. L'expression « exigibles » conserve les dispenses de L721-2 ; ni les pièces dispensées ni les autres documents hors des renvois limitatifs de L721-3 ne deviennent une condition supplémentaire du délai.")

record('L731-2', None,
       "Maintien de la présentation du diagnostic technique global à la première assemblée suivant sa réalisation ou sa révision. Une dépense de diagnostic décidée ou imposée ne peut éclairer les décisions de travaux si les copropriétaires n'en reçoivent pas le contenu ; la règle ne commande pas un diagnostic nouveau ni une assemblée spéciale.",
       "L731-1 lu en entier : décision sur la réalisation, majorité de l'article 24 et contenu technique. La note de 2021 relative aux dates d'entrée en vigueur n'est pas une date de réforme à réutiliser. Le diagnostic complet réalisé pour la copropriété reste présenté ; la limitation propre à la demande de police de L731-5 proposé ne transforme pas toute demande de police en nouvelle commande globale.",
       "Aucune baisse propre : information collective conservée à une assemblée existante, sans périodicité ni seconde présentation obligatoire nouvelle.",
       "Les obligations autonomes de diagnostic et de plan de travaux ne sont pas abrogées ; le coût de leur réalisation n'est pas évalué ici.",
       "Aucune charge nouvelle identifiée : aucune réunion dédiée, pièce ou délai supplémentaire n'est ajouté à l'obligation source.")

p = paragraphs('L731-5')
P7315 = (
    p[0][:-4]
    + ' Pour cette seule demande, les éléments prévus aux 3° et 4° de l\'article L. 731-1 ne sont pas exigés ; l\'évaluation du coût et la liste des travaux sont limitées à ceux nécessaires à la conservation de l\'immeuble et à la préservation de la santé et de la sécurité des occupants. Un diagnostic technique global déjà réalisé peut être produit sans être refait du seul fait de cette limitation. Les obligations de diagnostic de performance énergétique et de planification de travaux résultant d\'un autre fondement restent applicables dans leur champ propre.</p>'
    + p[1].replace("le diagnostic prévu à l'article L. 731-1", "le diagnostic mentionné au I, dans les limites de contenu qui y sont fixées,")
    + '<p>Ces dispositions s\'appliquent aux demandes notifiées à compter de l\'entrée en vigueur de la loi qui les prévoit et aux demandes en cours n\'ayant pas encore donné lieu à la réalisation du diagnostic. Elles ne font pas courir un nouveau délai d\'un mois. Les diagnostics déjà réalisés, les contrats de réalisation déjà conclus ainsi que les frais et recours antérieurs demeurent régis par les dispositions qui leur sont applicables.</p>'
)
record('L731-5', P7315,
       "Réduction de fond limitée à la police de sécurité : la demande ne peut plus imposer les volets d'amélioration de gestion patrimoniale et de performance énergétique du diagnostic global, ni la liste et l'évaluation des seuls travaux d'économies d'énergie. L'analyse des parties et équipements communs, de leurs obligations de construction, de la conservation et de la santé-sécurité reste exigible. Le délai d'un mois et la réalisation d'office aux frais du syndicat restent des garanties d'effectivité de la police.",
       "L731-1 lu : ses 1° et 2° subsistent pour cette demande, ses 3° et 4° ne sont plus imposés sur ce seul fondement, et son dernier alinéa est limité aux travaux de conservation et de santé-sécurité. Les diagnostics énergétiques et plans de travaux autonomes ne sont pas supprimés. Pas de formulaire ni certificat de sécurité nouveau. Les dispositions ne modifient pas l'entrée en vigueur historique de 2021 des arrêtés de police ; les contrats déjà conclus et frais anciens restent protégés. La demande doit toujours intervenir dans le livre V, pour des parties communes d'un immeuble collectif à usage principal d'habitation présentant des désordres potentiels, et non pour toute copropriété sans critère de risque.",
       "Allègement du contenu obligatoire d'un diagnostic demandé dans une procédure de police : retrait de ses volets patrimonial et énergétique non nécessaires à cette procédure, avec maintien des vérifications de conservation, santé et sécurité.",
       "Gain limité au travail non déjà réalisé ou contractuellement engagé ; les obligations énergétiques autonomes peuvent encore imposer un diagnostic. Aucune économie moyenne ni suppression de diagnostic de sécurité n'est affirmée.",
       "Aucune charge nouvelle identifiée : une demande déjà prévue devient plus étroite, sans attestation alternative, et un diagnostic existant peut être remis sans être refait. Les délais et frais d'office existants ne sont pas augmentés.",
       effects=[effect('obligation_removed', 'copropriete-diagnostic-police-cible-securite',
                       "Retrait des volets de gestion patrimoniale et de performance énergétique du diagnostic imposable sur le seul fondement de la police de sécurité.",
                       "La demande portait sur le diagnostic entier de L731-1, incluant son 3° d'amélioration de gestion et son 4° de performance énergétique, ainsi que les travaux d'économies d'énergie.",
                       "Les 3° et 4° ne sont pas exigibles pour cette demande ; coûts et travaux limités à conservation, santé et sécurité. Autres fondements énergétiques inchangés ; délai d'un mois maintenu.",
                       'legal_duty', "Syndicats et syndics de copropriétés collectives à usage principal d'habitation présentant des désordres potentiels et visés par une demande de police du livre V.",
                       "Demandes nouvelles et en cours avant réalisation ; aucun recommencement du mois ; diagnostics réalisés et contrats conclus sauvegardés.",
                       "Pas de nouveau rapport distinct : seule la portée de la demande existante est réduite, sans retirer les vérifications de sécurité.",
                       "demander au syndic de lui produire le diagnostic prévu à l'article L. 731-1.",
                       "Pour cette seule demande, les éléments prévus aux 3° et 4° de l'article L. 731-1 ne sont pas exigés ; l'évaluation du coût et la liste des travaux sont limitées à ceux nécessaires à la conservation de l'immeuble et à la préservation de la santé et de la sécurité des occupants.")],
       removed=["Exigibilité, dans la seule demande de police de L731-5, de l'analyse d'amélioration de gestion technique et patrimoniale prévue au 3° de L731-1.",
                "Exigibilité, sur ce seul fondement de police, du diagnostic de performance énergétique du 4° et du volet de travaux d'économies d'énergie sans nécessité de conservation, santé ou sécurité."],
       benefit="Le syndic peut produire un diagnostic global déjà réalisé sans nouvelle étude et bénéficie de la limitation pour les demandes futures et celles encore en cours avant réalisation. Le mois laissé pour produire le diagnostic, les protections de santé-sécurité et les droits sur les contrats et frais antérieurs demeurent.")

record('L732-1', None,
       "Maintien intégral du champ des prêts collectifs : dépenses de réparation, d'amélioration ou d'entretien d'un immeuble financées par un syndicat de copropriétaires. Cette délimitation donne accès aux règles protectrices du chapitre et ne prescrit pas à elle seule de souscrire un emprunt, d'obtenir un agrément ou de fournir un dossier supplémentaire.",
       "Le renvoi à l'article 14 de la loi de 1965 identifie le syndicat, sans viser un contrat d'emploi. L732-2 et L732-3 conservent respectivement le champ du prêt et les facilités de remboursement anticipé. Aucune cotisation nouvelle au FNAL ou taxe de financement n'est créée par ce chapitre.",
       "Aucun allègement autonome : conservation du champ donnant accès aux prêts collectifs pour les travaux d'immeuble et à leurs protections.",
       "Le texte extérieur de la loi de 1965 n'est pas réécrit ; les conditions bancaires, décisions collectives et dispositifs d'aides gardent leur champ propre.",
       "Aucune charge nouvelle identifiée : maintien exact du champ matériel et personnel de la source, sans extension d'assujettissement.",
       benefit="L'accès au régime des prêts collectifs reste ouvert pour de futurs travaux de réparation, amélioration ou entretien. Le renvoi définit le syndicat bénéficiaire sans condition d'immatriculation ou de carence SRU supplémentaire.")

record('L732-2', None,
       "Maintien nécessaire de l'encadrement de durée et des objets financés pour l'emprunt collectif du III de l'article 26-4 de la loi de 1965. La règle réglementaire lue est un plafond de trois cents mois, non une durée minimale d'attente ou un agrément : l'effacer exposerait les copropriétaires engagés collectivement à un endettement plus long sans garantie équivalente. L'éligibilité aux travaux financés par l'éco-prêt à taux zéro est conservée.",
       "R732-1 lu en entier : la durée ne peut excéder trois cents mois ; aucun chiffre de durée fixe ou minimum n'est substitué à ce maximum. Le renvoi à 244 quater U concerne les travaux éligibles à l'avance sans intérêt consentie au syndicat, non une suppression de cet avantage par l'IS à la distribution. Article 26-4 III de la loi de 1965 et conditions détaillées du crédit fiscal/éco-prêt restent des textes distincts ; leur intégralité n'est pas fournie dans ce lot et aucun contenu supplémentaire n'est inventé.",
       "Aucune réduction nouvelle : conservation d'une limite de durée protectrice d'un prêt collectif et de son champ de travaux, dont l'articulation avec l'avance sans intérêt.",
       "Les conditions détaillées d'engagement de chaque copropriétaire et de l'éco-prêt restent à leur texte propre ; aucune baisse de taux ou garantie publique nouvelle n'est déduite de cet article.",
       "Aucune charge nouvelle identifiée : aucun minimum de durée, justificatif ou agrément n'est ajouté ; le plafond existant et la finalité des fonds restent inchangés.",
       benefit="Le financement du reliquat de travaux après mobilisation des fonds du syndicat et celui des travaux éligibles à l'avance sans intérêt restent possibles pour les opérations futures. Le plafond de trois cents mois ne devient pas une durée imposée et aucune exclusivité de produit bancaire n'est créée.")

record('L732-3', None,
       "Maintien intégral de la facilité de remboursement anticipé tenant aux subventions publiques et aux quotes-parts des copropriétaires ne souhaitant pas bénéficier du prêt. Elle réduit le risque de payer durablement des intérêts sur des montants couverts ultérieurement ; son retrait serait défavorable, sans supprimer la dette ou une formalité redondante.",
       "La facilité accompagne les prêts définis par L732-1/2. Elle ne garantit pas la subvention, n'impose pas à un copropriétaire d'emprunter et ne doit pas être limitée aux contrats antérieurs. L'article n'institue ni un agrément ni un prélèvement ; aucune gratuité générale des intérêts ou pénalités non décidée n'est inventée.",
       "Aucun gain nouveau : la protection de remboursement anticipé est conservée pour les prêts futurs et les droits existants, sans restriction du fait générateur favorable.",
       "Le texte ne chiffre pas les frais bancaires ni toutes les modalités de remboursement ; leur coût n'est pas présumé nul par le maintien de cette facilité.",
       "Aucune charge nouvelle identifiée : maintien complet de la facilité source, sans demande ou condition documentaire ajoutée.",
       benefit="Chaque avantage possible du texte est conservé : prise en compte des subventions après financement et des versements de copropriétaires qui ne prennent pas part au prêt. Le bénéfice demeure ouvert aux futurs prêts et ne dépend pas de la seule antériorité d'une convention.")

record('L733-1', None,
       "Maintien intégral de la règle de sécurité sur le remisage d'engins motorisés dans les espaces communs, caves et sous-sols. La dérogation pour les espaces spécialement aménagés permet le remisage adapté ; supprimer la règle entière retirerait une protection de sécurité collective, tandis que supprimer la dérogation augmenterait la contrainte.",
       "Source en vigueur depuis le 20 août 2026, sans note jointe : cette date n'est pas présentée comme la promulgation de la réforme proposée. La règle vise le remisage, non tout passage d'un engin ou toute circulation ; aucun nouvel agrément d'aménagement, liste d'engins ou sanction n'est ajouté. Les limites éventuelles issues du droit de l'accessibilité et les dispositions réglementaires de sécurité ne sont pas effacées implicitement.",
       "Aucune réduction nouvelle : protection des espaces communs et exception d'aménagement sont conservées ensemble sans extension à la circulation des engins.",
       "La définition détaillée des engins et les règles techniques d'aménagement ne sont pas précisées dans cette source ; aucune portée supplémentaire n'en est déduite.",
       "Aucune charge nouvelle identifiée : le texte source reste entier, sans nouveau dossier, autorisation ou obligation de transformer les locaux.",
       benefit="L'exception pour tout espace spécialement aménagé au remisage est maintenue pour les aménagements futurs comme existants, dans chacun des espaces visés. Aucun agrément préalable ou justification périodique nouveau ne conditionne cette dérogation.")

p = paragraphs('L741-1')
assert len(p) == 11
old_penultimate = p[-2]
first_sentence = old_penultimate.split(' L\'instauration')[0]
assert first_sentence.endswith("l'opération.")
P7411 = ''.join(p[:-2]) + first_sentence + '</p>' + p[-1] + (
    '<p>Aucun rapport relatif à la salubrité et à la sécurité du bien n\'est à joindre à la déclaration d\'intention d\'aliéner sur le seul fondement du présent article pour les déclarations présentées à compter de l\'entrée en vigueur de la loi qui prévoit cette suppression. Il en va de même des rapports non encore produits au titre de déclarations en cours à cette date ; aucune nouvelle déclaration ni remise à zéro des délais n\'en résulte. Toute suspension fondée sur le seul défaut de ce rapport cesse à cette date ; le délai restant pour exercer la préemption est déterminé selon les règles de l\'article L. 213-2 du code de l\'urbanisme. Cette suppression s\'applique également lorsque l\'obligation de joindre le rapport avait été instituée avant cette date.</p>'
    '<p>Les décisions de préemption déjà prises, les conventions et engagements valablement conclus, les rapports déjà réalisés et les droits et recours des propriétaires, acquéreurs et occupants demeurent régis par les dispositions qui leur sont applicables. Les diagnostics et informations exigibles sur un fondement autonome ainsi que les signalements, inspections et pouvoirs de police de salubrité et de sécurité demeurent applicables dans leur champ propre ; aucun rapport de remplacement n\'est exigé au titre du présent article.</p>'
)
record('L741-1', P7411,
       "Réduction de fond : retrait de la faculté de subordonner les ventes dans le périmètre à un rapport administratif de salubrité et de sécurité joint à la déclaration de préemption, et de la démarche pour obtenir ce rapport. La sécurité relève toujours des diagnostics et polices autonomes, notamment du signalement suivi d'inspection de L741-2. Les six catégories d'actions, la convention, le droit de préemption facultatif et les pouvoirs de relogement sont intégralement maintenus.",
       "L211-4 et L213-2 urbanisme lus : supprimer dans le premier alinéa de L213-2 la seule référence aux informations dues au titre de L741-1, sans toucher L303-2 ni les pièces environnementales ou délais autonomes. Cette coordination extérieure au lot n'est pas réputée réalisée. La cessation d'une suspension exclusivement fondée sur le rapport conserve les règles de durée restante de L213-2, y compris sa borne d'un mois lorsqu'elle s'applique ; aucun nouveau délai intégral n'est ouvert. L741-2 est rédigé conjointement pour ne plus exiger le rapport et l'instauration préalable de la préemption renforcée ; son ancien renvoi relatif à l'avant-dernier alinéa est retiré avant l'ajout des transitions finales. Les onze alinéas initiaux restent dans leur ordre. Le renvoi aux troisième et avant-dernier alinéas de L521-3-3 vise le maire et le président d'EPCI dans sa version à cinq alinéas, lue entière ; il ne vise pas la carence SRU. La faculté de l'article 25-1 A de la loi de 2000 n'est plus nécessaire pour ce rapport supprimé ; son régime autonome n'est pas abrogé. Aucune source sru_context ni pièce compagnon n'est jointe à ce lot ; l'examen des 209 articles SRU n'est pas déclaré achevé.",
       "Retrait d'une pièce administrative susceptible d'être exigée du vendeur et de la démarche de réalisation associée, sans nouvelle déclaration de substitution. Les inspections de sécurité et les garanties de relogement demeurent.",
       "Le retrait ne concerne que le rapport institué sur L741-1 : déclaration de préemption, diagnostics autonomes et rapports de police restent possibles ou obligatoires dans leur champ. Leur coût total n'est pas chiffré.",
       "Aucune charge nouvelle identifiée : aucune attestation, pièce ou signalement ne remplace le rapport de vente supprimé ; les personnes publiques n'ont pas à produire un rapport équivalent pour chaque vente.",
       effects=[effect('obligation_removed', 'orcod-vente-fin-rapport-salubrite',
                       "Suppression du rapport administratif spécial joint à la déclaration de préemption dans les ORCOD.",
                       "L'instauration de la préemption renforcée pouvait s'accompagner d'un rapport de salubrité-sécurité à joindre selon L213-2, obligeant le vendeur à en obtenir la réalisation.",
                       "Aucun rapport à joindre sur ce fondement, y compris au titre d'une ancienne délibération ou d'une déclaration en cours dont le rapport n'est pas encore produit ; aucun rapport de substitution.",
                       'legal_duty', "Vendeurs de biens dans les opérations de requalification des copropriétés dégradées, autorités établissant le rapport et instructeurs de la préemption.",
                       "Déclarations nouvelles et rapports non produits des procédures en cours ; pas de nouveau dépôt ni remise à zéro ; suspension pour le seul rapport levée selon la durée restante de L213-2 ; préemptions décidées et autres droits antérieurs protégés.",
                       "Diagnostics, informations autonomes, inspections de police et obligations de relogement maintenus sans nouvelle collecte générale.",
                       "L'instauration du droit de préemption urbain renforcé peut être assortie de l'obligation de joindre un rapport relatif à la salubrité et à la sécurité du bien établi par les autorités compétentes et transmis selon les modalités prévues à l'article L. 213-2 dudit code.",
                       "Aucun rapport relatif à la salubrité et à la sécurité du bien n'est à joindre à la déclaration d'intention d'aliéner sur le seul fondement du présent article pour les déclarations présentées à compter de l'entrée en vigueur de la loi qui prévoit cette suppression.")],
       removed=["Faculté d'imposer au vendeur dans le périmètre ORCOD un rapport administratif de salubrité et de sécurité joint à la déclaration d'intention d'aliéner.",
                "Démarche spéciale pour obtenir la réalisation de ce rapport sur le fondement de l'article 25-1 A de la loi du 12 avril 2000, devenue sans objet pour ce seul rapport."],
       benefit="Les opérations futures conservent les aides et interventions immobilières, l'accompagnement et le relogement des occupants ainsi que la possibilité d'inclure des monopropriétés. Le vendeur est dispensé du rapport spécial ; les garanties de santé et de sécurité demeurent exercées sur leurs fondements autonomes, sans fermer une aide pour défaut de rapport.")

p = paragraphs('L741-2')
old0 = p[0]
condition = ", et si le droit de préemption urbain renforcé assorti de l'obligation mentionnée à l'avant-dernier alinéa de l'article L. 741-1  du présent code a été instauré et que la commune s'est engagée formellement à le déléguer à l'opérateur chargé de la mise en œuvre de l'opération d'intérêt national"
assert condition in old0
new0 = old0.replace(condition, '').replace("après avis du représentant de l'Etat dans la région et après consultation", 'après consultation')
P7412 = new0 + ''.join(p[1:]) + (
    '<p>Pour la déclaration d\'intérêt national, l\'instauration du droit de préemption urbain renforcé et l\'engagement de la commune de le déléguer à l\'opérateur ne sont pas exigés. L\'avis du représentant de l\'Etat dans la région n\'est pas une formalité préalable obligatoire. Aucun rapport relatif à la salubrité et à la sécurité d\'un bien joint à une déclaration d\'intention d\'aliéner n\'est requis comme condition de cette déclaration d\'intérêt national.</p>'
    '<p>Ces dispositions s\'appliquent aux déclarations d\'intérêt national prononcées à compter de l\'entrée en vigueur de la loi qui les prévoit, y compris aux procédures en cours sans nouveau dépôt ni recommencement des consultations et de leurs délais. Les opérations déjà déclarées d\'intérêt national, leurs conventions, aides et engagements valablement conclus restent applicables, sans que le maintien de cette qualification soit subordonné au rapport, à l\'instauration du droit de préemption ou à l\'engagement de délégation supprimés. Les droits de préemption et délégations déjà régulièrement établis, les décisions d\'acquisition et les droits et recours des tiers ne sont pas annulés du seul fait de cette suppression.</p>'
)
record('L741-2', P7412,
       "Réduction de fond : l'accès à la qualification d'intérêt national n'est plus subordonné à l'instauration de la préemption renforcée, à sa délégation promise par la commune ni au rapport spécial de vente ; l'avis interne préalable du préfet de région est supprimé. La coordination du seul rapport ne constitue pas une seconde pièce supprimée après L741-1. Sont conservés les enjeux majeurs, la complexité et les lourds investissements, le décret en Conseil d'Etat, les consultations locales et leur délai favorable, le relogement, l'inspection sous un mois après signalement et la conduite de l'opération.",
       "L102-12 urbanisme maintient sa consultation des collectivités ; sa lecture ne justifie pas de supprimer les avis locaux ou leur délai maximal de trois mois avec silence favorable. L321-1-1, lu entier, organise la conduite et la coordination des actions des 1°/4°/5°/6° de L741-1 : renvoi final conservé. Le deuxième alinéa de L741-2 vise bien les troisième et quatrième alinéas de L521-3-3 pour les collectivités, et L441-2-3 pour le préfet, lus ; aucune carence ou imputation SRU ne doit renaître de ce dernier renvoi général. Le nettoyage nécessaire de L441-2-3 de sa phrase de carence relève de son lot, non d'une suppression du DALO ici. La suppression du prérequis de préemption ne ferme pas la faculté de l'instituer sur L741-1 et ne défait pas une acquisition. L213-2 reste à coordonner pour le rapport supprimé.",
       "Retrait de prérequis coercitifs à une opération nationale et d'un avis administratif préalable distinct ; l'aide à la requalification et les pouvoirs de relogement restent ouverts aux opérations futures éligibles.",
       "La qualification reste conditionnée à des enjeux majeurs, une complexité et de lourds investissements, au décret et aux consultations locales. Aucun raccourcissement du délai de consultation ni des contrôles de sécurité n'est annoncé.",
       "Aucune charge nouvelle identifiée : aucun engagement, déclaration ou visa ne remplace les prérequis et l'avis retirés. Les procédures en cours conservent leurs consultations déjà engagées et leurs délais.",
       effects=[effect('obligation_removed', 'orcod-in-acces-sans-preemption-imposee',
                       "Suppression des prérequis de préemption renforcée et d'engagement formel de délégation pour accéder à l'intérêt national.",
                       "La commune devait avoir instauré la préemption renforcée assortie du rapport et promis formellement sa délégation à l'opérateur pour que l'opération soit déclarée d'intérêt national.",
                       "La préemption renforcée et la promesse de délégation ne sont plus exigées pour la qualification ; enjeux, décret, consultations, relogement et inspections subsistent.",
                       'legal_duty', "Communes, opérateurs et personnes publiques participant aux ORCOD susceptibles d'être déclarées d'intérêt national.",
                       "Déclarations nouvelles et dossiers en cours sans reprise des délais ; qualifications et aides anciennes conservées ; préemptions et délégations existantes non annulées.",
                       "Aucun engagement équivalent ni formalité nouvelle ; préemption volontaire dans le régime légal conservée.",
                       "et si le droit de préemption urbain renforcé assorti de l'obligation mentionnée à l'avant-dernier alinéa de l'article L. 741-1  du présent code a été instauré et que la commune s'est engagée formellement à le déléguer à l'opérateur chargé de la mise en œuvre de l'opération d'intérêt national.",
                       "Pour la déclaration d'intérêt national, l'instauration du droit de préemption urbain renforcé et l'engagement de la commune de le déléguer à l'opérateur ne sont pas exigés."),
                effect('obligation_removed', 'orcod-in-fin-avis-prefet-region',
                       "Suppression de l'avis préalable obligatoire du représentant de l'Etat dans la région.",
                       "Le décret en Conseil d'Etat exigeait un avis préalable du préfet de région, distinct des consultations des collectivités.",
                       "Cet avis n'est plus une formalité préalable obligatoire ; toutes les consultations des collectivités et le décret demeurent.",
                       'legal_duty', "Etat et services préparant le décret de qualification de l'ORCOD d'intérêt national.",
                       "Déclarations à compter de l'entrée en vigueur, dossiers en cours inclus, sans nouveau dépôt ni remise à zéro.",
                       "Aucun visa, avis conforme ou déclaration équivalente n'est créé.",
                       "Le décret en Conseil d'Etat est pris après avis du représentant de l'Etat dans la région et après consultation de l'établissement public de coopération intercommunale",
                       "L'avis du représentant de l'Etat dans la région n'est pas une formalité préalable obligatoire."),
                effect('coordination', 'orcod-vente-fin-rapport-salubrite',
                       "Coordination de la suppression du rapport spécial de vente décidée à L741-1, sans compter une seconde pièce supprimée.",
                       "L741-2 exigeait une préemption renforcée assortie de l'obligation de rapport de L741-1 comme prérequis de la qualification.",
                       "L741-2 ne peut plus exiger ce rapport pour la qualification d'intérêt national.",
                       'legal_duty', "Personnes publiques et opérateurs préparant la qualification nationale des ORCOD.",
                       "Qualification future et procédures en cours ; ancienne qualification préservée sans maintien du prérequis.",
                       "Aucun rapport ou attestation équivalent en remplacement.",
                       "le droit de préemption urbain renforcé assorti de l'obligation mentionnée à l'avant-dernier alinéa de l'article L. 741-1  du présent code",
                       "Aucun rapport relatif à la salubrité et à la sécurité d'un bien joint à une déclaration d'intention d'aliéner n'est requis comme condition de cette déclaration d'intérêt national.")],
       removed=["Prérequis d'instauration du droit de préemption urbain renforcé et d'engagement formel de la commune à le déléguer à l'opérateur de l'ORCOD d'intérêt national.",
                "Prérequis du rapport de salubrité-sécurité de L741-1, coordination de sa suppression sans seconde pièce ou seconde réduction comptée.",
                "Avis préalable obligatoire du représentant de l'Etat dans la région avant le décret déclarant l'opération d'intérêt national, sans avis de remplacement."],
       benefit="La qualification nationale et les aides, interventions et pouvoirs de relogement qui l'accompagnent restent disponibles pour les nouvelles opérations satisfaisant aux critères de gravité. Le silence favorable après trois mois est conservé. Les opérations, conventions, aides et engagements acquis ne perdent pas leur qualification du fait du retrait des prérequis.")

record('L741-3', None,
       "Maintien intégral d'une procédure judiciaire nécessaire pour diviser une copropriété gravement empêchée : expertise financée par l'opérateur, délai de trois mois renouvelable une fois, notifications, état des dettes, autonomie des volumes, autorisation des travaux, indemnisation des copropriétaires lésés et contrôle du juge. Les supprimer porterait sur les droits patrimoniaux et le contradictoire, sans retirer un prélèvement ou un doublon administratif démontré.",
       "I à VI et leurs alinéas relus : les pièces du II servent l'expertise ; le V et l'avant-dernier alinéa du VI renvoient à l'expropriation, non au licenciement. Le plafond de six mois de salaire, le seuil d'un an et le préavis de quinze jours du contrat unique sont donc inapplicables. Les 1°/2° du II de l'article 28 de la loi de 1965 règlent la répartition des créances et dettes ; ce texte externe n'est pas inventé ni réputé réécrit. Les renvois L741-1/2 demeurent cohérents : la suppression du rapport de vente et des prérequis de qualification ne supprime ni l'opération ni l'accès au juge. La dissolution ne fait disparaître ni indemnisation ni passif réparti.",
       "Aucune réduction nouvelle : la procédure protège les propriétaires et créanciers contre les conséquences d'une division judiciaire sans expertise, notification, répartition ou indemnité.",
       "Les frais de l'opérateur, délais d'expertise et compétences du juge sont maintenus ; la loi de 1965 et le code de l'expropriation ne sont pas réécrits dans ce lot.",
       "Aucune charge nouvelle identifiée : maintien de toutes les garanties, conditions, notifications et durées de la source, sans régime nouveau de preuve ou de travail.",
       benefit="L'expertise reste aux frais de l'opérateur ; l'offre d'indemnité des copropriétaires lésés et sa fixation judiciaire en cas de désaccord demeurent intégrales pour les futures divisions. La conservation de ces indemnités spéciales immobilières ne dépend d'aucune ancienneté d'emploi et n'est soumise à aucun plafond salarial.")

record('L741-4', None,
       "Maintien intégral de la voie judiciaire de distraction d'un immeuble ou de dissolution d'une association syndicale libre lorsque sa structure compromet l'ORCOD. Expertise, information des membres, seuil majoritaire pour envisager la dissolution, décision du juge, dévolution de l'actif et du passif, dettes des membres et prise en charge des frais de distraction par l'opérateur assurent les droits de propriété et des tiers ; aucun doublon à retirer n'est démontré.",
       "Le I subordonne la dissolution étudiée à une opération portant sur une part majoritaire du périmètre ; la distraction d'un immeuble ne doit pas être confondue avec cette hypothèse. Le III vise littéralement les « statuts du syndicat » dans un article consacré à l'association syndicale libre : terminologie source signalée, non corrigée silencieusement en nouvelle règle de dévolution. « Ce rapport » au I désigne le rapport de l'expert dont l'établissement n'est pas détaillé ; aucun délai ou destinataire additionnel n'est inventé. Ordonnance 2004-632 et urbanisme livre III/titre II/chapitre II restent des régimes extérieurs distincts de l'emploi. Les réformes de L741-1/2 ne rendent pas orphelin le renvoi aux opérations.",
       "Aucun allègement nouveau : maintien d'une faculté de traitement judiciaire des difficultés et des protections qui l'encadrent, avec frais de modification en cas de distraction à la charge de l'opérateur.",
       "Le régime extérieur des associations syndicales et la terminologie préexistante du III appellent contrôle dans leur champ ; aucune extinction de dette ou liquidation forcée nouvelle n'est décidée.",
       "Aucune charge nouvelle identifiée : maintien intégral des quatre subdivisions et de leurs conditions, sans ajouter de dossier ni étendre la responsabilité des propriétaires.",
       benefit="La possibilité de distraction ou de dissolution judiciaire reste ouverte aux futures ORCOD éligibles. Les frais de modification des statuts et actes de distraction restent à la charge de l'opérateur ; droits des tiers et modalités statutaires de dévolution ne sont pas supprimés sous prétexte d'allègement.")

record('L811-1', None,
       "Maintien intégral de l'affectation du financement des aides personnelles au logement et des primes de déménagement au FNAL. L'article n'établit pas lui-même une taxe, une cotisation ou un dossier ; le supprimer fragiliserait le fondement des prestations sans démontrer de baisse de prélèvement.",
       "L821-1 lu : aide personnalisée au logement, allocation de logement familiale, allocation de logement sociale et primes de déménagement pour conditions plus adaptées. Aucun montant, critère de ressources ou droit futur n'est réduit. Les ressources contributives du fonds relèvent d'autres dispositions : la suppression de la taxe sur les salaires n'abolit pas ici les contributions autonomes de logement et un changement de financeur ne serait pas une baisse de prélèvement démontrée.",
       "Aucun gain nouveau : la base de financement des aides et primes est préservée, sans nouveau transfert ni recette de compensation inventée.",
       "Le rendement des ressources du FNAL et le solde public de l'ensemble des réformes ne sont pas chiffrés ; les articles de ressources ne sont pas assignés à ce lot.",
       "Aucune charge nouvelle identifiée : maintien exact de l'affectation existante, sans nouveau taux, assiette, déclaration ou condition de prestation.",
       benefit="Toutes les catégories d'aides personnelles de L821-1 et les primes de déménagement gardent leur fondement de financement au FNAL, pour les bénéficiaires futurs comme actuels. Aucun avantage n'est fermé faute de financement de remplacement inventé dans cet article.")

record('L811-2', None,
       "Maintien intégral de la gouvernance du FNAL : un conseil de gestion et une habilitation à définir sa composition, la désignation et le fonctionnement. Un organe responsable d'un fonds de prestations a une fonction essentielle d'administration et de contrôle des fonds ; ce texte ne prescrit pas aux bénéficiaires un agrément, un rapport annuel ou une déclaration supplémentaire.",
       "L811-1 conserve le financement des aides par le fonds. Le renvoi réglementaire porte seulement sur sa gouvernance, non sur l'instauration d'une contribution ou d'une condition d'ouverture des aides. Les règles réglementaires du conseil ne sont pas assignées ici et leur éventuelle simplification ne peut être affirmée à partir de cette seule habilitation.",
       "Aucune réduction nouvelle : maintien d'une administration identifiable du fonds, sans prétendre qu'une suppression de conseil aurait chiffré l'économie de ses frais ou sécurisé autrement les prestations.",
       "La composition et les modalités effectives du conseil relèvent de dispositions non reproduites dans ce lot ; aucun audit de leurs coûts n'est déclaré réalisé.",
       "Aucune charge nouvelle identifiée : aucune exigence documentaire, réunion ou donnée supplémentaire n'est ajoutée au texte légal source.",
       benefit="La gouvernance conservée ne modifie aucun droit à l'aide ni aux primes de déménagement, présentes ou futures. Aucune nouvelle condition de demande ou d'accès au fonds n'est introduite par l'habilitation réglementaire maintenue.")


def reference_checks():
    assessments = {
        'L662-1': {
            'L1234-1': "L1234-1 vise le préavis du licenciement salarié, avec les seuils de six mois et deux ans dans la source et quinze jours pour les nouveaux contrats dans la proposition. L662-1 étend des règles de ventes d'immeubles et d'interdiction professionnelle, non un licenciement : aucune ancienneté ni notification de rupture d'emploi ne s'y applique.",
            'L1221-2': "L1221-2 proposé interdit un terme automatique pour les futurs contrats de travail et préserve les anciens contrats. Une vente à terme ou une VEFA de L261-9 à L261-16 est un contrat immobilier, non un CDD : son terme de livraison, son dépôt et ses garanties ne sont pas abolis par le contrat unique, ni assimilés à une durée d'emploi.",
            'L1234-9': "L1234-9 proposé concerne l'indemnité ordinaire patronale, seuil d'un an apprécié au terme effectif avec préavis, 0,20 mois sur toute l'ancienneté et mois complets, plafond six mois, avec droits anciens et spéciaux préservés. L'indemnité de résolution d'une vente de L261-14 ne relève pas de ce barème ; aucune de ses garanties futures n'est fermée par ce renvoi territorial.",
            'L261-12': "L261-12 interdit les versements VEFA avant contrat ou exigibilité et protège les dépôts de vente à terme sur compte spécial incessible, insaisissable et indisponible sauf prix. L662-1 étend cet article sans exception. La proposition cible conserve cette protection : aucun préavis de salarié, seuil d'ancienneté ni plafond d'indemnité d'emploi n'est applicable à ces fonds.",
            'L261-14': "L261-14 plafonne l'indemnité forfaitaire de résolution immobilière à 10 % du prix tout en permettant la réparation du dommage effectif. L662-1 l'étend sans exception ; la proposition cible conserve les deux éléments. Ce pourcentage du prix n'est pas l'indemnité salariale de L1234-9 et reste valable pour les futures ventes éligibles, sans seuil d'un an ni notification de licenciement.",
        },
        'L741-3': {
            'L1234-1': "Le délai de trois mois renouvelable une fois du III de L741-3 encadre l'expert judiciaire ; les notifications portent sur son rapport et l'offre d'indemnité, pas sur un licenciement. Les seuils de services et le préavis de L1234-1, y compris les quinze jours de la proposition pour nouveaux contrats, sont inapplicables ; les garanties immobilières ne sont pas raccourcies.",
            'L1221-2': "La division du syndicat de copropriétaires et sa dissolution au prononcé du juge sont des opérations immobilières, non la fin d'un emploi. L1221-2 proposé ne leur retire ni terme judiciaire ni effets patrimoniaux et ne crée aucun CDD spécial. Aucune nouvelle règle de contrat privé ou de durée de mission de l'expert n'est tirée de ce rapprochement.",
            'L1234-9': "Le V et le VI de L741-3 renvoient aux règles d'expropriation pour indemniser un partage inégal et fixer le désaccord, sans ancienneté de salarié. Le seuil d'un an à fin effective avec préavis inclus et le calcul de 0,20 mois par année totale au prorata des mois complets, plafond six mois de L1234-9 proposé, ne s'appliquent donc pas. L'expertise aux frais de l'opérateur et l'indemnisation immobilière future restent entières.",
        },
    }
    for number, obj in RESULTS.items():
        key = obj['code_id'] + '|' + obj['source_id']
        checks = []
        for target_key in REFS['requirements'][key]:
            target = REFS['targets'][target_key]
            checks.append(dict(target_key=target_key, view_sha256=target['view_sha256'],
                               assessment=assessments[number][target['number']]))
        obj['reference_checks'] = checks


# Les citations couvrent des phrases ou subdivisions entières, sans points de suspension.
source_text = plain(BY_NUMBER['L711-2']['source_xml'])
RESULTS['L711-2']['substantive_impact']['effects'][0]['source_quote'] = source_text[
    source_text.index('III. ―'):source_text.index('4° D\'informer')
].strip()
RESULTS['L731-5']['substantive_impact']['effects'][0]['source_quote'] = plain(paragraphs('L731-5')[0])
source_text = plain(BY_NUMBER['L741-2']['source_xml'])
first_sentence = source_text.strip().split('. Le décret')[0] + '.'
regional_sentence = re.search(r"Le décret en Conseil d'Etat est pris .*?concernés\.", source_text).group(0)
RESULTS['L741-2']['substantive_impact']['effects'][0]['source_quote'] = first_sentence
RESULTS['L741-2']['substantive_impact']['effects'][1]['source_quote'] = regional_sentence
RESULTS['L741-2']['substantive_impact']['effects'][2]['source_quote'] = first_sentence
RESULTS['L662-1']['review_notes'] += " Les renvois directs nouveaux à L241-7 et L214-6 à L214-9 ne figurent pas parmi les cibles fournies dans reference-targets.json : leurs textes officiels ont été lus dans le corpus public autorisé, sans ajouter de cible à reference_checks."
RESULTS['L711-5']['review_notes'] += " Le renvoi direct nouveau à L711-4 n'est pas une cible fournie dans reference-targets.json ; cet article est une source assignée lue intégralement et maintenue dans ce lot."

# Une seule entrée pour la même mesure et le même type d'effet dans un article.
# Le bilan commun conserve les deux suppressions et leurs preuves intégrales.
notarial_effects = RESULTS['L711-5']['substantive_impact']['effects']
assert len(notarial_effects) == 2
assert len({(e['measure_id'], e['kind']) for e in notarial_effects}) == 1
merged = notarial_effects[0].copy()
merged.update(
    description="Suppression des formalités notariales propres au registre à la vente : immatriculation d'office, imputation de ses frais et signalement obligatoire de toute erreur.",
    before="En l'absence de syndic ou après un mois de mise en demeure infructueuse, le notaire devait immatriculer d'office ; les frais incombaient au syndic ou au syndicat si le syndic n'était pas rémunéré. Il devait aussi signaler toute erreur constatée au registre.",
    after="La vente n'impose plus l'immatriculation d'office ni ses frais ; le numéro est mentionné s'il existe et le signalement d'erreur devient facultatif. L'immatriculation normale de L711-4 et les devoirs autonomes d'information et de conseil restent applicables.",
    affected_population="Notaires intervenant dans les ventes de lots de copropriété ; syndics et syndicats auxquels les frais d'immatriculation d'office étaient imputés.",
    replacement_or_new_burdens="Aucune attestation négative, déclaration de substitution ou tenue d'un registre d'erreurs n'est créée ; les devoirs autonomes de conseil et l'immatriculation normale subsistent.",
)
notarial_source = plain(BY_NUMBER['L711-5']['source_xml'])
merged['source_quote'] = notarial_source[notarial_source.index("En l'absence de syndic désigné"):].strip()
notarial_proposal = plain(P7115)
quote_start = notarial_proposal.index("L'absence d'immatriculation")
quote_end_text = "Le notaire peut informer l'établissement public chargé de la tenue du registre de toute erreur qu'il y constate."
quote_end = notarial_proposal.index(quote_end_text) + len(quote_end_text)
merged['proposed_quote'] = notarial_proposal[quote_start:quote_end]
RESULTS['L711-5']['substantive_impact']['effects'] = [merged]

RESULTS['L711-3']['review_notes'] += " Discordance préexistante à coordonner dans le règlement : L711-3 ouvre aux notaires l'ensemble des données, alors que R711-16 I ne vise que le 1° du II de L711-2 ; le maintien de la loi ne présente pas cette restriction réglementaire comme cohérente ni comme une nouvelle dispense."
RESULTS['L711-2']['review_notes'] += " Autre discordance préexistante : le IV rend publiques les informations du II, tandis que R711-17 ne vise que le 1° et en exclut le nom du syndic et le nombre de lots. La coordination réglementaire doit traiter cette différence, sans étendre silencieusement la publicité ni ajouter une collecte."
reference_checks()
answer = [RESULTS[s['number']] for s in SOURCES]
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'{len(answer)} articles écrits dans answer.json')
