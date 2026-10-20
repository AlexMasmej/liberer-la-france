import json
import re
import html
from pathlib import Path

ROOT = Path(__file__).parent
SOURCES = json.loads((ROOT / 'source.json').read_text())
REFS = json.loads((ROOT / 'reference-targets.json').read_text())
BY_NUMBER = {s['number']: s for s in SOURCES}
OUT = {}


def plain(xml):
    return html.unescape(re.sub(r'<[^>]+>', '', xml))


def paras(*items):
    return ''.join('<p>' + html.escape(p, quote=False) + '</p>' for p in items)


def impact(classification, assessment, limits, burdens, effects=None):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=limits, new_burdens_review=burdens, effects=effects or [])


def retained(number, reason, notes, assessment, limits, burdens, benefit=None):
    s = BY_NUMBER[number]
    o = {k: s[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    o.update(proposed_xml=None, reason=reason, review_notes=notes,
             status='retained_unchanged', classification='retained_necessary',
             substantive_impact=impact('retained_necessary', assessment, limits, burdens))
    if benefit:
        o['benefit_review'] = benefit
    OUT[number] = o


def rewritten(number, xml, reason, notes, assessment, limits, burdens, removed=None,
              repeal=None, classification='material_reduction', benefit=None):
    s = BY_NUMBER[number]
    o = {k: s[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    o.update(proposed_xml=xml, reason=reason, review_notes=notes, status='rewrite_draft',
             substantive_impact=impact(classification, assessment, limits, burdens))
    if repeal:
        o.update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19', repeal_scope=repeal)
    if removed:
        o.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19', removed_provisions=removed)
    if benefit:
        o['benefit_review'] = benefit
    OUT[number] = o


def effect(number, kind, measure, description, before, after, unit, people, transition,
           burdens, source_quote, proposed_quote):
    assert source_quote in plain(BY_NUMBER[number]['source_xml']), (number, source_quote)
    assert proposed_quote in plain(OUT[number]['proposed_xml']), (number, proposed_quote)
    OUT[number]['substantive_impact']['effects'].append(dict(
        kind=kind, measure_id=measure, description=description, before=before, after=after,
        unit=unit, affected_population=people, conditions_and_transition=transition,
        replacement_or_new_burdens=burdens, source_quote=source_quote, proposed_quote=proposed_quote))


retained('L583-1',
    "Maintien intégral utile : l'information sur les droits et l'assistance aux demandes évitent le non-recours. Le concours pour les dossiers d'autres régimes reste facultatif ; aucune formalité à la charge de l'allocataire n'est créée ni aucun prélèvement fixé. Retirer ces missions supprimerait une protection, sans alléger une démarche identifiée.",
    "Les 1° et 2° et le concours aux allocataires en fin de droit sont conservés. La note renvoie historiquement à L843-1 pour les aides de garde : cette note documentaire n'est pas une disposition nouvelle et ne modifie pas le champ normatif de l'article.",
    "L'article entier est maintenu : service, information et aide à la demande, sans réforme stylistique ni réduction revendiquée.",
    "Aucun coût de gestion ni effet sur le non-recours n'est mesuré ; les conditions des prestations et des autres régimes ne sont pas réécrites ici.",
    "Aucune charge nouvelle n'est identifiée : les deux missions obligatoires et la faculté d'accompagnement restent celles de la source.")

retained('L583-2',
    "Maintien intégral de la faculté d'avance : elle permet un paiement anticipé lorsque la demande établit les droits sans ambiguïté, avec remboursement interne aux fonds dans leur limite. Ce garde-fou évite une avance sans droit établi ; aucune autorisation ou pièce supplémentaire n'est prescrite.",
    "Conserver le financement par l'action sanitaire et sociale, le remboursement par les fonds des prestations légales et la limite des droits établis. La faculté existe déjà ; ce maintien n'est pas un nouveau report de paiement ni une extension de prestation.",
    "La faculté favorable d'avance et son plafond juridique sont conservés pour les demandes futures également ; aucun gain nouveau n'est compté.",
    "Ni automatisation du versement, ni financement supplémentaire, ni montant d'avance ne sont décidés par cet article.",
    "Aucune charge nouvelle n'est identifiée : la condition permettant d'apprécier sans ambiguïté la demande et les fonds financeurs sont inchangés.")

retained('L583-3',
    "Maintien intégral après examen : l'article privilégie déjà les échanges légaux d'informations et ne demande une déclaration qu'en leur absence. Il limite les données au strict nécessaire, protège le secret et organise un contrôle utile contre la fraude. Répéter le droit au réemploi des données ne constituerait pas une suppression supplémentaire.",
    "Les dix alinéas, L114-14, L114-17 et le champ de l'intermédiation L582-2/L523-1 sont conservés. L114-17 a été lu dans le corpus : il réserve déjà la bonne foi pour les déclarations inexactes ou incomplètes ; aucune nouvelle dispense de sanction n'est donc revendiquée. Le a du 2° de L821-1 vise le CCH, non l'AAH du CSS malgré l'homonymie de la cible fournie. Suspension pour refus de contrôle et garanties d'information demeurent distinctes d'un préavis de rupture d'emploi.",
    "Pas de changement de fond : échanges existants, déclaration subsidiaire, contrôle, minimisation et secret sont nécessaires aux prestations et à l'intermédiation.",
    "L'utilité de chaque demande concrète reste soumise à la stricte nécessité ; aucune économie nouvelle de collecte ni baisse des cotisations n'est démontrée.",
    "Aucune charge nouvelle n'est identifiée : aucun fichier, registre, délai ou justificatif n'est ajouté au circuit déjà prévu par la source.")

retained('L583-4',
    "Maintien intégral de la transmission institutionnelle du montant des indemnités journalières AT-MP. Elle permet l'appréciation des ressources sans imposer cette communication aux allocataires. L'intermédiaire fiscal n'est pas démontré redondant par le dossier ; supprimer ce flux risquerait de recréer une demande individuelle.",
    "Le 2° de L431-1 vise les indemnités d'incapacité temporaire, non une indemnité de rupture du contrat. Les limites tenant à la loi du 6 janvier 1978 sont conservées. Aucune ouverture d'accès supplémentaire aux données fiscales ou de santé.",
    "Le flux maladie–administration fiscale destiné aux organismes familiaux est conservé sans extension ; aucune nouvelle simplification n'est attribuée au maintien.",
    "Une suppression de l'intermédiation nécessiterait la preuve d'un flux direct légal et équivalent, absente de ce lot ; aucun tel flux n'est inventé.",
    "Aucune charge nouvelle n'est identifiée : seules les données et les personnes déjà visées par la transmission restent concernées.")

retained('L583-5',
    "Maintien de la communication du montant de pension fixé par un accord auquel la caisse a donné force exécutoire. Elle concourt à la cohérence des ressources fiscales et sociales sans déclaration supplémentaire du parent ; elle n'est pas un agrément ni une taxe accessoire.",
    "Le renvoi à L582-2 demeure limité à l'accord rendu exécutoire. L'article ne soumet pas les parents à une nouvelle démarche et n'autorise pas la transmission d'autres données de l'accord.",
    "La seule communication institutionnelle du montant de contribution reste inchangée ; aucun prélèvement supprimé ou gain de procédure nouveau.",
    "Les règles civiles de contribution et la fiscalité des pensions ne sont pas modifiées ; l'absence d'un doublon technique n'est pas chiffrée.",
    "Aucune charge nouvelle n'est identifiée : pas de nouveau destinataire, de registre ou d'information à fournir par les parents.")

retained('L584-1',
    "Maintien de l'habilitation réglementaire générale du livre V, nécessaire à l'exécution des prestations. Elle ne fixe elle-même ni déclaration, ni agrément, ni prélèvement et réserve expressément les taux ainsi que le chapitre 2 du titre IV. Son abrogation n'établirait pas la suppression d'une charge déterminée.",
    "Les deux exclusions de l'habilitation sont intégralement conservées. Les contraintes des décrets d'application doivent être examinées dans leurs articles propres ; cette habilitation ne peut servir à rétablir une obligation supprimée par la loi.",
    "Habilitation utile conservée sans nouveau corps normatif et sans assimiler le maintien à une simplification.",
    "L'ensemble des mesures réglementaires du livre V n'est pas évalué dans ce seul article ; aucun solde de contraintes n'est démontré.",
    "Aucune charge nouvelle n'est identifiée : la compétence réglementaire et ses exceptions restent identiques à celles de la source.")

s = BY_NUMBER['L612-1']['source_xml']
old = "; ces orientations sont soumises pour approbation à l'autorité compétente de l'Etat ;"
assert old in s
xml = s.replace(old, ';', 1) + paras(
    "À compter de l'entrée en vigueur de la loi supprimant l'approbation préalable, les orientations mentionnées au 2° sont applicables sans cette approbation, y compris lorsqu'elles ont été soumises à l'Etat avant cette date et n'ont pas encore été approuvées. Cette suppression ne modifie ni les aides et prestations attribuées, ni les plafonds et règles financières prévus à l'article L. 612-5, ni les contrôles de légalité et financiers ; ces contrôles ne peuvent rétablir une approbation particulière de ces orientations.")
rewritten('L612-1', xml,
    "Réforme de fond ciblée : suppression de l'approbation préalable des orientations d'action sanitaire et sociale. La tutelle financière et les plafonds de L612-5, le contrôle de légalité, la certification des comptes et les missions de service demeurent ; un visa particulier des orientations ajoute un verrou distinct sans fonction essentielle démontrée. Tout le reste du corps source est maintenu, notamment l'audition annuelle sur la qualité du service.",
    "Le 2° seul perd l'approbation ; les 1°, 3°, 4° et les alinéas suivants restent à leur place. Coordonner les décrets et actes de tutelle pour qu'ils n'imposent pas un visa équivalent sous couvert de contrôle. L612-5 et L612-5-1 du lot conservent les règles financières et la certification. Le régime indépendant n'est pas raccordé ici à la capitalisation des salariés privés.",
    "Une approbation préalable est effectivement retirée ; les pouvoirs de contrôle et les droits aux aides ne sont pas supprimés. Pas de baisse de cotisation revendiquée.",
    "Le temps administratif économisé et le coût public ne sont pas chiffrés ; les actes réglementaires d'exécution hors lot restent à coordonner.",
    "Aucune charge nouvelle n'est identifiée : l'approbation disparaît sans déclaration, délai d'attente ou contrôle préalable de remplacement.",
    removed=["Approbation préalable par l'autorité compétente de l'Etat des orientations générales d'action sanitaire et sociale du CPSTI."])
effect('L612-1', 'authorization_removed', 'cpsti-orientations-fin-approbation',
       "Retrait du visa préalable particulier des orientations d'action sanitaire et sociale.",
       "Orientations du 2° soumises à approbation de l'Etat, distincte des plafonds financiers.",
       "Orientations applicables sans cette approbation ; règles financières et contrôle de légalité maintenus.",
       'legal_duty', 'CPSTI et travailleurs indépendants bénéficiaires de son action sanitaire et sociale',
       "Dès l'entrée en vigueur, y compris orientations en attente d'approbation ; aides attribuées protégées.",
       "Aucune déclaration ou autorisation équivalente ; les contrôles subsistants ne peuvent rétablir ce visa.",
       "ces orientations sont soumises pour approbation à l'autorité compétente de l'Etat",
       "les orientations mentionnées au 2° sont applicables sans cette approbation")

# La transition ajoutée dans la cible L231-6-1 rendrait le renvoi ordinal flottant.
s = BY_NUMBER['L612-2']['source_xml']
old = "à l'exception du a du 5° et du dernier alinéa de l'article L. 231-6-1"
new = "à l'exception du a du 5° de l'article L. 231-6-1 et, dans ce même article, de la disposition prévoyant la perte du mandat des personnes dont le remplacement est demandé par l'organisation qui a procédé à leur désignation"
assert old in s
rewritten('L612-2', s.replace(old, new, 1),
    "Coordination nécessaire de fond inchangé : l'exception visant le dernier alinéa de L231-6-1 est désignée par son objet exact, la perte de mandat sur demande de remplacement par l'organisation. La proposition fournie de cette cible ajoute un alinéa transitoire final ; conserver l'ancien ordinal changerait l'exception. La personnalité morale, les organes, les contrôles, l'exception d'âge et les remboursements de mandat sont intégralement maintenus.",
    "Dans la source de L231-6-1, le dernier alinéa est le 2° terminal relatif à la demande de remplacement, et non le 1° qui concerne la cessation d'appartenance à l'organisation. Le renvoi proposé préserve uniquement l'exception réellement visée, ainsi que le a du 5°. Il ne retire aucune autre incompatibilité ni aucun pouvoir de contrôle. L231-12 rembourse le salaire maintenu pour mandat, non l'indemnité de rupture. L224-10/L151-1 ne doivent pas rétablir l'approbation particulière des orientations supprimée à L612-1. Cette coordination accompagne l'intégration de L231-6-1 proposé, sans anticiper sa transition.",
    "Seule la cible de l'exception est stabilisée face à l'ajout d'une transition dans L231-6-1 ; aucune nouvelle exclusion ou réduction de charge n'est créée.",
    "Le gain est exclusivement la cohérence du renvoi. Il dépend de l'intégration de la proposition de L231-6-1, distincte du droit officiel actuel.",
    "Aucune charge nouvelle n'est identifiée : même exception de remplacement et mêmes autres règles de mandat, sans formulaire, donnée ou délai ajouté.",
    classification='coordination_only')
effect('L612-2', 'coordination', 'cpsti-exception-remplacement-mandat',
       "Désignation explicite de l'exception de perte de mandat auparavant visée par le dernier alinéa.",
       "Exception du dernier alinéa de L231-6-1, qui correspond dans la source au remplacement demandé par l'organisation désignatrice.",
       "Même exception désignée par son objet malgré l'ajout d'un nouvel alinéa transitoire à la cible proposée.",
       'legal_duty', "Membres de l'assemblée générale et des instances régionales du CPSTI",
       "Coordination avec la rédaction proposée de L231-6-1 ; aucune cause autonome de perte de mandat ni aucun droit ancien modifiés.",
       "Aucune charge nouvelle ou mesure de remplacement ; il ne s'agit pas d'une seconde suppression d'incompatibilité.",
       "à l'exception du a du 5° et du dernier alinéa de l'article L. 231-6-1",
       "de la disposition prévoyant la perte du mandat des personnes dont le remplacement est demandé par l'organisation qui a procédé à leur désignation")

s = BY_NUMBER['L612-3']['source_xml']
old = " Le médiateur remet chaque année au Conseil de la protection sociale des travailleurs indépendants un rapport sur les activités de médiation des instances régionales de ce conseil. Ce rapport est transmis aux ministres chargés de la sécurité sociale et du budget ainsi qu'au Défenseur des droits."
assert old in s
xml = s.replace(old, '', 1) + paras(
    "À compter de l'entrée en vigueur de la loi supprimant le rapport annuel de médiation, aucun rapport ni transmission ne sont exigibles sur ce seul fondement, même pour une année antérieure. Les rapports déjà établis n'ont pas à être refaits. Les missions du médiateur national et des médiateurs régionaux, le traitement des réclamations, les voies de recours et les pouvoirs légaux du Défenseur des droits demeurent applicables.")
rewritten('L612-3', xml,
    "Réforme de fond : suppression du rapport annuel particulier de médiation et de sa transmission systématique à trois destinataires. La médiation, sa coordination nationale et les compétences du Défenseur des droits sont conservées ; elles ne dépendent pas d'un rapport périodique imposé. La composition, la parité et tous les sièges demeurent intégralement ceux de la source.",
    "Conserver le septième alinéa relatif aux directeurs des caisses : il est visé par l'alinéa suivant. Seules les deux dernières phrases du dernier alinéa source sont retirées. Aucun nouveau rapport regroupé, remontée statistique ou transmission de remplacement. La suppression vaut aussi pour les rapports non encore exigibles relatifs à des années anciennes ; les documents antérieurs et les réclamations individuelles ne sont pas effacés. Incohérence terminologique préexistante signalée : la phrase sur les commissaires du Gouvernement parle de conseil d'administration alors que L612-2 dote le CPSTI d'une assemblée générale ; son libellé n'est pas corrigé silencieusement ici.",
    "Retrait d'un rapport périodique obligatoire et de son circuit de transmission ; un seul dispositif supprimé, sans suppression du service de médiation.",
    "Le coût de rédaction et d'acheminement n'est pas connu ; les demandes légalement autonomes du Défenseur des droits restent possibles.",
    "Aucune charge nouvelle n'est identifiée : aucune statistique, déclaration ou justification nouvelle ne remplace le rapport supprimé.",
    removed=["Rapport annuel obligatoire du médiateur national sur les médiations régionales et transmission systématique aux ministres et au Défenseur des droits."])
effect('L612-3', 'obligation_removed', 'cpsti-fin-rapport-annuel-mediation',
       "Suppression du reporting périodique de médiation et des transmissions liées.",
       "Rapport chaque année au CPSTI, transmis aux ministres de la sécurité sociale et du budget et au Défenseur des droits.",
       "Aucun rapport annuel ni transmission exigibles sur ce fondement ; médiation et recours conservés.",
       'legal_duty', 'Médiateur national et instances régionales du CPSTI',
       "Obligations futures supprimées dès l'entrée en vigueur, y compris pour exercices anciens ; rapports déposés non refaits.",
       "Aucun document périodique de remplacement ; les pouvoirs légaux autonomes sont réservés.",
       "Le médiateur remet chaque année au Conseil de la protection sociale des travailleurs indépendants un rapport sur les activités de médiation des instances régionales de ce conseil.",
       "aucun rapport ni transmission ne sont exigibles sur ce seul fondement, même pour une année antérieure")

retained('L612-4',
    "Maintien intégral : les instances régionales décident des aides, assurent la représentation locale et désignent un médiateur. Le dépôt auprès des organismes locaux donne déjà un circuit commun d'instruction et de paiement ; supprimer la décision sans répartir ses compétences menacerait les aides. La faculté de regroupement territorial évite déjà de figer un organisme par région.",
    "Les cinq alinéas et le quatrième alinéa visé par L216-5 sont conservés. L213-1 I 9° met en œuvre les décisions d'action sociale, sans les transformer en cotisations nouvelles. Le médiateur accompagne un recours social ; il ne modifie ni préavis ni indemnité de rupture des salariés. Les aides restent accessibles aux situations futures éligibles.",
    "Organisation territoriale et circuit d'aide existants maintenus sans nouvelle formalité ni suppression de droit social.",
    "Une fusion supplémentaire de l'instruction et de la décision exigerait une allocation de compétences non établie ; aucun délai d'aide plus court n'est promis.",
    "Aucune charge nouvelle n'est identifiée : composition, ressort, faculté de regroupement et médiation restent ceux de l'article officiel.")

retained('L612-5',
    "Maintien intégral du financement et des plafonds de l'action sociale : la dotation couvre la gestion, l'arrêté encadre les montants après avis du CPSTI et le conseil répartit le plafond régional. Ce contrôle budgétaire est distinct de l'approbation des orientations retirée à L612-1 ; il protège les ressources des régimes sans taxer directement les indépendants.",
    "Les quatre alinéas et les renvois L632-1/L635-1 demeurent. L'entrée en vigueur du 1er janvier 2020 figurant dans la note est historique. La dotation n'est ni un transfert vers la capitalisation des salariés ni une cotisation accessoire supprimée ; aucune ressource de compensation n'est inventée.",
    "Maintien du cadre financier nécessaire aux aides et à la gestion, sans assimiler la dépense plafonnée à un nouveau prélèvement.",
    "Le niveau des dotations et l'adéquation des plafonds aux besoins ne sont pas chiffrés ; les arrêtés budgétaires ne sont pas réécrits ici.",
    "Aucune charge nouvelle n'est identifiée : dotation annuelle, avis, arrêté et répartition existaient déjà dans la source.")

retained('L612-5-1',
    "Maintien intégral du contrôle externe des comptes par la Cour des comptes et de sa transmission au Parlement. La certification des comptes annuels et combinés protège les fonds de retraite et d'invalidité-décès ; elle n'est pas le rapport d'activité de médiation supprimé et aucune certification équivalente redondante n'est identifiée ici.",
    "La réserve de LO132-2-1 du code des juridictions financières est conservée sans prétendre réécrire ce code extérieur. Le 3° de L612-1 reste stable. La date du 1er janvier 2020 de la note ne devient pas la date de la réforme proposée.",
    "Certification et information parlementaire maintenues comme garanties financières essentielles, sans nouvelle réduction revendiquée.",
    "L'organisation des travaux de la Cour des comptes et leur coût relèvent d'un champ extérieur non modifié par ce maintien.",
    "Aucune charge nouvelle n'est identifiée : ni double certification, ni nouvel état, ni nouveau destinataire ne sont ajoutés.")

s = BY_NUMBER['L612-6']['source_xml']
old = "Elles déclarent le nombre, attesté par un commissaire aux comptes, de travailleurs indépendants adhérents à leur organisation l'année précédente et justifient de leur influence au sens du premier alinéa du présent article."
new = "Elles déclarent le nombre de travailleurs indépendants adhérents à leur organisation l'année précédente et justifient de leur influence au sens du premier alinéa du présent article. Aucune attestation particulière de ce nombre par un commissaire aux comptes, fiche de synthèse signée par celui-ci ou pièce équivalente ne peut être exigée pour cette candidature. Cette dispense ne supprime ni les critères de représentativité, ni la vérification de la réalité des adhésions, ni les obligations autonomes de transparence financière et de contrôle des comptes."
assert old in s
xml = s.replace(old, new, 1) + paras(
    "La dispense d'attestation particulière du nombre d'adhérents s'applique aux candidatures déposées ou en cours d'examen à compter de l'entrée en vigueur de la loi qui la prévoit. Les attestations déjà produites n'ont pas à être refaites. La dispense n'affecte pas les listes et les mandats régulièrement établis avant cette date.")
rewritten('L612-6', xml,
    "Réforme de fond : retrait de la certification spécialement imposée au nombre d'adhérents, avec ses attestations et fiches équivalentes. La déclaration, le seuil d'audience de 8 %, les autres critères cumulatifs, le contrôle de réalité des adhésions et l'audit financier autonome restent requis. Les données Urssaf servant déjà à la vérification réglementaire et la déclaration conservée permettent le contrôle sans ce service privé obligatoirement acheté.",
    "Lecture complète dans le corpus de L2151-1, L2152-4, L2152-5 et L2152-6 du travail : ancienneté organisationnelle de deux ans, transparence, candidature et cycle restent distincts de l'ancienneté d'un salarié. R612-11, R612-13, R612-14, R612-17 et R612-18 ont également été lus : coordonner R612-13 et le 4° de R612-14 pour retirer attestation et fiche spéciale ; ne pas supprimer l'audit autonome et ses dispenses de R612-17. Le renvoi existant à L2152-5 n'impose pas lui-même la certification du nombre. Aucune suppression de l'attestation de représentativité patronale exigée par L2152-4 hors du présent champ n'est revendiquée. Ces règlements ne sont pas modifiés par ce lot.",
    "La certification particulière de l'audience du CPSTI est retirée, sans supprimer la preuve des critères ni le contrôle financier. Son coût exact n'est pas mesuré.",
    "La dispense vise la candidature CPSTI ; elle ne dispense pas une candidature patronale simultanée des exigences propres au code du travail. Coût net inconnu.",
    "Aucune charge nouvelle n'est identifiée : déclaration et contrôles existaient ; aucune nouvelle donnée, registre ou prestation d'audit ne remplace l'attestation.",
    removed=["Attestation obligatoire par commissaire aux comptes du nombre d'adhérents pour la représentativité au CPSTI et fiches justificatives particulières équivalentes."])
effect('L612-6', 'obligation_removed', 'cpsti-audience-fin-attestation-speciale',
       "Retrait de l'attestation spéciale du nombre d'adhérents, avec maintien du seuil et des contrôles.",
       "Nombre d'adhérents de l'année précédente déclaré et obligatoirement attesté par un commissaire aux comptes.",
       "Nombre toujours déclaré ; attestation et fiche spéciale non exigibles, contrôle de réalité et audit des comptes conservés.",
       'legal_duty', 'Organisations candidates à la représentativité des travailleurs indépendants au CPSTI',
       "Candidatures nouvelles et en cours à l'entrée en vigueur ; listes et mandats antérieurs préservés.",
       "Pas de déclaration supplémentaire ; exigences patronales autonomes d'une candidature simultanée réservées.",
       "Elles déclarent le nombre, attesté par un commissaire aux comptes, de travailleurs indépendants adhérents à leur organisation l'année précédente et justifient de leur influence au sens du premier alinéa du présent article.",
       "Aucune attestation particulière de ce nombre par un commissaire aux comptes, fiche de synthèse signée par celui-ci ou pièce équivalente ne peut être exigée pour cette candidature.")

retained('L613-1',
    "Maintien intégral de la réduction des cotisations familiales pour faibles revenus, jusqu'à 5,25 points. La cotisation générale subsiste : supprimer cette règle aggraverait la charge. Les cumuls expressément admis avec Acre, réduction maladie et dispositif agricole demeurent ouverts aux futures situations éligibles ; les supprimer ou modifier unilatéralement le non-cumul désarticulerait les articles réciproques.",
    "Seuil et conditions restent réglementaires, sans inventer leur valeur. L131-6-4 source et proposition ont été lus intégralement ; son III conserve le cumul avec L613-1, et son avantage concerne la création/reprise, non le préavis ou l'indemnité de rupture d'un salarié. L621-3 lu dans le corpus comporte le cumul réciproque. L731-13 est un renvoi existant au régime agricole dont le contenu n'est pas inventé ici. La note d'application au 1er janvier 2025 reste historique.",
    "Réduction favorable et exceptions au non-cumul intégralement maintenues, sans les compter comme une nouvelle baisse de 5,25 points.",
    "Les montants effectifs dépendent du revenu, du seuil et des décrets ; aucune baisse de la cotisation générale des indépendants ni extension au salariat n'est décidée ici.",
    "Aucune charge nouvelle n'est identifiée : mêmes bénéficiaires, conditions réglementaires et exceptions, sans nouvelle demande ou attestation.",
    "L'avantage est la réduction de cotisations familiales, limitée à 5,25 points pour les revenus sous le seuil réglementaire. Il demeure intégralement applicable aux périodes futures éligibles. Les trois possibilités favorables de cumul avec L131-6-4, L621-3 et L731-13 sont toutes conservées ; le plafond microsocial relève de L613-7 et n'est pas neutralisé par ce maintien.")

retained('L613-6',
    "Maintien intégral de la faculté de mandater la plateforme pour les démarches de début d'activité au guichet unique. Ce mandat est volontaire et facilite une obligation d'immatriculation distincte ; l'abroger retirerait une possibilité utile. Il ne vaut pas choix du précompte ni contrat de travail.",
    "Le guichet et le premier alinéa de CGI242 bis restent des renvois existants, sans contenu supplémentaire inventé. La note fixe l'application aux recettes du 1er janvier 2027 : ne pas anticiper cette échéance par une réécriture de style. L311-3, lu dans les cibles, définit notamment un régime optionnel d'affiliation au 35°, sans modifier le mandat de création d'activité.",
    "Possibilité de délégation conservée pour les futurs éligibles ; aucune obligation supprimée, aucun consentement présumé ajouté.",
    "Les obligations du guichet unique et les règles fiscales des plateformes ne sont pas supprimées par cette seule disposition facultative.",
    "Aucune charge nouvelle n'est identifiée : ni mandat obligatoire, ni formulaire ni transmission supplémentaire par rapport à la source.")

xml = paras(
    "I. - Les vendeurs et les prestataires relevant de l'article L. 613-7 ou du 35° de l'article L. 311-3 peuvent choisir que les cotisations et contributions sociales ainsi que les taxes et, le cas échéant, le versement libératoire mentionné au I de l'article 151-0 du code général des impôts dus au titre du chiffre d'affaires ou des recettes réalisés par l'intermédiaire d'une plateforme mentionnée à l'article L. 613-6 soient prélevés par l'opérateur de cette plateforme sur les sommes qui leur sont versées à ce titre. L'opérateur met en œuvre ce choix. Ce prélèvement vaut acquit de ces cotisations et contributions sociales, taxes et impôts par le cotisant concerné. Le choix est révocable pour les sommes non encore prélevées ; il peut être exprimé ou révoqué par tout moyen, sans formulaire ni registre distinct imposé au vendeur ou au prestataire. En l'absence de choix, le vendeur ou le prestataire déclare et acquitte les sommes dues selon les règles de droit commun qui lui sont applicables, sous réserve de la dispense prévue à l'article L. 613-8.",
    "Le présent article n'est pas applicable aux taxes mentionnées au chapitre Ier du titre II de la première partie du livre Ier du code général des impôts, aux articles 150 VI et 1447 du même code et au chapitre Ier du titre VII du livre IV du code des impositions sur les biens et services.",
    "Le choix du précompte n'est soumis à aucun délai minimal à compter du début ou de la reprise d'activité sur une plateforme. Il ne modifie ni les assiettes, ni les abattements, ni les exonérations, ni les taux réduits applicables. Pour les personnes dont les cotisations sont calculées selon le forfait mentionné à l'article L. 613-7, les cotisations et contributions comprises dans ce forfait sont précomptées dans la limite de 20 % du chiffre d'affaires ou des recettes effectivement réalisés, sans écarter les taux inférieurs et les exonérations plus favorables ; ce plafond ne s'étend ni à l'impôt sur le revenu, ni à la formation professionnelle hors forfait, ni au régime distinct du 35° de l'article L. 311-3. L'option volontaire pour des cotisations minimales conserve son régime propre. Aucune cotisation ou taxe supprimée ne peut être prélevée sur le fondement du présent article.",
    "Lorsque le vendeur ou le prestataire est redevable des taxes mentionnées au chapitre Ier du titre II de la première partie du livre Ier du code général des impôts au titre du chiffre d'affaires ou des recettes réalisés par l'intermédiaire d'une plateforme mentionnée au premier alinéa du présent I, l'organisme mentionné à l'article L. 213-1 du présent code régularise auprès du vendeur ou du prestataire le montant prélevé en application du premier alinéa du présent I. Un décret prévoit les conditions et modalités de cette régularisation.",
    "II. - En vue de déterminer les modalités du précompte choisi au I du présent article et de procéder aux opérations mentionnées au III, les vendeurs et les prestataires qui ont fait ce choix transmettent aux opérateurs des plateformes auxquelles ils ont recours les données permettant leur identification. Ces opérateurs transmettent ces mêmes données à l'organisme mentionné à l'article L. 225-1-1. Les transmissions prévues par le présent II ne sont pas exigibles pour les vendeurs et les prestataires qui n'ont pas choisi le précompte.",
    "Les pénalités particulières de 3 250 euros pour les vendeurs et prestataires et de 15 000 euros par vendeur ou prestataire pour les opérateurs, ainsi que leur réitération à six mois, sont supprimées. Cette suppression ne dispense pas de reverser les sommes effectivement prélevées et ne supprime pas les sanctions légalement autonomes de la fraude ou du détournement de ces sommes.",
    "La nature des données mentionnées au premier alinéa du présent II, leurs modalités de transmission et d'utilisation sont déterminées par décret en Conseil d'Etat. Ce décret ne peut rétablir les transmissions pour les personnes n'ayant pas choisi le précompte ni les pénalités particulières supprimées.",
    "III. - Pour les vendeurs et les prestataires ayant choisi le précompte, les opérateurs des plateformes concernées procèdent chaque mois, auprès de l'organisme mentionné à l'article L. 225-1-1 ou de l'un des organismes mentionnés à l'article L. 213-1 désigné par le directeur de l'organisme mentionné à l'article L. 225-1-1 pour exercer cette compétence :",
    "1° A la déclaration du montant du chiffre d'affaires ou des recettes réalisés par chaque vendeur ou prestataire par l'intermédiaire de la plateforme ;",
    "2° A la déclaration et au versement, pour le compte de chaque vendeur ou prestataire, des sommes précomptées en application du I du présent article.",
    "Par dérogation à l'article L. 133-10, les montants du chiffre d'affaires ou des recettes et les sommes précomptées déclarés en application des 1° et 2° du présent III sont arrondis au centime d'euro le plus proche.",
    "Un décret en Conseil d'Etat définit les modalités d'application du présent III.",
    "IV. - Les coûts des prélèvements, des déclarations et des versements que les opérateurs de plateforme effectuent en application du présent article sont à leur charge.",
    "Les cotisations et contributions sociales, les taxes et les impôts précomptés en application du présent article sont recouvrés dans les conditions et sous les garanties, sûretés et sanctions applicables aux cotisations et contributions précomptées sur la rémunération des salariés prévues aux chapitres III et IV du titre IV du livre II.",
    "La pénalité particulière d'un montant maximal égal à 5 % du chiffre d'affaires ou des recettes pour méconnaissance de l'obligation de précompte est supprimée. Les garanties et les sanctions de recouvrement mentionnées à l'alinéa précédent demeurent applicables dans leur champ propre, sans permettre de rétablir cette pénalité particulière.",
    "Ces dispositions s'appliquent à compter du 1er janvier 2027 ou, si elle est postérieure, de l'entrée en vigueur de la loi rendant le précompte facultatif. Pour les opérations soumises au dispositif avant le 1er janvier 2027 dans le cadre de l'application progressive aux plateformes volontaires prévue par le II de l'article 6 de la loi n° 2023-1250 du 26 décembre 2023, elles s'appliquent dès cette entrée en vigueur. Le maintien du précompte pour les sommes non encore prélevées dépend du choix du vendeur ou du prestataire, sans nouveau délai minimal. Les sommes prélevées auparavant conservent leur effet libératoire et doivent être déclarées, reversées et, s'il y a lieu, régularisées selon les règles applicables lors du prélèvement, sans double paiement ni double remboursement. Les sanctions non définitives et l'exécution des condamnations demeurent soumises aux règles d'application de la loi répressive plus douce. Les prescriptions, créances et recours des périodes antérieures sont conservés dans ce cadre.")
rewritten('L613-6-1', xml,
    "Réforme de fond : le précompte général imposé aux vendeurs des plateformes devient un service choisi et révocable ; les flux particuliers d'identification et de déclaration sont limités à ce choix. Sont retirés le délai minimal d'accès et les pénalités spécifiques de 3 250 euros, 15 000 euros et 5 %. Les dettes principales ne sont pas supprimées : le droit commun s'applique hors option. Le prélèvement choisi conserve son effet libératoire, la prise en charge des frais par la plateforme, les exclusions de taxes, la régularisation TVA, l'arrondi et les garanties de reversement. Coordination du plafond microsocial décidé à L613-7, sans appliquer ce plafond au 35° de L311-3 ni à l'IR.",
    "I à IV et 1°/2° du III sont conservés ; les anciens 1°/2° de pénalités du II sont supprimés avec leur norme. Le choix et sa révocation nécessitent un suivi nouveau par les plateformes : classement mixed, solde de coût inconnu. Le renvoi à L613-7 ne suffit pas à créer son plafond : sa réécriture et les décrets doivent être coordonnés ; le texte source intégral de L613-7 a été lu au corpus et la différence avec le projet est explicite. Les abattements de 60 % et 87 % du 35° de L311-3 demeurent à leur champ. Les missions d'Acoss et d'Urssaf ne sont pas des contrats de travail. La note d'effet immédiat de la modification du 30 décembre 2025 doit être articulée avec le calendrier général 2027 et le pilote volontaire 2026 de l'article 6 de la loi 2023-1250 ; la transition proposée conserve ces deux champs sans les anticiper. Coordonner décrets, arrêtés et formalités du précompte, ainsi que le contrôle de la pénalité de 5 % ; aucun texte d'exécution hors lot n'est déclaré réécrit.",
    "Les obligations de précompte et de flux particuliers cessent hors choix ; trois sanctions spéciales et le délai minimal sont supprimés. Le choix/révocation ajoute une gestion d'option, donc le bilan est mixte. Aucun impôt principal n'est déclaré aboli.",
    "Le coût net des options, le rendement social et l'effet sur la conformité ne sont pas chiffrés. Les obligations de droit commun, les obligations fiscales autonomes des plateformes et les anciennes périodes restent hors suppression.",
    "La gestion du choix et de sa révocation est un élément nouveau pour la plateforme ; aucun formulaire ni registre distinct n'est imposé au cotisant. Le coût net de cette gestion et des flux retirés n'est pas établi ; les transmissions et le reversement des prélèvements choisis restent dus.",
    removed=[
        "Précompte obligatoire et transmissions particulières d'identification et de recettes pour les vendeurs et prestataires qui ne choisissent pas ce service.",
        "Délai minimal ministériel entre le début ou la reprise d'activité et l'accès au précompte désormais facultatif.",
        "Pénalités particulières de 3 250 euros et 15 000 euros par personne ainsi que leur réitération possible après six mois.",
        "Pénalité particulière de 5 % du chiffre d'affaires ou des recettes pour méconnaissance du précompte, distincte des garanties de reversement maintenues."
    ], classification='mixed',
    benefit="L'effet libératoire de chaque prélèvement est expressément conservé, pour les prélèvements passés comme pour ceux choisis à l'avenir. Les frais restent à la charge de la plateforme et l'arrondi au centime demeure. Les exclusions TVA, 150 VI, CFE et CIBS sont reprises ; la régularisation de TVA demeure. La fin du délai minimal n'oblige personne à précompter plus tôt, le service devenant choisi. Les exonérations, abattements, taux inférieurs et l'option volontaire minimale sont préservés ; les 60 % et 87 % du 35° de L311-3 ne sont pas remplacés par le plafond microsocial de 20 %. Les recettes non précomptées restent soumises aux mêmes avantages dans le droit commun, avec la nouvelle dispense de déclaration nulle de L613-8.")
effect('L613-6-1', 'obligation_removed', 'plateformes-precompte-facultatif',
       "Fin du précompte imposé et des flux sociaux propres à ce service pour les non-optants.",
       "Prélèvement par l'opérateur des sommes dues sur les recettes de plateforme des personnes L613-7 ou L311-3 35°, avec flux mensuels et identification.",
       "Précompte sur choix du cotisant ; hors choix, paiement et déclaration de droit commun et absence de flux particuliers du II/III.",
       'legal_duty', 'Vendeurs et prestataires L613-7 ou L311-3 35° et plateformes correspondantes',
       "Calendrier 2027 ou entrée en vigueur ultérieure ; application dès la réforme dans le pilote volontaire antérieur ; prélèvements passés libératoires.",
       "Gestion du choix et de sa révocation pour les plateformes ; obligations ordinaires du vendeur hors choix maintenues, coût net inconnu.",
       "sont prélevés par l'opérateur de cette plateforme sur les sommes qui leur sont versées à ce titre.",
       "Les transmissions prévues par le présent II ne sont pas exigibles pour les vendeurs et les prestataires qui n'ont pas choisi le précompte.")
effect('L613-6-1', 'complexity_added', 'plateformes-precompte-facultatif',
       "Le service choisi implique le traitement d'une option et de ses révocations, inexistant dans le précompte obligatoire.",
       "Le dispositif imposait le précompte sans choix individuel du vendeur ou du prestataire.",
       "La plateforme met en œuvre un choix individuel révocable pour les sommes non encore prélevées.",
       'legal_duty', 'Plateformes et utilisateurs choisissant le précompte',
       "Même transition que la mise en place du précompte facultatif ; aucun formulaire ou registre distinct pour le cotisant.",
       "Suivi opérationnel de l'option et de sa révocation ; coût non mesuré, sans déduction automatique d'un gain net.",
       "sont prélevés par l'opérateur de cette plateforme sur les sommes qui leur sont versées à ce titre.",
       "Le choix est révocable pour les sommes non encore prélevées")
effect('L613-6-1', 'obligation_removed', 'plateformes-fin-penalites-speciales',
       "Suppression des sanctions particulières d'identification et de défaut de précompte, en conservant les garanties de reversement.",
       "Plafonds de 3 250 euros pour le vendeur, 15 000 euros par vendeur pour la plateforme, réitérables à six mois ; autre pénalité jusqu'à 5 % des recettes non précomptées.",
       "Ces pénalités spécifiques sont supprimées ; dette principale, reversement des sommes encaissées et sanctions autonomes restent applicables.",
       'other', 'Vendeurs, prestataires et plateformes soumis au dispositif de précompte',
       "Dès application de la réforme dans son champ ; réserve de la loi répressive plus douce pour sanctions non définitives et exécution.",
       "Aucune sanction spéciale de remplacement ; les sanctions légales autonomes ne sont pas une suppression supplémentaire.",
       "La méconnaissance par un opérateur de plateforme de l'obligation de précompte prévue au I entraîne l'application d'une pénalité d'un montant maximal égal à 5 % du chiffre d'affaires ou des recettes sur lesquels cette obligation a été méconnue.",
       "La pénalité particulière d'un montant maximal égal à 5 % du chiffre d'affaires ou des recettes pour méconnaissance de l'obligation de précompte est supprimée.")
effect('L613-6-1', 'deadline_reduced', 'plateformes-precompte-facultatif',
       "Suppression du délai minimal d'accès au service choisi, sans précompte anticipé imposé.",
       "Application après un délai depuis le début ou la reprise d'activité fixé par arrêté, dont la durée n'est pas fournie dans la source.",
       "Aucun délai minimal de début ou reprise pour le choix ; calendrier légal d'application du dispositif conservé.",
       'other', 'Utilisateurs éligibles au précompte facultatif',
       "Seulement à compter de l'application légale de la réforme ; aucune anticipation du calendrier 2027 ou du pilote.",
       "Choix facultatif avec gestion de l'option ; aucune avance imposée à un non-optant.",
       "qu'à l'expiration d'un délai à compter du début ou de la reprise d'activité sur une plateforme qui est défini par arrêté du ministre chargé de la sécurité sociale.",
       "Le choix du précompte n'est soumis à aucun délai minimal à compter du début ou de la reprise d'activité sur une plateforme.")
effect('L613-6-1', 'coordination', 'micro-social-plafond-vingt-pour-cent',
       "Le précompte ne doit pas neutraliser le plafond social de L613-7 décidé par la coordination, ni les avantages inférieurs.",
       "Prélèvement des sommes dues par renvoi aux régimes L613-7 ou L311-3 35°, sans plafond chiffré propre à cet article.",
       "Dans le seul forfait L613-7 : coordination du plafond de 20 % du CA/recettes réalisés, taux inférieurs préservés ; IR, formation hors forfait et L311-3 35° distincts.",
       'percent', 'Personnes L613-7 choisissant le précompte, avec réserve de leur option volontaire minimale',
       "Le plafond dépend du texte opératoire L613-7 et de sa propre transition ; aucune seconde baisse comptée dans ce renvoi.",
       "Pas d'assiette sociale élargie ; suivi d'option déjà recensé dans la mesure plateformes-precompte-facultatif.",
       "les vendeurs et les prestataires relevant de l'article L. 613-7 ou du 35° de l'article L. 311-3",
       "les cotisations et contributions comprises dans ce forfait sont précomptées dans la limite de 20 % du chiffre d'affaires ou des recettes effectivement réalisés")

xml = paras(
    "Sous réserve de l'article L. 613-6-1, les travailleurs indépendants mentionnés à l'article L. 613-7 déclarent chaque mois ou chaque trimestre leur chiffre d'affaires ou leurs recettes lorsque leur montant est positif. Aucune déclaration périodique n'est exigée pour une période dont le chiffre d'affaires ou les recettes sont nuls. Cette dispense ne fait obstacle ni à une déclaration volontaire, ni à la rectification d'un montant antérieurement déclaré, ni à la déclaration des recettes effectivement réalisées.",
    "L'absence de déclaration au titre d'une période nulle ne vaut ni cessation d'activité ni renonciation à un droit social ou à une exonération. Elle ne peut, à elle seule, justifier une radiation, une sanction pour défaut de déclaration de cette période ou la perte d'un avantage. Les conditions propres aux droits sociaux, aux exonérations et à l'option volontaire pour des cotisations minimales demeurent applicables.",
    "La dispense s'applique aux déclarations dont l'échéance intervient à compter de l'entrée en vigueur de la loi la prévoyant, y compris pour une période antérieure. Les déclarations déjà déposées ne sont pas à refaire. Elle s'applique aussi dans le cadre de l'application progressive aux plateformes volontaires prévue au II de l'article 6 de la loi n° 2023-1250 du 26 décembre 2023 ; elle n'anticipe pas l'application générale du dispositif de précompte au 1er janvier 2027. Les sommes réellement dues, les rectifications, les restitutions, les prescriptions et les recours afférents aux périodes antérieures demeurent régis par leurs règles propres, sous réserve de l'application de la loi répressive plus douce.")
rewritten('L613-8', xml,
    "Réforme de fond : retrait de la déclaration mensuelle ou trimestrielle à néant, qui ne liquide aucun montant proportionnel. Le chiffre d'affaires positif et les rectifications restent déclarés ; le recours au précompte évite toujours un double dépôt. La dispense ne déclenche ni radiation ni perte d'avantage du seul fait du silence sur une période nulle, et laisse possible une déclaration volontaire utile aux droits.",
    "Le calendrier de la note combine droit général au 1er janvier 2027 et pilote volontaire dès 2026 ; la dispense de déclaration nulle joue dès la réforme pour les échéances futures sans anticiper le précompte général. Coordonner les règlements de déclaration, pénalités, radiation et attestations pour qu'ils n'exigent pas de confirmation nulle de remplacement. Les déclarations positives, l'option de cotisations minimales et les conditions propres aux prestations ne sont pas supprimées.",
    "La déclaration périodique nulle expressément imposée par la source disparaît effectivement, sans simple reprise du réemploi des données déjà acquises.",
    "La dispense n'est pas une exonération de sommes dues ; son incidence sur les systèmes et sur les démarches d'attestation n'est pas chiffrée.",
    "Aucune charge nouvelle n'est identifiée : aucune attestation de chiffre d'affaires nul, confirmation périodique ou demande d'accès à la dispense n'est substituée au dépôt retiré.",
    removed=["Déclaration obligatoire mensuelle ou trimestrielle du chiffre d'affaires ou des recettes lorsque le montant de la période est nul."])
effect('L613-8', 'obligation_removed', 'micro-social-fin-declaration-neant',
       "Dispense des dépôts périodiques pour les périodes sans chiffre d'affaires ni recettes.",
       "Déclaration mensuelle ou trimestrielle obligatoire, y compris pour un montant nul, sous réserve du précompte.",
       "Seuls montants positifs obligatoirement déclarés ; dépôts volontaires et rectifications possibles, silence nul sans radiation automatique.",
       'legal_duty', 'Travailleurs indépendants du régime L613-7',
       "Échéances à compter de la réforme, même sur période ancienne ; déclarations déjà déposées non refaites ; calendrier du précompte conservé.",
       "Aucun dépôt nul de remplacement ; les obligations liées aux montants positifs demeurent.",
       "déclarent chaque mois ou chaque trimestre leur chiffre d'affaires ou leurs recettes, y compris lorsque leur montant est nul.",
       "Aucune déclaration périodique n'est exigée pour une période dont le chiffre d'affaires ou les recettes sont nuls.")

retained('L613-9',
    "Maintien intégral de l'ordre d'imputation du recouvrement partiel. Il n'impose ni taxe ni paiement supplémentaire et donne une règle nécessaire à l'affectation des sommes, distincte des taux. Le supprimer sans nouvel ordre créerait de l'incertitude sur l'acquit fiscal et les droits sociaux.",
    "La priorité IR ne crée pas d'IR si le versement libératoire n'est pas dû. Le renvoi L133-4-11 reste celui de la source pour l'affectation partielle des cotisations ; ni la suppression de CFE des microentrepreneurs ni le plafond de L613-7 ne sont neutralisés par cette règle d'ordre. La date du 1er janvier 2022 dans la note reste historique.",
    "Affectation inchangée des sommes effectivement recouvrées ; ce maintien n'est pas un transfert de financement décidé par la réforme.",
    "L'impact de la priorité fiscale sur la constitution des droits en cas de dette partielle n'est pas quantifié ; aucun ordre alternatif n'est inventé.",
    "Aucune charge nouvelle n'est identifiée : aucun versement, taux, compte ou relevé additionnel n'est demandé par cette règle maintenue.")

xml = paras(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant l'obligation de compte dédié des travailleurs indépendants relevant de l'article L. 613-7. Aucune obligation d'ouvrir, de dédier ou de maintenir un compte bancaire distinct ne peut être imposée sur son fondement, y compris lorsque le chiffre d'affaires a dépassé 10 000 euros pendant deux années civiles consécutives avant cette entrée en vigueur.",
    "Les comptes déjà ouverts peuvent être conservés volontairement. Leur changement d'affectation ou leur clôture demeure soumis aux stipulations contractuelles et aux règles bancaires applicables ; aucune clôture automatique n'est imposée. La suppression ne dispense ni de la tenue des documents comptables légalement exigés, ni de la justification des recettes, ni des obligations bancaires ayant un fondement légal autonome. Elle ne permet pas d'exiger un compte, un registre ou une déclaration de remplacement sur le seul fondement abrogé.",
    "Les créances contractuelles et les recours relatifs aux périodes antérieures sont préservés. L'application de la loi répressive plus douce aux sanctions non définitives et à l'exécution des condamnations demeure réservée.")
rewritten('L613-10', xml,
    "Abrogation de fond du compte obligatoirement dédié au-delà de deux années à 10 000 euros. La traçabilité peut rester assurée par les pièces ordinaires et les contrôles sans imposer un compte supplémentaire à tout microentrepreneur franchissant le seuil. Les autres obligations bancaires autonomes et la comptabilité subsistent ; aucun registre de remplacement ni suppression de dette sociale.",
    "Le seuil historique de 10 000 euros et les deux années sont cités pour empêcher leur survie, pas pour fixer un nouveau régime. L123-24 du commerce est un renvoi existant définissant les établissements ; les éventuelles obligations autonomes des commerçants ne sont pas présentées comme abrogées. Les contrats bancaires ne sont ni rompus ni gratuits de plein droit. Coordonner les demandes administratives qui exigeraient ce compte sur le seul ancien L613-10.",
    "L'obligation de dédier un compte à l'activité est supprimée, y compris pour les dépassements déjà constatés. Le montant des frais effectivement évités dépend des comptes utilisés.",
    "Les comptes exigés par un autre fondement, les frais contractuels et les pièces de comptabilité restent distincts ; aucun gain forfaitaire par entreprise n'est démontré.",
    "Aucune charge nouvelle n'est identifiée : ni registre, ni attestation bancaire, ni déclaration ne remplace le compte dédié supprimé.",
    repeal="Obligation de dédier un compte distinct aux transactions professionnelles des personnes L613-7 après dépassement de 10 000 euros pendant deux années consécutives.")
effect('L613-10', 'obligation_removed', 'micro-social-fin-compte-dedie',
       "Suppression du compte bancaire dédié imposé par cet article.",
       "Compte dédié à toutes les transactions professionnelles obligatoire pour les personnes L613-7 après plus de 10 000 euros de CA annuel deux années consécutives.",
       "Aucune ouverture ou affectation bancaire distincte imposée par L613-10, quel que soit le dépassement antérieur ; autres fondements autonomes réservés.",
       'legal_duty', 'Travailleurs indépendants du régime L613-7 dépassant le seuil source',
       "Fin de l'obligation dès l'entrée en vigueur ; comptes existants facultativement conservés, contrats et créances bancaires antérieurs préservés.",
       "Aucun registre ou compte de remplacement ; comptabilité et preuve des recettes demeurent.",
       "Les travailleurs indépendants mentionnés à l'article L. 613-7 sont tenus de dédier un compte ouvert dans un des établissements mentionnés à l'article L. 123-24 du code de commerce à l'exercice de l'ensemble des transactions financières liées à leur activité professionnelle lorsque leur chiffre d'affaires a dépassé pendant deux années civiles consécutives un montant annuel de 10 000 €.",
       "Aucune obligation d'ouvrir, de dédier ou de maintenir un compte bancaire distinct ne peut être imposée sur son fondement")

xml = paras(
    "Sauf demande contraire de la part des travailleurs indépendants effectuée dans des conditions fixées par décret, les éventuels montants minimaux afférents aux cotisations mentionnées à l'article L. 621-1, l'assiette minimale de cotisations prévue au dernier alinéa de l'article L. 621-2 et les montants minimaux de cotisations prévus à l'article L. 633-1, à l'avant-dernier alinéa de l'article L. 635-1 et au dernier alinéa de l'article L. 632-1 et, pour les professions libérales, à l'avant-dernier alinéa de l'article L. 642-1 et, le cas échéant, aux articles L. 644-1 et L. 644-2 ne sont pas applicables aux cotisations et aux contributions de sécurité sociale dues par les personnes mentionnées à l'article L. 262-2 du code de l'action sociale et des familles et à l'article L. 842-1 du présent code ainsi qu'aux cotisations et aux contributions de sécurité sociale dues par les personnes au titre des activités accessoires saisonnières qu'elles exercent. Aucune condition réglementaire supplémentaire ne peut restreindre cette dispense pour les personnes et activités ainsi définies.",
    "Cette dispense s'applique aux périodes d'activité courant à compter de l'entrée en vigueur de la loi l'étendant. Les périodes antérieures restent soumises aux règles qui leur étaient applicables, avec leurs dispenses, créances, restitutions, prescriptions et recours. Les demandes volontaires d'application des minima déjà formées demeurent valables selon leur régime propre. La dispense de minima ne supprime ni les cotisations calculées sur l'assiette réelle lorsqu'elles sont dues, ni les droits déjà constitués ; elle ne garantit pas des droits futurs identiques à ceux résultant de cotisations plus élevées.")
rewritten('L613-11', xml,
    "Réforme de fond favorable : suppression de l'habilitation à ajouter des conditions réglementaires à la dispense de minima pour les personnes et activités déjà définies par l'article ; inclusion explicite de l'assiette minimale de cotisation supplémentaire maladie de L621-2. La source visait L621-1, dont le texte actuel ne prévoit pas lui-même de minimum. Le nouveau corps conserve de façon autonome la dispense de tout éventuel minimum afférent à L621-1 et étend expressément la protection à L621-2, sans prétendre démontrer une simple concordance historique. La faculté de cotiser volontairement aux minima est conservée.",
    "Nouveau renvoi au dernier alinéa de L621-2 non fourni parmi les cibles de reference-targets.json : texte officiel et note lus intégralement au corpus public, qui prévoient effectivement une assiette minimale pour les indépendants hors L613-7 à faible revenu. L621-1, L632-1, L633-1, L635-1, L642-1 et L644-1/2 ont aussi été lus ; les autres renvois et qualifications restent ceux de la source. Le fondement autonome préservant la dispense L621-1 et l'extension L621-2 sont explicites, sans affirmer une filiation recodificatrice non prouvée. Coordonner les décrets qui imposeraient des conditions supplémentaires à cette dispense ; leur inventaire complet n'est pas réalisé dans ce lot. Le cadre de capitalisation des salariés privés n'est pas étendu aux indépendants.",
    "La dispense de minima est ouverte sans condition réglementaire additionnelle dans le champ légal et couvre explicitement l'assiette minimale L621-2. Pas de taux nouveau ni de suppression des cotisations sur revenu réel.",
    "Le nombre de bénéficiaires supplémentaires et les cotisations évitées dépendent des situations et des décrets antérieurs ; ils ne sont pas chiffrés. Les droits futurs peuvent différer.",
    "Aucune charge nouvelle n'est identifiée : pas de demande d'accès à la dispense ni de justificatif nouveau. La demande contraire de maintien volontaire des minima existait déjà.",
    removed=["Conditions réglementaires supplémentaires susceptibles de restreindre la dispense légale de minima des bénéficiaires visés et des activités accessoires saisonnières."],
    benefit="La dispense de minima est conservée pour les personnes visées par L262-2 et L842-1 et pour les activités accessoires saisonnières, et reste ouverte aux situations futures. La faculté favorable de demander volontairement le maintien des minima est reprise. Le nouveau texte étend explicitement la dispense à l'assiette minimale L621-2 et retire les conditions réglementaires additionnelles ; les anciennes périodes gardent leurs dispenses et recours. Aucun prélèvement de remplacement ni garantie fictive de droits futurs inchangés n'est créé.")
effect('L613-11', 'relief_extended', 'independants-dispense-minima-extension',
       "Retrait des conditions réglementaires additionnelles et fondement explicite de la dispense d'assiette minimale L621-2.",
       "Dispense de minima sous conditions réglementaires pour bénéficiaires visés et activités accessoires saisonnières ; renvoi source à L621-1 sans minimum dans son corps actuel.",
       "Même champ légal dispensé sans restriction réglementaire additionnelle, avec inclusion explicite de l'assiette minimale L621-2 ; option volontaire de minima conservée.",
       'legal_duty', 'Indépendants visés par L262-2 CASF ou L842-1 CSS et personnes au titre de leurs activités accessoires saisonnières',
       "Périodes à compter de l'entrée en vigueur ; anciennes dispenses et demandes volontaires préservées.",
       "Aucune démarche nouvelle d'accès ; contrôle de l'appartenance aux catégories légales maintenu, pas de droits futurs garantis à l'identique.",
       "ne sont pas applicables, sous certaines conditions déterminées par décret",
       "Aucune condition réglementaire supplémentaire ne peut restreindre cette dispense pour les personnes et activités ainsi définies.")

xml = paras(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant l'inéligibilité automatique qu'il prévoit. Aucune inéligibilité aux chambres de commerce et d'industrie territoriales ou aux chambres de métiers ne peut être prononcée ou opposée sur ce seul fondement après cette date. Les inéligibilités de six ans résultant exclusivement du présent article cessent de produire effet à cette date, sans rétablissement automatique d'un mandat antérieurement perdu.",
    "Cette suppression n'annule ni les condamnations prononcées en application des articles L. 114-13 ou L. 114-18, ni les décisions antérieures relatives aux mandats. Les infractions, les peines et les inéligibilités fondées sur d'autres dispositions, les obligations d'affiliation et de cotisation ainsi que les droits des organismes sociaux et leurs voies de recours demeurent applicables dans leur champ propre. L'application de la loi répressive plus douce demeure réservée.")
rewritten('L615-2', xml,
    "Abrogation de l'inéligibilité automatique de six ans aux chambres consulaires, conséquence accessoire uniforme des condamnations visées. Les infractions de fraude et de refus d'affiliation restent réprimées par L114-13/L114-18, lus dans le corpus ; leur protection essentielle ne suppose pas cette exclusion automatique additionnelle. Les peines fondées sur d'autres textes ne sont pas retirées.",
    "La suppression met aussi fin aux effets futurs de la seule inéligibilité automatique en cours sans annuler la condamnation ni restaurer de mandat. Les procédures électorales et conditions d'éligibilité autonomes des chambres ne sont pas réécrites ; vérifier leurs renvois éventuels à cet article avant consolidation. Pas d'amnistie générale ni de suppression de dette sociale.",
    "Fin d'une exclusion automatique de six ans ; la répression des comportements frauduleux et les autres incapacités légales restent distinctes.",
    "Les autres causes d'inéligibilité peuvent continuer d'exclure une candidature ; aucun effet sur le nombre de sièges ou les cotisations n'est démontré.",
    "Aucune charge nouvelle n'est identifiée : pas de demande de réhabilitation, d'autorisation ou de déclaration remplaçant la fin de l'exclusion.",
    repeal="Inéligibilité automatique de six ans aux chambres consulaires attachée aux condamnations L114-13 et L114-18, avec fin de ses effets futurs exclusivement fondés sur cet article.")
effect('L615-2', 'obligation_removed', 'independants-fin-ineligibilite-automatique',
       "Retrait de l'inéligibilité automatique consulaire de six ans.",
       "Personnes L611-1 condamnées au titre de L114-13 ou L114-18 inéligibles six ans aux chambres énumérées.",
       "Aucune inéligibilité fondée sur L615-2 ; effets futurs des exclusions en cours arrêtés, autres fondements préservés.",
       'other', 'Personnes L611-1 candidates aux chambres consulaires après les condamnations visées',
       "Effet dès l'entrée en vigueur, sans annuler condamnations ou décisions antérieures de mandat, sans rétablissement de mandat.",
       "Aucune procédure de remplacement ; infractions et peines autonomes maintenues.",
       "condamnées en application des articles L. 114-13 ou L. 114-18 sont inéligibles pour une durée de six ans",
       "Les inéligibilités de six ans résultant exclusivement du présent article cessent de produire effet à cette date")

xml = paras(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant la dérogation permettant de prononcer dès la première condamnation les peines d'inéligibilité et d'incapacité pour non-paiement des cotisations. Ces peines ne peuvent plus être prononcées sur le seul fondement de cette dérogation ; l'article L. 244-4 demeure applicable dans ses propres conditions.",
    "Les obligations de cotisation, le recouvrement et les sanctions ayant un fondement autonome ne sont pas supprimés. Les condamnations et décisions devenues définitives avant cette entrée en vigueur demeurent soumises aux règles qui leur sont applicables, sous réserve de l'application de la loi répressive plus douce aux sanctions non définitives et à l'exécution des condamnations. Aucun mandat antérieurement perdu n'est rétabli de plein droit.")
rewritten('L615-3', xml,
    "Abrogation de fond de l'aggravation spéciale qui permettait d'appliquer dès la première condamnation des incapacités et inéligibilités relevant du régime de récidive de L244-4. Le recouvrement et les sanctions ordinaires subsistent : il n'est pas nécessaire d'exclure plus tôt les indépendants de fonctions électives ou consultatives pour conserver le paiement obligatoire.",
    "L244-4 et ses notes ont été lus intégralement au corpus : récidive définie dans les douze mois avant expiration de la mise en demeure, peines judiciaires de six mois à cinq ans. Ce délai n'est pas le préavis de quinze jours d'un emploi privé. La note de source visant L612-12 est historique et ce numéro n'est pas présent comme article actif dans le corpus consulté ; elle n'est pas transformée en renvoi opératoire. La réforme ne modifie pas L244-4 hors de cette dérogation.",
    "Le juge ne peut plus employer cette dérogation pour des peines accessoires dès la première condamnation ; pas de remise de la cotisation principale.",
    "Le droit commun de récidive et les sanctions autonomes demeurent. La disparition d'un prononcé fondé seulement sur la dérogation ne retire pas une autre base légale applicable.",
    "Aucune charge nouvelle n'est identifiée : aucune sanction, formalité ou autorisation de remplacement ne se substitue à l'aggravation supprimée.",
    repeal="Dérogation permettant au juge de prononcer dès la première condamnation pour non-paiement les peines d'inéligibilité et d'incapacité normalement prévues à L244-4.",
    benefit="La dérogation de la source n'est pas un avantage pour le cotisant : elle permet de prononcer plus tôt des peines accessoires. Sa suppression rétablit les conditions ordinaires plus protectrices de L244-4, sans supprimer de réduction ou d'exonération. Les droits aux prestations et les allègements de cotisations restent à leurs fondements propres, pour les situations futures également ; aucune taxe n'est créée ou remplacée.")
effect('L615-3', 'obligation_removed', 'independants-fin-incapacite-premiere-condamnation',
       "Suppression de l'anticipation des peines accessoires dès la première condamnation.",
       "Inéligibilité et incapacité judiciaires de L244-4 possibles dès la première condamnation pour cotisations du titre.",
       "Plus de dérogation spéciale ; seules les conditions propres de L244-4 ou d'autres textes autonomes permettent ces peines.",
       'other', 'Travailleurs indépendants poursuivis pour non-paiement de cotisations des régimes du titre',
       "Prononcés après l'entrée en vigueur et application de la loi répressive plus douce dans son champ ; décisions définitives sans annulation générale.",
       "Pas de sanction ou procédure de remplacement ; dette sociale et voies de recouvrement maintenues.",
       "le juge peut prononcer les peines d'inéligibilité et d'incapacité prévues à cet article dès la première condamnation",
       "Ces peines ne peuvent plus être prononcées sur le seul fondement de cette dérogation")

xml = paras(
    "Le présent article est abrogé pour les clauses et conventions conclues ou renouvelées à compter de l'entrée en vigueur de la loi supprimant la nullité d'assurance qu'il prévoit. Pour ces clauses et conventions, le défaut de paiement des cotisations obligatoires ne peut, sur le fondement du présent article, entraîner leur nullité, une peine liée à leur proposition ou à leur souscription, ni la responsabilité solidaire de la personne les ayant fait souscrire au titre des cotisations de l'assuré.",
    "Cette abrogation ne dispense l'assuré ni de son affiliation obligatoire ni du paiement de ses cotisations et ne substitue aucune assurance privée à un régime obligatoire. Elle ne supprime ni le recouvrement, ni les infractions et responsabilités ayant un fondement légal autonome, ni les protections des assurés prévues par les autres textes.",
    "Pour les clauses et conventions conclues ou renouvelées avant cette entrée en vigueur, les droits, créances de cotisations et responsabilités nés de ces actes, leurs prescriptions et leurs voies de recours restent régis par les règles antérieurement applicables, y compris l'exclusion des contrats d'assurance complémentaire en matière de santé du champ de la nullité. L'application de la loi répressive plus douce aux sanctions non définitives et à l'exécution des condamnations demeure réservée. Aucun contrat de santé n'est soumis à une nullité ou à une condition de paiement nouvelle du fait de cette abrogation.")
rewritten('L615-4', xml,
    "Abrogation prospective de la nullité d'ordre public d'assurance, des peines particulières de souscription et de la solidarité spéciale du souscripteur professionnel. La nullité d'un contrat privé liée à un arriéré social ajoute une sanction au recouvrement sans être indispensable au maintien de l'affiliation ; les protections antifraude et les dettes sociales demeurent. La dérogation favorable des complémentaires santé est expressément protégée sur le stock ancien et devient sans objet pour les nouveaux contrats, dont toute cette nullité disparaît.",
    "La transition distingue les clauses et conventions conclues ou renouvelées après la réforme des créances et responsabilités déjà nées. Aucun remboursement général ni disparition des droits des organismes contre un débiteur ancien. Le décret en Conseil d'Etat déterminant les peines particulières doit être retiré dans son champ futur ; les infractions de fraude et de désaffiliation ayant une autre base demeurent. Ni capital décès, ni droit de succession, ni cotisation invalidité-décès obligatoire ne sont abolis par cet article.",
    "Les nouvelles souscriptions et renouvellements ne subissent plus la nullité, les peines propres et la solidarité sur ce fondement ; les cotisations restent intégralement dues.",
    "La validité du contrat au regard d'autres causes, les dettes anciennes et les responsabilités autonomes restent à apprécier. Aucune réduction de cotisations ou économie nationale n'est chiffrée.",
    "Aucune charge nouvelle n'est identifiée : aucun agrément, certificat d'apurement ou déclaration ne remplace la nullité supprimée ; les garanties d'autres textes subsistent.",
    repeal="Nullité d'assurance liée aux arriérés de cotisations, peines propres de proposition ou souscription et solidarité spéciale pour les clauses et conventions nouvelles ou renouvelées après la réforme.",
    benefit="L'exception favorable aux contrats d'assurance complémentaire santé est conservée expressément pour les actes antérieurs tant que leur régime de nullité subsiste. Pour les actes futurs, la nullité générale et ses accessoires sont entièrement supprimés, sans condition équivalente de remplacement : les contrats de santé ne peuvent donc devenir moins favorables sur ce fondement. Les protections des assurés, l'affiliation obligatoire et les droits sociaux autonomes demeurent, y compris pour les futures situations éligibles.")
effect('L615-4', 'obligation_removed', 'independants-assurance-fin-nullite-arrieres',
       "Suppression du blocage civil et pénal spécial de souscription d'assurance pour défaut de paiement social.",
       "Nullité d'ordre public si cotisant non à jour lors de la conclusion ou du renouvellement, hors complémentaire santé ; peines et solidarité spéciale du professionnel condamné.",
       "Ni nullité, ni peine propre, ni solidarité sur ce fondement pour les nouveaux actes ; affiliation et cotisations demeurent obligatoires.",
       'legal_duty', 'Travailleurs indépendants souscrivant une assurance couvrant des risques obligatoires et personnes proposant ces assurances',
       "Actes conclus ou renouvelés dès l'entrée en vigueur ; stock, créances et exception santé antérieurs préservés ; loi répressive plus douce réservée.",
       "Aucun certificat d'apurement ni déclaration d'assurance de remplacement ; responsabilités autonomes maintenues.",
       "Est entachée d'une nullité d'ordre public toute clause ou convention conclue par tout travailleur indépendant légalement tenu de cotiser à un régime d'assurance obligatoire garantissant les risques couverts à titre obligatoire par lesdits régimes, lorsque cette personne n'est pas à jour des cotisations dues à ce titre au moment de la conclusion ou du renouvellement du contrat.",
       "le défaut de paiement des cotisations obligatoires ne peut, sur le fondement du présent article, entraîner leur nullité")

retained('L615-5',
    "Maintien intégral du rattachement des prestations du livre VI aux règles sur la faute intentionnelle, les recours contre tiers responsables et la protection contre certains agissements d'intermédiaires. L376-1 et L376-2 protègent en particulier l'indemnisation prioritaire de la victime. Supprimer le renvoi entier retirerait aussi ces garanties ; aucune réforme de ces chapitres n'est décidée par le contrat unique.",
    "Lecture au corpus de L375-1, L376-1 à L376-4 et L377-2 à L377-4. L377-1 n'y figure pas comme texte actif ; cela ne vide pas le renvoi aux autres articles. Les obligations d'information du tiers et de l'assureur évitent un double paiement et protègent la subrogation. Le délai amiable de quinze jours de L376-3 n'est pas un préavis d'emploi. Le maximum obligatoire en récidive et la publication plafonnée à 7,5 euros de L377-4 constituent une difficulté préexistante à confronter aux règles d'individualisation des peines ; elle est signalée, sans réécriture silencieuse de cet article hors lot. Aucune filiation vers un contrat de travail n'est inventée.",
    "Le renvoi aux protections et règles communes des prestations est maintenu, sans compter une réduction de charge ni un nouveau régime.",
    "Les éventuels allègements de la procédure subrogatoire ou des sanctions doivent viser les articles de ces chapitres eux-mêmes ; leur examen n'est pas déclaré achevé par ce maintien.",
    "Aucune charge nouvelle n'est identifiée : le champ des chapitres appliqués aux prestations reste identique ; aucun nouveau dossier ou délai n'est ajouté.")


# Les cibles imposées sont recopiées exclusivement depuis le fichier fourni.
EMPLOYMENT_CONTEXT = {
    'L583-3': "L583-3 régit les données de prestations familiales, le logement et l'intermédiation alimentaire, non la conclusion ou la rupture d'un emploi.",
    'L583-4': "L583-4 transmet un montant d'indemnités AT-MP entre organismes ; la durée d'un emploi et son indemnité de rupture ne sont pas son objet.",
    'L612-2': "L612-2 organise les organes et les mandats du CPSTI ; les références au salariat concernent notamment l'exercice indemnisé de ces mandats.",
    'L612-3': "L612-3 fixe la composition et les représentations du CPSTI, et non la durée du contrat de ses représentants ou des salariés des caisses.",
    'L612-4': "L612-4 règle la représentation régionale, les aides et la médiation sociale des indépendants ; ces missions ne créent pas de CDD.",
    'L612-6': "L612-6 porte sur la représentativité d'organisations, avec un seuil d'audience de 8 % ; son ancienneté est organisationnelle, non salariale.",
    'L613-1': "L613-1 réduit des cotisations familiales d'indépendants et préserve les cumuls énumérés ; il ne détermine pas les droits de rupture d'un salarié.",
    'L613-6-1': "L613-6-1 concerne le précompte des recettes de vendeurs indépendants ou assimilés sociaux ; cette assimilation n'établit pas un contrat de travail.",
}
LABOUR_DETAILS = {
    'L1234-1': "La cible officielle prévoit les paliers de préavis inférieurs à six mois, d'un mois puis deux mois ; sa proposition réserve quinze jours calendaires aux contrats nouveaux et conserve les contrats antérieurs. Aucune de ces durées ne régit ce flux ou ce mandat social ; aucune notification de rupture n'est ajoutée.",
    'L1221-2': "La source autorise certains contrats à terme ; la proposition impose l'indétermination aux emplois privés nouveaux et conserve les contrats antérieurs. Le présent article ne comporte aucun terme d'emploi à convertir ni autorisation de nouveau CDD ; aucune durée de mission n'y est transformée en durée d'emploi.",
    'L1234-9': "La source ouvre l'indemnité après huit mois ; la proposition exige un an au terme effectif, préavis inclus, puis 0,20 mois sur toute l'ancienneté avec fractions en mois complets et plafond de six mois, employeur seul. Ce barème ne s'applique pas à la prestation, au mandat ou à la cotisation ici visés ; les droits anciens et spéciaux restent à leur champ.",
}
SPECIFIC_CHECKS = {
    ('L583-3', 'L821-1'): "La cible fournie est L821-1 du CSS sur l'AAH, alors que le quatrième alinéa de L583-3 vise expressément le a du 2° de L821-1 du code de la construction et de l'habitation, pour une allocation de logement. Il s'agit de deux articles homonymes : ni les conditions d'AAH ni leurs renvois historiques au travail ne doivent remplacer le renvoi CCH, déjà qualifié correctement dans la source. Aucune ancienneté ou notification de rupture ne conditionne ce contrôle locatif.",
    ('L583-4', 'L431-1'): "Le renvoi porte exactement sur le 2° : indemnité journalière d'incapacité temporaire imposant une interruption du travail, avec réserve propre aux pupilles de l'éducation surveillée. Il ne vise ni le capital d'incapacité permanente du 4°, ni les prestations de décès du 3°, ni une indemnité de licenciement. Le maintien de la transmission n'impose aucun préavis ou seuil d'ancienneté ; les prestations et exceptions de L431-1 ne sont pas réécrites.",
    ('L612-2', 'L231-12'): "Le renvoi maintient l'interdiction de traitement des administrateurs, le remboursement des déplacements et des salaires effectivement maintenus pour le mandat, ainsi que les indemnités de perte de gains des indépendants. Source et proposition conservent ces droits. Le salaire maintenu n'est pas une indemnité de rupture L1234-9 : aucun seuil d'un an ni plafond de six mois ne réduit ces remboursements, y compris dans un emploi nouveau éligible.",
    ('L612-2', 'L231-6-1'): "Le renvoi source exclut le a du 5° et le dernier alinéa de L231-6-1, soit le 2° terminal de perte du mandat sur demande de remplacement par l'organisation désignatrice. La proposition de la cible ajoute une transition après ce 2° : le nouveau L612-2 désigne donc explicitement l'objet de cette exception, sans l'étendre au 1° relatif à la cessation d'appartenance. L'exception du a du 5° reste inchangée. La suppression disciplinaire de dix ans de la cible n'est pas une règle d'indemnité de rupture ; aucune ancienneté ou notification salariale ne conditionne ici le remplacement du mandataire.",
    ('L612-3', 'L612-6'): "Les 1° et 2° de L612-3 renvoient aux organisations admises selon les critères et l'audience d'au moins 8 % de L612-6. La proposition de ce lot retire seulement l'attestation spéciale d'adhérents ; elle ne change ni seuil, ni critères, ni nombre de collèges ou de sièges. La déclaration commune patronale reste possible. Les critères d'ancienneté des organisations ne se confondent pas avec l'an d'ancienneté d'un salarié et n'autorisent aucun CDD.",
    ('L612-4', 'L216-5'): "Le quatrième alinéa de L612-4, conservé à sa place, prévoit le représentant consultatif dans les conseils locaux, dont celui de la caisse commune L216-5. Le renvoi réciproque du sixième alinéa de L216-5 à ce quatrième alinéa reste exact ; la proposition de L216-5 conserve ce siège. Ce mandat n'est ni un contrat de mission à terme ni une rupture d'emploi ; aucune ancienneté salariale ou notification de quinze jours n'est pertinente.",
    ('L612-4', 'L213-1'): "Le quatrième alinéa vise le siège consultatif dans l'Urssaf ; le I 9° de L213-1 confie en parallèle l'exécution des décisions régionales d'action sociale. Ces deux règles sont conservées. La proposition de L213-1 retire le recouvrement futur du CPF-CDD et coordonne les anciennes périodes sans supprimer les aides de L612-4. Le préavis d'emploi et l'indemnité d'un an n'encadrent ni l'instruction ni le paiement de ces aides.",
    ('L613-1', 'L131-6-4'): "L613-1 préserve expressément le cumul avec Acre de L131-6-4 ; le III de la cible, officiel comme proposé, le permet réciproquement. Les douze mois d'exonération, les seuils de trois quarts du PASS et du PASS et les conditions propres à la création/reprise ne sont pas des durées d'emploi ou un seuil d'indemnité de rupture. L'avantage demeure ouvert aux nouvelles créations éligibles et n'est pas borné aux anciens contrats.",
    ('L613-6', 'L311-3'): "L613-6 ouvre un mandat facultatif de début d'activité à la plateforme ; le 35° de L311-3 est une affiliation optionnelle distincte pour certaines recettes L611-1, avec abattements de 60 % ou 87 %. Le mandat n'impose ni cette option ni le précompte. La proposition de L311-3 conserve les avantages futurs et précise le contrat unique lorsqu'un véritable emploi privé existe ; elle ne transforme pas tous les indépendants de plateforme en salariés et ne modifie pas ici le calendrier 2027.",
    ('L613-6-1', 'L213-1'): "Le I de L613-6-1 conserve l'Urssaf pour la régularisation lorsque les recettes sont soumises à TVA et le III pour l'organisme local éventuellement désigné de précompte. L213-1 donne les compétences de recouvrement pertinentes ; sa proposition ne permet pas de recouvrer une taxe supprimée, ni le CPF-CDD sur périodes nouvelles. Le choix du précompte ne relève ni d'un préavis salarié ni d'une indemnité de rupture, et les dettes antérieures restent régularisables.",
    ('L613-6-1', 'L311-3'): "Le premier alinéa du I vise exactement le 35° de L311-3, non les autres catégories assimilées : option de régime général sous seuil 102 ter avec assiette de recettes abattues de 60 %, ou 87 % pour la location touristique visée. Source et proposition conservent ces abattements. Le nouveau plafond social de 20 % propre à L613-7 n'est pas appliqué à cette assiette distincte ; le choix de précompte reste accessible à ces futurs éligibles et ne crée pas d'emploi à terme.",
    ('L613-6-1', 'L225-1-1'): "Les II et III de L613-6-1 utilisent Acoss pour l'identification, la déclaration et le versement du précompte. Le 4° de L225-1-1 reçoit les prélèvements de tiers ; le 5° centralise les recouvrements et conserve leur affectation. La proposition n'en fait pas une dette nouvelle ni une résurrection de contribution supprimée. Limiter le précompte au choix du cotisant exige de coordonner ses flux techniques, sans changer les garanties des sommes déjà retenues ou appliquer le barème d'indemnité de rupture.",
}

for s in SOURCES:
    n = s['number']
    req = REFS['requirements'][s['code_id'] + '|' + s['source_id']]
    checks = []
    for key in req:
        t = REFS['targets'][key]
        if t['number'] in LABOUR_DETAILS:
            assessment = EMPLOYMENT_CONTEXT[n] + ' ' + LABOUR_DETAILS[t['number']]
        else:
            assessment = SPECIFIC_CHECKS[(n, t['number'])]
        checks.append(dict(target_key=key, view_sha256=t['view_sha256'], assessment=assessment))
    OUT[n]['reference_checks'] = checks

assert set(OUT) == set(BY_NUMBER)
(ROOT / 'answer.json').write_text(json.dumps([OUT[s['number']] for s in SOURCES], ensure_ascii=False, indent=2) + '\n')
print('answer.json :', len(OUT), 'articles')
