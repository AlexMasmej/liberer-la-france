import json
import re
from html import unescape
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
by_number = {a['number']: a for a in sources}
answers = {}


def base(number, reason, review_notes):
    a = by_number[number]
    return {k: a[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')} | {
        'proposed_xml': None,
        'reason': reason,
        'review_notes': review_notes,
        'status': 'retained_unchanged',
    }


def impact(classification, assessment, scope_limitations, new_burdens_review, effects):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=scope_limitations,
                new_burdens_review=new_burdens_review, effects=effects)


def effect(kind, measure_id, description, before, after, unit, affected_population,
           conditions_and_transition, replacement_or_new_burdens,
           source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit,
                affected_population=affected_population,
                conditions_and_transition=conditions_and_transition,
                replacement_or_new_burdens=replacement_or_new_burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


def retain(number, reason, notes, assessment, limitations, burdens, benefit=None):
    a = base(number, reason, notes)
    a['classification'] = 'retained_necessary'
    a['substantive_impact'] = impact('retained_necessary', assessment,
                                    limitations, burdens, [])
    if benefit:
        a['benefit_review'] = benefit
    answers[number] = a


def rewrite(number, xml, reason, notes, classification, assessment, limitations,
            burdens, effects, removed=None, benefit=None, repeal_scope=None):
    a = base(number, reason, notes)
    a['status'] = 'rewrite_draft'
    a['proposed_xml'] = xml
    a['substantive_impact'] = impact(classification, assessment, limitations,
                                    burdens, effects)
    if removed:
        a.update(change_type='normative_reduction',
                 reform_policy_id='editorial_direction_2026_10_19',
                 removed_provisions=removed)
    if benefit:
        a['benefit_review'] = benefit
    if repeal_scope:
        a.update(change_type='full_repeal',
                 repeal_policy_id='editorial_direction_2026_10_19',
                 repeal_scope=repeal_scope)
    answers[number] = a


def replace_once(number, old, new):
    s = by_number[number]['source_xml']
    assert s.count(old) == 1, (number, old)
    return s.replace(old, new, 1)


retain(
    'R104-31',
    "Maintien intégral après examen : le délai maximal de deux mois, la motivation et l'évaluation exigée en cas de silence encadrent la décision de filtrage environnemental. Supprimer l'examen ou transformer ici le silence en dispense supprimerait une garantie de détection des incidences notables ; aucune charge de formulaire ou transmission doublonnée ne figure dans cet article. Ce maintien ne constitue pas une réécriture.",
    "R. 104-28 à R. 104-30 lus dans le corpus : ce paragraphe concerne la décision de l'autorité environnementale, distincte de l'avis conforme de R. 104-35. Le point de départ est la réception du dossier de R. 104-29, sous réserve du nouveau départ spécialement prévu par R. 104-21 lorsque le ministre confie le dossier à la formation nationale ; les deux mois ne sont pas un délai minimal d'attente après une décision expresse. Cette règle spéciale de transfert, lue mais hors lot, n'est pas supprimée ici. Conserver la note d'application de l'article 26 du décret du 13 octobre 2021 pour les procédures et décisions qu'elle vise. Incohérence préexistante hors lot : R. 104-30 désigne R. 104-32 pour la naissance de la décision implicite, alors que son effet est fixé par R. 104-31 ; renvoi à rectifier dans R. 104-30, non modifié ici. Aucun schéma de plage ni dérogation littorale n'est supprimé.",
    "La source entière est conservée : aucune diminution du délai de deux mois, de l'obligation d'évaluation en cas de silence ou de la motivation n'est revendiquée.",
    "Ne concerne que le filtrage confié à l'autorité environnementale ; l'avis conforme avec silence favorable de R. 104-35 reste un régime distinct. Aucun effet fiscal ou budgétaire n'est établi.",
    "Aucune charge nouvelle n'est identifiée : le texte source reste intégral, sans nouvelle pièce, déclaration, période d'attente ni circuit de consultation."
)

retain(
    'R104-32',
    "Maintien intégral de l'accès public à la décision de filtrage ou à son caractère tacite, de son insertion au dossier de participation et de la mise en ligne par le service régional pour la mission régionale. Ces communications ont des destinataires et fonctions complémentaires : informer le public du fondement de la dispense ou de l'évaluation et rendre l'examen contestable. Aucun dépôt supplémentaire n'est créé par ce maintien.",
    "Version assignée applicable depuis le 5 août 2026, lue en entier. La décision tacite renvoie au silence valant évaluation de R. 104-31 ; elle ne doit pas être confondue avec l'avis tacite favorable de R. 104-35. Les trois voies de participation sont conservées. La seconde phrase désigne l'exécutant de la mise en ligne, sans exiger une seconde publication de même nature.",
    "L'obligation de publicité reste entière, y compris lorsque l'autorité ne répond pas. Elle assure une information et une possibilité de recours utiles, sans nouvelle simplification comptée.",
    "Le maintien porte sur la publicité du filtrage, pas sur une nouvelle évaluation ni sur les formalités des permis. Les autres règles de participation conservent leur propre champ.",
    "Aucune charge nouvelle n'est identifiée : mêmes documents, mêmes destinataires et même service de publication que dans la source, sans registre ou justificatif ajouté."
)

retain(
    'R104-33',
    "Maintien intégral de l'alternative entre évaluation décidée directement par la personne publique et saisine pour avis conforme lorsqu'elle estime l'évaluation inutile. L'avis externe empêche qu'une appréciation du porteur suffise à écarter les incidences notables ; la décision finale identifie la responsabilité et les voies de recours. La liberté de présentation du dossier est allégée dans R. 104-34, sans retirer ce contrôle de fond.",
    "Les cibles R. 104-8, R. 104-10 2°, R. 104-12, R. 104-14 2°, R. 104-16 et R. 104-17-2 ainsi que R. 104-19 à R. 104-27 ont été lues dans le corpus. Respecter leurs exclusions d'erreur matérielle et, pour le PLU, de réduction de zone urbaine ou à urbaniser, ainsi que leurs distinctions Natura 2000 et unités touristiques nouvelles. R. 104-34 et R. 104-35 sont coordonnés dans ce lot ; aucun nouveau filtrage des schémas de plage n'est créé. Le maintien de l'avis conforme ne prétend pas que chaque détail du dispositif serait imposé par la directive 2001/42/CE.",
    "Aucun second circuit n'est créé ni supprimé : la source conserve le choix d'évaluer directement et l'examen indépendant préalable à une décision de ne pas évaluer.",
    "Les exclusions favorables et les évaluations systématiques résultent des articles de champ ; cet article ne les étend ni ne les referme. Aucun gain distinct de celui du formulaire facultatif n'est compté ici.",
    "Aucune charge nouvelle n'est identifiée : maintien des deux branches existantes, sans attestation, confirmation annuelle ou demande additionnelle."
)

form_old = "La liste détaillée des informations devant figurer dans l'exposé est définie dans un formulaire dont le contenu est précisé par arrêté du ministre chargé de l'urbanisme."
form_new = "L'exposé est présenté sur un support librement choisi par la personne publique responsable, permettant sa réception et sa consultation. L'utilisation d'un formulaire ne peut être imposée. Les renseignements exigibles sont limités à ceux nécessaires à la description et à l'exposé prévus aux 1° et 2°. Aucune rubrique d'un formulaire ne peut, à elle seule, justifier une demande d'information supplémentaire."
form_xml = replace_once('R104-34', form_old, form_new)
assert form_xml.count('2° Un exposé décrivant notamment :') == 1
form_xml = form_xml.replace('2° Un exposé décrivant notamment :', '2° Un exposé décrivant :')
form_xml += "\n<p>La liberté de présentation de l'exposé s'applique aux dossiers transmis à compter de l'entrée en vigueur de la loi portant la présente réforme. Pour les dossiers déjà transmis, la personne publique responsable peut en bénéficier pour les compléments restant à fournir, sans nouveau dépôt des pièces déjà transmises ni reprise des délais. Les formulaires déjà transmis demeurent recevables. Les actes antérieurement pris et les règles d'application dans le temps prévues à l'article 26 du décret n° 2021-1345 du 13 octobre 2021 ne sont pas remis en cause.</p>"
rewrite(
    'R104-34', form_xml,
    "Réduction de fond : retrait du caractère prescriptif de la liste détaillée d'informations définie par formulaire ministériel et du caractère indéterminé de l'énumération introduite par notamment. Les renseignements exigibles sont limités aux besoins de la description et de l'exposé de l'article ; une rubrique de formulaire ne suffit plus à justifier une demande supplémentaire. La présentation devient expressément libre. Le corps complet conserve les 1°, 2°, a à d, le renvoi aux 2°, 3° et 5° du I de R. 122-14, tous les critères environnementaux de l'annexe II de la directive et la proportionnalité aux enjeux. Ni dispense d'examen, ni déclaration de remplacement.",
    "Coordination effectuée dans R. 104-35 : publier l'exposé motivant l'absence d'incidences en cas d'avis tacite, au lieu de rendre le formulaire à nouveau obligatoire. R. 122-14 I et II lus en entier ; leurs pièces et distinctions restent inchangées. L'arrêté ministériel fixant le contenu du formulaire prévu par le dernier alinéa de la source de R. 104-34, ainsi que son annexe, doivent être coordonnés pour que leur usage soit facultatif ; leur texte n'étant pas fourni, aucune date, rubrique précise ou lecture intégrale de cet arrêté n'est affirmée. Le maintien des informations utiles ne garantit pas une réduction de leur volume dans chaque dossier. Transition expresse pour nouveaux envois et compléments des dossiers en cours, sans réinitialisation et sans altération de la note de 2021. Mise en œuvre réglementaire à coordonner avec l'entrée en vigueur de la loi de réforme.",
    'material_reduction',
    "La source renvoyait à une liste détaillée obligatoire définie dans un formulaire et à une énumération non limitative. La proposition retire ce fondement aux demandes sans nécessité environnementale et rend le formulaire facultatif. Elle ne prouve pas que la source interdisait déjà toute autre présentation matérielle.",
    "Le contenu de l'arrêté et de son annexe n'est pas joint : aucune rubrique précise supprimée ni économie par dossier n'est démontrée. Les renseignements nécessaires à tous les critères européens, les compléments utiles, avis et droits de participation restent exigibles.",
    "Aucune charge nouvelle n'est identifiée : l'exposé et sa consultation existaient déjà ; aucun nouveau justificatif, certificat ou délai ne remplace le formulaire. La transition dispense expressément de refaire les dépôts acquis.",
    [effect(
        'obligation_removed', 'urbanisme-examen-environnemental-formulaire-facultatif',
        "Retrait du fondement réglementaire des renseignements imposés par la seule liste détaillée d'un formulaire, avec maintien de toutes les informations environnementales nécessaires.",
        "La source définit la liste détaillée des informations par un formulaire fixé par arrêté et introduit l'exposé par notamment ; l'exclusivité matérielle du support n'est pas démontrée par ce seul texte.",
        "Les renseignements sont limités aux besoins des 1° et 2° a à d, le formulaire est facultatif et sa seule rubrique ne fonde plus de demande supplémentaire.",
        'legal_duty', "Personnes publiques responsables relevant du second alinéa de R. 104-33.",
        "Nouveaux dossiers après entrée en vigueur de la loi ; option pour les compléments restant dus des dossiers en cours, sans nouveau dépôt ni nouveau départ des délais.",
        "Dossier, critères d'incidences et avis conforme maintenus ; aucune nouvelle déclaration ni attestation de remplacement.",
        form_old, "Aucune rubrique d'un formulaire ne peut, à elle seule, justifier une demande d'information supplémentaire."
    )],
    removed=["Caractère prescriptif de la liste détaillée d'informations définie par le formulaire ministériel et faculté d'exiger des rubriques sans nécessité pour la description et l'exposé environnemental de l'article."]
)

pub_old = "le formulaire mentionné à l'article R. 104-34"
pub_new = "l'exposé mentionné au 2° de l'article R. 104-34, quelle que soit sa présentation,"
rewrite(
    'R104-35', replace_once('R104-35', pub_old, pub_new),
    "Coordination nécessaire du formulaire facultatif : en cas de silence favorable, l'exposé effectivement soumis à l'autorité environnementale est publié et joint au dossier de participation, quelle que soit sa présentation. Les quatre alinéas sont conservés intégralement pour le surplus : saisine précoce, accusé de réception, quinze jours pour réclamer les compléments, consultation sanitaire facultative avec dix jours ouvrés au moins, avis conforme sous deux mois à compter de la réception initiale et silence favorable. Aucune seconde réduction de formalité n'est imputée à cet article.",
    "Même mesure que R. 104-34, sans nouvelle obligation de publier une autre catégorie d'information : le formulaire source portait déjà l'exposé. Les dossiers transmis avant la réforme et les formulaires déjà utilisés demeurent valables ; leur exposé reste publiable en application de cette rédaction. Ne pas déplacer le départ des deux mois à la date des compléments ni confondre les quinze jours de complétude avec un préavis de travail. La publicité de l'avis exprès est inchangée ; le silence conserve l'obligation de publier les motifs du porteur. Les autorités compétentes et la référence à R. 104-21 sont maintenues ; les cibles ont été lues dans le corpus.",
    'coordination_only',
    "Le renvoi au formulaire devient un renvoi à son contenu environnemental. Cette coordination empêche de rétablir le support imposé par la règle de publicité ; ni le contrôle ni les délais ne sont réduits une seconde fois.",
    "Le gain est porté une seule fois par R. 104-34. Aucun raccourcissement de l'instruction ni économie sur l'évaluation ou la consultation sanitaire n'est démontré par R. 104-35.",
    "Aucune charge nouvelle n'est identifiée : même exposé et mêmes destinataires qu'auparavant ; aucune publication supplémentaire, donnée nouvelle ou condition de dispense n'est ajoutée.",
    [effect(
        'coordination', 'urbanisme-examen-environnemental-formulaire-facultatif',
        "Maintien de la publicité des motifs du porteur sans rétablir le formulaire obligatoire.",
        "En cas d'avis tacite, le formulaire de R. 104-34 est publié et joint au dossier de participation.",
        "Dans le même cas, l'exposé de R. 104-34 est publié et joint, sur son support librement choisi.",
        'legal_duty', "Autorité environnementale et personnes publiques responsables des dossiers de R. 104-34.",
        "Même champ de publicité, y compris les dossiers sur formulaire déjà transmis ; application coordonnée à la faculté de présentation de R. 104-34.",
        "Aucune nouvelle publication ni dispense d'information du public ; contenu motivant le silence favorable conservé.",
        "L'avis ou la mention de son caractère tacite, ainsi que, dans ce dernier cas, le formulaire mentionné à l'article R. 104-34 sont mis en ligne sur le site internet de l'autorité environnementale et joints au dossier d'enquête publique, de participation du public par voie électronique ou de mise à disposition du public.",
        "L'avis ou la mention de son caractère tacite, ainsi que, dans ce dernier cas, l'exposé mentionné au 2° de l'article R. 104-34, quelle que soit sa présentation, sont mis en ligne sur le site internet de l'autorité environnementale et joints au dossier d'enquête publique, de participation du public par voie électronique ou de mise à disposition du public."
    )]
)

competence_old = "le conseil de territoire mentionné à l'article L. 134-13"
competence_new = "le conseil de territoire de l'établissement public territorial compétent mentionné à l'article L. 134-2"
rewrite(
    'R104-36', replace_once('R104-36', competence_old, competence_new),
    "Coordination de compétence, sans simplification matérielle revendiquée : remplacement du renvoi non retrouvé à L. 134-13 par la désignation du conseil de territoire de l'établissement public territorial compétent, fondée sur L. 134-2 et la fonction de son conseil documentée à L. 134-4. Les 1° à 4° et leurs autres renvois sont conservés. L'identification de l'organe élu qui assume la décision environnementale reste nécessaire ; elle n'ajoute pas un agrément au dossier.",
    "Incohérence documentaire préexistante signalée : L. 134-13 est absent du corpus fourni, alors que la source assignée de R. 104-36, datée du 5 août 2026, le vise encore. Les sources de L. 134-2 et L. 134-4 décrivent les établissements publics territoriaux du Grand Paris et leur conseil ; L. 134-11 et L. 134-12 décrivent le régime de la métropole d'Aix-Marseille-Provence. La correction identifie les organes actuellement compétents, sans faire revivre un conseil d'Aix-Marseille ni transférer de compétence de la métropole. La chronologie exacte de disparition de L. 134-13 n'est pas établie par les pièces locales : ne pas présenter cette concordance comme une filiation historique achevée. L. 143-16, L. 153-8, L. 163-3, R. 143-11, R. 153-15 et R. 122-13 ont été lus. Les décisions antérieures ne sont pas invalidées par cette coordination de référence.",
    'coordination_only',
    "La proposition corrige une référence de compétence absente du corpus ; elle conserve la décision des organes délibérants, sans compter comme suppression la simple clarification du conseil compétent.",
    "La filiation et la date exacte de disparition de L. 134-13 restent à documenter hors des pièces fournies. Aucun changement de répartition territoriale ni gain de délai n'est démontré.",
    "Aucune charge nouvelle n'est identifiée : les quatre catégories de décisions restent prises par l'organe délibérant compétent, sans saisine, rapport ou vote supplémentaire.",
    [effect(
        'coordination', 'urbanisme-evaluation-organe-deliberant-competent',
        "Remplacement d'une référence de compétence non retrouvée par la désignation de l'établissement public territorial compétent.",
        "Le 2° désigne un conseil de territoire par un renvoi à L. 134-13, absent du corpus fourni.",
        "Le 2° désigne le conseil de territoire de l'établissement public territorial compétent selon L. 134-2, sans modifier les autres autorités.",
        'other', "Collectivités et établissements publics décidant de réaliser ou non une évaluation des évolutions du PLU.",
        "Application selon les compétences légales en vigueur ; aucune remise en cause des décisions antérieures ni reconstitution d'une compétence disparue.",
        "Même décision délibérante ; aucune procédure de remplacement et aucune compétence nouvelle attribuée.",
        competence_old, competence_new
    )]
)

retain(
    'R104-37',
    "Maintien intégral de la motivation et de la publicité de la décision de réaliser ou non l'évaluation. Elles permettent au public de comprendre la dispense et d'en contester les motifs ; elles ne doublonnent pas l'avis environnemental, qui n'est pas la décision de la personne publique. Le renvoi aux régimes existants de publicité évite un circuit propre supplémentaire.",
    "R. 143-15, R. 153-21 et R. 163-9 ont été lus en entier : publicité des décisions concernant respectivement SCOT, PLU et carte communale ; R. 153-21 est étendu expressément aux unités touristiques nouvelles. Conserver la note transitoire de l'article 26 du décret de 2021. L'allègement de support dans R. 104-34 ne retire pas la motivation de la décision, dont la publicité reste distincte de celle de l'avis de R. 104-35. Aucune filiation SRU n'est déduite de ces seuls numéros.",
    "Le texte source demeure intégral : la motivation et la publicité restent des garanties de transparence de la dispense comme de l'évaluation ; aucune formalité supprimée n'est annoncée.",
    "Ne modifie pas les publicités des actes d'urbanisme elles-mêmes, qui ont un champ autonome. Aucune réduction du nombre de consultations ou des délais de recours n'est établie.",
    "Aucune charge nouvelle n'est identifiée : le maintien utilise les mêmes règles de publication, sans déclaration ou pièce attestant une nouvelle fois l'avis déjà rendu."
)

retain(
    'R104-38',
    "Maintien intégral d'une faculté favorable déjà existante : les procédures communes et coordonnées d'évaluation évitent des études séparées lorsque leurs conditions sont réunies. L'exigence que l'étude du projet couvre tous les éléments du rapport du document protège l'exhaustivité environnementale ; la retirer transformerait une mutualisation en dispense de contenu non décidée. Aucune nouvelle fusion n'est revendiquée.",
    "L. 104-1, L. 104-2, L. 104-2-1 et R. 104-18 lus dans le corpus ; le 3° de L. 104-2 conserve les schémas de plage et leurs facultés futures. Les renvois à environnement R. 122-25, R. 122-26, R. 122-26-1 et R. 122-27 sont maintenus : les sources de ce code ne figurent pas dans le corpus autorisé des cinq codes, leur détail n'est donc pas présenté comme vérifié intégralement. La note transitoire de l'article 26 du décret de 2021 reste applicable. Cette faculté n'est pas une obligation générale de dossier unique.",
    "La source permet déjà de coordonner ou de réunir des évaluations ; son maintien protège cet avantage sans compter une fusion supplémentaire ni supprimer les informations environnementales exigibles.",
    "L'usage des procédures dépend des conditions propres du code de l'environnement, dont les textes ne sont pas fournis. Aucun nombre d'études évitées ni coût national n'est établi.",
    "Aucune charge nouvelle n'est identifiée : la mutualisation reste facultative et son exigence de contenu existait déjà ; aucune attestation d'éligibilité supplémentaire n'est créée."
)

retain(
    'R104-39',
    "Maintien intégral des informations après adoption : mise à disposition du document, prise en compte des consultations, motifs des choix et solutions envisagées, y compris pour les autorités transfrontalières et les unités touristiques nouvelles. Le second alinéa réutilise déjà les formalités de publicité des actes ; une nouvelle fusion ne serait donc pas un gain. Ces obligations assurent transparence et contrôle de l'évaluation réalisée.",
    "L. 104-7 et R. 122-17 lus : information des autorités consultées et motivation de l'arrêté des unités touristiques nouvelles, avec renvoi réciproque au dernier alinéa de R. 104-39. Les deux articles distinguent bien publication et motivation. Les sources de L. 104-1, L. 104-2 et L. 104-2-1 maintiennent leur champ, notamment les schémas de plage ; aucune fermeture de leur évaluation ni de leur dérogation favorable. Conserver la note d'application du décret de 2021. L'obligation européenne d'information après décision est conservée, sans déclarer tous les détails de publicité nationalement incompressibles.",
    "Le contenu complet reste applicable : il documente les choix environnementaux après adoption. Aucun rapport supplémentaire ni allègement fictif d'une publicité déjà commune n'est compté.",
    "Ce maintien ne modifie ni les choix d'aménagement, ni la procédure européenne de consultation, ni les voies de recours. Aucune économie budgétaire ou réduction de délai n'est démontrée.",
    "Aucune charge nouvelle n'est identifiée : les mêmes informations sont fournies dans les formalités déjà prévues, sans nouvel état annuel, registre ou justificatif."
)

distance_measure = 'urbanisme-distance-interne-trois-metres-suppression'
exclusion_old = "R. 111-3, R. 111-5 à R. 111-19 et R. 111-28 à R. 111-30"
exclusion_new = "R. 111-3, R. 111-5 à R. 111-14, R. 111-16 à R. 111-19 et R. 111-28 à R. 111-30"
rewrite(
    'R111-1', replace_once('R111-1', exclusion_old, exclusion_new),
    "Coordination de l'abrogation de R. 111-15 : la liste des dispositions écartées dans les territoires couverts par un PLU ne comprend plus la règle de distance abrogée. Les autres exclusions territoriales, le champ général du règlement national et la faculté de lexique national restent exactement ceux de la source. Aucune extension du RNU aux territoires couverts par un PLU n'est créée et aucune seconde règle de distance n'est supprimée ici.",
    "Même mesure que R. 111-15, non une réduction autonome. Conserver l'exclusion de R. 111-3 et toutes celles de R. 111-5 à R. 111-14, de R. 111-16 à R. 111-19 et de R. 111-28 à R. 111-30, pour les PLU comme pour les documents en tenant lieu. R. 111-19 et R. 151-19, lus dans le corpus mais hors lot, doivent retirer R. 111-15 de leurs intervalles sans supprimer les dérogations aux autres distances ou les options des PLUi. Les prescriptions locales autonomes ne disparaissent pas par cette seule coordination.",
    'coordination_only',
    "Seule la plage de références est adaptée à la disparition de R. 111-15. Les exclusions favorables au bénéfice des territoires dotés d'un PLU restent intégrales ; aucun nouvel allègement distinct n'est compté.",
    "La disparition de la distance nationale ne supprime pas les règles locales qui auraient un fondement autonome. Les coordinations de R. 111-19 et R. 151-19 sont identifiées hors lot et non déclarées rédigées.",
    "Aucune charge nouvelle n'est identifiée : champ, autorisations concernées, faculté de lexique et toutes les autres exclusions demeurent ceux de la source.",
    [effect(
        'coordination', distance_measure,
        "Retrait de la référence à la distance abrogée dans la liste des exclusions territoriales du RNU.",
        "La plage R. 111-5 à R. 111-19 comprend la règle de distance interne de R. 111-15.",
        "La même exclusion est répartie en R. 111-5 à R. 111-14 et R. 111-16 à R. 111-19 ; les règles applicables restantes ne changent pas.",
        'other', "Constructions et aménagements dans les territoires dotés d'un PLU ou d'un document en tenant lieu.",
        "Coordination à l'entrée en vigueur de l'abrogation de R. 111-15, sans remettre en cause les titres antérieurs.",
        "Aucune obligation ajoutée et aucune seconde suppression de distance ; les règles locales autonomes subsistent.",
        exclusion_old, exclusion_new
    )]
)

retain(
    'R111-2',
    "Maintien intégral du pouvoir de refus ou de prescriptions contre les atteintes à la salubrité et à la sécurité publiques. Il s'agit d'une garantie essentielle couvrant situation, caractéristiques, importance et proximité d'autres installations, y compris dans les territoires à PLU. L'abrogation de la distance forfaitaire de R. 111-15 ne doit pas supprimer le traitement d'un risque réel d'incendie ou d'insalubrité. Aucun dossier propre supplémentaire n'est institué par cet article.",
    "R. 111-1 maintient l'applicabilité de R. 111-2 dans les territoires dotés d'un PLU. Conserver les quatre facteurs de risque et l'alternative entre prescriptions et refus. Ni la suppression de trois mètres entre bâtiments d'un même propriétaire ni les allègements d'eau et d'assainissement ne neutralisent cette clause. L. 111-11, lu, conserve séparément la desserte effective par les réseaux nécessaires.",
    "La source entière demeure une protection contre les risques publics. Aucun agrément ni taxe n'y est supprimé, et son maintien ne vaut pas création d'une nouvelle autorisation.",
    "Les prescriptions doivent rester liées à la salubrité ou à la sécurité du projet ; cet examen ne chiffre pas leur coût ni ne conclut à un solde global de contraintes.",
    "Aucune charge nouvelle n'est identifiée : même faculté de prescriptions et de refus, mêmes facteurs de risque, aucune attestation ou donnée additionnelle."
)

retain(
    'R111-3',
    "Maintien intégral de la protection contre l'exposition à des nuisances graves, notamment au bruit. Son seuil de gravité et son lien avec la localisation distinguent cette règle d'une restriction de simple confort ; elle protège la santé et les futurs occupants. Elle permet déjà des prescriptions au lieu d'un refus. Aucune formalité autonome, délai minimal ou prélèvement n'est à supprimer dans cet article.",
    "L'exclusion dans les territoires à PLU ou document en tenant lieu est conservée par R. 111-1. Le caractère non exhaustif du bruit parmi les nuisances graves reste entier ; ne pas limiter silencieusement la protection au bruit. L'articulation avec les normes acoustiques d'autres codes n'est pas présentée comme une identité de champ ou une duplication prouvée.",
    "Aucun changement normatif : la protection contre des nuisances graves est intégralement maintenue après examen de son seuil, de son champ et de la faculté de prescriptions adaptées.",
    "Ne porte pas sur les nuisances ordinaires ni sur un nouveau standard acoustique. Aucun doublon de portée identique n'est démontré dans les textes fournis.",
    "Aucune charge nouvelle n'est identifiée : maintien du même examen dans la procédure d'urbanisme, sans pièce acoustique supplémentaire créée par le présent lot."
)

retain(
    'R111-4',
    "Maintien intégral de la protection des sites et vestiges archéologiques contre un projet qui en compromet la conservation ou la mise en valeur. Les prescriptions possibles permettent d'adapter le projet ; le refus n'est pas une interdiction générale de construire. Les dommages au patrimoine pouvant être irréversibles, aucun doublon intégral avec une autorisation archéologique distincte n'est établi par les pièces locales et ne justifie une abrogation aveugle.",
    "R. 111-1 ne soustrait pas les territoires à PLU à cette protection. Conserver les deux objets, conservation et mise en valeur, ainsi que la double prise en compte de la localisation et des caractéristiques. Le code du patrimoine n'est pas fourni ; aucune conclusion d'exhaustivité ou de redondance avec ses procédures n'est formulée. Aucun renvoi ni chiffre de cet article n'est modifié.",
    "La règle source est maintenue pour prévenir des atteintes archéologiques irréversibles ; l'examen n'a pas établi de procédure doublonnée pouvant être retirée sans perte de cette fonction.",
    "La portée des procédures du code du patrimoine n'est pas vérifiée dans ce corpus. Le maintien n'est pas compté comme simplification et ne prouve pas un coût net favorable.",
    "Aucune charge nouvelle n'est identifiée : la source n'est pas réécrite et aucune étude, saisine ou autorisation archéologique supplémentaire n'est ajoutée."
)

retain(
    'R111-5',
    "Maintien intégral des conditions de desserte, d'accès des engins d'incendie et de sécurité des usagers des voies et accès. Ces exigences ont une fonction essentielle de secours et de prévention des accidents. Leur appréciation tient déjà compte de la position et de la configuration des accès ainsi que de la nature et de l'intensité du trafic ; la suppression de ces critères affaiblirait le contrôle plutôt qu'elle ne supprimerait une pièce redondante.",
    "R. 111-6, lu dans le lot, vise précisément le deuxième alinéa de R. 111-5 : conserver la séparation entre desserte générale et sécurité des accès. Les deux alinéas et tous leurs facteurs d'appréciation restent inchangés. L'exclusion territoriale de R. 111-1 demeure. La règle n'impose pas dans tous les cas une voie publique plutôt qu'une voie privée.",
    "Aucun changement par rapport à la source complète : les voies publiques ou privées restent admises et les contraintes sont rattachées à la desserte et aux risques de circulation ou d'incendie.",
    "Le maintien ne fixe pas de nouvelle largeur de voie ni de norme nationale d'engin. Aucun coût de travaux ni doublon avec les autres règles de sécurité n'est quantifié.",
    "Aucune charge nouvelle n'est identifiée : mêmes critères de desserte et mêmes facultés de refus ou prescriptions, sans nouvel avis de conformité ou attestation."
)

retain(
    'R111-6',
    "Maintien intégral des aménagements et limitations d'accès nécessaires à la sécurité de R. 111-5, deuxième alinéa. La première phrase exige déjà cette nécessité ; la limitation du nombre d'accès et le choix de la voie la moins gênante s'inscrivent dans l'intérêt de la sécurité explicitement posé. Réécrire cette dernière phrase sans démontrer un changement de portée serait un gain fictif. Aucun pouvoir de participation financière autonome n'est ajouté.",
    "R. 111-5 et R. 111-1 lus : l'exclusion des territoires dotés d'un PLU subsiste. La réalisation possible de voies privées et d'autres aménagements particuliers est maintenue seulement dans le champ de sécurité fixé par le texte. Ne pas confondre prescriptions matérielles de sécurité et participations financières postérieures aux permis de L. 424-6, qui relèvent d'une réforme distincte.",
    "La source entière conserve des mesures de prévention des accidents ; aucune suppression supplémentaire n'est revendiquée en renommant une proportionnalité déjà exigée par le texte.",
    "Les coûts des aménagements dépendent du risque et du projet. Le maintien n'établit ni gain budgétaire, ni absence de toute contrainte dans les secteurs à PLU soumis à leurs règles propres.",
    "Aucune charge nouvelle n'est identifiée : aucun aménagement, information ou contrôle supplémentaire par rapport aux trois phrases de la source."
)

play_source = "Lorsque le projet prévoit des bâtiments à usage d'habitation, l'autorité compétente mentionnée aux articles L. 422-1 à L. 422-3 peut exiger la réalisation, par le constructeur, d'aires de jeux et de loisirs situées à proximité de ces logements et correspondant à leur importance."
play_proposed = "La réalisation d'aires de jeux et de loisirs ne peut être imposée au constructeur sur le seul fondement du présent article."
play_xml = replace_once('R111-7', play_source, play_proposed)
play_xml += "\n<p>Cette suppression s'applique aux décisions prises à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris sur les demandes en cours, sans nouveau dépôt ni reprise des délais. Les prescriptions des autorisations régulièrement délivrées et les engagements contractuels valablement conclus avant cette date conservent leur régime et leurs voies de modification et de recours.</p>"
rewrite(
    'R111-7', play_xml,
    "Réduction de fond : retrait du pouvoir d'imposer au constructeur d'habitations des aires de jeux et de loisirs sur ce fondement général, sans besoin de sécurité démontré. La possibilité d'imposer le maintien ou la création d'espaces verts proportionnés au projet est intégralement conservée pour sa fonction environnementale et de qualité du cadre de vie. Aucune déclaration, contribution ou obligation de financement de remplacement n'est créée.",
    "Les articles L. 422-1 à L. 422-3 sur l'autorité d'urbanisme ont été lus ; le renvoi propre à l'obligation supprimée disparaît de ce corps sans modifier ces compétences. L'exclusion territoriale de R. 111-1 est conservée, sous réserve des renvois autonomes des PLUi de R. 151-19, lu. Les règles locales, conventions et équipements reposant sur un fondement autonome ne sont pas abolis. Les équipements antérieurs prescrits et contrats valables gardent leur régime ; pas de remboursement ou démolition générale. Coût des équipements publics éventuellement choisis à établir séparément, sans obligation de substitution instituée.",
    'material_reduction',
    "La source permettait d'ajouter une réalisation matérielle à la charge du constructeur d'habitations. Ce pouvoir national est retiré pour les décisions futures ; les espaces verts et les prescriptions antérieures restent protégés.",
    "La suppression ne vaut pas retrait de toute règle locale ni économie certaine pour chaque opération. Un éventuel choix public de créer des aires n'est ni financé ni chiffré par cet article.",
    "Aucune charge nouvelle n'est identifiée : aucun versement, réserve foncière, attestation ou équipement équivalent ne remplace les aires supprimées ; les espaces verts étaient déjà prévus.",
    [effect(
        'obligation_removed', 'urbanisme-aires-jeux-loisirs-fin-obligation-constructeur',
        "Suppression du pouvoir national d'imposer la réalisation d'aires de jeux et de loisirs au constructeur de logements.",
        "Une prescription pouvait obliger le constructeur d'habitations à réaliser à proximité des aires de jeux et de loisirs proportionnées aux logements.",
        "Aucune prescription de réalisation de ces aires ne peut reposer sur R. 111-7 ; la faculté relative aux espaces verts reste entière.",
        'legal_duty', "Constructeurs de bâtiments d'habitation auxquels R. 111-7 est applicable, dans son champ territorial et ses renvois autonomes.",
        "Décisions postérieures à l'entrée en vigueur de la loi, y compris demandes pendantes ; prescriptions et contrats valables antérieurs conservent leur régime.",
        "Aucune contribution ou déclaration équivalente ; les fondements locaux et contractuels distincts ne sont pas supprimés.",
        play_source, play_proposed
    )],
    removed=["Pouvoir d'imposer au constructeur d'habitations la réalisation d'aires de jeux et de loisirs sur le seul fondement national de R. 111-7."]
)

retain(
    'R111-8',
    "Maintien intégral des obligations de résultat en eau potable, eaux usées domestiques, eaux pluviales et de ruissellement, eaux résiduaires industrielles, conformément aux règlements applicables. Ce socle protège la salubrité, la ressource en eau et les tiers. Il n'impose pas lui-même un dossier, un équipement collectif uniforme ou une autorisation supplémentaire ; l'allègement des modalités techniques de R. 111-10 et des dérogations de R. 111-11 reste compatible avec lui.",
    "Ne supprimer aucune des quatre familles d'eau ni les étapes d'évacuation, d'épuration et de rejet industriel. R. 111-9 à R. 111-12 lus intégralement ; les solutions individuelles et les mélanges autorisés dans leurs conditions sanitaires restent accessibles aux futures situations éligibles. L'exclusion territoriale de R. 111-1 demeure, sans abolir les règlements sanitaires autonomes dans les territoires couverts par un PLU.",
    "Le socle sanitaire et environnemental de la source est conservé sans changement. Les simplifications de technique ou de dérogation interviennent dans les articles qui les imposent réellement.",
    "Ce maintien ne prétend pas avoir réécrit tous les règlements sanitaires visés ni réduit les coûts des réseaux. Aucun nouveau prélèvement ou économie nationale n'est identifié.",
    "Aucune charge nouvelle n'est identifiée : les mêmes obligations de résultat et le même renvoi aux règlements subsistent, sans demande documentaire nouvelle."
)

retain(
    'R111-9',
    "Maintien intégral de la desserte des bâtiments d'habitation par une distribution d'eau potable sous pression raccordée aux réseaux publics. Sa fonction sanitaire ne justifie pas de la supprimer avec les contraintes de configuration inutiles. Les solutions en absence de réseau de R. 111-10 et les dérogations favorables de R. 111-11, désormais de droit lorsque leurs conditions sont réunies, demeurent l'articulation du dispositif ; ce maintien n'institue pas un raccordement impossible.",
    "Lire conjointement R. 111-8, R. 111-10 et R. 111-11, tous examinés dans ce lot, et L. 111-11, lu dans le corpus. Le champ est celui des bâtiments d'habitation ; ne pas l'étendre à tout aménagement ou supprimer les conditions sanitaires des solutions dérogatoires. L'exclusion territoriale de R. 111-1 demeure. Les obligations distinctes du code de la santé publique ne sont pas réputées abrogées par les allègements de R. 111-10.",
    "Le principe de desserte de la source reste inchangé, dans son articulation existante avec l'absence de réseau et les dérogations sanitaires conservées. Aucun gain distinct n'est attribué à ce maintien.",
    "Ne décide pas la construction d'un réseau public ni une nouvelle participation de ses usagers. Les régimes de raccordement d'autres codes restent hors de cette réécriture.",
    "Aucune charge nouvelle n'est identifiée : même desserte de principe pour l'habitation, sans certificat, autorisation ou nouvelle condition de dérogation."
)

water_one_source = "En l'absence de réseau public de distribution d'eau potable et sous réserve que l'hygiène générale et la protection sanitaire soient assurées, l'alimentation est assurée par un seul point d'eau ou, en cas d'impossibilité, par le plus petit nombre possible de points d'eau."
water_one_proposed = "En l'absence de réseau public de distribution d'eau potable et sous réserve que l'hygiène générale et la protection sanitaire soient assurées, l'alimentation est assurée par un ou plusieurs points d'eau."
water_connection_source = "En outre, les installations collectives sont établies de manière à pouvoir se raccorder ultérieurement aux réseaux publics."
water_connection_proposed = "Les installations collectives sont établies de manière à pouvoir se raccorder ultérieurement aux réseaux publics existants. En l'absence de réseau public, la possibilité d'un raccordement ultérieur ne peut être exigée sur le seul fondement du présent article."
water_xml = replace_once('R111-10', water_one_source, water_one_proposed)
assert water_xml.count(water_connection_source) == 1
water_xml = water_xml.replace(water_connection_source, water_connection_proposed)
water_xml += "\n<p>Ces dispositions s'appliquent aux décisions prises à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris aux demandes en cours sans nouveau dépôt ni reprise des délais. Elles ne remettent pas en cause les prescriptions des autorisations antérieurement délivrées ni les obligations de raccordement fondées sur d'autres dispositions.</p>"
rewrite(
    'R111-10', water_xml,
    "Deux réductions de fond : suppression de la règle du point d'eau unique ou du nombre minimal à justifier par une impossibilité, puis retrait de l'obligation générale d'anticiper un raccordement à un réseau public absent. L'alimentation demeure obligatoire ; la protection sanitaire et l'hygiène générale restent exigées pour tous les points. La raccordabilité des installations collectives aux réseaux publics existants et les prescriptions techniques d'assainissement non collectif visées par R. 2224-17 du CGCT sont conservées. La possibilité d'utiliser une alimentation autonome sans réseau est maintenue, sans nouvelle autorisation de remplacement.",
    "Articulation vérifiée avec les sources R. 111-8, R. 111-9, R. 111-11 et L. 111-11. Le renvoi de l'assainissement à CGCT R. 2224-17 est repris sans modification ; ce texte n'est pas fourni dans le corpus autorisé et son contenu n'est pas déclaré vérifié intégralement. Les normes techniques et obligations autonomes peuvent conserver des prescriptions de raccordabilité : la suppression revendiquée est celle du fondement général propre à R. 111-10, pas de toute règle future de raccordement. Conserver les prescriptions des autorisations antérieures et les recours. Ni multiplication de points insalubres ni déversement sans traitement n'est autorisé.",
    'material_reduction',
    "La source entière imposait une minimisation du nombre de points d'eau et une conception raccordable même sans réseau présent. Ces deux contraintes propres à l'article sont retirées, tout en gardant le résultat sanitaire et les prescriptions d'assainissement.",
    "Les obligations techniques indépendantes, dont celles du CGCT et du code de la santé publique non fournis, ne sont pas abolies. Le coût évité dépend du projet et n'est pas établi globalement.",
    "Aucune charge nouvelle n'est identifiée : aucun agrément, registre des points d'eau ou attestation de remplacement n'est créé ; hygiène, potabilité et prescriptions techniques étaient déjà exigées.",
    [effect(
        'obligation_removed', 'urbanisme-alimentation-eau-fin-point-unique',
        "Suppression de la contrainte du point d'eau unique et de la justification d'impossibilité pour en prévoir plusieurs.",
        "En l'absence de réseau public potable : un seul point, ou le plus petit nombre possible seulement en cas d'impossibilité.",
        "Un ou plusieurs points sont admis, sous les mêmes conditions d'hygiène et de protection sanitaire, sans minimisation imposée par cet article.",
        'legal_duty', "Projets soumis à R. 111-10 dans les secteurs sans réseau public de distribution d'eau potable.",
        "Décisions après entrée en vigueur de la loi, y compris demandes en cours ; prescriptions des autorisations antérieures préservées.",
        "Aucune déclaration équivalente ; règlements sanitaires et contrôles autonomes conservés.",
        water_one_source, water_one_proposed
    ), effect(
        'obligation_removed', 'urbanisme-reseaux-absents-fin-raccordabilite-generale',
        "Retrait de l'obligation générale de concevoir les installations collectives pour un hypothétique réseau ultérieur.",
        "Les installations collectives devaient permettre un raccordement ultérieur aux réseaux publics, même en leur absence.",
        "Cette anticipation ne peut être exigée au seul titre de R. 111-10 ; les obligations autonomes de raccordement restent applicables.",
        'legal_duty', "Maîtres d'ouvrage d'installations collectives relevant de R. 111-10 sans réseau public.",
        "Décisions après entrée en vigueur de la loi et dossiers en cours sans reprise des délais ; autorisations antérieures préservées.",
        "Aucune obligation technique de substitution créée ; les prescriptions d'assainissement et la sécurité de l'alimentation restent.",
        water_connection_source, water_connection_proposed
    )],
    removed=[
        "Obligation d'un point d'eau unique ou du plus petit nombre possible et condition d'impossibilité pour s'en écarter en absence de réseau public.",
        "Obligation générale propre à cet article de préparer les installations collectives au raccordement futur à un réseau public absent."
    ]
)

water_relief_source = "Des dérogations à l'obligation de réaliser des installations collectives de distribution d'eau potable peuvent être accordées à titre exceptionnel, lorsque la grande superficie des parcelles ou la faible densité de construction ainsi que la facilité d'alimentation individuelle font apparaître celle-ci comme nettement plus économique, mais à la condition que la potabilité de l'eau et sa protection contre tout risque de pollution puissent être considérées comme assurées."
water_relief_proposed = "L'obligation de réaliser des installations collectives de distribution d'eau potable ne s'applique pas lorsque la grande superficie des parcelles ou la faible densité de construction ainsi que la facilité d'alimentation individuelle font apparaître celle-ci comme nettement plus économique, mais à la condition que la potabilité de l'eau et sa protection contre tout risque de pollution puissent être considérées comme assurées."
sanitation_relief_source = "Des dérogations à l'obligation de réaliser des installations collectives peuvent être accordées pour l'assainissement lorsque, en raison de la grande superficie des parcelles ou de la faible densité de construction, ainsi que de la nature géologique du sol et du régime hydraulique des eaux superficielles et souterraines, l'assainissement individuel ne peut présenter aucun inconvénient d'ordre hygiénique."
sanitation_relief_proposed = "L'obligation de réaliser des installations collectives ne s'applique pas pour l'assainissement lorsque, en raison de la grande superficie des parcelles ou de la faible densité de construction, ainsi que de la nature géologique du sol et du régime hydraulique des eaux superficielles et souterraines, l'assainissement individuel ne peut présenter aucun inconvénient d'ordre hygiénique."
relief_xml = replace_once('R111-11', water_relief_source, water_relief_proposed)
assert relief_xml.count(sanitation_relief_source) == 1
relief_xml = relief_xml.replace(sanitation_relief_source, sanitation_relief_proposed)
relief_xml += "\n<p>Les dispenses prévues aux deux premiers alinéas s'appliquent aux décisions prises à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris sur les demandes en cours sans nouveau dépôt ni reprise des délais. Les dérogations régulièrement accordées avant cette date conservent leurs effets. Le respect des conditions sanitaires et techniques demeure contrôlé dans les procédures légalement applicables.</p>"
rewrite(
    'R111-11', relief_xml,
    "Réduction de fond favorable : les deux possibilités discrétionnaires de dérogation deviennent des dispenses de droit lorsque leurs conditions de fond sont réunies. Le caractère exceptionnel de la dérogation d'eau potable disparaît. Tous les critères de superficie ou densité, facilité et économie nette de l'alimentation individuelle, potabilité, pollution, géologie, régime hydraulique et absence d'inconvénient hygiénique sont conservés. Ni nouvelle déclaration ni nouvel agrément ne remplace la décision favorable ; l'instruction sanitaire existante reste compétente.",
    "R. 111-8 à R. 111-10 et R. 111-12 lus ; le bénéfice porte sur l'obligation d'installations collectives, pas sur toutes les autorisations sanitaires ou de prélèvement d'eau d'autres codes. Ne pas présenter comme supprimée une procédure séparée que la source ne décrit pas : le changement démontré est l'abandon de la discrétion et de l'exceptionnalité, non le nombre d'autorisations initiales. Aucune baisse de taux ou de taxe n'est en cause. Le bénéfice est expressément ouvert aux décisions futures et aux demandes pendantes ; les dérogations antérieures subsistent sans nouvelle demande.",
    'material_reduction',
    "Les deux allègements existants deviennent opposables dès que leurs critères substantiels sont satisfaits. L'autorité ne peut plus les refuser pour leur seule nature dérogatoire ou, pour l'eau, l'absence d'exceptionnalité ; les garanties sanitaires de la source restent entières.",
    "Cette dispense ne supprime pas les règles sanitaires ni les contrôles autonomes et ne démontre pas qu'une autorisation distincte existait dans tous les cas. Les économies d'équipement sont propres à chaque projet.",
    "Aucune charge nouvelle n'est identifiée : mêmes conditions sanitaires, techniques et économiques, aucune attestation ou déclaration ajoutée. Le contrôle mentionné en transition est le contrôle existant, sans nouvelle procédure.",
    [effect(
        'relief_extended', 'urbanisme-derogations-reseaux-de-plein-droit',
        "Les deux dispenses d'installations collectives deviennent de droit : alimentation individuelle en eau potable et assainissement individuel, chacun sous l'ensemble de ses critères propres conservés.",
        "Eau potable : dérogation accordable à titre exceptionnel sous les critères de superficie ou densité, de facilité d'alimentation individuelle nettement plus économique, de potabilité et de protection contre toute pollution. Assainissement : dérogation accordable sous les critères de superficie ou densité, de géologie, de régime hydraulique et d'absence d'inconvénient hygiénique.",
        "Pour chacun des deux volets, l'obligation collective ne s'applique pas lorsque tous les critères qui lui sont propres sont réunis. L'exceptionnalité exigée pour l'eau et le pouvoir discrétionnaire d'octroi des deux dérogations disparaissent ; aucun critère sanitaire, technique ou économique conservé n'est retiré.",
        'regime', "Projets éligibles à l'alimentation individuelle en eau potable ou à l'assainissement individuel dans le champ de R. 111-11, selon leurs critères respectifs.",
        "Décisions après entrée en vigueur de la loi, y compris demandes pendantes sans nouveau dépôt ni reprise des délais ; les deux catégories de dérogations régulièrement accordées auparavant conservent leurs effets.",
        "Ni déclaration équivalente ni nouvel agrément ; prescriptions techniques et contrôles sanitaires existants maintenus. Aucune autorisation autonome d'un autre code n'est supprimée par cette mesure.",
        water_relief_source, water_relief_proposed
    )],
    removed=[
        "Caractère exceptionnel et pouvoir discrétionnaire d'écarter l'alimentation individuelle en eau malgré la réunion de toutes les conditions de la dérogation.",
        "Pouvoir discrétionnaire de refuser l'assainissement individuel alors que toutes les conditions sanitaires et techniques de la dérogation sont réunies."
    ],
    benefit="Deux avantages distincts sont conservés et renforcés : pour l'eau potable, dispense d'installation collective en cas de grandes parcelles ou faible densité, alimentation individuelle facile et nettement moins coûteuse, avec potabilité et protection contre toute pollution ; pour l'assainissement, dispense sous les critères de superficie ou densité, de géologie et de régime hydraulique assurant l'absence d'inconvénient hygiénique. Chacune devient de droit lorsque tous ses critères sont réunis. Elles restent ouvertes aux futures opérations éligibles et aux demandes en cours, et les dérogations régulièrement acquises conservent leurs effets. Aucun raccordement, déclaration ou agrément équivalent de remplacement n'est institué par cet article. Les contrôles et obligations sanitaires autonomes restent applicables."
)

retain(
    'R111-12',
    "Maintien intégral du traitement des eaux industrielles : séparation des eaux à épurer, prétraitement possible et réseau commun lorsque nécessaire au traitement d'une zone ou d'établissements groupés. La possibilité favorable de mélanger les eaux si la dilution ne crée aucune difficulté d'épuration est conservée pour toutes les situations futures éligibles. La supprimer aurait durci la règle ; supprimer les traitements aurait affaibli une protection essentielle de la salubrité et du milieu récepteur.",
    "Conserver les trois alinéas, le caractère conditionnel de l'autorisation de rejet dans le système de collecte, le prétraitement approprié et les deux destinations possibles du réseau industriel. Articulation avec R. 111-8 conservée ; les permis et autorisations environnementales ou sanitaires autonomes ne sont pas abolis. L'exclusion territoriale du RNU dans R. 111-1 reste applicable, sans retirer les normes d'autres codes.",
    "Aucun changement normatif : toutes les protections et la dérogation de mélange sont gardées. Le pouvoir d'imposer une desserte industrielle reste lié à l'épuration et au rejet, sans gain de simplification revendiqué.",
    "Le coût du prétraitement et des réseaux dépend de la pollution et du projet. Les régimes de rejet d'autres codes ne sont pas entièrement documentés dans le lot.",
    "Aucune charge nouvelle n'est identifiée : les mêmes traitements, possibilités de mélange et choix de destination subsistent, sans nouveau dossier industriel ou contrôle de remplacement."
)

cost_source = "Le projet peut être refusé si, par sa situation ou son importance, il impose soit la réalisation par la commune d'équipements publics nouveaux hors de proportion avec ses ressources actuelles, soit un surcroît important des dépenses de fonctionnement des services publics."
cost_proposed = "Le seul surcroît des dépenses de fonctionnement des services publics ne peut fonder un refus sur le fondement du présent article."
cost_xml = "<p>Le projet peut être refusé si, par sa situation ou son importance, il impose la réalisation par la commune d'équipements publics nouveaux hors de proportion avec ses ressources actuelles. " + cost_proposed + "</p>\n<p>Ces dispositions s'appliquent aux décisions prises à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris sur les demandes en cours, sans nouveau dépôt ni reprise des délais. Les décisions antérieures restent soumises au droit qui leur était applicable et aux voies de recours ouvertes ; aucun délai de recours expiré n'est rouvert.</p>"
rewrite(
    'R111-13', cost_xml,
    "Réduction de fond : suppression du motif autonome de refus tiré d'un simple surcroît important des dépenses de fonctionnement des services publics. La commune ne peut plus bloquer un projet sur ce seul fondement général. Le motif des équipements publics nouveaux hors de proportion avec les ressources actuelles reste entier, pour ne pas imposer des investissements matériellement insoutenables ; les obligations de desserte, d'eau, de sécurité et de salubrité restent distinctes. Aucune contribution compensatrice n'est créée.",
    "L. 111-11 lu conserve la condition de desserte par les réseaux nécessaires. R. 111-2 et R. 111-5 à R. 111-12 conservent sécurité, accès et eau. Limite importante lue dans le corpus : L. 111-4 4° garde sa condition autonome d'absence de surcroît important de dépenses publiques pour une construction exceptionnelle hors partie urbanisée ; cet article hors lot n'est pas implicitement modifié. R. 151-19, lu, incorpore R. 111-13 dans une option de règlement de PLUi : la réduction suit le renvoi, sans suppression de cette option. Les dépenses publiques réellement induites et les besoins d'équipement restent à évaluer, sans financement ou économie nationale présumé. Transition sans réouverture des décisions définitives.",
    'material_reduction',
    "La seconde branche de refus de la source disparaît pour les décisions futures : un surcroît de fonctionnement ne suffit plus au titre de cet article. La première branche relative aux équipements disproportionnés est maintenue sans nouvelle condition.",
    "Le coût des services publics n'est pas annulé et le solde public net n'est pas établi. La condition distincte de L. 111-4 4° subsiste ; la réforme ne garantit donc pas la constructibilité de tout projet hors partie urbanisée.",
    "Aucune charge nouvelle n'est identifiée : aucun paiement, étude de financement imposée au pétitionnaire ou contrat de compensation ne remplace le motif supprimé ; le test d'équipement existait déjà.",
    [effect(
        'obligation_removed', 'urbanisme-fin-refus-surcout-fonctionnement',
        "Retrait d'un obstacle autonome à l'autorisation tiré de l'augmentation des dépenses courantes de services publics.",
        "Le projet pouvait être refusé soit pour des équipements publics nouveaux disproportionnés, soit pour un surcroît important de fonctionnement.",
        "Seul le premier motif subsiste dans R. 111-13 ; le fonctionnement ne peut constituer à lui seul un motif de refus sur ce fondement.",
        'legal_duty', "Porteurs de projets relevant de R. 111-13, dans le champ territorial du RNU ou de ses renvois autonomes.",
        "Décisions après entrée en vigueur de la loi, y compris dossiers pendants ; décisions antérieures et délais de recours gardent leur régime.",
        "Aucun prélèvement ou financement obligatoire de remplacement ; desserte, équipements disproportionnés et régimes autonomes conservés.",
        cost_source, cost_proposed
    )],
    removed=["Motif autonome de refus du projet fondé sur le surcroît important des dépenses de fonctionnement des services publics."]
)

retain(
    'R111-14',
    "Maintien intégral après examen des trois motifs hors parties urbanisées : prévenir l'urbanisation dispersée incompatible avec les espaces naturels, protéger les activités agricoles et forestières ainsi que les sols et équipements, et préserver l'exploitation des ressources minières et de carrières identifiées par la loi. Les critères de compatibilité et de compromission évitent une interdiction indifférenciée. La protection d'espaces, de sols productifs et de ressources non renouvelables justifie de conserver ces conditions de fond plutôt que d'en faire une simple suppression de vocabulaire.",
    "Conserver 1°, 2° et 3° et l'alternative prescriptions/refus, avec les appellations d'origine contrôlée, indications géographiques protégées, aménagements fonciers et hydrauliques. L. 111-3 à L. 111-5 lus : leurs exceptions de constructibilité et avis distincts ne sont pas retirés ; R. 111-14 ne les remplace pas. R. 111-1 maintient l'exclusion de cette règle dans les territoires dotés d'un PLU. Les cibles minier L. 111-1 et L. 321-1 sont hors du corpus fourni ; leurs périmètres ne sont pas présentés comme vérifiés intégralement ni supprimés. Aucune origine SRU n'est présumée à partir du numéro.",
    "Les trois branches de la source restent intégrales : les protections spatiales et productives sont jugées nécessaires, sans nouvelle autorisation ni gain matériel revendiqué.",
    "Le corpus ne fournit pas les articles miniers ni tous les régimes d'espaces protégés. Le maintien n'établit pas leur absence de redondance générale, ni une réduction des contraintes de tout projet rural.",
    "Aucune charge nouvelle n'est identifiée : mêmes motifs, mêmes qualifications et mêmes possibilités de prescriptions ; aucun avis, quota ou donnée nouvelle n'est ajouté."
)

distance_source = "Une distance d'au moins trois mètres peut être imposée entre deux bâtiments non contigus situés sur un terrain appartenant au même propriétaire."
distance_proposed = "Pour les décisions prises à compter de cette entrée en vigueur, aucune distance entre deux bâtiments non contigus situés sur un terrain appartenant au même propriétaire ne peut être imposée sur le fondement du présent article."
distance_xml = "<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant la présente réforme. " + distance_proposed + " Cette suppression s'applique également aux demandes en cours, sans nouveau dépôt ni reprise des délais. Les renvois au présent article ne peuvent rétablir cette règle pour les décisions nouvelles.</p>\n<p>Les prescriptions des autorisations régulièrement délivrées avant cette date conservent leur régime, ainsi que leurs procédures de modification et leurs voies de recours. Les autres règles d'implantation, de sécurité et de salubrité ainsi que les droits des tiers demeurent applicables dans leur champ propre ; aucun nouveau délai de recours n'est ouvert contre une décision définitive.</p>"
rewrite(
    'R111-15', distance_xml,
    "Abrogation de fond pour l'avenir du pouvoir d'imposer une distance générale d'au moins trois mètres entre bâtiments non contigus d'un même propriétaire. Ce plancher uniforme peut bloquer divisions internes, extensions et densification sans risque particulier établi. Les risques réels restent traités par R. 111-2 et les règles de sécurité, et les autres règles de prospect et de limite parcellaire restent à leur champ ; aucune autorisation de dérogation ou déclaration de remplacement n'est créée.",
    "R. 111-1 coordonné dans ce lot. R. 111-16 à R. 111-19 et R. 151-19 ont été lus en entier : les trois mètres de R. 111-17 concernent la limite parcellaire et ne sont pas supprimés ; les dérogations de R. 111-19 aux règles restantes doivent demeurer ouvertes aux situations futures. Hors lot, remplacer dans les deux alinéas de R. 111-19 la borne R. 111-15 par R. 111-16, et dans R. 151-19 la plage R. 111-15 à R. 111-18 par R. 111-16 à R. 111-18, sans retirer l'option favorable de RNU des PLUi. Ces coordinations identifiées ne sont pas déclarées rédigées. Le texte interdit expressément de recréer la distance par un renvoi au fondement abrogé ; les règles locales autonomes et les prescriptions des permis antérieurs restent distinctes. Prévoir le véhicule réglementaire en Conseil d'Etat cohérent avec la date de la loi ; aucune date de promulgation n'est inventée.",
    'material_reduction',
    "Le pouvoir national de prescription d'une distance minimale interne de trois mètres est effectivement aboli pour les décisions nouvelles, et pas seulement différé. Les prescriptions antérieures et les distances d'autres fondements restent distinctes.",
    "L'abrogation ne supprime ni les prospects sur voie ou limite parcellaire, ni les distances fixées par un PLU autonome, ni les exigences de sécurité. Aucun nombre de logements supplémentaires ou gain national n'est démontré.",
    "Aucune charge nouvelle n'est identifiée : aucune déclaration, autorisation de rapprochement ou attestation compensatoire n'est créée. Les protections citées existaient déjà et ne constituent pas une nouvelle distance forfaitaire.",
    [effect(
        'obligation_removed', distance_measure,
        "Abolition du pouvoir d'imposer la distance interne nationale de trois mètres entre bâtiments non contigus du même propriétaire.",
        "Une distance d'au moins trois mètres pouvait être prescrite entre bâtiments non contigus sur le même terrain d'un même propriétaire.",
        "Aucune distance ne peut être exigée au titre de R. 111-15 pour une nouvelle décision ; les fondements autonomes de sécurité et d'implantation demeurent.",
        'legal_duty', "Porteurs de projets auxquels la règle de R. 111-15 s'appliquait directement ou par renvoi, notamment certains règlements de PLUi.",
        "Décisions après entrée en vigueur de la loi, y compris dossiers pendants sans nouveau dépôt ; prescriptions des titres antérieurs et voies ordinaires de modification protégées.",
        "Aucune démarche de remplacement ; les dérogations aux autres règles de distance sont préservées et les renvois ne peuvent faire revivre la règle abrogée.",
        distance_source, distance_proposed
    )],
    repeal_scope="Suppression pour les décisions futures du pouvoir d'imposer, sur ce fondement national, au moins trois mètres entre deux bâtiments non contigus d'un même propriétaire, sans supprimer les autres règles de sécurité ou de distance ni les prescriptions valables des titres antérieurs."
)


assert len(answers) == len(sources) == 24
result = [answers[a['number']] for a in sources]


def plain(xml):
    return unescape(re.sub(r'<[^>]*>', '', xml))


for source, a in zip(sources, result):
    for key in ('code_id', 'source_id', 'source_sha256', 'number'):
        assert a[key] == source[key], (a['number'], key)
    si = a['substantive_impact']
    assert si['version'] == 1
    for key in ('assessment', 'scope_limitations', 'new_burdens_review'):
        assert len(si[key]) >= 40, (a['number'], key)
    if a['status'] == 'retained_unchanged':
        assert a['proposed_xml'] is None
        assert a['classification'] == si['classification'] == 'retained_necessary'
        assert si['effects'] == []
    else:
        assert a['proposed_xml']
    if source['benefit_check_required']:
        assert len(a['benefit_review']) >= 100
    if a.get('change_type') == 'normative_reduction':
        assert a['reform_policy_id'] == 'editorial_direction_2026_10_19'
        assert all(len(x) >= 30 for x in a['removed_provisions'])
    if a.get('change_type') == 'full_repeal':
        assert plain(a['proposed_xml']).startswith(('Le présent article est abrogé', 'Abrogé'))
        assert len(a['repeal_scope']) >= 30
    effect_keys = [(e['measure_id'], e['kind']) for e in si['effects']]
    assert len(effect_keys) == len(set(effect_keys)), (a['number'], 'duplicate measure and effect')
    for e in si['effects']:
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', e['measure_id'])
        assert 6 <= len(e['measure_id']) <= 96
        assert len(e['source_quote']) >= 12
        assert len(e['proposed_quote']) >= 12
        assert e['source_quote'] in plain(source['source_xml']), (a['number'], 'source quote', e['source_quote'])
        assert e['proposed_quote'] in plain(a['proposed_xml']), (a['number'], 'proposed quote', e['proposed_quote'])

Path('answer.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'output_file': 'answer.json', 'article_count': len(result)}, ensure_ascii=False))
